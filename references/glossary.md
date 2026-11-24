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
  summary: CP 7303.050 的样品量以 **subs（份样）** 计：Table 2 给 Salmonella（如叶菜 30 subs × 100 g、番茄 10 subs × 454 g、RTE 三明治 30 subs × 100 g、散装奶酪按重量分 10/2/1 subs），Table 3 给其他分析物（如 L. mono 10 subs × 200 g、EHEC/STEC 10 × 50 g、Cyclospora 5 × 50 g、甲肝/诺如 3 × 150 g）。三条硬规则：① **样品量不含 702(b) 部分**；② 多分析物按最大 subs 数取足且每 sub 同时满足各分析物用量；③ **易腐产品与进口状态样品不取 702(b) 部分**（21 CFR 2.10(b)(3)）。ATTACHMENT B 的污秽/霉变样在无专门指令时为随机 10 个 2 lb subs，奶酪制样取 6 个 227 g 且不得合并。⚠ 这些是 **FDA 检查员的取证量**，不是企业批放行抽样计划、不是内控规格；企业抽样须依自身危害分析与验证另定。**702(b) 分割留样细则自 v4.16 起已有原文出处**：IOM Chapter 4 `4.3.2.2 / 4.3.2.3 / 4.7.4`（第二十来源，见 CAP-28 与 t227）。
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
  tags: [CP 7303.070, 版本陷阱, 更正本, PAC, PAF, 十七类不可混引]

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
  summary: 检查员取证口径。**异常容器 >1% 且企业未做 spoilage diagnosis**（判定腐败原因与批次能否放行）是检查员侧的显著观察项；PART V.1 把「异常容器 ≥1% 批确认掺假或进行性腐败」列为通知 Center 的触发之一；进口侧异常率 1% 以上须另提 DTR。pH 分析取样：**≤795 g（28 oz）取 24 罐，其余 12 罐**；具体抽样计划出处是 **IOM Chapter 4, Sample Schedule Chart 2（自 v4.16 起已收，见 CAP-28 与 t232）**；⚠ 它是取样计划，与 CP 7303.070 PART IV.2 的 pH 4.40/4.65 实验室触发线属两层。实验室对正常容器做 **14 天 progressive decomp** 培养，异常罐另做气体/气味/外观、净重与沥干重、漏罐测试、卷边解剖与内壁状态检查；`C. botulinum` 分析**仅 for-cause**（PAF `MIC`），涉病走 BAM Ch.17、不涉病走 BAM Ch.21A，典型分离株做 WGS 送 HFP/OLOAS 做毒素基因评价。⚠ 这些都是 FDA 取证与执法建议口径，不是企业内控抽样或放行标准。
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
  summary: 程序定义与两条路由。**RRA（Remote Regulatory Assessment）**：FDA 可对 AF/LACF 企业开展**自愿、全程远程**的记录/设施评估；CP 明确 `RRAs are not considered inspections`，不满足 FD&C Act 704 条要求现场 inspection 的法定场景（如 510(h)、503B(b)）。这是 **CP 内的程序性定义**，可据此回答「RRA 算不算检查」，但 **FDA 扩大 RRA 适用范围 / 境外无预告检查的政策公告原文仍未收**，不得据此推导政策，也不能替换 IOM 5.2.7 的预告三层口径。**两条路由**：`Keep Refrigerated` 产品免 21 CFR 113/114 → 归 **CP 7303.050（CAP-17）**；未贴标 AF/LACF「brites」运至中央仓贴标装箱的检查报 **`PAC 03040`（CAP-16）**。另：动物食品 LACF 用 `71070` 并联动 7371.000 / 21 CFR 507.5(b)；海产品 LACF 并做 7303.842 HACCP。**收录边界（v4.7 更新）**：第十来源 CP 7303.070 已收（CAP-19）；**第十一、十二来源 21 CFR Part 113 / 114 法规正文亦已收（CAP-20）**，全包口径为 v4.6 十类 → v4.7 十二类 → v4.8 十三类 → **v4.9 十四类不可混引**。仍未收：21 CFR part 108（FCE/SID/Emergency Permit）、**part 110（旧 CGMP，至今有效但正文未收）**、part 120（**part 123 自 v4.9 起已收，见 CAP-22**）（**IOM Ch.4 Chart 2 自 v4.16 起已收，见 t232**）、BAM、CPG、Import Alert 全文、其余 Compliance Programs，一律标「转引未收」。
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
  title: Shall / Should 的法定语义、4-1-25 Edition 版次与十七类不可混引
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
  source_chapter: CP 7303.878 PART I.1 / 〔§ 1.500〕（v4.21 起正文已收，CAP-33）
  summary: FSVP 语境下的 importer 指入境时该食品的美国货主或收货人；若入境时没有美国货主/收货人，则为经签署同意书确认、代表境外货主/收货人的美国代理或代表，可缩写 FSVPI。不要把「进口商」泛化成报关行、货代或境外出口商；CP 7303.878 自己写明 `the term importer hereinafter means importer as defined in 21 CFR 1.500`。
  tags: [FSVP, FSVPI, 1.500, 进口商定义, CP 7303.878, v4.8]

- id: t154
  title: FSVP 与 Part 117 Subpart G 供应链程序是两套法源、两类主体
  type: term
  source_chapter: CP 7303.878 PART II.3.A / 21 CFR part 117 Subpart G〔§ 117.135〕
  summary: FSVP 由 FSMA §301 增订的 FD&C Act §805 授权，法规为 21 CFR part 1 subpart L（§§1.500–1.514），义务主体是进口商 FSVPI；Supply-Chain Program 由 FD&C Act §418 授权、法规为 21 CFR part 117 Subpart G，义务主体是接收设施 receiving facility。二者常被混为「供应商验证」，但法条编号、记录要求与检查 program 都不同。part 1 subpart L 正文自 v4.21 起已收（CAP-33 `fsvp-statutory-requirements`），〔§ 1.5xx〕为企业义务的唯一基准，检查员侧仍回 CAP-21。
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
  title: CP 7303.878 版本口径、CP 7303.819 状态与十七类不可混引
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

- id: t183
  title: CP 7303.842 的版本判定与 CP 7303.844 合并口径
  summary: >-
    FDA《Compliance Program Guidance Manual 7303.842》封面写 IMPLEMENTATION DATE 11/01/2023、
    Correction date 09/30/2025、Date of Issuance 09/30/025（PDF 文本层残缺），正文页脚一律
    11/1/2023，PDF creationDate 2025-09-29。故文件名 20250929 只是**生成日**，本件是
    **2023-11-01 版程序的 2025-09-30 更正本**，不是 2025 新签发 program；与 CP 7303.050 /
    7303.070 / 7303.878 同属「旧程序 + 更正本」形态，不同于 CPGM 7303.040 的 2025-CPM-HFP-001
    新 Transmittal。首页 NOTE 与 PART I 写明 CP 7303.842（Seafood Processor Inspection Program）
    与 CP 7303.844（Imported Seafood Inspection Program）**已合并为单一程序**，但 PAC codes for
    sampling and analysis 仍区分进口与国产 —— 合并的是程序，不是码表。
  tags: [CP 7303.842, 版本判定, 更正本, CP 7303.844, 程序合并, 十七类不可混引]

- id: t184
  title: 检查程序作业层的效力边界（非法规、非 Guidance for Industry、不创设义务）
  summary: >-
    CP 7303.842 是 FDA 给检查员、进口分区、分部合规官与实验室的**内部作业指导**
    （PART I/II 明写 provides instruction to field staff），覆盖检查优先级、检查实施、取样、
    实验室分析分流、执法建议与报告上报。它不是法规、不是 Guidance for Industry，也不创设企业义务；
    企业义务仍回 21 CFR Part 123〔§ 123.xxx〕与 Part 117 Subparts A/B/F。CP 原文 L276 明写
    Part 117 subparts C/G 不能替代 Part 123 的法定义务。**双向误读都要防**：既不能把 CP 的检查动作
    写成企业义务，也不能因 CP 非强制把 Part 123 的 shall 义务稀释成可选。
  tags: [检查程序作业层, 内部作业指导, field staff, 不创设企业义务, 法条义务层, 三层配对]

- id: t185
  title: Table 1 与 Table 2 的分工、90/10 与 100 entry line items
  summary: >-
    Table 1（Product and Process Priority Ranking）按产品/工艺危害与行业合规情况**降序**排
    commodities，用于确定 HACCP 检查焦点；原文 Table 1 is not all inclusive，表外产品/工艺须查
    Hazards Guide 第 3 章，产品跨多类取**最高风险类别**，取样风险判定也用 Table 1。Table 2
    （Priorities for Establishment and Importer Inspections）**仅用于 work planning**，在 Table 1
    基础上按企业/进口商个体合规史降序；进口商检查数量由 OII workplan 定，**90%** 给高风险进口商、
    **10%** 给年进口 <100 entry line items 者；OAI 复检须待整改完成。两者不可对调。
  tags: [Table 1, Table 2, work planning, 90/10, 100 entry line items, OII Workplan, 检查优先级]

- id: t186
  title: 六类检查分流与各自的专门限制
  summary: >-
    PART III 分流：① Processor（多程序适用时分别覆盖、时间有限优先 03842H）；② Importer
    （〔§ 123.12〕验证、Table 2 选人 / Table 1 选产品、食品安全 MOU 国家产品排除、书面验证程序与
    affirmative steps、每产品一份 FD 3502；**境外加工商 HACCP 计划的其他缺陷不得写进 483**，须取
    副本转 HFP）；③ Vessels（通常靠港且非作业时检查）；④ Foreign Establishments（产品风险 + 合规史
    选点、只覆盖输美产品、须取文档与照片证据）；⑤ NSSP（须 shellfish standardized inspector /
    officer，用 ISSC Form 93-01(A)、依 NSSP Model Ordinance）；⑥ EMA / Food Fraud（一般监督须先得
    HFP concurrence，比对采购订单/原料标签/成品标签）。
  tags: [Processor Inspections, Importer Inspections, Vessels, Foreign Establishments, NSSP, EMA, 检查分流]

- id: t187
  title: PAC 双码表、03842H 同名不同义与 documentary samples 硬约束
  summary: >-
    取样/分析 PAC 进口 03844x / 04844A / 07844 / 09844x / 21844、国产 03842x / 04842A / 07842 /
    09842x / 21842；检查报告 PAC 另有 03842（documentary / 非 HACCP 评估）、03842H（Processor
    HACCP Inspection）、03844H（Importer HACCP Inspection）、03040（PC training）。⚠ **03842H
    在取样表是 HACCP Verification（验证 HACCP 计划关键限值充分性）且进口列 Not applicable，在报告表
    却是 Processor HACCP Inspection —— 同名不同义**。所有 documentary samples **只报 PAC 03842**，
    不得用以 H 结尾的 HACCP 验证 PAC，也不计入 Division Workplan 义务。
  tags: [PAC, 03842H, 03844H, documentary samples, HACCP Verification, 双码表, 报告归属]

- id: t188
  title: Sampling 三类与「不取样」同样是结论
  summary: >-
    ① 国产官方样品 Domestic official samples are to be collected "for cause" only；不必常规采国产样
    支持 HACCP 违规的监管行动，控制明显不足时**不取样**而在 483 说明控制缺失、EIR 描述条件，确需取样
    须先联系 HFP。② 进口监督取样数量由 OII Workplan 定、既往有安全缺陷的国外加工商/发货人条目优先、
    多数样品取自高风险产品。③ Documentary samples 见 t187。ATTACHMENT A 的 702(b) duplicate 部分
    不含在表列 subs 内、Filth 仅 for cause、CFP 只在疾病/暴发响应时采、RTE 才做 Listeria。
  tags: [Sampling, for cause only, Imported Surveillance, Documentary Samples, ATTACHMENT A, 不取样]

- id: t189
  title: PART IV 阈值是检查员作业口径，不是法规限值或放行标准
  summary: >-
    组胺 500 / 50 / 35 ppm、Indole 15 / 25 µg per 100 g、感官 subs 18 / 24 / 12 / 18、活虫零容忍、
    pH <4.6（腌渍品追加分析结束条件）、熏鱼 nitrite 100 ppm、RSSL ≥98% / <98%、净重过镀冰 48 subs、
    未去脏鱼 5 inches、Filth 6 个 2–3 lb subs —— 全部是 CP 的**追加分析 / 取样量 / 上报触发口径**，
    不是法规限值、不是产品合格判定标准、不是 BAM / AOAC 方法全文。判据出口是 CPG Sec. 540.525 /
    540.370 / 562.300 / 555.600 / 540.250 与 Hazards Guide 第 6 章 action levels（本包多为未收）；
    subs 数多处明说 only for surveillance and audit samples，reconditioning / DWPE 放行 /
    Domestic HACCP Verification 各有不同规则。
  tags: [PART IV, Criteria for Regulatory Action, 检查员触发值, CPG 540.525, 非法规限值, 转引未收]

- id: t190
  title: Table 4 是 ranking 工具，与 §123.6 显著性判定、自动执法结论分离
  summary: >-
    PART V 的 Table 4（Seafood HACCP Enforcement Strategy: Ranking of violation）逐条给
    Deficiency → Citation(123.x) → Major/Minor 映射，但原文 Significance must be determined on a
    case-by-case basis。Major/Minor 定义针对 HACCP 系统完整性与食品安全风险，**不是**〔§ 123.6〕
    hazard analysis 的 reasonably likely to occur / significant hazard 判定，也不是自动执法结论；
    记录伪造归 Title 18 / OCI 不在表内分级；非 123 违规（misbranding / EMA / 非鲭毒分解 /
    非安全 GMP）另走 Compliance Intake and Consultation Form。
  tags: [Table 4, Major Minor, case-by-case, 违规分级, 123.6 显著性, 非自动执法]

- id: t191
  title: 执法裁量、Center concurrence 与物种误标的法律定性
  summary: >-
    Warning Letters 原文 should be considered；DWPE 针对国外检查/记录审查偏差未纠正的境外加工商，
    放行或移出 import alert 须 HFP OCE concurrence 与英文证据；judicial actions 建议须 HFP OCE
    评估同意、FACTS 入案、CMS 电子提交；NMFS 通知依 FDA–NMFS MOU / FMD#-029。Species misbranding
    的定性是 **FD&C Act 403(b) / 21 U.S.C. 343(b)**，监管建议经 MARCS-CMS；物种替换可能**引入**
    海洋毒素/过敏原/鲭毒等额外安全危害，此时才转 CAP-23 做危害分析 —— 法律定性与危害判定分离。
    Import Alert 16-74 / 16-20 与 99-41 / 99-37 / 99-38 不是同一组。
  tags: [Warning Letters, DWPE, HFP OCE, judicial actions, 403(b), Species Misbranding, Import Alert 16-74]

- id: t192
  title: 十七类不可混引、引用规范、仍未收清单与转换质量红线
  summary: >-
    自 v4.12 起全包 **十七类来源不可混引**。CP 7303.842 引用写「CP 7303.842 PART x / Table x /
    ATTACHMENT A #x / Lxxx」；法条写〔§ 123.xxx〕〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕；指南写
    「Seafood Hazards Guide 第 4 版 Ch.x」；其它 CP / IOM / Handbook / SECG / Ed.5 各用其自身编号。
    仍未收：CPG 540.525 / 540.370 / 555.600 / 562.300 / 540.250 / 540.590 全文、21 CFR part 120 /
    1240 / 108 / 110 / 507、NSSP Guide、BAM / AOAC / MPM 方法全文、Import Alert 16-xx / 99-41 全文、
    21 CFR part 1 subpart L、FDA 3501 / 3502 表单全文、eNSpect / CMS / FACTS 内部系统（IOM Ch.4 自 v4.16 起已收，见 CAP-28）。
    转换件存在书签标题与正文伪标题交错（PART 各出现两次、H1 虚高 133）、`<u>` / `<br>` 标签、
    表格列头连写与页码混入，**检索以 PART / 小节 / 表号为准**，逐字引用只取散文段落且须剥离标记。
  tags: [十七类不可混引, 引用规范, 转引未收, 转换质量红线, 标题层级交错, v4.11]
# ============ 十七、21 CFR Part 108 紧急许可控制词族（v4.12）============

- id: t193
  title: emergency permit（紧急许可）
  type: term
  source_chapter: 21 CFR 108.3(d)；108.6(a)；108.25(a)；108.35(a)
  source_quote: |
    "Permit means an emergency permit issued by the Commissioner pursuant to section 404 of the act for such
    temporary period of time as may be necessary to protect the public health."
    —— 〔§ 108.3(d)〕
  summary: 依 FD&C Act §404 签发、附条件、临时性的许可。**最大的常识差异：它不是 LACF／酸化食品企业的常态义务**。108.25(a)／108.35(a) 用的都是 `may be required whenever the Commissioner finds ... that the commercial processor has failed to fulfill all the requirements of this section`，108.6(a) 再加 `A permit shall be required only during such temporary period`。也就是说：注册、备案、报告、BPCS 主管、记录是 **shall 级常态义务**；许可本身是**未履行义务后的救济手段**。凡输出「LACF 企业必须持紧急许可证」即为定性错误。
  tags: [法定定义, 核心概念, 高频误读, 十七来源]

- id: t194
  title: FCE registration（罐头企业注册，Form FDA 2541）
  type: term
  source_chapter: 21 CFR 108.25(c)(1)；108.35(c)(1)
  source_quote: |
    "shall, not later than 10 days after first so engaging, register and file with the Food and Drug Administration
    on Form FDA 2541 (food canning establishment registration) information"
  summary: 首次在任一州从事酸化食品或 LACF 的制造/加工/包装后 **10 个日历日**内，以 **Form FDA 2541** 注册。内容含企业名称、主营业地、各加工场所、加工方式（酸化食品按酸度与 pH 控制；LACF 按所用加工设备类型）与各场所食品清单。**外国加工者的时点更早**：`Foreign processors shall register before any offering of foods for import into the United States`（报检前，不受 10 天约束）。停业须在 90 天内通知，季节性停产与劳资纠纷/火灾/天灾等临时情形除外。注册是 FCE（Food Canning Establishment）编号的来源，与「许可」无关。
  tags: [手续义务, 时限, 十七来源]

- id: t195
  title: process filing（工艺备案）与 Form 2541e / 2541d / 2541f / 2541g
  type: term
  source_chapter: 21 CFR 108.25(c)(2)；108.35(c)(2)
  source_quote: |
    "shall, not later than 60 days after registration, and before packing any new product, provide the Food and
    Drug Administration information on the scheduled processes"
  summary: 注册后 **60 个日历日**内、且**包装任何新产品之前**，按每个食品每个容器规格分别备案 scheduled process。表单按形态分流：酸化食品 **2541e**（Acidified Method）；LACF **2541d**（Low-Acid Retorted）、**2541f**（Water Activity/Formulation Control）、**2541g**（Low-Acid Aseptic）。LACF 备案须含加工方法、设备类型、最低初温、时间温度、**杀菌值 Fo** 或其他等效科学证据、影响热穿透的关键因子。**关键区别**：备案 `Filing of this information does not constitute approval`——不是「等 FDA 批准才能生产」；所报工艺信息属 21 U.S.C. 331(j) / 18 U.S.C. 1905 意义的商业秘密。这套东西旧称 SID（Scheduled Process Information filing），现行法条只写 process filing。
  tags: [手续义务, 时限, 表单, 高频误读, 十七来源]

- id: t196
  title: prima facie basis（初步依据）
  type: term
  source_chapter: 21 CFR 108.25(a)；108.35(a)
  source_quote: |
    "Failure to meet these requirements shall constitute a prima facie basis for the immediate application of the
    emergency permit control provisions of section 404 of the act to that establishment, under the procedures
    established in subpart A of this part."
  summary: 未履行 108.25／108.35 义务（含注册与工艺备案）构成 FDA **立即适用** §404 紧急许可控制的「初步依据」。注意层级：「初步依据」是**启动 Subpart A 程序的理由**，不等于许可已生效——仍须走裁定 → 通知 → 3 个工作日异议 → 5 个工作日听证 → 裁定的完整链条。把 prima facie basis 读成「自动被要求持证」是常见越级误读。
  tags: [法定概念, 程序层级, 十七来源]

- id: t197
  title: working days 与日历天（Part 108 的两种时限）
  type: term
  source_chapter: 21 CFR 108.5(a)(1)；108.7(b)；108.10(b)；108.25(c)(1)；108.35(c)(2)
  source_quote: |
    "shall have 3 working days after receipt of such order within which to file objections."
    —— 〔§ 108.5(a)(1)〕
  summary: Part 108 混用两种日，**不可互换**。Subpart A 的**程序时限**全是 `working days`：3 个工作日提异议、听证 5 个工作日、听证后 5 个工作日裁定、许可申请 10 个工作日（可再延 10）、恢复申请 10 个工作日、无证产品放行 20 个工作日、工艺资料延期批复 30 个工作日。Subpart B 的**申报时限**全是日历天：注册 10 天、备案 60 天、停业通知 90 天、工艺变更报送 30 天。把「10 个工作日」写成「10 天」会让企业错过窗口，反之会让企业误以为还有余量。
  tags: [时限, 高频误读, 十七来源]

- id: t198
  title: retained product 与 advance written approval（无证生产的扣留与放行）
  type: term
  source_chapter: 21 CFR 108.12(a)
  source_quote: |
    "All food so manufactured, processed, or packed during such period without a permit shall be retained by the
    manufacturer, processor, or packer and may not be introduced or delivered for introduction into interstate
    commerce without the advance written approval of the Food and Drug Administration."
  summary: 企业被裁定需要许可但尚未取得时，可 `at his own risk` 继续生产，但该期间产品**必须由企业扣留**，未经 FDA **事先书面**批准不得进入州际贸易。放行的唯一实体门槛是 `an adequate showing that such food is free from microorganisms of public health significance`；FDA 须在收到书面请求后 20 个工作日内答复。企业可另交 competent authority 的公共卫生意义评估作为举证材料，但那不是放行依据。**注意这不是「无证生产即违法」**，而是「无证生产 + 产品不得自由流通」。108.12(b) 的合并仓库例外只覆盖「运到自有仓库」这一段。
  tags: [法定义务, 产品放行, 高频误读, 十七来源]

- id: t199
  title: refuse admission（拒绝入境，§801）
  type: term
  source_chapter: 21 CFR 108.25(j)；108.35(k)(1)
  source_quote: |
    "in lieu of providing for the issuance of an emergency permit under paragraph (a) of this section, the
    Commissioner will request the Secretary of the Treasury to refuse admission into the United States, pursuant to
    section 801 of the act"
  summary: 对外国商业加工者**不发紧急许可**，改为由 Commissioner 请求财政部长依 FD&C Act §801 拒绝入境。被拒产品须待 Commissioner 认定该加工者已合规且食品不致害方可入境，为此 FDA **保留现场检查权**〔§ 108.35(k)(2)〕。因此「外国 LACF 加工者会被要求办紧急许可」是错的——国内走许可、境外走拒绝入境，两条路方向相反。
  tags: [法定义务, 进口, 高频误读, 十七来源]

- id: t200
  title: school approved by the Commissioner（BPCS 类受训主管）
  type: term
  source_chapter: 21 CFR 108.25(f)；108.35(g)
  source_quote: |
    "shall be under the operating supervision of a person who has attended a school approved by the Commissioner"
  summary: 酸化工序人员（酸化、pH 控制、热处理等关键工序）与 LACF 的杀菌锅／热处理／无菌系统操作者**以及容器封口检查员**，须在参加过 Commissioner 批准学校并 `satisfactorily completed` 规定课程者监督下作业。108.25(f) 的课程内容法定列明（food-handling techniques、food protection principles、personal hygiene、plant sanitation practices、pH controls、critical factors in acidification）；108.35(g) 覆盖 retort / aseptic / container closure inspection，**加州除外**。1979-03-16 前完成 §108.35 / part 113 相应课程者视为已完成。BPCS 是行业对该类课程的通行称谓，法条本身只写 `school approved by the Commissioner`。
  tags: [法定义务, 人员培训, 十七来源]

- id: t201
  title: Part 108 记录保存（四套口径不可合并）
  type: term
  source_chapter: 21 CFR 108.25(g)；108.35(h)；113.100(g)；114.100(e)
  source_quote: |
    "shall prepare, review, and retain at the processing plant for a period of not less than one year, and at the
    processing plant or other reasonably accessible location for an additional two years, all records of processing,
    deviations in processing, container closure inspections, and other records specified in part 113 of this chapter."
    —— 〔§ 108.35(h)〕
  summary: 四套口径分别成立：① 〔§ 108.25(g)〕酸化食品**整段 3 年**（自生产日）；② 〔§ 108.35(h)〕LACF **厂内 ≥1 年 + 另 2 年**（合计 3 年，第一年季节性长停可季末转移）；③ 〔§ 113.100(g)〕厂内 ≥1 年 + 另 2 年，且 (h) 允许符合 part 11 的电子记录；④ 〔§ 114.100(e)〕整段 3 年，**无分段、无 part 11 条款**。起算点与存放地点要求各不相同，把四者合并成「3 年」一句交付即为错答。依 §704 检查时均须允许 FDA 授权雇员查阅复制。
  tags: [法定义务, 记录保存, 高频误读, 十七来源]

- id: t202
  title: intentional change 与「升参数不算变更」
  type: term
  source_chapter: 21 CFR 108.35(c)(2)(ii)
  source_quote: |
    "Any intentional change of a previously filed scheduled process or modification thereof in which the change
    consists solely of a higher initial temperature, a higher retort temperature, or a longer processing time, shall
    not be considered a change subject to this paragraph"
  summary: 所谓「降参数」——降低初温／杀菌温度、缩短时间、改配方／容器／其他基本条件——是法条意义上的故意变更：须**使用前**取得 qualified scientific authority 对充分性的证实，证实可先电话取得但须立即记录、书面确认并存档，且**首次使用后 30 天内**向 LACF Registration Coordinator 报送变更描述与证实记录。**升参数**（更高初温／更高杀菌温度／更长时间）**不算**本条变更，但若将定期采用仍须及时重新备案。另〔§ 108.35(c)(2)(iii)〕的「operating process」（操作者按高于 scheduled process 的参数运行）**也不构成**对 scheduled process 的修改——这两处常被反向误读成「任何工艺调整都无需报告」。
  tags: [法定义务, 工艺变更, 高频误读, 十七来源]

# ============ 十八、21 CFR Part 120 果汁 HACCP 词族（v4.13）============

- id: t203
  title: juice 与 Part 120 的管辖边界
  type: term
  source_chapter: 21 CFR 120.1(a)；120.3(j)(2)；120.3(l)
  source_quote: |
    "Any juice sold as such or used as an ingredient in beverages shall be processed in accordance with the
    requirements of this part."
    —— 〔§ 120.1(a)〕
  summary: juice 包括水果蔬菜榨取的水性液体、其可食部分果泥、或该液体/果泥的浓缩物；**作饮料配料也算**（`as an ingredient in beverages`），且不论是否曾进入州际贸易均适用。三层排除：① `Raw agricultural ingredients of juice are not subject to the requirements of this part`（〔§ 120.1(a)〕）；② 〔§ 120.3(j)(2)〕processing 不含「不从事其他加工的采收/采摘/运输」与「零售经营」；③ 〔§ 120.3(l)〕零售 establishment 若同时向其他企业销售或分销果汁则**不属**零售。常见误读：以为「浓缩汁复配」或「作配料卖给饮料厂」能跳出 Part 120——两者都在管辖内。
  tags: [法定定义, 管辖边界, 高频误读, 十八来源]

- id: t204
  title: 5-log reduction（果汁的法定削减指标）
  type: term
  source_chapter: 21 CFR 120.24(a)
  source_quote: |
    "a 5 log (i.e., 105) reduction, for a period at least as long as the shelf life of the product when stored
    under normal and moderate abuse conditions, in the pertinent microorganism"
  summary: 这是**法定要求**（`shall` 级），不是 FDA 建议。三个限定缺一不可：① **持续**（`consistently produce`）；② 覆盖**至少整个货架期**；③ 在**正常与中度滥用条件**下仍成立。⚠ 原文 `105` 是 PDF 文本层上标丢失，应为 10 的 5 次方（10⁵），引用须还原并注明。把它说成「指南建议 5-log」是最常见的效力误判。
  tags: [法定要求, 高频误读, 十八来源]

- id: t205
  title: pertinent microorganism（目标菌）
  type: term
  source_chapter: 21 CFR 120.24(a)
  source_quote: |
    "the most resistant microorganism of public health significance that is likely to occur in the juice"
  summary: 三条件同时成立：**最耐热** + **具公共卫生意义** + **在该果汁中可能出现**。果汁种类不同，目标菌可能不同，因此不存在「果汁 HACCP 一律针对沙门氏菌」或「一律针对大肠杆菌 O157」这种答案。⚠ 与〔§ 120.25〕的 **biotype I E. coli** 不是同一概念——后者是**果面处理专项验证的指示菌**，不得与 5-log 的目标菌互换。
  tags: [法定定义, 高频误读, 十八来源]

- id: t206
  title: HACCP 计划的七要素与「have and implement」
  type: term
  source_chapter: 21 CFR 120.8(a)(1)(2)；(b)(1)–(7)
  source_quote: |
    "Each processor shall have and implement a written HACCP plan whenever a hazard analysis reveals one or more
    food hazards that are reasonably likely to occur during processing"
  summary: 法条用的是「have and implement」，即**两份义务**——有书面计划 + 在运行，只写不做即违反。计划须**按加工场所**与**按果汁种类**分别制定；可对危害/CCP/关键限值/程序本质相同的产品分组，但**特定产品或工艺独有的要素**须在计划中清楚界定并在实践中遵守。七要素：(1) 列出须控制危害；(2) 列出各危害的 CCP，含 (i) 厂内引入与 (ii) 厂外（含采收前中后）引入两类；(3) 关键限值；(4) 监控程序与频次；(5) 按 §120.10(a) 的纠正行动计划；(6) 验证与确认程序及频次；(7) 记录系统（须载明监控的**实际值与观察**）。
  tags: [法定义务, 计划要素, 十八来源]

- id: t207
  title: reasonably likely to occur（果汁版的判定基准）
  type: term
  source_chapter: 21 CFR 120.7(a)(2)
  source_quote: |
    "A food hazard that is reasonably likely to occur is one for which a prudent processor would establish controls
    because experience, illness data, scientific reports, or other information provide a basis to conclude that there
    is a reasonable possibility that, in the absence of those controls, the food hazard will occur in the particular
    type of product being processed."
  summary: 判定基准是 **prudent processor 会不会设控制**，证据来源为经验、疾病数据、科学报告等；落脚点是 `in the particular type of product being processed`——**同一危害在不同果汁里结论可以不同**。评估还须含**严重性**判断〔§ 120.7(a)(2)〕。⚠ 危害分析须覆盖**厂内与厂外**、含**采收前中后**〔§ 120.7(b)〕，并列出〔§ 120.7(c)〕九项应考虑危害——注意 (c) 用 `should be given`，是**考虑清单**而非强制穷举，但漏考虑属分析缺陷。
  tags: [法定概念, 判定方法, 十八来源]

- id: t208
  title: SSOP 八项与 HACCP 计划的关系
  type: term
  source_chapter: 21 CFR 120.6(a)(1)–(8)；(b)；(d)
  source_quote: |
    "Sanitation standard operating procedure controls may be included in the HACCP plan required under § 120.8(b).
    However, to the extent that they are implemented in accordance with this section, they need not be included in
    the HACCP plan."
  summary: SSOP 须覆盖加工**前、中、后**的卫生条件与操作，至少含八项：接触食品/食品接触面/制冰用水安全；食品接触面（含器具、手套、外衣）状况与清洁；防不洁物与生熟交叉污染；洗手/手消毒/厕所设施；防润滑剂燃料农药清洁剂消毒剂冷凝水污染；有毒化合物标示储存使用；员工健康状况控制；防虫害进入。监测频次须至少确保符合 part 110 与 part 117 subpart B 中**既适合本厂又适合所加工食品**的条件，不符**及时**纠正。**两者关系是「可选纳入」而非「必须纳入」**：按 §120.6 监测的卫生控制不必进 HACCP 计划；反之亦然。
  tags: [法定义务, 卫生控制, 十八来源]

- id: t209
  title: 果汁的记录复审是「1 周（7 天）」而非「7 个工作日」
  type: term
  source_chapter: 21 CFR 120.11(a)(1)(iv)(A)(B)(C)
  source_quote: |
    "This review shall occur within 1 week (7 days) of the day that the records are made"
  summary: CCP 监控记录与纠正措施记录的复审须在**记录形成后 1 周（7 日历天）内**由按 §120.13 受训者**签字并注明日期**完成；校准与成品/在制品检验记录的复审只要求 `within a reasonable time`。⚠ 与 Part 117 的记录复审**工作日**口径不同，两套不可混用。另：计划确认（validation）须在**实施后 12 个月内至少一次**、此后**至少每年一次**，或工艺发生六类变化时（原料/来源、配方、加工方法或系统含软件、包装、分销系统、预期用途或消费者）；确认显示计划不足须**立即修改**〔§ 120.11(b)〕。
  tags: [法定义务, 时限, 高频误读, 十八来源]

- id: t210
  title: 果汁记录保存期（第六套口径）
  type: term
  source_chapter: 21 CFR 120.12(d)(1)(2)
  source_quote: |
    "in the case of perishable or refrigerated juices, at least 1 year after the date that such products were
    prepared, and for, in the case of frozen, preserved, or shelf stable products, 2 years or the shelf life of the
    product, whichever is greater"
  summary: 易腐或冷藏果汁 **≥1 年**；冷冻／保藏／货架稳定产品 **2 年或货架期，孰长**。**起算点是产品制备日**（`after the date that such products were prepared`），不是记录形成日、不是出厂日。异地存放：`(a)(1)` 与 `(a)(4)` 类记录在**监测发生后 6 个月**起允许，条件是**请求官方审查后 24 小时内可调取并提供到现场**；符合 (g) 的 part 11 电子记录**可视同在场**。这是全包第六套记录期口径——另有〔§ 108.25(g)〕3 年、〔§ 108.35(h)〕1+2、〔§ 113.100(g)〕1+2、〔§ 114.100(e)〕3 年、〔§ 123.9(b)(1)〕1 年/2 年，互不通用。
  tags: [法定义务, 记录保存, 高频误读, 十八来源]

- id: t211
  title: 果面处理与 biotype I E. coli 专项验证
  type: term
  source_chapter: 21 CFR 120.25
  source_quote: |
    "Each juice processor that relies on treatments that do not come into direct contact with all parts of the juice
    to achieve the requirements of § 120.24 shall analyze the finished product for biotype I Escherichia coli as
    follows"
  summary: 本条**只适用于果面处理者**（处理未接触果汁全部部分），不是所有果汁厂的常规出厂检验；靠热力杀菌达成 5-log 的厂，成品/在制品检验在〔§ 120.11(a)(1)(iii)〕下是 `At the option of the processor`。取样：**20 mL（两个 10 mL 子样）／每 1,000 加仑／每生产日**，子样随机取自**已可分销给消费者**的包装；日产量不足 1,000 加仑时按每 1,000 加仑取但**不少于每 5 个工作日一次**（注意这里是 `working days`）。方法为 AOAC 992.30 modified（ColiComplete）或等效。判读：任一子样阳性即 20 mL 记为阳性；**7 次检测中 2 次阳性 → 5-log 控制措施 `shall be deemed to be inadequate`**，须立即改用**压榨后**达成 5-log 的替代工艺 + 复审监控记录 + 按 §120.10 纠正。
  tags: [法定义务, 取样验证, 高频误读, 十八来源]

- id: t212
  title: Part 120 的两处豁免（对象不同，不可合并）
  type: term
  source_chapter: 21 CFR 120.24(a)(1)(2)；120.7(e)
  source_quote: |
    "HACCP plans for juice need not address the food hazards associated with microorganisms and microbial toxins
    that are controlled by the requirements of part 113 or part 114 of this chapter."
    —— 〔§ 120.7(e)〕
  summary: 两处豁免的**对象不同**：① 〔§ 120.24(a)(1)〕受 part 113 / 114 管辖者、〔§ 120.24(a)(2)〕单次热力步骤达货架稳定或含全部配料热处理的浓缩工艺——免的是 **5-log 这一工艺控制指标**，且 (a)(2) 以「把热力工艺副本纳入〔§ 120.7〕书面危害分析」为条件；② 〔§ 120.7(e)〕免的是 **HACCP 计划中对「part 113/114 已控制的微生物与微生物毒素」危害的处理**——范围**只到微生物类**，化学/物理/过敏原危害仍须控制。两者可同时成立也可只成立其一；把二者混成「受 113/114 管辖就不用做果汁 HACCP」是双重错误。另〔§ 120.5〕的 `Except as provided by § 117.5(c), parts 110 and 117 ... apply` 是 Part 117 默认适用的接口，而〔§ 117.5(c)〕逐字文本**本包未收**，不得反推。
  tags: [法定豁免, 法条接口, 高频误读, 十八来源]

- id: t213
  title: §117.5 四款豁免的结构差异（(b)(c) 无限缩款 vs (d) 有限缩）
  type: term
  source_chapter: 21 CFR 117.5(a)–(g)（Part 117 全文，v4.14 起随仓库分发）
  source_quote: |
    "Subparts C and G of this part do not apply with respect to activities that are subject to part 120 of this
    chapter (Hazard Analysis and Critical Control Point (HACCP) Systems) at a facility if you are required to comply
    with, and are in compliance with, part 120 of this chapter with respect to such activities."
    —— 〔§ 117.5(c)〕
  summary: 四款结构同构、**范围不同**，不可互套：(a) qualified facility → 转〔§ 117.201〕modified requirements；**(b) part 123 水产品** 与 **(c) part 120 果汁** 都是「双条件 + **无限缩款**」——`required to comply with, and are in compliance with` 两个并列条件，不合规即豁免不成立，而豁免范围内 Subparts C/G 的要求**全部**移出（含非微生物危害）；**(d) part 113 低酸罐头** 有 (d)(1) 双条件豁免 + **(d)(2) 限缩**：`applicable only with respect to the microbiological hazards that are regulated under part 113`，其余危害仍归 C/G；(e) 膳食补充剂按 part 111 + FD&C Act §761；(f) 受 §419 produce safety 管辖的活动；(g) farm mixed-type facility 的特定 pack/hold 情形。⚠ 关键判读：**不要因为 (d) 有限缩就以为 (c) 也有**，也不要因为 (c) 无限缩就以为「整厂免 PCHF」——边界止于「受该 part 管辖的 activities」，且豁免不含 Part 117 Subpart B 的 CGMP。
  tags: [法定豁免, 条款结构, 高频误读, 第二来源补齐]

# ============ 十九、CP 7303.847 果汁检查程序词族（v4.15）============

- id: t214
  title: CP 7303.847 的版本口径（文件名≠版本日）
  type: term
  source_chapter: CP 7303.847 封面
  source_quote: |
    "Date of Issuance: 11/02/2010"
    —— CP 7303.847 封面；同页另有 `IMPLEMENTATION DATE: 11/02/2010` 与 `Correction date: 09/18/2025`
  summary: 本件是 **2010-11-02 版程序的 2025-09-18 更正本**。⚠ 文件名 `20250922` 只是 PDF 生成日（creationDate 2025-09-22），**不是 2025 年新版 program**；与 CP 7303.050 / 7303.070 / 7303.842 / 7303.878 同属「旧程序 + 近期更正」形态，**不得套用 CPGM 7303.040 的 `2025-CPM-HFP-001` Transmittal 写法**。引用写「CP 7303.847（2010-11-02 版 / 2025-09-18 更正）」。
  tags: [版本口径, 高频误读, 十九来源]

- id: t215
  title: CPGM 的效力层级（不创设企业义务）
  type: term
  source_chapter: CP 7303.847 全文性质
  source_quote: |
    "A HACCP inspection is not a stand-alone part of the Juice HACCP Inspection Program but is one part of a larger
    system of control procedures."
  summary: Compliance Program Guidance Manual 是 FDA 给**检查员与分区**的内部作业指导：**非法规、非 Guidance for Industry、不创设企业义务**。它只回答「查什么、怎么取样、什么数值触发升级、文书怎么开」。企业义务回 21 CFR Part 120〔§ 120.xxx〕（CAP-26）。**不得用 CP 的检查动作反推法条，也不得把 CP 的取证量写成企业放行标准**——这是全包对 LACF（CAP-19）、海产品（CAP-24）一以贯之的纪律。
  tags: [效力层级, 核心概念, 十九来源]

- id: t216
  title: 三类样品的分流（验证／有因／文档性）与 PAC
  type: term
  source_chapter: CP 7303.847 PART III.4；封面 PAC 表
  source_quote: |
    "“Verification” samples are to be collected only when the investigator expects the inspection to be either NAI or
    VAI."
  summary: PAC 混用是本件最容易犯的硬错。① **验证（Verification）**：只在检查员**预期结果为 NAI 或 VAI** 时取，PAC 限 `847H` 系列（`03847H`/`04847H`/`07847H`/`09847H`/`21847H`），须分析 HACCP 计划中**全部相关安全危害**；② **有因（For Cause）**：**非常规**，仅在需判定安全问题范围时取，PAC 限 `03847`/`04847`/`07847`/`09847`；③ **文档性（Documentary）**：**只报 `03847`**，不得占用 `847H`，**且不计入分区工作计划**；④ 进口商报 `03847H` 且 Establishment Type 必须用 **A**（Importer/Broker）。
  tags: [手续义务, PAC, 高频误读, 十九来源]

- id: t217
  title: 「没取样」不能反推「没问题」的三条理由
  type: term
  source_chapter: CP 7303.847 PART II.2.A.2；PART III.4
  source_quote: |
    "Most deficiencies of the Juice HACCP regulation do not require a physical sample to confirm or document them."
  summary: 三条**独立**理由，任一成立即可解释「没取样」：① **进口商检查根本不取样**（`No samples are to be collected`）；② 验证样品**只在预期 NAI/VAI 时取**——检查员已倾向 OAI 时就不取；③ 原文自己写的：**多数法规缺陷不需要实物样品**（记录与执行面即可坐实）。因此「没取样」既可能是预期结果偏好，也可能只是本次属记录类缺陷；把它读成「合规」或「被放过」都是错的。反向也成立：**被取样不能证明被怀疑**。
  tags: [判定方法, 高频误读, 十九来源]

- id: t218
  title: HACCP 与非 HACCP 双检查组件
  type: term
  source_chapter: CP 7303.847 PART II.1；PART III.3
  source_quote: |
    "It is important to remember that the primary component of a juice inspection is HACCP, but also includes
    sanitation monitoring."
  summary: 加工者检查 = ① **HACCP 系统检查**（独立做一遍危害分析与 CCP 判定，再评企业的计划、关键限值、监控与记录）；② **非 HACCP 覆盖**（彻底 GMP 检查，含发网、安全照明等；污秽须记录蝇类数量类型与在产品上的时间、门窗破损路线、与粪便/垃圾/尸体的距离；标签违规；**经济欺诈**迹象）。进口商检查则是**纯记录审查**（§120.14 规格与 affirmative steps）。把果汁检查等同于"HACCP 一项"会漏掉一半取证面。
  tags: [检查流程, 取证, 十九来源]

- id: t219
  title: 进口商审查：先查 MOU，再查 affirmative steps
  type: term
  source_chapter: CP 7303.847 PART III.B；PART V
  source_quote: |
    "A HACCP plan from a foreign processor is an inadequate affirmative step under 21 CFR 120.14(a)(2) if the plan
    fails to list a hazard that is reasonably likely to occur."
  summary: 顺序是：482 → 定境外来源 → **查该国是否有适用于 juice HACCP 的 MOU**（HFP 主页列示；有则记录并**另选非 MOU 果汁**受检）→ 非 MOU 者审书面程序（产品规格 + affirmative steps）→ 审规格是否覆盖生物/物理/化学危害 → 审验证记录 → 缺陷按 **21 CFR 120.14** 用 eNSpect 引文开 483。**可据以开 483 的实体判据**：境外 HACCP 计划**漏列合理可能发生的危害**时，该计划**不构成充分的 affirmative step**。
  tags: [法定义务, 进口商, 判据, 十九来源]

- id: t220
  title: ATTACHMENT A 采样量（与触发值是两回事）
  type: term
  source_chapter: CP 7303.847 ATTACHMENT A
  source_quote: |
    "Collect ten (10) subsamples (Retail Containers) with a minimum sub- sample size of 32 fl oz."
  summary: 微生物 10 子样 × ≥32 fl oz（946 ml），零售容器——足够覆盖 E. coli O157:H7 / Listeria monocytogenes / Salmonella 三项；零售容器 >½ 加仑（1893 ml）须通知 Program Monitor。**铅** 12 随机子样 × ≥4 oz。**巴氏毒素**（仅苹果汁/苹果酒）：冷冻浓缩 6 子样 × ≥400 ml；单倍浓度 6 子样 × ≥500 ml。**污秽**：非 HACCP 6 子样、HACCP 硬/锐物 12 子样，且 `Analyze each subsample individually (no compositing)`。非 HACCP 与部分专项样品**双份供 702(b)**（`Please collect in duplicate to provide for the 702(b) portion.`）。⚠ 这些是**检查员取证量**，不是企业出厂检验标准。
  tags: [取样验证, 采样量, 十九来源]

- id: t221
  title: 铅的「拟议行动水平」不是法规限值
  type: term
  source_chapter: CP 7303.847 PART V 样品后续
  source_quote: |
    "proposed action levels of 0.010 mg/kg (10 ppb) in apple juice and 0.020 mg/kg (20 ppb) for other fruit and
    vegetable juices"
  summary: 出处是 **FDA 2022-04 铅草案指南**，性质是 **`proposed action levels`（拟议行动水平）**——不是法规限值、不是合规安全港。**苹果汁 10 ppb、其他果蔬汁 20 ppb**，两档不可对调。程序上：`Analyzing laboratories should refer any results above the proposed action levels to HFP for review`，由 **HFP 逐案审查**决定后续（需产品类型、检出值、采样时间地点、批次收货人）。⚠ 与 LACF 的 4.40/4.65（CP 7303.070 实验室触发线）、果汁的 5-log（〔§ 120.24(a)〕法定）分属三层，不得互替。
  tags: [数值分层, 高频误读, 十九来源]

- id: t222
  title: 升级路径与 60 天复检口径
  type: term
  source_chapter: CP 7303.847 PART V
  source_quote: |
    "the division should re-inspect the firm no later than 60 days from the last correspondence date"
  summary: 分层升级：**高风险**（暴发关联/未巴氏杀菌）且 CCP 有缺陷 → 走 CMS + RPM Ch.4 提合规行动建议；**巴氏杀菌企业** CCP 缺陷未及时纠正、企业不回应或不配合 → **最后通信日后 60 天内**复检（进口商同口径）；复检仍有原缺陷 → 联系 HFP/OCE/OCIC/DCC；**仅州内企业** → 优先借州/地方当局，无管辖权由 OII 与 HFP 商。病原阳性另走：州际判定 → 拟召回联系 HFP/Recalls → 拒不撤回联系 HFP/OCE/OCIC/DCC → 不涉州际则通报州官员。
  tags: [监管升级, 时限, 十九来源]

- id: t223
  title: 检查员不代写计划（检查纪律的出处）
  type: term
  source_chapter: CP 7303.847 PART III.1.A.1
  source_quote: |
    "this should not be interpreted to mean that either the flow chart or the HACCP plan will be prepared for the
    firm by the investigator"
  summary: 遇到无 HACCP 计划或计划不充分的企业，检查员**仍须做完整 HACCP 检查**，但**不得替企业编制流程图或 HACCP 计划**。这条既是检查纪律，也是本包「一律拒绝代写 HACCP 计划／代填表单／判法定身份」的规范出处之一（另见通用水产品卡与 Part 108 卡的同类边界）。配套：SSOP 相关 GMP 缺陷按〔§ 120.6〕引，其余 GMP 缺陷按 GMP 引并在 EIR 说明显著性；引文一律用 **eNSpect**。
  tags: [检查纪律, 边界, 十九来源]

- id: t224
  title: official sample（21 CFR 2.10 的三种管辖情形）
  type: term
  source_chapter: IOM 4.1.4 / 4.1.4.1；21 CFR 2.10
  source_quote: |
    "A sample is an _official sample_ if records (see IOM 4.4.4) or other evidence obtained show that the shipment, or other lot of the article from which the sample was collected, was: Introduced or delivered for introduction in interstate commerce, or Was in or was received in interstate commerce, or Was manufactured in a Territory or the District of Columbia."
  summary: FDA 取样的**效力起点**。三条件任一成立且有记录或证据支持，样品才是 official sample，可作为扣留/禁令/起诉的执法基础；进口样品一律是 official sample。另有四要件使样品 `valid`：随附确立联邦管辖与知情人身份的记录、代表所采之批、够实验室分析并在必要时留 702(b)、以维持证据完整性的方式标识封存并有清晰监管链。⚠ **official sample 分 physical 与 documentary（DOC）两类**，不是「只有实物才算」；INV / survey / non-regulatory 三类都不是 official sample。本包自 v4.16 起有原文（CAP-28）。
  tags: [取样程序, 法定管辖, IOM Ch.4, 二十类来源]

- id: t225
  title: DOC sample（documentary official sample）
  type: term
  source_chapter: IOM 4.1.4.1.1
  source_quote: |
    "A DOC sample is not a sample of records. It is a sample representing a lot of a regulated article"
    "Because no product is collected, a Form FDA 484, Receipt for Samples, is not issued for DOC samples."
  summary: 最易误读的样品类别。DOC **不是「记录复印件」**，而是「以记录代表一个批的 official sample」——记录本身就是样品本体，仍须代表可确立联邦管辖的批、仍须有 C/R。由标签/随附标识/州际运输记录/支持性证据构成。**两条硬例外**：`DOC samples are not officially sealed`（不贴 FDA 415a）、**不发 Form FDA 484**；但照片的电子介质另按 IOM 5.6.7.5 封。适用情形见 4.1.4.1.2（超大/固定安装/过贵/已不存在/无需化验/应急留用/拟按标签违法扣留）。⚠ 不要把「没贴封条、没开 484」读成「这次取样不算数」。
  tags: [取样程序, 样品类别, IOM Ch.4, 反直觉]

- id: t226
  title: INV / survey / non-regulatory sample（三类非 official sample）
  type: term
  source_chapter: IOM 4.1.5 / 4.1.6 / 4.1.7 / 4.3.6.6.2
  source_quote: |
    "Investigational (INV) samples are _not_ official samples."
    "Because these samples can be used as evidence in court, they must be sealed, and their integrity and chain of custody protected."
    "Survey samples are not official samples."
  summary: INV（investigational）：记录观察、支持监管行动，不需州际商业或联邦管辖；但**能进法庭，所以必须封条与完整证据链**。环境拭子、土壤、水、动物粪便、in-line/factory food、污秽 exhibit、部分投诉样一律按 **INV** 编号（产品码 `52Y[][]08` 等，不得用受检产品码）。**survey**：主动监督取数，只做数据、不作执法基础（如 DQST）。**non-regulatory**：替其他联邦/州/地方机构代做、FDA 对产品无管辖权。⚠ 把 INV 读成「非正式样品，随便采采」是本件最危险的误读。
  tags: [取样程序, 样品类别, IOM Ch.4, 证据链]

- id: t227
  title: 702(b) portion 与七项豁免（含污秽样品反向例外）
  type: term
  source_chapter: IOM 4.3.2.2 / 4.3.2.3 / 4.7.4；FD&C Act 702(b) [21 U.S.C. 372(b)]
  source_quote: |
    "FDA must, “upon request, provide a part of such official sample for examination or analysis by any person named on the label of the article, or the owner thereof, or his attorney or agent.”"
    "Note regarding filth samples: Regardless of the exemptions under 21 CFR 2.10(b) listed above, collect the 702(b) portion for filth samples, unless your supervisor directs otherwise."
  summary: 法定**分割留样请求权**（`upon request`，不是自动给付）。默认留样量 `at least twice the quantity estimated to be sufficient for analysis`（含实验室 reserve），双份子样须来自同一袋/箱/容器，并建议独立容器独立封条。**七项豁免**：① 器械与烟草不在法定范围；② 可采量不足分析量两倍（有多少采多少）；③ 两倍量成本超 $150；④ 无法以可行保存手段维持可分析状态（**明列 fresh produce / water samples / environmental swabs**）；⑤ 进口样品；⑥ 取自标签具名且为货主本人；⑦ 无标签或标签无具名者。⚠ **污秽样品是唯一反向例外**：无论豁免与否都要留。不留须在 C/R 的 Collection Remarks 写明理由。
  tags: [取样程序, 702(b), IOM Ch.4, 反直觉]

- id: t228
  title: Zone Concept 1–4 与检查员环境取样子样数
  type: term
  source_chapter: IOM 4.3.6.6.1；Exhibit 4-20 / 4-21
  source_quote: |
    "For Salmonella environmental swabbing, collect at least 100 swabs/subs and ideally 300 or more subs."
    "For Listeria environmental swabbing, collect at least 50 swabs/subs and ideally 100 or more subs."
  summary: Zone 1 直接接触面（切片机、混合机、输送带、器具、工作台）；**Zone 2** 紧邻 Zone 1（设备外表面、框架、推车、齿轮、通风、地面）；**Zone 3** 紧邻 Zone 2（走廊、门口、墙、电话、叉车）；**Zone 4** 远端（更衣室、干货/成品库、食堂、装卸区）。绝大多数子样取 Zone 1–2、Zone 3 次之、`Very few, if any ... from Zone 4`。Salmonella 以 Zone 2–4 为主（干性产品通常不采食品接触面），Listeria 以 Zone 1–2 为主（湿环境必须采接触面）；Listeria 须**生产 ≥4 小时且湿洗前**，Salmonella 宜在湿洗前。⚠ **50/100 是检查员侧最低量，不是企业 EMP 标准**；企业点位与频次依〔§ 117.165(a)(3)〕与自身危害分析。
  tags: [环境取样, Zone, IOM Ch.4, 检查员口径]

- id: t229
  title: 环境取样不得预告 / D-E 中和液 / 24 小时到实验室
  type: term
  source_chapter: IOM 4.3.6.6.1 / 4.3.6.6.2 / 4.7.3.6
  source_quote: |
    "it is preferable during your discussions with a firm not to mention FDA's intent to collect environmental samples until, immediately, before sampling begins"
    "transport/ship the sample to the servicing lab for analysis so it is received by the lab within 24 hours of collection."
  summary: 不得预告的理由是防止企业临时清洁、抑制微生物回收（这与 IOM 5.2.7 的「检查是否预告」是两个问题，不要读成「检查本身不通知」）。作业要点：**Dey-Engley（D/E）中和肉汤/缓冲液**为通用中和液（中和消毒剂 + 提供运输存活营养）；大面积用海绵/海绵棒，单向 `10 times vertically, then 10 times horizontally`，小面积（约 10 cm × 10 cm）Dacron 拭子再加 `10 times diagonally`；双层袋 + 预冻凝胶冰袋冷藏不冻结，**24 小时内到实验室**；闭控按每个无菌器材批留一份、**环境样不交开控**；冷藏样 ≤4.4 °C（40 °F）。**换手套规则**：Zone 2–4 且属常规监督抽样时同一 zone 内不必逐子换（每子间用 70% 乙醇消毒），**Zone 1 与 for-cause 检查仍须逐子换**。
  tags: [环境取样, 作业约束, IOM Ch.4, 反直觉]

- id: t230
  title: 表单链与 FDA 415a 官方封条的三条硬规则
  type: term
  source_chapter: IOM 4.2.5 / 4.7.4 / 4.7.5.3；Exhibit 4-4 / 4-5 / 4-17
  source_quote: |
    "The receipt is to be issued to the owner, operator, or agent-in-charge, upon completion of the inspection, but prior to leaving the premises."
    "The seal must bear only one signature."
    "Never place more than one sample in the same officially sealed package."
  summary: 按动作对号：到场检查 → FDA 482；运途中取样 → 给承运人 FDA 482 + **FDA 472 Carriers Receipt**；取任何实体样品 → **FDA 484 Receipt for Samples**（检查结束、离场前签发）；封样 → **FDA 415a Official Seal**（或金属封条）；包装标识 → **FDA 525**；证言 → FDA 463a / 1664 / 1664a / 1664b；州际证据 → FD 1662。**三类不发 482/484**：induced / undercover / online；DOC 另明文不发 484、不贴封条。**封条三硬规则**：只能一个签名（多人时由编制并签署 C/R 者签）、一样一封、702(b) 建议独立容器独立封条；封条可用至厂商有效期后 **5 年**；拆封后须重封并把每一张用过的封条随记录提交。不封条的唯一例外是「连续亲自保管 + 主管与实验室同意 + 当日提交」。
  tags: [取样程序, 表单链, 封条, IOM Ch.4]

- id: t231
  title: 阳性环境结果上 FDA 483 的门槛与 704(d) 四问
  type: term
  source_chapter: IOM 4.3.6.6.5 / 4.6.2.58 / 4.6.2.9
  source_quote: |
    "Significant positive environmental sample results, from swabs collected at food firms, are to be reported on the FDA 483 if the results are known prior to the conclusion/closeout of the inspection."
    "Environmental samples do not meet the criteria of 704(d) but FDA provides the sample results to firms."
  summary: 上 483 的三条件（foods program 适用）：① 属当前或未来 foods program 检查；② **检查未关账前已知**（原文明确不得为等结果延长检查）；③ 构成显著观察——Listeria 阳性在 **Zone 1/2**，或 Salmonella 阳性在 **Zone 2/3**。**Zone 3（Listeria）与 Zone 4（任一病原）不写**，除非与 Zone 1/2 阳性合并以加强执法。`704(d)` 四问全 yes 才勾（是食品 / 检查期间采 / 取自制造加工包装食品的场所 / 为查明是否含污秽腐败分解物质或不适于食用），且**选择性取样的食品部分要勾、环境样品明确不勾**（结果仍会给企业，由 HFP 发，非 OII 职责）。
  tags: [阳性结果, FDA 483, 704(d), IOM Ch.4]

- id: t232
  title: IOM Sample Schedule Chart 2（LACF / AF 取样计划）
  type: term
  source_chapter: IOM Sample Schedule Chart 2；4.3.6.4
  source_quote: |
    "The sample will consist of all abnormal containers and the number of normal cans specified under “2. Official Samples” below"
    "Sample size does not include 702(b) portion"
  summary: 全包从 v4.6 起反复标「未收」的取样量出处，自 v4.16 起有原文（CAP-28）。**LACF 现场检查**：按批大小对表，达到规定异常罐数即提前终止并取样（3/5/6/7/8/9/10/11 对应八档）；异常罐分 flipper / springer / soft swell / hard swell，**leaker 不计入「abnormal containers」**、只报数不采。**official sample = 全部异常罐 + 规定正常罐**（正常罐数已含 702(b)）；**investigational / import = 全部异常 + 12 正常罐**。污秽/微生物取样：≤795 g（28 oz）≤50 箱取 48 罐、>50 箱取 96 罐；>795 g ≤600 箱取 48 罐、>600 箱取 72 罐。**AF 的 pH 取样**：>795 g 取 12 罐（12 箱各 1）、≤795 g 取 24 罐（12 箱各 2），**且明确不含 702(b)**，异常罐另加至多 24 罐。⚠ 这是**取样计划**，与 CP 7303.070 PART IV.2 的 4.40/4.65/4.75 **实验室触发线**属两层，不得混写成一条数。转换件的四组列在 GFM 后错列，只引「批大小 → 检查数 → 提前终止数」对应关系。
  tags: [取样量, LACF, Chart 2, IOM Ch.4, 两层不得混引]

- id: t233
  title: 六套取样数量的分层与 IOM Ch.4 转换件引用纪律
  type: term
  source_chapter: CAP-28 E-Step 7 / B10 / B12；IOM 4.3.2 / 4.3.6.2
  source_quote: |
    "To determine sample size, first consult your assignment. If the assignment doesn't specify the sample size, follow the guidance in the applicable Compliance Program. The IOM SAMPLE SCHEDULE ... should be used if the Compliance Program doesn't state the sample size."
  summary: 取样量三级优先 **assignment → 适用 Compliance Program → IOM Sample Schedule**；三级都无才用通用规则（箱数平方根、12–36 子样、不足 12 全取、带 702(b) 时双份）。**六套数字互不替代**：① 50/100 环境子样数（IOM 4.3.6.6.1）；② 114 g / 4 oz 与 10 个零售容器（IOM 4.3.6.6.3/4）；③ Chart 2 的 48/96/72 罐（LACF 取样计划）；④ AF 的 12/24 罐（pH 取样，不含 702(b)）；⑤ CP 7303.050 Table 2/3（CAP-17）；⑥ 4.40/4.65/4.75 与 24 罐/12 罐（CP 7303.070 PART IV.2 实验室触发线，CAP-19）。**转换件四处红线**：文件前部 Word 点线目录块与 `picture intentionally omitted` 占位不可逐字引；书签错位（4.7.2 在 4.7.1 之前、4.6.4 混入 4.7 区）故检索以 `4.x.x` 小节号为准；`## **Dry Ice Guidance**` 等为伪标题；Chart 2 表格错列须回查 PDF。引用写「IOM 4.x.x / IOM Exhibit 4-xx / IOM Sample Schedule Chart x」，**不得写成〔§ 117.xxx〕**。
  tags: [引用规范, 分层, IOM Ch.4, 二十类来源]



# ============ v4.18 增量：21 CFR Part 101 食品标签法规正文（t234–t277，44 条） ============

- id: t234
  title: principal display panel (PDP)
  type: term
  source_chapter: 21 CFR Part 101 § 101.1（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The term principal display panel as it applies to food in package form and as used in this part, means the part of a label that is most likely to be displayed, presented, shown, or examined under customary conditions of display for retail sale. The principal display panel shall be large enough to accommodate all the mandatory label information required to be placed thereon by this part with clarity and conspicuousness and without obscuring design, vignettes, or crowding. Where packages bear alternate principal display panels, information required to be placed on the"'
  summary: 主展示面指包装食品在惯常零售陈列条件下最可能被展示、呈现、观看或检视的那部分标签，法定判据是「最可能被陈列」而非视觉直觉上的正面；该面须足够大，能清晰、显著且不遮挡地容纳本 part 要求置于其上的全部强制信息。面积按矩形高乘宽、圆柱或近圆柱容器高度的 40% 乘周长、其他形状总表面积的 40% 计算，且圆柱容器的强制信息必须落在这 40% 内；有备选主展示面时信息须逐面重复。常见误解是把它当成可自由指定的正面版式，忽略面积公式与重复义务。
  tags:
  - 标签载体
  - PDP
  - 位置义务
  - v4.18
  - Part 101
  - 法规正文层

- id: t235
  title: information panel
  type: term
  source_chapter: 21 CFR Part 101 § 101.2（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The term information panel as it applies to packaged food means that part of the label immediately contiguous and to the right of the principal display panel as observed by an individual facing the principal display panel with the following exceptions:"'
  summary: 信息面板指包装食品标签上紧邻主展示面、位于其右侧的那部分标签，以观察者面对主展示面时的方位为准，法定判据是相对方位而非任意空白面。条款另列例外：右侧紧邻面过小或不可用（如折叠翻盖、罐端）时可顺延至再右侧的下一个面板，有备选主展示面时以任一主展示面右侧为准。常见误解是把营养标签或配料表随便挪到背面即可，实际位置是可开观察项的法定义务。
  tags:
  - 标签载体
  - 信息面板
  - 位置义务
  - v4.18
  - Part 101
  - 法规正文层

- id: t236
  title: statement of identity
  type: term
  source_chapter: 21 CFR Part 101 § 101.3（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"(a) The principal display panel of a food in package form shall bear as one of its principal features a statement of the identity of the commodity. (b) Such statement of identity shall be in terms of: (1) The name now or hereafter specified in or required by any applicable Federal law or regulation; or, in the absence thereof, (2) The common or usual name of the food; or, in the absence thereof, (3) An appropriately descriptive term, or when the nature of the food is obvious, a fanciful name commonly used by the public for such food."'
  summary: 身份声明是主展示面上须作为主要特征之一载明的食品身份说明，法定顺序为：适用法律或法规已规定或要求的名称，缺失时用该食品的通用或常用名，再缺失时用适当描述性用语或公众惯用的臆造名（食品性质显而易见时）。各种可选形态（整、片、丁等）属身份声明必要部分并以相应字号标示，仿制食品还须以同等字号标注 imitation。常见误解是把品牌名当身份声明，或忽略形态与仿制标注的字号、粗体、平行基线要求。
  tags:
  - 品名
  - 身份声明
  - SubpartA
  - v4.18
  - Part 101
  - 法规正文层

- id: t237
  title: designation of ingredients (descending order of predominance)
  type: term
  source_chapter: 21 CFR Part 101 § 101.4（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Ingredients required to be declared on the label or labeling of a food, including foods that comply with standards of identity, except those ingredients exempted by § 101.100, shall be listed by common or usual name in descending order of predominance by weight on either the principal display panel or the information panel in accordance with the provisions of § 101.2, except that ingredients in dietary supplements that are listed in the nutrition label in accordance with § 101.36 need not be repeated in the ingredient list. Paragraph (g) of this section describes the ingredient list on dietary supplement products."'
  summary: 配料表须把应申报的各配料按通用或常用名依重量占比降序列于主展示面或信息面板，受 §101.100 豁免者除外；含量 2% 及以下的配料可在末尾以量化说明合并列示，配料名须用具体名而非集合统称。常见误解是把「按重量降序」当成可协商的排版偏好，或把配料申报等同于过敏原管控。需特别注意，本条是 Part 101 标签法源层，与 Part 117 预防控制层不同：Part 117〔§117.135(c)(2)〕管的是确保正确标签用到正确产品的标签控制这一预防控制，本条管的是标签上配料内容本身该写什么。
  tags:
  - 配料表
  - 降序
  - 与Part117区分
  - v4.18
  - Part 101
  - 法规正文层

- id: t238
  title: net quantity of contents
  type: term
  source_chapter: 21 CFR Part 101 § 101.7（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The principal display panel of a food in package form shall bear a declaration of the net quantity of contents. This shall be expressed in the terms of weight, measure, numerical count, or a combination of numerical count and weight or measure. The statement shall be in terms of fluid measure if the food is liquid, or in terms of weight if the food is solid, semisolid, or viscous, or a mixture of solid and liquid; except that such statement may be in terms of dry measure if the food is a fresh fruit, fresh vegetable, or"'
  summary: 净含量声明须置于主展示面，以重量、度量、计数或计数与重量/度量组合表达；液体用液量单位，固体、半固体、黏稠或固液混合物用重量，鲜果蔬等惯按干量出售者可用干量。常见误解是把它当作可放在背面任意位置的辅助信息，或忽略「液态用容量、固态用重量」的法定介质判据。
  tags:
  - 净含量
  - PDP
  - SubpartA
  - v4.18
  - Part 101
  - 法规正文层

- id: t239
  title: misbranding
  type: term
  source_chapter: 21 CFR Part 101 § 101.18（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Among representations in the labeling of a food which render such food misbranded is a false or misleading representation with respect to another food or a drug, device, or cosmetic. (b) The labeling of a food which contains two or more ingredients may be misleading by reason (among other reasons) of the designation of such food in such labeling by a name which includes or suggests the name of one or more but not all such ingredients, even though the names of all such ingredients are stated elsewhere in the labeling."'
  summary: 本条列举使食品构成 FD&C Act §403 意义上错标的 labeling 表述：对他种食品或药品、器械、化妆品作虚假或误导性表述；含两种以上配料却以只提及部分配料的名称命名（即便全部配料已在别处列明）；以及表达或暗示地理来源的表述（真实来源、合规商标、法定名称、消费者理解为类别而非产地的名称等除外）。常见误解是把错标与掺假混为一谈。需特别注意，本条是 Part 101 标签法源层，与 Part 117 预防控制层不同：403 misbranding 与 402 adulteration 是两条独立执法钩子，缺陷行动水平或过程失控结论不得反推为标签合规结论。
  tags:
  - 错标
  - 执法钩子
  - 与Part117区分
  - v4.18
  - Part 101
  - 法规正文层

- id: t240
  title: prominence and conspicuousness
  type: term
  source_chapter: 21 CFR Part 101 § 101.15（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"A word, statement, or other information required by or under authority of the act to appear on the label may lack that prominence and conspicuousness required by section 403(f) of the act by reason (among other reasons) of: (1) The failure of such word, statement, or information to appear on the part or panel of the label which is presented or displayed under customary conditions of purchase;"'
  summary: 强制词语、声明或其他信息若未出现在惯常购买条件下被展示的面板、未在有足够空间的多个可展示面板重复出现、标签未覆盖可用面积、因非强制内容挤占空间、因给其他内容更强显著性、或因字号字型小、背景对比不足、被图案遮挡或与图文拥挤，即可能缺乏 §403(f) 要求的显著性与醒目性；以外语呈现也可能导致空间不足豁免不适用。常见误解是显著性只是排版审美，实际它是可开具观察项的法定要件，且因非必需内容造成的空间不足不能反过来主张豁免。
  tags:
  - 显著性
  - 403(f)
  - SubpartA
  - v4.18
  - Part 101
  - 法规正文层

- id: t241
  title: labeling (与 label 的区分)
  type: term
  source_chapter: 21 CFR Part 101 § 101.15（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"If any article of labeling (other than a label) contains any representation in a foreign language, all words, statements, and other information required by or under authority of the act to appear on the label or labeling shall appear on such article of labeling."'
  summary: Part 101 大量条款并列写 label or in labeling，其中 labeling 的法定范围来自 FD&C Act §201(n)，涵盖随附的全部文字、图形与宣传物，而 label 仅指附着于容器本身的那张；§101.15(c)(3) 明确「labeling 中非 label 的任一物件」含外语表述时，所有应出现在 label 或 labeling 上的强制信息也须出现在该物件上。常见误解是把中文「标签」等同于瓶身贴纸，漏掉菜单、货架签、随附单张、广告。需特别注意，本条是 Part 101 标签法源层，与 Part 117 预防控制层不同：Part 117 的标签控制是管理义务，labeling 的宽范围则是本 part 的义务载体范围。
  tags:
  - labeling
  - 载体范围
  - 与Part117区分
  - v4.18
  - Part 101
  - 法规正文层

- id: t242
  title: serving / serving size
  type: term
  source_chapter: 21 CFR Part 101 § 101.9（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The term serving or serving size means an amount of food customarily consumed per eating occasion by persons 4 years of age or older which is expressed in a common household measure that is appropriate to the food. When the food is specially formulated or processed for use by infants or by toddlers, a serving or serving size means an amount of food customarily consumed per eating occasion by infants up to 12 months of age or by children 1 through 3 years of age, respectively."'
  summary: serving 或 serving size 指 4 岁及以上人群每次进食惯常消费的食品量，并以适合该食品的通用家用量具表达；专为婴儿或幼儿配方加工时分别按 12 个月以下婴儿、1 至 3 岁儿童的惯常消费量定义。除例外情形与仅通过减重计划销售的产品外，标签份量须由 §101.12(b) 的 RACC 推导。常见误解是把它当成厂商建议食用量或营养建议，实际它是监管比较基准，直接决定声称资格、Daily Value 与 disqualifying level 的计算分母。
  tags:
  - 份量
  - 比较基准
  - 营养标签
  - v4.18
  - Part 101
  - 法规正文层

- id: t243
  title: reference amounts customarily consumed (RACC)
  type: term
  source_chapter: 21 CFR Part 101 § 101.12（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The general principles and factors that the Food and Drug Administration (FDA) considered in arriving at the reference amounts customarily consumed per eating occasion (reference amounts) which are set forth in paragraph (b) of this section, are that: (1) FDA calculated the reference amounts for persons 4 years of age or older to reflect the amount of food customarily consumed per eating occasion by persons in this population group. These reference amounts are based on data set forth in appropriate national food consumption surveys."'
  summary: 参考量是 FDA 按产品类别钉死、列于 §101.12(b) 的每次进食惯常消费量，由全国食物消费调查数据的均值、中位数、众数及膳食指南、厂商用量等推导，4 岁以上与 4 岁以下分列，且只计可食部分、不含骨籽壳，并按主要预期用途确定。常见误解是把 RACC 当成工艺参数或危害分析输入，或把表内数值当成可直接引用的文本；它是 serving size、声称阈值与 disqualifying level 的共同分母，但本件表格为流式列值，具体数值须回原表核对。
  tags:
  - RACC
  - 比较基准
  - 声称资格
  - v4.18
  - Part 101
  - 法规正文层

- id: t244
  title: common household measure
  type: term
  source_chapter: 21 CFR Part 101 § 101.9（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"For labeling purposes, the term common household measure or common household unit means cup, tablespoon, teaspoon, piece, slice, fraction (e.g., 1⁄4 pizza), ounce (oz), fluid ounce (fl oz), or other common household equipment used to package food products (e.g., jar, tray). In expressing serving"'
  summary: 通用家用量具指杯、汤匙、茶匙、片、块、分数（如四分之一披萨）、盎司、液量盎司，或用于包装食品的常见家用容器（如罐、托盘）等，用于把 serving size 表达成消费者可理解的单位。常见误解是把它当成营销用语或可任取的公制换算；它是标签份量的法定表达形式，与克/毫升的公制声明并用，且除饮料外优先使用杯、匙。
  tags:
  - 份量表达
  - 家用量具
  - 营养标签
  - v4.18
  - Part 101
  - 法规正文层

- id: t245
  title: Daily Value (DV) / RDI / DRV
  type: term
  source_chapter: 21 CFR Part 101 § 101.9（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"For purposes of declaration of percent of Daily Value as provided for in paragraphs (d), (e), and (f) of this section, foods represented or purported to be specifically for infants through 12 months, children 1 through 3 years, pregnant women, and lactating women shall use the RDIs"'
  summary: Daily Value 是营养标签上 %DV 的比较基准，由维生素与矿物质的 Reference Daily Intake（RDI，§101.9(c)(8)(iv)）与宏量营养素及其他成分的 Daily Reference Value（DRV，§101.9(c)(9)）构成；特定人群（婴儿、1 至 3 岁、孕妇、乳母）须用为该人群设定的 RDI，其他食品用 4 岁以上成人儿童的 RDI。常见误解是把 %DV 当成该食品本身营养含量的百分比或个体化膳食建议，实际它是以 2,000 卡路里膳食为基准的法规参照值，且 RDI/DRV 数值随人群与快照日期不同，不可混算。
  tags:
  - DailyValue
  - RDI
  - DRV
  - v4.18
  - Part 101
  - 法规正文层

- id: t246
  title: simplified format
  type: term
  source_chapter: 21 CFR Part 101 § 101.9（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The declaration of nutrition information may be presented in the simplified format set forth herein when a food product contains insignificant amounts of eight or more of the following: Calories, total fat, saturated fat, trans fat, cholesterol, sodium, total carbohydrate, dietary fiber, total sugars, added sugars, protein,"'
  summary: 简化格式是当食品含八种（婴儿及 1 至 3 岁食品为六种）以上指定营养素达到「不显著量」时允许采用的 Nutrition Facts 呈现方式，仍须列出总热量、总脂肪、总碳水、蛋白质与钠，以及超过不显著量的其他营养素和需强化添加时的维生素矿物质；「不显著量」指可申报为零（总碳水、膳食纤维、蛋白质为可申报低于 1 克）的量。常见误解是把它当成小包装免标或随意删减营养素的通道，实际它只是格式简化，一旦在 label 或 labeling 上作任何营养声称即不得使用。
  tags:
  - 简化格式
  - 营养标签
  - 小包装
  - v4.18
  - Part 101
  - 法规正文层

- id: t247
  title: small business exemption (low-volume product)
  type: term
  source_chapter: 21 CFR Part 101 § 101.9（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"are the subject of a claim for an exemption that provides the information required under paragraph (j)(18)(iv) of this section, that is filed before the beginning of the time period for which the exemption is claimed, and that is filed by a person, whether it is the manufacturer, packer, or distributor, that qualifies to claim the exemption under the requirements for average full-time equivalent employees in paragraphs (j)(18)(i) or (j)(18)(ii) of this section; and whose labels, labeling, and advertising do not provide nutrition information or make a nutrient content or health claim."'
  summary: 小企业豁免是 §101.9(j)(18) 营养标签豁免清单的一项：低销量食品须在豁免期开始前提交载明规定信息的申报，由符合平均全职当量雇员门槛的制造商、包装商或经销商提出，且该产品标签、labeling 与广告均不得提供营养信息或作营养素含量/健康声称；门槛按首次进入州际商业的时间分档，其他产品按前 12 个月平均少于 100 名全职当量雇员且销量少于 10 万件判定。常见误解是把它当成主体资格豁免或可通用到配料表、警示声明；它只免 §101.9 营养标签，且举证责任在主张豁免者。
  tags:
  - 小企业豁免
  - 营养标签豁免
  - 举证
  - v4.18
  - Part 101
  - 法规正文层

- id: t248
  title: covered establishment
  type: term
  source_chapter: 21 CFR Part 101 § 101.11（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Covered establishment means a restaurant or similar retail food establishment that is a part of a chain with 20 or more locations doing business under the same name (regardless of the type of ownership, e.g., individual franchises) and offering for sale substantially the same menu items, as well as a restaurant or similar retail food establishment that is registered to be covered under paragraph (d) of this section."'
  summary: 受涵盖场所指属于同名经营 20 个及以上地点、供应实质相同菜单项的连锁餐馆或类似零售食品场所（无论个体加盟还是共同所有），以及依 (d) 款登记自愿纳入者；法定判据是 20 个地点、同名、菜单实质相同三要素。常见误解是把任何餐馆或单一门店都算进来，或与 Part 117 的 qualified facility 主体豁免混淆——后者免的是预防控制义务，本条确定的是 ACA §4205 菜单卡路里标签义务的适用主体。
  tags:
  - 菜单标签
  - 适用主体
  - ACA4205
  - v4.18
  - Part 101
  - 法规正文层

- id: t249
  title: standard menu item
  type: term
  source_chapter: 21 CFR Part 101 § 101.11（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Standard menu item means a restaurant-type food that is routinely included on a menu or menu board or routinely offered as a self-service food or food on display."'
  summary: 标准菜单项指常规列入菜单或菜单板、或常规作为自助食品或陈列食品供应的餐馆型食品；与之相对的 daily special（当日特供）、temporary menu item（每年出现少于 60 天）、custom order（按顾客要求偏离常规制作）、variable menu item（多口味列为单项）各有独立定义。常见误解是把所有上菜单的食物都当成标准菜单项，忽略「常规供应」这一判据以及组合餐、自助饮料的专门归类。
  tags:
  - 菜单标签
  - 标准菜单项
  - 定义
  - v4.18
  - Part 101
  - 法规正文层

- id: t250
  title: warning statement for unpasteurized juice
  type: term
  source_chapter: 21 CFR Part 101 § 101.17（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"(ii) Any beverage containing juice where neither the juice ingredient nor the beverage has been processed in the manner described in paragraph (g)(7) of this section, shall bear the following warning statement: WARNING: This product has not been pasteurized and, therefore, may contain harmful bacteria that can cause serious illness in children, the elderly, and persons with weakened immune systems."'
  summary: 对未经 (g)(7) 款所述足以防止、减少或消除病原的工艺处理的果汁，以及所含果汁与饮料本身均未如此处理的含汁饮料，法规要求带固定警示语：本产品未经巴氏杀菌，可能含有对儿童、老年人及免疫低下者致严重疾病的有害细菌；警示须显著置于信息面板或主展示面，WARNING 大写加粗并加框。常见误解是做了 5-log 工艺就自动免除所有标签义务，或以为警示语可替代 Part 120〔§120.24〕的 5-log 法定要求；实际是工艺义务、标签义务、检查取证三层并行。
  tags:
  - 强制警示
  - 未巴氏果汁
  - Part120接口
  - v4.18
  - Part 101
  - 法规正文层

- id: t251
  title: nutrient content claim
  type: term
  source_chapter: 21 CFR Part 101 § 101.13（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"A claim that expressly or implicitly characterizes the level of a nutrient of the type required to be in nutrition labeling under § 101.9 or under § 101.36 (that is, a nutrient content claim) may not be made on the label or in labeling of foods unless the claim is made in accordance with this regulation and with the applicable regulations in subpart D of this part or in part 105 or part 107 of this chapter."'
  summary: 营养素含量声称指明示或暗示表征 §101.9 或 §101.36 要求在营养标签中申报的某营养素水平的声称，除非符合本条通则与 Subpart D（或 part 105/107）的适用规定，不得出现在 label 或 labeling 上；营养标签本身按 §101.9/§101.36 出现在 Nutrition Facts 内的信息不算声称，但同样的信息移到标签别处即构成声称。常见误解是只有「低脂」「高钙」这类直白形容词才算，忽略暗示、相对声称与位置转换。
  tags:
  - 声称
  - 营养素含量
  - 授权闸门
  - v4.18
  - Part 101
  - 法规正文层

- id: t252
  title: expressed nutrient content claim
  type: term
  source_chapter: 21 CFR Part 101 § 101.13（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"An expressed nutrient content claim is any direct statement about the level (or range) of a nutrient in the food, e.g., “low sodium” or “contains 100 calories.”"'
  summary: 明示营养素含量声称是对食品中某营养素水平或范围的直接陈述，例如 low sodium 或 contains 100 calories；它与暗示声称共用同一套授权闸门，均须符合 §101.13 通则与 Subpart D 逐词定义。常见误解是认为只要数值真实即可随意表述，实际用词须落在法规已定义的术语及其不误导的合理拼写变体之内，且婴幼儿食品原则上禁用。
  tags:
  - 声称
  - 明示
  - SubpartD
  - v4.18
  - Part 101
  - 法规正文层

- id: t253
  title: implied nutrient content claim
  type: term
  source_chapter: 21 CFR Part 101 § 101.13（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"An implied nutrient content claim is any claim that: (i) Describes the food or an ingredient therein in a manner that suggests that a nutrient is absent or present in a certain amount (e.g., “high in oat bran”); or (ii) Suggests that a food, because of its nutrient content, may be useful in maintaining healthy dietary practices, where there is also implied or explicit information about the nutrition content of the food (e.g., “healthy”)."'
  summary: 暗示营养素含量声称指以某种方式描述食品或配料、使人联想到某营养素缺失或达到某含量（如 high in oat bran），或结合明示/暗示营养信息暗示该食品有助于维持健康膳食实践（如 healthy）的声称。常见误解是品牌名、符号、vignette、第三方引用不算声称；法规明确暗示与明示同等受管，且 §101.65 另列哪些关于产品性质的表述一般不构成暗示声称。
  tags:
  - 声称
  - 暗示
  - 品牌名
  - v4.18
  - Part 101
  - 法规正文层

- id: t254
  title: health claim
  type: term
  source_chapter: 21 CFR Part 101 § 101.14（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Health claim means any claim made on the label or in labeling of a food, including a dietary supplement, that expressly or by implication, including “third party” references, written statements (e.g., a brand name including a term such as “heart”), symbols (e.g., a heart symbol), or vignettes, characterizes the relationship of any substance to a disease or health-related condition. Implied health claims include those statements, symbols, vignettes, or other forms of communication that suggest, within the context in which they are presented, that a relationship exists between the"'
  summary: 健康声称指在食品（含膳食补充剂）的 label 或 labeling 上明示或暗示（含第三方文献引用、含 heart 之类字样的品牌名、心形符号、vignette）表征某物质与疾病或健康相关状况之间关系的声称；暗示健康声称还包括在呈现语境中令人联想到物质存在/水平与疾病关系的任何沟通形式。常见误解是把它与营养素含量声称互套授权，或以为有论文支持即可用；两者是两套独立授权体系，健康声称须另有 SSA 与不超 disqualifying level。
  tags:
  - 声称
  - 健康声称
  - 授权体系
  - v4.18
  - Part 101
  - 法规正文层

- id: t255
  title: disqualifying nutrient levels
  type: term
  source_chapter: 21 CFR Part 101 § 101.14（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Disqualifying nutrient levels means the levels of total fat, saturated fat, cholesterol, or sodium in a food above which the food will be disqualified from making a health claim. These levels are 13.0"'
  summary: 丧失资格营养素水平指食品中总脂肪、饱和脂肪、胆固醇或钠超过该阈值时，该食品即被取消作健康声称的资格；阈值按每 RACC、每标签份量，以及对 RACC 为 30 克或 2 汤匙以下的食品按每 50 克表述。常见误解是只核对正面授权条件而忽略这道负面门槛，或把阈值当成单一固定数值；它是「先过负面门槛」的资格筛，与正面 SSA 授权并存。
  tags:
  - 声称
  - 负面门槛
  - 阈值
  - v4.18
  - Part 101
  - 法规正文层

- id: t256
  title: significant scientific agreement (SSA)
  type: term
  source_chapter: 21 CFR Part 101 § 101.14（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Validity requirement. FDA will promulgate regulations authorizing a health claim only when it determines, based on the totality of publicly available scientific evidence (including evidence from well-designed studies conducted in a manner which is consistent with generally recognized scientific procedures and principles), that there is significant scientific agreement, among experts qualified by scientific training and experience to evaluate such claims, that the claim is supported by such evidence."'
  summary: 显著科学一致是 FDA 授权健康声称的有效性前提：FDA 须基于全部公开可得科学证据（含按公认科学程序实施的精心设计研究）判定，在具备科学训练与经验评估此类声称的合格专家之间存在该声称受证据支持的显著一致。常见误解是把它等同于「有论文支持」或企业自证；它是法规级证据门槛，只有经 §101.70 请愿并由 FDA 在 Subpart E 立规授权后方可使用。
  tags:
  - 声称
  - SSA
  - 证据门槛
  - v4.18
  - Part 101
  - 法规正文层

- id: t257
  title: chemical preservative
  type: term
  source_chapter: 21 CFR Part 101 § 101.22（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The term chemical preservative means any chemical that, when added to food, tends to prevent or retard deterioration thereof, but does not include common salt, sugars, vinegars, spices, or oils extracted from spices, substances added to food by direct exposure thereof to wood smoke, or chemicals applied for their insecticidal or herbicidal properties."'
  summary: 化学防腐剂指加入食品后倾向于防止或延缓其变质的任何化学物质，但不包括食盐、糖、醋、香辛料、香辛料提取油、经木材烟熏直接加入的物质，以及为杀虫除草目的施用的化学品；§101.22 要求含此类成分的食品即便非包装形式也须 labeling，且声明须置于食品、容器或包装上使其可能被普通人在惯常购买使用条件下读到。常见误解是把所有「防腐」成分都算进去，或忽略可统称与须具体名的区分。
  tags:
  - 配料
  - 化学防腐剂
  - SubpartB
  - v4.18
  - Part 101
  - 法规正文层

- id: t258
  title: spice
  type: term
  source_chapter: 21 CFR Part 101 § 101.22（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The term spice means any aromatic vegetable substance in the whole, broken, or ground form, except for those substances which have been traditionally regarded as foods, such as onions, garlic and celery; whose significant function in food is seasoning rather than nutritional; that is true to name; and from which no portion of any volatile oil or other flavoring principle has been removed."'
  summary: 香辛料指整粒、破碎或磨碎形态的芳香植物性物质，其显著功能在食品中是调味而非营养，且真实符合其名称、未去除任何挥发油或其他风味成分；洋葱、大蒜、芹菜等传统视为食品者除外，辣椒红、姜黄、藏红花等兼作色素者须标为 spice and coloring 除非用通用名。常见误解是把任何植物性调味料都叫 spice，忽略「调味而非营养」「未抽提风味成分」等法定判据。
  tags:
  - 配料
  - 香辛料
  - SubpartB
  - v4.18
  - Part 101
  - 法规正文层

- id: t259
  title: percent juice declaration
  type: term
  source_chapter: 21 CFR Part 101 § 101.30（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"If the beverage contains fruit or vegetable juice, the percentage shall be declared by the words “Contains __ percent (or %) ______ juice” or “__ percent (or %) juice,” or a similar phrase, with the first blank filled in with the percentage expressed as a whole number not greater than the actual percentage of the juice and the second blank (if used) filled in with the name of the particular fruit or vegetable (e.g., “Contains 50 percent apple juice” or “50 percent juice”)."'
  summary: 百分比声明是 §101.30 对自称含果蔬汁饮料强制的标签声明：触发面很宽，只要广告、标签或 labeling 出现果蔬汁名称或变体、作直接或间接表述，或带果蔬图案/vignette，或凭色素与风味呈现含汁外观与口味，即须申报，碳酸与否、浓缩与否、稀释与否、甚至实际不含汁都在范围内。措辞须为 Contains __ percent __ juice 或 __ percent juice 一类，百分比以不超过实际含量的整数填报，低于 1% 时须写 less than 1 percent juice，100% 果汁另按 (b)(3) 处理。常见误解是只有真含果汁才需声明、或可用模糊的「果汁饮料」回避百分比。
  tags:
  - 果汁
  - 百分比声明
  - 触发条件
  - v4.18
  - Part 101
  - 法规正文层

- id: t260
  title: incidental additive
  type: term
  source_chapter: 21 CFR Part 101 § 101.100（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Incidental additives that are present in a food at insignificant levels and do not have any technical or functional effect in that food. For the purposes of this paragraph (a)(3), incidental additives are: (i) Substances that have no technical or functional effect but are present in a food by reason of having been incorporated into the food as an ingredient of another food, in which the substance did have a functional or technical effect."'
  summary: 附带添加剂指以不显著量存在、且在该食品中无任何技术或功能效果的添加剂，可依 §101.100(a)(3) 免于配料表申报，具体含因作为另一食品配料带入者、加工助剂（加工中加入但包装前移除、转化为食品固有成分、或以不显著量残留且无功能效果者），以及从设备或包装迁移且非 §201(s) 食品添加剂或合规使用者。常见误解是把「免申报」理解成凡痕量即自动免，或以为亚硫酸盐也照此办理；亚硫酸盐另按 (a)(4) 的 10 ppm 可检出阈值单独判定。
  tags:
  - 豁免
  - 附带添加剂
  - 配料表
  - v4.18
  - Part 101
  - 法规正文层

- id: t261
  title: sulfiting agent
  type: term
  source_chapter: 21 CFR Part 101 § 101.100（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"For the purposes of paragraph (a)(3) of this section, any sulfiting agent (sulfur dioxide, sodium sulfite, sodium bisulfite, potassium bisulfite, sodium metabisulfite, and potassium metabisulfite) that has been added to any food or to any ingredient in any food and that has no technical effect in that food will be considered to be present in an insignificant amount only if no detectable amount of the agent is present in the finished food. A detectable amount of sulfiting agent is 10 parts per million"'
  summary: 亚硫酸盐剂指二氧化硫及亚硫酸钠、亚硫酸氢钠、亚硫酸氢钾、偏亚硫酸钠、偏亚硫酸钾等，加入食品或配料且在该食品中无技术效果者，只有在成品中不存在可检出量时才视为不显著而免于配料表申报；可检出量界定为成品中亚硫酸盐 10 ppm（mg/kg）或以上，并以液相色谱串联质谱法或 AOAC 990.28 判定。常见误解是把它并入 incidental additive 的自动豁免，或忽略「可检出即须申报」这一反向判据。
  tags:
  - 豁免
  - 亚硫酸盐
  - 10ppm
  - v4.18
  - Part 101
  - 法规正文层

- id: t262
  title: exemption from ingredient declaration (403(i)(2))
  type: term
  source_chapter: 21 CFR Part 101 § 101.100（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The following foods are exempt from compliance with the requirements of section 403(i)(2) of the act (requiring a declaration on the label of the common or usual name of each ingredient when the food is fabricated from two or more ingredients)."'
  summary: §101.100(a) 明确其所列食品豁免的是 FD&C Act §403(i)(2) 的配料表要求（即以两种以上配料制成时须在标签上申报各配料通用或常用名），而非整个标签义务；列举项包括什锦组合装、零售散装容器明示情形、附带添加剂、亚硫酸盐剂等。常见误解是把本豁免当成可通用到营养标签、警示声明或声称规则的总豁免；§101.9(j) 免的是营养标签、§101.108 免的是经批准的临时实验，三者豁免对象互不可替代。需特别注意，本条是 Part 101 标签法源层，与 Part 117 预防控制层不同：Part 117 的 qualified facility 等属主体豁免，与标签义务豁免不是同一制度。
  tags:
  - 豁免
  - 配料表
  - 与Part117区分
  - v4.18
  - Part 101
  - 法规正文层

- id: t263
  title: gluten-free
  type: term
  source_chapter: 21 CFR Part 101 § 101.91（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Any unavoidable presence of gluten in the food bearing the claim in its labeling is below 20 ppm gluten (i.e., below 20 mg gluten per kg of food)."'
  summary: gluten-free 是定量阈值定义而非营销词：食品不得含含麸质谷物、未经去麸加工的其衍生物、或虽经去麸加工但使食品中麸质达 20 ppm 及以上的衍生物，或本就不含麸质，且任何不可避免的麸质存在须低于 20 ppm；no gluten、free of gluten、without gluten 同等适用，不符即 deem misbranded，含 wheat 声明还须加星号转注说明。常见误解是把它当成「无添加」或与过敏原-free 声明同源。需特别注意，本条是 Part 101 标签法源层，与 Part 117 预防控制层不同：FALCPA 法定过敏原定义及交叉接触管理在 Part 117/Ed.5 一侧，20 ppm 是本条自身的声称判据。
  tags:
  - 无麸质
  - 20ppm
  - 与Part117区分
  - v4.18
  - Part 101
  - 法规正文层

- id: t264
  title: gluten-containing grain / gluten
  type: term
  source_chapter: 21 CFR Part 101 § 101.91（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The term “gluten-containing grain” means any one of the following grains or their crossbred hybrids (e.g., triticale, which is a cross between wheat and rye): (i) Wheat, including any species belonging to the genus Triticum; (ii) Rye, including any species belonging to the genus Secale; or (iii) Barley, including any species belonging to the genus Hordeum. (2) The term “gluten” means the proteins that naturally occur in a gluten-containing grain and that may cause adverse health effects in persons with celiac disease (e.g., prolamins and glutelins)."'
  summary: 含麸质谷物指小麦（Triticum 属）、黑麦（Secale 属）、大麦（Hordeum 属）及其杂交种（如小黑麦）；麸质指天然存在于这些谷物中、可能对乳糜泻患者产生不良健康效应的蛋白质（如醇溶蛋白、谷蛋白）。常见误解是把燕麦或玉米等非列明谷物也算入，或把麸质理解成泛化的「面筋蛋白」；法定范围是封闭列举，直接决定 gluten-free 判定的前半段。
  tags:
  - 无麸质
  - 封闭列举
  - 定义
  - v4.18
  - Part 101
  - 法规正文层

- id: t265
  title: fresh
  type: term
  source_chapter: 21 CFR Part 101 § 101.95（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The term “fresh,” when used on the label or in labeling of a food in a manner that suggests or implies that the food is unprocessed, means that the food is in its raw state and has not been frozen or subjected to any form of thermal processing or any other form of preservation, except as provided in paragraph (c) of this section."'
  summary: fresh 用在暗示食品未加工、未保存的语境时，指食品处于生鲜状态、未经冷冻、未经任何形式热处理或其他保存（(c) 款例外除外）；用于巴氏杀菌全脂奶等不暗示未加工的场合不受 (a) 款约束，而用于含巴氏杀菌配料的意面酱则受约束；fresh frozen/frozen fresh 另指采收后仍新鲜时快速冻结。常见误解是把 fresh 当成可自由使用的感官修饰词或质量等级，忽略品牌名、感官修饰语同样受管以及「是否暗示未加工」这一触发判据。
  tags:
  - 描述性声称
  - fresh
  - 触发条件
  - v4.18
  - Part 101
  - 法规正文层

- id: t266
  title: disclaimer (dietary supplement statements)
  type: term
  source_chapter: 21 CFR Part 101 § 101.93（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Disclaimer. The requirements in this section apply to the label or labeling of dietary supplements where the dietary supplement bears a statement that is provided for by section 403(r)(6) of the Federal Food, Drug, and Cosmetic Act (the act), and the manufacturer, packer, or distributor wishes to take advantage of the exemption to section 201(g)(1)(C) of the act that is provided by compliance with section 403(r)(6) of the act."'
  summary: 膳食补充剂依 FD&C Act §403(r)(6) 作结构/功能声明以取得 §201(g)(1)(C) 免责时，须在上市后 30 天内向 FDA 通报、随附声明文本并署名证明真实不误导，且每条声明须带固定免责文字：本声明未经 FDA 评估，本产品不用于诊断、治疗、治愈或预防任何疾病。常见误解是把它与疾病健康声称混用，或以为加一句小字即可自由作疾病相关表述；免责不授权健康声称，且多条声明时各有或共用复数免责的排版规则。
  tags:
  - 免责声明
  - 膳食补充剂
  - 结构功能声明
  - v4.18
  - Part 101
  - 法规正文层

- id: t267
  title: petition (nutrient content claim)
  type: term
  source_chapter: 21 CFR Part 101 § 101.69（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"This section pertains to petitions for claims, expressed or implied, that: (1) Characterize the level of any nutrient which is of the type required to be in the label or labeling of food by section 403(q)(1) or (q)(2) of the Federal Food, Drug, and Cosmetic Act (the act); and (2) That are not exempted under section 403(r)(5)(A) through (r)(5)(C) of the act from the requirements for such claims in section 403(r)(2)."'
  summary: §101.69 规范营养素含量声称请愿，适用于表征 §403(q)(1)/(q)(2) 要求申报的营养素水平、且不属于 §403(r)(5)(A)–(C) 豁免的明示或暗示声称；类型含新（尚未授权）声称、与已定义术语一致的同义术语、以及在品牌名中使用暗示声称。常见误解是把请愿当成企业自我备案即可启用新词；它是变更法规授权清单的正式程序，须依 §403(r)(4) 提交并载明科学依据。
  tags:
  - 请愿
  - SubpartD
  - 变更程序
  - v4.18
  - Part 101
  - 法规正文层

- id: t268
  title: petition (health claim)
  type: term
  source_chapter: 21 CFR Part 101 § 101.70（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Any interested person may petition the Food and Drug Administration (FDA) to issue a regulation regarding a health claim. An original and one copy of the petition shall be submitted, or the petitioner may submit an original and a computer readable disk containing the petition. Contents of the disk should be in a standard format, such as ASCII format. (Petitioners interested in submitting a disk should contact the"'
  summary: 任何利害关系人可请愿 FDA 就健康声称制定法规，须提交原件及副本（或磁盘）、外文材料附英译、并载明通讯地址；请愿须含科学证据综述、物质在代表食品中含量的分析数据、模型健康声称等，非临床研究须说明 GLP 合规、人体研究须说明 IRB 与知情同意合规。常见误解是把请愿等同于自动授权或把数据递交当作可使用声称；授权须由 FDA 在 Subpart E 立规，且全部数据在立案通知后公开。
  tags:
  - 请愿
  - SubpartE
  - 变更程序
  - v4.18
  - Part 101
  - 法规正文层

- id: t269
  title: model health claim
  type: term
  source_chapter: 21 CFR Part 101 § 101.70（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"D. Model health claim. One or more model health claims that represent label statements that may be used on a food label or in labeling for a food to characterize the relationship between the substance in a food to a disease or health-related condition that is justified by the summary of scientific data provided in section C of the petition. The model health claim shall include:"'
  summary: 模型健康声称指请愿中提出、可在食品 label 或 labeling 上用于表征食品中物质与疾病或健康相关状况关系、并由请愿 C 节科学数据摘要所证成的一条或多条标签措辞；须含对摘要相关结论的简要概括，以及该物质如何帮助消费者达成与健康益处相关的总体膳食模式或目标的表述。常见误解是把它当成可自由改写的范文；Subpart E 各条（§101.72–83）给出的是已授权模型措辞与适用条件，用不在授权清单内的表述仍属未授权声称。
  tags:
  - 模型措辞
  - 健康声称
  - SubpartE
  - v4.18
  - Part 101
  - 法规正文层

- id: t270
  title: claims not authorized
  type: term
  source_chapter: 21 CFR Part 101 § 101.71（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Health claims not authorized for foods in conventional food form or for dietary supplements of vitamins, minerals, herbs, or other similar substances: (a) Dietary fiber and cardiovascular disease. (b) Zinc and immune function in the elderly."'
  summary: §101.71 以清单形式列明对常规食品形态食品及维生素、矿物质、草本或类似物质膳食补充剂不予授权的健康声称（如膳食纤维与心血管疾病、锌与老年人免疫功能），是「负面清单 + 正面授权」双闸中的负面侧。常见误解是把它当成穷尽列举或以为未列入即可使用；健康声称能否使用仍取决于 §101.14 的 SSA、disqualifying level 与 Subpart E 是否立规授权。
  tags:
  - 负面清单
  - 健康声称
  - SubpartE
  - v4.18
  - Part 101
  - 法规正文层

- id: t271
  title: nutrition labeling of dietary supplements (Supplement Facts)
  type: term
  source_chapter: 21 CFR Part 101 § 101.36（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"The label of a dietary supplement that is offered for sale shall bear nutrition labeling in accordance with this regulation unless an exemption is provided for the product in paragraph (h) of this section. (b) The declaration of nutrition information on the label and in labeling shall contain the following information, using the subheadings and the format specified in paragraph (e) of this section."'
  summary: 膳食补充剂须以 Supplement Facts 形式作营养标签（§101.36(h) 豁免除外），含 Serving Size、Servings Per Container 等子标题，份量依 §101.9(b) 与 §101.12(b) Table 2 并以片、胶囊、包、茶匙等适合形态的术语表达；有 RDI 或 DRV 的 (b)(2)-膳食成分按 §101.9(c) 申报。常见误解是把 §101.9 的 Nutrition Facts 格式直接套用到补充剂，或把 §101.13/§101.14 的声称规则与 §101.93 的结构功能声明免责混为一谈。
  tags:
  - 膳食补充剂
  - SupplementFacts
  - SubpartC
  - v4.18
  - Part 101
  - 法规正文层

- id: t272
  title: substantial compliance
  type: term
  source_chapter: 21 CFR Part 101 § 101.43（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"FDA will find that there is substantial compliance with the guidelines in § 101.45 if it finds based on paragraph (a) of this section that at least 60 percent of all stores that are evaluated are in compliance. (d)"'
  summary: 实质合规是 FDA 判断生鲜果蔬鱼自愿营养标签指南是否被零售商整体遵守的法规级判定：在依 §101.45 抽查的 2,000 家代表性门店中，若至少 60% 的受评门店符合（陈列至少 90% 的 §101.44 清单品种、内容与格式合规、数据取自附录 C/D），即认定存在实质合规，并分别对农产品与鱼评估。常见误解是把它当成单店达标或企业自我声明；它是市场层面的统计判定，判定不达标会触发 §101.42 的强制标签报告机制。
  tags:
  - 自愿标签
  - 实质合规
  - 统计判定
  - v4.18
  - Part 101
  - 法规正文层

- id: t273
  title: voluntary nutrition labeling guidelines
  type: term
  source_chapter: 21 CFR Part 101 § 101.45（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Nutrition labeling for raw fruits, vegetables, and fish listed in § 101.44 should be presented to the public in the following manner: (1) Nutrition labeling information should be displayed at the point of purchase by an appropriate means such as by a label affixed to the food or through labeling including shelf labels, signs, posters, brochures, notebooks, or leaflets that are readily available and in close proximity to the foods. The nutrition labeling information may also be supplemented by a video, live demonstration, or other media."'
  summary: §101.45 为 §101.44 所列 20 种最常消费生鲜果蔬鱼给出自愿营养标签指南：信息应在购买点以贴标、货架签、标牌、海报、手册、活页或就近可取的小册子等方式呈现，份量与营养素按 §101.9(b)/(c) 确定且以生鲜可食部为基准，数值应取 FDA 附录 C/D 数据以保证一致性。常见误解是把「自愿」理解为可随意给数值；它是带 90% 覆盖率与统一数据口径的规范，且 §101.42/43 配有实质合规评估。
  tags:
  - 自愿标签
  - 生鲜果蔬鱼
  - SubpartC
  - v4.18
  - Part 101
  - 法规正文层

- id: t274
  title: good source / high / more / high potency
  type: term
  source_chapter: 21 CFR Part 101 § 101.54（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"“High” claims. (1) The terms “high,” “rich in,” or “excellent source of” may be used on the label and in the labeling of foods, except meal products as defined in § 101.13(l) and main dish products as defined in § 101.13(m), provided that the food contains 20 percent or more of the RDI or the DRV per reference amount customarily consumed."'
  summary: §101.54 规定 good source、high、more、high potency 类声称：只有使用本节定义的术语、符合 §101.13 通则、且食品按 §101.9/§101.10/§101.36 贴标时方可作出，且以该营养素的 RDI（§101.9(c)(8)(iv)）或 DRV（§101.9(c)(9)，总碳水除外）为基准；high/rich in/excellent source of 须达每 RACC 的 RDI 或 DRV 20% 以上。常见误解是把 20% 当成 %DV 或份量占比，或忽略相对声称 more 需有适当参照食品。
  tags:
  - 逐词阈值
  - 营养素含量声称
  - SubpartD
  - v4.18
  - Part 101
  - 法规正文层

- id: t275
  title: light or lite
  type: term
  source_chapter: 21 CFR Part 101 § 101.56（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"General requirements. A claim using the term light or lite to describe a food may only be made on the label or in labeling of the food if: (1) The claim uses one of the terms defined in this section in accordance with the definition for that term; (2) The claim is made in accordance with the general requirements for nutrient content claims in § 101.13; and (3) The food is labeled in accordance with § 101.9 or § 101.10, where applicable."'
  summary: light 或 lite 声称只有在使用本节定义术语、符合 §101.13 通则、且食品按 §101.9/§101.10 贴标时方可作出；若食品 50% 以上热量来自脂肪，须相对适当参照食品按每 RACC 减脂 50% 以上，否则另按低热量/低脂等判据，并须说明参照对象。常见误解是把它当成颜色、口感或轻盈质地的描述词；在标签语境下它是受逐词阈值约束的营养素含量声称，且 meal/main dish 产品另有限制。
  tags:
  - 逐词阈值
  - light
  - SubpartD
  - v4.18
  - Part 101
  - 法规正文层

- id: t276
  title: food allergy avoidance / absence claims (not implied claims)
  type: term
  source_chapter: 21 CFR Part 101 § 101.65（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"A claim that a specific ingredient or food component is absent from a product, provided that the purpose of such claim is to facilitate avoidance of the substances because of food allergies (see § 105.62 of this chapter), food intolerance, religious beliefs, or dietary practices such as vegetarianism or other nonnutrition related reason, e.g., “100 percent milk free;”"'
  summary: §101.65 明确某些关于产品性质的表述一般不构成暗示营养素含量声称：为便于因食物过敏（见 §105.62）、食物不耐受、宗教信仰或素食等膳食实践而回避某物质，声称某配料或成分不存在（如 100 percent milk free），且未处于 §101.13(b)(2) 会使其成为暗示声称的语境时，不受 §101.13 与本条约束。常见误解是把任何「不含 X」都当成营养声称或当成过敏原合规声明。需特别注意，本条是 Part 101 标签法源层，与 Part 117 预防控制层不同：过敏原交叉接触的预防控制、标签控制义务在 Part 117/Ed.5 一侧，本条只界定该表述是否落入声称监管。
  tags:
  - 过敏原
  - 暗示声称
  - 与Part117区分
  - v4.18
  - Part 101
  - 法规正文层

- id: t277
  title: temporary exemptions for labeling experiments
  type: term
  source_chapter: 21 CFR Part 101 § 101.108（eCFR 2026-11-05 快照，法规正文层）
  source_quote: '"Any firm that intends to undertake a labeling experiment that requires exemptions from certain requirements of §§ 101.9 and 105.66 of this chapter should submit a written proposal containing a thorough discussion of each of the following information items that apply to the particular experiment:"'
  summary: 临时实验豁免指企业拟开展需豁免 §101.9 与 §105.66 部分要求的标签实验时，应事先向 FDA 提交书面提案，载明待测试格式、分类判据、店内材料草案、起止日期与分析报告提交承诺、地域、效果测量机制等，并在与 FDA 协作的受控条件下进行、不得未经批准超期。常见误解是把它当成企业可自行试行的排版试点；它是 FDA 书面提案获批下的临时豁免，与 §101.100 配料表豁免、§101.9(j) 营养标签豁免对象不同，不可互替。
  tags:
  - 豁免
  - 临时实验
  - SubpartG
  - v4.18
  - Part 101
  - 法规正文层


- id: t278
  title: direct food additive（直接食品添加剂）
  type: term
  source_chapter: 21 CFR Part 172 标题 / Authority
  source_quote: '"Food Additives Permitted for Direct Addition to Food for Human Consumption"

    '
  summary: 直接加入食品、在成品中保留技术效果的添加剂，许可与限量由 Part 172 管；法源为 FD&C Act §201(s) 定义与 §409。与间接添加剂（包装材料迁移，Part 175–178）不同、与本包未收的 GRAS/临时许可不同。常见误读是把「直接添加剂」当成「可食用配料」或把间接添加剂混进来判定。
  tags:
  - 总则
  - 许可四元组
  - 效力层
  - v4.19
  - Part 172
  - 法规正文层
- id: t279
  title: good manufacturing practice（本部分的口径）
  type: term
  source_chapter: § 172.5(a)
  source_quote: '"Regulations prescribing conditions under which food additive substances may be safely used predicate usage under conditions of good manufacturing practice."

    '
  summary: 本部分的 cGMP 不是泛泛口号，§172.5(a) 把它定义为两条具体限制：用量不超过合理需要量、物质须为食品级。它叠加在每一条 §172.xxx 之上，即使条款给了 ppm 上限也仍然生效。常见误读是把 GMP 当「建议层」，以为无法律约束力。
  tags:
  - 总则
  - GMP
  - 兜底限制
  - v4.19
  - Part 172
  - 法规正文层
- id: t280
  title: amount reasonably required（合理需要量）
  type: term
  source_chapter: § 172.5(a)(1)
  source_quote: '"The quantity of the substance added to food does not exceed the amount reasonably required to accomplish its intended physical, nutritive, or other technical effect in food."

    '
  summary: 无 ppm 上限的条款由这条兜底：用量不得超过实现预期物理、营养或其他技术效果所合理需要的量。它是一条实质限制，主张者须能论证技术效果需要多少。常见误读是「没有数字＝不限量」。
  tags:
  - 总则
  - GMP
  - 用量判据
  - v4.19
  - Part 172
  - 法规正文层
- id: t281
  title: food grade（食品级）
  type: term
  source_chapter: § 172.5(a)(2)
  source_quote: '"Any substance intended for use in or on food is of appropriate food grade and is prepared and handled as a food ingredient."

    '
  summary: 用于食品的物质须为适当食品级，并作为食品配料制备与处理。工业级或非食品级原料即使化学上等同也不合规。常见误读是只看纯度数值、不问是否按食品配料管理。
  tags:
  - 总则
  - GMP
  - 纯度
  - v4.19
  - Part 172
  - 法规正文层
- id: t282
  title: existence of a regulation（许可法规的效力边界）
  type: term
  source_chapter: § 172.5(b)
  source_quote: '"The existence of a regulation prescribing safe conditions of use for a food additive shall not be construed to relieve the use of the substance from compliance with any other provision of the Act."

    '
  summary: 存在许可法规不得被解释为免除该物质受本法其他任何条款约束的义务。Part 172 只管许可与限量/规格层，标签归〔§ 101〕、过程控制归〔§ 117〕。常见误读是把「有 Part 172 条款」当成整体合规的免死金牌。
  tags:
  - 总则
  - 效力层
  - 不得混引
  - v4.19
  - Part 172
  - 法规正文层
- id: t283
  title: nutrient substance approval（营养物质许可 ≠ 有用性认定）
  type: term
  source_chapter: § 172.5(c)
  source_quote: '"The existence of any regulation prescribing safe conditions of use for a nutrient substance does not constitute a finding that the substance is useful or required as a supplement to the diet of humans."

    '
  summary: 营养物质获许可只解决安全性，不构成其「对人类膳食有用或必需」的认定。据此做营养声称或膳食必要性主张属越界。常见误读是把「FDA 批准该营养素」当声称依据。
  tags:
  - 总则
  - 效力层
  - 营养声称
  - v4.19
  - Part 172
  - 法规正文层
- id: t284
  title: antioxidant（抗氧化剂功能）
  type: term
  source_chapter: § 172.110(b)
  source_quote: '"The BHA is used alone or in combination with BHT, as an antioxidant in foods, as follows:"

    '
  summary: 抗氧化剂是本部分 Subpart B 的主功能之一，BHA 与 BHT 由同一表列头 total BHA and BHT 管、须合并计算。功能本身也是许可要件的一部分（超功能使用不获许可）。常见误读是把抗氧化剂与防腐剂混为一类从而套错限值表。
  tags:
  - SubpartB
  - 抗氧化剂
  - 合并限量
  - v4.19
  - Part 172
  - 法规正文层
- id: t285
  title: in combination（合并限量）
  type: term
  source_chapter: § 172.120(b)(2)
  source_quote: '"With disodium EDTA (disodium ethylenediaminetetraacetate) in the following foods at not to exceed, in combination, the levels prescribed, calculated as anhydrous C10H12O8N2CaNa2:"

    '
  summary: 「in combination」指两种或多种物质合用时的限量按合并值计，不得各自擦线合格。钙二钠 EDTA 与二钠 EDTA 即属此例。常见误读是各物质按各自表值独立计算。
  tags:
  - SubpartB
  - 合并限量
  - 计量基准
  - v4.19
  - Part 172
  - 法规正文层
- id: t286
  title: parts per million calculated as（计量基准）
  type: term
  source_chapter: § 172.180
  source_quote: '"in an amount not to exceed 20 parts per million calculated as tin (Sn)"

    '
  summary: 限值常附「以某元素计」（calculated as X）的换算基准，如以 Sn 计、以 Br 计、以无水物计。换算基准错了限值就错了。常见误读是按化合物整体质量而非指定元素/形态计算。
  tags:
  - 限值
  - 计量基准
  - 判读
  - v4.19
  - Part 172
  - 法规正文层
- id: t287
  title: as measured in the loin muscle（法定取样部位）
  type: term
  source_chapter: § 172.177(b)
  source_quote: '"as measured in the loin muscle"

    '
  summary: 取样部位本身可以是法规要件。烟熏鲢条款要求盐与亚硝酸盐均在 loin muscle 测定；换部位测出的数据不满足法定判据。常见误读是把限值当成对成品整体的平均值要求。
  tags:
  - SubpartB
  - 工艺参数
  - 取样判据
  - v4.19
  - Part 172
  - 法规正文层
- id: t288
  title: water phase portion（水相盐分）
  type: term
  source_chapter: § 172.177(b)
  source_quote: '"The brining procedure is controlled in such a manner that the water phase portion of the edible portion of the finished smoked product has a salt (NaCl) content of not less than 3.5 percent, as measured in the loin muscle"

    '
  summary: 盐分判据按「可食部的水相部分」计，且为下限（≥3.5%），与通常只给上限的限量方向相反。常见误读是按整鱼重量算盐分或只查上限。
  tags:
  - SubpartB
  - 工艺参数
  - 下限判据
  - v4.19
  - Part 172
  - 法规正文层
- id: t289
  title: treated malt use-locked labeling statement（用途锁定声明）
  type: term
  source_chapter: § 172.730(c)
  source_quote: '"the label or labeling of the treated malt shall bear, in addition to other information required by the Act, the statement, “Brewer''s Malt—To be used in the production of fermented malt beverages only”, or “Distiller''s Malt—To be used in the production of distilled spirits only”, whichever is the case."

    '
  summary: 用途限制通过处理物标签上的逐字法定措辞执行，自拟措辞不产生同样效果。同款结构亦见〔§172.725〕对赤霉酸/赤霉酸钾处理的麦芽。常见误读是以为意思相同即可。
  tags:
  - SubpartB
  - 标签义务
  - 用途锁定
  - v4.19
  - Part 172
  - 法规正文层
- id: t290
  title: bromate (calculated as Br)（以 Br 计的溴酸盐限值）
  type: term
  source_chapter: § 172.730(a)(1)
  source_quote: '"does not exceed 75 parts per million of bromate (calculated as Br)"

    '
  summary: 溴酸钾在麦芽中的限值为 ≤75 ppm 溴酸盐、以 Br 计，属「限值算在中间品」。常见误读是误算在成品饮料上，或按溴酸钾分子量而非 Br 计。
  tags:
  - SubpartB
  - 限值
  - 中间品
  - v4.19
  - Part 172
  - 法规正文层
- id: t291
  title: total residue of inorganic bromides（他源累计残留）
  type: term
  source_chapter: § 172.730(a)(2)
  source_quote: '"(2) The total residue of inorganic bromides in fermented malt beverages, resulting from the use of the treated malt plus additional residues of inorganic bromides that may be present from uses in accordance with other regulations in this chapter promulgated under sections 408 and/or 409 of the act, does not exceed 25 parts per million of bromide (calculated as Br)."

    '
  summary: 成品溴化物总残留须把「按本章其他法规使用所产生的额外同类残留」一并计入（≤25 ppm，以 Br 计）——即跨法规累计。常见误读是只算自己添加剂的贡献。
  tags:
  - SubpartB
  - 限值
  - 累计残留
  - v4.19
  - Part 172
  - 法规正文层
- id: t292
  title: carrier（载体）与浓度披露
  type: term
  source_chapter: § 172.110(c)(2)
  source_quote: '"When the additive is marketed in a suitable carrier, in addition to meeting the requirement of paragraph (c)(1) of this section, the label shall declare the percentage of the additive in the mixture."

    '
  summary: 以合适载体形式售卖的添加剂，标签除名称外还须申报添加剂在混合物中的百分比。常见误读是只标混合物商品名，不披露有效成分浓度。
  tags:
  - SubpartB
  - 标签义务
  - 复配物
  - v4.19
  - Part 172
  - 法规正文层
- id: t293
  title: intermediate mix（中间混合料）
  type: term
  source_chapter: § 172.804(d)(1)
  source_quote: '"The principal display panel of any intermediate mix of the additive for manufacturing purposes shall bear a statement of the concentration of the additive contained therein;"

    '
  summary: 面向生产的中间混合料须在主展示面标明添加剂浓度，以便下游正确配料。常见误读是把中间混合料当半成品、不做浓度披露。
  tags:
  - SubpartI
  - 标签义务
  - 复配物
  - v4.19
  - Part 172
  - 法规正文层
- id: t294
  title: adequate directions for use（足够使用说明）
  type: term
  source_chapter: § 172.120(c)(2)
  source_quote: '"The label or labeling of the additive container shall bear adequate use directions to provide a final food product that complies with the limitations provided in paragraph (b) of this section."

    '
  summary: 「足够使用说明」是法定的间接管控手段：通过容器标签指导下游，使成品不超限。常见误读是以为限值只靠终端检测，忽略说明书义务。
  tags:
  - 标签义务
  - 使用说明
  - 间接管控
  - v4.19
  - Part 172
  - 法规正文层
- id: t295
  title: To assure safe use（标签义务段）
  type: term
  source_chapter: § 172.730(b) 对照 § 172.110(c) 等
  source_quote: '"(b) To assure safe use of the additive, the label or labeling of the food additive shall bear, in addition to the other information required by the Act, the following:"

    '
  summary: 「To assure safe use」段是条款内的标签义务块，实测仅约 25% 条款带此段。有该段时必须落实（通常要求标添加剂名称与足够使用说明，如本处以 name of the additive 与 adequate directions for use 收口）；无该段时不得凭空补造。常见误读是默认条条都有标签义务。
  tags:
  - 标签义务
  - 条款语法
  - 判读
  - v4.19
  - Part 172
  - 法规正文层
- id: t296
  title: identity / specifications / conditions of use（三段式条款语法）
  type: term
  source_chapter: § 172.785
  source_quote: '"The additive may be safely used as an antimicrobial agent specific for Listeria monocytogenes (L. monocytogenes) in accordance with the following conditions:"

    '
  summary: 条款常按 (a) Identity → (b) Specifications → (c) Conditions of use 三段展开：身份要件、纯度/效价规格、使用条件。判读时逐段核对，任一段不满足即不合规。常见误读是只看用量一段。
  tags:
  - 条款语法
  - 判读
  - 生物类
  - v4.19
  - Part 172
  - 法规正文层
- id: t297
  title: incorporated by reference (IBR)
  type: term
  source_chapter: § 172.185(b) / § 172.785(b)(1)
  source_quote: '"The analytical method for determining the potency of the additive entitled “Determination of Potency of LMP-102TM,” dated October 9, 2003, and printed by Intralytix, Inc., is incorporated by reference."

    '
  summary: IBR 指把外部文件（FCC 页码、厂商方法、菌株资料）并入法规，法律效力等同正文，但内容不在本件、不在本技能包内。只可引「须符合某文件某版某页」，绝不转述其内部数值。常见误读是凭记忆写出被引文件的数值。
  tags:
  - 效力层
  - IBR
  - 不可转述
  - v4.19
  - Part 172
  - 法规正文层
- id: t298
  title: Food Chemicals Codex (FCC)
  type: term
  source_chapter: § 172.831(b)
  source_quote: '"The additive meets the specifications of the Food Chemicals Codex, 7th ed. (2010), pp. 993-995, which is incorporated by reference."

    '
  summary: FCC 是 Part 172 最常被 IBR 引用的纯度规格来源，引用须写清版次与页码（FCC 7th ed.＝2010、9th ed.＝2014）。版本/页码张冠李戴即引用错误。常见误读是把 FCC 当法规正文直接引其数值。
  tags:
  - 效力层
  - IBR
  - 纯度规格
  - v4.19
  - Part 172
  - 法规正文层
- id: t299
  title: specifications（纯度规格直写）
  type: term
  source_chapter: § 172.110(a)
  source_quote: '"Assay (total BHA), 98.5 percent minimum. Melting point 48 °C minimum."

    '
  summary: 部分条款把规格数值直接写在条文里（可核对），与整体 IBR 的条款并存于同一 Subpart。判定先问：这条给的是可读数值还是外转引用。常见误读是假设「有规格＝有可读数值」。
  tags:
  - 纯度规格
  - 判读
  - SubpartB
  - v4.19
  - Part 172
  - 法规正文层
- id: t300
  title: Use / Function 栏（功能限制）
  type: term
  source_chapter: § 172.120(b)(1)
  source_quote: '"(1) Alone, in the following foods at not to exceed the levels prescribed, calculated as the anhydrous compound:"

    '
  summary: 限值表常带 Use/Function 栏，把物质的使用绑定到特定功能（如 retard struvite formation、promote color retention）。超功能使用不在许可内。常见误读是只核对 ppm、忽略功能要件；表内 Use 栏文字属表区，须回原 PDF 核对。
  tags:
  - 限值表
  - 功能限制
  - 判读
  - v4.19
  - Part 172
  - 法规正文层
- id: t301
  title: specified foods（指定食品，封闭清单）
  type: term
  source_chapter: § 172.110
  source_quote: '"The food additive BHA (butylated hydroxyanisole) alone or in combination with other antioxidants permitted in food for human consumption in this subpart B may be safely used in or on specified foods, as follows:"

    '
  summary: 「specified foods」是封闭清单，须逐项对照；未列举的食品即不在许可内。常见误读是把列举当作举例、允许类推到「相近」食品。
  tags:
  - 许可四元组
  - 封闭清单
  - 判读
  - v4.19
  - Part 172
  - 法规正文层
- id: t302
  title: except in meat and poultry（肉禽除外）
  type: term
  source_chapter: § 172.829(c) / § 172.800
  source_quote: '"(c) The food additive neotame may be safely used as a sweetening agent and flavor enhancer in foods generally, except in meat and poultry, in accordance with current good manufacturing practice, in an amount not to exceed that reasonably required to accomplish the intended technical effect, in foods for which standards of identity established under section 401 of the Federal Food, Drug, and Cosmetic Act do not preclude such use."

    '
  summary: 「食品一般、肉禽除外」是通用甜味剂类条款的常见范围句式。肉禽制品属 USDA/FSIS 管辖，另成体系，不得搬用 Part 172 许可。常见误读是见「foods generally」就认为无类别限制。
  tags:
  - 许可四元组
  - 食品类别
  - 管辖分工
  - v4.19
  - Part 172
  - 法规正文层
- id: t303
  title: standards of identity do not preclude such use（标准身份不排除）
  type: term
  source_chapter: § 172.829(c)
  source_quote: '"in foods for which standards of identity established under section 401 of the Federal Food, Drug, and Cosmetic Act do not preclude such use"

    '
  summary: 即使有添加剂许可，若某标准化食品（section 401 标准身份）排除该用途，则仍不得使用。判定顺序是先过标准身份闸门、再过用量。常见误读是认为 FDA 许可优先于标准身份。
  tags:
  - 许可四元组
  - 标准身份
  - 判读
  - v4.19
  - Part 172
  - 法规正文层
- id: t304
  title: special dietary use（特殊膳食，part 105）
  type: term
  source_chapter: § 172.829(e)
  source_quote: '"(e) If the food containing the additive purports to be or is represented to be for special dietary use, it shall be labeled in compliance with part 105 of this chapter."

    '
  summary: 条款内部指向 part 105 的特殊膳食标签义务：食品若宣称或表示为特殊膳食用途，须符合 part 105。这是跨部分义务，不因符合 Part 172 用量而免除。常见误读是把该指引当可有可无的提示。
  tags:
  - 标签义务
  - 跨部分指引
  - SubpartI
  - v4.19
  - Part 172
  - 法规正文层
- id: t305
  title: antimicrobial agent（抗菌剂）
  type: term
  source_chapter: § 172.785
  source_quote: '"The additive may be safely used as an antimicrobial agent specific for Listeria monocytogenes (L. monocytogenes) in accordance with the following conditions:"

    '
  summary: 生物类抗菌剂（如李斯特菌噬菌体制剂）的许可对象是「针对特定致病菌的抗菌用途」，范围由靶菌与食品类别共同封闭。常见误读是当作广谱消毒剂或通用防腐剂使用。
  tags:
  - SubpartH
  - 抗菌剂
  - 生物类
  - v4.19
  - Part 172
  - 法规正文层
- id: t306
  title: bacteriophage（噬菌体）身份要件
  type: term
  source_chapter: § 172.785(a)(1)
  source_quote: '"The additive consists of a mixture of equal proportions of six different individually purified lytic-type (lacking lysogenic activity) bacteriophages (phages) specific against L. monocytogenes."

    '
  summary: 身份要件须逐条满足：6 种等比例、各自纯化、裂解型且无溶原活性、特异性针对 L. monocytogenes。常见误读是只看「含噬菌体」而不核数量、比例与溶原性。
  tags:
  - SubpartH
  - 身份要件
  - 生物类
  - v4.19
  - Part 172
  - 法规正文层
- id: t307
  title: ready-to-eat（9 CFR 430.1）
  type: term
  source_chapter: § 172.785(c)
  source_quote: '"(c) Conditions of use. The additive is used in accordance with current good manufacturing practice to control L. monocytogenes by direct application to meat and poultry products that comply with the ready-to-eat definition in 9 CFR 430.1."

    '
  summary: 适用范围边界外转到 9 CFR 430.1 的 ready-to-eat 定义：是否即食按该外部定义判定，不按「接近即食」的直觉。常见误读是以产品性质相近替代法定定义。
  tags:
  - SubpartH
  - 使用条件
  - 外部定义
  - v4.19
  - Part 172
  - 法规正文层
- id: t308
  title: potency / lytic result（效价与裂解结果）
  type: term
  source_chapter: § 172.785(b)(1)
  source_quote: '"The additive achieves a positive lytic result (OD600 ≤0.06) when tested against any of the following L. monocytogenes isolates available from American Type Culture Collection (ATCC): ATCC 35152 (serogroup 1/2a), ATCC 19118 (serogroup 4b), and ATCC 15313 (serogroup 1/2b)."

    '
  summary: 效价要件是「对指定 ATCC 菌株呈阳性裂解结果（OD600 ≤0.06）」，菌株编号与血清型是法定要件。测法多 IBR 外转。常见误读是只写「有抑菌效果」而不核指定菌株与阈值。
  tags:
  - SubpartH
  - 规格
  - 效力层
  - v4.19
  - Part 172
  - 法规正文层
- id: t309
  title: nutrient compensation（强制营养补偿）
  type: term
  source_chapter: § 172.867(d)
  source_quote: '"(d) To compensate for any interference with absorption of fat soluble vitamins, the following vitamins shall be added to foods containing olestra:"

    '
  summary: 脂肪替代物（Olestra）的许可以「强制补偿脂溶性维生素」为生效条件：须按规定量添加 A/D/E/K，否则不合规。常见误读是把补偿当推荐做法。
  tags:
  - SubpartI
  - 脂肪替代物
  - 强制条件
  - v4.19
  - Part 172
  - 法规正文层
- id: t310
  title: Dietarily insignificant（膳食上不显著）
  type: term
  source_chapter: § 172.867(e)(1)(iii)
  source_quote: '"an asterisk and statement, “Dietarily insignificant” shall appear prominently and conspicuously as specified in § 101.2(c) of this chapter;"

    '
  summary: Olestra 补偿添加的 A/D/E/K 须在配料表用星号标注，并在配料表后紧随星号与 Dietarily insignificant 声明，不得计入营养标签或营养声称。常见误读是把补偿维生素算作产品营养含量。
  tags:
  - SubpartI
  - 标签义务
  - 营养标签
  - v4.19
  - Part 172
  - 法规正文层
- id: t311
  title: natural flavoring substances（天然香料）
  type: term
  source_chapter: § 172.510
  source_quote: '"Natural flavoring substances and natural adjuvants may be safely used in food in accordance with the following conditions."

    '
  summary: 天然香料是名录型条款（Common name / Scientific name / Limitations 三列约千行），条首仅给「最小需要量 + GMP」通用条件，具体限制须逐行看 Limitations 列。名录内部行属不可逐字引用区。常见误读是把「在清单里」当「无限制」。
  tags:
  - SubpartF
  - 名录型条款
  - 导航
  - v4.19
  - Part 172
  - 法规正文层
- id: t312
  title: synthetic flavoring substances and adjuvants（合成香料与助剂）
  type: term
  source_chapter: § 172.515
  source_quote: '"Synthetic flavoring substances and adjuvants may be safely used in food in accordance with the following conditions."

    '
  summary: 合成香料清单（约 30 页、上千条物质名）为纯名录，不含用量限制列，只解决「是否被许可」。用量回到条首的「最小需要量 + GMP」。常见误读是去名录里找 ppm。
  tags:
  - SubpartF
  - 名录型条款
  - 导航
  - v4.19
  - Part 172
  - 法规正文层
- id: t313
  title: Do.（同上 / ditto）
  type: term
  source_chapter: § 172.510(b) 名录行示例
  source_quote: '"Arnica flowers Arnica montana L., A. fulgens Pursh, A. sororia Greene, or Do."

    '
  summary: Do. 是英文编纂惯用的「同上」，表示复制上一行同列的内容，绝非「无限制」。整列 Do. 还提示可能跨页续表被重置，须回原 PDF 逐格核对。示例行取自名录（名录内行属不可逐字引用区，此处仅引 Do. 语义）。常见误读是把 Do. 读成空白或免除。
  tags:
  - 限值表
  - 判读
  - 转换局限
  - v4.19
  - Part 172
  - 法规正文层
- id: t314
  title: multipurpose additive（多用途添加剂）
  type: term
  source_chapter: Subpart I
  source_quote: '"Subpart I — Multipurpose Additives"

    '
  summary: Subpart I 收录可按多种功能使用的添加剂（甜味剂、脂肪替代物、改性淀粉、乳化剂等），多为「食品一般 + cGMP」型或表格式限量。与前面按功能单列的子部分结构不同。常见误读是把它当作「无功能限制」。
  tags:
  - SubpartI
  - 结构
  - 导航
  - v4.19
  - Part 172
  - 法规正文层
- id: t315
  title: residual limitation（成品残留限值）
  type: term
  source_chapter: § 172.892
  source_quote: '"The quantity of any substance employed to effect such modification shall not exceed the amount reasonably required to accomplish the intended physical or technical effect, nor exceed any limitation prescribed."

    '
  summary: 改性淀粉类条款把「合理需要量」与「任何规定限值」并列，并常另设成品残留限值（如残锰、残磷）。限值可能落在处理剂、也可能落在成品残留。常见误读是只查处理剂用量、漏查成品残留。
  tags:
  - SubpartI
  - 限值
  - 残留
  - v4.19
  - Part 172
  - 法规正文层
- id: t316
  title: food starch-modified（法定品名）
  type: term
  source_chapter: § 172.892
  source_quote: '"the label of the food additive container shall bear the name of the additive “food starch-modified” in addition to other information required by the Act."

    '
  summary: 改性淀粉容器标签须逐字标示法定品名 food starch-modified。此类「法定品名」义务是条款自带义务的一种形态，与 To assure safe use 段不同。常见误读是自拟商品名代替法定品名。
  tags:
  - SubpartI
  - 标签义务
  - 法定品名
  - v4.19
  - Part 172
  - 法规正文层
- id: t317
  title: generally recognized as safe（条款内 GRAS 指引）
  type: term
  source_chapter: § 172.510(b)
  source_quote: '"used alone or in combination with flavoring substances and adjuvants generally recognized as safe in food, previously sanctioned for such use, or regulated in any section of this part."

    '
  summary: Part 172 条款内部会指向 GRAS、prior-sanctioned 或其他条款所管物质，形成「与获准物质组合使用」的许可路径。GRAS 本体（Part 182 等）不在本包内，只可引「属于 GRAS」这一事实，不复述其清单。常见误读是把 GRAS 当可在 Part 172 内自行认定。
  tags:
  - 效力层
  - 跨部分指引
  - 名录型条款
  - v4.19
  - Part 172
  - 法规正文层
- id: t318
  title: prior-sanctioned（既往认可）
  type: term
  source_chapter: § 172.515(b)
  source_quote: '"used alone or in combination with flavoring substances and adjuvants generally recognized as safe in food, prior-sanctioned for such use, or regulated by an appropriate section in this part."

    '
  summary: prior-sanctioned 指 1958 年添加剂修正案前已获 FDA/USDA 认可的物质，与 GRAS 并列为另一条合法性来源。其清单不在本包内，只可引「属于 prior-sanctioned」这一事实。常见误读是把 prior-sanctioned 与 GRAS 混为一条路径。
  tags:
  - 效力层
  - 跨部分指引
  - 名录型条款
  - v4.19
  - Part 172
  - 法规正文层
- id: t319
  title: food defense（食品防护）
  type: term
  source_chapter: § 121.3
  source_quote: '"food defense means, for purposes of this part, the effort to protect food from intentional acts of adulteration where there is an intent to cause wide scale public health harm."

    '
  summary: 本部分的法定口径是「防止蓄意掺假、且该掺假意图造成大规模公共卫生危害」的行动。构成要件含 intent 与 wide scale 两层；无此意图的掺杂（如为牟利掺假）不落入 Part 121，归 EMA（CAP-06）。常见误读是把 food defense 当成「厂区安保」或「防盗防破坏」的同义词。
  tags:
  - v4.20
  - Part 121
  - 法规正文层
  - 判读用语

- id: t320
  title: contaminant（本部分的污染物定义）
  type: term
  source_chapter: § 121.3
  source_quote: '"any biological, chemical, physical, or radiological agent that may be added to food to intentionally cause illness, injury, or death."

    '
  summary: 以「蓄意加入以造成疾病、伤害或死亡」为要件，且明列 radiological。与 Part 117 的危害口径相比，差别不在介质清单（两套都含放射性），而在「是否有蓄意与伤害意图」。常见误读是把本定义当成通用污染物定义去替换〔§ 117.3〕。
  tags:
  - v4.20
  - Part 121
  - 危害介质
  - 法规正文层

- id: t321
  title: significant vulnerability（显著脆弱性）
  type: term
  source_chapter: § 121.3
  source_quote: '"a vulnerability that, if exploited, could reasonably be expected to cause wide scale public health harm."

    '
  summary: 判据是「若被利用可合理预期造成大规模公共卫生危害」，由三要素评估：公共卫生影响（severity 与 scale）、物理接近程度、攻击者成功污染能力，且必须考虑内部人员。常见误读：只算单批后果不算波及范围（scale）；把「物理接近」简化成「有没有上锁」；或与〔§ 117.130〕的危害显著性混为一谈。
  tags:
  - v4.20
  - Part 121
  - 判定判据
  - 三要素

- id: t322
  title: actionable process step（APStep，可采取行动的过程步骤）
  type: term
  source_chapter: § 121.3
  source_quote: '"a point, step, or procedure in a food process where a significant vulnerability exists and at which mitigation strategies can be applied and are essential to significantly minimize or prevent the significant vulnerability."

    '
  summary: 三条件须同时成立：存在显著脆弱性、该点可施加缓解策略、且该策略对显著最小化不可或缺。常见误读是把关键工序或 CCP 直接等同于 APStep——CCP 针对无意引入的危害，APStep 针对蓄意行为，两者判定链与记录体系都不同。
  tags:
  - v4.20
  - Part 121
  - 判定判据

- id: t323
  title: mitigation strategies（缓解策略）
  type: term
  source_chapter: § 121.3
  source_quote: '"those risk-based, reasonably appropriate measures that a person knowledgeable about food defense would employ to significantly minimize or prevent significant vulnerabilities identified at actionable process steps"

    '
  summary: 指「懂食品防护的人在本部分科学认知下会采取的、基于风险的合理措施」。关键义务不是列出策略名，而是逐条书面解释其如何充分最小化该 APStep 的脆弱性（〔§ 121.135(a)〕），判定终点回指 §402 掺假。常见误读是把「加了门禁/装了监控」当作策略本身而不写充分性解释。
  tags:
  - v4.20
  - Part 121
  - 判定判据
  - 书面义务

- id: t324
  title: vulnerability assessment（脆弱性评估）
  type: term
  source_chapter: § 121.130(a)(c)
  source_quote: '"You must conduct or have conducted a vulnerability assessment for each type of food manufactured, processed, packed, or held at your facility"

    '
  summary: 按「每种食品」做，不是按车间或产线做；方法至少评估三要素并考虑内部人员。无论结论如何都必须书面，且须逐点说明「为何是/不是 APStep」（〔§ 121.130(c)〕 Regardless of the outcome）。常见误读是只解释「为什么它是 APStep」，对判 No 的点留空。
  tags:
  - v4.20
  - Part 121
  - 书面义务
  - 判定判据

- id: t325
  title: food defense plan（食品防护计划）
  type: term
  source_chapter: § 121.126
  source_quote: '"You must prepare, or have prepared, and implement a written food defense plan."

    '
  summary: 五要素封闭清单：书面脆弱性评估（含解释）、书面缓解策略（含解释）、监控书面程序、纠正措施书面程序、验证书面程序。计划本身是记录，须由 owner/operator/agent 在初次完成与每次修改时签名并注日期（〔§ 121.310〕）；与〔§ 117.126(b)〕的 FSP 七部件是两套清单，不可互套。
  tags:
  - v4.20
  - Part 121
  - 书面义务
  - 计划结构

- id: t326
  title: inside attacker（内部人员 / 内部攻击者）
  type: term
  source_chapter: § 121.130(b)
  source_quote: '"The assessment must consider the possibility of an inside attacker."

    '
  summary: 内部人员是脆弱性评估的强制考量项，不是加分项。常见误读有两种：只评估外来闯入者、忽略有权限接触产品的人员；或反过来把它读成「必须做背景调查/政审」——本部分只要求评估时考虑该可能性，不规定具体人事措施。
  tags:
  - v4.20
  - Part 121
  - 强制考量项

- id: t327
  title: qualified individual（Part 121 语境）
  type: term
  source_chapter: § 121.4 / § 121.3
  source_quote: '"A qualified individual may be, but is not required to be, an employee of the establishment."

    '
  summary: 四类活动（编制计划、脆弱性评估、识别与解释缓解策略、再分析）须由受标准化课程培训或等效岗位经验者执行；APStep 在岗人员另须受 food defense awareness 培训；监督责任须明确指派；培训记录须含日期、类型与受训人。常见误读是把「食品防护版 PCQI」直接等同于〔§ 117.180〕的 PCQI 培训体系。
  tags:
  - v4.20
  - Part 121
  - 人员资格
  - 记录

- id: t328
  title: U.S. owner or consignee（美国货主或收货人）
  type: term
  source_chapter: § 1.500
  source_quote: '"the person in the United States who, at the time of U.S. entry, either owns the food, has purchased the food, or has agreed in writing to purchase the food."

    '
  summary: 这是 FSVP 语境下 importer 的第一顺位人选：入境时在美国境内拥有、已购买或已书面同意购买该食品的人。只有不存在这样的主体时，才由境外货主指定的美国代理承担 importer 义务（须有签署同意书）。常见误读是把报关行、货代或境外出口商当成 importer。
  tags:
  - v4.21
  - subpart L
  - 法规正文层
  - 主体判定

- id: t329
  title: foreign supplier（境外供应商）
  type: term
  source_chapter: § 1.500
  source_quote: '"the establishment that manufactures/processes the food, raises the animal, or grows the food that is exported to the United States without further manufacturing/processing by another establishment, except for further manufacturing/processing that consists solely of the addition of labeling or any similar activity of a de minimis nature."

    '
  summary: 指最后制造/加工该食品、饲养动物或种植该食品并出口美国的实体。关键在例外句：**只加贴标签或类似轻微活动不构成「进一步加工」**，故该实体仍是 foreign supplier。常见误读是把品牌方、贸易商或再包装商当成供应商，从而错判验证对象。
  tags:
  - v4.21
  - subpart L
  - 法规正文层
  - 主体判定

- id: t330
  title: very small importer（极小进口商）
  type: term
  source_chapter: § 1.500 / § 1.512(b)(1)
  source_quote: '"With respect to the importation of human food, an importer (including any subsidiaries and affiliates) averaging less than $1 million per year, adjusted for inflation, during the 3-year period preceding the applicable calendar year, in sales of human food combined with the U.S. market value of human food imported, manufactured, processed, packed, or held without sale"

    '
  summary: 人类食品 <100 万美元/年、动物食品 <250 万美元/年（两套金额不可混用）；口径含子公司与关联企业、取 3 年均值、并把「未销售部分的美国市场价值」计入。符合者可走〔§ 1.512〕简化路径（书面保证每 2 年），但须每年 12 月 31 日前记录身份，证明记录存 3 年。
  tags:
  - v4.21
  - subpart L
  - 门槛
  - 简化路径

- id: t331
  title: receiving facility（接收设施）与 deemed compliance 的 except § 1.509
  type: term
  source_chapter: § 1.502(c) / § 1.500
  source_quote: '"You are deemed to be in compliance with the requirements of this subpart for a food you import, except for the requirements in § 1.509, if you are a receiving facility as defined in § 117.3 or § 507.3 of this chapter and you are in compliance with the following requirements of part 117 or part 507 of this chapter, as applicable"

    '
  summary: 既是接收设施、又符合〔§ 117.135〕/〔§ 117.136〕/Subpart G 之一者，视为已满足 FSVP 要求——**但排除〔§ 1.509〕**。即 UFI/DUNS 的每一 entry line 电子申报义务永远不豁免。这是全 subpart 最常被漏的一句，也是「我们是接收设施所以不用报 UFI」这类错误结论的来源。
  tags:
  - v4.21
  - subpart L
  - 法规正文层
  - 例外条款

- id: t332
  title: hazard requiring a control（需控制的危害，FSVP 口径）
  type: term
  source_chapter: § 1.500 / § 1.504
  source_quote: '"a known or reasonably foreseeable hazard for which a person knowledgeable about the safe manufacturing, processing, packing, or holding of food would, based on the outcome of a hazard analysis"

    '
  summary: FSVP 的危害分析结论单位。判定须按「不存在控制时的发生概率 + 发生后的严重性」评估（〔§ 1.504(c)(1)〕），且书面无论结论（〔§ 1.504(a)〕）。若无 hazards requiring a control，可免〔§ 1.505〕评估与〔§ 1.506〕验证，但**不免危害分析本身的书面义务**，且 covered produce 不适用该豁免。
  tags:
  - v4.21
  - subpart L
  - 判定判据

- id: t333
  title: serious hazard → 初次进口前 + 至少每年现场审核
  type: term
  source_chapter: § 1.506(d)(2)
  source_quote: '"there is a reasonable probability that exposure to the hazard will result in serious adverse health consequences or death to humans or animals, you must conduct or obtain documentation of an onsite audit of the foreign supplier before initially importing the food and at least annually thereafter"

    '
  summary: 两项要件同时成立才触发年度现场审核：① 危害**由境外供应商控制**；② 暴露后**可能造成严重健康后果或死亡**。要改为其他活动或降低频次，须做出并留存**书面判定**。常见误读是把「严重危害」等同于「显著危害」，或忽略「由供应商控制」这一前提。
  tags:
  - v4.21
  - subpart L
  - 验证活动
  - 硬时限

- id: t334
  title: written assurance（书面保证）三要素（FSVP）
  type: term
  source_chapter: § 1.507(b)
  source_quote: '"Any written assurances required under this section must contain the following: (1) Effective date; (2) Printed names and signatures of authorized officials; and (3) The assurance specified in the applicable paragraph."

    '
  summary: 〔§ 1.507〕五种免验证情形、〔§ 1.511(b)〕膳食补充剂、〔§ 1.512〕极小进口商路径都要用到的书面对价。三要素缺一即不成立：生效日期、授权官员印刷姓名与签名、以及该款所要求的保证内容。且出具方须**与保证一致行动并留记录**〔§ 1.507(c)〕——保证书不是纸面免责。
  tags:
  - v4.21
  - subpart L
  - 书面义务

- id: t335
  title: qualified auditor（合格审核人）
  type: term
  source_chapter: § 1.500 / § 1.503(b)
  source_quote: '"has technical expertise obtained through education, training, or experience (or a combination thereof) necessary to perform the auditing function"

    '
  summary: 做〔§ 1.506(e)(1)(i)〕或〔§ 1.511(c)(5)(i)(A)〕现场审核的人，须先是 qualified individual、另须具备审计职能所需技术专长。法定例举包括政府雇员（含外国政府）与依 subpart M 获认可的认证机构审核员。审核记录须包含「由合格审核人执行」的证明。
  tags:
  - v4.21
  - subpart L
  - 人员资格

- id: t336
  title: good compliance standing（良好合规状态，等效国家路径）
  type: term
  source_chapter: § 1.513(b)(2)
  source_quote: '"you must determine and document whether the foreign supplier of the food is in good compliance standing with the food safety authority of the country in which the foreign supplier is located."

    '
  summary: 走〔§ 1.513〕「FDA 已正式认可或判定等效的食品安全体系」路径时的第二个条件：除须记录供应商处于该国监管之下、且食品在认可范围内，还须判定并记录其在该国主管机关处的合规状态，并持续监控。常见误读是以为「来自等效国家」即自动免验证——仍免不了〔§ 1.503〕〔§ 1.509〕〔§ 1.510〕，也不适用于需进一步加工的食品。
  tags:
  - v4.21
  - subpart L
  - 简化路径
  - 判定判据

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

- [x] 第十六来源 **FDA CP 7303.842**（2023-11-01 版 / 2025-09-30 更正，80 物理页 / 148 书签）检查程序已并入，术语 t183–t192 共 10 条（版本判定与 7303.844 合并、内部作业指导层效力边界、Table 1/2 分工与 90/10、六类检查分流、PAC 双码表与 03842H 同名不同义、Sampling 三类与 for cause only、PART IV 阈值性质与 CPG 判据出口、Table 4 ranking 与 §123.6 显著性分离、执法裁量与 403(b) 误标定性、十六类不可混引与转换质量红线）。引文取自 CAP-24 R 段经 `.cangjie/verify_v4_11_quotes.py` 核验的 **36 个英文引用块**（36/36 命中正文区，0 超 100 词、0 表格引用）。原文标「CP 7303.842 PART x / Table x / ATTACHMENT A #x / Lxxx」，法条标〔§ 123.xxx〕，指南标「Seafood Hazards Guide 第 4 版 Ch.x」，三者不可混引；CPG / BAM / NSSP / Import Alert / part 1 subpart L 等未收正文一律标『转引未收』。全库 **192 条**，v4.11，**十六类来源不可混引**。

- [x] 第十七来源 **21 CFR Part 108**（Emergency Permit Control，4-1-25 Edition，11 页 / 9 条款）法规正文已并入，术语 t193–t202 共 10 条，围绕「手续层 vs 实体层」与「许可=救济不是常态」排布：emergency permit 的法定定义与临时性 → FCE 注册（2541，10 天/报检前）→ 工艺备案（2541e/2541d/2541f/2541g，60 天）与「备案≠批准」→ prima facie basis → working days 与日历天两种时限 → 无证生产的扣留与事先书面批准 → §801 拒绝入境 → BPCS 受训主管 → 记录保存四套口径 → 故意变更的边界（升参数不算）。引文取自 CAP-25 R 段经 `.cangjie/verify_v4_12_quotes.py` 核验的 **27 个英文引用块**（27/27 命中正文区，0 超 100 词、0 表格引用）。原文标〔§ 108.xxx〕，与〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕并列但互不混引；2541 系列表单栏目细则、FURLS / Center Views 操作、part 110/120 等未收正文一律标『转引未收』。全库 **202 条**，v4.12，**十七类来源不可混引**。

- [x] 第十八来源 **21 CFR Part 120**（HACCP Systems，4-1-25 Edition，10 页 / 15 条款）法规正文已并入，术语 t203–t212 共 10 条，围绕「独立 HACCP 体系 + 与 Part 117 的条件性接口」排布：juice 管辖与三项排除 → 5-log 的法定性 → pertinent microorganism → HACCP 计划七要素 → reasonably likely to occur 的 prudent processor 判定 → SSOP 八项与计划的关系 → 记录复审 1 周（7 日历天） → 记录保存第六套口径 → 果面处理的 biotype I E. coli 专项验证 → 两处豁免的对象差异。引文取自 CAP-26 R 段经 `.cangjie/verify_v4_13_quotes.py` 核验的 **26 个英文引用块**（26/26 命中正文区，0 超 100 词、0 表格引用）。原文标〔§ 120.xxx〕，与〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕并列但互不混引；〔§ 117.5(c)〕逐字文本、part 110 正文、CP 7303.047、CPG / Import Alert / BAM 全文一律标『转引未收』。全库 **212 条**，v4.13，**十八类来源不可混引**。

- [x] **第二来源 21 CFR Part 117 全文自 v4.14 起随仓库分发**（`books/_inbox/21-CFR-Part-117-2025.md`，160,825 字节 / 3,577 行）。该件自 v1 起就在 metadata 里声明为「第二来源」，但文件从未入库，导致全包〔§ 117.xxx〕引文长期无法在本仓库内复核——v4.13 的 CAP-26 因此把 §117.5(c) 标为「转引未收」。本轮补入后新增术语 **t213**（§117.5 四款豁免的结构差异），并对全包 **23 处**〔§ 117.xxx〕引文做追溯核验（`.cangjie/verify_v4_14_part117_quotes.py`，**23/23 命中**，含 2 处带省略号的节引按段核验）。全库 **213 条**，v4.14。

- [x] 第十九来源 **FDA CP 7303.847《Juice HACCP Inspection Program》**（2010-11-02 版 / 2025-09-18 更正，26 页 / 35 书签）检查程序已并入，术语 t214–t223 共 10 条，围绕「检查员侧取证」排布：版本口径与 CPGM 效力 → 三类样品分流（验证/有因/文档性）与 PAC → 「没取样」的三条理由 → HACCP 与非 HACCP 双组件 → 进口商 MOU 与 affirmative steps 判据 → ATTACHMENT A 采样量 → 铅拟议行动水平 → 60 天复检与升级路径 → 检查员不代写计划 → 与法条层 CAP-26 的分工。引文取自 CAP-27 R 段经 `.cangjie/verify_v4_15_quotes.py` 核验的 **28 个英文引用块**（28/28 命中正文区，0 超 100 词、0 表格引用）。原文标「CP 7303.847 PART x / ATTACHMENT A」，企业义务标〔§ 120.xxx〕；⚠ v4.13 曾把本程序误写为 `CP 7303.047`，v4.15 订正为 **7303.847**。全库 **223 条**，v4.15，**十九类来源不可混引**。

- [x] 第二十来源 **FDA IOM 2026 Chapter 4《Sampling》**（189 页 / 361 书签 / 4.2 MB）检查程序已并入，术语 t224–t233 共 10 条，围绕「取样作为证据的形式要件」排布：21 CFR 2.10 的 official sample 三条件 → DOC 的两条反直觉 → INV/survey/non-regulatory 三类 → 702(b) 七项豁免与污秽反向例外 → Zone 1–4 与 50/100 → 不得预告与 D/E、24 小时 → 表单链与 FDA 415a 三硬规则 → 阳性上 483 的三条件与 704(d) 四问 → Sample Schedule Chart 2 → 六套数量分层与转换件引用纪律。引文取自 CAP-28 R 段经 `.cangjie/verify_v4_16_quotes.py` 核验的 **60 个英文引用块**（60/60 命中正文区，0 超 100 词、0 表格引用；`body_only()` 排除自写文件头以防自我验证循环）。原文标「IOM 4.x.x / IOM Exhibit 4-xx / IOM Sample Schedule Chart x」，企业义务标〔§ 117.xxx〕等法规正文；⚠ 环境拭子 50/100 是**检查员侧最低量**，不是企业 EMP 标准。**全包自 v4.16 起二十类来源不可混引，28 张能力卡**。全库 **233 条**，v4.16。






---

## v4.17 增量术语 — IOM 2026 Chapter 6: Imports（t234 起）

> 完整词典见 `books/iom-2026-ch6-imports/GLOSSARY.md`（28 条）；此处收最易造成判定错误的高价值词条。

| 术语 | IOM 定义（浓缩） | 出处 | 与常识的差异 / 混淆后果 |
|---|---|---|---|
| May Proceed | 电子审查后允许货物进入流通的放行决定 | IOM 6.9.56 [p.56]、6.4.3 [p.35] | 字面像「准许继续办理」，实为终局放行；且系统定义明写「未作合规判定」，误当已合规会免除后续责任 |
| Conditional Release | 货物先交进口商控制但仍处 FDA 管辖、须保持可召回 | IOM 6.9.13 [p.51]、6.2.4 [p.20] | 不是「有条件合格」；货 may be moved 但不可分销，误判即 Failure to Hold |
| Failure to Hold | 未获 FDA 放行即已分销货物 | IOM 6.6.4.1 [p.43]、6.9.30 [p.53] | 原文特意加 `*Please note` 强调「不是移出港区」；按位置判断违规会答错 |
| DWPE | Detention Without Physical Examination，凭违规史/Import Alert 免实物查验即扣 | IOM 6.9.22 [p.52] | 「不检查」不是放过，恰是不检查就扣住；解除须至少一份 FDA 自采 audit sample，企业送检报告无效 |
| DER / DTR | 审查员提交扣留建议的两种 work type：DER 用于受 DWPE 约束，DTR 用于其他 | IOM 6.2.5.1 [p.21] | 按**触发依据**分流，不是严重度分级；误当轻重档会走错通道 |
| Detention / Refusal | Detention 是临时行政措施（基于 appear not to be），Refusal 是终局决定 | IOM 6.9.21 [p.52]、6.9.44 [p.55] | Refusal 仍非流程终点：档案到销毁/出口证明才关闭 |
| Release with Comment | 已明确认定存在违规（无公共健康风险）仍放行，并预告后续同类 entry 可能被拒 | IOM 6.9.69 [p.57] | 与 May Proceed / Release / IB Release 是四种法律含义不同的放行，不可统一映射成「放行＝合规」 |
| Prior Notice | 食品/饲料抵达前须经 FDA 电子**接收并确认**的独立法定前置义务 | IOM 6.1.5.1 [p.9]、6.1.5.5 [p.11] | 提交≠完成；15/30 天是上限、2/4/8 小时是下限，早报同样不合规；不能用报关单替代 |
| Reconditioning / Relabeling | 在 FDA 批准并监督下使不合格品达可采状态（Form FDA 766） | IOM 6.5.2.3 [p.40]、6.9.65/6.9.68 [p.57] | 改标 ⊂ 重整；企业未经批准自行返工**不产生放行效力**；申请主体是 importer of record |
| FDA 483a | FSVP Observations，只在检查结束 closeout 签发且只签已签名版 | IOM 6.8.2.1 [p.48-49] | **≠ FDA 483**（IOM Ch.5 现场检查观察项，CAP-18）；检查期间展示草稿被明文禁止 |
| FSVP Importer / Importer of Record | 前者是 FSMA 供应商验证主体（须在美国境内），后者是 CBP 报关/bond 主体 | IOM 6.9.40 [p.55]、6.9.43 [p.55] | 两套法律身份，常非同一人；混淆会导致 766 申请主体与 bond 判断出错 |
| IB | 同形异义：Import Bulletin（指示请求现场工作）vs Investigations Branch（IB Release 签发主体） | IOM 6.3.10.7 / 6.3.11 [p.32] | 误读会把现场放行当成进口公告 |

> **源层瑕疵（如实标注）**：6.9 术语表共 78 条，末条编号 `6-9.78` 与前 77 条 `6.9.x` 不一致；6.9 未收 DER、IUC、Import Bulletin、SDI、VQIP 本体、IB Release，须回 6.1–6.8 取定义。另 `6.2.5.5` 的 reasonable effort 条款正文跨页落在 p.23（与 6.3 起始页重叠），引用按小节号而非分块文件名。


## v4.18 — 21 CFR Part 101 术语增量（t234–t277，44 条）

> 全部回 `source-cfr-part101-2026.md` 原文逐字核验；`clause` 统一为〔§ 101.xxx〕，属**法规正文层**，与 Part 117 预防控制层、Ed.5 guidance 层不同源。

| 术语 | 条款 | 浓缩释义 | 常见误读 |
|---|---|---|---|
| principal display panel (PDP) | 〔§ 101.1〕 | 最可能在零售陈列条件下被展示的标签部分；面积按矩形高×宽 / 圆柱 40% 高×周长 / 其他形状 40% 总表面 | 当成可自由指定的「正面」；圆柱强制信息必须落在那 40% 内 |
| information panel | 〔§ 101.2〕 | 紧邻 PDP 右侧的法定相对方位（有例外） | 以为任意空白面都能放营养标签与配料表 |
| serving / serving size | 〔§ 101.9(b)〕 | 由 §101.12(b) RACC 推导的 customary consumption 量 | 当成厂商建议食用量或营养建议 |
| RACC | 〔§ 101.12〕 | 按产品类别给出的参考量，是所有声称阈值与 Daily Value 的共同分母 | 抄表值当企业内控规格；表值为不可逐字引用区 |
| nutrient content claim | 〔§ 101.13(b)〕 | 明示或暗示表征 §101.9/§101.36 要求标示的营养素水平 | 以为「暗示」「品牌名」不算 claim |
| health claim | 〔§ 101.14(a)(1)〕 | 明示或暗示表征某物质与疾病/健康相关状况的关系，含 heart 符号、vignette、第三方引用 | 以为「有研究支持」即可；须 SSA + 不超 disqualifying level |
| significant scientific agreement | 〔§ 101.14(b)〕 | 合格科学专家间的显著科学一致，健康声称获授权的法规级证据门槛 | 与「有论文/有专家背书」混同 |
| disqualifying level | 〔§ 101.14(a)(4)〕 | 食品中特定营养素超过阈值即**丧失**健康声称资格 | 只查正面条件、漏查负面资格门槛 |
| gluten-free | 〔§ 101.91(a)(3)〕 | 不可避免的麸质存在须 **below 20 ppm**，是定量定义 | 当成「无添加」营销词；与亚硫酸盐 10 ppm 混算 |
| incidental additive | 〔§ 101.100(a)(3)〕 | 量不显著且在该食品中无技术或功能效果，可免配料表申报 | 以为一律免申报；亚硫酸盐 ≥10 ppm 是反向例外 |
| 标签义务豁免 | 〔§ 101.100〕/〔§ 101.9(j)〕/〔§ 101.108〕 | 免的分别是配料表 403(i)(2) / 营养标签 / 经 FDA 批准的临时实验 | 把 §101.100 当营养标签豁免；把主体豁免混进来 |
| misbranding | 〔§ 101.18〕/ FD&C Act §403 | 标签或 labeling 中虚假或误导性陈述使食品错标 | 与 402(a) adulteration（掺假）混为一条执法钩子 |

> 完整 44 条见 `books/cfr-part101-2026/GLOSSARY.md`；YAML 块内 t234–t277 已并入上方词典。
---

## v4.19 增量术语 — 21 CFR Part 172: Direct Food Additives（t278 起）

> 完整词典见 `books/cfr-part172-2026/GLOSSARY.md`（41 条）；此处收最易造成判定错误的高价值词条。YAML 块内 t278–t318 已并入上方词典。

| 术语 | 条款 | 浓缩释义 | 常见误读 |
|---|---|---|---|
| direct food additive（直接食品添加剂） | 21 CFR Part 172 标题 / Authority | 直接加入食品、在成品中保留技术效果的添加剂，许可与限量由 Part 172 管；法源为 FD&C Act §201(s) 定义与 §409。与间接添加剂（包装材料迁移，Part 175–178）不同、与本包未收的 GRAS/临时许可不同。常… | 把「直接添加剂」当成「可食用配料」或把间接添加剂混进来判定 |
| good manufacturing practice（本部分的口径） | § 172.5(a) | 本部分的 cGMP 不是泛泛口号，§172.5(a) 把它定义为两条具体限制：用量不超过合理需要量、物质须为食品级。它叠加在每一条 §172.xxx 之上，即使条款给了 ppm 上限也仍然生效。常见误读是把 GMP 当「建议层」，以为无法律… | 把 GMP 当「建议层」，以为无法律约束力 |
| amount reasonably required（合理需要量） | § 172.5(a)(1) | 无 ppm 上限的条款由这条兜底：用量不得超过实现预期物理、营养或其他技术效果所合理需要的量。它是一条实质限制，主张者须能论证技术效果需要多少。常见误读是「没有数字＝不限量」。 | 「没有数字＝不限量」 |
| food grade（食品级） | § 172.5(a)(2) | 用于食品的物质须为适当食品级，并作为食品配料制备与处理。工业级或非食品级原料即使化学上等同也不合规。常见误读是只看纯度数值、不问是否按食品配料管理。 | 只看纯度数值、不问是否按食品配料管理 |
| existence of a regulation（许可法规的效力边界） | § 172.5(b) | 存在许可法规不得被解释为免除该物质受本法其他任何条款约束的义务。Part 172 只管许可与限量/规格层，标签归〔§ 101〕、过程控制归〔§ 117〕。常见误读是把「有 Part 172 条款」当成整体合规的免死金牌。 | 把「有 Part 172 条款」当成整体合规的免死金牌 |
| nutrient substance approval（营养物质许可 ≠ 有用性认定） | § 172.5(c) | 营养物质获许可只解决安全性，不构成其「对人类膳食有用或必需」的认定。据此做营养声称或膳食必要性主张属越界。常见误读是把「FDA 批准该营养素」当声称依据。 | 把「FDA 批准该营养素」当声称依据 |
| antioxidant（抗氧化剂功能） | § 172.110(b) | 抗氧化剂是本部分 Subpart B 的主功能之一，BHA 与 BHT 由同一表列头 total BHA and BHT 管、须合并计算。功能本身也是许可要件的一部分（超功能使用不获许可）。常见误读是把抗氧化剂与防腐剂混为一类从而套错限值表… | 把抗氧化剂与防腐剂混为一类从而套错限值表 |
| in combination（合并限量） | § 172.120(b)(2) | 「in combination」指两种或多种物质合用时的限量按合并值计，不得各自擦线合格。钙二钠 EDTA 与二钠 EDTA 即属此例。常见误读是各物质按各自表值独立计算。 | 各物质按各自表值独立计算 |
| parts per million calculated as（计量基准） | § 172.180 | 限值常附「以某元素计」（calculated as X）的换算基准，如以 Sn 计、以 Br 计、以无水物计。换算基准错了限值就错了。常见误读是按化合物整体质量而非指定元素/形态计算。 | 按化合物整体质量而非指定元素/形态计算 |
| as measured in the loin muscle（法定取样部位） | § 172.177(b) | 取样部位本身可以是法规要件。烟熏鲢条款要求盐与亚硝酸盐均在 loin muscle 测定；换部位测出的数据不满足法定判据。常见误读是把限值当成对成品整体的平均值要求。 | 把限值当成对成品整体的平均值要求 |
| water phase portion（水相盐分） | § 172.177(b) | 盐分判据按「可食部的水相部分」计，且为下限（≥3.5%），与通常只给上限的限量方向相反。常见误读是按整鱼重量算盐分或只查上限。 | 按整鱼重量算盐分或只查上限 |
| treated malt use-locked labeling statement（用途锁定声明） | § 172.730(c) | 用途限制通过处理物标签上的逐字法定措辞执行，自拟措辞不产生同样效果。同款结构亦见〔§172.725〕对赤霉酸/赤霉酸钾处理的麦芽。常见误读是以为意思相同即可。 | 以为意思相同即可 |
| bromate (calculated as Br)（以 Br 计的溴酸盐限值） | § 172.730(a)(1) | 溴酸钾在麦芽中的限值为 ≤75 ppm 溴酸盐、以 Br 计，属「限值算在中间品」。常见误读是误算在成品饮料上，或按溴酸钾分子量而非 Br 计。 | 误算在成品饮料上，或按溴酸钾分子量而非 Br 计 |
| total residue of inorganic bromides（他源累计残留） | § 172.730(a)(2) | 成品溴化物总残留须把「按本章其他法规使用所产生的额外同类残留」一并计入（≤25 ppm，以 Br 计）——即跨法规累计。常见误读是只算自己添加剂的贡献。 | 只算自己添加剂的贡献 |
| carrier（载体）与浓度披露 | § 172.110(c)(2) | 以合适载体形式售卖的添加剂，标签除名称外还须申报添加剂在混合物中的百分比。常见误读是只标混合物商品名，不披露有效成分浓度。 | 只标混合物商品名，不披露有效成分浓度 |
| intermediate mix（中间混合料） | § 172.804(d)(1) | 面向生产的中间混合料须在主展示面标明添加剂浓度，以便下游正确配料。常见误读是把中间混合料当半成品、不做浓度披露。 | 把中间混合料当半成品、不做浓度披露 |
| adequate directions for use（足够使用说明） | § 172.120(c)(2) | 「足够使用说明」是法定的间接管控手段：通过容器标签指导下游，使成品不超限。常见误读是以为限值只靠终端检测，忽略说明书义务。 | 以为限值只靠终端检测，忽略说明书义务 |
| To assure safe use（标签义务段） | § 172.730(b) 对照 § 172.110(c) 等 | 「To assure safe use」段是条款内的标签义务块，实测仅约 25% 条款带此段。有该段时必须落实（通常要求标添加剂名称与足够使用说明，如本处以 name of the additive 与 adequate direction… | 默认条条都有标签义务 |
| identity / specifications / conditions of use（三段式条款语法） | § 172.785 | 条款常按 (a) Identity → (b) Specifications → (c) Conditions of use 三段展开：身份要件、纯度/效价规格、使用条件。判读时逐段核对，任一段不满足即不合规。常见误读是只看用量一段。 | 只看用量一段 |
| incorporated by reference (IBR) | § 172.185(b) / § 172.785(b)(1) | IBR 指把外部文件（FCC 页码、厂商方法、菌株资料）并入法规，法律效力等同正文，但内容不在本件、不在本技能包内。只可引「须符合某文件某版某页」，绝不转述其内部数值。常见误读是凭记忆写出被引文件的数值。 | 凭记忆写出被引文件的数值 |
| Food Chemicals Codex (FCC) | § 172.831(b) | FCC 是 Part 172 最常被 IBR 引用的纯度规格来源，引用须写清版次与页码（FCC 7th ed.＝2010、9th ed.＝2014）。版本/页码张冠李戴即引用错误。常见误读是把 FCC 当法规正文直接引其数值。 | 把 FCC 当法规正文直接引其数值 |
| specifications（纯度规格直写） | § 172.110(a) | 部分条款把规格数值直接写在条文里（可核对），与整体 IBR 的条款并存于同一 Subpart。判定先问：这条给的是可读数值还是外转引用。常见误读是假设「有规格＝有可读数值」。 | 假设「有规格＝有可读数值」 |
| Use / Function 栏（功能限制） | § 172.120(b)(1) | 限值表常带 Use/Function 栏，把物质的使用绑定到特定功能（如 retard struvite formation、promote color retention）。超功能使用不在许可内。常见误读是只核对 ppm、忽略功能要件；表… | 只核对 ppm、忽略功能要件；表内 Use 栏文字属表区，须回原 PDF 核对 |
| specified foods（指定食品，封闭清单） | § 172.110 | 「specified foods」是封闭清单，须逐项对照；未列举的食品即不在许可内。常见误读是把列举当作举例、允许类推到「相近」食品。 | 把列举当作举例、允许类推到「相近」食品 |
| except in meat and poultry（肉禽除外） | § 172.829(c) / § 172.800 | 「食品一般、肉禽除外」是通用甜味剂类条款的常见范围句式。肉禽制品属 USDA/FSIS 管辖，另成体系，不得搬用 Part 172 许可。常见误读是见「foods generally」就认为无类别限制。 | 见「foods generally」就认为无类别限制 |
| standards of identity do not preclude such use（标准身份不排除） | § 172.829(c) | 即使有添加剂许可，若某标准化食品（section 401 标准身份）排除该用途，则仍不得使用。判定顺序是先过标准身份闸门、再过用量。常见误读是认为 FDA 许可优先于标准身份。 | 认为 FDA 许可优先于标准身份 |
| special dietary use（特殊膳食，part 105） | § 172.829(e) | 条款内部指向 part 105 的特殊膳食标签义务：食品若宣称或表示为特殊膳食用途，须符合 part 105。这是跨部分义务，不因符合 Part 172 用量而免除。常见误读是把该指引当可有可无的提示。 | 把该指引当可有可无的提示 |
| antimicrobial agent（抗菌剂） | § 172.785 | 生物类抗菌剂（如李斯特菌噬菌体制剂）的许可对象是「针对特定致病菌的抗菌用途」，范围由靶菌与食品类别共同封闭。常见误读是当作广谱消毒剂或通用防腐剂使用。 | 当作广谱消毒剂或通用防腐剂使用 |
| bacteriophage（噬菌体）身份要件 | § 172.785(a)(1) | 身份要件须逐条满足：6 种等比例、各自纯化、裂解型且无溶原活性、特异性针对 L. monocytogenes。常见误读是只看「含噬菌体」而不核数量、比例与溶原性。 | 只看「含噬菌体」而不核数量、比例与溶原性 |
| ready-to-eat（9 CFR 430.1） | § 172.785(c) | 适用范围边界外转到 9 CFR 430.1 的 ready-to-eat 定义：是否即食按该外部定义判定，不按「接近即食」的直觉。常见误读是以产品性质相近替代法定定义。 | 以产品性质相近替代法定定义 |
| potency / lytic result（效价与裂解结果） | § 172.785(b)(1) | 效价要件是「对指定 ATCC 菌株呈阳性裂解结果（OD600 ≤0.06）」，菌株编号与血清型是法定要件。测法多 IBR 外转。常见误读是只写「有抑菌效果」而不核指定菌株与阈值。 | 只写「有抑菌效果」而不核指定菌株与阈值 |
| nutrient compensation（强制营养补偿） | § 172.867(d) | 脂肪替代物（Olestra）的许可以「强制补偿脂溶性维生素」为生效条件：须按规定量添加 A/D/E/K，否则不合规。常见误读是把补偿当推荐做法。 | 把补偿当推荐做法 |
| Dietarily insignificant（膳食上不显著） | § 172.867(e)(1)(iii) | Olestra 补偿添加的 A/D/E/K 须在配料表用星号标注，并在配料表后紧随星号与 Dietarily insignificant 声明，不得计入营养标签或营养声称。常见误读是把补偿维生素算作产品营养含量。 | 把补偿维生素算作产品营养含量 |
| natural flavoring substances（天然香料） | § 172.510 | 天然香料是名录型条款（Common name / Scientific name / Limitations 三列约千行），条首仅给「最小需要量 + GMP」通用条件，具体限制须逐行看 Limitations 列。名录内部行属不可逐字引用区… | 把「在清单里」当「无限制」 |
| synthetic flavoring substances and adjuvants（合成香料与助剂） | § 172.515 | 合成香料清单（约 30 页、上千条物质名）为纯名录，不含用量限制列，只解决「是否被许可」。用量回到条首的「最小需要量 + GMP」。常见误读是去名录里找 ppm。 | 去名录里找 ppm |
| Do.（同上 / ditto） | § 172.510(b) 名录行示例 | Do. 是英文编纂惯用的「同上」，表示复制上一行同列的内容，绝非「无限制」。整列 Do. 还提示可能跨页续表被重置，须回原 PDF 逐格核对。示例行取自名录（名录内行属不可逐字引用区，此处仅引 Do. 语义）。常见误读是把 Do. 读成空白… | 把 Do. 读成空白或免除 |
| multipurpose additive（多用途添加剂） | Subpart I | Subpart I 收录可按多种功能使用的添加剂（甜味剂、脂肪替代物、改性淀粉、乳化剂等），多为「食品一般 + cGMP」型或表格式限量。与前面按功能单列的子部分结构不同。常见误读是把它当作「无功能限制」。 | 把它当作「无功能限制」 |
| residual limitation（成品残留限值） | § 172.892 | 改性淀粉类条款把「合理需要量」与「任何规定限值」并列，并常另设成品残留限值（如残锰、残磷）。限值可能落在处理剂、也可能落在成品残留。常见误读是只查处理剂用量、漏查成品残留。 | 只查处理剂用量、漏查成品残留 |
| food starch-modified（法定品名） | § 172.892 | 改性淀粉容器标签须逐字标示法定品名 food starch-modified。此类「法定品名」义务是条款自带义务的一种形态，与 To assure safe use 段不同。常见误读是自拟商品名代替法定品名。 | 自拟商品名代替法定品名 |
| generally recognized as safe（条款内 GRAS 指引） | § 172.510(b) | Part 172 条款内部会指向 GRAS、prior-sanctioned 或其他条款所管物质，形成「与获准物质组合使用」的许可路径。GRAS 本体（Part 182 等）不在本包内，只可引「属于 GRAS」这一事实，不复述其清单。常见误… | 把 GRAS 当可在 Part 172 内自行认定 |
| prior-sanctioned（既往认可） | § 172.515(b) | prior-sanctioned 指 1958 年添加剂修正案前已获 FDA/USDA 认可的物质，与 GRAS 并列为另一条合法性来源。其清单不在本包内，只可引「属于 prior-sanctioned」这一事实。常见误读是把 prior-… | 把 prior-sanctioned 与 GRAS 混为一条路径 |

> 完整 41 条见 `books/cfr-part172-2026/GLOSSARY.md`；YAML 块内 t278–t318 已并入上方词典。Part 172 术语为「判读用语」而非 21 CFR 117.3 式法定定义；不可逐字引用区为 16 张重建表格数值、§172.510/§172.515 名录内部行、全部 IBR 外部文件内容。

## v4.20 增量术语 — 21 CFR Part 121: Intentional Adulteration（t319–t327）

> 本段收最易造成判定错误的 9 条判读用语，已并入上方 YAML 块（t319–t327，全表 327 条）。Part 121 的定义属**本部分自用口径**（`for purposes of this part`），不得直接替换〔§ 117.3〕的术语，也不得与 CAP-06 的 EMA 术语互引。

| 术语 | 条款 | 浓缩释义 | 常见误读 |
|---|---|---|---|
| food defense（食品防护） | § 121.3 | 防蓄意掺假、且掺假意图造成**大规模公共卫生危害**的行动；构成要件是 intent + wide scale 两层 | 当成「厂区安保/防盗」；当成「食品欺诈（EMA）」 |
| contaminant（本部分） | § 121.3 | 蓄意加入以造成疾病、伤害或死亡的生物/化学/物理/**放射性**介质 | 当成通用污染物定义去替换〔§ 117.3〕 |
| significant vulnerability（显著脆弱性） | § 121.3 / § 121.130(a) | 若被利用可合理预期造成大规模公共卫生危害；三要素：公共卫生影响（severity 与 scale）/ 物理接近 / 攻击成功能力 | 只算单批后果不算 scale；把「物理接近」简化成「有没有锁门」 |
| actionable process step（APStep） | § 121.3 | 三条件同时成立：存在显著脆弱性 + 可施加缓解策略 + 该策略不可或缺 | 把 CCP 或「关键工序」直接当 APStep |
| mitigation strategies（缓解策略） | § 121.3 / § 121.135 | 基于风险、合理适当的措施；须逐条书面解释其**充分性**，终点回指 §402 掺假 | 只列策略名、不写充分性解释 |
| vulnerability assessment（脆弱性评估） | § 121.130 | 按**每种食品**做；三要素 + 强制考虑内部人员；无论结论如何都须书面并逐点说明理由 | 按车间做一份；只解释「是 APStep」的点，判 No 的留空 |
| food defense plan（食品防护计划） | § 121.126 | 五要素封闭清单：评估 / 策略 / 监控程序 / 纠正程序 / 验证程序；计划须签名注日期 | 用〔§ 117.126(b)〕FSP 七部件去套；不签名 |
| inside attacker（内部人员） | § 121.130(b) | 脆弱性评估的**强制考量项** | 只评外来闯入者；或反过来读成「必须做背景调查」 |
| qualified individual（Part 121 语境） | § 121.4 / § 121.3 | 四类核心活动须受标准化课程或等效岗位经验；APStep 人员另须 food defense awareness 培训 | 直接等同〔§ 117.180〕的 PCQI 培训体系 |

> 完整 9 条见上方 YAML 块 t319–t327；本部分术语为「判读用语」而非 21 CFR 117.3 式法定定义，不可逐字引作法规原文。

## v4.21 增量术语 — 21 CFR Part 1 Subpart L: FSVP（t328–t336）

> 本段收 9 条最易造成主体或时限错判的词条，已并入上方 YAML 块（t328–t336，全表 336 条）。FSVP 的定义属**本 subpart 自用口径**（`as they are used in this subpart`），不得直接替换〔§ 117.3〕的术语。

| 术语 | 条款 | 浓缩释义 | 常见误读 |
|---|---|---|---|
| U.S. owner or consignee | § 1.500 | importer 的第一顺位：入境时在美拥有／已购买／已书面同意购买者 | 把报关行、货代、境外出口商当 importer |
| foreign supplier | § 1.500 | 最后制造/加工、饲养或种植并出口美国的实体；**只加贴标签不算进一步加工** | 把品牌方或贸易商当供应商 |
| very small importer | § 1.500 / § 1.512 | 人食 <100 万、动物食品 <250 万（3 年均值、含关联企业、计入未销售市值） | 只算销售额、漏掉未销售部分市值；两套金额混用 |
| receiving facility + deemed compliance | § 1.502(c) | 三条件满足即视为合规，**但排除〔§ 1.509〕** | 「我们是接收设施所以不用报 UFI」 |
| hazard requiring a control | § 1.500 / § 1.504 | 按「无控制时概率 × 严重性」判定；书面无论结论 | 结论为「无」就不写；以为可免危害分析本身 |
| serious hazard → 年度现场审核 | § 1.506(d)(2) | 供应商控制的危害 + 可能致严重健康后果/死亡 → 初次前 + 每年 | 等同「显著危害」；忽略「由供应商控制」前提 |
| written assurance 三要素 | § 1.507(b) | 生效日期 / 授权官员印刷姓名与签名 / 该款保证内容 | 以为有对方盖章即成立；忽略〔§ 1.507(c)〕须一致行动 |
| qualified auditor | § 1.500 / § 1.503(b) | qualified individual + 审计技术专长（政府雇员或 subpart M 认证机构审核员） | 把内部质检員当合格审核人 |
| good compliance standing | § 1.513(b)(2) | 等效国家路径的第二个条件：须判定并记录供应商在该国主管机关的合规状态 | 「来自等效国家＝自动免验证」 |

> 完整 9 条见上方 YAML 块 t328–t336；本部分术语为「判读用语」，不作法规原文逐字引用。
