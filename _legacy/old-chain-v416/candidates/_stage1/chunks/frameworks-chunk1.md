# Frameworks 候选 — Chunk 1 (source.md 第 1–3300 行)

> 覆盖范围: Introduction（术语表/资源表）、Ch1（FSP 与 HACCP 对比）、Ch2（危害分析）、Ch3 前半（生物危害识别、过程相关危害、ROP 屏障、Transient/Resident）
> 提取规则: 不做筛选，宁错杀；每条均有本块原文依据。

- id: f1-01
  title: 六列危害分析工作表法
  type: framework
  source_chapter: Ch2 (2.3.2, Box 2-3)
  source_quote: |
    "Column 3: Here, you will record the conclusions of your hazard evaluation – i.e., the
    determinations you make of whether each listed food safety hazard requires a preventive
    control (Yes or No). ... Column 6: ... you specify whether the preventive control will be
    applied at this particular step (Yes/No)."
  summary: |
    把任何"风险判定"任务拆成一张六列表：步骤 → 识别潜在危害 → Yes/No 判定 → 判定理由 → 控制措施 → 是否在本步实施。
    每一列强制回答一个独立问题，使识别、评估、决策、论证、方案、落点彼此解耦、逐格填空。
    好处：任何一格空缺都可见，判定质量取决于填表纪律而非个人发挥；且天然生成可审计的书面记录。
    可迁移为通用的"风险六列法"：对象/风险/是否处置/理由/手段/在哪处置。
  tags: [structured-procedure, worksheet, hazard-analysis, decision-logic]

- id: f1-02
  title: 书面 Yes/No 判定——解释 No 与解释 Yes 同等重要的保守策略
  type: framework
  source_chapter: Ch2 (2.3.2 Column 4)
  source_quote: |
    "Explaining your reasons for a \"No\" conclusion can be just as important as explaining your
    reasons for a \"Yes\" conclusion. To be thorough and to have readily available answers to
    questions about your hazard analysis, you may find it useful to take a conservative approach
    by listing in Column 2 several potential hazards even though they clearly do not require a
    preventive control."
  summary: |
    决策不仅要记录"选了什么"，还必须记录"为什么没选"。
    对有争议的事项，宁可先把它列入清单再论证排除，也不悄悄忽略——把"排除"变成一个显式的、可辩护的决策。
    这是对抗事后质疑（检查/审计/复盘）的防线：空白的论证等于未考虑，写下的 No 才是被考虑过的 No。
    可迁移到任何需要"负向判定留痕"的场景：安全评审、投资否决、需求砍削。
  tags: [decision-logic, conservative-judgment, documentation, audit-defense]

- id: f1-03
  title: NACMCF 十类危害识别问题清单
  type: framework
  source_chapter: Ch2 (2.4.1)
  source_quote: |
    "You may find the following list of questions helpful during the hazard identification
    process. We adapted this list from Hazard Analysis and Critical Control Point Principles and
    Application Guidelines published by the National Advisory Committee on Microbiological
    Criteria for Foods."
  summary: |
    沿产品生命周期布置 10 组提问做系统性扫查：① 原料 ② 内在特性（组成/pH/a_w）③ 加工步骤 ④ 微生物本底 ⑤ 厂房设计 ⑥ 设备设计与使用 ⑦ 包装 ⑧ 员工健康与卫生 ⑨ 包装后储存 ⑩ 预期用途与使用者。
    每组内是具体的 yes/no 问题，逐组过一遍即可把"想漏了什么"变成"逐项排查"。
    本质是把隐性经验显性化为覆盖度清单，防止识别阶段凭直觉漏项。
    可迁移为任何领域的问题发现扫查表（设计评审、尽职调查）。
  tags: [checklist, hazard-identification, systematic-scan, NACMCF]

- id: f1-04
  title: 前期三文档 + 流程图现场核实
  type: framework
  source_chapter: Ch2 (2.3.1)
  source_quote: |
    "The purpose of a process flow diagram is to provide a clear, simple description of the steps
    involved in the processing of your food product and its associated ingredients as they 'flow'
    from receipt to distribution. ... You should verify the process flow diagram onsite in order
    to ensure no steps have been overlooked."
  summary: |
    在做任何分析之前，先固化三份基础文档：产品描述（含预期用途与消费人群）、工艺流程图、详细工艺描述（时间/手工/返工等细节）。
    关键纪律：流程图必须到现场走一遍核实——纸面流程与实际流程的偏差是分析失效的根源。
    逻辑：分析的输入质量决定分析质量；"文档上没有的步骤"永远不会被分析。
    可迁移为通用的"先建模、再核实、后分析"前置程序。
  tags: [preliminary-steps, process-flow, onsite-verification, groundwork]

- id: f1-05
  title: 危害评估双维度：严重性 × 无控制时的概率
  type: framework
  source_chapter: Ch2 (2.4.2)
  source_quote: |
    "Under 21 CFR 117.130(c)(1)(i), you must assess the severity of the illness or injury if the
    hazard were to occur and the probability that the hazard will occur in the absence of
    preventive controls."
  summary: |
    每个已识别的潜在危害都按两个独立维度评估：一旦发生有多严重（severity）× 在没有任何控制措施时发生的概率（probability）。
    两维都高才判定"需要预防控制"（Yes）；判定基准是"一个知情者在无控制的世界里会不会建控制"。
    注意概率是在"无控制前提下"估计的——这避免把已有控制误算成低风险而漏控。
    通用化为风险矩阵：后果 × 无防护时的暴露概率，用于排序与取舍。
  tags: [risk-matrix, severity, probability, hazard-evaluation]

- id: f1-06
  title: 严重性评估三因素
  type: framework
  source_chapter: Ch2 (2.4.2.1)
  source_quote: |
    "To evaluate the severity of a potential hazard, you should consider certain factors,
    including susceptibility of intended consumers to foodborne illness ..., the potential
    magnitude and duration of the illness or injury ..., and the possible impact of secondary
    problems (e.g., chronic sequelae such as kidney damage or reactive arthritis)."
  summary: |
    评估"有多严重"时不看平均情况，拆成三个放大器：① 目标人群易感性（婴儿/老人/免疫低下者）② 疾病的强度与持续时间（是否住院/致死）③ 二次远期后果（慢性后遗症如肾损伤、反应性关节炎）。
    同一危害对不同人群严重性完全不同——严重性是危害×人群的函数，不是危害的固有属性。
    自无专长时应咨询外部专家，不许拍脑袋。
    可迁移为通用的"后果分级三问"：伤谁、多痛、留不留后遗症。
  tags: [severity, vulnerable-population, consequence-assessment]

- id: f1-07
  title: 概率估计四数据源
  type: framework
  source_chapter: Ch2 (2.4.2.2)
  source_quote: |
    "When estimating likely occurrence, you should consider information from several sources,
    such as the following: Data from outbreaks of foodborne illness, Data from recalls,
    Information in the scientific literature, and Experience and historical information gathered
    by your facility."
  summary: |
    估计"会发生吗"时强制交叉使用四类证据：① 暴发数据（别人真实发生过）② 召回数据（监管视角的失效记录）③ 科学文献（机理与定量模型）④ 本厂历史（自身检测/投诉/污染史）。
    外部数据给出基线，内部数据给出修正；只用其中一类都会系统性偏差。
    配套原则：他厂的危害在本厂未必成立——设备、原料来源、工艺不同，必须逐厂单独估计。
    可迁移为通用的"四源证据法"做任何概率判断。
  tags: [evidence-sourcing, outbreak-data, recall-data, facility-history]

- id: f1-08
  title: 117.130(c)(2) 十类评估因素
  type: framework
  source_chapter: Ch2 (2.4.2.4)
  source_quote: |
    "When evaluating hazards, you must consider the effect of the following on the safety of the
    finished food for the consumer (21 CFR 117.130(c)(2)): The formulation of the food ... The
    condition, function, and design of the facility and equipment ... Raw materials and other
    ingredients ... Transportation practices ... Manufacturing/processing procedures ..."
  summary: |
    法规枚举的十类必须逐项考虑的因素：配方、厂房/设备状态、原料、运输、加工/处理程序、包装与标签、储存与分销、预期或可合理预见的用途、卫生（含员工卫生）、其他相关因素（如天气依赖性危害）。
    作用是把"评估是否全面"变成可核对的清单——检查者可逐项追问"这一项你考虑了吗"。
    每类因素都指向典型的失效模式（如多组分界面、老化设备藏污、冷却使孢子萌发）。
    可迁移为通用"环境因素盘点表"：任何系统的风险都沿这十个面向扫描。
  tags: [regulatory-checklist, evaluation-factors, failure-mode-scan]

- id: f1-09
  title: RTE 环境病原强制评估触发规则（if-then）
  type: framework
  source_chapter: Ch2 (2.4.2.3 / 117.130(c)(1)(ii))
  source_quote: |
    "you must include an evaluation of environmental pathogens whenever an RTE food is exposed
    to the environment prior to packaging and the packaged food does not receive a treatment or
    otherwise include a control measure (such as a formulation lethal to the pathogen) that would
    significantly minimize the pathogen."
  summary: |
    一条硬性 if-then 决策规则：IF 食品是即食（RTE）AND 包装前曾暴露于环境 AND 包装后无致死处理或等效控制 THEN 环境病原评估为强制项，无商量余地。
    两个条件相"与"即可触发，与工厂自认为多干净无关——规则的价值在于把"是否需要评估"从判断题变成条件核对题。
    体现了"用可观测的客观条件触发义务，而不是用主观判断豁免自己"的立法思路。
    可迁移为任何领域的强制检查触发器设计。
  tags: [if-then-rule, mandatory-trigger, environmental-pathogen, RTE]

- id: f1-10
  title: 控制措施识别七项考虑
  type: framework
  source_chapter: Ch2 (2.5)
  source_quote: |
    "your Food Safety Team should also consider - The effect of the control on identified
    potential food safety hazards ... - The feasibility of monitoring those controls ... - The
    location of the control with respect to other processing control measures ... - Corrective
    actions that will be needed in the event of a failure ... - The severity of the consequences
    in case of a failure of a control measure ... - Whether the control measure is applied to
    eliminate or significantly reduce the level of the hazard ... - Synergistic effects between
    control measures"
  summary: |
    选控制措施时的七维评估：① 对危害的实际效果（专用还是一控多害）② 可监控性（能否实时得到结果）③ 控制点与其他控制的位置关系（上游失效是否会击穿下游）④ 失效后纠正方案是否可行 ⑤ 失效后果严重性 ⑥ 是消除还是仅减小 ⑦ 控制间的协同效应（多项弱控制叠加成强屏障）。
    核心思想：控制措施不是孤立选的，要放进"控制网络"里评估——位置、冗余、协同、失效传播。
    可迁移为任何干预措施的选型框架（安全措施、流程改造、投资对冲）。
  tags: [control-selection, seven-considerations, control-network, synergies]

- id: f1-11
  title: 发现点 ≠ 控制点（列 6 逻辑）
  type: framework
  source_chapter: Ch2 (2.3.2 Column 6)
  source_quote: |
    "Because the worksheet breaks your production process into multiple steps, and the preventive
    control may be applied at a step in the process other than the step where you listed the
    hazard, you specify whether the preventive control will be applied at this particular step
    (Yes/No). It is important to note that identifying a hazard at a processing step as one that
    requires a preventive control does not mean that the hazard must be controlled at that
    processing step."
  summary: |
    把"问题在哪里被发现"与"控制在哪里实施"显式解耦：识别出危害的步骤不必是控制该危害的步骤。
    决策依据变为"在哪里控制最有效"，而不是"在哪里发现问题"——控制可以前移（供应链控制）或后移（成品检测）。
    工作表用独立的 Yes/No 列承载这个区分，避免"在哪发现就在哪修"的直觉错误。
    可迁移为通用的根因处置思维：修复点未必等于发现点，选杠杆最大的位置介入。
  tags: [decoupling, control-location, leverage-point, decision-logic]

- id: f1-12
  title: 逐步独立评估三分判定（引入/增长/可控制）
  type: framework
  source_chapter: Ch2 (2.4.2.2.4)
  source_quote: |
    "You should evaluate the potential hazards independently at each processing step ... you
    would identify a hazard as one requiring a preventive control if: it is reasonably likely
    that the hazard can be introduced at an unsafe level at that processing step; or it is
    reasonably likely that the hazard can increase to an unsafe level at that processing step; or
    the hazard was identified in an ingredient or at another processing or handling step and it
    can be controlled ... at the current processing step."
  summary: |
    每个加工步骤独立回答三个问题：危害会在此被引入吗？会在此增长到不安全水平吗？别处识别的危害能否在此被控制？
    三个条件任一成立即该步判定"Yes"。"可控制性"本身构成 Yes 的理由——即使危害不产生于此步。
    这防止"危害来源地"绑架"控制地点"，并保证每一步都被独立审视而非整体印象打分。
    可迁移为流程审计方法：逐节点问"引入/放大/可拦截"三问。
  tags: [step-wise-evaluation, introduce-grow-control, decision-rule]

- id: f1-13
  title: 每个 Yes 至少一控 + 一控多害
  type: framework
  source_chapter: Ch2 (2.5)
  source_quote: |
    "For every hazard you identify as requiring a preventive control, you must identify and
    implement at least one preventive control measure. ... Importantly, remember that more than
    one hazard may be addressed by a specific control measure. For example, several vegetative
    pathogens, such as Salmonella, L. monocytogenes, and E. coli O157:H7, are killed by cooking."
  summary: |
    双向映射规则：每个判为 Yes 的危害至少要有一个控制措施（无遗漏）；反之一个控制措施可以同时覆盖多个危害（不冗余）——如一次热处理同时杀灭沙门氏菌、李斯特菌、O157:H7。
    建立的是"危害—控制"多对多的覆盖矩阵，而非一一对应，资源效率与完备性兼得。
    验收标准：矩阵中不允许出现没有入边的危害节点。
    可迁移为任何风险治理的覆盖映射法（风险×对策矩阵、需求×测试用例矩阵）。
  tags: [mapping, coverage, one-control-many-hazards, completeness]

- id: f1-14
  title: 多组分界面微环境推理
  type: framework
  source_chapter: Ch3 (3.3.4.2.3)
  source_quote: |
    "Layering product components of significantly different pH or aw values alters the
    microenvironments at the interfaces of the components. A simple example is an eclair filled
    with a cream filling. The pH and aw at the interface of the pastry and the filling will be
    affected by the difference ... potentially resulting in an environment favorable to microbial
    growth."
  summary: |
    推理方法：整体性质安全 ≠ 各处安全。两种组分各自抑菌，但接触界面上 pH 与 a_w 会相互渗透，形成对微生物有利的"微环境"。
    因此评估必须问三个层次：各组分的参数 → 组合后整体平衡值 → 界面/装饰点局部值（如泡芙夹心、鹰嘴豆泥顶料）。
    通用化为"界面思维"：系统的薄弱点常出现在异质部分的交界处，而非任一部分内部。
    可迁移到材料腐蚀、组织接口、系统集成的失效分析。
  tags: [interface-thinking, microenvironment, multicomponent, reasoning-method]

- id: f1-15
  title: ROP 肉毒屏障判定与屏障组合（栅栏逻辑）
  type: framework
  source_chapter: Ch3 (3.3.4.2.4)
  source_quote: |
    "You should not use ROP unless barriers for C. botulinum are present. These barriers include:
    aw below 0.93; pH below 4.6; salt above 10%; thermal processing in the final container; and
    freezing with frozen storage and distribution. ... Combinations of barriers that individually
    would not control growth of C. botulinum can work together to prevent growth."
  summary: |
    采用某项技术（ROP）前先做屏障核对：五道独立屏障任一成立（a_w<0.93 / pH<4.6 / 盐>10% / 最终容器内热处理 / 冷冻储运）才允许使用。
    关键推理：单一屏障不达标不必然否决——多项弱屏障可组合成有效屏障（栅栏技术 hurdle technology）。
    背后的风险洞察是"先产毒后腐败"：ROP 抑制了需氧腐败菌（感官警讯），却给了厌氧产毒菌时间窗，因此不能用腐败迹象代替安全判定。
    可迁移为"启用新方案前先核对致命失效屏障"的准入清单思维。
  tags: [barrier-check, hurdle-technology, ROP, admission-criteria]

- id: f1-16
  title: 危害来源四分法 × 病原类型矩阵
  type: framework
  source_chapter: Ch3 (3.3, Table 3-2)
  source_quote: |
    "Food products can become contaminated with bacterial pathogens that can be: Ingredient-related
    hazards ...; Process-related hazards ...; Facility-related hazards ...; People-related hazards
    ... Table 3-2 is a Quick Reference Guide to help you identify potential pathogens by
    biological classification and potential sources or entry points in your facility."
  summary: |
    识别框架：把所有危害沿"来源（原料/工艺/设施/人员）× 类型（细菌/寄生虫/病毒）"二维展开成矩阵，每个格子填典型病原及其入口。
    用途：做危害识别时逐行扫描——原料带了什么、工艺会不会让它存活/增殖、环境会不会二次污染、人会不会带入。
    矩阵把"发散式头脑风暴"结构化为"入口枚举"，与 f1-03 的生命周期清单互补（一个按时间轴、一个按来源轴）。
    可迁移为通用的"来源×类型"风险盘点矩阵。
  tags: [matrix, hazard-sources, classification, quick-reference]

- id: f1-17
  title: 营养细胞 vs 孢子二分与"最抗性目标菌"推理
  type: framework
  source_chapter: Ch3 (3.3, 3.3.4.1)
  source_quote: |
    "Spores are not hazardous as long as they remain in the spore state. Unfortunately, spores are
    very resistant to heat, chemicals, and other treatments that would normally kill vegetative
    cells ... If the process is not designed to control the most resistant pathogen of concern in
    the food, pathogens may survive the treatment."
  summary: |
    杀灭类控制的推理路径：先区分目标对象是营养细胞还是孢子（孢子抗性远高，但休眠态无害）→ 识别食品中最具抗性的"目标病原"（pertinent pathogen）→ 按它设计工艺强度。
    隐含原则：工艺按最难杀的对象设计，而不是平均对象；对象不明确则工艺强度无从论证。
    配套事实：热处理不消除已形成的毒素——控制必须抢在毒素形成之前。
    可迁移为"按最坏目标设计"的鲁棒性思维（安全裕度、测试用例设计）。
  tags: [target-pathogen, spore-vs-vegetative, worst-case-design, lethality]

- id: f1-18
  title: Transient vs Resident 环境病原判定
  type: framework
  source_chapter: Ch3 (3.3.5.2)
  source_quote: |
    "pathogens may be present as 'transient' contamination or 'resident' contamination within the
    facility. ... the pathogens then become established in a harborage site, multiply, and persist
    for extended periods of time, even years. A harborage site, or niche, is a site ... that
    enables the accumulation of residues ... and permits the growth of microorganisms."
  summary: |
    环境检出阳性后的第一问：是 transient（随原料/人员/害虫带入，常规清洁即可清除，检出谱系多样）还是 resident（已定殖于 niche 藏匿点，持续数月甚至数年）？
    判定决定对策：transient→维持常规 CGMP；resident→强化卫生程序 + 深度排查藏匿点，常规 SSOP 无效。
    判定线索：同一种株型反复出现 = resident；每天检出的菌都不一样 = transient。
    可迁移为"偶发问题 vs 系统性问题"的分类思维：处置手段完全不同，误判会浪费资源或放任定殖。
  tags: [transient-vs-resident, niche, environmental-monitoring, classification]

- id: f1-19
  title: FSP↔HACCP 差异映射升级法（Table 1-1）
  type: framework
  source_chapter: Ch1 (1.4, 1.5)
  source_quote: |
    "Table 1-1 compares what is required for the elements of each type of plan. ... If you have an
    existing HACCP plan, you should determine if it satisfies all the PCHF requirements in part
    117. You can use existing programs, procedures, and records and supplement these with any
    additional information required, such as a supply-chain program."
  summary: |
    存量体系升级方法：不推倒重来，而是逐要素做新旧差异映射（危害分析/控制/监控/纠正/验证/验证确认/记录/召回计划 8 个要素各比一次），缺口处补充，满足处复用。
    升级方向的本质：从"仅 CCP 控制"扩展为"CCP + 非 CCP 控制点"，从"工艺控制"扩展为五类预防控制。
    价值：把"合规改造"变成有明确差异清单的增量工程，避免全盘重建的浪费与风险。
    可迁移为任何标准/框架迁移的 gap-mapping 方法（如旧认证→新认证、旧架构→新架构）。
  tags: [gap-mapping, migration, HACCP-to-FSP, incremental-upgrade]

- id: f1-20
  title: FSP 动态再分析触发器
  type: framework
  source_chapter: Ch1 (1.7)
  source_quote: |
    "The FSP is a dynamic document that reflects your current hazard analysis, preventive
    controls, and applicable procedures. The FSP as a whole must be reanalyzed at least every 3
    years. The reanalysis may be limited to the applicable portion of the FSP when you make
    changes to your system or equipment, when you become aware of new information about potential
    hazards ..., when there is an unanticipated food safety problem, or when you find that a
    preventive control ... is ineffective."
  summary: |
    文档不是一次性交付物：周期性触发（至少每 3 年全面再分析）+ 事件性触发（变更、新危害信息、意外问题、控制失效）双轨驱动更新。
    精妙之处：事件触发时允许只再分析"相关部分"——全量与增量的成本权衡被显式写入规则。
    本质是把"计划的时效性"制度化为触发器集合，防止计划与现实的静默漂移。
    可迁移为任何计划/文档的生命周期管理（应急预案年审、架构决策记录复审）。
  tags: [reanalysis-triggers, dynamic-document, periodic-plus-event-driven]

- id: f1-21
  title: 危害分析支点思维：分析做错则整个体系无效
  type: framework
  source_chapter: Ch2 (2.2)
  source_quote: |
    "If you do not conduct the hazard analysis correctly, and do not identify all hazards
    warranting preventive controls within the food safety plan, the food safety plan will not be
    effective in protecting consumers and preventing food safety issues, no matter how well your
    facility follows the plan."
  summary: |
    思维模型：危害分析是整个体系失效模式的根节点——执行再完美也无法弥补识别遗漏，"完美执行错误计划"仍是零。
    推论：资源分配应向分析阶段倾斜（好的团队、外部专家、充分信息），因为它是杠杆率最高的一环。
    同时明确了危害的边界：昆虫、毛发、腐败等质量缺陷不是 hazard，不进 FSP——定义先行，防止体系被无关事项稀释。
    可迁移为"上游判断决定下游一切"的优先级思维（需求分析、诊断先行）。
  tags: [foundational-thinking, leverage, hazard-analysis, scope-definition]

- id: f1-22
  title: 过程后添加配料危害检查
  type: framework
  source_chapter: Ch3 (3.3.4.3)
  source_quote: |
    "A facility that produces products containing ingredients added after a process control should
    consider the potential for the added components to be a process-related biological hazard as
    part of its hazard analysis."
  summary: |
    if-then 检查：IF 产品在设计上要在工艺控制（如杀菌）之后添加配料（坚果、果干、顶料、装饰）THEN 这些"绕过了杀伤步骤"的配料必须单独作为潜在危害评估。
    推理核心：工艺控制只保护它之前/之中的东西，在其之后进入的物料享受不到这层保护——"杀菌后添加"相当于该配料走的是无控制通道。
    防止的直觉错误："成品是熟的就安全"，忽视了后加组分从未被处理。
    可迁移为"保护屏障覆盖范围"检查：任何在防护措施之后加入的要素需重新评估。
  tags: [post-process-addition, coverage-gap, if-then-rule, hazard-check]

- id: f1-23
  title: 冷却窗口与竞争菌群消失推理
  type: framework
  source_chapter: Ch3 (3.3.4.2.2)
  source_quote: |
    "it is spores that survive the cooking process if they are present, and they begin to
    germinate when the product temperature begins to drop below 140°F. ... pathogenic spores that
    may be present are able to germinate, grow and possibly produce toxin due to the fact that
    most spoilage bacteria have been eliminated by the reduction step."
  summary: |
    因果链推理：热处理杀灭营养细胞和腐败菌 → 幸存孢子在冷却降至 140°F 以下时开始萌发 → 此时竞争者已被清除、营养gratis，幸存者反而比处理前长得更快 → 因此冷却阶段是独立的危害窗口，需要自己的控制。
    关键洞察：杀伤步骤会"清场"，让幸存者获得生态优势——处理过的食品比未处理的更怕时间温度滥用。
    与 f1-14 一起构成"工艺陷阱清单"：工序交接处（冷却、界面、后添加）比工序内部更危险。
    可迁移为"干预措施制造新风险窗口"的反思（抗生素杀死竞争菌后耐药菌定殖等）。
  tags: [cooling-window, competition-removal, unintended-consequence, process-trap]
