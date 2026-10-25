"""Phase 2 guards: review coverage, safe migration and honest provenance."""

from collections import Counter
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from common import read_yaml  # noqa: E402
from import_curriculum import normalize  # noqa: E402
from audit_curriculum import build  # noqa: E402


class CurriculumAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = read_yaml(ROOT / "curriculum/2027.yaml")["entries"]
        cls.reviews = read_yaml(ROOT / "reports/curriculum-review.yaml")["entries"]
        cls.summary = json.loads((ROOT / "reports/curriculum-audit.json").read_text())

    def test_every_date_has_one_specific_review(self):
        self.assertEqual(len(self.reviews), 365)
        self.assertEqual(Counter(r["id"] for r in self.reviews), Counter(e["id"] for e in self.index))
        self.assertEqual(Counter(r["date"] for r in self.reviews), Counter(e["date"] for e in self.index))
        for review in self.reviews:
            self.assertIn(review["review_status"], {"accepted", "revise", "replace"})
            self.assertTrue(review["scope_and_rationale"].strip())
        self.assertEqual(len({r["scope_and_rationale"] for r in self.reviews}), 365)

    def test_migration_preserves_calendar_identity_paths_and_training_status(self):
        baseline, _ = normalize(read_yaml(ROOT / "curriculum_2027_complete.yaml"))
        by_id = {e["id"]: e for e in baseline["entries"]}
        rebuilt, _, _, _ = build(ROOT)
        # Reapplying review metadata must preserve any live readiness state.
        self.assertEqual([e["status"] for e in rebuilt["entries"]], [e["status"] for e in self.index])
        for entry in self.index:
            with self.subTest(id=entry["id"]):
                unchanged = {k: v for k, v in entry.items() if k not in {"focus", "subdomain", "review_status", "status", "revision_state"}}
                original = {k: v for k, v in by_id[entry["id"]].items() if k not in {"focus", "subdomain", "status"}}
                self.assertEqual(unchanged, original)

    def test_accepted_review_never_claims_verified_outcome(self):
        history = [r for r in self.reviews if r["kind"] == "historical"]
        self.assertEqual(len(history), 313)
        self.assertTrue(all(r["observed_outcome"] == "unverified" for r in history))
        self.assertEqual(self.summary["verified_historical_outcomes"], 0)
        self.assertTrue(all(r["source_verification"] == "not_performed_in_phase2" for r in self.reviews))

    def test_single_primary_and_at_most_two_secondary_moves(self):
        families = {"causal-modeling", "prediction-counterfactual", "hypothesis-diagnosis", "constrained-decision", "evidence-selection", "quantitative-calibration", "boundary-transfer", "constructive-design"}
        for review in self.reviews:
            self.assertIn(review["primary_cognitive_move"], families)
            secondary = review["secondary_cognitive_moves"]
            self.assertLessEqual(len(secondary), 2)
            self.assertEqual(len(set(secondary)), len(secondary))
            self.assertNotIn(review["primary_cognitive_move"], secondary)
            self.assertEqual(review["kind"] == "micro_design", review["primary_cognitive_move"] == "constructive-design")

    def test_replacement_is_a_suggestion_with_original_material_retained(self):
        by_id = {e["id"]: e for e in self.index}
        for review in self.reviews:
            if review["review_status"] == "replace":
                entry = by_id[review["id"]]
                brief = read_yaml(ROOT / entry["brief_path"])
                self.assertEqual(brief["status"], entry["status"])
                self.assertEqual(brief["candidate_material"]["historical_case"], review["candidate_title"])
        self.assertEqual(self.summary["date_id_or_topic_replacements_applied"], 0)

    def test_all_weekly_density_signals_have_specific_followup(self):
        days = []
        for week in self.summary["weekly_review"]:
            days.extend(week["dates"])
            signal = (max(week["entity_hints"].values(), default=0) >= 2
                      or max(week["cognitive_moves"].values(), default=0) >= 3
                      or bool(week["repeated_overlap_clusters"]))
            if signal:
                self.assertTrue(week["followup_review"], week["iso_week"])
        self.assertEqual(Counter(days), Counter(e["date"] for e in self.index))

    def test_reports_and_canonical_review_metadata_are_reproducible(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/audit_curriculum.py")],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
