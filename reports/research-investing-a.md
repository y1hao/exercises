# Investing primary-source research — INV-035–043

Checked 2026-10-25. Research notes only; no ready promotion. All nine IDs were individually attempted. `availability` describes the historical cutoff; disclosure timing is a separate Phase4 concern. Precise cohort payback or share economics are not manufactured when inputs are missing.

## INV-035

```yaml
id: INV-035
status: sourced
reason: 2017-09-21 MongoDB S1直接记录AGPL、免费/付费转化、Atlas商业结果与云竞争；不用2018 SSPL或2019 DocumentDB倒灌。
event: MongoDB 2015—2017 融资
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
phase2_conditions:
  revision_state: awaiting_source
  policy_path: curriculum/planning-policy.yaml
  distinctness_clusters:
  - ME-16
  planned_exercise:
    planning_only: true
    anchor_request: 拟选 MongoDB 2017 资本窗口
    anchor_status: unverified_research_target
    main_question: 开源采用在哪些条件下不能由公司捕获付费价值？
    expected_output: 一个价值捕获边界及竞争反例
    evidence_to_verify:
    - 当时托管和部署规则
    - 替代者
    - 客户付费材料
    out_of_scope: 不把后续许可变化当当时竞争前提
```

## INV-036

```yaml
id: INV-036
status: blocked
reason: 2014原始融资公告确认SeriesB及累计26m，但所需客户采购任务/替代决策证据未取得；不能把厂商90%成本宣传当实测。
event: Snowflake 2012—2014 早期融资
cutoff: 2014 SeriesB融资决策前，具体可知客户材料未定；公告日不自动等于轮次关闭日。
initial_facts:
- id: F1
  text: Snowflake公告其从隐身状态公开云原生Elastic Data Warehouse。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 公开宣称结合SQL数据仓库、big-data灵活性及云弹性。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 公告称最近SeriesB由Redpoint领投，Sutter Hill及Wing参与。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 26m是累计融资，不是据该源已证明这一轮单独26m。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 技术/成本优势为厂商宣传及投资人评价，非独立客户证据。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 没有同期客户采购、合同或替换工作负载证据。
- 产品链接点击失败，未引入2020招股书的后期客户作为2014事前信息。
sources:
- id: S1
  url: https://www.globenewswire.com/news-release/2014/10/21/1186817/0/en/snowflake-raises-26m-in-funding-to-reinvent-the-data-warehouse.html
  publisher: Snowflake Computing / Marketwired
  published_at: '2014-10-21'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- url: https://www.globenewswire.com/news-release/2014/10/21/1186817/0/en/snowflake-raises-26m-in-funding-to-reinvent-the-data-warehouse.html
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  revision_state: awaiting_source
  policy_path: curriculum/planning-policy.yaml
  distinctness_clusters: []
  planned_exercise:
    planning_only: true
    anchor_request: 拟选 Snowflake 2014 早期融资，身份待核
    anchor_status: unverified_research_target
    main_question: 哪项客户证据能区分新市场需求与单纯技术升级？
    expected_output: 一个优先验证项及拒绝条件
    evidence_to_verify:
    - 真实轮次
    - 当时产品
    - 既有数仓替代与采购任务
    out_of_scope: 不泛谈云转型或使用后来的市场规模
```

## INV-037

```yaml
id: INV-037
status: sourced
reason: 2021-11-01 S1/A提供事前价格区间、股本、产能、已交付量与capex；最终IPO另有原招股书支持。
event: Rivian 2021 IPO 估值
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
phase2_conditions:
  revision_state: retained
  policy_path: curriculum/planning-policy.yaml
  distinctness_clusters: []
  quantitative_plan:
    mainline_measure: 产能达成约束的价值范围
    required_inputs:
    - IPO 前价格、股本、产能与资本开支
    - 可证公开假设
    missing_input_fallback:
      focus: evidence-selection
      question: 哪项产能或稀释证据最能推翻当前价格隐含的假设？
    fallback_applied: false
    input_verification: not_started
```

## INV-038

```yaml
id: INV-038
status: sourced
reason: 2019 Peloton原S1/A直接给净CAC计算及贡献口径；缺同cohort完整成本/留存，按既定evidence-selection fallback。
event: Peloton 2018—2019 Pre-IPO
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
phase2_conditions:
  revision_state: awaiting_source
  policy_path: curriculum/planning-policy.yaml
  distinctness_clusters: []
  planned_exercise:
    planning_only: true
    anchor_request: Peloton 2019 上市前一份硬件加订阅 cohort
    anchor_status: unverified_research_target
    main_question: 硬件带来的订阅收入需要多久覆盖获客投入？
    expected_output: 一个口径一致的回本边界
    evidence_to_verify:
    - 硬件毛利
    - 获取成本
    - 订阅贡献与留存窗口
    out_of_scope: 不把硬件收入和订阅收入重复计为收益
  quantitative_plan:
    mainline_measure: 硬件获客的回本窗口
    required_inputs:
    - 硬件毛利、获取成本、订阅贡献与同 cohort 留存
    missing_input_fallback:
      focus: evidence-selection
      question: 缺哪项硬件或订阅成本会让回本判断方向错误？
    fallback_applied: false
    input_verification: not_started
```

## INV-039

```yaml
id: INV-039
status: sourced
reason: Canva2015创始人融资原文可读，支持用户分群、Work采用与融资结果；付费留存未知正好限定尽调问题。
event: Canva 2013—2015 早期融资
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
phase2_conditions:
  revision_state: awaiting_source
  policy_path: curriculum/planning-policy.yaml
  distinctness_clusters: []
  planned_exercise:
    planning_only: true
    anchor_request: 拟选 Canva 2015 一轮融资，身份待核
    anchor_status: unverified_research_target
    main_question: 下一项什么证据能说明非设计师需求具有付费广度？
    expected_output: 一个分群尽调选择
    evidence_to_verify:
    - 轮次
    - 当时产品
    - 非设计师留存与合同或支付信号
    out_of_scope: 不重复产品题的模板价值假说
```

## INV-040

```yaml
id: INV-040
status: blocked
reason: Quibi创始人2020关闭原信已读，真实停止投入可核；数量校准所需现金、承诺支出及退出回收未公开。
event: Quibi 2020 关闭
cutoff: 2020-10-21wind-down决策之前，具体现金/承诺成本输入缺失。
initial_facts:
- id: F1
  text: Quibi为mobile-first premium内容服务。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 创始人声明仍有部分现金runway并考虑过pivot等选项。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 公开信称已穷尽可选方案。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 团队宣布wind down并向股东返还现金，而非持续耗尽所有资金。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 穷尽选项及失败理由为管理层自述，不是独立证实每种pivot不可能。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 确切现金余额、内容合同不可取消承诺、员工结算和资产出售回收缺失。
- 不能把媒体估算数或1.75bn累计融资当关闭日现金余额。
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
attempts:
- url: https://quibi-hq.medium.com/an-open-letter-from-quibi-8af6b415377f
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  revision_state: retained
  policy_path: curriculum/planning-policy.yaml
  distinctness_clusters: []
```

## INV-041

```yaml
id: INV-041
status: blocked
reason: 2015官方融资说明已读，但规划明确2014轮次决策边界；该文2015网络/产品指标不能回填2014。
event: Cloudflare 2014—2019 融资
cutoff: 拟选2014一轮融资，但关闭日及该时点业务指标未由一手材料锁定。
initial_facts:
- id: F1
  text: 2015公告称新融110m来自Fidelity、Google、Microsoft、Baidu、Qualcomm及原投资者。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 该文对比2012融资时23城市网络与2015的62城市网络。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 2015文章称覆盖约4m Internet properties及近每月1trillion page views。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 作者称本轮无特殊控制、董事席位、经济待遇或信息权；这是公司自述，不等于完整交易合同。
  source_ids:
  - S1
  availability: unknown
outcome:
  id: O1
  text: ''
  source_ids: []
  availability: post_decision
interpretation:
  text: 规模不是自动可防守的经济优势；不能引入后续Workers/现代安全产品。
  source_ids:
  - S1
  attribution: 维护者对原始材料的范围判断；技术或事故因果归属于来源作者，不代表独立复现实验
unknowns:
- 2014关闭原记录、同期免费/付费用户、单位成本与转化数据。
- 二手报道称2014年12月已关闭，但本笔记未将其升级为一手核实结论。
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
attempts:
- url: https://blog.cloudflare.com/why-we-raised-110m-from-fidelity-google-microsoft-baidu-and-qualcomm/
  result: 已实际打开并读取正文；来源范围与缺口见 reason / unknowns
phase2_conditions:
  revision_state: awaiting_source
  policy_path: curriculum/planning-policy.yaml
  distinctness_clusters: []
  planned_exercise:
    planning_only: true
    anchor_request: 拟选 Cloudflare 2014 一轮融资，身份待核
    anchor_status: unverified_research_target
    main_question: 免费流量与网络规模在哪种条件下才构成防守优势？
    expected_output: 一个壁垒判断及失效条件
    evidence_to_verify:
    - 该轮业务范围
    - 网络与客户口径
    - 价值捕获证据
    out_of_scope: 不混入后来六年的全部安全与开发者产品
```

## INV-042

```yaml
id: INV-042
status: sourced
reason: Zoom2013同期公司融资稿有产品、企业采用与价格，适合选择企业采用反证。
event: Zoom 2013—2015 融资
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
phase2_conditions:
  revision_state: awaiting_source
  policy_path: curriculum/planning-policy.yaml
  distinctness_clusters: []
  planned_exercise:
    planning_only: true
    anchor_request: 拟选 Zoom 2013 一轮早期融资，身份待核
    anchor_status: unverified_research_target
    main_question: 哪项企业采用证据最能反驳成熟竞争者足以满足需求？
    expected_output: 一个优先验证项及拒绝条件
    evidence_to_verify:
    - 当轮产品
    - 移动或会议体验
    - 企业采购信号
    out_of_scope: 不由后来赢家结果证明当时应下注
```

## INV-043

```yaml
id: INV-043
status: sourced
reason: 两份同期公司融资公告核实45.6bn→6.7bn及2022common equity；缺股本/全权利，建议审议预设boundary-transfer
  fallback。
event: Klarna 2021—2022 估值重定价
cutoff: 2021-06-10融资后、2022新融资宣布前；两轮比较材料只能在后续揭示。
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
phase2_conditions:
  revision_state: retained
  policy_path: curriculum/planning-policy.yaml
  distinctness_clusters: []
  quantitative_plan:
    mainline_measure: headline 估值与旧股经济价值差异
    required_inputs:
    - 两轮实际价格和股本
    - 公开股权权利
    - 稀释口径
    missing_input_fallback:
      focus: boundary-transfer
      question: 为什么缺少股权权利时，不能从融资估值比例推出旧股价值变化？
    fallback_applied: false
    input_verification: not_started
```
