# RUKSA CHORD — Product Requirements Document

**Version:** 0.1 design · **Track:** Blast Radius Zero · **Status:** planned, not implemented. **Owner:** YanIanZ.

## 1. Problem and customer
Enterprises increasingly delegate workflow decisions to several autonomous agents. Each may have a valid role and act within approved permissions, yet shared state, stale reads, retries and scheduling can create an unsafe global outcome. Ordinary single-agent tests and prompt-injection reviews do not fully address coordination failures.

Target users: AI platform engineers, internal automation owners, operations engineers and QA leads responsible for approving multi-agent systems before deployment.

## 2. One-sentence value
Find a **minimal, reproducible collective safety failure** and validate a bounded coordination repair before a multi-agent workflow ships.

## 3. Novel product mechanisms (proposals)
- **Collective Invariant Contract (CIC):** user specifies global properties that must hold across agents, independent of each agent's allowed actions.
- **Interaction Fracture Search (IFS):** Vultr inference suggests hypotheses/schedules; an isolated execution worker runs bounded interleavings. The trusted checker ranks real failures and returns the shortest observed witness. Do not call it exhaustive for unbounded distributed systems.
- **Coordination Repair Compiler (CRC):** model proposes a typed change (atomic reservations, lock/lease, idempotency, compensation); human approves it, and a new worker replays baseline-vs-patch under the same synthetic input budget.
- **Collective Safety Report (CSR):** original plan, allowed actions, executed code hash, trace, failed invariant, reproduction schedule, patch diff, measured before/after results, containment receipt and unresolved cases.

## 4. Hackathon P0 user journey
1. Select **Synthetic Inventory Race** template: two independently permitted agents, one stock unit, one-item requests.
2. User presses Find Fracture. Vultr Serverless Inference plans a bounded test and generates or edits executable synthetic actors.
3. Trusted Go policy validates budget, tools, resource limits and output contracts, then dispatches code to disposable Vultr worker sandbox. The simulation must actually run: no pre-rendered report.
4. Trusted checker consumes raw trace, independently evaluates global stock invariant and highlights a reproducible failing schedule (both read before either commits).
5. User proposes a coordination fix, such as atomic check-and-decrement. Model outputs an approval-required patch; a new disposable sandbox executes it.
6. Parity view contrasts baseline and patch over the same 20 bounded schedule interleavings. Export actual report and failure trace.
7. **Containment moment:** deliberately run harmless unbounded test code in a separate disposable worker. Timeout and teardown are recorded while control VM remains responsive.

## 5. P0 feature requirements
| ID | Feature | Acceptance |
|---|---|---|
| P0-01 | Public web mission workspace on Vultr | Real HTTPS URL; live run progress |
| P0-02 | Vultr Serverless Inference model planner | Real model call, ID, latency, schema validation |
| P0-03 | Code writer and isolated executor | Generated code actually runs in a sandbox separate from Go app |
| P0-04 | Trusted global invariant checker | Rejects 18 naive violation schedules in bounded fixture; 0 after atomic patch |
| P0-05 | Minimal counterexample with replay | Exact actor/step order and state transitions reproduced |
| P0-06 | Guarded coordination patch | Explicit human review; no outside-world changes; new sandbox rerun |
| P0-07 | Containment and lifecycle | CPU/memory/wall-time constraints, no secrets, deny egress, teardown observed |
| P0-08 | Collective Safety Report | Manifest with run/commit/code digests, actual measurements, caveats |
| P0-09 | Submission | Public repo, URL, video containing containment and architecture |

## 6. P1 stretch
Second incident fixture: idempotency double-charge **simulated only**; dynamic interleaving prioritization; schedule visualization; browser-based test to complement Pattern A; alternative approved patch candidate comparison; offline verification tool.

## 7. P2 later
Integration with customer-owned multi-agent staging environments via contracts; concurrency fault injection; business policy templates; recurring pre-release regression; enterprise multi-tenancy, audit retention and role management.

## 8. Non-goals and ethics
No actual payment, inventory or customer mutation. No unapproved fuzzing of third-party services. No claim that a sampled/interleaved toy state machine establishes formal verification of production distributed systems. Do not label a locally simulated run as Vultr containment.

## 9. Measurement and no-go
Measure explored schedules, global invariant violations, failure reproduction, input/code digest, real worker termination, denial tests and cost/latency. A model explanation is not a verifier. Any secret leakage, worker escape, forbidden network access or unbounded execution blocks public code mode. 

## 10. Definition of done
The end-to-end production-style web app executes model-authored code safely on Vultr, returns real verified output, shows a before/after coordination counterexample, records a containment moment and ships a credible public submission. Current repo does not yet satisfy those conditions.
