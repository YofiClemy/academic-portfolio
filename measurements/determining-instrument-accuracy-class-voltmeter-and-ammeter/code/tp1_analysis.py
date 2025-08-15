
# TP1 analysis: class from calibration
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from utils import check, data_dir_here, figures_dir_here

script = Path(__file__)
data_dir = data_dir_here(script)
figs_dir = figures_dir_here(script)

raw = pd.read_csv(data_dir / "tp1_readings.csv")
Xf = 1.2  # full-scale A

max_abs = raw["delta_A"].abs().max()
cls = 100*max_abs/Xf  # %

check("max |ΔX| [A]", max_abs, 0.01)
check("estimated class [%]", cls, 0.833)

# Plot calibration
plt.figure()
plt.plot(raw["Xp_A"], raw["Xm_A"], "o-", label="DUT vs Standard")
plt.plot([0,Xf],[0,Xf], "--", label="Ideal")
plt.xlabel("Standard Xp [A]")
plt.ylabel("DUT Xm [A]")
plt.title("TP1 Ammeter calibration")
plt.legend()
plt.tight_layout()
plt.savefig(figs_dir / "tp1_calibration.png", dpi=150)
