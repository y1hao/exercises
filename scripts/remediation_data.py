"""Phase 3 scope decisions. Importing this module never writes or uses network."""

from copy import deepcopy
from pathlib import Path
import re

import yaml

from common import UniqueKeyLoader, local_path, read_yaml

MANIFEST = 'curriculum/active-scopes-2027.yaml'
NOTES = tuple('reports/remediation-' + suffix + '.md' for suffix in (
    'engineering-a', 'engineering-b', 'product', 'investing',
))
DESIGNS = 'curriculum/design-admission-2027.yaml'
FOCUSES = {'causal-modeling', 'prediction-counterfactual', 'hypothesis-diagnosis',
           'constrained-decision', 'evidence-selection', 'quantitative-calibration',
           'boundary-transfer', 'constructive-design'}


def load_resolutions(root, complete=False):
    root = Path(root)
    result = {}
    for relative in NOTES:
        if not (root / relative).exists():
            if complete:
                raise ValueError(f'Missing remediation input: {relative}')
            continue
        content = local_path(root, relative).read_text(encoding='utf-8')
        blocks = re.findall(r'^```yaml\n(.*?)^```[ \t]*$', content, re.M | re.S)
        for block in blocks:
            row = yaml.load(block, Loader=UniqueKeyLoader)
            if not isinstance(row, dict) or not row.get('id'):
                raise ValueError(f'Invalid resolution in {relative}')
            identifier = row['id']
            if identifier in result:
                raise ValueError(f'Duplicate resolution ID: {identifier}')
            result[identifier] = {**row, 'record_path': relative}
    if (root / DESIGNS).exists():
        for row in read_yaml(local_path(root, DESIGNS))['entries']:
            if row['id'] in result:
                raise ValueError(f'Duplicate resolution ID: {row["id"]}')
            result[row['id']] = {**row, 'record_path': DESIGNS}
    return result


def active_resolutions(root):
    path = Path(root) / MANIFEST
    if not path.exists():
        return {}
    manifest = read_yaml(local_path(root, MANIFEST))
    if manifest.get('phase') != 3 or manifest.get('all_eligible') is not True:
        raise ValueError('An active scope manifest requires all 365 admissions')
    rows = load_resolutions(root, complete=True)
    if len(rows) != 365 or any(r.get('admission') != 'eligible' for r in rows.values()):
        raise ValueError('Active scopes cannot silently apply an incomplete remediation')
    return rows


def apply_current_scopes(index, root, rows=None):
    rows = active_resolutions(root) if rows is None else rows
    for entry in index['entries']:
        if entry['id'] in rows:
            row = rows[entry['id']]
            entry['focus'] = row['focus']
            entry['subdomain'] = row['subdomain']
    return index


def overlay_research(records, resolutions):
    records = deepcopy(records)
    for identifier, row in resolutions.items():
        if identifier not in records:
            continue
        old = records[identifier]
        record = deepcopy(row['research'])
        record['record_path'] = row['record_path']
        record['prior_assessment'] = {
            'status': old['status'], 'reason': old['reason'],
            'record_path': old['record_path'],
        }
        record['remediation_decision'] = row['decision']
        records[identifier] = record
    return records


def scope_record(row):
    keys = ('decision', 'main_question', 'expected_output', 'out_of_scope',
            'reason', 'record_path', 'quantitative_inputs', 'design_basis')
    return {k: deepcopy(row[k]) for k in keys if k in row}
