# FDA PCHF 指南 — 关键概念词典（Glossary Extractor 产出）

> 阶段 1 术语提取。每条均回 source.md 原文核验。
> 法定定义 = 21 CFR 117.3（Introduction III.A，指南提醒"未来规则制定可能修改，应查最新版"）；
> 指南自定义 = Introduction III.B 或各章 "Terms Used in This Chapter"（"may be used differently elsewhere"）。

```yaml
# ============ 一、hazard 三层级词族 ============

- id: t01
  title: hazard
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；Ch1 重申
  source_quote: |
    "Hazard: Any biological, chemical (including radiological), or physical agent that has the
    potential to cause illness or injury."
  summary: 危害仅指能致人生病或受伤的生物/化学（含放射）/物理因子。与常识最大的差异：虫害、毛发、腐败、违反质量标准等质量缺陷**不是** hazard——应控制但不属于 PCHF 意义上的危害（除非直接影响食品安全）。蟑螂是 pest，不是 hazard；毛发掉进产品是质量瑕疵。
  tags: [法定定义, 核心概念, 危害层级]

- id: t02
  title: known or reasonably foreseeable hazard
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)
  source_quote: |
    "A potential biological, chemical (including radiological), or physical hazard that is known
    to be, or has the potential to be, associated with the facility or the food."
  summary: 危害分析的识别对象。关键词是"与该设施或该食品相关联"——不是泛泛的行业危害清单，而是已知或有潜在可能与**本厂/本产品**相关的危害。常识用法谈"某类食品有什么危害"，法规用法锚定在具体设施。
  tags: [法定定义, 危害层级]

- id: t03
  title: potential hazard
  type: term
  source_chapter: Introduction III.B；Appendix 1 A1.1
  source_quote: |
    "Potential hazard: Synonym for 'known or reasonably foreseeable hazard' as defined in 21 CFR
    117.3." / "Form 2-B uses the abbreviated term 'potential hazard' … because of space
    limitations on the form."
  summary: |-
    potential hazard 只是 known or reasonably foreseeable hazard 的**同义词**（Form 2-B 表格空间所限的简写，FDA 拟在表单说明中注明）。最危险的误读：把附录 1 表中的 X 标记"潜在危害"当成"需要控制的危害"——它只是建议进入评估的起点，与常识里"潜在=可能发生=要防"的直觉完全不同。
  tags: [指南自定义, 危害层级, 高频误读]

- id: t04
  title: hazard requiring a preventive control
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；Appendix 1 A1.3
  source_quote: |
    "A known or reasonably foreseeable hazard for which a person knowledgeable about the safe
    manufacturing, processing, packing, or holding of food would, based on the outcome of a hazard
    analysis (which includes the severity … and the probability …) establish one or more preventive
    controls to significantly minimize or prevent the hazard in a food and components to manage
    those controls…"
  summary: 三层级的顶层。判定基准是"懂食品安全的人**会不会**建预防控制"（含严重性+概率双重评估），而不是"危害是否存在"。判定责任在每个工厂；判定结果必须书面（无论 Yes 还是 No，解释 No 与解释 Yes 同等重要）。
  tags: [法定定义, 危害层级, 核心概念]

- id: t05
  title: hazard analysis
  type: term
  source_chapter: Introduction III.B（脚注 4：改编自 FSPCA 定义）
  source_quote: |
    "The process of identifying hazards, and evaluating information on those hazards (including
    the severity of the illness or injury if the hazard were to occur and the conditions that could
    lead to its presence), to determine which hazards require a preventive control…"
  summary: 识别+评估两要素的过程。核心输出不是"危害清单"而是"哪些危害需要预防控制"的判定。必须书面，**无论结论如何**；结论错误或漏识别则整个 FSP 无效——"无论工厂执行得多好"。
  tags: [指南自定义, 核心概念]

- id: t06
  title: relevant hazards
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "Universe of all hazards that are most relevant to food safety and that are narrowed (through
    the hazard identification phase of a hazard analysis) to known or reasonably foreseeable
    ('potential') hazards that are then evaluated … to determine the hazards requiring a preventive
    control."
  summary: 指南用来表达"与食品安全最相关的全部危害"的漏斗顶端概念，经识别阶段收窄为 potential hazards，再经评估阶段收窄为需控危害。它把 hazard 三层级明确串成一条漏斗：relevant → potential → requiring a preventive control。
  tags: [指南自定义, 危害层级]

# ============ 二、预防控制与 FSP 词族 ============

- id: t07
  title: preventive controls
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)
  source_quote: |
    "Those risk-based, reasonably appropriate procedures, practices, and processes that a person
    knowledgeable about the safe manufacturing, processing, packing, or holding of food would
    employ to significantly minimize or prevent the hazards identified under the hazard analysis
    that are consistent with the current scientific understanding…"
  summary: 关键限定：基于风险、与**当时**科学认知一致、由"懂食品安全的人"会采用。与 HACCP 时代"控制=CCP 上的控制"不同，卫生控制、过敏原控制、供应链控制、召回计划都算预防控制；工艺控制应定 CCP，但预防控制可以不落在 CCP 上。
  tags: [法定定义, 核心概念]

- id: t08
  title: food safety plan (FSP)
  type: term
  source_chapter: Introduction III.B；Ch1.2 (117.126)
  source_quote: |
    "A set of documents that contain the written hazard analysis, the written preventive controls,
    the written supply-chain program (when applicable), the written recall plan, and written
    preventive control management components…"
  summary: FSP 是**文档集**，无标准化强制格式（任何包含 Part 117 要求信息的格式均可；附录 2 表单改编自 FSPCA 但非法定）。与常识差异：未识别出需控危害时，FSP 可以只含危害分析一份文件；FSP 是记录，须由设施负责人签署并注明日期。
  tags: [指南自定义, 核心概念]

- id: t09
  title: preventive controls qualified individual (PCQI)
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；Ch1.3
  source_quote: |
    "A qualified individual who has successfully completed training in the development and
    application of risk-based preventive controls at least equivalent to that received under a
    standardized curriculum recognized as adequate by FDA or is otherwise qualified through job
    experience to develop and apply a food safety system."
  summary: 两条资格路径：FDA 认可标准化课程（FSPCA 课程为基准）**或**工作经验。与常识差异：无须是本厂员工（可外包顾问）；不等于 HACCP 时代的"质量经理"头衔；FSP 编制、validation、记录审查等多项法定活动须由 PCQI 执行或在其监督下进行。
  tags: [法定定义, 核心概念]

- id: t10
  title: qualified individual
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；21 CFR 117.4
  source_quote: |
    "A person who has the education, training, or experience (or a combination thereof) necessary
    to manufacture, process, pack, or hold clean and safe food as appropriate to the individual's
    assigned duties. A qualified individual may be, but is not required to be, an employee…"
  summary: 注意与 PCQI 区分：qualified individual 是岗位胜任力概念，覆盖所有操作工（含临时工与季节工，117.4(b) 明确包含），判定标准是"与其被分配职责相适应"。常识把"合格人员"理解为管理层资格，此处是指每一位上手干活的人。
  tags: [法定定义, 易混术语]

- id: t11
  title: critical control point (CCP)
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)
  source_quote: |
    "A point, step, or procedure in a food process at which control can be applied and is
    essential to prevent or eliminate a food safety hazard or reduce such hazard to an acceptable
    level."
  summary: 与 HACCP 定义一致。Ch6 明确：若工艺控制能在某点预防/消除危害或降至可接受水平，应将该点定为 CCP；但 Part 117 **不排除**使用 HACCP 术语，"在 CCP 上建立的最大/最小值"与"117.135(c)(1) 的 maximum/minimum value"在指南看来无实质差异（指南在本章混用 critical limit 一词）。
  tags: [法定定义, 核心概念]

- id: t12
  title: critical value / critical limit
  type: term
  source_chapter: Introduction III.B（Part 117 未定义，指南用法）；Ch6.5
  source_quote: |
    "A maximum and/or minimum value to which a biological, chemical, or physical parameter must
    be controlled to significantly minimize or prevent a hazard requiring a preventive control."
  summary: 食品安全红线（为显著减小/预防需控危害，参数必须被控到的最大/最小值）。区别于 HACCP 的 critical limit（绑定 CCP）：117 框架下所有预防控制（含非 CCP 的卫生、过敏原控制）都可以有关键限值。
  tags: [指南自定义, 核心概念]

- id: t13
  title: operating limits
  type: term
  source_chapter: Introduction III.B；Ch6.5
  source_quote: |
    "Criteria that could be more stringent than critical values/limits and are established for
    reasons other than food safety." / "Part 117 does not define the term 'operating limit.'"
  summary: 比关键限值更严格、基于**非食品安全**原因（通常是质量）设立的内控线。如烘焙关键限值 13 min，操作限 15 min——烤了 14 分钟没食品安全问题但质量可能不达标。与常识差异：这不是法规要求，是企业自设的"缓冲报警线"。
  tags: [指南自定义, 高频误读]

- id: t14
  title: adjustment
  type: term
  source_chapter: Introduction III.B；Ch6.5
  source_quote: |
    "An intervention that you take if you determine that there is a deviation from an operating
    limit, without a deviation from a critical value/critical limit." / "Part 117 does not define
    the term 'adjustment.'"
  summary: 只偏离操作限、未偏离关键限时采取的干预（如调回面团挤料量）。核心边界：adjustment **不触发**纠正措施程序、不作纠正措施记录——很多人把调机当成 corrective action，是过度反应。
  tags: [指南自定义]

- id: t15
  title: deviation
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "Failure to meet a critical value/critical limit or adhere to a critical parameter/critical
    factor."
  summary: 偏差=未满足关键值/关键限值，或未遵守关键参数/关键因素。触发纠正措施；发现偏差时应**假定自上次合格检查起全部未受控**（监控间隔越长，风险产品越多）。
  tags: [指南自定义]

- id: t16
  title: critical parameter / critical factor
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "A parameter that could, if varied, affect the adequacy of a preventive control to
    significantly minimize or prevent a hazard requiring a preventive control."
  summary: |-
    若变动会影响预防控制充分性的参数。指南在 Ch6 用更泛化的 process parameter 指非关键限值参数——术语分工：critical limit 管"值"，critical parameter 管"因素"（如颗粒尺寸、pH 达到时间）。
  tags: [指南自定义]

- id: t17
  title: process parameter
  type: term
  source_chapter: Ch6.5
  source_quote: |
    "We use the more general term 'process parameter' (rather than 'critical factor') when
    referring to parameters other than those specified in the examples with critical limits."
    Examples: "baking/cooking time, baking/cooking temperature, dough weight, particle size, belt
    speed, and pump speed."
  summary: 与过程交付相关的可测量/可观察因素（时间、温度、重量、带速、泵速等）。指南刻意区分：落在关键限值上的叫 critical limit，其余过程变量用 process parameter——避免 HACCP 用户把所有参数都升级为"关键因素"。
  tags: [指南自定义, Ch6]

- id: t18
  title: monitor
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)
  source_quote: |
    "To conduct a planned sequence of observations or measurements to assess whether control
    measures are operating as intended."
  summary: |-
    "计划好的"观察/测量序列，评估控制是否按预期运行。设计四问：What/How/How often/Who。监控只是记录并不能保证安全；连续监控最优，记录至少每日回查。记录可为 exception record（只记失控）。
  tags: [法定定义, 核心概念]

- id: t19
  title: correction
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；21 CFR 117.150(c)
  source_quote: |
    "An action to identify and correct a problem that occurred during the production of food,
    without other actions associated with a corrective action procedure (such as actions to reduce
    the likelihood that the problem will recur, evaluate all affected food for safety, and prevent
    affected food from entering commerce)."
  summary: 及时纠正生产中发生的轻微、孤立、未影响产品安全的问题（如生产前发现残渣重新清洁）；可不记录。判定边界不是主观的：①问题是否已影响食品；②孤立还是反复。**反复出现的问题不适用 correction**——那说明程序无效。
  tags: [法定定义, 核心概念, 高频误读]

- id: t20
  title: corrective action
  type: term
  source_chapter: Introduction III.B；21 CFR 117.150
  source_quote: |
    "An action to identify and correct a food safety problem that occurred during the production
    of food, including actions associated with a corrective action procedure (such as actions to
    reduce the likelihood that the problem will recur, evaluate all affected food for safety, and
    prevent affected food from entering commerce)."
  summary: 四步完整程序：①纠正并查明原因；②降低复发可能；③评估**所有**受影响食品的安全性；④阻止受影响食品进入流通。必须记录。与 correction 的分界线是"是否已影响食品"+"孤立 vs 反复"；遇未预见问题还须酌情再分析 FSP。
  tags: [指南自定义, 核心概念]

- id: t21
  title: validation
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；21 CFR 117.160
  source_quote: |
    "Obtaining and evaluating scientific and technical evidence that a control measure,
    combination of control measures, or the food safety plan as a whole, when properly
    implemented, is capable of effectively controlling the identified hazards."
  summary: 事前用科学/技术证据确认"控制措施**能**有效控制危害"（做对的事）。常被与 verification 混为一谈。关键例外：过敏原控制、卫生控制、召回计划、供应链计划**不需要** validation（117.160(c)）；其他控制经 PCQI 书面论证也可豁免。
  tags: [法定定义, 核心概念, 高频误读]

- id: t22
  title: verification
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)
  source_quote: |
    "The application of methods, procedures, tests and other evaluations, in addition to
    monitoring, to determine whether a control measure or combination of control measures is or
    has been operating as intended and to establish the validity of the food safety plan."
  summary: 监控之外的日常核查：仪器校准、记录审查（PCQI 在规定时间间隔内，一般 7 个工作日）、产品检测、环境监测等——回答"系统**正在/已经**按预期运行吗"。同一活动可归监控或验证，但不必双重设立（117.140(a) 的灵活性）。
  tags: [法定定义, 核心概念, 高频误读]

- id: t23
  title: significantly minimize
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)
  source_quote: |
    "To reduce to an acceptable level, including to eliminate."
  summary: 法定的"显著减小"=降到可接受水平，**包括消除**。注意"acceptable level"不是零：技术上不可能把微生物降到零。这是贯穿全书的控制程度上限表述——热处理、环境监测、供应链保证的终极目标都锚定在这两个字上。
  tags: [法定定义, 核心概念]

- id: t24
  title: prerequisite programs
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "Procedures, including Current Good Manufacturing Practices (CGMPs), that provide the basic
    environmental and operating conditions necessary to support the Food Safety Plan."
  summary: 为 FSP 提供基本环境与运行条件的程序（含 CGMP）。与常识差异：前提程序是 FSP 的**支持层**而非其中一部分，但部分前提程序（如卫生控制）可升格为预防控制——升格后即纳入管理组件闭环。质量原因做的卫生操作（如控霉分区）不属于食品安全意义上的卫生控制。
  tags: [指南自定义]

- id: t25
  title: exception record
  type: term
  source_chapter: Introduction III.B；Table 11-2；117.145(c)(2)
  source_quote: |
    "A record that is created only when there is loss of control." / "A record that you establish
    only when there is loss of control."
  summary: 仅在失控时才建立的监控记录。典型场景：自动条码扫描器只在检出错标时生成记录。大幅降低记录负担的合法设计——但前提是监控本身连续且能可靠捕获每次失控。常被误以为是"少记录"的漏洞，实际是法规明确允许的记录形式（117.145(c)(2)）。
  tags: [指南自定义, 记录]

- id: t26
  title: root cause investigation / root cause analysis
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "Root cause investigation: A procedure used to attempt to determine the root cause(s) of a
    contamination event by investigating all aspects of the manufacturing process, including the
    environment…"
  summary: 针对污染事件（最常见病原污染，也可用于 402 掺假/403(w) 错标）的回溯调查：查全部工艺环节**含环境**，找出根因并防止复发；root cause analysis 是对调查信息的回溯评估以决定消除根因的行动。与常识差异：不是泛管理概念，而是与纠正措施、再分析触发挂钩的法定配套程序。
  tags: [指南自定义]

- id: t27
  title: process control（工艺控制）
  type: term
  source_chapter: 21 CFR 117.135(c)(1)（法规正文）；Ch4、Ch6（指南用法）
  source_quote: |
    "(1) Process controls. Process controls include procedures, practices, and processes to
    ensure the control of parameters during operations such as heat processing, acidifying,
    irradiating, and refrigerating foods. Process controls must include, as appropriate…"
  summary: |-
    **中文对照锚点**：本技能统一用"工艺控制"指代法规英文 process control（§ 117.135(c)(1)，五类预防控制之一）。法定形态是"程序/实践/过程，确保运行期间参数受控"（热处理、酸化、辐照、冷藏等），且须包含 (i) 与危害控制相关的参数、(ii) 须控制的生物/化学/物理参数的**最大值、最小值或其组合**——后者即"关键限值"在法规里的正式形态。指南 Ch6 补充：若工艺控制能在某点预防/消除危害或降至可接受水平，应将该点定为 CCP；但 Part 117 **不排除** HACCP 术语，工艺控制不必然落在 CCP 上（§ 117.135(a)(2) 明确 CCP 是可选的）。
  tags: [法定定义, 核心概念, 工艺控制, process control]

# ============ 三、微生物与环境词族 ============

- id: t28
  title: environmental pathogen
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)
  source_quote: |
    "A pathogen capable of surviving and persisting with the manufacturing processing, packing, or
    holding environment such that food may be contaminated… Examples … include Listeria
    monocytogenes and Salmonella spp. but do not include the spores of pathogenic sporeforming
    bacteria."
  summary: 能在环境中存活并**持续存在**从而污染食品的病原。两个关键限定：①例举仅 L. mono 与 Salmonella；②**明确排除**致病性孢子形成菌的孢子——直接影响环境监测义务的适用范围。与常识差异：不是"车间里可能出现的任何病原"。
  tags: [法定定义, 核心概念]

- id: t29
  title: RTE (ready-to-eat) food
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)
  source_quote: |
    "Any food that is normally eaten in its raw state or any other food, including a processed
    food, for which it is reasonably foreseeable that the food will be eaten without further
    processing that would significantly minimize biological hazards."
  summary: 生食即可，或可合理预见**不经**进一步显著减小生物危害的加工即被食用。判定锚点是"消费前还有没有 kill step"，不是"看起来像即食"。RTE + 包装前暴露于环境 + 包装后无致死处理 → 环境病原评估成为危害分析的**强制项**（117.130(c)(1)(ii)，没有商量余地）。
  tags: [法定定义, 核心概念]

- id: t30
  title: TCS food (time/temperature control for safety food)
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "A food that requires time/temperature control for safety to limit growth of, or toxin
    formation by, pathogens."
  summary: 需要时间/温度控制以限制病原生长**或毒素形成**的食品。与常识差异：目的限定为"安全"（for safety）而非"品质"——冷藏保质的普通食品不是 TCS；且"毒素形成"与"生长"并列，提醒 S. aureus 等产毒菌不需大量增殖即可致害。
  tags: [指南自定义]

- id: t31
  title: transient contamination（瞬时污染）
  type: term
  source_chapter: Ch3 §3.3.5.2.1
  source_quote: |
    "Bacterial pathogens … are typically introduced into the processing facility through, for
    example, incoming raw materials, personnel, or pests. … the proper application of cleaning and
    sanitizing in accordance with CGMPs is adequate to control the transient bacteria…"
  summary: 病原经原料/人员/虫害带入环境后，按 CGMP 正常清洁消毒即可控制的暂时性存在。日常检测出的杂乱菌谱通常是 transient 的特征。
  tags: [Ch3, 环境病原]

- id: t32
  title: resident contamination / resident strain（定殖污染）
  type: term
  source_chapter: Ch3 §3.3.5.2.2
  source_quote: |
    "…the pathogens then become established in a harborage site, multiply, and persist for
    extended periods of time, even years. … common cleaning and sanitation practices … do not
    control the presence of resident contaminants once they have become established. … The
    facility will need to use intensified sanitation procedures to eliminate the contamination."
  summary: 病原在藏匿点定殖、增殖并持续数月甚至数年；常规清洁**无效**，需强化卫生程序根除。Salmonella 与 L. mono 是定殖史最丰富的两种。这是环境监测被法定化的根本原因：检测的意义就是赶在 transient 变 resident 之前发现。
  tags: [Ch3, 环境病原, 核心概念]

- id: t33
  title: harborage site / niche（藏匿点）
  type: term
  source_chapter: Ch3 §3.3.5.2.2
  source_quote: |
    "A harborage site, or niche, is a site in the environment or on equipment (e.g., junctions,
    cracks, holes, and dead-end areas) that enables the accumulation of residues (food debris,
    dust, and water) and permits the growth of microorganisms such as L. monocytogenes and
    Salmonella."
  summary: 设备接缝、裂纹、孔洞、死角等使残渣（食物残屑、尘、水）积聚并支持病原生长、且难以检查和触及（从而在例行清洁中保护病原）的部位。老旧设备比现代卫生设计设备更易形成 niche——这是设备设计作为危害评估十因素之一的原因。
  tags: [Ch3, 环境病原]

- id: t34
  title: primary Salmonella-controlled hygiene areas
  type: term
  source_chapter: Ch3 §3.3.5.3.2
  source_quote: |
    "We recommend that you remove water immediately from the primary Salmonella-controlled hygiene
    areas (areas where RTE food is exposed to the environment)… You should maintain dry conditions
    at all times in primary Salmonella-controlled hygiene areas, except for the occasions when you
    have determined that controlled wet cleaning is necessary."
  summary: 干环境（RTE 食品暴露于环境的区域）的核心控制区，应**始终干燥**，仅经判定需要受控湿清洁（controlled wet cleaning）时例外。控水逻辑：干区积水处与积水已干处都可能藏匿沙门氏菌，后者还有含菌粉尘的空气传播风险。这是"湿区防李斯特靠干燥、干区防沙门靠控水"二分法的干区制度。
  tags: [Ch3, 环境病原, 卫生分区]

- id: t35
  title: hygienic zoning
  type: term
  source_chapter: Ch4 §4.4.2；Table 4（4.4.2）
  source_quote: |
    "Using hygienic zoning for separation of process operations such as raw vs. Work-in-Process
    (WIP) vs. finished product; wet vs. dry; personnel and materials flow; air balance." / "The
    objective of hygienic zoning is to reduce the potential for transient pathogens to enter…"
  summary: 按生/WIP/成品、湿/干、人流物流、气压平衡对作业区做物理分隔。两个易错点：①目标明确是阻止 transient 病原进入；②为控霉等**质量**原因做的分区不属于本指南定义的（食品安全）卫生控制。
  tags: [Ch4, 卫生分区]

- id: t36
  title: reduced oxygen packaging (ROP)
  type: term
  source_chapter: Ch3 §3.3.4.2.4；Appendix 1 A1.7.1
  source_quote: |
    "…reduced oxygen packaging (ROP) to prevent the growth of spoilage organisms and extend the
    [shelf life]…" / ROP 可延长货架期但可能造成 C. botulinum 生长环境（process-related biological hazard）。
  summary: 真空/气调等减氧包装的统称。危险机制：抑制好氧腐败菌的同时利于厌氧的 C. botulinum——"可能先产毒后腐败"，无感官警讯。指南判定规则：无 C. botulinum 屏障（aw<0.93 / pH<4.6 / 盐>10% / 最终容器热处理 / 冷冻储运）不得使用 ROP；低温抑制不可作为唯一屏障。
  tags: [Ch3, 过程危害]

- id: t37
  title: danger zone
  type: term
  source_chapter: Ch4 §4.3.2.1
  source_quote: |
    "…temperature range of concern (41°F (5°C) to 135°F (57°C)) the 'danger zone.' … no more
    than 4 hours in the danger zone (41°F (5°C) to 135°F (57°C)). Different pathogens have
    [different characteristics]…"
  summary: 41–135°F（5–57°C）的病原生长温度区间。关键警示：**4 小时规则是经验法则**，实际安全时限取决于病原与食品特性（Food Code 两段式冷却：135→70°F ≤2h、70→41°F ≤4h；FSIS 版协议不同），可基于自身产品研究设限，也可参照附录 3 Table 3-B/C。
  tags: [Ch4, 时间温度]

- id: t38
  title: lethality treatment / kill step
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "Lethality treatment: A process that is used to significantly minimize (kill, destroy)
    viruses, parasites, or the vegetative cells of bacteria or to inactivate spores of sporeforming
    bacteria." / "Kill step: Lethal processing to significantly minimize biological hazards."
  summary: 致死处理：杀灭/破坏（kill, destroy）病毒、寄生虫或细菌**营养细胞**，或使孢子失活（inactivate）。措辞差异是刻意的技术区分：营养细胞用 kill，孢子用 inactivate。易错点：本章热处理只杀营养细胞**不灭孢子**，也不消除已形成的 S. aureus / B. cereus 毒素。
  tags: [指南自定义, 核心概念, Ch6]

- id: t39
  title: non-lethality treatment
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "A process that is used to minimize or prevent the growth of microorganisms (e.g.,
    time/temperature controls, most formulation controls, and dehydration/drying) rather than for
    the purpose of killing/destroying them."
  summary: 抑制生长而非杀灭的处理：时间/温度控制、多数配方控制（a_w、pH）、干燥/脱水。与致死处理的分工决定验证策略：致死处理需要 validation，非致死处理的抑制效果同样要科学确立但不叫"杀菌"。常见误解是"晒干了=细菌死了"——脱水只是让它长不了。
  tags: [指南自定义, Ch6]

- id: t40
  title: EPIPT (End-Point Internal Product Temperature)
  type: term
  source_chapter: Introduction III.B；Ch4 §4.3.1.1；Ch6
  source_quote: |
    "A measurement of the internal product temperature at the end of the heat process."
  summary: 热处理结束时产品内部温度；经研究确立后可用"终点温度达标"替代全程时间-温度监控。三个前提：热分布研究（找冷点）+ 热穿透研究（最慢加热产品、最坏条件）+ 识别其他影响加热速率的关键因素；且仅可在研究所覆盖条件下使用。是降低连续/批式热处理监控负担的核心工具。
  tags: [指南自定义, Ch6, 工艺控制]

- id: t41
  title: pertinent pathogen
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "A known or reasonably foreseeable pathogen that requires a preventive control and is the
    most difficult to control by the process (e.g., the pathogen that has the greatest resistance
    to a lethality treatment or that is least impacted by a non-lethality treatment)."
  summary: 相关病原=需控危害中该工艺**最难控制**的病原（对致死处理耐受力最强，或对非致死处理最不敏感）。热处理工艺的目标菌就按它选定——如冷藏热灌装汤选非蛋白分解 C. botulinum type B，而非更常见的李斯特菌。选错目标菌=工艺看似达标实则无效。
  tags: [指南自定义, Ch6]

- id: t42
  title: surrogate microorganism
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "A non-pathogenic microorganism that has survival and/or growth capabilities that are similar
    to, or more robust than, the pertinent pathogen under the conditions being evaluated."
  summary: 验证研究中替代病原使用的**非致病**微生物，生存/生长能力须与相关病原相当或更强（宁强勿弱）。解决"不能往车间里故意投放病原"的现实问题；target microorganism = 验证研究中被评价的 pertinent pathogen 或其 surrogate 的合称。
  tags: [指南自定义, Ch6, 验证]

- id: t43
  title: microbial challenge study
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "A study in which a preventive control is 'challenged' by a pathogen or surrogate
    microorganism to determine the impact of the preventive control on the pathogen or its
    surrogate."
  summary: 用病原或替代菌"攻击"预防控制，以确定其影响的研究——配方/货架期控制（尤其 ROP、多组分界面）验证的主力工具，参照 NACMCF 攻击试验参数指南。与常识差异：不是抽检产品，而是主动接种的定向实验设计。
  tags: [指南自定义, 验证]

- id: t44
  title: D-value
  type: term
  source_chapter: Appendix 3；Ch4 §4.3.1.1
  source_quote: |
    "The time required to destroy 90 percent of the vegetative cells or spores at a given
    temperature is called the decimal reduction time, usually referred to as the 'D-value'… The
    D-value usually varies inversely with temperature."
  summary: 指定温度下消灭 90% 营养细胞或孢子所需时间（降一个 log10）。注意附录 3 版本把孢子也纳入（不限于营养细胞）。D 值通常与温度反向变化——这就引出 z 值。TDT（thermal death time，杀灭给定数量微生物所需时间）是 D 值的母概念。
  tags: [Appendix 3, 定量微生物]

- id: t45
  title: z-value
  type: term
  source_chapter: Appendix 3
  source_quote: |
    "A 'z-value' is derived from the reciprocal of the slope of the best straight line and is
    equal to the increase in the number of degrees (from a given starting temperature) that
    results in a 90 percent reduction in the D-value."
  summary: 使 D 值降为 1/10（降 90%）所需升高的温度数；log D–温度曲线斜率的倒数。D 值+ z 值共同刻画菌株在某温度下的热耐受性，是比较不同微生物热抵抗、跨温度换算致死率的工具（如 Table 3-D 以 z=13.5°F 计算 L. mono 致死率）。
  tags: [Appendix 3, 定量微生物]

- id: t46
  title: 6D process
  type: term
  source_chapter: Appendix 3（Table 3-D / 3-E）
  source_quote: |
    "The times provided are the length of time at the designated internal product temperature
    necessary to deliver a '6D' process for L. monocytogenes (i.e., a process that will accomplish
    a 6 logarithm (factor of 1,000,000) reduction in the number of L. monocytogenes)."
  summary: 6 个对数（百万倍）减少的处理。速查值：L. mono 158°F(70°C)/2 min；非蛋白分解 C. botulinum type B 194°F(90°C)/10 min。表值为保守值、适用于所有食品；可经热致死时间研究建立更短工艺，初始菌量低也可接受较低破坏程度——6D 不是法定通用标准而是默认保守设计。
  tags: [Appendix 3, 定量微生物, 核心概念]

- id: t47
  title: lethal rate
  type: term
  source_chapter: Appendix 3（Table 3-D）
  source_quote: |
    "Lethal rate, as used in Table 3-D, is the relative lethality of 1 minute at the designated
    internal product temperature as compared with the lethality of 1 minute at the reference
    internal product temperature of 158°F (70°C) (using a z = 13.5°F (7.5°C))."
  summary: 相对致死率：指定内部产品温度下 1 分钟相对参照温度（70°C）1 分钟的致死当量（如 1 min@145°F = 0.117×）。用于把非参照温度下的暴露时间折算累积致死效果——温度曲线积分计算 F 值的基础。
  tags: [Appendix 3, 定量微生物]

# ============ 四、过敏原词族 ============

- id: t48
  title: food allergen / major food allergen
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；FD&C Act 201(qq)
  source_quote: |
    "Food allergen: A major food allergen as defined in section 201(qq) of the Federal Food, Drug,
    and Cosmetic Act." 201(qq): "Milk, egg, fish…, Crustacean shellfish…, tree nuts…, wheat,
    peanuts, soybeans, and sesame or a food ingredient that contains protein derived from one of
    these foods, with certain exceptions regarding highly refined oils."
  summary: "九大类（'八大'+FASTER Act 2021 加入的芝麻，2023-01-01 起）或含其蛋白的配料；高度精炼油豁免。两个边界：①cochineal extract/carmine 等须按色素法规申报但**不是** 117 意义上的 food allergen；②不耐受物质（乳糖、亚硫酸盐、麸质）是化学危害但不入过敏原控制类别。"
  tags: [法定定义, 过敏原]

- id: t49
  title: allergen cross-contact
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)
  source_quote: |
    "The unintentional incorporation of a food allergen into a food."
  summary: 过敏原被**无意**引入食品。法定边界：FD&C 403(w) 的标签申报要求**不适用于**交叉接触引入的过敏原——交叉接触是安全性/掺假（402(a)(4)）问题而非标签问题。这意味着"标签合规"救不了交叉接触，必须靠 CGMP+预防控制。
  tags: [法定定义, 过敏原, 核心概念]

- id: t50
  title: unintended allergen presence (UAP)
  type: term
  source_chapter: Introduction III.B；Table 11-2（脚注 8）
  source_quote: |
    "The presence of an allergen due to allergen cross-contact." / "In the draft Chapter 3 … we
    used the terminology 'undeclared allergen' … When we finalize that chapter, we intend to use
    the terminology 'unintended allergen presence.'"
  summary: 因交叉接触导致的过敏原存在。术语沿革：2016 草案 Ch3 用 undeclared allergen，定稿拟统一改用 UAP——它是 FDA 刻意造的词，把"存在"与"是否已申报"拆开：UAP 是安全（掺假）问题，申报义务是标签问题。
  tags: [指南自定义, 过敏原]

- id: t51
  title: allergenic ingredient vs. allergenic component
  type: term
  source_chapter: Introduction III.B；Table 11-2
  source_quote: |
    "Allergenic component: A food allergen … that is a component of an ingredient (e.g., the food
    allergen 'milk' in a spice blend)." / "Allergenic ingredient: A food allergen … that is an
    ingredient of another food product (e.g., the food allergen 'peanuts' added to cookies)."
  summary: 前者=作为**配料**的过敏原（加进曲奇的花生）；后者=配料中所**含**的过敏原组分（香料混合物里的奶）。区分决定标签来源命名的追查深度（要穿透复配料找到过敏原组分）与交叉接触评估的对象。
  tags: [指南自定义, 过敏原]

- id: t52
  title: food allergen profile
  type: term
  source_chapter: Introduction III.B；Table 11-2
  source_quote: |
    "The food allergen sources present or absent in a food."
  summary: 某食品中过敏原来源的**存在/缺失**情况。排产规则（like into like / exact into exact）都以 profile 为单位：上一产品含下一产品没有的过敏原 → 需过敏原清洁；返工料只能回加到相同过敏原谱的产品。
  tags: [指南自定义, 过敏原]

- id: t53
  title: allergen cleaning procedure
  type: term
  source_chapter: Introduction III.B；Table 11-2
  source_quote: |
    "Procedures, practices, and processes for cleaning food-contact surfaces of equipment and
    utensils that are used for foods with different food allergen profiles."
  summary: 针对同一设备生产**不同过敏原谱**食品的清洁程序；作为预防控制时必须书面（区别于 CGMP 一般清洁）。验证活动谱系：目视 visibly clean → ATP/蛋白拭子（非特异）→ 过敏原特异性检测盒 → push-through 物/首件产品检测。可只监测步骤不做擦拭验证，但数量与性质须足以确保有效。
  tags: [指南自定义, 过敏原]

- id: t54
  title: visibly clean
  type: term
  source_chapter: Introduction III.B；Table 11-2
  source_quote: |
    "Without visibly detectable material such as food residue, film, or protein sheen."
  summary: 无可见可检物质（食物残渣、膜、蛋白光泽）。它是过敏原清洁验证链条的**最基础一档**，也是唯一"免费"的验证活动；但 ATP/蛋白拭子等更灵敏手段也非特异、未必能检出特定致敏蛋白——不能仅凭阴性结论清洁有效。
  tags: [指南自定义, 过敏原]

- id: t55
  title: changeover
  type: term
  source_chapter: Introduction III.B；Table 11-2
  source_quote: |
    "Procedures used to prepare the processing line when different products are produced on the
    same processing line."
  summary: 同一产线换产不同产品时的准备程序。是排产策略（无过敏原→少→多）与过敏原清洁程序的衔接点；排产被打乱时只要前一产品含后续产品没有的过敏原，就需执行过敏原清洁。
  tags: [指南自定义, 过敏原]

- id: t56
  title: work-in-process (WIP)
  type: term
  source_chapter: Introduction III.B；Table 11-2
  source_quote: |
    "Partially finished products that are in between different production stages (e.g., batched or
    pre-processed ingredients that are transferred to totes and held until moved to another
    processing line to be incorporated into another product)."
  summary: 处于生产阶段之间的半成品（如转桶暂存待转入另一产线的预加工配料）。卫生分区中 WIP 是独立隔断类别（raw / WIP / finished），因其"既非生也非终"的双重污染风险。
  tags: [指南自定义]

- id: t57
  title: rework
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；Table 11-1
  source_quote: |
    "Clean, unadulterated food that has been removed from processing for reasons other than
    insanitary conditions or that has been successfully reconditioned by reprocessing and that is
    suitable for use as food."
  summary: 合法返工的三个限定：出于**非不卫生**原因移出、或经再加工成功复原、适合作食品用的洁净未掺假食品。过敏原语境下的硬规则：返工料尽量回加到相同成品（exact into exact）；否则只能加入相同过敏原谱的其他产品。因卫生原因撤下的料不叫 rework。
  tags: [法定定义, 过敏原]

- id: t58
  title: allergen advisory statement
  type: term
  source_chapter: Ch11 §11.1、11.9
  source_quote: |
    "Allergen advisory statement" 如 "may contain [allergen]" 类预防性标签（旧称 allergen precautionary labeling）。
  summary: "咨询声明**不能替代** CGMP 或交叉接触预防控制；使用需 PCQI 书面论证，且声明须真实不误导。接收带声明的来料时须三选一：①产品已含该过敏原（已申报）→无影响；②传递声明到自家标签+按过敏原配料管理；③依据阈值数据的科学有效确定认为量足够低→不加声明。FDA 未设定过敏原免申报最大限量。"
  tags: [Ch11, 过敏原, 高频误读]

- id: t59
  title: label control（含 label content / label management control）
  type: term
  source_chapter: Introduction III.B；Ch11 §11.7
  source_quote: |
    "Label control: Procedures, practices, and processes employed for labeling the finished food,
    including ensuring that the finished food is not misbranded under section 403(w) of the FD&C
    Act."
  summary: 分两支：label content control（确保标签**内容**正确：成分声明/品名/Contains 声明）与 label management control（确保**正确标签**用于正确产品：色码、staging、电子文件选择）。指南强调：落实标签控制本身比分类更重要，两类可共用单一监控/验证活动与记录（117.140(a)）。
  tags: [指南自定义, 过敏原]

# ============ 五、供应链词族 ============

- id: t60
  title: supplier
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；Ch15
  source_quote: |
    "The establishment that manufactures/processes the food, raises the animal, or grows the food
    that is provided to a receiving facility without further manufacturing/processing by another
    establishment, except for further manufacturing/processing that consists solely of the
    addition of labeling or similar activity of a de minimis nature."
  summary: 关键边界：供应商是**实际制造/加工/饲养/种植**的企业。从经纪商/分销商或零售店采购时，供应商是链条上游的实际生产者而非中间商——不能把经纪商当供应商批准。标签等 de minimis 活动不算进一步加工。
  tags: [法定定义, 供应链, 高频误读]

- id: t61
  title: receiving facility
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；Ch15
  source_quote: |
    "A facility that is subject to subparts C and G of this part and that
    manufactures/processes a raw material or other ingredient that it receives from a supplier."
  summary: 受 subparts C/G 约束且对所收原料进行制造/加工的设施。两个限定都关键：仅储存不加工的设施不是 receiving facility；供应商不能自审、自证，只有 receiving facility 能批准供应商（117.415）。
  tags: [法定定义, 供应链]

- id: t62
  title: supply-chain-applied control
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；Ch15
  source_quote: |
    "A preventive control for a hazard in a raw material or other ingredient when the hazard in
    the raw material or other ingredient is controlled before its receipt."
  summary: 原料危害在其被**接收之前**即受控的预防控制——供应链控制的本质是"把控制前移到接收之前"。与常识差异：这不是泛指"对供应商做管理"，而是一个明确的预防控制类别，触发整套供应链程序（批准供应商、验证活动、18 项记录）。危害在自身设施控制时无需建立供应链计划。
  tags: [法定定义, 供应链, 核心概念]

- id: t63
  title: approved supplier
  type: term
  source_chapter: Introduction III.B；Table 15-3
  source_quote: |
    "A supplier that has met the criteria of the receiving facility's supply chain program, is
    controlling a hazard identified by the receiving facility as requiring a supply-chain-applied
    control, and has been approved by the receiving facility in accordance with the requirements
    of part 117, subpart G."
  summary: 三要素：满足收货方供应链计划标准+正在控制所识别危害+按 subpart G 获批准。必须在**收货前**批准并记录（117.420）；临时使用未批准供应商的原料须在接收使用前充分验证。
  tags: [指南自定义, 供应链]

- id: t64
  title: certificate of analysis (COA) / certificate of conformance (COC)
  type: term
  source_chapter: Introduction III.B；Table 15-3
  source_quote: |
    "A document, provided by the supplier of a food prior to or upon receipt of the food, that
    documents the analysis of certain characteristics and attributes of the food." COC: "…states
    that the processing of the food and/or the food itself conform to certain specifications."
  summary: COA=记录分析**结果**的文件；COC=声明符合规格的承诺文件。二者都是供应商可提供的验证活动（供应商不能自审或审查自己的记录，但可以提供检测与第三方审核）。COA 数据须与其他活动配合使用——检测只能是补充，永远不能是唯一手段。L.mono 专项的更精确定义与字段要求（接收前/接收时提供、COC 须含保证期与产品安全规格、COA 须含检出限）见 t98。
  tags: [指南自定义, 供应链]

- id: t65
  title: audit / second-party audit / third-party audit
  type: term
  source_chapter: Introduction III.A + III.B；Table 15-3
  source_quote: |
    "Audit: The systematic, independent, and documented examination (through observation,
    investigation, records review, discussions with employees of the audited entity, and, as
    appropriate, sampling and laboratory analysis) to assess an audited entity's food safety
    processes and procedures." "Second-party audit: An audit conducted by an employee of a
    receiving facility." "Third-party audit: An audit conducted by a qualified auditor that is not
    an employee of either the receiving facility or the supplier."
  summary: 系统性、独立、有记录的检查。二方=收货设施员工执行；三方=非双方员工的 qualified auditor 执行。不能接受的"验证活动"：供应商自审、供应商审查自己的记录。1 年内 FDA 等机构"适当"检查的书面结果可替代审核；USDA 有机认证检查、外国政府 HACCP 证书不能。
  tags: [法定定义+指南自定义, 供应链]

- id: t66
  title: qualified auditor
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；Table 15-2
  source_quote: |
    "A person who is a qualified individual as defined in this part and has technical expertise
    obtained through education, training, or experience (or a combination thereof) necessary to
    perform the auditing function as required by 21 CFR 117.180(c)(2). Examples …: (1) A government
    employee, including a foreign government employee; and (2) An audit agent of a certification
    body that is accredited in accordance with … part 1, subpart M."
  summary: 双重资格：qualified individual + 审计所需技术专长。法定例举：政府雇员（含外国政府）、按 part 1 subpart M 认可的认证机构的审核代理。所有现场审核（onsite audit）必须由 qualified auditor 执行（117.435）；验证活动不得存在影响结果的经济利益冲突。
  tags: [法定定义, 供应链]

- id: t67
  title: SAHCODH hazard
  type: term
  source_chapter: Introduction IV 缩写；Table 11-2、15-3；Ch15 §15.11.2
  source_quote: |
    "Serious adverse health consequences or death to humans hazard: A hazard for which there is a
    reasonable probability that exposure to the hazard will result in serious adverse health
    consequences or death to humans."
  summary: 暴露后有合理概率导致人类严重健康后果或死亡的危害——对应 Class I 召回级别。法规杠杆：若危害由供应商控制且为 SAHCODH → 验证活动**必须**是现场审核，首次使用前+至少每年一次；唯一例外是 PCQI 书面认定替代方案。多数食物过敏原危害属 SAHCODH。含 SAHCODH 危害的违规产品属 reportable food。
  tags: [核心概念, 供应链, 召回]

- id: t68
  title: qualified facility / very small business
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；Table 15-2
  source_quote: |
    "Very small business: A business (including any subsidiaries and affiliates) averaging less
    than $1,000,000, adjusted for inflation, per year, during the 3-year period preceding the
    applicable calendar year in sales of human food plus the market value of human food … without
    sale." Qualified facility: very small business 或直接销售给 qualified end-users 金额超过其他购买者且年销售总额低于 $500,000 的设施。
  summary: 极小企业=前 3 年人均年销售额（含无销售持有食品市值）低于 100 万美元（通胀调整）。qualified facility 是部分豁免 PCHF 的资格身份，但状态**可能逐年变动**（qualified ↔ not qualified），供应链验证相应改为书面保证（批准前+每年 12 月 31 日前状态保证）。
  tags: [法定定义, 豁免体系]

- id: t69
  title: written procedures for receiving raw materials and other ingredients
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)；Table 15-2
  source_quote: |
    "Written procedures to ensure that raw materials and other ingredients are received only from
    suppliers approved by the receiving facility (or, when necessary and appropriate, on a
    temporary basis from unapproved suppliers whose raw materials or other ingredients are
    subjected to adequate verification activities before acceptance for use)."
  summary: 收货书面程序：确保原料仅从批准供应商接收（临时例外：未批准供应商原料须在接收使用前充分验证），并记录使用。落地做法：纸质批准清单打勾核对、软件交叉核对采购单-供应商-物料并设防呆。
  tags: [法定定义, 供应链]

# ============ 六、化学危害词族 ============

- id: t70
  title: action level / defect action level
  type: term
  source_chapter: Ch12 §12.3.5；Introduction III.A（defect action level）
  source_quote: |
    "An action level is a level of contamination at which [food may be considered adulterated
    under FD&C Act 402(a)(1)] (see 21 CFR 109.6(d)). In this chapter, 'contaminant levels' include
    action levels, guidance levels, advisory levels…" / "Defect action level: A level of a
    non-hazardous, naturally occurring, unavoidable defect at which FDA may regard a food product
    'adulterated' … under section 402(a)(3)."
  summary: 两个极易混淆的概念：action level（Ch12）针对**有毒有害污染物**（如无机砷、铅），达到即可能按 402(a)(1) 认定掺假；defect action level（117.3）针对**无毒、天然、不可避免**的缺陷（如昆虫碎片），按 402(a)(3) 处理。语义关键：二者均以污染物"不可避免"为前提，不代表可避免时的允许水平；无 action level 时 FDA 可在最低检出水平执法。
  tags: [Ch12, 化学危害, 易混术语]

- id: t71
  title: economically motivated adulteration (EMA)
  type: term
  source_chapter: Ch3 §3.4.1.6；Ch12（117.130(b)(2)(iii)）
  source_quote: |
    危害分析必须考虑可能为经济目的故意引入的危害（117.130(b)(2)(iii)）；FDA 建议聚焦历史上存在此类掺假模式的情况（Table 3-8：三聚氰胺、铅盐增色香料、Sudan I 等）。
  summary: 为经济利益故意引入的物质（三聚氰胺虚增蛋白、姜黄加铬酸铅增色等）。判定焦点是**历史掺假模式**+配料原产国与特定供应商；判定需要预防控制时通过供应链计划解决。与常识差异：掺假进入危害分析的通道是"是否构成食品安全危害"，纯经济欺诈不在此列。
  tags: [Ch12, 化学危害]

- id: t72
  title: toxic elements
  type: term
  source_chapter: Appendix 1 A1.6.2.3；Ch12
  source_quote: |
    原称"重金属"（heavy metals）的化学危害：砷（arsenic）、镉（cadmium）、铅（lead）、汞（mercury）；汞主要是海产品危害，本指南/本附录不涉及。
  summary: 术语更新：官方已弃用"重金属"改称 toxic elements。Ch12 婴幼儿食品示例的关键判定：铅因种植区污染可能+婴幼儿脆弱人群→需预防控制（供应链程序）；砷镉仅对大米等富集作物成立。Closer to Zero 行动计划未来可能设定更多 action level。
  tags: [Appendix 1, 化学危害]

- id: t73
  title: mycotoxins
  type: term
  source_chapter: Appendix 1 A1.6.2.6；Ch12
  source_quote: |
    霉菌（真菌）在田间与贮藏期产生的毒性代谢物：黄曲霉毒素（花生/干玉米/树坚果）、伏马毒素（干玉米）、DON/呕吐毒素（小麦大麦）、赭曲霉毒素（咖啡/葡萄干/谷物）、棒曲霉素（苹果）。
  summary: 真菌毒素按"毒素-商品"对应关系评估。DON 案例链（Miller C→Baker D→Sandwich F）展示"条件性升格"：季节性信息恶化（新麦、USDA 周报、检测升高）时，原本不需预防控制的操作要升格为预防控制并加大验证——危害分析不是一劳永逸的静态结论。
  tags: [Appendix 1, Ch12, 化学危害]

# ============ 七、召回词族 ============

- id: t74
  title: recall / recall classification
  type: term
  source_chapter: Introduction III.B（引 21 CFR 7.3）；Ch14 Table 14-1
  source_quote: |
    "A firm's removal or correction of a marketed product that FDA considers to be in violation of
    the laws it administers… 'Recall' does not include a market withdrawal or a stock recovery."
    Class I: "reasonable probability that the use of, or exposure to, a violative product will
    cause serious adverse health consequences or death"; Class II: "temporary or medically
    reversible"; Class III: "not likely to cause illness or injury."
  summary: 三级分类：I=合理概率致严重后果或死亡；II=可能致暂时/可逆后果或严重后果概率遥远；III=不太可能致病伤。注意排除项：市场撤回（market withdrawal）与存货回收（stock recovery）不算召回；FDA Enforcement Report 网页发布不等于"公众警告"（后者保留给紧急严重危害）。
  tags: [Ch14, 召回, 核心概念]

- id: t75
  title: consignee / direct consignee / direct account
  type: term
  source_chapter: Ch14 Table 14-1（引 21 CFR 7.3、117.139）
  source_quote: |
    "Consignee: … anyone who received, purchased, or used the product being recalled." "Direct
    account: The term used in FDA's recall policy in 21 CFR part 7, subpart C to mean the first
    consignee in a recalling firm's distribution chain." "Direct consignee: The term used in 21
    CFR 117.139 to mean the first consignee… Part 117 uses the term 'direct consignee' to have the
    same meaning as 'direct account.'"
  summary: 收货人=收到、购买或使用了被召回产品的任何人；direct consignee（117.139 用语）与 direct account（part 7 用语）同义=分销链第一个收货人。召回计划第一程序就是通知直接收货人并说明退还/处置方法。
  tags: [Ch14, 召回]

- id: t76
  title: reportable food
  type: term
  source_chapter: Ch14 §14.7.1（FD&C 417）
  source_quote: |
    "A 'reportable food' is an article of food (other than dietary supplements or infant formula)
    for which there is a reasonable probability that the use of, or exposure to, such article of
    food will cause serious adverse health consequences or death to humans or animals."
  summary: 报告食品：合理概率使用或接触将致人（或动物）严重健康后果或死亡的食品（膳食补充剂与婴儿配方除外）。责任方须在确定后 **24 小时内**电子通知 FDA（RFR）。建议把 RFR 程序或交叉引用放进召回计划以便随时可得。
  tags: [Ch14, 召回]

# ============ 八、酸化食品与 LACF 词族 ============

- id: t77
  title: LACF (low-acid canned food)
  type: term
  source_chapter: Ch4 §4.3.1.1；Ch6.1；Appendix 1 A1.5.5
  source_quote: |
    低酸罐装食品=密封容器热加工低酸食品，21 CFR part 113 管辖；其杀菌环节的微生物危害不适用 PCHF 危害分析要求（但其化学与物理危害仍适用）。
  summary: 双法规体系的一极（part 113 vs PCHF）。牛奶巴氏杀菌另有 21 CFR 1240.61 与 PMO。判定"哪些规则对我适用"与规则本身同等重要——LACF 杀菌活动豁免 PCHF 生物危害要求，但别把化学/物理危害也一起豁免了。
  tags: [豁免体系, Ch4]

- id: t78
  title: acidified foods
  type: term
  source_chapter: Ch4 §4.3.3.2（引 21 CFR 114.3(b)）；Introduction III.A
  source_quote: |
    低酸食品加酸或酸性食品、a_w>0.85、成品平衡 pH≤4.6（21 CFR 114.3(b)）。注意 117.3 的定义将 "Acid foods or Acidified foods" 合并定义为 "Foods that have an equilibrium pH of 4.6 or below."
  summary: 注意术语双轨：part 114 的酸化食品定义含四要素（低酸+加酸+a_w>0.85+平衡 pH≤4.6），而 117.3 词汇表把 acid foods/acidified foods 简并为"平衡 pH≤4.6 的食品"。受 PCHF 约束的酸化食品企业须同时遵守 108.25/part 114 全部要求，双向借用程序记录但专项要求（Form 2541e 提交、3 年记录、容器编码）不可免除。
  tags: [Ch16, 豁免体系, 易混术语]

- id: t79
  title: scheduled process
  type: term
  source_chapter: Ch16 §16.2.1（引 21 CFR 114.3(e)）；Ch4 §4.3.3.2
  source_quote: |
    "…the process selected by a processor as adequate for [the manufacture of a food that] will
    not permit the growth of microorganisms of public health significance… includes control of pH
    and other critical factors equivalent to the process established with a competent process
    authority."
  summary: 加工者选定、足以使食品不允许公共健康意义微生物生长的工艺（含 pH 及其他关键因素控制），须向 FDA 申报（Form FDA 2541e）。成品平衡 pH 须在 scheduled process 指定时间内达到并保持 ≤4.6，且须频繁检测记录（114.80(a)(2)）。
  tags: [Ch16, 酸化食品]

- id: t80
  title: equilibrium pH
  type: term
  source_chapter: Ch4 §4.3.3.2；Ch16
  source_quote: |
    "An equilibrium pH is achieved [when all components have reached their natural pH
    equilibrium]… products that require several days to reach equilibrium pH to prevent the growth
    of C. botulinum."
  summary: 所有配料达到天然 pH 平衡后的成品 pH（大颗粒食品可能需数天）。最重要的陷阱：多组分界面微环境的 pH/aw 可与任一组分显著不同（泡芙皮馅、鹰嘴豆泥+顶部装饰）——各组分单独达标≠组合达标。
  tags: [Ch16, 酸化食品, 高频误读]

- id: t81
  title: water activity (a_w) / safe-moisture level
  type: term
  source_chapter: Introduction III.A (21 CFR 117.3)
  source_quote: |
    "Water activity (a_w): A measure of the free moisture in a food and is the quotient of the
    water vapor pressure of the substance divided by the vapor pressure of pure water at the same
    temperature." / "Safe-moisture level: A level of moisture low enough to prevent the growth of
    undesirable microorganisms in the finished product under the intended conditions…"
  summary: a_w=食品中自由水分的度量（水汽压之商）；安全水分水平=预期条件下足以防止不良微生物生长的水平。关键数值判据：a_w≤0.85 病原不能生长（S. aureus 界限）；a_w≤0.92 抑制芽孢萌发；ROP 屏障用 0.93。面包悖论：瓤 a_w 0.95 但靠 pH/外壳/霉菌先行等多重屏障保安全——"面包在变得危险之前先变质"。
  tags: [法定定义, 配方控制, 核心概念]

- id: t82
  title: process authority
  type: term
  source_chapter: Ch6 §6.9、6.16.1（脚注 7）
  source_quote: |
    "You also could obtain this information from a process authority that has knowledge about
    process parameters and minimum/maximum values (e.g., critical limits) for the product being
    produced."（Part 117 本身不强制该头衔）
  summary: 具备专业资格确立加工工艺的权威人士，可受托识别需关键限值的工艺参数并确定限值。与 part 114 的"胜任加工权威机构"（competent process authority）衔接。注意：委托专家完成的工作仍须纳入书面 FSP 并由 PCQI 负责——外包了工作，没外包责任。
  tags: [Ch6, 验证]

- id: t83
  title: cleaning / sanitize / controlled wet cleaning
  type: term
  source_chapter: Introduction III.B；Table 11-2
  source_quote: |
    "Cleaning: The removal of soil, including food residue, dirt, grease or other objectionable
    matter, from a surface." / "Sanitize: To adequately treat cleaned surfaces by a process that
    is effective in destroying vegetative cells of pathogens, and in substantially reducing
    numbers of other undesirable microorganisms, but without adversely affecting the product or
    its safety." / "Controlled wet cleaning: … using a limited amount of water and detergents and
    controlling the spread of the water used."
  summary: 三段术语：cleaning 去 soil（part 117 本身未定义 cleaning）→ sanitize 对已清洁表面杀灭病原营养细胞（先清洁后消毒，顺序不可反）→ controlled wet cleaning 是干区的限定用水版湿清洁。干环境湿清洁后必须彻底干燥再使用（117.35(d)）；湿区避免高压水枪（气溶胶扩散 L. mono）。
  tags: [指南自定义, 卫生]

- id: t84
  title: sanitation break
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "Stopping production to clean and sanitize all food-contact surfaces (FCSs) in the production
    system."
  summary: 停产以清洁消毒生产系统中**所有**食品接触面。与常识差异：不是"抽空擦一下"，是系统性停产清洁节律，通常与湿环境 L. mono 控制策略配套（生产期- sanitation break - 干燥期的循环）。
  tags: [指南自定义, 卫生]

- id: t85
  title: kill step cooking instructions vs. heating instructions
  type: term
  source_chapter: Introduction III.B
  source_quote: |
    "Cooking instructions: Instructions to heat-process food using a kill step (e.g., by baking,
    boiling, or microwave cooking)." / "Heating instructions: Instructions for consumers to
    heat-process food without using a kill step (e.g., through warming or through surface heat
    treatments (such as toasting))." / "Adequate cooking instructions: Cooking instructions that
    are adequate to significantly minimize biological hazards."
  summary: 指南严格区分两类消费者指令：cooking instructions 用 kill step（烘焙/煮沸/微波烹调），heating instructions 不含 kill step（仅加热/表面处理如烤吐司）。非 RTE 食品靠消费者烹饪控制危害时，标签上的 adequate cooking instructions 本身就是控制措施——写错或缺失=控制失效。
  tags: [指南自定义, 标签]

- id: t86
  title: listeristatic formulation（抑制型配方）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B（定义与 IX 一致）
  source_quote: |
    "Listeristatic formulation: pH less than or equal to 4.4; water activity less than or equal
    to 0.92; and formulations (including those established in whole or in part through processes
    such as fermentation or culturing) containing a combination of factors scientifically
    demonstrated to be effective in preventing growth."
  summary: 三条路径并列的**抑制型**配方定义。只承诺"阻止生长"，不承诺"杀灭"；与法规 acid foods（平衡 pH≤4.6）**不是同一基准**——4.4 是李斯特菌专用的抑制目标。典型形态为发酵/培养型配方。与 t87 成对阅读。
  tags: [指南自定义, 配方控制, 核心概念, Lmono专有, 高频误读]

- id: t87
  title: listericidal control（致死型控制）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B；定义另见 X.A
  source_quote: |
    "Listericidal control: a control that will consistently destroy viable cells of
    *L. monocytogenes* and consistently leads to a finished food that contains less than 0.04
    colony forming units (CFU) of *L. monocytogenes* per gram (g) of food."
  summary: 定义用**成品可检出性**（<0.04 CFU/g，即 <1 CFU/25 g）而非 log 数表述——是"结果定义"而非"强度定义"，因此必须与所用方法的检出灵敏度绑定阅读。常见误读：把"5 log"当成 listericidal 的定义；实际 5/6 log 是**兜底路径**（按工艺前初始负荷 ≤/>100 CFU/g 切换），且只在无科学研究时使用。
  tags: [指南自定义, 致死工艺, 核心概念, Lmono专有, 高频误读]

- id: t88
  title: adequately reduce（充分减少）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Adequately reduce: capable of reducing the presence of *L. monocytogenes* to an extent
    sufficient to prevent illness."
  summary: 本指南对"减少到什么程度算够"的**结果导向**表述——标准是"足以预防发病"，不是"降了多少 log"。与法定 significantly minimize（t23，"降到可接受水平，包括消除"）不同：本条锚定**发病后果**（prevent illness），更适合判断某个 listericidal 工艺是否够格。三者分工见 t100。
  tags: [指南自定义, 核心概念, Lmono专有, 易混术语]

- id: t89
  title: zone（分区）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Zone means a designation about a surface or area reflecting how near that surface or area
    is to a ready-to-eat food and the risk the surface or area poses to ready-to-eat food if the
    surface or area is contaminated with *L. monocytogenes*."
  summary: 按"**离 RTE 食品有多近**"给表面/区域打的等级标签，是环境监测采样频次与纠正措施严格度的分配依据（四区示例见附录 Table 4）。与既有 t35 hygienic zoning（按生/熟/湿/干做物理分隔）是两回事：zone 是**风险分级标签**，不必然有物理隔离。
  tags: [指南自定义, 环境监测, 卫生分区, Lmono专有]

- id: t90
  title: non-food-contact surface (non-FCS)（非食品接触面）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Non-food-contact surface (non-FCS) any surface that, under normal operating procedures,
    does not contact food or the food-contact surfaces of equipment. Examples … equipment, vents,
    fixtures, drains, walls, floors, and employee clothing, shoes, and accessories."
  summary: 判定式定义——"在**正常操作程序下**不接触食品、也不接触设备的食品接触面"。两个易错点：①判定前提是"正常操作程序"，异常工况（溢流、泄漏、飞溅）可使非 FCS 变成实际接触面；②示例包含员工衣物鞋履与配件——所以它同时是人员控制与手套更换规则的挂钩点。
  tags: [指南自定义, 环境监测, 卫生, Lmono专有]

- id: t91
  title: hold and test procedures（暂扣待检程序）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B；用法见 XIII.F.3 与 XIV.B
  source_quote: |
    "Hold and test procedures: procedures establishing the criteria for releasing product after
    receiving the results of tests conducted to determine the presence of a pathogen on an FCS."
  summary: |-
    **先暂扣、后凭检测结果放行**的成文程序。关键点：它不是"检出才隔离"，而是**事先写好放行准则**（什么结果放行、什么结果处置），所以必须在产品流向市场之前就已存在——事后再补就失去意义。与管理组件里的"暂存待 PCQI 评估"不同：hold and test 的放行依据是**检测结果**。
  tags: [指南自定义, 环境监测, 记录, Lmono专有, 高频误读]

- id: t92
  title: environmental sample（环境样品）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Environmental sample: A sample that is collected from a surface or area of the plant for
    the purpose of testing the surface or area for the presence of microorganisms, usually
    environmental pathogens."
  summary: 从厂房**表面或区域**采集、用于检验该表面/区域上微生物（通常是环境病原）的样品。定义里"**区域**"这一项易被忽略——擦拭取样之外还有整块区域取样（如地漏、地沟），二者的前处理与判定不同。环境监测优于产品检测的理由：环境监测能定位污染源，产品检测只能给出历史基准。
  tags: [指南自定义, 环境监测, Lmono专有]

- id: t93
  title: control point (CP)（控制点）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Control point (CP): Any step at which biological, physical, or chemical factors can be
    controlled."
  summary: 可施加控制的步骤——**比 CCP 宽**。与 t11（CCP：控制对预防/消除危害 essential）与 t12（critical limit：安全红线）构成三级：步骤（CP）→ 关键点（CCP）→ 关键限值（CL）。常见误读：把"可控制"直接等同于"关键控制点"——CP 只说明该步骤在技术上可干预，不说明它对特定危害是关键。
  tags: [指南自定义, HACCP, 易混术语]

- id: t94
  title: severity（严重性）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Severity: The seriousness of the effects of a hazard."
  summary: 危害后果的严重程度——是危害分析严重性×概率双维评估的第一维。定义极简，故意不列举等级：FDA 在 Part 117 语境下把等级划分留给评估者与 PCQI，但要求**书面**。可与 t67（SAHCODH：一个可操作化的严重性门槛）配读。与另两种"够不够"判据的分工见 t100。
  tags: [指南自定义, 危害层级]

- id: t95
  title: Listeria species (Listeria spp.)（李斯特菌属）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Listeria species (Listeria spp.): microorganisms within the genus *Listeria*, including
    the species *L. monocytogenes*."
  summary: 属级概念——**包含** L. monocytogenes。用途边界：环境监测与部分成品筛查用 spp. 层级（覆盖面广、便于识别定殖），但成品检测应指向 L. mono 本身；成品检 spp. 阳性时须判定是否 L. mono，否则按 L. mono 污染处理。与 t100 及工艺控制卡的"两套检测方向"配读。
  tags: [指南自定义, 检测, Lmono专有, 高频误读]

- id: t96
  title: food safety system（食品安全体系）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Food Safety System: The result of the implementation of a food safety plan."
  summary: FSP（t08，文档）**落地运行后的结果**——文档与体系是两件事。与 t08 配读可避免"文件齐了=体系有效"的误读（供应链卡 B3 已点名这种"书面体系≠真实安全"的失败模式）。
  tags: [指南自定义, 核心概念, 高频误读]

- id: t97
  title: clean in place (CIP) / clean out of place (COP)（原位清洗 / 拆位清洗）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Clean in place (CIP): The removal of soil from product contact surfaces in their process
    position by circulating, spraying, or flowing chemical solutions and water rinses onto and
    over the surfaces to be cleaned." / "Clean out of place (COP): A system (e.g., cleaning
    tanks) used to clean equipment parts, piping, etc. after disassembly."
  summary: 两种清洗形态的官方定义——CIP 不拆设备就地清洗；COP 拆开后清洗。选型判据不在本术语里而在环境控制逻辑里：能拆的优先 COP（可触达缝隙），不能拆的走 CIP（须验证喷淋覆盖与残留）。共用 CIP 系统另有温度与监控参数要求（见环境病原卡 nA-07）。
  tags: [指南自定义, 卫生, 清洗, Lmono专有]

- id: t98
  title: certificate of analysis (COA) / certificate of conformance (COC)（L.mono 专项精确定义）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B；专项内容要求见 VIII.B.3
  source_quote: |
    "Certificate of Analysis: a document, provided for a food prior to or upon receipt of the
    food, that documents certain characteristics and attributes of the food." / "Certificate of
    Conformance: a supplier's guarantee stating that raw materials and ingredients conform to a
    product safety specification."
  summary: |-
    **与 t64 同源但更精确**，两者须配读：t64 给通用定义与"检测不能作唯一手段"的纪律，本条给 L.mono 专项字段——COA 强调"**接收前或接收时**提供"（接收环节的闸门文件），COC 强调"**供应商的保证**"（conform to a product safety specification），两者都不等于"第三方证明"。专项补充：COC 须含保证期 + 产品安全规格 + 符合本指南与 part 117 的声明，并至少每年取得 + 每年现场审核；COA 须含抽样方案、分析结果、方法及**检出限**。
  tags: [指南自定义, 供应链, 记录, Lmono专有, 高频误读]

- id: t99
  title: high efficiency particulate air (HEPA) filter（高效颗粒空气过滤器）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B；使用要求见厂房工程控制卡
  source_quote: |
    "High efficiency particulate air (HEPA) filter: an air filter that has an efficiency of
    99.97 percent to 99.99 percent when tested using the dioctylphthalate (DOP) test with a
    particle size of 0.3 microns. Such filters can remove all yeast, mold, bacteria and other
    particles that are larger than 0.3 microns."
  summary: HEPA 的**判定性规格**——DOP 法、0.3 µm、效率 99.97–99.99%。注意这是"≥0.3 µm 粒径"的去除承诺，对更小的粒径（如气溶胶化的更细颗粒）不作保证；这是"HEPA ≠ 零穿透"的正确读法。空气过滤选型（ASHRAE 终级 vs HEPA）见 `environmental-engineering-controls` 卡。
  tags: [指南自定义, 空气过滤, 术语澄清, 高频误读]

- id: t100
  title: severity vs. adequately reduce vs. significantly minimize（三种"够不够"判据不可混用）
  type: term
  source_chapter: 综合 L.mono 指南 XIX.B 与 21 CFR 117.3（t23）
  source_quote: |
    "Adequately reduce: capable of reducing the presence of *L. monocytogenes* to an extent
    sufficient to prevent illness." / "Significantly minimize: To eliminate or reduce to an
    acceptable level, including to eliminate."
  summary: 三种判据的分工——**severity**（t94，后果有多重，用于危害分析）、**significantly minimize**（t23，法定预防控制目标：降到可接受水平，含消除）、**adequately reduce**（t88，本指南的工艺充分性判据：足以预防发病）。混用的典型后果：把"降到可接受水平"读成"降 5 log"（一个数都不是），或把"足以预防发病"读成"可检出即合格"（忽略 0.04 CFU/g 的方法灵敏度前提）。
  tags: [指南自定义加法定定义, 易混术语, 核心概念, Lmono专有]
- id: t101
  title: Small Entity Compliance Guide (SECG)
  type: term
  source_chapter: SECG I. Introduction（2016-10, Docket FDA-2011-N-0920）
  source_quote: |
    "We have prepared this Small Entity Compliance Guide in accordance with section 212 of the
    Small Business Regulatory Enforcement Fairness Act (Pub. Law 104-121)." / "The rule is binding
    and has the full force and effect of law."
  summary: FDA 依 SBREFA § 212 为境内外食品设施编写的白话版规则说明，**不是法规、不是认证、不是内审清单**。常见误读：把它当成义务来源（其实它自己声明不创设法律责任）、把它当成 2016-11 发布（首页为 **October 2016**）、把 2018-05 那份只讲合规日期延长的同名近似件当成操作手册。正确用法是拿它逐条建 GAP，再把每条结论回指〔§ 117.xxx〕。SECG XIII 章逐条转述 Subpart B 八条，XIV 章对应 § 117.95。
  tags: [SECG, 效力层级, 合规指南, 高频误读, 2016-10]

- id: t102
  title: adequate（法定结果义务，非「差不多就行」）
  type: term
  source_chapter: 21 CFR 117.3 Definitions
  source_quote: |
    "Adequate means that which is needed to accomplish the intended purpose in keeping with
    good public health practice."
  summary: cGMP 通篇用 adequate / as necessary / suitable / appropriate 而不给数字，其法定含义是**「足以按良好公共卫生实践达成预期目的」**。这是结果义务，解释权不在企业：「法规没写数值」不是免责理由，检查员看现场状态与运行结果。与 t100 的 adequately reduce（李斯特菌工艺充分性判据）不是同一层级——后者是指南自定义，本条是 Part 117 法定定义。
  tags: [法定定义, cGMP, 结果义务, 21CFR117.3]

- id: t103
  title: current thinking / should（FDA 指南的标准免责措辞）
  type: term
  source_chapter: SECG I. Introduction
  source_quote: |
    "This guidance represents the Food and Drug Administration's (FDA or Agency) current thinking
    on this topic. It does not establish any rights for any person and does not bind FDA or the
    public." / "The use of the word should in FDA guidances means that something is suggested or
    recommended, but not required."
  summary: 「represent current thinking + does not bind FDA or the public + should 非必须」是 FDA 指南的标准免责三件套，与 cGMP 里的 **current**（Current Good Manufacturing Practice，指跟上当前可行技术的持续义务）是**两个不同的 current**，不可混淆。效力错位：同一句 recommend 对只受 Subpart B 约束的主体是真建议，对受 PCHF 约束的主体背后可能站着 Part 117 的 must，须先分流主体身份。
  tags: [效力层级, 指南免责, should-vs-must, 易混术语]

- id: t104
  title: alternative approach（指南允许的替代方案）
  type: term
  source_chapter: SECG I. Introduction
  source_quote: |
    "You can use an alternative approach if it satisfies the requirements of the applicable
    statutes and regulations."
  summary: FDA 指南允许的合法出口，但**举证责任在企业**：须证明替代做法同样满足法规的结果义务，而不是「指南没写所以我随便做」。与 § 117.136 的法定出口不是一回事——后者是「不实施预防控制」的条款级通道，本条是「满足同一法规要求的另一种做法」。
  tags: [效力层级, 合规出口, 举证责任, SECG]

- id: t105
  title: 80 FR 55907 vs. 80 FR 56145（同一份规则的两个页码）
  type: term
  source_chapter: SECG I. Introduction + 21 CFR Part 117 各条 source note
  source_quote: |
    "On September 17, 2015, FDA published the final rule ... (PCHF rule) (80 FR 55907)." /
    "[80 FR 56145, Sept. 17, 2015, as amended at 81 FR 3715, Jan. 22, 2016]"
  summary: 二者是 **2015-09-17 同一份 PCHF 最终规则**的两个起始页：55907 是 Federal Register 规则发布通知的首页（SECG I 章引用它），56145 是同一通知中 **Part 117 法规条文部分**的首页（CFR 各条末尾 source note 引用它）。见到两个数字不要判成两份规则，也不要互相「纠错」。SECG 首页同时写明该规则 **2015-11-16 生效**、合规日期分档（现已全部过期）。
  tags: [出处核对, 高频误读, 法规沿革, SECG]

- id: t106
  title: adulterated vs. prohibited act（cGMP 失守与 C–G 不合规是两条执法钩子）
  type: term
  source_chapter: 21 CFR 117.1(a)(1), (b)；FD&C Act § 402(a)(3)/(4)、§ 301(uu)
  source_quote: |
    "Adulterated within the meaning of: (i) Section 402(a)(3) ... the food has been manufactured
    under such conditions that it is unfit for food; or (ii) Section 402(a)(4) ... under insanitary
    conditions whereby it may have become contaminated with filth" / "is a prohibited act under
    section 301(uu) of the Federal Food, Drug, and Cosmetic Act."
  summary: |-
    **cGMP 失守 → 食品被认定为 adulterated**（〔§ 117.1(a)(1)〕引 FD&C Act § 402(a)(3)/(4)）；**不遵守 Subparts C–G → 设施运营本身构成 prohibited act**（〔§ 117.1(b)〕引 § 301(uu)）。两者后续都可接警告信、扣押、禁令、进口扣留，但法律定性不同，写不符合项或整改报告时不可混用。本包 regulatory-boundaries 卡称其为「执法钩子」。
  tags: [法定后果, 执法钩子, cGMP, 易混术语]

- id: t107
  title: 强制现场审核升级（supplier onsite audit escalation）
  type: term
  source_chapter: 21 CFR 117.430(b)(1)(2)；对照 SECG IX.A（未展开）
  source_quote: |
    "when a hazard in a raw material or other ingredient will be controlled by the supplier and is
    one for which there is a reasonable probability that exposure to the hazard will result in
    serious adverse health consequences or death to humans: (i) The appropriate supplier
    verification activity is an onsite audit of the supplier; and (ii) The audit must be conducted
    before using the raw material or other ingredient from the supplier and at least annually thereafter."
  summary: 供应商验证活动的四类（现场审核／抽样检测／审阅记录／其他适当活动）并非自由选择。**若该原料危害由供应商控制，且暴露后有可能导致严重健康后果或死亡**，〔§ 117.430(b)(1)〕规定当时唯一适当的验证活动是**现场审核**，且须在首次使用前完成、之后至少每年一次。唯一合法降级出口是〔§ 117.430(b)(2)〕的 **written determination**（书面判定其他活动或更低频审核能提供足够保证）。SECG IX.A 只并列四类活动、未提这条升级，据 SECG 应答「能不能只靠 COA」会答错。
  tags: [供应链, 供应商验证, 强制条款, SECG 简化, 高频误读]

- id: t108
  title: qualified facility 状态双向通知（status change notification）
  type: term
  source_chapter: 21 CFR 117.201(c)(2)(i)(C)、(c)(3)、(d)；SECG XI.D（只写单向）
  source_quote: |
    "(C) By July 31 of the applicable calendar year, when the status of a facility changes from
    'not a qualified facility' to 'qualified facility' based on the annual determination required by
    paragraph (c)(1) of this section." / "When the status of a facility changes from 'qualified
    facility' to 'not a qualified facility' ... the facility must notify FDA of that change in status
    using Form 3942a by July 31 of the applicable calendar year."
  summary: 状态变更是**双向义务**，且时限都在 7 月 31 日。① **由非变是**：当年 **7 月 31 日**前完成首次申报〔(c)(2)(i)(C)〕——SECG XI.D 未写这一方向。② **由是变非**：当年 **7 月 31 日**前用 Form 3942a 通知 FDA〔(c)(3)〕，并在当年 **12 月 31 日**前符合危害分析与预防控制要求〔(d)〕。此外每年 **7 月 1 日**前须完成并记录资格判定〔(c)(1)〕；2020 年起每两年一次，在 10-01 至 12-31 窗口内提交〔(c)(2)(ii)〕。判定门槛用 `exceeded`（超过），不是「至少一半」。
  tags: [qualified facility, 申报时限, 双向义务, SECG 简化]

- id: t109
  title: qualified facility 豁免撤销程序（withdrawal of exemption）
  type: term
  source_chapter: 21 CFR 117.251、117.254、117.257、117.260、117.264、117.267、117.270、117.277；SECG XI.E（止于 15 日答复）
  source_quote: |
    "FDA may withdraw a qualified facility exemption — In the event of an active investigation of a
    foodborne illness outbreak that is directly linked to the qualified facility; or If FDA determines
    that it is necessary to protect the public health ..." / "provide an opportunity ... to respond in
    writing, within 15 calendar days of the date of receipt of the notification"
  summary: 触发情形两项〔§ 117.251(a)〕：与该设施直接相关的食源性疾病暴发**在行调查**；或 FDA 为保护公众健康判定必要。程序完整链条：书面意向通知 + **15 个日历日**书面答复窗口〔§ 117.251(b)(2)〕→ 撤销令须经分区主任（境外为 CFSAN 合规办公室主任）或其上级**批准**〔§ 117.254(a)〕→ 令件须载明法定内容〔§ 117.257〕→ 收到令后可选择**遵守或上诉**〔§ 117.260〕，可申请**非正式听证**〔§ 117.267、§ 117.270〕，决定时限见〔§ 117.277〕。**SECG XI.E 只写到 15 日答复**，据其判断「没有后续救济」是错的。
  tags: [qualified facility, 撤销豁免, 行政程序, SECG 简化]

- id: t110
  title: subpart B 的五类不适用情形（§ 117.5(k)）
  type: term
  source_chapter: 21 CFR 117.5(k)(1)(2)；SECG VI. Table 4 脚注 2（一行带过）
  source_quote: |
    "(k)(1) Except as provided by paragraph (k)(2) of this section, subpart B of this part does not
    apply to any of the following: (i) 'Farms' (as defined in § 1.227 of this chapter); (ii) Fishing
    vessels that are not subject to the registration requirements ...; (iii) Establishments solely
    engaged in the holding and/or transportation of one or more raw agricultural commodities;
    (iv) Activities of 'farm mixed-type facilities' ... that fall within the definition of 'farm'; or
    (v) Establishments solely engaged in hulling, shelling, drying, packing, and/or holding nuts
    (without additional manufacturing/processing, such as roasting nuts)."
  summary: 这是**唯一能把 CGMP 本身也免掉**的条款，与只免 Subparts C/G 的豁免不同层级。五类：farm、不受注册要求的渔船、**仅从事初级农产品存放和/或运输的场所**、farm mixed-type 设施中属 farm 定义的活动、**仅做坚果去壳/脱壳/干燥/包装/存放而不烘烤**的场所。回拉条款〔(k)(2)〕：farm 或 farm mixed-type 设施若干燥/脱水 covered produce 以形成 distinct commodity，则 subpart B 适用于该干燥品的包装、打包与存放（可通过符合 part 112 相应要求达标）。判定顺序上这是 Step 1 的第②关，SECG 仅在 Table 4 脚注 2 提一句。
  tags: [适用性边界, subpart B, farm, SECG 简化, 高频误读]

- id: t111
  title: Ed.5 Table 1 树坚果封闭清单（2025-01）
  type: term
  source_chapter: FDA 食品过敏原问答 Ed.5 C.7 / C.8（2025-01 修订终版）
  source_quote: |
    "Only the tree nuts listed in Table 1 are considered major food allergens, and, therefore, must meet the food allergen labeling requirements of section 403(w) of the FD&C Act. Because other tree nuts that are not listed in Table 1 do not have a robust body of evidence to support inclusion as a major food allergen, they should not be included in the 'Contains' statement even if they are used as ingredients ... Tree nuts used as ingredients, but not listed in Table 1, would still be required to be listed by common or usual name in the ingredient list (21 CFR 101.4)."
  summary: Table 1 共 12 种（Almond / Black walnut / Brazil nut / California walnut / Cashew / Filbert-Hazelnut / Heartnut-Japanese walnut / Macadamia-Bush nut / Pecan / Pine nut-Pinon nut / Pistachio / Walnut-English,Persian），附学名与科名。仅表内者进 "Contains" 且须写具体名称，不得笼统写 "tree nuts"；未列表者仍按通用名进配料表（21 CFR 101.4）。**官方全文一次都没出现 coconut**——"椰子不再是主要食物过敏原"是行业推论，不是 FDA 原话。属 FD&C Act 标签口径，不是〔§ 117.xxx〕义务；危害分析中的物料控制不因此免控。
  tags: [过敏原标签, Ed.5, Table 1, 树坚果, 高频误读]

- id: t112
  title: Ed.5 对 milk / eggs 的物种扩展（2025-01）
  type: term
  source_chapter: FDA 食品过敏原问答 Ed.5 C.1 / C.2 / C.3 / C.4；FR 90 FR 1133
  source_quote: |
    "FDA considers 'milk' as milk from domesticated cows, goats, sheep, or other ruminants." / "FDA considers 'eggs' as eggs from domesticated chickens, ducks, geese, quail, and other fowl."
  summary: 历史口径是"奶＝家牛乳、蛋＝家鸡蛋"，Ed.5 扩展（FR 公告称 expanded our historical interpretation）。标注法：配料表按通用名（goat milk / duck egg），过敏原声明须带动物来源（whey (goat milk)、ovalbumin (duck egg)、Contains goat milk / Contains duck egg）。属 FD&C Act § 201(qq) 标签解释层，不改写 Part 117 预防控制义务。
  tags: [过敏原标签, Ed.5, milk, eggs, 物种扩展]

- id: t113
  title: allergen-free 声明与 advisory 声明互斥（Ed.5 D.13 / D.14）
  type: term
  source_chapter: FDA 食品过敏原问答 Ed.5 D.12 / D.13 / D.14（2025-01 修订终版）
  source_quote: |
    "In addition, a product with an allergen-free claim should not have an advisory statement that includes the same allergen. For example, a product that has a 'may contain milk' statement should not also bear a 'milk-free' claim." / "An allergen advisory statement ... is not a substitute for adherence to current good manufacturing practices or food allergen preventive controls"
  summary: D.13：free-from 声明无专门法规定义但须真实不误导；做 "milk-free" 即预期连交叉接触的非故意残留都不存在；且不得与同一过敏原的 advisory 声明同现。D.14：配料表或 "Contains" 已声明的，也不得再叠同一过敏原 advisory。D.12 与 PCHF 指南 Ch11 一致：advisory 不能替代 CGMP 与过敏原预防控制。**free-from 是控制承诺，不是纯标签措辞**，会反向抬高排产、清洁与验证要求。
  tags: [过敏原标签, Ed.5, free-from, may contain, 声明互斥]

- id: t114
  title: defect action level（食品缺陷行动水平）
  type: term
  source_chapter: 21 CFR 117.3 定义 + 117.110；FDA Food Defect Levels Handbook INTRODUCTION
  source_quote: |
    "Defect action level means a level of a non-hazardous, naturally occurring, unavoidable defect at which FDA may regard a food product 'adulterated' and subject to enforcement action under section 402(a)(3) of the Federal Food, Drug, and Cosmetic Act." / "It is incorrect to assume that because the FDA has an established defect action level for a food commodity, the food manufacturer need only stay just below that level. The defect levels do not represent an average of the defects that occur in any of the products--the averages are actually much lower."
  summary: 法定定义用的是 FDA「may regard ... adulterated」——这是**FDA 的执法裁量起点**，不是企业合规上限、不是平均值、不是内控目标。Handbook 是 FDA 汇编的一览表（执法裁量参考，非法规非 guidance 建议层），〔§ 117.110(b)〕明文指向它取实例。低于阈值仍可因 FD&C Act 402(a)(4) 不卫生条件与〔§ 117.110(a)〕持续义务被判不合规；数值绑定 AOAC/MPM 方法与取样量，且随技术进步由 Federal Register Notices 修订。与过敏原 Ed.5、微生物限值、污染物 action level 分属不同法源，不得混用。
  tags: [缺陷行动水平, 执法裁量, 402(a)(3), 高频误读]

- id: t115
  title: lowest level currently feasible（当前可行的最低水平）
  type: term
  source_chapter: 21 CFR 117.110(a)；Handbook INTRODUCTION
  source_quote: |
    "(a) The manufacturer, processor, packer, and holder of food must at all times utilize quality control operations that reduce natural or unavoidable defects to the lowest level currently feasible."
  summary: 〔§ 117.110(a)〕是 Subpart B 的 **must 级持续结果义务**，也是「低于 action level 就算合规」这一误读的正确答案。判据不是某个数字，而是「在当前技术可行条件下还能不能更低」，须以质量控制的实际运行与持续改进记录举证。配套〔§ 117.110(b)〕掺混稀释禁令（终产品检测值不影响掺假认定）、〔§ 117.80(b)(3)(4)〕原料与返工品前置要求。Handbook 那句 "Poor manufacturing practices may result in enforcement action without regard to the action level" 是旧 110.110(c) 意译，**现行 § 117.110 只有 (a)(b) 两款**，不得标成〔§ 117.110(c)〕。
  tags: [117.110, 法定义务, 持续义务, 掺混稀释, 高频误读]

- id: t116
  title: 21 CFR 110.110（现行仍有效、但正文本包未收；v4.7 纠错）
  type: term
  source_chapter: FDA Food Defect Levels Handbook INTRODUCTION；80 FR 56144 (2015-09-17)；FDA 2018-09-12 最终规则 FR Doc. 2018-19855（外部核实、本包未收）；21 CFR Part 114（4-1-25 Edition）§114.5；source-cfr-part114-2025.md 文件头；CAP-20 B2
  source_quote: |
    "Title 21, Code of Federal Regulations, Part 110.110 allows the Food and Drug Administration (FDA) to establish maximum levels of natural or unavoidable defects in foods for human use that present no health hazard."
  summary: ⚠ **v4.7 推翻 v4.3 的错误结论**：本条原写「Part 110 依 2015-09-17 PCHF 最终规则于 2018-09-17 移除、110.110 是过时引用」，**不成立**。该规则的 **amendatory instruction 13**（80 FR 56144）本拟 `remove and reserve part 110`，但 FDA **2018-09-12 最终规则（FR Doc. 2018-19855，同日生效）撤回该指令**（官方措辞 `amendatory instruction 13 in the third column on page 56144 is withdrawn`），理由是部分小/极小微企业 part 117 合规日期延至 2020-01-27，删除会造成 4–16 个月 CGMP 空档；FDA 称将在所有企业达到 part 117 CGMP 合规日后另案移除。**eCFR 现行版 Part 110 仍列 11 个 sections（含 §110.110）**，§114.5 并列 `parts 110 and 117` 也是现行文本。正确处理：手册引言的 `21 CFR 110.110` 指向**仍有效、但正文本包未收**的旧 CGMP 条款 → 标「转引未收」，**不得判为过时引用**；Part 117 侧法定义务仍回〔§ 117.110〕〔§ 117.3〕〔§ 117.80(b)(3)(4)〕，现代化 CGMP 在 Subpart B。手册 "Poor manufacturing practices may result in enforcement action without regard to the action level" 是 **§110.110(c)** 意译，**仍不得标成〔§ 117.110(c)〕**（§117.110 只有 (a)(b) 两款），但理由改为「那是 part 110 的 (c) 款」而非「part 110 已删」。⚠ 2018-19855 正文属外部核实、本包未收，引用须注明是 Federal Register 规则。
  tags: [版本陷阱, 110.110, 117.110, Part 110, 高频误读, v4.7 纠错, 转引未收]

- id: t117
  title: SIGNIFICANCE OF DEFECT（缺陷的消费者意义：美学 vs 潜在健康危害）
  type: term
  source_chapter: FDA Food Defect Levels Handbook GLOSSARY, SIGNIFICANCE OF DEFECT；COMMODITIES 表
  source_quote: |
    "Refers to the real or potential impact on the consumer due to the presence of a particular defect. A listed defect can have more than one significance to the consumer (e.g., the mold defect of whole cassia has an aesthetic significance, whereas the mold defect of green coffee beans has a potential health hazard significance due to the threat of mold toxins produced by the mold species known to infect coffee beans)."
  summary: 商品表每条 DEFECT SOURCE 行都带 SIGNIFICANCE，多为 `Aesthetic`；但 Allspice Whole、Capsicum Pods、Ground Paprika、Cocoa Beans、Coffee Beans Green、Figs、Ginger Whole、Nutmeg Whole 等明确标 `Potential health hazard - may contain mycotoxin producing fungi`。**同一缺陷在不同基质上意义不同**：读表必须三列一起读（DEFECT + Method / ACTION LEVEL / DEFECT SOURCE + SIGNIFICANCE）。遇 mold / rot / decomposed 且标潜在健康危害，须联动〔§ 117.80(b)(3)〕天然毒素前置合规与〔§ 117.130〕化学危害分析；反之也不要把 insect fragments / rodent hair 一律升格为食品安全危害。
  tags: [SIGNIFICANCE, aesthetic, mycotoxin, 化学危害联动, 高频误读]

- id: t118
  title: eNSpect 观察项 designation / 检查 categorization / 检查 classification 三层分级
  type: term
  source_chapter: FDA CPGM 7303.040 现行版 PART V.1 / Table 2（2025-CPM-HFP-001, p32-35）
  source_quote: |
    "Individual observations are designated as either major (significant) or minor (not significant) in eNSpect. In addition, under this compliance program, overall inspections are categorized as critical, major, or minor; investigators do not make this categorization."
  summary: 现行 7303.040 把分级拆成三层：① **单条观察项**在 eNSpect 只有 major (significant) / minor (not significant)；② **整次检查**才 categorized as critical / major / minor，且 **`investigators do not make this categorization`**；③ 检查**分类**是 OAI / VAI / NAI。critical 对应控制失效并造成 SAHCODHA 合理可能性，通常 OAI + 发 483 + 敦促停产与召回；major 对应显著公共卫生关注；minor 通常为 discussion items 且一般不上 483（重复出现可升级）。**2020 版把 critical/major/minor 挂在单条观察项上（`Critical Observations`），已废止**——凡旧 SOP、培训教材或律所快讯说「这条 observation 是 critical」须先判版本。Table 2 只是讨论起点，最终看 totality of findings 的公共卫生意义。
  tags: [迎检, CPGM 7303.040, 三层分级, OAI, VAI, NAI, 版本陷阱, 高频误读]

- id: t119
  title: Focused PCHF Inspections（PAC 03040U，2025 版改义）
  type: term
  source_chapter: FDA CPGM 7303.040 现行版首页 PAC 表 + PART III.1.A(6)（p28）；对照 2020 版 PART III.1.A(6)
  source_quote: |
    "Focused PCHF inspections allow divisions to utilize fewer resources during for-cause, compliance follow-up, certain converted limited scope PCHF inspections, or as directed by assignments, by covering only certain requirements in subparts C and G."
  summary: 2020 版 `03040U` 是 `PCHF FOLLOW-UP INSPECTIONS`（州码 `03S045` 同），现行 `2025-CPM-HFP-001` 改为 **`FOCUSED PCHF INSPECTIONS`**：只覆盖 subparts C、G 的**部分**要求，触发限于 for-cause / 合规跟进 / 由 limited scope 转换 / assignments 四类，可只查一类或几类预防控制，且目的与范围须写进 EIR summary 与 endorsement。现行版另新增 `03040A`（FD&C Act Inspections）与州码 `03S040A`。⚠ 不要把 focused 与 full scope、limited scope、follow-up 混称；8 个 FDA PAC（03040 / 03040A / 03040L / 03040F / 03040Q / 03040R / 03040T / 03040U）各有覆盖范围与州合同码。
  tags: [迎检, CPGM 7303.040, PAC, 03040U, Focused PCHF, 版本陷阱, 高频误读]

- id: t120
  title: official review 与迎检记录举证（§117.320 / §117.315(c) / §117.305 / §117.310）
  type: term
  source_chapter: 21 CFR 117.320、117.315(a)(1)(c)、117.305、117.310、117.190(a)；CPGM 7303.040 PART III.1.A(1)(a)
  source_quote: |
    "All records required by this part must be made promptly available to a duly authorized representative of the Secretary of Health and Human Services for official review and copying upon oral or written request." / "Except for the food safety plan, offsite storage of records is permitted if such records can be retrieved and provided onsite within 24 hours of request for official review. The food safety plan must remain onsite."
  summary: 迎检硬义务集中在 Subpart F：**口头或书面请求即须 promptly 提供并可供复制**〔§ 117.320〕；**FSP 必须在现场**，其他记录异地存放须 **24 小时内**取回现场（现场可访问的电子记录视为 onsite）〔§ 117.315(c)〕；记录至少留 **2 年**〔§ 117.315(a)(1)〕，设备/工艺充分性研究停用后再留 2 年〔§ 117.315(b)〕；记录须含实际观测值、与活动同步生成、准确清晰不可擦、含工厂标识/日期时间/执行人签名或缩写/产品与批号〔§ 117.305〕；FSP 由 owner/operator/agent in charge 在**初始完成与每次修改**时签字注日期〔§ 117.310〕；实施记录六类见〔§ 117.190(a)〕。检查员常索取 **3–5 名**关键人员的资质与培训记录（CPGM PART III.1.A(1)(a)）。「记录放总部、明天补送」不成立。
  tags: [迎检, official review, 117.320, 117.315, 记录保存, FSP 现场, 24 小时, 高频误读]

- id: t121
  title: FDA 483 回复 15 个工作日（CPGM 期望值，非法定时限）
  type: term
  source_chapter: FDA CPGM 7303.040 现行版 PART III.1（p24）；对照 Part 117 法定时限
  source_quote: |
    "FDA expects to receive a facility's FDA 483 response within 15 business days of the end date of the inspection." / "For foreign inspections, FDA 483 responses should be sent to FDA483responseinternational@fda.hhs.gov."
  summary: CPGM 写明 FDA 期望在**检查结束日起 15 个工作日**内收到 483 回复，境外回复发专门邮箱，且**回复会影响 FDA 是否决定跟进**。这是检查员作业指导里的期望值，**不是 Part 117 法定时限**，不得与〔§ 117.145〕7 个工作日记录审核、豁免撤销 15/90/120 日窗口混算，也不能说「逾期即违法」。回复骨架为事实澄清 → 根因分析 → CAPA（责任人 + 时限）→ 有效性验证 + 证据附件，证据直接映射到记录举证矩阵。检查期间能当场改掉的 minor 项会被记入 CAR 系统并验证（CPGM PART III.1 / PART V.1.C）。
  tags: [迎检, FDA 483, 15 business days, CPGM, 非法定时限, 高频误读]

- id: t122
  title: Limited Scope PCHF 的取证边界与转换条件
  type: term
  source_chapter: FDA CPGM 7303.040 现行版 PART III.1.A(2)（p25-27）
  source_quote: |
    "Field inspection staff should not review written food safety plans (including the facility's hazard analysis, preventive control programs, supply-chain programs, or recall plan), or review implementation records." / "Do not conduct a limited scope PCHF inspection when FDA environmental sampling is being conducted during the inspection."
  summary: Limited Scope（PAC `03040L`）覆盖 A、B、F 并对 subpart C 做**观察式** broad assessment（process / allergen / sanitation 三类控制），检查员只问有无 FSP 与危害分析，**不审阅**书面 FSP 与实施记录，**不在 subparts C/G 出书面观察项**，也不覆盖供应链程序。问题不影响食品安全时按〔§ 117.135(a)(1)〕作 discussion item；若构成显著公共卫生风险，须通知分部决定是否转 full scope 或 focused。⚠ **FDA 做环境取样时不得做 limited scope**，必须是 full scope 或 focused；仅凭 limited scope 证据一般不就 C/G 建议执法，须先转换。企业不应据此把 FSP 收起来——转换后全套记录立即成为取证对象。
  tags: [迎检, CPGM 7303.040, Limited Scope PCHF, 环境取样, 检查类型转换, 高频误读]

- id: t123
  title: CP 7303.050 的版本形态（2022 签发 / 2025-09-10 更正，非 2025 新 program）
  type: term
  source_chapter: FDA CP 7303.050 首页（p1）；文件名 20250915_...
  source_quote: |
    "Date of Issuance: 06/03/2022" / "IMPLEMENTATION DATE 06/03/2022" / "Correction date: 09/10/2025"
  summary: 用户提供的 62 页 508-Compliant PDF 首页为 **Date of Issuance 06/03/2022、IMPLEMENTATION DATE 06/03/2022、Correction date 09/10/2025**；PDF 元数据 creationDate 2025-09-10、作者 HFP/OCE。文件名里的 `20250915` 指**2022 版程序的 2025 年更正本**，不是 2025 年新签发的 program；与 CPGM 7303.040 的 `2025-CPM-HFP-001`（新 Transmittal、08/29/2025 签发）不是同一种版本形态，不得互相套用。⚠ 本 program `Inspections are not planned under this compliance program`——它是**抽样 program**，检查由 7303.040 等 interacting programs 承担，只在其中视情形采 for-cause 产品/环境样；「7303.050 检查」「7303.050 分级」都是错误说法。引用用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」。
  tags: [CP 7303.050, 版本陷阱, 抽样 program, 非检查 program, 高频误读]

- id: t124
  title: subs（份样）与 702(b) 部分（FDA 取证量，非企业放行标准）
  type: term
  source_chapter: FDA CP 7303.050 PART III.1.C / Sample Size；Table 2、Table 3；FD&C Act 702(b)；21 CFR 2.10(b)(3)
  source_quote: |
    "The sample size does not include 702(b) portions. See IOM Chapters 4 and 6 for additional information on 702(b) portion. Do not collect 702(b) sample portions for perishable products (see  21 CFR 2.10(b)(3)) or for samples collected in import status (unless otherwise requested)." / "In the absence of specific instruction, randomly collect ten (10), 2 lb. subsamples."
  summary: CP 7303.050 的样品量以 **subs（份样）** 计：Table 2 给 Salmonella（如叶菜 30 subs × 100 g、番茄 10 subs × 454 g、RTE 三明治 30 subs × 100 g、散装奶酪按重量分 10/2/1 subs），Table 3 给其他分析物（如 L. mono 10 subs × 200 g、EHEC/STEC 10 × 50 g、Cyclospora 5 × 50 g、甲肝/诺如 3 × 150 g）。三条硬规则：① **样品量不含 702(b) 部分**；② 多分析物按最大 subs 数取足且每 sub 同时满足各分析物用量；③ **易腐产品与进口状态样品不取 702(b) 部分**（21 CFR 2.10(b)(3)）。ATTACHMENT B 的污秽/霉变样在无专门指令时为随机 10 个 2 lb subs，奶酪制样取 6 个 227 g 且不得合并。⚠ 这些是 **FDA 检查员的取证量**，不是企业批放行抽样计划、不是内控规格；企业抽样须依自身危害分析与验证另定。702(b) 分割留样细则在 IOM Chapter 4，本包未收。
  tags: [CP 7303.050, 抽样量, 702(b), subs, 非放行标准, 高频误读]

- id: t125
  title: 环境拭子 50/100 与 Zone 分区（CP 7303.050 ATTACHMENT A）
  type: term
  source_chapter: FDA CP 7303.050 ATTACHMENT A Part III.C / Sample Size / Table 1 Sampling Framework
  source_quote: |
    "A minimum of 50 subsamples (ideally 100 subs) should be collected for _Listeria_ analysis and a minimum of 100 subs (ideally 300 subs) should be collected for _Salmonella_ analysis." / "Investigators may determine whether to swab for _Listeria_ or for _Salmonella_ based on the food being manufactured during the inspection and the environment in which the food is exposed."
  summary: 资格前提两项：① 生产**包装前暴露于环境**的 RTE 食品且无后续致死处理/无抑制型配方控制；② 检查期间**正在加工** RTE 食品。数量：**Listeria 最少 50 subs（理想 100）、Salmonella 最少 100 subs（理想 300）**；点位不足须在检查结束前联系 program monitor。Table 1 的 Collection Zones 为 Listeria 主要 zones 1-3、Salmonella 主要 zones 2-3（逐字原文见本条 source_quote 与卡片 R 段）；湿区偏 L. monocytogenes、偶发受潮的干区偏 Salmonella；历史环境阳性厂在原阳性 Zone 及邻近加密。⚠ 这是**检查员选点与取证量**，不是企业环境监测频次标准（后者见 L.mono 2017 Draft 建议层与 environmental-pathogen-sanitation 卡）。运输须 UPS Next Day Air Early A.M.、24 h 到室、周一至周四发运、周五不发、冷藏不冷冻；Salmonella 分析须在采集后 48 ± 2 h 内启动，超时样品无效。
  tags: [CP 7303.050, 环境取样, Zone 1, Zone 2, 50 subs, 100 subs, 湿干二分]

- id: t126
  title: WGS / GenomeTrakr 与环境拭子不计数
  type: term
  source_chapter: FDA CP 7303.050 PART IV.5.a、ATTACHMENT A Part IV.3.A / 3.C / Part IV.4
  source_quote: |
    "All positive samples for the following pathogens must send an isolate to WGS for analysis, unless otherwise specified or requested." / "WGS must be performed immediately on all confirmed _Listeria monocytogenes_ or _Salmonella_ positives and the results must be submitted to GenomeTrakr database, the national sub-typing network for foodborne disease surveillance." / "No enumeration will be performed on environmental swab/sponge samples."
  summary: 确认阳性的 **Salmonella / L. monocytogenes / E. coli O157:H7 或其他 STEC** 分离株一律做全基因组测序并上传 GenomeTrakr；环境拭子若分离出 L. mono 或 Salmonella（Zone 1/2/3），须联系 HFP/OCE 请求与**同厂历史分离株及 CDC 临床株**比对（非致病 Listeria spp. 不请求），可能翻出多年定殖史。产品 L. mono 阳性有剩余样品时按 eBAM Ch.10 计数（常规 composite、CORE/死亡相关按单个 sub），但**环境拭子不做计数**——拭子的判读维度是阳性点位与数量、WGS 关联和现场条件，不是菌数。实验室确认结果后 24 小时内先通报分部 Compliance Branch 再向企业发 FDA Form 1551；CRO（Cannot Rule Out）结果也须通报。⚠ WGS/GenomeTrakr 是 FDA 实验室动作，不是企业法定义务；企业侧对应义务是〔§ 117.170〕再分析触发与〔§ 117.190(a)〕实施记录。
  tags: [CP 7303.050, WGS, GenomeTrakr, 环境拭子, 不计数, 阳性升级]

- id: t127
  title: ATTACHMENT A Part V.1 三档 Findings 与 Direct Reference Authority
  type: term
  source_chapter: FDA CP 7303.050 ATTACHMENT A Part V.1 Findings / Part V.3.B Compliance Activities；PART V 表 7、表 8
  source_quote: |
    "Consideration for enforcement depends on several factors including the firm’s compliance history, the significance and severity of inspection observations, the prevalence and location of pathogens in the environment, the possible route of contamination, and the adequacy and timeliness of the firm’s corrective actions." / "HFP has not given Direct Reference Authority for any compliance actions related to violations resulting from environmental sampling results at this time." / "The table is not inclusive of all FDA enforcement strategies."
  summary: 环境取样结果的三档：① **无需行动**＝无显著条件且未检出环境病原；② **视厂方响应决定是否行动**＝显著 cGMP/卫生失控，或 Zones 2–3 阳性但无法建立到食品/食品接触面的直接污染路径（此档整改速度与证据权重最大，纠正须在检查结束前验证留证）；③ **预期采取监管行动**＝显著 cGMP/卫生失控、**Zone 1 阳性**、或 Zones 2/3 阳性且观察到直接交叉污染。执法判断逐案看合规史、观察项严重度、病原流行率与位置、污染路径、**整改充分性与及时性**。⚠ HFP **尚未**就环境取样结果授予 Direct Reference Authority，所有行政/法律行动须会签并与州伙伴讨论。PART V 表 7/8 列 voluntary corrective action、召回、warning letter、行政扣留、扣押、禁令、注册暂停、Import Alert / DWPE 等（domestic / foreign 分栏；指控 402(a)(1)/(3)/(4)、801(a)(3)），原文两次声明**非穷尽、逐案判断**，不是「检出 X 必定导致 Y」的对照表。
  tags: [CP 7303.050, Zone 1, 三档 Findings, Direct Reference Authority, 逐案判断, 非穷尽]

- id: t128
  title: IOM 483 措辞纪律与 Category 3 non-reportable observation（效力分层的制度性反证）
  type: term
  source_chapter: FDA IOM 2026 Chapter 5, §§ 5.5.10、5.5.10.7、5.5.11、5.5.11.3
  source_quote: |
    "However, do not quote regulations or incorporate standards (e.g.ISO 13485:2016) when reporting your observations." / "Do not cite deviations from policy or guidance documents on the FDA 483, FDA 483a, or FDA 4056." / "However, do not report opinions, conclusions, or characterize conditions as "violative." The determination of whether any condition is “violative” is an agency decision made after considering all circumstances, facts, and evidence." / "Observations, based on your judgement, that deviate from official published guidance, but do not deviate from regulations, and warrant discussion with management."
  summary: FDA 483 只写**事实性、显著**的观察项（clear / specific / significant / 不重复 / 按显著性排序），用 Who/What/When/Where/Why/How Much/How Often 写清并给总体比例（如 `Two out of 50 records examined`）、以 `So What?` 自验；**不引法规原文、不纳入标准、不引 policy/guidance 偏离、不写 opinions 或 violative**——是否违法是 FDA 事后综合全部事实证据的 agency decision。IOM 5.5.11.3 把 non-reportable observations 分三类，其中 **Category 3＝仅偏离官方 guidance 而未违反法规**，只能口头讨论并写入 EIR 的 `General Discussion with Management`，且 eNSpect 无对应 cite。这从检查员侧制度性印证本包分层：**Guidance / SECG / Handbook / CPGM / CP 7303.050 都不是可直接开观察项的法定义务**；⚠ 但不得反过来读成「指南可以不做」——同一事实若同时构成〔§ 117.xxx〕失守（如 adequate、〔§ 117.110(a)〕），仍会被写成事实性观察项。
  tags: [IOM 2026 Ch.5, FDA 483, 措辞纪律, non-reportable observation, 效力分层, 高频误读]

- id: t129
  title: FDA 检查表单地图（482 / 482c / 482d / 483 / 483a / 4056 / 484）
  type: term
  source_chapter: FDA IOM 2026 Chapter 5, §§ 5.1.4.2.1、5.5.1、5.5.10、5.5.12.5、5.8.1.3；Exhibit 5-1/5-5/5-10/5-17/5-18
  source_quote: |
    "After showing your credentials, issue the original, properly executed, and signed FDA 482, Notice of Inspection, to the most responsible individual at the firm." / "A Notice of Inspection is not required to be issued during foreign inspections (refer to 5.5.8); however, credentials should still be presented to the most responsible individual at the firm." / "You must issue a Form 484, Receipt for Samples, if you collect any physical sample during an inspection."
  summary: 发给 **owner / operator / agent-in-charge（OOAC）**，且 IOM 5.8.1.3 要求用 OOAC 与企业的**法定名称**（不得用 alias / DBA）：**FDA 482** Notice of Inspection＝国内到场、检查开始前（纸质签名或电子签名 PDF 须确认送达；团队检查所有成员签字）；**境外一般不发 482**（除非美国军方设施）但仍须出示证件；**482d**＝FSVP 记录索取；**482c**＝检查前索取记录（Exhibit 5-10）；**FDA 483**＝检查结束、离厂前的收尾会签发**已签署**版本（IOM 5.5.10.3 禁止展示未签署草稿）；**483a**＝FSVP Observations；**4056**＝Produce Farm Inspection Observations；**FDA 484** Receipt for Samples＝采集**任何实体样品**时必发，一般在检查结束时签发（提前签发视为结束检查，须另发 482 才能继续）。另：证件可查看并记录姓名/号码但**不得复印、不得按指纹**（18 U.S.C. 701）。
  tags: [IOM 2026 Ch.5, FDA 482, FDA 483, FDA 484, OOAC, 表单地图, 境外检查]

- id: t130
  title: IOM 5.2.7 预告三层口径（食品企业一般不预告、境外通常提前告知、预告不是预约）
  type: term
  source_chapter: FDA IOM 2026 Chapter 5, §§ 5.2.7、5.2.7.1、5.2.7.2；§§ 5.1.4.2.1、5.5.8
  source_quote: |
    "Pre-announcements are mandatory for all medical device surveillance inspections—and some Bioresearch Monitoring (BIMO) inspections—in accordance with the criteria and instructions below. Routine produce farm inspections should be pre-announced, unless otherwise directed." / "In general, though, it may be inappropriate to pre-announce inspections of food establishments, blood banks, source plasma establishments, and some BIMO inspections, but this is subject to program division discretion." / "In general, the Agency usually announces foreign inspections in advance, partly due to logistics such as arranging travel and access to facilities, securing visas, and partly because of the high costs of conducting foreign inspections." / "The pre-announcement of domestic inspections should generally be no less than five calendar days in advance of the inspection." / "ORA's primary purpose for pre-announcing is to ensure that the appropriate records and personnel will be available so that we may execute an effective inspection. It is _not_ to make an appointment for the inspection."
  summary: 三层必须一起读：① 医疗器械 surveillance 与部分 BIMO **强制预告**，常规 produce farm 检查应预告；② **食品企业检查** `may be inappropriate to pre-announce`，由 program division 裁量；③ **境外检查通常提前告知**（签证、差旅、成本）。国内预告一般**不少于 5 个日历日**，改期由 investigator/team 决定且新日期不得晚于原日期 +5 天，企业要求时可早于 5 天；预告目的是确保**人员与记录在场**，不是预约，不得称 `appointment to inspect`；届时人员/记录不到位会被记入 EIR。⚠ 此前 inspection-readiness 卡把「2025 扩大境外无预告检查」记为政策层、原文未收——补入 IOM 后须区分：**「通常提前告知」是常态，「无预告」是政策变化**，两者不是同一件事；不得写成「FDA 从不预告」或「境外一律无预告」。
  tags: [IOM 2026 Ch.5, Pre-Announcement, 5 个日历日, 境外检查, 无预告检查, 高频误读]

- id: t131
  title: 拒绝检查的边界（301(e)/(f)、非法定信息与 FD&C Act 807(b)）
  type: term
  source_chapter: FDA IOM 2026 Chapter 5, §§ 5.5.2、5.5.2.1、5.5.2.3、5.5.3；FD&C Act 301(e)/(f)、704、807(b) [21 U.S.C. 384c(b)]
  source_quote: |
    "A refusal of inspection is refusal to permit entry or other action that prohibits you from obtaining records and information to which the FDA is entitled under the law." / "It is not an inspection "refusal" when management refuses to provide information (for example, formulations, lists of shipments and manufacturing codes, etc.) not specifically required by law or regulation." / "For international food inspections, section 807(b) of the FD&C Act (21 U.S.C. 384c(b)), authorizes the FDA to refuse admission of a food ..."
  summary: 拒绝**入场**援引 `301(f)` + `704`；拒绝提供或复制**依法有权取得**的记录援引 `301(e)`；检查员须能证明检查在 reasonable time / manner / limits 内进行、已出示证件并（国内）签发 482（CPG Sec. 130.100 口径，正文未收）。⚠ **拒绝提供法规未强制要求的信息**（IOM 明确举例配方、发货清单、生产编码）**不构成 inspection refusal**；企业可依 IOM 5.1.5 提出商业秘密保护诉求。但〔§ 117.320〕要求法定记录口头/书面请求即 promptly 提供并可供复制、〔§ 117.315(c)〕FSP 必须在现场，不能拿「保密」一刀切拒绝。**境外食品检查**拒绝的后果更重：FD&C Act **807(b)** 授权 FDA 对该外国工厂的食品拒绝入境，并可能 Import Alert、注销食品设施注册；IOM 5.5.2.1 要求以 Operation 15 – Foreign Investigation 备忘录上报，不得记为 Washout。⚠ 药品/器械的 `501(j)`「拒绝即掺假」规则**不得套到食品**。
  tags: [IOM 2026 Ch.5, 拒绝检查, 301(e), 301(f), 807(b), 商业秘密, 境外检查]

- id: t132
  title: 样品合格不阻碍 cGMP 指控，以及记录/电子记录/照片的证据固定
  type: term
  source_chapter: FDA IOM 2026 Chapter 5, §§ 5.6.4、5.6.5.1、5.6.6.1、5.6.7；§§ 5.5.12.1、5.5.12.3
  source_quote: |
    "Lack of a violative physical sample is not a bar to pursuing regulatory and/or administrative action providing the cGMP deficiencies have been well documented. Likewise, physical samples found in compliance are not a bar to pursuing action under cGMP charges." / "Do not remove the firm's only copy of records. If duplicates are not available, whenever possible, scan, photograph, or photocopy." / "Of note: Do not personally access a firm’s system to review electronic records, databases, or source data during the course of an inspection" / "Photos taken during inspections are not investigational samples. They are exhibits. Only use FDA-issued equipment, such as a government-issued camera, to take photographs"
  summary: ① **没有阳性实体样**不阻碍依充分记录的 cGMP 缺陷采取监管/行政行动，**样品合格也不阻碍 cGMP 指控**——cGMP 是〔§ 117.3〕`adequate` 的观察型结果义务，与检测结果无关。② 记录作 exhibit：**不得取走企业唯一副本**，应扫描/拍照/复印并核对可读性、保全证据链、不得通过外部邮件接收 exhibit（远程 FSVP 例外）。③ 电子记录：**检查员不得亲自登录企业系统**，应由企业人员操作、检查员旁视提问（仅 BIMO 5.14.2.1 与生物制品 5.13.2.5.1 例外）。④ 检查照片是 **exhibit 不是样品**，只能用 FDA 配发设备（个人设备可能被保全并进入 discovery）。⑤ 检查员至少**每日一次**与管理层沟通可能形成 483 的发现（5.5.12.1），且不得提供咨询建议；**15 个工作日**内的充分 483 回复 `may impact FDA's determination of the need for subsequent action`（5.5.12.3）——与 CPGM 7303.040 PART III.1 双出处，均非法定时限。
  tags: [IOM 2026 Ch.5, 证据链, 样品合格, cGMP 指控, 电子记录, FDA 484, 15 business days]

- id: t133
  title: 九类不可混引与 IOM 收录范围（v4.5 引用纪律）
  type: term
  source_chapter: 全包引用规范；source-cp-7303-050-2025.md / source-iom-ch5-2026.md 文件头
  source_quote: |
    "Do not cite deviations from policy or guidance documents on the FDA 483, FDA 483a, or FDA 4056." —— IOM 5.5.10.7
  summary: v4.5 起全包**九类来源不可混引**：① 21 CFR Part 117 法规正文〔§ 117.xxx〕；② FDA PCHF 行业指南（Ch/小节号）；③ L.mono RTE 指南（其章节号，Draft 建议层）；④ SECG（SECG 章号）；⑤ 过敏原 Ed.5（问答编号如 C.8 / D.13，FD&C Act 标签解释）；⑥ Food Defect Levels Handbook（「Handbook 章名 + 产品名」，执法裁量参考）；⑦ CPGM 7303.040（「CPGM 7303.040 PART x」，附件带 ATTACHMENT A 前缀）；⑧ **CP 7303.050（「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」，其 ATTACHMENT A Part V 与主文 PART V 同名不同口径）**；⑨ **IOM 2026（「IOM 5.x.x / IOM Exhibit 5-x」，Exhibit 编号与小节号不同层，勿把 Exhibit 5-5 写成 IOM 5.5.5）**。⚠ 本包**只收 IOM 2026 Chapter 5 单章**；IOM Ch.3（3.2 权限）、Ch.4（Sampling / 702(b) / 4.3.6.6 / 4.6 / 4.7）、Ch.6（Imports / 6.4 / 6.8.1.4）、Ch.7、Ch.8、Ch.9、Ch.10，以及 RPM、CPG 全套、Import Alerts、eBAM/AOAC/MPM 方法正文、SOP-001052、FMD-147 均未收；遇 IOM 正文的跨章引用只标「转引未收」，不得代填。
  tags: [引用规范, 九类不可混引, IOM 2026 Ch.5, CP 7303.050, 收录边界, v4.5]

- id: t134
  title: PAC / PAF 与抽样报告系统（FACTS / SERIO / OASIS / CMS）
  type: term
  source_chapter: FDA CP 7303.050 首页 PRODUCT/ASSIGNMENT CODES、PART III.2 Table 4、PART IV.6 Table 6、ATTACHMENT A Part III Table 2
  source_quote: |
    "Report domestic sample collections and all analytical results into the Field Accomplishment and Compliance Tracking System (FACTS). Import sample collections should be reported in the System for Entry Review and Imports Operations (SERIO) and/or the Operational & Administrative System for Import Support (OASIS), as appropriate."
  summary: CP 7303.050 首页列 **FDA PAC**：`03037D` 国内/进口奶酪及奶酪制品微生物样、`03803D` 国内人类食品微生物样、`03819C` 进口人类食品微生物样、`03050B` 国内/进口人类食品污秽样、`03050E` 国内/进口人类食品设施 exhibit 样、`03050N` 国内人类食品环境样；**州合同码** `03S050N`。PART III.2 Table 4 给采集报样的 PAC/PAF 组合（MIC / PAR / VIR / CCD / FDF / FIL / NAR），PART IV.6 Table 6 给分析结果报样的组合（`*NAR` 仅用于 FACTS 未预设的特殊微生物检测）；ATTACHMENT A Table 2 给环境采样工时 PAC。**国内**样品与全部分析结果报 FACTS，**进口**报 SERIO / OASIS，执法建议经 CMS 提交 HFP/OCE 并关联样品；进口另按 IOM Ch.6 6.4 与 RPM Ch.9 的 Import Alerts / Import Bulletins 处理（正文未收），与被抽行 same or similar 的 entry lines 须转 compliance branch 待结果，一般不再抽已在 DWPE 清单上的产品（除非另有分析物关切）。⚠ PAC/PAF 是 FDA 内部作业码，不是企业要填的合规编号，也不是检查类型码（后者见 CPGM 7303.040 的 03040 系列）。
  tags: [CP 7303.050, PAC, PAF, FACTS, SERIO, OASIS, CMS, 进口抽样, 内部作业码]


- id: t135
  title: CP 7303.070 的版本形态（2024 签发 / 2025-09-26 更正，文件名 20250929 只是生成日）
  type: term
  source_chapter: FDA CP 7303.070 首页（p1）；PDF 元数据 title / creationDate
  source_quote: |
    "Date of Issuance: 09/26/2024" / "IMPLEMENTATION DATE: 9/26/2024" / "Correction Date: 9/26/2025"
  summary: 用户提供的 61 页 508-Compliant PDF 首页为 **Date of Issuance 09/26/2024、IMPLEMENTATION DATE 9/26/2024、Correction Date 9/26/2025**；PDF title 亦写 `(Implementation Date 09/26/2024)`，creationDate 2025-09-29。文件名 `20250929` 是 **PDF 生成日，不是签发日**；本件是 **2024 版程序的 2025 更正本**，与 CP 7303.050（2022 签发 / 2025-09-10 更正）同属更正本形态，不同于 CPGM 7303.040 的 `2025-CPM-HFP-001`（新 Transmittal、08/29/2025 签发）。引用写「CP 7303.070（2024 签发 / 2025-09-26 更正）」，不要写成「2025 版 7303.070」。首页 PAC `03070A/B/C`（境内 AF / LACF / 无菌 LACF）、`03070F/G/J`（进口）、`71070`（动物食品）；PAF `ACD`（常规）、`MIC`（仅 C. botulinum for-cause）；Problem Codes `AFD / ACF / LAF`。
  tags: [CP 7303.070, 版本陷阱, 更正本, PAC, PAF, 十五类不可混引]

- id: t136
  title: §117.5(d)(1)(2) 的 LACF 管辖分流与 AF 不豁免（CP 7303.070 官方细化）
  type: term
  source_chapter: CP 7303.070 PART II.2.C(1)；21 CFR 117.5(d)(1)(2)、117.1(c)
  source_quote: |
    "LACF products are subject to the CGMP and PCHF rule (21 CFR part 117). However, subparts C and G do not apply to activities covered by 21 CFR part 113" / "The exemption in paragraph (d)(1) of this section is applicable only with respect to the microbiological hazards that are regulated under part 113 of this chapter." / "Acidified foods are subject to the CGMP & PCHF rule."
  summary: 本包最容易被误用的一处。**①** LACF 受 Part 117 约束，〔§ 117.5(d)(1)〕只免 **part 113 覆盖活动**的 Subparts C/G；**②**〔§ 117.5(d)(2)〕再限定该豁免**仅限 part 113 管辖的微生物危害**；CP 逐字给出残余危害：`Staphylococcus aureus` 生长与产毒、化学危害、物理危害仍归 Subparts C/G。**③**〔§ 117.1(c)〕明定受专项 CGMP 法规管辖的食品同时受 Part 117 约束，Subpart B/F 不因该豁免消失。**④** **酸化食品不在 § 117.5(d) 内**：`Acidified foods are subject to the CGMP & PCHF rule`，其 PCHF 覆盖转 CP 7303.040，检查重点仍在 21 CFR part 108/114（不论规模）。**⑤** ⚠〔§ 117.201〕是 **qualified facility 的 modified requirements**（attestation、双份保证书、7 月 31 日），**不是 LACF 条款，不得误引**。CP 原文标「CP 7303.070 PART II.2.C(1)」，法规标〔§ 117.5(d)(1)(2)〕，两者不可混引。
  tags: [管辖分流, 117.5(d), 117.1(c), 117.201, 酸化食品, 双法规并集, 高频误读]

- id: t137
  title: 法源三角 21 CFR part 108 / 113 / 114（CP 7303.070 转引未收）
  type: term
  source_chapter: CP 7303.070 PART I、PART II.1 Objectives、PART VII.2；21 CFR 117.1(c)
  source_quote: |
    "In addition, 21 CFR part 108 “Emergency Permit Control” requires manufacturers of AF or LACF to register their processing plants, file their scheduled processes with FDA and to adhere to the mandatory requirements expressed in the GMPs."
  summary: CP 7303.070 据以判定合规的法源是 **part 108（Emergency Permit Control：FCE 加工厂注册、SID 定时工艺备案）、part 113（密封容器热加工低酸食品）、part 114（酸化食品）**，三套正文**本包均未收**。CP 内出现的 FCE、SID、SUP-SID、filed scheduled process、Process Authority、商业无菌、Emergency Permit、BPCS（Better Process Control School）、Form 2541e 等都属**转引**，只能标「转引未收」，**不得从 CP 反推法条**，也不得把 CP 的检查动作（观察运行中 retort、审核温度分布/热穿透、卷边完整性、冷却水消毒残留、异常罐处置、投诉档案）写成 Part 117 的企业义务。PART VII.2 把 LACF Registration and Process Files 归 HFP；FURLS 的 AF/LACF 注册备案系统可判 LACF / AF / aseptic / aw-controlled 及容器尺寸、加工方式、关键因子。完整判定见 CAP-19 `lacf-inspection-program`。
  tags: [21 CFR part 108, 21 CFR part 113, 21 CFR part 114, FCE, SID, Process Authority, 转引未收]

- id: t138
  title: 酸化食品判定三步与 Maximum Equilibrium pH
  type: term
  source_chapter: CP 7303.070 PART III.1.A Acidified Food Determination（STEP 1–3）
  source_quote: |
    "This value is called the “Maximum Equilibrium pH”." / "Submit the information to HFP-OCE-OE-LACF-AND-ACIDIFIEDFOODS@fda.hhs.gov for review to determine if there is a significant difference between the pH of the finished product and the predominant acid(s) or acid food(s)."
  summary: 检查员遇「疑似酸化食品」时收集配方与包装信息交 HFP 判定。**STEP 1**：合并全部 pH ≤4.6 的酸成分 + 全部配方用水，测该混合物 pH；**STEP 2**：加入全部 pH >4.6 的低酸成分，固体研磨/匀浆成与成品同比例的平滑混合物，测得值称 **"Maximum Equilibrium pH"**；**STEP 3**：送 HFP 官方邮箱由 HFP 判断成品 pH 与主导酸/酸性食品之间是否存在 significant difference。所有配料须与成品同品种同比例。包装判 ROP 的阈值是最终包装氧透过率 `< 10,000 cc/m²/24 hours at 24°C`（源文 `10,000 cc/ m[2] /24 hours at 24ºC` 为 PDF 上标转录）。企业自判产品身份时成品**至少测 6 个单元**；⚠ **最终法定身份由 HFP 判定，本包不得替企业下结论**。注意平衡 pH 4.6 的法定定义与持续维持义务在〔§ 117.3〕〔§ 117.80(c)(14)〕，不是 CP 创设。
  tags: [酸化食品判定, Maximum Equilibrium pH, ROP, 平衡 pH, HFP 判定, CP 7303.070]

- id: t139
  title: 三套 pH / aw 数字（法定边界 / 检查员触发线 / L.mono 建议层）
  type: term
  source_chapter: 〔§ 117.3〕〔§ 117.80(c)(14)(15)〕；CP 7303.070 PART IV.2；L.mono 指南 IX
  source_quote: |
    "If one or more containers have pH values equal to or greater than 4.40, or if the mean pH plus 2 standard deviations is equal to or greater than 4.40, a second analyst must promptly (same day) re-determine the pH values" / "Never average the two analysts' results together."
  summary: 三套数字互不替代。**第一套（法定）**：pH **4.6**（平衡 pH，〔§ 117.3〕定义、〔§ 117.80(c)(14)〕须监测并维持）、aw **0.85**（LACF 管辖/安全水分，〔§ 117.80(c)(15)〕须加工至并维持安全水分水平）。**第二套（CP 7303.070 检查员/实验室作业）**：pH **4.40** 触发第二分析师同日换 pH 计复测、**4.65** 触发两分析师各测余下半数、**4.75**（异常罐 + 活的嗜温革兰阳性厌氧芽孢菌）触发 botulinum neurotoxin 与 `C. botulinum` PCR；aw **0.90 / 0.93** 触发换仪器在同 3 罐复测；`Never average the two analysts' results together`——original analysis 与 check analysis 分别判定。**第三套（L.mono 草案建议层）**：pH ≤**4.4**、aw ≤**0.92** 是 listeristatic 配方设计基准。⚠ 三者用途不同、不得互替：pH 4.5 勉强满足酸化管辖、会触发 CP 复测、却不满足 L.mono 抑制目标；4.40/4.65/1%/24 罐也不是企业放行标准。
  tags: [pH 4.6, pH 4.40, pH 4.65, pH 4.75, aw 0.85, aw 0.90, aw 0.92, 三套数字, 高频误读]

- id: t140
  title: 异常罐 1%、795 g / 24 罐与 14 天 progressive decomp（FDA 取证口径）
  type: term
  source_chapter: CP 7303.070 PART III.1.A Inspectional Considerations、PART III.1.B、PART IV.2、PART V.1
  source_quote: |
    "Visual observation of warehoused product that shows a significant number of abnormal containers (greater than 1%) where the firm has not conducted a spoilage diagnosis" / "The total sample size for containers 795 grams (i.e., 28 oz.) net weight or smaller is 24 containers.  The total sample size for all others is 12 containers."
  summary: 检查员取证口径。**异常容器 >1% 且企业未做 spoilage diagnosis**（判定腐败原因与批次能否放行）是检查员侧的显著观察项；PART V.1 把「异常容器 ≥1% 批确认掺假或进行性腐败」列为通知 Center 的触发之一；进口侧异常率 1% 以上须另提 DTR。pH 分析取样：**≤795 g（28 oz）取 24 罐，其余 12 罐**；具体抽样计划出处是 **IOM Chapter 4, Sample Schedule Chart 2（正文未收）**。实验室对正常容器做 **14 天 progressive decomp** 培养，异常罐另做气体/气味/外观、净重与沥干重、漏罐测试、卷边解剖与内壁状态检查；`C. botulinum` 分析**仅 for-cause**（PAF `MIC`），涉病走 BAM Ch.17、不涉病走 BAM Ch.21A，典型分离株做 WGS 送 HFP/OLOAS 做毒素基因评价。⚠ 这些都是 FDA 取证与执法建议口径，不是企业内控抽样或放行标准。
  tags: [异常罐, 1%, 795 克, 24 罐, progressive decomp, BAM, 非放行标准]

- id: t141
  title: Import Alert 99-37 / 99-38 与「未备案不自动 DWPE」陷阱
  type: term
  source_chapter: CP 7303.070 PART III.2 Import Entry Review、PART V.2 (f)
  source_quote: |
    "Do not recommend firm/products for an Import Alert/DWPE solely based on firm/product not registered and/or filed processes with FDA since all LACF and acidified foods should be checked for registration and  process filing."
  summary: 两个 Import Alert 与一条反直觉限制。**#99-37** 针对「被判为 LACF/AF 且无 filed scheduled process」的 **DWPE（Detention Without Physical Examination）**；**#99-38** 针对「已提交 scheduled process 但过程控制不足」。⚠ 反直觉陷阱：CP 原文明确**不得仅因企业/产品未注册或未备案就建议列入 Import Alert/DWPE**——所有 LACF/AF 产品都须先查验注册与备案，且 #99-37 的适用以 `when FDA determines such action is necessary for efficient and effective protection of the public health` 为前提（例如检查显示潜在公共卫生风险、屡次规避备案）。进口审核：FDA import systems 用 AofC 交叉核验 **FCE 与 SID** 与 LACF/AF 数据库，系统查询失败须人工核验（Center Views 的 HFP tab）；地址无法核实或不符 → **DTR（detention recommendation）**；SID 与容器尺寸、品名、备案状态不符 → 现场查验或 DTR。加入 Red List 的建议经 CMS 报 DIO，非 direct reference 范围须附 Center concurrence。⚠ Import Alert 全文、CPG Sec. 520.200/520.300、RPM Ch.9 本包未收。
  tags: [Import Alert 99-37, Import Alert 99-38, DWPE, FCE, SID, DTR, 反直觉陷阱]

- id: t142
  title: RRA 程序性定义、Keep Refrigerated / brites 路由与十四类不可混引（v4.7 定稿 / v4.9 口径）
  type: term
  source_chapter: CP 7303.070 PART II.2.B(2)、PART II.2.C(1)(2)；FD&C Act 704(a)(1)
  source_quote: |
    "RRAs are not considered inspections, conducted pursuant to section 704(a)(1) of the FD&C Act" / "Products labeled “Keep Refrigerated” are exempt from 21 CFR 113/114. These products should be covered under Compliance Program 7303.050."
  summary: 程序定义与两条路由。**RRA（Remote Regulatory Assessment）**：FDA 可对 AF/LACF 企业开展**自愿、全程远程**的记录/设施评估；CP 明确 `RRAs are not considered inspections`，不满足 FD&C Act 704 条要求现场 inspection 的法定场景（如 510(h)、503B(b)）。这是 **CP 内的程序性定义**，可据此回答「RRA 算不算检查」，但 **FDA 扩大 RRA 适用范围 / 境外无预告检查的政策公告原文仍未收**，不得据此推导政策，也不能替换 IOM 5.2.7 的预告三层口径。**两条路由**：`Keep Refrigerated` 产品免 21 CFR 113/114 → 归 **CP 7303.050（CAP-17）**；未贴标 AF/LACF「brites」运至中央仓贴标装箱的检查报 **`PAC 03040`（CAP-16）**。另：动物食品 LACF 用 `71070` 并联动 7371.000 / 21 CFR 507.5(b)；海产品 LACF 并做 7303.842 HACCP。**收录边界（v4.7 更新）**：第十来源 CP 7303.070 已收（CAP-19）；**第十一、十二来源 21 CFR Part 113 / 114 法规正文亦已收（CAP-20）**，全包口径为 v4.6 十类 → v4.7 十二类 → v4.8 十三类 → **v4.9 十四类不可混引**。仍未收：21 CFR part 108（FCE/SID/Emergency Permit）、**part 110（旧 CGMP，至今有效但正文未收）**、part 120（**part 123 自 v4.9 起已收，见 CAP-22**）、IOM Ch.4 Chart 2、BAM、CPG、Import Alert 全文、其余 Compliance Programs，一律标「转引未收」。
  tags: [RRA, Keep Refrigerated, brites, 7303.050, 7303.040, 十四类不可混引, 收录边界, v4.6, v4.7]

- id: t143
  title: 〔§ 117.1(c)〕专项 CGMP 法规与 Part 117 并行适用（不是二选一）
  type: term
  source_chapter: 21 CFR Part 117 §117.1(c)；21 CFR Part 113 / 114（4-1-25 Edition）文件头
  source_quote: |
    "Food covered by specific current good manufacturing practice regulations also is subject to the requirements of those regulations."
  summary: 受专项 CGMP 法规（part 113 / 114 等）管辖的食品**同时**受 Part 117 约束，所以「做 LACF 就不归 Part 117 管」「做了 PCHF 就不用管 part 113」都错。v4.7 起本包有三套独立编号的法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕（**v4.9 增为四套：加〔§ 123.xxx〕，见 CAP-22**），彼此并行、不是上下位、不是新旧替代；`regulatory-boundaries` 里「Part 117 是唯一判定基准」只能理解为**判定 Part 117 义务**的唯一基准。CP 7303.070 的检查动作仍属检查员作业指导（CAP-19），企业义务清单见 CAP-20。
  tags: [117.1(c), 并行适用, 四套法规正文, LACF, 酸化食品, v4.7]

- id: t144
  title: 〔§ 117.5(d)(1)(2)〕条件性、有限豁免（双条件 + 仅限微生物危害）
  type: term
  source_chapter: 21 CFR Part 117 §117.5(d)(1)(2)；CP 7303.070 PART II.2.C(1)
  source_quote: |
    "Subparts C and G of this part do not apply with respect to activities that are subject to part 113 of this chapter (Thermally Processed Low-Acid Foods Packaged in Hermetically Sealed Containers) at a facility if you are required to comply with, and are in compliance with, part 113 of this chapter with respect to such activities."
    "The exemption in paragraph (d)(1) of this section is applicable only with respect to the microbiological hazards that are regulated under part 113 of this chapter."
  summary: Subparts C/G 对 part 113 覆盖活动不适用，**但必须同时满足** `required to comply with` **且** `in compliance with` part 113，企业 part 113 不合规时豁免根本不成立。即便成立，〔§ 117.5(d)(2)〕也把豁免限定在 part 113 管辖的**微生物危害**——未被热处理控制且需预防控制的危害（S. aureus 生长产毒、化学、物理、过敏原）仍归 Subparts C/G。⚠ **part 114 完全不在 §117.5 豁免清单内**（清单是 part 123 (b)、part 120 (c)、part 113 (d)），酸化食品全程受 B/C/G 约束。结论必须按危害逐条切分，不能给「整厂免检」二值答案。
  tags: [117.5(d), 条件性豁免, 微生物危害, 金葡, AF 不豁免, 高频误读]

- id: t145
  title: 〔§ 114.5〕parts 110 and 117 掺假判据与 Part 110 至今有效（v4.7 纠错）
  type: term
  source_chapter: 21 CFR Part 114 §114.5（4-1-25 Edition，FR citation 80 FR 56144）；FR Doc. 2018-19855（外部核实、本包未收）；CAP-20 B2
  source_quote: |
    "The criteria in §§ 114.10, 114.80, 114.83, 114.89, and 114.100, as well as the criteria in parts 110 and 117 of this chapter, apply in determining whether an article of acidified food is adulterated:"
  summary: 酸化食品掺假判定并列引用 §§114.10/114.80/114.83/114.89/114.100 **以及 parts 110 and 117**。这**不是笔误、不是过时引用**：FDA 2018-09-12 最终规则（FR Doc. 2018-19855）撤回了 2015 规则拟于 2018-09-17 删除 part 110 的 amendatory instruction 13（`amendatory instruction 13 in the third column on page 56144 is withdrawn`），因合规日期延长会造成 4–16 个月 CGMP 空档；eCFR 现行版 Part 110 仍列 11 个 sections。由此 v4.3「Part 110 已移除、110.110 是过时引用」结论作废，正确写法是「现行仍有效、正文本包未收 → 转引未收」。⚠ 不得把 `parts 110 and 117` 改写成只有 part 117；2018-19855 正文属外部核实、引用须注明。
  tags: [114.5, parts 110 and 117, Part 110, 掺假判据, v4.7 纠错, 转引未收]

- id: t146
  title: 4.6 / 0.85 法定身份边界（low-acid foods / acid foods / acidified foods）
  type: term
  source_chapter: 21 CFR Part 113 §113.3(n)；21 CFR Part 114 §114.3(a)(b)(d)
  source_quote: |
    "Low-acid foods means any foods, other than alcoholic beverages, with a finished equilibrium pH greater than 4.6 and a water activity (aw) greater than 0.85. Tomatoes and tomato products having a finished equilibrium pH less than 4.7 are not classed as low-acid foods."
    "Acid foods means foods that have a natural pH of 4.6 or below."
    "They have a water activity (aw) greater than 0.85 and have a finished equilibrium pH of 4.6 or below."
  summary: 低酸食品＝成品平衡 pH >4.6 **且** aw >0.85（酒精饮料除外）；番茄及番茄制品 finished equilibrium pH <4.7 另有例外。酸性食品＝天然 pH ≤4.6。酸化食品＝aw >0.85 且成品平衡 pH ≤4.6（由低酸成分加酸/酸化剂而来），另有一组排除项（碳酸饮料、果酱果冻、冷藏、aw ≤0.85 等，见 §114.3(b)）。⚠ 4.6 / 0.85 是**法条层**身份边界；CP 7303.070 的 4.40 / 4.65 / 4.75 / 0.90 / 0.93 是检查员实验室触发线；L.mono 草案 ≤4.4 / ≤0.92 是建议层抑制型配方基准——三套数字不可互替。
  tags: [113.3(n), 114.3, 4.6, 0.85, finished equilibrium pH, 番茄例外, 三套数字]

- id: t147
  title: BPCS 人员监督与 §113.5 判据清单（两 part 课程覆盖不同）
  type: term
  source_chapter: 21 CFR Part 113 §113.5 / §113.10；21 CFR Part 114 §114.10
  source_quote: |
    "The criteria in §§ 113.10, 113.40, 113.60, 113.81, 113.83, 113.87, 113.89, and 113.100 shall apply in determining whether the facilities, methods, practices, and controls used by the commercial processor in the manufacture, processing, or packing of low-acid foods in hermetically sealed containers are operated or administered in a manner adequate to protect the public health."
    "This person shall supervise only in those areas for which a school approved by the Commissioner identifies the person as having satisfactorily completed training."
    "All operators of processing and packaging systems shall be under the operating supervisions of a person who has attended a school approved by the Commissioner for giving instruction in food-handling techniques, food-protection principles, personal hygiene and plant sanitation practices, pH controls and critical factors in acidification"
  summary: 〔§ 113.5〕明文列出判定商业加工商设施/方法/实践/控制是否足以保护公众健康所适用的八个条款（§§113.10、113.40、113.60、113.81、113.83、113.87、113.89、113.100）。BPCS（Better Process Control School）：Part 113 侧监督人须完成 FDA 认可学校课程，且**只能监督学校认定其合格通过的领域**〔§ 113.10〕；Part 114 侧课程另含 `pH controls and critical factors in acidification`〔§ 114.10〕，1979-03-16 前的 §108.35 与 part 113 课程视为符合。⚠ 课程认可的法源 §108.35 在 part 108，正文本包未收，标「转引未收」。
  tags: [113.5, 113.10, 114.10, BPCS, Process Authority, 108.35, 转引未收]

- id: t148
  title: Scheduled process、critical factors、FDA 调阅权与 LACF 偏差处置
  type: term
  source_chapter: 21 CFR Part 113 §113.83 / §113.87 / §113.89
  source_quote: |
    "Scheduled processes for low-acid foods shall be established by qualified persons having expert knowledge of thermal processing requirements for low-acid foods in hermetically sealed containers and having adequate facilities for making such determinations."
    "Critical factors, e.g., minimum headspace, consistency, maximum fill-in or drained weight, aw, etc., that may affect the scheduled process, shall be specified in the scheduled process."
    "Scheduled processes must be made readily available to the supervisor and any duly authorized employee of the Food and Drug Administration."
    "A system for product traffic control in the retort room shall be established to prevent unretorted product from bypassing the retort process."
    "Whenever any process is less than the scheduled process or when critical factors are out of control for any low-acid food or container system as disclosed from records by processor check or otherwise, the commercial processor of that low-acid food shall either fully reprocess that portion of the production involved"
  summary: 〔§ 113.83〕scheduled process 须由具备低酸食品热力杀菌专业知识与 adequate facilities 的 qualified persons 确立，critical factors（最小顶隙、稠度、最大装量/沥干重、aw 等）须写入 scheduled process。〔§ 113.87(b)〕FDA duly authorized employee 有权调阅 scheduled process（法条级，与 IOM 5.x 的记录索取程序分属两层，见 CAP-18）；同条要求杀菌室张贴规程、设 product traffic control 防未杀菌产品绕过 retort、使用 heat-sensitive indicator。〔§ 113.89〕工艺低于 scheduled process 或关键因子失控 → 返工/按合格工艺重处理/评价或销毁并单独建档。⚠ FCE 注册与 SID 备案在 part 108，正文未收。
  tags: [113.83, 113.87(b), 113.89, scheduled process, critical factors, traffic control, FDA 调阅权]

- id: t149
  title: 两 part 记录保存口径不同（§113.100(g)(h) 的 1+2 年 + part 11 vs §114.100(e) 的整段 3 年）
  type: term
  source_chapter: 21 CFR Part 113 §113.100(a)(g)(h)；21 CFR Part 114 §114.100(a)–(e)
  source_quote: |
    "Processing and production information shall be entered at the time it is observed by the retort or processing system operator, or other designated person, on forms that include the product, the code number, the date, the retort or processing system number, the size of container"
    "Records of this part may be maintained electronically, provided they are in compliance with part 11 of this chapter."
    "Copies of all records provided for in paragraphs (b), (c), and (d) of this section shall be retained at the processing plant or other reasonably accessible location for a period of 3 years from the date of manufacture."
  summary: 不得串用。〔§ 113.100(a)〕加工与生产信息须 `at the time it is observed` 由 retort/processing system operator 记录；〔§ 113.100(g)〕副本在加工厂保存 ≥1 年、再在加工厂或其他合理可及地点保存另 2 年（合计 3 年；季节包停产可于季末提前转移），且 §113.83 确立 scheduled process 的记录不在 (g) 分段规则内；〔§ 113.100(h)〕允许电子记录但须符合 part 11。〔§ 114.100(a)–(d)〕给原料/包装材料/成品检验、加工与生产、偏差单独建档、初始分销四类记录；(e) 只要求 (b)(c)(d) 副本在加工厂或其他合理可及地点自生产日起保存 3 年，**无 1+2 分段、无 (h) 款、全文无 electronic / part 11 字样**。⚠ CAP-20 草稿曾把两 part 合并写成「都是 1+2 年且可用 part 11 电子记录」，v4.7 已按 CFR 正文更正。
  tags: [113.100(g)(h), 114.100(e), 1+2 年, 整段 3 年, part 11, 记录保存, v4.7 纠错]

- id: t150
  title: 〔§ 114.80〕酸化食品成品平衡 pH ≤4.6、热处理与 pH >4.0 电位法
  type: term
  source_chapter: 21 CFR Part 114 §114.80(a)(1)(2)；§114.90 方法
  source_quote: |
    "Acidified foods shall be so manufactured, processed, and packaged that a finished equilibrium pH value of 4.6 or lower is achieved within the time designated in the scheduled process and maintained in all finished foods."
    "Acidified foods shall be thermally processed to an extent that is sufficient to destroy the vegetative cells of microorganisms of public health significance"
    "If the finished equilibrium pH of the food is above 4.0, the measurement of the finished equilibrium pH shall be by a potentiometric method, and the in-process measurements by titration or colorimetry shall be related to the finished equilibrium pH."
  summary: 酸化食品须在 scheduled process 指定时间内达到成品平衡 pH ≤4.6 并在全部成品中维持；**酸化不等于免除热处理**——仍须热处理到足以杀灭公共卫生意义的微生物营养细胞（vegetative cells，不是芽孢）。成品平衡 pH >4.0 时须用电位法（potentiometric method）测定，过程中用滴定/比色的结果须与电位法结果建立关联。方法清单在〔§ 114.90〕，§113.81(e) 亦回指 §114.90。⚠ 4.0 是方法切换线，不是产品放行 pH；CP 7303.070 的 4.40 / 4.65 是 FDA 实验室双分析师复测触发线，不得当法定限值。
  tags: [114.80, 114.90, vegetative cells, potentiometric method, 4.0, 酸化不等于免热处理]

- id: t151
  title: 〔§ 114.89〕AF 偏差三条法定路径（含按 part 113 作低酸食品热处理）
  type: term
  source_chapter: 21 CFR Part 114 §114.83 / §114.89；§114.89(b)
  source_quote: |
    "The scheduled process shall be established by a qualified person who has expert knowledge acquired through appropriate training and experience in the acidification and processing of acidified foods."
    "Whenever any process operation deviates from the scheduled process for any acidified food and/or the equilibrium pH of the finished product is higher than 4.6, the commercial processor of the acidified food shall either:"
    "(b) thermally process it as a low-acid food under part 113 of this chapter;"
  summary: 〔§ 114.83〕scheduled process 须由在酸化与酸化食品加工方面具备 appropriate training and experience 的 qualified person 确立。〔§ 114.89〕当工艺偏离 scheduled process **或**成品平衡 pH >4.6，商业加工商必须三选一：(a) 由 competent processing authority 确立的工艺完全返工；(b) 按 part 113 作为低酸食品热处理；(c) 隔离并由 competent processing authority 按公认程序评价潜在公共卫生意义、留评价程序与结果记录；评价未证明安全则返工或销毁。⚠ 不是「再加点酸调到 4.5 就放行」；LACF 侧偏差走〔§ 113.89〕，两条路径不同。
  tags: [114.89, 114.83, 三条路径, part 113 热处理, competent processing authority, 偏差处置]

- id: t152
  title: Shall / Should 的法定语义、4-1-25 Edition 版次与十五类不可混引
  type: term
  source_chapter: 21 CFR Part 114 §114.3(a) 定义；21 CFR Part 113 / 114（4-1-25 Edition）FR citation；全包引用规范
  source_quote: |
    "Shall is used to state mandatory requirements."
    "Should is used to state recommended or advisory procedures or to identify recommended equipment."
  summary: Part 113 / 114 正文用 shall 表强制要求、should 表推荐或建议性程序/设备——与 FDA 指南里的 should / we recommend 不同，法规正文的 shall 是企业法定义务。⚠ `4–1–25 Edition` 是 CFR 年度编纂版次（修订至 2025-04-01），不是 2025 年新规则；条文末尾的 FR citation 才是修订出处（§114.5 为 `[80 FR 56144, Sept. 17, 2015]`，§113.100 为 `[44 FR 16215 ... as amended at 76 FR 11923, Mar. 3, 2011]`）。两份 PDF 是 GPO 双栏印刷版连续页截取，按「页 → 左栏 → 右栏」重排并保留印刷断词连字符，检索以 § 编号为准。v4.7 起**十二类不可混引**（v4.8 增至十三类、v4.9 增至十四类）：三套法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕＋ PCHF 指南 / L.mono 指南 / SECG / Ed.5 / Handbook / CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070；检查员作业指导不创设企业义务。
  tags: [shall, should, 4-1-25 Edition, FR citation, 双栏转换, 十四类不可混引, v4.7]


- id: t153
  title: FSVPI（§1.500 importer）与美国货主/收货人定义
  type: term
  source_chapter: CP 7303.878 PART I.1 / 21 CFR part 1 subpart L §1.500（转引未收）
  summary: FSVP 语境下的 importer 指入境时该食品的美国货主或收货人；若入境时没有美国货主/收货人，则为经签署同意书确认、代表境外货主/收货人的美国代理或代表，可缩写 FSVPI。不要把「进口商」泛化成报关行、货代或境外出口商；CP 7303.878 自己写明 `the term importer hereinafter means importer as defined in 21 CFR 1.500`。
  tags: [FSVP, FSVPI, 1.500, 进口商定义, CP 7303.878, v4.8]

- id: t154
  title: FSVP 与 Part 117 Subpart G 供应链程序是两套法源、两类主体
  type: term
  source_chapter: CP 7303.878 PART II.3.A / 21 CFR part 117 Subpart G〔§ 117.135〕
  summary: FSVP 由 FSMA §301 增订的 FD&C Act §805 授权，法规为 21 CFR part 1 subpart L（§§1.500–1.514），义务主体是进口商 FSVPI；Supply-Chain Program 由 FD&C Act §418 授权、法规为 21 CFR part 117 Subpart G，义务主体是接收设施 receiving facility。二者常被混为「供应商验证」，但法条编号、记录要求与检查 program 都不同。本包未收 part 1 subpart L 正文，一律标「转引未收」。
  tags: [FSVP, 供应链程序, 双法源, 805, 418, 1.500, 117.135, v4.8]

- id: t155
  title: deemed compliance 与 §1.509 例外
  type: term
  source_chapter: CP 7303.878 PART II.3.A / CPGM 7303.040 PART III
  summary: 进口商同时是 manufacturer/processor 且被认定符合 21 CFR part 117（或 507）供应链要求时，视为对其进口食品符合 FSVP 要求；但原文括号 `except they must comply with section 1.509 of the FSVP regulation` 把入境标识义务单独留下。反向口径同样重要：不是 receiving facility 的进口商 `must comply with the FSVP requirements for that food`，没有该通道；仅受 Subpart B CGMP 或 §117.206 / §507.51 约束的仓储设施也可能单独接受 FSVP 检查。
  tags: [deemed compliance, 1.509, receiving facility, 117.206, 507.51, v4.8]

- id: t156
  title: §1.509 每一 entry line 的 UFI / DUNS 申报
  type: term
  source_chapter: CP 7303.878 PART I.1 / PART V.1.A
  summary: FSVPI 须确保在向 CBP 报关时，对**每一条 entry line** 以电子方式提供其名称、电子邮箱与 FDA 认可的唯一设施标识 UFI；FDA 认可的是 DUNS 号码。不是「每年报一次」或「每家企业报一次」。PART V.1.A 把未确保这些信息电子申报列为较轻一档观察，PART III.1.A 把相关 handout 列为检查员应提供的资源。
  tags: [1.509, UFI, DUNS, CBP, entry line, FSVP, v4.8]

- id: t157
  title: §1.501 八类 FSVP 豁免与 modified requirements 分节
  type: term
  source_chapter: CP 7303.878 PART I.1 / PART I.2
  summary: 豁免见 §1.501(b)–(h)：符合 part 120 / 123 的果汁与水产及其原料、研究评估用、个人消费、酒精饮料相关、转运过境、进口加工后复出口且不在美销售、美国出口后未再境外加工而退回、进口时受 USDA 管辖的特定肉禽蛋制品。FSVP 条款又分 standard（§1.502/503/504/505/506/508/509/510）与 modified（§1.507 危害进口后受控、§1.511 膳食补充剂、§1.512 VSI 或小境外供应商、§1.513 SRA）；原文明确符合 modified 条件者**可以选择**走 standard。part 120 正文本包未收、**part 123 自 v4.9 起已收（见 CAP-22）**。
  tags: [1.501, 豁免, standard requirements, modified requirements, 1.512, 1.513, v4.8]

- id: t158
  title: FSVP 检查不取样、PART IV 全空
  type: term
  source_chapter: CP 7303.878 PART III.1.C / PART IV
  summary: 原文 `Samples will not be collected as part of an FSVP inspection.`，PART IV – ANALYTICAL 四节全部 `Intentionally Left Blank`。FSVP 检查是记录审评型：查按食品建立的 FSVP、书面危害分析、供应商批准评价与验证活动记录、§1.509 记录、纠正措施。不得把 CP 7303.050 的 subs 样品量、环境拭子、WGS / PAF 代码套过来；检查可 on-site 或 remote（RRA 的法定地位另见 CAP-19）。
  tags: [不取样, PART IV, 记录审评, 7303.050, RRA, 483a, v4.8]

- id: t159
  title: FSVP 483a 观察分级、NAI/VAI/OAI 与执法裁量因素
  type: term
  source_chapter: CP 7303.878 PART V.1
  summary: 最重大观察包括未 develop/maintain/follow FSVP、无书面危害分析或未记录对他方危害分析的审阅（尤其 SAHCODHA 危害）、无供应商批准评价、无验证活动、未履行 modified requirement 活动、以及 FDA 书面索取后未及时提供 FSVP 记录；较轻一档含未记录批准、未建书面程序、未记录 FSVP 变更、未确保 §1.509 信息。分类为 NAI / VAI / OAI。PART V.1.C 要求权衡违法史、SAHCODHA 风险、进口量、是否首次检查（`Initial FSVP violations should be prioritized ... only when there are known food safety risks`）、偏差范围、自愿合规与渐进改善、是否换商号继续进口。
  tags: [483a, NAI, VAI, OAI, SAHCODHA, 执法裁量, v4.8]

- id: t160
  title: §801(a)(3) 拒绝入境、§301(zz) 禁止行为与 direct reference authority
  type: term
  source_chapter: CP 7303.878 PART V.2 / PART V.3
  summary: FSVPI 不符合 FSVP 即违反 §805；FDA 可依 §801(a)(3) / §1.514(a) 拒绝该食品入境，官方指控措辞见 CAP-21 R 段；无合规 FSVP 而进口另构成 §301(zz)（21 U.S.C. 331(zz)）/ §1.514(b) 禁止行为，并可引出 §302 禁令、§303 刑事与 §306 debarment。但 WL / Untitled Letter / Import Alert 99-41 的 direct reference authority **只在有限情形授予**（HFP Enforcement Bulletin #13），其余须经 CMS 送 HFP OCE OE Imports Enforcement Branch（动物食品 CVM OSC DFC）并取得分类一致。
  tags: [801(a)(3), 301(zz), 1.514, direct reference, CMS, 拒绝入境, v4.8]

- id: t161
  title: Import Alert 99-41 Red List 与 99-37/99-38 不得混引
  type: term
  source_chapter: CP 7303.878 PART V.3.C / CP 7303.070 PART V.2
  summary: 99-41 针对 FSVP 不合规进口商，按「具体食品 + 具体境外供应商」组合或全部食品列入 Red List；未列组合在不受其他掺假/误标 Alert 约束时仍可继续进口，移除须按 99-41 指示向原发函 Division 提交证据、经 CMS 建议并咨询 Center，且应先申请移除再进口。99-37 / 99-38 属 CP 7303.070 的 LACF/AF 备案与过程控制轨道，且该卡另有「不得仅因未注册/未备案建议 DWPE」的反直觉限制。两者触发条件、列名对象与法律 hook 都不同。
  tags: [99-41, Red List, 99-37, 99-38, DWPE, 移除流程, v4.8]

- id: t162
  title: CP 7303.878 版本口径、CP 7303.819 状态与十五类不可混引
  type: term
  source_chapter: CP 7303.878 首页 / Change History p4 / 全包引用规范
  summary: 本件是 Transmittal 2023-CPM-CFSAN-003、Implementation Date 09/27/2023 的 2023 版程序，Date of Issuance 08/28/2025 对应 Change History 的 Corrections（仅重组后 POC 与机构名称缩写更新），不是 2025 新 program；与 7303.050（2022/2025-09-10 更正）、7303.070（2024/2025-09-26 更正）同型。CP 7303.819 是 2006 FY06/07/08 旧程序、已过 COMPLETION DATE 9/30/08 而非现行，准确说法不是「法规意义上废止」。全包自 v4.8 起十三类、**v4.9 起十四类不可混引**：四套法规正文〔§ 117/113/114/123.xxx〕＋ PCHF 指南 / L.mono 指南 / SECG / Ed.5 / Handbook 五类参考指南层 ＋ CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / CP 7303.878 五类检查员作业层；检查员作业指导不创设企业义务。
  tags: [7303.878, 版本陷阱, 7303.819, 十四类不可混引, 收录边界, v4.8]

- id: t163
  title: fish 与 fishery product 的法定范围（§123.3(d)(e)）
  summary: >-
    〔§ 123.3(d)〕fish 含淡水与海水真骨鱼、甲壳类、其他水生动物（明列鳄鱼、蛙、水龟、水母、海参、海胆及其卵），
    明确不含鸟与哺乳动物，且包含全部软体动物，前提是供人食用；〔§ 123.3(e)〕fishery product 指以鱼为特征配料的
    任何人类食品。边界意义：鳄鱼、蛙腿、水龟等边缘物种属 part 123 管辖而非普通食品；但 birds 与 mammals
    （如养殖兔、鳄梨除外）不属 fish。判定顺序是先看物种是否落入 (d)、再看成品是否以鱼为特征配料。

- id: t164
  title: processing 的三项法定排除（§123.3(k)(2)）
  summary: >-
    〔§ 123.3(k)〕把 processing 定义为 handling、storing、preparing、heading、eviscerating、shucking、freezing、
    改变市场形态、manufacturing、preserving、packing、labeling、码头卸货与 holding 等；(k)(2) 明列三项不适用本 part：
    (i) 不从事其他加工的捕捞或运输、(ii) 仅为在捕捞船上暂存而进行的去头、去内脏或冷冻、(iii) 零售经营。
    这三项同时也是 §117.5(b) 豁免的边界之外——不在 processing 内的活动不属 part 123 管辖，因而不能主张
    「受 part 123 管辖所以免 Subparts C/G」，须回到 Part 117 自行判定。

- id: t165
  title: §123.5(a) 默认适用与 §117.5(b) 双向锁定
  summary: >-
    两处法条构成双向锁定：〔§ 123.5(a)〕原文 Except as provided by § 117.5(b), parts 110 and 117 of this chapter
    apply，即 Part 110 / 117 是默认适用、§117.5(b) 是唯一例外出口；〔§ 117.5(b)〕则规定 Subparts C and G 对受
    part 123 管辖的 activities 不适用，条件是 required to comply with 且 in compliance with part 123。
    推论：做水产品不等于只按 part 123 管；也不能因为「我们做 HACCP」就认为 PCHF 整体不适用。

- id: t166
  title: §117.5(b) 无限缩款——不得套用 part 113 的微生物限制
  summary: >-
    part 113 的豁免有〔§ 117.5(d)(2)〕追加限制：仅适用于 part 113 管辖的微生物危害。part 123 的〔§ 117.5(b)〕
    没有对应条款。因此两个方向都错：把 part 113 的「仅限微生物危害」搬过来会低估豁免范围（误以为化学、物理危害
    仍须 PCHF）；因为「没限缩」就推成整厂免检会高估豁免范围（忽略 activities 限定与 Subpart B 不在豁免内）。
    正确口径是「受 part 123 管辖的 activities 范围内的 Subparts C/G」。

- id: t167
  title: Subpart B / C 的 augments 语义与 §123.16 的例外只排一条
  summary: >-
    〔§ 123.15〕与〔§ 123.20〕都用 This subpart augments subpart A of this part 表述，即熏制熏味水产品与
    新鲜冷冻双壳软体动物的专项要求是叠加在 Subpart A 之上，不是另一套替代体系；漏 Subpart A 的 HACCP 计划、
    纠正措施、验证、记录、培训即为漏项。另需区分两种例外范围：〔§ 123.16〕的 except those subject to part 113 or 114
    只排除该条自身，Subpart A 全套义务仍适用；〔§ 123.20〕则是对「含足以杀灭公众健康意义微生物繁殖体处理的加工」
    整体不适用 Subpart C。

- id: t168
  title: HACCP 计划的九项危害考虑清单（§123.6(c)(1)）
  summary: >-
    〔§ 123.6(c)(1)〕要求列出按 (a) 识别的、须对每种水产品控制的 RTL 危害，并以 Consideration should be given to
    whether any food safety hazards are reasonably likely to occur as a result of the following 引出 (i)–(ix) 共 9 项：
    自然毒素、微生物污染、化学污染、农药、兽药残留、鲭鱼毒素种或其他种的分解、寄生虫、未经批准的直接或间接食品
    或着色添加剂使用、物理危害。措辞是 should be given 的考虑清单而非强制穷举，但漏考虑属危害分析缺陷；
    寄生虫项有三个触发条件（已知或应知将不经足以灭虫的工艺食用、声称、标示或意图如此食用）。

- id: t169
  title: 纠正措施三条路径与隔离扣留顺序（§123.7）
  summary: >-
    〔§ 123.7(a)〕给两个入口：(1) 按预先制定的纠正措施计划，或 (2) 按 (c) 程序。〔§ 123.7(b)〕的纠正措施计划
    须确保 No product enters commerce that is either injurious to health or is otherwise adulterated as a result of
    the deviation，并纠正偏差原因。〔§ 123.7(c)〕的顺序是：先按 (c)(1) Segregate and hold 隔离扣留 → (c)(2) 由
    具备适当培训或经验者评审可接受性（该培训 may or may not include §123.10 培训）→ (c)(3)(4) 必要时纠正产品与
    原因 → (c)(5) 由按 §123.10 培训者及时复审并必要时修改 HACCP 计划。跳过隔离直接放行是最常见的违规形态。

- id: t170
  title: 验证的两个时间硬指标——1 周复审与至少每年复审（§123.8）
  summary: >-
    〔§ 123.8(a)(3)(i)〕要求 CCP 监控记录的复审须在记录形成后 1 周内完成（This review shall occur within 1 week
    of the day that the records are made），(a)(3)(ii) 对纠正措施记录给同一时限；两项复审均须由按 §123.10 培训者
    签名并注明日期。(a)(1) 另要求 HACCP 计划在可能影响危害分析或改动计划的变更发生时及至少每年一次复审，
    且复审显示计划不再满足 §123.6(c) 时须立即修改。1 周是法条明文，不是内部 SOP 自定的建议值。

- id: t171
  title: 三套记录保存口径不可串用（§123.9 / §113.100 / §114.100）
  summary: >-
    part 123 按产品类型分档：〔§ 123.9(b)(1)〕冷藏产品自记录形成日起至少 1 年、冷冻保藏或货架稳定产品至少 2 年，
    存于加工场所或进口商美国营业地；(b)(2) 设备或工艺总体适宜性记录（含科学研究与评价结果）至少 2 年，起算点
    是从其对该产品的适用性；(b)(3) 季节性停产或船上偏远加工点存储受限时可在季末转移至其他合理可及地点，
    但须应要求立即归还；(f) 电子记录可接受但须有适当控制确保数据与签名完整性。对照：Part 113〔§ 113.100(g)〕
    是厂内至少 1 年加另存 2 年（1+2 分段）且 (h) 引 part 11；Part 114〔§ 114.100(e)〕是自生产日起整段 3 年、
    无分段、无 part 11 条款。三套写法互推即错，不得统一写成「法规要求 3 年」。

- id: t172
  title: §123.12 进口商验证与 FSVP 是双轨，及 Part 123 版本口径
  summary: >-
    〔§ 123.12〕是 part 123 自带的进口商义务：二选一为 (a)(1) 从与 FDA 有现行有效 MOU 的国家采购（须覆盖该产品、
    证明检查体系等效、准确反映现状、整体可执行）或 (a)(2) 建立并实施书面验证程序，程序至少列产品规格与
    (a)(2)(ii)(A)–(F) 中至少一项 affirmative step；(b) 可聘 competent third party 协助或代为执行、包括代写程序；
    (c) 保存英文记录；(d) 无等效保证即视为掺假并拒绝入境。该轨与 FSVP（21 CFR part 1 subpart L，法源 FD&C Act §805）
    是两套法源两套结构，可共用证据但互不替代；FSVP 的 deemed compliance 明文只免 FSVP 且保留 §1.509 义务，
    不覆盖 §123.12。版本口径：4-1-25 Edition 是 CFR 年度编纂版次而非 2025 新规，SOURCE 为 60 FR 65197 (1995-12-18)；
    CP 7303.842 海产品检查程序与 part 120、1240、108、110 正文仍未收，一律标转引未收；
    全包口径由 v4.8 十三类升为 v4.9 十四类不可混引。
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

## 自检记录

- [x] 全部条目回 source.md 原文核验（Introduction III.A 150–372 行、III.B 374–610 行、Ch3 3278–3400 行、Ch4/6/11/14/15/16 及 Appendix 3 18790–18845 行）
- [x] 区分法定定义（21 CFR 117.3）与指南自定义（III.B / 各章 Terms 表）——用 tags 标注
- [x] 不做筛选：三层级 hazard 词族、五类预防控制、管理组件、过敏原、供应链、化学、召回、酸化、卫生全覆盖
- [x] 110 条（原始 84 条 + 21 CFR Part 117 增量 1 条 + L.mono 指南 XIX Glossary 增量 15 条 + SECG 增量 10 条；按"宁错杀"原则超额收录，多为同一词条的法定/自定义双轨或成对辨析条目）
- [x] 第三来源《Control of Listeria monocytogenes in RTE Foods (Draft, 2017-01)》术语 t86–t100 已并入；t64 与 t98 为同源词条的通用定义/专项精确定义双轨，已互链；harborage site / lethality treatment / operating limits / prerequisite programs / cleaning-sanitize / correction / validation / verification / FSP 等已有等价条目，不重复新增 id
- [x] 第四来源 FDA《Small Entity Compliance Guide》(2016-10) 术语 t101–t106 已并入；SECG 章节号与〔§ 117.xxx〕分列标注，四层效力栈见 cgmp-compliance-guide 卡；allergen cross-contact 已有既有条目，不重复新增 id
- [x] SECG 三处已知简化（供应商强制现场审核、qualified facility 双向通知、撤销豁免完整程序）与 § 117.5(k) 五类不适用情形已补为 t107–t110，均标注 SECG 未展开之处
- [x] 高频误读类术语（potential hazard、operating limit、correction、validation、supplier、equilibrium pH、action level）均含常识差异说明
- [x] 第五来源 FDA《食品过敏原标签问答 Ed.5》(2025-01 修订终版) 术语 t111–t113 已并入；全部标注为 FD&C Act 标签解释层，不与〔§ 117.xxx〕法定义务混引
- [x] 第六来源 FDA《Food Defect Levels Handbook》术语 t114–t117 已并入（defect action level 执法裁量性质、lowest level currently feasible 持续义务、110.110 引用纠错（v4.7：Part 110 至今有效、正文未收）、SIGNIFICANCE 美学/健康危害分诊）；手册原文标「Handbook 章名 + 产品名」，法规标〔§ 117.xxx〕，两者不混引
- [x] 第七来源 FDA CPGM 7303.040 现行版（`2025-CPM-HFP-001`）术语 t118–t122 已并入（三层分级、Focused PCHF / 03040U 改义、official review 记录举证、483 回复 15 工作日、Limited Scope 取证边界）；CPGM 原文标「CPGM 7303.040 PART x」，法规标〔§ 117.xxx〕，检查员作业指导不升格为企业义务；2020 版旧口径单列为版本陷阱
- [x] 第八来源 FDA CP 7303.050（2022 签发 / 2025-09-10 更正）术语 t123–t127 已并入（版本形态与『非检查 program』、subs 与 702(b)、环境拭子 50/100 与 Zone、WGS/GenomeTrakr 与拭子不计数、三档 Findings 与 Direct Reference）；原文标「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」，subs 数一律注明为 FDA 取证量而非放行标准
- [x] 第九来源 FDA IOM 2026 Chapter 5 术语 t128–t134 已并入（483 措辞纪律与 Category 3 non-reportable observation、表单地图、预告三层、拒绝边界与 807(b)、样品合格不阻碍 cGMP 指控与证据固定、九类不可混引与 IOM 收录范围、PAC/PAF 与报样系统）；原文标「IOM 5.x.x / IOM Exhibit 5-x」，遇跨章引用标『转引未收』
- [x] 第十来源 FDA CP 7303.070（2024 签发 / 2025-09-26 更正）术语 t135–t142 已并入（版本形态、§117.5(d)(1)(2) 管辖分流与 AF 不豁免、法源三角转引未收、酸化判定三步与 Maximum Equilibrium pH、三套 pH/aw 数字、异常罐 1% 与 24 罐/12 罐、Import Alert 99-37/99-38 与 DWPE 陷阱、RRA 程序性定义与 Keep Refrigerated / brites 路由）；原文标「CP 7303.070 PART x / ATTACHMENT x」，21 CFR part 108 / 110 / 120 等未收正文一律标『转引未收』（其中 Part 113 / 114 正文自 v4.7 起已收、Part 123 自 v4.9 起已收）；全包口径 v4.6 十类 → v4.7 十二类 → **v4.8 十三类不可混引**，全库 **162 条**
- [x] 第十一来源 **21 CFR Part 113**（4-1-25 Edition，36 页 / 10 条款）与第十二来源 **21 CFR Part 114**（7 页 / 8 条款）法规正文已并入，术语 t143–t152 共 10 条（并行适用、条件性有限豁免、§114.5 与 Part 110 纠错、4.6/0.85 法定身份、BPCS 与 §113.5、scheduled process 与 FDA 调阅权、**两 part 记录保存口径差异**、§114.80 热处理与电位法、§114.89 三条偏差路径、shall/should 与十二类不可混引）；引文全部取自 CAP-20 R 段已逐字核验的 26 个英文引用块；原文标〔§ 113.xxx〕〔§ 114.xxx〕，与〔§ 117.xxx〕并列但互不混引。**v4.7 同步更正 t116（Part 110 至今有效、正文未收）与 CAP-20 草稿把两 part 记录合并为「都是 1+2 年」的错误**

- [x] 第十三来源 FDA CP 7303.878（Transmittal 2023-CPM-CFSAN-003，2023-09-27 版 / 2025-08-28 更正，33 页 / 20 书签）术语 t153–t162 共 10 条已并入（FSVPI 定义、FSVP 与 Part 117 Subpart G 双法源、deemed compliance 与 §1.509 例外、每一 entry line 的 UFI/DUNS、§1.501 豁免与 standard/modified 分节、FSVP 检查不取样、483a 观察分级与 NAI/VAI/OAI、§801(a)(3)/§301(zz) 与 direct reference、Import Alert 99-41 与 99-37/99-38 区分、版本口径与十三类不可混引）；原文标「CP 7303.878 PART x」，21 CFR part 1 subpart L 正文一律标『转引未收』。全库 162 条，v4.8。

- [x] 第十四来源 **21 CFR Part 123**（Fish and Fishery Products，4-1-25 Edition，9 页 / 13 条款）法规正文已并入，术语 t163–t172 共 10 条（fish 与 fishery product 范围、processing 三项排除、§123.5(a) 默认适用与 §117.5(b) 双向锁定、§117.5(b) 无限缩款、augments 语义与 §123.16 例外范围、九项危害考虑清单、纠正措施三条路径与隔离扣留顺序、1 周复审与每年复审、三套记录期口径不可串用、§123.12 与 FSVP 双轨及版本口径）；引文取自 CAP-22 R 段已逐字核验的 33 个英文引用块（32 条 Part 123 + 1 条 §117.5(b)）。原文标〔§ 123.xxx〕，CP 7303.842 与 part 120/1240/108/110 一律标『转引未收』。全库 **172 条**，v4.9。

- [x] 第十五来源 **FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版（June 2022，SGR 129）** 技术指南已并入，术语 t173–t182 共 10 条，围绕**完整危害分析判定链**排布：should 的效力层级 → hazard analysis 与 HACCP plan 书面化义务不对称 → species/process-related 二分 → reasonably likely to occur 与无控制假设态 → significant hazard 等价且不等于本步设 CCP → Worksheet 六栏 → control strategy example 与 CCP 漂移 → CCP 至少一个 → critical limit 与替代限值论证 → 监控四问。引文取自 CAP-23 R 段经 `.cangjie/verify_v4_10_quotes.py` 逐字核验的 **37 个英文引用块**（37/37 命中源文件正文区，0 超 100 词，0 表格引用）。原文标「Seafood Hazards Guide 第 4 版 Ch.x / L####」，法条标〔§ 123.xxx〕，两者不可混引；CP 7303.842、NSSP Guide、part 120/1240/108/110/507、Appendix 5 回指的 CPG 与 CFR 外部法源一律标『转引未收』。全库 **182 条**，v4.10，**十五类来源不可混引**。
