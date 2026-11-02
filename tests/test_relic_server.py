"""HTTP integration tests for owned RELIC legacy fixture (no real browser/AI)."""
import json
import sys
import threading
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "examples" / "legacy-community-portal"))
from server import Handler, evaluate_request


class LegacyFixtureHTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)

    def submit(self, record):
        raw = json.dumps(record).encode("utf-8")
        request = Request(self.base + "/api/request", data=raw, headers={"Content-Type": "application/json"}, method="POST")
        try:
            with urlopen(request, timeout=3) as response:
                return response.status, json.loads(response.read())
        except HTTPError as error:
            return error.code, json.loads(error.read())

    def test_all_owned_synthetic_oracle_cases_via_real_http(self):
        cases = json.loads((ROOT / "fixtures/relic/behavior-cases.json").read_text(encoding="utf-8"))
        for case in cases["cases"]:
            with self.subTest(case=case["id"]):
                status, actual = self.submit(case["input"])
                self.assertEqual(actual, case["expected"])
                self.assertEqual(status, 200 if actual["accepted"] else 422)

    def test_conditional_boundary_is_server_side(self):
        record = {"region": "Center", "issue": "drain", "priority": "urgent", "description": "x" * 29}
        self.assertEqual(self.submit(record)[1]["error_code"], "URGENT_DESCRIPTION_TOO_SHORT")
        record["description"] = "x" * 30
        self.assertTrue(self.submit(record)[1]["accepted"])
        with urlopen(self.base + "/", timeout=3) as response:
            page = response.read().decode("utf-8")
        self.assertNotIn("description.length<30", page)
        self.assertIn("/api/request", page)

    def test_invalid_structure_and_oversized_body(self):
        status, body = self.submit({"region": "North"})
        self.assertEqual(status, 422)
        self.assertEqual(body["error_code"], "INVALID_FIELDS")
        request = Request(self.base + "/api/request", data=b"x" * 5000, headers={"Content-Type": "application/json"}, method="POST")
        with self.assertRaises(HTTPError) as raised:
            urlopen(request, timeout=3)
        self.assertEqual(raised.exception.code, 413)

    def test_only_expected_paths_exposed(self):
        with urlopen(self.base + "/healthz", timeout=3) as response:
            self.assertEqual(json.loads(response.read())["healthy"], True)
        with self.assertRaises(HTTPError) as raised:
            urlopen(self.base + "/../server.py", timeout=3)
        self.assertEqual(raised.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
