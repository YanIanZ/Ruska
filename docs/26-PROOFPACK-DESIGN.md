# SUPERSEDED — Historical RUKSA Concept (NOT CURRENT SCOPE)

> Current product is **RUKSA RELIC**, the Autonomous Digital Restoration Studio. See [active PRD](32-RELIC-PRD.md), [architecture](33-RELIC-ARCHITECTURE.md), and [security](36-RELIC-SECURITY.md). The text below is retained for historical reference and must not be used as RELIC implementation instructions.

---

# ProofPack — Proof-Carrying Execution Design

Status: PROPOSED V2; existing EVP-1 JSON schema remains the binding v1 contract until an explicit migration.

## What ProofPack must answer
- What input snapshot and objective did the user authorize?
- What capabilities, cost/resource budgets and network targets did policy permit?
- What exact code/image was executed, in which sandbox, with which observed exit/cleanup status?
- What outputs were returned, which bytes are preserved, and what source rows support the finding?
- What did independent deterministic verification accept, reject or mark inconclusive?
- Who approved which exact action digest, if any?

## Receipt categories
MISSION, POLICY, EXECUTION, SOURCE, FINDING, VERIFIER, CONTAINMENT and ACTION_DRAFT. Each receipt has mission/run/step identifiers, timestamp, origin, content digest and versioned schema. The immutable snapshot digest binds provenance.

## Assurance must be multidimensional
1. execution_observed: a real run and its termination recorded (true/false/unknown).
2. integrity_status: UNSIGNED, SIGNED, or INVALID; hash/signature status only.
3. business_rule_status: VERIFIED, INCONCLUSIVE, REJECTED, NOT_RUN.
4. source_authenticated: TRUE, FALSE, UNKNOWN.
5. containment_status: PASSED, FAILED, NOT_RUN (specific test and environment).

No green VERIFIED label based solely on an LLM response, valid signature or screenshot. Signed FAILED runs are legitimate failure receipts; they never become successful work.

## Issuance path
Trusted Go control plane canonicalizes immutable input and the policy capsule before dispatch. Worker executes sandbox code with no signing, database or Vultr inference keys. Worker return values and screenshots are untrusted. Trusted Go verifier compares canonical invoice/PO input using integer cents. Only then does the trusted signer, when implemented and tested, sign deterministic canonical payload using JCS RFC 8785 and Ed25519. Verification checks signer public key, full artifact bytes, rule version and exact references.

## Required adversarial examples
- Invoice 42: (13800 - 12000) * 10 = 18000 cents; an agent-produced 19000-cent claim must be REJECTED.
- Modify one artifact byte => integrity INVALID.
- Swap source row references => INCONCLUSIVE or REJECTED.
- Sandbox times out => signed or unsigned *failure receipt*, never a successful output.
- Missing signing implementation => clearly UNSIGNED, never fabricated cryptography.

## Boundaries and migration
No TEE remote attestation unless hardware measurement actually exists. Signer compromise and forged source content are residual risks. Never call an ordinary log a cryptographic proof. A future V2 schema and offline verifier must be added alongside conformance tests; do not silently break EVP-1 or its existing JSON schema.
