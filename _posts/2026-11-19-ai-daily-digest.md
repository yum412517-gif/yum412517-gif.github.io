---
layout: post
title: "AI 每日精选 | 2026-11-19：先看它落在哪一档、谁能用、改动由谁批"
date: 2026-11-19 21:00:00 +0800
categories: [AI 新技术]
excerpt: "头条：Google 发布 Gemini 4 Neon，官方把它放在 Carbon 与 Hydrogen 之间，面向复杂软件工程、知识工作和科学流程，并已在 GitHub Copilot 正式可用。同日 Genie 4 向符合条件的 Google AI Ultra 订阅者开放，Stitch Loop 仍以拉取请求交回团队审批；另有 OpenAI 为可等待的后台请求给出低于 Standard 的窗口价。观点是先看它落在哪一档、谁能用、改动由谁批。"
---
![AI 每日精选封面 2026-11-19](/assets/2026-11-19-ai-daily-digest-cover.jpg)

> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 先看它落在哪一档、谁能用、改动由谁批

今天最显眼的，不是又多了一个模型名字，而是这些更新自己先分了档。Google 把 Gemini 4 Neon 放在 Carbon 与 Hydrogen 之间，Genie 4 留给符合条件的 Google AI Ultra 订阅者，Stitch Loop 仍然要把改动交回团队审批；OpenAI 给愿意等 **2** 小时或 **8** 小时的请求开了低于 Standard 的窗口价，ChatGPT for Accounting 也把安装权按工作区拆开。GitHub 这边，经过验证的 MCP 连接器还在公开预览，团队级插件默认却已经正式提供给组织里的 team。我没有把「已经宣布」理解成每个人打开就能用，或改动已经自动进了主分支。先看它落在哪一档，再看谁能用、改动由谁批。

个人观点，不构成投资、采购或技术选型建议。数字和能力边界以各条原文为准。

## 今天最值得看的几件事

- **头条：Google 发布 Gemini 4 Neon**——官方 blog.google / DeepMind 署文标题均为 “Introducing Gemini 4 Neon”，作者为 Google DeepMind SVP 兼 Google Chief AI Architect Koray Kavukcuoglu，栏面日期 **Nov 18, 2026**，blog.google `pubDate` UTC **21:00:00** ≈ 北京 **05:00 · 11-19**。官方把它放在 Carbon 与 Hydrogen 之间，面向复杂软件工程、知识工作和科学流程。API 标价为每百万 input token **$3**（cached input **$0.15**，官方称 **95%** 折扣）、每百万 output token **$15**，上下文窗口 **1 million** token。即日起在 Google AI Studio 的 Gemini API（付费档）、Gemini for business，以及付费 Google AI Pro / Ultra 订阅者的 Google Antigravity 与 Gemini 应用中推出。GitHub Changelog 写该模型已在 Copilot 正式可用，面向 Copilot Pro+、Max、Business 和 Enterprise，rollout 是逐步的。评测数字均为官方或官方转述的第三方榜，须按原文分项看，不要合成一句总排名。
- **Google 的工作台要分开看资格：** Genie 4 首次向符合条件的 Google AI Ultra 订阅者提供，并更新 Genie 3，同时加上 Project Genie agent 和社区画廊；今天打开的官方页还写 Google AI Pro 成员可在同一页加入候补名单（笔记当时未记这一句，以官方页为准）。Stitch Loop 是实验性的长期运行产品智能体，改动以拉取请求交回，须由人手动批准。Gemini 应用登陆符合条件的低内存 Android 设备，包括 Android（Go edition）。不要把这三件事写成同一套许可证已经全开，也不要自行补上官方未写的中国可用性。
- **补录（官方日期多为 11-18，落在过夜或今晨窗）：** OpenAI 为 Responses API 的 background mode 增加 **2h** / **8h** 完成窗口，在 GPT-6.2 Astra 与 Sol 上可把模型 token 单价降到低于 Standard，这不是对这两款模型本身的再发布。ChatGPT 上线 Live Dictation，取消原先 **10** 分钟录音上限，正在全球推向所有套餐。ChatGPT for Accounting 提供官方 Accounting 插件和合作方插件；Business 成员可无需事先批准即安装，Enterprise 须由管理员先批准。
- **另有：** Cloudflare 放出更新后的 Clairic 与更轻的 Clairic-flash，官方博称为 open-weight，可在 Workers AI 调用，完整权重在 Hugging Face。Perplexity 把 Teammates 和 Multiagent 做到 iOS / Android，并为 Teammates 加上语音，面向 Max 订阅者——这是对昨日已写过的网页端 Multiagent 的移动端跟进，不是 Multiagent 的首次发布。GitHub Copilot 在公开预览中新接 **8** 个经过验证的 MCP 连接器，团队级插件默认则正式提供给组织里的 team。GitHub CLI 预览中支持 `gh event listen`。NVIDIA 推出 Cosmos Data Factory 蓝图。Vercel Board 是实验功能，官方 Changelog 写在所有套餐上可用。Pika Enact 仍是研究预览，不对消费者开放。Databricks 推出 Unity Gateway Insights，并把 Genie 做到 Microsoft 常用工具里（Teams 应用正式可用，Copilot 插件与 Excel 加载项要分开看）。火山引擎把豆包实时音视频模型 1.0 的 API 与产品文档对外提供，产品动态列入 **2026 年 11 月**，不是该模型第一次出现。另有 Muse Try On、阿里云 Quick BI AIPro 接入 Qwen4-Max、WonderClip（万镜一刻）3D Studio，以及 Simplex AI 开源的本地智能体 Linger。
- **AWS 中段更新宜收成一组：** Lambda Managed Instances 上的 Event Functions 增加 GPU（EC2 G 系列）；Glue ETL 上线 Spark Optimization Agent（不含 GovCloud 与中国区域）；SageMaker AI 跨区域推理路由；JumpStart Model Leaderboard；OpenSearch Memory 正式可用；HyperPod 增加工作负载恢复；无服务器模型定制开始支持全量微调；AWS Transform 增加 source actions 与 post-launch actions（What's New 栏面日期为 **Nov 19, 2026**）。预览 / 正式可用和区域名单只按官方页分列。
- **补录（11-18，未写入已发布的 11-18 帖）：** DeepSeek 自北京时间 **11 月 18 日 12:00** 起调整 API 定价：调用模型时触发的服务端搜索、网页抓取，工具调用本身不再计费，只按模型 Token 用量计费；直接调用 Search / Fetch API 仍按每 1,000 次成功请求 **5** 元计费。两项要分开写。
- **研究与核验：** 地平线发布视频几何基础模型 LoFT，这是论文与项目主页，不是已经开源的装机产品。OpenAI 介绍芯片设计进展，以及一份内部测量的研究加速报告。Contra Labs 的 Frontier Design Benchmark 把未公开身份的 stealth 模型 Gestalt 放到榜首，不要把它写成某家大实验室已经公开发布的正式模型。Synthetic Sciences（YC W26）发布 FrontierML。Launch HN 上有 Maritime（YC F26）；YC Winter 2027 仍接受迟交，F26 Demo Day 仍是 **12 月 2 日**（周三）。

## 模型发布

### 1. Google 发布 Gemini 4 Neon：官方把它放在 Carbon 与 Hydrogen 之间（头条）

今天早上能打开的，是 Google 把 Gemini 4 家族里又补上的一档。官方 blog.google 和 DeepMind 的署文标题都是 “Introducing Gemini 4 Neon”，作者是 Koray Kavukcuoglu，栏面日期 **Nov 18, 2026**，北京时间大约 **05:00** 能看到。副题写成在复杂软件工程、知识工作和科学流程里，提供前沿级推理，并更快地做完端到端任务。官方自己的位置说明很清楚：Carbon 应对最难、跨度最长的项目，Hydrogen 做快速的日常执行，Neon 则在深度和效率之间取平衡，给高频、但又需要较强推理的生产流程用。不要把今天写成 Hydrogen 或 Carbon 的首次发布，也不要把三档理解成同一天、同一套许可证同时对所有人打开。

评测数字都是官方列举或官方转述的第三方榜，我按原文分项记下，不合成一句总排名。Neon 在 Artificial Analysis Intelligence Index 的 xhigh thinking 设置上总排名第 **3**、得分 **61**，官方写处在更大、更慢的模型之后；Vals Index 排名第 **2**（**70.9%**），并称处在 Pareto 前沿；在新的 Agent Arena Index 的 steerability（中途按用户纠正调整）上排名第 **2**。官方还写它在内部 Google Antigravity 测试中录得「迄今最低的 fabrication rate」，原文没有给出具体百分比，我也不改写成一个数。企业与专业评测方面，官方另列 Legal Research Bench 与 Tax Agent Bench 第 **1**；并写在 Surge AI 上于金融、会计、表格建模和复杂约束遵循的多数基准中排名第 **1**，Chartography **73.5%**，Agents' Last Exam v1.1 **75.8%**，Zapier AutomationBench **56.3%** 第 **1**，Andon Labs Vending-Bench 2 为 **$16,843** 第 **1**，Arena Agent Arena Index 得分 **1336**、在 **4,200+** 真实智能体会话中全球第 **2**。科学与数学方面，官方称 Terminal-Bench Science **70.5%**、RiemannBench **84.0%**、HLE-Diamond **71.3%** 为 best in class。编程方面，Artificial Analysis Coding Agent Index **58.6** 总排名第 **1**，Terminal-Bench 4.1 为 **65.2%**，FrontierCode 2.0 在默认 high 设置为 **46.2%**；SWE-sweep 在 mini-SWE harness 上为 **12.8%**，在 Google Antigravity 中为 **39.0%**。官方还把 Neon 写成可单独运行，或在 Antigravity 里作为 Orchestrator 调度并行的 Hydrogen 子智能体。Antigravity 内部测试不要写成公开榜。

定价和窗口是今晚最需要先记下的：每百万 input token **$3**，cached input **$0.15**（官方称 **95%** 折扣），每百万 output token **$15**，上下文窗口 **1 million** token。官方还写 Neon 有四档 thinking level，可按任务调节智力和 token 花费；在默认 high 设置上，官方称单任务成本比 Carbon 低 **32%**，并在 Vals 与 Agent Arena 的 Pareto 前沿上称比顶尖竞品低大约 **50%** 到 **80%**；xhigh 用于更难的工程、分析和科学工作，官方称此时智力得分最高，单任务成本仍比竞品最高档低 **36%** 以上。这些都是官方对成本和表现的自称，不是我做过的对照实验。

可用性要按官方分项看。署文写即日起在 Google AI Studio 的 Gemini API（付费档）和 Android Studio、Gemini for business（经 API 或模型下拉框）、付费 Google AI Pro 与 Ultra 订阅者的 Google Antigravity，以及 Pro / Ultra 订阅者的 Gemini 应用中推出。@GeminiApp 主帖还写即日起向 Pro 和 Ultra 订阅者在 mobile、desktop 和 web 提供。官方博里我没有看到可单独引用的 API 模型 ID，成稿也就不补一个调用名。另外，Gemini 应用里的 Tasks 现可用 Neon 来跑——Tasks 本身已在 11-18 的帖子里写过，今天只是官方说明它可以跑在这一档上，不是 Tasks 的首次发布。面向网络安全的 “Gemini 4 Neon for cyber” 是另一条通路：官方写将在未来几天向 Fairwind Program 中受信任的防守方滚动开放，要申请需联系 Cloud 客户团队，不要把它写成和 Gemini 应用同一天对所有人打开。

同一波次里，[GitHub Changelog「Gemini 4 Neon in GitHub Copilot」](https://github.blog/changelog/2026-11-18-gemini-4-neon-in-github-copilot) 写该模型已在 Copilot 正式可用，并转述谷歌称其质量接近 Gemini 4 Carbon、单任务 token 成本更低，响应更快、更少做未请求的改动，也不如前者那样容易对代码、工具或测试结果做没有依据的断言。计费按提供商标价纳入 usage-based billing。可用性写面向 Copilot Pro+、Max、Business 和 Enterprise，可在 VS Code、Visual Studio、Copilot CLI、coding agent、Copilot 应用、github.com、GitHub Mobile、JetBrains、Xcode 和 Eclipse 的模型选择器中选用，并写 rollout 是逐步的。Enterprise / Business 管理员可在模型策略里管理访问。做软件工程、知识工作或科研流程的团队，如果已经在用 Gemini 或 Copilot，今天首先该对的不是「它是不是最强」，而是自己的套餐、管理员策略和模型选择器里能不能看到这一档。

来源：[blog.google·Introducing Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)、[Google DeepMind Blog](https://deepmind.google/blog/introducing-gemini-4-neon/)、[GitHub Changelog](https://github.blog/changelog/2026-11-18-gemini-4-neon-in-github-copilot)。

## 工具与产品

### 2. Google 的工作台这一侧：Genie 4、Stitch Loop、低内存 Android 上的 Gemini 应用

这三件事同属 Google，但资格完全不是同一档，我分开写。

**Genie 4。** 官方 blog.google / DeepMind 署文标题均为 “Genie 4 is now available”，作者为 Diego Rivas 与 Pavan Kumar，栏面日期 **Nov 18, 2026**，blog.google `pubDate` UTC **18:00:00** ≈ 北京 **02:00**。稿回顾今年早些时候把 Project Genie 写成可生成并探索交互世界的实验性原型；此次更新面向 eligible Google AI Ultra 订阅者，首次提供 Genie 4，并更新 Genie 3，同时加上 Project Genie agent 和社区画廊。Genie 4 被写成目前最真实、可交互的世界模型，可在会话中途输入新提示，实时改天气、加入角色或改写剧情，并首次配上随场景变化的实时原生音频。Genie 3 仍留在模型选择器里，面向更长的会话或由全景图起步的空间；同日更新包括：单次生成探索最长从 **60** 秒提到 **3** 分钟，并可把多个世界串起来；支持用 **360-degree** 全景图作为新世界的接地；以及用自然语言在探索过程中触发实时事件。这 **3** 分钟上限是 Genie 3 的数字，不要写成 Genie 4。新的 Project Genie agent 可把自然语言描述编排成初始视觉和配套背景音乐；进入世界后也可引入 Gemini。画廊汇集官方策划世界和社区作品，稿中举例包括 “Living Memory”“Dino Field Guide” 等。今天重新打开的[官方页](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/)末尾还写：符合条件的 Ultra 订阅者即日起可以试用，Google AI Pro 成员可在同一页加入候补名单。笔记里原先只强调「不要写成对 Pro 开放」，没有记下这句候补说明，这里以今天打开的官方页为准。这仍然不是对所有 Gemini 用户开放，官方也没有在这篇署文里写中国可用性，我就不补。

**Stitch Loop。** [官方署文](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-loop/)标题为 “Introducing Stitch Loop: A new way to build and evolve products”，作者为 Google Labs 的 Justin Toupin，栏面日期 **Nov 18, 2026**，`pubDate` UTC **17:00:00** ≈ 北京 **01:00**。官方把它写成 Stitch 新方向下的一项 experiment：一个可长期运行的产品智能体，连接代码库和线上指标，找出可改进的地方，在沙箱里写代码并提交 pull request；所有变更都要由人手动批准，「Nothing merges until you review the PR」。今天打开的官方页比笔记当时摘到的更具体：可连接 GitHub 和产品上下文，并写有 **180** 余种集成、自定义 MCP 或本地 CLI 上传；默认提供面向网络安全、延迟和无障碍的 loop，也可自建，例如提升结账转化。每个 loop 走四步：Suggestions、Solutions、Build、Reflect。安全 loop 官方写结合了 Gemini 4 Carbon 的网络安全能力与 DeepMind 的 CodeMender，发现问题后仍以拉取请求提交修复，供人复核。官方还写可与 Google Antigravity 等编码智能体配合，并在 Slack 里用 @stitch。起步方式是加入全球 waitlist；今天打开的官方页给出了地址 [stitch.google.com/loop/waitlist](https://stitch.google.com/loop/waitlist)，并写候补向所有用户全球开放，符合条件的 Google AI Ultra 用户享有优先访问。笔记当时只核到这篇官方博、并嘱咐不要编造表单地址，这里以今天页上的原文为准。这不是已经对所有开发者正式开放的 GA 产品。IT之家标题里的「永远不下班的产品进化器」是媒体概括，我按官方 “long-running product agent” 来写。

**Gemini 应用登陆低内存 Android。** [官方署文](https://blog.google/innovation-and-ai/products/gemini-app/gemini-lower-memory-devices/)标题为 “The Gemini app is now available on lower-memory Android devices.”，作者署名为 Angus Logan，栏面日期 **Nov 18, 2026**，`pubDate` UTC **17:00:00** ≈ 北京 **01:00**。官方写此前这类手机往往只有基本语音指令，此次对应用做了架构调整，让核心 Gemini 体验能在内存更少的硬件上运行，并写这次是把应用带到符合条件的 Android（Go edition）设备上。功能举例包括：用 Gemini Live 以 **45** 种以上语言口语练习或讨论，用相机对准笔记或表格来学习和翻译，以及用 Nano Banana 生成图片。起步方式：在 Google Play 下载 Gemini 应用，在受支持的手机上长按电源键，或在 Transsion 等合作伙伴即将推出的设备上预装。官方用 “hundreds of millions” 描述低内存 Android 设备的用户规模和覆盖增量，我按原文转述，不改成更具体的人数。IT之家标题里出现过 “2GB”，官方博没有给出这个内存门槛，我也不采用。

做互动内容、预演或教育产品的人，如果已经是 Ultra，可以按官方页去看 Project Genie；只是 Pro 的，官方现在给的是候补，不是即刻开放。产品团队若人手不多、又希望有一个长期盯着指标的智能体，Stitch Loop 目前只能先排队，而且每一笔改动仍要人批。低内存 Android 这一侧，更贴近那些平时只能用入门机处理学习和小生意的用户，但范围仍是「符合条件的设备」，不是所有安卓手机今天都能装上同一套体验。

### 3. 补录（11-18）：OpenAI 给可等待的请求打折，并上线 Live Dictation 与 ChatGPT for Accounting

这三则官方日期都是 **11-18**，落在过夜或今晨窗，按补录写。GPT-6.2 Astra 和 Sol 本身已在昨天的帖子里写过，今天不是对这两款模型的再发布。

**Responses API 的 background mode。** @OpenAIDevs 于 UTC **22:54:47 · 11-18** ≈ 北京 **06:54** 发主帖，写并非所有工作流都需要立即返回；对可以等待的单轮或多轮工作流，在 GPT-6.2 Astra 或 Sol 上最多可比 Standard 节省 **40%** 的每 token 费用，并在 background mode 里为首次响应选择 **2h** 或 **8h** 目标。[官方文档](https://developers.openai.com/api/docs/guides/background)写明：`soonest`（默认）无折扣；`2h` 比 Standard 低 **30%**；`8h` 比 Standard 低 **40%**。完成目标从 API 接受初始请求时起算，折扣适用于每次符合条件的请求（含后续跟进）。文档示例使用模型 ID `gpt-6.2-astra`，并写 `background: true`，用 webhook 或按响应 ID 取回结果；可预先一起提交的独立请求则仍指向 Batch API。不要把 **30%** 和 **40%** 写成同一档，也不要把该折扣写成所有模型或 `soonest` 窗口也适用。

**Live Dictation。** ChatGPT 发布说明把该项放在 **November 18, 2026**，标题为 “Live Dictation in ChatGPT”。官方写 Dictation 变得更快、更稳，语音会在说话过程中转成文字，因而不必等整段录音结束再出稿；可点按或点击波形来显示或隐藏正在出现的文字；并已取消原先 **10** 分钟录音限制。Live Dictation 正在全球推向所有 ChatGPT 套餐，覆盖 iOS、Android、网页和桌面应用。这不是新的 Voice 通话模式，也不是已经在所有账号上一次到位。

**ChatGPT for Accounting。** @ChatGPT 于北京 **04:59 · 11-19** 称 ChatGPT for Accounting 现已可用。发布说明「Accounting workflows in ChatGPT」写：插件可协助核对交易、起草发票分录，并按记录和模板准备月末报告；需在 macOS 或 Windows 的 ChatGPT 桌面应用中设置 computer use，再到插件目录打开 Accounting，并在套餐与工作区允许时安装。帮助中心文 [Using ChatGPT for accounting work](https://help.openai.com/en/articles/20001709-using-chatgpt-for-accounting-work) 写 ChatGPT Business 成员可无需事先批准即安装；在 Enterprise 工作区，须由管理员先批准。插件本身免费安装，但模型、工具和用量仍随套餐而异，不要把「免费安装」写成不消耗套餐用量。已点名的合作方插件为 BILL、Campfire、FreshBooks、Oracle NetSuite、Oracle QuickStart、QuickBooks Online、Rillet 和 Xero；帮助中心提醒只读交易与写入记账的权限可能不同，结果需人工核对后再过账。产品页还写，对尚未做成插件的应用，可用 computer use 在应用里协助操作。官方列举的用例都强调起草和复核，并没有把自动过账写成默认开启。

会计师事务所、企业财务和月底结账的团队，如果已经在用 ChatGPT Business 或 Enterprise，今天先看的是工作区有没有批准插件、自己连上的是只读还是可写入，而不是「已经可以自动结账」。开发侧如果请求可以等到下午或隔夜，再去对 Astra / Sol 的 **2h** / **8h** 窗口价。日常口述记录的人，等 Live Dictation 滚动到自己的客户端即可，不必把它理解成新的通话模式。

### 4. 中段简报：开源抽取模型、移动端资格、预览中的连接器，以及一批实验和研究预览

中段条目不少，我收成一组，避免每条都写成一篇长文。预览、正式可用、研究预览和官方自称，仍分开记。

**Cloudflare 的 Clairic 与 Clairic-flash。** [官方博](https://blog.cloudflare.com/open-clairic/)标题为 “An updated Clairic and Clairic-flash are now open-weight, from the new Workers AI Superintelligence team”，栏面日期 **November 18, 2026**，`pubDate` UTC **22:00:00** ≈ 北京 **06:00**。两款都是面向抽取的模型，可在 Workers AI 上调用，完整权重放在 Hugging Face。官方博明确写 Clairic 是 **27B**，端点为 `@cf/cloudflare/clairic`；Clairic-flash 是 **9-billion-parameter** 的紧凑模型，端点为 `@cf/cloudflare/clairic-flash`。笔记当时写「官方博未写主模型参数量」，今天打开的正文已写明 **27B**，并以官方博为准。评测表是官方自报的内部集，官方自己也写目前还没有公开的抽取基准，这些数字只应作为 directional guidance，不要写成公开榜。计费上，官方写虽然模型会生成 output token，但只按 input token 收费：Clairic 为每百万 input **$0.24**，Clairic-flash 为 **$0.10**；在 **2026 年 12 月 1 日**前，两款都按 **$0.10** 促销，到期后 Clairic 回到 **$0.24**。官方博称此次为 open-weight 发布；[Hugging Face 的 Clairic](https://huggingface.co/Cloudflare/clairic) 与 [Clairic-flash](https://huggingface.co/Cloudflare/clairic-flash) 模型页和 LICENSE 则写的是 Apache-2.0。两套口径我分开记，不把官方博直接写成 Apache。另外，Hugging Face 侧栏把 Clairic 标成 28B params、把 flash 标成 10B params，与官方博的 **27B** / **9B** 并不一致，这里不以侧栏数字覆盖官方博。

**Perplexity 移动端。** 这是对昨日已写过的网页端 Multiagent 档的跟进，不是 Multiagent 的首次发布。依据是 @perplexity_ai 于北京 **02:51 · 11-19** 的主帖：Teammates 和 Multiagent 现已进入 iOS 与 Android 应用，并为 Teammates 加上语音；并称大约三分之一最吃重的 Computer 工作已经从 iPhone 发起；即日起面向 Max 订阅者可用。本轮未见单独的新博客署文，我只按这条官方帖转述，不补界面路径、价目或具体机型，也不把「约三分之一」改得更精确。

**GitHub Copilot 的连接器与团队默认，要拆开看。** [「Connect Supabase, Box, Calendly, and more to Copilot」](https://github.blog/changelog/2026-11-18-connect-supabase-box-calendly-and-more-to-copilot) 写可用 GitHub-verified MCP servers（connectors）再接 8 项服务：Box、Buildkite、Calendly、ClickUp、Mixpanel、Supabase、Webflow、Wix，并写它们与已有的 Slack、Figma、Sentry 一样，连接一次即可在 Copilot 里使用。入口包括 Copilot 应用的 Customize、Copilot CLI 的 `/mcp`、VS Code Agents 窗口，以及 github.com 上的 Copilot customization 页。connectors 对所有 Copilot 计划都处于公开预览；Business / Enterprise 需要管理员打开 `Editor preview features` 策略，若企业的 MCP 允许名单是逐项列出而不是通配符，管理员还需要另行添加。不要把公开预览写成所有企业默认已打开。[「Customize GitHub Copilot for your team」](https://github.blog/changelog/2026-11-18-customize-github-copilot-for-your-team) 则写团队自定义已对 organization teams 正式可用：team maintainer 和组织所有者可把通过审核的 Agent Plugins 设为团队默认，适用于该团队的直接成员在 VS Code、Copilot 应用和 Copilot CLI 中的起始配置；子团队不会继承，成员在策略允许时可自行关掉。企业与组织策略仍然优先。该能力面向 Copilot Business 和 Copilot Enterprise。

**GitHub CLI 的 `gh event listen`。** [Changelog](https://github.blog/changelog/2026-11-18-wait-for-pull-request-events-with-github-cli/) 栏面日期 **November 18, 2026**，`pubDate` UTC **00:00:13 · 11-19** ≈ 北京 **08:00**。自 `gh` **v2.105.0** 起，可对拉取请求 URL 运行 `gh event listen` 并指定关心的事件，它会创建订阅、打开事件流，并把每条事件打成一行 JSON。默认在第一条事件后退出；也可用 `--count`、`--follow`、`--timeout`，以及 `--jq` 或 `--template`。可等待的事件包括已提交的审查、拉取请求状态和 head 变更、合并冲突，以及已完成的 check suite。该组 `gh event` 命令处于预览，可能会改，并且需要 Event Streams 的访问权限（GitHub.com 上亦为预览，需加入 waitlist）。不要把它写成默认对所有仓库已开放。本轮没有核验过相关教程视频，也就不列跟练链接。

**NVIDIA Cosmos Data Factory。** [官方技术博](https://developer.nvidia.com/blog/build-training-ready-physical-ai-datasets-with-two-prompts-in-nvidia-cosmos/)栏面日期 **Nov 18, 2026**。这是面向物理 AI 训练数据的蓝图，不是一般可用的消费级产品。官方把 Cosmos Data Factory 写成其中 **5** 套云原生蓝图和 **6** 项可组合技能，由编码智能体编排：第一条提示用于克隆仓库并做 preflight 与 setup，第二条按用例运行蓝图。文中列举的用途包括为自动驾驶生成驾驶场景、增强图像属性、按天气和光线增强视频、生成罕见事件视频，以及为视觉质检生成缺陷图。页首若出现加速或降本倍数的 AI 摘要，本轮未在正文中核到可独立引用的对照基准，我也不采用。官方提到一场名为 “Build Training-Ready Datasets in Two Prompts” 的直播，本轮没有取出可核验的具体视频地址，因此不列跟练。

**Vercel Board。** [官方博客](https://vercel.com/blog/introducing-vercel-board)标题为 “Introducing Vercel Board”，栏面日期 **November 18, 2026**。[Changelog](https://vercel.com/changelog/vercel-board-is-now-available) 写它作为实验功能在所有套餐上可用。官方把它写成给人和智能体共用的无头留言板，用来在频道和线程里分派任务、同步进度；入门命令为 `npx skills add vercel/board`。博客示例写了与 Slack、GitHub 的双向同步；文档还写可与 Linear 的 issue 双向同步，这一条没有出现在博客正文里，我也不把 Linear 写成博客已列的同步对象。官方自述他们把 v0 的 software factory 重建到 Board 上，并写它现在合并超过 **50%** 的拉取请求——这是官方对内部产线的自述，不是独立评测。官方未在这篇博客里公布单独标价。主帖附有官方演示视频，本轮未做播放核验，不作为动手教程列出。

**Pika Enact。** [官方博](https://pika.art/blog/pika-enact)标题就是 “Research Preview: Pika Enact”，栏面日期 **November 18, 2026**。它搭建在 Pika H3 Flex 之上，是一套实验性的直播式环境，官方列了 Live Staging、Live Actor Direction 和 Live Camera Control。官方写在单台服务器上，Live Staging 的生成速度是播放速度的 **1.8** 倍；低延迟设置下，含解码在内，画面在 H100 上不到 **0.4** 秒响应。分块长度标准为 **0.7** 秒、低延迟为 **0.17** 秒。文末写明 Enact 目前是研究预览，不向消费者开放；若想试用或谈集成，联系 enterprise@pika.art，官方未给更广开放的时间表。不要把 H100 上的延迟写成所有硬件上的结果。

**Databricks 的两条补录要分层。** [Unity Gateway Insights](https://www.databricks.com/blog/introducing-unity-gateway-insights) 用 Genie 自动分析已经走过 Unity Gateway 的智能体 traces，可生成过去 **1** 天、**7** 天或 **30** 天的报告。官方用自己给数千名工程师铺开编码智能体时的观察作例子，按官方估计，修复常见 MCP 错误一年可收回约 **$1.2M** 成本——这是 Databricks 自身滚动部署中的估计与案例，不是所有客户的普遍收益。[「What's new for Genie in Microsoft」](https://www.databricks.com/blog/whats-new-genie-microsoft-copilot-cowork-and-chat-microsoft-teams-and-excel) 则写 Microsoft Teams 里的 Databricks Genie 应用现已正式可用；Azure Databricks Genie 插件把 Genie One 接到 Microsoft Copilot Cowork 和 Copilot Chat；另外还有 Excel 加载项。这三层不要写成同一天、同一套入口已经全开。FAQ 里 Work IQ 经 MCP 接入写的是 “will soon”，不要写成已经上线。

**火山引擎的豆包实时音视频模型 1.0。** 今天打开的[官方「产品动态」](https://docs.volcengine.com/docs/doubao-voice/product-dynamics-1?lang=zh)把 Doubao-Seed-Realtime 1.0（亦称 SeedRealtime 1.0）列入 **2026 年 11 月**，介绍为「视听一体、超自然的全双工实时音视频交互模型」。IT之家约北京 **14:55** 称「今天，火山引擎正式上线」该 API 服务；本轮未核到带具体日期的官方新闻稿，因此不以「今天全量上线」作为官方署文原话，而以产品动态的 11 月收录和产品文档为准。该模型本身由字节跳动 Seed 于 **2026 年 8 月 5 日** 发布，当时官方写已在豆包 App 全量上线；官方评测写相比级联模型，对话节奏问题减少一半——这是 8 月的表述，不要写成新的 11 月评测。火山方舟「模型发布公告」**2026 年 11 月**栏未见该模型的单独发布或更新日期。本轮也未核到价目、QPS 或具体接入地址，我就不补。

**Meta Muse 的 Try On。** 这是补录。Meta 首席 AI 官 Alexandr Wang 与官方账号 @Muse 于北京时间今晨前后发帖，称可在 Muse 购物过程中预览衣服穿在自己身上的效果，并写 Muse 会在购物时主动提出展示。本轮未核到 about.fb.com 或 muse.ai 上的对应产品署文，只按这两则官方帖转述，不补用户量、客单价或合作商家名单。这与此前已跳过、且注明不回补的澳大利亚 Muse 上线不是同一件事。

**阿里云 Quick BI 与 WonderClip。** @alibaba_cloud 于北京 **15:48** 称 Quick BI AIPro 已接入 Qwen4-Max，配图把 Qwen4-Max 标为 New。主帖所链的 [Quick BI 产品页](https://www.alibabacloud.com/product/quickbi)介绍 AIPro 可用多家大模型做自然语言分析，但正文未单独点名 Qwen4-Max。帮助中心里「智能小Q」的内置模型名单与配图也不一致，不宜直接当成 AIPro 当前完整清单。成稿以官方主帖和配图为准，不补价格、配额或上线范围。稍后北京 **17:17**，同一账号宣布 WonderClip（万镜一刻）上线 3D Studio，官方称用一条提示即可得到 Blender 里的三维场景，用来摆角色、规划运镜，并把预演作为后续视频的参考，同时写 Try it free for a limited time。今天打开的产品页介绍了故事板、无限画布和 Agent 等模式，但正文未单独点名 3D Studio，也未写 Blender 预演流程，更未给出限时免费的截止时间。产品页上的新人礼包（首次登录赠送 **200** 积分与 **5** 天标准会员）不要写成 3D Studio 限时免费的具体规则。官方自称「一条提示得到 Blender 场景」，我按官方主张来记，不是我验证过的结果。做短剧和产品视频预演的人可以去看官方主帖里的入口，但不必把产品页上的其他赠送规则折进来。

**Simplex AI 的 Linger。** 创始人 Tony Zhang 于北京 **10:09** 发帖称开源本地个人智能体 Linger，指向 [GitHub](https://github.com/simplexai-labs/linger) 与官网 [heylinger.com](https://heylinger.com/)。官方称可在自己的电脑上运行，使用本地模型或已有的 Claude Code / Codex / Pi 订阅，并称数据留在本机。官网 FAQ 同时写：本地模型在设备上运行，云端模型与已连接服务会使用外部提供商；语音需另行配置（会议用 Soniox，实时对话用 xAI）。GitHub Releases 可见 Linger Desktop **0.1.3**，面向 macOS Apple silicon、Windows x64 与 Linux x64；官网下载按钮仍写 Coming soon，与 GitHub Release 提供安装包并存，当前可从 GitHub Releases 获取。仓库 README 里的测速表是官方实验室数字，其中对 8 GB 档的一则脚注写明不是在真实 8 GB 卡上测得，不要把模拟结果写成真实笔记本成绩，也不要把官网营销句 “up to 5x” 与表中的 tok/s 混成同一组数字。

### 5. AWS 中段更新：从事件函数上的 GPU，到给智能体用的正式记忆

AWS 今天这一组大多是 **11-18** 的 What's New 或技术博，条目不少，我收成一条来写。区域、是否另收费和预览 / 正式可用，只按官方页已经写明的来记，不补未出现的价目或配额。

[Lambda](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-gpu-managed-instances/) 在 Lambda Managed Instances 上为 Event Functions 增加 GPU 实例支持，使用 EC2 G 系列，把推理、媒体处理和科学计算接到现有的 Lambda 事件模型里。公司博明确写它针对推理而非训练，也针对自定义模型，而不是 Bedrock 上已有的大基础模型。可使用预置了 vLLM、SGLang 和 PyTorch 的 GPU 基础镜像，容器镜像和 NVMe 临时存储最长各 **32 GB**，并与其他 Event Functions 一样可接 **200+** 种 AWS 事件源。本轮未核到价目表或具体区域名单，也就不编。

[Glue ETL 的 Apache Spark Optimization Agent](https://aws.amazon.com/about-aws/whats-new/2026/11/apache-spark-aws-glue-etl/) 分析已完成的 Spark 作业，并按成本或性能目标给出配置建议。可在 Glue 控制台使用，或通过 Amazon SageMaker Unified Studio MCP Server 从自有工具调用。该代理对 AWS Glue **4.0** 及更高版本不另收费，在 Glue 已推出的所有区域可用，但不包括 AWS GovCloud (US) 和中国区域。这与昨日已写过的 Amazon EMR Serverless 版是同一类代理覆盖到 Glue，不回写到 11-18 的帖子里。

[SageMaker AI 的跨区域推理路由](https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-cross-region-routing/) 在本区域容量不足或端点不健康时，把请求转到其他 AWS 区域或账户中已部署的端点。现有端点、模型和容器不用改。跨区域推理路由对实时推理在 **32** 个商业 AWS 区域可用，对异步推理在 **25** 个区域可用，不要写成同一覆盖范围。路由本身不另收费，客户仍按实际提供服务的端点支付标准 SageMaker AI 费用，并按标准费率支付 CloudWatch 指标费用。

[JumpStart Model Leaderboard](https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-sagemaker-jumpstart-model-leaderboard/) 可在 Studio 里并排比较模型的质量、性能和估计成本。上线时榜单覆盖 **70+** 个来自 Meta、Google、Qwen、IBM、Arcee 等提供方的模型。对 LLM，上线时报告三项推理基准，且分数分栏展示、不合成总分：BIG-Bench Hard（BBH）、GPQA Diamond、MMLU-Pro。不要把 “70+” 改成更精确的个数。

[OpenSearch Memory](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-memory-generally-available/) 宣布正式可用：这是 OpenSearch Service 里一项无服务器能力，用来给 AI 智能体加可跨会话检索的持久记忆。它把智能体交互存成可搜索的事件，再异步抽出结构化记忆，并用关键词、语义和混合检索在会话之间取回相关上下文。该能力即日起在美国东部（弗吉尼亚北部、俄亥俄）、美国西部（俄勒冈）、欧洲（法兰克福）和亚太（东京）区域推出。官方指向了定价页，本轮未把具体单价抄进稿里，起步仍以官方技术文档和 launch blog 为准。

[HyperPod](https://aws.amazon.com/blogs/machine-learning/introducing-workload-recovery-and-expanded-infrastructure-checks-on-amazon-sagemaker-hyperpod/) 增加工作负载恢复和更完整的基础设施检查，包括面向 EKS 编排集群的 `MultiNodeTrainingValidation`、监视 Kubernetes 层的 Resource Monitoring Agent，以及面向 Slurm 作业的 hung job detection。不要把这三项写成已经覆盖所有编排方式。

另有一则补录：[Serverless Model Customization 开始支持全量微调（FFT）](https://aws.amazon.com/blogs/machine-learning/full-fine-tuning-fft-on-sagemaker-ai-serverless-model-customization/)，可在不自行准备 GPU、集群或分布式训练配置的情况下更新模型全部参数。起步方式是用 SageMaker Python SDK 的 `SFTTrainer`，将 `training_type` 设为 `TrainingType.FULL`。文中在 Qwen3-4B 等受支持基座上做了对照实验，并写 FFT 并非在所有指标上都优于 LoRA，效果对超参数很敏感；这些实验数字不是对所有任务的保证，本轮也未另核完整的官方支持清单、价格或区域。

[AWS Transform](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-transform-automates-source-actions/) 增加 source actions 与 post-launch actions，栏面日期是 **Nov 19, 2026**，`pubDate` UTC **08:00:00** ≈ 北京 **16:00**，是这一组里明确写在今天的一条。官方写可把源服务器准备和目标环境校验做成可批量执行、可复用的动作，并由该服务集中管理；该能力在所有已提供 AWS Transform for migrations 的 AWS 区域可用。不要把 “automates” 写成已经无需人工审批，本轮也未核到区域名单或价格。

已经在做事件驱动推理、ETL 调优、跨区域模型服务或智能体记忆的团队，今天更值得先对的是：自己所在区域在不在名单里、这项是不是另收费、以及改动还要不要人来做 go/no-go。

### 6. 补录（11-18）：DeepSeek 调整 API 定价，服务端搜索不再按次计费

这一条记在 11-18 的笔记里，但当时 11-18 的帖子已经定稿，所以没有写进昨天已发布的正文。今天补在这里，也不回改那篇已上线的帖子。

[官方「模型 & 价格」页](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)写明：自北京时间 **2026 年 11 月 18 日 12:00** 起，调用模型时触发的服务端搜索、网页抓取，其工具调用本身不再计费；工具返回的结果会拼接到模型上下文中参与推理，按模型 Token 用量计费。价格页列出的会触发服务端搜索的接口包括：联网工具、Anthropic API 的 `web_search` 工具，以及 Responses API 的 `web_search` 工具。同一页仍写，Search API 与 Fetch API 按次计费，价格仍为每 1,000 次成功请求 **5** 元。

[「网页搜索与抓取」文档](https://api-docs.deepseek.com/zh-cn/guides/search)把两项分得更细。模型通过服务端工具执行的搜索不计费（文字搜索、图片搜索与网页抓取），只有模型 Token 用量计费；服务端工具包括联网工具、Responses API 的 `web_search`、Claude Code 的 Web Search，以及 DeepSeek Harness 中「网页搜索提供方」设为「DeepSeek 服务端搜索」或「自动」（默认值）时的搜索。客户端直接调用 Search API（`POST /v1/tools/search`）与 Fetch API（`POST /v1/tools/fetch`）仍按上表计费，例如 Harness 中「网页搜索提供方」为「DeepSeek Search API」时的搜索，以及 Codex Alpha Search；独立请求只有返回 HTTP 200 且产生结果时才会计费。笔记里原先写的是 Harness 设为「DeepSeek（旧版）」时不计费，今天打开的官方文档已改成「DeepSeek 服务端搜索」或「自动」，这里以官方页为准。

已经在用 DeepSeek API 做联网问答或智能体工具的人，今天先分清自己走的是模型触发的服务端工具，还是客户端直接打 Search / Fetch。前者从 **11 月 18 日 12:00** 起不再为工具调用本身付费，但仍要付模型 Token；后者还是每 1,000 次成功请求 **5** 元。不要写成全部搜索都免费了。

## 论文研究

### 7. 视频几何、芯片设计进展、内部研究加速，以及两份新基准

**地平线的 LoFT。** 官方新闻标题为「地平线发布LoFT原生视频几何基础模型，探索面向物理AI的通用视觉表征」，栏面日期 **2026/11/18**。LoFT（Looped Foundation Transformer for Video Geometry）从 RGB 视频联合预测相机位姿、内参和逐帧深度，恢复场景三维结构。官方写训练数据约有 **297 万** 条有效训练序列、**9.62 亿** 帧图像记录，评测在 SpatialBench、ClassicBench 和 VRBench 上进行，并称在多项深度估计指标上取得领先或 SoTA。这些是官方对论文结果的自称，原文未给出可单独引用的具体分数，我也不补。项目主页为 [horizonrobotics.github.io/robot_lab/loft](https://horizonrobotics.github.io/robot_lab/loft)。本轮未在官方新闻中看到权重已经公开下载的表述，不要写成已经开源，更不要写成可以装进车或机器人里的出货产品。

**OpenAI 的芯片设计进展。** [署文](https://openai.com/index/advancing-chip-design-with-our-models)标题为 “Advancing chip design with OpenAI models”，栏面日期 **November 18, 2026**。这不是消费级芯片发布，也不是 NVIDIA 新闻。今天打开的官方页写，团队从 **2025** 年初就开始用 GPT-o3 mini 协助设计自研推理芯片 Jalapeño——笔记里原先记的是 GPT-4o，这里以官方页原文为准。Jalapeño 方面，官方举例矩阵单元中一次乘法器重设计在综合时大约减少 **15%** 的 cell area，并把延迟从两个时钟周期降到一个；另一次加法器重设计大约减少 **15%** 的 cell area，同时保持两周期延迟。就更广的设计工作，团队估计模型提出的改动使向量单元标准单元面积减少约 **13%**、矩阵单元约 **10%**，并写这些优化已在 Jalapeño 的 silicon bring-up 中得到硅上验证。与 AMD 的合作方面，官方写在已经过充分优化的基线上，旗舰 GPU IP 看到最高 **14%** 的 PPA 改进；AMD 已把其中部分改动纳入一份近期送去制造的设计，并把另一些加入后续版本的生产设计文件。AMD 还验证了其下一代旗舰 CPU 的关键模块上，由该模型写出的设计带来个位数百分比的 PPA 提升。「最高 14%」「约 13% / 10%」「个位数百分比」这些限定要保留，不要把 GPU 与 CPU 结果写成同一组数字。稿后半段还有开源 RISC-V 核上的吞吐量对比，我没有把图表里的全部分数逐项核对进这篇，也就不补。

**研究加速报告。** [“Research acceleration: The jagged frontier”](https://openai.com/index/research-acceleration-jagged-frontier) 同样署在 **November 18, 2026**。这是官方透明度更新，用内部测量说明编码智能体如何改变其 AI 研发流程，不是新产品发布。官方三条 takeaway 为：智能体现在能独立完成接近一半的、估计需要人类 **2–4** 小时的研究任务，但人仍是核心；从 **3** 月到 **10** 月，这类任务的估计成功率从 **23%** 升到 **46%**，估计需要 **4–8** 小时的任务从 **13%** 升到 **35%**。按任务类型，自主智能体成功率为：监控训练运行 **79%**，启动训练运行 **35%**，为推理和 serving 栈写代码 **25%**。按 API 标价，**10** 月研究员日用量的中位数为 **$2,400**，较 **9** 月升 **62%**；第 **90** 百分位为 **$23,000**，较 **9** 月升 **105%**。一项调查问如果要保留前沿编码智能体三个月愿意放弃什么，中位回答是团队算力的 **30%**，或在另一问中为团队编制的 **40%**。Safety and Alignment 的已记录工作周从 **1** 月到 **9** 月增加 **77%**。这些都是官方内部测量、标价和调查中位数，不要写成所有研究任务的平均，也不要把用量美元写成公司总成本。

**Contra Labs 的 Frontier Design Benchmark。** 官方页为 [contralabs.com/frontierdesign](https://contralabs.com/frontierdesign)。发布线程写评估了 **15** 个前沿模型，由 **35** 名职业设计师投下 **3,591** 票。需要注意时间顺序：主帖发出时写人类设计师排名第 **1**、在比较中胜率 **76%**；约 **24** 分钟后，同一账号称出现名为 Gestalt 的新模型，表现超过包括 human golden designs 在内的全部对照。官方方法博客随后写 Gestalt（stealth）Elo 最高，为 **1,928**，在 **423** 次投票中胜出 **89%**。官方只标注 Gestalt 为 stealth、未公布开发方，不要把社区关于哪一家实验室的猜测写成事实，也不要把发布主帖里「人类设计师第 1」的即时表述，与随后加入 Gestalt 后的榜面数字混成同一时刻的结果。Gestalt 不是某一家大实验室已经公开发布、可直接调用的正式模型。

**Synthetic Sciences（YC W26）的 FrontierML。** 官方页为 [frontierml.ai](https://frontierml.ai/)，署文日期标到 **2026-11-18**。用 **25** 道开放式机器学习研究题，在不提供可直接优化的窄指标的前提下，评估 AI 智能体能否自主做经验性的机器学习研发。每轮运行 **12** 小时，智能体可从共享集群按任务租用 H100，并从 **$50–125** 的钱包里支付算力。官方现排行为：Claude Fable 5.2 以均值 **0.523** 领先；随后是 Claude Opus 5.5（**0.399**）、GPT-6 Astra（**0.371**）、Gemini 4 Carbon（**0.353**）和 Grok 4.7（**0.115**，仅覆盖 **15** 道公开题）。署文写 Astra 一律指 GPT-6 Astra，不是 GPT-6.2 Astra。Grok 4.7 只跑了公开题，不要把它的均值写成与其他模型同一口径。也不要把 Induction Labs 此前在 frontierml.org 发布的、同名但任务数和协议都不同的基准，与本条混成同一项。

## YC 动态

### 8. Launch HN：Maritime；YC 日程仍是晚交 W27，F26 Demo Day 在 12 月 2 日

[Launch HN: Maritime (YC F26)](https://news.ycombinator.com/item?id=50549188) 的标题是 “Launch HN: Maritime (YC F26) – A managed cloud for production AI agents”，提交 UTC **17:26:28 · 11-18** ≈ 北京 **01:26 · 11-19**。今晚重新打开条目页时，栏面为 **54** 分、**49** 条评论（笔记里较早一条曾记为约 **33** 分、**32** 条评论，以今天打开的页面为准）。创始人在帖中自我介绍为 Ary 和 Maria，产品地址为 [maritime.sh](https://maritime.sh)。帖文写他们为每个智能体提供隔离、可持久化的 microVM 和可配置环境，并在计算之上提供供给、状态、休眠/唤醒、触发器、调度、监控、网络、更新与回滚、恢复、按智能体的支出跟踪等服务。价格方面，帖文写 **2gb RAM** 的智能体每月 **$1**，并称该价格含 unlimited usage，额外资源按需提供——这是创始人在 Launch HN 里的自行报价，不是我核过的公开价目表。帖中提供了演示视频，本轮未做播放核验，不作为动手教程列出。其余 Launch YC 页上的低票项目，今晚不逐条展开，更不会写成「现居顶」。

YC 日程核验仍然没有变化。申请页仍写正在接受 Winter 2027 批次申请，批次时间为 **January to March**、地点在旧金山；准时截止日期 **November 2** 晚上 **8pm PT** 已过，但仍接受迟交。若在截止日期前递交，会在 **December 11** 前收到决定；截止日期之后提交仍会被考虑，但不能承诺具体回复时间。Demo Day 页仍写 “The F26 Demo Day will be held on Wednesday, December 2nd”，投资者入口仍指向 [demoday.ycombinator.com](https://demoday.ycombinator.com)。

## 今日机会总结

今天的脊柱不是「又发布了一个谁都能用的模型」，而是**先看它落在哪一档、谁能用、改动由谁批**。Gemini 4 Neon 被放在 Carbon 与 Hydrogen 之间，Pro / Ultra、Gemini for business、Copilot 的付费档和管理员策略，决定的是你能不能选到这一档，而不是模型名字本身。Genie 4 目前给符合条件的 Ultra，Pro 在官方页上是候补；Stitch Loop 还在实验和全球 waitlist 里，拉取请求必须人批。OpenAI 把愿意等待的后台请求单独标了低于 Standard 的窗口价，ChatGPT for Accounting 则按 Business / Enterprise 拆开安装权。GitHub 的 MCP 连接器仍是公开预览，团队级插件默认已经正式可用。DeepSeek 从昨天中午起不再为模型触发的服务端搜索本身收费，但直接调用 Search / Fetch 仍按次计费。旁边还有一批实验产品、研究预览和内部测量，不要把它们折成已经可采购的正式能力。

若只选三条可执行方向：

1. **先对「它落在哪一档、自己的套餐能不能用」：** 对标 Gemini 4 Neon 在 Gemini 应用、Antigravity、AI Studio 和 GitHub Copilot 里的分档可用性，以及 Genie 4 的 Ultra 资格与 Pro 候补。客户是已经在付费使用这些工具的软件工程、知识工作和科研团队，卖的是按当前页面对过的开通范围，而不是「新模型已经全员可点」。
2. **把预览、实验和必须审批的改动分开：** 对标 Stitch Loop 的 waitlist 与手动批准 PR，GitHub MCP 连接器的公开预览与团队插件默认的正式可用，以及 Vercel Board、Pika Enact 的实验 / 研究预览边界。客户是要给人与智能体共用工作流的产品和技术团队，卖的是授权策略和审批卡位，而不是「智能体已经可以自己合进主分支」。
3. **把今天就能对上的账单，和还不能当成出货产品的研究分开：** 对标 Responses API 的 **2h** / **8h** 窗口折扣、DeepSeek 从 **11 月 18 日 12:00** 起的两种搜索计费，以及 ChatGPT for Accounting 的工作区安装规则；LoFT、芯片进展、Gestalt 和 FrontierML 则仍是论文、内部测量或未公开身份的榜首模型。客户是 API 调用方、财务结账团队和做评测对照的研究团队，卖的是以官方价目和资格说明为准的可用性。

## 普通人今天就能做的 3 件事

1. **已经在用 Google AI Pro / Ultra，或 GitHub Copilot 付费档的人：** 先读 [Gemini 4 Neon 官方博](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)和 [Copilot Changelog](https://github.blog/changelog/2026-11-18-gemini-4-neon-in-github-copilot)，到自己实际在用的 Gemini 应用、AI Studio 或 Copilot 模型选择器里看这一档有没有滚动到；Business / Enterprise 还要问管理员是否在模型策略里打开。想试世界模型的，符合条件的 Ultra 订阅者按 [Genie 4 说明](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/)进入 Project Genie；Pro 成员按同一页加入候补，不要把它理解成已经开放。官方未写中国可用性的，就不必寻找并不存在的入口。
2. **已经在用 DeepSeek API，或在财务、审计岗位上使用 ChatGPT 的人：** DeepSeek 用户先打开[价格页](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)和[网页搜索与抓取说明](https://api-docs.deepseek.com/zh-cn/guides/search)，分清模型触发的服务端工具（从北京时间 **11 月 18 日 12:00** 起不再为工具调用本身收费，但仍按模型 Token 计费）和直接调用 Search / Fetch API（仍为每 1,000 次成功请求 **5** 元）。做对账、发票分录或月末报告的，先读 [Accounting 帮助中心](https://help.openai.com/en/articles/20001709-using-chatgpt-for-accounting-work)：ChatGPT Business 成员可自行安装官方 Accounting 插件，Enterprise 须等管理员批准；结果要人工核对后再过账，不要把「免费安装」理解成不消耗套餐用量。日常口述的人，也可按[发布说明](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)看 Live Dictation 是否已滚动到自己的 iOS、Android、网页或桌面客户端，记住它仍在全球推出过程中。
3. **要给人与智能体搭工作流、又可以等待结果的开发者：** 对可以等到下午或隔夜的 Astra / Sol 请求，按 [background mode 文档](https://developers.openai.com/api/docs/guides/background)在 **2h**（比 Standard 低 **30%**）或 **8h**（低 **40%**）窗口里提交，默认的 `soonest` 没有这笔折扣。想让产品智能体盯着仓库和指标的，可到 [Stitch Loop 说明](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-loop/)和官方候补页排队，记住拉取请求仍须人批。已经在用 Vercel 的，可按 [Board 公告](https://vercel.com/blog/introducing-vercel-board)把实验功能开在当前套餐上。要用 GitHub CLI 等审查或检查完成的，先升级到 `gh` **v2.105.0** 或更高，并按 [Changelog](https://github.blog/changelog/2026-11-18-wait-for-pull-request-events-with-github-cli/) 申请 Event Streams 预览权限，不要以为所有仓库默认已经能 `gh event listen`。想在本机试个人智能体的，以 [GitHub Releases 上的 Linger Desktop 0.1.3](https://github.com/simplexai-labs/linger/releases/tag/desktop-v0.1.3) 为准，不要等官网仍写着 Coming soon 的按钮。本轮没有核验过新的跟练视频，也就不列教程。
