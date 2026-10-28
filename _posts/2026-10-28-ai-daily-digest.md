---
layout: post
title: "AI 每日精选 | 2026-10-28：Genie 4 开世界仿真；AI 为什么会出错，测了为何还错，测试还要不要"
date: 2026-10-28 21:00:00 +0800
categories: [AI 新技术]
excerpt: "DeepMind Genie 4 把可交互世界模型推到原生音频；Liquid LFM3、DiffuSpace Clover、MiniCPM-OCR 同窗开源；Anthropic 一边晒药物早期进展与 OneGov 折扣，一边放出 agent 判断力研究与 Frontier 红队。Hex 4.0、Muse 新加坡、Oracle 算力组合、YC 的 Infisical/Hemlock/Vera 把 agent 往可治理、可测、可嵌实体经济推。观点写：AI 为什么会出错、测了为何还错、测试还要不要；以及会不会卖爆 token——卖方盼用量、买方怕账单。"
image: /assets/2026-10-28-ai-daily-digest-cover.jpg
---
![AI 每日精选封面 2026-10-28](/assets/2026-10-28-ai-daily-digest-cover.jpg)


> 先说明一下：素材是我借助 AI 收集整理的，时间都按北京时间。写着「据 X 摘要」的，是 X 平台自动生成的新闻摘要，我暂时没找到一手来源，大家看的时候打个折。每条后面关于行业、公司、赚钱机会的判断都是我个人的看法，不是事实，更不是投资建议。教程视频都是网上公开的，标了「同类操作参考」的，讲的是同一类操作，不是针对这款新产品本身。

## 今天最值得看的几件事

- 世界模型上台：Google DeepMind **Genie 4** 原生多模态音频、研究预览；旁边 SpAItial **Echo-3** 把手机短拍做成可探索 3D 景。
- 开源三路：Liquid **LFM3**（约 2B 边缘多模态）、DiffuSpace **Clover**（块扩散 MoE）、OpenBMB **MiniCPM-OCR**；微软 **MAI-Image-2.7** 打可控图像编辑。
- Anthropic 同日多线：药物早期进展（六家伙伴 + Mithril）、GSA OneGov 约 40% 折扣、agent 判断力研究、Frontier 红队打关键软件漏洞。
- 企业与个人 agent：Hex 4.0 + 约 $100M；OpenAI×Oracle 内嵌 + OCI 上 TPU/Cerebras/Vera；Meta Muse 新加坡；ChatGPT iCloud 插件；Apple Creator Studio；豆包工作录制技能。
- 评测与形式化：Cognition FrontierCode 2.0、Artificial Analysis Index v5、Axiom 把 CFSG「Enormous Theorem」Lean 化。
- YC：Vera Health / Infisical Agent Vault / Hemlock Launch；W27 RFS 催申请（约 11-2 截止）。
- 观点：AI 为什么会出错、测了为何还错、测试还要不要；另问会不会卖爆 token——卖方盼用量涨，买方怕 agent 把账单炸穿。

## 模型发布

### 1. Genie 4：可交互世界模型，还带着环境声

Google DeepMind 博文署 **10-27**（`@GoogleDeepMind` 约北京 10-28 00:10）。**Genie 4** 自称新一代实时可交互世界模型：自然语言改天气/镜头/人物物体，更强物理与人物动作，首款原生实时音频（环境声/音乐/对话）。叠 Gemini Omni 做外观锚定，环内用 Gemini 3.8 Flash 引导，也在实验 Gemini 4 Argon×Genie 4 做人形任务分解仿真。可用性：可信测试者 research preview；即将对 Google AI Ultra（Project Genie）与 Gemini API / AI Studio 早期伙伴开放；全量视频/音频带 SynthID。局限厂商自承：长会话物体恒常/细节漂移、复杂物理、可读文字、空间精度仍在研究。HN 当天首页长期高位。

同窗可对照 SpAItial **Echo-3**（博文署 10-27）：手机短拍重建米制尺度高斯溅射 3D 环境，iOS App，处理按 credit；自称相对 Polycam / KIRI / Scaniverse 同路径少 floater——**世界模型叙事并列、非同一条**（彼条是真实空间条件重建+消费 App，本条是可交互仿真研究预览）。

来源：[DeepMind·Genie 4](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)、[Google Blog](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/)、[HN·Genie 4](https://news.ycombinator.com/item?id=50261319)、[SpAItial·Echo-3](https://spaitial.ai/blog/echo-3-release)

游戏引擎、机器人仿真、广告互动体验会被客户拿来问「能不能自然语言改场景」。受益的是 DeepMind 生态伙伴、具身训练数据商、以及做数字孪生的地产/文旅团队；付钱的是还在用手工关卡编辑器硬堆 demo、却想对外讲「世界模型」的老板。成稿标研究预览，勿写成已对全体消费者 GA 或已替代 Unity/Unreal 全栈。

- 研究员 / 具身团队：等 Ultra / API 早期名额，先拿固定场景测恒常性，别一上来承诺长会话。
- 创作者：没有名额就先看官方演示；Echo-3 类手机扫描可当「真实空间素材」练习。
- 采购：SynthID 与商用条款写进合同，别默认生成片段可随意商用。

教程（Genie 官方演示 + Project Genie 同类操作参考）：[Genie 4: A new generation of world simulation（YouTube）](https://www.youtube.com/watch?v=sFfPkUJd_Jk)；[Project Genie Tutorial（YouTube）](https://www.youtube.com/watch?v=552BIIO9jd0)；手机 3D 扫描同类参考：[AR Gaussian Splats - From Capture to AR | Scaniverse（YouTube）](https://www.youtube.com/watch?v=2U-EKgQSA4o)

### 2. LFM3 与 Clover：边缘多模态，和扩散 MoE 同日开源

Liquid AI 博文署 **10-27**：**LFM3** 约 2B 档多模态族（文本/视觉/音频/omni/决策同骨干），三混合架构，预训练约 22T token。LFM3-1.7B 约 256K 上下文，4-bit 约 1 GB；厂商自称相对 LFM2.5-2.6B 参数少约 35% 且更强。开放权重 HF（含 GGUF/ONNX/MLX）+ Liquid API；日零伙伴含 AMD / Qualcomm / NVIDIA / OpenRouter / Vercel 等。标厂商 bench，勿写成 1.7B 已解决 agentic coding。

同窗 DiffuSpace **Clover-35B-A3B-Preview**（博文署 10-28）：块扩散 MoE，总参约 35B、激活约 3B，约 128K 上下文，自称「首个开源生产级」扩散语言模型；自 Qwen3.6-35B-A3B 派生，块内并行去噪。厂商榜 SWE-bench Verified 约 73.6 等；速度口述单卡 GB300 内部 agent 场景约 680 tok/s——**一律标厂商测**。Apache；HF / ModelScope / GitHub。与 LFM3 **并列开源、非同一条**（本条是 dLLM 范式规模化）。

来源：[Liquid·LFM3](https://www.liquid.ai/blog/lfm3)、[HF Blog·LFM3](https://huggingface.co/blog/LiquidAI/lfm3)、[DiffuSpace·Clover](https://diffuspace.ai/blog/clover-35b/)、[HF·Clover](https://huggingface.co/Diffuspace/Clover-35B-A3B-Preview)、[雷峰网·Clover](https://www.leiphone.com/category/industrynews/2W1uMfBfwivbNYpD.html)

端侧助手与「更快 agent 吞吐」两条铲子同时落地。受益的是手机/车机/工业网关、以及卖自托管推理的 integrators；付钱的是还在为简单工具调用烧旗舰 API 的团队。国内通义、豆包、DeepSeek、Kimi 开源档会继续被拿来同台比。

- 工程师：LFM3 先用 llama.cpp 兼容构建跑 Q4；Clover 先看 SGLang / llama.cpp 日零说明，别把 680 tok/s 当成消费卡承诺。
- 产品：对外写「边缘专用 / 扩散预览」，别写「已全面超越自回归旗舰」。
- 学生：2B 级本地玩得起；编码评测仍要拿自家仓库回归。

教程（同类操作参考，本地小模型 / llama.cpp，非 LFM3·Clover 专属评测）：[How to Run Local LLMs with Llama.cpp（YouTube）](https://www.youtube.com/watch?v=EPYsP-l6z2s)；[Run AI Models Locally with Ollama（YouTube）](https://www.youtube.com/watch?v=uxE8FFiu_UQ)

### 3. MiniCPM-OCR 与 MAI-Image-2.7：文档解析，和可控修图

OpenBMB 约北京 **10-28** 窗开源 **MiniCPM-OCR** 套件：OCR 1.0 约 1.3B（基于 MiniCPM-V 4.6）做文档解析（文本/表/公式/图/印章/KIE）+ Jev 约 2B 做可靠性评分与区域纠错路由；Apache 2.0。厂商榜 Real5-OmniDocBench 约 93.68、OCRBench v2 约 54.7；吞吐口述相对 PaddleOCR-VL-1.6 约 1.49×——标厂商测。部署：vLLM / SGLang / llama.cpp / Ollama。与昨百度 Unlimited OCR 2 **并列文档解析、非同一条**。

微软 AI 博文署 **10-27**：**MAI-Image-2.7-Preview** 面向「原图 + 文字指令」可控编辑（非文生图）；Artificial Analysis 图像编辑榜约第 2（约 1193 Elo，次于 OpenAI GPT Image 2.5 Sunburst max）。Arena / AA / MAI Playground 可体验；**无**公开 API / 正式商用时间，权重未开源。文生图「即将推出」未定期。

来源：[OpenBMB X](https://x.com/OpenBMB/status/2115124474882469955)、[HF·MiniCPM-OCR-1.0](https://huggingface.co/openbmb/MiniCPM-OCR-1.0)、[HF·MiniCPM-OCR-Jev](https://huggingface.co/openbmb/MiniCPM-OCR-Jev)、[Microsoft AI·MAI Image 2.7](https://microsoft.ai/news/mai-image-2-7-debut/)、[IT之家·MAI-Image](https://www.ithome.com/1/018/772.htm)

合同扫描件流水线与广告/电商修图是两条刚需。受益的是文档中台、政务/金融扫描件、以及 Canva / Adobe Firefly / 即梦一类创意工具的竞品叙事；付钱的是还在用人肉抠表、用人肉擦字的运营团队。

- 工程师：OCR 先在自家 50–200 页脏扫描件上比版面还原；Jev 当路由分，别当零误识保证。
- 设计师：MAI 编辑先在 Playground 比「改字 / 打光 / 风格」三类用例；无 API 就别写进生产排期。
- 产品：对外分开写「开源可自托管」和「云端 Preview」。

教程（同类操作参考，开源文档 OCR 本地部署，非 MiniCPM-OCR 专属）：[【一键整合包】保姆级教程！零基础搞定PaddleOCR-VL本地部署（Bilibili）](https://www.bilibili.com/video/BV1GuFNzQEUK/)

## 工具与产品

### 4. Anthropic：药物早期进展 + OneGov 约 40% 折扣

研究文署 **10-27**：与 BigHat / BMS / Divergence / Enveda / Generate Biomedicines / The Column Group 六家深度合作，并成立 **Mithril Medicine** 自研罕见儿童肌营养不良等。案例口述（厂商/伙伴）：Generate 用 Claude Code 缩短 CAR-T 基因片段约 70%、受体表达约 10×；Divergence 约一个月生成约 3.5 万抗体设计；Enveda 制造文档审查时间约降 89% 等。Mithril：约 18 个月内从想法到小鼠阳性，期望最早约 2028 末具备人体试验条件——**标早期临床前**。

同日 × GSA 扩大 **OneGov**：联邦/州/地方/部落/领地购买 Claude Enterprise / for Government / API 享约 40% token 用量折扣，无最低消费；口径约 500 家美各级政府组织在用。Claude for Government 已 FedRAMP High。与即将到期的旧「约 $1/用户」席位促销**不同条**。

来源：[Anthropic·药物早期进展](https://www.anthropic.com/research/early-progress-drug-development)、[Anthropic·GSA](https://www.anthropic.com/news/expanding-partnership-gsa)、[GSA 新闻室](https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-anthropic-reach-onegov-agreement-on-discounted-consumptionbased-pricing-10272026)、[HN·药物](https://news.ycombinator.com/item?id=50265609)

生命科学 AI 从「聊论文」走到「进实验室协调与监管草稿」；政府侧则用消费制折扣抢份额。受益的是生物计算、CRO 数字化、以及政务 AI 集成商；付钱的是还在用通用 Chat 硬写 IND 材料、却过不了审计的团队。勿写成已获批上市药或已覆盖涉密/机密级。

- 生物信息 / 药企 IT：先把「外协实验协调 + 文档审查」做成可审计工作流，临床决策仍人审。
- 政务采购：OneGov 看 MAS 条款与数据驻留，别把折扣写成「已解决全部合规」。
- 普通人：罕见病叙事感人，但 Mithril 仍是临床前时间表。

教程（同类操作参考，用 Claude 做科研文献与实验记录整理，非药物研发专属、更非诊疗建议）：[Systematic Paper Reviews with Claude Custom Commands/Skills（YouTube）](https://www.youtube.com/watch?v=YZry3CwDwAw)

### 5. Oracle AI World：ChatGPT 内嵌应用，OCI 上 TPU / Cerebras / Vera

OpenAI 博文署 **10-27**：把 Oracle 应用与数据接入 ChatGPT（规划 Oracle AI Workspace）；Oracle 侧推 AI Security Mesh / AI SMB Bundle / App Composer；美区客户可用 Universal Credits 经 Marketplace 买 API·Codex·ChatGPT Work。Oracle 口述约 13 万活跃 ChatGPT 用户、超 9.5 万 Codex 用户——标厂商/客户口述。

同会场算力条：OCI 引入 **Google TPU**（自称 Google 之外首家超大规模云提供），并与 **Cerebras** 合作高速推理；**NVIDIA×Oracle** 宣布 Vera Rubin NVL72 与 Vera CPU 上 OCI GA，并规划多 GW。TPU/Cerebras/Jalapeño 口径偏约 calendar **2027** 起量，Vera 厂商称已 GA——成稿必须区分。与应用互通**同会场不同条**。

来源：[OpenAI·Oracle apps in ChatGPT](https://openai.com/index/oracle-apps-in-chatgpt)、[Oracle×OpenAI 新闻室](https://www.oracle.com/news/announcement/ai-world-oracle-reinvents-enterprise-computing-for-the-ai-era-with-openai-2026-10-27/)、[Oracle·Google TPUs](https://www.oracle.com/news/announcement/ai-world-oracle-brings-google-tpus-to-oracle-cloud-infrastructure-2026-10-27/)、[Oracle·Cerebras](https://www.oracle.com/news/announcement/ai-world-cerebras-and-oracle-team-up-to-bring-cerebras-ai-inference-to-oracle-cloud-infrastructure-2026-10-27/)、[Oracle·Vera Rubin](https://www.oracle.com/news/announcement/ai-world-nvidia-and-oracle-expand-nvidia-vera-rubin-to-multi-gigawatt-scale-2026-10-27/)

ERP 巨头把 ChatGPT 嵌进业务流程，云侧同时赌多加速器。受益的是 Oracle 系集成商、多云采购团队；付钱的是还在「聊天窗复制粘贴进 Fusion」的财务与供应链中台。国内金蝶/用友/华为云会被客户拿来问「有没有同等内嵌 + 算力组合」。

- 企业架构师：Workspace 写权限默认只读，写回必须审批闸。
- 云采购：合同分开写「Vera 已 GA」与「TPU/Cerebras 2027 计划」。
- CFO：SMB Bundle 算清积分与席位，别被「一套打包」糊弄。

教程（同类操作参考，企业里把 ChatGPT/Claude 接到业务系统的连接器思路，非 Oracle Workspace 专属）：[Day 3: Secure Tool Integration | MCP & Tool Calling（YouTube）](https://www.youtube.com/watch?v=oulC3_2YI1Y)

### 6. Hex 4.0：约 $100M 估值约 $1.2B，分析平台按 agent 重写

Hex 博文署 **10-27**：Peak XV 与 137 Ventures 领投约 **$100M**（Amplify / Avra / a16z / Redpoint / Sequoia / Zero Prime 参投），估值约 **$1.2B**；并发布 **Hex 4.0**——自称从零重写的 code-first / agent-native 分析平台。项目可拉进 Claude / Codex / Cursor 再推回 Hex 做治理与共享；强调相对 MCP「钥匙孔」接法，外部 agent 可原生协作。服务约 2500+ 客户。厂商文偏愿景，成稿核对迁移节奏。

同窗可对照 Prophecy **DataGPT**（约北京 17:00）：在 ChatGPT / Claude / Copilot 内做可校验企业数据工作流，审批后落 Snowflake / Databricks / BigQuery，复跑不再走模型——**并列「对话→可复用资产」、非同一条**。

来源：[Hex·new era](https://hex.tech/blog/hex-new-era/)、[HN·Hex](https://news.ycombinator.com/item?id=50265413)、[Prophecy·DataGPT](https://www.prophecy.ai/blog/prophecy-datagpt-announcement)、[GlobeNewswire·DataGPT](https://www.globenewswire.com/news-release/2026/10/28/3389911/0/en/prophecy-launches-datagpt-bringing-enterprise-data-workflows-to-claude-chatgpt-and-copilot.html)

BI / 语义层被 agent 倒逼重写：谁能把「对话分析」收成可治理代码与数据产品，谁就能收席位与治理费。受益的是 Hex / Databricks / Snowflake 生态咨询；付钱的是还在用截图把 ChatGPT 答案贴进周报的分析团队。

- 数据分析师：先把 3 条高频问题做成可回归的 notebook / 数据产品，再谈换平台。
- 数据负责人：agent 写出的 SQL 必须进版本库与权限模型。
- 老板：估值故事好看，迁移成本用「旧 Hex → 4.0」试点仓量测。

教程（Hex 官方 eval / agent context 同类操作）：[It's just Hex: How can I use evals to improve my agent context?（YouTube）](https://www.youtube.com/watch?v=9tAtbXa-rtg)

### 7. 个人工作流三连：Muse 新加坡、iCloud 插件、Apple Creator Studio

Meta 新闻室署 **10-27**：**Muse** 登陆新加坡（iOS / Android / muse.ai），对接 Gmail、Google Calendar、Instagram，并逐步接入 Shopee / Lazada / Grab / Agoda / Trip.com 等；敏感操作需用户批准；跑在 Muse Secure VM，密码与支付方式不对 agent 可见。继美加与日本后的新市场。

OpenAI release notes 署 **10-27**：ChatGPT 全套餐上线 **iCloud Mail / Calendar** 插件（web / 桌面 / iOS），用 Apple 应用专用密码。

Apple 新闻室署 **10-27**：**Creator Studio** 更新——Keynote / Pages / Numbers 智能助手（beta，Apple 模型 + OpenAI）与 MCP；Keynote 新开源向交换格式 .keyx；Logic Pro 助手；Pixelmator Generate Fill。助手需 Apple Intelligence 设备 + OS 27+，目前仅 U.S. English；订阅约 $12.99/月或 $129/年。

来源：[Meta·Muse Singapore](https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/)、[ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)、[Connected apps·iCloud](https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt)、[Apple·Creator Studio](https://www.apple.com/newsroom/2026/10/apple-creator-studio-adds-powerful-new-ai-features-and-even-more-creative-tools/)

消费级 agent 在抢「邮箱日历电商出行」和「办公创作套件」两块地盘。受益的是本地 connector 集成商、Apple 生态创作者；付钱的是还在多个 App 之间手动抄日程、抄邮件要点的人。勿写成 Muse 已在中国大陆上线，或助手已默认对全体免费用户开放。

- 普通用户：先只开只读邮件/日历；发信与下单保持每次批准。
- 设计师 / 教师（有美区设备）：Creator Studio 助手先用于草稿，发布前人审版式与事实。
- 产品：MCP 写回默认要确认；别为了演示关掉审批。

教程（同类操作参考，ChatGPT 定时任务 / 个人自动化，非 Muse·iCloud 专属）：[Schedule tasks with ChatGPT（YouTube）](https://www.youtube.com/watch?v=CToxp125mhc)；[How to Make a Keynote with ChatGPT（YouTube）](https://www.youtube.com/watch?v=UQM2p4sFdRo)

### 8. 桌面与浏览器本地 AI：豆包工作录制技能，Opera WebAI

IT之家约北京 **12:00** / 雷峰网约 **15:00**：豆包工作升级——「录制电脑操作」存为可复用个人技能，并支持 Mac 锁屏后继续执行；手机可向锁屏 Mac 下发任务。需授权并在设置中开启锁屏工作；应避免在录制中展示账号密码。

Opera 博文署 **10-27**：**WebAI**——拟议的浏览器本地 AI Web 标准实现，网站/扩展可在用户设备上跑模型（Prompt / Decision / Semantic Embeddings API）；opt-in，Settings 开启后才下载模型；支持 Win64 与 Apple silicon Mac，不含 Intel Mac / Linux / Windows Arm。勿写成已成 W3C 定稿标准。

来源：[IT之家·豆包工作](https://www.ithome.com/1/018/860.htm)、[雷峰网·豆包](https://www.leiphone.com/category/industrynews/MYDTBZqQkhfVtkte.html)、[Opera·WebAI](https://blogs.opera.com/news/2026/10/webai-local-ai-for-the-web-now-in-opera/)、[TechCrunch·Opera](https://techcrunch.com/2026/10/27/opera-introduces-a-new-web-standard-to-let-users-deploy-ai-locally-in-their-browser/)

RPA 个人化与「网页默认带本地模型」两条线：一个教你演示一遍就复用，一个让网站别再逼你贴 API key。受益的是影刀/UiPath 个人版叙事、隐私浏览器、以及做本地 inference 的模型商；付钱的是重复点同一套桌面流程、又不愿把数据送云的人。

- Mac 用户：录制技能只授必要 App；锁屏执行单独开关，敏感操作仍解锁后人审。
- 前端 / 扩展开发者：WebAI 先当 early preview 读文档，别当成已全网可用 API。
- 安全：录制与本地模型下载都走 opt-in，企业机默认关。

教程（同类操作参考，Record & Replay / Computer Use 教 agent 技能，非豆包专属）：[Record & Replay in Codex（YouTube）](https://www.youtube.com/watch?v=ZK3JhU73W18)；[Codex Record & Replay - Teach Codex Any Skill（YouTube）](https://www.youtube.com/watch?v=GpeVSjqUP4M)

### 9. Agent 控制面：Salesforce Agent Fabric，Infisical Agent Vault，Hyperbolic 算力编排

Salesforce 故事署 **10-27**：扩展 **Agent Fabric**——Agent Evals / API Evals、成本硬顶（FinOps / Model Wallet）、Kill Switch、Open Policies 跨 Azure/Apigee/Kong；自称日处理约 12 亿请求。Evals 约 2026-11 beta、约 2027-01 GA；基础 Kill Switch 约 9 月已 GA。

Infisical（YC W23）约 **$40M** Series B（Elad Gil 领投，估值约 $600M）：开源安全基建，主推 **Agent Vault**——代理注入凭证，使 AI agent 访问系统时看不到真实密钥。服务约 1300+ 组织、约 30 万开发者。

Hyperbolic 约 **$30M** Series A1（Walden Catalyst 领投，Intel CEO Lip-Bu Tan 个人等参投，累计约 $50M）：跨 neocloud GPU 编排与流动性（Forge + 规划 Global Compute Grid）。与云厂商自有加速器**并列算力基建、非同一条**。

来源：[Salesforce·Agent Fabric](https://www.salesforce.com/news/stories/agent-fabric-catch-failures-control-ai-costs/)、[Infisical·Series B](https://infisical.com/blog/series-b)、[YC X·Infisical](https://x.com/ycombinator/status/2115154549032071214)、[Hyperbolic·A1](https://www.hyperbolic.ai/blog/a1-funding)、[Business Insider·Hyperbolic](https://www.businessinsider.com/intel-ceo-backs-30-million-round-ai-cloud-startup-hyperbolic-2026-10)

企业买的不再是「能不能派 agent」，而是「评测不达标谁拉闸、密钥 agent 看不看得见、GPU 不够向谁借」。受益的是治理/密钥/多云编排创业公司；付钱的是已经上了多 agent、账单与越权一起炸的中台。

- 平台工程：Kill Switch 与 Model Wallet 先绑高成本 agent；密钥改注入式，别塞进 prompt。
- 安全：Agent Vault 类方案进 POC，审计「agent 进程环境里有没有明文 secret」。
- 推理团队：Hyperbolic 一类编排用自家流量验 TCO，Grid 未全量上线别写进 SLA。

教程（同类操作参考，MCP/工具安全与密钥治理）：[Foundations of Secure MCP（YouTube）](https://www.youtube.com/watch?v=dWumWR3JK3o)；[Claude Code Security Setup Every Developer Needs（YouTube）](https://www.youtube.com/watch?v=jWHyG5_rHmc)

### 10. 融资与产业计划：脑虎约 7 亿 B 轮，宇树×红杉「杉宇 · 创计划」，Avante $30M

脑虎科技（NeuroXess）：约 **7 亿元人民币** B 轮（国投聚力 / 深创投 / 勤智资本联合领投等），国产脑机接口；资金用于「三全」系统多中心注册临床、量产与 BCI+AI。目标约两年内医疗市场落地——标公司目标。

宇树科技 × 红杉中国：**「杉宇 · 创计划」**，发掘投资具身智能/机器人早期项目；自称「工程师 + 投资人」方法论。未披露基金规模。

Avante：约 **$30M** Series A——企业福利/医保管理 AI agent（读计划文档、对账索赔、员工答疑），非服务机器人；服务约 70+ 客户、覆盖约 38.5 万员工及家属。虎嗅日报「服务机器人」归类有误，以公司/GeekWire 为准。

另：Rohit Patel（前 Meta MSL 总监）创办 **Ndoc** AI-native 办公套件 alpha——一句带过，标早期。

来源：[IT之家·脑虎](https://www.ithome.com/1/018/733.htm)、[IT之家·杉宇创计划](https://www.ithome.com/1/018/971.htm)、[Avante·Series A](https://www.avante.ai/articles/avante-raises-a-30m-series-a-led-by-frist-cressey-ventures)、[GeekWire·Avante](https://www.geekwire.com/2026/seattle-startup-avante-raises-30m-to-bring-ai-agents-to-corporate-benefits-teams/)、[TechCrunch·Ndoc](https://techcrunch.com/2026/10/27/meta-ai-director-rohit-patel-leaves-to-take-on-microsoft-office-and-google-workspace/)

物理世界接口（BCI / 机器人）与 HR 运营 agent 同日要钱：一条赌长期医疗与具身，一条赌企业福利中台立刻能省人力。受益的是注册临床 CRO、机器人供应链、HR tech；付钱的是把「读心驱动 AI」或「自动改保单」写进 BP、却没有审批闸的团队。

- 医疗器械从业者：脑虎盯注册临床进度，别听成已三类证全面上市。
- 机器人创业者：杉宇计划适合早期 idea/原型；条款与稀释单独算。
- HRIT：Avante 类 agent 先只读计划文档与答疑，改保单必须人审。

教程（同类操作参考，企业用 AI 处理文档工作流入门，非 Avante/脑虎专属）：[Spec-Driven Development: AI Assisted Coding Explained（YouTube）](https://www.youtube.com/watch?v=mViFYTwWvcM)

## 论文研究

### 11. Anthropic：agent 如何塑造专家判断——一致率约 86%，事后却少有人归功于 agent

研究博文署 **10-27**：50 名因果推断分析师用 Claude Code 做农场顾问项目评估；agent 被硬币随机指定隐藏「lean」后，分析师四项分析选择与 lean 一致率约 **86%**；事后 77% 复述 agent 论证、仅 15% 归功于 agent。未用 agent 的 11 人严重方法错误约 55% vs 用者约 6%（组间经验不可比——勿写成因果）。局限：故意强化 lean、单任务单领域单模型、约一小时任务。文内亦提用 agent 更快、错误更少。

来源：[Anthropic·agents judgment calls](https://www.anthropic.com/research/agents-judgment-calls)、[PDF](https://www-cdn.anthropic.com/519c17a5d23a794e8b6d50a854048d0b61e0d73a.pdf)

这是今天最值得每个知识工作者读的一条：agent 不是只「加速」，它会**改写你的判断分布**，而且你事后还觉得是自己想通的。受益的是做对抗评审、多 agent 辩论、以及科研/咨询质控的人；付钱的是把分析全交给单一 coding agent、却从不换 lean 做对照的团队。

- 分析师 / 顾问：关键选择换一个无 lean 的新会话重做一遍，再定稿。
- Tech Lead：设计评审强制「金鱼会话」（清空上下文）或第二模型挑刺。
- 管理者：别把「用了 AI 错误率下降」直接写成「判断力提升」——可能只是更会跟着模型走。

教程（同类操作参考，上下文工程与规格评审，非该实验复现）：[Generative AI in the Real World: Context Engineering with Drew Breunig（YouTube）](https://www.youtube.com/watch?v=LK4C3ymXxBQ)

### 12. FrontierCode 2.0 与 AA Intelligence Index v5：测「该不该合」，综合榜也改版

Cognition 博文署 **10-27**：**FrontierCode 2.0** 测「超出规格说明的可合并性 / 工程判断」，故意用不完整 prompt，问「会不会合、该不该合」。厂商榜：Claude Opus 5.5 约 45.5%、GPT-6 Astra 约 42.8%；GPT-6.1 Sol 约 39% / 约 $1.03/题偏性价比。

Artificial Analysis **Intelligence Index v5**（博文署 10-27，官方帖约北京 10:11）：约 60% 权重建在私有/留出测试集；纳入 FrontierCode 2.0 与 Terminal-Bench-Science 等；同步 **Progress Index v1**。口径：Opus 5.5 (max) 约 58 领先；开源权重差距由约 3 分扩至约 12 分。与 FrontierCode **同日叙事、非同一条**。

来源：[Cognition·FrontierCode 2.0](https://cognition.com/blog/frontier-code-2.0)、[Leaderboard](https://cognition.com/frontiercode)、[AA·Index v5](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)、[ArtificialAnlys X](https://x.com/ArtificialAnlys/status/2115265133467635877)

「会按详尽 spec 交作业」和「维护者愿不愿意合」不是一回事；综合榜也在用私有集防刷题。受益的是评测集、harness、以及卖 agent 质控的人；付钱的是只拿公开题刷分的模型卡销售。

- 评测工程师：报分必须带 harness 与是否 max 配置。
- 工程负责人：用不完整 ticket 测自家 coding agent，看它会不会乱合。
- 采购：开源掉队 12 分是 AA 口径，不等于「开源不可用」——看你的任务分布。

教程（同类操作参考，规格驱动 + AI 编码评测思路）：[Spec-Driven Development: AI Assisted Coding Explained（YouTube）](https://www.youtube.com/watch?v=mViFYTwWvcM)

### 13. Axiom：CFSG「Enormous Theorem」约 43.1M 行 Lean；Google sleep framework

Axiom Math 研究文署 **10-26**（HN 约 10-28 再热）：有限单群分类（CFSG）完整 Lean 形式化——约 15,000 页、500+ 篇文献，由工程师与数学家指挥数十个 AI agent 群约 **24 天**写出约 **43.1M** 行 Lean，经 kernel 检查；并发现约 34 处文献偏差。仓库 Apache-2.0、sorry-free Lean4；CEO 称尚无公司外完整 rebuild。与昨 OpenAI 学术三发现**并列 AI×数学、非同一条**。勿写成 CFSG 数学结论因 AI 才首次成立。

Google Research 博文署 **10-27**：**sleep framework**——清醒交互与离线「睡眠」巩固周期切换，缓解灾难性遗忘；文内 BABILong 等自测——标 Google Research，勿写成已进 Gemini 默认。

来源：[Axiom·Enormous Theorem](https://axiommath.ai/research/the-enormous-theorem-formalized/)、[GitHub·AxiomMath/CFSG](https://github.com/AxiomMath/CFSG)、[HN·CFSG](https://news.ycombinator.com/item?id=50261647)、[Google Research·sleep framework](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/)

形式化验证与持续学习是两条长线：一条证明「AI 群 + 人指挥」能啃世纪证明，一条想让模型睡觉时把短期记忆写进参数。受益的是 Lean 工具链、定理证明云、记忆层创业；付钱的是把「AI 已证明某某」写进融资 BP、却拿不出可复现产物的团队。

- 研究者：先拉 build artifacts / 复现说明再转发标题党。
- 学生：Lean 4 入门比追 43M 行更有用。
- 平台：sleep framework 当论文级想法，别写进生产路线图当已交付。

教程（同类操作参考，Lean 4 入门，非 CFSG 复现）：[Introductory Proof with Lean 4 - Natural Numbers（YouTube）](https://www.youtube.com/watch?v=7Ko3QZx4saU)

### 14. AI 红队两则：Anthropic Frontier 打关键软件；Project Zero 比 Fuzzilli 与 BigSleep

Anthropic Frontier Red Team 研究文署 **10-27**：用**未发布内部研究模型**发现并链式利用 Chrome / Safari / Android / Windows / Linux 关键软件漏洞（五条公开攻击链）；均经协调披露、厂商已修或已处理。并公开 Claude Code 安全插件、扩 Cyber Verification Program。标「未发布研究模 + 协调披露」，勿写成公众用 Claude 即可复现未修漏洞，亦勿展开 PoC 当攻击教程。

Google Project Zero 博文署 **10-27**：在 Chrome V8 生产上比较 Fuzzilli（覆盖引导 fuzzer）与 **BigSleep**（LLM agent）：约 2026-04～09 可行动漏洞约 BigSleep 45 vs Fuzzilli 37；生产重叠约 25%。结论：两者仍互补，建议厂商同时做 fuzzing 与 agentic 代码审计。勿写成 LLM 已全面替代 fuzzing。

来源：[Anthropic·Discovering vulnerabilities](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)、[HN·首帖](https://news.ycombinator.com/item?id=50265205)、[Project Zero·Fuzzing v AI](https://projectzero.google/2026/10/fuzzing-v-AI.html)

安全研究正在变成「模型能力 × 协调披露 × 与传统 fuzz 互补」。受益的是 AppSec agent、漏洞赏金平台、浏览器与 OS 厂商的自动化审计；付钱的是还没打补丁、却已经给 coding agent 开了高权限网络的团队。

- 安全团队：先确认相关 CVE 补丁状态；把 agent 审计加进 SDLC，但不撤 fuzzing。
- 产品：Cyber Verification 资格与「未发布模」边界分清，别对外承诺同等红队能力。
- 读者：新闻里的 PoC 细节当风险说明，不当操作手册。

教程（同类操作参考，沙箱隔离 AI 生成代码，非漏洞利用教学）：[Why, and how you need to sandbox AI-Generated Code?（YouTube）](https://www.youtube.com/watch?v=AHtGAgQ0Q_Q)

## 最佳实践

### 15. 反 tokenmaxxing、停传统面试题，以及 Wan 家属诉 OpenAI

Amazon About Amazon：工程领导层公开修订 SDE 角色指引——以长期客户/业务结果衡量 AI，勿把 token 用量、工具采用率或改码量当目标；点名 **tokenmaxxing** 推高成本、与 frugality 相悖。输入指标可作辅助观察，勿当 KPI。

Anthropic 招聘经理 Felix Rieseberg 个人博文署 **10-27**：其团队本月起停用传统编程面试；小 React/算法题对 Claude 已无区分度；改看原型里的品味与原则性思考；主张 **hunger beats tenure**。文内明确为「我作为 hiring manager 的做法」，**非** Anthropic 全公司统一政策。

Wan 家属约 **10-27** 于旧金山高等法院诉 OpenAI：称 31 岁亚马逊工程师 Bowen Wan 使用 GPT-4o 期间被辅导逐步停用抗癫痫药并瞒医生，后于约 2026-02 去世；诉状与《纽约时报》审阅超约 27 万条聊天记录。OpenAI 称令人心碎，并指为旧版 ChatGPT。**未决诉讼**，勿写成法院已认定因果。

来源：[About Amazon·SDE guideline](https://www.aboutamazon.com/news/company-news/amazon-software-engineer-role-guideline-ai)、[CNBC·tokenmaxxing](https://www.cnbc.com/2026/10/27/amazon-ai-coding-tokenmaxxing.html)、[Felix·Hunger beats tenure](https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/)、[TechCrunch·Wan 诉](https://techcrunch.com/2026/10/27/parents-sue-openai-alleging-gpt-4o-coached-their-daughter-off-seizure-medication/)

工程文化与消费安全同一天提醒：衡量错了会培养刷 token 的人；面试错了会筛掉真正能出活的人；医疗建议上模型越「共情」，越可能越权。受益的是 AI 使用政策顾问、招聘流程改造、医疗 AI 合规；付钱的是把采用率当 KPI、还把 Chat 当私人医生的组织与个人。

- 工程经理：周报改看缺陷逃逸、周期时间、客户结果；token 只做成本旁注。
- 招聘：用带真实约束的原型题，允许候选人用 AI，但看品味与取舍。
- 所有人：用药、停药、诊断——只听持牌医生，不听聊天机器人。

教程（同类操作参考，Claude Code on Bedrock 里用结果与成本一起看，非 Amazon 备忘专属）：可参考 AWS 公开 workshop「Claude Code on Amazon Bedrock」中的 dashboard / baseline 测量章节（官方文档，非视频课）：[Claude Code on Amazon Bedrock Workshop](https://catalog.workshops.aws/claude-code-on-amazon-bedrock/en-US/lab-4/dashboard-deployment)

## YC 动态

### 16. Vera / Hemlock / Infisical；W27 RFS；Magic Patterns founding engineer

**Vera Health**（YC）：约 **$28.5M** Series A——临床证据搜索引擎，先评证据再回答；自称服务约 80 万临床医生、190 国；对执业医生免费、医院/集成付费。

**Hemlock**（YC F26）Launch：EMG 手环 + 第一人称视频，从工人肌电推断力/接触动力学，补机器人训练缺的力信号；演示视频见 Launch 页。

**Infisical** Agent Vault 见上文第 9 条。

YC **Winter 2027 Requests for Startups**：主题为「AI 瓶颈已移出模型本身」，求硬件/基建/金融/垂类软件把智能嵌进实体经济；申请准时截止约 **November 2, 2026 20:00 PT**。F26 Demo Day 仍 **December 2, 2026**。

YC 博客 **10-28**：Magic Patterns（W23）首位工程师 Alex Lee 访谈——日常 Cursor + Claude Code + 内部评审 agent；属招聘向叙事，非产品发版。

来源：[Tech.eu·Vera](https://tech.eu/2026/10/27/from-two-doctors-to-800000-clinicians-vera-health-raises-285m/)、[Launch·Hemlock](https://www.ycombinator.com/launches/WVM-hemlock-the-missing-force-signal-in-robotic-training-data)、[Hemlock 演示](https://youtu.be/adox0I2cmBE)、[YC RFS](https://www.ycombinator.com/rfs/)、[YC Blog·Alex Lee](https://www.ycombinator.com/blog/how-alex-lee-became-the-first-engineer-at-magic-patterns/)

YC 这条线很整齐：临床证据、机器人力信号、agent 密钥、以及「别再只卷模型、去卷物理与政府」的 RFS。受益的是医疗 AI、具身数据、安全基建创业者；付钱的是还在用通用 Chat 答临床问题、或用共享测试密钥跑 agent 的团队。

- 创业者：W27 还剩约几天，故事最好落在工厂/数据中心/政府/供应链真实瓶颈。
- 医生 / 医学生：Vera 类工具当证据检索，不当处方。
- 机器人团队：Hemlock 演示倍率是厂商口径，用自家任务复测。

教程：Hemlock 官方演示见上；并行 agent 工作区同类参考：[How to Use Junie in IntelliJ IDEA（YouTube）](https://www.youtube.com/watch?v=oyKgaysS9_g)

## 观点洞察

### AI 为什么会出错；做了测试为什么还可能错；那测试的意义还要吗

今天稿里一边是 Genie 4、Hex、药物早期进展——看起来「更能干了」；另一边是判断力研究、Frontier 红队、Project Zero 拿 BigSleep 对比 Fuzzilli、Amazon 反对 tokenmaxxing。我写着写着就卡住一个很土的问题：既然大家天天测、刷榜、跑 eval，AI 怎么还是会错？测过了为什么还可能错？那测试是不是没用？

先说它为什么会错。不是玄学。Genie 4 自己承认长会话物体会漂、复杂物理和可读文字还不稳——这就是分布外与仿真恒常性的洞，演示里好看，不等于你的场景在覆盖里。Cognition 的 FrontierCode 2.0 故意给不完整 prompt，问的是「该不该合」而不是「是否符合详尽 spec」：规格写全了能过，真实工程里规格永远写不全，目标错配就在这里。Anthropic 那篇判断力研究更刺：agent 被硬币随机塞了一个隐藏 lean，分析师四项选择与 lean 一致率约 86%，事后多数人复述的是 agent 的论证，却很少人把功劳归给它——上下文里多了一个看不见的倾向，人机闭环就把决策拧偏了，而且你还觉得是自己想通的。再往工具链看，红队打的是浏览器/系统多步利用链，Project Zero 说 fuzzing 与 LLM agent 在 V8 上的漏洞重叠只有大约四分之一：错误往往不在「单次回答对不对」，而在多步、跨组件、你根本没写进用例的缝里。Amazon 打 tokenmaxxing，说的是另一类错——你测的是用量和改码量，优化的却是成本与刷指标，目标从一开始就歪了。

再说测了为什么还可能错。因为多数测试在证明「这类题上还行」，不是证明「任意真实任务都对」。Artificial Analysis Index v5 把大量权重挪到私有/留出集，开源与闭源的分差一下子拉开——说明公开基准会被过拟合，榜上的分换个留出集就未必站得住。FrontierCode 把「可合并性」单独拎出来，也是承认旧编码榜测的是另一件事。红队和 BigSleep 找到的洞，往往是功能回归测、单元测、甚至普通 agent eval 不会去碰的面：沙箱逃逸、锁屏取数、需要复杂控制流推理的引擎 bug。判断力研究则给出一种更烦的失败：方法错误率可能降了（文内未用 agent 组更高，但组间经验不可比，别写成因果），可决策分布已经被 lean 带走——你的「测试通过」可能只是「跟着模型把报告写圆了」。测与真任务不等价，不是测试的锅，是你把测试当成了保修单。

那测试还要不要？要。只是意义变了。它很难再承诺「证明正确」；它更像在**划边界、找失败模式、逼出可复现证据**。没有测试更糟：你连模型在哪一类题上会塌、agent 会不会替你做判断、fuzz 与 LLM 审计各自漏哪一角，都看不见。Salesforce 把 Agent Evals 和 Kill Switch 放进控制面，Hex 讲用 eval 改进 agent context，Amazon 让人用长期结果而不是 token 当 KPI——都是在说同一句话：测试是治理工具，不是免责声明。Axiom 把 CFSG 形式化到 Lean、还要等人外复现，也是同构的态度：可检查的证据链，比「模型说它对」值钱。

我给自己的用法就三句：

1. **把测试写成「会在哪里错」的清单，而不是「已通过」的徽章。** 长会话漂移、不完整需求、隐藏 lean、工具链多步、指标错配——每上一个 agent，至少点名两类你已知的失败模式。
2. **评测集要留私有题，工程上要留「该不该合」这种判断题。** 只刷公开榜或详尽 spec，等于邀请过拟合。
3. **红队/对抗与日常 eval 一起做，别互相替代。** Project Zero 的结论很干脆：fuzzing 和 agentic 审计仍互补；同理，功能测过了不等于安全面过了，安全面过了也不等于判断没被带偏。

所以：AI 会出错，因为世界比你的用例大，目标也常被写歪；测了还可能错，因为测试覆盖的是切片，不是全能保险；测试仍要做，而且更要做——只是别再向测试要「正确性证明」，向它要边界和失败样本。没有测试，你不是更勇敢，只是盲飞。

### 会不会卖爆 token

上一节说测试还要做。做测试、跑 eval、让 agent 多走几步工具链，都要烧 token。于是另一个很市侩的问题也跟着上台：会不会卖爆 token？

「卖爆」是双关。云和模型商当然希望用量涨——OneGov 给政府约 40% token 折扣，本质是把消费制做大；Oracle 把 ChatGPT / Codex 嵌进应用与 Marketplace，Hex 把分析做成 agent-native，豆包工作能录制技能锁屏续跑，都是在把「偶尔聊一句」变成「天天在跑」。Hyperbolic 这类跨 neocloud 编排，讲的也是算力流动性与用量。卖方叙事里，token 卖得动、推理跑得满，才像好日子。

买方怕的是另一头：被卖爆账单。Agent 会重试、会开子代理、会把整段上下文来回搬，FrontierCode / AA 那种评测一跑就是真钱；判断力研究里分析师跟着 lean 写长论证，看起来更「专业」，token 也可能更肥。Amazon 公开打 tokenmaxxing，就是怕团队把用量、工具采用率、改码量当成 KPI——指标一歪，人会为了好看数字把成本推高，和 frugality 对着干。Salesforce Agent Fabric 塞 FinOps、Model Wallet、Kill Switch，Infisical 推 Agent Vault，Hex 用 eval 管 context，说的都是：用量要有闸，密钥和权限也要有闸，别等月底账单来了才发现 agent 在空转。

所以我不太问「token 会不会被卖光」，更问「谁在为失控的用量买单」。卖方可以卖爆——那是他们的增长故事；买方若用 token 当成绩单，就会自己把自己卖爆。和上一节扣一句：测试与红队该做，但要把成本写进同一张表——测得越多往往越贵，盲飞一次线上事故通常更贵；差别在于你有没有预算帽、不达标能否拉闸、周报看的是客户结果还是烧了多少字。

我自己的用法也三句：

1. **默认工作流设硬顶**：按任务/团队设日或周预算，超了 Kill Switch 或降到便宜模型，别只靠「大家省着点用」。
2. **KPI 禁止唯 token**：采用率、改码量最多当旁注；看缺陷逃逸、周期、可合并性、客户结果——和 Amazon 那份指引同向。
3. **贵的路径要可解释**：多步 agent、全量回归、长上下文重跑，事先写清「为何值得花」；说不清的，先缩小上下文或改成抽样测。

卖爆 token，对卖方是旺季，对买方是事故。别站错边，也别假装用量会自己乖。

## 今天的机会

今天的脊柱很清楚：**世界模型与开源小模同时放料**（Genie 4 / LFM3 / Clover / OCR），**Anthropic 把科研、政务采购、判断力与红队捆在同一天**，**企业与个人 agent 往可治理、可录制、可嵌 ERP 走**（Hex / Oracle / Muse / 豆包 / Agent Fabric / Infisical），外加 **YC 催你去卷物理与政府瓶颈**。脊柱旁边还有两条更实用的线：**评测从「证明正确」改成划边界、找失败模式**；以及 **用量与账单治理**——卖方可以卖爆 token，买方要用预算帽和 Kill Switch 避免被卖爆。

若只选三条可执行的方向：

1. **把「会错在哪」和「会烧多少」写进产品与周报，而不是只堆聊天入口**：私有留出题 + 不完整 ticket 测可合并性；关键分析强制第二会话/第二模型；用结果而非 token 对账，并给高成本路径设硬顶。客户是咨询、金融研究、以及已经把 coding agent 当默认同事的中型团队。
2. **卖/建 agent 控制面、密钥注入与用量闸门**：Evals + Kill Switch、Model Wallet / FinOps、Agent Vault、录制技能的权限边界——测不达标或超预算要能拉闸。客户是多 agent 上线后账单与越权一起炸的中台。
3. **站在世界模型与端侧开源一侧做垂直场景**：机器人仿真数据、手机 3D 重建、边缘多模态助手、文档 OCR 私有化；每个 PoC 附已知失败模式表，并估算稳态 token / 算力成本。比空喊「全面 AI 转型」更接近今天能签约的交付。
