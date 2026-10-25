# Phase 3 产品历史来源核查

逐条实际阅读记录；仅研究素材，不是可执行 Brief。sourced 不代表 ready。retrospective 内容默认时间可用性 unknown。

## PRO-001

```yaml
id: PRO-001
status: blocked
reason: 回顾访谈可确认重做及初版定位，但没有同期用户行为可区分可编程性与上手成本。
event: Notion 早期产品重做（2015—2016）
cutoff: 2015 重做节点；具体轮次未知
initial_facts:
- id: F1
  text: Ivan 回顾初版为无需代码的编程应用。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 回顾称用户兴趣不足，2015 重新设计。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 访谈称团队探索多种设计。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 未见当轮任务观察或分群；不能断言复杂导致失败。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://www.figma.com/blog/design-on-a-deadline-how-notion-pulled-itself-back-from-the-brink-of-failure/
  publisher: Figma / Ivan Zhao 访谈
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不替创始人编造动机或评判全部重做策略
```

## PRO-002

```yaml
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
status: blocked
reason: API 可确认路段比较与排行榜机制，但不能定位早期版本及回访分群/干预。
event: Strava Segment 排行榜（2009—）
cutoff: 早期活动回访窗口未定位
initial_facts:
- id: F1
  text: 官方 API 把 segment 定义为一段道路。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 运动员用时被比较并生成 leaderboard。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: API 区分努力次数和独立运动员数量。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 未给历史回访、未暴露组或实验材料。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://strava.github.io/api/v3/segments/
  publisher: Strava
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不从打开频率直接推断产品创造了留存
```

## PRO-005

```yaml
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
status: blocked
reason: 取得 S-1 定位但正文超读取上限；没有 2008—2011 同区域日期的有效供需数据。
event: Airbnb 房源与旅客匹配（2008—2011）
cutoff: 早期本地窗口未确定
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 地区日期需求、可订房源、转化口径均缺
sources: []
attempts:
- 检索 Airbnb S-1；尝试读取 SEC 2020 S-1/A，返回正文超过 4MB 上限；检索所得 2020 总量不能代替早期本地分布。
phase2_conditions: 建议采用预设的证据选择备用问题（尚未改变focus），选择最高价值供需数据；仍需早期具体事件证据，禁止补合成供需表。
```

## PRO-008

```yaml
id: PRO-008
status: blocked
reason: 2019 S-1 支持免费转付费机制，但不能回填为 2013—2015 的具体采购节点及套餐。
event: Slack 早期企业内部扩散（2013—2015）
cutoff: 2013—2015 指定团队购买窗口未定位
initial_facts:
- id: F1
  text: 2019 S-1 称组织常由 Free 计划开始。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: S-1 把搜索超过 10,000 条与 SSO 列为公司认为的付费原因。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 文件说明团队深度使用与集成后常升级。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 这是公司回顾/2019 定价，缺早期买方权限和预算材料。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不概括三年全部企业扩散史
```

## PRO-009

```yaml
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
status: blocked
reason: 2015 原始研究提供 streak 与继续使用的相关性，未定位改动前后或学习成效。
event: Duolingo 连续学习 Streak 早期设计（2010s）
cutoff: 2015-03-01 至 03-10 观察窗口（非确定的产品改动）
initial_facts:
- id: F1
  text: 研究用连续两天的 streak 日志估计 D 到 D+1 的概率。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 观察窗口为 2015-03-01 至 03-10。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 研究发现 streak 从零到约二十天时继续概率提高。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 研究观察的是继续使用，不能据此推断能力提高或改动因果。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://www.csd.cmu.edu/sites/default/files/phd-thesis/CMU-CS-15-106.pdf
  publisher: Brendan Meeder / CMU
  published_at: '2015-05-04'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不把签到或打开次数作为学习成效
```

## PRO-011

```yaml
id: PRO-011
status: blocked
reason: 当前官方定价可核免费 viewers，但缺 2016—2022 特定历史版收费及权限快照。
event: Figma 免费协作者与编辑席位（2016—2022）
cutoff: 2016—2022 版本未锁定
initial_facts:
- id: F1
  text: 当前官方定价允许免费无限 viewers 查看评论。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 编辑席位和查看能力有区分；当前页面包含后来的产品包。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 当前页面允许链接分享并控制查看/编辑。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 不能把当前价格与后来的席位类型回填到早期。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://www.figma.com/pricing/
  publisher: Figma
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不混用六年套餐或直接推出企业采购成功
```

## PRO-012

```yaml
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
status: blocked
reason: 核查二手增长史后未找到可独立确认操作、许可和转化的一手记录；不能把流传的 Craigslist hack 当事实。
event: 候选 2009—2010 Craigslist 导流；具体日期及操作未确定
cutoff: 未确定，禁止将后来的叙述变成同期已知信息
initial_facts:
- id: F1
  text: 2016 年 Boston Hospitality Review 文章叙述跨发房源及供应招募；它是作者整理，并非平台原始记录。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 文章没有给出同窗口曝光、转化和渠道许可的可核数据。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 仅有公开自报/文档描述；不把发布、相关性或后来的成功当成因果结论。
unknowns:
- 是否及何时部署候选操作、许可、真实转化、终止时间
sources:
- id: S1
  url: https://www.bu.edu/bhr/2016/01/08/the-making-of-airbnb/
  publisher: Boston Hospitality Review / Morgan Brown
  published_at: '2016-01-08'
  source_type: secondary
  checked_at: '2026-10-25'
  supports:
  - F1
  - E1
attempts:
- Airbnb 官方域与创始人采访检索；阅读 Boston Hospitality Review 正文；检索结果中的增长故事未当作一手证据。
phase2_conditions: 保持换题条件；不可据二手叙事自动晋级或替换。
```

## PRO-014

```yaml
id: PRO-014
status: blocked
reason: 官方 Iwata Asks 主站 502，英国迁移 URL 只返回导航；尚未实际读到策略正文。
event: Nintendo Wii 体感大众化战略（2006）
cutoff: 2006 发布前策略点待核
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources: []
attempts:
- 检索 Iwata Asks Wii Hardware；原始 iwataasks.nintendo.com 返回 502；Nintendo UK Introduction 页面实际正文仅导航，未冒充读到访谈。
phase2_conditions: 需恢复官方访谈或可靠原始存档。
```

## PRO-015

```yaml
id: PRO-015
status: blocked
reason: 2015 S-1 证实手作市场定位，未定位早期单一品类的供给约束和买方任务。
event: Etsy 手作卖家社区（2005—）
cutoff: 2005 起的特定品类决策未确定
initial_facts:
- id: F1
  text: S-1 记载 Etsy 于 2005-06 在 Brooklyn 作为手作及 craft supplies 市场成立。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 2015 规则包含手作、vintage、craft supplies；不能回填初创全套规则。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: S-1 把独特商品和人与人的关系作为定位。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 全站 2014 GMS 不能证明早期单品类匹配优势。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不把垂直社区本身当作护城河证明
```

## PRO-016

```yaml
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
status: sourced
reason: 2014 发布直接确认按请求与执行时间收费；负载数据未取得，建议采用预设的风险迁移备用问题，尚未修改focus或认定正式应用。
event: AWS Lambda 2014-11-13 Preview 计费
cutoff: 2014-11-13 公告已知、工作负载选择前
initial_facts:
- id: F1
  text: Lambda 由事件触发代码，AWS 管理计算资源。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 按请求及执行计算时间计费，时间以 100ms 为单位。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 公告列出图片上传、应用活动等触发。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 自动弹性并未移除请求数、运行时间变化带来的账单风险。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 按用量的 Preview 服务推出；未取得同一真实工作负载，不能制作历史账单。
  source_ids:
  - S1
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://aws.amazon.com/about-aws/whats-new/2014/11/13/introducing-aws-lambda/
  publisher: AWS
  published_at: '2014-11-13'
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
phase2_conditions: quantitative_plan fallback 应显式切到 boundary-transfer：按调用收费把哪种费用风险转给客户；不得补负载或发明账单。
```

## PRO-020

```yaml
id: PRO-020
status: blocked
reason: 2013 memo 证实搜索定位，但缺早期历史保留规则、权限及具体知识任务路径。
event: Slack 可搜索团队消息历史（2013—）
cutoff: 2013-07-31 memo；单版历史规则待确定
initial_facts:
- id: F1
  text: Butterfield memo 提出把团队沟通做成可搜索档案。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 他把减少信息负担和利用历史档案视为产品承诺。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: memo 要求 comprehensive and accurate search。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 未给首版保留期限与不同成员访问边界。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://medium.com/@stewart/we-dont-sell-saddles-here-4c59524d650d
  publisher: Stewart Butterfield
  published_at: '2014-02-17'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不泛论所有团队知识和长期粘性
```

## PRO-021

```yaml
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
status: blocked
reason: 取得团队原始发布回顾，但发布价格和首版功能/替代边界尚未从同期一手资料完整核实。
event: Basecamp Hey 邮件产品发布（2020）
cutoff: 2020-06-15 上线前
initial_facts:
- id: F1
  text: REWORK 团队访谈确认 2020-06-15 上线。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 团队称该产品经过两年开发。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 回顾报道上线后的客户支持与 iOS 审核摩擦。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 当前 HEY Way 已包括后续能力，不能当 2020 快照。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://37signals.com/podcast/two-weeks/
  publisher: Basecamp / REWORK
  published_at: '2020-07-28'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不评估整个邮箱市场或把争议当需求证明
```

## PRO-023

```yaml
id: PRO-023
status: blocked
reason: 2009 S-1 说明 ERB 与实时市场如何连接，但未确证 1998—2000 具体版本/先后决策。
event: OpenTable 餐厅端库存系统（1998—2000）
cutoff: 1998—2000 安装餐厅软件到开放市场的节点未锁定
initial_facts:
- id: F1
  text: 2009 S-1 描述 ERB 替代纸质预订，支持现场运营。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 网站连接 ERB 可用库存，线上预约直接写入餐厅系统。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 餐厅收费包含安装、月费和每位线上就座客费用，食客免费。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 公司称逐家销售餐厅软件建立本地库存临界规模；此描述是 2009 版本。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-024

```yaml
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
status: blocked
reason: 创始人回顾确认约会版本和放开上传，但缺同期用户行为与可靠时序；与预设的“用户上传别的内容引发转型”不一致。
event: YouTube 2005 约会版本转通用视频分享
cutoff: 2005 约会版本上线后一周（回忆中的窗口；不认定具体日）
initial_facts:
- id: F1
  text: Steve Chen/Jawed Karim 在 Sequoia 访谈称第一版按约会场景随机展示视频并评分。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: Chen 回忆上线一周没有上传，而非先观察到大量非约会视频。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: Chen 表示放开各种视频上传后也没有立即加速增长。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 回忆称约五月上线；不能把这一日期与四月首视频不加解释地拼成精确时间线。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 仅有公开自报/文档描述；不把发布、相关性或后来的成功当成因果结论。
unknowns:
- 原版发布日、同期上传数据与转型触发的直接记录
sources:
- id: S1
  url: https://sequoiacap.com/podcast/crucible-moments-youtube
  publisher: Sequoia / Steve Chen、Jawed Karim 回顾访谈
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 阅读访谈 From Dating Site to Video Sharing Platform 与后续段落；官方 YouTube 周年文章检索只能确认注册和早期视频。
phase2_conditions: 不得使用“非约会上传已证明新用途”故事；需同期原始材料或明确批准修改训练证据口径。
```

## PRO-026

```yaml
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
status: blocked
reason: 官方生命周期可核最后版本和终止支持；2017 投入决策及理由的一手声明尚未读到。
event: Microsoft Windows Phone 停止投入（2017）
cutoff: 2017 投入终止决策前
initial_facts:
- id: F1
  text: Microsoft 官方把 2017-10 的1709列为 Windows 10 Mobile 最后版本。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 官方随后宣布 2019-12-10 终止支持。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 最后发行与结束安全支持是两个不同日期。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 2017 Belfiore 相关 tweets 仅在二手报道找到，未核原文/存档。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-mobile-end-of-support
  publisher: Microsoft
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-031

```yaml
id: PRO-031
status: blocked
reason: 官方回顾有累积匹配叙事，但缺 2012 同窗口喜欢、匹配和有效对话；fallback 也需早期具体规则。
event: Tinder Swipe 匹配（2012）
cutoff: 2012 版本未取得
initial_facts:
- id: F1
  text: 2024 官方营销文称 2012 上线、两年达十亿 matches。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 营销例子展示已发展关系者的首条消息，属于选择后的成功个案。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 未提供所有匹配的对话率分母。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 2024 个案与累计匹配不能回填到 2012 cohort。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://www.tinderpressroom.com/Real-Messages,-Real-Romance-Tinders-New-Campaign-Inspired-by-Couples-First-Chats
  publisher: Tinder
  published_at: '2024-07-08'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 按计划 fallback 选择行为证据；需补早期 feature 快照，不用合成对话漏斗。
```

## PRO-032

```yaml
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
status: blocked
reason: 2020 S-1 正文超上限且没有 2014—2019 某客户的账单路径与预算，不能判断采用还是治理失效。
event: Snowflake Consumption Model（2014—2019）
cutoff: 指定客户用量窗口未确定
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources: []
attempts:
- 检索 Snowflake S-1 和消费模型；打开 SEC 原文件返回超4MB；后来的投资者演示不能替代早期客户路径。
phase2_conditions: 需真实客户同口径用量和预算证据；不凭公司收入上升归因。
```

## PRO-034

```yaml
id: PRO-034
status: blocked
reason: 2010论文验证机制及延迟，但不能确认服务器/P2P/缓存组合全部属于2008同版；2008题初始信息仍不足，265ms不能回填。
event: Spotify 2008-10 欧洲流式播放上线；2010 性能观察
cutoff: 2008 上线、2010 实测前；265ms 不进入开场
initial_facts:
- id: F1
  text: 论文说明自2008-10 在六个欧洲国家提供服务。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 播放器结合服务器、P2P 和本地缓存提供按需音乐。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 2010 作者实测中位播放延迟为265ms，包含缓存命中。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 该测量不是2008首日数据，也不测感知价值或留存反事实。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://kreitz.se/spotify-p2p10/
  publisher: Gunnar Kreitz、Fredrik Niemelä / IEEE P2P'10
  published_at: '2010-08-27'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-035

```yaml
id: PRO-035
status: blocked
reason: 创始人回述2008采用freemium，但2GB来自访谈时套餐讨论，缺2008准确边界与按任务升级证据；不得回填后来容量。
event: Dropbox 2008-09 发布 freemium 配额
cutoff: 2008 发布套餐已知、某使用任务升级判断前
initial_facts:
- id: F1
  text: Houston 称2008公开发布时已用免费到一定容量、超额收费模式。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 访谈以免费2GB为当时容量边界讨论，非承诺全部后续套餐不变。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 创始人强调定价需预先考虑，给免费后收回会带来损失感。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 同篇承认想靠AB testing/分析校准，未给按任务的升级队列。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://mixergy.com/interviews/drew-houston-dropbox-interview/
  publisher: Mixergy / Drew Houston
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不混入推荐奖励或后续团队套餐
```

## PRO-036

```yaml
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
status: sourced
reason: 原投资者保存自己原文，确认出站签名机制；缺同窗口漏斗，建议采用计划里的证据选择备用问题，尚未修改focus。
event: Hotmail 1996—1997 邮件附加推广
cutoff: 推广文案机制已知、扩散结果隐藏；具体上线日未核
initial_facts:
- id: F1
  text: Jurvetson 记述免费网页邮件在每封出站消息附加推广。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 最终文案删去建议中的 P.S.，并与用户正文区分。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 作者自报用户快速增长及有限营销支出，但不是完整 cohort 漏斗。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 新用户可继续发带推广的邮件；未给发送、去重曝光、注册和再发送分母。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 签名传播存在；不能算出可靠病毒系数或用累计用户数推出有效留存。
  source_ids:
  - S1
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
- 若来源为事后回顾，仅确认其明确记载的当时已知观察或已实施规则；不把后续效果当作事前可知。
sources:
- id: S1
  url: https://www.flickr.com/photos/jurvetson/10446705354
  publisher: Steve Jurvetson 保存自己的1997/1998原文
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
phase2_conditions: fallback evidence-selection：缺哪个漏斗分母会令传播系数失去意义；精确系数不可计算。
```

## PRO-038

```yaml
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
status: blocked
reason: 找到了2013创始人原文入口但连续500，缺实际阅读的地区密度、等待与成本证据。
event: DoorDash 郊区餐饮配送起点（2013）
cutoff: 2013 郊区初始配送窗口未锁定
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources: []
attempts:
- 检索 Stanley Tang 2013-11-28 原文；带斜杠和不带斜杠 URL 均500；YC公司页仅当下总览，不足以支持早期密度。
phase2_conditions: 不可补订单或成本；fallback constrained-decision 需先取得可核早期路线和等待约束。
```

## PRO-041

```yaml
id: PRO-041
status: blocked
reason: 官方回顾确认2015免费扩展，但尚缺当时安装到首反馈操作快照，设计师原文无法读取。
event: Grammarly 浏览器实时纠错（2015—）
cutoff: 2015 扩展上线；具体版本日未知
initial_facts:
- id: F1
  text: Grammarly 官方回顾把免费 Chrome 扩展发布置于2015。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 扩展和 freemium 转型同时扩大写作支持入口。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 官方称用户覆盖个人邮件、学生作文和专业写作。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 回顾未给首反馈步骤、安装漏斗或当时支持网站清单。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://www.grammarly.com/blog/company/grammarly-12-year-history/
  publisher: Grammarly
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不总结全部写作产品或预设反馈必然有用
```

## PRO-042

```yaml
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
status: blocked
reason: 定位2015 F-1自助销售披露但原文超读取上限，且不能填补2000s具体审批/安全购买场景。
event: Atlassian Jira 自助购买（2000s）
cutoff: 2000s 某采购约束尚未锁定
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources: []
attempts:
- 检索 Atlassian 2015 F-1；尝试读取 SEC filename1.htm 返回超4MB；未把搜索摘要的97%网站成交当同期2000s情境。
phase2_conditions: 不估无来源销售成本或评价全部销售策略
```

## PRO-044

```yaml
id: PRO-044
status: blocked
reason: 官方回顾明确首次测试为 2018，年份不必武断改为 2019；但没有当轮分群、参与与学习结果，无法执行既定区分任务。
event: Duolingo 2018 Leaderboards 初测
cutoff: 2018 首次测试前；具体日未核实
initial_facts:
- id: F1
  text: Duolingo 官方说明首次测试 Leaderboards 在 2018 年。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 官方说明早期为五个 leagues，与后来十个版本不同。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 后来的说明按相似习惯及时区匹配；这是当前描述，不可回填为 2018 规则。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 官方称竞争对许多学习者有效，但没有该试验样本、效应量或学习测量。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 仅有公开自报/文档描述；不把发布、相关性或后来的成功当成因果结论。
unknowns:
- 2018 实验规则、分组、回访分母、能力测量
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
attempts:
- 阅读官方 leagues 说明全文；对照用户讨论但未以讨论作为发布日期依据。
phase2_conditions: 2018 是测试年；不可把后续完整规则或 XP 当学习能力。
```

## PRO-045

```yaml
id: PRO-045
status: blocked
reason: 尚无2010—2011一轮邀请规则及受邀后行为的一手记录；后续开放注册报道不能替代。
event: Pinterest Waitlist 邀请制（2010—2011）
cutoff: 2010—2011 邀请窗口未定位
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources: []
attempts:
- 检索 Pinterest 官方archive/2012开放注册及早期创始人资料；结果以二手报道为主，未取得可读同期邀请规则和回访队列。
phase2_conditions: 不以邀请数和排队长度直接证明 PMF
```

## PRO-046

```yaml
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
status: sourced
reason: 原负责人完整回顾提供30分钟流程、激活定义和明确自选择限制，可考虑计划中的证据选择备用问题，尚未修改focus。
event: Superhuman早期强制30分钟人工onboarding
cutoff: 早期已采用30分钟引导后，判断是否继续强制人工引导；确切年月未公开
initial_facts:
- id: F1
  text: Gaurav Vohra回顾早期扩展阶段要求30分钟人工引导；第一批曾更长，不能把30分钟当最初首版。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 早期客户常已使用Gmail多年，需要迁移工作流并学习快捷键。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 负责人自报超过65%在引导后完全迁移邮件，约为直接进入产品者两倍。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 他明确比较很难控制自选择偏差；到场者与愿自助者不同。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: 人工计划后来扩展并转部分自助；没有可当作同期因果留存提升的随机数据。
  source_ids:
  - S1
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
- 若来源为事后回顾，仅确认其明确记载的当时已知观察或已实施规则；不把后续效果当作事前可知。
sources:
- id: S1
  url: https://review.firstround.com/superhuman-onboarding-playbook/
  publisher: Gaurav Vohra / First Round Review
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
phase2_conditions: 量化所需同期成本、收入和因果激活不足；建议采用预设的evidence-selection备用问题（尚未改变focus），不把文章产能×月费的模型当实际利润。
```

## PRO-050

```yaml
id: PRO-050
status: blocked
reason: 2019 S-1可核免费/付费并行与传播叙述，但可读正文未直接核实40分钟及同版付费时长；2020教育豁免也不能回填2019套餐。
event: Zoom 2019 Basic免费会议限制
cutoff: 2019-03-22 S-1公布套餐后；具体团队是否升级判断前
initial_facts:
- id: F1
  text: S-1说明免费Basic用于体验核心会议能力，群组会议有限时。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 付费提供更长群组会议及管理能力；受邀者可参加他人会议。
  source_ids:
  - S1
  availability: unknown
evidence:
- id: E1
  text: 免费群组会议40分钟限制构成与任务时长相关的升级边界。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 公司把受邀参加会议作为产品触达其他用户的入口；未给这项限制独立实验。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不混入后来套餐或默认所有会议都超过时限
```

## PRO-051

```yaml
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
status: blocked
reason: 2017官方字数实验页面读取404；未取得可读2006原始字符规则和SMS来源。
event: Twitter 初期字数约束（2006）
cutoff: 2006规则节点未核
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources: []
attempts:
- 检索Twitter/X原始字数历史；2017官方Giving-you-more-characters页面搜索可见但打开404，二手Jack引语未代替原文。
phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-056

```yaml
id: PRO-056
status: blocked
reason: 2019 S-1证实fair billing credits，但尚无该版账单活跃定义与触发窗口，不能误用DAU定义。
event: Slack 按活跃成员计费（2013—）
cutoff: 候选单版billing规则未锁定
initial_facts:
- id: F1
  text: S-1称部分付费客户按人数并月/季对账。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 未用满合同人数时可得信用额度抵后续账单，不是现金退款。
  source_ids:
  - S1
  availability: unknown
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
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不把公平感当已观测数据或混用后续条款
```

## PRO-057

```yaml
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
status: sourced
reason: 2010同期供需故障记录直接支持局部时段与车辆位置边界；缺同口径数量，建议采用预设的预测备用问题，尚未修改focus。
event: Uber 2010-11 Samasource活动需求峰值
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
  text: 局部需求峰值导致无可用车；没有公开足够数值预测每辆车的等待效应。
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
phase2_conditions: quantitative fallback prediction-counterfactual：局部新增供给在什么条件下不缩短等待；不得补请求/车数/价格。
```

## PRO-059

```yaml
id: PRO-059
status: blocked
reason: 原候选摄影售鞋故事只检索到二手MVP复述，未定位原始创始人记录或交易证据。
event: Zappos 先拍摄当地鞋店商品（1999）
cutoff: 1999拍摄本地鞋店试验未核
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources: []
attempts:
- 检索Zappos官方历史与Nick Swinmurn采访；结果多为后来MVP教学文，未找到可实际阅读的原始试验记录。
phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-060

```yaml
id: PRO-060
status: blocked
reason: 未找到2010s单次recurring功能快照与分群/干预；当前帮助页读取失败，不能建立留存归因。
event: Todoist Recurring Tasks（2010s）
cutoff: 2010s版本未锁定
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources: []
attempts:
- 检索Todoist recurring retention和2015版本；当前官方帮助页无法读取，搜索结果中的员工留任与用户留存无关。
phase2_conditions: 不声称存在未核实的独立上线事件
```

## PRO-061

```yaml
id: PRO-061
status: blocked
reason: 定位2021原始S-1含奖励与funded定义，但HTML超上限、优化PDF404，尚无逐条正文核验。
event: Robinhood Referral 免费股票（2015—）
cutoff: 2015—具体奖励轮次尚未锁定
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources: []
attempts:
- 尝试SEC robinhoods-1.htm正文超4MB；投资者优化PDF404；未用二手推广链接填具体历史奖励条款。
phase2_conditions: 缺同窗口有效账户与奖励支出，fallback evidence-selection仍需当轮规则核实。
```

## PRO-062

```yaml
id: PRO-062
status: blocked
reason: 找到Datadog2019 S-1入口但未核具体试用转组织购买的角色和证据，不能用平台总增长替代。
event: Datadog 免费试用到企业监控（2010—2019）
cutoff: 具体试用采购节点未确定
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources: []
attempts:
- 检索Datadog官方IR/S-1；候选SEC URL不可读，官方IR索引只给文件元数据；未把搜索误返Fastly招股书当Datadog。
phase2_conditions: 不压缩九年扩张为单一故事
```

## PRO-063

```yaml
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
status: sourced
reason: 2018 F-1有免费/付费双层及2015—17分部经济性，可做边界判断；无单cohort完全成本与转化反事实。
event: Spotify 2017广告免费与Premium经济性
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
  text: 广告分部2017由负毛利转正；不能推出每个免费用户可持续盈利。
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
phase2_conditions: 建议采用预设的boundary-transfer备用问题（尚未改变focus）；若后续恢复数量题，需匹配收入、用户期均分母及完整许可成本，不把60%当转化率。
```

## PRO-065

```yaml
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
status: blocked
reason: 同期公告确认垂直产品与迁移流程，但未找到拆分前游戏内容相对其他类别的集中度或行为比较，不能验证识别高价值子群的关键前提。
event: Twitch 从 Justin.tv 拆分（2011）
cutoff: 2011-06-06公开beta发布
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
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-068

```yaml
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
status: blocked
reason: 整合公告验证身份、粉丝和内容自动迁移，但未取得迁移后创作者持续发布或流失行为材料；不能用自动升级等同预期创作者迁移。
event: TikTok 收购 Musical.ly（2017—2018）
cutoff: 2018-08-01整合公告；网页标注08-02
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
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不同时评价收购价格、算法和全球扩张
```

## PRO-070

```yaml
id: PRO-070
status: blocked
reason: 官方首年回顾明确2016-09-28发布多人编辑及设计评审用途，但未取得一场具体远程评审的参与任务、光标位置及可观察协调行为；不能用泛称协作代替单场材料。
event: Figma 多人光标（2016—）
cutoff: 2016-09-28多人编辑发布
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
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不估没有来源的沟通工时或转到企业采购
```

## PRO-071

```yaml
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
status: blocked
reason: 当期发布核实Enterprise的SCIM与SSO，但列客户名称没有真实采购阻碍与买方验证过程，尚不满足单项安全采购节点。
event: Notion Enterprise 安全功能（2020—）
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
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不列完整大型企业安全清单
```

## PRO-073

```yaml
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
status: blocked
reason: 2018 S-1回述2015迁移与客户损失，但缺公告窗口单一服务品类的供需和账户迁移规则，不能由总市场规模替代品类流动性。
event: Upwork Elance 与 oDesk 合并（2013—2015）
cutoff: 2015-05 Upwork重启、8月迁移前
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
  text: ''
  source_ids: []
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
attempts:
- 实际阅读S-1迁移及核心客户章节；2015官方重启公告正文403，不将摘要当核实。
phase2_conditions: 不评价两年全部整合或全部服务市场
```

## PRO-076

```yaml
id: PRO-076
status: blocked
reason: 当前帮助文档验证关系与上手路径，但未给历史版本日期，不能将当前默认单向/双向选项回填2018；单工作流仍缺可冻结的历史快照。
event: Notion 数据库视图与关联（2018—）
cutoff: 2018后某历史版本待核实
initial_facts:
- id: F1
  text: 当前官方文档以客户表与购买物品表说明关系。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 当前关系属性让两个数据库的页面相连接。
  source_ids:
  - S1
  availability: unknown
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
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不估没有数据的留存提升
```

## PRO-077

```yaml
id: PRO-077
status: blocked
reason: 找到 2013 App of the Year 认可，但未找到具体排名驱动活动、时序及曝光行为数据。
event: 候选 Duolingo 2010s App Store 排名活动（未定位）；已确认 2013 获奖
cutoff: 活动未定位
initial_facts:
- id: F1
  text: CMU 同期文章报道 Duolingo 获 Apple 2013 App of the Year。
  source_ids:
  - S1
  availability: unknown
- id: F2
  text: 文章报告累计下载及月活；均非某次排名冲击的实验数据。
  source_ids:
  - S1
  availability: unknown
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
  text: ''
  source_ids: []
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
attempts:
- 官方博客及同期 CMU 检索；阅读 CMU 正文；未用下载总量替代渠道归因。
phase2_conditions: 不把获奖故事替代计划中的可观察渠道活动。
```

## PRO-078

```yaml
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
status: blocked
reason: 2016 S-1验证试用、API及采购角色，但没有一个具体早期集成从开发者交接到采购的过程；不能用八年developer-first总述代替节点。
event: Twilio Developer-first API（2008—2016）
cutoff: 2016-10-07公开披露所述当前模式
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
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不总结八年 developer-first 战略
```

## PRO-082

```yaml
id: PRO-082
status: blocked
reason: 已读同期报道及其原帖链接，但官方X博客与CEO原帖正文抓取失败，且没有品牌识别或广告信任行为测量；不足以核实计划要求的品牌结果。
event: Twitter 改为 X 的品牌重塑（2023）
cutoff: 2023-07品牌更名窗口
initial_facts:
- id: F1
  text: 同期MacRumors观察网页版鸟标被临时X替代；这是次级现场报道。
  source_ids:
  - S1
  availability: pre_decision
- id: F2
  text: 同日报道当时官方app仍叫Twitter，不能假定所有界面同步更名。
  source_ids:
  - S1
  availability: pre_decision
evidence:
- id: E1
  text: 报道链接CEO关于更名和综合应用愿景的推文。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 报道转述综合应用愿景并引用原帖；该转述不能证明广告客户信任的实际变化。
  source_ids:
  - S1
  availability: post_decision
outcome:
  text: ''
  source_ids: []
interpretation: 机制可作待检验预测；发布公告不证明采用、留存或因果效应。
unknowns:
- 内部决策材料、反事实与独立效果测量未公开
sources:
- id: S1
  url: https://www.macrumors.com/2023/07/24/TWITTER-REBRANDED-AS-X/
  publisher: MacRumors / Tim Hardwick
  published_at: '2023-07-24'
  source_type: secondary
  checked_at: '2026-10-25'
  supports:
  - F1
  - F2
  - E1
  - E2
attempts:
- 实际阅读MacRumors正文；打开其CEO原帖链接失败；打开X年终官方博客失败。
phase2_conditions: 保留既定单一认知动作；结果仅最终揭晓。
```

## PRO-083

```yaml
id: PRO-083
status: blocked
reason: 2008协作功能与复用路径有同期原文，但未取得一次具体跨项目贡献关系闭环；功能存在不足以证明难迁移贡献网络。
event: GitHub 开源贡献网络（2008—）
cutoff: 2008-12 Fork Queue推出时
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
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不把开源人气或仓库数当护城河
```

## PRO-084

```yaml
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
status: blocked
reason: 2019 S-1有受邀者转host的公司叙述及大客户免费起点统计，但未取得同版首次主持身份步骤和受邀转主持行为分母；不能把大客户55%当受邀者转化率。
event: Zoom 会议邀请链接传播（2013—2020）
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
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不重复 PRO-094 的下载注册摩擦判断
```

## PRO-086

```yaml
id: PRO-086
status: blocked
reason: 2020官方解释验证无关注图的新用户输入和推荐流程，但未取得首轮分群/行为比较，不能用全站主要停留在For You替代冷启动假说证据。
event: TikTok For You 默认推荐流（2018—2020）
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
  text: ''
  source_ids: []
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
attempts:
- 检索并实际阅读所列来源正文；未把搜索摘要作为已验证材料。
phase2_conditions: 不以之后全站使用时长证明初期因果
```

## PRO-098

```yaml
id: PRO-098
status: blocked
reason: 确认 2021 beta 和具体设备流程；2024 改动仅取得行业报道，未取得原始改动说明或用户行为材料，不能推断失败原因。
event: Horizon Workrooms 2021 beta；候选 2024 精简改动待一手核实
cutoff: 候选 2024 改动之前；确切日未验证
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
  text: 2024-05-30 UploadVR 报道删白板等并简化流程；为二手观察，不能当内部动机。
  source_ids:
  - S2
  availability: post_decision
outcome:
  text: ''
  source_ids: []
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
- id: S2
  url: https://www.uploadvr.com/horizon-workrooms-overhaul/
  publisher: UploadVR / David Heaney
  published_at: '2024-05-30'
  source_type: secondary
  checked_at: '2026-10-25'
  supports:
  - E2
attempts:
- 阅读 Meta 发布正文和 UploadVR 更新报道；检索 Meta 2024 原始变更未得可核正文。
phase2_conditions: 候选“方向调整”不可当已证实失败归因；正式锁定决策需原始改动材料。
```
