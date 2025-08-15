# Measuring resistances by comparison and by substitution

> Electrical Measurements lab (UNSE), May 2025. DC source, analog V/A, decade standard.

## Problem
Estimate Rx using (a) comparison with a voltmeter and (b) substitution with a standard plus ammeter; quantify uncertainty and compare.

## Setup
DC supply ~25 V; analog voltmeter (class 1, RV = 24.6 kΩ), analog ammeter; decade standard ~300 Ω.  
- photo: 
    - `figures/setup_comp.png`
    - `figures/setup_sub.png` 
- diagram: 
    - `figures/diagram_comp.png`
    - `figures/diagram_sub.png`

## Method
Ran both methods, logged readings and meter specs, computed Rx and propagated class and appreciation errors.

## Key results
- **Comparison method:** U = **25 V**, Uᵥ = **2.2 V** → **Rx = 254.9 kΩ ± 15.759%**
  - Absolute range: **(254.9 ± 40.14) kΩ**
- **Substitution method:** Iₚ = **11.1 mA**, Iₓ = **6.75 mA** → **Rx = 493.3 Ω ± 26.28%**
  - Absolute range: **(493.3 ± 129.7) Ω**

## What I learned / skills
Comparison vs substitution tradeoffs, meter loading, uncertainty propagation.

## Files
- Report: [`report.pdf`](report.pdf) · Data/Figures/Code folders  
- Spanish report: [`TP3 - Medidas eléctricas - Chevauchey C.pdf`](es/TP3%20-%20Medidas%20el%C3%A9ctricas%20-%20Chevauchey%20C.pdf)

---

**My analysis approach**  
Modeled meter loading for comparison, used equal-indication substitution with a standard, propagated class and appreciation errors to percent uncertainties.

*Licensing*: Code MIT. Docs/figures CC BY-NC 4.0.
