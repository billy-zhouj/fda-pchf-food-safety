# v4-11 · CP 7303.842 误读与反例（14 条）

> 审阅范围：仅 `cp-7303-842-full.md`（下称 **CP**，1334 行；`Lxxx` 均指该转换产物的行号）与 `capability-index.md`（下称 **索引**，23 张能力卡；引用用卡 slug 或「索引第 N 行」）。
> 定位：CP 7303.842 是 FDA 给 field staff / OII / HFP 的**内部检查作业指导（Compliance Program Guidance Manual）**，不是法规正文、不是企业合规清单、不是 BAM 全文。企业法定义务在 21 CFR Part 123 与 Part 117 Subpart B（见 `seafood-haccp-statutory-requirements`）。
> 每条四要素：`错误说法` / `为什么错` / `正确口径` / `依据`。

---

## CE-01 把 CP 的检查动作当企业法定义务

- **错误说法**：「CP 7303.842 要求企业必须填 FDA 3501、按 Table 1 排产、配合全程 walk-through、把缺陷按 regulatory significance 降序写进 483、按 Table 2 安排整改——这些就是海产品加工者的法定义务。」
- **为什么错**：CP 自述主语是检查员。L142 说本程序「identifies the necessary training and skills **field staff must possess** to conduct inspections and provides instructions specific to the inspection of seafood importers, seafood processing facilities, and seafood products」；L155 目标是「through inspections ... **for compliance with** the requirements of FD&C Act and **its implementing regulations**」——检查是手段，被检查的合规依据是法规。L252「Inspections **must** be conducted by **trained food safety staff**」、L105「FDA and contracted **state inspectors** should complete these forms」主语全是检查方。真正的企业侧口径在 L276：「**Seafood processors are legally obligated to meet the requirements of part 123** if they meet the definition of a seafood processor」，且「the requirements for subparts C and G of part 117 **cannot replace** the requirements defined in part 123」。把 CP 动作直译成企业义务，等于把「检查员怎么做」偷换成「企业必须做什么」，还会漏掉真正的义务来源。
- **正确口径**：企业义务回 21 CFR Part 123（§123.6 危害分析与 HACCP 计划、§123.7 纠正措施、§123.8 验证、§123.9 记录、§123.10 培训、§123.11 卫生、§123.12 进口商验证）与 Part 117 Subpart B（CGMP）；CP 只描述 FDA 如何检查这些义务。FDA 3501/3502 是检查员的电子报表（L104–107），483 是检查员的观察文书（L285、L115），均非企业提交件。条款级判定走 `seafood-haccp-statutory-requirements`，危害分析判定链走 `seafood-hazards-controls-guide`。
- **依据**：CP L142、L155、L104–107、L115、L252、L276、L285；索引第 26 行（CAP-22「判断哪些问题超出本包（**CP 7303.842**…）」）；slug `seafood-haccp-statutory-requirements`、`investigator-authority-procedure`。

## CE-02 把 PART IV `Criteria for Regulatory Action` 阈值当法规限值或 BAM 方法全文

- **错误说法**：「PART IV 写了组胺 ≥500 ppm、吲哚 ≥25 µg/100 g、虾污物 6 个 subs 平均值等数值，所以这些就是法规限量；低于即合规、达到即自动违法。而且这节就是 BAM 海产品分析方法的全文。」
- **为什么错**：这些是 surveillance/audit 取样下的**内部执法建议阈值与分样规则**，CP 自己把「定罪名」外链到 CPG：L543–544「Based on analytical data, **refer to CPG Sec. 540.525**. As of the implementation date of the program, this CPG is **under revision**」；L588–589 虾/吲哚「refer to CPG Sec. 540.370」；L609–610 其他产品「refer to CPG Sec. 540.370」；L944–945 净重「Refer to CPG Sec 562.300」。L381–396 的污物阈值也自承「The above guidance **does not include all types of filth**」并要送 Center SME。L1057「**Significance must be determined on a case-by-case basis**」、L1058–1060 的 Major/Minor 定义、L982「Regulatory action **can be recommended** under 402(a)(4)」都表明是裁量性建议而非自动法定限值。天然毒素 action level 也被外链到指南正文（L873「FDA established action levels for natural toxins can be found in **Chapter 6 of the Seafood HACCP Guide**」）。同时 L347 明说本节只是「Use the **methods referenced** in the appropriate section of this Part」，方法正文是 BAM/AOAC/MPM 的外部转引，CP 未收录。
- **正确口径**：PART IV 的 `Criteria for Regulatory Action` = 检查/实验室判断**是否建议移送监管行动**的内部判据 + 取样量；法律定性依据 FD&C Act 402(a)(1)/(a)(3)/(a)(4)、21 CFR Part 123 与相应 CPG（540.525 / 540.370 / 562.300 / 555.600 等，见 L1105）。阈值不是「法规上限/合规下限」，低于阈值不等于合规，达到阈值也不等于自动定罪；方法正文须回 BAM / AOAC / MPM 原文。
- **依据**：CP L347、L381–396、L543–544、L588–589、L609–610、L873、L944–945、L982、L1057、L1105；slug `inspection-sampling`、`chemical-hazard-controls`、`defect-action-levels`、`investigator-authority-procedure`。

## CE-03 把 CP 7303.844 当现行独立程序

- **错误说法**：「进口海产品检查仍归 CP 7303.844（Imported Seafood Inspection Program），与 CP 7303.842 并行，进口商要分别对照两套程序。」
- **为什么错**：首页 NOTE 已明说合并。L7：「**NOTE: CP 7303.842 ... and CP 7303.844 ... have been combined into a single compliance program – CP 7303.842, Seafood Processor and Products Inspection Program.** PAC codes for sampling and analysis will still reflect whether the product is imported or domestic.」L142 复述：「The current ... CP 7303.842, is a **combination of the previous compliance programs**, the Seafood Processor Inspection Program (CP 7303.842) and the Imported Seafood Inspection Program (CP 7303.844).」7303.844 是「previous / 已合并」，不是现行独立程序；进口与国产的区别只保留在 PAC 码（03844* / 03842*，L12–25）与检查轨道（L32「03844H Importer HACCP Inspection」）上。
- **正确口径**：现行只有一份 CP 7303.842，覆盖国产与进口加工者/进口商。不要再引用 7303.844 作为独立现行程序，更不要把它当成另一套企业义务；需要区分进口/国产时看 PAC 前缀，不看程序号。
- **依据**：CP L7、L142、L12–25、L30–33；slug `seafood-haccp-statutory-requirements`（§123.12 进口商验证）、`fsvp-inspection-program`。

## CE-04 把 Table 1 / Table 2 的检查优先级当企业合规清单

- **错误说法**：「Table 1 把 ROP、未去脏鱼、生食贝类列为 HIGHER RISK，把冷冻/干藏仓列为 LOWER RISK——所以前者是重点合规项、后者基本可以不做 HACCP；Table 2 的 OAI→VAI→NAI 顺序就是企业整改优先级清单。」
- **为什么错**：两张表是 FDA 的**资源配置/工作计划工具**。L159「Table 1 **prioritizes in descending order** specific seafood commodities **for inspection** ... These should be used **as a guide when identifying the focus of a seafood HACCP inspection**」；L196「Table 2 is **for work planning purposes** and further builds upon the product risk ranking」；L197 直接给检查配额（「90% ... on higher risk importers / remaining 10% ... less than 100 entry line items」）；L199 谈 OAI 复检时机。L189 的「Lower regulatory priority hazards」定义为「unlikely to result in serious health consequences and where industry compliance with FDA's requirements is **consistently good**」——是监管优先级，不是「危害不存在/免于控制」。L186 也只说冷冻/干藏仓「A HACCP plan is **not normally needed** ... although **sanitation requirements must still be met**」，并非豁免。
- **正确口径**：Table 1/2 决定 FDA 先查谁、查什么、查多少，不产生、也不减免企业义务。企业是否需 HACCP 计划、哪些危害须列入，按 §123.6 与危害分析判定链（§123.6(c)(1) 九项考虑清单）判定；CGMP（Part 117 Subpart B）对所有海产品加工者一律适用。合规清单来自法规正文，不是风险排序表。
- **依据**：CP L151–159、L187–189、L191–206（L196、L197、L199）、L276、L311；slug `seafood-haccp-statutory-requirements`、`seafood-hazards-controls-guide`、`inspection-readiness`。

## CE-05 把 PART IV 实验室方法当 BAM 海产品章节全文

- **错误说法**：「PART IV 的 METHODOLOGY 已经把 BAM 海产品章节全文收进来了，照 CP 做即可，不必查 BAM 原文。」
- **为什么错**：CP 里出现的是**指向性引用 + CP 自己的取样/制样/合成规则**，不是 BAM 全文。L446 只给「BAM on line Chapter 19 ... **page 19.04 - 19.05**」；L617 给的是 BAM 网址；L625、L631–634、L666、L672、L700、L715–717、L739、L788 都是「BAM, Chapter X」式指针。更关键的是 CP 会**覆盖** BAM 步骤：L728–729「THE FOLLOWING INSTRUCTIONS ARE TO BE USED **IN LIEU OF** CHAPTER 28, Section C」；L655–660 规定李斯特「analyze **two (2) composites per samples**」并按 6/10 subs 取 83.3 g / 50 g；L770 给出 CP 自有的 WPS/亚硝酸盐判据（「for the microbiological safety analysis, 10 subsamples are to be each analyzed individually」「100 ppm in smoked fish」）；L823–824、L837–839、L843、L848、L851 则混用 AOAC 与「accepted/approved by NSSP」的方法状态。L347「Use the **methods referenced**」与 L353–354（化疗药、化学污染物另回 7304.018 / 7304.004 / 7304.019）已把边界写清。
- **正确口径**：PART IV = 本检查程序的分析判据、取样/合成/制样规则 + 对 BAM / AOAC / MPM / NSSP 方法的**转引清单**；BAM 章节正文、AOAC 全文、MPM 全文均未收录（属「外部方法转引未收层」）。具体培养、分离、确证步骤须回 BAM 原文；遇到与 BAM 冲突的 CP 指令（APW 裂解液、composite 规则）以 CP 的「in lieu of」为准并标注层级。
- **依据**：CP L347、L353–354、L446、L617、L625、L631–634、L655–660、L672、L700、L715–717、L728–734、L739、L770、L788、L823–824、L837–839、L843、L848、L851；slug `inspection-sampling`、`seafood-hazards-controls-guide`（「标识导出件表格…Appendix 3 残表为不可逐字引用区」的分层纪律）。

## CE-06 把 CP 7303.842 与 CP 7303.878（FSVP 进口商检查，明确不取样）混用

- **错误说法**：「进口商检查就是 FSVP 检查，按 CP 7303.878 走，PART IV 是空的、不取样；反过来 CP 7303.842 的进口商检查也可以照搬 FSVP 的『不取样 / 无 PART IV』结论。」
- **为什么错**：两套程序的法源、主体、动作都不同。本 CP 的进口商检查是 **21 CFR 123.12** 的海产品 HACCP 进口商验证：L311「Under the seafood HACCP Regulation, **21 CFR 123.12**, importers are required to verify that foreign processors are in compliance ...」，配套 L32「03844H **Importer HACCP Inspection**」、L310–315（书面验证程序、产品规格、affirmative steps 取证）、L323–324（affirmative step inadequacy / FDA 3502），并给出 §123.12 特有的 MOU 替代路径（「Products from countries that currently have a food safety MOU with FDA should be excluded」）。而且 CP 7303.842 **明确会取样**：L329–337「Imported Seafood Surveillance Sampling」、整个 PART IV、L325–340 的取样与 documentary samples。反过来，索引 CAP-21 (`fsvp-inspection-program`) 明确「FSVP 检查**不取样、PART IV 全空**」「Samples will not be collected」「Intentionally Left Blank」，法源为 FD&C Act §805 / 21 CFR part 1 subpart L；CAP-22 亦强调「§123.12 进口商验证与 FSVP 是**两套法源两套结构**，deemed compliance **不覆盖** §123.12」。
- **正确口径**：海产品进口商 HACCP 验证 → CP 7303.842 + §123.12（会取样、有 PART IV、有 FDA 3502）；FSVP 进口商 → CP 7303.878 + 21 CFR part 1 subpart L（不取样、PART IV 空白）。两者不可互相套用取样量、观察项或执法路径；同一进口商可能同时受两套要求约束，须分别判定。
- **依据**：CP L32、L104–106、L310–315、L323–324、L325–340、L311；索引第 21、25、26 行；slug `fsvp-inspection-program`、`seafood-haccp-statutory-requirements`、`inspection-sampling`。

## CE-07 把 Warning Letter / DWPE 阈值当自动触发（须经裁量与 Center 一致）

- **错误说法**：「只要 Table 4 判为 Major、或样品达到 PART IV 的 action 数值、或 foreign processor 缺陷未改正，就自动发 Warning Letter / 自动 DWPE / 自动扣押，企业无需再走程序。」
- **为什么错**：CP 用的全是**裁量 + 上报 + Center 一致**措辞。L1074「Warning Letters **should be considered** for significant deviations ...」；L1077「Foreign processors **may** be subject to detention without physical examination if deviations ... are **not corrected**. Requests for release ... **should be forwarded to HFP OCE for concurrence**」；L1084「Recommendations for legal actions **must be submitted to HFP OCE for evaluation and concurrence**」「forwarded to the **Center's** compliance unit in FACTS ... via **CMS**」；L1092「should submit a case via CMS to **DIOP** ... **DIOP and HFP OCE OE will confer** on DWPE recommendations」；L91 限定「inspections that were **classified as OAI** and for which the **Division is recommending action**」才经 CMS 提交；L466 要求争议/返工提案「confer with, or ... **submit the owners' submissions to the Center** for consideration」；L1057「Significance must be determined on a **case-by-case basis**」。索引 CAP-21 亦记「direct reference authority 只在有限情形授予、其余案件须经 CMS 送 Center 并取得分类一致」。
- **正确口径**：任何执法动作都是「Division 建议 → CMS/FACTS 报送 → HFP OCE / Center 评估并取得 concurrence / 分类一致 → 才可能采取」。Table 4 排名、PART IV 数值只是「是否建议移送」的输入，不是自动触发器；direct reference 只在有限情形授权。DWPE 移除/放行同样须 HFP OCE concurrence 且提交英文证据（L1077）。
- **依据**：CP L91、L466、L1057、L1074、L1077、L1084、L1085、L1092、L1100–1104；slug `fsvp-inspection-program`、`investigator-authority-procedure`、`inspection-readiness`。

## CE-08 把 PAC 码当产品分类或危害分类

- **错误说法**：「03842A/03844C/07842/21842 这些 PAC 就是海产品的产品类别码或危害类别码，按 PAC 就能判断产品属于哪一类、有哪些危害。」
- **为什么错**：PAC/PAF 是**FACTS 数据上报与 OII 工作量归属码**。L10–11「PRODUCT/ASSIGNMENT CODES ... **REPORT COLLECTIONS AND ANALYSIS USING**」；L26「**REPORT INSPECTIONS** under the following PACs」；L34「additional PAC codes **for Reporting Purposes**」；L44「FIELD REPORTING REQUIREMENTS」；L52「Report the following analytical results into the **FACTS Data System**」；L7 明说「PAC codes for sampling and analysis will **still reflect whether the product is imported or domestic**」（03844*=进口 / 03842*=国产，L12–25）。L30「03842 Documentary samples or seafood inspection activities that are **not part of the HACCP assessment**」、L31「03842H **Processor HACCP Inspection**」、L33「03040 **PC training and training records requirements**」、L339「documentary samples ... are **NOT** to use the PACs (those ending in 'H') reserved for HACCP verification samples **nor ... count towards division Workplan obligations**」、L968–971（21842 食品欺诈 / 21005 NLEA / 21R829 营养欺诈 / PAF FDF→FDE）。可见 PAC 随「分析项目 + 进口/国产 + 是否为 HACCP 验证 + 报表用途」变化，与产品/危害分类无关。
- **正确口径**：产品分类用首页的「INDUSTRY CODE 16, USE APPLICABLE CLASS, SUBCLASS, PIC, AND GROUP PRODUCT CODES」（L7）与 Seafood List / 成品市场形态；危害分类用《Fish and Fishery Products Hazards and Controls Guidance》Ch.3（Table 3-2/3-3/3-4，见 L159、L334、L939、L1210）与 §123.6 危害分析。PAC/PAF 只用于填报 FACTS、OII workplan、CMS 移送，不得反推危害清单或合规义务。
- **依据**：CP L7、L10–42、L44、L50–72、L91–103、L339、L968–971、L1210；slug `inspection-readiness`、`inspection-sampling`、`seafood-hazards-controls-guide`。

## CE-09 Import Alert 16-74 与 99-41 / 99-37 / 99-38 混淆

- **错误说法**：「Import Alert 16-74 就是 FSVP 的 99-41（或 LACF/AF 的 99-37/99-38），都是『未列 Green List 就 DWPE』的同一张警报，可以互相套用 Red/Green List 规则。」
- **为什么错**：对象、法源、程序完全不同。16-74 是**本 CP 的海产品专项**：L170 指向「Import Alert **16-74**」；L637「Import Alert 16-74 **prohibits entries of salt-cured, and/or air-dried, un-eviscerated fish** ... from processors that are not included on the **Green list**」；L1227–1231「Import Alert 16-74, Uneviscerated Finfish ... main concern is **C. botulinum toxin formation** ... **does not apply to fresh or frozen uneviscerated raw fish**」且「a single instance ... is sufficient to detain the entry and add the processor to the **Red List for IA 16-74**」。本 CP 还另有 16-125（ROP，L165）、16-20（河豚，L865）。而 99-41 属 FSVP、99-37/99-38 属 LACF/AF：索引 CAP-21「区分 Import Alert **99-41（FSVP）** 与 **99-37 / 99-38（LACF/AF）**，说明 Red List 按『食品 + 供应商』组合列入与移除流程」；CAP-19「解释 Import Alert 99-37/99-38 与『不得仅因未注册未备案建议 DWPE』的反直觉限制」。把 16-74 当成 99-41 会误套「FSVP 主体 / 食品+供应商组合 / 不取样」；当成 99-37/99-38 会误套 LACF 注册备案逻辑。
- **正确口径**：16-74 = 海产品未去脏/部分去脏加工鱼（盐渍、干制、熏制、腌渍、发酵），风险为 C. botulinum，按「processor 是否在 Green List」扣留，归 CP 7303.842；99-41 = FSVP，归 CP 7303.878；99-37/99-38 = LACF/AF 未注册未备案/FCE-SID，归 CP 7303.070。三者警报号、列入/移除条件、适用产品、配套检查程序均不可互换。
- **依据**：CP L165、L170、L637、L865、L1227–1231；索引第 23 行（CAP-19）、第 25 行（CAP-21）；slug `fsvp-inspection-program`、`lacf-inspection-program`、`seafood-haccp-statutory-requirements`。

## CE-10 把物种替换（FD&C Act 403(b) misbranding）当 HACCP 危害

- **错误说法**：「物种替换/错标是海产品 HACCP 的一种显著危害，必须作为 §123.6 危害写进 HACCP 计划并设 CCP。」
- **为什么错**：CP 把物种替换定性为**标签/掺假违法**，明确排除在 Part 123 之外。L1087–1090「**Species misbranding is a violation of the Act [section 403(b) of the FD&C Act or 21 U.S.C. 343(b)]**」「Specimen charge: The article is **misbranded** ... in that it is **offered for sale under the name of another food**」；L1070「VIOLATIONS OF REGULATIONS **OTHER THAN 21 CFR 123** ... These include **misbranding, economically motivated adulteration**, non-scombrotoxin decomposition, non-safety related GMP violations」；L114–115 要求把 misbranding 证据写进 483 与 Species Substitution Questionnaire；L936–939、L971 把它归到 Project 21 / PAC 21842 / PAF FDF→FDE（食品欺诈与经济欺骗）。CP 只说替换**可能引入**额外安全危害：L297「Food fraud in the form of species substitution and misbranding **can introduce additional safety concerns**. Some species of fish are associated with significant food safety hazards such as **marine toxins, allergens, and scombrotoxin** which require specific controls」；L939「... **should** be consulted **if misbranding ... results in exposure to additional hazards** is suspected」。需进危害分析的是「被错标物种带来的毒素/过敏原/组胺暴露」，不是「替换」行为本身。
- **正确口径**：物种替换的法律定性是 FD&C Act §403(b) misbranding（21 U.S.C. 343(b)），走标签/食品欺诈/掺假轨道（CP 7321.005、Project 21、PAC 21842、CPG 540.475/540.750 等，见 L1113–1115）。它不自动成为 §123.6 的 significant hazard；只有当替换导致消费者暴露于物种相关危害时，才按《Guide》Ch.3 与 `seafood-hazards-controls-guide` 的 18 步判定链评估是否 reasonably likely to occur、是否列入 HACCP 计划。市场名称归 Seafood List，不归 HACCP 计划。
- **依据**：CP L114–115、L295–297、L936–939、L947–955、L968–971、L1070、L1087–1092、L1113–1115；slug `seafood-hazards-controls-guide`、`chemical-hazard-controls`、`seafood-haccp-statutory-requirements`。

## CE-11 把 NSSP 检查当 FDA 单独法规体系

- **错误说法**：「生食贝类走 NSSP，是 FDA 之外另一套独立法规体系，企业按 NSSP Model Ordinance 履行义务即可，与 21 CFR Part 123 无关。」
- **为什么错**：CP 把 NSSP 定位为**州/联邦合作计划与检查执行框架**，且反复强调检查依据仍是海产品 HACCP 法规。L215–217：CP 7318.004「covers the **evaluation of state, tribal and foreign shellfish programs and related technical assistance only**」，而「CP 7303.842 **provides instructions to food safety staff (i.e., State inspectors in participating States)** for conducting inspections of establishments and for the collection and analyzing of samples **under the NSSP**. State inspectors should follow and implement the requirements and guidance included in the **Model Ordinance**」。L307–309 要求 NSSP 检查由 shellfish standardized inspector 用 ISSC Form 93-01(A)、按 NSSP Model Ordinance 进行。关键在 L233–238：「**The inspections must be based on the Seafood HACCP regulation and FDA recommendations as opposed to local state requirements**」——联邦法定依据仍是 21 CFR Part 123（双壳贝类源头控制 §123.28）。L171 表 1 注（「FDA State contract inspections **should not cover** raw molluscan shellfish in States participating in the NSSP」）是资源/管辖分工，不是另立法规。L823、L837–838、L843、L848、L851 的「accepted/approved by NSSP」说明 NSSP 是方法认可与州际互认体系（ISSC / ICSSL，L217、L309），不是 FDA 单独颁布的法规。索引 CAP-22 把 NSSP 列入「超出本包」，CAP-23 亦标注 NSSP Guide 为外部转引。
- **正确口径**：NSSP = National Shellfish Sanitation Program，由 ISSC / Model Ordinance / 州 shellfish control authority 运作的州际合作与互认体系；FDA 端通过 CP 7318.004（计划评估）与 CP 7303.842（州合同检查员作业指导）接入。企业联邦义务仍来自 21 CFR Part 123 §123.28（approved growing waters、shellstock tag、shucked 标签）与 Part 117 Subpart B；Model Ordinance 是州/合作层要求，不得当作 FDA 单独法规体系，也不得替代 Part 123。
- **依据**：CP L171、L215–217、L233–238、L307–309、L823、L837–838、L843、L848、L851、L873；索引第 26 行（CAP-22「超出本包…NSSP…」）、第 27 行（CAP-23）；slug `seafood-haccp-statutory-requirements`、`seafood-hazards-controls-guide`。

## CE-12 把 Table 4 违规分级当 §123.6 的 significant hazard 判定

- **错误说法**：「Table 4 把『Hazard(s) not listed in the plan / 123.6(c)(1)』标成 Major、把『Hazard analysis not conducted / 123.6(a)』标成 Minor，所以 Major 就是 significant hazard、Minor 就不是显著危害；按 Table 4 就能做 §123.6 的危害显著性判定。」
- **为什么错**：两个「significance」同形异义。Table 4 的标题与说明写的是**违规/缺陷的监管显著性**：L977、L987「Table 4, Seafood HACCP **Enforcement Strategy: Ranking of violation**, provides information for determining the **significance of violations of Part 123**」；L983–986「may assist you in **prioritizing seafood HACCP cases for potential regulatory action**」；L1058–1060 定义 Major/Minor 是「if left uncorrected, could **jeopardize the integrity of the HACCP system** / significantly increase food safety risk」——评的是**检查发现的缺陷**，不是危害本身；L1057「Significance must be determined on a **case-by-case basis**」也指违规显著性。而 §123.6 的 significant hazard / reasonably likely to occur 是**危害分析**判断：在无控制条件下按审慎加工者标准逐步骤评估，走 Ch.3 表、Hazard Analysis Worksheet 六栏、Column 3 / Column 6 剪枝闸门（索引 CAP-23），条款级义务在 CAP-22 的 §123.6(c)(1)(i)–(ix)。两者一为 PART V 执法排序、一为 §123.6 计划设计，层面与判据都不同。
- **正确口径**：Table 4 = 检查员对「已发现的 Part 123 违规」做 Major/Minor 监管显著性排序，用于决定是否建议监管行动（配合 CE-07 的裁量/Center 一致），不产生也不替代危害分析结论。某危害是否 significant / 是否须进 HACCP 计划，按 §123.6 与 `seafood-hazards-controls-guide` 的判定链判定；条款级认定回 `seafood-haccp-statutory-requirements`。
- **依据**：CP L977、L983–987、L991–1056、L1057、L1058–1060；索引第 26 行（CAP-22 §123.6(c)(1)）、第 27 行（CAP-23「reasonably likely to occur / significant hazard / Column 3、Column 6 两道剪枝闸门」「区分显著危害判定与 CCP 定位」）；slug `seafood-haccp-statutory-requirements`、`seafood-hazards-controls-guide`。

## CE-13 版本误读（文件名 `20250929` / `09/30/025` / 实施日与更正日）

- **错误说法**：「文件名带 `20250929`，且首页写 `Date of Issuance: 09/30/025`，所以这是一份 2025 年 9 月 30 日新签发/新修订的程序（新规）；或反过来把 09/30/025 当成 2005/0025 年的某次旧签发。」
- **为什么错**：`20250929` 是转换/生成日戳，不是程序签发日，也不代表 2025 年出了新规（索引第 23 行 CAP-19 把 `20250929` 与「2024-09-26 签发 / 2025-09-26 更正本的版本形态」并列，正是提醒别把生成日当版本依据）。首页 L8「Date of Issuance: **09/30/025**」是 **PDF 转录形态**：`025` 缺了 `2`，实为 `09/30/2025`，恰与 L6 的「**Correction date: 09/30/2025**」对应，是更正日期被转录进了首页 issuance 栏，并非另一次签发。权威版本标识是 L6「**IMPLEMENTATION DATE 11/01/2023** / Correction date: 09/30/2025」，并由 L1182、L1191、L1201「Date of Issuance: **11/1/2023**」以及 L1213、L1224、L1247、L1260、L1270、L1282、L1295 的页眉「**November 1, 2023**」自洽印证；L544「**As of the implementation date of the program**, this CPG is under revision」也以 implementation date 为准。索引多处给出同类纪律：第 21 行 CAP-17「识别 2022 签发 / 2025-09-10 更正的版本形态，避免套用 7303.040 的 Transmittal 口径」；第 24 行 CAP-20、第 26 行 CAP-22「识别 **4-1-25 Edition 是 CFR 年度编纂版次而非 2025 新规**」。
- **正确口径**：本程序 = **IMPLEMENTATION DATE 11/01/2023**（签发/实施，页眉 Date of Issuance 11/1/2023）+ **Correction date 09/30/2025**（更正，首页 `09/30/025` 为其转录残缺形态）。文件名 `20250929` 仅为产物生成日，既非签发日也非「2025 新规」；引用版本时写「11/01/2023 实施 / 09/30/2025 更正」，不要写「2025-09-30 签发」，也不要把 4-1-25 Edition 当新规。
- **依据**：CP L6、L8、L544、L1182、L1191、L1201、L1213、L1247、L1295；索引第 21、23、24、26 行；slug `lacf-inspection-program`、`lacf-statutory-requirements`、`inspection-sampling`、`fsvp-inspection-program`。

## CE-14 与 CAP-23 的 Ch.3 勾选表、CAP-22 的 `shall` 法定义务混引

- **错误说法**：「CP 多处让检查员『refer to Chapter 3』，所以《Guide》Ch.3 的 Table 3-2/3-3/3-4 勾选结果就是法定危害清单；反过来，既然指南是非强制的，Part 123 的 `shall` 义务也可以按 CP/指南口径酌情报『可选』。三层文件可以互相代替引用。」
- **为什么错**：CP、指南、法规是三个不同效力层，CP 自己也只用 `should` 引 Ch.3。L159「Food safety staff **should** refer to Chapter 3 of the ... Guide ... to identify **potential** species and process related hazard for products that do not fall into the categories listed」；L334「**should** refer to ... Chapter 3 ... to identify associated hazards of concern」；L495「**consult** the ... Guidance, Chapter 3, Table 3-2」；L939「Chapter 3 ... **should** be consulted **if** misbranding ... results in exposure to additional hazards is suspected」。这些都是检查员识别**潜在**危害的线索，不是义务。索引 CAP-23 明确：「判断 **Ch.3 三张表能否单独用于 reasonably likely to occur 判定**并给出正确用法」「纠正**把指南当法规、把 should 读成 shall** 的误读；**纠正因指南非强制而把 Part 123 法定义务稀释成可选的反向误读**」「给每条输出标注**法定层、指南建议层或外部法源转引未收层**标签」「分流法定义务、法定时限与条款级判定至 **CAP-22** 与〔§ 123.xxx〕」；CAP-22 则逐条列 `shall` 义务并区分「§123.11(a) SSOP 的 **should** 与 (b)(c) 监测记录的 **shall**」。CP 侧也守住这条线：L276「the requirements for subparts C and G of part 117 **cannot replace** the requirements defined in part 123 ... **legally obligated** to meet the requirements of part 123」。
- **正确口径**：三层分开标注、不可互套——① **CP 7303.842**（本卡）：给 field staff 的检查/取样/上报作业指导，`should`/`consult` 为建议；② **《Guide》第 4 版 / CAP-23** (`seafood-hazards-controls-guide`)：技术指南建议层，Ch.3 表只用于列潜在危害，须经 18 步判定链、无控制条件下审慎加工者标准、Column 3 / Column 6 剪枝闸门才能得显著性结论；③ **21 CFR Part 123 / CAP-22** (`seafood-haccp-statutory-requirements`)：法条义务层 `shall`，危害分析、HACCP 计划、纠正措施、验证、记录、培训、卫生、进口商验证的条款级判定与法定时限均回此层，并叠加 Part 117 Subpart B CGMP。凡「条款级判定 / 是否违法 / 法定时限」一律转 CAP-22 + 〔§ 123.xxx〕；凡「Ch.3 勾选表 / reasonably likely to occur / CCP 定位」转 CAP-23；凡「CP 检查动作 / PAC / 取样量 / 执法排序」留在本卡并标注为内部作业指导层。
- **依据**：CP L159、L276、L334、L495、L939、L1057、L1210；索引第 26 行（CAP-22）、第 27 行（CAP-23「十五类不可混引、转引未收、指南建议层、法条义务层」）；slug `seafood-haccp-statutory-requirements`、`seafood-hazards-controls-guide`。

---

## `also_read` 建议

> 新卡定位 = CP 7303.842 的「误读/反例层」：它**不承载法条义务、不承载指南判定链、不承载其它 CP 的取样细则**。因此与下列 9 张卡都是**双向辅读**关系——既「新卡须被某卡辅读以取正确口径」，也「某卡须被新卡辅读以挡回误读」。按相关度排序。

1. **`seafood-haccp-statutory-requirements`**（CAP-22，法条层，最核心）
   - 新卡 ← 它：CE-01/04/10/12/14 凡落到「企业有没有法定义务、§123.6 是否显著危害、`shall` 还是 `should`、法定时限」都必须辅读本卡取条款级口径；本卡不写法条结论。
   - 它 ← 新卡：CAP-22 自述「判断哪些问题超出本包（**CP 7303.842**…）」；读者在其处遇到「检查怎么查 / PAC / FDA 483 / Table 4 排名 / PART IV 数值 / Import Alert 16-74」时须辅读新卡，避免把内部作业指导当法规正文（CE-01、CE-12）。

2. **`seafood-hazards-controls-guide`**（CAP-23，指南层）
   - 新卡 ← 它：CE-05/10/12/14 涉及 Ch.3 勾选表、reasonably likely to occur、50/500 ppm、物种替换引入危害、附录数值能否作关键限值时，须辅读本卡取「指南建议层」判定链与三层标签。
   - 它 ← 新卡：CAP-23「拒绝代写 HACCP 计划、不判法定身份与不出合规结论」「分流取样至 inspection-sampling」「十五类不可混引、转引未收」；读者在其处遇到「CP 检查动作 / PAC / Warning Letter / DWPE / Import Alert」时须辅读新卡，尤其 CE-12（Table 4 不是 significant hazard 判定）与 CE-14（三层不可互套）。

3. **`inspection-sampling`**（CAP-17，CP 7303.050 取样）
   - 新卡 ← 它：CE-02/05/06 的样品量、subs、composite、702(b) 留样、PAF/PAC 需辅读本卡，辨清「CP 7303.050 的样品量与环境拭子」与「CP 7303.842 的 surveillance 取样」是两套、不能互套。
   - 它 ← 新卡：CAP-17 覆盖 7303.050 并声明「eBAM/AOAC/MPM 方法正文…超出本包」；读者在其处遇到海产品专项（03842/03844 PAC、组胺/吲哚/天然毒素 subs、Import Alert 16-74、Table A-1/A-2）时须辅读新卡 CE-05、CE-09。

4. **`fsvp-inspection-program`**（CAP-21，CP 7303.878）
   - 新卡 ← 它：CE-06/07/09 的「FSVP 不取样、PART IV 空白」「Import Alert 99-41」「direct reference 须经 CMS 送 Center 一致」须辅读本卡取 FSVP 侧口径。
   - 它 ← 新卡：CAP-21 把「**7303.842**」列为并列路由并要求「区分 99-41 与 99-37/99-38」；读者在其处遇到「海产品进口商 §123.12 验证 / 16-74 / 会取样的进口商 HACCP 检查」时须辅读新卡 CE-06、CE-09，避免反向套用 FSVP 的「不取样」结论。

5. **`lacf-inspection-program`**（CAP-19，CP 7303.070）
   - 新卡 ← 它：CE-04/09/13 的 ROP 与 Part 113/114 分工、99-37/99-38、`20250929` 生成日 / 4-1-25 Edition 版本形态，须辅读本卡取 LACF 侧口径。
   - 它 ← 新卡：CAP-19 明说「海产品 **7303.842 HACCP 的并行路由**」；读者在其处遇到「Table 1 已把 subject to Part 113/114 的 ROP 排除」「CP 7303.842 与 7303.070 的资源/管辖分工」「16-74 不是 99-37/99-38」时须辅读新卡 CE-04、CE-09。

6. **`inspection-readiness`**（CAP-16，CPGM 7303.040 迎检）
   - 新卡 ← 它：CE-01/04/07/08 的 PAC、FDA 483、EIR、OAI/VAI/NAI、eNSpect、记录举证、Direct Reference Authority 须辅读本卡取 PCHF 迎检通用骨架与效力分层。
   - 它 ← 新卡：CAP-16 覆盖 03040* 检查类型并声明「抽样方法、警告信答复、进口扣留应诉…超出本包」；读者在其处遇到海产品专项 PAC（03842H/03844H/03842/03844）、FDA 3501/3502、§123.12 进口商验证时须辅读新卡。

7. **`investigator-authority-procedure`**（CAP-18，IOM / 检查员权限）
   - 新卡 ← 它：CE-01/07 的「CP 是给 field staff 的内部作业指导」「483 措辞纪律、证据链、CMS/Center concurrence」须辅读本卡取 IOM/704(a)(1) 法理——「guidance 不是可直接开观察项的法定义务」正是 CE-01 的依据。
   - 它 ← 新卡：CAP-18「用 IOM 5.5.11.3 反证本包九类来源的效力分层」；读者在其处遇到「海产品检查的 483 观察项 / 拒绝入场 / 进口商记录索取」时须辅读新卡，辨清 CP 作业指导与法规义务的分界。

8. **`chemical-hazard-controls`**（CAP-06，组胺/化学危害限值）
   - 新卡 ← 它：CE-02/10 的组胺 50 ppm 分解指示 / 500 ppm 毒性水平、天然毒素 action level、defect 与掺假分界、物种替换引入的海洋毒素/过敏原/鲭鱼毒素危害，须辅读本卡取化学/组胺限值口径（CAP-23 亦明确「分流组胺与化学危害限值至 chemical-hazard-controls」）。
   - 它 ← 新卡：本卡处理「行动水平/进口警报等监管标准变化」；读者在其处遇到「CP PART IV 的 surveillance 阈值 / CPG 540.525、540.370 / Import Alert 16-74」时须辅读新卡 CE-02、CE-09，避免把检查判据当法规限量。

9. **`defect-action-levels`**（CAP-15，缺陷行动水平效力层）
   - 新卡 ← 它：CE-02 的污物/分解阈值「是不是法规上限 / 低于阈值是否即合规」正是本卡核心纪律；CP L381–396 的虾污物阈值、L1105 的 CPG 555.600/555.650 清单须辅读本卡拆解。
   - 它 ← 新卡：CAP-15 处理 21 CFR 117.110 与掺混稀释/reconditioning；读者在其处遇到「海产品 surveillance 污物/分解取样（6 subs、12/18/24 subs）、CPG 540.370、PAC 03842B/03844B」时须辅读新卡，辨清「CP 检查判据」与「defect action level」两套阈值体系。

> 其余 14 张卡（CAP-01～CAP-14：危害分析方法、管理组件、工艺验证、环境病原、过敏原、供应链、召回、豁免边界、参考表纪律、豁免撤销、环境工程、人员卫生、cGMP 分诊等）与本卡仅间接相关，本轮**不列入** `also_read`——避免把 Part 117 PCHF 体系的判定链与海产品 HACCP 体系互套（呼应 CE-14 与 CAP-23「两套判定体系不可互套」）。
