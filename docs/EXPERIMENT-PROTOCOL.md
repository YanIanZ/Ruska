# Collective Safety Experiment Protocol — CHORD-CIC/1

**Status:** proposed wire design; Python offline engine is an example reference model, NOT a secure protocol implementation.

## Scope
Controlled testing of two synthetic inventory reservation agents, each with read/decide/commit steps. Input is a typed fixture, not arbitrary script, for the offline baseline.

## Collective Invariant Contract (CIC)
- Initial stock: one unit.
- Two agent identities with equal local permissions.
- Locally permissible decision: reserve only if last observed stock is >= requested quantity.
- Global requirement: remaining_stock never below zero and total committed reservations never above initial stock.
- Schedule budget: enumerate 20 step interleavings preserving each agent's own program order.
- The contract's scope is *this single in-memory process*, not real distributed transactions.

## Evidence categories
INPUT_SNAPSHOT (canonical JSON digest), MODEL_PLAN (Vultr model/version and plan hash, future), EXECUTION (code SHA, worker image hash, resource limit, exit/cleanup, future), STEP_TRACE (agent, action, read value, before/after state), CHECK (global invariant and rule version), REPLAY (exact schedule and outcomes), PATCH (typed proposal, owner approval and new execution run), CONTAINMENT (measured negative test).

## Local run
`python3 -m chord.cli --json` returns the complete offline trace and exposes explicit false flags for llm_called, vultr_vm_used, isolated_sandbox_used and containment_tested.

## Proof semantics
- "VIOLATED" iff a real state transition within the tested model breaks the declared predicate.
- "HELD" iff every enumerated schedule of the **bounded model** meets the declared predicate.
- A claimed minimal failure is a shortest observed failing prefix among the explored schedules, not necessarily a global optimum under all possible asynchronous/network behaviours.
- Atomic reservation guard passes the bounded fixture but does not imply universal prevention of coordination hazards.
- The model's description of the failure is never the authoritative test result.
- Each physical sandbox run must issue a fresh execution ID; retries and failures remain recorded.
- Reports with missing artifacts remain INCONCLUSIVE and must not claim VERIFIED.

## P0 acceptance
1. Baseline local enumerator: 20 unique schedules, naive violation count 18.
2. Guarded atomic model: 20 unique schedules, violation count 0.
3. Independently replay identified actor/step schedule reproduces the violation.
4. Future live worker: actor code executed inside disposable Vultr sandbox and actual source/trace hashes match report.
5. Tampered or missing trace is rejected by trusted checker.
6. Separate containment run proves wall-clock kill/teardown and control VM responsiveness.

## No external side effects
All resource names, inventory and orders are fictional. Model must not receive operational credentials or run against actual commerce backends.
