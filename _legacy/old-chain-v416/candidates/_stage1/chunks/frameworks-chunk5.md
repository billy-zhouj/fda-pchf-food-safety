# Frameworks — Chunk 5 (lines 13201–16500, Ch12 尾部 / Ch14 召回 / Ch15 供应链 / Ch16 酸化食品)

> 提取员：framework-extractor 分块 5/6。不做筛选（宁错杀），阶段 1.5 去重。
> "是否反复出现"判断仅限本段。

```yaml
- id: f5-01
  title: 条件性升格思维模型（危害分析结论不是静态的）
  type: framework
  source_chapter: Ch12 §12.12（Miller C DON 案例链）
  source_quote: |
    "The outcome of Miller C's hazard analysis is that the hazard of DON in wheat RACs is not a hazard
    requiring a preventive control unless the available information (such as the test results for incoming
    RACs and milled wheat products associated with 'new crop' wheat or USDA's weekly reports) indicate the
    potential for higher levels of DON than expected. When the potential for higher than expected levels of
    DON is indicated, Miller C: implements its physical cleaning processes as a preventive control and
    maximizes use of the electronic color sorter..."
  summary: |
    同一套危害分析结论可以带条件：基线条件下某危害"不是需预防控制的危害"，
    但当外部信息（新收获季初批检测、USDA 周报、地堆储存、检出率上升）显示
    风险可能升高时，原本作为 CGMP 运行的程序要即时升格为预防控制（process control），
    并配套加强验证（加大检测频次）、纠正措施和记录。
    思维结构：把危害分析结论写成"默认态 + 触发条件 + 升格动作"的三段式，
    而非一次性的是/否判定。这是"危害分析是活的文档"的具体操作化。
    同一逻辑沿供应链向下传递（Miller C→Baker D→Sandwich F），每个环节
    都在采购协议里预埋"信息恶化时的联动条款"。
  tags: [mental-model, conditional-escalation, dynamic-analysis, mycotoxin]

- id: f5-02
  title: 跨层级验证传递（评估上游对上游的控制方案）
  type: framework
  source_chapter: Ch12 §12.14（Sandwich Maker F）/ Ch15 §15.7.4.2
  source_quote: |
    "As part of its process for entering into purchase agreements with suppliers of pre-sliced bread,
    Sandwich Maker F reviews the procedures, processes, and practices applicable to the supplier's
    evaluation of the adequacy of the miller's program to control the level of DON in milled wheat
    products, including whether and how the miller adapts its program when the potential for higher than
    expected levels of DON in wheat RACs is indicated."
  summary: |
    当危害由供应链更上游控制时，下游不直接验证控制者，而是审查自己的直接供应商
    "如何评估其上游控制是否充分"——即验证供应商的验证体系，而非验证控制本身。
    三级案例链中每一环都只看上一环：Sandwich F 审 Baker D 对 miller 程序的评估，
    Baker D 审 Miller C/E 的检测与升格机制。
    这是"信任但要验证验证者"（trust but verify the verifier）的分层结构，
    可迁移到任何多层外包/多级供应商管理场景。
  tags: [supply-chain, verification, layered-assurance]

- id: f5-03
  title: 按供应商能力定制契约化验证（差异化管理协议）
  type: framework
  source_chapter: Ch12 §12.13（Baker D）
  source_quote: |
    "When the miller's procedures, processes, and practices include a program for analytical testing for DON
    (which is the case for Miller C), Baker D reviews those test results to confirm that the levels of DON are
    consistent with the FDA advisory level before entering into a purchase agreement... When the miller's
    procedures, processes, and practices do not include a program for analytical testing for DON (which is the
    case for Miller E), Baker D arranges for analytical testing on several shipments of flour from that miller..."
  summary: |
    面对控制同一危害、但能力不同的两个供应商，采购方不在合同里复制同一套条款，
    而是按对方现有程序设计差异化协议：
    有检测程序的（Miller C）→ 审其检测结果 + 约定"信息恶化时可按批索要 COA"；
    无检测程序的（Miller E）→ 签约前自己安排多批检测确认基线 + 预埋
    "接受与否以 DON 检测结果为条件"的附加验收标准（可由任一方检测）。
    思维结构：把验证要求写进合同变成"条件触发的权利"，缺什么补什么，
    而不是一刀切或放弃合作。
  tags: [decision-framework, contracting, supplier-management]

- id: f5-04
  title: 召回四程序框架（通知/警告/核查/处置）
  type: framework
  source_chapter: Ch14 §14.3
  source_quote: |
    "the written recall plan must include procedures that describe the steps to be taken, and assign
    responsibility for taking those steps, to perform the following actions as appropriate to the facility:
    Directly notify the direct consignees of the food being recalled...; Notify the public about any hazard
    presented by the food when appropriate to protect public health; Conduct effectiveness checks to verify
    that the recall is carried out; and Appropriately dispose of recalled food—e.g., through reprocessing,
    reworking, diverting to a use that does not present a safety concern, or destroying the food."
  summary: |
    召回计划的骨架是四个动作，每个动作既要写"怎么做"（程序），又要写"谁来做"（责任分配）：
    ① 直接通知直接收货人（含退回/处置方式）；② 必要时通知公众；
    ③ 有效性核查（确认召回确实执行到位）；④ 召回食品的处置（再加工/改用途/销毁）。
    注意"有效性核查"是一个独立的闭环步骤——发出通知不等于召回完成，
    必须回头确认每一层收货人都收到通知并采取了行动。
    可迁移为任何危机响应预案的四步模板：通知→升级→核查执行→处置善后。
  tags: [recall, crisis-response, decision-framework]

- id: f5-05
  title: 书面召回通讯 6 要素
  type: framework
  source_chapter: Ch14 §14.5.1
  source_quote: |
    "Proactively address the questions that direct consignees are likely to have by describing in detail the
    components to be included in your written recall communication (e.g., identify the food, explain the reason
    for the recall, specify the depth of the recall, provide instructions for what direct consignees should do
    with the food, and make it easy for recipients to communicate with you); and Include model letters that you
    would modify based on the specific situation that warranted the recall."
  summary: |
    召回通讯写什么？六个要素：① 准确识别食品（品名/规格/批号/代码/保质期，附标签）；
    ② 简明解释召回原因和健康危害；③ 说明召回深度（批发/零售/消费者层）；
    ④ 给收货人的具体指令（下架/停发/转通知其客户/退回/未退回部分怎么销毁）；
    ⑤ 让对方容易回复你（免费电话、预付邮资回执卡、回复表）；⑥ 预置模板信函，
    届时按实际情况修改即可发出。
    思维结构：事先站在"接收方会问什么"的角度写模板，把危机时的即时写作
    变成填空题；且电话通知必须用书面确认兜底。
  tags: [recall, communication, checklist, template-thinking]

- id: f5-06
  title: 公众警告判定标准（最后手段原则）
  type: framework
  source_chapter: Ch14 §14.5.2
  source_quote: |
    "public warnings are used to alert the public that a food being recalled presents a serious hazard to
    health. A public warning is reserved for urgent situations where other means of preventing use of the
    recalled product appear inadequate... Your recall plan should describe your criteria for determining
    whether a public warning is appropriate."
  summary: |
    通知公众不是召回的默认动作，而是有门槛的最后手段，判定标准是：
    召回食品构成严重健康危害 + 其他阻止产品使用的手段都不够用。
    两者同时满足才动用新闻媒体发布公众警告；FDA 执法报告的公开列表
    不等于公众警告，不以紧迫性为前提。
    思维结构：把"要不要公开发声"从事后争论变成事前标准——
    在计划里预先写明自己的判定准则和发布步骤，危机时按标准执行而非临场博弈。
  tags: [decision-framework, public-warning, proportionality]

- id: f5-07
  title: 召回管理团队责任分配框架
  type: framework
  source_chapter: Ch14 §14.6
  source_quote: |
    "Identify members (and alternate members) of a recall management team, headed by a recall coordinator...
    those with responsibilities for distribution, production and quality assurance, consumer affairs,
    accounting, legal counsel, public relations, technical, marketing, and regional sales managers and
    staffs... Specify who is responsible for the decision to conduct a recall."
  summary: |
    召回预案的组织维度：指定一名召回协调员统筹并记录全部召回活动，
    按职能分配成员（分销：停发与召回统计；生产/质保：批次识别、停产、查记录确定
    是否扩大召回范围；消费者事务：应对咨询；公关：新闻稿与媒体；营销/区域销售：
    通知客户与零售端取货），每个成员配替任者，并写明姓名/职务/电话/邮箱/
    非工作时间联系方式/职责，且明确"由谁决定发起召回"。
    思维结构：危机响应的关键不是临时组建团队，而是预先把决策权、
    执行权和备份人写死在纸上——决策人尤其要单独指定。
  tags: [crisis-response, roles, decision-framework]

- id: f5-08
  title: 严重危害三重联动判定（SAHCODH ↔ Class I 召回 ↔ reportable food）
  type: framework
  source_chapter: Ch14 §14.2.1 / Ch15 §15.11.2.1
  source_quote: |
    "SAHCODH hazards are those for which a recall of a violative product posing such a hazard is designated
    as 'Class 1' under 21 CFR 7.3(m)(1) (i.e., a situation in which there is a reasonable probability that the
    use of, or exposure to, a violative product will cause serious adverse health consequences or death)...
    Foods (other than dietary supplements or infant formula) containing a SAHCODH hazard are considered
    'reportable foods,' subject to the Reportable Food Registry requirements..."
  summary: |
    "暴露后有合理概率导致严重健康后果或死亡"（SAHCODH）这一个判定，
    同时锚定三套制度：召回分级中的 Class I、报告性食品（RFR）义务、
    以及供应链计划中最严格的"首用前+每年现场审核"要求。
    思维结构：不要对同一风险反复做独立判断——找到那个贯穿性的严重度定义，
    一次判定，多处联动生效（监管端如此，企业内控亦可如此设计）。
  tags: [mental-model, classification, linkage, SAHCODH]

- id: f5-09
  title: RFR 24 小时报告规则
  type: framework
  source_chapter: Ch14 §14.7.1
  source_quote: |
    "A ''reportable food'' is an article of food (other than dietary supplements or infant formula) for which
    there is a reasonable probability that the use of, or exposure to, such article of food will cause serious
    adverse health consequences or death to humans or animals... food firms that are ''responsible parties''
    ... are required to notify FDA electronically with certain information within 24 hours of determining that
    a food they manufactured, processed, packed, or held is a reportable food."
  summary: |
    一旦判定自己的食品是"报告性食品"（合理概率造成严重健康后果或死亡），
    责任方必须在 24 小时内向 FDA 电子报告。指南建议把 RFR 合规程序
    （或交叉引用）纳入召回计划，让召回团队随时能取用——因为召回期间时间就是一切。
    思维结构：对"判定成立→报告义务启动"设置硬性时钟（24h），
    并把触发后的动作程序预先放进预案而非事后查找。
  tags: [regulatory, reportable-food, time-bound, recall]

- id: f5-10
  title: 比例原则：风险越大，验证越严、越频
  type: framework
  source_chapter: Ch15 §15.7.4.1
  source_quote: |
    "when the hazard is one for which there is a reasonable probability that exposure to the hazard will cause
    serious adverse health consequences or death, in general you must conduct an annual onsite audit before
    using the raw material or other ingredient from the supplier and at least annually thereafter... For other
    hazards, the determination of supplier verification activities, and the frequency of conducting those
    activities, also should be risk-based – i.e., the greater the risk presented by the hazard, the more robust
    the verification activity, and the greater the frequency of the verification."
  summary: |
    供应链验证投入不是均一的，而是与危害风险的严重度×概率成比例的连续谱：
    SAHCODH 危害一端锁定"每年现场审核"的硬底线；其他危害则按风险大小
    自由选择验证活动的强度（审核/检测/文件审查/问卷）和频次。
    同一原则还反向应用于绩效评估：危害风险越大，对供应商绩效的审查越要严格。
    这是整章的元规则——一切具体要求都是这条比例原则的特例。
  tags: [proportionality, risk-based, mental-model, supply-chain]

- id: f5-11
  title: 四种供应商验证活动工具箱
  type: framework
  source_chapter: Ch15 §15.7.2
  source_quote: |
    "Section 21 CFR 117.410(b) of subpart G specifies four appropriate supplier verification activities for
    raw materials and other ingredients... Onsite audits; Sampling and testing of the raw material or other
    ingredient; Review of the supplier's relevant food safety records; [and] Other appropriate supplier
    verification activities based on supplier performance and the risk associated with the raw material or
    other ingredient."
  summary: |
    验证供应商的手段是一个四格工具箱：① 现场审核（看得最全：计划+实施+记录+访谈）；
    ② 原料抽样检测（可周期或逐批，注意抽样局限）；③ 审查供应商的相关食品安全记录
    （含其对其上游的审核/检测记录）；④ 其他基于供应商表现和原料风险的自行设计活动
    （如事实型问卷、审计方案证书信息、不审核年份的环境监测记录替代）。
    第四格是开放式设计空间——法规只框定前三格，第四格交给企业按风险自造。
    选择哪几种、组合方式和频次由 4 因素判定（见 f5-12）。
  tags: [toolbox, verification, supply-chain]

- id: f5-12
  title: 批准供应商与定验证活动的 4 因素判定
  type: framework
  source_chapter: Ch15 §15.7.4
  source_quote: |
    "Section 21 CFR 117.410(d)(1) specifies factors that you must consider in approving suppliers and
    determining appropriate supplier verification activities (including determining the frequency of conducting
    the activity)... the requirement to consider each of these factors applies every time you approve a supplier
    ... The [four factors are]: hazard analysis; entity controlling the hazard; supplier performance; [and]
    other factors (such as storage and transportation practices)."
  summary: |
    每次批准供应商、每次确定验证活动及其频次，都要过同一组四因素：
    ① 危害分析（严重性×概率决定验证强度）；② 谁在控制危害
    （直接供应商还是其上游，决定验证指向谁）；③ 供应商表现
    （程序/规程、法规合规史如警告信与进口警报、食品安全史如检测结果/审核结果/整改响应）；
    ④ 其他因素（储运条件、集团内部知识等）。
    附一条便利例外：供应商是 qualified facility / 非 covered farm / <3000 只蛋鸡的蛋场时，
    因素③可缩小为只看合规历史。
    思维结构：把"凭印象选供应商"变成每次都要走一遍的结构化判定。
  tags: [decision-framework, supplier-approval, four-factors]

- id: f5-13
  title: 控制主体定位：验证追着控制者走
  type: framework
  source_chapter: Ch15 §15.7.4.2 / §15.6.4
  source_quote: |
    "the second factor... is the entity or entities that will be applying controls for the hazards requiring a
    supply-chain-applied control... If the control is not applied by your direct supplier, you would direct your
    supplier verification activities to your supplier's supplier, but there is some flexibility in how you could
    do this."
  summary: |
    危害的实际控制者可能不是你的直接供应商（例：调味料商 X 只是混合，
    杀菌过程在其上游的奶粉厂 Y 和香料厂 Z）。此时验证活动要指向真正控制危害的实体，
    实现路径有三条：自己直接对 Y/Z 做验证；依赖直接供应商 X 对 Y/Z 的验证文件
    （但必须自己审查评估并记录该审查）；或两者混合。
    同理，当控制由"供应商定义之外"的第三方实体（如独立的采收/包装商）实施时，
    收货设施必须自行验证或取得其文件并审查评估。
    思维结构：责任跟着控制走，文件流跟着责任走。
  tags: [supply-chain, entity-mapping, verification]

- id: f5-14
  title: 供应商不能自审自证（独立性底线）
  type: framework
  source_chapter: Ch15 §15.8.3
  source_quote: |
    "a receiving facility may not accept any of the following as a supplier verification activity from its
    supplier: A determination by its supplier of the appropriate supplier verification activities for that
    supplier; An audit conducted by its supplier of that supplier; A review by its supplier of that supplier's
    own relevant food safety records; or The conduct by its supplier of other appropriate supplier verification
    activities for that supplier."
  summary: |
    供应商对自己能做的事被明确划界：不得代替收货设施决定验证活动、
    不得审核自己、不得审查自己的记录、不得自行开展其他验证活动。
    供应商只被允许做两件事：对其所控危害的抽样检测（以 COA 等文件提供），
    以及提供由第三方 qualified auditor 审核它的审核结果。
    思维结构：任何"既当运动员又当裁判"的自证都无效——独立性是验证有效性的前提；
    供应商的检测可以作为证据，但不能作为判断。
  tags: [independence, conflict-of-interest, supply-chain, principle]

- id: f5-15
  title: 书面认定（written determination）作为灵活性的制度化出口
  type: framework
  source_chapter: Ch15 §15.11.2.2
  source_quote: |
    "The exception to the requirement to conduct an annual onsite audit when the hazard requiring a preventive
    control is a SAHCODH hazard is when there is a written determination that other verification activities
    and/or less frequent onsite auditing of the supplier provide adequate assurance that the hazards are
    controlled. The written determination is part of your food safety plan and, thus, must be prepared by (or
    under the oversight of) your PCQI."
  summary: |
    即便是"SAHCODH 危害必须每年现场审核"的硬规则，也留了一个出口：
    由 PCQI 做出书面认定，论证"其他验证活动和/或更低频审核足以提供充分保证"，
    即可替代年度审核。典型场景：同一集团内子公司供应商（母公司统一体系）；
    或多年合规史供应商（用"两年一审+ intervening 年季度检测"的组合并写进书面程序）。
    思维结构：硬规则+书面例外是两全设计——灵活性不被堵死，
    但每次动用灵活性都要付出"书面论证并由有资格者签名"的成本，
    把自由裁量变成可检查的记录。指南中多次出现此模式（如过敏原咨询声明论证）。
  tags: [written-determination, flexibility, mental-model, escape-hatch]

- id: f5-16
  title: 替代验证的"双书面保证"结构（年度状态 + 两年合规）
  type: framework
  source_chapter: Ch15 §15.11.3–15.11.5
  source_quote: |
    "...if you: Obtain written assurance that the supplier is a qualified facility... Before first approving the
    supplier for an applicable calendar year; and On an annual basis thereafter...; and Obtain written
    assurance, at least every 2 years, that the supplier is producing the raw material or other ingredient in
    compliance with applicable FDA food safety regulations..."
  summary: |
    对三类特殊供应商（qualified facility、非 covered farm 的农产品农场、<3000 只蛋鸡的蛋场），
    验证活动统一替换为两层书面保证：① 每年（首次批准前+此后每年 12 月 31 日前）
    保证其豁免/身份状态；② 至少每两年保证其合规性（描述所实施的预防控制，
    或声明遵守非联邦食品安全法）。
    思维结构：把对小供应商的验证从"查它的体系"降为"收它的承诺"，
    但承诺必须是周期性的、书面的、内容有法定选项的；
    且状态可能漂移（ qualified facility 界限随销售额变动），年度确认就是对漂移的防护。
  tags: [written-assurance, alternative-verification, qualified-facility]

- id: f5-17
  title: 临时供应商应急路径（降级验证+限时+多源备份）
  type: framework
  source_chapter: Ch15 §15.9.2
  source_quote: |
    "For an unapproved supplier that you plan to use on a temporary basis, we recommend that you conduct at
    least a minimal review of the supplier... you must subject the applicable raw materials or other ingredients
    to adequate verification activities before acceptance for use... You should use unapproved suppliers only
    on a temporary basis until you are able to fully evaluate and approve a new supplier..."
  summary: |
    断供应急（地震/天气、独家供应商设备故障、供应商出污染问题、突然停业）时
    允许临时使用未批准供应商，但有三重护栏：① 事前做最低限度审查
    （查 FDA 网站有无警告信/进口警报）；② 原料在使用前必须经受充分验证
    （如逐批统计抽样检测沙门氏菌，或审查其杀菌工艺记录）；③ 只能临时用
    （数周到数月），并尽快全面评估转正；预案上建议对每种原料维持多个已批准供应商以减少应急需求。
    思维结构：给刚性规则（只用批准供应商）预置一个受控的泄压阀，
    而不是让断供压力把人推向绕过规则。
  tags: [emergency, temporary-supplier, controlled-exception]

- id: f5-18
  title: 信任递减频率模型（检测频次随履约历史放松）
  type: framework
  source_chapter: Ch15 §15.7.2.2
  source_quote: |
    "We recommend that you establish the frequency of such testing by first conducting the sampling and testing
    on a relatively frequent basis (e.g., monthly) until the supplier establishes a good history of supplying an
    acceptable raw material or other ingredient, after which time you could sample and test less frequently,
    such as quarterly."
  summary: |
    对供应商的检测频次不必恒定：起步用高频率（如每月）建立信任基线，
    待供应商积累良好的供货历史后降频（如每季度）。
    这与周期性验证的理念一致——定期验证提供的是对供应商表现的常规反馈，
    而不是只在出问题时才去看。
    思维结构：验证强度是信任的函数，信任由数据积累而来；
    与 f5-01 的"信息恶化即升频"正好构成双向调节——检测频率随风险上下浮动。
  tags: [frequency, trust-building, adaptive-monitoring]

- id: f5-19
  title: 抽样检测的局限性自知框架
  type: framework
  source_chapter: Ch15 §15.7.2.2
  source_quote: |
    "you should use scientifically-based sampling plans that provide reasonable assurance that the hazard has
    been significantly minimized or prevented and that address known limitations of sampling and testing foods
    as a verification activity. For example, your sampling plan should take into consideration whether a hazard
    is homogeneously distributed throughout the lot..."
  summary: |
    用检测做验证时必须正面处理检测的已知局限：危害在批内是否均匀分布
    （不均匀→抽样天然有漏检风险）、食品组分是否干扰分析方法、
    方法灵敏度能否检出低浓度危害。对策：取有代表性的样品、
    用在该食品基质中已证明可靠的方法、用灵敏度匹配的方法。
    思维结构：任何工具都有失效模式，选择工具的同时要写出它的失效模式与缓解手段——
    这也是全书"检测只能补充、不能替代其他验证活动"的底层逻辑。
  tags: [limitations, sampling, epistemics, testing]

- id: f5-20
  title: 检查替代审核的等效性判定
  type: framework
  source_chapter: Ch15 §15.12.3
  source_quote: |
    "an ''appropriate'' inspection conducted for compliance ''with applicable FDA regulations'' means that the
    inspection must be sufficiently relevant to compliance with applicable FDA food safety regulations to
    credibly substitute for an onsite audit. For example, inspection by USDA to determine whether a farm
    satisfies the requirements of the produce safety regulation could constitute an appropriate inspection...
    but an inspection by USDA to determine whether a farm satisfies the requirements of the National Organic
    Program could not."
  summary: |
    政府检查的书面结果可替代现场审核（1 年内），但等效性要看"针对同一法规/同一危害"：
    USDA 对农产品安全法规的检查可替代，USDA 有机认证检查不可替代；
    外国政府发的 HACCP 证书也不被接受为替代（要求不同、发证依据不明），
    但可作为降低审核频次书面认定的支持材料之一。
    思维结构：判断替代物是否成立，看它验证的对象与原要求是否重合——
    名义相似不等于等效；等效性论证要落到具体条款。
  tags: [equivalence, substitution, audit, decision-framework]

- id: f5-21
  title: Qualified auditor 能力三元组模型
  type: framework
  source_chapter: Ch15 §15.12.1
  source_quote: |
    "A person should have at least some actual experience in auditing (including assisting in audits or
    observing audits) to meet the definition of a qualified auditor, because the necessary technical expertise
    likely cannot be obtained solely through education and/or training that does not involve assisting or
    observing others in the performance of an audit. The GFSI's auditor competency model lists three main
    components for auditor competencies: (1) Auditing skills and knowledge; (2) technical skills and knowledge;
    and (3) behavior and systems thinking..."
  summary: |
    审核员的资格不是一张证书，而是三个来源的组合：教育、培训、经验——
    且三者不能完全互相替代：纯课堂培训不算数，必须有实际参与审核的经历
    （协助或观摩审核）。可借鉴的能力模型（GFSI）：审核技能与知识、
    技术技能与知识、行为与系统思维三主轴。政府雇员（含外国政府雇员）
    和经认可的认证机构审核代理是典型的 qualified auditor。
    思维结构：资格认定应区分"知识维度"与"实践维度"，动手经验是不可压缩项。
  tags: [competency, qualification, auditor]

- id: f5-22
  title: 支付与结果脱钩（经济利益冲突禁止）
  type: framework
  source_chapter: Ch15 §15.11.6
  source_quote: |
    "payment must not be related to the results of the activity. For example, you may not give a qualified
    auditor who conducts an onsite audit... greater compensation for determining that a supplier is in
    compliance with applicable FDA requirements. Also, you may not reduce the compensation of a qualified
    auditor or qualified individual or assess financial penalties because the qualified auditor or qualified
    individual identified areas of supplier noncompliance."
  summary: |
    验证活动的结果不得受经济利益影响：不得给"判合格"的审核员多付钱，
    也不得因审核员"找出了不符合"而降薪或罚款；供应商同样不得做此类支付。
    有利益冲突的 qualified individual 丧失独立开展验证活动的资格。
    例外边界：供应商员工做检测并出 COA 不被禁止（这是法定的供应商可做活动）；
    供应商提供的第三方审核也可用。
    思维结构：让裁判的收入与其判决结果脱钩，是保障判断独立性的制度设计——
    奖与罚双向都构成污染。
  tags: [conflict-of-interest, independence, incentive-design]

- id: f5-23
  title: 集团化集中管理（corporate parent 代行供应链职能）
  type: framework
  source_chapter: Ch15 §15.6.2
  source_quote: |
    "your corporate parent could have a team that establishes written procedures for supplier approval,
    determines supplier verification activities, conducts supplier verification activities, and maintains
    required documentation. In addition, your corporate parent could establish and implement a supply-chain
    program that takes into consideration its knowledge of the food safety programs in place at all of the
    facilities under its ownership."
  summary: |
    法定义务落在工厂，但履行可以上移：集团层面可担任 PCQI、建供应商批准书面程序、
    定验证活动、执行验证、维护记录，并可利用"它对所有旗下工厂安全体系的了解"
    设计集团级供应链计划——这也是集团内子公司供应商可豁免年度审核书面认定的基础
    （同一食品安全体系+集团层验证）。
    记录异地存放合法，但须能在官方要求后 24 小时内取回现场；电子可及即视为现场。
    思维结构：责任主体与执行主体可以分离，分离必须靠记录可及性来兜底。
  tags: [corporate-governance, centralization, records]

- id: f5-24
  title: 双法规双向借用策略（含"专项不可免"清单）
  type: framework
  source_chapter: Ch16 §16.2.3–16.2.4
  source_quote: |
    "the procedures, practices, and processes that you establish and implement to comply with the requirements
    prescribed by 21 CFR 108.25 and part 114, and records that you establish and keep to comply with those
    requirements, could partially ̶ but not fully ̶ satisfy corresponding requirements of the PCHF rule...
    If a specific acidified food requirement exceeds the corresponding requirement of the PCHF rule, you must
    comply with the specific acidified food requirement."
  summary: |
    同时受 PCHF（part 117）与酸化食品专项法规（108.25/part 114）管辖的企业，
    不必做两套体系：一套程序/记录可以双向借用——用 2541e 表参数充当 PCHF 的
    书面工艺控制，用 PCHF 的监控/记录满足 part 114 的 pH 监测等对应要求。
    但借用是"部分而非全部"：专项超出部分不可免——Form 2541/2541e 提交、
    应 FDA 要求提供工艺资料、3 年记录保存（超出 part 117 的 2 年）、
    容器永久可见编码、分销记录、向 FDA 通报流通中的问题。
    思维结构：多套合规体系叠加时，先做要求映射表找重合区复用，
    再显式列出"映射不到的残余义务"单独兜底——复用不能靠感觉，要靠逐条对照。
  tags: [regulatory-mapping, dual-compliance, acidified-foods, reuse]

- id: f5-25
  title: 二阶危害链推理（间接危害的正名）
  type: framework
  source_chapter: Ch16 §16.3 / §16.9
  source_quote: |
    "Microorganisms of non-health significance, by themselves, are not 'hazards' as that term is defined in
    part 117. However... when critical factors are not carefully controlled, the vegetative cells of some
    microorganisms of non-health significance (such as some spoilage bacteria) can grow in an acid environment
    and, in so doing, cause the pH of the food to increase. Therefore, under part 117, a knowledgeable person
    could identify microorganisms of non-health significance in shelf-stable acidified foods as biological
    hazards requiring a preventive control."
  summary: |
    腐败微生物本身按定义不是"危害"，但它的生长会抬高 pH，而 pH 升高会让
    肉毒梭菌孢子萌发产毒——于是通过这条因果链，腐败菌在酸化食品中可以被
    合法地识别为"需预防控制的生物危害"。
    同款推理也用于容器密封（渗漏→再污染）和耐酸孢子（B. licheniformis 耐热耐酸）。
    思维结构：判定"X 是不是危害"时不要只看 X 的直接致病性，
    要看 X 是否是通向真正危害的必要一环——二阶、间接的危害同样需要控制。
  tags: [reasoning, causal-chain, hazard-identification, second-order]

- id: f5-26
  title: 供应商不合格处置阶梯
  type: framework
  source_chapter: Ch15 §15.7.5
  source_quote: |
    "The appropriate actions you take in response to nonconformance will depend on the circumstances and the
    specific root cause of the nonconformance and could include: Discontinuing use of the supplier...;
    Notifying the supplier of the problem and requesting documentation of corrective actions...; Assisting the
    supplier's efforts to correct and prevent recurrence of the problem; Revising your supply-chain program;
    and Conducting, or working with your supplier to conduct, a recall of an adulterated or misbranded food."
  summary: |
    发现供应商未控制所识别危害（通过审核/验证检测/文件审查/投诉等渠道）时，
    必须按 117.150 及时采取并记录行动，处置选项构成一个由轻到重的阶梯：
    暂停使用直至原因解决 → 通知供应商并索取纠正措施文件 → 协助其纠正与防复发
    → 修订自己的供应链计划 →（最重）与供应商一起召回受污染/错标食品。
    选项取决于具体情况和根因，而非机械套用。
    思维结构：对合作方的失效响应是分级的伙伴关系管理，从止损、沟通、
    赋能、自省到共同善后，而不是"发现问题就拉黑"。
  tags: [nonconformance, escalation-ladder, supplier-management]
```
