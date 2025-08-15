# Measuring resistances by comparison and by substitution

> Electrical Measurements lab (UNSE), May 2025. DC source, analog V/A, decade standard.

## Problem
Estimate Rx using (a) comparison with a voltmeter and (b) substitution with a standard plus ammeter; quantify uncertainty and compare.

## Setup
DC supply ~25 V; analog voltmeter (class 1, RV = 24.6 kΩ), analog ammeter; decade standard ~300 Ω.  
- photo: `figures/setup.png`  
- diagram: `figures/diagram.png`

## Method
Ran both methods, logged readings and meter specs, computed Rx and propagated class and appreciation errors.

## Key results
- Comparison method: **Rx ≈ 254.9 kΩ ± 15.759%**
- Substitution method: **Rx ≈ 493.3 Ω**
- Voltmeter internal resistance used for loading model: **RV = 24.6 kΩ**

## What I learned / skills
Comparison vs substitution tradeoffs, meter loading, uncertainty propagation.

## Files
- Report: [`report.pdf`](report.pdf) · Data/Figures/Code folders  
- Spanish report: [`TP3 - Medidas eléctricas - Chevauchey C.pdf`](es/TP3%20-%20Medidas%20el%C3%A9ctricas%20-%20Chevauchey%20C.pdf)

---

**My analysis approach**  
Modeled meter loading for comparison, used equal-indication substitution with a standard, propagated class and appreciation errors to percent uncertainties.

*Licensing*: Code MIT. Docs/figures CC BY-NC 4.0.
# Wheatstone bridge: resistance measurement

> Electrical Measurements lab (UNSE), May 2025. DC Wheatstone bridge.

## Problem
Measure an unknown resistance with a Wheatstone bridge and quantify uncertainty and relative error against a nominal.

## Setup
DC source; bridge arms around 500 Ω; null detector.  
- Diagram/photo: `figures/setup.png`  
- Block diagram: `figures/block-diagram.png`

## Method
Balanced the bridge and computed Rx from arm ratios; evaluated sensitivity and propagated instrument tolerances.

## Key results
- **Rx = 479.12 Ω**
- **Uncertainty: ± 8.227%**
- **Relative error vs 500 Ω nominal: 4.14%**

## What I learned / skills
Null methods, bridge sensitivity, uncertainty vs excitation and resistor tolerances.

## Files
- Report: [`report.pdf`](report.pdf) · Data/Figures/Code  
- Spanish report: [`TP4 - Medidas eléctricas - Chevauchey C.pdf`](es/TP4%20-%20Medidas%20el%C3%A9ctricas%20-%20Chevauchey%20C.pdf)

---

**My analysis approach**  
Used balance condition, computed combined sensitivity, propagated percent errors to Rx; cross-checked against nominal.

*Licensing*: Code MIT. Docs/figures CC BY-NC 4.0.
