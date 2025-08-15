
# TP6 analysis: wattmeter corrected power (motor case)
import pandas as pd
from pathlib import Path
from utils import check, data_dir_here

script = Path(__file__)
data_dir = data_dir_here(script)

m = pd.read_csv(data_dir / "tp6_motor_values.csv")
U = m.loc[0,"U_V"]; I = m.loc[0,"Ic_A"]
Pm = m.loc[0,"Pm_W_used_in_error_panel"]  # 111 W
RVW = m.loc[0,"RVW_Ohm"]; RV = m.loc[0,"RV_Ohm"]
K = m.loc[0,"CT_ratio"]
# Correction as per your report: subtract instrument powers from K*Pm
Pc = K*Pm - (U**2)*(1.0/RV + 1.0/RVW)
check("Motor Pc [W]", round(Pc,2), m.loc[0,"Pcarga_W"])
pd.DataFrame([{"Pc_recomputed_W": round(Pc,2)}]).to_csv(data_dir / "tp6_recomputed.csv", index=False)
