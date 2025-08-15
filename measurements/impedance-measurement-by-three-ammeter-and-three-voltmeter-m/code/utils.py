
import pandas as pd
import numpy as np
from pathlib import Path

def abs_from_pct(val, pct):
    return val * (pct/100.0)

def pct_from_abs(val, abs_err):
    return 0.0 if val == 0 else 100.0*abs(abs_err)/abs(val)

def check(name, got, ref, tol=1e-3):
    ok = np.isfinite(got) and np.isfinite(ref) and abs(got - ref) <= tol
    status = "OK" if ok else "DIFF"
    print(f"{name}: {got:.6g} (ref {ref:.6g}) [{status}]")
    return ok

def data_dir_here(script_path):
    # ../data relative to this script
    return Path(script_path).resolve().parent.parent / "data"

def figures_dir_here(script_path):
    # ../figures relative to this script
    d = Path(script_path).resolve().parent.parent / "figures"
    d.mkdir(parents=True, exist_ok=True)
    return d
