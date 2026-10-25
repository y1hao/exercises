# 实施进度

更新日期：2026-10-25（Pacific/Auckland）。

**Phase 3 整改完成，停在阶段交界，等待用户同意进入 Phase 4。** 本轮未commit/push。

初轮125道blocked与1道rejected均已处理：116道正式收窄/修订问题、9道真实换题、1道补核后保留。没有再要求完成题目所不需要的私有现金跑道、同cohort成本或未披露交易条款；保留27道可追溯实际输入的数量题。完整映射见[phase3-revisions.md](phase3-revisions.md)，逐题来源见remediation笔记。此前已完成的其他复核材料一并保留，本轮后半段收敛处理剩余失败项，没有继续扩展检查框架。

| 类型 | 数量 | 当前状态 |
|---|---:|---|
| 工程历史 | 157 | sourced |
| 产品历史 | 104 | sourced |
| 创投历史 | 52 | sourced |
| 微设计 | 52 | candidate；已有范围与合成约束基础 |
| 合计 | 365 | 制作前eligible；0 blocked、0 rejected、0 ready |

9项实际替换：ENG-054→Cloudflare 2017闰秒；ENG-117→RocksDB Ribbon Filter；ENG-157→Rust 1.52.1；PRO-001→Google Wave；PRO-013→Airbnb 2014推荐重建；PRO-059→Buffer早期验证；PRO-082→Max品牌扩展；PRO-093→Bluesky取消邀请；INV-034→Chegg增长诊断。

所有日期、ID、路径和candidate_material保留。四份根目录原始输入不修改。Phase2 planning及初轮source-decisions保留为历史；后续制作使用各Brief的active_scope及research，不恢复已取消的旧问题。

eligible仅表示已有素材与明确任务足以进入制作；sourced仅表示已读来源支持所选节点。发布政策、技术文档、公司自报、模型与当事人回顾均保留其性质，不当作独立因果证明。完整Brief、剧透检查、Case QA与对话试验尚未执行，属于后续阶段。

## 本轮验收

全部通过：

- 365日期、星期配额、ID、路径、索引/Brief状态结构及覆盖检查。
- Phase2审核/规划、Phase3核源与整改输出的只读复现检查。
- 62项测试，包括126个初轮失败项均已正式采用可追溯范围、真实替换与不完整整改拒绝应用。
- Python编译与Git空白检查。
- 四份原始输入SHA-256与初始快照一致；365条原始candidate_material及日期/ID/路径一致。

研究记录与范围已完整同步，全部365条制作前检查通过。离线检查验证结构与同步，不冒充网络核查或训练QA。未生成opening、完整evidence_pool或Starter Prompt，未启动Phase4/5。

---

下方为初轮核源时的历史记录；其“已完成”只表示当时逐项初审结束，已被本轮更严格的全题准入要求补充。

# Phase 3 初轮核源完成时的归档记录

更新日期：2026-10-25（Pacific/Auckland）。

**Phase 1–3 已完成，本轮停在 Phase 3；等待用户同意后才进入 Phase 4。** 用户要求的 Phase 2 修订已先提交为本地 commit `072cda3`，随后开展来源验证。Phase 3 成果按用户本轮要求保存为独立本地提交（提交号见 Git 历史），未 push。用户再次指定 Phase 3，未授权进入 Phase 4；当前保留本阶段结果，等待明确后续方向。未创建或修改定时任务。

## 当前真实状态

| 类型 / 领域 | candidate | sourced | ready | blocked | rejected |
|---|---:|---:|---:|---:|---:|
| 工程历史 | 0 | 115 | 0 | 41 | 1 |
| 产品历史 | 0 | 48 | 0 | 56 | 0 |
| 创投历史 | 0 | 24 | 0 | 28 | 0 |
| 工程微设计 | 22 | 0 | 0 | 0 | 0 |
| 产品微设计 | 18 | 0 | 0 | 0 | 0 |
| 创投微设计 | 12 | 0 | 0 | 0 | 0 |
| 合计 | **52** | **187** | **0** | **125** | **1** |

313 个历史条目均实际尝试并记录明确 sourced/blocked/rejected 理由；sourced 只表示已读到支持所选节点的可信直接材料，不表示完整 Brief 或对话 QA 通过。blocked 不表示资料不存在。52 个微设计尚未做 Phase 4 约束与评价 QA。

## Phase 3 交付与关键发现

- 7 份 `reports/research-*.md` 是逐条维护输入，包含事件、决策边界、事前事实、隐藏证据候选、实际结果/文档行为、归因、未知、来源元数据和失败尝试。已同步 313 个历史文件的 research/status/就绪说明与唯一索引；原始 candidate_material、日期、ID、路径、标题及 focus 保留。
- `reports/source-verification.md` / `.json` 给出全部有效状态及理由；`scripts/verify_sources.py` 可只读复现，`--apply` 明确同步。离线脚本检查覆盖、引用、可知性与状态，不冒充在线事实核查、剧透检查或完整 Case QA。
- `curriculum/source-decisions-2027.yaml` 对 39 条数量主线逐项复核：INV-001、INV-037 可作有边界的数量比较；37 条本轮未齐输入。即使机制来源可读，缺原题数字且未正式应用备用问题仍设 blocked；保留原核源建议状态以便追溯。Blue Apron 的累计 CPC 和贡献表 cohort 窗口不一致，不能拿公司平均值假装匹配 CAC。
- ENG-011 已确认独立的 2024-03-26 事故，与 ENG-040 的 2023 供电事件分开。ENG-054 的 Google 闰秒归属、多个旧版本或产品发布日期仍有缺口；逐条记录，不编造节点。
- INV-005 的 Yelp 2005 Series B 标签与同期 memo 不符；INV-010 核实到 2015 Figma A 轮/Preview，未证实拟选 2016 融资；PRO-025 等流行故事和官方/当事人记录存在时序或机制差异，均见具体笔记。
- ENG-157 原 Blaze 候选 rejected，另记录已核到直接材料的 Rust 1.52 构建回退备选，但尚未换题。ENG-117 与 INV-034 仍缺 Phase 2 指定的独立优化/付费 cohort，保留 blocked 并待替换审议。
- Phase 2 报告、planning 和 revision_state 明确为历史规划快照；当前来源状态见 status/research，不用旧的 not_started 覆盖本轮结论。未修改原计划或 Consumer 契约。

## Phase 3 验收

| 检查 | 结果 |
|---|---|
| 全年日期、配额、ID、路径和索引/Brief 状态 | PASS，365 日期保留，0 ready |
| 313 条研究覆盖、来源引用及可知性结构 | PASS，无重复、遗漏或 unattempted；sourced 初始事实仅 pre_decision |
| 39 条数量准入与未应用备用动作 | PASS，2 可有限比较、37 blocked，不自动补合成数据或改 focus |
| Phase 2 初审、规划和 Phase 3 报告复现 | PASS，三个脚本默认只读检查通过 |
| 单元 / 契约 / 规划 / 来源回归 | PASS，60 tests；包含未知引用、缺直接结果来源、事后信息、未尝试阻塞、缺数量输入、全量覆盖和同步保护 |
| Python 编译、Git diff 与新增文本空白 | PASS |
| 四份原始输入 SHA-256 | PASS，与 Phase 1 快照一致 |
| 完整 Brief、剧透与真实对话 QA | 未执行，属于后续 Phase 4/5，不宣称可训练 |

下一步须先由用户审阅本阶段结果，再决定如何处理 blocked/rejected 和是否进入 Phase 4。可补取原文/同期材料、正式采纳已预列的定性或证据备用题并同步映射，或审议替换；不能凭配额填空。Phase 4、5 均未启动。

---

以下为 Phase 2 修订完成时的历史快照。其中“当前”“尚未授权”“均 candidate”等时态仅描述当时，不代表上面的最新实施状态。

# Phase 2 修订完成时的归档记录

更新日期：2026-10-25（Pacific/Auckland）。

**Phase 1、Phase 2 初审及本轮范围修订已完成，当前停在 Phase 2。** 用户先要求提交成果，再撤回进入 Phase 3 的指示，改为先落实 Phase 2 审核结果；本轮已按新授权直接修订。Phase 3 尚未进行外部核源，Phase 4/5 也未启动。

## 当前真实状态

| 类型 / 领域 | candidate | sourced | ready | blocked | rejected |
|---|---:|---:|---:|---:|---:|
| 工程历史 | 157 | 0 | 0 | 0 | 0 |
| 产品历史 | 104 | 0 | 0 | 0 | 0 |
| 创投历史 | 52 | 0 | 0 | 0 | 0 |
| 工程微设计 | 22 | 0 | 0 | 0 | 0 |
| 产品微设计 | 18 | 0 | 0 | 0 | 0 |
| 创投微设计 | 12 | 0 | 0 | 0 | 0 |
| 合计 | **365** | **0** | **0** | **0** | **0** |

313 个历史条目尚未核源；52 个设计条目尚未通过约束 QA。没有 blocked 条目不等于没有问题，只表示还未进入逐条验证。365 个候选文件均不具备训练就绪声明。

## Phase 2 本轮范围修订

本轮不再只保留“需要修改”的备注，而是明确后续生产必须使用的任务范围。初审 `review_status` 保留为历史，另新增 `revision_state`：

| 进度 | 条数 | 已落实的内容 |
|---|---:|---|
| retained | 164 | 初审保留，不额外改写任务范围 |
| awaiting_source | 191 | 历史题已明确拟研究节点、一个主问题、一项输出、所需证据和排除范围；等待核源确认事实 |
| revised | 9 | 合成设计的任务、假设和相关变化已改写 |
| awaiting_replacement | 1 | ENG-157 的替换目标、独立性与来源准入条件已写明；真实替代事件尚未确定 |

- 原始输入和所有 `candidate_material` 保持不变；每个候选 Brief 新增 `planning`，后续核源及 Brief 制作应先遵守其 `planned_exercise`，不再直接扩写原始多年综述。
- 9 个设计修订已直接落成具体方案。DES-026 改为 workspace 中断恢复，不再同时设计启动、缓存和计费；DES-041 明确有限容量和可拒收边界，允许证明条件不可兼得；DES-042 仅用明确标注的合成参数讨论一笔订单现金时序。
- 39 个数量题均列出来源输入、计算口径与一个具体备用问题和认知动作。历史主线缺数字不补合成值；合成值只可在明确切换的反事实附加题中使用。所有备用动作目前均未应用，未擅自重分课程动作。
- 为全部 25 个复用簇列出每个成员当前的任务范围和分化条件。保留日期和 ID，不因换公司就声称机制不同。
- ENG-011 必须取得独立于 ENG-040 的拟选 2024 事件材料；INV-034 必须取得独立于 PRO-080 问卷的融资和付费 cohort；ENG-117 必须定位单次 SSD 优化。不能满足条件时进入替换队列。没有用新编事件补齐。
- 新增 `scripts/revise_curriculum.py`，可显式重建规划汇总、索引进度、365 个 Brief 的规划字段与修订报告；默认只读校验复现性，非 planning 内容和训练状态保留。
- 更新 README、AGENTS、初审报告与原用数建议，消除“缺数字可以直接合成补主线”的旧表述。用户原始计划和 Consumer 文件未改。

入口为 `reports/phase2-revision-results.md`；结构化汇总为 `curriculum/planning-2027.yaml`；维护输入为 revision-plans TSV、design-revisions YAML、quantitative-requirements TSV 和 planning-policy YAML。

### 本轮验收

| 检查 | 结果 |
|---|---|
| 全年日期、ID、配额、训练状态 | PASS，日期未挪动，365 candidate、0 sourced、0 ready |
| 初审修改项覆盖与规划同步 | PASS，191 历史范围、9 设计修订、1 替换槽位，全部与索引和候选文件一致 |
| 数量题用数与备用问题 | PASS，39 条完整，备用动作均未应用 |
| 初审和修订报告复现检查 | PASS，两个脚本默认只读检查通过 |
| 单元 / 契约 / 规划回归 | PASS，48 tests，包括修订进度、数据保护、未核历史节点、合成边界及报告幂等性 |
| Python 编译、Git diff 和新增文本空白 | PASS |
| 原始四份输入 SHA-256 | PASS，与 Phase 1 快照一致 |
| 来源验证、完整 Brief、对话验收 | 未执行，当前修订不代表训练就绪 |

本轮没有需要用户即时选择的额外问题；剩余不确定性都是明确记录的事实和来源条件，不能凭用户偏好或推测填补。用户尚未重新授权 Phase 3，因此停在此处。

Phase 1–2 初审已按用户要求提交为 `1a28046`（本地，未 push）。本轮修订尚未 commit/push；没有更改或创建定时任务。

## Phase 2 初审交付与发现（历史记录）

- 通读全部 365 条候选，各有具体 `scope_and_rationale`；审核结果 **164 accepted、200 revise、1 replace**。审核动作与训练状态独立，accepted 不表示事实或 Brief 验收通过。
- 主内容领域覆盖工程 8 类、产品 8 类、创投 7 类；微设计保持工程 22、产品 18、创投 12。完整分布见 `curriculum-audit.md` / `.json`。
- 根据题目实际认知要求将 canonical `focus` 校准为八类：因果 49、预测 52、诊断 31、决策 57、选证据 41、数量校准 39、边界迁移 44、主动构造 52。各条均为一个主要动作，次要动作暂为空。
- `curriculum-review.yaml` 记录全部条目的原动作、现动作、领域、处理意见、叙事框架和复用关联；维护输入为 `phase2-review-notes.tsv`。
- `phase2-overlap-review.yaml` 记录 25 个事件身份 / 材料复用 / 机制相邻审查簇；不把同公司直接视为重复事件。
- 核查全部 53 个 ISO 周片段，对较低密度阈值触发的 16 个周片段逐项复核；结果见 `phase2-weekly-review.yaml`。Dropbox 的工程成本与投资毛利题同周，须区分所用材料与输出。
- 工程可靠性 22 条中 11 条标题含 Cloudflare；核源时需保证不同事件与机制，未来替换优先补其他实体的独立失败或回退节点。
- **ENG-157 建议替换**：与 ENG-080 的 2015 Blaze/Bazel 构建缓存主题缺乏独立决策点；原槽位、素材和 candidate 状态保留，未编造替代案例。
- ENG-011 与 ENG-040 可能复用供电事件；INV-034 与 PRO-080 可能复用 PMF 调查。先收窄与核对，独立材料不足再决定替换。ENG-117 等标题需定位具体来源，尚未宣称事实错误。
- 9 个微设计需收窄或补合成边界：DES-016、020、026、028、035、039、041、042、051。没有提前扩写为完整 Brief。
- 成败多样性仅按候选叙事规划：创投历史为机会 24、压力 11、争议 / 混合权衡 17。所有 313 个历史真实结果仍标记 unverified，未把叙事分类当作已核实成败。

### Phase 2 验收

| 检查 | 结果 |
|---|---|
| 日期、ID、配额、路径和训练状态 | PASS，365 个日期完整，全部 candidate |
| 逐条审核 | PASS，365 条唯一记录，全部有具体意见 |
| 审核报告可重建 | PASS，`scripts/audit_curriculum.py` 默认只读核对通过 |
| 相对 Phase 1 的变更范围 | PASS，仅 canonical focus 和新增 review_status；完整映射见 `curriculum-revisions.md` |
| 原始输入及候选素材保护 | PASS，四份输入哈希未变，365 条原始候选记录完整保留 |
| 单元 / 契约 / 审核回归 | PASS，39 tests；涵盖安全迁移、建议替换不等于已换题、未核源标签、周内复核完整性和报告复现 |
| Python 编译、Git diff 和新增文本空白检查 | PASS |
| 新增事实核源 / 训练状态晋级 | 无；不适用于本次规划分类和元数据校准 |

本阶段新增审核脚本、审核回归测试及 7 份审核输入 / 报告（逐条 TSV、复用 YAML、周内 YAML、完整审核 YAML、汇总 JSON、总报告 Markdown、变更映射 Markdown），更新 canonical 索引、覆盖报告、校验器、README、AGENTS 和进度记录。脚本只重建规划数据，不访问网络、不生成案例、不自动改变训练状态。

## Phase 1 交付

- 原始根目录 YAML / Markdown、计划和 Consumer 文档全部保持原字节；输入清单、原始 Git 状态和 SHA-256 见 `phase1-input-snapshot.json`。
- `curriculum/2027.yaml` 含 365 个唯一日期，覆盖 2027-01-01 至 2027-12-31；保持原始 ID 和日历，配额与星期一致。
- 313 个历史、52 个微设计候选文件完整保留各自原始记录；不以摘要冒充经过核实的开场或证据。
- `scripts/import_curriculum.py` 可重现导入，遇到任何既有目标即拒绝覆盖；字段映射见 `import-mapping.md`。
- `scripts/validate_curriculum.py` 校验日期、星期、ID、字段、同仓库安全路径、Brief 身份/状态和 ready 内容结构；拒绝重复 YAML 键、路径穿越及指向仓库外的符号链接。
- `scripts/report_coverage.py` 生成机器可读的领域、子领域、认知动作和状态分布，以及同标题重复提示；`coverage.json` 明确仅为结构盘点，不是 Phase 2 事件重复或课程质量结论。
- README 给出环境安装、字段、状态晋级和验证方法；AGENTS 记录事实边界、输入保护、阶段授权与维护检查。
- 三个协议文件仅建立稳定路径并标记 `status: draft`；所有候选仍不可消费，ready 校验拒绝草稿协议。完整协议将在 Phase 5 实施。

## Phase 1 验收记录

| 检查 | 结果 |
|---|---|
| 标准索引校验 | PASS，365 日期完整，无重复日期 / ID，无星期错配 |
| 路径和 Brief 身份 / 状态 | PASS，365 个 Brief 与三份协议入口均存在 |
| 输入保护 | PASS，四份输入 SHA-256 未变 |
| 单元 / 契约回归 | PASS，31 tests，包含缺失 / 重复日期、错星期、重复 ID、缺文件、越界路径、身份错配、无效 ready Brief、来源引用、草稿协议、导入防覆盖与完整测试样本 |
| Python 编译检查 | PASS |
| Git diff / 新增文本空白检查 | PASS |
| 本次新增事实核源 | 不适用；没有新增已核实事实或晋级状态 |
| 真实新对话 / 公开 GitHub 端到端训练 | 未执行，非 Phase 1 验收内容 |

仅结构通过不能证明来源真实性、时间边界正确、开场无剧透或互动质量合格。测试中的 ready 样本明确为合成测试夹具，运行于临时目录，不计入以上状态统计。

## 变更范围和剩余工作

新增 `.gitignore`、`requirements.txt`、README、AGENTS；新增 `curriculum/`、`cases/`、`designs/`、`protocols/`、`scripts/`、`tests/`、`reports/`。项目环境位于被忽略的 `.venv/`；依赖 PyYAML 6.0.3 已安装。未修改原始输入，未 commit/push，未创建或修改定时任务。

Phase 2 初审意见已经过本轮范围修订，尚未确定 ENG-157 的真实替代事件；历史事件身份、时点、数据和结果仍需后续验证。没有本地技术阻塞。只有用户重新同意，才能进入 **Phase 3：313 个历史案例的来源验证**；届时以 planning 中的具体范围优先核查重叠与模糊身份，再逐条定位直接来源、时间边界、证据与结果，诚实记录 sourced/blocked/rejected 和原因。

只有用户同意后才进入 Phase 3；Phase 4 完整 Brief 和 Phase 5 协议与交接测试仍须各自获得阶段授权。仅本地文件尚不可由公开 GitHub URL 读取；实际公开读取验证须在后续明确授权发布后进行。
