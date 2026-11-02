#!/usr/bin/env python3
"""Validates fictional RELIC behavior oracle fixture, NOT an AI-generated app."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "fixtures" / "relic" / "behavior-cases.json"

def run():
    data = json.loads(FILE.read_text(encoding="utf-8"))
    assert data["schema_version"] == "relic-fixture-v1"
    assert data["rights"] == "RUKSA authored synthetic demo"
    assert data["source"] == "examples/legacy-community-portal/index.html"
    assert (ROOT / data["source"]).exists()
    cases = data["cases"]
    assert len(cases) == 4
    assert len({case["id"] for case in cases}) == len(cases)
    errors = {"REGION_REQUIRED", "URGENT_DESCRIPTION_TOO_SHORT"}
    for case in cases:
        inp, expected = case["input"], case["expected"]
        assert inp["region"] in ("", "North", "Center", "South")
        assert inp["issue"] in ("streetlight", "drain", "pavement")
        assert inp["priority"] in ("normal", "urgent")
        desc = inp["description"].strip()
        if not inp["region"]:
            actual = {"accepted": False, "error_code": "REGION_REQUIRED"}
        elif inp["priority"] == "urgent" and len(desc) < 30:
            actual = {"accepted": False, "error_code": "URGENT_DESCRIPTION_TOO_SHORT"}
        else:
            actual = {"accepted": True, "code": "-".join([inp["region"], inp["issue"], inp["priority"]]).upper()}
        assert actual == expected, (case["id"], actual, expected)
        if not expected["accepted"]:
            assert expected["error_code"] in errors
    print("PASS: 4 synthetic community portal oracle cases. No browser or AI execution tested.")

if __name__ == "__main__":
    try:
        run()
    except (OSError, AssertionError, ValueError, KeyError) as ex:
        print(f"FAIL: {ex}", file=sys.stderr)
        sys.exit(1)
