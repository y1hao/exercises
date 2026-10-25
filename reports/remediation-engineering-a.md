# Phase 3 admission remediation — ENG-001–079

Checked 2026-10-25. Maintenance notes only; not Phase 4 Briefs, no ready promotion. Eligible means material is sufficient to author a Brief, not dialogue QA. New scope decisions are explicit; existing verified records preserve prior checks.

## ENG-001

```yaml
id: ENG-001
decision: retain
scenario_title: Google Spanner（2012）
focus: causal-modeling
subdomain: distributed-consistency
main_question: 面对跨地区事务与外部一致性需求，判断 TrueTime 的时钟不确定性如何影响提交等待。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Google Spanner（2012）的单一范围；不要求实际练习不提供未经核实的逐次时钟值。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：面对跨地区事务与外部一致性需求，判断 TrueTime 的时钟不确定性如何影响提交等待。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-002

```yaml
id: ENG-002
decision: reframe
scenario_title: Docker 多阶段构建缓存教程（2019-07-02）
focus: prediction-counterfactual
subdomain: developer-tooling-build
main_question: 仅 pom.xml 改动时，缓存失效从哪个步骤传播到哪些后续步骤？
expected_output: 在官方示例顺序上标出重建起点、传播范围及源码独改的对照
out_of_scope: 不声称是2018 BuildKit具体实现，不估镜像体积
reason: 2018候选版本未证实；正式改锚2019同期官方Maven教程，不填造Dockerfile或依赖。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：仅 pom.xml 改动时，缓存失效从哪个步骤传播到哪些后续步骤？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-002
  status: sourced
  reason: 2018候选版本未证实；正式改锚2019同期官方Maven教程，不填造Dockerfile或依赖。
  event: Docker 多阶段构建缓存教程（2019-07-02）
  cutoff: 2019-07-02公开教程中已给定Dockerfile顺序、尚未预测修改结果
  initial_facts:
  - id: F1
    text: 示例以 Maven/JDK 构建 Java 应用。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: pom.xml 与 src 分开复制，依赖获取位于其间。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 一个步骤因输入改变失去缓存会使后续步骤重建。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 依赖获取单独成层，只依赖 pom.xml；最终阶段从 builder 复制产物。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 示例把依赖下载与源码编译分离，源码单改可复用依赖层；改清单仍使依赖层及后续构建失效。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - Dockerfile图示以官方例子为准，不补造未公开构建日志。
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
    - O1
  attempts:
  - url: https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
      planning_only: true
      anchor_request: BuildKit 2018 候选窗口的一份多阶段 Dockerfile，具体版本待核
      anchor_status: unverified_research_target
      main_question: 只修改依赖清单后，哪一层起需要重建？
      expected_output: 标出缓存失效起点及一次可验证预测
      evidence_to_verify:
      - 当时 Dockerfile 示例
      - 层输入与缓存键语义
      out_of_scope: 不同时估镜像体积或重写整个构建流程
    remediation_applied: true
    scope_change: 2018候选版本未证实；正式改锚2019同期官方Maven教程，不填造Dockerfile或依赖。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-003

```yaml
id: ENG-003
decision: retain
scenario_title: Slack 2021 年 1 月服务中断
focus: evidence-selection
subdomain: reliability-diagnosis
main_question: 新年首个工作日请求增长伴随后台资源问题；在有限指标下排列调查优先级。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Slack 2021 年 1 月服务中断的单一范围；不要求未提供逐台机器原始日志；不得编造。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：新年首个工作日请求增长伴随后台资源问题；在有限指标下排列调查优先级。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-004

```yaml
id: ENG-004
decision: reframe
scenario_title: Terraform v1.5.0 状态升级责任边界（2023）
focus: boundary-transfer
subdomain: architecture-api
main_question: 旧状态进入新 provider 时，Core 与 provider 各承担什么转换责任，哪些改动不能夹带？
expected_output: 划分一次UpgradeResourceState与ReadResource的责任，并指出违反语义的转换
out_of_scope: 不综述七年协议，不把Framework现行例子回填历史
reason: 以已读v1.5.0官方固定tag生命周期契约替代未锁定的2016—2023泛称；保留状态升级单一问题。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：旧状态进入新 provider 时，Core 与 provider 各承担什么转换责任，哪些改动不能夹带？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-004
  status: sourced
  reason: 以已读v1.5.0官方固定tag生命周期契约替代未锁定的2016—2023泛称；保留状态升级单一问题。
  event: Terraform v1.5.0 状态升级责任边界（2023）
  cutoff: Terraform v1.5.0设计工件，调用UpgradeResourceState前
  initial_facts:
  - id: F1
    text: 状态快照会跨run保留。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 用户可能升级provider，而资源schema与旧状态不兼容。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: Core将原始旧状态交给UpgradeResourceState，并不掌握旧schema。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: ReadResource另负责检测远端变化；schema升级应保留信息含义。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 契约将旧状态解码与形状转换交给provider；返回与当前schema相容但语义不变的Upgraded State。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 不提供虚构provider故障或旧新字段数据；使用文档规定的操作合同。
  sources:
  - id: S1
    url: https://github.com/hashicorp/terraform/blob/v1.5.0/docs/resource-instance-change-lifecycle.md
    publisher: HashiCorp / Terraform maintainers
    published_at: '2023'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://developer.hashicorp.com/terraform/plugin/framework/resources/state-upgrade
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://github.com/hashicorp/terraform/blob/v1.5.0/docs/resource-instance-change-lifecycle.md
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 以已读v1.5.0官方固定tag生命周期契约替代未锁定的2016—2023泛称；保留状态升级单一问题。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-005

```yaml
id: ENG-005
decision: reframe
scenario_title: JDK 11 实验性 ZGC 的采用边界（2018）
focus: constrained-decision
subdomain: runtime-concurrency
main_question: 仅因暂停目标与堆大小符合发布目标，就应直接采用这版ZGC吗？
expected_output: 给出试用/推迟决定，并用一项平台或机制限制说明推翻条件
out_of_scope: 不把设计目标当实测SLO，不虚构同口径吞吐结果，不混入分代ZGC
reason: JEP403缺口由Oracle JDK11同期release notes补齐；把需要未知负载基准的决定改为受明确支持边界约束的试用决策。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：仅因暂停目标与堆大小符合发布目标，就应直接采用这版ZGC吗？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-005
  status: sourced
  reason: JEP403缺口由Oracle JDK11同期release notes补齐；把需要未知负载基准的决定改为受明确支持边界约束的试用决策。
  event: JDK 11 实验性 ZGC 的采用边界（2018）
  cutoff: JDK11发布说明工件，2018版采用评估前
  initial_facts:
  - id: F1
    text: ZGC随JDK11作为实验性功能提供。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 该版本的目标包括低暂停和大堆支持。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 昂贵的标记、压缩等工作并发进行。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 初始版仅Linux/x64，且不支持类卸载、compressed oops及Graal组合。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 发布要求显式解锁实验选项；满足目标本身不消除版本支持限制，也不保证某服务达标。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 10ms是发布所述目标，不是此练习测得的任意服务暂停；没有生产SLO数据。
  sources:
  - id: S1
    url: https://www.oracle.com/java/technologies/javase/11-relnote-issues.html
    publisher: Oracle / JDK11 release notes
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
  - url: https://openjdk.org/jeps/333
    result: 两次open均403，未读取原文
  - url: https://www.oracle.com/java/technologies/javase/11-relnote-issues.html
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: JEP403缺口由Oracle JDK11同期release notes补齐；把需要未知负载基准的决定改为受明确支持边界约束的试用决策。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-006

```yaml
id: ENG-006
decision: reframe
scenario_title: Figma 并发属性更新模型（2019）
focus: hypothesis-diagnosis
subdomain: data-storage
main_question: 两端编辑同一对象时，如何判别是属性级覆盖还是文档整体覆盖？
expected_output: 用同对象不同属性和同属性的两组对照，给出各自预期收敛结果
out_of_scope: 不要求未公开的持久化ACK语义，不设计完整同步系统
reason: 原持久化确认问题缺公开契约；改为2019原文直接公开的属性级冲突诊断，同一公司同一工件，无补造日志。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：两端编辑同一对象时，如何判别是属性级覆盖还是文档整体覆盖？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-006
  status: sourced
  reason: 原持久化确认问题缺公开契约；改为2019原文直接公开的属性级冲突诊断，同一公司同一工件，无补造日志。
  event: Figma 并发属性更新模型（2019）
  cutoff: 2019-10-16公开模型，比较属性级与文档级覆盖之前
  initial_facts:
  - id: F1
    text: 文档是有ID的对象树，每个对象有多项属性。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 客户端经WebSocket接入文档的中心服务器。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 不同对象或同对象不同属性的更新不冲突。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 同一对象同一属性按到达服务器的顺序确定最后值。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 原文AB与BC并发编辑的文本属性结果可为AB或BC，不能据该模型合并成ABC；原子边界是属性值。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 同步到另一端不代表已核实持久化；该契约仍未知且不作为题目输入。
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
    - O1
  attempts:
  - url: https://www.figma.com/blog/how-figmas-multiplayer-technology-works/
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://www.figma.com/blog/how-figmas-multiplayer-technology-works/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 原持久化确认问题缺公开契约；改为2019原文直接公开的属性级冲突诊断，同一公司同一工件，无补造日志。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-007

```yaml
id: ENG-007
decision: reframe
scenario_title: SolarWinds SUNSPOT 构建注入取证（2021-01披露）
focus: evidence-selection
subdomain: security-isolation
main_question: 仓库检出的源码正常时，应比较哪一处构建过程证据才能检验编译期注入？
expected_output: 选择编译输入与构建前后文件的一项对照，写明能区分的两个假说
out_of_scope: 不提供攻击操作教程，不假定独立重建当时可用，不讨论横向移动
reason: 签名验证不能直接证明源代码未被临时替换；将问题收窄为调查方实际分析工件上的构建期证据，避免未核独立重建。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：仓库检出的源码正常时，应比较哪一处构建过程证据才能检验编译期注入？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-007
  status: sourced
  reason: 签名验证不能直接证明源代码未被临时替换；将问题收窄为调查方实际分析工件上的构建期证据，避免未核独立重建。
  event: SolarWinds SUNSPOT 构建注入取证（2021-01披露）
  cutoff: 2021-01-11调查报告材料快照，在根据构建样本判断注入路径前
  initial_facts:
  - id: F1
    text: 调查针对Orion构建环境中的恶意工具SUNSPOT。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 正常编译任务由MsBuild.exe执行。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 样本监测MsBuild命令行中的Orion解决方案路径。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 分析显示源文件先被备份/替换，编译结束后再恢复。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: CrowdStrike在其受托调查中判定SUNSPOT临时替换InventoryManager.cs，使标准编译产物含SUNBURST；这是调查归因而非本项目独立复现。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 攻击者全部初始入口未知；未证实客户能在当时自行独立复现构建。
  sources:
  - id: S1
    url: https://www.crowdstrike.com/en-us/blog/sunspot-malware-technical-analysis/
    publisher: CrowdStrike Intelligence Team
    published_at: '2021-01-11'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://www.solarwinds.com/blog/new-findings-from-our-investigation-of-sunburst
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://www.crowdstrike.com/en-us/blog/sunspot-malware-technical-analysis/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 签名验证不能直接证明源代码未被临时替换；将问题收窄为调查方实际分析工件上的构建期证据，避免未核独立重建。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-008

```yaml
id: ENG-008
decision: reframe
scenario_title: Discord Read States GC 尖峰复盘（2020公开）
focus: hypothesis-diagnosis
subdomain: performance-cost
main_question: 下一项观测如何区分 GC 暂停与非 GC 的等待？
expected_output: 列出两个竞争解释并选择区分它们的一项观测
out_of_scope: 不把迁移 Rust 当作预定结论
reason: 将未核实2019事故日纠正为2020-02-04公开复盘；保留其周期抖动诊断工件，不推定具体生产发生日。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：下一项观测如何区分 GC 暂停与非 GC 的等待？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-008
  status: sourced
  reason: 将未核实2019事故日纠正为2020-02-04公开复盘；保留其周期抖动诊断工件，不推定具体生产发生日。
  event: Discord Read States GC 尖峰复盘（2020公开）
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
    remediation_scope: 将未核实2019事故日纠正为2020-02-04公开复盘；保留其周期抖动诊断工件，不推定具体生产发生日。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-009

```yaml
id: ENG-009
decision: retain
scenario_title: Raft 论文（2014）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: 在Raft Figure8的旧任期条目已有多数副本时，若领导者崩溃，能否断言该条目不会被覆写？
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Raft 论文（2014）的单一范围；不要求需在 Phase4 对照原图逐项转录日志状态。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：在Raft Figure8的旧任期条目已有多数副本时，若领导者崩溃，能否断言该条目不会被覆写？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-010

```yaml
id: ENG-010
decision: retain
scenario_title: Go Modules 引入（2018）
focus: causal-modeling
subdomain: developer-tooling-build
main_question: 按2018原文依赖图计算MVS构建列表：为何同一模块取所需最高版本却不自动追逐所有最新版？
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Go Modules 引入（2018）的单一范围；不要求训练需使用原图依赖而非臆造历史依赖。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：按2018原文依赖图计算MVS构建列表：为何同一模块取所需最高版本却不自动追逐所有最新版？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-011

```yaml
id: ENG-011
decision: reframe
scenario_title: Cloudflare PDX01 双路供电失效（2024-03-26）
focus: constrained-decision
subdomain: reliability-diagnosis
main_question: 两路电源还可能共享什么失效点，下一步应验证哪一处？
expected_output: 一项冗余验证决策及其共同原因假说
out_of_scope: 不合并两年事故；找不到独立事件则申请换题
reason: 只保留已核实2024独立事件；2023只作当时已知改进背景，与ENG040分开，不把4月发布日写成事故日。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：两路电源还可能共享什么失效点，下一步应验证哪一处？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-011
  status: sourced
  reason: 只保留已核实2024独立事件；2023只作当时已知改进背景，与ENG040分开，不把4月发布日写成事故日。
  event: Cloudflare PDX01 双路供电失效（2024-03-26）
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
    remediation_scope: 只保留已核实2024独立事件；2023只作当时已知改进背景，与ENG040分开，不把4月发布日写成事故日。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-012

```yaml
id: ENG-012
decision: reframe
scenario_title: Protocol Buffers proto2 字段号复用边界（2026固定规范）
focus: prediction-counterfactual
subdomain: architecture-api
main_question: 删掉SearchRequest中的可选page_number字段后，把其编号2给另一含义的字段会怎样影响新旧读写者？
expected_output: 预测旧消息/旧读者的错读风险，并选择字段号或字段名reservation的适用边界
out_of_scope: 不声称是2008特定部署，不混合二进制与JSON/TextFormat保证
reason: 现行proto2说明已核实但不能追溯为2008；正式固定2026-10-19文档commit d056cc7的真实SearchRequest/删除字段工件。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：删掉SearchRequest中的可选page_number字段后，把其编号2给另一含义的字段会怎样影响新旧读写者？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-012
  status: sourced
  reason: 现行proto2说明已核实但不能追溯为2008；正式固定2026-10-19文档commit d056cc7的真实SearchRequest/删除字段工件。
  event: Protocol Buffers proto2 字段号复用边界（2026固定规范）
  cutoff: 文档commit d056cc774b257d185b39400a8e4c90f6ca330297的proto2契约，变更schema之前
  initial_facts:
  - id: F1
    text: 规范SearchRequest示例含optional int32 page_number=2。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 字段号标识wire格式中的字段，不能随在用schema任意重编号。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 删除非required字段后应保留其编号，编译器拒绝复用reserved编号。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 字段名在JSON/TextFormat有独立兼容意义；二进制wire-safe也可能破坏语言层exhaustive enum switch。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 该固定规范要求分清wire解析、源码编译及文本编码边界；删除后复用旧号不是安全演进。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 这是有日期的真实规范修订，不是虚构2008事故；不制造真实客户端升级日志。
  sources:
  - id: S1
    url: https://raw.githubusercontent.com/protocolbuffers/protocolbuffers.github.io/d056cc774b257d185b39400a8e4c90f6ca330297/content/programming-guides/proto2.md
    publisher: Protocol Buffers maintainers
    published_at: '2026-10-19'
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
  - url: https://raw.githubusercontent.com/protocolbuffers/protocolbuffers.github.io/d056cc774b257d185b39400a8e4c90f6ca330297/content/programming-guides/proto2.md
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
      scope: 客户端与服务器独立演进时，预测删除字段、改变编号、增加枚举值造成的兼容性风险。
    remediation_applied: true
    scope_change: 现行proto2说明已核实但不能追溯为2008；正式固定2026-10-19文档commit d056cc7的真实SearchRequest/删除字段工件。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-013

```yaml
id: ENG-013
decision: retain
scenario_title: JVM Double-Checked Locking 语义修订（2004）
focus: hypothesis-diagnosis
subdomain: runtime-concurrency
main_question: 用 Java 内存模型重审惰性单例初始化，辨别排序与可见性保证。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留JVM Double-Checked Locking 语义修订（2004）的单一范围；不要求FAQ后修订删除过性能评价；不采用被划掉的性能结论。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：用 Java 内存模型重审惰性单例初始化，辨别排序与可见性保证。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-014

```yaml
id: ENG-014
decision: reframe
scenario_title: RocksDB Universal Compaction 2023 设计说明
focus: constrained-decision
subdomain: data-storage
main_question: 写放大已是瓶颈但磁盘空间紧张，能否仅凭较低写放大就选择Universal？
expected_output: 作出有条件的策略选择，说明读放大与major compaction临时空间的否决条件
out_of_scope: 不估未给出的生产吞吐，不将2023工件写成2013具体上线
reason: 官方wiki明确2023-06-29修订；固定该说明的sorted runs与空间契约，修正原候选2013未证实首次实现。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：写放大已是瓶颈但磁盘空间紧张，能否仅凭较低写放大就选择Universal？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-014
  status: sourced
  reason: 官方wiki明确2023-06-29修订；固定该说明的sorted runs与空间契约，修正原候选2013未证实首次实现。
  event: RocksDB Universal Compaction 2023 设计说明
  cutoff: 2023-06-29 wiki设计工件，选择compaction策略前
  initial_facts:
  - id: F1
    text: Universal把多个相邻时间段的sorted runs合并。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 该策略目标是减轻写放大。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 延迟合并使读时可能面对更多sorted runs及更大性能波动。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: major compaction前后同时保留输入与输出可使column family临时空间接近翻倍。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 该策略把写放大收益与读放大、空间峰值交换；是否合适依约束，不是无条件升级。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 未给真实负载和磁盘余量，训练应给出条件边界，不替用户编容量。
  sources:
  - id: S1
    url: https://github.com/facebook/rocksdb/wiki/Universal-Compaction
    publisher: RocksDB maintainers / Changyu Bi
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
  - url: https://github.com/facebook/rocksdb/wiki/Universal-Compaction
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
      scope: 写密集系统选择 compaction 策略时，比较写放大、空间峰值与查询延迟。
    remediation_applied: true
    scope_change: 官方wiki明确2023-06-29修订；固定该说明的sorted runs与空间契约，修正原候选2013未证实首次实现。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-015

```yaml
id: ENG-015
decision: reframe
scenario_title: Cloudflare 支持工单会话令牌事件（2023-10-18）
focus: evidence-selection
subdomain: security-isolation
main_question: 当前只能先核验一类凭据，应按什么暴露路径排序？
expected_output: 一个优先对象及可改变排序的证据
out_of_scope: 不提前给后续入侵结果或借用 Okta 案例事实
reason: 将OAuth候选纠正为原文session/authentication token；不借用11月后续入侵事件。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：当前只能先核验一类凭据，应按什么暴露路径排序？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-015
  status: sourced
  reason: 将OAuth候选纠正为原文session/authentication token；不借用11月后续入侵事件。
  event: Cloudflare 支持工单会话令牌事件（2023-10-18）
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
    published_at: '2023-10-20'
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
    remediation_scope: 将OAuth候选纠正为原文session/authentication token；不借用11月后续入侵事件。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-016

```yaml
id: ENG-016
decision: reframe
scenario_title: Uber H3 地理索引（2018）
focus: constrained-decision
subdomain: performance-cost
main_question: 以定价聚合位置事件时，层级六角单元比邮编区域提供什么一致的分析边界，又不能保证什么精度？
expected_output: 一个索引选择及其不适用条件
out_of_scope: 不要求未知误差阈值，不计算无来源距离误差或设计全球位置平台
reason: 保留2018当事人设计材料；撤去原问题未提供的允许误差阈值，单问公开的聚合边界。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：以定价聚合位置事件时，层级六角单元比邮编区域提供什么一致的分析边界，又不能保证什么精度？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-017

```yaml
id: ENG-017
decision: reframe
scenario_title: Redis Cluster 3.0.0 ASK 与 MOVED（2015）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: 迁移中的slot对一个尚未迁走/已经迁走的key，会返回什么，客户端应永久改映射吗？
expected_output: 分别预测源节点仍有key与缺key时的路由，并解释ASKING单请求范围
out_of_scope: 限定单key、非MULTI请求，不扩展为任意跨key事务或全局一致性
reason: 补读Redis3.0.0 cluster.c与networking.c，原2015候选现已固定到具体源码。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：迁移中的slot对一个尚未迁走/已经迁走的key，会返回什么，客户端应永久改映射吗？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-017
  status: sourced
  reason: 补读Redis3.0.0 cluster.c与networking.c，原2015候选现已固定到具体源码。
  event: Redis Cluster 3.0.0 ASK 与 MOVED（2015）
  cutoff: Redis3.0.0 slot处于MIGRATING/IMPORTING、一个普通单key请求到达源节点前
  initial_facts:
  - id: F1
    text: slot由源节点迁向目标，迁移期间源节点可能仍持有部分key。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 目标的IMPORTING状态需要客户端显式ASKING后才按迁移例外处理请求。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: getNodeByQuery在MIGRATING且缺key时返回ASK目标，而稳定非本地slot返回MOVED。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: resetClient在非MULTI且上一命令不是ASKING本身时清掉ASKING标记。
    source_ids:
    - S2
    availability: pre_decision
  outcome:
    id: O1
    text: ASK允许下一普通请求临时访问目标，不能据此永久认定slot归属已经迁完；迁完的MOVED才代表稳定路由变化。
    source_ids:
    - S1
    - S2
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - MULTI例外已排除；具体生产迁移日志及客户端实现不在材料中。
  sources:
  - id: S1
    url: https://raw.githubusercontent.com/redis/redis/3.0.0/src/cluster.c
    publisher: Redis maintainers
    published_at: '2015'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - O1
  - id: S2
    url: https://raw.githubusercontent.com/redis/redis/3.0.0/src/networking.c
    publisher: Redis maintainers
    published_at: '2015'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
    - O1
  attempts:
  - url: https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://raw.githubusercontent.com/redis/redis/3.0.0/src/cluster.c
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  - url: https://raw.githubusercontent.com/redis/redis/3.0.0/src/networking.c
    result: CLI实际读取resetClient对REDIS_ASKING清理的条件。
  phase2_conditions:
    original:
      scope: 迁移 hash slots 时如何处理重定向、并发写和暂时不一致，检验客户端模型。
    remediation_applied: true
    scope_change: 补读Redis3.0.0 cluster.c与networking.c，原2015候选现已固定到具体源码。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-018

```yaml
id: ENG-018
decision: retain
scenario_title: CircleCI Dynamic Config（2021）
focus: constrained-decision
subdomain: developer-tooling-build
main_question: 大型 CI 流水线需按变更选择任务时，权衡静态配置与生成配置的可测试性。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留CircleCI Dynamic Config（2021）的单一范围；不要求不借用2023默认启用规则作为2021事实。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：大型 CI 流水线需按变更选择任务时，权衡静态配置与生成配置的可测试性。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-019

```yaml
id: ENG-019
decision: retain
scenario_title: Cloudflare 2025 年 8 月 AWS 互联拥塞
focus: hypothesis-diagnosis
subdomain: reliability-diagnosis
main_question: 哪项地域对照最能区分链路问题与应用自身故障？
expected_output: 两个假说与一项区分性观测
out_of_scope: 不假定全球故障或预先确认拥塞根因
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Cloudflare 2025 年 8 月 AWS 互联拥塞的单一范围；不要求无逐包数据；容量图为近似估计，不当作精确链路测量。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：哪项地域对照最能区分链路问题与应用自身故障？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-020

```yaml
id: ENG-020
decision: reframe
scenario_title: Compose UI 1.4.3 TextField 同步状态反馈工件
focus: causal-modeling
subdomain: architecture-api
main_question: 在onValueChange里先等异步用户名校验再更新value，为何可能出现丢字与光标错乱？
expected_output: 重建输入、状态持有者和内部控制器反馈链，指出应移动的异步边界
out_of_scope: 不将旧value-based API规则外推到后来TextFieldState接口，不设计整个UI框架
reason: 原2021锚点未锁定，正式改为Android Developers作者明确标明Compose UI1.4.3的真实故障演示工件，替代泛泛单向流讲解。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：在onValueChange里先等异步用户名校验再更新value，为何可能出现丢字与光标错乱？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-020
  status: sourced
  reason: 原2021锚点未锁定，正式改为Android Developers作者明确标明Compose UI1.4.3的真实故障演示工件，替代泛泛单向流讲解。
  event: Compose UI 1.4.3 TextField 同步状态反馈工件
  cutoff: Compose UI1.4.3的文中示例工件，观察异步校验导致异常之前
  initial_facts:
  - id: F1
    text: 示例TextField以value显示状态、用onValueChange回传编辑。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 用户名需要异步业务校验，示例把状态放入ViewModel。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 作者明确该版本有IME、用户state holder、内部controller三份需要同步的状态。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 示例在更新state前延后，旧异步结果可覆盖新输入；即使默认dispatcher的flow收集也有延迟边界。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 作者演示丢字、重复与光标问题，并把TextField状态同步立即更新，异步校验另行调度；这是指定旧版示例，不是所有响应式状态都错误。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 文章后更新明确写1.4.3但该段修订日未知；不把所有现文都声称2022首发已知，排除2025新API结论。
  sources:
  - id: S1
    url: https://medium.com/androiddevelopers/effective-state-management-for-textfield-in-compose-d6e5b070fbe5
    publisher: Android Developers / Alejandra Stamato
    published_at: '2022-09-14'
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
  - url: https://medium.com/androiddevelopers/effective-state-management-for-textfield-in-compose-d6e5b070fbe5
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
      scope: 从命令式 UI 转向声明式 UI，检查状态单向流动对组件边界的影响。
    remediation_applied: true
    scope_change: 原2021锚点未锁定，正式改为Android Developers作者明确标明Compose UI1.4.3的真实故障演示工件，替代泛泛单向流讲解。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-021

```yaml
id: ENG-021
decision: reframe
scenario_title: PEP 703 有条件接受与渐进发布（2023-10-24）
focus: boundary-transfer
subdomain: runtime-concurrency
main_question: 对仍依赖C扩展的生产服务，接受提案是否已经足以支持切换默认运行模式？
expected_output: 区分提案接受、实验可用与生产支持三条边界，并提出一条可改变采用决定的兼容证据
out_of_scope: 不引用2024以后落地结果，不要求虚构CPU基准或具体服务负载
reason: 不使用现行PEP回填2023，改锚2023-10-24 Steering Council同期明确声明的采用边界。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：对仍依赖C扩展的生产服务，接受提案是否已经足以支持切换默认运行模式？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-021
  status: sourced
  reason: 不使用现行PEP回填2023，改锚2023-10-24 Steering Council同期明确声明的采用边界。
  event: PEP 703 有条件接受与渐进发布（2023-10-24）
  cutoff: 2023-10-24接受公告中的阶段规划，后续实现与生态结果未知
  initial_facts:
  - id: F1
    text: 提案旨在允许可选无GIL构建。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: C扩展生态与既有CPython高效集成是重要兼容约束。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 委员会称没有完成实现时难以评估扩展适配，线程问题可能仅在高负载暴露。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 首阶段明确实验、不得默认安装且不支持生产；后续支持/默认需另作决定。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 委员会接受提案但要求渐进且可回退，保留因破坏性或可维护性问题逆转整项工作的可能。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 公告预期性能代价不是测得生产基准；不把预期百分比当已实现结果。
  sources:
  - id: S1
    url: https://discuss.python.org/t/pep-703-making-the-global-interpreter-lock-optional-in-cpython-acceptance/37075
    publisher: Python Steering Council / Thomas Wouters
    published_at: '2023-10-24'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://peps.python.org/pep-0703/
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://discuss.python.org/t/pep-703-making-the-global-interpreter-lock-optional-in-cpython-acceptance/37075
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 不使用现行PEP回填2023，改锚2023-10-24 Steering Council同期明确声明的采用边界。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-022

```yaml
id: ENG-022
decision: reframe
scenario_title: LevelDB 1.22 的 L0 积压与压缩工件
focus: prediction-counterfactual
subdomain: data-storage
main_question: 写入持续快于后台压缩时，为什么读放大会先随L0积压而变坏？
expected_output: 沿memtable、L0重叠文件与合并路径预测，并给出节流的代价边界
out_of_scope: 不以文档举例磁盘速率冒充生产测量，不声称1.22即2011首发实现
reason: 已CLI读取官方1.22固定tag impl.md，正式冻结此实现而非main/模糊2011版本。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：写入持续快于后台压缩时，为什么读放大会先随L0积压而变坏？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-022
  status: sourced
  reason: 已CLI读取官方1.22固定tag impl.md，正式冻结此实现而非main/模糊2011版本。
  event: LevelDB 1.22 的 L0 积压与压缩工件
  cutoff: LevelDB1.22实现工件，后台compaction跟不上新增L0文件前
  initial_facts:
  - id: F1
    text: 写入先进入log与memtable。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 旧memtable刷成L0 SST文件，L0文件键范围可重叠。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 超限压缩会合并本层与下层重叠文件。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: impl.md解释后台写被节流时L0可积压，读取需合并更多文件，并提出限制前台写速率。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 该实现文档展示压缩、读路径与节流的权衡；更快接收写入并非在压缩受限时免费提高整体吞吐。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 文档中的磁盘速率和L0积压计算是作者说明例子，非某次生产日志，不外推为硬件测量。
  sources:
  - id: S1
    url: https://raw.githubusercontent.com/google/leveldb/1.22/doc/impl.md
    publisher: Google / LevelDB maintainers
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
  - url: https://raw.githubusercontent.com/google/leveldb/1.22/doc/impl.md
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
      scope: 随机写密集场景使用 LSM 后，预测 compaction、读放大与空间放大的变化。
    remediation_applied: true
    scope_change: 已CLI读取官方1.22固定tag impl.md，正式冻结此实现而非main/模糊2011版本。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-023

```yaml
id: ENG-023
decision: retain
scenario_title: GitHub Actions pwn requests 风险（2020—）
focus: causal-modeling
subdomain: security-isolation
main_question: 不可信 PR 的哪条执行路径会跨入高权限上下文？
expected_output: 画出一条数据到执行的信任跨越
out_of_scope: 不把风险类别假装成未核实的独立入侵事故
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留GitHub Actions pwn requests 风险（2020—）的单一范围；不要求生产仓库名称与实际被窃信息未给出；不补造。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：不可信 PR 的哪条执行路径会跨入高权限上下文？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-024

```yaml
id: ENG-024
decision: retain
scenario_title: Amazon Aurora 共享存储（2017）
focus: causal-modeling
subdomain: distributed-consistency
main_question: 面对数据库实例故障与日志持久化，重建计算节点与分布式存储的恢复契约。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Amazon Aurora 共享存储（2017）的单一范围；不要求具体生产故障日志未公开，不编造恢复时长。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：面对数据库实例故障与日志持久化，重建计算节点与分布式存储的恢复契约。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-025

```yaml
id: ENG-025
decision: reframe
scenario_title: Nix 2006 论文中的时间戳纯度边界
focus: hypothesis-diagnosis
subdomain: developer-tooling-build
main_question: 相同声明的构建产物不同，如何区分时间戳差异与实际依赖漂移？
expected_output: 提出一个检查产物差异位置的检验，说明什么结果支持哪种解释
out_of_scope: 不虚构特定derivation或两次生产构建记录，不混同Guix引导信任题
reason: 原要求真实derivation与故障快照未齐；改为作者论文明确给出的linker/ar时间戳反例与模型边界工件。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：相同声明的构建产物不同，如何区分时间戳差异与实际依赖漂移？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-025
  status: sourced
  reason: 原要求真实derivation与故障快照未齐；改为作者论文明确给出的linker/ar时间戳反例与模型边界工件。
  event: Nix 2006 论文中的时间戳纯度边界
  cutoff: 2006论文第5.7、6.8节的模型反例，比较输出差异前
  initial_facts:
  - id: F1
    text: 构建输出可含链接器写入的系统时间。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Nix模型区分构建声明与输出内部编码。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 论文承认同一derivation每次可产生细微不同输出。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: Mac OS X ar归档时间戳甚至有与外层归档时间的链接约束。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 作者明确限定扩展相等假设：编码差异不必改变行为，但可变网络输入或影响链接的时间戳不能凭声明相同就排除。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 这是论文真实反例分析，不冒充某次Nix生产事故；无可核对的两次二进制哈希。
  sources:
  - id: S1
    url: https://edolstra.github.io/pubs/phd-thesis.pdf
    publisher: Eelco Dolstra / Utrecht University
    published_at: '2006-01-18'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://edolstra.github.io/pubs/phd-thesis.pdf
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://edolstra.github.io/pubs/phd-thesis.pdf
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 原要求真实derivation与故障快照未齐；改为作者论文明确给出的linker/ar时间戳反例与模型边界工件。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-026

```yaml
id: ENG-026
decision: retain
scenario_title: Cloudflare 2023 年 10 月 Workers KV 部署问题
focus: hypothesis-diagnosis
subdomain: reliability-diagnosis
main_question: 从部署相关性出发，下一项什么证据能区分权限与存储问题？
expected_output: 一个诊断优先项及两个预期观测差异
out_of_scope: 开场不先断言部署工具就是原因
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Cloudflare 2023 年 10 月 Workers KV 部署问题的单一范围；不要求不提供未公开逐请求日志。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：从部署相关性出发，下一项什么证据能区分权限与存储问题？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-027

```yaml
id: ENG-027
decision: retain
scenario_title: SQLite WAL 模式引入（2010）
focus: constrained-decision
subdomain: architecture-api
main_question: 读写并发需求改变时，评估 write-ahead log 相比 rollback journal 的可见性与恢复权衡。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留SQLite WAL 模式引入（2010）的单一范围；不要求不得将2026发现的WAL-reset bug当2010事前信息。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：读写并发需求改变时，评估 write-ahead log 相比 rollback journal 的可见性与恢复权衡。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-028

```yaml
id: ENG-028
decision: reframe
scenario_title: Dapper 采样开销测量的误差边界（2010）
focus: quantitative-calibration
subdomain: performance-cost
main_question: 从论文Table2看，1/16与1/1024采样的延迟差异足以证明后者让服务更快吗？
expected_output: 计算百分点差，结合误差范围给出有界结论，并解释不能推出稀有故障覆盖率
out_of_scope: 不计算缺输入的罕见故障漏采概率，不把负开销视为真实加速
reason: 保留数量训练，正式改为原论文可追溯的同口径采样开销与误差比较；不用缺失故障频率。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：从论文Table2看，1/16与1/1024采样的延迟差异足以证明后者让服务更快吗？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-028
  status: sourced
  reason: 保留数量训练，正式改为原论文可追溯的同口径采样开销与误差比较；不用缺失故障频率。
  event: Dapper 采样开销测量的误差边界（2010）
  cutoff: 2010论文Table2实验工件，解释测量结论前
  initial_facts:
  - id: F1
    text: 实验在Web search cluster比较非自适应采样频率。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 表中指标为相对未追踪基准的平均延迟、吞吐百分比变化。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 1/16的延迟变化2.12%，1/1024为-0.20%。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 论文列延迟实验误差2.5%，吞吐误差0.15%。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 两项延迟点估计差为2.32个百分点；论文认为低采样开销在实验误差内，不能凭-0.20%宣称加速，更不能证明特定稀有事件已覆盖。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 误差含义以论文为准，不补造置信区间或样本数；罕见故障分布仍未知。
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
  - url: https://research.google.com/pubs/archive/36356.pdf
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 保留数量训练，正式改为原论文可追溯的同口径采样开销与误差比较；不用缺失故障频率。
quantitative_inputs:
- name: 1/16采样平均延迟变化
  value: 2.12
  unit: percent
  source_ids:
  - S1
- name: 1/1024采样平均延迟变化
  value: -0.2
  unit: percent
  source_ids:
  - S1
- name: 延迟实验误差
  value: 2.5
  unit: percent
  source_ids:
  - S1
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-029

```yaml
id: ENG-029
decision: retain
scenario_title: Rust Ownership 与 Borrow Checker（2015）
focus: boundary-transfer
subdomain: runtime-concurrency
main_question: 这段共享引用能否通过编译检查，检查的保证到哪里为止？
expected_output: 一个边界判断及不受保证的业务竞态例子
out_of_scope: 不讲完整 ownership 教程或宣称消除所有并发错误
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Rust Ownership 与 Borrow Checker（2015）的单一范围；不要求Phase4需逐字对照原文代码而非改成现代语法后假称2015。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：这段共享引用能否通过编译检查，检查的保证到哪里为止？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-030

```yaml
id: ENG-030
decision: reframe
scenario_title: Snowflake 共享数据与虚拟仓库隔离（SIGMOD 2016）
focus: boundary-transfer
subdomain: data-storage
main_question: 停掉或扩容一个VW，会改变共享表的持久性或另一VW的数据副本吗？
expected_output: 划分共享持久层、私有计算与本地缓存三条责任并给出一次扩容预测
out_of_scope: 不混用后来版本，不把共享存储误称完全没有性能耦合
reason: 已通过官方2019目录中托管的2016原论文取得正文，消除原访问阻塞；训练只用2016模型。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：停掉或扩容一个VW，会改变共享表的持久性或另一VW的数据副本吗？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-030
  status: sourced
  reason: 已通过官方2019目录中托管的2016原论文取得正文，消除原访问阻塞；训练只用2016模型。
  event: Snowflake 共享数据与虚拟仓库隔离（SIGMOD 2016）
  cutoff: SIGMOD2016论文架构快照，一次VW停机/扩容操作前
  initial_facts:
  - id: F1
    text: 表数据存于共享S3层，VW由EC2工作节点构成。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 每条查询只在一个VW内执行。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 创建或销毁VW不改变数据库状态；不同VW访问同一共享表而无需复制。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 工作节点具有本地表数据缓存，resize后不立即搬移缓存，靠后续访问与LRU调整。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 2016设计允许独立伸缩计算而保留共享持久表；节点缓存生命周期随worker，扩容不等于持久数据重分片。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 不承诺S3吞吐/网络完全隔离；论文未提供任意负载扩容延迟。
  sources:
  - id: S1
    url: https://www.snowflake.com/wp-content/uploads/2019/06/Snowflake_SIGMOD.pdf?_fsi=7hkSrLqs
    publisher: Snowflake Computing / Dageville et al.
    published_at: '2016'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://www.snowflake.com/wp-content/uploads/2016/06/Snowflake_SIGMOD.pdf
    result: 不可达，未读到正文
  - url: https://dl.acm.org/doi/pdf/10.1145/2882903.2903741
    result: 403，未读到正文
  - url: https://www.snowflake.com/wp-content/uploads/2019/06/Snowflake_SIGMOD.pdf?_fsi=7hkSrLqs
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
      scope: 工作负载隔离和弹性扩容需求下，分析虚拟仓库如何改变资源竞争。
    remediation_applied: true
    scope_change: 已通过官方2019目录中托管的2016原论文取得正文，消除原访问阻塞；训练只用2016模型。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-031

```yaml
id: ENG-031
decision: retain
scenario_title: MongoDB 副本集选主（2016—2020）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: 一次已确认写入在给定选举时序后是否仍可读取？
expected_output: 逐步标出写确认、选举和可见性的关系
out_of_scope: 不跨版本混用 majority 的含义
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留MongoDB 副本集选主（2016—2020）的单一范围；不要求具体历史生产副本时序没有；如编排状态推演需明确为规范条件而非事故日志。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：一次已确认写入在给定选举时序后是否仍可读取？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-032

```yaml
id: ENG-032
decision: reframe
scenario_title: Guix 2013 论文引导链依赖检查
focus: evidence-selection
subdomain: developer-tooling-build
main_question: 最终工具链已重建且不再引用bootstrap路径，能否据此排除引导二进制信任风险？
expected_output: 选择一项独立检验信任根的证据，并精确说明路径引用检查已证明什么
out_of_scope: 不把可重建等同恶意编译器不存在，不重复Nix未声明时间输入
reason: 原Guix网页不可达；已读作者2013原论文第4节与Figure10，改用有版本边界的引导工件与真实依赖检查结果。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：最终工具链已重建且不再引用bootstrap路径，能否据此排除引导二进制信任风险？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-032
  status: sourced
  reason: 原Guix网页不可达；已读作者2013原论文第4节与Figure10，改用有版本边界的引导工件与真实依赖检查结果。
  event: Guix 2013 论文引导链依赖检查
  cutoff: 2013论文Figure10工件，审查最终工具链与引导输入的关系前
  initial_facts:
  - id: F1
    text: Guix构建程序依赖Guile运行。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 最早Guile由随源码提供的静态bash、tar、xz、mkdir解包得到。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: bootstrap Guile随后取得其他预编译工具链输入。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 作者检查最终工具链文件是否引用bootstrap输入的store目录。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 该检查界定最终工具链不再有对预编译bootstrap路径的直接依赖；它不是独立证明输入二进制无恶意行为，后者是维护者对证明范围的逻辑判断。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 原始引导二进制的全部来源与恶意编译器排除证据未由该检查证明。
  sources:
  - id: S1
    url: https://arxiv.org/pdf/1305.4584
    publisher: Ludovic Courtès / ELS 2013
    published_at: '2013-05-20'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://guix.gnu.org/en/blog/2013/the-bootstrap-binaries/
    result: 不可访问，未取得正文
  - url: https://arxiv.org/pdf/1305.4584
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 原Guix网页不可达；已读作者2013原论文第4节与Figure10，改用有版本边界的引导工件与真实依赖检查结果。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-033

```yaml
id: ENG-033
decision: retain
scenario_title: AWS S3 2017 年 us-east-1 中断
focus: causal-modeling
subdomain: reliability-diagnosis
main_question: 维护操作误影响存储子系统容量；从控制指令到跨服务后果重建故障传播。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留AWS S3 2017 年 us-east-1 中断的单一范围；不要求实际命令文本与服务器数量未公开，禁止编造。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：维护操作误影响存储子系统容量；从控制指令到跨服务后果重建故障传播。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-034

```yaml
id: ENG-034
decision: reframe
scenario_title: 2018 Meltdown/Spectre 补丁的 NWChem 实测开销
focus: quantitative-calibration
subdomain: security-isolation
main_question: 同一双节点NWChem任务补丁前58.4秒、后65.0秒，按旧基准与论文平均分母分别得到什么开销？
expected_output: 计算约11.3%与10.7%，解释分母差异并限定同机/组合补丁测量
out_of_scope: 不归因于KPTI单一机制，不把HPC小实验外推所有服务，不要求缺失的服务SLO
reason: 补得SUNY Buffalo研究者2018同期一手实验，正式改成特定工作负载和版本的数量校准；修正原只称Meltdown但补丁同时覆盖Spectre。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：同一双节点NWChem任务补丁前58.4秒、后65.0秒，按旧基准与论文平均分母分别得到什么开销？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-034
  status: sourced
  reason: 补得SUNY Buffalo研究者2018同期一手实验，正式改成特定工作负载和版本的数量校准；修正原只称Meltdown但补丁同时覆盖Spectre。
  event: 2018 Meltdown/Spectre 补丁的 NWChem 实测开销
  cutoff: 2018-01-16论文v2 TableI双节点NWChem测量工件，在解释补丁开销前
  initial_facts:
  - id: F1
    text: 测试在固定CCR开发集群与CentOS7.4.1708上进行。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 内核从3.10.0-693.5.2更新到693.11.6，同时修复三项Meltdown/Spectre CVE。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 双节点NWChem平均walltime由58.4秒变为65.0秒。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 对应运行次数21与56；表格开销分母用前后均值的平均，而非旧均值。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 同一组测量按旧均值算约11.30%，按论文平均分母算约10.70%；作者观测到该负载退化，但未隔离KPTI单项代价。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 论文表注显著性alpha有排版疑点，与正文0.05不同；本题不以该表注作统计显著性判断。
  sources:
  - id: S1
    url: https://arxiv.org/pdf/1801.04329v2
    publisher: SUNY Buffalo CCR / Nikolay Simakov et al.
    published_at: '2018-01-16'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://meltdownattack.com/meltdown.pdf
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://arxiv.org/pdf/1801.04329v2
    result: 实际阅读arxiv默认PDF，正文明确标为1801.04329v2、2018-01-16；来源记录用其显式v2 URL，数据取TableI与Methods。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 补得SUNY Buffalo研究者2018同期一手实验，正式改成特定工作负载和版本的数量校准；修正原只称Meltdown但补丁同时覆盖Spectre。
quantitative_inputs:
- name: 双节点NWChem补丁前均值
  value: 58.4
  unit: seconds
  source_ids:
  - S1
- name: 补丁后均值
  value: 65.0
  unit: seconds
  source_ids:
  - S1
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-035

```yaml
id: ENG-035
decision: retain
scenario_title: GraphQL 在 Facebook 的起源（2012—2015）
focus: boundary-transfer
subdomain: architecture-api
main_question: 移动端数据需求快速分化时，比较固定 REST endpoint 与客户端声明式查询的边界。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留GraphQL 在 Facebook 的起源（2012—2015）的单一范围；不要求精确请求计数需要具体资源图，勿借ENG056的GitHub例子。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：移动端数据需求快速分化时，比较固定 REST endpoint 与客户端声明式查询的边界。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-036

```yaml
id: ENG-036
decision: reframe
scenario_title: Linux 2.6.23 CFS 公平账户与红黑树（2007）
focus: causal-modeling
subdomain: runtime-concurrency
main_question: 相同权重任务中，一个已经占用更多CPU后，为何其下一次获调度的相对优先权会下降？
expected_output: 沿运行记账、wait_runtime与fair_key排序解释一次竞争变化
out_of_scope: 不把后续vruntime字段倒灌到该tag，不混用EEVDF，不给不存在的任务时长日志
reason: 本轮发现v2.6.23归档文档及源码使用wait_runtime/fair_key；修正前轮将现行vruntime说明等同2007该实现的错误。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：相同权重任务中，一个已经占用更多CPU后，为何其下一次获调度的相对优先权会下降？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-036
  status: sourced
  reason: 本轮发现v2.6.23归档文档及源码使用wait_runtime/fair_key；修正前轮将现行vruntime说明等同2007该实现的错误。
  event: Linux 2.6.23 CFS 公平账户与红黑树（2007）
  cutoff: Linuxv2.6.23固定tag设计与sched_fair.c，完成一次CPU运行记账后重新入队前
  initial_facts:
  - id: F1
    text: CFS以理想公平共享CPU作为比较基准。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 实际一次只运行一个任务，等待任务相对积累应得CPU。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 该tag运行记账按应得时间减去实际执行时间更新wait_runtime。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: nice0入队键为fair_clock减wait_runtime，红黑树取最左任务，并保留调度粒度以免过度切换。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 已消耗超过份额的任务在公平账户中相对落后于仍等待的任务，后者逐渐取得调度机会；不代表每个瞬间严格等分。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 该tag字段与后续vruntime实现不同；这里只按本次实际读到的固定源码推演。
  sources:
  - id: S1
    url: https://raw.githubusercontent.com/torvalds/linux/v2.6.23/kernel/sched_fair.c
    publisher: Linux / Ingo Molnar and contributors
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
  - url: https://www.kernel.org/doc/Documentation/scheduler/sched-design-CFS.txt
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://raw.githubusercontent.com/torvalds/linux/v2.6.23/kernel/sched_fair.c
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
      scope: 负载不均的 CPU 任务争用下，推导 vruntime 如何影响公平与延迟。
    remediation_applied: true
    scope_change: 本轮发现v2.6.23归档文档及源码使用wait_runtime/fair_key；修正前轮将现行vruntime说明等同2007该实现的错误。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-037

```yaml
id: ENG-037
decision: reframe
scenario_title: Redis 3.0 异步复制与 Sentinel 确认边界（2015）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: primary已确认、某replica尚未复制时提升该replica，这个ACK足以证明写入保留吗？
expected_output: 给出有条件的数据保留预测，说明限制落后副本配置仍不保证每条写都有N份
out_of_scope: 不编秒级故障日志，不把后来的WAIT/默认设置回填旧版
reason: 补读Redis3.0.0 redis.conf和sentinel.conf，冻结异步复制及failover重配契约，替代未锁定2013现行文档。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：primary已确认、某replica尚未复制时提升该replica，这个ACK足以证明写入保留吗？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-037
  status: sourced
  reason: 补读Redis3.0.0 redis.conf和sentinel.conf，冻结异步复制及failover重配契约，替代未锁定2013现行文档。
  event: Redis 3.0 异步复制与 Sentinel 确认边界（2015）
  cutoff: Redis3.0.0配置工件，指定副本在确认写尚未复制时即将成为新主
  initial_facts:
  - id: F1
    text: 该版本明确replication是异步的。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Sentinel failover会把其他副本改为跟随新主。
    source_ids:
    - S2
    availability: pre_decision
  evidence:
  - id: E1
    text: 主节点可在满足最少副本连接/lag条件时接受写。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 配置文档明确该限制不保证N个副本实际接受了每条写，只能限制暴露窗口。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 在题目明确的未复制条件下，已确认写不能由被提升副本提供；配置限制与同步逐写确认是不同保证。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 未给真实故障时序；本题明示规范条件推演，不声称某次真实Redis丢数据事故。
  sources:
  - id: S1
    url: https://raw.githubusercontent.com/redis/redis/3.0.0/redis.conf
    publisher: Redis maintainers
    published_at: '2015'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - E1
    - E2
    - O1
  - id: S2
    url: https://raw.githubusercontent.com/redis/redis/3.0.0/sentinel.conf
    publisher: Redis maintainers
    published_at: '2015'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F2
  attempts:
  - url: https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://raw.githubusercontent.com/redis/redis/3.0.0/redis.conf
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  - url: https://raw.githubusercontent.com/redis/redis/3.0.0/sentinel.conf
    result: CLI实际读取3.0.0 sentinel.conf的parallel-syncs与failover-timeout重配说明。
  phase2_conditions:
    original:
      scope: 根据主从延迟和故障检测事件，预测 promote 后的数据丢失窗口和脑裂可能性。
    remediation_applied: true
    scope_change: 补读Redis3.0.0 redis.conf和sentinel.conf，冻结异步复制及failover重配契约，替代未锁定2013现行文档。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-038

```yaml
id: ENG-038
decision: retain
scenario_title: Go 1.21 Toolchain 管理（2023）
focus: constrained-decision
subdomain: developer-tooling-build
main_question: 离线环境应允许自动选取工具链，还是显式固定它？
expected_output: 一个策略及其失败回退条件
out_of_scope: 不同时设计完整供应链管理方案
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Go 1.21 Toolchain 管理（2023）的单一范围；不要求不把推荐策略当唯一答案；离线约束需明确为练习条件。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：离线环境应允许自动选取工具链，还是显式固定它？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-039

```yaml
id: ENG-039
decision: reframe
scenario_title: Pingora 同负载迁移与连接复用比例（2022）
focus: quantitative-calibration
subdomain: performance-cost
main_question: 同一客户连接复用率由87.1%变为99.92%，对应每个请求新建连接比例减少多少倍，能否用它解释全部资源收益？
expected_output: 按未复用比例计算约161倍差异，并把客户指标与全网资源归因分开
out_of_scope: 不推算没有连接成本分解的内存字节或财务节省
reason: 正式缩小数量主线到来源中同客户复用率的可计算比例；保留数量训练，撤掉独立CPU/内存归因要求。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：同一客户连接复用率由87.1%变为99.92%，对应每个请求新建连接比例减少多少倍，能否用它解释全部资源收益？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-039
  status: sourced
  reason: 正式缩小数量主线到来源中同客户复用率的可计算比例；保留数量训练，撤掉独立CPU/内存归因要求。
  event: Pingora 同负载迁移与连接复用比例（2022）
  cutoff: 2022-09-14发布的迁移测量工件，按给定同客户口径计算前
  initial_facts:
  - id: F1
    text: 旧NGINX连接池局限于worker。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Pingora可在线程间共享连接。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 一位主要客户的连接复用率由87.1%升至99.92%。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 同负载全生产服务CPU少约70%、内存少约67%，原文列多个来源因素而非单一连接成本。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 按请求口径推导未复用比例12.9%/0.08%约161.25；与作者约160倍新连接下降相符，不能据此把全服务资源收益归给单一因素。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 客户身份、每连接资源成本及单因素对照未知；推导仅在同请求口径成立。
  sources:
  - id: S1
    url: https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/
    publisher: Cloudflare / Pingora team
    published_at: '2022-09-14'
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
  - url: https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 正式缩小数量主线到来源中同客户复用率的可计算比例；保留数量训练，撤掉独立CPU/内存归因要求。
quantitative_inputs:
- name: 旧连接复用率
  value: 87.1
  unit: percent
  source_ids:
  - S1
- name: 新连接复用率
  value: 99.92
  unit: percent
  source_ids:
  - S1
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-040

```yaml
id: ENG-040
decision: retain
scenario_title: Cloudflare 2023 年 11 月控制面中断
focus: boundary-transfer
subdomain: reliability-diagnosis
main_question: 数据中心供电故障令控制面不可用而部分数据面仍工作；判断故障域与依赖分层。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Cloudflare 2023 年 11 月控制面中断的单一范围；不要求不把2024改善成效提前置入2023开场。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：数据中心供电故障令控制面不可用而部分数据面仍工作；判断故障域与依赖分层。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-041

```yaml
id: ENG-041
decision: retain
scenario_title: Google Bigtable（2006）
focus: causal-modeling
subdomain: data-storage
main_question: 大规模稀疏宽表如何实现有序键扫描，分析 tablet 切分与单点热点。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Google Bigtable（2006）的单一范围；不要求不编造真实热键指标。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：大规模稀疏宽表如何实现有序键扫描，分析 tablet 切分与单点热点。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-042

```yaml
id: ENG-042
decision: reframe
scenario_title: Kubernetes 1.18 CRD 与聚合 API 存储边界（2020）
focus: constrained-decision
subdomain: architecture-api
main_question: 扩展资源必须使用独立存储与logs类自定义子资源，应选CRD还是聚合API？
expected_output: 选择一个扩展机制，指出决定选择的最小不可满足条件及新增运维责任
out_of_scope: 不引入后续CEL或field selector特性，不泛列全部扩展机制
reason: 已下载官方release-1.18分支正文，改锚2020的明确版本，替代未锁定2016—2018泛称。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：扩展资源必须使用独立存储与logs类自定义子资源，应选CRD还是聚合API？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-042
  status: sourced
  reason: 已下载官方release-1.18分支正文，改锚2020的明确版本，替代未锁定2016—2018泛称。
  event: Kubernetes 1.18 CRD 与聚合 API 存储边界（2020）
  cutoff: Kubernetes1.18官方Custom Resources文档契约，选择扩展实现前
  initial_facts:
  - id: F1
    text: CRD让主API server通用地服务并存储自定义对象。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 聚合API由主server将请求代理到独立扩展server。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 该版比较表列CRD不支持自定义存储，聚合API支持。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: logs/exec等其他子资源同样只有聚合API支持，且额外server部署引入故障点。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 该工件把上述要求放在聚合API能力边界内；若只需通用CRUD与受支持子资源，CRD可省去额外服务。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 本轮通过允许的CLI实际读取公开原文；不声称旧版本已有后来的扩展能力。
  sources:
  - id: S1
    url: https://raw.githubusercontent.com/kubernetes/website/release-1.18/content/en/docs/concepts/extend-kubernetes/api-extension/custom-resources.md
    publisher: Kubernetes documentation maintainers
    published_at: '2020'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://raw.githubusercontent.com/kubernetes/website/release-1.18/content/en/docs/concepts/extend-kubernetes/api-extension/custom-resources.md
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 已下载官方release-1.18分支正文，改锚2020的明确版本，替代未锁定2016—2018泛称。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-043

```yaml
id: ENG-043
decision: reframe
scenario_title: Spectre variant 1 边界检查与可观察状态（2018）
focus: boundary-transfer
subdomain: security-isolation
main_question: x的边界检查最终拒绝访问，为何仍不能仅由此断言秘密未影响可观察状态？
expected_output: 区分架构结果回滚与缓存状态边界，并指出检验后者的观测类型
out_of_scope: 只用variant1条件分支示例，不混同Meltdown权限检查或variant2间接跳转
reason: 固定原论文明确variant1原始示例，消除前轮泛称架构访问拒绝易与Meltdown混淆的问题。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：x的边界检查最终拒绝访问，为何仍不能仅由此断言秘密未影响可观察状态？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-043
  status: sourced
  reason: 固定原论文明确variant1原始示例，消除前轮泛称架构访问拒绝易与Meltdown混淆的问题。
  event: Spectre variant 1 边界检查与可观察状态（2018）
  cutoff: 2018论文variant1示例，在判断错误推测是否完全无影响前
  initial_facts:
  - id: F1
    text: 示例先检查x是否小于array1_size。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: CPU可在检查结果未到达前预测分支并推测执行。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 错误推测的架构计算结果会被回滚。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 示例中依秘密而定的访存可改变缓存，缓存副作用并不随架构寄存器一起回滚。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 原研究通过侧信道观察证明该边界检查不足以覆盖所有微架构可观察信息；不是要求解除内核访问权限。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 不提供利用步骤或虚构计时日志；具体硬件适用与缓解因版本不同。
  sources:
  - id: S1
    url: https://spectreattack.com/spectre.pdf
    publisher: Paul Kocher et al. / original researchers
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
  - url: https://spectreattack.com/spectre.pdf
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 固定原论文明确variant1原始示例，消除前轮泛称架构访问拒绝易与Meltdown混淆的问题。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-044

```yaml
id: ENG-044
decision: retain
scenario_title: Facebook TAO（2013）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: 研究社交图读多写少场景中，缓存层与主存储的更新传播及一致性取舍。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Facebook TAO（2013）的单一范围；不要求不虚构复制延迟或一致性SLA。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：研究社交图读多写少场景中，缓存层与主存储的更新传播及一致性取舍。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-045

```yaml
id: ENG-045
decision: reframe
scenario_title: Cargo 0.53.0 resolver 2 特性合并工件（2021）
focus: prediction-counterfactual
subdomain: developer-tooling-build
main_question: 新增普通依赖bar启用winapi的std/winnt后，原foo所启用fileapi/handleapi会怎样变化？
expected_output: 按官方菱形例子列共享包feature并集，并给出build-dependency例外边界
out_of_scope: 不把resolver2归到2013，不把feature并集误称随机不可复现
reason: 已CLI实际读取Cargo0.53.0固定tag，采用文中真实foo/bar/winapi例子，消除原现行规范历史范围歧义。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：新增普通依赖bar启用winapi的std/winnt后，原foo所启用fileapi/handleapi会怎样变化？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-045
  status: sourced
  reason: 已CLI实际读取Cargo0.53.0固定tag，采用文中真实foo/bar/winapi例子，消除原现行规范历史范围歧义。
  event: Cargo 0.53.0 resolver 2 特性合并工件（2021）
  cutoff: Cargo0.53.0文档指定resolver=2，在加入bar普通依赖前
  initial_facts:
  - id: F1
    text: feature名称归定义它的package所有。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 官方示例foo为winapi启用fileapi和handleapi。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: bar为同一winapi启用std和winnt时，普通依赖构建取四项并集。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: resolver2不会将build-dependency/proc-macro与普通依赖的feature无条件合并。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 增加普通路径会启用已有共享依赖的附加feature，而分离的构建上下文可能需要各自构建；规则确定但边界重要。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 沿官方依赖图与feature名称；不虚构生产项目的Cargo.lock或编译失败。
  sources:
  - id: S1
    url: https://raw.githubusercontent.com/rust-lang/cargo/0.53.0/src/doc/src/reference/features.md
    publisher: Rust / Cargo maintainers
    published_at: '2021'
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
  - url: https://raw.githubusercontent.com/rust-lang/cargo/0.53.0/src/doc/src/reference/features.md
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 已CLI实际读取Cargo0.53.0固定tag，采用文中真实foo/bar/winapi例子，消除原现行规范历史范围歧义。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-046

```yaml
id: ENG-046
decision: reframe
scenario_title: .NET 6 Hill Climbing 吞吐反馈工件（2021）
focus: evidence-selection
subdomain: runtime-concurrency
main_question: worker数量增加却不能仅凭队列下降判定收益，下一项该记录什么才能区分不足与竞争？
expected_output: 选择同采样窗口的完成率与线程变化关系，列正负两种预期
out_of_scope: 不伪造生产吞吐曲线，不把总线程数当可用worker数
reason: 固定官方v6.0.0源码而非main；改为该控制器真实使用的反馈选择题，无须未知实际故障曲线。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：worker数量增加却不能仅凭队列下降判定收益，下一项该记录什么才能区分不足与竞争？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-046
  status: sourced
  reason: 固定官方v6.0.0源码而非main；改为该控制器真实使用的反馈选择题，无须未知实际故障曲线。
  event: .NET 6 Hill Climbing 吞吐反馈工件（2021）
  cutoff: dotnet/runtime v6.0.0 PortableThreadPool.HillClimbing.cs，选择反馈指标前
  initial_facts:
  - id: F1
    text: 控制器以完成任务数除以采样时长计算throughput。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 源码同时记录currentThreadCount与吞吐样本。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 控制器比较线程波动与吞吐波动的关系。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 源码明确反相时后退、90度相位时不判断，并用噪声降低调整信心。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 该实现依据吞吐反馈调整线程，不按队列长度或线程数单独判断；输出和事件日志保留新线程数与调整统计。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 这是控制器源码工件，线程竞争的具体业务原因仍需实验，不宣称已定位真实事故。
  sources:
  - id: S1
    url: https://github.com/dotnet/runtime/blob/v6.0.0/src/libraries/System.Private.CoreLib/src/System/Threading/PortableThreadPool.HillClimbing.cs
    publisher: Microsoft / .NET runtime maintainers
    published_at: '2021'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://github.com/dotnet/runtime/blob/main/src/libraries/System.Private.CoreLib/src/System/Threading/PortableThreadPool.HillClimbing.cs
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://github.com/dotnet/runtime/blob/v6.0.0/src/libraries/System.Private.CoreLib/src/System/Threading/PortableThreadPool.HillClimbing.cs
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 固定官方v6.0.0源码而非main；改为该控制器真实使用的反馈选择题，无须未知实际故障曲线。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-047

```yaml
id: ENG-047
decision: retain
scenario_title: Fastly 2021 年 6 月大面积故障
focus: boundary-transfer
subdomain: reliability-diagnosis
main_question: 潜伏软件缺陷被客户配置触发；评估配置有效性与底层实现之间的责任边界。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Fastly 2021 年 6 月大面积故障的单一范围；不要求触发配置具体内容与软件bug代码未公开。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：潜伏软件缺陷被客户配置触发；评估配置有效性与底层实现之间的责任边界。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-048

```yaml
id: ENG-048
decision: reframe
scenario_title: SQLite NGQP 导致 Fossil 查询回归（2013）
focus: hypothesis-diagnosis
subdomain: data-storage
main_question: 索引已经存在但升级后查询变慢，应先补索引还是检验选择率估计？
expected_output: 用两条可用连接次序与数据选择率证据区分缺索引和统计缺口
out_of_scope: 只取NGQP首次升级案例，不混入2017后改进或2025星形查询启发式
reason: 找到官方NGQP文档第5.1—5.2真实Fossil回归，替换无实际快照的普通教程；有SQL、索引、选择率与修复对照。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：索引已经存在但升级后查询变慢，应先补索引还是检验选择率估计？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-048
  status: sourced
  reason: 找到官方NGQP文档第5.1—5.2真实Fossil回归，替换无实际快照的普通教程；有SQL、索引、选择率与修复对照。
  event: SQLite NGQP 导致 Fossil 查询回归（2013）
  cutoff: SQLite3.8.0时期Fossil timeline回归，已知升级后慢、尚未执行ANALYZE修复
  initial_facts:
  - id: F1
    text: Fossil用SQLite存储版本记录，升级NGQP后timeline由毫秒级变为接近10秒。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 子查询连接plink与tagxref；两者均已有相关索引。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 一个check-in通常只有很少子项，trunk标签却命中成千记录。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 没有统计时NGQP按索引同等选择性估计，实际可比较先按父项或先按标签的两种连接顺序。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 官方记录运行ANALYZE立即修复性能；随后CROSS JOIN固定顺序，但作者也说明不同数据分布可反转优劣。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 只用文档具体历史案例节；不补造EXPLAIN输出、统计表行或精确速度倍数。
  sources:
  - id: S1
    url: https://www.sqlite.org/queryplanner-ng.html
    publisher: SQLite / D. Richard Hipp et al.
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
  - url: https://www.sqlite.org/queryplanner.html
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://www.sqlite.org/queryplanner-ng.html
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 找到官方NGQP文档第5.1—5.2真实Fossil回归，替换无实际快照的普通教程；有SQL、索引、选择率与修复对照。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-049

```yaml
id: ENG-049
decision: reframe
scenario_title: Kubernetes 1.18 Job 控制器与执行职责（2020）
focus: causal-modeling
subdomain: architecture-api
main_question: Job已创建但Pod尚未运行，为什么不能直接认定Job控制器没有履行它的职责？
expected_output: 划分期望对象、Pod创建、调度与kubelet执行的链条和一个观测点
out_of_scope: 不讲2014未确认的Deployment历史，不把API创建确认当工作完成
reason: 补读官方release-1.18控制器文档的真实Job示例，固定对象与版本，替代2014泛称。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：Job已创建但Pod尚未运行，为什么不能直接认定Job控制器没有履行它的职责？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-049
  status: sourced
  reason: 补读官方release-1.18控制器文档的真实Job示例，固定对象与版本，替代2014泛称。
  event: Kubernetes 1.18 Job 控制器与执行职责（2020）
  cutoff: Kubernetes1.18文档Job机制，Job已写入API、检查Pod是否开始前
  initial_facts:
  - id: F1
    text: Job对象声明要完成的任务。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 控制器经API server观察对象并创建或移除Pod。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 官方明确Job controller本身不运行Pod或容器。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: Pod调度后由节点kubelet执行，其他控制面组件需先响应新对象。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: Job声明、控制器调和与最终执行有职责和时间边界；单个API确认不能证明各阶段已完成。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 不提供无来源的生产调度日志；实际失败在哪一段需以对象状态区分。
  sources:
  - id: S1
    url: https://raw.githubusercontent.com/kubernetes/website/release-1.18/content/en/docs/concepts/architecture/controller.md
    publisher: Kubernetes documentation maintainers
    published_at: '2020'
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
  - url: https://raw.githubusercontent.com/kubernetes/website/release-1.18/content/en/docs/concepts/architecture/controller.md
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
      scope: 从 Deployment、ReplicaSet、Pod 分层理解声明式 API 如何分配状态和所有权。
    remediation_applied: true
    scope_change: 补读官方release-1.18控制器文档的真实Job示例，固定对象与版本，替代2014泛称。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-050

```yaml
id: ENG-050
decision: reframe
scenario_title: Kafka 2011 批量发布实验
focus: quantitative-calibration
subdomain: performance-cost
main_question: 同一实验批量从1到50时，消息吞吐和隐含发布请求率各如何变化？
expected_output: 算出吞吐约8倍与按满批折算的请求率，并说明为什么仍不能计算等待时间
out_of_scope: 不补到达分布，不将异步无ACK结果迁移为强持久事务吞吐
reason: 正式改为原论文可追溯批量/吞吐的更小数量题，保留数量动作，不再精算未公开等待分布。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：同一实验批量从1到50时，消息吞吐和隐含发布请求率各如何变化？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-050
  status: sourced
  reason: 正式改为原论文可追溯批量/吞吐的更小数量题，保留数量动作，不再精算未公开等待分布。
  event: Kafka 2011 批量发布实验
  cutoff: NetDB2011 producer experiment工件，在解释批量数据前
  initial_facts:
  - id: F1
    text: 实验每条消息200字节，共一千万条。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Kafka producer测试采用异步、不等待broker确认。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: batch=1平均发布约50000条/秒；batch=50约400000条/秒。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 一次publish可含一批消息，作者称批量摊销RPC开销；批量50接近1Gb链路限制。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 按满批折算请求率从50000次/秒变为8000次/秒，消息吞吐约8倍；缺到达时间与排队分布，不能得出端到端等待改善。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 按满批折算为透明算术，非抓包观测；原实验未保证每条发布消息均被broker接收。
  sources:
  - id: S1
    url: https://www.microsoft.com/en-us/research/wp-content/uploads/2017/09/Kafka.pdf
    publisher: LinkedIn / Jay Kreps, Neha Narkhede, Jun Rao
    published_at: '2011-06-12'
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
  - url: https://www.microsoft.com/en-us/research/wp-content/uploads/2017/09/Kafka.pdf
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 正式改为原论文可追溯批量/吞吐的更小数量题，保留数量动作，不再精算未公开等待分布。
quantitative_inputs:
- name: 小批大小
  value: 1
  unit: messages/request
  source_ids:
  - S1
- name: 大批大小
  value: 50
  unit: messages/request
  source_ids:
  - S1
- name: 小批吞吐
  value: 50000
  unit: messages/s
  source_ids:
  - S1
- name: 大批吞吐
  value: 400000
  unit: messages/s
  source_ids:
  - S1
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-051

```yaml
id: ENG-051
decision: retain
scenario_title: Log4Shell（2021）
focus: causal-modeling
subdomain: security-isolation
main_question: 日志字符串最终触发 JNDI 远程查找；在数据到控制的路径上定位信任边界。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Log4Shell（2021）的单一范围；不要求具体应用配置与JDK条件需在Brief固定，不能泛称所有Java日志皆可RCE。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：日志字符串最终触发 JNDI 远程查找；在数据到控制的路径上定位信任边界。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-052

```yaml
id: ENG-052
decision: retain
scenario_title: Amazon Dynamo（2007）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: 在这一组读写配置下，请求会失败还是返回多个版本？
expected_output: 一条分区时序预测及冲突条件
out_of_scope: 不设计整个购物车系统或做无数字的精算
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Amazon Dynamo（2007）的单一范围；不要求需指定可达节点与时序，否则请求失败还是多版本无法唯一确定。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：在这一组读写配置下，请求会失败还是返回多个版本？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-053

```yaml
id: ENG-053
decision: reframe
scenario_title: Nx 2020 Affected 与真实部署基线工件
focus: constrained-decision
subdomain: developer-tooling-build
main_question: 共享bike-utils改动后，只按应用目录git diff决定跳过构建是否安全？
expected_output: 给出需重建的应用集合，并指定last-successful-deploy到HEAD的比较基线
out_of_scope: 不混入2026 task-based affected，不伪造实际商业部署事故
reason: 找到Nx团队成员Rareș Matei同期亲写官方合作教程，明确项目依赖图、改动和输出；不再依赖现行v24行为。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：共享bike-utils改动后，只按应用目录git diff决定跳过构建是否安全？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-053
  status: sourced
  reason: 找到Nx团队成员Rareș Matei同期亲写官方合作教程，明确项目依赖图、改动和输出；不再依赖现行v24行为。
  event: Nx 2020 Affected 与真实部署基线工件
  cutoff: 2020-04-21作者示例版本，bike-utils改动、决定哪些部署前
  initial_facts:
  - id: F1
    text: 示例有bike-store、car-store两个前端及bike-store-api。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: bike-store和bike-store-api共同import bike-utils。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 作者示例在bike-utils变更后把依赖方标为affected。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: print-affected支持base/head，部署基线使用最后成功部署commit，而非只取HEAD的父提交。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 教程说明共享工具变更使bike-store部署而car-store被跳过；仅改Express API则两个前端都可跳过，依赖关系决定影响。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 这是同期公开教学工件，不声称真实生产事故；网页个别解释文字有笔误，采用明确依赖与示例结果，不照抄矛盾语句。
  sources:
  - id: S1
    url: https://www.netlify.com/blog/2020/04/21/deploying-nx-monorepos-to-netlify/
    publisher: Netlify / Nrwl engineer Rareș Matei
    published_at: '2020-04-21'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://nx.dev/docs/features/ci-features/affected
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://www.netlify.com/blog/2020/04/21/deploying-nx-monorepos-to-netlify/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
      scope: 在 Monorepo 中按依赖图选择受影响任务，分析图不完整时的漏构建风险。
    remediation_applied: true
    scope_change: 找到Nx团队成员Rareș Matei同期亲写官方合作教程，明确项目依赖图、改动和输出；不再依赖现行v24行为。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-054

```yaml
id: ENG-054
decision: replace
scenario_title: Cloudflare 2017 闰秒导致DNS负时长故障
focus: causal-modeling
subdomain: reliability-diagnosis
main_question: 上游DNS明明几毫秒返回，为什么本地延迟权重仍可能触发服务异常？
expected_output: 重建墙钟回拨、负RTT、平滑与权重选择的因果链，并指出一条保护边界
out_of_scope: 不继续沿用未核实的Google2012故障，不混用2019后Go单调时钟语义
reason: 原Google2012事故身份无法核实，正式替换为当事人2017-01-01独立事故；全年未发现另一闰秒槽位，ID与日期保留。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：上游DNS明明几毫秒返回，为什么本地延迟权重仍可能触发服务异常？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-054
  status: sourced
  reason: 原Google2012事故身份无法核实，正式替换为当事人2017-01-01独立事故；全年未发现另一闰秒槽位，ID与日期保留。
  event: Cloudflare 2017 闰秒导致DNS负时长故障
  cutoff: 2017-01-01 RRDNS部分CNAME失败已可见，读取代码并诊断根因前
  initial_facts:
  - id: F1
    text: RRDNS会查询上游resolver来展开客户CNAME。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 其选择机制保存并平滑resolver响应时长。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 当时Go time.Now不保证单调，结束值可能早于start。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 随机权重选择函数要求非负参数，负时长经过平滑仍可能传入。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: Cloudflare归因于闰秒回拨使RTT及平滑权重变负，触发panic；补丁在时间回退时重置相关性能状态，避免负数进入选择器。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 该复盘的因果归属为Cloudflare；不将DNS错误比例等同全网不可用。
  sources:
  - id: S1
    url: https://blog.cloudflare.com/how-and-why-the-leap-second-affected-cloudflare-dns/
    publisher: Cloudflare / John Graham-Cumming
    published_at: '2017-01-01'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://developers.google.com/time/smear
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://blog.cloudflare.com/how-and-why-the-leap-second-affected-cloudflare-dns/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
      scope: 时间推进异常引发高 CPU 及服务退化；识别时钟假设与同步机制的关系。
    remediation_applied: true
    scope_change: 原Google2012事故身份无法核实，正式替换为当事人2017-01-01独立事故；全年未发现另一闰秒槽位，ID与日期保留。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-055

```yaml
id: ENG-055
decision: retain
scenario_title: Go 1.14 异步抢占（2020）
focus: prediction-counterfactual
subdomain: runtime-concurrency
main_question: 另一个可运行 goroutine 何时才有机会执行？
expected_output: 一项前后行为预测及仍可能停顿的边界
out_of_scope: 不把调度改进等同于消除所有暂停
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Go 1.14 异步抢占（2020）的单一范围；不要求原文无具体循环片段，应在Brief明确最小示例为规范推演。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：另一个可运行 goroutine 何时才有机会执行？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-056

```yaml
id: ENG-056
decision: reframe
scenario_title: GitHub API v4 发布工件的请求责任边界（2016）
focus: boundary-transfer
subdomain: architecture-api
main_question: 客户端要用户资料及前三仓库的关系数据时，声明式查询减少什么工作，又把什么责任移到服务端？
expected_output: 划分字段选择、关系遍历与授权/查询执行责任，不宣称全面性能提高
out_of_scope: 不编造同期REST端点和分页调用数，不要求精确请求比
reason: 正式采用预列boundary-transfer备用问题；发布原文的完整GraphQL查询和一次返回足以支撑责任边界，不依赖缺失REST对应端点。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：客户端要用户资料及前三仓库的关系数据时，声明式查询减少什么工作，又把什么责任移到服务端？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-056
  status: sourced
  reason: 正式采用预列boundary-transfer备用问题；发布原文的完整GraphQL查询和一次返回足以支撑责任边界，不依赖缺失REST对应端点。
  event: GitHub API v4 发布工件的请求责任边界（2016）
  cutoff: 2016-09-14发布示例工件；后续2021页面更新不作当时新能力证据
  initial_facts:
  - id: F1
    text: 原REST使用资源URL提示，调用者常需多次拼装视图。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 发布示例由客户端声明用户和前三个仓库所需字段。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 示例展示一条GraphQL请求取得指定关系与字段。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 同文展示email权限不足时的字段级授权错误，服务端仍需schema、解析与权限检查。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 该API把结果形状交给客户端声明，并由服务端组合和约束查询；少一类客户端拼装责任不保证少一类服务端数据库工作。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 网页标注2021-11-17更新，不采更新后未能归于发布版本的能力；精确REST调用数保持未知。
  sources:
  - id: S1
    url: https://github.blog/developer-skills/github/the-github-graphql-api/
    publisher: GitHub Engineering
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
  - url: https://github.blog/developer-skills/github/the-github-graphql-api/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 正式采用预列boundary-transfer备用问题；发布原文的完整GraphQL查询和一次返回足以支撑责任边界，不依赖缺失REST对应端点。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-057

```yaml
id: ENG-057
decision: reframe
scenario_title: Amazon Redshift 2015 列块跳过与分布工件
focus: causal-modeling
subdomain: data-storage
main_question: 查询只需少数列并按已排序值过滤时，列布局与块范围信息分别怎样减少读取？
expected_output: 区分读列、跳块与分布键减少跨节点传输三种机制，只重建前两项主链
out_of_scope: 不使用无负载的倍数收益，不将2015文档写作2012实测
reason: 补得SIGMOD2015 AWS作者原论文，明确晚于2012 preview；用同一设计快照替代现行文档追溯早期实现。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：查询只需少数列并按已排序值过滤时，列布局与块范围信息分别怎样减少读取？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-057
  status: sourced
  reason: 补得SIGMOD2015 AWS作者原论文，明确晚于2012 preview；用同一设计快照替代现行文档追溯早期实现。
  event: Amazon Redshift 2015 列块跳过与分布工件
  cutoff: SIGMOD2015架构工件，决定一类列投影/范围过滤查询的数据读取路径前
  initial_facts:
  - id: F1
    text: 每个slice按列把值存入固定尺寸数据块链。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 分析查询可以只投影部分列，而不是整行。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 论文说明per-column compression与columnar layout。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: Redshift以顺序扫描及内存中的块值范围跳过无关column blocks，不采用传统索引。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 论文所述实现结合列选择、压缩及范围块跳过降低扫描工作；布局带来的工作量变化与特定查询实际速度仍应分开。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 不引用论文业务采用解释为独立因果证据；无可比查询输入不能给速度倍数。
  sources:
  - id: S1
    url: https://cdn.amazon.science/df/5f/9251d6f9403c99b070e11be88e38/amazon-redshift-and-the-case-for-simpler-data-warehouses.pdf
    publisher: AWS / Anurag Gupta et al.
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
  - url: https://docs.aws.amazon.com/redshift/latest/dg/c_columnar_storage_disk_mem_mgmnt.html
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://cdn.amazon.science/df/5f/9251d6f9403c99b070e11be88e38/amazon-redshift-and-the-case-for-simpler-data-warehouses.pdf
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
      scope: 大量扫描与聚合请求时，判断压缩、排序键和数据分布对于性能的影响。
    remediation_applied: true
    scope_change: 补得SIGMOD2015 AWS作者原论文，明确晚于2012 preview；用同一设计快照替代现行文档追溯早期实现。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-058

```yaml
id: ENG-058
decision: reframe
scenario_title: Kafka 0.8.0 ISR 缩减与 ACK 边界（2013）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: requiredAcks=-1时，一个落后副本被移出ISR，会怎样改变这条消息的确认条件？
expected_output: 沿ISR成员与offset条件给出状态预测，并说明它不等于任意故障下不丢消息
out_of_scope: 不混用后来的min.insync.replicas默认值，不宣称ACK意味着所有分配副本都有消息
reason: 已读0.8.0固定tag Partition.scala正文；收窄到可核ISR缩减/ACK条件，避免缺少选举全契约时做无限故障保证。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：requiredAcks=-1时，一个落后副本被移出ISR，会怎样改变这条消息的确认条件？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-058
  status: sourced
  reason: 已读0.8.0固定tag Partition.scala正文；收窄到可核ISR缩减/ACK条件，避免缺少选举全契约时做无限故障保证。
  event: Kafka 0.8.0 ISR 缩减与 ACK 边界（2013）
  cutoff: Kafka0.8.0 Partition.scala机制快照，执行maybeShrinkIsr/checkEnoughReplicasReachOffset前
  initial_facts:
  - id: F1
    text: 分区分别维护assignedReplicas与inSyncReplicas。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 落后时间或消息差达到该版条件时可从ISR移出。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: requiredAcks负值要求当前ISR内replicas达到requiredOffset。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: maybeShrinkIsr更新ISR后会重算high watermark，源码明确ISR可缩到1。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 此实现按当前ISR而非所有分配副本判断全确认；若ISR只剩leader，其确认不证明已存在另一个已复制副本。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 这是版本源码推演，不冒充某次broker事故；全体ISR同时失败和unclean election不在已证明保证内。
  sources:
  - id: S1
    url: https://raw.githubusercontent.com/apache/kafka/0.8.0/core/src/main/scala/kafka/cluster/Partition.scala
    publisher: Apache Kafka maintainers
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
  - url: https://raw.githubusercontent.com/apache/kafka/0.8.0/core/src/main/scala/kafka/server/KafkaConfig.scala
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://raw.githubusercontent.com/apache/kafka/0.8.0/core/src/main/scala/kafka/cluster/Partition.scala
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 已读0.8.0固定tag Partition.scala正文；收窄到可核ISR缩减/ACK条件，避免缺少选举全契约时做无限故障保证。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-059

```yaml
id: ENG-059
decision: reframe
scenario_title: Remote Execution API v2.0.0 Action 缓存键工件
focus: evidence-selection
subdomain: developer-tooling-build
main_question: 检查什么输入最能暴露错误的远端缓存复用？
expected_output: 一个核验项与可推翻正确性的例子
out_of_scope: 不重新讲整个 Bazel 依赖图
reason: 固定原有已核proto tag v2.0.0；不将copyright2018推作tag发布日期。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：检查什么输入最能暴露错误的远端缓存复用？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-059
  status: sourced
  reason: 固定原有已核proto tag v2.0.0；不将copyright2018推作tag发布日期。
  event: Remote Execution API v2.0.0 Action 缓存键工件
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
    remediation_scope: 固定原有已核proto tag v2.0.0；不将copyright2018推作tag发布日期。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-060

```yaml
id: ENG-060
decision: retain
scenario_title: Heartbleed OpenSSL（2014）
focus: prediction-counterfactual
subdomain: security-isolation
main_question: TLS heartbeat 输入长度校验缺失导致内存泄漏；推演信任边界和测试覆盖盲点。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Heartbleed OpenSSL（2014）的单一范围；不要求最小代码片段与具体报文长度还需对照补丁，公告不提供完整测试覆盖历史。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：TLS heartbeat 输入长度校验缺失导致内存泄漏；推演信任边界和测试覆盖盲点。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-061

```yaml
id: ENG-061
decision: retain
scenario_title: Cloudflare 2024 年 6 月 DDoS 规则事故
focus: hypothesis-diagnosis
subdomain: reliability-diagnosis
main_question: 下一项什么观测能区分恶意流量、误伤与回源故障？
expected_output: 选择一项可同时区分三种解释的观测
out_of_scope: 不预先把保护误伤当作真实原因
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Cloudflare 2024 年 6 月 DDoS 规则事故的单一范围；不要求所有错误率有各自分母，不能把回源5xx与本服务不可用混用。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：下一项什么观测能区分恶意流量、误伤与回源故障？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-062

```yaml
id: ENG-062
decision: reframe
scenario_title: Netflix BBA-0 码率与缓冲取舍（2013实验/2014论文）
focus: constrained-decision
subdomain: performance-cost
main_question: 容量刚下降时，应只看瞬时吞吐立即降码率，还是结合已有缓冲选择下一段？
expected_output: 依论文BBA-0规则给出一次缓冲接近reservoir与充足时的两种决策边界
out_of_scope: 不编带宽轨迹或逐段时长，不把BBA-0当后来全部Netflix客户端算法
reason: Netflix博客不可达，补得Stanford与Netflix作者SIGCOMM2014原论文；冻结BBA-0、2013实验范围。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：容量刚下降时，应只看瞬时吞吐立即降码率，还是结合已有缓冲选择下一段？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-062
  status: sourced
  reason: Netflix博客不可达，补得Stanford与Netflix作者SIGCOMM2014原论文；冻结BBA-0、2013实验范围。
  event: Netflix BBA-0 码率与缓冲取舍（2013实验/2014论文）
  cutoff: 2014论文BBA-0机制工件，选择下一视频chunk码率前
  initial_facts:
  - id: F1
    text: 客户端一次下载一个固定播放时长chunk，缓冲以秒表示。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 播放器只在一个chunk到达后才能选下一段码率，无法取消当前下载。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: BBA-0在reservoir区域选最低码率，缓冲增大后按rate map上调。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 基线reservoir90秒、总缓冲240秒，码率切换采用离散档位与缓冲余量。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 作者实验显示BBA-0减少rebuffer与切换但牺牲部分video rate；缓冲充分的稳态与从空启动需区别，最大码率不是唯一目标。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 已读论文机制与实验，不把后来BBA-1/2的改进混入BBA-0规则；没有虚构的一次生产波动日志。
  sources:
  - id: S1
    url: https://yuba.stanford.edu/~huangty/sigc040-huang.pdf
    publisher: Stanford / Netflix; Huang, Johari, McKeown, Trunnell, Watson
    published_at: 2014-08
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://netflixtechblog.com/a-steady-state-approach-to-rate-adaptation-1b05b3a806f7
    result: 不可访问，未取得正文
  - url: https://yuba.stanford.edu/~huangty/sigc040-huang.pdf
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: Netflix博客不可达，补得Stanford与Netflix作者SIGCOMM2014原论文；冻结BBA-0、2013实验范围。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-063

```yaml
id: ENG-063
decision: reframe
scenario_title: Rust 1.39 async Future 的取消与析构边界（2019）
focus: prediction-counterfactual
subdomain: runtime-concurrency
main_question: 一个async Future尚停在await处就被drop，是否会继续执行await后的清理语句？
expected_output: 区分停止poll、释放已持有字段与执行后续异步业务三个结果
out_of_scope: 不声称撤销已完成外部副作用，不套用Tokio特定任务句柄取消规则
reason: 补读RFC2394的取消=drop模型与1.39官方析构规则；保留原取消/资源边界，排除RFC中尚未稳定的async closure和await宏语法。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：一个async Future尚停在await处就被drop，是否会继续执行await后的清理语句？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-063
  status: sourced
  reason: 补读RFC2394的取消=drop模型与1.39官方析构规则；保留原取消/资源边界，排除RFC中尚未稳定的async closure和await宏语法。
  event: Rust 1.39 async Future 的取消与析构边界（2019）
  cutoff: Rust1.39语言工件，Future已被poll至Pending、尚未被drop
  initial_facts:
  - id: F1
    text: async调用创建保存状态的Future，函数体需poll才推进。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 状态会保留跨await所需的已初始化值。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: RFC2394明确其惰性模型中取消通过drop Future实现。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: Rust1.39析构规则对已初始化字段递归析构；未初始化字段不被析构。
    source_ids:
    - S2
    availability: pre_decision
  outcome:
    id: O1
    text: 停止持有并drop该Future不会为了清理而恢复执行剩余函数体；它会按所有权析构已有状态，已发生的外部动作也不因此自动回滚。
    source_ids:
    - S1
    - S2
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 析构的具体外部效果取决于字段类型的Drop契约；泄漏、abort与运行时task所有权需另作界定。
  sources:
  - id: S1
    url: https://rust-lang.github.io/rfcs/2394-async_await.html
    publisher: Rust RFC authors / rust-lang
    published_at: '2018'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - O1
  - id: S2
    url: https://doc.rust-lang.org/1.39.0/reference/destructors.html
    publisher: Rust language team
    published_at: '2019'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
    - O1
  attempts:
  - url: https://blog.rust-lang.org/2019/11/07/Async-await-stable/
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://rust-lang.github.io/rfcs/2394-async_await.html
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  - url: https://doc.rust-lang.org/1.39.0/reference/destructors.html
    result: 通过CLI下载并实际读取1.39官方析构规则正文；未使用现行文档回填。
  phase2_conditions:
    original:
      scope: Future 的惰性执行与任务轮询不同于线程时，预测取消与资源释放边界。
    remediation_applied: true
    scope_change: 补读RFC2394的取消=drop模型与1.39官方析构规则；保留原取消/资源边界，排除RFC中尚未稳定的async closure和await宏语法。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-064

```yaml
id: ENG-064
decision: reframe
scenario_title: OCI Image Specification v1.0.0 的运行边界（2017）
focus: boundary-transfer
subdomain: architecture-api
main_question: 镜像符合v1.0.0格式，是否足以断言它能在另一CPU架构正常运行？
expected_output: 指出内容寻址/层配置保证，并据os、architecture指出运行兼容的必要前提
out_of_scope: 不把格式互操作等同内核、CPU、应用行为或安全保证
reason: 已实际读v1.0.0固定tag spec.md与config.md，消除原规范正文缺口。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：镜像符合v1.0.0格式，是否足以断言它能在另一CPU架构正常运行？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-064
  status: sourced
  reason: 已实际读v1.0.0固定tag spec.md与config.md，消除原规范正文缺口。
  event: OCI Image Specification v1.0.0 的运行边界（2017）
  cutoff: OCI image-spec v1.0.0，检查另一平台运行前
  initial_facts:
  - id: F1
    text: 镜像由manifest、filesystem layers和configuration组成。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 规范目标是构建、传输和准备运行的工具互操作。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 配置要求architecture与os字段，声明二进制适用平台。
    source_ids:
    - S2
    availability: pre_decision
  - id: E2
    text: 层内容摘要与配置确定镜像身份；这些数据还需转成runtime bundle由运行时执行。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: v1.0.0标准化可交换镜像工件与配置，平台字段仍是必要选择条件；符合格式不能逻辑推出任意平台执行成功。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 运行时内核能力、外部依赖与应用正确性不由格式合规单独证明。
  sources:
  - id: S1
    url: https://raw.githubusercontent.com/opencontainers/image-spec/v1.0.0/spec.md
    publisher: Open Container Initiative maintainers
    published_at: '2017-07-17'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E2
    - O1
  - id: S2
    url: https://raw.githubusercontent.com/opencontainers/image-spec/v1.0.0/config.md
    publisher: Open Container Initiative maintainers
    published_at: '2017-07-17'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E1
    - E2
    - O1
  attempts:
  - url: https://opencontainers.org/posts/announcements/2017-07-17-open-container-initiative-oci-releases-v1-0-of-container-standards/
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://raw.githubusercontent.com/opencontainers/image-spec/v1.0.0/spec.md
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  - url: https://raw.githubusercontent.com/opencontainers/image-spec/v1.0.0/config.md
    result: 本轮实际打开并读到architecture/os与ImageID规则。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 已实际读v1.0.0固定tag spec.md与config.md，消除原规范正文缺口。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-065

```yaml
id: ENG-065
decision: retain
scenario_title: Google Megastore（2011）
focus: constrained-decision
subdomain: distributed-consistency
main_question: 在 entity group 内外选择一致性边界，判断事务范围扩大对延迟和可用性的影响。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Google Megastore（2011）的单一范围；不要求不将每组少量写入经验阈值外推所有现代数据库。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：在 entity group 内外选择一致性边界，判断事务范围扩大对延迟和可用性的影响。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-066

```yaml
id: ENG-066
decision: retain
scenario_title: VS Code Remote Development（2019）
focus: boundary-transfer
subdomain: developer-tooling-build
main_question: 编辑器 UI 与执行环境分离时，重建扩展在本地/远端运行的职责边界。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留VS Code Remote Development（2019）的单一范围；不要求个别扩展可能不兼容，不能声称全部无需改动。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：编辑器 UI 与执行环境分离时，重建扩展在本地/远端运行的职责边界。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-067

```yaml
id: ENG-067
decision: retain
scenario_title: PostgreSQL MVCC VACUUM（2000s—）
focus: causal-modeling
subdomain: data-storage
main_question: 为何删除已经提交，旧版本占用仍不能立即释放？
expected_output: 一条可见性到回收受阻的因果链
out_of_scope: 不将所有表膨胀都归因于同一个长事务
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留PostgreSQL MVCC VACUUM（2000s—）的单一范围；不要求没有实际事务ID/日志；Phase4需将规范状态时序明确标为推演。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：为何删除已经提交，旧版本占用仍不能立即释放？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-068

```yaml
id: ENG-068
decision: retain
scenario_title: AWS us-east-1 2021 年 12 月网络事件
focus: constrained-decision
subdomain: reliability-diagnosis
main_question: 控制平面与内部网络拥塞导致连锁影响；评估监控和恢复操作的可达性。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留AWS us-east-1 2021 年 12 月网络事件的单一范围；不要求原始内部日志、配置值未公开；不编造。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：控制平面与内部网络拥塞导致连锁影响；评估监控和恢复操作的可达性。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-069

```yaml
id: ENG-069
decision: reframe
scenario_title: Capital One 2019 WAF角色凭据与对象权限边界
focus: causal-modeling
subdomain: security-isolation
main_question: 一处网络入口失守如何扩大为多个对象存储bucket访问，最小权限能在哪段限制后果？
expected_output: 画出入口、角色凭据、列举与复制权限的链条，区分阻断入口和限制授权
out_of_scope: 不编造原文未披露的SSRF请求或metadata端点，不把起诉指控当法院已认定技术事实
reason: 本轮下载并渲染阅读原complaint第5—6页，补齐WAF-Role凭据、list与sync链条；删除原候选未由该文明确给出的SSRF细节。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：一处网络入口失守如何扩大为多个对象存储bucket访问，最小权限能在哪段限制后果？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-069
  status: sourced
  reason: 本轮下载并渲染阅读原complaint第5—6页，补齐WAF-Role凭据、list与sync链条；删除原候选未由该文明确给出的SSRF细节。
  event: Capital One 2019 WAF角色凭据与对象权限边界
  cutoff: 2019-07-17收到外部泄露线索后、完整调查结论前
  initial_facts:
  - id: F1
    text: Capital One用云服务支持业务并存放申请及其他数据。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 2019-07-17外部报告称GitHub gist可能含其泄露数据。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 起诉材料引述公司调查称第一条命令取得WAF-Role凭据。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 后续命令使用该角色列举bucket，再复制其有权限读取的数据。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    id: O1
    text: 2019-07-29宣誓书记录公司已识别防火墙配置错误、角色凭据与对象权限组成的访问链；此为调查/指控记录，不是独立复现或已裁判认定。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 本原文未给全部IAM策略或精确SSRF报文，不能填造；后续司法结论不属于本题已核记录。
  sources:
  - id: S1
    url: https://www.justice.gov/usao-wdwa/press-release/file/1188626/dl?inline=
    publisher: US DOJ / FBI; 2019-07-29 complaint and affidavit
    published_at: '2019-07-29'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://www.justice.gov/usao-wdwa/pr/seattle-tech-worker-arrested-data-theft-involving-large-financial-services-company
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://www.justice.gov/usao-wdwa/press-release/file/1188626/dl?inline=
    result: 本轮下载公开PDF，用PDFKit渲染并实际逐页查看第4—6页；第6页第10—11段明确三条命令与角色权限，网页文本提取失败已由图像正文补核。
  phase2_conditions:
    original:
      scope: 从 SSRF 到云凭据和对象存储访问，分析最小权限与网络过滤的边界。
    remediation_applied: true
    scope_change: 本轮下载并渲染阅读原complaint第5—6页，补齐WAF-Role凭据、list与sync链条；删除原候选未由该文明确给出的SSRF细节。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-070

```yaml
id: ENG-070
decision: reframe
scenario_title: Go 1.1 已知阻塞系统调用与 M/P 交接（2013）
focus: prediction-counterfactual
subdomain: runtime-concurrency
main_question: 一个 goroutine 阻塞后，M 与 P 分别发生什么变化？
expected_output: 标出执行与可调度资源的时序
out_of_scope: 不做没有工作量输入的容量估计
reason: 固定原有已核go1.1 proc.c；候选2012仅是设计窗口，不再混称为该运行实现发布日。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：一个 goroutine 阻塞后，M 与 P 分别发生什么变化？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-070
  status: sourced
  reason: 固定原有已核go1.1 proc.c；候选2012仅是设计窗口，不再混称为该运行实现发布日。
  event: Go 1.1 已知阻塞系统调用与 M/P 交接（2013）
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
    remediation_scope: 固定原有已核go1.1 proc.c；候选2012仅是设计窗口，不再混称为该运行实现发布日。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-071

```yaml
id: ENG-071
decision: reframe
scenario_title: Crossplane Resource Composition Accepted 设计工件（v1.13.0归档）
focus: boundary-transfer
subdomain: architecture-api
main_question: 底层资源将admin-username改名后，如何保持公开username连接契约，并说明不能隐藏的边界？
expected_output: 沿官方Composition连接字段映射指出谁承担适配及一个语义不兼容条件
out_of_scope: 不把旧InfrastructureDefinition草案术语当v1.13部署API，不设计完整资源平台
reason: CLI取得v1.13.0归档Accepted设计；明确题目是该设计示例契约分析，不声称历史草案原样部署。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：底层资源将admin-username改名后，如何保持公开username连接契约，并说明不能隐藏的边界？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-071
  status: sourced
  reason: CLI取得v1.13.0归档Accepted设计；明确题目是该设计示例契约分析，不声称历史草案原样部署。
  event: Crossplane Resource Composition Accepted 设计工件（v1.13.0归档）
  cutoff: v1.13.0归档设计文档的Connection Details示例，替换底层字段前
  initial_facts:
  - id: F1
    text: 复合资源公开一组连接详情构成契约。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 底层资源也会暴露自己的连接secret键。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 示例用name:username把底层admin-username映射到公开username。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 契约要求每个连接详情恰由一项组成资源满足，不能天真合并可能同名的secrets。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 该设计工件通过显式映射隔离底层字段命名；底层语义变化或所需详情无法提供时，纯重命名不能维持原契约。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 归档页明确设计已演进；只评审示例中的连接契约，不宣称InfrastructureDefinition是v1.13可运行API。
  sources:
  - id: S1
    url: https://raw.githubusercontent.com/crossplane/crossplane/v1.13.0/design/design-doc-composition.md
    publisher: Crossplane / Nic Cope and maintainers
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
  - url: https://github.com/crossplane/crossplane/blob/main/design/design-doc-composition.md
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://raw.githubusercontent.com/crossplane/crossplane/v1.13.0/design/design-doc-composition.md
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: CLI取得v1.13.0归档Accepted设计；明确题目是该设计示例契约分析，不声称历史草案原样部署。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-072

```yaml
id: ENG-072
decision: reframe
scenario_title: Venice 2022 跨区域最终一致性工件
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: 只知道某地区摄入完成和系统采用跨区最终一致，能否推定另一区立即读到新值？
expected_output: 一个新鲜度边界预测和必要确认点
out_of_scope: 不擅自承诺强一致或精确复制延迟
reason: 固定2022-09-26开源设计说明，不要求缺失的精确ACK时点或最大复制延迟。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：只知道某地区摄入完成和系统采用跨区最终一致，能否推定另一区立即读到新值？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-072
  status: sourced
  reason: 固定2022-09-26开源设计说明，不要求缺失的精确ACK时点或最大复制延迟。
  event: Venice 2022 跨区域最终一致性工件
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
    remediation_scope: 固定2022-09-26开源设计说明，不要求缺失的精确ACK时点或最大复制延迟。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-073

```yaml
id: ENG-073
decision: reframe
scenario_title: Sapling 2022 专用后端的 clone 与历史下载
focus: boundary-transfer
subdomain: developer-tooling-build
main_question: 初次clone没有取回大部分历史时，随后访问未缓存历史的等待分别由本地和专用后端承担什么？
expected_output: 一张操作责任划分及一个离线边界
out_of_scope: 不重新设计整个版本控制系统
reason: 固定2022-11-15发布工件及专用后端，选择初始clone/后续历史查询的一条路径，不外推Git兼容后端。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：初次clone没有取回大部分历史时，随后访问未缓存历史的等待分别由本地和专用后端承担什么？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-073
  status: sourced
  reason: 固定2022-11-15发布工件及专用后端，选择初始clone/后续历史查询的一条路径，不外推Git兼容后端。
  event: Sapling 2022 专用后端的 clone 与历史下载
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
    remediation_scope: 固定2022-11-15发布工件及专用后端，选择初始clone/后续历史查询的一条路径，不外推Git兼容后端。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-074

```yaml
id: ENG-074
decision: retain
scenario_title: Google Borg 集群超售（2015）
focus: constrained-decision
subdomain: performance-cost
main_question: 混合在线与批处理工作负载时，评估资源预留、优先级和实际利用率。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Google Borg 集群超售（2015）的单一范围；不要求不可据此虚构当前cell资源分布或保证任意超售比例。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：混合在线与批处理工作负载时，评估资源预留、优先级和实际利用率。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-075

```yaml
id: ENG-075
decision: reframe
scenario_title: PostgreSQL 13 B-tree 去重的适用分布（2020）
focus: prediction-counterfactual
subdomain: data-storage
main_question: 重复键变少后，posting-list去重的空间收益会怎样变化，哪些索引根本不能用？
expected_output: 给出重复减少的定性空间预测与一条具体不适用条件
out_of_scope: 不编页面尺寸或键分布，不把体积缩小自动等同查询加速
reason: 正式采用预列prediction-counterfactual备用问题；固定PG13官方机制与限制，无须缺失的实际页面数量。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：重复键变少后，posting-list去重的空间收益会怎样变化，哪些索引根本不能用？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
  id: ENG-075
  status: sourced
  reason: 正式采用预列prediction-counterfactual备用问题；固定PG13官方机制与限制，无须缺失的实际页面数量。
  event: PostgreSQL 13 B-tree 去重的适用分布（2020）
  cutoff: PostgreSQL13 btree-implementation机制，判断一次索引分布变化前
  initial_facts:
  - id: F1
    text: B-tree叶项包含键与指向表行的TID。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 去重将相同键合成单个posting list，键只存一次、TID保留。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 重复值少时可合并键更少；写负载可能仍承担固定小开销。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: PG13明确INCLUDE索引及某些类型/非确定collation不适用去重。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 该实现可延迟叶页分裂并减轻重复项占用；收益依赖重复和适用条件，不能从功能存在推出任意索引有同等节省。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 原数量输入仍未获得，已正式换主问题和focus，不假装完成了页面级估算。
  sources:
  - id: S1
    url: https://www.postgresql.org/docs/13/btree-implementation.html
    publisher: PostgreSQL Global Development Group
    published_at: '2020'
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
  - url: https://www.postgresql.org/docs/13/btree-implementation.html
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original:
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
    remediation_applied: true
    scope_change: 正式采用预列prediction-counterfactual备用问题；固定PG13官方机制与限制，无须缺失的实际页面数量。
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-076

```yaml
id: ENG-076
decision: retain
scenario_title: Atlassian 2022 年云服务恢复事故
focus: constrained-decision
subdomain: reliability-diagnosis
main_question: 维护脚本错误移除站点资源且恢复耗时；判断数据恢复与重新供应的不同边界。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Atlassian 2022 年云服务恢复事故的单一范围；不要求PIR记录部分早期恢复点不一致后补救；不能简化为所有站点初次恢复都无数据差异。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：维护脚本错误移除站点资源且恢复耗时；判断数据恢复与重新供应的不同边界。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-077

```yaml
id: ENG-077
decision: retain
scenario_title: Kubernetes CVE-2018-1002105
focus: hypothesis-diagnosis
subdomain: security-isolation
main_question: 分析 API Server 权限提升链条，区分认证、授权与升级连接协议的信任边界。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Kubernetes CVE-2018-1002105的单一范围；不要求不能声称已有实际利用；公告明确没有简单审计检测方法。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：分析 API Server 权限提升链条，区分认证、授权与升级连接协议的信任边界。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-078

```yaml
id: ENG-078
decision: retain
scenario_title: Go GC Concurrent Mark Sweep（2015）
focus: causal-modeling
subdomain: runtime-concurrency
main_question: 从 stop-the-world 转向并发标记时，推理 write barrier 对暂停与吞吐的影响。
expected_output: 一项可检验的主判断及其适用边界
out_of_scope: 不外推为未核实的其他版本或生产负载
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Go GC Concurrent Mark Sweep（2015）的单一范围；不要求没有固定工作负载，不能精算吞吐损失。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：从 stop-the-world 转向并发标记时，推理 write barrier 对暂停与吞吐的影响。；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```

## ENG-079

```yaml
id: ENG-079
decision: retain
scenario_title: Kubernetes EndpointSlice 传播（2019—2021）
focus: prediction-counterfactual
subdomain: distributed-consistency
main_question: 控制面确认删除后，一条旧请求路径是否还可能被使用？
expected_output: 一个传播时序与能证明生效的观察点
out_of_scope: 不把多组件异步传播写成全局即时生效
reason: 已逐条复审原核源的初始事实、证据、结局与未知：保留Kubernetes EndpointSlice 传播（2019—2021）的单一范围；不要求新请求路由与已有连接需区分；全局所有节点生效需要各节点观测，单次API
  ACK不足。
admission: eligible
admission_reason: 该范围可直接用现有来源材料制作：控制面确认删除后，一条旧请求路径是否还可能被使用？；结果已有原始来源，所列未知不作为完成主问题的必需输入。
research:
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
material_review:
  opening_facts: 至少2条；仅事前可知事实，完整开场留Phase4
  evidence: 至少2条有不同作用的可追溯材料；按历史可知性区别释放
  outcome: 直接来源；因果归因保留作者边界
  phase4_not_started: true
```
