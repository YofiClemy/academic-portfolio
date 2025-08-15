
# TP3 analysis: comparison and substitution
import pandas as pd
from pathlib import Path
from utils import check, data_dir_here, abs_from_pct

script = Path(__file__)
data_dir = data_dir_here(script)

comp = pd.read_csv(data_dir / "tp3_comparison_readings.csv")
sub  = pd.read_csv(data_dir / "tp3_substitution_readings.csv")
comb = pd.read_csv(data_dir / "tp3_combined.csv")

Rx_comp = comp["Rx_kOhm"].iloc[0]*1000
Rx_sub  = sub["Rx_Ohm"].iloc[0]

check("Rx comparison [Ω]", Rx_comp, comb.loc[comb.method=='comparison',"Rx_Ohm"].item())
check("Rx substitution [Ω]", Rx_sub, comb.loc[comb.method=='substitution',"Rx_Ohm"].item())

# Write recomputed quick summary
out = pd.DataFrame({
    "method": ["comparison","substitution"],
    "Rx_Ohm_recomputed": [Rx_comp, Rx_sub]
})
out.to_csv(data_dir / "tp3_recomputed.csv", index=False)
