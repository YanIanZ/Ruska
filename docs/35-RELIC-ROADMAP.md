# RUKSA RELIC — Six-Day Build Plan

Status: proposed; current state is documentation only.

| Day | Work | Demonstrable exit gate |
|---|---|---|
| Nov 3 | Freeze scope, stand up owned legacy fixture website, Vultr VM A/VM B, inference handshake | Owned legacy portal reachable; backend calls Vultr LLM |
| Nov 4 | Build isolated Playwright observation engine, limit steps/domains, capture state transitions | Browser actually clicks and captures two-step flow, real trace |
| Nov 5 | Compile Behavior Genome and synthesize accessible UI using Vultr Inference | Generated frontend code compiles in isolated guest and can be previewed |
| Nov 6 | Parity Arena: matched valid/invalid/boundary cases; comparison and feedback | True mismatch fails; equal normalized outputs pass |
| Nov 7 | Restore Studio UI side-by-side, export Capsule, keyboard/axe smoke tests, containment drills | Owner can inspect old and new UI, trace and case results; timeout/egress deny observed |
| Nov 8 | Reliability, video, pitch, security tests, publish URL and submit | Public app/repo/video/deck and real Vultr run evidenced before event cutoff |

## Priority P0
- Real browser Playwright and code build inside disposable sandbox with enforced limits.
- One owned legacy mock workflow with 3 meaningful test journeys.
- Actually generated UI code from model (no hardcoded final app disguised as generated).
- Paired comparison against old behavior; intentional mismatch demonstrably fails.
- Missing Knowledge Ledger labels unknowns; human approval for export.
- Containment demonstration and public Vultr demo.

## P1
- More polished side-by-side UI, 2nd sample, Ed25519 signed Capsule, shadow/rollback visualization.
- No extra project-wide reusable SDK until complete P0.

## Scope-cut decisions
If browser runner not working by Nov 4, cut auto-generation polish and fix browser. If generation cannot be made reproducible by Nov 5, use constrained JSON component DSL + LLM-authored DSL (still actual inference and generated code), avoid free-form package install. If unsafe egress, disable public run and show controlled prerecorded evidence plus static preview only; this cannot substitute for required real execution in final submission, so fix isolation before submission. Do not fabricate functionality.

## 2.0 execution rules

The active schedule is now tracked in [RELIC 2.0 scorecard](46-RELIC-DELIVERY-SCORECARD.md). **Critical path remains actual browser and code execution on Vultr**, not expansion into numerous tools. Counterfactual probing against a typed owned fixture is a high-value addition; broader autonomous discovery, second workflow, full Passport signatures, enterprise services and microVM optimization are stretch or post-event. The offline lab is runnable prep work but does not fulfill any cloud or sandbox requirement.

### Concrete foundation now available
The project-owned browser target is a loopback-only synthetic HTTP service with validation on the server. This is stronger than a self-contained static form, but **does not** satisfy the hackathon browser-in-Vultr sandbox requirement. Immediate P0 engineering step: deploy the owned mock service in an isolated demo environment, then execute Playwright from a separate restricted worker and record actual observation traces. [Fixture guide](../examples/legacy-community-portal/README.md).
