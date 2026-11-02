# Executable Continuity Passport — Artifact Contract

**Status:** design proposal, not a deployed cryptographically signed proof.

A RELIC "restoration" should hand an engineering team an **executable continuity contract**. The output must be usable independently of RUKSA's marketing claims and repeatable in another test environment.

## Passport contents
1. **Authorization**: project-owned fixture and operator review; later, documented owner consent for external targets.
2. **Original snapshot & constraints**: origin identifier, allowed route, observed UI states, observation schema revision, input/trace digests.
3. **Behavior Genome**: evidence-linked fields, transitions, conditional rules, and UNKNOWN ledger.
4. **Candidate source**: generated code, package locks, build logs, image/version digests.
5. **Parity cases**: stable input fixtures, normalized outcomes for original and candidate, PASS/FAIL/NOT_TESTED for each.
6. **Counterexamples**: exact minimal reproducible case and which hypothesis it disproved.
7. **Accessibility diagnostics**: keyboard path and automation results; never equate an automated checker with WCAG certification.
8. **Security receipt**: allowed sandbox capabilities, process/resource limits, observed termination, network rules tested.
9. **Migration review**: uncovered risk, manual checklist, owner decision, rollback strategy and release block indicators.

## Status is a vector, not one green score
\`behavioral_parity = (tested_pass, tested_fail, not_tested)\`;
\`original_source_trust = OWNED_FIXTURE | AUTHORIZED_EXTERNAL | UNKNOWN\`;
\`source_authority = OBSERVED | INFERRED | UNKNOWN\`;
\`artifact_integrity = UNSIGNED | SIGNED | INVALID\`;
\`security_gate = PASSED | FAILED | NOT_RUN\`.

A passing test means that particular test case passed. It never implies a complete behavioral reconstruction. A hash protects bytes only relative to the trusted hash, and a signature binds signer identity only if keys are secure.

## Lifecycle
DISCOVERED -> GENOME_REVIEW -> CANDIDATE_BUILT -> PARITY_CHECKED -> HUMAN_REVIEW -> EXPORTABLE. FAILED and BLOCKED are observable outcomes and remain attached to versioned attempts. Each generated candidate is immutable; fixes create new revisions. Export cannot imply deployment. Real cutover is post-hackathon and must require manual authorization.

## Offline artifact (today)
examples/relic-lab/parity_lab.py produces a **JSON parity laboratory report**, with SHA-256 source manifest hashes. The prototype has neither browser traces nor signed evidence. Its report must explicitly set \`assurance_level = offline_fixture_model_only\` and \`artifact_integrity = UNSIGNED\`.

## Future compatibility
Current Behavior Genome schema in schemas/behavior-genome.schema.json is preliminary. Add a versioned Passport schema only when field semantics and cryptographic checks are implemented; do not silently change deployed contracts.
