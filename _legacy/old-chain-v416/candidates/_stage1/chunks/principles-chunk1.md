# 原则提取候选 — 分块 1/6（第 1–3300 行：Introduction、Ch1、Ch2、Ch3 前半）

```yaml
- id: p1-01
  title: 设施必须编制并实施书面食品安全计划（FSP）
  type: principle
  source_chapter: Ch1 The Food Safety Plan (§1.1-1.2)
  source_quote: |
    "The PCHF requirements specify that a facility must prepare, or have prepared, and
    implement a written food safety plan. See 21 CFR 117.126."
  summary: |
    FSP 不是可选项：凡适用 PCHF 的设施必须"编制（或委托编制）+ 实施"一份书面 FSP。
    书面化是整个 117 部分合规的起点——口头或"实践中的做法"不算数。
    FSP 本身也是必须保存的记录（117.126(c)、subpart F）。
  tags: [principle, requirement, fsp, written-document]

- id: p1-02
  title: 危害分析无论结论如何都必须书面
  type: principle
  source_chapter: Ch1 §1.2 / Ch2 §2.1
  source_quote: |
    "This hazard analysis must be written, regardless of whether any hazards requiring a
    preventive control are identified." / "The hazard analysis must be written, regardless of
    the results of the analysis, and must include two elements: (1) a hazard identification
    and (2) a hazard evaluation."
  summary: |
    即使分析结论是"没有任何危害需要预防控制"，危害分析本身仍必须写成书面文件。
    危害分析必须包含两个要件：危害识别 + 危害评估，缺一不可。
    在本块内两次出现（Ch1 与 Ch2），是 FDA 有意强调的高频要求。
  tags: [principle, requirement, hazard-analysis, written-document]

- id: p1-03
  title: FSP 必须由 PCQI 编制或监督编制，PCQI 不必是本厂员工
  type: principle
  source_chapter: Ch1 §1.3
  source_quote: |
    "A 'preventive controls qualified individual' (PCQI) must develop (or oversee the
    development of) the FSP. ... The PCQI does not need to be an employee of the facility."
  summary: |
    FSP 的编制（或编制监督）责任法定归属 PCQI；PCQI 可通过 FSPCA 标准课程或工作经验取得资格。
    PCQI 不要求是内部员工——可以外聘，这为中小设施提供了合规路径。
    危害分析作为 FSP 的一部分同样须在 PCQI 监督下进行（117.126(a)(2)）。
  tags: [principle, requirement, pcqi, responsibility]

- id: p1-04
  title: FSP 必须由业主/经营者/负责人签署并注明日期——首次完成时和每次修改时
  type: principle
  source_chapter: Ch1 §1.3
  source_quote: |
    "The FSP must be signed and dated by the owner, operator or agent in charge of the facility
    when it is first completed and whenever the plan is modified (See 21 CFR 117.310.)"
  summary: |
    签署要求有两个触发时点：首次完成时、每次修改时——不能只在最初签一次。
    签署主体必须是 owner/operator/agent in charge，不能由 PCQI 代签。
    FSP 可以是散置的多份文件，签封面页或签"文件清单"（如目录页）均可满足要求。
  tags: [principle, requirement, signature, record]

- id: p1-05
  title: 未识别出需控危害时，FSP 可以只有危害分析一份文件
  type: principle
  source_chapter: Ch1 §1.2
  source_quote: |
    "If the hazard analysis does not identify any hazards requiring a preventive control, the
    only document in the FSP would be the hazard analysis."
  summary: |
    FSP 的规模与危害分析结论挂钩：结论为"无需控危害"时，危害分析即构成完整 FSP。
    这避免了"空转的预防控制程序"——没有 Yes 危害就不需要硬凑控制措施。
    与 p1-02 呼应：文件可以极简，但书面判定不可省略。
  tags: [principle, fsp, minimal-scope]

- id: p1-06
  title: "hazard"仅指能致病致伤的因素——虫害、毛发、腐败等质量缺陷不属于 FSP 范畴
  type: principle
  source_chapter: Ch1 §1.2
  source_quote: |
    "Many conditions are highly undesirable in food, such as the presence of insects, hair,
    filth or spoilage... Unless these conditions directly affect food safety, documents
    addressing these issues are not included in an FSP."
  summary: |
    食品安全语境下的 hazard 有严格边界：仅限有潜力致病或致伤的生物/化学（含放射）/物理因子。
    虫害、毛发、污物、腐败等应受控的质量缺陷，除非直接影响安全，否则不进 FSP。
    该区分决定文件边界：把质量问题塞进 FSP 会稀释资源；把安全问题当质量问题则会漏控。
  tags: [principle, definition-boundary, hazard, scope]

- id: p1-07
  title: 预防控制可施加于 CCP 以外的步骤——FSP 比 HACCP 覆盖面更宽
  type: principle
  source_chapter: Ch1 §1.4.1
  source_quote: |
    "In an FSP, preventive controls may be applied at CCPs, but also at points other than at
    CCPs. The FSP includes control measures that, under the HACCP approach, may have been
    included in prerequisite programs or CGMPs."
  summary: |
    与 HACCP 的核心差异之一：供应商控制、过敏原控制、卫生控制在 FSP 下都是正式的预防控制，
    而传统 HACCP 把它们放在前置程序/CGMP 里。
    非过程类预防控制可以不设关键限值（如卫生分区、供应商控制）——不强套 CCP 模式。
    存量 HACCP 企业升级的关键认知：从"CCP 为中心"扩展到"控制为中心"。
  tags: [principle, fsp-vs-haccp, preventive-control, ccp]

- id: p1-08
  title: 预防控制按"适当性"监控——非 CCP 控制可以不被监控
  type: principle
  source_chapter: Ch1 §1.4.2
  source_quote: |
    "In an FSP, preventive controls are only monitored as appropriate to the nature of the
    preventive control and its role in the facility's food safety system, and some preventive
    controls that are not applied at CCPs may not be monitored."
  summary: |
    HACCP 中 CCP 必须监控；FSP 中监控按控制的性质与角色"酌情"配置。
    这不是放松而是分层：工艺控制监控最密，卫生/供应商控制用验证活动替代部分监控。
    判断依据是"该控制在食品安全体系中的角色"，而非控制类型本身。
  tags: [principle, monitoring, fsp-vs-haccp, proportionality]

- id: p1-09
  title: 对某些预防控制，即时纠正（correction）比完整纠正措施更合适
  type: principle
  source_chapter: Ch1 §1.4.3
  source_quote: |
    "immediate corrections (e.g., re-cleaning and sanitizing a line before start-up of
    production when food residue remains after cleaning) may be more appropriate for some
    preventive controls than a specific corrective action involving product risk evaluations."
  summary: |
    FSP 提供纠正弹性：轻微、孤立、未波及产品安全的问题走 correction 路径，
    不必每次启动四步纠正措施程序（防复发/评估受影响食品/阻止入市）。
    典型场景：开工前清洁后仍有残留→重新清洁消毒即可。
    correction 与 corrective action 的边界问题在 Ch5 详细展开——这里是首次预告。
  tags: [principle, correction, corrective-action, flexibility]

- id: p1-10
  title: 部分预防控制不需要 validation（如卫生控制）
  type: principle
  source_chapter: Ch1 §1.4.5
  source_quote: |
    "The extent of validation activities may be less rigorous for some preventive controls than
    others, or may not be required (e.g., sanitation controls)."
  summary: |
    validation（科学/技术证据确认控制有效）主要针对工艺控制；卫生控制、过敏原控制、
    召回计划等不要求 validation，验证强度也分级。
    避免过度工程：不要为所有控制都做挑战性试验。
    "哪些控制需要 validation"是 FSP 设计中的分流决策点。
  tags: [principle, validation, proportionality, sanitation]

- id: p1-11
  title: 每个识别出需控危害的产品必须配备召回计划
  type: principle
  source_chapter: Ch1 §1.4.6
  source_quote: |
    "In an FSP, a Recall Plan must be prepared for each product for which a hazard requiring a
    preventive control has been identified."
  summary: |
    召回计划是 FSP 的法定组成（HACCP 无此要求），触发条件是"该产品识别出需控危害"。
    逐产品配备，不是全厂一份通用计划。
    召回计划本身也是一类预防控制（117.135(c)(5)）。
  tags: [principle, requirement, recall-plan]

- id: p1-12
  title: 存量 HACCP 计划可直接沿用，缺什么补什么
  type: principle
  source_chapter: Ch1 §1.5
  source_quote: |
    "If you have an existing HACCP plan, you should determine if it satisfies all the PCHF
    requirements in part 117. You can use existing programs, procedures, and records and
    supplement these with any additional information required, such as a supply-chain program."
  summary: |
    升级路径：先做差距评估（HACCP 计划是否满足 117 全部要求），再补缺（典型缺口是供应链程序）。
    现有程序、记录均可复用，不必推倒重来。
    与 Table 1-1 的差异映射配合使用效果最佳。
  tags: [principle, haccp-migration, gap-analysis]

- id: p1-13
  title: FSP 无标准化格式——任何格式均可，只要信息齐全
  type: principle
  source_chapter: Ch1 §1.6 / Introduction §V
  source_quote: |
    "There is no standardized or required format for an FSP. ... You can use whatever format
    works best for your facility, provided that the FSP includes all the required information."
  summary: |
    FDA 不规定 FSP 格式；指南展示的表格仅是示例。判定标准是"包含 117 要求的全部信息"。
    本块内两次出现（Introduction 与 Ch1），是 FDA 反复给企业的"免格式焦虑"承诺。
    可以用 FSPCA 表单，也可以自创格式或用书面叙述（narrative）。
  tags: [principle, format, flexibility, documentation]

- id: p1-14
  title: FSP 是动态文件：至少每 3 年整体再分析一次；触发事件时局部再分析
  type: principle
  source_chapter: Ch1 §1.7
  source_quote: |
    "The FSP is a dynamic document that reflects your current hazard analysis, preventive
    controls, and applicable procedures. The FSP as a whole must be reanalyzed at least every
    3 years. The reanalysis may be limited to the applicable portion of the FSP when you make
    changes to your system or equipment, when you become aware of new information about
    potential hazards..."
  summary: |
    数值界限：整体再分析周期 = 至少 3 年一次（117.170），这是 FSP 的"保质期"。
    四类触发事件可只做局部再分析：体系/设备变更、新危害信息、意外食品安全问题、控制无效。
    "动态文件"意味着 FSP 的价值在于持续维护，而非一次性通过检查。
  tags: [principle, numeric-boundary, reanalysis, 3-year]

- id: p1-15
  title: 指南中"should"仅表示建议，不构成强制要求
  type: principle
  source_chapter: Introduction §II
  source_quote: |
    "The use of the word should in FDA guidances means that something is suggested or
    recommended, but not required."
  summary: |
    阅读全书的关键解密规则：guidance 本身不创设法律责任，除非引用了具体法规/法律条款。
    涉及 21 CFR 条文引用（如 must + 条款号）的是硬要求；纯 should 是建议。
    读法规指南类文本时先分层"法定 vs 建议"，避免把建议当强制而过度合规。
  tags: [principle, meta-rule, reading-rule, should-vs-must]

- id: p1-16
  title: 危害分析应提供决策理由——书面理由是对检查质疑的防线
  type: principle
  source_chapter: Ch2 §2.2
  source_quote: |
    "Your hazard analysis should provide justification for your decisions. ... it can be a
    resource for you when you are asked by inspectors or auditors to justify why certain hazards
    were or were not included in your FSP."
  summary: |
    危害分析不只是内部工具，还是对抗外部审查的证据文件。
    书面理由的价值在检查员/审核员质疑"为什么没控这个危害"时兑现。
    "解释 No 与解释 Yes 同等重要"的操作基础就在这里。
  tags: [principle, justification, inspection-defense]

- id: p1-17
  title: 解释"No"与解释"Yes"同等重要
  type: principle
  source_chapter: Ch2 §2.3.2 (Column 4)
  source_quote: |
    "Explaining your reasons for a 'No' conclusion can be just as important as explaining your
    reasons for a 'Yes' conclusion."
  summary: |
    六列工作表的核心纪律：第 3 列写结论，第 4 列必须写理由——无论结论是 Yes 还是 No。
    "No"的书面理由决定了该危害被排除的合法性；空白即为漏洞。
    这是全块乃至全书反复出现的操作规则（Ch2 两次强调）。
  tags: [principle, operational-rule, no-justification, worksheet]

- id: p1-18
  title: 保守策略：把争议危害列入第 2 列并写明"No"理由
  type: principle
  source_chapter: Ch2 §2.3.2 (Column 2)
  source_quote: |
    "you may find it useful to take a conservative approach by listing in Column 2 several
    potential hazards even though they clearly do not require a preventive control (especially
    when there has been significant debate over whether something is actually a potential
    hazard for the facility), and explain the reasons for your 'No' conclusion."
  summary: |
    对争议大的危害，宁可列出来再论证排除，也不要干脆不列。
    好处：自查和他查时能直接展示"我们考虑过并排除了它"。
    这是"解释 No 与 Yes 同等重要"的具体操作手法。
  tags: [principle, checklist, conservative-approach, worksheet]

- id: p1-19
  title: 危害分析做错，整个 FSP 无论执行多好都无效
  type: principle
  source_chapter: Ch2 §2.2
  source_quote: |
    "If you do not conduct the hazard analysis correctly, and do not identify all hazards
    warranting preventive controls within the food safety plan, the food safety plan will not
    be effective in protecting consumers and preventing food safety issues, no matter how well
    your facility follows the plan."
  summary: |
    危害分析是全体系的阿基米德支点：识别失败=控制对象缺失=后续监控/验证全部空转。
    "no matter how well your facility follows the plan"——执行质量无法弥补分析质量。
    资源分配含义：在危害分析上投入的判断力回报最高。
  tags: [principle, hazard-analysis, foundation, leverage-point]

- id: p1-20
  title: 由多功能食品安全团队在 PCQI 监督下做危害分析
  type: principle
  source_chapter: Ch2 §2.3.1
  source_quote: |
    "we recommend that a Food Safety Team of individuals with expertise in the day-to-day
    operations of your facility conduct your hazard analysis under the oversight of a
    Preventive Controls Qualified Individual. The individuals may include personnel from
    production, sanitation, quality control, laboratory, and maintenance."
  summary: |
    危害分析不是 PCQI 一个人闭门造车：需要生产、卫生、QC、实验室、维修等多职能参与。
    多职能的价值是"对工艺流程和哪里会出错有完整理解"。
    PCQI 保留法定监督职责；团队提供现场知识。可补充外部专家。
  tags: [principle, team, hazard-analysis, collaboration]

- id: p1-21
  title: 危害分析前三项前置步骤：产品描述、流程图、详细工艺描述
  type: principle
  source_chapter: Ch2 §2.3.1
  source_quote: |
    "we recommend that you define and document the following details for the facility:
    - Product description, including its distribution, intended use, and identification of
    consumer or end user; - Process flow diagram; and - Detailed process description."
  summary: |
    PCHF 不强制但 FDA 强烈建议的前置步骤三件套。
    产品描述需含 RTE 属性、包装类型、储运条件、预期用途与目标人群（婴幼儿/老人/免疫低下
    人群决定更严格的控制）。
    详细工艺描述要覆盖环境暴露时长、手工操作、返工掺入等对危害分析有影响的细节。
  tags: [principle, preliminary-steps, product-description, flow-diagram]

- id: p1-22
  title: 流程图必须现场核实（onsite verification）
  type: principle
  source_chapter: Ch2 §2.3.1
  source_quote: |
    "You should verify the process flow diagram onsite in order to ensure no steps have been
    overlooked."
  summary: |
    流程图是危害分析的盘点清单——漏一步就漏一处危害评估。
    纸面流程图与车间实际必有偏差，必须到现场逐步核对。
    流程图应覆盖接收、储存、制备、加工、包装、储运全部步骤及所用设备。
  tags: [principle, verification, flow-diagram, onsite]

- id: p1-23
  title: 工厂有责任识别 Ch3/附录 1 之外的任何危害
  type: principle
  source_chapter: Ch2 §2.4.1
  source_quote: |
    "The hazards identified in Chapter 3 and in Appendix 1 do not represent an exhaustive list
    of hazards potentially associated with a food facility or food. You are responsible for
    identifying any hazard that may be associated with your process or product, even if it is
    not listed in Chapter 3."
  summary: |
    附录 1 的 X 标记和 Ch3 的危害知识库只是"建议评估的起点"，不是免责清单。
    判定责任永远在工厂本身——"表上没有"不能作为漏识别的抗辩。
    与 BOOK_OVERVIEW 核心命题 12 呼应："照表抄"会过度，"不看表"会违规。
  tags: [principle, responsibility, appendix1, hazard-identification]

- id: p1-24
  title: 识别出危害的步骤不必是控制它的步骤
  type: principle
  source_chapter: Ch2 §2.3.2 (Column 6) / §2.4.2.4
  source_quote: |
    "It is important to note that identifying a hazard at a processing step as one that
    requires a preventive control does not mean that the hazard must be controlled at that
    processing step."
  summary: |
    六列工作表第 6 列的设计逻辑：危害的"发现地"与控制的"施加地"可以分离。
    控制位置的选择标准是"在哪里控制最有效"，而非"在哪里发现"。
    本块内 Ch2 出现两次（Column 6 说明与 §2.4.2.4 结尾），是 FDA 刻意重复的关键规则。
  tags: [principle, operational-rule, control-location, worksheet]

- id: p1-25
  title: 危害评估双维度：严重性 × 无控制时的发生概率
  type: principle
  source_chapter: Ch2 §2.4.2
  source_quote: |
    "you must assess the severity of the illness or injury if the hazard were to occur and the
    probability that the hazard will occur in the absence of preventive controls."
  summary: |
    法定评估框架（117.130(c)(1)(i)）：每个潜在危害都要按严重性和概率两维评估。
    严重性看三因子：目标人群易感性、疾病规模与持续时间、继发问题（如 HUS、反应性关节炎）。
    概率看六因子：危害与食品/设施的关联频率、CGMP 有效性、制备方式、运输、储存、消费前处理。
    缺专业知识评估严重性时应咨询外部专家。
  tags: [principle, requirement, severity, probability, evaluation]

- id: p1-26
  title: 逐设施独立评估——同一产品在别的工厂的危害不必然是你的危害
  type: principle
  source_chapter: Ch2 §2.4.2.2
  source_quote: |
    "Hazards identified in one operation or facility may not be significant in another operation
    or facility producing the same or similar products because different equipment and processes
    may be used... You should consider each operation and facility location individually."
  summary: |
    禁止照抄同行危害分析：设备、工艺、原料来源不同，危害谱就不同。
    典型例子：玻璃瓶装 vs 塑料瓶装同一饮料，玻璃危害评估完全不同。
    "逐设施独立"是 117 体系对企业判断责任的再度确认。
  tags: [principle, facility-specific, no-copying, evaluation]

- id: p1-27
  title: RTE 食品暴露于环境且包装后无致死处理→环境病原评估是强制项
  type: principle
  source_chapter: Ch2 §2.4.2 / §2.4.2.3 (117.130(c)(1)(ii))
  source_quote: |
    "you must include an evaluation of environmental pathogens whenever an RTE food is exposed
    to the environment prior to packaging and the packaged food does not receive a treatment or
    otherwise include a control measure (such as a formulation lethal to the pathogen) that
    would significantly minimize the pathogen."
  summary: |
    唯一无条件的强制评估项：两条件（RTE + 包装前暴露 + 无后续灭活）同时成立即触发，
    没有商量余地。目标病原：L. monocytogenes、Salmonella、E. coli O157:H7。
    本块内出现 3 次（§2.4.2 清单、§2.4.2.3、§2.4.2.4 结尾），是本块重复度最高的要求。
    这是环境监测义务的逻辑源头。
  tags: [principle, mandatory, rte, environmental-pathogen, listeria]

- id: p1-28
  title: 评估危害时必须考虑 117.130(c)(2) 列举的十类因素
  type: principle
  source_chapter: Ch2 §2.4.2.4
  source_quote: |
    "When evaluating hazards, you must consider the effect of the following on the safety of the
    finished food for the consumer (21 CFR 117.130(c)(2)): - The formulation of the food...
    - The condition, function, and design of the facility and equipment... - Raw materials and
    other ingredients... - Transportation practices... - Manufacturing/processing procedures..."
  summary: |
    法定强制清单（must consider）：配方、设施/设备状况、原辅料、运输、加工步骤、包装与标签、
    储存分销、预期用途、卫生与员工健康、其他相关因素（如天气依赖性危害）。
    十类因素是查漏清单——评估记录中应能对应看到每类的考虑痕迹。
    每类因素都附有具体示例（如老设备→niches→强化卫生控制）。
  tags: [principle, requirement, checklist, evaluation-factors, 117-130c2]

- id: p1-29
  title: 多组分食品的界面微环境可推翻单组分的 a_w/pH 判断
  type: principle
  source_chapter: Ch2 §2.4.2.4 / Ch3 §3.3.4.2.3
  source_quote: |
    "A multicomponent food may have individual ingredients that do not support growth of
    undesirable microorganisms (e.g., because of pH or a w), but when put together there may be
    an interface where the pH and a w change (e.g., pies, layered breads)."
  summary: |
    安全陷阱：各组分单独看都抑制病原生长，组合后界面处 pH/a_w 重新分布，可能形成生长微环境。
    例子：奶油夹心酥皮——酥皮高 pH 低 a_w、夹心低 pH 高水分，界面处恰好 Favorable。
    本块内出现两次（Ch2 评估因素、Ch3 配方控制），是 FDA 强调的高频陷阱。
    评估多组分产品必须考虑成品均衡 pH/a_w 与各组分的差异、以及顶部装饰性配料的影响。
  tags: [principle, trap, multicomponent, interface, ph-aw]

- id: p1-30
  title: 每个"Yes"危害必须至少识别并实施一个预防控制
  type: principle
  source_chapter: Ch2 §2.5
  source_quote: |
    "For every hazard you identify as requiring a preventive control, you must identify and
    implement at least one preventive control measure. See 21 CFR 117.135. Importantly, remember
    that more than one hazard may be addressed by a specific control measure."
  summary: |
    Yes 结论的硬约束：第 5 列必须填控制措施并落实实施（117.135），不得留空。
    反向灵活：一个控制措施可覆盖多个危害（如烹饪同时杀灭 Salmonella、L. mono、E. coli O157:H7）。
    控制类型不限 CCP：供应链、过敏原、卫生、过程、其他控制均可。
  tags: [principle, requirement, preventive-control, one-to-many]

- id: p1-31
  title: 工艺控制可消除/预防危害的点应划为 CCP
  type: principle
  source_chapter: Ch2 §2.5
  source_quote: |
    "If a process control can be applied at a point or step in the food production process to
    prevent or eliminate the food safety hazard, or reduce it to an acceptable level, you should
    classify the point or step as a Critical Control Point (CCP)."
  summary: |
    CCP 的划入标准（而非划出）：工艺控制在某点能预防/消除/降至可接受水平→该点就是 CCP。
    FSP 保留 CCP 概念但收窄其范围——只针对工艺控制类。
    非 CCP 的预防控制（卫生/过敏原/供应链）不必套用 CCP 的关键限值模式。
  tags: [principle, ccp, classification, process-control]

- id: p1-32
  title: 危害分析越彻底，控制越精准，体系越有效
  type: principle
  source_chapter: Ch2 §2.5
  source_quote: |
    "The more thorough the hazard analysis, the more targeted your controls will be to ensure
    hazards are significantly minimized or prevented, and the more effective your food safety
    program will be in preventing illness or injury to consumers."
  summary: |
    投入产出逻辑链：分析深度→控制精度→体系有效性。
    与 p1-19 互为正反两面：分析不足则体系失效，分析充分则资源精准投放。
    识别控制措施时还应系统考虑 7 项：控制效果、监控可行性、控制位置、纠正措施、失败后果、
    消除还是减小、控制间协同效应。
  tags: [principle, thoroughness, resource-allocation, effectiveness]

- id: p1-33
  title: 已形成的毒素不会被后续热处理破坏——控制必须赶在产毒之前
  type: principle
  source_chapter: Ch3 §3.3.4.2.1
  source_quote: |
    "if the time and temperature abuse allows production of toxin, such as toxin production from
    S. aureus in temperature-abused custard pies, this toxin will not be destroyed by a heat
    step later in the process."
  summary: |
    时序规则：热处理能杀菌但不能灭毒素（S. aureus、B. cereus 肠毒素）——产毒一旦发生，
    后面的 kill step 救不回来。
    控制含义：产毒前的时间温度控制是独立于最终热处理的必要控制，不可用"反正后面会烤"
    来豁免前段管控。
    这是"热处理万能论"的法定否定。
  tags: [principle, toxin, timing, heat-treatment-limit]

- id: p1-34
  title: 致死步骤前的过度繁殖会使致死工艺失效
  type: principle
  source_chapter: Ch3 §3.3.4.2.1
  source_quote: |
    "Vegetative pathogens may grow in products during processing steps and may be ultimately
    destroyed by a lethal step such as cooking. However, too much bacterial growth before the
    lethal step may render the lethal process inadequate."
  summary: |
    致死工艺按"初始菌量"设计——前面的生长抬高了初始基数，固定 6D/5D 减少量后终点残留超标。
    烘焙面糊室温放置数小时即属此类场景（S. aureus 生长产毒+基数膨胀）。
    前段控制与最终致死步骤是串联关系，前段失守=全链失守。
  tags: [principle, growth-before-kill, process-design, timing]

- id: p1-35
  title: 孢子耐受性远超营养细胞——kill step 后仍需 pH/a_w/温度控制孢子菌
  type: principle
  source_chapter: Ch3 §3.3.1-3.3.2
  source_quote: |
    "when spores are a concern, the process steps used to kill them are often much more severe
    than those necessary to kill vegetative cells. ... other controls such as reduced pH or
    water activity (a w) or temperature control (refrigeration or freezing) may be needed to
    control sporeformers that remain after a kill step."
  summary: |
    孢子在休眠态无危害，但一旦发芽生长即成危害；常规致死工艺只杀营养细胞。
    kill step 清掉竞争菌后，幸存孢子反而获得"无菌竞争优势"，条件适合时更危险。
    控制策略：对 kill step 后仍存活的孢子菌，用 pH<4.6、低 a_w、冷藏/冷冻接力抑制。
  tags: [principle, spores, control-strategy, hurdles]

- id: p1-36
  title: 预防控制应基于目标病原的具体特性设计
  type: principle
  source_chapter: Ch3 §3.3
  source_quote: |
    "Because the characteristics of foodborne pathogens differ, the preventive controls that
    you identify and implement to control specific pathogens should be based on the
    characteristics of those specific pathogens."
  summary: |
    控制措施不能"一刀切"：抗热性、生长温度范围、a_w/pH 耐受因病原而异。
    设计前提是确定 pertinent pathogen（最难控制的目标病原）。
    附录 3 的生长极限表与 6D 表是这一原则的工具化。
  tags: [principle, pathogen-specific, design-basis]

- id: p1-37
  title: 工艺必须按目标病原中最耐受者设计（pertinent pathogen 规则）
  type: principle
  source_chapter: Ch3 §3.3.4.1
  source_quote: |
    "If the process is not designed to control the most resistant pathogen of concern in the
    food, pathogens may survive the treatment."
  summary: |
    致死工艺的设计基准不是"平均病原"而是"最难杀的那个"（抗热性最高者）。
    孢子 vs 营养细胞、不同菌种间抗性差异可达数量级（见附录 3 D 值表）。
    附件因素：酸性 pH 利于杀灭，糖和油会屏蔽热效应，水分存在利于破坏——设计时须计入。
  tags: [principle, pertinent-pathogen, design-basis, heat-resistance]

- id: p1-38
  title: 致死量必须达到食品冷点（cold spot）
  type: principle
  source_chapter: Ch3 §3.3.4.1
  source_quote: |
    "Bacterial pathogens in the cold spot of the food will be inactivated more slowly than those
    at the surface because those in the cold spot are subjected to less heat. If the minimum
    process for lethality is not achieved at the cold spot, pathogens may survive the treatment."
  summary: |
    热处理的验证点在冷点而非表面：表面先热，冷点受热最少、灭菌最慢。
    冷点未达最低致死工艺→病原存活，整个处理作废。
    这为 Ch6/Ch9 的热分布研究（cold spot 定位）埋下伏笔。
  tags: [principle, cold-spot, lethality, heat-treatment]

- id: p1-39
  title: pH<4.6 可将 C. botulinum 排除出需控危害
  type: principle
  source_chapter: Ch3 §3.3.4.2.3
  source_quote: |
    "a naturally acidic product with a pH below 4.6 may rule out C. botulinum as a hazard
    requiring a preventive control, since this pH will prevent spore germination, growth, and
    toxin production."
  summary: |
    数值判据：pH<4.6 抑制 C. botulinum 孢子发芽、生长和产毒，可作为排除该危害的依据。
    这是酸化食品体系（pH 4.6 分界）在 PCHF 中的对应锚点。
    注意措辞是"may rule out"——仍需结合配方整体（如界面效应）评估。
  tags: [principle, numeric-boundary, ph-4-6, botulinum]

- id: p1-40
  title: 不得使用 ROP，除非存在 C. botulinum 屏障（五大屏障清单）
  type: principle
  source_chapter: Ch3 §3.3.4.2.4
  source_quote: |
    "You should not use ROP unless barriers for C. botulinum are present. These barriers
    include: a w below 0.93; pH below 4.6; salt above 10%; thermal processing in the final
    container; and freezing with frozen storage and distribution."
  summary: |
    减氧包装（ROP）的准入门槛：五屏障至少居其一——a_w<0.93、pH<4.6、盐>10%、最终容器内
    热处理、冷冻+冷冻储运。
    每个屏障单独即足以控制 C. botulinum 生长；单个不足的屏障可组合生效。
    这是"包装方式选择"层面的硬规则。
  tags: [principle, numeric-boundary, rop, barriers, botulinum]

- id: p1-41
  title: 温度不得作为 ROP 的唯一控制
  type: principle
  source_chapter: Ch3 §3.3.4.2.4
  source_quote: |
    "Refrigeration below 38°F (3.33°C) can prevent growth of all strains of C. botulinum, but
    because temperatures above this are commonly employed for refrigeration, temperature should
    not be relied on as the only control."
  summary: |
    数值与规则：3.33°C（38°F）以下可抑制全部 C. botulinum 菌株，但常规冷藏温度普遍高于此值。
    因此冷藏不能单独作为 ROP 的肉毒屏障，必须叠加其他屏障。
    单一防线思维在温度依赖型控制中被明确否定。
  tags: [principle, numeric-boundary, rop, single-point-of-failure]

- id: p1-42
  title: ROP 陷阱：可能"先产毒、后腐败"——无感官警讯
  type: principle
  source_chapter: Ch3 §3.3.4.2.4
  source_quote: |
    "Lower oxygen levels favor pathogens that can grow in the absence of oxygen over the aerobic
    spoilage organisms that require oxygen for growth. For this reason, you may get toxin
    production before you get spoilage - something that is less likely to happen in traditional
    packaging."
  summary: |
    ROP 抑制需氧腐败菌的同时选择了厌氧病原菌——腐败征兆（感官报警器）被消除。
    结果：食品闻起来/看起来正常，毒素已经产生；货架期延长还为产毒提供了更多时间。
    这解释了为什么 ROP 需要屏障而不是仅靠"卖出前没问题"。
  tags: [principle, trap, rop, no-sensory-warning]

- id: p1-43
  title: 工艺控制之后添加的配料必须作为过程相关生物危害评估
  type: principle
  source_chapter: Ch3 §3.3.4.3
  source_quote: |
    "A facility that produces products containing ingredients added after a process control
    should consider the potential for the added components to be a process-related biological
    hazard as part of its hazard analysis."
  summary: |
    "kill step 之后加料"（沙拉包坚果果干、烘焙品顶部装饰）等于把未处理原料直接混入已灭菌产品。
    这些后加配料的病原负载不受前面的工艺控制保护，需独立评估其危害。
    评估要点：后加配料的来源控制（供应链）、或对后加步骤本身施加控制。
  tags: [principle, post-process-ingredients, hazard-analysis, trap]

- id: p1-44
  title: 容器完整性缺失是包装后再污染的主因（缺陷封口+污染冷却水）
  type: principle
  source_chapter: Ch3 §3.3.4.4
  source_quote: |
    "The primary causes of recontamination of foods after a process control step and packaging
    are defective container closures and contaminated cooling water. ... Contaminated cooling
    water can enter through the container closure, especially if the closure is defective."
  summary: |
    灭菌后的食品仍可能因包装环节失守被再污染：封口缺陷 + 冷却水入侵是两大通道。
    机理：水浴冷却时容器内形成负压，污染冷却水经缺陷封口被"吸"入。
    主要威胁病原：C. botulinum、L. mono、E. coli O157:H7、Salmonella、S. aureus、B. cereus。
  tags: [principle, container-integrity, recontamination, cooling-water]

- id: p1-45
  title: CGMP 甚至 CGMP+HACCP 也不能保证环境再污染不发生→需要卫生控制+环境监测
  type: principle
  source_chapter: Ch3 §3.3.5
  source_quote: |
    "experience has shown that application of CGMPs - even in combination with a HACCP plan -
    cannot guarantee that contamination of a processed food from the environment will not occur."
  summary: |
    经验性断言：CGMP+HACCP 的组合在环境再污染问题上不是充分防线。
    法律后果：环境病原为需控危害时，卫生控制（117.135(c)(3)）+ 环境监测（含取样检测）
    成为法定配置。
    这是环境监测从"最佳实践"升格为"义务"的论证逻辑。
  tags: [principle, environmental-monitoring, sanitation-control, gmp-limit]

- id: p1-46
  title: 瞬时污染 vs 定殖（resident）污染——定殖菌可存活数年，常规清洁无效
  type: principle
  source_chapter: Ch3 §3.3.5.2
  source_quote: |
    "Bacterial pathogens causing resident contamination can also be introduced into the
    processing facility, where the pathogens then become established in a harborage site,
    multiply, and persist for extended periods of time, even years."
  summary: |
    二分法：瞬时污染=随原料/人员/害虫进入、常规 CGMP 清洁可控；定殖=藏匿于 niche
    （接缝、裂缝、孔洞、死角）持续数月至数年。
    niche 难以检查和触及，能保护病原躲过常规清洁——这就是环境监测存在的微生物学依据。
    区分两者决定响应策略：瞬时→常规 SSOP 即可；定殖→强化卫生程序+根除调查。
  tags: [principle, transient-vs-resident, niche, sanitation-strategy]

- id: p1-47
  title: 附录 3 生长极限数据来自实验室培养基极端值，未必适用于你的工艺条件
  type: principle
  source_chapter: Ch3 §3.3.1 / §3.3.2（Table 3-A 警示）
  source_quote: |
    "Data shown are the minimum or maximum values - i.e., the extreme limits reported among the
    references cited. These values may have been obtained in laboratory media, which may be more
    favorable to growth than many foods. These values may not apply to your specific processing
    conditions."
  summary: |
    使用速查表的安全阀：Table 3-A 数值是文献极端值（最耐/最敏感端），且多来自实验室培养基。
    直接当设计依据有双面风险：过于保守（过度控制）或失真（培养基比真实食品更利于生长）。
    本块内出现两次（营养细胞节与孢子节开头），是 FDA 对速查工具的一致性警示。
  tags: [principle, caveat, appendix3, data-limitation]

- id: p1-48
  title: 确保合规的责任必须明确分配给具备资质的主管人员
  type: principle
  source_chapter: Introduction §V Training (117.4(c))
  source_quote: |
    "responsibility for ensuring compliance by individuals with the requirements of part 117
    must be clearly assigned to supervisory personnel who have the education, training, or
    experience (or a combination thereof) necessary to supervise the production of clean and
    safe food."
  summary: |
    法定要求（117.4(c)）：合规监督责任要"明确分配"（clearly assigned）给有资质的主管。
    不能是模糊的"人人有责"——必须落到具名的、具备教育培训或经验的主管头上。
    与 PCQI 制度呼应：体系的责任链是 owner→PCQI→supervisory personnel→qualified individuals。
  tags: [principle, requirement, accountability, supervision]

- id: p1-49
  title: 培训按岗位职责配置——各类人员各有明确的最低培训内容
  type: principle
  source_chapter: Introduction §V Training
  source_quote: |
    "All personnel who enter production areas should have adequate training about the importance
    of health and hygiene... Personnel with responsibilities for purchasing should have adequate
    training regarding the importance of applicable food safety specifications and supply-chain
    controls..."
  summary: |
    FDA 给出按角色的培训地图：进入生产区者（卫生）、采购（规格与供应链控制）、收货（验货与
    储存条件、生熟/过敏原隔离）、维修（污染与交叉接触风险）、清洁消毒（各步骤与异常处置）、
    生产的（各步骤重要性与异常处置）、环境取样与检测人员（操作规程）、主管（FSP 相关程序）、
    厂管理层（FSP 全貌）。
    判断标准统一为"adequate"——与职责相称。
  tags: [principle, checklist, training, role-based]

- id: p1-50
  title: FSP 及其实施记录必须保存
  type: principle
  source_chapter: Ch1 §1.2
  source_quote: |
    "This written FSP is a record that you must maintain. See 21 CFR 117.126(c) and 21 CFR part
    117, subpart F... In addition, you must maintain records to document that you are
    implementing the FSP."
  summary: |
    两层记录义务：FSP 文件本身是记录（117.126(c)、subpart F）+ 实施 FSP 的证明记录（117.190）。
    只有计划没有实施记录 = 体系未运转；记录是"做过"的唯一证据形式。
    本规则贯穿后续管理组件章节（监控/纠正/验证各有记录要求）。
  tags: [principle, requirement, records, implementation]

- id: p1-51
  title: 逐个加工步骤独立评估危害（三条件判定）
  type: principle
  source_chapter: Ch2 §2.4.2.2.4
  source_quote: |
    "You should evaluate the potential hazards independently at each processing step to
    determine whether you should identify that hazard as one requiring a preventive control...
    if: it is reasonably likely that the hazard can be introduced at an unsafe level at that
    processing step; or... increase to an unsafe level at that processing step; or the hazard
    was identified in an ingredient or at another... step and it can be controlled at the current
    processing step."
  summary: |
    "Yes"的三个充分条件（任一成立即 Yes）：①该步会以不安全水平引入危害；②该步危害会增长至
    不安全水平；③危害在别处识别出但可在本步被控制。
    第三条与 p1-24（控制位置可分离）衔接。
    评估时还须结合分销储存方式、预期用途与消费者（前置步骤的产出）。
  tags: [principle, decision-rule, per-step, evaluation]

- id: p1-52
  title: FSP 应针对自身产品与操作量身定制
  type: principle
  source_chapter: Introduction §II
  source_quote: |
    "We recommend that you consider how this guidance relates to each of your operations and
    tailor your FSP to the specific circumstances for the foods you process."
  summary: |
    指南的定位是"通用参考"，企业必须做"指南→自身操作"的映射转化。
    禁止照搬示例工厂（Cookie A、Soup A 等）的参数而不做适用性论证。
    与 p1-26（逐设施独立评估）、p1-23（表外危害责任）构成同一责任 philosophy 的三个侧面。
  tags: [principle, tailoring, no-copying]

- id: p1-53
  title: 配方参数可协同构成抑制病原的"生态系统"（hurdle technology）
  type: principle
  source_chapter: Ch3 §3.3.4.2.3
  source_quote: |
    "Formulation parameters such as pH, a w, use of preservatives, and oxygen availability, can
    work in concert to establish an ecosystem that is designed to inhibit the growth of the
    pathogens that may be present."
  summary: |
    多屏障协同：pH、a_w、防腐剂、氧可用性可单独不足、组合充分（栅栏技术）。
    Ch2 §2.5 亦提到"协同效应"（配方控制联合防腐+酸化+低 a_w 个别不控、合起来控）。
    应用含义：评估配方控制时看整体屏障体系而非单参数达标。
    但必须警惕 p1-29 的界面微环境对"组合效果"的破坏。
  tags: [principle, hurdle-technology, formulation, synergy]

- id: p1-54
  title: 烹后冷却至 140°F 以下时幸存孢子开始发芽
  type: principle
  source_chapter: Ch3 §3.3.4.2.2
  source_quote: |
    "it is spores that survive the cooking process if they are present, and they begin to
    germinate when the product temperature begins to drop below 140°F."
  summary: |
    数值界限：140°F（60°C）是冷却段孢子发芽的起始温度阈值——冷却程序的干预点。
    烹后食品的主要威胁从营养细胞切换为孢子（C. perfringens、B. cereus、non-proteolytic
    C. botulinum）。
    冷却太慢=孢子在危险温区停留过久→发芽生长产毒；部分孢子甚至能在冷藏温度下缓慢发芽。
  tags: [principle, numeric-boundary, cooling, 140f, spores]

- id: p1-55
  title: 工艺设计与监控应覆盖"计划外"的过程相关危害
  type: principle
  source_chapter: Ch3 §3.3.4
  source_quote: |
    "Some process-related biological hazards can occur if something goes wrong with a process
    control. ... Other process-related biological hazards are not related to something going
    wrong with a process control. For example, if you plan to use reduced oxygen packaging (ROP)
    to prevent the growth of spoilage organisms and extend the shelf life..."
  summary: |
    过程相关危害分两类：①控制失效型（欠火候、冷却不当、配方失误）；②设计内固有型
    （ROP 延长货架期、后加配料、容器完整性）。
    第二类尤其容易被漏掉——它们不是"出错"的结果，而是正常运营的副产品。
    危害识别时必须两类都问：哪里可能出错 + 哪里是设计本身引入的风险。
  tags: [principle, hazard-identification, by-design, process-related]
```

## 自检

- [x] 每条都是"可直接应用的规则/断言"，非思维结构
- [x] 有明确原文依据（均为本块 1–3300 行内摘录）
- [x] 引用 ≤100 英文单词（长清单类条目做了截断并保留核心句）
- [x] 不做筛选（55 条，宁滥勿缺）
- [x] 术语定义类内容未收录（归 glossary-extractor）；案例/暴发史未收录（归 case-extractor）
- [x] "反复出现"判断仅基于本块：p1-02（2次）、p1-07（Ch1 多处）、p1-13（2次）、p1-24（2次）、p1-27（3次）、p1-29（2次）、p1-47（2次）
