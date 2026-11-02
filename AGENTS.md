# RUKSA RELIC — Engineer and AI Coding Agent Instructions

**IMPORTANT:** Active scope changed to the Autonomous Digital Restoration Studio. Do NOT build the historical invoice reconciliation agent or a generic sandbox SaaS.

Read in order: docs/00-INDEX.md, docs/32-RELIC-PRD.md, docs/33-RELIC-ARCHITECTURE.md, docs/36-RELIC-SECURITY.md, docs/35-RELIC-ROADMAP.md.

Deliver ONE real complete proof: actual browser observations from our OWNED examples/legacy-community-portal/index.html, typed Behavior Genome with observed/inferred/unknown states, actual new frontend generated via Vultr Serverless Inference, code built inside disposable restricted sandbox, paired Playwright tests comparing old/new behavior, and exportable human-review package.

Do not claim hidden server logic was recovered from an inaccessible source. Do not introduce arbitrary URL crawling, copyrighted-site cloning, password extraction, open outbound internet from guest, privileged mounts, Docker socket, model-defined permissions, unbounded code or public production writes. No real personal data.

Vultr VM control plane and separate worker VM; enforce egress at runtime and check KVM availability before selecting microVM. All LLM calls for Challenge 1 use Vultr Serverless Inference. A model response is untrusted data, never a policy decision.

Every completed milestone requires real run ID, commit SHA, input case and pass/fail record. Test owner controls final review, and no P0 security failure is waived to make a demo green.

## RELIC 2.0 requirements for AI coding agents

Before writing an agent loop, run the [offline parity lab](examples/relic-lab/README.md) and its tests; keep the **bad candidate rejected** rather than hiding it. The expected failing candidate process exit code is 1, which is correct for this negative example.

Next implement the *real* browser-observed version: Playwright traces must come from a sandboxed owned site and must link each OBSERVED Genome rule to source evidence. Let Vultr Serverless Inference propose bounded probes and code changes; Go policy decides which actions may occur. Never present the handwritten reference model as real browser evidence, and never copy a third-party production app.

Use [Continuity Engineering](docs/42-RELIC-2-0-NORTH-STAR.md), [Counterfactual Engine](docs/43-COUNTERFACTUAL-ARCHAEOLOGY.md), [Passport](docs/44-CONTINUITY-PASSPORT.md) and [Scorecard](docs/46-RELIC-DELIVERY-SCORECARD.md). Preserve explicit unknown states and real failed parity records.

### Owned black-box fixture
Run the [local legacy HTTP fixture](examples/legacy-community-portal/README.md) before implementing discovery. Its urgent-description rule lives server-side. New Playwright code should interact through browser-visible states/responses rather than reading the fixture's Python source to manufacture a discovery. CI's HTTP tests are only fixture verification; write additional genuine sandboxed Playwright tests with observed trace IDs for P0.
