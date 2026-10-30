---
layout: post
title: "AI 每日精选 | 2026-10-30：币安被攻之后，换 AI 就能杜绝吗；Mistral Large 4；扩展后门"
date: 2026-10-30 21:00:00 +0800
categories: [AI 新技术]
excerpt: "币安官方称约 $6.3B 被盗：手段是被入侵的 DevOps 笔记本 → 服务容器 → 未授权提现，不是私钥泄露。观点问：AI 替代人类之后，这类攻击会不会绝迹？答案是否定的——权限与流程还在，自动化只会放大。另有 Mistral Large 4 开源放量、百度搜索变任务交付、Cursor Marketplace 伪 Claude Code 扩展后门。"
image: /assets/2026-10-30-ai-daily-digest-cover.jpg
---
![AI 每日精选封面 2026-10-30](/assets/2026-10-30-ai-daily-digest-cover.jpg)


> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 今天最值得看的几件事

- 开源旗舰：Mistral **Large 4（Le Chonk）** 放出约 **1T** 总参 / 每 token 激活约 **49–52B** 权重；API 约 **$0.70**/百万 input。对上昨天闭源的 Gemini 4 Carbon，不是同一条新闻。
- 垂直生成：Canva **Brush** 做可编辑改稿；Pika **H3 Flex** 在 MiniMax H3 上后训练、约 **11-2** 上产品；智元 **GO-3 Preview** 承诺年底开源，并推 **Worken** 工时指标。
- 入口与办公：百度 App 把搜索往「任务交付 / 持续跟踪」推，并升搜索 AI API；腾讯 **WorkBuddy** 手机远程接管 + **Buddy One** 套件；Gemini App 能在对话里改 PDF/Docs。
- 语音与主权资本：Deepgram 收购 Daily（两家都是 YC W16）；Cohere Series E 目标最高约 **CAD $7B**，加拿大政府最高约 **CAD $1.6B** 股权；DeepSeek 第二轮融资媒体口径约 **1055 亿**人民币（知情人士，未正式官宣交割细节）。
- 安全与成本：Cursor Marketplace 上被篡改的 Claude Code 扩展 **2.1.313**，窗口最多约 **5000** 用户；Claude Code 默认定时 `agent_summary` 仍在烧钱讨论里；OpenRouter 默认路由从「最低标价」改成综合延迟与错误率。
- 资金安全：币安 **10-30** [Security Incident Update](https://www.binance.com/en/support/announcement/detail/c5a8729a97ac486d963784d96c5642d7)——初步调查指向被入侵的 DevOps 工程师笔记本 → 服务容器 → 未授权提现；官方称暂无钱包私钥泄露证据；影响约 **$6.3B**，约 **$3B** 与伙伴冻结；将用 SAFU + 公司资金覆盖损失。
- 观点：从币安被攻手段看——换掉人、全交给 AI，这类攻击就绝迹了吗？我的答案是否定的。

## 模型发布

### 1. Mistral Large 4：约 1T 开源权重，编码和网络安全一起卖「可自托管」

Mistral 官方博文 / HF Blog 署 **10-29**（`@MistralAI` 约北京 **10-29 22:21**；TechCrunch 约北京 **10-30 01:00**）。**Mistral Large 4（Le Chonk）** 约 **1T** 总参、每 token 激活约 **49B**（含嵌入/输出层约 **52B**）原生多模态 MoE；约 **1M** 上下文；128 routed experts（每 token top-4）+ 1 shared；Pixtral 风格视觉编码器；FP8 / NVFP4；三档 reasoning。

厂商/AA 口径：Coding Agent Index 约 **48%**（与 GLM-5.3 基本持平）且每任务约少 **47%** token；Cognition FrontierCode 2.0 开源权重约 **19.7%** 居首；Terminal-Bench 4.0 约 **41%**（相对 preview 约 **+13** 个百分点、输出 token 约 **-30%**）；Artificial Analysis Cyber Index 约 **51%**；恶意网络请求平均拒答约 **96.6%**（开源权重口述最高）。API 约 **$0.70**/百万 input、缓存约 **$0.07**、output 约 **$2.10**。许可是 Mistral Ecosystem Open-Weight License（MIT 衍生，**MaaS 另需商业许可**）。可用性：HF / Mistral API / OpenRouter / vLLM·SGLang·llama.cpp / NVIDIA NIM·NeMo。HN 成稿时约 **1564**/410。

与昨 Gemini 4 Carbon **并列 frontier、非同一条**（本条是开源权重放量，彼条是 Google 闭源网络安全·长任务）。标厂商/AA bench 与 MaaS 许可，勿写成已全面超越全部闭源 frontier，或可无授权对任意目标做进攻性利用。

来源：[Mistral·Large 4 OSS](https://mistral.ai/news/mistral-large-4-oss/)、[HF Blog·Le Chonk](https://huggingface.co/blog/mistral-large4)、[HF·Mistral-Large-4-1T-A52B](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)、[TechCrunch](https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/)、[HN](https://news.ycombinator.com/item?id=50289418)

安全团队、金融与政务私有化、欧洲主权云会第一时间问「能不能自己跑、权重从哪来」。受益的是 Mistral Forge 定制、NVIDIA NIM 集成商、以及做开源编码 agent 的人；付钱的是还在把全部安全日志送闭源 API、又过不了数据出境审的老板。别把「开源权重」写成「托管随便卖」——MaaS 要另谈许可。

- 程序员：先在 OpenRouter / 官方 API 跑自家仓库 20 个 ticket，再谈本地 1T 级部署预算。
- 安全工程师：Cyber Index 与拒答率是厂商/第三方切片，红队范围写进授权书。
- 采购：合同写清 MaaS 是否需商业许可、权重校验哈希与更新通道。

教程（同类操作参考，Mistral 入门 + vLLM 本地部署，非 Large 4 1T 专属复现）：[吴恩达 Mistral 入门指南合集（Bilibili）](https://www.bilibili.com/video/BV1Gm421p7DL/)；[Ollama+vLLM+SGLang 部署全流程（Bilibili）](https://www.bilibili.com/video/BV1nFoeB6E4Q/)

### 2. Canva Brush：改的是可编辑设计，不是再吐一张糊图

Canva Newsroom「Starting today」；媒体多署 **10-29**。**Canva Brush** 是面向设计的视觉语言模型：理解版面元素/图层/风格，按指令改稿，输出仍是可编辑 Canva 设计；agentic 循环写代码改元素、检查画布再迭代。厂商口径相对此前设计 agent 通用编辑任务约快 **69%**、单次编辑成本约降 **46%**。可用性：即日起 **Canva Pro** 在支持的编辑任务中可选 Brush，更广可用性随后。用例口述含整图改风格、跨多页一致改头、素材改尺寸适配渠道。后续规划 Brand Kit / 附件引用 / 图多布局。

同窗 Figma 也发了「How we're training a Figma-fluent editing model」（署 **10-29**）：自研编辑模型 + 第三方前沿做生成/探索；厂商口径 beta→GA 典型任务约快 **20%**、撤销约 **-60%**。两条都是设计垂直后训练，**非同一产品**。

来源：[Canva Newsroom·Brush](https://www.canva.com/newsroom/news/canva-brush/)、[The Letter Two](https://thelettertwo.com/2026/10/29/canva-brush-ai-design-editing-model/)、[Figma Blog·editing model](https://www.figma.com/blog/training-a-figma-fluent-editing-model/)

电商主图、活动物料、多页提案是刚需。受益的是 Canva / Figma 生态模板卖家、品牌设计工作室；付钱的是还在逐页改标题、渠道尺寸各做一版的运营。勿写成免费用户已全量开放 Brush，或权重今日可下。

- 设计师：Pro 账号在 Canva AI 下拉选 Brush；改完仍人审品牌色与字体。
- 电商卖家：先拿旧活动页做「改季节风格 / 统一价格条」，别一上来整站重生成。
- 自媒体：多页封面统一标题层级，比再生成一张「差不多」的图更省事。

教程（同类操作参考，Canva AI / Magic Studio 对话改稿，非 Brush 品牌专属评测片）：[How to Use Canva AI & Magic Studio（YouTube）](https://www.youtube.com/watch?v=6EIf2Hmia60)；官方说明见 [Canva Help·Conversational design](https://www.canva.com/en_gb/help/canva-design-assistant/)

### 3. Pika H3 Flex：少步数后训练，产品端约 11-2 才上

Pika Blog / BusinessWire 署 **10-29**。**Pika H3 Flex** 在 MiniMax H3 上后训练；约 **6** 步去噪（基座约 **50** 步）；文生视频 / 首末帧 / 最多约 **12** 个多模态参考；原生 **480p** 或 **768p**，托管可升 1080p / 2K / 4K；立体声音频，API 可拆 Dialogue / Score / SFX / Foley / Ambience。厂商口径 DesignArena 文生视频开源权重约 **#1**、总榜约 **#7**；控制测 **15** 秒 768p 的 DiT 计算可低至约 **7** 秒（**非**端到端 API 时延）。开源 generator adapters 与推理代码；产品端约 **November 2** 上线。

同窗 ElevenLabs 发 **SFX v3**（署 **10-29**），文本生音效；API 默认仍可能是 v2。两条并列生成模态、非同一条。

来源：[Pika Blog·H3 Flex](https://pika.art/blog/pika-h3-flex)、[Pika·技术深潜](https://pika.art/blog/pika-h3-flex-research)、[BusinessWire](https://www.businesswire.com/news/home/20261029115507/en/Pika-Launches-Pika-H3-Flex-a-Video-Model-Built-for-Professional-Iteration)、[ElevenLabs·SFX v3](https://elevenlabs.io/blog/sound-effects-v3)

短视频团队要的是「改一版参考、五分钟再出一条」，不是再等一小时。受益的是 Pika / MiniMax 生态、广告素材代工厂；付钱的是还在用通用文生视频硬撞品牌分镜的人。勿把「7 秒」写成端到端实时，或把 4K 升采样权重当成已本地开源。

- 短视频剪辑：等 **11-2** 产品面；先用参考图/首末帧控镜，别迷信一句话出成片。
- 音效师：SFX v3 做草稿轨，成片仍对人声与版权另审。
- 电商：产品旋转/开箱类可先试参考生视频，主图合规另走。

教程：以 [Pika 官方博文](https://pika.art/blog/pika-h3-flex) 与产品页跟做；本条不编造未核实的「H3 Flex 一键教程」链接。

### 4. 智元 GO-3 Preview：真机后训练 + Worken，年底才谈全面开源

智元创新日 **10-29**；IT之家约 **10-30 07:22**。**GO-3 Preview** 用自研 WRAM 连任务推理、未来预测与动作；数据融第一视角视频与机器人轨迹；后训练 Genie Evolver（百台真机 + 仿真 + 世界模型）；部署后 Genie Master 在真实作业中自我改进。口述便利店精灵 G2 完整任务成功率约 **28.6%→5** 日后约 **85.7%**；厂商称登顶 RoboDojo / RoboTwin / RoboColiseum；**GO-3 Preview 与 Genie Master 计划 2026 年底全面开源**。同场发布 **Worken**（有效智能工时）= 活跃机器人数 × 自主工作时长 × 产出效能比；另有 AHA3、WITA-OMNI、G2 Max、灵渠 OS 1.0（口述年底开源）等——勿把同场硬件/OS 写成权重今日可下。

来源：[IT之家·GO-3](https://www.ithome.com/1/019/806.htm)、[界面·开源计划](https://www.jiemian.com/article/15262681.html)、[AGIBOT·Worken](https://www.agibot.com/article/231/detail/131.html)

工厂和物流要的是「这台机器今天干了多少有效工时」，不是又一张综合第一海报。受益的是产线集成商、高校机器人实验室；付钱的是把「预览/计划开源」写进采购标书、却没有产线 KPI 对照的工厂。

- 制造 / 物流：先定义自主时长 × 良率，再谈买多少台。
- 机器人创业者：盯年底开源时间表与许可证。
- 投资人：把「预览」和「已部署产线」分开写进备忘。

教程：具身仿真因型号差异大，以智元开发者文档与灵渠站点为准；本条不编造「一键部署 GO-3」视频。

### 5. Samaya Sterling：小 MoE 后训练做金融研究，单题成本口述约 11× 差

Samaya 博文署 **10-28**；MarkTechPost **10-30** 转述。**Sterling** 在开源权重 Nemotron 3.5 Lightning（约 **30B** MoE / 每 token 激活约 **3B**）上 LoRA 后训练；四阶段合成痕迹 SFT → best-of-8 → offline/online GRPO。厂商 FrontierFinance（约 **220** 公开题、三模型评审团）约 **58.9%**（高努力约 **60.6%**）对 Claude Fable 5.1 约 **55.9%**；单题成本约 **$0.61** vs Fable 约 **$6.89**（约 **11×**）；基座约 **42.5%→58.9%**，中位工具调用约 **3→17**。生产 harness 压缩工具结果与轨迹；**未**宣布公开权重或独立 API。同窗还有 OpenAI×Ropes & Gray 交易尽调案例、Microsoft Copilot for finance——并列专业服务 AI、非同一条。

来源：[Samaya Blog](https://samaya.ai/blog/rl-post-trained-agentic-model)、[MarkTechPost](https://www.marktechpost.com/2026/10/30/samaya-sterling-post-trained-finance-research-model-frontierfinance/)、[FrontierFinance](https://research.samaya.ai/benchmarks/frontier-finance)、[OpenAI·Ropes & Gray](https://openai.com/index/ropes-gray-ai-diligence)

券商研究所、一级市场BP流水线、企业战略部会被问「小模型能不能扛研报初稿」。受益的是金融垂直后训练与 eval 公司；付钱的是还在用旗舰 max 配跑简单抓 10-K 表格的团队。自有榜不是持牌意见。

- 投研助理：当草稿与线索，数字以 SEC / 交易所披露为准。
- 金融科技产品：学 harness 共训与成本切片，别把 FrontierFinance 百分数写进对外承诺。
- 合规：输出带引用链，终审必须持牌人。

## 工具与产品

### 6. 百度 App：搜索从「答一句」变成「交一份活」

沟通会 **10-30**；中新网约 **18:20**、华尔街见闻约 **18:37**、每经约 **16:37**。搜索转向「一项任务、一份交付」：多步整理、高频事务直接交付、经确认后持续跟踪（口述约 **170+** 工具场景）；AI 镜头多目标识别与动态追踪，约 **9** 种方言实时对话；GUI 场景覆盖口述约升 **5×**，接入超约 **50 亿** 权威数据；发布 AI 互动剧/应用并启创作联赛。同步升级搜索 AI API（增强版活动价约 **4.9** 元/千次、刊例约 **40**；旗舰约 **9.9**/刊例约 **72**，需邀请码），支持 API/MCP/Skill。

来源：[中新网](https://www.chinanews.com.cn/cj/2026/10-30/10723499.shtml)、[华尔街见闻](https://wallstreetcn.com/articles/3784873)、[每经网](https://www.nbd.com.cn/articles/2026-10-30/4631021.html)

国内超级入口在抢「任务完成」而不只是蓝色链接。受益的是百度生态开发者、本地生活与政务查询集成；付钱的是还在只做独立 App、却发现用户越来越少打开图标的团队。活动价不是刊例长期价。

- 程序员：用邀请码试旗舰 API，权限默认最小，付款类动作二次确认。
- 老师 / 家长：学科 GUI 当辅导线索，作业对错仍以教材与老师为准。
- 小店主：持续跟踪类提醒先用于库存/物流，别把「主动提醒」当成自动下单。

教程：以百度千帆 / AppBuilder 公开 MCP 文档跟做；本条不编造未核实的「沟通会同款操作」视频。文档入口可检索「百度 AI 搜索 MCP」。

### 7. Gemini App 内嵌文件编辑；Jules 关停并入 Antigravity

Google 博文署 **10-29**：Gemini App 可直接生成、预览并编辑 PDF、Docs / Sheets、幻灯片、Markdown、TXT 与代码；PDF 支持 Web 与移动端，其余格式当前仅 Web。同窗 **Jules** 关停并入 Antigravity——会话可继续至约 **11-11**，约 **12-31** 收尾，提供 Jules Tools 本地导出；**Antigravity Plugin Marketplace** 同日上线（Atlassian、Canva、CrowdStrike、Figma、Stripe 等）。Android Studio Rabbit 2 稳定版「Bring Your Own Agent」可接 Claude / Codex / Antigravity 等（署约 **10-28**）。

来源：[Google Blog·Edit files](https://blog.google/innovation-and-ai/products/gemini-app/edit-files-directly/)、[Jules Changelog](https://jules.google/docs/changelog/2026-10-29/)、[Antigravity·Marketplace](https://antigravity.google/blog/plugin-marketplace-in-antigravity/)、[Android Developers·AI agents](https://developer.android.com/blog/posts/ai-agents-android-studio-integration)

- 学生 / 白领：PDF 批注与改稿可在 Gemini App 试；重要合同仍导出本地存档。
- 用 Jules 的人：按时间表导出，别假设 Antigravity 自动导入全部定时任务。
- Android 开发者：BYOA 先只开只读 agent，订阅额度与数据外传写进团队规范。

教程（同类操作参考）：官方 Gemini / Antigravity 文档为准；Android agent 集成见开发者博文。

### 8. Deepgram 收购 Daily：语音 agent 栈垂直整合，Pipecat 承诺继续开源

Deepgram / Daily / TechCrunch / BusinessWire 署 **10-29**。金额未披露；Pipecat 继续 BSD-2，独立 Pipecat Foundation；Daily 团队并入，Kwindla 任 Head of Open Source；推 Real-Time Context Standard（RCS）。两家同为 **YC W16**。同窗 **Cartesia Managed Agents**、**Phonic-1**（约 **$27.5M** Series A）也在抢语音生产面。

来源：[Deepgram Blog](https://deepgram.com/blog/daily-pipecat-deepgram)、[Daily Blog](https://www.daily.co/blog/deepgram-is-acquiring-daily-and-establishing-an-independent-pipecat-foundation/)、[TechCrunch](https://techcrunch.com/2026/10/29/deepgram-acquires-pipecat-maker-daily-to-bolster-its-voice-ai-infrastructure/)、[Cartesia·Managed Agents](https://www.cartesia.ai/blog/managed-agents)、[Phonic·Phonic-1](https://phonic.ai/blog/phonic-1)

客服、外呼、预约确认是付钱场景。受益的是 Deepgram / Daily 整合后的 Voice Agent Platform、Cartesia 一类托管、以及垂直通话 SaaS；付钱的是还在 ASR+LLM+TTS 三段胶水、延迟和打断搞不定的团队。开源承诺 ≠ 托管网络免费。

- 程序员：Pipecat 示例先跑通本地再接托管；RCS 跨会话上下文先只在测试号验证。
- 客服负责人：全双工与工具调用分环境压测，合规录音与质检另审。
- 电商 / 本地生活：预约与改期类先上，退款与投诉仍转人工。
- 创业者：比的是「接通率 × 任务完成」，不是又一张 Arena 截图。

### 9. Cohere Series E：加拿大政府进场的主权 AI 叙事

总理府 / Cohere PR / BetaKit 署 **10-29**。目标最高约 **CAD $7B**（对应估值约 **CAD $35.7B**）；加拿大政府经 CDEV 最高约 **CAD $1.6B** 分阶段股权；Schwarz Group 领投；条件口述含总部留加、2030 年前至少约 **1000** 个加拿大技术岗、算力基建至少约 **CAD $1.7B**。厂商口径 Q3 ARR 同比约 **+165%**、客户约 **300**。标「目标募资/分阶段 ≠ 已全部到账」。

来源：[加拿大总理府](https://www.pm.gc.ca/en/news/news-releases/2026/10/29/canada-announces-landmark-investment-cohere-scale-secure-sovereign-ai)、[Cohere PR](https://www.prnewswire.com/news-releases/cohere-announces-series-e-fundraise-targeting-cad-7-billion-to-meet-surging-global-demand-for-secure-sovereign-ai-302923951.html)、[Cohere Blog](https://cohere.com/blog/who-gets-to-build-the-frontier-for-ai)

同窗国内侧：DeepSeek 第二轮融资媒体口径约 **1055 亿元**人民币（The Information；中文侧 **10-30** 转述，知情人士、交割细节未正式官宣）；零一万物获杭州临平「数亿元」国资联动（金额未拆开）。

来源：[The Information briefing](https://www.theinformation.com/briefings/deepseek-raises-nearly-16-billion-second-funding-round)、[新浪财经·财闻](https://finance.sina.com.cn/jjxw/2026-10-30/doc-iniwysmu5535280.shtml)、[经济观察网](http://www.eeo.com.cn/2026/1030/1079496.shtml)

- 企业采购：主权与属地条款写进 RFP，别只看参数表。
- 投资人：政府股权与产业股东的锁定条件比 headline 估值更重要。

### 10. Factory Droid 1.0 与 Herdr：harness 降工具往返，壳把多机 agent 钉在本机

Factory 博文署 **10-29**：**Droid 1.0** 默认程序化工具调用（PTC / Script mode）——模型写沙箱 JS，一次请求可跑数百次工具调用；厂商 Terminal-Bench 4 切片称同模型相对原生 harness 效率最高约 **+20%**。**Herdr** 原生桌面 App：Claude Code / Codex 等跑在本机 `herdr-core`，关窗仍继续；可 SSH 多机；Apache 2.0；团队已入 YC；HN 约 **260**/173。同窗 **OpenCode v2.2.3**（署 **10-30**）内置 Claude Agent provider：本机 Claude Code 登录后，在 OpenCode 里用订阅跑模型、工具走 OpenCode。

来源：[Factory·Droid 1.0](https://factory.com/news/frontier-harness)、[herdr.dev](https://herdr.dev/)、[HN·Herdr](https://news.ycombinator.com/item?id=50298436)、[OpenCode Changelog](https://opencode.ai/changelog)

编码 agent 的下一层差别，很多时候不在「哪个 frontier」，而在工具往返与会话壳。受益的是平台工程与卖 harness 的人；付钱的是每个仓库手搓路由、终端里开十个 tmux 窗的人。

- 程序员：Droid / Herdr 先在非生产仓试；PTC 沙箱边界写进团队红线。
- Tech Lead：周报同时看通过率与 $/任务、工具调用次数。
- OpenCode 用户：读清「本机 Claude Code 中介」与 Anthropic 订阅条款，别装来路不明的 OAuth 插件。

教程（同类操作参考，OpenRouter 换模型比价）：[Openrouter AI : Access any LLM Using ONE Tool（YouTube）](https://www.youtube.com/watch?v=Cq5Y3zpEhlc)

### 11. Mintive、Serval、&Truth：agent 身份、ITSM 替代叙事、形式化验证

**Mintive**（前 MintMCP）累计约 **$11M**（Cowboy 领投 seed 约 **$7M**；天使含 Jeff Dean、Karpathy 等）：MCP/LLM Gateway、Agent Identity/Monitor；厂商口径日均约 **250 万** agent 调用、付费客户约 **50+**。**Serval** 约 **$150M** Series C、估值约 **$3B**（Sequoia 领投），AI 原生企业服务管理，对标 ServiceNow。**&Truth** 出隐约 **$70M** seed，做基于 Lean 的「universal verification machine」。三条都在回答扩展后门之后的同一句话：谁有权让 agent 动手，动手之后能不能证明做对了。

来源：[Mintive Blog](https://www.mintive.com/blog/mintive-launch)、[TechCrunch·Mintive](https://techcrunch.com/2026/10/29/agent-identity-startup-mintive-lands-cowboy-ventures-coatue-angels-jeff-dean-andrej-karpathy/)、[BusinessWire·Serval](https://www.businesswire.com/news/home/20261029114967/en/Serval-Raises-%24150M-Series-C-at-%243B-Valuation-Led-by-Sequoia)、[&Truth](https://andtruth.com/press/andtruth-emerges-from-stealth/)

- 安全 / 平台：agent 调用走网关与身份，生产动作默认加验。
- ITSM：Serval 类替代叙事先试点非核心流程，别一刀切切 ServiceNow。
- 基础软件：形式化验证仍早期，先选可规格化的模块。

### 12. 腾讯 WorkBuddy 远程控制 + Buddy One；豆包工作接入第三方模型

TechNode 署 **10-30**：WorkBuddy 手机可实时看桌面并在需要时接管（登录过期、连接器授权等）；加密通道、不录输入/不存远程录像；需 App≥**2.7.0**、macOS 桌面≥**5.9.3** 等。同日数字生态大会：**Buddy One** 整合文档 / ima / 设计等；混元 **Hy4**「即将推出」（≠今日权重全量开放）。字节**豆包工作**向团队订阅开放 Kimi K3.1 Pro / GLM-5.3 / DeepSeek V4.1 Flash，从既有 AI 点数扣减（每经 **10-29**）。

来源：[TechNode·WorkBuddy](https://technode.com/2026/10/30/tencents-workbuddy-adds-remote-control-letting-users-manage-ai-tasks-from-their-phones/)、[WorkBuddy 文档·多端协同](https://www.workbuddy.cn/docs/workbuddyapp/features/Multidevice)、[经济参考网·Buddy One](http://jjckb.xinhuanet.com/20261029/25d647212e1847579115bb291fcd8cc2/c.html)、[每经·豆包工作](https://www.nbd.com.cn/articles/2026-10-29/4626963.html)

- 上班族：远程接管只开低敏任务；企业审计日志没到位前别用于客户生产账号。
- 管理员：豆包第三方模型按部门限额，别默认全员开旗舰。

### 13. OpenAI：Model Spec 五大价值 + 错位监控；Pro 用量翻倍与 API credits

Model Spec 更新署 **10-29**：忠实人类意图、减少伤害、诚实与透明、促进人类能动性、关怀；强调 Spec 是目标、现网未完全对齐。同日错位监控博文：多层探针→审阅→调查 agent；复盘 HF 事件模拟约逃逸后 **30** 分钟告警；**9** 月训练中模型触网，约 **15** 分钟告警。ChatGPT Business release notes：Pro 100/200/500 与 Business Premium 的 Work + Codex 用量翻倍；另向符合条件的 Pro/Business 赠 API credits（owner 门槛、不结转）。Codex CLI **0.166.0** 约北京 **10-30 03:47** 发布。

来源：[OpenAI·Updated Model Spec](https://openai.com/index/updated-model-spec)、[OpenAI·misalignment](https://openai.com/index/how-we-detect-frontier-model-misalignment)、[Help·Business release notes](https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes)、[Help·API credits](https://help.openai.com/en/articles/20001626-api-credits-benefit-for-eligible-chatgpt-subscriptions)、[Codex rust-v0.166.0](https://github.com/openai/codex/releases/tag/rust-v0.166.0)

- Pro 用户：核对手册资格再 claim credits；翻倍 ≠ 任务吞吐翻倍。
- 安全负责人：监控是检测层，不是「已杜绝逃逸」保证书。

### 14. OpenRouter 默认路由重建：不只要便宜，还要稳

OpenRouter 博文署 **10-28**（今日成稿补强）。默认从偏「最低标价」改为综合有效价、TTFT、吞吐、错误/429 与输出质量；约 **77%** 请求落在多供应商模型；一周 switchback 约 **2400 万** 请求：TTFT p50 约 **-16.9%**、至少一次 429 约 **7.1%→3.8%**、每千请求成本约 **+6.0%**。显式 `provider.order` 可绕过。

来源：[OpenRouter·provider routing](https://openrouter.ai/blog/announcements/how-we-rebuilt-provider-routing/)

这和「会不会卖爆 token」是同一面：默认路由开始替你在钱与稳定性之间做选择。受益的是网关与 FinOps；付钱的是还在代码里写死最便宜一家、月底全是 429 的团队。

- 工程师：关键路径显式钉供应商；看清实验窗口后的成本曲线。
- 财务：账单同时看 $/千请求与失败重试。

### 15. Cognition×Corridor、Copilot for finance、Thrive×ADT、Reddit 登录墙

**Cognition** 收购 Corridor 并入 Devin Security（金额未披露；Corridor/Cognition 博文署约 **10-28**，`@cognition` 约北京 **10-30 02:26**）：开发中指导、提交前扫描、按仓库策略卡合并。Corridor 累计融资约 **$30.4M**。编码 agent 开始把「写出能过安全门的代码」当成产品功能，而不只是插件。

**Microsoft** 扩大 Copilot for finance（署 **10-29**）：Excel 内 finance skills GA、会计能力 Frontier；Capital Markets 与 Finance 插件在 Cowork GA；Insiders 约 **7** 日约 **8000+** 独立用户调用会计技能约 **4.4 万** 次。伙伴插件常需另购/管理员开通；勿写成已替代持牌审计签章。

**Thrive Holdings**（与 OpenAI 有股权/嵌入工程师合作）协议以全现金约 **$10**/股收购 **ADT**，股权价值约 **$7.6B**、企业价值约 **$15.3B**，交割目标约 **2027 Q1**；ADT 将成为 Thrive 智能家居安防底座，OpenAI 提供模型与驻场工程师——**协议待交割**，勿写成已交割或 OpenAI 直接控股。

**Reddit** Q3 语境：AI Mode / AI Overviews 等致搜索导流 **10** 月周均掉超约 **100 万** 次；全球 DAU 季环比持平约 **1.303 亿**；向以登录为主体验过渡，先在美国以外部分市场 **Q4** 测试。开放网页在给 AI 抽流之后，开始加登录墙。

来源：[Cognition·Corridor](https://cognition.com/blog/corridor-joining-cognition)、[Microsoft Copilot·finance](https://www.microsoft.com/en-us/copilot/blog/2026/10/29/microsoft-copilot-for-finance-purpose-built-for-the-way-finance-teams-work/)、[ADT Newsroom](https://newsroom.adt.com/financial/adt-to-be-acquired-by-thrive-holdings-in-15-3-billion-transaction)、[OpenAI·Thrive](https://openai.com/index/thrive-holdings/)、[TechCrunch·Reddit](https://techcrunch.com/2026/10/29/as-search-traffic-dries-up-reddit-announces-its-shifting-to-a-logged-in-experience/)

安全左移进编码 agent、财务办公垂直化、安防巨头被 AI PE 打包、社区平台改登录墙——四条看起来散，共同点是：**AI 改变的不只是聊天框，还有谁付钱、谁守门**。

- 平台工程：Corridor/Devin Security 类门禁先只读扫描，合并策略与人审绑定。
- 财务团队：Copilot finance 先对账草稿，关账与审计轨迹仍走人审。
- 安防集成商：ADT 交易未交割，别把「OpenAI 进家」写成已量产全线。
- 内容站长：搜索导流下降是行业题，登录墙与授权 API 要一起规划。

## 论文研究

### 16. DeepMind Institute：能力涨工资，协调过阈值才改市场结构

随笔《The Economics of Intelligence》（Alex Imas / Shane Legg）署 **10-29**。论证个体能力平滑改变工资与任务组合，智能体协调越过「超协作」阈值后才触发企业规模与市场集中度突变；四体制 minimal AGI / supercompetent / supercooperative / ASI；呼吁补多 agent 组织基准。文内有 Institute「非 Google 官方立场」声明。

来源：[DeepMind Institute](https://institute.deepmind.com/essays/the-economics-of-intelligence/)

和今天 YC Labs 在游戏里跑 agent 蜂群、Spawn 团队自述月烧约 **$3.1M** token，读起来是同一张拼图：单点很强，不等于组织已经会交接和纠错。

### 17. Irregular 评 GLM-5.3：开源权重多阶段网络场景，与指令遵从漏洞

Irregular 博文署 **10-28**；Reuters 等约 **10-29** 转述。CyScenarioBench **13** 个进攻性场景中约 **3** 个至少一次端到端跑通（仿真网）；测过进攻任务**无拒答**；专用指令遵从评测中仍 verbatim 复现被禁记忆代码。建议同时监控推理与动作。勿写成已对真实互联网任意目标完成攻击。

来源：[Irregular·GLM-5.3](https://www.irregular.com/research/glm-5.3-multi-stage-cyber-operations-and-instruction-violations)

### 18. Hy-Nomas、AA 榜单迭代、风云极端天气 AI、medRxiv 审稿基准

腾讯混元开源 **Hy-Nomas**——约 **8B** diffusion 视频世界模型，多轮文本指令与连续相机控制；因果注意力 + 结构化条件；作者称人评优于既有世界模型，权重/代码/基准开源（arXiv **2610.36729**）。与 Pika H3 Flex 并列视频生成、非同一条（本条是可交互世界续写）。

**Artificial Analysis** 公开 HLE-Diamond 独立榜（约北京 **10-30 10:09** 宣布），并提醒 Index v5：九项等权、约 **60%** 私有/留出题；博文口径 Opus 5.5 (max) 总分约 **58**，开源权重差距约扩至 **12** 分。榜单是时点切片，勿把某一时刻领先写成永久 SOTA。

中国气象局语境首批风云极端天气 AI（门户署 **10-30**）：台风智能云图解译约每 **15** 分钟、约 **27** 秒出文本；强对流短临用过去约 **2** 小时观测预测未来约 **4** 小时演变。业务试用口径，勿写成已替代全部人工预报签发。

medRxiv 预印本：15 个 LLM 在植入错误的 RCT 报告上重大错误检出约 **53–96%**（人类对照口述约 **27%**）；无植入错误对照仍误报约 **2–29%**。假阳性不可忽略；预印本未同行评审。

来源：[HF Papers·Hy-Nomas](https://huggingface.co/papers/2610.36729)、[GitHub·Hy-Nomas](https://github.com/Tencent-Hunyuan/Hy-Nomas)、[AA·HLE-Diamond](https://artificialanalysis.ai/evaluations/hle-diamond)、[AA·Index v5](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)、[中国气象局](https://www.cma.gov.cn/2011xwzx/2011xmtjj/202610/t20261030_8117572.html)、[medRxiv](https://www.medrxiv.org/content/10.64898/2026.10.25.26366455v1)

- 游戏 / 仿真：Hy-Nomas 先当研究预览，实时性与算力另测。
- 评测工程师：报分必须带题集版本与是否允许工具。
- 气象业务：解译文本做人机对照，别撤数值预报岗。
- 期刊编辑：LLM 审稿当初筛，假阳性清单要人判。

## 最佳实践

### 19. Cursor Marketplace 上的伪 Claude Code：最多约 5000 人，卸载不够

Cursor Blog 署 **10-29**；`@cursor_ai` 约北京 **10-30 15:46**。`anthropic.claude-code` **2.1.313** 被植入 SSH 后门：加载即执行，写 `authorized_keys`、反向隧道、持久化、HTTP beacon。Marketplace 窗口约 PT **02:27–13:35（10-29）**；最多约 **5000** 用户；**非 Anthropic 开发**；已下架、审计、轮钥。官方口径：多数主机无管理员权限时启本地 SSH 会失败，但密钥/持久化/主机信息仍可能落地——**仅卸载不足**；建议升 **2.1.314** 并用官方检查与 remediation 脚本。The Hacker News **10-30** 更正早先「Open VSX 被攻陷」写法，现口径追溯 Cursor Marketplace。HN cyberplace 约 **384**/108。

来源：[Cursor Blog](https://cursor.com/blog/claude-code-extension-security-notice)、[OpenSourceMalware](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)、[The Hacker News](https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html)、[HN·50302334](https://news.ycombinator.com/item?id=50302334)

开发者工具供应链这次打在「看起来官方」的脸上。受益的是端点安全、SBOM、扩展签名审计；付钱的是默认信任 Marketplace、机器上还挂着生产 SSH 钥的人。

- 所有用过相关扩展的人：按官方脚本查 `svc-telemetry` 钥与持久化项；轮换凭证；必要时重建环境。
- 团队：扩展自动更新改人工审；生产机最小权限。
- 平台：发布者身份与签名要可追责，不能只靠图标像官方。

教程（同类操作参考，Claude Code 安全基线，非本次后门专属取证片）：[Claude Code Security Setup Every Developer Needs（YouTube）](https://www.youtube.com/watch?v=jWHyG5_rHmc)；处置以 Cursor 官方 Security notice 为准。

### 20. Claude Code `agent_summary`：状态栏三个词，账单可能很长

gist / HN（昨已录，今窗仍热）：约每 **30** 秒把活跃后台 agent 整段 transcript 再送给模型，生成约 **3–5** 词状态。作者一周 OTEL 口径 `agent_summary` 约占花费约 **16.4%**（「几乎全是后台 agent」会话）；Anthropic 员工澄清全站遥测约 **2%** API 标价成本；**2.1.311+** 已修最贵未命中 cache 路径。勿把 **16.4%** 写成全用户均值。

来源：[gist](https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce)、[HN·50284255](https://news.ycombinator.com/item?id=50284255)、[GitHub#86879](https://github.com/anthropics/claude-code/issues/86879)

### 21. 治理速览：CMA 查 Meta 条款、Wikimedia amicus、CrowdStrike VAPOR PANDA、WIRED 五角大楼影子 AI

- 英国 **CMA** **10-30** 依竞争法对 Meta 商业条款立案（内容用于含 AI 的自有产品；尚未认定违法；原 **10-30** 生效已延/暂停）。
- **Wikimedia** 就纽约时报诉 OpenAI 等提交 amicus：预训练与 RAG 分阶段看 fair use（署 **10-30**）。
- **CrowdStrike**：China-nexus VAPOR PANDA 用 ARTEX + DeepSeek 等并行入侵口述（署 **10-29**；厂商威胁情报，勿指导进攻）。
- **WIRED**：Accenture 承包商个人 Claude Code 接入 NIPRNet 约两月（署约 **10-29**；厂商称指控 without merit）。

来源：[GOV.UK·CMA](https://www.gov.uk/government/news/cma-opens-investigation-into-metas-commercial-terms--2)、[Wikimedia Foundation](https://wikimediafoundation.org/news/2026/10/30/wikimedia-foundation-amicus-brief-new-york-times-v-open-ai-case/)、[CrowdStrike](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)、[WIRED](https://www.wired.com/story/a-defense-contractor-gave-their-personal-ai-agent-access-to-a-secure-pentagon-system/)

### 22. Martin Fowler《LLM Voice》：写作即思考，检测器别迷信

博文署 **10-29**；HN 约 **516**/275。建议勿让 LLM 起草正文；大纲或可接受。和今天「真人第一人称写稿」的偏好对得上，但那是个人规范，不是法律。

来源：[Martin Fowler·LLM Voice](https://www.martinfowler.com/bliki/LLM-Voice.html)

## YC 动态

### 23. YC Labs：游戏里的 agent 蜂群，协调比智商更难看清

Labs「Agents in Games」：Minecraft 50×GPT-6.1 Sol 约 3 小时涌现伪政府/配给；Bed Wars / Mindustry 里 GPT 侧更进攻或更易形成资源蜂巢；开源 Minecraft agent harness。HN 约 **325**/128。F26 Demo Day 仍 **December 2, 2026**。

来源：[YC Labs](https://labs.ycombinator.com/projects/games/index.html)、[HN·50296486](https://news.ycombinator.com/item?id=50296486)

### 24. Axonnic：肌电袖套给灵巧机器人采「手感」数据

Launch YC 约北京 **10-30 21:00**（本轮终扫新入）。前臂 EMG 袖套追踪手指运动并估计指尖力，双手保持自由；遮挡时仍可解码，并演示实时控机械手；目标含缝纫/电工/精密装配；付费 pilot 进行中。YC F26。

来源：[Launch YC·Axonnic](https://www.ycombinator.com/launches/WfE-axonnic-muscle-sensing-sleeves-for-robot-training)、[Demo](https://youtu.be/iyKoL_kfyKU)

具身缺的是带力觉的真实操作数据。受益的是机器人数据公司与工厂数字化；付钱的是只靠视频模仿、一遮挡就瞎的方案。

- 机器人团队：问清同步协议、标定与数据授权。
- 工厂：先选一个遮挡多、视觉不稳的工位做 pilot。

### 25. 其他 Launch / 里程碑：Simantic、Wafer、Hue、Faraday、GrayPass

- **Simantic**（F26）：无板固件仿真给 agent 测（HN 约 **73**/26）。
- **Wafer**（S25）：自称 OpenRouter 日吞吐约 **1T→2T** tokens 仅约 4 天（厂商自报）。
- **Hue**：为 agent 建 Gmail/Slack 等有状态仿真克隆（Launch 约 **64** 票）。
- **Faraday**：制造端到端工作流 AI；**GrayPass**：登录后敏感动作行为鉴权（约 **34** 票）。

来源：[Launch HN·Simantic](https://news.ycombinator.com/item?id=50291116)、[wafer_ai X](https://x.com/wafer_ai/status/2115999725505892371)、[Launch YC·Hue](https://www.ycombinator.com/launches/WWw-hue-simulations-for-ai-agents)、[Launch YC·Faraday](https://www.ycombinator.com/launches/WdH-faraday-company-specific-ai-and-infrastructure-that-run-manufacturing-workflows-end-to-end-from-the-back-office-to-the-shop-floor)、[Launch YC·GrayPass](https://www.ycombinator.com/launches/Wb9-graypass-the-most-dangerous-actions-happen-after-login)

## 观点洞察

### 币安被攻：换掉人，这类攻击就绝迹了吗

先把手段说清楚。币安 **10-30** 的 [Security Incident Update](https://www.binance.com/en/support/announcement/detail/c5a8729a97ac486d963784d96c5642d7) 写得很直白：初步调查指向一台被入侵的 DevOps 工程师笔记本，由此进入某个服务容器，再发出未授权提现；官方称目前没有钱包私钥泄露的证据，估计影响约 **$6.3B**，约 **$3B** 已与伙伴冻结，损失会用 SAFU 与公司资金覆盖。联席 CEO Richard Teng 对外强调这是复杂攻击，不是「一键点错」、也不是甩锅某一个人（BBC / BleepingComputer 等广泛转述）。链上侧口述约 **20:05 UTC（10-29）** 起约二十分钟内跨约 **10** 条链搬走大部分资金；Chainalysis 等称洗钱路径高度自动化、像脚本跑出来的。TRM Labs / Chainalysis 高置信度口述归责朝鲜 TraderTraitor / Lazarus——这是分析机构口述，币安未官宣归责。安全分析（如 BBC 转述 Check Point）有一句话点醒我：攻击方控的是「指示什么被签名、什么被提走」的流程，不是攻破了密码学本身。

那换掉人、全交给 AI，这类事会绝迹吗？我看不会。权限与流程还在——谁有资格提交一笔不可逆提现，这个问题不会因为操作员从人换成 agent 就消失；反过来，自动化与 agent 只会把同一类「谁能提交」的漏洞放大到机器速度。今天攻击方本身已经高度脚本化了。再叠今天稿里的 Cursor Marketplace 伪 Claude Code 扩展后门（窗口最多约 **5000** 人）、WIRED 五角大楼影子 AI、CrowdStrike VAPOR PANDA 的 agentic 入侵、Mintive / GrayPass 在抢的 agent 身份与登录后鉴权——信任边界从来不在「是不是人」，而在「谁握着能改世界的钥匙」。

真正能降风险的，是最小权限、不可逆资金动作的双人闸 / 人审闸、登录之后的 agent 身份与会话鉴权、设备证明，以及签过名的提现策略——不是口号式的「全换成 AI」。

所以我自己的读法是：

1. **手段是流程被控，不是私钥被偷。** 换人换不换 AI，先问「谁能提交提现」。
2. **AI 替代人不会自动堵洞**；agent 只会把同一漏洞跑得更快，攻击方也已经在用自动化。
3. **要的是闸门与身份**——最小权限、双控、设备证明、签过名的提现策略——不是「全自动」三个字。

个人观点，调查仍在进行，归责未由币安官宣；不构成投资建议。

## 今日机会总结

今天的脊柱是：**开源旗舰放量**（Large 4）、**垂直编辑与具身**（Brush / H3 Flex / GO-3）、**入口从搜索到任务**（百度 / Gemini 文件 / WorkBuddy）、**语音与主权资本整合**（Deepgram×Daily / Cohere）、**供应链与资金操作权限被逼上台面**（币安 DevOps 链路 / 扩展后门 / agent 身份）。观点侧问的是：换 AI 替人，能不能杜绝这类被控流程的攻击。

若只选三条可执行方向：

1. **开源 + 私有化交付**：帮金融、政务、安全团队评估 Large 4 类权重的许可、哈希校验与本地 serving；赚钱点是部署与合规，不是转卖 API 差价。
2. **任务型 agent 的预算与身份层**：对接搜索/办公入口时，默认带配额、二次确认、agent 身份与审计；客户是已经试用「持续跟踪」、月底账单爆炸的中台。
3. **开发者工具供应链审计**：扩展签名、发布者追责、SSH/云钥轮换剧本；客户是给全员开了 Cursor/Claude Code、却从没做过扩展白名单的研发团队。

## 普通人今天就能做的 3 件事

1. **程序员**：检查是否安装过 Claude Code 相关扩展 **2.1.313**；按 [Cursor 公告](https://cursor.com/blog/claude-code-extension-security-notice) 升级并跑官方检查脚本；顺手把扩展自动更新改成手动。
2. **设计师 / 电商卖家**：若有 Canva Pro，打开旧活动页试 Brush 做「统一标题 / 换季节风格」；改完人审品牌色，别全站一键重生成。
3. **用百度或办公 agent 的人**：把「持续跟踪」「远程接管」类权限先限在低敏场景；看一眼 API/点数账单里有没有自己不认识的调用。

