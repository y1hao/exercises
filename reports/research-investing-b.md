# Phase 3 来源核查：INV-044—INV-052

核查日期：2026-10-25。9 条逐项实际浏览：4 sourced、5 blocked；0 ready。sourced 仅表示真实事件或原始文件及其结果/行为有直接来源，不表示已具备训练所需全部数据。规划降级条件、历史可知性与未取得材料逐条保留。

## INV-044

```yaml
id: INV-044
status: blocked
reason: 来源支持同窗 GOV、收入和 GAAP 成本桥，但 pass-through/履约归属分项尚未完整取得；quantitative 主线门槛未闭合，boundary-transfer 仅为待应用规划降级。
event: DoorDash 2020 IPO 前 S-1/A 中的 2019 年全年利润桥
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
  source_ids: *id001
  availability: pre_decision
- id: E2
  text: adjusted cost of revenue 从 GAAP 成本再剔除股权薪酬及分摊管理费用；不能把该口径当全部履约成本。
  source_ids: *id001
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
phase2_conditions:
- 沿用一个 2019 全年利润桥；若要求完整履约成本归属而缺子项，执行 boundary-transfer，讨论责任与成本口径。
```

## INV-045

```yaml
id: INV-045
status: sourced
reason: 已阅读直接来源，支持可辨识事件或原始文件及其披露结果；训练数据完整性与 Case QA 尚待完成。
event: DoorDash 2014 年 5 月 Sequoia 领投 A 轮
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
phase2_conditions:
- 真实轮次已确定为 2014 A；没有独立城市材料，规划要求待正式切换为 evidence-selection。
- 首轮不提供 2015 扩张规模、2020 上市或事后成功判断。
```

## INV-046

```yaml
id: INV-046
status: sourced
reason: 已阅读直接来源，支持可辨识事件或原始文件及其披露结果；训练数据完整性与 Case QA 尚待完成。
event: FTX 2021-07-20 公告的 9 亿美元 B 轮
cutoff: 2021 年 7 月该轮尽调/投资决定前；公开融资公告为同时期 issuer claim
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
phase2_conditions:
- 不编造当轮融资条款或 DD 文件；可索取材料只作为尽调要求，不冒充已存在的历史材料。
- 必须明确托管边界、关联方提款和权限验证；所有调查结论留隐藏证据。
```

## INV-047

```yaml
id: INV-047
status: blocked
reason: 可确认有多笔 bridge/债务修改，但尚未闭合规划要求的最后一笔续命融资身份，且缺完整合同、股本及同时点跑道。
event: Better SPAC 延期期间融资：最后一笔续命融资身份尚未闭合
cutoff: 待定位最后一笔续命融资签署前；不能把 2021 bridge 与 2023 债务修改合成一次交易
initial_facts: []
evidence:
- id: E1
  text: SEC 财务附注披露 2021 年 12 月发行 pre-closing bridge notes，零票息、不可现金偿还，2023-06-30 账面 7.5 亿美元。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 2023 年 2 月信用额度修改将债务分为有担保 AB 和无担保 C；后者还款节奏取决于后续融资承诺。
  source_ids:
  - S1
  availability: unknown
- id: E3
  text: 截至 2023-06-30 bridge 尚未转优先股，附注说明延长到期需同意、章程法律步骤等障碍。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 现有材料说明资本顺位与转换条件确实复杂；没有完整合同和确定决策时点，不能给旧股权精确稀释预测。
unknowns:
- 尚未证明规划所指最后一轮续命融资究竟是哪一笔。
- 未取得该笔完整签署合同、同日 cap table 与可支配现金跑道；不能将信用额度修改等同新增现金。
sources:
- id: S1
  url: https://www.sec.gov/Archives/edgar/data/1835856/000162828023030682/exhibit991-super8xkbetterq2.htm
  publisher: Better Holdco / SEC
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
  - E2
  - E3
attempts:
- 搜索并打开 SEC 2023 二季度财务附注与对应 MD&A，逐段检查 bridge、2023 credit facility 及后续事项。
- 公司 2023 closing 新闻页返回 404；SEC 2023 年报 PDF 与 IR PDF 抓取失败，未用搜索摘要中的 closing 总融资额代替合同。
phase2_conditions:
- 保留 INV-047；先定位最后一笔真实交易及完整合同。
- 缺合同按规划转 evidence-selection；不补造稀释比例、清算优先权或退出价格。
```

## INV-048

```yaml
id: INV-048
status: sourced
reason: 已阅读直接来源，支持可辨识事件或原始文件及其披露结果；训练数据完整性与 Case QA 尚待完成。
event: Palantir 2020-09-21 S-1/A：Acquire / Expand / Scale 交付披露
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
  source_ids: *id001
  availability: pre_decision
- id: E2
  text: 2019 Acquire 客户收入 60 万美元、贡献亏损 6540 万；公司披露的是交付分群而非任意全体客户的平台复制率。
  source_ids: *id001
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
phase2_conditions:
- 只保留 2020 上市前一个公开窗口和两项经营假说；不归纳此后五年资本或股价。
- 贡献毛利为公司定义的非 GAAP 口径，后续 Brief 必须完整说明成本边界。
```

## INV-049

```yaml
id: INV-049
status: blocked
reason: 原始 seed memo 已确认，但可服务 SMB 分母、独立支付证据和服务范围不足；quantitative 主线仍未满足，evidence-selection 尚未正式应用。
event: Wix 2007-10-19 BVP 第二轮 seed 投资建议 memo
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
  source_ids: *id001
  availability: pre_decision
- id: E2
  text: memo 的网站数量和小企业数量是作者引用的市场断言；列举的 5.95 美元到数百美元月费是外部网站托管背景，不是 Wix 实测价格。
  source_ids: *id001
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
phase2_conditions:
- 身份修正为 2007-10-19 第二轮 seed memo，不能写成泛 2008 seed。
- 数量输入不足，按规划应改为 evidence-selection，尚未修改 canonical focus；不得以 memo 市场断言冒充独立实测。
```

## INV-050

```yaml
id: INV-050
status: blocked
reason: 融资身份与借款结果已核，但 4 月 6 日未修订签署合同及融资前现金预测不足，不能完成接受/等待的现金与条款选择。
event: Airbnb 2020-04-06 Silver Lake / Sixth Street 10 亿美元融资
cutoff: 2020-04-06 此笔融资同意前；后来的 4 月 first-lien 交易与 4 月 17 日修订均不并入首轮
initial_facts:
- id: I1
  text: 当时疫情已影响全球旅行；公司融资公告承认严重旅行环境和恢复不确定性。
  source_ids: &id001
  - S1
  availability: pre_decision
- id: I2
  text: 融资拟引入 Silver Lake 和 Sixth Street，公告为 10 亿美元债务与股权证券组合。
  source_ids: *id001
  availability: pre_decision
evidence:
- id: E1
  text: 2020 年报确认 4 月存在两笔各 10 亿美元融资；second-lien 净到款 9.675 亿美元，first-lien 净到款 9.614 亿，不能混为同一笔。
  source_ids:
  - S2
  availability: post_decision
- id: E2
  text: 年报披露 second-lien 的浮息、PIK 选项、担保及 warrants；这些描述含后续修订，不能全部反推为 4 月 6 日原始条款。
  source_ids:
  - S2
  availability: post_decision
outcome:
  text: 该轮融资有同期公告，年报确认 second-lien 实际借款；融资成功不自动回答当时接受融资是否优于等待。
  source_ids:
  - S1
  - S2
interpretation: 现金与条款的选择只能在同日可知信息下评估；后来的 IPO 定价不属于该决定的兜底。
unknowns:
- 未取得 4 月 6 日时点的完整现金预测与未修订签署合同，不能量算等待跑道。
- 4 月 17 日 warrants 修订须单独标时点，不能从 2021 年报回填为最初提议。
sources:
- id: S1
  url: https://news.airbnb.com/silver-lake-sixth-street-partners-invest-1-billion-in-airbnb
  publisher: Airbnb
  published_at: '2020-04-06'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - I1
  - I2
  - outcome
- id: S2
  url: https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm
  publisher: Airbnb / SEC
  published_at: '2021-02-26'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
  - E2
  - outcome
attempts:
- 阅读 4 月 6 日公告和 2020 年报 Loan Agreements / Term Loans，区分 first 与 second lien。
- S-1 过大、S-1/A 与 NYU 镜像抓取失败；年报指向的 4 月 17 日合同修订链接及 SECInfo 镜像抓取失败。
phase2_conditions:
- 真实融资身份已锁定，现金与初始合同仍是制作门槛；不足时保持 blocked，不给数值化接受/等待答案。
- 只用 4 月 6 日一次决定；后续融资、warrants 调整和 IPO 只可作为后置材料。
```

## INV-051

```yaml
id: INV-051
status: blocked
reason: S-1 已核，但个人/团队套餐收入和可归属成本未取得，无法量算独立结构贡献；quantitative 主线仍未满足，evidence-selection 尚未正式应用。
event: Dropbox 2018-02-23 S-1：客户/套餐与公司毛利口径
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
  source_ids: *id001
  availability: pre_decision
- id: E2
  text: 公司说明 2017 成本下降含基础设施优化，仍没有个人/团队套餐收入及可归属成本分解。
  source_ids: *id001
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
phase2_conditions:
- 按批准规划应降为 evidence-selection，尚未修改 canonical focus；量化拆分的缺口须显式保留。
- 与 ENG-150 区分：主问题限定个人/团队和套餐结构，不重复自建存储阈值。
```

## INV-052

```yaml
id: INV-052
status: sourced
reason: 已阅读直接来源，支持可辨识事件或原始文件及其披露结果；训练数据完整性与 Case QA 尚待完成。
event: GitLab 2017-10-09 GV 领投 2000 万美元 C 轮
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
phase2_conditions:
- 锁定 2017 C 轮；主动作仍为一项优先尽调及无付费 PMF 的反例。
- 补齐合同分群前只做证据选择，不从开源人气推导付费需求。
```
