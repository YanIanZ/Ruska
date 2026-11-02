# Engineering Backlog

All future implementation tasks are OPEN unless linked to passing runtime checks.

| ID | Priority | Owner Role | Work | Acceptance |
|---|---|---|---|---|
| CH-001 | P0 | DevOps | Provision 2 Vultr VMs and HTTPS | Reachable VM A control and VM B worker |
| CH-002 | P0 | AI | Vultr Serverless Inference adapter | Real typed model plan + source code |
| CH-003 | P0 | Backend | Go mission API, dispatch and policy compiler | Correct auth, idempotency, denied tool inputs |
| CH-004 | P0 | Security | Disposable isolated code guest + egress and quotas | Real cleanup, no secrets, timed-out process |
| CH-005 | P0 | Runtime | Execute generated synthetic agent Python | Real trace and source digest from guest |
| CH-006 | P0 | Verification | Independent global invariant checker | Rejects false/malformed traces |
| CH-007 | P0 | AI/Runtime | Typed patch + rerun in new guest | Reproducible before/after policy results |
| CH-008 | P0 | Frontend | Agent interleaving and counterexample visual | Product UI reflecting real telemetry |
| CH-009 | P0 | QA | Security and E2E negative tests | Fail closed; no fake PASS statuses |
| CH-010 | P0 | PM | Submission video, architecture, repo | Public URL, video with containment |
| CH-011 | P1 | Research | Differential schedule ranking | Measured against exhaustive bounded reference |
| CH-012 | P1 | Runtime | Second synthetic shared-resource failure | Separate acceptance dataset |
| CH-013 | P2 | Product | Enterprise staging workflow connector | Separate authorization and compliance analysis |

## Work gates
No new product scope until CH-001..CH-007 run on actual Vultr. No public code mode until CH-004 and CH-009 pass. The offline reference engine is the deterministic fixture, not an "AI implementation done" claim.
