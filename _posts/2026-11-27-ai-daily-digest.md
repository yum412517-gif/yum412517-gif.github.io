---
layout: post
title: "AI 每日精选 | 2026-11-27：开源了，先看许可写给谁、能跑在哪、分数是谁测的"
date: 2026-11-27 21:00:00 +0800
categories: [AI 新技术]
excerpt: "头条：11-26，俄罗斯 Sber 把 GigaChat 4 的两档权重放到了 Hugging Face，昨天那篇精选漏收了，今天按补录来写。708B 的模型卡写的是 MIT，37B 写的是面向个人的非商用许可，两条许可并不一样；质量对比是官方自评，能跑在哪也差得很远。11-27 同一家又放开源的 GigaEdge Enhance 语音增强 SDK。补录 DeepL 的 Aure v2，以及栏面写 Nov 27、RSS 落到 11-28 凌晨的 Amazon Neptune Graph Sessions。观点是开源了，先看许可写给谁、能跑在哪、分数是谁测的。"
---
![AI 每日精选封面 2026-11-27](/assets/2026-11-27-ai-daily-digest-cover.jpg)

> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 开源了，先看许可写给谁、能跑在哪、分数是谁测的

今天最显眼的，不是又一家美国大厂改了名字，而是俄罗斯的 Sber 把新模型的权重放到了 Hugging Face。官方[俄文署文](https://giga.chat/blog/posts/gigachat-4)的栏面日期是 11-26，没有更精确的钟点；英文页还写着正在翻译，先看俄文。昨天那篇精选没有查 giga.chat，所以这条按补录来写。它一次放出两档：[37B](https://huggingface.co/ai-sage/GigaChat4-37B-A4B) 和 [708B](https://huggingface.co/ai-sage/GigaChat4-708B-A41B)，都写了原生一百万 token 的上下文，instant 和 reasoning 两种模式做在同一个检查点里，也可以调工具。听起来像「开源就能用」，可两张模型卡上的许可并不一样。708B 写的是 MIT；37B 写的是 Noncommercial License for individuals 1.0，许可证把使用主体写成同意条款的个人，并且明文禁止慈善机构、教育机构、公共研究机构和政府机构使用。官方自评把 708B 写成和智谱 GLM 5.3、DeepSeek-V4.1-Flash-1017、Mistral-Large-4-1T-A52B 同一档，把 37B 写成和 Qwen3.6-35B-A3B 相近，这些都是他们自己的测量，完整协议在[技术报告](https://github.com/salute-developers/gigachat4/blob/main/GigaChat_4.pdf)里。能跑在哪也差得很远：37B 的 FP8 卡写可以在单张 H100 80GB 上部署，708B 的 FP8 示例是两个节点、每个节点八张 H100。同一天 11-27，Sber 又发了[GigaEdge Enhance](https://giga.chat/blog/en/posts/giga-edge-enhance-sdk)，这是面向 CPU 服务器、手机和浏览器的开源流式语音增强 SDK，[仓库](https://github.com/salute-developers/giga-edge-enhance)里是 MIT。补录里还有 11-26 下午 DeepL 的 [Aure v2](https://www.deepl.com/en/press-release/aure-v2) 新闻稿，速度和质量对比同样是内部基准；以及栏面写 Nov 27、RSS 落到 11-28 凌晨 3 点的 [Amazon Neptune Graph Sessions](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-neptune-graph-sessions-generally-available/)，给每个代理单独一张图、空闲 15 分钟缩到零。开源了，先看许可写给谁、能跑在哪、分数是谁测的。

个人观点，不构成投资、采购或技术选型建议。数字和能力边界以各条原文为准。

## 今天最值得看的几件事

- **头条是补录：GigaChat 4 的权放出了，但两档许可和硬件门槛不是同一回事。** 11-26 的署文把 37B 和 708B 一起介绍，试用入口指向技术报告和模型卡，并没有写已经进了消费级助手。质量表是「按我们的评估」。俄文博文里 37B 的激活参数写成约 3.8B，模型卡和仓库名写作 4B，不要私自改成一个数字。
- **11-27 当天，同一家把语音增强 SDK 开源了。** GigaEdge Enhance 可以在 CPU 和浏览器里拼增强通道，仓库是 MIT。文里的质量和时延是他们在一台笔记本的 WSL2 环境里测的，不能当成已经过独立评测。
- **另一条补录是语音翻译。** DeepL 在 11-26 下午发布 Aure v2，面向已有的 Voice 客户，首发六种语言，输入和输出都要落在这六种里。新闻稿里的 50%、32% 是 11 月的内部研究，不是第三方评测。
- **账单和空闲缩容要看栏面日期。** Amazon Neptune Graph Sessions 的栏面是 Nov 27，RSS 则是北京时间 11-28 凌晨 3 点。它可以给每个代理单独一张图，空闲 15 分钟后缩到零，数据还在；定价页写了 s-NCU 的容量和按秒计费，但本轮打开时美元单价是脚本载入的，这里不写具体价钱。
- **本窗没有美国头部厂的新旗舰模型。** OpenAI、Anthropic、Google、xAI、Cursor 的官方栏目里，今晚都没有核到需要单列的新旗舰。Anthropic 11-25 有一篇把 Messages API 迁到 Rust 的工程署文，昨天漏收了，只短写，不当成新产品。
- **YC 核验：** 今天上午约 **08:15** 重新打开 `launches.json` 时，按时间倒序栏顶仍是只有 **4** 票的 Nutmeg，后面是 Altair Health（**5** 票）、Light Anchor（**13** 票）、Boat（**9** 票）、Vestris（**18** 票）等，不单列展开，也不写「现居顶」。已在更早写过的 River 现为 **26** 票，Morphy（公司名栏为 MouseCat）**11** 票，FlashDrive **32** 票，仍见栏内，不再展开。Winter 2027 申请仍在接受迟交，准时截止日期 **November 2** 晚上 **8pm PT** 已过；准时提交的将在 **December 11** 前收到决定。F26 Demo Day 仍为 **12 月 2 日**（周三）。

## 模型发布

### 1. 补录 11-26：Sber 放出 GigaChat 4，两档许可不是同一套

GigaChat 是俄罗斯联邦储蓄银行 Sber 的模型线。11-26 的[署文](https://giga.chat/blog/posts/gigachat-4)把 GigaChat 4 写成两档新模型，37B 和 708B 都支持最长一百万 token 的上下文，都能调用工具，并且把快速回答和先推理再回答做在同一个检查点里。英文页标题是 [Two Powerful Models, One Million Tokens, and New Agentic Capabilities](https://giga.chat/blog/en/posts/gigachat-4)，但页上仍提示译文还没好，技术细节以俄文和[技术报告](https://giga.chat/blog/en/posts/gigachat-4-tech-report)为准。

架构上，官方说这是在 GigaChat 3.5 的混合结构上继续放大：MoE，再配上 Gated DeltaNet 和带 DSA 的 MLA。博文写 37B 每 token 约激活 3.8B 参数，708B 约激活 41B；Hugging Face 上的卡片和仓库名则写作 A4B、A41B，也就是 4B 和 41B。这两种写法我都保留，不擅自改齐。署文还写，两档模型都能接进 Claude Code、Codex、OpenHands 一类的代理外壳里改仓库、调工具。

真正要先看的是许可和门槛。37B 的[模型卡](https://huggingface.co/ai-sage/GigaChat4-37B-A4B)写明采用 Noncommercial License for individuals 1.0，完整条文在[这份 LICENSE.txt](https://huggingface.co/ai-sage/GigaChat4-37B-A4B/blob/main/LICENSE.txt)里：被许可方写成同意条款的个人，模型及其派生只许非商用，用它为商业目的生成输出是禁止的；个人研究、实验、没有预期商业用途的爱好项目可以作为允许的用途，但条文里同时也写了，慈善、教育、公共研究、公共安全或卫生、环保组织和政府机构的使用是禁止的。不要把「非商用」理解成学校或政府一定能用。708B 的[模型卡](https://huggingface.co/ai-sage/GigaChat4-708B-A41B)则写 MIT。硬件也不在一个量级：37B 的 FP8 说明写可以在单张 H100 80GB 上部署，权重大约 40 GB，还要为缓存和状态另留内存；708B 的 FP8 示例是两个节点、每个节点八张 H100。对做本地部署的人来说，能下载不等于能合规地用，更不等于笔记本电脑就能跑。

分数方面，官方写「按我们的评估」。708B 被放在和智谱 GLM 5.3、DeepSeek-V4.1-Flash-1017、Mistral Large 4 同一档里比较，37B 则对 Qwen3.6-35B-A3B。署文举了若干自测数字，例如 708B 在 reasoning 模式下 Terminal-Bench 2.1 为 69.66%、Function Calling Benchmark（FCLv4）为 79.55%，37B 对应为 39.33% 和 72%。这些都不是独立榜，完整条件和对照表在[GitHub 上的 PDF](https://github.com/salute-developers/gigachat4/blob/main/GigaChat_4.pdf)里。对做检索增强、客服或代码代理的团队，这档模型提供了又一条可自托管的开源线，但选型时要把许可、卡数和自评口径放在一起看，而不是只看参数量和一句「对标某某」。

「如何试用」这一节只给了技术报告和两张模型卡，没有写已经进了 GigaChat 的消费级聊天产品。第三方如果有这种说法，我这边还对不上官方原文，先不写。

对在俄罗斯市场做本地化、或者想在自有机房里跑长上下文代理的人，708B 的 MIT 和百万上下文是一个可以认真看的选项，前提是算力预算跟得上。对只有单卡、又想试试 37B 的个人开发者，先把那份个人非商用许可读完，再决定能不能用于自己的项目。本轮没有核到它已经在全球主要云上架的官方说明。

## 公开检索之外，许可、语音和按次计费的图

### 2. 11-27：GigaEdge Enhance 把流式语音增强做成了开源 SDK

同一实验室在 11-27 发布了 [GigaEdge Enhance](https://giga.chat/blog/en/posts/giga-edge-enhance-sdk)。官方把它写成可在 CPU 服务器、移动设备和浏览器里做流式语音增强的 SDK：应用可以从神经去噪、归一化和动态处理等模块里拼出一条增强通道，共享核心走 ONNX Runtime 或 TensorFlow Lite。代码和三个配套模型在 [GitHub 仓库](https://github.com/salute-developers/giga-edge-enhance)，根目录的 LICENSE.txt 是 MIT。署文写公开了 8 kHz 的 INT8 模型，以及判别式和混合的 48 kHz FP32 模型。

质量、实时率和内存数字都是文内自测，测试机器写的是一台 Intel Core Ultra 5 125H，系统是 Windows 11 上的 WSL2，不能直接当成裸机 Linux 或手机端的通例。对做视频会议、呼叫中心或端侧语音接口的人，这是一套可以自己集成的降噪工具，但要把实验室数字和你这边的麦克风、编解码器负荷分开看。仓库许可是 MIT，和 GigaChat 4 的 37B 不是同一套，不要混着记。

### 3. 补录 11-26 下午：DeepL 的 Aure v2 更快了，语言范围却更窄

11-26 下午，DeepL 发了 [Aure v2 新闻稿](https://www.deepl.com/en/press-release/aure-v2)，`dateModified` 是 UTC 6:29，大约北京 14:29，已经早于昨天那篇精选的截稿，但当时没有查 DeepL 的新闻稿栏。11-11 首发的 Aure 我们一直留在笔记里没有单独成篇，这次写的是正式的第二版，不是把旧条拿出来加热。

新闻稿写，Aure v2 已向 DeepL Voice 客户提供，覆盖在线会议、面对面交谈，以及 Voice 的 API；支持的语言会自动启用，不必再做额外开通。首发是英语、德语、法语、西班牙语、日语和韩语，更多语言「即将推出」。产品页补充了两个容易忽略的边界：前代 Aure 还支持意大利语和葡萄牙语，v2 目前没有；而且 v2 要求你说的语言和对方听到的语言都在这六种之内，也还不能自动识别语种，必须显式选择。不要把它写成「开了就覆盖所有 DeepL Voice 语言」。

速度和质量是卖点，也是要打折看的部分。新闻稿写，在内部基准里，相对 Aure 的中位翻译延迟降了 50%，在所测的全部语言对上质量高于六个竞品系统，英日方向比 Google Gemini 3.5 Live Translate 少 32% 的翻译错误。脚注写明：这是 2026 年 11 月的内部研究，材料是 1 分钟真实语音、10 个语言对，转写经过人工校验，走公开 API、不含应用开销，真实对话里的结果可能不同。对做跨国会议、现场接待或客服的人，这确实更接近「能聊起来」而不是「等半句再听」，但采购时仍应拿自己的语对和场景复测，不要把内部百分比直接写进标书。产品页上的试用入口是 DeepL Voice，新闻稿没有把 Aure v2 本身写成无条件免费。

### 4. 栏面 Nov 27、RSS 今早 3 点：Neptune 给每个代理一张可缩到零的图

[Amazon Neptune 的 What’s New](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-neptune-graph-sessions-generally-available/) 栏面写 Posted on: Nov 27, 2026，RSS 时间是 UTC 19:00 · 11-27，也就是北京时间 11-28 凌晨 3 点。这是今天早上才出现在订阅里的 11-27 官方稿，所以日期我两边都保留，不把它假装成昨天下午就已经在栏目置顶。

官方的场景写得很明确：做 GraphRAG、代理或按用户分析时，常常希望每个会话或任务都有自己的图，而图的大小事先不好估。Graph Sessions 是一种按代理设计的计算模式，不必按预置图的 16 m-NCU 下限来付费；创建时可选 4 或 8 个 s-NCU 作为起始工作内存，并留出最多两倍的余量（4 能到 8，8 能到 16），按实际用到的内存计费。空闲 15 分钟后自动缩到零，下一次查询在数秒内恢复，图和数据还在，不必为下一轮重新装载。创建可以用控制台、CLI 或 SDK，查询用 openCypher，和其它 Neptune Analytics 图一样。

定价页还补了一层：这套会话跑在隔离的 Lambda MicroVM 里，每个 s-NCU 对应 1 GB 内存和 0.25 vCPU，计算按运行秒计费；停掉之后不计计算，只计存储。本轮打开定价页时，美元单价是脚本载入的，我没有把它抄成一个固定数字，需要看的人直接去[官方定价页](https://aws.amazon.com/neptune/pricing/)。URL 里带 generally-available，正文用的是 now supports，我也没有看到区域名单。对在 AWS 上做知识图谱或给每个客户单独一份关系图的人，这降低了「开一张图就要按预置下限付钱」的负担，但仍要把空闲缩容、恢复时间和存储费用算进链路里，不要理解成闲置完全免费。

### 5. 补录 11-25：Anthropic 把 Messages API 迁到了 Rust

11-25，Anthropic 在研究栏发了[把 Messages API 从 Python 迁到 Rust](https://www.anthropic.com/research/migrating-api-to-rust) 的工程署文。栏面是 Nov 25，更新时间落到北京 11-26 凌晨 0:27，已经进了昨天的采集窗口，但昨天的笔记里还写栏面仍是更早的公司稿和 Claude Ship，这条漏了，今天短补一句。官方写，他们用原来的 Messages API 来核验新实现，并由 Claude 代理团队去追 Python 和 Rust 两个版本之间的差异。文中关于耗时、CPU、内存和线上匹配率的数字，都是他们自己的工程回顾，不是面向用户的新产品，也不应当成第三方评测。对在生产里用 Anthropic API 的人，这更像是厂里换引擎的说明，不改变你这边的调用方式，但能提醒一句：代理帮忙搬代码之后，真正花时间的往往是证明行为和旧版一致。

## YC 核验

今天上午约 08:15 再打开 `launches.json`，按时间倒序栏顶仍是 Nutmeg，现为 4 票；后面 Altair Health 5 票、Light Anchor 13 票、Boat 9 票、Vestris 18 票，都不达到需要单列的程度，也不写「现居顶」。River、Morphy、FlashDrive 还在栏里，票数变化不大，不再展开。Winter 2027 仍接受迟交，11 月 2 日晚上 8 点（太平洋时间）的准时截止已经过了；准时交的会在 12 月 11 日前收到决定，迟交仍会审，但不承诺时间。F26 Demo Day 仍是 12 月 2 日，周三。

## 普通人可以做的 3 件事

1. **想下载或试用 GigaChat 4 的个人开发者、以及评估自托管的工程负责人：** 先分清要看的是[37B](https://huggingface.co/ai-sage/GigaChat4-37B-A4B) 还是 [708B](https://huggingface.co/ai-sage/GigaChat4-708B-A41B)。37B 不是 MIT，先读[这份个人非商用许可](https://huggingface.co/ai-sage/GigaChat4-37B-A4B/blob/main/LICENSE.txt)，不要默认公司项目、学校实验室或政府项目都能用。708B 是 MIT，但官方 FP8 示例是 16 张 H100 的量级，单卡笔记本跑不了。质量数字以[署文](https://giga.chat/blog/posts/gigachat-4)和[技术报告](https://github.com/salute-developers/gigachat4/blob/main/GigaChat_4.pdf)为准，当作官方自评，而不是已经对过的公开榜。

2. **已经在用 DeepL Voice 做会议或现场翻译的人，以及要接 Voice API 的产品经理：** 对照[新闻稿](https://www.deepl.com/en/press-release/aure-v2)和[产品页](https://www.deepl.com/en/products/voice/aure)，看自己的语对是否落在英、德、法、西、日、韩这六种之内，并且输入、输出都在其中。意大利语或葡萄牙语目前仍要走前代 Aure。新闻稿写支持语言会自动启用，但 v2 还不能自动识别你在说哪种语言。延迟和错误率是内部基准，若要用于客服或商务谈判，最好用自己的录音复测一遍。

3. **在 AWS 上做 GraphRAG，或想给每个用户、每个代理单独一份图的人：** 先读[这则 What’s New](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-neptune-graph-sessions-generally-available/)和[定价页](https://aws.amazon.com/neptune/pricing/)。起始档是 4 或 8 个 s-NCU，空闲 15 分钟后缩到零，数据还在；停止后不计计算、只计存储。栏面日期和 RSS 时刻不一致，并不影响能力本身，但说明它是今早才进订阅源的 11-27 稿。具体美元单价以定价页当时显示为准，这里不抄一个可能过时的数字。做质谱或小分子鉴定的人，昨天写过的 DeepMind Mass Spec 技能申请入口仍然有效，并不在今天这条里重复展开。本轮没有核验过新的跟练视频，也就不列教程。

