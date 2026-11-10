# 阶段 1 候选池 — 术语提取器（v4.10 / 第 15 类来源）

- **源文档**：`C:/Users/周至/AppData/Local/Temp/seafood_guide.md` — FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版（June 2022）导出全文。实测 `wc -l` 为 31,322 行（任务描述为 31,321 行，差 1 行疑为末行换行计数差异）；**本文件所有依据行号一律以该 md 实际回读结果为准**。
- **产出时间**：2026-11-06
- **阶段 / 角色**：cangjie-skill 阶段 1 / glossary-extractor（检索式取块 + 脚本预筛），只读分析 + 写候选池。
- **既有库**：`fda-pchf-food-safety/candidates/glossary.md` 共 172 条（t1–t172，v4.9 十四类）。本轮追加 **t173–t182 共 10 条**，来自第 15 类来源，用于支撑「完整危害分析判定链」新卡。
- **本轮产出约束**：候选池 ≥12 条（实际 15 条），YAML 草案终选 10 条；只写本文件，不修改包内其它任何文件。
- **引用纪律**：英文原句一律用 `> ` 引用块，每段 ≤100 词，只取散文段落并标行号；表格、页码、页眉、章节标题、项目符号列表、步骤列表**不作逐字引用**，仅在中文里转述。原文弯引号 “ ” 为 U+201C/U+201D，非 ASCII 双引号。
- **判定链主线**：`should`（效力分层）→ 危害识别（species / process）→ 显著性判定（reasonably likely to occur / significant hazard）→ Worksheet 六栏落表 → 控制策略与 CCP 定位 → critical limit 与监控四问 → 书面化期望。

---

## T-01 should

- **依据行号**：L100–108（术语级定义）；辅助 L115–126、L129–135、L1507、L1534–1540（全文 should 用法）
- **作者本人的定义/用法**：指南在开篇把 `should` 当成一个**术语级的强制程度标记**单独定义：凡 Agency guidance 正文里的 should 一律读作「建议 / 推荐、非强制」；只有明确转引法规或法条（如 21 CFR 123.6）时才产生法定义务。这与 L115–126「控制策略与做法只是推荐，除非被法规或法令要求」以及 L1507「不要求使用附录 1 表格」相互印证。

〔L100–104〕
> FDA's guidance documents, including this guidance, do not establish legally enforceable responsibilities. Instead, guidance describes the Agency's current thinking on a topic and should be viewed only as recommendations, unless specific regulatory or statutory requirements are cited.


〔L105–108〕
> The use of the word “should” in Agency guidance means that something is suggested or recommended, but not required.

- **与常识或 PCHF 语境的差异**：常识里 should 只是礼貌或建议语气，无精确法律含义；PCHF（21 CFR Part 117）语境中没有对 should 的术语级定义，读 Part 117 相关指南时不能把本定义反向套用为「Part 117 也在定义 should」。最易错点：把「you should record the reason in Column 4」「FDA expects a written hazard analysis」误升格为法定义务——§123.6 只强制 hazard analysis 与 HACCP plan 本身，表单、书面化、限值示例都是 should 层。判定链上「强制 / 建议」必须分层，否则整张卡的效力标注会全错。
- **建议 id**：t173
- **建议 tags**：[指南自定义, 效力层级, 高频误读, 判定链]

---

## T-02 hazard analysis vs HACCP plan

- **依据行号**：L1500–1516、L1517–1540（重点 L1503–1506、L1534–1540）；法规正文转载 L29810–29834
- **作者本人的定义/用法**：作者把两者拆成**两个法定动作且书面化义务不对称**：(1) 存在显著危害时必须有并实施书面 HACCP plan（§123.6(b)）；(2) 所有加工者必须「进行或委托进行」hazard analysis（§123.6(a)）；(3) 但危害分析本身**不要求以书面形式保存**，书面化只是 FDA 的期望（expects），理由是便于强制复审、以及应对监管质询时举证某危害为何被纳入或未纳入计划。另 L1507 明确法规不要求使用附录 1 的标准化表格。

〔L1503–1506〕
> requires that you prepare a HACCP plan for fish and fishery products that you process if there are significant food safety hazards associated with the products.


〔L1520–1527〕
> The Seafood HACCP Regulation requires that all seafood processors conduct, or have conducted for them, a hazard analysis to determine whether there are food safety hazards that are reasonably likely to occur in their product and to the preventive measures that a processor can apply to control those hazards (21 CFR 123.6(a)).


〔L1534–1540〕
> The Seafood HACCP Regulation does not require that the hazard analysis be kept in writing. However, FDA expects that a written hazard analysis will be useful when you perform mandatory HACCP plan reassessments and when you are asked by regulators to justify why certain hazards were or were not included in your HACCP plan.

- **与常识或 PCHF 语境的差异**：常识把「危害分析」与「HACCP 计划」当作同一份文件；作者明确是两份东西，且 plan 必须书面、analysis 不必须。PCHF 语境（§117.130 / §117.135）里 hazard analysis 是**书面**义务并须由 PCQI 复核，若把 Part 117 的惯性套到 Part 123，就会凭空造出一个本指南明文否定的义务。反过来，「FDA expects」也不是可忽略的套话：它是复审与 483 举证时的实际证据标准，属于「非强制但事实上必须有」的软义务，恰好卡在 should 层。
- **建议 id**：t174
- **建议 tags**：[法定定义, 指南自定义, 判定链, 高频误读]

---

## T-03 species-related hazard vs process-related hazard

- **依据行号**：L1678–1694（Step 7 散文定义）、L2104–2124（Ch.3 引言与 Table 3-2 / 3-3 / 3-4 归类）、L1705–1708（Column 2 落表）
- **作者本人的定义/用法**：分类轴是**危害被引入的地点 / 环节**，不是危害的种类。在厂区外、收获前 / 中 / 后随原料带来的称 species-related hazard（查 Table 3-2 脊椎动物、Table 3-3 无脊椎动物）；在厂区环境内、由加工方式带来的称 process-related hazard。Ch.3 的 Table 3-4 定义落在项目符号列表里，仅转述：该类危害由**成品形态（finished product form）、包装类型（package type）、储运方式（method of distribution and storage）**三者决定（L2118–2124）。L1705–1708 要求把查表所得潜在物种相关危害写入 Worksheet 第 2 栏，且「at every processing step」——每一个加工步骤都要记。

〔L1678–1687〕
> Biological, chemical, and physical hazards can affect the safety of fishery products. Some food safety hazards are associated with the product (e.g., the species of fish, the way in which the fish is raised or caught, and the region of the world from which the fish originates). These hazards are introduced outside the processing plant environment before, during, or after harvest. This guidance refers to these as “species-related hazards.”


〔L1687–1694〕
> Other food safety hazards are associated with the way in which the product is processed (e.g., the type of packaging, the manufacturing steps, and the kind of storage). These hazards are introduced within the processing plant environment. This guidance refers to these as “process-related hazards.” They are covered in Step 8.

- **与常识或 PCHF 语境的差异**：常识按「生物 / 化学 / 物理」给危害分类，作者改用「来源位置」分类——一个 species-related 危害本身仍可能是生物或化学的（组胺、寄生虫、天然毒素皆是）。「process-related」极易被误读成「某道工序操作失误」，其定义实际锚定成品形态 + 包装 + 储运，是产品与流通设计的结果（例如真空包装带来的肉毒梭菌风险）。PCHF（§117.130）按「与本设施或本食品相关联」识别 known or reasonably foreseeable hazard，不设 species / process 二分；本二分是 Seafood HACCP 指南特有的查表入口，不能与 Part 117 的危害识别清单互推。
- **建议 id**：t175
- **建议 tags**：[指南自定义, 危害层级, 判定链, 易混术语]

---

## T-04 reasonably likely to occur

- **依据行号**：L1780–1789（指南转引 21 CFR 123.6(a)）、L29819–29827（Appendix 转载 §123.6(a) 法规正文）、L129–135（表格用途限制）
- **作者本人的定义/用法**：定义含三个不可拆的限定：① 判定主体是 **prudent processor**（假想的审慎加工者）；② 证据基础是 experience / illness data / scientific reports / other information 四类信息；③ 判定基准状态是 **in the absence of those controls**——在「撤掉这些控制措施」的前提下评估发生的合理可能性，而不是评估现有控制下的残余风险。L129–135 另限定 Ch.3 与 Ch.4–21 表格只是用来判断 ordinary circumstances 下哪些危害 reasonably likely to occur，且 the tables should not be used separately for this purpose——不能单靠表格下结论，须结合各章与自身 / 外部专家知识。

〔L1780–1789〕
> The Seafood HACCP Regulation defines a food safety hazard that is reasonably likely to occur as “one for which a prudent processor would establish controls because experience, illness data, scientific reports, or other information provide a basis to conclude that there is a reasonable possibility that it will occur in the particular type of fish or fishery product being processed in the absence of those controls.”

- **与常识或 PCHF 语境的差异**：常识把 reasonably likely 读成概率阈值（如「超过 50%」）；作者给的是「一个审慎加工者会不会据此设控制」的**规范性 / 行为标准**，不是统计判断。最关键的反直觉点是判定发生在「无控制假设态」：若按 PCHF 习惯在「已有预防控制有效」的前提下评估显著性，会把本应判显著的危害错判为不显著，从而整条 CCP / 关键限值链被跳过。PCHF 对应概念是 known or reasonably foreseeable hazard 与 hazard requiring a preventive control（§117.130(a)(2)），措辞、证据要求与「无控制假设态」均不同，不可互引。
- **建议 id**：t176
- **建议 tags**：[法定定义, 判定链, 核心概念, 高频误读]

---

## T-05 significant hazard

- **依据行号**：L1774–1779（Step 10）、L1823–1827、L1813–1822（Column 3 / 4）
- **作者本人的定义/用法**：作者用 in other words 把 significant hazard **直接等价于** reasonably likely to occur，是 Step 10 对第 2 栏潜在危害清单做收敛后的输出：第 3 栏答 Yes / No、第 4 栏写理由，且第 3 栏答 No 的步骤可跳过 Steps 11–18。同时特别强调「某步骤判显著 ≠ 必须在该步骤控制」，控制点位置由 Step 11 另定。

〔L1776–1779〕
> Narrow the list of potential hazards that you entered in Column 2 of the Hazard Analysis Worksheet to those that are significant or, in other words, “reasonably likely to occur.”


〔L1823–1827〕
> It is important to note that identifying a hazard as significant at a processing step does not mean that it must be controlled at that processing step. Step 11 will help you determine where in the process the critical control point is located.

- **与常识或 PCHF 语境的差异**：常识里 significant 指危害的严重程度 / 后果大小；这里与严重性无关，纯粹是「是否进入 HACCP 控制链」的**二分开关**，等价于发生可能性判断。potential hazard（第 2 栏）与 significant hazard（第 3 栏 Yes）是两级，不可混同——把查表得到的「潜在危害」直接当成「必须设 CCP 的显著危害」是最常见误读。PCHF 用 hazard requiring a preventive control 表达类似开关，但 Part 117 允许用 prerequisite program、卫生控制、供应链控制等管理，不必落到 CCP；本指南的显著危害则最终必须至少落到一个 CCP（见 T-08）。
- **建议 id**：t177
- **建议 tags**：[法定定义, 判定链, 核心概念, 高频误读]

---

## T-06 Hazard Analysis Worksheet（六栏）

- **依据行号**：L1673–1675（Col 1）、L1705–1708（Col 2）、L1813–1822（Col 3 / 4）、L1848–1851（Col 5）、L1863–1870（Col 6）；表单说明 L1517–1533、L1876–1884
- **作者本人的定义/用法**：六栏映射为 **Col 1 加工步骤 → Col 2 潜在危害 → Col 3 是否显著 → Col 4 判定理由 → Col 5 预防措施 / 控制策略 → Col 6 是否 CCP**。Step 6–11 全在这张表上完成，Step 12 再把 Col 6 为 Yes 的步骤搬进 HACCP Plan Form（L1876–1884）。L1517–1533 说明该表为两页、附录 1 有空白表；法规不要求使用该表（L1507）。表内自带剪枝规则：Col 3 答 No 可跳过 Steps 11–18，Col 6 答 No 可跳过 Steps 12–18。

〔L1705–1708〕
> Determine whether the species has a potential species-related hazard by looking for a “√” mark (or one- or three-letter codes for a natural toxin) in the right-hand columns of the table. If it does, record the potential species-related hazard(s) in Column 2 of the Hazard Analysis Worksheet, at every processing step.


〔L1813–1822〕
> If you determine that a potential hazard is significant at a processing step, you should answer “Yes” in Column 3 of the Hazard Analysis Worksheet. If you determine that a potential hazard is not significant at a processing step, you should answer “No” in that column. You should record the reason for your “Yes” or “No” answer in Column 4. You need not complete Steps 11 through 18 for a hazard for those processing steps where you have recorded a “No.”


〔L1848–1851〕
> The control strategies contain preventive measure information. Record the preventive measure(s) in Column 5 of the Hazard Analysis Worksheet for each “Yes” answer in Column 3.


〔L1863–1870〕
> If you determine that a processing step is a CCP for a significant hazard, you should enter “Yes” in Column 6 of the Hazard Analysis Worksheet. If you determine that a processing step is not a CCP for a significant hazard, you should enter “No” in that column. You need not complete Steps 12 through 18 for a hazard for those processing steps where you have recorded a “No.”

- **与常识或 PCHF 语境的差异**：常识把「工作表」当成可选记录模板；在判定链里它是「显著性判定 + CCP 判定」的**发生地**，Col 4 的理由是后续复审与监管质询的唯一举证位（呼应 T-02 的 FDA expects）。「每一步都记 Col 2」与常识「只记关键工序」相反。PCHF 的危害分析表单（Form 2-B 等）按危害 / 工序列 preventive control，**不设「是否 CCP」栏**；把 Part 117 表单习惯套过来会漏掉 Col 6 这个通往 HACCP Plan Form 的接口。
- **建议 id**：t178
- **建议 tags**：[指南自定义, 判定链, 表单结构, 核心概念]

---

## T-07 control strategy example

- **依据行号**：L1837–1847（Step 11）、L1897–1902（Step 13 各章 Set Critical Limits 分节）、L1939–1945（Step 14 各章 Establish Monitoring Procedures 分节）
- **作者本人的定义/用法**：Ch.4–7、9、11–21 每章对同一危害给出一条或多条「控制策略示例」，每条示例自带 Identify CCPs / Set Critical Limits / Establish Monitoring Procedures 等分节。作者刻意用 **example** 而非 requirement：控制同一危害往往不止一种方式，选哪条策略决定 CCP 落在哪个加工步骤，也决定关键限值与监控参数。

〔L1842–1847〕
> Each chapter discusses one or more “control strategy example(s)” for how the hazard can be controlled, because there are often more ways than one to control a hazard. CCP(s) for one control strategy example often differ from those of another example for the same hazard.

- **与常识或 PCHF 语境的差异**：常识把「控制措施」当成针对危害的固定答案；作者明确同一危害存在多种合法控制路径，**CCP 位置随所选策略而变，因此 CCP 不是危害的固有属性**。这与 PCHF 的 preventive control 组合思路接近，但 Part 117 不要求把控制收敛到「至少一个 CCP」；本指南里策略选择的后果直接体现在 Worksheet Col 5 / 6 与 HACCP Plan Form Col 1–3。误读风险是把某一章的示例限值当成法定限值抄进计划，忽略 L121–126「选用其他控制策略（含其他关键限值）须科学论证其充分性」（见 T-09）。
- **建议 id**：t179
- **建议 tags**：[指南自定义, 判定链, 控制策略, 高频误读]

---

## T-08 critical control point (CCP)

- **依据行号**：L1828–1836（Step 11 与 CCP 判定树）、L1852–1862（至少一个 CCP / 21 CFR 123.6(c)(2) / 123.3(b)）、L1863–1870（Col 6）
- **作者本人的定义/用法**：CCP 被定义为「流程中的点，即加工步骤」，不是设备、不是参数。每个显著危害**至少有一个** CCP（法定下限，不是恰好一个）；一个危害可跨多个 CCP，一个加工步骤可同时是多个危害的 CCP；控制效果须达到 prevent / eliminate / reduce to an acceptable level 三档之一。判定工具是 Appendix 3 的 Figure A-2 CCP decision tree（L1833–1836）。

〔L1852–1859〕
> For every significant hazard, there must be at least one CCP where the hazard is controlled (21 CFR 123.6(c)(2)). In some cases, control may be necessary at more than one CCP for a single hazard. In other cases, a processing step may be a CCP for more than one hazard. CCPs are points in the process (i.e., processing steps) where the HACCP control activities will occur.


〔L1860–1862〕
> Control activities at a CCP can effectively prevent, eliminate, or reduce the hazard to an acceptable level (21 CFR 123.3(b)).

- **与常识或 PCHF 语境的差异**：常识把 CCP 理解为「最关键的那台设备 / 那个温度点」；作者定义为流程中的**步骤**，且「至少一个」是下限而非唯一解。与 T-05 联动：显著的步骤不等于 CCP 所在的步骤（L1823–1827），这正是 Step 11 独立存在的原因。PCHF（Part 117 Subpart C）刻意不用 CCP 作核心范畴，改用 process preventive control + 参数监控 + 纠偏 / 验证 / 确认；把 §117 的 process control 直接称作 CCP，或把 §123.6(c)(2) 的「至少一个 CCP」套到 Part 117 计划上，都是跨框架误引。
- **建议 id**：t180
- **建议 tags**：[法定定义, 判定链, 核心概念, 易混术语]

---

## T-09 critical limit（含替代限值的科学论证）

- **依据行号**：L121–126（选用其他策略 / 限值须科学论证）、L1605–1607（步骤列表，不逐字引用）、L1891–1902（Step 13 定义）、L1903–1920（松紧后果与 operating limit）、L1921–1933（须对应被监控参数）
- **作者本人的定义/用法**：critical limit 是「为控制危害，某工艺参数必须被控制到的最大或最小值」（L1891–1896）。作者附加四条用法：① 限值须直接对应将被监控的参数（L1921–1931，例如监控水浴温度与传送带速度就把这两项写成限值，而不是写产品中心温度）；② 过严会在并无安全问题时触发纠正措施，过松会放行不安全品；③ 可另设更严的 operating limit 以便在偏离关键限值前调整（L1911–1920）；④ **不采用本指南示例限值时，加工者须科学论证其充分性**（L121–126）。

〔L121–126〕
> Processors may choose to use other control strategies, as long as they comply with the requirements of the applicable food safety laws and regulations. However, processors that chose to use other control strategies (e.g., critical limits) should scientifically establish their adequacy.


〔L1891–1896〕
> For each processing step where a significant hazard is identified on the HACCP Plan Form, identify the maximum or minimum value to which a parameter of the process must be controlled in order to control the hazard.


〔L1903–1910〕
> You should set a critical limit at such a value that if it is not met, the safety of the product may be questionable. If you set a more restrictive critical limit, you could, as a result, be required to take corrective action when no safety concern actually exists. On the other hand, if you set a critical limit that is too loose, you could, as a result, allow an unsafe product to reach the consumer.

- **与常识或 PCHF 语境的差异**：常识把关键限值当成 FDA 规定的固定数字；本指南的数字来自各章 control strategy example（**示例**），可替换，但替换必须自带科学论证，且该论证动作本身只是 should，法规义务落点是「符合适用食品安全法律法规」。「限值必须对应被监控参数」反直觉：产品中心温度这种真正的安全指标反而不能写，因为无法连续监控，要写可连续监控的替代参数。PCHF 有 parameter 与 min / max 值、有 validation / verification 体系，但没有 §123 这套「critical limit / operating limit / CL 偏离即必须纠偏」的硬绑定；Part 117 的偏离走 correction / corrective action，不必预设 CL 偏离即纠偏。
- **建议 id**：t181
- **建议 tags**：[指南自定义, 判定链, 控制策略, 高频误读]

---

## T-10 HACCP Plan Form 监控四问（What / How / Frequency / Who）

- **依据行号**：L1605–1611（步骤列表 What / How / Frequency / Who，不逐字引用）、L1934–1950（Step 14 四问散文）、L1951–1979（频率原理与 Col 4–7）、L1875–1884（Step 12 建表）
- **作者本人的定义/用法**：四问是监控程序的**完整描述框架**，分别落入 HACCP Plan Form 第 4 / 5 / 6 / 7 栏；第 1–3 栏由 Step 12–13 填入 CCP 步骤、危害、关键限值。作者另给出频率判定原理：监控须直接测量已设限值的参数（L1951–1954）、连续监控 always desirable 但非必需、频率取决于正常波动与测量值贴近限值的程度、连续监控的纸 / 电子记录须至少每日复核（L1954–1976）。

〔L1934–1939〕
> For each processing step where a significant hazard is identified on the HACCP Plan Form, describe monitoring procedures that will ensure that critical limits are consistently met (21 CFR 123.6(c)(4)).


〔L1946–1950〕
> To fully describe your monitoring program, you should answer four questions: (1) What will be monitored? (2) How will monitoring be done? (3) How often will monitoring be done (frequency)? and (4) Who will do the monitoring?


〔L1977–1979〕
> Enter the “What,” “How,” “Frequency,” and “Who” monitoring information in Columns 4, 5, 6, and 7, respectively, of the HACCP Plan Form.

- **与常识或 PCHF 语境的差异**：常识里「监控」只等于「测什么 / 多久测一次」；作者把 How（方法）与 Who（责任人）列为与 What / Frequency 同等的必答项，缺一即程序不完整。「监控参数必须与关键限值同参数」（呼应 T-09）意味着不能监控一个量却为另一个量设限值。PCHF（§117.145 / §117.150）把 monitoring 与 corrective action、verification、validation 并列为预防控制的管理组件，并要求 PCQI oversight；本指南的 Who 只要求谁执行监控，未引入 PCQI 概念——跨框架套用会凭空加人。
- **建议 id**：t182
- **建议 tags**：[法定定义, 判定链, 表单结构, 监控]

---

## T-11 prudent processor

- **依据行号**：L1780–1789（定义内出现）、L29821（Appendix 转载法规正文）、L13100（Ch.12 另一处一般性用法）
- **作者本人的定义/用法**：prudent processor 是 §123.6(a) 定义里的**假想判定主体**：显著性不取决于「本厂实际会不会设控制」，而取决于「一个掌握同等经验 / 疾病数据 / 科学报告的审慎加工者会不会设」。全文仅此定义性出现（另 L13100 在 Ch.12 语境下作一般表述），无独立术语条目。

〔L1780–1789〕
> The Seafood HACCP Regulation defines a food safety hazard that is reasonably likely to occur as “one for which a prudent processor would establish controls because experience, illness data, scientific reports, or other information provide a basis to conclude that there is a reasonable possibility that it will occur in the particular type of fish or fishery product being processed in the absence of those controls.”

- **与常识或 PCHF 语境的差异**：常识把 prudent 当普通形容词修饰；这里它是一个**客观化标尺**，用来排除「本厂没出过事所以不显著」的主观抗辩。PCHF 的 §117.130 由掌握食品安全知识的 PCQI（具体持证人员）承担判断，主体不是假想理性人；两者不可等同。语义已被 t176（reasonably likely to occur）完整吸收，故列为备选不单独立条。
- **建议 id**：t183（本轮备选，不纳入 YAML 草案；语义已并入 t176）
- **建议 tags**：[法定定义, 判定链, 备选]

---

## T-12 scombroid toxin-forming species / histamine

- **依据行号**：L6474–6514（Ch.7 UNDERSTAND THE POTENTIAL HAZARD）、L6555–6581、L27547（Appendix 5 Table A-5，表格只描述不逐字引用）
- **作者本人的定义/用法**：作者用法要点：① 病名坚持用 **scombrotoxin poisoning**，明确弃用 scombroid poisoning / histamine poisoning，理由是致病鱼种已超出 Scombridae / Scomberesocidae，且除组胺外还有腐胺、尸胺等生物胺参与（L6503–6513）；② 物种集合是「time / temperature abuse 后能产生高组胺的鱼」，以金枪鱼、鲯鳅、马林、蓝鱼为主，完整清单在 Table 3-2；③ 组胺一旦形成，加热（含杀菌釜）或冷冻都不能消除（L6555–6557）。Appendix 5 Table A-5（L27547）给出 Histamine 两档判读：≥500 ppm 判 toxic、≥50 ppm 判 decomposed，出处 Sec. 540.525 CPG——**该行落在表格内，按规则只作描述、不逐字引用**。

〔L6477–6488〕
> Scombrotoxin (histamine) formation as a result of time and temperature abuse of certain species of fish can cause consumer illness. The illness is closely linked to the development of histamine in these fish. In most cases, histamine levels in illness-causing fish have been above 200 ppm, often above 500 ppm. However, there is some evidence that other chemicals (e.g., biogenic amines such as putrescine and cadaverine) may also play a role in the illness.


〔L6489–6494〕
> Seafood-related scombrotoxin poisoning is primarily associated with the consumption of tuna, mahi-mahi, marlin, and bluefish. Table 3-2 (Chapter 3) identifies other species that are also capable of developing elevated levels of histamine when temperature abuse occurs.


〔L6495–6503〕
> The illness caused by the consumption of fish in which scombrotoxin has formed is most appropriately referred to as “scombrotoxin poisoning.” The illness has historically been known by other names. Originally, the illness was termed “scombroid poisoning” because of its association with fish in the families Scombridae and Scomberesocidae. However, other species of fish are now known to cause the illness.

- **与常识或 PCHF 语境的差异**：常识把「组胺中毒」当作组胺单一物质超标；作者把它定义为「时间 / 温度滥用 + 特定鱼种 + 产组胺菌 + 可能伴随其他生物胺」的综合症，且病名刻意不叫 histamine poisoning。**200 / 500 ppm（Ch.7 致病鱼实测水平）与 50 / 500 ppm（CPG 执法判读档）是两套不同口径**，不可混为「FDA 规定组胺限值 50 ppm」。与 T-15 严格区分：L5244–5250 明确 scombrotoxin 由腐败菌形成生物胺，not considered natural toxins，故 Ch.6 的天然毒素安全水平表不适用于它。PCHF 语境无此物种清单与 ppm 档，属 Part 123 海产品专属。
- **建议 id**：t184（本轮备选，不纳入 YAML 草案）
- **建议 tags**：[指南自定义, 危害层级, 高频误读, 备选]

---

## T-13 ambient temperature（parasite 冻结三条件）

- **依据行号**：L4681–4691（Ch.5 寄生虫冻结三条件）、L4670–4679（影响因素）、L4692–4697（盐渍 / 醋渍不足）
- **作者本人的定义/用法**：三条等效冻结路径（-20°C / 7 天；-35°C 冻实后 -35°C / 15 小时；-35°C 冻实后 -20°C / 24 小时）**全部以 ambient temperature（环境温度 / 库温）表述**，并附加「厚度超过 6 英寸的大鱼可能不适用」的例外；盐渍 / 醋渍只能降低、不能消除或降到可接受水平（L4692–4697）。

〔L4681–4689〕
> Freezing and storing at an ambient temperature of -4°F (-20°C) or below for 7 days (total time), or freezing at an ambient temperature of -31°F (-35°C) or below until solid and storing at an ambient temperature of -31°F (-35°C) or below for 15 hours, or freezing at an ambient temperature of -31°F (-35°C) or below until solid and storing at an ambient temperature of -4°F (-20°C) or below for 24 hours are sufficient to kill parasites.


〔L4689–4691〕
> Note that these conditions may not be suitable for freezing particularly large fish (e.g., thicker than 6 inches).

- **与常识或 PCHF 语境的差异**：常识（及多数通用 HACCP 教材）写「产品中心温度 -20°C 保持 7 天」；作者用的是 **ambient temperature（环境 / 介质温度）而非鱼体中心温度**，两者在厚鱼上差异显著——这也正是 6 英寸例外的原因。三条件是「足以杀灭」的充分条件之一，不是唯一路径；与 PCHF 语境下的 lethality treatment / validation 思路不同，这里给的是可直接采用的成组时间–温度配方。
- **建议 id**：t185（本轮备选，不纳入 YAML 草案）
- **建议 tags**：[指南自定义, 控制策略, 高频误读, 备选]

---

## T-14 water phase salt

- **依据行号**：L25924–25935（Appendix 4 散文提及）、L17148–17150（Ch.13 的 i.e. 操作定义，列表项不逐字引用）、L1298–1299、L14194、L16727–16732
- **作者本人的定义/用法**：Appendix 4 只把 water phase salt 列为 Table A-1 中「能维持病原菌生长的最大值」参数之一（与 aw、pH、温度、需氧性并列），**并未在此给出定义**；L25932–25935 还警告表内是文献报道的极端值、may not apply to your processing conditions。真正的操作定义散见正文，如 L17148–17150 的同位语：water phase salt level 指「鱼肉水相部分中的盐浓度」（the concentration of salt in the water portion of the fish flesh），并给出 ≥5% 抑制 C. botulinum 的用例；Ch.13 多处把它与 aw、pH 一起作为多重屏障（barriers）参数。

〔L25924–25931〕
> This appendix contains information on the growth and inactivation of bacterial pathogens. Table A-1 contains information on the minimum water activity (a w ), acidity (pH), and temperature; the maximum, pH, water phase salt, and temperature; and oxygen requirements that will sustain growth for the bacterial pathogens that are of greatest concern in seafood processing.

- **与常识或 PCHF 语境的差异**：常识里的「盐度 / 含盐量」是占产品总重的百分比（% w/w）；water phase salt 只算**水相中的盐**，不等同于总配方盐量，也不等同于 water activity（aw），三者不可互相换算。用户指定的 L25926–25929 只是「提及」而非定义，故本条为弱候选：附录把它当表格参数列举，定义依赖 Ch.13 正文，且明确「极端值不适用于你的工艺条件」。PCHF 语境（§117 / 酸化与低酸食品）常用 aw、pH 作控制参数，不设 water phase salt 这一术语，属海产品 / 肉毒梭菌控制专属。
- **建议 id**：t186（本轮备选，不纳入 YAML 草案）
- **建议 tags**：[指南自定义, 控制策略, 备选]

---

## T-15 natural toxin

- **依据行号**：L5202–5255（Ch.6 定义、六种综合征、安全水平用途）、L5235–5243、L5244–5250（与 scombrotoxin 划界）
- **作者本人的定义/用法**：由鱼类 / 贝类所生存水体中的天然毒素（多数由海洋藻类 phytoplankton 产生，经食物链逐级富集）造成的危害；另承认少数非藻类来源、仅特定鱼种特有的毒素与有害化合物（L5220–5223）。全球已识别天然毒素众多，但「currently six recognized natural toxin poisoning syndromes」为 ASP、AZP、CFP、DSP、NSP、PSP（L5224–5234，列表只作描述）。最关键的用法限定：Appendix 5 的安全水平用于确认疾病、发布风险渔区通告、决定渔区关闭，**should not be identified in the HACCP plan**——不能当成 HACCP 计划里的关键限值。L5244–5250 明确把 scombrotoxin（组胺）排除在 natural toxins 之外。

〔L5206–5223〕
> Fish and molluscan shellfish contaminated with natural toxins from the water in which they lived can cause consumer illness. Most of these toxins are produced by naturally occurring marine algae (phytoplankton). Fish or molluscan shellfish consume the algae, or animals that have consumed the algae, which causes the toxins to accumulate in the fish's or molluscan shellfish's flesh. The toxin continues to accumulate in the feeding animal's body at each point of consumption and results in higher levels further up the food chain.


〔L5235–5243〕
> All safety levels identified through guidance and regulations for natural toxins may be found in “Appendix 5: FDA and EPA Safety Levels in Regulations and Guidance” of this Guide; however, these levels should not be identified in the HACCP plan as they are utilized for confirming illnesses (i.e. CFP), inform advisories for at risk harvest areas (i.e., CFP) and/or make a determination for harvest area closures (i.e., ASP, AZP, DSP, NSP, and PSP.)

- **与常识或 PCHF 语境的差异**：常识把「天然毒素安全水平」当作产品放行 / 限值标准；作者明文**禁止把它写进 HACCP plan**，其用途是公共卫生监测与渔区管理，不是加工者的 CCP 关键限值。与 T-12 的划界：组胺由腐败菌在时间 / 温度滥用后形成，不是天然毒素，两章的安全水平与判定口径互不通用。PCHF（§117.130）把天然毒素列为化学危害之一，但无「渔区关闭 / 通告」这类由政府监测驱动的 upstream 控制；本指南的控制重点在原料来源与收获水域，而非厂内工序。
- **建议 id**：t187（本轮备选，不纳入 YAML 草案）
- **建议 tags**：[指南自定义, 危害层级, 高频误读, 备选]

---

## 可直接粘贴的 YAML 草案

```yaml
# ===== v4.10 追加 t173–t182（第 15 类来源：FDA Fish and Fishery Products
#      Hazards and Controls Guidance, 4th Ed., June 2022）=====
# 说明：草案内不使用任何 ASCII 双引号，一律中文引号「」或裸写，避免 safe_load 失败。

- id: t173
  title: should 是术语级的强制程度标记（非 required）
  summary: >-
    指南在开篇专门定义：Agency guidance 中出现的 should 一律表示建议或推荐，而非要求；
    只有在明确转引法规或法条时才产生法定义务。指南正文宣称自身不设立可依法强制执行的责任，
    控制策略与做法只是推荐，除非被法规或法令要求。判定链上必须把「§123.6 强制的 HACCP 计划与危害分析」
    与「指南用 should 表述的表单、书面化、限值示例」分层，否则会把建议误升格为法定义务。
  tags: [指南自定义, 效力层级, 高频误读, 判定链]

- id: t174
  title: hazard analysis 与 HACCP plan 是两个法定动作，书面化义务不对称
  summary: >-
    §123.6(a) 要求所有海产品加工者进行或委托进行危害分析，判定是否存在 reasonably likely to occur 的
    食品安全危害并识别可施加的预防措施；§123.6(b) 要求危害分析显示存在此类危害时必须拥有并实施书面 HACCP 计划。
    但指南明说：法规不要求危害分析以书面形式保存，也不要求使用附录 1 的表格；FDA 只是期望有书面危害分析，
    理由是便于强制复审与应监管要求举证某危害为何被纳入或未纳入计划。切勿把 Part 117 的书面危害分析义务套到 Part 123。
  tags: [法定定义, 指南自定义, 判定链, 高频误读]

- id: t175
  title: species-related hazard 与 process-related hazard 按引入地点二分
  summary: >-
    分类轴是危害被引入的环节而非危害种类：在厂区外、收获前中后随原料带来的称 species-related hazard
    （查 Table 3-2 脊椎动物、Table 3-3 无脊椎动物）；在厂区环境内由加工方式带来的称 process-related hazard
    （查 Table 3-4，由成品形态、包装类型、储运方式三者决定）。查表所得潜在物种相关危害须记入 Worksheet 第 2 栏，
    且每一个加工步骤都要记。process-related 不是「某工序出错」，而是产品与流通设计的结果，例如真空包装带来的
    肉毒梭菌风险。PCHF 按与设施或食品相关联识别危害，不设此二分。
  tags: [指南自定义, 危害层级, 判定链, 易混术语]

- id: t176
  title: reasonably likely to occur 的三要素与「无控制假设态」（§123.6(a)）
  summary: >-
    法规定义为：一个审慎加工者会据经验、疾病数据、科学报告或其他信息，断定在缺乏那些控制措施的情况下，
    该危害在所加工的特定鱼或渔产品中有合理发生可能性，因而会为其设立控制。三个不可拆的限定是：
    判定主体为假想的 prudent processor、证据基础为四类信息、判定基准为 in the absence of those controls 的假设态。
    它不是统计概率阈值，而是规范性判断；若在已有控制有效的前提下去评估，会错判为不显著并跳过整条 CCP 链。
    Ch.3 与各章表格仅辅助判断普通情形下的显著性，且不得单独使用。
  tags: [法定定义, 判定链, 核心概念, 高频误读]

- id: t177
  title: significant hazard 等价于 reasonably likely to occur，且不等于本步骤必须控制
  summary: >-
    Step 10 把第 2 栏潜在危害清单收敛为 significant hazards，作者用 in other words 直接等同于
    reasonably likely to occur。因此 significant 与危害严重程度无关，只是「是否进入 HACCP 控制链」的二分开关，
    输出落在第 3 栏 Yes 或 No 与第 4 栏理由。指南特别强调：某加工步骤判显著并不意味着必须在该步骤实施控制，
    CCP 位置由 Step 11 另定。把查表得到的潜在危害直接当成必须设 CCP 的显著危害，是最常见的误读。
  tags: [法定定义, 判定链, 核心概念, 高频误读]

- id: t178
  title: Hazard Analysis Worksheet 六栏是危害分析判定链的书面载体
  summary: >-
    第 1 栏加工步骤、第 2 栏潜在危害（查表所得，每一步都记）、第 3 栏是否显著、第 4 栏判定理由、
    第 5 栏预防措施或控制策略、第 6 栏是否 CCP。Step 6 至 Step 11 全在这张表上完成：第 3 栏答 No 的步骤
    可跳过 Steps 11 至 18，第 6 栏答 No 的步骤可跳过 Steps 12 至 18；Step 12 再把第 6 栏为 Yes 的步骤
    搬进 HACCP Plan Form。第 4 栏理由是后续复审与监管质询的唯一举证位，呼应 FDA 对书面危害分析的期望。
    PCHF 表单不设是否 CCP 一栏，套用会漏掉这条接口。
  tags: [指南自定义, 判定链, 表单结构, 核心概念]

- id: t179
  title: control strategy example：同一危害多条策略，CCP 位置随之改变
  summary: >-
    Ch.4 至 7、9、11 至 21 每章对同一危害给出一条或多条控制策略示例，并各带 Set Critical Limits、
    Establish Monitoring Procedures、Identify CCPs 分节。作者刻意用 example 而非 requirement：控制同一危害
    往往不止一种方式，选哪条策略决定 CCP 落在哪个加工步骤，也决定关键限值与监控参数。
    因此 CCP 不是危害的固有属性。误读风险是把某章示例限值当成法定限值抄进计划，
    忽略选用其他控制策略或限值须科学论证其充分性这一要求。
  tags: [指南自定义, 判定链, 控制策略, 高频误读]

- id: t180
  title: CCP 是加工步骤，每个显著危害至少一个（§123.6(c)(2) / §123.3(b)）
  summary: >-
    CCP 被定义为流程中的点，即加工步骤，而非设备或参数。每个显著危害必须至少有一个 CCP 加以控制，
    但可多于一个 CCP；一个加工步骤也可同时是多个危害的 CCP。CCP 上的控制活动须能有效预防、消除危害，
    或将其降低到可接受水平。判定用 Appendix 3 的 CCP 判定树。显著危害所在的步骤不等于 CCP 所在的步骤，
    这正是 Step 11 独立存在的原因。PCHF 不用 CCP 作核心范畴，改用 process preventive control 加管理组件，
    两套框架不可互引。
  tags: [法定定义, 判定链, 核心概念, 易混术语]

- id: t181
  title: critical limit 须对应被监控参数，替换示例限值须科学论证
  summary: >-
    Step 13 定义为：为控制危害，某工艺参数必须被控制到的最大或最小值。限值须直接对应将被监控的参数，
    例如监控水浴温度与传送带速度就把这两项写成限值，而不是写无法连续监控的产品中心温度。
    限值过严会在并无安全问题时触发纠正措施，过松会放行不安全品；可另设更严的 operating limit 提前调整。
    最关键的是：加工者可选用其他控制策略或关键限值，但须科学论证其充分性，且须符合适用食品安全法律法规。
    本指南各章限值只是示例，不是 FDA 规定的固定数字。
  tags: [指南自定义, 判定链, 控制策略, 高频误读]

- id: t182
  title: HACCP Plan Form 监控四问 What / How / Frequency / Who
  summary: >-
    Step 14 要求完整描述监控程序须回答四问：监控什么、如何监控、多久监控一次、由谁监控，
    分别落入 HACCP Plan Form 第 4、5、6、7 栏；第 1 至 3 栏由 Step 12 至 13 填入 CCP 步骤、危害与关键限值。
    监控须直接测量已设限值的参数，连续监控总是可取但非必需，频率取决于正常波动与测量值贴近限值的程度，
    连续监控记录至少每日复核。四问中 How 与 Who 与 What 或 Frequency 同等必答，缺一即程序不完整。
    PCHF 另要求 PCQI 监督，本指南的 Who 只指执行监控者，不可凭空加人。
  tags: [法定定义, 判定链, 表单结构, 监控]
```

---

## 覆盖率自查

- **指定行块覆盖**：任务列出的 13 组位置全部回读并落条。① reasonably likely to occur（L1780–1789）→ T-04；② significant hazard（L1774–1779）→ T-05；③ species-related vs process-related（L2107–2124 + L1678–1694）→ T-03；④ should（L105–108）→ T-01；⑤ control strategy example（L1843–1847）→ T-07；⑥ hazard analysis vs HACCP plan（L1503–1506 / L1534–1540）→ T-02；⑦ CCP（L1852–1862）→ T-08；⑧ critical limit 与替代限值科学论证（L121–126 / L1605–1607 / L1891–1933）→ T-09；⑨ Worksheet 六栏（L1705–1708 / L1813–1822 / L1848–1851 / L1863–1870，另补 L1673–1675）→ T-06；⑩ 监控四问（L1607–1611 列表 + L1946–1950 散文）→ T-10；⑪ prudent processor（L1782）→ T-11；⑫ scombroid / histamine（L6474 起 + L27547）→ T-12；⑬ 可选补充三项（ambient temperature L4681–4689 → T-13；water phase salt L25926–25929 → T-14；natural toxin L5204 起 → T-15）全部覆盖。
- **数量与编号**：候选池 **15 条**（≥12 要求满足），终选 **10 条**（t173–t182），超额备选 **5 条**（t183–t187，顺序编号但本轮不落库）。终选 10 条接续既有 t172，编号连续无跳号；备选条目的建议 id 明确标注「本轮备选，不纳入 YAML 草案」。
- **判定链闭环**：终选 10 条按链序排列且首尾闭合——效力层（t173）→ 危害识别（t175）→ 显著性判定（t176、t177）→ 落表载体（t178）→ 策略与 CCP（t179、t180）→ 限值与监控（t181、t182）→ 书面化期望回扣（t174）。每条均含「与常识差异」和「与 PCHF（Part 117）语境差异」两层说明，共 20 处差异标注。
- **引用合规**：共 32 段顶格 `> ` 引用块，均取自散文段落，实测每段 18–83 词（`max 83`），全部 ≤100 词，并逐段标注 `〔Lxxxx–xxxx〕` 行号标签（32 段与 32 个标签一一对应）。以下**未作逐字引用**、仅中文转述：Appendix 5 Table A-5 的 50 / 500 ppm 行（L27547）、Table 3-4 的项目符号定义（L2118–2124）、Ch.6 六种综合征列表（L5229–5234）、Step 列表 What / How / Frequency / Who（L1607–1611）、页码页眉（如 L6469「6 - 19 (August 2019)」、L27537「A5 - 7 (June 2021)」）、章节标题（L5202、L6474）、Ch.13 的 water phase salt 列表项同位语（L17148–17150）。
- **YAML 安全性**：草案内 **0 个 ASCII 双引号**，需要引号处一律用中文「」或裸写；`>-` 块标量统一 4 空格缩进、无空行、无 ASCII 冒号加空格的行、无以 `- ` 开头的行，可直接 `yaml.safe_load`。字段严格为 `- id:` / `title:` / `summary: >-` / `tags: [...]`，与既有 t171 / t172 一致。
- **溯源与转引边界**：21 CFR 123.6(a) 法规正文在本文件 L29810–29834 有转载，已用于交叉核对 T-02 / T-04；§123.3(b)、§123.6(c)(2)、§123.6(c)(4)、§123.7 在指南内均以括注形式转引，未另核 CFR 年度编纂版正文，按既有包口径标注为转引未收。任务称源文档 31,321 行，实测 `wc -l` 为 31,322 行，差 1 行疑为末行换行计数差异；所有引用行号均按本文件实际回读确认，未使用推测行号。
- **只读纪律**：本轮仅新增本候选文件，未修改 `glossary.md` 或包内其它任何文件。
