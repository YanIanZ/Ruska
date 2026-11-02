# Architecture & Security Review Action Register

Status: OPEN design findings, not resolved implementation vulnerabilities. Do not close by documentation changes alone.

| ID | Severity | Problem | Required implementation acceptance |
|---|---|---|---|
| SEC-01 | High | Signed evidence is optional despite product positioning | Trusted signed manifest with negative tests or explicitly UNSIGNED fallback |
| SEC-02 | High | Demo cookie auth lacks complete CSRF and object authorization contract | Cross-session read, replay and forged approvals rejected |
| SEC-03 | Critical | URL allowlist can fail to prevent actual network egress | Destination enforced outside guest; metadata/private/redirect tests denied |
| SEC-04 | High | Worker impersonation/replay | mTLS/signed scoped envelope, nonce cache, expiration tests |
| SEC-05 | High | Shared-kernel container escape residual risk | Conditional microVM preference and real worker hardening/cleanup audit |
| ARC-01 | Medium | Mission-level SSE vs per-run event sequences disagree | Monotonic mission event stream OR change endpoint schema and tests |
| SPEC-01 | Medium | Evidence prose disagrees with integrity object placement | EVP-1 schema source of truth; contract tests |
| SPEC-02 | Low | JSON Schema IDs point at a different repo spelling | Change IDs to YanIanZ/Ruska and validate links |
| SAFE-01 | High | Browser prompt injection/SSRF | Owned mock portal only; deny policy tests |
| SCOPE-01 | High | Six-day scope has unrealistic breadth | Tier H passes before Tier S work |

Resolution requires code review, actual negative tests, evidence IDs and deployment checks. GitHub Draft PR stays unmerged pending owner review.
