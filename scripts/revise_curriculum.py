"""Apply/check Phase 2 scope revisions without sourcing or making ready Briefs."""

import argparse
from collections import Counter
import csv
from pathlib import Path

import yaml

from audit_curriculum import FOCUS, load_notes, table
from common import ROOT, read_yaml

MANIFEST = "curriculum/planning-2027.yaml"
REPORT = "reports/phase2-revision-results.md"
POLICY = "curriculum/planning-policy.yaml"
REVISION_STATES = ("retained", "awaiting_source", "revised", "awaiting_replacement")


def tsv_by_id(path):
    with Path(path).open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    result = {}
    for row in rows:
        identifier = row.get("id")
        if not identifier or identifier in result or None in row or not all(isinstance(v, str) and v.strip() for v in row.values()):
            raise ValueError(f"Incomplete or duplicate planning row in {path}: {identifier}")
        result[identifier] = row
    return result


def yaml_text(data):
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100)


def prepare(root):
    root = Path(root)
    notes = load_notes(root)
    index = read_yaml(root / "curriculum/2027.yaml")
    entries = index["entries"]
    by_id = {e["id"]: e for e in entries}
    if len(entries) != 365 or len(by_id) != 365 or set(by_id) != set(notes):
        raise ValueError("Planning requires the same 365 unique source/index/review IDs")
    history = tsv_by_id(root / "curriculum/revision-plans-2027.tsv")
    design_rows = read_yaml(root / "curriculum/design-revisions-2027.yaml")["entries"]
    designs = {r["id"]: r for r in design_rows}
    if len(designs) != len(design_rows):
        raise ValueError("Duplicate design revision ID")
    numbers = tsv_by_id(root / "curriculum/quantitative-requirements-2027.tsv")
    policy = read_yaml(root / POLICY)
    replacements = policy["replacement_requests"]
    historical_targets = {e["id"] for e in entries if e["kind"] == "historical" and notes[e["id"]]["action"] == "revise"}
    design_targets = {e["id"] for e in entries if e["kind"] == "micro_design" and notes[e["id"]]["action"] == "revise"}
    replacement_targets = {identifier for identifier, row in notes.items() if row["action"] == "replace"}
    if set(history) != historical_targets or set(designs) != design_targets or set(replacements) != replacement_targets:
        raise ValueError("Revision inputs must cover exactly historical/design revise and replace targets")
    if set(numbers) != {e["id"] for e in entries if e["focus"] == "quantitative-calibration"}:
        raise ValueError("Every quantitative exercise must have exactly one input and fallback plan")
    if set(policy["revision_states"]) != set(REVISION_STATES):
        raise ValueError("Unknown revision states in planning policy")
    conditional = policy["conditional_requests"]
    if not set(conditional) <= set(by_id):
        raise ValueError("Conditional requests contain unknown IDs")
    for identifier, row in history.items():
        required = {"id", "anchor_request", "main_question", "expected_output", "evidence_requirements", "out_of_scope"}
        if set(row) != required:
            raise ValueError(f"Incomplete historical scope or evidence requirements: {identifier}")
    for identifier, row in designs.items():
        for field in ("title", "main_question", "expected_output", "scenario", "scoped_change", "out_of_scope"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(f"Missing design {field}: {identifier}")
        assumptions = row.get("planning_assumptions")
        if not isinstance(assumptions, list) or not assumptions or not all(isinstance(v, str) and v.strip() for v in assumptions):
            raise ValueError(f"Design requires explicit synthetic assumptions: {identifier}")
    for identifier, row in numbers.items():
        if row["fallback_focus"] not in set(FOCUS.values()) - {"quantitative-calibration", "constructive-design"}:
            raise ValueError(f"Invalid quantitative fallback: {identifier}")
    overlap = read_yaml(root / "reports/phase2-overlap-review.yaml")["clusters"]
    cluster_ids = Counter(c["id"] for c in overlap)
    if any(total != 1 for total in cluster_ids.values()):
        raise ValueError("Overlap cluster IDs must be unique")
    clusters_by_id = {identifier: [] for identifier in by_id}
    for cluster in overlap:
        if not set(cluster["ids"]) <= set(by_id):
            raise ValueError(f"Unknown member in cluster {cluster['id']}")
        for identifier in cluster["ids"]:
            clusters_by_id[identifier].append(cluster["id"])
    planning, outputs = [], {}
    scopes = {}
    for entry in entries:
        identifier = entry["id"]
        record = {
            "id": identifier, "date": str(entry["date"]),
            "revision_state": "retained", "policy_path": POLICY,
            "distinctness_clusters": clusters_by_id[identifier],
        }
        if identifier in history:
            row = history[identifier]
            record["revision_state"] = "awaiting_source"
            record["planned_exercise"] = {
                "planning_only": True,
                "anchor_request": row["anchor_request"],
                "anchor_status": "unverified_research_target",
                "main_question": row["main_question"],
                "expected_output": row["expected_output"],
                "evidence_to_verify": row["evidence_requirements"].split("；"),
                "out_of_scope": row["out_of_scope"],
            }
        elif identifier in designs:
            record["revision_state"] = "revised"
            record["planned_exercise"] = {"planning_only": True, "synthetic": True,
                                          **{k: v for k, v in designs[identifier].items() if k != "id"}}
        elif identifier in replacements:
            record["revision_state"] = "awaiting_replacement"
            record["replacement_request"] = replacements[identifier]
        if identifier in numbers:
            row = numbers[identifier]
            record["quantitative_plan"] = {
                "mainline_measure": row["mainline_measure"],
                "required_inputs": row["required_inputs"].split("；"),
                "missing_input_fallback": {"focus": row["fallback_focus"], "question": row["fallback_question"]},
                "fallback_applied": False,
                "input_verification": "not_started",
            }
        if identifier in conditional:
            record["source_identity_condition"] = conditional[identifier]
        scopes[identifier] = (
            record["planned_exercise"]["main_question"] if "planned_exercise" in record else
            record["replacement_request"]["desired_topic"] if "replacement_request" in record else
            notes[identifier]["note"]
        )
        entry["revision_state"] = record["revision_state"]
        planning.append(record)
        # These are planning fields only. All existing Brief content is preserved.
        brief = read_yaml(root / entry["brief_path"])
        brief["planning"] = {k: v for k, v in record.items() if k not in {"id", "date"}}
        outputs[entry["brief_path"]] = yaml_text(brief)
    manifest = {
        "phase": 2, "purpose": "修订训练范围；不是已核实事实、开场材料或完整 Brief",
        "policy_path": POLICY, "entries": planning,
    }
    outputs[MANIFEST] = yaml_text(manifest)
    outputs["curriculum/2027.yaml"] = yaml_text(index)
    states = Counter(r["revision_state"] for r in planning)
    report = [
        "# Phase 2 修订落实记录",
        "本轮把初审意见落实为生产端的候选训练范围。原审核结论 164 accepted / 200 revise / 1 replace 保留，另以 revision_state 记录落实进度；两者都不表示来源或训练验收。Phase 3 尚未开始。",
        "## 落实进度",
        table(["修订进度", "条数", "含义"], [[state, states[state], policy["revision_states"][state]] for state in REVISION_STATES]),
        "191 个历史修改项已各自明确一个拟研究节点、一个主要问题、一项输出、所需证据和排除范围；这些节点都是研究目标，日期、版本和事件身份未确认为事实。9 个设计修改项已明确合成前提和相关变化。ENG-157 只落实替换准入条件，未指定或声称找到真实替代事件。",
        "## 使用规则",
        "`curriculum/planning-2027.yaml` 是本轮完整规划汇总，每个候选 Brief 的 `planning` 与之同步。后续 Phase 3/4 以 planned_exercise 规定的范围研究和制作题目，candidate_material 仅用于原始追溯；不能再直接按原始多年综述扩写。",
        "规划层不设置历史 as-of 日期、不填来源和真实结果；不生成 opening、evidence_pool 或完整评价协议。所有 365 条 status 均保持 candidate。需要改变训练状态、认知动作或实际换题时，应另行核实并记录映射。",
        "## 39 条数量题的处理",
        "每题列出了所需输入、计算口径和缺数据时的具体替代问题。历史主线只用可追溯且事前可知的数字；允许透明的推导，不允许缺数字就补合成值。反事实合成数字必须明确切换且只属于附加练习。",
        "39 条仍保留原 quantitative-calibration 动作，fallback_applied 均为 false。只有核源证明输入不足后才手动采纳预设替代问题，并同步动作映射。",
        table(["ID", "主线计算", "必须查到的输入", "缺失时动作 / 问题"], [
            [identifier, row["mainline_measure"], row["required_inputs"], row["fallback_focus"] + "：" + row["fallback_question"]]
            for identifier, row in sorted(numbers.items())]),
        "## 重复与条件处理",
        "ENG-157：保留原日期、ID 和素材，拟补一个独立构建工具失败/恢复/回退节点，不重复现有缓存、特性合并或 affected 图问题。ENG-011：必须证明拟选 2024 事件与 ENG-040 独立。INV-034：必须有独立于 PRO-080 问卷的融资和付费 cohort 材料。ENG-117：必须定位单次 SSD 成本优化。后二者及 ENG-011 不满足条件就进入替换队列。",
        "未来替代优先降低 Cloudflare 可靠性集中度，但本轮没有为调整比例而编造新事件。保留全部日历，不立即搬动同周 Dropbox 题：工程题聚焦自建阈值，投资题必须额外分解客户/套餐结构。",
        "以下逐簇给出各成员当前的唯一范围。Phase 3 若发现无法形成不同条件、观察或输出，应再收窄或换题；换公司名本身不算分化。",
    ]
    for cluster in overlap:
        report.extend([f"### {cluster['id']}", cluster["assessment"], "处理条件：" + cluster["action"],
                       table(["成员", "本轮确定的任务范围"], [[identifier, scopes[identifier]] for identifier in cluster["ids"]])])
    report.extend([
        "## 200 个修改项与替换槽位",
        "下面的问题都是规划文字，不得在未核源时作为当时已知事实给学员。设计题的数值和政策只属于明确标记的合成场景。",
        table(["ID", "进度", "落实后的单一问题 / 替换目标"], [[r["id"], r["revision_state"], scopes[r["id"]]] for r in planning if r["revision_state"] != "retained"]),
        "## 仍需后续证据的问题",
        "独立事件、具体版本、事前日期、公开数字、真实交易权利与结果都仍待 Phase 3；设计约束虽已收窄，也仍需 Phase 4 的完整 Brief 与 Phase 5 对话 QA。范围修订完成不等于训练准备完成。用户要求先处理 Phase 2，本轮结束后停止，不自动进入 Phase 3。",
    ])
    outputs[REPORT] = "\n\n".join(report) + "\n"
    return outputs, states


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--apply", action="store_true", help="Write scope metadata and generated planning outputs")
    args = parser.parse_args()
    try:
        outputs, states = prepare(args.root)
        if args.apply:
            for rel, content in outputs.items():
                (args.root / rel).write_text(content, encoding="utf-8")
        else:
            for rel, expected in outputs.items():
                path = args.root / rel
                if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                    raise ValueError(f"Missing/stale planning output: {rel}")
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
        raise SystemExit(f"Planning revision failed: {exc}") from exc
    print(f"PASS: 365 planning records; {dict(states)}; 39 quantitative gates; training status unchanged.")


if __name__ == "__main__":
    main()
