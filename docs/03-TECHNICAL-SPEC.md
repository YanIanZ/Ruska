# Technical Specification — RUKSA v1

## 1. Technology choices

- Web: Next.js/React/TypeScript, Tailwind or CSS modules, accessible component primitives; deploy on Vultr.
- API/orchestration: Go (stable supported version at implementation), HTTP JSON REST, SSE event stream.
- Data: PostgreSQL with migrations, query constraints and transactions; optional object storage for evidence bytes.
- Inference: Vultr Serverless Inference compatible API; model selection configurable via `VULTR_MODEL`.
- Runtime: isolated Python 3.x container and Playwright/Chromium container on a separate Vultr worker VM.
- Reports: structured JSON and CSV first; PDF after acceptance of core.

## 2. Repository target packages

```text
apps/web/                 # Next.js pages and API client
services/api/             # Go router, auth/session, upload, events
services/orchestrator/    # state machine, jobs, policy, inference adapter
services/verifier/        # deterministic financial and evidence verification
workers/supervisor/       # job acceptance, lifecycle and resource controls
workers/python-runner/    # ephemeral Python image without secrets
workers/browser-runner/   # ephemeral Playwright image
packages/contracts/      # JSON schemas and TS types generated from OpenAPI
infrastructure/vultr/    # provision/deploy scripts, network and firewall config
fixtures/synthetic/      # deterministic demo data, no real customers
```

These directories are **planned**, not present as implemented services in the initial docs-only repository.

## 3. Canonical arithmetic and comparison

Money represented as signed integer **cents** and ISO currency. Reject unknown currency, negative quantity and nonrepresentable decimals. For demo USD only. Normalization: `(vendor_id, supplier_invoice_number)` dedup key; `(po_id, sku)` unique PO line key. Each invoice row references a matching PO line; on mismatch, don't silently select a different line.

Algorithm (deterministic code):

```python
for invoice in invoices:
    key = (invoice.vendor_id, invoice.supplier_invoice_number)
    if key in previously_seen:
        record_duplicate(key, previously_seen[key], invoice.id)
    else:
        previously_seen[key] = invoice.id
    purchase_order = po_index.get((invoice.po_id, invoice.sku))
    if purchase_order is None:
        record_unknown_po(invoice.id)
        continue
    delta = (invoice.unit_price_cents - purchase_order.unit_price_cents) * invoice.quantity
    if delta > 0:
        record_price_variance(invoice.id, delta)
```

Use independent code path or separate fixture oracle to verify output, not an LLM assertion. Do not aggregate duplicate invoice value into price variance.

## 4. Plan evaluation

Plan must conform to `schemas/plan.schema.json`. Whitelisted tools only: `parse_documents`, `execute_python`, `browse_allowlisted_vendor`, `verify_findings`, `prepare_action_draft`. Reject dynamic shell commands, arbitrary URLs, unknown hostnames, scheduling loops and tasks that request secrets. All executed code is treated as untrusted even when produced by our own model.

## 5. Worker job contract

- Control-plane job envelope: job ID, mission and run IDs, input handles/digests, tool, constrained egress policy, max CPU/memory/PIDs/time/output bytes, policy revision, dispatch nonce, expiration.
- Worker response: `sandbox_id`, runtime name, started/ended timestamps, exit code, termination reason, bounded logs, output artifact descriptors/digests and resource observations.
- Worker does not receive LLM keys, PostgreSQL DSN, Vultr cloud API credentials, or signer private key.
- Browser navigation: allow only exact synthetic domain(s), validate IP and redirect targets at connect time; reject metadata service, RFC1918/link-local/private addresses unless explicitly isolated mock service on an isolated internal network.

## 6. API behavior

OpenAPI contract: [`../schemas/openapi.yaml`](../schemas/openapi.yaml). JSON errors use `{error:{code,message,trace_id,details}}`. Use `Idempotency-Key` for run creation and approval. `POST /v1/missions` accepts metadata and references to staged uploaded input artifacts; upload endpoint may be added by implementation or use multipart constrained by schema. Return `202` for async work; `GET /v1/missions/{missionId}/events` streams events.

## 7. State semantics

- Mission: `DRAFT -> QUEUED -> PLANNING -> AWAITING_POLICY -> EXECUTING -> VERIFYING -> NEEDS_REVIEW -> COMPLETED`; terminal alternatives `BLOCKED | FAILED | CANCELED` from eligible nonterminal states. Explicitly allow `VERIFYING -> COMPLETED` when no approval needed.
- Run: `QUEUED -> RUNNING -> VERIFYING -> SUCCEEDED | FAILED | BLOCKED | TIMED_OUT | CANCELED`. Separate cleanup flag `sandbox_destroyed_at` avoids conflating execution with resource teardown.
- Finding: `UNVERIFIED -> VERIFIED | INCONCLUSIVE | REJECTED`; no promotion without source and deterministic rule success.
- Approval: `PENDING -> APPROVED | REJECTED | EXPIRED`; exact action digest signed or recorded with actor/time.

## 8. Concurrency, consistency and failure

- One active run per mission in MVP. Server rejects conflicting starts with `409`.
- Retry maximum two transient inference/worker errors; no automatic retry for policy breach or arithmetic mismatch.
- Idempotency keys TTL 24h; repeated request returns same run ID.
- DB transitions use optimistic `version` and event outbox, monotonic SSE sequence per mission.
- Timeouts: inference 30s, sandbox 60s default, overall mission 180s (configurable and measured); reject unbounded plans.
- Error handling: fail closed, return actionable error without exposing infrastructure internals.

## 9. Environment configuration blueprint

| Var | Meaning | Secret? |
|---|---|---|
| `RUKSA_ENV` | staging/production | no |
| `DATABASE_URL` | PostgreSQL connection | yes |
| `VULTR_INFERENCE_API_KEY` | Vultr inference key, control plane only | yes |
| `VULTR_INFERENCE_BASE_URL` | `https://api.vultrinference.com/v1` | no |
| `VULTR_MODEL` | verified live model identifier | no |
| `WORKER_ENDPOINT` | private dispatcher endpoint | no |
| `WORKER_AUTH_TOKEN` | temporary demo only; prefer mTLS | yes |
| `EVIDENCE_SIGNING_KEY` | trusted signer key | yes |
| `SANDBOX_TIMEOUT_SECONDS` | default 60 | no |
| `DEMO_CONCURRENT_RUNS` | default 2 | no |

Do not commit `.env` or token values. Use structured secret injection and rotate compromised values.

## 10. Maintainability requirements

No direct API handlers invoking Docker. No model output sent to `sh -c` on control plane. No unvalidated arbitrary SQL or file path. All complex state transitions receive unit tests. Separate pure deterministic verifier from model-generated code and run it in a trusted, reviewable module with fixed schemas.
