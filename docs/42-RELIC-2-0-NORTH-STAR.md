# RUKSA RELIC 2.0 — Continuity Engineering

**Decision:** Keep RUKSA RELIC as the Autonomous Digital Restoration Studio. Expand depth, not breadth. **Status:** proposal for owner review; no new product implementation is asserted.

## The unsolved task
An old web application may still be essential even when its source code, original developers, tests and documentation are gone. A screenshot clone can look modern and silently violate the workflow: accept wrong inputs, lose confirmations, change validation and discriminate against keyboard users. RUKSA will preserve **what users can actually accomplish**, not the pixels.

## Stronger product thesis
RUKSA RELIC is an **AI laboratory for reconstructing observable software behavior**. It discovers an application by acting as a user, formulates hypotheses, chooses safe counterfactual experiments, generates an accessible replacement, and independently challenges the replacement. It exports an **Executable Continuity Passport**, which explicitly describes tested behavior, unknown behavior and failure boundaries.

### Three new breakthroughs to demonstrate
1. **Counterfactual Archaeology:** Instead of replaying a predetermined happy path only, the agent proposes the *next highest-information safe probe*. For a priority-dependent field, it tries missing/short/boundary/long descriptions and distinguishes actual validated behavior from untested guesses.
2. **Continuity Atlas:** A state/transition/rule matrix over the old and new software. Every node is marked OBSERVED, HYPOTHESIZED, DIFFERENT, MATCHED or UNKNOWN with evidence. It reports coverage denominator; never say "100% of software restored" from four tests.
3. **Executable Continuity Passport:** Human-auditable source code, original and candidate input/output traces, reproducible parity tests, supported behavior graph and untested-risk ledger. This is a migration artifact, not merely an AI-generated report.

## Non-obvious demonstration
Show an old 3-step fictional service portal whose urgent case requires a description >= 30 characters. The first AI candidate wrongly accepts a 10-character urgent description. Counterfactual Archaeology generates targeted probes, Parity Arena discovers the mismatch, then an actual generated/edited replacement is built and retested. The difference disappears **only for the tested coverage set**. The resulting report says what is still unknown.

## Scope distinction
- Hackathon P0: One owned legacy app, one bounded discovery policy, real browser observations and isolated code build, deterministic paired outcomes, visible unknown ledger, real containment.
- Stretch: automated probe selection from evidence, counterexample minimization, accessibility regression checks, code revision after failing parity.
- Beyond hackathon: support authorized legacy sites, authenticated flows with owner consent, more back-end behavior, human governance and phased cutover.

## Strongest defensible differentiation
Legacy modernization, browser automation, website cloning and AI code generation already exist. Our focus is *counterfactual probing + epistemic certainty controls + executable parity to preserve service continuity*. We do not claim a "world-first" or guaranteed reconstruction of private server rules.

## Metrics (measured after implementation)
- observed_rules / asserted_rules
- parity_passes / executed_cases and failed_cases
- unexplored states / discovered state graph
- source-linked evidence rate
- time-to-first-reproducible counterexample
- successful sandbox containment under the defined negative test suite
- keyboard and accessibility checks per workflow
- human-review time and estimated modernization effort on **declared** scope only

## User experience
Use one hero journey: **Discover → Challenge → Rebuild → Compare → Hand Off**. The interface should show an old site, a new site, a red failing behavioral difference, and an exported continuity passport. Avoid generic chat dashboards.
