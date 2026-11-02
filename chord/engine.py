"""Deterministic controlled experiment for emergent multi-agent failures.

All actors and inventory are synthetic. The local prototype does NOT demonstrate
cloud sandbox containment, LLM-generated code, or real distributed concurrency.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from typing import Any

SCHEMA = "chord-experiment-v1"
AGENTS = ("agent_a", "agent_b")
STEPS = ("read", "decide", "commit")
MODES = ("naive", "atomic")


def validate_experiment(experiment: dict[str, Any]) -> dict[str, Any]:
    if type(experiment) is not dict:
        raise ValueError("experiment must be a JSON object")
    expected = {"schema_version", "initial_stock", "reservation_size", "agents"}
    if set(experiment) != expected:
        raise ValueError("experiment contains unknown/missing fields")
    if experiment["schema_version"] != SCHEMA:
        raise ValueError("unsupported schema_version")
    if type(experiment["initial_stock"]) is not int or experiment["initial_stock"] != 1:
        raise ValueError("prototype supports exactly one synthetic stock unit")
    if type(experiment["reservation_size"]) is not int or experiment["reservation_size"] != 1:
        raise ValueError("prototype supports one unit per agent")
    if experiment["agents"] != list(AGENTS):
        raise ValueError("prototype supports exactly two named synthetic agents")
    return experiment


def possible_schedules() -> list[list[str]]:
    """Every order-preserving interleaving of two 3-step agents: C(6,3)=20."""
    schedules = []
    for left_positions in itertools.combinations(range(6), 3):
        selected = set(left_positions)
        schedules.append([
            AGENTS[0] if index in selected else AGENTS[1]
            for index in range(6)
        ])
    return schedules


def run_schedule(schedule: list[str], mode: str, initial_stock: int = 1) -> dict[str, Any]:
    if mode not in MODES:
        raise ValueError("invalid coordination policy")
    if len(schedule) != 6 or set(schedule) != set(AGENTS) or any(
        schedule.count(agent) != 3 for agent in AGENTS
    ):
        raise ValueError("unsupported schedule")
    shared = {"remaining_stock": initial_stock, "reservations_issued": 0}
    private = {
        agent: {"stage": 0, "last_seen_stock": None, "approved_locally": False}
        for agent in AGENTS
    }
    trace = []
    first_failure_at = None
    for sequence, agent in enumerate(schedule):
        local = private[agent]
        if local["stage"] >= len(STEPS):
            raise ValueError("invalid agent step ordering")
        action = STEPS[local["stage"]]
        before_stock = shared["remaining_stock"]
        result: dict[str, Any] = {}
        if action == "read":
            local["last_seen_stock"] = shared["remaining_stock"]
            result = {"observed_stock": local["last_seen_stock"]}
        elif action == "decide":
            local["approved_locally"] = local["last_seen_stock"] >= 1
            result = {"eligible_from_snapshot": local["approved_locally"]}
        else:
            if not local["approved_locally"]:
                result = {"reservation_committed": False, "reason": "LOCAL_REJECT"}
            elif mode == "atomic" and shared["remaining_stock"] < 1:
                result = {"reservation_committed": False, "reason": "ATOMIC_STOCK_GUARD"}
            else:
                shared["remaining_stock"] -= 1
                shared["reservations_issued"] += 1
                result = {"reservation_committed": True}
        local["stage"] += 1
        globally_safe = (
            shared["remaining_stock"] >= 0
            and shared["reservations_issued"] <= initial_stock
        )
        if not globally_safe and first_failure_at is None:
            first_failure_at = sequence
        trace.append({
            "sequence": sequence,
            "agent": agent,
            "action": action,
            "stock_before": before_stock,
            "stock_after": shared["remaining_stock"],
            "result": result,
            "global_invariant_holds": globally_safe,
        })
    if any(private[agent]["stage"] != 3 for agent in AGENTS):
        raise ValueError("incomplete schedule")
    return {
        "coordination_policy": mode,
        "schedule": schedule,
        "trace": trace,
        "final_state": shared,
        "global_invariant": "remaining_stock >= 0 && reservations_issued <= initial_stock",
        "status": "VIOLATED" if first_failure_at is not None else "HELD",
        "first_failure_sequence": first_failure_at,
    }


def enumerate_experiment(experiment: dict[str, Any], mode: str) -> dict[str, Any]:
    valid = validate_experiment(experiment)
    if mode not in MODES:
        raise ValueError("invalid coordination policy")
    results = [run_schedule(schedule, mode, valid["initial_stock"]) for schedule in possible_schedules()]
    violations = [row for row in results if row["status"] == "VIOLATED"]
    first = min(
        violations,
        key=lambda row: (row["first_failure_sequence"], row["schedule"]),
        default=None,
    )
    # No LLM decides the invariant outcome; the pure state machine computes it.
    return {
        "mode": mode,
        "schedules_explored": len(results),
        "violations": len(violations),
        "safe_schedules": len(results) - len(violations),
        "shortest_failure_prefix": first["trace"][: first["first_failure_sequence"] + 1] if first else None,
        "representative_counterexample": first,
        "all_schedules_safe": not violations,
    }


def reproducible_report(experiment: dict[str, Any]) -> dict[str, Any]:
    valid = validate_experiment(experiment)
    baseline = enumerate_experiment(valid, "naive")
    mitigation = enumerate_experiment(valid, "atomic")
    assert baseline["violations"] > 0, "seeded failure is not reproducible"
    assert mitigation["violations"] == 0, "proposed fix did not pass local model"
    canonical = json.dumps(valid, sort_keys=True, separators=(",", ":")).encode()
    return {
        "title": "RUKSA CHORD — Collective Coordination Counterexample",
        "experiment_sha256": hashlib.sha256(canonical).hexdigest(),
        "scope": "synthetic_local_state_machine_only",
        "llm_called": False,
        "vultr_vm_used": False,
        "isolated_sandbox_used": False,
        "containment_tested": False,
        "formally_verified_distributed_system": False,
        "baseline": baseline,
        "patched": mitigation,
        "interpretation": "Individual locally valid reservation decisions can violate a global stock invariant when snapshots are stale.",
        "caveat": "The atomic fix passes all 20 interleavings in THIS bounded synthetic model; this is not a proof for real production agents.",
    }
