# 阶段 1 候选池 — 框架提取器（v4.10 / 第 15 类来源）

- 源文档：`C:/Users/周至/AppData/Local/Temp/seafood_guide.md` —— FDA《Fish and Fishery Products Hazards and Controls Guidance》June 2022 第 4 版导出全文，31,321 行；全文行号均以此文件为准。
- 扫描范围：L1–210（导言、范围与 Table of Contents）、L680–855（修订记录中对四段式的元描述）、L1439–2095（Ch.1–2 全量精读）、L2097–2144（Ch.3 Introduction 与 Notes）、L3495–25902（Ch.4–21 章节标题全量定位、四段式结构抽样、Appendix 1–3 表单与判定树）、L25921–28285（Appendix 4–9 标题登记）；并辅以全文 Grep 扫描 `^## Chapter`、`STEP \d+:`、四段式关键词、`^## Appendix` 做全量核对。
- 产出时间：2026-11-06
- 卡片定位：本候选池服务「技术指南层的判定方法」，目标是蒸馏出**完整危害分析判定链**；21 CFR Part 123 的法条义务层由包内 CAP-22 `seafood-haccp-statutory-requirements` 承担，二者不重叠。
- 引用约定：英文原句一律取自**散文段落**，用 `> ` 引用块，每段 ≤100 词并标注行号；表格、页码、页眉、Appendix 3 塌陷残表不作逐字引用。

## F-01 Ch.2 的 18 步 HACCP 计划开发主流程（含 Preliminary Steps 分组与双表栏目映射）

- 类型：主流程框架（端到端开发流程 + 两张表单的逐栏投影）
- 依据行号：L1492–1516（适用前提与表单说明）、L1517–1540（Hazard Analysis Worksheet 说明）、L1542–1615（The Steps 速览清单与 ° 分组）、L1560–2085（STEP 1–18 逐步详述）、L1872–2095（HACCP Plan Form 段）、L25765–25816（Appendix 1 两张空白表的栏目编号）
- 框架步骤：
  1. 确认适用前提：仅当产品存在显著食品安全危害时才须编制 HACCP 计划；每个加工场所、每类产品各一份，危害与控制完全相同时方可合并成一份（L1503–1516）；HACCP 计划表本身非强制格式，但用 Appendix 1 标准表有助于通过审查（L1496–1510）。
  2. 【Preliminary Steps，STEP 1–5，分组标记见 L1548「Preliminary Steps」与 L1559「PRELIMINARY STEPS」，对应速览清单第一组 °°°°°（L1550–1557）】依次填两张表首页通用信息栏：① Provide general information（厂名/地址，L1560） ② Describe the food（市场名或拉丁名、成品描述、包装类型，L1565–1595） ③ Describe the method of distribution and storage（L1619–1630） ④ Identify the intended use and consumer（L1631 起） ⑤ Develop a flow diagram（从接收到分销的全部步骤、含非鱼配料的接收与储存、须现场核实，L1657–1669；示例见 Appendix 2 的 Figure A-1）。
  3. 【Hazard Analysis Worksheet，STEP 6–11，对应速览清单第二组 °°°°°°（L1596–1603）】⑥ Set up the worksheet：把流程图每一加工步骤写入 Worksheet 第 1 栏（L1671–1675） ⑦ 品种相关潜在危害 → 第 2 栏（L1676–1708） ⑧ 工艺相关潜在危害 → 第 2 栏（L1732–1740） ⑨ Understand the potential hazard（查 Ch.4–21，L1761–1773） ⑩ 显著性判定 → 第 3 栏 Yes/No、第 4 栏理由（L1774–1822） ⑪ 识别 CCP → 第 5 栏预防措施、第 6 栏 CCP Yes/No（L1828–1870）。
  4. 【HACCP Plan Form 前半，STEP 12–14，对应速览清单第三组 °°°（L1604–1611）】⑫ Set up the form：把第 6 栏为 Yes 的 CCP 步骤与危害抄入 Plan Form 第 1、2 栏（L1875–1884） ⑬ Set critical limits → 第 3 栏（L1891–1933） ⑭ Establish monitoring procedures 的 What/How/Frequency/Who → 第 4/5/6/7 栏（L1934–1979）。
  5. 【原理 4–7，STEP 15–17，对应速览清单第四组 °°°（L1612–1615）】⑮ 纠偏程序 → 第 8 栏（L1980–2026） ⑯ 记录系统 → 第 9 栏（L2027–2046） ⑰ 验证程序 → 第 10 栏（L2048–2084）。
  6. 【STEP 18 收尾】所有显著危害走完后，由现场最高负责人或更高层签署并注明日期，表示企业接受该计划实施（L2085–2095）。
  7. 两道剪枝闸门：第 3 栏填 No 的加工步骤，该危害不必再做 STEP 11–18（L1820–1822）；第 6 栏填 No 的加工步骤，不必再做 STEP 12–18（L1868–1870）。
- 可回答的新问题：若某潜在危害在 Worksheet 第 3 栏的所有加工步骤都填了 No，按 18 步流程最终生成的 HACCP Plan Form 中该危害会占几行、签名页又该如何解释这份「零 CCP 计划」的正当性？

> (L1493–1496) This guidance document is designed to walk you through a series of 18 steps that will yield a completed Hazard Analysis Critical Control Point (HACCP) plan.

## F-02 危害识别分流：Ch.3 三张表 → Ch.4–21 的两阶段联动

- 类型：分流/检索框架（物种维 + 工艺维查表，再叠加章节判定），附带「表不得单独使用」的认识论约束
- 依据行号：L127–136（导言中的联动与禁令）、L1676–1694（品种相关 / 工艺相关危害的定义）、L1695–1760（STEP 7/8 查表规则）、L2097–2134（Ch.3 Introduction 三表定义与 Notes）、L1761–1773（STEP 9 转入章节）
- 框架步骤：
  1. 先按物种门类分流：有脊椎（finfish 等）查 Table 3-2「Potential Vertebrate Species-Related Hazards」，无脊椎（虾、蚝、蟹、龙虾等）查 Table 3-3「Potential Invertebrate Species-Related Hazards」（L1695–1703、L2108–2117）。
  2. 在表第 1 栏（市场名）或第 2 栏（拉丁名）定位 STEP 2 已确认的物种，查右侧栏是否出现「√」或天然毒素的 1/3 字母代码；命中即把该**品种相关危害**写入 Worksheet 第 2 栏，且**在每一个加工步骤都写一行**（L1695–1708）。
  3. 再用 STEP 2/3 已确认的成品形态与包装类型查 Table 3-4「Potential Process-Related Hazards」第 1/2 栏，把命中的**工艺相关危害**同样写入第 2 栏、每个加工步骤（L1732–1740、L2118–2124）；若产品同时符合多个成品类别（如熟虾又是即食鱼制品沙拉），须把所有命中类别的危害全部列出（L1741–1752）。
  4. 补充表外危害：以自身或外部专家经验补入表未列、新出现或本地区/本厂特有的危害；三表只是「潜在危害清单」，不是显著危害结论（L1709–1715、L1753–1760、L2128–2134）。
  5. 联动闸门：三张表**不得单独用于判定 "reasonably likely to occur"**，必须与 Ch.4–21 各章信息、以及自身/外部专家知识合并，才能判断某危害对特定产品或工艺是否显著、以及显著后如何控制（L127–136、L2128–2134）。
  6. 以第 2 栏每个潜在危害为检索键，进入 STEP 9 逐章查 Ch.4–7、9、11–21 的四段式内容（L1761–1773），完成从「查表」到「查章」的交接。
- 可回答的新问题：当同一产品同时命中 Table 3-4 的两个成品类别、而这两个类别在 Ch.4–21 中指向互不兼容的 Control Strategy Example 时，Worksheet 第 2 栏应合并成一行还是拆成两行分别走显著性判定？分流规则本身没规定，用该框架能推出什么处置？

> (L127–136) The information contained in the tables in Chapter 3 and in Chapters 4 through 21 provide guidance for determining which hazards are "reasonably likely to occur" in particular fish and fishery products under ordinary circumstances. However, the tables should not be used separately for this purpose. The tables list potential hazards for specific species and finished product types. This information should be combined with the information in the subsequent chapters to determine the likelihood of occurrence.

> (L2128–2134) The tables provide lists of potential hazards. You should use the tables, together with the information provided in Chapters 4 through 21, and your own expertise or that of outside experts, to determine whether the hazard is significant for your particular product or process and, if so, how it should be controlled.

## F-03 显著性判定链：reasonably likely to occur 的定义、三情形与 Column 3/4 落地

- 类型：判定链（法规定义 → 逐步骤三情形 → 表单 Yes/No 与理由 → 剪枝）
- 依据行号：L1774–1789（STEP 10 与定义）、L1790–1795（各章对应 section）、L1796–1812（三情形与须考虑的因素）、L1813–1827（Column 3/4、剪枝、显著≠该步控制）
- 框架步骤：
  1. 收窄对象：把 Worksheet 第 2 栏的「潜在危害」清单收窄为「显著危害」，即 "reasonably likely to occur"（L1776–1779）。
  2. 套用法规定义：谨慎加工者基于经验、疾病数据、科学报告或其它信息，会因为在**缺乏这些控制**时存在发生的合理可能性而设立控制（L1780–1789）。
  3. 逐步骤独立评估：同一危害可在 A 步骤显著、在 B 步骤不显著，不得对整张表一次性下结论（L1796–1798）。
  4. 命中任一情形即判该步骤显著：(1) 该步骤可能以不安全水平**引入**危害；(2) 该步骤可能使危害**增长**到不安全水平；(3) 危害在其它步骤已显著，而**本步骤能把它预防、消除或降低到可接受水平**（L1799–1808）。情形 (3) 意味着「真正实施控制的步骤」本身也要判为显著。
  5. 叠加 STEP 3/4 的画像：判定时须纳入分销/储存方式与预期用途/消费者（如即食、易感人群）（L1809–1812）。
  6. 写入表单：显著 → 第 3 栏 Yes；不显著 → 第 3 栏 No；两者都必须在第 4 栏写明理由（L1813–1820）。
  7. 剪枝与交棒：第 3 栏为 No 的步骤不再做 STEP 11–18（L1820–1822）；「判为显著」不等于「必须在该步骤控制」，控制点位置留给 STEP 11（L1823–1827）。
- 可回答的新问题：某危害在冷藏分销条件下不会增至不安全水平（情形 2 不成立），但当预期用途改为即食、目标消费者为免疫低下人群时，三情形中哪一条会被重新激活、第 4 栏又该写什么理由？书里只说「须考虑预期用途与消费者」，未给出它与三情形的映射规则。

> (L1780–1789) The Seafood HACCP Regulation defines a food safety hazard that is reasonably likely to occur as "one for which a prudent processor would establish controls because experience, illness data, scientific reports, or other information provide a basis to conclude that there is a reasonable possibility that it will occur in the particular type of fish or fishery product being processed in the absence of those controls."

> (L1799–1808) A potential hazard is significant at the processing or handling step if (1) it is reasonably likely that the hazard can be introduced at an unsafe level at that processing step; or (2) it is reasonably likely that the hazard can increase to an unsafe level at that processing step; or (3) it is significant at another processing or handling step and it can be prevented, eliminated, or reduced to an acceptable level at the current processing or handling step.

## F-04 「in the absence of controls」反事实判定模型

- 类型：反事实判定规则（消除「已有控制即不显著」的典型误判）
- 依据行号：L1709–1719（已有控制不意味着危害不显著）、L1720–1731（口径与 scombrotoxin 双情形）、L1786–1789（定义中同源的 "in the absence of those controls"）
- 框架步骤：
  1. 先声明判定基准：危害发生的可能性必须在**假设没有任何控制措施**的条件下评估（L1720–1721）。
  2. 排除干扰证据：不得以「我们已有常规/传统控制」或「历年未检出」为由把危害判为不显著（L1716–1719）。
  3. 对「未曾观察到该危害」做双情形归因：情形 A = 物种本身不具备产生该危害的能力（如鱼不能生成组胺）；情形 B = 已存在的控制（如捕捞船时间/温度控制）压制了它（L1721–1727）。
  4. 分别下结论：情形 A → 不是 reasonably likely to occur，可不列入 HACCP 计划；情形 B → 仍是 reasonably likely to occur，且这些现有控制**必须写进 HACCP 计划**（L1728–1731）。
  5. 回写表单：情形 B 的控制措施进入 Worksheet 第 5 栏（预防措施），并继续走 STEP 11–18（与 F-03、F-05 衔接）。
  6. 一致性检查：法规定义中的 "in the absence of those controls" 与本口径同源，凡引用定义时，不得把现有控制算作「发生可能性」的减项（L1786–1789）。
- 可回答的新问题：一家工厂以「连续三年供应商证书 + 逐批检测均为阴性」证明某危害不显著，按反事实模型它必须补交什么证据才能排除情形 B？书里只给了 scombrotoxin 一个例子，未给出一般化的举证责任规则。

> (L1720–1727) The likelihood of a hazard occurring should be judged in the absence of controls. For example, the fact that scombrotoxin (histamine) development in a particular species of fish has not been noted may be the result of (1) the inability of the fish to produce histamine or (2) the existence of controls that are already in place to prevent its development (e.g., harvest vessel time and temperature controls).

## F-05 CCP 定位判定链：Appendix 3 判定树 + STEP 11 + 每危害至少一个 CCP

- 类型：判定树逻辑复原 + 定位规则 + 表单落地
- 依据行号：L1823–1827（显著≠该步控制）、L1828–1870（STEP 11 全文）、L1843–1848（不同控制策略 CCP 位置不同）、L1852–1862（每危害 ≥1 CCP 与 CCP 定义）、L25876–25882（Appendix 3 引导散文）、L25884–25902（Appendix 3 判定树塌陷残表，仅复原逻辑）
- 框架步骤：
  1. 输入收窄：只取 Worksheet 第 3 栏为 Yes 的加工步骤与危害（L1829–1831）。
  2. 复原 Appendix 3 的 Figure A-2 CCP 判定树（L25888–25902 在导出件中只剩 Q1/Q2/Q3 标签与零散问句，以下为**可复原的逻辑，非逐字原文**）：Q1 该步骤涉及的危害是否具有足以需要控制的风险与严重性；Q2 该步骤是否存在针对该危害的控制措施；Q3 该步骤的控制对于把危害预防、消除或降低到消费者可接受水平是否必要。按 Yes/No 分支决定是否把该步骤定为 CCP，否定分支指向「Modify this step, process or product」。
  3. 明确判定树的地位：它只是辅助工具，不得完全依赖，单独使用可能出错（L25876–25879，引导散文）。
  4. 结合章节定位：Ch.4–21 各章「Identify Critical Control Points」段给出控制应施加的位置；同一危害常有多种控制策略示例，不同示例的 CCP 往往不同（L1837–1848）。
  5. 把选定控制策略的预防措施写入 Worksheet 第 5 栏（L1848–1851）。
  6. 合规下限：每个显著危害**至少有一个 CCP**（21 CFR 123.6(c)(2)）；一个危害可有多个 CCP，一个加工步骤也可同时是多个危害的 CCP；CCP 是过程中 HACCP 控制活动实际发生的加工步骤（L1852–1859）。
  7. 写入第 6 栏：该步骤是 CCP → Yes，否则 No；第 6 栏为 No 的步骤不再做 STEP 12–18（L1863–1870）。
  8. 层级区分：「显著」属于 STEP 10 的危害属性，「CCP」属于 STEP 11 的控制位置属性，二者不可混同（L1823–1827）。
- 可回答的新问题：把同一显著危害的控制策略从「源头控制」换成「加工过程控制」时，Q2 的答案会在流程图的哪个步骤上发生翻转、从而使 Worksheet 第 6 栏的 Yes 落点前移还是后移？书里只说「CCP 往往不同」，未给出可推导的位移方向。

> (L1843–1848) Each chapter discusses one or more "control strategy example(s)" for how the hazard can be controlled, because there are often more ways than one to control a hazard. CCP(s) for one control strategy example often differ from those of another example for the same hazard.

> (L1852–1859) For every significant hazard, there must be at least one CCP where the hazard is controlled (21 CFR 123.6(c)(2)). In some cases, control may be necessary at more than one CCP for a single hazard. In other cases, a processing step may be a CCP for more than one hazard. CCPs are points in the process (i.e., processing steps) where the HACCP control activities will occur.

（说明：Appendix 3 判定树本体 L25884–25902 在导出件中已塌陷成残表，按约束不作逐字引用、不伪造原文，仅以上述 Q1/Q2/Q3 逻辑复原呈现；其引导散文 L25876–25882 亦仅在步骤 3 中作意译。）

## F-06 Ch.4–21 各章统一的四段式章节模板（含 Control Strategy Example）

- 类型：章节模板 / 检索框架（16 章同构 + 示例表参数抽取）
- 依据行号：L1761–1773、L1790–1795、L1837–1847、L1898–1902、L1939–1945、L2002–2008、L2033–2038、L2055–2060（8 处 STEP 说明反复声明「Chapters 4 through 7, 9, and 11 through 21」各含对应 section）；抽样行号：Ch.4 L3497/L3789/L3943/L4181、Ch.5 L4609/L4709/L4813/L4852、Ch.6 L5204/L5827/L5901/L5899、Ch.9 L9127/L9354/L9555/L10014、Ch.11 L11138/L11921/L12764、Ch.12 L14387/L14583/L14931、Ch.15–21 L20572/L20995/L22128/L23108/L23747/L24764/L25267；L703/L722/L730/L742 与 L768/L799/L818/L839（修订记录对四段式的元描述）；L9027–9132（Ch.8、Ch.10 例外）
- 框架步骤：
  1. 以 Worksheet 第 2 栏每个潜在危害为检索键，定位对应章节（章标题清单见 L3495–25265）。
  2. 段 1「Understand the Potential Hazard」：读取危害的显著性、在水产品中形成的条件、可用的控制方法（L1769–1773）。
  3. 段 2「Determine Whether the Potential Hazard Is Significant」：按该章给出的评估信息做显著性判定，回写 Worksheet 第 3/4 栏（L1790–1795）。
  4. 段 3「Identify Critical Control Points」：读取控制应施加的位置（L1837–1842）。
  5. 段 4「Develop a Control Strategy」：读取该章给出的一个或多个 Control Strategy Example；每个示例通常还附一张「HACCP 计划片段」示例表（如 Ch.9 的 TABLE 9-1~9-7、Ch.11 的 TABLE 11-1~11-7），从中抽取关键限值、监控、纠偏、记录、验证的具体参数（L10191/L10330/L10454/L13050/L13201 等）。
  6. 同构性统计：文档在 8 处 STEP 说明中一致列举 "Chapters 4 through 7, 9, and 11 through 21"，即 Ch.4、5、6、7、9、11、12、13、14、15、16、17、18、19、20、21 共 **16 章**采用该四段式；Ch.8（L9027–9122，仅一段散文加参考文献）与 Ch.10（L11122–11132，仅声明第四版不提供甲基汞 HACCP 控制建议）不含四段式，正是该清单排除这两章的原因。
  7. 把段 4 抽取的参数按栏目填入 HACCP Plan Form（与 F-07 衔接）。
- 可回答的新问题：把某章的 7 张 Control Strategy Example 片段表按栏目直接拼起来，能否构成一份完整 HACCP 计划？按 18 步流程还缺哪些由 STEP 1–12 产生、而片段表不会包含的栏目？

> (L1762–1773) Consult the hazards and controls chapters of this guidance document (Chapters 4 through 7, 9, and 11 through 21) for each of the potential hazards that you entered in Column 2 of the Hazard Analysis Worksheet. These chapters offer guidance for completing your hazard analysis and developing your HACCP plan. Each chapter contains a section, "Understand the Potential Hazard," that provides information about the significance of the hazard, the conditions under which it may develop in a fishery product, and methods available to control the hazard.

## F-07 七原理落地到 HACCP 计划表单：CL / What-How-Frequency-Who / 纠偏 / 记录 / 验证

- 类型：表单落地框架（原理 2–7 的参数化 + 双阈值 + 参数绑定）
- 依据行号：L1605–1615（速览清单第三、四组）、L1872–1884（STEP 12）、L1891–1933（STEP 13）、L1934–1979（STEP 14）、L1980–2026（STEP 15）、L2027–2046（STEP 16）、L2048–2084（STEP 17）、L2085–2095（STEP 18）、L25797–25810（Appendix 1 十栏空表）
- 框架步骤：
  1. STEP 12 建表：把 Worksheet 第 6 栏为 Yes 的 CCP 步骤与其显著危害抄入 Plan Form 第 1、2 栏（L1875–1884）。
  2. 原理 2「Set critical limits」→ 第 3 栏：为每个显著危害确定须控制参数的最大/最小值；限值过严会触发无谓纠偏，过松会放行不安全产品（L1891–1910）。
  3. 双阈值：可另设比关键限值更严的 operating limit，在偏离关键限值之前先调整工艺；其严程度依工艺波动经验与典型值接近关键限值的程度设定（L1911–1920）；偏离 operating limit 不触发正式纠偏（L2023–2024）。
  4. 参数绑定：关键限值必须直接对应将要监控的参数（例：既监控水温又监控传送带速度时，限值写水温/带速，而非产品中心温度）（L1921–1931）。
  5. 原理 3「Monitoring」→ 第 4/5/6/7 栏：逐项回答 What / How / Frequency / Who（L1946–1950、L1977–1979）；监控须直接测量设定了关键限值的那个参数，连续监控最理想，测量间隔越长则一次偏离牵连的产品越多，连续记录也须至少每日复核（L1951–1976）。
  6. 原理 4「Corrective action」→ 第 8 栏：偏离时须同时做到「不安全产品不流入消费者」与「纠正造成偏离的问题」；可预定纠偏也可按 21 CFR 123.7(c) 执行，预定者可在紧急情况下照章办理并免去因偏离重新评估计划；反复偏离须重评该 CCP 的充分性（L1980–2024）。
  7. 原理 5「Recordkeeping」→ 第 9 栏：列出用于记录监控执行情况的记录名称，记录须含实际值与观察值（L2027–2046）。
  8. 原理 6/7「Verification」→ 第 10 栏：验证计划既充分又被持续执行，覆盖关键限值充分性验证（工艺确立）、CCP 监控设备校准、周期性成品与过程检测、监控/纠偏/验证记录复核；校准失准时须回溯自上次校准以来的监控记录（L2048–2082）。
  9. STEP 18 收尾：签名 + 日期（L2085–2095）。
- 可回答的新问题：operating limit 与 critical limit 之间的缓冲区间应当如何由监控频率与工艺波动反推设定？书里只说「基于经验」，未给定量方法，用该框架能推出哪些必须纳入反推的变量？

> (L1946–1950) To fully describe your monitoring program, you should answer four questions: (1) What will be monitored? (2) How will monitoring be done? (3) How often will monitoring be done (frequency)? and (4) Who will do the monitoring?

## F-08 端到端「完整危害分析判定链」（F-01~F-07 的数据流串联与可追溯性）

- 类型：端到端串联框架（分层数据流 + 两道闸门 + 合规下限校验 + 反向追溯），直接呼应本卡「完整危害分析判定链」目标
- 依据行号：L127–136、L1492–1615、L1671–1870、L1872–2095、L25765–25816（两张空白表栏目）
- 框架步骤：
  1. 【输入层】STEP 1–5 产出产品/工艺静态画像：厂名、物种、成品、包装、分销储存、预期用途与消费者、经验证的流程图。
  2. 【识别层】STEP 6–8 以 Table 3-2/3-3（物种维）+ Table 3-4（成品/包装/分销储存维）产出 Worksheet 第 1、2 栏；规则是每一潜在危害在每一加工步骤各占一行。
  3. 【理解层】STEP 9 以第 2 栏为检索键，查 Ch.4–21 四段式的段 1（F-06）。
  4. 【显著性闸门 1】STEP 10 逐步骤套用 F-03 三情形并叠加 F-04 反事实口径 → 第 3 栏 Yes/No、第 4 栏理由；第 3 栏 No 即终止该危害在该步骤的后续全部步骤（L1820–1822）。
  5. 【定位层】STEP 11 对第 3 栏 Yes 的步骤套 Appendix 3 三问（F-05）→ 第 5 栏预防措施、第 6 栏 CCP Yes/No；第 6 栏 No 即终止 STEP 12–18（L1868–1870）。合规下限校验：每个显著危害至少有一个第 6 栏 Yes（L1852–1854）。
  6. 【参数化层】STEP 12–17 把第 6 栏 Yes 的行投影为 Plan Form 第 1–10 栏（F-07），参数取自所选 Control Strategy Example 的片段表。
  7. 【收尾层】STEP 18 签名/日期；两张表通过「加工步骤名 + 危害名」逐行对应（Worksheet 第 1/2 栏 ↔ Plan Form 第 1/2 栏，L1875–1884）。
  8. 【反向追溯】Plan Form 任一栏目都应能回溯到 Ch.3 的某张表（危害来源）与 Ch.4–21 某章某段（判定与参数来源）；无法回溯的栏目即判定链断点。
- 可回答的新问题：若监管审查要求把 Plan Form 第 3 栏的每个关键限值反查到 Ch.3 的表与 Ch.4–21 的具体段落，哪些栏目天然可追溯、哪些栏目（如第 9 栏记录名称）只能由 18 步流程自身产生？这一「可追溯性分层」书里没有讨论，用该串联框架能推出什么？

（F-08 为纯结构性串联，不配英文引用块。）

## 覆盖率自查

- **章节标题（全量扫描）**：以 `^## Chapter` 定位到 Ch.1–21 共 21 个标题行 —— L1439、L1486、L2097、L3495、L4607、L5202、L6474、L9027、L9123、L11122、L11134、L14103、L16467、L19710、L20570、L20993、L22126、L23106、L23739、L24762、L25265。Ch.4–21 的 18 个标题全部确认，无遗漏。
- **Ch.2（全量精读）**：L1485–1696（表单说明、The Steps 速览清单与 Preliminary Steps 分组、STEP 1–7 详述）、L1695–1884（STEP 7–12）、L1885–2095（STEP 12–18）逐段精读；并以 `STEP \d+:` 全文核对 18 个步骤标题（L1560/1565/1619/1631/1657/1671/1676/1732/1761/1774/1828/1875/1891/1934/1980/2027/2048/2085），逐条无缺。仅 L1635–1654（STEP 4 预期用途/消费者举例）略读，不影响框架提取。
- **Ch.3（导言精读，表体略读）**：L2097–2144（Introduction 三表定义与 Notes 联动）、L1695–1760（STEP 7/8 查表规则）全部精读；Table 3-2/3-3/3-4 本体（约 L2145–3494，千余行表格）未按行细读，仅通过 Introduction 与 STEP 说明确认三表的用途与列结构 —— 表格按约束不作逐字引用。
- **Ch.4–21（标题全量 + 结构级扫描 + 抽样精读）**：18 个章标题全部定位；四段式关键词全文检索确认文档在 8 处 STEP 说明中一致声明 "Chapters 4 through 7, 9, and 11 through 21"（16 章），并抽样验证 Ch.4/5/6/7/9/11/12/15/16/17/18/19/20/21 的实际标题行号（见 F-06）。Ch.8（L9027–9122，仅一段散文加参考文献）与 Ch.10（L11122–11132，仅一段「第四版不提供甲基汞 HACCP 控制建议」）确认不含四段式，属刻意简化/塌陷章节，正是 16 章清单排除它们的原因。其余各章正文（Ch.5/6/7/13/14/16/17/18/19/20/21，多为数百至上千行的控制策略示例表与参考文献）因篇幅过长，仅做标题级与结构级扫描，未逐行细读；Ch.14（L19710 起）开头为标准散文介绍，未定位到全大写四段式标题，疑为导出格式差异，但文档明确将其列入 16 章。
- **Appendix 1–5（全量定位）**：Appendix 1 L25750、Appendix 2 L25824、Appendix 3 L25884、Appendix 4 L25921、Appendix 5 L27450，5 个标题全部确认；另登记 Appendix 6–9（L27641/27966/28210/28285）及目录所列 Appendix 10–12、Addendum 1–2（L46–77），不在本卡 Ch.4–21 技术判定链范围，未细读。
- **塌陷 / 未细读清单**：① Appendix 1 空白表单（L25765–25816）在导出件中转为 markdown 表格，栏目名仍可读，仅用于核对 F-01/F-07 的栏目编号，未作逐字引用；② Appendix 2 流程图（L25840–25870）塌陷为逐格残表，未细读；③ **Appendix 3 CCP 判定树（L25884–25902）塌陷为残表**，仅保留 Q1/Q2/Q3 标签与零散问句，按约束只复原逻辑、不伪造逐字原文、不作逐字引用，引导散文 L25876–25882 亦仅在 F-05 步骤 3 作意译；④ Appendix 4（L25921–27449）与 Appendix 5（L27450–27640）为长篇细菌生长/灭活与安全水平数据表，未逐行细读；⑤ Ch.3 三张表本体与各章 Control Strategy Example 示例表均为表格，按约束不作逐字引用。
- **引用合规复核**：全文英文引用块共 10 段，全部取自散文段落（导言 L127–136、Ch.3 Notes L2128–2134、Ch.2 说明 L1493–1496 / L1762–1773 / L1780–1789 / L1799–1808 / L1720–1727 / L1843–1848 / L1852–1859 / L1946–1950），每段 ≤100 词并标注行号；表格、页码、页眉、Appendix 3 残表均未作逐字引用。
