# SUPERSEDED — Historical RUKSA Concept (NOT CURRENT SCOPE)

> Current product is **RUKSA RELIC**, the Autonomous Digital Restoration Studio. See [active PRD](32-RELIC-PRD.md), [architecture](33-RELIC-ARCHITECTURE.md), and [security](36-RELIC-SECURITY.md). The text below is retained for historical reference and must not be used as RELIC implementation instructions.

---

# Vultr Deployment and Operations Runbook

**This is a runbook for future implementation, not confirmation of deployment.** Credentials and public IPs must never be embedded in this repository.

## 1. Required services

- **Vultr Cloud Compute:** VM A for public app/backend/control orchestration; VM B for sandbox execution. Both are Vultr-hosted, as required for the challenge.
- **Vultr Serverless Inference:** required for every Blast Radius Zero LLM call, base URL `https://api.vultrinference.com/v1`.
- **Storage:** PostgreSQL on VM A or managed Vultr DB if budget allows; optional object storage for artifacts.
- **Domain and TLS:** public HTTPS for UI and API; use DNS pointed at control VM, certificate issuance and renewals.

## 2. Preflight

1. Register for lablab and Vultr; verify the gift code and whether credits were applied.
2. Check region/plan availability and actual per-hour price **in account console**. No assumed pricing in docs.
3. Select stable supported OS and provision VM A/VM B; create isolated/private network where available.
4. Firewall: expose 443 to internet on VM A; admin SSH via restricted source or managed access; VM B only reachable from VM A on necessary port; never expose DB/worker directly.
5. Configure OS updates, nonroot deployment user, inbound rate limits and system audit logs.
6. Confirm rootless Docker/needed runtime is supported on chosen VM; test cgroup and network restrictions locally before accepting arbitrary jobs.

## 3. Deployment topology

```text
Internet -> HTTPS reverse proxy -> Web / Go API (VM A)
                                    |-> PostgreSQL (private)
                                    |-> Vultr Inference HTTPS
                                    |-> Signed limited jobs -> Worker supervisor (VM B)
                                                              -> disposable containers
```

The control server must never grant the browser direct access to Docker or the worker supervisor. Keep inference key and signing private key on VM A only.

## 4. Environment and secrets

- Supply `DATABASE_URL`, `VULTR_INFERENCE_API_KEY`, `EVIDENCE_SIGNING_KEY`, and worker authentication via protected VM environment/secret store; do not put them in container images, logs or JS bundles.
- Keep `.env.example` free of values that look like live credentials.
- Confirm `curl /readyz` returns 503 when inference/DB/worker unavailable rather than misrepresenting a live system.
- Record model ID, max context, expected API endpoints and observed latency from actual account before go-live.

## 5. Worker controls — operational checklist

- Only authenticated VM A dispatches jobs to VM B.
- Runtime enforces nonroot, readonly FS, no-new-privileges, cap drop, isolated network, process and memory/time caps.
- No Docker socket mount into application/agent containers.
- Every run gets a unique ID and temp directory; cleanup after completion or failure.
- Reaper cleans orphaned containers; a separate service checks stalled job leases.
- Worker image digests are pinned for reproducibility; do not run latest unpinned image blindly.

## 6. Verification commands (examples; adapt after service exists)

```bash
# Example only, after deployment and once host/domain chosen
curl -fsS https://YOUR-RUKSA-DOMAIN/healthz
curl -fsS https://YOUR-RUKSA-DOMAIN/readyz
# Verify execution using the test plan and observe the corresponding event stream
```

Do not include sudo curl-to-shell installation shortcuts in production runbooks. Use signed official packages and reviewed installation instructions.

## 7. Monitoring and alerting

Measure: health success, request p95, run queue depth, sandbox creations/teardowns, timeouts, OOMs, verifier failures, cost per mission and inference token use. Set alerts for public 5xx spikes, cleanup backlog, memory pressure and credit depletion. Scrub source content and secrets from logs; use short TTL for demo.

## 8. Cost controls

Before deployment, record **actual** VM hourly rates and inference prices. Budget worksheet:

`estimated_total = (vm_a_hourly + vm_b_hourly) * hours + inference_tokens * unit_rate + storage + data_transfer + margin`.

Turn off unused instances. Keep a 25% credit reserve and set a credit balance threshold. Verify billing rules and account eligibility; free credits are not an unlimited spending guarantee.

## 9. Rollback and teardown

Maintain previous release/tag and DB migration compatibility. If compromised, disable public run action; rotate keys; terminate worker instance. On hackathon completion decide whether to keep deployment and attach payment method; otherwise delete VM, volumes, snapshots and artifact storage to stop costs. Record cleanup in ops checklist.

## 10. Incident statuses

`INFERENCE_UNAVAILABLE`, `WORKER_UNHEALTHY`, `SANDBOX_POLICY_REJECTED`, `SANDBOX_TIMEOUT`, `VERIFICATION_FAILED`, `STORAGE_LIMIT_REACHED`, `CREDIT_LIMIT_WARNING`. The UI shows a safe, actionable status without displaying private hostnames or keys.
