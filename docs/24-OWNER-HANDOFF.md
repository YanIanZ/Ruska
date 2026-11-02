# SUPERSEDED — Historical RUKSA Concept (NOT CURRENT SCOPE)

> Current product is **RUKSA RELIC**, the Autonomous Digital Restoration Studio. See [active PRD](32-RELIC-PRD.md), [architecture](33-RELIC-ARCHITECTURE.md), and [security](36-RELIC-SECURITY.md). The text below is retained for historical reference and must not be used as RELIC implementation instructions.

---

# Owner Handoff — How to Publish and Start Building

**Status as of 2026-11-02:** local repository containing planning documents, machine-readable schemas and synthetic fixtures. **No GitHub repository, deployed app, live Vultr resources or PR is represented as created by this bundle.**

## 1. Publish to GitHub

The local package is initialized as a Git repository and has an initial documentation commit. When extracted into a folder and GitHub CLI is authenticated as `YanIanZ`, use:

```bash
cd RUKSA
./scripts/publish_to_github.sh
```

The script checks authentication, creates the public `YanIanZ/RUKSA` repository if absent, configures origin and pushes main without force. **This action changes a public account and requires owner execution/login; do not claim it has run until confirmed in GitHub.**

Alternative: manually create an empty **public** `RUKSA` repository on GitHub without auto-generated README/license/gitignore, then `git remote add origin https://github.com/YanIanZ/RUKSA.git && git push -u origin main`. Only use the URL after the repository exists.

## 2. Initial checks

```bash
python3 scripts/validate_fixtures.py
python3 scripts/check_docs.py
```

Check `git status`, license and README. Confirm GitHub Actions `documentation-and-fixtures` passes on the actual pushed commit.

## 3. Hackathon work start order

- Confirm registration and account credits at event kickoff. Recheck published rules.
- Open GitHub implementation issues from `docs/11-BACKLOG.md`.
- Create services after kickoff with API/worker skeleton, then run actual sandbox on Vultr.
- Publish deployment URL only after verified from a clean browser.
- Record containment moment and real evidence trail before video/pitch completion.

## 4. What this bundle is NOT

It is **not** a full-stack implemented product, an AI model integration, a sandbox deployment, a completed security audit or an official lablab submission. `scripts/validate_fixtures.py` is a deterministic oracle for a sample fixture only. The documentation includes proposed service layouts; no phantom directories are listed as deployed code.

## 5. Suggested issue kick-off

First issues: INF-01 (Vultr control VM), INF-03 (Vultr inference), CORE-01 (Go API), INF-02 (worker VM), WORK-01/02 (sandbox), DATA-01/02 (finance verifier), WEB-01 (frontend). Prioritize `docs/12-TEST-PLAN.md` release gates over aesthetics.

## 6. Submission deadline

Official end is 2026-11-08 22:00 UTC / 2026-11-09 05:00 WIB. Verify on event live dashboard. Review MIT/open-source rules before code submission.
