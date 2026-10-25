# Phase 3 来源核查：ENG-080—ENG-157

核查日期：2026-10-25。78条均已实际尝试：65 sourced、12 blocked、1 rejected；0 ready。仅研究记录，不是可消费 Brief。sourced 要求来源支持可辨识事件或artifact及其结果/行为，未完成训练QA。滚动文档不得倒推首发时语义；各条 phase2_conditions 约束后续扩写。

## ENG-080

```yaml
id: ENG-080
status: sourced
reason: 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。
event: 2015 Bazel Beta 公告
cutoff: 2015-09-09 Beta 发布前的构建系统选择
initial_facts:
- id: I1
  text: Google 使用大型共享代码库并从源码构建
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 自动测试与多语言平台是设计背景
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Beta 提供多语言构建测试及自定义规则 API
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 分布式缓存仍列于未来路线图
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: Bazel Beta 已公开；不可把路线图中的分布式缓存当成已交付。
  source_ids:
  - S1
interpretation: 以上观察与厂商/作者归因分开使用；可迁移机制属于后续维护者解释。
unknowns:
- 精确决策过程和未公开数据未知。
sources:
- id: S1
  url: https://opensource.googleblog.com/2015/09/building-build-system-bazel-reaches-beta.html
  publisher: Google
  published_at: '2015-09-09'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 核查 Beta 公告正文；猜测的 Hello World URL 读取失败。
phase2_conditions:
- 保留 ENG-080；区别本地增量与尚未交付的分布式缓存。
```

## ENG-081

```yaml
id: ENG-081
status: sourced
reason: 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。
event: Lambda Extensions 2020 预览生命周期
cutoff: 2020-10-08 API 预览使用时
initial_facts:
- id: I1
  text: 函数运行在可复用的执行环境
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 扩展与函数共享执行环境资源
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: freeze 要等待 runtime 与所有扩展完成
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: SHUTDOWN 是独立生命周期事件
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 调用结束并不等于执行环境销毁；环境可冻结并复用。
  source_ids:
  - S1
interpretation: 以上观察与厂商/作者归因分开使用；可迁移机制属于后续维护者解释。
unknowns:
- 精确决策过程和未公开数据未知。
sources:
- id: S1
  url: https://aws.amazon.com/blogs/compute/building-extensions-for-aws-lambda-in-preview/
  publisher: AWS
  published_at: '2020-10-08'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 搜索并阅读全文生命周期部分。
phase2_conditions:
- 仅使用生命周期规则；文章现有容器镜像补充不能自动倒推到预览日。
```

## ENG-082

```yaml
id: ENG-082
status: sourced
reason: 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。
event: 2025-06-12 Workers KV 依赖事故
cutoff: 2025-06-12 故障响应早期；尚未披露根因
initial_facts:
- id: I1
  text: KV 被多个产品用作配置和认证依赖
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: Access 和 Gateway 等服务出现故障
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 复盘将起因归于 KV 底层存储依赖失败
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 恢复期间缓存回填与限流使错误继续存在
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 底层存储恢复后服务恢复；部分团队尝试削弱 KV 依赖。
  source_ids:
  - S1
interpretation: 以上观察与厂商/作者归因分开使用；可迁移机制属于后续维护者解释。
unknowns:
- 精确决策过程和未公开数据未知。
sources:
- id: S1
  url: https://blog.cloudflare.com/cloudflare-service-outage-june-12-2025/
  publisher: Cloudflare
  published_at: '2025-06-12'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开独立复盘，核查影响、依赖与恢复时间线。
phase2_conditions:
- 与其他 Cloudflare 事故分离；初始披露不得先给根因。
```

## ENG-083

```yaml
id: ENG-083
status: sourced
reason: 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。
event: Notion 2021 PostgreSQL 分片迁移
cutoff: 2021 年迁移键选择前；具体决策日未知
initial_facts:
- id: I1
  text: 每个 block 归属一个 workspace
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 常见查询主要在同一 workspace 内
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 团队选择 workspace ID 作为分区键
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 迁移后为 480 逻辑 shard、32 物理数据库
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 一次短维护窗口完成切换；作者报告用户感知性能改善。
  source_ids:
  - S1
interpretation: 以上观察与厂商/作者归因分开使用；可迁移机制属于后续维护者解释。
unknowns:
- 精确决策过程和未公开数据未知。
sources:
- id: S1
  url: https://www.notion.com/blog/sharding-postgres-at-notion
  publisher: Notion
  published_at: '2021-10-06'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 阅读全文数据分布、分区键与迁移部分。
phase2_conditions:
- 只讨论数据放置键；不能以 UUID 均匀推断租户负载均匀。
```

## ENG-084

```yaml
id: ENG-084
status: sourced
reason: 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。
event: Netflix 2012 Open Connect 发布
cutoff: 2012-06-04 网络扩展决策；首批试点已存在
initial_facts:
- id: I1
  text: 此前视频依赖商业 CDN 分发
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 视频规模和增长促使团队评估专用网络
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Open Connect 可在 ISP 或互联网交换点交付
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 公告时约 5% 数据已通过该网络
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 专用 CDN 已投入服务，计划逐步承担多数分发。
  source_ids:
  - S1
interpretation: 以上观察与厂商/作者归因分开使用；可迁移机制属于后续维护者解释。
unknowns:
- 精确决策过程和未公开数据未知。
sources:
- id: S1
  url: https://about.netflix.com/en/news/announcing-the-netflix-open-connect-network
  publisher: Netflix
  published_at: '2012-06-04'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 检索并打开当日发布公告。
phase2_conditions:
- 没有同地区命中率和完整成本表；数量主线改用 planning 的 constrained-decision 备用问题。
```

## ENG-085

```yaml
id: ENG-085
status: sourced
reason: 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。
event: CockroachDB v20.1 串行化冲突与重试
cutoff: v20.1 事务重试判断；具体执行时间非历史事故
initial_facts:
- id: I1
  text: v20.1 支持嵌套事务
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 并发读写同一数据可能产生串行化冲突
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 不能内部消解的冲突返回 SQLSTATE 40001
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 普通嵌套 savepoint 不等同于特殊事务重启协议
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 需要客户端重试的冲突存在；不能把嵌套回滚当作通用修复。
  source_ids:
  - S1
interpretation: 以上观察与厂商/作者归因分开使用；可迁移机制属于后续维护者解释。
unknowns:
- 精确决策过程和未公开数据未知。
sources:
- id: S1
  url: https://www.cockroachlabs.com/blog/nested-transactions-in-cockroachdb-20-1/
  publisher: Cockroach Labs
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开 v20.1 专文，核查冲突与限制说明。
phase2_conditions:
- Phase 4 必须明确读写集合为协议推演，不能假造真实事务日志。
```

## ENG-086

```yaml
id: ENG-086
status: blocked
reason: 只核到论文题名、作者与 2016 发表信息，未读到支持变更治理的正文。
event: Google Piper 2016 论文
cutoff: 2016 论文；具体协作决策时点未核定
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 以上观察与厂商/作者归因分开使用；可迁移机制属于后续维护者解释。
unknowns:
- 精确决策过程和未公开数据未知。
- 只核到论文题名、作者与 2016 发表信息，未读到支持变更治理的正文。
sources:
- id: S1
  url: https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/
  publisher: Google Research
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 官方论文页可读；ACM 下载链接与 archive/45424.pdf 均无法读取正文。
phase2_conditions:
- 仍需原论文正文中的协作路径和权限材料；元数据不足以判 sourced。
```

## ENG-087

```yaml
id: ENG-087
status: sourced
reason: 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。
event: React Server Components RFC 0188
cutoff: RFC 修订文本的方案评估；不能声称全部语义来自 2020 首稿
initial_facts:
- id: I1
  text: 服务器组件仅在服务器执行
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 客户端组件承载交互状态
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 服务器可读取后台数据并把 props 传给客户端
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: RFC 明确跨界 props 要可序列化
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: RFC 记录服务端与客户端可组合及其能力约束，2020 公告明确仍在研发。
  source_ids:
  - S1
interpretation: 以上观察与厂商/作者归因分开使用；可迁移机制属于后续维护者解释。
unknowns:
- 精确决策过程和未公开数据未知。
sources:
- id: S1
  url: https://github.com/reactjs/rfcs/blob/main/text/0188-server-components.md
  publisher: React
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
- id: S2
  url: https://react.dev/blog/2020/12/21/data-fetching-with-react-server-components
  publisher: React
  published_at: '2020-12-21'
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 打开 2020 公告和 RFC；注意 RFC 列明 use client 等后续变更。
phase2_conditions:
- 范围保持单次跨边界传递；Phase 4 固定 RFC commit，不能混用 2020 命名与新指令。
```

## ENG-088

```yaml
id: ENG-088
status: sourced
reason: 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。
event: Jens Axboe io_uring 接口设计论文
cutoff: 2019 接口设计比较；论文当前修订日期未显示
initial_facts:
- id: I1
  text: 旧 aio 提交和完成处理存在复制与调用开销
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 小 I/O 对每次请求开销敏感
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: io_uring 采用共享 SQ 和 CQ
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 作者用内存序协调生产者与消费者
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 设计避免在提交与完成路径复制请求结构；不保证任意工作负载收益。
  source_ids:
  - S1
interpretation: 以上观察与厂商/作者归因分开使用；可迁移机制属于后续维护者解释。
unknowns:
- 精确决策过程和未公开数据未知。
sources:
- id: S1
  url: https://kernel.dk/io_uring.pdf
  publisher: Jens Axboe
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 读取作者 PDF 的设计目标与双 ring 章节。
phase2_conditions:
- 尚无本题同口径安全评估；Phase 4 不把性能收益当安全保证，不引用后续版本数据。
```

## ENG-089

```yaml
id: ENG-089
status: sourced
reason: 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。
event: ISCA 2014 RowHammer 实验
cutoff: 2014 论文实验观察前；不是后续提权事件
initial_facts:
- id: I1
  text: 内存隔离要求访问一个地址不改变别处数据
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: DRAM 密度上升会增大相邻单元耦合风险
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 作者在真实 Intel 和 AMD 系统演示扰动
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 129 个模块中 110 个出现错误
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 重复激活一行可以损坏邻近行数据，突破纯软件地址隔离假设。
  source_ids:
  - S1
interpretation: 以上观察与厂商/作者归因分开使用；可迁移机制属于后续维护者解释。
unknowns:
- 精确决策过程和未公开数据未知。
sources:
- id: S1
  url: https://users.ece.cmu.edu/~omutlu/pub/dram-row-hammer_isca14.pdf
  publisher: CMU / Intel researchers
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开原论文并读摘要与实验样本说明。
phase2_conditions:
- 不得将 2015 提权利用当成 2014 已知结果。
```

## ENG-090

```yaml
id: ENG-090
status: sourced
reason: 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。
event: GitLab 2017-01-31 数据库删除及恢复
cutoff: 2017-01-31 误删后恢复路径选择
initial_facts:
- id: I1
  text: 数据库采用一主一从
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 有一份当日为测试手动创建的 staging LVM 快照
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 日常 pg_dump 备份实际不可用
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: staging 磁盘性能限制恢复速度
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 团队从 staging 快照恢复数据库；部分近期数据无法恢复。
  source_ids:
  - S1
interpretation: 以上观察与厂商/作者归因分开使用；可迁移机制属于后续维护者解释。
unknowns:
- 精确决策过程和未公开数据未知。
sources:
- id: S1
  url: https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/
  publisher: GitLab
  published_at: '2017-02-10'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开正式复盘，核查架构、快照、恢复与数据损失。
phase2_conditions:
- 事前仅提供已观察到的恢复检查结果；不能提前泄露最终恢复路径。
```

## ENG-091

```yaml
id: ENG-091
status: sourced
reason: 一手材料直接支持 artifact 或事件行为；不是 ready。
event: Vitess v5.0 Primary Vindex 文档样例
cutoff: v5.0 文档快照，2020-02-04；非 2010 首发行为
initial_facts:
- id: I1
  text: sharded 表必须指定 Primary Vindex
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 同一 keyspace ID 的行位于同一 shard
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Primary Vindex 同时影响分片键和映射方案
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 无适用 Secondary Vindex 时查询可能发往所有 shard
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 文档明确给出插入路由与查询扇出行为。
  source_ids:
  - S1
interpretation: 机制推演须与来源中的观察和当事人归因分别标记。
unknowns:
- 未公开的实际决策过程和完整工作量未知。
sources:
- id: S1
  url: https://vitess.io/files/version-pdfs/Vitess-Docs-5.0-02-04-2020.pdf
  publisher: Vitess
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 检索早期 Vitess 发布文章，打开 v5.0 历史 PDF 108 页附近。
phase2_conditions:
- 缺实际租户工作负载；可做已发布 artifact 的路由推演，不能编造迁移史。
```

## ENG-092

```yaml
id: ENG-092
status: sourced
reason: 一手材料直接支持 artifact 或事件行为；不是 ready。
event: 2011 Zab 论文恢复阶段
cutoff: 2011 协议恢复，旧 leader 失效后
initial_facts:
- id: I1
  text: Zab 用 primary-backup 复制状态变化
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 有 quorum 存活是推进前提
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Discovery 按 epoch 与 zxid 选择历史
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: Synchronization 建立新历史后按序提交投递
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 未提交 proposal 是否保留取决于被选中的历史，不能把全部未提交内容一律视为删除。
  source_ids:
  - S1
interpretation: 机制推演须与来源中的观察和当事人归因分别标记。
unknowns:
- 未公开的实际决策过程和完整工作量未知。
sources:
- id: S1
  url: https://www.cs.cornell.edu/courses/cs6452/2012sp/papers/zab-ieee.pdf
  publisher: Yahoo! Research authors
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 微软猜测入口失败；打开论文原文镜像并核对 Phase 1/2。
phase2_conditions:
- 必须具体列出已接受与已提交状态，保持与 Raft 题的区分。
```

## ENG-093

```yaml
id: ENG-093
status: sourced
reason: 一手材料直接支持 artifact 或事件行为；不是 ready。
event: GitHub 团队 2021 迁移 Codespaces
cutoff: 2021 团队开发环境迁移前，具体决策日未知
initial_facts:
- id: I1
  text: 此前大量开发基于 macOS 本地环境
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 本地环境偶发破坏需要重新构建
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 团队解耦 macOS 依赖并在 Linux 承载开发环境
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 预构建用于缩短新环境准备时间
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 团队报告多数 GitHub.com 开发迁到 Codespaces。
  source_ids:
  - S1
interpretation: 机制推演须与来源中的观察和当事人归因分别标记。
unknowns:
- 未公开的实际决策过程和完整工作量未知。
sources:
- id: S1
  url: https://github.blog/engineering/infrastructure/githubs-engineering-team-moved-codespaces/
  publisher: GitHub
  published_at: '2021-08-11'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开迁移工程文章；页面标记 2022-12-19 更新。
phase2_conditions:
- 迁移结果为团队报告；不可声称没有网络依赖或推断所有仓库适用。
```

## ENG-094

```yaml
id: ENG-094
status: sourced
reason: 一手材料直接支持 artifact 或事件行为；不是 ready。
event: gRPC 2015 设计原则
cutoff: 2015-09-08 API 选型
initial_facts:
- id: I1
  text: 客户端与服务器的算力及网络能力可能不均衡
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 流式接口用于时序相关消息
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 流量控制用于限制缓冲和过快发送者
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 取消与 deadline 可沿调用链传播
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 2015 原则文档明确支持流、取消及标准状态码；不是业务恰好一次保证。
  source_ids:
  - S1
interpretation: 机制推演须与来源中的观察和当事人归因分别标记。
unknowns:
- 未公开的实际决策过程和完整工作量未知。
sources:
- id: S1
  url: https://grpc.io/blog/principles/
  publisher: Google / gRPC
  published_at: '2015-09-08'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 检索并打开当年设计原则与发布公告。
phase2_conditions:
- 真实 API artifact 可作边界推演，业务负载只能标为教学示例。
```

## ENG-095

```yaml
id: ENG-095
status: sourced
reason: 一手材料直接支持 artifact 或事件行为；不是 ready。
event: JDK 9 G1 回收器规范
cutoff: JDK 9 的暂停目标与区域选择
initial_facts:
- id: I1
  text: G1 将堆划分为区域
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 回收目标受暂停时间预算约束
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: G1 按区域收益与预算安排回收
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 暂停目标不构成每次暂停的硬保证
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: JDK9 指南记录以可预测暂停为目标的区域回收机制。
  source_ids:
  - S1
interpretation: 机制推演须与来源中的观察和当事人归因分别标记。
unknowns:
- 未公开的实际决策过程和完整工作量未知。
sources:
- id: S1
  url: https://docs.oracle.com/javase/9/gctuning/garbage-first-garbage-collector.htm
  publisher: Oracle
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- JEP248 返回 403；改读 Oracle JDK9 专版指南。
phase2_conditions:
- 仅依据 JDK9 行为，不以当前 JDK 默认策略倒推 2017 所有机器。
```

## ENG-096

```yaml
id: ENG-096
status: blocked
reason: 页面确认当事人演讲存在，但本轮未取得可核查明星账号混合扇出的正文。
event: Twitter 2013 Timelines at Scale 演讲
cutoff: 2012—2014 候选，待取得讲稿正文
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制推演须与来源中的观察和当事人归因分别标记。
unknowns:
- 未公开的实际决策过程和完整工作量未知。
- 页面确认当事人演讲存在，但本轮未取得可核查明星账号混合扇出的正文。
sources:
- id: S1
  url: https://www.infoq.com/presentations/Twitter-Timeline-Scalability/
  publisher: InfoQ / Raffi Krikorian
  published_at: '2013-04-03'
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 搜索演讲与幻灯片；打开 InfoQ 仅有视频播放器、概要和讲者信息；搜索到转述未当作验证。
phase2_conditions:
- 需取得当事人幻灯片/可核对讲稿，确认 fanout-on-read 具体历史边界。
```

## ENG-097

```yaml
id: ENG-097
status: sourced
reason: 一手材料直接支持 artifact 或事件行为；不是 ready。
event: Google 2020-12-14 身份服务事故
cutoff: 2020-12-14 错误出现后的诊断起点
initial_facts:
- id: I1
  text: 多个需要 Google 身份的服务出现错误
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 已有网络数据平面配置仍能工作
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 旧配额系统把用量错误报告为零
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 配额下调阻止身份数据库写入并导致过期读取被拒绝
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 禁用配额执行后错误下降，多数服务恢复；少量服务恢复滞后。
  source_ids:
  - S1
interpretation: 机制推演须与来源中的观察和当事人归因分别标记。
unknowns:
- 未公开的实际决策过程和完整工作量未知。
sources:
- id: S1
  url: https://status.cloud.google.com/incident/zall/20013
  publisher: Google
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开官方状态事件，核对 RCA 和控制/数据平面影响。
phase2_conditions:
- 根因与恢复动作只作隐藏证据，按实际可见状态分轮披露。
```

## ENG-098

```yaml
id: ENG-098
status: sourced
reason: 一手材料直接支持 artifact 或事件行为；不是 ready。
event: runc CVE-2019-5736 维护者通告
cutoff: 2019-02-11 通告发布时的升级决定
initial_facts:
- id: I1
  text: 攻击者控制的容器镜像是风险输入之一
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 在已有容器内执行命令也可能触发相关路径
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 通告要求容器内 root 等条件
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 漏洞可覆写宿主 runc 二进制并取得宿主执行能力
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 维护者公布修复及受影响条件；不能把任意非特权容器都描述为可直接利用。
  source_ids:
  - S1
interpretation: 机制推演须与来源中的观察和当事人归因分别标记。
unknowns:
- 未公开的实际决策过程和完整工作量未知。
sources:
- id: S1
  url: https://www.openwall.com/lists/oss-security/2019/02/11/2
  publisher: runc maintainer Aleksa Sarai
  published_at: '2019-02-11'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 初次误入较新 advisory 后按 CVE 找到维护者原始公开邮件。
phase2_conditions:
- 只保留 2019 CVE 链条；不要混入其他 runc FD 漏洞。
```

## ENG-099

```yaml
id: ENG-099
status: blocked
reason: 当前 8.0 指南可证冲突集合语义，不能据此确认 2013 版本。
event: FoundationDB 2013 事务层候选
cutoff: 2013 版本未找到可读证据
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制推演须与来源中的观察和当事人归因分别标记。
unknowns:
- 未公开的实际决策过程和完整工作量未知。
- 当前 8.0 指南可证冲突集合语义，不能据此确认 2013 版本。
sources:
- id: S1
  url: https://apple.github.io/foundationdb/developer-guide.html
  publisher: FoundationDB
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 搜索 2013 事务资料并打开官方指南；看到当前 8.0 标记和 conflict ranges 部分。
phase2_conditions:
- 需要旧版文档或当年论文；未获授权前不擅改题名到 8.0。
```

## ENG-100

```yaml
id: ENG-100
status: sourced
reason: 一手材料直接支持 artifact 或事件行为；不是 ready。
event: TypeScript 3.4 增量构建
cutoff: 2019-03-29 版本特性使用
initial_facts:
- id: I1
  text: watch 模式依据旧依赖图识别受影响文件
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 跨运行需要把构建信息保存在文件
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 3.4 incremental 引入 tsbuildinfo
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: API 表面变化与不变的增量编译成本不同
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 3.4 可保存构建图并复用；不同 TS 版本不保证互读缓存格式。
  source_ids:
  - S1
interpretation: 机制推演须与来源中的观察和当事人归因分别标记。
unknowns:
- 未公开的实际决策过程和完整工作量未知。
sources:
- id: S1
  url: https://devblogs.microsoft.com/typescript/announcing-typescript-3-4/
  publisher: Microsoft
  published_at: '2019-03-29'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开 3.4 公告和 3.0 项目引用 release notes。
phase2_conditions:
- 只讨论依赖失效范围；Phase4 需固定版本及明确声明签名示例为演示代码。
```

## ENG-101

```yaml
id: ENG-101
status: sourced
reason: 一手直接材料可核查事件或发布行为，尚未Case QA。
event: Uber Schemaless 2016 架构文章
cutoff: 2016 文档中的实体与访问路径选择
initial_facts:
- id: I1
  text: 基本实体是以 row/column/ref key 定位的不可变 cell
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: cell 保存 JSON，系统不强制对象 schema
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 更新通过写更高 ref key 的新版本完成
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 二级索引是最终一致的
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: MySQL 作为底层存储，弱 schema 不消除应用的演进责任。
  source_ids:
  - S1
interpretation: 观察、当事人归因与维护者机制推断必须分开。
unknowns:
- 内部决策日和未公开指标未知。
sources:
- id: S1
  url: https://www.uber.com/gb/en/blog/schemaless-part-two-architecture/
  publisher: Uber
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开架构原文 cell、索引与工作节点章节。
phase2_conditions:
- 不把弱 schema 等同无数据契约；只比较一类字段变化。
```

## ENG-102

```yaml
id: ENG-102
status: sourced
reason: 一手直接材料可核查事件或发布行为，尚未Case QA。
event: Git LFS 2015 公告
cutoff: 2015-04-08 早期采用决定
initial_facts:
- id: I1
  text: Git 工作流对大型二进制版本化存在困难
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 音视频和数据集是公告举例的目标文件
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Git 内记录小型文本指针
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 实际文件放到远程服务
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: LFS 扩展公开并在 GitHub 开放早期访问，文件可用性增加独立远端依赖。
  source_ids:
  - S1
interpretation: 观察、当事人归因与维护者机制推断必须分开。
unknowns:
- 内部决策日和未公开指标未知。
sources:
- id: S1
  url: https://github.blog/news-insights/product-news/announcing-git-large-file-storage-lfs/
  publisher: GitHub
  published_at: '2015-04-08'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开发布公告。
phase2_conditions:
- 不使用当前价格与配额；远端缺失的后果是维护者机制推断。
```

## ENG-103

```yaml
id: ENG-103
status: sourced
reason: 一手直接材料可核查事件或发布行为，尚未Case QA。
event: PEP3156 asyncio 回调与协作调度
cutoff: Python3.4 对应 PEP 接口设计，非真实线上事故
initial_facts:
- id: I1
  text: 事件循环负责安排回调
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 协作任务通过 Future 与调度器协作
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 同一循环应保证回调互斥执行
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 同步代码未退出时另一个回调不能启动
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 阻塞当前回调会延迟循环内其他回调；这是规范行为推论，不是捏造的故障日志。
  source_ids:
  - S1
interpretation: 观察、当事人归因与维护者机制推断必须分开。
unknowns:
- 内部决策日和未公开指标未知。
sources:
- id: S1
  url: https://peps.python.org/pep-3156/
  publisher: Python / Guido van Rossum
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开 PEP 原文并核对 Mutual Exclusion of Callbacks。
phase2_conditions:
- Phase4 的最小代码必须标为规范演示；不混用后续 async/await 首发年代。
```

## ENG-104

```yaml
id: ENG-104
status: sourced
reason: 一手直接材料可核查事件或发布行为，尚未Case QA。
event: Cloudflare 2025-11-18 Bot Management 故障
cutoff: 2025-11-18 11:20 UTC 初始诊断
initial_facts:
- id: I1
  text: 核心流量出现错误
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: Bot Management 特征文件被定期全网分发
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 元数据权限变化导致生成重复特征行
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 变大的文件触发 bots 模块错误并影响核心代理
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 团队停止异常文件分发、恢复已知良好文件，流量恢复；属于独立 11 月事件。
  source_ids:
  - S1
interpretation: 观察、当事人归因与维护者机制推断必须分开。
unknowns:
- 内部决策日和未公开指标未知。
sources:
- id: S1
  url: https://blog.cloudflare.com/18-november-2025-outage/
  publisher: Cloudflare
  published_at: '2025-11-18'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开独立复盘，核查 query behaviour change 与代理依赖路径。
phase2_conditions:
- 严格区别 ENG155 12月 WAF 解析事故；根因不进入 opening。
```

## ENG-105

```yaml
id: ENG-105
status: sourced
reason: 一手直接材料可核查事件或发布行为，尚未Case QA。
event: OSDI2006 Chubby 锁服务论文
cutoff: 2006 客户端 lease 失效及延迟请求判断
initial_facts:
- id: I1
  text: 接口提供 advisory locks
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 失联与消息延迟会使旧客户端仍有在途操作
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: sequencer 含锁模式和 generation
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 接收方须校验 sequencer 并拒绝过期请求
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 论文给出服务端 fencing 机制；仅获得锁不自动拦住旧写请求。
  source_ids:
  - S1
interpretation: 观察、当事人归因与维护者机制推断必须分开。
unknowns:
- 内部决策日和未公开指标未知。
sources:
- id: S1
  url: https://www.usenix.org/legacy/event/osdi06/tech/full_papers/burrows/burrows.pdf
  publisher: Google / Mike Burrows
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开原论文并核对 §2.4 sequencer、lock delay 与缓存。
phase2_conditions:
- 保留 lease 与 fencing 单一边界，不泛讲所有共识协议。
```

## ENG-106

```yaml
id: ENG-106
status: sourced
reason: 一手直接材料可核查事件或发布行为，尚未Case QA。
event: Language Server Protocol 2016 联合发布
cutoff: 2016-06-27 语言服务接口决策
initial_facts:
- id: I1
  text: 语言服务器向编辑器提供诊断和定义查询
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 语言服务可用独立语言实现
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: didOpen/didChange/definition 通过 JSON-RPC 交互
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 同一服务器实现可以供不同工具复用
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 微软与 Red Hat、Codenvy 宣布共同采用协议，减少各编辑器重复适配。
  source_ids:
  - S1
interpretation: 观察、当事人归因与维护者机制推断必须分开。
unknowns:
- 内部决策日和未公开指标未知。
sources:
- id: S1
  url: https://code.visualstudio.com/blogs/2016/06/27/common-language-protocol
  publisher: Microsoft
  published_at: '2016-06-27'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开当年公告及完整消息流程。
phase2_conditions:
- 协议未自动保证各客户端功能完整一致；未来实现承诺不当成已完成。
```

## ENG-107

```yaml
id: ENG-107
status: sourced
reason: 一手直接材料可核查事件或发布行为，尚未Case QA。
event: Equifax2017 漏洞修补与资产识别
cutoff: 2017-03 Struts 漏洞通告后；完整报告为事后材料
initial_facts:
- id: I1
  text: 在线争议门户处理消费者数据
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 组织有修补通告与资产识别职责
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Equifax向GAO报告漏洞识别与补丁检查未覆盖争议门户。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: GAO记录Equifax关于访问隔离及检测缺陷的解释，未独立验证全部补救效果。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 攻击者通过争议门户取得数据；GAO 将多个控制缺陷分别记录。
  source_ids:
  - S1
interpretation: 观察、当事人归因与维护者机制推断必须分开。
unknowns:
- 内部决策日和未公开指标未知。
sources:
- id: S1
  url: https://www.gao.gov/assets/gao-18-559.pdf
  publisher: U.S. GAO
  published_at: '2018-08-30'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开 GAO 正式调查 PDF，核查 patch 与识别、检测章节。
phase2_conditions:
- GAO 是直接调查来源；对 Equifax自述归因需保持归属，不用后见之明指责单个人。
```

## ENG-108

```yaml
id: ENG-108
status: blocked
reason: 官方摘要可读，但没有取得 hedged requests 的原文成本与实验分布。
event: The Tail at Scale 2013 论文
cutoff: 2013 paper snapshot 待取得正文
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 观察、当事人归因与维护者机制推断必须分开。
unknowns:
- 内部决策日和未公开指标未知。
- 官方摘要可读，但没有取得 hedged requests 的原文成本与实验分布。
sources:
- id: S1
  url: https://research.google/pubs/the-tail-at-scale/
  publisher: Google Research
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- Google 官方元数据页可读；archive/40801.pdf 失败；CACM下载与文章页返回403。
phase2_conditions:
- 数量题不补数字；待正文可用后按备用反事实问题处理相关慢副本。
```

## ENG-109

```yaml
id: ENG-109
status: sourced
reason: 一手直接材料可核查事件或发布行为，尚未Case QA。
event: OpenTelemetry2019 合并公告
cutoff: 2019 年合并方案；具体决策日未知
initial_facts:
- id: I1
  text: 此前两个近似遥测项目并存
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 开发者面对兼容与选择成本
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 领导团队承诺通过 bridge 向统一项目迁移
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 年底把旧项目只读是计划而非当时已完成结果
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: OpenTelemetry 统一项目已发起；公告支持合并意图，不能证明所有厂商绑定已经消失。
  source_ids:
  - S1
interpretation: 观察、当事人归因与维护者机制推断必须分开。
unknowns:
- 内部决策日和未公开指标未知。
sources:
- id: S1
  url: https://opensource.googleblog.com/2019/05/opentelemetry-merger-of-opencensus-and.html
  publisher: OpenTracing / OpenCensus project leaders
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开参与合并的项目负责人原文。
phase2_conditions:
- API 统一和导出后端分离；未读完整首版规范前不声称具体 exporter 保证。
```

## ENG-110

```yaml
id: ENG-110
status: sourced
reason: 一手直接材料可核查事件或发布行为，尚未Case QA。
event: Discord2022 Cassandra→Scylla 消息迁移
cutoff: 2022 messages 迁移前，具体切换日未知
initial_facts:
- id: I1
  text: 消息按 channel 与时间桶分区
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 热点读取影响相同副本上其他请求
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 数据服务引入 request coalescing 和一致散列路由
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 团队迁移到 ScyllaDB 并改写迁移器
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 文章记录迁移完成与维护、延迟改善；不能把全部收益只归因于替换数据库。
  source_ids:
  - S1
interpretation: 观察、当事人归因与维护者机制推断必须分开。
unknowns:
- 内部决策日和未公开指标未知。
sources:
- id: S1
  url: https://discord.com/blog/how-discord-stores-trillions-of-messages
  publisher: Discord
  published_at: '2023-03-06'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开原文热点、数据服务、迁移与结果章节。
phase2_conditions:
- 没有完整同口径总成本和工作量，采用 constrained-decision 备用；限2022消息库一次迁移。
```

## ENG-111

```yaml
id: ENG-111
status: sourced
reason: 一手直接材料可核查事件或发布行为，尚未Case QA。
event: Cloudflare2026-02-20 BYOIP 路由撤销
cutoff: 2026-02-20 撤销后外部连通性诊断
initial_facts:
- id: I1
  text: 只有部分 BYOIP 前缀受影响
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 外部访问可见连接超时
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 配置改动意外撤销约1100个前缀
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 部分撤销还删除了边缘服务配置，重新广播不总足够
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 回退停止新增撤销，工程师恢复前缀配置后修复；1.1.1.1 DNS解析本身不受影响。
  source_ids:
  - S1
interpretation: 观察、当事人归因与维护者机制推断必须分开。
unknowns:
- 内部决策日和未公开指标未知。
sources:
- id: S1
  url: https://blog.cloudflare.com/cloudflare-outage-february-20-2026/
  publisher: Cloudflare
  published_at: '2026-02-21'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开独立2026复盘，核查BGP观察点、恢复与DNS区别。
phase2_conditions:
- 不能和2022网络事故混为同一事件；一条邻居统计不等于全互联网观测。
```

## ENG-112

```yaml
id: ENG-112
status: sourced
reason: 直接材料支持事件或artifact行为，完整训练未验收。
event: Node.js v10.24.1 libuv 线程池文档
cutoff: 固定v10.24.1 API快照，非2009首发时行为
initial_facts:
- id: I1
  text: 异步文件API与部分crypto操作使用libuv线程池
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: dns.lookup也使用线程池
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 线程池默认4线程且大小固定
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 长任务会影响其他看似无关的池内API
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 官方文档明确池饱和可影响异步API延迟；不能将所有I/O都归为线程池。
  source_ids:
  - S1
interpretation: 来源描述与我们的推论分开；不能以当前文档倒推早年版本。
unknowns:
- 精确决策日及未公开观测未知。
sources:
- id: S1
  url: https://nodejs.org/download/release/v10.24.1/docs/api/cli.html
  publisher: Node.js
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开旧版官方文档 UV_THREADPOOL_SIZE 章节。
phase2_conditions:
- 需要进一步给最小请求类型与回调执行位置；不得编造线上指标。
```

## ENG-113

```yaml
id: ENG-113
status: sourced
reason: 直接材料支持事件或artifact行为，完整训练未验收。
event: etcd v3.3 灾难恢复规则
cutoff: v3.3 集群失去quorum后的恢复决定
initial_facts:
- id: I1
  text: N成员集群最多容忍(N-1)/2永久故障
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 成员暂时失效不同于数据永久损坏
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 永久失去多数后不能继续接受更新
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: snapshot restore用于重建逻辑集群
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 规范区分成员恢复与灾难恢复；不能靠继续向无quorum集群添加成员恢复共识。
  source_ids:
  - S1
interpretation: 来源描述与我们的推论分开；不能以当前文档倒推早年版本。
unknowns:
- 精确决策日及未公开观测未知。
sources:
- id: S1
  url: https://etcd.io/docs/v3.3/op-guide/recovery/
  publisher: etcd
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开v3.3恢复文档并核查quorum段落。
phase2_conditions:
- 保持2015—2018候选版本范围；不能自动承诺恢复所有未快照写入。
```

## ENG-114

```yaml
id: ENG-114
status: sourced
reason: 直接材料支持事件或artifact行为，完整训练未验收。
event: Gitpod Classic snapshot 分享规则
cutoff: 2026-10-25读取的Classic文档快照；不能倒推2020首发
initial_facts:
- id: I1
  text: snapshot是工作区某时点状态
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 跟随snapshot链接会在跟随者账户开启新workspace
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 文档明确分享敏感信息需谨慎
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 怀疑凭据泄漏时建议旋转凭据
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: snapshot复用提供可复现场景，但不会自动清除分享内容中的敏感信息。
  source_ids:
  - S1
interpretation: 来源描述与我们的推论分开；不能以当前文档倒推早年版本。
unknowns:
- 精确决策日及未公开观测未知。
sources:
- id: S1
  url: https://ona.com/docs/classic/user/configure/workspaces/collaboration
  publisher: Gitpod / Ona
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 检索Gitpod snapshot；官方旧链接重定向至Ona Classic文档并读取。
phase2_conditions:
- 2020—开放区间内可保留Classic artifact，Phase4必须固定文档/源码版本和snapshot内容，不能断言2020凭据处理。
```

## ENG-115

```yaml
id: ENG-115
status: sourced
reason: 直接材料支持事件或artifact行为，完整训练未验收。
event: XZ5.6.0/5.6.1后门发现
cutoff: 2024-03-29公开披露前的异常排查
initial_facts:
- id: I1
  text: SSH相关进程出现异常性能及工具检查信号
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 近期liblzma版本是调查对象
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 部分恶意构建逻辑仅在发布tarball中
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: Git源码快照与上游发布工件并非同一内容
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 发现者公开将问题定位到上游发布链；不是仅Debian包被改。
  source_ids:
  - S1
interpretation: 来源描述与我们的推论分开；不能以当前文档倒推早年版本。
unknowns:
- 精确决策日及未公开观测未知。
sources:
- id: S1
  url: https://www.openwall.com/lists/oss-security/2024/03/29/4
  publisher: Andres Freund
  published_at: '2024-03-29'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开发现者原始邮件，核查tarball与Git差异及调查起点。
phase2_conditions:
- 事实保持发现者当时已披露范围；攻击者组织身份未知。
```

## ENG-116

```yaml
id: ENG-116
status: sourced
reason: 直接材料支持事件或artifact行为，完整训练未验收。
event: Envoy xDS当前文档ACK语义
cutoff: 2026-10-25文档快照；不是2017语义断言
initial_facts:
- id: I1
  text: 控制面通过DiscoveryResponse传送资源
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 客户端用nonce对应收到的响应
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: ACK表示资源单独校验有效及应用意图
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: ACK之后仍可能应用失败
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 官方协议文档明确ACK不保证配置已成功生效，更不保证业务健康。
  source_ids:
  - S1
interpretation: 来源描述与我们的推论分开；不能以当前文档倒推早年版本。
unknowns:
- 精确决策日及未公开观测未知。
sources:
- id: S1
  url: https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol.html
  publisher: Envoy
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 尝试v1.12和v1.17归档均失败；读取最新文档ACK/NACK摘要。
phase2_conditions:
- 开放年代候选可锚当前artifact；Phase4须锁commit，不能混称为2017原版。
```

## ENG-117

```yaml
id: ENG-117
status: blocked
reason: 已找到ZippyDB真实架构演进文章，但未找到本题所需独立SSD成本优化与同负载成本数据。
event: ZippyDB SSD单位成本优化候选
cutoff: 2010s具体优化未确认
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 来源描述与我们的推论分开；不能以当前文档倒推早年版本。
unknowns:
- 精确决策日及未公开观测未知。
- 已找到ZippyDB真实架构演进文章，但未找到本题所需独立SSD成本优化与同负载成本数据。
sources:
- id: S1
  url: https://engineering.fb.com/2021/08/06/core-infra/zippydb/
  publisher: Meta
  published_at: '2021-08-06'
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 分别检索ZippyDB+SSD+cost、Meta官方ZippyDB；打开2021原文，SSD未命中；2026新闻不作2010s证据。
phase2_conditions:
- 独立优化条件未满足；进入待替换审查，不以通用RocksDB/集中容量池文章冒充SSD优化。
```

## ENG-118

```yaml
id: ENG-118
status: sourced
reason: 直接材料支持事件或artifact行为，完整训练未验收。
event: Knight Capital2012部署事故SEC调查
cutoff: 2012-08-01市场开盘前后的发布检查
initial_facts:
- id: I1
  text: SMARS部署到8台服务器
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: I2
  text: 旧Power Peg代码保留在一台未更新服务器
  source_ids:
  - S1
  availability: unknown
- id: E1
  text: 新标志触发旧代码执行
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 组织没有充分部署复核与错误订单限额控制
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 错误交易形成巨大非预期头寸并造成约4.6亿美元损失。
  source_ids:
  - S1
interpretation: 来源描述与我们的推论分开；不能以当前文档倒推早年版本。
unknowns:
- 精确决策日及未公开观测未知。
sources:
- id: S1
  url: https://www.sec.gov/files/litigation/admin/2013/34-70694.pdf
  publisher: U.S. SEC
  published_at: '2013-10-16'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开SEC行政处罚原文，核查漏部署、控制缺陷与损失。
phase2_conditions:
- 不能将未部署节点信息当作所有操作者当时已知；初始材料只给发布流程观察。
```

## ENG-119

```yaml
id: ENG-119
status: sourced
reason: 直接材料支持事件或artifact行为，完整训练未验收。
event: Google F1 VLDB2013论文
cutoff: 2013论文中的F1/Spanner分层判断
initial_facts:
- id: I1
  text: F1服务AdWords关系数据需求
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: Spanner提供跨数据中心同步复制
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: F1在Spanner上提供SQL与分布式查询层
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 同步复制会增加提交延迟
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 已发表设计组合关系查询和底层强一致存储；不能把查询优化责任全归于Spanner。
  source_ids:
  - S1
interpretation: 来源描述与我们的推论分开；不能以当前文档倒推早年版本。
unknowns:
- 精确决策日及未公开观测未知。
sources:
- id: S1
  url: https://www.vldb.org/pvldb/vol6/p1068-shute.pdf
  publisher: Google authors / VLDB
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 官方论文页及原VLDB PDF已打开；猜测Google archive下载失败。
phase2_conditions:
- Phase4按论文层次限定单查询责任；不将F1等同Spanner产品。
```

## ENG-120

```yaml
id: ENG-120
status: blocked
reason: 官方2.2发布说明可证持久流、至少一次及窗口去重，但不能据此认定是2020发布契约。
event: NATS JetStream2020候选
cutoff: 2020具体preview语义待核定
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 来源描述与我们的推论分开；不能以当前文档倒推早年版本。
unknowns:
- 精确决策日及未公开观测未知。
- 官方2.2发布说明可证持久流、至少一次及窗口去重，但不能据此认定是2020发布契约。
sources:
- id: S1
  url: https://github.com/nats-io/nats.docs/blob/master/release_notes/whats_new_22.md
  publisher: NATS
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 猜测JetStream发布URL失败；搜索到2.2正式发布资料和2019技术预览，打开官方2.2 release notes。
phase2_conditions:
- 需核定2020preview或显式改期映射；不把消息exactly once扩展为业务副作用一次。
```

## ENG-121

```yaml
id: ENG-121
status: sourced
reason: 直接材料支持事件或artifact行为，完整训练未验收。
event: Pants2.0依赖推断设计
cutoff: 2020-10-29依赖声明选择
initial_facts:
- id: I1
  text: Python导入语句可提供依赖信息
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 构建图控制缓存和按影响范围执行
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Pants2.0按文件推断依赖
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: BUILD字段可以覆盖或扩展推断
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 依赖声明负担下降，但不等于任意运行时动态依赖都能被推断。
  source_ids:
  - S1
interpretation: 来源描述与我们的推论分开；不能以当前文档倒推早年版本。
unknowns:
- 精确决策日及未公开观测未知。
sources:
- id: S1
  url: https://www.pantsbuild.org/blog/2020/10/29/dependency-inference
  publisher: Pants
  published_at: '2020-10-29'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开2.0发布及依赖推断专文。
phase2_conditions:
- 只讨论漏推断时的显式退路；性能百分比是作者报告且不作通用预测。
```

## ENG-122

```yaml
id: ENG-122
status: blocked
reason: 本轮未取得可读的指定旧版监督/持久化正文。
event: Akka actor重启状态候选
cutoff: 2010s版本语义待原文
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 与真实史实分开标注机制推断；示例不得变成虚构事故。
unknowns:
- 未公开工作量、内部决策过程或具体故障日志未知。
- 本轮未取得可读的指定旧版监督/持久化正文。
sources:
- id: S1
  url: https://doc.akka.io/docs/akka/2.5/general/supervision.html
  publisher: Akka
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 尝试官方2.5 actors、2.5/2.6 supervision及v2.5.32 GitHub文档路径均失败；不以常识填补。
phase2_conditions:
- 需要Classic或PersistentActor明确模式、确认点和投递规则；不能泛称重启恢复业务状态。
```

## ENG-123

```yaml
id: ENG-123
status: sourced
reason: 直接资料可证事件或artifact；完整Case QA尚未执行。
event: OpenAPI3.0.0正式规范
cutoff: 2017-07-26契约设计时
initial_facts:
- id: I1
  text: 规范为HTTP API提供语言无关描述
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 消费方无需读实现源码即可了解接口能力
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 规范分别定义参数、requestBody和responses
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 规范的文档对象不自动实施服务端校验
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 3.0.0规范已发布，契约可支撑生成工具；一致执行仍需实现和验证。
  source_ids:
  - S1
interpretation: 与真实史实分开标注机制推断；示例不得变成虚构事故。
unknowns:
- 未公开工作量、内部决策过程或具体故障日志未知。
sources:
- id: S1
  url: https://spec.openapis.org/oas/v3.0.0.html
  publisher: OpenAPI Initiative / Linux Foundation
  published_at: '2017-07-26'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开准确3.0.0版本规范，核对版本和接口对象。
phase2_conditions:
- 不把先写契约当作已证因果成功；固定一次接口变更，示例须标明。
```

## ENG-124

```yaml
id: ENG-124
status: sourced
reason: 直接资料可证事件或artifact；完整Case QA尚未执行。
event: Kubernetes CVE-2019-11253官方披露
cutoff: 2019安全通告后的补丁/授权决定
initial_facts:
- id: I1
  text: API接受YAML或JSON请求
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 旧RBAC默认策略对匿名请求更宽松
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 获授权的恶意载荷可耗尽CPU或内存
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 在授权阶段被拒绝的请求不触发该漏洞
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 官方列出1.13.12、1.14.8、1.15.5和1.16.2修复版本并给出RBAC缓解。
  source_ids:
  - S1
interpretation: 与真实史实分开标注机制推断；示例不得变成虚构事故。
unknowns:
- 未公开工作量、内部决策过程或具体故障日志未知。
sources:
- id: S1
  url: https://github.com/kubernetes/kubernetes/issues/83253
  publisher: Kubernetes Security Response Committee
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开官方CVE issue正文和mitigation部分。
phase2_conditions:
- 区分原始2019-09-27 issue时间与后续编辑的CVE通告；不把所有匿名用户都视为获授权。
```

## ENG-125

```yaml
id: ENG-125
status: sourced
reason: 直接资料可证事件或artifact；完整Case QA尚未执行。
event: Cloudflare2019-07-02 WAF正则事故
cutoff: 2019-07-02 13:45 UTC初始报警
initial_facts:
- id: I1
  text: 新WAF规则刚经全球发布
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 外部测试、502和CPU饱和报警相继出现
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: simulate模式仍会执行正则
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 规则性能测试未覆盖失控CPU，规则SOP允许直接全球发布
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 执行全球WAF终止后CPU与流量恢复，后续验证回退再启用WAF。
  source_ids:
  - S1
interpretation: 与真实史实分开标注机制推断；示例不得变成虚构事故。
unknowns:
- 未公开工作量、内部决策过程或具体故障日志未知。
sources:
- id: S1
  url: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/
  publisher: Cloudflare
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开官方详细复盘并读取事件、测试缺口与恢复。
phase2_conditions:
- 不复用2025两起事故根因；单一主线是规则预验证与回退证据。
```

## ENG-126

```yaml
id: ENG-126
status: blocked
reason: 官方深度文档可证primary/secondary锁恢复机制，但未证其内容在2016版本的具体状态。
event: TiDB2016 Percolator候选
cutoff: 2016具体版本尚未核定
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 与真实史实分开标注机制推断；示例不得变成虚构事故。
unknowns:
- 未公开工作量、内部决策过程或具体故障日志未知。
- 官方深度文档可证primary/secondary锁恢复机制，但未证其内容在2016版本的具体状态。
sources:
- id: S1
  url: https://tikv.github.io/deep-dive-tikv/distributed-transaction/percolator.html
  publisher: TiKV
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 打开TiKV Percolator文档读完整prewrite/commit/crash章节；2017 PingCAP历史文章读取失败。
phase2_conditions:
- 需定位2016代码/文档快照；不将当前或未标日期文档当作2016真实执行。
```

## ENG-127

```yaml
id: ENG-127
status: sourced
reason: 直接资料可证事件或artifact；完整Case QA尚未执行。
event: Buck2 2023公开的单一增量图
cutoff: 2023-04-06发布时的增量计算设计
initial_facts:
- id: I1
  text: Buck2以Rust重写且支持可扩展规则
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 大量构建工作可并行
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 发布文说明单一增量依赖图避免分阶段设计
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 动态依赖特性被限制以保持查询速度和密封性
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: Buck2已开源；Meta报告内部构建更快，但不构成所有工作量的性能保证。
  source_ids:
  - S1
interpretation: 与真实史实分开标注机制推断；示例不得变成虚构事故。
unknowns:
- 未公开工作量、内部决策过程或具体故障日志未知。
sources:
- id: S1
  url: https://engineering.fb.com/2023/04/06/open-source/buck2-open-source-large-scale-build-system/
  publisher: Meta
  published_at: '2023-04-06'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
- id: S2
  url: https://github.com/facebook/buck2/blob/main/dice/dice/docs/index.md
  publisher: Meta
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 打开2023公告及官方DICE源码文档确认引擎身份。
phase2_conditions:
- DICE源码文档是滚动版本，具体细粒度失效规则要锁2023commit，不混入modern DICE重写。
```

## ENG-128

```yaml
id: ENG-128
status: blocked
reason: 已找到官方架构说明但包含后续压缩和多节点内容，不能确认2017查询窗口的版本行为。
event: TimescaleDB2017 hypertables候选
cutoff: 2017快照待取得
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 与真实史实分开标注机制推断；示例不得变成虚构事故。
unknowns:
- 未公开工作量、内部决策过程或具体故障日志未知。
- 已找到官方架构说明但包含后续压缩和多节点内容，不能确认2017查询窗口的版本行为。
sources:
- id: S1
  url: https://github.com/timescale/docs.timescale.com-content/blob/master/introduction/architecture.md
  publisher: Timescale
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 检索2017架构、尝试原论文和TigerData重定向均失败；0.5.0 README路径读取失败；当前说明只作后续研究入口。
phase2_conditions:
- 数量题不得补数据；获得历史版本后使用prediction-counterfactual备用，需明确chunk规则。
```

## ENG-129

```yaml
id: ENG-129
status: sourced
reason: 直接资料可证事件或artifact；完整Case QA尚未执行。
event: 2015浏览器Promise微任务实验
cutoff: 2015-08-17文中测试片段运行前
initial_facts:
- id: I1
  text: 同一脚本安排setTimeout和Promise.then
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 同步script start/end在当前任务执行
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 文章给出规范期望次序promise先于timer
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 部分当时浏览器实际出现timer先于promise的差异
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 有可运行片段和当时浏览器观察；不能用今天单一引擎结果冒充2015所有浏览器。
  source_ids:
  - S1
interpretation: 与真实史实分开标注机制推断；示例不得变成虚构事故。
unknowns:
- 未公开工作量、内部决策过程或具体故障日志未知。
sources:
- id: S1
  url: https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/
  publisher: Jake Archibald
  published_at: '2015-08-17'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开作者原始技术演示，核对代码、预期及兼容性差异。
phase2_conditions:
- 宿主固定浏览器，区分规范期望和真实实现观察；不混Node nextTick。
```

## ENG-130

```yaml
id: ENG-130
status: sourced
reason: 直接资料可证事件或artifact；完整Case QA尚未执行。
event: YouTube2011 Hydra并行视频处理
cutoff: 2011提速设计；具体决策日未知
initial_facts:
- id: I1
  text: 上传文件的尺寸、时长和分辨率在增加
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 用户等待视频可发布是优化目标
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 上传与处理可以重叠
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: Hydra把视频拆成小块并行处理再重组
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 工程师报告处理速度与短时间发布比例改善；没有披露完整调度成本或积压样本。
  source_ids:
  - S1
interpretation: 与真实史实分开标注机制推断；示例不得变成虚构事故。
unknowns:
- 未公开工作量、内部决策过程或具体故障日志未知。
sources:
- id: S1
  url: https://blog.youtube/news-and-events/speed-thrills-tackling-youtube-video/
  publisher: YouTube
  published_at: '2011-02-14'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开当事工程师官方博客，核查Hydra与发布延迟。
phase2_conditions:
- 源支持降低等待的设计，若坚持具体队列优先级需补资料；不能编造预算或优先队列。
```

## ENG-131

```yaml
id: ENG-131
status: sourced
reason: 直接资料可证事件或artifact；完整Case QA尚未执行。
event: Bazel3.7.0 Starlark扩展规则
cutoff: 3.7.0文档快照，属于2017—2020范围
initial_facts:
- id: I1
  text: 规则把输入通过action转成输出
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 工具和标准库也应计入规则输入
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Starlark规则位于bzl并由BUILD加载
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 规则有loading、analysis和execution阶段约束
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 公开扩展模型可实现原生未支持的工具；接口设计须满足阶段边界。
  source_ids:
  - S1
interpretation: 与真实史实分开标注机制推断；示例不得变成虚构事故。
unknowns:
- 未公开工作量、内部决策过程或具体故障日志未知。
sources:
- id: S1
  url: https://docs.bazel.build/versions/3.7.0/skylark/rules.html
  publisher: Bazel
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开固定3.7.0规则文档及2018语言规范分离公告。
phase2_conditions:
- 不能把可用内部实现自动当稳定API；Phase4围绕单项扩展责任。
```

## ENG-132

```yaml
id: ENG-132
status: sourced
reason: 直接来源支持所选artifact或事件，完整Case QA未执行。
event: GitHub2018-10-21数据库网络分区事故
cutoff: 2018-10-21 23:13 UTC恢复决策
initial_facts:
- id: I1
  text: 东西两地数据库含对方未复制的写入
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 应用不能承受跨区域写入延迟
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 团队选择fail-forward以保护已接收写入
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 暂停webhook与Pages，重建副本后恢复拓扑
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 服务长时间降级后恢复；复盘发布时少量写入仍在人工核对，不宜简化为已全部无损。
  source_ids:
  - S1
interpretation: 只允许依据已核查材料推演；推断需明示，不能写成实测史实。
unknowns:
- 未公开的完整工作量、精确内部决策过程未知。
sources:
- id: S1
  url: https://github.blog/news-insights/company-news/oct21-post-incident-analysis/
  publisher: GitHub
  published_at: '2018-10-30'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开候选示例链接发现只是初报，另找并读正式post-incident analysis。
phase2_conditions:
- 核源URL改指详细复盘；恢复速度与一致性围绕单一决策。
```

## ENG-133

```yaml
id: ENG-133
status: sourced
reason: 直接来源支持所选artifact或事件，完整Case QA未执行。
event: Cassandra2.1可调一致性规则
cutoff: 2.1文档快照；读请求发出前
initial_facts:
- id: I1
  text: 每次I/O可选择一致性级别
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: RF3的quorum为2个副本
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: ONE可能读到陈旧数据
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 读写quorum交集提供已成功写的可见性条件
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 官方旧版文档支持指定副本配置推演；不能将quorum自动当作并发线性化承诺。
  source_ids:
  - S1
interpretation: 只允许依据已核查材料推演；推断需明示，不能写成实测史实。
unknowns:
- 未公开的完整工作量、精确内部决策过程未知。
sources:
- id: S1
  url: https://docs.datastax.com/en/cassandra-oss/2.1/cassandra/dml/dml_config_consistency_c.html
  publisher: DataStax
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开DataStax Cassandra2.1归档，核对读写和quorum交集。
phase2_conditions:
- 版本落在2010—2015范围；Phase4需单独注明并发写与时间戳前提。
```

## ENG-134

```yaml
id: ENG-134
status: sourced
reason: 直接来源支持所选artifact或事件，完整Case QA未执行。
event: Gradle6.6 Configuration Cache
cutoff: 2020年6.6配置结果复用前
initial_facts:
- id: I1
  text: 配置缓存保存任务图的状态
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 任务依赖的输入必须可重现
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 部分活JVM状态不能被序列化/重建
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 未声明系统属性读取与执行期Project访问会报缓存问题
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 6.6文档给出违规检测及失败示例，默认不静默接受不兼容缓存。
  source_ids:
  - S1
interpretation: 只允许依据已核查材料推演；推断需明示，不能写成实测史实。
unknowns:
- 未公开的完整工作量、精确内部决策过程未知。
sources:
- id: S1
  url: https://docs.gradle.org/6.6/userguide/configuration_cache.html
  publisher: Gradle
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开6.6发布说明和固定版本requirements章节。
phase2_conditions:
- 区别配置缓存与构建action输出缓存；只核验一次不适合复用的配置。
```

## ENG-135

```yaml
id: ENG-135
status: sourced
reason: 直接来源支持所选artifact或事件，完整Case QA未执行。
event: npm event-stream2018依赖劫持
cutoff: 2018-11-26恶意包告警后的应对
initial_facts:
- id: I1
  text: 新维护者给event-stream加入flatmap-stream依赖
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 恶意逻辑仅针对特定构建环境触发
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: npm移除flatmap-stream与event-stream3.3.6
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 发布构建过程会注入针对Copay的钱包恶意代码
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: npm接管包避免继续滥用；其公告引用Copay确认特定已发行版本受影响。
  source_ids:
  - S1
interpretation: 只允许依据已核查材料推演；推断需明示，不能写成实测史实。
unknowns:
- 未公开的完整工作量、精确内部决策过程未知。
sources:
- id: S1
  url: https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident
  publisher: npm
  published_at: '2018-11-27'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开npm官方技术分析全文。
phase2_conditions:
- 不推断所有安装者都泄露私钥；源中的Copay确认属明确转述。
```

## ENG-136

```yaml
id: ENG-136
status: sourced
reason: 直接来源支持所选artifact或事件，完整Case QA未执行。
event: Druid2014论文实时摄取与handoff
cutoff: 2014论文的单事件查询可见性
initial_facts:
- id: I1
  text: 实时节点摄取事件流并维护可查询索引
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 历史节点服务不可变segment
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 事件在实时索引后即可查询
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: persist/merge/handoff转成列式不可变segment后再交接
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 论文描述查询不必等深存储与历史节点接管，但摄取不等同任意更新支持。
  source_ids:
  - S1
interpretation: 只允许依据已核查材料推演；推断需明示，不能写成实测史实。
unknowns:
- 未公开的完整工作量、精确内部决策过程未知。
sources:
- id: S1
  url: https://people.csail.mit.edu/matei/courses/2015/6.S897/readings/druid.pdf
  publisher: Metamarkets authors
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 初次猜测arxiv号是无关物理论文已排除；检索并读原作者SIGMOD论文镜像。
phase2_conditions:
- 采用2014 artifact，不捏造2011事故；聚合/更新能力的损失要按论文而非当前Druid推断。
```

## ENG-137

```yaml
id: ENG-137
status: blocked
reason: 当前man page可读但没有本题所需2002版本与同口径连接/就绪性能材料。
event: Linux epoll2002候选
cutoff: 2002接口与性能比较未核完整
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 只允许依据已核查材料推演；推断需明示，不能写成实测史实。
unknowns:
- 未公开的完整工作量、精确内部决策过程未知。
- 当前man page可读但没有本题所需2002版本与同口径连接/就绪性能材料。
sources:
- id: S1
  url: https://man7.org/linux/man-pages/man7/epoll.7.html
  publisher: Linux man-pages
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 读取man7手册；检索作者2001/2002 nio-improve原页并尝试打开，返回502；不据当前接口倒推旧版复杂度。
phase2_conditions:
- 数量题优先备用prediction-counterfactual；仍需原始接口成本说明，不编造benchmark。
```

## ENG-138

```yaml
id: ENG-138
status: sourced
reason: 直接来源支持所选artifact或事件，完整Case QA未执行。
event: Stripe2017幂等API设计文章
cutoff: 2017-02-22契约快照
initial_facts:
- id: I1
  text: 连接中断可能发生在服务端操作成功之后
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 客户端因此无法确定是否可安全重试
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 请求携带唯一幂等key
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 服务端可识别重复请求并返回原结果
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 文章解释安全重试契约，文章年不是API最初发布年。
  source_ids:
  - S1
interpretation: 只允许依据已核查材料推演；推断需明示，不能写成实测史实。
unknowns:
- 未公开的完整工作量、精确内部决策过程未知。
sources:
- id: S1
  url: https://stripe.com/blog/idempotency
  publisher: Stripe
  published_at: '2017-02-22'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开2017原文核对模糊失败与Idempotency-Key流程。
phase2_conditions:
- 文章未核足key保留期；Phase4补当时文档，不把当前24小时策略倒推到2017。
```

## ENG-139

```yaml
id: ENG-139
status: sourced
reason: 直接来源支持所选artifact或事件，完整Case QA未执行。
event: Cloudflare2022-06-21网络中断
cutoff: 2022-06-21 06:27 UTC配置部署后
initial_facts:
- id: I1
  text: 配置分批部署至不同网络架构地点
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: MCP架构地点受到集中影响
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: BGP策略条目重排撤销关键前缀
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 回退期间工程师彼此覆盖改动延长恢复
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 19个地点离线造成显著流量影响，完成回退后恢复。
  source_ids:
  - S1
interpretation: 只允许依据已核查材料推演；推断需明示，不能写成实测史实。
unknowns:
- 未公开的完整工作量、精确内部决策过程未知。
sources:
- id: S1
  url: https://blog.cloudflare.com/cloudflare-outage-on-june-21-2022/
  publisher: Cloudflare
  published_at: '2022-06-21'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开官方独立复盘并核对逐阶段部署和网络架构。
phase2_conditions:
- 与2026 BYOIP撤销区分；不能仅按地点数估算请求影响。
```

## ENG-140

```yaml
id: ENG-140
status: blocked
reason: 当前官方架构可证Raft角色，但尚无2015版本与单请求路径的原始材料。
event: Consul2015多数据中心架构候选
cutoff: 2015版本快照未取得
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 只允许依据已核查材料推演；推断需明示，不能写成实测史实。
unknowns:
- 未公开的完整工作量、精确内部决策过程未知。
- 当前官方架构可证Raft角色，但尚无2015版本与单请求路径的原始材料。
sources:
- id: S1
  url: https://developer.hashicorp.com/consul/docs/architecture
  publisher: HashiCorp
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 检索2015 WAN/Raft；尝试v0.6.0两种官方GitHub历史文档路径均Cache miss。
phase2_conditions:
- 不以当前WAN/LAN和新WAL后端倒推2015；需旧版文档确认跨DC写入边界。
```

## ENG-141

```yaml
id: ENG-141
status: sourced
reason: 直接来源支持所选artifact或事件，完整Case QA未执行。
event: Atom1.32 Tree-sitter发布
cutoff: 2018-10-31局部编辑反馈判断
initial_facts:
- id: I1
  text: 语法高亮和折叠依赖代码结构
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 整文件解析会延迟编辑反馈
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Tree-sitter随编辑增量更新语法树
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: Atom1.32默认采用新解析体系
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 发布文记录增量解析带来的编辑功能；未提供本题精确节点或字符更新成本。
  source_ids:
  - S1
interpretation: 只允许依据已核查材料推演；推断需明示，不能写成实测史实。
unknowns:
- 未公开的完整工作量、精确内部决策过程未知。
sources:
- id: S1
  url: https://github.blog/news-insights/product-news/atoms-new-parsing-system/
  publisher: GitHub
  published_at: '2018-10-31'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开2018官方文章并核对Speed与功能段落。
phase2_conditions:
- 主线应为更新范围预测；精确错误恢复和节点复用仍需固定版本代码，不使用虚构性能数。
```

## ENG-142

```yaml
id: ENG-142
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: Workers2018 isolate执行环境设计
cutoff: 2018-11-09设计对比；不是2017首发全部承诺
initial_facts:
- id: I1
  text: 边缘系统需要低开销执行不可信客户代码
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 单进程可容纳多个V8 isolate
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: isolate把代码与可访问的变量组合成隔离上下文
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 厂商设计目标是快速启动且限制跨isolate内存访问
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: Workers采用isolate而非每租户容器；文章性能与安全主张属于厂商解释。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://blog.cloudflare.com/cloud-computing-without-containers/
  publisher: Cloudflare
  published_at: '2018-11-09'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开当时官方技术文章隔离与部署背景。
phase2_conditions:
- 不得把V8名称当安全证明；具体攻击模型和基准仍待Case QA。
```

## ENG-143

```yaml
id: ENG-143
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: Okta2023支持系统HAR泄漏
cutoff: 2023-10-13客户提供可疑IP后的日志选择
initial_facts:
- id: I1
  text: 支持系统附件可包含HAR文件
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: I2
  text: 不同文件访问入口产生不同日志事件与ID
  source_ids:
  - S1
  availability: unknown
- id: E1
  text: 攻击者取得部分HAR内会话token
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: Okta报告5个客户的会话被劫持
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 后续扩大日志核查识别额外文件访问；服务账户凭据暴露途径仍以最可能解释表达。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://sec.okta.com/articles/2023/11/unauthorized-access-oktas-support-case-management-system-root-cause/
  publisher: Okta
  published_at: '2023-11-03'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开独立根因通告，核查HAR、日志路径与已确认利用。
phase2_conditions:
- 区别token、密码与支持附件；134客户为该通告阶段范围，不冒充后续调查最终全集。
```

## ENG-144

```yaml
id: ENG-144
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: MergeTree排序键文档artifact
cutoff: 2026-10-25读取快照；非2016所有语法
initial_facts:
- id: I1
  text: 数据由多个按键排序的part构成
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: ORDER BY指定排序键
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 稀疏索引有额外读取粒度
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 后台merge重组parts以改善存储
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 文档给出排序键与索引裁剪机制；单类查询可据此做选择而不是全表参数同时优化。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://clickhouse.com/docs/reference/engines/table-engines/mergetree-family/mergetree
  publisher: ClickHouse
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开官方文档核对ORDER BY、Data storage与sparse index。
phase2_conditions:
- Phase4锁定具体版本；排除当前projection、TTL等后加特性，不能回填2016。
```

## ENG-145

```yaml
id: ENG-145
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: C++11内存序工作草案文本
cutoff: C++11语义由N3337镜像核对，草案发表于2012
initial_facts:
- id: I1
  text: 标准提供relaxed、acquire与release等内存序
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: atomic访问的原子性与其他内存排序是不同保证
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: relaxed不提供跨操作排序
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 读到release sequence值的acquire与release同步
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 规范规定发布读取的同步条件，atomic标志本身不能替代正确的读值与同步关系。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://timsong-cpp.github.io/cppwp/n3337/atomics.order
  publisher: WG21 draft; Tim Song HTML transcription
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 2011 N3242 PDF过大不可读，HTML猜测失败；读取N3337逐段标准转录。
phase2_conditions:
- 明确2012工作草案用于核对C++11语义，不能当2011正式ISO版；Phase4用无数据竞争最小代码。
```

## ENG-146

```yaml
id: ENG-146
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: React16.8 Hooks稳定发布
cutoff: 2019-02-06引入Hooks的状态抽象
initial_facts:
- id: I1
  text: 类组件此前承载状态与生命周期逻辑
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 复用有状态逻辑是Hooks目标
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 16.8提供稳定Hooks实现
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 既有class与Hooks可并存，不要求全量重写
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: Hooks稳定发布；函数闭包的state读取受创建时render影响，需配FAQ解释。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://legacy.reactjs.org/blog/2019/02/06/react-v16.8.0.html
  publisher: React
  published_at: '2019-02-06'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
- id: S2
  url: https://legacy.reactjs.org/docs/hooks-faq.html
  publisher: React
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 打开2019发布公告及旧版Hooks FAQ stale props/state示例。
phase2_conditions:
- FAQ为后续归档文本，不能断言每一FAQ细节当天已有；代码作为抽象推演。
```

## ENG-147

```yaml
id: ENG-147
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: Facebook2021-10-04骨干网中断
cutoff: 2021-10-04网络维护命令执行后恢复决定
initial_facts:
- id: I1
  text: 骨干连接数据中心与对外服务节点
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: DNS服务依据到数据中心的连通性发布BGP路由
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 审计工具缺陷未挡住断开骨干命令
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 骨干失效引发DNS撤路由及运维工具不可用
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 派工程师到现场恢复骨干，再分阶段恢复流量，避免同时恢复带来的负载冲击。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/
  publisher: Meta
  published_at: '2021-10-05'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开当事工程团队详细复盘。
phase2_conditions:
- 初轮不透露命令根因；恢复路径与自身依赖是唯一决策范围。
```

## ENG-148

```yaml
id: ENG-148
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: Uber2016 Ringpop成员与请求转发设计
cutoff: 2016-02-04节点加入时路由判断
initial_facts:
- id: I1
  text: 工作节点用SWIM变体传播成员视图
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 一致散列将工作映射至节点
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 成员传播最终使各节点发现彼此
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: handle-or-forward在应用内转发到负责节点
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: Ringpop在Geospatial实际部署；文章说明自动路由，但不保证瞬时所有视图一致。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://www.uber.com/us/en/blog/ringpop-open-source-nodejs-library/
  publisher: Uber
  published_at: '2016-02-04'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开2016原文成员、散列和转发流程。
phase2_conditions:
- 暂时分歧具体错误需源码/版本确认；不能将官方宣传every request reaches correct node当故障下绝对保证。
```

## ENG-149

```yaml
id: ENG-149
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: GitHub Actions cache信任边界文档
cutoff: 2026-10-25文档快照；不是2019原始权限
initial_facts:
- id: I1
  text: cache复用按key与restore-keys查找
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 作用域包含分支和PR merge ref
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: PR merge ref缓存不能由base分支或其他PR直接复用
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 低信任触发器默认分支缓存有额外写入限制
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 当前文档明确缓存范围及污染威胁；同key不能跨越作用域自动证明可信。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching
  publisher: GitHub
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开官方cache文档access restrictions及低信任触发器段落。
phase2_conditions:
- Phase4必须锁服务策略时点；禁止将当前新增只读规则回填2019。
```

## ENG-150

```yaml
id: ENG-150
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: Dropbox2016披露Magic Pocket迁移
cutoff: 2013—2015自建存储决策；具体内部决策日未知
initial_facts:
- id: I1
  text: 用户文件规模推动专用存储需求
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 系统必须保持高耐久和可用性
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 先双写试运行再只由自有系统服务部分数据
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 扩容与跨区域传输需额外硬件和自动化工程
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 2016公告时超过90%用户数据由自建基础设施存储服务；未披露可复现的全部成本账。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://dropbox.tech/infrastructure/magic-pocket-infrastructure
  publisher: Dropbox
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开2016工程原文，核对dark launch与迁移时间线。
phase2_conditions:
- 没有同口径采购/运维/利用率成本，使用constrained-decision备用；2016是披露年不是首次承载年。
```

## ENG-151

```yaml
id: ENG-151
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: LastPass2022备份窃取公开更新
cutoff: 2022-12-22获知备份被复制后的风险判断
initial_facts:
- id: I1
  text: 第三方云存储承载生产归档备份
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 备份同时包含未加密元数据和加密vault字段
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 攻击者取得云存储访问与解密相关密钥
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 通告警告离线猜测master password可能解密所窃vault
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 厂商确认备份与vault副本被复制；没有此来源可证全部密码已解密或全部用户安全。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://blog.lastpass.com/posts/notice-of-recent-security-incident
  publisher: LastPass
  published_at: '2022-12-22'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开2022-12-22原始通告，核查备份范围与brute force边界。
phase2_conditions:
- zero knowledge宣传与已确认泄漏分开；不写无来源破解速度或统一PBKDF2设置。
```

## ENG-152

```yaml
id: ENG-152
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: Elasticsearch2.x近实时检索文档
cutoff: 2.x一次写入确认后搜索前
initial_facts:
- id: I1
  text: 新文档先进入内存索引缓冲
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 段可先写入文件系统cache
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: refresh写出并打开新段使其可检索
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: refresh不等于fsync完整持久化commit
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 写入后不能立即搜索是近实时机制的正常结果；可手动refresh但有性能代价。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://www.elastic.co/guide/en/elasticsearch/guide/2.x/near-real-time.html
  publisher: Elastic
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 最初2.4reference路径失败，找到并读取官方2.x Definitive Guide。
phase2_conditions:
- 不要把2010首版行为与2.x混称；固定2.x且说明查询可见性与耐久性不同。
```

## ENG-153

```yaml
id: ENG-153
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: Erlang/OTP22 supervisor重启策略
cutoff: OTP22固定文档一次子进程失败后
initial_facts:
- id: I1
  text: supervisor对子进程指定restart策略
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: intensity和period限制重启强度
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: one_for_one只重启失败子进程
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: one_for_all会终止并重启同组子进程
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 监督树恢复进程运行能力；持久业务状态是否恢复不由该重启策略本身保证。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://www.erlang.org/docs/22/design_principles/sup_princ.html
  publisher: Erlang/OTP
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开OTP22官方监督行为文档，核查策略与强度。
phase2_conditions:
- 1990s—是开放区间，实际anchor为OTP22；不声称1990s已有所有当前选项。
```

## ENG-154

```yaml
id: ENG-154
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: GitHub2021可复用workflow GA
cutoff: 2021-11-29文档示例的跨仓版本治理
initial_facts:
- id: I1
  text: 跨仓复制workflow会分散维护点
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 团队希望集中共用构建与部署步骤
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: jobs可用uses引用另一仓workflow并带@版本
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: workflow_call、inputs/outputs让调用者与被调用者交换数据
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 可复用workflow已GA并报告有大量仓库使用；不代表集中更新自动安全。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://github.blog/news-insights/product-news/github-actions-reusable-workflows-is-generally-available/
  publisher: GitHub
  published_at: '2021-11-29'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开当年GA公告及具体跨仓uses@1示例。
phase2_conditions:
- 不估计维护工时；SHA固定能力还要当年规范证据，不把2022私库共享功能提前。
```

## ENG-155

```yaml
id: ENG-155
status: sourced
reason: 已读直接来源支持事件或artifact，完整Case QA尚未执行。
event: Cloudflare2025-12-05 FL1/WAF解析改动事故
cutoff: 2025-12-05 08:47 UTC配置传播后
initial_facts:
- id: I1
  text: 团队正调整请求体解析buffer以缓解React漏洞
  source_ids:
  - S1
  availability: pre_decision
- id: I2
  text: 有渐进软件部署与快速全局配置两条路径
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 第二项关闭WAF测试工具的全局变更触发FL1规则异常
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: skip路径缺少execute对象导致Lua nil访问
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 09:12回退后流量恢复；受影响需要旧FL1及Managed Ruleset组合。
  source_ids:
  - S1
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
sources:
- id: S1
  url: https://blog.cloudflare.com/5-december-2025-outage/
  publisher: Cloudflare
  published_at: '2025-12-05'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - E1
  - E2
  - outcome
attempts:
- 打开12月5日独立复盘，核查两步变更与具体Lua异常。
phase2_conditions:
- 与11月重复feature文件事故不同；灰度应覆盖配置路径与FL1/规则组合，不提供无来源检测率。
```

## ENG-156

```yaml
id: ENG-156
status: blocked
reason: 当前官方控制器开发约定可读，但未定位2014—2016版本artifact。
event: Kubernetes2014—2016控制器候选
cutoff: 历史版本循环语义待原始快照
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
- 当前官方控制器开发约定可读，但未定位2014—2016版本artifact。
sources:
- id: S1
  url: https://github.com/kubernetes/community/blob/main/contributors/devel/sig-api-machinery/controllers.md
  publisher: Kubernetes
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 尝试kubernetes v1.3.0旧设计路径失败；读取community当前文档，含较新队列API不宜倒推2016。
phase2_conditions:
- 需历史文档/源码commit证明reconcile与重试规则；保持原日期ID不以新教程冒充旧实现。
```

## ENG-157

```yaml
id: ENG-157
status: rejected
reason: 原候选按Phase2重复风险拒绝；真实替换提案为Rust1.52.0构建ICE及1.52.1默认禁用增量。
event: 原Google Blaze2015候选与ENG080复用；替换提案待决
cutoff: 原候选2015；提案Rust2021升级决策另列
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 已知观察、作者归因与维护者推论必须分开；不承诺未核出的数字。
unknowns:
- 未公开内部过程与全部版本细节未知。
- 原候选按Phase2重复风险拒绝；真实替换提案为Rust1.52.0构建ICE及1.52.1默认禁用增量。
sources:
- id: S1
  url: https://blog.rust-lang.org/2021/05/10/Rust-1.52.1/
  publisher: Rust project
  published_at: '2021-05-10'
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 核查ENG080的2015Bazel公告；另打开Rust项目官方1.52.1完整公告。
phase2_conditions:
- 仅提案：保留ENG157日期ID，标题须经显式课程修订映射后换为Rust1.52.1。官方证据：1.52.0新指纹校验暴露既有增量错误；降级旧编译器不会修复潜在误编译；1.52.1默认禁用增量。聚焦升级/关闭优化/降级的发布选择，独立于远端action缓存；尚未写canonical。
replacement_proposal:
  title: Rust 1.52.0 构建 ICE 与 1.52.1 禁用增量（2021）
  decision: 升级到补丁版、停用增量或降级旧版之间如何选择？
  source_ids:
  - S1
  verified_facts:
  - 新指纹校验暴露早已存在的增量误编译风险。
  - 1.52.1默认关闭增量，官方不推荐降级旧版本。
  status: proposal_only_not_canonical_replacement
```
