# Phase 3 来源验证

核查日期：2026-10-25。全部 313 个历史条目均已逐项尝试，状态与理由见下表和相应研究记录。52 个微设计仍是 candidate。没有 ready 条目，未进入 Phase 4。

| 领域 | sourced | blocked | rejected |
|---|---|---|---|
| engineering | 115 | 41 | 1 |
| product | 48 | 56 | 0 |
| investing | 24 | 28 | 0 |

合计：187 sourced、125 blocked、1 rejected。sourced 仅表示已定位并阅读支持所选节点的可信直接材料，未通过完整 Brief QA。

## 事实与时点边界

`research` 保存核源素材，不能作为 Consumer 的 opening。availability 是历史可知性，不能代替 Phase 4 的证据释放时机；post_decision/unknown 不能进入事前开场。cutoff 可以是明确的事务、版本或产品决策边界；需要精确日的案例在 Phase 4 固定，无法固定的不得 ready。

投资 memo 的投资建议、公司融资公告、设计论文的实现描述分别是所观察的文档或行为；不能说成交易已经交割、投资已实现回报或经过独立复现。事后当事人记录须保留叙事局限。部分来源日期不详，published_at 为 null；未补造日期。

Phase 2 的 review_status、revision_state 和 planning 是规划历史快照；当前核源状态以 canonical status 与 research 为准。原候选标题和 candidate_material 保留，研究 event 记录纠正后的锚点，尚未自动改号、改日期、改 focus 或应用备用题。

## 需要重点处理的身份和替换

- ENG-011 与 ENG-040 已分开核对：2024 与 2023 不同供电事故；不得混写成同一事件。

- ENG-054：Google 2012 闰秒候选归属存疑；不能把其他公司的 Linux 故障写成 Google 故障。

- ENG-080：2015 Bazel 发布时的远程缓存有路线图边界，不能写成所有能力当时已经提供。

- ENG-117：尚未取得规划要求的单次 SSD 优化；保留 blocked，进入替换审议。

- ENG-157：原 Blaze 候选因与 ENG-080 重复而 rejected；研究记录中的 Rust 1.52 回退提案仅是提案，尚未替换原日期槽。

- INV-005：2005 Yelp memo 指此前天使融资后的首次风险融资，原“Series B”标签不可靠。INV-010：核实到的是 2015 Figma Series A/Preview，未确认原拟选 2016 独立轮次。

- INV-034：找到 2019 a16z B 轮公告，仍缺独立付费留存及服务成本 cohort；不能复用 PRO-080 PMF 问卷补足，保留 blocked 并待替换审议。

- PRO-013/025/044 等传播故事、年份或因果主张需按逐条记录处理，不因广为流传就升级。

## 阻塞处理与后续

blocked 包括读取失败、实际年份/版本未固定、缺同期行为、关键数值或条款不可核，以及规划节点与来源不符。它表示本轮未核实，不能据此断言资料不存在。每条 attempts 记录本轮实际尝试及限制，未打开的搜索摘要未当成已核事实。

数量题只保留来源支持的口径；缺输入条目仍有 Phase 2 备用问题可审议，但本轮未自动应用，不能靠合成数字补主线。所有 blocked/rejected 保留当天槽位，待补源或显式修订。

本脚本是离线引用、覆盖与同步检查，不能自动证明 URL 可访问、主张正确、无剧透或对话可运行。Phase 4 须再次核对具体要进入开场/证据池的主张，完善出处定位和时间线，再进行完整 Case QA。

## 39 条数量主线复核

按 Phase 2 的原问题检查输入齐备性，2 条可进行有边界的数量比较，37 条本轮未核齐。即使找到了可信机制或融资材料，缺原数量主线输入且尚未正式应用备用问题的条目仍为 blocked。研究笔记的原建议状态保存在 source_assessment_status；索引采用复核后的有效状态。

| ID | 数量输入状态 | 复核理由 |
|---|---|---|
| INV-001 | sufficient_for_scoped_comparison | 已读取公开事前价格区间、股本和业务分项；只能做有明确口径的区间比较，不推定折现率。 |
| INV-002 | insufficient_this_round | 招股书正文读取失败，同窗口广告与交易的归属成本未核实。 |
| PRO-007 | insufficient_this_round | 缺早期同地区日期的有效供需和匹配分布。 |
| INV-009 | insufficient_this_round | 公司贡献口径不能替代同城市或同 cohort 补贴和履约数据。 |
| ENG-028 | insufficient_this_round | 有采样机制，缺特定故障频率与独立性，不能算漏采概率。 |
| PRO-019 | insufficient_this_round | 有发布时计价规则，但缺同一有来源工作负载的调用与执行时间。 |
| ENG-039 | insufficient_this_round | 有总连接与资源测量，但缺连接占用成本分解，不能估连接复用的独立贡献。 |
| INV-015 | insufficient_this_round | 未核定对应融资进入时点及同城市收入、补贴、履约成本。 |
| PRO-031 | insufficient_this_round | 缺同期喜欢、匹配和有效对话的可比较数量。 |
| ENG-050 | insufficient_this_round | 有消息及批次基准，缺等待分布和到达工作量，不能精算延迟代价。 |
| ENG-056 | insufficient_this_round | 关系查询可核，REST 对应端点与分页未齐，不能比较精确请求数。 |
| PRO-037 | insufficient_this_round | 有签名机制记录，缺同期发送到注册再发送的完整漏斗。 |
| INV-020 | insufficient_this_round | 原文读取受限，IPO 股本和客户风险成本未逐项核实。 |
| PRO-040 | insufficient_this_round | 原文访问失败，缺同区路线、等待、订单与配送成本。 |
| INV-021 | insufficient_this_round | 历史平均毛利不能代替新增订户边际版税；合同输入不足。 |
| PRO-049 | insufficient_this_round | 有人工作业流程，缺可归属成本和同窗口激活收益，无法回本计算。 |
| ENG-075 | insufficient_this_round | 已定位去重机制，缺实际重复键分布及页面尺寸。 |
| INV-026 | insufficient_this_round | 递延定义可核，但股本、事前可见价格与期限未完成抽取。 |
| INV-027 | insufficient_this_round | 官方报表未提供已核实的同 cohort CAC、复购、贡献和损耗输入。 |
| ENG-084 | insufficient_this_round | Open Connect 发布可核，缺同地区命中率及交付、部署完整成本。 |
| PRO-058 | insufficient_this_round | 同城时段供需现象可核，缺同口径等待、价格、车辆与交易量。 |
| PRO-061 | insufficient_this_round | 申报入口存在但正文读取失败；奖励支出和有效持续账户尚未逐项核实。 |
| INV-032 | insufficient_this_round | 定价结果可核，事前完整财务与稀释股本尚未抽取。 |
| PRO-064 | insufficient_this_round | 分部经济性可核，缺可归属成本和同一转化口径来回答原数量问题。 |
| INV-033 | insufficient_this_round | 招股书有 cohort 收入与贡献，但 94 美元 CPC 采用更广的累计获客窗口，不能直接视作同 cohort CAC；原回本主线缺匹配输入。 |
| INV-034 | insufficient_this_round | 独立融资记录可核，缺 PMF 问卷之外的付费留存和服务成本 cohort。 |
| ENG-108 | insufficient_this_round | 只取得摘要，未读到完整尾延迟分布及额外请求工作量。 |
| INV-037 | sufficient_for_scoped_comparison | S-1/A 含事前价格区间、股本、交付及资本开支；不得与最终版股数混算。 |
| ENG-110 | insufficient_this_round | 消息迁移机制可核，缺同窗口总成本、资源、工作量和迁移投入。 |
| INV-038 | insufficient_this_round | 有公司净 CAC 和贡献定义，缺同 cohort 留存及完整现金成本时序。 |
| ENG-117 | insufficient_this_round | 未找到原规划单次 SSD 优化和同负载可归属成本。 |
| INV-043 | insufficient_this_round | 两轮 headline 估值可核，缺完整股本、每股价格和权利，不能推出旧股实际损失。 |
| ENG-128 | insufficient_this_round | 当前文档含后续架构，无法确认 2017 同窗口数据及版本。 |
| INV-044 | insufficient_this_round | 公司总体口径不能替代可归属履约成本；本轮未核齐原数量输入。 |
| PRO-087 | insufficient_this_round | 两版政策价格之外，同一可追溯请求和执行量尚未核齐。 |
| ENG-137 | insufficient_this_round | 缺 2002 接口快照及同口径连接数、就绪事件与性能测量。 |
| INV-049 | insufficient_this_round | 网站总量或作者市场愿景不能等同可服务付费客群和支付意愿。 |
| ENG-150 | insufficient_this_round | 迁移事实可核，缺同口径采购、运维、利用率与存储总成本。 |
| INV-051 | insufficient_this_round | 申报总体毛利不能分解个人和团队业务的完整归属成本。 |

## 逐项核查结果

| ID / Brief | 状态 | 核实事件 / 决策边界 | 理由 / 研究记录 |
|---|---|---|---|
| [ENG-001](../cases/engineering/ENG-001.yaml) | sourced | Google Spanner（2012）；论文设计快照，事务协调者选择提交时间戳之前；不混用 Cloud Spanner 后续实现。 | 2012 原论文直接支持 TrueTime 不确定性与 commit-wait；无须编造时钟采样。（[记录](../reports/research-engineering-a.md#eng-001)） |
| [INV-001](../cases/investing/INV-001.yaml) | sourced | Arm 2023 IPO 定价前的业务和股本评估；2023-09-05 路演公告之后、9 月 13 日最终定价公告之前；最终价不得开场给出。 | 已读取官方 F-1、路演与定价公告，能区分价格区间、业务数据与最终发行价。（[记录](../reports/research-investing.md#inv-001)） |
| [ENG-002](../cases/engineering/ENG-002.yaml) | blocked | BuildKit Docker 分层缓存（2018—）；未锁定 2018 版本；目前只确认 2019 官方教程。 | 已读 Docker 2019 多阶段构建教程，但尚未确认 2018 BuildKit 版本对应 Dockerfile 快照；不得将现行缓存规则回填。（[记录](../reports/research-engineering-a.md#eng-002)） |
| [PRO-001](../cases/product/PRO-001.yaml) | blocked | Notion 早期产品重做（2015—2016）；2015 重做节点；具体轮次未知 | 回顾访谈可确认重做及初版定位，但没有同期用户行为可区分可编程性与上手成本。（[记录](../reports/research-product.md#pro-001)） |
| [ENG-003](../cases/engineering/ENG-003.yaml) | sourced | Slack 2021 年 1 月服务中断；2021-01-04 初始告警、监控面板不可用时；因果解释与修复留到揭晓。 | Slack 当事人复盘提供可排序的观测、自动扩缩容与恢复材料。（[记录](../reports/research-engineering-a.md#eng-003)） |
| [PRO-002](../cases/product/PRO-002.yaml) | sourced | Pinterest 2015 Pin It 保存路径改进；2015-04-02 新版功能已介绍、行为效果尚未揭晓 | 锁定 2015-04-02 按钮改进；官方说明路径和点击变化，足以作任务摩擦预测。（[记录](../reports/research-product.md#pro-002)） |
| [ENG-004](../cases/engineering/ENG-004.yaml) | blocked | Terraform Provider 协议演进（2016—2023）；待选择有日期或 tag 的升级示例；现行 v1.18 文档不可当作早期快照。 | 官方现行状态升级说明已读，但未锁定 2016–2023 范围内的协议/Framework版本。（[记录](../reports/research-engineering-a.md#eng-004)） |
| [INV-002](../cases/investing/INV-002.yaml) | blocked | Instacart 2023 IPO 前订单与广告贡献拆分；拟以 2023 上市前公开报表为界，尚未完整核定。 | 招股书正文读取失败，同窗口广告与交易的归属成本未核实。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing.md#inv-002)） |
| [ENG-005](../cases/engineering/ENG-005.yaml) | blocked | Java ZGC 上线（2018—2023）；2018 JDK11 候选；精确采用时点未核定。 | 尝试读取 JEP 333 两次返回 403；未读取原文，不以搜索摘要核源。（[记录](../reports/research-engineering-a.md#eng-005)） |
| [PRO-003](../cases/product/PRO-003.yaml) | sourced | Adobe Creative Suite 转订阅 CC（2013）；2013 年 5 月宣布后，Q3 结果尚未公开 | 同期 SEC 文件确认转向日期、保留永久授权的边界和后续经营结果；财报收入不等于现金流。（[记录](../reports/research-product.md#pro-003)） |
| [ENG-006](../cases/engineering/ENG-006.yaml) | blocked | Figma Multiplayer 数据模型（2019—）；2019 已连接客户端收到对象更新后、持久化确认未知。 | Figma 2019 原文已读，但不提供文档同步到持久化确认的完整契约，不能完成规划中的确认点判断。（[记录](../reports/research-engineering-a.md#eng-006)） |
| [PRO-004](../cases/product/PRO-004.yaml) | blocked | Strava Segment 排行榜（2009—）；早期活动回访窗口未定位 | API 可确认路段比较与排行榜机制，但不能定位早期版本及回访分群/干预。（[记录](../reports/research-product.md#pro-004)） |
| [ENG-007](../cases/engineering/ENG-007.yaml) | blocked | SolarWinds Orion 供应链攻击（2020）；2020 已签名发布工件的鉴别节点尚未锁定。 | SolarWinds 当事人调查已读，确认构建注入；发布工件签名与来源核验的可操作证据链仍不足。（[记录](../reports/research-engineering-a.md#eng-007)） |
| [INV-003](../cases/investing/INV-003.yaml) | sourced | Fiverr 2011 年 Bessemer 投资建议；2011-01-10 投资建议窗口，以投资方当时记录为限。 | 已读取 Bessemer 2011-01-10 原始投资建议正文；适合检查交易质量证据，不推断后续回报。（[记录](../reports/research-investing.md#inv-003)） |
| [ENG-008](../cases/engineering/ENG-008.yaml) | sourced | Discord Go 垃圾回收瓶颈（2019）；Read States 服务出现周期性抖动、深入归因前；不声称2019精确事故日。 | Discord 原文提供两分钟周期、缓存扫描与调参对照；需修正候选2019为2020公开复盘，服务历史日期未知。（[记录](../reports/research-engineering-a.md#eng-008)） |
| [PRO-005](../cases/product/PRO-005.yaml) | sourced | Dropbox 推荐好友送空间（2008—2010）；推荐方案已说明、演讲的增长结果尚未揭晓 | 创始人演讲原始幻灯片确认双边激励、产品传播与自报注册结果；保留效果识别限制。（[记录](../reports/research-product.md#pro-005)） |
| [ENG-009](../cases/engineering/ENG-009.yaml) | sourced | Raft 论文（2014）；论文 Figure 8 的某次领导者崩溃后、下一次选举前；使用论文原图状态。 | 2014 原论文给出选举限制、日志匹配及旧任期提交反例。（[记录](../reports/research-engineering-a.md#eng-009)） |
| [PRO-006](../cases/product/PRO-006.yaml) | sourced | Nintendo Switch 混合主机（2017）；2017-01-13 公布规格后、正式发售前 | 同期 Nintendo 产品公告描述客厅、桌面、掌机模式及对应任务，足以限定单一使用情境。（[记录](../reports/research-product.md#pro-006)） |
| [ENG-010](../cases/engineering/ENG-010.yaml) | sourced | Go Modules 引入（2018）；2018 MVS 提案中的依赖图、构建列表计算前。 | 设计者2018原文直接定义 MVS 并含依赖图示例。（[记录](../reports/research-engineering-a.md#eng-010)） |
| [INV-004](../cases/investing/INV-004.yaml) | sourced | Shopify 2010 Series A 投资建议；2010-10-12 | 直接投资备忘录包含同期客户、MRR、现金和拟议条款，可支持尽调证据选择。（[记录](../reports/research-investing.md#inv-004)） |
| [ENG-011](../cases/engineering/ENG-011.yaml) | sourced | Cloudflare 2023—2024 年数据中心双重供电事故；2024-03-26 PDX01失联后，两个电源路径同时不可用但共同原因未定时；不把4月8日发布日写成事故日。 | 已找到并阅读全文：2024-03-26为同设施独立供电事件，非2023复述；原候选将发布月份误作事故月份需纠正。（[记录](../reports/research-engineering-a.md#eng-011)） |
| [PRO-007](../cases/product/PRO-007.yaml) | blocked | Airbnb 房源与旅客匹配（2008—2011）；早期本地窗口未确定 | 缺早期同地区日期的有效供需和匹配分布。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-product.md#pro-007)） |
| [ENG-012](../cases/engineering/ENG-012.yaml) | sourced | Google Protocol Buffers 兼容策略（2008—）；proto2 二进制消息 schema 更新前；仅规范行为，不声称当前文本于2008已完全相同。 | proto2 官方指南直接给出字段更新兼容规则；锚定已读规范快照，非2008特定发布事件。（[记录](../reports/research-engineering-a.md#eng-012)） |
| [PRO-008](../cases/product/PRO-008.yaml) | blocked | Slack 早期企业内部扩散（2013—2015）；2013—2015 指定团队购买窗口未定位 | 2019 S-1 支持免费转付费机制，但不能回填为 2013—2015 的具体采购节点及套餐。（[记录](../reports/research-product.md#pro-008)） |
| [ENG-013](../cases/engineering/ENG-013.yaml) | sourced | JVM Double-Checked Locking 语义修订（2004）；Java新内存模型评估窗口，读取惰性单例字段前。 | JSR133参与者2004FAQ含双检代码、失败机制与新volatile保证。（[记录](../reports/research-engineering-a.md#eng-013)） |
| [INV-005](../cases/investing/INV-005.yaml) | sourced | Yelp 2005 首次风险融资的投资建议，而非已确认 Series B；2005-10-03 | 同期备忘录足以界定内容壁垒问题，同时发现原始 Series B 标签与直接记录冲突。（[记录](../reports/research-investing.md#inv-005)） |
| [ENG-014](../cases/engineering/ENG-014.yaml) | sourced | RocksDB Universal Compaction（2013—）；该已读 wiki 设计快照，选择 compaction 策略之前。 | RocksDB 官方 wiki 支持写/读/空间放大取舍；锚定2023修订工件而非虚称2013精确实现。（[记录](../reports/research-engineering-a.md#eng-014)） |
| [PRO-009](../cases/product/PRO-009.yaml) | sourced | Netflix 1998-04-14 DVD 邮寄租赁上线；1998-04-14 发布条件已知、采用结果未知 | 找到 1998 原始发布，明确按次计价、邮寄与选片路径，不借后续订阅结果。（[记录](../reports/research-product.md#pro-009)） |
| [ENG-015](../cases/engineering/ENG-015.yaml) | sourced | Cloudflare OAuth token 泄露与缓解（2023）；2023-10-18发现Okta异常访问后、确认影响范围之前；不引入11月后续事件。 | 2023-10-18事件有独立官方复盘，明确是session/authentication token而非已证实OAuth token；与ENG143后续事件必须分开。（[记录](../reports/research-engineering-a.md#eng-015)） |
| [PRO-010](../cases/product/PRO-010.yaml) | blocked | Duolingo 连续学习 Streak 早期设计（2010s）；2015-03-01 至 03-10 观察窗口（非确定的产品改动） | 2015 原始研究提供 streak 与继续使用的相关性，未定位改动前后或学习成效。（[记录](../reports/research-product.md#pro-010)） |
| [ENG-016](../cases/engineering/ENG-016.yaml) | sourced | Uber H3 地理索引（2018）；2018设计说明快照、为定价聚合位置事件时。 | Uber 2018原文支持单一位置聚合需求及六角/层级取舍，采用定性选择不补误差数字。（[记录](../reports/research-engineering-a.md#eng-016)） |
| [INV-006](../cases/investing/INV-006.yaml) | blocked | Tesla 2008 年 12 月可转换借款；拟为 2008 年 12 月追加资本决定前；精确决策日和当时可得材料未确认。 | 2010 S-1 可核实 2008 年融资与条款，但缺足够证据确定某个 2008 续资决策前可知的现金跑道和里程碑。（[记录](../reports/research-investing.md#inv-006)） |
| [ENG-017](../cases/engineering/ENG-017.yaml) | sourced | Redis Cluster 槽位迁移（2015）；规范live-reconfiguration步骤，槽位处于MIGRATING/IMPORTING时。 | Redis官方Cluster规范可支撑ASK/MOVED的单次迁移行为；锚点为规范工件而非未核实2015事故。（[记录](../reports/research-engineering-a.md#eng-017)） |
| [PRO-011](../cases/product/PRO-011.yaml) | blocked | Figma 免费协作者与编辑席位（2016—2022）；2016—2022 版本未锁定 | 当前官方定价可核免费 viewers，但缺 2016—2022 特定历史版收费及权限快照。（[记录](../reports/research-product.md#pro-011)） |
| [ENG-018](../cases/engineering/ENG-018.yaml) | sourced | CircleCI Dynamic Config（2021）；2021 setup工作流在运行期决定是否生成后续配置之前。 | 2021官方支持教程完整说明setup/continuation契约。（[记录](../reports/research-engineering-a.md#eng-018)） |
| [PRO-012](../cases/product/PRO-012.yaml) | sourced | GitHub 2016-09-14 Pull Request Reviews 发布；2016-09-14 功能公布时；此前只有行评论的体验作已知背景 | 2016 官方上线公告直接确认正式 Review 状态和评论打包能力。（[记录](../reports/research-product.md#pro-012)） |
| [ENG-019](../cases/engineering/ENG-019.yaml) | sourced | Cloudflare 2025 年 8 月 AWS 互联拥塞；2025-08-21 16:27 UTC影响出现后、拥塞根因确认前。 | 2025-08-21原复盘直接给出地域边界、链路观测与恢复。（[记录](../reports/research-engineering-a.md#eng-019)） |
| [INV-007](../cases/investing/INV-007.yaml) | blocked | Theranos 2013—2015 投资者陈述及 2018 SEC 指控；原计划要求某轮融资前；具体轮次与起始信息仍缺证。 | 已读取 SEC 原始诉状，但它是事后指控材料；尚未确认指定轮次的事前材料与尽调权限。（[记录](../reports/research-investing.md#inv-007)） |
| [ENG-020](../cases/engineering/ENG-020.yaml) | sourced | Android Jetpack Compose（2021）；Compose声明式UI状态设计，TextField回调触发之前。 | 官方Compose架构页提供明确状态/事件数据流及TextField例子；训练锚定规范设计快照。（[记录](../reports/research-engineering-a.md#eng-020)） |
| [PRO-013](../cases/product/PRO-013.yaml) | blocked | 候选 2009—2010 Craigslist 导流；具体日期及操作未确定；未确定，禁止将后来的叙述变成同期已知信息 | 核查二手增长史后未找到可独立确认操作、许可和转化的一手记录；不能把流传的 Craigslist hack 当事实。（[记录](../reports/research-product.md#pro-013)） |
| [ENG-021](../cases/engineering/ENG-021.yaml) | blocked | Python GIL 争论与 PEP 703（2023）；2023提案评估时点；当前正文修订时点混合，不视为全为当时已知。 | PEP703原文已读，但现行文本含后续Final/实现完成信息；2023修订快照与同口径工作负载待锁定。（[记录](../reports/research-engineering-a.md#eng-021)） |
| [PRO-014](../cases/product/PRO-014.yaml) | blocked | Nintendo Wii 体感大众化战略（2006）；2006 发布前策略点待核 | 官方 Iwata Asks 主站 502，英国迁移 URL 只返回导航；尚未实际读到策略正文。（[记录](../reports/research-product.md#pro-014)） |
| [ENG-022](../cases/engineering/ENG-022.yaml) | sourced | Google LSM-tree LevelDB（2011）；impl.md所述LSM实现模型，新增随机写入导致memtable轮换前；不把main视为2011精确tag。 | LevelDB原实现说明含明确LSM路径与2011实验工件，可用机制预测。（[记录](../reports/research-engineering-a.md#eng-022)） |
| [INV-008](../cases/investing/INV-008.yaml) | sourced | Coinbase 2021 直接上市前周期盈利判断；2021 年 S-1 公开之后、直接上市之前；不采用上市后价格。 | 上市前 S-1 完整可读，直接披露周期依赖及不同年度盈利，可支持竞争解释训练。（[记录](../reports/research-investing.md#inv-008)） |
| [ENG-023](../cases/engineering/ENG-023.yaml) | sourced | GitHub Actions pwn requests 风险（2020—）；2021公开安全说明中的pull_request_target工作流，checkout不可信PR前。 | GitHub Security Lab披露基于其报告过的实际workflow漏洞，具有可读危险例子。（[记录](../reports/research-engineering-a.md#eng-023)） |
| [PRO-015](../cases/product/PRO-015.yaml) | blocked | Etsy 手作卖家社区（2005—）；2005 起的特定品类决策未确定 | 2015 S-1 证实手作市场定位，未定位早期单一品类的供给约束和买方任务。（[记录](../reports/research-product.md#pro-015)） |
| [ENG-024](../cases/engineering/ENG-024.yaml) | sourced | Amazon Aurora 共享存储（2017）；论文设计快照、计算实例崩溃且共享存储仍有副本时。 | SIGMOD2017原论文经Amazon Science获取正文，支持日志/存储恢复契约。（[记录](../reports/research-engineering-a.md#eng-024)） |
| [PRO-016](../cases/product/PRO-016.yaml) | sourced | MongoDB Atlas 2016-06-28 上线；2016-06-28 公告条件已知、后续商业表现未知 | 2016 原始公告确认托管服务及自服务选项，可执行用户任务/运维责任迁移的预测。（[记录](../reports/research-product.md#pro-016)） |
| [ENG-025](../cases/engineering/ENG-025.yaml) | blocked | Nix 可重现构建（2004—）；论文6.8节假设边界；尚未选定具体构建诊断时点。 | Nix创始人2006论文已读并发现明确非确定构建反例，但规划要求的一份derivation与一次实际非确定构建快照尚不齐。（[记录](../reports/research-engineering-a.md#eng-025)） |
| [INV-009](../cases/investing/INV-009.yaml) | blocked | Lyft 2019 上市前贡献口径；2019-03-18 披露后，定价前 | 公司贡献口径不能替代同城市或同 cohort 补贴和履约数据。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing.md#inv-009)） |
| [ENG-026](../cases/engineering/ENG-026.yaml) | sourced | Cloudflare 2023 年 10 月 Workers KV 部署问题；2023-10-30多产品错误出现、定位KV依赖前。 | 官方复盘证实KV部署工具配置、401与依赖传播，不是猜测源提示。（[记录](../reports/research-engineering-a.md#eng-026)） |
| [PRO-017](../cases/product/PRO-017.yaml) | sourced | Slack 2013 预览前邀请外部团队试用；最初几个朋友团队已同意试用，尚未扩到Rdio更大团队；具体日未知 | 创始人回顾提供内部工具对外试用和团队规模差异的直接观察，足以测试 dogfooding 迁移边界。（[记录](../reports/research-product.md#pro-017)） |
| [ENG-027](../cases/engineering/ENG-027.yaml) | sourced | SQLite WAL 模式引入（2010）；2010-07-21版本3.7.0新增WAL选择时；排除页面中后续2026缺陷。 | SQLite官方WAL说明明确3.7.0引入日期、并发及checkpoint行为。（[记录](../reports/research-engineering-a.md#eng-027)） |
| [PRO-018](../cases/product/PRO-018.yaml) | sourced | Snapchat 2011—2012 短暂照片消息；2012-05-10回述的2011发布后、尚未揭晓学校使用观察的产品判断窗口 | 同期创始人文章给出非正式沟通目标与当时用户反馈；预测表达行为而不宣称因果。（[记录](../reports/research-product.md#pro-018)） |
| [ENG-028](../cases/engineering/ENG-028.yaml) | blocked | Google Dapper 采样追踪（2010）；论文采样策略选择时；不预设未给的请求或故障频率。 | 有采样机制，缺特定故障频率与独立性，不能算漏采概率。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-a.md#eng-028)） |
| [INV-010](../cases/investing/INV-010.yaml) | blocked | Figma 2015 Series A 与 Preview（候选 2016 轮次待改）；2015-12-03 Preview 发布时，2016 多人功能前 | 直接公司与投资人文章确认的是 2015 A 轮，不是拟选的 2016 融资；采购证据也不足。（[记录](../reports/research-investing.md#inv-010)） |
| [ENG-029](../cases/engineering/ENG-029.yaml) | sourced | Rust Ownership 与 Borrow Checker（2015）；2015文章中的跨线程共享例子、编译判断前；沿用原文版本语法。 | 2015 Rust官方并发文章含实际共享/所有权示例和编译拒绝边界。（[记录](../reports/research-engineering-a.md#eng-029)） |
| [PRO-019](../cases/product/PRO-019.yaml) | blocked | AWS Lambda 2014-11-13 Preview 计费；2014-11-13 公告已知、工作负载选择前 | 有发布时计价规则，但缺同一有来源工作负载的调用与执行时间。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-product.md#pro-019)） |
| [ENG-030](../cases/engineering/ENG-030.yaml) | blocked | Snowflake 分离存储和计算（2016）；2016论文设计快照待取。 | 尝试Snowflake2016官方PDF与ACM DOI均未取得正文，不凭标题核实架构细节。（[记录](../reports/research-engineering-a.md#eng-030)） |
| [PRO-020](../cases/product/PRO-020.yaml) | blocked | Slack 可搜索团队消息历史（2013—）；2013-07-31 memo；单版历史规则待确定 | 2013 memo 证实搜索定位，但缺早期历史保留规则、权限及具体知识任务路径。（[记录](../reports/research-product.md#pro-020)） |
| [ENG-031](../cases/engineering/ENG-031.yaml) | sourced | MongoDB 副本集选主（2016—2020）；MongoDB4.4归档契约快照，一次确认写入后、primary选举/重启前；准确文档发表日未知。 | MongoDB4.4归档文档锁定候选年份范围内版本，明确write concern/journal/read语义。（[记录](../reports/research-engineering-a.md#eng-031)） |
| [INV-011](../cases/investing/INV-011.yaml) | blocked | SpaceX 2008 生存融资与 CRS 里程碑；2008-12-23 合同授予前；确切资金决定日未核实 | 官方来源确认采购结果，但没有支持拟选资本决策时剩余现金和可选行动的事前材料。（[记录](../reports/research-investing.md#inv-011)） |
| [ENG-032](../cases/engineering/ENG-032.yaml) | blocked | Guix 构建隔离（2013）；2013引导链设计候选，具体工件未读取。 | 尝试Guix2013官方引导文章不可达，未获得足够正文。（[记录](../reports/research-engineering-a.md#eng-032)） |
| [PRO-021](../cases/product/PRO-021.yaml) | sourced | PayPal 2001 在线拍卖支付扩散；2002-02-11 S-1/A披露后，依据公开支付流程判断渠道依赖；不回填2001事前 | 2002 原始招股书有具体付款/收款流程、未注册收款人路径及拍卖使用比例。（[记录](../reports/research-product.md#pro-021)） |
| [ENG-033](../cases/engineering/ENG-033.yaml) | sourced | AWS S3 2017 年 us-east-1 中断；2017-02-28 9:37AM PST维护指令之后，故障传播调查前。 | AWS直接复盘给出误指令、index/placement依赖与跨服务后果。（[记录](../reports/research-engineering-a.md#eng-033)） |
| [PRO-022](../cases/product/PRO-022.yaml) | blocked | Basecamp Hey 邮件产品发布（2020）；2020-06-15 上线前 | 取得团队原始发布回顾，但发布价格和首版功能/替代边界尚未从同期一手资料完整核实。（[记录](../reports/research-product.md#pro-022)） |
| [ENG-034](../cases/engineering/ENG-034.yaml) | blocked | Meltdown（2018）；2018缓解评估时，具体服务负载未锁定。 | Meltdown原论文已读，攻击/隔离有直接证据；规划指定单一负载的同口径性能代价未取得。（[记录](../reports/research-engineering-a.md#eng-034)） |
| [INV-012](../cases/investing/INV-012.yaml) | sourced | SendGrid 2011 Series B 投资建议；2011-12-16 备忘录形成时 | 同期投资备忘录直接支持产品、客户访问、竞品与拟议交易。（[记录](../reports/research-investing.md#inv-012)） |
| [ENG-035](../cases/engineering/ENG-035.yaml) | sourced | GraphQL 在 Facebook 的起源（2012—2015）；2015公开设计快照，移动端选择数据获取接口之前。 | GraphQL设计者2015发布说明足以限定移动端层级查询的接口边界。（[记录](../reports/research-engineering-a.md#eng-035)） |
| [PRO-023](../cases/product/PRO-023.yaml) | blocked | OpenTable 餐厅端库存系统（1998—2000）；1998—2000 安装餐厅软件到开放市场的节点未锁定 | 2009 S-1 说明 ERB 与实时市场如何连接，但未确证 1998—2000 具体版本/先后决策。（[记录](../reports/research-product.md#pro-023)） |
| [ENG-036](../cases/engineering/ENG-036.yaml) | sourced | Linux CFS 调度器（2007）；Linux2.6.23 CFS设计模型，runnable任务选取之前。 | Linux原始CFS设计说明明确2.6.23及vruntime调度逻辑。（[记录](../reports/research-engineering-a.md#eng-036)） |
| [PRO-024](../cases/product/PRO-024.yaml) | sourced | Sentry 2017-12-05 Enterprise SAML SSO；2017-12-05 公布 Enterprise 身份集成功能时 | 锁定 2017 Enterprise SAML 发布，直接列出管理员、身份治理和付费边界；实际采购收益未知。（[记录](../reports/research-product.md#pro-024)） |
| [ENG-037](../cases/engineering/ENG-037.yaml) | sourced | Redis Sentinel 自动故障转移（2013）；Sentinel规范中的分区与promote前；不声称现行参数在2013完全一致。 | Redis Sentinel官方说明明确异步复制与分区旧主场景，可支撑定性预测。（[记录](../reports/research-engineering-a.md#eng-037)） |
| [INV-013](../cases/investing/INV-013.yaml) | sourced | Airbnb 2009 年初经营现金生存试验；2009 年初 YC 期间，在首次纽约经营试验之前（精确日未知） | 直接参与者回顾包含现金目标和经营试验；标明事后回忆，不当作同期公开市场信息。（[记录](../reports/research-investing.md#inv-013)） |
| [ENG-038](../cases/engineering/ENG-038.yaml) | sourced | Go 1.21 Toolchain 管理（2023）；Go1.21工具链管理引入，离线构建执行前。 | Go1.21同期设计者文章明确下载/选择规则，适合离线策略取舍。（[记录](../reports/research-engineering-a.md#eng-038)） |
| [PRO-025](../cases/product/PRO-025.yaml) | blocked | YouTube 2005 约会版本转通用视频分享；2005 约会版本上线后一周（回忆中的窗口；不认定具体日） | 创始人回顾确认约会版本和放开上传，但缺同期用户行为与可靠时序；与预设的“用户上传别的内容引发转型”不一致。（[记录](../reports/research-product.md#pro-025)） |
| [ENG-039](../cases/engineering/ENG-039.yaml) | blocked | Cloudflare Pingora 替换 NGINX（2022—2024）；2022说明中的NGINX连接池瓶颈诊断；收益测量在提交预测后揭示。 | 有总连接与资源测量，但缺连接占用成本分解，不能估连接复用的独立贡献。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-a.md#eng-039)） |
| [PRO-026](../cases/product/PRO-026.yaml) | sourced | 首代 iPhone 2007 软键盘公布；2007-01-09 公告后、上市前 | 2007 原始发布明确软键盘及预测纠错设计，适合比较可变界面与输入学习成本。（[记录](../reports/research-product.md#pro-026)） |
| [ENG-040](../cases/engineering/ENG-040.yaml) | sourced | Cloudflare 2023 年 11 月控制面中断；2023-11-02控制面与analytics异常出现后、完整依赖梳理之前。 | 2023-11独立官方复盘直接支持控制面/数据面故障域，与2024ENG011分开。（[记录](../reports/research-engineering-a.md#eng-040)） |
| [INV-014](../cases/investing/INV-014.yaml) | blocked | Box 2014 延期上市窗口融资；2014-07-07 融资公告后 | 直接公告确认融资，但条款明确未披露；不足以预测旧股的合同稀释或顺位。（[记录](../reports/research-investing.md#inv-014)） |
| [ENG-041](../cases/engineering/ENG-041.yaml) | sourced | Google Bigtable（2006）；论文设计模型，选择row key及tablet负载分布之前。 | Bigtable2006原论文直接支持有序行键、tablet切分与局部热点推演。（[记录](../reports/research-engineering-a.md#eng-041)） |
| [PRO-027](../cases/product/PRO-027.yaml) | sourced | GitHub 2019-01-07 免费私有仓库；2019-01-07 新政策已知、后续采用未知 | 2019 官方公告有明确免费边界与商业计划，足以进行采用/收入结构预测。（[记录](../reports/research-product.md#pro-027)） |
| [ENG-042](../cases/engineering/ENG-042.yaml) | blocked | Kubernetes CRD 与 Aggregated API（2016—2018）；2016–2018内具体版本待核。 | 官方CRD/聚合API比较已读，但现行能力含后续webhook等特性，未锁定2016–2018同版本契约。（[记录](../reports/research-engineering-a.md#eng-042)） |
| [PRO-028](../cases/product/PRO-028.yaml) | sourced | Figma 2021-11-16 评论重做；2021-11-16 改动已公布、效果未知 | 在 2017— 的候选范围锁定 2021 评论重做，官方有用户研究反馈与交接功能的直接描述。（[记录](../reports/research-product.md#pro-028)） |
| [ENG-043](../cases/engineering/ENG-043.yaml) | sourced | Spectre（2018）；原始披露的推测执行观察模型；固定变体并在预测前隐藏实际泄漏。 | Spectre原研究论文支持一条缓存观察路径与架构权限边界。（[记录](../reports/research-engineering-a.md#eng-043)） |
| [INV-015](../cases/investing/INV-015.yaml) | blocked | Uber 上市前最近私募窗口与局部单位经济；2019 上市前；最近融资窗口尚未核定 | 未核定对应融资进入时点及同城市收入、补贴、履约成本。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing.md#inv-015)） |
| [ENG-044](../cases/engineering/ENG-044.yaml) | sourced | Facebook TAO（2013）；论文一次远端写完成、本地数据库异步复制尚未赶上时。 | TAO2013原论文给出MySQL持久层、cache层与跨区异步传播。（[记录](../reports/research-engineering-a.md#eng-044)） |
| [PRO-029](../cases/product/PRO-029.yaml) | sourced | LinkedIn 2003-05 初始邀请及转介绍网络；2003-05-07 上线初期，用户反馈尚未揭示 | 取得 2003 实际用户讨论及 Reid Hoffman 同期答复，能区分邀请增长与可信关系。（[记录](../reports/research-product.md#pro-029)） |
| [ENG-045](../cases/engineering/ENG-045.yaml) | sourced | Rust Cargo Features 设计（2013—）；resolver=2明确指定的规范模型、增加一条普通依赖之前；不声称2013已具resolver2。 | Cargo官方features页明确union及resolver2例外，可选一版resolver进行菱形依赖推演。（[记录](../reports/research-engineering-a.md#eng-045)） |
| [PRO-030](../cases/product/PRO-030.yaml) | blocked | Microsoft Windows Phone 停止投入（2017）；2017 投入终止决策前 | 官方生命周期可核最后版本和终止支持；2017 投入决策及理由的一手声明尚未读到。（[记录](../reports/research-product.md#pro-030)） |
| [ENG-046](../cases/engineering/ENG-046.yaml) | blocked | .NET ThreadPool Hill Climbing（2000s—）；运行时与负载观测快照待定。 | 已读.NET官方HillClimbing源码，但未锁定历史tag及一个实际worker调整的观测曲线。（[记录](../reports/research-engineering-a.md#eng-046)） |
| [INV-016](../cases/investing/INV-016.yaml) | sourced | Pinterest 2011 投资考察备忘录；2011-04-03 备忘录形成时 | 直接投资记录可用于选择下一项需求证据；不把兴趣活动等同收入。（[记录](../reports/research-investing.md#inv-016)） |
| [ENG-047](../cases/engineering/ENG-047.yaml) | sourced | Fastly 2021 年 6 月大面积故障；2021-06-08客户配置变化后、定位触发条件之前。 | Fastly2021官方事故说明明确有效配置触发潜伏实现bug与恢复。（[记录](../reports/research-engineering-a.md#eng-047)） |
| [PRO-031](../cases/product/PRO-031.yaml) | blocked | Tinder Swipe 匹配（2012）；2012 版本未取得 | 缺同期喜欢、匹配和有效对话的可比较数量。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-product.md#pro-031)） |
| [ENG-048](../cases/engineering/ENG-048.yaml) | blocked | SQLite Query Planner（2010s）；规划要求的同SQL实际计划变慢节点未取得。 | SQLite官方查询规划教程有SQL/索引及ANALYZE推理，但无版本化真实慢查询计划与统计快照。（[记录](../reports/research-engineering-a.md#eng-048)） |
| [PRO-032](../cases/product/PRO-032.yaml) | sourced | Dropbox 2007-04-04 HN 公开 demo；2007-04-04 demo 发布前，讨论和后续反馈隐藏 | 2007 原始 HN 反馈加创始人回顾确认 demo 的兴趣信号；明确与后一年 Digg 视频区分。（[记录](../reports/research-product.md#pro-032)） |
| [ENG-049](../cases/engineering/ENG-049.yaml) | sourced | Kubernetes API 对象与控制器分离（2014—）；Kubernetes声明对象被创建后、控制器调和之前；不宣称Deployment在2014初版已有。 | 官方控制器文档可支撑声明状态与执行职责的分离；以设计工件为锚点。（[记录](../reports/research-engineering-a.md#eng-049)） |
| [INV-017](../cases/investing/INV-017.yaml) | sourced | Twilio 2009 seed 延长融资建议；2009-11-06 备忘录形成时 | 直接备忘录支持延长 runway 以等待进一步验证的决策节点。（[记录](../reports/research-investing.md#inv-017)） |
| [ENG-050](../cases/engineering/ENG-050.yaml) | blocked | LinkedIn Kafka 日志存储（2011）；2011论文producer实验工件，比较batch1与50前；实验结果隐藏。 | 有消息及批次基准，缺等待分布和到达工作量，不能精算延迟代价。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-a.md#eng-050)） |
| [PRO-033](../cases/product/PRO-033.yaml) | blocked | Snowflake Consumption Model（2014—2019）；指定客户用量窗口未确定 | 2020 S-1 正文超上限且没有 2014—2019 某客户的账单路径与预算，不能判断采用还是治理失效。（[记录](../reports/research-product.md#pro-033)） |
| [ENG-051](../cases/engineering/ENG-051.yaml) | sourced | Log4Shell（2021）；2021 Log4j2受影响版本处理不可信日志输入之前；修补结局在最终揭晓。 | Apache原安全公告明确CVE-2021-44228输入控制、JNDI与LDAP执行条件。（[记录](../reports/research-engineering-a.md#eng-051)） |
| [PRO-034](../cases/product/PRO-034.yaml) | blocked | Spotify 2008-10 欧洲流式播放上线；2010 性能观察；2008 上线、2010 实测前；265ms 不进入开场 | 2010论文验证机制及延迟，但不能确认服务器/P2P/缓存组合全部属于2008同版；2008题初始信息仍不足，265ms不能回填。（[记录](../reports/research-product.md#pro-034)） |
| [ENG-052](../cases/engineering/ENG-052.yaml) | sourced | Amazon Dynamo（2007）；论文设计模型的一次分区与读取前；沿论文N/R/W示例，不造购物车事故。 | Dynamo2007原论文支持N/R/W、版本冲突和sloppy quorum边界。（[记录](../reports/research-engineering-a.md#eng-052)） |
| [INV-018](../cases/investing/INV-018.yaml) | sourced | Toast 2015 首轮机构融资建议；2015-12-14 备忘录形成时 | 同期投资备忘录明确 Series B 身份和餐厅 POS/支付场景。（[记录](../reports/research-investing.md#inv-018)） |
| [ENG-053](../cases/engineering/ENG-053.yaml) | blocked | Nx Affected Builds（2020—）；2020候选快照未锁定；本次已读v24页。 | Nx现行v24 affected机制已经变化为task-based，无法直接用于原候选2020项目依赖图题。（[记录](../reports/research-engineering-a.md#eng-053)） |
| [PRO-035](../cases/product/PRO-035.yaml) | blocked | Dropbox 2008-09 发布 freemium 配额；2008 发布套餐已知、某使用任务升级判断前 | 创始人回述2008采用freemium，但2GB来自访谈时套餐讨论，缺2008准确边界与按任务升级证据；不得回填后来容量。（[记录](../reports/research-product.md#pro-035)） |
| [ENG-054](../cases/engineering/ENG-054.yaml) | blocked | Google 2012 年闰秒 Linux 故障；候选2012事故尚未识别。 | 候选Google2012闰秒Linux高CPU事件身份未核实；Google官方时间文档称自2008已smear，不能混用其他公司2012事故。（[记录](../reports/research-engineering-a.md#eng-054)） |
| [PRO-036](../cases/product/PRO-036.yaml) | sourced | Discover Weekly 2015-07 推出；2015-07-21 功能介绍已知、后续使用结果未知 | 同期 Spotify staff 帖确认规则与资格，后续官方使用总量支持功能持续使用；因果留存未知。（[记录](../reports/research-product.md#pro-036)） |
| [ENG-055](../cases/engineering/ENG-055.yaml) | sourced | Go 1.14 异步抢占（2020）；Go1.14运行忙循环且另一goroutine可运行时，限支持平台。 | Go1.14官方release notes明确异步抢占语义及平台例外。（[记录](../reports/research-engineering-a.md#eng-055)） |
| [INV-019](../cases/investing/INV-019.yaml) | blocked | Stripe 2011 种子融资尽调；2011 年候选种子轮；确切日与可知材料未核实 | 检索主要得到轮次数据库与二手报道，未找到足以支持同期金融责任、团队和实际轮次的直接材料。（[记录](../reports/research-investing.md#inv-019)） |
| [ENG-056](../cases/engineering/ENG-056.yaml) | blocked | GitHub REST 到 GraphQL API v4（2016）；2016 Early Access发布工件，客户端需获取用户前三仓库及计数；不采用2021后续成果。 | 关系查询可核，REST 对应端点与分页未齐，不能比较精确请求数。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-a.md#eng-056)） |
| [PRO-037](../cases/product/PRO-037.yaml) | blocked | Hotmail 1996—1997 邮件附加推广；推广文案机制已知、扩散结果隐藏；具体上线日未核 | 有签名机制记录，缺同期发送到注册再发送的完整漏斗。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-product.md#pro-037)） |
| [ENG-057](../cases/engineering/ENG-057.yaml) | sourced | Amazon Redshift 列式分析（2012）；列式分析存储布局选择；候选2012首发日期不由此现行页证实。 | Redshift官方存储说明直接支持只读所需列与同类型压缩；作为架构工件而非2012实测事件。（[记录](../reports/research-engineering-a.md#eng-057)） |
| [PRO-038](../cases/product/PRO-038.yaml) | sourced | Instagram 从 Burbn 缩减功能（2010）；2010 Burbn已有使用观察、聚焦Instagram前；确切日未核实 | 已实际读到官方完整转录；创始人回顾明确Burbn最受喜爱的是图片分享并聚焦照片问题。回顾不是2010原始日志或因果实验。（[记录](../reports/research-product.md#pro-038)） |
| [ENG-058](../cases/engineering/ENG-058.yaml) | blocked | Kafka 复制协议（2012—2013）；原候选2012–2013内0.8.0实现，完整版本规则待核。 | 尝试Kafka0.8官方归档多种路径仅返回重定向页；取得0.8.0配置源码但选举/ACK全契约仍未读取。（[记录](../reports/research-engineering-a.md#eng-058)） |
| [INV-020](../cases/investing/INV-020.yaml) | blocked | Nubank 2021 IPO 估值；2021-12 IPO 定价前 | 原文读取受限，IPO 股本和客户风险成本未逐项核实。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing.md#inv-020)） |
| [ENG-059](../cases/engineering/ENG-059.yaml) | sourced | Bazel Remote Execution API（2018—）；v2.0.0 Action/Command契约，决定复用缓存之前。 | Remote Execution API v2.0.0原proto固定版本，支持action输入与环境边界核验。（[记录](../reports/research-engineering-a.md#eng-059)） |
| [PRO-039](../cases/product/PRO-039.yaml) | sourced | Teams 2017-03-14 面向 Office365 商业客户 GA；2017-03-14 公布方案、后续竞争结果未知 | 2017 GA 公告直接确认 Office365 分发条件与实际试用组织，足够进行渠道与产品竞争假说分析。（[记录](../reports/research-product.md#pro-039)） |
| [ENG-060](../cases/engineering/ENG-060.yaml) | sourced | Heartbleed OpenSSL（2014）；OpenSSL1.0.1f等受影响版本接收heartbeat时，结果在推演后揭晓。 | OpenSSL2014原公告直接确认heartbeat缺边界检查、泄漏能力及修复。（[记录](../reports/research-engineering-a.md#eng-060)） |
| [PRO-040](../cases/product/PRO-040.yaml) | blocked | DoorDash 郊区餐饮配送起点（2013）；2013 郊区初始配送窗口未锁定 | 原文访问失败，缺同区路线、等待、订单与配送成本。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-product.md#pro-040)） |
| [ENG-061](../cases/engineering/ENG-061.yaml) | sourced | Cloudflare 2024 年 6 月 DDoS 规则事故；2024-06-20 17:47后第二事件初期，观测异常、尚未知规则触发bug。 | 2024-06-20复盘明确两个连续事件；只取第二个DDoS规则触发率限bug，避免混同首个拥塞。（[记录](../reports/research-engineering-a.md#eng-061)） |
| [INV-021](../cases/investing/INV-021.yaml) | blocked | Spotify 2018 上市前版税与边际毛利；2018-02-28 F-1 发布后 | 历史平均毛利不能代替新增订户边际版税；合同输入不足。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing.md#inv-021)） |
| [ENG-062](../cases/engineering/ENG-062.yaml) | blocked | Netflix 自适应码率播放（2010s）；2010s具体自适应码率设计与播放节点待核。 | 尝试Netflix稳态码率文章不可达；单一带宽下降时的缓冲状态/设计版本未取得。（[记录](../reports/research-engineering-a.md#eng-062)） |
| [PRO-041](../cases/product/PRO-041.yaml) | blocked | Grammarly 浏览器实时纠错（2015—）；2015 扩展上线；具体版本日未知 | 官方回顾确认2015免费扩展，但尚缺当时安装到首反馈操作快照，设计师原文无法读取。（[记录](../reports/research-product.md#pro-041)） |
| [ENG-063](../cases/engineering/ENG-063.yaml) | blocked | Rust async/await 稳定（2019）；Rust1.39稳定的future创建/轮询模型；取消节点未锁定。 | 2019 Rust稳定发布原文已读，足以证明lazy/poll；取消与资源释放的同版本语义未齐，保留原范围不自动缩成惰性常识题。（[记录](../reports/research-engineering-a.md#eng-063)） |
| [PRO-042](../cases/product/PRO-042.yaml) | sourced | Unity Runtime Fee 2023修订至2024撤销；2023-09-22 修订政策已公布，2024取消隐藏 | 2023修订信与2024取消公告完整确认收费政策变动；明确没有真实收费账单。（[记录](../reports/research-product.md#pro-042)） |
| [ENG-064](../cases/engineering/ENG-064.yaml) | blocked | Docker Image OCI 标准化（2015—2017）；2017 v1.0发布窗口；页面正文新闻稿日期另为7月19日，保留差异。 | 2017 OCI原发布公告已读；v1.0镜像规范正文尝试未取得，未完成格式保证与运行时前提的逐条核对。（[记录](../reports/research-engineering-a.md#eng-064)） |
| [INV-022](../cases/investing/INV-022.yaml) | sourced | LinkedIn 2006 投资建议与商业化尽调；2006-12-11 备忘录形成时 | 直接投资 memo 包含当时网络规模、收入和交易建议。（[记录](../reports/research-investing.md#inv-022)） |
| [ENG-065](../cases/engineering/ENG-065.yaml) | sourced | Google Megastore（2011）；2011论文选择entity group划分、一次跨组操作之前。 | CIDR2011原论文经Google链接读到，entity group边界、两阶段提交和吞吐约束完整。（[记录](../reports/research-engineering-a.md#eng-065)） |
| [PRO-043](../cases/product/PRO-043.yaml) | blocked | Atlassian Jira 自助购买（2000s）；2000s 某采购约束尚未锁定 | 定位2015 F-1自助销售披露但原文超读取上限，且不能填补2000s具体审批/安全购买场景。（[记录](../reports/research-product.md#pro-043)） |
| [ENG-066](../cases/engineering/ENG-066.yaml) | sourced | VS Code Remote Development（2019）；2019 Remote Development预览，选择扩展安装/执行位置之前。 | 2019 VS Code原发布说明明确本地UI/远端workspace扩展职责，可运行边界迁移问题。（[记录](../reports/research-engineering-a.md#eng-066)） |
| [PRO-044](../cases/product/PRO-044.yaml) | blocked | Duolingo 2018 Leaderboards 初测；2018 首次测试前；具体日未核实 | 官方回顾明确首次测试为 2018，年份不必武断改为 2019；但没有当轮分群、参与与学习结果，无法执行既定区分任务。（[记录](../reports/research-product.md#pro-044)） |
| [ENG-067](../cases/engineering/ENG-067.yaml) | sourced | PostgreSQL MVCC VACUUM（2000s—）；PostgreSQL13，一个旧快照仍可能看见已删除版本时。 | PostgreSQL13归档官方文档锁定一版MVCC回收规则，可做规范时序而不伪装事故。（[记录](../reports/research-engineering-a.md#eng-067)） |
| [INV-023](../cases/investing/INV-023.yaml) | sourced | WeWork 2019 年救助融资的现金与控制分离；2019-10-22 公告后，后续执行前 | 当事方公告区分新融资、旧股收购和原承诺加速；可训练不把名义总额等同公司现金。（[记录](../reports/research-investing.md#inv-023)） |
| [ENG-068](../cases/engineering/ENG-068.yaml) | sourced | AWS us-east-1 2021 年 12 月网络事件；2021-12-07 7:30AM PST后内部服务退化、监控不完整时。 | AWS2021-12-07直接复盘详细记录网络、监控/部署依赖与恢复约束。（[记录](../reports/research-engineering-a.md#eng-068)） |
| [PRO-045](../cases/product/PRO-045.yaml) | blocked | Pinterest Waitlist 邀请制（2010—2011）；2010—2011 邀请窗口未定位 | 尚无2010—2011一轮邀请规则及受邀后行为的一手记录；后续开放注册报道不能替代。（[记录](../reports/research-product.md#pro-045)） |
| [ENG-069](../cases/engineering/ENG-069.yaml) | blocked | Capital One 云环境泄露（2019）；2019-07-17外部告知潜在泄露后、完整机制调查前。 | DOJ原发布说明已读，支持Capital One2019事件及WAF配置问题；具体SSRF→凭据→S3链条需可读原complaint，PDF当前仅图片未取得文本。（[记录](../reports/research-engineering-a.md#eng-069)） |
| [PRO-046](../cases/product/PRO-046.yaml) | sourced | Airbnb 2009 纽约房源摄影；2009年纽约房源浏览、实地摄影前，确切日未核 | Joe Gebbia访谈与早期导师回顾直接支持纽约改善房源照片；前后收入不能独立证明照片因果。（[记录](../reports/research-product.md#pro-046)） |
| [ENG-070](../cases/engineering/ENG-070.yaml) | sourced | Go Scheduler G-M-P 模型（2012）；Go1.1实现中已知阻塞系统调用entersyscallblock之前；不混同channel park。 | Go1.1源码固定tag直接给出G/M/P和blocking syscall移交；候选2012是设计时间，运行工件为2013版，需记录范围修正。（[记录](../reports/research-engineering-a.md#eng-070)） |
| [INV-024](../cases/investing/INV-024.yaml) | sourced | Mistral 2023 seed 后需求验证选择；2023-06-13 seed 公告后，模型发布前 | 直接领投方同期文章支持资本与团队条件，后续同方记录可单独核对产品发布结果。（[记录](../reports/research-investing.md#inv-024)） |
| [ENG-071](../cases/engineering/ENG-071.yaml) | blocked | Crossplane Compositions（2020—2023）；2020–2023中一次Composition输入输出契约快照待锁定。 | Crossplane Accepted设计正文已读，但该文显式说明部署术语/实现已演变，历史版本合同未锁定，v1.13 tag尝试失败。（[记录](../reports/research-engineering-a.md#eng-071)） |
| [PRO-047](../cases/product/PRO-047.yaml) | sourced | Netflix 2007-01-16 即时观看PC功能；2007-01-16 公告已知、上线后采用未知 | 2007原始公告给出渐进流媒体策略、内容与技术限制，能判断蚕食与分发的取舍。（[记录](../reports/research-product.md#pro-047)） |
| [ENG-072](../cases/engineering/ENG-072.yaml) | sourced | LinkedIn Venice 多区域数据（2022）；2022设计快照，一地区write/ingest完成后、跨区可见性核验之前。 | LinkedIn2022原开源说明直接声明eventual consistency及active-active复制，不擅自承诺精确延迟。（[记录](../reports/research-engineering-a.md#eng-072)） |
| [PRO-048](../cases/product/PRO-048.yaml) | sourced | Steam Workshop 2011-10-13 TF2提交中心上线；2011-10-13 新中心已说明、长期供给未知 | 2011原始Valve公告明确提交/反馈机制与既有创作者收益，足以预测供给激励，避免前后因果错置。（[记录](../reports/research-product.md#pro-048)） |
| [ENG-073](../cases/engineering/ENG-073.yaml) | sourced | Meta Sapling 版本控制（2022）；2022发布工件中的Sapling专用后端查询，用户尚未下载所需历史时。 | Meta2022发布说明提供lazy history下载、分段changelog与Git后端限制，足以单一历史操作责任分析。（[记录](../reports/research-engineering-a.md#eng-073)） |
| [INV-025](../cases/investing/INV-025.yaml) | sourced | Datadog 2015 Series C 融资与集成价值；2015-01-29 公司公告后 | 同期公司公告确认 3100 万美元 C 轮、当时集成和客户使用描述。（[记录](../reports/research-investing.md#inv-025)） |
| [ENG-074](../cases/engineering/ENG-074.yaml) | sourced | Google Borg 集群超售（2015）；论文资源回收策略选择，在线任务尚未出现负载峰值时。 | Borg2015原论文直接支持资源reservation、优先级与回收取舍。（[记录](../reports/research-engineering-a.md#eng-074)） |
| [PRO-049](../cases/product/PRO-049.yaml) | blocked | Superhuman早期强制30分钟人工onboarding；早期已采用30分钟引导后，判断是否继续强制人工引导；确切年月未公开 | 有人工作业流程，缺可归属成本和同窗口激活收益，无法回本计算。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-product.md#pro-049)） |
| [ENG-075](../cases/engineering/ENG-075.yaml) | blocked | PostgreSQL B-tree Deduplication（2020）；PostgreSQL13重复键索引选择、插入引发去重之前。 | 已定位去重机制，缺实际重复键分布及页面尺寸。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-a.md#eng-075)） |
| [PRO-050](../cases/product/PRO-050.yaml) | blocked | Zoom 2019 Basic免费会议限制；2019-03-22 S-1公布套餐后；具体团队是否升级判断前 | 2019 S-1可核免费/付费并行与传播叙述，但可读正文未直接核实40分钟及同版付费时长；2020教育豁免也不能回填2019套餐。（[记录](../reports/research-product.md#pro-050)） |
| [ENG-076](../cases/engineering/ENG-076.yaml) | sourced | Atlassian 2022 年云服务恢复事故；2022-04-05误删后已定位脚本、评估恢复路径之前。 | Atlassian2022完整PIR支持app/site ID误删、备份与跨产品恢复差异。（[记录](../reports/research-engineering-a.md#eng-076)） |
| [INV-026](../cases/investing/INV-026.yaml) | blocked | Roblox 2021 直接上市前估值口径；2021-02-11 S-1/A 披露后，上市前 | 递延定义可核，但股本、事前可见价格与期限未完成抽取。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing.md#inv-026)） |
| [ENG-077](../cases/engineering/ENG-077.yaml) | sourced | Kubernetes CVE-2018-1002105；2018受影响apiserver代理upgrade请求后，未授权后续请求进入既有连接前。 | Kubernetes官方CVE issue提供升级连接绕过认证授权、受影响路径与修复版本。（[记录](../reports/research-engineering-a.md#eng-077)） |
| [PRO-051](../cases/product/PRO-051.yaml) | sourced | Terraform Enterprise 2017-12-12 GA；2017-12-12 公告已知、组织试用/购买前 | 2017 GA直接比较OSS与Enterprise的工作区及治理功能，可测试自管替代条件。（[记录](../reports/research-product.md#pro-051)） |
| [ENG-078](../cases/engineering/ENG-078.yaml) | sourced | Go GC Concurrent Mark Sweep（2015）；Go1.5并发标记时mutator准备修改堆指针之前。 | Go1.5设计者同期文章直接解释三色标记与write barrier不变量。（[记录](../reports/research-engineering-a.md#eng-078)） |
| [PRO-052](../cases/product/PRO-052.yaml) | sourced | Duolingo 2012-06 对外开放；2012-06-19 发布；beta结果隐藏或按需分层 | 2012发布原材料有免费定位、任务、商业计划与beta使用，不以免费直接推出学习障碍全部消除。（[记录](../reports/research-product.md#pro-052)） |
| [ENG-079](../cases/engineering/ENG-079.yaml) | sourced | Kubernetes EndpointSlice 传播（2019—2021）；v1.21.0某EndpointSlice变更已经进cache但proxier尚未应用时；限定iptables数据面。 | Kubernetesv1.21.0源码固定tag明确EndpointSlice pending/applied缓存及回调队列，支持非即时生效。（[记录](../reports/research-engineering-a.md#eng-079)） |
| [INV-027](../cases/investing/INV-027.yaml) | blocked | HelloFresh 2017 资本窗口 cohort 回收；2017 上市窗口，精确截止日待核 | 官方报表未提供已核实的同 cohort CAC、复购、贡献和损耗输入。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing.md#inv-027)） |
| [ENG-080](../cases/engineering/ENG-080.yaml) | sourced | 2015 Bazel Beta 公告；2015-09-09 Beta 发布前的构建系统选择 | 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。（[记录](../reports/research-engineering-b.md#eng-080)） |
| [PRO-053](../cases/product/PRO-053.yaml) | sourced | WhatsApp 2011-02-22 v2.6群聊；2011-02-22 功能公布、继续使用结果未知 | 2011原始群聊发布有具体平台、人数和退出规则，足以作关系图扩展预测。（[记录](../reports/research-product.md#pro-053)） |
| [ENG-081](../cases/engineering/ENG-081.yaml) | sourced | Lambda Extensions 2020 预览生命周期；2020-10-08 API 预览使用时 | 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。（[记录](../reports/research-engineering-b.md#eng-081)） |
| [PRO-054](../cases/product/PRO-054.yaml) | sourced | GitHub Student Developer Pack 2014-10-07；2014-10-07 发布、未来职业转化未知 | 原始发布确认学生免费套装、成本定位与资格，能评估长期渠道。（[记录](../reports/research-product.md#pro-054)） |
| [ENG-082](../cases/engineering/ENG-082.yaml) | sourced | 2025-06-12 Workers KV 依赖事故；2025-06-12 故障响应早期；尚未披露根因 | 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。（[记录](../reports/research-engineering-b.md#eng-082)） |
| [INV-028](../cases/investing/INV-028.yaml) | sourced | Twitch 2012 投资建议；2012-07-07 备忘录形成时 | 直接 memo 支持直播产品和主播行为，不重复 2011 拆分节点。（[记录](../reports/research-investing.md#inv-028)） |
| [ENG-083](../cases/engineering/ENG-083.yaml) | sourced | Notion 2021 PostgreSQL 分片迁移；2021 年迁移键选择前；具体决策日未知 | 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。（[记录](../reports/research-engineering-b.md#eng-083)） |
| [PRO-055](../cases/product/PRO-055.yaml) | blocked | Twitter 初期字数约束（2006）；2006规则节点未核 | 2017官方字数实验页面读取404；未取得可读2006原始字符规则和SMS来源。（[记录](../reports/research-product.md#pro-055)） |
| [ENG-084](../cases/engineering/ENG-084.yaml) | blocked | Netflix 2012 Open Connect 发布；2012-06-04 网络扩展决策；首批试点已存在 | Open Connect 发布可核，缺同地区命中率及交付、部署完整成本。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-b.md#eng-084)） |
| [PRO-056](../cases/product/PRO-056.yaml) | blocked | Slack 按活跃成员计费（2013—）；候选单版billing规则未锁定 | 2019 S-1证实fair billing credits，但尚无该版账单活跃定义与触发窗口，不能误用DAU定义。（[记录](../reports/research-product.md#pro-056)） |
| [ENG-085](../cases/engineering/ENG-085.yaml) | sourced | CockroachDB v20.1 串行化冲突与重试；v20.1 事务重试判断；具体执行时间非历史事故 | 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。（[记录](../reports/research-engineering-b.md#eng-085)） |
| [INV-029](../cases/investing/INV-029.yaml) | sourced | Coinbase 2013 Series A 之后的运营验证；2013-05-22 A 轮公告后，12 月 B 轮前 | 公司同期融资公告确认独立 A 轮和参与者，任务可限定下一项验证而非精确投资定价。（[记录](../reports/research-investing.md#inv-029)） |
| [ENG-086](../cases/engineering/ENG-086.yaml) | blocked | Google Piper 2016 论文；2016 论文；具体协作决策时点未核定 | 只核到论文题名、作者与 2016 发表信息，未读到支持变更治理的正文。（[记录](../reports/research-engineering-b.md#eng-086)） |
| [PRO-057](../cases/product/PRO-057.yaml) | sourced | BlackBerry 2016-09-28 硬件开发外包决策；2016-09-28 决策公布；后续转型结果隐藏 | 同期财报说明终止内部硬件、授权安排及软件客户结果，可评估能力迁移，区别非GAAP。（[记录](../reports/research-product.md#pro-057)） |
| [ENG-087](../cases/engineering/ENG-087.yaml) | sourced | React Server Components RFC 0188；RFC 修订文本的方案评估；不能声称全部语义来自 2020 首稿 | 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。（[记录](../reports/research-engineering-b.md#eng-087)） |
| [PRO-058](../cases/product/PRO-058.yaml) | blocked | Uber 2010-11 Samasource活动需求峰值；活动前配车；当晚7—8点结果隐藏，精确活动日未独立核 | 同城时段供需现象可核，缺同口径等待、价格、车辆与交易量。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-product.md#pro-058)） |
| [ENG-088](../cases/engineering/ENG-088.yaml) | sourced | Jens Axboe io_uring 接口设计论文；2019 接口设计比较；论文当前修订日期未显示 | 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。（[记录](../reports/research-engineering-b.md#eng-088)） |
| [INV-030](../cases/investing/INV-030.yaml) | blocked | Convoy 2023 关闭前现金生存诊断；2023-10-19 关闭公告前；缺可用事前现金材料 | CEO 原始备忘录经媒体完整转载可核实关闭与当事人解释，但不能支持关闭前现金周期的竞争假说诊断。（[记录](../reports/research-investing.md#inv-030)） |
| [ENG-089](../cases/engineering/ENG-089.yaml) | sourced | ISCA 2014 RowHammer 实验；2014 论文实验观察前；不是后续提权事件 | 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。（[记录](../reports/research-engineering-b.md#eng-089)） |
| [PRO-059](../cases/product/PRO-059.yaml) | blocked | Zappos 先拍摄当地鞋店商品（1999）；1999拍摄本地鞋店试验未核 | 原候选摄影售鞋故事只检索到二手MVP复述，未定位原始创始人记录或交易证据。（[记录](../reports/research-product.md#pro-059)） |
| [ENG-090](../cases/engineering/ENG-090.yaml) | sourced | GitLab 2017-01-31 数据库删除及恢复；2017-01-31 误删后恢复路径选择 | 直接一手材料支持事件或版本行为；完整 Case QA 尚未执行。（[记录](../reports/research-engineering-b.md#eng-090)） |
| [PRO-060](../cases/product/PRO-060.yaml) | blocked | Todoist Recurring Tasks（2010s）；2010s版本未锁定 | 未找到2010s单次recurring功能快照与分群/干预；当前帮助页读取失败，不能建立留存归因。（[记录](../reports/research-product.md#pro-060)） |
| [ENG-091](../cases/engineering/ENG-091.yaml) | sourced | Vitess v5.0 Primary Vindex 文档样例；v5.0 文档快照，2020-02-04；非 2010 首发行为 | 一手材料直接支持 artifact 或事件行为；不是 ready。（[记录](../reports/research-engineering-b.md#eng-091)） |
| [INV-031](../cases/investing/INV-031.yaml) | blocked | Atlassian 2002–2005 自举经营模式的局部选择；2002–2005 具体扩张决定尚未锁定 | 创始人 2010 讲话支持历史经营模式，但未定位 Phase 2 所要求的早期单次经营选择及其结果。（[记录](../reports/research-investing.md#inv-031)） |
| [ENG-092](../cases/engineering/ENG-092.yaml) | sourced | 2011 Zab 论文恢复阶段；2011 协议恢复，旧 leader 失效后 | 一手材料直接支持 artifact 或事件行为；不是 ready。（[记录](../reports/research-engineering-b.md#eng-092)） |
| [PRO-061](../cases/product/PRO-061.yaml) | blocked | Robinhood Referral 免费股票（2015—）；2015—具体奖励轮次尚未锁定 | 申报入口存在但正文读取失败；奖励支出和有效持续账户尚未逐项核实。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-product.md#pro-061)） |
| [ENG-093](../cases/engineering/ENG-093.yaml) | sourced | GitHub 团队 2021 迁移 Codespaces；2021 团队开发环境迁移前，具体决策日未知 | 一手材料直接支持 artifact 或事件行为；不是 ready。（[记录](../reports/research-engineering-b.md#eng-093)） |
| [PRO-062](../cases/product/PRO-062.yaml) | blocked | Datadog 免费试用到企业监控（2010—2019）；具体试用采购节点未确定 | 找到Datadog2019 S-1入口但未核具体试用转组织购买的角色和证据，不能用平台总增长替代。（[记录](../reports/research-product.md#pro-062)） |
| [ENG-094](../cases/engineering/ENG-094.yaml) | sourced | gRPC 2015 设计原则；2015-09-08 API 选型 | 一手材料直接支持 artifact 或事件行为；不是 ready。（[记录](../reports/research-engineering-b.md#eng-094)） |
| [INV-032](../cases/investing/INV-032.yaml) | blocked | Reddit 2024 IPO 定价；2024-03-20 定价前 | 定价结果可核，事前完整财务与稀释股本尚未抽取。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing.md#inv-032)） |
| [ENG-095](../cases/engineering/ENG-095.yaml) | sourced | JDK 9 G1 回收器规范；JDK 9 的暂停目标与区域选择 | 一手材料直接支持 artifact 或事件行为；不是 ready。（[记录](../reports/research-engineering-b.md#eng-095)） |
| [PRO-063](../cases/product/PRO-063.yaml) | sourced | Google Maps Navigation 2009-10-28 Android2.0 beta；2009-10-28 新导航已说明、采用未知 | 2009原始Google发布有任务前后路径和限制，留存因果明确未知。（[记录](../reports/research-product.md#pro-063)） |
| [ENG-096](../cases/engineering/ENG-096.yaml) | blocked | Twitter 2013 Timelines at Scale 演讲；2012—2014 候选，待取得讲稿正文 | 页面确认当事人演讲存在，但本轮未取得可核查明星账号混合扇出的正文。（[记录](../reports/research-engineering-b.md#eng-096)） |
| [PRO-064](../cases/product/PRO-064.yaml) | blocked | Spotify 2017广告免费与Premium经济性；2018-02-28 公开2017财报后、定性经济性判断前 | 分部经济性可核，缺可归属成本和同一转化口径来回答原数量问题。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-product.md#pro-064)） |
| [ENG-097](../cases/engineering/ENG-097.yaml) | sourced | Google 2020-12-14 身份服务事故；2020-12-14 错误出现后的诊断起点 | 一手材料直接支持 artifact 或事件行为；不是 ready。（[记录](../reports/research-engineering-b.md#eng-097)） |
| [INV-033](../cases/investing/INV-033.yaml) | blocked | Blue Apron 2017 上市客户贡献口径；2017-06-28 招股书发布后，交割前 | 招股书有 cohort 收入与贡献，但 94 美元 CPC 采用更广的累计获客窗口，不能直接视作同 cohort CAC；原回本主线缺匹配输入。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing.md#inv-033)） |
| [ENG-098](../cases/engineering/ENG-098.yaml) | sourced | runc CVE-2019-5736 维护者通告；2019-02-11 通告发布时的升级决定 | 一手材料直接支持 artifact 或事件行为；不是 ready。（[记录](../reports/research-engineering-b.md#eng-098)） |
| [PRO-065](../cases/product/PRO-065.yaml) | sourced | Google Reader 关闭（2013）；2013-03-13 关闭公告公布后，评价退出安排前 | 当期关闭公告直接给出公司理由与退出安排；无足以量化资源机会成本的公开数据。（[记录](../reports/research-product.md#pro-065)） |
| [ENG-099](../cases/engineering/ENG-099.yaml) | blocked | FoundationDB 2013 事务层候选；2013 版本未找到可读证据 | 当前 8.0 指南可证冲突集合语义，不能据此确认 2013 版本。（[记录](../reports/research-engineering-b.md#eng-099)） |
| [PRO-066](../cases/product/PRO-066.yaml) | sourced | Apple App Store 上线（2008）；2008-06-09 宣布分发规则后、七月实际采用前 | 上线前分成与发布后分发行为均有同期官方公告；下载不等于长期网络效应。（[记录](../reports/research-product.md#pro-066)） |
| [ENG-100](../cases/engineering/ENG-100.yaml) | sourced | TypeScript 3.4 增量构建；2019-03-29 版本特性使用 | 一手材料直接支持 artifact 或事件行为；不是 ready。（[记录](../reports/research-engineering-b.md#eng-100)） |
| [INV-034](../cases/investing/INV-034.yaml) | blocked | Superhuman 2019 Series B 与独立付费 cohort；2019-06-27 投资公告后 | 独立融资记录可核，缺 PMF 问卷之外的付费留存和服务成本 cohort。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing.md#inv-034)） |
| [ENG-101](../cases/engineering/ENG-101.yaml) | sourced | Uber Schemaless 2016 架构文章；2016 文档中的实体与访问路径选择 | 一手直接材料可核查事件或发布行为，尚未Case QA。（[记录](../reports/research-engineering-b.md#eng-101)） |
| [PRO-067](../cases/product/PRO-067.yaml) | blocked | Twitch 从 Justin.tv 拆分（2011）；2011-06-06公开beta发布 | 同期公告确认垂直产品与迁移流程，但未找到拆分前游戏内容相对其他类别的集中度或行为比较，不能验证识别高价值子群的关键前提。（[记录](../reports/research-product.md#pro-067)） |
| [ENG-102](../cases/engineering/ENG-102.yaml) | sourced | Git LFS 2015 公告；2015-04-08 早期采用决定 | 一手直接材料可核查事件或发布行为，尚未Case QA。（[记录](../reports/research-engineering-b.md#eng-102)） |
| [PRO-068](../cases/product/PRO-068.yaml) | sourced | GitHub Dependabot 集成（2019）；2019-05-23公开beta发布后，评估审查流程前 | 2019公开beta清楚记录安全修复如何嵌入PR工作流；只验证机制和已发布行为，不把所有依赖升级当安全修复成效。（[记录](../reports/research-product.md#pro-068)） |
| [ENG-103](../cases/engineering/ENG-103.yaml) | sourced | PEP3156 asyncio 回调与协作调度；Python3.4 对应 PEP 接口设计，非真实线上事故 | 一手直接材料可核查事件或发布行为，尚未Case QA。（[记录](../reports/research-engineering-b.md#eng-103)） |
| [INV-035](../cases/investing/INV-035.yaml) | sourced | MongoDB 2015—2017 融资；2017-09-21公开S1资本窗口，评估免费采用转付费能力；不声称当年云厂商均已提供同名托管MongoDB。 | 2017-09-21 MongoDB S1直接记录AGPL、免费/付费转化、Atlas商业结果与云竞争；不用2018 SSPL或2019 DocumentDB倒灌。（[记录](../reports/research-investing-a.md#inv-035)） |
| [ENG-104](../cases/engineering/ENG-104.yaml) | sourced | Cloudflare 2025-11-18 Bot Management 故障；2025-11-18 11:20 UTC 初始诊断 | 一手直接材料可核查事件或发布行为，尚未Case QA。（[记录](../reports/research-engineering-b.md#eng-104)） |
| [PRO-069](../cases/product/PRO-069.yaml) | blocked | TikTok 收购 Musical.ly（2017—2018）；2018-08-01整合公告；网页标注08-02 | 整合公告验证身份、粉丝和内容自动迁移，但未取得迁移后创作者持续发布或流失行为材料；不能用自动升级等同预期创作者迁移。（[记录](../reports/research-product.md#pro-069)） |
| [ENG-105](../cases/engineering/ENG-105.yaml) | sourced | OSDI2006 Chubby 锁服务论文；2006 客户端 lease 失效及延迟请求判断 | 一手直接材料可核查事件或发布行为，尚未Case QA。（[记录](../reports/research-engineering-b.md#eng-105)） |
| [PRO-070](../cases/product/PRO-070.yaml) | blocked | Figma 多人光标（2016—）；2016-09-28多人编辑发布 | 官方首年回顾明确2016-09-28发布多人编辑及设计评审用途，但未取得一场具体远程评审的参与任务、光标位置及可观察协调行为；不能用泛称协作代替单场材料。（[记录](../reports/research-product.md#pro-070)） |
| [ENG-106](../cases/engineering/ENG-106.yaml) | sourced | Language Server Protocol 2016 联合发布；2016-06-27 语言服务接口决策 | 一手直接材料可核查事件或发布行为，尚未Case QA。（[记录](../reports/research-engineering-b.md#eng-106)） |
| [INV-036](../cases/investing/INV-036.yaml) | blocked | Snowflake 2012—2014 早期融资；2014 SeriesB融资决策前，具体可知客户材料未定；公告日不自动等于轮次关闭日。 | 2014原始融资公告确认SeriesB及累计26m，但所需客户采购任务/替代决策证据未取得；不能把厂商90%成本宣传当实测。（[记录](../reports/research-investing-a.md#inv-036)） |
| [ENG-107](../cases/engineering/ENG-107.yaml) | sourced | Equifax2017 漏洞修补与资产识别；2017-03 Struts 漏洞通告后；完整报告为事后材料 | 一手直接材料可核查事件或发布行为，尚未Case QA。（[记录](../reports/research-engineering-b.md#eng-107)） |
| [PRO-071](../cases/product/PRO-071.yaml) | sourced | Netflix 从单次租赁转向订阅（1999）；1999-12-16 Marquee公开发布后，评估收费摩擦前 | 1999同期公告给出确切订阅规则，需修正候选常见的无限租赁说法；只支持任务与收费机制，不证明留存效果。（[记录](../reports/research-product.md#pro-071)） |
| [ENG-108](../cases/engineering/ENG-108.yaml) | blocked | The Tail at Scale 2013 论文；2013 paper snapshot 待取得正文 | 只取得摘要，未读到完整尾延迟分布及额外请求工作量。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-b.md#eng-108)） |
| [PRO-072](../cases/product/PRO-072.yaml) | blocked | Notion Enterprise 安全功能（2020—）；2020-11-19 SCIM发布 | 当期发布核实Enterprise的SCIM与SSO，但列客户名称没有真实采购阻碍与买方验证过程，尚不满足单项安全采购节点。（[记录](../reports/research-product.md#pro-072)） |
| [ENG-109](../cases/engineering/ENG-109.yaml) | sourced | OpenTelemetry2019 合并公告；2019 年合并方案；具体决策日未知 | 一手直接材料可核查事件或发布行为，尚未Case QA。（[记录](../reports/research-engineering-b.md#eng-109)） |
| [INV-037](../cases/investing/INV-037.yaml) | sourced | Rivian 2021 IPO 估值；2021-11-01公开S1/A，最终IPO定价前；只用57–62美元预估区间，不能提前给78。 | 2021-11-01 S1/A提供事前价格区间、股本、产能、已交付量与capex；最终IPO另有原招股书支持。（[记录](../reports/research-investing-a.md#inv-037)） |
| [ENG-110](../cases/engineering/ENG-110.yaml) | blocked | Discord2022 Cassandra→Scylla 消息迁移；2022 messages 迁移前，具体切换日未知 | 消息迁移机制可核，缺同窗口总成本、资源、工作量和迁移投入。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-b.md#eng-110)） |
| [PRO-073](../cases/product/PRO-073.yaml) | sourced | Pinterest 从 Tote 演化（2009—2010）；Tote alpha观察到分享行为后、决定聚焦Pinterest前；确切日期未核实 | 2011原始投资备忘录回述Tote的alpha行为与访谈，支持任务假说辨别；没有购买转化数据，不把分享当作零购买的测量。（[记录](../reports/research-product.md#pro-073)） |
| [ENG-111](../cases/engineering/ENG-111.yaml) | sourced | Cloudflare2026-02-20 BYOIP 路由撤销；2026-02-20 撤销后外部连通性诊断 | 一手直接材料可核查事件或发布行为，尚未Case QA。（[记录](../reports/research-engineering-b.md#eng-111)） |
| [PRO-074](../cases/product/PRO-074.yaml) | sourced | Adobe 收购 Figma 失败（2022—2023）；2023-11-28 CMA初步发现公开后、最终交易结局前 | 交易未决时监管方公开竞争分析与最终公司公告可相互对照；监管判断仍是初步结论，不作为已证产品失败。（[记录](../reports/research-product.md#pro-074)） |
| [ENG-112](../cases/engineering/ENG-112.yaml) | sourced | Node.js v10.24.1 libuv 线程池文档；固定v10.24.1 API快照，非2009首发时行为 | 直接材料支持事件或artifact行为，完整训练未验收。（[记录](../reports/research-engineering-b.md#eng-112)） |
| [INV-038](../cases/investing/INV-038.yaml) | blocked | Peloton 2018—2019 Pre-IPO；2019-09-10上市前文件公开后，评估硬件抵扣获客成本的口径。 | 有公司净 CAC 和贡献定义，缺同 cohort 留存及完整现金成本时序。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing-a.md#inv-038)） |
| [ENG-113](../cases/engineering/ENG-113.yaml) | sourced | etcd v3.3 灾难恢复规则；v3.3 集群失去quorum后的恢复决定 | 直接材料支持事件或artifact行为，完整训练未验收。（[记录](../reports/research-engineering-b.md#eng-113)） |
| [PRO-075](../cases/product/PRO-075.yaml) | blocked | Upwork Elance 与 oDesk 合并（2013—2015）；2015-05 Upwork重启、8月迁移前 | 2018 S-1回述2015迁移与客户损失，但缺公告窗口单一服务品类的供需和账户迁移规则，不能由总市场规模替代品类流动性。（[记录](../reports/research-product.md#pro-075)） |
| [ENG-114](../cases/engineering/ENG-114.yaml) | sourced | Gitpod Classic snapshot 分享规则；2026-10-25读取的Classic文档快照；不能倒推2020首发 | 直接材料支持事件或artifact行为，完整训练未验收。（[记录](../reports/research-engineering-b.md#eng-114)） |
| [PRO-076](../cases/product/PRO-076.yaml) | blocked | Notion 数据库视图与关联（2018—）；2018后某历史版本待核实 | 当前帮助文档验证关系与上手路径，但未给历史版本日期，不能将当前默认单向/双向选项回填2018；单工作流仍缺可冻结的历史快照。（[记录](../reports/research-product.md#pro-076)） |
| [ENG-115](../cases/engineering/ENG-115.yaml) | sourced | XZ5.6.0/5.6.1后门发现；2024-03-29公开披露前的异常排查 | 直接材料支持事件或artifact行为，完整训练未验收。（[记录](../reports/research-engineering-b.md#eng-115)） |
| [INV-039](../cases/investing/INV-039.yaml) | sourced | Canva 2013—2015 早期融资；2015 SeriesA公告工件，Canva for Work已推出；精确公开日正文无日期，官方10年timeline将该文归2015。 | Canva2015创始人融资原文可读，支持用户分群、Work采用与融资结果；付费留存未知正好限定尽调问题。（[记录](../reports/research-investing-a.md#inv-039)） |
| [ENG-116](../cases/engineering/ENG-116.yaml) | sourced | Envoy xDS当前文档ACK语义；2026-10-25文档快照；不是2017语义断言 | 直接材料支持事件或artifact行为，完整训练未验收。（[记录](../reports/research-engineering-b.md#eng-116)） |
| [PRO-077](../cases/product/PRO-077.yaml) | blocked | 候选 Duolingo 2010s App Store 排名活动（未定位）；已确认 2013 获奖；活动未定位 | 找到 2013 App of the Year 认可，但未找到具体排名驱动活动、时序及曝光行为数据。（[记录](../reports/research-product.md#pro-077)） |
| [ENG-117](../cases/engineering/ENG-117.yaml) | blocked | ZippyDB SSD单位成本优化候选；2010s具体优化未确认 | 未找到原规划单次 SSD 优化和同负载可归属成本。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-b.md#eng-117)） |
| [PRO-078](../cases/product/PRO-078.yaml) | sourced | Instagram Stories 发布（2016）；2016-08-02美国发布后、评估用户行为前 | 同期官方发布清楚记录临时分享规则和减少过度发帖担心的主张；未证明发布频率或心理压力的因果变化。（[记录](../reports/research-product.md#pro-078)） |
| [ENG-118](../cases/engineering/ENG-118.yaml) | sourced | Knight Capital2012部署事故SEC调查；2012-08-01市场开盘前后的发布检查 | 直接材料支持事件或artifact行为，完整训练未验收。（[记录](../reports/research-engineering-b.md#eng-118)） |
| [INV-040](../cases/investing/INV-040.yaml) | blocked | Quibi 2020 关闭；2020-10-21wind-down决策之前，具体现金/承诺成本输入缺失。 | Quibi创始人2020关闭原信已读，真实停止投入可核；数量校准所需现金、承诺支出及退出回收未公开。（[记录](../reports/research-investing-a.md#inv-040)） |
| [ENG-119](../cases/engineering/ENG-119.yaml) | sourced | Google F1 VLDB2013论文；2013论文中的F1/Spanner分层判断 | 直接材料支持事件或artifact行为，完整训练未验收。（[记录](../reports/research-engineering-b.md#eng-119)） |
| [PRO-079](../cases/product/PRO-079.yaml) | sourced | Netflix 取消邮寄 DVD 与流媒体捆绑（2011）；2011-09 Qwikster计划公布后、十月撤回前；具体宣布日未以一手公告复核 | CEO同期财报电话会直接区分价格取消波与Qwikster品牌决策，支持拆分取舍复盘；无法把全部订户损失归因Qwikster。（[记录](../reports/research-product.md#pro-079)） |
| [ENG-120](../cases/engineering/ENG-120.yaml) | blocked | NATS JetStream2020候选；2020具体preview语义待核定 | 官方2.2发布说明可证持久流、至少一次及窗口去重，但不能据此认定是2020发布契约。（[记录](../reports/research-engineering-b.md#eng-120)） |
| [PRO-080](../cases/product/PRO-080.yaml) | sourced | Superhuman 2017—2018 PMF 调查与分群路线图；首次调查已回收、细分路线图尚待制定；具体日未知 | 创始人原文给出调查对象、问题、分群过程及后来问卷分数；足以做调查证据解读，不能据此证明因果 PMF。（[记录](../reports/research-product.md#pro-080)） |
| [ENG-121](../cases/engineering/ENG-121.yaml) | sourced | Pants2.0依赖推断设计；2020-10-29依赖声明选择 | 直接材料支持事件或artifact行为，完整训练未验收。（[记录](../reports/research-engineering-b.md#eng-121)） |
| [INV-041](../cases/investing/INV-041.yaml) | blocked | Cloudflare 2014—2019 融资；拟选2014一轮融资，但关闭日及该时点业务指标未由一手材料锁定。 | 2015官方融资说明已读，但规划明确2014轮次决策边界；该文2015网络/产品指标不能回填2014。（[记录](../reports/research-investing-a.md#inv-041)） |
| [ENG-122](../cases/engineering/ENG-122.yaml) | blocked | Akka actor重启状态候选；2010s版本语义待原文 | 本轮未取得可读的指定旧版监督/持久化正文。（[记录](../reports/research-engineering-b.md#eng-122)） |
| [PRO-081](../cases/product/PRO-081.yaml) | blocked | Twilio Developer-first API（2008—2016）；2016-10-07公开披露所述当前模式 | 2016 S-1验证试用、API及采购角色，但没有一个具体早期集成从开发者交接到采购的过程；不能用八年developer-first总述代替节点。（[记录](../reports/research-product.md#pro-081)） |
| [ENG-123](../cases/engineering/ENG-123.yaml) | sourced | OpenAPI3.0.0正式规范；2017-07-26契约设计时 | 直接资料可证事件或artifact；完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-123)） |
| [PRO-082](../cases/product/PRO-082.yaml) | blocked | Twitter 改为 X 的品牌重塑（2023）；2023-07品牌更名窗口 | 已读同期报道及其原帖链接，但官方X博客与CEO原帖正文抓取失败，且没有品牌识别或广告信任行为测量；不足以核实计划要求的品牌结果。（[记录](../reports/research-product.md#pro-082)） |
| [ENG-124](../cases/engineering/ENG-124.yaml) | sourced | Kubernetes CVE-2019-11253官方披露；2019安全通告后的补丁/授权决定 | 直接资料可证事件或artifact；完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-124)） |
| [INV-042](../cases/investing/INV-042.yaml) | sourced | Zoom 2013—2015 融资；2013-09-24 SeriesB公开材料，评估新进入窗口；不使用疫情后增长。 | Zoom2013同期公司融资稿有产品、企业采用与价格，适合选择企业采用反证。（[记录](../reports/research-investing-a.md#inv-042)） |
| [ENG-125](../cases/engineering/ENG-125.yaml) | sourced | Cloudflare2019-07-02 WAF正则事故；2019-07-02 13:45 UTC初始报警 | 直接资料可证事件或artifact；完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-125)） |
| [PRO-083](../cases/product/PRO-083.yaml) | blocked | GitHub 开源贡献网络（2008—）；2008-12 Fork Queue推出时 | 2008协作功能与复用路径有同期原文，但未取得一次具体跨项目贡献关系闭环；功能存在不足以证明难迁移贡献网络。（[记录](../reports/research-product.md#pro-083)） |
| [ENG-126](../cases/engineering/ENG-126.yaml) | blocked | TiDB2016 Percolator候选；2016具体版本尚未核定 | 官方深度文档可证primary/secondary锁恢复机制，但未证其内容在2016版本的具体状态。（[记录](../reports/research-engineering-b.md#eng-126)） |
| [PRO-084](../cases/product/PRO-084.yaml) | sourced | Adobe Creative Cloud Libraries（2014—）；2016-06-21 Photoshop CC更新后、判断素材交付方式前 | 2016具体版本明确跨文档/应用共享与只读权限，可据此判断单素材复用及替代边界；没有退出成本的实际测量。（[记录](../reports/research-product.md#pro-084)） |
| [ENG-127](../cases/engineering/ENG-127.yaml) | sourced | Buck2 2023公开的单一增量图；2023-04-06发布时的增量计算设计 | 直接资料可证事件或artifact；完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-127)） |
| [INV-043](../cases/investing/INV-043.yaml) | blocked | Klarna 2021—2022 估值重定价；2021-06-10融资后、2022新融资宣布前；两轮比较材料只能在后续揭示。 | 两轮 headline 估值可核，缺完整股本、每股价格和权利，不能推出旧股实际损失。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing-a.md#inv-043)） |
| [ENG-128](../cases/engineering/ENG-128.yaml) | blocked | TimescaleDB2017 hypertables候选；2017快照待取得 | 当前文档含后续架构，无法确认 2017 同窗口数据及版本。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-b.md#eng-128)） |
| [PRO-085](../cases/product/PRO-085.yaml) | blocked | Zoom 会议邀请链接传播（2013—2020）；2019-03-22公开2019模式 | 2019 S-1有受邀者转host的公司叙述及大客户免费起点统计，但未取得同版首次主持身份步骤和受邀转主持行为分母；不能把大客户55%当受邀者转化率。（[记录](../reports/research-product.md#pro-085)） |
| [ENG-129](../cases/engineering/ENG-129.yaml) | sourced | 2015浏览器Promise微任务实验；2015-08-17文中测试片段运行前 | 直接资料可证事件或artifact；完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-129)） |
| [PRO-086](../cases/product/PRO-086.yaml) | blocked | TikTok For You 默认推荐流（2018—2020）；2020-06-18公开说明的产品快照 | 2020官方解释验证无关注图的新用户输入和推荐流程，但未取得首轮分群/行为比较，不能用全站主要停留在For You替代冷启动假说证据。（[记录](../reports/research-product.md#pro-086)） |
| [ENG-130](../cases/engineering/ENG-130.yaml) | sourced | YouTube2011 Hydra并行视频处理；2011提速设计；具体决策日未知 | 直接资料可证事件或artifact；完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-130)） |
| [INV-044](../cases/investing/INV-044.yaml) | blocked | DoorDash 2020 IPO 前 S-1/A 中的 2019 年全年利润桥；2020-11-30 S-1/A 已公开、IPO 定价之前；仅使用 2019 全年同窗口 | 公司总体口径不能替代可归属履约成本；本轮未核齐原数量输入。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing-b.md#inv-044)） |
| [ENG-131](../cases/engineering/ENG-131.yaml) | sourced | Bazel3.7.0 Starlark扩展规则；3.7.0文档快照，属于2017—2020范围 | 直接资料可证事件或artifact；完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-131)） |
| [PRO-087](../cases/product/PRO-087.yaml) | blocked | Workers 2023-09-28 CPU-time 新计价公告；2023-09-28 公告后、2023-10-31 选择迁移前 | 两版政策价格之外，同一可追溯请求和执行量尚未核齐。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-product-b.md#pro-087)） |
| [ENG-132](../cases/engineering/ENG-132.yaml) | sourced | GitHub2018-10-21数据库网络分区事故；2018-10-21 23:13 UTC恢复决策 | 直接来源支持所选artifact或事件，完整Case QA未执行。（[记录](../reports/research-engineering-b.md#eng-132)） |
| [PRO-088](../cases/product/PRO-088.yaml) | sourced | Figma 2015-12-03 Preview 后继续投入浏览器协作；2015-12-03 Preview 公开后、决定下一步协作需求验证前 | 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。（[记录](../reports/research-product-b.md#pro-088)） |
| [ENG-133](../cases/engineering/ENG-133.yaml) | sourced | Cassandra2.1可调一致性规则；2.1文档快照；读请求发出前 | 直接来源支持所选artifact或事件，完整Case QA未执行。（[记录](../reports/research-engineering-b.md#eng-133)） |
| [INV-045](../cases/investing/INV-045.yaml) | sourced | DoorDash 2014 年 5 月 Sequoia 领投 A 轮；2014 年 A 轮投资决定之前；公开回顾只用于重建，不把后来的扩城成绩前置 | 已阅读直接来源，支持可辨识事件或原始文件及其披露结果；训练数据完整性与 Case QA 尚待完成。（[记录](../reports/research-investing-b.md#inv-045)） |
| [ENG-134](../cases/engineering/ENG-134.yaml) | sourced | Gradle6.6 Configuration Cache；2020年6.6配置结果复用前 | 直接来源支持所选artifact或事件，完整Case QA未执行。（[记录](../reports/research-engineering-b.md#eng-134)） |
| [PRO-089](../cases/product/PRO-089.yaml) | blocked | GitLab / Goldman Sachs 企业采用候选，采购时点未闭合；待确认一次集团采购决定及日期；不以当前客户页替代历史合同 | 真实企业采用有直接材料，但采购节点时间和部署控制证据未闭合，不能支持规划要求的当时取舍。（[记录](../reports/research-product-b.md#pro-089)） |
| [ENG-135](../cases/engineering/ENG-135.yaml) | sourced | npm event-stream2018依赖劫持；2018-11-26恶意包告警后的应对 | 直接来源支持所选artifact或事件，完整Case QA未执行。（[记录](../reports/research-engineering-b.md#eng-135)） |
| [PRO-090](../cases/product/PRO-090.yaml) | sourced | Google 2022-09-29 宣布关闭 Stadia 消费服务；2022-09-29 宣布关闭前；准确内部决策日期未知 | 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。（[记录](../reports/research-product-b.md#pro-090)） |
| [ENG-136](../cases/engineering/ENG-136.yaml) | sourced | Druid2014论文实时摄取与handoff；2014论文的单事件查询可见性 | 直接来源支持所选artifact或事件，完整Case QA未执行。（[记录](../reports/research-engineering-b.md#eng-136)） |
| [INV-046](../cases/investing/INV-046.yaml) | sourced | FTX 2021-07-20 公告的 9 亿美元 B 轮；2021 年 7 月该轮尽调/投资决定前；公开融资公告为同时期 issuer claim | 已阅读直接来源，支持可辨识事件或原始文件及其披露结果；训练数据完整性与 Case QA 尚待完成。（[记录](../reports/research-investing-b.md#inv-046)） |
| [ENG-137](../cases/engineering/ENG-137.yaml) | blocked | Linux epoll2002候选；2002接口与性能比较未核完整 | 缺 2002 接口快照及同口径连接数、就绪事件与性能测量。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-b.md#eng-137)） |
| [PRO-091](../cases/product/PRO-091.yaml) | sourced | Substack 2022-04-12 recommendations beta；2022-04-12 发布后、预测作者推荐网络效果前 | 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。（[记录](../reports/research-product-b.md#pro-091)） |
| [ENG-138](../cases/engineering/ENG-138.yaml) | sourced | Stripe2017幂等API设计文章；2017-02-22契约快照 | 直接来源支持所选artifact或事件，完整Case QA未执行。（[记录](../reports/research-engineering-b.md#eng-138)） |
| [PRO-092](../cases/product/PRO-092.yaml) | blocked | Google Photos 2015-05-28 自动备份任务；2015-05-28 上线后、用户选择自动备份前 | 备份到检索复用机制已核，但规划要求的同版导出和退出边界缺直接材料。（[记录](../reports/research-product-b.md#pro-092)） |
| [ENG-139](../cases/engineering/ENG-139.yaml) | sourced | Cloudflare2022-06-21网络中断；2022-06-21 06:27 UTC配置部署后 | 直接来源支持所选artifact或事件，完整Case QA未执行。（[记录](../reports/research-engineering-b.md#eng-139)） |
| [INV-047](../cases/investing/INV-047.yaml) | blocked | Better SPAC 延期期间融资：最后一笔续命融资身份尚未闭合；待定位最后一笔续命融资签署前；不能把 2021 bridge 与 2023 债务修改合成一次交易 | 可确认有多笔 bridge/债务修改，但尚未闭合规划要求的最后一笔续命融资身份，且缺完整合同、股本及同时点跑道。（[记录](../reports/research-investing-b.md#inv-047)） |
| [ENG-140](../cases/engineering/ENG-140.yaml) | blocked | Consul2015多数据中心架构候选；2015版本快照未取得 | 当前官方架构可证Raft角色，但尚无2015版本与单请求路径的原始材料。（[记录](../reports/research-engineering-b.md#eng-140)） |
| [PRO-093](../cases/product/PRO-093.yaml) | blocked | Clubhouse 2021 opening-day 取消邀请候选；2021 年取消 waitlist 前；精确发布日期待直接材料确认 | 尝试直接访问官方材料均失败；搜索摘要不能替代原文，且缺同批邀请用户的长期关系行为证据。（[记录](../reports/research-product-b.md#pro-093)） |
| [ENG-141](../cases/engineering/ENG-141.yaml) | sourced | Atom1.32 Tree-sitter发布；2018-10-31局部编辑反馈判断 | 直接来源支持所选artifact或事件，完整Case QA未执行。（[记录](../reports/research-engineering-b.md#eng-141)） |
| [PRO-094](../cases/product/PRO-094.yaml) | blocked | Zoom 2018/2020 邀请加入流程候选；待锁定一个设备、版本和受邀加入任务 | 有同期标题和流程说明，但尚缺完整同版安装、身份与设备约束，无法确认主线摩擦边界。（[记录](../reports/research-product-b.md#pro-094)） |
| [ENG-142](../cases/engineering/ENG-142.yaml) | sourced | Workers2018 isolate执行环境设计；2018-11-09设计对比；不是2017首发全部承诺 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-142)） |
| [INV-048](../cases/investing/INV-048.yaml) | sourced | Palantir 2020-09-21 S-1/A：Acquire / Expand / Scale 交付披露；2020-09-21 公开文件之后、直接上市交易之前 | 已阅读直接来源，支持可辨识事件或原始文件及其披露结果；训练数据完整性与 Case QA 尚待完成。（[记录](../reports/research-investing-b.md#inv-048)） |
| [ENG-143](../cases/engineering/ENG-143.yaml) | sourced | Okta2023支持系统HAR泄漏；2023-10-13客户提供可疑IP后的日志选择 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-143)） |
| [PRO-095](../cases/product/PRO-095.yaml) | sourced | Apple 2016-06-08 宣布订阅资格与一年后分成增强；2016-06-08 公告后、开发者决定是否设计长期订阅前 | 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。（[记录](../reports/research-product-b.md#pro-095)） |
| [ENG-144](../cases/engineering/ENG-144.yaml) | sourced | MergeTree排序键文档artifact；2026-10-25读取快照；非2016所有语法 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-144)） |
| [PRO-096](../cases/product/PRO-096.yaml) | blocked | Calendly 2013 链接式预约初版候选；2013 初版上线时；精确功能版本未锁定 | 创办年份可核，但初版两边身份与预约流程缺同版证据；现有描述混合后续多年功能。（[记录](../reports/research-product-b.md#pro-096)） |
| [ENG-145](../cases/engineering/ENG-145.yaml) | sourced | C++11内存序工作草案文本；C++11语义由N3337镜像核对，草案发表于2012 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-145)） |
| [INV-049](../cases/investing/INV-049.yaml) | blocked | Wix 2007-10-19 BVP 第二轮 seed 投资建议 memo；2007-10-19 memo 建议作出之前；memo 内估计和建议条款须标归属 | 网站总量或作者市场愿景不能等同可服务付费客群和支付意愿。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing-b.md#inv-049)） |
| [ENG-146](../cases/engineering/ENG-146.yaml) | sourced | React16.8 Hooks稳定发布；2019-02-06引入Hooks的状态抽象 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-146)） |
| [PRO-097](../cases/product/PRO-097.yaml) | sourced | Figma 2019-01-29 Organization 套餐与 Uber 全公司迁移；2019-01-29 公布的 Organization 方案与 beta 客户反馈已知后，验证组织采购信号前 | 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。（[记录](../reports/research-product-b.md#pro-097)） |
| [ENG-147](../cases/engineering/ENG-147.yaml) | sourced | Facebook2021-10-04骨干网中断；2021-10-04网络维护命令执行后恢复决定 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-147)） |
| [PRO-098](../cases/product/PRO-098.yaml) | blocked | Horizon Workrooms 2021 beta；候选 2024 精简改动待一手核实；候选 2024 改动之前；确切日未验证 | 确认 2021 beta 和具体设备流程；2024 改动仅取得行业报道，未取得原始改动说明或用户行为材料，不能推断失败原因。（[记录](../reports/research-product.md#pro-098)） |
| [ENG-148](../cases/engineering/ENG-148.yaml) | sourced | Uber2016 Ringpop成员与请求转发设计；2016-02-04节点加入时路由判断 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-148)） |
| [INV-050](../cases/investing/INV-050.yaml) | blocked | Airbnb 2020-04-06 Silver Lake / Sixth Street 10 亿美元融资；2020-04-06 此笔融资同意前；后来的 4 月 first-lien 交易与 4 月 17 日修订均不并入首轮 | 融资身份与借款结果已核，但 4 月 6 日未修订签署合同及融资前现金预测不足，不能完成接受/等待的现金与条款选择。（[记录](../reports/research-investing-b.md#inv-050)） |
| [ENG-149](../cases/engineering/ENG-149.yaml) | sourced | GitHub Actions cache信任边界文档；2026-10-25文档快照；不是2019原始权限 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-149)） |
| [PRO-099](../cases/product/PRO-099.yaml) | sourced | eBay 1999 年报记录的交易后 Feedback Forum 规则；2000 年 1999 年报公开后，一次选择陌生交易对手前；不混入 1996 或后来卖家禁负评规则 | 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。（[记录](../reports/research-product-b.md#pro-099)） |
| [ENG-150](../cases/engineering/ENG-150.yaml) | blocked | Dropbox2016披露Magic Pocket迁移；2013—2015自建存储决策；具体内部决策日未知 | 迁移事实可核，缺同口径采购、运维、利用率与存储总成本。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-engineering-b.md#eng-150)） |
| [PRO-100](../cases/product/PRO-100.yaml) | blocked | Shopify 2009-06-02 App Store 首发：BaseSync 商品同步需求；2009-06-02 首发后、商家选择 BaseSync 外部扩展前 | 首发身份与单项插件用途已核，但规划需要的早期权限、数据及替代边界材料不足。（[记录](../reports/research-product-b.md#pro-100)） |
| [ENG-151](../cases/engineering/ENG-151.yaml) | sourced | LastPass2022备份窃取公开更新；2022-12-22获知备份被复制后的风险判断 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-151)） |
| [INV-051](../cases/investing/INV-051.yaml) | blocked | Dropbox 2018-02-23 S-1：客户/套餐与公司毛利口径；2018-02-23 S-1 公开后、IPO 定价之前 | 申报总体毛利不能分解个人和团队业务的完整归属成本。 尚未应用备用问题，原数量主线保持 blocked。（[记录](../reports/research-investing-b.md#inv-051)） |
| [ENG-152](../cases/engineering/ENG-152.yaml) | sourced | Elasticsearch2.x近实时检索文档；2.x一次写入确认后搜索前 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-152)） |
| [PRO-101](../cases/product/PRO-101.yaml) | sourced | Canva for Education 2019 澳大利亚学校 beta：教师布置与批改课堂作品；2019 beta 发布后，教师决定是否采用课堂作品任务前；原媒体 PDF 精确日未知 | 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。（[记录](../reports/research-product-b.md#pro-101)） |
| [ENG-153](../cases/engineering/ENG-153.yaml) | sourced | Erlang/OTP22 supervisor重启策略；OTP22固定文档一次子进程失败后 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-153)） |
| [PRO-102](../cases/product/PRO-102.yaml) | sourced | Dropbox 2008-09-11 公测上线的桌面文件夹同步；2008-09-11 公开上线前，已有 beta 与桌面客户端；精确内部设计决定日期未知 | 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。（[记录](../reports/research-product-b.md#pro-102)） |
| [ENG-154](../cases/engineering/ENG-154.yaml) | sourced | GitHub2021可复用workflow GA；2021-11-29文档示例的跨仓版本治理 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-154)） |
| [INV-052](../cases/investing/INV-052.yaml) | sourced | GitLab 2017-10-09 GV 领投 2000 万美元 C 轮；2017 C 轮投资决定前；使用此前已公布的企业套餐能力 | 已阅读直接来源，支持可辨识事件或原始文件及其披露结果；训练数据完整性与 Case QA 尚待完成。（[记录](../reports/research-investing-b.md#inv-052)） |
| [ENG-155](../cases/engineering/ENG-155.yaml) | sourced | Cloudflare2025-12-05 FL1/WAF解析改动事故；2025-12-05 08:47 UTC配置传播后 | 已读直接来源支持事件或artifact，完整Case QA尚未执行。（[记录](../reports/research-engineering-b.md#eng-155)） |
| [PRO-103](../cases/product/PRO-103.yaml) | blocked | Atlassian 2020-03-18 Jira Cloud 免费档全面推出；2020-03-18 公告后、小团队选择 Free 或升级前 | 免费发布日期和人数限制可核，但同版功能与迁移规则未闭合，无法完成完整采用/升级边界。（[记录](../reports/research-product-b.md#pro-103)） |
| [ENG-156](../cases/engineering/ENG-156.yaml) | blocked | Kubernetes2014—2016控制器候选；历史版本循环语义待原始快照 | 当前官方控制器开发约定可读，但未定位2014—2016版本artifact。（[记录](../reports/research-engineering-b.md#eng-156)） |
| [PRO-104](../cases/product/PRO-104.yaml) | sourced | Canva 2013-08-26 首次限量推出在线拖拽设计平台；2013-08-26 公开推出前，决定非设计师任务的产品组合；内部决定日期未知 | 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。（[记录](../reports/research-product-b.md#pro-104)） |
| [ENG-157](../cases/engineering/ENG-157.yaml) | rejected | 原Google Blaze2015候选与ENG080复用；替换提案待决；原候选2015；提案Rust2021升级决策另列 | 原候选按Phase2重复风险拒绝；真实替换提案为Rust1.52.0构建ICE及1.52.1默认禁用增量。（[记录](../reports/research-engineering-b.md#eng-157)） |
