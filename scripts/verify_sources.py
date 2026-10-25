"""Reproduce Phase 3 research records; offline checks do not verify web truth.

Maintainers must actually read sources before editing reports/research-*.md.
This command checks provenance references and synchronizes research, status and the readiness note.
It never creates openings, changes exercise focus, replaces events, or sets ready.
"""

import argparse
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import re
from urllib.parse import urlparse

import yaml

from common import ROOT, UniqueKeyLoader, local_path, read_yaml
from audit_curriculum import table
from remediation_data import active_resolutions, overlay_research, apply_current_scopes

NOTES = (
    'reports/research-engineering-a.md', 'reports/research-engineering-b.md',
    'reports/research-product.md', 'reports/research-product-b.md', 'reports/research-investing.md',
    'reports/research-investing-a.md', 'reports/research-investing-b.md',
)
REPORT = 'reports/source-verification.md'
INVENTORY = 'reports/source-verification.json'
DECISIONS = 'curriculum/source-decisions-2027.yaml'
RECORD_STATUSES = {'sourced', 'blocked', 'rejected'}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def record_errors(record):
    """Check research integrity, not factual accuracy or trainability."""
    errors = []
    if not isinstance(record, dict):
        return ['research record must be a mapping']
    for field in ('id', 'reason', 'event', 'cutoff', 'interpretation', 'phase2_conditions'):
        if not record.get(field):
            errors.append(f'missing {field}')
    if record.get('status') not in RECORD_STATUSES:
        errors.append('research status must be sourced/blocked/rejected')
    if not isinstance(record.get('attempts'), list) or not record['attempts']:
        errors.append('every assessment requires actual attempts')
    if not isinstance(record.get('unknowns'), list):
        errors.append('unknowns must be an explicit list')
    sources = record.get('sources')
    if not isinstance(sources, list):
        return errors + ['sources must be a list, possibly empty when blocked']
    source_map = {}
    for source in sources:
        if not isinstance(source, dict):
            errors.append('source must be a mapping')
            continue
        sid = source.get('id')
        if not nonempty(sid) or sid in source_map:
            errors.append('source IDs must be unique and nonempty')
            continue
        source_map[sid] = source
        try:
            raw_url = source.get('url')
            url = urlparse(raw_url) if isinstance(raw_url, str) else None
            host = (url.hostname or '') if url else ''
        except (ValueError, TypeError):
            host = ''
        if not host or url.scheme not in {'http', 'https'} or any(host == reserved or host.endswith('.' + reserved) for reserved in ('example.com', 'example.org', 'example.net', 'localhost')) or host.endswith(('.invalid', '.example', '.test', '.localhost')):
            errors.append(f'{sid}: real HTTP(S) source URL required')
        if not nonempty(source.get('publisher')) or not nonempty(source.get('checked_at')):
            errors.append(f'{sid}: publisher and checked_at required')
        if 'published_at' not in source:
            errors.append(f'{sid}: published_at must be explicit (null if unknown)')
        if source.get('source_type') not in {'primary', 'secondary'}:
            errors.append(f'{sid}: source_type must be primary/secondary')
        if not isinstance(source.get('supports'), list):
            errors.append(f'{sid}: supports must be a list')
    claims = {}
    initial = record.get('initial_facts')
    evidence = record.get('evidence')
    for field, items in (('initial_facts', initial), ('evidence', evidence)):
        if not isinstance(items, list):
            errors.append(f'{field} must be a list')
            continue
        for item in items:
            if not isinstance(item, dict) or not nonempty(item.get('id')) or not nonempty(item.get('text')):
                errors.append(f'{field}: claim requires id/text')
                continue
            cid = item['id']
            if cid in claims:
                errors.append(f'duplicate claim ID: {cid}')
            claims[cid] = item
            if item.get('availability') not in {'pre_decision', 'post_decision', 'unknown'}:
                errors.append(f'{cid}: explicit historical availability required')
            if field == 'initial_facts' and record.get('status') == 'sourced' and item.get('availability') != 'pre_decision':
                errors.append(f'{cid}: sourced initial facts must be pre_decision')
    outcome = record.get('outcome')
    if not isinstance(outcome, dict) or not isinstance(outcome.get('text'), str):
        errors.append('outcome must contain text (empty when not established)')
    elif outcome['text']:
        claims[outcome.get('id', 'outcome')] = outcome
    for cid, claim in claims.items():
        refs = claim.get('source_ids')
        if not isinstance(refs, list) or not refs or not set(refs) <= set(source_map):
            errors.append(f'{cid}: missing or unknown source_ids')
            continue
        for sid in refs:
            if cid not in source_map[sid].get('supports', []):
                errors.append(f'{sid}: does not declare support for {cid}')
    # Some records also trace attributed interpretations explicitly.
    interpretation = record.get('interpretation')
    if isinstance(interpretation, dict) and interpretation.get('id'):
        claims[interpretation['id']] = interpretation
    for sid, source in source_map.items():
        if set(source.get('supports', [])) - set(claims):
            errors.append(f'{sid}: supports unknown claim IDs')
    if record.get('status') == 'sourced':
        if not initial or not evidence or not outcome or not outcome.get('text'):
            errors.append('sourced requires initial facts, evidence and observed outcome/artifact')
        outcome_refs = outcome.get('source_ids', []) if outcome else []
        if not any(source_map.get(sid, {}).get('source_type') == 'primary' for sid in outcome_refs):
            errors.append('sourced event/outcome requires a directly supporting primary source')
    return errors


def load_records(root, apply_remediation=True):
    records = {}
    for relative in NOTES:
        path = local_path(root, relative)
        content = path.read_text(encoding='utf-8')
        blocks = re.findall(r'^```yaml\n(.*?)^```[ \t]*$', content, re.M | re.S)
        if not blocks:
            raise ValueError(f'No research records in {relative}')
        for block in blocks:
            record = yaml.load(block, Loader=UniqueKeyLoader)
            errors = record_errors(record)
            identifier = record.get('id') if isinstance(record, dict) else '?'
            if errors:
                raise ValueError(f'{relative} / {identifier}: ' + '; '.join(errors))
            if identifier in records:
                raise ValueError(f'Duplicate research ID: {identifier}')
            records[identifier] = {**record, 'record_path': relative}
    decisions = read_yaml(local_path(root, DECISIONS))['entries']
    by_id = {d['id']: d for d in decisions}
    index = read_yaml(local_path(root, 'curriculum/2027.yaml'))['entries']
    planning = read_yaml(local_path(root, 'curriculum/planning-2027.yaml'))['entries']
    quantitative = {e['id'] for e in planning if 'quantitative_plan' in e}
    if len(by_id) != len(decisions) or set(by_id) != quantitative:
        raise ValueError('Scope decisions must cover exactly all quantitative IDs')
    for identifier, decision in by_id.items():
        if decision.get('fallback_applied') is not False or not nonempty(decision.get('reason')):
            raise ValueError(f'No automatic fallback or unexplained scope decision: {identifier}')
        if decision.get('input_status') not in {'sufficient_for_scoped_comparison', 'insufficient_this_round'}:
            raise ValueError(f'Unknown quantitative input status: {identifier}')
        if identifier not in records:
            continue  # Full historical coverage is checked before any write in prepare().
        record = records[identifier]
        record['scope_decision'] = {**decision, 'decision_path': DECISIONS}
        if decision['input_status'] == 'insufficient_this_round':
            if decision.get('effective_status') != 'blocked':
                raise ValueError(f'Missing numerical inputs must remain blocked: {identifier}')
            record['source_assessment_status'] = record['status']
            record['source_assessment_reason'] = record['reason']
            record['status'] = 'blocked'
            record['reason'] = decision['reason'] + ' 尚未应用备用问题，原数量主线保持 blocked。'
        elif record['status'] != 'sourced':
            raise ValueError(f'Sufficient quantitative inputs require a sourced assessment: {identifier}')
    return overlay_research(records, active_resolutions(root)) if apply_remediation else records


def yaml_text(value):
    return yaml.safe_dump(value, allow_unicode=True, sort_keys=False, width=100)


def prepare(root=ROOT):
    root = Path(root)
    records = load_records(root)
    index = apply_current_scopes(read_yaml(root / 'curriculum/2027.yaml'), root)
    active = active_resolutions(root)
    history = {e['id']: e for e in index['entries'] if e['kind'] == 'historical'}
    if len(history) != 313 or set(records) != set(history):
        raise ValueError(f'Expected exactly all 313 historical IDs; missing={sorted(set(history)-set(records))}, extra={sorted(set(records)-set(history))}')
    outputs = {}
    rows = []
    for identifier, entry in history.items():
        record = records[identifier]
        brief = read_yaml(local_path(root, entry['brief_path']))
        if brief.get('id') != identifier or brief.get('kind') != 'historical':
            raise ValueError(f'Brief identity mismatch: {identifier}')
        if entry['status'] == 'ready' or brief.get('status') == 'ready':
            raise ValueError(f'Phase 3 cannot overwrite a ready Brief: {identifier}')
        # Preserve original material, calendar, title, focus and Phase 2 snapshot.
        brief['research'] = deepcopy(record)
        brief['status'] = entry['status'] = record['status']
        phase3_note = {
            'sourced': '已定位并阅读直接来源，研究素材见 research；完整 Brief 与 Case QA 尚未完成，不可用于训练。',
            'blocked': '已进行 Phase 3 核查但关键条件未满足，原因见 research；不可用于训练。',
            'rejected': '原选题不适合继续制作，理由与替换提案见 research；尚未换题，不可用于训练。',
        }[record['status']]
        if brief.get('production', {}).get('phase') != 4:
            brief['readiness_note'] = phase3_note
        outputs[entry['brief_path']] = yaml_text(brief)
        rows.append(dict(id=identifier, domain=entry['domain'], status=record['status'],
                         brief_path=entry['brief_path'], record_path=record['record_path'],
                         event=record['event'], cutoff=record['cutoff'], reason=record['reason']))
    outputs['curriculum/2027.yaml'] = yaml_text(index)
    counts = Counter(r['status'] for r in rows)
    numerical = [records[e['id']]['scope_decision'] for e in history.values() if 'scope_decision' in records[e['id']]]
    totals = [[domain] + [sum(r['domain'] == domain and r['status'] == status for r in rows) for status in ('sourced', 'blocked', 'rejected')] for domain in ('engineering', 'product', 'investing')]
    if active:
        numerical = [dict(id=r['id'], input_status='verified_scoped_inputs', reason=r['reason']) for r in active.values() if r['focus'] == 'quantitative-calibration']
    sufficient = sum(d['input_status'] in {'sufficient_for_scoped_comparison', 'verified_scoped_inputs'} for d in numerical)
    report = [
        '# Phase 3 来源验证',
        '核查日期：2026-10-25。全部 313 个历史条目均已逐项尝试，状态与理由见下表和相应研究记录。52 个微设计仍是 candidate。没有 ready 条目，未进入 Phase 4。',
        table(['领域', 'sourced', 'blocked', 'rejected'], totals),
        f"合计：{counts['sourced']} sourced、{counts['blocked']} blocked、{counts['rejected']} rejected。sourced 仅表示已定位并阅读支持所选节点的可信直接材料，未通过完整 Brief QA。",
        '## 事实与时点边界',
        '`research` 保存核源素材，不能作为 Consumer 的 opening。availability 是历史可知性，不能代替 Phase 4 的证据释放时机；post_decision/unknown 不能进入事前开场。cutoff 可以是明确的事务、版本或产品决策边界；需要精确日的案例在 Phase 4 固定，无法固定的不得 ready。',
        '投资 memo 的投资建议、公司融资公告、设计论文的实现描述分别是所观察的文档或行为；不能说成交易已经交割、投资已实现回报或经过独立复现。事后当事人记录须保留叙事局限。部分来源日期不详，published_at 为 null；未补造日期。',
        'Phase 2 的 review_status、revision_state 和 planning 是规划历史快照；当前核源状态以 canonical status 与 research 为准。原候选标题和 candidate_material 保留，研究 event 记录纠正后的锚点，尚未自动改号、改日期、改 focus 或应用备用题。',
        '## 需要重点处理的身份和替换',
        '- ENG-011 与 ENG-040 已分开核对：2024 与 2023 不同供电事故；不得混写成同一事件。',
        '- ENG-054：Google 2012 闰秒候选归属存疑；不能把其他公司的 Linux 故障写成 Google 故障。',
        '- ENG-080：2015 Bazel 发布时的远程缓存有路线图边界，不能写成所有能力当时已经提供。',
        '- ENG-117：尚未取得规划要求的单次 SSD 优化；保留 blocked，进入替换审议。',
        '- ENG-157：原 Blaze 候选因与 ENG-080 重复而 rejected；研究记录中的 Rust 1.52 回退提案仅是提案，尚未替换原日期槽。',
        '- INV-005：2005 Yelp memo 指此前天使融资后的首次风险融资，原“Series B”标签不可靠。INV-010：核实到的是 2015 Figma Series A/Preview，未确认原拟选 2016 独立轮次。',
        '- INV-034：找到 2019 a16z B 轮公告，仍缺独立付费留存及服务成本 cohort；不能复用 PRO-080 PMF 问卷补足，保留 blocked 并待替换审议。',
        '- PRO-013/025/044 等传播故事、年份或因果主张需按逐条记录处理，不因广为流传就升级。',
        '## 阻塞处理与后续',
        'blocked 包括读取失败、实际年份/版本未固定、缺同期行为、关键数值或条款不可核，以及规划节点与来源不符。它表示本轮未核实，不能据此断言资料不存在。每条 attempts 记录本轮实际尝试及限制，未打开的搜索摘要未当成已核事实。',
        '数量题只保留来源支持的口径；缺输入条目仍有 Phase 2 备用问题可审议，但本轮未自动应用，不能靠合成数字补主线。所有 blocked/rejected 保留当天槽位，待补源或显式修订。',
        '本脚本是离线引用、覆盖与同步检查，不能自动证明 URL 可访问、主张正确、无剧透或对话可运行。Phase 4 须再次核对具体要进入开场/证据池的主张，完善出处定位和时间线，再进行完整 Case QA。',
        '## 39 条数量主线复核',
        f'按 Phase 2 的原问题检查输入齐备性，{sufficient} 条可进行有边界的数量比较，{len(numerical)-sufficient} 条本轮未核齐。即使找到了可信机制或融资材料，缺原数量主线输入且尚未正式应用备用问题的条目仍为 blocked。研究笔记的原建议状态保存在 source_assessment_status；索引采用复核后的有效状态。',
        table(['ID', '数量输入状态', '复核理由'], [[d['id'], d['input_status'], d['reason']] for d in numerical]),
        '## 逐项核查结果',
        table(['ID / Brief', '状态', '核实事件 / 决策边界', '理由 / 研究记录'], [[f"[{r['id']}](../{r['brief_path']})", r['status'], str(r['event']) + '；' + str(r['cutoff']), str(r['reason']) + f"（[记录](../{r['record_path']}#{r['id'].lower()})）"] for r in rows]),
    ]
    if active:
        report = [
            '# Phase 3 来源验证（正式整改后）',
            '初轮核源后按用户要求补源、正式改题与换题。全部365个日期已通过制作前准入；本表仅记录来源状态，制作进度见progress.md。原始输入、ID和日期保留；旧研究笔记与source-decisions是初轮历史记录。',
            table(['领域', 'sourced', 'blocked', 'rejected'], totals),
            '当前单题范围以各Brief的active_scope为准；planning仍为Phase2历史快照。正式改题、动作迁移和替换的逐条理由见 [phase3-revisions.md](phase3-revisions.md)，365题准入见 [phase3-admission.md](phase3-admission.md)。',
            'sourced和制作前eligible均不表示训练ready；尚须Phase4完整材料、时点/剧透与Case QA以及Phase5协议验收。解释、公司自报和作者模型不能写成独立证实的因果或未披露历史事实。',
            '原39个数量主线的不足已通过补源或显式修订处理；不继续要求已取消的隐藏cohort、成本或股权权利输入。下列为当前数量题及已核范围；未把合成负载回填历史主线。',
            table(['ID', '输入状态', '范围理由'], [[d['id'], d['input_status'], d['reason']] for d in numerical]),
            table(['ID / Brief', '状态', '核实事件 / 决策边界', '理由 / 研究记录'], [[f"[{r['id']}](../{r['brief_path']})", r['status'], str(r['event']) + '；' + str(r['cutoff']), str(r['reason']) + f"（[记录](../{r['record_path']}#{r['id'].lower()})）"] for r in rows]),
        ]
    outputs[REPORT] = '\n\n'.join(report) + '\n'
    inventory = dict(phase=3, checked_at='2026-10-25', scope='manual_primary_source_research_not_ready_QA', counts=dict(counts), historical_total=313, micro_design_candidate=52, ready=0, quantitative_decisions=numerical, entries=rows)
    outputs[INVENTORY] = json.dumps(inventory, ensure_ascii=False, indent=2) + '\n'
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='explicitly synchronize records/status; default is read-only')
    args = parser.parse_args()
    try:
        outputs = prepare()
        stale = []
        for relative, expected in outputs.items():
            path = ROOT / relative
            if args.apply:
                path.write_text(expected, encoding='utf-8')
            elif not path.exists() or path.read_text(encoding='utf-8') != expected:
                stale.append(relative)
        if stale:
            raise ValueError(f'Research outputs out of sync: {", ".join(stale)}')
    except (ValueError, OSError, yaml.YAMLError) as exc:
        parser.exit(1, f'FAIL: {exc}\n')
    print(f'PASS: 313 historical assessments, source references and synchronized outputs ({"applied" if args.apply else "read-only"}); this is not external verification or ready QA')


if __name__ == '__main__':
    main()
