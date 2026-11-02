# Execution Roadmap — 3–8 November 2026

**Internal final freeze:** 2026-11-08 18:00 WIB target (adjust after kickoff). **Official lablab deadline:** 2026-11-08 22:00 UTC / 2026-11-09 05:00 WIB. Check official dashboard immediately before submission. **Baseline:** 2026-11-02 design preparation; product implementation begins during competition.

## Prioritization rule

Critical chain: `Vultr VM + inference -> plan -> policy -> code sandbox -> deterministic findings -> evidence UI -> containment demo -> submission`. Everything outside this chain can be cut. Browser path is important differentiation but must not delay reliable Pattern A execution.

| Day | Focus | Deliverables | Exit gate |
|---|---|---|---|
| Day 1, Nov 3 | Bootstrap and infrastructure | Monorepo, Go API skeleton, Vultr VM, inference adapter, PostgreSQL schema, Next.js shell | TLS app/API reachable; test inference call through Vultr recorded |
| Day 2, Nov 4 | Real sandbox execution | Typed plan, dispatcher, worker VM, constrained Python runner, cleanup, SSE | Generated/specified Python runs in separate isolated worker; bounded output visible |
| Day 3, Nov 5 | Business domain | Fixture ingest, canonical PO lookup, pricing and duplicate checks, mission UI | Fixture produces precise expected findings, no fabricated data |
| Day 4, Nov 6 | Safety and provenance | Evidence protocol, signature/hash verification, timeout and prompt-injection demos, browser runner if stable | Containment behavior reproducible; no keys in sandbox |
| Day 5, Nov 7 | User-facing quality | Evidence Explorer, approval draft, error/retry UX, accessibility, report JSON/CSV, deployment hardening | Three successful E2E runs; manual QA with reproducible findings |
| Day 6, Nov 8 | Submission and reliability | Record demo, produce pitch slides/cover, final README, smoke tests, publish URL, submit via lablab | Public URL, repo, video, deck and lablab confirmation recorded |

## Daily activity blocks

### D1

- Verify scope/credits, choose Vultr region and VM plan with cost buffer.
- Create repo/branches and default MIT license; import docs and fixtures.
- First inference smoke test; record actual model ID (only after confirming live availability).
- Create DB migrations, liveness/readiness endpoints, artifact metadata.
- Establish release environment and safe demo session.

### D2

- Supervisor authentication, per-job nonce and policy budget.
- Container lifecycle create/start/log/kill/remove; verify file/memory/network restrictions.
- Worker-to-API typed envelope; job state transactions and idempotency.
- SSE and sanitized console; make one real executed analysis visible.

### D3

- Input parser; money in cents; duplicate and missing PO rules.
- Bench fixture truth-set comparison; create findings/evidence joins.
- Render stable result table and no-approval-by-default workflow.

### D4

- Sign manifest after trusted verification; verify artifact digests.
- Sandbox timeout and mock malicious supplier content tests.
- Browser sandbox limited to controlled portal only; if network policy is uncertain, disable browser in public UI.

### D5

- Polish operator journey and empty/error states.
- Validate no traces of real credentials in logs or frontend bundle.
- Collect metrics with measured baselines; optimize only after correctness.

### D6

- Record live mission showing input, plan, execution, evidence and containment.
- Run public URL test in clean browser; test responsive UI and keyboard path.
- Submission: GitHub, demo URL, cover, video, deck, tech tags, narrative.
- Freeze, no last-minute unrelated refactor; leave rollback path.

## Dependencies and fallbacks

- **Inference model unavailable:** choose another available Vultr Serverless Inference model; keep same typed schema and eval fixture.
- **Second VM unaffordable:** use isolated worker containers on Vultr host with explicit risk note; do not claim separate-host isolation. Sandbox remains mandatory.
- **Browser automation unsafe/unreliable:** ship Pattern A code-only pathway and include honest roadmap; Pattern B is optional according to official brief.
- **PDF report takes too long:** ship JSON/CSV and scriptable manifest verification; PDF is P1.
- **Cryptographic signing incomplete:** SHA-256 evidence hashes and transparent unsigned status; do not label proof as signed.

## Day-end proof of progress

At end of each day save: commit SHA, passed test logs (redacted), deployment URL/health state if available, current blockers and next day's gate. No `DONE` without a linked test or artifact.
