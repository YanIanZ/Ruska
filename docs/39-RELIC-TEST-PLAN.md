# RUKSA RELIC — Acceptance & Negative Test Matrix

Status: NOT RUN. Evidence is required before marking any item passed.

| ID | Level | Test | Expected |
|---|---|---|---|
| D01 | P0 | Owned mock portal healthy, 3-step journey | Real browser reaches confirmation |
| D02 | P0 | Model proposes browser exploration via Vultr inference | Trace includes real model ID and actions |
| D03 | P0 | Browser executes in isolated sandbox | Sandbox process ID / runtime metrics and teardown observed |
| D04 | P0 | Behavior Genome marks untested rules | Inferred/unknown not promoted to observed |
| D05 | P0 | Generated code is compiled and hosted in sandbox | Real build artifacts and preview |
| D06 | P0 | Valid synthetic transaction old/new | Identical normalized outputs under fixture oracle |
| D07 | P0 | Missing required field old/new | Both reject with comparable category |
| D08 | P0 | Hidden threshold boundary | Candidate mismatch fails and repaired one passes |
| D09 | P0 | Uncovered API behavior | Mark UNKNOWN and withhold "complete parity" |
| D10 | P0 | Endless loop generated step | Stops at wall time and guest destroyed |
| D11 | P0 | Blocked private/metadata egress | Network enforcement denies |
| D12 | P0 | Host secret probe and cross-session attempt | Secrets unavailable; 403/404 as appropriate |
| D13 | P0 | Public web URL, Vultr VM/inference proof | Valid, observed live app; video includes containment |
| D14 | P1 | Keyboard-only generated form | Focus and error navigation usable |
| D15 | P1 | Axe automated accessibility checks | No new measured violations in seeded checks; not WCAG certification |
| D16 | P1 | Downloaded Revival Capsule source/tests | Unpack and reproduce fixture results |

Never fabricate test results or screenshots. Report commit SHA, observed run IDs, seed data and reason for any INCONCLUSIVE outcome. One failed critical security gate blocks publicly accessible sandbox execution.

## Offline baseline — a separate test tier, not live product evidence

- LAB-01: Correct typed candidate => four fixture cases PASS; zero mismatches in 41 bounded synthetic description-length probes.
- LAB-02: Wrong candidate => one fixture FAIL; at least one counterexample (the current wrong threshold 10 yields mismatches for lengths 10..29).
- LAB-03: Reject candidate JSON with unexpected keys, non-boolean requiredness or non-integer threshold.
- LAB-04: 29-character urgent description rejected by authored reference model; 30-character accepted.
- LAB-05: Reports must label browser, Vultr inference, sandbox containment and generated source build as **not tested**.

See [the runnable offline lab](../examples/relic-lab/README.md). These tests cannot replace live isolated Playwright/code execution tests in the earlier P0 matrix. CI passes only prove the fixture-level model experiment works.
