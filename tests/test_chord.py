"""Tests for OFFLINE CHORD synthetic state machine; no cloud or sandbox claims."""
import json
import unittest
from pathlib import Path

from chord.engine import (
    enumerate_experiment,
    possible_schedules,
    reproducible_report,
    run_schedule,
    validate_experiment,
)


FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "inventory-race.json"


class ChordTests(unittest.TestCase):
    def setUp(self):
        self.experiment = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_schedule_enumeration_is_complete_for_two_three_step_agents(self):
        schedules = possible_schedules()
        self.assertEqual(len(schedules), 20)
        self.assertEqual(len({tuple(s) for s in schedules}), 20)
        self.assertTrue(all(s.count("agent_a") == s.count("agent_b") == 3 for s in schedules))

    def test_naive_has_emergent_failure(self):
        result = enumerate_experiment(self.experiment, "naive")
        self.assertEqual(result["schedules_explored"], 20)
        self.assertEqual(result["violations"], 18)
        self.assertIsNotNone(result["representative_counterexample"])
        self.assertEqual(result["representative_counterexample"]["final_state"]["remaining_stock"], -1)

    def test_atomic_mitigation_holds_in_this_bounded_model(self):
        result = enumerate_experiment(self.experiment, "atomic")
        self.assertEqual(result["violations"], 0)
        self.assertEqual(result["safe_schedules"], 20)
        self.assertTrue(result["all_schedules_safe"])

    def test_baseline_serial_order_can_be_safe(self):
        result = run_schedule(["agent_a"] * 3 + ["agent_b"] * 3, "naive")
        self.assertEqual(result["status"], "HELD")
        self.assertEqual(result["final_state"]["reservations_issued"], 1)

    def test_reproducible_report_never_claims_infrastructure_checks(self):
        report = reproducible_report(self.experiment)
        self.assertEqual(report["scope"], "synthetic_local_state_machine_only")
        self.assertFalse(report["isolated_sandbox_used"])
        self.assertFalse(report["llm_called"])
        self.assertFalse(report["containment_tested"])
        self.assertEqual(len(report["experiment_sha256"]), 64)

    def test_reject_unknown_fixtures_and_policies(self):
        with self.assertRaises(ValueError):
            validate_experiment({**self.experiment, "shell": "rm anything"})
        with self.assertRaises(ValueError):
            enumerate_experiment(self.experiment, "unrestricted")
        with self.assertRaises(ValueError):
            run_schedule(["agent_a"] * 6, "naive")

    def test_counterexample_prefix_ends_in_failure(self):
        baseline = enumerate_experiment(self.experiment, "naive")
        prefix = baseline["shortest_failure_prefix"]
        self.assertFalse(prefix[-1]["global_invariant_holds"])
        self.assertTrue(all(x["global_invariant_holds"] for x in prefix[:-1]))


if __name__ == "__main__":
    unittest.main()
