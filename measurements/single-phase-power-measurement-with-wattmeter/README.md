# Single-phase power measurement with wattmeter

> Electrical Measurements lab (UNSE), May–Jun 2025. AC source, resistive/inductive loads, analog wattmeter with CT.

## Problem
Measure active power with a wattmeter and current transformer; compute S, Q, PF; correct for instrument power draw and estimate uncertainty.

## Setup
Wattmeter; voltmeter; ammeter via CT; selectable loads (motor and air conditioner).  
- photo: `figures/setup-AC.png`, `figures/setup-motor.png`  
- diagram: `figures/diagram-AC.png`, `figures/diagram-motor.png`

## Method
Recorded wattmeter indication Pm along with V and I; corrected for instrument power draw and CT ratio to obtain load power Pcarga. Computed S = UI, PF = P/S, and Q = √(S²−P²).

## Key results (Motor)
- **U = 220 V**, **I_c = 3.22 A**, **S = 708.4 VA**
- **R_VW ≈ 14.72 kΩ**, **R_V = 40 kΩ**, **CT ratio = 2:1**
- **P_carga = 215.5 W ± 3.916%** → **(215.5 ± 8.44) W**
- **Q_carga = 674.83 var**, **PF = 0.30**

## Key results (Air conditioner)
- **U = 233 V**, **I_c = 3.5 A**, **S = 815.5 VA**
- **R_VW ≈ 44 kΩ**, **R_V = 40 kΩ**
- **P_carga = 777.4 W**, **Q_carga = 246.35 var**, **PF = 0.95**

## What I learned / skills
Using CTs safely, wattmeter corrections, separating P/Q/S, spotting over-compensation artifacts, uncertainty propagation with angle terms.

## Files
- Report: [`report.pdf`](report.pdf) · Data/Figures/Code  
- Spanish report: [`TP6 - Medidas eléctricas - Chevauchey C.pdf`](es/TP6%20-%20Medidas%20el%C3%A9ctricas%20-%20Chevauchey%20C.pdf)

---

**My analysis approach**  
Accounted for wattmeter/voltmeter power draw, applied CT ratio, then propagated percent errors including wattmeter phase error.

*Licensing*: Code MIT. Docs/figures CC BY-NC 4.0.
