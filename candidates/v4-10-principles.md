# 阶段 1 候选池 — 原则提取器（v4.10 / 第 15 类来源）

- 源文档：`C:/Users/周至/AppData/Local/Temp/seafood_guide.md`（FDA《Fish and Fishery Products Hazards and Controls Guidance》June 2022 Edition，第 4 版导出全文，共 31,321 行；本文所有行号均以此文件为准）
- 扫描范围：全量定向扫描 + 全文正则复核。覆盖导言（L1–147）、Ch.1 范围与限制（L113–144）、Ch.3 危害分析工作表与 18 步流程（L1500–2160）、Ch.5 寄生虫（L4660–4708）、Ch.7 组胺/鲭鱼毒素（L6820–6895）、Ch.9/13 化学与病原菌（L14445–14494、L21335–21367）、Appendix 1 工作表列头（L25774、L25783）、Appendix 3 CCP 决策树（L25880–25893）、Appendix 5 安全水平表（L27425–27619）、21 CFR 123 法规重印（L29810–29827）。
- 提取口径：只取散文段落作英文引用；表格内数值仅作中文描述、不逐字引用（Appendix 5、A-5 各行、Ch.7 控制策略表均按此处理）。
- 与既有卡的分工：CAP-22 负责 **21 CFR Part 123 法条义务层**（shall / must / 强制性义务）；本卡只负责 **技术指南层**（should / 建议 / 可替代 / 须科学论证）。二者最易混淆，故每个候选单元末尾单列「与 CAP-22 法条层的区分」。
- 产出时间：2026-11-06
- 候选单元数：10

---

## P-01 非约束性三层边界：guidance 不设可执行责任、`should` 仅建议、替代控制策略须科学论证充分性

- 类型：效力边界口径 / 全卡总纲原则
- 依据行号：
  - L100–108（导言「FDA's guidance documents」独立段）
  - L115–126（Ch.1「Scope and Limitations」首段）
  - L137–144（Ch.1「Scope and Limitations」末段）
  - L92–95（导言读者对象段）
  - 以上为 4 个彼此独立、分布在不同小节的散文段落，满足 V1 跨域验证。
- 原则表述：本指南的效力须分四层理解，不可整册当作强制规范。
  1. **效力层**：guidance 本身不产生 legally enforceable responsibilities，只表述 Agency's current thinking；**唯有文中明确引用了 regulatory or statutory requirements 时，被引用的那部分才带强制力**。
  2. **语义层**：`should` = suggested or recommended, but not required；指南中出现的 `must` / `shall` / `requires` 几乎都是回指法条（如 L1852–1854 回指 21 CFR 123.6(c)(2)），不能据此推断指南自身设义务。
  3. **替代层**：加工者可以选用其他控制策略（含其他 critical limits），但必须同时满足：(a) 符合 applicable food safety laws and regulations；(b) **scientifically establish their adequacy**（科学论证其充分性）。
  4. **兜底层**：指南不替代加工者自行实施的危害分析；未列入指南的危害在特定情形下仍可能相关；须对 new or emerging problems 保持警觉（如以往未关联的鱼种出现天然毒素）。

  > FDA's guidance documents, including this guidance, do not establish legally enforceable responsibilities. Instead, guidance describes the Agency's current thinking on a topic and should be viewed only as recommendations, unless specific regulatory or statutory requirements are cited. The use of the word "should" in Agency guidance means that something is suggested or recommended, but not required. 〔L100–108〕

  > The control strategies and practices provided in this guidance are recommendations to the fish and fishery products industry unless they are required by regulation or statute. This guidance provides information that would likely result in a HACCP plan that is acceptable to FDA. Processors may choose to use other control strategies, as long as they comply with the requirements of the applicable food safety laws and regulations. However, processors that chose to use other control strategies (e.g., critical limits) should scientifically establish their adequacy. 〔L115–126〕

  > The guidance is not a substitute for the performance of a hazard analysis by a processor of fish and fishery products, as required by FDA's regulations. Hazards not covered by this guidance may be relevant to certain products under certain circumstances. In particular, processors should be alert to new or emerging problems (e.g., the occurrence of natural toxins in fish not previously associated with that toxin). 〔L137–144〕

- 违反后果 / 反例：
  - 把 Ch.5 的冻结参数、Ch.7 的 50 ppm 采样要求、Appendix 5 的数值直接当作「FDA 强制限值」对企业开具不符合项——指南自身不设可执行责任，只有回指法条处才强制。
  - 采用自选关键限值（如自定巴氏杀菌时间/温度）却未做科学验证、无验证记录——违反 L124–126 的「scientifically establish their adequacy」。
  - 因为「指南没提到这个危害」就把新出现的毒素/区域特异性危害排除在危害分析之外——违反 L139–144 兜底义务。
- 与 CAP-22 法条层的区分：CAP-22 处理的是 21 CFR Part 123 中以 `shall` 表述的强制义务（如 123.6(a) 须作危害分析、123.6(b) 须有书面 HACCP 计划），违反即构成法规不符合。本单元处理的是**同一部指南文件本身的法律地位**：它是建议性文件，多数条款用 `should`，且允许替代方案。判定某条要求是否强制，唯一依据是「该处是否引用了法规/法条」，而非它在指南里读作 `must` 还是 `should`。

---

## P-02 表不可单独使用 + 自身/外部专家补表外危害（跨章节反复强调的原则）

- 类型：清单使用规则 / 跨章节反复强调原则
- 依据行号（**全部重复出现位置，共 5 处**）：
  1. L127–136（Ch.1「Scope and Limitations」，针对 Ch.3 及 Ch.4–21 全部表格的总声明）
  2. L137–144（Ch.1 同小节，危害未覆盖与新出现危害的兜底）
  3. L1709–1719（Ch.3 STEP 7，物种相关危害 Tables 3-2 / 3-3）
  4. L1753–1760（Ch.3 STEP 8–9，工艺相关危害 Table 3-4）
  5. L2128–2134（Ch.3 表下 NOTES，物种识别表的通用注释）
  - 分布跨 Ch.1 总论与 Ch.3 三个不同操作步骤，是全文重复密度最高的原则之一。
- 原则表述：Ch.3 的物种/工艺危害表只给出 **potential hazards（潜在危害）** 清单，不是显著性结论，更不是完整危害清单。使用规则固定为三段式：
  1. 表**不得单独使用**（should not be used separately）；
  2. 必须与 Ch.4–21 各危害章节的信息 **combined** 后，才能判定 likelihood of occurrence；
  3. 必须叠加**自身专业知识或外部专家**（your own expertise, or that of outside experts）补出表外危害——物种表补「本区域新/特有」危害，工艺表补「本厂厂房、设备、工艺新/特有」危害。
  - 该三段式在 Ch.1 声明一次、Ch.3 的 STEP 7 / STEP 8–9 / 表下 NOTES 各重复一次，属于**刻意反复强调**，不是编辑冗余。

  > The information contained in the tables in Chapter 3 and in Chapters 4 through 21 provide guidance for determining which hazards are "reasonably likely to occur" in particular fish and fishery products under ordinary circumstances. However, the tables should not be used separately for this purpose. The tables list potential hazards for specific species and finished product types. This information should be combined with the information in the subsequent chapters to determine the likelihood of occurrence. 〔L127–136〕

  > Tables 3-2 and 3-3 include the best information currently available to FDA concerning hazards that are specific to each species of fish. You should use your own expertise, or that of outside experts, as necessary, to identify any hazards that may not be included in the table (e.g., those that may be new or unique to your region). You may already have effective controls in place for a number of these hazards as part of your routine or traditional handling practices. The presence of such controls does not mean that the hazard is not significant. 〔L1709–1719〕

  > Table 3-4 includes the best information currently available to FDA concerning hazards that are related to specific processing techniques. You should use your own expertise, or that of outside experts as necessary, to identify any hazards that may not be included in the table (e.g., those that are new or unique to your physical plant, equipment, or process). 〔L1753–1760〕

  > The tables provide lists of potential hazards. You should use the tables, together with the information provided in Chapters 4 through 21, and your own expertise or that of outside experts, to determine whether the hazard is significant for your particular product or process and, if so, how it should be controlled. 〔L2128–2134〕

- 违反后果 / 反例：
  - 只查 Table 3-2 打了勾就把潜在危害抄进工作表 Column 2、直接给 Yes/No，不查 Ch.4–21 的「Understand the Potential Hazard」「Determine Whether this Potential Hazard Is Significant」——典型「表格单独使用」违规。
  - 加工进口/本区域新鱼种、或新增了一条腌制/烟熏线，仅按表内已有危害判定，未引入外部专家评估区域特异性毒素或本厂特有交叉污染——表外危害漏判。
  - 把「表里没有这个危害」当作「这个危害不显著」的论据——表只列 potential hazards，不列显著性结论。
- 与 CAP-22 法条层的区分：21 CFR 123.6(a) 只要求「开展危害分析以判断是否存在 reasonably likely to occur 的危害」，并**不规定用什么表、也不要求使用 FDA 的表格**（L1506–1507 明确 the regulation does not require that you use the form included in Appendix 1）。Ch.3 表格及其「不得单独使用 / 专家补表外」规则是 FDA 提供的**技术工具使用规范**，属指南层；企业不用 FDA 表格并不违法，但若用了就须按上述三段式使用，否则危害分析本身可能因不充分而违反法条层义务。

---

## P-03 「无控制条件下判定」原则：已有控制有效，恰恰证明危害「合理可能发生」

- 类型：危害分析判定链核心规则 / 跨章节反复原则
- 依据行号：
  - L1716–1731（Ch.3 STEP 7，原则句 + 组胺两例分岔）
  - L1780–1789（Ch.3 STEP 10，引 Seafood HACCP Regulation 对 reasonably likely to occur 的定义）
  - L6945–6955（Ch.7 组胺/时间温度滥用章节，独立复述）
  - L14451–14481（Ch.13 病原菌生长/产毒章节，独立复述 + 三条件清单）
  - L29820–29827（21 CFR 123.6(a) 法规原文重印，定义法定来源）
  - 跨 Ch.3 流程章、Ch.7 与 Ch.13 两个危害专章、法规重印四处，重复最充分。
- 原则表述：判定「危害是否 reasonably likely to occur」必须在 **in the absence of controls（假设不存在任何控制）** 的前提下进行。控制措施的存在不是「危害不显著」的证据，反而是「该危害在无控制时会发生」的证据——因此该危害应判为显著，且现有控制应被正式纳入 HACCP 计划。
  - **两个例子的分岔（L1721–1731，同一观察、相反结论）**：观察到「某种鱼从未出现组胺（scombrotoxin）形成」，原因可能是——
    - 情形 (1)：**该鱼种本身不能产生组胺**（inability of the fish to produce histamine）→ 无控制条件下也不会发生 → hazard is **not** reasonably likely to occur → 判 No。
    - 情形 (2)：**已存在控制防止其形成**（如捕捞船时间/温度控制 harvest vessel time and temperature controls）→ 无控制条件下会发生 → hazard **is** reasonably likely to occur → 判 Yes，且 the controls should be included in the HACCP plan。
  - 分岔的唯一判别依据不是「历史上有没有出过事」，而是「去掉控制后会不会出事」。L29820–29827 的法定定义同样以 "in the absence of those controls" 收尾，说明这不是指南自行发明的口径，而是对法条定义的操作化。

  > You may already have effective controls in place for a number of these hazards as part of your routine or traditional handling practices. The presence of such controls does not mean that the hazard is not significant. The likelihood of a hazard occurring should be judged in the absence of controls. 〔L1716–1721〕

  > For example, the fact that scombrotoxin (histamine) development in a particular species of fish has not been noted may be the result of (1) the inability of the fish to produce histamine or (2) the existence of controls that are already in place to prevent its development (e.g., harvest vessel time and temperature controls). In the first case, the hazard is not reasonably likely to occur. In the second case, the hazard is reasonably likely to occur, and the controls should be included in the HACCP plan. 〔L1721–1731〕

  > The Seafood HACCP Regulation defines a food safety hazard that is reasonably likely to occur as "one for which a prudent processor would establish controls because experience, illness data, scientific reports, or other information provide a basis to conclude that there is a reasonable possibility that it will occur in the particular type of fish or fishery product being processed in the absence of those controls." 〔L1780–1789〕

  > To answer this question, you should consider the potential for time and temperature abuse in the absence of controls. You may already have controls in your process that minimize the potential for time and temperature abuse that could result in unsafe levels of histamine. This guidance will help you determine whether those or other controls should be included in your HACCP plan. 〔L6945–6955〕

  > Remember that you should consider the potential for time and temperature abuse in the absence of controls. You might already have controls in your process that minimize the potential for time and temperature abuse that could result in unsafe levels of pathogenic bacteria or toxins. This section and subsequent sections will help you determine whether those or other controls should be included in your Hazard Analysis Critical Control Point (HACCP) plan. 〔L14451–14461〕

- 违反后果 / 反例：
  - 「我们一直有冷藏/时间温度控制，从来没出过组胺问题，所以这个危害不显著」→ 正好判反。按 L1729–1731 应判 Yes，并把捕捞船/冷藏控制写入 HACCP 计划。
  - 把「已有控制」当作 Column 3 填 No 的理由，却又不把该控制纳入 HACCP 计划 → 控制游离于计划之外，既无监控也无纠偏，实质失控。
  - 误把情形 (1)（鱼种本身不产组胺，可判 No）套用到情形 (2)（有控制才没出事），或反之——两例的结论完全相反，是本原则最易错的分岔点。
- 与 CAP-22 法条层的区分：CAP-22 承载 **"reasonably likely to occur" 的法定定义及其来源**（21 CFR 123.3 / 123.6(a)，prudent processor 标准，L29820–29827 即法规原文重印）。本单元承载的是**把该定义落到工作表上的操作判定规则**：在「假设无控制」下评估、控制存在即判 Yes、控制须入计划、以及两例分岔的推理路径。法条给的是「什么是显著危害」，指南给的是「面对一个具体加工步骤该怎么判」。

---

## P-04 逐步独立评估显著性 + 三条判定标准 + 累积效应与预期用途

- 类型：判定链规则 / 显著性评估口径
- 依据行号：
  - L1796–1812（Ch.3 STEP 10，逐步独立评估 + 三条判定标准 + 分销/储存/预期用途/消费者）
  - L6945–6966（Ch.7 组胺，跨步骤累积时间温度滥用）
  - L14462–14494（Ch.13 病原菌，「all of the following conditions are met」三条件清单）
  - 跨 Ch.3 流程章与 Ch.7、Ch.13 两个危害专章，3 个独立段落。
- 原则表述：显著性不是对「产品整体」一次判定，而是 **independently at each processing step（每个加工步骤独立判定）**；同一危害可在此步显著、在彼步不显著。逐步判定按三条标准取「或」：
  1. 该步**引入**不安全水平的危害是合理可能的；
  2. 该步使危害**增加**到不安全水平是合理可能的；
  3. 危害在**另一步**显著，而**当前步**可将其预防、消除或降低到可接受水平（即当前步是潜在 CCP）。
  - 判定时还须纳入 L1808–1812 的分销与储存方式、预期用途与消费者（来自 STEP 3/4）；并须考虑 **cumulative effect（累积效应）**——单个步骤的时间温度滥用不足以致病，但多个连续步骤的累积滥用可能足够（L6956–6966）；Ch.13 进一步把「无控制条件下累积滥用可发生且该步贡献显著」列为判定条件之一（L14474–14481）。

  > You should evaluate the significance of a potential hazard independently at each processing step. It may be significant at one step but not at another. A potential hazard is significant at the processing or handling step if (1) it is reasonably likely that the hazard can be introduced at an unsafe level at that processing step; or (2) it is reasonably likely that the hazard can increase to an unsafe level at that processing step; or (3) it is significant at another processing or handling step and it can be prevented, eliminated, or reduced to an acceptable level at the current processing or handling step. 〔L1796–1808〕

  > When evaluating the significance of a hazard at a processing step, you should consider the method of distribution and storage and the intended use and consumer of the product, which you developed in Steps 3 and 4. 〔L1808–1812〕

  > Time and temperature abuse that occurs at successive processing and storage steps may be sufficient to result in unsafe levels of histamine, even when abuse at one step alone would not result in such levels. For this reason, you should consider the cumulative effect of time and temperature abuse during the entire process. 〔L6956–6966〕

- 违反后果 / 反例：
  - 只给整条产品线填一行「组胺：No」，未按接收/解冻/腌制/包装/储运逐步判定 → 漏掉某步「引入」或「增加」的显著性。
  - 逐步评估时只看单步温升，忽略 L6956–6966 的跨步骤累积滥用，判成 No。
  - 未考虑产品是即食（RTE）还是需烹饪、面向婴幼儿还是普通成人，直接套用默认判定 → 违反 L1808–1812。
  - 把第 (3) 条「当前步可降低危害」误读为「该步必须控制」（见 P-05）。
- 与 CAP-22 法条层的区分：21 CFR 123.6(a) 要求危害分析覆盖「before, during, and after harvest」各环节危害，但**不规定判定标准、不规定按加工步骤拆分、也不规定累积效应判法**（L29810–29819）。三条标准、逐步独立评估、累积效应、预期用途纳入，全部是指南层把法条义务操作化的技术口径。

---

## P-05 Yes/No 都要写理由；「显著」≠「必须在该步控制」

- 类型：工作表填写口径 / 判定链衔接规则
- 依据行号：
  - L1813–1822（Ch.3 STEP 10 尾，Column 3 的 Yes/No 与 Column 4 理由）
  - L1823–1827（Ch.3 STEP 10 后紧接的重要注释块）
  - L1828–1870（Ch.3 STEP 11，CCP 判定与 Column 6、以及 21 CFR 123.6(c)(2) 回指）
  - L1534–1540（Ch.3 导言，书面危害分析非法条强制）
  - 4 个独立散文段落，含一处「指南内因回指法条而出现 must」的对照样本。
- 原则表述：
  1. Column 3 无论填 **Yes 还是 No，都必须在 Column 4 记录理由**（record the reason for your "Yes" or "No" answer）。填 No 的步骤可跳过 STEP 11–18；填 Yes 的步骤必须继续走完 CCP 判定与控制措施设计。
  2. **判定显著 ≠ 判定 CCP**：identifying a hazard as significant at a processing step does not mean that it must be controlled at that processing step；CCP 定位由 STEP 11 单独完成（借助 Appendix 3 决策树）。
  3. 每个显著危害**至少有一个 CCP** 予以控制（21 CFR 123.6(c)(2)），但一个危害可有多个 CCP、一个步骤可控制多个危害。Column 6 的 Yes/No 同样决定是否跳过 STEP 12–18。
  4. 危害分析是否书面化：法条不要求，FDA 期望书面化以便于强制性的 HACCP 计划再评估与应对监管质询（L1534–1540）——这是「指南推荐强于法条底线」的典型样本。

  > If you determine that a potential hazard is significant at a processing step, you should answer "Yes" in Column 3 of the Hazard Analysis Worksheet. If you determine that a potential hazard is not significant at a processing step, you should answer "No" in that column. You should record the reason for your "Yes" or "No" answer in Column 4. You need not complete Steps 11 through 18 for a hazard for those processing steps where you have recorded a "No." 〔L1813–1822〕

  > It is important to note that identifying a hazard as significant at a processing step does not mean that it must be controlled at that processing step. Step 11 will help you determine where in the process the critical control point is located. 〔L1823–1827〕

  > For every significant hazard, there must be at least one CCP where the hazard is controlled (21 CFR 123.6(c)(2)). In some cases, control may be necessary at more than one CCP for a single hazard. In other cases, a processing step may be a CCP for more than one hazard. CCPs are points in the process (i.e., processing steps) where the HACCP control activities will occur. 〔L1852–1859〕

- 违反后果 / 反例：
  - Column 3 填 No 但 Column 4 空白，或只给 Yes 写理由、No 不写 → 违反 L1818–1820「Yes or No 都要写理由」；监管质询时无法 justify why certain hazards were not（L1539–1540）。
  - 因某步判了 Yes（显著），就自动把该步设为 CCP 并设关键限值、监控、纠偏 → 混淆 STEP 10 与 STEP 11，可能造成 CCP 冗余或把控制放在无效步骤。
  - 显著危害存在却全表 Column 6 均为 No、无任何 CCP → 直接触及 21 CFR 123.6(c)(2) 法条层底线。
  - 把「法条不强制书面危害分析」理解为「可以不做记录」——法条虽不要求，但无记录则无法支撑 HACCP 计划再评估与合理性说明。
- 与 CAP-22 法条层的区分：CAP-22 规定「须有书面 HACCP 计划」「每个 CCP 须有关键限值」「须监控/纠偏/验证/记录」（123.6(c)）等结果性义务，且「至少一个 CCP」本身是法条（L1852–1854 的 `must` 正因回指 123.6(c)(2)）。本单元是**工作表层的填写与衔接规则**：Column 3/4/6 怎么填、Yes/No 都要理由、显著与 CCP 分离、哪些步骤可跳过 11–18 或 12–18。L1534–1540 更给出一条明确分界——危害分析书面化「法条不要求、指南期望」，恰好位于两层之间。

---

## P-06 完整危害分析判定链：18 步序列与工作表 6 列映射

- 类型：流程清单 / 判定链骨架（回应用户「完整危害分析判定链」要求）
- 依据行号：
  - L1500–1540（Ch.3 导言，危害分析义务来源与工作表定位）
  - L1555–2085（Ch.3 STEP 1–18 完整展开，18 个独立步骤标题）
  - L25774、L25783（Appendix 1 危害分析工作表列头，6 列结构；列头文字按表格内容仅描述、不逐字引用）
  - L25884–25893（Appendix 3 CCP 决策树 Q1–Q3）
  - L29810–29827（21 CFR 123.6(a)/(b) 法规原文重印，判定链的法条锚点）
  - 跨 Ch.3、Appendix 1、Appendix 3、法规重印四个独立区域。
- 原则表述：指南把「从产品描述到 HACCP 计划成形」拆成固定 18 步，并由 Appendix 1 的 6 列工作表承载，各步骤与列一一映射：
  - **预备（STEP 1–6，L1560–1675）**：1 一般信息、2 描述食品（市场名/拉丁名、成品形态）、3 分销与储存方式、4 预期用途与消费者、5 绘制流程图、6 建立危害分析工作表。
  - **危害分析（STEP 7–11，L1676–1870）**：7 物种相关潜在危害（Tables 3-2/3-3）→ Column 2；8 工艺相关潜在危害（Table 3-4）→ Column 2；9 查阅 Ch.4–21 理解潜在危害；10 逐步判定显著性 → Column 3（Yes/No）+ Column 4（理由）；11 判定 CCP（Appendix 3 决策树）→ Column 5（预防措施）+ Column 6（CCP Yes/No）。
  - **HACCP 计划（STEP 12–18，L1875–2085）**：12 建立 HACCP 计划表、13 设定关键限值、14 监控程序、15 纠偏行动、16 记录保持、17 验证程序、18 完成 HACCP 计划表。
  - 跳过规则：Column 3 = No → 跳过 11–18；Column 6 = No → 跳过 12–18（L1820–1822、L1868–1870）。
  - 全链的法条锚点只有两处：21 CFR 123.6(a)（须作危害分析，L1520–1527、L29810–29819）与 123.6(b)(c)（显著危害须有 HACCP 计划，L29828–29833）；其余 18 步与工作表均为 FDA 的标准化模板，法条不要求使用该表（L1506–1507）。

  > The regulation does not require that you use the form included in Appendix 1. However, using this standardized form may help you develop an acceptable plan and will expedite regulatory review. 〔L1506–1509〕

  > The Seafood HACCP Regulation requires that all seafood processors conduct, or have conducted for them, a hazard analysis to determine whether there are food safety hazards that are reasonably likely to occur in their product and to the preventive measures that a processor can apply to control those hazards (21 CFR 123.6(a)). 〔L1520–1527〕

- 违反后果 / 反例：
  - 跳过 STEP 3/4（分销方式、预期用途与消费者）直接判显著性 → STEP 10 的 L1808–1812 失去输入，即食/非即食、婴幼儿/成人被同质化处理。
  - 直接从 STEP 7 跳到 STEP 13 设关键限值，未经 STEP 10 显著性与 STEP 11 CCP 判定 → 判定链断裂，关键限值无对应 CCP。
  - 把 18 步当作法定程序，认定「未逐步填写 Appendix 1 表格即违法」→ 与 L1506–1507 相反；法条只要求危害分析与 HACCP 计划的结果。
  - Column 3 = No 的步骤仍继续填 STEP 12–18，或 Column 6 = No 的步骤仍设监控记录 → 违反跳过规则，制造无意义的计划条目。
- 与 CAP-22 法条层的区分：CAP-22 描述的是「必须有什么」（危害分析、书面 HACCP 计划、七大要素、CCP 关键限值等法条结果），本单元描述的是「按什么顺序、用哪张表、哪一格填什么、何时可以停」的**操作序列**。18 步清单与 6 列工作表是指南提供的实现路径，法条既不规定顺序也不强制表格；把路径当法条、或把法条结果当路径，都是两层混淆。

---

## P-07 关键限值须科学论证充分性；指南里的数字不是 FDA 新设限值（外部法源回指）

- 类型：充分性论证义务 / 引用与法源归属口径
- 依据行号：
  - L120–126（Ch.1「Scope and Limitations」，替代控制策略与科学论证义务）
  - L21340–21362（Ch.13 蒸煮/巴氏杀菌，「scientifically established process」与 EPIPT 验证，跨章复现同一义务）
  - L715–717（导言修订摘要，Ch.9 Table 9-1 被移除、改为在 Appendix 5 中「as a reference」引用）
  - L27442–27448（Appendix 5 导言，levels 的性质与「may not always be suitable for critical limits」）
  - L27450–27550（Appendix 5 表格 References 列，外部法源清单；表内数值按口径仅描述、不逐字引用）
  - L27606–27619（Appendix 5 脚注 1、6、8、9，tolerances / NSSP / guidance levels / import tolerances 的法源标注）
  - L6827–6843（Ch.7 掺假判定回指 FD&C Act 21 U.S.C. 331/342）
  - 跨导言、Ch.1、Ch.7、Ch.13、Appendix 5 五个独立区域。
- 原则表述：
  1. **自选限值的义务**：可用其他控制策略/关键限值，但须 scientifically establish their adequacy（L124–126）；Ch.13 把这一义务具体化为 process validation——温度分布研究找冷点、热穿透研究取最慢加热单元、识别影响升温的关键因子、且 EPIPT 只能在科学研究覆盖的条件下使用（L21340–21362）。
  2. **附录数值的性质**：Appendix 5 明列的是 **FDA 与 EPA 既有安全水平**，多数是「agency could take legal action 的执法触发点」，因此 **may not always be suitable for critical limits**；脚注 1 明说这些值是 **tolerances**（21 CFR 109 / 556、40 CFR 180），脚注 8 明说 **Guidance levels are not intended to be identified in the HACCP plan as a control measure**。故「指南里的数字」既不是 FDA 在本指南中新设的限值，也不自动等于关键限值。
  3. **外部法源回指清单**（来自 L27450–27550 表格 References 列与 L27608–27619 脚注，仅作归属描述）：
     - **CPG（Compliance Policy Guide）**：Sec. 540.525（组胺）、540.250（PSP）、540.600（甲基汞）、555.300（沙门氏菌）、555.425（硬质异物）、575.100（有机氯农药）；Compliance Program 7303.842（金葡菌 / PSP）。
     - **21 CFR**：Part 556 系列（兽药残留 tolerance，如 556.500 / 556.118 / 556.283 / 556.640 / 556.660）、21 CFR 109、21 CFR 172.140、21 CFR 117.3（RTE 定义引用）、21 CFR 113（LACF，见 P-09）。
     - **40 CFR Part 180 系列**：EPA 农药残留 tolerance（如 180.142 / 180.445 / 180.169 / 180.364 / 180.472 等）。
     - **NSSP Guide for the Control of Molluscan Shellfish**：弧菌与海洋生物毒素的判定与批准方法（脚注 6 回指）。
     - **其他**：ICMSF 1996 等科学文献、Import Tolerance（进口耐受量，脚注 9）、FD&C Act 21 U.S.C. 342 掺假条款。
     - 版本沿革佐证：第 4 版把 Ch.9 原 Table 9-1（action and tolerance levels）**移除**，改为「included as a reference in Appendix 5」（L715–717），说明 Appendix 5 的定位是**法源索引**而非新设标准。
  4. **无既设水平也不免责**：Regardless of an established level or not，FDA 仍可依 FD&C Act 对掺假食品采取法律行动（L27445–27448）；Ch.7 亦强调分解鱼即使不形成组胺，也因 21 U.S.C. 342 掺假而禁止州际流通（L6827–6843）。

  > Processors may choose to use other control strategies, as long as they comply with the requirements of the applicable food safety laws and regulations. However, processors that chose to use other control strategies (e.g., critical limits) should scientifically establish their adequacy. 〔L120–126〕

  > This appendix lists FDA and EPA levels relating to safety attributes of fish and fishery products. In many cases, these levels represent the point at which the agency could take legal action to include removing product from market. Consequently, the levels contained in this table may not always be suitable for critical limits. 〔L27442–27444〕

  > Regardless of an established level or not, FDA may take legal action against food deemed to be adulterated as defined by the Federal Food, Drug and Cosmetic Act (FD&C Act) [21 U.S.C. 342]. A food is adulterated if the food bears or contains any poisonous or deleterious substance which may render it injurious to health under section 402 (a)(1) of the FD&C Act. 〔L27445–27448〕

  > These values are tolerances. (Reference: 21CFR 109, 21CFR 556 and 40 CFR 180). 〔L27608〕

  > Guidance levels are not intended to be identified in the HACCP plan as a control measure. 〔L27618〕

  > Removed Table 9-1 (action and tolerance levels) which has been included as a reference in Appendix 5. 〔L715–717〕

- 违反后果 / 反例：
  - 把 Appendix 5 中某农药/兽药数值直接抄成 HACCP 计划的 critical limit，且未做充分性论证 → 违反 L27443–27444 与 L27618；执法触发水平 ≠ 过程控制限值。
  - 引用「FDA 规定组胺不得超过 50 ppm」却不标注其外部法源实为 CPG Sec. 540.525，或把 40 CFR 180 的 EPA 农药耐受量说成「FDA 海产品 HACCP 新设限值」→ 法源归属错误。
  - 自选巴氏杀菌 EPIPT 值却未做温度分布/热穿透研究、未在验证覆盖条件下使用 → 违反 L21347–21365 的科学验证要求。
  - 因「Appendix 5 没有列出某污染物」就认定可放行 → L27445–27448 明确无既设水平时 FDA 仍可依掺假条款执法。
- 与 CAP-22 法条层的区分：CAP-22 的强制义务来自 **21 CFR Part 123**（要求每个 CCP 设关键限值、并须有支持性依据）。本单元涉及的数字**法源在 Part 123 之外**——CPG、21 CFR 556 / 109 / 172 / 113、40 CFR 180、NSSP Guide、ICMSF、FD&C Act——且指南明确这些水平「不总是适合作为关键限值」「guidance levels 不作控制措施」。因此：法条层回答「关键限值必须有、必须有依据」，指南层回答「依据可以来自哪里、附录里的数字能不能直接拿来用、自选限值要做什么验证」。引用任一数值时须注明外部法源，不得表述为 FDA 在本指南中新设的限值。

---

## P-08 数值型控制参数的不可互换性：冻结三条件 / 6 英寸例外 / 盐渍无效；组胺 50 ppm 与 500 ppm 的分野

- 类型：参数成套性规则 / 数值口径
- 依据行号：
  - L4668–4691（Ch.5 寄生虫，影响因素 + 三组冻结条件 + 6 英寸例外，散文段落）
  - L4692–4708（Ch.5 盐渍/醋渍、修剪/烛光/物理去除均不能消除危害，散文段落）
  - L6850–6854（Ch.7 组胺，50 ppm guidance level 与 500 ppm 的散文表述）
  - L6831–6843（Ch.7 分解掺假与组胺形成的区分，散文段落）
  - L589（导言修订摘要，≥50 ppm 拒收的散文表述）
  - L6483（Ch.7 背景散文，提及 often above 500 ppm）
  - L27547（Appendix 5 表格「≥500 ppm toxic / ≥50 ppm decomposed」，**表格内容仅描述、不逐字引用**）
  - 跨 Ch.5、Ch.7、导言、Appendix 5 四个独立区域；所有逐字数值均取自散文段落。
- 原则表述：**数值参数是不可拆配的成套条件，且不同性质的阈值不可互换。**
  1. **Ch.5 寄生虫冻结是三组「温度 × 时间」的 OR 充分条件，任一组内部参数不可拆配互换**（L4681–4689）：
     - (a) -4°F (-20°C) 或以下冷冻并储存 **7 天（total time）**；
     - (b) -31°F (-35°C) 或以下冻至坚实，并在 -31°F (-35°C) 或以下储存 **15 小时**；
     - (c) -31°F (-35°C) 或以下冻至坚实，并在 -4°F (-20°C) 或以下储存 **24 小时**。
     - 三者各自成套：不能把 (b) 的「15 小时」配到 (a) 的 -20°C，也不能把 (c) 的「固化后 -20°C」拆成单独条件。效果还受冻至坚实所需时长、保持时长、鱼种/来源、寄生虫种类影响（绦虫比线虫敏感、吸虫比线虫耐受，L4668–4679）。
     - **6 英寸例外**：these conditions may not be suitable for freezing particularly large fish (e.g., thicker than 6 inches)——厚度是隐含的适用边界，不能对大鱼无条件套用三组参数。
     - **不可替代**：盐渍/醋渍只能 reduce、不能 eliminate 或 minimize to an acceptable level（线虫幼虫在 80° salinometer 盐水、21% 重量比盐中可存活 28 天）；修剪腹鳍、烛光检查、物理剔除同样不能彻底消除（L4692–4708）。
  2. **Ch.7 / Appendix 5 组胺双阈值性质不同，不可混用**（散文取数）：50 ppm 是 **guidance level / 分解（decomposed）指示水平**——在一份鱼或一批中某部位检出 50 ppm，其他部位可能超过 500 ppm；500 ppm 是 **toxic（毒性）水平**。Appendix 5 表格把二者并列为「≥500 ppm - toxic; ≥50 ppm - decomposed」（L27547，仅描述），导言修订摘要把 ≥50 ppm 用作拒收触发（L589），但二者法律性质不同：**分解即掺假**（21 U.S.C. 342），即使该分解类型不会导致组胺形成也禁止州际流通（L6831–6843）——因此不能把 50 ppm 当作「毒性安全线」，也不能把 500 ppm 当作「分解判定线」。

  > The effectiveness of freezing to kill parasites depends on several factors, including the temperature of the freezing process, the length of time needed to freeze the fish tissue, the length of time the fish is held frozen, the species and source of the fish, and the type of parasite present. The temperature of the freezing process, the length of time the fish is held frozen, and the type of parasite appear to be the most important factors. For example, tapeworms are more susceptible to freezing than are roundworms. Flukes appear to be more resistant to freezing than roundworms. 〔L4668–4679〕

  > Freezing and storing at an ambient temperature of -4°F (-20°C) or below for 7 days (total time), or freezing at an ambient temperature of -31°F (-35°C) or below until solid and storing at an ambient temperature of -31°F (-35°C) or below for 15 hours, or freezing at an ambient temperature of -31°F (-35°C) or below until solid and storing at an ambient temperature of -4°F (-20°C) or below for 24 hours are sufficient to kill parasites. Note that these conditions may not be suitable for freezing particularly large fish (e.g., thicker than 6 inches). 〔L4681–4691〕

  > Brining and pickling may reduce the parasite hazard in a fish, but they do not eliminate it, nor do they minimize it to an acceptable level. Nematode larvae have been shown to survive 28 days in an 80° salinometer brine (21% salt by weight). 〔L4692–4697〕

  > For this reason, a guidance level has been set of 50 ppm histamine in the edible portion of fish. If 50 ppm is found in one section of a fish or lot, there is the possibility that other sections may exceed 500 ppm. 〔L6850–6854〕

  > It is important to recognize that the Federal Food, Drug, and Cosmetic Act (the FFD&C Act) prohibits interstate commerce of adulterated foods (21 U.S.C. 331). Under the FFD&C Act, a food that is decomposed is considered adulterated (21 U.S.C 342). Accordingly, a fish or fishery product that is decomposed in whole or in part is prohibited from entering interstate commerce even if the type of decomposition may not lead to scombrotoxin (histamine) formation. 〔L6827–6843〕

- 违反后果 / 反例：
  - 「-20°C 冻 15 小时」「-35°C 冻 7 天」这类跨组拆配 → 不属于 L4681–4689 任一充分条件，寄生虫控制失效。
  - 对厚度超过 6 英寸的大鱼直接套用三组参数，未考虑冻至坚实所需时长 → 中心未达标。
  - 用盐渍/醋渍/烛光剔除替代冻结作为寄生虫控制策略 → 与 L4692–4708 明确冲突，不能 minimize to an acceptable level。
  - 把 50 ppm 当作「毒性阈值」并据此放行分解鱼，或把 500 ppm 当作「分解判定线」→ 混淆 guidance level 与 toxic level，且忽略分解即掺假的独立法律后果。
  - 从 Appendix 5 表格（L27547）逐字引数值充当「FDA 限值」→ 表格内容按本卡口径只描述、不逐字引用，且法源为 CPG Sec. 540.525（见 P-07）。
- 与 CAP-22 法条层的区分：21 CFR Part 123 **不规定任何具体温度/时间/ppm 参数**，只要求 CCP 有关键限值且有依据。三组冻结条件、6 英寸例外、50/500 ppm 双阈值均属指南层的**技术参数与充分性示范**；而「分解食品禁止州际流通」来自 FD&C Act 21 U.S.C. 342（法规层，见 P-07 法源回指）。能力卡须把「参数可作关键限值的候选来源」与「法条强制的参数义务」分开，避免把指南推荐数值表述为法定限值。

---

## P-09 主体与范围边界：不覆盖消费者/零售、不提供 retorting、市场名称归 Seafood List

- 类型：适用范围边界 / 外部机构回指
- 依据行号：
  - L92–95（导言，消费者与零售 establishments 的排除声明）
  - L4660–4667（Ch.5，retorting 归 21 CFR 113 LACF 法规）

  - L2135–2143（Ch.3 表下 NOTES，可接受市场名称与 The Seafood List 的分工）
  - L2144–2156（Ch.3 表下 NOTES，濒危物种归 NOAA / USFWS）
  - 4 个独立散文段落，跨导言、Ch.3、Ch.5。
- 原则表述：本指南的适用主体是 **fish and fishery products 的加工者（processor）** 及联邦/州监管人员（L96–99），并明确划出四条外边界：
  1. **不专门针对消费者或零售企业的安全操作**（does not specifically address safe handling practices by consumers or by retail establishments），但许多概念对二者仍适用。
  2. **不提供 retorting（低酸罐头热力杀菌）信息**——该部分归 21 CFR 113（LACF Regulation），指南只讲到 Ch.16 蒸煮/巴氏杀菌。
  3. **可接受市场名称的判定归 The Seafood List**（FDA Seafood List），本指南不是 official resource；标注须用可接受名称，跨州贸易物种以 Seafood List 为准。
  4. **濒危物种与监管限制归 NOAA「ESA Threatened & Endangered」清单和 USFWS「Endangered Species」**，并附物种替代（species substitution）可能构成经济欺诈/错误标识、并导致食品安全危害被漏判的提示（L2157–2166）。
  - 共同口径：指南在边界处一律**回指外部法源或外部机构**，不自行扩张适用范围。

  > The guidance does not specifically address safe handling practices by consumers or by retail establishments, although many of the concepts contained in this guidance are applicable to both. 〔L92–95〕

  > Regulatory requirements for retorting (i.e., thermal processing of low acid canned foods) are contained in the Thermally Processed Low-Acid Foods Packaged in Hermetically Sealed Containers regulation, 21 CFR 113 (hereinafter, the Low-Acid Canned Foods (LACF) Regulation). This guidance does not provide further information on retorting. 〔L4660–4667〕

  > Acceptable names should be used when labeling seafood products. Refer to "The Seafood List" to determine acceptable names for species subject to interstate commerce. This Guide is not the official resource for determination of acceptable names. 〔L2135–2140〕

  > Some species are endangered and/or have regulatory restrictions. For information concerning endangered species, please refer to National Oceanic and Atmospheric Administration (NOAA) "ESA Threatened & Endangered" list and/or the U.S. Fish & Wildlife Services "Endangered Species". 〔L2144–2150〕

- 违反后果 / 反例：
  - 用本指南给零售门店/家庭消费者设定「合规义务」→ 超出 L92–95 的主体边界。
  - 在本指南里查找低酸罐头 retorting 的关键限值与杀菌规程 → 该内容归 21 CFR 113，本指南明确不提供。
  - 用本指南的物种表当作「可接受市场名称」的官方依据来判定错误标识 → 与 L2139–2140 直接冲突，须查 The Seafood List。
  - 忽略物种替代（species substitution）导致的危害漏判，或未把濒危物种问题回指 NOAA/USFWS。
- 与 CAP-22 法条层的区分：21 CFR Part 123 的适用主体是 **processor（加工者）**，法条层界定「谁必须做危害分析、谁必须有 HACCP 计划」。本单元是**指南自身的内容范围声明**：它不覆盖消费者/零售、不写 retorting、不充当命名权威、不判定濒危物种。两层边界方向不同——法条层用「主体」划定义务，指南层用「内容回指」划定不写什么；且回指对象（21 CFR 113、Seafood List、NOAA/USFWS）多在 Part 123 之外。

---

## P-10 版本口径：封面 June 2022 与分章页脚 June 2021 属分章滚动修订

- 类型：版本与引用口径
- 依据行号：
  - L1–L23、L52、L77、L146–147、L242–243、L327–328、L419–420、L515–516、L619–620、L719–720（封面标题与导言 G-1…G-12 页脚，均标 **June 2022 Edition**）
  - L2160（Ch.3 页脚「3 - 1 (June 2021)」）
  - L25886（Appendix 3 页脚「Tree A3 - 1 (June 2021)」）
  - L27452、L27468、L27480、L27493、L27505、L27522、L27537、L27551、L27590、L27602（Appendix 5 各页脚「A5 - 1 … A5 - 12 (June 2021)」）
  - L695–L701（导言修订摘要，以「Chapter 9 … modified … as of June 2022」形式按章列出改动）
  - L715–L717（导言修订摘要，Ch.9 Table 9-1 移除并入 Appendix 5 作 reference）
  - 版本标识分布于封面、导言页脚、Ch.3、Appendix 3、Appendix 5、修订摘要等多个独立区域。
- 原则表述：本导出件为 **June 2022 Edition（第 4 版）整册**，封面与导言 G 页页脚统一标 June 2022；但**具体章节/附录沿用各自最近一次修订的页脚日期（June 2021）**，Ch.3、Appendix 3、Appendix 5 均如此。导言修订摘要进一步以「按章列改动」的方式记录 2022 版变化（如 Chapter 9 更名、Table 9-1 移除并入 Appendix 5）。
  - 因此口径是：**整册版本号 ≠ 各章内容修订时点**，属分章滚动修订（rolling chapter-level revision）。引用时应标注「June 2022 Edition, 第 X 章，页脚 June 2021」，不能仅凭封面 June 2022 断言全册内容均为 2022 年新修，也不能因某章页脚是 June 2021 就否认它属于第 4 版。
  - 修订摘要本身也说明版本差异落在具体章节（章标题、链接、EPA 要求说明、表格归并），而非全册同步重写。

  > "Including Pesticides" has been modified with the following recommendations as of June 2022: - Title of the Chapter has changed from: "and Pesticides" to "Including Pesticides" since pesticides are a subset of chemicals. - Language in the chapter has been updated to reflect the chapter title change. 〔L695–701〕

  > Removed Table 9-1 (action and tolerance levels) which has been included as a reference in Appendix 5. 〔L715–717〕

- 违反后果 / 反例：
  - 引用 Appendix 5 的限值时写「FDA 2022 年 6 月新发布的安全水平」→ 该附录页脚为 June 2021，且内容为既有法源回指（见 P-07），既非 2022 新增、也非新设限值。
  - 因 Ch.3 页脚是 June 2021 就判定「这部分不属于 June 2022 第 4 版」→ 混淆整册版本与分章修订时点。
  - 比较第 3 版与第 4 版差异时只看封面日期，未利用导言修订摘要的按章改动清单（L695–L717），导致漏记 Chapter 9 更名与 Table 9-1 归并。
- 与 CAP-22 法条层的区分：CAP-22 引用的 21 CFR Part 123 属**法规**，其版本以 CFR 年度版 / eCFR 现行文本为准，修订通过 Federal Register 规则制定程序，具有确定的生效日期。本单元的 June 2022 / June 2021 是**指南文件的版本标识**，通过页脚与修订摘要体现，不产生法规效力、不设生效日期。两类「版本」不可互相校对或互相替代：不能用指南页脚日期推断法规修订时间，也不能用法典版本去否定指南的章节滚动修订事实。

---

## 覆盖率自查

| 提取要求 | 对应候选单元 | 关键行号是否覆盖 | 独立段落数 |
| --- | --- | --- | --- |
| 1. 非约束性三层边界（不设可执行责任 / should / 替代策略须科学论证 / 表不单独用 / 不替代危害分析 / 新危害警觉） | P-01（主）、P-02 | L100–108、L115–126、L127–144、L92–95 | 4 |
| 2.「无控制条件下判定」+ 两例分岔 | P-03 | L1716–1731、L1780–1789、L6945–6955、L14451–14481、L29820–29827 | 5 |
| 3. Yes/No 都写理由 / 显著≠该步控制 / 逐步独立评估 | P-05、P-04 | L1796–1827、L1828–1870、L1534–1540、L6956–6966、L14462–14494 | 6 |
| 4. 表不可单独用 + 自身/外部专家补表外危害（全部重复位置） | P-02 | L127–136、L137–144、L1709–1719、L1753–1760、L2128–2134（共 5 处，已穷举） | 5 |
| 5. 关键限值充分性论证 + Appendix 5 外部法源回指（CPG 540.525 / 21 CFR 556 / 40 CFR 180 / NSSP Guide） | P-07 | L120–126、L715–717、L21340–21362、L27442–27448、L27450–27550、L27606–27619、L6827–6843 | 7 |
| 6. 数值型控制参数不可互换（冻结三条件 / 6 英寸 / 盐渍无效 / 组胺 50·500 ppm） | P-08 | L4668–4708、L6827–6843、L6850–6854、L589、L6483、L27547 | 6 |
| 7. 主体与范围边界（消费者/零售 / retorting / Seafood List） | P-09 | L92–95、L4660–4667、L2135–2143、L2144–2156 | 4 |
| 8. 版本口径（封面 2022 / 分章页脚 2021） | P-10 | L1–23、L146–147、L2160、L25886、L27452 及 A5-2…A5-12、L695–717 | 多区域 |
| 附加：用户要求「完整危害分析判定链」 | P-06 | L1500–1540、L1555–2085（STEP 1–18）、L25774/L25783、L25884–25893、L29810–29827 | 5 |

- 候选单元总数：**10**（在 8–12 区间内，宁精勿滥；P-01–P-10 各自主题独立，无重复拆项）。
- 每个单元「依据行号」均列出 ≥2 个独立散文段落；其中 P-02、P-03、P-07 为跨章节反复强调型，已标注全部重复位置。
- 英文引用块：全部取自散文段落（含导言修订摘要、表下 NOTES、脚注等散文性文字），每段 ≤100 词并标行号；**Appendix 5 表格（L27450–27550）、Appendix 1 工作表列头（L25774/L25783）、Ch.7 控制策略表中的数值一律仅作中文描述、未逐字引用**。
- 表格数值逐字引用自查：P-07、P-08 中出现的 50 ppm / 500 ppm 取自 L6850–6854、L589、L6483 等散文段落；Ch.5 的 -4°F / -31°F / 7 days / 15 hours / 24 hours / 6 inches / 80° salinometer / 21% 取自 L4681–4697 散文段落；L27547 表格行仅以中文描述其并列关系，未逐字抄录。
- 与 CAP-22 区分：10 个单元全部填写该字段，统一口径为「CAP-22 = 21 CFR Part 123 法条义务层（shall / must / 强制、违规即法规不符合）；本卡 = 技术指南层（should / 建议 / 可替代 / 须科学论证 / 外部法源回指）」，并逐单元点明具体分界证据（如 L1506–1507 表格非法条强制、L1534–1540 书面化法条不要求、L1852–1854 的 must 源于回指 123.6(c)(2)、L29820–29827 法规原文重印）。
- 未覆盖/已排除项：L28306「they should not be used」经复核为过敏原原料隔离标签语境（L28298–28307），与本批原则无关，未纳入；L13100「prudent processor」为一般性举例，未单独成单元，其法定定义已由 P-03 的 L1780–1789 / L29820–29827 承载。
- 只写入本文件，未修改包内其它任何文件。
