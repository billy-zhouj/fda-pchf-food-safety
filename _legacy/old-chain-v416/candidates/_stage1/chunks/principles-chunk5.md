# Stage 1 原则提取候选 — 分块 5/6（第 13201–16500 行）

> 覆盖范围：Ch12 尾部（Manufacturer B 记录 + Miller C/Baker D/Sandwich F DON 条件性升格案例链）、Ch13（占位）、Ch14 召回计划、Ch15 供应链程序、Ch16 酸化食品、Ch17（占位）。
> 提取角色：principle-extractor（原则/清单/规则/断言），不做筛选。
> "是否反复出现"判断仅限本段。

```yaml
- id: p5_01
  title: DON 咨询水平只针对成品，原料须自建内部规格
  type: principle
  source_chapter: 第 12 章 · 化学危害预防控制（12.12 Miller C 案例脚注 35）
  source_quote: |
    That guidance does not identify an advisory level for wheat RACs, explaining that significant
    variability in manufacturing processes applicable to wheat RACs does not make it practical to do
    so. Based on Miller C's experience ..., Miller C's PCQI determines and establishes an internal
    specification for a level of DON in inbound wheat RACs that is adequate to ensure that the levels
    of DON in its milled wheat products will not exceed FDA advisory levels.
  summary: |
    FDA 的 DON 咨询水平只针对成品小麦制品（面粉、麸皮、胚芽），
    不对小麦原料（RAC）设定咨询水平——因为不同制粉工艺差异太大，无法统一。
    因此企业必须以成品咨询水平为反推目标，由 PCQI 基于自身工艺经验
    为进厂原料建立内部规格（internal specification）。
    规则：监管限值缺位 ≠ 无需限值；上游原料的合格判据由企业自建并自证。
    这是"监管终点限值 → 自建过程限值"的通用转化模式，适用于各类原料-成品场景。
  tags: [principle, mycotoxin, DON, internal-specification, numeric-boundary]

- id: p5_02
  title: 成品毒元素超内部规格的三步响应
  type: principle
  source_chapter: 第 12 章 · 化学危害预防控制（12.11.3 Manufacturer B 验证）
  source_quote: |
    If the level of a toxic element exceeds internal specifications for a finished product,
    Manufacturer B: conducts a root cause investigation ...; assesses whether changes should be made
    to the supply-chain program for the applicable ingredient; and determines appropriate disposition
    of the finished product ..., including preventing affected food from entering into commerce if
    Manufacturer B cannot ensure that the affected food is not adulterated.
  summary: |
    成品检测超过内部规格时的固定三步：① 根因调查（找出污染来源配料：
    大米还是维生素矿物质预混料）；② 评估是否需要修改对应配料的供应链程序；
    ③ 处置受影响成品——若无法确保食品未被掺假（FD&C 法案 402 条），
    必须阻止其进入商业流通。
    规则：超规格不只是"放行/扣留"二选一，还要闭环回供应链程序本身。
    每份相关记录（规格、测试、处置）都须 PCQI 签名注明日期审查。
  tags: [principle, toxic-elements, testing, disposition, root-cause]

- id: p5_03
  title: 条件性升格：季节性信息恶化时 CGMP 措施升格为预防控制
  type: principle
  source_chapter: 第 12 章 · 化学危害预防控制（12.12 Miller C 危害分析结论）
  source_quote: |
    The outcome of Miller C's hazard analysis is that the hazard of DON in wheat RACs is not a hazard
    requiring a preventive control unless the available information (such as the test results for
    incoming RACs ... and USDA's weekly reports) indicate the potential for higher levels of DON than
    expected. When the potential for higher than expected levels of DON is indicated, Miller C:
    implements its physical cleaning processes as a preventive control ...
  summary: |
    危害分析的结论可以是"条件性"的：常态下 DON 不是需要预防控制的危害，
    现有措施作为 CGMP 运行即可；但一旦出现升格触发信息（新粮首检、
    USDA 周报显示产区 DON 偏高、地堆储存小麦、检出率上升），
    原有物理清洗程序必须升格为预防控制（工艺控制）运行，
    并配套：最大化使用电子色选机、加测成品作为验证、超标批次纠正（转饲料/工业用/销毁）、
    记录监控/验证/纠正。危害分析不是静态结论，而是"状态机"。
    同一断言在本段 Miller C、Baker D 两案例中重复出现。
  tags: [principle, conditional-escalation, DON, hazard-analysis, reanalysis-trigger, recurring]

- id: p5_04
  title: 检测频次的四类升档触发条件
  type: principle
  source_chapter: 第 12 章 · 化学危害预防控制（12.12 Miller C 定期检测）
  source_quote: |
    The frequency of testing varies and is increased for circumstances such as: the initial receipt
    of "new crop" wheat RACs ...; USDA's weekly reports ... about the elevated prevalence and/or
    levels of DON in wheat RACs from a geographic region supplying Miller C; receipt of wheat RACs
    that were stored in ground piles; and increased detection of DON in incoming wheat RACs or milled
    wheat products.
  summary: |
    检测不是固定频次，四类事件触发升档：① 收到本收获季"新粮"首批
    （摸清当季 DON 基线）；② USDA 周报显示本供应区域 DON 偏高；
    ③ 收到地堆储存的原料；④ 原料或成品检出率上升
    （此时色选加工的每批成品都要做验证检测）。
    规则：监测信息流（外部报告+内部检出）应直接驱动检测频次，
    而非固定日历。这是"信息驱动的采样计划"通用模式。
  tags: [principle, testing-frequency, DON, trigger-list, monitoring]

- id: p5_05
  title: 采购前审查制粉商程序；无检测程序者先自测再签约
  type: principle
  source_chapter: 第 12 章 · 化学危害预防控制（12.13 Baker D 案例分析）
  source_quote: |
    When the miller's procedures, processes, and practices include a program for analytical testing
    for DON ..., Baker D reviews those test results to confirm that the levels of DON are consistent
    with the FDA advisory level before entering into a purchase agreement. When the miller's
    procedures ... do not include a program for analytical testing ..., Baker D arranges for
    analytical testing on several shipments of flour from that miller to confirm ...
  summary: |
    签订采购协议前必须审查供应商的相关程序：制粉商自带 DON 检测程序
    （Miller C）→ 审查其检测结果确认与 FDA 咨询水平一致；
    制粉商无检测程序（Miller E）→ 在签约前自行安排对若干批次面粉检测确认。
    两种情况下采购协议都必须写明：制粉商在出现 DON 偏高迹象时须通知采购方；
    采购方有权按批索取 COA 或增加"以 DON 检测结果为放行条件"的验收标准。
    规则：尽调义务与合同条款是危害控制的载体，签约即控险。
  tags: [principle, purchase-agreement, supplier-review, DON, COA]

- id: p5_06
  title: 下游凭上游的供应商管理链条获得保证
  type: principle
  source_chapter: 第 12 章 · 化学危害预防控制（12.14 Sandwich Maker F 案例分析）
  source_quote: |
    As part of its process for entering into purchase agreements with suppliers of pre-sliced bread,
    Sandwich Maker F reviews the procedures, processes, and practices applicable to the supplier's
    evaluation of the adequacy of the miller's program to control the level of DON in milled wheat
    products ... The outcome of Sandwich Maker F's hazard analysis is that the hazard of DON in
    pre-sliced bread is not a hazard requiring a preventive control.
  summary: |
    三明治厂 F 距离制粉环节隔了两级（F→Baker D→Miller C/E），它不直接测 DON，
    而是审查直接供应商（面包厂 D）"如何评估制粉商程序充分性"的程序本身。
    只要这条逐级传递的审查链条完整，F 可在危害分析中得出
    "DON 不是需要预防控制的危害"的结论。
    规则：供应链上的保证可以逐级传递，但每一级都要有可审查的程序化证据。
    与 Baker D 案例合并构成"条件性升格"链条的下游端。
  tags: [principle, supply-chain, assurance-transfer, DON, tiered-suppliers]

- id: p5_07
  title: 召回计划不适用管理组件
  type: principle
  source_chapter: 第 14 章 · 召回计划（14.1 本章目的）
  source_quote: |
    Although the written recall plan is a type of preventive control (see 21 CFR 117.135(c)(5)), the
    PCHF requirements specify that the written recall plan is not subject to the preventive control
    management components specified in 21 CFR 117.140 (i.e., monitoring, corrective actions and
    corrections, and verification.) (See 21 CFR 117.140(c).) Therefore, this chapter does not discuss
    the application of preventive control management components to your written recall plan.
  summary: |
    书面召回计划虽被归类为一种预防控制，但法规明确豁免其管理组件义务——
    无须监控、无须纠正措施、无须验证（21 CFR 117.140(c)）。
    这是五类预防控制中唯一的管理组件全豁免项（供应链程序只需子集）。
    规则：给控制措施分类时，先查它是否带管理组件豁免，再决定资源配置。
    Ch16 表 16-7 再次引用此条（在本段内第二次出现）。
  tags: [principle, recall-plan, exemption, management-components, recurring]

- id: p5_08
  title: 召回计划四项法定程序
  type: principle
  source_chapter: 第 14 章 · 召回计划（14.3 概述）
  source_quote: |
    you must establish a written recall plan for food that requires a preventive control (21 CFR
    117.139(a)). ... the written recall plan must include procedures that describe the steps to be
    taken, and assign responsibility for taking those steps, to perform the following actions as
    appropriate to the facility: Directly notify the direct consignees ...; Notify the public ...;
    Conduct effectiveness checks ...; and Appropriately dispose of recalled food.
  summary: |
    凡存在需要预防控制的危害的食品，必须建立书面召回计划，
    且计划必须同时包含"步骤描述"与"责任分配"两要素，覆盖四项行动：
    ① 直接通知直接收货人（含如何退回/处置）；② 适当时告知公众危害；
    ③ 开展有效性核查（effectiveness checks）验证召回落实；④ 适当处置召回食品
    （再加工、返工、转安全用途或销毁）。
    每项程序都要写明由谁执行——没有责任人的步骤清单不算合规程序。
  tags: [principle, recall-plan, checklist, four-procedures, regulation]

- id: p5_09
  title: 书面召回通讯六要素
  type: principle
  source_chapter: 第 14 章 · 召回计划（14.5.1–14.5.1.6）
  source_quote: |
    Proactively address the questions that direct consignees are likely to have by describing in
    detail the components to be included in your written recall communication (e.g., identify the
    food, explain the reason for the recall, specify the depth of the recall, provide instructions
    for what direct consignees should do with the food, and make it easy for recipients to
    communicate with you); and Include model letters ...
  summary: |
    召回计划应预先规定书面召回通讯的六项内容：① 识别食品（品名、规格、
    批号、代码、保质期、UPC、发货日期，并附产品标签）；② 简述召回原因
    与健康危害；③ 指明召回深度（批发/零售/消费者层）；④ 给出收货人处置指令
    （下架、停运、通知其客户、退回、销毁方式）；⑤ 便于回传（免费电话、
    邮资已付回执卡、电子邮件、在线表单），并跟进无回应者；⑥ 收录可按情况
    修改的模板召回信——事先备模板才能在召回时快速发出完整信息。
  tags: [principle, recall-communication, checklist, six-elements, template]

- id: p5_10
  title: 电话召回通知须以书面确认
  type: principle
  source_chapter: 第 14 章 · 召回计划（14.5.1）
  source_quote: |
    If your recall plan specifies that you will contact your direct consignees by phone, we recommend
    that your recall plan also specify that you will confirm that phone communication in writing
    (e.g., follow up the phone call with a written communication such as a letter, email, telefax, or
    text message) and/or document your phone communication in an appropriate manner. (See 21 CFR
    7.49(b).)
  summary: |
    召回通讯可以用任何有效方式进行（信件、邮件、传真、短信均可），
    但若选择电话通知，必须以书面方式确认该电话沟通（通话后补发书面通知）
    和/或以适当方式记录通话内容。
    规则：口头通知在召回场景下不具备完整证据效力，一切关键通知都要落纸。
  tags: [principle, recall, documentation, phone-confirmation]

- id: p5_11
  title: 公众警告的判定标准：紧迫+严重+其他手段不足
  type: principle
  source_chapter: 第 14 章 · 召回计划（14.5.2 适当时告知公众）
  source_quote: |
    A public warning is reserved for urgent situations where other means of preventing use of the
    recalled product appear inadequate. ... Your recall plan should describe your criteria for
    determining whether a public warning is appropriate. ... Unlike with public warnings, the recalls
    listed in the FDA Enforcement Report are not limited to urgent situations that present serious
    hazards to health and are not necessarily used to alert the public about the risk or hazard of a
    product under recall.
  summary: |
    公众警告（public warning）专用于紧迫情形——当其他阻止召回产品被使用的
    手段都显得不足时，通过大众媒体或专业媒体发布。
    召回计划必须写明判定"是否发布公众警告"的标准，以及发布后采取的步骤。
    注意区分：FDA Enforcement Report 列出所有召回（含 Class III），
    属常规信息公开，不等于公众警告；企业在 FDA 网页被公示也不代表情形紧迫。
    规则：公众警告是最后手段，判定标准要事先书面化而不是临场拍板。
  tags: [principle, public-warning, decision-criteria, recall, classification]

- id: p5_12
  title: 有效性核查的目的：验证通知已送达且已行动
  type: principle
  source_chapter: 第 14 章 · 召回计划（14.5.3）
  source_quote: |
    The purpose of an effectiveness check is to verify that all consignees at the specified recall
    depth have received notification about the recall and have taken appropriate action. (See 21 CFR
    7.42(b)(3).)
  summary: |
    有效性核查不是"发通知"本身，而是验证召回深度范围内的所有收货人
    ① 已收到召回通知、② 已采取适当行动。
    计划应收录可修改的核查函/回执格式/电话问卷模板（FDA 程序手册
    Exhibit 7-1 至 7-3 提供样例），以便需要时快速启用。
    规则：任何通知类活动都要设计"回执验证"环节，否则等于没验证效果。
  tags: [principle, effectiveness-check, recall, verification]

- id: p5_13
  title: 召回管理团队：成员+替任+联系方式+决策人
  type: principle
  source_chapter: 第 14 章 · 召回计划（14.6 责任分配程序）
  source_quote: |
    Identify members (and alternate members) of a recall management team, headed by a recall
    coordinator. ... Provide the following information about each member (and alternate member): Name
    and job position/title; Business phone number ... and email address; After-hours phone number
    ...; and Responsibilities; and Specify who is responsible for the decision to conduct a recall.
  summary: |
    召回计划必须指定召回管理团队：以召回协调员为首，成员按职能覆盖
    配送、生产与质量、消费者事务、公关、市场、区域销售等；
    每名成员（及替任成员，用于成员不可用时顶替）记录四项信息：
    姓名职位、办公电话+邮箱、下班后电话、职责范围。
    最关键的一条：必须明确指定"由谁决定发起召回"。
    规则：危机预案的价值在于决策权与通讯录事先书面化，节省召回时的黄金时间。
  tags: [principle, recall-team, responsibility-assignment, crisis-preparedness]

- id: p5_14
  title: RFR：确定可报告食品后 24 小时内电子通知 FDA
  type: principle
  source_chapter: 第 14 章 · 召回计划（14.7.1）
  source_quote: |
    food firms that are "responsible parties" as defined in the statute are required to notify FDA
    electronically with certain information within 24 hours of determining that a food they
    manufactured, processed, packed, or held is a reportable food. ... We recommend that your recall
    plan include any procedures you have to comply with the RFR, or a cross-reference to such
    procedures, so that the procedures will be readily available to your recall management team.
  summary: |
    可报告食品（reportable food）：除膳食补充剂和婴儿配方食品外，
    使用或暴露于该食品有合理可能性导致人或动物严重健康后果或死亡者。
    法定责任方在确定自己制造/加工/包装/持有的食品属可报告食品后，
    必须在 24 小时内以电子方式向 FDA 提交规定信息（RFR 义务）。
    建议将 RFR 合规程序（或其交叉引用）纳入召回计划，让召回团队即取即用——
    召回期间时间至关重要。
    数值界限：24 小时，硬性法定时限。
  tags: [principle, RFR, 24-hours, numeric-boundary, reporting]

- id: p5_15
  title: 决定召回后立即通知 FDA 召回协调员，先于媒体与客户
  type: principle
  source_chapter: 第 14 章 · 召回计划（14.7.2）
  source_quote: |
    The industry recall guidance recommends that you notify the appropriate FDA Recall Coordinator
    as soon as a decision is made that a recall is appropriate and prior to the issuance of press or
    written notification to customers (FDA, 2014). ... the draft initiation of voluntary recalls
    guidance encourages firms to consult with FDA while its own investigation is ongoing ...
  summary: |
    一旦作出召回决定，应立即通知对应的 FDA 召回协调员，
    且必须在向媒体发布新闻稿或向客户发出书面通知之前完成。
    调查进行中若对问题定性有疑问，应主动与 FDA 沟通咨询。
    规则：监管沟通在对外沟通之前——顺序错误会放大法律与声誉风险。
    召回计划应预先收录本指南相关指引与信函模板清单，供团队随时调用。
  tags: [principle, FDA-notification, sequence, recall, communication-order]

- id: p5_16
  title: 经纪商/分销商不是供应商，须穿透至实际制造者
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.3.2、15.8.1）
  source_quote: |
    entities such as brokers, produce aggregators, food distributors, and cold storage facilities are
    neither receiving facilities that are required to establish a supply-chain program nor suppliers,
    because such entities are not manufacturers/processors. ... Thus, if you buy raw materials or
    other ingredients from a broker or distributor, you should ask the broker or distributor to
    provide you with information that allows you to approve the establishment that
    manufactures/processes the food ... as a supplier.
  summary: |
    法规定义下的"供应商"是制造/加工食品、饲养动物或种植食品的机构；
    经纪商、农产品集散商、分销商、冷藏库既不是供应商也不是收货设施。
    从经纪商/分销商采购时，必须通过其提供的信息去批准真正的制造者/种植者
    为供应商；从零售渠道采购时，可利用标签上的制造/包装/分销商信息定位实体。
    规则：批准对象永远是"做食品的人"，不是"卖食品的人"。
  tags: [principle, supplier-definition, broker, distributor, supply-chain]

- id: p5_17
  title: 本厂自行控制危害则无须供应链程序
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.6.1）
  source_quote: |
    You are not required to establish and implement a supply-chain program for a particular raw
    material or other ingredient if you will control the hazard at your own facility, regardless of
    whether your supplier has also applied one or more preventive controls for that hazard to raw
    materials and other ingredients that your supplier provides to you. (See 21 CFR 117.405(a)(1).)
  summary: |
    若收货设施将在自己的设施内控制某危害，则对该原料无须建立供应链程序——
    即使供应商也针对同一危害实施了预防控制（双保险不改变义务归属）。
    反之，凡危害需在接收前控制（supply-chain-applied control），就必须有程序。
    另：食品接触物质（食品接触物）不产生供应链控制义务——
    长期 CGMP 加 FDA 上市前审查已足够覆盖其风险。
    规则：控制位置决定程序类型，而非危害本身。
  tags: [principle, supply-chain-program, applicability, food-contact-substances]

- id: p5_18
  title: 异地保存的供应链记录须 24 小时内可调取
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.6.2 母公司参与）
  source_quote: |
    your corporate parent ... could establish and implement a supply-chain program ... The records
    documenting the supply-chain program are subject to the requirements, in subpart F ... offsite
    storage of records (such as storage at the place of business of your corporate parent ...) is
    permitted if such records can be retrieved and provided onsite within 24 hours of request for
    official review. If your corporate parent establishes and maintains the records ... electronically
    and you can access applicable records ... electronically, we consider the records to be onsite.
  summary: |
    母公司可代为建立供应链程序：组建团队制定批准程序、决定与执行验证活动、
    维护文档，甚至由母公司层面人员担任 PCQI，并可结合其对旗下所有设施
    食品安全体系的了解统一设计程序。
    约束条件：异地保存（如存于母公司办公地）的记录必须能在官方审查要求后
    24 小时内调回现场；若母公司电子化维护且设施可电子访问，则视为现场记录。
    数值界限：24 小时调取时限。
  tags: [principle, corporate-parent, records, 24-hours, numeric-boundary]

- id: p5_19
  title: 研究或评估用途食品的四条件豁免
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.6.3.2）
  source_quote: |
    The requirements for a supply-chain program do not apply to food that is supplied for research or
    evaluation use, provided that such food: Is not intended for retail sale and is not sold or
    distributed to the public; Is labeled with the statement "Food for research or evaluation use";
    Is supplied in a small quantity that is consistent with a research, analysis, or quality
    assurance purpose ...; and Is accompanied with documents ... stating that the food will be used
    for research or evaluation purposes and cannot be sold or distributed to the public.
  summary: |
    供应链程序义务对研究/评估用途食品豁免，但四个条件必须同时满足：
    ① 不面向零售销售、不向公众出售或分发；② 标签标注
    "Food for research or evaluation use"且标签须牢固附着直到使用完毕；
    ③ 数量与科研/分析/QA 目的相称（如农药检测 10 磅、真菌毒素检测 50 磅
    可算少量），剩余部分妥善处置；④ 按行业惯例随附文件声明用途且不得转售。
    反例：展会上供试吃的食品属于"向公众分发"，不适用豁免——
    即使提供方是 R&D 设施；但在展会上针对特定受试者开展的界定研究可豁免。
  tags: [principle, exemption, research-use, four-conditions, trade-show]

- id: p5_20
  title: 危害控制者非供应商本人时须验证或审查第三方文档
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.6.4）
  source_quote: |
    When a supply-chain-applied control is applied by an entity other than the receiving facility's
    supplier ..., the receiving facility must: (1) Verify the supply-chain-applied control; or (2)
    obtain documentation of an appropriate verification activity from another entity, review and
    assess the entity's applicable documentation, and document that review and assessment. (See 21
    CFR 117.405(c).)
  summary: |
    最典型场景：农场是法定供应商，但采收与包装由独立企业经营
    （如控制清洗水温防微生物渗入、循环水换水计划）。
    此时收货设施必须：① 自行验证该控制；或 ② 从他方获取验证活动文档，
    审查评估该文档，并书面记录审查评估。
    FDA 不要求收货设施对采收者/包装者套用全套"供应商"要求，
    审查其相关食品安全记录（如 RTE 农产品采收工培训记录、换水计划记录）即可。
    规则：控制者与供应商分离时，验证责任仍归收货设施，路径可以借道。
  tags: [principle, supply-chain, third-party-control, documentation-review]

- id: p5_21
  title: 四类合格供应商验证活动
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.7.2）
  source_quote: |
    Section 21 CFR 117.410(b) of subpart G specifies four appropriate supplier verification activities
    for raw materials and other ingredients. ... [1] Onsite audits; [2] Sampling and testing of the
    raw material or other ingredient; [3] Review of the supplier's relevant food safety records; [4]
    Other appropriate supplier verification activities based on supplier performance and the risk
    associated with the raw material or other ingredient.
  summary: |
    供应商验证活动只有四种法定类型：① 现场审核；② 原料抽样检测
    （可周期性或逐批）；③ 审查供应商相关食品安全记录（能证明供应商
    遵循其控制程序且危害已受控的记录，包括供应商对其上游的审核记录）；
    ④ 基于供应商表现与原料风险的其他活动（如事实型问卷、
    特定审核体系认证信息、无审核年度的环境监测记录审查）。
    可单独或组合使用；选哪种、多频繁由 117.410(d) 四因素决定。
    相关记录审查例：黑胡椒蒸汽处理案例中可向供应商 A 索取对处理企业 B 的审核记录。
  tags: [principle, supplier-verification, four-activities, checklist, supply-chain]

- id: p5_22
  title: 抽样检测的计划设计：科学布点+方法适配+先密后疏
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.7.2.2）
  source_quote: |
    We recommend that you establish the frequency of such testing by first conducting the sampling and
    testing on a relatively frequent basis (e.g., monthly) until the supplier establishes a good
    history of supplying an acceptable raw material ..., after which time you could sample and test
    less frequently, such as quarterly. ... your sampling plan should take into consideration whether
    a hazard is homogeneously distributed throughout the lot, and your selection of an analytical
    method should consider whether food components could interfere with the method ...
  summary: |
    用抽样检测做供应商验证时的规则组合：① 频次策略——先高频
    （如每月）直到供应商建立良好历史，再降为较低频（如每季度）；
    ② 抽样计划必须科学设定，考虑危害在批次中是否均匀分布
    （分布不均是抽样天然漏检的根源）；③ 方法选择要考虑食品基质干扰
    与灵敏度是否足以检出低浓度危害；④ 样品须能代表整批。
    供应商可自行检测并出具 COA 代替采购方检测，但采购方必须审查评估并记录。
  tags: [principle, sampling, testing, method-selection, frequency]

- id: p5_23
  title: 批准供应商的四项必虑因素
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.7.4）
  source_quote: |
    Section 21 CFR 117.410(d)(1) specifies factors that you must consider in approving suppliers and
    determining appropriate supplier verification activities ...: [i] the hazard analysis ...; [ii]
    the entity or entities that will be applying controls for the hazards requiring a supply-chain-
    applied control; [iii] supplier performance ...; [iv] any other factors as appropriate and
    necessary, such as storage and transportation practices.
  summary: |
    每次批准供应商、每次确定验证活动与频次时，四因素必虑（仅 15.7.4.5 例外可减）：
    ① 危害分析——危害性质决定验证强度（SAHCODH 危害→首次使用前+每年现场审核）；
    ② 控制危害的实体——可能是直接供应商或其上游，验证对象随之指向；
    ③ 供应商表现——程序/实践、适用的 FDA 法规合规情况（警示函、进口警报、
    强制召回等执法行动）、与所购原料相关的食品安全历史（检测、审核结果、
    问题响应速度）；④ 其他因素——储存运输实践（如需控温运输、
    需防霉储存的原料）。
    规则：风险越高，验证越严格、越频繁。
  tags: [principle, supplier-approval, four-factors, risk-proportional, checklist]

- id: p5_24
  title: 供应商表现审查可查阅公开执法信息但不一票否决
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.7.4.3.2）
  source_quote: |
    Being subject to an FDA enforcement action such as a warning letter or an import alert should not
    necessarily disqualify a supplier. However, you should consider carefully the actions a supplier
    has taken as a result of regulatory compliance issues along with how it impacts your approval of
    that supplier and your verification activities.
  summary: |
    评估供应商合规表现时可用公开渠道：FDA 在线数据库检索警示函、
    进口警报、进口拒绝、召回与检查记录；检索疫情调查、注册暂停等公开行动；
    要求供应商提供近期监管检查文件。
    判定规则：被采取执法行动（警示函/进口警报）不必然取消资格——
    关键看供应商事后采取了什么整改行动、以及该历史如何影响你的批准决定
    和验证活动的类型与频次。
    FDA 已与澳大利亚、加拿大、新西兰签订体系互认安排，可用对应国家法规信息。
  tags: [principle, supplier-performance, warning-letter, import-alert, evaluation]

- id: p5_25
  title: SAHCODH 危害：首次使用前审核+每年审核+13–14 个月宽限
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.11.2.1）
  source_quote: |
    when a hazard in a raw material or other ingredient will be controlled by the supplier and is one
    for which there is a reasonable probability that exposure to the hazard will result in serious
    adverse health consequences or death to humans (SAHCODH hazard): The appropriate supplier
    verification activity is an onsite audit of the supplier; and The audit must be conducted before
    using the raw material ... and at least annually thereafter. ... We do not expect to take action
    if the timeframe between annual audits is reasonably close to one year (e.g., within 13-14
    months).
  summary: |
    危害由供应商控制且属 SAHCODH（暴露有合理概率导致严重健康后果或死亡，
    对应 Class I 召回）时，硬性要求两条：① 适当的验证活动只能是现场审核；
    ② 使用该原料之前必须完成审核，此后至少每年一次。
    执行宽限：两次年度审核间隔接近一年（如 13–14 个月）FDA 不采取行动
    （考虑第三方审核员改期等现实原因）。
    含 SAHCODH 危害的食品即"可报告食品"，触发 RFR 义务。
    数值界限：每年至少 1 次；宽限窗口 13–14 个月。
  tags: [principle, SAHCODH, onsite-audit, numeric-boundary, 13-14-months, recurring]

- id: p5_26
  title: SAHCODH 年审豁免须 PCQI 书面认定，非同集团供应商建议仍保留 2–3 年审核
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.11.2.2）
  source_quote: |
    The exception to the requirement to conduct an annual onsite audit ... is when there is a written
    determination that other verification activities and/or less frequent onsite auditing of the
    supplier provide adequate assurance that the hazards are controlled. ... we recommend that your
    supplier verification activities generally include some frequency of onsite auditing, such as every
    2 or 3 years for most suppliers not in your same corporate structure.
  summary: |
    唯一例外：PCQI 编制（或监督编制）的书面认定——其他验证活动和/或
    更低频的现场审核能提供充分保证。该书面认定属于食品安全计划的一部分。
    示例：同一母公司体系下的子公司供应商，可凭母公司统一食品安全体系
    及集团验证活动记录替代年审。
    对集团外的多数供应商，即使豁免年审，也建议保留某种现场审核频次
    （每 2 或 3 年），并在无审核年份做每季度抽样检测（如"两年一审+隔年季度检测"组合）。
    规则：豁免不是免除证据——替代方案与历史合规证据都要成文。
  tags: [principle, SAHCODH, exception, written-determination, PCQI]

- id: p5_27
  title: qualified facility 替代验证：年度资格保证+两年合规保证
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.11.3）
  source_quote: |
    Obtain written assurance that the supplier is a qualified facility as defined by § 117.3: Before
    first approving the supplier for an applicable calendar year; and On an annual basis thereafter,
    by December 31 of each calendar year ...; and Obtain written assurance, at least every 2 years,
    that the supplier is producing the raw material ... in compliance with applicable FDA food safety
    regulations ...
  summary: |
    供应商是 qualified facility（极小企业：前 3 年年均食品销售额低于
    50 万美元（经通胀调整），或直接对 qualified end-users 销售为主）时，
    可用书面保证替代四类验证活动（含 SAHCODH 年审义务）。两份保证：
    ① 年度保证其 qualified facility 身份——首次批准前取得，此后每年
    12 月 31 日前为下一年度取得；② 至少每 2 年一次的合规保证——内容二选一：
    简述其为控制相关危害所实施的预防控制，或声明其遵守州/地方/部落等
    非联邦食品安全法（或 FDA 互认国家法规）。
    供应商自行判定身份，采购方负责索取书面保证；供应商可提供其提交 FDA 的
    Form 3942a 副本供使用。数值界限：50 万美元门槛、每 2 年、12 月 31 日前。
  tags: [principle, qualified-facility, written-assurance, numeric-boundary, 500000-dollars, biennial]

- id: p5_28
  title: 非覆盖农场替代验证：年度身份保证+两年 402 条确认
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.11.4）
  source_quote: |
    if a supplier is a farm that grows produce and is not a covered farm under the produce safety
    regulation ... Obtain written assurance that the raw material or other ingredient provided by the
    supplier is not subject to the produce safety regulation ...: Before first approving the supplier
    for an applicable calendar year; and On an annual basis thereafter, by December 31 ...; and Obtain
    written assurance, at least every 2 years, that the farm acknowledges that its food is subject to
    section 402 of the FD&C Act.
  summary: |
    供应商为非覆盖农场（non-covered farm）时的替代验证：
    ① 年度书面保证其农产品不受 produce safety regulation（21 CFR part 112）
    约束——首次批准前+此后每年 12 月 31 日前；② 至少每 2 年的书面保证——
    确认其知悉食品受 FD&C 法案 402 条约束（或互认国家法规）。
    判定依据：前 3 年农产品年均销售额低于 2.5 万美元（§112.4(a)）即非覆盖农场；
    或符合合格豁免条件（§112.4(b)/112.5）且 FDA 未撤销豁免。
    供应商自判身份，采购方负责索取书面保证。
    数值界限：2.5 万美元年销售额、每 2 年。
  tags: [principle, produce-farm, covered-farm, numeric-boundary, 25000-dollars, written-assurance]

- id: p5_29
  title: 小型蛋鸡场替代验证：少于 3000 只蛋鸡
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.11.5）
  source_quote: |
    if a supplier is a shell egg producer that is not subject to the requirements of 21 CFR part 118
    ... because it has less than 3,000 laying hens ... Obtain written assurance that the shell eggs
    produced by the supplier are not subject to 21 CFR part 118 because the shell egg producer has
    less than 3,000 laying hens: Before first approving the supplier ...; and On an annual basis
    thereafter, by December 31 ...; and Obtain written assurance, at least every 2 years, that the
    shell egg producer acknowledges that its food is subject to section 402 of the FD&C Act.
  summary: |
    供应商为壳蛋生产者且少于 3000 只产蛋鸡（故不受 21 CFR part 118 约束）时，
    可用替代验证：① 年度书面保证其壳蛋因蛋鸡少于 3000 只而不受 part 118
    约束——首次批准前+此后每年 12 月 31 日前；② 至少每 2 年书面确认
    其食品受 FD&C 法案 402 条约束。
    同 qualified facility 与非覆盖农场两条：供应商自判身份、采购方负责索取保证。
    这三类替代验证与 15.7.4.5 的"仅查合规史"例外互为表里。
    数值界限：3000 只蛋鸡、每年、每 2 年。
  tags: [principle, shell-eggs, numeric-boundary, 3000-hens, written-assurance, biennial]

- id: p5_30
  title: 三类小供应商的简化例外：只查合规史
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.7.4.5）
  source_quote: |
    Section 117.410(d)(2) provides that considering supplier performance can be limited to the
    supplier's compliance history ..., if the supplier is: (i) A qualified facility as defined by 21
    CFR 117.3; (ii) a farm that grows produce and is not a covered farm under 21 CFR part 112 ...; or
    (iii) a shell egg producer that is not subject to the requirements of 21 CFR part 118 because it
    has less than 3,000 laying hens.
  summary: |
    批准供应商四因素中的"供应商表现"审查，对三类供应商可简化为只查合规历史：
    ① qualified facility（极小企业）；② 非覆盖农场；③ 少于 3000 只蛋鸡的
    壳蛋生产者。即无须审查其程序/实践细节与食品安全历史全貌。
    这是对中小上游供应商的义务减负设计，与其在 117.430 下的替代验证活动
    （书面保证制）配套。规则：识别供应商所属法定类别是选择审查深度的前提。
  tags: [principle, supplier-performance, simplified-review, small-supplier, exemption]

- id: p5_31
  title: 经济利益冲突禁止：报酬不得与验证结果挂钩
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.11.6）
  source_quote: |
    there must not be any financial conflicts of interests that influence the results of the
    verification activities listed in 21 CFR 117.410(b). ... payment must not be related to the
    results of the activity. For example, you may not give a qualified auditor who conducts an onsite
    audit ... greater compensation for determining that a supplier is in compliance ...; Also, you may
    not reduce the compensation of a qualified auditor ... or assess financial penalties because the
    qualified auditor ... identified areas of supplier noncompliance. Similarly, a supplier may not
    make such payments.
  summary: |
    验证活动不得受经济利益冲突影响，且报酬不得与活动结果挂钩：
    ① 不得因审核员"判定合规"而多付报酬；② 不得因审核员发现不符合项
    而减薪或罚款；③ 供应商也不得进行此类支付。
    有利益冲突的合格人员不得独立执行验证活动。
    边界澄清：不禁止供应商员工为其自证做抽样检测（提供 COA 是允许的），
    也不禁止依赖第三方合格审核员对供应商做的审核。
    规则：审核独立性靠报酬结构保障，不只靠职业操守。
  tags: [principle, conflict-of-interest, auditor-independence, payment, supply-chain]

- id: p5_32
  title: 供应商不能自审自证：四项禁止接受的活动
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.8.3）
  source_quote: |
    a receiving facility may not accept any of the following as a supplier verification activity from
    its supplier: A determination by its supplier of the appropriate supplier verification activities
    for that supplier; An audit conducted by its supplier of that supplier; A review by its supplier
    of that supplier's own relevant food safety records; or The conduct by its supplier of other
    appropriate supplier verification activities for that supplier.
  summary: |
    供应商不得充当自己的验证者，四项一律不可接受：① 供应商自行决定
    对其适用的验证活动；② 供应商对自身的审核；③ 供应商审查自己的
    相关食品安全记录；④ 供应商对自己执行的其他验证活动。
    供应商唯一可以扮演的角色：对其所控危害做抽样检测并提供文档（如 COA），
    以及提供由第三方合格审核员对其所做的审核——两者采购方仍须审查评估并记录。
    规则：自我验证在合规体系里零效力；独立第三方是底线。
  tags: [principle, self-verification, prohibition, supply-chain, third-party, recurring]

- id: p5_33
  title: 只从批准供应商收货；临时供应商须用前充分验证
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.9.2）
  source_quote: |
    Written procedures for receiving raw materials and other ingredients must be established and
    followed ...; The written procedures ... must ensure that raw materials and other ingredients are
    received only from approved suppliers (or, when necessary and appropriate, on a temporary basis
    from unapproved suppliers whose raw materials or other ingredients are subjected to adequate
    verification activities before acceptance for use) ...; Use of the written procedures ... must be
    documented.
  summary: |
    必须建立并遵循接收原料的书面程序，确保原料只从已批准供应商接收，
    且程序的使用情况要形成记录。唯一例外通道：必要时可临时从未批准供应商
    进货，但其原料在投入使用前必须经过充分验证活动（如逐批沙门氏菌检测、
    审查其杀菌工艺记录），并记录所做验证。
    程序可落在"批准供应商清单"勾选、计算机系统拦截未批准供应商等机制上；
    若依赖经纪商/分销商执行，应与其约定文档方式（如逐票核对清单）供审查。
  tags: [principle, receiving-procedures, approved-supplier, temporary-supplier, verification]

- id: p5_34
  title: 临时供应商只用过渡期，且应多供应商冗余
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.9.2）
  source_quote: |
    You should use unapproved suppliers only on a temporary basis until you are able to fully evaluate
    and approve a new supplier ... An appropriate time period for use of an unapproved supplier on a
    temporary basis might vary ... from a few weeks to a few months. ... Having multiple suppliers
    approved for each raw material or ingredient you receive can reduce the use of temporary suppliers
    when one supplier becomes unavailable.
  summary: |
    临时启用未批准供应商的场景：地震/极端天气等环境事故、独家供应商
    重大设备故障、供应商出现污染问题、供应商未预告即停业。
    使用前至少做最低限度审查（查 FDA 网站有无警示函/进口警报）；
    使用时长限于过渡期——数周至数月，期间应尽快完成正式评估批准；
    若预计将长期使用，必须立即按完整程序批准并修订供应链程序。
    预防措施：每种原料批准多个供应商，减少被迫走临时通道的机会。
    数值界限：临时期数周至数月。
  tags: [principle, temporary-supplier, emergency, redundancy, supply-chain]

- id: p5_35
  title: 供应商不符合项的及时处置与文档化
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.7.5）
  source_quote: |
    if you determine through auditing; verification testing; document review; relevant consumer,
    customer or other complaints; or otherwise that the supplier is not controlling hazards that you
    have identified as requiring a supply-chain-applied control, you must take and document prompt
    action in accordance with 21 CFR 117.150 ... The appropriate actions ... could include:
    Discontinuing use of the supplier until the cause or causes ... are adequately addressed; ...
    Assisting the supplier's efforts to correct and prevent recurrence ...
  summary: |
    通过审核、验证检测、文档审查、消费者/客户投诉等任何渠道发现供应商
    未控制已识别危害时，必须按 117.150 及时采取行动并记录，
    确保其原料不会导致你的食品掺假或错标。
    可选行动清单：① 停用该供应商直至根因充分解决；② 通知供应商问题
    并索取其纠正措施文档；③ 协助供应商纠正与防复发；④ 修订自己的
    供应链程序；⑤ 与供应商联合召回掺假/错标食品。
    规则：发现问题→及时行动→书面记录，三件套缺一不可。
  tags: [principle, nonconformance, corrective-action, supplier, checklist]

- id: p5_36
  title: 供应链程序 18 项记录清单
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.13 表 15-4）
  source_quote: |
    Table 15-4 lists the records required (as applicable) for the supply-chain program. (See 21 CFR
    117.475(c).) ... records of the supply-chain program must be reviewed within a reasonable time
    after the records are made by (or under the oversight of) a PCQI to ensure that the records are
    complete, the activities reflected in the records occurred in accordance with the food safety
    plan, the preventive controls are effective, and appropriate decisions were made about corrective
    actions.
  summary: |
    117.475(c)(1)–(18) 列明供应链程序的全部法定记录：① 书面供应链程序；
    ② 进口商 FSVP 合规文档；③ 供应商批准文档（批准依据+批准清单）；
    ④ 接收书面程序；⑤ 程序使用证明；⑥ 验证活动的选择决定文档；
    ⑦ 现场审核文档（供应商名、程序、日期、结论、纠正措施、合格审核员资质）；
    ⑧ 抽样检测文档（样品与批号、方法、日期、结果、纠正、实验室）；
    ⑨ 记录审查文档；⑩ 其他验证活动文档；⑪ SAHCODH 替代方案书面认定；
    ⑫–⑭ qualified facility/非覆盖农场/小型蛋鸡场替代验证的两份书面保证；
    ⑮ 替代审核的检查结果；⑯ 供应商不符合项处置；⑰ 对非供应商实体所施控制的验证；
    ⑱ 对他方文档的审查评估记录。所有记录须由 PCQI（或其监督下）在合理时间内审查。
  tags: [principle, records, 18-items, checklist, 117-475, PCQI-review]

- id: p5_37
  title: 政府检查可替代现场审核的条件与边界
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.12.3）
  source_quote: |
    ... the following inspections to substitute for an onsite audit, provided that the inspection was
    conducted within 1 year of the date that the onsite audit would have been required to be
    conducted: The written results of an appropriate inspection of the supplier for compliance with
    applicable FDA food safety regulations ...; ... We would not accept a HACCP certificate issued by
    a foreign government as a substitute for an onsite audit because HACCP requirements are not
    identical to the PCHF requirements ...
  summary: |
    FDA、其他联邦机构（如 USDA）、州/地方/部落/领地机构对供应商的
    合规检查书面结果可替代现场审核，前提：检查在审核应做之日起 1 年内完成，
    且检查与 FDA 食品安全法规充分相关——USDA 为农产品安全法规做的检查合格，
    为 National Organic Program 做的检查不合格。外国供应商可用 FDA 或
    互认国家食品安全主管部门的检查结果，且食品须在互认范围内。
    边界：外国政府颁发的 HACCP 证书不可替代现场审核（HACCP 要求与 PCHF
    不等同、发证依据不明），但可作为其他验证活动的考量因素之一。
    数值界限：1 年内。
  tags: [principle, inspection-substitution, onsite-audit, numeric-boundary, HACCP-certificate]

- id: p5_38
  title: 供应链合规日期按供应商逐个计算
  type: principle
  source_chapter: 第 15 章 · 供应链程序（15.14）
  source_quote: |
    The compliance dates for implementing your supply-chain program apply with respect to each of your
    suppliers, not to your supply-chain program as a whole, because the compliance dates depend on
    whether your suppliers will be subject to part 117, the produce safety regulation, or neither
    regulation. For those suppliers subject to part 117 or the produce safety regulation, you are not
    required to conduct supplier verification activities until after your supplier's compliance date is
    reached.
  summary: |
    供应链程序的合规日期不是"一刀切"的设施级日期，而是逐供应商确定：
    取决于该供应商是否受 part 117 或农产品安全法规约束。
    若供应商受上述法规约束，则在其自身合规日期到达之前，收货设施
    无须对该供应商开展验证活动；供应商不受任何一部法规约束时，
    按收货设施自身规模适用 2017-09-18（小企业）或 2017-03-17（非小企业）。
    规则：义务时点跟随控制义务主体，而非跟随自己。
  tags: [principle, compliance-dates, supplier-specific, supply-chain]

- id: p5_39
  title: 酸化食品记录保存 3 年，超过 PCHF 的 2 年
  type: principle
  source_chapter: 第 16 章 · 酸化食品（16.2.4、16.12）
  source_quote: |
    If a specific acidified food requirement exceeds the corresponding requirement of the PCHF rule,
    you must comply with the specific acidified food requirement. As discussed in section 16.12, part
    114 requires that you keep records required by part 114 for 3 years, which exceeds the 2-year
    record retention requirement in part 117 for records documenting the food safety plan and
    implementation of the food safety plan. (See 21 CFR 114.100(e) and 21 CFR 117.315.)
  summary: |
    双法规（108.25/part 114 与 PCHF）并行时的总规则：专项要求超出 PCHF
    对应要求的部分，必须遵守专项要求。
    最典型的是记录保存期：108.25(g) 与 114.100(e) 要求记录自生产之日起
    保存 3 年，超过 part 117 最长 2 年的保存期要求。
    本断言在 16.2.4、16.12 正文与附录 16-1 表中三处重复出现（本段内高频）。
    数值界限：3 年（酸化专项）＞ 2 年（PCHF）。
  tags: [principle, acidified-foods, records, 3-years, numeric-boundary, recurring]

- id: p5_40
  title: 容器编码无 PCHF 对应要求也必须遵守
  type: principle
  source_chapter: 第 16 章 · 酸化食品（16.13）
  source_quote: |
    Part 114 requires that each container or product be marked with an identifying code permanently
    visible to the naked eye. (See 21 CFR 114.80(b) for the complete requirements.) There is no
    corresponding requirement for coding in the PCHF rule. You must comply with all requirements for
    coding in 21 CFR 114.80(b) even though there is no corresponding requirement for coding in the
    PCHF rule.
  summary: |
    part 114 要求每个容器或产品标注肉眼永久可见的识别编码，
    PCHF 规则中完全没有对应要求——但这不构成免除理由，
    仍必须完整遵守 114.80(b) 的全部编码要求。
    这是"双法规体系下专项要求不可因 PCHF 缺位而豁免"的又一实例
    （与 3 年记录、Form 2541e 提交并列，附录 16-1 表中重复列出）。
    规则：两套法规是叠加关系而非替代关系，取并集义务。
  tags: [principle, coding, acidified-foods, dual-regulation, 114-80b, recurring]

- id: p5_41
  title: Form 2541e 纳入食品安全计划不免除提交义务
  type: principle
  source_chapter: 第 16 章 · 酸化食品（16.10.1、附录 16-1）
  source_quote: |
    the requirement in 21 CFR 108.25(c)(2) to submit Form FDA 2541e to FDA has no corresponding
    requirement in the PCHF rule. You must submit Form FDA 2541e to FDA as required by 21 CFR
    108.25(c)(2) even if you include Form FDA 2541e in your food safety plan. ... you must include
    your process controls in the food safety plan that you keep onsite even though you submit them to
    FDA on Form FDA 2541e, because the food safety plan must be kept onsite (see 21 CFR 117.315(d)).
  summary: |
    向 FDA 提交定值工艺（scheduled process）表单 Form 2541e 是 108.25(c)(2)
    的专项要求，PCHF 无对应义务；把 2541e 收进食品安全计划作为书面工艺控制
    使用（这是最省力的双合规做法），也不免除提交义务——提交照做。
    反向同样成立：即使已向 FDA 提交 2541e，食品安全计划仍必须现场留存
    包含工艺控制的版本（117.315(d)）。同一断言在 16.2.2、16.10.1 与
    附录 16-1 三处重复。另：Form 2541 注册是食品罐装企业注册，
    在 Form 3537 设施注册之外额外进行，二者不可互替。
  tags: [principle, Form-2541e, acidified-foods, dual-regulation, submission, recurring]

- id: p5_42
  title: 双法规可互相借用但只能部分满足
  type: principle
  source_chapter: 第 16 章 · 酸化食品（16.2.3）
  source_quote: |
    the procedures, practices, and processes that you establish and implement to comply with the
    requirements prescribed by 21 CFR 108.25 and part 114, and records that you establish and keep to
    comply with those requirements, could partially — but not fully — satisfy corresponding
    requirements of the PCHF rule. Likewise, the procedures ... that you establish and implement to
    comply with the requirements of the PCHF rule ... could partially — but not fully — satisfy
    corresponding requirements of 21 CFR 108.25 and part 114.
  summary: |
    酸化食品企业同时受 108.25/part 114 与 PCHF 约束，双向借用是允许的：
    part 114 的 pH 频繁测试记录可满足 PCHF 的监控记录要求，
    108.25(e) 的召回程序可满足 PCHF 召回计划，反之亦然。
    但借用只能"部分而非完全"满足——每套法规都有超出另一套的部分
    （如 2541e 提交、容器编码、3 年记录、危害分析无对应项）。
    策略：用 16.5 表 16-2 快速对照两套要求，逐项判断借用方向与补差项。
    规则：合规 = 两套义务的并集，借用只减少重复工作量，不减少义务总量。
  tags: [principle, dual-regulation, leverage, acidified-foods, partial-satisfaction]

- id: p5_43
  title: PCHF 召回计划要满足 108.25(e) 须加"通知 FDA"程序
  type: principle
  source_chapter: 第 16 章 · 酸化食品（16.10.4 表 16-6）
  source_quote: |
    the requirement in 21 CFR 108.25(e) for the recall procedures to include notifying FDA of any
    recalls has no corresponding requirement in the PCHF rule for a recall plan. Therefore, a written
    recall plan that you establish and implement to comply with the requirements of the PCHF rule
    could only satisfy all requirements of 21 CFR 108.25(e) regarding recalls if it also includes
    procedures for notifying FDA of any recalls.
  summary: |
    PCHF 书面召回计划（117.139 的四程序）整体满足 108.25(e) 召回程序要求的
    唯一缺口是"通知 FDA 任何召回"——该要求 PCHF 没有。
    因此酸化食品企业若想用一份召回计划覆盖两法，必须在计划中额外加入
    通知 FDA 的程序（反向借用 108.25(e) 程序满足 PCHF 则天然完备）。
    规则：做单一文件双合规时，先找出两套要求中互相缺位的那一项并补齐。
  tags: [principle, recall-plan, 108-25e, dual-regulation, acidified-foods]

- id: p5_44
  title: pH 4.6 是肉毒孢子萌发红线，但腐败菌可抬升 pH 击穿防线
  type: principle
  source_chapter: 第 16 章 · 酸化食品（16.3、16.9）
  source_quote: |
    When the pH of a food is 4.6 or below, spores of C. botulinum will not germinate and grow ...
    However, an acidified food can pose a risk of botulism if pH and other critical factors are not
    carefully controlled during processing ... the vegetative cells of some microorganisms of non-
    health significance (such as some spoilage bacteria, yeasts, and molds) can grow in an acid
    environment and, in so doing, cause the pH of the food to increase.
  summary: |
    pH ≤ 4.6 时肉毒梭菌孢子不萌发生长——这是酸化食品可常温存放、
    无须 LACF 级热处理的科学基础。但防线会被击穿：关键因子控制不当时，
    非健康显著微生物（腐败菌、酵母、霉菌）的营养细胞可在酸性环境中生长并抬升 pH；
    蜡状芽孢杆菌等还能产耐热耐酸孢子，热处理灭营养细胞不灭孢子。
    因此 part 114 要求定值工艺同时控制病原与非健康显著微生物，
    PCHF 框架下可将其识别为需要预防控制的生物危害。
    数值界限：pH 4.6。
  tags: [principle, pH, 4.6, numeric-boundary, C-botulinum, acidified-foods]

- id: p5_45
  title: 满足 117.4 培训不等于满足酸化专项培训，反之亦然
  type: principle
  source_chapter: 第 16 章 · 酸化食品（16.6、16.7 表 16-3/16-4）
  source_quote: |
    in general, satisfying the training requirements of 21 CFR 117.4 would not satisfy the specialized
    training requirements of 21 CFR 108.25(f) and 114.10. ... a person who satisfies the qualification
    requirements of the PCHF rule for a PCQI ... would not be qualified to supervise the processing
    and packaging of acidified foods unless that person also satisfies the specialized training
    requirements of 21 CFR 108.25(f) and 114.10.
  summary: |
    酸化专项培训（经 Commissioner 批准的学校完成规定课程，俗称
    Better Process Control School）与 PCHF 的 117.4(c) 主管人员资格、
    PCQI 资格互不替代：① 完成 BPCS 课程可满足 117.4(c) 的监管资格；
    ② 但满足 PCHF 资格者若未完成专项课程，仍不得监管酸化/热处理/包装操作。
    定值工艺还须由在酸化加工方面有培训与经验获取专家知识的合格人员建立（114.83）。
    规则：人员资质也遵循双法规并集原则，专项资质是独立门槛。
  tags: [principle, training, BPCS, PCQI, dual-regulation, acidified-foods]

- id: p5_46
  title: 108.25(d)：食品在市时的问题须通知 FDA（独立于 RFR）
  type: principle
  source_chapter: 第 16 章 · 酸化食品（附录 16-1）
  source_quote: |
    Notify FDA about problems when food is in commerce | 21 CFR 108.25(d) (problems include
    spoilage, process deviation, or contamination with microorganisms, the nature of which has
    potential health-endangering significance) | Notifying FDA about problems when an acidified food is
    in commerce is in addition to your responsibility to report problems to the Reportable Food
    Registry ...
  summary: |
    酸化食品在商业流通中出现腐败、工艺偏离或微生物污染（性质具有潜在
    危害健康意义）等问题时，必须通知 FDA（108.25(d)）。
    该义务与 RFR 报告义务相互独立、并行存在——即使某问题未达
    "可报告食品"门槛，也可能触发 108.25(d) 的通知义务，反之亦然。
    规则：多套报告义务并存时，按各自门槛分别履行，不能以已报其一为由免报其他。
  tags: [principle, notification, 108-25d, RFR, acidified-foods]
```

## 自检

- [x] 每条都是可直接应用的规则/断言（非思维结构）
- [x] 每条有明确原文摘录（≤100 英文单词）
- [x] 数值界限类候选带具体数字（24h RFR、13–14 个月、50 万美元、100 万美元/极小企业、2.5 万美元非覆盖农场、3000 只蛋鸡、pH 4.6、3 年/2 年记录、每年年审、每 2 年保证、12 月 31 日、1 年内检查替代）
- [x] 不做筛选（宁错杀）
- [x] "反复出现"判断仅限本段：p5_03（Miller C/Baker D 两处）、p5_07（14.1 与 16.11）、p5_25/32（15 章内多处呼应）、p5_39/40/41（Ch16 三处重复）已标注 recurring
