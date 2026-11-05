---
layout: post
title: "AI 每日精选 | 2026-11-05：写码抢壳；壳、闸、邻居"
date: 2026-11-05 21:00:00 +0800
categories: [AI 新技术]
excerpt: "头条：OpenAI×Pierre、Meta×Conductor、Factory×HumanLayer，外加 ChatGPT×Codex 共享用量与 Claude Code 约 99% 降本。观点谈写码 Agent 的三道账：谁抢到壳、谁过得了闸、算力能不能过邻居。另有 Images 2.6、Ripple / Kimi / SWE-2 Flash、数据中心选票与 Community Compact、Uber Agent 冷数据。"
---
![AI 每日精选封面 2026-11-05](/assets/2026-11-05-ai-daily-digest-cover.jpg)


> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 今天最值得看的几件事

- **头条：写码 Agent 控制面兼并潮**——OpenAI 拟购 **Pierre**、Meta 收 **Conductor**、Factory 收 **HumanLayer**；旁证 Cat Wu / Austin Lau 赴 OpenAI；同日 ChatGPT×Codex **12** 月共享用量、Claude Code 状态栏约 **99%** 降本、Apple 员工日额度下调。
- OpenAI **Images 2.6**：可调速、可逐帧编辑的 GIF；官方称周生图约 **40** 亿张。
- 开源/可部署写码基座：Ricursive **Ripple-65B Preview**、Moonshot **Kimi K3.1 Pro**（+昇腾/vLLM/SGLang Day-0）、Cognition **SWE-2 Flash**；旁证百度 **ERNIE 5.5 Flash Base**、ByteDance **Axion 1.0**。
- 美中期选举数据中心选票几乎全线受限 + OpenAI **National Community Compact**；旁证 TeraWulf×Google 为 Anthropic 肯塔基租约信用背书。
- 安全边界：OpenAI「**948** LPE」管道、Xen **XSA-523**（Claude 发现）、CERT-In **CRAFTY FALCON**、Arcjet **Himalia**。
- Uber：最忙一周约 **4** 单网约车 / 约 **500** 单 Eats 经第三方 Agent。
- 企业 Agent 控制面：Snowflake Expedition、Adobe CX Enterprise Coworker、Kimi Hosted Agents、Anthropic **commerce-agents**。
- 硬评测：SemiAnalysis **GDPx** 顶分约 **12%**、**LoLBench** resolved 约 **14%**；旁证 RoboColosseum 上 Unitree G1 零完成。
- YC：W27 逾期仍审，F26 Demo Day **12-02**。
- 观点：**壳、闸、邻居**——写码 Agent 与算力的三道账。

## 最佳实践

### 1. 写码 Agent 抢壳：Pierre / Conductor / HumanLayer + 共享用量与降本（头条）

同一窗里，三家在收「写码 Agent 外面那层壳」。OpenAI 官方署 **November 4, 2026** 宣布拟收购 **Pierre Computer Company**：Code Storage + 开源 Trees / Diffs（Codex 应用内浏览与 diff 已用其库），目标把面向 Agent 并行写码的 Git 工作流做进 Codex，并对照本周自研 Git 后端 **Pando**；交割须监管等惯常条件，金额未披，开源项目拟保持开源。Meta 收购 **Conductor**（多 Agent 并行工作区，Agent 来自 Anthropic/OpenAI 等，非自研基座）——Axios 首报、公司写「joining Meta」，TechCrunch 约 **1:10 PM PST · 11-04**（≈ 北京 **05:10 · 11-05**）确认；自 **11-04** 停新注册，Cloud **11-13** 只读、**11-20** 关停并删云数据，本地版继续修到约 **2027** 初。Factory 同日宣布 **HumanLayer** 加入：将开源，现平台过渡期至少保持可用，未来数周拟把多人协作与规格/设计文档能力带进 Factory。旁证人事：Claude Code 产品负责人 Cat Wu（`@_catwu`）约北京 **08:25 · 11-05** 宣布加入 OpenAI 领导 Core Products 产品管理；Anthropic 增长营销骨干 Austin Lau 同窗称 recently joined OpenAI。

计量闸几乎叠在同一天。OpenAI Help Center 确认自 **12** 月起 Plus / Pro / Business 的 ChatGPT 与 Codex 用量合并为同一 token 额度，**Instant chat 不计入**；未公布各档具体 token 数。Claude Code **v2.1.316**：后台子 Agent 状态栏改由 Haiku **5.5** 读短笔记生成，自称每次更新约少耗 **99%** token（有后台子 Agent 的会话约少耗额度约 **5%**）；**v2.1.317** 微调游戏复刻提示词，**v2.1.318** 修权限键误触等。Bloomberg 称 Apple 自 **10** 月起部分工程师日上限由约 **$300→$200**，并拟再压至约 **$100**；工程外不少团队本就约 **$100**/日。

来源：[OpenAI·acquire Pierre](https://openai.com/index/openai-to-acquire-pierre/)、[Conductor·joining Meta](https://www.conductor.build/announcement)、[TechCrunch·Meta×Conductor](https://techcrunch.com/2026/11/04/meta-acquires-ai-coding-startup-conductor/)、[Factory·HumanLayer](https://factory.com/news/humanlayer)、[OpenAI Help·ChatGPT and Codex usage](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits)、[Claude Code changelog](https://code.claude.com/docs/en/changelog)、[X·@ClaudeDevs](https://x.com/ClaudeDevs/status/2118063143167693011)、[Bloomberg·Apple AI budgets](https://www.bloomberg.com/news/articles/2026-11-04/apple-cuts-internal-ai-usage-budgets-in-move-to-reduce-spending)、[X·@_catwu](https://x.com/_catwu/status/2118137612577968402)、[Business Insider·Cat Wu](https://www.businessinsider.com/cat-wu-joins-openai-from-anthropic-product-lead-coup-2026-11)

谁抢到「壳」，谁就更接近写码工作流的默认入口；谁过不了「闸」，演示再炫也会在账单上熄火。受益的是 Git/diff 审阅基建、企业写码 Agent 控制面、用量观测与降本工具；付钱的是把「宣布拟收购」写成「已交割取代 GitHub」、或把约 **99%** 写成「全体 Claude 订阅已全面降价」的人。标「拟收购 ≠ 已交割；金额多未披；Cloud 关停时间表 ≠ 本地版已停；Help Center 政策预告 ≠ 今日切表；约 **99%**/**5%** 为公司估计 ≠ 第三方审计；Bloomberg 匿名信源 ≠ Apple 官方稿；本人 X 帖 ≠ OpenAI News 室人事稿」。

- 工程负责人：选型时问清「Agent 的 diff/分支/审阅落在谁的产品里」，别只比模型榜。
- 重度 Codex / Claude Code 用户：先查 Settings → Usage 与 `claude --version`（须 **≥2.1.316**），把 **12** 月共享额度写进团队预算。
- 创业者：壳被收并不等于需求消失——做「可迁出的审计、策略、协作层」比再做一个聊天壳更贴今天的并购逻辑。

教程：以 [OpenAI Pierre 公告](https://openai.com/index/openai-to-acquire-pierre/)、[Claude Code changelog](https://code.claude.com/docs/en/changelog) 与 [Help Center 用量说明](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits) 为准。降本操作可参考公开文 [Claude Code Background Subagents: Haiku 5.5 Status Line](https://aicodewith.ai/en/blog/claude-code-background-subagent-status-haiku-usage)（跟版本升级，非 Anthropic 官方片）。本条未核到针对 Pierre/Conductor 交割后产品的成熟 Bilibili/YouTube 操作片。

## 模型发布

### 2. OpenAI Images 2.6：可编辑动图进 ChatGPT

官方署 **November 4, 2026**（`@OpenAI` 约北京 **07:35 · 11-05**）：宣称生图约 **50%** 更快；原生支持把提示词或上传图做成可调速、可逐帧编辑的动画 GIF；参考图可保存复用；ChatGPT / Codex 全订阅档全球桌面/移动/网页可用。API 侧推出 GPT‑Image‑2.6 **Flare**（quality=low 自称最快约 **6** 秒）与 **Sunburst**（medium/high 偏细节与跨次一致性）；新增 image markup、SVG 导出与 complexity / quality 控制。官方称 ChatGPT/Codex/API 合计每周生图约 **40** 亿张。配套 System Card 写 GIF 运动相关风险（靶向违例集召回约 **77.66%**——勿写成生产违例率）。

来源：[OpenAI·Introducing Images 2.6](https://openai.com/index/introducing-images-2-6/)、[The Verge·ChatGPT GIFs](https://www.theverge.com/ai-artificial-intelligence/1026474/openai-chatgpt-animated-gifs-images-2-6)、[System Card·GIF risks](https://deploymentsafety.openai.com/chatgpt-images-2-6/gif-risks-safeguards-and-evaluations)

可编辑视觉今天进了默认聊天入口——和写码壳是同一天的「入口战」。受益的是营销素材、产品动效草稿、需要短循环的社媒团队；付钱的是把周生图量写成「第三方审计」、或把 GIF 写成「已替代全部视频生成」的人。标「全球可用 ≠ 各账号已同步放量；公司周量 ≠ 审计；Flare **6** 秒为 low quality；GIF 安全召回 ≠ 生产零漏检」。

- 运营 / 设计：先用一张品牌静帧试「无缝循环 + 保留人脸/包装细节」提示词，再谈批量。
- 独立开发者：API 的 markup / SVG / complexity 比「再套一层聊天壳」更适合做垂直插件。
- 风控：动图审核规则与静图不同，合同里单独写 GIF 风险条款。

教程：以 [官方页](https://openai.com/index/introducing-images-2-6/) 为准；公开图文跟练可参考 [digit.in·How to turn images into animated GIFs](https://www.digit.in/how-to/general/how-to-turn-your-images-into-animated-gifs-using-chatgpt-images-2-6.html)（第三方 how-to，非 OpenAI 官方片）。本条未核到一手官方 YouTube 专片。

### 3. Ripple-65B、Kimi K3.1 Pro、SWE-2 Flash：可部署写码基座一日三连

**Ricursive Ripple-65B Preview**：从零预训练约 **12T** token、上下文至约 **1M** 的稠密 **65B**（非 MoE）；自称 TerminalBench **2.1** 约 **80.52**，全链路研发成本约 **$32M**（自称约为前开源 agentic coding SOTA 约 **1/10**）；已上 HF / Together / GMI / OpenRouter。**Moonshot Kimi K3.1 Pro** 权重落 HF：约 **2.8T** MoE / 激活约 **104B**、约 **1M** 上下文、原生多模态；自称 Terminal-Bench **4.0** 约 **65.7**、DeepSWE v1.1 约 **75.5** 等；许可为 **Kimi K3.1 Pro License**（非纯 Apache）。同日 **vLLM** / **SGLang** Day-0，华为昇腾据 IT之家约 **11-05 08:45** 同步 0 Day（Atlas **800** A3 / **900** A3 SuperPod / 昇腾 **950** 等）。**Cognition SWE-2 Flash**：基于 Inkling-Small（约 **276B** / 激活约 **12B**）再 RL；Terminal-Bench **4.0** 自称约 **0.9→20.0**；相对 SWE-2 约 **1/5** 价、约 **3×** 速（回放仿真口径），付费档免费用至约 **11-30**；权重暂不公开。旁证：百度开源 **ERNIE 5.5 Flash Base**（约 **280B** / 激活约 **14B**，约 **33.5T** token 预训练基座）；ByteDance 等 **Axion 1.0** 开源 Agent 基座（轻量 SFT+RL，**35B** reproduction 上 HF）。

来源：[Ricursive·Ripple](https://www.ricursive.com/ripple)、[HF·Ripple-65B-Preview](https://huggingface.co/ricursiveAI/Ripple-65B-Preview)、[HF·Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)、[vLLM·Day-0 Kimi](https://vllm.ai/blog/2026-11-04-kimi-k31-pro)、[SGLang·Day-0](https://www.sglang.io/blog/kimi-k3.1-pro-day0-support)、[IT之家·昇腾 0 Day](https://www.ithome.com/1/022/502.htm)、[Cognition·SWE-2 Flash](https://cognition.com/blog/swe-2-flash)、[ERNIE Blog·5.5 Flash Base](https://ernie.baidu.com/release/ernie-5-5-flash-base/)、[Axion 1.0](https://axion1-0.github.io/)

壳在被大厂收，底座却在开源侧加速——一条卖「可本地部署的写码脑」，一条卖「更便宜的日常工程 Agent」。受益的是私有化推理、昇腾/异构纳管、Devin 类中端档采购；付钱的是把公司自报表写成「已定美国/中国开源第一」、或把 HF 可下写成「已等同 Apache 无限商用」的人。标「TerminalBench 等为公司自报 ≠ 第三方盲测；**$32M**/约 **1/10** 为自家成本口径；Kimi 许可 ≠ Apache；Day-0 ≠ 已证生产 SLA；SWE-2 Flash 无公开权重；ERNIE Base ≠ 已对齐对话产品；Axion **35B** reproduction ≠ 已开源 **122B**」。

- 平台工程：先按 [vLLM recipe](https://recipes.vllm.ai/moonshotai/Kimi-K3.1-Pro) 在隔离集群跑通，再谈替换 Claude/GPT 写码。
- 采购：把「许可文本 + 硬件适配范围 + 是否可自托管权重」拆进三行，别只听榜分。
- 日常工程团队：SWE-2 Flash 免费窗到约 **11-30**，适合先压评审/文档类任务，别一上来绑关键路径。

教程：Kimi 部署以 [vLLM Day-0 博文](https://vllm.ai/blog/2026-11-04-kimi-k31-pro) 与 [recipes 页](https://recipes.vllm.ai/moonshotai/Kimi-K3.1-Pro) 为准；Ripple / SWE-2 Flash / ERNIE 以各自官方页与 HF 卡为准。本条未核到针对 Ripple-65B 或 SWE-2 Flash 的成熟中文实操片。

## 工具与产品

### 4. 企业 Agent 控制面：Snowflake、Adobe、Kimi Hosted、commerce-agents

**Snowflake** 在 Expedition 2026（署 **Nov. 3**）推 Business Ontology + Cortex AI Gateway（鉴权、费用硬限、Abuse Detection、Sandboxes 等，能力分档 GA/preview），并升级 **CoCo**（约 **9,100** 账户周活）/ **CoWork**（约 **5,800**），预告常驻 Bots。**Adobe** 署 **November 4** 宣布 CX Enterprise Coworker 可在 ChatGPT / Claude / Gemini for business / Copilot 等内使用（Databricks Genie 已列；Amazon Quick / IBM / Snowflake 称将跟进），绑 MCP 与 A2A。**Moonshot** 正式上线 **Kimi Hosted Agents**（Harness as a Service）：约 **140+** Skills、约 **30+** 插件，沙箱标价自称约 **¥0.072**/小时；首批官方模板约 **12** 个（二级稿多写「**8** 个金融」——以 docs 为准）。**Anthropic** 开源 **commerce-agents** 蓝图：购物 Agent + 商家 Agent 参考实现（目录/购物车/结账交接；商家改价须人工批准），伙伴引用含 Shopify、Visa、Mastercard 等；自称零售侧购物车可大约 **35%**、完成购买意愿大约 **60%** 更高（公司客户口径）。

来源：[Snowflake·Ontology & Gateway](https://www.snowflake.com/en/news/press-releases/expedition-2026-business-ontology-ai-gateway/)、[Snowflake·CoCo and CoWork](https://www.snowflake.com/en/news/press-releases/expedition-2026-coco-cowork/)、[Adobe Newsroom·CX Coworker](https://news.adobe.com/news/2026/11/adobe-integrates-agentic-cx-enterprise-coworker-into-ai-platforms)、[Kimi·托管智能体概览](https://platform.kimi.com/docs/hosted-agents/overview)、[Claude·commerce agents](https://claude.com/resources/articles/claude-for-commerce-agents)、[GitHub·anthropics/commerce-agents](https://github.com/anthropics/commerce-agents)

写码壳在被收，企业侧则在卖「可上生产的控制面」——策略门、工作台嵌入、托管 harness、交易蓝图四条路并行。受益的是数据平台治理、营销 CX 集成商、金融投研模板集成、电商结账交接中间件；付钱的是把会场新闻稿写成「全部租户已 GA」、或把约 **35%** 购物车增益写成「已无人值守改价上架」的人。标「GA/preview/private 分档须对照；账户周活为公司口径；平台可用 ≠ 管理员已默认开通；约 **¥0.072**/小时 ≠ 全成本；蓝图可 fork ≠ 任意目录即生产可用；Managed Agents 为 beta」。

- 数据 / BI 负责人：先问 Cortex Gateway 是否盖住「模 + 工具 + MCP」三道调用，再听 CoWork demo。
- 营销技术：Coworker 进 ChatGPT/Claude 只是分发——真正卡点仍是受众权限与投放人工确认。
- 电商 / 客服产品：fork commerce-agents 时把「结账仍交商户既有流程」写进验收，别承诺 Agent 直接扣款。

教程：以各家官方文档为准；本条未核到针对 Snowflake Expedition 2026 或 Kimi Hosted Agents 的成熟 Bilibili/YouTube 专片。同类可搜「Cortex AI Gateway」「Claude Agent SDK commerce」公开分享作流程参考。

### 5. Uber Agent 冷数据：一周约 4 单车 / 约 500 单 Eats

TechCrunch 约 **1:56 PM PST · 11-04**（≈ 北京 **05:56 · 11-05**）据 Uber Q3 会：十月最忙一周（万圣节周）约 **3.2** 亿次行程+外卖中，经第三方 AI Agent 下单的网约车仅约 **4** 单、Uber Eats 约 **500** 单；管理层称「非常早期」。对照 App 内约 **50** 秒叫车 / 约 **90** 秒再点常用餐。DoorDash 上周「仅数百」Agent 单叙事（Ars 约 **10** 月）同窗再热。

来源：[TechCrunch·Uber AI agents](https://techcrunch.com/2026/11/04/almost-no-one-uses-ai-agents-to-book-their-uber-company-says/)、[The Verge](https://www.theverge.com/transportation/1026306/uber-ai-agents-q3-earnings-disintermediation)、[Ars·DoorDash agents](https://arstechnica.com/ai/2026/10/doordash-says-outside-ai-agents-have-only-led-to-hundreds-of-orders-so-far/)

蓝图可以很满，交易闭环的冷数据很刺眼——和 commerce-agents、灵光类连接器是同一张图的另一面。受益的是深嵌 App 内的助手、能证明「比原生更快」的垂直 Agent；付钱的是把「单周抽样」写成「Agent 经济已失败」、或把管理层展望写成「已给出上线日」的人。标「单周 ≠ 全年；仅统计下到 Uber 的单 ≠ 意图调用失败数；展望 ≠ 时间表」。

- 消费级 Agent 产品：KPI 先对齐「比原生 App 少几秒/少几步」，再讲多 Agent 编排。
- 投资者观察：把 Uber/DoorDash 冷数据与「购物车 +35%」客户口径并排放，别只听一边。
- 创业者：交易闭环的钱更可能在「企业午餐/差旅合规」窄场景，而不是全民代叫车。

教程：本条无操作教程；跟踪以财报会实录与后续 IR 为准。

## 最佳实践（续）

### 6. 安全边界：948 LPE、Xen XSA-523、CRAFTY FALCON、Arcjet Himalia

OpenAI 署 **November 4** 公开「A thousand fewer paths to root」：中 **10** 月一次运行对常见 Linux 桌面配置动态复现约 **1,724** 个漏洞，产出约 **291** 信息泄露 PoC 与约 **948** 个可获 root 的独立 LPE，并生成候选补丁；全流程 API 费用约 **$1,213,430**（约 **$1,279**/独立 LPE）；人类审阅后报送维护者。Xen **XSA-523**（公开约 **2026-11-03**）：grant copy 批处理缓存校验不完整，恶意 guest 可对同主机其他域（含 Dom0）任意读写；发现归功于 Anthropic 用 Claude，经 Ada Logics 验证；官方称无已知缓解，须打补丁并重启。印度 CERT-In 标示 **CRAFTY FALCON**：称对 BFSI 的 AI 驱动攻击 ongoing，列公开进攻向工具（ARTEX / PentAGI 等），经测试环境横向进生产、₹1 试转再放大额。Arcjet 署 **November 5** 发 **Himalia 1** 提示注入分类器（对启用该检测的 SDK 调用上线），另 **Thebe 1** / **Carme 1** 进 early access。

来源：[OpenAI·thousand fewer paths](https://openai.com/index/a-thousand-fewer-paths-to-root)、[Xen·XSA-523](https://xenbits.xenproject.org/xsa/advisory-523.html)、[Indian Express·Crafty Falcon](https://indianexpress.com/article/technology/tech-news-technology/cert-in-crafty-falcon-ai-driven-hacking-campaign-fintech-10951672/)、[Arcjet·custom AI security models](https://arcjet.com/blog/introducing-arcjets-custom-ai-security-models)

模既能挖洞也能当闸——和写码 Agent 放权是同一天的「边界账」。受益的是补丁编排、纵深隔离（Firecracker/gVisor 叙事）、金融 API 签名与测试/生产隔离、Agent 注入专用分类器；付钱的是把受控研究管道写成「已对公网无人值守利用」、或把顾问署文写成「已公开全部受害名单」的人。标「人类审阅报送 ≠ 已无人值守利用；**948** 为去重补丁口径；XSA 无缓解 ≠ 云租户已全面失守；顾问 ≠ 完整损失披露；Himalia 自测集 ≠ 生产零漏报」。

- 平台安全：把「低权限 + 未打满补丁 ≈ 功能上 root」写进基线，优先隔离与补丁 SLA。
- 金融 / 支付：测试与生产断网、服务端校验 + nonce，别只信「正版 App 可调」。
- Agent 产品：注入检测按场景分模（客服 vs 写码 vs 修洞），别共用一个 frontier 护栏口号。

教程：以各顾问/官方博文为准；本条无「如何利用」教程，也不应跟练攻击步骤。补丁与隔离同类可搜公开「Xen security advisory patch」「Linux LPE patch management」运维分享作防御参考。

## 产业与资本

### 7. 数据中心选票几乎全线受限 + OpenAI Community Compact

CNBC 约 **1:56 PM EST · 11-04** 汇总：Ballotpedia 口径约 **10** 州、约 **41** 项数据中心相关措施；除北达科他州 Harwood 一项外，已出结果的措施均偏向限制或否决亲建设提案；俄亥俄一州即约 **21** 项。反数据中心叙事进入全州选情（俄亥俄参议员、德州州长等）。CNBC 选民调查约 **56%** 称数据中心为其关键或重大投票因素。404 Media 另记约 **40+** 场、约 **13** 州等口径（与 CNBC 州数不完全一致）。OpenAI 署 **November 5** 发 **National Community Compact** + Compute Campus Policy Blueprint：自付电费与配套基建全成本、重大开支前财务担保、水与噪声研究、不对公职人员签宽 NDA、本地岗位与学徒等；蓝图吁大电用户自担增量电网成本、高峰可削减负荷（例 Effingham 与 Georgia Power 协议高峰可减供至约 **1000 MW**）。旁证：TeraWulf 披露 Google 为 Anthropic 在肯塔基约 **401 MW**、约 **20** 年租约（公司口径合约承诺约 **$19B**）签信用支持协议——背书 ≠ Google 直接投资 **$19B**。

来源：[CNBC·data center ballot](https://www.cnbc.com/2026/11/04/data-center-ballot-measures-2026-midterm.html)、[404 Media](https://www.404media.co/american-voters-overwhelmingly-reject-ai-data-centers/)、[OpenAI·responsible AI infrastructure](https://openai.com/index/setting-new-standard-responsible-ai-infrastructure/)、[Compute Campus Policy Blueprint PDF](https://cdn.openai.com/pdf/compute-campus-policy-blueprint.pdf)、[CNBC·OpenAI pay for power](https://www.cnbc.com/2026/11/05/openai-to-pay-for-data-center-power-after-election-shows-ai-concern.html)、[TeraWulf PR](https://investors.terawulf.com/news-events/press-releases/detail/148/terawulf-secures-google-credit-backstop-for-project-financing-in-support-of-19-billion-anthropic-lease-executes-definitive-fluor-epc-agreement)

昨天观点写过主权与刷榜账本；今天新的冷水是：**算力要过邻居的选票**，契约与信用背书是同一条链上的反应。受益的是社区沟通/公用事业成本分摊顾问、可削减负荷的柔性用电方案、带信用增强的租约融资；付钱的是把选票写成「联邦已立法全面禁建」、或把 Compact 写成「已覆盖全部第三方托管校园」的人。标「选票 ≠ 联邦禁令；约 **41**/**10** 州与 404 口径须并列；蓝图呼吁 ≠ 已成州法；信用背书 ≠ 已并网；约 **$19B** 为租约承诺口径」。

- 基建 / 能源项目：把「自付全成本 + 高峰可减负荷 + 本地就业报告」写进标书，而不只是 MW 数。
- 模型公司：产能地图同时标「能买到的卡」和「邻居愿不愿意让你建」。
- 读者：转发选票结果务必带「地方措施、非全国停工」标签。

教程：本条无操作教程；政策文本以 [OpenAI 原文与 Blueprint PDF](https://openai.com/index/setting-new-standard-responsible-ai-infrastructure/) 为准。

### 8. YC：W27 逾期仍审，F26 Demo Day 12-02

YC Apply 本轮再核验：W27 准时截止已过，仍收逾期；准时申请约 **December 11** 前获决定；F26 Demo Day 仍定 **December 2**。同窗 Conductor（YC）并入 Meta 已写入头条。Launch HN **Kino AI**（YC S23）协作视频编辑（Agent 可同场）升温，完整编辑器免费、Pro 约 **$25**/编辑席/月——篇幅所限不单开。

来源：[YC Apply](https://www.ycombinator.com/apply/)、[YC Demo Day](https://www.ycombinator.com/demoday)、[Launch HN·Kino AI](https://news.ycombinator.com/item?id=50368804)

批次窗还开着，alumni 却已在被写进大厂壳——和头条是同一条并购潮的 YC 侧。受益的是仍想冲 W27 的团队、做 Agent 协作媒资的工具；付钱的是把逾期写成「与准时同等承诺」的人。标「逾期仍审 ≠ 保证面试；Demo Day 日期 ≠ 已公开完整榜单」。

- 想申请 W27：还能交，别再等完美叙事。
- 观察并购：YC 写码 Agent 被收，说明「壳」比「再训一个小模」更好卖。

教程：申请以 [YC Apply](https://www.ycombinator.com/apply/) 为准。

## 论文研究

### 9. 硬评测合集：GDPx 顶约 12%、LoLBench resolved 约 14%

**SemiAnalysis GDPx**（通讯署 **Nov 02**，本窗回捞）：约 **206** 题、**11** 域（芯片/安全/生物/金融/法律等），默认约 **8** 小时；公开榜顶 Claude Opus **5.5** 约 **12.0%**、Gemini **4** Carbon 约 **10.9%**、GPT-**6** Astra 约 **9.6%**——公司称最佳亦仅约 **12%**；金融/法律在严格二元打分下多模接近 **0**。**LoLBench**：约 **100** 题 / **29** 个大型开源系统，仓库均约 **2.4M** LoC；评 **28** 个 Agent，最高 resolved 仅约 **14%**（Claude Code / mini-SWE-agent × Opus **5**）；失败最大头为跨模块定位不全。旁证 **RoboColosseum**：Unitree G1 人形五项任务无一策略完全完成，平均进度约 **13.3%–23.2%**。

来源：[SemiAnalysis·GDPx](https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities)、[GDPx 榜站](https://gdpx.semianalysis.com/)、[arXiv·LoLBench](https://arxiv.org/abs/2609.37143)、[HF·LoLBench](https://huggingface.co/datasets/lolbench26/LoLBench)、[arXiv·RoboColosseum](https://arxiv.org/abs/2611.02497)

壳可以很快被收购，真干活的硬尺子今天仍停在约一成到一成四——和头条、Uber 冷数据是同一根脊柱上的「别把演示写成验收」。受益的是评测 harness、长程大仓定位工具、真机分布式评测池；付钱的是把约 **12%**/**14%** 写成「Agent 已全面无能」或反过来写成「已可无人交付整仓」的人。标「付费通讯/作者自建榜 ≠ 全量可复现；顶分口径随 harness 变；G1 零完成 ≠ 已证人形全面不可用」。

- 工程负责人：内部验收对齐「提案→跨模块落地」而不是单文件补丁通过率。
- 选型：GDPx 式域等权比单榜 SWE 更能打脸 PPT。
- 具身团队：先看 Open Track 盲测，再听一镜 demo。

教程：以榜站与 arXiv 为准；本条未核到针对 GDPx / LoLBench 的成熟跟练片。同类可搜「SWE-bench Harbor 评测」「agent harness 评测」公开教程作流程参考。

## 观点洞察

### 壳、闸、邻居：写码 Agent 与算力的三道账

昨天写的是物理层的三道门——能动、能过审、能托付。今天材料换了场地：Git 工作流、订阅额度、选票箱。

先说**壳**。OpenAI 收 Pierre，是把 diff 与 Code Storage 往 Codex 里收；Meta 收 Conductor，是把多 Agent 并行工作区收进自家；Factory 收 HumanLayer，是把「人在回路」的协作壳收进企业写码产品。Cat Wu 与 Austin Lau 赴 OpenAI，则是壳背后的产品与增长编制也在搬家。壳，指的是开发者每天打开的默认入口，不是又一个聊天框。

再说**闸**。ChatGPT 与 Codex **12** 月共享用量，是把「主聊天」和「写码 Agent」收到同一本账；Claude Code 把状态栏摘要从整段对话改成短笔记，自称约 **99%** 降本——这是工程闸；Apple 把员工日额度从约 **$300** 往下压，是组织闸。闸不过，壳再漂亮也只是演示环境。

最后是**邻居**。美中期选举里，数据中心相关地方选票几乎全线偏向限制或否决；OpenAI 同日抛出 Community Compact，讲自付电费、财务担保、水与噪声、本地岗位。TeraWulf×Google 为 Anthropic 肯塔基租约做信用背书，则是资本侧用另一张表回答「谁在担违约」。邻居，指的是机柜落地前要过的社区与选票，不是只算 $/GPU 时的表格。

我自己读材料时会多问三句：

1. **壳：** 这个 Agent 的分支、diff、审阅、权限，最后落在谁的产品里？用户能不能带着历史迁走？
2. **闸：** 额度是按会话、按座、还是按 ChatGPT+Codex 合并？状态栏/子 Agent/共享池有没有把「看不见的 token」写进账单？
3. **邻居：** 算力扩建有没有过地方票？电和水的全成本谁付？高峰能不能减负荷，而不是只贴「AI 工厂」海报？

过得了这三问，再谈 Images 2.6 的周四十亿张、Ripple 的约 **$32M** 训出开源写码模、或 commerce-agents 的购物车增益也不迟；过不了，再响的写码 Agent 叙事，都只是还没写进采购合同与社区听证的能力清单。个人观点，数字以各条原文为准，不构成投资或采购建议。

## 今日机会总结

今天的脊柱是：**写码控制面兼并与计量闸**（Pierre / Conductor / HumanLayer、共享用量、Claude Code 降本、Apple 额度、Cat Wu）、**可部署写码/Agent 基座**（Ripple / Kimi / SWE-2 Flash / ERNIE / Axion）、**算力社会许可**（选票 + Community Compact + TeraWulf 信用背书），外加安全边界、Uber 交易冷数据、企业控制面与硬评测约 **12%**/**14%**。观点侧把壳 / 闸 / 邻居收成三道账。

若只选三条可执行方向：

1. **可迁出的写码 Agent 控制层**：对标三起兼并，做审计、策略、协作与导出，而不是再做一个易被收编的壳；客户是怕被锁定的工程负责人。
2. **用量与降本观测包**：对齐 ChatGPT×Codex 合并额度、Claude Code 子 Agent 账单、企业内部日额度——卖「看得见的闸」，客户是被 **12** 月切表吓到的采购与平台组。
3. **算力落地的社区与公用事业包**：对标 Compact 与选票冷水，帮园区写全成本电费、高峰削减、本地就业与噪声水报告；客户是要过听证会的基建方，不是只要 MW 海报的买方。

## 普通人今天就能做的 3 件事

1. **重度用 Codex / Claude Code 的人：** 打开 [用量说明](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits)，把 **12** 月共享额度记进团队日历；本地执行 `claude --version`，低于 **2.1.316** 就升级。
2. **做私有化写码/Agent 的人：** 打开 [Kimi-K3.1-Pro HF](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) 与 [vLLM Day-0](https://vllm.ai/blog/2026-11-04-kimi-k31-pro)，先读许可与硬件适配范围，再决定是否值得排期试跑。
3. **关注算力与电费的人：** 读一眼 [OpenAI Community Compact](https://openai.com/index/setting-new-standard-responsible-ai-infrastructure/)，对照自己城市有没有类似「谁付配套电费/谁承担停建风险」的条款——这比只盯模型参数更接近今天的真实约束。

---

*草稿待审阅；确认后再发博客。有要改的直接说。*
