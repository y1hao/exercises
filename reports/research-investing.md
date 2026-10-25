# Phase 3 创投来源核查 — INV001–034

核查日期 2026-10-25。仅研究素材；不代表完整 Brief 或 ready。投资 memo 中拟议交易必须与交割、长期回报区分。

## INV-001

```yaml
id: INV-001
status: sourced
reason: 已读取官方 F-1、路演与定价公告，能区分价格区间、业务数据与最终发行价。
event: Arm 2023 IPO 定价前的业务和股本评估
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
phase2_conditions: 计算只使用公开价格、股本与已披露业务口径；不补造估值参数。
```

## INV-002

```yaml
id: INV-002
status: blocked
reason: 找到同期 S-1 和官方 PDF，但正文读取渠道因体积或访问错误失败；不能把搜索摘要当成完整利润归属依据。
event: Instacart 2023 IPO 前订单与广告贡献拆分
cutoff: 拟以 2023 上市前公开报表为界，尚未完整核定。
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 搜索检索到广告与交易收入分类，不足以确认各自完整成本口径。
unknowns:
- 广告与交易成本的可归属范围；同窗口订单利润；完整原文。
sources: []
attempts:
- https://www.sec.gov/Archives/edgar/data/1579091/000119312523221345/d55348ds1.htm：正文超
  4MB 抓取限制。
- https://investors.instacart.com/static-files/f55982cd-0974-4fbf-ba2a-c1a545971697：官方
  PDF 读取错误。
- https://instacart.gcs-web.com/static-files/8fe29217-df54-48c5-89a1-387a5220ef0e：官方
  PDF 读取错误。
phase2_conditions: 不退回 2020 融资混用数据；需重试正文或改用明确的定性备用问题。
```

## INV-003

```yaml
id: INV-003
status: sourced
reason: 已读取 Bessemer 2011-01-10 原始投资建议正文；适合检查交易质量证据，不推断后续回报。
event: Fiverr 2011 年 Bessemer 投资建议
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
  text: 公司 2012 年转载报道提及此前早期融资，但不是 2011 年可知材料或直接轮次证明。
  source_ids:
  - S2
  availability: post_decision
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
  - outcome
- id: S2
  url: https://www.fiverr.com/news/the-next-web
  publisher: Fiverr转载The Next Web
  published_at: '2012-05-03'
  source_type: secondary
  checked_at: '2026-10-25'
  supports:
  - E2
attempts:
- 打开 BVP 原始备忘录及公司转载新闻；不以转载当原始轮次合同。
phase2_conditions: 以备忘录证据选择为训练范围，不要求无依据的精确仓位。
```

## INV-004

```yaml
id: INV-004
status: sourced
reason: 直接投资备忘录包含同期客户、MRR、现金和拟议条款，可支持尽调证据选择。
event: Shopify 2010 Series A 投资建议
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
phase2_conditions: 只做下一项尽调证据选择，不把拟议条款默认为最终交割。
```

## INV-005

```yaml
id: INV-005
status: sourced
reason: 同期备忘录足以界定内容壁垒问题，同时发现原始 Series B 标签与直接记录冲突。
event: Yelp 2005 首次风险融资的投资建议，而非已确认 Series B
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
phase2_conditions: 原候选标题应记录轮次修正；原始输入与日期ID保留。
```

## INV-006

```yaml
id: INV-006
status: blocked
reason: 2010 S-1 可核实 2008 年融资与条款，但缺足够证据确定某个 2008 续资决策前可知的现金跑道和里程碑。
event: Tesla 2008 年 12 月可转换借款
cutoff: 拟为 2008 年 12 月追加资本决定前；精确决策日和当时可得材料未确认。
initial_facts: []
evidence:
- id: E1
  text: S-1 回溯记载 2008 年 12 月新增借款收到 1450 万美元，并有以此后融资价格一定比例转换的安排。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: S-1 把 2009 年追加借款和之后股权融资分开披露，不能合并成同一笔 2008 现金。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 后来的 S-1 确认存在 2008 年 12 月借款及后续转换过程，但不证明每个投资者当时看到完整现金资料。
  source_ids:
  - S1
interpretation: 可作结果核实材料，尚不足以自包含地重建续资前决策。
unknowns:
- 当时现金跑道；具体续资前技术状态；投资者可见材料。
sources:
- id: S1
  url: https://ir.tesla.com/_flysystem/s3/sec/000119312510017054/ds1-gen_0.pdf
  publisher: Tesla
  published_at: '2010-01-29'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
  - E2
  - outcome
attempts:
- 读取官方 S-1 的 2008 convertible notes 段落；搜索同期融资公告与 2008 危机记录。
phase2_conditions: 不从后来回顾补造当时跑道，也不要求精确收益。
```

## INV-007

```yaml
id: INV-007
status: blocked
reason: 已读取 SEC 原始诉状，但它是事后指控材料；尚未确认指定轮次的事前材料与尽调权限。
event: Theranos 2013—2015 投资者陈述及 2018 SEC 指控
cutoff: 原计划要求某轮融资前；具体轮次与起始信息仍缺证。
initial_facts: []
evidence:
- id: E1
  text: SEC 诉状称投资人收到技术、合同、监管与财务陈述。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 诉状区分公司宣称可处理的测试范围与监管方指控的实际能力；两者都不能预先当投资人已知。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 2018 年 SEC 提出证券欺诈指控；本诉状本身不是全部事实已经审判认定的证明。
  source_ids:
  - S1
interpretation: 指控可以支持需要核查的主张，不能由此编写全知视角的事前尽调。
unknowns:
- 所选投资轮次；当时可索取的技术结果；哪些陈述何时可知。
sources:
- id: S1
  url: https://www.sec.gov/files/litigation/complaints/2018/comp-pr2018-41-theranos-holmes.pdf
  publisher: US SEC
  published_at: '2018-03-14'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
  - E2
  - outcome
attempts:
- 读取 SEC 诉状及其投资者陈述段落；搜索同期投资节点。
phase2_conditions: 不将 2004—2015 合并为一次融资，也不将后来指控当开场真相。
```

## INV-008

```yaml
id: INV-008
status: sourced
reason: 上市前 S-1 完整可读，直接披露周期依赖及不同年度盈利，可支持竞争解释训练。
event: Coinbase 2021 直接上市前周期盈利判断
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
phase2_conditions: 只诊断盈利可持续性的解释，不做没有进入价格的仓位精算。
```

## INV-009

```yaml
id: INV-009
status: blocked
reason: 已读 S-1/A，但未得到拟选城市或 cohort 的同口径补贴与成本，不能开展原数量题。
event: Lyft 2019 上市前贡献口径
cutoff: 2019-03-18 披露后，定价前
initial_facts: []
evidence:
- id: E1
  text: Contribution 排除部分会计项目，并非 EBITDA 或净利润。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 2018 年贡献率为 42.7%，调整后 EBITDA 仍为负；两者不能混用。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  text: ''
  source_ids: []
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 城市/cohort 原始输入及回收期未取得。
sources:
- id: S1
  url: https://investor.lyft.com/financials/sec-filings/content/0001193125-19-077391/d633517ds1a.htm
  publisher: Lyft via SEC
  published_at: '2019-03-18'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
  - E2
attempts:
- 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
phase2_conditions: 可审议口径对照备用题；尚未迁移 focus。
```

## INV-010

```yaml
id: INV-010
status: blocked
reason: 直接公司与投资人文章确认的是 2015 A 轮，不是拟选的 2016 融资；采购证据也不足。
event: Figma 2015 Series A 与 Preview（候选 2016 轮次待改）
cutoff: 2015-12-03 Preview 发布时，2016 多人功能前
initial_facts: []
evidence:
- id: E1
  text: 2015 Preview 发布文章的 1800 万美元是累计融资口径，不能直接当单轮金额。
  source_ids:
  - S1
  availability: unknown
outcome:
  text: 2015-12-03 宣布 Preview；2016 多人功能属于未来计划。
  source_ids:
  - S1
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 2016 独立轮次、团队采购和预算角色未核实。
sources:
- id: S1
  url: https://www.figma.com/blog/design-meet-the-internet/
  publisher: Figma / Dylan Field
  published_at: '2015-12-03'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
  - outcome
attempts:
- 打开 Figma 发布正文。
- 打开 https://greylock.com/blog/design-together/ ：2015-12-02 宣布 Greylock 领投 Series
  A，但未取得采购 cohort。
phase2_conditions: 建议显式修正为 2015 轮次，获得采购材料后再解除阻塞。
```

## INV-011

```yaml
id: INV-011
status: blocked
reason: 官方来源确认采购结果，但没有支持拟选资本决策时剩余现金和可选行动的事前材料。
event: SpaceX 2008 生存融资与 CRS 里程碑
cutoff: 2008-12-23 合同授予前；确切资金决定日未核实
initial_facts: []
evidence: []
outcome:
  text: 2008-12-23 NASA 向 SpaceX 和 Orbital 授予商业 ISS 补给合同。
  source_ids:
  - S1
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 剩余资本、付款时序及当时可行融资方案未核实。
sources:
- id: S1
  url: https://space.commerce.gov/commercial-iss-resupply-contracts-awarded/
  publisher: US Office of Space Commerce
  published_at: '2008-12-23'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - outcome
attempts:
- 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
phase2_conditions: 不能从合同名义价值推断当时现金到账；需补资本约束。
```

## INV-012

```yaml
id: INV-012
status: sourced
reason: 同期投资备忘录直接支持产品、客户访问、竞品与拟议交易。
event: SendGrid 2011 Series B 投资建议
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
phase2_conditions: 按投递能力和接口体验的可复制边界，不倒灌上市后数据。
```

## INV-013

```yaml
id: INV-013
status: sourced
reason: 直接参与者回顾包含现金目标和经营试验；标明事后回忆，不当作同期公开市场信息。
event: Airbnb 2009 年初经营现金生存试验
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
phase2_conditions: 只讨论经营验证与融资优先级；不算精确种子回报。
```

## INV-014

```yaml
id: INV-014
status: blocked
reason: 直接公告确认融资，但条款明确未披露；不足以预测旧股的合同稀释或顺位。
event: Box 2014 延期上市窗口融资
cutoff: 2014-07-07 融资公告后
initial_facts: []
evidence:
- id: E1
  text: 公告披露 TPG Growth 与 Coatue 投资 1.5 亿美元，并安排 TPG 董事。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  text: 公司公告新增投资；公告并未披露优先权等交易条款。
  source_ids:
  - S1
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 估值、清算顺位及完整股本变化未核实。
sources:
- id: S1
  url: https://www.boxinvestorrelations.com/news-and-media/news/press-release-details/2014/Box-Announces-150-Million-Investment-from-TPG-Growth-and-Coatue/default.aspx
  publisher: Box
  published_at: '2014-07-07'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
  - outcome
attempts:
- 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
phase2_conditions: 维持 blocked；可审议改为交易条款证据选择，不虚构优先权。
```

## INV-015

```yaml
id: INV-015
status: blocked
reason: 未取得匹配实际私募轮次的城市收入、补贴、成本，不能拿全公司报表替代局部计算。
event: Uber 上市前最近私募窗口与局部单位经济
cutoff: 2019 上市前；最近融资窗口尚未核定
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 最近一轮的实际进入日期与局部 cohort 数据不足。
sources:
- id: S1
  url: https://www.sec.gov/Archives/edgar/data/1543151/000119312519120759/d647752ds1a.htm
  publisher: Uber via SEC
  published_at: '2019-04-26'
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 检索 Uber 2019 S-1/A；只定位到公开申报入口，尚未完成正文和城市输入核验，未据此升级。
phase2_conditions: 不得拼接不同轮估值或以公司亏损代替城市贡献口径。
```

## INV-016

```yaml
id: INV-016
status: sourced
reason: 直接投资记录可用于选择下一项需求证据；不把兴趣活动等同收入。
event: Pinterest 2011 投资考察备忘录
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
  text: 投资人已整理考察材料并安排创始人演示；实际交割条款及长期回报未在此记录中核实。
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
phase2_conditions: 问题是下一项证据选择，不让用户作已知价格的仓位精算。
```

## INV-017

```yaml
id: INV-017
status: sourced
reason: 直接备忘录支持延长 runway 以等待进一步验证的决策节点。
event: Twilio 2009 seed 延长融资建议
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
phase2_conditions: 保持种子期验证范围，不使用上市后成绩。
```

## INV-018

```yaml
id: INV-018
status: sourced
reason: 同期投资备忘录明确 Series B 身份和餐厅 POS/支付场景。
event: Toast 2015 首轮机构融资建议
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
phase2_conditions: 讨论特定餐厅条件下的切换成本，不能由支付绑定推导唯一正确选择。
```

## INV-019

```yaml
id: INV-019
status: blocked
reason: 检索主要得到轮次数据库与二手报道，未找到足以支持同期金融责任、团队和实际轮次的直接材料。
event: Stripe 2011 种子融资尽调
cutoff: 2011 年候选种子轮；确切日与可知材料未核实
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 早期轮次、产品上线时间、合规责任分配与运营证据均待核。
sources:
- id: S1
  url: https://stripe.com/newsroom
  publisher: Stripe
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 检索 site:stripe.com 2011 funding seed；未找到所需同期融资正文。
- 检索结果含 https://techcrunch.com/2011/03/28/stealth-payment-startup-stripe-paypal/ ，未把摘要当核验。
phase2_conditions: 不以创始人后来的名声替代当时证据。
```

## INV-020

```yaml
id: INV-020
status: blocked
reason: 已尝试不同 SEC 招股书版本，但正文超过读取上限；核心股本和经营数字未逐项确认。
event: Nubank 2021 IPO 估值
cutoff: 2021-12 IPO 定价前
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 完整股本、价格与单位经济口径未核。
sources:
- id: S1
  url: https://www.sec.gov/Archives/edgar/data/1691493/000119312521352703/d213207d424b1.htm
  publisher: Nu Holdings via SEC
  published_at: '2021-12-08'
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 打开最终招股书得到 Content length is too large。
- 尝试 https://www.sec.gov/Archives/edgar/data/1691493/000119312521347503/d213207df1a.htm
  亦未取得正文。
phase2_conditions: 保留数量要求门槛，不凭搜索摘要进行估值。
```

## INV-021

```yaml
id: INV-021
status: blocked
reason: 招股书支持历史平均毛利，但未取得足以分离单个新增客户边际版税的合同输入。
event: Spotify 2018 上市前版税与边际毛利
cutoff: 2018-02-28 F-1 发布后
initial_facts: []
evidence:
- id: E1
  text: 2017 Premium 毛利率为 22%；这不是新增一位订阅者的边际毛利。
  source_ids:
  - S1
  availability: pre_decision
- id: E2
  text: 公司将毛利改善部分归于 2017 新授权协议；部分合同细节保密。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  text: 披露的 Premium 毛利率由 2015 年 15% 变为 2017 年 22%，不能由此确认单客边际成本。
  source_ids:
  - S1
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 边际版税、最低保证与客户归属成本未知。
sources:
- id: S1
  url: https://www.sec.gov/Archives/edgar/data/1639920/000119312518063434/d494294df1.htm
  publisher: Spotify via SEC
  published_at: '2018-02-28'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
  - E2
  - outcome
attempts:
- 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
phase2_conditions: 建议使用预列边界判断备用题；未自动更改主动作。
```

## INV-022

```yaml
id: INV-022
status: sourced
reason: 直接投资 memo 包含当时网络规模、收入和交易建议。
event: LinkedIn 2006 投资建议与商业化尽调
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
phase2_conditions: 只选择继续尽调门槛，不把注册用户数直接等同付费网络效应。
```

## INV-023

```yaml
id: INV-023
status: sourced
reason: 当事方公告区分新融资、旧股收购和原承诺加速；可训练不把名义总额等同公司现金。
event: WeWork 2019 年救助融资的现金与控制分离
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
phase2_conditions: 训练解释救助结构；若要求执行结果或现金 runway，须补资料。
```

## INV-024

```yaml
id: INV-024
status: sourced
reason: 直接领投方同期文章支持资本与团队条件，后续同方记录可单独核对产品发布结果。
event: Mistral 2023 seed 后需求验证选择
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
  text: 2023-12-11 领投方后续公告记录 Mistral 7B、Mixtral 与 API 已发布及后续 A 轮；这不能提前用于 seed 判断，也不等于付费
    PMF 已证实。
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
phase2_conditions: 只选择需求验证里程碑，不估未知现金 runway；后续产品成绩只能最终揭晓。
```

## INV-025

```yaml
id: INV-025
status: sourced
reason: 同期公司公告确认 3100 万美元 C 轮、当时集成和客户使用描述。
event: Datadog 2015 Series C 融资与集成价值
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
phase2_conditions: 只讨论壁垒条件和可复制部分，不讲四年增长。
```

## INV-026

```yaml
id: INV-026
status: blocked
reason: 已读 bookings 与递延定义，但尚未逐项核准股本和可用价格，不能完成估值区间。
event: Roblox 2021 直接上市前估值口径
cutoff: 2021-02-11 S-1/A 披露后，上市前
initial_facts: []
evidence:
- id: E1
  text: Bookings 由收入、递延收入变动和其他非现金调整构成，不能直接当期利润。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  text: ''
  source_ids: []
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 完全稀释股本、上市前可见进入价格及递延期限尚待逐项复核。
sources:
- id: S1
  url: https://www.sec.gov/Archives/edgar/data/1315098/000119312521038726/d87104ds1a.htm
  publisher: Roblox via SEC
  published_at: '2021-02-11'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
attempts:
- 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
phase2_conditions: 保留 blocked，不能借上市后的参考价格回填。
```

## INV-027

```yaml
id: INV-027
status: blocked
reason: 官方 2017 中期财务报告可访问，但不足以取得拟选 cohort 的 CAC、复购、履约损耗和回收时序。
event: HelloFresh 2017 资本窗口 cohort 回收
cutoff: 2017 上市窗口，精确截止日待核
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 同 cohort CAC、订单贡献、损耗与回收窗口未齐。
sources:
- id: S1
  url: https://ir.hellofreshgroup.com/media/document/75c35bcd-d012-41c4-ada3-a2955514dc16/assets/HelloFresh_FS_website_FINAL.pdf?disposition=inline
  publisher: HelloFresh
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 打开官方 publications 页面并进入 2017 H1 财务报表；已确认 4 页报表可读，尚未取得所需 cohort 表。
phase2_conditions: 不能用 Blue Apron 或不同年份的数字填空。
```

## INV-028

```yaml
id: INV-028
status: sourced
reason: 直接 memo 支持直播产品和主播行为，不重复 2011 拆分节点。
event: Twitch 2012 投资建议
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
phase2_conditions: 优先选择主播留存或观看证据；不借后来的收购证明 PMF。
```

## INV-029

```yaml
id: INV-029
status: sourced
reason: 公司同期融资公告确认独立 A 轮和参与者，任务可限定下一项验证而非精确投资定价。
event: Coinbase 2013 Series A 之后的运营验证
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
phase2_conditions: 只作条件式继续验证；监管与运营责任仍未知，不拼接不同轮次或精确量化仓位。
```

## INV-030

```yaml
id: INV-030
status: blocked
reason: CEO 原始备忘录经媒体完整转载可核实关闭与当事人解释，但不能支持关闭前现金周期的竞争假说诊断。
event: Convoy 2023 关闭前现金生存诊断
cutoff: 2023-10-19 关闭公告前；缺可用事前现金材料
initial_facts: []
evidence:
- id: E1
  text: CEO 在关闭备忘录中解释货运衰退与资本收缩，并称此前四个月尝试战略选项。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: CEO 于 2023-10-19 宣布关闭当前核心经营，大部分人员离职。
  source_ids:
  - S1
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 应收应付、付款承诺、可融资性及实际现金余额未知；CEO 归因未获独立因果识别。
sources:
- id: S1
  url: https://www.geekwire.com/2023/convoy-collapse-read-ceos-memo-detailing-sudden-shutdown-of-seattle-trucking-startup/
  publisher: Dan Lewis memo reproduced by GeekWire
  published_at: '2023-10-19'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
  - outcome
attempts:
- 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
phase2_conditions: 转载只将标明的 CEO 备忘录作为第一手记录；媒体其余评论不当直接证据。
```

## INV-031

```yaml
id: INV-031
status: blocked
reason: 创始人 2010 讲话支持历史经营模式，但未定位 Phase 2 所要求的早期单次经营选择及其结果。
event: Atlassian 2002–2005 自举经营模式的局部选择
cutoff: 2002–2005 具体扩张决定尚未锁定
initial_facts: []
evidence:
- id: E1
  text: 创始人回顾称早期因无法负担销售团队，采用低价、网站标价及自行下载。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 2010 讲话也描述后续 OEM 尝试失败，但不能将此不同年份事件混入 2002–2005。
  source_ids:
  - S1
  availability: unknown
outcome:
  text: ''
  source_ids: []
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 早期单一决策日、采购条件与独立结果未核实。
sources:
- id: S1
  url: https://businessofsoftware.org/talks/atlassian-from-bootstrap-to-60m-what-ive-learnt/
  publisher: Business of Software / Scott Farquhar
  published_at: '2010'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
  - E2
attempts:
- 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
phase2_conditions: 需要补同期早期节点；不能悄悄换成 2010 OEM 失败。
```

## INV-032

```yaml
id: INV-032
status: blocked
reason: 公司定价公告正文可读，但事前招股书 PDF 读取失败，未核准用于原估值题的财务与股本输入。
event: Reddit 2024 IPO 定价
cutoff: 2024-03-20 定价前
initial_facts: []
evidence: []
outcome:
  text: 公司 2024-03-20 宣布每股 34 美元；2200 万发行股中包含老股，公司不取得老股出售所得。
  source_ids:
  - S1
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 事前完全稀释股本和经营口径尚未逐项核验。
sources:
- id: S1
  url: https://investor.redditinc.com/news-events/news-releases/news-details/2024/Reddit-Announces-Pricing-of-Initial-Public-Offering/default.aspx
  publisher: Reddit
  published_at: '2024-03-20'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - outcome
attempts:
- 实际打开公司定价公告正文。
- SEC 初始推测 URL 返回404；打开 https://d18rn0p25nwr6d.cloudfront.net/CIK-0001713445/73b1cef0-9111-449a-a74e-057d6e7a45e4.pdf
  返回读取错误。
phase2_conditions: 不能先给最终定价当作待预测输入。
```

## INV-033

```yaml
id: INV-033
status: sourced
reason: 招股书包含 cohort、CPC 和贡献定义，足以区分收入回收与实际订单贡献。
event: Blue Apron 2017 上市客户贡献口径
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
phase2_conditions: 可做有来源口径比较和可估边界，不把营收直接算利润。
```

## INV-034

```yaml
id: INV-034
status: blocked
reason: 已找到独立于 PMF 问卷的融资方公告，但只有价格与投资人体验，仍缺付费留存和服务成本 cohort。
event: Superhuman 2019 Series B 与独立付费 cohort
cutoff: 2019-06-27 投资公告后
initial_facts: []
evidence:
- id: E1
  text: 投资人公告说明当时每月 30 美元，并宣布 a16z 领投 Series B。
  source_ids:
  - S1
  availability: pre_decision
outcome:
  text: 2019-06-27 a16z 宣布领投 B 轮；本页并未提供可验证的付费 cohort 单位经济。
  source_ids:
  - S1
interpretation: 只采用来源可支持的披露或当事人判断；不把融资建议当作已实现投资回报。
unknowns:
- 真实付费 cohort、人工 onboarding 服务成本、收入口径与留存未齐。
sources:
- id: S1
  url: https://a16z.com/announcement/superhuman/
  publisher: Andreessen Horowitz / David Ulevitch
  published_at: '2019-06-27'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
  - outcome
attempts:
- 实际打开并阅读上述来源正文；按 Phase 2 单一范围筛选。
phase2_conditions: 保留 blocked 并进入替换审议条件；不复用 PRO080 的 PMF 问卷。
```
