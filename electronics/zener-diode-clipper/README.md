# Zener clipper (dual thresholds)

> Electronics lab (UNSE), May 2025. Zener clamp with two thresholds, measured under different loads.

## Problem
Design a symmetrical clipper with two Zeners to clamp at about **+6.3 V** and **+4.6 V** equivalent thresholds.

## Setup
Zeners: 1N4732A (5.6 V), 1N4734A (3.9 V); series resistors 150 Ω/1 W ×2; transformer half-secondary 12 VAC; scope + DMM.

## Method
Anti-series Zeners with a current-limiting resistor; measure input/output. Repeat with a parallel load to show clamp current sharing and recompute Zener current from measured RMS on the load.

## Key results
- Thresholds: **5.6 V + 0.7 V = 6.3 V**, **3.9 V + 0.7 V = 4.6 V**  
- Series-resistor dissipation at peak current: **0.76 W** → 1 W part is adequate  
- With parallel load: measured **V_rms ≈ 5.31 V** across 150 Ω ⇒ **I_load ≈ 35.4 mA**  
- Zener current at that point: **I_Z ≈ 37.6 mA** (from 71 mA budget)

## What I learned / skills
Zener clamp design, sizing for Zener and resistor power, interpreting RMS under non-sinusoidal waveforms, sharing between Zener and load.

## Files
- Report: [`report.pdf`](report.pdf) • Spanish original in [`/es/TP3 - Electronica - Chevauchey C.pdf`](es/)
- Figures: [`figures/`](figures/)
- Code: [`code/`](code/)

---

**My analysis approach**  
Derived clamp thresholds using Zener plus diode forward drop, then closed the current budget from measured RMS to split load vs Zener current.
