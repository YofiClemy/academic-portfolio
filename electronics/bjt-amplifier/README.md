# BJT amplifier (gain-20 and gain-15)

> Electronics lab (UNSE), May 2025. Single-stage EC amplifiers; design vs lab reality.

## Problem
Design EC amplifiers targeting |A_v| ≈ 20 and ≈15, then sweep frequency and compare to expectations.

## Setup
BC337; V_CC=15 V; resistors per design (see report); input/output coupling caps and optional emitter bypass; scope + variable-freq source.

## Method
Pick I_C, set V_E for thermal headroom, center Q on load line, compute R_C and R_E; choose divider R1, R2 for V_B; size C_in/C_out/C_E for f_min≈20 Hz. Build, then sweep ~20 Hz to 3.2 MHz and log |A_v|.

## Key results
- **Amplifier 1:** settled at **|A_v| ≈ 7** at low frequency without bypass; bandwidth roll-off: **−3.85** @ 500 kHz, **−2** @ 1 MHz, **−1** @ 2 MHz, **−0.75** @ 3.2 MHz.  
- **Amplifier 2:** design for |A_v| ≈ 15 with partial bypass; lab values documented in report plots; outcome limited by device parasitics and chosen bias.

## What I learned / skills
Q-point tradeoffs, emitter degeneration vs gain/stability, coupling capacitor sizing, measured frequency response vs small-signal model.

## Files
- Report: [`report.pdf`](report.pdf) • Spanish original in [`/es/TP5 - Electronica - Chevauchey C.pdf`](es/)
- Figures: [`figures/`](figures/)
- Code: [`code/`](code/)

---

**My analysis approach**  
Derived target R_E1 (unbypassed) for gain setpoint, split R_E into AC/DC parts, then matched lab sweep against the expected pole roll-off.
