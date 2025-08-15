# Three-phase power in balanced three-wire systems (Aron method)

> Electrical Measurements lab (UNSE), late May 2025. Two-wattmeter method with current transformers.

## Problem
Measure active power in a balanced three-wire system using two wattmeters (Aron method) and estimate combined uncertainty.

## Setup
Two analog wattmeters via CTs; three-phase balanced loads (R, RL, RC); lab three-phase source.  
- photo: `figures/setup-med.png`, `figures/setup-fase.png`, `figures/setup-traf.png`  
- diagram: `figures/diagram.png`

## Method
Read W1 and W2 and computed total active power Pc = Kt (W1 + W2), with Kt the CT ratio. Evaluated class and angle errors and propagated to Pc.

## Key results
- **W1 ≈ 1010 W**, **W2 ≈ 688 W**
- **Pc ≈ 3396 W**
- **Combined uncertainty: ~2.9%**

## What I learned / skills
Two-wattmeter method, interpreting W1/W2 sign changes vs load type, handling CT ratio and angle errors in the uncertainty budget.

## Files
- Report: [`report.pdf`](report.pdf) · Data/Figures/Code  
- Spanish report: [`TP7 - Medidas eléctricas - Chevauchey C.pdf`](es/TP7%20-%20Medidas%20el%C3%A9ctricas%20-%20Chevauchey%20C.pdf)

---

**My analysis approach**  
Summed wattmeters with CT ratio, validated sign with coil swap on reactive cases, then propagated meter classes into Pc.

*Licensing*: Code MIT. Docs/figures CC BY-NC 4.0.
