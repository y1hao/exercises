# Phase 3 产品题范围修订与补源

优先处理初轮未通过题。正式采用单一可回答问题；发布与规则工件不证明行为因果。不是完整Brief或ready。

## PRO-001

```yaml
id: PRO-001
decision: replace
scenario_title: Google Wave 2009预览至2010独立产品投入复核
focus: hypothesis-diagnosis
subdomain: user-research-value
main_question: 开发者对实时协作演示叫好，能否区分日常任务价值与技术新鲜感？
expected_output: 一个可核对的判断、来源支持的机制及能推翻它的条件
out_of_scope: 不把公告、相关性或回顾等同已识别的采用/留存因果；不补造指标、条款或任务日志
reason: Notion原重做时间与因果材料不足，真实换为Google Wave的任务价值与技术喝彩判断；保留诊断动作，不声称已经识别失败原因。
admission: eligible
admission_reason: 至少2条事前事实、2条实质证据和直接来源支持的真实交付/观察结局已具备；准入制作并非ready。
research:
  id: PRO-001
  status: sourced
  reason: Notion原重做时间与因果材料不足，真实换为Google Wave的任务价值与技术喝彩判断；保留诊断动作，不声称已经识别失败原因。
  event: Google Wave 2009预览至2010独立产品投入复核
  cutoff: 2009开发者预览后、2010-08-04停止独立开发公告前；不把采用不足先放首轮
  initial_facts:
  - id: F1
    text: 2009开发者预览已展示浏览器逐字实时输入、拖拽文件和历史回放。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 展示时开发者热烈回应；团队当时仍不确定用户会如何使用这种沟通方式。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: Google记录了实时图片共享、上下文拼写检查和第三方机器人等实际用例。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 2010负责人称虽有忠实用户，采用未达预期；该阈值与分群未公开。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 2010-08-04 Google宣布不再把Wave作为独立产品继续开发，并保留开源技术和数据迁出安排。
    source_ids:
    - S1
  interpretation: 来源只确认直接记载的规则、行为和结果；因果链为可检验维护者分析，不以历史结果倒判唯一理性选择。
  unknowns:
  - 完整内部决策与反事实结果未公开；公司主张和当事人回忆需单独标明
  sources:
  - id: S1
    url: https://googleblog.blogspot.com/2010/08/update-on-google-wave.html
    publisher: Google / Urs Hölzle
    published_at: '2010-08-04'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮重新打开并阅读所列来源正文，按新范围逐条核对；不使用搜索摘要替代。
  phase2_conditions: 不替创始人编造动机或评判全部重做策略
```

## PRO-002

```yaml
id: PRO-002
decision: retain
scenario_title: Pinterest 2015 Pin It 保存路径改进
focus: causal-modeling
subdomain: ux-activation
main_question: 流程内捕获比回到应用搜索，具体减少了哪一步摩擦？
expected_output: 一条任务路径与一项行为预测
out_of_scope: 不计算没有漏斗数据的激活提升
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-002
  status: sourced
  reason: 锁定 2015-04-02 按钮改进；官方说明路径和点击变化，足以作任务摩擦预测。
  event: Pinterest 2015 Pin It 保存路径改进
  cutoff: 2015-04-02 新版功能已介绍、行为效果尚未揭晓
  initial_facts:
  - id: F1
    text: Pin It 用于收藏在外部网页发现的内容。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 新版包含 visual selector 和查找/创建 board 的操作。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 官方称新路径只需 couple of clicks、约为原先一半。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 官方提供浏览器按钮安装入口；不需要重新在 Pinterest 找原网页内容。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 改进版已发布，官方描述保存步骤缩短；无激活漏斗提升的可核因果值。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://newsroom-archive.pinterest.com/the-save-button-for-the-internet
    publisher: Pinterest / Cesar I.
    published_at: '2015-04-02'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 不计算没有漏斗数据的激活提升
```

## PRO-003

```yaml
id: PRO-003
decision: retain
scenario_title: Adobe Creative Suite 转订阅 CC（2013）
focus: prediction-counterfactual
subdomain: pricing-monetization
main_question: 订阅替代永久授权时，为什么收入确认节奏可能暂时变差，而订阅基础仍在扩大？
expected_output: 一个方向预测及ARR、收入、现金的口径区别
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-003
  status: sourced
  reason: 同期 SEC 文件确认转向日期、保留永久授权的边界和后续经营结果；财报收入不等于现金流。
  event: Adobe Creative Suite 转订阅 CC（2013）
  cutoff: 2013 年 5 月宣布后，Q3 结果尚未公开
  initial_facts:
  - id: F1
    text: Creative Cloud 2012 已提供订阅。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 2013 年 5 月宣布新功能仅给 CC；CS6 仍可永久购买但无后续大版本。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 财报称订阅按期间确认收入，转型期间永久授权收入下降。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: Q3 末付费订阅 1,031,000，Creative ARR 655 百万美元。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 截至 2013 Q3 订阅增长，财报记录收入下降及利润压力；不能把 ARR 当收到的现金。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  - 若来源为事后回顾，仅确认其明确记载的当时已知观察或已实施规则；不把后续效果当作事前可知。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/796343/000079634313000058/adbe10qq313.htm
    publisher: Adobe / SEC
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-004

```yaml
id: PRO-004
decision: reframe
scenario_title: Strava 2024年末榜单异常清理与比较信号
focus: hypothesis-diagnosis
subdomain: retention-workflow
main_question: 榜单上的异常高名次更支持真实运动表现，还是记录/活动类型污染？
expected_output: 一个可核对的判断、来源支持的机制及能推翻它的条件
out_of_scope: 不把公告、相关性或回顾等同已识别的采用/留存因果；不补造指标、条款或任务日志
reason: 早期回访因果缺数据；正式改为2024榜单比较信号的竞争假说诊断，不再推断排行榜创造留存。
admission: eligible
admission_reason: 至少2条事前事实、2条实质证据和直接来源支持的真实交付/观察结局已具备；准入制作并非ready。
research:
  id: PRO-004
  status: sourced
  reason: 早期回访因果缺数据；正式改为2024榜单比较信号的竞争假说诊断，不再推断排行榜创造留存。
  event: Strava 2024年末榜单异常清理与比较信号
  cutoff: 2024-12规则清理前；后发当事人文章明确描述既有规则与此后结果
  initial_facts:
  - id: F1
    text: Segment榜单按已记录活动比较成绩，并长期接受社区手动标记。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 此前规则重点标记破世界纪录及异常爬升的骑行，未破纪录的异常仍可漏过。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 规则系统2024-12清理掉650万项异常活动，是清理数量而非独立作弊人数。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 后续ML会识别车辆、误标跑步的骑行等类型；GPS损坏也能生成异常，不能把异常一律称作弊。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 2024-12规则清理后，2025-05跑步榜又移除445万异常活动；榜单数据质量是持续问题，名次不保证同条件实力。
    source_ids:
    - S1
  interpretation: 来源只确认直接记载的规则、行为和结果；因果链为可检验维护者分析，不以历史结果倒判唯一理性选择。
  unknowns:
  - 完整内部决策与反事实结果未公开；公司主张和当事人回忆需单独标明
  sources:
  - id: S1
    url: https://stories.strava.com/es/articles/keeping-stravas-segment-leaderboards-fair-an-engineers-perspective
    publisher: Strava / James Wang
    published_at: '2026-03-06'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮重新打开并阅读所列来源正文，按新范围逐条核对；不使用搜索摘要替代。
  phase2_conditions: 不从打开频率直接推断产品创造了留存
```

## PRO-005

```yaml
id: PRO-005
decision: retain
scenario_title: Dropbox 推荐好友送空间（2008—2010）
focus: constrained-decision
subdomain: distribution-growth
main_question: 是否保留双边空间奖励，并用什么滥用边界限制它？
expected_output: 一项激励选择及质量/滥用反例
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-005
  status: sourced
  reason: 创始人演讲原始幻灯片确认双边激励、产品传播与自报注册结果；保留效果识别限制。
  event: Dropbox 推荐好友送空间（2008—2010）
  cutoff: 推荐方案已说明、演讲的增长结果尚未揭晓
  initial_facts:
  - id: F1
    text: Drew Houston 说明推荐计划有双边激励。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 激励为额外空间，适合分享和存储任务；具体 MB 不从后来的规则回填。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 2010 演讲称注册增 60%，属于创始人自报，未公开实验设计。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 幻灯片区分推荐计划与共享文件夹等其他传播来源。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 原始演讲自报推荐计划提高注册；未证明长期留存、单位成本或排除作弊。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  - 若来源为事后回顾，仅确认其明确记载的当时已知观察或已实施规则；不把后续效果当作事前可知。
  sources:
  - id: S1
    url: https://andrewchen.com/wp-content/uploads/2022/08/dropbox-startuplessonslearned-100423230315-phpapp02.pdf
    publisher: Drew Houston；Andrew Chen 保存原始幻灯片
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-006

```yaml
id: PRO-006
decision: retain
scenario_title: Nintendo Switch 混合主机（2017）
focus: hypothesis-diagnosis
subdomain: strategy-pivot
main_question: 便携与客厅结合是否更能服务这类用户的任务？
expected_output: 一个目标用户假说及反例
out_of_scope: 不编造内部定位会议或完整主机战争
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-006
  status: sourced
  reason: 同期 Nintendo 产品公告描述客厅、桌面、掌机模式及对应任务，足以限定单一使用情境。
  event: Nintendo Switch 混合主机（2017）
  cutoff: 2017-01-13 公布规格后、正式发售前
  initial_facts:
  - id: F1
    text: Switch 可接电视或使用自带屏幕便携玩。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Joy-Con 可拆分，支持两位玩家共用和本地联机。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 官方设定随地点、内容及个人偏好选模式。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 同发布材料把 1-2-Switch 描述为面对面聚会场景。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 混合设备及对应游戏公开；公告不证明用户偏好、销量或来自 Wii U 教训的因果解释。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.nintendo.co.jp/corporate/release/en/2017/170113.html
    publisher: Nintendo
    published_at: '2017-01-13'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 不编造内部定位会议或完整主机战争
```

## PRO-007

```yaml
id: PRO-007
decision: reframe
scenario_title: Airbnb 2022 Split Stays：长住供给增加与可完成预订
focus: evidence-selection
subdomain: network-marketplaces
main_question: Split Stays 展示更多房源，是否就解决了长住匹配？在“结果房源数”与“两段均有可订日期且完成两次确认的行程比例”中选一个主要验证量并说明理由。
expected_output: 一段证据取舍与失败条件。
out_of_scope: 只看两段长住匹配；不估 2008 年城市供需，不把展示增长当成交增长。
reason: 原 2008–2011 供需数不足；正式采用证据选择备用动作，改为有发布快照的 2022 Split Stays。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-007
  status: sourced
  reason: 原 2008–2011 供需数不足；正式采用证据选择备用动作，改为有发布快照的 2022 Split Stays。
  event: Airbnb 2022 Split Stays：长住供给增加与可完成预订
  cutoff: 2022-05-11 发布方案评审；实际采用方案与效果陈述后置
  initial_facts:
  - id: F1
    text: 发布说明称此前三个月近一半住宿夜数来自一周及以上行程。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 原本一次搜索只找一套覆盖整个长住日期的房源。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 拆成两套房源后可组合不同日期供给；官方称长住搜索通常能多显示约40%的房源，这是展示口径。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 地图显示两段距离和顺序，旅客仍须一次一套地分别完成两次预订，组合可见性不等于两单完成。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 2022年夏季发布实际推出Split Stays；40%是公司对可显示房源的描述，未披露对应成交或履约提升。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 两段同时可订、确认流失及履约率未公开；不构造城市订单表。
  sources:
  - id: S1
    url: https://news.airbnb.com/2022-summer-release
    publisher: Airbnb
    published_at: '2022-05-11'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索 Airbnb S-1；尝试读取 SEC 2020 S-1/A，返回正文超过 4MB 上限；检索所得 2020 总量不能代替早期本地分布。
  - url: https://news.airbnb.com/2022-summer-release
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 建议采用预设的证据选择备用问题（尚未改变focus），选择最高价值供需数据；仍需早期具体事件证据，禁止补合成供需表。
    remediation_applied: true
    scope_change: 原 2008–2011 供需数不足；正式采用证据选择备用动作，改为有发布快照的 2022 Split Stays。
```

## PRO-008

```yaml
id: PRO-008
decision: reframe
scenario_title: Slack 2019披露的自助采用转组织销售
focus: evidence-selection
subdomain: b2b-adoption
main_question: 免费团队已在使用时，搜索历史需求与高管采购承诺哪个更接近组织付费证据？
expected_output: 一个可核对的判断、来源支持的机制及能推翻它的条件
out_of_scope: 不把公告、相关性或回顾等同已识别的采用/留存因果；不补造指标、条款或任务日志
reason: 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。
admission: eligible
admission_reason: 至少2条事前事实、2条实质证据和直接来源支持的真实交付/观察结局已具备；准入制作并非ready。
research:
  id: PRO-008
  status: sourced
  reason: 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。
  event: Slack 2019披露的自助采用转组织销售
  cutoff: 2019-05-13版功能与销售流程披露后，判断组织付费证据前
  initial_facts:
  - id: F1
    text: 2019版Free允许直接开始使用，无需付款或正式销售互动。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Free可搜索消息上限10000条，Plus提供SSO；这是该版功能边界。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 披露的销售流程从champion和自助POC进入C-suite与业务负责人；使用者不必拥有预算。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 公司记录FY2018收入约10%来自此前免费、当年转付费的组织，不能当免费用户转化率。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 2019招股书已记录自助与销售互补的实际流程和免费转付费收入；没有单客户合同或因果转化率。
    source_ids:
    - S1
  interpretation: 来源只确认直接记载的规则、行为和结果；因果链为可检验维护者分析，不以历史结果倒判唯一理性选择。
  unknowns:
  - 完整内部决策与反事实结果未公开；公司主张和当事人回忆需单独标明
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1764925/000162828019006616/slacks-1a1.htm
    publisher: Slack / SEC
    published_at: '2019-05-13'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮重新打开并阅读所列来源正文，按新范围逐条核对；不使用搜索摘要替代。
  phase2_conditions: 不概括三年全部企业扩散史
```

## PRO-009

```yaml
id: PRO-009
decision: retain
scenario_title: Netflix 1998-04-14 DVD 邮寄租赁上线
focus: causal-modeling
subdomain: user-research-value
main_question: 该方案最主要减少了用户哪一种租赁摩擦？
expected_output: 一条用户任务因果链及剩余成本
out_of_scope: 不提前使用后续订阅或流媒体结果
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-009
  status: sourced
  reason: 找到 1998 原始发布，明确按次计价、邮寄与选片路径，不借后续订阅结果。
  event: Netflix 1998-04-14 DVD 邮寄租赁上线
  cutoff: 1998-04-14 发布条件已知、采用结果未知
  initial_facts:
  - id: F1
    text: 可在线选租或购买超过 900 DVD 标题。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 一次在家租七天，首两部每部 4 美元，同单额外标题每部 3 美元。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告承诺当日发货、美国境内两至三天收到。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: CEO 把广泛 DVD 选择与便利作为承诺；不是测量后的用户动机。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 按次付费邮寄租赁正式开放；送达等待仍存在，不引入后续订阅或流媒体。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://about.netflix.com/en/news/first-online-dvd-rental-store-opens
    publisher: Netflix
    published_at: '1998-04-14'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 不提前使用后续订阅或流媒体结果
```

## PRO-010

```yaml
id: PRO-010
decision: reframe
scenario_title: Duolingo 约2019取消streak与每日目标绑定的A/B试验
focus: hypothesis-diagnosis
subdomain: ux-activation
main_question: 降低连续记录门槛后，回访提高能否推出每天学习任务完成得更多？
expected_output: 一个可核对的判断、来源支持的机制及能推翻它的条件
out_of_scope: 不把公告、相关性或回顾等同已识别的采用/留存因果；不补造指标、条款或任务日志
reason: 将未定位的2010s改动重锚为官方明确描述的单次A/B试验；真实结果同时提供收益与代价。
admission: eligible
admission_reason: 至少2条事前事实、2条实质证据和直接来源支持的真实交付/观察结局已具备；准入制作并非ready。
research:
  id: PRO-010
  status: sourced
  reason: 将未定位的2010s改动重锚为官方明确描述的单次A/B试验；真实结果同时提供收益与代价。
  event: Duolingo 约2019取消streak与每日目标绑定的A/B试验
  cutoff: 文章所称约一年前的规则试验开始前；约2019，内部精确日未知
  initial_facts:
  - id: F1
    text: 旧版必须达到自己设置的每日目标才能延长streak。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 团队已观察到有些连续两天使用的人无streak，目标越高越明显。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 试验把完成一课即可续streak与旧规则比较，报告D14留存相对增加3.3%。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 同时较少学习者完成每日目标；更多日活和总学习时间不能直接证明语言能力提高。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 分离机制后日活相对增加1%、20天内日学习者有streak的比例相对增加10.5%；公布者承认每日目标完成的代价。
    source_ids:
    - S1
  interpretation: 来源只确认直接记载的规则、行为和结果；因果链为可检验维护者分析，不以历史结果倒判唯一理性选择。
  unknowns:
  - 完整内部决策与反事实结果未公开；公司主张和当事人回忆需单独标明
  sources:
  - id: S1
    url: https://blog.duolingo.com/improving-the-streak/
    publisher: Duolingo
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮重新打开并阅读所列来源正文，按新范围逐条核对；不使用搜索摘要替代。
  phase2_conditions: 不把签到或打开次数作为学习成效
```

## PRO-011

```yaml
id: PRO-011
decision: reframe
scenario_title: Figma 2025 席位审批：把意外升级的控制点提前
focus: causal-modeling
subdomain: pricing-monetization
main_question: 在既有“用户先升级、管理员账前审核”与新“付费权限先审批”之间，画出意外增席账单如何产生，并判断提前审批最直接改变哪个因果环节。
expected_output: 一条升级→审批→计费的因果链与一个代价。
out_of_scope: 只看2024年公告中的2025席位转换；不拼接2016年以来套餐或声称采购已成功。
reason: 旧范围过宽且缺历史套餐版本；冻结2024-12-10公告中的审批与单人席位机制，不依赖后来补入的临时权限细节。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-011
  status: sourced
  reason: 旧范围过宽且缺历史套餐版本；冻结2024-12-10公告中的审批与单人席位机制，不依赖后来补入的临时权限细节。
  event: Figma 2025 席位审批：把意外升级的控制点提前
  cutoff: 2024-12-10 新计费安排公布时
  initial_facts:
  - id: F1
    text: 旧流程允许用户驱动升级，再由管理员于账单前审核。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司宣布2025-03-11起改变席位和计费安排，付费权限的管理员控制是明确问题。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 新默认流程要求会产生费用的升级先经管理员批准。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 旧按产品分开席位改为每位用户一个席位类型，将权限选择与账单归属合并；审批摩擦仍可能影响实际协作。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 公告确定2025-03-11实施新安排；这是公布的产品政策，不是已证实的采购转化或成本降低。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 页面说明后续补充过临时席位信息；本题不将该细节回填到2024-12-10首版。
  - 未披露审批对协作速度或续费的实验结果。
  sources:
  - id: S1
    url: https://www.figma.com/blog/billing-experience-update-2025/
    publisher: Figma / Ben Stern
    published_at: '2024-12-10'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - url: https://www.figma.com/blog/billing-experience-update-2025/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 不混用六年套餐或直接推出企业采购成功
    remediation_applied: true
    scope_change: 旧范围过宽且缺历史套餐版本；冻结2024-12-10公告中的审批与单人席位机制，不依赖后来补入的临时权限细节。
```

## PRO-012

```yaml
id: PRO-012
decision: retain
scenario_title: GitHub 2016-09-14 Pull Request Reviews 发布
focus: prediction-counterfactual
subdomain: retention-workflow
main_question: 把零散行内评论合并为正式审查状态，会怎样改变作者判断“可以合并”的信号？
expected_output: 一项流程预测及不能单靠approve保证的条件
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-012
  status: sourced
  reason: 2016 官方上线公告直接确认正式 Review 状态和评论打包能力。
  event: GitHub 2016-09-14 Pull Request Reviews 发布
  cutoff: 2016-09-14 功能公布时；此前只有行评论的体验作已知背景
  initial_facts:
  - id: F1
    text: 原有 PR 可对具体代码行留言。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Reviews 增加正式 approve 和 request changes 状态。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 可留 review summary。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 评论可在提交前删除、编辑、打包。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: Reviews 在所有 PR 可用；协作采用和留存提升不在公告中证明。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://github.blog/news-insights/product-news/a-whole-new-github-universe-announcing-new-tools-forums-and-features/
    publisher: GitHub
    published_at: '2016-09-14'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-013

```yaml
id: PRO-013
decision: replace
scenario_title: Airbnb 2014跨端推荐计划重建
focus: constrained-decision
subdomain: distribution-growth
main_question: 能同时修复移动端邀请缺口与改进邀请文案时，应把渠道控制投入在哪个可测环节？
expected_output: 一个可核对的判断、来源支持的机制及能推翻它的条件
out_of_scope: 不把公告、相关性或回顾等同已识别的采用/留存因果；不补造指标、条款或任务日志
reason: 正式放弃未核Craigslist hack，保留Airbnb但换为有当事人完整测量记录的独立推荐节点；区别Dropbox空间激励在于跨端路径与旅行完成口径。
admission: eligible
admission_reason: 至少2条事前事实、2条实质证据和直接来源支持的真实交付/观察结局已具备；准入制作并非ready。
research:
  id: PRO-013
  status: sourced
  reason: 正式放弃未核Craigslist hack，保留Airbnb但换为有当事人完整测量记录的独立推荐节点；区别Dropbox空间激励在于跨端路径与旅行完成口径。
  event: Airbnb 2014跨端推荐计划重建
  cutoff: 2014推荐计划重建前，既有计划入口与奖励规则可知；不先给A/B胜者
  initial_facts:
  - id: F1
    text: 旧推荐计划网页难找，移动app中没有该入口。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 新计划在受邀者完成首旅后向双方给25美元旅行抵扣，不是下载即付现金。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 重建覆盖web、iOS、Android，并追踪邀请到新guest/host的漏斗而非只数下载。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 同期文案A/B把“自己得25”与“给朋友25”比较，后者全球表现较好，未公开完整分群效应。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 公司报告重建后部分市场推荐带来的预订增加逾25%，又继续做入口和文案迭代；不是对Craigslist漏洞的证实。
    source_ids:
    - S1
  interpretation: 来源只确认直接记载的规则、行为和结果；因果链为可检验维护者分析，不以历史结果倒判唯一理性选择。
  unknowns:
  - 完整内部决策与反事实结果未公开；公司主张和当事人回忆需单独标明
  sources:
  - id: S1
    url: https://medium.com/airbnb-engineering/hacking-word-of-mouth-making-referrals-work-for-airbnb-46468e7790a6
    publisher: Airbnb / Jason Bosinoff
    published_at: '2014-03-27'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - Airbnb 官方域与创始人采访检索；阅读 Boston Hospitality Review 正文；检索结果中的增长故事未当作一手证据。
  - 本轮重新打开并阅读所列来源正文，按新范围逐条核对；不使用搜索摘要替代。
  phase2_conditions: 保持换题条件；不可据二手叙事自动晋级或替换。
```

## PRO-014

```yaml
id: PRO-014
decision: reframe
scenario_title: Nintendo Wii 2006：用直觉操作扩大游戏人口
focus: constrained-decision
subdomain: strategy-pivot
main_question: 在已有DS触控尝试和扩大非玩家群体的目标下，Wii应把有限产品差异化投入到传统操作熟练者还是全家可上手的控制方式？选一个并说明牺牲。
expected_output: 一个目标用户选择、两个事前约束和一项代价。
out_of_scope: 不重建未读到的访谈，不用Wii销量反推2006决策必然正确。
reason: 用2006年报的事前目标与2007财报的真实推出结果替代不可访问的Iwata Asks访谈。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-014
  status: sourced
  reason: 用2006年报的事前目标与2007财报的真实推出结果替代不可访问的Iwata Asks访谈。
  event: Nintendo Wii 2006：用直觉操作扩大游戏人口
  cutoff: 2006 Wii发布前；2007销量后置
  initial_facts:
  - id: F1
    text: 2006年报明确提出跨年龄、性别与文化扩大游戏人口。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司此前已用DS触控、语音和Touch Generations面向较少玩传统游戏的人。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 年报将Wii Remote的直觉操作作为全家可玩的差异化方向，而不是只描述画面竞争。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 既有DS实践支持降低操作门槛的可行性；它不能独立证明新家用机市场一定同样接受。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 2007-04-26财报确认Wii已推出，首五个月硬件销售584万台；公司对扩大用户的解释仍是当事人归因。
    source_ids:
    - S2
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 销量不能隔离控制器、价格、游戏内容、渠道的独立作用。
  sources:
  - id: S1
    url: https://www.nintendo.co.jp/kessan/annual0603e.pdf
    publisher: Nintendo
    published_at: '2006'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
  - id: S2
    url: https://www.nintendo.co.jp/ir/pdf/2007/070426e.pdf
    publisher: Nintendo
    published_at: '2007-04-26'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - O1
  attempts:
  - 检索 Iwata Asks Wii Hardware；原始 iwataasks.nintendo.com 返回 502；Nintendo UK Introduction 页面实际正文仅导航，未冒充读到访谈。
  - url: https://www.nintendo.co.jp/kessan/annual0603e.pdf
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  - url: https://www.nintendo.co.jp/ir/pdf/2007/070426e.pdf
    result: 实际打开并阅读PDF第3页Wii推出与584万台销售条目。
  phase2_conditions:
    original: 需恢复官方访谈或可靠原始存档。
    remediation_applied: true
    scope_change: 用2006年报的事前目标与2007财报的真实推出结果替代不可访问的Iwata Asks访谈。
```

## PRO-015

```yaml
id: PRO-015
decision: reframe
scenario_title: Etsy 2015招股书版定制商品对话闭环
focus: causal-modeling
subdomain: network-marketplaces
main_question: 对订购定制家具的买方，卖家对话怎样弥补通用商品列表无法表达的匹配条件？
expected_output: 一个可核对的判断、来源支持的机制及能推翻它的条件
out_of_scope: 不把公告、相关性或回顾等同已识别的采用/留存因果；不补造指标、条款或任务日志
reason: 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。
admission: eligible
admission_reason: 至少2条事前事实、2条实质证据和直接来源支持的真实交付/观察结局已具备；准入制作并非ready。
research:
  id: PRO-015
  status: sourced
  reason: 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。
  event: Etsy 2015招股书版定制商品对话闭环
  cutoff: 2015-03-04披露的产品快照；一项定制需求的选择前
  initial_facts:
  - id: F1
    text: 2015市场支持手作、定制和复古商品，包括定制家具等非标准品。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 买方可按颜色、价格、位置等筛选，并直接与卖家沟通定制或个性化。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: Conversations被用于讨论订单、定制要求和生产过程；2014成员共发2.16亿消息但非每单因果效果。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 招股书把独特性和制作来源视为买方动机，明确是公司判断，非已识别护城河。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 截至2015披露版已有定制商品与Conversations交易沟通流程；特色供给需要表达任务需求，消息总量不能证明成交增量。
    source_ids:
    - S1
  interpretation: 来源只确认直接记载的规则、行为和结果；因果链为可检验维护者分析，不以历史结果倒判唯一理性选择。
  unknowns:
  - 完整内部决策与反事实结果未公开；公司主张和当事人回忆需单独标明
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1370637/000119312515077045/d806992ds1.htm
    publisher: Etsy / SEC
    published_at: '2015-03-04'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮重新打开并阅读所列来源正文，按新范围逐条核对；不使用搜索摘要替代。
  phase2_conditions: 不把垂直社区本身当作护城河证明
```

## PRO-016

```yaml
id: PRO-016
decision: retain
scenario_title: MongoDB Atlas 2016-06-28 上线
focus: prediction-counterfactual
subdomain: b2b-adoption
main_question: 开源数据库从下载自管到云端托管，分析用户身份、渠道和销售方式的变化。
expected_output: 一个明确判断、可推翻条件及证据边界
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-016
  status: sourced
  reason: 2016 原始公告确认托管服务及自服务选项，可执行用户任务/运维责任迁移的预测。
  event: MongoDB Atlas 2016-06-28 上线
  cutoff: 2016-06-28 公告条件已知、后续商业表现未知
  initial_facts:
  - id: F1
    text: Atlas 提供按需云数据库及基础设施管理，初期运行 AWS。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公告让用户通过 cloud/atlas 直接取得服务。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 服务承担部署、扩展及运行管理。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: Azure 和 GCP 是公告中的后续计划，不能写成首日已提供。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 托管服务推出；用户类型及销售结构实际变化仍需后续队列资料，不把营销效率承诺当结果。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.mongodb.com/company/newsroom/press-releases/mongodb-unveils-mongodb-atlas-the-new-industry-standard-for-database-as-a-service
    publisher: MongoDB
    published_at: '2016-06-28'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-017

```yaml
id: PRO-017
decision: retain
scenario_title: Slack 2013 预览前邀请外部团队试用
focus: boundary-transfer
subdomain: user-research-value
main_question: 内部团队用得顺，能否直接推出120人团队也用得顺？
expected_output: 指出团队规模变化导致失效的一条迁移边界
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-017
  status: sourced
  reason: 创始人回顾提供内部工具对外试用和团队规模差异的直接观察，足以测试 dogfooding 迁移边界。
  event: Slack 2013 预览前邀请外部团队试用
  cutoff: 最初几个朋友团队已同意试用，尚未扩到Rdio更大团队；具体日未知
  initial_facts:
  - id: F1
    text: Butterfield 回顾最初靠内部团队验证工具。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 团队向朋友公司请求试用，包含 Cozy、Rdio。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 他称初期邀请约六至十家公司。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: Rdio 从前端小组扩展到工程组及约 120 人，公司观察到大团队体验问题并修改产品。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 据创始人回顾，外部规模差异促使产品修改，2013-08 发布 preview；回顾不能证明所有企业均适用。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  - 若来源为事后回顾，仅确认其明确记载的当时已知观察或已实施规则；不把后续效果当作事前可知。
  sources:
  - id: S1
    url: https://review.firstround.com/from-0-to-1b-slacks-founder-shares-their-epic-launch-strategy/
    publisher: First Round Review / Stewart Butterfield 访谈
    published_at: '2015-02-26'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-018

```yaml
id: PRO-018
decision: retain
scenario_title: Snapchat 2011—2012 短暂照片消息
focus: prediction-counterfactual
subdomain: ux-activation
main_question: 短暂照片定位更可能服务“精修展示”还是课间随手沟通？
expected_output: 一项使用场景预测；区分创始人观察与心理归因
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-018
  status: sourced
  reason: 同期创始人文章给出非正式沟通目标与当时用户反馈；预测表达行为而不宣称因果。
  event: Snapchat 2011—2012 短暂照片消息
  cutoff: 2012-05-10回述的2011发布后、尚未揭晓学校使用观察的产品判断窗口
  initial_facts:
  - id: F1
    text: Evan 2012 年称希望分享笨拙自拍和朋友间搞怪照片。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 原型 2011 夏迭代、同年九月进 App Store。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 创始人称联系用户后发现很多高中生在课间传照片。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 他说服务器流量在上学日较高、周末较低；是当事人自报而非完整数据。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 同期自报出现非正式传话用途；不能量化阅后即焚本身提高消息量，且短暂展示不等于不可保存。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  - 若来源为事后回顾，仅确认其明确记载的当时已知观察或已实施规则；不把后续效果当作事前可知。
  sources:
  - id: S1
    url: https://newsroom.snap.com/lets-chat
    publisher: Snap / Evan Spiegel
    published_at: '2012-05-10'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-019

```yaml
id: PRO-019
decision: reframe
scenario_title: AWS Lambda 2020：100ms到1ms计费粒度的有限计算
focus: quantitative-calibration
subdomain: pricing-monetization
main_question: 对官方日志中27.55ms执行、1GB内存的调用，旧100ms取整与新1ms取整各计多少时长、该次时长费用下降多少？为什么不能把同一百分比直接称为整月总账单降幅？
expected_output: 100ms与28ms、72%时长费用下降，以及请求费和调用分布的边界。
out_of_scope: 不使用作者另设的10万用户生产情景；不补工作负载，不算未知月账单。
reason: 原2014preview缺可核实际负载；保留数量动作，明确改成2020-12-01官方计费变更及实测REPORT。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-019
  status: sourced
  reason: 原2014preview缺可核实际负载；保留数量动作，明确改成2020-12-01官方计费变更及实测REPORT。
  event: AWS Lambda 2020：100ms到1ms计费粒度的有限计算
  cutoff: 2020-12-01 计费规则发布时
  initial_facts:
  - id: F1
    text: 此前Lambda除按请求计费，还将执行时长向上取整至100ms。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 时长费用取决于配置内存；官方展示同一应用1024MB内存的真实REPORT，不是只按请求收费。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 新规则向上取整到1ms且无最短时长，官方展示27.55ms执行计为28ms；对该时长旧规则计为100ms。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 公告明确请求费用不变；调用数与时长分布会决定整月账单，单次时长取整节省不能直接外推总额。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: AWS从2020年12月账期向中国区之外区域实施1ms粒度，中国区从次年1月；文中示例日志展示新28ms计费时长。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 两个REPORT是同一应用不同调用；不把它们当性能改进的配对实验。
  - 月调用分布和免费额度实际使用未知。
  sources:
  - id: S1
    url: https://aws.amazon.com/blogs/aws/new-for-aws-lambda-1ms-billing-granularity-adds-cost-savings/
    publisher: AWS / Danilo Poccia
    published_at: '2020-12-01'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - url: https://aws.amazon.com/blogs/aws/new-for-aws-lambda-1ms-billing-granularity-adds-cost-savings/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: quantitative_plan fallback 应显式切到 boundary-transfer：按调用收费把哪种费用风险转给客户；不得补负载或发明账单。
    remediation_applied: true
    scope_change: 原2014preview缺可核实际负载；保留数量动作，明确改成2020-12-01官方计费变更及实测REPORT。
quantitative_inputs:
- name: 旧计费粒度
  value: 100
  unit: ms
  source_ids:
  - S1
- name: 新计费粒度
  value: 1
  unit: ms
  source_ids:
  - S1
- name: 官方REPORT执行时长
  value: 27.55
  unit: ms
  source_ids:
  - S1
- name: 配置内存
  value: 1024
  unit: MB
  source_ids:
  - S1
```

## PRO-020

```yaml
id: PRO-020
decision: reframe
scenario_title: Slack 2019版消息搜索与历史额度
focus: causal-modeling
subdomain: retention-workflow
main_question: 新成员寻找旧决策时，可搜索历史的价值在哪个权限与额度边界失效？
expected_output: 一个可核对的判断、来源支持的机制及能推翻它的条件
out_of_scope: 不把公告、相关性或回顾等同已识别的采用/留存因果；不补造指标、条款或任务日志
reason: 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。
admission: eligible
admission_reason: 至少2条事前事实、2条实质证据和直接来源支持的真实交付/观察结局已具备；准入制作并非ready。
research:
  id: PRO-020
  status: sourced
  reason: 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。
  event: Slack 2019版消息搜索与历史额度
  cutoff: 2019-05-13版功能规则已知，新成员执行检索任务前
  initial_facts:
  - id: F1
    text: 2019产品中消息、app帖子与文件文字可搜索，但仅对有权限用户开放。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Free历史搜索只覆盖10000条，付费可搜索更多；不得改用后来的90天规则。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公司说明消息周围上下文可帮助新成员理解旧决策，这是机制主张而非工时测量。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 历史档案随持续使用积累，但额度与访问权限意味着并非所有积累都可被新成员复用。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 2019公开披露中搜索、上下文档案及免费额度已经交付；可以判断复用边界，不能推断真实留存因果。
    source_ids:
    - S1
  interpretation: 来源只确认直接记载的规则、行为和结果；因果链为可检验维护者分析，不以历史结果倒判唯一理性选择。
  unknowns:
  - 完整内部决策与反事实结果未公开；公司主张和当事人回忆需单独标明
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1764925/000162828019006616/slacks-1a1.htm
    publisher: Slack / SEC
    published_at: '2019-05-13'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮重新打开并阅读所列来源正文，按新范围逐条核对；不使用搜索摘要替代。
  phase2_conditions: 不泛论所有团队知识和长期粘性
```

## PRO-021

```yaml
id: PRO-021
decision: retain
scenario_title: PayPal 2001 在线拍卖支付扩散
focus: causal-modeling
subdomain: distribution-growth
main_question: 哪一方的任务使邀请支付工具成为自然步骤？
expected_output: 一条交易到邀请的传播闭环
out_of_scope: 不以后来支付份额代替初期机制证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-021
  status: sourced
  reason: 2002 原始招股书有具体付款/收款流程、未注册收款人路径及拍卖使用比例。
  event: PayPal 2001 在线拍卖支付扩散
  cutoff: 2002-02-11 S-1/A披露后，依据公开支付流程判断渠道依赖；不回填2001事前
  initial_facts:
  - id: F1
    text: 付款人输入收件人邮箱、金额和资金来源。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 商户可用 Web Accept 在自己网页收款；PayPal 与 eBay 无合同关系。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 截至 2001-09 的九个月，客户标识 68.3% 支付额来自网上拍卖，尤其 eBay。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: eBay 有竞争支付产品且可限制 PayPal 展示，是渠道依赖风险。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 拍卖支付占多数，能够展示交易如何产生收付款邀请；不能直接证明某一方邀请的增量效应。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  - 若来源为事后回顾，仅确认其明确记载的当时已知观察或已实施规则；不把后续效果当作事前可知。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1103415/000091205702004798/a2060419zs-1a.htm
    publisher: PayPal / SEC
    published_at: '2002-02-11'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 冻结2002-02-11公开快照；2001支付统计当作已发生的证据，不作未来结果。若原题必须锚定2001则仍需同期材料。
```

## PRO-022

```yaml
id: PRO-022
decision: reframe
scenario_title: HEY 2020：跨平台订阅与App Store首用冲突
focus: constrained-decision
subdomain: strategy-pivot
main_question: 在继续提供统一账务帮助、同时让新下载iOS用户能实际试用的约束下，应优先设计什么最小首用入口？给一个兼顾渠道和服务承诺的方案，并指出不能承诺的审核结果。
expected_output: 一个首用范围方案与两条不可丢失的约束。
out_of_scope: 只看2020年6月冲突；不评判苹果规则合法性、不把媒体争议当需求证明。
reason: 原邮箱定位材料缺冻结历史版本；同一HEY发布事件改为2020-06-19及22日有具体公开工件的渠道/首用决策，保持约束决策动作。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-022
  status: sourced
  reason: 原邮箱定位材料缺冻结历史版本；同一HEY发布事件改为2020-06-19及22日有具体公开工件的渠道/首用决策，保持约束决策动作。
  event: HEY 2020：跨平台订阅与App Store首用冲突
  cutoff: 2020-06-19 公开立场之后、1.0.3方案前；实际提交方案后置
  initial_facts:
  - id: F1
    text: HEY提供Web、Mac、Windows、Linux、Android和iOS多平台服务，并已有统一账务支持体系。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: CEO于6月19日公开强调试用延期、退款和特殊折扣由其团队直接帮助客户的服务承诺；这是公司立场而非独立政策裁决。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公司当时采用iOS仅登录、不提示外部开通入口的方式；苹果方面据6月22日公开信提出下载后不能使用的首用异议。
    source_ids:
    - S2
    availability: post_decision
  - id: E2
    text: 公司要继续更新iOS应用，同时希望保持跨平台一致的付款和帮助渠道；把所有首用障碍交给网页版会留下空白体验。
    source_ids:
    - S1
    - S2
    availability: pre_decision
  outcome:
    id: O1
    text: 6月22日公司提交1.0.3：应用内可申请14天随机临时免费邮箱，同时推进企业付款的HEY for Domains；这是提交方案，不宣称已获批准。
    source_ids:
    - S2
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 未取得苹果全部审核往来与1.0.3最终审核结果；不将CEO单方政策描述当中立法律结论。
  sources:
  - id: S1
    url: https://www.hey.com/apple/iap/
    publisher: HEY / Jason Fried
    published_at: '2020-06-19'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E2
  - id: S2
    url: https://www.hey.com/apple/path/
    publisher: HEY / Jason Fried
    published_at: '2020-06-22'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E1
    - E2
    - O1
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - url: https://www.hey.com/apple/iap/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  - url: https://www.hey.com/apple/path/
    result: 实际打开并阅读6月22日公开信；严格区分1.0.2已发布与1.0.3仅提交审核。
  phase2_conditions:
    original: 不评估整个邮箱市场或把争议当需求证明
    remediation_applied: true
    scope_change: 原邮箱定位材料缺冻结历史版本；同一HEY发布事件改为2020-06-19及22日有具体公开工件的渠道/首用决策，保持约束决策动作。
```

## PRO-023

```yaml
id: PRO-023
decision: reframe
scenario_title: OpenTable 2009 ERB与实时席位确认
focus: causal-modeling
subdomain: network-marketplaces
main_question: 为什么把电话、到店和网上预约放进同一库存，才可能让线上确认可信？
expected_output: 一个可核对的判断、来源支持的机制及能推翻它的条件
out_of_scope: 不把公告、相关性或回顾等同已识别的采用/留存因果；不补造指标、条款或任务日志
reason: 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。
admission: eligible
admission_reason: 至少2条事前事实、2条实质证据和直接来源支持的真实交付/观察结局已具备；准入制作并非ready。
research:
  id: PRO-023
  status: sourced
  reason: 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。
  event: OpenTable 2009 ERB与实时席位确认
  cutoff: 2009-01-30公开的ERB机制快照，判断线上库存可信前
  initial_facts:
  - id: F1
    text: ERB在餐厅前台记录网上、电话和walk-in预约，而不是只保留网上份额的静态清单。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 2009版食客按地点、日期、时间和人数找实时可订桌位，食客端免费。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 餐厅ERB通过互联网实时更新中央网站；库存变化会反映到下一次搜索。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 餐厅购买安装、订阅及就座计费服务，前台管理本身也有价值；不是仅靠流量吸引餐厅。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 2009招股书披露网络已有约10000家餐厅，ERB与线上实时确认形成已实施闭环；不回填1998初版，也不把餐厅数当本地流动性。
    source_ids:
    - S1
  interpretation: 来源只确认直接记载的规则、行为和结果；因果链为可检验维护者分析，不以历史结果倒判唯一理性选择。
  unknowns:
  - 完整内部决策与反事实结果未公开；公司主张和当事人回忆需单独标明
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1125914/000104746909000513/a2190140zs-1.htm
    publisher: OpenTable / SEC
    published_at: '2009-01-30'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮重新打开并阅读所列来源正文，按新范围逐条核对；不使用搜索摘要替代。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-024

```yaml
id: PRO-024
decision: retain
scenario_title: Sentry 2017-12-05 Enterprise SAML SSO
focus: evidence-selection
subdomain: b2b-adoption
main_question: 先验证哪项治理需求，最能说明企业有独立付费理由？
expected_output: 一个验证动作及反证条件
out_of_scope: 不总结六年商业化或照搬 SSO 万能答案
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-024
  status: sourced
  reason: 锁定 2017 Enterprise SAML 发布，直接列出管理员、身份治理和付费边界；实际采购收益未知。
  event: Sentry 2017-12-05 Enterprise SAML SSO
  cutoff: 2017-12-05 公布 Enterprise 身份集成功能时
  initial_facts:
  - id: F1
    text: SAML 2.0 SSO 面向 Sentry Enterprise 组织。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公告说明通过现有身份提供方进行成员管理。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 管理员可统一密码政策、访问记录、入职和撤销权限。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 公告给出配置步骤和 Enterprise 升级入口；不是已观察到的成交证据。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 治理能力被置于 Enterprise 套餐；可选择验证采购必要性的证据，不能宣称已识别真实预算持有人。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://blog.sentry.io/introducing-saml/
    publisher: Sentry / Ryan Goldman
    published_at: '2017-12-05'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 不总结六年商业化或照搬 SSO 万能答案
```

## PRO-025

```yaml
id: PRO-025
decision: reframe
scenario_title: YouTube 2005：零上传之后放宽内容范围能检验什么
focus: hypothesis-diagnosis
subdomain: user-research-value
main_question: 在约会视频版本一周零上传的回忆材料中，“约会用途不吸引人”与“根本没有有效触达”都成立吗？说明放宽视频用途能排除哪一项、仍不能排除哪一项。
expected_output: 两个竞争解释和一次改版的识别边界。
out_of_scope: 只评估首轮改版的诊断力；不使用非约会上传已证明新用途的虚构故事。
reason: 以创始人有明确归属的事后口述重建2005年决策，不宣称找到了同期日志；修正“已有大量非约会上传”的错误触发。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-025
  status: sourced
  reason: 以创始人有明确归属的事后口述重建2005年决策，不宣称找到了同期日志；修正“已有大量非约会上传”的错误触发。
  event: YouTube 2005：零上传之后放宽内容范围能检验什么
  cutoff: 2005年约会版本发布约一周后的转向节点；具体日期仅口述约数
  initial_facts:
  - id: F1
    text: 陈士骏回忆首个版本约2005年5月推出，一周没有视频上传。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 卡里姆描述约会版本随机展示视频并让用户评分，不能自由选择内容。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 零上传只观测到末端行为，没有触达或上传尝试分母，无法唯一定位需求问题。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 创始人回忆取消约会限制后也没有立即大幅增长；这条后验材料用于检验原诊断而非当作转向前已知事实。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    id: O1
    text: 团队改为允许任何类型视频；创始人明确否认改版即刻带来巨大增长。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 未取得2005年同期日志、流量或上传尝试数据；所有历史叙述标为创始人事后回忆。
  sources:
  - id: S1
    url: https://sequoiacap.com/podcast/crucible-moments-youtube
    publisher: Sequoia / Steve Chen、Jawed Karim 口述
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
  - 阅读访谈 From Dating Site to Video Sharing Platform 与后续段落；官方 YouTube 周年文章检索只能确认注册和早期视频。
  - url: https://sequoiacap.com/podcast/crucible-moments-youtube
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 不得使用“非约会上传已证明新用途”故事；需同期原始材料或明确批准修改训练证据口径。
    remediation_applied: true
    scope_change: 以创始人有明确归属的事后口述重建2005年决策，不宣称找到了同期日志；修正“已有大量非约会上传”的错误触发。
```

## PRO-026

```yaml
id: PRO-026
decision: retain
scenario_title: 首代 iPhone 2007 软键盘公布
focus: constrained-decision
subdomain: ux-activation
main_question: 对同时需要浏览网页和发短信的用户，是否以软键盘换取屏幕空间？
expected_output: 一项界面取舍及输入不适用的反例
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-026
  status: sourced
  reason: 2007 原始发布明确软键盘及预测纠错设计，适合比较可变界面与输入学习成本。
  event: 首代 iPhone 2007 软键盘公布
  cutoff: 2007-01-09 公告后、上市前
  initial_facts:
  - id: F1
    text: 多点触控屏以手指控制，输入时显示屏幕键盘。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: SMS 使用 QWERTY 软键盘，而非固定实体键盘。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 官方称键盘有预测、纠错与拼写能力。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 键盘可随任务出现，屏幕兼作浏览和播放器界面。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 软键盘方案被公布；官方易用性承诺不等于输入速度或错误率比较试验。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.apple.com/newsroom/2007/01/09Apple-Reinvents-the-Phone-with-iPhone/
    publisher: Apple
    published_at: '2007-01-09'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-027

```yaml
id: PRO-027
decision: retain
scenario_title: GitHub 2019-01-07 免费私有仓库
focus: prediction-counterfactual
subdomain: pricing-monetization
main_question: 从私有仓库付费转向更开放的免费层，判断开发者平台采用和收入结构。
expected_output: 一个明确判断、可推翻条件及证据边界
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-027
  status: sourced
  reason: 2019 官方公告有明确免费边界与商业计划，足以进行采用/收入结构预测。
  event: GitHub 2019-01-07 免费私有仓库
  cutoff: 2019-01-07 新政策已知、后续采用未知
  initial_facts:
  - id: F1
    text: Free 新增无限私有仓库，每仓库最多三位协作者。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公开仓库仍免费且无限协作者。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: Pro 和 Team 保留专业协作功能。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: Enterprise 合并 Cloud 与 Server 的按席位供给。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 免费私有库政策推出；不得混入 2020 无限协作者或声称增量收入已经证实。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://github.blog/news-insights/product-news/new-year-new-github/
    publisher: GitHub / Nat Friedman
    published_at: '2019-01-07'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-028

```yaml
id: PRO-028
decision: retain
scenario_title: Figma 2021-11-16 评论重做
focus: causal-modeling
subdomain: retention-workflow
main_question: 评论怎样改变这一次设计交接的等待和理解？
expected_output: 一条交接反馈机制
out_of_scope: 不把评论使用直接等同于组织采购或长期留存
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-028
  status: sourced
  reason: 在 2017— 的候选范围锁定 2021 评论重做，官方有用户研究反馈与交接功能的直接描述。
  event: Figma 2021-11-16 评论重做
  cutoff: 2021-11-16 改动已公布、效果未知
  initial_facts:
  - id: F1
    text: 用户研究发现许多协作者难以发现评论，转用其他渠道。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 利益相关人常在一条评论塞多个问题，设计师难逐项回应。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 新版提高 viewer 评论侧栏可见性，并支持圈选区域评论。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 设计师可保持相关评论打开并编辑画布；这是可观察功能，不是已测交付提速。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 新评论功能分批向用户推出；等待时间和理解改善仍需测量。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.figma.com/blog/stay-in-the-flow-with-redesigned-comments/
    publisher: Figma / Ryhan Hassan
    published_at: '2021-11-16'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 不把评论使用直接等同于组织采购或长期留存
```

## PRO-029

```yaml
id: PRO-029
decision: retain
scenario_title: LinkedIn 2003-05 初始邀请及转介绍网络
focus: prediction-counterfactual
subdomain: distribution-growth
main_question: 通过已有联系人转介绍，会怎样改变一次陌生业务联系的可信度与传播阻力？
expected_output: 一项传播预测及身份去重反例
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-029
  status: sourced
  reason: 取得 2003 实际用户讨论及 Reid Hoffman 同期答复，能区分邀请增长与可信关系。
  event: LinkedIn 2003-05 初始邀请及转介绍网络
  cutoff: 2003-05-07 上线初期，用户反馈尚未揭示
  initial_facts:
  - id: F1
    text: LinkedIn 定位专业业务联系，用户通过已有联系人转介绍。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 一名用户描述同一人不同邮箱邀请未合并的身份问题。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 用户报告在短时间收到多份邀请；仅是个案，非网络平均。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: Hoffman 在原讨论解释转发是对具体请求提供联系人信誉。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 同期邀请产生连接和身份摩擦；不能用邀请量替代信任或后续职业价值。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://joi.ito.com/weblog/2003/05/07/linkedin-launch.html
    publisher: Joi Ito；评论包含 Reid Hoffman
    published_at: '2003-05-07'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-030

```yaml
id: PRO-030
decision: reframe
scenario_title: Windows 10 Mobile 2018公告：停止支持的用户迁移取舍
focus: constrained-decision
subdomain: strategy-pivot
main_question: 面向仍依赖Windows 10 Mobile的用户，应该把剩余产品资源优先放在新增功能还是迁移与支持终止说明？用版本和支持范围约束给出一个选择。
expected_output: 一个选择、两个约束及一个仍需保障的用户任务。
out_of_scope: 不推断2017内部退出会议；不讨论整个微软移动战略。
reason: 原2017退出范围缺内部决策材料；改为2018-12-21可核支持终止公告，事件年份显式变更。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-030
  status: sourced
  reason: 原2017退出范围缺内部决策材料；改为2018-12-21可核支持终止公告，事件年份显式变更。
  event: Windows 10 Mobile 2018公告：停止支持的用户迁移取舍
  cutoff: 2018-12-21 对2019终止支持安排的沟通节点
  initial_facts:
  - id: F1
    text: 1709于2017年10月发布，是Windows 10 Mobile最后版本。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公告把2019-12-10定为全部Windows 10 Mobile及Enterprise产品终止支持日。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 终止后不再提供免费安全更新和非安全修补，兼容性继续可用并不等于风险仍受维护。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 免费协助支持和在线技术内容更新也结束，迁移问题同时涉及软件和帮助渠道。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 微软正式公告上述支持结束安排；本题只以公开终止政策为结果，不编造迁移完成率。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 公告不是设备立即停机说明；具体用户依赖、迁移成本与完成率未知。
  sources:
  - id: S1
    url: https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-mobile-end-of-support
    publisher: Microsoft
    published_at: '2018-12-21'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - url: https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-mobile-end-of-support
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 保留既定单一认知动作；结果仅最终揭晓。
    remediation_applied: true
    scope_change: 原2017退出范围缺内部决策材料；改为2018-12-21可核支持终止公告，事件年份显式变更。
```

## PRO-031

```yaml
id: PRO-031
decision: reframe
scenario_title: Tinder 2017：双向同意不等于有效对话
focus: evidence-selection
subdomain: network-marketplaces
main_question: 要验证推荐创造了互相交流的价值，选总右滑数、互相匹配数还是匹配后双方都实际回复的比例作为主要证据？依2017双向同意机制说明分母与盲点。
expected_output: 一个指标选择、清楚分母和不能证明的价值层级。
out_of_scope: 不估2012匹配漏斗；不构造真实cohort或把聊天当长期关系成功。
reason: 执行预设证据选择fallback；改为2017工程负责人可核机制快照，删除缺数据的2012数量推算。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-031
  status: sourced
  reason: 执行预设证据选择fallback；改为2017工程负责人可核机制快照，删除缺数据的2012数量推算。
  event: Tinder 2017：双向同意不等于有效对话
  cutoff: 2017采访所描述产品机制；不回填为2012完整规则
  initial_facts:
  - id: F1
    text: Tinder工程负责人Brian Lee描述产品先推荐附近用户，再由用户滑动表达兴趣。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 双方都右滑才形成match，随后可开始对话。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 单方右滑只是意向；互相match仍仅完成双方同意门槛，不等于实际回复。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: Lee指出共同兴趣本身不够形成深连接，只能帮助开启对话，说明推荐信号与后续互动必须分层。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 2017实际产品把双方同意作为匹配与聊天入口；没有公布本题可用的完整转化漏斗。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 未核得2012原始cohort；具体回复率和关系质量未知，不能计算匹配效率。
  sources:
  - id: S1
    url: https://softwareengineeringdaily.com/wp-content/uploads/2017/10/SED434-Tinder-Management.pdf
    publisher: Software Engineering Daily / Brian Lee（Tinder当事人采访）
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
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - url: https://softwareengineeringdaily.com/wp-content/uploads/2017/10/SED434-Tinder-Management.pdf
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 按计划 fallback 选择行为证据；需补早期 feature 快照，不用合成对话漏斗。
    remediation_applied: true
    scope_change: 执行预设证据选择fallback；改为2017工程负责人可核机制快照，删除缺数据的2012数量推算。
```

## PRO-032

```yaml
id: PRO-032
decision: retain
scenario_title: Dropbox 2007-04-04 HN 公开 demo
focus: evidence-selection
subdomain: user-research-value
main_question: 公开demo后的技术讨论、注册兴趣与实际持续使用，哪一项最能验证待解决的同步任务？
expected_output: 一个优先证据选择并用真实HN异议检验
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-032
  status: sourced
  reason: 2007 原始 HN 反馈加创始人回顾确认 demo 的兴趣信号；明确与后一年 Digg 视频区分。
  event: Dropbox 2007-04-04 HN 公开 demo
  cutoff: 2007-04-04 demo 发布前，讨论和后续反馈隐藏
  initial_facts:
  - id: F1
    text: Houston 以 YC application 项目分享本地文件夹后台同步 demo。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 产品尚未大规模开放，创始人收集潜在使用者兴趣。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: HN 讨论既有热情，也有安装权限、离线边界及信任质疑。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: Houston 在 Mixergy 明确两次视频：5,000 到75,000等候人数属于第二次 Digg 视频。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 首视频获得具体需求反馈；2007 视频不能借用后一年等候人数，更不能等同留存。
    source_ids:
    - S1
    - S2
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  - 若来源为事后回顾，仅确认其明确记载的当时已知观察或已实施规则；不把后续效果当作事前可知。
  sources:
  - id: S1
    url: https://news.ycombinator.com/item?id=8863
    publisher: Hacker News / dhouston
    published_at: '2007-04-04'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - outcome
  - id: S2
    url: https://mixergy.com/interviews/drew-houston-dropbox-interview/
    publisher: Mixergy / Drew Houston
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-033

```yaml
id: PRO-033
decision: reframe
scenario_title: Snowflake 2023成本界面：总消费增长的诊断分叉
focus: hypothesis-diagnosis
subdomain: b2b-adoption
main_question: 预算预警显示可能超支时，怎样用总credits、每100个jobs的credits和昂贵查询列表区分“工作量增加”与“单位工作消耗增加”？给一个先后诊断顺序及其不能识别的边界。
expected_output: 一条有判别方向的诊断链；明确任务组合改变的混淆。
out_of_scope: 只分析2023发布界面已有指标的诊断力；不虚构真实客户涨价或浪费事件，不使用尚未推出的Cost Insights。
reason: 原2014–2019客户预算事件没有独立材料；明确改为2023-11-02私测产品工件，训练成本告警可否支持因果诊断，删除不存在的历史cohort要求。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-033
  status: sourced
  reason: 原2014–2019客户预算事件没有独立材料；明确改为2023-11-02私测产品工件，训练成本告警可否支持因果诊断，删除不存在的历史cohort要求。
  event: Snowflake 2023成本界面：总消费增长的诊断分叉
  cutoff: 2023-11-02 私测界面方案快照
  initial_facts:
  - id: F1
    text: 管理员面对按账户、仓库和查询归属的Snowflake消费，单一总额不能说明消耗来自何种工作。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公开成本界面展示总美元/credits、日均消费、最贵仓库与查询，以及credits per 100 jobs趋势。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 每100个jobs的单位指标使任务量与单位消耗可以分开初查；但不同jobs的任务组合并未被这个分母自动控制。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 预算页面把截至当日实际累计消费与余月预测分开；预警基于设定预算和趋势，不是已确认浪费的诊断结论。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: Snowflake发布Cost Management Interface私测与AWS Budgets公测；Cost Insights仍是即将私测的预告，不能写成已可用自动诊断。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 来源是界面机制与发布范围，不是某客户实际超支资料。
  - 任务复杂度、任务组合和业务价值仍未知；单位credits也不能直接等同价值。
  sources:
  - id: S1
    url: https://www.snowflake.com/en/blog/optimize-spend-new-cost-management-interface/
    publisher: Snowflake / Samartha Chandrashekar、Shruti Anand、PD Dutta
    published_at: '2023-11-02'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索 Snowflake S-1 和消费模型；打开 SEC 原文件返回超4MB；后来的投资者演示不能替代早期客户路径。
  - url: https://www.snowflake.com/en/blog/optimize-spend-new-cost-management-interface/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 需真实客户同口径用量和预算证据；不凭公司收入上升归因。
    remediation_applied: true
    scope_change: 原2014–2019客户预算事件没有独立材料；明确改为2023-11-02私测产品工件，训练成本告警可否支持因果诊断，删除不存在的历史cohort要求。
```

## PRO-034

```yaml
id: PRO-034
decision: reframe
scenario_title: Spotify 2010：快速起播不能只归因P2P
focus: causal-modeling
subdomain: ux-activation
main_question: 按2010公开机制，把随机选曲和顺序播放的起播路径分别画出；为什么全体265ms中位起播延迟不能全归因于P2P？
expected_output: 两条短因果链与一个归因限制。
out_of_scope: 只看首次播放体验路径；不推出留存或付费提升，不将2010机制回填2008首版。
reason: 原2008首用判断缺同期机制细节；冻结2010作者论文中明确测量口径和缓存/预取/服务器/P2P路径。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-034
  status: sourced
  reason: 原2008首用判断缺同期机制细节；冻结2010作者论文中明确测量口径和缓存/预取/服务器/P2P路径。
  event: Spotify 2010：快速起播不能只归因P2P
  cutoff: 2010论文机制快照；总体性能结果在最后揭晓
  initial_facts:
  - id: F1
    text: 服务允许按需搜索选择曲目，也允许按列表顺序连续播放。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 2010论文明确限定桌面客户端；手机不参与P2P，不能混为同一架构。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 随机未缓存曲目先通过已连接服务器请求约15秒音频，同时寻找P2P来源；首段启动不必等待P2P完成。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 顺序曲目可提前预取；本地缓存也避免重取，论文265ms总体中位数包含缓存曲目，因此多条机制同时影响统计。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 论文实测总体中位起播延迟265ms（含缓存）；这支持当时系统低延迟观察，不是P2P独立贡献或用户留存实验。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 不同路径的独立因果贡献与留存效果未提供；总体中位数也不是首次新用户起播中位数。
  sources:
  - id: S1
    url: https://kreitz.se/spotify-p2p10/spotify-p2p10.pdf
    publisher: Gunnar Kreitz、Fredrik Niemelä / IEEE P2P 2010
    published_at: '2010'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - url: https://kreitz.se/spotify-p2p10/spotify-p2p10.pdf
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 保留既定单一认知动作；结果仅最终揭晓。
    remediation_applied: true
    scope_change: 原2008首用判断缺同期机制细节；冻结2010作者论文中明确测量口径和缓存/预取/服务器/P2P路径。
```

## PRO-035

```yaml
id: PRO-035
decision: reframe
scenario_title: Dropbox Pro 2014：容量与共享控制的付费触发
focus: prediction-counterfactual
subdomain: pricing-monetization
main_question: 若只把Pro容量增加到1TB而不提供共享权限控制，哪些原来因共享风险而考虑升级的任务仍无法满足？预测一类升级动机并给出可推翻它的观察。
expected_output: 一个有条件的反事实预测及其反例。
out_of_scope: 只看2014 Pro改版；不混入2008发布、推荐奖励或后来团队套餐。
reason: 2008免费额度与升级队列不足；改为2014-08-27具体Pro发布政策，对同一付费触发问题做有限反事实。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-035
  status: sourced
  reason: 2008免费额度与升级队列不足；改为2014-08-27具体Pro发布政策，对同一付费触发问题做有限反事实。
  event: Dropbox Pro 2014：容量与共享控制的付费触发
  cutoff: 2014-08-27 Pro改版方案评审
  initial_facts:
  - id: F1
    text: 既有Pro用户已经使用Dropbox保存与分享文件；公司称用户要求更强共享保护。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 改版保持每月9.99美元，计划合并为1TB单一Pro方案。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 新方案提供共享链接密码和到期时间；它们解决访问边界而非存储容量。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 共享文件夹只读权限控制编辑风险，远程擦除用于丢失设备；这些任务不会因容量增加自动完成。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: Dropbox宣布容量与控制功能一同升级，既有Pro用户自动更新；没有公布拆分各功能的升级转化贡献。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 缺少各功能独立实验和升级用户动机分布；预测允许被观察否定。
  sources:
  - id: S1
    url: https://blog.dropbox.com/topics/product/introducing-more-powerful-dropbox-pro
    publisher: Dropbox / Chenli Wang
    published_at: '2014-08-27'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - url: https://blog.dropbox.com/topics/product/introducing-more-powerful-dropbox-pro
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 不混入推荐奖励或后续团队套餐
    remediation_applied: true
    scope_change: 2008免费额度与升级队列不足；改为2014-08-27具体Pro发布政策，对同一付费触发问题做有限反事实。
```

## PRO-036

```yaml
id: PRO-036
decision: retain
scenario_title: Discover Weekly 2015-07 推出
focus: hypothesis-diagnosis
subdomain: retention-workflow
main_question: 累计播放很多，能区分新鲜感、已有重度用户与新增留存吗？
expected_output: 两个解释及以私人可取消歌单规则为约束的检验
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-036
  status: sourced
  reason: 同期 Spotify staff 帖确认规则与资格，后续官方使用总量支持功能持续使用；因果留存未知。
  event: Discover Weekly 2015-07 推出
  cutoff: 2015-07-21 功能介绍已知、后续使用结果未知
  initial_facts:
  - id: F1
    text: 自动加入30首歌歌单，每周一更新。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 根据个人和类似口味用户历史；需注册两周并在最近30天活跃。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: staff 说明默认私人、可取消关注。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 2020 官方称2015-07至2020-06-25累计播放超过23亿小时；不等于新增留存。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 功能推出且长期有播放；固定周期与算法命中对回访的独立作用尚未识别。
    source_ids:
    - S1
    - S2
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://community.spotify.com/forum/en/discussion/1174410/discover-weekly-post-your-feedback-here
    publisher: Spotify / staff Rorey
    published_at: '2015-07-21'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - outcome
  - id: S2
    url: https://newsroom.spotify.com/2020-07-09/spotify-users-have-spent-over-2-3-billion-hours-streaming-discover-weekly-playlists-since-2015/
    publisher: Spotify
    published_at: '2020-07-09'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-037

```yaml
id: PRO-037
decision: reframe
scenario_title: Hotmail 1996邮件页脚传播：机会分母如何去重
focus: evidence-selection
subdomain: distribution-growth
main_question: 若把每封带Hotmail推广页脚的外发邮件都算一次独立拉新机会，会在哪个分母上失真？在发送量、去重未注册收件人数和新注册人数中组织一个可解释的传播口径。
expected_output: 一条发送→触达→注册链，选择关键分母并解释重复与既有用户。
out_of_scope: 不计算没有公开输入的传播系数，不将总体增长归因全部给页脚。
reason: 采用预设证据选择fallback。来源为投资董事Jurvetson事后重刊的1997/1998版本叙述，不能混作1996同期观测；只保留明示机制与作者观察。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-037
  status: sourced
  reason: 采用预设证据选择fallback。来源为投资董事Jurvetson事后重刊的1997/1998版本叙述，不能混作1996同期观测；只保留明示机制与作者观察。
  event: Hotmail 1996邮件页脚传播：机会分母如何去重
  cutoff: 1996页脚机制决策的事后重建；准确日期和同期漏斗未获得
  initial_facts:
  - id: F1
    text: Hotmail提供免费的Web邮箱，收件人可通过网页采用服务。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 投资董事回忆推广页脚加入私人外发邮件曾有争议，团队通过明确分隔并删去P.S.缓和。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 每封外发邮件都携带推广，但作者描述收件人通常是朋友同事，存在地区和关系簇，并非互不重叠的随机受众。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 作者把发送者自身使用服务称为隐含背书；这解释为什么应区分触达和信任后的注册，而不是把发送次数直接当新增人数。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 团队实际采用分隔的推广页脚；后来用户增长是董事回忆的整体观察，不是页脚独立实验。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 重刊混合原1997与1998文章版本，数字适用时点有差异；本题不使用增长数字。
  - 去重收件人、既有注册状态及转化率未公开。
  sources:
  - id: S1
    url: https://www.flickr.com/photos/jurvetson/10446705354
    publisher: Steve Jurvetson / Flickr本人重刊
    published_at: '2013-10-23'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - url: https://www.flickr.com/photos/jurvetson/10446705354
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: fallback evidence-selection：缺哪个漏斗分母会令传播系数失去意义；精确系数不可计算。
    remediation_applied: true
    scope_change: 采用预设证据选择fallback。来源为投资董事Jurvetson事后重刊的1997/1998版本叙述，不能混作1996同期观测；只保留明示机制与作者观察。
```

## PRO-038

```yaml
id: PRO-038
decision: retain
scenario_title: Instagram 从 Burbn 缩减功能（2010）
focus: hypothesis-diagnosis
subdomain: user-research-value
main_question: 用户最喜欢照片能支持缩减Burbn，还是已证明删功能本身必然带来增长？
expected_output: 两个可区分的价值假说及未识别因素
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-038
  status: sourced
  reason: 已实际读到官方完整转录；创始人回顾明确Burbn最受喜爱的是图片分享并聚焦照片问题。回顾不是2010原始日志或因果实验。
  event: Instagram 从 Burbn 缩减功能（2010）
  cutoff: 2010 Burbn已有使用观察、聚焦Instagram前；确切日未核实
  initial_facts:
  - id: F1
    text: Burbn是签到应用，同时可以分享图片和视频；创始人在2011回述原版。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 创始人称团队观察到用户最喜欢分享图片；该观察在聚焦决定之前，未公开样本与日志。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 团队聚焦照片不好看、上传慢、多服务分享三个问题，并围绕它们构建Instagram。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 演讲说明提早在写caption前上传及缩小照片以降低等待；不是删除功能单独效果。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: Burbn转为以照片为中心的Instagram；创始人报告发布后用户增长，不能证明精简单独造成增长。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://stvp.stanford.edu/node/12536/printable/print
    publisher: Stanford STVP
    published_at: '2011-05-11'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 早期PDF403；随后通过官方视频页Read Transcript成功打开并实际阅读完整转录的Burbn及问题聚焦段落。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-039

```yaml
id: PRO-039
decision: retain
scenario_title: Teams 2017-03-14 面向 Office365 商业客户 GA
focus: boundary-transfer
subdomain: strategy-pivot
main_question: Office365渠道可直接迁移为Teams采用的条件是什么？
expected_output: 一项渠道迁移边界，区分试用组织与持续使用
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-039
  status: sourced
  reason: 2017 GA 公告直接确认 Office365 分发条件与实际试用组织，足够进行渠道与产品竞争假说分析。
  event: Teams 2017-03-14 面向 Office365 商业客户 GA
  cutoff: 2017-03-14 公布方案、后续竞争结果未知
  initial_facts:
  - id: F1
    text: Teams 作为 Office365 聊天协作空间进入181市场19语言。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 结合既有 Office 文档、笔记、任务与会话。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: Microsoft 自报从2016-11 preview已有5万多组织使用。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 公告给客户案例引语，但无随机对比 Slack 的任务成效。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 随 Office365 向商业客户发布；不能由采用组织数证明产品胜过 Slack。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://news.microsoft.com/source/2017/03/14/microsoft-teams-rolls-out-to-office-365-customers-worldwide/
    publisher: Microsoft
    published_at: '2017-03-14'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-040

```yaml
id: PRO-040
decision: reframe
scenario_title: DoorDash 2013：创始人配送阶段是否扩大覆盖
focus: constrained-decision
subdomain: network-marketplaces
main_question: 当配送人员只有创始人、调度依赖Google Voice与Find My Friends时，下一步应优先增加可接单地区还是先验证现有地区履约链？依据实际资源作一个范围选择并说明代价。
expected_output: 一个扩张范围选择及两条履约约束。
out_of_scope: 不计算每单利润或等待时长；不编订单表、路线距离或2013服务承诺。
reason: 执行预设constrained-decision fallback；用CEO公开回顾里的真实早期运作约束替代缺失数量输入。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-040
  status: sourced
  reason: 执行预设constrained-decision fallback；用CEO公开回顾里的真实早期运作约束替代缺失数量输入。
  event: DoorDash 2013：创始人配送阶段是否扩大覆盖
  cutoff: 2013年6月正式DoorDash推出前阶段；以2017 CEO回忆重建
  initial_facts:
  - id: F1
    text: 正式命名前称Palo Alto Delivery，唯一配送员是几位联合创始人。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: CEO回忆初期依赖Google Voice、Find My Friends与自己的汽车，没有成熟物流组织。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 宣传主要在宿舍公告板贴传单，获客触达与创始人配送半径绑在本地。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 完成履约要协调订单、餐厅与在路上的有限人手；2017回顾把配送速度与选择范围列为最后一公里取舍，不能由其后规模倒推初期已解决。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    id: O1
    text: 公司2013年6月正式推出DoorDash，并从创始人配送发展为更大平台；本题不使用2017规模作事前约束或证明最优。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 没有可核2013订单、成本、等待分布和精确半径；只做资源约束下范围选择。
  sources:
  - id: S1
    url: https://about.doordash.com/en-ca/news/four-years-in-and-just-getting-started
    publisher: DoorDash / Tony Xu
    published_at: '2017-06-22'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索 Stanley Tang 2013-11-28 原文；带斜杠和不带斜杠 URL 均500；YC公司页仅当下总览，不足以支持早期密度。
  - url: https://about.doordash.com/en-ca/news/four-years-in-and-just-getting-started
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 不可补订单或成本；fallback constrained-decision 需先取得可核早期路线和等待约束。
    remediation_applied: true
    scope_change: 执行预设constrained-decision fallback；用CEO公开回顾里的真实早期运作约束替代缺失数量输入。
```

## PRO-041

```yaml
id: PRO-041
decision: reframe
scenario_title: Grammarly 2019：词上即时同义词与首次价值路径
focus: causal-modeling
subdomain: ux-activation
main_question: 把2019手机键盘的“写完一个词后暂停即可看到同义词”与手动另开编辑器比较，画出它缩短首次获得有用措辞建议的路径；哪个环节仍需用户实际评价才能称为价值？
expected_output: 一条用户动作因果链及一个未被自动完成的价值判断。
out_of_scope: 不补2015浏览器首用转化数据，不概括全部写作功能，不默认建议一定更好。
reason: 原2015扩展首次价值证据不足；改用2019-11-28官方明确发布的手机键盘交互快照，保留首次价值因果动作。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-041
  status: sourced
  reason: 原2015扩展首次价值证据不足；改用2019-11-28官方明确发布的手机键盘交互快照，保留首次价值因果动作。
  event: Grammarly 2019：词上即时同义词与首次价值路径
  cutoff: 2019手机同义词交互发布快照
  initial_facts:
  - id: F1
    text: 用户在手机上快速写作，不能由输入速度直接判断表达是否合适。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 2019官方回顾明确Grammarly Keyboard推出同义词建议。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 写完一个词暂停即可出现建议，不需将全文复制到另一编辑器；之前输入的词也可通过移动光标触发。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 同义词反馈直接绑定当前词，减少发现建议的操作，但词是否适合上下文仍需写作者判断；发布说明没有给实际接受率。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 官方发布的键盘交互已支持上述词上建议；没有公布本题可用的首次有用建议时间或转化改善实验。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 首用耗时、建议采纳与文本质量的因果效果未知；另开编辑器仅是明确的流程反事实，不冒充历史实验。
  sources:
  - id: S1
    url: https://www.grammarly.com/blog/product/new-features-2019/
    publisher: Grammarly / Brittney Ross
    published_at: '2019-11-28'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - url: https://www.grammarly.com/blog/product/new-features-2019/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 不总结全部写作产品或预设反馈必然有用
    remediation_applied: true
    scope_change: 原2015扩展首次价值证据不足；改用2019-11-28官方明确发布的手机键盘交互快照，保留首次价值因果动作。
```

## PRO-042

```yaml
id: PRO-042
decision: retain
scenario_title: Unity Runtime Fee 2023修订至2024撤销
focus: evidence-selection
subdomain: pricing-monetization
main_question: 哪些证据说明收费规则可被理解，哪些才说明开发者愿意继续投入？
expected_output: 一个信任验证选择及能推翻的结果
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-042
  status: sourced
  reason: 2023修订信与2024取消公告完整确认收费政策变动；明确没有真实收费账单。
  event: Unity Runtime Fee 2023修订至2024撤销
  cutoff: 2023-09-22 修订政策已公布，2024取消隐藏
  initial_facts:
  - id: F1
    text: 2023修订不向 Personal 收 runtime fee，Pro/Enterprise 仅新LTS起符合条件项目适用。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 符合条件者按2.5%收入分成与每月新增engagement计算额二者较低计费，均自报。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: Marc Whitten承认宣布前未充分征求反馈并要求重建信任。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 2024-09-12官方取消游戏 runtime fee，即刻生效。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 2024取消，后续官方FAQ明确该费未实施；不得编造被收费或撤费导致回流的用户数。
    source_ids:
    - S2
    - S3
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://unity.com/blog/an-open-letter-to-our-community
    publisher: Unity / Marc Whitten
    published_at: '2023-09-22'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
  - id: S2
    url: https://unity.com/blog/unity-is-canceling-the-runtime-fee
    publisher: Unity / Matt Bromberg
    published_at: '2024-09-12'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
    - outcome
  - id: S3
    url: https://unity.com/products/pricing-updates
    publisher: Unity
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-043

```yaml
id: PRO-043
decision: reframe
scenario_title: Atlassian 2015：自助销售把评估责任移到哪里
focus: boundary-transfer
subdomain: b2b-adoption
main_question: 2015公开自助试用和在线购买模式把哪些评估工作转给客户，又有哪些工作仍由Atlassian与Experts承担？判断“无传统直销”等不等于“无人帮助”。
expected_output: 一张客户/产品文档/支持/渠道四方责任边界表。
out_of_scope: 不估销售成本，不回填2000年代具体Jira套餐，不把在线交易份额当纯自动化直销份额。
reason: 原2000年代时间范围过宽；实际下载并提取2015-11-09 F-1，冻结当时自助评估与支持边界。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-043
  status: sourced
  reason: 原2000年代时间范围过宽；实际下载并提取2015-11-09 F-1，冻结当时自助评估与支持边界。
  event: Atlassian 2015：自助销售把评估责任移到哪里
  cutoff: 2015-11-09 F-1公开销售模式快照
  initial_facts:
  - id: F1
    text: 招股书披露公开产品价格、文档与知识库，提供免费且功能完整的试用。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司当时不雇用传统佣金制直接销售队伍，购买主要走网页自动流程并支持信用卡或转账。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 免费试用仍包括完整技术和销售支持，客户服务团队继续协助并发现可自动化环节；自助不等于取消服务。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: Atlassian Experts提供部署、定制、本地货币语言和合规采购帮助；客户承担初步评估不代表组织采购与实施全能自助完成。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: F-1报告超过98%交易经网站，但间接渠道约占2015财年收入25%；两种不同分母同时存在，不能把网站交易误读成没有渠道服务。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 招股书是公司披露，不是边界转移独立因果评估；具体销售成本、客服满意度和客户实施费用未知。
  sources:
  - id: S1
    url: https://d1lge852tjjqow.cloudfront.net/CIK-0001650372/5a3f92c2-b552-414e-9c41-2b1a17e01f07.pdf
    publisher: Atlassian / 2015 F-1
    published_at: '2015-11-09'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索 Atlassian 2015 F-1；尝试读取 SEC filename1.htm 返回超4MB；未把搜索摘要的97%网站成交当同期2000s情境。
  - url: https://d1lge852tjjqow.cloudfront.net/CIK-0001650372/5a3f92c2-b552-414e-9c41-2b1a17e01f07.pdf
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  - url: https://d1lge852tjjqow.cloudfront.net/CIK-0001650372/5a3f92c2-b552-414e-9c41-2b1a17e01f07.pdf
    result: 实际下载公开PDF并用PDFKit提取第7、27、64、112、125页；第125页核读完整试用支持、在线购买与Experts条目。
  phase2_conditions:
    original: 不估无来源销售成本或评价全部销售策略
    remediation_applied: true
    scope_change: 原2000年代时间范围过宽；实际下载并提取2015-11-09 F-1，冻结当时自助评估与支持边界。
```

## PRO-044

```yaml
id: PRO-044
decision: reframe
scenario_title: Duolingo 排行榜规则快照：名次下降能诊断学习退步吗
focus: hypothesis-diagnosis
subdomain: retention-workflow
main_question: 按公开每周重组、跨课程竞争规则，名次下降应怎样区分“本人的学习变化”与“比较组变化”？说明仅凭排行榜不能确认的一个学习结论。
expected_output: 两个竞争解释、一个判别顺序和不能推出的结论。
out_of_scope: 只推演公开规则，不合成真实学员日志，不把2018首测和后来完整联赛规则混为同一版本。
reason: 2018仅能核实测试年份，缺同期队列；正式改为2026-10-25可读公开规则快照，保留假设诊断并移除虚构实验。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-044
  status: sourced
  reason: 2018仅能核实测试年份，缺同期队列；正式改为2026-10-25可读公开规则快照，保留假设诊断并移除虚构实验。
  event: Duolingo 排行榜规则快照：名次下降能诊断学习退步吗
  cutoff: 2026-10-25公开规则快照；页面原始发布日期未能确定
  initial_facts:
  - id: F1
    text: 每周按当地时区周日开始新联赛，是相对同组学习者的周期排名。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 官方说明每周匹配相似学习习惯和近似时区的人；同组可来自不同课程和语言。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 组内相对位置同时取决于本人及其他人的活动，跨周比较又更换对手；仅名次变动无法唯一定位本人水平变化。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 官方提供退出排行榜的设置，并把它定位为激励参与的竞争功能；这不是独立语言能力测验。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 公开产品实际提供上述分组、每周竞争与退出机制；公司称2018测试竞争能激励许多学习者，但未提供本题可用的学习能力因果实验。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 页面后续更新史未知，不把当前10级联赛规则回填2018。
  - 未提供同口径能力评测、实验队列和个体学习变化；本题为规则推演，不冒充历史学员观察。
  sources:
  - id: S1
    url: https://blog.duolingo.com/duolingo-leagues-leaderboards/
    publisher: Duolingo
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
  - 阅读官方 leagues 说明全文；对照用户讨论但未以讨论作为发布日期依据。
  - url: https://blog.duolingo.com/duolingo-leagues-leaderboards/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 2018 是测试年；不可把后续完整规则或 XP 当学习能力。
    remediation_applied: true
    scope_change: 2018仅能核实测试年份，缺同期队列；正式改为2026-10-25可读公开规则快照，保留假设诊断并移除虚构实验。
```

## PRO-045

```yaml
id: PRO-045
decision: reframe
scenario_title: Pinterest 2020 Story Pins：曝光还是被尝试的想法
focus: evidence-selection
subdomain: distribution-growth
main_question: Story Pins希望让创作者的想法可操作；在曝光量、保存量和尝试后附图/文字反馈之间选一个最贴近“内容帮助用户做成事情”的主要证据，并指出其选择偏差。
expected_output: 一个主要证据选择、一个补充口径与偏差。
out_of_scope: 不以邀请码、排队长度或曝光直接证明PMF；不评价整个短视频市场。
reason: 原2010候补名单缺可核原始材料；明确换为同品牌2020-09-23 Story Pins发布，有实际内容交互和度量入口，不与2015 Save案例混用。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-045
  status: sourced
  reason: 原2010候补名单缺可核原始材料；明确换为同品牌2020-09-23 Story Pins发布，有实际内容交互和度量入口，不与2015 Save案例混用。
  event: Pinterest 2020 Story Pins：曝光还是被尝试的想法
  cutoff: 2020-09-23 Story Pins beta设计与发布快照
  initial_facts:
  - id: F1
    text: Pinterest服务帮助人发现食谱、DIY等可付诸行动的想法，Story Pins支持视频、旁白、图文。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 创作者可在应用内发布，无需另建网站，也可增加原料或材料详情页。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 内容可保存到看板并持续被发现，不在24小时后消失；保存显示未来意向但不保证已经实践。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 发布说明提供尝试后附图和文字反馈，也提供Pin Stats曝光与互动；前者更接近实际行动，但只覆盖愿意反馈的人。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 2020-09-23在美国精选创作者中推出Story Pins beta，美国iOS/Android/Web开始可见；并非全球创作者全面开放。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 来源是发布机制，未给真实cohort效果；反馈具有自选偏差且可能不代表全部实际尝试。
  sources:
  - id: S1
    url: https://newsroom-archive.pinterest.com/en-gb/introducing-story-pins-and-new-ways-for-creators-to-build-and-grow-with-pinterest
    publisher: Pinterest
    published_at: '2020-09-23'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索 Pinterest 官方archive/2012开放注册及早期创始人资料；结果以二手报道为主，未取得可读同期邀请规则和回访队列。
  - url: https://newsroom-archive.pinterest.com/en-gb/introducing-story-pins-and-new-ways-for-creators-to-build-and-grow-with-pinterest
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 不以邀请数和排队长度直接证明 PMF
    remediation_applied: true
    scope_change: 原2010候补名单缺可核原始材料；明确换为同品牌2020-09-23 Story Pins发布，有实际内容交互和度量入口，不与2015 Save案例混用。
```

## PRO-046

```yaml
id: PRO-046
decision: retain
scenario_title: Airbnb 2009 纽约房源摄影
focus: hypothesis-diagnosis
subdomain: user-research-value
main_question: 摄影后收入提高，可否判定照片是唯一瓶颈？
expected_output: 两个竞争解释及在非随机前后比较下的更新
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-046
  status: sourced
  reason: Joe Gebbia访谈与早期导师回顾直接支持纽约改善房源照片；前后收入不能独立证明照片因果。
  event: Airbnb 2009 纽约房源摄影
  cutoff: 2009年纽约房源浏览、实地摄影前，确切日未核
  initial_facts:
  - id: F1
    text: Gebbia回顾纽约房源照片质量很差，难理解实际房间。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 创始人决定亲自去纽约拍摄而非先扩规模。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 访谈报告摄影后周收入由约200到400美元，属非随机前后比较。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: Paul Graham回顾创始人在纽约拜访用户并改善房源。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 实地摄影与收入改善在当事人回顾中出现；获客、服务和照片同时改变，不能独立归因。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  - 若来源为事后回顾，仅确认其明确记载的当时已知观察或已实施规则；不把后续效果当作事前可知。
  sources:
  - id: S1
    url: https://review.firstround.com/how-design-thinking-transformed-airbnb-from-failing-startup-to-billion-dollar-business/
    publisher: First Round Review / Joe Gebbia访谈
    published_at: '2015-02-03'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - outcome
  - id: S2
    url: https://paulgraham.com/ds.html
    publisher: Paul Graham
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-047

```yaml
id: PRO-047
decision: retain
scenario_title: Netflix 2007-01-16 即时观看PC功能
focus: constrained-decision
subdomain: strategy-pivot
main_question: 是否把片库小、仅PC的即时观看作为DVD会员附加功能先推出？
expected_output: 一项渐进发布选择及技术/内容边界
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-047
  status: sourced
  reason: 2007原始公告给出渐进流媒体策略、内容与技术限制，能判断蚕食与分发的取舍。
  event: Netflix 2007-01-16 即时观看PC功能
  cutoff: 2007-01-16 公告已知、上线后采用未知
  initial_facts:
  - id: F1
    text: DVD会员保留邮寄服务，新即时观看无需另加月费。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 首批约1000部/剧集，对比邮寄库超过70000标题，六个月分批开放。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告说明PC浏览器安装小程序后流式观看，避免完整下载等待。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: Hastings把内容与技术限制视为大众采用需数年的原因，属预期。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 流媒体作为DVD订阅附加功能推出；不是2007立即退出DVD。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://about.netflix.com/en/news/netflix-offers-subscribers-the-option-of-instantly-watching-movies-on-their
    publisher: Netflix
    published_at: '2007-01-16'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-048

```yaml
id: PRO-048
decision: retain
scenario_title: Steam Workshop 2011-10-13 TF2提交中心上线
focus: causal-modeling
subdomain: network-marketplaces
main_question: 这个回报机制会怎样影响创作者持续供给？
expected_output: 一条贡献到回报的机制及反向激励
out_of_scope: 不混同 Workshop 与独立有偿市场
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-048
  status: sourced
  reason: 2011原始Valve公告明确提交/反馈机制与既有创作者收益，足以预测供给激励，避免前后因果错置。
  event: Steam Workshop 2011-10-13 TF2提交中心上线
  cutoff: 2011-10-13 新中心已说明、长期供给未知
  initial_facts:
  - id: F1
    text: 中心允许上传、看状态和接收Valve反馈。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 社区可在同处查看、评论、给提交物评分。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告称此前一年Mann Co.Store创作者收益超过200万美元。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 这个金额发生在Workshop上线前，不能作为它带来收益的效果。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: Workshop上线，社区反馈与选择入口改善；未验证创作者长期持续供给率。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.teamfortress.com/post.php?id=6508
    publisher: Valve / TF2 Team
    published_at: '2011-10-13'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 不混同 Workshop 与独立有偿市场
```

## PRO-049

```yaml
id: PRO-049
decision: reframe
scenario_title: Superhuman人工入门：产能ARR模型与利润的边界
focus: quantitative-calibration
subdomain: ux-activation
main_question: 依作者公开模型，每周40次完成入门、每年45周、每位客户每月30美元，单专员可新增多少年化订阅额？为什么这不能直接称为当年利润或人工入门的因果回报？
expected_output: 一次648000美元ARR计算、明确模型前提及两项不能推断的结论。
out_of_scope: 只复算作者公开产能模型；不编造cohort、流失率或实际获客利润。
reason: 保留数量动作但收窄为可核公开模型；40次×45周×月费是产能情景，不冒充历史实际净收入。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-049
  status: sourced
  reason: 保留数量动作但收窄为可核公开模型；40次×45周×月费是产能情景，不冒充历史实际净收入。
  event: Superhuman人工入门：产能ARR模型与利润的边界
  cutoff: 作者回顾中的入门产能模型评估；原文未给模型适用的精确日历年
  initial_facts:
  - id: F1
    text: 作者Gaurav Vohra是创建并领导Superhuman人工入门团队的当事人；单次入门后缩短为30分钟。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 其公开模型目标为扣除爽约后每周40次完成通话、每年45周，月费30美元。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 这些值是有足够需求下的人员产能与定价假设；年化新增订阅额为40×45×30×12。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 作者承认人工入门与自助的激活比较存在选择偏差；参加30分钟通话者本来就是自助人群的子集。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 作者给出的模型结果约65万美元新增ARR/专员/年；不能由此推出实际利润或独立因果激活提升。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 模型不是核验过的实际财报；流失、付款时点、可归因激活增量和净利未知。
  sources:
  - id: S1
    url: https://review.firstround.com/superhuman-onboarding-playbook/
    publisher: First Round Review / Gaurav Vohra（当事人撰文）
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
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - url: https://review.firstround.com/superhuman-onboarding-playbook/
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 量化所需同期成本、收入和因果激活不足；建议采用预设的evidence-selection备用问题（尚未改变focus），不把文章产能×月费的模型当实际利润。
    remediation_applied: true
    scope_change: 保留数量动作但收窄为可核公开模型；40次×45周×月费是产能情景，不冒充历史实际净收入。
quantitative_inputs:
- name: 已完成入门目标
  value: 40
  unit: 次/周
  source_ids:
  - S1
- name: 工作周模型
  value: 45
  unit: 周/年
  source_ids:
  - S1
- name: 订阅标价
  value: 30
  unit: 美元/月
  source_ids:
  - S1
```

## PRO-050

```yaml
id: PRO-050
decision: reframe
scenario_title: Zoom 2020教育豁免：免费时限与管理需求
focus: constrained-decision
subdomain: pricing-monetization
main_question: 学校仅因课堂超过40分钟而考虑付费时，应先申请Basic教育豁免还是购买Education，哪项管理需求会改变选择？
expected_output: 一个带身份验证和管理需求边界的套餐选择
out_of_scope: 不编造内部实验、未公开用户数或历史版本，不将发布方解释当独立测量。
reason: 改用官方2020记录明确的40分钟豁免与Education差异，取消未核2019完整套餐。
admission: eligible
admission_reason: 单一产品节点、两项背景与两项证据及直接支持的交付/观察结果已核对；准入不等于ready。
research:
  id: PRO-050
  status: sourced
  reason: 改用官方2020记录明确的40分钟豁免与Education差异，取消未核2019完整套餐。
  event: Zoom 2020教育豁免：免费时限与管理需求
  cutoff: 使用官方页2020年3月日期段落中的教育豁免及套餐对比；不把2021/2022后续结束安排放入起始信息。
  initial_facts:
  - id: F1
    text: 2020年3月学校关闭推动线上课堂需求，Zoom公告临时取消部分K-12免费Basic账户40分钟时限。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 申请路径要求学校提交请求并验证学校邮箱域名；不意味着任意个人账户均获豁免。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 验证后学校域名下Basic账户可获时限豁免，学生可通过教师发出的链接参加。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 同页Education方案另列SSO、LTI及增强用户管理；只取消时限不提供所有这些管理能力。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: Zoom发布并实施面向学校的临时时限豁免；公告不是学校迁移、付费或教学效果实验。
    source_ids:
    - S1
  interpretation: 产品交付或规则是可观察工件；对用户心理、采用与因果的解释属于待检验假说。
  unknowns:
  - 内部决策、完整行为数据及反事实未知，不作为本题必需输入。
  sources:
  - id: S1
    url: https://www.zoom.com/en/blog/how-to-use-zoom-for-online-learning/
    publisher: Zoom
    published_at: '2020-03-29'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手来源正文；只提取新范围所需事实，未把搜索摘要当作验证。
  phase2_conditions: 正式采用新问题；保留原候选和旧规划以便追溯。
```

## PRO-051

```yaml
id: PRO-051
decision: retain
scenario_title: Terraform Enterprise 2017-12-12 GA
focus: evidence-selection
subdomain: b2b-adoption
main_question: 面对工作区历史、权限和策略护栏，先验证哪项责任确实不能由当前OSS流程覆盖？
expected_output: 一个组织治理验证项及自管替代边界
out_of_scope: 不套用其他开源工具案例的功能清单
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-051
  status: sourced
  reason: 2017 GA直接比较OSS与Enterprise的工作区及治理功能，可测试自管替代条件。
  event: Terraform Enterprise 2017-12-12 GA
  cutoff: 2017-12-12 公告已知、组织试用/购买前
  initial_facts:
  - id: F1
    text: OSS已有workspaces，便于个人和小团队管理多个state。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Enterprise把工作区集中并增加权限、UI和history。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: Sentinel提供policy-as-code治理护栏。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 公司称beta覆盖100多个组织；未公开具体买方预算或净收益。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 协作治理版GA，可做采购证据选择；不得断言开源必然不能满足或直接套当下HCP命名。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.hashicorp.com/blog/hashicorp-terraform-enterprise-general-availability
    publisher: HashiCorp / Maciej Skierkowski
    published_at: '2017-12-12'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 不套用其他开源工具案例的功能清单
```

## PRO-052

```yaml
id: PRO-052
decision: retain
scenario_title: Duolingo 2012-06 对外开放
focus: constrained-decision
subdomain: user-research-value
main_question: 对有电脑和网络但无法付费的学习者，免费课程解决了什么，仍没解决什么？
expected_output: 一项定位选择及时间/接入成本边界
out_of_scope: 不提前借后来的广告模式解释选择
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-052
  status: sourced
  reason: 2012发布原材料有免费定位、任务、商业计划与beta使用，不以免费直接推出学习障碍全部消除。
  event: Duolingo 2012-06 对外开放
  cutoff: 2012-06-19 发布；beta结果隐藏或按需分层
  initial_facts:
  - id: F1
    text: 提供英、西、法、德免费课程和真实网页翻译练习。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 商业翻译服务是将来的变现计划，免费学习不意味着业务无成本。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 发布引用创始人称beta10万人中3万人每周至少使用30分钟。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 电脑会追踪弱词并调整后续练习；这些使用数据不单独证明能力提高。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 免费服务上线，已有部分beta重复使用；支付门槛被移除，时间、动机和学习质量仍需区分。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.cmu.edu/news/stories/archives/2012/june/june19_duolingo.html
    publisher: CMU / Luis von Ahn、Severin Hacker
    published_at: '2012-06-19'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 不提前借后来的广告模式解释选择
```

## PRO-053

```yaml
id: PRO-053
decision: retain
scenario_title: WhatsApp 2011-02-22 v2.6群聊
focus: causal-modeling
subdomain: retention-workflow
main_question: 五人群聊把逐个发送改成共享会话，会怎样改变小组协调及打扰？
expected_output: 一条群聊机制及退出/静音边界
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-053
  status: sourced
  reason: 2011原始群聊发布有具体平台、人数和退出规则，足以作关系图扩展预测。
  event: WhatsApp 2011-02-22 v2.6群聊
  cutoff: 2011-02-22 功能公布、继续使用结果未知
  initial_facts:
  - id: F1
    text: iPhone、BlackBerry、Android v2.6支持群聊，Symbian尚在开发。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 首版群聊上限五人。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 用户可删除对话退出。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 群聊提醒可单独设置，不能假设参与者没有退出或静音选择。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 群聊推出；公告不提供关系图和留存效应。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://blog.whatsapp.com/group-chat
    publisher: WhatsApp Team
    published_at: '2011-02-22'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-054

```yaml
id: PRO-054
decision: retain
scenario_title: GitHub Student Developer Pack 2014-10-07
focus: evidence-selection
subdomain: distribution-growth
main_question: 免费工具降低学生成本后，什么证据才说明其转成真实项目中的持续使用？
expected_output: 一个验证证据，区分既有学生基线和Pack效果
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-054
  status: sourced
  reason: 原始发布确认学生免费套装、成本定位与资格，能评估长期渠道。
  event: GitHub Student Developer Pack 2014-10-07
  cutoff: 2014-10-07 发布、未来职业转化未知
  initial_facts:
  - id: F1
    text: 套装把合作伙伴开发工具免费提供学生。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 官方定位为降低真实工具成本并支持动手学习。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告列出Atom、云平台等工具，不能混用当下伙伴配额。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 发布前已有逾十万学生用免费GitHub；这是先前基线，非Pack效果。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 学生套装推出；未来付费与职业采用未在发布时证实。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://github.blog/developer-skills/career-growth/the-best-developer-tools-now-free-for-students/
    publisher: GitHub / John Britton
    published_at: '2014-10-07'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-055

```yaml
id: PRO-055
decision: reframe
scenario_title: Twitter 2017：字符上限触顶率的分母比较
focus: quantitative-calibration
subdomain: ux-activation
main_question: 英语推文9%恰好140字符、日语0.4%，二者差多少百分点、倍数是多少？这些数能否说明英语用户因限制而放弃发布的概率是日语用户的22.5倍？
expected_output: 8.6个百分点与22.5倍的计算，以及推文分母和未发布内容的识别边界。
out_of_scope: 不推断用户留存、放弃率或2006 SMS渠道效果；不把语言组差异当随机实验。
reason: 原2006渠道边界缺可核首版机制；改为2017-09-26明确发布的语言组统计与280字符试验，增加真实数量动作。
admission: eligible
admission_reason: 明确冻结单一工件/事件与问题；2条事前事实、2条有效证据、直接来源支持结果齐备。
research:
  id: PRO-055
  status: sourced
  reason: 原2006渠道边界缺可核首版机制；改为2017-09-26明确发布的语言组统计与280字符试验，增加真实数量动作。
  event: Twitter 2017：字符上限触顶率的分母比较
  cutoff: 2017-09-26 小范围扩字试验决策；试验结果不作先验
  initial_facts:
  - id: F1
    text: 当时既有上限140字符，公司希望保留简短表达。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司明确比较不同语言并计划仅对日中韩之外受挤压语言试验280字符。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 已发送英语推文中9%长度为140字符，日语为0.4%；这是推文分母，不是独立用户或全部尝试输入分母。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 作者描述因压缩而删词甚至不发送的情形，但未给其比例；已发布文本的触顶率无法识别未发送内容或用户级放弃率。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: Twitter公布小范围280字符测试并承诺继续收集数据；不能把当日政策公告写成已证实的留存提升。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 这是来源所述机制/作者观察；维护者只据此推演有限条件，不宣称独立因果实验或全局收益。
    source_ids:
    - S1
    attribution: 来源作者陈述与维护者范围判断分列
  unknowns:
  - 没有用户级去重或未发布草稿分母；语言差异还受表达习惯和内容构成影响。
  sources:
  - id: S1
    url: https://blog.x.com/en_us/topics/product/2017/Giving-you-more-characters-to-express-yourself
    publisher: Twitter / Aliza Rosen、Ikuhiro Ihara
    published_at: '2017-09-26'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - 检索Twitter/X原始字数历史；2017官方Giving-you-more-characters页面搜索可见但打开404，二手Jack引语未代替原文。
  - url: https://blog.x.com/en_us/topics/product/2017/Giving-you-more-characters-to-express-yourself
    result: 本轮实际打开并阅读正文，按新问题逐条复核；旧范围缺口通过显式修订消除，不声称找到了原来缺失的资料。
  phase2_conditions:
    original: 保留既定单一认知动作；结果仅最终揭晓。
    remediation_applied: true
    scope_change: 原2006渠道边界缺可核首版机制；改为2017-09-26明确发布的语言组统计与280字符试验，增加真实数量动作。
quantitative_inputs:
- name: 已发送英语推文140字符占比
  value: 9
  unit: '%'
  source_ids:
  - S1
- name: 已发送日语推文140字符占比
  value: 0.4
  unit: '%'
  source_ids:
  - S1
```

## PRO-056

```yaml
id: PRO-056
decision: reframe
scenario_title: Slack 2019披露：fair billing的信用额度
focus: causal-modeling
subdomain: pricing-monetization
main_question: 未使用席位产生抵后续账单的credit，会怎样改变管理员邀请成员的成本风险？
expected_output: 一条邀请—使用—后续账单的机制链及失效条件
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 收窄到S-1已披露credit机制，不要求未核活跃天数，也不混用DAU。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-056
  status: sourced
  reason: 收窄到S-1已披露credit机制，不要求未核活跃天数，也不混用DAU。
  event: Slack 2019披露：fair billing的信用额度
  cutoff: 2019 S-1公开后，按该披露评估邀请风险；不声称2013规则或确切活跃窗口。
  initial_facts:
  - id: F1
    text: S-1称部分付费客户按人数并月/季对账。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 未用满合同人数时可得信用额度抵后续账单，不是现金退款。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 风险因素称inactive用户带来fair billing credits。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: S-1的24小时创建/消费内容是DAU统计定义，未证实也是计费活跃定义。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: S-1确有未使用席位产生后续抵账credit的机制；未证明实际邀请量的因果变化。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1764925/000162828019006616/slacks-1a1.htm
    publisher: Slack / SEC
    published_at: '2019-05-13'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-057

```yaml
id: PRO-057
decision: retain
scenario_title: BlackBerry 2016-09-28 硬件开发外包决策
focus: constrained-decision
subdomain: strategy-pivot
main_question: 已有软件与品牌授权能力，是否足以支持停止内部硬件开发？
expected_output: 一项资源迁移选择及软件客户口径限制
out_of_scope: 不评价整个转型结果或猜内部意图
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-057
  status: sourced
  reason: 同期财报说明终止内部硬件、授权安排及软件客户结果，可评估能力迁移，区别非GAAP。
  event: BlackBerry 2016-09-28 硬件开发外包决策
  cutoff: 2016-09-28 决策公布；后续转型结果隐藏
  initial_facts:
  - id: F1
    text: 公司已有安全、应用软件及Android Hub+授权。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Q2已与印尼合资伙伴签设备制造、分发和品牌许可。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告称约3000企业customer wins；不能等同独立新logo。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 软件服务GAAP收入1.38亿美元、non-GAAP1.56亿美元，口径必须区分。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: Chen宣布结束内部硬件开发并外包，解释是降低资本需求；长期成效未由该公告证明。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1070235/000107023516000166/q217pressrelease.htm
    publisher: BlackBerry / SEC
    published_at: '2016-09-28'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 不评价整个转型结果或猜内部意图
```

## PRO-058

```yaml
id: PRO-058
decision: reframe
scenario_title: Uber 2010 Samasource活动：局部供需峰值
focus: prediction-counterfactual
subdomain: network-marketplaces
main_question: 增加全晚车辆会保证7—8点请求都被满足吗，哪项局部供需条件会使预测反转？
expected_output: 一个带时间和位置条件的预测及失败边界
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 正式采用预测备用题，取消没有数据的每辆车等待效应计算。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-058
  status: sourced
  reason: 正式采用预测备用题，取消没有数据的每辆车等待效应计算。
  event: Uber 2010 Samasource活动：局部供需峰值
  cutoff: 活动前配车；当晚7—8点结果隐藏，精确活动日未独立核
  initial_facts:
  - id: F1
    text: Uber通过用户和limo公司连接派车。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司尝试增加路上车辆并优化已有车辆位置来缩短接车。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 当晚虽增加车辆，7—8点同时请求仍未全部满足。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 公告解释其余时段较正常；不能用全晚车辆总量替代局部供需。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 同期公司记录当晚增加车辆后7—8点仍未全部满足请求；其余时段较正常。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  - 若来源为事后回顾，仅确认其明确记载的当时已知观察或已实施规则；不把后续效果当作事前可知。
  sources:
  - id: S1
    url: https://www.uber.com/us/en/newsroom/huge-hurts-demand-prediction-in-uberland/
    publisher: Uber Team
    published_at: '2010-11-17'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-059

```yaml
id: PRO-059
decision: replace
scenario_title: Buffer 2010：落地页意向到首笔付款
focus: evidence-selection
subdomain: user-research-value
main_question: 邮件登记、点击付费套餐与实际付款，哪一步最能检验付费需求，仍不能证明什么？
expected_output: 一项证据排序、下一步测试及小样本边界
out_of_scope: 不编造内部实验、未公开用户数或历史版本，不将发布方解释当独立测量。
reason: 真实换题：Zappos摄影售鞋原始材料未取得，采用创始人2011同期回顾的实际验证。
admission: eligible
admission_reason: 单一产品节点、两项背景与两项证据及直接支持的交付/观察结果已核对；准入不等于ready。
research:
  id: PRO-059
  status: sourced
  reason: 真实换题：Zappos摄影售鞋原始材料未取得，采用创始人2011同期回顾的实际验证。
  event: Buffer 2010：落地页意向到首笔付款
  cutoff: 2010年落地页加价格页之后、产品发布前；材料为2011创始人回顾，付款结果后揭。
  initial_facts:
  - id: F1
    text: 创始人想将排队发推做成独立应用。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 先用两页落地页收集邮件反馈，后加入价格页。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 价格页仍有人点击并留邮件；点击不是付款。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 2010-11-30推出可用产品，创始人记录四天内获得首名付费客户。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 创始人记载首笔实际付款；单次付款不证明广泛需求、留存或盈利。
    source_ids:
    - S1
  interpretation: 产品交付或规则是可观察工件；对用户心理、采用与因果的解释属于待检验假说。
  unknowns:
  - 内部决策、完整行为数据及反事实未知，不作为本题必需输入。
  sources:
  - id: S1
    url: https://buffer.com/resources/idea-to-paying-customers-in-7-weeks-how-we-did-it/
    publisher: Buffer / Joel Gascoigne
    published_at: '2011-02-16'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手来源正文；只提取新范围所需事实，未把搜索摘要当作验证。
  phase2_conditions: 正式采用新问题；保留原候选和旧规划以便追溯。
```

## PRO-060

```yaml
id: PRO-060
decision: reframe
scenario_title: Todoist 2026规则快照：固定周期与完成后周期
focus: hypothesis-diagnosis
subdomain: retention-workflow
main_question: 一项迟做的周任务再次排到周二，是调度规则还是留存机制；哪项观察最能区分？
expected_output: 一项规则诊断与独立留存验证
out_of_scope: 不编造内部实验、未公开用户数或历史版本，不将发布方解释当独立测量。
reason: 用已读官方规则快照取代未核2010s留存研究；允许推演文档例子，不虚构真实用户实验。
admission: eligible
admission_reason: 单一产品节点、两项背景与两项证据及直接支持的交付/观察结果已核对；准入不等于ready。
research:
  id: PRO-060
  status: sourced
  reason: 用已读官方规则快照取代未核2010s留存研究；允许推演文档例子，不虚构真实用户实验。
  event: Todoist 2026规则快照：固定周期与完成后周期
  cutoff: 以2026-10-25读取的官方规则为快照；不推定2010s已有同版行为。
  initial_facts:
  - id: F1
    text: 官方文档区分按原计划日期重复的every和按完成时间重复的every!。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 例子中周一到期的任务可能在周二完成。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: every week完成后安排下周一，every! week则安排下周二。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 规则只安排未来日期；逾期任务的下一次安排不能被当成用户留存的直接证据。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 官方规则工件明确两种日期行为；文档例子是说明性输入，不是用户实测。
    source_ids:
    - S1
  interpretation: 产品交付或规则是可观察工件；对用户心理、采用与因果的解释属于待检验假说。
  unknowns:
  - 内部决策、完整行为数据及反事实未知，不作为本题必需输入。
  sources:
  - id: S1
    url: https://www.todoist.com/help/todoist/features/introduction-to-recurring-dates-YUYVJJAV
    publisher: Todoist
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手来源正文；只提取新范围所需事实，未把搜索摘要当作验证。
  phase2_conditions: 正式采用新问题；保留原候选和旧规划以便追溯。
```

## PRO-061

```yaml
id: PRO-061
decision: reframe
scenario_title: Robinhood 2021披露：推荐奖励的触发点
focus: evidence-selection
subdomain: distribution-growth
main_question: 开户、绑银行账户与领取奖励，哪一步才触发该示例义务；持续有价值的账户还缺什么证据？
expected_output: 一项漏斗与义务触发的核对，提出下一项账户质量观察
out_of_scope: 不编造内部实验、未公开用户数或历史版本，不将发布方解释当独立测量。
reason: 正式采用证据题，缺少同cohort收益和奖励成本时不编造CAC回收；使用公司给SEC的真实示例。
admission: eligible
admission_reason: 单一产品节点、两项背景与两项证据及直接支持的交付/观察结果已核对；准入不等于ready。
research:
  id: PRO-061
  status: sourced
  reason: 正式采用证据题，缺少同cohort收益和奖励成本时不编造CAC回收；使用公司给SEC的真实示例。
  event: Robinhood 2021披露：推荐奖励的触发点
  cutoff: 2021公开披露该回复后审查规则；信件原为非公开提交，不假称6月15日已向全部投资人公开。
  initial_facts:
  - id: F1
    text: 公司2021-06-15回复SEC关于推荐奖励会计的询问。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 示例为已有用户分享链接，新用户注册、获批并绑银行账户。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公司称绑银行账户时才赚得奖励并给推荐者分配具体股票；不是点击或仅注册即触发。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 可在60天内领取，过期未领则不再有该义务；领取也不证明账户持续交易或贡献。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公司解释将所分配股票在领取时用于结清义务；这是代表性规则示例，不是全部推广活动或用户质量实验。
    source_ids:
    - S1
  interpretation: 产品交付或规则是可观察工件；对用户心理、采用与因果的解释属于待检验假说。
  unknowns:
  - 内部决策、完整行为数据及反事实未知，不作为本题必需输入。
  sources:
  - id: S1
    url: https://investors.robinhood.com/static-files/a427a740-0439-41da-ba14-c0f719358032
    publisher: Robinhood / SEC correspondence
    published_at: '2021-06-15'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手来源正文；只提取新范围所需事实，未把搜索摘要当作验证。
  phase2_conditions: 正式采用新问题；保留原候选和旧规划以便追溯。
```

## PRO-062

```yaml
id: PRO-062
decision: reframe
scenario_title: Datadog 2019：免费用户与组织付费的证据缺口
focus: evidence-selection
subdomain: b2b-adoption
main_question: 自助安装和免费使用之后，哪项组织行为最能支持付费采用，而不是把总客户增长当成转化率？
expected_output: 一条免费到组织采购的待验证链及优先证据
out_of_scope: 不编造内部实验、未公开用户数或历史版本，不将发布方解释当独立测量。
reason: 取得实际S-1正文，保留产品证据任务，取消虚构的单客户历史交接。
admission: eligible
admission_reason: 单一产品节点、两项背景与两项证据及直接支持的交付/观察结果已核对；准入不等于ready。
research:
  id: PRO-062
  status: sourced
  reason: 取得实际S-1正文，保留产品证据任务，取消虚构的单客户历史交接。
  event: Datadog 2019：免费用户与组织付费的证据缺口
  cutoff: 2019-09-17 S-1/A公开后评估采用证据。
  initial_facts:
  - id: F1
    text: 招股文件描述自助安装、免费试用及免费层。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司同时使用自助、inside sales和enterprise sales渠道。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公司明确警告免费层用户可能不带来组织内购买和部署。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 其客户指标排除免费层/试用；2019年6月30日8846客户不是所有试用用户分母。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公司实际披露混合销售模式及付费客户口径；未给试用到企业购买的因果转化率。
    source_ids:
    - S1
  interpretation: 产品交付或规则是可观察工件；对用户心理、采用与因果的解释属于待检验假说。
  unknowns:
  - 内部决策、完整行为数据及反事实未知，不作为本题必需输入。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1561550/000119312519246194/d745413ds1a.htm
    publisher: Datadog / SEC
    published_at: '2019-09-17'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手来源正文；只提取新范围所需事实，未把搜索摘要当作验证。
  phase2_conditions: 正式采用新问题；保留原候选和旧规划以便追溯。
```

## PRO-063

```yaml
id: PRO-063
decision: retain
scenario_title: Google Maps Navigation 2009-10-28 Android2.0 beta
focus: causal-modeling
subdomain: ux-activation
main_question: 语音引导与自动重规划移除了哪一步驾驶任务摩擦，又增加了什么联网边界？
expected_output: 一条任务链及离线反例
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-063
  status: sourced
  reason: 2009原始Google发布有任务前后路径和限制，留存因果明确未知。
  event: Google Maps Navigation 2009-10-28 Android2.0 beta
  cutoff: 2009-10-28 新导航已说明、采用未知
  initial_facts:
  - id: F1
    text: 之前手机路线为文字列表。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 新beta给Android2.0提供语音引导与自动重新规划。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 可键入或语音搜索目的地，不必知道精确地址。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 互联网连接带来最新地图、商家、交通及StreetView，意味着联网依赖。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 从查路线到行驶导航的功能推出；无留存提升的对照数据。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://maps.googleblog.com/2009/10/google-maps-navigation-comes-to-android.html
    publisher: Google / Iljya Kalai
    published_at: '2009-10-28'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-064

```yaml
id: PRO-064
decision: reframe
scenario_title: Spotify 2017广告层：毛利转正与免费获客
focus: quantitative-calibration
subdomain: pricing-monetization
main_question: 广告分部毛利率从-12%到10%改变多少，为什么60%新增Premium来自免费层仍不是免费转化率？
expected_output: 一项百分点计算与两种分母的边界
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 保留真实数量训练，取消单cohort完全成本/转化反事实。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-064
  status: sourced
  reason: 保留真实数量训练，取消单cohort完全成本/转化反事实。
  event: Spotify 2017广告层：毛利转正与免费获客
  cutoff: 2018-02-28 公开2017财报后、定性经济性判断前
  initial_facts:
  - id: F1
    text: 广告免费与Premium两服务并行。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司称自2014-02追踪以来超过60%新增Premium来自广告免费服务；不是免费用户转化率。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 2017广告分部毛利率10%，2016为负12%，披露主要受授权协议影响。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 版权和流媒体交付成本随免费MAU增加；毛利未包含全部经营费用。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 公司披露2017广告分部毛利转正；该结果不等于每位免费用户盈利。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1639920/000119312518063434/d494294df1.htm
    publisher: Spotify / SEC
    published_at: '2018-02-28'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
quantitative_inputs:
- name: 2016_ad_margin
  value: -12
  unit: percent
  source_ids:
  - S1
- name: 2017_ad_margin
  value: 10
  unit: percent
  source_ids:
  - S1
```

## PRO-065

```yaml
id: PRO-065
decision: retain
scenario_title: Google Reader 关闭（2013）
focus: constrained-decision
subdomain: strategy-pivot
main_question: 忠实用户与下降使用量同时存在时，是否应停止维护并提供数据迁出？
expected_output: 一项取舍及用户价值/资源约束的区别
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-065
  status: sourced
  reason: 当期关闭公告直接给出公司理由与退出安排；无足以量化资源机会成本的公开数据。
  event: Google Reader 关闭（2013）
  cutoff: 2013-03-13 关闭公告公布后，评价退出安排前
  initial_facts:
  - id: F1
    text: Reader仍有忠实用户。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Google称使用量下降并聚焦较少产品；这是公司解释而非独立审计。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 宣布2013-07-01退休，提供三个月迁移期。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 订阅数据可通过Google Takeout导出。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 公司正式宣布关闭及导出通道；公告未测量实际流失损失。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://googlereader.blogspot.com/2013/03/powering-down-google-reader.html
    publisher: Google / Alan Green
    published_at: '2013-03-13'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-066

```yaml
id: PRO-066
decision: retain
scenario_title: Apple App Store 上线（2008）
focus: constrained-decision
subdomain: network-marketplaces
main_question: 是否把定价权与70%分成留给开发者来启动应用供给？
expected_output: 一项平台激励选择及下载不等于长期网络效应
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-066
  status: sourced
  reason: 上线前分成与发布后分发行为均有同期官方公告；下载不等于长期网络效应。
  event: Apple App Store 上线（2008）
  cutoff: 2008-06-09 宣布分发规则后、七月实际采用前
  initial_facts:
  - id: F1
    text: 开发者自定应用价格，包括免费，并保留70%销售收入。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Apple宣布App Store将在62个国家提供无线分发。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 2008-07-14公告称上线首周末下载超过一千万次。
    source_ids:
    - S2
    availability: post_decision
  - id: E2
    text: 当时800余应用、200余免费，可无线下载、用iTunes账户付费并获得更新提醒。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 上线后出现大量下载与第三方供给；这些总量不证明分成安排单独造成采用。
    source_ids:
    - S2
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.apple.com/newsroom/2008/06/09iPhone-SDK-Downloads-Top-250-000/
    publisher: Apple
    published_at: '2008-06-09'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
  - id: S2
    url: https://www.apple.com/newsroom/2008/07/14iPhone-App-Store-Downloads-Top-10-Million-in-First-Weekend/
    publisher: Apple
    published_at: '2008-07-14'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-067

```yaml
id: PRO-067
decision: reframe
scenario_title: Twitch 2011 beta：游戏频道迁移方案
focus: prediction-counterfactual
subdomain: user-research-value
main_question: 保留关注者、VOD及旧链接，会怎样影响现有游戏频道迁移，什么仍会阻止创作者继续直播？
expected_output: 一个迁移预测、连续性机制及反例
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 把无分类集中度数据的垂直拆分识别题改成已有明确规则的频道迁移预测。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-067
  status: sourced
  reason: 把无分类集中度数据的垂直拆分识别题改成已有明确规则的频道迁移预测。
  event: Twitch 2011 beta：游戏频道迁移方案
  cutoff: 2011-06公开beta公告后、6月22日opt-in迁移前。
  initial_facts:
  - id: F1
    text: Twitch复用Justin.tv直播基础设施，专注电竞。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Justin.tv原游戏内容可在Twitch看，计划最终迁移并保留旧链接。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 6月22日opt-in保留观看量、关注者和VOD，并可让原频道自动跳转。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 公告称社区反馈参与开发；未给类别级需求对比。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 同期公告推出游戏直播beta并列6月22日opt-in迁移路径；没有证明所有创作者迁移成功。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://twitchtv.wordpress.com/2011/06/
    publisher: TwitchTV官方博客
    published_at: 2011-06
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-068

```yaml
id: PRO-068
decision: retain
scenario_title: GitHub Dependabot 集成（2019）
focus: causal-modeling
subdomain: retention-workflow
main_question: 把漏洞修复变成PR，在哪一步缩短发现到审查的闭环？
expected_output: 一条工作流机制与仍需人工判断的责任
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-068
  status: sourced
  reason: 2019公开beta清楚记录安全修复如何嵌入PR工作流；只验证机制和已发布行为，不把所有依赖升级当安全修复成效。
  event: GitHub Dependabot 集成（2019）
  cutoff: 2019-05-23公开beta发布后，评估审查流程前
  initial_facts:
  - id: F1
    text: Dependabot集成后，GitHub发布自动安全修复公开beta。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 修复以GitHub生成的pull request呈现，目标为依赖漏洞。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: PR形态把修复放入现有开发者审查流程。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 官方将其描述为自动化工作流中的繁琐部分；此为产品方价值主张。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 安全修复PR功能已发布；无漏洞修复时间或回归风险的独立效果数据。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://github.blog/changelog/2019-05-23-dependabot-automated-security-fixes/
    publisher: GitHub
    published_at: '2019-05-23'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-069

```yaml
id: PRO-069
decision: reframe
scenario_title: Musical.ly 2018整合：账户迁移与持续创作
focus: prediction-counterfactual
subdomain: distribution-growth
main_question: 账户、粉丝与内容自动迁移后，持续创作是否也会自动保持，哪项条件会使预测失败？
expected_output: 一条账户连续性到创作行为的预测及可观测反例
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 保留预测动作，正式取消没有材料的迁移后留存结论；实际升级工件作为最终揭晓。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-069
  status: sourced
  reason: 保留预测动作，正式取消没有材料的迁移后留存结论；实际升级工件作为最终揭晓。
  event: Musical.ly 2018整合：账户迁移与持续创作
  cutoff: 2018-08整合公告已公开、评价后续持续创作之前；网页标注8月2日。
  initial_facts:
  - id: F1
    text: 已有创作者账户、内容、粉丝将自动转到TikTok。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Musical.ly用户更新应用会自动升级到TikTok。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 升级版同时有社区feed和For You。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 反应、手势滤镜等被列为即将推出功能，不能说整合当日已全部可用。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 官方宣布应用升级并自动保留账户、内容与粉丝；没有披露创作者持续发布效果。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://newsroom.tiktok.com/musical-ly-and/?lang=en
    publisher: TikTok
    published_at: '2018-08-02'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-070

```yaml
id: PRO-070
decision: reframe
scenario_title: Figma 2016多人编辑：共同画布与评审协调
focus: causal-modeling
subdomain: ux-activation
main_question: 共同URL和同时编辑如何减少评审状态不同步，又在哪种工作方式下增加协调成本？
expected_output: 一条同步机制与不同意同步协作的反例
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 将缺单场光标日志的题改为官方交付规则与回顾明确支持的协调机制，不制造会议。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-070
  status: sourced
  reason: 将缺单场光标日志的题改为官方交付规则与回顾明确支持的协调机制，不制造会议。
  event: Figma 2016多人编辑：共同画布与评审协调
  cutoff: 2016-09-28多人编辑已交付后评价规则；使用2017回顾重建，具体场次不虚构。
  initial_facts:
  - id: F1
    text: 多人编辑于2016-09-28发布；依据2017官方回顾。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Figma同时提供稳定分享URL供多人访问同一设计。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 团队回顾列举结对设计、指导和设计批评用途。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 回顾承认结对设计有不同意见，未给单场光标交互记录。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 官方回顾确认2016-09-28推出多人编辑并列评审/结对用途；回顾承认结对设计有不同意见。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.figma.com/blog/reflecting-on-figmas-first-year/
    publisher: Figma / Dylan Field
    published_at: '2017-05-20'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-071

```yaml
id: PRO-071
decision: retain
scenario_title: Netflix 从单次租赁转向订阅（1999）
focus: constrained-decision
subdomain: pricing-monetization
main_question: 四次租赁加无到期日的套餐，会对低频和高频用户产生什么不同吸引力？
expected_output: 一项套餐选择，不能误称无限租赁
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-071
  status: sourced
  reason: 1999同期公告给出确切订阅规则，需修正候选常见的无限租赁说法；只支持任务与收费机制，不证明留存效果。
  event: Netflix 从单次租赁转向订阅（1999）
  cutoff: 1999-12-16 Marquee公开发布后，评估收费摩擦前
  initial_facts:
  - id: F1
    text: Marquee每月15.95美元含四次DVD租赁，无到期日与滞纳金。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 额外租赁每次3.98美元含运费，同时最多留四张；并非无限租赁。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 用户可预选片单，寄回DVD后自动寄下一张。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 可随时取消，并使用预付回邮信封。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 订阅与自动补片方案已发布；公告未给留存改善或相对按次方案实验。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://about.netflix.com/en/news/netflix-com-transforms-dvd-business-eliminating-late-fees-and-due-dates-from
    publisher: Netflix
    published_at: '1999-12-16'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 1999订阅不得与2000无限方案混用；发布公告12月与后续财报称9月推出的差异保留，不虚构同一天。
```

## PRO-072

```yaml
id: PRO-072
decision: reframe
scenario_title: Notion 2020 SCIM发布：登录与成员离职管理
focus: evidence-selection
subdomain: b2b-adoption
main_question: 客户担心离职者继续访问时，应先验证SSO登录还是SCIM成员移除链路，怎样设计区分性验证？
expected_output: 一项安全任务到验证步骤的对应及不充分条件
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 只要求已交付安全功能的验证选择，不虚构采购阻碍或因SCIM成交。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-072
  status: sourced
  reason: 只要求已交付安全功能的验证选择，不虚构采购阻碍或因SCIM成交。
  event: Notion 2020 SCIM发布：登录与成员离职管理
  cutoff: 2020-11-19 SCIM发布
  initial_facts:
  - id: F1
    text: SCIM让组织通过身份提供商创建、管理和移除成员与群组。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: SCIM及SAML SSO包含在Enterprise，支持Okta、Rippling和自定义应用。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 官方引导联系Enterprise团队。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: IBM、Nike、Pixar被列为Enterprise客户；未说明是否因SCIM成交。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 2020-11-19发布Enterprise SCIM及身份提供商支持；客户名单不证明成交原因。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.notion.com/releases/2020-11-19
    publisher: Notion
    published_at: '2020-11-19'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-073

```yaml
id: PRO-073
decision: retain
scenario_title: Pinterest 从 Tote 演化（2009—2010）
focus: hypothesis-diagnosis
subdomain: user-research-value
main_question: 收藏而不购买更支持哪一种用户任务解释？
expected_output: 两个假说与一个区分证据
out_of_scope: 不将创始人回忆称为当时日志
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-073
  status: sourced
  reason: 2011原始投资备忘录回述Tote的alpha行为与访谈，支持任务假说辨别；没有购买转化数据，不把分享当作零购买的测量。
  event: Pinterest 从 Tote 演化（2009—2010）
  cutoff: Tote alpha观察到分享行为后、决定聚焦Pinterest前；确切日期未核实
  initial_facts:
  - id: F1
    text: Tote为高端品牌开发商品目录iPhone应用；2011备忘录回述2009接触。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: alpha朋友用户大量使用一个小型社交分享功能；这是投资人记录的回顾性观察。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 备忘录说访谈发现用户缺少分享和策展商品清单的工具。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 团队搁置Tote，Pinterest于2010Q2发布；是路线变化而非购买假说被实验否定。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 团队将聚焦转向策展与分享；未提供Tote购买率或对照实验。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - alpha样本、日志和购买率不明；备忘录由投资人撰写，并非2009原始行为日志
  sources:
  - id: S1
    url: https://staging.bvp.com/memos/pinterest
    publisher: Bessemer / Jeremy Levine、Sarah Tavel
    published_at: '2011-04-03'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 区分实际记载的分享/策展与候选所说收藏不购买；不虚构零购买事实。
```

## PRO-074

```yaml
id: PRO-074
decision: retain
scenario_title: Adobe 收购 Figma 失败（2022—2023）
focus: constrained-decision
subdomain: strategy-pivot
main_question: 这项产品整合选择面临什么不可忽略的风险？
expected_output: 一个决策及能改变它的条件
out_of_scope: 不先揭晓交易结果或把受阻归为产品失败
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-074
  status: sourced
  reason: 交易未决时监管方公开竞争分析与最终公司公告可相互对照；监管判断仍是初步结论，不作为已证产品失败。
  event: Adobe 收购 Figma 失败（2022—2023）
  cutoff: 2023-11-28 CMA初步发现公开后、最终交易结局前
  initial_facts:
  - id: F1
    text: CMA称Adobe XD与Figma在产品设计软件竞争。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: CMA初步认为交易可能消除产品设计竞争，并影响图像编辑与插画创新；不是最终裁定。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 双方2023-12-18宣布终止交易。
    source_ids:
    - S2
    availability: post_decision
  - id: E2
    text: 双方解释为无法明确取得欧盟与英国必要批准，同时声明不同意监管发现。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 交易未完成；不能由此推论Figma产品失败或某项整合必然无价值。
    source_ids:
    - S2
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.gov.uk/government/news/adobe-figma-deal-could-harm-uk-digital-design-sector
    publisher: UK CMA
    published_at: '2023-11-28'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
  - id: S2
    url: https://news.adobe.com/news/news-details/2023/adobe-and-figma-mutually-agree-to-terminate-merger-agreement
    publisher: Adobe与Figma联合公告
    published_at: '2023-12-18'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 不先揭晓交易结果或把受阻归为产品失败
```

## PRO-075

```yaml
id: PRO-075
decision: reframe
scenario_title: Upwork 2015 Elance迁移：市场合并与参与者流失
focus: prediction-counterfactual
subdomain: network-marketplaces
main_question: 将用户与项目迁到一个更大市场，何时反而会减少有效参与，哪项迁移行为最能检验？
expected_output: 一个有条件的流动性预测与迁移流失反例
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 取消未取得的单品类规模精算，保留迁移预测并使用招股回顾的实际用户损失。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-075
  status: sourced
  reason: 取消未取得的单品类规模精算，保留迁移预测并使用招股回顾的实际用户损失。
  event: Upwork 2015 Elance迁移：市场合并与参与者流失
  cutoff: 2015-08迁移启动边界；2018回顾重建背景，用户流失结果后揭，不把2015-08计划放到5月。
  initial_facts:
  - id: F1
    text: 2014两平台合并后，2015-05刷新oDesk为Upwork；来自2018回顾披露。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 2015-08开始让Elance客户、自由职业者和项目迁入Upwork。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公司披露部分用户未迁移，短期拖累核心客户增长。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 公司称整合后市场更大、更有流动性；没有单品类比较数据。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 2018 S-1回顾部分用户没有迁移，短期拖累核心客户增长；规模增加不保证所有参与者受益。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1627475/000119312518267594/d575528ds1.htm
    publisher: Upwork / SEC
    published_at: '2018-09-06'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际阅读S-1迁移及核心客户章节；2015官方重启公告正文403，不将摘要当核实。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-076

```yaml
id: PRO-076
decision: reframe
scenario_title: Notion关系属性2026快照：客户与购买记录
focus: causal-modeling
subdomain: retention-workflow
main_question: 关联客户表和购买记录怎样增加复用价值，单向和双向选项又怎样增加理解与维护成本？
expected_output: 一条关系复用机制及复杂性抵消价值的条件
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 冻结已读官方文档的2026快照，不把当前关系默认行为回填2018。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-076
  status: sourced
  reason: 冻结已读官方文档的2026快照，不把当前关系默认行为回填2018。
  event: Notion关系属性2026快照：客户与购买记录
  cutoff: 2026-10-25读取的帮助文档快照；说明性客户/物品例子不是历史真实客户实验。
  initial_facts:
  - id: F1
    text: 当前官方文档以客户表与购买物品表说明关系。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 当前关系属性让两个数据库的页面相连接。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 当前路径为新增属性、选Relation、选目标库并添加关系。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 当前默认单向，可切换对应双向关系；不代表早期同样默认。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 官方文档提供建立关系及切换双向关系的实际流程；不证明历史留存提升。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.notion.com/help/relations-and-rollups
    publisher: Notion
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-077

```yaml
id: PRO-077
decision: reframe
scenario_title: Duolingo 2013 App of the Year：认可与需求归因
focus: evidence-selection
subdomain: distribution-growth
main_question: 获奖时已有下载和月活指标，哪项时间与来源证据才能区分自然需求和曝光冲击？
expected_output: 一个可区分的观察窗口及累计量不足的理由
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 取消未定位的排名活动，采用已核实2013获奖与同期指标的证据题。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-077
  status: sourced
  reason: 取消未定位的排名活动，采用已核实2013获奖与同期指标的证据题。
  event: Duolingo 2013 App of the Year：认可与需求归因
  cutoff: 2013获奖报道公开后，评价增长归因所需证据；不复演未核活动。
  initial_facts:
  - id: F1
    text: CMU 同期文章报道 Duolingo 获 Apple 2013 App of the Year。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 文章报告累计下载及月活；均非某次排名冲击的实验数据。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 文章引述创始人关于低收入学习者的需求。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 文章未提供获奖前后曝光、自然下载或留存序列。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: CMU同期报道Duolingo获得Apple 2013 App of the Year并列下载/月活；不是排名冲击实验。
    source_ids:
    - S1
  interpretation: 仅有公开自报/文档描述；不把发布、相关性或后来的成功当成因果结论。
  unknowns:
  - 实际活动、榜单口径、获奖与曝光先后、归因窗口
  sources:
  - id: S1
    url: https://www.cmu.edu/homepage/society/2013/fall/app-of-the-year.shtml
    publisher: Carnegie Mellon University
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 官方博客及同期 CMU 检索；阅读 CMU 正文；未用下载总量替代渠道归因。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-078

```yaml
id: PRO-078
decision: retain
scenario_title: Instagram Stories 发布（2016）
focus: prediction-counterfactual
subdomain: ux-activation
main_question: 24小时消失且无公开点赞的Stories，会怎样改变一次非正式分享的可见性成本？
expected_output: 一项分享预测及私信/观众控制反例
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-078
  status: sourced
  reason: 同期官方发布清楚记录临时分享规则和减少过度发帖担心的主张；未证明发布频率或心理压力的因果变化。
  event: Instagram Stories 发布（2016）
  cutoff: 2016-08-02美国发布后、评估用户行为前
  initial_facts:
  - id: F1
    text: Stories照片视频24小时自动消失，不出现在永久profile与feed。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 使用已有关注关系，在feed上方显示朋友或所关注账号的故事。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 没有公开点赞与评论，回应通过私信。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 可隐藏特定观众、查看谁看过，也可把部分故事发到永久profile。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: Stories功能上线；减少过度发帖担心是发布方主张，无对应对照实验。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://about.fb.com/ja/news/2016/08/instagram_instagramstories/
    publisher: Instagram / Meta日文Newsroom
    published_at: '2016-08-03'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-079

```yaml
id: PRO-079
decision: retain
scenario_title: Netflix 取消邮寄 DVD 与流媒体捆绑（2011）
focus: hypothesis-diagnosis
subdomain: pricing-monetization
main_question: 取消波发生在何时，能区分价格变化和Qwikster品牌变化的解释？
expected_output: 两个解释与时间顺序约束
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-079
  status: sourced
  reason: CEO同期财报电话会直接区分价格取消波与Qwikster品牌决策，支持拆分取舍复盘；无法把全部订户损失归因Qwikster。
  event: Netflix 取消邮寄 DVD 与流媒体捆绑（2011）
  cutoff: 2011-09 Qwikster计划公布后、十月撤回前；具体宣布日未以一手公告复核
  initial_facts:
  - id: F1
    text: DVD提供较完整片库但依赖邮寄，streaming即时但片库较少；CEO回顾的当时产品差别。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 价格上调已先在7月公告，取消反应早于Qwikster撤回。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: CEO称价格上调的取消反应分7月及9—10月两波。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 10月24日CEO确认迅速改变路线，DVD继续保留Netflix品牌；将Qwikster称作不听用户的象征是本人解释。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 放弃DVD另立品牌计划，继续推广streaming；不是恢复原有价格，也不证明拆分单独导致所有损失。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 未取得原始9月公告与10月10日博客；精确日期和双站账户细节不列为已核事实
  - CEO解释与实际因果贡献不同
  sources:
  - id: S1
    url: https://s22.q4cdn.com/959853165/files/doc_financials/quarterly_reports/2011/q3/NFLX-Transcript-2011-10-24T22_00.pdf
    publisher: Netflix财报电话会 / Thomson Reuters转录
    published_at: '2011-10-24'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-080

```yaml
id: PRO-080
decision: retain
scenario_title: Superhuman 2017—2018 PMF 调查与分群路线图
focus: evidence-selection
subdomain: user-research-value
main_question: 只能再深挖一群问卷受访者，应选谁来确定速度价值的改进路线？
expected_output: 一个分群证据选择及抽样偏差边界
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-080
  status: sourced
  reason: 创始人原文给出调查对象、问题、分群过程及后来问卷分数；足以做调查证据解读，不能据此证明因果 PMF。
  event: Superhuman 2017—2018 PMF 调查与分群路线图
  cutoff: 首次调查已回收、细分路线图尚待制定；具体日未知
  initial_facts:
  - id: F1
    text: 调查邀请近两周至少使用两次的用户。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 最初 very disappointed 回答为 22%；它只描述抽样回应，不代表全市场。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 四问包括失去产品感受、受益人、主要价值与改进建议。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 创始人后来报告分群、聚焦速度及改进后问卷比例达到 58%。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 创始人报告后续调查达到 58%；未提供随机试验或独立因果识别。
    source_ids:
    - S1
  interpretation: 仅有公开自报/文档描述；不把发布、相关性或后来的成功当成因果结论。
  unknowns:
  - 完整原始答卷、未回复偏差、同批样本可比性、留存与收入反事实
  sources:
  - id: S1
    url: https://blog.superhuman.com/how-superhuman-built-an-engine-to-find-product-market-fit/
    publisher: Superhuman / Rahul Vohra
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 阅读创始人文章调查方法、四步骤和结尾结果；仅把数值作为自报调查。
  phase2_conditions: 与 INV-034 同源；本题限问卷分群和产品路线图，投资题需独立投资材料；58% 只在最终揭晓。
```

## PRO-081

```yaml
id: PRO-081
decision: reframe
scenario_title: Twilio 2016披露：开发者自助与企业采购
focus: causal-modeling
subdomain: b2b-adoption
main_question: 免费API试用移除了哪一步阻力，为什么企业安全和采购批准仍可能成为独立瓶颈？
expected_output: 一条技术采用到组织购买的因果链及瓶颈边界
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 改为同份2016文件明确支持的双重角色机制，不制造早期单个客户交接。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-081
  status: sourced
  reason: 改为同份2016文件明确支持的双重角色机制，不制造早期单个客户交接。
  event: Twilio 2016披露：开发者自助与企业采购
  cutoff: 2016-10-07公开文件的模式快照。
  initial_facts:
  - id: F1
    text: 开发者可免费试用，通过文档与免费支持开始，按用量扩张付费。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Enterprise Plan提供安全、访问管理和细粒度管理；产品最早从2008语音API开始。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 企业部署可能需安全、合规、采购、运营、IT批准，教育和价格谈判更久。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 销售针对技术与业务领导，后者咨询开发者；公司称开发者常是倡导者。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: S-1记录开发者试用与企业销售角色并存；公司称开发者常为倡导者，未证明每次试用都会成交。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1447669/000119312516733893/d237988ds1.htm
    publisher: Twilio / SEC
    published_at: '2016-10-07'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-082

```yaml
id: PRO-082
decision: replace
scenario_title: HBO Max→Max 2023：品牌扩展与旧用户连续性
focus: prediction-counterfactual
subdomain: strategy-pivot
main_question: 品牌从HBO扩展到全家内容，会怎样影响既有用户的价值识别，保留历史与套餐能消除哪些风险？
expected_output: 一个品牌预测与用户连续性缓解措施的边界
out_of_scope: 不编造内部实验、未公开用户数或历史版本，不将发布方解释当独立测量。
reason: 真实换题：Twitter/X缺直接结果材料，采用WBD同期公告中明确品牌目标和迁移措施；不要求广告信任测量。
admission: eligible
admission_reason: 单一产品节点、两项背景与两项证据及直接支持的交付/观察结果已核对；准入不等于ready。
research:
  id: PRO-082
  status: sourced
  reason: 真实换题：Twitter/X缺直接结果材料，采用WBD同期公告中明确品牌目标和迁移措施；不要求广告信任测量。
  event: HBO Max→Max 2023：品牌扩展与旧用户连续性
  cutoff: 2023-04-12公告后、5月23日计划推出前。
  initial_facts:
  - id: F1
    text: 2023-04-12宣布Max，计划5月23日在美国推出。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司解释新品牌要表达HBO Max与discovery+之外更广的内容定位；这是公司目标。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告承诺现有HBO Max用户按原价格进入，并至少六个月保留现套餐功能。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 资料、观看历史和列表迁移是连续性承诺，不能自动维持对HBO品牌的认知。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: WBD实际发布Max品牌和迁移方案；公告中的计划不等于全部迁移已完成或品牌效果已测量。
    source_ids:
    - S1
  interpretation: 产品交付或规则是可观察工件；对用户心理、采用与因果的解释属于待检验假说。
  unknowns:
  - 内部决策、完整行为数据及反事实未知，不作为本题必需输入。
  sources:
  - id: S1
    url: https://ir.wbd.com/news-and-events/financial-news/financial-news-details/2023/WARNER-BROS.-DISCOVERY-UNVEILS-MAX-STREAMING-SERVICE/default.aspx
    publisher: Warner Bros. Discovery
    published_at: '2023-04-12'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手来源正文；只提取新范围所需事实，未把搜索摘要当作验证。
  phase2_conditions: 正式采用新问题；保留原候选和旧规划以便追溯。
```

## PRO-083

```yaml
id: PRO-083
decision: reframe
scenario_title: GitHub 2008 Fork Queue：跨fork采用提交
focus: boundary-transfer
subdomain: network-marketplaces
main_question: 网站上挑选提交就能替代本地协作验证吗，冲突与测试在哪一步限制这一便利？
expected_output: 一个从发现到采用的迁移边界及验证条件
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 把未证明的关系网络锁定改为已交付Fork Queue的协作边界，不要求具体跨项目贡献故事。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-083
  status: sourced
  reason: 把未证明的关系网络锁定改为已交付Fork Queue的协作边界，不要求具体跨项目贡献故事。
  event: GitHub 2008 Fork Queue：跨fork采用提交
  cutoff: 2008-12 Fork Queue发布快照。
  initial_facts:
  - id: F1
    text: 2008-02 PR可通知fork者拉取，或让其请求原作者拉取。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 2008-12 Fork Queue按用户列项目fork网络的commits。
    source_ids:
    - S2
    availability: pre_decision
  evidence:
  - id: E1
    text: 可选提交cherry-pick到测试branch，报告成功/失败，并忽略不适用提交。
    source_ids:
    - S2
    availability: post_decision
  - id: E2
    text: 官方建议本地fetch测试后再合并；网站操作不取代测试。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: GitHub发布按用户列fork提交、cherry-pick到测试branch及报告成功/失败的工件，同时建议本地测试。
    source_ids:
    - S2
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://github.blog/news-insights/the-library/oh-yeah-there-s-pull-requests-now/
    publisher: GitHub / Chris Wanstrath
    published_at: '2008-02-23'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
  - id: S2
    url: https://github.blog/news-insights/the-library/the-fork-queue/
    publisher: GitHub / Scott Chacon
    published_at: '2008-12-16'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-084

```yaml
id: PRO-084
decision: retain
scenario_title: Adobe Creative Cloud Libraries（2014—）
focus: causal-modeling
subdomain: retention-workflow
main_question: 跨工具复用怎样改变一次交付和退出成本？
expected_output: 一条复用机制及不依赖套件的替代条件
out_of_scope: 不把全部套件续费都归因于共享素材
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-084
  status: sourced
  reason: 2016具体版本明确跨文档/应用共享与只读权限，可据此判断单素材复用及替代边界；没有退出成本的实际测量。
  event: Adobe Creative Cloud Libraries（2014—）
  cutoff: 2016-06-21 Photoshop CC更新后、判断素材交付方式前
  initial_facts:
  - id: F1
    text: Libraries让设计元素在多个文档与Creative Cloud应用间应用并与同事共享。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 2016此版新增只读共享，让同事使用素材但不能改变、重命名或删除。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 新增Stock许可徽标可辨认库素材是否已许可。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 发布者回述Libraries起于2014；2016新权限不能回填2014首版。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 跨工具素材和只读共享功能有具体版本；退出成本机制属于待判断推论，未有续费因果数据。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://blog.adobe.com/en/publish/2016/06/21/adobe-releases-major-photoshop-cc-update-today-and-announces-more-digital-imaging-product-features-coming-soon
    publisher: Adobe / Pam Clark
    published_at: '2016-06-21'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  phase2_conditions: 不把全部套件续费都归因于共享素材
```

## PRO-085

```yaml
id: PRO-085
decision: reframe
scenario_title: Zoom 2019披露：大客户的免费起点
focus: quantitative-calibration
subdomain: distribution-growth
main_question: 344个大客户中55%曾有免费host大约对应多少客户，为什么这不是受邀者转付费率？
expected_output: 一项数量级复算、条件概率分母与选择偏差说明
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 保留真实数量训练，取消未取得的首次主持流程与受邀用户分母。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-085
  status: sourced
  reason: 保留真实数量训练，取消未取得的首次主持流程与受邀用户分母。
  event: Zoom 2019披露：大客户的免费起点
  cutoff: 2019-03-22公开2019模式
  initial_facts:
  - id: F1
    text: 公司说用户通常先由同事邀请参加会议，可免费加入或主持。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司称参会者体验后常成为付费host；不是独立对照效果。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 截至2019-01-31财年344个年收入超过10万美元客户中，55%订阅前至少有一位免费host。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 上述分母为既有大客户，不是所有受邀者，也没有首次主持身份流程。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: S-1披露既有大客户中55%曾有免费host；不是所有受邀者的转化实验。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1585521/000119312519083351/d642624ds1.htm
    publisher: Zoom / SEC
    published_at: '2019-03-22'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
quantitative_inputs:
- name: large_customers
  value: 344
  unit: customers with annual revenue above USD100000
  source_ids:
  - S1
- name: prior_free_host_share
  value: 55
  unit: percent of those large customers
  source_ids:
  - S1
```

## PRO-086

```yaml
id: PRO-086
decision: reframe
scenario_title: TikTok 2020 For You：无关注图的首轮推荐
focus: hypothesis-diagnosis
subdomain: ux-activation
main_question: 没有关注任何人时，首轮推荐仍能形成什么反馈链，怎样区分兴趣匹配和热门内容的解释？
expected_output: 两个竞争解释与一项能区分的新用户观察
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 改为公开冷启动机制与可检验解释，不要求缺失的真实分群实验或宣称推荐效果。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-086
  status: sourced
  reason: 改为公开冷启动机制与可检验解释，不要求缺失的真实分群实验或宣称推荐效果。
  event: TikTok 2020 For You：无关注图的首轮推荐
  cutoff: 2020-06-18公开说明的产品快照
  initial_facts:
  - id: F1
    text: 打开TikTok落入For You；新用户可选择宠物、旅行等兴趣类别。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 不选择类别时先给通用热门视频；首轮点赞、评论、重播开始个性化。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 完成较长视频比国家相同等弱信号权重更高，关注也能影响推荐。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 官方称For You是多数用户停留的地方；未给新用户关系图条件实验。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 官方2020说明新用户可选兴趣或先看通用热门视频，再由互动更新推荐；没有给新用户因果对照。
    source_ids:
    - S1
  interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
  unknowns:
  - 内部决策材料、反事实与独立效果测量未公开
  sources:
  - id: S1
    url: https://newsroom.tiktok.com/how-tiktok-recommends-videos-for-you?lang=en
    publisher: TikTok
    published_at: '2020-06-18'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-087

```yaml
id: PRO-087
decision: reframe
scenario_title: Workers 2023 CPU计量：I/O等待的计费边界
focus: boundary-transfer
subdomain: pricing-monetization
main_question: 把I/O等待占比较高的服务迁移时，CPU计量改变哪项成本暴露，为什么不能只凭wall time判断账单？
expected_output: 一条CPU/等待口径边界与迁移时仍需核对的输入
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 正式采用计量边界备用题，取消无实测同负载/完整旧价表的账单计算；不把官方例子当客户实测。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-087
  status: sourced
  reason: 正式采用计量边界备用题，取消无实测同负载/完整旧价表的账单计算；不把官方例子当客户实测。
  event: Workers 2023 CPU计量：I/O等待的计费边界
  cutoff: 2023-09-28 公告后、2023-10-31 选择迁移前
  initial_facts:
  - id: I1
    text: 新方案按 CPU 时间而非等待 I/O 的 wall time 计计算量；适用 Workers 和 Pages Functions。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 公告允许 2023-10-31 起逐项目 opt in，新项目默认新价；Paid 与 Enterprise 合同迁移有不同时间规则。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 文章给出 100ms 总耗时、10ms CPU 的说明性例子，但未标为真实客户同负载测量，不能作为历史实测工作负载。
    source_ids: *id001
    availability: pre_decision
  - id: E2
    text: 旧 Bundled/Unbound 与新价表在嵌图中；正文没有完整可复算价格表。
    source_ids: *id001
    availability: pre_decision
  outcome:
    text: 2023-09-28官方公告CPU-time新计量与opt-in安排；此交付不证明任何客户实际省钱。
    source_ids:
    - S1
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 未取得两版完整价格表和同一真实请求量、CPU 与 wall time 数据，主线账单对照无法完成。
  sources:
  - id: S1
    url: https://blog.cloudflare.com/workers-pricing-scale-to-zero/
    publisher: Cloudflare
    published_at: '2023-09-28'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 打开并阅读定价公告正文与迁移范围；点击 old/new pricing 图均抓取失败。
  - 检索历史定价和正文 workload；未把示意用量或当前滚动价格替代历史真实负载。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-088

```yaml
id: PRO-088
decision: retain
scenario_title: Figma 2015-12-03 Preview 后继续投入浏览器协作
focus: evidence-selection
subdomain: user-research-value
main_question: 哪项需求证据最能支持继续投入浏览器协作？
expected_output: 一个优先验证信号及可拒绝条件
out_of_scope: 不复用融资论点或多人数据模型机制
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-088
  status: sourced
  reason: 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。
  event: Figma 2015-12-03 Preview 后继续投入浏览器协作
  cutoff: 2015-12-03 Preview 公开后、决定下一步协作需求验证前
  initial_facts:
  - id: I1
    text: Preview 已提供链接分享、上下文反馈和共享品牌颜色；作者称曾内部 dogfood 18 个月并与 alpha 用户合作。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 设计师跨职能任务包括共享资产、改文案、给工程师标注；这是创始人对协作需求的判断，并非独立需求统计。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 2015 公告把 simultaneous multiplayer editing 与共享资产库列为 2016 计划，不能当当时已交付。
    source_ids: *id001
    availability: pre_decision
  - id: E2
    text: 2016-09-28 发布公告才确认实时多人编辑完成并向所有人开放注册。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: Preview 先交付分享与反馈；多人同时编辑于 2016 后续交付，二者必须分时点。
    source_ids:
    - S1
    - S2
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - alpha 访谈原始记录、任务频率和付费意愿未知。
  sources:
  - id: S1
    url: https://www.figma.com/blog/design-meet-the-internet/
    publisher: Figma / Dylan Field
    published_at: '2015-12-03'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - outcome
  - id: S2
    url: https://www.figma.com/blog/multiplayer-editing-in-figma/
    publisher: Figma / Evan Wallace
    published_at: '2016-09-28'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
    - outcome
  attempts:
  - 打开 2015 Preview 及 2016 multiplayer 公告，逐段核对现有功能与未来计划。
  phase2_conditions:
  - 主问题限需求优先验证信号及拒绝条件；不复用融资或多人数据结构机制。
  - 2016 结局不得进入 2015 首轮。
```

## PRO-089

```yaml
id: PRO-089
decision: reframe
scenario_title: GitLab Goldman Sachs客户案例：工具链整合任务
focus: evidence-selection
subdomain: b2b-adoption
main_question: 从自建工具到GitLab，现有材料最支持哪项购买任务，又不足以证明哪些部署控制取舍？
expected_output: 一个有来源的采用理由及不能推出的采购条件
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 采用直接客户案例的采购任务，不要求未取得的历史合同签署日和部署控制。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-089
  status: sourced
  reason: 采用直接客户案例的采购任务，不要求未取得的历史合同签署日和部署控制。
  event: GitLab Goldman Sachs客户案例：工具链整合任务
  cutoff: 以2026-10-25读到的客户案例为已公开工件；原采购日期未披露，不设虚构历史决策日。
  initial_facts:
  - id: F1
    text: 客户案例描述Goldman从自建工具链评估git-based产品。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 案例描述需求覆盖代码、评审、构建、测试及部署。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: GitLab 客户案例称 Goldman 从自建工具链评估 git-based 产品，认为 GitLab CI/CD 最符合需求。
    source_ids:
    - S1
    availability: unknown
  - id: E2
    text: 案例记载其使用代码、评审、构建、测试和部署完整生态，并引述企业管理层。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 客户案例记载Goldman采用GitLab CI/CD和代码到部署生态；不能据此断言完整采购合同或实际控制权条款。
    source_ids:
    - S1
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 客户案例未明确采购日期、当时 SaaS/self-managed 选项、部署控制要求和预算审批链。
  - 不能从金融行业身份推断必然自托管，或从现行 Premium 名称回填当时套餐。
  sources:
  - id: S1
    url: https://about.gitlab.com/customers/goldman-sachs/
    publisher: GitLab / Goldman Sachs quoted participants
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 检索集团采购/部署控制候选并打开 Goldman Sachs 客户案例全文，检查采购角色、评估过程和部署说明。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-090

```yaml
id: PRO-090
decision: retain
scenario_title: Google 2022-09-29 宣布关闭 Stadia 消费服务
focus: hypothesis-diagnosis
subdomain: strategy-pivot
main_question: 可运行的流媒体技术是否足以推出消费者服务达到采用要求？
expected_output: 技术可行与商业采用两个假说，保留未公开阈值
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-090
  status: sourced
  reason: 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。
  event: Google 2022-09-29 宣布关闭 Stadia 消费服务
  cutoff: 2022-09-29 宣布关闭前；准确内部决策日期未知
  initial_facts:
  - id: I1
    text: Stadia 已作为消费者云游戏服务运营，用户持有通过服务购买的游戏库。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 相关交易包括 Google Store 购买的 Stadia 硬件和 Stadia Store 的游戏及附加内容。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 负责人称技术基础强但用户 traction 未达到预期；这是公司归因，未公布活跃/留存阈值。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 公告安排 2023-01-18 前继续游玩，并退还指定渠道硬件、游戏及附加内容购买款。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: Google 正式开始 winding down 消费者 Stadia，同时表示底层流媒体技术可用于公司其他业务；没有宣称技术不可用。
    source_ids:
    - S1
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 产品采用不足的具体机制、财务阈值及技术体验对用户流失的独立贡献未知。
  sources:
  - id: S1
    url: https://blog.google/products-and-platforms/products/stadia/message-on-stadia-streaming-strategy/
    publisher: Google / Phil Harrison
    published_at: '2022-09-29'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 打开官方关闭公告正文，核对 traction 归因、游戏可用期、退款范围与技术再利用描述。
  phase2_conditions:
  - 隐藏关闭结果；学员比较技术可行与商业采用假说，不直接把厂商归因当因果证明。
```

## PRO-091

```yaml
id: PRO-091
decision: retain
scenario_title: Substack 2022-04-12 recommendations beta
focus: boundary-transfer
subdomain: network-marketplaces
main_question: 作者控制的推荐与回荐在什么条件下形成有效传播，又何时只是互相循环？
expected_output: 一个网络边界与净新增不能识别的反例
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-091
  status: sourced
  reason: 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。
  event: Substack 2022-04-12 recommendations beta
  cutoff: 2022-04-12 发布后、预测作者推荐网络效果前
  initial_facts:
  - id: I1
    text: 作者此前推荐其他作者大多为手动操作；平台称作者希望有更容易的合作方式。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 新功能由作者选择推荐 publication 及评语，新读者订阅后看到推荐；不是算法推荐。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 获推荐作者会收到含订阅影响的通知并被鼓励回荐；作者可管理推荐列表。
    source_ids: *id001
    availability: pre_decision
  - id: E2
    text: 5 月更新收录作者报告增长加快，并称推荐别人的作者更可能被回荐；这些是平台观察和用户自述，未给随机对照。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 推荐流程已交付，后来更新出现跨作者订阅传播的观察；不能把相关性当净新增或付费留存因果。
    source_ids:
    - S1
    - S2
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 曝光、订阅与反事实净增长的独立 cohort 未取得；互荐的质量和操纵边界未知。
  sources:
  - id: S1
    url: https://on.substack.com/p/recommendations
    publisher: Substack
    published_at: '2022-04-12'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - outcome
  - id: S2
    url: https://on.substack.com/p/recommendations-update
    publisher: Substack
    published_at: '2022-05-16'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
    - outcome
  attempts:
  - 打开发布与一个月更新全文，区分作者控制、通知机制和事后推广指标。
  phase2_conditions:
  - 只锚定 2022 首发；不把 2024 app+recommendations 合并贡献倒填首发结果。
```

## PRO-092

```yaml
id: PRO-092
decision: reframe
scenario_title: Google Photos 2015：备份到检索的复用价值
focus: causal-modeling
subdomain: retention-workflow
main_question: 自动备份怎样通过检索和跨设备复用产生继续使用的价值，哪些价值无需假定退出受阻？
expected_output: 一条备份—组织—复用的机制链及其失效条件
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 保留同版可读的核心机制，取消没有材料的2015导出/退出规则。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-092
  status: sourced
  reason: 保留同版可读的核心机制，取消没有材料的2015导出/退出规则。
  event: Google Photos 2015：备份到检索的复用价值
  cutoff: 2015-05-28 上线后、用户选择自动备份前
  initial_facts:
  - id: I1
    text: 推出的 standalone Photos 自动备份并同步，可在多设备访问。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 免费 unlimited high-quality 为压缩档，公告说明照片最高 16MP、视频 1080p；不能称无限原图。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 产品按人物、地点和事物自动分组并支持搜索，无需手动标签；可生成拼图、动画等复用内容。
    source_ids: *id001
    availability: pre_decision
  - id: E2
    text: 分享链接可让收件人不装 app 或登录就查看，并将内容保存到自己的图库。
    source_ids: *id001
    availability: pre_decision
  outcome:
    text: 2015-05-28发布自动备份、搜索组织与链接分享；不能据此宣称留存提升或无法导出。
    source_ids:
    - S1
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 2015 年该版批量导出、元数据完整性和退出条件未取得同期直接说明；现行 Takeout 不能倒推。
  sources:
  - id: S1
    url: https://blog.google/products-and-platforms/products/photos/picture-this-fresh-approach-to-photos/
    publisher: Google / Anil Sabharwal
    published_at: '2015-05-28'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 打开首发公告核对套餐、自动上传、搜索和分享。
  - 检索 2015 Google Photos Takeout / export，结果多为当前第三方迁移教程，未将其作为当时导出条件。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-093

```yaml
id: PRO-093
decision: replace
scenario_title: Bluesky 2024取消邀请：增长控制与社区质量
focus: hypothesis-diagnosis
subdomain: distribution-growth
main_question: 取消邀请码后增长加快若伴随体验下降，怎样区分稀缺消失和审核容量压力？
expected_output: 两个竞争解释、一项分群观察及容量边界
out_of_scope: 不编造内部实验、未公开用户数或历史版本，不将发布方解释当独立测量。
reason: 真实换题：Clubhouse原文不可读，采用Bluesky同期公开记录；邀请码不仅可能制造稀缺，也被用于管理增长。
admission: eligible
admission_reason: 单一产品节点、两项背景与两项证据及直接支持的交付/观察结果已核对；准入不等于ready。
research:
  id: PRO-093
  status: sourced
  reason: 真实换题：Clubhouse原文不可读，采用Bluesky同期公开记录；邀请码不仅可能制造稀缺，也被用于管理增长。
  event: Bluesky 2024取消邀请：增长控制与社区质量
  cutoff: 2024-02-06开放公告后，评估后续增长与社区行为的假说。
  initial_facts:
  - id: F1
    text: 2024-02-06 Bluesky宣布任何人可以注册，无需邀请码。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 团队解释此前一年用邀请控制增长，同时建设审核工具和custom feeds。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 当日公告已有超过300万人；这是注册规模描述，不是活跃或留存测量。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 开放与审核工具建设同时存在，无法仅凭总增长识别邀请码稀缺对关系质量的作用。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 平台实际宣布并开放无邀请注册；没有把注册数视为持久关系网络或审核效果。
    source_ids:
    - S1
  interpretation: 产品交付或规则是可观察工件；对用户心理、采用与因果的解释属于待检验假说。
  unknowns:
  - 内部决策、完整行为数据及反事实未知，不作为本题必需输入。
  sources:
  - id: S1
    url: https://bsky.social/about/blog/02-06-2024-join-bluesky
    publisher: Bluesky
    published_at: '2024-02-06'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手来源正文；只提取新范围所需事实，未把搜索摘要当作验证。
  phase2_conditions: 正式采用新问题；保留原候选和旧规划以便追溯。
```

## PRO-094

```yaml
id: PRO-094
decision: reframe
scenario_title: Zoom加入路径2026读取快照：电脑音频与电话
focus: boundary-transfer
subdomain: ux-activation
main_question: 浏览器不能完成电脑音频时，电话加入何时能延续参会任务，何时无法替代？
expected_output: 一个围绕音频任务的替代路径及功能边界
out_of_scope: 不编造内部实验、未公开用户数或历史版本，不将发布方解释当独立测量。
reason: 按实际读取的FAQ收窄为音频路径，不声称2013零安装/零注册，也不推定2018页面从未改过。
admission: eligible
admission_reason: 单一产品节点、两项背景与两项证据及直接支持的交付/观察结果已核对；准入不等于ready。
research:
  id: PRO-094
  status: sourced
  reason: 按实际读取的FAQ收窄为音频路径，不声称2013零安装/零注册，也不推定2018页面从未改过。
  event: Zoom加入路径2026读取快照：电脑音频与电话
  cutoff: 2026-10-25读取的FAQ快照，原页标注2018-01-30；不声称冻结了2018全部规则。
  initial_facts:
  - id: F1
    text: FAQ列浏览器、客户端、移动端及电话加入方式。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 浏览器路径要求输入meeting ID；电话路径使用邀请中的拨号号码与ID。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 电脑音频还需可用输入输出设备并选择Join Audio，进入会议不等于已接通音频。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 电话可不装Zoom app加入，但该路径不能由本文证明提供屏幕共享或完整视觉任务。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 官方FAQ记载多条加入与音频检查路径；文档行为不等于真实用户摩擦已经测量。
    source_ids:
    - S1
  interpretation: 产品交付或规则是可观察工件；对用户心理、采用与因果的解释属于待检验假说。
  unknowns:
  - 内部决策、完整行为数据及反事实未知，不作为本题必需输入。
  sources:
  - id: S1
    url: https://www.zoom.com/en/blog/zoom-faqs-joining-meetings/
    publisher: Zoom / Jihoon Park
    published_at: '2018-01-30'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手来源正文；只提取新范围所需事实，未把搜索摘要当作验证。
  phase2_conditions: 正式采用新问题；保留原候选和旧规划以便追溯。
```

## PRO-095

```yaml
id: PRO-095
decision: reframe
scenario_title: Apple 2016订阅公告：一年后的分成激励
focus: prediction-counterfactual
subdomain: pricing-monetization
main_question: 提高持续订阅一年后的开发者收入，会怎样改变留存投入，在哪些条件下也可能增加用户退出摩擦？
expected_output: 一个有条件的激励预测及负面反例
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 限定同期公告明确的一年后收入提高，不将当前70/85细则、Small Business或累计规则倒填2016。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-095
  status: sourced
  reason: 限定同期公告明确的一年后收入提高，不将当前70/85细则、Small Business或累计规则倒填2016。
  event: Apple 2016订阅公告：一年后的分成激励
  cutoff: 2016-06-08 公告后、开发者决定是否设计长期订阅前
  initial_facts:
  - id: I1
    text: 官方当日公告计划把自动续订订阅开放到所有 app 类别，包括游戏。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 公告将符合资格订阅满一年后的开发者收入提升列为新政策，并提供更灵活定价；不是所有一次性购买降抽成。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 当前官方规则说明首年 70%、累计一年付费服务后 85%，扣除适用税费；当前文档包含后来 Small Business 等例外，不能整页回填 2016。
    source_ids:
    - S2
    availability: unknown
  - id: E2
    text: 2016 原公告仅在此页说明一年后提高收入，其详细原链接已失效，原版精确例外和累计规则未完整取得。
    source_ids: *id001
    availability: pre_decision
  outcome:
    text: 2016-06-08官方宣布扩展订阅资格并提高满一年后的开发者收入；本题不要求失效旧链接中的精确例外。
    source_ids:
    - S1
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 尚缺 2016 原始完整条文，不能确认当前的恢复天数、group 计算及特殊项目例外均适用于当年。
  - 留存是否因此改善没有因果试验，不能用政策意图冒充实际效果。
  sources:
  - id: S1
    url: https://developer.apple.com/news/?id=06082016a
    publisher: Apple
    published_at: '2016-06-08'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E2
    - outcome
  - id: S2
    url: https://developer.apple.com/app-store/subscriptions/
    publisher: Apple
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E1
  attempts:
  - 打开 Apple 2016 Coming Soon 原公告与现行订阅文档；核对当前分配规则并标明版本差异。
  - 原文 What’s New in Subscriptions 链接 404，尝试 WWDC2016 301 两版 URL 均不可访问；未以媒体摘要替代精确历史条文。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-096

```yaml
id: PRO-096
decision: reframe
scenario_title: Calendly预约页2026快照：两边身份与协调摩擦
focus: causal-modeling
subdomain: user-research-value
main_question: 预约方无需注册而组织者配置可用时段，怎样改变协调成本分配，什么约束仍会使预约失败？
expected_output: 一条双边任务链与可用时间为空的反例
out_of_scope: 不编造内部实验、未公开用户数或历史版本，不将发布方解释当独立测量。
reason: 采用已读官方帮助快照，取消未核2013初版全部行为。
admission: eligible
admission_reason: 单一产品节点、两项背景与两项证据及直接支持的交付/观察结果已核对；准入不等于ready。
research:
  id: PRO-096
  status: sourced
  reason: 采用已读官方帮助快照，取消未核2013初版全部行为。
  event: Calendly预约页2026快照：两边身份与协调摩擦
  cutoff: 2026-10-25读取的官方预约规则快照；不重建2013初版。
  initial_facts:
  - id: F1
    text: 预约方只需邮箱，无需创建Calendly账户或登录。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 组织者用可用时段及连接日历来避免重复预约。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 确认邮件中的链接允许预约方改期或取消，无需登录。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 日历冲突、可用性设置及关闭的event type仍可能让页面无可预约时段；免注册不能解决这些限制。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 官方帮助给出预约与改期规则；没有声称这一版本已在2013存在或独立测量过采用效果。
    source_ids:
    - S1
  interpretation: 产品交付或规则是可观察工件；对用户心理、采用与因果的解释属于待检验假说。
  unknowns:
  - 内部决策、完整行为数据及反事实未知，不作为本题必需输入。
  sources:
  - id: S1
    url: https://calendly.com/help/scheduling-faq
    publisher: Calendly
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手来源正文；只提取新范围所需事实，未把搜索摘要当作验证。
  phase2_conditions: 正式采用新问题；保留原候选和旧规划以便追溯。
```

## PRO-097

```yaml
id: PRO-097
decision: retain
scenario_title: Figma 2019-01-29 Organization 套餐与 Uber 全公司迁移
focus: evidence-selection
subdomain: b2b-adoption
main_question: Uber全公司迁移与90%设计使用，能证明预算批准了吗？
expected_output: 一个采购验证项；区分使用者与经济买家
out_of_scope: 不重复评论价值、多人光标或席位激励
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-097
  status: sourced
  reason: 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。
  event: Figma 2019-01-29 Organization 套餐与 Uber 全公司迁移
  cutoff: 2019-01-29 公布的 Organization 方案与 beta 客户反馈已知后，验证组织采购信号前
  initial_facts:
  - id: I1
    text: Organization 为首个 enterprise-grade 方案，包含统一账单、audit reports、团队权限和 SSO 等组织治理能力。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 公告列明 beta 合作企业包括 Uber、Volvo、Square；设计负责人反馈文件碎片化和跨品牌团队管理需求。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: Uber 参与者称 beta 后决定全公司迁移；公告称其 90% 产品设计工作已在 Figma 中完成。
    source_ids: *id001
    availability: pre_decision
  - id: E2
    text: 管理员可通过 SSO 移除离职者、限制组织外访问，并向承包商授予限定团队/项目权限。
    source_ids: *id001
    availability: pre_decision
  outcome:
    text: Organization 已发布并出现参与者叙述的全公司迁移；使用率与迁移不等于已独立确认的预算批准或采购合同。
    source_ids:
    - S1
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 具体经济买家、批准预算、合同价格及支付证明未知。
  - 客户证言经厂商挑选，不代表所有组织，也不能识别治理功能对采购的独立贡献。
  sources:
  - id: S1
    url: https://www.figma.com/blog/figma-organization/
    publisher: Figma / Dylan Field and quoted beta customers
    published_at: '2019-01-29'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 打开原 Organization 公告，核对 beta 客户、统一账单、访问控制与迁移叙述；排除网页新增的后来 Enterprise 提示。
  phase2_conditions:
  - 首轮把预算批准作为待验证项，不把使用者自述当预算持有人承诺。
  - 与 PRO-088 分开：只做组织采购与治理，不重复浏览器协作需求。
```

## PRO-098

```yaml
id: PRO-098
decision: reframe
scenario_title: Horizon Workrooms 2021 beta：VR与网页加入的任务差异
focus: hypothesis-diagnosis
subdomain: strategy-pivot
main_question: 白板协作未达预期时，哪项对照最能区分设备加入摩擦和任务本身价值不足？
expected_output: 两个竞争解释与一项控制设备条件的验证
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 回到一手材料完整的2021 beta，取消未核2024精简动机及失败因果。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-098
  status: sourced
  reason: 回到一手材料完整的2021 beta，取消未核2024精简动机及失败因果。
  event: Horizon Workrooms 2021 beta：VR与网页加入的任务差异
  cutoff: 2021-08-19 beta发布后，评估协作任务机制及待检验假说；不混入2024改动。
  initial_facts:
  - id: F1
    text: Meta 于 2021-08-19 发布 Quest 2 免费 Workrooms beta，允许 VR 与网页视频加入。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 原版提供白板、桌面/键盘追踪、屏幕共享；使用 VR 有设备及账号前提。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: Meta 把远程协作价值作为产品承诺，而非已测量收益。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: VR内可用白板、桌面/键盘追踪和屏幕分享，网页视频加入不等于获得全部VR交互。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: Meta实际发布Quest 2 Workrooms beta及网页视频加入；公告中的远程协作价值仍是承诺，未有对照收益。
    source_ids:
    - S1
  interpretation: 仅有公开自报/文档描述；不把发布、相关性或后来的成功当成因果结论。
  unknowns:
  - 官方 2024 release note、任务失败率、设备影响与价值影响的分离
  sources:
  - id: S1
    url: https://about.fb.com/news/2021/08/introducing-horizon-workrooms-remote-collaboration-reimagined/
    publisher: Meta
    published_at: '2021-08-19'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 阅读 Meta 发布正文和 UploadVR 更新报道；检索 Meta 2024 原始变更未得可核正文。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-099

```yaml
id: PRO-099
decision: retain
scenario_title: eBay 1999 年报记录的交易后 Feedback Forum 规则
focus: causal-modeling
subdomain: network-marketplaces
main_question: 只许交易伙伴评价且同一对账户最多影响一分，怎样改变陌生交易判断？
expected_output: 一条信誉机制及串谋/履约边界
out_of_scope: 不混入后续双向评价政策
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-099
  status: sourced
  reason: 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。
  event: eBay 1999 年报记录的交易后 Feedback Forum 规则
  cutoff: 2000 年 1999 年报公开后，一次选择陌生交易对手前；不混入 1996 或后来卖家禁负评规则
  initial_facts:
  - id: I1
    text: 买卖双方自行完成支付和交付；卖家可参考买家反馈决定付款方式及先款/先货。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 注册用户有反馈档案和净评分；该版限制为已完成交易伙伴留反馈，同一对账户对净分最多影响一分。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 公司禁止自有其他账户刷正评或多账户重复负评，足够负面的评分会导致暂停交易资格。
    source_ids: *id001
    availability: pre_decision
  - id: E2
    text: 年报称反馈降低陌生交易的匿名性和不确定性；这是公司机制解释，没有独立完成率实验。
    source_ids: *id001
    availability: pre_decision
  outcome:
    text: 该版公开规则把可见信誉与交易资格相连；不代表信誉保证付款履约或完全防止串谋。
    source_ids:
    - S1
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 精确规则切换日期未在年报本段给出；本题锚定年报中的已生效版本，不称其为 1996 初版。
  - 评分对完成率的独立因果增量未知。
  sources:
  - id: S1
    url: https://www.annualreports.com/HostedData/AnnualReportArchive/e/NASDAQ_EBAY_1999.pdf
    publisher: eBay annual report, mirrored by AnnualReports
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
  - 打开公司 1999 年报 PDF，核对 Feedback Forum、交易履约和反滥用段落。
  - 另读 eBay 1996 founder letter 与历史 feedback FAQ；其非交易评价规则不同，不与年报版合并。
  phase2_conditions:
  - 只讨论一个早期已生效规则版本；后续买卖权限变化不得混入。
  - 不把公司“降低不确定性”归因升级为实测完成率提高。
```

## PRO-100

```yaml
id: PRO-100
decision: reframe
scenario_title: Shopify 2009 App Store首发：BaseSync扩展边界
focus: boundary-transfer
subdomain: retention-workflow
main_question: 商品同步需求由外部BaseSync满足，怎样改变核心产品与扩展的责任边界，什么时候应停止外推？
expected_output: 一条需求—扩展—依赖关系及不能假定的权限边界
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 只讨论首发可核产品边界，不再要求未取得的2009完整数据权限或退出合同。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-100
  status: sourced
  reason: 只讨论首发可核产品边界，不再要求未取得的2009完整数据权限或退出合同。
  event: Shopify 2009 App Store首发：BaseSync扩展边界
  cutoff: 2009-06-02 首发后、商家选择 BaseSync 外部扩展前
  initial_facts:
  - id: I1
    text: 首发清单列有 BaseSync，把商店商品同步到 Google Base；这是具体插件任务而非泛生态规模。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 首发宣布 app 可由开发者创建并出售，Shopify 管理 App Store 交易并向商家宣传新 app。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告解释用按需安装功能避免核心店铺软件过度臃肿；此为平台设计动机，未提供留存实验。
    source_ids: *id001
    availability: pre_decision
  - id: E2
    text: 首发还列出发票打印、评论和数字商品等 app，支持 API/App Store 实际发布的身份。
    source_ids: *id001
    availability: pre_decision
  outcome:
    text: Shopify实际首发API/App Store并列BaseSync商品同步功能；公告不证明留存因果或完整数据权利。
    source_ids:
    - S1
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 未取得 2009 BaseSync 的数据授权范围、撤销权限、数据可迁出条件和实际收费协议。
  - 不能用当前 OAuth scopes/partner revenue share 倒推首发版。
  sources:
  - id: S1
    url: https://www.shopify.com/news/shopify-launches-api-platform-and-app-store
    publisher: Shopify
    published_at: '2009-06-02'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 打开 2009 原始发布稿，核对 API beta、具体首发 app、交易管理与分发约定。
  - 检索首发 app 历史，当前开发文档不能闭合 2009 插件数据/权限条件。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-101

```yaml
id: PRO-101
decision: reframe
scenario_title: Canva Education 2019 beta：教师中介的采用
focus: prediction-counterfactual
subdomain: distribution-growth
main_question: 课堂中由教师布置和评阅作品，能在什么条件下转为学生独立使用，哪项学校情境会让预测失效？
expected_output: 一个跨情境预测及失效条件
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 保留2019免费beta实际课堂流程；明确预测而非要求已测量毕业后转化。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-101
  status: sourced
  reason: 保留2019免费beta实际课堂流程；明确预测而非要求已测量毕业后转化。
  event: Canva Education 2019 beta：教师中介的采用
  cutoff: 2019 beta 发布后，教师决定是否采用课堂作品任务前；原媒体 PDF 精确日未知
  initial_facts:
  - id: I1
    text: 教育 beta 为澳大利亚学校推出的免费产品，提供教师/学生共享工作空间、课堂模板和素材。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 公告列有 GSuite/Google Classroom 集成及学生向教师分享作品以评阅打分的流程。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 媒体包确认 beta 已推出并提供海报、worksheet、report 等任务模板；不是只宣布未来教育愿景。
    source_ids: *id001
    availability: pre_decision
  - id: E2
    text: 公司十周年时间线把 Education 上线归入 2019，可交叉确认年份，但属于 2023 回顾。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 官方媒体包确认免费Education beta课堂模板、共享和评阅流程；没有证明毕业后的独立留存。
    source_ids:
    - S1
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 学生离开学校后的身份迁移、设计资产保留与独立用途 cohort 未取得。
  - 学校/学生规模不能乘套餐价格当未来商业收入。
  sources:
  - id: S1
    url: https://static-cse.canva.com/blob/148194/Canva-for-Education.pdf
    publisher: Canva
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - outcome
  - id: S2
    url: https://www.canva.com/newsroom/news/canva-10-year-timeline/
    publisher: Canva
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
  attempts:
  - 打开四页官方教育媒体包，核对 Australian beta、免费内容、Classroom 集成及评阅流程。
  - 打开官方十年时间线核对 2019 年份；未以当前教育资格和产品条件回填初版。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-102

```yaml
id: PRO-102
decision: retain
scenario_title: Dropbox 2008-09-11 公测上线的桌面文件夹同步
focus: causal-modeling
subdomain: ux-activation
main_question: 熟悉的本地文件夹怎样把云端同步变成用户已有的任务路径？
expected_output: 一条任务机制及多功能定位混淆的反例
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-102
  status: sourced
  reason: 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。
  event: Dropbox 2008-09-11 公测上线的桌面文件夹同步
  cutoff: 2008-09-11 公开上线前，已有 beta 与桌面客户端；精确内部设计决定日期未知
  initial_facts:
  - id: I1
    text: 创始人描述目标需求为忘带 USB、给自己发邮件和难以远程访问文件，而非抽象云存储容量。
    source_ids:
    - S2
    availability: pre_decision
  - id: I2
    text: 产品已在 beta 中供人试用，准备在 Mac/Windows 外提供功能相同的 Linux 客户端。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 2008-09-11 公司宣布所有人可用，Linux 客户端同期发布，另有 iPhone 优化网页访问。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 创始人回顾将交互比作自动处理文件的 magic folder，并承认初期把备份/同步/分享都堆在定位中使人困惑。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 产品实际公开交付跨桌面客户端的文件访问与同步；熟悉文件夹降低任务解释成本是可检验机制，尚非因果实验结论。
    source_ids:
    - S1
    - S2
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 本次未取得冻结的 2008 逐屏演示和首次成功同步率；不能把后来的 onboarding 指标回填。
  - 同期 iPhone 是优化网页，不是后来原生 iOS app。
  sources:
  - id: S1
    url: https://blog.dropbox.com/topics/company/dropbox-launches-to-the-public
    publisher: Dropbox / Drew Houston
    published_at: '2008-09-11'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I2
    - E1
    - outcome
  - id: S2
    url: https://mixergy.com/interviews/drew-houston-dropbox-interview/
    publisher: Drew Houston interview / Mixergy
    published_at: '2011-12-21'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - E2
    - outcome
  attempts:
  - 打开同期公开上线稿及创始人完整访谈，核对客户端、平台和 magic-folder 叙述时点。
  phase2_conditions:
  - 锚定文件夹同步的激活机制，不复用邀请码传播或自建存储成本。
  - 首轮不提供后来的等待名单或规模成果作为同步交互有效性的证明。
```

## PRO-103

```yaml
id: PRO-103
decision: reframe
scenario_title: Jira Cloud 2020免费档：十人边界与团队增长
focus: prediction-counterfactual
subdomain: pricing-monetization
main_question: 十人以内永久免费会怎样改变新团队采用；需求或人数超过边界时，哪种条件使采用预测反转？
expected_output: 一个条件预测及增长后付费/替代的边界
out_of_scope: 不推定未披露用户实验、留存因果、合同或完整历史版本；不把功能交付等同商业成功。
reason: 只使用2020-03-18公告明确的免费人数及长期供给，不要求未核迁移细则或价格精算。
admission: eligible
admission_reason: 复用已读来源并正式修订为材料可支撑的单题范围；缺失的内部数据不再是完成题目的必要输入。
research:
  id: PRO-103
  status: sourced
  reason: 只使用2020-03-18公告明确的免费人数及长期供给，不要求未核迁移细则或价格精算。
  event: Jira Cloud 2020免费档：十人边界与团队增长
  cutoff: 2020-03-18 公告后、小团队选择 Free 或升级前
  initial_facts:
  - id: I1
    text: 公告称 Jira Software 等 flagship Cloud 产品向至多十人的团队免费，并声明不是限时优惠。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 选用 Cloud 与当时远程协作场景相连，但公告没有记录该小团队的未来人数增长。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 当前 licensing 页保留 2020-09-21 停售新 Cloud Starter 许可的历史说明，同时列有现行免费功能边界；二者不可自动合成 3 月首发套餐。
    source_ids:
    - S2
    availability: unknown
  - id: E2
    text: 3 月公告确认免费版实际可访问，未提供该次全部功能限制、已有付费团队迁移与超额处理规则。
    source_ids: *id001
    availability: pre_decision
  outcome:
    text: 3月18日官方宣布至多十人免费且非限时优惠；本题不混入9月或当前版本的功能、迁移细则。
    source_ids:
    - S1
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 2020-03-18 Free 的完整存储、权限、支持与迁移限制未取得冻结版。
  - 不能把 2019 局部 rollout、2020 3 月 GA、9 月停售 Starter 与当前规则揉成一次发布。
  sources:
  - id: S1
    url: https://www.atlassian.com/blog/company-news/atlassian-cloud-remote-friendly-tools-free-small-teams
    publisher: Atlassian / Scott Farquhar
    published_at: '2020-03-18'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E2
    - outcome
  - id: S2
    url: https://www.atlassian.com/licensing/cloud
    publisher: Atlassian
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E1
  attempts:
  - 打开 2020 发布公告和 licensing 页面，核对发布日期与历史 Starter 说明。
  - 检索同期 Free 人数/功能限制；当前页面未证明当时全部套餐与迁移规则。
  - 本轮复用并阅读初轮逐项记录的一手来源内容；按新问题与公开材料时点核对，不宣称新发现内部实验。
  phase2_conditions: 正式使用本条新范围与认知动作，Phase2原题留作历史。
```

## PRO-104

```yaml
id: PRO-104
decision: retain
scenario_title: Canva 2013-08-26 首次限量推出在线拖拽设计平台
focus: hypothesis-diagnosis
subdomain: user-research-value
main_question: 在非设计师完成一张海报的任务中，怎样区分素材寻找与排版操作两个价值假说？
expected_output: 两个任务假说；不声称已识别组件最大贡献
out_of_scope: 不以发布、用户总量或事后成功代替因果证据
reason: 复核原直接来源素材；保留原节点与单一认知动作。
admission: eligible
admission_reason: 原研究已逐条核对直接来源；事实、证据及实际交付/观察结局齐全，问题只要求来源能支持的判断；尚非ready。
research:
  id: PRO-104
  status: sourced
  reason: 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。
  event: Canva 2013-08-26 首次限量推出在线拖拽设计平台
  cutoff: 2013-08-26 公开推出前，决定非设计师任务的产品组合；内部决定日期未知
  initial_facts:
  - id: I1
    text: 产品面向没有传统桌面设计工具经验的人，组合浏览器拖拽、集成素材搜索和可用设计元素。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 基本设计免费，可上传自己的内容，发布设计时按 premium element 收取 1 美元；不是订阅套餐。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 发布稿宣布从当日面向美国、澳大利亚有限用户 rollout，并接受等待名单报名。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 文中列出素材、字体、布局及与客户协作的能力；没有模板、素材、编辑器三项的独立实验比较。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 在线设计平台实际限量发布；可据任务分析各组成部分价值，但不能声称模板已被实验证明是唯一或最大贡献。
    source_ids:
    - S1
  interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
  unknowns:
  - 早期用户任务观察、完成时间和不同组件对成功率的独立作用未知。
  - 首发布局不是后来完整 Canva 模板、AI 或品牌工具集合。
  sources:
  - id: S1
    url: https://www.prweb.com/releases/canva_makes_graphic_design_amazingly_simple_for_everyone/prweb11055904.htm
    publisher: Canva via PRWeb
    published_at: '2013-08-26'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 打开同期公司发布稿，核对限量推出、免费/单元素付费、集成素材与拖拽功能；另读公司时间线但未前置后期成果。
  phase2_conditions:
  - 只比较 2013 非设计师的单类任务；观察/合成使用任务必须显式分开。
  - 不以融资金额或后来用户规模代替组件价值证据。
```
