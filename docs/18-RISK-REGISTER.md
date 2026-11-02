# SUPERSEDED — Historical RUKSA Concept (NOT CURRENT SCOPE)

> Current product is **RUKSA RELIC**, the Autonomous Digital Restoration Studio. See [active PRD](32-RELIC-PRD.md), [architecture](33-RELIC-ARCHITECTURE.md), and [security](36-RELIC-SECURITY.md). The text below is retained for historical reference and must not be used as RELIC implementation instructions.

---

# Risk Register — RUKSA Hackathon

Scores are qualitative planning estimates, not measured probabilities. **P:** likelihood; **I:** impact; H/M/L. Risk owner is assigned role, not confirmed individual.

| ID | Risk | P/I | Early signal | Mitigation / fallback | Owner |
|---|---|---|---|---|---|
| R01 | Vultr credit or VM provisioning delayed | M/H | No usable VM by end of Day 1 | Start docs and local fixtures; provision minimal VM; event support escalation | DevOps |
| R02 | Inference model lacks stable structured output | M/H | Plan fails schema repeatedly | Pick alternate supported Vultr model; reduce schema and validate; bounded retries | AI |
| R03 | Sandbox configuration unsafe | M/H | Host mounts/secrets/network leak | Block public release; test hardening on worker VM; remove generic code entry | Security |
| R04 | Browser SSRF/network restrictions unreliable | H/H | Can navigate internal/private host | Disable browser path; ship Pattern A only | Security |
| R05 | Demo costs exceed available credits | M/M | Rapid inference or VM spend | Rate limits, token caps, stop unused instances, reserve budget | DevOps |
| R06 | Fake sense of verification from signatures | M/H | UI calls everything “proven” | Separate hash-integrity vs business-rule verified; communicate limits | Product |
| R07 | Scope creep (multi-agent/ERP) | H/H | P0 not working by Day 3 | Freeze P1/P2, follow critical path | PM |
| R08 | Worker reliability / orphan containers | M/H | Dead jobs remain RUNNING | Lease expiry, cleanup reaper, terminal state reconciliation | Backend |
| R09 | Monetary or duplicate false positives | M/H | Oracle inconsistent | Integer-cent verifier and pinned fixtures; reject ungrounded claims | Data |
| R10 | Frontend polishing delays actual execution | H/H | UI polished, sandbox not live | Prioritize real execution proof ahead of animation | PM |
| R11 | Public demo abuse | M/H | Unexpected runs / spam | Demo fixture-only, rate limit, per-session quotas and kill switch | Security |
| R12 | GitHub/repo submission incomplete | M/H | No public repo or deck on Day 5 | Submission checklist, publish docs early and test anonymous access | PM |
| R13 | Code built before contest violates contest rules | L/H | Event-specific prohibition found | Check current rulebook; keep pre-event material as planning docs | PM |
| R14 | Name/trademark collision | M/M | Search finds conflicting commercial mark | Keep RUKSA provisional, do formal clearance later | PM |
| R15 | Evidence artifacts leak content | M/H | Screenshot/log includes sensitive data | Synthetic-only, redaction, short retention, storage access control | Security |

## Review cadence

Daily after build: adjust impact/likelihood based on evidence, link mitigations to tickets, record residual risk and release blockers. No risk can be closed merely because documentation exists. Any P0 security issue with High impact triggers a no-go until resolved and retested.

## Trigger-based fallback

- End Day 2 without real sandbox: stop UX work; resolve worker integration.
- End Day 3 without price verifier: stop browser automation; ship financial core.
- Any secret exposure: disable public deployment and rotate credentials immediately.
- Day 6 without full demo: record honest Pattern A code-only demo rather than fabricate browser output.
