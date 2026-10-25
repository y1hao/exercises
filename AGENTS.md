# 仓库维护约定

## 范围和协作

- 先读 `2027_exercises_codex_phase1-5_plan.md` 与 `2027_daily_exercise_consumer_prompt.md`；后者是权威消费契约，字段或路径冲突必须显式记录并同步修订。
- 用户要求逐阶段授权：每个 Phase 完成后汇报、等待同意，再进入下一阶段。当前实施阶段和进度见 `reports/progress.md`。
- 保留未提交工作；不得覆盖两份根目录原始课程，不用 `git clean -fd` / `git reset --hard`。不自动 commit/push、切默认分支或操作真实定时任务。
- 本项目只需要纯文本与简单 Python 脚本，不新增数据库、网站或训练记录写回后端。

## 数据与事实

- 唯一消费索引为 `curriculum/2027.yaml`；保留全部日期和稳定 ID。换题、改日期或改号必须记录映射与理由。
- 不将候选摘要、source_hint 或示例链接当作已验证事实。来源核实应记录真实 URL、发布者、日期（可知时）、原始/次级属性、支持内容和核查结果；没有逐条检查，不宣称已验证。
- 明确区分历史事实、当事人解释、维护者推断、未知与合成假设；不编造日志、指标、观点、融资价格或交易条款。事前信息不得越过历史决策时点。
- 历史结局、隐藏证据和参考解法不得进入首轮或可复制 Starter Prompt。合成微设计必须标明假设，评价允许多个自洽方案。
- 文件存在不代表 ready；只有内容、来源和 Case QA 全通过才同步升级索引和 Brief。资料不足写明 blocked/rejected 原因；不得换下一题掩盖失败。
- Protocol 草稿不得用于 ready 训练；正常 Consumer 输出及失败行为必须遵守现有 Consumer 契约。

## 每次改动的检查

执行并报告以下 lint / 结构 / 覆盖检查：

```sh
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

- 比对 `reports/phase1-input-snapshot.json` 的原始输入哈希，保护输入和用户已有修改。
- Phase 2 审核输入见 `reports/phase2-review-notes.tsv`、复用簇与周内复核 YAML；改动后显式执行 `scripts/audit_curriculum.py --apply` 重建报告。默认执行为只读复现检查。`review_status` 不是训练状态，replace 建议不代表已经换题。
- 本轮规划输入位于 `curriculum/revision-plans-2027.tsv`、`design-revisions-2027.yaml`、`quantitative-requirements-2027.tsv` 和 `planning-policy.yaml`；通过 `scripts/revise_curriculum.py --apply` 同步索引 revision_state、规划汇总与 Brief 的 planning，再重建 audit。核源与制作 Brief 应遵守 planned_exercise 的单一范围，candidate_material 只用于追溯。
- 历史主线的数字必须可追溯且事前可知。输入不足时优先采用逐题列明的定性或证据问题并记录动作映射，不自动补合成值；合成数字只属于明确切换的反事实附加题。微设计参数应显式标合成。
- Phase2替换条件保留为历史；Phase3已落实ENG-157→Rust 1.52.1、ENG-117→Ribbon Filter、INV-034→Chegg，ENG-011已独立核源。当前制作范围与原题映射见active_scope和phase3-revisions，不恢复旧待替换状态。
- 涉及事实内容、证据或状态晋级时，额外逐条核实相关来源；结构校验不能替代来源验证、剧透检查或对话试验。仅结构改动应在报告中说明没有新增核源结论。
- 更新 `reports/progress.md` 的准确状态数量、检查结果、阻塞和剩余工作；不以文件数量或模拟结果冒充完整验收。

- Phase 3 维护输入为 `reports/research-*.md`，数量主线的有效状态复核为 `curriculum/source-decisions-2027.yaml`。核源后显式运行 `scripts/verify_sources.py --apply`，同步 research/status 和 source-verification 报告；默认离线只读检查，不能自动核实网络事实或设 ready。
- Phase 2 的 planning/revision_state 是历史规划快照，不能用 input_verification:not_started 覆盖当前 research 结论。缺数量输入且备用动作尚未应用时保持 blocked；原核源建议状态可另存 source_assessment_status。
- 研究中的 availability 只表示历史可知性；unknown/post_decision 不得进入 sourced 的初始事实。工程规范/设计工件须标明版本与机制快照，不能编造成生产事故。融资建议、宣布、交割和实现回报必须区分。

- 用户最新要求：Phase3不能只以313条都有状态就结束，必须先处理补源/改题/换题，使365题全部通过制作前准入，再汇报并等待Phase4授权。本轮来源与范围输入见`reports/remediation-*.md`、52设计前置审查见`curriculum/design-admission-2027.yaml`。`scripts/phase3_admission.py --progress`只写诚实进度；`--apply`在全365 eligible前必须拒绝，不设置ready。
- 原Phase2 planning与初轮source-decisions保留为历史。正式改题后用active_scope和phase4_admission判断实际制作范围，保留日期/ID/candidate_material及逐条映射。不能让老生成器恢复已正式取消的缺数字要求或覆写新focus。

- 用户要求收敛工作：后续只处理未通过项或明确发现的事实错误，不再把补题扩大为新一轮全量复核或继续扩建检查框架。当前126个初轮失败项已处理，尚未获Phase4授权。
