
# TP4 analysis: Wheatstone bridge balance
import pandas as pd
from pathlib import Path
from utils import check, data_dir_here

script = Path(__file__)
data_dir = data_dir_here(script)

v = pd.read_csv(data_dir / "tp4_wheatstone_values.csv")
R1,R2,R3 = v.loc[0,["R1_Ohm","R2_Ohm","R3_Ohm"]]
Rx = (R2 * R3) / R1  # balance condition
check("Rx [Ω]", Rx, v.loc[0,"Rx_Ohm_rounded"])

pd.DataFrame([{"Rx_from_balance_Ohm": Rx}]).to_csv(data_dir / "tp4_recomputed.csv", index=False)
