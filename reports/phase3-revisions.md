# Phase 3 正式改题映射

保留全部日期、ID与原始候选素材。下列变更已正式采用；不是 Phase 4 或 ready 晋级。

| ID | 日期 | 动作 | 原题 | 现题 | 原动作 → 现动作 | 理由 |
|---|---|---|---|---|---|---|
| ENG-001 | 2027-01-01 | retain | Google Spanner（2012） | Google Spanner（2012） | causal-modeling → causal-modeling | 已逐条复审原核源的初始事实、证据、结局与未知：保留Google Spanner（2012）的单一范围；不要求实际练习不提供未经核实的逐次时钟值。 |
| INV-001 | 2027-01-02 | reframe | Arm 2023 IPO 估值 | Arm 2023 IPO：公开价格区间与基本股本 | quantitative-calibration → quantitative-calibration | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-001 | 2027-01-03 | reframe | 平台资源 API 的抽象边界 | 平台资源 API 的抽象边界 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-002 | 2027-01-04 | reframe | BuildKit Docker 分层缓存（2018—） | Docker 多阶段构建缓存教程（2019-07-02） | prediction-counterfactual → prediction-counterfactual | 2018候选版本未证实；正式改锚2019同期官方Maven教程，不填造Dockerfile或依赖。 |
| PRO-001 | 2027-01-05 | replace | Notion 早期产品重做（2015—2016） | Google Wave 2009预览至2010独立产品投入复核 | hypothesis-diagnosis → hypothesis-diagnosis | Notion原重做时间与因果材料不足，真实换为Google Wave的任务价值与技术喝彩判断；保留诊断动作，不声称已经识别失败原因。 |
| ENG-003 | 2027-01-06 | retain | Slack 2021 年 1 月服务中断 | Slack 2021 年 1 月服务中断 | evidence-selection → evidence-selection | 已逐条复审原核源的初始事实、证据、结局与未知：保留Slack 2021 年 1 月服务中断的单一范围；不要求未提供逐台机器原始日志；不得编造。 |
| PRO-002 | 2027-01-07 | retain | Pinterest Pin It 浏览器按钮（2010s） | Pinterest 2015 Pin It 保存路径改进 | causal-modeling → causal-modeling | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-004 | 2027-01-08 | reframe | Terraform Provider 协议演进（2016—2023） | Terraform v1.5.0 状态升级责任边界（2023） | boundary-transfer → boundary-transfer | 以已读v1.5.0官方固定tag生命周期契约替代未锁定的2016—2023泛称；保留状态升级单一问题。 |
| INV-002 | 2027-01-09 | reframe | Instacart 2020—2023 融资/上市 | Instacart 2023年报：净额收入与毛利边界 | quantitative-calibration → quantitative-calibration | 改用实际读到的2023年报，取消缺少成本分摊的上市前分部估值。 |
| DES-002 | 2027-01-10 | reframe | 移动端即时记录的第一分钟 | 移动端即时记录的第一分钟 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-005 | 2027-01-11 | reframe | Java ZGC 上线（2018—2023） | JDK 11 实验性 ZGC 的采用边界（2018） | constrained-decision → constrained-decision | JEP403缺口由Oracle JDK11同期release notes补齐；把需要未知负载基准的决定改为受明确支持边界约束的试用决策。 |
| PRO-003 | 2027-01-12 | retain | Adobe Creative Suite 转订阅 CC（2013） | Adobe Creative Suite 转订阅 CC（2013） | prediction-counterfactual → prediction-counterfactual | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-006 | 2027-01-13 | reframe | Figma Multiplayer 数据模型（2019—） | Figma 并发属性更新模型（2019） | boundary-transfer → hypothesis-diagnosis | 原持久化确认问题缺公开契约；改为2019原文直接公开的属性级冲突诊断，同一公司同一工件，无补造日志。 |
| PRO-004 | 2027-01-14 | reframe | Strava Segment 排行榜（2009—） | Strava 2024年末榜单异常清理与比较信号 | hypothesis-diagnosis → hypothesis-diagnosis | 早期回访因果缺数据；正式改为2024榜单比较信号的竞争假说诊断，不再推断排行榜创造留存。 |
| ENG-007 | 2027-01-15 | reframe | SolarWinds Orion 供应链攻击（2020） | SolarWinds SUNSPOT 构建注入取证（2021-01披露） | evidence-selection → evidence-selection | 签名验证不能直接证明源代码未被临时替换；将问题收窄为调查方实际分析工件上的构建期证据，避免未核独立重建。 |
| INV-003 | 2027-01-16 | reframe | Fiverr 2011 Series A | Fiverr 2011投资备忘录：交易热度与重复需求 | evidence-selection → evidence-selection | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-003 | 2027-01-17 | reframe | 可恢复的异步 Workflow | 可恢复的异步 Workflow | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-008 | 2027-01-18 | reframe | Discord Go 垃圾回收瓶颈（2019） | Discord Read States GC 尖峰复盘（2020公开） | hypothesis-diagnosis → hypothesis-diagnosis | 将未核实2019事故日纠正为2020-02-04公开复盘；保留其周期抖动诊断工件，不推定具体生产发生日。 |
| PRO-005 | 2027-01-19 | retain | Dropbox 推荐好友送空间（2008—2010） | Dropbox 推荐好友送空间（2008—2010） | constrained-decision → constrained-decision | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-009 | 2027-01-20 | retain | Raft 论文（2014） | Raft 论文（2014） | prediction-counterfactual → prediction-counterfactual | 已逐条复审原核源的初始事实、证据、结局与未知：保留Raft 论文（2014）的单一范围；不要求需在 Phase4 对照原图逐项转录日志状态。 |
| PRO-006 | 2027-01-21 | retain | Nintendo Switch 混合主机（2017） | Nintendo Switch 混合主机（2017） | hypothesis-diagnosis → hypothesis-diagnosis | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-010 | 2027-01-22 | retain | Go Modules 引入（2018） | Go Modules 引入（2018） | causal-modeling → causal-modeling | 已逐条复审原核源的初始事实、证据、结局与未知：保留Go Modules 引入（2018）的单一范围；不要求训练需使用原图依赖而非臆造历史依赖。 |
| INV-004 | 2027-01-23 | reframe | Shopify 2010 Series A | Shopify 2010投资备忘录：SMB自助模式的扩展边界 | evidence-selection → evidence-selection | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-004 | 2027-01-24 | reframe | 从一个垂直行业切入的 SaaS | 从一个垂直行业切入的 SaaS | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-011 | 2027-01-25 | reframe | Cloudflare 2023—2024 年数据中心双重供电事故 | Cloudflare PDX01 双路供电失效（2024-03-26） | constrained-decision → constrained-decision | 只保留已核实2024独立事件；2023只作当时已知改进背景，与ENG040分开，不把4月发布日写成事故日。 |
| PRO-007 | 2027-01-26 | reframe | Airbnb 房源与旅客匹配（2008—2011） | Airbnb 2022 Split Stays：长住供给增加与可完成预订 | quantitative-calibration → evidence-selection | 原 2008–2011 供需数不足；正式采用证据选择备用动作，改为有发布快照的 2022 Split Stays。 |
| ENG-012 | 2027-01-27 | reframe | Google Protocol Buffers 兼容策略（2008—） | Protocol Buffers proto2 字段号复用边界（2026固定规范） | prediction-counterfactual → prediction-counterfactual | 现行proto2说明已核实但不能追溯为2008；正式固定2026-10-19文档commit d056cc7的真实SearchRequest/删除字段工件。 |
| PRO-008 | 2027-01-28 | reframe | Slack 早期企业内部扩散（2013—2015） | Slack 2019披露的自助采用转组织销售 | evidence-selection → evidence-selection | 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。 |
| ENG-013 | 2027-01-29 | retain | JVM Double-Checked Locking 语义修订（2004） | JVM Double-Checked Locking 语义修订（2004） | hypothesis-diagnosis → hypothesis-diagnosis | 已逐条复审原核源的初始事实、证据、结局与未知：保留JVM Double-Checked Locking 语义修订（2004）的单一范围；不要求FAQ后修订删除过性能评价；不采用被划掉的性能结论。 |
| INV-005 | 2027-01-30 | reframe | Yelp 2005 Series B | Yelp 2005首次风险融资备忘录：评论供给与发现路径 | boundary-transfer → boundary-transfer | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-005 | 2027-01-31 | reframe | 团队日历的真正协作价值 | 团队日历的真正协作价值 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-014 | 2027-02-01 | reframe | RocksDB Universal Compaction（2013—） | RocksDB Universal Compaction 2023 设计说明 | constrained-decision → constrained-decision | 官方wiki明确2023-06-29修订；固定该说明的sorted runs与空间契约，修正原候选2013未证实首次实现。 |
| PRO-009 | 2027-02-02 | retain | Netflix DVD 邮寄方案（1997—1999） | Netflix 1998-04-14 DVD 邮寄租赁上线 | causal-modeling → causal-modeling | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-015 | 2027-02-03 | reframe | Cloudflare OAuth token 泄露与缓解（2023） | Cloudflare 支持工单会话令牌事件（2023-10-18） | evidence-selection → evidence-selection | 将OAuth候选纠正为原文session/authentication token；不借用11月后续入侵事件。 |
| PRO-010 | 2027-02-04 | reframe | Duolingo 连续学习 Streak 早期设计（2010s） | Duolingo 约2019取消streak与每日目标绑定的A/B试验 | hypothesis-diagnosis → hypothesis-diagnosis | 将未定位的2010s改动重锚为官方明确描述的单次A/B试验；真实结果同时提供收益与代价。 |
| ENG-016 | 2027-02-05 | reframe | Uber H3 地理索引（2018） | Uber H3 地理索引（2018） | constrained-decision → constrained-decision | 保留2018当事人设计材料；撤去原问题未提供的允许误差阈值，单问公开的聚合边界。 |
| INV-006 | 2027-02-06 | reframe | Tesla 2008 融资危机 | Tesla 2010披露：2008借款与后续转换条件 | constrained-decision → prediction-counterfactual | 采用已读S-1披露的借款身份；不要求未公开2008现金跑道。 |
| DES-006 | 2027-02-07 | reframe | 遥测 SDK 的默认安全性 | 遥测 SDK 的默认安全性 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-017 | 2027-02-08 | reframe | Redis Cluster 槽位迁移（2015） | Redis Cluster 3.0.0 ASK 与 MOVED（2015） | prediction-counterfactual → prediction-counterfactual | 补读Redis3.0.0 cluster.c与networking.c，原2015候选现已固定到具体源码。 |
| PRO-011 | 2027-02-09 | reframe | Figma 免费协作者与编辑席位（2016—2022） | Figma 2025 席位审批：把意外升级的控制点提前 | causal-modeling → causal-modeling | 旧范围过宽且缺历史套餐版本；冻结2024-12-10公告中的审批与单人席位机制，不依赖后来补入的临时权限细节。 |
| ENG-018 | 2027-02-10 | retain | CircleCI Dynamic Config（2021） | CircleCI Dynamic Config（2021） | constrained-decision → constrained-decision | 已逐条复审原核源的初始事实、证据、结局与未知：保留CircleCI Dynamic Config（2021）的单一范围；不要求不借用2023默认启用规则作为2021事实。 |
| PRO-012 | 2027-02-11 | retain | GitHub Pull Request Review（2016） | GitHub 2016-09-14 Pull Request Reviews 发布 | prediction-counterfactual → prediction-counterfactual | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-019 | 2027-02-12 | retain | Cloudflare 2025 年 8 月 AWS 互联拥塞 | Cloudflare 2025 年 8 月 AWS 互联拥塞 | hypothesis-diagnosis → hypothesis-diagnosis | 已逐条复审原核源的初始事实、证据、结局与未知：保留Cloudflare 2025 年 8 月 AWS 互联拥塞的单一范围；不要求无逐包数据；容量图为近似估计，不当作精确链路测量。 |
| INV-007 | 2027-02-13 | reframe | Theranos 2004—2015 融资 | Theranos 2013：渠道背书与技术验证 | evidence-selection → evidence-selection | 用2013同期合作公告建立事前信息；2018 SEC指控只作事后材料。 |
| DES-007 | 2027-02-14 | reframe | 开发者 API 的计费单位 | 开发者 API 的计费单位 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-020 | 2027-02-15 | reframe | Android Jetpack Compose（2021） | Compose UI 1.4.3 TextField 同步状态反馈工件 | causal-modeling → causal-modeling | 原2021锚点未锁定，正式改为Android Developers作者明确标明Compose UI1.4.3的真实故障演示工件，替代泛泛单向流讲解。 |
| PRO-013 | 2027-02-16 | replace | Airbnb 早期 Craigslist 分发（2009—2010） | Airbnb 2014跨端推荐计划重建 | constrained-decision → constrained-decision | 正式放弃未核Craigslist hack，保留Airbnb但换为有当事人完整测量记录的独立推荐节点；区别Dropbox空间激励在于跨端路径与旅行完成口径。 |
| ENG-021 | 2027-02-17 | reframe | Python GIL 争论与 PEP 703（2023） | PEP 703 有条件接受与渐进发布（2023-10-24） | constrained-decision → boundary-transfer | 不使用现行PEP回填2023，改锚2023-10-24 Steering Council同期明确声明的采用边界。 |
| PRO-014 | 2027-02-18 | reframe | Nintendo Wii 体感大众化战略（2006） | Nintendo Wii 2006：用直觉操作扩大游戏人口 | constrained-decision → constrained-decision | 用2006年报的事前目标与2007财报的真实推出结果替代不可访问的Iwata Asks访谈。 |
| ENG-022 | 2027-02-19 | reframe | Google LSM-tree LevelDB（2011） | LevelDB 1.22 的 L0 积压与压缩工件 | prediction-counterfactual → prediction-counterfactual | 已CLI读取官方1.22固定tag impl.md，正式冻结此实现而非main/模糊2011版本。 |
| INV-008 | 2027-02-20 | reframe | Coinbase 2021 直接上市 | Coinbase 2021披露：周期盈利与固定费用风险 | hypothesis-diagnosis → hypothesis-diagnosis | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-008 | 2027-02-21 | reframe | 至少一次任务执行的对外契约 | 至少一次任务执行的对外契约 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-023 | 2027-02-22 | retain | GitHub Actions pwn requests 风险（2020—） | GitHub Actions pwn requests 风险（2020—） | causal-modeling → causal-modeling | 已逐条复审原核源的初始事实、证据、结局与未知：保留GitHub Actions pwn requests 风险（2020—）的单一范围；不要求生产仓库名称与实际被窃信息未给出；不补造。 |
| PRO-015 | 2027-02-23 | reframe | Etsy 手作卖家社区（2005—） | Etsy 2015招股书版定制商品对话闭环 | causal-modeling → causal-modeling | 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。 |
| ENG-024 | 2027-02-24 | retain | Amazon Aurora 共享存储（2017） | Amazon Aurora 共享存储（2017） | causal-modeling → causal-modeling | 已逐条复审原核源的初始事实、证据、结局与未知：保留Amazon Aurora 共享存储（2017）的单一范围；不要求具体生产故障日志未公开，不编造恢复时长。 |
| PRO-016 | 2027-02-25 | retain | MongoDB Atlas 自服务云产品（2016） | MongoDB Atlas 2016-06-28 上线 | prediction-counterfactual → prediction-counterfactual | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-025 | 2027-02-26 | reframe | Nix 可重现构建（2004—） | Nix 2006 论文中的时间戳纯度边界 | hypothesis-diagnosis → hypothesis-diagnosis | 原要求真实derivation与故障快照未齐；改为作者论文明确给出的linker/ar时间戳反例与模型边界工件。 |
| INV-009 | 2027-02-27 | reframe | Lyft 2017—2019 IPO 前融资 | Lyft 2019招股披露：贡献率与经营盈利 | quantitative-calibration → quantitative-calibration | 正式收窄为已披露贡献率，不要求城市补贴或同cohort成本。 |
| DES-009 | 2027-02-28 | reframe | 开源开发工具如何进入企业 | 开源开发工具如何进入企业 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-026 | 2027-03-01 | retain | Cloudflare 2023 年 10 月 Workers KV 部署问题 | Cloudflare 2023 年 10 月 Workers KV 部署问题 | hypothesis-diagnosis → hypothesis-diagnosis | 已逐条复审原核源的初始事实、证据、结局与未知：保留Cloudflare 2023 年 10 月 Workers KV 部署问题的单一范围；不要求不提供未公开逐请求日志。 |
| PRO-017 | 2027-03-02 | retain | Slack 从游戏内聊天转型（2012—2013） | Slack 2013 预览前邀请外部团队试用 | boundary-transfer → boundary-transfer | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-027 | 2027-03-03 | retain | SQLite WAL 模式引入（2010） | SQLite WAL 模式引入（2010） | constrained-decision → constrained-decision | 已逐条复审原核源的初始事实、证据、结局与未知：保留SQLite WAL 模式引入（2010）的单一范围；不要求不得将2026发现的WAL-reset bug当2010事前信息。 |
| PRO-018 | 2027-03-04 | retain | Snapchat 阅后即焚机制（2011—2012） | Snapchat 2011—2012 短暂照片消息 | prediction-counterfactual → prediction-counterfactual | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-028 | 2027-03-05 | reframe | Google Dapper 采样追踪（2010） | Dapper 采样开销测量的误差边界（2010） | quantitative-calibration → quantitative-calibration | 保留数量训练，正式改为原论文可追溯的同口径采样开销与误差比较；不用缺失故障频率。 |
| INV-010 | 2027-03-06 | reframe | Figma 2015—2016 融资 | Figma 2015 Preview：产品交付与融资叙事 | evidence-selection → evidence-selection | 改正2016轮次标签，采用2015同期Preview；不把累计1800万当单轮融资或把未来功能算成交付。 |
| DES-010 | 2027-03-07 | reframe | 一个不依赖每日打卡的留存机制 | 一个不依赖每日打卡的留存机制 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-029 | 2027-03-08 | retain | Rust Ownership 与 Borrow Checker（2015） | Rust Ownership 与 Borrow Checker（2015） | boundary-transfer → boundary-transfer | 已逐条复审原核源的初始事实、证据、结局与未知：保留Rust Ownership 与 Borrow Checker（2015）的单一范围；不要求Phase4需逐字对照原文代码而非改成现代语法后假称2015。 |
| PRO-019 | 2027-03-09 | reframe | AWS Lambda 按调用与执行时间计费（2014） | AWS Lambda 2020：100ms到1ms计费粒度的有限计算 | quantitative-calibration → quantitative-calibration | 原2014preview缺可核实际负载；保留数量动作，明确改成2020-12-01官方计费变更及实测REPORT。 |
| ENG-030 | 2027-03-10 | reframe | Snowflake 分离存储和计算（2016） | Snowflake 共享数据与虚拟仓库隔离（SIGMOD 2016） | causal-modeling → boundary-transfer | 已通过官方2019目录中托管的2016原论文取得正文，消除原访问阻塞；训练只用2016模型。 |
| PRO-020 | 2027-03-11 | reframe | Slack 可搜索团队消息历史（2013—） | Slack 2019版消息搜索与历史额度 | causal-modeling → causal-modeling | 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。 |
| ENG-031 | 2027-03-12 | retain | MongoDB 副本集选主（2016—2020） | MongoDB 副本集选主（2016—2020） | prediction-counterfactual → prediction-counterfactual | 已逐条复审原核源的初始事实、证据、结局与未知：保留MongoDB 副本集选主（2016—2020）的单一范围；不要求具体历史生产副本时序没有；如编排状态推演需明确为规范条件而非事故日志。 |
| INV-011 | 2027-03-13 | reframe | SpaceX 2002—2008 早期资本 | SpaceX 2009采购披露：合同额与技术里程碑 | constrained-decision → constrained-decision | 用FAA真实合同与测试披露替代未公开的2008剩余现金决策。 |
| DES-011 | 2027-03-14 | reframe | Coding Agent 的最小权限模型 | Coding Agent 的最小权限模型 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-032 | 2027-03-15 | reframe | Guix 构建隔离（2013） | Guix 2013 论文引导链依赖检查 | evidence-selection → evidence-selection | 原Guix网页不可达；已读作者2013原论文第4节与Figure10，改用有版本边界的引导工件与真实依赖检查结果。 |
| PRO-021 | 2027-03-16 | retain | PayPal eBay 买卖双方扩散（1999—2002） | PayPal 2001 在线拍卖支付扩散 | causal-modeling → causal-modeling | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-033 | 2027-03-17 | retain | AWS S3 2017 年 us-east-1 中断 | AWS S3 2017 年 us-east-1 中断 | causal-modeling → causal-modeling | 已逐条复审原核源的初始事实、证据、结局与未知：保留AWS S3 2017 年 us-east-1 中断的单一范围；不要求实际命令文本与服务器数量未公开，禁止编造。 |
| PRO-022 | 2027-03-18 | reframe | Basecamp Hey 邮件产品发布（2020） | HEY 2020：跨平台订阅与App Store首用冲突 | constrained-decision → constrained-decision | 原邮箱定位材料缺冻结历史版本；同一HEY发布事件改为2020-06-19及22日有具体公开工件的渠道/首用决策，保持约束决策动作。 |
| ENG-034 | 2027-03-19 | reframe | Meltdown（2018） | 2018 Meltdown/Spectre 补丁的 NWChem 实测开销 | constrained-decision → quantitative-calibration | 补得SUNY Buffalo研究者2018同期一手实验，正式改成特定工作负载和版本的数量校准；修正原只称Meltdown但补丁同时覆盖Spectre。 |
| INV-012 | 2027-03-20 | reframe | SendGrid 2011 Series B | SendGrid 2011投资备忘录：体验与投递能力的壁垒 | boundary-transfer → boundary-transfer | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-012 | 2027-03-21 | reframe | 增量 CI 的依赖判断 | 增量 CI 的依赖判断 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-035 | 2027-03-22 | retain | GraphQL 在 Facebook 的起源（2012—2015） | GraphQL 在 Facebook 的起源（2012—2015） | boundary-transfer → boundary-transfer | 已逐条复审原核源的初始事实、证据、结局与未知：保留GraphQL 在 Facebook 的起源（2012—2015）的单一范围；不要求精确请求计数需要具体资源图，勿借ENG056的GitHub例子。 |
| PRO-023 | 2027-03-23 | reframe | OpenTable 餐厅端库存系统（1998—2000） | OpenTable 2009 ERB与实时席位确认 | causal-modeling → causal-modeling | 正式收窄/重锚为直接材料可支持的单一任务；保留未知，不要求未公开因果或数字。 |
| ENG-036 | 2027-03-24 | reframe | Linux CFS 调度器（2007） | Linux 2.6.23 CFS 公平账户与红黑树（2007） | causal-modeling → causal-modeling | 本轮发现v2.6.23归档文档及源码使用wait_runtime/fair_key；修正前轮将现行vruntime说明等同2007该实现的错误。 |
| PRO-024 | 2027-03-25 | retain | Sentry Developer Monitoring 商业化（2015—2021） | Sentry 2017-12-05 Enterprise SAML SSO | evidence-selection → evidence-selection | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-037 | 2027-03-26 | reframe | Redis Sentinel 自动故障转移（2013） | Redis 3.0 异步复制与 Sentinel 确认边界（2015） | prediction-counterfactual → prediction-counterfactual | 补读Redis3.0.0 redis.conf和sentinel.conf，冻结异步复制及failover重配契约，替代未锁定2013现行文档。 |
| INV-013 | 2027-03-27 | reframe | Airbnb 2009 Seed 生存融资 | Airbnb 2009年初：经营试验与生存目标 | constrained-decision → constrained-decision | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-013 | 2027-03-28 | reframe | 双边服务市场的冷启动 | 双边服务市场的冷启动 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-038 | 2027-03-29 | retain | Go 1.21 Toolchain 管理（2023） | Go 1.21 Toolchain 管理（2023） | constrained-decision → constrained-decision | 已逐条复审原核源的初始事实、证据、结局与未知：保留Go 1.21 Toolchain 管理（2023）的单一范围；不要求不把推荐策略当唯一答案；离线约束需明确为练习条件。 |
| PRO-025 | 2027-03-30 | reframe | YouTube 从视频约会设想转型（2005） | YouTube 2005：零上传之后放宽内容范围能检验什么 | hypothesis-diagnosis → hypothesis-diagnosis | 以创始人有明确归属的事后口述重建2005年决策，不宣称找到了同期日志；修正“已有大量非约会上传”的错误触发。 |
| ENG-039 | 2027-03-31 | reframe | Cloudflare Pingora 替换 NGINX（2022—2024） | Pingora 同负载迁移与连接复用比例（2022） | quantitative-calibration → quantitative-calibration | 正式缩小数量主线到来源中同客户复用率的可计算比例；保留数量训练，撤掉独立CPU/内存归因要求。 |
| PRO-026 | 2027-04-01 | retain | Apple iPhone 首代触控键盘（2007） | 首代 iPhone 2007 软键盘公布 | constrained-decision → constrained-decision | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-040 | 2027-04-02 | retain | Cloudflare 2023 年 11 月控制面中断 | Cloudflare 2023 年 11 月控制面中断 | boundary-transfer → boundary-transfer | 已逐条复审原核源的初始事实、证据、结局与未知：保留Cloudflare 2023 年 11 月控制面中断的单一范围；不要求不把2024改善成效提前置入2023开场。 |
| INV-014 | 2027-04-03 | reframe | Box 2014 延期 IPO 与融资 | Box 2014融资：董事席位与未披露权利 | prediction-counterfactual → evidence-selection | 采用证据选择备用题，取消没有合同支持的旧股稀释预测。 |
| DES-014 | 2027-04-04 | reframe | 在线数据库 Schema 演进 | 在线数据库 Schema 演进 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-041 | 2027-04-05 | retain | Google Bigtable（2006） | Google Bigtable（2006） | causal-modeling → causal-modeling | 已逐条复审原核源的初始事实、证据、结局与未知：保留Google Bigtable（2006）的单一范围；不要求不编造真实热键指标。 |
| PRO-027 | 2027-04-06 | retain | GitHub Private Repositories 免费开放（2019） | GitHub 2019-01-07 免费私有仓库 | prediction-counterfactual → prediction-counterfactual | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-042 | 2027-04-07 | reframe | Kubernetes CRD 与 Aggregated API（2016—2018） | Kubernetes 1.18 CRD 与聚合 API 存储边界（2020） | constrained-decision → constrained-decision | 已下载官方release-1.18分支正文，改锚2020的明确版本，替代未锁定2016—2018泛称。 |
| PRO-028 | 2027-04-08 | retain | Figma 评论与设计协作（2017—） | Figma 2021-11-16 评论重做 | causal-modeling → causal-modeling | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-043 | 2027-04-09 | reframe | Spectre（2018） | Spectre variant 1 边界检查与可观察状态（2018） | boundary-transfer → boundary-transfer | 固定原论文明确variant1原始示例，消除前轮泛称架构访问拒绝易与Meltdown混淆的问题。 |
| INV-015 | 2027-04-10 | reframe | Uber 2015—2019 私募融资 | Uber 2019Q4：Gross Bookings、收入与ANR | quantitative-calibration → quantitative-calibration | 改用2020披露的2019Q4实际数值，不再要求IPO前城市密度或补贴数据。 |
| DES-015 | 2027-04-11 | reframe | 记账产品的第一份有效反馈 | 记账产品的第一份有效反馈 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-044 | 2027-04-12 | retain | Facebook TAO（2013） | Facebook TAO（2013） | prediction-counterfactual → prediction-counterfactual | 已逐条复审原核源的初始事实、证据、结局与未知：保留Facebook TAO（2013）的单一范围；不要求不虚构复制延迟或一致性SLA。 |
| PRO-029 | 2027-04-13 | retain | LinkedIn 邀请联系人网络（2003—） | LinkedIn 2003-05 初始邀请及转介绍网络 | prediction-counterfactual → prediction-counterfactual | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-045 | 2027-04-14 | reframe | Rust Cargo Features 设计（2013—） | Cargo 0.53.0 resolver 2 特性合并工件（2021） | prediction-counterfactual → prediction-counterfactual | 已CLI实际读取Cargo0.53.0固定tag，采用文中真实foo/bar/winapi例子，消除原现行规范历史范围歧义。 |
| PRO-030 | 2027-04-15 | reframe | Microsoft Windows Phone 停止投入（2017） | Windows 10 Mobile 2018公告：停止支持的用户迁移取舍 | constrained-decision → constrained-decision | 原2017退出范围缺内部决策材料；改为2018-12-21可核支持终止公告，事件年份显式变更。 |
| ENG-046 | 2027-04-16 | reframe | .NET ThreadPool Hill Climbing（2000s—） | .NET 6 Hill Climbing 吞吐反馈工件（2021） | evidence-selection → evidence-selection | 固定官方v6.0.0源码而非main；改为该控制器真实使用的反馈选择题，无须未知实际故障曲线。 |
| INV-016 | 2027-04-17 | reframe | Pinterest 2011 Series A | Pinterest 2011已签term sheet：兴趣与商业意向 | evidence-selection → evidence-selection | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-016 | 2027-04-18 | reframe | 早期基金的后续投资储备 | 跟投与桥接的资本优先级 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-047 | 2027-04-19 | retain | Fastly 2021 年 6 月大面积故障 | Fastly 2021 年 6 月大面积故障 | boundary-transfer → boundary-transfer | 已逐条复审原核源的初始事实、证据、结局与未知：保留Fastly 2021 年 6 月大面积故障的单一范围；不要求触发配置具体内容与软件bug代码未公开。 |
| PRO-031 | 2027-04-20 | reframe | Tinder Swipe 匹配（2012） | Tinder 2017：双向同意不等于有效对话 | quantitative-calibration → evidence-selection | 执行预设证据选择fallback；改为2017工程负责人可核机制快照，删除缺数据的2012数量推算。 |
| ENG-048 | 2027-04-21 | reframe | SQLite Query Planner（2010s） | SQLite NGQP 导致 Fossil 查询回归（2013） | hypothesis-diagnosis → hypothesis-diagnosis | 找到官方NGQP文档第5.1—5.2真实Fossil回归，替换无实际快照的普通教程；有SQL、索引、选择率与修复对照。 |
| PRO-032 | 2027-04-22 | retain | Dropbox 早期 Demo 视频（2007） | Dropbox 2007-04-04 HN 公开 demo | evidence-selection → evidence-selection | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-049 | 2027-04-23 | reframe | Kubernetes API 对象与控制器分离（2014—） | Kubernetes 1.18 Job 控制器与执行职责（2020） | causal-modeling → causal-modeling | 补读官方release-1.18控制器文档的真实Job示例，固定对象与版本，替代2014泛称。 |
| INV-017 | 2027-04-24 | reframe | Twilio 2009 Seed | Twilio 2009：小额种子延长与等待验证 | boundary-transfer → boundary-transfer | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-017 | 2027-04-25 | reframe | 跨部门 B2B 产品的引导路径 | 跨部门 B2B 产品的引导路径 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-050 | 2027-04-26 | reframe | LinkedIn Kafka 日志存储（2011） | Kafka 2011 批量发布实验 | quantitative-calibration → quantitative-calibration | 正式改为原论文可追溯批量/吞吐的更小数量题，保留数量动作，不再精算未公开等待分布。 |
| PRO-033 | 2027-04-27 | reframe | Snowflake Consumption Model（2014—2019） | Snowflake 2023成本界面：总消费增长的诊断分叉 | hypothesis-diagnosis → hypothesis-diagnosis | 原2014–2019客户预算事件没有独立材料；明确改为2023-11-02私测产品工件，训练成本告警可否支持因果诊断，删除不存在的历史cohort要求。 |
| ENG-051 | 2027-04-28 | retain | Log4Shell（2021） | Log4Shell（2021） | causal-modeling → causal-modeling | 已逐条复审原核源的初始事实、证据、结局与未知：保留Log4Shell（2021）的单一范围；不要求具体应用配置与JDK条件需在Brief固定，不能泛称所有Java日志皆可RCE。 |
| PRO-034 | 2027-04-29 | reframe | Spotify 早期即时播放体验（2008） | Spotify 2010：快速起播不能只归因P2P | causal-modeling → causal-modeling | 原2008首用判断缺同期机制细节；冻结2010作者论文中明确测量口径和缓存/预取/服务器/P2P路径。 |
| ENG-052 | 2027-04-30 | retain | Amazon Dynamo（2007） | Amazon Dynamo（2007） | prediction-counterfactual → prediction-counterfactual | 已逐条复审原核源的初始事实、证据、结局与未知：保留Amazon Dynamo（2007）的单一范围；不要求需指定可达节点与时序，否则请求失败还是多版本无法唯一确定。 |
| INV-018 | 2027-05-01 | reframe | Toast 2015 Series B | Toast 2015投资备忘录：POS和支付绑定边界 | boundary-transfer → boundary-transfer | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-018 | 2027-05-02 | reframe | 渐进发布与紧急停止 | 渐进发布与紧急停止 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-053 | 2027-05-03 | reframe | Nx Affected Builds（2020—） | Nx 2020 Affected 与真实部署基线工件 | boundary-transfer → constrained-decision | 找到Nx团队成员Rareș Matei同期亲写官方合作教程，明确项目依赖图、改动和输出；不再依赖现行v24行为。 |
| PRO-035 | 2027-05-04 | reframe | Dropbox Freemium 存储配额（2008—） | Dropbox Pro 2014：容量与共享控制的付费触发 | prediction-counterfactual → prediction-counterfactual | 2008免费额度与升级队列不足；改为2014-08-27具体Pro发布政策，对同一付费触发问题做有限反事实。 |
| ENG-054 | 2027-05-05 | replace | Google 2012 年闰秒 Linux 故障 | Cloudflare 2017 闰秒导致DNS负时长故障 | causal-modeling → causal-modeling | 原Google2012事故身份无法核实，正式替换为当事人2017-01-01独立事故；全年未发现另一闰秒槽位，ID与日期保留。 |
| PRO-036 | 2027-05-06 | retain | Spotify Discover Weekly（2015） | Discover Weekly 2015-07 推出 | hypothesis-diagnosis → hypothesis-diagnosis | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-055 | 2027-05-07 | retain | Go 1.14 异步抢占（2020） | Go 1.14 异步抢占（2020） | prediction-counterfactual → prediction-counterfactual | 已逐条复审原核源的初始事实、证据、结局与未知：保留Go 1.14 异步抢占（2020）的单一范围；不要求原文无具体循环片段，应在Brief明确最小示例为规范推演。 |
| INV-019 | 2027-05-08 | reframe | Stripe 2010—2011 Seed | Stripe早期人工安装：2013当事人回顾 | evidence-selection → evidence-selection | 以Paul Graham当事人回顾为节点，不虚构2011种子轮条款或客户数据。 |
| DES-019 | 2027-05-09 | reframe | 有用而克制的通知系统 | 有用而克制的通知系统 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-056 | 2027-05-10 | reframe | GitHub REST 到 GraphQL API v4（2016） | GitHub API v4 发布工件的请求责任边界（2016） | quantitative-calibration → boundary-transfer | 正式采用预列boundary-transfer备用问题；发布原文的完整GraphQL查询和一次返回足以支撑责任边界，不依赖缺失REST对应端点。 |
| PRO-037 | 2027-05-11 | reframe | Hotmail 邮件签名增长（1996—1997） | Hotmail 1996邮件页脚传播：机会分母如何去重 | quantitative-calibration → evidence-selection | 采用预设证据选择fallback。来源为投资董事Jurvetson事后重刊的1997/1998版本叙述，不能混作1996同期观测；只保留明示机制与作者观察。 |
| ENG-057 | 2027-05-12 | reframe | Amazon Redshift 列式分析（2012） | Amazon Redshift 2015 列块跳过与分布工件 | causal-modeling → causal-modeling | 补得SIGMOD2015 AWS作者原论文，明确晚于2012 preview；用同一设计快照替代现行文档追溯早期实现。 |
| PRO-038 | 2027-05-13 | retain | Instagram 从 Burbn 缩减功能（2010） | Instagram 从 Burbn 缩减功能（2010） | hypothesis-diagnosis → hypothesis-diagnosis | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-058 | 2027-05-14 | reframe | Kafka 复制协议（2012—2013） | Kafka 0.8.0 ISR 缩减与 ACK 边界（2013） | prediction-counterfactual → prediction-counterfactual | 已读0.8.0固定tag Partition.scala正文；收窄到可核ISR缩减/ACK条件，避免缺少选举全契约时做无限故障保证。 |
| INV-020 | 2027-05-15 | reframe | Nubank 2021 IPO 估值 | Nubank 2021定价：普通股与BDR换算 | quantitative-calibration → quantitative-calibration | 保留数量训练，改为发行方给出的BDR比率和币种，取消未核股本估值与客户风险成本。 |
| DES-020 | 2027-05-16 | reframe | 高基数追踪数据怎样付得起 | 稀有错误追踪的保留取舍 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-059 | 2027-05-17 | reframe | Bazel Remote Execution API（2018—） | Remote Execution API v2.0.0 Action 缓存键工件 | evidence-selection → evidence-selection | 固定原有已核proto tag v2.0.0；不将copyright2018推作tag发布日期。 |
| PRO-039 | 2027-05-18 | retain | Microsoft Teams 与 Slack 竞争（2017—2020） | Teams 2017-03-14 面向 Office365 商业客户 GA | boundary-transfer → boundary-transfer | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-060 | 2027-05-19 | retain | Heartbleed OpenSSL（2014） | Heartbleed OpenSSL（2014） | prediction-counterfactual → prediction-counterfactual | 已逐条复审原核源的初始事实、证据、结局与未知：保留Heartbleed OpenSSL（2014）的单一范围；不要求最小代码片段与具体报文长度还需对照补丁，公告不提供完整测试覆盖历史。 |
| PRO-040 | 2027-05-20 | reframe | DoorDash 郊区餐饮配送起点（2013） | DoorDash 2013：创始人配送阶段是否扩大覆盖 | quantitative-calibration → constrained-decision | 执行预设constrained-decision fallback；用CEO公开回顾里的真实早期运作约束替代缺失数量输入。 |
| ENG-061 | 2027-05-21 | retain | Cloudflare 2024 年 6 月 DDoS 规则事故 | Cloudflare 2024 年 6 月 DDoS 规则事故 | hypothesis-diagnosis → hypothesis-diagnosis | 已逐条复审原核源的初始事实、证据、结局与未知：保留Cloudflare 2024 年 6 月 DDoS 规则事故的单一范围；不要求所有错误率有各自分母，不能把回源5xx与本服务不可用混用。 |
| INV-021 | 2027-05-22 | reframe | Spotify 2016—2018 上市前投资 | Spotify 2018披露：平均毛利与新增订户 | quantitative-calibration → quantitative-calibration | 正式收窄为分部历史平均毛利，保留实数而不假设保密版税合同。 |
| DES-021 | 2027-05-23 | reframe | 缺少渠道优势时怎样验证付费 | 缺少渠道优势时怎样验证付费 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-062 | 2027-05-24 | reframe | Netflix 自适应码率播放（2010s） | Netflix BBA-0 码率与缓冲取舍（2013实验/2014论文） | constrained-decision → constrained-decision | Netflix博客不可达，补得Stanford与Netflix作者SIGCOMM2014原论文；冻结BBA-0、2013实验范围。 |
| PRO-041 | 2027-05-25 | reframe | Grammarly 浏览器实时纠错（2015—） | Grammarly 2019：词上即时同义词与首次价值路径 | causal-modeling → causal-modeling | 原2015扩展首次价值证据不足；改用2019-11-28官方明确发布的手机键盘交互快照，保留首次价值因果动作。 |
| ENG-063 | 2027-05-26 | reframe | Rust async/await 稳定（2019） | Rust 1.39 async Future 的取消与析构边界（2019） | prediction-counterfactual → prediction-counterfactual | 补读RFC2394的取消=drop模型与1.39官方析构规则；保留原取消/资源边界，排除RFC中尚未稳定的async closure和await宏语法。 |
| PRO-042 | 2027-05-27 | retain | Unity Runtime Fee 争议与撤回（2023—2024） | Unity Runtime Fee 2023修订至2024撤销 | evidence-selection → evidence-selection | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-064 | 2027-05-28 | reframe | Docker Image OCI 标准化（2015—2017） | OCI Image Specification v1.0.0 的运行边界（2017） | boundary-transfer → boundary-transfer | 已实际读v1.0.0固定tag spec.md与config.md，消除原规范正文缺口。 |
| INV-022 | 2027-05-29 | reframe | LinkedIn 2006 Series C | LinkedIn 2006投资备忘录：注册网络与企业购买 | evidence-selection → evidence-selection | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-022 | 2027-05-30 | reframe | 评价体系如何建立可信的 Marketplace | 评价体系如何建立可信的 Marketplace | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-065 | 2027-05-31 | retain | Google Megastore（2011） | Google Megastore（2011） | constrained-decision → constrained-decision | 已逐条复审原核源的初始事实、证据、结局与未知：保留Google Megastore（2011）的单一范围；不要求不将每组少量写入经验阈值外推所有现代数据库。 |
| PRO-043 | 2027-06-01 | reframe | Atlassian Jira 自助购买（2000s） | Atlassian 2015：自助销售把评估责任移到哪里 | boundary-transfer → boundary-transfer | 原2000年代时间范围过宽；实际下载并提取2015-11-09 F-1，冻结当时自助评估与支持边界。 |
| ENG-066 | 2027-06-02 | retain | VS Code Remote Development（2019） | VS Code Remote Development（2019） | boundary-transfer → boundary-transfer | 已逐条复审原核源的初始事实、证据、结局与未知：保留VS Code Remote Development（2019）的单一范围；不要求个别扩展可能不兼容，不能声称全部无需改动。 |
| PRO-044 | 2027-06-03 | reframe | Duolingo Leagues（2018） | Duolingo 排行榜规则快照：名次下降能诊断学习退步吗 | hypothesis-diagnosis → hypothesis-diagnosis | 2018仅能核实测试年份，缺同期队列；正式改为2026-10-25可读公开规则快照，保留假设诊断并移除虚构实验。 |
| ENG-067 | 2027-06-04 | retain | PostgreSQL MVCC VACUUM（2000s—） | PostgreSQL MVCC VACUUM（2000s—） | causal-modeling → causal-modeling | 已逐条复审原核源的初始事实、证据、结局与未知：保留PostgreSQL MVCC VACUUM（2000s—）的单一范围；不要求没有实际事务ID/日志；Phase4需将规范状态时序明确标为推演。 |
| INV-023 | 2027-06-05 | reframe | WeWork 2019 撤回 IPO 与救助 | WeWork 2019救助公告：公司现金与老股流动性 | constrained-decision → constrained-decision | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-023 | 2027-06-06 | reframe | 插件 SDK 的稳定扩展点 | 插件 SDK 的稳定扩展点 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-068 | 2027-06-07 | retain | AWS us-east-1 2021 年 12 月网络事件 | AWS us-east-1 2021 年 12 月网络事件 | constrained-decision → constrained-decision | 已逐条复审原核源的初始事实、证据、结局与未知：保留AWS us-east-1 2021 年 12 月网络事件的单一范围；不要求原始内部日志、配置值未公开；不编造。 |
| PRO-045 | 2027-06-08 | reframe | Pinterest Waitlist 邀请制（2010—2011） | Pinterest 2020 Story Pins：曝光还是被尝试的想法 | evidence-selection → evidence-selection | 原2010候补名单缺可核原始材料；明确换为同品牌2020-09-23 Story Pins发布，有实际内容交互和度量入口，不与2015 Save案例混用。 |
| ENG-069 | 2027-06-09 | reframe | Capital One 云环境泄露（2019） | Capital One 2019 WAF角色凭据与对象权限边界 | causal-modeling → causal-modeling | 本轮下载并渲染阅读原complaint第5—6页，补齐WAF-Role凭据、list与sync链条；删除原候选未由该文明确给出的SSRF细节。 |
| PRO-046 | 2027-06-10 | retain | Airbnb 早期纽约房源摄影（2009） | Airbnb 2009 纽约房源摄影 | hypothesis-diagnosis → hypothesis-diagnosis | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-070 | 2027-06-11 | reframe | Go Scheduler G-M-P 模型（2012） | Go 1.1 已知阻塞系统调用与 M/P 交接（2013） | prediction-counterfactual → prediction-counterfactual | 固定原有已核go1.1 proc.c；候选2012仅是设计窗口，不再混称为该运行实现发布日。 |
| INV-024 | 2027-06-12 | reframe | Mistral AI 2023 Seed | Mistral 2023种子轮：技术经历与需求里程碑 | constrained-decision → constrained-decision | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-024 | 2027-06-13 | reframe | 开源与托管服务的商业边界 | 开源与托管服务的商业边界 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-071 | 2027-06-14 | reframe | Crossplane Compositions（2020—2023） | Crossplane Resource Composition Accepted 设计工件（v1.13.0归档） | boundary-transfer → boundary-transfer | CLI取得v1.13.0归档Accepted设计；明确题目是该设计示例契约分析，不声称历史草案原样部署。 |
| PRO-047 | 2027-06-15 | retain | Netflix 从 DVD 转向流媒体（2007） | Netflix 2007-01-16 即时观看PC功能 | constrained-decision → constrained-decision | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-072 | 2027-06-16 | reframe | LinkedIn Venice 多区域数据（2022） | Venice 2022 跨区域最终一致性工件 | prediction-counterfactual → prediction-counterfactual | 固定2022-09-26开源设计说明，不要求缺失的精确ACK时点或最大复制延迟。 |
| PRO-048 | 2027-06-17 | retain | Steam Workshop 创作者市场（2011—） | Steam Workshop 2011-10-13 TF2提交中心上线 | causal-modeling → causal-modeling | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-073 | 2027-06-18 | reframe | Meta Sapling 版本控制（2022） | Sapling 2022 专用后端的 clone 与历史下载 | boundary-transfer → boundary-transfer | 固定2022-11-15发布工件及专用后端，选择初始clone/后续历史查询的一条路径，不外推Git兼容后端。 |
| INV-025 | 2027-06-19 | reframe | Datadog 2015—2019 融资 | Datadog 2015 C轮：集成广度的可迁移边界 | boundary-transfer → boundary-transfer | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-025 | 2027-06-20 | reframe | 取消订阅也要维护长期信任 | 取消订阅也要维护长期信任 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-074 | 2027-06-21 | retain | Google Borg 集群超售（2015） | Google Borg 集群超售（2015） | constrained-decision → constrained-decision | 已逐条复审原核源的初始事实、证据、结局与未知：保留Google Borg 集群超售（2015）的单一范围；不要求不可据此虚构当前cell资源分布或保证任意超售比例。 |
| PRO-049 | 2027-06-22 | reframe | Superhuman 人工一对一 Onboarding（2017—） | Superhuman人工入门：产能ARR模型与利润的边界 | quantitative-calibration → quantitative-calibration | 保留数量动作但收窄为可核公开模型；40次×45周×月费是产能情景，不冒充历史实际净收入。 |
| ENG-075 | 2027-06-23 | reframe | PostgreSQL B-tree Deduplication（2020） | PostgreSQL 13 B-tree 去重的适用分布（2020） | quantitative-calibration → prediction-counterfactual | 正式采用预列prediction-counterfactual备用问题；固定PG13官方机制与限制，无须缺失的实际页面数量。 |
| PRO-050 | 2027-06-24 | reframe | Zoom 免费会议 40 分钟限制（2013—） | Zoom 2020教育豁免：免费时限与管理需求 | constrained-decision → constrained-decision | 改用官方2020记录明确的40分钟豁免与Education差异，取消未核2019完整套餐。 |
| ENG-076 | 2027-06-25 | retain | Atlassian 2022 年云服务恢复事故 | Atlassian 2022 年云服务恢复事故 | constrained-decision → constrained-decision | 已逐条复审原核源的初始事实、证据、结局与未知：保留Atlassian 2022 年云服务恢复事故的单一范围；不要求PIR记录部分早期恢复点不一致后补救；不能简化为所有站点初次恢复都无数据差异。 |
| INV-026 | 2027-06-26 | reframe | Roblox 2021 直接上市 | Roblox 2021披露：bookings与收入倍数 | quantitative-calibration → quantitative-calibration | 正式改为可复算的确认口径，取消未核股本与假设直接上市交易价格。 |
| DES-026 | 2027-06-27 | reframe | 可快速启动的远程开发环境 | 远程 workspace 的中断恢复边界 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-077 | 2027-06-28 | retain | Kubernetes CVE-2018-1002105 | Kubernetes CVE-2018-1002105 | hypothesis-diagnosis → hypothesis-diagnosis | 已逐条复审原核源的初始事实、证据、结局与未知：保留Kubernetes CVE-2018-1002105的单一范围；不要求不能声称已有实际利用；公告明确没有简单审计检测方法。 |
| PRO-051 | 2027-06-29 | retain | HashiCorp Terraform Enterprise（2014—2021） | Terraform Enterprise 2017-12-12 GA | evidence-selection → evidence-selection | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-078 | 2027-06-30 | retain | Go GC Concurrent Mark Sweep（2015） | Go GC Concurrent Mark Sweep（2015） | causal-modeling → causal-modeling | 已逐条复审原核源的初始事实、证据、结局与未知：保留Go GC Concurrent Mark Sweep（2015）的单一范围；不要求没有固定工作负载，不能精算吞吐损失。 |
| PRO-052 | 2027-07-01 | retain | Duolingo 免费语言学习定位（2011—2012） | Duolingo 2012-06 对外开放 | constrained-decision → constrained-decision | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-079 | 2027-07-02 | retain | Kubernetes EndpointSlice 传播（2019—2021） | Kubernetes EndpointSlice 传播（2019—2021） | prediction-counterfactual → prediction-counterfactual | 已逐条复审原核源的初始事实、证据、结局与未知：保留Kubernetes EndpointSlice 传播（2019—2021）的单一范围；不要求新请求路由与已有连接需区分；全局所有节点生效需要各节点观测，单次API ACK不足。 |
| INV-027 | 2027-07-03 | reframe | HelloFresh 2015—2017 融资 | HelloFresh 2017年报：贡献利润到EBITDA的缺口 | quantitative-calibration → quantitative-calibration | 采用已读FY2017真实报表，不再求同cohort CAC或损耗。 |
| DES-027 | 2027-07-04 | reframe | 跨区域配置变更的生效语义 | 跨区域配置变更的生效语义 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-080 | 2027-07-05 | reframe | Google Bazel 构建系统公开（2015） | Bazel 2015 Beta：已交付能力与未来缓存承诺 | causal-modeling → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-053 | 2027-07-06 | retain | WhatsApp 群聊上线（2011） | WhatsApp 2011-02-22 v2.6群聊 | causal-modeling → causal-modeling | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-081 | 2027-07-07 | retain | AWS Lambda Extensions API（2020） | AWS Lambda Extensions API（2020） | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-054 | 2027-07-08 | retain | GitHub Student Developer Pack（2014） | GitHub Student Developer Pack 2014-10-07 | evidence-selection → evidence-selection | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-082 | 2027-07-09 | retain | Cloudflare 2025 年 6 月 Workers KV 故障 | Cloudflare 2025 年 6 月 Workers KV 故障 | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-028 | 2027-07-10 | reframe | Twitch 2012 Series B | Twitch 2012投资备忘录：主播持续使用与观看规模 | evidence-selection → evidence-selection | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-028 | 2027-07-11 | reframe | 受监管行业 AI 创业的可信起点 | 行政表单草稿的人工确认边界 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-083 | 2027-07-12 | retain | Notion 数据库分片（2021） | Notion 数据库分片（2021） | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-055 | 2027-07-13 | reframe | Twitter 初期字数约束（2006） | Twitter 2017：字符上限触顶率的分母比较 | boundary-transfer → quantitative-calibration | 原2006渠道边界缺可核首版机制；改为2017-09-26明确发布的语言组统计与280字符试验，增加真实数量动作。 |
| ENG-084 | 2027-07-14 | reframe | Netflix Open Connect CDN（2012） | Open Connect 2012：接入条件与扩展边界 | quantitative-calibration → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-056 | 2027-07-15 | reframe | Slack 按活跃成员计费（2013—） | Slack 2019披露：fair billing的信用额度 | causal-modeling → causal-modeling | 收窄到S-1已披露credit机制，不要求未核活跃天数，也不混用DAU。 |
| ENG-085 | 2027-07-16 | reframe | CockroachDB 分布式事务（2016—2020） | CockroachDB v20.1：嵌套回滚与事务重试 | prediction-counterfactual → hypothesis-diagnosis | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-029 | 2027-07-17 | reframe | Coinbase 2012—2013 Seed/Series A | Coinbase 2013 A轮：融资后的运营能力验证 | constrained-decision → constrained-decision | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-029 | 2027-07-18 | reframe | 多人编辑时的冲突可见性 | 多人编辑时的冲突可见性 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-086 | 2027-07-19 | reframe | Google Piper 单体仓库（2016） | Google Piper/Rosie 跨团队变更治理（2016论文） | constrained-decision → evidence-selection | 取得带作者、DOI与逐页正文的原论文镜像，保留Google Research元数据作身份复核；只聚焦Rosie治理而非泛论单仓。 |
| PRO-057 | 2027-07-20 | retain | BlackBerry 从硬件转向软件服务（2016） | BlackBerry 2016-09-28 硬件开发外包决策 | constrained-decision → constrained-decision | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-087 | 2027-07-21 | reframe | React Server Components（2020—2023） | React RFC 0188：序列化跨组件边界 | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-058 | 2027-07-22 | reframe | Uber 城市级供需冷启动（2010—2012） | Uber 2010 Samasource活动：局部供需峰值 | quantitative-calibration → prediction-counterfactual | 正式采用预测备用题，取消没有数据的每辆车等待效应计算。 |
| ENG-088 | 2027-07-23 | reframe | Linux io_uring（2019） | io_uring 设计文档：共享队列与每次I/O开销 | constrained-decision → causal-modeling | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-030 | 2027-07-24 | reframe | Convoy 2023 关闭 | Convoy 2023关闭备忘录：资本环境与经营解释 | causal-modeling → causal-modeling | 正式改为关闭公告后的归因审查，不要求此前未公开现金周期。 |
| DES-030 | 2027-07-25 | reframe | 共享平台里的租户资源隔离 | 共享平台里的租户资源隔离 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-089 | 2027-07-26 | retain | Rowhammer（2014） | Rowhammer（2014） | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-059 | 2027-07-27 | replace | Zappos 先拍摄当地鞋店商品（1999） | Buffer 2010：落地页意向到首笔付款 | evidence-selection → evidence-selection | 真实换题：Zappos摄影售鞋原始材料未取得，采用创始人2011同期回顾的实际验证。 |
| ENG-090 | 2027-07-28 | retain | GitLab 2017 年生产数据库误删除 | GitLab 2017 年生产数据库误删除 | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-060 | 2027-07-29 | reframe | Todoist Recurring Tasks（2010s） | Todoist 2026规则快照：固定周期与完成后周期 | hypothesis-diagnosis → hypothesis-diagnosis | 用已读官方规则快照取代未核2010s留存研究；允许推演文档例子，不虚构真实用户实验。 |
| ENG-091 | 2027-07-30 | retain | Vitess 分片治理（2010—） | Vitess 分片治理（2010—） | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-031 | 2027-07-31 | reframe | Atlassian 2002—2005 自举期 | Atlassian 2010创始人演讲：OEM扩张的模式冲突 | boundary-transfer → boundary-transfer | 用演讲实际记载的OEM尝试取代无法锁定2002—2005的单次节点。 |
| DES-031 | 2027-08-01 | reframe | 探索型内容产品怎样衡量好推荐 | 探索型内容产品怎样衡量好推荐 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-092 | 2027-08-02 | retain | ZooKeeper Zab（2011） | ZooKeeper Zab（2011） | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-061 | 2027-08-03 | reframe | Robinhood Referral 免费股票（2015—） | Robinhood 2021披露：推荐奖励的触发点 | quantitative-calibration → evidence-selection | 正式采用证据题，缺少同cohort收益和奖励成本时不编造CAC回收；使用公司给SEC的真实示例。 |
| ENG-093 | 2027-08-04 | retain | GitHub Codespaces 发布（2021） | GitHub Codespaces 发布（2021） | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-062 | 2027-08-05 | reframe | Datadog 免费试用到企业监控（2010—2019） | Datadog 2019：免费用户与组织付费的证据缺口 | evidence-selection → evidence-selection | 取得实际S-1正文，保留产品证据任务，取消虚构的单客户历史交接。 |
| ENG-094 | 2027-08-06 | retain | gRPC Streaming API 设计（2015） | gRPC Streaming API 设计（2015） | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-032 | 2027-08-07 | reframe | Reddit 2024 IPO 定价 | Reddit 2024发行文件：账面稀释与价格 | quantitative-calibration → quantitative-calibration | 使用发行人公开假设计算而非自造价格；保留数量校准，不需要完整未来估值。 |
| DES-032 | 2027-08-08 | reframe | 减少内存占用而不破坏延迟 | 减少内存占用而不破坏延迟 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-095 | 2027-08-09 | retain | Java G1 GC 默认化（2017） | Java G1 GC 默认化（2017） | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-063 | 2027-08-10 | retain | Google Maps 移动端导航上线（2009） | Google Maps Navigation 2009-10-28 Android2.0 beta | causal-modeling → causal-modeling | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-096 | 2027-08-11 | reframe | Twitter 2012—2014 时间线扇出 | Twitter Timelines at Scale：写扇出与读取合并边界（2012演讲工件） | constrained-decision → constrained-decision | 取得原幻灯片可读文本；删掉未经直接核实的明星混合方案落地结论，收敛成工件快照上的单次路径取舍。 |
| PRO-064 | 2027-08-12 | reframe | Spotify 广告免费与 Premium 并存（2008—） | Spotify 2017广告层：毛利转正与免费获客 | quantitative-calibration → quantitative-calibration | 保留真实数量训练，取消单cohort完全成本/转化反事实。 |
| ENG-097 | 2027-08-13 | retain | Google 2020 年身份验证故障 | Google 2020 年身份验证故障 | hypothesis-diagnosis → hypothesis-diagnosis | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-033 | 2027-08-14 | reframe | Blue Apron 2015—2017 融资/上市 | Blue Apron 2017：回收倍数与cohort窗口 | quantitative-calibration → quantitative-calibration | 正式改为公司回收展示的算术与cohort适用性核对；保留数量训练，不计算未披露的真实cohort回本天数。 |
| DES-033 | 2027-08-15 | reframe | 小市场 2C 创业如何越过分发限制 | 小市场 2C 创业如何越过分发限制 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-098 | 2027-08-16 | retain | runC 容器逃逸 CVE-2019-5736 | runC 容器逃逸 CVE-2019-5736 | causal-modeling → causal-modeling | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-065 | 2027-08-17 | retain | Google Reader 关闭（2013） | Google Reader 关闭（2013） | constrained-decision → constrained-decision | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-099 | 2027-08-18 | reframe | FoundationDB 事务层（2013） | FoundationDB 8.0 文档：读写冲突集合 | prediction-counterfactual → evidence-selection | 明确冻结来源版本；不倒推候选初始年份。 |
| PRO-066 | 2027-08-19 | retain | Apple App Store 上线（2008） | Apple App Store 上线（2008） | constrained-decision → constrained-decision | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-100 | 2027-08-20 | retain | Microsoft TypeScript 增量构建（2018—2020） | Microsoft TypeScript 增量构建（2018—2020） | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-034 | 2027-08-21 | replace | Superhuman 2017—2019 融资 | Chegg 2023：生成式AI冲击下的增长与留存 | quantitative-calibration → hypothesis-diagnosis | 真实换题：Superhuman缺独立付费cohort且与PRO-080问卷重叠，改用Chegg已公开经营反馈。 |
| DES-034 | 2027-08-22 | reframe | 自动化产品如何保留用户控制权 | 自动化产品如何保留用户控制权 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-101 | 2027-08-23 | retain | Uber Schemaless（2016） | Uber Schemaless（2016） | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-067 | 2027-08-24 | reframe | Twitch 从 Justin.tv 拆分（2011） | Twitch 2011 beta：游戏频道迁移方案 | evidence-selection → prediction-counterfactual | 把无分类集中度数据的垂直拆分识别题改成已有明确规则的频道迁移预测。 |
| ENG-102 | 2027-08-25 | retain | Git LFS 的外置大文件模型（2015） | Git LFS 的外置大文件模型（2015） | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-068 | 2027-08-26 | retain | GitHub Dependabot 集成（2019） | GitHub Dependabot 集成（2019） | causal-modeling → causal-modeling | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-103 | 2027-08-27 | retain | Python asyncio 引入（2014） | Python asyncio 引入（2014） | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-035 | 2027-08-28 | reframe | MongoDB 2015—2017 融资 | MongoDB 2017 S-1：免费使用与可捕获商业价值 | boundary-transfer → boundary-transfer | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-035 | 2027-08-29 | reframe | Agent Eval 作为日常开发工作流 | 小型缺陷修复的 agent 回归门槛 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-104 | 2027-08-30 | retain | Cloudflare 2025 年 11 月 Bot Management 故障 | Cloudflare 2025 年 11 月 Bot Management 故障 | causal-modeling → causal-modeling | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-069 | 2027-08-31 | reframe | TikTok 收购 Musical.ly（2017—2018） | Musical.ly 2018整合：账户迁移与持续创作 | prediction-counterfactual → prediction-counterfactual | 保留预测动作，正式取消没有材料的迁移后留存结论；实际升级工件作为最终揭晓。 |
| ENG-105 | 2027-09-01 | retain | Google Chubby 锁服务（2006） | Google Chubby 锁服务（2006） | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-070 | 2027-09-02 | reframe | Figma 多人光标（2016—） | Figma 2016多人编辑：共同画布与评审协调 | causal-modeling → causal-modeling | 将缺单场光标日志的题改为官方交付规则与回顾明确支持的协调机制，不制造会议。 |
| ENG-106 | 2027-09-03 | retain | Language Server Protocol（2016） | Language Server Protocol（2016） | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-036 | 2027-09-04 | reframe | Snowflake 2012—2014 早期融资 | Snowflake 2014公开发布：技术承诺与需求证据 | evidence-selection → evidence-selection | 取消无材料的融资前采购复演，改为公开发布后投资论证验证。 |
| DES-036 | 2027-09-05 | reframe | 协作产品的套餐边界 | 协作产品的套餐边界 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-107 | 2027-09-06 | retain | Equifax Apache Struts 漏洞（2017） | Equifax Apache Struts 漏洞（2017） | evidence-selection → evidence-selection | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-071 | 2027-09-07 | retain | Netflix 从单次租赁转向订阅（1999） | Netflix 从单次租赁转向订阅（1999） | constrained-decision → constrained-decision | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-108 | 2027-09-08 | reframe | Google Tail at Scale（2013） | The Tail at Scale：延迟对冲的工作量与收益（2013） | quantitative-calibration → quantitative-calibration | 取得作者站点原论文全文；原数量输入现可直接追溯，缩小为已公布基准比较，保留数量动作。 |
| PRO-072 | 2027-09-09 | reframe | Notion Enterprise 安全功能（2020—） | Notion 2020 SCIM发布：登录与成员离职管理 | evidence-selection → evidence-selection | 只要求已交付安全功能的验证选择，不虚构采购阻碍或因SCIM成交。 |
| ENG-109 | 2027-09-10 | retain | OpenTelemetry 规范统一（2019） | OpenTelemetry 规范统一（2019） | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-037 | 2027-09-11 | reframe | Rivian 2021 IPO 估值 | Rivian 2021初步IPO区间：基本股本与产能爬坡 | quantitative-calibration → quantitative-calibration | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-037 | 2027-09-12 | reframe | 离线编辑与跨设备恢复 | 离线编辑与跨设备恢复 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-110 | 2027-09-13 | retain | Discord 消息存储迁移（2017—2023） | Discord 2022消息迁移：节点数与原始磁盘容量 | quantitative-calibration → quantitative-calibration | 原成本问题缺总成本账，正式改成作者公开的节点/原始磁盘容量比较，保留数量训练。 |
| PRO-073 | 2027-09-14 | retain | Pinterest 从 Tote 演化（2009—2010） | Pinterest 从 Tote 演化（2009—2010） | hypothesis-diagnosis → hypothesis-diagnosis | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-111 | 2027-09-15 | retain | Cloudflare 2026 年 2 月 BYOIP 路由撤销 | Cloudflare 2026 年 2 月 BYOIP 路由撤销 | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-074 | 2027-09-16 | retain | Adobe 收购 Figma 失败（2022—2023） | Adobe 收购 Figma 失败（2022—2023） | constrained-decision → constrained-decision | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-112 | 2027-09-17 | retain | Node.js libuv 事件循环（2009—） | Node.js libuv 事件循环（2009—） | causal-modeling → causal-modeling | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-038 | 2027-09-18 | reframe | Peloton 2018—2019 Pre-IPO | Peloton 2019：净CAC的硬件毛利抵扣 | quantitative-calibration → boundary-transfer | 正式采用预列边界问题：净CAC已经抵扣硬件毛利，不再求缺完整cohort的回本时间。 |
| DES-038 | 2027-09-19 | reframe | 投资尽调的最小信息集 | 投资尽调的最小信息集 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-113 | 2027-09-20 | retain | etcd Raft 故障恢复（2015—2018） | etcd Raft 故障恢复（2015—2018） | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-075 | 2027-09-21 | reframe | Upwork Elance 与 oDesk 合并（2013—2015） | Upwork 2015 Elance迁移：市场合并与参与者流失 | prediction-counterfactual → prediction-counterfactual | 取消未取得的单品类规模精算，保留迁移预测并使用招股回顾的实际用户损失。 |
| ENG-114 | 2027-09-22 | reframe | Gitpod 工作区快照（2020—） | Gitpod Classic：工作区快照分享的信任边界 | constrained-decision → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-076 | 2027-09-23 | reframe | Notion 数据库视图与关联（2018—） | Notion关系属性2026快照：客户与购买记录 | causal-modeling → causal-modeling | 冻结已读官方文档的2026快照，不把当前关系默认行为回填2018。 |
| ENG-115 | 2027-09-24 | retain | XZ Utils 后门事件（2024） | XZ Utils 后门事件（2024） | evidence-selection → evidence-selection | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-039 | 2027-09-25 | reframe | Canva 2013—2015 早期融资 | Canva 2015 Series A：组织采用与付费广度 | evidence-selection → evidence-selection | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-039 | 2027-09-26 | reframe | 默认安全的审计事件模型 | 权限变更审计的身份与保留边界 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-116 | 2027-09-27 | reframe | Envoy xDS 动态配置（2017—） | Envoy xDS 协议：ACK与实际生效 | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-077 | 2027-09-28 | reframe | Duolingo App Store 排名驱动（2010s） | Duolingo 2013 App of the Year：认可与需求归因 | evidence-selection → evidence-selection | 取消未定位的排名活动，采用已核实2013获奖与同期指标的证据题。 |
| ENG-117 | 2027-09-29 | replace | Meta ZippyDB SSD 成本优化（2010s） | RocksDB Ribbon Filter：内存与构建CPU权衡（2021） | quantitative-calibration → quantitative-calibration | 原ZippyDB单次SSD成本优化未获独立材料，正式替换为同属性能成本的独立Ribbon机制；全年rg未发现另一Ribbon案例。来源模型参数按作者假设标注，不冒充实测业务成本。 |
| PRO-078 | 2027-09-30 | retain | Instagram Stories 发布（2016） | Instagram Stories 发布（2016） | prediction-counterfactual → prediction-counterfactual | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-118 | 2027-10-01 | retain | Knight Capital 2012 年部署事故 | Knight Capital 2012 年部署事故 | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-040 | 2027-10-02 | reframe | Quibi 2020 关闭 | Quibi 2020公开信：有剩余现金仍停止投入 | constrained-decision → constrained-decision | 正式采用定性决策备用题，取消未公开现金跑道精算。 |
| DES-040 | 2027-10-03 | reframe | B2B 客户要求功能时如何取舍 | B2B 客户要求功能时如何取舍 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-119 | 2027-10-04 | retain | Google F1 数据库（2013） | Google F1 数据库（2013） | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-079 | 2027-10-05 | retain | Netflix 取消邮寄 DVD 与流媒体捆绑（2011） | Netflix 取消邮寄 DVD 与流媒体捆绑（2011） | hypothesis-diagnosis → hypothesis-diagnosis | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-120 | 2027-10-06 | reframe | NATS JetStream 持久流（2020） | NATS 2.2 JetStream：窗口去重与业务效果 | boundary-transfer → hypothesis-diagnosis | 明确冻结来源版本；不倒推候选初始年份。 |
| PRO-080 | 2027-10-07 | retain | Superhuman PMF 调查（2017—2018） | Superhuman 2017—2018 PMF 调查与分群路线图 | evidence-selection → evidence-selection | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-121 | 2027-10-08 | retain | Pants v2 构建系统（2020—） | Pants v2 构建系统（2020—） | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-041 | 2027-10-09 | reframe | Cloudflare 2014—2019 融资 | Cloudflare 2015融资：网络规模与防守条件 | boundary-transfer → boundary-transfer | 纠正未核2014融资身份，采用2015官方公告已有材料。 |
| DES-041 | 2027-10-10 | reframe | Streaming Pipeline 的背压契约 | 有限容量下的事件接收承诺 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-122 | 2027-10-11 | reframe | Akka Actor 系统（2010s） | Akka 2.4.20 PersistentActor：恢复与下一条消息 | prediction-counterfactual → causal-modeling | 明确冻结来源版本；不倒推候选初始年份。 |
| PRO-081 | 2027-10-12 | reframe | Twilio Developer-first API（2008—2016） | Twilio 2016披露：开发者自助与企业采购 | causal-modeling → causal-modeling | 改为同份2016文件明确支持的双重角色机制，不制造早期单个客户交接。 |
| ENG-123 | 2027-10-13 | retain | OpenAPI 3.0 规格演进（2017） | OpenAPI 3.0 规格演进（2017） | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-082 | 2027-10-14 | replace | Twitter 改为 X 的品牌重塑（2023） | HBO Max→Max 2023：品牌扩展与旧用户连续性 | prediction-counterfactual → prediction-counterfactual | 真实换题：Twitter/X缺直接结果材料，采用WBD同期公告中明确品牌目标和迁移措施；不要求广告信任测量。 |
| ENG-124 | 2027-10-15 | retain | Kubernetes CVE-2019-11253 | Kubernetes CVE-2019-11253 | causal-modeling → causal-modeling | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-042 | 2027-10-16 | reframe | Zoom 2013—2015 融资 | Zoom 2013 B轮：businesses与付费购买信号 | evidence-selection → evidence-selection | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-042 | 2027-10-17 | reframe | 硬件加软件业务的现金流边界 | 一笔硬件订单的现金缺口 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-125 | 2027-10-18 | retain | Cloudflare 2019 年 WAF 正则事故 | Cloudflare 2019 年 WAF 正则事故 | evidence-selection → evidence-selection | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-083 | 2027-10-19 | reframe | GitHub 开源贡献网络（2008—） | GitHub 2008 Fork Queue：跨fork采用提交 | boundary-transfer → boundary-transfer | 把未证明的关系网络锁定改为已交付Fork Queue的协作边界，不要求具体跨项目贡献故事。 |
| ENG-126 | 2027-10-20 | reframe | TiDB Percolator 模型（2016） | TiKV Deep Dive：Percolator primary提交后的secondary锁 | prediction-counterfactual → hypothesis-diagnosis | 明确冻结来源版本；不倒推候选初始年份。 |
| PRO-084 | 2027-10-21 | retain | Adobe Creative Cloud Libraries（2014—） | Adobe Creative Cloud Libraries（2014—） | causal-modeling → causal-modeling | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-127 | 2027-10-22 | retain | Buck2 引入 Dice 增量引擎（2023） | Buck2 引入 Dice 增量引擎（2023） | causal-modeling → causal-modeling | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-043 | 2027-10-23 | reframe | Klarna 2021—2022 估值重定价 | Klarna 2021—2022：headline估值与每股价值 | quantitative-calibration → quantitative-calibration | 正式改为headline重定价比例与每股经济损失的边界；保留可算部分，不假定清算顺位或同比例稀释。 |
| DES-043 | 2027-10-24 | reframe | 低频高价值工具如何被记住 | 低频高价值工具如何被记住 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-128 | 2027-10-25 | reframe | TimescaleDB Hypertables（2017） | TimescaleDB Hypertable：范围查询与chunk排除（文档快照） | quantitative-calibration → prediction-counterfactual | 明确冻结来源版本；不倒推候选初始年份。 |
| PRO-085 | 2027-10-26 | reframe | Zoom 会议邀请链接传播（2013—2020） | Zoom 2019披露：大客户的免费起点 | prediction-counterfactual → quantitative-calibration | 保留真实数量训练，取消未取得的首次主持流程与受邀用户分母。 |
| ENG-129 | 2027-10-27 | retain | JavaScript Promise 微任务队列（2015） | JavaScript Promise 微任务队列（2015） | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-086 | 2027-10-28 | reframe | TikTok For You 默认推荐流（2018—2020） | TikTok 2020 For You：无关注图的首轮推荐 | hypothesis-diagnosis → hypothesis-diagnosis | 改为公开冷启动机制与可检验解释，不要求缺失的真实分群实验或宣称推荐效果。 |
| ENG-130 | 2027-10-29 | reframe | YouTube 视频转码队列（2010s） | YouTube 2011 Hydra：等待与并行化的边界 | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-044 | 2027-10-30 | reframe | DoorDash 2019—2020 IPO 前融资 | DoorDash 2020披露：2019 GOV到毛利口径桥 | quantitative-calibration → quantitative-calibration | 原规划要求未披露的履约归属，现改为同份报表GOV到毛利的桥与不同利润口径；保留真实数字的数量校准。 |
| DES-044 | 2027-10-31 | reframe | 跨团队事件契约的版本演进 | 跨团队事件契约的版本演进 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-131 | 2027-11-01 | retain | Bazel Starlark 扩展接口（2017—2020） | Bazel Starlark 扩展接口（2017—2020） | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-087 | 2027-11-02 | reframe | Cloudflare Workers 定价演进（2017—2023） | Workers 2023 CPU计量：I/O等待的计费边界 | quantitative-calibration → boundary-transfer | 正式采用计量边界备用题，取消无实测同负载/完整旧价表的账单计算；不把官方例子当客户实测。 |
| ENG-132 | 2027-11-03 | retain | GitHub 2018 年 10 月数据库故障 | GitHub 2018 年 10 月数据库故障 | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-088 | 2027-11-04 | retain | Figma 浏览器协作编辑定位（2012—2016） | Figma 2015-12-03 Preview 后继续投入浏览器协作 | evidence-selection → evidence-selection | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-133 | 2027-11-05 | retain | Cassandra 无主写入（2010—2015） | Cassandra 无主写入（2010—2015） | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-045 | 2027-11-06 | reframe | DoorDash 2013—2014 Seed/Series A | DoorDash 2014 A轮：Palo Alto向郊区外推 | boundary-transfer → boundary-transfer | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-045 | 2027-11-07 | reframe | 双边预约产品的公平分配 | 双边预约产品的公平分配 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-134 | 2027-11-08 | retain | Gradle Configuration Cache（2020—） | Gradle Configuration Cache（2020—） | evidence-selection → evidence-selection | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-089 | 2027-11-09 | reframe | GitLab 从开源到企业平台（2011—2021） | GitLab Goldman Sachs客户案例：工具链整合任务 | constrained-decision → evidence-selection | 采用直接客户案例的采购任务，不要求未取得的历史合同签署日和部署控制。 |
| ENG-135 | 2027-11-10 | retain | npm event-stream 依赖劫持（2018） | npm event-stream 依赖劫持（2018） | evidence-selection → evidence-selection | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-090 | 2027-11-11 | retain | Google Stadia 关闭（2022—2023） | Google 2022-09-29 宣布关闭 Stadia 消费服务 | hypothesis-diagnosis → hypothesis-diagnosis | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-136 | 2027-11-12 | retain | Apache Druid 实时摄取（2011—） | Apache Druid 实时摄取（2011—） | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-046 | 2027-11-13 | reframe | FTX 2021—2022 风险融资 | FTX 2021 B轮公告后：托管与关联方权限尽调 | evidence-selection → evidence-selection | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-046 | 2027-11-14 | reframe | Webhook 平台的交付保障 | Webhook 平台的交付保障 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-137 | 2027-11-15 | reframe | Linux epoll（2002） | Linux man-pages epoll：interest/ready列表与通知边界 | quantitative-calibration → prediction-counterfactual | 明确冻结来源版本；不倒推候选初始年份。 |
| PRO-091 | 2027-11-16 | retain | Substack 推荐网络上线（2022） | Substack 2022-04-12 recommendations beta | boundary-transfer → boundary-transfer | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-138 | 2027-11-17 | retain | Stripe Idempotency-Key API 设计（2017） | Stripe Idempotency-Key API 设计（2017） | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-092 | 2027-11-18 | reframe | Google Photos 无限高质量备份（2015） | Google Photos 2015：备份到检索的复用价值 | causal-modeling → causal-modeling | 保留同版可读的核心机制，取消没有材料的2015导出/退出规则。 |
| ENG-139 | 2027-11-19 | retain | Cloudflare 2022 年 6 月网络中断 | Cloudflare 2022 年 6 月网络中断 | hypothesis-diagnosis → hypothesis-diagnosis | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-047 | 2027-11-20 | reframe | Better.com 2021—2023 SPAC 延期 | Better 2023财务附注：零票息bridge的股权风险 | prediction-counterfactual → prediction-counterfactual | 锁定2021 bridge在2023财务附注的状态，取消未确认最后一笔续命融资与完整估值。 |
| DES-047 | 2027-11-21 | reframe | 没有历史数据时如何设计定价实验 | 没有历史数据时如何设计定价实验 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-140 | 2027-11-22 | reframe | Consul 多数据中心架构（2015） | Consul 跨数据中心：成员发现与Raft保证（机制快照） | boundary-transfer → boundary-transfer | 明确冻结来源版本；不倒推候选初始年份。 |
| PRO-093 | 2027-11-23 | replace | Clubhouse 邀请码扩散（2020—2021） | Bluesky 2024取消邀请：增长控制与社区质量 | hypothesis-diagnosis → hypothesis-diagnosis | 真实换题：Clubhouse原文不可读，采用Bluesky同期公开记录；邀请码不仅可能制造稀缺，也被用于管理增长。 |
| ENG-141 | 2027-11-24 | reframe | Tree-sitter 增量解析（2018） | Tree-sitter 2018：局部编辑与语法结构复用 | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-094 | 2027-11-25 | reframe | Zoom 一键加入会议设计（2013—） | Zoom加入路径2026读取快照：电脑音频与电话 | boundary-transfer → boundary-transfer | 按实际读取的FAQ收窄为音频路径，不声称2013零安装/零注册，也不推定2018页面从未改过。 |
| ENG-142 | 2027-11-26 | retain | Cloudflare Workers 隔离与启动性能（2017—） | Cloudflare Workers 隔离与启动性能（2017—） | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-048 | 2027-11-27 | reframe | Palantir 2015—2020 资本评估 | Palantir 2020披露：Scale分群的选择边界 | hypothesis-diagnosis → hypothesis-diagnosis | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-048 | 2027-11-28 | reframe | 从旧工具迁移到新 B2B 产品 | 从旧工具迁移到新 B2B 产品 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-143 | 2027-11-29 | retain | Okta 2023 客户支持系统事件 | Okta 2023 客户支持系统事件 | causal-modeling → causal-modeling | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-095 | 2027-11-30 | reframe | Apple App Store 订阅分成规则（2016） | Apple 2016订阅公告：一年后的分成激励 | prediction-counterfactual → prediction-counterfactual | 限定同期公告明确的一年后收入提高，不将当前70/85细则、Small Business或累计规则倒填2016。 |
| ENG-144 | 2027-12-01 | reframe | ClickHouse MergeTree（2016—） | ClickHouse MergeTree：排序键与索引裁剪快照 | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-096 | 2027-12-02 | reframe | Calendly 链接式预约（2013） | Calendly预约页2026快照：两边身份与协调摩擦 | causal-modeling → causal-modeling | 采用已读官方帮助快照，取消未核2013初版全部行为。 |
| ENG-145 | 2027-12-03 | reframe | C++11 std::atomic 内存序（2011） | C++ N3337草案（2012）：原子标志的发布同步 | hypothesis-diagnosis → causal-modeling | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-049 | 2027-12-04 | reframe | Wix 2007—2008 Seed | Wix 2007：市场总量与付费需求的论证缺口 | quantitative-calibration → evidence-selection | 正式采用预列证据选择备用题，取消无付款数据的SMB可服务市场精算；memo本身是可检验的真实投资论证。 |
| DES-049 | 2027-12-05 | reframe | 配额控制与账单系统的边界 | 配额控制与账单系统的边界 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-146 | 2027-12-06 | retain | React Hooks 发布（2019） | React Hooks 发布（2019） | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-097 | 2027-12-07 | retain | Figma 从设计师向组织扩散（2016—2022） | Figma 2019-01-29 Organization 套餐与 Uber 全公司迁移 | evidence-selection → evidence-selection | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-147 | 2027-12-08 | retain | Facebook 2021 年 10 月全球中断 | Facebook 2021 年 10 月全球中断 | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-098 | 2027-12-09 | reframe | Meta Horizon Workrooms 方向调整（2021—2024） | Horizon Workrooms 2021 beta：VR与网页加入的任务差异 | hypothesis-diagnosis → hypothesis-diagnosis | 回到一手材料完整的2021 beta，取消未核2024精简动机及失败因果。 |
| ENG-148 | 2027-12-10 | retain | Uber Ringpop 一致性散列（2016） | Uber Ringpop 一致性散列（2016） | prediction-counterfactual → prediction-counterfactual | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-050 | 2027-12-11 | reframe | Airbnb 2020 IPO 前融资 | Airbnb 2020借款的年报核对：两笔融资与净到款 | constrained-decision → quantitative-calibration | 把接受/等待的未知现金选择改为2021年报已公开后的融资核对；保留实际数量输入。 |
| DES-050 | 2027-12-12 | reframe | AI 助手的隐私透明度 | AI 助手的隐私透明度 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-149 | 2027-12-13 | reframe | GitHub Actions 缓存服务设计（2019—） | GitHub Actions：缓存key、分支与PR作用域快照 | evidence-selection → evidence-selection | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-099 | 2027-12-14 | retain | eBay 买家与卖家信誉体系（1995—2000） | eBay 1999 年报记录的交易后 Feedback Forum 规则 | causal-modeling → causal-modeling | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-150 | 2027-12-15 | reframe | Dropbox Magic Pocket（2016） | Magic Pocket 2016：自建存储的迁移验证条件 | quantitative-calibration → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-100 | 2027-12-16 | reframe | Shopify App Store（2009） | Shopify 2009 App Store首发：BaseSync扩展边界 | boundary-transfer → boundary-transfer | 只讨论首发可核产品边界，不再要求未取得的2009完整数据权限或退出合同。 |
| ENG-151 | 2027-12-17 | retain | LastPass 2022 备份窃取 | LastPass 2022 备份窃取 | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-051 | 2027-12-18 | reframe | Dropbox 2015—2018 上市前投资 | Dropbox 2018披露：合并毛利增量与套餐归因 | quantitative-calibration → quantitative-calibration | 正式改为合并报表的毛利算术与归因上限；可比较总体收入/毛利率，不再拆解未披露个人与团队业务。 |
| DES-051 | 2027-12-19 | reframe | 巨头进入后小型平台如何选择位置 | 巨头捆绑下的两条可验证路线 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-152 | 2027-12-20 | retain | Elasticsearch 倒排索引（2010—） | Elasticsearch 倒排索引（2010—） | causal-modeling → causal-modeling | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-101 | 2027-12-21 | reframe | Canva Education 免费供给（2019） | Canva Education 2019 beta：教师中介的采用 | prediction-counterfactual → prediction-counterfactual | 保留2019免费beta实际课堂流程；明确预测而非要求已测量毕业后转化。 |
| ENG-153 | 2027-12-22 | retain | Erlang OTP Supervision（1990s—） | Erlang OTP Supervision（1990s—） | boundary-transfer → boundary-transfer | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-102 | 2027-12-23 | retain | Dropbox 文件夹同步交互（2008） | Dropbox 2008-09-11 公测上线的桌面文件夹同步 | causal-modeling → causal-modeling | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-154 | 2027-12-24 | retain | GitHub Actions 可复用工作流（2021） | GitHub Actions 可复用工作流（2021） | constrained-decision → constrained-decision | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| INV-052 | 2027-12-25 | reframe | GitLab 2015—2017 融资 | GitLab 2017 C轮：企业套餐与支付需求 | evidence-selection → evidence-selection | 本轮逐条复核原一手材料的事实、时点、证据和结果，正式以本条限定问题制作；不把公告/备忘录当成回报或唯一因果证明。 |
| DES-052 | 2027-12-26 | reframe | 细粒度权限系统的可理解性 | 细粒度权限系统的可理解性 | constructive-design → constructive-design | 逐题明确一项输出、可满足或可证明不兼得的约束和有辨识力的变化；保留Phase2已收窄的合成边界。 |
| ENG-155 | 2027-12-27 | retain | Cloudflare 2025 年 12 月解析逻辑故障 | Cloudflare 2025 年 12 月解析逻辑故障 | evidence-selection → evidence-selection | 本轮逐项复核原直接来源事实、证据与结果；以当前明确问题为制作范围，排除未披露负载、成本或首发年份外推。 |
| PRO-103 | 2027-12-28 | reframe | Atlassian Jira Cloud 分层定价（2019—2020） | Jira Cloud 2020免费档：十人边界与团队增长 | prediction-counterfactual → prediction-counterfactual | 只使用2020-03-18公告明确的免费人数及长期供给，不要求未核迁移细则或价格精算。 |
| ENG-156 | 2027-12-29 | reframe | Kubernetes 控制器协调循环（2014—2016） | Kubernetes Job controller：期望状态与异步控制（文档工件） | prediction-counterfactual → prediction-counterfactual | 明确冻结来源版本；不倒推候选初始年份。 |
| PRO-104 | 2027-12-30 | retain | Canva 在线设计模板化（2013） | Canva 2013-08-26 首次限量推出在线拖拽设计平台 | hypothesis-diagnosis → hypothesis-diagnosis | 复核原直接来源素材；保留原节点与单一认知动作。 |
| ENG-157 | 2027-12-31 | replace | Google Blaze 构建缓存（2015） | Rust 1.52.1：增量编译ICE后的发布选择（2021） | causal-modeling → constrained-decision | 正式应用Phase2替换槽：原Blaze2015与ENG080事件复用；Rust真实补丁发布的关闭优化/升级/降级选择独立于远端action缓存命中、特性合并和affected图。保留ENG157原日期ID。 |
