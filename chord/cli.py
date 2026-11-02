"""Command line entrypoint for offline CHORD experiments (standard library only)."""
import argparse
import json
import sys
from pathlib import Path

from chord.engine import reproducible_report


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a synthetic CHORD coordination experiment")
    parser.add_argument("--fixture", type=Path, default=Path("fixtures/inventory-race.json"))
    parser.add_argument("--json", action="store_true", help="Emit a full machine-readable trace")
    args = parser.parse_args()
    try:
        experiment = json.loads(args.fixture.read_text(encoding="utf-8"))
        report = reproducible_report(experiment)
    except (ValueError, KeyError, AssertionError, OSError, TypeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        b, p = report["baseline"], report["patched"]
        print("RUKSA CHORD | OFFLINE SYNTHETIC MODEL | NOT A VULTR SANDBOX TEST")
        print(f"Schedule enumeration: {b['schedules_explored']} possible interleavings")
        print(f"Naive coordination: {b['violations']} global-invariant violations")
        print(f"Atomic coordination: {p['violations']} global-invariant violations")
        print("Result: counterexample found and typed coordination mitigation checked")
        print("Not tested: Vultr Inference, cloud isolation, containment, real agent code")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
