# Voltage doubler and quintuplicator (diodes)

> Electronics lab (UNSE), May 2025. 12 VAC half-secondary, breadboard builds.

## Problem
Build a diode-capacitor doubler and a quintuplicator, then observe output under load.

## Setup
Transformer 230→(12+12) VAC; diodes 1N4007; capacitors 1 µF/50 V; loads: 100 Ω/0.25 W and 100 kΩ/0.25 W; Rigol DS1052.

## Method
Assemble doubler, probe nodes across the two diodes and storage caps, then repeat for quintuplicator by extending the ladder. Test with loads to show sag under current draw and verify resistor power limits.

## Key results
- Doubler: output ~2·V_peak in light load; under **R=100 Ω** heavy sag, used only for demonstration.  
- Quintuplicator: high no-load DC; with **R=100 kΩ** the dissipation is safe (**~0.077 W** at 88 V), so the 0.25 W resistor is within limits.  
- Power checks done for candidate 1 kΩ showed it would far exceed rating; rejected.

## What I learned / skills
Charge-pump behavior, load regulation limits of multipliers, practical diode drops and capacitor ripple under load.

## Files
- Report: [`report.pdf`](report.pdf) • Spanish original in [`/es/TP2 - Electronica - Chevauchey C.pdf`](es/)
- Figures: [`figures/`](figures/)
- Code: [`code/`](code/)

---

**My analysis approach**  
Documented node voltages and load sag; computed resistor power to keep within ratings; contrasted doubler vs quintuplicator behavior under load.
