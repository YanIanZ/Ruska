# RUKSA RELIC — Counterfactual Parity Lab

**Executable local prototype, NOT a functioning AI/browser/sandbox service.** The experiment compares a handwritten model of the project-owned legacy form against a typed candidate policy. It demonstrates how RELIC should reject a superficially plausible but behaviorally incorrect modernization.

## Run (Python standard library, offline)
\`\`\`bash
python3 examples/relic-lab/parity_lab.py --candidate examples/relic-lab/candidate-wrong.json
# Expected exit code 1. One of 4 reference cases FAILS; bounded probes find 20 mismatching lengths (10..29).

python3 examples/relic-lab/parity_lab.py --candidate examples/relic-lab/candidate-correct.json --json
# Expected exit code 0; 4/4 fixture cases match, zero differences across 41 bounded synthetic probes.

python3 -m unittest discover -s tests -p "test_relic_*.py" -v
\`\`\`

All reports explicitly say \`assurance_level = offline_fixture_model_only\`, \`artifact_integrity = UNSIGNED\`, and all runtime flags are false. This is **not proof of Vultr inference, browser automation, isolated execution, or complete application parity**.

## Differentiation
A regular screenshot clone might accept the short urgent report and still look great. This lab detects that semantic error and gives the shortest counterexample in a bounded synthetic search. The planned real agent will derive hypotheses from authorized Playwright observations rather than a handwritten reference model.

## Safety
No arbitrary Python execution is accepted from candidate JSON. Only strict typed fields are parsed. Only the project's fictional synthetic portal is modeled; no outside network requests.
