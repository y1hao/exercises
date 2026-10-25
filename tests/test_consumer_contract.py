"""Consumer input guards; all mutations take place in a temporary repository."""

from copy import deepcopy
from datetime import date
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from common import read_yaml, write_yaml  # noqa: E402
from import_curriculum import normalize  # noqa: E402
from validate_curriculum import validate  # noqa: E402


class InputPreservationTests(unittest.TestCase):
    def test_repository_contract(self):
        self.assertEqual(validate(ROOT), [])

    def test_original_input_hashes_unchanged(self):
        snapshot = json.loads((ROOT / "reports/phase1-input-snapshot.json").read_text())
        for rel, expected in snapshot["input_sha256"].items():
            with self.subTest(path=rel):
                self.assertEqual(hashlib.sha256((ROOT / rel).read_bytes()).hexdigest(), expected)

    def test_all_candidates_are_lossless_and_calendar_is_unchanged(self):
        original = read_yaml(ROOT / "curriculum_2027_complete.yaml")
        entries = read_yaml(ROOT / "curriculum/2027.yaml")["entries"]
        by_id = {row["id"]: row for row in original["slots"]}
        self.assertEqual(len(entries), len(by_id))
        for entry in entries:
            with self.subTest(id=entry["id"]):
                brief = read_yaml(ROOT / entry["brief_path"])
                self.assertEqual(brief["candidate_material"], by_id[entry["id"]])
                self.assertEqual(str(entry["date"]), str(by_id[entry["id"]]["date"]))

    def test_import_is_reproducible(self):
        index, briefs = normalize(read_yaml(ROOT / "curriculum_2027_complete.yaml"))
        # Test regeneration independently of later reviewed/enriched canonical data.
        with tempfile.TemporaryDirectory(prefix="exercises-import-") as output:
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/import_curriculum.py"), "--output-root", output],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(index, read_yaml(Path(output) / "curriculum/2027.yaml"))
            for path, brief in briefs.items():
                self.assertEqual(brief, read_yaml(Path(output) / path))

    def test_import_refuses_to_overwrite(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/import_curriculum.py")],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Refusing to overwrite", result.stderr)


class ValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sandbox = tempfile.TemporaryDirectory(prefix="exercises-phase1-")
        cls.root = Path(cls.sandbox.name)
        cls.original, briefs = normalize(read_yaml(ROOT / "curriculum_2027_complete.yaml"))
        for rel, content in {"curriculum/2027.yaml": cls.original, **briefs}.items():
            write_yaml(cls.root / rel, content)
        (cls.root / "protocols").mkdir()
        for name in ("runner.md", "historical.md", "micro-design.md"):
            (cls.root / "protocols" / name).write_text("<!-- status: draft -->\nTEST FIXTURE\n")

    @classmethod
    def tearDownClass(cls):
        cls.sandbox.cleanup()

    def setUp(self):
        self.data = deepcopy(self.original)

    def check(self):
        write_yaml(self.root / "curriculum/2027.yaml", self.data)
        return validate(self.root)

    def rejects(self, message):
        self.assertTrue(any(message in error for error in self.check()), message)

    def replace_file(self, path, content):
        original = path.read_bytes()
        self.addCleanup(path.write_bytes, original)
        if isinstance(content, str):
            path.write_text(content, encoding="utf-8")
        else:
            write_yaml(path, content)

    def make_ready(self, kind):
        entry = next(e for e in self.data["entries"] if e["kind"] == kind)
        entry["status"] = "ready"
        fixture = "historical.yaml" if kind == "historical" else "micro-design.yaml"
        brief = read_yaml(ROOT / "tests/fixtures" / fixture)
        brief.update({k: entry[k] for k in ("id", "kind", "domain", "status")})
        self.replace_file(self.root / entry["brief_path"], brief)
        for rel in ("protocols/runner.md", entry["protocol_path"]):
            self.replace_file(self.root / rel, "TEST FIXTURE: available protocol\n")
        return entry, brief

    def test_normal_input(self):
        self.assertEqual(self.check(), [])

    def test_missing_date(self):
        self.data["entries"].pop()
        self.rejects("missing dates")

    def test_duplicate_date(self):
        self.data["entries"][1]["date"] = self.data["entries"][0]["date"]
        self.rejects("duplicate date")

    def test_duplicate_id(self):
        self.data["entries"][3]["id"] = self.data["entries"][0]["id"]
        self.rejects("duplicate ID")

    def test_wrong_weekday(self):
        a, b = self.data["entries"][:2]
        a["date"], b["date"] = b["date"], a["date"]
        self.rejects("weekday allocation mismatch")

    def test_outside_year(self):
        self.data["entries"][0]["date"] = "2026-01-01"
        self.rejects("outside 2027")

    def test_invalid_date(self):
        self.data["entries"][0]["date"] = "2027-02-30"
        self.rejects("invalid date")

    def test_yaml_native_date_is_accepted(self):
        self.data["entries"][0]["date"] = date(2027, 1, 1)
        self.assertEqual(self.check(), [])

    def test_invalid_timezone(self):
        self.data["timezone"] = "UTC"
        self.rejects("timezone")

    def test_nonexistent_brief(self):
        self.data["entries"][0]["brief_path"] = "cases/engineering/missing.yaml"
        self.rejects("file does not exist")

    def test_unsafe_paths(self):
        for value in ("../secret.yaml", "/private/tmp/secret.yaml", "https://other/repo", "cases/../secret.yaml", "cases\\secret.yaml", "cases/%2e%2e/secret.yaml"):
            with self.subTest(path=value):
                self.data["entries"][0]["brief_path"] = value
                self.rejects("brief_path")

    def test_symlink_escape(self):
        with tempfile.TemporaryDirectory(prefix="exercises-outside-") as outside:
            source = Path(outside) / "outside.yaml"
            source.write_text("id: ENG-001\n")
            link = self.root / "escape.yaml"
            link.symlink_to(source)
            self.addCleanup(link.unlink)
            self.data["entries"][0]["brief_path"] = "escape.yaml"
            self.rejects("path escapes repository")

    def test_wrong_protocol(self):
        self.data["entries"][0]["protocol_path"] = "protocols/micro-design.md"
        self.rejects("protocol_path must be")

    def test_missing_runner(self):
        runner = self.root / "protocols/runner.md"
        content = runner.read_bytes()
        runner.unlink()
        self.addCleanup(runner.write_bytes, content)
        self.rejects("runner:")

    def test_brief_identity_mismatch(self):
        path = self.root / self.data["entries"][0]["brief_path"]
        brief = read_yaml(path)
        brief["id"] = "ENG-999"
        self.replace_file(path, brief)
        self.rejects("Brief/index id mismatch")

    def test_status_mismatch(self):
        self.data["entries"][0]["status"] = "sourced"
        self.rejects("Brief/index status mismatch")

    def test_unknown_status(self):
        self.data["entries"][0]["status"] = "candidate_needs_verification"
        self.rejects("invalid status")

    def test_review_status_is_separate_from_readiness(self):
        self.data["entries"][0]["review_status"] = "ready"
        self.rejects("invalid review_status")

    def test_revision_state_cannot_claim_readiness(self):
        self.data["entries"][0].update(review_status="accepted", revision_state="ready")
        self.rejects("revision_state does not match")

    def test_revision_state_must_match_brief(self):
        self.data["entries"][0].update(review_status="accepted", revision_state="retained")
        self.rejects("Brief/index revision_state mismatch")

    def test_malformed_types_report_errors(self):
        self.data["entries"][0].update({"status": [], "domain": {}, "kind": [], "id": [], "date": False})
        errors = self.check()
        self.assertGreaterEqual(len(errors), 5)

    def test_ready_without_complete_brief(self):
        entry = self.data["entries"][0]
        entry["status"] = "ready"
        path = self.root / entry["brief_path"]
        brief = read_yaml(path)
        brief["status"] = "ready"
        self.replace_file(path, brief)
        errors = self.check()
        for message in ("opening", "resolution", "sources", "evidence_pool", "draft protocol"):
            self.assertTrue(any(message in error for error in errors), message)

    def test_structurally_complete_historical_fixture(self):
        self.make_ready("historical")
        self.assertEqual(self.check(), [])

    def test_structurally_complete_design_fixture(self):
        self.make_ready("micro_design")
        self.assertEqual(self.check(), [])

    def test_unknown_source_reference(self):
        entry, brief = self.make_ready("historical")
        brief["evidence_pool"][0]["source_ids"] = ["missing"]
        write_yaml(self.root / entry["brief_path"], brief)
        self.rejects("unknown source_ids")

    def test_placeholder_source_url(self):
        entry, brief = self.make_ready("historical")
        brief["sources"][0]["url"] = "https://example.org/placeholder"
        write_yaml(self.root / entry["brief_path"], brief)
        self.rejects("real HTTP(S) URL")

    def test_incomplete_design(self):
        entry, brief = self.make_ready("micro_design")
        brief["perturbations"] = []
        del brief["initial_constraints"]
        write_yaml(self.root / entry["brief_path"], brief)
        errors = self.check()
        self.assertTrue(any("perturbations" in error for error in errors))
        self.assertTrue(any("initial_constraints" in error for error in errors))

    def test_duplicate_yaml_keys(self):
        self.replace_file(self.root / self.data["entries"][0]["brief_path"], "id: ENG-001\nid: ENG-002\n")
        self.rejects("Duplicate YAML key")

    def test_invalid_yaml_reports_error(self):
        self.replace_file(self.root / self.data["entries"][0]["brief_path"], "id: [\n")
        self.rejects("entry 1")


if __name__ == "__main__":
    unittest.main()
