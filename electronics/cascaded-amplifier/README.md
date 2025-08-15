# Cascaded amplifier (two EC stages)

> Electronics II (UNSE), May 2025. Two EC stages with interstage coupling, AC sweep.

## Problem
Design a two-stage amplifier to exceed **|A_v| ≈ 250** with reasonable Rout and stability.

## Setup
Two EC stages (BC337), interstage coupling capacitor, bias dividers per design; C_in, C_out chosen for f_min≈20 Hz; Rigol scope + generator.

## Method
Stage-wise design: pick I_C and V_E, compute r_e, select R_C and R_E; set dividers; add full bypass on stage 2 to meet gain while keeping stage 1 partially degenerated. Couple stages with C_AC sized from divider || input.

## Key results
- Designed small-signal gains: **A_v1 ≈ −26.19**, **A_v2 ≈ −10.38** → **A_v_total ≈ +272**  
- Lab/Sim sweep: first stage gain ≈ 24 falling to ≈ 18.5 by ~200 kHz; combined stages stabilize between **~260 and ~430** depending on frequency and loading.

## What I learned / skills
Gain stacking, interstage coupling design, pole placement and bandwidth, bias stability across stages.

## Files
- Report: [`report.pdf`](report.pdf) • Spanish original in [`/es/TP6 - Electronica - Chevauchey C.pdf`](es/)
- Figures: [`figures/`](figures/)
- Code: [`code/`](code/)

---

**My analysis approach**  
Computed each stage gain from r_e and R_C/(r_e+R_E’), verified Q in active region, then sized C_in/C_out/C_AC from effective input/output resistances and f_min target.
