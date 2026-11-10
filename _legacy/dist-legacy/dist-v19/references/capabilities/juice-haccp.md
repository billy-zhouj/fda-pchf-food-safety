# 果汁 HACCP 体系（21 CFR Part 120 法规正文）（juice-haccp）

*来源分层：本卡取用**单套法规正文**——**21 CFR Part 120**〔§ 120.xxx〕（Hazard Analysis and Critical Control Point (HACCP) Systems，4-1-25 Edition，10 页 / 15 条款，书页 439–448）。它是**独立的 HACCP 体系法规**，不是「果汁版的 Part 117」，也不是 Part 117 的子集；与 Part 117 的关系由〔§ 120.5〕一句话锁定（Part 117 默认适用，〔§ 117.5(c)〕为唯一例外出口），而〔§ 117.5(c)〕的条文原话**自 v4.14 起已在包内**（`books/_inbox/21-CFR-Part-117-2025.md`，Part 117 全文 160,825 字节 / 3,577 行）。*

*⚠ **本卡补的是全包最后一处「成熟法规但只有转引」的缺口**：`seafood-haccp-statutory-requirements`（CAP-22）的 A2 第 22 条、`seafood-hazards-controls-guide`（CAP-23）头注、`lacf-statutory-requirements`（CAP-20）B10、`emergency-permit-control`（CAP-25）B10、`cgmp-compliance-guide`（CAP-15）未收清单、`reference-tools-discipline` 第 12 条，此前一律把 **part 120 正文**标为「转引未收」。自 v4.13 起改为正向引用〔§ 120.xxx〕。仍属「转引未收」的是：part 110 正文、CPG / Import Alert 全文、BAM 方法全文。⚠ **果汁检查程序（CP 7303.847）自 v4.15 起已收**，检查员取证口径见 CAP-27 `juice-inspection-program`——v4.13 曾把该程序号误写为 `7303.047`，正确号是 **7303.847**。⚠ v4.13 曾把〔§ 117.5(c)〕也列为「转引未收」——那是因为第二来源（Part 117 正文）在 metadata 里声明了却**从未随仓库分发**；v4.14 该文件已入库，全包 21 处〔§ 117.xxx〕引文经 `.cangjie/verify_v4_14_part117_quotes.py` 追溯核验 **21/21 命中**，此处不再标未收。*

*本卡定位：给**果汁 HACCP 的实体法定义务**——适用边界、危害分析、计划七要素、纠正措施、验证与确认、记录、培训、进口商义务，以及 Subpart B 的 **5-log** 与 **E. coli 专项验证**。不覆盖：检查员取证口径（CP 7303.847，自 v4.15 起已收，见 CAP-27）、F0/D/z 计算、BAM 检测方法全文、以及基于 GC/MS 的香气成分等质量指标。*

## R — 原文

**① 适用范围与原料排除（§120.1）**：

> "Any juice sold as such or used as an ingredient in beverages shall be processed in accordance with the requirements of this part."
> —— 〔§ 120.1(a)〕；`as an ingredient in beverages` 使**配料用途**也落入管辖

> "Raw agricultural ingredients of juice are not subject to the requirements of this part."
> —— 〔§ 120.1(a)〕；生鲜农原料（水果蔬菜本身）不在本 part 内——与〔§ 120.3(j)(2)〕的 `processing` 排除项配套

**② 三个定义决定判定链（§120.3）**：

> "Critical control point means a point, step, or procedure in a food process at which a control measure can be applied and at which control is essential to reduce an identified food hazard to an acceptable level."
> —— 〔§ 120.3(d)〕；`control is essential` 是必要条件，不是「可以控制的地方」

> "Food hazard means any biological, chemical, or physical agent that is reasonably likely to cause illness or injury in the absence of its control."
> —— 〔§ 120.3(g)〕；**`in the absence of its control`** 是无控制假设态，与 Part 117 的 hazard 定义同构

> "Validation means that element of verification focused on collecting and evaluating scientific and technical information to determine whether the HACCP plan, when properly implemented, will effectively control the identified food hazards."
> —— 〔§ 120.3(p)〕；validation ⊂ verification，两者不是并列关系

> "Verification means those activities, other than monitoring, that establish the validity of the HACCP plan and that the system is operating according to the plan."
> —— 〔§ 120.3(q)〕；`other than monitoring` 把监控从验证里切出去

**③ 与 Part 117 / Part 110 的唯一接口（§120.5）**：

> "Except as provided by § 117.5(c), parts 110 and 117 of this chapter apply in determining whether the facilities, methods, practices, and controls used to process juice are safe, and whether the food has been processed under sanitary conditions."
> —— 〔§ 120.5〕；**Part 117 是默认适用**，`Except as provided by § 117.5(c)` 是唯一例外出口，且是条件性的

**③b 该出口的条文原话（§117.5(c)，v4.14 起可逐字核对）**：

> "Subparts C and G of this part do not apply with respect to activities that are subject to part 120 of this chapter (Hazard Analysis and Critical Control Point (HACCP) Systems) at a facility if you are required to comply with, and are in compliance with, part 120 of this chapter with respect to such activities."
> —— 〔§ 117.5(c)〕；`required to comply with, and are in compliance with` 是**两个并列条件**——企业未遵守 Part 120 时豁免不成立

**③c 与 (d) 的关键差异：(c) 没有范围限缩款（逐字对照）**：

> "The exemption in paragraph (d)(1) of this section is applicable only with respect to the microbiological hazards that are regulated under part 113 of this chapter."
> —— 〔§ 117.5(d)(2)〕；(c) **没有**对应条款，故 part 120 活动范围内的 Subparts C/G 要求**全部**被豁免（含非微生物危害），但**仅限**受 part 120 管辖的 activities

**④ 危害分析（§120.7）**：

> "Each processor shall develop, or have developed for it, a written hazard analysis to determine whether there are food hazards that are reasonably likely to occur for each type of juice processed by that processor and to identify control measures that the processor can apply to control those hazards."
> —— 〔§ 120.7(a)〕；**每种果汁**一份，可代做但不可无书面

> "A food hazard that is reasonably likely to occur is one for which a prudent processor would establish controls because experience, illness data, scientific reports, or other information provide a basis to conclude that there is a reasonable possibility that, in the absence of those controls, the food hazard will occur in the particular type of product being processed."
> —— 〔§ 120.7(a)(2)〕；判定基准是 `prudent processor` + `reasonable possibility` + **特定产品**

> "HACCP plans for juice need not address the food hazards associated with microorganisms and microbial toxins that are controlled by the requirements of part 113 or part 114 of this chapter."
> —— 〔§ 120.7(e)〕；豁免**只到微生物与微生物毒素**，化学/物理/过敏原危害仍须控制

**⑤ HACCP 计划与法律定性（§120.8 / §120.9）**：

> "Each processor shall have and implement a written HACCP plan whenever a hazard analysis reveals one or more food hazards that are reasonably likely to occur during processing"
> —— 〔§ 120.8(a)〕；`have and implement` 是**两份义务**——有文件 + 在运行

> "shall render the juice products of that processor adulterated under section 402(a)(4) of the Federal Food, Drug, and Cosmetic Act."
> —— 〔§ 120.9〕；法条**直接给掺假定性**，不经「不符合 CGMP」中转

**⑥ 纠正措施（§120.10）**：

> "Segregate and hold the affected product, at least until the requirements of paragraphs (b)(2) and (b)(3) of this section are met"
> —— 〔§ 120.10(b)(1)〕；无适用计划时的第一步是**隔离扣留**，顺序不可颠倒

**⑦ 验证与确认的两个时限（§120.11）**：

> "This review shall occur within 1 week (7 days) of the day that the records are made"
> —— 〔§ 120.11(a)(1)(iv)(A)〕与〔(B)〕；**日历 7 天**，不是「7 个工作日」——与 Part 117 的记录复审口径不同

> "this validation shall occur at least once within 12 months after implementation and at least annually thereafter"
> —— 〔§ 120.11(b)〕；确认的**起算点**是「实施后」，不是「计划签署日」

**⑧ 记录保存的第六套口径（§120.12）**：

> "in the case of perishable or refrigerated juices, at least 1 year after the date that such products were prepared, and for, in the case of frozen, preserved, or shelf stable products, 2 years or the shelf life of the product, whichever is greater"
> —— 〔§ 120.12(d)(1)〕；**起算点是「产品制备日」**，且货架稳定类用 `whichever is greater`（2 年与货架期孰长）

> "if such records can be retrieved and provided onsite within 24 hours of request for official review"
> —— 〔§ 120.12(d)(2)〕；异地存放的**唯一条件**，且须在监测发生后 6 个月才允许异地

> "The trained individual need not be an employee of the processor."
> —— 〔§ 120.13(b)〕；受训者可外聘——与 Part 123 的培训条款同构

> "the product will appear to be adulterated and will be denied entry."
> —— 〔§ 120.14(d)〕；进口商无法提供等效保证时的法定后果

**⑨ 5-log 是法定要求（§120.24）**：

> "a 5 log (i.e., 105) reduction, for a period at least as long as the shelf life of the product when stored under normal and moderate abuse conditions, in the pertinent microorganism"
> —— 〔§ 120.24(a)〕；⚠ 原文上标在 PDF 文本层丢失，`105` 实为 `10⁵`，引用时须还原为「10 的 5 次方」并注明是文本层缺陷

> "the most resistant microorganism of public health significance that is likely to occur in the juice"
> —— 〔§ 120.24(a)〕；`pertinent microorganism` 的定义——**不是**泛指的「目标菌」，也不是沙门氏菌或大肠杆菌 O157

> "A juice processor using a single thermal processing step sufficient to achieve shelf-stability of the juice or a thermal concentration process that includes thermal treatment of all ingredients"
> —— 〔§ 120.24(a)(2)〕；第二处豁免，条件是热力工艺副本须进〔§ 120.7〕的书面危害分析

**⑩ E. coli 专项验证只针对果面处理（§120.25）**：

> "Each juice processor that relies on treatments that do not come into direct contact with all parts of the juice to achieve the requirements of § 120.24 shall analyze the finished product for biotype I Escherichia coli as follows"
> —— 〔§ 120.25〕；**适用对象是「处理未接触果汁全部部分」者**，不是所有果汁厂

> "One 20 milliliter (mL) sample (consisting of two 10 mL subsamples) for each 1,000 gallons of juice produced shall be sampled each production day."
> —— 〔§ 120.25(a)〕；取样单位是「每 1,000 加仑 / 每生产日」，子样取自**已可分销给消费者**的包装

> "not less than once every 5 working days"
> —— 〔§ 120.25(a)〕；日产量不足 1,000 加仑时的**最低频次**（注意这里用的是 `working days`）

> "If two samples in a series of seven tests are positive for E. coli, the control measures to attain the 5-log reduction standard shall be deemed to be inadequate"
> —— 〔§ 120.25(e)〕；`deemed to be inadequate` 是**法定视为**，不留给企业自行判断

## I — 自述

我管的是「**果汁企业到底被哪部法规管、必须做什么**」。在此之前，全包涉及果汁只能写「part 120 转引未收」——因为 `lacf-statutory-requirements`、`seafood-haccp-statutory-requirements` 都只是从〔§ 117.5(c)〕倒推出「果汁有同类豁免」，却拿不到条文本身。现在能直接给〔§ 120.xxx〕。

我最想钉死的是**四件事**：

1. **5-log 是法定要求，不是建议**。〔§ 120.24(a)〕的 `shall include ... a 5 log (i.e., 10⁵) reduction` 是 `shall`，而且要求覆盖**货架期**与**正常及中度滥用条件**。目标菌是 `pertinent microorganism` = 果汁中可能出现的**最耐热、具公共卫生意义**的微生物。凡答「FDA 建议 5-log」「目标是沙门氏菌」「做一次验证即可」都是错的。
2. **Part 117 默认适用，不要因为「有 Part 120」就整厂脱离 PCHF**。〔§ 120.5〕的 `Except as provided by § 117.5(c), parts 110 and 117 ... apply` 说明：受 Part 120 管辖只换出口，不换默认。而〔§ 117.5(c)〕的原文（v4.14 起可逐字核对）是两个**并列条件**：`if you are required to comply with, and are in compliance with, part 120` —— 企业不合规时豁免不成立。更关键的是它**没有 (d)(2) 那样的范围限缩**：part 120 管辖活动范围内的 Subparts C/G 要求全部被豁免（含非微生物危害），但豁免边界止于「受 part 120 管辖的 activities」——纯采收、运输、零售仍在 Part 117 内自判。
3. **两处豁免范围极窄，且豁免的对象不同**：〔§ 120.24(a)(1)(2)〕豁免的是 **5-log 这个工艺控制指标**；〔§ 120.7(e)〕豁免的是 **HACCP 计划中对「part 113/114 已控制的微生物与微生物毒素」危害的处理**。前者不减 Subpart A 义务，后者不减化学/物理/过敏原危害。把两处混成「受 113/114 管辖就不用做果汁 HACCP」是双重错误。
4. **文档时限是「日历 7 天」，不是「7 个工作日」**。〔§ 120.11(a)(1)(iv)(A)(B)〕写的是 `within 1 week (7 days)`；(C) 的校准与检验记录才放宽到 `within a reasonable time`。同时〔§ 120.25(a)〕里又出现 `working days`——**同一部法规里两种日并存，不可互换**。

第三件是**记录保存的第六套口径**：〔§ 120.12(d)(1)〕易腐/冷藏 ≥1 年、冷冻/保藏/货架稳定 2 年或货架期孰长，起算点是**产品制备日**。加上已有的〔§ 108.25(g)〕3 年、〔§ 108.35(h)〕1+2、〔§ 113.100(g)〕1+2、〔§ 114.100(e)〕3 年、〔§ 123.9(b)(1)〕1 年/2 年，全包现在有**六套记录期**，任何「一般保存 3 年」的笼统答法都不成立。

我拒绝四件事：把 5-log 说成建议层；把 §120.25 的 E. coli 检测说成所有果汁厂的常规出厂检验；用 (b)/(d) 的措辞替 (c) 编原话（现在有原文，直接引）；把六套记录期合并成一句话。

## A1 — 书中案例

**案例 1：客户问「我们做 NFC 橙汁，是走 Part 117 还是 Part 120？」**
两者都走，但层次不同。〔§ 120.5〕规定 `Except as provided by § 117.5(c), parts 110 and 117 of this chapter apply`——Part 117 是默认适用的 CGMP + PCHF 底座；Part 120 在此之上叠加果汁专属的 HACCP 体系（SSOP、危害分析、计划、纠正措施、验证、记录、培训）与 Subpart B 的 5-log。若企业满足〔§ 117.5(c)〕的**双条件**（`required to comply with, and are in compliance with, part 120`），可获得 Subparts C/G 的**条件性**豁免，且该款**没有 (d)(2) 式的微生物限缩**——part 120 活动范围内的要求全部移出 C/G；但 CGMP（Subpart B）仍在，且边界止于受 part 120 管辖的 activities。**正确答法是把「默认适用 + 条件性出口 + 果汁专项叠加」三层讲清**，而不是二选一。

**案例 2：厂里说「我们的 5-log 是照着 FDA 指南做的，不是硬性要求」。**
这是效力误判。〔§ 120.24(a)〕原文是 `shall include in their HACCP plans control measures that will consistently produce, at a minimum, a 5 log (i.e., 10⁵) reduction`，是 `shall`；且须覆盖**货架期**、在**正常与中度滥用条件**下成立。目标菌按同款定义为 `the most resistant microorganism of public health significance that is likely to occur in the juice`。所以「做了 5-log 验证」不够，还要证明**持续性**（consistently）与**货架期覆盖**。若该厂同时是 LACF 或酸化食品（受 part 113/114 管辖），才可能落入〔§ 120.24(a)(1)〕的豁免——但豁免的只是 5-log，不是整套 HACCP。

**案例 3：柑橘汁厂用果面处理（surface treatment）达成 5-log，问要不要做成品检测。**
要做，这是强制项而非可选项。〔§ 120.25〕的适用对象正是 `relies on treatments that do not come into direct contact with all parts of the juice`。取样为 **20 mL（两个 10 mL 子样）／每 1,000 加仑／每生产日**，子样须随机取自**已可分销给消费者**的包装；日产量不足 1,000 加仑时按每 1,000 加仑取、但**不少于每 5 个工作日一次**。检测项目是 **biotype I E. coli**。判读规则：**7 次检测中 2 次阳性 → 5-log 控制措施「被视为不足」**，须立即改用**压榨后**达成 5-log 的替代工艺，并复审监控记录、按 §120.10 纠正。注意反面：**不做果面处理、靠热力杀菌达成 5-log 的厂，本条不适用**，其成品/在制品检验在〔§ 120.11(a)(1)(iii)〕下是 `At the option of the processor`。

**案例 4：QA 问「记录到底保存几年」，同时提到冷藏果汁和冷冻浓缩汁。**
两档不同，且起算点特殊。〔§ 120.12(d)(1)〕：易腐或冷藏果汁 **≥1 年**；冷冻／保藏／货架稳定产品 **2 年或货架期，孰长**。两者起算点都是**产品制备日**（`after the date that such products were prepared`），不是记录形成日、不是出厂日。另〔§ 120.12(d)(2)〕：`(a)(1)` 与 `(a)(4)` 类记录在**监测发生后 6 个月**起可异地存放，条件是**请求官方审查后 24 小时内能调取并提供到现场**；符合 (g) 的电子记录可视同在场。把 Part 113 的「1+2 年」或 Part 114 的「整段 3 年」套到果汁上是错的。

**案例 5：进口商从巴西买冷冻橙汁，能不能只靠供应商的 HACCP 证书？**
不能只靠一张证书。〔§ 120.14(a)〕给的是**二选一**：从有现行有效 MOU 的国家采购，或建立并实施**书面验证程序**——后者至少含产品规格 + **至少一项 affirmative steps**（A 取得批次相关的 HACCP 计划与前提程序 SOP 记录；B 取得境外政府或合格第三方的**持续或逐批证书**；C 定期检查境外设施；D 存档**英文版**危害分析与 HACCP 计划 + 书面保证；E 定期检测 + 英文书面保证；F 其他等效措施）。进口商可聘**合格第三方**代办（含代写验证程序），但须保存**英文**记录证明执行与结果〔§ 120.14(c)〕。若拿不出等效保证，`the product will appear to be adulterated and will be denied entry`〔§ 120.14(d)〕。⚠ 这套义务是 Part 120 自带的，与 FSVP（21 CFR part 1 subpart L）是**两套并行**，不能互相替代。

## A2 — 未来触发

1. 用户问「果汁企业适用哪部法规」→ 本卡：Part 117 默认 + Part 120 专项叠加。
2. 用户问「果汁要不要做 HACCP」→ 〔§ 120.8(a)〕：危害分析显示合理可能发生的危害即须有并实施书面计划。
3. 用户问「5-log 是法定还是建议」→ 法定，〔§ 120.24(a)〕`shall ... consistently produce`。
4. 用户问「5-log 针对什么菌」→ `pertinent microorganism` = 最耐热、具公共卫生意义、可能出现在该果汁中的微生物〔§ 120.24(a)〕。
5. 用户问「5-log 要覆盖多久」→ 至少货架期，且须在正常与中度滥用条件下成立。
6. 用户问「哪些果汁厂可以不做 5-log」→ 〔§ 120.24(a)(1)〕受 part 113/114 管辖者；〔§ 120.24(a)(2)〕单次热力达货架稳定或含全部配料热处理的浓缩工艺（须把热力工艺副本放进危害分析）。
7. 用户问「做了 LACF 是不是就不用做果汁 HACCP」→ 不是，豁免的只是 5-log；〔§ 120.7(e)〕另只免「微生物与微生物毒素」类危害的计划处理。
8. 用户问「果汁 HACCP 要不要管过敏原」→ 要，〔§ 120.7(c)(8)〕把「可能致敏的未申报配料」列为应考虑项；〔§ 120.7(e)〕只免微生物类。
9. 用户问「危害分析要写多细」→ 〔§ 120.7(a)(1)–(5)〕五项 + (a)(2) 的 `prudent processor` 判定 + 严重性评估 + (c) 九项考虑。
10. 用户问「计划要包含什么」→ 〔§ 120.8(b)(1)–(7)〕七要素，含厂内/厂外两类 CCP 分列。
11. 用户问「多个产品能不能共用一份计划」→ 可分组，但须危害、CCP、关键限值、程序**本质相同**，且独有要素须在计划中清楚界定〔§ 120.8(a)(2)〕。
12. 用户问「偏离关键限值怎么办」→ 〔§ 120.10(a)〕有预设计划则按计划；无则〔§ 120.10(b)〕隔离扣留 → 评审 → 产品处置 → 纠正原因 → 及时验证。
13. 用户问「记录多久复审一次」→ 〔§ 120.11(a)(1)(iv)(A)(B)〕记录形成后 **1 周（7 天）**；校准与检验记录在合理时间内。
14. 用户问「7 个工作日还是 7 天」→ 果汁是**日历 7 天**，与 Part 117 的工作日口径不同，不可混用。
15. 用户问「HACCP 计划多久确认一次」→ 实施后 12 个月内至少一次，此后至少每年一次，或工艺变化时〔§ 120.11(b)〕。
16. 用户问「没有 HACCP 计划的企业要不要做确认」→ 要，〔§ 120.11(c)〕工艺变化时须重新评估危害分析充分性。
17. 用户问「记录保存几年」→ 易腐/冷藏 ≥1 年；冷冻/保藏/货架稳定 2 年或货架期孰长〔§ 120.12(d)(1)〕；起算点是产品制备日。
18. 用户问「记录能不能放总部」→ 〔§ 120.12(d)(2)〕监测后 6 个月起可异地，须 24 小时内可提供到现场。
19. 用户问「电子记录可以吗」→ 〔§ 120.12(g)〕按 part 11 维护的计算机化记录可接受。
20. 用户问「谁有资格做危害分析和记录复审」→ 〔§ 120.13(a)(1)–(4)〕四类职能 + (b) 标准化课程等效或岗位经验；可外聘。
21. 用户问「果汁进口商要做什么」→ 〔§ 120.14(a)〕MOU 或书面验证程序 + 至少一项 affirmative steps；英文记录；无保证则拒绝入境。
22. 用户问「FSVP 能不能替代 §120.14」→ 不能，两套并行。
23. 用户问「果面处理的 E. coli 检测怎么做」→ 〔§ 120.25(a)(c)〕20 mL（2×10 mL）/1,000 加仑/生产日；AOAC 992.30 modified 或等效方法。
24. 用户问「多久取一次」→ 每日；产量不足 1,000 加仑/日时不少于每 5 个工作日一次。
25. 用户问「几次阳性算失控」→ 〔§ 120.25(e)〕7 次中 2 次阳性即「视为不足」，须立即改用压榨后达成 5-log 的替代工艺。
26. 用户问「不合格产品能不能回流复配」→ 超本卡；须按 §120.10 处置并结合 FD&C Act §402 判定，不得据本文给复配结论。
27. 用户问「果汁的 CGMP 看哪一套」→ 〔§ 120.5〕Part 110 / Part 117 默认适用；〔§ 120.6〕另给 SSOP 八项。
28. 用户问「SSOP 要不要写进 HACCP 计划」→ 可不写，〔§ 120.6(d)〕按 §120.6 监测的部分不必纳入计划。
29. 用户问「违反 Part 120 的法律后果」→ 〔§ 120.9〕直接构成 FD&C Act 402(a)(4) 掺假。
30. 用户问「CP 7303.847 果汁检查程序查什么」→ **转 CAP-27 `juice-inspection-program`**（v4.15 起已收）；含检查优先级、三类样品分流（验证/有因/文档性）、ATTACHMENT A 采样量、铅与巴氏毒素触发值、60 天复检口径。
31. 用户问「果汁企业能不能免 Subparts C/G / 免到什么程度」→ 〔§ 117.5(c)〕：**双条件**（合规才成立）+ **无限缩款**（区别于 (d)(2) 的「仅限微生物」），故 part 120 活动范围内的 C/G 全部豁免，但纯采收/运输/零售不在内。
32. 用户问「§117.5(b)(c)(d) 是不是一回事」→ 结构同构、范围不同：(b) part 123 与 (c) part 120 **都无**范围限缩款，(d) part 113 有 (d)(2) 把豁免限定在微生物危害；三者条款号与 scope 各自独立，不得互套。

## E — 执行要点

**Step 1 — 先定「谁被管、管到哪一步」。** 用〔§ 120.1(a)〕判产品（`juice` 含浓缩物与果泥；作饮料配料也算），再用〔§ 120.3(j)(2)〕排除三项（不从事其他加工的采收/采摘/运输、零售经营），并用〔§ 120.3(l)〕判零售establishment（同时向其他企业销售的**不属**零售）。原料是生鲜农产品的，按〔§ 120.1(a)〕不在本 part 内。

**Step 2 — 画三层义务栈，不要写成一张清单。**

| 层 | 内容 | 法条 |
|---|---|---|
| 底座（默认适用） | CGMP + PCHF；出口仅〔§ 117.5(c)〕，**双条件且无限缩款** | 〔§ 120.5〕〔§ 117.5(c)〕（v4.14 起可逐字核对） |
| 果汁专项（Subpart A） | SSOP 八项〔§ 120.6〕、书面危害分析〔§ 120.7〕、HACCP 计划七要素〔§ 120.8〕、纠正措施〔§ 120.10〕、验证与确认〔§ 120.11〕、记录〔§ 120.12〕、培训〔§ 120.13〕、进口商〔§ 120.14〕 | 〔§ 120.xxx〕 |
| 专项增量（Subpart B） | 5-log〔§ 120.24〕；果面处理者的 E. coli 验证〔§ 120.25〕 | 〔§ 120.xxx〕 |

〔§ 120.20〕明写 Subpart B 是 `augments`（增量）而非替代——只答 Subpart B 而漏 Subpart A，即为漏项。

**Step 3 — 分清两处豁免的对象。** 〔§ 120.24(a)(1)(2)〕免的是 **5-log**；〔§ 120.7(e)〕免的是 **HACCP 计划中对 part 113/114 已控制的微生物与微生物毒素危害的处理**。两处都不减 Subpart A 的其他义务，也都不减化学/物理/过敏原危害的控制。答「受 113/114 管辖＝不用做果汁 HACCP」是双重错误。

**Step 4 — 时限与记录期逐条标口径，禁止概括。**

| 事项 | 口径 | 出处 |
|---|---|---|
| CCP 监控与纠正措施记录复审 | **1 周（7 日历天）** | 〔§ 120.11(a)(1)(iv)(A)(B)〕 |
| 校准与成品/在制品检验记录复审 | 合理时间内 | 〔§ 120.11(a)(1)(iv)(C)〕 |
| 计划确认 | 实施后 12 个月内 ≥1 次，此后 ≥每年 1 次 + 变化时 | 〔§ 120.11(b)〕 |
| 记录保存（易腐/冷藏） | ≥1 年，自**产品制备日** | 〔§ 120.12(d)(1)〕 |
| 记录保存（冷冻/保藏/货架稳定） | 2 年或货架期，**孰长** | 〔§ 120.12(d)(1)〕 |
| 异地存放 | 监测后 **6 个月**起，须 **24 小时**内到现场 | 〔§ 120.12(d)(2)〕 |
| E. coli 取样频次 | 每 1,000 加仑/生产日；不足 1,000 加仑时不少于每 **5 个工作日** | 〔§ 120.25(a)〕 |
| 7 次 2 阳性 | 视为控制措施不足，须立即改替代工艺 | 〔§ 120.25(e)〕 |

**Step 5 — 与其余五套法规正文（Part 108 / 113 / 114 / 117 / 123）交叉时，先判轨道再引条款。** LACF（Part 113）、酸化食品（Part 114）、海产品（Part 123）、紧急许可（Part 108）各有独立编号与独立豁免结构；果汁只是**又一轨**。交叉点只有三处：〔§ 120.24(a)(1)〕（113/114 管辖者免 5-log）、〔§ 120.7(e)〕（113/114 已控制的微生物与毒素危害免于计划处理）、〔§ 120.5〕（Part 117 默认适用）。

**Step 6 — 收尾声明。** 每条结论标〔§ 120.xxx〕（法条层）；检查员侧标「CP 7303.847 PART x / ATTACHMENT A」（v4.15 起已收，见 CAP-27）；part 110 正文、BAM 方法、CPG / Import Alert 全文一律标「转引未收」。⚠ `5 log (i.e., 105)` 是 PDF 文本层上标丢失，引用时须还原为 10⁵ 并注明。**全包自 v4.15 起十九类不可混引，当前为 27 张能力卡。**

## B — 边界

**B1 — 5-log 是法定要求，不是指南建议（本卡最容易被降格的一条）。** 〔§ 120.24(a)〕用 `shall include ... control measures that will consistently produce, at a minimum, a 5 log (i.e., 10⁵) reduction`，且要求 `for a period at least as long as the shelf life` 与 `under normal and moderate abuse conditions`。三个限定词都要在答案里出现：**持续（consistently）**、**货架期**、**正常与中度滥用**。只说「要做 5-log」是不完整的。

**B2 — 目标菌是 `pertinent microorganism`，不是「沙门氏菌」也不是「大肠杆菌 O157」。** 〔§ 120.24(a)〕定义为 `the most resistant microorganism of public health significance that is likely to occur in the juice`——**最耐热**、**具公共卫生意义**、**在该果汁中可能出现**，三个条件同时成立。果汁种类不同，目标菌可能不同；把某一种菌当成通用答案即为错答。注意 §120.25 里的 **biotype I E. coli** 是**果面处理专项验证的指示菌**，与 5-log 的 pertinent microorganism 不是同一个概念，不得互换。

**B3 — §120.25 只适用于果面处理者，不是通用出厂检验。** 适用条件是 `relies on treatments that do not come into direct contact with all parts of the juice`。靠热力杀菌达成 5-log 的厂，成品/在制品检验在〔§ 120.11(a)(1)(iii)〕下是 `At the option of the processor`。把 E. coli 检测写成「所有果汁厂的强制出厂检验」是超范围适用；反过来，把果面处理厂的检测写成「可选」则是漏掉强制项。

**B4 — Part 117 是默认适用；〔§ 117.5(c)〕是唯一出口，且是「双条件 + 无限缩」。** 〔§ 120.5〕的 `Except as provided by § 117.5(c), parts 110 and 117 ... apply` 定默认；〔§ 117.5(c)〕定出口，原文（v4.14 起在包内，`books/_inbox/21-CFR-Part-117-2025.md`）是 `if you are required to comply with, and are in compliance with, part 120 of this chapter with respect to such activities`——**两个并列条件**，不合规即豁免不成立，不得写成「果汁自动免 PCHF」。⚠ 与 (d) 的差异是实质性的：(d)(2) 把豁免限定在 part 113 管辖的**微生物危害**，(c) **没有**对应限缩款，所以 part 120 活动范围内 Subparts C/G 的全部要求（含非微生物危害）都被豁免——但边界止于「受 part 120 管辖的 activities」，纯采收/运输/零售不在内，仍回 Part 117 自判；且豁免不含 Part 117 Subpart B 的 CGMP（〔§ 120.5〕的 `parts 110 and 117 ... apply` 只在 (c) 范围内被替换）。不得把 (d)(2) 的「仅限微生物」口径套到 (c) 上，反之亦然。

**B5 — 两处豁免对象不同，不得合并。** 〔§ 120.24(a)(1)(2)〕免 **5-log 这一工艺控制指标**；〔§ 120.7(e)〕免 **HACCP 计划中对「part 113/114 已控制的微生物与微生物毒素危害」的处理**。前者的豁免对象是「一项控制要求」，后者是「一类危害的计划处理」；两者可以同时成立，也可以只成立其一。

**B6 — 记录期是第六套口径，不得与前五套合并。** 果汁：易腐/冷藏 ≥1 年、冷冻/保藏/货架稳定 2 年或货架期孰长，起算点产品制备日〔§ 120.12(d)(1)〕。此前已有〔§ 108.25(g)〕3 年、〔§ 108.35(h)〕1+2、〔§ 113.100(g)〕1+2、〔§ 114.100(e)〕3 年、〔§ 123.9(b)(1)〕1 年/2 年。任何「一般保存 3 年」或「都是 2 年」的概括都是错的。

**B7 — 文档时限两种日并存。** 〔§ 120.11(a)(1)(iv)(A)(B)〕是 `within 1 week (7 days)`（日历天）；〔§ 120.25(a)〕是 `every 5 working days`（工作日）。同一部 part 内两种口径并存，答复必须标明是哪种。

**B8 — §120.14 与 FSVP 是两套并行义务。** 〔§ 120.14〕是 Part 120 自带的进口商义务（MOU 或书面验证程序 + affirmative steps），法源是本 part；FSVP（21 CFR part 1 subpart L）是另一套，法源是 FD&C Act §805。进口果汁**可能同时**触发两者：§120.14 的验证程序不自动满足 FSVP，FSVP 的危害分析也不自动满足 §120.14。与 Part 123 的〔§ 123.12〕是同一结构，但**条款号与要求清单不同，不得互引**。

**B9 — 法律后果由法条直接给。** 〔§ 120.9〕：未建立并实施符合 §§120.6/120.7/120.8 的 HACCP 体系，或未按本 part 运行 → 产品**依 FD&C Act 402(a)(4) 构成掺假**。这与「不符合 CGMP 因而可能被认定掺假」的间接路径不同，不要绕道论证。

**B10 — 引用规范与未收清单。** 本卡标〔§ 120.xxx〕；Part 117 标〔§ 117.xxx〕（〔§ 117.5(c)〕原文 v4.14 起在包内，可逐字引）。⚠ part 110 正文未收、CPG 与 Import Alert 全文未收、BAM / AOAC 检测方法全文未收——凡涉这些内容一律标「转引未收」。果汁检查程序 CP **7303.847** 自 v4.15 起已收，检查员侧一律转 CAP-27。（v4.13 曾误写为 `7303.047`。）⚠ `5 log (i.e., 105)` 的 `105` 是 PDF 文本层上标丢失，引用须还原为 10⁵ 并注明。**十九类不可混引，当前 27 张能力卡。**
