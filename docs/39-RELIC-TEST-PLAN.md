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
