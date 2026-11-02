# Product Requirements Document — RUKSA RELIC v0.1

Status: PROPOSED / NOT IMPLEMENTED. Owner: YanIanZ. Hackathon: Vultr 3–8 Nov 2026. Track: Blast Radius Zero.

## 1. Problem and outcome
Reconstruct **observable user workflow behavior**, not a pixel clone. Given an operator-owned multi-step legacy form, RELIC outputs a modern accessible working interface and a reproducible parity test record. Never infer inaccessible server rules as certain.

## 2. Target personas
- Maintainer of an old institution or community portal without reliable original documentation.
- Accessibility advocate or designer tasked with making a public service easier to use.
- Engineering manager evaluating whether a legacy workflow can be modernized safely.

## 3. Primary user story
As an owner, I select the synthetic legacy service portal and click *Discover*. The agent explores it, creates a trace-based state machine, and shows what it observed vs inferred. I approve a bounded reconstruction. In a disposable environment it generates and builds new UI code and runs the same valid/invalid journeys. I inspect parity gaps and export the revived app and automated tests for engineering review.

## 4. MVP P0 features
- F1: Owned-site selector. Public app permits only project-hosted synthetic demo service; no arbitrary URL crawl.
- F2: Browser archaeology. Playwright captures page state, normalized DOM/accessibility tree, screenshots, field metadata, observed validation transitions and mocked responses.
- F3: Behavior Genome editor. Flow steps, field types, validation, expected outcomes, evidence refs, confidence class OBSERVED / HYPOTHESIS / UNKNOWN. Human corrects and approves.
- F4: Rebirth code generation. Vultr Serverless Inference proposes a constrained source patch/project in isolated workspace; sandbox validates package dependencies, builds and serves preview with no cloud/database credentials.
- F5: Parity Arena. Test harness replays fixed synthetic journeys against old and generated UI and compares normalized result payload, error messages, state sequence and completion.
- F6: Human handoff. Download generated source, observation trace, parity tests and migration checklist; never auto-publish.
- F7: Containment demonstration. Bounded time/memory/network enforcement and teardown with real traces.
- F8: Public Vultr-hosted web product UI and demo.

## 5. P1 stretch
- Keyboard path and automated axe-core accessibility regression metrics.
- Workflow diff timeline and interactive two-column before/after comparison.
- An alternate legacy sample workflow; source-free semantic reconstruction template.
- Self-contained Revival Capsule with versioned schema and optional Ed25519 signature.

## 6. P2 post-hackathon
- Authorized authenticated-site exploration and explicit consent scopes.
- Multi-role path exploration, security/privacy constraints and deeper API contracts.
- Human expert review, enterprise role model, git export / pull request creation and integration tests.
- Per-tenant policy and lifecycle management.

## 7. Explicit non-goals
No general arbitrary-web copying, no source reconstruction claims, no unauthorized third-party site mirroring, no production migration/cutover, no guarantee of complete behavioral parity, no legal accessibility certification. Demo only on owned synthetic fixtures.

## 8. Acceptance tests
A1: Original fictional portal supports ≥3 distinct flows including valid, invalid and boundary case.
A2: Agent-driven browser exploration really executes in isolated worker and records trace and screenshots.
A3: Generated UI project is an actual built artifact, not a static screenshot or hand-authored fake response.
A4: Paired E2E test independently asserts expected fixture outputs and labels uncovered states.
A5: A deliberately introduced rule discrepancy causes parity FAIL, not green success.
A6: Bounded malicious/runaway code is contained; control plane stays responsive; no secrets in sandbox.
A7: Public app on Vultr + Vultr Serverless Inference model calls recorded; demo, repo and docs visible.

## 9. KPIs (report measured values only)
Explored path count, known rule coverage, behavioral parity pass/total, accessibility regression checks, real sandbox runtime and cleanup, total time to generate, Vultr cost per run, manual review effort. Avoid extrapolating fixture parity to real-world sites.

## 10. User-facing terminology
OBSERVED = captured from the original owned demo; HYPOTHESIS = model guess not independently reproduced; UNKNOWN = outside coverage; PARITY PASSED = exact tested journeys agree; READY FOR REVIEW = not production-ready; REJECTED = mismatch/block.

## 11. RELIC 2.0 — Product depth addendum (not a new product)

**User outcome:** A maintainer can identify which exact hidden workflow rule is violated by a modern candidate and produce a reproducible minimal counterexample. The interface shows tested vs untested behavior; nothing is declared universally restored.

### Additional requirements
- CF-01: AI may propose **bounded safe probes** only for a registered, owned target; control plane decides exact execution capability and cost.
- CF-02: Behavior Genome records *source trace* and epistemic status for each rule (OBSERVED/INFERRED/UNKNOWN), plus the coverage denominator.
- CF-03: When parity differs, present the exact fixture input and both normalized outcomes; attempt bounded counterexample minimization on an isolated synthetic environment.
- CF-04: A Continuity Passport exports candidate revision, test code, environment, observed trace hashes, unresolved rules and required human sign-off.
- CF-05: The product never calls an untested workflow "restored"; security and functionality verdicts remain independent.

### Current executable prototype
The **offline** Python parity lab uses a handwritten model of the owned synthetic portal; it is not a substitute for P0 live Playwright, AI code generation or Vultr deployment. See [lab README](../examples/relic-lab/README.md). Two typed candidate specs make a failing vs passing conditional validation rule reproducible without network or dependencies.

### Acceptance extension
Wrong candidate threshold 10 fails the known urgent-description case; correct threshold 30 passes four fixture cases. The bounded 0–40 description probe finds a counterexample to the wrong candidate but none against the matching model in that range. This is **coverage of a limited mock**, not global behavioral parity.

See [Counterfactual Engine](43-COUNTERFACTUAL-ARCHAEOLOGY.md), [Passport](44-CONTINUITY-PASSPORT.md) and [two-speed delivery](46-RELIC-DELIVERY-SCORECARD.md).

### Test-target authenticity refinement
The original 2008-style fixture is served by a minimal local HTTP service with a server-side conditional validation rule. The browser-facing script cannot simply inspect a hardcoded threshold; a future observer must submit allowed synthetic inputs to discover it. This is an authored demo site and not actual archaeological recovery of an inaccessible production system. [Run instructions](../examples/legacy-community-portal/README.md).
