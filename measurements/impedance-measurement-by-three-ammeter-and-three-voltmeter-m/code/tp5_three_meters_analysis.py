
# TP5 analysis: three voltmeters and three ammeters
import pandas as pd, numpy as np
from pathlib import Path
from utils import check, data_dir_here, abs_from_pct

script = Path(__file__)
data_dir = data_dir_here(script)

v = pd.read_csv(data_dir / "tp5_3V_values.csv")
a = pd.read_csv(data_dir / "tp5_3A_values.csv")
comb = pd.read_csv(data_dir / "tp5_combined.csv")

# Verify absolute uncertainty calculations against percentages
def verify(method, col, pct_col):
    row = comb.loc[comb.method==method].iloc[0]
    abs_unc = abs_from_pct(row[col+"_Ohm"] if col in ["Zx","R","XL"] else row["P_W"], row[pct_col])
    name = f"{method} {col} abs_unc"
    ref = row[col+"_abs_unc_Ohm"] if col in ["Zx","R","XL"] else row["P_abs_unc_W"]
    check(name, round(abs_unc,2), ref)

# 3V
verify("three_voltmeters","Zx","Zx_abs_unc_Ohm")
verify("three_voltmeters","R","R_abs_unc_Ohm")
verify("three_voltmeters","XL","XL_abs_unc_Ohm")
verify("three_voltmeters","P","P_abs_unc_W")

# 3A
verify("three_ammeters","Zx","Zx_abs_unc_Ohm")
verify("three_ammeters","R","R_abs_unc_Ohm")
verify("three_ammeters","XL","XL_abs_unc_Ohm")
verify("three_ammeters","P","P_abs_unc_W")

# Dump a small file with deltas
rows = []
for _, row in comb.iterrows():
    rows.append({
        "method": row["method"],
        "Zx_check": row["Zx_abs_unc_Ohm"] - abs_from_pct(row["Zx_Ohm"], row["Zx_abs_unc_Ohm"]/row["Zx_Ohm"]*100 if row["Zx_Ohm"] else 0),
    })
pd.DataFrame(rows).to_csv(data_dir / "tp5_recomputed.csv", index=False)
