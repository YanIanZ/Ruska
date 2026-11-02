# SUPERSEDED — Historical RUKSA Concept (NOT CURRENT SCOPE)

> Current product is **RUKSA RELIC**, the Autonomous Digital Restoration Studio. See [active PRD](32-RELIC-PRD.md), [architecture](33-RELIC-ARCHITECTURE.md), and [security](36-RELIC-SECURITY.md). The text below is retained for historical reference and must not be used as RELIC implementation instructions.

---

# RUKSA Two-Speed Roadmap — Win the Demo, Build the Platform

Status: proposed hackathon plan. Event online build Nov 3–8, 2026, submission Nov 8 22:00 UTC. Official brief: https://lablab.ai/ai-hackathons/vultr-hackathon

## Tier H: uncuttable public demo
- Vultr VM backend and hosted web app, Vultr Serverless Inference for all agent LLM calls.
- Mission Capsule typed plan and deterministic policy checks.
- Real Python code generated/proposed by agent and EXECUTED in disposable sandbox on worker VM, with enforced resource and network limits.
- 150-invoice procurement fixture and real Go verifier: three seeded anomalies, $180 price mismatch, reject false $190 answer.
- ProofPack v1 with byte hashes, actual execution info, input references and honest SIGNED/UNSIGNED status. Ed25519 signed manifest is high-priority P0 goal, but never fake it if unavailable.
- Containment Theater: bounded runaway process, blocked forbidden egress, cleanup and healthy control plane.
- Simple evidence UI, review-gated vendor clarification DRAFT, public URL, recorded video, slides and repo.

## Tier S: stretch only AFTER Tier H passes
MicroVM via Microsandbox if KVM and egress policy demonstrably work; browser to owned mock portal; second independent shadow sandbox; offline signed ProofPack verifier; report export.

## Tier P: after judging
Reusable SDK/CLI and policy registry; multi-workflow templates; enterprise tenancy/SSO; real read-only connectors and consent; worker fleet, customer-managed keys, retention controls, compliance audits.

## Day gates
Nov 3: Vultr inference + API deployed, HTTPS accessible.
Nov 4: actual sandbox execution and bounded cleanup observed.
Nov 5: fixture + Go verifier end-to-end, all known anomalies explained.
Nov 6: proof manifest and containment negatives demonstrated.
Nov 7: evidence/approval UI, fresh-session end-to-end and safe failure UX.
Nov 8: test, video, slides, public demo, submit to lablab before official deadline.

## Kill-switches for scope
If no real sandbox by end Nov 4, drop browser, shadow replay, PDF and polish. If verifier incorrect by Nov 5, pause AI creativity and fix domain truth. If egress restrictions fail, disable public browser/custom-code mode. If KVM absent, disclose container boundary. If Ed25519 incomplete, mark ProofPack UNSIGNED. No Kubernetes, model training, ERP integration or multitenancy during hackathon.

## Demo narrative
User launches mission -> AI plan passes constrained policy -> real sandbox executes -> false model claim ($190) rejected by independent verifier ($180) -> ProofPack shows evidence -> containment test destroys a runaway guest while the app stays healthy -> human reviews draft resolution. Measured real output, not simulated logs.

## Competitive framing
The goal is **execution accountability**, not a novelty claim for sandboxing alone. Judges evaluate technology, presentation, business value and originality. No fixed win percentage is justified without final competitors and working product. More ambitious architecture increases upside only when the minimum proof actually runs.
