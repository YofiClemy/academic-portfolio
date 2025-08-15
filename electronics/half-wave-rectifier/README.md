# Half-wave rectifier

> Electronics lab (UNSE), Apr 2025. Transformer 12 VAC secondary, scope on bench.

## Problem
Build a half-wave rectifier, observe the waveforms with and without a reservoir capacitor, and verify safe load power.

## Setup
Transformer 230→(12+12) VAC, 1 A; diode 1N4007; electrolytic 100 µF/25 V; loads 100 Ω/5 W and 1 kΩ/1.2 W; Rigol DS1052 scope.

- Photos/plots: `figures/` (input, post-diode, post-capacitor, loaded cases)

## Method
Measure VAC at the secondary, then insert rectifier and capacitor, probing nodes before/after the diode and at the capacitor. Compute required RL for 600 mA target, and verify power dissipation for available resistors.

## Key results
- Load for 0.6 A target (from 17.8 V peak): **R_L ≈ 29.66 Ω**, **P ≈ 10.68 W**  
- Safe use checks:  
  - 100 Ω/5 W → **I_max ≈ 178 mA**, **P ≈ 3.97 W**  
  - 1 kΩ/1.2 W → **I_max ≈ 17.8 mA** (safe)  
- Waveforms: rectified half-wave; with 100 µF reservoir, DC level rises with ripple consistent with load.

## What I learned / skills
Diode rectification, ripple vs. load, power checks against component ratings, scope probing of rectifier nodes.

## Files
- Report: [`report.pdf`](report.pdf) • Spanish original in [`/es/TP1 - Electronica - Chevauchey C.pdf`](es/)
- Data/figures: [`figures/`](figures/)
- Code (optional reproducibility): [`code/tp1_analysis.py`](code/)

---

**My analysis approach**  
Computed R and power from secondary peak, verified resistor ratings, and documented measured waveforms to match expected rectified shapes.

*Licensing*: Code MIT. Docs/figures CC BY-NC 4.0.
