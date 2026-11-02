# Behavior Genome Protocol — Observable Workflow Archaeology

Status: Proposed schema for owned synthetic flows; not reverse engineering claims against third-party systems.

## What can actually be observed
- State: URL, visible and accessible control descriptions, hashed DOM fragment, screenshot digest, timestamp.
- Action: click, fill, select, navigate, submit; exact field alias and synthetic input.
- Transition: old/new state ID and result class.
- Contract: form requiredness, validation feedback, confirmation payload on controlled fixture.
- Provenance: run and sandbox identity, Playwright trace ref, synthetic fixture ID, authorization ID.

## Behavior Genome structure (illustrative, not an approved JSON Schema)
\`\`\`json
{
  "schema": "ruksa-behavior-genome-draft-1",
  "workflow": "community-service-request",
  "states": [
    {"id":"start","observed":true},
    {"id":"details","observed":true},
    {"id":"confirmation","observed":true}
  ],
  "rules": [
    {"id":"R1","claim":"service_type required","status":"OBSERVED","evidence":["trace-001"]},
    {"id":"R2","claim":"priority implies additional minimum text","status":"HYPOTHESIS","evidence":[]}
  ],
  "unknowns": ["other users, storage semantics, production backend"]
}
\`\`\`

## Required epistemic states
- **OBSERVED:** actually reproduced with controlled input and trace.
- **INFERRED:** suggested from interface semantics but untested; not accepted as parity fact.
- **DISPROVED:** tested and contradicted.
- **UNKNOWN:** cannot verify from available evidence.
Never convert inferred rules to observed based on repeated LLM explanations.

## Parity cases
Each case binds synthetic inputs + expected states + normalized side effect from an independent reference fixture:
1. Valid service request results in deterministic confirmation.
2. Missing required region fails with expected validation.
3. Boundary case: urgent report requires longer description; test both sides of threshold.
4. Invalid or hostile field content must be rendered as plain text and not execute scripts.

Comparator covers only these specific journeys; untested interactions remain UNKNOWN.

## Generated program format
Candidate UI is generated from a constrained component schema, may only call a mock project's same-origin API adapter, cannot install unrestricted shell dependencies without worker policy. Build must execute in disposable sandbox; no code or package install on control VM.

## Accessibility
Use semantic native form controls, correctly associated labels and validation, visible keyboard focus, sensible tab order and error summary. Run axe-core and keyboard path tests; automated checks are not proof of full WCAG 2.2 AA conformance.

## Export contract
Revival Capsule contains original behavior trace manifest, approved Genome, generated source, executable parity test code, case results, coverage gap ledger, rollback and limitations. Only human owner can authorize future deployment.
