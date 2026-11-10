# 阶段 1 候选池 — 案例提取器（v4.10 / 第 15 类来源）

- **源文档**：`C:/Users/周至/AppData/Local/Temp/seafood_guide.md` — FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版（June 2022）导出全文，实测 31,322 行 / 1,709,446 字节。本文所有行号均以此文件为准。
- **上游目标**：本来源将作为第 15 类来源蒸馏成 1 张能力卡，用户要求「完整危害分析判定链」；本候选池专供能力卡 **A1（书中案例）** 段取用，只收指南「亲自演示过」的实例，不收法规条文、不收二手摘要。
- **检索策略**：局部命中型取块提取（Grep 定位锚点 → 按命中行号分块 Read 上下文 → 截取散文段落）。锚点关键词见文末「覆盖率自查」。
- **引用约定**：英文原句一律用 `> ` 引用块，每块 ≤100 词，只取散文段落并标行号；导出件中的**表格单元、页眉页脚**（如 `A2 - 1 (June 2021)`）、以及 **Table 3-1 / Table 3-2 等字符粘连文本一律不作逐字引用**，仅以中文描述其内容。
- **判定链定位约定**：「18 步」据 Ch.2「THE STEPS」清单（L1542–1615）与 L1828–2085 的 STEP 11–18 标题（STEP 1–5 预备步骤 / STEP 6–10 危害分析工作表 / STEP 11 识别 CCP / STEP 12–18 HACCP 计划表）。「四段式」为本文定位用映射：**段①** 产品与工艺描述 / 潜在危害识别（STEP 2–9）、**段②** 显著性判定（STEP 10）、**段③** CCP 定位与控制策略（STEP 11–13）、**段④** 监控·纠偏·记录·验证（STEP 14–18）。若能力卡已有正式四段式定义，以能力卡为准。
- **产出时间**：2026-11-06。
- **案例数**：11（C-01 – C-11）。

---

## C-01 Ch.2 建表实例：STEP 2 描述食品/包装、STEP 3 描述分销储存

- **依据行号**：L1542–1630（THE STEPS 清单 L1548–1615；STEP 2 L1565–1595；STEP 3 L1619–1630；STEP 4 L1631–1656）。
- **指南演示了什么**：指南在「亲自建表」环节给出**可直接照抄的示例清单**，把抽象的产品描述拆成三问：① 鱼种的市场名/拉丁名（`Tuna (Thunnus albacares)`、`Shrimp (Pandals spp.)`、`Jack mackerel (Trachurus spp.)`）；② 成品食品形态（`Individually quick frozen, cooked, peeled shrimp`、`Fresh tuna steaks`、`Frozen, surimi-based, imitation king crab legs`、`Fresh, raw drum, in-the-round`、`Raw shrimp, in-shell`、`Raw, shucked clams`、`Fresh seafood salad, with shrimp and blue crabmeat`、`Frozen, breaded pollock sticks`、`Frozen crab cakes`）；③ 包装类型（`Vacuum-packaged plastic bag`、`Aluminum can`、`Bulk, in wax-coated paperboard box`、`Plastic container with snap lid`）。STEP 3 再给分销储存示例（`Stored and distributed frozen`、`Distributed on ice and then stored under refrigeration or on ice`）。关键在于：这些字段不是登记用的行政信息，而是后续 STEP 7/8 查 Table 3-2/3-3（物种）与 Table 3-4（成品类别+包装类型）的**检索键**——描述填错，危害识别整条链就从源头偏掉。
- **判定链位置**：18 步 STEP 2（Describe the food）、STEP 3（distribution & storage），兼作 STEP 4（intended use/consumer）与 STEP 7/8 的输入；四段式段①（产品与工艺描述 / 潜在危害识别的起点）。
- **可迁移到的新问题**：给定「冷冻面包鳕鱼块、真空塑料袋、-18℃ 冷链分销、供一般公众充分加热后食用」，应如何逐项填写 STEP 2/3/4，并据此预判会命中 Table 3-4 的哪一成品类别与包装类型？

> STEP 2: Describe the food. Identify the market name or Latin name (species) of the fishery component(s) of the product.
>
> STEP 3: Describe the method of distribution and storage. Identify how the product is distributed and stored after distribution.
>
> （L1565–1567、L1619–1622）

---

## C-02 Ch.2 组胺「无控制条件」二选一：同一现象得出相反结论

- **依据行号**：L1715–1731（STEP 7 尾部；`L1720–1731` 为二选一实例本体）。
- **指南演示了什么**：指南在讲「判定危害是否显著」之前，先立了一条裁决规则——**危害发生可能性必须在「假定没有任何控制措施」的条件下判断**（`The likelihood of a hazard occurring should be judged in the absence of controls.`）。随后用鲭鱼毒素（组胺）亲自演示同一表面现象（某鱼种「从未见组胺问题」）的两种归因：情形一，鱼本身不具备产组胺能力 → 危害「不是合理可能发生的」，不必列入 HACCP 计划；情形二，之所以没出问题是因为**船上已存在时间/温度控制** → 危害「是合理可能发生的」，必须把该控制纳入 HACCP 计划并设 CCP。这是全篇最凝练的一次「判定链」演示：**已有控制 ≠ 危害不显著**，反而恰恰证明控制不可省。L1715–1719 还先打了预防针：常规/传统操作里已有的有效控制，并不意味着该危害不显著。
- **判定链位置**：18 步 STEP 7（识别物种相关危害）与 STEP 10（Determine whether the potential hazard is significant）之间的裁决规则；四段式段②（显著性判定），是段②→段③ 的分叉闸门。
- **可迁移到的新问题**：某金枪鱼加工厂申诉「我们投产三年从未检出组胺，所以组胺不是显著危害、无需 CCP」，请依据本实例指出其推理错在哪、应追问哪两项事实，并给出两种归因下各自的判定结论。

> The likelihood of a hazard occurring should be judged in the absence of controls. For example, the fact that scombrotoxin (histamine) development in a particular species of fish has not been noted may be the result of (1) the inability of the fish to produce histamine or (2) the existence of controls that are already in place to prevent its development (e.g., harvest vessel time and temperature controls). In the first case, the hazard is not reasonably likely to occur.
>
> （L1720–1729）

> In the second case, the hazard is reasonably likely to occur, and the controls should be included in the HACCP plan.
>
> （L1729–1731）

---

## C-03 Ch.2 STEP 8「熟虾做沙拉」同时命中两个成品类别（最能体现判定链）

- **依据行号**：L1732–1760（STEP 8 全文；核心实例 `L1741–1752`）。
- **指南演示了什么**：指南在 STEP 8（查 Table 3-4，按成品食品+包装类型列出工艺相关危害）中亲自演示了一条极易漏判的规则：**一个产品可能同时符合 Table 3-4 中多个成品食品类别的描述**。示例是「把虾煮熟后用来做成品沙拉」——此时必须同时查 `cooked shrimp`（熟虾）与 `salads … prepared from ready-to-eat fishery products`（由即食水产品制备的沙拉）两个类别，并把**两类各自的潜在危害全部**写进危害分析工作表第 2 栏、且覆盖每一个加工步骤。指南同时点明 Table 3-4 只代表 FDA 现有最佳信息，仍须用自己的或外部专家经验补表外危害（L1753–1760）。这条实例把「产品描述（STEP 2）→ 类别匹配（STEP 8）→ 危害并集 → 逐步骤登记」完整串了起来，是 A1 段最该保留的判定链样本。
- **判定链位置**：18 步 STEP 8（Identify potential process-related hazards），上游锚定 STEP 2 的成品描述，下游喂给 STEP 9（Understand the potential hazard）与 STEP 10（显著性判定）；四段式段①（潜在危害识别）。
- **可迁移到的新问题**：某厂生产「熟蟹肉 + 即食鱼糜的冷藏海鲜沙拉，气调盒装」，它同时命中 Table 3-4 的哪些成品类别？请说明为何不能只按「沙拉」一类列危害，并写出并集登记到 Column 2 的操作步骤。

> You may need to include potential hazards for more than one finished product food category from Table 3-4, which will happen when your product fits more than one description. For example, if you cook shrimp and use it to prepare a finished product salad, you should look at both the "cooked shrimp" and the "salads … prepared from ready-to-eat fishery products" categories in Table 3-4, Column 1. Potential hazards from both finished product food categories apply to your product and should be listed in Column 2 of the Hazard Analysis Worksheet.
>
> （L1741–1752）

---

## C-04 Ch.3 Table 3-1 物种替换导致危害漏识别

- **依据行号**：L2162–2181（表前说明 L2162–2170；Table 3-1 本体 L2172–2181）。
- **指南演示了什么**：指南明确说这些例子「based on actual incidents of species substitution or misbranding」（基于真实的物种替换/误标事件），并给出一张四列对照表：**实际鱼种 → 该鱼种真正的物种相关危害 → 被误标成的名称 → 按误标名称会识别出的危害**。演示了 5 组错配（下表为**中文描述，因导出件该表存在字符粘连，不作逐字引用**）：Escolar 标成 Sea Bass（真实的 Gempylid 鱼毒/组胺被漏，误按 Sea Bass 只识别寄生虫）；Puffer Fish 标成 Monkfish（河豚毒素/麻痹性贝毒被漏，误判为寄生虫）；Spanish Mackerel 标成 Kingfish（寄生虫、组胺、雪卡鱼毒被漏成「无」）；Basa 标成 Grouper（环境化学污染物、养殖药物被漏，误判为寄生虫/雪卡鱼毒）；Grouper 标成 Cod 则危害被低估。结论：**市场名是查 Table 3-2/3-3 的唯一入口，名称一错，STEP 7 的物种危害识别整栏作废**。
- **判定链位置**：18 步 STEP 2（Identify the market name or Latin name）与 STEP 7（按 Table 3-2/3-3 查物种相关危害）之间的失效模式；四段式段①（产品描述 → 潜在危害识别）的输入完整性校验。
- **可迁移到的新问题**：一批进口原料报「Monkfish」，但供应链证据显示实为 Puffer Fish；若危害分析按报美名称查 Table 3-2，会漏掉哪些危害、又凭空多出哪些危害？应如何把「物种身份核验」前置为 STEP 2 的控制点？

> Furthermore, species substitution may cause potential food safety hazards to be overlooked or misidentified by processors or end users, as shown in Table 3-1, "The Effect of Misbranding through Species Substitution on the Identification of Potential Species-Related Hazards." These examples are based on actual incidents of species substitution or misbranding.
>
> （L2163–2170）

---

## C-05 Ch.5 寄生虫：涉疫产品清单与冻结三条件

- **依据行号**：L4637–4652（产品清单）、L4654–4697（控制手段；`L4681–4691` 为冻结三条件）、L4709 起（显著性判定）。
- **指南演示了什么**：指南列出**曾实际引发人体寄生虫感染的产品清单**（ceviche 青柠汁腌鱼、lomi lomi 柠檬汁腌鲑鱼、poisson cru 柑橘汁腌鱼、herring roe、sashimi、sushi、green herring 轻腌鲱鱼、drunken crabs 酒腌蟹、cold-smoked fish 冷熏鱼、undercooked grilled fish 未熟烤鱼），并说明美国胃肠病医师调查证实此类感染有足够频率，因而对「拟生食的含寄生虫鱼种」应设预防控制（L4647–4652）。随后给出**冻结杀虫的三组等价条件**（任一即可）：-4°F(-20°C) 及以下冻藏 7 天（总时长）；或 -31°F(-35°C) 及以下冻至实心后同温保持 15 小时；或 -31°F(-35°C) 及以下冻至实心后 -4°F(-20°C) 及以下保持 24 小时；并注明对特别大的鱼（厚于 6 英寸）可能不适用。还顺带演示了「什么不算充分控制」：盐渍/醋渍仅降低不消除、修剪腹肉/灯检挑虫也不能降到可接受水平（L4692–4708）——这与 C-02 的「无控制条件」判定精神一致。
- **判定链位置**：18 步 STEP 9（Understand the potential hazard：理解危害发生条件与控制手段）与 STEP 10（显著性判定）；落到 STEP 13（Set critical limits，冻结三条件即为关键限值）与 STEP 14（监控冻藏温度/时间）；四段式段①→段②→段③/④。
- **可迁移到的新问题**：一款「青柠汁腌鲷鱼 + 冷熏」即食拼盘，寄生虫危害是否显著？若厂方只有 -20℃ 冷库、无 -35℃ 速冻，应选用三条件中的哪一条、记录里必须监控哪三个量、为何「腌渍」不能作为独立 CCP？

> Some products that have been implicated in human parasite infection are the following: ceviche (fish and spices marinated in lime juice); lomi lomi (salmon marinated in lemon juice, onion, and tomato); poisson cru (fish marinated in citrus juice, onion, tomato, and coconut milk); herring roe; sashimi (slices of raw fish); sushi (pieces of raw fish with rice and other ingredients); green herring (lightly brined herring); drunken crabs (crabs marinated in wine and pepper); cold-smoked fish; and, undercooked grilled fish.
>
> （L4637–4646）

> Freezing and storing at an ambient temperature of -4°F (-20°C) or below for 7 days (total time), or freezing at an ambient temperature of -31°F (-35°C) or below until solid and storing at an ambient temperature of -31°F (-35°C) or below for 15 hours, or freezing at an ambient temperature of -31°F (-35°C) or below until solid and storing at an ambient temperature of -4°F (-20°C) or below for 24 hours are sufficient to kill parasites. Note that these conditions may not be suitable for freezing particularly large fish (e.g., thicker than 6 inches).
>
> （L4681–4691）

---

## C-06 Ch.6 天然毒素：Example 1 源头控制 / Example 2 贝类采捕区控制

- **依据行号**：L5945–6073（CCP 定位 + Example 1 正文 + Table 6-1）、L6075–6123 及 L6267–6284（Example 2 正文 + Table 6-2）。
- **指南演示了什么**：指南先立 CCP 定位规则——**加工环节不可行时，天然毒素应在「接收」步骤控制**（L5949–5952），随后给出两个控制策略并各配一张「假定应用」的 HACCP 计划表：

| Example | 控制策略 | CCP 位置 | 监控什么 |
| --- | --- | --- | --- |
| Ex.1 源头控制（非软体贝类的鱼，L5974 起） | 拒收来自禁渔区、毒素消费建议区、已知雪卡毒素污染区的鱼（L5982–5993）；仅适用一级加工商（L5979–5981） | Receiving（接收新鲜鱼） | 渔船捕捞记录中标示的**捕捞区状态**（是否受限/建议/禁捕），目视核查，每批（L5994–6011）；关键限值偏离即拒收并停用供应商 |
| Ex.2 采捕区控制（软体贝类，L6075 起） | 每容器须带标签（采捕日期/地点、种类数量、捕捞者或船注册号），且必须来自 shellfish control authority 批准水域（L6079–6123） | Receiving（接收带壳贝类） | 进厂贝类**标签信息**，逐袋目视检查，拒收无标签袋（Table 6-2 L6284，中文转述） |

  两张表各自「亲自演示」了一个具体加工主体：Ex.1 是**接收本地捕捞 grouper、控制雪卡毒素**的一级加工商；Ex.2 是**直接从捕捞者接收 shellstock oysters** 的一级加工商。表格标题下还统一声明「天然毒素可能只是该产品若干显著危害之一，另查 Table 3-2/3-4」——即本策略只解决一条危害，不替代完整危害分析。
- **判定链位置**：18 步 STEP 11（Identify critical control points）与 STEP 13–17（关键限值 / 监控 What·How·Frequency·Who / 纠偏 / 记录 / 验证）；四段式段③（CCP 定位与控制策略）+ 段④。
- **可迁移到的新问题**：一家一级加工商接收本地捕捞的 grouper，已知该海域偶有雪卡毒素消费建议；CCP 应设在哪个步骤、关键限值如何表述、监控「什么/如何/频率/谁」四栏各填什么？若换成直接从捕捞者收带壳牡蛎，CCP 与监控对象应作何改变？

> This example table illustrates a hypothetical application of the control strategy just presented in "Control Strategy Example 1 – Source Control for Fish Other Than Molluscan Shellfish." The example illustrates the basic control for natural toxins by a primary processor receiving locally harvested grouper. It is provided for illustrative purposes only.
>
> （L6047–6049）

> This example table illustrates a hypothetical application of the control strategy just presented in "Control Strategy Example 2 Harvest Area Control for Molluscan Shellfish." This example illustrates how a primary processor of shellstock oysters, could control natural toxins in shellstock oysters received directly from a harvester. It is provided for illustrative purposes only.
>
> （L6270–6272）

---

## C-07 Ch.9 环境化学污染物与农药：Control Strategy Example 1–4

- **依据行号**：L10191–10549（Table 9-1 L10191–10206；Example 2 L10209–10326；Table 9-2 L10330–10341；Example 3 L10344–10450；Table 9-3 L10454–10470；Example 4 L10473–10519；Table 9-4 L10535–10548）。
- **指南演示了什么**：本章用「同一危害（环境化学污染物与农药）、七种控制策略」的方式亲自演示了**同一危害可因证据来源不同而把 CCP 放在不同位置、监控不同对象**。前四个 Example 各自配一张「仅供说明」的 HACCP 计划表，且每张表都点名一个具体加工主体：

| Example | 控制策略 | CCP 位置 | 监控什么 | 表中演示主体 |
| --- | --- | --- | --- | --- |
| Ex.1 On-Farm Visits（Table 9-1） | 收获前现场访问审查养殖条件/周边土地利用 + 取鱼体或池水样检测 | **Pre-harvest**（收获前） | 书面签字的现场访问报告 + 污染物/农药残留检测结果；每个生长周期每场至少一次 | aquacultured tilapia（L10193） |
| Ex.2 Supplier's Certification（L10209 起，Table 9-2） | 每批随附供应商证书/保证书，声明鱼非来自污染水域 | Receiving | 证书/保证书**是否存在**（目视），每批 | aquacultured trout（L10332） |
| Ex.3 Records of Testing and Monitoring（L10344 起，Table 9-3） | 查验证据链：新供应商池水/源水分析 + 所有供应商鱼体组织检测 + 年度土地利用报告 | Receiving | 检测报告与监测报告（目视核对），新供应商首次交货查水、所有供应商每批查鱼体、每年查土地利用 | farm-raised striped bass（L10456） |
| Ex.4 Chemical Contaminants Testing by Processor（L10473 起，Table 9-4） | 加工商自行取样检测；关键限值=不得超过联邦耐受量/行动水平 | Receiving | **鱼体组织中的残留量**，用经验证方法分析，每批 | aquacultured eel（L10537） |

  注意四者的迁移逻辑：从「自己去现场」→「信供应商一纸证书」→「查第三方检测记录」→「自己逐批化验」，CCP 由 Pre-harvest 前移到 Receiving，监控对象由「报告/证书的存在」变为「实测残留量」。表格还反复提示「实际计划须另行指定具体污染物、取样方案、分析方法」（L10194–10197）——即示例表只是骨架。
- **判定链位置**：18 步 STEP 11（CCP 定位）、STEP 13（关键限值）、STEP 14（监控 What/How/Frequency/Who）、STEP 15–17（纠偏/记录/验证）；四段式段③ + 段④。
- **可迁移到的新问题**：一家无自有实验室的养殖罗非鱼进口商，在 Ex.1–Ex.4 中应选哪一种策略？CCP 设在哪、监控栏填「证书存在」还是「残留实测值」、验证环节须补什么？若后来建成自有实验室，判定链上哪几栏必须改写？

> This table provided for illustrative purpose only is an example of a portion of a HACCP plan using "Control Strategy Example 1 - On-Farm Visits." This example illustrates how an aquacultured tilapia processor can control environmental chemical contaminants and pesticides.
>
> （L10193–10194）

> What Will Be Monitored? Presence of a certificate signed by the farmer or authorized farmer's representative, or other supplier (e.g., middleman, collector) specifying that fish were harvested from uncontaminated waters. How Will Monitoring Be Done? Visual check for the presence of a certificate or letter of guarantee.
>
> （L10233–10242）

---

## C-08 Ch.9 环境化学污染物与农药：Control Strategy Example 5–7（含野生捕捞与贝类）

- **依据行号**：L10551–11009（Example 5 L10551–10692 / Table 9-5 L10696–10709；Example 6 L10712–10793 / Table 9-6 L10797–10808；Example 7 L10811–10992 / Table 9-7 L10996–11009）。
- **指南演示了什么**：后三个 Example 把控制策略从「养殖」扩展到「第三方认证 / 野生捕捞 / 软体贝类」，继续演示「控制策略 → CCP 位置 → 监控什么」：

| Example | 控制策略 | CCP 位置 | 监控什么 | 表中演示主体 |
| --- | --- | --- | --- | --- |
| Ex.5 Third-Party Farm Certification（L10551 起） | 凭第三方农场认证证书或官网名录，声明供应商在认证计划下运行；指南特别强调「即便有第三方认证， verifying 产品不超耐受量仍是加工商责任」（L10596–10601） | Receiving | 第三方证书 / 在线名录文件**是否存在**（目视），每批或每个生长周期至少一次 | aquacultured barramundi（L10699） |
| Ex.6 Source Control for Wild-Caught Fish（L10712 起） | 拒收来自因污染被关闭的商业捕捞区、或处于消费建议区的野生鱼 | Receiving | **捕捞区状态**——捕捞者声明或捕捞记录，并核对监管机关网站/公告，每批 | wild caught bluefish（L10799） |
| Ex.7 Source Control for Molluscan Shellfish（L10811 起） | 贝类标签 + 批准采捕水域（与 C-06 的 Ex.2 同构，但危害换成环境化学污染物） | Receiving | 进厂贝类**标签信息**，逐袋目视检查 | shellstock oysters（L10998） |

  Ex.6 与 Ex.7 的示范价值在于：同一「接收」CCP，监控对象可以是「一纸声明/一张标签」而非实验室数据；且 Table 9-7 明确提醒「采捕区污染物只是若干显著危害之一，另查天然毒素与采捕区病原体」。
- **判定链位置**：18 步 STEP 11、STEP 13–17；并回扣 STEP 9（理解危害来源：养殖 vs 野生 vs 贝类采捕区）；四段式段③ + 段④。
- **可迁移到的新问题**：一批野生蓝鱼来自某州已发布「多氯联苯消费建议」的水域，但供应商能提供逐批捕捞记录；请判断该批是否可接收、CCP 与监控对象是什么、若改用第三方认证证书（Ex.5）能否替代、加工商责任边界在哪？

> This table provided for illustrative purpose only is an example of a portion of a HACCP plan using "Control Strategy Example 6 - Source Control for Wild Caught Fish Other Than Molluscan Shellfish." This example illustrates how a wild caught bluefish processor can control environmental chemical contaminants and pesticides. Environmental contaminants and pesticides from the harvest area may be only one of several significant hazards for this product.
>
> （L10799–10802）

> What Will Be Monitored? Certificate or documentation indicating the farm operates under a third-party farm certification program. How Will Monitoring Be Done? Visual check for the presence of a certificate or documentation.
>
> （L10602–10609）

---

## C-09 Ch.11 水产养殖药物：Control Strategy Example 1–5

- **依据行号**：L13050–13614（Table 11-1 L13050–13064；Example 2 L13067–13197 / Table 11-2 L13201–13229；Example 3 L13233 起 / Table 11-3 L13381；Example 4 L13416 起 / Table 11-4 L13511–13530；Example 5 L13533–13598 / Table 11-5 L13602 起）。
- **指南演示了什么**：本章把 C-07 的骨架移植到「养殖药物」危害，并亲自演示**关键限值如何被法规化的用药规则填满**（只用 FDA 批准/条件批准并按标签使用、由持证兽医监督的超标签使用、低监管优先清单、进口耐受量、INAD 研究性新药豁免 21 CFR 511 等，L13072–13096）。五个 Example 的三要素：

| Example | 控制策略 | CCP 位置 | 监控什么 | 表中演示主体 |
| --- | --- | --- | --- | --- |
| Ex.1 On-Farm Visits（Table 11-1） | 收获前现场访问审查用药与疾病预防方案 + 取样验证 | **Pre-harvest** | 书面签字的现场访问报告、INAD 证书；每个生长周期每场至少一次 | farm-raised tilapia（L13052） |
| Ex.2 Supplier's Certification（L13067 起，Table 11-2） | 每批随附证书声明仅用合规药物 | Receiving | 证书/保证书**是否存在**（目视），每批 | farm-raised shrimp（L13203） |
| Ex.3 Processor's Pre-Qualified Supplier Program（L13233 起） | 供应商须在预合格名录 + 持续或逐批证书 | Receiving | 名录资格与证书 | Table 11-3（L13381） |
| Ex.4 Records of Drug Use（L13416 起，Table 11-4） | 逐批调阅猪场用药记录 + INAD 证书 | Receiving | 每批**用药记录**（目视），每批 | farm-raised shrimp（L13513） |
| Ex.5 Drug Residue Testing（L13533 起，Table 11-5） | 加工商自检；关键限值=不得检出未批准药残 / 不得超 FDA 耐受量 | Receiving | **鱼可食部位药物残留**，经验证方法，每批 | farm-raised Tilapia（L13604） |

  与 C-07 对照可见：同一「七策略」结构在不同危害章复用，但关键限值内容随危害换成药物清单/耐受量，验证环节须写明「检测哪些药、取样方案、每种药的分析方法」（L13053–13055、L13606–13611）。这是能力卡「判定链可迁移」的好证据。
- **判定链位置**：18 步 STEP 11、STEP 13–17；四段式段③ + 段④；并与 STEP 9（理解危害）联动。
- **可迁移到的新问题**：一家养殖虾加工商的供应商只能提供逐批「合规用药证书」，无现场访问能力、无实验室；在 Ex.1–Ex.5 中应选哪个、CCP 设在哪、监控四栏填什么、验证环节是否仍需抽样送检？若某批检出未批准药物残留，纠偏与「恢复控制」两步分别做什么？

> This table is an example (for illustrative purposes only) of a portion of a Hazard Analysis Critical Control Point (HACCP) plan using "Control Strategy Example 1 - On-Farm Visits." This example illustrates how a primary processor of farm-raised tilapia can control aquaculture drugs.
>
> （L13052–13053）

> What Will Be Monitored? Presence of a certificate signed by the farmer or authorized farmer's representative, or another supplier (e.g., middleman, collector) indicating proper drug usage.
>
> （L13107–13112）

---

## C-10 Ch.19 过敏原 / 亚硫酸盐：Control Strategy Example 1–4 与「CCP 前移」

- **依据行号**：L24200–24281（Example 1–4 的 `*Example:*` 斜体实例段与策略命名）、L24270–24716（Example 1 正文 L24270 起 / Table 19-2 L24400–24424；Example 2 L24428–24505 / Table 19-3 L24509–24533；Example 3 L24537–24586 / Table 19-4 L24590–24614；Example 4 L24618–24683 / Table 19-5 L24689–24714）。
- **指南演示了什么**：本章最值得进 A1 的是**同一危害因「成品标签是否声明」而把 CCP 放在不同步骤**的亲自演示。四个 Example 三要素：

| Example | 控制策略 | CCP 位置 | 监控什么 | 表中演示主体 |
| --- | --- | --- | --- | --- |
| Ex.1 Finished Product Label Examinations（L24270 起，Table 19-2） | 成品标签审查，保证配料表声明过敏原且标签贴对产品；可用单一 CCP，也可拆成两个 CCP（L24298–24309） | **Finished product labeling** | 成品标签配料表是否列出 sablefish 与 Yellow No. 5；每批首张 + 之后每小时一张 | hot smoked sablefish / smoked fish processor（L24402） |
| Ex.2 Receiving Controls for Pre-printed Labels（L24428 起，Table 19-3） | 预印标签到货时审查，把 CCP 从贴标前移到收标签 | **Receiving of pre-printed finished product labels** | 预印标签配料表与产品规格/过敏原清单比对；每批抽若干卷 | raw breaded fish fillets and fingers（pollock、eggs、wheat、soy）（L24511） |
| Ex.3 Raw Material Testing（L24537 起，Table 19-4） | 原料亚硫酸盐筛查；关键限值 <10 ppm | **Shrimp receiving**（原料接收，非成品标签） | 每批进厂原料亚硫酸盐残留（malachite green test），代表性取样 | shell-on shrimp（L24592） |
| Ex.4 Review of Supplier Declarations or Labeling（L24618 起，Table 19-5） | 审核供应商「未用亚硫酸盐」声明或原料标签；标签未声明时 CCP 设在接收 | **Shrimp receiving** | 每批供应商证书/声明或原料标签目视；验证=每季度每供应商至少抽 1 样送检、每个新供应商至少 1 样 | shell-on shrimp（L24691） |

  L24244–24254 与 L24262–24278 两个斜体实例把判定链讲透：冷冻虾加工商**成品标签不声明亚硫酸盐**时，应把 CCP 设在「原料接收」并检测/取证，此时成品标签环节**不需要**为该危害再设 CCP；反之若标签已声明，控制点就落在标签。这直接演示了「产品描述（标签是否声明）→ 危害定位 → CCP 位置」的因果链。
- **判定链位置**：18 步 STEP 2/3（标签与产品描述）、STEP 8（工艺相关危害识别）、STEP 11（CCP 定位）、STEP 13–17；四段式段①→段③→段④，且是「输入条件改变导致 CCP 位置改变」的范例。
- **可迁移到的新问题**：一款冷冻去壳虾成品标签未声明亚硫酸盐，厂方把 CCP 设在「成品贴标」并逐张核对标签——请依据 Ex.3/Ex.4 指出错在哪、CCP 应移到哪一步、关键限值取多少、监控与验证各填什么？若厂方改为在标签上声明亚硫酸盐，判定链又该如何改写？

> A frozen shrimp processor receives shrimp directly from the harvest vessel and does not label the finished product with a sulfiting agent declaration. The processor should set the CCP for sulfiting agents at the raw material receiving step and test incoming lots of shrimp for the presence of sulfiting agents. The processor would not need to have a CCP for this hazard at finished product labeling.
>
> （L24245–24254）

> This table is an example of a portion of a HACCP plan using "Control Strategy Example 1." This example illustrates how a smoked fish processor can control undeclared major food allergens and food intolerance substances in the production of hot smoked sablefish. It is provided for illustrative purposes only.
>
> （L24402–24403）

---

## C-11 Appendix 2 产品流程图示例：FROZEN SALMON FILLETS（Figure A-1）

- **依据行号**：L1657–1669（Ch.2 STEP 5 正文及回指）、L25824–25883（Appendix 2 全文；Figure A-1 L25831；步骤框 L25833–25867）。
- **指南演示了什么**：指南给出一张可直接仿制的**产品流程图**，标题 `FIGURE A-1: PRODUCT FLOW DIAGRAM EXAMPLE: FROZEN SALMON FILLETS`，用 12 个顺序步骤框演示「从接收到分销」的物料流：Receiving → Fish Pump → Sort → Refrigerated Storage → Head/Gut → Wash → Fillet → Inspect → Freeze → Glaze → Weigh/Package → Frozen Storage（L25833–25867，均为表格框，按约定不作逐字引用）。Ch.2 L1668–1669 明确写「Figure A-1 (Appendix 2) is an example of a flow diagram」，即这张图是 STEP 5 的示范产出；STEP 6（L1671–1675）紧接着要求「把流程图中的每个加工步骤逐一抄进危害分析工作表第 1 栏」，STEP 7/8 再要求「在**每一个**加工步骤」登记潜在危害（L1707–1708、L1737–1740）。因此这张 12 框图不是孤立插图，而是整条判定链的物理骨架：框的数量与顺序决定了 Column 1 行数，进而决定 Column 2 要逐步骤列多少危害、以及 CCP 只能落在哪些真实存在的步骤上。L25876–25882 还引出 Appendix 3 的 CCP 决策树，并警告不可完全依赖决策树。
- **判定链位置**：18 步 **STEP 5（Develop a flow diagram）**，是 STEP 5 的产出、STEP 6（Set up the Hazard Analysis Worksheet）与 STEP 7/8（逐步骤识别危害）的输入；四段式段①（产品与工艺描述）。须与「12 个加工步骤」区分：12 步是产品流程图的内容，18 步是建表流程，Figure A-1 位于后者第 5 步。
- **可迁移到的新问题**：为「冷冻三文鱼片」画出 Figure A-1 式流程图后，18 步中紧接着要做的两步是什么？请说明流程图中每个框如何变成危害分析工作表 Column 1 的一行、为何 Refrigerated Storage 与 Frozen Storage 两个框都必须在 Column 2 逐行登记危害、以及 CCP 为何只能出现在这 12 个框所对应的步骤上。

> STEP 5: Develop a flow diagram. The purpose of the diagram is to provide a clear, simple description of the steps involved in the processing of your fishery product and its associated ingredients as they "flow" from receipt to distribution. The flow diagram should cover all steps in the process that your firm performs.
>
> （L1657–1663）

> This appendix contains a product flow diagram that can be used as an example when you develop your own flow diagram.
>
> （L25826–25827）

---

## 覆盖率自查

**检索过的关键词（Grep，全文）**

| 关键词 / 正则 | 用途 | 命中概况 |
| --- | --- | --- |
| `Control Strategy Example` | 定位各章控制策略实例 | 大量命中，集中在 L467/474（Ch.4）、L4023–4850（Ch.5 寄生虫）、L5955–6284（Ch.6）、L9649–11009（Ch.9）、L12129–13935（Ch.11）、L14655–15533（Ch.12）、L17560–17653（Ch.13）、L22506–22515（Ch.16）、L24208–24691（Ch.19）、L25470–25517（Ch.20）等 |
| `Table 3-1` | 定位物种替换实例 | L2166（表前说明） |
| `Table 3-4` | 定位 STEP 8 成品类别表引用 | L1734 / 1743 / 1749 / 1753（STEP 8 引用）、L2118（目录）、L3437（表头） |
| `STEP 1[1-8]:` | 核验 18 步编号 | L1828 / 1875 / 1891 / 1934 / 1980 / 2027 / 2048 / 2085（STEP 11–18） |
| `*Examples:*` / `Examples:` | 定位 Ch.2 示例清单 | count 8（L1568 / 1574 / 1588 / 1623 / 1635 / 1649 等） |
| `FROZEN SALMON FILLETS\|ceviche\|Escolar\|Poisson\|Puffer\|scombrotoxin\|histamine` | 定位 Ch.3 / Ch.5 / Appendix 2 具体实例词 | count 290 |
| `STEP`（Ch.2「THE STEPS」清单） | 核验 STEP 1–10 名称与顺序 | L1542–1615、L1560 / 1565 / 1619 / 1631 / 1657 / 1671 / 1676 / 1732 / 1761 / 1774 |

**实际读过的行号区间（Read 分块）**

| 区间 | 内容 |
| --- | --- |
| L1540–1779 | Ch.2 THE STEPS 清单、STEP 1–10 正文、组胺二选一（1720–1731）、熟虾沙拉（1741–1752） |
| L2160–2204 | Ch.3 Table 3-1 表前说明与表体（含字符粘连）、Table 3-2 表头 |
| L4620–4714 | Ch.5 寄生虫涉疫产品清单、冻结影响因素与三条件、显著性判定开头 |
| L5940–6124 | Ch.6 CCP 定位规则、Control Strategy Example 1 全文、Table 6-1、Example 2 前半 |
| L6265–6286 | Ch.6 Table 6-2 说明散文与表头 |
| L10190–10359 | Ch.9 Table 9-1、Example 2 全文、Table 9-2、Example 3 开头 |
| L10340–10519 | Ch.9 Example 3 全文、Table 9-3、Example 4 全文 |
| L10535–10829 | Ch.9 Table 9-4、Example 5 / 6 / 7 正文、Table 9-5 / 9-6 |
| L10990–11009 | Ch.9 Table 9-7 说明散文 |
| L13045–13264 | Ch.11 Table 11-1、Example 2 全文、Table 11-2、Example 3 开头 |
| L13505–13614 | Ch.11 Table 11-4、Example 5 全文、Table 11-5 说明 |
| L24200–24309 | Ch.19 Example 1–4 的斜体实例段、DEVELOP A CONTROL STRATEGY |
| L24400–24719 | Ch.19 Table 19-2 / 19-3 / 19-4 / 19-5 与 Example 1–4 正文 |
| L25815–25909 | Appendix 2 Appendix 2 说明、Figure A-1 步骤框、Appendix 3 决策树开头 |

**仅 Grep 定位、未逐块精读**（诚实标注，避免虚报覆盖）：L1828–2085（STEP 11–18 标题，仅取编号与名称）、L2118 / L3437（Table 3-4 目录与表头）、L467–474 / L4023–4850 / L12129–12683 / L14655–15533 / L17560–17653 / L22506–22515 / L25470–25517（其它章的 Control Strategy Example 命中，本轮未纳入案例）。

**6 大块要求覆盖核对**：① Ch.2 建表 + 组胺二选一 + 熟虾沙拉 → C-01 / C-02 / C-03 ✓；② 各章 Control Strategy Example（Ch.6 / Ch.9 / Ch.11 / Ch.19）→ C-06 / C-07 / C-08 / C-09 / C-10 ✓；③ Ch.3 Table 3-1 → C-04 ✓；④ Ch.5 寄生虫清单与冻结三条件 → C-05 ✓；⑤ Appendix 2 流程图 → C-11 ✓；⑥ 目标 8–12 个案例 → 11 个 ✓。所有英文引用块均为散文段落、每块 ≤100 词并标行号；Table 3-1、各 Table 单元、页眉页脚与粘连文本均仅以中文描述，未作逐字引用。
