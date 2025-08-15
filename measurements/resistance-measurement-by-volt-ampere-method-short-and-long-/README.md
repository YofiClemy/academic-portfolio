# Measuring resistances by the volt-ampere method (short and long connections)

> Electrical Measurements lab (UNSE), Apr 2025. DC source, analog meters.

## Problem
Measure an unknown resistance with the voltmeter–ammeter method using short vs long connections; quantify insertion error and pick the better topology.

## Setup
DC supply ~25 V; analog voltmeter (RV = 24.6 kΩ), analog ammeter (RA = 0.1 Ω).  
- setup: 
    - `figures/setup_long.png`
    - `figures/setup_short.png`  
- diagram:
    - `figures/diagram_long.png`
    - `figures/diagram_short.png`
- graph: `figures/graph.png`

## Method
Took V and I readings with both wiring topologies. Computed Rm = Vm/Im and corrected insertion errors using RV and RA to obtain Rx. Computed the inflection resistance RPi where both topologies yield equal insertion error.

## Key results
- Short connection: **Rx = 356.132 Ω ± 3.04%** → **(356.132 ± 10.828) Ω**
- Long connection: **Rx = 357.04 Ω ± 3.08%** → **(357.04 ± 11.001) Ω**
- Inflection point: **Rₚᵢ ≈ 49.648 Ω** (short preferred below Rₚᵢ, long above)

**Constants used**
- Voltmeter internal resistance **RV = 24.6 kΩ**
- Ammeter internal resistance **RA = 0.1 Ω**

## What I learned / skills
Voltmeter-ammeter topology tradeoffs, insertion error modeling, choosing topology by inflection threshold.

## Files
- Report: [`report.pdf`](report.pdf)  
- Data/Figures/Code: [`data/`](data/) · [`figures/`](figures/) · [`code/`](code/)  
- Spanish report: [`TP2 - Medidas eléctricas - Chevauchey C.pdf`](es/TP2%20-%20Medidas%20el%C3%A9ctricas%20-%20Chevauchey%20C.pdf)

---

**My analysis approach**  
Derived Rx for both topologies, propagated meter class and resolution, solved for RPi to justify topology selection.

*Licensing*: Code MIT. Docs/figures CC BY-NC 4.0.
