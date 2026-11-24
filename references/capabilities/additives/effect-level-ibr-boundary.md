> 本卡隶属 CAP-31 来源路由入口 references/capabilities/direct-food-additives.md；加载前先读该入口卡。**本卡是横切口径层/效力层，不单独抢路由，须依附 V01–V04 业务卡使用。**

# 效力层与 IBR 边界（effect-level-ibr-boundary）

*来源分层与定位：本卡是**横切口径层**，不新增业务意图，只定义「Part 172 的条文里哪些内容可引用、哪些不可」。它覆盖 21 CFR Part 172 全篇的规格引用形态（实测 **43 条／27% 使用 incorporated by reference**），eCFR 2026-11-05 快照；〔§ 172.xxx〕是**第八套独立编号**，全包**二十三类来源不可混引**。效力栈恒为：**法规正文（八套编号）＞ FDA 指南（should 建议层）＞ CPGM／CP／IOM 检查程序（检查员视角、不创设企业义务）**；冲突时法规正文为准。本卡**不判**：许可链与五形态（→**V01**）、防腐剂/抗菌剂（→**V02**）、甜味剂（→**V03**）、名录导航（→**V04**）；不代写法律文书、不出合规结论、不判产品法定身份。*

## R — 原文

> "The percentage of TBHQ in the food additive is not less than 99.0 percent when tested by the assay described in the Food Chemicals Codex, 9th ed. (2014), pp. 1192-1194, which is incorporated by reference, or an equivalent method."
> —— 〔§ 172.185(b)〕[pdf-page 19]
> 中文自译：TBHQ 规格属**半开放 IBR**——条文给出一个可判的下限数值（≥99.0%），测法引用 FCC 9th ed. (2014) pp. 1192-1194，并保留「或等效方法」。可引用「≥99.0%」这一条文数值。

> "(b) The additive meets the specifications of the Food Chemicals Codex, 7th ed. (2010), pp. 993-995, which is incorporated by reference."
> —— 〔§ 172.831(b)〕[pdf-page 127]
> 中文自译：三氯蔗糖规格属**整体外转 IBR**——条文本体**不含任何 assay/杂质数值**，只可引「须符合 FCC 7th ed. (2010) pp. 993-995」。不得转述该文件内部数值。

> "(1) Assay for neotame, not less than 97.0 percent and not more than 102.0 percent on a dry basis. (2) Free dipeptide acid (N-[N-(3,3-dimethylbutyl)-L-α-aspartyl]-L-phenylalanine), not more than 1.5 percent. (3) Other related substances, not more than 2.0 percent. (4) Lead, not more than 2.0 milligrams per kilogram. (5) Water, not more than 5.0 percent."
> —— 〔§ 172.829(b)〕[pdf-page 124]
> 中文自译：纽甜规格**直写数值**——assay 97.0–102.0%、游离二肽酸 ≤1.5%、其他相关物质 ≤2.0%、铅 ≤2.0 mg/kg、水 ≤5.0%，可直接核对与引用。同一 Subpart 内，直写与整体 IBR 两种形态并存。

> "The analytical method for determining the potency of the additive entitled “Determination of Potency of LMP-102TM,” dated October 9, 2003, and printed by Intralytix, Inc., is incorporated by reference."
> —— 〔§ 172.785(b)(1)〕[pdf-page 109]
> 中文自译：噬菌体制剂的效价测法 IBR 到厂商文件——**测法名称、日期、出具方、菌株编号**全在外部；只可照抄「方法名称 + 日期 + 出具方」，不转述其内部数值。

> "(b) The food additive meets the following specifications: (1) As found in Food Chemicals Codex: (i) L-Alanine, pages 28 and 29."
> "(2) As found in “Specifications and Criteria for Biochemical Compounds,” NAS/NRC Publication, for the following:"
> —— 〔§ 172.320(b)〕[pdf-page 30–31]
> 中文自译：氨基酸规格走**二级引用链**——先指到 FCC 的具体页码、再指到 NAS/NRC Publication；须走到终点才知规格来源，且这些外部内容不可转述。

> "(b) The existence of a regulation prescribing safe conditions of use for a food additive shall not be construed to relieve the use of the substance from compliance with any other provision of the Act."
> —— 〔§ 172.5(b)〕[pdf-page 5]
> 中文自译：许可法规的存在不解除本法其他义务——这是「许可层 ≠ 整体合规」的效力边界条文依据。

**本卡反直觉口径清单（V05，效力层校准）**
1. IBR 文件与法规正文**效力等同**，但其内容**不在本 PDF、不在本技能包**——只可引「须符合某文件某版某页」。
2. IBR 有两种句式：**半开放**（给可判数值 + 或等效方法，如 TBHQ ≥99.0%）与**整体外转**（条文无数值，如三氯蔗糖）。判定先问「有没有可读数值」。
3. 同一 Subpart 内两种形态并存（纽甜直写 vs 三氯蔗糖整体 IBR）——**不能假设「有规格＝有可读数值」**。
4. 版次与页码不可张冠李戴：**FCC 7th ed.＝2010**、**FCC 9th ed.＝2014**。
5. 规格符合只是四元组一环，满足纯度不等于合规（回 V01）。
6. **不可逐字引用区**三类：16 张重建表格数值、§172.510/§172.515 名录内部行、全部 IBR 外部文件内容。
7. 效力栈：法规正文（八套编号）＞ FDA 指南（should）＞ CPGM/CP/IOM（检查员视角、不创设企业义务）。
8. **八套编号不得互引替代**：〔§ 172.xxx〕与〔§ 101/108/113/114/117/120/123.xxx〕各管各自义务。

## I — 自述

本卡不判业务，只管「引用边界」。任何一张 Part 172 子卡给出纯度规格时，都要过这道关，顺序是：① 判该规格是**直写数值**还是 **IBR 外转**；② 若直写，可引条文数值；③ 若 IBR，只可引「须符合某文件某版某页」，并按版本核对（FCC 7th ed.=2010 / 9th ed.=2014）；④ 二级引用链（如 §172.320 → FCC 页码 → NAS/NRC）须走到终点；⑤ 任何落在**不可逐字引用区**的内容一律停在「回原 PDF / 回原文件核对」。

IBR 的两种句式决定了能说什么。**半开放**（§172.185 的 `not less than 99.0 percent ... or an equivalent method`）给了一个可判下限，且保留等效方法空间，可引该数值。**整体外转**（§172.831 的 `meets the specifications of the Food Chemicals Codex, 7th ed. (2010), pp. 993-995, which is incorporated by reference`）条文不含数值，只可引文件页码。判错句式——把整体外转的条款「补」出数值，或把半开放的条款说成「全在外部」——都属越界。

外部依赖还有一个隐性风险：**测法/菌株/日期全外转**（§172.785 的噬菌体效价、滴度、LLO、TOC 测法）。这类条款只可照抄「方法名称 + 日期 + 出具方」与菌株编号，不转述其内部数值。

第三层是**效力栈**。Part 172 是联邦法规正文（最终规则、具法律约束力）；FDA 指南用 should、是建议层；CPGM/CP/IOM 是检查员视角、不创设企业义务。三者冲突时以法规正文为准，指南只作解释与例证。本件与全包其余来源合为**二十八类不可混引**，〔§ 172.xxx〕与其余七套编号并列，不得互引替代。

红线：本卡的输出是**引用纪律**，不是业务结论。它必须依附 V01–V04 业务卡——单独加载不产出可交付动作。任何「把 IBR 内部数值写成法规原文」「把指南 should 当法规依据」「把检查程序当企业义务」「跨编号互引」的做法，都是本卡要拦的错误。

## A1 — 案例用法

**情景一：规格句式判定（cases.md CAND-CS-15；〔§ 172.185〕〔§ 172.831〕）**
- 问题：QA 问「某添加剂纯度数值是多少」，需要区分能否直接给数。
- 动作：核 §172.185(b) 半开放 → 可引 `not less than 99.0 percent`；核 §172.831(b) 整体外转 → 只可引 FCC 7th ed. (2010) pp. 993-995。
- 判定/后果：前者给数值、后者给文件页码；把后者「补」出数值即编造法规。

**情景二：FCC 版次/页码核对（counter-examples.md CAND-CE-08；〔§ 172.185〕〔§ 172.831〕）**
- 问题：某报告引用「FCC 7th ed. (2014) pp. 744-746」。
- 动作：核 FCC 版次年份——**7th ed.=2010、9th ed.=2014**；核该页码是否真属该版。
- 判定/后果：版次与年份不匹配即引用错误；页码须回原文件核对。

**情景三：二级引用链须走到终点（cases.md CAND-CS-13；〔§ 172.320〕）**
- 问题：查某氨基酸纯度规格。
- 动作：按 (b)(1) 走到 FCC 具体页码（如 `L-Alanine, pages 28 and 29.`）；(b)(2) 走到 NAS/NRC Publication；两者内容均不可转述。
- 判定/后果：引用须落到「某文件某页」；链条任何一环缺失即无法核对。

**情景四：外部文件数值不可转述（counter-examples.md CAND-CE-13 与 CAND-CE-06；〔§ 172.785〕〔§ 172.831〕）**
- 问题：有人把噬菌体测法文件里的效价阈值、或 FCC 里的杂质限值直接写进结论。
- 动作：核 §172.785(b) 的 IBR 只允许引「方法名称 + 日期 + 出具方 + 菌株编号」；核转换件标注的不可逐字引用区。
- 判定/后果：转述即越界；正确做法是标注「须符合某文件某版本，数值回原文件核对」。

**情景五：效力栈与编号边界（counter-examples.md CAND-CE-01；〔§ 172.5(b)〕）**
- 问题：有人主张「FDA 指南说应该这样做，所以是法定义务」或「Part 117 条款可以覆盖 Part 172 判定」。
- 动作：核效力栈——指南 should 是建议层、CPGM/CP/IOM 不创设义务；核 §172.5(b) 许可不免除本法其他义务；核八套编号并列、不得互引替代。
- 判定/后果：指南不能当法规依据、检查程序不能当企业义务、跨编号不得互引；冲突时法规正文为准。

## A2 — 触发与执行

**触发 → 动作／分流（16 条）**
1. 触发：问「某纯度规格数值是多少」 → 动作／分流：先判直写 or IBR；IBR 只给文件页码。
2. 触发：问「IBR 文件里的数值能不能写进结论」 → 动作／分流：否，只可引「须符合某文件某版某页」。
3. 触发：问「FCC 版次页码对不对」 → 动作／分流：7th ed.=2010 / 9th ed.=2014；页码回原文件核对。
4. 触发：问「哪些内容不可逐字引用」 → 动作／分流：16 张重建表数值 / 名录内部行 / IBR 外部文件内容。
5. 触发：问「FDA 指南算不算法规依据」 → 动作／分流：否，should 建议层，不作法定依据。
6. 触发：问「CPGM/CP/IOM 是不是企业义务」 → 动作／分流：否，检查员视角、不创设企业义务。
7. 触发：问「Part 172 和 Part 117 条款能不能互引」 → 动作／分流：否，八套编号并列、不得互引替代。
8. 触发：问「满足纯度规格是不是就合规」 → 动作／分流：否，规格只是四元组一环（→V01）。
9. 触发：问「二级引用链怎么走」 → 动作／分流：走到终点（FCC 页码 / NAS-NRC / 厂商方法）；内容不可转述。
10. 触发：问「测法/菌株/日期在哪」 → 动作／分流：照抄方法名称 + 日期 + 出具方 + 菌株编号；数值不转述。
11. 触发：问「{某条款}是不是 incorporated by reference」 → 动作／分流：核实；给「是/否 + 引用对象 + 版本页码」。
12. 触发：问「效力栈怎么排」 → 动作／分流：法规正文（八套编号）＞ 指南（should）＞ 检查程序。
13. 触发：问「冲突时以谁为准」 → 动作／分流：法规正文为准；指南只作解释与例证。
14. 触发：问「本件是不是官方正式文本」 → 动作／分流：eCFR 快照，`authoritative but unofficial`；快照日期 ≠ 生效日。
15. 触发：问「某数值是不是 Decimal/版式脚注」 → 动作／分流：FR citation 是编纂注记、非独立条文。
16. 触发：问「转引未收的法源怎么办」 → 动作／分流：标「转引未收」，不据本 part 反推其内容。

## E — 边界与误读

**反场景**
- 用户要**业务结论**（某添加剂能否用/用量多少） → 回 **V01–V04**；本卡只给引用纪律。
- 用户要**代写法律文书、出具法律意见** → 不出，回专业审校。
- 用户要**具体 IBR 内部数值** → 本卡不给，标「回原文件核对」。

**高频误读**
- CE-06：符合 FCC 规格＝合规全部 → 否，只是一环。
- CE-08：IBR 数值可转述 → 否，越界。
- CE-13：重建表数值可直接引 → 否，回原 PDF。
- CE-01：有条款＝整体合规 → 否，§172.5(b)。

**来源与位阶边界**
- **eCFR 快照，非 GPO 正式文本**：自述 `authoritative but unofficial`；2026-11-05 是快照日期，条文末尾 FR citation 才是修订出处。
- **不可逐字引用区**：16 张重建表格数值（词级坐标启发式重建，跨页续表与 `Do.` 行有归属歧义）、§172.510/§172.515 名录内部行、全部 IBR 外部文件内容。
- **转引未收**：FD&C Act 全文、21 CFR Part 170/171/175–178/180、1 CFR part 51、FCC 各版正文、9 CFR 430.1、40 CFR 725.421(d)、AOAC/厂商方法正文、ATCC 菌株资料。
- **最强反对意见保留**：本件近三成条款把规格外转，意味着**本技能包对相当一部分物质的纯度只能给「去哪查」而非「是什么」**；不标注这一点而给出看似完整的规格结论，是本卡要防的最大失真。

## B — 判停

**何时停**
- 涉及 IBR 内部数值 → 停，标「不可逐字引用，回原文件核对」。
- 涉及表内数值 → 停，标「回原 PDF 核对」。
- 用户要业务结论 → 停，转 V01–V04。

**何时转**
- 业务判定 → **V01/V02/V03/V04**；标签内容 → **CAP-30**；过程控制 → **CAP-01～09**；检查程序与进口作业 → **CAP-27/CAP-29**。

**输出纪律**
- 任何规格结论须标「直写 or IBR + 文件版本页码」；不得给外部文件内部数值。
- **本卡不单独抢路由**，须依附业务卡；单独加载不产出可交付动作。
- 不代写文书、不出合规结论、不判法定身份。
