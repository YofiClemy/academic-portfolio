# Logic systems — traffic lights in Proteus (optional HDL/testbench)

> Context: Undergraduate lab at UNSE.

## Problem

> Design and simulate a two-direction traffic light controller using a Moore FSM built from discrete TTL logic in Proteus. Two intersections run in lock-step with a 60 s cycle: Green 27 s → Yellow 3 s → Red 27 s → Yellow 3 s.

# Setup
Tools / instruments (simulation):
	•	Proteus 8 (virtual oscilloscope, logic analyzer, signal generator)
Core components (TTL):
	•	2× 74LS90 decade counters (units / tens)
	•	2× 74LS248 BCD → 7-segment decoders
	•	JK flip-flops (e.g., 74LS76/112) for lamp latches
	•	AND/OR/NOT gates for state decoding
	•	3-color “traffic light” indicators, dual 7-segment display
	•	1 Hz clock source (seconds)

## Diagram/photo: 
![Setup](figures/setup.pdf)

## Method
	1.	Timing spec → state table: define 27/3/27/3 second windows and the interlock between directions.
	2.	Counters: cascade 74LS90 (00–59) and drive 7-seg via 74LS248 to show seconds.
	3.	Decode logic: AND/OR/NOT networks assert JKFF Set/Reset to drive R/Y/G per direction.
	4.	Simulation & probing: run at 1 Hz; verify durations with the logic analyzer and virtual scope.
	5.	Edge-case fix (V2): retime rollover decodes so both directions stay synchronized at 59→00.
	6.	(Optional) HDL/testbench: assert the lamp sequence from a 60-tick counter for automated checks.

## Key results
	•	Phase durations:
	•	Green: 27.0 s, Yellow: 3.0 s, Red: 27.0 s, Yellow: 3.0 s (total 60.0 s)
	•	Skew between directions: ≤ 0.0 s (lock-step after V2 retime)
	•	% error (timing): ≈ 0% at 1 Hz (digital, deterministic)
	•	Propagation margin: worst-case TTL path delay (ns) ≪ 1 s clock → huge timing slack

## What I learned / skills
	•	FSM design (Moore), synchronous timing & clocking
	•	TTL counters/decoders (74LS90 / 74LS248), JK flip-flop control
	•	Hazard/rollover debugging, clean decode retiming
	•	Proteus simulation, logic analyzer & scope usage
	•	Clear documentation and result validation
	•	(Optional) HDL/testbench for sequence assertions

## Files
	•	Report: report.pdf
	•	Data: data/
	•	Figures: figures/
	•	Code / Proteus project: proteus/


## My analysis approach
State assumptions → derive expected behavior → simulate nominal & edge cases → check timing windows → if mismatch, analyze hazards/propagation → retime logic → re-verify → document.

Licensing: Code MIT. Docs/figures CC BY-NC 4.0.