# 海产品危害分析与控制的技术指南层：完整危害分析判定链（seafood-hazards-controls-guide）

*来源分层：本卡（CAP-23）取用**第 15 类来源**——FDA《Fish and Fishery Products Hazards and Controls Guidance》**第 4 版 June 2022**（SGR 129，本地 `source-seafood-hazards-guide-2022.md`，导出全文 1,709,446 字节 / 约 31,321 行）。它是 21 CFR Part 123（Seafood HACCP Regulation）与 Part 1240 的**配套技术指南层**：负责 how to 判定，即怎么识别危害、怎么在**无控制条件下**判 `reasonably likely to occur`、怎么填六栏工作表、怎么定 CCP 与关键限值。它**不具法律约束力**，`should` 只是建议，企业可另选控制策略但须科学论证其充分性；凡法定义务、法定时限、条款级判定一律回〔§ 123.xxx〕／CAP-22，本卡只给方法论与建议参数。*

*与 CAP-22 `seafood-haccp-statutory-requirements` 是**配对而非合并**：CAP-22 是**法条义务层**（21 CFR Part 123，`shall`／违反即法规不符合）；本卡是**指南建议层**（`should`／推荐／可替代／须科学论证）。必须同时防两个方向的误读：① 把指南当法规、把 `should` 读成 `shall`、把控制策略示例与 Appendix 5 数值当合规清单；② 因「指南非强制」就把 Part 123 的 `shall` 义务稀释成可选。指南内凡出现 `must`／`require`（如「每个显著危害至少一个 CCP」）几乎都是回指 21 CFR 123.6(c)(2)，其强制力来自法规而非指南。二者不可互相替代，也不得把二者合并成一张「合规清单」。*

*全包自 v4.10 起「**十五类来源不可混引**」。本卡引用一律写「Seafood Hazards Guide 第 4 版 Ch.x / Appendix x / L####」（L 号以原始导出全文 `seafood_guide.md` 为准），法条一律写〔§ 123.xxx〕，**两者不可互换**，不得把指南章号写成条款号，也不得把指南内的法规转录（Appendix 8 / Addendum 1 / Additional Document 1–2）当作独立法源。层次为：法规正文 ＞ FDA 指南 ＞ CPGM／CP／IOM 检查程序（仅检查员视角）。*

*正文本包**仍未收**：CP 7303.842（海产品检查程序）、NSSP Guide（软体贝类）、21 CFR part 120（果汁 HACCP）／part 1240（贝类卫生）／part 108／part 110／part 507、Import Alert 16-xx 系列、BAM 海产品章节，以及本指南 Appendix 5 回指的 CPG Sec. 540.525／555.300／575.100、21 CFR 556 系列、40 CFR 180 系列、Import Tolerance 等外部法源。涉及其具体数值与条款级结论一律标「转引未收」。本卡与 `hazard-analysis-method`、`chemical-hazard-controls`、`process-control-validation`、`allergen-program`、`inspection-sampling` 各有分工，见 B12。*

## R — 原文

**① 效力边界：指南不设可执行责任、`should` 只是建议、替代策略须科学论证、版次声明（逐字）**：

> "FDA’s guidance documents, including this guidance, do not establish legally enforceable responsibilities. Instead, guidance describes the Agency’s current thinking on a topic and should be viewed only as recommendations, unless specific regulatory or statutory requirements are cited."
> —— Seafood Hazards Guide 第 4 版 Ch.1 / L100–105

> "The use of the word “should” in Agency guidance means that something is suggested or recommended, but not required."
> —— Seafood Hazards Guide 第 4 版 Ch.1 / L105–108

> "The control strategies and practices provided in this guidance are recommendations to the fish and fishery products industry unless they are required by regulation or statute. This guidance provides information that would likely result in a HACCP plan that is acceptable to FDA. Processors may choose to use other control strategies, as long as they comply with the requirements of the applicable food safety laws and regulations. However, processors that chose to use other control strategies (e.g., critical limits) should scientifically establish their adequacy."
> —— Seafood Hazards Guide 第 4 版 Ch.1 / L115–126

> "This is the fourth edition of the Food and Drug Administration’s (FDA’s) “Fish and Fishery Products Hazards and Controls Guidance.”"
> —— Seafood Hazards Guide 第 4 版 Ch.1 / L1444–1446

**② 识别层：表不可单独用、指南不替代危害分析、须叠加章节与专家、表非穷尽（逐字）**：

> "The information contained in the tables in Chapter 3 and in Chapters 4 through 21 provide guidance for determining which hazards are “reasonably likely to occur” in particular fish and fishery products under ordinary circumstances. However, the tables should not be used separately for this purpose. The tables list potential hazards for specific species and finished product types. This information should be combined with the information in the subsequent chapters to determine the likelihood of occurrence."
> —— Seafood Hazards Guide 第 4 版 Ch.1 / L127–136

> "The guidance is not a substitute for the performance of a hazard analysis by a processor of fish and fishery products, as required by FDA’s regulations. Hazards not covered by this guidance may be relevant to certain products under certain circumstances. In particular, processors should be alert to new or emerging problems (e.g., the occurrence of natural toxins in fish not previously associated with that toxin)."
> —— Seafood Hazards Guide 第 4 版 Ch.1 / L137–144

> "The tables provide lists of potential hazards. You should use the tables, together with the information provided in Chapters 4 through 21, and your own expertise or that of outside experts, to determine whether the hazard is significant for your particular product or process and, if so, how it should be controlled."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L2128–2134

> "Tables 3-2 and 3-3 include the best information currently available to FDA concerning hazards that are specific to each species of fish. You should use your own expertise, or that of outside experts, as necessary, to identify any hazards that may not be included in the table (e.g., those that may be new or unique to your region)."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1709–1715

**③ 建表与书面化：18 步、表格非法条强制、危害分析书面化非强制（逐字）**：

> "This guidance document is designed to walk you through a series of 18 steps that will yield a completed Hazard Analysis Critical Control Point (HACCP) plan."
> —— Seafood Hazards Guide 第 4 版 Ch.2 / L1492–1497

> "The regulation does not require that you use the form included in Appendix 1. However, using this standardized form may help you develop an acceptable plan and will expedite regulatory review."
> —— Seafood Hazards Guide 第 4 版 Ch.2 / L1506–1510

> "The Seafood HACCP Regulation does not require that the hazard analysis be kept in writing. However, FDA expects that a written hazard analysis will be useful when you perform mandatory HACCP plan reassessments and when you are asked by regulators to justify why certain hazards were or were not included in your HACCP plan."
> —— Seafood Hazards Guide 第 4 版 Ch.2 / L1534–1540

**④ 显著性闸门的前提：无控制条件下判定与组胺两情形分岔（逐字）**：

> "You may already have effective controls in place for a number of these hazards as part of your routine or traditional handling practices. The presence of such controls does not mean that the hazard is not significant."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1715–1719

> "The likelihood of a hazard occurring should be judged in the absence of controls. For example, the fact that scombrotoxin (histamine) development in a particular species of fish has not been noted may be the result of (1) the inability of the fish to produce histamine or (2) the existence of controls that are already in place to prevent its development (e.g., harvest vessel time and temperature controls)."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1720–1727

> "In the first case, the hazard is not reasonably likely to occur. In the second case, the hazard is reasonably likely to occur, and the controls should be included in the HACCP plan."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1728–1731

**⑤ 判定尺：reasonably likely to occur 的法定定义转引与 significant 的等价（逐字）**：

> "The Seafood HACCP Regulation defines a food safety hazard that is reasonably likely to occur as “one for which a prudent processor would establish controls because experience, illness data, scientific reports, or other information provide a basis to conclude that there is a reasonable possibility that it will occur in the particular type of fish or fishery product being processed in the absence of those controls.”"
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1780–1789

> "Narrow the list of potential hazards that you entered in Column 2 of the Hazard Analysis Worksheet to those that are significant or, in other words, “reasonably likely to occur.”"
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1776–1779

**⑥ 显著性逐步判定：按步骤独立评估、三情形（L1796–1808）、预期用途、累积效应（逐字）**：

> "You should evaluate the significance of a potential hazard independently at each processing step. It may be significant at one step but not at another."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1795–1798

> "A potential hazard is significant at the processing or handling step if (1) it is reasonably likely that the hazard can be introduced at an unsafe level at that processing step; or (2) it is reasonably likely that the hazard can increase to an unsafe level at that processing step; or (3) it is significant at another processing or handling step and it can be prevented, eliminated, or reduced to an acceptable level at the current processing or handling step."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1799–1808

> "When evaluating the significance of a hazard at a processing step, you should consider the method of distribution and storage and the intended use and consumer of the product, which you developed in Steps 3 and 4."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1808–1812

> "Time and temperature abuse that occurs at successive processing and storage steps may be sufficient to result in unsafe levels of histamine, even when abuse at one step alone would not result in such levels. For this reason, you should consider the cumulative effect of time and temperature abuse during the entire process. Information is provided above to help you assess the significance of time and temperature abuse that may occur in your process."
> —— Seafood Hazards Guide 第 4 版 Ch.7 / L6956–6966

**⑦ 落表与衔接：Yes/No 都写理由、显著不等于该步控制（逐字）**：

> "If you determine that a potential hazard is significant at a processing step, you should answer “Yes” in Column 3 of the Hazard Analysis Worksheet. If you determine that a potential hazard is not significant at a processing step, you should answer “No” in that column. You should record the reason for your “Yes” or “No” answer in Column 4. You need not complete Steps 11 through 18 for a hazard for those processing steps where you have recorded a “No.”"
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1813–1822

> "It is important to note that identifying a hazard as significant at a processing step does not mean that it must be controlled at that processing step. Step 11 will help you determine where in the process the critical control point is located."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1823–1827

**⑧ 定位层：Step 11 判定树、控制策略示例 CCP 漂移、至少一个 CCP、判定树不可完全依赖（逐字）**：

> "For each processing step where a significant hazard is identified in Column 3 of the Hazard Analysis Worksheet, determine whether it is necessary to exercise control at that step in order to control the hazard. Figure A-2 (Appendix 3) is a critical control point (CCP) decision tree that can be used to aid you in your determination."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1828–1836

> "Each chapter discusses one or more “control strategy example(s)” for how the hazard can be controlled, because there are often more ways than one to control a hazard. CCP(s) for one control strategy example often differ from those of another example for the same hazard."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1843–1847

> "For every significant hazard, there must be at least one CCP where the hazard is controlled (21 CFR 123.6(c)(2)). In some cases, control may be necessary at more than one CCP for a single hazard. In other cases, a processing step may be a CCP for more than one hazard. CCPs are points in the process (i.e., processing steps) where the HACCP control activities will occur."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L1852–1859

> "This appendix contains a decision tree that may be used to assist you with the identification of critical control points (CCPs). You should not rely exclusively on the decision tree, because error may result."
> —— Seafood Hazards Guide 第 4 版 Appendix 3 / L25876–25879

**⑨ 参数化层：关键限值定义、须对应监控参数、监控四问、Appendix 5 数值的性质（逐字）**：

> "For each processing step where a significant hazard is identified on the HACCP Plan Form, identify the maximum or minimum value to which a parameter of the process must be controlled in order to control the hazard."
> —— Seafood Hazards Guide 第 4 版 Ch.2 / L1891–1896

> "Consider that the critical limit should directly relate to the parameter that you will be monitoring. For example, if you intend to monitor the temperature of the water in the cooker and the speed of the belt that carries the product through the cooker (because you have determined that these factors result in the desired internal product temperature for the desired time), you should specify water temperature and belt speed as critical limits, not the internal temperature of the product."
> —— Seafood Hazards Guide 第 4 版 Ch.2 / L1921–1931

> "To fully describe your monitoring program, you should answer four questions: (1) What will be monitored? (2) How will monitoring be done? (3) How often will monitoring be done (frequency)? and (4) Who will do the monitoring?"
> —— Seafood Hazards Guide 第 4 版 Ch.2 / L1946–1950

> "This appendix lists FDA and EPA levels relating to safety attributes of fish and fishery products. In many cases, these levels represent the point at which the agency could take legal action to include removing product from market. Consequently, the levels contained in this table may not always be suitable for critical limits."
> —— Seafood Hazards Guide 第 4 版 Appendix 5 / L27442–27444

> "Guidance levels are not intended to be identified in the HACCP plan as a control measure."
> —— Seafood Hazards Guide 第 4 版 Appendix 5 / L27618

**⑩ 具体参数与适用边界：寄生虫冻结、盐渍无效、组胺双阈值、retorting 与主体范围（逐字）**：

> "Freezing and storing at an ambient temperature of -4°F (-20°C) or below for 7 days (total time), or freezing at an ambient temperature of -31°F (-35°C) or below until solid and storing at an ambient temperature of -31°F (-35°C) or below for 15 hours, or freezing at an ambient temperature of -31°F (-35°C) or below until solid and storing at an ambient temperature of -4°F (-20°C) or below for 24 hours are sufficient to kill parasites. Note that these conditions may not be suitable for freezing particularly large fish (e.g., thicker than 6 inches)."
> —— Seafood Hazards Guide 第 4 版 Ch.5 / L4681–4691

> "Brining and pickling may reduce the parasite hazard in a fish, but they do not eliminate it, nor do they minimize it to an acceptable level. Nematode larvae have been shown to survive 28 days in an 80° salinometer brine (21% salt by weight)."
> —— Seafood Hazards Guide 第 4 版 Ch.5 / L4692–4697

> "For this reason, a guidance level has been set of 50 ppm histamine in the edible portion of fish. If 50 ppm is found in one section of a fish or lot, there is the possibility that other sections may exceed 500 ppm."
> —— Seafood Hazards Guide 第 4 版 Ch.7 / L6850–6854

> "The process of heating raw fish sufficiently to kill bacterial pathogens is also sufficient to kill parasites. Guidance concerning cooking and pasteurizing to kill bacterial pathogens is provided in Chapters 13 (hot smoking) and 16 (cooking and pasteurization). Regulatory requirements for retorting (i.e., thermal processing of low acid canned foods) are contained in the Thermally Processed Low-Acid Foods Packaged in Hermetically Sealed Containers regulation, 21 CFR 113 (hereinafter, the Low-Acid Canned Foods (LACF) Regulation). This guidance does not provide further information on retorting."
> —— Seafood Hazards Guide 第 4 版 Ch.5 / L4654–4667

> "The guidance does not specifically address safe handling practices by consumers or by retail establishments, although many of the concepts contained in this guidance are applicable to both."
> —— Seafood Hazards Guide 第 4 版 Ch.1 / L92–95

> "This Guide is not the official resource for determination of acceptable names."
> —— Seafood Hazards Guide 第 4 版 Ch.3 / L2139–2140

## I — 自述

我管的是「**拿到一个具体鱼种 + 具体加工／包装／储运方式之后，按什么链、用哪张表、哪一格填什么、何时可以停，最终怎么判出 CCP 与关键限值**」——即端到端的**完整危害分析判定链**：产品描述／流程图 → Ch.3 三表识别品种相关 + 工艺相关潜在危害 → Ch.4–21 四段式理解危害 → 在无控制条件下逐步判 `reasonably likely to occur` 显著性 → Column 3/4 的 Yes/No **都写理由** → Step 11 CCP 判定树定位 → 选控制策略示例 → 定关键限值与监控四问 → 纠正措施／记录／验证／签名。它是**指南层的方法论**，不是法条义务清单，也不是可照抄的合规模板；法定义务、法定时限、条款级判定一律回〔§ 123.xxx〕／CAP-22。

我钉死六处高频误读：

1. **把指南当法规。** 指南不设 legally enforceable responsibilities，`should` = suggested or recommended, but not required（L100–108）。把 Ch.5 冻结参数、Ch.7 的 50 ppm、Appendix 5 数值说成「FDA 强制限值」，或据此开不符合项，都是把建议升格为法条。
2. **反向把 Part 123 的 `shall` 稀释成可选。** 「指南非强制」只描述指南自身，不触及 Part 123 的危害分析、书面 HACCP 计划、至少一个 CCP、纠正措施、记录与验证义务（L1852–1854 的 `must` 正因回指 21 CFR 123.6(c)(2)）。指南内凡 `must`／`require` 多属回指法条，须转 CAP-22。
3. **把 Ch.3 表单独当显著性结论，或当成穷尽清单。** 表只列 potential hazards，明文 `should not be used separately`；必须与 Ch.4–21 及自身／外部专家合并（L127–136、L2128–2134），并补表外、区域特有、厂房特有与新出现危害（L1709–1719、L1753–1760、L137–144）。「表里没打勾」不等于「不显著」。
4. **以「已有控制、从没出过事」判危害不显著。** 显著性必须在**无控制条件**下评估；已有控制有效恰恰证明该危害 `reasonably likely to occur`，应判 Yes 并把控制纳入 HACCP 计划（L1715–1731）。这是本卡最反直觉、最易与 PCHF 危害分析混淆之处。
5. **把「某步显著」直接等于「该步必须设 CCP」。** 显著是 STEP 10 的危害属性，CCP 是 STEP 11 的控制位置属性（L1823–1827）；同一危害换了控制策略示例，CCP 落点就变（L1843–1847）。
6. **把示例数值当法定终点，或随意替代关键限值却不做科学论证。** 示例数值只是「经论证的起点」；可另选控制策略／关键限值，但须 `scientifically establish their adequacy`（L115–126）。Appendix 5 的多数水平是执法触发点，`may not always be suitable for critical limits`（L27442–27444），guidance levels 更是明文不作控制措施（L27618）。

我拒绝：把 `should` 写成 `shall`；把控制策略示例／Appendix 5 数值当合规清单；代写 HACCP 计划、代填表单、判法定身份或出合规结论；从 Appendix 3 塌陷残表逐字复原判定树问答；把 Appendix 5 数值说成 FDA 在本指南中新设的限值；用本指南回答消费者／零售、retorting、可接受市场名称、濒危物种等已明确转出的问题；把指南章号与〔§ 123.xxx〕互换；混引十五类来源。

## A1 — 书中案例

**案例 1（C-01，建表实例）：某厂做「冷冻面包鳕鱼块、真空塑料袋、-18℃ 冷链分销、供一般公众充分加热后食用」，问危害分析从哪一步起。** 情境→判定链位置：STEP 2（Describe the food）／STEP 3（distribution and storage），是 STEP 7/8 查 Table 3-2/3-3 与 Table 3-4 的**检索键**，兼 STEP 4（intended use and consumer）的输入。正确结论：市场名／拉丁名、成品形态、包装类型、分销储存方式、预期用途与消费者须逐项写实；描述填错，品种维与工艺维的命中整条链从源头偏掉，后续显著性、CCP、关键限值全部失效。依据：L1542–1615（THE STEPS 清单）、L1565–1595、L1619–1630。

**案例 2（C-02，无控制二选一）：金枪鱼加工厂申诉「投产三年从未检出组胺，所以组胺不是显著危害、无需 CCP」。** 情境→判定链位置：STEP 7 与 STEP 10 之间的「无控制条件」裁决闸门。正确结论：推理反了。须追问两项事实——(1) 该鱼种本身是否不能产生组胺（可判 No、不列入计划）；(2) 从未出问题是否只因捕捞船时间／温度控制等已有控制在压制它（仍判 Yes，且这些控制**必须写进 HACCP 计划**并设 CCP）。「没出过事」是因果倒置，不得作为 Column 3 填 No 的理由。依据：L1715–1731、L1780–1789、L6945–6955（Ch.7 独立复述）。

**案例 3（C-03，熟虾做沙拉）：把虾煮熟后用来做成品海鲜沙拉，Table 3-4 该查哪一类。** 情境→判定链位置：STEP 8 按成品食品 + 包装类型查 Table 3-4。正确结论：一个产品可能同时符合多个成品类别；须同时查 `cooked shrimp` 与 `salads … prepared from ready-to-eat fishery products` 两类，把**两类各自的潜在危害全部**写入 Worksheet Column 2、并覆盖每一个加工步骤，不能只按「沙拉」一类列危害。依据：L1732–1752（核心 L1741–1752）、L1753–1760。

**案例 4（C-04，物种替换）：一批进口原料报「Monkfish」，供应链证据显示实为 Puffer Fish。** 情境→判定链位置：STEP 2 物种身份 → STEP 7 按 Table 3-2 查品种相关危害，属输入完整性校验。正确结论：市场名是查表的唯一入口，名称一错 STEP 7 整栏作废——按错名会漏掉河豚毒素／麻痹性贝毒，凭空多出寄生虫；须把物种身份核验（供应链／标签一致性）前置为 STEP 2 输入前提。可接受市场名的权威判定归 The Seafood List（L2135–2140），本指南不是该用途官方来源。依据：L2157–2170（Species substitution 段与 Table 3-1 表前说明）、L2162–2181（表体因导出件字符粘连，仅作中文描述不作逐字引用）。

**案例 5（C-05，寄生虫）：「青柠汁腌鲷鱼 + 冷熏」即食拼盘，厂方只有 -20℃ 冷库、无 -35℃ 速冻。** 情境→判定链位置：STEP 9（Ch.5 理解危害发生条件与控制手段）→ STEP 10（显著性）→ STEP 13（关键限值）→ STEP 14（监控）。正确结论：拟生食的含寄生虫鱼种应判显著；三组冻结条件任取其一即可作关键限值候选（-4°F(-20°C) 7 天／-31°F(-35°C) 冻实后同温 15 小时／-31°F 冻实后 -4°F(-20°C) 24 小时），监控库温与时长；**盐渍／醋渍／柠檬汁腌渍、修剪腹肉、灯检挑虫只减量、不能消除或降到可接受水平，不得作为独立 CCP**；厚于 6 英寸的大鱼参数可能不适用，须单独验证冻结曲线。依据：L4637–4652（涉疫产品清单）、L4668–4691、L4692–4708。

**案例 6（C-06 / C-07 / C-09，控制策略与 CCP 漂移）：一级加工商接收本地捕捞 grouper（雪卡毒素），或养殖罗非鱼进口商（环境化学污染物／农药／养殖药物），可从源头控制、供应商证书、第三方认证、逐批检测等多条策略里选。** 情境→判定链位置：STEP 11（Identify CCPs）与 STEP 13–17（关键限值／监控／纠偏／记录／验证）。正确结论：同一危害因所选控制策略不同，CCP 位置（Pre-harvest / Receiving / Finished product labeling）与监控对象（捕捞区状态／证书是否存在／标签信息／鱼体实测残留量）随之改变，`CCP(s) for one control strategy example often differ from those of another`（L1843–1847）；各章示例表只是「仅供说明」的骨架，实际计划须另行指定具体污染物、取样方案、分析方法并做验证。依据：L5945–6123（Ch.6 Ex.1/Ex.2）、L10191–11009（Ch.9 Ex.1–7）、L13050–13614（Ch.11 Ex.1–5）、L1837–1847。

**案例 7（C-10，过敏原／亚硫酸盐 CCP 前移）：冷冻去壳虾成品标签未声明亚硫酸盐，厂方把 CCP 设在「成品贴标」并逐张核对标签。** 情境→判定链位置：STEP 2（标签是否声明）→ STEP 8 → STEP 11，是「输入条件改变导致 CCP 位置改变」的范例。正确结论：标签未声明时 CCP 应前移到**原料接收**（检测进厂虾亚硫酸盐残留或查供应商声明，关键限值 <10 ppm），成品贴标环节**不需要**为该危害再设 CCP；若厂方改为在标签上声明亚硫酸盐，控制点才落到标签。依据：L24200–24281（斜体实例 L24245–24254）、L24537–24614（Table 19-4／19-5）、L24402–24403；与 `allergen-program` 的分工见 B12。

**案例 8（C-11，流程图）：为「冷冻三文鱼片」画出 Figure A-1 式 12 框流程图后，18 步里紧接着做什么。** 情境→判定链位置：STEP 5（Develop a flow diagram）的产出 → STEP 6（Set up the Worksheet）→ STEP 7/8。正确结论：12 个框（Receiving → … → Frozen Storage）逐一抄进 Worksheet Column 1（框的数量与顺序决定 Column 1 行数），每个框在 Column 2 逐行登记潜在危害，Refrigerated Storage 与 Frozen Storage 两个框都须登记；CCP 只能落在流程图里真实存在的步骤上。注意 12 步是产品流程图、18 步是建表流程，二者不可混。依据：L1657–1669、L1671–1675、L1705–1708、L1737–1740、L25824–25883（Figure A-1 为逐格表格框，按红线仅描述不作逐字引用）；STEP 6–8 输入关系同 F-08。

## A2 — 未来触发

1. 用户问「拿到一个具体海产品怎么做完整危害分析／判定链从哪开始」→ 本卡主干 F-08 端到端链（STEP 1–18），先给链序再逐步展开。
2. 用户问「怎么描述食品／分销储存／预期用途／消费者」→ STEP 1–4（本卡）；字段是 Table 3-2/3-3/3-4 的检索键，填错整链偏掉。
3. 用户问「流程图怎么画／要不要现场核实」→ STEP 5 与 Appendix 2 Figure A-1（本卡）；流程图须覆盖接收至分销全部步骤及非鱼配料的接收与储存。
4. 用户问「品种相关危害与工艺相关危害怎么分、查哪张表」→ Table 3-2（脊椎）／3-3（无脊椎）与 Table 3-4（成品形态 + 包装类型 + 分销储存）；本卡。
5. 用户问「一个产品同时命中 Table 3-4 多个成品类别怎么办」→ 全部类别危害取并集写入 Column 2、覆盖每个加工步骤（C-03 / L1741–1752）。
6. 用户问「Ch.3 的表能不能单独用来判 reasonably likely to occur」→ **不能**；须结合 Ch.4–21 与自身／外部专家（L127–136、L2128–2134），属高频边界问答。
7. 用户问「表里没打勾是不是就等于这个危害不显著」→ 不是；表只列潜在危害、非穷尽，须补区域／厂房／设备／工艺特有与新出现危害（L1709–1719、L1753–1760、L137–144）。
8. 用户问「Ch.4–21 各章怎么读／四段式是什么」→ STEP 9 以 Column 2 为检索键 + 四段式（Understand the Potential Hazard / Determine Whether Significant / Identify CCPs / Develop a Control Strategy）；16 章同构，Ch.8、Ch.10 例外；本卡。
9. 用户问「reasonably likely to occur 到底怎么判」→ 无控制条件下、审慎加工者标准、四类证据（L1780–1789、L1720–1731），本卡；**问法条定义来源与 21 CFR 123.3／123.6(a)** 转 CAP-22。
10. 用户问「我们一直有冷藏／时温控制、从没出过组胺，能不能判不显著」→ 反例；判 Yes 且把现有控制写进 HACCP 计划（C-02 / L1715–1731）。
11. 用户问「显著性是按整条产品线判还是按步骤判」→ 每个加工步骤独立评估 + 三情形取或（L1795–1808）；叠加分销／预期用途（L1808–1812）与跨步骤累积滥用（L6956–6966）。
12. 用户问「Worksheet 第 3 栏填 Yes/No，第 4 栏要不要都写理由」→ 都要写（L1813–1822）；No 只豁免 STEP 11–18、不豁免理由；书面化期望见 L1534–1540。
13. 用户问「某步判显著，是不是就得在该步设 CCP」→ 不是；显著是 STEP 10 属性、CCP 是 STEP 11 属性（L1823–1827）。
14. 用户问「CCP 判定树怎么问／Appendix 3 能不能照抄」→ 本卡只给 Q1/Q2/Q3 **逻辑复原**与「不可完全依赖」警告（L25876–25879）；导出件残表 L25888–25902 已塌陷，**不得逐字复原**，须回查 PDF 原版。
15. 用户问「同一危害为什么不同章节给的 CCP 不一样」→ control strategy example 多条并存、CCP 位置随策略漂移（L1843–1847）；选策略即选 CCP 落点。
16. 用户问「每个显著危害至少要几个 CCP」→ 至少一个（L1852–1859，回指 21 CFR 123.6(c)(2)）；**条款级判定**转 CAP-22。
17. 用户问「关键限值怎么定／能不能用别的数值」→ STEP 13 定义 + 须对应被监控参数（L1891–1896、L1921–1931）；**替代限值须科学论证充分性**（L115–126），转 `process-control-validation` 做验证方法论。
18. 用户问「Appendix 5 的 50 ppm / 500 ppm 能不能直接抄成关键限值」→ 不能；那是 FDA/EPA 既有安全水平、多数是执法触发点，`may not always be suitable for critical limits`（L27442–27444），guidance levels 不作控制措施（L27618）；数值外部法源回指 CPG / 21 CFR 556 / 40 CFR 180 / NSSP（**转引未收**），具体取样方案转 `inspection-sampling`、化学危害限值转 `chemical-hazard-controls`。
19. 用户问「监控程序要写哪几栏」→ What / How / Frequency / Who 四问 → Plan Form 第 4/5/6/7 栏（L1946–1950、L1977–1979）；连续记录至少每日复核（L1969–1976）。
20. 用户问「偏离 CL 怎么办／记录验证怎么填」→ STEP 15–17（纠偏、记录、验证）与 STEP 18 签名；**法定纠偏路径、记录保存期、1 周复审、至少每年复审**一律转 CAP-22〔§ 123.7〕〔§ 123.8〕〔§ 123.9〕。
21. 用户问「危害分析要不要书面／不用 Appendix 1 表格违不违法」→ 法条不要求书面危害分析、也不要求用该表（L1506–1509、L1534–1540），但 FDA 期望书面以便复审与举证；**法定义务边界**转 CAP-22。
22. 用户问「寄生虫冻结参数／盐渍能不能杀虫／6 英寸例外」→ Ch.5 三组温度×时间充分条件、6 英寸例外、盐渍醋渍只减量不消除（L4681–4697、L4703–4708）；参数适用边界见 B8。
23. 用户问「组胺 50 ppm 与 500 ppm 分别是什么／分解鱼能不能放行」→ 50 ppm guidance level（分解指示）、500 ppm toxic（L6850–6854），分解即掺假的独立法律后果（L6827–6843、FD&C Act 21 U.S.C. 342 **转引未收**）；执法限值转 `chemical-hazard-controls` / `inspection-sampling`。
24. 用户问「肉毒／冷熏／水相盐／全程冷藏能不能单独作屏障」→ Ch.13 否定式警告（`refrigeration alone cannot be relied upon`，L21106–21112）、多重屏障须逐项论证；具体参数与验证转 `process-control-validation` / `chemical-hazard-controls`。
25. 用户问「过敏原／亚硫酸盐／标签该不该声明、CCP 放哪」→ Ch.19 成品标签审查 vs 原料接收（C-10 / L24245–24254）；本卡给「产品描述 → CCP 前移」判定链，过敏原程序管理与交叉接触清洁转 `allergen-program`。
26. 用户问「这是不是法规／FDA 强制要求这么做吗／不照做会不会开 483」→ **把指南当法规**高频误读：指南不设可执行责任、`should` 只是建议（L100–108）；是否违法一律转 CAP-22〔§ 123.xxx〕；483 与检查作业口径转 `inspection-readiness` / `investigator-authority-procedure`，CP 7303.842 **正文本包未收**。
27. 用户问「既然指南非强制，是不是危害分析、HACCP 计划都可以不做」→ **反向误读**：Part 123 的 `shall` 义务不因指南非强制而稀释；危害分析〔§ 123.6(a)〕、书面 HACCP 计划〔§ 123.6(b)〕、至少一个 CCP〔§ 123.6(c)(2)〕转 CAP-22。
28. 用户问「把 Appendix 5／控制策略示例数值当合规清单开不符合项」→ 拒绝；示例数值是「经论证的起点」不是法定终点，guidance levels 不作控制措施（L27618），且无既设水平时 FDA 仍可依掺假条款执法（L27445–27448）。
29. 用户问「第 4 版 June 2022 是不是 2022 年新规／某章页脚 June 2021 算不算旧版」→ **版本口径**：封面 June 2022 第 4 版（L1444–1446），Ch.3 / Appendix 3 / Appendix 5 页脚仍 June 2021，属分章滚动修订；不得写成「2022 新规」，也不得据页脚否认其属第 4 版（B10）。
30. 用户问「消费者／零售、retorting、可接受市场名称、濒危物种、Part 120/1240/NSSP、Import Alert 16-xx、BAM 怎么查」→ **仍未收／已转出**：本指南明文不覆盖（L92–95、L4654–4667、L2139–2140、L2144–2156），一律标「转引未收」，不给条款级结论。
31. 用户问「帮我把这份 HACCP 计划写出来／判这个产品合不合法」→ 超出本包，转出（B12）：本卡只给方法论与层标签，不代写计划、不代填表单、不判法定身份。
32. 用户问「十五类来源怎么引用／L 号是什么／能不能把指南章号写成 §123」→ 引用规范（B11）：指南写「Seafood Hazards Guide 第 4 版 Ch.x / Appendix x / L####」，法条写〔§ 123.xxx〕，两者不可互换；十五类不可混引。

## E — 执行要点

**Step 1 — 输入层：先定产品与工艺的静态画像（STEP 1–5）。** 依次写实厂名地址、物种市场名／拉丁名、成品形态、包装类型、分销与储存方式、预期用途与消费者，并绘制从接收至分销的流程图（含非鱼配料接收与储存、须现场核实）。这些字段是后续 STEP 7/8 查 Table 3-2/3-3（物种维）与 Table 3-4（成品／包装／储运维）的**检索键**；描述不实即判定链断点，须回 Step 1 重做。

**Step 2 — 识别层：建六栏工作表并填 Column 1/2（STEP 6–8）。** 把流程图每个加工步骤写入 Column 1；按物种查 Table 3-2/3-3 得品种相关潜在危害、按成品形态+包装+储运查 Table 3-4 得工艺相关潜在危害，二者**在每一个加工步骤各占一行**写入 Column 2；同时以自身／外部专家补表外、区域特有、厂房特有与新出现危害。两道闸门在此预埋：Column 3=No 剪枝 STEP 11–18，Column 6=No 剪枝 STEP 12–18。

**Step 3 — 理解层：以 Column 2 为检索键查 Ch.4–21（STEP 9）。** 逐危害定位对应章节的四段式：段 1 Understand the Potential Hazard 读发生条件与可用控制方法，段 2 Determine Whether Significant 读评估信息，段 3 Identify CCPs 读控制应施加的位置，段 4 Develop a Control Strategy 读一条或多条控制策略示例及其计划片段参数。Ch.8、Ch.10 不含四段式（前者仅散文加文献，后者声明不提供甲基汞控制建议）。

**Step 4 — 显著性闸门 1：无控制条件下逐步判（STEP 10）。** 每一步独立评估，先声明「假设所有现有控制都不存在」；命中三情形任一即判该步显著——该步引入至不安全水平／该步增长至不安全水平／他步显著但本步可预防消除降低到可接受水平；并叠加分销储存、预期用途与消费者、跨步骤累积滥用。显著→Column 3 填 Yes，不显著→填 No，**两者都必须在 Column 4 写出理由**；理由本身就是复审与监管质询的唯一举证位。

**Step 5 — 定位层：CCP 判定与控制策略（STEP 11）。** 只取 Column 3=Yes 的行，用 Appendix 3 的 Figure A-2 判定树逻辑（Q1 风险与严重性是否足以需控 / Q2 本步是否存在控制措施 / Q3 本步控制对降至可接受水平是否必要）判断，否定分支指向 Modify this step, process or product；判定树只是辅助工具、不可完全依赖。结合 Ch.4–21 的 Identify CCPs 段选定控制策略示例，把预防措施写入 Column 5，把 CCP Yes/No 写入 Column 6。合规下限校验：每个显著危害至少有一个 Column 6=Yes（回指 21 CFR 123.6(c)(2)，**条款级判断转 CAP-22**）。

**Step 6 — 参数化层：把 Column 6=Yes 的行投影进 HACCP 计划表（STEP 12–14）。** 两表通过「加工步骤名 + 危害名」逐行对应，映射如下：

| 六栏工作表（Hazard Analysis Worksheet） | 内容 | 产生步骤 | → 十栏 HACCP 计划表（HACCP Plan Form） | 产生步骤 |
|---|---|---|---|---|
| Column 1 | 加工步骤（流程图每框一行） | STEP 6 | Column 1（仅抄 CCP 步骤名） | STEP 12 |
| Column 2 | 潜在危害（品种 + 工艺，每步都写） | STEP 7 / 8 | Column 2（该 CCP 对应的显著危害） | STEP 12 |
| Column 3 | 是否显著 Yes / No | STEP 10 | —（No 即剪枝 STEP 11–18） | — |
| Column 4 | Yes / No 的理由（两者都写） | STEP 10 | —（复审与举证材料，不进计划表） | — |
| Column 5 | 预防措施 / 控制策略 | STEP 11 | — | — |
| Column 6 | 是否 CCP Yes / No | STEP 11 | —（Yes 才进计划表；No 剪枝 STEP 12–18） | — |
| — | — | — | Column 3 关键限值（最大/最小值，须对应被监控参数；可设更严 operating limit） | STEP 13 |
| — | — | — | Column 4/5/6/7 监控 What / How / Frequency / Who | STEP 14 |
| — | — | — | Column 8 纠正措施程序 | STEP 15 |
| — | — | — | Column 9 记录保持系统 | STEP 16 |
| — | — | — | Column 10 验证程序 | STEP 17 |
| 首页签名 + 日期 | 由现场最高负责人或更高层签署 | — | 首页签名 + 日期，表示企业接受实施 | STEP 18 |

关键限值取自所选控制策略示例的片段参数，但**只是建议起点**：若改用其他策略／限值，须科学论证其充分性（L115–126）；Appendix 5 的执法触发水平不总是适合关键限值（L27442–27444），guidance levels 不作控制措施（L27618）。

**Step 7 — 收尾层与反向追溯（STEP 15–18）。** 补齐纠正措施、记录、验证三栏与签名日期；然后做可追溯性检查：Plan Form 任一栏应能回溯到 Ch.3 某张表（危害来源）与 Ch.4–21 某章某段（判定与参数来源），无法回溯的栏目即判定链断点，须回 Step 2 或 Step 3 补证据。Column 9 记录名称等由 18 步流程自身产生的栏目，属「流程产生」而非「章节可追溯」，须明确标注。

**Step 8 — 输出必带层标签（收尾声明）。** 任何输出必须逐条标注三类层标签之一：① **法定层**〔§ 123.xxx〕／CAP-22（危害分析、书面 HACCP 计划、至少一个 CCP、纠偏、记录保存期、1 周复审、至少每年复审等 `shall` 义务，以及法定身份判定）；② **指南建议层**（本卡：18 步、Ch.3 三表、无控制条件判定、六栏／十栏表单、控制策略示例、冻结／组胺参数等 `should` 方法论与建议参数）；③ **外部法源转引未收**（Appendix 5 回指的 CPG / 21 CFR 556 / 40 CFR 180 / NSSP Guide / Import Tolerance、FD&C Act 掺假条款、CP 7303.842、part 120/1240/108/110/507、Import Alert 16-xx、BAM 海产品章节）。引用规范：指南写「Seafood Hazards Guide 第 4 版 Ch.x / Appendix x / L####」，法条写〔§ 123.xxx〕，**不可互换**；十五类来源不可混引。凡输出中出现「必须／违法／合规」字样，必须先确认它属于哪一层，不得把建议层的 `should` 直接写成法定层的 `shall`。

## B — 边界

**B1 — 双向防呆：指南非强制 ⇄ Part 123 强制，两个方向都错。** 方向 ①：把 guidance 的 `should` 读成 `shall`，宣称「FDA 指南规定了某关键限值」或据此开不符合项——指南自身不设 legally enforceable responsibilities，只有明确转引 regulatory or statutory requirements 处才带强制力（L100–108）。方向 ②：因「这只是 guidance、不具强制力」把指南明文转述的法规义务（危害分析、书面 HACCP 计划、每个显著危害至少一个 CCP、按〔§ 123.7〕〔§ 123.8〕记录与复审）一并当成推荐、可酌情省略——凡点名 21 CFR 123／113 的 `must`／`require`／`shall`，效力来自法规本身，转 CAP-22。判定某条要求是否强制，唯一依据是「该处是否引用了法规／法条」，而非它在指南里读作 `must` 还是 `should`。

**B2 — Ch.3 表不可单独使用，且不是穷尽清单。** 表只列 potential hazards，明文 `the tables should not be used separately`；必须与 Ch.4–21 各章信息 **combined**、并叠加自身或外部专家，才能判 likelihood of occurrence 与显著性（L127–136、L2128–2134）。表是「FDA 当前最佳信息」而非穷尽，须补区域新／特有（L1709–1715）与厂房、设备、工艺新／特有（L1753–1760）危害，并对 new or emerging problems 保持警觉（L137–144）。「表里没这个危害」不是「该危害不显著」的论据；只查表打勾就填 Yes/No 是典型「表格单独使用」。

**B3 — 显著性必须在「无控制条件」下判定。** `The likelihood of a hazard occurring should be judged in the absence of controls`（L1720–1721）。不得以「我们已有常规／传统控制」「历年未检出」为由把危害判为不显著；控制措施的存在不是「危害不显著」的证据，反而是「该危害在无控制时会发生」的证据。组胺两情形必须分清：鱼种本身不能产组胺 → 判 No、可不列入计划；已有捕捞船时间／温度控制压制了它 → 仍判 Yes，且 `the controls should be included in the HACCP plan`（L1728–1731）。法规定义中的 `in the absence of those controls`（L1780–1789）与此同源，凡引用定义不得把现有控制算作发生可能性的减项。

**B4 — 显著 ≠ 该步控制；Yes/No 都要写理由；两道剪枝闸门不可误用。** `identifying a hazard as significant at a processing step does not mean that it must be controlled at that processing step`，CCP 位置由 STEP 11 另定（L1823–1827）。Column 3 无论 Yes 还是 No 都必须在 Column 4 记录理由（L1813–1822）；填 No 只豁免 STEP 11–18，**不豁免理由记录**，也不得理解为「可以不做记录」——书面理由支撑 HACCP 计划再评估与监管质询（L1534–1540）。Column 3=No 跳过 STEP 11–18、Column 6=No 跳过 STEP 12–18（L1820–1822、L1868–1870），对已剪枝的步骤继续填计划表条目即制造无意义内容。

**B5 — CCP 随控制策略漂移；Appendix 3 判定树塌陷，不可逐字复原。** 同一危害常有多条 control strategy example，换策略则 CCP 位置、监控对象、关键限值随之改变（L1843–1847）；CCP 不是危害的固有属性。导出件中 Appendix 3 的 Figure A-2 判定树（L25888–25902）已退化为 Q1/Q2/Q3 标签与错位残表（`IscontrolatthisstepnecessaryforSafety?` 等），**不得据其逐字复原问答或当作可引用决策工具**，须回查 PDF 原版；本卡只给逻辑复原与引导散文 L25876–25879 的「不可完全依赖」警告。同一危害多 CCP、同一步骤多危害 CCP 均允许（L1852–1859）。

**B6 — 替代关键限值须科学论证；示例数值不是合规清单。** 可用其他控制策略／关键限值，但须同时符合适用食品安全法律法规、并 `scientifically establish their adequacy`（L115–126）；Ch.13 把该义务具体化为工艺验证（温度分布找冷点、热穿透取最慢加热单元、EPIPT 只能在科学研究覆盖条件下使用，L21340–21362）。反向也错：把 Ch.4–21 示例片段表里的时温／盐度／水相盐、或 Appendix 5 的 tolerance／action level／guidance level 抄成「合规阈值清单」，认为达到即合法、未达即违法——这些是 recommendations，目标是「likely result in a HACCP plan that is acceptable to FDA」，不是法条本身。

**B7 — Appendix 5 数值是外部法源快照，须回指并标「转引未收」。** Appendix 5 明列的是 FDA 与 EPA**既有**安全水平，多数是「agency could take legal action 的执法触发点」，故 `may not always be suitable for critical limits`（L27442–27444）；脚注明说 These values are tolerances（21 CFR 109 / 556、40 CFR 180，L27608）、`Guidance levels are not intended to be identified in the HACCP plan as a control measure`（L27618）。第 4 版把 Ch.9 原 Table 9-1 移除、改为在 Appendix 5 作 reference（L715–717），更证明它是**法源索引**而非新设标准。回指对象：CPG Sec. 540.525（组胺）／540.250／540.600／555.300／555.425／575.100、Compliance Program 7303.842、21 CFR 556 系列、40 CFR 180 系列、NSSP Guide、Import Tolerance、ICMSF、FD&C Act 21 U.S.C. 342 —— 本包多数未收，涉具体数值合规结论一律标「转引未收」，不得表述为「FDA 在本指南中新设的限值」。且 `Regardless of an established level or not`，FDA 仍可依掺假条款执法（L27445–27448），数值不是合规护身符。

**B8 — 数值型参数成套且不可互换，各有适用边界。** Ch.5 寄生虫冻结是三组「温度 × 时间」的 OR 充分条件（L4681–4689），任一组内部参数不可拆配（不得把 -35°C 的 15 小时配到 -20°C，也不得把「冻实后 -20°C 24 小时」拆成单独条件）；全部以 **ambient temperature（环境／库温）** 表述而非鱼体中心温度，效果还受冻至坚实时长、鱼种／来源、寄生虫种类影响（L4668–4679）；**厚于 6 英寸的大鱼可能不适用**（L4689–4691）。盐渍／醋渍／柠檬汁腌渍、修剪腹肉／灯检挑虫只减量、不消除、不能降到可接受水平（L4692–4697、L4703–4708），不得单独作 CCP。Ch.7 的 50 ppm 是 guidance level／分解指示、500 ppm 是 toxic 水平，二者性质不同不可混用（L6850–6854）；分解即掺假（21 U.S.C. 342，L6827–6843）是独立法律后果。Ch.12/13 的冷藏、盐、烟熏、干燥均为**条件性屏障**，`refrigeration alone cannot be relied upon`（L21106–21112），不得单凭一项宣称控制到位。

**B9 — 主体与内容范围：不覆盖消费者／零售、不提供 retorting、命名与濒危物种外链。** 指南「does not specifically address safe handling practices by consumers or by retail establishments」（L92–95），只面向加工者并供监管者评估 HACCP 计划；不提供 retorting（低酸罐头热力杀菌）信息，该部分归 21 CFR 113（L4654–4667）；可接受市场名称的权威来源是 The Seafood List，`This Guide is not the official resource for determination of acceptable names`（L2139–2140）；濒危物种与 ESA 限制归 NOAA／USFWS（L2144–2156）。物种替换（species substitution）既是经济欺诈／误标，也会使潜在危害被漏识别或错识（L2157–2170），须把物种身份核验前置为 STEP 2 输入前提；但本指南不处理掺假／错误标签的法律定性。

**B10 — 版本口径：封面 June 2022 与多章 June 2021 页脚属分章滚动修订。** 本导出件为 **June 2022 Edition（第 4 版）整册**（封面、导言 G 页页脚与 L1444–1446 的 fourth edition 声明），但 Ch.3 页脚 `3 - 1 (June 2021)`（L2160）、Appendix 3 `A3-1 (June 2021)`（L25886）、Appendix 5 各页 `A5 - 1 … A5 - 12 (June 2021)`（L27452 起）、Ch.19 书目 `August 2019` 均为各章最近修订时点；导言修订摘要按章列 2022 年改动（含 Chapter 9 更名、Table 9-1 归并入 Appendix 5，L695–717）。引用须写「第 4 版 June 2022（该章页脚 June 2021）」，**不得**写成「2022 年新规／新发布安全水平」，也不得因某章页脚 2021 就否认它属于第 4 版。指南页脚日期不产生法规效力、不设生效日期，与 CFR 年度编纂版次／Federal Register 生效日是两套「版本」，不可互相校对或替代。

**B11 — 导出件转换质量红线与十五类不可混引引用规范。** 本导出件是 PDF／网页转 Markdown，**不是可信的逐字文本**：表格列头连写（`MARKETNAMES`／`LATINNAMES`／`Parasite3HazardsCHP5`）、词条重复粘连（`ALFONSINOALFONSINO`／`AMBERJACKAMBERJACKAMBERJACK`）、字符丢失（`fsh`→fish、`Pufer Fish`、`Specifcations`）、页码页眉混入正文（`3 - 2 (June 2021).`、`A5 - 2 (June 2021)`）、章节标题层级错乱、以及 Appendix 3 判定树图形塌陷（L25888–25902）。因此 R 段英文引用块**只能取自散文段落**，每段 ≤100 词，PDF 换行合并为空格、其余字符（含弯引号、`should`／`shall`、括号、`chose` 等原文细节）逐字保留；表格单元、页码页眉页脚、Appendix 3 残表、粘连文本、附加法规全文转录一律标为「不可引用区」。全包自 v4.10 起**十五类来源不可混引**：指南写「Seafood Hazards Guide 第 4 版 Ch.x / Appendix x / L####」，法条写〔§ 123.xxx〕，PCHF 指南用 Ch／小节号，L.mono 用其章节号，SECG 用 SECG 章号，Ed.5 用问答编号，Handbook 用「Handbook 章名 + 产品名」，CPGM 7303.040 用「CPGM 7303.040 PART x」，CP 7303.050 / 7303.070 / 7303.878 用各自 PART x，IOM 用「IOM 5.x.x / Exhibit 5-x」，Addendum／Appendix 8 的 Part 123 转录**只作对照不作引用依据**；part 120 / 1240 / 108 / 110 / 507、CP 7303.842、NSSP Guide 一律标「转引未收」。

**B12 — 与其它卡的分工、不代写、仍未收清单。** 本卡＝第 15 类来源的**技术指南层／完整危害分析判定链**。问「法条义务、条款级判定、法定时限、法定身份」→ CAP-22 `seafood-haccp-statutory-requirements`〔§ 123.xxx〕；问「PCHF／Part 117 危害分析、PCQI、书面危害分析、known or reasonably foreseeable hazard」→ `hazard-analysis-method`（**两套判定体系不可互套**：本卡是 Seafood HACCP 的 `reasonably likely to occur` + 无控制假设态，Part 117 不设 species/process 二分、不设是否 CCP 一栏）；问「组胺／化学危害具体限值与检测方法」→ `chemical-hazard-controls`；问「工艺验证、科学论证充分性、温度分布／热穿透」→ `process-control-validation`；问「过敏原程序、交叉接触与清洁」→ `allergen-program`；问「取样方案与感官／分解检验」→ `inspection-sampling`；问「检查员作业／483／Import Alert」→ `inspection-readiness` / `investigator-authority-procedure`；问「LACF／酸化食品」→ `lacf-statutory-requirements` / `lacf-inspection-program`。**本卡不代写 HACCP 计划、不代填表单、不判法定身份、不承诺合规、不出法律结论**（计划须由〔§ 123.10〕合格者制定）。正文本包仍未收：CP 7303.842、NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、Import Alert 16-xx 系列、BAM 海产品章节、Appendix 5 回指的 CPG Sec. 540.525 / 555.300 / 575.100 / 21 CFR 556 / 40 CFR 180 / Import Tolerance 全文 —— 一律标「转引未收」，不给条款级结论。
