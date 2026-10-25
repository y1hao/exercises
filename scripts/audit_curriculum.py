"""Rebuild Phase 2 artifacts from individually reviewed notes; never verify history.

Default is a read-only reproducibility check. --apply explicitly updates only the
index's focus/review_status fields and the generated audit artifacts.
"""

import argparse
from collections import Counter, defaultdict
import csv
from datetime import date
import json
from pathlib import Path
import re

import yaml

from common import ROOT, read_yaml, write_yaml

FOCUS = {
    "c": "causal-modeling", "p": "prediction-counterfactual",
    "h": "hypothesis-diagnosis", "d": "constrained-decision",
    "e": "evidence-selection", "q": "quantitative-calibration",
    "b": "boundary-transfer", "x": "constructive-design",
}
FOCUS_LABELS = {
    "causal-modeling": "因果机制重建", "prediction-counterfactual": "预测 / 反事实",
    "hypothesis-diagnosis": "竞争假说诊断", "constrained-decision": "约束下决策",
    "evidence-selection": "高信息价值证据选择", "quantitative-calibration": "数量级估计 / 校准",
    "boundary-transfer": "适用边界 / 跨域迁移", "constructive-design": "主动构造",
}
AREAS = {
    "engineering": {
        "distributed-systems": ("分布式与一致性", "distributed_consistency distributed_messaging distributed_sync data_streaming"),
        "developer-tools": ("开发者工具 / 构建系统", "developer_tooling_build build_tools developer_environment agent_devtools"),
        "reliability": ("可靠性", "reliability_diagnosis reliability_platform workflow_control_plane"),
        "architecture-api": ("架构与 API", "architecture_api api_sdk data_api_evolution"),
        "runtime-concurrency": ("运行时 / 并发", "runtime_concurrency runtime_performance"),
        "storage-query": ("存储 / 查询", "data_storage observability_data"),
        "security-isolation": ("安全 / 隔离", "security_isolation security_audit security_multitenancy"),
        "performance-cost": ("性能 / 成本", "performance_cost platform_cost"),
    },
    "product": {
        "user-value": ("用户问题 / 价值", "user_research_value"),
        "interaction-activation": ("交互 / 激活", "ux_activation activation_ux trust_behavior collaboration_ux workflow_automation"),
        "pricing-monetization": ("定价 / 变现", "pricing_monetization pricing_packaging"),
        "retention-workflow": ("留存 / 工作流", "retention_workflow retention_jobs habitless_workflow collaboration_adoption discovery_content"),
        "distribution-growth": ("分发 / 增长", "distribution_growth"),
        "network-marketplace": ("网络效应 / Marketplace", "network_marketplaces marketplace_trust"),
        "positioning-strategy": ("定位 / 竞争 / Pivot", "strategy_pivot roadmap_strategy"),
        "b2b-adoption": ("B2B 采购 / 采用", "b2b_adoption"),
    },
    "investing": {
        "pmf-growth-quality": ("PMF / 增长质量", "pmf_traction marketplace_liquidity validation_experiment"),
        "unit-economics": ("Unit Economics", "unit_economics hardware_business_model pricing_validation"),
        "valuation-terms-sizing": ("估值 / 交易条款 / 仓位", "valuation_terms portfolio_allocation"),
        "market-timing": ("市场规模 / 时机", "market_timing geographic_expansion wedge_market_entry"),
        "moat-competition": ("竞争壁垒", "moat_competition competitive_positioning oss_business_model"),
        "funding-survival-exit": ("融资 / 生存 / 退出", "funding_survival_exit"),
        "founder-execution": ("创始团队 / 执行", "founder_execution distribution_gtm regulated_enterprise_gtm investment_diligence"),
    },
}
FRAMES = {
    "technical": "技术机制 / 约束", "opportunity": "机会 / 采用叙事",
    "stress": "事故 / 生存压力叙事", "contested": "争议 / 混合权衡叙事",
    "synthetic": "合成设计",
}
ARTIFACTS = ("reports/curriculum-review.yaml", "reports/curriculum-audit.json", "reports/curriculum-audit.md", "reports/curriculum-revisions.md")


def load_notes(root):
    with (root / "reports/phase2-review-notes.tsv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    notes = {}
    for row in rows:
        identifier = row.get("id")
        if not identifier or identifier in notes:
            raise ValueError(f"Missing/duplicate review ID: {identifier}")
        if row.get("action") not in {"accepted", "revise", "replace"}:
            raise ValueError(f"Invalid audit action: {identifier}")
        if row.get("focus") not in FOCUS or row.get("frame") not in FRAMES:
            raise ValueError(f"Invalid focus/frame: {identifier}")
        if not row.get("note", "").strip() or None in row:
            raise ValueError(f"Invalid review note: {identifier}")
        notes[identifier] = row
    return notes


def entity(title):
    # Textual entity hints only: this is neither corporate attribution nor an event key.
    aliases = (
        (r"Cloudflare", "Cloudflare"), (r"GitHub", "GitHub"),
        (r"Google", "Google"), (r"AWS|Amazon", "Amazon/AWS"),
        (r"Meta|Facebook", "Meta/Facebook"), (r"Microsoft|\.NET|VS Code", "Microsoft"),
        (r"JVM|Java |JavaScript", "JavaScript" if "JavaScript" in title else "Java/JVM"),
    )
    for pattern, label in aliases:
        if re.search(pattern, title):
            return label
    return re.split(r"[\s（(]", title)[0]


def content_area(domain, subdomain, identifier):
    # The SDK exercise is primarily an API contract, not a storage design.
    if identifier == "DES-006":
        return "architecture-api"
    for area, (_, values) in AREAS[domain].items():
        if subdomain in values.split():
            return area
    raise ValueError(f"Unmapped content area: {identifier} {domain}/{subdomain}")


def build(root):
    index = read_yaml(root / "curriculum/2027.yaml")
    original = {r["id"]: r for r in read_yaml(root / "curriculum_2027_complete.yaml")["slots"]}
    notes = load_notes(root)
    identifiers = [e["id"] for e in index["entries"]]
    if len(identifiers) != 365 or len(set(identifiers)) != 365 or set(notes) != set(identifiers) or set(original) != set(identifiers):
        raise ValueError("Audit must cover exactly the 365 source/index IDs once each")
    overlap = read_yaml(root / "reports/phase2-overlap-review.yaml")
    cluster_by_id = defaultdict(list)
    seen_clusters = set()
    for cluster in overlap["clusters"]:
        cid, members = cluster["id"], cluster["ids"]
        if cid in seen_clusters or len(members) < 2 or len(members) != len(set(members)) or not set(members) <= set(identifiers):
            raise ValueError(f"Invalid overlap cluster: {cid}")
        if not cluster.get("assessment") or not cluster.get("action"):
            raise ValueError(f"Incomplete overlap cluster: {cid}")
        seen_clusters.add(cid)
        for identifier in members:
            cluster_by_id[identifier].append(cid)
    reviews, revisions = [], []
    for entry in index["entries"]:
        identifier = entry["id"]
        row, note = original[identifier], notes[identifier]
        design = entry["kind"] == "micro_design"
        if design != (note["focus"] == "x") or design != (note["frame"] == "synthetic"):
            raise ValueError(f"Design focus/frame mismatch: {identifier}")
        title = row["title"] if design else row["historical_case"]
        original_focus = row["primary_cognitive_move"] if design else row["planned_cognitive_move"]
        family = FOCUS[note["focus"]]
        area = content_area(entry["domain"], row["subdomain"], identifier)
        reviews.append({
            "id": identifier, "date": str(entry["date"]), "kind": entry["kind"],
            "domain": entry["domain"], "candidate_title": title,
            "event_anchor_basis": "synthetic_constraints" if design else "candidate_title_not_source_verified",
            "content_area": area,
            "primary_cognitive_move": family, "secondary_cognitive_moves": [],
            "original_cognitive_move": original_focus,
            "review_status": note["action"], "scope_and_rationale": note["note"],
            "candidate_narrative_frame": note["frame"],
            "observed_outcome": "not_applicable_synthetic" if design else "unverified",
            "source_verification": "not_performed_in_phase2",
            "overlap_clusters": cluster_by_id[identifier],
        })
        if "revision_state" in entry:
            reviews[-1]["revision_state"] = entry["revision_state"]
            reviews[-1]["planning_path"] = "curriculum/planning-2027.yaml"
        revisions.append({
            "id": identifier, "date": str(entry["date"]),
            "old_focus": original_focus.replace("_", "-"), "new_focus": family,
            "review_status": note["action"],
        })
        entry["focus"] = family
        entry["review_status"] = note["action"]
    groups = defaultdict(list)
    entity_ids = defaultdict(list)
    for review in reviews:
        iso = date.fromisoformat(review["date"]).isocalendar()
        groups[f"{iso.year}-W{iso.week:02d}"].append(review)
        if review["kind"] == "historical":
            entity_ids[entity(review["candidate_title"])].append(review["id"])
    weeks = []
    weekly_notes = read_yaml(root / "reports/phase2-weekly-review.yaml")["weeks"]
    followup_weeks = set()
    for week, rows in sorted(groups.items()):
        entity_count = Counter(entity(r["candidate_title"]) for r in rows if r["kind"] == "historical")
        moves = Counter(r["primary_cognitive_move"] for r in rows)
        flags = []
        if max(entity_count.values(), default=0) >= 3:
            flags.append("same_textual_entity_at_least_3")
        if max(moves.values(), default=0) >= 4:
            flags.append("same_primary_move_at_least_4")
        neighbors = Counter(cid for row in rows for cid in row["overlap_clusters"])
        repeated_neighbors = {cid: total for cid, total in neighbors.items() if total >= 2}
        followup = max(entity_count.values(), default=0) >= 2 or max(moves.values(), default=0) >= 3 or bool(repeated_neighbors)
        if followup:
            followup_weeks.add(week)
            if not weekly_notes.get(week):
                raise ValueError(f"Weekly density signal has no individual review: {week}")
        weeks.append({"iso_week": week, "dates": [r["date"] for r in rows],
                      "entity_hints": dict(sorted(entity_count.items())),
                      "cognitive_moves": dict(sorted(moves.items())), "flags": flags,
                      "repeated_overlap_clusters": dict(sorted(repeated_neighbors.items())),
                      "followup_review": weekly_notes.get(week)})
    if set(weekly_notes) != followup_weeks:
        raise ValueError("Weekly review notes must match all lower-threshold density signals")
    counts = lambda values: dict(sorted(Counter(values).items()))
    reliability = [row for row in original.values() if row["track"] == "engineering" and row["subdomain"] == "reliability_diagnosis"]
    summary = {
        "scope": "phase2_planning_review_no_source_verification",
        "total": len(reviews), "review_status": counts(r["review_status"] for r in reviews),
        "kind_domain": counts(f"{r['kind']}/{r['domain']}" for r in reviews),
        "content_areas": counts(f"{r['domain']}/{r['content_area']}" for r in reviews),
        "cognitive_moves": counts(r["primary_cognitive_move"] for r in reviews),
        "historical_cognitive_moves": counts(r["primary_cognitive_move"] for r in reviews if r["kind"] == "historical"),
        "original_cognitive_moves": counts(r["original_cognitive_move"] for r in reviews),
        "candidate_frames": counts(r["candidate_narrative_frame"] for r in reviews),
        "investing_historical_frames": counts(r["candidate_narrative_frame"] for r in reviews if r["domain"] == "investing" and r["kind"] == "historical"),
        "actions_by_kind_domain": {key: counts(r["review_status"] for r in reviews if f"{r['kind']}/{r['domain']}" == key)
                                   for key in sorted({f"{r['kind']}/{r['domain']}" for r in reviews})},
        "entity_hints": [{"label": label, "count": len(ids), "ids": ids} for label, ids in
                         sorted(entity_ids.items(), key=lambda item: (-len(item[1]), item[0]))],
        "engineering_reliability_concentration": {
            "total": len(reliability),
            "cloudflare": sum("Cloudflare" in row["historical_case"] for row in reliability),
            "basis": "original_candidate_titles_not_verified_history",
        },
        "overlap_clusters": overlap["clusters"], "weekly_review": weeks,
        "weekly_flag_thresholds": {"same_textual_entity": 3, "same_primary_move": 4},
        "weekly_followup_thresholds": {"same_textual_entity": 2, "same_primary_move": 3, "same_overlap_cluster": 2},
        "weekly_flag_limitations": "仅用于定位密度风险，不等于重复事件；部分首尾 ISO 周不足七天。",
        "verified_historical_outcomes": 0, "date_id_or_topic_replacements_applied": 0,
        "revision_progress": counts(e.get("revision_state", "identified") for e in index["entries"]),
    }
    audit = {"basis": summary["scope"], "status_semantics": "accepted 仅表示保留选题，不是事实、Brief 或 ready 验收", "entries": reviews}
    return index, audit, summary, revisions


def table(headers, rows):
    return "\n".join(["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)] +
                     ["| " + " | ".join(str(cell).replace("|", "\\|") for cell in row) + " |" for row in rows])


def render_report(summary):
    actions = summary["review_status"]
    flags = [w for w in summary["weekly_review"] if w["flags"]]
    followups = [w for w in summary["weekly_review"] if w["followup_review"]]
    design_revise = sum(counts.get("revise", 0) for key, counts in summary["actions_by_kind_domain"].items() if key.startswith("micro_design/"))
    sections = [
        "# Phase 2 全年课程审核\n",
        f"已通读并记录 365 条候选的具体范围与处理意见：accepted {actions.get('accepted', 0)}、revise {actions.get('revise', 0)}、replace {actions.get('replace', 0)}。",
        "这是课程规划审核，未查询外部资料、未验证历史事实或结果；accepted 仅指保留选题。Phase 2 结束时所有条目为 candidate；这是规划历史快照，当前核源状态见 source-verification.md。",
        "逐条意见以 `phase2-review-notes.tsv` 为维护输入，`curriculum-review.yaml` 为完整机器可读记录；分布、周内检查与聚类汇总见 `curriculum-audit.json`。原始输入、日期、ID 和候选素材全部保留。\n",
        "## 领域和审核动作\n",
        table(["类型 / 领域", "数量", "accepted", "revise", "replace"],
              [[key, total] + [summary["actions_by_kind_domain"][key].get(a, 0) for a in ("accepted", "revise", "replace")]
               for key, total in summary["kind_domain"].items()]),
        "\n内容领域采用 8 个工程、8 个产品、7 个创投类别。历史候选的原始分类按统一名称映射；微设计按主要交付物归类，保留原 subdomain。安全、信任等跨领域因素仍见逐条意见，不被单个主类别穷尽。\n",
    ]
    for domain, areas in AREAS.items():
        rows = [[label, summary["content_areas"].get(f"{domain}/{key}", 0)] for key, (label, _) in areas.items()]
        sections.extend([f"### {domain}\n", table(["主要内容领域（含微设计）", "次数"], rows), ""])
    sections.extend([
        "所有规定主领域都有候选覆盖；微设计为工程 22、产品 18、创投 12，并非全部高并发设计。计数只说明规划覆盖，不证明各题机制独立或材料充足。\n",
        "## 认知动作校准\n",
        table(["主要认知动作", "全年", "历史"], [[label, summary["cognitive_moves"].get(key, 0), summary["historical_cognitive_moves"].get(key, 0)] for key, label in FOCUS_LABELS.items()]),
        "\n每条只保留一个主要动作；本阶段未额外分配次要动作（列表为空，后续如需增加最多两项）。",
        "原始动作标签呈轮换式分布（根据候选序列观察），且部分与题意不符。PRO-002 无漏斗数字却标数量估计，改为捕获流程的因果机制；ENG-092 推演 proposal 恢复，改为预测；ENG-129 预测微任务次序，改为预测；ENG-043 检验权限模型边界，改为边界迁移。",
        "数量题的主线输入必须可追溯且事前可知，允许注明方法的推导；无法取得必要数字则采用预设的方向、边界或证据选择问题，不能自动填合成参数。合成数字只属于明确切换的反事实附加练习。39 条输入要求和备用问题见 quantitative-requirements-2027.tsv；核源前不自动改动作。",
        "规范化后的类别分布不追求机械均匀。52 个设计都以主动构造为主，细分对象仍保留在原始认知动作与 subdomain 中；不能把共同的设计动作误判为 52 个重复案例。\n",
        "## 事件和机制重复\n",
        f"人工记录 {len(summary['overlap_clusters'])} 个复用审查簇；事件身份风险与机制相邻、同公司不同节点分开列于 `phase2-overlap-review.yaml`。",
        "- ENG-080 / ENG-157：候选材料的 2015 Blaze/Bazel 缓存主题缺少独立决策点；保留前者，后者建议替换。没有擅自指定或编造替代事件。",
        "- ENG-011 / ENG-040：供电标题可能包含同一事件，前者须锁定另一独立节点，否则成为替换候选。现有文本不足以断言已重复。",
        "- PRO-080 / INV-034：可能复用同一 PMF 调查。产品题保留证据选择；投资题需独立的融资与商业质量材料，否则替换。",
        "- ENG-015 / ENG-143：第三方凭据事件可能相邻；必须分别核实暴露路径与时点，不能相互借用事实。",
        "构建缓存、quorum、重试/幂等、开源商业化、低频产品和邀请链接均有机制拥挤风险，逐簇列出分化要求。Figma、Dropbox、Netflix 等同公司题不因公司名相同就合并。\n",
        "## 周内密度与年度集中度\n",
        f"按 ISO 周检查全部 {len(summary['weekly_review'])} 个周片段，首尾不完整周照实保留。阈值为同一文本实体至少 3 次或同一主要认知动作至少 4 次；触发 {len(flags)} 个周片段。",
        table(["周", "需要检查的密度信号"], [[w["iso_week"], ", ".join(w["flags"])] for w in flags]) if flags else "未触发上述高密度阈值；不代表较低频的机制相似性已经消除。",
        "\n同实体仅用于定位集中度，不作为事件重复结论。所有周的日期、实体与认知动作计数保存在 JSON，跨周复用由人工簇补充。",
        f"较低阈值（同实体 2 次、同动作 3 次或同复用簇 2 次）触发的 {len(followups)} 个周片段已逐项复核，记录见 `phase2-weekly-review.yaml`。W50 的 Dropbox 工程成本与投资毛利存在实际材料复用风险，需在来源验证时区分；当前不挪日期。",
        table(["周", "具体复核与动作"], [[w["iso_week"], w["followup_review"]] for w in followups]),
        table(["文本实体提示（前十）", "历史候选次数"], [[row["label"], row["count"]] for row in summary["entity_hints"][:10]]),
        f"\n原始工程可靠性候选 {summary['engineering_reliability_concentration']['total']} 条中，有 {summary['engineering_reliability_concentration']['cloudflare']} 条标题含 Cloudflare，集中度较高，且部分标题笼统。后续需逐条核源并保持不同故障机制。若仍需替换，优先补非 Cloudflare 的独立失败、回退或恢复决策，不新增未验证题名。\n",
        "## 结果多样性与投资偏差\n",
        table(["候选文本的叙事框架", "全年次数", "创投历史次数"], [[FRAMES[key], value, summary["investing_historical_frames"].get(key, 0)] for key, value in summary["candidate_frames"].items()]),
        "\n上表根据候选文字作规划分类，是对文本的推断，不是已验证的成功 / 失败 / 混合历史结果统计。313 个历史 observed_outcome 全为 unverified，verified_historical_outcomes 为 0。",
        "事故、关闭、救助、估值重定价和争议题已进入规划：例如 Tesla 生存融资、WeWork 救助、Convoy 关闭、Blue Apron cohort、Quibi 止损、Klarna 重定价、FTX 尽调与 Better.com 延期。它们不能自动等同于投资人最终亏损或在事前应当拒投。",
        "机会叙事仍较多，存在从最终知名公司回看早期融资的选择偏差。Phase 3 须核实每个投资时点、价格/条款可得性、后果观察窗口和不确定性；缺价格或条款时只判断继续尽调、经营假设或有标记的情景，不要求精确仓位或实现收益率。",
        "好公司、好投资和好时机必须分别讨论；IPO、融资轮和后来成功不能共用一个 as-of。不得由事后赢家、关闭或股价单独证明当时决策优劣。\n",
        "## 范围与后续动作\n",
        f"{actions.get('accepted', 0)} 条 accepted 保留其单一微观题意，仍需后续核源和完整 Brief。{actions.get('revise', 0)} 条 revise 已逐条指出应收窄的功能、时间、指标或假说；常见问题是多年综述、无数据精算、提前归因和多个主任务。",
        f"{design_revise} 个设计题需要额外收窄或明确合成约束，涵盖基金储备、APM、远端环境、受监管服务、eval、审计、背压、硬件现金流和巨头竞争；名单见逐条记录。",
        "ENG-157 是唯一 replace 建议，尚未确定替代事件；日期和 ID 保持原状；本报告记录 Phase 2 建议，当前状态以索引及 Phase 3 报告为准。ENG-011、INV-034、ENG-117 等在无法获得独立材料时可能进入后续替换队列，此处不提前认定事实错误。",
        "初审校准 focus 和 review_status，映射见 `curriculum-revisions.md`；后续范围修订另以 revision_state 追踪，具体问题、证据要求、合成约束和数量题规则见 `phase2-revision-results.md` 及 `curriculum/planning-2027.yaml`。没有实际换题、改号、挪日期或升级训练状态。",
        "当前修订进度：" + "、".join(f"{key} {value}" for key, value in summary["revision_progress"].items()) + "。原始 revise/replace 标签保留作为审核历史，不代表仍只有备注未落实。",
        "Phase 2 完成后停止，待用户同意再进入 Phase 3 来源验证；不提前制作 ready Brief、完整协议或声称训练对话验收通过。\n",
    ])
    return "\n\n".join(section.strip() for section in sections if section.strip()) + "\n"


def render_revisions(revisions):
    lines = ["# Phase 2 canonical 索引变更映射\n",
             "本表记录初审相对 Phase 1 的 focus/review_status 映射；后续 revision_state 和候选 planning 范围详见 phase2-revision-results.md。日期、ID、kind、domain、subdomain、status、路径和原始候选素材保持原值。replace 是规划建议，未实施换题。\n",
             table(["日期", "ID", "原 focus", "校准后 focus", "审核动作"],
                   [[r[k] for k in ("date", "id", "old_focus", "new_focus", "review_status")] for r in revisions])]
    return "\n\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--apply", action="store_true", help="Apply reviewed focus/status metadata and write audit artifacts")
    args = parser.parse_args()
    try:
        index, audit, summary, revisions = build(args.root)
    except (OSError, KeyError, TypeError, ValueError, yaml.YAMLError) as exc:
        raise SystemExit(f"Audit failed: {exc}") from exc
    yaml_text = yaml.safe_dump(audit, allow_unicode=True, sort_keys=False, width=100)
    outputs = dict(zip(ARTIFACTS, (
        yaml_text, json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        render_report(summary), render_revisions(revisions),
    )))
    if args.apply:
        write_yaml(args.root / "curriculum/2027.yaml", index)
        for rel, content in outputs.items():
            (args.root / rel).write_text(content, encoding="utf-8")
    else:
        if read_yaml(args.root / "curriculum/2027.yaml") != index:
            raise SystemExit("Index focus/review_status differs from reviewed notes")
        for rel, expected in outputs.items():
            if not (args.root / rel).is_file() or (args.root / rel).read_text(encoding="utf-8") != expected:
                raise SystemExit(f"Audit artifact is missing or stale: {rel}")
    print(f"PASS: {summary['total']} individual reviews; {summary['review_status']}; Phase 2 planning snapshot, no external verification by this command.")


if __name__ == "__main__":
    main()
