# RUKSA RELIC — Data & API Contract

**Status:** Proposed, not implemented. Machine spec: ../schemas/relic-openapi.yaml; typed observed behavior: ../schemas/behavior-genome.schema.json.

## Main entities
restorations(id, session_id, fixture_id, state, created_at); observations(id, restoration_id, run_id, action, from_state, to_state, trace_sha256); genomes(id, restoration_id, revision, content_digest, human_approved); candidates(id, restoration_id, source_digest, build_status, preview_ref); parity_cases(id, restoration_id, case_id, old_result, new_result, verdict); execution_jobs(id, restoration_id, runtime, policy_digest, status, cleanup_at); artifacts(id, owner_session, restoration_id, sha256, bytes, access_class); events(restoration_id, monotonic_seq, payload_safe).

## REST v1
POST /v1/restorations — create from fixed owned fixture ID.
GET /v1/restorations/{id} — session-scoped status.
POST /v1/restorations/{id}/discover — bounded browser exploration.
GET /v1/restorations/{id}/genome — evidence-linked behavior contract.
POST /v1/restorations/{id}/genome/approve — owner confirms exact digest.
POST /v1/restorations/{id}/generate — model produces candidate, build sandbox.
POST /v1/restorations/{id}/parity — paired browser journeys.
GET /v1/restorations/{id}/events — authorized SSE.
GET /v1/restorations/{id}/capsule — reviewed source and tests export.

All mutation endpoints require session owner, CSRF/Origin protection and bounded idempotency. No arbitrary website URLs in public demo.

## Fixture truth
fixtures/relic/behavior-cases.json defines four synthetic cases. Missing region => REGION_REQUIRED. Urgent priority + trimmed description < 30 characters => URGENT_DESCRIPTION_TOO_SHORT. Valid result => code REGION-ISSUE-PRIORITY uppercased. Fixture backend here is purely local. No real civic service is queried.

## Reliability
Mission-level monotonic event sequence, bounded retries, immutable run and candidate IDs, failed code-build remains failed rather than "restored". Behavior parity covers only observed journey set, not invisible backend logic.
