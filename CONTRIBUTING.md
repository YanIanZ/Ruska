# Contributing to RUKSA

RUKSA is a prototype intended for the Vultr Agent Rush Hackathon. Scope and safety are tightly controlled.

1. Open an issue mapping to `docs/11-BACKLOG.md` and include exact acceptance criteria.
2. Use a short-lived feature branch; avoid bulk merges that obscure behavior.
3. Include tests and update OpenAPI, schemas and documentation when contract changes.
4. Treat all input files, model output and browser contents as untrusted.
5. Do not commit secrets or real customer financial data. Use `fixtures/synthetic/` only.
6. Never mark a safety test passed without evidence from the actual runtime.
7. Include rollout/rollback guidance for infrastructure changes.
8. Prefer clear error states over permissive bypasses.

Run `python3 scripts/validate_fixtures.py` and `python3 scripts/check_docs.py` before submitting a documentation change. Full runtime tests will be introduced once actual services exist.

Contribution of code is under MIT license; only submit work you have rights to redistribute.
