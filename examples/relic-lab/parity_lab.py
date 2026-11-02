#!/usr/bin/env python3
"""RUKSA RELIC offline counterfactual-parity laboratory.

This tests HANDWRITTEN models of our OWNED synthetic portal, not a live browser,
Vultr inference, generated code, sandbox isolation or a deployed service.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CASES = ROOT / "fixtures" / "relic" / "behavior-cases.json"
SCHEMA = "relic-candidate-model-v1"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reference_model(record: dict[str, Any]) -> dict[str, Any]:
    """Handwritten behavioral oracle based on the project-owned legacy fixture."""
    region = record["region"]
    issue = record["issue"]
    priority = record["priority"]
    description = record["description"].strip()
    if not region:
        return {"accepted": False, "error_code": "REGION_REQUIRED"}
    if priority == "urgent" and len(description) < 30:
        return {"accepted": False, "error_code": "URGENT_DESCRIPTION_TOO_SHORT"}
    return {"accepted": True, "code": f"{region}-{issue}-{priority}".upper()}


def validate_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    allowed = {"schema_version", "requires_region", "urgent_min_description_length"}
    if set(candidate) != allowed or candidate.get("schema_version") != SCHEMA:
        raise ValueError("Only the fixed, typed synthetic candidate policy is supported")
    if type(candidate["requires_region"]) is not bool:
        raise ValueError("requires_region must be a boolean")
    threshold = candidate["urgent_min_description_length"]
    if type(threshold) is not int or not (1 <= threshold <= 100):
        raise ValueError("urgent threshold must be an integer in [1,100]")
    return candidate


def candidate_model(record: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    """Interprets a fixed, non-executable candidate rule specification."""
    region = record["region"]
    issue = record["issue"]
    priority = record["priority"]
    description = record["description"].strip()
    if candidate["requires_region"] and not region:
        return {"accepted": False, "error_code": "REGION_REQUIRED"}
    if priority == "urgent" and len(description) < candidate["urgent_min_description_length"]:
        return {"accepted": False, "error_code": "URGENT_DESCRIPTION_TOO_SHORT"}
    return {"accepted": True, "code": f"{region}-{issue}-{priority}".upper()}


def compare_cases(candidate: dict[str, Any], dataset: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for case in dataset["cases"]:
        observed = reference_model(case["input"])
        expected = case["expected"]
        if observed != expected:
            raise ValueError(f"Reference model differs from fixture oracle for {case['id']}")
        actual = candidate_model(case["input"], candidate)
        rows.append({
            "case_id": case["id"],
            "status": "PASS" if actual == observed else "FAIL",
            "reference": observed,
            "candidate": actual,
        })
    return rows


def counterfactual_probes(candidate: dict[str, Any], max_length: int = 40) -> dict[str, Any]:
    """Bounded synthetic length search, not an autonomous browser observation."""
    differences = []
    for length in range(max_length + 1):
        record = {
            "region": "Center", "issue": "drain", "priority": "urgent",
            "description": "x" * length,
        }
        legacy = reference_model(record)
        modern = candidate_model(record, candidate)
        if legacy != modern:
            differences.append({
                "description_length": length,
                "input": record,
                "reference": legacy,
                "candidate": modern,
            })
    return {
        "probe_family": "synthetic_urgent_description_boundary",
        "range_inclusive": [0, max_length],
        "case_count": max_length + 1,
        "mismatch_count": len(differences),
        "smallest_counterexample": differences[0] if differences else None,
        "mismatch_lengths": [item["description_length"] for item in differences],
    }


def report(candidate_path: Path, fixture_path: Path = CASES) -> dict[str, Any]:
    candidate = validate_candidate(json.loads(candidate_path.read_text(encoding="utf-8")))
    dataset = json.loads(fixture_path.read_text(encoding="utf-8"))
    if dataset.get("schema_version") != "relic-fixture-v1":
        raise ValueError("Unexpected fixture schema")
    cases = compare_cases(candidate, dataset)
    probes = counterfactual_probes(candidate)
    passed = sum(item["status"] == "PASS" for item in cases)
    return {
        "product": "RUKSA RELIC",
        "assurance_level": "offline_fixture_model_only",
        "runtime": {
            "real_browser_execution": False, "vultr_inference": False,
            "sandbox_containment_tested": False, "generated_source_compiled": False,
        },
        "artifact_integrity": "UNSIGNED",
        "candidate_sha256": digest(candidate_path),
        "fixture_sha256": digest(fixture_path),
        "tested_cases": len(cases),
        "passed_cases": passed,
        "failed_cases": len(cases) - passed,
        "case_results": cases,
        "counterfactual_probe": probes,
        "coverage_warning": "Only the specified owned synthetic form rules were modeled; hidden backend behavior is UNKNOWN.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True, type=Path, help="Typed candidate JSON")
    parser.add_argument("--json", action="store_true", help="Print machine-readable result")
    args = parser.parse_args()
    try:
        output = report(args.candidate)
    except (ValueError, KeyError, OSError, TypeError, json.JSONDecodeError) as error:
        print(f"INVALID: {error}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(output, indent=2, sort_keys=True))
    else:
        print("RUKSA RELIC — Offline Fixture Parity Laboratory (NOT browser/AI)")
        print(f"Cases: {output['passed_cases']}/{output['tested_cases']} passed")
        for item in output["case_results"]:
            print(f"  {item['status']:4s}  {item['case_id']}")
        probes = output["counterfactual_probe"]
        if probes["smallest_counterexample"]:
            c = probes["smallest_counterexample"]
            print(f"COUNTEREXAMPLE: urgent description length={c['description_length']}; "
                  f"reference={c['reference']}; candidate={c['candidate']}")
        else:
            print("No differences found in 41 bounded synthetic probes; untested behavior remains UNKNOWN")
        print("Assurance: UNSIGNED; simulated reference models only")
    return 1 if output["failed_cases"] or output["counterfactual_probe"]["mismatch_count"] else 0


if __name__ == "__main__":
    sys.exit(main())
