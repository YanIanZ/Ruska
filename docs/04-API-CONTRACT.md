# SUPERSEDED — Historical RUKSA Concept (NOT CURRENT SCOPE)

> Current product is **RUKSA RELIC**, the Autonomous Digital Restoration Studio. See [active PRD](32-RELIC-PRD.md), [architecture](33-RELIC-ARCHITECTURE.md), and [security](36-RELIC-SECURITY.md). The text below is retained for historical reference and must not be used as RELIC implementation instructions.

---

# API Contract — RUKSA HTTP v1

**Source of truth:** [`../schemas/openapi.yaml`](../schemas/openapi.yaml). API is proposed, not live.

## Conventions

- JSON over HTTPS, version prefix `/v1`, UTC ISO-8601 timestamps, IDs are UUIDv7/UUID strings.
- Authentication for public demo: scoped, expiring demo session; admin/worker endpoints private. Avoid hardcoding a universal demo secret in client assets.
- `X-Request-ID` assigned by server; `Idempotency-Key` mandatory on non-idempotent run and approval creation.
- Errors: `400` invalid request; `401` unauthorized; `403` policy denied; `404` absent/not visible; `409` invalid transition/conflict; `413` too large; `422` semantic invalid; `429` quota; `500` internal; `503` unavailable. Return stable error codes.
- Money is integer cents (`amount_cents`), with `currency` set to `USD` in demo. Never accept float money from model.

## Endpoints

| Method | Endpoint | Description | Response |
|---|---|---|---|
| `GET` | `/healthz` | Liveness only | `200` |
| `GET` | `/readyz` | Dependency readiness | `200/503` |
| `POST` | `/v1/missions` | Create mission referencing sanitized fixture/input IDs | `201 Mission` |
| `GET` | `/v1/missions` | Paginated list for current demo session | `200` |
| `GET` | `/v1/missions/{missionId}` | Mission metadata and latest state | `200` |
| `POST` | `/v1/missions/{missionId}/runs` | Start bounded orchestration | `202 Run` |
| `GET` | `/v1/missions/{missionId}/runs/{runId}` | Run status, phases and resource outcome | `200` |
| `GET` | `/v1/missions/{missionId}/events` | SSE progress; `Last-Event-ID` optional | `200 text/event-stream` |
| `GET` | `/v1/missions/{missionId}/findings` | Findings with verifier and evidence IDs | `200` |
| `GET` | `/v1/missions/{missionId}/evidence` | Manifest metadata and trace links | `200` |
| `POST` | `/v1/missions/{missionId}/approvals/{approvalId}` | Approve or reject exact draft digest | `200` |
| `GET` | `/v1/missions/{missionId}/report` | Generate/download structured JSON report | `200` |

Input uploads (when implemented) must be made via a constrained staged upload endpoint or deployment-hosted fixture selector. The initial demo can be fixture-first; do not falsely advertise production file upload before it exists.

## Example mission creation

```http
POST /v1/missions HTTP/1.1
Content-Type: application/json

{
  "title": "Reconcile November procurement invoices",
  "objective": "Find supplier pricing, duplicate invoice and missing PO exceptions",
  "dataset_id": "demo-2026-11-v1",
  "vendor_portal_url": "https://vendor-demo.example.test/"
}
```

```json
{
  "id": "018fae88-4abc-7654-9e22-c22ebedd4411",
  "status": "DRAFT",
  "dataset_id": "demo-2026-11-v1",
  "input_sha256": "<64-char-sha256-populated-by-server>",
  "created_at": "2026-11-03T16:00:00Z"
}
```

**Note:** example UUID/timestamp and placeholder digests are illustrative; not live data. A request cannot declare its own canonical digest.

## Example run creation

`POST /v1/missions/{id}/runs` with `Idempotency-Key: <uuid>` and body `{"execution_profile":"demo-constrained"}`. Returns `202` with run ID and `QUEUED`. A run may be rejected at policy check; client listens to SSE and does not assume success from `202`.

## SSE events

- Events have `id: <sequence>` and `event: mission.state | run.step | policy.decision | finding.created | run.terminal`.
- `data:` contains typed object `{event_id, mission_id, run_id, type, state, occurred_at, safe_payload}`.
- On reconnect send `Last-Event-ID`; server streams retained history when possible and otherwise instructs client to refetch current state.
- Do **not** stream raw model prompts, confidential source contents, sandbox stderr beyond sanitized excerpts, or infrastructure secrets.

## Approval mechanics

Action proposals are immutable and include `action_id`, `action_type=DRAFT_VENDOR_CLARIFICATION`, `payload_digest`, `requested_by`, and expiration. A user must present the exact digest being approved. `APPROVED` does not send email or spend funds in v1; it authorizes displaying/exporting the draft. If digest differs return `409` and force re-review.

## Input and data hygiene

Set bounded pagination (max 100); limit file upload by total bytes and MIME when implemented; reject CSV formula-injection output via escaping cells starting `=`, `+`, `-`, `@` in exported CSV. Use safe Content-Disposition filenames and virus/content screening for uploads in future real-data deployment.
