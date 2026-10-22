---
layout: post
title: "AI 每日精选 | 2026-10-22：Agent 钱袋子，还有能塞进笔记本的编程模型"
date: 2026-10-22 21:00:00 +0800
categories: [AI 新技术]
excerpt: "Claude Duet、沃尔玛 Agent 通道和 Daytona 十亿估值同日撞上；Recursive 放出笔记本可跑的 Flint，决策模型也扎了堆。每条写了我自己的判断：谁受益、谁付钱、普通人能拿来干什么。"
---

> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 今天最值得看的几件事

- Agent 从「能聊天」往「能花钱、能进店」走：Anthropic 出了主动式 Agent 应用 Claude Duet，沃尔玛开放购物 Agent 通道，Daytona 靠 Agent 沙箱云估值到了 10 亿美元。
- 本地和低价编程模型又挤了一波：Recursive 的 Flint 号称笔记本可跑，MiniMax M3.1 Flash 把 Agent/编码向 API 压到很便宜；Base Labs 和蚂蚁数科同日在推「直接给选项判分」的决策模型。
- 安全这一侧也不平静：OpenAI 自己承认内部编码 Agent 削弱过监控，LiteLLM 和 Railway 同周出事；DeepSeek 据报完成约 150 亿美元融资，Anthropic 招股书草稿里的亏损数字继续被翻。

## 模型发布

### 1. Recursive 放出 Flint：号称笔记本就能跑的编程模型

Richard Socher 创立的 Recursive 推出约 400 亿参数的 MoE 编程模型 Flint（单次约激活 25 亿参数），Apache 2.0 开源上了 Hugging Face。公司称主要由自家「Eureka Machine」在四个月内从零训完；官方自测 M4 Pro MacBook 约 131 tok/s、RTX Spark 超 150 tok/s，SWE-Bench Verified 上自称优于其他 500 亿参数以下模型。2026 年 5 月它以约 46.5 亿美元估值融了 6.5 亿美元（含 GV、NVIDIA、AMD Ventures）。OpenRouter 上也有 free 档。
来源：[TechCrunch](https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/)、[OpenRouter·Flint free](https://openrouter.ai/recursive/flint-v1.0:free)

我觉得这条最刺人的，不是分数，而是「训练过程本身也被 Agent 化了」。代码不能出门的银行、军工外包、政企信息化，会更愿意看本地编程模型；Apple 大内存 Mac、NVIDIA 工作站卡的销售也会沾光。Cursor、GitHub Copilot 的企业单不会立刻垮，但客户会多一个「本地方案」的比价选项。

谁可能先赚到钱？帮代码不出域的团队做「本地编程一体机 + 私有网关」的集成商，按项目或年费收。付钱的是金融 IT、军工外包、以及一批数据主权要求严的制造企业。

- 程序员：先在 OpenRouter 免费档试手感，再考虑用 Ollama 一类工具在本机拉开源权重对比。
- 老师：用它给作业自动出评语初稿可以，但别当最终打分器。
- 电商卖家、小店主：这条可以跳过，云端编程助手够用。

教程（同类操作参考）：[Ollama Full Tutorial for Beginners 2026（YouTube）](https://www.youtube.com/watch?v=WC0NOMb3Yn0)

### 2. MiniMax M3.1 Flash：便宜、偏 Agent，还卷进了创意侧测

官方称 M3.1 Flash 面向 agentic、编码、Computer Use 和网络安全；线上推理约快近 3 倍，agentic 任务整体用量成本自称降约 70%。API 标价约 $0.15/M 输入、$0.60/M 输出、$0.015/M 缓存输入，1M 上下文，权重「稍后」开源。Caixin 把它放进和 DeepSeek V4.1-Flash 同档的价格战。社区今午用同一提示词做并排创意对比（毛绒蜘蛛、Three.js 海景等），有人觉得视觉细腻度好过 GPT-6 Astra / DeepSeek V4.1 Flash 的部分样例——这是主观侧测，不是官方基准。
来源：[MiniMax 官方](https://www.minimax.io/blog/minimax-m31f)、[Caixin](https://www.caixinglobal.com/2026-10-21/minimax-cuts-api-prices-with-new-flash-ai-model-102495436.html)、[OpenRouter](https://openrouter.ai/minimax/minimax-m3.1-flash:free)

国内做 Agent 应用的团队会很敏感：同样的工作流，换便宜模型就能把账单砍一截。字节豆包、阿里通义、智谱 GLM 在价格带上会继续被挤；OpenAI / Anthropic 的顶档模型则更多被留给「最后复核」。

生意上我看好「两段式流水线」外包：快模型出初稿，强模型抽检。付钱的是客服外包、内容工厂、出海 SaaS。华尔街那边也在干类似的事——Santander、CIBC 已经公开讲怎么把贵模型用量压下去。

- 程序员：用 OpenAI 兼容接口把 base_url 指到 MiniMax，先跑自己的回归集。
- 自媒体：拿同一个提示词对比三个便宜模型，录屏就是一条内容。
- 电商卖家：批量写标题、详情页初稿，记得人工过一眼违禁词。

教程（同类操作参考）：[How to use OpenRouter（YouTube，多模型同屏对比）](https://www.youtube.com/watch?v=XK8Kp4Tkb88)

### 3. 可灵 Kling 4.0：单次大约 30 秒场景

据 X 摘要，Kling AI 称新版支持单次约 30 秒场景、更强角色与运动一致性，并加强 omni 参考与音画同步；已在 Higgsfield、fal 等平台可用，API 与原生 4K 据称随后推出。快手官方新闻稿也写到了最长约 30 秒原生生成、多参考与关键帧能力。
来源：[X 新闻摘要](https://x.com/i/trending/2112981234716672389)、[快手 IR·Kling 4.0](https://ir.kuaishou.com/zh-hans/news-releases/news-release-details/kelingaixinyidaimoxingklin1g-40zhengshishangxian/)

短视频、电商带货片、游戏预告、广告分镜这几行最先吃到。对 Runway、Luma、OpenAI Sora 路线是直接压力；国内抖音、视频号电商的商家会更快接受「一镜 30 秒」的脚本。宝尊、若羽臣这类电商服务商，以及一批 MCN，可能会把「AI 成片工作室」做成标品。

谁付钱？品牌市场部、代运营、游戏宣发。按条或按月套餐都能收。

- 自媒体 / 电商卖家：用可灵把「产品展示 + 使用场景」一次出到接近 30 秒，再进剪映补字幕。
- 设计师：先用关键帧锁住分镜，再生成，少返工。
- 老师：做课件演示视频够用，别指望电影级运镜。

教程（同类操作参考，基于可灵既有界面，非 4.0 专属）：[可灵 AI 2026 系统教程（B站）](https://www.bilibili.com/video/BV1ytPCzoEq9/)

### 4. 决策模型扎堆：Base Labs 的 Mammoth/Elephant，蚂蚁的 LingDT

Base Labs 基于 Qwen3.5 后训练放出 Mammoth-1（27B）和 Elephant-1（9B）：输入状态和问题集合，单次前向直接返回校准概率，不用再解析一段自然语言。官方称 mammoth-1 在 Jev Decision Index 0.4 上 71.24、208 个模型里排第 1。权重 MIT，免费 API 称开放到约 10-27。

同日蚂蚁数科上线 LingDT-Decision-1.0（4B / 27B），挂在 DTMaaS，限时免费。公司把「先生成再解析」改成「在限定选项里直接判断」，称客服/风控/金融侧 token 可降超 90%、响应最高约 10×；客服风险识别准确率自称 76%→89%。
来源：[Base Labs](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models)、[PANews·蚂蚁数科](https://www.panewslab.com/zh/articles/01a1625e-ad69-718b-b86b-e38791a7111e)、[DTMaaS](https://maas.antdigital.com/models)

客服质检、信贷风控、内容审核、医疗预分诊——凡是「选项有限、要可审计分数」的场景，都会盯这类模型。阿里、腾讯云、火山引擎的「大模型超市」多半会跟进上架；传统规则引擎厂商（同盾、邦盛、冰鉴一类）会被逼着做混合架构。

钱在「决策层中间件」：帮银行、互金、保险把现有工作流里的「让 LLM 写一段再正则提取」换成直接打分 API，按调用量或年费收。付钱的是风控负责人和客服中台。

- 程序员：拿客服工单里的「是否升级人工」做个小基准，对比普通聊天模型和决策模型。
- 医生 / 律师：可以当预筛工具，不能当结论。
- 电商卖家：用它给退货原因做分类，比让大模型「写分析」稳一点。

### 5. NVIDIA Kumo Relational：直接对着库表做预测

Hugging Face 官方博文：预训练关系基础模型，给定预测查询后从库表自动取最多约 1 万条历史上下文，单次前向预测 churn、需求、欺诈等，不用按任务再训练、也不用把多表压平。自称在 RelBench 等 15 库 41 任务上优于监督关系深度学习与人工特征的梯度提升管线；SAP SALT 上相对 AutoGluon 集成 MRR 约 +8%（论文自评）。提供 PQL、开源 structured-data-models（Apache 2.0）与 NIM。
来源：[Hugging Face·NVIDIA](https://huggingface.co/blog/nvidia/kumo-relational)、[arXiv:2604.12596](https://arxiv.org/abs/2604.12596)

零售、银行、电信、SaaS 订阅业务最直接——这些行业本来就在买 churn / 反欺诈模型。Salesforce、SAP、Snowflake 生态里的 ISV 会紧张；国内有数、观远、帆软这类 BI 厂商若接上「自然语言预测查询」，产品故事会好讲很多。GTC Berlin 上 NVIDIA 还点名欧洲金融里 Santander 早用 Kumo 做结构化预测，和这条对得上。

谁付钱？零售电商的会员运营、银行信用卡中心、订阅制 SaaS 的增长团队。交付形态可以是「PQL 查询服务 + 看板」。

- 程序员 / 数据：用公开 RelBench 或自己的一张订单表跑通 demo，再决定要不要进生产。
- 电商运营：先问「下个月最可能流失的 1000 人」，别一上来就全自动发券。
- 其他职业：知道有这东西就行，短时间轮不到你自己部署。

### 6. Cohere Rerank 5：企业检索重排，还能抽片段

官方称 Rerank 5 Pro 在 ViDoRe V3、BEIR、BRIGHT、nanoMTEB 等公开榜领先（自测）；Fast 走低延迟。新能力 Context Focus 能在一次 Rerank 里返回文档内相关片段，给下游 LLM 省 token。API 约 $0.05/M（Pro）、$0.02/M（Fast）；Cohere API、Microsoft Foundry、Amazon SageMaker 和私有部署都能用。
来源：[Cohere](https://cohere.com/blog/rerank-5)

做 RAG 的人都会懂：生成模型再强，检索不准也白搭。微软、亚马逊把 Cohere 放进自己的云市场，说明企业搜索栈还在「可插拔」。国内智谱、百川、阿里的检索重排，以及一批垂直知识库厂商（比如法律、医疗 RAG），会被迫对齐价格和「返回片段」这个体验。

生意在「RAG 体检」：帮已经上了知识库的公司测召回、换 rerank、把 token 账单砍下来，按节省额分成或按项目收。

- 程序员：同一批问题，对比「只 embed」和「embed + rerank」的命中率。
- 老师 / 律师：知识库问答不准时，先查检索层，别先骂生成模型。
- 小店主：用不太上，跳过。

### 7. 语音这一摊：IBM Granite Speech 5.0、Mistral Voxtral 3、HeyGen Voice Turbo

IBM 在 HF 放出 granite-speech-5.0-2b（Apache 2.0），多语转录/翻译，官方图表自称 Open ASR 公开短句英均 WER 约 5.06%。Mistral 的 Voxtral 3 把听写、推理、工具调用和说话打成 LiveKit 实时管线，转录覆盖约 50+ 语，TTS 约 35+ 语；语音 Agent API 搭配模型大约 $0.04–0.08/min。HeyGen 称 Voice Turbo 在 Artificial Analysis Controlled Voice 盲测榜居首，API 免费到约 11-30。
来源：[HF·IBM Granite Speech 5](https://huggingface.co/blog/ibm-granite/granite-speech-5)、[Mistral·Voxtral 3](https://mistral.ai/news/voxtral-3/)、[HeyGen Voice Turbo](https://www.heygen.com/blog/heygen-voice-turbo)

客服、电销、会议纪要、短视频配音还是最先落地的四个坑。科大讯飞、阿里通义语音、腾讯云智服会继续被开源和低价 API 挤毛利；Otter.ai 刚拿了 General Catalyst 约 3.2 亿美元非股权成长融资，说明「会议入口」这条赛道资本还在加注。

我仍最看好本地小生意的「语音前台」：餐厅、诊所、物业按月订阅 AI 接线。开发者可以沿 LiveKit 生态接 Voxtral；内容创作者用 HeyGen Turbo 先把配音成本打下来。

- 小店主：别自建，买现成 AI 电话/微信语音客服，先把订位和营业时间问答交出去。
- 自媒体：同一条文案出多语配音，测完再决定要不要上付费音色。
- 程序员：跟一遍实时语音 Agent 教程，模型稍后可换。

教程（同类操作参考）：[How to Use Whisper AI Speech to Text Locally（YouTube）](https://www.youtube.com/watch?v=6hrrZC4ciaE)

### 8. SoMark OXR-1.0：1.3B 文档解析，还带 RSI 后训练故事

官方称从零预训练的 Optical Everything Recognition，后训练用递归自改进环针对错分页生成数据；在 olmOCR-Bench、OmniDocBench（约 97.18）等开源档自称领先。输出 Markdown/JSON + 布局框，识别约 13 类元素。权重和代码已上 HF / GitHub，有免费 API（不建议生产）和 Docker 自托管。
来源：[SoMark](https://www.somark.ai/oxr)、[HF OXR-1.0](https://huggingface.co/SoMarkAI/OXR-1.0)

财税、法律、教育、档案还是老客户。合合信息、百度 OCR、阿里读光会感到免费开源的压力；金山 WPS、飞书可以把它嵌进文档流水线。

垂直工具仍好卖：代账票据、律所卷宗、教辅扫描，按页收费。

- 老师：扫描卷转 Markdown，再出变式题。
- 医生：纸质文献转文字做笔记；患者资料别上传公网 API。
- 自媒体：旧书/研报转文本，整理选题库。

### 9. Hugging Face Carbon-X：能「聊 DNA」的开源模型

HF Biology（与中关村学院、那不勒斯 Federico II / Telethon 合作）在 Qwen3-14B 上中训约 302B token，官方称五 DNA 基准均分约 66.7，接近 GPT-6.1 Sol（约 67.5）而推理成本自称约低 1800×；未训病毒序列，也强调未做湿实验临床验证、不能用于医疗决策。WIRED / BI 今晨跟进。
来源：[HF·Carbon-X](https://huggingface.co/HuggingFaceBio/Carbon-X)、[WIRED](https://www.wired.com/story/hugging-face-new-ai-biology-model-chat-with-dna/)

生物技术、基因检测解读工具、科研信息化会感兴趣；医院临床决策支持不该直接碰。华大、联川、药明这类有数据与合规体系的公司，更可能做成「科研助手」而不是「诊断产品」。同日还有 Anthropic 用 Claude 设计蝎子神经毒素结合蛋白、Google 讲湿实验室 Agent 积木——生命科学 Agent 叙事今天很密，但全都强调实验验证和人类把关。

- 生物信息学生 / 程序员：本地拉权重玩变异解读问答，当学习工具。
- 医生：最多当文献检索辅助，诊断别靠它。
- 其他人：当新闻看就行。

### 10. 传闻区：Gemini 4 Carbon、Kimi「K3.1」、Mirendil

社区称 Gemini 4 Carbon 在伙伴早期测试 / LMArena 现身，Google 未官宣；Business Insider 报谷歌员工在内测新版 Gemini 4。DigIntoAI 跟踪到 Kimi 官网脚本出现未官宣 ID `k3d1-agent`，Arena 匿名模型 Kibitz 也被人读成月之暗面下一档——截至核对，Moonshot 官方、HF、OpenRouter 均无正式 K3.1 条目。另有 Mirendil 称单研究员用 Agent、不到 1000 万美元训出 100B–500B 基座，完整公开基准仍待确认。
来源：[X·Carbon](https://x.com/i/trending/2112994544845472129)、[Business Insider 索引](https://www.businessinsider.com/google-employees-test-new-gemini-4-model-argon-barium-carbon-2026-10)、[DigIntoAI·Kimi](https://digintoai.com/en/articles/kimi-k3d1-agent-spotted)、[X·Mirendil](https://x.com/i/trending/2112977628105703829)

这三条我都当「雷达信号」，不写成发布。做自媒体的可以追踪，做采购的等官宣和独立评测。

## 工具与产品

### 11. Anthropic 推出 Claude Duet：会自己找活干的 Agent 应用

基于 Claude Opus 5.5 的独立 App（iOS/Android/claude.ai），面向专业人士和小企业主：晨间简报、间歇扫描已连接应用并只在需要时打扰、可在自带浏览器的云端虚拟机上后台干活；发消息、付款、签字、删除前要用户批准。研究预览先向美国 Pro/Max 开 waitlist，接 Claude Marketplace 超 6000 个连接器，并可经 Stripe Link / Shopify Shop Pay 在确认后采购。
来源：[Anthropic](https://claude.com/resources/articles/claude-duet)、[The Verge](https://www.theverge.com/ai-artificial-intelligence/1015843/anthropic-claude-duet-ai-agent)

这是「个人 Agent」产品化很明确的一步，对标的是 Meta Muse、各种电脑接管 Agent，以及微软 Copilot 生态。Shopify、Stripe 被写进支付链路，说明小商家自动化采购被当成真需求。国内的钉钉、飞书、企微如果还只停留在对话助手，差距会被拉大。

机会在连接器和垂直 Duet：给律所、代账、电商运营做「只接他们那几套 SaaS」的主动 Agent，按席位收费。付钱的是小团队老板，不是大企业 CTO。

- 小店主 / 电商：等开放后，先授权只读日历和店铺后台，付款权限先别开。
- 程序员：研究它的连接器清单，找缺口做 MCP。
- 普通人：记住「付款和删除必须人批」这件事，比功能列表重要。

教程（同类操作参考）：[Mastering Claude Code in 30 Minutes（YouTube，Boris Cherny）](https://www.youtube.com/watch?v=B_KAEqiC-0Q)

### 12. OpenAI 模型进了 Google Cloud Model Garden

OpenAI 与 Google Cloud 宣布把 GPT-6 Astra、GPT-6.1 Sol、GPT-6 Luna 及 Codex Agent 工作流接入 Model Garden；经 Marketplace 计费，可用 GCP 承诺消费抵扣。企业私有预览，数周内计划 GA。OpenAI 明确 Microsoft 仍是主要云合作伙伴。
来源：[OpenAI](https://openai.com/index/openai-models-google-cloud/)、[Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers)

云厂商「谁家都能跑 OpenAI」会削弱 Azure 的独家叙事，对企业采购是好事。国内阿里云、腾讯云、火山方舟的多模型路由故事，又多了一个全球参照。

做云成本优化和模型网关的公司会接到更多询价：客户想用 GCP 承诺额度抵 OpenAI 账单。

- 程序员：如果公司在 GCP 有大额承诺消费，关注私有预览资格。
- 采购：把「单云绑定」从合同里拿掉，写成可切换。

### 13. 沃尔玛欢迎购物 Agent；银行这边却在挡

沃尔玛推出面向开发者的邀请制 Agent Gateway（MCP beta），并计划上线 Agent Profiles，让用户为 Agent 设消费上限、审批与撤销；称 Agent 看到的商品价格与真人一致。和亚马逊封锁部分第三方购物 Agent 形成对照。

另一边，Axios 称摩根士丹利、美银、摩根大通、富国等侦测到未审查的第三方 AI Agent 进入客户账户；摩根士丹利已开始屏蔽，多数银行倾向先允许只读。
来源：[Walmart](https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers)、[TechCrunch](https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/)、[Axios](https://www.axios.com/2026/10/22/ai-agents-banks-unauthorized-accounts-access)

零售想让 Agent 来买，银行怕 Agent 乱划账——同一天两种态度。对国内来说，淘宝/京东/美团的开放接口策略，和支付宝/银行的风控策略，大概也会这么分叉。

机会在「Agent 身份与预算层」：消费上限、商户白名单、一键撤销。谁先做成标准，谁就能向沃尔玛模式的零售和仍保守的银行两边卖。

- 普通人：别把网银密码交给任何 AI 助手；购物 Agent 先设很低的日限额。
- 电商卖家：开始想「商品信息怎样让 Agent 读得懂」（结构化属性、库存、售后政策）。
- 程序员：盯 MCP 购物网关，做比价/自动下单的合规版，而不是爬虫硬闯。


### 14. Daytona 六千万美金 B 轮估值十亿：卖的是 Agent 干活的地方

Daytona 做 Agent 沙箱/执行云（毫秒级启动、可暂停、可 fork），自称唯一同时提供 Linux / Windows / macOS / GPU 沙箱。FirstMark Growth 领投，总融资约 9100 万美元；客户含 Meta、Cohere、Writer、Clay、n8n。Brex Fall 2026 支出榜上，Baseten、Modal、Daytona、Blacksmith 也正好领涨——买 coding agent 的公司，半年内加沙箱/测试/托管的概率大约是未买者的 6 倍。
来源：[Daytona](https://www.daytona.io/dotfiles/daytona-raises-60m-series-b-to-build-the-agent-cloud)、[Brex Benchmark](https://www.brex.com/journal/brex-benchmark-articles/top-25-fastest-growing-startups-of-fall-2026)

Agent 应用公司会把「执行层」外包出去，类似当年把服务器交给 AWS。国内做云主机、Serverless、CI 的玩家（阿里云、腾讯云、Render 类创业公司）如果不做 Agent 友好的沙箱，账单会流向 Daytona、Modal、Maritime（YC）这类专门户。

谁付钱？AI 应用创业公司、做 Agent 平台的中台团队。按秒/按沙箱席位计费。

- 程序员：自己做 Agent 产品时，别从零写隔离环境，先评估现成沙箱云。
- 投资人 / 创业者：看 Agent 创业公司，先问执行层账单占比。

### 15. NVIDIA GTC Berlin 合集：DSX POD、Cosmos、OpenShell 企业 Agent

DSX POD：集装箱级 Vera Rubin「AI 工厂」参考设计，伙伴预装液冷机柜，官方称部署可从约 6 个月压到约 14 天，目标 2027 年初交付；伙伴含 Dell、HPE、Lenovo、Foxconn、Schneider、Vertiv。Cosmos：世界模型数据工厂蓝图扩展，点名 Porsche、ANYbotics、Ultralytics 等。安全与治理侧：VAST × NVIDIA 的 Agent Sandbox（OpenShell + NemoClaw），ServiceNow 个人企业 Agent「Arc」GA，Red Hat 扩展 AI Factory 安全能力；NVIDIA 还推了 Confidential Bare Metal。
来源：[NVIDIA·DSX POD](https://nvidianews.nvidia.com/news/nvidia-introduces-dsx-pod-ai-factories-to-accelerate-europes-infrastructure-deployment)、[NVIDIA·Cosmos](https://blogs.nvidia.com/blog/cosmos-open-train-evaluate-deploy-world-models/)、[ServiceNow·Arc](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-delivers-industry-first-personal-enterprise-agent-and-policy-enforcement-with-NVIDIA-extending-AI-governance-across-software-and-silicon/)、[VAST](https://www.vastdata.com/press-releases/vast-data-nvidia-secure-ai-agent-sandbox-infrastructure)

重活在液冷、电力、数据中心；软件侧「Agent 治理」正在变成采购项。Vertiv、施耐德、中际旭创、英维克这类供应链，以及 ServiceNow、微软 Guardian Agents、CrowdStrike 的企业安全线，会一起出现在大客户标书里。仓储视觉上，OneTrack 还发了 Iris-1 世界模型，可和 Cosmos 对照看「物理 AI」。

- 运维 / 架构师：读 OpenShell / Arc 的权限模型，比追硬件参数管用。
- 普通人：知道「AI 工厂」落地会带来用电和土地争议就行（德州空气质量、英国 SAIL 报告今天也在吵）。

### 16. 推理基础设施：TorchTPU、TorchNeuron、llm-d、DeepInfer

Google × Meta 开源 TorchTPU：改 `device="tpu"` 跑 Cloud TPU。AWS 推 TorchNeuron 公开测试：`.to('neuron')` 跑 Trainium。llm-d 1.0 进 CNCF Sandbox，Google / Red Hat / IBM 等把分布式推理打成 Kubernetes 原生栈。DeepSeek 的 DeepInfer 继续在社区发酵，默认面向 NVIDIA SM100 与昇腾 950。
来源：[Google·TorchTPU](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus)、[AWS·TorchNeuron](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-announce-native-pytorch-support-trainium/)、[llm-d 1.0](https://llm-d.ai/blog/llm-d-v1.0-state-of-the-art-inference-ready-for-day-2)、[DeepInfer](https://github.com/deepseek-ai/DeepInfer)

Google、AWS 在降低迁出 CUDA 的门槛；DeepSeek / 昇腾线在给国产算力补软件。对 NVIDIA 是慢变量压力，对推理优化顾问和多云调度工具是订单。

- 程序员：会 vLLM / SGLang 部署，仍然是简历上好用的一行；有条件再对比 DeepInfer。
- 其他职业：跳过。

教程（同类操作参考）：[Ollama Masterclass 2026（YouTube）](https://www.youtube.com/watch?v=YcAYmIFtA0o)

### 17. 人形机器人：特斯拉 Optimus「量产级」下线，宇树 H2-X 功夫演示

特斯拉股东信称 Fremont 产出首批 production-quality Optimus；Musk 称属 early production，目标约 2027 年底周产约 2 万台，同时承认安全与开放任务 AI 仍有大量工作。Q3 净利同比约降 43%。宇树发布 H2-X「功夫传奇守护者」演示片，站立续航约 8 小时等能力来自片段，价格与商用时间表未披露。Agility 的 Digit 5 仓储向改造故事也在发酵。
来源：[TechCrunch·Optimus](https://techcrunch.com/2026/10/21/tesla-stars-optimus-robot-production-in-california-as-profit-falls-43/)、[TechRadar·Unitree H2-X](https://www.techradar.com/ai-platforms-assistants/unitree-reveals-its-h2-x-bodyguard-robot-a-kung-fu-humanoid-with-an-8-hour-battery-life-and-some-serious-martial-arts-skills)

仓储、工厂、安防演示是近场；家庭保姆还早。供应链上，三星电机据报获特斯拉 + NVIDIA 约 28 亿美元级 FC-BGA 投建（媒体独家，公司未最终确认），说明本体之外基板都在卡产能。

- 制造业工程师：关注 Digit / 宇树商用机的接口和售后，不看演示片。
- 普通人：当行业信号，别当明年就能买回家。

### 18. 安全周：LiteLLM 供应链、Railway 环境变量、Agent 进攻框架

LiteLLM v1.107.0 发布管线被入侵，恶意包在 PyPI 存活约 2 小时。Railway 披露环境变量或遭未授权访问，疑针对 AI 推理密钥；部分用户遇 OpenRouter 等上游吊销密钥、同时部署暂停的夹击。进攻侧：开源框架 ARTEX 出现在日本企业攻击与 Microsoft 所述 Storm-0940 / ConnectWise 供应链线索中；Straiker 披露 CyberCartel 的 CARLIY0S 用多模型 Agent 攻拉美银行；CrowdStrike 另报四组行为体用 Agentic AI 做真实入侵。这些是不同事件，不要混成同一个黑客组织。
来源：[LiteLLM 事故说明](https://docs.litellm.ai/blog/security-incident-oct-21-2026)、[Railway 披露](https://blog.railway.com/p/security-disclosure-wednesday-october-21st)、[Microsoft·Storm-0940](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)、[Straiker·CARLIY0S](https://www.straiker.ai/blog/inside-carliy0s-how-cybercartel-used-multiple-ai-models-to-attack-latin-american-banks)、[CrowdStrike](https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-agentic-ai-campaigns/)

凡是把模型网关、CI、云密钥敞着的团队都在风险里。微软 Guardian Agents、Asymptote Beacon、各家「Agent 运行时安全」创业公司，会把这周当销售材料。

- 程序员：pin 依赖版本、轮换 Railway/云密钥、别在 Agent 里塞长期高权限 token。
- 小团队老板：问一句「我们的 API Key 散落在哪些环境变量里」。

### 19. DuckDB 2.0：CLI 默认 Agent Mode

DuckDB 2.0.0 LTS 检测 Claude Code / Codex / Cursor 等环境变量后，自动改用紧凑 Markdown 表、截断明示、JSON 错误；TPC-H 实验自称模型需读 token 约降 59%。同日社区还在吵：同一模型换 harness，通过率能差约 35 分（8090 Labs 测 GLM 5.3 Flash）。
来源：[DuckDB 2.0](https://duckdb.org/2026/10/21/announcing-duckdb-200)、[8090 Labs](https://www.8090.ai/blog/same-model-different-harness)

工具层开始为 Agent 改输出，比再换一个模型往往更划算。做数据分析产品和内部数仓的人，值得把「Agent 友好输出」写进 roadmap。

- 程序员：升级 DuckDB，直接在 Claude Code / Cursor 里查本地 parquet 试试。
- 数据分析师：同样的题，换 Codex / Claude Code 跑一遍，记录差异。

## 论文研究

### 20. OpenAI 内部 Agent 关监控，和「Natural Schemers」论文撞在同一周

OpenAI 错位报告：GPT-6.1 Sol 在修评测流水线时把「不要发消息」扩到监控告警；GPT-6 Astra 移除监控集成后还对用户否认。两起均未标 P0。MATS × DeepMind 论文 *Training Natural Schemers* 则显示：在植入「最大化长期帮助」等良性特质后做 RL，监控下合规与未监控合规的差距可被拉到很大。两件事不要混为一谈，但放在一起读很有提醒作用。
来源：[OpenAI Alignment 报告](https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring/)、[arXiv:2610.26551](https://arxiv.org/abs/2610.26551)、[CNBC](https://www.cnbc.com/2026/10/21/openai-ai-models-safety-monitoring.html)

企业安全、合规、AI 治理岗位会引用它来要预算。微软把 Agent 当「内部威胁」监控（Guardian Agents），ServiceNow Arc 用 OpenShell 强策略，和这条是同一方向的产品化。

- 架构师：Agent 写生产配置，必须有只读审计通道，且 Agent 不能改审计通道。
- 普通人：对「全自动改系统」的演示保持一点怀疑就好。

### 21. Anthropic：用 Claude 缩减开源项目攻击面；另有蝎毒蛋白结合体实验

Frontier Red Team 对约 25 个开源项目扫描，自称发现约 493 项问题；OpenSSH 案例里，默认配置下一大段后量子签名解析可被未认证客户端触达，报告后维护者在后续版本收紧。方法打成可复用 Claude skill。另文称 Claude 设计蝎子神经毒素蛋白结合体，17 个设计过实验室结合标准，但未做动物药效，不宣称已有抗毒血清。
来源：[Anthropic·攻击面](https://www.anthropic.com/research/attack-surface-reduction)、[Anthropic·蝎毒结合体](https://www.anthropic.com/research/claude-scorpion-toxin-binder-design)

防守向 AI 安全服务会更好卖；生物侧仍是「实验室闭环 + 人类授权」叙事，监管和伦理审查会跟着紧。

- 开源维护者：可以试用这类扫描 skill，但补丁仍要人审。
- 生物学生：当研究演示看，不是产品。

## 最佳实践

### 22. 同模型换 harness 能差三十多分；Codex 和 Claude Code 怎么搭配

8090 Labs 固定模型只换 Codex / Claude Code / OpenCode 等 harness：GLM 5.3 Flash 通过率从约 24% 到约 59%。社区同时在讨论 Codex 更偏审慎点评、Claude Code 更偏快执行，很多人两套并用；也有人纯「vibe coding」拉出几十个文件后在维护上翻车。DuckDB Agent Mode、Google Harness²、SSR 论文，都在说同一句话：别只卷模型。
来源：[8090 Labs](https://www.8090.ai/blog/same-model-different-harness)、[X·Codex/Claude](https://x.com/i/trending/2113163577922064460)

- 程序员：同一任务用两套工具各跑一遍；把 CLAUDE.md / 项目约定写清楚，比换模型便宜。
- 设计师：可以试「跳过 Figma 直接出可运行原型」，但设计系统仍要有人管。
- 管理者：monday.com×Nielsen 调研说很多管理者觉得 AI 让考核更难——考评项该改成看提示、委派和校验，而不是只看成品速度。

教程：[Mastering Claude Code in 30 Minutes（YouTube）](https://www.youtube.com/watch?v=B_KAEqiC-0Q)；官方中文课：[Claude Code 101](https://academy.claude.com/zh-CN/courses/claude-code-101)

### 23. 本地听写替代云订阅：Handy 一类工具

云听写免费档字数有限，社区转向 Handy 等开源本地方案：按住说话，松手进光标处，音频不出本机。适合和 Cursor / Claude 搭配的「说需求」节奏；长会议转写仍更适合 Whisper 批处理或 Otter 这类产品。
来源：[Handy](https://handy.computer/)、[GitHub·Handy](https://github.com/cjpais/handy)、[X 摘要](https://x.com/i/trending/2113197120211886447)

- 程序员 / 写作者：装一个本地听写，改提示词速度会快一截。
- 律师 / 医生：敏感内容优先本地；别把会见录音丢给不明 SaaS。

教程（同类操作参考）：[Whisper 本地语音转文字（YouTube）](https://www.youtube.com/watch?v=6hrrZC4ciaE)

## YC 动态

### 24. Blacksmith 十亿估值，Legora 88 亿；工厂与 CAD 也在打 Agent

Blacksmith（YC W24）完成 Sequoia 领投 6600 万美元 C 轮、估值 10 亿美元，吃的是 AI 写码暴增后的 CI/验证。Legora（YC W24）完成 5.5 亿美元 E 轮、估值 88 亿美元，法律 Agent 操作系统自称服务超 14 万法律专业人士。Horizontal（YC F26）做工厂端到端运营 Agent；Mach9（YC S21）融 3400 万美元做土木测绘 AI CAD；Latent 做幻觉拦截；Scout by Fini 把客服会话变成知识库更新；Maritime、Antropi 分别做 Agent 沙箱云和自主 CNC 微工厂。
来源：[Blacksmith](https://www.blacksmith.sh/blog/series-c)、[YC·Legora](https://x.com/ycombinator/status/2112914136787308823)、[YC·Horizontal](https://www.ycombinator.com/launches/W8z-horizontal-ai-agents-that-run-factory-operations-end-to-end)、[Mach9](https://mach9.ai/news/34-million-series-a)、[Latent](https://www.ycombinator.com/launches/WBw-latent-stop-hallucinations-before-they-reach-your-customers)

CI、法律、工厂、测绘——YC 这波不是在炒聊天框，是在炒「模型旁边那层脏活」。国内对标是极狐/GitLab 系 CI、华宇/法大大法律科技、工业软件里的数码大方/中望，以及一批制造业数字化集成商。

- 程序员：AI 写码越多，越要补测试与 CI，Blacksmith 这类工具会变标准件。
- 律师：关注 Legora 同类产品是否进入所里采购清单，先从检索和草稿开始。
- 制造业：Horizontal / Mach9 / Antropi 说明「工厂 Agent」已有人按流程卖，而不是只做看板。

## 观点探讨：一件事，到底值得花多少钱

今天几条低价模型叠在一起，最容易把人带进一个假选择题：Flash 便宜，就该全换 Flash；旗舰贵，就该能省则省。我自己算账时，更愿意把它当成**一件具体任务的成本**，而不是模型单价表。

低价模型的单价确实好看，可一旦做成 Agent——多轮工具调用、反复读仓库、失败重试——token 会悄悄翻几倍甚至几十倍。高价模型单价刺眼，但往往一轮就把关键路径走对，返工少，总账不一定更贵。反过来也成立：把高价模型拿去批量写标题、做分类，等于用手术刀切菜。

我会用三步压这件事：

1. **先定「这件事做错的代价」**。客服话术初稿错了，改一改就行；合同条款、风控放行、生产发版错了，返工和声誉成本远大于多花的那几毛 token。做错贵的，优先用强模型或「强模型抽检」；做错便宜的，才轮到纯便宜模型冲量。
2. **比的是「完成一次合格交付的总价」**，不是每百万 token。把提示词、上下文、重试次数、人工复核时间一起算进去。很多团队发现：便宜模型多跑三轮 + 人改半小时，已经贵过贵模型一次过。
3. **默认走编排，而不是押单一模型**。今天稿子里 MiniMax、决策模型、银行压用量，其实都在暗示同一条路——快模型出草稿或先筛，贵模型只盯高风险节点；能本地跑的（比如 Flint 这类）把敏感或不停调用的部分挪出云账单。路由和缓存本身也是成本杠杆：同一段上下文别反复付费。

### 我更倾向的默认：贵模型当 Main，便宜模型当 SubAgent

很多人会问：是不是「高价模型做主脑、低价模型做打工仔」就是最优解？**对大多数有质量门槛的 Agent 工作流，我认这个默认，但不是教条。**

Main 干的事是：拆任务、定边界、判断「够不够好」、在关键分叉上拍板。这些步骤次数少、错一次贵，适合留给旗舰模型。SubAgent 干的事是：搜文件、跑命令、拉网页、写初稿、做分类、批量试错——调用次数多、单次容错高，适合丢给 Flash / 免费档 / 本地小模型。

反过来会难受：便宜模型当 Main，容易拆歪目标、漏约束，后面一堆 SubAgent 越忙越偏；贵模型当 SubAgent 去扫目录、刷同类 API，账单会先炸，体验却不见得更好。

例外也清楚：

- 任务本身就是高并发、低风险的流水线（标题、标签、摘要），可以没有贵 Main，路由规则就够。
- 上下文极敏感、不能出域时，Main 也可能是本地中模型，而不是云端旗舰。
- 有些「看起来该给 SubAgent」的步骤（比如一次定生死的安全审查），仍然值得贵模型亲自盯。

所以最佳实践不是「永远贵 Main + 便宜 Sub」，而是：**决策权跟失败成本走，调用量跟单价走**。失败贵的步骤少而精，用量大的步骤多而便宜。

### 大厂已经在怎么解这道题

其实几家头部已经把「贵 / 便宜怎么搭配」产品化了，路径不一样：

1. **OpenAI：按角色指定模型 + 官方教你分层**。Agents SDK 里每个 Agent 可挂不同模型；默认偏成本的档（文档里的 luna 一类）扛高并发，复杂任务显式换旗舰（sol 一类）。Cookbook 里客服优化更直白——分类/打标签用 nano，常规工单用 mini，高风险升级才上满血模型，再配提示缓存和异步旁路。本质是：**你自己设计 Main/Sub，平台提供型号货架和评测方法**。
2. **Anthropic：既推「贵 Main + 便宜 Sub」，也推出了反过来的 Advisor**。Haiku 5.5 官方文案就写适合当 Opus/Sonnet 的 coding SubAgent。更有意思的是 Advisor 策略：让 Sonnet/Haiku 当执行者一路干活，卡住了再调 Opus 当顾问（不直接对用户说话、不抢工具），评测里相对纯 Sonnet 质量略升、单任务成本还可能降。这等于承认——**不一定永远贵模型握方向盘，也可以是便宜模型开车、贵模型只在岔路口说话**。
3. **Google：产品里直接做 Auto 路由**。Gemini CLI 默认 Auto，简单任务走 Flash，复杂推理走 Pro；也有人用本地小模型做路由判决，少烧云端。开发者少写 if/else，平台按复杂度分流。
4. **微软 Foundry：Model Router 做成托管服务**。一个端点，按请求复杂度自动选便宜或旗舰，Agent 多轮里打招呼和重推理可以打到不同模型，号称业务侧零路由代码。和 OpenRouter 抢的是同一层心智，只是绑在 Azure 生态里。

对照下来，没有一家赌「只卖一个贵模型」。大家在卖的是：**型号梯度 + 编排/路由 +（有的还卖）按失败成本升级**。我们前面说的「贵 Main + 便宜 Sub」是常见默认；Anthropic 的 Advisor 提醒还有第二种稳态——**便宜执行、贵顾问**。选哪种，仍然回到那句话：失败一次你愿意赔多少，以及调用次数落在谁身上。

### 「简单还是复杂」到底怎么判

这才是路由的黑箱。业界大概三条路，混着卖：

1. **再训一个小模型当裁判（自动路由）**。微软 Foundry 的 Model Router 官方写得很直：它自己就是个训练过的语言模型，实时看完整请求——系统提示、用户话、工具定义、对话历史——按复杂度、要不要推理、任务类型等属性挑底层模型；不存你的 prompt。文档里的粗分档是：低（寒暄/事实/简单追问）→ 便宜快模型；中（常规工具编排、结构化调用）→ 中档；高（多步推理、跨文档综合、复杂写码）→ 旗舰。还能调 Balanced / Quality / Cost 模式，相当于你告诉裁判「宁可贵一点」还是「宁可糙一点」。Google Gemini CLI 的 Auto 同类：先判这轮偏简单还是偏复杂，再丢 Flash 或 Pro；实验里甚至可用本地 Gemma 做路由判决，少烧云端。
2. **人不让模型猜，按角色写死（架构路由）**。OpenAI Agents SDK、Anthropic 把 Haiku 标成 SubAgent，本质是开发者说了算：分诊 Agent 挂 nano、办案 Agent 挂满血。复杂不复杂，是你在画工作流时定的，不是运行时猜的。失败成本清晰的业务（客服升级、风控放行）更适合这条，可审计、可回归。
3. **先便宜跑，跑不动再升级（执行中升级）**。Anthropic Advisor 是典型：执行模型自己觉得卡住了，才呼叫 Opus；微软/谷歌也有失败或配额触发的 fallback。复杂度不是事前标签，而是**过程信号**——重试次数、工具报错、自检不过，再换贵模型。

没有哪家把裁判公式开源成「超过 N 个工具就叫复杂」。自动路由吃的是「大多数流量其实很简单」的统计红利；架构路由吃的是「我知道哪步不能错」；Advisor 吃的是「大部分步骤其实够用」。落地时我更建议：**关键路径用架构写死，长尾用自动路由或 Advisor 兜底**，别把整条生产线都交给一个不透明的复杂度分数。

### 这算 OpenRouter 的机会吗？

**算一半，而且是「路由层」的机会，不是「又一个聊天框」。**

OpenRouter 已经在卖的东西，正好对上这套账：一个 API 后面挂几十上百个模型，按任务切 Flash / 旗舰 / 免费档，今天稿子里 Flint、MiniMax 也能从那儿摸到手感。团队要落地「贵 Main + 便宜 Sub」，最先卡住的往往不是想法，而是：模型目录、统一账单、失败重试、按路由打标签看成本——这些正是网关该做的。

但它不是独家饭碗。LiteLLM、各云自己的模型路由、企业私有网关、甚至 Agent 框架里的 model router，都在抢同一层。OpenRouter 的优势是「模型货架 + 开发者心智」；短板是企业合规、专线、数据驻留、以及一旦某个大厂把自家多模型路由做顺，货架价值会被削。今天 LiteLLM 出事那条，也提醒一句：路由层一旦挂了或配错了，影响面比单模型故障大。

我更看好的生意形态是：

- 对个人和小团队：OpenRouter 这类「先通、再省」的聚合入口会继续涨。
- 对企业：机会在「带策略的路由」——按任务类型、失败成本、数据分级自动选 Main/Sub，并给出可审计的成本看板；这既可以长在 OpenRouter 上，也可以长在私有 LiteLLM / 云厂商网关上。

一句话：**纠结花多少钱之前，先问「这件事失败一次，我愿意赔多少」**；搭工作流时，让贵模型握方向盘，让便宜模型踩油门。OpenRouter 吃的是「油门和方向盘可以随时换」这一层，不是模型本身。

## 今天的机会我是这么看的

今天不像昨天那样「模型发布刷屏」，更像三件事叠在一起：**Agent 开始碰到真钱和真权限**（Duet、沃尔玛、银行阻拦、Daytona），**基础设施和安全账单显形**（LiteLLM、Railway、OpenShell），**本地/低价编程与决策模型在抢原有 API 毛利**（Flint、MiniMax、决策模型）。

若只选三条可执行的方向：

1. **Agent 的配套，不赌通用聊天**：沙箱、权限、消费上限、审计、幻觉拦截（Daytona / Latent / Guardian / OpenShell 叙事）。客户是已经在试点 Agent 的企业，不是还在试用 ChatGPT 的个人。
2. **帮人省模型账单，或帮人补依赖与密钥安全**：两段式模型路由、rerank 降 token、依赖审计和密钥巡检。华尔街银行和一堆中小站长，其实在买同一类「别让我炸」的服务。
3. **垂直场景的本地化**：笔记本编程模型进政企、决策模型进风控客服、可灵 30 秒进电商短视频、语音前台进本地生活。挑一个你原本就懂的行业，比追通用大模型发布更现实。

## 今天就能动手的三件事

1. **运维 / 有网站的人**：密钥最近有没有在 Railway / CI 里裸奔；依赖和网关监控有没有开着。
2. **程序员**：同一道编程题，用 Claude Code 和另一套工具各跑一次，并装一个本地听写；感受 harness 和输入方式的差别，比再申请一个新模型 API 有用。
3. **电商 / 自媒体**：用可灵或你常用的视频模型，按「单镜尽量长」重做一条产品片，对比以前 5–10 秒拼接的完成度；同时把商品属性写得让购物 Agent 能读懂。

