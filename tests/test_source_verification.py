"""Guard provenance, historical disclosure and Phase 3's bounded migration."""

from copy import deepcopy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from common import read_yaml  # noqa: E402
from verify_sources import load_records, prepare, record_errors  # noqa: E402
from phase3_admission import assess, prepare as prepare_remediation  # noqa: E402


def fixture():
    return dict(id='ENG-001', status='sourced', reason='Read original paper',
                event='Documented design snapshot', cutoff='Before commit choice',
                initial_facts=[dict(id='F1', text='Documented condition', source_ids=['S1'], availability='pre_decision')],
                evidence=[dict(id='E1', text='Documented mechanism', source_ids=['S1'], availability='post_decision')],
                outcome=dict(text='Observed documented outcome', source_ids=['S1']),
                interpretation='Attribution is distinct from observations', unknowns=[],
                sources=[dict(id='S1', url='https://research.google/pubs/', publisher='Authors',
                              published_at=None, checked_at='2026-10-25', source_type='primary',
                              supports=['F1', 'E1', 'outcome'])],
                attempts=['Opened and read paper'], phase2_conditions='One decision')


class ProvenanceTests(unittest.TestCase):
    def test_valid_record_can_have_unknown_publication_date(self):
        self.assertEqual(record_errors(fixture()), [])

    def test_unknown_source_or_claim_reference_rejected(self):
        record = fixture()
        record['evidence'][0]['source_ids'] = ['S2']
        self.assertTrue(any('source_ids' in e for e in record_errors(record)))
        record = fixture()
        record['sources'][0]['supports'].append('invented')
        self.assertTrue(any('unknown claim' in e for e in record_errors(record)))

    def test_sourced_requires_direct_outcome_support(self):
        record = fixture()
        record['sources'][0]['source_type'] = 'secondary'
        self.assertTrue(any('primary source' in e for e in record_errors(record)))
        record = fixture()
        record['outcome']['text'] = ''
        self.assertTrue(any('observed outcome' in e for e in record_errors(record)))

    def test_postdecision_or_unknown_information_cannot_be_initial(self):
        for availability in ('post_decision', 'unknown'):
            record = fixture()
            record['initial_facts'][0]['availability'] = availability
            self.assertTrue(any('pre_decision' in e for e in record_errors(record)))

    def test_blocked_is_not_unattempted_and_needs_no_invented_result(self):
        record = fixture()
        record.update(status='blocked', initial_facts=[], evidence=[], sources=[], outcome=dict(text='', source_ids=[]))
        self.assertEqual(record_errors(record), [])
        record['attempts'] = []
        self.assertTrue(any('attempts' in e for e in record_errors(record)))

    def test_duplicate_sources_and_reserved_urls_rejected(self):
        record = fixture()
        record['sources'].append(deepcopy(record['sources'][0]))
        self.assertTrue(any('unique' in e for e in record_errors(record)))
        record = fixture()
        record['sources'][0]['url'] = 'https://example.com/paper'
        self.assertTrue(any('real HTTP' in e for e in record_errors(record)))


class PhaseThreeIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_records(ROOT)
        cls.outputs = prepare(ROOT)
        cls.entries = read_yaml(ROOT / 'curriculum/2027.yaml')['entries']

    def test_all_historical_ids_assessed_without_ready_or_design_promotion(self):
        history = {e['id'] for e in self.entries if e['kind'] == 'historical'}
        self.assertEqual(len(history), 313)
        self.assertEqual(set(self.records), history)
        for entry in self.entries:
            if entry['id'] in history:
                self.assertEqual(entry['status'], self.records[entry['id']]['status'])
            else:
                self.assertEqual(entry['status'], 'candidate')
            self.assertNotEqual(entry['status'], 'ready')

    def test_migration_preserves_candidate_planning_without_training_material(self):
        for entry in self.entries:
            if entry['kind'] != 'historical':
                self.assertNotIn(entry['brief_path'], self.outputs)
                continue
            current = read_yaml(ROOT / entry['brief_path'])
            generated = yaml.safe_load(self.outputs[entry['brief_path']])
            self.assertEqual(current, generated)
            self.assertNotIn('opening', generated)
            self.assertNotIn('resolution', generated)
            self.assertEqual(generated['research'], self.records[entry['id']])
            original_material = generated['candidate_material']
            self.assertTrue(original_material)
            self.assertEqual(generated['planning'], current['planning'])

    def test_generators_are_read_only_and_exactly_reproducible(self):
        for relative, expected in self.outputs.items():
            self.assertEqual((ROOT / relative).read_text(), expected, relative)
        second = prepare(ROOT)
        self.assertEqual(self.outputs, second)

    def test_incomplete_coverage_fails_before_any_outputs_can_be_applied(self):
        incomplete = deepcopy(self.records)
        incomplete.pop('ENG-001')
        with patch('verify_sources.load_records', return_value=incomplete):
            with self.assertRaisesRegex(ValueError, 'all 313 historical IDs'):
                prepare(ROOT)

    def test_insufficient_quantitative_inputs_remain_blocked_without_fallback(self):
        # Frozen first-pass decisions retain their original meaning after a
        # separately recorded scope correction has actually been applied.
        first_pass = load_records(ROOT, apply_remediation=False)
        decisions = read_yaml(ROOT / 'curriculum/source-decisions-2027.yaml')['entries']
        self.assertEqual(len(decisions), 39)
        for decision in decisions:
            record = first_pass[decision['id']]
            self.assertFalse(record['scope_decision']['fallback_applied'])
            if decision['input_status'] == 'insufficient_this_round':
                self.assertEqual(record['status'], 'blocked')
                self.assertIn('source_assessment_status', record)
            else:
                self.assertEqual(record['status'], 'sourced')

    def test_rejected_slot_has_real_replacement_and_preserves_original(self):
        brief = read_yaml(ROOT / 'cases/engineering/ENG-157.yaml')
        self.assertEqual(brief['status'], 'sourced')
        self.assertIn('Rust', brief['scenario_title'])
        self.assertIn('Blaze', brief['candidate_material']['historical_case'])
        self.assertEqual(brief['planning']['revision_state'], 'awaiting_replacement')
        self.assertEqual(brief['research']['prior_assessment']['status'], 'rejected')
        self.assertEqual(brief['active_scope']['decision'], 'replace')

    def test_all_initial_failures_have_applied_scopes_and_direct_sources(self):
        first_pass = load_records(ROOT, apply_remediation=False)
        failures = {identifier for identifier, record in first_pass.items()
                    if record['status'] in {'blocked', 'rejected'}}
        self.assertEqual(len(failures), 126)
        for identifier in failures:
            with self.subTest(id=identifier):
                entry = next(e for e in self.entries if e['id'] == identifier)
                brief = read_yaml(ROOT / entry['brief_path'])
                self.assertEqual(brief['status'], 'sourced')
                self.assertTrue(brief['active_scope']['main_question'])
                self.assertEqual(brief['research']['prior_assessment']['status'], first_pass[identifier]['status'])
                self.assertEqual(record_errors(brief['research']), [])

    def test_incomplete_remediation_cannot_be_activated(self):
        index, resolutions, rows = assess(ROOT)
        rows[0]['state'] = 'pending'
        with patch('phase3_admission.assess', return_value=(index, resolutions, rows)):
            with self.assertRaisesRegex(ValueError, 'Cannot activate'):
                prepare_remediation(ROOT)


if __name__ == '__main__':
    unittest.main()
