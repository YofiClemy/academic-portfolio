
# TP7 analysis: two-wattmeter method (Aron)
import pandas as pd
from pathlib import Path
from utils import check, data_dir_here

script = Path(__file__)
data_dir = data_dir_here(script)

v = pd.read_csv(data_dir / "tp7_values.csv")
Pc = (v.loc[0,"W1_W"] + v.loc[0,"W2_W"]) * v.loc[0,"KT"]
check("Pc [W]", Pc, v.loc[0,"Pm_W"])
pd.DataFrame([{"Pc_recomputed_W": Pc}]).to_csv(data_dir / "tp7_recomputed.csv", index=False)
