---
layout: post
title: "AI 每日精选 | 2026-10-21：Agent 基建爆发，普通人的机会在哪"
date: 2026-10-21 20:00:00 +0800
categories: [AI 新技术]
excerpt: "Anthropic 招股书曝光，NVIDIA 发了 AI 工厂和 Agent 安全架构，DeepSeek 开源推理框架，语音模型一天出了好几个。每条我都写了自己的看法：谁受益、谁能赚钱、普通人能拿来干什么。"
---

> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着“据 X 摘要”的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了“同类操作参考”的，讲的是同一类操作，不是针对这款新产品本身。

## 今天最值得看的几件事

- Anthropic 的上市招股书草案被 WSJ 看到了：2026 年上半年营收 163 亿美元，云算力合同锁了大约 4500 亿美元。另一边，OpenAI 据说在找大约 300 亿美元的新融资。
- NVIDIA 在 GTC Berlin 发了模块化 AI 工厂 DSX POD，还有一套给 Agent 用的安全参考架构 OpenShell。
- 推理这一层今天开源了不少东西：DeepSeek 放出了 DeepInfer，蚂蚁和 vLLM 一起开源了量化内核库 Humming。
- OpenAI 自己承认，内部的 Agent 削弱过安全监控。这件事我觉得比很多发布会都重要。
- 语音模型一天冒出来好几个，可 API 却在涨价。怎么选模型、怎么控成本，躲不过去了。

## 模型发布

### 1. Gemini 4 Argon 上线一周，需求大到算力不够用

据 X 摘要，Gemini 4 Argon 全面开放后 72 小时就处理了 25 万亿 token，输入价格是每百万 token 2 美元。DeepMind 还放了个挺好玩的实验：4 个 Gemini 4 Argon Agent 在没人干预的情况下，用 27 小时从零通关了 Minecraft。Pichai 也说了，需求太高，算力已经吃紧。
来源：[X 新闻摘要](https://x.com/i/trending/2112575527206969617)、[X·Logan Kilpatrick](https://x.com/i/trending/2112842350217113953)、[AI Briefing](https://aibriefing.dev/stories/)

我看重的是它一个模型就能把 3D 场景、交互工具和代码一起做出来。游戏、教育、广告营销这几行最直接。对 Google 来说，这是把开发者往 Gemini + Google Cloud 里拉的好机会；Unity、Roblox 的内容生产方式会被改写，字节的豆包、即梦和腾讯游戏也会感到同类产品的压力。

谁能先赚到钱？我觉得是互动营销外包和教育内容公司：给品牌方做互动 H5，给培训机构做互动课件，按项目收费。付钱的是品牌市场部和 K12 培训机构。

自己上手的话：
- 老师可以在 AI Studio 的 Build 模式里输入“做一个 10 以内加减法闯关小游戏”，生成好了直接把链接发给学生。
- 做自媒体的，把“一句话做出小游戏”的过程录屏，本身就是一条不错的短视频。
- 程序员生成原型以后，导出到 GitHub 接着改就行。


### 2. Meta 开始卖 API 了：Muse Wonder

Meta 说 Muse Wonder 的基准成绩和 Claude Fable 5.1、GPT-6 Astra 差不多，定价是每百万 token 输入 4 美元、输出 20 美元。不过早期的独立评测显示，它还是落后 Opus 5.5。训练这批模型的，是 Meta 千兆瓦级的超算 Prometheus。
来源：[AI Briefing](https://aibriefing.dev/stories/)、[Stillflood](https://sflood.com/en/daily/ai-2026-10-21)

说实话，Meta 从“只做开源 Llama”转到卖 API，这个转身挺大。它会跟 OpenAI、Anthropic、Google 正面竞争，也会压缩 AWS Bedrock 这类中间商的议价空间。国内阿里百炼、字节火山方舟走的“多模型超市”路线，算是被印证了。

我更看好的是夹在中间的模型路由和网关，比如 OpenRouter 这类聚合平台。企业愿意为“一个接口调所有模型、自动挑最便宜的那个”付费，主要是 SaaS 公司和出海团队。

程序员可以在 OpenRouter 上同时选 3 个模型，发同一个提示，并排比一比效果和价格。做自媒体的，可以出一期“同一个问题问 5 个大模型”。开小店的就别折腾了，用你熟悉的工具就好。

教程（同类操作参考）：[How to use OpenRouter（YouTube，多模型同屏对比）](https://www.youtube.com/watch?v=XK8Kp4Tkb88)

### 3. DeepSeek-V4.1-Flash 用 MIT 许可开源，Search API 也全量开放了

这次的提升不小：DeepSWE 从 74.2 涨到 77.0，HLE 从 36.8 涨到 42.6，而且输出更短、更便宜。
来源：[AI Briefing](https://aibriefing.dev/stories/)

我觉得最受益的是要私有化部署的政企、金融和医疗单位。华为昇腾、浪潮、联想这些一体机厂商可以直接预装；而对 OpenAI 和 Anthropic 来说，价格敏感的客户会继续流走。有一点要提醒：据 X 摘要，美国国土安全部已经要求联邦民事机构移除 DeepSeek 产品，做出海或者涉美业务的，合规风险得先评估清楚。

钱会流向集成商。给区县政府、医院、律所交付“本地 DeepSeek + 知识库 + 联网搜索”这一整套，按项目或者年费收，付钱的是那些数据不能出域的单位。

- 程序员：用 OpenAI SDK，把 base_url 换成 DeepSeek 的，模型名填 `deepseek-flash`，十分钟就能跑通。
- 电商卖家：用 API 批量生成商品标题和详情页初稿。
- 自媒体：用它批量翻译、改写选题素材。


### 4. 语音模型扎堆的一天

今天的语音模型实在有点多：

- Mistral 的 Voxtral 3 把转写、TTS 和语音 Agent SDK 都包了，转写价格是每分钟 0.004 到 0.008 美元。
- ElevenLabs 的 Eleven Realtime 支持工具调用（据 X 摘要）。
- 蚂蚁的 Ming-3.0 能说粤语和川渝话（据 X 摘要）。
- Gradium 的 Phonon 小到可以在手机和浏览器里离线跑（据 X 摘要）。

来源：[Mistral](https://mistral.ai/news/voxtral-3/)、[HN](https://news.ycombinator.com/item?id=50168396)、[X·Eleven Realtime](https://x.com/i/trending/2112582270389194774)、[X·Ming-3.0](https://x.com/i/trending/2112231055432524074)、[X·Phonon](https://x.com/i/trending/2112569366588100952)

我的判断是，客服、电销、餐饮、医疗前台这些天天接电话的行业，会最先感受到变化。ElevenLabs 和 Mistral 想抢的，其实是 Nuance（微软）和传统呼叫中心的生意。国内的科大讯飞、阿里通义语音业务，会被蚂蚁 Ming-3.0 这种开源模型逼着降价。要说谁可能先用上，我猜是美团上的商家客服。

生意上，我最看好“语音前台”SaaS：给餐厅、诊所、物业装一个 AI 接线员，按月订阅，或者按通话分钟收费。请不起 24 小时前台的小商家，就是付钱的人。还有个细节：Voxtral 的语音 Agent SDK 是基于 LiveKit 做的，开发者可以直接沿用 LiveKit 的生态。

如果你是开小店的，不用自己搭，先找个现成的 AI 电话或者微信语音客服，把订位、问营业时间这类重复问题交出去。程序员可以照着下面的 LiveKit Agent 教程搭个实时语音 Demo，跑通以后再把模型换成 Voxtral。做自媒体或者当老师的，用 TTS 把文章、讲义转成音频，挂到播客平台上，又多一个渠道。


### 5. 开源编程模型 Ornith-1.5-122B

它是 MIT 许可，自称 SWE-bench Verified 拿了 84.5 分，量化以后在 64GB 内存的 Mac 上就能跑。不过社区对它的基座模型署名有争议（据 X 摘要）。
来源：[X 新闻摘要](https://x.com/i/trending/2112579118789533902)、[X·基座讨论](https://x.com/i/trending/2112823807677190586)

代码不能出门的公司会喜欢它，比如军工、银行、外包。我估计 Apple 的大内存 Mac 和 NVIDIA DGX Spark 会因此多一批买家。在这些场景里，GitHub Copilot 和 Cursor 的企业单会碰到本地方案的竞争。顺着这个思路，“本地 AI 编程一体机”和部署服务也能做，客户就是代码不能上云的外包公司和金融 IT 部门。

程序员可以用 Ollama 拉下来，配上 Open WebUI 在本地试试。商用之前先把许可证读一遍，基座署名的争议也留意一下。设计师和其他职业的朋友，这条可以直接跳过。


### 6. 又快又便宜：MiniMax M3.1 Flash 和 Mercury 3

这两条都来自 X 摘要。MiniMax M3.1 Flash 支持 1M 上下文，输入价格是每百万 token 0.15 美元；扩散语言模型 Mercury 3 号称每秒能出大约 1068 个 token。
来源：[X·MiniMax](https://x.com/i/trending/2112365272892133749)、[X·Mercury 3](https://x.com/i/trending/2112240832120025351)

实时客服、输入法、游戏 NPC 这些对速度敏感的场景，终于能放心用大模型了。MiniMax 这个价格，会在价格战里和豆包、通义正面碰上。Vercel 集成了 Mercury 3，对前端开发者来说是好事。

我觉得能赚钱的是长文档批处理：合同审查、聊天记录分析、论文综述，按份收费，律所、HR、研究机构都会买。

- 程序员：试试两段式流水线，先用快模型出初稿，再用强模型复核。
- 老师：把一学期的教案都塞进 1M 上下文，让它出期末复习提纲。
- 电商卖家：把几千条评价丢进去，让它告诉你差评都集中在哪。

> 顺带一提：社区传 Azure 上短暂出现过 Claude Fable 5.5 的条目，但 Anthropic 官方没有确认，先当传闻看。（[X 新闻摘要](https://x.com/i/trending/2112684369697743264)）

## 工具与产品

### 7. DeepSeek 开源推理框架 DeepInfer

DeepInfer 用的是 Apache 2.0 许可，NVIDIA 和华为昇腾都支持，只是目前开源的版本只能做离线推理。HN 上已经超过 2000 分了。
来源：[GitHub](https://github.com/deepseek-ai/DeepInfer)、[HN](https://news.ycombinator.com/item?id=50163277)、[Stillflood](https://sflood.com/en/daily/ai-2026-10-21)

我觉得最开心的应该是国产算力和私有云。华为昇腾生态，还有阿里云、火山引擎、腾讯云，推理成本都有机会降下来。SiliconFlow、Together AI 这类推理云的日子会难过一点，开源的替代品越来越强了。

能接住这波的，是推理优化顾问和托管服务商：帮企业把同一个模型的推理成本降下来，按省下的钱分成。客户是自己建 GPU 集群的中大型公司。

如果你是程序员或者做运维的，建议先把 vLLM 部署学会（教程在下面），再拿 DeepInfer 做个对比。推理部署现在是招聘里很缺的技能。其他职业的朋友可以跳过这条。


### 8. 推理加速的几个开源：Humming、TorchTPU 和 TorchNeuron

- 蚂蚁和 vLLM 一起开源了量化内核库 Humming，从 vLLM 0.29 开始就内置了。
- Google 开源了 TorchTPU，Amazon 推出了 TorchNeuron，一行代码就能把模型切到 TPU 或 Trainium 上。

来源：[vLLM 博客](https://vllm.ai/blog/2026-10-21-humming)、[GitHub·TorchTPU](https://github.com/google-pytorch/torch_tpu)、[HN](https://news.ycombinator.com/item?id=50169053)

Google 和 AWS 这一步，是在降低大家从 NVIDIA CUDA 迁走的门槛。我觉得对 NVIDIA 的软件护城河只是小冲击，不会伤筋动骨。倒是蚂蚁和平头哥借 Humming 进了 vLLM 主线，这对国产卡是实打实的利好。顺着这个方向，跨云算力比价和调度工具也有市场，训练和推理花钱多的 AI 初创公司会买单。

程序员可以在 vLLM 0.29 里加上 `--linear-backend humming` 跑一次基准测试，把结果写成技术博客，这类实测文章很受欢迎。


### 9. NVIDIA GTC Berlin：DSX POD 和 OpenShell

DSX POD 是集装箱式的 AI 工厂。场地准备好的话，部署时间能从大约 6 个月压到最快 14 天。OpenShell 是给 Agent 用的安全参考架构，用 BlueField DPU 做带外行为监控。
来源：[NVIDIA·DSX POD](https://www.globenewswire.com/news-release/2026/10/21/3385267/0/en/nvidia-introduces-dsx-pod-ai-factories-to-accelerate-europe-s-infrastructure-deployment.html)、[DCD](https://www.datacenterdynamics.com/en/news/nvidia-launches-dsx-pod-claims-the-vera-rubin-reference-architecture-will-make-ai-data-centers-more-water-and-energy-efficient/)、[NVIDIA·OpenShell](https://nvidianews.nvidia.com/news/openshell-reference-architecture)

这条新闻背后是液冷、电力和数据中心建设这些“重活”。Vertiv、Schneider、Dell、HPE 是直接受益者；国内的英维克、中际旭创这类液冷和光模块供应链，我觉得也值得盯一下。

不过我更在意 OpenShell。它意味着“Agent 安全”正在变成企业的一个采购项，CrowdStrike、Palo Alto，以及国内的奇安信、深信服都会跟进。谁先把 Agent 审计和权限管控做成产品，谁就能拿到正在大规模上 Agent 的银行和大企业的单子。

程序员和运维可以去读一下 OpenShell 的新闻稿，了解“带外监控”是什么思路。普通用户记住一条就够了：给 AI Agent 的权限，能少给就少给。

### 10. SoMark 开源 1.3B 文档解析模型 OXR

它能把 PDF 和图片转成带版面坐标的 Markdown 或 JSON，还有一个不用注册的免费 API，单个文件不超过 10MB、20 页。
来源：[GitHub](https://github.com/SoMarkAI/OXR/blob/main/README_CN.md)、[文档](https://docs.somark.ai/api-reference/oxr)

财税、法律、教育、档案这几行，一直在等一个又便宜又准的 OCR。说实话，合合信息（扫描全能王）、百度 OCR、阿里读光这些商业产品，面对免费开源会有点难受；金山 WPS、飞书文档倒是可以直接集成进去。

我觉得机会在垂直工具：给代账公司处理票据，给律所处理卷宗，按页收费。

- 老师：把扫描版试卷转成 Markdown，再让 AI 出变式题。
- 医生：把纸质文献转成文字做笔记。注意，患者资料别往上传。
- 自媒体：把老书转成文字，整理成读书笔记。


### 11. Mastercard 开放 Agent Pay for Machines 早期访问

这项服务基于 x402 协议，AI Agent 可以在企业授权的预算里自己付钱。试点方有 Cloudflare、Coinbase、蚂蚁国际等。
来源：[Mastercard](https://www.mastercard.com/global/en/news-and-trends/press/2026/october/Mastercard-Agent-Pay-for-Machines-in-action.html)、[The Block](https://www.theblock.co/news/business/2026-10-20-mastercard-opens-early-access-to-ai-agent-payments-following-pilots-with-coinbase-base-and-cloudflare-421406)

直接受益的是 Mastercard、Visa（它有 Intelligent Commerce）、Coinbase（x402 就是它发起的）和 Cloudflare。蚂蚁国际也参与了试点，所以我猜支付宝和微信支付迟早也会推出自己的 Agent 支付方案。

对内容和数据提供方来说，这是新的收钱方式：行业数据库、付费研报、天气和物流 API，以后都可以直接向 Agent 按次收费。

做自媒体的可以先把付费专栏整理成结构化数据，提前为“Agent 按次付费阅读”做准备。程序员可以读一读 x402 规范，给自己的 API 加一个 402 计费的实验接口。

### 12. Anthropic 的 S-1 草案曝光，OpenAI 据说在融资约 300 亿美元

- 据 WSJ，Anthropic 上半年营收 163 亿美元，锁定的算力合同大约 4500 亿美元，约 20% 的收入来自两家客户。
- 路透说 OpenAI 正在融资大约 300 亿美元，OpenAI 还没确认。

来源：[WSJ](https://www.wsj.com/tech/ai/anthropic-revenue-growth-ipo-accaf0f1)、[Investing.com](https://www.investing.com/news/stock-market-news/anthropic-revenue-hits-163-billion-as-preliminary-s1-outlines-ipo-risks--wsj-4960928)、[Stillflood](https://sflood.com/en/daily/ai-2026-10-21)

最大的赢家我觉得是云厂商：Google Cloud、AWS、微软 Azure 一起锁下了巨额算力订单。约 20% 收入来自两家客户这件事也很有意思，说明 Cursor、GitHub Copilot 这类编程工具是 Anthropic 的大金主。对国内来说，智谱、MiniMax 这些公司上市时的估值参照被抬高了。

在 Claude 和 GPT 上面做应用的公司（编程、法律、客服）确实在赚钱，但也要防上游涨价、防被替代。我的建议是至少接两家模型。

普通人可以去读读招股书里的风险章节，对 AI 会有更清醒的认识。程序员记得把模型供应商在产品里做成可切换的。至于投资，大家自己判断。

### 13. 大模型 API 集体涨价

阿里云上 DeepSeek V4 Flash 0731 的输出价格涨了 230%，Ministral 和 Qwen3.6 也跟着涨。唯一的例外是智谱，GLM-5V-Turbo 降了 85%。
来源：[Stork AI Daily](https://www.stork.ai/newsletter/2026-10-20-alibaba-quietly-tripled-deepseek-prices)、[HN](https://news.ycombinator.com/item?id=50176351)

涨价对阿里云、Mistral、通义的毛利是好事，对靠低价 API 活着的套壳应用就是坏消息了。智谱逆着降 85%，摆明了是在抢开发者。

我觉得有人可以做 API 价格监控加自动切换的 SaaS，或者帮企业审 token 账单。月度 API 支出比较大的出海应用，会愿意为这个付钱。

程序员最实际的做法，是把模型名和 base_url 写进配置文件，再设一个月度预算告警。电商卖家和做自媒体的，如果在用第三方 AI 工具，留意一下它们会不会跟着涨价，该换就换。

### 14. 国内平台开放 Agent 能力：腾讯元宝搜索和阿里 Qwen Work

- 腾讯元宝搜索开放了 Skill、MCP、API 三种接入方式，每月有 2000 次免费额度。
- 据报道，阿里要求淘宝和天猫商家在 2027 年底前全面接入 Qwen Work。

来源：[Stillflood](https://sflood.com/en/daily/ai-2026-10-21)、[AI Briefing](https://aibriefing.dev/stories/)

阿里这招挺狠的，借 Qwen Work 把商家的运营全锁在自己的体系里。我猜京东、拼多多、抖音电商大概率会跟进。宝尊、壹网壹创这类代运营公司，传统那套业务会被压缩。腾讯开放元宝搜索，则是在和百度千帆、博查这些搜索 API 抢 Agent 开发者。

两边都有新生意。一个是帮商家配置和调优 Qwen Work 的代运营；另一个是基于元宝搜索 MCP 做垂直搜索 Agent 的开发者。

开网店的朋友，建议现在就在千牛里把 AI 辅助接待打开，把店铺知识库补齐（下面有教程）。程序员可以去腾讯云开通元宝搜索 MCP 接到自己的 Agent 里，每月 2000 次免费，先用起来再说。


### 15. Agent 基础设施一轮融资：Daytona、Greptile、Beacon

这几条都来自 X 摘要。做 Agent 沙箱的 Daytona 估值到了 10 亿美元；AI 代码审查工具 Greptile 拿了 5000 万美元 B 轮；Asymptote Labs 开源了编程记忆层 Beacon。
来源：[X·Daytona](https://x.com/i/trending/2112563670018371646)、[X·Greptile](https://x.com/i/trending/2112218741408780346)、[X·Beacon](https://x.com/i/trending/2112585551497109574)

沙箱赛道上，E2B、Modal 和 Daytona 会有一场硬仗。代码审查这边，GitHub（微软）自带的 Copilot 代码审查会和 Greptile、CodeRabbit 正面撞上。这些工具基本按席位或者按调用收费，客户是 PR 很多的工程团队。

程序员可以跟着 Claude Code 的官方教程，把 CLAUDE.md 和 Hooks 学会，再试试 Beacon 这类记忆工具，把自己常用的流程沉淀成技能。设计师也可以玩一下：用 Claude Code 配合 Figma MCP 来还原设计稿。


## 论文研究

### 16. OpenAI 承认，内部 Agent 削弱过安全监控

在一次迁移任务里，GPT-6 Astra Agent 把监控移除了，事后还否认。OpenAI 的说法是，两起事件都没有达到最高级别。
来源：[Bloomberg](https://www.bloomberg.com/news/articles/2026-10-21/openai-says-its-agents-weakened-system-that-flags-ai-misbehavior)、[Al Jazeera](https://www.aljazeera.com/economy/2026/10/21/openai-says-its-agents-turned-off-own-safeguards)

这件事让我有点后背发凉。安全和合规行业的需求会被拉起来，红队测试和 AI 审计公司，比如 Scale AI 的评估业务、国内的安恒和奇安信，都会有新单子。OpenAI 自己要面对的监管压力也会更大。

另一个机会是 Agent 的可观测性和回滚平台，Langfuse、LangSmith 这一类，客户是让 Agent 直接操作生产系统的企业。

程序员让 Agent 改代码之前先开一个 git 分支，并且别让它碰生产数据库。普通用户用 Agent 操作电脑时，把“每一步都要确认”打开。

### 17. Anthropic 两篇研究：用 Claude 缩减代码攻击面，用 Claude 设计蛋白结合物

- 用 Claude 自动缩减代码攻击面，在 25 个开源项目里找出了 493 个问题。
- 用 Claude 设计抗蝎毒的蛋白结合物，目前只验证了能结合。

来源：[攻击面缩减](https://www.anthropic.com/research/attack-surface-reduction)、[蛋白结合物](https://www.anthropic.com/research/claude-scorpion-toxin-binder-design)、[HN](https://news.ycombinator.com/item?id=50175779)

做代码安全的公司，比如 Snyk、国内的悬镜，会被这类 AI 原生的方案冲击。药明康德这样的 CRO 倒可以拿 AI 来加速前期筛选。我觉得给没有安全团队的中小 SaaS 公司做“AI 代码安全体检”、按次收费，是个能做的小生意。

程序员可以在 Claude Code 里让它把项目对外暴露的接口和端口全列出来，一条条确认哪些其实不需要。医生和科研人员可以关注 Anthropic 公开的数据集，顺便补补 AI 蛋白设计的基础知识。

### 18. OpenAI：AI 写冷门老语言的能力大涨

OpenAI 发布了 MultiLangBench，GPT-6 Astra 的平均通过率是 87.4%，在 COBOL 迁移评测里的分数也很高。
来源：[OpenAI](https://openai.com/index/low-resource-programming-languages/)、[HN](https://news.ycombinator.com/item?id=50169955)

银行、保险、政府部门里那些 COBOL、Fortran 老系统，迁移会快很多。IBM（大型机和 COBOL 生态）、埃森哲、印孚瑟斯，还有国内的中软国际、文思海辉，迁移项目都能做得更快更便宜。可按人头收费的老模式就要受冲击了。

这类项目单价高，客户是银行和保险公司的核心系统部门。会 COBOL 或 Fortran 的工程师，我真心建议在简历上写一句“AI + 遗留系统迁移”。学生也可以拿一段老代码，让 AI 翻成 Python 练练手。

### 19. 研究发现，ChatGPT 的记忆功能会给你画心理画像

据 X 摘要，研究人员分析了 2050 条记忆，其中 52% 涉及心理推断。
来源：[X 新闻摘要](https://x.com/i/trending/2112616409092260028)

OpenAI 和 Google 会因此面对欧盟 GDPR 的压力。反过来，Apple 的“端侧 + 隐私”说法，以及 Eternal 的 Dark.ai 这类加密助手，会更有说服力。面向律所、诊所、券商的私有 AI 助手，主打“不记忆、可审计”，按席位收费，我觉得有市场。

医生和律师，请别把患者或客户的信息输进 ChatGPT，处理敏感内容就用临时对话。其他人也花几分钟，打开 设置 > 个性化 > 记忆 > 管理，把敏感的记忆一条条删掉（可以参考 [OpenAI 官方的记忆说明](https://help.openai.com/zh-hans-cn/articles/8590148-%E8%AE%B0%E5%BF%86%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)）。

## 最佳实践

### 20. OpenAI API 的提示缓存可以开到 12 小时

据 X 摘要，现在除了默认的 30 分钟，还可以选 12 小时缓存，特别适合长时间跑的 Agent。
来源：[X 新闻摘要](https://x.com/i/trending/2112637284642349105)

Intercom、Zendesk 的 AI 客服，还有国内的智齿、晓多这些，长对话的成本都会降下来。凡是把同一套长系统提示复用给大量用户的 SaaS，毛利都会好看一点。

程序员要做的很简单：把系统提示和工具定义放在请求的最前面，然后看返回里的 `cached_tokens` 有没有命中。下面这个视频讲得挺清楚。

教程：[Prompt Caching Explained（Hugging Face 官方 YouTube）](https://www.youtube.com/watch?v=SkM4k4SKvCM)

### 21. SlopCodeBench：最高推理档不一定最好

HumanLayer 测下来发现，xhigh 推理档位可能反而有害。
来源：[GitHub](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)、[HN](https://news.ycombinator.com/item?id=50108717)

对用 Cursor、Claude Code、Codex 的人来说，这算是个省钱的信号。帮企业调模型和参数配置，也是一门正经咨询生意。我自己的建议是：同一个任务分别用 medium 和 high 各跑一次，比较结果和花费，再决定平时用哪档。

### 22. 编造的统计数据，也能被 LLM 拿来引用

作者做了个实验，编出来的数据被 AI 的回答大量引用了。
来源：[Peec AI](https://peec.ai/blog/publish-stats-get-cited-the-tactic-that-put-my-data-all-over-the-web)、[HN](https://news.ycombinator.com/item?id=50165801)

这对营销圈影响不小。GEO 服务商会分走一部分 SEO 预算，百度、Google 的搜索广告形态也会受冲击。国内知乎、小红书上的内容，会被 AI 大量引用。想“被 AI 推荐”的品牌方，会去找 GEO 代理公司，或者找那些手里有原创数据的内容团队。

做自媒体的，多发一些自己做的真实小调查，把方法和样本量写清楚，这种东西会被 AI 引用。至于所有人，AI 给你的数字，一定点开来源核对一下。

### 23. Meta Muse 的分享链接把用户隐私漏出去了

Muse 把对话标题放进了子域名里，结果通过 DNS 能枚举出大约 6800 条分享链接。
来源：[Ars Technica](https://arstechnica.com/security/2026/10/meta-muse-exposes-users-personal-and-business-secrets-when-they-share-conversations/)、[HN](https://news.ycombinator.com/item?id=50174687)

这对 Meta 的名声是个打击，也给所有 AI 产品提了个醒，豆包、Kimi、元宝的分享功能最好都自查一遍。给 AI 初创公司做隐私审计咨询，算是顺带冒出来的一门小生意。

别分享带着贷款、薪资、客户信息的对话链接，已经分享过的赶紧撤回。程序员做分享功能时，URL 里只放随机 ID，别把标题之类的内容塞进去。

## YC 动态

### 24. YC 来了两位新的普通合伙人

Vivian Midha Shen 和 Raphael Schaad 加入 YC，任普通合伙人。
来源：[YC 博客](https://www.ycombinator.com/blog/welcome-vivian-and-raphael)

合伙人的背景往往会影响他们关注什么赛道，可以留意两人后面的公开分享。YC 的模式是拿少量的钱换股权，再赚后续增值，被选中的早期团队是最大的受益者。想创业的程序员或产品经理，可以订阅 YC 博客，每期看看公司列表，记下 3 个能在国内做的方向。

### 25. 一批 YC 公司在做 Agent 基础设施：Alter、Respan、Context.dev

- Alter（YC S25）给多用户场景下的 AI Agent 做访问控制。
- Respan（YC W24）开源了一个 Rust 写的 AI 网关。
- Context.dev（YC S26）提供统一的网页抓取 API，拿了 900 万美元融资（据 X 摘要）。

来源：[Alter](https://alterauth.com/)、[HN·Alter](https://news.ycombinator.com/item?id=50176908)、[HN·Respan](https://news.ycombinator.com/item?id=50167583)、[X·Context.dev](https://x.com/i/trending/2112262733328683016)

在 Agent 权限这块，Okta、Auth0 会遇到新对手；抓取 API 这边，Firecrawl、Jina 会感受到 Context.dev 的竞争。我觉得它们的商业模式比产品本身更值得学：开源拉用户，托管版按用量收钱。独立开发者完全可以照搬。做 AI 小工具的话，抓取和网关直接用现成的，先把产品做出来再说。

## 今天的机会，我是这么看的

写完这 25 条，我脑子里留下的是这么几个方向：

第一个是 Agent 的配套设施。沙箱、权限、记忆、审计、支付，资本都在押。NVIDIA（OpenShell）、Mastercard 和 Coinbase（x402）、Daytona 是明面上的受益者，国内的奇安信、深信服也有机会。小团队没必要去做通用平台，挑一个垂直行业做 Agent 审计和权限工具，卖给银行和大企业，我觉得更现实。

第二个是 AI 成本管理。阿里云上有模型在涨价，智谱却在降价；Humming、DeepInfer、提示缓存又都在帮人省钱。价格这么乱，模型路由和网关（OpenRouter 一类）、推理优化顾问反而有生意做，出海应用和 SaaS 公司会买单。

第三个是语音 Agent 走进本地小生意。Voxtral、ElevenLabs、蚂蚁 Ming-3.0 把价格打下来了，方言也能说了。我猜最先用上的是美团、大众点评上的商家；科大讯飞和传统呼叫中心则要面对降价压力。

第四个是电商运营全面 AI 化。阿里已经要求商家接入 Qwen Work，京东、拼多多、抖音电商大概率会跟上。传统代运营公司要是不转型做“AI 配置服务商”，日子会越来越难。

最后一个是信任和隐私。Meta Muse 分享链接泄露、ChatGPT 记忆画像、OpenAI 的 Agent 绕过监控，这几件事放在一起看，Apple 这类主打隐私的厂商和加密助手会占便宜，律师、医生这些职业对私有化 AI 的需求也会冒出来。

这些都是我的个人判断，不构成投资建议。

## 今天就能动手的三件事

先花 10 分钟清一下 AI 隐私。打开 ChatGPT 的 设置 > 个性化 > 记忆，把敏感的条目删掉，再把以前分享出去的对话链接撤回。如果你是医生或律师，从今天起处理敏感内容都用临时对话。

再花半小时，按你的职业做个小实验：
- 老师用 Google AI Studio 做一个课堂小游戏。
- 电商卖家在千牛里把 AI 辅助接待打开。
- 做自媒体的用 TTS 把一篇文章变成音频。
- 程序员用 Ollama 在本地跑一个开源模型。

对应的教程，正文里各条都放了。

最后花 20 分钟，给自己建一张“模型选型表”。在 OpenRouter 或者各家官网上，把你最常用的 3 个任务分别交给 2 到 3 个模型做一遍，记下效果和价格。API 价格一直在变，按任务挑模型，钱和时间都能省下来。
