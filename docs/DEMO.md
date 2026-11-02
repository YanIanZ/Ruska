# CHORD Demo — The Failure Nobody Authorized

**Target:** ~3-minute tightly edited story, all execution real at submission time.

0:00–0:18 — "Both agents are compliant. The system is not." Show one fictional stock unit and two order agents.
0:18–0:40 — User asks Vultr-powered planner to find a coordination failure. Model produces bounded experiment/tool plan and generated Python code digest appears.
0:40–1:15 — Disposable Vultr worker actually executes it. Animated step timeline comes from real event records, not simulated UI.
1:15–1:40 — Highlight both agents reading stock=1, both locally deciding yes, and the second commit violating global invariant. Show exact replayable failing sequence.
1:40–2:05 — Model proposes typed atomic reservation. Human approves, new disposable worker reruns identical 20 schedules; trusted verifier compares.
2:05–2:35 — Separate harmless endless loop in worker triggers actual timeout; container is destroyed; Go control service stays healthy. Show no credentials in guest and denied egress if tested.
2:35–3:00 — Download Collective Safety Report and explain enterprise staging benefit, disclosed limitations, and potential expansion.

## Show real evidence
Actual inference call, VM, source SHA, worker container ID, clock/resource limits, exit code, emitted trace and verifier verdict. If one of these is not built, do not show fabricated successful state. Backup video may show *previously recorded real execution* when labeled.

## Presentation differentiator
A visually clear "agent A green / agent B green / system red" paradox, then exact counterexample, patch and retest. Never sell this as discovering a new class of concurrency bugs.
