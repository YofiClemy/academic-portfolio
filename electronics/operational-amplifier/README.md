# Op-amp: gain-20 amplifier + square-wave oscillator

> Electronics II (UNSE), May 2025. LM741 non-inverting amplifier and RC relaxation oscillator.

## Problem
1) Build a non-inverting amplifier with **A_v = 20**.  
2) Design a variable-frequency square-wave oscillator between **1 kHz** and **10 kHz** with ~5 Vpp output.

## Setup
LM741; R_f and R_1 for non-inverting gain; RC network with positive feedback for relaxation oscillator; pot + series resistor for frequency span; scope + bench supply.

## Method
- **Amplifier:** A_v = 1 + R_f/R_1 ⇒ choose **R_f ≈ 19 kΩ**, **R_1 ≈ 1 kΩ**.  
- **Oscillator:** use Schmitt-trigger comparator + RC; with β = R1/(R1+R2) ≈ 0.5, frequency **f ≈ 0.455/(R·C)**. Choose **C = 10 nF**, **R ≈ 4.7 kΩ to ~50 kΩ** to span 10→1 kHz with a safety series resistor.

## Key results
- Non-inverting stage: nominal **A_v ≈ 20** with 1 kΩ/19 kΩ.  
- Oscillator range: with **C = 10 nF** and **R ≈ 4.7–50 kΩ**, **f ≈ 10 kHz → 1 kHz**.  
- Output swing around 5 V in the chosen supply rails (clipped by op-amp limits).

## What I learned / skills
Op-amp gain setting, Schmitt trigger design, RC timing vs hysteresis, practical limits of old-school LM741.

## Files
- Report: [`report.pdf`](report.pdf) • Spanish original in [`/es/TP7 - Electronica - Chevauchey C.pdf`](es/)
- Figures: [`figures/`](figures/)
- Code: [`code/`](code/)

---

**My analysis approach**  
Mapped the oscillator frequency law from β and RC, then selected a pot + fixed resistor to guarantee the requested 1–10 kHz span without dropping out.
