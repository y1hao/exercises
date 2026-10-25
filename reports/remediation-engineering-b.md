# Phase 3 准入修订：ENG-080—ENG-157

原始核源由研究代理保存；代理额度限制后由root逐项审查保存的事实、范围与引用，补读关键原文。只有eligible才可进入制作，未进入Phase4。

## ENG-080

```yaml
id: ENG-080
decision: reframe
scenario_title: Bazel 2015 Beta：已交付能力与未来缓存承诺
focus: boundary-transfer
subdomain: developer-tooling-build
main_question: Beta公告中的哪些构建能力已交付，哪些缓存收益仍不能作为选型承诺？
expected_output: 一项交付/路线图区分及采用前提
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-080
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: Bazel 2015 Beta：已交付能力与未来缓存承诺
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 保留 ENG-080；区别本地增量与尚未交付的分布式缓存。
```

## ENG-081

```yaml
id: ENG-081
decision: retain
scenario_title: AWS Lambda Extensions API（2020）
focus: boundary-transfer
subdomain: architecture-api
main_question: 扩展观察到调用结束，能否认为整个执行环境已经结束？
expected_output: 一项生命周期保证及超出保证的需求
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-081
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 仅使用生命周期规则；文章现有容器镜像补充不能自动倒推到预览日。
```

## ENG-082

```yaml
id: ENG-082
decision: retain
scenario_title: Cloudflare 2025 年 6 月 Workers KV 故障
focus: prediction-counterfactual
subdomain: reliability-diagnosis
main_question: 底层存储依赖失效波及多个产品；画出依赖图并寻找可切断的级联路径。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-082
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 与其他 Cloudflare 事故分离；初始披露不得先给根因。
```

## ENG-083

```yaml
id: ENG-083
decision: retain
scenario_title: Notion 数据库分片（2021）
focus: constrained-decision
subdomain: data-storage
main_question: 对这一类租户分布，应如何选择数据放置键？
expected_output: 一个放置决定及热点反例
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-083
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 只讨论数据放置键；不能以 UUID 均匀推断租户负载均匀。
```

## ENG-084

```yaml
id: ENG-084
decision: reframe
scenario_title: Open Connect 2012：接入条件与扩展边界
focus: constrained-decision
subdomain: performance-cost
main_question: 首批仅承载约5%流量、支持ISP及交换点交付时，应怎样限定下一批试点的采用条件？
expected_output: 一个试点准入与退回商业CDN的条件
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-084
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: Open Connect 2012：接入条件与扩展边界
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 没有同地区命中率和完整成本表；数量主线改用 planning 的 constrained-decision 备用问题。
```

## ENG-085

```yaml
id: ENG-085
decision: reframe
scenario_title: CockroachDB v20.1：嵌套回滚与事务重试
focus: hypothesis-diagnosis
subdomain: distributed-consistency
main_question: 收到40001后，回滚普通嵌套savepoint能否完成事务重试，重试责任应落在哪里？
expected_output: 一项重试边界及不能替代它的局部回滚
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-085
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: CockroachDB v20.1：嵌套回滚与事务重试
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - Phase 4 必须明确读写集合为协议推演，不能假造真实事务日志。
```

## ENG-086

```yaml
id: ENG-086
decision: reframe
scenario_title: Google Piper/Rosie 跨团队变更治理（2016论文）
focus: evidence-selection
subdomain: developer-tooling-build
main_question: 这次跨团队兼容变更是否值得进入Rosie批量流程，审查成本如何设边界？
expected_output: 一个治理决定与自治成本
out_of_scope: 不做单仓多仓的全面辩论
reason: 取得带作者、DOI与逐页正文的原论文镜像，保留Google Research元数据作身份复核；只聚焦Rosie治理而非泛论单仓。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-086
  status: sourced
  reason: 取得带作者、DOI与逐页正文的原论文镜像，保留Google Research元数据作身份复核；只聚焦Rosie治理而非泛论单仓。
  event: Google Piper/Rosie 跨团队变更治理（2016论文）
  cutoff: 2016-07论文所记流程冻结；在下一次大规模兼容变更提交前
  initial_facts:
  - id: I1
    text: 单一代码库允许跨项目修改，代码所有权仍按目录分派。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: Rosie会把大补丁拆分成项目级补丁。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 拆分后的补丁需独立测试和代码审查后才提交。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: 论文记录2013新增大规模变更审查流程，衡量收益、审查者时间及仓库变动成本。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 论文记录治理引入后2013至2014 Rosie提交量下降；这是流程观察，不能推出质量必然提升。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://www.slideshare.net/slideshow/why-google-stores-billions-of-lines-of-code-in-a-single-repository-252346710/252346710
    publisher: Rachel Potvin / Josh Levenberg，CACM原文逐页镜像
    published_at: '2016-07-01'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
    access_note: 原始作者论文的第三方逐页镜像；不是镜像站编辑论述。Google/ACM原下载403已记录。
  - id: S2
    url: https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/
    publisher: Google Research
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports: []
  attempts:
  - 官方论文页可读；ACM 下载链接与 archive/45424.pdf 均无法读取正文。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
```

## ENG-087

```yaml
id: ENG-087
decision: reframe
scenario_title: React RFC 0188：序列化跨组件边界
focus: boundary-transfer
subdomain: architecture-api
main_question: 服务器组件数据和客户端交互逻辑跨边界时，序列化限制排除了哪类传递？
expected_output: 一项可传递契约及不能据此宣称的能力
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-087
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: React RFC 0188：序列化跨组件边界
  cutoff: 2026-10-25本轮已读取的公开工件快照，评估其明确契约；不声称候选首发年份即含这些语义。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 范围保持单次跨边界传递；Phase 4 固定 RFC commit，不能混用 2020 命名与新指令。
```

## ENG-088

```yaml
id: ENG-088
decision: reframe
scenario_title: io_uring 设计文档：共享队列与每次I/O开销
focus: causal-modeling
subdomain: runtime-concurrency
main_question: 共享SQ/CQ可以消除哪部分提交和完成开销，为什么不能据此保证任意小I/O负载加速？
expected_output: 一个开销路径与收益适用条件
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-088
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: io_uring 设计文档：共享队列与每次I/O开销
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 尚无本题同口径安全评估；Phase 4 不把性能收益当安全保证，不引用后续版本数据。
```

## ENG-089

```yaml
id: ENG-089
decision: retain
scenario_title: Rowhammer（2014）
focus: boundary-transfer
subdomain: security-isolation
main_question: 高频内存访问可扰动邻近位，识别软件访问权限与物理效应之间的边界。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-089
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不得将 2015 提权利用当成 2014 已知结果。
```

## ENG-090

```yaml
id: ENG-090
decision: retain
scenario_title: GitLab 2017 年生产数据库误删除
focus: constrained-decision
subdomain: reliability-diagnosis
main_question: 恢复备份发现多层缺陷；根据恢复演练证据决定止损与重建路线。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-090
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 事前仅提供已观察到的恢复检查结果；不能提前泄露最终恢复路径。
```

## ENG-091

```yaml
id: ENG-091
decision: retain
scenario_title: Vitess 分片治理（2010—）
focus: constrained-decision
subdomain: data-storage
main_question: 为这一类写入和查询，所选 shard key 的代价是否可接受？
expected_output: 一个键选择及跨 shard 反例
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-091
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 缺实际租户工作负载；可做已发布 artifact 的路由推演，不能编造迁移史。
```

## ENG-092

```yaml
id: ENG-092
decision: retain
scenario_title: ZooKeeper Zab（2011）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: 旧 leader 的未提交 proposal 在恢复后会怎样处理？
expected_output: 一条 proposal 命运预测及安全依据
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-092
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 必须具体列出已接受与已提交状态，保持与 Raft 题的区分。
```

## ENG-093

```yaml
id: ENG-093
decision: retain
scenario_title: GitHub Codespaces 发布（2021）
focus: constrained-decision
subdomain: developer-tooling-build
main_question: 从本地环境转向云端开发，判断开发环境可重现性与网络依赖的取舍。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-093
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 迁移结果为团队报告；不可声称没有网络依赖或推断所有仓库适用。
```

## ENG-094

```yaml
id: ENG-094
decision: retain
scenario_title: gRPC Streaming API 设计（2015）
focus: boundary-transfer
subdomain: architecture-api
main_question: 用一项需增量返回和流量控制的业务分析 unary 与 streaming 对错误语义的影响。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-094
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 真实 API artifact 可作边界推演，业务负载只能标为教学示例。
```

## ENG-095

```yaml
id: ENG-095
decision: retain
scenario_title: Java G1 GC 默认化（2017）
focus: prediction-counterfactual
subdomain: runtime-concurrency
main_question: 暂停预算改变后，回收选择可能怎样变化？
expected_output: 一个区域回收预测及吞吐边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-095
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 仅依据 JDK9 行为，不以当前 JDK 默认策略倒推 2017 所有机器。
```

## ENG-096

```yaml
id: ENG-096
decision: reframe
scenario_title: Twitter Timelines at Scale：写扇出与读取合并边界（2012演讲工件）
focus: constrained-decision
subdomain: performance-cost
main_question: 面对扇出延迟，应把哪类发布留在写时物化、哪类改成读时合并，必须补看什么负载证据？
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不扩写整家公司或系统史，不添加未公开指标、日志和决策者观点
reason: 取得原幻灯片可读文本；删掉未经直接核实的明星混合方案落地结论，收敛成工件快照上的单次路径取舍。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-096
  status: sourced
  reason: 取得原幻灯片可读文本；删掉未经直接核实的明星混合方案落地结论，收敛成工件快照上的单次路径取舍。
  event: Twitter Timelines at Scale：写扇出与读取合并边界（2012演讲工件）
  cutoff: QCon SF 2012幻灯片架构快照；评估下一类大关注者发布路径
  initial_facts:
  - id: I1
    text: 讲者Raffi Krikorian将home timeline读取列为高频负载。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 幻灯片给出写入扇出到接收者时间线缓存的路径。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 缓存使用Redis原生列表，RPUSHX仅向已缓存的时间线添加。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: 幻灯片报告向100万接收者交付的p50约3.5秒；这是该演讲负载观察，不是所有请求保证。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 可揭晓的真实工件是写时预物化并缓存时间线的架构；不宣称已证实明星账号混合扇出已上线。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://speakerdeck.com/angelbotto/raffi-krikorian-twitter-timelines-at-scale
    publisher: Raffi Krikorian 原演讲幻灯片镜像
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
  - 搜索演讲与幻灯片；打开 InfoQ 仅有视频播放器、概要和讲者信息；搜索到转述未当作验证。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
```

## ENG-097

```yaml
id: ENG-097
decision: retain
scenario_title: Google 2020 年身份验证故障
focus: hypothesis-diagnosis
subdomain: reliability-diagnosis
main_question: 共享身份服务资源问题导致多产品失效；寻找能区分控制面与业务服务的观测。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-097
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 根因与恢复动作只作隐藏证据，按实际可见状态分轮披露。
```

## ENG-098

```yaml
id: ENG-098
decision: retain
scenario_title: runC 容器逃逸 CVE-2019-5736
focus: causal-modeling
subdomain: security-isolation
main_question: 恶意容器覆写运行时二进制的条件是什么；重建容器边界失败链。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-098
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 只保留 2019 CVE 链条；不要混入其他 runc FD 漏洞。
```

## ENG-099

```yaml
id: ENG-099
decision: reframe
scenario_title: FoundationDB 8.0 文档：读写冲突集合
focus: evidence-selection
subdomain: distributed-consistency
main_question: 给定同一文档的原子计数与reset示例，哪种读写交叠需要显式读冲突范围？
expected_output: 一组冲突预测和一个不冲突对照
out_of_scope: 不同时展开所有事务层组件
reason: 明确冻结来源版本；不倒推候选初始年份。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-099
  status: sourced
  reason: 明确冻结来源版本；不倒推候选初始年份。
  event: FoundationDB 8.0 文档：读写冲突集合
  cutoff: 2026-10-25读取的8.0指南conflict ranges机制快照；不是2013发布行为
  initial_facts:
  - id: I1
    text: 默认事务目标为strict serializability。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 指南说明事务会跟踪读写键范围。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 先提交事务写入后提交事务读取的值时，后者冲突失败并通常重试。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: snapshot read不添加read conflict range；atomic operations也不添加普通读冲突范围。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 文档明确的冲突规则可核对一组事务是否重试；不能把snapshot read的低冲突率当作相同隔离保证。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://apple.github.io/foundationdb/developer-guide.html
    publisher: FoundationDB
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
  - 搜索 2013 事务资料并打开官方指南；看到当前 8.0 标记和 conflict ranges 部分。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
```

## ENG-100

```yaml
id: ENG-100
decision: retain
scenario_title: Microsoft TypeScript 增量构建（2018—2020）
focus: prediction-counterfactual
subdomain: developer-tooling-build
main_question: 哪些下游项目需要重新检查，哪些不必？
expected_output: 一张受影响项目集合
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-100
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 只讨论依赖失效范围；Phase4 需固定版本及明确声明签名示例为演示代码。
```

## ENG-101

```yaml
id: ENG-101
decision: retain
scenario_title: Uber Schemaless（2016）
focus: constrained-decision
subdomain: data-storage
main_question: 这类字段变化更适合弱 schema 存储还是关系约束？
expected_output: 一个模型选择与迁移代价
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-101
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不把弱 schema 等同无数据契约；只比较一类字段变化。
```

## ENG-102

```yaml
id: ENG-102
decision: retain
scenario_title: Git LFS 的外置大文件模型（2015）
focus: boundary-transfer
subdomain: architecture-api
main_question: 当版本控制面对二进制文件膨胀时，推演指针对象和远端存储改变了什么契约。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-102
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不使用当前价格与配额；远端缺失的后果是维护者机制推断。
```

## ENG-103

```yaml
id: ENG-103
decision: retain
scenario_title: Python asyncio 引入（2014）
focus: prediction-counterfactual
subdomain: runtime-concurrency
main_question: 一个任务中的同步等待会如何影响其他协作任务？
expected_output: 一条执行时序与可观察延迟预测
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-103
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - Phase4 的最小代码必须标为规范演示；不混用后续 async/await 首发年代。
```

## ENG-104

```yaml
id: ENG-104
decision: retain
scenario_title: Cloudflare 2025 年 11 月 Bot Management 故障
focus: causal-modeling
subdomain: reliability-diagnosis
main_question: 一项配置数据变化可能通过哪条依赖路径影响请求？
expected_output: 一条待证实的传播链及最弱证据环节
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-104
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 严格区别 ENG155 12月 WAF 解析事故；根因不进入 opening。
```

## ENG-105

```yaml
id: ENG-105
decision: retain
scenario_title: Google Chubby 锁服务（2006）
focus: boundary-transfer
subdomain: distributed-consistency
main_question: 面对 lease、故障和客户端缓存，判断分布式锁能保证哪些性质、不能保证哪些性质。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-105
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 保留 lease 与 fencing 单一边界，不泛讲所有共识协议。
```

## ENG-106

```yaml
id: ENG-106
decision: retain
scenario_title: Language Server Protocol（2016）
focus: boundary-transfer
subdomain: developer-tooling-build
main_question: 一套语言能力服务多个编辑器，评估标准化协议对创新与扩展能力的影响。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-106
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 协议未自动保证各客户端功能完整一致；未来实现承诺不当成已完成。
```

## ENG-107

```yaml
id: ENG-107
decision: retain
scenario_title: Equifax Apache Struts 漏洞（2017）
focus: evidence-selection
subdomain: security-isolation
main_question: 已知漏洞、补丁和资产清单脱节；判断组织层面的可利用窗口与防线优先级。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-107
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - GAO 是直接调查来源；对 Equifax自述归因需保持归属，不用后见之明指责单个人。
```

## ENG-108

```yaml
id: ENG-108
decision: reframe
scenario_title: The Tail at Scale：延迟对冲的工作量与收益（2013）
focus: quantitative-calibration
subdomain: performance-cost
main_question: 已披露基准的p99.9改善倍数与额外请求比例各是多少，为什么两者不能直接换算成相同百分比的CPU成本？
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不扩写整家公司或系统史，不添加未公开指标、日志和决策者观点
reason: 取得作者站点原论文全文；原数量输入现可直接追溯，缩小为已公布基准比较，保留数量动作。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-108
  status: sourced
  reason: 取得作者站点原论文全文；原数量输入现可直接追溯，缩小为已公布基准比较，保留数量动作。
  event: The Tail at Scale：延迟对冲的工作量与收益（2013）
  cutoff: 2013-02论文公布的BigTable基准快照；评估该实验已披露结果的数量边界
  initial_facts:
  - id: I1
    text: 实验一次读取1000个键，分布在100台服务器。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 该实验无对冲时整次读取p99.9为1800毫秒。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 延迟10毫秒发起对冲后，实验p99.9为74毫秒。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: 额外请求仅约2%；作者另说明在p95之后对冲约把请求增加限制在5%。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 实测案例显示尾延迟约下降24.3倍而请求量增加2%；该结论局限于给出的负载及副本干扰相关性。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://barroso.org/publications/TheTailAtScale.pdf
    publisher: Jeffrey Dean / Luiz André Barroso
    published_at: '2013-02-01'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - Google 官方元数据页可读；archive/40801.pdf 失败；CACM下载与文章页返回403。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
quantitative_inputs:
- name: keys
  value: 1000
  unit: keys
  source_ids:
  - S1
- name: servers
  value: 100
  unit: servers
  source_ids:
  - S1
- name: baseline_p999
  value: 1800
  unit: ms
  source_ids:
  - S1
- name: hedged_p999
  value: 74
  unit: ms
  source_ids:
  - S1
- name: hedge_delay
  value: 10
  unit: ms
  source_ids:
  - S1
- name: extra_requests
  value: 2
  unit: percent
  source_ids:
  - S1
```

## ENG-109

```yaml
id: ENG-109
decision: retain
scenario_title: OpenTelemetry 规范统一（2019）
focus: boundary-transfer
subdomain: architecture-api
main_question: 统一这项 API 能减少哪种迁移依赖，又不能减少哪种？
expected_output: 一个可迁移边界判断
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-109
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - API 统一和导出后端分离；未读完整首版规范前不声称具体 exporter 保证。
```

## ENG-110

```yaml
id: ENG-110
decision: retain
scenario_title: Discord 2022消息迁移：节点数与原始磁盘容量
focus: quantitative-calibration
subdomain: data-storage
main_question: 177台平均4TB到72台9TB后，节点数和原始磁盘容量分别变化多少；为什么不是相同百分比的成本节省？
expected_output: 两项归一化计算及不能推出的总成本/数据库独立因果贡献
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 原成本问题缺总成本账，正式改成作者公开的节点/原始磁盘容量比较，保留数量训练。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-110
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: Discord 2022消息迁移：节点数与原始磁盘容量
  cutoff: 2023-03-06文章发布后的2022年5月迁移结果比较；不将事后改善放入迁移前初始信息。
  initial_facts:
  - id: I1
    text: 旧Cassandra集群有177节点，每节点平均4TB磁盘。
    source_ids:
    - S1
    availability: pre_decision
  - id: I2
    text: 新ScyllaDB集群有72节点，每节点9TB磁盘。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 团队还引入了数据服务、request coalescing与一致散列路由，数据库引擎并非唯一变化。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 历史消息读取p99由40—125ms区间降到15ms；未给出各配置完整硬件及运维成本。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 作者报告2022年5月迁移完成并在随后生产运行改善延迟和运维；原始容量由708TB到648TB可透明推导，不能当作可用数据量或美元成本。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  - root本轮重新打开Discord全文Several Months Later段，确认177/72节点、4/9TB与p99，原文明确2022年5月切换。
  phase2_conditions:
  - 没有完整同口径总成本和工作量，采用 constrained-decision 备用；限2022消息库一次迁移。
quantitative_inputs:
- name: old_nodes
  value: 177
  unit: nodes
  source_ids:
  - S1
- name: old_disk_per_node
  value: 4
  unit: TB average
  source_ids:
  - S1
- name: new_nodes
  value: 72
  unit: nodes
  source_ids:
  - S1
- name: new_disk_per_node
  value: 9
  unit: TB
  source_ids:
  - S1
```

## ENG-111

```yaml
id: ENG-111
decision: retain
scenario_title: Cloudflare 2026 年 2 月 BYOIP 路由撤销
focus: prediction-counterfactual
subdomain: reliability-diagnosis
main_question: 若一项前缀被撤销，不同外部观察点会呈现什么症状？
expected_output: 一条控制面操作到外部症状的预测
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-111
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不能和2022网络事故混为同一事件；一条邻居统计不等于全互联网观测。
```

## ENG-112

```yaml
id: ENG-112
decision: retain
scenario_title: Node.js libuv 事件循环（2009—）
focus: causal-modeling
subdomain: runtime-concurrency
main_question: 回调延迟来自事件循环等待还是线程池等待？
expected_output: 一条请求执行链及可区分的观察
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-112
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 需要进一步给最小请求类型与回调执行位置；不得编造线上指标。
```

## ENG-113

```yaml
id: ENG-113
decision: retain
scenario_title: etcd Raft 故障恢复（2015—2018）
focus: constrained-decision
subdomain: distributed-consistency
main_question: 应继续成员替换，还是进入灾难恢复流程？
expected_output: 一个恢复选择及数据一致性前提
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-113
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 保持2015—2018候选版本范围；不能自动承诺恢复所有未快照写入。
```

## ENG-114

```yaml
id: ENG-114
decision: reframe
scenario_title: Gitpod Classic：工作区快照分享的信任边界
focus: boundary-transfer
subdomain: developer-tooling-build
main_question: 快照链接可复现场景时，哪些敏感状态不会因跨账户重建而自动消失？
expected_output: 一项可复用范围及凭据暴露应对边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-114
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: Gitpod Classic：工作区快照分享的信任边界
  cutoff: 2026-10-25本轮已读取的公开工件快照，评估其明确契约；不声称候选首发年份即含这些语义。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 2020—开放区间内可保留Classic artifact，Phase4必须固定文档/源码版本和snapshot内容，不能断言2020凭据处理。
```

## ENG-115

```yaml
id: ENG-115
decision: retain
scenario_title: XZ Utils 后门事件（2024）
focus: evidence-selection
subdomain: security-isolation
main_question: 开源维护与构建脚本被渗透；从源码审查到发布工件判断可检测点。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-115
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 事实保持发现者当时已披露范围；攻击者组织身份未知。
```

## ENG-116

```yaml
id: ENG-116
decision: reframe
scenario_title: Envoy xDS 协议：ACK与实际生效
focus: boundary-transfer
subdomain: architecture-api
main_question: 客户端ACK一项配置后，控制面对已应用和业务健康分别能承诺什么？
expected_output: 一项ACK语义及仍须观察的生效条件
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-116
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: Envoy xDS 协议：ACK与实际生效
  cutoff: 2026-10-25本轮已读取的公开工件快照，评估其明确契约；不声称候选首发年份即含这些语义。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 开放年代候选可锚当前artifact；Phase4须锁commit，不能混称为2017原版。
```

## ENG-117

```yaml
id: ENG-117
decision: replace
scenario_title: RocksDB Ribbon Filter：内存与构建CPU权衡（2021）
focus: quantitative-calibration
subdomain: performance-cost
main_question: 在作者相同误报率模型下，每key省多少过滤器内存、增加多少构建CPU；哪些驻留和寿命条件会破坏这项收益？
expected_output: 一项成本拆分与可核实数量关系
out_of_scope: 只比较作者披露的Ribbon与Bloom空间、构建代价；不泛谈存储成本或宣称已定位SSD优化事故
reason: 原ZippyDB单次SSD成本优化未获独立材料，正式替换为同属性能成本的独立Ribbon机制；全年rg未发现另一Ribbon案例。来源模型参数按作者假设标注，不冒充实测业务成本。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-117
  status: sourced
  reason: 原ZippyDB单次SSD成本优化未获独立材料，正式替换为同属性能成本的独立Ribbon机制；全年rg未发现另一Ribbon案例。来源模型参数按作者假设标注，不冒充实测业务成本。
  event: RocksDB Ribbon Filter：内存与构建CPU权衡（2021）
  cutoff: 2021-12-29官方文章的相同误报率filter比较；不是ZippyDB生产成本事件
  initial_facts:
  - id: I1
    text: RocksDB 6.15起提供Ribbon作为Bloom的可选替代。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 文章模型在相同误报率下使用Bloom约10、Ribbon约7 bits/key。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 正文报告Ribbon约省30%空间、构建CPU约3至4倍；具体模型给出每key构建32与140ns。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: 构建临时内存约230与75 bits/key；冷过滤器不全驻留时，驻留内存收益会变弱。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 真实工件支持省约3 bits/key和约4.375倍模型构建CPU的比较；这不是SSD或生产总成本下降幅度。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://rocksdb.org/blog/2021/12/29/ribbon-filter.html
    publisher: RocksDB / Peter Dillinger
    published_at: '2021-12-29'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 分别检索ZippyDB+SSD+cost、Meta官方ZippyDB；打开2021原文，SSD未命中；2026新闻不作2010s证据。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
quantitative_inputs:
- name: bloom_filter
  value: 10
  unit: bits/key
  source_ids:
  - S1
- name: ribbon_filter
  value: 7
  unit: bits/key
  source_ids:
  - S1
- name: bloom_construct
  value: 32
  unit: ns/key in author model
  source_ids:
  - S1
- name: ribbon_construct
  value: 140
  unit: ns/key in author model
  source_ids:
  - S1
- name: bloom_temporary
  value: 75
  unit: bits/key approximately
  source_ids:
  - S1
- name: ribbon_temporary
  value: 230
  unit: bits/key approximately
  source_ids:
  - S1
```

## ENG-118

```yaml
id: ENG-118
decision: retain
scenario_title: Knight Capital 2012 年部署事故
focus: constrained-decision
subdomain: reliability-diagnosis
main_question: 部分服务器部署状态不一致触发异常交易；判断 release 原子性与 Kill Switch 的作用。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-118
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: Knight Capital2012部署事故SEC调查
  cutoff: 2012-08-01市场开盘前后的发布检查
  initial_facts:
  - id: I1
    text: SMARS部署到8台服务器
    source_ids:
    - S1
    availability: pre_decision
  - id: I3
    text: SMARS是为客户股权订单提供自动路由的系统。
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
    - I3
  attempts:
  - 打开SEC行政处罚原文，核查漏部署、控制缺陷与损失。
  - root本轮重新打开SEC 34-70694第一页，核对自动路由对象；未把漏部署节点先给开场。
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不能将未部署节点信息当作所有操作者当时已知；初始材料只给发布流程观察。
```

## ENG-119

```yaml
id: ENG-119
decision: retain
scenario_title: Google F1 数据库（2013）
focus: boundary-transfer
subdomain: data-storage
main_question: 这项查询责任落在 F1 哪层，底层事务保证又到哪里？
expected_output: 一个查询与事务责任边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-119
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - Phase4按论文层次限定单查询责任；不将F1等同Spanner产品。
```

## ENG-120

```yaml
id: ENG-120
decision: reframe
scenario_title: NATS 2.2 JetStream：窗口去重与业务效果
focus: hypothesis-diagnosis
subdomain: distributed-consistency
main_question: 业务处理已完成但ack丢失，2.2的窗口去重声明能否证明外部副作用只发生一次？
expected_output: 一个投递保证与业务效果边界
out_of_scope: 不提前加入后续版本功能
reason: 明确冻结来源版本；不倒推候选初始年份。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-120
  status: sourced
  reason: 明确冻结来源版本；不倒推候选初始年份。
  event: NATS 2.2 JetStream：窗口去重与业务效果
  cutoff: NATS 2.2发布说明快照；移除未经核实的2020首发时点
  initial_facts:
  - id: I1
    text: JetStream在NATS server内提供流持久化。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 持久流通过consumer投递或重放消息。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 2.2发布说明承诺至少一次投递。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: 同一发布说明限定exactly once为within a window，不是任意时长外部业务副作用。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 可核结果是2.2交付了持久流及有窗口限制的去重契约；外部数据库写入并未被该声明自动纳入。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://github.com/nats-io/nats.docs/blob/master/release_notes/whats_new_22.md
    publisher: NATS
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
  - 猜测JetStream发布URL失败；搜索到2.2正式发布资料和2019技术预览，打开官方2.2 release notes。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
```

## ENG-121

```yaml
id: ENG-121
decision: retain
scenario_title: Pants v2 构建系统（2020—）
focus: constrained-decision
subdomain: developer-tooling-build
main_question: 自动推导漏掉这项依赖时，应怎样退回显式声明？
expected_output: 一个回退决定及正确性判据
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-121
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 只讨论漏推断时的显式退路；性能百分比是作者报告且不作通用预测。
```

## ENG-122

```yaml
id: ENG-122
decision: reframe
scenario_title: Akka 2.4.20 PersistentActor：恢复与下一条消息
focus: causal-modeling
subdomain: runtime-concurrency
main_question: 重启后下一条消息能看到哪些已持久化状态，哪些未持久化状态无法据此保证？
expected_output: 一条消息与状态恢复时序
out_of_scope: 不合并不同模式的顺序与持久性保证
reason: 明确冻结来源版本；不倒推候选初始年份。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-122
  status: sourced
  reason: 明确冻结来源版本；不倒推候选初始年份。
  event: Akka 2.4.20 PersistentActor：恢复与下一条消息
  cutoff: 2017-08-10 Akka 2.4.20 Java文档快照；一次持久化actor重启前
  initial_facts:
  - id: I1
    text: 同一实体的persistenceId在actor不同生命周期保持稳定。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 事件被持久化后才用来修改事件溯源actor的状态。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: PersistentActor启动或重启会重放已入journal的事件。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: 恢复期间新消息被stash，恢复完成后才交给actor处理；重放消息sender为deadLetters。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 文档的恢复完成顺序可核对下一条消息看到的状态；未持久化状态或外部副作用不因此自动恢复。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://doc.akka.io/docs/akka/2.4/AkkaJava.pdf
    publisher: Lightbend
    published_at: '2017-08-10'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 尝试官方2.5 actors、2.5/2.6 supervision及v2.5.32 GitHub文档路径均失败；不以常识填补。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
```

## ENG-123

```yaml
id: ENG-123
decision: retain
scenario_title: OpenAPI 3.0 规格演进（2017）
focus: constrained-decision
subdomain: architecture-api
main_question: 先写契约能否减少这次变更的接口分歧？
expected_output: 一个协作选择及仍需运行验证的部分
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-123
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不把先写契约当作已证因果成功；固定一次接口变更，示例须标明。
```

## ENG-124

```yaml
id: ENG-124
decision: retain
scenario_title: Kubernetes CVE-2019-11253
focus: causal-modeling
subdomain: security-isolation
main_question: 通过 YAML/JSON 解码路径引发资源耗尽，分析 API 输入验证与控制面 DoS 风险。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-124
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 区分原始2019-09-27 issue时间与后续编辑的CVE通告；不把所有匿名用户都视为获授权。
```

## ENG-125

```yaml
id: ENG-125
decision: retain
scenario_title: Cloudflare 2019 年 WAF 正则事故
focus: evidence-selection
subdomain: reliability-diagnosis
main_question: 新规则使 CPU 使用急剧上升；区分部署、回滚与性能预验证机制。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-125
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不复用2025两起事故根因；单一主线是规则预验证与回退证据。
```

## ENG-126

```yaml
id: ENG-126
decision: reframe
scenario_title: TiKV Deep Dive：Percolator primary提交后的secondary锁
focus: hypothesis-diagnosis
subdomain: distributed-consistency
main_question: primary已提交而secondary还留锁时，应寻找什么状态区分等待、提交清锁和回滚？
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不扩写整家公司或系统史，不添加未公开指标、日志和决策者观点
reason: 明确冻结来源版本；不倒推候选初始年份。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-126
  status: sourced
  reason: 明确冻结来源版本；不倒推候选初始年份。
  event: TiKV Deep Dive：Percolator primary提交后的secondary锁
  cutoff: 2026-10-25读取的官方Percolator教学算法快照；不声明2016所有实现语义
  initial_facts:
  - id: I1
    text: 算法把事务分为prewrite和commit。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: secondary锁记录primary锁所在位置。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: primary提交形成事务提交节点，secondary提交失败不改变已经提交的事务。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: 读遇到较早事务的锁时需退避处理；恢复可依据primary的状态决定锁的提交或回滚。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 可核对的是官方算法图解中的primary决定和secondary锁处理；不是某次生产故障或现代优化快路径。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://tikv.github.io/deep-dive-tikv/distributed-transaction/percolator.html
    publisher: TiKV
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
  - 打开TiKV Percolator文档读完整prewrite/commit/crash章节；2017 PingCAP历史文章读取失败。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
```

## ENG-127

```yaml
id: ENG-127
decision: retain
scenario_title: Buck2 引入 Dice 增量引擎（2023）
focus: causal-modeling
subdomain: developer-tooling-build
main_question: Meta 重写构建工具时，研究细粒度依赖追踪如何改变增量计算与正确性。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-127
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - DICE源码文档是滚动版本，具体细粒度失效规则要锁2023commit，不混入modern DICE重写。
```

## ENG-128

```yaml
id: ENG-128
decision: reframe
scenario_title: TimescaleDB Hypertable：范围查询与chunk排除（文档快照）
focus: prediction-counterfactual
subdomain: data-storage
main_question: 同一未压缩hypertable中，查询时间窗口跨过更多chunk边界后，哪些chunk仍可被排除？
expected_output: 一个候选chunk集合的定性变化及不能据此推算扫描行数的边界
out_of_scope: 不为历史主线发明数据规模
reason: 明确冻结来源版本；不倒推候选初始年份。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-128
  status: sourced
  reason: 明确冻结来源版本；不倒推候选初始年份。
  event: TimescaleDB Hypertable：范围查询与chunk排除（文档快照）
  cutoff: 2026-10-25读取的官方architecture.md机制快照，限定未压缩单节点chunk
  initial_facts:
  - id: I1
    text: hypertable内部被拆成对应时间范围和分区键范围的chunk。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: chunk底层是PostgreSQL标准表，范围互不重叠。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 查询规划器可据非重叠范围排除无需访问的chunk。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: chunk可整体丢弃以落实保留策略，无需逐行删除。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 文档支持范围扩大时候选chunk集合的变化；无真实负载数据时不能报告扫描行数或加速倍数。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://github.com/timescale/docs.timescale.com-content/blob/master/introduction/architecture.md
    publisher: Timescale
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
  - 检索2017架构、尝试原论文和TigerData重定向均失败；0.5.0 README路径读取失败；当前说明只作后续研究入口。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
```

## ENG-129

```yaml
id: ENG-129
decision: retain
scenario_title: JavaScript Promise 微任务队列（2015）
focus: prediction-counterfactual
subdomain: runtime-concurrency
main_question: 这些同步任务、微任务和 timer 回调按什么次序执行？
expected_output: 一条执行序列及饥饿边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-129
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 宿主固定浏览器，区分规范期望和真实实现观察；不混Node nextTick。
```

## ENG-130

```yaml
id: ENG-130
decision: reframe
scenario_title: YouTube 2011 Hydra：等待与并行化的边界
focus: constrained-decision
subdomain: performance-cost
main_question: 上传和处理重叠、再分块并行时，应优先验证哪一段等待，为什么没有总成本账就不能决定全面采用？
expected_output: 一个延迟验证优先级与采用条件
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-130
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: YouTube 2011 Hydra：等待与并行化的边界
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 源支持降低等待的设计，若坚持具体队列优先级需补资料；不能编造预算或优先队列。
```

## ENG-131

```yaml
id: ENG-131
decision: retain
scenario_title: Bazel Starlark 扩展接口（2017—2020）
focus: boundary-transfer
subdomain: architecture-api
main_question: 这个扩展应通过稳定接口提供，还是保留为内部能力？
expected_output: 一个接口边界及不兼容风险
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-131
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不能把可用内部实现自动当稳定API；Phase4围绕单项扩展责任。
```

## ENG-132

```yaml
id: ENG-132
decision: retain
scenario_title: GitHub 2018 年 10 月数据库故障
focus: constrained-decision
subdomain: reliability-diagnosis
main_question: 网络分区导致数据库复制与服务状态异常；在数据完整性与恢复速度间作取舍。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-132
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 核源URL改指详细复盘；恢复速度与一致性围绕单一决策。
```

## ENG-133

```yaml
id: ENG-133
decision: retain
scenario_title: Cassandra 无主写入（2010—2015）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: 在这组 quorum 配置下，读取可能得到哪个版本？
expected_output: 一条写入与读取时序预测
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-133
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 版本落在2010—2015范围；Phase4需单独注明并发写与时间戳前提。
```

## ENG-134

```yaml
id: ENG-134
decision: retain
scenario_title: Gradle Configuration Cache（2020—）
focus: evidence-selection
subdomain: developer-tooling-build
main_question: 什么检查最能证明该配置结果不适合复用？
expected_output: 一个检查动作与可反驳的缓存假说
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-134
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 区别配置缓存与构建action输出缓存；只核验一次不适合复用的配置。
```

## ENG-135

```yaml
id: ENG-135
decision: retain
scenario_title: npm event-stream 依赖劫持（2018）
focus: evidence-selection
subdomain: security-isolation
main_question: 维护者交接导致恶意依赖代码进入发布链；如何界定依赖信任和审查成本。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-135
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不推断所有安装者都泄露私钥；源中的Copay确认属明确转述。
```

## ENG-136

```yaml
id: ENG-136
decision: retain
scenario_title: Apache Druid 实时摄取（2011—）
focus: prediction-counterfactual
subdomain: data-storage
main_question: 一条新事件何时进入可查询结果，转换会牺牲什么？
expected_output: 一个新鲜度预测及聚合边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-136
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 采用2014 artifact，不捏造2011事故；聚合/更新能力的损失要按论文而非当前Druid推断。
```

## ENG-137

```yaml
id: ENG-137
decision: reframe
scenario_title: Linux man-pages epoll：interest/ready列表与通知边界
focus: prediction-counterfactual
subdomain: runtime-concurrency
main_question: 就绪连接占比升高时，ready集合相对于interest集合的稀疏优势怎样变化；何种ET读取方式会使此推断失效？
expected_output: 一个定性相对收益方向与一项ET使用边界；不报告无基准的复杂度常数
out_of_scope: ET 漏读只作边界，不再成为第二主任务
reason: 明确冻结来源版本；不倒推候选初始年份。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-137
  status: sourced
  reason: 明确冻结来源版本；不倒推候选初始年份。
  event: Linux man-pages epoll：interest/ready列表与通知边界
  cutoff: 2026-10-25读取的Linux man-pages 6.15 epoll(7)快照；不倒推2002基准
  initial_facts:
  - id: I1
    text: epoll将注册兴趣集合保存在内核interest list。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: ready list动态保存当前可I/O的文件描述符引用。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: epoll_wait取可用事件，未就绪时可阻塞。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: ET模式必须非阻塞并读写到EAGAIN再等待；只读掉部分缓冲可能无限等待。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 接口工件可核对就绪集合变化和ET残留数据反例；不能据此给出任意负载select/poll的实测加速比。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://man7.org/linux/man-pages/man7/epoll.7.html
    publisher: Linux man-pages project
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
  - 读取man7手册；检索作者2001/2002 nio-improve原页并尝试打开，返回502；不据当前接口倒推旧版复杂度。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
```

## ENG-138

```yaml
id: ENG-138
decision: retain
scenario_title: Stripe Idempotency-Key API 设计（2017）
focus: prediction-counterfactual
subdomain: architecture-api
main_question: 请求超时后，用同一个 key 重试可以期待什么结果？
expected_output: 一条重试结果预测及 key 的边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-138
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 文章未核足key保留期；Phase4补当时文档，不把当前24小时策略倒推到2017。
```

## ENG-139

```yaml
id: ENG-139
decision: retain
scenario_title: Cloudflare 2022 年 6 月网络中断
focus: hypothesis-diagnosis
subdomain: reliability-diagnosis
main_question: 一次路由配置变更影响多个机房；依据流量路径识别 blast radius 与回滚优先级。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-139
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 与2026 BYOIP撤销区分；不能仅按地点数估算请求影响。
```

## ENG-140

```yaml
id: ENG-140
decision: reframe
scenario_title: Consul 跨数据中心：成员发现与Raft保证（机制快照）
focus: boundary-transfer
subdomain: distributed-consistency
main_question: 看到WAN成员发现已传播后，还需哪个请求路径和一致性证据才能承诺远端数据已提交？
expected_output: 一个跨区保证边界
out_of_scope: 不把成员发现和数据共识当同一承诺
reason: 明确冻结来源版本；不倒推候选初始年份。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-140
  status: sourced
  reason: 明确冻结来源版本；不倒推候选初始年份。
  event: Consul 跨数据中心：成员发现与Raft保证（机制快照）
  cutoff: 2026-10-25官方架构/概念文档快照；不倒推2015实现
  initial_facts:
  - id: I1
    text: Consul server用Raft维护注册服务等状态。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 官方概念文档将gossip用于成员发现、故障探测和事件广播。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 单个datacenter是按LAN延迟优化的范围。
    source_ids:
    - S2
    availability: post_decision
  - id: E2
    text: 不同datacenter的发现/通信不等同于同一Raft提交；一致性还取决于请求所选一致性模式。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 可核机制是成员传播与一致性承诺属于不同责任；WAN成员消息本身不是另一Raft集群的提交证明。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://developer.hashicorp.com/consul/docs/concept
    publisher: HashiCorp
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E2
    - outcome
  - id: S2
    url: https://developer.hashicorp.com/consul/tutorials/production-vms/reference-architecture
    publisher: HashiCorp
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E1
  attempts:
  - 检索2015 WAN/Raft；尝试v0.6.0两种官方GitHub历史文档路径均Cache miss。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
```

## ENG-141

```yaml
id: ENG-141
decision: reframe
scenario_title: Tree-sitter 2018：局部编辑与语法结构复用
focus: prediction-counterfactual
subdomain: developer-tooling-build
main_question: 局部编辑后增量语法树能改变哪些反馈路径，为什么不能保证完全免于重算？
expected_output: 一个复用范围预测和所需观察点
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-141
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: Tree-sitter 2018：局部编辑与语法结构复用
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 主线应为更新范围预测；精确错误恢复和节点复用仍需固定版本代码，不使用虚构性能数。
```

## ENG-142

```yaml
id: ENG-142
decision: retain
scenario_title: Cloudflare Workers 隔离与启动性能（2017—）
focus: constrained-decision
subdomain: performance-cost
main_question: 启动需求和隔离要求下，isolate 是否适合该负载？
expected_output: 一个执行容器选择与必须核验的隔离条件
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-142
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不得把V8名称当安全证明；具体攻击模型和基准仍待Case QA。
```

## ENG-143

```yaml
id: ENG-143
decision: retain
scenario_title: Okta 2023 客户支持系统事件
focus: causal-modeling
subdomain: security-isolation
main_question: 支持文件中的身份数据被利用；判断日志、会话 token 与第三方信任风险。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-143
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: Okta2023支持系统HAR泄漏
  cutoff: 2023-10-13客户提供可疑IP后的日志选择
  initial_facts:
  - id: I1
    text: 支持系统附件可包含HAR文件
    source_ids:
    - S1
    availability: pre_decision
  - id: I3
    text: 2023-10-13 BeyondTrust已提供与所报事件有关的可疑IP。
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
    - I3
  attempts:
  - 打开独立根因通告，核查HAR、日志路径与已确认利用。
  - root本轮重新打开Okta 2023-11-03通告的调查时间线，核实10月13日可知信号。
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 区别token、密码与支持附件；134客户为该通告阶段范围，不冒充后续调查最终全集。
```

## ENG-144

```yaml
id: ENG-144
decision: reframe
scenario_title: ClickHouse MergeTree：排序键与索引裁剪快照
focus: constrained-decision
subdomain: data-storage
main_question: 以排序键和稀疏索引的公开契约看，排序应优先服务哪类过滤路径，代价到哪里？
expected_output: 一个单类查询的排序责任和代价边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-144
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: ClickHouse MergeTree：排序键与索引裁剪快照
  cutoff: 2026-10-25本轮已读取的公开工件快照，评估其明确契约；不声称候选首发年份即含这些语义。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - Phase4锁定具体版本；排除当前projection、TTL等后加特性，不能回填2016。
```

## ENG-145

```yaml
id: ENG-145
decision: reframe
scenario_title: C++ N3337草案（2012）：原子标志的发布同步
focus: causal-modeling
subdomain: runtime-concurrency
main_question: 读到release sequence的acquire与relaxed读取分别对普通数据可见性保证什么？
expected_output: 一项最小同步条件及错误的原子性外推
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-145
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: C++ N3337草案（2012）：原子标志的发布同步
  cutoff: N3337（2012）固定草案的发布/读取同步条件判断；不将草案日期写成2011。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 明确2012工作草案用于核对C++11语义，不能当2011正式ISO版；Phase4用无数据竞争最小代码。
```

## ENG-146

```yaml
id: ENG-146
decision: retain
scenario_title: React Hooks 发布（2019）
focus: prediction-counterfactual
subdomain: architecture-api
main_question: 组件复用逻辑从类生命周期转向函数闭包；预测新抽象可能暴露的状态错误。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-146
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - FAQ为后续归档文本，不能断言每一FAQ细节当天已有；代码作为抽象推演。
```

## ENG-147

```yaml
id: ENG-147
decision: retain
scenario_title: Facebook 2021 年 10 月全球中断
focus: constrained-decision
subdomain: reliability-diagnosis
main_question: 骨干网配置使服务及运维访问受损；讨论恢复能力对自身依赖的风险。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-147
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 初轮不透露命令根因；恢复路径与自身依赖是唯一决策范围。
```

## ENG-148

```yaml
id: ENG-148
decision: retain
scenario_title: Uber Ringpop 一致性散列（2016）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: 在节点变更与 gossip 传播下预测路由视图暂时分歧造成的请求问题。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-148
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 暂时分歧具体错误需源码/版本确认；不能将官方宣传every request reaches correct node当故障下绝对保证。
```

## ENG-149

```yaml
id: ENG-149
decision: reframe
scenario_title: GitHub Actions：缓存key、分支与PR作用域快照
focus: evidence-selection
subdomain: developer-tooling-build
main_question: 同key命中前，哪项分支或触发器作用域检查能阻止错误复用？
expected_output: 一个可核的可信边界检查及其盲区
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-149
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: GitHub Actions：缓存key、分支与PR作用域快照
  cutoff: 2026-10-25本轮已读取的公开工件快照，评估其明确契约；不声称候选首发年份即含这些语义。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - Phase4必须锁服务策略时点；禁止将当前新增只读规则回填2019。
```

## ENG-150

```yaml
id: ENG-150
decision: reframe
scenario_title: Magic Pocket 2016：自建存储的迁移验证条件
focus: constrained-decision
subdomain: performance-cost
main_question: 双写和dark launch之后，哪些已验证条件足以支持扩大切换，哪些总成本条件仍不能推出？
expected_output: 一项阶段性迁移条件及不可识别的成本结论
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-150
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
  event: Magic Pocket 2016：自建存储的迁移验证条件
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 没有同口径采购/运维/利用率成本，使用constrained-decision备用；2016是披露年不是首次承载年。
```

## ENG-151

```yaml
id: ENG-151
decision: retain
scenario_title: LastPass 2022 备份窃取
focus: boundary-transfer
subdomain: security-isolation
main_question: 凭据保护与加密备份被获取后，分析离线破解和密钥管理风险。
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-151
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - zero knowledge宣传与已确认泄漏分开；不写无来源破解速度或统一PBKDF2设置。
```

## ENG-152

```yaml
id: ENG-152
decision: retain
scenario_title: Elasticsearch 倒排索引（2010—）
focus: causal-modeling
subdomain: data-storage
main_question: 写入已确认但查不到，缺少的是哪一个可见性步骤？
expected_output: 一条写确认到检索可见的因果链
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-152
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不要把2010首版行为与2.x混称；固定2.x且说明查询可见性与耐久性不同。
```

## ENG-153

```yaml
id: ENG-153
decision: retain
scenario_title: Erlang OTP Supervision（1990s—）
focus: boundary-transfer
subdomain: runtime-concurrency
main_question: 重启策略可以恢复哪种能力，又不能恢复哪种业务正确性？
expected_output: 一个恢复边界与未恢复状态
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-153
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 1990s—是开放区间，实际anchor为OTP22；不声称1990s已有所有当前选项。
```

## ENG-154

```yaml
id: ENG-154
decision: retain
scenario_title: GitHub Actions 可复用工作流（2021）
focus: constrained-decision
subdomain: architecture-api
main_question: 该团队应怎样固定复用版本以兼顾升级与可追溯？
expected_output: 一个版本策略及责任边界
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-154
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 不估计维护工时；SHA固定能力还要当年规范证据，不把2022私库共享功能提前。
```

## ENG-155

```yaml
id: ENG-155
decision: retain
scenario_title: Cloudflare 2025 年 12 月解析逻辑故障
focus: evidence-selection
subdomain: reliability-diagnosis
main_question: 什么灰度观测最能提前区分解析错误与流量变化？
expected_output: 一个观测选择及可停止发布的证据
out_of_scope: 不虚构真实请求日志、具体事务/负载、未披露成本或历史首发版本；仅在来源支持的机制、交付和故障边界内判断。
reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
admission: eligible
admission_reason: 已复核2项可知事实、至少2项实质证据和来源支持的结果/工件契约；未知不影响当前限定问题。
research:
  id: ENG-155
  status: sourced
  reason: 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。
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
  - root本轮逐项阅读初轮保存的事前事实、证据、结果和引用，核对新问题是否超出材料；未新增未核事实。
  phase2_conditions:
  - 与11月重复feature文件事故不同；灰度应覆盖配置路径与FL1/规则组合，不提供无来源检测率。
```

## ENG-156

```yaml
id: ENG-156
decision: reframe
scenario_title: Kubernetes Job controller：期望状态与异步控制（文档工件）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: 一次创建Pod请求成功后控制器再次观察到旧状态，下一步要依据什么判断是否继续协调而非认为工作完成？
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不扩写整家公司或系统史，不添加未公开指标、日志和决策者观点
reason: 明确冻结来源版本；不倒推候选初始年份。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-156
  status: sourced
  reason: 明确冻结来源版本；不倒推候选初始年份。
  event: Kubernetes Job controller：期望状态与异步控制（文档工件）
  cutoff: 2026-10-25官方Controllers文档机制快照；不声称2014—2016源码细节
  initial_facts:
  - id: I1
    text: controller观察资源spec中的期望状态。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: Job controller追踪Job资源及为其运行工作的Pod资源。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: Job controller通过API server请求创建/删除Pod，本身不运行容器。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: 其它组件再调度运行Pod，Job完成后controller更新完成状态。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 工件说明控制循环推进状态、结果由多个组件异步达成；单次API请求成功不等于业务已完成，也不保证系统永远静止。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://kubernetes.io/docs/concepts/architecture/controller/
    publisher: Kubernetes
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
  - 尝试kubernetes v1.3.0旧设计路径失败；读取community当前文档，含较新队列API不宜倒推2016。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
```

## ENG-157

```yaml
id: ENG-157
decision: replace
scenario_title: Rust 1.52.1：增量编译ICE后的发布选择（2021）
focus: constrained-decision
subdomain: developer-tooling-build
main_question: 面对unstable fingerprints，应升级补丁、关闭增量还是降级；什么证据会改变选择？
expected_output: 围绕单一问题给出可由证据推翻的解释或选择及边界
out_of_scope: 不扩写整家公司或系统史，不添加未公开指标、日志和决策者观点
reason: 正式应用Phase2替换槽：原Blaze2015与ENG080事件复用；Rust真实补丁发布的关闭优化/升级/降级选择独立于远端action缓存命中、特性合并和affected图。保留ENG157原日期ID。
admission: eligible
admission_reason: 2项可知事实、2项实质证据与机制/事件结局齐备；尚未制作完整Brief和QA。
research:
  id: ENG-157
  status: sourced
  reason: 正式应用Phase2替换槽：原Blaze2015与ENG080事件复用；Rust真实补丁发布的关闭优化/升级/降级选择独立于远端action缓存命中、特性合并和affected图。保留ENG157原日期ID。
  event: Rust 1.52.1：增量编译ICE后的发布选择（2021）
  cutoff: 2021-05-10 1.52.1公告已发布、团队尚未决定本地工具链应对方式
  initial_facts:
  - id: I1
    text: 1.52.0新增指纹校验会以unstable fingerprints ICE暴露增量编译不一致。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: release profile默认关闭增量；dev/test等配置可启用，必须先确定本地实际配置。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 官方说明底层增量错误早已存在，旧版本缺校验可能出现静默误编译。
    source_ids: *id001
    availability: post_decision
  - id: E2
    text: 1.52.1默认停用增量，官方建议升级或显式关闭增量，不建议为此降级。
    source_ids: *id001
    availability: post_decision
  outcome:
    text: 实际发布的1.52.1通过临时默认关闭增量规避风险，并保留显式opt-in；这不是已经修好所有增量错误。
    source_ids:
    - S1
  interpretation: 来源所述观察/机制与维护者迁移推论分开；规范示例是工件推演，不宣称真实生产事故。
  unknowns:
  - 未公开内部决策日、完整负载及业务效果未知；不要求用户据此精算。
  sources:
  - id: S1
    url: https://blog.rust-lang.org/2021/05/10/Rust-1.52.1/
    publisher: Rust project
    published_at: '2021-05-10'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 核查ENG080的2015Bazel公告；另打开Rust项目官方1.52.1完整公告。
  - 本轮实际打开一手正文，按可读机制/事件重新核查准入。
  phase2_conditions:
  - 保留原ID和课程日期；候选标题与本次修订建立显式映射。
  - 结果和隐藏证据不得进入首轮或Starter Prompt。
```
