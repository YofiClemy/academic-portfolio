# run_study.py
# Minimal, robust feeder study:
# - Baseline LF + SC
# - OLTC test (only if a tap exists)
# - Shunt capacitor sweep at weakest bus
# - Targeted rebalancing on hot-trafo LV feeder
# - Small cap+rebalance combos
# - Snapshot all scenarios with action metadata
# - Pick smallest feasible fix (vmin>=0.95, vmax<=1.05, loadings<=100)
# - Re-apply "best" safely and run SC; then restore state
#
# Artifacts written:
#   figures/ …                      -> PNG plots
#   data/res_*.csv                  -> baseline results (LF, SC)
#   data/scenario_summary.csv       -> all scenario KPIs + actions
#   data/run_kpis__*.csv            -> baseline vs selected KPIs
#   data/best_scenario__*.json/txt  -> chosen action (metadata)
#   data/net_{before,after}__*.pkl.gz -> pandapower nets (portable)
#
# Reload a saved net later:
#   import gzip, pickle
#   with gzip.open("data/net_after__....pkl.gz","rb") as f: net = pickle.load(f)

from pathlib import Path
import sys
import math
import copy, os
import re, time
import warnings
import gzip, pickle

# 0) Headless plotting; use Agg backend so CI/servers with no display still save PNGs
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import pandas as pd
import pandapower as pp
import pandapower.networks as pn
import pandapower.shortcircuit as sc

warnings.filterwarnings("ignore", category=FutureWarning, module="pandapower")

# --- Env print (repro) --------------------------------------------------------
print("Using Python:", sys.executable)
print("Versions -> pandas:", pd.__version__)
print("pandapower:", pp.__version__)

# 1) Global limits + selection policy (tweak to your standards) ----------------
V_MIN_FLOOR = 0.95
V_MAX_CAP   = 1.05
LINE_MAX = 95.0
TRAFO_MAX = 95.0
POLICY = "avoid_rebalance"   # "avoid_rebalance", "min_cap", or "min_thermal"

# 2) Ensure output folders exist ----------------------------------------------
Path("figures").mkdir(parents=True, exist_ok=True)
Path("data").mkdir(parents=True, exist_ok=True)

# 3) Minimal, robust net saver (gzipped pickle) --------------------------------
def save_pp_net(net, path_base):
    """Save pandapower net to <path_base>.pkl.gz (single, reliable format)."""
    out_path = f"{path_base}.pkl.gz"
    with gzip.open(out_path, "wb") as f:
        pickle.dump(net, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Saved pandapower net -> {out_path}")

# 4) Build baseline network + steady-state power flow --------------------------
net = pn.create_cigre_network_mv(with_der=False)   # MV template (no DER)
pp.runpp(net)                                      # Baseline load flow (LF)

# 5) Baseline short-circuit (IEC 60909) ----------------------------------------
sc.calc_sc(net, case="max")                        # Baseline max-fault snapshot

# 6) Quick baseline voltage profile plot ---------------------------------------
try:
    plt.figure()
    if hasattr(pp.plotting, "plot_voltage_profile"):
        pp.plotting.plot_voltage_profile(net)      # Use helper if present
    else:
        vm = net.res_bus.vm_pu
        plt.plot(vm.values, marker="o")
        plt.axhline(V_MIN_FLOOR, ls="--"); plt.axhline(V_MAX_CAP, ls="--")
        plt.xlabel("Bus index"); plt.ylabel("Vm (pu)")
    plt.title("Voltage Profile (Baseline)")
    plt.savefig("figures/voltage_profile.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Voltage profile saved -> figures/voltage_profile.png")
except Exception as e:
    print("Voltage plot skipped:", e)

# 7) Baseline KPIs + CSV exports (for traceability) ----------------------------
print("---------------------------------------------------------------------")
print("Line loading mean %:", float(net.res_line.loading_percent.mean()),
      "Trafo loading mean %:", float(net.res_trafo.loading_percent.mean()))
print("---------------------------------------------------------------------")
net.res_bus.to_csv("data/res_bus.csv", index=False)
net.res_line.to_csv("data/res_line.csv", index=False)
if hasattr(net, "res_bus_sc") and not net.res_bus_sc.empty:
    net.res_bus_sc.to_csv("data/res_bus_sc.csv", index=False)
print("Exported res_bus/res_line/res_bus_sc -> data/*.csv")
print("---------------------------------------------------------------------")

vmin = float(net.res_bus.vm_pu.min()); vmax = float(net.res_bus.vm_pu.max())
print(f"Voltage pu: min={vmin:.3f}  max={vmax:.3f}")

lines = net.res_line.copy(); lines["name"] = net.line.name.values
hot_lines = lines.sort_values("loading_percent", ascending=False).head(5)
print("\nTop-5 lines by loading %:\n", hot_lines[["name","loading_percent"]])

trafos = net.res_trafo.copy()
trafos["name"] = net.trafo.name.values
trafos["sn_mva"] = net.trafo.sn_mva.values
trafos["headroom_%"] = 100 - trafos["loading_percent"]
trafos["s_mva_est"] = trafos["sn_mva"] * trafos["loading_percent"] / 100.0
print("\nTransformers:\n", trafos[["name","sn_mva","loading_percent","headroom_%","s_mva_est"]])
print("---------------------------------------------------------------------")

# 8) Helpers -------------------------------------------------------------------
def lv_feeder_load_indices(net, trafo_idx):
    """
    Return indices of loads electrically connected to the LV bus of `trafo_idx`.
    WHY: lets us “rebalance” by scaling only that LV feeder’s loads (not global).
    FALLBACK: if topology graph not available -> return all load indices.
    """
    try:
        from pandapower.topology import create_nxgraph
        import networkx as nx
        G = create_nxgraph(net, respect_switches=True)
        lv_bus = int(net.trafo.at[trafo_idx, "lv_bus"])
        comp = nx.node_connected_component(G, lv_bus)
        return net.load[net.load.bus.isin(comp)].index
    except Exception as e:
        print("Topology helper unavailable -> using ALL loads for rebalancing. Detail:", e)
        return net.load.index

def plot_network_stress(net,
                        line_thr=(70, 90, 100),
                        trafo_thr=(70, 90, 100),
                        annotate=True,
                        filename="figures/network_stress.png"):
    """
    Draw one “stress map” figure where:
      - Lines & trafos are colored by loading thresholds (green→purple).
      - Buses are red if Vm<0.95 pu.
    WHY: a one-glance visualization of thermal & voltage hotspots.
    """
    # Ensure solved results exist
    if (getattr(net, "res_bus", None) is None) or net.res_bus.empty or "vm_pu" not in net.res_bus:
        pp.runpp(net)

    # Ensure coordinates exist (generate if none)
    try:
        geodf = getattr(net, "bus_geodata")
    except AttributeError:
        geodf = None
    if geodf is None or getattr(geodf, "empty", True):
        try:
            from pandapower.plotting import create_generic_coordinates
            try:
                create_generic_coordinates(net, overwrite=True)
            except TypeError:
                create_generic_coordinates(net)
        except Exception as e:
            import pandas as _pd
            try:
                from pandapower.topology import create_nxgraph
                import networkx as nx
                G = create_nxgraph(net, respect_switches=True)
                pos = nx.spring_layout(G, seed=42, k=None)
                net.bus_geodata = _pd.DataFrame({
                    "x": [pos.get(int(b), (i, 0))[0] for i, b in enumerate(net.bus.index)],
                    "y": [pos.get(int(b), (0, i))[1] for i, b in enumerate(net.bus.index)],
                }, index=net.bus.index)
            except Exception as ee:
                raise RuntimeError(f"Could not create bus geodata (pp:{e}; fallback:{ee})")

    X = net.bus_geodata["x"]; Y = net.bus_geodata["y"]
    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    def color_for(val, thr):
        if val <= thr[0]: return "#2ca02c"   # green
        if val <= thr[1]: return "#ff7f0e"   # orange
        if val <= thr[2]: return "#d62728"   # red
        return "#7d3c98"                     # purple

    fig, ax = plt.subplots(figsize=(9, 7))

    # Lines colored by loading
    if hasattr(net, "line") and not net.line.empty:
        for i, row in net.line.iterrows():
            if not row.get("in_service", True) or i not in net.res_line.index:
                continue
            fb, tb = int(row.from_bus), int(row.to_bus)
            if fb not in X.index or tb not in X.index:
                continue
            load = float(net.res_line.at[i, "loading_percent"])
            c = color_for(load, line_thr)
            ax.plot([X.at[fb], X.at[tb]], [Y.at[fb], Y.at[tb]],
                    color=c, lw=2.5, alpha=0.95, zorder=2)
            if annotate:
                xm, ym = (X.at[fb] + X.at[tb]) / 2.0, (Y.at[fb] + Y.at[tb]) / 2.0
                ax.text(xm, ym, f"L{i}", fontsize=7, ha="center", va="center", color="#333")

    # Transformers colored by loading
    if hasattr(net, "trafo") and not net.trafo.empty:
        for i, row in net.trafo.iterrows():
            if not row.get("in_service", True) or i not in net.res_trafo.index:
                continue
            hv, lv = int(row.hv_bus), int(row.lv_bus)
            if hv not in X.index or lv not in X.index:
                continue
            load = float(net.res_trafo.at[i, "loading_percent"])
            c = color_for(load, trafo_thr)
            ax.plot([X.at[hv], X.at[lv]], [Y.at[hv], Y.at[lv]],
                    color=c, lw=3.5, ls="--", alpha=0.9, zorder=3)
            xm, ym = (X.at[hv] + X.at[lv]) / 2.0, (Y.at[hv] + Y.at[lv]) / 2.0
            ax.scatter([xm], [ym], s=70, c=c, marker="s", edgecolor="k", linewidths=0.5, zorder=4)
            if annotate:
                name = row["name"] if "name" in net.trafo.columns else f"T{i}"
                ax.text(xm, ym, name, fontsize=8, ha="center", va="bottom", color="#111")

    # Buses: flag undervoltage
    vm = net.res_bus.vm_pu
    bus_colors = ["#e74c3c" if float(v) < 0.95 else "#6c757d" for v in vm]
    ax.scatter(X.values, Y.values, s=12, c=bus_colors, zorder=5)

    # Legend + framing
    patches = [
        mpatches.Patch(color="#2ca02c", label=f"≤{line_thr[0]}%"),
        mpatches.Patch(color="#ff7f0e", label=f"≤{line_thr[1]}%"),
        mpatches.Patch(color="#d62728", label=f"≤{line_thr[2]}%"),
        mpatches.Patch(color="#7d3c98", label=f">{line_thr[2]}%"),
    ]
    ax.legend(handles=patches, title="Loading % (lines & trafos)", loc="best", frameon=True)
    ax.set_aspect("equal", adjustable="datalim"); ax.set_axis_off()
    ax.set_title("Network Stress Map (lines & transformers by loading)", fontsize=12)
    fig.tight_layout(); fig.savefig(filename, dpi=150, bbox_inches="tight"); plt.close(fig)
    print(f"Saved: {filename}")

def plot_voltage_profile_two(net_before, net_after,
                             filename="figures/voltage_profile_before_after.png",
                             labels=("Before","After")):
    """
    Side-by-side voltage profile comparison.
    WHY: shows how the chosen action lifted Vmin and kept Vmax in limits.
    """
    pp.runpp(net_before); pp.runpp(net_after)
    vm_b = net_before.res_bus.vm_pu.values
    vm_a = net_after.res_bus.vm_pu.values
    fig, ax = plt.subplots(figsize=(9,5))
    ax.plot(vm_b, marker="o", lw=1.5, label=labels[0])
    ax.plot(vm_a, marker="s", lw=1.5, ls="--", label=labels[1])
    ax.axhline(0.95, ls=":", lw=1); ax.axhline(1.05, ls=":", lw=1)
    ax.set_ylim(0.90, 1.07)
    ax.set_xlabel("Bus index"); ax.set_ylabel("Voltage (pu)")
    ax.set_title("Voltage Profile — Before vs After")
    ax.legend()
    fig.tight_layout(); fig.savefig(filename, dpi=150, bbox_inches="tight"); plt.close(fig)
    print(f"Saved: {filename}")

# 9) Scenario recorder (append KPIs + action metadata) -------------------------
snaps = []
def snapshot(label, **meta):
    """Capture LF KPIs for a scenario and embed the action we just applied."""
    row = {
        "case": label,
        "vmin": float(net.res_bus.vm_pu.min()),
        "vmax": float(net.res_bus.vm_pu.max()),
        "line_max_%": float(net.res_line.loading_percent.max()),
        "trafo_max_%": float(net.res_trafo.loading_percent.max()),
    }
    # Include each transformer loading by name (useful for reporting)
    tdf = net.res_trafo.copy(); tdf["name"] = net.trafo.name.values
    for i, r in tdf.iterrows():
        row[f"trafo_{tdf.at[i,'name']}_%"] = float(r.loading_percent)
    # Action defaults + override by meta (cap q, tap delta, rebalance factor…)
    row.update({"dtap": 0, "q_mvar": 0.0, "frac": 1.0})
    row.update(meta)
    snaps.append(row)

# 10) Baseline snapshot (reference row) ----------------------------------------
snapshot("baseline")

# 11) OLTC test (if taps exist): try +1/+2 steps, then restore -----------------
t_hot = net.res_trafo.loading_percent.idxmax()  # “hottest” trafo (for context)
tap_mask = ("tap_pos" in net.trafo.columns) and net.trafo["tap_pos"].notna()
tap_candidates = net.res_trafo[tap_mask].sort_values("loading_percent", ascending=False) if not isinstance(tap_mask, bool) else pd.DataFrame()

if len(tap_candidates):
    t_tap = tap_candidates.index[0]
    trafo_name = net.trafo.at[t_tap, "name"] if "name" in net.trafo.columns else f"trafo_{t_tap}"
    tap0 = int(net.trafo.at[t_tap, "tap_pos"])
    tmin = int(net.trafo.at[t_tap, "tap_min"]); tmax = int(net.trafo.at[t_tap, "tap_max"])
    step = float(net.trafo.at[t_tap, "tap_step_percent"])
    for delta in [1, 2]:
        new_tap = tap0 + delta
        if new_tap < tmin or new_tap > tmax:
            continue
        net.trafo.at[t_tap, "tap_pos"] = new_tap
        pp.runpp(net)
        print(f"OLTC {trafo_name}: +{delta} taps (~{step*delta:.2f}%) -> "
              f"Vmin={net.res_bus.vm_pu.min():.3f}, "
              f"Line max={net.res_line.loading_percent.max():.1f}%, "
              f"{trafo_name}={net.res_trafo.at[t_tap,'loading_percent']:.1f}%")
        snapshot(f"tap+{delta}", dtap=delta)  # record result
    net.trafo.at[t_tap, "tap_pos"] = tap0; pp.runpp(net)  # restore baseline
else:
    print("No transformers with defined OLTC -> skipping OLTC scenario.")

# 12) Capacitor sweep at weakest bus (0/1/2/3 MVAr), clean between tries -------
bmin = int(net.res_bus.vm_pu.idxmin())  # current lowest-voltage bus
for q in [0.0, 1.0, 2.0, 3.0]:
    sh = None
    if q > 0:
        sh = pp.create_shunt(net, bus=bmin, q_mvar=-q, p_mw=0.0, name=f"cap_{q}MVAr")
    pp.runpp(net)
    print(f"Cap {q:.1f} MVAr -> Vmin={net.res_bus.vm_pu.min():.3f}, "
          f"Line max={net.res_line.loading_percent.max():.1f}%, "
          f"Trafo_max={net.res_trafo.loading_percent.max():.1f}%")
    snapshot(f"cap_{q}MVAr", q_mvar=q, cap_bus=bmin)  # record cap scenario
    if sh is not None:
        net.shunt.drop(sh, inplace=True); pp.runpp(net)  # remove for next try

# 13) Targeted rebalancing on hottest trafo’s LV feeder (scale P only) ---------
def safe_lv_indices(net, t_idx):
    try:
        return lv_feeder_load_indices(net, t_idx)
    except Exception:
        return net.load.index

load_idxs = safe_lv_indices(net, t_hot)          # scope of loads to scale
oldP = net.load.loc[load_idxs, "p_mw"].copy()
for frac in [1.0, 0.95, 0.90, 0.85]:
    net.load.loc[load_idxs, "p_mw"] = oldP * frac
    pp.runpp(net)
    print(f"Rebalance x{frac:.2f} -> Vmin={net.res_bus.vm_pu.min():.3f}, "
          f"Line max={net.res_line.loading_percent.max():.1f}%, "
          f"Trafo_max={net.res_trafo.loading_percent.max():.1f}%")
    snapshot(f"rebalance_{int(frac*100)}pct", frac=frac, rebalance_trafo_idx=int(t_hot))
# Restore original loads after sweep
net.load.loc[load_idxs, "p_mw"] = oldP; pp.runpp(net)

# 14) Small combined grid (cap 1/2 MVAr) × (rebalance 0.95/0.90) ---------------
for q in [1.0, 2.0]:
    sh = pp.create_shunt(net, bus=bmin, q_mvar=-q, p_mw=0.0, name=f"cap_{q}MVAr_combo")
    for frac in [0.95, 0.90]:
        net.load.loc[load_idxs, "p_mw"] = oldP * frac
        pp.runpp(net)
        print(f"Cap {q:.1f} + Rebalance x{frac:.2f} -> "
              f"Vmin={net.res_bus.vm_pu.min():.3f}, "
              f"Line max={net.res_line.loading_percent.max():.1f}%, "
              f"Trafo_max={net.res_trafo.loading_percent.max():.1f}%")
        snapshot(f"cap_{q}MVAr+rebalance_{int(frac*100)}pct",
                 q_mvar=q, frac=frac, cap_bus=bmin, rebalance_trafo_idx=int(t_hot))
    # Clean up for next combo
    net.load.loc[load_idxs, "p_mw"] = oldP
    net.shunt.drop(sh, inplace=True); pp.runpp(net)

# 15) Persist all scenarios to CSV (single table of KPIs + actions) ------------
df = pd.DataFrame(snaps)
cols = ["case","vmin","vmax","line_max_%","trafo_max_%","dtap","q_mvar","frac"] + \
       [c for c in df.columns if c.startswith("trafo_")] + \
       [c for c in ["cap_bus","rebalance_trafo_idx"] if c in df.columns]
df[cols].to_csv("data/scenario_summary.csv", index=False)
print("Scenario summary -> data/scenario_summary.csv")

# 16) Filter feasible scenarios and pick “best” per POLICY ---------------------
feasible = df[
    (df["vmin"] >= V_MIN_FLOOR) &
    (df["vmax"] <= V_MAX_CAP) &
    (df["line_max_%"] <= LINE_MAX) &
    (df["trafo_max_%"] <= TRAFO_MAX)
].copy()

best = None
if feasible.empty:
    print(f"No feasible cases (vmin>={V_MIN_FLOOR}, vmax<={V_MAX_CAP}, line<={LINE_MAX}, trafo<={TRAFO_MAX}).")
else:
    # Ensure action columns exist for sorting
    for col, default in [("q_mvar", 0.0), ("frac", 1.0), ("dtap", 0)]:
        if col not in feasible.columns:
            feasible[col] = default

    # Selection logic:
    #  - "avoid_rebalance": prefer fixes that keep frac≈1, then minimal cap/tap
    #  - "min_cap":         minimize q_mvar; allow more rebalance if needed
    #  - "min_thermal":     minimize thermal peaks, then cap/tap
    if POLICY == "avoid_rebalance":
        no_rebal = feasible[feasible["frac"] >= 0.999]
        pool = no_rebal if not no_rebal.empty else feasible
        best = pool.sort_values(
            by=["q_mvar", "dtap", "line_max_%", "trafo_max_%", "vmin"],
            ascending=[ True,     True,   True,        True,          False]
        ).iloc[0]
    elif POLICY == "min_cap":
        best = feasible.sort_values(
            by=["q_mvar", "frac", "dtap", "line_max_%", "trafo_max_%", "vmin"],
            ascending=[ True,     False,  True,   True,        True,          False]
        ).iloc[0]
    elif POLICY == "min_thermal":
        best = feasible.sort_values(
            by=["line_max_%", "trafo_max_%", "frac", "q_mvar", "dtap", "vmin"],
            ascending=[ True,         True,          False,  True,     True,   False]
        ).iloc[0]
    else:
        raise ValueError(f"Unknown POLICY '{POLICY}'")

    # Small KPI file: baseline vs selected (easy to paste in reports)
    def _write_run_kpis(df_all, best_row, path):
        base = df_all[df_all["case"]=="baseline"].iloc[0][["vmin","vmax","line_max_%","trafo_max_%"]]
        sel  = df_all[df_all["case"]==best_row["case"]].iloc[0][["vmin","vmax","line_max_%","trafo_max_%"]]
        pd.DataFrame([
            {"phase":"baseline", **base.to_dict()},
            {"phase":"selected", **sel.to_dict()}
        ]).to_csv(path, index=False)

    print("Best candidate (LF):", best.to_dict())

    # Unique file name bits for this run
    case_slug = re.sub(r'[^a-zA-Z0-9]+', '-', str(best["case"])).strip('-').lower()
    run_id = time.strftime("%Y%m%d-%H%M%S")

    _write_run_kpis(df, best, path=f"data/run_kpis__{case_slug}__{run_id}.csv")

    # Persist decision metadata (JSON & friendly TXT)
    best_dict = dict(best)
    best_dict = {k: (None if pd.isna(v) else v) for k, v in best_dict.items()}
    Path("data").mkdir(exist_ok=True)
    pd.DataFrame([best_dict]).to_json(f"data/best_scenario__{case_slug}__{run_id}.json",
                                      orient="records", indent=2)
    with open("data/run_manifest.txt", "w") as f:
        f.write(
            f"policy={POLICY}\n"
            f"limits: Vmin>={V_MIN_FLOOR}, Vmax<={V_MAX_CAP}, line<={LINE_MAX}%, trafo<={TRAFO_MAX}%\n"
            f"case={case_slug}, run_id={run_id}\n"
        )
    with open("data/best_scenario.txt", "w") as f:
        f.write("BEST SCENARIO\n")
        for k, v in best_dict.items():
            f.write(f"{k}: {v}\n")

    print("Chosen action →",
          f"cap={best.get('q_mvar',0)} MVAr @ bus {best.get('cap_bus')}, ",
          f"rebalance×{best.get('frac',1.0)}, ",
          f"dtap={int(best.get('dtap',0))}")

    # 17) Apply chosen action, produce BEFORE/AFTER plots, SC, then restore ----
    os.makedirs("figures", exist_ok=True)

    # Keep a copy of the baseline network for comparison & saving
    base_net = copy.deepcopy(net)
    save_pp_net(base_net, f"data/net_before__{case_slug}__{run_id}")

    # Action engine: apply (cap, rebalance, tap) as encoded in `best`
    def apply_actions_for_row(net, row, load_idxs_default):
        pp.runpp(net)

        # 17a) Add shunt capacitor if requested (q_mvar>0).
        #      In pandapower, capacitive Q is entered as negative.
        q = float(row.get("q_mvar", 0.0) or 0.0)
        sh_id = None
        cap_bus_used = None
        if q > 0:
            cb = row.get("cap_bus", None)
            if cb is None or (isinstance(cb, float) and math.isnan(cb)):
                # Prefer current weakest bus; else LV bus of target trafo
                if "vm_pu" not in net.res_bus or net.res_bus["vm_pu"].isnull().all():
                    pp.runpp(net)
                if "vm_pu" not in net.res_bus or net.res_bus["vm_pu"].isnull().all():
                    t_idx = int(row.get("rebalance_trafo_idx", net.res_trafo.loading_percent.idxmax()))
                    cb = int(net.trafo.at[t_idx, "lv_bus"]) if "lv_bus" in net.trafo.columns else int(net.bus.index[0])
                else:
                    cb = int(net.res_bus["vm_pu"].idxmin())
            else:
                cb = int(cb)
            cap_bus_used = cb
            sh_id = pp.create_shunt(net, bus=cb, q_mvar=-q, p_mw=0.0, name="cap_best")

        # 17b) Rebalance: scale loads on target LV feeder by `frac` (≤1.0).
        frac = float(row.get("frac", 1.0) or 1.0)
        if "rebalance_trafo_idx" in row and row["rebalance_trafo_idx"] is not None and str(row["rebalance_trafo_idx"]) != "nan":
            try:
                reb_t = int(row["rebalance_trafo_idx"])
            except Exception:
                reb_t = int(net.res_trafo.loading_percent.idxmax())
            scope = lv_feeder_load_indices(net, reb_t)
        else:
            scope = load_idxs_default
        oldP = net.load.loc[scope, "p_mw"].copy()
        if frac < 1.0:
            net.load.loc[scope, "p_mw"] = oldP * frac

        # 17c) OLTC: if dtap!=0 and a tap-capable trafo exists, shift within limits.
        dtap = int(row.get("dtap", 0) or 0)
        tap_changed = False
        t_tap_used = None
        if dtap != 0:
            tap_mask = ("tap_pos" in net.trafo.columns) and net.trafo["tap_pos"].notna()
            tap_candidates = net.res_trafo[tap_mask].sort_values("loading_percent", ascending=False) if not isinstance(tap_mask, bool) else pd.DataFrame()
            if len(tap_candidates):
                t_tap = tap_candidates.index[0]
                tap0 = int(net.trafo.at[t_tap, "tap_pos"])
                tmin = int(net.trafo.at[t_tap, "tap_min"]); tmax = int(net.trafo.at[t_tap, "tap_max"])
                newtap = max(min(tap0 + dtap, tmax), tmin)
                net.trafo.at[t_tap, "tap_pos"] = newtap
                tap_changed = True
                t_tap_used = (t_tap, tap0)

        pp.runpp(net)
        return {
            "sh_id": sh_id,
            "cap_bus_used": cap_bus_used,
            "scope": scope,
            "oldP": oldP,
            "tap_restore": t_tap_used if tap_changed else None,
        }

    # Apply actions and re-solve
    state = apply_actions_for_row(net, best, load_idxs_default=load_idxs)
    pp.runpp(net)

    # Save AFTER state; create comparison plots
    after_net = copy.deepcopy(net)
    save_pp_net(after_net, f"data/net_after__{case_slug}__{run_id}")
    plot_voltage_profile_two(base_net, after_net,
                             filename=f"figures/voltage_profile__{case_slug}__{run_id}.png")
    plot_network_stress(base_net,  filename=f"figures/network_stress_before__{case_slug}__{run_id}.png")
    plot_network_stress(after_net, filename=f"figures/network_stress_after__{case_slug}__{run_id}.png")

    print("Applied:",
          {"q_mvar": float(best.get("q_mvar", 0.0) or 0.0),
           "cap_bus_used": state.get("cap_bus_used"),
           "frac": float(best.get("frac", 1.0) or 1.0),
           "tap_steps": int(best.get("dtap", 0) or 0)})

    # 18) Short-circuit (AFTER state) + export results -------------------------
    sc.calc_sc(net, case="max")
    if hasattr(net, "res_bus_sc") and not net.res_bus_sc.empty:
        net.res_bus_sc.to_csv(f"data/res_bus_sc__{case_slug}__{run_id}.csv", index=False)

    # 19) Cleanup: remove temporary changes and fully restore baseline ----------
    if state.get("sh_id") is not None:
        net.shunt.drop(state["sh_id"], inplace=True)
    if state.get("scope") is not None:
        net.load.loc[state["scope"], "p_mw"] = state["oldP"]
    if state.get("tap_restore") is not None:
        t_tap, tap0 = state["tap_restore"]
        net.trafo.at[t_tap, "tap_pos"] = tap0
    pp.runpp(net)

# 20) All done -----------------------------------------------------------------
print("Done.")