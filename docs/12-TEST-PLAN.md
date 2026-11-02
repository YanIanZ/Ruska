# Test Plan — Functional, Security and Submission

**Current status:** Planned, no live tests run. **Fixtures:** synthetic only. **Execution ownership:** owner/engineers; reports must include environment, version and reproducible steps.

## Test matrix

| ID | Test | Preconditions | Expected result | Release gate |
|---|---|---|---|---|
| UT-01 | Exact cent arithmetic | Reference fixture | INV-0042 delta = 18000 cents | P0 |
| UT-02 | Duplicate detection | Invoice 86/87 share vendor+supplier number | One duplicate pair finding | P0 |
| UT-03 | Unknown PO | Invoice row 121 unknown PO | Unknown-PO finding, not monetary | P0 |
| UT-04 | Ordinary records | 146 unaffected invoice records | No false exceptions | P0 |
| UT-05 | Bad CSV schema | Missing `po_id` column | Reject 422, no run | P0 |
| API-01 | Create + run mission | Valid fixture and session | 201 mission; 202 run; SSE terminal status | P0 |
| API-02 | Duplicate run request | Same idempotency key | Same run returned, not duplicated | P0 |
| API-03 | Invalid transition | Completed -> Executing | 409 and no mutation | P0 |
| API-04 | Cross-session evidence | Session B accesses session A | Denied; no artifact leaked | P0 |
| AI-01 | Vultr model call | Valid API key and model | Trace shows Vultr inference origin | P0 |
| AI-02 | Unknown tool in plan | Model proposes `shell_root` | Blocked before worker | P0 |
| AI-03 | Prompt-injection CSV | Untrusted cell requests secret | Ignored, policy enforced | P0 |
| RUN-01 | Python actual execution | Work VM online | Executed result, actual exit metadata | P0 |
| RUN-02 | Infinite-loop timeout | 5s test policy | Killed, cleanup and terminal state | P0 |
| RUN-03 | No secrets | Sandbox inspection | No inference key/DB URL/cloud token accessible | P0 |
| RUN-04 | Network block | Attempt to fetch metadata/private IP | Denied in sandbox | P0 |
| RUN-05 | Worker failure | Kill worker during job | Run fails/recovers boundedly; no stuck forever | P0 |
| EVD-01 | Good manifest verification | Known artifact bytes | All required hashes verify | P0 |
| EVD-02 | Tampered artifact | Modify one byte | Hash mismatch, not verified | P0 |
| EVD-03 | Wrong result claim | Agent claims $190 instead of $180 | Trusted verifier rejects | P0 |
| WEB-01 | Fresh session E2E | Public URL in incognito | Can complete fixture mission | P0 |
| WEB-02 | Keyboard only | No mouse | Can navigate findings and approve draft | P1 |
| WEB-03 | Refresh/reconnect | Run underway | Rehydrates via REST + SSE | P1 |
| BR-01 | Synthetic vendor browser | Approved mock URL | Screenshot and output logged | P1 |
| BR-02 | Browser redirect SSRF | URL redirects to private IP | Blocked | P1 (mandatory if browser enabled) |
| SUB-01 | Demo and URLs | Public deployment | Repo, video, slides, app all reachable | P0 |

## Fixture oracle

Run `python3 scripts/validate_fixtures.py` in this repo. The script checks static synthetic CSV dataset and seed findings. This is a **fixture checker only**, not proof of AI, sandbox or cloud integration. Expected: 150 invoices, 3 exception types, 18000 cents priced delta, one duplicate pair and one unknown PO. Record actual command output when executed.

## Required reports

Store dated execution reports outside secrets: test ID, git SHA, environment (`local/staging/prod`), input fixture version/digest, command or user steps, actual vs expected, pass/fail, trace ID, screenshots (sanitized), test operator, reason for waiver. No future-tense tests can be marked PASSED.

## Quality gate

**P0 must all pass**, especially real sandbox isolation, serverless inference source, actual executed work, public URL and containment demo. P1 may be skipped if documented. A failed security P0 test blocks deployment; it is not acceptable to hide the failure via UI fallback.

## Regression suite for each release

Schema validation -> deterministic fixture oracle -> Go unit tests -> API contract tests -> isolated worker negative tests -> frontend E2E -> live public smoke -> demo rehearsal. Prefer deterministic seeded tests over repeatedly querying a nondeterministic model for exact numbers.
