# Engineering primary-source research — ENG-001–079

Checked 2026-10-25. Research notes only; not a runnable Brief and no ready promotion. Every assigned ID was attempted individually. `availability` refers to the historical cutoff, not coach disclosure: even pre_decision evidence can be withheld from the opening. Publication-time design artifacts are used as documented mechanism snapshots, not invented production incidents. Version/date uncertainties are explicit. Precise canonical event renaming and fallback focus synchronization remain root integration work.

## ENG-001

```yaml
id: ENG-001
status: sourced
reason: 2012 原论文直接支持 TrueTime 不确定性与 commit-wait；无须编造时钟采样。
event: Google Spanner（2012）
cutoff: 论文设计快照，事务协调者选择提交时间戳之前；不混用 Cloud Spanner 后续实现。
initial_facts:
- id: F1
  text: 数据跨数据中心同步复制。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: TrueTime API 显式返回时间不确定范围。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 提交时间戳不早于协调者接收提交消息时 TT.now().latest。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 协调者应用提交记录前等待 TT.after(s)，等待可与 Paxos 通信重叠。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 论文描述借由该时序约束保证外部一致性。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 技术机制来自论文；不能把微基准等同任意部署延迟。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 实际练习不提供未经核实的逐次时钟值。
sources:
- id: S1
  url: https://research.google.com/pubs/archive/39966.pdf
  publisher: Google / Corbett et al.
  published_at: '2012'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://research.google.com/pubs/archive/39966.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 面对跨地区事务与外部一致性需求，判断 TrueTime 的时钟不确定性如何影响提交等待。
```

## ENG-002

```yaml
id: ENG-002
status: blocked
reason: 已读 Docker 2019 多阶段构建教程，但尚未确认 2018 BuildKit 版本对应 Dockerfile 快照；不得将现行缓存规则回填。
event: BuildKit Docker 分层缓存（2018—）
cutoff: 未锁定 2018 版本；目前只确认 2019 官方教程。
initial_facts:
- id: F1
  text: 教程将依赖获取和源码复制分成不同步骤。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 教程示例使用 Maven 和多阶段构建。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 改变步骤输入会使后续缓存失效。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: COPY --from 将构建产物复制到最终阶段。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 2019 教学工件足以支持一般题，但不是已验证的 2018 BuildKit 工件。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 2018 对应 BuildKit tag 与纯文本 Dockerfile。
- 若调整锚点到 2019，需记录候选范围修订。
sources:
- id: S1
  url: https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/
  publisher: Docker / Tibor Vass
  published_at: '2019-07-02'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: BuildKit 2018 候选窗口的一份多阶段 Dockerfile，具体版本待核
  anchor_status: unverified_research_target
  main_question: 只修改依赖清单后，哪一层起需要重建？
  expected_output: 标出缓存失效起点及一次可验证预测
  evidence_to_verify:
  - 当时 Dockerfile 示例
  - 层输入与缓存键语义
  out_of_scope: 不同时估镜像体积或重写整个构建流程
```

## ENG-003

```yaml
id: ENG-003
status: sourced
reason: Slack 当事人复盘提供可排序的观测、自动扩缩容与恢复材料。
event: Slack 2021 年 1 月服务中断
cutoff: 2021-01-04 初始告警、监控面板不可用时；因果解释与修复留到揭晓。
initial_facts:
- id: F1
  text: Americas 早间错误率升高。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 仪表盘与告警服务不可用，但日志及直接查询指标仍可用。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 网络退化与后端等待同时出现。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: CPU 下降触发过缩容，线程利用率随后触发大量扩容。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: Slack 报告网络问题叠加 web tier 饱和及扩容问题使服务不可用。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 为 Slack 事后因果归因；不是单纯新年流量增长结论。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 未提供逐台机器原始日志；不得编造。
sources:
- id: S1
  url: https://slack.engineering/slacks-outage-on-january-4th-2021/
  publisher: Slack / Laura Nolan
  published_at: '2021-02-01'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://slack.engineering/slacks-outage-on-january-4th-2021/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 新年首个工作日请求增长伴随后台资源问题；在有限指标下排列调查优先级。
```

## ENG-004

```yaml
id: ENG-004
status: blocked
reason: 官方现行状态升级说明已读，但未锁定 2016–2023 范围内的协议/Framework版本。
event: Terraform Provider 协议演进（2016—2023）
cutoff: 待选择有日期或 tag 的升级示例；现行 v1.18 文档不可当作早期快照。
initial_facts:
- id: F1
  text: 状态记录资源 schema version。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: provider 声明当前 schema version。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: CLI 在规划前请求 provider 升级旧状态。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 没有相应升级实现时返回错误；响应错误保留旧状态。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 可支持边界概念，不能证明某个历史版本行为。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 历史版本快照和一次完整旧新状态示例。
sources:
- id: S1
  url: https://developer.hashicorp.com/terraform/plugin/framework/resources/state-upgrade
  publisher: HashiCorp
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://developer.hashicorp.com/terraform/plugin/framework/resources/state-upgrade
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Terraform 一次 provider 状态升级的协议快照，版本待核
  anchor_status: unverified_research_target
  main_question: 旧状态交给新 provider 时，谁必须承担兼容转换？
  expected_output: 画出一条状态升级责任边界并指出一个拒绝条件
  evidence_to_verify:
  - 旧新状态表示
  - 协议升级约定
  - 错误处理说明
  out_of_scope: 不综述七年插件协议或设计新平台
```

## ENG-005

```yaml
id: ENG-005
status: blocked
reason: 尝试读取 JEP 333 两次返回 403；未读取原文，不以搜索摘要核源。
event: Java ZGC 上线（2018—2023）
cutoff: 2018 JDK11 候选；精确采用时点未核定。
initial_facts: []
evidence: []
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 不得填入暂停与吞吐数字。
  source_ids: []
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- JEP 正文及同口径工作负载测量未取得。
sources: []
attempts:
- url: https://openjdk.org/jeps/333
  result: 两次open均403，未读取原文
phase2_conditions:
  planning_only: true
  anchor_request: 拟选 2018 候选 ZGC 发布窗口，具体 JDK 与实现待核
  anchor_status: unverified_research_target
  main_question: 对有明确暂停目标的一类大堆服务，是否应试用这版 ZGC？
  expected_output: 一项采用决定及能推翻它的工作负载条件
  evidence_to_verify:
  - 该版本 GC 机制
  - 同口径暂停与吞吐观测
  - 服务约束
  out_of_scope: 不混入分代 ZGC 或比较全部 JVM 回收器
```

## ENG-006

```yaml
id: ENG-006
status: blocked
reason: Figma 2019 原文已读，但不提供文档同步到持久化确认的完整契约，不能完成规划中的确认点判断。
event: Figma Multiplayer 数据模型（2019—）
cutoff: 2019 已连接客户端收到对象更新后、持久化确认未知。
initial_facts:
- id: F1
  text: 文档打开时下载副本，后续更新通过 WebSocket 同步。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: comments/users/teams 等存于 Postgres，采用另一个同步系统。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 断线重连会下载新副本、重新应用离线编辑。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 对象属性冲突由服务器最后收到的值决定。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 同步与持久化不可等同是维护者边界判断。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 文档持久化写入/ACK语义及失败窗口缺失。
sources:
- id: S1
  url: https://www.figma.com/blog/how-figmas-multiplayer-technology-works/
  publisher: Figma / Evan Wallace
  published_at: '2019-10-16'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://www.figma.com/blog/how-figmas-multiplayer-technology-works/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Figma 2019 候选说明中的一次并发对象更新
  anchor_status: unverified_research_target
  main_question: 一个编辑已同步到另一客户端，能否据此断言它已持久保存？
  expected_output: 区分两个确认点并给出一个失败边界
  evidence_to_verify:
  - 对象更新传播说明
  - 持久化确认语义
  - 断联行为
  out_of_scope: 不设计完整多人同步算法
```

## ENG-007

```yaml
id: ENG-007
status: blocked
reason: SolarWinds 当事人调查已读，确认构建注入；发布工件签名与来源核验的可操作证据链仍不足。
event: SolarWinds Orion 供应链攻击（2020）
cutoff: 2020 已签名发布工件的鉴别节点尚未锁定。
initial_facts:
- id: F1
  text: Orion 构建过程成为调查对象。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: SolarWinds 与外部调查者分析构建注入。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 厂商称发现用于向 Orion 构建插入 SUNBURST 的恶意代码源。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 厂商当时未独立核实攻击者身份。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 恶意代码注入及复杂性评价属厂商归因。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 当时签名检查输入与独立重建可行性；CISA 原URL返回403。
sources:
- id: S1
  url: https://www.solarwinds.com/blog/new-findings-from-our-investigation-of-sunburst
  publisher: SolarWinds / Sudhakar Ramakrishna
  published_at: '2021-01-11'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://www.solarwinds.com/blog/new-findings-from-our-investigation-of-sunburst
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: SolarWinds 2020 候选事件的发布工件核验节点
  anchor_status: unverified_research_target
  main_question: 在签名仍可信的条件下，下一项什么检查最能检验工件来源？
  expected_output: 选择一项证据并解释它可排除的假说
  evidence_to_verify:
  - 构建到签名的链路
  - 可知工件信息
  - 公开检查能力
  out_of_scope: 不设计横向传播防御体系或复现攻击
```

## ENG-008

```yaml
id: ENG-008
status: sourced
reason: Discord 原文提供两分钟周期、缓存扫描与调参对照；需修正候选2019为2020公开复盘，服务历史日期未知。
event: Discord Go 垃圾回收瓶颈（2019）
cutoff: Read States 服务出现周期性抖动、深入归因前；不声称2019精确事故日。
initial_facts:
- id: F1
  text: 服务以 LRU 缓存保存 Read States。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 延迟图出现周期性尖峰，分配量较低。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 改变 GC Percent 未改变尖峰；源码显示低频分配下仍会强制 GC。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 减小 LRU 后尖峰缩小，但缓存命中下降使 p99 变差。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: Discord 将尖峰归因于扫描大缓存，并报告 Rust 改写改善表现。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 属于当事人对特定服务的归因；不能推导所有 Go 服务应改 Rust。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 精确运行时 tag 与原始观测序列未给出；不复造图中数值。
sources:
- id: S1
  url: https://discord.com/blog/why-discord-is-switching-from-go-to-rust
  publisher: Discord / Jesse Howarth
  published_at: '2020-02-04'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://discord.com/blog/why-discord-is-switching-from-go-to-rust
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Discord 2019 候选迁移决策前的一类延迟抖动
  anchor_status: unverified_research_target
  main_question: 下一项观测如何区分 GC 暂停与非 GC 的等待？
  expected_output: 列出两个竞争解释并选择区分它们的一项观测
  evidence_to_verify:
  - 当时运行时版本
  - 暂停与分配观测
  - 延迟口径
  out_of_scope: 不把迁移 Rust 当作预定结论
```

## ENG-009

```yaml
id: ENG-009
status: sourced
reason: 2014 原论文给出选举限制、日志匹配及旧任期提交反例。
event: Raft 论文（2014）
cutoff: 论文 Figure 8 的某次领导者崩溃后、下一次选举前；使用论文原图状态。
initial_facts:
- id: F1
  text: Raft 管理复制日志并区分任期。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 选举需要多数票。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: RequestVote 比较末条日志任期，再比较长度。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 旧任期条目不能仅靠副本计数直接提交。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: Figure 8 展示旧任期多数副本条目仍可覆写；当前任期多数提交后间接保护前序条目。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 算法结论，不编造成真实生产事故。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 需在 Phase4 对照原图逐项转录日志状态。
sources:
- id: S1
  url: https://raft.github.io/raft.pdf
  publisher: Stanford / Ongaro and Ousterhout
  published_at: '2014'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://raft.github.io/raft.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 以领导者崩溃与日志冲突为场景，推演选举限制、日志匹配与安全性边界。
```

## ENG-010

```yaml
id: ENG-010
status: sourced
reason: 设计者2018原文直接定义 MVS 并含依赖图示例。
event: Go Modules 引入（2018）
cutoff: 2018 MVS 提案中的依赖图、构建列表计算前。
initial_facts:
- id: F1
  text: 模块声明其他模块的最低版本要求。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 设计假设新版本遵守 import compatibility rule。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 遍历依赖要求，同一模块出现多次取要求中的最高版本。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 升级特定模块将其新构建列表加入再归并。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: MVS 保留满足要求的最低选择，不会每次构建自动追逐所有最新版本。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 可预测性与高保真构建为设计者论点；兼容假设不证明实际包无bug。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 训练需使用原图依赖而非臆造历史依赖。
sources:
- id: S1
  url: https://research.swtch.com/vgo-mvs
  publisher: Russ Cox
  published_at: '2018-02-21'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://research.swtch.com/vgo-mvs
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 取代 GOPATH 版本管理时，分析 minimal version selection 如何影响依赖解析和兼容性。
```

## ENG-011

```yaml
id: ENG-011
status: sourced
reason: 已找到并阅读全文：2024-03-26为同设施独立供电事件，非2023复述；原候选将发布月份误作事故月份需纠正。
event: Cloudflare 2023—2024 年数据中心双重供电事故
cutoff: 2024-03-26 PDX01失联后，两个电源路径同时不可用但共同原因未定时；不把4月8日发布日写成事故日。
initial_facts:
- id: F1
  text: 2023事件后团队已做跨设施HA及容量准备。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 2024-03-26 PDX01再次完全失电，primary与redundant电源路径均不可用。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Cloudflare转述Flexential报告：四个switchboard据报同时失败；上下游电源设备仍正常。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 初步归因指向过低breaker coordination设置触发级联；何时设置未知。
  source_ids:
  - S1
  availability: post_decision
- id: E3
  text: 2月已做cut test；此次大多数控制面约7分钟自动恢复，但部分服务仍需人工干预。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 2024事件验证了HA改进降低影响，仍暴露analytics等未完工作；不能声称零影响。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 供电细节是Cloudflare转述设施方初步判断；服务恢复为Cloudflare自报。与ENG040分别是2024冗余验证和2023控制面依赖诊断。
  source_ids:
  - S1
  attribution: 当事人解释及维护者范围划分
unknowns:
- breaker设置何时建立和设施方完整调查未公开。
- 两个供电路径并不意味着独立故障域。
sources:
- id: S1
  url: https://blog.cloudflare.com/major-data-center-power-failure-again-cloudflare-code-orange-tested/
  publisher: Cloudflare / Matthew Prince, John Graham-Cumming, Jeremy Hartman
  published_at: '2024-04-08'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - E3
  - O1
attempts:
- url: https://blog.cloudflare.com/major-data-center-power-failure-again/
  result: 旧推测slug不可达
- url: https://blog.cloudflare.com/major-data-center-power-failure-again-cloudflare-code-orange-tested/
  result: 已打开阅读全文，确认独立事件与2023差异
phase2_conditions:
  planning_only: true
  anchor_request: 拟选 2024 独立供电事件；身份及与 2023 事件的差异待核
  anchor_status: unverified_research_target
  main_question: 两路电源还可能共享什么失效点，下一步应验证哪一处？
  expected_output: 一项冗余验证决策及其共同原因假说
  evidence_to_verify:
  - 独立事件复盘
  - 两路供电依赖
  - 当时测试或处置记录
  out_of_scope: 不合并两年事故；找不到独立事件则申请换题
```

## ENG-012

```yaml
id: ENG-012
status: sourced
reason: proto2 官方指南直接给出字段更新兼容规则；锚定已读规范快照，非2008特定发布事件。
event: Google Protocol Buffers 兼容策略（2008—）
cutoff: proto2 二进制消息 schema 更新前；仅规范行为，不声称当前文本于2008已完全相同。
initial_facts:
- id: F1
  text: 消息字段有稳定数字编号。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 旧读者可能与新写者同时存在。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 删除非required字段后不得复用字段号。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 新增enum值属于二进制wire安全更新；JSON/TextFormat有不同边界。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 规范允许部分 schema 演进，但字段号复用破坏兼容。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 规范保证与业务语义相容不是同一性质。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 发布日未知；不以规范快照证明特定2008部署。
sources:
- id: S1
  url: https://protobuf.dev/programming-guides/proto2/
  publisher: Protocol Buffers project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://protobuf.dev/programming-guides/proto2/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 客户端与服务器独立演进时，预测删除字段、改变编号、增加枚举值造成的兼容性风险。
```

## ENG-013

```yaml
id: ENG-013
status: sourced
reason: JSR133参与者2004FAQ含双检代码、失败机制与新volatile保证。
event: JVM Double-Checked Locking 语义修订（2004）
cutoff: Java新内存模型评估窗口，读取惰性单例字段前。
initial_facts:
- id: F1
  text: 单例路径在同步外检查共享 instance。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 旧内存模型允许初始化写与引用发布重排。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 未正确同步可读到部分构造对象。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 新模型下 volatile instance 建立初始化与读取的 happens-before。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: FAQ说明Java1.5新volatile语义可修复该双检发布问题。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 仅语言内存模型保证；不据此声称所有懒加载代码正确。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- FAQ后修订删除过性能评价；不采用被划掉的性能结论。
sources:
- id: S1
  url: https://www.cs.umd.edu/~pugh/java/memoryModel/jsr-133-faq.html
  publisher: Jeremy Manson / Brian Goetz
  published_at: 2004-02
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.cs.umd.edu/~pugh/java/memoryModel/jsr-133-faq.html
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 用 Java 内存模型重审惰性单例初始化，辨别排序与可见性保证。
```

## ENG-014

```yaml
id: ENG-014
status: sourced
reason: RocksDB 官方 wiki 支持写/读/空间放大取舍；锚定2023修订工件而非虚称2013精确实现。
event: RocksDB Universal Compaction（2013—）
cutoff: 该已读 wiki 设计快照，选择 compaction 策略之前。
initial_facts:
- id: F1
  text: Universal compaction 合并 sorted runs。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 设计目标是降低写放大。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 代价包括读放大与空间放大。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: major compaction 可暂时使 column family 的磁盘空间翻倍。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 策略以写放大收益交换读取及空间成本。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 来自实现者文档；例子参数不是生产测量。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不将2013视为已经核实的具体首次上线日期。
sources:
- id: S1
  url: https://github.com/facebook/rocksdb/wiki/Universal-Compaction
  publisher: RocksDB project
  published_at: '2023-06-29'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://github.com/facebook/rocksdb/wiki/Universal-Compaction
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 写密集系统选择 compaction 策略时，比较写放大、空间峰值与查询延迟。
```

## ENG-015

```yaml
id: ENG-015
status: sourced
reason: 2023-10-18事件有独立官方复盘，明确是session/authentication token而非已证实OAuth token；与ENG143后续事件必须分开。
event: Cloudflare OAuth token 泄露与缓解（2023）
cutoff: 2023-10-18发现Okta异常访问后、确认影响范围之前；不引入11月后续事件。
initial_facts:
- id: F1
  text: 攻击者使用 Okta 支持工单中被窃的会话 token。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 该 token 具有管理权限。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Cloudflare 观察到两个员工账户在 Okta 平台被攻陷。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 响应团队核查会话、权限及支持来源活动以界定范围。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: Cloudflare称快速响应遏制该次事件，未影响客户系统或信息。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 无客户影响为厂商调查结论；不能扩展为所有后续事件无影响。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 具体逐项凭据轮换优先序未公开；不得虚构OAuth类型或11月结果为事前信息。
sources:
- id: S1
  url: https://blog.cloudflare.com/how-cloudflare-mitigated-yet-another-okta-compromise/
  publisher: Cloudflare
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://blog.cloudflare.com/how-cloudflare-mitigated-yet-another-okta-compromise/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 凭据泄露后、后续入侵结果未知的一个轮换节点
  anchor_status: unverified_research_target
  main_question: 当前只能先核验一类凭据，应按什么暴露路径排序？
  expected_output: 一个优先对象及可改变排序的证据
  evidence_to_verify:
  - 事件身份和时间线
  - 泄露凭据类别
  - 权限与轮换状态
  out_of_scope: 不提前给后续入侵结果或借用 Okta 案例事实
```

## ENG-016

```yaml
id: ENG-016
status: sourced
reason: Uber 2018原文支持单一位置聚合需求及六角/层级取舍，采用定性选择不补误差数字。
event: Uber H3 地理索引（2018）
cutoff: 2018设计说明快照、为定价聚合位置事件时。
initial_facts:
- id: F1
  text: 请求与供给事件具有经纬度位置。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 精确逐点分析昂贵，城市分析需要细粒度区域。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: H3将事件归入六角单元，供需计数用于surge定价。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 邮编等行政区域大小形状不均且会因非业务原因改变。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: Uber报告采用层级六角索引支持市场分析。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 六角量化误差收益属于Uber设计理由；不是误差为零。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 未公开业务可容忍误差阈值，不能虚构。
sources:
- id: S1
  url: https://www.uber.com/us/en/blog/h3/
  publisher: Uber / Isaac Brodsky
  published_at: '2018-06-27'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.uber.com/us/en/blog/h3/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: H3 2018 候选设计中的单一位置聚合需求
  anchor_status: unverified_research_target
  main_question: 面对这个查询和允许误差，是否应选层级六角网格？
  expected_output: 一个索引选择及其不适用条件
  evidence_to_verify:
  - 当时 H3 精度与层级说明
  - 一种查询
  - 误差需求
  out_of_scope: 不同时设计全球位置平台和全部空间查询
```

## ENG-017

```yaml
id: ENG-017
status: sourced
reason: Redis官方Cluster规范可支撑ASK/MOVED的单次迁移行为；锚点为规范工件而非未核实2015事故。
event: Redis Cluster 槽位迁移（2015）
cutoff: 规范live-reconfiguration步骤，槽位处于MIGRATING/IMPORTING时。
initial_facts:
- id: F1
  text: 槽位由源节点向目标节点迁移。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 迁移过程中一些key仍留在源节点。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: MIGRATING节点对不存在的key发ASK而非永久MOVED。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: ASKING只允许一次目标请求，不应立即更新永久槽位映射。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 迁移完成后MOVED允许客户端更新永久映射。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 规范模型，不编造并发生产日志。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 2015原始release文本未锁定，后续Brief应注明规范快照范围。
sources:
- id: S1
  url: https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/
  publisher: Redis project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 迁移 hash slots 时如何处理重定向、并发写和暂时不一致，检验客户端模型。
```

## ENG-018

```yaml
id: ENG-018
status: sourced
reason: 2021官方支持教程完整说明setup/continuation契约。
event: CircleCI Dynamic Config（2021）
cutoff: 2021 setup工作流在运行期决定是否生成后续配置之前。
initial_facts:
- id: F1
  text: setup config带setup:true。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: setup workflow可以运行常规job以计算后续工作。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: CIRCLE_CONTINUATION_KEY与生成配置交给continuation API。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: setup可判定无需工作而结束；当时说明继续流水线有六小时窗口。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 同一pipeline可先生成配置再继续执行相应workflow。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 配置生成并不自动证明依赖选择正确；可讨论验证成本。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不借用2023默认启用规则作为2021事实。
sources:
- id: S1
  url: https://discuss.circleci.com/t/intro-to-dynamic-config-via-setup-workflows/39868
  publisher: CircleCI support
  published_at: '2021-04-23'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://discuss.circleci.com/t/intro-to-dynamic-config-via-setup-workflows/39868
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 大型 CI 流水线需按变更选择任务时，权衡静态配置与生成配置的可测试性。
```

## ENG-019

```yaml
id: ENG-019
status: sourced
reason: 2025-08-21原复盘直接给出地域边界、链路观测与恢复。
event: Cloudflare 2025 年 8 月 AWS 互联拥塞
cutoff: 2025-08-21 16:27 UTC影响出现后、拥塞根因确认前。
initial_facts:
- id: F1
  text: AWS us-east-1来源的部分客户请求高延迟与丢包。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: Cloudflare为客户源站提供反向代理和缓存。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 影响限制在Cloudflare与AWS us-east-1之间，全球其他服务正常。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 流量突增饱和互联；撤回部分BGP广告后其他互联也饱和。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 影响19:38明显降低，20:18前仍有间歇延迟。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: Cloudflare归因为流量/容量而非攻击或BGP劫持。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 无逐包数据；容量图为近似估计，不当作精确链路测量。
sources:
- id: S1
  url: https://blog.cloudflare.com/cloudflare-incident-on-august-21-2025
  publisher: Cloudflare
  published_at: '2025-08-22'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://blog.cloudflare.com/cloudflare-incident-on-august-21-2025
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 2025 年 8 月互联拥塞候选事件，身份待核
  anchor_status: unverified_research_target
  main_question: 哪项地域对照最能区分链路问题与应用自身故障？
  expected_output: 两个假说与一项区分性观测
  evidence_to_verify:
  - 事件复盘
  - 地域影响范围
  - 链路与应用观测时序
  out_of_scope: 不假定全球故障或预先确认拥塞根因
```

## ENG-020

```yaml
id: ENG-020
status: sourced
reason: 官方Compose架构页提供明确状态/事件数据流及TextField例子；训练锚定规范设计快照。
event: Android Jetpack Compose（2021）
cutoff: Compose声明式UI状态设计，TextField回调触发之前。
initial_facts:
- id: F1
  text: Composable接收state并暴露event回调。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 已绘制UI通过state变化触发重组。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 状态向下流、事件向上传到state holder。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: onValueChange请求修改值，实际显示依赖value更新。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 状态持有者负责改变状态，显示组件从状态重新构造UI。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 测试/一致性收益为官方架构理由，非量化生产结果。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 该现行页面不可证明全部示例在2021逐字存在；不填历史上线指标。
sources:
- id: S1
  url: https://developer.android.com/develop/ui/compose/architecture
  publisher: Android Developers
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://developer.android.com/develop/ui/compose/architecture
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 从命令式 UI 转向声明式 UI，检查状态单向流动对组件边界的影响。
```

## ENG-021

```yaml
id: ENG-021
status: blocked
reason: PEP703原文已读，但现行文本含后续Final/实现完成信息；2023修订快照与同口径工作负载待锁定。
event: Python GIL 争论与 PEP 703（2023）
cutoff: 2023提案评估时点；当前正文修订时点混合，不视为全为当时已知。
initial_facts:
- id: F1
  text: 提案讨论可选无GIL构建。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 该提案必须处理CPython C-API兼容。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 无GIL构建的对象头变化影响ABI，扩展需重编。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 依赖GIL保护状态的C扩展需要显式锁。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 不引入Python3.13后续实际成绩作为2023证据。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 2023固定修订hash；工作负载和服务采用约束。
sources:
- id: S1
  url: https://peps.python.org/pep-0703/
  publisher: Python / Sam Gross
  published_at: '2023-01-09'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://peps.python.org/pep-0703/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: PEP 703 的 2023 提案评估窗口，具体修订待核
  anchor_status: unverified_research_target
  main_question: 对一类 CPU 多线程负载，兼容代价是否足以推迟采用？
  expected_output: 一个采用决定与一条改变决定的兼容证据
  evidence_to_verify:
  - 提案版本
  - 对象兼容约束
  - 同口径工作负载观测
  out_of_scope: 不引用后续落地成绩作为当时已知
```

## ENG-022

```yaml
id: ENG-022
status: sourced
reason: LevelDB原实现说明含明确LSM路径与2011实验工件，可用机制预测。
event: Google LSM-tree LevelDB（2011）
cutoff: impl.md所述LSM实现模型，新增随机写入导致memtable轮换前；不把main视为2011精确tag。
initial_facts:
- id: F1
  text: 更新进入log和memtable。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: memtable随后写成level0 sstable。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 超过level限额会将文件与下一层重叠文件合并。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: level0积累使读取必须合并更多文件，后台压缩可触发写入节流。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 顺序持久化与后台合并交换写、读与空间成本。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 说明中的IO数字包含作者假设，不当作真实磁盘观测。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 2011运行tag未知；不采用未经核实的默认值进行精算。
sources:
- id: S1
  url: https://github.com/google/leveldb/blob/main/doc/impl.md
  publisher: Google / LevelDB project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://github.com/google/leveldb/blob/main/doc/impl.md
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 随机写密集场景使用 LSM 后，预测 compaction、读放大与空间放大的变化。
```

## ENG-023

```yaml
id: ENG-023
status: sourced
reason: GitHub Security Lab披露基于其报告过的实际workflow漏洞，具有可读危险例子。
event: GitHub Actions pwn requests 风险（2020—）
cutoff: 2021公开安全说明中的pull_request_target工作流，checkout不可信PR前。
initial_facts:
- id: F1
  text: 外部PR代码是不可信输入。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: pull_request_target可运行于具有写token/Secrets的上下文。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 显式checkout并构建不可信PR可在特权runner执行其脚本。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 未在workflow中显式引用Secrets也不消除内存或磁盘中token风险。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 官方建议分离不可信构建和特权处理，或使用权限受限pull_request触发。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 这是公开漏洞模式工件，不冒充特定未具名入侵事故。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 生产仓库名称与实际被窃信息未给出；不补造。
sources:
- id: S1
  url: https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/
  publisher: GitHub Security Lab / Jaroslav Lobačevski
  published_at: '2021-08-03'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 一次 pwn requests 风险的公开披露或公告窗口
  anchor_status: unverified_research_target
  main_question: 不可信 PR 的哪条执行路径会跨入高权限上下文？
  expected_output: 画出一条数据到执行的信任跨越
  evidence_to_verify:
  - 当时工作流示例
  - token 权限
  - 公告中的触发条件
  out_of_scope: 不把风险类别假装成未核实的独立入侵事故
```

## ENG-024

```yaml
id: ENG-024
status: sourced
reason: SIGMOD2017原论文经Amazon Science获取正文，支持日志/存储恢复契约。
event: Amazon Aurora 共享存储（2017）
cutoff: 论文设计快照、计算实例崩溃且共享存储仍有副本时。
initial_facts:
- id: F1
  text: 实例生命周期与存储生命周期分离。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 每条数据在三个AZ各有两份副本。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 4/6写quorum与3/6读quorum用于副本恢复边界。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 计算节点推动redo到存储，恢复从存储确定可恢复日志界限。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 论文报告该架构支持快速崩溃恢复与无数据丢失的副本故障转移。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 性能/可用性结果属论文作者实验与设计保证，需保留故障假设。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 具体生产故障日志未公开，不编造恢复时长。
sources:
- id: S1
  url: https://cdn.amazon.science/dc/2b/4ef2b89649f9a393d37d3e042f4e/amazon-aurora-design-considerations-for-high-throughput-cloud-native-relational-databases.pdf
  publisher: Amazon / Verbitski et al.
  published_at: '2017'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://cdn.amazon.science/dc/2b/4ef2b89649f9a393d37d3e042f4e/amazon-aurora-design-considerations-for-high-throughput-cloud-native-relational-databases.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 面对数据库实例故障与日志持久化，重建计算节点与分布式存储的恢复契约。
```

## ENG-025

```yaml
id: ENG-025
status: blocked
reason: Nix创始人2006论文已读并发现明确非确定构建反例，但规划要求的一份derivation与一次实际非确定构建快照尚不齐。
event: Nix 可重现构建（2004—）
cutoff: 论文6.8节假设边界；尚未选定具体构建诊断时点。
initial_facts:
- id: F1
  text: 存储路径由构建输入推导。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 纯函数模型假设构建由声明输入确定。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 可变网络资源是确定性反例，fetchurl使用预先指定hash检查。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 论文还讨论归档时间戳等环境因素。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 边界已核实，但不能编造两次构建输出或日志。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 具体derivation、版本与真实不同产物证据。
sources:
- id: S1
  url: https://edolstra.github.io/pubs/phd-thesis.pdf
  publisher: Eelco Dolstra
  published_at: '2006-01-18'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://edolstra.github.io/pubs/phd-thesis.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 一份 Nix derivation 及一次非确定构建的实现快照
  anchor_status: unverified_research_target
  main_question: 两次相同声明却得到不同产物，最先检查哪项隐含输入？
  expected_output: 一个可证伪的环境输入假说
  evidence_to_verify:
  - derivation 内容
  - 实际输入边界
  - 对应版本说明
  out_of_scope: 不讲完整包管理史或重新证明引导信任
```

## ENG-026

```yaml
id: ENG-026
status: sourced
reason: 官方复盘证实KV部署工具配置、401与依赖传播，不是猜测源提示。
event: Cloudflare 2023 年 10 月 Workers KV 部署问题
cutoff: 2023-10-30多产品错误出现、定位KV依赖前。
initial_facts:
- id: F1
  text: Cloudflare多产品依赖Workers KV存取配置及认证状态。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 不使用KV的Workers应用未受影响。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: KV操作返回401而非键值；Pages外层表现可为500。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 源复盘将问题定位为KV新部署工具配置/bug。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 多个服务不可用37分钟，回滚/处置恢复。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 401不等同存储数据丢失；根因属于Cloudflare事后归因。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不提供未公开逐请求日志。
sources:
- id: S1
  url: https://blog.cloudflare.com/cloudflare-incident-on-october-30-2023/
  publisher: Cloudflare / Matt Silverlock and Kris Evans
  published_at: '2023-11-01'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://blog.cloudflare.com/cloudflare-incident-on-october-30-2023/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 2023 年 10 月 KV 候选部署窗口，身份待核
  anchor_status: unverified_research_target
  main_question: 从部署相关性出发，下一项什么证据能区分权限与存储问题？
  expected_output: 一个诊断优先项及两个预期观测差异
  evidence_to_verify:
  - 部署时间线
  - 状态码口径
  - 权限和存储依赖范围
  out_of_scope: 开场不先断言部署工具就是原因
```

## ENG-027

```yaml
id: ENG-027
status: sourced
reason: SQLite官方WAL说明明确3.7.0引入日期、并发及checkpoint行为。
event: SQLite WAL 模式引入（2010）
cutoff: 2010-07-21版本3.7.0新增WAL选择时；排除页面中后续2026缺陷。
initial_facts:
- id: F1
  text: 默认模式使用rollback journal。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: WAL将写入与主数据库文件分开。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: WAL支持读者和写者并行，但仍只有单个writer。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 读者固定end mark，checkpoint需避免覆盖读者所需内容。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: WAL改善读写并发但增加checkpoint、共享内存与同主机约束。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 不是同时多写者或网络文件系统方案。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不得将2026发现的WAL-reset bug当2010事前信息。
sources:
- id: S1
  url: https://www.sqlite.org/wal.html
  publisher: SQLite project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.sqlite.org/wal.html
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 读写并发需求改变时，评估 write-ahead log 相比 rollback journal 的可见性与恢复权衡。
```

## ENG-028

```yaml
id: ENG-028
status: sourced
reason: Dapper2010原论文提供采样规则；缺特定故障频率，按规划回退到证据选择。
event: Google Dapper 采样追踪（2010）
cutoff: 论文采样策略选择时；不预设未给的请求或故障频率。
initial_facts:
- id: F1
  text: 分布式请求跨多个服务，完整追踪有开销。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 首版采用平均1/1024候选trace的统一采样。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 低流量工作负载可能漏重要事件，论文提出按单位时间目标trace数自适应采样。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 采集阶段依trace id统一采或弃整个trace。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 作者报告高吞吐服务低采样仍足以分析多数重要模式，低流量需调整。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 数量题仅能用已给采样率，稀有事件漏采精算需额外频率；改问还需收集何证据。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 缺具体故障频率/独立性，不计算伪精确漏采概率。
sources:
- id: S1
  url: https://research.google.com/pubs/archive/36356.pdf
  publisher: Google / Sigelman et al.
  published_at: 2010-04
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://research.google.com/pubs/archive/36356.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Dapper 2010 候选说明中的单一采样策略
  anchor_status: unverified_research_target
  main_question: 在有来源的请求量与采样口径下，稀有故障漏采风险如何变化？
  expected_output: 一个漏采数量级判断及其适用假设
  evidence_to_verify:
  - 请求与故障频率
  - 采样单位
  - 来源支持的采样规则
  out_of_scope: 不估整个追踪系统成本；缺输入则改证据选择
  quantitative_plan:
    mainline_measure: 稀有事件漏采数量级
    required_inputs:
    - 请求与故障频率
    - 采样单位
    - 同口径采样规则
    missing_input_fallback:
      focus: evidence-selection
      question: 应先核验采样独立性还是故障发生分布，才能判断诊断价值？
    fallback_applied: false
    input_verification: partial_source_check_see_unknowns
```

## ENG-029

```yaml
id: ENG-029
status: sourced
reason: 2015 Rust官方并发文章含实际共享/所有权示例和编译拒绝边界。
event: Rust Ownership 与 Borrow Checker（2015）
cutoff: 2015文章中的跨线程共享例子、编译判断前；沿用原文版本语法。
initial_facts:
- id: F1
  text: 所有权由编译器静态检查。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 线程通信或共享数据需要满足相应所有权限制。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 文章展示channel转移消息所有权。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: Mutex将访问限制于锁保护，并解释编译器阻止错误共享的示例。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 同一所有权模型用于内存安全与避免数据竞争。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 不保证业务时序、死锁或所有逻辑竞态都消失。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- Phase4需逐字对照原文代码而非改成现代语法后假称2015。
sources:
- id: S1
  url: https://blog.rust-lang.org/2015/04/10/Fearless-Concurrency/
  publisher: Rust / Aaron Turon
  published_at: '2015-04-10'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://blog.rust-lang.org/2015/04/10/Fearless-Concurrency/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Rust 2015 候选版本的一段跨线程共享引用示例
  anchor_status: unverified_research_target
  main_question: 这段共享引用能否通过编译检查，检查的保证到哪里为止？
  expected_output: 一个边界判断及不受保证的业务竞态例子
  evidence_to_verify:
  - 版本对应的引用规则
  - 最小示例
  - 线程共享约束
  out_of_scope: 不讲完整 ownership 教程或宣称消除所有并发错误
```

## ENG-030

```yaml
id: ENG-030
status: blocked
reason: 尝试Snowflake2016官方PDF与ACM DOI均未取得正文，不凭标题核实架构细节。
event: Snowflake 分离存储和计算（2016）
cutoff: 2016论文设计快照待取。
initial_facts: []
evidence: []
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 不能从候选摘要宣称已验证虚拟仓库隔离。
  source_ids: []
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 尝试 https://www.snowflake.com/wp-content/uploads/2016/06/Snowflake_SIGMOD.pdf 不可达；https://dl.acm.org/doi/pdf/10.1145/2882903.2903741
  403。
sources: []
attempts:
- url: https://www.snowflake.com/wp-content/uploads/2016/06/Snowflake_SIGMOD.pdf
  result: 不可达，未读到正文
- url: https://dl.acm.org/doi/pdf/10.1145/2882903.2903741
  result: 403，未读到正文
phase2_conditions:
  scope: 工作负载隔离和弹性扩容需求下，分析虚拟仓库如何改变资源竞争。
```

## ENG-031

```yaml
id: ENG-031
status: sourced
reason: MongoDB4.4归档文档锁定候选年份范围内版本，明确write concern/journal/read语义。
event: MongoDB 副本集选主（2016—2020）
cutoff: MongoDB4.4归档契约快照，一次确认写入后、primary选举/重启前；准确文档发表日未知。
initial_facts:
- id: F1
  text: w:1只要求primary确认。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 副本集可能发生primary stepdown与rollback。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 使用majority及投票成员journal支持已确认写保护。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: majority journal等待被关闭时，多数节点瞬时丢失可使majority写回滚；local读还可看到待回滚数据。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: acknowledged与可见不单独保证在任何故障序列下持久存在。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 只使用4.4档案的规则，不混入5.0默认值。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 具体历史生产副本时序没有；如编排状态推演需明确为规范条件而非事故日志。
sources:
- id: S1
  url: https://www.mongodb.com/docs/v4.4/core/replica-set-rollbacks/
  publisher: MongoDB
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.mongodb.com/docs/v4.4/core/replica-set-rollbacks/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 拟选原候选范围内的一版 MongoDB 选举语义
  anchor_status: unverified_research_target
  main_question: 一次已确认写入在给定选举时序后是否仍可读取？
  expected_output: 逐步标出写确认、选举和可见性的关系
  evidence_to_verify:
  - 具体版本
  - write concern
  - 副本时序与回滚规则
  out_of_scope: 不跨版本混用 majority 的含义
```

## ENG-032

```yaml
id: ENG-032
status: blocked
reason: 尝试Guix2013官方引导文章不可达，未获得足够正文。
event: Guix 构建隔离（2013）
cutoff: 2013引导链设计候选，具体工件未读取。
initial_facts: []
evidence: []
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 不以重现hash推断引导链可信。
  source_ids: []
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 尝试 https://guix.gnu.org/en/blog/2013/the-bootstrap-binaries/ 不可访问；需原始论文/存档引导说明。
sources: []
attempts:
- url: https://guix.gnu.org/en/blog/2013/the-bootstrap-binaries/
  result: 不可访问，未取得正文
phase2_conditions:
  planning_only: true
  anchor_request: Guix 2013 候选引导链的一次可信性检查
  anchor_status: unverified_research_target
  main_question: 重建产物一致之后，还需要什么证据检验引导链可信？
  expected_output: 一项检查及其仍不能证明的性质
  evidence_to_verify:
  - 引导依赖
  - 可重建范围
  - 信任根说明
  out_of_scope: 不重复 Nix 未声明环境输入的诊断
```

## ENG-033

```yaml
id: ENG-033
status: sourced
reason: AWS直接复盘给出误指令、index/placement依赖与跨服务后果。
event: AWS S3 2017 年 us-east-1 中断
cutoff: 2017-02-28 9:37AM PST维护指令之后，故障传播调查前。
initial_facts:
- id: F1
  text: S3团队在排查billing处理慢的问题。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 维护playbook原意只移除少量服务器。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 错误输入导致移除更多容量，涉及index和placement子系统。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: placement依赖index，其他依赖S3服务及恢复操作也受影响。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 子系统需完全重启，期间S3请求及若干依赖服务受阻。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 指令失误与传播链为AWS复盘，不简化为单一人的错误。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 实际命令文本与服务器数量未公开，禁止编造。
sources:
- id: S1
  url: https://aws.amazon.com/message/41926/
  publisher: Amazon Web Services
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://aws.amazon.com/message/41926/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 维护操作误影响存储子系统容量；从控制指令到跨服务后果重建故障传播。
```

## ENG-034

```yaml
id: ENG-034
status: blocked
reason: Meltdown原论文已读，攻击/隔离有直接证据；规划指定单一负载的同口径性能代价未取得。
event: Meltdown（2018）
cutoff: 2018缓解评估时，具体服务负载未锁定。
initial_facts:
- id: F1
  text: 内核地址在架构上禁止用户访问。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 乱序执行可产生随后回滚指令的副作用。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 论文展示通过微架构通道观察内核信息。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: KAISER/KPTI通过减少用户地址空间内核映射缓解Meltdown，不能因此消除Spectre。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 攻击可行性不是任意业务负载的成本数据。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 同一负载开关隔离前后指标及服务安全/性能约束。
sources:
- id: S1
  url: https://meltdownattack.com/meltdown.pdf
  publisher: Lipp et al. / original researchers
  published_at: '2018'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://meltdownattack.com/meltdown.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Meltdown 2018 候选缓解决策中的一类负载
  anchor_status: unverified_research_target
  main_question: 对这类负载，是否接受所需隔离的性能代价？
  expected_output: 一项缓解决定及边界负载
  evidence_to_verify:
  - 攻击前提
  - 缓解范围
  - 同口径性能观察
  out_of_scope: 不精算无来源成本或混用 Spectre 条件
```

## ENG-035

```yaml
id: ENG-035
status: sourced
reason: GraphQL设计者2015发布说明足以限定移动端层级查询的接口边界。
event: GraphQL 在 Facebook 的起源（2012—2015）
cutoff: 2015公开设计快照，移动端选择数据获取接口之前。
initial_facts:
- id: F1
  text: Facebook移动应用需要描述复杂数据且支持产品迭代。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 当时GraphQL已在Facebook内部使用。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 查询按UI所需层级描述对象关系。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: REST可能需要多次往返，GraphQL让客户端声明所需字段。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: Facebook公开规范草案及参考实现，原文解释从内部需求发展出的接口。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 作者报告采用与优势；不能推断GraphQL自动降低所有服务端成本。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 精确请求计数需要具体资源图，勿借ENG056的GitHub例子。
sources:
- id: S1
  url: https://graphql.org/blog/2015-09-14-graphql/
  publisher: GraphQL / Lee Byron
  published_at: '2015-09-14'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://graphql.org/blog/2015-09-14-graphql/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 移动端数据需求快速分化时，比较固定 REST endpoint 与客户端声明式查询的边界。
```

## ENG-036

```yaml
id: ENG-036
status: sourced
reason: Linux原始CFS设计说明明确2.6.23及vruntime调度逻辑。
event: Linux CFS 调度器（2007）
cutoff: Linux2.6.23 CFS设计模型，runnable任务选取之前。
initial_facts:
- id: F1
  text: 真实CPU一次只能运行有限任务，CFS用理想等分CPU作模型。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 每任务记录归一化虚拟运行时间。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 选择最小vruntime的可运行任务。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 时间排序红黑树维护任务，nice权重及唤醒规则影响细节。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 任务执行增加vruntime，使其他任务随后得到CPU机会。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 这是公平模型，不是所有任务响应时延相等。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不混入后来的EEVDF；确切文档发布日期未知。
sources:
- id: S1
  url: https://www.kernel.org/doc/Documentation/scheduler/sched-design-CFS.txt
  publisher: Linux kernel / Ingo Molnar
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.kernel.org/doc/Documentation/scheduler/sched-design-CFS.txt
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 负载不均的 CPU 任务争用下，推导 vruntime 如何影响公平与延迟。
```

## ENG-037

```yaml
id: ENG-037
status: sourced
reason: Redis Sentinel官方说明明确异步复制与分区旧主场景，可支撑定性预测。
event: Redis Sentinel 自动故障转移（2013）
cutoff: Sentinel规范中的分区与promote前；不声称现行参数在2013完全一致。
initial_facts:
- id: F1
  text: Redis主从采用异步复制。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 故障转移会选择某个副本提升为新主。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 被确认写可能尚未到达被提升副本。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 隔离客户端仍写旧主时，分区修复后旧主数据被新主覆盖。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: Sentinel不保证所有已确认写在故障后保留；限制复制滞后可缩小风险但损失部分可用性。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 不是故障检测共识自身即可提供数据强一致。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不提供无来源秒级丢失窗口或2013生产日志。
sources:
- id: S1
  url: https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/
  publisher: Redis project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 根据主从延迟和故障检测事件，预测 promote 后的数据丢失窗口和脑裂可能性。
```

## ENG-038

```yaml
id: ENG-038
status: sourced
reason: Go1.21同期设计者文章明确下载/选择规则，适合离线策略取舍。
event: Go 1.21 Toolchain 管理（2023）
cutoff: Go1.21工具链管理引入，离线构建执行前。
initial_facts:
- id: F1
  text: go.mod的go行从建议变成最低工具链要求。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: toolchain行可指定开发该模块的工具链偏好。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 缺少较新工具链时go命令可按module机制下载并重执行。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: GOTOOLCHAIN可强制特定版本或使用version+auto。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 自动管理降低手工安装工作，但离线环境需要预置符合要求的工具链。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 离线失败预测是维护者从下载规则推导；不能假称真实企业故障。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不把推荐策略当唯一答案；离线约束需明确为练习条件。
sources:
- id: S1
  url: https://go.dev/blog/toolchain
  publisher: Go / Russ Cox
  published_at: '2023-08-14'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://go.dev/blog/toolchain
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Go 1.21 候选工具链机制在离线构建中的采用节点
  anchor_status: unverified_research_target
  main_question: 离线环境应允许自动选取工具链，还是显式固定它？
  expected_output: 一个策略及其失败回退条件
  evidence_to_verify:
  - 该版本工具链选择规则
  - 下载行为
  - 离线约束
  out_of_scope: 不同时设计完整供应链管理方案
```

## ENG-039

```yaml
id: ENG-039
status: sourced
reason: Pingora官方2022复盘含同流量CPU/内存与连接复用观测；只能估可支持范围，不能归因全部收益于连接。
event: Cloudflare Pingora 替换 NGINX（2022—2024）
cutoff: 2022说明中的NGINX连接池瓶颈诊断；收益测量在提交预测后揭示。
initial_facts:
- id: F1
  text: NGINX连接池按worker隔离。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 扩worker使连接分散，降低跨请求复用机会。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Pingora采用多线程共享连接池；全客户新建连接约为旧方案三分之一。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 作者报告同流量下CPU约少70%、内存约少67%，同时列有语言与其他架构原因。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 实际迁移后连接复用和资源使用改善；单一客户87.1%到99.92%不可外推全客户。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 不能由总资源降幅识别连接复用的独立因果贡献；数字问需回退至可解释范围。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 缺连接占用成本分解，因此不精算连接复用解释了多少内存。
sources:
- id: S1
  url: https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/
  publisher: Cloudflare
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Pingora 候选迁移说明中的单一连接复用瓶颈
  anchor_status: unverified_research_target
  main_question: 连接复用变化能解释多少资源占用差异？
  expected_output: 一个来源范围内的资源收益估计
  evidence_to_verify:
  - 可比负载
  - 连接与内存口径
  - 公开测量的适用范围
  out_of_scope: 不把单项基准外推为全网收益
  quantitative_plan:
    mainline_measure: 资源变化中可归因的范围
    required_inputs:
    - 同口径连接复用和资源观测
    - 基准负载范围
    missing_input_fallback:
      focus: evidence-selection
      question: 哪项对照最能区分连接复用收益与负载结构变化？
    fallback_applied: false
    input_verification: partial_source_check_see_unknowns
```

## ENG-040

```yaml
id: ENG-040
status: sourced
reason: 2023-11独立官方复盘直接支持控制面/数据面故障域，与2024ENG011分开。
event: Cloudflare 2023 年 11 月控制面中断
cutoff: 2023-11-02控制面与analytics异常出现后、完整依赖梳理之前。
initial_facts:
- id: F1
  text: 控制面包含客户网站/API与配置管理。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: analytics和日志服务也依赖Portland设施。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 供电问题导致关键设施不可用。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 网络/安全流量继续工作，但部分客户无法修改设置；DR恢复多数控制面早于全部服务恢复。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 事故至11月4日04:25UTC完成恢复，部分日志/数据集留缺口。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 持续服务与配置管理有不同故障域；不是所有数据都无损恢复。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不把2024改善成效提前置入2023开场。
sources:
- id: S1
  url: https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/
  publisher: Cloudflare / Matthew Prince
  published_at: '2023-11-04'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 数据中心供电故障令控制面不可用而部分数据面仍工作；判断故障域与依赖分层。
```

## ENG-041

```yaml
id: ENG-041
status: sourced
reason: Bigtable2006原论文直接支持有序行键、tablet切分与局部热点推演。
event: Google Bigtable（2006）
cutoff: 论文设计模型，选择row key及tablet负载分布之前。
initial_facts:
- id: F1
  text: 数据模型为稀疏多版本映射。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 行按row key字典序保存。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 连续行范围组成tablet，是分布与负载均衡单位。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 表增长会自动切分tablet；扫描相邻键可降低RPC数。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 有序局部性使范围扫描有效，但热键/热范围不能仅靠全局节点数消除。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 热点结论为依据分片单位的维护者推演，非论文报告的具体事故。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不编造真实热键指标。
sources:
- id: S1
  url: https://research.google.com/archive/bigtable-osdi06.pdf
  publisher: Google / Chang et al.
  published_at: '2006'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://research.google.com/archive/bigtable-osdi06.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 大规模稀疏宽表如何实现有序键扫描，分析 tablet 切分与单点热点。
```

## ENG-042

```yaml
id: ENG-042
status: blocked
reason: 官方CRD/聚合API比较已读，但现行能力含后续webhook等特性，未锁定2016–2018同版本契约。
event: Kubernetes CRD 与 Aggregated API（2016—2018）
cutoff: 2016–2018内具体版本待核。
initial_facts:
- id: F1
  text: CRD与聚合API是不同扩展机制。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 官方现行比较表区分自定义存储能力。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 聚合API可提供不同存储模式。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 现行CRD表列有webhook支持，不能直接当早期能力。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 需同版本比较，不以现行表直接判定早期不可满足。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 旧版本CRD schema/查询行为与需求快照。
sources:
- id: S1
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
  publisher: Kubernetes project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 一版 Kubernetes 扩展机制下的自定义查询需求
  anchor_status: unverified_research_target
  main_question: 该需求用 CRD 能否满足，还是必须扩展 API 服务？
  expected_output: 一个选择及最小不可满足条件
  evidence_to_verify:
  - 同版本 CRD 能力
  - 所需查询行为
  - 聚合 API 契约
  out_of_scope: 不泛列所有扩展方式优缺点
```

## ENG-043

```yaml
id: ENG-043
status: sourced
reason: Spectre原研究论文支持一条缓存观察路径与架构权限边界。
event: Spectre（2018）
cutoff: 原始披露的推测执行观察模型；固定变体并在预测前隐藏实际泄漏。
initial_facts:
- id: F1
  text: CPU使用分支预测与推测执行。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 错误推测的架构计算结果会被丢弃。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 推测执行仍可能留下可测微架构副作用。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 论文实验证明可诱导受害者执行正常路径不会执行的操作，并经侧信道泄漏。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 架构层访问限制未完整覆盖微架构可观察状态。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 变体条件必须各自保留；KPTI防Meltdown不等同解决Spectre。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不得混用不同变体触发前提或编造测量日志。
sources:
- id: S1
  url: https://spectreattack.com/spectre.pdf
  publisher: Kocher et al. / original researchers
  published_at: '2018'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://spectreattack.com/spectre.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Spectre 2018 候选披露中的一条观察路径
  anchor_status: unverified_research_target
  main_question: 架构层访问被拒绝后，为什么仍需检验可观察信息边界？
  expected_output: 指出一项架构保证与它未覆盖的观察
  evidence_to_verify:
  - 该变体的触发前提
  - 可观察量
  - 缓解边界
  out_of_scope: 不估无数据成本或把漏洞与 Meltdown 混同
```

## ENG-044

```yaml
id: ENG-044
status: sourced
reason: TAO2013原论文给出MySQL持久层、cache层与跨区异步传播。
event: Facebook TAO（2013）
cutoff: 论文一次远端写完成、本地数据库异步复制尚未赶上时。
initial_facts:
- id: F1
  text: TAO针对读多写少的社交图提供固定查询API。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: MySQL负责持久化，TAO提供图感知缓存。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 成功转发写后本地leader先更新缓存，local slave database可能尚未收到复制。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 跨区异步复制以读取性能与吞吐交换一致性。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: TAO显式偏向可用性与单机效率，可能出现短暂陈旧读取。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 作者对设计取舍的说明，不预设所有读都最新。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不虚构复制延迟或一致性SLA。
sources:
- id: S1
  url: https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf
  publisher: Facebook / Bronson et al.
  published_at: '2013'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 研究社交图读多写少场景中，缓存层与主存储的更新传播及一致性取舍。
```

## ENG-045

```yaml
id: ENG-045
status: sourced
reason: Cargo官方features页明确union及resolver2例外，可选一版resolver进行菱形依赖推演。
event: Rust Cargo Features 设计（2013—）
cutoff: resolver=2明确指定的规范模型、增加一条普通依赖之前；不声称2013已具resolver2。
initial_facts:
- id: F1
  text: 每个package定义自己的命名feature集合。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 同一依赖可能被多个包启用不同feature。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 正常依赖使用启用feature的并集。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: resolver2对未构建平台、build依赖/proc-macro与部分dev依赖不合并。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 增加普通依赖可能给共享包启用额外feature；不是任意上下文都全局合并。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 规则是确定性解析，不应直接称不可重现。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 示例图须标明规范推演，不编造成历史生产依赖。
sources:
- id: S1
  url: https://doc.rust-lang.org/cargo/reference/features.html
  publisher: Rust / Cargo project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://doc.rust-lang.org/cargo/reference/features.html
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 一版 Cargo resolver 下的一个菱形依赖特性组合
  anchor_status: unverified_research_target
  main_question: 增加一条依赖后，现有包会启用哪些额外特性？
  expected_output: 一张变更前后特性集合对照
  evidence_to_verify:
  - resolver 版本
  - 依赖图
  - feature 合并规则
  out_of_scope: 不把 feature 合并直接等同于不可复现
```

## ENG-046

```yaml
id: ENG-046
status: blocked
reason: 已读.NET官方HillClimbing源码，但未锁定历史tag及一个实际worker调整的观测曲线。
event: .NET ThreadPool Hill Climbing（2000s—）
cutoff: 运行时与负载观测快照待定。
initial_facts:
- id: F1
  text: 实现按完成数/采样时间计算吞吐。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 实现保存线程数及吞吐样本。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 通过线程变化与吞吐变化的波形比较估计调整方向。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 噪声影响置信度与调整幅度。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 线程增加并非必然提升吞吐。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 历史tag、worker队列、同口径吞吐曲线缺失。
sources:
- id: S1
  url: https://github.com/dotnet/runtime/blob/main/src/libraries/System.Private.CoreLib/src/System/Threading/PortableThreadPool.HillClimbing.cs
  publisher: .NET / Microsoft
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://github.com/dotnet/runtime/blob/main/src/libraries/System.Private.CoreLib/src/System/Threading/PortableThreadPool.HillClimbing.cs
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 一个 .NET 实现快照下的 worker 注入调整
  anchor_status: unverified_research_target
  main_question: 下一项测量怎样区分线程不足与线程竞争？
  expected_output: 一项观测选择及两种相反预测
  evidence_to_verify:
  - 运行时版本
  - worker 与队列观测
  - 吞吐曲线口径
  out_of_scope: 不综述 ThreadPool 历史或只凭线程数下结论
```

## ENG-047

```yaml
id: ENG-047
status: sourced
reason: Fastly2021官方事故说明明确有效配置触发潜伏实现bug与恢复。
event: Fastly 2021 年 6 月大面积故障
cutoff: 2021-06-08客户配置变化后、定位触发条件之前。
initial_facts:
- id: F1
  text: 边缘网络运行先前部署的软件。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 客户提交了一份有效配置。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 5月12日起的部署引入在特定配置/条件下触发的潜伏bug。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 停用触发配置后恢复，49分钟内95%网络正常。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 6月8日事件使85%网络返回错误，根因在底层软件bug而非配置无效。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 根因与规模为Fastly复盘，不能把合法配置视为用户过错。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 触发配置具体内容与软件bug代码未公开。
sources:
- id: S1
  url: https://www.fastly.com/blog/summary-of-june-8-outage
  publisher: Fastly / Nick Rockwell
  published_at: '2021-06-08'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.fastly.com/blog/summary-of-june-8-outage
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 潜伏软件缺陷被客户配置触发；评估配置有效性与底层实现之间的责任边界。
```

## ENG-048

```yaml
id: ENG-048
status: blocked
reason: SQLite官方查询规划教程有SQL/索引及ANALYZE推理，但无版本化真实慢查询计划与统计快照。
event: SQLite Query Planner（2010s）
cutoff: 规划要求的同SQL实际计划变慢节点未取得。
initial_facts:
- id: F1
  text: SQL描述结果，planner选择执行算法。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 可选索引影响访问路径。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 教程用fruit='Orange'说明个别值与平均选择性不同。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: ANALYZE统计使planner在多个索引间估计，未运行时选择可能任意。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 可保留题意，但需锁定可复现工件或改为规范例子并记录。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 版本、EXPLAIN计划输出、同数据分布及实际慢查询观测。
sources:
- id: S1
  url: https://www.sqlite.org/queryplanner.html
  publisher: SQLite project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://www.sqlite.org/queryplanner.html
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 一个 SQLite 查询计划和统计信息快照
  anchor_status: unverified_research_target
  main_question: 慢查询更可能来自缺索引还是基数估计偏差？
  expected_output: 两个假说及一项区分实验
  evidence_to_verify:
  - 同一 SQL
  - 索引定义
  - 统计与计划输出
  - 版本
  out_of_scope: 不泛讲查询优化器或编造运行日志
```

## ENG-049

```yaml
id: ENG-049
status: sourced
reason: 官方控制器文档可支撑声明状态与执行职责的分离；以设计工件为锚点。
event: Kubernetes API 对象与控制器分离（2014—）
cutoff: Kubernetes声明对象被创建后、控制器调和之前；不宣称Deployment在2014初版已有。
initial_facts:
- id: F1
  text: 对象spec描述期望状态。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 控制器观察资源并使当前状态接近期望。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 控制器一般经API server创建或删除其他对象。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 官方Job例子指出controller不亲自运行Pod，其他组件调度/执行。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 声明对象、调和与实际执行存在职责和时间边界。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 原候选Deployment/ReplicaSet/Pod层级需配合同期API引用，不泛化为创建即运行。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 历史版本与Deployment引入日期未核；ready前需固定对象示例版本。
sources:
- id: S1
  url: https://kubernetes.io/docs/concepts/architecture/controller/
  publisher: Kubernetes project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://kubernetes.io/docs/concepts/architecture/controller/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 从 Deployment、ReplicaSet、Pod 分层理解声明式 API 如何分配状态和所有权。
```

## ENG-050

```yaml
id: ENG-050
status: sourced
reason: Kafka2011原论文提供200-byte消息及batch1/50对照；等待无实测分布，沿既定fallback做方向预测。
event: LinkedIn Kafka 日志存储（2011）
cutoff: 2011论文producer实验工件，比较batch1与50前；实验结果隐藏。
initial_facts:
- id: F1
  text: 单producer发送一千万条200-byte消息。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 同实验配置对比batch1及50，broker异步flush。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 论文报告约5万与40万messages/s的平均吞吐。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 作者明确无broker ACK提高吞吐但不能保证每条已收到；批处理摊薄RPC开销。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 该实验批50提高吞吐近数量级，但不能据此计算任意低流量批等待。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 收益受异步确认、网络等多因素影响，不把所有差异归于磁盘顺序写。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 缺到达分布和等待时间测量；采用prediction-counterfactual备用题，保留未核输入。
sources:
- id: S1
  url: https://www.microsoft.com/en-us/research/wp-content/uploads/2017/09/Kafka.pdf
  publisher: LinkedIn / Kreps, Narkhede, Rao
  published_at: '2011'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.microsoft.com/en-us/research/wp-content/uploads/2017/09/Kafka.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Kafka 2011 候选存储设计的一段批量写入路径
  anchor_status: unverified_research_target
  main_question: 增大批量会怎样改变单位写入工作量和等待？
  expected_output: 一个吞吐与等待的数量级权衡
  evidence_to_verify:
  - 消息大小
  - 批大小
  - 同口径磁盘或调用观测
  out_of_scope: 不同时证明零拷贝、顺序写和全部吞吐收益
  quantitative_plan:
    mainline_measure: 批量变化的工作量与等待边界
    required_inputs:
    - 消息与批大小
    - 同口径调用或存储工作量
    missing_input_fallback:
      focus: prediction-counterfactual
      question: 批量增大时吞吐和等待会朝什么方向变化，哪个前提可能失效？
    fallback_applied: false
    input_verification: partial_source_check_see_unknowns
```

## ENG-051

```yaml
id: ENG-051
status: sourced
reason: Apache原安全公告明确CVE-2021-44228输入控制、JNDI与LDAP执行条件。
event: Log4Shell（2021）
cutoff: 2021 Log4j2受影响版本处理不可信日志输入之前；修补结局在最终揭晓。
initial_facts:
- id: F1
  text: log4j-core会处理日志消息及参数中的lookup。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 攻击者可能控制进入日志的字符串。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: CVE说明JNDI功能未约束攻击者控制的LDAP等端点。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 仅log4j-api而无core的应用不受该CVE影响。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 官方确认可导致从LDAP加载任意代码；初始2.15修复后另有不完整配置问题，不能把其当万能最终修复。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 漏洞能力是公告确认，不冒充某次具体受害者入侵结果。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 具体应用配置与JDK条件需在Brief固定，不能泛称所有Java日志皆可RCE。
sources:
- id: S1
  url: https://logging.apache.org/security.html
  publisher: Apache Logging Services
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://logging.apache.org/security.html
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 日志字符串最终触发 JNDI 远程查找；在数据到控制的路径上定位信任边界。
```

## ENG-052

```yaml
id: ENG-052
status: sourced
reason: Dynamo2007原论文支持N/R/W、版本冲突和sloppy quorum边界。
event: Amazon Dynamo（2007）
cutoff: 论文设计模型的一次分区与读取前；沿论文N/R/W示例，不造购物车事故。
initial_facts:
- id: F1
  text: 购物车需求强调在部分故障下继续接收操作。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: N为复制数，R/W为成功读写所需响应数。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: sloppy quorum使用preference list中前N个健康节点，不始终为原N节点。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 对象版本与应用协助冲突合并处理分歧。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 分区可产生多个不可直接排序的版本，不能仅由R+W>N推导所有故障下强一致。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 论文机制，不以SLA数字判断任意分区执行必成功。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 需指定可达节点与时序，否则请求失败还是多版本无法唯一确定。
sources:
- id: S1
  url: https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
  publisher: Amazon / DeCandia et al.
  published_at: '2007'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Dynamo 2007 候选设计的一次网络分区
  anchor_status: unverified_research_target
  main_question: 在这一组读写配置下，请求会失败还是返回多个版本？
  expected_output: 一条分区时序预测及冲突条件
  evidence_to_verify:
  - 该设计版本
  - 副本与读写配置
  - 冲突处理规则
  out_of_scope: 不设计整个购物车系统或做无数字的精算
```

## ENG-053

```yaml
id: ENG-053
status: blocked
reason: Nx现行v24 affected机制已经变化为task-based，无法直接用于原候选2020项目依赖图题。
event: Nx Affected Builds（2020—）
cutoff: 2020候选快照未锁定；本次已读v24页。
initial_facts:
- id: F1
  text: 现行命令从Git变化文件识别工作。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 当前文档明确与Nx23及之前project-based affected不同。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 当前按任务inputs及下游输出依赖选择任务。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 忽略文件与lockfile规则也会改变集合。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 版本差异是具体阻塞；需历史project graph工件。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 2020版本文档、依赖图与一次改动集合。
sources:
- id: S1
  url: https://nx.dev/docs/features/ci-features/affected
  publisher: Nx
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://nx.dev/docs/features/ci-features/affected
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 在 Monorepo 中按依赖图选择受影响任务，分析图不完整时的漏构建风险。
```

## ENG-054

```yaml
id: ENG-054
status: blocked
reason: 候选Google2012闰秒Linux高CPU事件身份未核实；Google官方时间文档称自2008已smear，不能混用其他公司2012事故。
event: Google 2012 年闰秒 Linux 故障
cutoff: 候选2012事故尚未识别。
initial_facts:
- id: F1
  text: Google官方称自2008起用smear而非clock steps处理闰秒。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 该说明同时指出smear实现后来曾从20小时变为24小时。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 当前推荐为noon-to-noon线性24小时smear。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 文档例子明确是假定的2022闰秒，不是真实事件。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 不能以全行业Linux闰秒问题自动归到Google。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 需要Google特定故障原复盘；否则进入有理由换题队列。
sources:
- id: S1
  url: https://developers.google.com/time/smear
  publisher: Google Developers
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://developers.google.com/time/smear
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 时间推进异常引发高 CPU 及服务退化；识别时钟假设与同步机制的关系。
```

## ENG-055

```yaml
id: ENG-055
status: sourced
reason: Go1.14官方release notes明确异步抢占语义及平台例外。
event: Go 1.14 异步抢占（2020）
cutoff: Go1.14运行忙循环且另一goroutine可运行时，限支持平台。
initial_facts:
- id: F1
  text: 此前无函数调用循环可能延迟调度/GC。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 场景必须指定Go1.14和支持异步抢占的平台。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: release notes说明goroutine现可异步抢占，忙循环不再潜在死锁scheduler或严重拖延GC。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: windows/arm、darwin/arm、js/wasm和plan9为当时例外。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 调度机会不再依赖忙循环主动函数调用；不保证所有暂停消失。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: Unix信号/EINTR变化是实现后果，不泛化为零延迟调度。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 原文无具体循环片段，应在Brief明确最小示例为规范推演。
sources:
- id: S1
  url: https://go.dev/doc/go1.14
  publisher: Go project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://go.dev/doc/go1.14
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Go 1.14 候选抢占规则下的一段 CPU 忙循环
  anchor_status: unverified_research_target
  main_question: 另一个可运行 goroutine 何时才有机会执行？
  expected_output: 一项前后行为预测及仍可能停顿的边界
  evidence_to_verify:
  - 具体运行时
  - 循环片段
  - 抢占可达条件
  out_of_scope: 不把调度改进等同于消除所有暂停
```

## ENG-056

```yaml
id: ENG-056
status: sourced
reason: 2016原发布文章有完整关系查询和单请求结果；REST对应分页/endpoint不齐，应用既定boundary-transfer fallback。
event: GitHub REST 到 GraphQL API v4（2016）
cutoff: 2016 Early Access发布工件，客户端需获取用户前三仓库及计数；不采用2021后续成果。
initial_facts:
- id: F1
  text: REST集成者报告需要多次调用才能组完整资源视图。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 目标示例是用户名、starred总数及前三仓库的多个计数。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 文章给出带repositories(first:3)的GraphQL查询及完整响应。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: GitHub解释schema类型、授权、分页、速率限制与backend batching仍由服务端实现。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 示例用一次请求返回目标数据；不能凭此推算所有REST端点的精确请求数。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 声明式查询移走客户端拼装复杂性，但增加服务端查询/授权/成本管理。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 当时REST分页对应端点未逐项取得；使用boundary-transfer备用问题，禁止编造REST调用数。
sources:
- id: S1
  url: https://github.blog/developer-skills/github/the-github-graphql-api/
  publisher: GitHub
  published_at: '2016-09-14'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://github.blog/developer-skills/github/the-github-graphql-api/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: GitHub API v4 候选发布时的单一资源关系查询
  anchor_status: unverified_research_target
  main_question: 完成同一份客户端结果，REST 与 GraphQL 分别需要多少请求？
  expected_output: 同结果口径的请求计数及一个服务端代价
  evidence_to_verify:
  - 当时 endpoint 或 schema
  - 分页规则
  - 请求示例
  out_of_scope: 不凭 API 名称估算全面性能提升
  quantitative_plan:
    mainline_measure: 完成同一结果的请求次数
    required_inputs:
    - 同期 endpoint 和 schema
    - 分页规则
    - 同一目标结果
    missing_input_fallback:
      focus: boundary-transfer
      question: 声明式查询减少了哪种客户端工作，又把什么复杂性转给服务端？
    fallback_applied: false
    input_verification: partial_source_check_see_unknowns
```

## ENG-057

```yaml
id: ENG-057
status: sourced
reason: Redshift官方存储说明直接支持只读所需列与同类型压缩；作为架构工件而非2012实测事件。
event: Amazon Redshift 列式分析（2012）
cutoff: 列式分析存储布局选择；候选2012首发日期不由此现行页证实。
initial_facts:
- id: F1
  text: 分析查询常只读少数列。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 列式块保存同一列多个记录的值。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 只读取查询所需列可减少磁盘与内存加载。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 同类型值可选择特定压缩编码。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 文档展示列式布局可减少I/O；其中三倍示意是简化例子而非真实基准。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 排序键与分布需另外来源；不能从此页独立断言全部性能原因。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不外推简化示例倍数；2012版本快照未锁定。
sources:
- id: S1
  url: https://docs.aws.amazon.com/redshift/latest/dg/c_columnar_storage_disk_mem_mgmnt.html
  publisher: Amazon Web Services
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://docs.aws.amazon.com/redshift/latest/dg/c_columnar_storage_disk_mem_mgmnt.html
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 大量扫描与聚合请求时，判断压缩、排序键和数据分布对于性能的影响。
```

## ENG-058

```yaml
id: ENG-058
status: blocked
reason: 尝试Kafka0.8官方归档多种路径仅返回重定向页；取得0.8.0配置源码但选举/ACK全契约仍未读取。
event: Kafka 复制协议（2012—2013）
cutoff: 原候选2012–2013内0.8.0实现，完整版本规则待核。
initial_facts: []
evidence: []
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 不能把现代unclean election默认值回填早期。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 尝试 https://kafka.apache.org/081/documentation.html、https://kafka.apache.org/08/documentation.html
  均为redirect内容。
- 仍需ISR状态机、leader选举和producer ack同版本实现。
sources:
- id: S1
  url: https://raw.githubusercontent.com/apache/kafka/0.8.0/core/src/main/scala/kafka/server/KafkaConfig.scala
  publisher: Apache Kafka
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- url: https://raw.githubusercontent.com/apache/kafka/0.8.0/core/src/main/scala/kafka/server/KafkaConfig.scala
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 拟选 2012—2013 内的一版 Kafka 复制规则
  anchor_status: unverified_research_target
  main_question: 一个 broker 失效后，这条消息还能否被安全确认？
  expected_output: 一条 ISR 与选举状态变化预测
  evidence_to_verify:
  - 版本
  - ack 配置
  - ISR 状态
  - 选举规则
  out_of_scope: 不混用后来默认值或回到通用 Raft 日志题
```

## ENG-059

```yaml
id: ENG-059
status: sourced
reason: Remote Execution API v2.0.0原proto固定版本，支持action输入与环境边界核验。
event: Bazel Remote Execution API（2018—）
cutoff: v2.0.0 Action/Command契约，决定复用缓存之前。
initial_facts:
- id: F1
  text: Action包含command digest与input root digest。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 输入目录及其blob必须存在于CAS。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Command记录arguments和显式environment_variables，等价字段需按规范排序。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 未额外规定时，系统库/挂载等执行环境由API实现定义，worker还可能有默认环境变量。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: action摘要只能覆盖声明/编码的输入，环境一致性仍需客户端与worker契约保证。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 核验遗漏工具链/环境可揭露错误缓存复用；不假称API保证任意未声明环境。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 工具链实际标识需具体实现补证；2018 copyright不是tag发布日期。
sources:
- id: S1
  url: https://raw.githubusercontent.com/bazelbuild/remote-apis/v2.0.0/build/bazel/remote/execution/v2/remote_execution.proto
  publisher: Bazel Authors
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://raw.githubusercontent.com/bazelbuild/remote-apis/v2.0.0/build/bazel/remote/execution/v2/remote_execution.proto
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Remote Execution API 的一项 action 请求
  anchor_status: unverified_research_target
  main_question: 检查什么输入最能暴露错误的远端缓存复用？
  expected_output: 一个核验项与可推翻正确性的例子
  evidence_to_verify:
  - API 版本
  - action 输入
  - 环境和摘要范围
  out_of_scope: 不重新讲整个 Bazel 依赖图
```

## ENG-060

```yaml
id: ENG-060
status: sourced
reason: OpenSSL2014原公告直接确认heartbeat缺边界检查、泄漏能力及修复。
event: Heartbleed OpenSSL（2014）
cutoff: OpenSSL1.0.1f等受影响版本接收heartbeat时，结果在推演后揭晓。
initial_facts:
- id: F1
  text: TLS heartbeat由对端输入。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 受影响版本为1.0.1及1.0.2beta系列指定版本。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 处理heartbeat缺少bounds check，可向已连接客户端或服务器泄漏内存。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 修复为1.0.1g，临时可禁用heartbeat后重编。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 公告确认每次可泄漏至多64k内存。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 读越界是已确认机制；不能虚构泄露了某个真实私钥。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 最小代码片段与具体报文长度还需对照补丁，公告不提供完整测试覆盖历史。
sources:
- id: S1
  url: https://openssl-library.org/news/secadv/20140407.txt
  publisher: OpenSSL
  published_at: '2014-04-07'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://openssl-library.org/news/secadv/20140407.txt
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: TLS heartbeat 输入长度校验缺失导致内存泄漏；推演信任边界和测试覆盖盲点。
```

## ENG-061

```yaml
id: ENG-061
status: sourced
reason: 2024-06-20复盘明确两个连续事件；只取第二个DDoS规则触发率限bug，避免混同首个拥塞。
event: Cloudflare 2024 年 6 月 DDoS 规则事故
cutoff: 2024-06-20 17:47后第二事件初期，观测异常、尚未知规则触发bug。
initial_facts:
- id: F1
  text: 该日曾有先后两个事件，第二个发生于新DDoS规则逐步部署之后。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 请求错误与CPU、TTFB退化可作调查输入。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 规则通过cookie及rate limit组合触发legacy组件意外调用路径。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 请求进程进入无限循环；重启改善，关闭规则及修复Traffic Manager恢复服务。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 第二事件经滚动重启和禁用规则缓解，复盘未发现蓄意利用或入侵证据。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 并非普通误拦截；应允许流量/策略/源站三个假说再用观测区分。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 所有错误率有各自分母，不能把回源5xx与本服务不可用混用。
sources:
- id: S1
  url: https://blog.cloudflare.com/cloudflare-incident-on-june-20-2024/
  publisher: Cloudflare
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://blog.cloudflare.com/cloudflare-incident-on-june-20-2024/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 2024 年 6 月 DDoS 规则候选，事件身份待核
  anchor_status: unverified_research_target
  main_question: 下一项什么观测能区分恶意流量、误伤与回源故障？
  expected_output: 选择一项可同时区分三种解释的观测
  evidence_to_verify:
  - 独立复盘
  - 规则生效时序
  - 受影响请求范围
  out_of_scope: 不预先把保护误伤当作真实原因
```

## ENG-062

```yaml
id: ENG-062
status: blocked
reason: 尝试Netflix稳态码率文章不可达；单一带宽下降时的缓冲状态/设计版本未取得。
event: Netflix 自适应码率播放（2010s）
cutoff: 2010s具体自适应码率设计与播放节点待核。
initial_facts: []
evidence: []
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 不能编造缓冲秒数和码率曲线。
  source_ids: []
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 尝试 https://netflixtechblog.com/a-steady-state-approach-to-rate-adaptation-1b05b3a806f7
  不可访问；需作者论文或官方存档。
sources: []
attempts:
- url: https://netflixtechblog.com/a-steady-state-approach-to-rate-adaptation-1b05b3a806f7
  result: 不可访问，未取得正文
phase2_conditions:
  planning_only: true
  anchor_request: 一份 Netflix 自适应码率设计中的一次带宽下降
  anchor_status: unverified_research_target
  main_question: 当前应降低画质还是维持码率等待缓冲？
  expected_output: 一个播放决定及会改变决定的缓冲条件
  evidence_to_verify:
  - 设计版本
  - 可知带宽观察
  - 缓冲状态和目标
  out_of_scope: 不设计整套流媒体算法或追求最高码率
```

## ENG-063

```yaml
id: ENG-063
status: blocked
reason: 2019 Rust稳定发布原文已读，足以证明lazy/poll；取消与资源释放的同版本语义未齐，保留原范围不自动缩成惰性常识题。
event: Rust async/await 稳定（2019）
cutoff: Rust1.39稳定的future创建/轮询模型；取消节点未锁定。
initial_facts:
- id: F1
  text: async fn返回Future。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 单纯调用async fn不自动调度执行。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 文章例子通过await执行future。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: Rust使用poll模型，避免每个future都创建独立调度工作的开销。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 不能将drop自动等同远端操作回滚。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 取消时具体Future状态、Drop实现和资源释放来源。
sources:
- id: S1
  url: https://blog.rust-lang.org/2019/11/07/Async-await-stable/
  publisher: Rust / Niko Matsakis
  published_at: '2019-11-07'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://blog.rust-lang.org/2019/11/07/Async-await-stable/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: Future 的惰性执行与任务轮询不同于线程时，预测取消与资源释放边界。
```

## ENG-064

```yaml
id: ENG-064
status: blocked
reason: 2017 OCI原发布公告已读；v1.0镜像规范正文尝试未取得，未完成格式保证与运行时前提的逐条核对。
event: Docker Image OCI 标准化（2015—2017）
cutoff: 2017 v1.0发布窗口；页面正文新闻稿日期另为7月19日，保留差异。
initial_facts:
- id: F1
  text: OCI分别发布Runtime和Image Format规范。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: Runtime规范处理生命周期，Image规范处理镜像格式。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 公告将二者描述为最小、开放标准及可移植性基础。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 认证计划当时尚待推出，非公告即所有实现已通过认证。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 运行兼容边界需规范正文，不能以营销可移植宣称覆盖环境差异。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- https://raw.githubusercontent.com/opencontainers/image-spec/v1.0.0/README.md读取cache
  miss；需版本化正文。
sources:
- id: S1
  url: https://opencontainers.org/posts/announcements/2017-07-17-open-container-initiative-oci-releases-v1-0-of-container-standards/
  publisher: Open Container Initiative
  published_at: '2017-07-17'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://opencontainers.org/posts/announcements/2017-07-17-open-container-initiative-oci-releases-v1-0-of-container-standards/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: OCI 候选标准的一版镜像互操作契约
  anchor_status: unverified_research_target
  main_question: 镜像格式符合规范，是否就能推断应用在另一运行时正常工作？
  expected_output: 一个格式保证与一个未保证行为
  evidence_to_verify:
  - 具体规范版本
  - 镜像内容边界
  - 运行时前提
  out_of_scope: 不综述标准化历史或把格式兼容等同环境兼容
```

## ENG-065

```yaml
id: ENG-065
status: sourced
reason: CIDR2011原论文经Google链接读到，entity group边界、两阶段提交和吞吐约束完整。
event: Google Megastore（2011）
cutoff: 2011论文选择entity group划分、一次跨组操作之前。
initial_facts:
- id: F1
  text: 每个entity group提供可串行化ACID。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 组内提交日志经Paxos同步跨数据中心复制。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 组划得太细增加跨组操作，太大串行化无关写降低吞吐。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 跨组可用高延迟/争用的2PC，通常建议异步queue。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 应用应按自然访问边界分组，在局部事务与跨组成本间取舍。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 跨逻辑组异步不等于同一组物理副本异步。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不将每组少量写入经验阈值外推所有现代数据库。
sources:
- id: S1
  url: https://www.cidrdb.org/cidr2011/Papers/CIDR11_Paper32.pdf
  publisher: Google / Baker et al.
  published_at: '2011'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.cidrdb.org/cidr2011/Papers/CIDR11_Paper32.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 在 entity group 内外选择一致性边界，判断事务范围扩大对延迟和可用性的影响。
```

## ENG-066

```yaml
id: ENG-066
status: sourced
reason: 2019 VS Code原发布说明明确本地UI/远端workspace扩展职责，可运行边界迁移问题。
event: VS Code Remote Development（2019）
cutoff: 2019 Remote Development预览，选择扩展安装/执行位置之前。
initial_facts:
- id: F1
  text: 本地开发工具与远端开发服务共同工作。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 远端VM/容器拥有自己的语言与运行环境。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: UI extensions本地安装，不访问workspace文件。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: Workspace extensions远端运行以访问远端文件系统和工具；openExternal/clipboard应作用于本地。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 分离后IntelliSense、debug等可在远端工具环境运行，同时保留本地交互。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 原文是预览能力及设计说明，不将后续stable功能提前。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 个别扩展可能不兼容，不能声称全部无需改动。
sources:
- id: S1
  url: https://code.visualstudio.com/blogs/2019/05/02/remote-development
  publisher: Microsoft / VS Code team
  published_at: '2019-05-02'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://code.visualstudio.com/blogs/2019/05/02/remote-development
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 编辑器 UI 与执行环境分离时，重建扩展在本地/远端运行的职责边界。
```

## ENG-067

```yaml
id: ENG-067
status: sourced
reason: PostgreSQL13归档官方文档锁定一版MVCC回收规则，可做规范时序而不伪装事故。
event: PostgreSQL MVCC VACUUM（2000s—）
cutoff: PostgreSQL13，一个旧快照仍可能看见已删除版本时。
initial_facts:
- id: F1
  text: UPDATE/DELETE不立即移除旧行版本。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: MVCC需保留其他事务仍可能看到的版本。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: VACUUM可回收已不再被任何事务需要的死版本。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 普通VACUUM通常供内部重用，不像VACUUM FULL重写表主动归还OS空间。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 删除提交不意味着旧版本立即可删或文件立即缩小。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 长期快照是可能原因，不能把所有膨胀唯一归因于长事务。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 没有实际事务ID/日志；Phase4需将规范状态时序明确标为推演。
sources:
- id: S1
  url: https://www.postgresql.org/docs/13/routine-vacuuming.html
  publisher: PostgreSQL project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.postgresql.org/docs/13/routine-vacuuming.html
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 一版 PostgreSQL 中长事务与清理重叠的时序
  anchor_status: unverified_research_target
  main_question: 为何删除已经提交，旧版本占用仍不能立即释放？
  expected_output: 一条可见性到回收受阻的因果链
  evidence_to_verify:
  - 版本
  - 事务快照
  - 清理可回收条件
  out_of_scope: 不将所有表膨胀都归因于同一个长事务
```

## ENG-068

```yaml
id: ENG-068
status: sourced
reason: AWS2021-12-07直接复盘详细记录网络、监控/部署依赖与恢复约束。
event: AWS us-east-1 2021 年 12 月网络事件
cutoff: 2021-12-07 7:30AM PST后内部服务退化、监控不完整时。
initial_facts:
- id: F1
  text: 内部网络承载监控、内部DNS、授权及部分EC2控制面。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 大多数客户应用在主网络上。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 扩容触发连接活动激增，跨网络设备拥塞，重试进一步增加负荷。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 监控与内部部署系统受影响，团队借助日志及逐步隔离流量恢复。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 1:34PM拥塞明显改善，2:22PM网络设备全部恢复，部分服务继续恢复自身能力。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: AWS归因为未适当backoff的潜伏代码路径与网络拥塞；不要判全球客户数据面全停。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 原始内部日志、配置值未公开；不编造。
sources:
- id: S1
  url: https://aws.amazon.com/message/12721/
  publisher: Amazon Web Services
  published_at: '2021-12-10'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://aws.amazon.com/message/12721/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 控制平面与内部网络拥塞导致连锁影响；评估监控和恢复操作的可达性。
```

## ENG-069

```yaml
id: ENG-069
status: blocked
reason: DOJ原发布说明已读，支持Capital One2019事件及WAF配置问题；具体SSRF→凭据→S3链条需可读原complaint，PDF当前仅图片未取得文本。
event: Capital One 云环境泄露（2019）
cutoff: 2019-07-17外部告知潜在泄露后、完整机制调查前。
initial_facts:
- id: F1
  text: GitHub用户向Capital One报告潜在数据盗取。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: Capital One确认入侵后联系FBI。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: DOJ称complaint指控通过配置错误的WAF访问数据。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 搜查后发现包含复制数据的存储设备，属于当时执法方陈述。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 保留指控/观察之别，不以2019公告推定刑事判决。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 原complaint PDF https://www.justice.gov/usao-wdwa/press-release/file/1188626/dl?inline=
  已打开但无可抽取正文，不能宣称已逐页核实技术链。
- 具体IAM权限、SSRF请求及对象访问证据。
sources:
- id: S1
  url: https://www.justice.gov/usao-wdwa/pr/seattle-tech-worker-arrested-data-theft-involving-large-financial-services-company
  publisher: US Department of Justice
  published_at: '2019-07-29'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://www.justice.gov/usao-wdwa/pr/seattle-tech-worker-arrested-data-theft-involving-large-financial-services-company
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 从 SSRF 到云凭据和对象存储访问，分析最小权限与网络过滤的边界。
```

## ENG-070

```yaml
id: ENG-070
status: sourced
reason: Go1.1源码固定tag直接给出G/M/P和blocking syscall移交；候选2012是设计时间，运行工件为2013版，需记录范围修正。
event: Go Scheduler G-M-P 模型（2012）
cutoff: Go1.1实现中已知阻塞系统调用entersyscallblock之前；不混同channel park。
initial_facts:
- id: F1
  text: M为worker线程，P为执行Go代码所需资源。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: M可在没有P时阻塞或处于syscall。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: entersyscallblock将G置Gsyscall，releasep后handoffp。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: exitsyscall优先重新获取旧P，再尝试其他idle P，否则把G放回runnable等待。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 阻塞M不必永久占住P，P可让其他M执行Go代码；返回仍需P才能继续。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 阻塞类型决定路径，不用无工作量输入做容量估计。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 设计文档GDoc仅JavaScript壳、export失败；已用源实现替代并记录版本。
sources:
- id: S1
  url: https://raw.githubusercontent.com/golang/go/go1.1/src/pkg/runtime/proc.c
  publisher: Go project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://raw.githubusercontent.com/golang/go/go1.1/src/pkg/runtime/proc.c
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: G-M-P 候选实现的一次阻塞与唤醒
  anchor_status: unverified_research_target
  main_question: 一个 goroutine 阻塞后，M 与 P 分别发生什么变化？
  expected_output: 标出执行与可调度资源的时序
  evidence_to_verify:
  - 实现版本
  - 阻塞类型
  - M/P 绑定和唤醒规则
  out_of_scope: 不做没有工作量输入的容量估计
```

## ENG-071

```yaml
id: ENG-071
status: blocked
reason: Crossplane Accepted设计正文已读，但该文显式说明部署术语/实现已演变，历史版本合同未锁定，v1.13 tag尝试失败。
event: Crossplane Compositions（2020—2023）
cutoff: 2020–2023中一次Composition输入输出契约快照待锁定。
initial_facts:
- id: F1
  text: 设计目标是将应用需求映射到底层managed resources。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 面向使用者只暴露配置子集。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 原设计示例将底层admin-username映射为对外username连接字段。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 文首说明InfrastructureDefinition/ApplicationDefinition未按原样构建，后来采用CompositeResourceDefinition。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 不能将Accepted文档全部示例当成实际发布API。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- https://raw.githubusercontent.com/crossplane/crossplane/v1.13.0/design/design-doc-composition.md
  cache miss；需可读tag文档或真实Composition/XRD示例。
sources:
- id: S1
  url: https://github.com/crossplane/crossplane/blob/main/design/design-doc-composition.md
  publisher: Crossplane / Nic Cope
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://github.com/crossplane/crossplane/blob/main/design/design-doc-composition.md
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: 一版 Crossplane Composition 的一个输入输出契约
  anchor_status: unverified_research_target
  main_question: 底层云对象变化后，平台使用方哪些字段仍应稳定？
  expected_output: 一个稳定接口边界与不可隐藏的条件
  evidence_to_verify:
  - 版本
  - composition 示例
  - 暴露字段与底层映射
  out_of_scope: 不重新设计 DES-001 的完整资源 API
```

## ENG-072

```yaml
id: ENG-072
status: sourced
reason: LinkedIn2022原开源说明直接声明eventual consistency及active-active复制，不擅自承诺精确延迟。
event: LinkedIn Venice 多区域数据（2022）
cutoff: 2022设计快照，一地区write/ingest完成后、跨区可见性核验之前。
initial_facts:
- id: F1
  text: Venice服务批/流派生数据。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 该系统公开定位为eventually-consistent。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: nearline writes以active-active复制到各区，冲突采用确定性解决。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 行政操作各区异步执行；Da Vinci本地状态通过changelog更新并与服务端最终一致。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 跨区复制存在独立传播阶段，一地完成不能单独证明另一地立即可见。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 完成→立即跨区可见不成立是维护者从复制契约得出的有限推论。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 公开文未给精确写ACK定义或最大复制延迟；询问这些数据时必须答未知。
sources:
- id: S1
  url: https://www.linkedin.com/blog/engineering/open-source/open-sourcing-venice-linkedin-s-derived-data-platform
  publisher: LinkedIn / Félix GV
  published_at: '2022-09-26'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.linkedin.com/blog/engineering/open-source/open-sourcing-venice-linkedin-s-derived-data-platform
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Venice 2022 候选说明的一次区域复制读取
  anchor_status: unverified_research_target
  main_question: 写入在一区完成后，另一区的读取最多能推断什么？
  expected_output: 一个新鲜度边界预测和必要确认点
  evidence_to_verify:
  - 设计快照
  - 写完成定义
  - 复制与读取可见性
  out_of_scope: 不擅自承诺强一致或精确复制延迟
```

## ENG-073

```yaml
id: ENG-073
status: sourced
reason: Meta2022发布说明提供lazy history下载、分段changelog与Git后端限制，足以单一历史操作责任分析。
event: Meta Sapling 版本控制（2022）
cutoff: 2022发布工件中的Sapling专用后端查询，用户尚未下载所需历史时。
initial_facts:
- id: F1
  text: 大型仓库的历史可远大于工作副本。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 发布时只开源client，部分扩展依赖专用server。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: clone几乎不下载历史，后续按需取commit/tree/file。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: Segmented Changelog先下载图的高层形状，再懒取细节；cache/index允许可配置的部分离线流程。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 历史操作的数据与等待责任由本地缓存、图索引和远端按需取回共同承担。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 不能把专用后端优化声称在任意Git仓库可用；离线能力有边界。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 未发布原始延迟轨迹，不编造性能数字。
sources:
- id: S1
  url: https://engineering.fb.com/2022/11/15/open-source/sapling-source-control-scalable/
  publisher: Meta Engineering
  published_at: '2022-11-15'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://engineering.fb.com/2022/11/15/open-source/sapling-source-control-scalable/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: Sapling 2022 候选的一次历史查询操作
  anchor_status: unverified_research_target
  main_question: 这个历史操作的等待和一致性分别由客户端还是后端负责？
  expected_output: 一张操作责任划分及一个离线边界
  evidence_to_verify:
  - 发布说明
  - 该操作数据路径
  - 缓存与服务端约定
  out_of_scope: 不重新设计整个版本控制系统
```

## ENG-074

```yaml
id: ENG-074
status: sourced
reason: Borg2015原论文直接支持资源reservation、优先级与回收取舍。
event: Google Borg 集群超售（2015）
cutoff: 论文资源回收策略选择，在线任务尚未出现负载峰值时。
initial_facts:
- id: F1
  text: 同一cell混合生产与batch等不同优先级任务。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 用户请求资源常高于当前实际使用。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: Borg依细粒度使用估计reservation，回收未用资源给能接受低质量资源的batch。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 高优先级任务可抢占低优先级；线上优先级带内限制相互抢占以防级联。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 提高利用率依赖估计、打包、优先级与允许回收，不能只看资源request总和。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 论文Figure12是一个cell观测，不是所有负载无OOM保证。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不可据此虚构当前cell资源分布或保证任意超售比例。
sources:
- id: S1
  url: https://research.google.com/pubs/archive/43438.pdf
  publisher: Google / Verma et al.
  published_at: '2015'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://research.google.com/pubs/archive/43438.pdf
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 混合在线与批处理工作负载时，评估资源预留、优先级和实际利用率。
```

## ENG-075

```yaml
id: ENG-075
status: sourced
reason: PostgreSQL13官方dedup实现文档支持机制；缺重复分布/页面尺寸，按既定prediction-counterfactual fallback。
event: PostgreSQL B-tree Deduplication（2020）
cutoff: PostgreSQL13重复键索引选择、插入引发去重之前。
initial_facts:
- id: F1
  text: 重复索引tuple可拥有相同key而不同TID。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: B-tree去重可用一个posting list tuple表示一组重复。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: key仅存一次，随后为排序TID数组。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 少/无重复的写密集负载可能只有固定额外成本，deduplicate_items可禁用。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 重复越多通常越有空间收益；重复减少时收益缩小，不能在无数据分布下估具体倍数。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 索引缩小不自动证明特定查询更快。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 原规划一组真实重复键与尺寸未给；采用定性备用题，非补合成数。
sources:
- id: S1
  url: https://www.postgresql.org/docs/13/btree-implementation.html
  publisher: PostgreSQL project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.postgresql.org/docs/13/btree-implementation.html
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  planning_only: true
  anchor_request: PostgreSQL 2020 候选去重版本的一组重复键
  anchor_status: unverified_research_target
  main_question: 这组重复键的索引空间会减少到什么数量级？
  expected_output: 一个范围估计及其不适用分布
  evidence_to_verify:
  - 版本
  - 重复键分布
  - 页面或索引尺寸口径
  out_of_scope: 不把索引缩小直接等同查询更快
  quantitative_plan:
    mainline_measure: 索引体积变化数量级
    required_inputs:
    - 重复键分布
    - 页面或索引尺寸
    - 对应版本机制
    missing_input_fallback:
      focus: prediction-counterfactual
      question: 重复键变少后，去重对空间的作用将如何变化？
    fallback_applied: false
    input_verification: partial_source_check_see_unknowns
```

## ENG-076

```yaml
id: ENG-076
status: sourced
reason: Atlassian2022完整PIR支持app/site ID误删、备份与跨产品恢复差异。
event: Atlassian 2022 年云服务恢复事故
cutoff: 2022-04-05误删后已定位脚本、评估恢复路径之前。
initial_facts:
- id: F1
  text: 维护意图为删除旧Insight应用。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 删除API同时接受site和app标识，输入类型未二次确认。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 错误site ID导致删除883站点，涉及775客户。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 备份可恢复个别存储，但大批站点跨产品协调恢复缺少已自动化runbook。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 全部客户4月18日恢复，部分停用达14天；作者报告RTO失守、RPO满足。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 存在备份≠快速恢复完整服务，恢复包含身份/依赖与重新供应。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- PIR记录部分早期恢复点不一致后补救；不能简化为所有站点初次恢复都无数据差异。
sources:
- id: S1
  url: https://www.atlassian.com/blog/how-we-build/post-incident-review-april-2022-outage
  publisher: Atlassian
  published_at: '2022-04-29'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://www.atlassian.com/blog/how-we-build/post-incident-review-april-2022-outage
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 维护脚本错误移除站点资源且恢复耗时；判断数据恢复与重新供应的不同边界。
```

## ENG-077

```yaml
id: ENG-077
status: sourced
reason: Kubernetes官方CVE issue提供升级连接绕过认证授权、受影响路径与修复版本。
event: Kubernetes CVE-2018-1002105
cutoff: 2018受影响apiserver代理upgrade请求后，未授权后续请求进入既有连接前。
initial_facts:
- id: F1
  text: apiserver代理连接到kubelet或聚合API后端。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 调用者可能只获discovery或pod exec等有限权限。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 漏洞让错误响应后的backend TCP连接继续暴露给调用者。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 后续请求使用apiserver连接身份，不再经过原来的独立授权，且不进入apiserver审计日志。
  source_ids:
  - S1
  availability: post_decision
outcome:
  id: O1
  text: 官方列出聚合API及kubelet权限提升风险并建议升级修复版本。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 不是所有路径都要求同等认证；匿名discovery情形和已授权exec需分别说明。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 不能声称已有实际利用；公告明确没有简单审计检测方法。
sources:
- id: S1
  url: https://github.com/kubernetes/kubernetes/issues/71411
  publisher: Kubernetes / Jordan Liggitt
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://github.com/kubernetes/kubernetes/issues/71411
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 分析 API Server 权限提升链条，区分认证、授权与升级连接协议的信任边界。
```

## ENG-078

```yaml
id: ENG-078
status: sourced
reason: Go1.5设计者同期文章直接解释三色标记与write barrier不变量。
event: Go GC Concurrent Mark Sweep（2015）
cutoff: Go1.5并发标记时mutator准备修改堆指针之前。
initial_facts:
- id: F1
  text: collector与mutator同时工作。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 黑对象表示已扫描，白对象仍待证明可达。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: write barrier维护黑对象不能直接指向白对象的不变量。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: Go1.5将新可达白对象染灰，并仍短暂停世界检查剩余灰色来源。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  id: O1
  text: 并发标记用mutator写屏障成本换取较短STW阶段，并未消除所有GC开销。
  source_ids:
  - S1
  availability: post_decision
interpretation:
  text: 采用2015屏障机制，不混入后来hybrid barrier。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 没有固定工作负载，不能精算吞吐损失。
sources:
- id: S1
  url: https://go.dev/blog/go15gc
  publisher: Go / Richard Hudson
  published_at: '2015-08-31'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
attempts:
- url: https://go.dev/blog/go15gc
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  scope: 从 stop-the-world 转向并发标记时，推理 write barrier 对暂停与吞吐的影响。
```

## ENG-079

```yaml
id: ENG-079
status: sourced
reason: Kubernetesv1.21.0源码固定tag明确EndpointSlice pending/applied缓存及回调队列，支持非即时生效。
event: Kubernetes EndpointSlice 传播（2019—2021）
cutoff: v1.21.0某EndpointSlice变更已经进cache但proxier尚未应用时；限定iptables数据面。
initial_facts:
- id: F1
  text: kube-proxy按service及slice跟踪endpoint。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 缓存区分已由proxier应用与pending的EndpointSlice。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: slice内endpoint移动需要按slice缓存，避免错误删除。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: iptables proxier的OnEndpointSliceDelete/Update先更新endpointsChanges，再触发Sync；syncRunner与syncProxyRules负责后续应用。
  source_ids:
  - S1
  - S2
  availability: pre_decision
outcome:
  id: O1
  text: 控制面更新与本地数据面应用之间可存在间隔；旧路径可在更新传播完成前继续存在。
  source_ids:
  - S1
  - S2
  availability: post_decision
interpretation:
  text: 旧路径存在是从分阶段实现推导的可能性，不是某次真实生产请求已证明；不承诺最长传播时间。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 新请求路由与已有连接需区分；全局所有节点生效需要各节点观测，单次API ACK不足。
sources:
- id: S1
  url: https://raw.githubusercontent.com/kubernetes/kubernetes/v1.21.0/pkg/proxy/endpointslicecache.go
  publisher: Kubernetes project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
  - O1
- id: S2
  url: https://raw.githubusercontent.com/kubernetes/kubernetes/v1.21.0/pkg/proxy/iptables/proxier.go
  publisher: Kubernetes project
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E2
  - O1
attempts:
- url: https://raw.githubusercontent.com/kubernetes/kubernetes/v1.21.0/pkg/proxy/endpointslicecache.go
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
- url: https://raw.githubusercontent.com/kubernetes/kubernetes/v1.21.0/pkg/proxy/iptables/proxier.go
  result: 已打开并读取v1.21.0回调、同步及conntrack清理注释
phase2_conditions:
  planning_only: true
  anchor_request: 一版 EndpointSlice 中的一次 endpoint 删除
  anchor_status: unverified_research_target
  main_question: 控制面确认删除后，一条旧请求路径是否还可能被使用？
  expected_output: 一个传播时序与能证明生效的观察点
  evidence_to_verify:
  - 版本
  - 控制面确认语义
  - 数据面刷新路径
  out_of_scope: 不把多组件异步传播写成全局即时生效
```
