# Pitch Deck — RUKSA (8-slide narrative)

This is a slide content outline, not an exported PPT/PDF. Create final slide file with current demo screenshots and observed metrics rather than mock achievements.

## Slide 1 — RUKSA

**Title:** RUKSA · Work Done. Proof Attached.  
**One-line:** Autonomous procurement reconciliation with isolated execution and independently verifiable findings.  
Visual: product dashboard screenshot **only after implemented**.

## Slide 2 — The invisible problem

Procurement teams must reconcile invoice/PO differences. Generic agents can say they succeeded, but that is not verifiable. Show **before**: input spreadsheets, multiple vendor pages, manual reconciliation. Do not invent labor savings.

## Slide 3 — Agent workflow

Mission -> Vultr Inference plan -> policy -> real Python/Playwright sandbox -> deterministic verification -> signed evidence manifest (if implemented) -> human approval. Highlight architecture's separation of duties.

## Slide 4 — What we built

Demo journey: 150 synthetic invoice records, three known anomalies, **$180 price variance** on 10 units. Show real app screenshot and what code actually executed. Flag live features vs planned extensions.

## Slide 5 — Evidence that answers can be trusted

Zoom into `INV-0042`: invoice unit 13800 cents, PO unit 12000 cents, qty 10; independent expected delta 18000 cents. Show source row, sandbox artifact and verifier rule. Explain that evidence is auditable, not magic truth.

## Slide 6 — Blast Radius Zero demonstration

Show intentional infinite loop within disposable sandbox, timeout policy triggered, worker cleanup, unaffected control plane. Show actual log traces and no secrets, not fabricated results.

## Slide 7 — Technical fit and business opportunity

Vultr Cloud Compute as control plane + sandbox worker; Vultr Serverless Inference for model calls; real deployed public application. Finance/procurement operators benefit from evidence-linked exception review; pilot needed for commercial validation.

## Slide 8 — Roadmap & call to action

MVP -> vendor portal comparisons -> secure ERP adapters -> enterprise review workflows. Conclude: **“AI should earn trust through proof of executed work.”** Repo/demo URL; team owner and hackathon acknowledgment.

## Speaker notes

Keep jargon secondary to business consequence. Favor readable live screenshots and one tangible exception over excessive architecture arrows. No claim of SOC 2, guaranteed security, 99.9% accuracy or customer traction without evidence.
