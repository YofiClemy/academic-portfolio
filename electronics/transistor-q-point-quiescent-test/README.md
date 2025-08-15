# Transistor Q-point (three bias cases)

> Electronics lab (UNSE), May 2025. Hand-analysis + plots for bias networks.

## Problem
Find the quiescent operating point for three BJT bias networks and identify operating region.

## Setup
Given component sets for cases A, B, C with V_CC, divider values, and β.

## Method
Compute base current from divider or fixed bias, get I_C = β·I_B, then V_CE = V_CC − I_C·R_C (and − I_E·R_E when present). Compare against region boundaries.

## Key results
- **Case A (active):** R_B=33 kΩ, R_C=1 kΩ, V_CC=12 V, β=75 → **I_B ≈ 0.1 mA**, **I_C ≈ 7.5 mA**, **V_CE ≈ 4.5 V**
- **Case B (active):** R1=300 kΩ, R2=200 kΩ, R_C=22 kΩ, V_CC=18 V, β=12 → **I_B ≈ 54 µA**, **I_C ≈ 0.65 mA**, **V_CE ≈ 3.7 V**
- **Case C (saturation-leaning by data):** R1=400 kΩ, R2=200 kΩ, R_C=1 kΩ, R_E=100 Ω, V_CC=25 V, β=100 → **I_B ≈ 53 µA**, **I_C ≈ 5.32 mA**, **V_CE ≈ 19.1 V**

## What I learned / skills
Bias math, load-line reasoning, placing Q for symmetric swing vs thermal stability.

## Files
- Report: [`report.pdf`](report.pdf) • Spanish original in [`/es/TP4 - Electronica - Chevauchey C.pdf`](es/)
- Figures: [`figures/`](figures/)
- Code: [`code/`](code/)

---

**My analysis approach**  
Worked each case from divider/fixed bias to Q, checked region by V_BE and V_CE, and used load-line sketches to verify.
