# Engineering Backlog and Acceptance Criteria

**Priority:** P0 submission-critical, P1 differentiation, P2 post-hackathon. **Task status:** all `TODO` by default. Assigned to owner/team only when confirmed.

| ID | Priority | Work item | Depends on | Acceptance evidence |
|---|---|---|---|---|
| INF-01 | P0 | Provision control VM and TLS reverse proxy | Vultr account | HTTPS health from public client |
| INF-02 | P0 | Provision isolated worker VM and private dispatch channel | INF-01 | Worker rejects unauthenticated request |
| INF-03 | P0 | Configure Vultr inference API adapter | INF-01 | Real model response, tokens/logged model ID |
| CORE-01 | P0 | Create Go API, migrations and DTOs | INF-01 | `go test` + migration smoke |
| CORE-02 | P0 | Implement mission lifecycle and transactional events | CORE-01 | Invalid transitions blocked under test |
| CORE-03 | P0 | Implement typed plan validation and policy gate | CORE-02, INF-03 | Unknown tools/URLs denied before dispatch |
| CORE-04 | P0 | Implement worker job and retry envelope | CORE-03, INF-02 | End-to-end dispatch idempotent |
| WORK-01 | P0 | Build nonprivileged Python image and supervisor | CORE-04 | Generated analysis code executes, exits, removed |
| WORK-02 | P0 | Apply cgroup/resource/time/network policy | WORK-01 | Infinite loop times out; key absent |
| DATA-01 | P0 | Parse and snapshot synthetic CSV fixtures | CORE-01 | 150 invoices validate and hash |
| DATA-02 | P0 | Deterministic PO matching in integer cents | DATA-01 | Price variance 18000 cents |
| DATA-03 | P0 | Duplicate and unknown PO detectors | DATA-02 | One duplicate pair, one unknown PO |
| EVD-01 | P0 | Record sandbox execution and source artifacts | WORK-01, DATA-01 | Every verified result links to source |
| EVD-02 | P0 | Trusted independent rule verifier | DATA-02, EVD-01 | Tampered amount rejected |
| WEB-01 | P0 | Dashboard / Mission create / execution timeline | CORE-02 | Clean-browser E2E passes |
| WEB-02 | P0 | Findings detail and evidence drawer | EVD-02 | Invoice/PO references visible |
| WEB-03 | P0 | Approval-gated action draft view | WEB-02 | Cannot send or mutate external systems |
| SAFE-01 | P0 | Containment, secret and SSRF negative tests | WORK-02 | Tests recorded and passed |
| OPS-01 | P0 | Logging, rate limit, quota, cleanup and error pages | CORE-02 | Public app doesn't expose raw logs/keys |
| SUB-01 | P0 | Record demo including verified containment | all P0 core | Video visibly shows actual policy outcome |
| SUB-02 | P0 | Publish public URL + docs + submission metadata | SUB-01 | Valid lablab confirmation |
| WORK-03 | P1 | Hardened Playwright browser for mock vendor portal | WORK-02 | Redirect/SSRF restriction tested |
| EVD-03 | P1 | Sign JCS canonical manifest with Ed25519 | EVD-02 | Tampered artifact and signature rejected |
| WEB-04 | P1 | Accessible containment monitor | WORK-02 | Shows real limits, teardown outcome |
| WEB-05 | P1 | CSV/JSON/PDF report export | EVD-02 | Export traceable and CSV sanitized |
| CORE-05 | P1 | Immutable mission replay | CORE-02 | New run, same snapshot digest |
| PROD-01 | P2 | Organization accounts / roles | Release 1.0 | Formal separate spec |
| PROD-02 | P2 | ERP/provider connectors | PROD-01 | Explicit consent and audit |

## Suggested GitHub issue batches

1. **Foundation:** INF-01..03, CORE-01, WEB-01.
2. **Mission safety and orchestration:** CORE-02..04, WORK-01..02, SAFE-01.
3. **Domain/value:** DATA-01..03, EVD-01..02, WEB-02..03.
4. **Demo/release:** OPS-01, SUB-01..02.
5. **Stretch:** WORK-03, EVD-03, WEB-04..05, CORE-05.

## Mandatory Definition of Done per ticket

- Changes implemented on feature branch with small reviewable commits.
- Unit/integration tests added or explained with reproducible manual verification.
- No secrets or non-synthetic private datasets checked in.
- Documentation/OpenAPI updated for public interfaces.
- Acceptance evidence linked to run or screenshot; failure/limitations honestly described.
- Security-sensitive changes reviewed for prompt injection, server-side request forgery and privilege escalation.

## Critical path policy

If the project falls behind by 12 hours, drop PDF and replay. If behind by 24 hours, drop optional browser feature. Never substitute fake execution logs for the real sandbox. If isolation is not working, fail launch instead of removing guardrails.
