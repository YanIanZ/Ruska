# RUKSA / CHORD

**Safe alone does not mean safe together.**

**Status:** New research product direction for Vultr Agent Rush Hackathon 2026, Challenge 1 — Blast Radius Zero. The repository currently contains a **real, locally executable synthetic schedule-analysis prototype and detailed implementation designs**, NOT a deployed agent, Vultr inference integration or sandbox service.

## Product thesis
RUKSA CHORD is an **Emergent Safety Laboratory** that discovers collective hazards in multi-agent workflows when individually permitted steps interact through shared resources. The user describes an operation, Vultr Serverless Inference proposes bounded experiments and code, disposable Vultr sandboxes execute the experiments, and a separate trusted verifier checks global safety invariants, identifies a minimal failing interleaving and retests an approved coordination patch.

The product answers: **What fails only because independent agents act together?**

This is not reverse engineering and does not reuse the scope of REA, invoice reconciliation or digital restoration. Formal concurrency testing, model checking and multi-agent verification are established fields; RUKSA proposes an integrated product workflow, not an unprecedented mathematical discovery.

## Hero scenario
Two independently authorized order agents both see one remaining item. Each local approval is correct based on its stale read; two approvals may result in overselling. A bounded schedule explorer finds a failing interleaving, produces a replayable trace, and compares it against an atomic reservation policy.

## Run the offline synthetic proof-of-concept

Requires Python 3.10+ and no third-party dependencies:

\`\`\`bash
python3 -m chord.cli
python3 -m chord.cli --json
python3 -m unittest discover -s tests -v
\`\`\`

Expected in the **bounded synthetic model**: 20 interleavings, 18 failures with naive coordination, 0 failures with atomic reservation, and 7 unit tests passing.

This is *not* real distributed-agent execution, a Vultr VM demonstration, or evidence of cloud containment. The code is intentionally deterministic to establish the first reproducible research example before integrating real sandboxed agent-generated code.

## Hackathon target
Choose **Challenge 1: Blast Radius Zero**. Requirements include a Vultr VM control/backend, Vultr Serverless Inference for *all agent LLM calls*, agent-written code that actually runs in isolated disposable sandboxes on Vultr, real verifiable execution output, a public web interface and a recorded containment moment. See the [challenge-specific implementation map](docs/CHALLENGE-MAPPING.md).

## Product workflow
1. Define experiment and collective invariant.
2. Use Vultr Serverless Inference to plan bounded agent interleavings and/or produce executable test code.
3. Dispatch each experiment to a per-run sandbox on a dedicated Vultr worker VM; never execute agent-authored code in Go API process.
4. Collect actual traces and artifact hashes.
5. Trusted deterministic checker finds a counterexample; LLM can explain but cannot change verdict.
6. Generate a typed coordination patch proposal; execute the before/after comparison in new sandboxes.
7. Export a **Collective Safety Report** with measured outcomes, reproduction recipe and residual risks.

## Design documents
- [PRD](docs/PRD.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Security](docs/SECURITY.md)
- [Challenge mapping](docs/CHALLENGE-MAPPING.md)
- [Experimental protocol](docs/EXPERIMENT-PROTOCOL.md)
- [Originality and product positioning](docs/ORIGINALITY.md)
- [Delivery roadmap](docs/ROADMAP.md)
- [Demo script](docs/DEMO.md)
- [Testing](docs/TEST-PLAN.md)
- [Engineering backlog](docs/BACKLOG.md)

## Out of scope
No unauthorized external agent systems, production e-commerce writes, payment processing, real personal data, live vendor API access, arbitrary public code execution, claimed unhackable infrastructure, or claims that 20 synthetic schedules cover realistic distributed behavior.

## Old RUKSA prototypes
A previous Draft PR explored procurement and RELIC digital restoration. That is superseded direction and **is not in this new clean branch**. REA remains a separate reverse-engineering tool.

## License
MIT. See LICENSE.
