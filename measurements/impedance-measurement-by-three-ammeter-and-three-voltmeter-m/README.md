# Measuring impedances: three voltmeters and three ammeters

> Electrical Measurements lab (UNSE), May 2025. AC source, analog meters, ballast load.

## Problem
Estimate a series RL impedance with the three-voltmeter and three-ammeter methods; compare results and uncertainties.

## Setup
AC source 0–250 VAC, ballast load; either three analog voltmeters or three analog ammeters; series standard resistor RP ~100 Ω.  
- photo: `figures/setup-3V.png`, `figures/setup-3A.png`  
- diagram: `figures/diagram-3V.png`, `figures/diagram-3A.png`

## Method
For 3V: measured U, UZ, and URP and solved for Zx, R, XL, φ, and P. For 3A: measured I, IZ, and IRP and derived the same quantities. Propagated class and appreciation errors for each method.

## Key results (3 voltmeters)
- **U = 144 V**, **U_Z = 62 V**, **U_RP = 129 V**, **R_P = 100 Ω**
- **φ = 89.1° ± 7.54%** → **(89.1 ± 6.72)°**
- **|Zₓ| = 208.06 Ω ± 5.63%** → **(208.06 ± 11.71) Ω**
- **R = 3.27 Ω ± 13.17%** → **(3.27 ± 0.43) Ω**
- **X_L = 208.03 Ω ± 5.63%** → **(208.03 ± 11.72) Ω**
- **P = 1.255 W ± 8.31%** → **(1.26 ± 0.10) W**

## Key results (3 ammeters)
- **I = 3.12 A**, **I_Z = 2.05 A**, **I_RP = 1.506 A**, **R_P = 105 Ω**
- **φ = 58.1° ± 18.21%** → **(58.1 ± 10.58)°**
- **|Zₓ| = 159.7 Ω ± 3.55%** → **(159.7 ± 5.67) Ω**
- **R = 84.39 Ω ± 21.76%** → **(84.39 ± 18.36) Ω**
- **X_L = 135.58 Ω ± 13.36%** → **(135.58 ± 18.11) Ω**
- **P = 217.82 W ± 12.74%** → **(217.82 ± 27.75) W**

## What I learned / skills
Vector treatment of AC measurements, method selection based on load and sensitivity, practical uncertainty propagation from derived quantities.

## Files
- Report: [`report.pdf`](report.pdf) · Data/Figures/Code  
- Spanish report: [`TP5 - Medidas eléctricas - Chevauchey C.pdf`](es/TP5%20-%20Medidas%20el%C3%A9ctricas%20-%20Chevauchey%20C.pdf)

---

**My analysis approach**  
Applied 3V and 3A formulas, enforced series constraints, then combined class and appreciation errors to obtain uncertainties; compared methods vs load behavior.

*Licensing*: Code MIT. Docs/figures CC BY-NC 4.0.
