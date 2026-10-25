# Phase 1 导入映射

实际输入是仓库根目录的 `curriculum_2027_complete.yaml`（`slots` 数组）。配套 Markdown 的 365 个日期/ID 与之逐项一致。原文件保留不改；其提到的两份历史上游分卷不在仓库，不作为依赖。

| 原始字段 / 值 | 消费索引 / 候选 Brief | 处理 |
|---|---|---|
| `slots` | `entries` | 按原日期排序，全年 365 条 |
| `id` / `date` | 同名字段 | 原值保留，不改号、不挪日期 |
| 历史 `track` | `kind: historical` / 对应 `domain` | engineering、product、investing 原领域保留 |
| `track: micro_design` | `kind: micro_design` | 领域另取原始 `domain` |
| 微设计 `domain: venture` | `domain: investing` | 12 条，统一 Consumer 枚举；原值保存在 `candidate_material` |
| `candidate_needs_verification` | `status: candidate` | 313 条；不表示已核实 |
| `candidate_needs_review` | `status: candidate` | 52 条；不表示已完成设计 QA |
| `subdomain` | `subdomain` | 下划线改连字符，含义不变 |
| 历史 `planned_cognitive_move` | `focus` | 下划线改连字符 |
| 微设计 `primary_cognitive_move` | `focus` | 下划线改连字符；Phase 2 再审核认知动作分类 |
| `historical_case` / `title` | Brief 的 `scenario_title` | 内部候选标题，未做剧透审核 |
| 全部原始记录字段 | Brief 的 `candidate_material` | 逐条完整保留，包括原状态、来源提示和示例 URL |
| 无原始对应 | `brief_path` / `protocol_path` | 按 kind/domain/ID 构建同仓库路径 |
| 无原始对应 | 顶层 `timezone` | 按契约固定 `Pacific/Auckland` |

没有生成事前事实、历史结局或证据池，没有声称任何来源已核实。365 个候选文件用于路径完整性和后续维护；不满足训练 Brief 的 ready 门槛。

无 ID 冲突，故无需 `id-map.md`。本阶段没有课程替换或日期迁移。原始 Git 状态和文件哈希见 `phase1-input-snapshot.json`，实际状态以该快照为准，不沿用计划中“原始课程尚未 commit”的过时描述。
