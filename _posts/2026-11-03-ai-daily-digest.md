---
layout: post
title: "AI 每日精选 | 2026-11-03：Anthropic S-1「或将触及」RSI；能用、能证、能关"
date: 2026-11-03 21:00:00 +0800
categories: [AI 新技术]
excerpt: "头条：Anthropic 修订 S-1/A，风险侧称或将触及 RSI 阈值，单季营收约 $17B。观点谈 Agent 的三道闸：谁能用、谁能证明跑的是哪份权重、谁能一键关停。另有 LifeVal、CrowdStrike Kill Switch、Hydrogen-1.0、Salesforce×Cresta、Tutor $75M、YC W27 准时截止已过。"
---
![AI 每日精选封面 2026-11-03](/assets/2026-11-03-ai-daily-digest-cover.jpg)


> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 今天最值得看的几件事

- **头条：Anthropic 修订 S-1/A**——内部估计「或将很快」触及 RSP 里由 AI 导致的戏剧性加速进展（媒体作 RSI 近阈）；单季营收约 **$17B**，算力承诺约 **$895.4B**；澳零售拟走 CommSec、纳斯达克 ticker **ANT**。
- OpenAI LifeVal：日常生活任务智能体评测尺（对照昨 GDPx「专家高 ROI」）。
- CrowdStrike：Falcon Guardian **AI Kill Switch** 今日可用，并拟购 Dreadnode / Fiddler。
- OpenAI：下一轮内部 security sprint × Cathedral Systems，Bug Bounty 例外最高约 **$172K**。
- Deep Principle Hydrogen-1.0：开源权重科学模型（化学/材料/生命）。
- Salesforce 签协议收购 Cresta：语音客服 Agent，报道约 **$2.7B**。
- Tutor Intelligence：**$75M** Series B（a16z），仓储机器人「先部署后建模」。
- 高盛：收紧 Claude Code / Copilot 系，交易员与银行家多数失去 vibe coding 权限。
- Anthropic FlashProve + 文本水印自今日扩到更多既有 Claude。
- Stanford Zou 组：复测 **50** 条经典 LLM 结论，约 **44%** 已过期。
- YC：W27 准时截止已过，仍收逾期；Garry Tan 称年花约 **$10–20 万** token。
- 观点：**能用、能证、能关**——Agent 今天写进合同的三道闸。

## 最佳实践

### 1. Anthropic 修订 S-1/A：「或将触及」RSI 与单季约 $17B（头条）

TechCrunch（约 **2:14 PM PST · 11-02** ≈ 北京 **11-03 06:14**）与 The Verge / CNBC 跟进修订稿：风险侧写内部估计「或将很快」触及 RSP「由 AI 导致的戏剧性加速进展」定义，同时写明**当前模型均未**被标为越过该阈值、仍在评估；不预期可预见期内可安全让 Claude **完全自主**设计并构建下一代 frontier 而无有意义人类监督，正考虑更新 RSP。财务侧补全三季：单季营收约 **$17B**（约 **$16.96B**，同比约 **+1,127%** / 环比约 **+47%**），净亏损约 **$23.29B**（报道多指非现金融资相关费用为主），算力/基础设施承诺约 **$895.4B**。澳侧升温：CommSec 称若 IPO 推进将作澳零售牵头经纪，**不**申请 ASX，交割后拟纳斯达克 ticker **ANT**；媒体叙事「感恩节前」上市；估值讨论约 **$1.5T**（对照早前约 **$2T**）。SEC EDGAR 可核。

来源：[TechCrunch·RSI](https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/)、[The Verge·S-1 numbers](https://www.theverge.com/ai-artificial-intelligence/1024420/anthropics-updated-s-1-has-even-more-eye-popping-numbers)、[CNBC](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html)、[SEC EDGAR S-1/A index](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/0001628280-26-068676-index.htm)、[CNA/Reuters·Australian retail](https://www.channelnewsasia.com/business/anthropic-plans-australian-share-offer-in-ipo-commsec-says-6514811)、[AFR·CommSec](https://www.afr.com/technology/anthropic-reveals-more-australian-details-as-ipo-approaches-20261103-p61as6)

招股书把「快碰到自改进阈值」和「单季一百七十亿营收」写在同一份文件里——这是治理披露，不是产品发布会。受益的是合规/风险披露顾问、券商零售配售渠道，以及盯 RSP 标签节奏的安全团队；付钱的是把「或将触及」写成「Claude 已自主迭代自身」、或把 **$895.4B** 承诺写成「已全额现金支出」的人。标「『或将触及』≠ 已实现 RSI；未贴超阈标签；**$17B** 营收 / **$895.4B** 承诺 ≠ 已 IPO 定价或已全额现金支出；澳零售经纪筹备 ≠ 招股书已生效或已开申购」。

- 合规 / 风控：先读 RSP 原文定义与「当前未超阈」并列句，再转发媒体标题。
- 投资者观察：招股书兼具披露与营销，TC 提醒 dual 读法——数字以 EDGAR 为准。
- 安全研究者：公司明写「不预期完全自主造下一代」，这是政策句，不是技术天花板证明。

教程：以 [TechCrunch](https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/) 与 [SEC EDGAR](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/0001628280-26-068676-index.htm) 为准；本条不编造未核实的「RSI 已实装」讲解片。

## 模型发布

### 2. Deep Principle Hydrogen-1.0：开源权重科学模型

杭州 Deep Principle 官方博文署 **November 2, 2026**：面向化学/材料/生命科学，在 Z.ai GLM-5.3 上做领域后训练；数据含领域知识、完整实验记录（意图/步骤/观察/结果，含失败）与发现轨迹。官方自测 FrontierScience-Research 约 **38.3%**（对照 GPT-6-Astra **33.3%**）、GPQA-Diamond 约 **93.0%**；MarkTechPost 等转述总参约 **753B** MoE（激活约 **40B** 级）、上下文约 **1M**。MIT 许可权重上 Hugging Face / ModelScope，另有 NVFP4 / MXFP4 量化仓；API 走 NeuroSpark，亦可进公司 AI Scientist「Mira」。官方强调完整数据集与配方未随权重公开，输出须专家复核。

来源：[Deep Principle Blog](https://blog.deepprinciple.com/introducing-hydrogen-1.0/)、[Hugging Face·Hydrogen-1.0](https://huggingface.co/deep-principle/Hydrogen-1.0)、[MarkTechPost](https://www.marktechpost.com/2026/11/02/deep-principle-hydrogen-1-0-open-weight-scientific-model/)

开权重科学模把「实验失败轨迹」写进训练叙事，但配方仍锁着。受益的是材料/化学实验室草稿臂、可本地部署的科研团队；付钱的是把官方自测榜写成「已全面超越 Astra 全家」、或把开权重当成已开训练数据的人。标「官方自测榜 ≠ 第三方复现；开权重 ≠ 开训练数据/配方；辅助草稿 ≠ 已验证实验结论」。

- 科研工程：先在隔离环境跑公开基准子集，再谈进湿实验流程。
- 实验室负责人：合同里写清「模型输出须专家复核」，别当自动发论文按钮。
- 开源贡献者：权重可下，配方不可抄——别承诺「可完整复现训练」。

教程：以 [官方博文](https://blog.deepprinciple.com/introducing-hydrogen-1.0/) 与 [HF 模型卡](https://huggingface.co/deep-principle/Hydrogen-1.0) 为准；本条未核到针对 Hydrogen-1.0 的成熟 Bilibili/YouTube 操作片，不编造。

## 工具与产品

### 3. OpenAI LifeVal：日常生活任务的智能体评测尺

官方 Research 署 **November 2, 2026**：任务域来自 ATUS / MTUS 及约 **3,995** 人问卷，覆盖照护、健康、教育、家务行政、个人财务、购物、政府服务等。官方示例分含入园短名单约 **93.1%**、洪涝志愿者组织约 **98.0%**、寻房并加契税/地契到购物车 **100%** 等；二手整理曲线：GPT-5.2（约 **2025-12**）均奖励约 **49.3%** → GPT-6 Astra（约 **2026-09**）约 **80.6%**（仅自家模型序列）。强调 browser/computer use 与 connectors；**未**公开完整题集/评分细则/他厂对照。

来源：[OpenAI·LifeVal](https://openai.com/index/lifeval/)、[OpenAI News](https://openai.com/news/)

昨天 GDPx 量的是芯片/金融/法律等高 ROI 长时程域，今天 LifeVal 量的是「帮你办完一件琐事」。尺子不同，结论不能串。受益的是个人助理产品与 connectors 集成商；付钱的是把「Astra 在 LifeVal 约 80%」写成「真实生活中无人接管成功率 80%」的人。标「自家评测曲线 ≠ 可复现公开榜；示例高分 ≠ 全任务集；未含 Claude/Gemini 对照」。

- 产品经理：选型时问「你们测的是 LifeVal 式日常，还是 GDPx 式专家域？」
- 个人用户：示例高分多挂在具体剧本上，别当成全家桶万能。
- 评测工程：没有公开题集前，别宣称第三方复现。

教程：以 [LifeVal 官方页](https://openai.com/index/lifeval/) 为准；本条无已核实的第三方复现教程视频。

### 4. CrowdStrike：AI Kill Switch + 拟购 Dreadnode / Fiddler

Fal.Con Europe 多条官方 PR 署 **November 3, 2026**：Falcon Guardian **AI Kill Switch** 今日可用——授权管理员可在 agent 越权/失控时终止运行（先 Gateway、随后扩 endpoint）、策略阻再启、切断企业网并写审计。Guardian 自约 **2026-09** GA，本轮补齐 AI Gateway、agent-level hooks（点名 Claude Code / Codex / Copilot / M365 Copilot / OpenCode / Cursor）、SafeMind、AI 供应链（恶意 skills/MCP），以及 Anthropic 合作在 Claude Cowork VM 内跑 Falcon sensor（pre-beta）。拟购 **Dreadnode**（部署前自动 AI 安全测试，拟 **Q4 FY27** GA）与 **Fiddler AI**（Agent 可观测，拟以 Falcon Observe 并入，同窗 GA 目标）；两笔均以现金为主，交割目标 CrowdStrike **FY27** 四季。客户例：Everpure CISO 称有 Kill Switch 才敢扩大 agent。

来源：[CrowdStrike·AI Kill Switch](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-introduces-ai-kill-switch-for-ai-safety/)、[Acquire Dreadnode](https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-acquire-dreadnode-advance-ai-trust-and-deliver/)、[Acquire Fiddler](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-to-acquire-fiddler-to-deliver-agent-observability/)、[Blog·Falcon Guardian](https://www.crowdstrike.com/en-us/blog/crowdstrike-advances-ai-security-and-safety-falcon-guardian/)

企业终于把「一键关停 agent」写进产品名——和招股书里的 RSI 近阈叙事，是同一天的两面。受益的是已上 Claude Code/Cursor 机群、需要审计与急停的安全团队，以及红队/可观测厂商；付钱的是把「签署拟购」写成「已交割全功能上线」、或把 hooks 名单当成已覆盖任意自研 agent 的人。标「签署协议 ≠ 已交割；Kill Switch 今日可用 ≠ 已默认装进全部客户；hooks 名单 ≠ 已覆盖任意自研 agent」。

- 安全负责人：先盘点公司里跑着的编码 agent 与 MCP，再问 Kill Switch 挂在 Gateway 还是 endpoint。
- CISO / 合规：采购合同加「失控终止 + 审计日志保留」条款，比只买「更强模型」更贴今天的新闻。
- 开发者：hooks 覆盖主流 IDE agent，自研 runtime 仍要自己留急停。

教程：以 [Kill Switch PR](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-introduces-ai-kill-switch-for-ai-safety/) 与 Falcon Guardian 博文为准；本条未核到成熟中文实操片，不编造。

### 5. OpenAI：下一轮 security sprint + Bug Bounty 提奖

官方两页均署 **November 2, 2026**（`@OpenAI` 约北京 **10:29 · 11-03** 发帖）：与 Cathedral Systems 合作，研究员用 OpenAI 模型与内部团队一起找弱点/测修复；叙事接续上一轮约 **25%** 产品工程师用 Codex 查洞，并挂钩 Daybreak「**$10 亿**/六个月」前线防御方补贴。Security Bug Bounty：中/高/严重档中位区间平均逾四倍上调，核心产品严重漏洞最高约 **$30K**，例外严重最高约 **$100K**，叠加质量/忠诚/优先战役加成后最高约 **$172K**；待发奖改用新区间，过去 **30** 天已发奖若新区间更高则补差。**11-20–21** 团队现身 Oakland PROMPT2PWN。

来源：[Preparing our next security sprint](https://openai.com/index/preparing-our-next-security-sprint-to-harden-openai/)、[Rewarding defenders with bigger bug bounties](https://openai.com/index/rewarding-defenders-with-bigger-bug-bounties/)、[X·@OpenAI](https://x.com/OpenAI/status/2117444048227123277)

一边花大钱请人攻自己，一边 CrowdStrike 卖关停键——防御账本今天写得很直白。受益的是独立安全研究员与防御侧工具链；付钱的是把「最高约 $172K」当成常规严重档均值、或把 sprint 计划写成「已证明零事故」的人。标「合作与 sprint 计划 ≠ 已公开漏洞清单；最高约 **$172K** 含加成例外 ≠ 常规严重档均值」。

- 安全研究员：读清 Base / Loyalty / 优先战役乘数，别只看海报最高价。
- 平台安全岗：对照自家 bounty 表，看是否还在用「2023 价」。
- 读者：Cathedral 是合作找洞，不是外包接管平台权限。

教程：以两则 OpenAI 官方页为准；赏金细则以页面表格为准，本条不链未核实的「教你刷 bounty」视频。

### 6. Salesforce 签协议收购 Cresta：语音客服 Agent

官方新闻署 **November 2, 2026**：把「语音优先」客服 Agent 并入 Service Cloud / Agentforce——Cresta 自称语音操作系统：端到端处理复杂来电、实时教练人工坐席、分析每通互动，客户含 Marriott / Comcast / Alaska Airlines。官方**未**披露对价；The Information 报道约 **$2.7B**（对照 Cresta **2022** Series C 估值约 **$1.6B**）。预计 Salesforce **FY2028** 第一季度交割（约 **2027** 年 **2–4** 月），须监管批准；交割后仍支持既有联络中心/电话平台。

来源：[Salesforce News](https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-cresta/)、[The Information·$2.7B](https://www.theinformation.com/briefings/exclusive-salesforce-acquires-startup-cresta-2-7-billion)

大厂用真金白银买「能接电话的 Agent」，不是又发一个演示 demo。受益的是联络中心集成商、实时质检/教练类产品；付钱的是把「签署协议」写成「已交割并替代全人工客服」、或把报道金额当成官方确认条款的人。标「签署协议 ≠ 已交割；报道约 **$2.7B** ≠ 官方确认条款；续支持他厂联络中心 ≠ 已承诺永久多宿主」。

- 客服 / 运营负责人：问清交割前并行支持哪些电话平台，别假设明天就切 Agentforce 全家桶。
- 语音 AI 创业者：Marriott/Comcast 级客户名单说明「复杂来电 + 真人教练」仍是买家要的包。
- 并购观察：金额以官方披露为准，TI 报道先当区间。

教程：以 [Salesforce 新闻稿](https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-cresta/) 为准；本条无已核实的 Cresta 迁移操作片。

### 7. Tutor Intelligence：$75M Series B——仓储机器人「先部署后建模」

a16z 博文署 **November 2, 2026**：约 **$75M** Series B（累计约 **$117M**），a16z 领投，USV 与 Neo 跟投；未披露估值/营收。资金用于机器人基础模型与 Sonny/Cassie 两款仓储物流机器人的制造部署。模式是远程人类「tutor」辅助联网机器人完成拣货/码垛，用真实作业数据回训再向机队推送；客户按小时或按拣付费、无设备买断/无长期合同。自称设施数同比约近 **4×**，目标 **2027** 年底合约机约 **1,000+** 台且美国制造。

来源：[a16z·Investing in Tutor Intelligence](https://a16z.com/announcement/investing-in-tutor-intelligence/)、[The Next Web](https://thenextweb.com/news/tutor-intelligence-75m-series-b-a16z-robot-workers)

同窗韩国 NC AI 还发了面向机器人/工业边缘的 VAETKI Vision **3B** VLM（官方新闻室署 **11-03**，焊接域微调分大幅跳升属公司自报）——一条是「先装进现场再训」，一条是「超轻量视觉底座」。受益的是仓配自动化集成、边缘 VLM 部署商；付钱的是把融资目标机队写成「已无人值守替代全美仓配工人」的人。标「融资与目标机队 ≠ 已披露 ARR 或已全自主；远程 tutor 叙事 ≠ 已无人值守；VAETKI 公司自报三榜/焊接分 ≠ 第三方复现」。

- 物流 / 供应链：按小时/按拣合同先算全成本（含远程 tutor），再比人力。
- 机器人创业：a16z 叙事强调「先部署后建模」——有现场数据比先堆通用大模型更好讲故事。
- 工业视觉：3B 边缘模适合算力受限现场，但先要第三方复现与开放权重口径。

教程：以 [a16z 公告](https://a16z.com/announcement/investing-in-tutor-intelligence/) 与 [NC AI 新闻室](https://nc-ai.com/ko/newsroom/press/nc-ai-3b-sota) 为准；本条不编造未核实的仓配机器人操作片。

### 8. 高盛收紧编码 AI 工具 + Anthropic Message Threads

Bloomberg Law（约 **1:52 PM UTC · 11-02** ≈ 北京 **21:52 · 11-02**）：**10 月**内部指引将 Claude Code 与 GitHub Copilot 系使用范围收至工程师（及兼具量化/交易/工程的 strats），多数交易员与银行家失去此前数月「vibe coding」权限；发言人称实验期后把工具交给「最适合长期使用」的人群。同窗 Anthropic Messages API 公测 **Message Threads**（Release notes 署 **Nov 2**）：长会话/Agent 循环把对话缓存在服务端，官方称多数 Claude Code 用户已默认开启，在约 **500K–1M** token 请求上中位 TTFT 约降 **35%**；计费与 rate limit **不变**；线程闲置约 **5** 分钟过期、最长约 **1** 小时删除。

来源：[Bloomberg Law](https://news.bloomberglaw.com/capital-markets/goldman-restricts-traders-and-bankers-from-using-some-ai-tools)、[Quartz](https://qz.com/goldman-sachs-restricts-ai-coding-tools-traders-bankers-110226)、[Claude·Message threads](https://claude.com/resources/articles/message-threads)、[Docs·Message threads](https://platform.claude.com/docs/en/build-with-claude/message-threads)

一边是华尔街把编码 agent 从「人人可玩」收回工程师岗，一边是 Anthropic 把长会话 TTFT 压下来——**谁能用**和**怎么用得动**同一天更新。受益的是企业 AI 治理顾问、已有工程编制的量化/交易科技团队；付钱的是把「内部指引报道」写成「高盛已全面去 AI」、或把 TTFT 下降写成「账单下降」的人。标「内部指引报道 ≠ 全球统一永久禁令；收口编码工具 ≠ 已下架全部 GS AI Assistant；TTFT 中位降幅 ≠ 账单下降；过期须重放 ≠ 永久服务端记忆」。

- 金融 IT：盘点非工程岗还在用的 Copilot/Claude Code 账号，按新指引收口。
- Agent 开发者：Message Threads 省的是首 token 等待，不是百万 token 单价。
- 管理者：实验期结束要写清「谁保留权限、审计怎么留」。

教程：治理以 Bloomberg / Quartz 报道为准；Threads 以 [官方文档](https://platform.claude.com/docs/en/build-with-claude/message-threads) 为准。本条无已核实的「高盛内部工具」教程（也不该有）。

## 论文研究

### 9. FlashProve + 文本水印：可证明推理与可标记输出

Anthropic Research 署 **November 2, 2026** 发布 FlashProve：开源 zkSNARK「可证明推理」原型——服务方对权重做承诺后，就「该承诺模型确产生了这些输出」给出短证明；评测用 Llama 4 Maverick，单卡 H100 在线证明约 **110 tok/s**，每约 **1,024**-token 请求证明约 **18.78–19 MB**；自承限制含整数化/贪婪解码、上下文至约 **1,024** 等。同窗自 **2026-11-03** 起将文本水印扩到更多既有 Claude（报道点名 Mythos **5**、Opus **4.7/4.6**、Sonnet **4.6** 等）；不可见词选统计模式，**不含**用户或组织标识；检测 API 仍私测，挂钩 EU AI Act Article **50(2)**。

来源：[Anthropic Research·provable inference](https://www.anthropic.com/research/provable-inference)、[Claude Help·How Claude marks AI-generated content](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)、[Mashable SEA](https://sea.mashable.com/tech/56556/anthropic-expands-text-watermarking-to-older-claude-versions-beginning-november-3)

一条在证「跑的是不是那份权重」，一条在标「这段字是不是模型写的」——都是证明权，不是更强聊天。受益的是监管合规、媒体事实核查、需要对外验签的 API 卖方；付钱的是把开源原型写成「Claude 生产流量已默认开证」、或把「检测到水印」写成「可还原始作者」的人。标「开源原型 ≠ 已对 Claude 生产默认开证；检测到水印 ≠ 可还原始作者或全链路 provenance；无水印 ≠ 必非 AI；私测检测 API ≠ 公众可自验」。

- 合规：欧区新模透明度义务与既有模过渡扩标，分开记时间表。
- 平台工程：FlashProve 是密码学路径，公司称已另有签署+信任服务器重算路径达标。
- 内容审核：水印随复制粘贴走，轻编辑后可能仍在——别当法庭级鉴定。

教程：以 [FlashProve 研究页](https://www.anthropic.com/research/provable-inference) 与 [Help Center](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) 为准；本条无面向公众的「一键验水印」成熟教程。

### 10. Stanford Zou 组：LLM 结论的「保质期」

组页署 **November 2, 2026**：复测 **50** 条广被引用的 LLM 结论，跨约 **20** 模（约 **2024-07–2026-09**）。约 **44%**（**22**）判过期（相对效应 ≤ 原效应约 **1/5**）、约 **34%** 减弱、约 **16%** 仍成立、约 **6%** 加强；有过期估计日的样本从发表到过期均值约 **15.7** 月。能力失败类（数草莓字母、假引用、lost-in-the-middle 等）多过期；谄媚/自偏好评委/政治 lean 等偏好类更耐久。假引用案例：原 GPT-3.5 约 **55%** 虚构引用，近期 Sonnet **5.5** / GPT-6.1 Sol 同提示下约 **1%** / **0%**——作者提醒会议「抓假引用」政策可能过时。

来源：[Queen & Zou·The shelf life of LLM findings](https://zou-group.github.io/llm-claims-shelf-life/)

同窗 MIT CSAIL「Weight-Space Programming」博文（署 **Nov 2**，HN 首页热）展示前沿模可无梯度读写小网权重——另一条提醒「能力边界也会被编辑」。合在一起看：**去年论文里的失败模式，今年可能已经不是瓶颈；今年的安全结论，也别假设永远成立。** 受益的是复现工程、评测平台、会更新政策的会议组委；付钱的是把「44% 过期」写成「一切旧安全研究作废」的人。标「**50** 条样本 ≠ 全体 AI 论文；拟合过期 ≠ 单模永久安全；假引用下降 ≠ 已消灭所有幻觉」。

- 研究者：引用 2024 年「模型不会 X」前，先看 Zou 组有没有同类复测。
- 会议 / 期刊：假引用抓手可能要换代，别只靠旧基准 overlapping。
- 读者：保质期是方法论文，不是「AI 已无幻觉」新闻稿。

教程：以 [组页原文](https://zou-group.github.io/llm-claims-shelf-life/) 为准；Weight-Space 旁证见 [Takehi et al. 博文](https://rikiyat.github.io/blog/weight-space-programming/)。本条不编造「复现 50 条」速成片。

## YC 动态

### 11. W27 准时截止已过 + Garry Tan 年花约 $10–20 万 token

YC Apply 文案已改：on-time deadline **was November 2 at 8pm PT**（≈ 北京 **11-03 12:00** 已过），仍接受逾期申请；准时约 **December 11** 前获决定，逾期仍审但不承诺时点；批次 **1–3 月**旧金山线下。截止前 `@ycombinator` 多轮 RT 合伙人催更。另 TechCrunch（约 **4:35 PM PST · 11-02** ≈ 北京 **11-03 08:35**）：YC CEO Garry Tan 在即将上线的 Walter Isaacson 播客中称年花约 **$100K–$200K** 在 agent token；用 agent 做工作/编码/播客备课，开源 **23** 个 Claude Code skill「gstack」；YC 内部 agent「Stray Light」带 company brain；自知属「crazy privilege」，强调个人 agent 要普及「成本必须下来」。

来源：[YC Apply](https://www.ycombinator.com/apply/)、[X·@ycombinator 截止催更链](https://x.com/ycombinator/status/2117392134798229746)、[TechCrunch·Garry Tan](https://techcrunch.com/2026/11/02/y-combinators-garry-tan-uses-ai-agents-so-much-he-spends-up-to-200k-a-year-on-tokens/)

申请窗从「tonight」变成「was… but late OK」；同一天 CEO 把个人 token 账单说到六位数——**使用权的价格**被说得很具体。受益的是仍想交逾期材料的创始人、卖降本路由/skill 包的工具商；付钱的是把截止写成「已停收」或「Demo Day 已开始」、或把个人口述开支写成「YC 财报标配」的人。标「逾期仍审 ≠ 与准时同等承诺时点；个人口述开支 ≠ 公司财报；Stray Light 叙事 ≠ 已开源或对外售卖」。

- 想申请 W27：还能交，但别赌和准时同一批复节奏。
- 创始人 / 重度用户：把 Garry 的数字当上限参照，先算自己任务完成率再加预算。
- 读者：播客引述不是审计账单。

教程：申请以 [YC Apply](https://www.ycombinator.com/apply/) 为准；Garry 访谈以 [TechCrunch](https://techcrunch.com/2026/11/02/y-combinators-garry-tan-uses-ai-agents-so-much-he-spends-up-to-200k-a-year-on-tokens/) 为准。本条不编造申请辅导片。

## 观点洞察

### 能用、能证、能关：Agent 今天写进合同的三道闸

今天几条其实在写同一句话的三个版本：**谁被允许用 Agent，谁能证明它跑的是什么，谁能在它发疯时把它关掉。**

先说**能用**。高盛把 Claude Code / Copilot 系从交易员、银行家桌上收回工程师岗——实验期结束，权限跟着编制走。Garry Tan 另一头说自己年花约 **十到二十万刀** token，还开源一堆 skill；Message Threads 把长会话 TTFT 压约 **35%**，账单却明确说不变。三件事叠在一起：使用权正在从「公司配了账号就能玩」变成「岗位 × 额度 × 延迟」的合同条款。LifeVal 则把「配了就能办成日常琐事」做成自家尺子——和昨天 GDPx 的专家域长时程榜不是同一本账。

再说**能证**。Anthropic 同一窗口放出 FlashProve（证输出确实来自承诺过的那份权重）和文本水印扩标（标这段字像不像模型写的），又在 S-1/A 里写「或将触及」RSI 阈值、同时强调当前未贴超阈标签、不预期完全自主造下一代。Stanford Zou 组补了一刀：约 **44%** 的经典 LLM 结论已经过期，平均保质期大约一年半。证明权不只是密码学和统计水印，还包括**你敢不敢把去年的论文结论写进今年的采购合同**。

最后是**能关**。CrowdStrike 把 AI Kill Switch 做成今日可用的产品名，hooks 点到 Claude Code、Codex、Cursor 等；OpenAI 同步拉高 Bug Bounty、再开一轮和 Cathedral 的 security sprint。Salesforce 花报道约 **$2.7B** 买 Cresta，Tutor 融 **$75M** 继续「人在回路教机器人」——买家要的是可部署、可教练、出了事有人按停，不是无限自治的演示。

所以我自己看材料时会多问三句：

1. **能用：** 这个 Agent 挂在谁的编制和哪条额度池上？非工程岗还有没有权限？
2. **能证：** 出了事能否证明跑的是哪份权重、哪段输出是否带水印/是否可验？引用的「模型不会 X」是不是已经过期？
3. **能关：** Gateway / endpoint 上有没有急停？MCP 和 skills 供应链谁审过？

过得了这三问，再谈 RSI 近阈、LifeVal 高分、Kill Switch 海报也不迟；过不了，再响的招股书数字、再亮的日常任务曲线，都只是还没写进运维手册的功能列表。个人观点，数字以各条原文为准，不构成投资或采购建议。

## 今日机会总结

今天的脊柱是：**治理披露与 Agent 急停**（Anthropic S-1 RSI、CrowdStrike Kill Switch、OpenAI sprint/bounty）、**专用化落地**（Hydrogen-1.0、Cresta 语音、Tutor 仓储机器人）、**使用权与尺子**（高盛收口、Garry 账单、LifeVal、Stanford 保质期），外加 **YC W27 准时窗收口**。观点侧把能用 / 能证 / 能关收成三道闸。

若只选三条可执行方向：

1. **企业 Agent 急停与审计包**：对标 CrowdStrike hooks + Kill Switch 叙事，帮已上 Claude Code/Cursor/Copilot 的中型团队做「盘点 → Gateway 策略 → 审计日志」试点；客户是怕失控扩员的 CISO，不是要「更强模型」的演示买家。
2. **垂直专用化交付**：科学草稿臂（Hydrogen 类开权重 + 专家复核流程）、语音客服教练（Cresta/Service Cloud 叙事）、仓配「人在回路」机器人集成——卖可验收 SLA，不卖「全面替代人工」口号。
3. **评测与结论保质期咨询**：把 LifeVal 日常尺、GDPx 专家尺、以及 Zou 组「结论过期」方法，收成采购侧对账表；客户是怕「去年论文还在 PPT 里、模型已经换代」的采购与风控。

## 普通人今天就能做的 3 件事

1. **公司里已在用 Claude Code / Cursor / Copilot 的人：** 列一张「谁在用、连了哪些 MCP/skills、出问题找谁关」的表；对照 CrowdStrike 今天公开的 hooks 名单，看自己是否完全裸奔。没有 Kill Switch 产品也没关系，先有人为急停流程。
2. **读模型评测 / 写采购材料的人：** 任选一条你还在引用的「模型不会做 X」结论，打开 [Zou 组保质期页](https://zou-group.github.io/llm-claims-shelf-life/) 看同类是否已过期；同时问供应商测的是 LifeVal 式日常还是 GDPx 式专家域。
3. **还想交 YC W27 的人：** 准时截止已过，但 [Apply](https://www.ycombinator.com/apply/) 仍写接受逾期——先交再磨，别再等「完美叙事」。

---

*草稿待审阅；确认后再发博客。有要改的直接说。*
