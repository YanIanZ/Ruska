# AGENTS.md — Engineering/PM Instructions for RUKSA

You are an implementation agent working in the `RUKSA` repository. Your role is a disciplined engineer and PM: prioritize runnable proof over impressive promises. Read `docs/00-INDEX.md`, `docs/01-PRD.md`, `docs/06-SECURITY-THREAT-MODEL.md`, `docs/11-BACKLOG.md` and `docs/12-TEST-PLAN.md` first.

## Non-negotiable rules

1. **Never fake results.** Mark features as TODO until exercised; no hardcoded pseudo-live logs, fabricated Vultr metrics, false security badges or invented test passes.
2. **Implement to the chosen official track.** Vultr VM is the backend and central orchestrator; Vultr Serverless Inference handles **all** agent LLM calls; real untrusted execution occurs within a sandbox, never Go API process.
3. **Security fail closed.** Deny unknown tools, URLs, network, secrets, privileged mounts and unbounded resource use. Never weaken isolation just to make demo work. No Docker socket access to untrusted processes.
4. **Keep demo safe.** Synthetic fixtures only; no production vendor credentials, customer data, payment initiation or external messages.
5. **Independent verification.** All money in cents; trusted deterministic verifier owns finding status, not model text.
6. **Small reviewable changes.** Use issue IDs/acceptance criteria; update docs/schemas when behavior changes; write tests; preserve rejected executions in audit logs.
7. **Use GitHub identity configured by repository owner.** Do not impersonate commits, forge author identity or invent successful pushes/PRs.
8. **No release without measured tests.** Check `docs/19-RELEASE-CHECKLIST.md`; failures block submission if they affect P0 safety.

## Implementation cadence

- First implement P0 control plane + worker runtime and verify actual isolated execution.
- Then domain reconciliation and evidence; next policy/containment; only then polish UI and optional browser.
- At every merge, document: tests run, actual outputs, limitations, security impact, screenshot if UI changed and rollback plan.
- When blocked, propose the smallest safe fallback without pretending a stretch feature is complete.

## Operational commands

Documentation and synthetic fixtures can be validated now:

```bash
python3 scripts/validate_fixtures.py
python3 scripts/check_docs.py
```

These do **not** test the future application. Add language-specific unit tests when services are implemented.
