"""Guard applied scope changes, original facts and numerical fallback boundaries."""

from collections import Counter
from pathlib import Path
import subprocess
import sys
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from common import read_yaml  # noqa: E402
from revise_curriculum import prepare, tsv_by_id  # noqa: E402
from audit_curriculum import FOCUS  # noqa: E402


class PlanningRevisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = read_yaml(ROOT / "curriculum/2027.yaml")["entries"]
        cls.planning = read_yaml(ROOT / "curriculum/planning-2027.yaml")["entries"]
        cls.by_id = {r["id"]: r for r in cls.planning}

    def test_all_initial_revision_actions_have_applied_scopes(self):
        notes = tsv_by_id(ROOT / "reports/phase2-review-notes.tsv")
        self.assertEqual(len(self.planning), 365)
        self.assertEqual(Counter(r["revision_state"] for r in self.planning), {
            "retained": 164, "awaiting_source": 191, "revised": 9, "awaiting_replacement": 1,
        })
        for entry in self.index:
            plan = self.by_id[entry["id"]]
            self.assertEqual(plan["revision_state"], entry["revision_state"])
            if notes[entry["id"]]["action"] == "revise":
                scope = plan["planned_exercise"]
                self.assertTrue(scope["main_question"].strip())
                self.assertTrue(scope["expected_output"].strip())
                self.assertTrue(scope["out_of_scope"].strip())

    def test_original_candidate_briefs_preserved_outside_planning(self):
        outputs, _ = prepare(ROOT)
        for entry in self.index:
            brief = read_yaml(ROOT / entry["brief_path"])
            regenerated = yaml.safe_load(outputs[entry["brief_path"]])
            with self.subTest(id=entry["id"]):
                self.assertEqual({k: v for k, v in brief.items() if k != "planning"},
                                 {k: v for k, v in regenerated.items() if k != "planning"})

    def test_historical_anchors_are_unverified_targets(self):
        for plan in self.planning:
            if plan["revision_state"] == "awaiting_source":
                scope = plan["planned_exercise"]
                self.assertTrue(scope["planning_only"])
                self.assertEqual(scope["anchor_status"], "unverified_research_target")
                self.assertTrue(scope["evidence_to_verify"])
                self.assertNotIn("historical_as_of", scope)
                self.assertNotIn("sources", scope)

    def test_all_quantitative_items_have_unapplied_specific_fallbacks(self):
        notes = tsv_by_id(ROOT / 'reports/phase2-review-notes.tsv')
        quant = {identifier for identifier, note in notes.items() if FOCUS[note['focus']] == 'quantitative-calibration'}
        planned = {r["id"] for r in self.planning if "quantitative_plan" in r}
        self.assertEqual(quant, planned)
        self.assertEqual(len(planned), 39)
        for identifier in planned:
            rule = self.by_id[identifier]["quantitative_plan"]
            self.assertTrue(rule["required_inputs"])
            self.assertFalse(rule["fallback_applied"])
            self.assertEqual(rule["input_verification"], "not_started")
            self.assertNotEqual(rule["missing_input_fallback"]["focus"], "quantitative-calibration")

    def test_synthetic_changes_are_bounded_and_not_historical_claims(self):
        designs = [r for r in self.planning if r["revision_state"] == "revised"]
        self.assertEqual(len(designs), 9)
        for record in designs:
            scope = record["planned_exercise"]
            self.assertTrue(scope["synthetic"])
            self.assertTrue(scope["planning_assumptions"])
            self.assertTrue(scope["scoped_change"])
        self.assertIn("中断后", self.by_id["DES-026"]["planned_exercise"]["main_question"])
        self.assertIn("不可同时满足", "".join(self.by_id["DES-041"]["planned_exercise"]["planning_assumptions"]))

    def test_replacement_and_identity_conditions_remain_open(self):
        replacement = self.by_id["ENG-157"]
        self.assertNotIn("planned_exercise", replacement)
        self.assertTrue(replacement["replacement_request"]["acceptance_conditions"])
        self.assertNotIn("replacement_event", replacement["replacement_request"])
        for identifier in ("ENG-011", "INV-034", "ENG-117", "ENG-015"):
            self.assertTrue(self.by_id[identifier]["source_identity_condition"])

    def test_generation_is_idempotent_and_inputs_are_not_modified(self):
        _, states = prepare(ROOT)
        self.assertEqual(sum(states.values()), 365)
        result = subprocess.run([sys.executable, str(ROOT / "scripts/revise_curriculum.py")],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
