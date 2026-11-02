# Counterfactual Archaeology Engine — Design Spec

**Status:** Proposed runtime engine. An offline fixture-model laboratory is included as a small deterministic prototype; it is NOT evidence of live browser exploration, Vultr inference or sandbox isolation.

## Goal
From a small number of authorized observations, find useful next tests that reduce uncertainty about a **specific workflow contract**, without probing unrelated sites or exhausting the application.

## Inputs
- Registered project-owned workflow target ID and explicit operator authorization.
- Observation graph: states, supported actions, field selectors, input classes, source trace refs.
- Behavior hypotheses with evidence and confidence status: OBSERVED, INFERRED, UNKNOWN, DISPROVED.
- Per-run budget: max actions, pages, wall time, network destinations, synthetic submissions.
- Seeded safe input data and deterministic test oracle for the owned fictional portal.

## Exploration policy: information gain, not random crawling
1. Observe current state and enumerate only form controls in the allowlisted mock app.
2. Identify missing information: requiredness, conditional constraints, accepted length ranges, navigation error path, confirmation semantics.
3. Generate **safe, bounded input variants** around hypotheses: empty vs valid, exact boundary -1/at/+1, supported enum variations.
4. Rank probes by likely discriminatory value and coverage gain using known transitions; never invent actions outside the operator's allowed set.
5. Execute probes in a disposable browser using isolated synthetic fixtures with reset between runs.
6. Normalize outcome into abstract state, error class, confirmation payload; strip volatile IDs, timestamps and visuals without destroying semantics.
7. Reconcile observations with hypotheses; a single sample may confirm only that exact behavior under that input. Mark ambiguous or inaccessible rules UNKNOWN.
8. Produce a Behavior Genome with source evidence and an explicit coverage denominator.

## Counterexample minimization
When candidate output differs from the original on a bounded synthetic input, shrink the input while preserving mismatch (e.g. reducing a description length from 29 characters toward the smallest witness). Record the smallest found counterexample and the search bounds. This is a test aid, not formal proof of universal behavior.

## Strict safeguards
- Demo target MUST be project-owned, registered and unambiguously allowlisted; no arbitrary input URLs.
- The agent must not request or store authentication material, scrape private records, probe rate-limit defenses or bypass anti-automation.
- Only disposable fixture data; every form submit uses a dedicated synthetic backend/reset.
- Rate, time, action and total request budgets enforced by control-plane policy, never by prompt text alone.
- Browser network isolation must block metadata, private and foreign endpoints.
- DOM text is lower-trust data; cannot authorize new tools or resource limits.
- A supported path with uncertain back-end behavior is NOT "restored" until owner approves additional evidence.

## Proposed algorithm
\`\`\`text
hypotheses := infer_from(authorized_observations)
while steps_remaining and uncertain_rules:
  candidates := enumerate_safe_mutations(hypotheses, approved_actions)
  probe := rank_by_information_gain(candidates, budget, risk)
  observed := sandbox_browser.run(probe)
  hypotheses := update_evidence(hypotheses, observed)
return behavior_genome(observed, hypotheses, unknowns)
\`\`\`

The offline CLI under examples/relic-lab/ intentionally uses a **handwritten mock reference model**, so it can demonstrate deterministic candidate failures and minimum counterexamples without a browser. Actual Playwright integration is a separate P0/P1 implementation milestone.

## Acceptance contract
- Invalid candidate threshold detected.
- Exact boundary 29/30 semantics correctly identified in fixture oracle.
- A deliberately generated false positive/negative is reproducible with full test input.
- Covered and uncovered states are independently represented.
- Agent cannot expand target domains or execute an unbounded probe plan.
- Tests report trace/source IDs and model version; no implied universal correctness.

## More faithful black-box test target

The owned legacy portal now exposes \`POST /api/request\` with its conditional priority/description rule enforced in [server.py](../examples/legacy-community-portal/server.py), not the page's JavaScript. This makes the intended agent task genuinely observation-driven at the HTTP/browser surface, although the authored fixture source remains public in GitHub for transparency. The included Python HTTP tests verify the service behavior; they **do not** establish that a real AI has discovered the rule using Playwright.

Use the target only on loopback for local development or through a separately controlled owned demo service for Vultr browser worker integration.
