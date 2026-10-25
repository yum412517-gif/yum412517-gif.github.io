---
layout: post
title: "AI 每日精选 | 2026-10-25：科技外难见回报，推理层却在数钱——全自动运营还远，责任仍在买方"
date: 2026-10-25 18:00:00 +0800
categories: [AI 新技术]
excerpt: "Kimi K3.1 Pro 登上社区榜；OpenAI 以降价抢企业编码份额；Anthropic 劝你把 subagent 折回单循环；Apollo 说 Mag7 以外没见 AI 财务回报，Deedy 却算开源推理服务商可冲百万美元月营收。另有 Argus 开源 SOC、Axon 警用 AI 记录仪、Elvis 歌词训练诉讼与 YC Paper Club 推理主题。观点里校正：Anthropic Agent 工时约 6:1 不是「AI 开除、全自动运营」，线上事故也几乎不会由模型厂兜底。每条写了我自己的判断：谁受益、谁付钱、普通人能拿来干什么。"
---

> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 今天最值得看的几件事

- 榜与价：Kimi K3.1 Pro 正式发布后一夜登上 Agent Arena / Vals 社区榜；OpenAI 以降价把 Rippling 等企业编码用量从 Anthropic 那边抢回来。
- Harness 往回收、责任仍在买方：Anthropic Applied AI 写清何时把 subagent 折进主循环；Show HN 的 Argus 则把 Agent 调查锁成只读，变更走独立 action broker——能干不等于能背锅。
- ROI 分化：Apollo 说 Mag7 以外几乎看不到 AI 财务回报；Deedy 同时给出开源推理服务商「租卡卖 token」冲到约 $1M/月的经济账——铲子层还在数钱，应用层多数还没赚到。
- 人与版权：Apricitas 旧文今日 HN 高位再上榜，美国创意业四年裁员逾约 20 万但 AI 难单独定量；Authentic Brands 等诉 Anthropic 称训练用了 Elvis 约 274 首歌词（诉状主张）。
- 现场与桌面：Axon Body 5 自称 25× AI 算力、冲突检测仍要人审；YC 的 HeyClicky 公开推 Windows 首版；YC Paper Club 本周盯推理，口径是「训练 1 FLOP / 每年 serving 约 6 FLOP」。

## 模型发布

### 1. Kimi K3.1 Pro：社区榜约第 11 / 第 8，别和厂商自测混着读

正式发布已写进昨稿（约 10-24 凌晨官方博客 / Bloomberg）。过夜社区侧：Agent Arena（页标数据日期 Oct 23, 2026）列 Kimi K3.1 Pro (Max) 约第 11，Net Improvement 约 7.61%±3.00%（约 4,071 sessions），Cost/Task (P50) 约 $1.14，标价约 $2/$10 每百万 token；Vals 模型页写 Release Date Oct 23，Vals Index 约 62.52%（±1.14），榜约第 8/27，Terminal-Bench 4.0 约 63.64%（页称该分榜约第 3/55）。权重仍计划 11-04。

成稿只补这一笔：**厂商自测（昨笔记 Terminal-Bench 等）和 Arena / Vals 社区、第三方榜不是同一套尺子。** 别拿昨稿 65.7% 和今天 Vals 的 63.64% 对打输赢。X 新闻摘要也撮「Arena #11 / Vals 开源权重领先」口径——摘要打折看。
来源：[Agent Arena·Agent](https://arena.ai/leaderboard/agent)、[Vals·Kimi K3.1 Pro](https://www.vals.ai/models/kimi_kimi-k3.1-pro)、[Kimi 技术博客](https://www.kimi.ai/blog/kimi-k3-1-pro)

对国内做 Agent / 编码流水线的团队，意思很简单：榜上有名可以拿去跟采购聊，但选型还是得用自己的回归集。字节豆包、阿里通义、智谱、DeepSeek 开源档继续同台；OpenAI / Anthropic 顶档仍多留给终审。11-04 权重落地后，vLLM / SGLang / 硅基流动一类 Day-0 接新权重的栈会再热闹一轮。

- 程序员：OpenAI 兼容端点先跑自家三个真实任务；对照 Opus / Astra 时别混 harness。
- 产品 / 采购：对外材料分开写「厂商自测」和「Arena / Vals」，避免被质疑口径。
- 自媒体：同一提示词录 Pro vs 上一档，再叠公开 demo，内容够写。

教程（同类操作参考，基于 Kimi OpenAI 兼容接入，非 K3.1 Pro 专属）：[Connect Kimi K3 to Any App!（YouTube）](https://www.youtube.com/watch?v=wTAXn8d28DQ)；另可参考：[How to Use Kimi K3 inside of Claude Code/OpenCode（YouTube）](https://www.youtube.com/watch?v=hjvEJvkEUz0)

## 工具与产品

### 2. Argus（Show HN）：开源、自托管的「Agent 时代」安全运营平台

作者 `@thomasunise` Show HN（约北京 10-25 01:13）+ 同日另帖链官方页（约 05:54，HN 首页约 27 分量级）+ GitHub `thomasunise/argus`：自称 MIT、自托管多租户安全运营平台——采集云/身份/代码/端点/网络/K8s 进证据图；检测含 agent swarm、机器速侦察等。关键设计：**AI Agent 只读调查、不直接改生产**；唯一可变更路径走独立 action broker（策略、审批、dry run、回滚、kill switch）。另含 AI gateway / shadow-AI 发现、沙箱攻击演练、可授权范围内自主渗透测试等。支持 Claude / OpenAI / 本机 Ollama，或无模型时回退确定性逻辑；Docker / Helm / Terraform。官方强调自主响应与渗透默认关闭，需部署开关 + 租户 opt-in。

这是早期基础仓，不是认证合规产品，得按环境调优。可与下面 Anthropic「单 Agent 循环」对照：一边简化 harness，一边把「能动手」从调查 Agent 里拆出去。
来源：[HN·Show HN Argus](https://news.ycombinator.com/item?id=50223201)、[HN·Argus 首页帖](https://news.ycombinator.com/item?id=50225748)、[GitHub·thomasunise/argus](https://github.com/thomasunise/argus)、[官方页](https://thomasunise.com/argus)

谁会买账？已经上了云 + 身份 + K8s、又怕 Agent 直接改生产的中小安全团队；做 MSSP / SOC 外包的公司可以把「只读调查 + broker 审批」当交付话术。国内奇安信、深信服、长亭一类会继续被客户拿来问「你们有没有 Agent 只读模式」；国外 Splunk / Elastic / CrowdStrike 叙事压力在「调查能不能交给 Agent、变更能不能拦」。

- 安全工程师：先 Docker 起仓，默认关掉自主响应与渗透；只读调查跑通再谈 broker。
- 架构师：把「证据图」和「变更路径」分仓分权限，别塞进同一个 service account。
- 小团队老板：这不是买完就能过等保的盒子，当脚手架看。

教程（同类操作参考，开源 AI SOC 分析师，非 Argus 专属）：[Open-Source AI SOC Analyst That Actually Works — Meet Talon（YouTube）](https://www.youtube.com/watch?v=5xDRfyrWoSA)

### 3. Axon Body 5 / Guardian：警用记录仪自称 25× AI，冲突检测仍需人审

官方新闻稿（datePublished 约 10-24 17:06 UTC ≈ 北京 10-25 01:06）：宣布 Axon Body 5 与 Body 5 Pro，自称相对前代约 **25× AI 处理能力**、低光更好、续航约 +20%。Pro 另加近焦扫驾照、前置扬声器（配合 Axon Assistant 实时翻译）与更大内存。配套 **Axon Guardian**（AI Era Plan 内新类）：Body 4/5 录音中可做 Escalation Detection（口头冲突升温告警进 Axon Fusus，**人工审直播再决定**是否增援）；Fleet 3 车载可做 Approach Alert（停驶车辆开门告警）。另提 Draft One（录像音频→报告草稿）。通用上市日未定。

成稿必须写清：这是「人审 + 告警」，不是无人自主执法。Ethics & Equity Advisory Council 口径在官方稿里也有。
来源：[Axon 官方新闻稿](https://www.axon.com/newsroom/press-releases/axon-announces-body-5)、[投资者稿](https://investor.axon.com/2026-10-24-Axon-Announces-Body-5-Next-Generation-Camera-Built-for-the-AI-Era)

公共安全硬件/现场 AI 的钱，最终来自警局预算与「AI Era」订阅。Motorola Solutions、国内海康/大华公安线、以及做笔录自动化的软件商会跟；公民社会与合规律师会盯「告警误报 → 增援」的问责链。企业安防（零售、医院、酒店）是 Axon 自己点名的第二战场。

- 公共安全信息化：试点先写「人审直播」SOP，别写成自动派警。
- 产品经理：Draft One 类报告草稿有市场，但必须保留原音与人工改稿痕迹。
- 普通人：当治理信号看——现场 AI 越强，越要问谁对误报负责。

教程（同类操作参考，警用记录仪 AI 辅助审片，非 Body 5 / Guardian 专属产品教程）：[Avon Police using AI to help review body camera footage（YouTube）](https://www.youtube.com/watch?v=nr6J3yqHeLI)

### 4. OpenAI 降价抢企业编码份额：Rippling CEO 的用量翻转

Benzinga 转载 The Information（Laura Bratton；约 10-24 10:00 EDT ≈ 北京 22:00，落过夜窗）+ Subvolts 摘要：Rippling CEO Parker Conrad 称，五月 Anthropic 约占数百工程师编码任务约 57%、OpenAI 约 16%；至十月为压成本后约 OpenAI 52% / Anthropic 18%。叙事强调 OpenAI 以更低价抢份额。X 新闻摘要另撮 Replit 在约 30% 折扣后大额转向 OpenAI——**成稿以 The Information / Benzinga 引 Conrad 数字为准，Replit 细节勿超出已核实二报。**

这是企业采购/定价竞争二报，不是新模型。可与 Anthropic 单 Agent 指南对照：一边在抢座位，一边在教客户把 harness 变简单、把账单压下来。
来源：[Benzinga·The Information](https://www.benzinga.com/content/62577789/anthropic-s-margin-openai-s-opportunity)、[Subvolts 摘要](https://subvolts.com/anthropic/web/trade/anthropics-margin-is-openais-opportunity-924760/)

谁受益？短期是 OpenAI 企业编码席位与愿意换供应商的工程组织；谁付钱？Rippling 这类「几百工程师同时开 Agent」的公司，以及 Cursor / Claude Code / Codex 生态里被卷进比价的团队。国内阿里云百炼、字节火山、月之暗面 API 会继续用「同任务更便宜」打同类标书。Anthropic 若守质量溢价，得证明多付的那截钱换来了更少返工——否则 CFO 只看单价。

- 工程经理：按任务类型拆账（草稿 / 终审 / 长跑 Agent），别整仓绑死一家。
- 程序员：同一任务在 Claude Code / Cursor / Codex 上各跑一遍，记时间和返工次数，比记官价有用。
- 采购：合同写清折扣档位与锁定期，避免「便宜三个月再涨回来」。

教程（同类操作参考，三家编码 Agent 同任务对比，非 Rippling 采购案专属）：[Cursor vs Claude Code vs Codex（I Built the Same App 3 Times）（YouTube）](https://www.youtube.com/watch?v=OnCep-HlMzI)

## 论文研究

### 5. arXiv:2610.29162——为什么 AI 生成的语言这么难懂？

NYU / UT Austin（Thomas Hikaru Clark、Matias B. Martin、Kyle Mahowald）。HN（约北京 10-25 02:04 上榜，晚间仍约 198 分 / 169 评量级）热议。对照 14 个前后沿模型（文中含 Claude Opus 5/5.5、GPT-5.6 系、Kimi K2.5、GLM 5、Olmo/Llama 等）在聊天/编码/议论文设定下的输出，相对回译 paraphrase 与人类基线：多数模型更常用未登录 bigram、低频率 n-gram、无生命主语+有生命动词、去关系词的宾语关系从句等与人类加工难度相关的特征。作者假设 math/code/reasoning 的可验证奖励与上下文压缩压力弱化了「可懂」目标，并以 Qwen2.5-1.5B + 长度惩罚 GRPO 做机制旁证。

注：文中对照模型名属论文实验设定；**勿外推未写明的产品结论。**
来源：[arXiv:2610.29162](https://arxiv.org/abs/2610.29162)、[HN](https://news.ycombinator.com/item?id=50223647)

对做 ToC 产品、客服话术、公文写作、教育辅导的团队，这是提醒：榜分涨了，读者读起来未必更轻松。Grammarly、Notion AI、国内的秘塔 / 通义公文类，可以把「可读性」写进 eval，而不只盯 BLEU / 任务成功率。内容工厂若只用模型出稿再人改，返工成本往往藏在「读不懂」里。

- 产品经理：给生成文案加一道「人类可读」抽样，比再堆形容词有用。
- 自媒体 / 编辑：AI 初稿先过「删掉空话、拆开长句」的人工关。
- 研究者：长度惩罚与可懂性的权衡值得跟，别只追 reasoning 分。

教程（同类操作参考，AI 文风/「AI slop」识别与规避，非该论文复现）：[Why AI Slop is So Bad (And How to Prevent It)（YouTube）](https://www.youtube.com/watch?v=K5zsgZwEqZE)

## 最佳实践

### 6. Anthropic Applied AI：何时把 subagent 折回主 Agent 单循环

官方文《Building agents: When to fold subagents into your main agent loop》（社区/二报多记约 10-22；本日 X 摘要反复再热）。要点：多企业部署里，单 Agent + skills / 工具渐进披露常在质量上优于「一提示打天下」与多 subagent，且时延/成本更低；一例客户单循环约 2× 快于多 Agent harness；Claude Code 在更强模型上把系统提示砍逾约 80%。仍保留 subagent 的情形：上下文膨胀可测、需并行且可丢弃上下文、工具选择冲突。配套 GitHub `anthropics/single-agent-loop-kit`（参考实现，README 称非长期维护）与 `/claude-api` 相关 skills。

可与 Argus「只读调查」和 Rippling 编码份额同读：客户既要更便宜，也要更简单；多 Agent 编排若只是复制组织架构图，账单和延迟会一起涨。
来源：[Anthropic 官方文](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop)、[GitHub·single-agent-loop-kit](https://github.com/anthropics/single-agent-loop-kit)

生意在「帮企业做 harness 减肥」：审计现有 subagent 清单、合并技能、补端到端 eval。付钱的是已经堆了几十个「部门专属 Agent」、却抱怨慢和贵的中台。LangGraph / CrewAI / 国内 Dify 多 Agent 模板的实施商，要准备「何时不该拆」的咨询话术，而不只卖「再加一个 Agent」。

- 程序员：先建 10 条端到端黄金例，再决定折哪个 subagent；折一个测一次。
- 架构师：中央小组守系统提示与总 eval，各业务队改 skills / 工具，别人人改总提示。
- 小团队：默认单循环 + 少量工具；并行研究、可丢弃上下文再上 subagent。

教程（同类操作参考，Anthropic 官方谈如何把 Agent 建得更有效；另附社区 masterclass）：[Building more effective AI agents（YouTube·Anthropic）](https://www.youtube.com/watch?v=uhJJgc-0iTQ)；[Claude Agents Tutorial: Free 2-Hour Masterclass by Anthropic（YouTube）](https://www.youtube.com/watch?v=OZ9NhFwVCtQ)

### 7. Apollo Torsten Slok：科技业以外未见 AI 财务回报

Apollo《The Daily Spark》（署 October 24, 2026）+ HN（约北京 10-25 03:47 上榜，晚间仍约 551 分 / 574 评量级）：称 Mag 7 人均营收与利润率上升，而 S&P 493 两项走平；调整后全要素生产率仍未见 AI 拉动；主流企业开始把 token 开支视作侵蚀利润的成本中心而非增长源；VC 公司 token 支出仍升，但宏观影响在 Agent/token 局限于经济一小块时仍有限。结论：AI 故事取决于 S&P 493 而非 Mag 7，目前科技外尚无营收/利润改善证据。

属宏观评论/图表分析。可与下条 Deedy「推理服务商冲 $1M/月」对照写「铲子 vs 应用 ROI」。
来源：[Apollo·Daily Spark](https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector)、[HN](https://news.ycombinator.com/item?id=50224463)

对 CFO、咨询公司、ERP/行业软件商，这是冷水：演示很炫不等于利润表动了。麦肯锡、埃森哲、国内的汉得 / 中软实施项目，会被董事会多问一句「去掉 Mag7 之后呢」。卖 GPU 与云的英伟达、微软、亚马逊、谷歌短期仍吃铲子红利；卖「行业 Agent」的创业公司，要准备用可审计的成本中心叙事，而不是增长叙事。

- 企业数字化负责人：试点写清基线（单任务成本、返工率、周期），90 天复测，别只报「节省小时数」。
- 投资人：分清基础设施收入和应用层利润，别用 Mag7 估值逻辑套传统行业。
- 普通人：听到「全面赋能」先问利润表哪一行变了。

教程（同类操作参考，如何度量企业 AI ROI，非 Apollo 报告解读）：[AI ROI Measurement | Proving the Business Value of Artificial Intelligence（YouTube）](https://www.youtube.com/watch?v=iCRP1aeqqt0)

### 8. Apricitas：美国创意产业四年裁员逾约 20 万——AI 难单独定量

Joseph Politano 文《AI and the Fall? of the Creative Class》（Substack 署 **2026-09-27**；HN 约北京 10-25 07:11 上榜，晚间仍约 358 分 / 352 评、首页前列）。称美国「创意」相关行业四年累计减员逾约 20 万、近一年约 5 万量级；电影/影视与录音等子行业合计减员逾约 10 万（约近三分之一）。作者强调无法把 AI 与好莱坞整合、离岸制作、流媒体/社媒分流等拆开；同时指出线下演出仍在增、数字创意多数子板块同向下滑，故 AI 影响「难以排除」。文中亦提 Anthropic 少做影音生成、OpenAI 曾放弃 Sora 类视频平台等口径——**以一手文章为准。**

属宏观就业评论再上榜，不是今日新品。
来源：[Apricitas 原文](https://www.apricitas.io/p/ai-and-the-fall-of-the-creative-class)、[HN](https://news.ycombinator.com/item?id=50226419)

对影视后期、广告制作、游戏外包、唱片周边的人，这不是「AI 杀死创意」的判决书，而是「结构性收缩 + 技术替代叠在一起、账很难分」。Midjourney、Runway、Pika、可灵、即梦会继续吃工具订阅；工会、劳务派遣与教培会吃「转岗/人机协作」课。国内短视频与游戏美术外包已经历过一轮降本，逻辑类似。

- 创意从业者：把「会提示词」当成基础技能，真正溢价仍在审美、叙事与客户沟通。
- 工作室老板：用 AI 砍的是重复初稿与变体，不是客户关系；裁员叙事对外要诚实。
- 自媒体：写就业话题时把作者「难以定量」写进去，别写成单因果。

教程（同类操作参考，创意工作如何随 AI 变化，非 Apricitas 数据课）：[AI In Creativity: Krea's Founder On How Work Changes（YouTube·Forbes）](https://www.youtube.com/watch?v=NEBqKKfe-RM)

### 9. Deedy Das：开源推理服务商可快速冲到约 $1M/月

`@deedydas`（Menlo）原帖（约北京 10-25 11:20；本日早间漏收后补录）。称大量 inference provider 以极低门槛冲到约 $1M/月：即便按需租 B300 约 $8/GPU-hr，GLM 5.3 / Kimi K3 / DeepSeek 4.1 Flash·Pro 等开源模型在约 100 tok/s 吞吐下可做到约 $10–20+/GPU-hr；并引 DeepSeek DeepInfer 自称 off-peak 约 $38/GPU-hr。毛利取决于利用率与推理栈；OpenRouter / Vercel 等网关聚合需求；中文开源实验室规模化后或要求收入分成/预发布权。门槛低到可「vibe code」起仓，每周数十家冒头、以偏低毛利冲营收再融资。风险：开源模型是否持续有竞争力、实验室是否加租、芯片形态变化、算力短缺时谁拿得到卡。点名增长激进的新玩家 inference.net / DeepInfra / Wafer / Relace / Morph，以及 Crusoe / CoreWeave / Nebius / GMI 等 neocloud 自做推理，与 Modal / Fireworks / Baseten 对照。

属投资人市场观察/经济账，**数字以 Deedy 原帖为准，勿外推未核实营收。** 可与 Apollo「科技外无回报」对照：铲子层（卡、推理、网关）仍在讲增长故事，应用层多数还在成本中心。
来源：[Deedy X](https://x.com/deedydas/status/2114195317860266432)

谁受益？会调 vLLM/SGLang、拿得到卡、能把利用率做上去的小团队；谁付钱？所有用开源模型 API 的应用方，以及被网关抽成的流量。国内硅基流动、DeepSeek 官方推理、阿里云 / 火山引擎的「开源模型托管」会继续卷单价；Fireworks、Together、Baseten 要防「低毛利冲量再融资」的新玩家。

- 有 GPU 资源的程序员：先算清楚 GPU-hr 成本与 token 售价，利用率低于某线就别硬开公有推理。
- 创业者：网关（OpenRouter 类）是获客捷径，也是毛利杀手；大客户尽量直连。
- 应用团队：多备两家 provider，模型实验室一加租你就被挤。

教程（同类操作参考，用 vLLM 起 OpenAI 兼容推理服务，非某一家 provider 专属）：[Serve LLMs Locally in Python: vLLM with an OpenAI-Compatible API（YouTube）](https://www.youtube.com/watch?v=1GlQJnwzDJw)；深入一点：[Understanding vLLM with a Hands On Demo（YouTube）](https://www.youtube.com/watch?v=qdPkA5mxLhg)

### 10. Authentic Brands 等诉 Anthropic：称 Claude 训练用了 Elvis 约 274 首歌词

Billboard 首报 + Rolling Stone / Hollywood Reporter 跟进（起诉约 **Friday Oct 23**；THR 署约 10-24 19:22 ET ≈ 北京 10-25 07:22；本日晚间 HN newest 约 1 分上榜）。原告含 Authentic Brands 旗下 ABG EPE IP 等，案号报道为 ABG EPE IP LLC et al. v. Anthropic PBC（北加州）；称未经许可将「Can't Help Falling in Love」「Don't Be Cruel」「A Little Less Conversation」等约 274 首歌词纳入训练，并指 Claude 在加护栏后仍会「为现代听众」改写且结构/钩子接近原作。报道口径：法定赔偿按每首最高约 $150,000 计约 **$41.1M**，另加规避技术保护与剥离版权管理信息等主张，合计报道约 **$48.6M** 量级；另求永久禁令、陪审团审理、训练数据与抓取说明，以及销毁训练库/权重/服务器上的未授权副本。同律师团队此前亦有 Reservoir 等诉。

**以上均为诉状主张；Anthropic 公开回应待核，勿写成已认定侵权。**
来源：[Billboard](https://www.billboard.com/pro/elvis-presley-estate-sues-suno-anthropic/)、[Rolling Stone](https://www.rollingstone.com/music/music-news/elvis-presley-rightsholders-anthropic-lawsuit-infringement-1235647682/)、[Hollywood Reporter](https://www.hollywoodreporter.com/music/music-industry-news/anthropic-elvis-presley-lawsuit-ai-1236739617/)、[HN](https://news.ycombinator.com/item?id=50229645)

音乐版权方对大模型训练/输出的新一轮诉讼。Suno / Udio 类生成音乐公司、以及所有在产品里「续写经典歌词」的聊天应用，合规成本会再抬一截。国内做 AI 音乐、短视频 BGM、有声书的公司，采购训练数据时要把「能否证明授权链」写进合同。受益的是版权集体管理组织、数据授权中间商、以及卖「训练数据 provenance」的初创。

- 产品 / 法务：输出侧对受保护歌词做拒答与引用检测；训练侧留数据来源台账。
- 音乐人 / 权利人：诉讼是谈判筹码，不等于短期就能收到授权费。
- 普通人：别把「AI 会唱 Elvis」当成可以商用的素材。

教程（同类操作参考，AI 训练与创意版权争议科普，非本案庭审）：[How AI Models Steal Creative Work — and What to Do About It | Ed Newton-Rex | TED（YouTube）](https://www.youtube.com/watch?v=U9d0p96N1iw)

## YC 动态

### 11. HeyClicky（YC）：公开推 Windows 首版 + 大版本绘制/本机操控

创始人 `@FarzaTV` 帖（约北京 10-25 03:49；YC 官方账号 RT）宣布 HeyClicky 上 Windows。官网 changelog **v1.1.1 署 Oct 23, 2026** 已写「HeyClicky for Windows: The first version…」并可从首页 Windows 下载；同版还含屏上 2D/3D 绘制讲解、统一「one brain」、Mac 端 computer-use（需确认）、Chrome 扩展让 Agent 用已登录站点、notch 统一入口与例行任务等。

成稿写明：changelog 日期为 10-23，过夜窗为创始人/YC 公开推介；属桌面侧 AI buddy / Agent 扩展平台，非新基座模型。
来源：[Farza X](https://x.com/FarzaTV/status/2114081836544708655)、[YC RT](https://x.com/ycombinator/status/2114106085196157150)、[changelog v1.1.1](https://www.heyclicky.com/changelog)、[YC·HeyClicky](https://www.ycombinator.com/companies/heyclicky)

桌面 Agent 从 Mac 扩到 Windows，用户盘立刻大一截。可与昨稿 Cursor Computer Use、Claude Computer Use 同窗：大家都在抢「能点屏幕的助手」，差别在权限模型和是否绑浏览器登录态。影刀、UiPath、国内的按键精灵生态会感到「自然语言 RPA」压力；Chrome 扩展 + 已登录站点是双刃剑——方便，也等于把会话交给 Agent。

- Windows 重度用户：先装在非工作机或虚拟机，别一上来授全部桌面权限。
- 产品经理：盯「已登录站点」白名单，支付与邮箱默认排除。
- 创业者：跨平台 computer-use + 例行任务，比再做一个聊天框更像 YC 口味。

教程（同类操作参考，Claude Computer Use 安装与演示，非 HeyClicky 专属）：[How to Use Claude Computer Use (Step-by-Step Tutorial)（YouTube）](https://www.youtube.com/watch?v=_gYthLMXlsA)

### 12. YC Paper Club 本周：推理——「训练 1 FLOP / 每年 serving 约 6 FLOP」

`@ycombinator` 原帖（约北京 10-25 00:30）：称本周 Paper Club 聚焦 inference；并写「For every FLOP spent training a model, roughly six go to serving it each year」，以及过去十年把 serving 做对已对应逾约 $220B 市值。属 YC 社区活动推介。二报播客摘要另点 Together AI Dan Fu、Luminal Joe Fiotti 等嘉宾口径——**成稿以 YC 原帖数字为准，嘉宾细节需再核一手。**

与 Deedy 的推理服务商经济账是同一条河：训练是单次大账单，serving 是每年重复的印钞机（也是成本机）。
来源：[YC X·Paper Club](https://x.com/ycombinator/status/2114031815916912736)

对做推理优化、编译器、定制内核、neocloud 的团队，这是 YC 在公开喊「看 serving」。Together、Fireworks、Modal、Baseten、国内的硅基流动 / 潞晨，叙事都会往「单位 token 更便宜 / 更稳」收。应用层创业若还只讲模型智商、不讲 serving 成本，融资材料会越来越难讲。

- 系统 / MLInfra 工程师：Paper Club 主题可当阅读清单；先把 prefills vs decode、KV cache、批处理吃透。
- 创业者：BP 里单独一页写 serving 毛利与卡供给，别只贴 Arena 分数。
- 其他人：当产业重心信号即可。

教程（同类操作参考，推理系统与 vLLM 吞吐，非 Paper Club 当场录像）：[Understanding vLLM with a Hands On Demo（YouTube）](https://www.youtube.com/watch?v=qdPkA5mxLhg)

## 观点洞察：Agent 工时 6:1，并不等于全自动运营——更不等于模型厂替你兜底

今天稿里 Anthropic 一边教客户把 subagent 折回单循环，一边在企业编码席位上被 OpenAI 用价格挤；Argus 则把 Agent 调查锁成只读、变更必须走 broker。同一天若再刷到「Anthropic 用 AI 把人开除了」的二手标题，很容易连成一句：反正公司已经全自动了，业务可以交给 AI，线上炸了找模型厂赔。

先把电影情节拆掉。

### 事实校正：不是「AI 一键裁员」

一手是 Anthropic 自己的研究报告 [How employment is changing at Anthropic](https://www.anthropic.com/research/employment-at-anthropic)（Published Oct 16, 2026；TechCrunch / Guardian 有二报）。里面写得很清楚的几件事：

- 到八月，**interactive agent hours 相对员工大约 6:1**——Agent 干活时间已经远超人。
- 技术部门初级员工占比大约从 **21% 掉到 14%**；初级技术招聘大约从 **27% 掉到 9%**。公司仍在扩张，但少招「只会写实现」的初级档。
- 产品设计文案团队在 spring 2026 做出 context graph 之后「scaled the team out」，人轮岗去写 prompts / evals——报告口径是 **内部调配与岗位变形**，并强调 early warning + prioritize internal redeployments，**不是**公开宣布的「AI 一键裁员」。
- 人的注意力反而成了瓶颈：读完 Agent 输出都能占掉大半周；会议时间还在升；战略与面对面协调几乎仍靠人，Slack 辩论和当面开会在定方向，Agent 并没有坐进董事会。

管理层此前还有过「大约 90% 代码由 Claude 写」一类说法——那是产能叙事，不是责任转让书。你今天稿里的 Apollo 图也在提醒：Mag7 以外多数公司连财务回报都还没看见，更别说「已经全自动运营」。

所以：**自动化在加速，全自动运营远未实现。** 少招初级、把可 Agent 化的活交出去、人被调去管 Agent / 做判断——这才是报告里的主线，不是「人被模型开除、公司交给 Claude 跑」。

### 谁来负责这个业务？能不能「交给 AI」？

法律责任与组织责任仍在雇主和产品 owner。AI 是工具和执行层，不是法人，也不会出席事故复盘。

「交给 AI」只能交**可回滚的执行**：草稿、只读调查、生成补丁、跑测试、准备变更单。不能交的是问责——谁批准上线、谁对客户与监管签字、出事谁停机谁道歉。今天 Argus 把调查锁只读、变更走 action broker，和 Anthropic 单 Agent 指南里强调的预算、写闸门、人审 eval，其实是同一句话：**能干的路径可以自动化，碰真钱、真生产、真关系的闸门要人写死。**

这里我想再借一点昨稿提过的达里奥原则观：原则与升级路径必须由人写成可执行教义——催几次升级、何种变更必须人批、何种输出禁止自动发。你不写，Agent 就会最大化你随口说的 KPI；出了事，法院和客户找的是公司，不是「当时那个 session」。

Rippling 今天把编码用量从 Anthropic 拨向更便宜的 OpenAI，也说明买方仍在为席位和账单做主。换供应商的是人，担生产责任的也是人。别把「Agent 写了大部分代码」读成「Agent 成了业务负责人」。

### 模型厂会不会兜底线上事故？

现实里，**几乎不会。**

你用模型编码上了线，事故责任在部署方：变更审批、测试覆盖、灰度、回滚、值班、对客户的 SLA。模型厂卖的是 API / 工具；商业条款侧，Customer 通常有责任评估 Outputs 是否适合自己的用例、生产前要不要人审。典型 SaaS 是免责声明 + 责任上限，排除间接损失和业务中断——**不是**「你的线上故障我们按营收损失赔」。

Anthropic 对外有过 copyright indemnity 一类叙事（Expanded legal protections）：那是针对**授权使用引发的版权索赔**路径，和「模型写的代码搞挂生产、模型厂替你赔业务损失」不是一回事。勿把版权保护听成生产事故保险。

若真要「兜底」，得另走：商业保险、共同保险、专门的 AI 责任险，或极少数企业级定制合同里把责任写死——目前都不是默认能力，也不是按 token 附赠的。今天 Apollo 说科技外难见回报，一边是 CFO 把 token 当成本中心；一边你还指望同一张 API 账单里含「事故全赔」，两边加起来更不现实。

### 可执行的几条

1. **生产路径保留人批与回滚**：Agent 可以出 PR，合并与发布仍走人；能自动回滚的才允许自动合。
2. **调查与草稿可以大胆交给 Agent**：对齐 Argus 只读、单循环 skills；变更、支付、删库、对客通知默认黑名单。
3. **合同与保险分开谈**：采购模型时问清版权 indemnity 边界；生产风险另买保险或写进自己的变更制度，别默认「厂商会赔」。
4. **别误读产能口号**：90% 代码是 AI 写的，不等于 90% 责任在模型厂；少招初级也不等于公司已经无人值守。

一句话：**Agent 可以替你加班，不能替你背锅；全自动运营还没到，问责链条更不会自动搬到模型厂。** 今天稿里那些「折 harness、加 broker、比编码价、算 ROI」的动作，值钱的地方正在这儿——让模型在你划定的棋盘上跑快，而不是假装棋盘已经交给模型。

## 今天的机会

今天没有大厂全新基座首发，主线更像四件事叠在一起：**社区榜给开源旗舰补信誉**（Kimi K3.1 Pro），**企业编码席位开始比价**（Rippling / OpenAI vs Anthropic），**harness 往回收、变更闸门往外拆**（Anthropic 单循环、Argus 只读 + broker），**铲子层仍在讲增长、应用与创意就业侧在讲成本与裁员**（Deedy / YC Paper Club vs Apollo / Apricitas），外加一条**音乐版权诉讼**提醒训练数据不是免费午餐。

若只选三条可执行的方向：

1. **把编码 Agent 账单拆开再谈切换**：按草稿 / 终审 / 长跑任务对比 Claude Code、Cursor、Codex（及 Kimi 兼容端点）；合同写清折扣档与锁定期。客户是已有几百席位的工程组织。
2. **卖「简单 harness + 硬闸门」**：帮企业折 subagent、补端到端 eval；安全侧做只读调查与 action broker。客户是 Agent 又慢又贵、又不敢让它改生产的中台与 SOC。
3. **站在推理铲子或版权合规一侧**：有卡有栈就盯 utilization 与网关抽成；做内容/音乐产品就把授权链与输出拒答写进发布清单。比空喊「全面 AI 转型」更接近今天的钱和风险。

