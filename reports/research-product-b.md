# Phase 3 来源核查：PRO-087—PRO-104（不含 PRO-098）

核查日期：2026-10-25。受派 17 条均实际尝试：9 sourced、8 blocked、0 ready。PRO-098 按整合分工跳过，沿用已有 blocked 记录。状态仅为来源研究，不晋级 ready；规划降级未经正式应用。

## PRO-087

```yaml
id: PRO-087
status: blocked
reason: 已核实 CPU 计量调整及适用窗口，但两版价格和真实同负载输入不足，数量主线仍 blocked。
event: Workers 2023-09-28 CPU-time 新计价公告
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
  text: ''
  source_ids: []
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
attempts:
- 打开并阅读定价公告正文与迁移范围；点击 old/new pricing 图均抓取失败。
- 检索历史定价和正文 workload；未把示意用量或当前滚动价格替代历史真实负载。
phase2_conditions:
- quantitative 门槛未闭合；boundary-transfer 是规划允许但尚未正式应用的降级。
- 保留一次 2023 调整，不混用 2017—2023 多轮政策。
```

## PRO-088

```yaml
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
status: blocked
reason: 真实企业采用有直接材料，但采购节点时间和部署控制证据未闭合，不能支持规划要求的当时取舍。
event: GitLab / Goldman Sachs 企业采用候选，采购时点未闭合
cutoff: 待确认一次集团采购决定及日期；不以当前客户页替代历史合同
initial_facts: []
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
  text: ''
  source_ids: []
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
  - E1
  - E2
attempts:
- 检索集团采购/部署控制候选并打开 Goldman Sachs 客户案例全文，检查采购角色、评估过程和部署说明。
phase2_conditions:
- 仍需单次采购日期、部署约束及比较选项；不得扩写成十年企业化路线。
```

## PRO-090

```yaml
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
status: blocked
reason: 备份到检索复用机制已核，但规划要求的同版导出和退出边界缺直接材料。
event: Google Photos 2015-05-28 自动备份任务
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
  text: ''
  source_ids: []
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
attempts:
- 打开首发公告核对套餐、自动上传、搜索和分享。
- 检索 2015 Google Photos Takeout / export，结果多为当前第三方迁移教程，未将其作为当时导出条件。
phase2_conditions:
- 在补足同期导出条件前保持 blocked；不提前引入后来收费或无限备份取消。
```

## PRO-093

```yaml
id: PRO-093
status: blocked
reason: 尝试直接访问官方材料均失败；搜索摘要不能替代原文，且缺同批邀请用户的长期关系行为证据。
event: Clubhouse 2021 opening-day 取消邀请候选
cutoff: 2021 年取消 waitlist 前；精确发布日期待直接材料确认
initial_facts: []
evidence: []
outcome:
  text: ''
  source_ids: []
interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
unknowns:
- 官方全文被检索索引收录但实际 open 不可访问，未完成直接来源检查。
- 邀请对下载及长期关系网络的独立因果效果与留存分群未知。
sources:
- id: S1
  url: https://blog.clubhouse.com/opening-day/
  publisher: Clubhouse
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports: []
attempts:
- 搜索官方 Opening Day，实际打开带/不带末尾斜杠均不可访问。
- 尝试官方 early beta Check 1/2/3 与 Android welcome 页面亦不可访问；不把搜索摘要全文当核查完成。
phase2_conditions:
- 保留邀请机制候选；需恢复原始材料和单一节点，不编造稀缺导致留存的结论。
```

## PRO-094

```yaml
id: PRO-094
status: blocked
reason: 有同期标题和流程说明，但尚缺完整同版安装、身份与设备约束，无法确认主线摩擦边界。
event: Zoom 2018/2020 邀请加入流程候选
cutoff: 待锁定一个设备、版本和受邀加入任务
initial_facts: []
evidence:
- id: E1
  text: 2018-01-30 FAQ 列出浏览器输入 meeting ID、客户端和移动 app 等加入方式，但未完整说明该设备安装和身份条件。
  source_ids:
  - S1
  availability: unknown
- id: E2
  text: 2020-12-16 入门文章写浏览器可不下载客户端加入；该网页现有内容未提供冻结版本证据。
  source_ids:
  - S2
  availability: unknown
outcome:
  text: ''
  source_ids: []
interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
unknowns:
- 2013 初版或拟选历史版中单一受邀设备的身份要求、浏览器限制、安装提示和主持人设置仍未全部闭合。
- 不能把当前 Zoom Events OTP 流程混入早期 Meetings。
sources:
- id: S1
  url: https://www.zoom.com/en/blog/zoom-faqs-joining-meetings/
  publisher: Zoom
  published_at: '2018-01-30'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
- id: S2
  url: https://www.zoom.com/en/blog/getting-started-with-zoom-meetings/
  publisher: Zoom
  published_at: '2020-12-16'
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E2
attempts:
- 打开两篇官方指南正文；检索到当前无账户加入和认证设置文档，但因版本不锁定未倒填历史。
phase2_conditions:
- 必须先锁定设备/版本/主持人设置；仅判断一次加入摩擦，不复用 PRO-085 的成为发起者传播预测。
```

## PRO-095

```yaml
id: PRO-095
status: sourced
reason: 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。
event: Apple 2016-06-08 宣布订阅资格与一年后分成增强
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
  text: 2016 官方公告确有按订阅持续时间改变开发者分配的设计；当前官方文档记录 70/85 这一行为，2016 精确细则仍需原版核对。
  source_ids:
  - S1
  - S2
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
  - outcome
attempts:
- 打开 Apple 2016 Coming Soon 原公告与现行订阅文档；核对当前分配规则并标明版本差异。
- 原文 What’s New in Subscriptions 链接 404，尝试 WWDC2016 301 两版 URL 均不可访问；未以媒体摘要替代精确历史条文。
phase2_conditions:
- 可做一年后分成改变的定性反事实预测；涉及 2016 数值账单或例外前必须补原版规则。
- 不前置后来的 Small Business Program 或外链付费政策。
```

## PRO-096

```yaml
id: PRO-096
status: blocked
reason: 创办年份可核，但初版两边身份与预约流程缺同版证据；现有描述混合后续多年功能。
event: Calendly 2013 链接式预约初版候选
cutoff: 2013 初版上线时；精确功能版本未锁定
initial_facts: []
evidence:
- id: E1
  text: Calendly 公司介绍确认 Tope Awotona 于 2013 创办，目的为减少预约来回邮件。
  source_ids:
  - S1
  availability: post_decision
- id: E2
  text: 开发参与方 Railsware 描述可分享 URL、invitee 只能见预约页而非后台；页面同时列出现代集成，其 timeline 从 2014-01 起。
  source_ids:
  - S2
  availability: unknown
outcome:
  text: ''
  source_ids: []
interpretation: 产品机制和可迁移判断属于维护者分析；厂商解释、用户叙述和实际观察须分别呈现。
unknowns:
- 2013 版 invitee 是否无需账户、具体可见可用时段及确认流程未取得同期材料。
- 当前无账户帮助文章和社区回复不能证明 2013 同样实现。
sources:
- id: S1
  url: https://calendly.com/about
  publisher: Calendly
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E1
- id: S2
  url: https://railsware.com/case-studies/calendly/
  publisher: Railsware, development participant
  published_at: null
  source_type: primary
  checked_at: '2026-10-25'
  supports:
  - E2
attempts:
- 打开 Calendly 公司历史和 Railsware 参与方 case study，核对年份与现代功能混写。
- 打开 2025-09-11 社区无账户预约说明 https://community.calendly.com/asked-answered-79/do-invitees-need-to-login-to-book-through-calendly-4644，因非 2013 版本且作者身份不充分未作为历史直接证据。
phase2_conditions:
- 不得将当前可用性自动倒推 2013；补同期演示/页面或明确提出改锚建议后再制作。
- 不复用 Zoom 首次发起会议的传播预测。
```

## PRO-097

```yaml
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

## PRO-099

```yaml
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
status: blocked
reason: 首发身份与单项插件用途已核，但规划需要的早期权限、数据及替代边界材料不足。
event: Shopify 2009-06-02 App Store 首发：BaseSync 商品同步需求
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
  text: ''
  source_ids: []
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
attempts:
- 打开 2009 原始发布稿，核对 API beta、具体首发 app、交易管理与分发约定。
- 检索首发 app 历史，当前开发文档不能闭合 2009 插件数据/权限条件。
phase2_conditions:
- 保留单项 BaseSync 任务；补当时插件权限及退出数据前保持 blocked。
- 不得用全部插件数量或厂商动机直接推出留存因果。
```

## PRO-101

```yaml
id: PRO-101
status: sourced
reason: 直接来源支持可识别的产品节点及其交付行为；仍未执行 Case QA。
event: Canva for Education 2019 澳大利亚学校 beta：教师布置与批改课堂作品
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
  text: 课堂任务有实际供给和评阅流程；该资料没有证明教育用户毕业后独立留存或付费转换。
  source_ids:
  - S1
  - S2
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
  - outcome
attempts:
- 打开四页官方教育媒体包，核对 Australian beta、免费内容、Classroom 集成及评阅流程。
- 打开官方十年时间线核对 2019 年份；未以当前教育资格和产品条件回填初版。
phase2_conditions:
- 主输出为迁移预测和不迁移反例，后续身份/资产路径缺口必须列为验证条件。
- 不要把免费学校账户计为未来付费需求。
```

## PRO-102

```yaml
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
status: blocked
reason: 免费发布日期和人数限制可核，但同版功能与迁移规则未闭合，无法完成完整采用/升级边界。
event: Atlassian 2020-03-18 Jira Cloud 免费档全面推出
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
  text: ''
  source_ids: []
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
phase2_conditions:
- 先补同版功能、价格和迁移规则再给升级预测；保持一次 2020-03-18 节点。
```

## PRO-104

```yaml
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
