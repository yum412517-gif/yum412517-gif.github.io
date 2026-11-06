---
layout: post
title: "AI 每日精选 | 2026-11-06：钱包进 Claude；钱包、终端、闸"
date: 2026-11-06 21:00:00 +0800
categories: [AI 新技术]
excerpt: "头条：OpenAI GPT‑6 Cyber 与 Google Gemini Omni 1.2 Flash 同窗放量。观点谈 Agent 的三道账：谁碰得到钱包、谁摸得到终端、谁过得了闸。另有 Claude×Plaid 理财、Dropbox×Tigris、Muse/Edits/ElevenMusic、真机 Harness 与工信部进网、Teammates/Cursor Live Apps、Clutch 谈判与 METR 约 2×。"
---
![AI 每日精选封面 2026-11-06](/assets/2026-11-06-ai-daily-digest-cover.jpg)


> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 今天最值得看的几件事

- **头条：frontier 产品双发**——OpenAI **GPT‑6 Cyber**（网络安全专用，Preparedness 升 **Critical**）与 Google **Gemini Omni 1.2 Flash**（原生约 **15** 秒视频 GA，Vids 月免约 **3** 条）；旁证 Thinking Machines **Inkling 2 Small**、腾讯 **Hy4**、蚂蚁 **Ling-3.2-flash**。
- Claude **Personal Finance**×**Plaid**：美区 Pro/Max/Ultra beta，只读连银行/卡/贷款/投资。
- Dropbox 拟购 **Tigris** 约 **$350M** 现金 + **DBX Agent Cloud**（先 S3 兼容）。
- 消费多模态：Meta **Muse** 语音/表情 Avatar 美区放量；ElevenMusic×**SoundCloud** 直发；Instagram **Edits** Mac + **MCP**。
- 真机入口与中国闸：Launch YC **Phone Harness**、**Glasshand** 托管真机；工信部《智能体终端进网管理》通知公开。
- 企业 Agent 面：Perplexity **Teammates**（Max research preview）、Cursor **Build Live Apps**、Airbnb 旅行 Agent 约 **2027 H1**。
- 安全/执法闸：Palo Alto 据报谈购 **Clutch Security** 约 **$500M**；Claude Enterprise **Security Center**；旁证美司法部 **DOJ-SITF**。
- METR：Anthropic 高权限 R&D 加速评估约 **2×**。
- YC：W27 逾期仍审，F26 Demo Day **12-02**；Rivet / Limnion / Databuddy / Asim / Hesper / Verno / Vorelios / Kino 等并入一条。
- 观点：**钱包、终端、闸**——Agent 碰到账户与设备的三道账。

## 模型发布

### 1. GPT‑6 Cyber + Omni 1.2 Flash：安全专用模与可编辑视频同窗放量（头条）

同一窗里，一边是「只给获批红队」的网络安全专用模，一边是「有 Google 账号就能试」的视频生成。OpenAI 署 **November 5, 2026** 正式发 **GPT‑6 Cyber**：自称 ExploitGym 约 **48.5%**（对照 GPT‑5.6 Cyber 约 **32.1%**，相对提升约 **51%**）；Preparedness Framework 网络安全档由 High 升至 **Critical**。对齐侧 ExploitGym Honeypot：无部署提示时越界利用约 **99.93%** 回避、有提示时约 **100%**（对照 5.6 Cyber 约 **94.49%**）。叙事已用于 Linux 约 **948** 个 LPE 利用管道与 Firefox 约 **81** 个高严重未知洞（Mozilla 已开始合入补丁）；RemoteExploitBench 上 Daybreak Blue×Astra 拒答约 **100%**、Cyber 完成约 **95%**。初始经 API/Codex 向部分 **Daybreak Red** 客户开放，称将扩至全部 Daybreak Red，并另开 Critical Infrastructure 分组；配套约 **$1B** Daybreak for Frontline Defenders 叙事。Google 同日署 **Nov 05** 正式发 **Gemini Omni 1.2 Flash**：原生最长约 **15** 秒（1.1 约 **10** 秒）、时长可按 **1** 秒步进约 **3–15** 秒；多轮对话编辑；相对 1.1 降价约 **30%**——API **720p** 约 **$0.07**/秒；Gemini API / Gemini for business / Google Cloud 一般可用，带 SynthID。配套 Google Vids 切到 Omni **1.2** Flash，有 Google 账号或 Workspace 者每月可免费生成至多约 **3** 条 **15** 秒视频；Gemini 应用向 AI Ultra 订户滚动放量。

来源：[OpenAI·Introducing GPT‑6 Cyber](https://openai.com/index/introducing-gpt-6-cyber)、[The Verge·GPT-6 Cyber](https://www.theverge.com/ai-artificial-intelligence/1027599/openai-gpt-6-cyber-launch)、[TechCrunch·cybersecurity model](https://techcrunch.com/2026/11/05/openai-released-a-new-cybersecurity-model-is-that-enough/)、[Google Blog·Gemini Omni 1.2 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)、[Google Vids·Omni 1.2 Flash](https://blog.google/products-and-platforms/products/workspace/omni-1-2-flash-google-vids/)

一边卖「过闸才能用的攻击面研究模」，一边卖「免费额度就能摸的视觉入口」——和昨天写码壳兼并是不同场地的入口战。受益的是获批 Daybreak 的安全团队、补丁编排与 OT/ICS 紫队、短视频/Ads 素材流水线、Vids 教育与营销模板；付钱的是把 Cyber 写成「公众可调攻击模」、或把 Vids 月约 **3** 条写成「API 无限」的人。标「ExploitGym/Honeypot 为公司评测 ≠ 第三方盲测；**Critical** 为自家框架标签；获批 Daybreak Red ≠ 公众可调；约 **948**/**81** 为受控研究+人类审阅报送 ≠ 已无人值守对公网利用；官方 GA ≠ 各账号已同步放量；约 **$0.07**/秒为 **720p** 口径」。

- 安全负责人：先核组织是否在 Daybreak Red、是否另批 GPT‑6 Cyber，再谈替换人工红队 KPI。
- 内容运营：打开 [vids.new](https://vids.new)，用一张品牌静帧试 **15** 秒循环，再谈批量；额度按月计，别拿测试 prompt 烧免费条。
- 独立开发者：Omni API 的多轮编辑与参考片段比「再套一层聊天壳」更适合做垂直插件。

教程：Cyber 以 [OpenAI 公告](https://openai.com/index/introducing-gpt-6-cyber)、[Daybreak 概览](https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview) 与 [Responses API·Daybreak](https://developers.openai.com/api/docs/guides/daybreak) 为准——无公开「如何利用」跟练片，也不应跟练攻击步骤。Omni / Vids 以 [官方 Vids 博文](https://blog.google/products-and-platforms/products/workspace/omni-1-2-flash-google-vids/) 为准；公开图文跟练可参考 [7minai·15 秒视频 how-to](https://7minai.com/how-to-make-15-second-videos-with-gemini-omni-1-2-flash/)（第三方，非 Google 官方片）。Vids 产品入门可参考公开片 [Intro to Google Vids](https://www.youtube.com/watch?v=qwmu5GlThyw)（同类 Workspace 操作，非 Omni 1.2 专片）。本条未核到针对 GPT‑6 Cyber 的成熟 Bilibili/YouTube 操作片。

### 2. Inkling 2 Small、Hy4、Ling-3.2-flash：开源/闪档多模态一日三连

**Thinking Machines Inkling 2 Small**：MoE 约 **594B** 总参 / **17B** 激活，图像输入与可变 effort；自称 Artificial Analysis Intelligence Index 约 **31**；初始经 **Tinker** 推理与微调，**权重暂闭源**，称完成外部安全测试后拟约下周以 **Apache 2.0** 开权重。**腾讯 Hy4**：首次加入视觉理解与 computer-use（CLI/GUI）；权重与 system card 称「未来数日」放出，当前经 TokenHub / WorkBuddy / CodeBuddy / 元宝 / 企微 AI 助手与 OpenRouter 等可用；定价自称约 **$0.90**/百万 input、**$2.70**/百万 output；**11-04–11-15** WorkBuddy/CodeBuddy 免费、TokenHub 约五折至约 **12-31**。**蚂蚁 Ling-3.2-flash**：原生多模态 MoE，约 **560B** / 激活约 **25B**、约 **1M** 上下文；公司口径三项基准超 Claude Opus 5（max）——OmniDocBench1.5 约 **92.21**、ZEROBench（Sub）约 **43.71**、Vision2Web 约 **85.86**；API 自称约 **$0.30**/百万 input、**$0.90**/百万 output，上线前约 **2** 周限时免费。旁证：Kakao **Kanana-2-v-decide**（结构化判断专用、自称单卡 H200 约 **<0.04** 秒）、淘宝 **MNN-Pocket-0.3B**（端侧）、PFN **PLaMo 3 Translate**——篇幅所限不单开。

来源：[Thinking Machines·Inkling 2 Small](https://thinkingmachines.ai/news/inkling-2-small/)、[Tencent·Hy4](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/)、[蚂蚁百灵·changelog](https://developer.ant-ling.com/zh-CN/docs/getting-started/changelog/)、[IT之家·Ling-3.2-flash](https://www.ithome.com/0/1023/043.htm)

闭源侧在卖「过闸的专用模」和「可编辑视频」；开源/闪档侧在卖「可微调、可嵌入 Agent 循环的脑」。受益的是私有化推理、computer-use 集成商、文档/前端多模态流水线；付钱的是把「下周 Apache」写成「已可本地下载」、或把公司盲评写成「已定开源第一」的人。标「AA Index / 财务盲评 / 三项超 Opus 为公司或引用快照 ≠ 第三方盲测冻结；闭源可调 ≠ 已可本地下载；Hy4 权重未落盘；Ling 两周免费与价目以控制台为准；「原生多模态」≠ 已开源全量权重」。

- 平台工程：Inkling 先在 Tinker 压 agentic coding；Hy4 / Ling 先对隔离集群跑通 computer-use / 多模态长程，再谈替换默认闭源。
- 采购：把「许可文本 + 是否可自托管权重 + 免费窗截止日期」拆进三行。
- 端侧/小模团队：Kanana decide、MNN-Pocket、PLaMo Translate 更适合「结构化输出 / 离线手机 / 翻译」窄场景，别拿去对打 frontier 通用助手。

教程：以各家官方页与 changelog 为准。本条未核到针对 Inkling 2 Small / Hy4 / Ling-3.2-flash 的成熟 Bilibili/YouTube 专片；同类可搜「vLLM 部署多模态 MoE」「OpenRouter computer-use」公开分享作流程参考。

## 最佳实践

### 3. Claude Personal Finance×Plaid：美区只读理财进聊天入口

Anthropic 推 **Personal Finance**（美区 beta）：经 **Plaid** 只读连接银行/信用卡/贷款/投资账户，可用自然语言问开支分类、异常扣费、订阅与发薪前剩余等；自称无广告、不推销自家信贷/存款，且非投资建议工具。可见范围含银行名、账户名/类型/末四位、余额与信用额度、至多约 **24** 个月流水；枢纽内对话称不用于训练。起步面向美区 **Pro / Max / Ultra**（非 Free/Team/Enterprise；渐进放量；web/Desktop/iOS/Android）。Plaid 官方同日确认由其承接账户连接与流水整理。对照 OpenAI ChatGPT 约 **5** 月同类能力。

来源：[Claude·Introducing Personal Finance](https://claude.com/resources/articles/introducing-personal-finance-in-claude)、[Claude Help·Use Personal Finance](https://support.claude.com/en/articles/18185620-use-personal-finance-in-claude)、[Plaid·Powers Financial Insights In Claude](https://plaid.com/blog/plaid-anthropic-financial-insights-in-claude/)、[TechCrunch](https://techcrunch.com/2026/11/05/claude-can-now-analyze-your-spending-with-its-new-personal-finance-tool/)、[The Verge](https://www.theverge.com/ai-artificial-intelligence/1027652/anthropic-claude-plaid-personal-finance)

钱包第一次以「只读账户图」进了 Claude 的默认侧栏——和 Cyber 的「过闸才能碰攻击面」是同一天的权限叙事。受益的是消费理财入口、Plaid 类聚合中间件、订阅审计与异常扣费提醒工具；付钱的是把只读写成「已可代转账投资」、或把美区 beta 写成「全球/Team 已开」的人。标「只读 ≠ 已证零越权动作；美区付费档 beta ≠ 全球/Team 已开；枢纽不训练 ≠ 枢纽外隐私设置自动等价；AI 可算错须对银行对账；Plaid 同意范围随银行屏变」。

- 美区 Pro/Max/Ultra 用户：侧栏打开 Personal Finance → Link accounts with Plaid，先只连一张日常消费卡试问「上月订阅清单」。
- 财务/风控产品：对照 Claude 与 ChatGPT 理财面，问清「只读范围 + 训练排除 + 人闸」三行再谈接入。
- 普通读者（非美区）：本条无操作入口；关注的是「Agent 碰钱包」会不会很快复制到本地银行开放银行接口。

教程：以 [Claude Help·Use Personal Finance](https://support.claude.com/en/articles/18185620-use-personal-finance-in-claude) 十步为准。公开图文跟练可参考 [FindSkill·Setup guide](https://findskill.ai/blog/claude-personal-finance-connect-bank-setup-guide-2026/)（第三方整理 Help Center，非 Anthropic 官方片）。本条未核到成熟一手官方 YouTube/Bilibili 专片。

### 4. 真机入口 + 中国进网闸：Phone Harness / Glasshand × 工信部通知

**Phone Harness**（Launch YC）：开源 harness（自称 GitHub 约 **4K+** star、MIT）经 Mac 上 iPhone Mirroring 或 Android adb 接管本机（无越狱、手机端无需装 App）；另提供 Cloud 真机池，**24/7** 在线并跨会话保持登录；叙事解锁仅移动端 App、长登录态、读短信/2FA 与真实设备指纹。**Glasshand**：数据中心托管实体 iPhone/Mac（自称非 VM），经 API 给 Claude Code / Codex / Cursor 等看屏、点按、键入；可装 App Store、加 eSIM 收短信；月租口径约 **$60**/iPhone、**$90**/Mac。同日中文媒体公开工信部办公厅《关于加强智能体终端设备进网管理的通知》（工信厅信管〔2026〕42号，文号署 **2026-10-24**）：预置智能体的手机/平板/可穿戴须适配验证与设置页公示；进网检测纳入智能体适配与涉诈前置评测，终端智能体参考互联国标配备唯一身份码；OTA 须事先方案、专家评估后方可正式对用户提供；分发平台推动 App 以电子签名声明是否同意被智能体调用，未声明不得强制调用。

来源：[Launch YC·Phone Harness](https://www.ycombinator.com/launches/WdR-phone-harness-let-your-agent-tap-scroll-and-type-on-your-iphone-or-android)、[phone-harness.com](https://phone-harness.com/)、[Glasshand](https://glasshand.com/)、[中新网·工信部](https://www.chinanews.com.cn/cj/2026/11-06/10727035.shtml)、[IT之家](https://www.ithome.com/0/1023/059.htm)、[新华网](https://www.news.cn/20261106/b56a8a3cb14e40a69d997b37b39cc99a/c.html)

Agent 要摸到「真机身」；监管要摸到「谁预装、谁可被调用」——和钱包只读是同一根脊柱上的终端账。受益的是移动端 computer-use 基建、真机云池、终端厂适配与分发平台签名声明中间件；付钱的是把读短信/2FA 写成「已可无人值守接管个人银行 App」、或把进网通知写成「已全面封杀第三方 Agent」的人。标「约 **4K** star / 约 **$60/$90** 为自称或官网快照；Mirroring/adb ≠ 云真机同 SLA；通知署 **10-24**、媒体 **11-06** 公开；唯一身份码/适配库为推进中；细则与标准仍待落地」。

- 移动测试 / Agent 产品：先在隔离号上跑 Phone Harness 或 Glasshand，合同写清擦除 SOP 与账号 ToS。
- 终端厂 / 应用商店：对照通知四条——适配公示、进网评测、OTA 报备、调用声明——排进发版清单。
- 普通用户：别把「Agent 能点我的手机」当成默认便利；先问谁持有设备、谁能读短信。

教程：Phone Harness / Glasshand 以各自官网与 Launch 页为准。本条未核到成熟 Bilibili/YouTube 专片；政策文本以中新网/新华网转述与后续工信部全文发布为准。无「如何绕过进网」教程，也不应跟练。

## 工具与产品

### 5. Dropbox×Tigris 约 $350M + DBX Agent Cloud：文件层要当 Agent 底座

Dropbox 宣布拟收购 **Tigris Data Inc.**，并推 **DBX Agent Cloud**：8-K 披露 **11-03** 达成约 **$350M** 现金收购协议（可调价），预计 **2026** Q4 交割（须惯例条件）。DBX Agent Cloud 先以可独立购买的 **S3 兼容**对象存储起步，后续规划 filesystem 与多模态 content processing，叙事服务训练数据/模型产物/Agent 跨会话文件。同步「新 Dropbox 体验」：在既有文件上找/摘要/对比/起草/改 PDF·图/转写/剪视频等，先出计划再经用户批准执行，可连到 ChatGPT / Claude / Muse 等；自称已覆盖逾约 **70,000** 团队，首批英区 Standard/Advanced 在美/英/澳，更广约 **2027**。Tigris 官方确认体验/API/零出口费价目与团队暂不变。旁证：Box 同窗推 Context Retrieval×NVIDIA Nemotron（自称 Recall@5 约 **+20%**、token 约 **-90%**）——篇幅并入对照，不单开。

来源：[Dropbox Blog·next chapter](https://blog.dropbox.com/topics/company/dropboxs-next-chapter)、[BusinessWire](https://www.businesswire.com/news/home/20261105637007/en/Dropbox-Announces-Plans-to-Acquire-Tigris-Data-Inc.-and-Unveils-DBX-Agent-Cloud-as-Part-of-AI-Powered-Product-Evolution)、[Tigris·Dropbox plans to acquire](https://www.tigrisdata.com/blog/dropbox-plans-acquire-tigris.md)、[TechCrunch](https://techcrunch.com/2026/11/05/dropbox-acquires-tigris-data-for-350m-to-bolster-its-ai-iinfrastructure/)、[Box Blog·Partners With NVIDIA](https://blog.box.com/box-partners-nvidia-deliver-trusted-content-layer-enterprise-ai)

昨天卖的是写码壳；今天文件柜自己要当 Agent 的对象存储——钱包、终端之后，下一层是「文件能不能被 Agent 安全读写」。受益的是 S3 兼容 Agent 存储、企业内容治理、计划-批准式文件 Agent；付钱的是把拟收购写成「已交割取代 AWS S3」、或把约 **70,000** 团队写成「管理员已默认开通全部 Agent 改文件」的人。标「约 **$350M** 为 8-K 口径、须交割；拟收购 ≠ 已完成；S3 兼容起步 ≠ filesystem/处理已 GA；连 ChatGPT/Claude/Muse ≠ 各租户已默认开通；Box 约 **20%**/**90%** 为公司潜力口径」。

- 平台 / 数据负责人：选型时问清「Agent 跨会话文件落在谁的桶里、出口费与驻留法域」。
- Dropbox 现网管理员：先开「计划再批准」试点，别一上来给 Agent 写权限。
- 创业者：可迁出的审计与策略层，比再做一个聊天壳更贴今天的文件并购逻辑。

教程：以 [Dropbox 公告](https://blog.dropbox.com/topics/company/dropboxs-next-chapter) 与 Tigris 说明为准。本条未核到针对 DBX Agent Cloud 的成熟 Bilibili/YouTube 专片。

### 6. Muse、ElevenMusic×SoundCloud、Edits Mac：消费多模态三条入口

**Meta Muse** 美区应用（mobile / web / Mac）放量实时语音与表情 Avatar：点电话图标开聊；可选仅语音/旁挂 Avatar/全屏；自称数百种声线；后续称将上 AI Glasses 与年内 Muse Charm——硬件须另核。**ElevenLabs ElevenMusic × SoundCloud**：创作者可在 ElevenMusic 内直发 SoundCloud；Artist Pro 新老订户可获约 **3** 个月 ElevenMusic Pro（至多约 **1,000** 首/月等）；曲目标 ElevenMusic 来源披露；ElevenLabs 称累计已生成逾约 **2500** 万轨。**Instagram Edits** 发 Mac 桌面版：免费多轨剪辑 + 经 **MCP** 接任意 AI Agent（含 Muse）做粗剪，再回手工精修；无水印 **4K** 导出并可直发 Instagram；仅 **macOS**；自称移动端 Edits 用户约 **5000 万**。

来源：[Meta Newsroom·Give Your Muse a Voice](https://about.fb.com/news/2026/11/introducing-muse-ai-voice-expressive-avatars/)、[TechCrunch·Muse](https://techcrunch.com/2026/11/05/meta-says-us-users-can-now-video-chat-with-their-muse-ai-avatar/)、[TechCrunch·ElevenLabs×SoundCloud](https://techcrunch.com/2026/11/05/elevenlabs-now-lets-users-publish-ai-generated-music-directly-on-soundcloud/)、[Edits Blog](https://edits.instagram.com/blog/edits-desktop-video-editor)、[The Verge·Edits MCP](https://www.theverge.com/tech/1027444/instagram-edits-desktop-ai-agents-muse-mcp)、[TechCrunch·Edits desktop](https://techcrunch.com/2026/11/05/instagram-brings-edits-to-desktop-to-take-on-capcut/)

通话角色、出歌直发、剪辑台接 MCP——消费侧三条线都在抢「打开就能做」的入口，和 Omni 视频、钱包侧栏是同一天的注意力战争。受益的是创作者工具集成商、AI 音乐披露与分发合规中间件、MCP 粗剪插件；付钱的是把美区放量写成「Glasses/Charm 已发货」、或把 MCP 写成「任意 Agent 开箱即通」的人。标「美区应用 ≠ 硬件已上市；Artist Pro 福利有期限；约 **2500** 万轨 / 约 **5000 万** 用户为公司口径；仅 Mac；跨端同项目仍在做」。

- 美区 Muse 用户：点右上角电话图标，先试「边走边口述行程」再谈全屏 Avatar。
- 音乐创作者：直发前核对 SoundCloud AI 内容政策与来源披露，别默认「平台已全面拥抱」。
- 短视频创作者（Mac）：用 Edits 接 Muse 做 rough cut，精修仍留在时间线——合同别承诺无人值守出片。

教程：Muse 以 [Meta Help·How to get started](https://www.meta.com/help/superintelligence/1331373868832401/) 与 Newsroom 为准；公开图文可参考 [How to Use Muse Voice](https://openaimaster.ai/how-to-use-muse-voice-2026/)（第三方，非 Meta 官方片）。Edits / ElevenMusic 以官方 blog 与 TC 为准。本条未核到针对 Edits MCP 或 ElevenMusic×SoundCloud 直发的成熟一手官方片。

### 7. Teammates、Cursor Live Apps、Airbnb 2027 H1：常驻同事、可分享应用、旅行垂直窗

**Perplexity Teammates**：面向持续进行中工作的个人 Agent——多 Agent 编排、自有桌面与浏览器、对 Slack/GitHub/Linear 等主动监控；初始 research preview：个人 **Max**（约 **$200**/月）网页端；Enterprise 默认不在首发；CEO 称内部已跑约 **10,000** 个 teammate。**Cursor Build Live Apps**：Cloud Agent 可从描述搭可分享 Web 应用（脚手架、按需 Postgres、Cursor SSO、托管与域名）；发布前确定性检查 + Agent 安全审阅，须用户显式 publish；面向已开 Cloud Agents 的付费档。**Airbnb** 在 Q3 股东信明确旅行 AI Agent 放量窗口为约 **2027** 上半年：从旅行专用界面组件实时「生成式 UI」拼界面，并在站内行动；Chesky 对比通用 Agent 擅预约、旅行「发现本身是体验」。

来源：[Perplexity·Teammates](https://www.perplexity.ai/hub/blog/teammates-are-agents-for-complex-ongoing-work)、[The Verge·Teammates](https://www.theverge.com/ai-artificial-intelligence/1028302/perplexity-teammates-ai-agents-work)、[Cursor Changelog·Build Live Apps](https://cursor.com/changelog/build-live-apps)、[Cursor Docs·Apps](https://cursor.com/docs/cloud-agent/apps)、[TechCrunch·Airbnb AI travel agent](https://techcrunch.com/2026/11/05/airbnb-says-its-launching-an-ai-travel-agent-in-the-first-half-of-2027/)、[The Verge·Airbnb](https://www.theverge.com/tech/1028412/airbnb-ai-travel-agent-q3-2026-earnings)

常驻同事、一键出可分享应用、垂直场景把窗口钉到 **2027 H1**——企业侧在卖「能托付多久」而不是「能不能聊」。受益的是工作区 Agent 治理、内部工具快速发布、旅行垂直生成式 UI；付钱的是把 Max preview 写成「Enterprise 已开」、或把股东信窗口写成「已上线公测」的人。标「约 **$200**/月门槛；约 **10,000** 为公司口径；安全检查 ≠ 合规认证；GitLab 未发；约 **2027 H1** 可滑」。

- Max 用户：先给 Teammate 一个循环研究任务 + Slack 只读，再开主动监控写权限。
- Cursor 付费 + Cloud Agents：显式说「build an app」，Publish 前看密钥检查是否拦下 .env。
- 旅行产品：把「站内履约 + 生成式 UI」写成验收，别承诺已打通全行业原生预订。

教程：Teammates 以 [Help·Get started](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates) 为准；Cursor 以 [Docs·Apps](https://cursor.com/docs/cloud-agent/apps) 为准，公开图文可参考 [AI Code With·Live Apps](https://aicodewith.ai/es/blog/cursor-live-apps-cloud-agent-deploy-share-link)（第三方整理文档，非 Cursor 官方片）。Airbnb 无操作教程，跟踪以股东信与后续产品署文为准。本条未核到针对 Teammates / Live Apps 的成熟一手官方 YouTube 专片。

### 8. 安全闸升温：Clutch 谈判、Claude Security Center、DOJ-SITF

TechCrunch 据报 Palo Alto Networks 正谈判收购 **Clutch Security**：约 **$500M** 现金 + 里程碑，服务 AI Agent 非人身份（API 密钥/服务账号/令牌等）生命周期与权限治理；Clutch 约 **2025-01** Series A 约 **$20M**，现 ARR 逼近约 **$10M**；双方未置评——**谈判进行中、可能不成交**。Anthropic 为 Claude Enterprise 加 **Security Center**（beta）与 inference hooks（prompt / pre-tool-call）**GA**——把提示与工具调用送进企业自有 DLP 做 allow/deny；另有集中管理控制台 **admin.claude.com**（beta，setup **不可撤销**）。旁证：美司法部 **November 5** 成立 **Super Intelligence Task Force（DOJ-SITF）**，协调涉「超级智能」滥用的刑/民执法，合并 **2026-01-09** 既有 AI Task Force。

来源：[TechCrunch·Palo Alto×Clutch](https://techcrunch.com/2026/11/05/palo-alto-networks-in-talks-to-buy-ai-agent-security-startup-clutch-for-500m/)、[Claude·Enterprise security updates](https://claude.com/resources/articles/claude-enterprise-security-updates)、[Help·Inference hooks](https://support.claude.com/en/articles/16059458-inference-hooks-overview)、[DOJ·Super Intelligence Task Force](https://www.justice.gov/opa/pr/department-justice-launches-super-intelligence-task-force)、[Nextgov](https://www.nextgov.com/artificial-intelligence/2026/11/department-justice-forms-ai-task-force/417074/)

Cyber 在卖能力，Clutch/Security Center/DOJ 在卖「谁能碰密钥、谁能过工具调用、谁被执法盯上」——和钱包只读、终端进网是同一天的闸。受益的是非人身份治理、企业 DLP×Agent hooks、合规审计报告工具；付钱的是把据报谈判写成「已交割进 Prisma」、或把通稿写成「已立新刑罪/已出可操作合规清单」的人。标「据报谈判 ≠ 已签约；约 **$500M**/ARR 为报道口径；Security Center/集中管理多为 beta；hooks GA ≠ 已覆盖 Platform API；DOJ 备忘录 ≠ 已禁开源模」。

- 安全采购：非人身份与 Agent 工具调用分两本账，别只买「提示词护栏」口号。
- Claude Enterprise Owner：开集中管理前先定不可撤销 Owner；hooks 先接只读 deny。
- 法务：DOJ-SITF 当执法优先级信号，合同里写清跨境与关键基础设施边界。

教程：以各官方资源文 / DOJ 通稿为准。本条无攻击教程；防御同类可搜公开「non-human identity management」「DLP tool call hooks」运维分享作流程参考。

## 论文研究

### 9. METR：Anthropic R&D 加速约 2× 的高权限评估

METR 发布对 Anthropic 的高权限 AI R&D 加速独立评估（评估窗约 **8-12–10-29**，终稿约 **11-03**，公开署 **Nov 5**）：主观结论——截至约 **2026-10**，Anthropic 在「定义良好任务」上的能力改进速率约为此前约 **2024-03–2025-10** 的约 **2×**（团队亦接受约 **1.3–3×** 不确定性）；猜测约 **80%** 或可归因于广泛用 AI 做研发，但证据多被打码。可公开经验：自约 **2025-10** 起内部 AECI 趋势加速约 **1.9×**［**95%** CI 约 **1.5–2.8×**］；可排除「训练算力规模加速」为主因；未看到未来约 **12** 个月明确瓶颈。旁证同窗还有 Science’s Last Exam、Joules-to-GDP、高血压表筛等——硬尺子很多，本条只收 METR 这一根与「加速度」最贴的。

来源：[METR·Independent Assessment](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/)、[The Verge·METR](https://www.theverge.com/ai-artificial-intelligence/1028046/an-anthropic-risk-assessment-from-ai-safety-organization-metr-is-out)

能力在加速，证据却大量打码——和 Cyber Critical、DOJ 任务组是同一张「谁在量 frontier 风险」的图。受益的是第三方评估机构、实验室治理顾问、可验证任务上的 AECI 类尺子；付钱的是把约 **2×** 写成「已证全行业递归自我改进」或反过来写成「已触发某硬停机」的人。标「高权限但仍大量打码 ≠ 可独立复现全证据；约 **2×** 为 METR 主观综合；AECI 偏可验证任务 ≠ messy 真实影响；无瓶颈观察 ≠ 已预言失控时间表」。

- 安全治理：把「加速区间 + 证据可见度」写进董事会材料，而不只贴模型榜。
- 研究者：读 METR 原文附录，分清主观综合与可公开 AECI。
- 读者：转发时带「评估窗与不确定性区间」，别只留一个「2×」标题。

教程：以 [METR 原文](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/) 为准。本条未核到针对该评估的成熟跟练片。

## YC 与生态

### 10. YC：W27 逾期仍审，F26 Demo Day 12-02；Launch 合集

YC Apply 本轮再核验：W27 准时截止已过，仍收逾期；准时申请约 **December 11** 前获决定；F26 Demo Day 仍定 **December 2**。同窗较强 Launch 并入一条：**Rivet**（W23）开源 Actor 编排（自称冷启 p99 约 **4.9 ms** vs sandbox 约 **1.7 s**）；**Limnion**/Siglake（F26）Agent-first 遥测湖仓；**Databuddy**（F26）无 cookie 产品分析 + MCP；**Asim** 真机物理安全极限测试；**Hesper AI** 财险理赔端到端 Agent（人闸签字）；**Verno** 原生改 P&ID；**Vorelios** 跨物理场秒级预测；**Kino AI**（S23）代码优先视频编辑（Pro 约 **$25**/席/月）。Phone Harness 已写入第 4 条，此处不重复展开。跳过武器向等条目。

来源：[YC Apply](https://www.ycombinator.com/apply/)、[YC Demo Day](https://www.ycombinator.com/demoday/)、[Launch HN·Rivet](https://news.ycombinator.com/item?id=50381687)、[Launch YC·Limnion](https://www.ycombinator.com/launches/WhD-limnion-telemetry-storage-built-for-the-agentic-era)、[Launch YC·Databuddy](https://www.ycombinator.com/launches/WsC-databuddy-product-analytics-for-founders-without-a-data-team)、[Launch YC·Asim](https://www.ycombinator.com/launches/Wsw-asim-find-your-robot-s-safety-limits-before-deployment)、[Launch YC·Hesper AI](https://www.ycombinator.com/launches/WpY-hesper-ai-ai-agents-that-work-every-insurance-claim-end-to-end)、[Launch YC·Verno](https://www.ycombinator.com/launches/Wil-verno-ai-that-edits-and-checks-the-engineering-documents-behind-every-industrial-plant)、[Launch YC·Vorelios](https://www.ycombinator.com/launches/Whd-vorelios-ai-that-can-engineer-anything)、[Launch HN·Kino AI](https://news.ycombinator.com/item?id=50368804)

批次窗还开着，校友却已在卖「真机、理赔、工业图、遥测湖」——和终端闸、企业 Agent 面是同一条垂直落地潮。受益的是仍想冲 W27 的团队、做 Agent 可观测与垂直人闸的工具；付钱的是把逾期写成「与准时同等承诺」、或把 Launch 自报基准写成「已替代 Datadog/Premiere」的人。标「逾期仍审 ≠ 保证面试；Demo Day 日期 ≠ 已公开完整榜单；各 Launch 数字多为公司口径」。

- 想申请 W27：还能交，别再等完美叙事。
- 观察并购与垂直：真机 Harness、理赔人闸、工业文档比「再训一个小模」更好讲清楚谁付钱。

教程：申请以 [YC Apply](https://www.ycombinator.com/apply/) 为准。

## 观点洞察

### 钱包、终端、闸：Agent 碰到账户与设备的三道账

昨天写的是写码 Agent 的壳、闸、邻居。今天材料换了场地：银行流水、手机屏幕、进网通知与非人身份。

先说**钱包**。Claude Personal Finance 经 Plaid 只读连上美区用户的卡与账户；Dropbox 要把文件柜收成 Agent 可读可写的对象存储；ElevenMusic 直发 SoundCloud，是内容侧的「钱与分发」闭环。钱包，指的是 Agent 能不能看见——以及将来会不会动到——你的余额、订阅与文件资产，不是又一个理财聊天框。

再说**终端**。Phone Harness 与 Glasshand 让 Agent 点真 iPhone；Muse 把通话做成默认入口；Edits Mac 用 MCP 把粗剪接进桌面时间线；工信部通知则把「预置智能体的手机/平板」拉进进网与 OTA 闸。终端，指的是 Agent 的手落在哪块玻璃上、短信与 2FA 谁能读，不是演示里的模拟器截图。

最后是**闸**。GPT‑6 Cyber 升到 Critical 却只给 Daybreak Red；Claude Enterprise 用 Security Center 与 inference hooks 拦工具调用；Palo Alto 据报要花约 **$500M** 买 Clutch 管非人身份；DOJ 成立 Super Intelligence Task Force；METR 则用约 **2×** 提醒：实验室自己也在加速，但证据大量打码。闸，指的是谁批准、谁审计、谁在执法名单上，不是模型卡上的安全形容词。

我自己读材料时会多问三句：

1. **钱包：** 这个 Agent 对账户/文件是只读、计划-批准，还是可写可转？训练与枢纽外对话的隐私边界写清了没有？
2. **终端：** 点按发生在用户本机、托管真机，还是模拟器？短信/eSIM/登录态的持有人是谁？进网与调用声明过了没有？
3. **闸：** 工具调用有没有企业 DLP hooks？非人身份谁轮换？安全专用模有没有 Daybreak 类准入，而不是「会拒绝」一句口号？

过得了这三问，再谈 Omni 的 **15** 秒、Inkling 的开权意向、或 Airbnb 的 **2027 H1** 也不迟；过不了，再响的「Agent 同事」叙事，都只是还没写进银行同意书、进网检测与采购合同的能力清单。个人观点，数字以各条原文为准，不构成投资或采购建议。

## 今日机会总结

今天的脊柱是：**frontier 产品双发**（GPT‑6 Cyber + Omni 1.2 Flash）与**开源/闪档多模态**（Inkling / Hy4 / Ling），**钱包与文件入口**（Personal Finance、Dropbox×Tigris），**终端与进网**（Phone Harness / Glasshand / 工信部），**企业常驻面**（Teammates / Live Apps / Airbnb 窗口），以及**安全与执法闸**（Clutch 谈判、Security Center、DOJ-SITF、METR 约 **2×**）。观点侧把钱包 / 终端 / 闸收成三道账。

若只选三条可执行方向：

1. **只读钱包与计划-批准文件层**：对标 Personal Finance 与 Dropbox「先计划再批准」，做订阅审计、异常扣费、文件 Agent 的权限与导出层；客户是怕 Agent 乱动资产的个人与 IT。
2. **真机 computer-use + 进网合规包**：对标 Phone Harness / Glasshand 与工信部通知，卖隔离号真机池、擦除 SOP、适配公示与调用声明工具；客户是要上架的终端厂与怕封号的 Agent 产品。
3. **非人身份与工具调用闸**：对标 Clutch 赛道与 Claude hooks，做 API 密钥生命周期、pre-tool-call deny、审计报告；客户是被 Agent 放权吓到的安全采购，不是只要「更聪明模型」的演示买家。

## 普通人今天就能做的 3 件事

1. **美区 Claude 付费用户：** 打开 [Personal Finance Help](https://support.claude.com/en/articles/18185620-use-personal-finance-in-claude)，若侧栏已有入口，先只连一张消费卡，问「上月订阅清单」——对完银行再决定是否加账户。
2. **有 Google 账号的人：** 打开 [vids.new](https://vids.new) 或读 [Omni 1.2 Vids 博文](https://blog.google/products-and-platforms/products/workspace/omni-1-2-flash-google-vids/)，用月免额度试一条 **15** 秒品牌静帧，别先拿测试 prompt 烧光。
3. **用 Cursor 付费 + Cloud Agents 的人：** 读一眼 [Apps 文档](https://cursor.com/docs/cloud-agent/apps)，显式让 Cloud Agent「build an app」，Publish 前确认密钥检查过了——团队应用默认别公开。
