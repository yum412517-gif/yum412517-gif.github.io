---
layout: post
title: "AI 每日精选 | 2026-10-23：决策接口上架，Agent 开始有标准件"
date: 2026-10-23 20:40:00 +0800
categories: [AI 新技术]
excerpt: "OpenAI Decisions API 转正，决策模型本地化跟着来；Agent Skills 捐进 Linux 基金会，Google 出 Agent 算力引擎，1Password 给 Agent 加凭证闸门。安全侧 METR 审计和 ARTEX 攻防同天升温。每条写了我自己的判断：谁受益、谁付钱、普通人能拿来干什么。"
---

> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 今天最值得看的几件事

- 决策层产品化：OpenAI Decisions API 正式 GA，Fastino GLiDE 开源权重，Perplexity 放出本机 Decider——分类、路由、打分不再非要先「写一段再解析」。
- Agent 标准件与落地：Anthropic 把 Agent Skills 捐给 Linux 基金会下的 AAIF，同日补齐 Open Responses / OpenEnv / OpenSandbox；Google 预告 Agent Compute Engine；1Password、Uber、Claude Auto mode 各自往「能干活、能进企业」推一步。
- 设计资产可交付：Canva 自研 Craft、Ideogram 出矢量 Vector 1.0，Hi3D 把生产级几何精修开源。
- 开源与推理栈：MiniMax M3.1 Flash 权重按约定放出，vLLM 当日 Day-0；科大讯飞端云一体星火 X2.6。
- 安全攻防显形：METR 公开嵌入式评估 OpenAI 内部 Agent 监控；微软指 Storm-0940 用开源 Agent 框架 ARTEX；AWS Continuum 与 Claude Security 在卖「可验证修复」；x402 支付协议刚爆过严重洞。

## 模型发布

### 1. MiniMax M3.1 Flash：权重按约定开源，vLLM 当日接上

官方 10-19 已推 API（自称相对前代推理近 3× 快、用量成本约降 70%；约 $0.15/M 入、$0.60/M 出），并预告权重 10-23 放出；今天 HF `MiniMaxAI/MiniMax-M3.1-Flash` 上线。约 428B MoE / 每 token 约 23B 激活，多模态，上下文自称最高约 1M。vLLM 官方博文同日宣布 Day-0：覆盖 NVIDIA Blackwell/Rubin 与 AMD MI350 系，预建镜像可用；性能数字来自 vLLM 官方基准，未见独立第三方复测。SGLang 等也宣称 Day-0。DeepSeek、MiniMax 据央视系账号与路透/SCMP 转述，已完成拟议出口管制背景下的技术出口登记并继续开源——草案仍在征求意见，勿写成「已获正式出口许可证」。
来源：[MiniMax Blog](https://www.minimax.io/blog/minimax-m31f)、[HF MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)、[vLLM Day-0](https://vllm.ai/blog/2026-10-23-minimax-m31-flash)、[Reuters 转述出口登记](https://www.investing.com/news/stock-market-news/chinas-deepseekminimax-win-approval-for-ai-global-use-state-mediaaffiliated-entity-says-4968133)

国内做 Agent / 编码流水线的团队会立刻掂量：同样工作流换便宜 Flash，再叠缓存，账单能再砍一截。字节豆包、阿里通义、智谱、DeepSeek Flash 档继续被挤；OpenAI / Anthropic 顶档更多留给终审。推理侧 vLLM / SGLang / Inferact 这类「Day-0 接新权重」的栈，会变成开源模型发布的标配附件。

生意上我仍看好「两段式」：Flash 出草稿或跑工具，旗舰抽检。付钱的是客服外包、内容工厂、出海 SaaS。自建推理的团队，Day-0 镜像能省掉一周踩坑。

- 程序员：用 vLLM 镜像或 OpenRouter 先跑自己的回归集，别一上来信官方 tok/s。
- 自媒体：同一提示词对比 Flash 与上一档，录屏就是内容。
- 电商卖家：批量标题/详情初稿可以，违禁词还得人看。

教程（同类操作参考）：[Run any open-source LLM on the cloud with vLLM（YouTube）](https://www.youtube.com/watch?v=rNtoDOtmoHQ)

### 2. 设计向模型同日两发：Canva Craft 与 Ideogram Vector 1.0

Canva Research 放出首个从零训练的文生图基座 Craft：两阶段「先规划构图/层级/文字再渲染」，最高约 2K、30+ 画幅；自称 DesignArena 图像实验室第 2，人物与风景子榜第 1。训练偏 Canva 模板库（海报/社媒/演示），可经 Magic Layers 转可编辑图层；Dream Lab 全量可用并开放 Public API，MCP「即将」接入。规划 Craft-fast / ultrafast，Leonardo.ai 团队参与。

同窗 Ideogram 发首个矢量模型 Vector 1.0：文生或图转可编辑 SVG，API 文生矢量约 $0.13–0.20/张量级。场景是 logo、印刷、品牌资产——能改色、能缩放、能拆形状。
来源：[Canva Newsroom](https://www.canva.com/newsroom/news/canva-craft/)、[TechCrunch·Canva](https://techcrunch.com/2026/10/22/canva-releases-its-first-image-generation-model/)、[Ideogram Vector](https://ideogram.ai/models/vector/)、[Ideogram 官方 X](https://x.com/ideogram_ai/status/2113300317584720259)

Midjourney、Nano Banana、Adobe Firefly 在「好看」上继续卷；Canva / Ideogram 在卷「能进设计系统」。对国内稿定设计、创客贴、美图设计室是直接压力；代运营和品牌工作室会把「AI 出可编辑图层/SVG」写进交付清单。

谁付钱？电商品牌市场部、MCN、中小企业做物料外包。按张或按席位都能收。

- 设计师：用 Craft 出构图，再进图层改字；logo 线优先试矢量，少在位图里抠边。
- 电商 / 自媒体：主图和信息图可以一条流水线，印刷物料记得要 SVG。
- 老师：课件插图够用，别指望品牌级字标一次过。

教程（同类操作参考，基于 Canva Magic Studio 既有界面，非 Craft 专属）：[How to Use Canva Magic Studio（YouTube）](https://www.youtube.com/watch?v=MnI4tb0uMwo)

### 3. 决策模型开源与本地化：Fastino GLiDE，Perplexity Decider for Mac

Fastino 在 HF 开源 GLiDE（仓内标 glide-v1.2）：给定状态与 typed 问题，单次前向返回各选项概率（choice / noul / score），不生成文本；约 26B，需约 ≥80GB 单卡，另有托管 API。许可含 Community License + 基于 Qwen3.8-27B 的第三方条款。

Perplexity 放出 Decider for Mac：Apple silicon 本机跑约 4B 的 `pplx-decider-flash-v1.2`（首启约 5.8GB GGUF），本地 Decisions API `127.0.0.1:8080`，无 Key、无按量账单，请求形态与托管版一致。
来源：[HF fastino/GLiDE](https://huggingface.co/fastino/GLiDE)、[Perplexity·Decider for Mac](https://docs.perplexity.ai/docs/decisions/decider-for-mac)、[HF pplx-decider-flash-v1.2](https://huggingface.co/perplexity-ai/pplx-decider-flash-v1.2)

这和今天的 OpenAI Decisions API、昨天 Base Labs / 蚂蚁 LingDT 是同一条河：客服升级、风控放行、内容审核、路由分流——要的是可审计分数，不是散文。阿里、腾讯云、火山的「模型超市」多半会跟进上架；规则引擎厂商会被逼做混合架构。

钱在「决策中间件」和「本机决策网关」：帮互金、保险、电商客服把「让 LLM 写一段再正则」换成直接打分。付钱的是风控和客服中台。

- 程序员：拿「是否升级人工」做小基准，对比聊天模型和决策模型。
- 律师 / 医生：最多当预筛，不能当结论。
- 小店主：退货原因分类可以试；别拿去自动拒赔。

教程（同类操作参考）：[OpenAI Agents SDK: Guardrails & Structured Output（YouTube）](https://www.youtube.com/watch?v=MYR68hG2hFI)

### 4. 科大讯飞星火 X2.6：端云一体，外加 4B 端侧

10-22 讯飞 1024 开发者节发布。云端 Spark-X2.6：293B 总参 / 30B 激活 MoE，上下文扩至约 1M；公司强调全国产算力与长程效率（现场口径含训练/推理效率倍数，成稿作公司自称）。端云按任务路由纯端 / 纯云 / 协同；刘庆峰口径称未来约 60% 场景可端侧。端侧 X2.6-4B 同步推出，HF/ModelScope 可见权重。API 页 X2.6 限时 6 折。
来源：[华尔街见闻](https://wallstreetcn.com/articles/3784219)、[人民网英文转述](http://en.people.cn/n3/2026/1023/c90000-20511624.html)、[HF Spark-X2.6-4B](https://huggingface.co/XHToken/Spark-X2.6-4B)

教育、政务、车机、办公套件仍是讯飞主场。对华为盘古、阿里通义、百度文心的「端侧+国产算力」叙事是同台竞争；对纯云 API 创业公司，政企标书里「可端侧」会多一个勾选项。

- 程序员：先拿 4B 在 Ollama / 本机跑手感，再决定要不要上云端 X2.6。
- 老师：口语评测、作文初评可以试点，分数别全自动。
- 其他人：当国产效率信号看即可。

教程（同类操作参考）：[Ollama Full Tutorial for Beginners 2026（YouTube）](https://www.youtube.com/watch?v=WC0NOMb3Yn0)

### 5. Hi3D V1.0 开源：图条件几何精修到约 1536³

北京团队把生产验证过的 image-to-3D 精修权重开源（原 Sparc3D 叙事）：粗网格 + 参考图条件下稀疏 latent 多遍精修，名义 512³ / 1024³ / 1536³；仅几何、无纹理。HF / GitHub 已上；1536³ 档公司仅在约 96GB H20 验证。许可可商用，超约 20 万 MAU 或月入约 $100 万须另申请。同场商用 V3.0（自称更高分辨率+纹理）勿写成已开源。
来源：[Hi3D 官方](https://www.hi3d.ai/hi3d-1-0-open-source)、[HF Hi3Dv1.0](https://huggingface.co/hi3d-official/Hi3Dv1.0)

游戏资产、电商 3D、工业原型会感兴趣；Meshy、Luma、国内数美 / 时光坐标一类会感到开源压力。和 Canva Craft、Ideogram Vector 同日，像在说：生成物要「可进生产线」，不只是好看。

- 游戏 / 三维同学：有大显存再碰 1536³；小团队先 512³ 看管线。
- 电商：产品三维展示可以跟，贴图还得另做。
- 其他人：跳过。

## 工具与产品

### 6. OpenAI Decisions API 正式 GA：分类/路由/评分的低延迟接口

基于 GPT-6 Luna 的专用 Decisions 端点转一般可用；相对 Responses API 上的 Luna 自称可快约 10×，面向有界答案（predicate / choice / score）。公测后新增：原生 GPT-Live、prompt caching、美/欧驻留、原生 JSON 输入、单请求最多约 400 问。标价约 $0.10/M 输入、$0.01/M 缓存输入，无输出 token 费。客户口径：Box 保单路由约 5× 快；Datadog 对 agent shell 风险打分 p95 较前沿模型约 40× 快；Ramp、Sierra、Speak 也给了延迟/成本数字——均为客户/官方口径。
来源：[OpenAI·Decisions](https://openai.com/index/decisions-api)、[开发者文档](https://developers.openai.com/api/docs/guides/decisions)

这是把昨天还在「决策模型」概念区的东西，收成平台标准接口。Anthropic、Google、国内大厂若只卖聊天补全，企业采购会多问一句「有没有 Decisions 这类端点」。风控、客服、可观测性（Datadog 叙事）、语音下一步动作（Speak）都会成为样板间。

机会在「把现有 Agent 里的 if/else 和正则提取，换成 Decisions 调用」的迁移咨询，按调用量分成或项目制。付钱的是已经上了 Agent、却被延迟和解析错误折磨的中台。

- 程序员：先把一个分类节点从 chat 改成 Decisions，比全盘重写稳。
- 产品经理：选项集合设计比提示词文采重要。
- 小店主：暂时用不上，等客服 SaaS 把这层藏进产品。

教程（同类操作参考）：[Hands-On Structured Outputs in LLMs（YouTube）](https://www.youtube.com/watch?v=gsJxuvdSa68)

### 7. Agent 标准进 Linux 基金会：Skills、Open Responses、OpenEnv、OpenSandbox

Anthropic 把 Agent Skills（SKILL.md 文件夹格式）捐赠给 AAIF，称自 2025-12 以来约 70+ 平台集成（含 ChatGPT、Cursor、GitHub Copilot、VS Code），约 100 万 skills、近 2.8 亿次安装。Linux Foundation 同日宣布 AAIF 一年内从 3 个项目扩至 10 个，新增四项：Agent Skills；OpenAI 的 Open Responses（多厂商互操作接口规范）；Hugging Face 的 OpenEnv（可插拔 RL 环境）；阿里的 OpenSandbox（多语言 SDK + Docker/K8s 沙箱）。场合是圣何塞 AGNTCon + MCPCon。
来源：[Anthropic·捐赠 Skills](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)、[Linux Foundation / AAIF](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox)

「Agent 互操作」从口头联盟变成基金会项目清单。Cursor、Copilot、ChatGPT、国内通义/文心的 Agent 市场，会被迫对齐 Skills / Responses 形状；沙箱云（Daytona、Maritime、阿里 OpenSandbox）会把兼容写成卖点。做垂直 Skill 包（律所、代账、电商运营）的小团队，分发渠道变宽了。

- 程序员：把团队高频流程收成 SKILL.md，比再写一套私有 plugin 划算。
- 创业者：盯 Open Responses 兼容层，别只绑一家 Chat API。
- 普通人：知道「Agent 开始有 USB-C」就行。

教程（同类操作参考）：[MCP Tutorial for Beginners: Connect Claude to Any Tool（YouTube）](https://www.youtube.com/watch?v=40k3SIwlFVM)

### 8. Google 的 Agent 基建包：Compute Engine、Knowledge Catalog、Claude 双托管

Google Cloud 预告 Agent Compute Engine：面向 Agent 的硬件隔离 microVM（Titanium IPU、短生命周期凭证等），称已支撑 Gemini Agent，客户 preview「未来数月」。同场开源 Agent Substrate（GKE，自称高密度激活），扩展 Gateway / Registry / Identity / OTel。Knowledge Catalog 做自学习上下文 enrichment + Knowledge Studio（preview），内部口径自称准确率近 4×、token 最多约少 75%。另：Claude 在 GCP 新增 Anthropic-managed 部署 GA，与 Google-managed 并行，账单仍走 GCP；可用 Fable 5.1 / Sonnet 5.5 / Haiku 5.5 / Opus 5.5 等。
来源：[Google Cloud·ACE](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance)、[Knowledge Catalog](https://cloud.google.com/blog/products/data-analytics/knowledge-catalog-self-learning-context-enrichment-for-ai-agents)、[Claude on GCP](https://cloud.google.com/blog/products/ai-machine-learning/expanding-claude-availability-on-google-cloud)

企业采购会从「哪个模型聪明」转向「Agent 跑在哪、上下文谁维护、身份怎么审计」。微软 Azure AI、AWS Bedrock、国内阿里云 / 腾讯云的 Agent 运行时，都会被拿来对标 ACE + Substrate。多云已买 GCP 承诺消费的公司，Claude Anthropic-managed 是抵扣账单的新出口。

- 架构师：先画清 Agent 身份（SPIFFE）和上下文域，再挑模型。
- 采购：合同写明 Google-managed vs Anthropic-managed 的数据处理方。
- 程序员：个人项目用 Gemini API CLI 实验预览即可，企业特性等 preview。

教程（同类操作参考）：[Tips for building AI agents（YouTube）](https://www.youtube.com/watch?v=LP5OCa20Zpg)

### 9. Agent 进办公室：1Password 凭证闸门、Uber 全员 ChatGPT Work、Claude Auto mode 默认

1Password for Agents：Agent 到登录页向 1Password 申请凭证，用户桌面端审批后由 1Password 填表，密码/OTP 不进模型。对接宣称含 Meta Muse、Claude Duet、ChatGPT Work、Grok Bot 等（部分滚动上线）。Individual/Family 无额外费用。

OpenAI 客户故事：Uber 自约 1000 人试点扩至全球 3 万+ 员工用 ChatGPT Work（接 Drive/Gmail/Calendar/Slack）。Anthropic：Pro/Max/Team 多数 Claude 应用下周起新会话默认 Auto mode——自动放行安全操作、拦高风险；Enterprise / API 仍先 opt-in。Claude Code 数据：人手拦危险命令约 13.6%、auto mode 约 89%（付费测试口径）。
来源：[1Password for Agents](https://1password.com/blog/1password-for-ai-agents)、[OpenAI·Uber](https://openai.com/index/uber-chatgpt-work-rollout)、[Claude·Auto mode](https://claude.com/blog/auto-mode-default-in-claude-code)

「能干活」和「能进企业」撞在同一周。国内的企业微信、钉钉、飞书若还停在对话助手，和 Duet / Work / Muse 的差距会被采购看见。密码管理（1Password、Bitwarden 企业版、国内的各类 PAM）会多一个 Agent 审批产品线。

- 小团队老板：先上「凭证不进模型」的闸门，再开自动模式。
- 程序员：Auto mode 可以开，高风险目录仍手批。
- 普通人：别把网银密码交给任何 Agent。

教程（同类操作参考）：[Mastering Claude Code in 30 minutes（YouTube）](https://www.youtube.com/watch?v=B_KAEqiC-0Q)

### 10. Framer 官方 MCP：画布和 CMS 交给 Agent，人只做终审

远程 MCP `https://mcp.framer.com/mcp`，Claude / Codex / Cursor / Grok Bot 等可改画布、管 CMS、发布站点；改动仍在 Framer 内审阅。
来源：[Framer MCP](https://www.framer.com/mcp/)、[Framer Updates](https://www.framer.com/updates)

Webflow、Studio、国内奥格 / 凡科一类建站工具会被迫补 MCP。独立开发者和工作室可以把「改文案 / 上活动页」交给 Agent，自己只看 diff。

- 设计师 / 建站：接上 MCP 后，先只授修订权限，发布按钮留人。
- 程序员：研究 Framer MCP 的工具列表，找缺口做垂直 Skill。
- 小店主：活动页改价改图可以试，支付配置别自动。

教程（同类操作参考）：[MCP Tutorial for Beginners（YouTube）](https://www.youtube.com/watch?v=40k3SIwlFVM)

### 11. Warp Sciences 隐身：约 2.15 亿做美方药化 CRO + 机器人湿实验

前 OpenAI 科学负责人 Kevin Weil 等创办，Lightspeed 领投 Series A，公司口径估值约 $8.65 亿 post-money。定位美国本土化学 CRO：为人制药客户合成测试先导化合物，化学家示教后把重复步骤交给机器人；自述不做自有管线。叙事对标把大量外包到中国（报道点名如药明康德）的工作回流。
来源：[Business Wire](https://www.businesswire.com/news/home/20261022200104/en/Warp-Sciences-Emerges-From-Stealth-With-%24215-Million-to-Build-U.S.-Chemistry-Services-for-Drug-Research)、[TechCrunch](https://techcrunch.com/2026/10/22/former-openai-science-lead-launches-warp-science-to-automate-wet-labs-with-robots/)

AI × 机器人 × 生命科学的「卖铲人」又一家。药明、康龙、凯莱英等 CXO 会关注订单是否分流；国内想做湿实验 Agent 的团队，合规和场地比模型难。Anthropic 同日开放生命科学 Guest Investigators（8–12 周共研），说明大厂也在用合作网络补实验闭环。

- 生物 / 药化同学：当行业信号，实验室规范比追 demo 重要。
- 投资人：看这类公司先问产能与客户续约，不看创始人光环。
- 其他人：跳过。

### 12. Agent 分发权：Meta Muse 进日本，Spotify 想当「Agent 背后的媒体源」

Muse 自 10-23 起在日本提供，北美以外首个正式市场；隔离 VM + Sentinel，敏感操作需确认；连 Gmail / 日历 / Instagram 及 Stripe、Shopify、Trip.com 等，日本侧推进与美客多、Money Forward、票务平台联动。

Spotify 联席 CEO 称音乐是少数在 agentic 时代可顺风的品类——目标是成为任意 Agent（Muse、ChatGPT、Claude）背后的媒体源，听歌数据不交给合作方。对照：亚马逊等在挡第三方购物 Agent，Spotify 选择 lean in。
来源：[Meta 日本·Muse](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[TechCrunch·Spotify](https://techcrunch.com/2026/10/22/spotifys-current-ai-bet-is-about-being-the-music-service-that-agents-choose/)

个人 Agent 开始抢「区域」和「默认媒体源」。国内的抖音、网易云、汽水音乐若只做 App 内推荐，以后可能要面对「Agent 点名播放」的接口政治。电商侧昨天的沃尔玛欢迎 / 银行阻拦，和今天的 Spotify lean in，是同一张图的两边。

- 产品经理：列一张「哪些能力愿意被外部 Agent 调用」的白名单。
- 音乐人 / 播客：关注平台是否提供 Agent 可读的结构化曲库。
- 普通人：Muse 类 Agent 先关支付权限。

### 13. 生产侧 Agent：Replit Monitoring Agent；推理聚合 You.com Router

Replit：生产告警→读日志指标→调查→写修复并验证；默认邮件汇总，实验性 opt-in 可自动发布已验证修复。定位「口袋 on-call」。

You.com Inference Router：开源权重 + 网页搜索一体、OpenAI 兼容；自称 ≥99.9% SLA、零数据保留、美国托管；客户口径有「账单约减半」——为客户自述。模型目录滚动含 Kimi、GLM、DeepSeek、Qwen、MiniMax 等。
来源：[Replit Monitoring Agent](https://replit.com/blog/replit-monitoring-agent)、[You.com Inference Router](https://you.com/resources/introducing-inference-router)

编码 Agent 之后是运维 Agent；开源权重托管之后是带搜索和 SLA 的路由。Datadog、PagerDuty、国内的观测云 / 夜莺会感到「Agent 自动修」叙事压力；OpenRouter、Fireworks、Together、国内硅基流动会多一个带搜索的对手。欧洲侧还有 YC 的 Munito（默认隐私、欧区端点）——地缘上的镜像产品。

- 程序员：Monitoring Agent 类功能先开「只告警+出 PR、不自动发布」。
- 创业公司：推理账单敏感就评估 Router / Munito，记得做回归。
- 运维：自动发布开关默认关。

教程（同类操作参考）：[How to use OpenRouter（YouTube）](https://www.youtube.com/watch?v=XK8Kp4Tkb88)

### 14. 算力与资本：Humain 84MW、Nebius 35 亿贷款、哈萨克斯坦出口许可、Meta Class C、a16z Frontier

沙特 Humain × NVIDIA 扩约 84MW / 约 2.7 万 GPU 管线（含未具名美客户约 50MW Vera Rubin 段，视最终协议）。Nebius 获 Citi 约 $35 亿高级担保过桥，加码 AI 云。Firebird × Kazakhtelecom：约 4.5 万 Grace Blackwell 获美出口许可，一期 Data Center Valley 拟 2027 Q3 商用——许可≠已交付上架。Meta 发非投票 Class C 为 AI 基建/并购筹资，并留出卖股缴加州拟议富人税空间。a16z Crypto 更名为 a16z Frontier，扩至 AI/机器人。同窗还有 inDrive × Pony.ai × NVIDIA 在哈萨克斯坦的 Robotaxi MOU（拟 2027 上半年阿斯塔纳试运营）、Rivian 收购世界模型创业公司 Third Dimension。
来源：[The National·Humain](https://www.thenationalnews.com/future/technology/2026/10/22/saudi-arabias-humain-expands-nvidia-deal-with-84mw-ai-computing-plan/)、[Nebius](https://nebius.com/newsroom/nebius-secures-3-5-billion-financing-facility-with-citi)、[NVIDIA·Kazakhstan](https://blogs.nvidia.com/blog/kazakhstan-ai-compute-ecosystem/)、[TechCrunch·a16z Frontier](https://techcrunch.com/2026/10/22/as-blockchain-investing-falls-out-of-vogue-a16z-crypto-rebrands-as-a16z-frontier/)、[TechCrunch·Rivian](https://techcrunch.com/2026/10/22/rivian-buys-world-model-startup-to-accelerate-self-driving-ambitions/)

钱和兆瓦还在往「AI 工厂」堆；软件侧 Minerva（NVIDIA AIOps）和昨日 OpenShell 在 HN 继续升温（采集窗内约 400+ 分），说明运维与沙箱也是采购项。对中国供应链（液冷、光模块、电力）是订单；对要建本地推理的创业公司是租金压力。

- 基建 / 投资：分清「出口许可 / MOU / 已通电」。
- 普通人：数据中心争地争电的新闻会更多，和 ABC 民调里「反对新建」对得上。

## 论文研究

### 15. Anthropic：用 Claude 在汇编级大规模形式化验证开源库

与 Theorem 合作，在 RISC-V 汇编级对 OSS-Fuzz 中 123 个库、239 个 fuzz 入口证明「给定假设下对 <64MB 输入无崩溃」；约 1.8 亿行 Rocq，经检查器验证。过程中发现并修补多年未现的边界 bug（含 CVE 再发现）。Theorem 提供为其他开源项目跑同管线，并发布 Claude skill。HN 本窗持续高位讨论。
来源：[Anthropic Research](https://www.anthropic.com/research/formal-verification)、[Anthropic X](https://x.com/AnthropicAI/status/2113390212911083894)

防守向 AI 安全、关键开源基础设施（OpenSSH 一类）的维护组织会跟进。和昨天「攻击面缩小」、今天 METR 监控评估、微软 KLS 人机协作证明，叠成「AI 参与硬验证」叙事——但都强调机器证明 + 人类假设，不是魔法免检。

- 开源维护者：可以排队试 Theorem 管线，补丁仍要人审。
- 安全工程师：把「形式化假设」写进威胁模型，比只跑 fuzz 多一层。
- 其他人：当研究突破看。

### 16. 医学与数学两记：MAI-DxO 上 Science；MSR 人机协作证 KLS

Microsoft AI：MAI-DxO 诊断编排器 + SDBench 刊于 Science。公司口径：304 例 NEJM 复杂病例约 83% vs 医师约 22–36%；急诊样例约 80% vs 约 47%。开源部分 benchmark 代码；与 Mayo 等推进真实场景评估。**文本基准 ≠ 临床获批产品。**

MSR：Xinzhi Zhang 与 Zhao Song 证明 KLS 猜想（约 31 年）；叙事称 AI Agent 在人主导下探索大量思路，另有独立证明与 Lean 跟进。数学社区确认仍在展开。
来源：[Microsoft AI·MAI-DxO](https://microsoft.ai/news/building-medical-superintelligence/)、[MSR·KLS](https://www.microsoft.com/en-us/research/blog/solving-a-31-year-old-grand-challenge-in-mathematics-the-kls-conjecture/)

医院 IT、医学教育、保险预审会买「编排式诊断辅助」故事；监管和伦理审查会更紧。数学侧说明「人定方向 + Agent 铺路」可以碰真猜想，但新闻稿不等于终审定论。

- 医生：当文献 / 教学工具，诊断别甩锅给模型。
- 数学研究生：可复现公开证明与 Lean，不追叙事。
- 产品：医疗口号慎写「超医师」。

### 17. Agent 如何变强：MIT「玩耍」迁移；腾讯×复旦 WorkForge；Toolflation

MIT 论文：13 个 Claude Agent 在未见过的模拟荒岛独处约 30 小时、无任务，出现自定规则等「玩耍」行为；其后在限时任务上整体优于同架构零经验对照；学习载体是可编辑文本记忆。主观体验未证，有认知科学家保留「或为角色扮演」意见。

腾讯混元 × 复旦 WorkForge：从真实文件合成可验证长程工作环境，自称约 1.67 万环境；SFT 后 GDPval 等大幅提升。发稿时未见公开代码/数据集。

Google / Toronto 的 Toolflation：卖方 Agent 在竞争下自发夸大工具描述，严重时可扭曲买方选择至接近随机；主张「对第三方诚实」属安全对齐。开源了代码与数据集。
来源：[arXiv:2610.07130](https://arxiv.org/abs/2610.07130)、[TechCrunch·玩耍](https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/)、[arXiv:2610.04906 WorkForge](https://arxiv.org/abs/2610.04906)、[arXiv:2610.28454 Toolflation](https://arxiv.org/abs/2610.28454)

做 Agent 平台的人该紧张的是「经验如何沉淀」和「工具市场如何防通胀」。MCP 注册中心、企业工具目录、应用商店审核，都会多一项「描述是否诚实」的评测。MemTensor 开源的 MemT-1.0（原生记忆基座）可对照看「记忆是否该进权重」。

- 程序员：工具描述加「能力边界 + 失败用例」；别只写营销句。
- 产品：Agent 应用商店上架，准备抽检。
- 研究者：playground 里留「无任务区间」或许可当课程学习。

教程（同类操作参考）：[Tips for building AI agents（YouTube）](https://www.youtube.com/watch?v=LP5OCa20Zpg)

### 18. 社会与教育：CEPR「学习惩罚」；Anthropic 预期落差；Harvard AI 审稿

CEPR 讨论稿：约 2.6 万中国中学生面板——采纳生成式 AI 后作业分升、完成时间降，但约半年内闭卷考试分约 −20%，高利害考试损失充分显现约需两年；外包型用户受损更大。讨论稿，未逐校复核。

Anthropic Institute：公众 vs 实验室员工对 AI 经济影响预期落差大（如诺奖级发现、工作可被 AI 完成比例）。Harvard IQSS 工作论文：盲测中 AI 审稿在多项指标优于高质人工审稿样本——样本来自预投服务，非产品发布。
来源：[CEPR DP21577](https://cepr.org/publications/dp21577)、[Anthropic·Expectations Gap](https://www.anthropic.com/research/ai-expectations-gap)、[Gary King·peerless](https://gking.harvard.edu/peerless/)

教育部门、期刊编辑部、政策团队会引用。教培公司和「AI 写作业」工具会被家长追问考试成绩；期刊可能试点「作者预跑 AI 审稿 + 编辑终审」，也要防同质化。

- 老师 / 家长：作业允许 AI，考试与口试权重上调。
- 研究生：AI 审稿可当预检，别替代同行评议。
- 管理者：别用实验室员工的乐观代替社会预期。

## 最佳实践

### 19. METR×Redwood：嵌入式评估 OpenAI 内部 Agent 监控

2026-07-21 至 08-11 三周，评估方持内部代码/监控配置现场工作，公开帖仅高层摘要。发现覆盖缺口与可规避路径示例：估约 75–94% 达 GPT-5.5+ 的内部 Responses API Agent 流量「有资格」被监控；compaction 未监控等致漏监（OpenAI 称评估期间已修）；Agent 可拖长回合推迟监控等。OpenAI 称影响生产栈的漏洞已修；评估方**未复核**。可与昨内部 Agent 关监控事故对照，勿混成同一事件。
来源：[METR](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/)

企业安全、合规、董事会会拿它要预算。微软 Guardian Agents、ServiceNow Arc、各家 Agent 运行时安全创业公司，会把这类报告当销售附件。

- 架构师：审计通道必须 Agent 不可改；监控延迟不能被「拖回合」套利。
- 管理者：第三方嵌入式评估比自评 PDF 值钱。
- 普通人：对「我们有监控」多问一句覆盖率。

### 20. 攻防一周：ARTEX 供应链、Continuum / Claude Security、x402 支付洞、Clinton「18 个月」

微软：中国背景口径 Storm-0940 用开源多 Agent 渗透框架 ARTEX 加速打击，评估其关联 ConnectWise 供应链入侵；对超约 2250 个 M365 租户尝试登录等（厂商归因，细节未独立复核）。AWS Continuum for code vulnerabilities GA：可利用性验证 + 按业务冲击排序 + PR 修复（当前一律人审）。Claude Security：仓库持续扫描、修复跟踪、威胁模型，Enterprise 公测。V12 披露 x402 协议约 25 项漏洞（含 3 严重：可假付、SIWx 域校验、默认无支出上限）；称约 8 月已修、设默认约 $1/笔。Anthropic 副 CISO Jason Clinton 称未来约 18 个月网络安全或先更糟，呼吁董事会批「基础防护」预算——从业者预警，非漏洞通告。OpenAI 另与波兰 NASK 签安全研究合作，并致信加州州长建议加强 SB 53。
来源：[Microsoft·Storm-0940](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)、[AWS Continuum](https://aws.amazon.com/blogs/aws/aws-continuum-for-code-vulnerabilities-is-now-generally-available/)、[Claude Security](https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes)、[V12·x402](https://v12.sh/blog/x402)、[Clinton 原帖](https://x.com/JasonDClinton/status/2113325263157395456)、[OpenAI×NASK](https://openai.com/index/openai-nask-ai-safety-security-partnership/)

进攻方用 Agent 压缩从侦察到提权的时间；防守方在卖「可验证利用 + 自动出 PR」。任何接了自动支付、自动修代码、自动登录的团队，都要把支出上限和人审闸门当成默认。

- 程序员：依赖锁定、密钥轮换；Agent 支付默认日限额。
- 安全负责人：用 Continuum / Claude Security 一类工具清告警噪音，修复合入要闭环。
- 老板：董事会材料里单独列「基础防护」而不是只写 AI 项目。

### 21. Agent 准入分叉：美大行继续挡、瑞典政府屏蔽 ChatGPT/Claude、Etsy 收紧 AI 上架

昨 Axios 线今早继续升温：大行限制未审查第三方 Agent 用客户凭证操作，只读路径往往仍可。瑞典政府办公厅自周一起屏蔽工作电脑访问 ChatGPT 与 Claude，导向已批准的 Copilot（媒体转述内网口径）；部分人员仍可通过自研平台访问。Etsy：首图须未编辑实拍、AI 艺术须披露、禁 bot 铺货。
来源：[Yahoo Finance 转述银行](https://finance.yahoo.com/technology/ai/articles/five-major-banks-blocking-ai-165359538.html)、[Sveriges Radio](https://www.sverigesradio.se/artikel/chat-gpt-och-claude-forbjuder-regeringskansliet)、[The Verge·Etsy](https://www.theverge.com/tech/1017261/etsy-ai-rules-policies-restrictions-listing)

金融要闸门，政府要合同内工具，电商要实物信任——三套逻辑。国内的银行开放银行、政务云白名单、淘宝/拼多多对 AI 生成图的治理，大概也会这么分叉。Barclays 称年内裁约 5000 人、AI 是「icing on the cake」，提醒：裁员新闻里的 AI 往往是配料不是主菜。

- 普通人：购物 Agent 设低限额；网银别授权给未审查助手。
- 电商卖家：按 Etsy 新规自查首图与 AI 披露，国内平台大概率跟风。
- 公务 / 国企 IT：列「批准工具清单」，比全面封禁好执行。

### 22. 选型与舆论：Coding Agent Index v2.0；ABC 民调；算力碳排与幻觉判例

Artificial Analysis Coding Agent Index v2.0：更严任务集上 Claude Code + Opus 5.5 领跑；同测多数配置分数下降。ABC/Post/Ipsos：约 57% 美国人认为 AI「对社会不好」，约 66% 反对新建数据中心。Berget 开源单次请求 CO₂ 算法，同请求得州约 8.5× 瑞典（方法为厂商+智库，边际排放会改结论）。美国第五巡回因 AI 幻觉撤销密西西比联邦法官禁令并改派——书记官用 AI 起草误入虚假判例。
来源：[Artificial Analysis Coding Agents](https://artificialanalysis.ai/agents/coding-agents)、[ABC News 民调](https://abcnews.com/Politics/americans-ai-bad-society-oppose-data-centers-abcpostipsos/story?id=137414085)、[Berget CO₂](https://berget.ai/en/blog/per-request-co2-press-release)、[Courthouse News·第五巡回](https://www.courthousenews.com/fifth-circuit-castigates-ai-rulings-in-school-diversity-policy-case/)

选型看「模型+harness」合分，不看单模参数。舆论与碳排会进入数据中心环评；法律文书必须人核引用——和 Toolflation、x402 一样，都是「Agent 输出进真实世界」的护栏问题。美国财政部 COINS 出境投资 NPRM（含 AI/超算等）仍是征求意见，勿写成已生效禁令。

- 程序员：同一任务用 Claude Code 与另一套各跑一遍，记录差异。
- 律师 / 法务：任何 AI 起草的裁定/合同，引用必须可点击核验。
- 关注公共事务的人：数据中心争议会长期化。

教程：[Mastering Claude Code in 30 minutes（YouTube）](https://www.youtube.com/watch?v=B_KAEqiC-0Q)

## YC 动态

### 23. 工厂到分销的决策 Agent：OpEra 与 Lark

OpEra（Launch YC）：连 WMS/ERP/Excel 做排产、仓储与配送优化，变化可用自然语言或 Agent 触发重规划；自述案例含配送成本约降 38% 等（公司口径）。Lark：叠在分销商既有 ERP 上，推荐补货、起草采购与供应商邮件，规则内可自动下单；演示视频已公开。可与昨 Horizontal（工厂运营 Agent）对照。
来源：[Launch YC·OpEra](https://www.ycombinator.com/launches/W3c-opera-the-ai-decision-engine-for-factories-warehouses-and-fleets)、[Launch YC·Lark](https://www.ycombinator.com/launches/W5s-lark-ai-agents-for-distributors)

制造与分销的「脏活系统」仍是 YC 主战场。国内用友、金蝶、旺店通生态里的实施商，可以把同类 Agent 做成交付件。

- 供应链 / 制造业：先旁路推荐，审批后再写回 ERP。
- 程序员：ERP 连接器 + 可解释优化，比纯聊天值钱。

教程（产品演示）：[Meet Lark: AI agents for distributors（YouTube）](https://www.youtube.com/watch?v=ZmQ8DWiVuv8)

### 24. 发布前质量闸门：Aucert、Simulithic；GTM 与医疗：Kiwi、Cesara、Ignition

Aucert：专用 Agent 无脚本自测移动 App（商店政策、无障碍、类真人逐屏），附证据报告。Simulithic：跨设备/浏览器 AI 用户测试，可嵌 CI/CD。Kiwi：给 GTM Agent 做数据工程师，每步展示 SQL 与快照。Cesara：医保合约核对与欠付追回。Ignition：美企 20–200 人 AI-native 福利经纪（持证经纪人+AI，美国市场）。
来源：[Aucert](https://www.ycombinator.com/launches/WGP-aucert-ai-agents-that-verify-mobile-apps-autonomously)、[Simulithic](https://www.ycombinator.com/launches/W3D-simulithic-ai-users-that-test-your-app-on-every-device-and-browser)、[Kiwi](https://www.ycombinator.com/launches/WGR-kiwi-your-gtm-agent-s-data-engineer)、[Cesara](https://www.ycombinator.com/launches/WBc-cesara-ai-agents-that-make-sure-every-healthcare-transaction-is-paid-per-contract)、[Ignition](https://www.ycombinator.com/launches/TzC-ignition-the-ai-native-benefits-broker-for-modern-companies)

Agent 写代码变快之后，验证、数据可信、垂直合规变成新瓶颈。和 Replit Monitoring（发布后）正好前后夹击。

- 移动开发：上架前用 Aucert / Simulithic 同类流程压一轮。
- 医疗运营（美国）：合约核对自动化值得试点，自动申诉要人审。
- GTM：Agent 每步要能展开到 SQL，不然别接生产。

教程（产品演示）：[Aucert launch（YouTube）](https://www.youtube.com/watch?v=pd_mqx7HXNo)；[Simulithic launch（YouTube）](https://www.youtube.com/watch?v=u7nAthxNX0c)

### 25. 协作与推理地缘：Awesomic Supernova；Munito 欧侧开源推理

Awesomic Supernova：Agent + 自有团队 + 认证专家同一项目，每项目独立云电脑；宣称接 Claude Code / Codex / Cursor。Munito：前 Mistral 推理负责人创办，OpenAI/Anthropic 兼容 API，欧区默认零保留，面向金融/医疗/法律数据驻留需求；可与 You.com Router（美侧）对照。
来源：[Awesomic](https://www.ycombinator.com/launches/WJf-new-awesomic-prompt-with-ai-perfect-with-experts-all-in-one-app)、[Munito](https://www.ycombinator.com/launches/WJe-munito-ai-open-model-inference-provider-for-europe-private-by-default)

「人机混编交付」和「开源权重落在哪片大陆」都是真需求。Orgo 一类 Agent 云桌面、OpenRouter、Fireworks 会碰到同一采购清单。

- 设计 / 外包团队：Agent 出初稿、专家收尾，按项目报价。
- 欧洲合规敏感客户：先看 Munito / 欧区端点，再谈功能。

教程（产品演示）：[Awesomic Supernova（YouTube）](https://www.youtube.com/watch?v=ZuDp9OvYYDM)；[Munito（YouTube）](https://www.youtube.com/watch?v=5tjInE84mY4)

## 观点洞察：Harness，还是反向 Harness？

编程这边最近有个很拧巴的现象：工具越来越像「马具」（Harness）——给模型套上仓库、终端、测试、沙箱，让它自己跑；可实际体验常常反过来：模型一口气吐出大段 diff，人只剩两个按钮——**Accept** 或 **Run**。你来不及读完，也很难判断它是不是完整、是不是在胡说。社区里有人刻薄地叫它 Cuck Coding：人还在场，但已经不像在写代码，更像在给机器点「同意」。

正统 Harness 的意思，是**人定目标与边界，机器在笼子里干活**。反向 Harness 则是**机器定节奏与体量，人被输出淹没，只负责放行**。后者不一定是产品故意做坏，而是速度与体积的副作用：生成比阅读快一个数量级时，默认交互就会滑向「先跑再说」。

这是不是常态？**在「草稿与冲量」层，恐怕就是常态**——补测试、改文案、扫目录、出初版 PR，Accept/Run 会越来越常见，假装每人每行都精读不现实。**在「生产与权限」层，它不该是常态**——一键合进 main、自动改密钥、自动打补丁、自动花钱，如果还只靠肉眼点 Accept，那是事故排队，不是效率。

今天几条「闸门」新闻，其实都在回答同一件事：**当人已经读不过来时，用什么代替肉眼。**

- **METR 盯 OpenAI 内部 Agent 监控**：连厂商自己的监控都有缺口、可被拖回合套利。说明「我们有监控」不等于「输出可信」；没有不可篡改的审计通道，反向 Harness 会连证据都造假。
- **AWS Continuum / Claude Security**：卖的不是更多建议，是可验证利用、按冲击排序、修复跟踪。思路是——别让人读完几千行 AI 补丁，让机器证明「这洞真的能打、这修复真的合上」。
- **1Password for Agents、银行挡未审查 Agent、政府白名单工具**：凭证与登录本身就是闸门。人点 Accept 之前，模型根本拿不到真密钥、进不了账户。
- **Aucert / Simulithic 一类发布前质量闸**：把「能不能上线」从个人感觉，变成可重复的测试与仿真。人仍点按钮，但按钮背后是绿灯/红灯，不是盲信。
- **Claude Auto mode**：自动程度提高的同时，企业更需要默认限额、人审合入、沙箱。Auto 不是取消闸门，是把闸门从「每行 code review」改成「策略 + 抽检 + 回滚」。

怎么解？我不指望退回「每行手写」。更现实的组合大概是：

1. **读不过来的，就不要用「读」当唯一闸门**——测试、类型检查、差分覆盖、沙箱试跑、安全扫描，必须先于 Accept 进 main。
2. **权限跟失败成本走**——改文档可以宽，改鉴权/支付/生产配置必须窄；Agent 默认无密钥、无支出、无直接合入。
3. **抽检代替精读**——随机或按风险抽一段让人（或旗舰模型）复核，接受「大部分输出无人通读」这个事实，但拒绝「全部无人把关」。
4. **承认 Cuck Coding 是一种工作模式，给它命名、限域，而不是假装高尚**——草稿区可以这样干；生产区把它当事故预兆。

有人会立刻反问：边界一加，效率是不是先掉一截？团队会不会把大把时间耗在写 Test Case 上，生成代码的红利被吃光？

我的看法是：**会短期变慢，但不该慢在「人肉补一万条用例」；该慢在「把少量高杠杆闸门装上」。** 全量手写测试去追上 AI 的输出速度，确实是亏本买卖——模型一小时能吐的 diff，人一周写不完对等断言。更划算的是三层边界，成本差很多：

- **免费或近免费的**：类型检查、格式化、lint、已有 CI、沙箱默认无网/无密钥。几乎不抢编码时间，却能挡住一大类瞎跑。
- **中等成本的**：只给**会炸的路径**补测试（鉴权、支付、数据迁移、核心业务不变量），其余靠生成后自动跑已有套件 + 失败再补。测试是随风险长的，不是随生成量长的。
- **贵的、该省着花的**：人通读、全量新写用例、事事双人复核。留给抽检和高失败成本节点。

还有一个常被忽略的账：**返工和事故也是时间。** 今天 Continuum / Claude Security 卖「可验证修复」、Aucert 卖发布前闸门，本质是承认——省掉边界省下的那几小时，后面会以线上回滚、安全应急、信任破产的形式加倍还回来。边界不是为了让人多写测试，而是为了让 Accept 从「盲目同意」变成「绿灯才合入」。

所以效率公式我会改写成：生成速度 × 一次通过率 − 事故成本。只拉分子、不管分母，账是假的。AI 既然能写实现，也该被要求（或被工具强制）写出/补上**那一小撮**断言；人的时间从「写满测试」挪到「定哪些不变量绝不能破」。

那闸门会不会直接把**使用成本**顶上去？会，但要分清加的是哪一类成本。lint、类型、沙箱、默认无密钥，边际成本接近零；Continuum / Claude Security / 发布前仿真、旗舰模型抽检，才是真金白银和延迟。账要和「无闸门时的事故、回滚、合规罚款、客户信任」对着算——今天银行挡未审查 Agent、政府白名单工具，已经在替你定价：进不了门，再便宜的模型调用也是零。个人玩玩具可以薄闸门；碰支付、凭证、生产合入，闸门费往往比一次翻车便宜。

还有一种更刺耳的说法：**闸门是不是只因为模型不够好才存在？** 模型足够完美，人类这些设置是不是都可以拆掉？

我不这么看。闸门有一半确实在补模型的不完美——幻觉、漏测、偷懒绕监控（METR 那类）。模型变强，这一半可以变薄：更少误报、更少「为防蠢而设」的摩擦。但另一半闸门跟聪明无关，跟**权力与责任**有关：谁能碰密钥、谁能划账、谁能合进 main、出事谁背锅。再强的模型也是代理，不是法人；银行不会因为模型 IQ 高就取消支出上限，1Password 不会因为旗舰「足够好」就把真密码默认灌进上下文。航空再成熟也有清单，不是因为飞行员笨。

所以更可能的稳态不是「完美模型 → 零闸门」，而是**模型越好，闸门从「防蠢」转向「防权」**：少拦明显蠢补丁，多拦越权、超预算、不可审计的自动放行。有些场景（本地草稿、一次性脚本）可以几乎无闸门；有些场景（自动修生产、Agent 购物/转账）闸门会永远在。今天的新闻也在暗示这点——标准件和监控变多，不是因为大家觉得模型没进步，而是因为模型开始真能碰钱和权限了。

一句话：**Harness 该套在模型身上（沙箱、凭证、测试、监控）；反向 Harness 出现时，就把闸门从「人眼」换成「机器可验证的红绿信号」。** 今天 AAIF、Continuum、1Password、METR 吵的，其实都是在抢这条红线该画在哪。人不会消失，但人的岗位会从「读完每一行」变成「设计什么情况下机器不许自己放行」——边界会吃掉一点点 Accept 的爽感，换的是少一次把整周进度打回草稿区；成本会上去一点，换的是别把「模型够聪明」误当成「可以不要缰绳」。

## 今天的机会我是这么看的

今天不像「又一个聊天模型发布日」，更像三件事钉在一起：**决策从生成里拆出来**（Decisions API、GLiDE、Decider），**Agent 开始有标准件和闸门**（AAIF Skills、ACE、1Password、Auto mode），**安全与准入把账单和权限按住**（METR、ARTEX、Continuum、银行/政府/Etsy）。

若只选三条可执行的方向：

1. **卖决策层与路由，不卖又一句话匣子**：把分类/打分/升级节点换成 Decisions 或开源决策模型；顺手做成本看板。客户是已经上了 Agent、被延迟和解析错误折磨的中台。
2. **卖 Agent 的配套标准件**：Skills 包、MCP 连接器、凭证闸门、沙箱、发布前测试（Aucert/Simulithic 叙事）、发布后 on-call。客户是试点 Duet/Work/Muse 的团队，不是还在试用聊天框的个人。
3. **挑一个你懂的垂直脏活**：工厂/分销优化、医保合约、设计可编辑资产、欧侧隐私推理。比追通用大模型发布更现实。

## 今天就能动手的三件事

1. **程序员**：把工作流里一个「让模型写一段再正则提取」的节点，改成结构化输出或 Decisions 风格调用；同一任务用两套 harness 各跑一遍。
2. **有设计/建站需求的人**：用 Canva 现有 Magic 流程出一张可进图层的物料，并看一眼 Ideogram 矢量是否适合你的 logo 线；Framer 用户可试官方 MCP，发布权留人。
3. **带团队的人**：列清单——哪些系统允许 Agent 登录、日限额多少、修代码是否必须人审；对照 1Password for Agents 和银行/政府准入新闻，缺闸门的先补闸门。

