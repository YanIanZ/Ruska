# Hackathon Demo and Submission Playbook

**Event:** [Vultr Agent Rush](https://lablab.ai/ai-hackathons/vultr-hackathon). **Track:** Blast Radius Zero. **Status:** submission not yet made.

## 1. Core storyline

**Problem:** AI confidently claims it completed work, but operations teams need proof. **Solution:** RUKSA plans, safely executes, independently verifies and presents source-linked findings. **Business case:** synthetic procurement invoice reconciliation with a verified $180 unit-price discrepancy, plus a suspected duplicate and an unknown PO.

## 2. Demo data narrative

Import 150 synthetic invoices and 150 purchase-order lines. Three intentionally planted anomaly scenarios: price variance +$180 on `INV-0042`, duplicate supplier invoice number on `INV-0087` vs `INV-0086`, and unknown purchase-order reference on `INV-0121`. All data is generated for demo; no user, vendor or bank real-world data is present.

**Important:** `$180` is a **price variance**, not the sum of all possible financial exposure. Do not add duplicate value or unknown-PO value into that figure without separate verification.

## 3. Three-minute presentation script

| Time | Visual | Voice-over intention |
|---|---|---|
| 00:00–00:20 | Problem and invoice table | Teams cannot audit opaque AI assertions |
| 00:20–00:40 | Product intro | RUKSA: work done, proof attached |
| 00:40–01:05 | Create mission and show constrained plan | Intent turns into typed jobs via Vultr inference |
| 01:05–01:35 | Real sandbox execution + data output | A separate Vultr-hosted sandbox runs generated Python, not the API process |
| 01:35–02:05 | Findings + evidence graph | Model explanation is checked against invoice/PO values; $180 verified |
| 02:05–02:35 | Containment negative demo | Infinite loop hits timeout; worker destroys container; control plane still works |
| 02:35–03:00 | Approval draft and closing | Human governs action; no payment/external send; platform vision |

Adapt runtime to event video limit if official guidelines change. No fake terminal recordings or synthetic logs presented as real execution.

## 4. Submission deliverables

- [ ] Public GitHub source repository with MIT license and setup instructions.
- [ ] Public product URL hosted on Vultr; backend VM is the control system.
- [ ] Real multi-step agent using Vultr Serverless Inference for **all** agent LLM calls.
- [ ] Containment evidence in video: run a safe test infinite loop or denied action in isolated sandbox.
- [ ] Demo video file/link with clear walkthrough of problem, tech, safety and result.
- [ ] Pitch slides / deck file and project cover image.
- [ ] Architecture diagram, full use case and Vultr integration documented in README.
- [ ] Project title, descriptions, technology tags and official lablab submission confirmation.

**Deadline in UTC:** 2026-11-08 22:00. **Deadline in WIB:** 2026-11-09 05:00. Confirm official page again at submission. Registration closes at kickoff 2026-11-03 15:00 UTC.

## 5. Suggested submission fields

**Title:** RUKSA — Autonomous Work, Verified by Evidence

**Tagline:** Work Done. Proof Attached.

**Short description:** An evidence-first AI operations agent that reconciles procurement invoices using real isolated execution on Vultr, independent financial verification and human approval gates.

**Long description:** RUKSA turns procurement tasks into typed, policy-checked missions. Vultr Serverless Inference plans the workflow, a Vultr-hosted orchestrator dispatches code/browser steps to disposable sandboxes, and a deterministic verifier cross-checks anomalous invoice records against purchase orders. Every confirmed finding carries source identifiers, executed-step metadata and artifact integrity evidence. The operator can inspect findings and approve a draft follow-up without any automated external financial action. The recorded demo shows live sandbox containment, including an intentional timeout.

**Category tags:** AI agents, Vultr, serverless inference, cloud compute, sandbox, procurement, auditability, enterprise automation, Go, Python, Playwright.

## 6. Scoring map

| Criterion | What to show |
|---|---|
| Application of Technology | Working Vultr VM orchestration, actual code sandbox, inference integration, policy and execution artifacts |
| Presentation | One complete coherent use case, readable UX and short crisp evidence story |
| Business Value | Auditable invoice exception discovery and reduced manual review hypothesis |
| Originality | Proof-carrying workflow acceptance and source-linked deterministic results |

Do not state numerical score predictions or superiority to competitors as fact.

## 7. Demo reliability checklist

- [ ] Product URL works from an incognito session.
- [ ] Fixture mission runs 3 times on current deployed commit.
- [ ] Browser or code execution genuinely occurs; no pre-recorded state is mislabeled live.
- [ ] Sandbox resource policy and teardown are displayed and logged.
- [ ] No secret appears in screen recording, network inspector or log.
- [ ] Evidence links open and amount is computed from displayed source values.
- [ ] Camera/mic capture clean; video has readable captions and no irrelevant UI clutter.
- [ ] Final submission links tested in a second browser.

## 8. Final pitch

“AI agents should not be trusted because they sound confident. They should be trusted because their work can be independently verified. RUKSA doesn't just automate work. It makes automation accountable.”
