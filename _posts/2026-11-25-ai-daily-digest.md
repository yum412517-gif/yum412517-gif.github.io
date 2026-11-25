---
layout: post
title: "AI 每日精选 | 2026-11-25：代理接到审批和办公数据了，先看必须走哪扇门、规则写在哪、哪一步还要人点头"
date: 2026-11-25 21:00:00 +0800
categories: [AI 新技术]
excerpt: "头条：补录 11-23，Anthropic 发布仍在测试的 Claude Ship，可按团队写在仓库里的政策审阅、修复并批准拉取请求，但对零数据保留、HIPAA 配置和客户托管密钥的组织暂不开放。11-24，Google 宣布 Workspace 的 MCP 服务器与 CLI 正式可用，并配上 Cloud Agent Gateway；代理须走这两扇门，技术强制自 2027 年 2 月 1 日起，用量配额自 4 月 1 日起计费，发邮件、改共享和批量编辑前仍要人确认。同一逻辑也出现在 Anthropic 的企业前沿安全保障公开测试，以及 AWS 上面向 Claude 的可信访问接口。观点是代理接到审批和办公数据了，先看必须走哪扇门、规则写在哪、哪一步还要人点头。"
---
![AI 每日精选封面 2026-11-25](/assets/2026-11-25-ai-daily-digest-cover.jpg)

> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 代理接到审批和办公数据了，先看必须走哪扇门、规则写在哪、哪一步还要人点头

今天最显眼的，不是又多了一个模型名字，而是代理已经接到两处很要害的地方：一处是代码仓库里的批准，另一处是邮箱、文档和日历里的办公数据。但接到了，并不等于谁都能开，也不等于它能自己把最后一步点掉。补录 11-23：Anthropic 的官方署文把 [Claude Ship](https://claude.com/resources/articles/introducing-claude-ship) 写成当天起以测试版提供，面向 Claude Team 和 Enterprise、而且只接 GitHub。它由已经正式可用的 Code Review，再加上仍在测试的 PR Steward、Claude Approvals 组成；开发者可以在 Claude Code 里运行 `/ship`，管理员也可以按仓库打开，让它在拉取请求上自动跑。批准与否看的是团队写在仓库里的政策文件，官方建议多数客户先用观察模式。PR Steward 被设计为不批准、不合并。用量按 token 计，观察模式也可能因为政策引用了 Claude 的审查而产生 Code Review 账单。零数据保留、HIPAA 配置或客户托管加密密钥的组织，官方写了现在还不能用。11-24，Google 的 [Workspace 博文](https://workspace.google.com/blog/product-announcements/built-for-trust-and-control-new-ai-agent-protections-and-developer-tools-in-google-workspace) 和 [Cloud 博文](https://cloud.google.com/blog/products/identity-security/deploying-agents-safely-in-your-enterprise) 宣布 Workspace 的 MCP 服务器与 CLI 正式可用，并同时推出 Google Cloud Agent Gateway。官方写，AI 代理须经这两扇门，而不是传统 REST 接口，技术强制自 **2027 年 2 月 1 日** 起；用量配额自 **2027 年 4 月 1 日** 起计费。发邮件、改 Drive 共享权限、做批量编辑之前，仍要人确认。用户以后在自己这边查看并撤销代理对邮件和文件的访问，以及把最敏感的邮件、文件对外部代理关掉，官方都还写着即将推出，不能当成今天已经能开的开关。同一日，AWS 宣布 [Bedrock 可信访问计划接口](https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-trusted-access-api-with-anthropics-enterprise-frontier-safeguards-and-enterprise-data-controls/) 正式可用，并为企业前沿安全保障、企业数据控制给出面向 Claude 的公开预览：数据放在客户自己的账户，或放在 Amazon 管理的存储里，监测到风险后生成供客户审阅的安全案例。这和补录 11-23、Anthropic 把[与零数据保留兼容的企业前沿安全保障](https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards) 开到公开测试，是同一条线上的事。再往日常使用上看，11-24 豆包的[小豆产品页](https://www.doubao.com/xiaodou/)已经可以打开，官方把它写成一个会主动办事、并能在授权后连接抖音、飞书、日历等应用的个人助理，连哪个、断哪个由你决定；至于邀请制公测和获赠免费额度，今晚核到的是 [IT之家](https://www.ithome.com/1/031/329.htm) 对豆包官方当日宣布的转述，产品页本身没有抽出这些句子，也就不能写成已经核对过的官网原句。代理接到审批和办公数据了，先看必须走哪扇门、规则写在哪、哪一步还要人点头。

个人观点，不构成投资、采购或技术选型建议。数字和能力边界以各条原文为准。

## 今天最值得看的几件事

- **头条：代理接到了批准和办公数据，但门、政策和人点头的步骤是分开写的。** 补录 11-23 的 Claude Ship 可以按仓库里的政策批准例行变更，官方仍建议先观察，也不对零数据保留、HIPAA 配置和客户托管密钥的组织开放。11-24 的 Workspace MCP 与 CLI 正式可用，强制走这两扇门要从 **2027 年 2 月 1 日** 算，配额计费要从 **4 月 1 日** 算；发邮件、改共享、批量编辑前仍要确认。「即将推出」的用户撤销和敏感文件限制，不要写成今天已经能用。AWS 上的可信访问接口是正式可用，Claude 的两项数据控制仍是公开预览，还要先看资格再加入。
- **模型这一侧，今天更硬的是开源和自评，不是新的通用聊天旗舰。** 11-24 商汤发布并开源 SenseNova U1.6，官方强调 8B 模型的原生图像自修正；美学和 UltraTextBench 数字是官方自评，Token Plan 写的是注册用户限时免费体验。OpenAI 帮助中心已经可以读到 Responses API 里的医疗模型配置，文中举了 `gpt-6.2-astra-healthcare` 为例，但官方 changelog 今晚打开是 403，所以不上线日期、也不把媒体列出的其他模型 ID 写成已经核对过的清单；它也不等于可以处理受保护健康信息，更不是医疗器械批准。
- **中段可以收成一组。** 11-24，Claude 把 artifact 装成 Mac / Windows 应用的能力以测试版滚动推出，完整电脑权限有明确限制。同一天，Skills over MCP 进入公开测试，Tasks 和 Elicitation 对部分套餐宣布正式可用。补录 11-23 夜间到 11-24 凌晨：Gemini API 的文件切片只为实际检查的部分计费；Search 的 Personal Intelligence 可选择加入 Wallet 和 Drive。OpenAI 与 Cisco 的 Shirudo 是开源运行时，不要写成已经全面可用。小豆的产品页是官方的，邀请制公测目前按媒体转述来写。OpenWorks 的项目页今晚可以打开，但 OpenAI News RSS 里还没有单独署文，所以不上头条。
- **研究署文不少，都要按自称和未完成的验证来读。** 北京时间今天凌晨，Google DeepMind 推出 Humanity’s First Exam，测的是日常问题上能不能反复做对，榜是主办方榜。11-24，OpenAI 发了蛋白质设计署文，以及用 Astra、Codex 在公开望远镜数据里找出系外行星候选的故事；候选还不是已确认的行星。官方 GitHub 数学仓库同日放上矩阵乘法指数为 **9/4** 的预印本，今晚 HN 讨论分很高，但这是预印本里的证明声称。补录 11-23，DeepMind 还写了用 Gemini 4 代理团队改进量子算法、并用 Lean 做形式化验证，倍数都是官方自称。
- **YC 核验：** 今晚约 **20:11** 重新打开 `launches.json` 时，按时间倒序栏顶是新出现但票数偏低的 Altair Health（**4** 票）、Light Anchor（**11** 票）、Boat（**8** 票）、Vestris（**16** 票）等，不单列展开，也不写「现居顶」。已在 11-21 写过的 River 现为 **25** 票，Morphy（公司名栏为 MouseCat）**11** 票，FlashDrive **30** 票，仍见栏内，不再展开。Winter 2027 申请仍在接受迟交，准时截止日期 **November 2** 晚上 **8pm PT** 已过；F26 Demo Day 仍为 **12 月 2 日**（周三）。

## 通道、规则与还要人点头的那一步

### 1. 补录 11-23：Claude Ship 可以按仓库政策批准拉取请求，但还在测试，也不是谁都能开

Anthropic 的署文栏面日期是 **November 23, 2026**，[介绍 Claude Ship](https://claude.com/resources/articles/introducing-claude-ship)。它没有写进 11-23 那天的冻结笔记，今晚也没从可用的官方 RSS 里核到精确时刻，所以这里按补录来写，不把「一定是当晚 19:20 之后才上线」说成已经核对过的时间事实。产品页在 [claude.com/product/claude-ship](https://claude.com/product/claude-ship)，命令说明在 [文档](https://code.claude.com/docs/en/ship-command)。

官方把 Claude Ship 拆成三块：已经正式可用的 Code Review，以及仍在测试的 PR Steward、Claude Approvals。开发者更新 Claude Code 后，可以在自己的变更上运行 `/ship`：它会推送、打开拉取请求、做审查，并处理反馈和失败的检查；最后能不能合并，仍取决于这个人的权限和仓库的分支规则。管理员也可以按仓库打开，不必每次手敲命令。Claude Approvals 读取默认分支上的政策文件，政策允许时可以批准例行变更，也可以要求人来签字；官方把它比作更聪明的 CODEOWNERS，并建议多数客户先用观察模式，再考虑把分支保护改成必须过它这一关。PR Steward 处理失败的检查、合并冲突和审查意见，官方写它被设计为不批准、不合并；每次推送后会留言说明改了什么、怎么撤回，也可以用 `@claude` 指令干预或让它停下。

谁能用，写得很清楚：Claude Team 和 Enterprise，仓库要在 GitHub。零数据保留、HIPAA 配置或客户托管加密密钥的组织，官方写暂不可用。计费按 token，管理员可以为 Code Review 和 PR Steward 设置支出上限；Approvals 没有基础费用，但政策里的分类器按 token 计，而且只要政策用了 Claude 的审查，即使还在观察模式，也会触发一次计费的 Code Review。运行 `/ship` 计入常规的 Claude Code 用量。符合条件的 Enterprise 组织可以领取至少 **10,000** 美元的 Claude Ship 积分，须在领取后 **30** 天内用完，领取截止日是 **2027 年 1 月 15 日**，条款适用。署文里 Claude Code 团队自称，6 月到 9 月，在把 Claude 的审查当作更广流程中一层的前提下，合并的拉取请求超过翻倍，回退比例下降超过 **40%**，这是官方自己的观察，不是独立评测。

对已经在用 Claude Code 的软件团队、以及要给产品经理或支持人员一条受控提交通道的工程负责人来说，这可能降低「审查和批准跟不上写代码速度」的摩擦；但观察模式不是免费彩排，政策文件写得宽，等于把批准权提前交给模型，这两个都值得先想清楚。

### 2. 11-24：Workspace 为代理开了正式的门，强制和计费都在后面，高影响操作仍要人点头

Google Workspace 的署文日期是 **November 24, 2026**，见[这篇产品公告](https://workspace.google.com/blog/product-announcements/built-for-trust-and-control-new-ai-agent-protections-and-developer-tools-in-google-workspace)；Google Cloud 同一天发了[企业侧的配套说明](https://cloud.google.com/blog/products/identity-security/deploying-agents-safely-in-your-enterprise)。[Workspace AI Tools Addendum](https://workspace.google.com/terms/ai-tools/) 标明最近一次修改也是这一天。

官方宣布 Workspace 的 MCP 服务器和 CLI 正式可用，作为代理进入 Workspace 的两扇由 Google 管理的门。MCP 服务器面向云端和网页代理，开箱覆盖 Gmail、Drive、Docs、Sheets、Slides、Calendar、Chat 和 Tasks，Keep 还写着即将加入。CLI 面向本地、桌面代理和自动化，提供范围内的登录和结构化输出。Cloud 博文同时推出 Google Cloud Agent Gateway，用于 Google Cloud 上的模型、MCP 和 Agent2Agent 流量：按 Agent Registry 校验代理身份，执行 IAM 和默认拒绝的出站规则，并用 Model Armor 做提示注入筛查。

更关键的是规则，而不是「又能接上一种协议」。新的附加条款要求 AI 代理走 MCP 或 CLI，而不是传统 REST，技术强制从 **2027 年 2 月 1 日** 开始，官方写这是给迁移留的时间。外部代理必须使用专用的 OAuth 客户端 ID，并配上最小权限范围；限时批准还写着即将推出；用量配额从 **2027 年 4 月 1 日** 开始计费。日常起草和摘要可以自动跑，但在 Workspace 里，代理发邮件、更改 Drive 共享权限或做批量编辑之前，MCP 和 CLI 会要求明确的用户确认。管理员可以在管理控制台查看、审计和撤销代理；用户自己查看活动并撤销对邮件、文件的访问，官方写的是即将提供。把最敏感的邮件和特定 Drive 文件、文件夹对外部代理关掉，也还是即将推出，不要当成今天已经能勾上的选项。附加条款还写了代理不得把用户数据拿去永久原样存储或训练模型，派生数据要在规定窗口内删除，断开后也要删。

已经在用外部代理读写公司邮箱和网盘的团队，宜现在就看自己的连接是不是走这两扇门，别等到强制日再找接口。计费日也还早，但配额怎么设、确认规则谁来定，适合先在管理控制台里过一遍。

### 3. 补录 11-23 到 11-24：企业想把数据留在自己这边，官方给的是测试和预览，不是自动开通

补录 11-23：Anthropic 的产品更新把[与零数据保留兼容的企业前沿安全保障](https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards) 写成进入公开测试。署文解释，单条请求的分类器看不住跨多次、跨多个代理的滥用，所以要有一层跨请求的自动安全监测；在这套设计里，Anthropic 和云厂商不保留提示词与回复，客户自带 Amazon S3 或 Google Cloud Storage，监测在客户控制的存储上进行，发现风险后生成不含输入输出的安全案例，交给客户自己审阅。官方还写，运营人员不会人工审阅这些输入输出，数据也不用于训练。入口包括 Claude Platform、在 AWS 上的 Claude Platform、Amazon Bedrock，以及 Google Cloud 上的 Claude；Microsoft Foundry 写的是即将支持。符合条件的客户会收到启用说明，存储仍按云厂商的常规费用计。这不是对所有企业账户默认打开的正式可用功能。

11-24，AWS 机器学习博客宣布 [Bedrock 可信访问计划接口](https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-trusted-access-api-with-anthropics-enterprise-frontier-safeguards-and-enterprise-data-controls/) 正式可用，RSS 时间是 UTC **05:01:14**，大约北京 **13:01**。这个接口用来发现、申请并加入模型提供商的可信访问计划，管理员可以用已有的 IAM 和服务控制策略决定谁能加入。同一篇里，面向 Claude 的企业前沿安全保障和企业数据控制进入公开预览，文中写覆盖 Claude Fable、Claude Mythos，以及经网络安全验证计划使用的 Opus 5.5 和 Sonnet 5.5。前者把数据留在客户自己的 AWS 账户，Anthropic 和 Bedrock 都不保留提示词与回复；后者把保留数据放在 Amazon 管理的存储里，Anthropic 不保留。两者在监测到风险时，都会生成供客户审阅的安全案例。资格可能是已经符合、或需要先申请，批准和接受条款是分开的步骤，也可以随时退出。不要把这项预览写成所有 Bedrock 账户已经自动开通，更不要把它和接口本身的正式可用混成一件事。

一个值得单独记一笔的别扭是：Claude Ship 眼下不对零数据保留的组织开放，而企业前沿安全保障又正把零数据保留和安全监测放到一起测试。如果公司同时需要自动批准代码和把对话留在自己的桶里，这两条线现在还不能想当然地当成已经打通。

## 模型发布

### 4. 11-24：商汤开源 SenseNova U1.6，卖点是图里的字能自己改

商汤官网新闻的路径日期是 **2026-11-24**，见 [SenseNova U1.6 正式发布：美学进阶，字准意达](https://www.sensetime.com/cn/news/sensenova-u1-6-open-source-20261124-1152)。官方写，当天正式发布并开源，第一次为 U 系列的 8B 开源模型加上原生图像自修正：同一模型先出首稿，再对照原始提示检查画面里的文字问题，然后结合首稿和原提示生成修正版。[GitHub 仓库](https://github.com/OpenSenseNova/SenseNova-U1/) 的 `LICENSE` 今晚打开是 Apache License 2.0，README 也把发布日记在 **2026-11-24**，并写已有 4 步、8 步蒸馏变体，以及 ComfyUI 的官方支持。

评测数字都是官方自称：内部用户评测里，U1.6 Lite 的美学得分比 U1.5 Lite 高约 **10%**；在 UltraTextBench 的密集信息图测试中，单次生成是 **86.04**，打开自修正后到 **92.28**，相对提升约 **7%**。官方同时写，自修正训练主要针对信息图，尽管在部分非信息图场景里也看到了泛化，所以不要把它理解成所有海报、插画都会自动校对。产品入口写了商汤小浣熊、Seko、Kapi 相机、SenseNova Token Plan、SenseNova Studio 和 ComfyUI。Token Plan 的原文是注册用户可限时免费体验，不是无限期、无门槛的全面免费。

做活动海报、信息图或短剧视觉的人，如果已经在用小浣熊或 ComfyUI，可以按官方路径试试自修正前后差多少；但官方榜不能代替你自己这一批中文密集排版的验收。

### 5. OpenAI 帮助中心已列出医疗模型配置，不等于可以处理病历，更不是医疗器械批准

今晚打开的 [Healthcare model configurations in the OpenAI API](https://help.openai.com/en/articles/20001656-healthcare-model-configurations-in-the-openai-api) 写着大约 18 小时前更新过。文案说，这类配置面向 API 组织，不必先有 ChatGPT for Healthcare 或 ChatGPT Enterprise 工作区；在 Responses API 请求里指定受支持的医疗模型 ID，例如 `gpt-6.2-astra-healthcare`，并且必须启用网页搜索，才会走专用的医疗检索索引，用来回答临床问题、比较研究和做带引用的证据摘要。官方写，回答和引文都要先审再采信，这些配置不能替代专业医学判断。进入该配置本身，也并不授权处理受保护健康信息；若要处理这类信息，组织必须先与 OpenAI 签订适用的商业伙伴协议，并满足账户和工具配置要求。

官方 changelog 今晚打开是 HTTP **403**，所以我不以媒体报道里的上线日期或其他模型 ID，写成已经核对过的官方清单。开发医疗检索或文献综述工具的团队可以先读帮助中心和定价页，但不要把「API 里出现了 healthcare 这个后缀」理解成已经拿到器械许可，或已经可以合法处理病历。

## 中段简报

11-24，Anthropic 还发了 [把 artifact 安装成 Mac 和 Windows 应用](https://claude.com/resources/articles/install-as-app)，测试版正在 Claude 桌面端滚动推出。装好后会有自己的图标和窗口，底层 artifact 改了会自动更新，对 Claude 的请求计入套餐用量。权限分三档：默认相当于浏览器能做的事；应用权限可申请通知、全局快捷键等；完整电脑权限则可能运行程序、读写或删除文件，而且不必每次再问。完整权限只给你自己做的应用，或团队、企业里由本组织做的应用，且只覆盖当前版本，更新后会再问一次；若应用里有来自其他网站的部分，那部分更新时官方写了可能不会再问。Anthropic 不在安装前审查这些应用。HIPAA-ready 组织和混合部署不能用；Team 默认打开、完整权限关闭，Enterprise 默认关闭，要由所有者打开。部分类型的 artifact，包括 Claude Docs、Slides 和 Sheets，不能这样安装。对想把常用工作页钉到Dock 里的人来说，这比每次翻聊天记录方便，但完整权限应当只给自己信得过、而且清楚来源的应用。

同一天的另一篇署文是 [MCP 服务器现在可以把技能、任务等交给 Claude](https://claude.com/resources/articles/skills-over-mcp-tasks-and-more)。Skills over MCP 在 Claude 和 Claude Code 进入公开测试：服务器可以随工具一起发布技能，Claude 只在需要时加载，并随服务器更新，用户不必另行安装。它对 Pro、Max、Ultra 默认打开，Team 要管理员打开，Enterprise 还写着即将提供。Tasks 和 Elicitation 对 Pro、Max、Ultra 宣布正式可用，并向 Team、Enterprise 滚动；前者让服务器把耗时工作放到后台，后者可以在中途用表单或链接征求用户同意，例如在创建付费项目或删除仓库之前。File Uploads 还是即将推出。官方自称 MCP 的 SDK 每月有超过 **7 亿** 次下载，Claude 上的连接器超过 **10,000** 个，工具搜索可以在多服务器场景里把工具定义占用的上下文减少超过 **85%**，这些都是官方自己的数字。MCP 本身不是今天才发布的新标准，这篇写的是二周年节点上的能力扩展。

补录 11-23 夜间到 11-24 凌晨：Google 在 [Gemini API 里加入文件切片](https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/)。署文栏面是 **Nov 23, 2026**，RSS 时间 UTC **16:12**，大约北京 **00:12 · 11-24**。开发者可以把 PDF、Office、OpenDocument 以及音视频交给接口，只取需要的页、表、片段和图层，官方写只为模型实际检查的部分计费；现有的文件大小和页数限制仍然适用，并覆盖所有 Gemini 4 模型。对经常把整本季报塞进上下文的代理团队，这可能直接打到账单上，但省略切片参数时，文档和幻灯片默认仍会按保留版式的页面图来处理，不一定更便宜。

同一夜稍晚，Google Search 的署文 [让搜索更贴合你自己](https://blog.google/products-and-platforms/products/search/google-search-personal-intelligence-apps/) 栏面也是 **Nov 23, 2026**，RSS 为 UTC **17:00**，大约北京 **01:00 · 11-24**。它把 Google Wallet 和 Drive 加进 AI Mode 里的 Personal Intelligence，需要在搜索个性化设置里选择加入，并可以随时改。不要写成默认已经打开，更不要忽略它会用到消费记录和文档。

OpenAI 与 Cisco 的 [Shirudo](https://openai.com/index/introducing-shirudo) 署文栏面是 **November 23, 2026**，RSS 为 UTC **21:20**，大约北京 **05:20 · 11-24**。这是一个开源运行时，用 eBPF 在仍在运行的 Linux 系统上加载临时防护，官方写可以在补丁还没铺开时先挡住特定利用路径；受控测试里，用 Codex 生成的防护在不必重启的情况下，挡住了一次针对运行中 Elasticsearch 的 Java4Shell 尝试。运行时按 BSD 2-Clause 开源，BPF 程序是 BSD 与 GPL 双许可。官方给了虚拟机入门和实验环境，并预告 **12 月 15 日** 的技术讲解。它不是已经全面可用的产品，也不应理解成可以代替正式补丁。

豆包的个人助理「小豆」，官方产品页是 https://www.doubao.com/xiaodou/ 。页上把它写成会结合聊过的事和已连接的应用主动提醒，也可以在授权后使用抖音、飞书、日历、健康和地理位置等信息，连哪个、断哪个由你决定。11-24，[IT之家](https://www.ithome.com/1/031/329.htm) 和财新等媒体转述豆包官方宣布：邀请制公测，凭邀请码体验，并获赠一定量免费额度，相关能力以后会逐步出现在豆包 App 里。这些关于公测和额度的句子，今晚没有从产品页里核到原文，所以只写成媒体转述。想试的人应以官方入口和自己收到的邀请为准，也不要把「会主动办事」理解成已经可以在未授权的应用里任意操作。

OpenAI 的 [OpenWorks 项目页](https://openai.com/openworks/) 今晚可以打开，[申请说明](https://help.openai.com/en/articles/20001724-how-to-apply-to-openworks-and-follow-up-on-your-application) 也已写明规则：试点面向独立所有的美国小企业，含三个月 ChatGPT Business，对参与企业免费；软件和 SaaS、风险投资支持、以及私募股权所有的企业不在范围内。合作伙伴需每月至少拿出四天做实地协助，并办一场工作坊，津贴最高每月 **8,000** 美元，身份是承包商。帮助中心还写，项目邮箱尚未开放。OpenAI News RSS 到 UTC **11:34:54 · 11-25** 仍没有单独署文，所以这条不上头条，也不把某个发布日写成已经核对过的新闻栏面日期。若你不在美国这 20 个试点社区，官方也不保证会开到你所在的地方。

## 论文研究

### 6. 今天凌晨：DeepMind 推出 Humanity’s First Exam，测的是日常问题能不能反复做对

Google DeepMind 的 [Humanity’s First Exam](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/) 署文栏面是 **Nov 24, 2026**，RSS 时间为 UTC **19:30**，大约北京 **03:30 · 11-25**。作者是 Oran Kelly。官方写，现有前沿模型在复杂数学、编程和科学上已经很强，多数基准测的是能力上限；HFE 改测模型能不能把一件简单的事、以及它的轻微变体，每次都做对。数据集是 **544** 条初级的文本和图像提示，覆盖 **20** 项基础能力。署文提供了实时榜和技术报告入口，并邀请社区参加为期三周、到 **12 月 15 日** 截止的 Kaggle 竞赛，提交今天的模型仍会做错的日常问题。榜是主办方榜，不是独立实验室的排行，分数变动也还在进行中。

### 7. 11-24：OpenAI 放出矩阵乘法指数为 9/4 的预印本，蛋白质设计署文也在同一天

OpenAI 官方数学仓库在 **November 24, 2026** 这一栏下放出预印本 [The matrix multiplication exponent is nine fourths](https://github.com/openai/math/tree/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026)，PDF 在[这里](https://raw.githubusercontent.com/openai/math/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)。摘要称，平方矩阵乘法的指数在每个域上都是 **9/4**；上界已知，本文给出匹配的下界：对每个 n≥2，形式算术电路至少需要 **⌈n^{9/4}/2⌉** 个乘法或除法门，即便线性运算是免费的。这是官方仓库里的证明声称，不是已经完成独立同行评审的期刊论文；本轮也没有逐条核到完整的形式化验证覆盖范围，所以不写成「已经全部用 Lean 证明完毕」。今晚约 **20:11** 重新打开 HN [50637220](https://news.ycombinator.com/item?id=50637220) 时为 **716** 分、**395** 条讨论，是当时首页最高的一条，讨论热度不能代替评审。

同一天稍后，OpenAI 还发了 [GPT-6 模型展现出内在的蛋白质设计能力](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities)，RSS 时间为 UTC **13:00**，大约北京 **21:00 · 11-24**。官方写，GPT-6 家族可以只靠推理和通用代码工具设计蛋白质的结构和序列，而不调用专门的生物学生成模型；内部研究模型在多项任务上达到或超过专门模型，这是官方自评。与 Onava 的实验室测试里，基于 GPT-6.2 设计的蛋白质在五个靶点上显示出结合证据，经改造的抗体片段也保留了结合；专门模型帮助提供氨基酸序列并筛选要送去实验的候选。文中更细的数字是：针对五个靶点测试了 **322** 个小结合蛋白，其中 **35** 个、约 **10.9%** 呈结合阳性。这是研究与实验室结合证据，不是医疗器械批准，也不是已经可以按这句话去设计药物。生物安全风险，文中指向他们的预备框架。今晚约 **20:11**，HN [50634658](https://news.ycombinator.com/item?id=50634658) 为 **286** 分、**86** 条讨论。

同日稍早的另一篇是 [用 Astra 寻找遥远行星](https://openai.com/index/searching-for-distant-planets-with-astra)，RSS 为 UTC **11:00**，大约北京 **19:00 · 11-24**。两位业余天文学者分别用 Codex 和 Astra，在公开望远镜数据里做搜索，并把候选交给专业人员。开文就把结果写成「给了专业天文学家几个值得再看的位置」，后文也说明确认一颗行星可能要数月或数年。Bond 在约 **10 万** 颗 Kepler 星的数据里标出 200 多个信号，其中 10 个来自已知行星；两颗比较突出的是 KIC 5689121（亮度约每 **13.8** 天下降一次，若确是行星，直径大约是地球的 **2.4** 倍）和 KIC 6691030（约每 **4.8** 天一次）。SETI 研究所的 Vishal Gajjar 独立检索找到了这两个信号。Byrd 在约 **1900 万** 颗星的数据里初筛出 49 个候选，最强的一个已交给 TESS 团队，等待进一步分析。不要把这些候选写成已经确认的行星。

### 8. 补录 11-23：DeepMind 用 Gemini 4 代理团队改量子算法，并用 Lean 验证

Google DeepMind 的署文 [Finding faster quantum algorithms with agents and formal verification](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/) 栏面日期是 **November 23, 2026**，同样没有写进 11-23 的冻结笔记，精确时刻今晚也没有从 RSS 核到，故按补录来写。作者包括 Sergey Shirobokov、Ben Jaderberg 和 Ryan Babbush 等，与 Google Quantum AI 合作。官方写，他们让多支彼此独立的 Gemini 4 代理团队提出改进，每项结果都用 Lean 证明，并把 Lean 库、问题说明和已验证的解开源。

署文里的倍数都是官方自称，且明确写了：即便有这些改进，要在科学仿真里真正跑起来，所需资源仍可能高于第一批纠错量子计算机。分项数字是：与惯性约束聚变相关的一条电路，计算成本降为原来的约 **1/11.8**，纠错量子比特从 **5650** 降到 **4338**；一种常见光敏分子的模拟便宜约 **8** 倍；与药物代谢相关的细胞色素 P450，改进约 **2.5** 倍，量子比特从 **481** 降到 **333**；某一种 Grover 算法实现加快约 **2.57** 倍；arcsin 这一常用例程加快约 **290** 倍。不要把这些数字收成「最多大约快 10 倍」一句话，也不要把「用 Lean 验证了文中这些电路改进」理解成相关物理装置已经可以在现有硬件上运行。

## YC 动态

### 9. YC 核验：仍是晚交 W27，F26 Demo Day 在 12 月 2 日；无新 Launch 需要展开

今晚打开的[申请页](https://www.ycombinator.com/apply)仍写正在接受 Winter 2027 批次申请，批次时间为 **January to March**，地点在旧金山；准时截止日期 **November 2** 晚上 **8pm PT** 已过，但仍接受迟交。若在截止日期前递交，会在 **December 11** 前收到决定；截止日期之后提交仍会被考虑，但不能承诺具体回复时间。[Demo Day 页](https://www.ycombinator.com/demoday)仍写 “The F26 Demo Day will be held on Wednesday, December 2nd”，投资者入口仍指向 [demoday.ycombinator.com](https://demoday.ycombinator.com)。

今晚约 **20:11**（北京时间）重新打开 `launches.json` 时，按时间倒序栏顶是 Altair Health（Fall 2026，**4** 票，`created_at` UTC **16:00:00 · 11-24**）、Light Anchor（Fall 2026，**11** 票）、Dynamite（**4** 票）、Boat（Fall 2026，**8** 票）和 Vestris（Summer 2026，**16** 票）。这些都是本窗新出现或新靠近栏顶的条目，票数偏低，不单列为精选，也不写「现居顶」。已在 11-21 写过的 River（Fall 2026）现为 **25** 票，Morphy（Winter 2026，公司名栏为 MouseCat）为 **11** 票，Resin Technologies 为 **8** 票，STASIS 为 **8** 票，Oasive 为 **14** 票，FlashDrive 为 **30** 票，仍见栏内，不再展开。Launch HN: Versine（YC F26）在 HN [50634426](https://news.ycombinator.com/item?id=50634426) 今晚约 **20:11** 为 **90** 分，同样不按精选条目展开。

## 普通人今天就能做的 3 件事

1. **已经在用 Claude Team 或 Enterprise、并且代码在 GitHub 上的工程团队：** 若要试 Claude Ship，宜先选一个仓库，打开观察模式，并先给 Code Review 和 PR Steward 设置支出上限，再决定要不要把分支保护改成必须过自动批准。政策文件写的是「哪些变更可以不经过人」，不宜一上来就写得很宽。零数据保留、HIPAA 配置或客户托管密钥的组织，官方写了现在还不能用，不必在这些环境里反复重试。`/ship` 从 11-23 起在 Claude Code 和桌面应用滚动推出，以你这边实际看到的命令为准。积分领取若适用，截止日是 **2027 年 1 月 15 日**，须在领取后 **30** 天内用完，条款以官网为准。

2. **正在让外部代理读公司 Gmail、Drive 或日历的 Workspace 管理员和开发者：** 先对照[配置说明](https://workspace.google.com/blog/product-announcements/built-for-trust-and-control-new-ai-agent-protections-and-developer-tools-in-google-workspace)看现有连接是否走 MCP 服务器或 CLI，并在管理控制台里检查代理身份、确认规则和审计。技术强制从 **2027 年 2 月 1 日** 开始，用量配额从 **4 月 1 日** 开始计费，现在还有时间迁，但不宜把 REST 接口当成可以一直用下去的默认路径。发邮件、改共享、批量编辑前仍要人确认。用户自己撤销访问、以及把最敏感的邮件和文件夹对外部代理关掉，官方都还写着即将推出，不能当成今天已经能开的开关。若公司还在看 Claude 的数据驻留方案，Bedrock 上的可信访问接口已经正式可用，但企业前沿安全保障和企业数据控制仍是公开预览，要先看资格再决定加不加入。

3. **想在自己电脑或日常应用里让代理多帮一点忙的人：** 用 Claude 桌面端的，可以先把常用的 artifact 装成应用，但完整电脑权限只给自己做的、并且信得过的应用，更新后也要再看一次授权；HIPAA-ready 和混合部署不能用，Enterprise 默认是关的。用 Google 搜索的，若要打开 Personal Intelligence 对 Wallet 和 Drive 的连接，需在设置里选择加入，并随时可以关掉，不要以为这是默认发生的。想看豆包「小豆」的，先以[产品页](https://www.doubao.com/xiaodou/)和自己是否拿到邀请为准；邀请制公测和免费额度目前是媒体对官方宣布的转述，连接应用前也要看清授权范围。OpenWorks 只面向符合条件的美国小企业试点，不在名单里的不必按已经能申请成功来理解。本轮没有核验过新的跟练视频，也就不列教程。

