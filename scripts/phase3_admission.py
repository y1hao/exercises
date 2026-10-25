"""Check Phase 3 preparation for every slot, without creating Phase 4 Briefs.

--progress writes an honest work-in-progress report. --apply is permitted only
after every slot has an eligible, validated decision. It is not ready promotion.
"""

import argparse
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path

import yaml

from common import ROOT, local_path, read_yaml
from audit_curriculum import FOCUS, load_notes, table
from remediation_data import (MANIFEST, FOCUSES, load_resolutions, scope_record,
                              overlay_research, apply_current_scopes)
from verify_sources import record_errors, load_records, yaml_text

REPORT = 'reports/phase3-admission.md'
SUMMARY = 'reports/phase3-admission.json'


def resolution_errors(row, kind):
    errors = []
    for field in ('id', 'scenario_title', 'subdomain', 'main_question',
                  'expected_output', 'out_of_scope', 'reason', 'admission_reason'):
        if not isinstance(row.get(field), str) or not row[field].strip():
            errors.append(f'missing {field}')
    if row.get('decision') not in {'retain', 'reframe', 'replace'}:
        errors.append('decision must be retain/reframe/replace')
    if row.get('focus') not in FOCUSES:
        errors.append('unknown cognitive focus')
    if row.get('admission') not in {'eligible', 'pending'}:
        errors.append('admission must be eligible/pending')
    if row.get('admission') != 'eligible':
        return errors
    if kind == 'historical':
        research = row.get('research', {})
        errors.extend(record_errors(research))
        if research.get('id') != row['id'] or research.get('status') != 'sourced':
            errors.append('eligible history requires same-ID sourced research')
        if len(research.get('initial_facts', [])) < 2 or len(research.get('evidence', [])) < 2:
            errors.append('eligible history requires two substantive initial facts and two evidence items')
        if row.get('focus') == 'constructive-design':
            errors.append('historical exercises cannot become synthetic designs')
        if row.get('focus') == 'quantitative-calibration':
            inputs = row.get('quantitative_inputs', [])
            if len(inputs) < 2:
                errors.append('quantitative scope needs actual traceable numerical inputs')
            sources = {s['id'] for s in research.get('sources', [])}
            for item in inputs:
                if (not isinstance(item, dict) or not item.get('name') or not item.get('unit')
                        or type(item.get('value')) not in {int, float}
                        or not item.get('source_ids') or not set(item['source_ids']) <= sources):
                    errors.append('invalid quantitative input or source reference')
    else:
        basis = row.get('design_basis', {})
        if row.get('focus') != 'constructive-design' or basis.get('synthetic') is not True:
            errors.append('design preparation must be explicitly synthetic')
        for field in ('assumptions', 'feasibility_reason', 'discriminating_change',
                      'evaluation_basis', 'acceptable_tradeoffs'):
            if not basis.get(field):
                errors.append(f'missing design_basis.{field}')
    return errors


def assess(root=ROOT):
    root = Path(root)
    index = read_yaml(root / 'curriculum/2027.yaml')
    resolutions = load_resolutions(root)
    entries = {e['id']: e for e in index['entries']}
    if set(resolutions) - set(entries):
        raise ValueError('Unknown IDs in remediation inputs')
    rows = []
    for identifier, entry in entries.items():
        row = resolutions.get(identifier)
        errors = resolution_errors(row, entry['kind']) if row else []
        state = 'unassessed' if row is None else 'invalid' if errors else row['admission']
        rows.append(dict(id=identifier, date=str(entry['date']), kind=entry['kind'],
                         domain=entry['domain'], brief_path=entry['brief_path'],
                         state=state, errors=errors,
                         reason=row.get('admission_reason') if row else '尚未记录本轮准入',
                         decision=row.get('decision') if row else None,
                         title=row.get('scenario_title') if row else None))
    return index, resolutions, rows


def report_outputs(rows, complete):
    counts = Counter(r['state'] for r in rows)
    text = [
        '# Phase 3 制作前准入',
        '本轮按用户要求先解决补源、改题和换题。没有进入 Phase 4，不生成 opening、完整 evidence_pool 或 ready 状态。',
        f"逐题准入：{dict(counts)}。全部可进入制作：{'是' if complete else '否'}；未通过者不能因文件存在或初轮 sourced 而略过。",
        'eligible 表示当前单题范围有可制作的事实/约束基础；不是完整训练 QA，也不表示历史结果能证明唯一正确选择。pending 是已记录但待复核，unassessed 是未写本轮判断，invalid 表示记录未通过引用或素材检查。',
        table(['ID', '日期', '准入', '动作', '当前题目', '缺口 / 复核理由'], [[r['id'], r['date'], r['state'], r['decision'] or '', r['title'] or '', '; '.join(r['errors']) or r['reason']] for r in rows]),
    ]
    summary = dict(phase=3, all_eligible=complete, counts=dict(counts), entries=rows)
    return {REPORT: '\n\n'.join(text) + '\n', SUMMARY: json.dumps(summary, ensure_ascii=False, indent=2) + '\n'}


def prepare(root=ROOT, progress=False):
    root = Path(root)
    index, resolutions, rows = assess(root)
    complete = len(rows) == 365 and all(r['state'] == 'eligible' for r in rows)
    outputs = report_outputs(rows, complete)
    if progress:
        return outputs, False
    if not complete:
        raise ValueError(f'Cannot activate Phase 4 preparation: {dict(Counter(r["state"] for r in rows))}')
    original_notes = load_notes(root)
    old_records = load_records(root, apply_remediation=False)
    research = overlay_research(old_records, resolutions)
    mappings = []
    for entry in index['entries']:
        row = resolutions[entry['id']]
        brief = read_yaml(local_path(root, entry['brief_path']))
        if entry['status'] == 'ready' or brief.get('status') == 'ready':
            raise ValueError('Phase 3 does not overwrite ready training')
        original_title = brief['candidate_material'].get('historical_case', brief['candidate_material'].get('title'))
        mappings.append(dict(id=entry['id'], date=str(entry['date']),
                             old_title=original_title, new_title=row['scenario_title'],
                             old_focus=FOCUS[original_notes[entry['id']]['focus']], new_focus=row['focus'],
                             decision=row['decision'], reason=row['reason'], record_path=row['record_path']))
        brief['scenario_title'] = row['scenario_title']
        brief['active_scope'] = scope_record(row)
        brief['phase4_admission'] = dict(state='eligible', reason=row['admission_reason'], report_path=REPORT)
        if entry['kind'] == 'historical':
            brief['research'] = research[entry['id']]
            brief['status'] = entry['status'] = 'sourced'
            brief['readiness_note'] = '已定位并阅读直接来源，研究素材见 research；完整 Brief 与 Case QA 尚未完成，不可用于训练。'
        else:
            brief['status'] = entry['status'] = 'candidate'
            brief['readiness_note'] = '合成题的范围、约束与可评价性已通过制作前准入；尚未制作完整 Brief 或通过 Case QA，不可训练。'
        outputs[entry['brief_path']] = yaml_text(brief)
    apply_current_scopes(index, root, resolutions)
    outputs['curriculum/2027.yaml'] = yaml_text(index)
    outputs[MANIFEST] = yaml_text(dict(phase=3, all_eligible=True, entries=mappings))
    outputs['reports/phase3-revisions.md'] = '# Phase 3 正式改题映射\n\n保留全部日期、ID与原始候选素材。下列变更已正式采用；不是 Phase 4 或 ready 晋级。\n\n' + table(
        ['ID', '日期', '动作', '原题', '现题', '原动作 → 现动作', '理由'],
        [[r['id'], r['date'], r['decision'], r['old_title'], r['new_title'], r['old_focus'] + ' → ' + r['new_focus'], r['reason']] for r in mappings]) + '\n'
    return outputs, True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--progress', action='store_true', help='write only preparation progress; never activate scopes')
    args = parser.parse_args()
    try:
        outputs, complete = prepare(progress=args.progress)
        stale = []
        for relative, expected in outputs.items():
            path = ROOT / relative
            if args.apply or args.progress:
                path.write_text(expected, encoding='utf-8')
            elif not path.exists() or path.read_text(encoding='utf-8') != expected:
                stale.append(relative)
        if stale:
            raise ValueError(f'Admission outputs out of sync: {stale}')
    except (ValueError, OSError, yaml.YAMLError) as exc:
        parser.exit(1, f'FAIL: {exc}\n')
    print('All 365 admissions eligible; Phase 4 NOT started.' if complete else 'Progress only; incomplete admission, no active curriculum changes.')


if __name__ == '__main__':
    main()
