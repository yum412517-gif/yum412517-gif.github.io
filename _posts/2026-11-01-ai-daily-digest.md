---
layout: post
title: "AI 每日精选 | 2026-11-01：ChatGPT×Codex 共用额度；把成本账算清楚"
date: 2026-11-01 21:00:00 +0800
categories: [AI 新技术]
excerpt: "头条：ChatGPT 与 Codex 自 12 月起按 token 共用用量。观点谈成本：订阅额度账单、工厂编程成本、Flash 与 27B 的口径差、机房电费与社会许可的隐性账，以及 ernd 这类 AI 账单卡。另有 DeepSeek Superagent、Memdoor/GVS5H、YC Odin。"
image: /assets/2026-11-01-ai-daily-digest-cover.jpg
---
![AI 每日精选封面 2026-11-01](/assets/2026-11-01-ai-daily-digest-cover.jpg)


> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 今天最值得看的几件事

- **头条：OpenAI 帮助中心——自 12 月起 Plus / Pro / Business 的用量在 ChatGPT 与 Codex 间共享（按 token；Instant chat 不计）**。
- 开源 agent：DeepSeek 开源 **dsh-superagent-prototype**（研究原型；Bloomberg / SCMP 等已跟进转述）。
- 工厂物理 AI：HD Hyundai Robotics × Palantir——问题处理均时 **21.5→7.9** 天；编程成本目标降逾半。
- 推理时编排：GVS5H / Memdoor 多实例「账本式」协作——对齐 Fable 5 的数字要分清统计与成本口径。
- 数据中心：xAI Colossus 空污诉讼继续；TechCrunch 写数据中心已成中期选举议题（约 **$200B** 项目受阻）。
- 使用边界：Claude「训练更大模型」拦截 vs 帮助中心书面许可政策。
- YC：Odin Robotics + ernd 双 Launch；W27 申请约 **11-2** 截止催更。
- 观点：**把成本账算清楚**——token 池、产线工时、编排口径、机房隐性账，别只看标价。

## 工具与产品

### 1. OpenAI：ChatGPT 与 Codex 自 12 月共用用量额度（头条）

帮助中心页相对抓取约今早仍标近期更新。Plus / Pro / Business 自 **December** 起，ChatGPT 与 Codex 共用一份用量，按 **token** 计量；更强模型、更复杂任务消耗更多；**Instant chat 不计入**共享池。Settings → Usage 将显示合并剩余额度与重置时间；触顶可等重置、升级，或购买 credits（合格功能）。官方称多数用户不必比现在更频繁地等重置，但仍在为切换做准备。

来源：[OpenAI Help·Understanding ChatGPT and Codex usage limits](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits)

订阅产品在把「聊天」和「干活」收进同一张额度表。受益的是把 Work / Codex 当主生产力入口的人（额度可见性更好）；付钱的是以为 Instant 闲聊也在啃同一池、或 12 月前不看 Usage 的重度用户。标「12 月起效 ≠ 已公布各档具体 token 上限或精确切换日」，勿写成 Instant 也被计入或个人免费档已同步。

- Plus / Pro：每周看一眼 Settings → Usage，大任务前先确认剩余与重置窗。
- Business 管理员：把「聊天 + Codex」合并池写进内部用量规范，别按旧的「两边各算各的」排排期。
- 重度编码者：复杂 agent 任务别默认选最强模型硬刷；触顶优先看 credits 是否划算，再谈升级。

教程：以 [官方帮助中心](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits) 与 Settings → Usage 界面为准；本条不编造未核实的「共用额度迁移」操作视频。

### 2. DeepSeek：开源 dsh-superagent-prototype——仓库常驻编码 agent 研究原型

GitHub `deepseek-ai/dsh-superagent-prototype`，`created` 约昨 **17:32** 北京。面向**单个** GitHub 仓库的「尽量少占人注意力」主动编码 agent；打包为 DeepSeek Harness bundle；监听 GitHub（可选飞书），获准请求时开独立工作项/会话目录，完成后在原对话回复（如开 PR）；Web panel 展示需人处理项。README 写明：research prototype、非官方产品，与内部版及《Exploring Super-agent Design》不完全一致。今日 Bloomberg / Moneycontrol / Investing / Techmeme / SCMP 等主流转述「挑战 Claude Code」叙事——**合并来源，不另开条**。

来源：[GitHub·dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)、[docs/007-architecture](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/docs/007-architecture.md)、[Bloomberg via Moneycontrol](https://www.moneycontrol.com/artificial-intelligence/deepseek-drops-enhanced-coding-agent-with-aim-to-rival-anthropic-article-14065416.html)、[SCMP](https://www.scmp.com/tech/article/3372884/deepseek-unveils-ai-super-agent-coding-race-openai-anthropic)

「永远在线仓库同事」的开源参考实现，不是又一个聊天框。受益的是已用 DeepSeek Harness、想研究 Router→Worker / ticket 治理的团队；付钱的是把「MIT 开源」直接当「可无人值守任意私仓」的人。标「研究原型 ≠ 生产默认 DeepSeek 产品」与「MIT/需适配 ≠ 可无人值守任意私仓」。

- 平台工程师：先读 SETUP.md / deployment，用独立 agent GitHub 账号与隔离机；别把生产密钥塞进 executor 环境。
- 开源维护者：对照架构文看 ticket / mandate / panel，再决定要不要抄工作流，别抄「永远在线」口号。
- 媒体读者：SCMP / Bloomberg 标题偏「挑战 Claude Code」——以 README 的 research prototype 自述为准。

教程：以 [SETUP.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/SETUP.md) 与 [docs/006-deployment](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/docs/006-deployment.md) 跟做（官方建议让 coding agent 读 SETUP 逐步问你）；本条不编造未核实的专属评测片。

### 3. HD Hyundai Robotics × Palantir：物理 AI 试点——21.5 天到 7.9 天

Yonhap / Korea Herald 等周日报道。自 **8 月**试点：AI agent 先分析既有机器人程序并提出改进，工程师再按现场经验精炼；相关问题处理平均耗时 **21.5→7.9** 天（约 **63%**）；公司预期机器人编程成本可降逾 **50%**。CTO Ahn Seong-hwan 于纽约 Palantir Sovereignty Bootcamp 作主题分享；双方将设高管 steering committee 扩场景；现场工程师角色拟从基础编程/调试扩展为「现场方案专家」。

来源：[Yonhap](https://en.yna.co.kr/view/AEN20261101001300320)、[Korea Herald](https://www.koreaherald.com/article/10921723)、[Korea Times](https://www.koreatimes.co.kr/business/tech-science/20261101/hd-hyundai-robotics-palantir-to-slash-robot-programming-costs-with-ai)

工厂里的 AI 不是多一个聊天窗口，而是把「示教—试跑—改路径」里最耗人的一段变成「提案 + 人审」。受益的是工业机器人软件栈、仿真与 Palantir AIP 类平台；付钱的是把试点均时写成「已取消全部现场工程师」的材料。标「试点均时与成本目标 ≠ 已全产线商用替代全部示教编程」，勿写成 Palantir 已收购机器人硬件。

- 制造业 IT / 自动化：先选可量化的编程/排障工单，记均时与返工率，再谈扩场景。
- 现场工程师：角色在往「定义问题 + 审 AI 提案」走——经验仍是终审，不是被替换掉的零件。
- 采购：问清数据是否出厂、仿真与实机闭环谁负责，别只买「物理 AI」四个字。

教程：以韩媒报道与双方公开口径为准；Palantir 平台侧可看官方 [Building with Palantir AIP](https://www.youtube.com/playlist?list=PLqTLGbLI0Cvmn-o_mZKkG7mr-TztcKFNZ) 播放列表（**同类操作参考**：AIP 工作流，非本条机器人编程专属片）。本条不编造未核实的「21.5→7.9 天复现」视频。

## 模型发布

本窗无新西方/国内商业旗舰权重一手首发（周日薄窗）。开源侧见上 DeepSeek superagent 原型——属 agent 运行时，不是新 frontier 基座权重。

## 论文研究

### 4. GVS5H / Memdoor：无训练「账本式」多实例编排——数字要对口径

GVS5H（Gorilla vs. 5 Humans）：新鲜同模型实例经共享文件系统（plan / notes / 当前解）分解与协作，无额外训练。作者表称本地 **Qwen3.8-27B** manager 臂 LiveCodeBench Hard 近 **100** 题 pass@1 约 **92.4%**，对照 Fable 5 单次约 **90.4%**（Holm 校正后 p≈0.88，**不可称统计显著击败**）。「约 **9%** 成本」属 **Qwen3.8-Flash-Next** manager 臂相对 Fable 5，**不是** 27B；27B manager 成本口述约 Fable 的 **~78%**。Memdoor 为 CLI agent，含 team-solve 工作流示例；HN 标题「5×Qwen3.8-27B beats Fable 5」属简化传播。

来源：[GitHub·slee-persis/GVS5H](https://github.com/slee-persis/GVS5H)、[GitHub·guregodevo/memdoor](https://github.com/guregodevo/memdoor)、[Authon 读表澄清](https://blog.authon.dev/qwen3-8-27b-vs-fable-5-coding-benchmark-gvs5h-real-numbers)、[HN·Memdoor](https://news.ycombinator.com/item?id=50320995)

推理时组织有时比「再买一张旗舰票」更接近问题。受益的是开源 harness、本地 27B 部署与评测工程；付钱的是把 HN 标题直接写进 BP、却分不清 Flash-Next 与 27B 成本臂的人。标「对齐 ≠ 全面超越 Fable」「Flash-Next 9% ≠ 27B 成本」与「单基准/作者表 ≠ 第三方全面复现」。

- 评测工程师：复现时固定后端、记清 Holm 校正与成本臂，别只贴 pass@1。
- Agent 开发者：学「共享文件系统当账本 + 测试脚本判成败」，别学「五个模型喊话就赢了」。
- 采购小模型的人：问供应商要的是编排增益，还是单次调用分数。

教程：以 [GVS5H README](https://github.com/slee-persis/GVS5H) 与 [Memdoor team-solve 示例](https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve) 跟做；多 agent 编排思路可参考 [Claude Code Multi-Agent Orchestration（同类操作参考）](https://www.youtube.com/watch?v=RpUTF_U4kiw)——讲的是编排范式，不是 GVS5H 复现片。本条不编造未核实的「击败 Fable 5」评测视频。

## 最佳实践

### 5. Apple Ternus：「不为 AI 而发 AI」

TechCrunch 转述 Wired 访谈（署约 **10-31** PDT，北京已入 **11-01**）。Apple CEO John Ternus 称喜欢当前 AI 站位；会在新产品中「绝对」用 AI，但 **「We don't want to ship AI for AI's sake」**——做对时用户不必分辨是 AI 还是传统软件，关键是否做出真正喜爱的产品；被问及 agent 是否会让 app 多余时，称产品创造仍是深度人性的事。

来源：[TechCrunch](https://techcrunch.com/2026/10/31/apple-ceo-says-the-company-doesnt-want-to-ship-ai-for-ais-sake/)

这句话适合当产品评审的过滤器，而不是当「Apple 弃云端大模型」的谣言燃料。受益的是真正解决任务的垂直产品；付钱的是功能列表里只写「接入 GPT」却说不清用户多爱用一分钟的人。标访谈口述，勿写成 Apple 已放弃全部云端大模型或 Siri AI 路线图变更公告。

- 产品经理：上线前问一句——关掉 AI 角标，用户还爱不爱用。
- 创业者：BP 里少写「我们用了某某大模型」，多写完成率与留存。

教程：以 [TechCrunch 原文](https://techcrunch.com/2026/10/31/apple-ceo-says-the-company-doesnt-want-to-ship-ai-for-ais-sake/) 为准；本条不编造未核实访谈片。

### 6. 数据中心合规与反弹：Colossus 诉讼继续 + 中期选举特写

两条同属「基建要过社会许可」，**并列叙事、非同一条**。

**xAI Colossus：** 联邦法官 Debra M. Brown 驳回 xAI 驳回动议——NAACP（南方环境法中心代理）Clean Air Act 公民诉讼继续；指控至少约 **35** 台燃烧轮机等未获建设/运行空气许可。xAI 主张轮机属「移动源」豁免且原告无资格；裁定原告有法定资格、密西西比 SIP 下非 mobile sources、公民诉讼条款未违宪。NAACP 称此前 DOJ 类似动议本月亦被驳。

**TechCrunch 中期选举特写：** 即使在布鲁克林，选举讨论也反复回到 AI 与数据中心反弹；援引 Data Center Watch——**2026** 上半年近 **$200B** 数据中心项目因政治与社区反对被推迟、搁置或叫停；宾州/乔治亚/德州/纽约/弗吉尼亚等考虑更多护栏；现场对「挺 AI 数据中心」提问遭嘘。叙事对照工会短期建设就业 vs 建成后常设岗稀少、社区「缺乏同意」与环境健康担忧。

来源：[TechCrunch·Colossus](https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/)、[TechCrunch·中期选举](https://techcrunch.com/2026/10/31/data-centers-are-now-a-midterm-issue-even-in-brooklyn/)

算力叙事从「再建一座」走到「邻居同不同意」。受益的是环境合规咨询、社区联络（liaison）岗与能讲清电费/噪音/排放的运营商；付钱的是把「诉讼继续」写成「已关停」、或把「$200B 受阻」写成「全美禁令已通过」的人。标「诉讼继续 ≠ 已判违法或已关停 Colossus」；特写为观察与第三方报告转述，勿写成中期选举结果已定。

- 基建 / 能源从业者：环评、空气许可与社区沟通进关键路径，别只盯 MW  headline。
- 投资者：区分「洽谈中的机房」与「已并网且许可齐备的产能」。
- 读者：两条都是合规与政治压力，不是产品发布会参数。

教程：以两篇 TechCrunch 原文为准；本条不编造未核实的诉讼庭审或选举片。

### 7. Claude：训练更大模型拦截 vs 帮助中心政策

HN 热议个人账号（含港区等口述）凡触及「训练更大/竞品模型」即被标「training a competitor」拦截。对照官方帮助中心（署 **2026-03-16**）：客户拥有 Outputs，但**未经书面许可**不得用服务训练/开发 AI 模型；允许训非竞品专用工具（情感/分类/摘要/抽取/语义检索/异常检测等）；禁止训通用聊天、开放式生成、以 Outputs 为训练目标、反推训练方法等。社区另有 VPN / 信任分 / 数据标注触发等假说——**官方本窗无新公告**。

来源：[Claude Help·Can I use my Outputs to train an AI model?](https://support.claude.com/en/articles/12326764-can-i-use-my-outputs-to-train-an-ai-model)、[HN](https://news.ycombinator.com/item?id=50319358)

ToS 摩擦会越来越多地长成产品体验。受益的是合规咨询与「分类器/抽取」等明确白名单场景；付钱的是把研究讨论写成「请帮我训一个对标 Claude 的基座」的人。标「个人遭遇与帮助中心政策 ≠ 新发布全面封杀一切 ML 讨论」，勿写成 Anthropic 已禁止全部学术研究问答。

- 研究者：问架构与公开论文可以，别把「用 Outputs 灌一个通用竞品」写进 prompt。
- 企业客户：合同与书面许可另谈；默认假设「聊天记录可拿去训自家通用模型」会踩线。
- 普通用户：分类、摘要、检索类专用工具仍在帮助中心允许范围内——先读原文再设计工作流。

教程：以 [Claude 帮助中心原文](https://support.claude.com/en/articles/12326764-can-i-use-my-outputs-to-train-an-ai-model) 为准；本条不编造未核实的「绕过拦截」视频，也不提供任何规避步骤。

## YC 动态

### 8. Odin Robotics + ernd：工厂臂与 AI 账单卡，外加 W27 催更

**Odin Robotics（YC F26）：** 创始人公开「We just launched」——AI 驱动机械臂嵌入**现有**产线，做 CNC 上下料、传送带装箱、码垛等；强调确定性控制 + 学习技能应对换产/不规则件，而不是为机器人重建整线。YC 官方 RT。可与上条 HD Hyundai×Palantir **并列具身/工厂自动化、非同一条**（一条是编程/排障软件成效，一条是嵌入产线的臂）。

**ernd（YC F26）：**「The credit card for the AI stack」——面向支付 AI 账单的美国公司；口述 AI 供应商消费约 **4%** 返还（部分伙伴 **5%**），协商额度/容量优惠；Priority GPU and inference capacity 标 **Coming soon**；官网开放 request card。官网自述独立、厂商不背书。

**W27：** `@ycombinator` 提醒 Winter 2027 申请约 **2** 天后截止（**November 2**）；列 $500K、tokens/credits 等。昨已录 Early Access——本轮仅作催更。

来源：[Launch YC·Odin](https://www.ycombinator.com/launches/WJg-odin-robotics-robot-arms-that-do-repetitive-manual-work-in-existing-factories)、[odin-robotics.com](https://odin-robotics.com/)、[ernd.io](https://ernd.io/)、[YC·ernd](https://www.ycombinator.com/companies/ernd)、[ycombinator X·W27](https://x.com/ycombinator/status/2116600929382527221)

一边是产线里的重复劳动，一边是云账单上的重复扣款——YC 本窗两条都在「嵌进现有流程」而不是「重建世界」。受益的是工厂自动化集成商与 AI 支出管理；付钱的是把 Launch 帖当成「已规模化替代全部工位」或「已全面发卡」的人。标「X 公开推广窗 ≠ Launch 页首次创建日」「试点交付 ≠ 已规模化替代全部人工工位」；ernd 标「early access / Final terms come with the card ≠ 已全面发卡或已绑定 OpenAI/Anthropic 官方赞助」。

- 工厂运营：Odin 类方案先问换产时间、不规则件失败率与安全围栏，再谈「AI」。
- 初创 CFO：ernd 先看条款与返点是否覆盖你的真实供应商清单；Coming soon 的 GPU 优先权别写进本季预算。
- 想申请 W27：截止约 **11-2**，材料先交再磨。

教程：Odin 官方 Demo 见 [YouTube](https://www.youtube.com/watch?v=K-Mein4nAlA)（Launch 页同源演示）；ernd 以 [ernd.io](https://ernd.io/) 申请页为准，本条不编造未核实开卡教程。

## 观点洞察

### 把成本账算清楚：token、工时、口径与隐性账

今天几条新闻其实在问同一件事——**钱和工时到底花在哪儿**，以及你报表上写的「便宜」，是不是换了口径的便宜。

先看订阅。OpenAI 自 **12** 月起让 ChatGPT 与 Codex 共用一份 token 池，Instant 不计。表面上还是同一个 Plus / Pro 月费，账单结构变了：闲聊摸鱼和跑 agent 任务抢同一杯水。以前你可以假装「聊天归聊天、编码归编码」；合并之后，Usage 页上的剩余额度就是唯一的真话。我自己会养成一个习惯：大任务前先看表，复杂推理别默认拉满最强模型——触顶再买 credits，往往比事后抱怨「额度怎么突然没了」便宜。Ternus 那句「不为 AI 而发 AI」在这里可以当配菜：功能该不该上，是产品问题；上了之后每一跳花多少 token，是成本问题。两边都要过，缺一不可。

工厂那边给的是另一张账本。Hyundai × Palantir 试点把问题处理均时从约 **21.5** 天压到 **7.9** 天，编程成本目标降逾半。注意：这是**试点均时与成本目标**，不是「现场工程师可以裁光」。省下来的，首先是示教、试跑、改路径里最耗人的那一段；人还在，只是从手写每一行，变成审 agent 提案。Odin 嵌进现有产线做上下料，逻辑类似——不砸整线，先抠重复劳动的单位成本。物理世界的 AI 省钱，最后一定要落到「天」和「元」，演示片里的流畅度不算数。

再往下是评测口径。GVS5H / Memdoor 这波最容易被标题带跑：「五小模型打败 Fable」。细看才发现，**约 9% 成本**说的是 Flash-Next 那条臂；本地 27B manager 口述大约是 Fable 的 **~78%**，而且 Holm 校正后并不能喊「统计显著击败」。同一套「便宜」，换一条臂数字差一截。采购或写材料的人若把 Flash 的 9% 和 27B 的分数糊成一句话，后面对账会很难看。我的读法很土：先问「这个百分数对应哪条模型臂、含不含编排开销」，再谈要不要上生产。

最外面一圈是机房。Colossus 诉讼继续、中期选举特写里近 **$200B** 项目因社区反对受阻——电费、空气许可、邻居同不同意，都是**不出现在 GPU 单价表上的成本**。延期几个月的融资成本、公关与合规律师费，往往比再谈一轮芯片折扣更疼。ernd 这类「AI 栈信用卡」盯的是另一头：云账单每月划走的那一笔，想用返还和额度谈判把单位成本压一点。Coming soon 的 GPU 优先权先别写进本季预算，但「AI 支出要单独记账、别和差旅糊在一起」这件事，现在就可以做。

所以我给自己列了四道对账题，写材料或拍板前过一遍：

1. **订阅池：** 聊天和 agent 是否已抢同一杯水？触顶路径是等重置、升级还是 credits？
2. **产线工时：** 省的是天和人，还是只是 PPT 上的「智能化」？
3. **评测口径：** 便宜的是哪条臂？显著吗？复现成本谁出？
4. **隐性账：** 电、许可、社区反对导致的延期，有没有进关键路径？

过得了这四问，成本故事才站得住；过不了，再响的「降本」口号都只是换了个说法的加预算。个人观点，数字以各条原文为准，不构成投资或采购建议。

## 今日机会总结

今天的脊柱是：**订阅额度合并**（ChatGPT×Codex）、**开源常驻仓库 agent 原型**（DeepSeek）、**工厂物理 AI 试点数字**（Hyundai×Palantir）、**推理时多实例编排的口径战**（GVS5H/Memdoor），以及 **数据中心社会许可**。观点侧把几条串成同一本成本账：token 池、产线工时、评测口径与机房隐性账。

若只选三条可执行方向：

1. **用量治理与成本可见性**：帮团队做 ChatGPT/Codex（及多厂商）合并池看板、任务级 token 预算与触顶告警；客户是 12 月切换前后怕「额度突然打穿」的中小团队。
2. **产线 AI 提案 + 人审交付**：对标 Hyundai 试点，卖「机器人程序分析 / 排障工单均时」试点包；赚钱点是可审计的提案与工程师工作流，不是又一个聊天机器人。
3. **开源 harness 评测与私有化**：GVS5H / Memdoor 类账本编排 + 本地 27B，帮客户分清「对齐」与「显著击败」、Flash 臂与 27B 臂成本；客户是舍不得全量旗舰、又想要编码 pass 率的中台。

## 普通人今天就能做的 3 件事

1. **付费用 ChatGPT / Codex 的人：** 打开 Settings → Usage，搞清当前剩余与重置时间；大任务前先估模型档位——12 月共用池生效前，先养成看表的习惯。对照 [帮助中心](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits)。
2. **管账单 / 写需求的人：** 列一张小表——这个月 ChatGPT/Codex（或其它模型）花在「闲聊」和「真干活」各多少；大任务默认降一档模型试一次，再决定要不要拉满。
3. **想申请 YC W27 的人：** 截止约 **11-2**，今天把材料交上去比再打磨口号更重要。

---

*草稿待审阅：确认后我再发到博客。有要改的直接说。*
