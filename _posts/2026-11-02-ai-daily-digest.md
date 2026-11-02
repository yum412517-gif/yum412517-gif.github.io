---
layout: post
title: "AI 每日精选 | 2026-11-02：美团 LongCat-2.5；主权账本与刷榜账本"
date: 2026-11-02 21:00:00 +0800
categories: [AI 新技术]
excerpt: "头条：美团 LongCat-2.5 长程多模态 MoE。观点谈主权账本与刷榜账本：OpenAI compute campuses、阿布扎比四协议、韩国 2027 AI/芯片预算，对照 GDPx 与 Particle 的单价口径。另有 Notion 积分切日、OpenCode MAU、YC W27 截止。"
---
![AI 每日精选封面 2026-11-02](/assets/2026-11-02-ai-daily-digest-cover.jpg)


> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 今天最值得看的几件事

- **头条：美团龙猫 LongCat-2.5**——约 **1.6T** 总参 / **48B** 激活的长程多模态 MoE；API 已开，权重「将放出」。
- OpenAI：拟把数据中心改称「AI compute campuses」，中期选举后政策/社区叙事。
- 阿布扎比 × OpenAI：政府 MRG、ADNOC、Mubadala、Inception42 四份协议。
- Notion：存量 Business / Enterprise 今日切到 AI 积分制。
- OpenCode：十月 MAU 称 **2200 万**（环比 **+28%**）；YC 转发。
- SemiAnalysis GDPx：11 域长时程智能体基准——刷榜≠干活。
- 韩国：李在明 **2027** 预算演说，AI/芯片约 **21.3 万亿韩元**。
- Particle-1 LongMemEval：读侧接近前沿、单价约 **1/23**（Garry Tan / YC 侧扩散）。
- Calegari×Tao：数学界如何接住「AI 倾倒」的结果。
- YC：Nitroduck Launch + **W27 今日 8pm PT** 截止。
- 观点：**主权账本与刷榜账本**——算力要过邻居，分数要对口径。

## 模型发布

### 1. 美团龙猫 LongCat-2.5：长程智能体向的原生多模态 MoE（头条）

技术博文署 **2026-11-1**，API 更新日志 **2026-11-02**「LongCat-2.5 上线」；IT之家约 **09:18**、经济观察网 / TechNode / 新京报（约 **18:41**）跟进。总参约 **1.6T**、每 token 激活约 **48B**；相对 2.0 强化原生视觉与智能体编程。视觉走多层级离散 token（SAE + RVQ），主干统一处理图文；长程 Agentic RL（异步 partial rollout、断网与清 Git 史抑 reward hacking、跨 harness 混合训练）。国产加速器上 dual-shard FSDP、W4A4 推理（相对 W8A8：Prefill/Decode 吞吐约 **+43% / +43%**；新京报另补线上压测 TTFT 约 **-16%**、逐 token 约 **-20%**）。官方表报 Terminal Bench v4.0 **38.5**、BrowseComp **91.9**、Vision2Web **78.6** 等（对照项多取公开报告/榜单）；兼容 Claude Code / Codex / Hermes 等 harness。官方价页列初上线限时折扣：输入未命中缓存 **¥2** / 命中 **¥0.04**、输出 **¥8**（每百万 tokens；美元档约 **$0.30 / $0.006 / $1.20**），并注明「实际费用以结算为准」。经济观察网 / 新京报另提商家 AI 经营工作台「妙手」（古茗/徐升记/益禾堂等连锁案例）与王兴「不会成为 token 工厂」口径；在线 demo/API 已开，GitHub/HF 权重「将随后放出」。

来源：[LongCat 技术博文](https://longcat.ai/blog/longcat-2.5)、[API 更新日志·2026-11-02](https://longcat.ai/platform/docs/zh/change-log)、[官方价页](https://longcat.ai/platform/docs/zh/pricing/longcat-2.5)、[IT之家](https://www.ithome.com/0/1020/873.htm)、[经济观察网](http://www.eeo.com.cn/2026/1102/1082059.shtml)、[TechNode 英文](https://technode.com/2026/11/02/meituan-launches-longcat-2-5-multimodal-ai-model-for-extended-coding-tasks/)、[动点科技](https://cn.technode.com/post/2026-11-02/meituan-longcat-2-5-multimodal-coding-model/)、[新京报](https://www.bjnews.com.cn/detail/1793616111168317.html)

国内大厂把「长程 agent + 国产栈 + 主业商家面」捆在一起发。受益的是已用 Claude Code/Codex harness、想试国产长程臂的团队，以及连锁商家侧「妙手」类经营助手；付钱的是把官方自测榜直接写成「全面超越 Opus 5 / GPT-6」的人。标「官方自测榜 ≠ 第三方复现；W4A4/国产栈数字 ≠ 任意云上同价吞吐；权重『将放出』≠ 已开源可用；价页限时折扣 ≠ 长期目录价；『妙手』案例 ≠ 模型能力通吃全行业经营」。

- 工程负责人：先在隔离项目接 API，对照自家 harness（Claude Code / Codex）跑同一批长程任务，再谈换栈。
- 成本同学：用价页折扣表估百万 token 账单，同时记下缓存命中率——命中档差一个数量级。
- 餐饮 / 零售运营：把「妙手」当主业产品面看，别当成通用大模型能力证明。

教程：以 [LongCat 技术博文](https://longcat.ai/blog/longcat-2.5) 与 [平台文档 / 价页](https://longcat.ai/platform/docs/zh/pricing/longcat-2.5) 为准；本条不编造未核实的「对打 Opus 5」评测视频。

## 工具与产品

### 2. OpenAI：拟将数据中心改称「AI compute campuses」

Axios 独家（署约 **11-01** 晚）引首席全球事务官 Chris Lehane：中期选举是「electoral portal」，跛鸭会期自 **11-09** 起发力，并瞄向 **2028**「AI 将成为议题」；叙事打包 AI「speed limits」（最强系统强制安全护栏）、数据中心社区契约/州立法参与、经济机会与国际标准。TechCrunch（约 **1:55 PM PST · 11-01** ≈ 北京 **11-02 05:55**）与 Business Insider 引发言人确认「compute campuses」命名——称更能描述算力/能源/技能投资的规模与角色，希望托管社区共同塑造并分享机会。

来源：[Axios](https://www.axios.com/2026/11/01/scoop-openai-post-midterm-policy)、[TechCrunch](https://techcrunch.com/2026/11/01/openai-might-rebrand-its-data-centers-as-ai-compute-campuses/)、[Business Insider](https://www.businessinsider.com/openai-ai-data-centers-rebrand-compute-campuses-midterms-2026-11)

基建叙事从「再建一座机房」改成「和邻居一起办校园」。受益的是社区联络、州立法顾问与能讲清电费/就业的运营商；付钱的是把「拟议改称」写成「已立法全面替换 Stargate 法律名称」的人。标「拟议改称与社区契约 ≠ 已立法或已全面替换行业用语」，勿写成民主党已赢下参众两院定局。

- 基建 / 能源从业者：公关话术之外，先把空气许可、电价与社区就业数字备齐。
- 政策观察：跛鸭会期与 **2028** 叙事是风向标，不是已通过的法案文本。
- 读者：这是政策产品面，不是新模型发布会。

教程：以 Axios / TechCrunch / BI 原文为准；本条不编造未核实的政策宣讲片。

### 3. 阿布扎比 × OpenAI：四份战略协议——政府、能源、投资、五年落地

阿布扎比王储会见 Sam Altman 并见证签署。官方称启动「全球首个」AI-native Machine-Readable Government（MRG）：指定政策/法规译成机器可读形式，辅助许可/证书等常规合规评估，每条评估可追溯到规则，官员保留最终决定；DGE 牵头，首个试点已在 ADAFSA 食品进口场景投产，推理走阿联酋本地 residency。能源面：ADNOC + G42（经 Inception42）+ OpenAI，称 ADNOC 为能源行业首家部署 OpenAI frontier 技术的公司；ADNOC/ZAWYA 补两起步场景——油田 master planning 与「仍在地下时给每桶油估值」的跨生产/炼化/物流/销售交易 agent 链；并点 Daybreak Blue 加固网防、ChatGPT Enterprise 向逾 **4 万**员工铺开（称 MENA 最大、采用率逾 **97%**）。投资面：Mubadala + Inception42 + OpenAI 用于分析/机会识别/风险评估。另 Inception42 与 OpenAI 签五年协议，覆盖政府/企业/教育。

来源：[Abu Dhabi Media Office](https://www.mediaoffice.abudhabi/en/crown-prince-news/khaled-bin-mohamed-bin-zayed-meets-sam-altman-and-witnesses-signing-of-agreements-with-openai/)、[The National·ADNOC](https://www.thenationalnews.com/business/energy/2026/11/02/adnoc-signs-agreement-with-openai-and-g42-to-deploy-frontier-ai/)、[The National·政府与教育](https://www.thenationalnews.com/news/uae/2026/11/02/abu-dhabi-agrees-openai-deals-to-boost-government-services-and-education/)、[Gulf News / WAM](https://gulfnews.com/uae/government/sheikh-khaled-meets-sam-altman-witnesses-signing-of-agreements-with-openai-1.500732283)、[ZAWYA / ADNOC](https://www.zawya.com/en/press-release/adnoc-signs-landmark-partnership-agreement-with-openai-and-g42-becoming-first-energy-company-to-deploy-openai-frontier-technology-1859105)

主权云把「本地推理 + 可追溯审批 + 能源交易」捆成一套落地故事。受益的是政府数字化集成商、能源数字化与本地 GPU 托管；付钱的是把「签约与试点」写成「已全政府无人审批」的人。标「签约与试点 ≠ 已全政府无人审批；『全球首个』属官方自称 ≠ 独立审计；能源/投资协议 ≠ 已披露合同金额或替换全部人工决策；企业普及率自报 ≠ 已替代核心运营审批」。

- 政务数字化：先盯「规则可追溯 + 人拍板」的试点边界，别抄「全自动发证」口号。
- 能源 IT：问清数据是否出阿联酋、agent 链哪一段必须人审。
- 企业采购：Enterprise 铺开率是采用指标，不是安全审计结论。

教程：以阿布扎比官方与 ADNOC/ZAWYA 新闻稿为准；本条不编造未核实的「MRG 落地」操作视频。

### 4. Notion：存量 Business / Enterprise 今日切到 AI 积分制

产品博文署 **10-19** 宣布新客即时生效，帮助中心写明存量 **2026-11-02** 切换。每位成员每月约 **1,500** Standard（`Auto` 路由、Notion 代选模型）+ **500** Select（自选模型 / 自建 Custom Agents；额度可因套餐与采购安排不同，以 Settings → Notion AI → Usage 为准）；二者分池、不互通、不跨成员、不滚存；用尽后默认暂停，管理员可开「允许用工作区 Notion credits 续跑」并另购。官方称 `Auto` 在 20+ 常见知识工作上相对 Opus 5.5 / Astra 约 **90%** 更低均费（「积分约可多用 **10×**」属自家估算）；Agent 单任务可跑逾 **24** 小时；可接 ChatGPT Plus/Pro/Go 进个人 Notion Agent（不耗 Standard/Select）；Enterprise BYOK 仍私人 alpha。

来源：[Notion Blog·Agents, rebuilt to do more for less](https://www.notion.com/blog/notion-ai-more-for-less)、[Notion Help·Manage your AI credits](https://www.notion.com/help/manage-your-ai-credits)

协作套件把「谁花多少、花在哪条臂」写进管理员面板。受益的是已重度用 Notion Agent、想控账单的中台；付钱的是切日前没看 Usage、把官方 **10×** 估算当成自己工作区账单的人。标「官方 10×/90% 估算 ≠ 任意工作区账单；切日 ≠ 全员已收到管理员邮件细则；ChatGPT 连接 ≠ 覆盖 Custom Agents」。

- 管理员：今天打开 Settings → Notion AI → Usage，确认 Standard/Select 余量与「用尽后续跑」开关。
- 知识工作者：长跑 Agent 优先走 `Auto`，自选旗舰模型前先看 Select 池。
- 已绑 ChatGPT 的个人用户：个人 Agent 连接不耗工作区两池——别和工作区额度混算。

教程：以 [Manage your AI credits](https://www.notion.com/help/manage-your-ai-credits) 与 Settings → Notion AI → Usage 为准；本条不编造未核实的「积分迁移」操作视频。

### 5. OpenCode：十月 MAU 称 2200 万（环比 +28%）

创始人 Jay（`@jayair`）称十月月活增至 **2200 万**，为自 **3 月**以来最大单月跳升；帖尾注「Sent from OpenCode」；`@ycombinator` 约北京 **10:05** 转发放大。

来源：[X·@jayair](https://x.com/jayair/status/2117064681592631643)、[X·@ycombinator RT](https://x.com/ycombinator/status/2117075543174906249)

开源编程 agent 的增长曲线仍在加速，但口径是创始人自报。受益的是已在 OpenCode / 多模型路由上押注的团队；付钱的是把 MAU 写成「已审计披露」或「官方已超越 Claude Code/Codex」的人。标「创始人自报 MAU ≠ 经审计披露；未拆付费/多模型路由贡献」，勿写成 YC 已投注新一轮。

- 工程负责人：拿自家仓库跑一周，记完成率与返工，再和 Claude Code/Codex 比，别只看 MAU 海报。
- 开源贡献者：增长窗口适合交插件/harness 适配，先看许可证与模型路由配置。
- 读者：YC 转发是放大，不是尽调结论。

教程：以 OpenCode 官方文档与产品页为准；通用编码 agent 入门可参考公开的 Claude Code / Codex 类教程（**同类操作参考**：agent 工作流，非本条 MAU 复现片）。本条不编造未核实的「2200 万用户」评测视频。

### 6. 韩国：2027 预算演说——AI/芯片约 21.3 万亿韩元

李在明国会 **2027** 预算演说：AI/芯片等「三大 mega」投入约 **21.3 万亿韩元**（约 **$16B**，称近翻倍于 **2026**）；另约 **4.7 万亿**（韩联社另述约 **4.6 万亿**）冲「世界最高性能」主权 AI 模型；总支出约 **820.9–821 万亿**（同比约 **+12.8%**）。另 **NEXT 10** 战略技术约 **13.8 万亿**、国防约 **73.3 万亿**（约 **+8%**，强调 AI/机器人/无人机混编）；芯片面点首尔圈 fab 与西南集群、电力/水/园区基建约 **2.1 万亿**；CNBC 另补培训约 **2000** 名半导体设计/区域芯片专才。预算案仍待国会通过。

来源：[Yonhap](https://en.yna.co.kr/view/AEN20261102000952315)、[The Straits Times](https://www.straitstimes.com/asia/east-asia/south-korea-to-double-spending-on-ai-and-chips-in-2027)、[CNBC](https://www.cnbc.com/2026/11/02/south-korea-ai-spending-budget.html)、[Seoul Economic Daily](https://en.sedaily.com/politics/2026/11/02/korea-to-invest-213-trillion-won-in-ai-under-2027-budget)

主权 AI 竞赛写进了财政案的总盘子。受益的是韩系存储/代工供应链、电力与园区基建、半导体人才培训；付钱的是把「预算演说」写成「已训出对标 Opus/GPT 的主权权重」的人。标「预算演说与编制 ≠ 已立法拨款或已训出对标模型；『世界最高性能』属政治目标 ≠ 已公布榜单；公司投资意向 ≠ 本条财政支出」。

- 产业观察：盯国会通过节点与 fab/电力分项，而不是口号里的「世界最高」。
- 求职 / 培训：合同院系与区域芯片专才项目比「主权模型」口号更近落地。
- 读者：这是财政与产业政策，不是新模型权重发布。

教程：以韩联社 / CNBC / 海峡时报报道为准；本条不编造未核实的预算解读片。

## 论文研究

### 7. SemiAnalysis GDPx：11 域高 ROI 智能体基准——刷榜≠干活

SemiAnalysis 发布 GDPx（General Agentic Benchmark）：芯片设计、网络安全、生物、金融、法律、量化交易、递归自我改进、硬件设计、材料科学、对齐、软件工程等 **11** 域；与 **14** 家领域 RL 环境伙伴共建 **206** 题，默认时限约 **8** 小时，优先跑各家原生 harness（Claude Code / Codex / Antigravity 等），无原生则默认 OpenCode；headline 为三轮 pass@1 域均权。v1.0 公开榜：Claude Opus 5.5 **12.0%**（约 **$51.41**/task）、Gemini 4 Carbon **10.9%**（约 **$16.29**）、GPT-6 Astra **9.6%**（约 **$53.99**）等；作者称金融/法律在严格二值评分下几乎全员 **0**，安全分类器会压低 Opus/Astra 在 cyber·bio·alignment 的总分，且无单一模型通吃各域。方法论批评 OpenAI GDPval 为「前 agent 时代」一次性提示+弱环境，主张用真实交易室/零日环境/实验室仪器等长时程环境；计划 **3–6** 个月迭代。

来源：[X·@SemiAnalysis_](https://x.com/SemiAnalysis_/status/2117075900575477855)、[GDPx 官网](https://gdpx.semianalysis.com/)、[SemiAnalysis Newsletter](https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities)

「旗舰模型很强」和「能在真实环境里干完 8 小时活」不是同一句话。受益的是评测工程、领域 RL 环境与 harness 厂商；付钱的是把「Opus 只有 12%」写成「只有 12% 智力」、或把 Carbon/Astra 写成已全面公开可用的人。标「单一研究机构基准 ≠ 行业标准；付费长文细节 ≠ 全任务开源可复现；安全拒答导致的分数下沉 ≠ 能力绝对排序」。

- 评测工程师：复现时固定 harness、时限与安全策略，别只贴 headline 百分数。
- 采购：问供应商要「你们在哪一域、多少美元/task 过了线」，别只要 Arena 名次。
- 创业者：金融/法律几乎全员 0 的域，可能是垂直 agent 的缺口，不是「大模型已经够用」的证据。

教程：以 [GDPx 官网](https://gdpx.semianalysis.com/) 与 Newsletter 方法论为准；本条不编造未核实的「复现 GDPx」评测视频。

## 最佳实践

### 8. Particle-1 LongMemEval：读侧接近前沿，单价约 1/23

Garry Tan 公开 gbrain-evals finding（`@ycombinator` RT）：在固定 gbrain 检索上下文上，LongMemEval-S **500** 题读侧——Claude Opus 5.5 **474/500（94.8%）**、GPT-6.1 Sol **464（92.8%）**、particle-1 **457（91.4%）**；相对 Opus 差距约 **-3.4** 分。目录价下每题正确约 **$0.0993 / $0.0381 / $0.0043**，约合 **$1** 买约 **10 / 26 / 230** 个正确答案（约 **23×** 价差相对 Opus）。作者称 particle-1 主要输在「建议类」题：把「结合既往偏好给建议」当成「检索不到就说不知道」。评测自承天花板高、单次作答、官方 gpt-4o 裁判、公开开发集；effort 设定不对齐；披露 YC 投 Particle、gbrain 为 Tan 自有项目。Particle-1 官方博文署 **2026-10-28**（本窗新意是 Tan 公开 finding，非模型首发日）。

来源：[X·@garrytan](https://x.com/garrytan/status/2117137390016073977)、[X·@ycombinator RT](https://x.com/ycombinator/status/2117138730372981181)、[gbrain-evals finding](https://github.com/garrytan/gbrain-evals/blob/b392700f2f647c201a8bedca71d43fd6a7fbb31c/docs/findings/2026-11-01-particle-1-longmemeval-w10b.md)、[Particle·Introducing Particle-1](https://particle.ai/blog/introducing-particle-1)

分数差几个点，单价差一个数量级——这才是采购常要面对的账。受益的是记忆/检索读侧工作负载与成本敏感的中台；付钱的是把「探索性 finding」写成「已全面追平 Opus」、或把读侧记忆题当成 agent 编码能力的人。标「探索性 finding ≠ 行业标准；目录价比 ≠ 任意账单；读侧记忆题 ≠ agent 编码能力；YC 投资披露须写明」。

- 采购 / 成本：先画「任务类型 × 可接受分差 × 单价」，再决定哪条臂跑读侧。
- 产品：建议类失败模式值得单独回归——「不知道」有时是对齐，有时是能力缺口。
- 读者：YC 投资与自有评测项目已披露，读结论时打折。

教程：以 [finding 原文](https://github.com/garrytan/gbrain-evals/blob/b392700f2f647c201a8bedca71d43fd6a7fbb31c/docs/findings/2026-11-01-particle-1-longmemeval-w10b.md) 与 [Particle 博文](https://particle.ai/blog/introducing-particle-1) 为准；本条不编造未核实的「1/23 单价」复现视频。

### 9. Calegari×Tao：「Mathematics has changed. Let's act like it」

Frank Calegari 在 Terry Tao「What's new」客座撰文（署 **1 November, 2026**；HN 热议）。以 OpenAI **10-06** 倾倒逾 **700** 篇研究稿为分水岭，主张数学界勿沉溺于「被掏空」情绪，而应像有限单群分类后的修订工作那样接管结果、拓宽问题视野。具体建议：所有成果按「可能 AI 辅助」评估并要求讲清为何有趣/引出何问；招聘更重当面交流与视野叙事；期刊提高写作与思想门槛；研究生教育加重广度；研讨班少报增量多讲卡住的大道；对 AI 产出结果主张人类共同体 ownership。文中援引 Hugo Duminil-Copin 对公开开放问题几乎「全部被宣称证明」的反应。

来源：[What's new·Mathematics has changed. Let's act like it](https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/)、[HN](https://news.ycombinator.com/)

科研社区的评价尺子，正在被迫从「谁先证出来」转向「谁能讲清这为什么重要」。受益的是能做修订、综述与问题设计的人；付钱的是把客座意见文写成「OpenAI 已正式解决 Langlands」或「数学期刊已全面停刊」的人。标「客座意见文 ≠ OpenAI/学会官方政策」。

- 研究者：交稿/研讨前多写一句「这个问题引出什么」，少写「模型又证了一条」。
- 期刊 / 招聘：把「视野叙事与当面交流」写进流程，比单纯加 AI 查重更贴近文中主张。
- 学生：广度与卡住的大问题，可能比堆增量引理更值钱。

教程：以 [博文原文](https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/) 为准；本条不编造未核实的访谈片。

## YC 动态

### 10. Nitroduck Launch + W27 今日截止

**Nitroduck（YC F26）Launch YC：** 花粉递送 CRISPR——把编辑载荷装进花粉粒，授粉后出编辑种子，绕开多数作物「单细胞再生整株」瓶颈；宣称让育种从平均 **8–16** 年压缩、使抗性基因迭代快于病原演化，并引用 specialty crops 约 **$40B** 潜在特许权市场；基因组测序与 AI 用于「该瞄什么性状」；称 **2026** 起约全球 **2/3** 地区基因编辑合法。

**W27：** 准时申请截止今日 **November 2 at 8pm PT**（≈ 北京 **11-03 12:00**）；准时提交者约 **December 11** 前获决定，逾期仍审但不承诺时点；批次 **1–3 月**旧金山线下。`@ycombinator` 全日多轮催更，「Consider this a sign」；晚间 `@paulg` 亦发截止日提醒并被 YC RT。F26 Demo Day 仍约 **December 2, 2026**。

来源：[Launch YC·Nitroduck](https://www.ycombinator.com/launches/WZO-nitroduck-designs-new-colors-flavors-and-disease-resistance-into-fruits-and-veggies)、[YC Apply](https://www.ycombinator.com/apply/)、[X·@ycombinator「Consider this a sign」](https://x.com/ycombinator/status/2117122326198374662)、[X·@paulg 截止日催更](https://x.com/paulg/status/2117206380356456500)、[X·@ycombinator RT paulg](https://x.com/ycombinator/status/2117209391976120391)

一边是育种周期的压缩叙事，一边是申请窗的最后几小时——YC 本窗两条都在「窗口期」。受益的是农业生物技术与正在交材料的创始人；付钱的是把 Launch 叙事写成「已商业化全作物平台」、或把截止日写成「Demo Day 已开始」的人。标「Launch 叙事 ≠ 已商业化全作物编辑平台；法律覆盖与田间审评因国而异；截止日 ≠ Demo Day；逾期申请 ≠ 一律拒收」。

- 想申请 W27：现在交比再改口号重要；逾期仍可能被看，但不承诺时点。
- 农业科技：先问监管辖区与田间试验路径，再谈「AI 定靶」。
- 读者：Nitroduck 与 W27 催更并列批次窗口，不是同一条产品新闻。

教程：申请以 [YC Apply](https://www.ycombinator.com/apply/) 为准；Nitroduck 以 Launch 页为准。本条不编造未核实的申请辅导或田间操作视频。

## 观点洞察

### 主权账本与刷榜账本：算力要过邻居，分数要对口径

今天几条其实在翻同一本账的两面：**谁出钱、谁点头、邻居同不同意**；以及 **榜上的分，对应哪条臂、多少美元、什么环境**。

先看主权这一面。OpenAI 把数据中心改口叫「AI compute campuses」，Axios 写的是中期选举后的政策冲刺——社区契约、州立法、speed limits，瞄的是跛鸭会期和更远的 **2028**。阿布扎比同一天签了四份协议：政府 MRG 试点已经在食品进口场景跑，ADNOC 把油田规划和桶价估值交给本地推理上的 frontier 技术，官员仍留最终决定权。韩国国会演说里，AI/芯片约 **21.3 万亿韩元**、主权模型另约 **4.7 万亿**——财政案写成「近翻倍」，但演说不等于拨款到账，更不等于已经训出对标 Opus 的权重。三条放一起看，故事不是「谁家模型更强」，而是**算力落在哪片土地上，要过谁的许可**：邻居、议会、王室与国企董事会。美团 LongCat-2.5 的「国产栈 + 限时价 + 妙手商家面」，其实也是另一本主权/主业账——只是货币和审批链条换了中国语境。

再翻到刷榜这一面。GDPx 把 11 个高 ROI 域、约 8 小时时限、原生 harness 摆上台面：Opus 5.5 headline 约 **12%**，金融/法律严格二值下几乎全员 **0**，还附上每 task 几十美元的账单。Particle-1 在 LongMemEval 读侧只落后 Opus 约 **3.4** 分，目录价却差到约 **23×**。两套数字提醒同一件事：**「接近前沿」可以指分数，也可以指每正确一题花多少钱；「12%」不是「只有 12% 智商」，而是「在这套又贵又长的环境里过线率」**。Notion 今天把存量工作区切到 Standard/Select 分池，OpenCode 自报 MAU **2200 万**——前者逼你看额度表，后者很容易让人用增长海报代替任务完成率。我自己写材料前会多问一句：这个百分数，是 Arena、是 GDPx、还是你业务里那 50 个工单？

所以两本账最好一起对：

1. **主权账：** 机房/API 落在哪？社区、国会、国企董事会谁签字？本地 residency 是营销词还是合同条款？
2. **刷榜账：** 分是哪套基准、哪条模型臂、含不含 harness 与安全拒答？单价是目录价还是你账单上的有效价？

过得了这两问，再谈「我们要用 AI 改造某某」也不迟；过不了，再响的 campuses、再亮的 leaderboard，都只是换了封面的加预算。个人观点，数字以各条原文为准，不构成投资或采购建议。

## 今日机会总结

今天的脊柱是：**国产长程 MoE 上线**（LongCat-2.5）、**算力政治与主权落地**（compute campuses、阿布扎比四协议、韩国预算）、**额度与单价口径**（Notion 切日、GDPx、Particle），外加 **YC 窗口**（Nitroduck + W27 截止）。观点侧把主权许可和刷榜口径收成同一本对账题。

若只选三条可执行方向：

1. **长程 agent 国产臂试点**：对标 LongCat-2.5，在隔离项目接 API，用现有 Claude Code/Codex harness 跑同一批长任务，输出「完成率 × 缓存命中 × 人民币账单」对照表；客户是想降旗舰依赖、又不敢盲切的中台。
2. **主权/合规落地咨询**：政府 MRG 式「规则机器可读 + 人终审」、能源本地推理、数据中心社区契约——卖可审计试点包，不卖「全自动审批」口号。
3. **评测与单价对账**：帮团队把 GDPx 类长时程域分数，和 Particle 类读侧单价画在同一张图上；客户是采购与 CFO，怕「榜上第一、账单打穿」。

## 普通人今天就能做的 3 件事

1. **用 Notion Business / Enterprise 的人：** 打开 Settings → Notion AI → Usage，确认 Standard/Select 余量与用尽后是否允许 credits 续跑——今天是存量切日。对照 [帮助中心](https://www.notion.com/help/manage-your-ai-credits)。
2. **跑编码 agent / 看模型榜的人：** 任选一个真实任务，记下「用哪条臂、花多少、是否在时限内做完」；对照 GDPx「长时程 + 美元/task」思维，别只截一张 leaderboard。
3. **想申请 YC W27 的人：** 截止是今日 **8pm PT**（北京 **11-03 12:00**），先交再磨。入口：[YC Apply](https://www.ycombinator.com/apply/)。

---

*草稿待审阅；确认后再发博客。有要改的直接说。*
