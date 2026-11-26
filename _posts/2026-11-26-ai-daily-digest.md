---
layout: post
title: "AI 每日精选 | 2026-11-26：给全网代理开放检索了，先看默认会公开什么、限额怎么算、是不是还在测试"
date: 2026-11-26 21:00:00 +0800
categories: [AI 新技术]
excerpt: "头条：11-25 夜间，Cloudflare 发布 Search for Agents，站点打开开关后会自动建索引，并在自己的域名上向代理暴露搜索接口；官方博文写面向所有客户、含有限额的免费档，但开发者文档仍写测试版，用量按 AI Search 计划和限额计，计费自 2026 年 12 月 1 日起。同一窗里，GitHub 宣布未做选择的 Copilot 代码审查账单将从 12 月 30 日起默认记到组织；AWS 则为语音代理和隔离沙箱给出仍在预览的能力。补录 DeepMind 面向质谱解析的 Mass Spec Skills。观点是给全网代理开放检索了，先看默认会公开什么、限额怎么算、是不是还在测试。"
---
![AI 每日精选封面 2026-11-26](/assets/2026-11-26-ai-daily-digest-cover.jpg)

> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 给全网代理开放检索了，先看默认会公开什么、限额怎么算、是不是还在测试

今天最显眼的，不是又多了一个模型名字，而是网站可以把检索接口直接开给外面的代理。11-25 夜间，Cloudflare 的[署文](https://blog.cloudflare.com/search-for-agents/)把 [Search for Agents](https://developers.cloudflare.com/ai-search/how-to/search-for-agents/) 写成当天起提供：在控制台或接口里打开开关，它会为这个站点创建 AI Search 实例、开始抓取和索引，并在你自己的域名上露出搜索接口；页面里会带上供代理发现的说明和地址，搜到的是 Markdown 内容，而不是再代你生成一段答案。官方博文写，所有客户都能开，也包括有限额的 Free 档；打开之后，互联网上的代理都可以来用，但仍要经过你这边的 bot 管理、AI Crawl Control 和 WAF。听起来像一键完成，可官方文档仍把这项能力写成所有套餐上的测试版，并且提醒：只应索引你打算公开检索的内容。用量跟 [AI Search 的定价和限额](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) 走，定价页写计费自 **2026 年 12 月 1 日** 起，每个账户每月有包含额度，超出按官方公布的美元单价计；Free 档每天最多爬 **500** 页，往往比「最多 10 万页」更先碰到。同一窗里，默认值也在别处要变：GitHub 的 changelog 写，若组织还没为 Copilot 代码审查选过账单归属，自 **2026 年 12 月 30 日** 起，有许可的成员所做审查将默认记到仓库所属组织。AWS 则放出了面向语音代理的 Transcribe Turbo 公开预览，以及用 Lambda durable functions 在 MicroVM 里跑代理生成代码的开发者预览，二者都还不能按已经能上生产来理解。给全网代理开放检索了，先看默认会公开什么、限额怎么算、是不是还在测试。

个人观点，不构成投资、采购或技术选型建议。数字和能力边界以各条原文为准。

## 今天最值得看的几件事

- **头条：站点可以对全网代理开放检索，但公开范围、限额和是否还在测试，要分开看。** 11-25 夜间，Cloudflare 让站点用一个开关完成建索引和接口暴露，博文写所有客户都能开，文档却仍写测试版。打开后，代理按设计就能发现并搜索你打算公开的内容，同时仍受 WAF 和爬虫控制约束。计费按 AI Search 的计划和限额，起始日是 **12 月 1 日**，不要写成已经无条件免费，也不要把 Free 档理解成没有日爬上限。
- **账单和预览要一起核。** GitHub 将把未做选择的 Copilot 代码审查，从 **12 月 30 日** 起默认记到组织；现在不选，不等于以后还按成员额度走。AWS 的 Lambda MicroVM 编排是开发者预览，官方写了不要用于生产。补录 11-25 白天的 Transcribe Turbo 也是公开预览，英语 batch 和流式、其他语言、以及 12 月底才到的轮次能力，状态并不一样。
- **研究侧是补录。** DeepMind 的质谱技能署文栏面是 11-25，RSS 则落在 11-24 晚上，昨天那篇精选漏收了。它可以在 Antigravity 里协助解析串联质谱，但官方自己也写了：新分子不能只靠它确认，部分异构体也分辨不了。10,000 个最高用量名额是有资格和名额限制的，不是自动开通。
- **本窗没有新的通用模型主发布。** OpenAI、Anthropic、Google、xAI、Cursor 的官方栏目里，今晚都没有核到需要单列的新旗舰模型。媒体和 HN 上关于 ChatGPT 合并 Chat / Work、加重用户更快触顶的说法，本轮没有在官方发布说明里对上，先不写进正文。
- **YC 核验：** 今晚约 **20:05** 重新打开 `launches.json` 时，按时间倒序栏顶是新出现但只有 **1** 票的 Nutmeg，后面是 Altair Health（**4** 票）、Light Anchor（**11** 票）、Boat（**8** 票）、Vestris（**17** 票）等，不单列展开，也不写「现居顶」。已在 11-21 写过的 River 现为 **26** 票，Morphy（公司名栏为 MouseCat）**11** 票，FlashDrive **31** 票，仍见栏内，不再展开。Winter 2027 申请仍在接受迟交，准时截止日期 **November 2** 晚上 **8pm PT** 已过；F26 Demo Day 仍为 **12 月 2 日**（周三）。

## 公开检索、限额和还在测试的那一层

### 1. 11-25 夜间：Cloudflare 给站点加了一键搜索接口，官方文档仍写着测试

Cloudflare 署文的 RSS 时间是 UTC **14:00 · 11-25**，大约北京 **22:00**，已经晚于昨天那篇精选的截稿。[介绍 Search for Agents](https://blog.cloudflare.com/search-for-agents/) 里，官方把它写成此前 AI Search 的下一步：过去要把自己的网站做成数据源，需要先手动建实例，再自己把搜索接口接到域名上，并设法让代理知道去哪里搜；现在这些被收到控制台「Quick Actions」里的一个开关，也可以用接口打开。

打开之后，Cloudflare 会按默认配置创建 AI Search 实例并开始爬取。代理要发现它，靠的是每页里自动加入的说明，例如搜索地址会指向站点自己域名下的 `/.well-known/search`。如果同时也开了 Markdown for Agents，代理用 Markdown 方式要页面时，同样的信息会出现在文首。官方特意写了：这个接口返回的是检索到的内容，用 Markdown 给出，而不是再让另一个模型替站点回答。它还支持较新的 HTTP QUERY 方法。这些接口仍然受你这边的 bot 管理、AI Crawl Control 和 WAF 影响，不是打开开关就把门禁全部撤掉。

需要留心的是两处并不完全相同的官方表述。博文写「Starting today」，面向所有客户，也包括有限额的 Free 档；[开发者文档](https://developers.cloudflare.com/ai-search/how-to/search-for-agents/)则写，Search for Agents 在所有套餐上是 **beta**，并且只应索引你打算公开检索的内容。用量以 [AI Search 定价页](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) 为准：官方写计费自 **2026 年 12 月 1 日** 起；每个账户每月包含 **500 万** 个摄入 token、**10 GB-month** 存储、**1,000** 次语义查询和 **1,000** 次全文查询。超出后的官方美元价是：基础摄入每百万 token **0.75** 美元，图像处理再加每百万 token **0.50** 美元，存储每 GB-month **2.00** 美元，语义 / 向量 / 混合查询每 1,000 次 **0.75** 美元，全文查询每 1,000 次 **0.10** 美元。Workers Free 每账户最多 **100** 个实例，而且网站 discover 爬取每天最多 **500** 页，文档写这常常是真正先碰到的上限；Workers Paid 默认最多 **5,000** 个实例，再多出的每个每月 **0.10** 美元。这些是官方美元标价，不要自行折成人民币，也不要把「12 月 1 日起计费」理解成在此之前完全没有限额。

对已经把文档站、产品说明或帮助中心放在 Cloudflare 上的团队来说，这可能减少一层自建检索。但也正因为接口会写进每一页、默认面向能够发现它的代理，打开之前更宜先想清楚：哪些目录本来就不该被公开搜到，以及现有的爬虫和 WAF 规则会不会把合法查询一并拦住。

## 中段简报

11-25 夜间到 11-26 凌晨，GitHub 在 [changelog](https://github.blog/changelog/2026-11-25-copilot-code-review-billing-will-default-to-the-organization) 里写了一件还没生效、但必须先做选择的事。适用范围是拥有 Copilot Business 或 Copilot Enterprise 的组织和企业。若还没有为「已有 Copilot 许可的成员」选择代码审查怎么计费，那么自 **2026 年 12 月 30 日** 起，这些审查将记到仓库所属组织的账单；想维持现在的算法，要在那之前改成 Member。今天在没有保存选择时，这类审查仍走成员自己的 Copilot 额度。已经选过 Member 或 Organization 的，选择继续有效。没有启用 AI Credits 按量付费、有账单锁，或没有可计费客户的账户，会被设成 Member。没有 Copilot 许可的成员，原来那一项单独设置不变。官方还写，组织计费需要打开 AI Credits 按量付费，并且可能增加组织支出；若设置由企业统一管理，由企业所有者来选。对工程负责人来说，这更像一封到期提醒，而不是今天已经改账。

同一窗里，AWS 宣布 [用 Lambda durable functions 编排 MicroVM](https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-microvm/)。栏面日期是 **Nov 25, 2026**，RSS 大约是北京 **04:00 · 11-26**。官方把它写成开发者预览：可以在隔离的 MicroVM 里跑不受信任、或由代理生成的代码，例如软件工厂、安全扫描，或编排 CI/CD。任务可以单次执行，也可以开一个会话，让后续步骤共用文件和内存；durable function 负责生命周期、检查点和重试，一个函数还可以并行管多台 MicroVM。目前扩展加在 TypeScript 和 Python 的 Durable Execution SDK 上，并且只在同时支持 durable functions 与 Lambda MicroVMs 的区域提供。官方写得很直白：预览功能可能变更，不要用于生产负载。

补录 11-25 白天：AWS 的 [Transcribe Turbo](https://aws.amazon.com/about-aws/whats-new/2026/11/transcribe-turbo-preview/) 进入公开预览，栏面是 **Nov 25, 2026**，RSS 大约北京 **16:00**，早于昨天精选截稿，当时没有写入，这里补上。公开预览落在 US East (Ohio)，覆盖批量和流式。官方自称，流式目前支持英语、葡萄牙语、法语、意大利语、德语和西班牙语，英语词错误率相对当前生产模型下降约 **14%**，其余语言约 **11%**，格式准确率提高超过 **20** 个百分点；批量里，英语 Turbo 已在大多数 AWS 区域正式可用，上述其他语言以及中文、日语、韩语、阿拉伯语则是预览，自称词错误率约低 **16%**。这些都是官方自评。基础模型不必改 API、代码或 SDK。为语音代理准备的两项能力——按语义和韵律判断对方是否说完，以及在每一轮给出运行时提示——上线时先支持英语，其余语言官方写到 **2026 年 12 月底**；官方还自称前者大约 **615 毫秒** 响应、打断率 **5%**，后者在英语客服数据上把菜单路由准确率从 **87%** 提到 **97%**。这两项官方写不再另收费。不要把整项 Turbo 理解成已经全面正式可用，也不要把「两项能力不另收费」写成整个服务免费。

## 论文研究

### 2. 补录 11-24 夜间至 11-25：DeepMind 给 Antigravity 加上质谱解析技能，确认结构仍要人来看

DeepMind 署文[用 Mass Spec Skills 从谱图走到结构](https://deepmind.google/blog/interpreting-mass-spectra-with-google-antigravity/) 的栏面日期是 **November 25, 2026**，但 RSS 的发布时间是 UTC **13:07 · 11-24**，大约北京 **21:07 · 11-24**。昨天那篇精选当晚没能解析 DeepMind 的 RSS，只核到了量子算法那一篇，所以这篇按补录来写，并把栏面和 RSS 两处时间都留在这里。

官方写的是一套给 Google Antigravity 用的领域技能，用来解释串联质谱、整理证据，并把每一步接到已有的开源工具和公共化合物库上。它针对的是一个很具体的瓶颈：一次检测可以冒出上万个分子信号，可光谱库平均只能给大约 **5%** 的谱图找到参考，人体样本大约 **10%**——这组比例是署文里转述的既有局面，不是今天新测的独立榜。模型本身算不准碎片质量，也不适合在数百万条化合物里逐条比对，所以官方把它写成「推理加上工具」，而不是单靠模型直接给出结构。署文也把做不到的地方写清楚了：镜像分子和部分近缘异构体，只靠 LC-MS/MS 分不开；真正还没进数据库的新分子，它不能独自确认，最多给出式量、峰归属和一份可供化学家接着做的注释表。文中「即使轻量模型也能达到前沿检索准确率」是官方自称；合作者引言里「大多数评估中超过 90%」，以及文内示例里 **97.7%** 的碎片强度被解释，都只是自称或举例，不能当成已经过同行评审的通例。

官方写，今天就可以下载 Antigravity 并安装 Mass Spec 插件；企业用户可选择 Use Business Account，再用 Google Cloud 凭证登录。另外还提供 **10,000** 个科学家名额，可在最高用量档免费使用 **6** 个月，滚动开通，但要看资格、容量和遴选，并不是申请了就一定有。署文上的申请入口是 [这张表](http://forms.gle/WvmBbPvRbpKG1BPn9)，科学场景说明在 [Antigravity 的科学用例页](https://antigravity.google/use-cases/science)。对做天然产物、代谢组或环境分析的实验室，这可能把重复的查库和峰归属往前推一步，最后拍板的仍应是人。

## YC 动态

### 3. YC 核验：仍是晚交 W27，F26 Demo Day 在 12 月 2 日；无新 Launch 需要展开

[申请页](https://www.ycombinator.com/apply)今晚仍写正在接受 Winter 2027 批次申请，准时截止日期 **November 2** 晚上 **8pm PT** 已过，但仍接受迟交。若在截止日期前递交，会在 **December 11** 前收到决定；截止日期之后提交仍会被考虑，但不能承诺具体回复时间。[Demo Day 页](https://www.ycombinator.com/demoday)仍写 “The F26 Demo Day will be held on Wednesday, December 2nd”。今晚约 **20:05** 重新打开 `launches.json` 时，按时间倒序栏顶是新出现的 Nutmeg（Logical，Fall 2025，北京时间 **01:33 · 11-26** 左右入库），但只有 **1** 票；其后是 Altair Health **4** 票、Light Anchor **11** 票、Boat **8** 票、Vestris **17** 票等。这些票数都不高，不单列为精选，也不写「现居顶」。已在 11-21 写过的 River 现为 **26** 票，Morphy（Winter 2026，公司名栏为 MouseCat）为 **11** 票，FlashDrive 为 **31** 票，仍见栏内，不再展开。

## 普通人今天就能做的 3 件事

1. **自己的站点已经接在 Cloudflare 上、又打算让外面的代理来搜文档或产品说明的人：** 先读[文档](https://developers.cloudflare.com/ai-search/how-to/search-for-agents/)和[定价页](https://developers.cloudflare.com/ai-search/platform/limits-pricing/)，再决定开不开这个开关。它仍是测试版；打开后，接口会写进页面，默认面向能够发现它的代理。只应索引你打算公开检索的内容，并先检查 AI Crawl Control 和 WAF 会不会把查询放行或误拦。计费按官方定价从 **2026 年 12 月 1 日** 起算，Free 档每天最多爬 **500** 页，不要按「没有上限的免费检索」来规划。

2. **正在用 Copilot Business 或 Copilot Enterprise、而且还没为代码审查选过账单归属的组织管理员：** 对照[这则 changelog](https://github.blog/changelog/2026-11-25-copilot-code-review-billing-will-default-to-the-organization)，看现在的选择是 Default、Member 还是 Organization。若希望 **12 月 30 日** 之后仍记在成员额度上，要在此之前明确选 Member；什么都不选，默认就会改到组织。组织计费还需要打开 AI Credits 按量付费，并可能推高账单。若设置由企业统一管理，这件事要找 enterprise owner，不是每个仓库管理员都能改。

3. **在做语音代理，或想在隔离环境里跑代理生成代码的人：** Transcribe Turbo 的公开预览目前以 US East (Ohio) 为主，英语批量和流式、其他语言、以及要到 12 月底的轮次能力，范围并不相同；文中「不另收费」只覆盖那两项流式新能力。Lambda 的 MicroVM 编排是开发者预览，官方写了不要用于生产。做质谱或小分子鉴定的人，可以先看 DeepMind 的[署文](https://deepmind.google/blog/interpreting-mass-spectra-with-google-antigravity/)和[科学用例页](https://antigravity.google/use-cases/science)，在 Antigravity 里安装插件试用；**10,000** 个最高档免费名额要申请，也要过资格和名额，不能当成已经自动开通。本轮没有核验过新的跟练视频，也就不列教程。

