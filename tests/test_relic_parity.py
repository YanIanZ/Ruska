#!/usr/bin/env python3
"""Tests for the offline RELIC lab only; not live sandbox or browser tests."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "examples" / "relic-lab"))
import parity_lab

CORRECT = ROOT / "examples" / "relic-lab" / "candidate-correct.json"
WRONG = ROOT / "examples" / "relic-lab" / "candidate-wrong.json"


class RelicParityLabTests(unittest.TestCase):
    def test_correct_model_passes_fixture_and_probes(self):
        r = parity_lab.report(CORRECT)
        self.assertEqual((r["passed_cases"], r["failed_cases"]), (4, 0))
        self.assertEqual(r["counterfactual_probe"]["mismatch_count"], 0)
        self.assertEqual(r["artifact_integrity"], "UNSIGNED")
        self.assertFalse(r["runtime"]["real_browser_execution"])

    def test_wrong_model_rejected_and_counterexample_minimized(self):
        r = parity_lab.report(WRONG)
        self.assertEqual(r["failed_cases"], 1)
        self.assertEqual(r["counterfactual_probe"]["mismatch_count"], 20)
        minimum = r["counterfactual_probe"]["smallest_counterexample"]
        self.assertEqual(minimum["description_length"], 10)
        self.assertEqual(minimum["reference"]["error_code"], "URGENT_DESCRIPTION_TOO_SHORT")
        self.assertTrue(minimum["candidate"]["accepted"])

    def test_explicit_original_boundary(self):
        record = {"region": "Center", "issue": "drain", "priority": "urgent", "description": "x" * 29}
        self.assertFalse(parity_lab.reference_model(record)["accepted"])
        record["description"] += "x"
        self.assertTrue(parity_lab.reference_model(record)["accepted"])

    def test_unrecognized_candidate_properties_rejected(self):
        candidate = json.loads(CORRECT.read_text(encoding="utf-8"))
        candidate["command"] = "whoami"
        with self.assertRaises(ValueError):
            parity_lab.validate_candidate(candidate)

    def test_bool_is_not_accepted_as_threshold(self):
        candidate = json.loads(CORRECT.read_text(encoding="utf-8"))
        candidate["urgent_min_description_length"] = True
        with self.assertRaises(ValueError):
            parity_lab.validate_candidate(candidate)


if __name__ == "__main__":
    unittest.main()
