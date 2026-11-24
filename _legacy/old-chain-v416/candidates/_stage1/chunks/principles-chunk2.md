# 阶段 1 · 原则提取器 · 分块 2/6（source.md 第 3301–6600 行）

> 覆盖范围：Ch3 后半（湿/干环境二分法、化学危害、物理危害）、Ch4（五类预防控制）、Ch5（管理组件）、Ch6 前半（热处理设计与监控）。
> "是否反复出现"判断仅限本段。不做筛选（宁错杀）。

```yaml
- id: p2-01
  title: 冷食低于 41°F、热食高于 135°F（危险温区规则）
  type: principle
  source_chapter: Ch4 · 4.3.2 Time-Temperature as a Process Control
  source_quote: |
    The most general recommendation is to hold cold foods below 41°F (5°C) and to keep hot
    foods above 135°F (57°C). ... We call the temperature range of concern (41°F (5°C) to
    135°F (57°C)) the "danger zone."
  summary: |
    通用时间-温度控制基准：冷食保持 <41°F(5°C)，热食保持 >135°F(57°C)，
    两者之间是"危险温区"，病原菌在该区间呈对数生长。
    不仅要控温度，还要控制在危险温区内的累计暴露时间——
    传统经验法则是危险温区内不超过 4 小时，但实际安全上限取决于
    病原种类与食品支持生长的能力，可基于 US Food Code、附录 3 表 3-B
    或自有产品研究设定更精确的限值。
  tags: [principle, time-temperature, numeric-bound, danger-zone, rule-of-thumb]

- id: p2-02
  title: 两段式冷却协议（135→70°F 两小时内，70→41°F 再四小时内）
  type: principle
  source_chapter: Ch4 · 4.3.2.1 Cooling after Cooking
  source_quote: |
    The U.S. Food Code specifies the application of a two part cooling protocol ... First,
    drop the temperature from 135°F (57°C) to 70°F (21°C) within two hours. ... Second,
    after dropping the initial temperature to 70°F (21°C), you can take up to additional
    4 hours to get the product down to 41°F (5°C).
  summary: |
    烹后冷却是影响食品安全的关键工序：热食大体积冷却有时长达 36 小时，
    期间孢子（如 C. botulinum）会萌发生长。两段式冷却要求：
    第一段 135°F→70°F 必须在 2 小时内完成（此区间病原繁殖最快），
    第二段 70°F→41°F 可再花最多 4 小时。
    FSIS 对肉禽有等效替代方案：130→80°F 不超过 1.5 小时，
    80→40°F 不超过 5 小时。大体积食品建议用 blast freezer/冷却隧道/
    换热器/滚筒冰水等快速冷却手段。冷却是产毒孢子萌发的陷阱工序。
  tags: [principle, numeric-bound, cooling, two-stage, sporeformer]

- id: p2-03
  title: a_w 0.85 是病原生长的安全分界（S. aureus 界限）
  type: principle
  source_chapter: Ch4 · 4.3.3.1 Water activity as a Formulation Process Control
  source_quote: |
    Yeasts and molds can grow at low water activity; however 0.85 is considered the safe
    cutoff level for pathogen growth. Water activity of 0.85 is based on the minimum water
    activity for S. aureus growth.
  summary: |
    a_w ≤0.85 是病原营养细胞不能生长的安全界限，依据是 S. aureus 的
    最低生长水分活度。据此把食品分三类：a_w>0.85 湿性食品（需冷藏或
    其他屏障控病原）；a_w 0.60–0.85 中间水分食品（不需冷藏控病原，
    但因酵母霉菌而有货架期限制）；a_w<0.60 低水分食品（无需冷藏也有
    长货架期）。降低 a_w 有两条路径：配方（加盐/糖）和脱水。
    配方控制有两种做法：照搬科学已确立的配方流程，或自建流程并对
    成品取样检测 a_w 加以验证。
  tags: [principle, numeric-bound, water-activity, aw-0.85, formulation]

- id: p2-04
  title: a_w ≤0.92 抑制孢子萌发（双界限体系）
  type: principle
  source_chapter: Ch5 · Table 5-1 Application of Preventive Controls to Biological Hazards
  source_quote: |
    Reducing the water activity (e.g., by adding solutes such as sugar and salt) to 0.92
    or below will inhibit outgrowth of spores ... to 0.85 or below will inhibit growth of
    vegetative cells of pathogens.
  summary: |
    a_w 有两条防线数值：≤0.92 抑制芽孢萌发（outgrowth），
    ≤0.85 抑制营养细胞生长。设计配方控制时必须先明确目标是控
    营养细胞还是控孢子，因为两者界限相差 0.07。
    同时注意：a_w 控制只"阻止生长"，对已形成的 S. aureus 与
    B. cereus 呕吐型毒素无效——毒素一旦形成，任何配方控制都救不回来。
  tags: [principle, numeric-bound, aw-0.92, spore, toxin]

- id: p2-05
  title: pH 4.6 是 C. botulinum 孢子萌发的法定分界线
  type: principle
  source_chapter: Ch4 · 4.3.3.2 Acidity (pH) as a Formulation Process Control
  source_quote: |
    when the pH of a food is 4.6 or below, spores of C. botulinum will not germinate and
    grow. As a result, the pH of 4.6 is a dividing line for the purpose of determining
    whether a food ... is subject to part 113 as an LACF or part 114 as an acidified food.
  summary: |
    pH 4.6 是双法规分界：pH≤4.6 的食品 C. botulinum 孢子不萌发，
    故天然酸性食品不受 LACF（part 113）或酸化食品（part 114）管辖；
    pH>4.6 即低酸食品。酸化食品必须在预定时间内使成品平衡 pH 达到
    ≤4.6 并全程维持；平衡 pH 是所有配料达到天然平衡后的 pH，
    大颗粒食品可能需要数天——此时必须冷藏以防 C. botulinum 产毒。
    注意降 pH 主要是抑制而非杀菌：E. coli O157:H7 等可在酸性条件下
    长期存活。腐败菌产酸代谢会抬高 pH 破坏屏障，故酸化食品还需
    热处理杀灭营养细胞或用许可防腐剂替代。
  tags: [principle, numeric-bound, ph-4.6, botulinum, acidified-food]

- id: p2-06
  title: 金属异物 7–25 mm 是 FDA 支持执法的危害尺寸带
  type: principle
  source_chapter: Ch3 · 3.5 Physical Hazards
  source_quote: |
    FDA's Health Hazard Evaluation Board has supported regulatory action against products
    with metal fragments of 0.3 inches (7 mm) to 1.0 inches (25 mm) in length. Such
    fragments have been shown to be a hazard to consumers.
  summary: |
    金属碎片长度 7 mm–25 mm（0.3–1.0 英寸）是 FDA 卫生危害评估
    委员会支持执法的尺寸区间——该区间碎片可造成牙齿损伤、口咽割伤、
    肠道穿孔、窒息甚至死亡。玻璃碎片适用同一尺寸标准。
    控制手段：金属探测/X 射线、磁铁、筛网等物理分离，以及对高危
    设备（锯片、网状传送带、金属对金属接触部件）的定期检查。
    注意金属探测的局限：不锈钢难检出、物体取向影响检出能力
    （标定探 2 mm 球可能漏检 24 mm 长不锈钢丝）、产品导电性干扰。
  tags: [principle, numeric-bound, physical-hazard, metal, 7-25mm]

- id: p2-07
  title: 烹饪热处理通用目标 5D–7D；孢子目标 6D（90°C 10 min）
  type: principle
  source_chapter: Ch4 · 4.3.1.1 Lethal Heat Treatments (Cooking)
  source_quote: |
    Typically, we recommend a thermal process that achieves a 5D to 7D reduction for most
    cooking treatments. However, if the expected initial microbial load is low, a less
    severe thermal process may be adequate. For cooking processes that target pathogenic
    sporeformers such as C. botulinum type E and non-proteolytic types B and F (i.e.,
    194°F (90°C) for 10 min), generally a 6D reduction ... is suitable.
  summary: |
    烹饪类热处理以最耐热的目标病原为基准：大多数烹饪处理推荐
    5D–7D 减少；初始菌量低时可放宽。针对致病孢子形成菌
    （C. botulinum E 型与非蛋白分解 B/F 型）时通常 6D，
    参考条件 90°C/194°F 保持 10 分钟；6D 工艺时间可按目标病原查
    附录 3 表 3-D（L. mono 为目标）与 3-E（非蛋白分解 C. botulinum B 型为
    目标）。热处理只杀营养细胞、不灭孢子、不消除已形成的毒素
    （S. aureus / B. cereus 呕吐毒素）——技术上不可能降到零。
  tags: [principle, numeric-bound, lethality, 5D-7D, 6D, cooking]

- id: p2-08
  title: 技术上不可能把微生物降到零
  type: principle
  source_chapter: Ch4 · 4.3.1.1 Thermal Destruction of Microorganisms
  source_quote: |
    Importantly, it is not possible to technically achieve a level of reduction to zero, or
    "no microorganisms"; instead, as a technical matter the probability of finding the
    organism becomes less likely as the magnitude of reduction increases.
  summary: |
    任何致死处理都只是概率游戏：每增加 1D，残存概率降 10 倍，
    但"零微生物"在技术上不可达。5D 处理是把 10,000 细胞/克降到
    每 10 克 1 个细胞的概率水平。这条原则反驳了"检测合格=无病原"
    的幻觉，也是抽样检测天然有漏检风险的理论根源——
    安全来自过程设计，不来自终产品检测。
  tags: [principle, lethality, zero-limit, detection-limits]

- id: p2-09
  title: 辐照获批用途与剂量上限表（0.3–44 kGy）
  type: principle
  source_chapter: Ch4 · 4.3.1.3 Irradiation as a Lethality Process Control
  source_quote: |
    Radiation treatment at doses of 2–7 kiloGray (kGy), depending on the source of
    radiation and the food, have been reported to effectively eliminate potentially
    pathogenic non-sporeforming bacteria ... Bacterial spores are more resistant to
    irradiation than non-sporeforming bacteria.
  summary: |
    辐照对非孢子形成病原的有效剂量一般为 2–7 kGy（D10 值：Vibrio
    0.02–0.14、Salmonella 0.18–0.92、L. mono 0.20–1.0 kGy 等，冷冻食品
    约翻倍）。21 CFR 179.26(b) 各用途剂量上限（截至 2016 年 4 月）：
    猪肉旋毛虫 0.3–1 kGy；家禽 4.5 kGy（冷冻 7.0）；鲜肉 4.5/7.0 kGy；
    带壳鲜蛋 3.0 kGy；发芽种子 8.0 kGy；贝类 5.5 kGy；生菜菠菜 4.0 kGy；
    甲壳类 6.0 kGy；干香料草本 ≤30 kGy；干酶制剂 ≤10 kGy；
    NASA 航天肉 ≥44 kGy。获批剂量不能消除孢子。辐照在美国按
    食品添加剂管理，需 FDA 上市前批准；按食品添加剂法规使用的
    辐射源不需纳入危害分析。
  tags: [principle, numeric-bound, irradiation, dose-table, kGy]

- id: p2-10
  title: HPP 商用压力 600–700 MPa，孢子最耐压需配热或酸或冷藏
  type: principle
  source_chapter: Ch4 · 4.3.1.2 High Pressure Processing (HPP)
  source_quote: |
    High pressure processing of foods requires pressures of 400 to 700 MPa ... Most
    commercial food industry applications use pressures in the range of 600 to 700 MPa.
    Bacterial spores are well established as the most pressure-resistant biological forms
    known.
  summary: |
    HPP 需 400–700 MPa（4000–7000 bar），商用多为 600–700 MPa，
    批式处理 1–20 分钟。细菌孢子是最耐压的生物形态，单独靠高压
    无法灭活，通常需加热配合。因此 HPP 的最佳适用对象是酸性食品
    和 HPP 后冷藏的食品（后者提供孢子控制）——C. botulinum 是
    最耐压最危险的微生物，是高压工艺设计的核心挑战。
    寄生虫参考：旋毛虫 >200 MPa 10 min 可灭；隐孢子虫卵囊
    5.5×10^8 Pa 60 秒无感染性。
  tags: [principle, numeric-bound, HPP, MPa, spore]

- id: p2-11
  title: Validation 豁免清单：过敏原/卫生/召回/供应链不需 validation
  type: principle
  source_chapter: Ch4 · 4.2 Overview of Preventive Controls
  source_quote: |
    You do not need to validate: (1) Food allergen controls; (2) sanitation controls;
    (3) the recall plan; and (4) the supply-chain program. You also do not need to
    validate other preventive controls, if the ... qualified individual prepares ... a
    written justification that validation of the other control is not applicable.
  summary: |
    法定四类预防控制豁免 validation（科学有效性确认）：
    过敏原控制、卫生控制、召回计划、供应链计划。
    其余控制若 PCQI 以书面论证说明"基于危害性质与控制性质，
    validation 不适用"，也可豁免。除此之外的工艺控制都必须由
    PCQI 执行或监督 validation。豁免 validation ≠ 豁免管理组件——
    监控、纠正措施、verification、记录仍然适用。
  tags: [principle, rule, validation, exemption-list]

- id: p2-12
  title: 发现偏差即假定自上次合格检查起全程未受控
  type: principle
  source_chapter: Ch5 · 5.5.2 Monitoring
  source_quote: |
    If a measurement shows that a deviation from the control value has occurred, you
    should assume that the control value had not been met since the last check in which
    the value was acceptable. As a result, the greater the time span between measurements,
    the more products you are putting at risk.
  summary: |
    监控发现失控时，受影响产品范围的默认推定是"自上次合格检查起
    全部未受控"——不是从发现时刻起。因此监控频次直接决定风险敞口
    大小：两次测量间隔越长，处于风险中的产品越多。
    即使有连续监控，也必须定期（至少每天一次）人工核查连续记录
    是否出现偏离。校准同理：仪器不准时须回溯评估自上次校准以来的
    记录，校准频次低的体系有更多产品暴露于风险。
  tags: [principle, monitoring, deviation, retrospective-assumption]

- id: p2-13
  title: correction 与 corrective action 的判定边界
  type: principle
  source_chapter: Ch5 · 5.5.3 Corrective Actions and Corrections
  source_quote: |
    Corrections may be appropriate instead of corrective actions when minor, isolated
    problems occur that do not directly impact product safety. ... if you observe food
    residue on "clean" equipment prior to production, corrections would involve
    re-cleaning and sanitizing the equipment before it is used.
  summary: |
    判定用 correction 还是完整 corrective action 程序，边界是两个条件：
    ①问题是否已直接影响到产品安全（生产前发现残留→只需重洗设备，
    无涉及产品）；②问题是轻微孤立的还是反复的。
    Correction 不强制记录（及时+轻微+孤立三条件满足时），
    但建议记录以便发现设备劣化趋势。
    Corrective action 四目标：纠正问题、降低复发可能、评估所有受影响
    食品、防止未经评估的食品入市。未预见的食品安全问题仍须采取
    全套纠正措施并再分析 FSP 相应部分。
  tags: [principle, rule, correction, corrective-action, decision-boundary]

- id: p2-14
  title: 关键限值偏差反复出现=程序无效=触发再分析
  type: principle
  source_chapter: Ch5 · 5.5.3 Corrective Actions and Corrections
  source_quote: |
    Evaluation of historical corrective action records can help to identify recurring
    problems. When critical limit deviations frequently reoccur, the process and the Food
    Safety Plan may need reanalysis and modification.
  summary: |
    孤立偏差可按既定程序处理；同一问题反复出现则说明控制程序本身
    无效，必须回溯历史纠正措施记录识别重复模式，并对工艺和 FSP
    （或其相关部分）进行再分析修改。重大变更需要正式管理流程：
    重新发放表单、再培训员工、分阶段实施、更新标签、通知供应商。
  tags: [principle, recurrence, reanalysis, corrective-action]

- id: p2-15
  title: 监控程序四问：What / How / How often / Who
  type: principle
  source_chapter: Ch5 · 5.5.2 Monitoring
  source_quote: |
    To fully describe your monitoring program, the procedures should answer four
    questions: (1) What will be monitored? (2) How will monitoring be done? (3) How
    often will monitoring be done (frequency)? (4) Who will do the monitoring?
  summary: |
    完整的监控程序必须回答四问：监控什么（与危害控制直接相关的
    参数或活动）、怎么监控（方法与设备）、多久监控一次（频次要能
    捕捉正常波动并发现偏离，连续监控最理想）、谁监控（写明岗位，
    执行者须具备相应教育/培训/经验）。
    监控记录可用 exception records——只在失控时才建立记录，
    大幅降低记录负担。
  tags: [principle, checklist, monitoring, four-questions]

- id: p2-16
  title: 干区防沙门氏菌：主卫生区始终保持干燥，湿清洁后彻底干燥
  type: principle
  source_chapter: Ch3 · 3.3.5.3.2 Dry process environments + Ch4 · 4.4
  source_quote: |
    You should maintain dry conditions at all times in primary Salmonella-controlled
    hygiene areas, except for the occasions when you have determined that controlled wet
    cleaning is necessary. ... Any time water is used for cleaning, the equipment should
    be thoroughly dried before use.
  summary: |
    水是干加工环境沙门氏菌污染的单一最重要风险因素：哪怕极少量、
    短时间断续出现的水都足以让沙门氏菌生长；积水干掉后形成的
    含菌粉尘还会经空气传播。规则：沙门氏菌主控卫生区（RTE 食品
    暴露区）始终保持干燥；冷凝、阀门泄漏、暴雨渗漏、消防喷淋等
    事件后必须立即清除积水；采用干清洁或受控湿清洁，
    湿清洁后必须彻底干燥方可使用。低水分食品的接触面使用前必须
    处于清洁、干燥、卫生状态（21 CFR 117.35(d)(1)）。
  tags: [principle, rule, dry-environment, salmonella, moisture-control]

- id: p2-17
  title: 湿区防李斯特菌：尽可能保持环境干燥，警惕气溶胶扩散
  type: principle
  source_chapter: Ch3 · 3.3.5.3.1 Wet process environments
  source_quote: |
    The most effective strategy to prevent the contamination of finished products with
    L. monocytogenes is to maintain an environment as dry as possible. ... aerosols from
    high pressure water hoses used during cleaning operations help spread
    L. monocytogenes throughout the environment.
  summary: |
    反直觉核心原则：湿加工环境防李斯特菌的最有效策略恰恰是保持
    环境尽量干燥。湿地面是李斯特菌从环境源转移到接触面的载体
    （人员/设备/托盘流动传播）；高压水枪的气溶胶把细菌从地面
    溅到传送带、台面、产品容器上——因此避免地面漫水与高压冲洗，
    按需用水、分区隔离用水。湿清洁后的干燥步骤能抑制残存微生物
    生长。对固有湿工序（混合、烹煮、漂烫），目标是控制人流物流
    和清洁方式，最大限度减少积水与气溶胶。
  tags: [principle, wet-environment, listeria, aerosol, keep-dry]

- id: p2-18
  title: 常规清洁只控 transient 定殖菌须强化卫生程序根除
  type: principle
  source_chapter: Ch3 · 3.3.5.2 Transient vs resident environmental pathogens
  source_quote: |
    while common cleaning and sanitation practices are adequate to control the presence
    of transient contaminants, such practices do not control the presence of resident
    contaminants once they have become established. ... The facility will need to use
    intensified sanitation procedures to eliminate the contamination.
  summary: |
    环境病原分 transient（瞬时，常规清洁可控制）与 resident（定殖，
    藏匿于 niche 持续数月至数年）两种状态。一旦定殖，常规 SSOP 无效，
    必须用强化卫生程序根除。沙门氏菌和李斯特菌是定殖史最丰富的
    两种病原。卫生控制（人员规范+设备设施设计）的使命是防止
    transient 变 resident。定殖决定因素：环境温度、可利用水分、
    营养可及性——清洁的意义首先是断粮（去营养）。
  tags: [principle, resident-strain, transient, sanitation]

- id: p2-19
  title: 消毒剂必须按 EPA 注册标签使用
  type: principle
  source_chapter: Ch4 · 4.4.1 Cleaning and Sanitizing Food-Contact Surfaces
  source_quote: |
    You should use all sanitizers in accordance with the EPA-registered (or similar
    registration in other countries) label use instructions, including approval for use
    in food establishments.
  summary: |
    所有消毒剂必须严格按 EPA 注册标签（其他国家按同类注册）的
    使用说明执行，包括确认其获批用于食品企业。清洁四要素——时间、
    温度、机械力、化学浓度——只有当设备和设施设计允许充分接近
    所有表面时才能可靠施加，所以卫生设计是卫生控制的前提。
    清洁（去土壤=细菌营养源）与消毒（灭病原营养细胞）是两个概念，
    清洁后才消毒；能同时清洁+消毒的系统（如蒸汽）视为满足消毒定义。
  tags: [principle, rule, sanitizer, EPA-label, cleaning]

- id: p2-20
  title: EPIPT 三前提：热分布研究+热穿透研究+识别其他关键因素
  type: principle
  source_chapter: Ch4 · 4.3.1.1 EPIPT + Ch6 · 6.6
  source_quote: |
    If you want to monitor EPIPT, you should: Conduct a temperature distribution study
    within the heating system to identify any cold spots; Conduct a heat penetration
    study that accounts for the slowest heating product under the worst case heating
    conditions ...; and Identify other critical factors of processing and/or packaging.
  summary: |
    用"终点内部产品温度（EPIPT）"替代全程时间-温度监控有三个前提：
    ①热分布研究找出系统冷点；②热穿透研究覆盖最慢加热产品在
    最坏工况下的表现；③识别影响加热速率的其他关键因素。
    EPIPT 只能在科学研究覆盖的条件下使用，这些条件作为带最大/最小
    值的工艺参数被监控。EPIPT 一经确立即无时间维度——只监控
    成品温度（如每批测一次）。适用对象：汤、酱等可用搅拌锅
    对流加热的产品。
  tags: [principle, numeric-bound, EPIPT, validation-preconditions, heat-treatment]

- id: p2-21
  title: 大颗粒食品不能靠抽检粒子温度控烹饪——必须科学验证
  type: principle
  source_chapter: Ch4 · 4.3.1.1 Cooking (large particles)
  source_quote: |
    You cannot control cooking processes for products with large particles by
    periodically checking the internal temperature of some of the product particles as
    they leave the cooker because you cannot verify that each particle reached the
    appropriate temperature for adequate time. Therefore, you should establish the
    process scientifically and validate it through a scientific study.
  summary: |
    含大颗粒的食品（炖菜、浓汤中的蔬菜块）以传导加热为主，颗粒
    中心升温速率受颗粒大小与稠度支配。离开锅具时抽测若干颗粒的
    内部温度无法证明每个颗粒都达标——因此必须通过科学研究
    （通常由热处理专家/过程权威执行、PCQI 监督）确立工艺，
    证明只要满足所有关键因素（温度、时间、粒度上限等）的
    最大/最小值，所有颗粒都会得到充分热处理；粒度上限本身
    就是关键限值。
  tags: [principle, rule, large-particles, conduction, validation]

- id: p2-22
  title: 借用外部热处理数据须按自家产品调整
  type: principle
  source_chapter: Ch4 · 4.3 Process Controls (sources of parameters)
  source_quote: |
    You should use care when applying information from any of these sources to
    processing parameters for a specific product and process. ... the temperature (and
    time at that temperature) necessary to kill microorganisms in a food product can
    depend on the fat level in that food product.
  summary: |
    文献、政府指南（FSIS、EPA）、行业协会、过程权威、同行评审文献
    都可用于设定工艺参数，但照搬有风险：杀灭微生物所需的温度与
    时间取决于食品成分——脂肪含量升高、水分降低、蛋白质存在、
    高糖（降低 a_w）都会增强微生物耐热性；pH 偏离最适生长点则
    使其更敏感。借用参数必须按自家产品与工艺的差异调整。
  tags: [principle, heat-resistance, adaptation, parameters]

- id: p2-23
  title: 致死处理无法消除孢子与已形成的毒素（四类处理通用局限）
  type: principle
  source_chapter: Ch5 · Table 5-1 + Ch6 · 6.2
  source_quote: |
    In general, heat processes will not eliminate spores of bacterial pathogens ...
    Will not eliminate preformed toxins of S. aureus and B. cereus emetic toxin ...
    Therefore, if you use one of the heat treatments described in this chapter, you may
    need to establish and implement additional preventive controls to control spores.
  summary: |
    四类致死处理（热、辐照、HPP、抗菌熏蒸）的通用局限：
    ①都不能可靠消除细菌孢子（HPP 最耐压、辐照孢子更耐、
    PPO 熏蒸对孢子无效）；②都不能消除已形成的 S. aureus 与
    B. cereus 呕吐毒素；③孢子靠后续屏障控制——冷藏/冷冻/降 a_w
    至 0.92 以下/降 pH。热处理杀死营养细胞后，腐败竞争菌也被清除，
    温度滥用时孢子反而更容易萌发产毒。
  tags: [principle, spore-limitation, toxin, lethality]

- id: p2-24
  title: 召回计划四要素与两项提前准备
  type: principle
  source_chapter: Ch4 · 4.7 Recall Plan
  source_quote: |
    The written recall plan must include procedures ... (1) Directly notify the direct
    consignees ... (2) Notify the public ... (3) Conduct effectiveness checks ... and
    (4) Appropriately dispose of recalled food. ... Adequately code products to make
    possible positive lot identification ...
  summary: |
    存在需预防控制危害的食品必须建立书面召回计划，四程序：
    直接通知直接收货人（含退回/处置方法）、必要时通知公众、
    有效性核查、召回食品的妥善处置（重加工/改作他用/销毁）。
    两项提前准备可最小化召回冲击：①产品编码做到批次可正向识别；
    ②保存分销记录，保存期超过产品货架期与预期使用期。
  tags: [principle, checklist, recall-plan, four-elements]

- id: p2-25
  title: 操作限（operating limit）偏离只需 adjustment，不触发纠正措施
  type: principle
  source_chapter: Ch6 · 6.5 Terms Used in This Chapter
  source_quote: |
    we use the term "operating limit" to mean criteria that may be more stringent than
    critical limits and are established for reasons other than food safety. ... you could
    make an adjustment to the dough depositor if you observe that the amount of dough
    deposited exceeds the operating limit of 27 g, but does not exceed the critical
    limit of 28 g.
  summary: |
    操作限是比关键限更严格、基于非食品安全原因（通常是质量）的
    内控线。偏离操作限但未越关键限→只做 adjustment（调整）并记录，
    用于发现设备劣化趋势；越过关键限→触发纠正措施程序。
    例：饼干面团投料关键限 ≤28g，操作限 27g，投到 27.5g 只需调机。
    关键限与 117 法规中的"最大值/最小值"在 CCP 处无实质区别，
    可沿用 HACCP 术语。
  tags: [principle, rule, operating-limit, critical-limit, adjustment]

- id: p2-26
  title: EMA 危害分析看历史掺假模式并按原产国判断
  type: principle
  source_chapter: Ch3 · 3.4.1.6 Economically motivated adulteration
  source_quote: |
    We recommend that you focus on circumstances where there has been a pattern of such
    adulteration in the past, suggesting a potential for intentional adulteration even
    though the past occurrences may not be associated with the specific supplier or the
    specific food product.
  summary: |
    经济利益驱动掺假（EMA）的识别规则：聚焦历史上有掺假模式的
    情形——即使过去事件与本供应商或本产品无关。分析时同时考虑
    配料原产国与特定供应商两个维度。案例：某国乳品加三聚氰胺
    抬高表观蛋白含量（29 万婴幼儿患病、6 死亡），故从有掺假史的
    国家采购乳制品须把三聚氰胺纳入危害分析；无掺假史国家的
    国产/进口乳制品则不需考虑。判定为需控危害后通过供应链计划
    解决。工具：USP 食品欺诈数据库、137 起 EMA 事件报告。
  tags: [principle, EMA, food-fraud, country-of-origin]

- id: p2-27
  title: 进口农产品农药残留应按供应链控制管理
  type: principle
  source_chapter: Ch3 · 3.4.1.1 Pesticides
  source_quote: |
    Fruits and vegetables that have been grown in the United States usually are in
    compliance with EPA's pesticide tolerance regulations. If you obtain produce from a
    foreign country you should take steps to ensure that the imported produce will be in
    compliance with U.S. pesticide tolerance regulations, such as by considering
    pesticide residues to be chemical hazards that warrant preventive controls, such as
    supply-chain controls.
  summary: |
    美国本土种植的果蔬通常符合 EPA 农药残留限量；从外国采购的
    农产品则应把农药残留视为需要预防控制的化学危害，
    通过供应链控制+供应商验证程序确保合规。无残留限量或超限
    即掺假。类似逻辑适用于：兽药残留（按标签用药不应有残留；
    供应链控制）、真菌毒素（生长收成条件年际波动大，即使当年
    条件好也需要供应链控制）、重金属（种植区土壤评估）。
  tags: [principle, supply-chain, pesticide, imported-produce]

- id: p2-28
  title: 真菌毒素防控靠储藏水分控制+物理分选
  type: principle
  source_chapter: Ch4 · 4.3.6 / 4.3.7 Mycotoxin controls
  source_quote: |
    The principal process control for prevention of mold growth in storage conditions is
    the control of moisture. ... mycotoxins in raw agricultural commodities are present
    in a very small proportion of individual seeds or kernels. As a result, removing the
    contaminated seeds or kernels mechanically is a practical and effective process
    control.
  summary: |
    田间与储藏期霉菌生长的决定性环境因素是温度、水分、时间，
    而大规模储藏无法控低温，故水分控制是储藏期防霉的主控手段
    （不当干燥或返潮是污染根源）。由于真菌毒素只存在于极小比例
    的个别籽粒中，按颜色/损伤/霉变进行人工或电子分选去除
    污染籽粒是实用有效的工艺控制。注意：毒素已形成则无法消除，
    只能去除带毒籽粒。
  tags: [principle, mycotoxin, moisture-control, physical-sorting]

- id: p2-29
  title: 过敏原控制两支柱：防交叉接触+标签控制（生产排程与 like into like）
  type: principle
  source_chapter: Ch4 · 4.5 Food Allergen Controls + Ch5 · Table 5-4
  source_quote: |
    Schedule production of products that do not contain food allergens before production
    of products that do contain food allergens or schedule production of products with a
    unique food allergen last. ... using "like into like," appropriate storage and
    handling, tracking.
  summary: |
    过敏原控制两大支柱（117.135(c)(2)）：①防交叉接触——收货时
    标识含过敏原料、隔离储存、无过敏产品先排产/独特过敏原最后
    排产、物理分隔工序、专用清洁工具、返工遵循"like into like"
    （同类返工回同类产品）并做好追踪；②标签控制——每批新到标签
    都要做标签审核、建立正确贴标程序。八大过敏原（乳、蛋、鱼、
    甲壳类、坚果、花生、小麦、大豆）占美国食物过敏 90% 以上；
    贴错标签/用错包装（巧克力冰淇淋装到含杏仁款包装）本身就是
    化学危害。
  tags: [principle, allergen, scheduling, like-into-like, label-review]

- id: p2-30
  title: 硫化剂"偶带物质"豁免门槛：<10 ppm 且无技术作用
  type: principle
  source_chapter: Ch3 · 3.4.2.2 Sulfiting agents
  source_quote: |
    Sulfiting agents are considered to be incidental only if they have no technical
    effect in the finished food and are present at less than 10 parts per million (ppm)
    (21 CFR 101.100(a)(4)). The quantity of sulfiting agents added to food should not
    exceed the amount necessary to achieve the intended technical effect(s).
  summary: |
    六种硫化剂（SO2、亚硫酸钠、亚硫酸氢钠、焦亚硫酸钠等）在成品
    中同时满足"无技术作用"+"残留 <10 ppm"两个条件才视为偶带物质
    而免于标示；添加量不得超过达到预期技术作用所需的最小量。
    超最大使用水平即构成化学危害（无论该上限源于食品不耐受还是
    添加剂安全使用条件）——控制策略是配方管理防止误配方。
    Yellow No. 5 必须逐名标示；胭脂虫提取物/洋红按专属条款标示，
    不属于 117 的"食品过敏原"定义但控制策略类似。
  tags: [principle, numeric-bound, sulfites, 10-ppm, labeling]

- id: p2-31
  title: 危害分析无发现也必须书面记录该判定
  type: principle
  source_chapter: Ch5 · 5.1 Purpose of this Chapter
  source_quote: |
    Note that if you determine through your hazard analysis that there are no hazards
    requiring preventive controls, you must still document that determination in your
    written hazard analysis (see 21 CFR 117.130(a)(2)).
  summary: |
    即使危害分析结论是"没有需要预防控制的危害"，这个判定本身
    也必须写入书面危害分析。危害分析无论结论如何都必须书面化、
    由 PCQI 完成——空白即违规。这与全书"解释 No 与解释 Yes 同样
    重要"的主线一致：书面理由是对抗检查质疑的防线。
  tags: [principle, documentation, hazard-analysis, written-determination]

- id: p2-32
  title: 预定纠正措施程序的三重价值与四要素记录
  type: principle
  source_chapter: Ch5 · 5.5.3 Corrective Actions and Corrections
  source_quote: |
    A predetermined corrective action procedure has the following advantages: (1) It
    provides detailed instructions for an employee to follow in the event of a deviation
    ...; (2) it can be prepared at a time when an emergency situation is not calling for
    an immediate decision; and (3) it removes the obligation to reassess the food safety
    plan in response to a deviation.
  summary: |
    预先写好的纠正措施程序有三大价值：给员工偏离时的详细操作
    指引、在非紧急时刻从容制定、免于每次偏离都触发 FSP 再评估
    义务。纠正措施记录须含四要素：如何识别并纠正问题、
    如何降低复发可能、如何评估所有受影响食品的安全性、
    受影响食品的数量与处置去向。放行受影响产品须有书面依据
    证明偏离未造成食品安全危害；拒收/销毁也要记录。
  tags: [principle, corrective-action, four-elements, predetermined]

- id: p2-33
  title: 冷冻不是杀菌：-8°C 以下微生物学稳定但病原可长期存活
  type: principle
  source_chapter: Ch4 · 4.3.2.2 Freezing
  source_quote: |
    Foods are microbiologically stable when held at temperatures below 17.6°F (-8°C).
    During frozen storage, populations of viable microorganisms in most foods will
    decrease; however, some microorganisms remain viable for long periods of time ...
    you cannot count on freezing to eliminate pathogens.
  summary: |
    低于 -8°C（17.6°F）食品微生物学稳定（冻藏中多数食品活菌数下降），
    但多数病毒、细菌孢子、部分营养细胞可完好存活冻融；
    不能指望冷冻消灭病原。冷冻对多细胞寄生虫（原虫、线虫、吸虫）
    是有效致死手段，有既定时间-温度程序； Cyclospora 相对耐冻
    （树莓蛋糕 -3.3°C 冷冻后仍致暴发）。冷冻控生长对 S. aureus 与
    B. cereus 产毒有效，对已形成的毒素无效。
  tags: [principle, numeric-bound, freezing, -8C, parasites]

- id: p2-34
  title: 酸化食品须控腐败菌抬酸导致的肉毒反扑
  type: principle
  source_chapter: Ch4 · 4.3.3.2 Acidification
  source_quote: |
    the action of the spoilage organisms can raise the pH, compromising the safety of
    the product because any spores of C. botulinum that are in the food can germinate,
    grow, and produce botulinum toxin. The acidified foods regulation requires that you
    thermally process the food to an extent that is sufficient to destroy the vegetative
    cells of pathogenic and non-pathogenic microorganisms.
  summary: |
    酸化食品的安全屏障（pH≤4.6）会被腐败菌的代谢破坏：腐败菌
    抬高 pH 后，食品中的 C. botulinum 孢子即可萌发产毒。
    因此酸化食品法规要求热处理到足以杀灭在该食品储运条件下
    能繁殖的病原性与非病原性（腐败）微生物的营养细胞，
    或改用许可防腐剂抑制其繁殖。酸化食品还需 FDA 注册
    （Food Canning Establishment 编号）并向 FDA 提交 scheduled process。
    直接酸化须控酸-食品配比；批式酸化须充分平衡。
  tags: [principle, acidified-food, spoilage, ph-rise, botulinum]

- id: p2-35
  title: 冷却过程的再污染三通道：手接触、冷凝水滴、与其他食品接触
  type: principle
  source_chapter: Ch4 · 4.3.2.1 Cooling after Cooking
  source_quote: |
    Be advised that food can be recontaminated during the cooling process as a result of
    hand contact, condensate drip, or contact with other foods.
  summary: |
    即使致死步骤完美，冷却环节仍会把病原重新带入食品：人员手部
    接触、上方设备冷凝水滴落、与生/其他食品交叉接触。
    烹后食品在冷却是最脆弱窗口（腐败竞争菌已被清除、孢子萌发中），
    所以冷却是卫生控制与防再污染设计的重点工序。只有能灭活孢子
    且冷却期间有防再污染保护的工艺（少数加压蒸汽工艺），
    冷却步骤才不构成关键控制点。
  tags: [principle, recontamination, cooling, condensate]

- id: p2-36
  title: 监控仪器的连续记录检查频次：批次每批一次，连续设备每天一次
  type: principle
  source_chapter: Ch6 · 6.8.3 Frequency of Monitoring
  source_quote: |
    If you use a continuous temperature-recording device ... for monitoring, you should
    do a visual check of the recorded data at least once per batch. ... For the heating
    time of a continuous process, you should monitor the automated timers at least once
    per day or pump speed setting at least twice per shift.
  summary: |
    连续温度记录装置的人工目视核查频次：批式设备至少每批一次
    （EPIPT 每批必测）；连续设备至少每天一次；连续工序的自动计时器
    每天至少检查一次、泵速设定每班至少两次，且凡改动计时器/泵速
    后必须检查。连续设备温度记录仪应安装在经研究确定的冷点，
    大型烤箱须在顶部/中部/底部多点安装。热时间由记录启止时刻
    计算，可用定时器给出完成提示音/光。
  tags: [principle, numeric-bound, monitoring-frequency, batch, continuous]

- id: p2-37
  title: 湿加工区的含尘干燥积水与干区的双重风险
  type: principle
  source_chapter: Ch3 · 3.3.5.3.2 Dry process environments
  source_quote: |
    Potential problems arise when there is visible water present in the dry areas or
    when there are areas in which standing water has dried out. Salmonella may be found
    both in wet spots and in spots where standing water has dried ... The latter
    situation may present an additional risk of spread via the generation of airborne
    contaminated dust.
  summary: |
    干区出现水有两种状态，两种都危险：①可见积水——沙门氏菌
    直接生长繁殖；②积水已干——细菌留在干涸斑点上，还会随
    含菌粉尘经空气扩散传播（新增风险）。这意味着"水干了就没事"
    是错误认知；干区发现过水的区域本身就成了潜在藏匿点。
    配套判断：设备内部积水与高相对湿度这类"不明显水源"
    同样计入风险源。
  tags: [principle, dry-area, airborne-dust, standing-water]

- id: p2-38
  title: 生产品种确定是否需要卫生学分区及其范围
  type: principle
  source_chapter: Ch4 · 4.4.2 Hygienic Zoning
  source_quote: |
    The objective of hygienic zoning is to reduce the potential for transient pathogens
    to enter sensitive areas in the facility, such as packing areas where an RTE product
    is exposed to the processing environment. ... You should determine the need for, and
    scope of, a hygienic zoning program based on your facility, the products you make,
    and the outcome of your hazard analysis.
  summary: |
    卫生学分区的目标是减少 transient 病原进入敏感区（如 RTE 产品
    暴露于环境的包装区）。分区的必要性与范围不是一刀切：
    面粉厂、RTE 冷藏食品厂、罐装酸化食品厂的需求截然不同，
    须按工厂结构、包装、人流物流走向、交叉区域、原料潜在污染物、
    气流、辅助区域综合判定。分区维度：生 vs 在制品 vs 成品、
    湿 vs 干、人员/物料流向、空气压差平衡。
    注意：为控霉变等质量原因做的分区不算 PCHF 卫生控制——
    法定卫生控制只需覆盖食品安全。
  tags: [principle, hygienic-zoning, RTE, scope-determination]

- id: p2-39
  title: 设施相关化学危害通常走 CGMP 而非预防控制
  type: principle
  source_chapter: Ch3 · 3.4.3 Facility-Related Chemical Hazards
  source_quote: |
    In this guidance, we do not discuss preventive controls for facility-related chemical
    hazards such as cleaning chemicals and the leaching of heavy metals from containers
    or utensils, because such hazards are usually addressed through CGMPs.
  summary: |
    清洁剂残留、设备容器具重金属浸出等设施相关化学危害，
    通常由 CGMP（21 CFR 117.40 设备器具条款、117.37 水质条款）覆盖，
    不需要单独的预防控制。同理，来自顶灯灯具等的玻璃危害
    走 CGMP；木、石等原料相关物理危害通常走 CGMP 或供应链控制。
    分流规则：看危害的引入途径——设施/环境的系统性问题归 CGMP，
    配料与工艺环节的问题归预防控制或供应链控制。
  tags: [principle, CGMP, routing, heavy-metals, glass]

- id: p2-40
  title: 辐照与配方对营养细胞的差异效力：靠酸杀不了菌
  type: principle
  source_chapter: Ch5 · Table 5-1（Formulation 行）
  source_quote: |
    In, general, you can rely on added acid to prevent growth of vegetative bacterial
    pathogens, but you cannot rely on added acid to eliminate vegetative cells of
    bacterial pathogens.
  summary: |
    配方控制（加酸、a_w、防腐剂）与致死处理的效力边界：
    加酸能可靠地阻止营养细胞病原生长，但不能依赖它消灭营养细胞；
    降 a_w、干燥、冷冻同理只抑制不杀灭。即配方类控制是"生长控制"
    而非"杀灭控制"——若工艺逻辑需要消灭（如后续无其他屏障），
    必须用致死处理。防腐剂（山梨酸盐、丙酸盐、苯甲酸盐等）
    可同时抑制酵母霉菌与部分病原（如 L. mono、S. aureus），
    但对孢子只能阻止萌发不能消除。
  tags: [principle, formulation, inhibition-vs-kill, preservatives]
```

## 扫描备注

- **数值界限类**：p2-01/02/03/04/05/06/07/09/10/30/33/36 已带具体数字。
- **规则类**：p2-11/12/13/16/17/19/20/21/22/23/25/26/27/31/39 已按要求覆盖验证豁免清单、偏差回溯假定、消毒剂 EPA 标签、干区干燥/湿清洁后干燥、检测不能降为零（p2-08）。
- **ROP 五屏障**未出现在本段（位于 Ch3 前半/后续章节，属其他分块）；本段未识别到 ROP 内容。
- 本段内"反复出现"观察：湿/干二分法与"水是最重要风险因素"在 Ch3 与 Ch4 卫生节重复出现（p2-16/17/37/38）；"配方只抑制不杀灭"在 Ch4 与 Ch5 Table 5-1 重复（p2-23/40）；"书面判定义务"在 Ch5 重申（p2-31）。
