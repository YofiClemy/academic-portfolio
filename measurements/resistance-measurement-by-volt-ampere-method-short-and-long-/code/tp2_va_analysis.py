
# TP2 analysis: volt-ampere method (short/long), insertion error model check
import pandas as pd
from pathlib import Path
from utils import check, data_dir_here

script = Path(__file__)
data_dir = data_dir_here(script)

df = pd.read_csv(data_dir / "tp2_combined.csv")
rows = []
for _, r in df.iterrows():
    Rm = r["Vm_V"] / (r["Im_mA"]/1000.0)
    Rx = Rm / (1 - r["ei_frac"])
    ok_rm = check(f"{r['topology']} Rm [Ω]", Rm, r["Rm_Ohm"])
    ok_rx = check(f"{r['topology']} Rx [Ω]", Rx, r["Rx_Ohm"])
    if r["topology"] == "short":
        ei_model = r["Rx_Ohm"] / (r["Rx_Ohm"] + r["RV_kOhm"]*1000)
    else:
        ei_model = - r["RA_Ohm"] / (r["Rx_Ohm"] + r["RA_Ohm"])
    ok_ei = check(f"{r['topology']} ei model", round(ei_model,6), r["ei_model_from_RV_RA"])
    rows.append({**r.to_dict(), "Rm_recomputed": Rm, "Rx_recomputed": Rx, "ei_model_recomputed": ei_model,
                 "ok_Rm": ok_rm, "ok_Rx": ok_rx, "ok_ei": ok_ei})
out = pd.DataFrame(rows)
out.to_csv(data_dir / "tp2_recomputed.csv", index=False)
print("Wrote", data_dir / "tp2_recomputed.csv")
