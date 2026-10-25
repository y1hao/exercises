# 2027 世界模型直觉训练

全年课程用于约 20 分钟的中文预测、诊断、决策与微设计练习。课程索引决定日期，Brief 保存事实或合成约束，Protocol 约束教练，新对话据此自适应互动。

**Phase 4 首批5题已生成，等待用户审阅。** 按全年顺序制作2027-01-01至01-05的4道历史题和1道微设计，[开场预览](reports/phase4-first-5.md)可直接阅读。新增内容为review_draft；仍有313道历史题sourced、52道微设计candidate、0 ready，尚未进行完整协议/对话验收。Phase3整改已提交为`aac70fc`，365题的来源与范围基础保留；本轮只制作这5题。

## 本地运行

需要 Python 3.10+；唯一第三方依赖是 `requirements.txt` 中固定版本的 PyYAML。

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/validate_curriculum.py
.venv/bin/python scripts/report_coverage.py --output reports/coverage.json
.venv/bin/python scripts/audit_curriculum.py
.venv/bin/python scripts/revise_curriculum.py
.venv/bin/python scripts/verify_sources.py
.venv/bin/python scripts/phase3_admission.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m compileall -q scripts tests
git diff --check
```

所有脚本的默认输入均相对仓库目录定位，不依赖启动时的工作目录。校验失败退出码为 1；覆盖脚本拒绝汇总结构无效的索引。以上校验、测试和编译检查构成本阶段 lint / 检查流程。

## 文件职责

| 路径 | 职责 |
|---|---|
| `curriculum_2027_complete.yaml` / `.md` | 用户原始输入，保留不改 |
| `2027_exercises_codex_phase1-5_plan.md` | 范围、实施顺序与验收标准 |
| `2027_daily_exercise_consumer_prompt.md` | 消费端权威契约 |
| `curriculum/2027.yaml` | 唯一消费索引，365 个日期 |
| `cases/{engineering,product,investing}/*.yaml` | 历史候选素材及未来完整 Brief |
| `designs/*.yaml` | 微设计候选素材及未来完整 Brief |
| `protocols/*.md` | 公共及两种类型协议，当前为草稿 |
| `reports/phase1-input-snapshot.json` | 实施前文件列表、Git 状态和输入 SHA-256 |
| `reports/import-mapping.md` | 字段、状态和领域转换记录 |
| `reports/coverage.json` | 可重建的结构分布与同标题提示，不代替 Phase 2 审核 |
| `reports/curriculum-audit.md` / `.json` | Phase 2 全年审核、分布与周内密度 |
| `reports/phase2-review-notes.tsv` | 365 条具体审核意见的维护输入 |
| `reports/curriculum-review.yaml` | 每条的内容领域、主要认知动作、审核动作和复用关联 |
| `reports/phase2-overlap-review.yaml` / `phase2-weekly-review.yaml` | 25 个复用审查簇、16 个周片段的具体复核 |
| `reports/curriculum-revisions.md` | Phase 1 到 Phase 2 的全部 focus / 审核动作映射 |
| `curriculum/planning-2027.yaml` | 365 条修订进度；200 个明确任务、39 个用数与备用问题计划 |
| `curriculum/revision-plans-2027.tsv` | 191 条历史修改项的研究节点、主要问题、输出、证据与排除范围 |
| `curriculum/design-revisions-2027.yaml` | 9 个设计题的具体范围、合成假设和相关变化 |
| `curriculum/quantitative-requirements-2027.tsv` | 39 个数量题的输入要求和缺数字时的具体备用问题 |
| `curriculum/planning-policy.yaml` | 用数规则、修订进度含义、替换目标与条件 |
| `reports/phase2-revision-results.md` | 本轮修订总览、逐题问题和各复用簇的范围分工 |
| `reports/research-*.md` | 逐项实际核源的维护输入：事实、证据、结果、来源和失败尝试 |
| `curriculum/source-decisions-2027.yaml` | 初轮39条数量题的历史复核快照；正式整改后的范围另见active_scope |
| `reports/remediation-*.md` | 补源、范围修订和实际换题的逐题输入与来源 |
| `curriculum/active-scopes-2027.yaml` / `reports/phase3-revisions.md` | 当前已采用范围与原题、动作的映射，保留日期和ID |
| `reports/phase3-admission.md` / `.json` | 制作前检查结果；eligible不等于训练ready |
| `reports/source-verification.md` / `.json` | Phase 3 逐项有效状态、理由、身份纠错及阻塞 |
| `reports/progress.md` | 分阶段进度与验收结果 |

### 索引

顶层固定 `year: 2027`、`timezone: Pacific/Auckland`、`entries`。每条含：

| 字段 | 约束 |
|---|---|
| `date` | `YYYY-MM-DD`，全年唯一且连续；Auckland 当地日期 |
| `id` | 保留原始 `ENG/PRO/INV/DES-NNN` ID，全年唯一 |
| `kind` | `historical` 或 `micro_design` |
| `domain` | `engineering`、`product`、`investing` |
| `subdomain` / `focus` | 子领域；Phase 2 将主要认知动作统一为下述八类，原始动作另存审核记录 |
| `status` | `candidate`、`sourced`、`ready`、`blocked`、`rejected` |
| `review_status` | `accepted`、`revise`、`replace`，仅课程审核动作，不表示来源或训练通过 |
| `revision_state` | `retained`、`awaiting_source`、`revised`、`awaiting_replacement`，记录 Phase 2 范围修订的历史快照，当前核源状态看 status/research |
| `brief_path` | 同仓库相对路径，必须存在且身份、状态一致 |
| `protocol_path` | `protocols/historical.md` 或 `protocols/micro-design.md` |

周一三五工程历史、周二四产品历史、周六创投历史、周日微设计。索引不内联历史结局。候选 Brief 用 `candidate_material` 原样保存原始记录，用 `origin` 指回原始输入；Phase 3 的 `research` 另存核源素材，不是 `opening` 或可直接消费的完整 Brief。

主要认知动作八类为 `causal-modeling`、`prediction-counterfactual`、`hypothesis-diagnosis`、`constrained-decision`、`evidence-selection`、`quantitative-calibration`、`boundary-transfer`、`constructive-design`。每条一个主要动作，最多两个次要动作（本轮未分配）。设计题统一主动构造，具体设计对象仍见 subdomain 与原始动作。

`scripts/audit_curriculum.py` 默认只读核对审核输入、索引元数据与生成报告是否一致。维护逐条意见、复用簇或周内复核后，用 `--apply` 明确更新报告及索引的 focus/review_status；不会修改日期、身份、候选素材或训练状态。accepted 表示保留选题；replace 表示建议替换，尚未执行换题。不得将这两个词误用为 ready 或 rejected。

### 本轮范围修订怎样生效

本轮整改后，Phase 4 应以各 Brief 的 `active_scope` 为制作范围；`planning.planned_exercise` 保留为Phase 2历史快照；`candidate_material` 保存原文用于追溯，不再把其中多年综述直接扩成训练。该规划字段没有历史开场、证据池或真实结果，不能被 Consumer 当作 `opening`。

- 164 条 `retained`：初审保留，仍须核源或设计 QA。
- 191 条 `awaiting_source`：已明确一个拟研究节点、主要问题、输出、所需证据与排除范围；事件身份、版本和日期尚待核实。
- 9 条 `revised`：合成设计的范围和假设已改写，尚未完成 Brief 或对话 QA。
- 1 条 `awaiting_replacement`：Phase 2 的 ENG-157 替换目标与准入条件已确定；初轮Phase 3的备选曾仅为提案；本轮已正式替换为Rust 1.52.1增量编译ICE回退，旧规划标签不变。

以上计数和标签是 Phase 2 规划快照，不能代替当前核源状态。初审 revise/replace 标签保留为历史，不表示仍只有未处理备注。规划中的 anchor_request 仅是拟核查对象，不是已经确认的历史 as-of。修订脚本保留 Brief 的非 planning 字段；核源脚本另外同步 research/status/readiness_note，原始候选材料保留不改。

39 条数量题的真实主线仅允许可追溯且事前可知的输入，可透明推导，缺数字不自动补合成值。每题记录具体备用问题和动作；核源确认输入不足后才能手动采用并记录映射。合成参数仅可用于明确切换的反事实附加练习；微设计本来就是合成题，参数须明确声明。

修改规划输入后，显式重建并检查：

```sh
.venv/bin/python scripts/audit_curriculum.py --apply
.venv/bin/python scripts/revise_curriculum.py --apply
.venv/bin/python scripts/audit_curriculum.py --apply
.venv/bin/python scripts/revise_curriculum.py
```

第二次 audit 用于同步新修订进度；两个脚本默认均为只读一致性检查。修订脚本只更新规划元数据与报告，不改训练状态，不自动采用备用动作或实际换题。来源验证开始后，后续进度应如实追加，不能把本轮研究目标误称为事实。

### 核源记录怎样生效

`scripts/verify_sources.py` 默认只读核对 313 个历史条目的完整覆盖、来源与主张引用、事前信息边界及索引/Brief 同步。维护 `reports/research-*.md` 并逐条实际核源后，用 `--apply` 显式更新历史 Brief 的 `research`、`status`、就绪说明与索引状态，同时重建来源报告；它不访问网络、不生成开场、不设置ready；正式整改通过active-scopes清单采用核源记录与focus，避免旧生成器恢复已取消范围。

每项记录包含所选事件、决策边界、可知事实、按需证据、观察到的结果、解释、未知和真实尝试。`pre_decision/post_decision/unknown` 记录历史可知性；它与教练何时释放证据是两个字段，不能直接替代 Phase 4 的证据释放规则。后见回顾需保留局限；投资建议不能写成实际交割或已实现回报，设计工件不能写成未验证的生产事故。

39 道数量题另经 `source-decisions-2027.yaml` 复核。主线输入未齐、备用问题未正式应用时保持 blocked，即使已经读到可信机制材料；原核源建议状态另存 `source_assessment_status`。该文件不自动迁移认知动作。本轮已用remediation记录正式修订并通过 `scripts/phase3_admission.py --apply` 同步标题、范围、动作及映射；当前保留27道有来源数值的数量题，其余改用明确的备用或修订问题。

### 从候选到可运行

1. `candidate`：仅有课程想法，先完成 Phase 2 的课程质量审核。
2. `sourced`：历史事件及结果已经逐条核源，记录真实 URL、发布者、日期（可知时）、原始/次级属性、支持的事实与检查记录。来源提示或能打开网页本身不代表已验证。
3. `ready`：Brief、事实时间边界、证据、交互材料与 Case QA 全部通过，且协议可用。微设计不要求历史核源，但须通过约束和评价 QA。索引和 Brief 同步升级。
4. `blocked` / `rejected`：写明原因，不删日期、不偷换题、不以现场生成的材料补足。

历史 ready 的结构检查包括 `historical_as_of`、`objective`、`opening`、`evidence_pool`、`resolution`、`boundaries`、`sources` 及来源引用；微设计包括 `objective`、`opening`、`initial_constraints`、1–2 项 `perturbations`、`evaluation_criteria`、`boundaries`。具体内容格式以实施计划为准。

结构通过并不证明事实正确、无剧透或训练质量达标；这些仍须逐条来源审查、人工检查和对话试验。校验器不访问网络，也不自动升级任何状态。只有 ready 条目可被 Consumer 消费，其余必须明确失败。

### 安全重现导入

`scripts/import_curriculum.py` 只用于首次导入；任一目标已存在时会在写入前整体拒绝，防止覆盖后续人工审核的内容。需要比对时导入至新的临时目录：

```sh
.venv/bin/python scripts/import_curriculum.py --output-root /private/tmp/exercises-import-review
```

原始文件内提到的两份上游分卷并不在当前仓库；当前完整 YAML 为本次实际输入，不依赖不存在的文件。没有重新生成或补造课程。

## 阶段边界与发布

每阶段完成后向用户汇报并等待同意，才能进入下一阶段。当前仍停在Phase 3，尚未制作完整Brief。用户已授权先 commit、再进入 Phase 3；Phase 2 修订已本地提交为 `072cda3`，未 push。Phase3整改已提交`aac70fc`。当前仅获授权制作Phase4首批5题；后续批次等待用户审阅，Phase5训练试验尚未授权。Phase 2 结果多样性是候选叙事审核，不是已验证历史结果统计。

完整 Brief 将包含隐藏证据与结局；Consumer 只把事前 `opening` 放进 Starter Prompt。新训练对话必须能读取完整公开文件；读取失败应中止，不得编造事实。未来只有 commit/push 后，新增文件才能从公开 GitHub 读取。Phase 3 成果按用户要求保存为独立本地提交（提交号见 Git 历史）；未推送，未创建定时任务。
