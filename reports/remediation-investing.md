# Phase 3 创投题准入修订

这是逐题素材与范围准入，不是完整Brief。pending不得推定可制作。保留日期与ID，所有改题有映射。

## INV-001

```yaml
id: INV-001
decision: reframe
scenario_title: Arm 2023 IPO：公开价格区间与基本股本
focus: quantitative-calibration
subdomain: valuation-terms
main_question: 47—51美元区间与已披露基本股数对应怎样的价值范围，为什么不能直接当完全稀释内在价值？
expected_output: 一项条件性基本市值比较及业务/股本限制
out_of_scope: 限定已披露基本股数和价格区间的条件性比较；不当作完全稀释市值、最终发行价预测或内在价值。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-001
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Arm 2023 IPO：公开价格区间与基本股本
  cutoff: 2023-09-05 路演公告之后、9 月 13 日最终定价公告之前；最终价不得开场给出。
  initial_facts:
  - id: F1
    text: 业务收入区分授权及其他收入与版税收入。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 路演给出每 ADS 47 至 51 美元区间，出售方是 SoftBank 全资主体。
    source_ids:
    - S2
    availability: pre_decision
  evidence:
  - id: E1
    text: F-1 披露截至 2023 年 6 月的已发行普通股为 1025234000 股，估值时须区分股本与出售数量。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: F-1 对 2023 年 6 月季度的版税收入减少与授权收入变化分别说明。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 9 月 13 日公告最终每 ADS 定价 51 美元，初始出售 9550 万 ADS。
    source_ids:
    - S3
  interpretation: 发行价是定价事实，不证明内在价值或事前决策最优。
  unknowns:
  - 未来增长、折现率与个人可获得的分配价格不能由发行公告确定。
  sources:
  - id: S1
    url: https://investors.arm.com/static-files/7c8dbdc5-414a-4092-8ca3-69858726618e
    publisher: Arm
    published_at: '2023-08-21'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - E1
    - E2
  - id: S2
    url: https://newsroom.arm.com/news/arm-announces-launch-of-ipo-roadshow
    publisher: Arm
    published_at: '2023-09-05'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F2
  - id: S3
    url: https://newsroom.arm.com/news/arm-announces-pricing-of-initial-public-offering
    publisher: Arm
    published_at: '2023-09-13'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - outcome
  attempts:
  - 官方 HTML 大文档读取失败，改用已打开的官方 PDF；另读取路演及定价正文。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
quantitative_inputs:
- name: preliminary_price_low
  value: 47
  unit: USD per ADS
  source_ids:
  - S2
- name: preliminary_price_high
  value: 51
  unit: USD per ADS
  source_ids:
  - S2
- name: basic_ordinary_shares
  value: 1025234000
  unit: shares, not fully diluted
  source_ids:
  - S1
```

## INV-002

```yaml
id: INV-002
decision: reframe
scenario_title: Instacart 2023年报：净额收入与毛利边界
focus: quantitative-calibration
subdomain: unit-economics
main_question: 交易与广告收入合计能复算多少毛利；为什么不能据此分配两项业务各自的履约利润？
expected_output: 一项合并毛利复算与净额列报、成本归属的边界
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 改用实际读到的2023年报，取消缺少成本分摊的上市前分部估值。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-002
  status: sourced
  reason: 改用实际读到的2023年报，取消缺少成本分摊的上市前分部估值。
  event: Instacart 2023年报：净额收入与毛利边界
  cutoff: 2024-03-05年报公开后评估已披露经营质量，不模拟2023IPO前获得未来报表。
  initial_facts:
  - id: F1
    text: 年报将收入分为交易收入和广告及其他收入。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 交易收入在支付商品款及shopper报酬后净额列报；并非消费者订单总额。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 2023交易收入2171、广告及其他871、收入成本764，单位均为百万美元。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 报表给出的合并毛利2278；收入成本还有支付处理、保险等，不能把广告收入全算成广告利润。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 年报实际披露3042收入和2278毛利；这是公司合并会计结果，不是各业务独立利润。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1579091/000157909124000027/cart-20231231.htm
    publisher: Maplebear / SEC
    published_at: '2024-03-05'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手材料；本轮按修改后的单一问题核对，不以搜索摘要补事实。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
quantitative_inputs:
- name: transaction_revenue
  value: 2171
  unit: USD million
  source_ids:
  - S1
- name: advertising_other
  value: 871
  unit: USD million
  source_ids:
  - S1
- name: cost_of_revenue
  value: 764
  unit: USD million
  source_ids:
  - S1
```

## INV-003

```yaml
id: INV-003
decision: reframe
scenario_title: Fiverr 2011投资备忘录：交易热度与重复需求
focus: evidence-selection
subdomain: pmf-traction
main_question: 六万笔月交易和自然增长已知时，下一项重复交易证据应怎样检验需求质量？
expected_output: 一个分群证据选择及反证条件
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-003
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Fiverr 2011投资备忘录：交易热度与重复需求
  cutoff: 2011-01-10 投资建议窗口，以投资方当时记录为限。
  initial_facts:
  - id: F1
    text: Fiverr 为低价服务交易市场，投资备忘录讨论早期消费互联网机会。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 投资者将低现金消耗与有时间继续试验视为判断条件。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 备忘录把自然增长和客户满意度列为投资论据，这属于投资者评估。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 备忘录记载2010年12月每月约六万笔5美元交易、没有营销支出；不能由交易数推出独立客户留存。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 原始文件提出投资建议；不能据此确认实际交割价格或实现回报。
    source_ids:
    - S1
  interpretation: 低 burn 提供验证时间，是备忘录的论点，不等同于重复交易质量已被证明。
  unknowns:
  - 原候选所称 Series A 的交割细节；可公开复用的完整 cohort 数字。
  sources:
  - id: S1
    url: https://www.bvp.com/memos/fiverr
    publisher: Bessemer Venture Partners
    published_at: '2011-01-10'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 打开 BVP 原始备忘录及公司转载新闻；不以转载当原始轮次合同。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  - 本轮重新打开Fiverr memo Overview及Service段，核对六万笔/月与未营销的披露。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-004

```yaml
id: INV-004
decision: reframe
scenario_title: Shopify 2010投资备忘录：SMB自助模式的扩展边界
focus: evidence-selection
subdomain: market-timing
main_question: 信用卡自助和无需长期合同的现金效率，可以外推到哪类客户采购条件？
expected_output: 一项自助增长机制及企业采购反例
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-004
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Shopify 2010投资备忘录：SMB自助模式的扩展边界
  cutoff: '2010-10-12'
  initial_facts:
  - id: F1
    text: 备忘录描述面向 SMB 的信用卡自助 SaaS，通常无需长期合同。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 备忘录列出近万客户与每月 43.8 万美元 MRR，属于投资者当时材料。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 备忘录记录此前融资少、账上现金且无债，不能把 GMV 当公司收入。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 文中把 SMB 市场规模与营销扩张列为需判断的机会或风险。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 文件建议按 2000 万美元投前估值投入 500 万并取得约 20% 完全稀释持股；这是建议条款而非实现收益。
    source_ids:
    - S1
  interpretation: 网页的当代回顾引用与原 memo 正文应分层，不将后来的 Shopify 成功前置。
  unknowns:
  - 独立核验的长期投资收益；原始客户级 cohort。
  sources:
  - id: S1
    url: https://www.bvp.com/memos/shopify
    publisher: Bessemer Venture Partners
    published_at: '2010-10-12'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 打开 BVP 原始 memo 正文并区分回顾引语。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-005

```yaml
id: INV-005
decision: reframe
scenario_title: Yelp 2005首次风险融资备忘录：评论供给与发现路径
focus: boundary-transfer
subdomain: moat-competition
main_question: 本地核心贡献者和搜索发现两种路径，怎样区分评论网络的可复制边界？
expected_output: 一项可迁移机制与不成立的网络效应推断
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-005
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Yelp 2005首次风险融资备忘录：评论供给与发现路径
  cutoff: '2005-10-03'
  initial_facts:
  - id: F1
    text: 备忘录记载此前有 100 万美元天使融资，称本轮为首次 venture financing。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 产品允许查看商家评论及通过好友取得可信建议。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 文中将少量高贡献者与本地社区感列为增长解释，不是经对照试验证实的因果。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 搜索引擎流量与朋友网络是不同发现路径，不能把流量都归给网络外部性。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 原文件提出 1300 万美元投前、500 万美元投资机会，并称已同意 term sheet 条件；未提供已实现回报。
    source_ids:
    - S1
  interpretation: 评论质量和可复制目录是合理竞争解释，作者的忠诚用户判断须标为当时评价。
  unknowns:
  - 独立交割证明与后续投资收益；评论网络的净因果作用。
  sources:
  - id: S1
    url: https://www.bvp.com/memos/yelp
    publisher: Bessemer Venture Partners
    published_at: '2005-10-03'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 打开原始备忘录的 Summary、Product 与条款段落。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-006

```yaml
id: INV-006
decision: reframe
scenario_title: Tesla 2010披露：2008借款与后续转换条件
focus: prediction-counterfactual
subdomain: funding-survival-exit
main_question: 2008年12月借款的到账与未来融资价格挂钩转换，分别解决和留下什么风险？
expected_output: 一个现金到账—未来定价—稀释风险的条件链
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 采用已读S-1披露的借款身份；不要求未公开2008现金跑道。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-006
  status: sourced
  reason: 采用已读S-1披露的借款身份；不要求未公开2008现金跑道。
  event: Tesla 2010披露：2008借款与后续转换条件
  cutoff: 2010-01-29 S-1已公开后的条款风险评估；不是复演2008年12月融资前选择。
  initial_facts:
  - id: F1
    text: 2010 S-1回溯单列2008年12月融资。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 该笔借款收到1450万美元，不能把2009新增借款算作2008可用现金。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 转换安排与此后融资价格的一定比例挂钩。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 另有2009追加借款及后续股权融资，时间、现金和转换不能合成一笔。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: S-1记载借款及后续转换过程，未证明每位投资人事前掌握完整现金资料。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://ir.tesla.com/_flysystem/s3/sec/000119312510017054/ds1-gen_0.pdf
    publisher: Tesla
    published_at: '2010-01-29'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-007

```yaml
id: INV-007
decision: reframe
scenario_title: Theranos 2013：渠道背书与技术验证
focus: evidence-selection
subdomain: founder-execution
main_question: Walgreens合作公告能验证什么，哪项独立技术证据缺失应阻止把渠道背书当成技术成功？
expected_output: 一条可核验的技术尽调门槛及背书的证明边界
out_of_scope: 不把后来调查事实提前交给投资者
reason: 用2013同期合作公告建立事前信息；2018 SEC指控只作事后材料。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-007
  status: sourced
  reason: 用2013同期合作公告建立事前信息；2018 SEC指控只作事后材料。
  event: Theranos 2013：渠道背书与技术验证
  cutoff: 2013-09-09合作公告公开后，独立技术尽调前。
  initial_facts:
  - id: F1
    text: 2013-09-09两家公司宣布长期合作，首个Palo Alto服务点计划当月开放。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 全国扩张是计划；少量血样可完成广泛检测是合作方宣传主张，尚非独立验证。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 渠道、门店覆盖与合作身份本身不披露测试方法或独立准确性比较。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 2018 SEC指控融资陈述涉及技术、业务与财务误导；这是监管指控，不能倒灌成2013投资人已知。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 2018 SEC宣布欺诈指控及公司与Holmes同意和解；不把该公告称为全部事实的审判认定。
    source_ids:
    - S2
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://corporate.walgreens.com/news-and-stories/press-releases/2013/theranos-selects-walgreens-as-a-long-term-partner-through-which-to-offer-its-new-clinical-laboratory-service/
    publisher: Walgreens / Theranos
    published_at: '2013-09-09'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
  - id: S2
    url: https://www.sec.gov/newsroom/press-releases/2018-41
    publisher: US SEC
    published_at: '2018-03-14'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手材料；本轮按修改后的单一问题核对，不以搜索摘要补事实。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-008

```yaml
id: INV-008
decision: reframe
scenario_title: Coinbase 2021披露：周期盈利与固定费用风险
focus: hypothesis-diagnosis
subdomain: valuation-terms
main_question: 2020盈利能否视作正常化盈利，哪项周期和费用证据会改变判断？
expected_output: 一项有来源的竞争解释与可验证条件
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-008
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Coinbase 2021披露：周期盈利与固定费用风险
  cutoff: 2021 年 S-1 公开之后、直接上市之前；不采用上市后价格。
  initial_facts:
  - id: F1
    text: 公司交易费是主要净收入来源，2020 交易收入占净收入逾 96%。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 2020 总收入约 13 亿美元、净利约 3.223 亿美元，2019 为净亏损。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: S-1 明示增长随加密资产价格周期呈波浪变化。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 公司表示费用大体独立于净收入，因此交易活动下降时可能再次亏损。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 已公开的 2019 与 2020 财务呈现亏损到盈利的变化，并非已观察到未来永久利润水平。
    source_ids:
    - S1
  interpretation: 周期解释是公司披露且可讨论的机制，不等同于精确价格预测。
  unknowns:
  - 未来周期；个人可获得的进入价格；长期正常化利润。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1679788/000162828021003168/coinbaseglobalincs-1.htm
    publisher: Coinbase via SEC
    published_at: '2021-02-25'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 完整打开 S-1 并阅读周期、收入与费用段落。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-009

```yaml
id: INV-009
decision: reframe
scenario_title: Lyft 2019招股披露：贡献率与经营盈利
focus: quantitative-calibration
subdomain: unit-economics
main_question: 贡献率从23.9%到42.7%改善多少；为什么它不等于经营盈利或密度的独立因果效应？
expected_output: 百分点复算与贡献口径到盈利结论的边界
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 正式收窄为已披露贡献率，不要求城市补贴或同cohort成本。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-009
  status: sourced
  reason: 正式收窄为已披露贡献率，不要求城市补贴或同cohort成本。
  event: Lyft 2019招股披露：贡献率与经营盈利
  cutoff: 2019-03-18披露后、定价前，评估公开会计口径。
  initial_facts:
  - id: F1
    text: 2019-03-18招股书列2016—2018贡献率。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Contribution排除部分会计项目，不是EBITDA或净利润。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 2016贡献率23.9%，2018为42.7%。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 2018调整后EBITDA仍为负943.5百万美元；两指标不能互换。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 披露贡献率改善与调整后EBITDA亏损并存；不能由公司平均值识别密度贡献。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://investor.lyft.com/financials/sec-filings/content/0001193125-19-077391/d633517ds1a.htm
    publisher: Lyft / SEC
    published_at: '2019-03-18'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
quantitative_inputs:
- name: 2016_contribution_margin
  value: 23.9
  unit: percent
  source_ids:
  - S1
- name: 2018_contribution_margin
  value: 42.7
  unit: percent
  source_ids:
  - S1
- name: 2018_adjusted_EBITDA
  value: -943.5
  unit: USD million
  source_ids:
  - S1
```

## INV-010

```yaml
id: INV-010
decision: reframe
scenario_title: Figma 2015 Preview：产品交付与融资叙事
focus: evidence-selection
subdomain: pmf-traction
main_question: 浏览器设计Preview已交付而多人编辑仍在路线图，哪项团队验证最值得投资人先做？
expected_output: 一个已交付/待验证边界及下一项团队工作流验证
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 改正2016轮次标签，采用2015同期Preview；不把累计1800万当单轮融资或把未来功能算成交付。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-010
  status: sourced
  reason: 改正2016轮次标签，采用2015同期Preview；不把累计1800万当单轮融资或把未来功能算成交付。
  event: Figma 2015 Preview：产品交付与融资叙事
  cutoff: 2015-12-03 Preview发布后、多人编辑交付前。
  initial_facts:
  - id: F1
    text: 2015-12-03宣布浏览器设计工具Preview。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 同期可通过链接分享和评论；多人协作列为之后计划。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告提到累计融资1800万美元，不证明某一轮单独1800万。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 多人功能仍待未来推出，现有可访问性不证明团队已愿意付费采购。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公司发布Preview；此时不能把之后多人编辑成功当作投资已验证。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://www.figma.com/blog/design-meet-the-internet/
    publisher: Figma / Dylan Field
    published_at: '2015-12-03'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-011

```yaml
id: INV-011
decision: reframe
scenario_title: SpaceX 2009采购披露：合同额与技术里程碑
focus: constrained-decision
subdomain: market-timing
main_question: 12次发射16亿美元的合同，能否作为当下可用现金或轨道运输已验证的证明？
expected_output: 合同、现金与工程验证三个节点的资本承诺门槛
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 用FAA真实合同与测试披露替代未公开的2008剩余现金决策。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-011
  status: sourced
  reason: 用FAA真实合同与测试披露替代未公开的2008剩余现金决策。
  event: SpaceX 2009采购披露：合同额与技术里程碑
  cutoff: 2009一季度报告可取得后，对已披露合同与技术证据作资本里程碑评估；不复演2008年合同前的私募选择。
  initial_facts:
  - id: F1
    text: FAA 2009一季度报告记载NASA于2008-12-23授予商业补给合同。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: SpaceX合同为12次发射16亿美元，有效期至2016年。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 报告另记载2008-11-22九发动机约三分钟静态点火。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 合同采购与地面点火是不同证据：报告未给按期到账现金，也未将静态点火说成轨道补给交付。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: NASA实际授予SpaceX及Orbital采购合同；授予不等于全部收入或现金已实现。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://www.faa.gov/about/office_org/headquarters_offices/ast/media/Quarterly%20Launch%20Report%201st%20Quarter%202009.pdf
    publisher: FAA Office of Commercial Space Transportation
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
  - 实际打开并阅读所列一手材料；本轮按修改后的单一问题核对，不以搜索摘要补事实。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-012

```yaml
id: INV-012
decision: reframe
scenario_title: SendGrid 2011投资备忘录：体验与投递能力的壁垒
focus: boundary-transfer
subdomain: moat-competition
main_question: 客户说易集成、支持好时，哪些优势可复制，哪项投递证据才能改变壁垒判断？
expected_output: 一个壁垒成立条件及反证
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-012
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: SendGrid 2011投资备忘录：体验与投递能力的壁垒
  cutoff: 2011-12-16 备忘录形成时
  initial_facts:
  - id: F1
    text: SendGrid 提供托管邮件基础设施接口。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 备忘录拟投 1320 万美元；包含老股流动性安排，不应全部当新增经营现金。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 客户访问记录强调集成简易、支持以及不必自建邮件能力。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 备忘录将 ExactTarget 等列为实际竞争，不能把当时的体验优势直接等同永久信誉壁垒。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 已观察到的决策材料是提交投资建议；不能仅由此证明交割或未来回报。
    source_ids:
    - S1
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 客户访问是投资人选取样本；信誉形成成本的完整账本未知。
  sources:
  - id: S1
    url: https://www.bvp.com/memos/sendgrid
    publisher: Bessemer Venture Partners
    published_at: '2011-12-16'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-013

```yaml
id: INV-013
decision: reframe
scenario_title: Airbnb 2009年初：经营试验与生存目标
focus: constrained-decision
subdomain: funding-survival-exit
main_question: 现金目标明确而增长尚不稳定时，怎样选择下一项经营试验并限制融资依赖？
expected_output: 一项行动选择与改变选择的信号
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-013
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Airbnb 2009年初：经营试验与生存目标
  cutoff: 2009 年初 YC 期间，在首次纽约经营试验之前（精确日未知）
  initial_facts:
  - id: F1
    text: 创始人此前依靠信用卡负债维持经营。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 当时目标是每月约 4000 美元，以覆盖约 3500 房租和 500 食物。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 团队从搜索需求发现纽约的重要性并亲自到访房东、改进照片。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 早期需求集中在特定地点，不支持不加验证地全面扩张。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: Graham 回忆 2009-02-22 收到 ramen profitable 邮件；2 月前三周费用收入逐步增加。
    source_ids:
    - S1
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 回顾有选择偏差；无法单独识别照片、拜访与其他变化的因果贡献；融资条款未知。
  sources:
  - id: S1
    url: https://www.ycombinator.com/blog/the-airbnbs/
    publisher: Y Combinator / Paul Graham
    published_at: '2020-12-10'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
    narrative_limit: 2020 年直接参与者回顾，非同期公开信息；早期资金目标是团队内部已知信息。
  attempts:
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-014

```yaml
id: INV-014
decision: reframe
scenario_title: Box 2014融资：董事席位与未披露权利
focus: evidence-selection
subdomain: valuation-terms
main_question: 公告给出的融资与董事变动，足以判断旧股经济风险吗；应优先取得哪项合同证据？
expected_output: 一个最重要合同验证及控制权/经济权利的边界
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 采用证据选择备用题，取消没有合同支持的旧股稀释预测。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-014
  status: sourced
  reason: 采用证据选择备用题，取消没有合同支持的旧股稀释预测。
  event: Box 2014融资：董事席位与未披露权利
  cutoff: 2014-07-07公告后评估证据充分性，不假装公告给出全部合同。
  initial_facts:
  - id: F1
    text: 2014-07-07公告TPG Growth及Coatue投资1.5亿美元。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公告安排TPG董事加入。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告明确交易条款未披露。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 已宣布的董事安排不等于完整清算、转换或反稀释权利。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公司宣布新增投资与董事安排；没有公开完整交易条款。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://www.boxinvestorrelations.com/news-and-media/news/press-release-details/2014/Box-Announces-150-Million-Investment-from-TPG-Growth-and-Coatue/default.aspx
    publisher: Box
    published_at: '2014-07-07'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-015

```yaml
id: INV-015
decision: reframe
scenario_title: Uber 2019Q4：Gross Bookings、收入与ANR
focus: quantitative-calibration
subdomain: unit-economics
main_question: 同季GAAP收入和ANR分别占Gross Bookings多少，为什么两种比率都不是平台利润率？
expected_output: 两个同口径比率及不等于利润的成本边界
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 改用2020披露的2019Q4实际数值，不再要求IPO前城市密度或补贴数据。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-015
  status: sourced
  reason: 改用2020披露的2019Q4实际数值，不再要求IPO前城市密度或补贴数据。
  event: Uber 2019Q4：Gross Bookings、收入与ANR
  cutoff: 2020-02-06结果已公开后，比较2019Q4指标。
  initial_facts:
  - id: F1
    text: 公司2020-02-06披露2019Q4经营结果。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Gross Bookings、GAAP收入与Adjusted Net Revenue是三个不同口径。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 当季Gross Bookings18131、GAAP收入4069、ANR3730，均为百万美元。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 当季净亏损1096百万美元；收入或ANR相对Bookings的比率不是净利润率。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公司披露当季收入与ANR均为正但净亏损；不能从比率识别某城市是否盈利。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://investor.uber.com/news-events/news/press-release-details/2020/Uber-Announces-Results-for-Fourth-Quarter-and-Full-Year-2019/default.aspx
    publisher: Uber
    published_at: '2020-02-06'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手材料；本轮按修改后的单一问题核对，不以搜索摘要补事实。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
quantitative_inputs:
- name: gross_bookings
  value: 18131
  unit: USD million
  source_ids:
  - S1
- name: GAAP_revenue
  value: 4069
  unit: USD million
  source_ids:
  - S1
- name: ANR
  value: 3730
  unit: USD million
  source_ids:
  - S1
```

## INV-016

```yaml
id: INV-016
decision: reframe
scenario_title: Pinterest 2011已签term sheet：兴趣与商业意向
focus: evidence-selection
subdomain: pmf-traction
main_question: 收藏和跟随品味者的行为，哪项后续证据最能区别兴趣与商业需求？
expected_output: 一个分群验证与不可外推的付费判断
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-016
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Pinterest 2011已签term sheet：兴趣与商业意向
  cutoff: 2011-04-03 备忘录形成时
  initial_facts:
  - id: F1
    text: 产品允许收藏网页内容并关注他人整理的集合。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 前身 Totes 的社交分享行为为团队提供了产品方向线索。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 当时 iPhone 应用被描述为即将推出，不能当作成熟移动增长已经发生。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 备忘录描述用户跟随品味相近者的行为；尚不能推出明确商业购买意向。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 2011-04-03备忘录记录已签署领投1000万美元Series A、4000万美元投前并含13%未分配期权池的term sheet；非交割或实现收益证明。
    source_ids:
    - S1
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 可比较留存 cohort、支付意向和最终融资条款未核实。
  sources:
  - id: S1
    url: https://www.bvp.com/memos/pinterest
    publisher: Bessemer Venture Partners
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
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  - 本轮重新打开Pinterest memo并核对已签term sheet段；明确与最终交割分开。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-017

```yaml
id: INV-017
decision: reframe
scenario_title: Twilio 2009：小额种子延长与等待验证
focus: boundary-transfer
subdomain: market-timing
main_question: 应以小额延长融资等待大客户和新功能验证，还是立即承担完整A轮承诺？
expected_output: 一项分阶段承诺与验证门槛
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-017
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Twilio 2009：小额种子延长与等待验证
  cutoff: 2009-11-06 备忘录形成时
  initial_facts:
  - id: F1
    text: Twilio 提供类似 Web API 的语音通信能力。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司寻求后续 A 轮，而潜在投资者仍要求新功能和大客户的验证。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 此前种子轮约 80 万美元。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 备忘录建议追加 12.5 万美元，用延长融资为产品和商业验证争取时间。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 记录可确认的是追加投资建议；不将其等同确定完成的 A 轮或未来盈利。
    source_ids:
    - S1
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 实际剩余现金、后续 A 轮成交条款与样本外客户未知。
  sources:
  - id: S1
    url: https://www.bvp.com/memos/twilio
    publisher: Bessemer Venture Partners
    published_at: '2009-11-06'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-018

```yaml
id: INV-018
decision: reframe
scenario_title: Toast 2015投资备忘录：POS和支付绑定边界
focus: boundary-transfer
subdomain: moat-competition
main_question: 已上线模块与未来路线图分开后，POS/支付绑定在哪类餐厅工作流中才有切换成本？
expected_output: 一个切换成本条件与替代反例
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-018
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Toast 2015投资备忘录：POS和支付绑定边界
  cutoff: 2015-12-14 备忘录形成时
  initial_facts:
  - id: F1
    text: 备忘录描述 2400 万美元首轮机构融资。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 云 POS 结合支付和餐厅运营能力，但其中一些功能仍在路线图中。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 餐厅运行时的系统可用性直接影响经营，不是普通可有可无工具。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 应区分已上线的模块与未来规划，避免用五年路线图证明当时已经形成完整绑定。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: Bessemer 的记录建议投入 1750 万美元取得约 14.3% 完全稀释权益；这是投资建议口径。
    source_ids:
    - S1
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 客户迁移成本明细及失败迁移案例未知。
  sources:
  - id: S1
    url: https://www.bvp.com/memos/toast
    publisher: Bessemer Venture Partners
    published_at: '2015-12-14'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-019

```yaml
id: INV-019
decision: reframe
scenario_title: Stripe早期人工安装：2013当事人回顾
focus: evidence-selection
subdomain: founder-execution
main_question: 替意向客户当场安装能验证团队执行的哪一步，为什么仍不足以证明付费需求和金融运营能力？
expected_output: 一条意向—激活证据链及下一项运营验证
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 以Paul Graham当事人回顾为节点，不虚构2011种子轮条款或客户数据。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-019
  status: sourced
  reason: 以Paul Graham当事人回顾为节点，不虚构2011种子轮条款或客户数据。
  event: Stripe早期人工安装：2013当事人回顾
  cutoff: 2013-07回顾已公开后评价所述执行证据；不复演具体未核实的2011轮次。
  initial_facts:
  - id: F1
    text: Graham回顾Stripe创始人向YC同批初创公司招募试用。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 答应试用与完成安装是两个步骤。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 当对方同意时，创始人直接要来电脑当场安装。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 作者用这一行为解释早期人工推进；文章未给相应付费留存或金融合规审计。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 观察者记录实际人工安装行为；不能把观察者解释或文中假设增长算术当成Stripe实测。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://www.paulgraham.com/ds.html?viewfullsite=1
    publisher: Paul Graham
    published_at: 2013-07
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手材料；本轮按修改后的单一问题核对，不以搜索摘要补事实。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-020

```yaml
id: INV-020
decision: reframe
scenario_title: Nubank 2021定价：普通股与BDR换算
focus: quantitative-calibration
subdomain: valuation-terms
main_question: 一份BDR价格看起来低于一股美股，换汇及份额换算后是否代表更便宜？
expected_output: 一个同权益单位的价格换算与舍入边界
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 保留数量训练，改为发行方给出的BDR比率和币种，取消未核股本估值与客户风险成本。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-020
  status: sourced
  reason: 保留数量训练，改为发行方给出的BDR比率和币种，取消未核股本估值与客户风险成本。
  event: Nubank 2021定价：普通股与BDR换算
  cutoff: 2021-12-08定价公告后核对所代表权益；不预测随后市场价格。
  initial_facts:
  - id: F1
    text: 发行方2021-12-08宣布普通股定价9美元。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 每份BDR代表1/6普通股。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告BDR定价8.36雷亚尔，采用每美元5.579雷亚尔汇率。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 普通股与BDR的币种及权益份额不同；公布值有舍入，不能直接比较9与8.36。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 发行方宣布两地发行定价；公告中的预期交割日不是已完成交割。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://www.nasdaq.com/press-release/nu-holdings-ltd.-announces-pricing-of-initial-public-offering-2021-12-08
    publisher: Nu Holdings issuer release via Nasdaq
    published_at: '2021-12-08'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手材料；本轮按修改后的单一问题核对，不以搜索摘要补事实。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
quantitative_inputs:
- name: ordinary_price
  value: 9
  unit: USD per ordinary share
  source_ids:
  - S1
- name: BDR_price
  value: 8.36
  unit: BRL per BDR
  source_ids:
  - S1
- name: FX
  value: 5.579
  unit: BRL per USD
  source_ids:
  - S1
- name: BDR_denominator
  value: 6
  unit: BDRs per ordinary share
  source_ids:
  - S1
```

## INV-021

```yaml
id: INV-021
decision: reframe
scenario_title: Spotify 2018披露：平均毛利与新增订户
focus: quantitative-calibration
subdomain: unit-economics
main_question: Premium毛利率从15%到22%的改善如何表达；它对新增订户的边际版税证明了多少？
expected_output: 百分点及相对增幅复算，指出平均量到边际量的缺口
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 正式收窄为分部历史平均毛利，保留实数而不假设保密版税合同。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-021
  status: sourced
  reason: 正式收窄为分部历史平均毛利，保留实数而不假设保密版税合同。
  event: Spotify 2018披露：平均毛利与新增订户
  cutoff: 2018-02-28 F-1已公开后的平均与边际比较。
  initial_facts:
  - id: F1
    text: F-1公开2015—2017 Premium分部毛利率。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 分部平均毛利并非多一位客户的边际毛利。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: Premium毛利率2015为15%、2016为16%、2017为22%。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 公司将改善部分归于2017新授权协议；部分合同保密，不能唯一分离增量客户成本。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公司披露Premium平均毛利改善，不证明每个新增客户边际回报相同。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
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
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
quantitative_inputs:
- name: 2015_Premium_margin
  value: 15
  unit: percent
  source_ids:
  - S1
- name: 2017_Premium_margin
  value: 22
  unit: percent
  source_ids:
  - S1
```

## INV-022

```yaml
id: INV-022
decision: reframe
scenario_title: LinkedIn 2006投资备忘录：注册网络与企业购买
focus: evidence-selection
subdomain: pmf-traction
main_question: 注册人数与企业合同出现时，哪项证据更应决定继续商业化尽调？
expected_output: 一项尽调门槛及不能由用户量推出的结论
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-022
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: LinkedIn 2006投资备忘录：注册网络与企业购买
  cutoff: 2006-12-11 备忘录形成时
  initial_facts:
  - id: F1
    text: 备忘录记载约 800 万注册用户。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司接近收支平衡，月收入约 150 万美元。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 企业销售产品年合同额约 1 万至 15 万美元。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 建议投入 1250 万美元取得约 5% 完全稀释股权；拟议价格须与交易完成区分。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 已形成在约 2.375 亿美元投前口径下的投资建议；未核实最终交割和实现收益。
    source_ids:
    - S1
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 网络密度的独立效应及企业购买 cohort 未充分披露。
  sources:
  - id: S1
    url: https://www.bvp.com/memos/linkedin
    publisher: Bessemer Venture Partners
    published_at: '2006-12-11'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-023

```yaml
id: INV-023
decision: reframe
scenario_title: WeWork 2019救助公告：公司现金与老股流动性
focus: constrained-decision
subdomain: funding-survival-exit
main_question: 名义融资总额中，哪些部分支持公司经营，哪些只改变旧股流动性与控制安排？
expected_output: 一份现金/权益/控制的口径拆分
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-023
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: WeWork 2019救助公告：公司现金与老股流动性
  cutoff: 2019-10-22 公告后，后续执行前
  initial_facts:
  - id: F1
    text: 方案包括 50 亿美元新增融资。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 另有最高 30 亿美元老股 tender，以及加速先前承诺的 15 亿美元。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 老股转让所得不等同进入公司经营账户。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 公告预计 SoftBank 经济权益接近 80%，但无多数投票权，公司不成为其子公司；须区分经济权益与控制。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公告明确调整董事会和领导安排，Neumann 转为董事会观察员；这是宣布的安排，后续 tender 交割未在本来源确认。
    source_ids:
    - S1
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 各笔资金执行条件、实际到账时序与后续 tender 结果未在本来源确认。
  sources:
  - id: S1
    url: https://www.wework.com/ideas/newsroom-landing-page/wework-announces-significant-funding-from-softbank-group
    publisher: WeWork
    published_at: '2019-10-22'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-024

```yaml
id: INV-024
decision: reframe
scenario_title: Mistral 2023种子轮：技术经历与需求里程碑
focus: constrained-decision
subdomain: market-timing
main_question: 团队研究经历和种子资本已知时，应先验证哪项企业需求里程碑？
expected_output: 一个需求验证门槛和存活前提
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-024
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Mistral 2023种子轮：技术经历与需求里程碑
  cutoff: 2023-06-13 seed 公告后，模型发布前
  initial_facts:
  - id: F1
    text: 领投方宣布种子融资超过 1.05 亿欧元。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 创始团队来自 Meta 与 Alphabet 等研究经历，目标为开放模型。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 同期论点强调欧洲及开放模型机会，属于投资人判断，不是已经验证的客户需求。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 研究团队经历不能单独证明企业愿意付费或切换。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 2023-12-11 领投方后续公告记录 Mistral 7B、Mixtral 与 API 已发布及后续 A 轮；这不能提前用于 seed 判断，也不等于付费 PMF 已证实。
    source_ids:
    - S2
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 付费客户、资本实际消耗和可存活期限未知。
  sources:
  - id: S1
    url: https://lsvp.com/stories/meet-europes-next-great-generative-ai-startup-mistral-ai/
    publisher: Lightspeed Venture Partners
    published_at: '2023-06-13'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
  - id: S2
    url: https://lsvp.com/stories/building-with-mistral-why-we-doubled-down/
    publisher: Lightspeed Venture Partners
    published_at: '2023-12-11'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - outcome
  attempts:
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-025

```yaml
id: INV-025
decision: reframe
scenario_title: Datadog 2015 C轮：集成广度的可迁移边界
focus: boundary-transfer
subdomain: moat-competition
main_question: 接近百种集成与选取的客户证言已知时，什么条件才会把集成便利变成切换成本？
expected_output: 一个可复制部分与壁垒条件
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-025
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Datadog 2015 C轮：集成广度的可迁移边界
  cutoff: 2015-01-29 公司公告后
  initial_facts:
  - id: F1
    text: 公司宣布 3100 万美元 Series C，由现有投资人 Index 领投。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 当时将近 100 种技术的数据整合进统一监测界面。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: AdRoll CTO 描述跨服务器排障价值，是公司公告选取的客户证言。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 2014 已扩展多个云服务商支持；集成广度可证，独立迁移成本仍不能由此推出。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公司宣布融资用于工程、销售、营销和产品开发；未据此证明形成不可复制壁垒。
    source_ids:
    - S1
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 独立客户迁移试验、流失 cohort 与竞品替代成本未知。
  sources:
  - id: S1
    url: https://www.datadoghq.com/about/latest-news/press-releases/series-c/
    publisher: Datadog
    published_at: '2015-01-29'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-026

```yaml
id: INV-026
decision: reframe
scenario_title: Roblox 2021披露：bookings与收入倍数
focus: quantitative-calibration
subdomain: valuation-terms
main_question: 固定同一估值分子，把bookings当收入会使收入倍数偏差多少，差额是否是当期利润？
expected_output: bookings/收入比值与递延收入、现金流的边界
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 正式改为可复算的确认口径，取消未核股本与假设直接上市交易价格。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-026
  status: sourced
  reason: 正式改为可复算的确认口径，取消未核股本与假设直接上市交易价格。
  event: Roblox 2021披露：bookings与收入倍数
  cutoff: 2021-02-22 S-1/A公开后、直接上市前；只核对已公开报表。
  initial_facts:
  - id: F1
    text: 2021-02-22 S-1/A列明2020收入与bookings调节。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Bookings含收入、递延收入变动及其他调整，不能等同收入或利润。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 2020收入923885、递延收入增加965919、其他调整-7261、bookings1882543，单位千美元。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 同期经营现金流524340、自由现金流411220千美元，亦不是bookings或利润的同义词。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 申报文件调节至1882543千美元bookings；差额主要与确认时间有关，非当期利润增量。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://d18rn0p25nwr6d.cloudfront.net/CIK-0001315098/a327f07f-86d6-461c-a020-83cb4882d100.pdf
    publisher: Roblox / SEC issuer-hosted filing
    published_at: '2021-02-22'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手材料；本轮按修改后的单一问题核对，不以搜索摘要补事实。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
quantitative_inputs:
- name: revenue
  value: 923885
  unit: USD thousand
  source_ids:
  - S1
- name: deferred_revenue_change
  value: 965919
  unit: USD thousand
  source_ids:
  - S1
- name: other_adjustments
  value: -7261
  unit: USD thousand
  source_ids:
  - S1
- name: bookings
  value: 1882543
  unit: USD thousand
  source_ids:
  - S1
```

## INV-027

```yaml
id: INV-027
decision: reframe
scenario_title: HelloFresh 2017年报：贡献利润到EBITDA的缺口
focus: quantitative-calibration
subdomain: unit-economics
main_question: 贡献利润207.8百万欧元却有负70.1百万调整后EBITDA，二者差额占收入多少，能否全称为固定成本？
expected_output: 一个利润桥与未披露成本分类的边界
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 采用已读FY2017真实报表，不再求同cohort CAC或损耗。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-027
  status: sourced
  reason: 采用已读FY2017真实报表，不再求同cohort CAC或损耗。
  event: HelloFresh 2017年报：贡献利润到EBITDA的缺口
  cutoff: 2018-03-21 FY2017已公布后，核对贡献到EBITDA的差额。
  initial_facts:
  - id: F1
    text: 2018-03-21发布FY2017结果。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Contribution与Adjusted EBITDA是不同公司口径，贡献利润为排除SBC口径。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: FY2017收入904.9、贡献利润207.8、调整后EBITDA-70.1，单位百万欧元。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 贡献利润为正而EBITDA仍负；公布Q4活跃客户不能作全年订单的人均分母。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公司披露全年贡献率23.0%、调整后EBITDA率-7.7%；2018盈亏平衡是展望，非已实现。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://assets.ctfassets.net/irplh84t0tdt/1ZhSbql2qqdXpHeWBKpApz/19da9765c592e51c4e22b21aa7decda0/Press_Release_ENG_HelloFresh_FY17_21.3.18.pdf
    publisher: HelloFresh
    published_at: '2018-03-21'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手材料；本轮按修改后的单一问题核对，不以搜索摘要补事实。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
quantitative_inputs:
- name: revenue
  value: 904.9
  unit: EUR million
  source_ids:
  - S1
- name: contribution_ex_SBC
  value: 207.8
  unit: EUR million
  source_ids:
  - S1
- name: adjusted_EBITDA
  value: -70.1
  unit: EUR million
  source_ids:
  - S1
```

## INV-028

```yaml
id: INV-028
decision: reframe
scenario_title: Twitch 2012投资备忘录：主播持续使用与观看规模
focus: evidence-selection
subdomain: pmf-traction
main_question: 复杂开播条件下的持续主播行为，是否比总观看量提供更强的下一步需求证据？
expected_output: 一个优先检查、样本偏差与反证
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-028
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Twitch 2012投资备忘录：主播持续使用与观看规模
  cutoff: 2012-07-07 备忘录形成时
  initial_facts:
  - id: F1
    text: 备忘录记载每月约 15 万主播。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 约 1700 主播能够持续吸引至少 300 名观众。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 即使需要复杂软件或额外硬件，部分主播仍持续使用，是需求信号但非无偏留存样本。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 投资人记录了部分主播试用其他直播服务后返回的行为，需保留样本选择局限。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 备忘录建议投入 1300 万美元、投前估值 5300 万美元；未将建议写成已实现回报。
    source_ids:
    - S1
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 完整主播 cohort、观看留存和广告单位经济未知。
  sources:
  - id: S1
    url: https://www.bvp.com/memos/twitch
    publisher: Bessemer Venture Partners
    published_at: '2012-07-07'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-029

```yaml
id: INV-029
decision: reframe
scenario_title: Coinbase 2013 A轮：融资后的运营能力验证
focus: constrained-decision
subdomain: market-timing
main_question: 公告仍列购买和交付痛点时，应继续核验哪项运营或合规责任才值得进一步承诺？
expected_output: 一项条件式继续验证，不精算未知进入价格
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-029
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Coinbase 2013 A轮：融资后的运营能力验证
  cutoff: 2013-05-22 A 轮公告后，12 月 B 轮前
  initial_facts:
  - id: F1
    text: 公司宣布取得 500 万美元 A 轮。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: USV 的 Fred Wilson 领投；另有 Ribbit、SV Angel 等参与。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公司说明融资目标是改善购买限额、购买后交付速度和可用支付方式等痛点。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 公告正在招聘工程、设计、支持、compliance 与商务开发人员；不等同这些能力已经完备。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公司于 2013-05-22 宣布 A 轮完成；12 月融资是不同轮，不能合并当一笔交易。
    source_ids:
    - S1
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 具体监管判断、银行通道责任和完整经营指标未知。
  sources:
  - id: S1
    url: https://www.coinbase.com/en-au/blog/coinbase-raises-usd5m-in-series-a-funding
    publisher: Coinbase
    published_at: '2013-05-22'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-030

```yaml
id: INV-030
decision: reframe
scenario_title: Convoy 2023关闭备忘录：资本环境与经营解释
focus: causal-modeling
subdomain: funding-survival-exit
main_question: CEO把关闭归于货运衰退和融资收缩，哪条因果链已被记录，哪条仍需经营数据区分？
expected_output: 一个含竞争解释的因果图及可证伪观察
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 正式改为关闭公告后的归因审查，不要求此前未公开现金周期。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-030
  status: sourced
  reason: 正式改为关闭公告后的归因审查，不要求此前未公开现金周期。
  event: Convoy 2023关闭备忘录：资本环境与经营解释
  cutoff: 2023-10-19完整备忘录已公开后作归因评价，不模拟关闭前掌握内部财务。
  initial_facts:
  - id: F1
    text: 2023-10-19 CEO宣布关闭当前核心经营。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 备忘录回顾此前四个月探索战略选项；这是当事人陈述。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: CEO把货运衰退与资本市场收缩并列为解释。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 其称多种战略选项未能形成出路；该陈述本身未披露逐订单经营效率或完整现金数据。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: CEO宣布停止当前核心业务，大部分人员离职；关闭事实不独立证实某一种唯一原因。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://www.geekwire.com/2023/convoy-collapse-read-ceos-memo-detailing-sudden-shutdown-of-seattle-trucking-startup/
    publisher: Dan Lewis original memo reproduced by GeekWire
    published_at: '2023-10-19'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-031

```yaml
id: INV-031
decision: reframe
scenario_title: Atlassian 2010创始人演讲：OEM扩张的模式冲突
focus: boundary-transfer
subdomain: founder-execution
main_question: 低价自助模式扩展到OEM采购，哪项发布与支持要求使原增长机制失效？
expected_output: 一个可迁移机制及失效条件
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 用演讲实际记载的OEM尝试取代无法锁定2002—2005的单次节点。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-031
  status: sourced
  reason: 用演讲实际记载的OEM尝试取代无法锁定2002—2005的单次节点。
  event: Atlassian 2010创始人演讲：OEM扩张的模式冲突
  cutoff: 2010演讲公开后评价其所述OEM失败，具体尝试日未披露。
  initial_facts:
  - id: F1
    text: 创始人回顾因无法负担销售团队，采用低价、公开标价及自行下载。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 演讲还记载曾尝试进入OEM销售，而非所有客户都同一采购方式。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 其称OEM客户要求约两年发布周期和长期支持。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 这与快速发布的自助模式冲突，创始人把OEM尝试描述为失败；不把回顾等同独立因果实验。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 创始人报告OEM扩张未奏效；没有把这一事件硬定为2002—2005。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://businessofsoftware.org/talks/atlassian-from-bootstrap-to-60m-what-ive-learnt/
    publisher: Business of Software / Scott Farquhar
    published_at: '2010'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-032

```yaml
id: INV-032
decision: reframe
scenario_title: Reddit 2024发行文件：账面稀释与价格
focus: quantitative-calibration
subdomain: valuation-terms
main_question: 发行方以32.50美元为例列10.43美元每股有形净资产，22.07美元差额是什么，为什么不等于即时经济损失？
expected_output: 一项稀释复算及账面值与内在价值的边界
out_of_scope: 不混用不同窗口，不捏造交易条款或未来正常利润。
reason: 使用发行人公开假设计算而非自造价格；保留数量校准，不需要完整未来估值。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-032
  status: sourced
  reason: 使用发行人公开假设计算而非自造价格；保留数量校准，不需要完整未来估值。
  event: Reddit 2024发行文件：账面稀释与价格
  cutoff: 2024-03-19 FWP公开后、3月20日最终定价前。
  initial_facts:
  - id: F1
    text: 2024-03-19 FWP列发行方在32.50美元假设发行价下的稀释示例。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 这是发行方示例而非已确定最终定价；有形账面价值不等于内在价值。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 示例发行前每股有形净资产8.26美元，发行后10.43美元，新投资人稀释22.07美元。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 3月20日最终宣布34美元，2200万发行股含老股；公司不取得老股出售所得。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 公司3月20日公布实际发行定价；不能把34美元倒填3月19日的计算假设。
    source_ids:
    - S2
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1713445/000162828024011794/redditfwp31924.htm
    publisher: Reddit / SEC
    published_at: '2024-03-19'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
  - id: S2
    url: https://investor.redditinc.com/news-events/news-releases/news-details/2024/Reddit-Announces-Pricing-of-Initial-Public-Offering/default.aspx
    publisher: Reddit
    published_at: '2024-03-20'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手材料；本轮按修改后的单一问题核对，不以搜索摘要补事实。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
quantitative_inputs:
- name: issuer_assumed_price
  value: 32.5
  unit: USD per share
  source_ids:
  - S1
- name: postoffering_NTBV
  value: 10.43
  unit: USD per share
  source_ids:
  - S1
- name: preoffering_NTBV
  value: 8.26
  unit: USD per share
  source_ids:
  - S1
```

## INV-033

```yaml
id: INV-033
decision: reframe
scenario_title: Blue Apron 2017：回收倍数与cohort窗口
focus: quantitative-calibration
subdomain: unit-economics
main_question: 115美元贡献与94美元CPC形成怎样的比值，为什么它还不能证明同一cohort六个月回本？
expected_output: 一项复算、两种分母窗口的核对及不可推出的结论
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 正式改为公司回收展示的算术与cohort适用性核对；保留数量训练，不计算未披露的真实cohort回本天数。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-033
  status: sourced
  reason: 正式改为公司回收展示的算术与cohort适用性核对；保留数量训练，不计算未披露的真实cohort回本天数。
  event: Blue Apron 2017：回收倍数与cohort窗口
  cutoff: 2017-06-28 招股书发布后，交割前
  initial_facts:
  - id: F1
    text: 招股书披露平均 Cost per Customer 94 美元，按累计营销支出除累计获客数定义。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 六个月累计净收入平均约 410 美元，不包含产生收入的变动成本。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 六个月净贡献约 115 美元；贡献采用对应期平均订单成本，不是客户逐单精确利润。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 不同期限列采用有足够存续时间的不同 cohort，不能视作同一批客户连续轨迹。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 发行招股书最终列示每股 10 美元、3000 万股的 IPO；公司披露的贡献回收不等于持续正净利润。
    source_ids:
    - S1
  interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
  unknowns:
  - 更晚 cohort 是否恶化及未来履约效率未知；不能将平均 CPC 当每个付费渠道 CAC。
  sources:
  - id: S1
    url: https://www.stifel.com/prospectusfiles/PD_2474.pdf
    publisher: Blue Apron issuer prospectus hosted by Stifel
    published_at: '2017-06-28'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
quantitative_inputs:
- name: reported_CPC
  value: 94
  unit: USD per acquired customer, pooled window
  source_ids:
  - S1
- name: six_month_contribution
  value: 115
  unit: USD per eligible-cohort customer
  source_ids:
  - S1
- name: six_month_revenue
  value: 410
  unit: USD per eligible-cohort customer
  source_ids:
  - S1
```

## INV-034

```yaml
id: INV-034
decision: replace
scenario_title: Chegg 2023：生成式AI冲击下的增长与留存
focus: hypothesis-diagnosis
subdomain: pmf-traction
main_question: 新客户增长受压而管理层称留存强，哪些观察最能区分获客替代与存量价值流失？
expected_output: 两个竞争解释、一项区分证据及未来结果的归因边界
out_of_scope: 不得复用 PRO-080 问卷作主要材料；缺独立数据则换题
reason: 真实换题：Superhuman缺独立付费cohort且与PRO-080问卷重叠，改用Chegg已公开经营反馈。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-034
  status: sourced
  reason: 真实换题：Superhuman缺独立付费cohort且与PRO-080问卷重叠，改用Chegg已公开经营反馈。
  event: Chegg 2023：生成式AI冲击下的增长与留存
  cutoff: 2023-05-01 Q1公告后、后续全年结果前。
  initial_facts:
  - id: F1
    text: 2023-05-01 Q1结果披露订阅服务用户510万，同比下降5%。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: CEO称3月起ChatGPT兴趣上升、影响新客户增长，同时称既有客户留存强；后者是管理层自述。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: Q1订阅收入同比降3%；增长、用户数与留存不是同一指标。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 后来Q4订阅用户460万，同比降9%，订阅收入同比降6%；不能把跨季用户差额视为同cohort流失。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 2023Q4披露订阅用户与收入同比下降；这一结果未独立识别AI或其他因素各自贡献。
    source_ids:
    - S2
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://investor.chegg.com/Press-Releases/press-release-details/2023/Chegg-Announces-First-Quarter-2023-Earnings/default.aspx
    publisher: Chegg
    published_at: '2023-05-01'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
  - id: S2
    url: https://investor.chegg.com/Press-Releases/press-release-details/2024/Chegg-Reports-2023-Fourth-Quarter-and-Full-Year-Financial-Results/default.aspx
    publisher: Chegg
    published_at: '2024-02-05'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
    - outcome
  attempts:
  - 实际打开并阅读所列一手材料；本轮按修改后的单一问题核对，不以搜索摘要补事实。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-035

```yaml
id: INV-035
decision: reframe
scenario_title: MongoDB 2017 S-1：免费使用与可捕获商业价值
focus: boundary-transfer
subdomain: moat-competition
main_question: 免费核心、Enterprise与Atlas并存时，哪些采用信号不能直接变成公司的付费价值？
expected_output: 一项价值捕获边界和可替代反例
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-035
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: MongoDB 2017 S-1：免费使用与可捕获商业价值
  cutoff: 2017-09-21公开S1资本窗口，评估免费采用转付费能力；不声称当年云厂商均已提供同名托管MongoDB。
  initial_facts:
  - id: F1
    text: Community Server按AGPL提供免费核心数据库。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: Atlas于2016-06推出，按消费使用每月收费。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: S1披露Atlas占FY2017收入1%、截至2017-07-31半年收入5%，1,900余客户。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 风险披露承认免费用户不一定转付费；竞争者包括传统数据库、非关系数据库与AWS/GCP/Azure。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 公司已通过Enterprise和Atlas捕获部分商业价值，但下载量及免费使用不等于付费价值归属。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 转化风险为公司披露；竞争反例应限当时可证明产品，不能把后来SSPL变化当预设。
    source_ids:
    - S1
    attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
  unknowns:
  - 精确免费用户分母未知，不能用下载次数当用户数算转化率。
  - 本源列云竞争者但不证明2017具体同兼容托管替代，待ready时补具体产品。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1441816/000104746917006014/a2233365zs-1.htm
    publisher: MongoDB / SEC EDGAR
    published_at: '2017-09-21'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://www.sec.gov/Archives/edgar/data/1441816/000104746917006014/a2233365zs-1.htm
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-036

```yaml
id: INV-036
decision: reframe
scenario_title: Snowflake 2014公开发布：技术承诺与需求证据
focus: evidence-selection
subdomain: market-timing
main_question: 云弹性、SQL兼容及成本宣传中，哪项真实客户替代行为最值得投资人优先核验？
expected_output: 一个区分技术可行与采购需求的验证及反例
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 取消无材料的融资前采购复演，改为公开发布后投资论证验证。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-036
  status: sourced
  reason: 取消无材料的融资前采购复演，改为公开发布后投资论证验证。
  event: Snowflake 2014公开发布：技术承诺与需求证据
  cutoff: 2014-10-21公开发布后检验投资论证，不假装拥有此前投委会资料。
  initial_facts:
  - id: F1
    text: 2014-10-21公告公开Elastic Data Warehouse。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公告主张结合SQL数据仓库、数据灵活性和云弹性。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告称最近Series B由Redpoint领投，Sutter Hill及Wing参与；26m为累计融资。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 厂商90%成本节约是宣传主张，不是已独立核实的同工作负载成本实验。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公司公开产品与融资身份；这些事实尚不等于客户已愿意替代原数据仓库。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://www.globenewswire.com/news-release/2014/10/21/1186817/0/en/snowflake-raises-26m-in-funding-to-reinvent-the-data-warehouse.html
    publisher: Snowflake Computing issuer release / Marketwired
    published_at: '2014-10-21'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-037

```yaml
id: INV-037
decision: reframe
scenario_title: Rivian 2021初步IPO区间：基本股本与产能爬坡
focus: quantitative-calibration
subdomain: valuation-terms
main_question: 用57—62美元初步区间作基本市值敏感性比较时，哪些股本和产能条件会使外推失效？
expected_output: 一个条件性区间及不能提前使用最终定价的边界
out_of_scope: 基本股数为文件假设口径，转换票据/期权可能随价格改变；区间仅为明确固定所报基本股数的算术敏感性，不是最终完全稀释估值或产能预测。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-037
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Rivian 2021初步IPO区间：基本股本与产能爬坡
  cutoff: 2021-11-01公开S1/A，最终IPO定价前；只用57–62美元预估区间，不能提前给78。
  initial_facts:
  - id: F1
    text: 预估IPO每股57–62美元；当时假设基本发行后A+B股约861,995,652，不含部分期权/RSU等。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 截至10月31日生产180辆、交付156辆R1T，多数给员工。
    source_ids:
    - S1
    availability: pre_decision
  - id: F3
    text: Normal厂宣称安装年产能150,000；计划至2023累计capex约8bn。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 安装产能与实际爬坡不同，S1预计2024年初才达当前安装产能年化速率。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 转换票据及Forever发行的股数随IPO价格变化；基本股数不能当完全稀释恒定股本。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 最终IPO实际每股78美元、发行153m股；该结果需以最终424B4独立来源在最后揭晓，不证明产能/内在价值合理。
    source_ids:
    - S2
    availability: post_decision
  interpretation:
    text: 产能与capex为公司计划，不是已完成事实；估值情景不输出唯一目标价或持仓。
    source_ids:
    - S1
    attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
  unknowns:
  - 基本市值可按同版价格和股数推导，但不能和最终版发行股数混用。
  - 真实未来毛利与扩产成功概率未知，定量估值需声明模型边界；不能当合成历史事实。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1874178/000119312521315537/d157488ds1a.htm
    publisher: Rivian / SEC EDGAR
    published_at: '2021-11-01'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - F3
    - E1
    - E2
  - id: S2
    url: https://www.sec.gov/Archives/edgar/data/1874178/000119312521328239/d157488d424b4.htm
    publisher: Rivian / SEC EDGAR
    published_at: '2021-11-09'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - O1
  attempts:
  - url: https://www.sec.gov/Archives/edgar/data/1874178/000119312521315537/d157488ds1a.htm
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://www.sec.gov/Archives/edgar/data/1874178/000119312521328239/d157488d424b4.htm
    result: 已打开并读取最终定价与发行数，仅用于揭晓
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
quantitative_inputs:
- name: price_low
  value: 57
  unit: USD preliminary
  source_ids:
  - S1
- name: price_high
  value: 62
  unit: USD preliminary
  source_ids:
  - S1
- name: assumed_basic_postoffer_shares
  value: 861995652
  unit: shares at the prospectus assumption, not fully diluted
  source_ids:
  - S1
- name: produced_by_Oct31
  value: 180
  unit: vehicles
  source_ids:
  - S1
- name: delivered_by_Oct31
  value: 156
  unit: vehicles
  source_ids:
  - S1
```

## INV-038

```yaml
id: INV-038
decision: reframe
scenario_title: Peloton 2019：净CAC的硬件毛利抵扣
focus: boundary-transfer
subdomain: unit-economics
main_question: 同一笔硬件毛利在净CAC和订阅回收模型里分别出现时，哪一步会重复抵扣？
expected_output: 一份去重后的获取成本到订阅贡献口径图及适用边界
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 正式采用预列边界问题：净CAC已经抵扣硬件毛利，不再求缺完整cohort的回本时间。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-038
  status: sourced
  reason: 正式采用预列边界问题：净CAC已经抵扣硬件毛利，不再求缺完整cohort的回本时间。
  event: Peloton 2019：净CAC的硬件毛利抵扣
  cutoff: 2019-09-10上市前文件公开后，评估硬件抵扣获客成本的口径。
  initial_facts:
  - id: F1
    text: 业务组合含Connected Fitness硬件及订阅。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司净CAC定义为调整后销售营销费用减调整后硬件毛利。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公司披露FY2019净CAC总额1.6m、每新增订阅者5美元，不能重复再把已抵扣硬件毛利算一次。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: Subscription Contribution是非GAAP，排除折旧摊销与股权激励，不能等同完整自由现金贡献。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 公司展示低净CAC及订阅贡献的经济模型，同时披露口径限制；不足以直接计算任意cohort真实回本天数。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 经调整毛利抵扣获客是公司模型；不能把公司LTV预测视为后来实际兑现。
    source_ids:
    - S1
    attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
  unknowns:
  - 缺同cohort留存及现金成本时间序列；采用备用题：缺哪项硬件或订阅成本会让回本判断方向错误。
  - 总体月churn不能无说明替代每个cohort存活率。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1639825/000119312519242158/d738839ds1a.htm
    publisher: Peloton / SEC EDGAR
    published_at: '2019-09-10'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://www.sec.gov/Archives/edgar/data/1639825/000119312519242158/d738839ds1a.htm
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-039

```yaml
id: INV-039
decision: reframe
scenario_title: Canva 2015 Series A：组织采用与付费广度
focus: evidence-selection
subdomain: pmf-traction
main_question: 组织采用和免费非营利席位并存时，下一项分群证据怎样检验付费需求？
expected_output: 一项付款/续用检查及样本边界
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-039
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Canva 2015 Series A：组织采用与付费广度
  cutoff: 2015 SeriesA公告工件，Canva for Work已推出；精确公开日正文无日期，官方10年timeline将该文归2015。
  initial_facts:
  - id: F1
    text: 设计工具面向marketers、非营利、bloggers及教育等用户。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 原文称五百万用户、超过3500万design，不能直接当付费用户。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 创始人称Canva for Work上月推出，Yelp、Upworthy、Lonely Planet等采用。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 非营利团队可免费使用Work，因此企业/组织采用本身仍不等于付款。
    source_ids:
    - S1
    availability: pre_decision
  - id: E3
    text: 公司十年 timeline 将该创始人融资文章归于 2015 年；这是后见时间定位材料。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    id: O1
    text: 原文宣布15m SeriesA由Felicis领投、Blackbird和Matrix参与，资金支持扩张；它未公开证明各非设计师群体付费留存。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 采用/用户量来自公司自报；可选择验证付款、续用与分群，不能由后来的赢家规模证成2015下注。
    source_ids:
    - S1
    attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
  unknowns:
  - 各分群付费转化率、合同金额与retention未知。
  - 公告日期不明确，不借二手报道日期伪装原文已标。
  sources:
  - id: S1
    url: https://www.canva.com/newsroom/news/exciting-news-here-at-canva/
    publisher: Canva / Melanie Perkins
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
    url: https://www.canva.com/newsroom/news/canva-10-year-timeline/
    publisher: Canva
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E3
  attempts:
  - url: https://www.canva.com/newsroom/news/exciting-news-here-at-canva/
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://www.canva.com/newsroom/news/canva-10-year-timeline/
    result: 已读2015段并点击到原创始人融资说明；后见timeline不作同期用户数据
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-040

```yaml
id: INV-040
decision: reframe
scenario_title: Quibi 2020公开信：有剩余现金仍停止投入
focus: constrained-decision
subdomain: funding-survival-exit
main_question: 既有投入和剩余现金分别应怎样进入继续投入判断；什么条件才足以支持再试一次？
expected_output: 一项前瞻停止门槛及对沉没成本的处理
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 正式采用定性决策备用题，取消未公开现金跑道精算。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-040
  status: sourced
  reason: 正式采用定性决策备用题，取消未公开现金跑道精算。
  event: Quibi 2020公开信：有剩余现金仍停止投入
  cutoff: 2020-10-21公开信已可取得后的停止投入论证评价；不复演公告前的未知现金决策。
  initial_facts:
  - id: F1
    text: 2020-10-21公开信描述mobile-first premium服务及未达到预期。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 创始人称仍有现金跑道，并考虑过pivot等战略选项。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 创始人称已经穷尽可行选项；这是当事人判断而非独立证实。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 其选择wind down并向股东返还剩余现金，未选择持续经营直到现金全耗尽。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 创始人宣布结束经营并返还现金；不据此推定所有替代方案的净现值。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://quibi-hq.medium.com/an-open-letter-from-quibi-8af6b415377f
    publisher: Quibi / Jeffrey Katzenberg and Meg Whitman
    published_at: '2020-10-21'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-041

```yaml
id: INV-041
decision: reframe
scenario_title: Cloudflare 2015融资：网络规模与防守条件
focus: boundary-transfer
subdomain: moat-competition
main_question: 免费流量与网络覆盖在什么条件下才形成防守优势，在哪种客户价值条件下不能外推？
expected_output: 一条规模到防守的机制及失效条件
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 纠正未核2014融资身份，采用2015官方公告已有材料。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-041
  status: sourced
  reason: 纠正未核2014融资身份，采用2015官方公告已有材料。
  event: Cloudflare 2015融资：网络规模与防守条件
  cutoff: 2015-09-22公告后评估防守机制，不倒填2014未知轮次。
  initial_facts:
  - id: F1
    text: 2015-09-22宣布110m融资，投资方包括Fidelity、Google、Microsoft、Baidu、Qualcomm及原投资人。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司对比2012的23城市与2015的62城市网络。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公司自报约4m Internet properties及近每月1trillion page views；不是已披露单客盈利。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 作者称投资者未获特殊控制、董事席位、经济或信息权；这是公司自述而非完整合同。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 公司公告融资与网络扩展，网络规模本身不证明所有免费流量都有可防守的价值。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://blog.cloudflare.com/why-we-raised-110m-from-fidelity-google-microsoft-baidu-and-qualcomm/
    publisher: Cloudflare / Joshua Motta
    published_at: '2015-09-22'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - outcome
  attempts:
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-042

```yaml
id: INV-042
decision: reframe
scenario_title: Zoom 2013 B轮：businesses与付费购买信号
focus: evidence-selection
subdomain: market-timing
main_question: 4500家businesses和300万参与者，哪种企业购买证据才能反驳成熟竞品已足够的判断？
expected_output: 一项采购验证和不能由使用总量推出的结论
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-042
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Zoom 2013 B轮：businesses与付费购买信号
  cutoff: 2013-09-24 SeriesB公开材料，评估新进入窗口；不使用疫情后增长。
  initial_facts:
  - id: F1
    text: 产品将视频、web meetings及mobility统一，提供视频/音频/屏幕共享。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 公司称超过4500 businesses与3m participants使用；二者不是同一指标。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 公告列最多25人会议、商业产品9.99美元/月。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 公司将新融资用途指向教育、医疗及全球扩张，未披露4500businesses全部付费或enterprise contracts。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    id: O1
    text: 公司宣布6.5m SeriesB由Horizons领投，投资人加入董事会；采用增长是公司自报。
    source_ids:
    - S1
    availability: post_decision
  interpretation:
    text: 为尽调选择提供真实产品和有限商业信号；不由后来的赢家结果判当时必投。
    source_ids:
    - S1
    attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
  unknowns:
  - 采购链、付费转化和留存未知；应优先索取企业主动替换竞品并续用付款的证据。
  - 具体持股价格及基金仓位未知，不做精确投资回报/仓位。
  sources:
  - id: S1
    url: https://www.prnewswire.com/news-releases/zoom-video-communications-announces-record-customer-growth-and-series-b-funding-225021372.html
    publisher: Zoom Video Communications / PR Newswire
    published_at: '2013-09-24'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - E1
    - E2
    - O1
  attempts:
  - url: https://www.prnewswire.com/news-releases/zoom-video-communications-announces-record-customer-growth-and-series-b-funding-225021372.html
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-043

```yaml
id: INV-043
decision: reframe
scenario_title: Klarna 2021—2022：headline估值与每股价值
focus: quantitative-calibration
subdomain: valuation-terms
main_question: 45.6到6.7十亿美元的headline降幅是多少；它在哪一步不能替代旧股每股经济损失？
expected_output: 一个比例计算与缺少股本/权利时的不可识别边界
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 正式改为headline重定价比例与每股经济损失的边界；保留可算部分，不假定清算顺位或同比例稀释。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-043
  status: sourced
  reason: 正式改为headline重定价比例与每股经济损失的边界；保留可算部分，不假定清算顺位或同比例稀释。
  event: Klarna 2021—2022：headline估值与每股价值
  cutoff: 2022-07-11新融资公告已可取得，先核对两轮headline口径，再核对每股权利；不作2021投资预测。
  initial_facts:
  - id: F1
    text: 2021公司宣布639m新equity融资。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 2021公告post-money为45.6bn，SoftBank Vision Fund2领投。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 2022-07-11公司公告800m融资、post-money6.7bn，并明确是common equity。
    source_ids:
    - S2
    availability: post_decision
  - id: E2
    text: 2022公告希望随后让1000余小股东按pro-rata参与，不能当所有旧股已等比例参与。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    id: O1
    text: headline post-money降幅可对比，但不等于每位旧股东实际经济损失比例；旧股持有数、增资与权利仍必要。
    source_ids:
    - S1
    - S2
    availability: post_decision
  interpretation:
    text: 2022管理层对市场环境归因需标为当事人解释；不能擅自编造新轮优先清算条款。
    source_ids:
    - S1
    - S2
    attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
  unknowns:
  - 两轮完整cap table、每股价格、旧股参加增资情况与全部股权权利未公开。
  - 采用备用题：为什么缺少股权权利时，不能从融资估值比例推出旧股价值变化。
  sources:
  - id: S1
    url: https://news.cision.com/klarna-bank-ab--publ-/r/klarna-secures-additional-funding-as-consumers-demand-smarter-alternatives-to-shop--bank----pay,c3365020
    publisher: Klarna / Cision
    published_at: '2021-06-10'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - F2
    - O1
  - id: S2
    url: https://s205.q4cdn.com/644747736/files/doc_news/Klarna-closes-major-financing-round-during-worst-stock-downturn-in-50-years-holding-2022.pdf
    publisher: Klarna
    published_at: '2022-07-11'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E1
    - E2
    - O1
  attempts:
  - url: https://news.cision.com/klarna-bank-ab--publ-/r/klarna-secures-additional-funding-as-consumers-demand-smarter-alternatives-to-shop--bank----pay,c3365020
    result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
  - url: https://s205.q4cdn.com/644747736/files/doc_news/Klarna-closes-major-financing-round-during-worst-stock-downturn-in-50-years-holding-2022.pdf
    result: 已打开并读取融资金额、post-money、common equity与pro-rata段落
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
quantitative_inputs:
- name: prior_postmoney
  value: 45.6
  unit: USD billion
  source_ids:
  - S1
- name: new_postmoney
  value: 6.7
  unit: USD billion
  source_ids:
  - S2
- name: new_financing
  value: 800
  unit: USD million common equity
  source_ids:
  - S2
```

## INV-044

```yaml
id: INV-044
decision: reframe
scenario_title: DoorDash 2020披露：2019 GOV到毛利口径桥
focus: quantitative-calibration
subdomain: unit-economics
main_question: 用同份报表的收入、成本与折旧算毛利，为什么不能把GOV差额都称作履约成本？
expected_output: 一项8.85−5.23−0.27的复算及GOV/贡献利润的口径边界
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 原规划要求未披露的履约归属，现改为同份报表GOV到毛利的桥与不同利润口径；保留真实数字的数量校准。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-044
  status: sourced
  reason: 原规划要求未披露的履约归属，现改为同份报表GOV到毛利的桥与不同利润口径；保留真实数字的数量校准。
  event: DoorDash 2020披露：2019 GOV到毛利口径桥
  cutoff: 2020-11-30 S-1/A 已公开、IPO 定价之前；仅使用 2019 全年同窗口
  initial_facts:
  - id: I1
    text: 2019 Marketplace GOV 为 80 亿美元；GOV 包含税费、小费和平台费用，排除 Drive 订单金额。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 披露的桥为 GOV 减 merchant/Dasher pass-through 及退款、credits、promotions 得收入；Drive 按单费用作为其他收入净入 pass-through。
    source_ids: *id001
    availability: pre_decision
  - id: I3
    text: 2019 收入 8.85 亿美元，cost of revenue（不含折旧摊销）5.23 亿，相关折旧摊销 0.27 亿；三项均为公司口径。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 2019 毛利为 3.35 亿美元；Contribution Loss 为 2 亿，净亏损 6.67 亿，彼此不是同一利润指标。
    source_ids: &id002
    - S1
    availability: pre_decision
  - id: E2
    text: adjusted cost of revenue 从 GAAP 成本再剔除股权薪酬及分摊管理费用；不能把该口径当全部履约成本。
    source_ids: *id002
    availability: pre_decision
  outcome:
    text: 同份披露同时显示正毛利、负贡献利润和净亏损，GOV 规模不能直接推出净盈利。
    source_ids:
    - S1
  interpretation: 利润桥边界可据披露展开；具体城市单量或骑手单次成本不能替换公司全年口径。
  unknowns:
  - GOV 到收入的净额桥不等于会计费用表；各 pass-through 子项的全年独立金额未在本次摘录取得。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1792789/000119312520304953/d752207ds1a.htm
    publisher: DoorDash / SEC
    published_at: '2020-11-30'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - I3
    - E1
    - E2
    - outcome
  attempts:
  - 打开 S-1/A，核对 GOV 定义、Our Financial Model、全年成本表及毛利 reconciliation，区分收购子公司财务附注。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
quantitative_inputs:
- name: marketplace_GOV
  value: 8
  unit: USD billion
  source_ids:
  - S1
- name: revenue
  value: 885
  unit: USD million
  source_ids:
  - S1
- name: cost_ex_DA
  value: 523
  unit: USD million
  source_ids:
  - S1
- name: DA_in_cost
  value: 27
  unit: USD million
  source_ids:
  - S1
```

## INV-045

```yaml
id: INV-045
decision: reframe
scenario_title: DoorDash 2014 A轮：Palo Alto向郊区外推
focus: boundary-transfer
subdomain: pmf-traction
main_question: 当地需求成立以后，什么供需条件才支持把一地流动性外推到新城区？
expected_output: 一项迁移边界与可推翻的地方条件
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-045
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: DoorDash 2014 A轮：Palo Alto向郊区外推
  cutoff: 2014 年 A 轮投资决定之前；公开回顾只用于重建，不把后来的扩城成绩前置
  initial_facts:
  - id: I1
    text: DoorDash 从 Palo Alto 本地餐馆配送切入；多边平台需要同时组织商户、顾客和配送供给。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 投资人当时关注当地业务能否向郊区外推；Sequoia 的回顾称 Palo Alto 已有 product-market fit，此为投资人判断。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: Sequoia 与创始人访谈明确说明 2014 年 5 月领投 A 轮。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 当事人回顾称扩张由 Palo Alto 到 East San Jose；未给可独立核查的城市获客、供给与进入成本分表。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: A 轮身份已由直接参与者确认；郊区扩张是其叙述的策略，不能据此证明任一新城都具备同样流动性。
    source_ids:
    - S1
    - S2
  interpretation: 本地成功外推所需反证属于维护者分析；不能把融资成功或后来的上市当作当时城市经济性的验证。
  unknowns:
  - 未取得不同城市在 A 轮前的独立 cohort、配送供给和市场进入成本材料。
  - NFX 转录的内部 memo 有删节，所述贡献毛利明确是公司 claim；未以其替代未公开原表。
  sources:
  - id: S1
    url: https://sequoiacap.com/podcast/crucible-moments-doordash
    publisher: Sequoia / Tony Xu / Alfred Lin
    published_at: null
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - outcome
  - id: S2
    url: https://sequoiacap.com/article/doordash-ipo-resilience-gets-results
    publisher: Sequoia / Alfred Lin
    published_at: '2020-12-09'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E2
    - outcome
  attempts:
  - 阅读 Sequoia 全文回顾和访谈；打开其原始 A 轮 deck Dropbox 链接但返回空错误页。
  - 阅读 https://podcast.nfx.com/episodes/doordash-memo/transcript；是外部转录且 cohort 图删节，未当完整原始尽调材料。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-046

```yaml
id: INV-046
decision: reframe
scenario_title: FTX 2021 B轮公告后：托管与关联方权限尽调
focus: evidence-selection
subdomain: founder-execution
main_question: 融资规模和知名投资者能否替代托管隔离验证，缺哪项权限证据应停止继续尽调？
expected_output: 一项停止门槛与事后司法证据的正确位置
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-046
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: FTX 2021 B轮公告后：托管与关联方权限尽调
  cutoff: 2021-07-20融资公告已知之后、后续资产安全尽调之前；不假定仍可按同轮条款进入，也不前置2024司法结果。
  initial_facts:
  - id: I1
    text: FTX 对外定位为加密资产交易所；其当轮公告将扩张和产品增长列为资金用途。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 公司宣布 B 轮 9 亿美元、180 亿美元估值；这验证公告身份，不能验证客户资产隔离或交易对手风险。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 司法部 2024 年通报：陪审团定罪后，Bankman-Fried 被判 25 年；案件涉及客户资金挪用和对投资人虚假陈述。
    source_ids:
    - S2
    availability: post_decision
  - id: E2
    text: 通报指出客户资产安全、Alameda 无特殊待遇等表述与实际行为不符；这些是事后司法材料。
    source_ids:
    - S2
    availability: post_decision
  outcome:
    text: 后续司法结果支持托管和关联方权限必须独立验证的训练方向；不得把这些后来事实放进 2021 年首轮。
    source_ids:
    - S2
  interpretation: 停止尽调的门槛应由学员提出；本报告没有证明某位 2021 投资人收到或忽略了特定材料。
  unknowns:
  - 实际 data room、投资人索取和取得的托管对账、关联交易清单及权限审计未知。
  - 2023 SEC complaint 的约 10 亿美元轮次描述与公司公告 9 亿口径不同，未擅自调和。
  sources:
  - id: S1
    url: https://www.prnewswire.com/news-releases/ftx-trading-ltd-closes-900m-series-b-round-largest-raise-in-crypto-exchange-history-847881913.html
    publisher: FTX via PR Newswire
    published_at: '2021-07-20'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
  - id: S2
    url: https://www.justice.gov/usao-sdny/pr/samuel-bankman-fried-sentenced-25-years-prison
    publisher: US DOJ / SDNY
    published_at: '2024-03-28'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E1
    - E2
    - outcome
  attempts:
  - 阅读公司融资公告与 DOJ 判刑通报正文。
  - 打开 SEC Nishad Singh complaint https://www.sec.gov/files/litigation/complaints/2023/comp-pr2023-40.pdf，区分指控与判决。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-047

```yaml
id: INV-047
decision: reframe
scenario_title: Better 2023财务附注：零票息bridge的股权风险
focus: prediction-counterfactual
subdomain: funding-survival-exit
main_question: 零票息且不可现金偿还的bridge，为何仍会改变旧股风险，哪些转换条件会改变判断？
expected_output: 一条到期—转换—稀释条件链及缺合同处的边界
out_of_scope: 不推定未披露交易条款、内部现金跑道、同cohort成本或因果贡献；公开披露时点不是原私募投资时点。
reason: 锁定2021 bridge在2023财务附注的状态，取消未确认最后一笔续命融资与完整估值。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-047
  status: sourced
  reason: 锁定2021 bridge在2023财务附注的状态，取消未确认最后一笔续命融资与完整估值。
  event: Better 2023财务附注：零票息bridge的股权风险
  cutoff: 2023年披露截至6月30日财务附注已公开后，评价已披露bridge条件；不模拟2021投资前资料。
  initial_facts:
  - id: F1
    text: 附注单列2021年12月pre-closing bridge notes。
    source_ids:
    - S1
    availability: pre_decision
  - id: F2
    text: 票据零票息且不可现金偿还；不等于免费资本或没有股权风险。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 截至2023-06-30账面750m美元，仍未转优先股。
    source_ids:
    - S1
    availability: pre_decision
  - id: E2
    text: 附注说明延期需要同意及章程等步骤；另有2023年2月信用额度修改，不能合并成同一交易。
    source_ids:
    - S1
    availability: pre_decision
  outcome:
    text: 财务附注报告bridge仍未转换的状态及相关条件；不是将未来SPAC完成预先当成确定结果。
    source_ids:
    - S1
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1835856/000162828023030682/exhibit991-super8xkbetterq2.htm
    publisher: Better Holdco / SEC
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
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
```

## INV-048

```yaml
id: INV-048
decision: reframe
scenario_title: Palantir 2020披露：Scale分群的选择边界
focus: hypothesis-diagnosis
subdomain: moat-competition
main_question: 正贡献毛利是Scale分类条件时，Scale客户毛利改善能否证明整个交付模式可复制？
expected_output: 一个选择偏差诊断与能改变判断的证据
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-048
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: Palantir 2020披露：Scale分群的选择边界
  cutoff: 2020-09-21 公开文件之后、直接上市交易之前
  initial_facts:
  - id: I1
    text: 公司披露 Gotham 与 Foundry 两个平台，并以客户获取、扩张、规模阶段描述交付经济性。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: Acquire 客户年收入低于 10 万美元，常以低价或免费 pilot 开始；Scale 分类同时要求年收入超过 10 万且贡献毛利为正。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 2019 Scale 客户收入 5.657 亿美元、贡献毛利率 55%；相同客户 H1 2020 收入 2.963 亿、贡献毛利率 68%。
    source_ids: &id002
    - S1
    availability: pre_decision
  - id: E2
    text: 2019 Acquire 客户收入 60 万美元、贡献亏损 6540 万；公司披露的是交付分群而非任意全体客户的平台复制率。
    source_ids: *id002
    availability: pre_decision
  outcome:
    text: 公开文件记录相同 Scale 客户的贡献毛利率变化；由于 Scale 本身按正毛利筛选，不能单独证明全平台已可规模化复制。
    source_ids:
    - S1
  interpretation: “客户嵌入就是平台复制”和“客户只是咨询项目”均仍是假说；需部署工时、标准产品复用及后续扩张区别证据。
  unknowns:
  - 未取得每客户部署工时、工程人力、定制代码占比及可比较的标准化部署 cohort。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1321655/000119312520249544/d904406ds1a.htm
    publisher: Palantir / SEC
    published_at: '2020-09-21'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 打开 S-1/A，核对平台描述、阶段定义及同一 Scale 客户的 2019/H1 2020 披露。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-049

```yaml
id: INV-049
decision: reframe
scenario_title: Wix 2007：市场总量与付费需求的论证缺口
focus: evidence-selection
subdomain: market-timing
main_question: memo从网站总量推到可付费需求的哪一跳最薄弱，应优先用怎样的付款观察检验？
expected_output: 一个论证缺口、最高信息价值验证及停止外推的条件
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 正式采用预列证据选择备用题，取消无付款数据的SMB可服务市场精算；memo本身是可检验的真实投资论证。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-049
  status: sourced
  reason: 正式采用预列证据选择备用题，取消无付款数据的SMB可服务市场精算；memo本身是可检验的真实投资论证。
  event: Wix 2007：市场总量与付费需求的论证缺口
  cutoff: 2007-10-19 memo 建议作出之前；memo 内估计和建议条款须标归属
  initial_facts:
  - id: I1
    text: 原始 memo 署名 Adam Fisher，建议 BVP 投资 200 万美元第二轮 seed；这是建议文件而非签署交割证明。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 产品面向大众富媒体网页/组件创作，临近 closed beta；作者明确表示商业模式仍不确定。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: memo 把小企业网站列为目标用途，并讨论订阅、模板、广告等商业化选择；没有给出已观测的 Wix SMB 付费意愿。
    source_ids: &id002
    - S1
    availability: pre_decision
  - id: E2
    text: memo 的网站数量和小企业数量是作者引用的市场断言；列举的 5.95 美元到数百美元月费是外部网站托管背景，不是 Wix 实测价格。
    source_ids: *id002
    availability: pre_decision
  outcome:
    text: 原始 memo 在承认商业模式不确定的同时推荐投资；能支持分析其论证缺口，不能凭其 TAM 断言形成独立市场验证。
    source_ids:
    - S1
  interpretation: 维护者判断：富媒体创作用户、网站数与可付费 SMB 分母需要分离；不能把免费用户直接乘任意价格。
  unknowns:
  - 当时可服务的特定 SMB 分母、独立支付证据、转化率和服务边界不足。
  - 本次未取得实际交割文件，memo 所载估值和所有权是提议条款。
  sources:
  - id: S1
    url: https://www.bvp.com/memos/wix
    publisher: Bessemer Venture Partners / Adam Fisher
    published_at: '2007-10-19'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 阅读 BVP 原始 memo 的日期、deal、business model 与网站市场段落，区分推荐、估计和观察；网页重刊日期未知，published_at 使用原文日期。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```

## INV-050

```yaml
id: INV-050
decision: reframe
scenario_title: Airbnb 2020借款的年报核对：两笔融资与净到款
focus: quantitative-calibration
subdomain: valuation-terms
main_question: 两笔各10亿美元借款合计净到款多少，为什么不能把名义金额、净现金和一笔原始合同混成同一口径？
expected_output: 一项总额到净现金复算及交易身份边界
out_of_scope: 不借 IPO 价格兜底或混用两次交易
reason: 把接受/等待的未知现金选择改为2021年报已公开后的融资核对；保留实际数量输入。
admission: eligible
admission_reason: 明确单一节点与可回答的问题，至少2项事前事实、2项实质证据和直接支持的观察结果；准入不等于ready。
research:
  id: INV-050
  status: sourced
  reason: 把接受/等待的未知现金选择改为2021年报已公开后的融资核对；保留实际数量输入。
  event: Airbnb 2020借款的年报核对：两笔融资与净到款
  cutoff: 2021-02-26年报已公开后核对2020借款，不把后来的细节当2020-04-06已知。
  initial_facts:
  - id: F1
    text: 2021年报公开2020年4月两笔各10亿美元融资。
    source_ids:
    - S2
    availability: pre_decision
  - id: F2
    text: 同期4月6日公告为Silver Lake与Sixth Street的债务及股权证券组合；不等于两笔借款身份完全相同。
    source_ids:
    - S1
    availability: pre_decision
  evidence:
  - id: E1
    text: 年报记载second-lien净到款967.5、first-lien净到款961.4，单位百万美元。
    source_ids:
    - S2
    availability: pre_decision
  - id: E2
    text: 年报条款说明包含后续修订，不能全部反推为4月6日初始合同。
    source_ids:
    - S2
    availability: pre_decision
  outcome:
    text: 公司年报确认借款和两项净到款；融资实现不证明当时接受必优于等待。
    source_ids:
    - S2
  interpretation: 来源披露、当事人解释与维护者推论区分；不以事后结果裁定唯一正确选择。
  unknowns:
  - 完整内部判断及反事实结果未知；不计算未披露的价格、成本或实现回报。
  sources:
  - id: S1
    url: https://news.airbnb.com/silver-lake-sixth-street-partners-invest-1-billion-in-airbnb
    publisher: Airbnb
    published_at: '2020-04-06'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F2
  - id: S2
    url: https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm
    publisher: Airbnb / SEC
    published_at: '2021-02-26'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - F1
    - E1
    - E2
    - outcome
  attempts:
  - 复用并逐项阅读初轮保存的一手材料摘录与引用，按本轮正式修订的问题和披露时点核对；未宣称重新获取完整合同。
  phase2_conditions: 本轮正式修订单题范围；原候选和Phase2规划另保留，制作时使用本条新范围。
quantitative_inputs:
- name: second_lien_face
  value: 1000
  unit: USD million
  source_ids:
  - S2
- name: first_lien_face
  value: 1000
  unit: USD million
  source_ids:
  - S2
- name: second_lien_net
  value: 967.5
  unit: USD million
  source_ids:
  - S2
- name: first_lien_net
  value: 961.4
  unit: USD million
  source_ids:
  - S2
```

## INV-051

```yaml
id: INV-051
decision: reframe
scenario_title: Dropbox 2018披露：合并毛利增量与套餐归因
focus: quantitative-calibration
subdomain: unit-economics
main_question: 收入和毛利率同时变化后，总毛利约增多少；这能否唯一识别套餐组合贡献？
expected_output: 一个按披露精度计算的总毛利增量与不能识别的归因
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 正式改为合并报表的毛利算术与归因上限；可比较总体收入/毛利率，不再拆解未披露个人与团队业务。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-051
  status: sourced
  reason: 正式改为合并报表的毛利算术与归因上限；可比较总体收入/毛利率，不再拆解未披露个人与团队业务。
  event: Dropbox 2018披露：合并毛利增量与套餐归因
  cutoff: 2018-02-23 S-1 公开后、IPO 定价之前
  initial_facts:
  - id: I1
    text: 2017 付费用户 1100 万，口径是付费许可证/用户，单人可能有多个账户；不是 1100 万企业合同。
    source_ids: &id001
    - S1
    availability: pre_decision
  - id: I2
    text: 2017 ARPU 为 111.91 美元；公司将同比增加归因于较高价套餐组合，包括 Business Advanced，但未披露独立结构贡献。
    source_ids: *id001
    availability: pre_decision
  evidence:
  - id: E1
    text: 2016/2017 公司收入 8.448/11.068 亿美元，毛利率 54%/67%；这是汇总口径。
    source_ids: &id002
    - S1
    availability: pre_decision
  - id: E2
    text: 公司说明 2017 成本下降含基础设施优化，仍没有个人/团队套餐收入及可归属成本分解。
    source_ids: *id002
    availability: pre_decision
  outcome:
    text: 公司毛利改善与较高价格套餐组合同时见于 S-1；不能从合并毛利表唯一解出套餐结构贡献。
    source_ids:
    - S1
  interpretation: 训练应追问独立客户和套餐数据，不再次用 ENG-150 的存储成本数字作为答案。
  unknowns:
  - 个人与团队各自收入、合同折扣、活跃席位及相应服务成本未取得。
  - 企业计划价格变化、客户规模与基础设施成本的交互贡献无法由汇总表识别。
  sources:
  - id: S1
    url: https://www.sec.gov/Archives/edgar/data/1467623/000119312518055809/d451946ds1.htm
    publisher: Dropbox / SEC
    published_at: '2018-02-23'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - E1
    - E2
    - outcome
  attempts:
  - 阅读首份 S-1，核对付费用户定义、ARPU、收入成本表及 2017 成本变动说明。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
quantitative_inputs:
- name: 2016_revenue
  value: 844.8
  unit: USD million
  source_ids:
  - S1
- name: 2017_revenue
  value: 1106.8
  unit: USD million
  source_ids:
  - S1
- name: 2016_margin
  value: 54
  unit: percent rounded
  source_ids:
  - S1
- name: 2017_margin
  value: 67
  unit: percent rounded
  source_ids:
  - S1
```

## INV-052

```yaml
id: INV-052
decision: reframe
scenario_title: GitLab 2017 C轮：企业套餐与支付需求
focus: evidence-selection
subdomain: pmf-traction
main_question: 企业功能和标价已经存在时，哪项证据才能区分活跃开源社区与真实企业付款？
expected_output: 一项付费尽调门槛与不可推出的PMF结论
out_of_scope: 不外推未披露cohort、边际成本、股本权利或因果贡献；不把公司披露或投资建议当成已实现投资回报。
reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
admission: eligible
admission_reason: 已逐项复核保存的直接来源事实和引用；现题限于来源可支持的条件、比较与结果，不要求缺失输入。
research:
  id: INV-052
  status: sourced
  reason: 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。
  event: GitLab 2017 C轮：企业套餐与支付需求
  cutoff: 2017 C 轮投资决定前；使用此前已公布的企业套餐能力
  initial_facts:
  - id: I1
    text: 2016-12-08 已发布 EE Premium，面向全球团队，包含高级支持、Geo、高可用和工作流控制等能力。
    source_ids:
    - S2
    availability: pre_decision
  - id: I2
    text: Premium 公开价格 199 美元/用户/年；公司解释单独产品采购导致内部审批阻力，因此改为打包。价格和厂商解释不等于支付 cohort。
    source_ids:
    - S2
    availability: pre_decision
  evidence:
  - id: E1
    text: GitLab 2017-10-09 公告确认 GV 领投 2000 万美元 Series C。
    source_ids:
    - S1
    availability: post_decision
  - id: E2
    text: 公告的组织采用/开源使用规模是公司营销说法，未区分社区用户与签约付费企业。
    source_ids:
    - S1
    availability: post_decision
  outcome:
    text: 真实轮次及融资前企业套餐可确认；已有企业功能和标价仍不能单独证明企业付费 PMF。
    source_ids:
    - S1
    - S2
  interpretation: 优先尽调项可选择付费合同 cohort、续费/扩张与采购周期，具体优先级由学员论证。
  unknowns:
  - 未取得 2017 社区与付费企业分群、真实合同数、续费和扩张收入。
  - GV 后来 IPO 回顾属于事后材料，不能将 2021 收入增长倒填成 2017 支付证据。
  sources:
  - id: S1
    url: https://about.gitlab.com/press/releases/2017-10-09-gitlab-raises-c-round/
    publisher: GitLab
    published_at: '2017-10-09'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - E1
    - E2
    - outcome
  - id: S2
    url: https://about.gitlab.com/blog/announcing-gitlab-enterprise-edition-premium/
    publisher: GitLab
    published_at: '2016-12-08'
    source_type: primary
    checked_at: '2026-10-25'
    supports:
    - I1
    - I2
    - outcome
  attempts:
  - 阅读 2017 C 轮新闻稿与 2016 Premium 公告全文，核对日期、价格和产品内容。
  - 阅读 GV IPO 回顾 https://www.gv.com/news/gitlab-ipo，仅作事后身份交叉检查，不前置增长结果。
  - 本轮复核初轮逐项保存的来源摘录、引用和未知；正式缩小问题范围，不新增没有依据的史实。
  phase2_conditions: 本轮正式采用本条新问题与认知动作；原数量门槛仅存历史，不再要求未披露输入。
```
