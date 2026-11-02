# SUPERSEDED — Historical RUKSA Concept (NOT CURRENT SCOPE)

> Current product is **RUKSA RELIC**, the Autonomous Digital Restoration Studio. See [active PRD](32-RELIC-PRD.md), [architecture](33-RELIC-ARCHITECTURE.md), and [security](36-RELIC-SECURITY.md). The text below is retained for historical reference and must not be used as RELIC implementation instructions.

---

# Containment Theater — Ethical Demonstration

Goal: visibly prove measured sandbox limits, not show attacks on real services.

## Demo scenes
1. **Normal mission**: 150 synthetic invoices, three seeded exceptions, actual sandbox run, canonical source rows and code digest.
2. **Adversarial Twin Lite**: substitute a deliberately incorrect $190 claim for invoice 42. Independent verifier returns $180 and rejects fabricated claim.
3. **Runaway sandbox**: execute harmless endless loop with 5s test limit in disposable guest; capture exit reason, cleanup and control-plane health.
4. **Forbidden egress**: attempt benign connection to controlled private/reserved test address, show network policy deny event. Do not contact real cloud metadata.
5. **Prompt injection**: project-owned vendor HTML instructs exfiltration of a harmless sentinel; no tool capability grant; no outbound leak.
6. **ProofPack tampering**: mutate a copy of an artifact; digest/signature verification rejects changes; show honest source authentication unknown when appropriate.

## Evidence per scene
Record commit SHA, worker runtime type, timestamp, input digest, job capsule ID, signed/unsigned receipt, policy version, observed measurement, PASS/FAIL, screenshot/terminal trace (sanitized). Avoid unverified celebratory badges.

## Public safety gate
Any failed containment test disables the relevant public execution feature. Restrict demo to owned synthetic data and project-owned mock endpoints. No claim of zero exploits, external systems tested, or hardware attestation.
