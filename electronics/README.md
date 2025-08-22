# Electronics II — Lab Portfolio (UNSE, 2025)

> Labs for **Electronics II** at UNSE (2025). Each subfolder includes a transladed report (`report.pdf`), an English summary (`README.md`), figures, and (when useful) small scripts to reproduce key calculations or plots.
> Original report in spanish can be found in /es

## Summary of labs

- **TP1 — Half-wave rectifier**
  - Built a 12 VAC half-wave rectifier. Measured waveforms at transformer, post-diode, and with reservoir capacitor. Verified load power against resistor ratings.
  - Insight: ripple is set by load current and C; diode drop and component power limits matter more than wishful thinking.
[Report.pdf](./half-wave-rectifier/report.pdf)

- **TP2 — Voltage doubler & quintuplicator (diodes)**
  - Implemented a 2x doubler and a 5x multiplier; compared no-load vs loaded outputs.
  - Insight: with more stages, output impedance skyrockets and “n×Vpk” only holds at tiny load currents.
[Report.pdf](./diode-voltage-doubler-and-quintuplicator/report.pdf)

- **TP3 — Zener clipper (dual thresholds)**
  - Symmetrical limiter targeting roughly +6.3 V / -4.6 V; tested with and without a parallel load.
  - Insight: clamp levels shift with Zener current and diode forward drop. Size the series resistor for IZ(min) and power.
[Report.pdf](./zener-diode-clipper/report.pdf)

- **TP4 — BJT Q-point**
  - Analyzed three bias topologies; placed Q using load lines; checked active/saturation/cutoff.
  - Insight: divider bias and emitter degeneration stabilize Q better than fixed bias; center Q for symmetric swing.
[Report.pdf](./transistor-q-point-quiescent-test/report.pdf)

- **TP5 — BJT amplifier (single stage)**
  - Designed CE amplifiers for target gains; swept ~20 Hz to ~3.2 MHz.
  - Results: |Av| ~ 7 for the stability-biased build; a second build ~ 18 at low frequency; roll-off follows device parasitics and bypass choices.
  - Insight: removing bypass trades gain for linearity and thermal stability.
[Report.pdf](./bjt-amplifier/report.pdf)

- **TP6 — Cascaded amplifier (two CE stages)**
  - Designed CE1 + CE2 with interstage coupling to exceed |Av| ~ 250.
  - Results: combined gain stabilized roughly **260–430** across the band; first stage ~ 24 falling to ~ 18.5 by ~200 kHz.
  - Insight: gain stacks and poles stack; interstage capacitor sizing and bias isolation matter.
[Report.pdf](./cascaded-amplifier/report.pdf)

- **TP7 — Op-amp: non-inverting amplifier + square-wave oscillator**
  - Built a non-inverting amplifier (Av ~ 20) and a relaxation oscillator (1–10 kHz).
  - Results: LM741 -3 dB ~ 50 kHz; TL081 ~ 175 kHz. Oscillator ran stably across the target range.
  - Insight: choose op-amp for GBW and slew; oscillator f ~ k/(RC) depends on hysteresis (beta) and supply rails.
[Report.pdf](./operational-amplifier/report.pdf)

## Skills & techniques applied

- **Diodes & rectification:** half-wave rectification, ripple vs C and load, diode-drop modeling, safe power checks.  
- **Voltage multipliers:** Cockcroft–Walton style ladders, stage-count trade-offs, load regulation limits, ESR/diode-drop effects.  
- **Clippers & clamps:** Zener biasing, IZ(min)/IZ(max), series-resistor sizing, clamp accuracy under load.  
- **Biasing & Q-point:** fixed vs divider bias, emitter degeneration, load-line analysis, handling beta variation.  
- **Small-signal BJT design:** r_e estimation, gain with/without emitter bypass, input/output impedance, coupling and bypass capacitors.  
- **Multi-stage amplifiers:** gain stacking, interstage coupling network, bandwidth and pole placement, phase through cascades.  
- **Op-amp practice:** non-inverting gain setting, comparator with hysteresis (Schmitt), RC timing, GBW-limited bandwidth.  
- **Measurement & validation:** oscilloscope setup, frequency sweeps, -3 dB identification, reconciling theory with lab data.  
- **Simulation:** quick checks in Proteus and Falstad to de-risk bench time.

## What I learned

1. **Specs vs reality:** diode drops, ESR, and beta scatter move targets; design margins are not optional.  
2. **Bias first, then gain:** a neat gain number is worthless if Q drifts or clips under signal.  
3. **Capacitors are strategy:** coupling, bypass, and reservoir capacitors each set different corners; size deliberately.  
4. **Stage count is a tax:** every added stage buys gain and sells bandwidth and stability.  
5. **Op-amps aren’t interchangeable:** GBW and slew dictate usable bandwidth; TL081 outpaces LM741 as expected.  
6. **Measure like you mean it:** -3 dB, clamp levels, and ripple are measurement problems before they’re math problems.

## Folders

**Each folder includes:**  
`report.pdf` (English); 
`README.md` (English), <=1-minute read: Problem, Setup, Method, Key results, What I learned, Files); `figures/` (photos, schematics, scope screenshots); `data/` (CSV measurements or sweep points when applicable); `code/` (optional short scripts to recompute key results or make plots).
`/e` Original report (Spanish)

## Reproducibility

Where present, scripts in `code/`:
- load from `../data/`
- recompute the numbers listed in each README’s Key results
- write `*_recomputed.csv` and 1–2 figures to `../figures/`

> No code was used at the bench; scripts only reproduce calculations from the reports.

## Licensing

- **Code:** MIT  
- **Reports & figures:** CC BY-NC 4.0
