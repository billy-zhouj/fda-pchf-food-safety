# Stage 1 Framework Candidates — Chunk 2 (source.md 行 3301–6600)

> 覆盖范围: Ch3 后半（湿/干环境二分法、化学/物理危害）、Ch4 预防控制（热力杀菌学 D/z、a_w、pH、两段式冷却、清洁策略、辐照/熏蒸）、Ch5 管理组件（监控四问、correction vs corrective action、exception records）、Ch6 前半（热处理设计三步法、EPIPT、关键限值 vs 操作限）。
> 说明: 原文未见 "ROP 屏障" 内容（ROP 应在本块之前的行段），故本块无该条候选。

- id: f2-01
  title: 湿/干环境二分法（环境病原控制战略选择器）
  type: framework
  source_chapter: 第3章 3.3.5.3
  source_quote: |
    "Food processing operations can typically be classified into one of two simple categories –
    wet processing environments or dry processing environments... This very simple distinction has
    significant implications for the strategy that must be applied to control food contamination
    from environmental pathogens... The pathogen most often associated with cold and wet
    processing environments is L. monocytogenes, and the pathogen most often associated with
    warm and dry processing environments is Salmonella."
  summary: |
    把加工环境按温度×水分切成两个象限：冷藏/冷冻+湿、常温+干。
    每个象限对应一个"头号环境病原"：湿区=李斯特菌，干区=沙门氏菌。
    由此推出相反的卫生战略：湿区防李斯特菌的核心是"尽量保持干燥"（控制积水、冷凝水、气溶胶）；
    干区防沙门氏菌的核心是"严格控水"（任何微量、短时的水都可能让沙门氏菌定殖）。
    这是一个"环境分类→对手识别→战略反转"的思考结构：两类环境的最优清洁策略完全相反。
  tags: [framework, environmental-pathogen, dichotomy, strategy, food-safety]
  repeat_in_chunk: yes

- id: f2-02
  title: Transient vs Resident 判定与卫生升级路径
  type: framework
  source_chapter: 第3章 3.3.5.2
  source_quote: |
    "while common cleaning and sanitation practices are adequate to control the presence of
    transient contaminants, such practices do not control the presence of resident contaminants
    once they have become established... Once an environmental pathogen has become established
    as a 'resident strain,' there is a persistent contamination risk... The facility will need to use
    intensified sanitation procedures to eliminate the contamination."
  summary: |
    环境污染分两个阶段：瞬时污染（常规清洁可控）与定殖污染（病原藏进 niche，持续数月至数年）。
    常规 SSOP 对定殖菌无效——必须升级为强化卫生程序才能根除。
    由此推出两个思考动作：(1) 卫生控制的首要目标是"阻断瞬时→定殖的转化"，而不是只做日常清洁；
    (2) 一旦检出定殖（同一菌株反复出现），问题定性从"清洁执行不到位"升级为"需要根除项目"。
    判断依据是污染的时间持续性，而不是检出量。
  tags: [framework, mental-model, sanitation, resident-strain, escalation]
  repeat_in_chunk: yes

- id: f2-03
  title: 化学危害按引入机制分流控制
  type: framework
  source_chapter: 第3章 3.4.1.3（3.4 全节）
  source_quote: |
    "When your hazard analysis identifies a heavy metal that requires a preventive control, the type
    of control would depend on how the heavy metal could get into your food product... an unsafe
    level of a heavy metal such as lead could be introduced into a food product as a result of a
    food-contact surface constructed with lead solder. CGMP controls... generally can control
    chemical hazards such as heavy metals that can leach from food-contact surfaces."
  summary: |
    同一种化学危害（如铅），来源不同则控制手段完全不同：
    来自土壤/环境→供应链控制（要求种植区评估）；来自设备浸出→CGMP（117.40 设备器具控制）；
    来自配方过量→工艺控制/配方管理；来自田间→供应商验证。
    思考结构是"先问危害从哪条路径进来，再对路径开药"，而不是对危害名称查表套控制。
    该分流逻辑在 3.4 全节对农药、兽药、霉菌毒素、环境污染物反复使用。
  tags: [framework, decision-framework, chemical-hazard, root-cause-routing]
  repeat_in_chunk: yes

- id: f2-04
  title: 化学残留的"容忍度判定"逻辑（action level / tolerance 推理）
  type: framework
  source_chapter: 第3章 3.4
  source_quote: |
    "Chemical residues in a food are not always considered hazards and their occurrence may be
    unavoidable. Because the particular chemical and its levels in the food determine whether it is
    a hazard... Action levels and tolerances are established based on the unavoidability of the
    poisonous or deleterious substances and do not represent permissible levels of contamination
    where it is avoidable."
  summary: |
    判断化学残留是否构成危害的推理路径：①查该化学物是否已有 tolerance/action level；
    ②有→超过限值才是危害；无→检出即可成为危害（达最低可检出水平即可执法）；
    ③关键区分：限值建立在"不可避免"之上，可避免的污染不存在"许可水平"。
    即残留≠危害，"化学物性质+含量+可避免性"三要素共同决定。
  tags: [framework, decision-framework, chemical-hazard, threshold, regulatory]
  repeat_in_chunk: no

- id: f2-05
  title: EMA（经济动机掺假）历史模式推断法
  type: framework
  source_chapter: 第3章 3.4.1.6
  source_quote: |
    "We recommend that you focus on circumstances where there has been a pattern of such
    adulteration in the past, suggesting a potential for intentional adulteration even though the past
    occurrences may not be associated with the specific supplier or the specific food product...
    consider both the country of origin of an ingredient that may contain the hazard and any
    specific supplier associated with an ingredient containing that hazard."
  summary: |
    评估掺假可能性的思考方法：不要求"这个供应商/这个产品出过事"才预警，
    只要该原料类别存在历史掺假模式（如三聚氰胺→乳品、铅铬酸盐→姜黄），即推断潜在风险。
    评估时用两个变量定位风险：原产国（是否有掺假史）+ 具体供应商。
    这是一种基于历史模式的归纳推理：把"行业级前科"当作"个体级嫌疑"的先验。
    若判定为需控制，路线是纳入供应链程序。
  tags: [framework, mental-model, EMA, food-fraud, inductive-reasoning]
  repeat_in_chunk: no

- id: f2-06
  title: 预防控制六类分类框架
  type: framework
  source_chapter: 第4章 4.2
  source_quote: |
    "The PCHF requirements also specify that preventive controls must include, as appropriate to
    the facility and the food: (1) Process controls; (2) Food allergen controls; (3) Sanitation
    controls; (4) Supply-chain controls; (5) Recall plan; and (6) Other controls."
  summary: |
    把所有食品安全控制措施归入六类：工艺控制、过敏原控制、卫生控制、供应链控制、召回计划、其他控制。
    分类价值在于：每类绑定不同的管理组件义务——如工艺控制需要 validation，
    而过敏原控制、卫生控制、召回计划、供应链计划不需要 validation（117.160(c) 明确豁免）。
    思考时先定"这是哪一类控制"，再查该类的配套义务清单，避免遗漏或过度。
  tags: [framework, taxonomy, preventive-controls, compliance]
  repeat_in_chunk: no

- id: f2-07
  title: 热处理两分法（商业无菌 vs 致病菌削减）
  type: framework
  source_chapter: 第4章 4.3.1.1
  source_quote: |
    "Heat treatments generally fall into into the following two categories: - Heat treatment that
    leads to commercial sterility: heat processing at high temperatures (> 212 [o] F (100°C)) under
    presssure with the objective of killing all forms of microorganisms, including the spores of
    bacteria... - Heat treatment that reduces microbial pathogens but does not lead to commercial
    sterility... designed to kill the vegetative forms of microorganisms with little to no effect on
    the spores of bacteria."
  summary: |
    设计热处理前先回答"我的目标是哪一档"：>100°C 加压→商业灭菌（杀孢子，产品常温稳定）；
    70–100°C 温和热处理→只杀营养细胞（不灭孢子，产品需冷藏等后续屏障）。
    分档决定下游义务：温和档必须为幸存孢子设计额外控制（冷藏/酸化/a_w），
    且温和档若涉及低酸罐装食品则整体改受 LACF 法规（part 113）管辖，脱离 PCHF 体系。
    思考结构：目标决定强度，强度决定孢子处置责任，责任决定适用法规。
  tags: [framework, decision-framework, heat-treatment, spores, regulatory-boundary]
  repeat_in_chunk: no

- id: f2-08
  title: D 值 / z 值 / log reduction 热力杀菌学框架
  type: framework
  source_chapter: 第4章 4.3.1.1
  source_quote: |
    "D Value (the decimal reduction time) is the time required to kill 90% of the microorganisms...
    z Value refers to the degrees in Farhenheit required for the thermal destruction curve to cross
    one log cycle (i.e., for reducing the D value by a factor of 10)... These processes are designed
    to ensure product safety by achieving a 6-log reduction (6D)."
  summary: |
    用指数衰减语言量化杀菌：D 值=杀灭 90% 群体所需时间；z 值=D 值降 10 倍所需的温度变化量；
    6D=百万倍减少，是温和热处理的设计基准（如 L. mono 70°C/2min，非蛋白分解 C. botulinum 90°C/10min）。
    思考方法：把"杀菌"从模糊形容词翻译成"目标菌 × 目标 D 倍数 × 温度-时间组合"的三元组，
    任何工艺改动都可以换算成 D 值当量做比较。辐照体系用同构的 D10 值复用该框架。
  tags: [framework, quantitative, D-value, z-value, thermal-processing]
  repeat_in_chunk: yes

- id: f2-09
  title: 不可归零的概率思维（杀菌的技术上限）
  type: framework
  source_chapter: 第4章 4.3.1.1
  source_quote: |
    "it is not possible to technically achieve a level of reduction to zero, or 'no microorganisms';
    instead, as a technical matter the probability of finding the organism becomes less likely as
    the magnitude of reduction increases."
  summary: |
    杀菌永远做不到"零"，只能让检出概率随削减倍数指数下降。
    思考上要完成从"消除问题"到"把概率压到可接受水平"的转换：安全是用 6D、99.9999% 这样的
    概率语言定义的，而不是绝对保证。这个模型决定了对"无菌""零风险"表述的警惕，
    也解释了为什么体系依赖多重屏障而非单点完美。
  tags: [framework, mental-model, probabilistic-thinking, limits, food-safety]
  repeat_in_chunk: no

- id: f2-10
  title: 以最耐药目标菌设计工艺（target pathogen 选择法）
  type: framework
  source_chapter: 第4章 4.3.1.1
  source_quote: |
    "You should design a cooking process to target heat resistant vegetative pathogens, such as
    L. monocytogenes. Typically, we recommend a thermal process that achieves a 5D to 7D
    reduction for most cooking treatments. However, if the expected initial microbial load is low,
    a less severe thermal process may be adequate. For cooking processes that target pathogenic
    sporeformers such as C. botulinum type E... generally a 6D reduction in the level of
    contamination is suitable."
  summary: |
    设计致死工艺的第一步不是定温度，而是选"靶菌"：工艺强度按目标人群中最耐药的那一档设定
    （营养细胞→L. monocytogenes；非蛋白分解孢子→C. botulinum type E/B/F）。
    靶菌选定后强度档位跟随：常规烹饪 5D–7D，孢子靶 6D，初始负载低时可放宽。
    思考结构："选最难的对手→定削减倍数→反解时间温度"，附录 3-D/3-E 表即此框架的查表实现。
  tags: [framework, decision-framework, target-pathogen, process-design]
  repeat_in_chunk: no

- id: f2-11
  title: 借用参数必须按食品基质调整（文献移植降级规则）
  type: framework
  source_chapter: 第4章 4.3
  source_quote: |
    "You should use care when applying information from any of these sources to processing
    parameters for a specific product and process... the temperature (and time at that temperature)
    necessary to kill microorganisms in a food product can depend on the fat level in that food
    product."
  summary: |
    从文献、法规、行业协会拿到的工艺参数是"别人基质上的结论"，不能直接照抄。
    食品成分改变微生物耐热性：水分↓耐热↑、脂肪↑耐热↑、蛋白质保护、pH 偏离最适生长点更敏感等（Table 4-6）。
    思考规则：移植外部参数=获得起点假设，必须针对自家产品的水活度/pH/盐/脂肪/蛋白做调整，
    必要时自行做研究。这是"外部证据→本地化验证"的通用推理链条。
  tags: [framework, reasoning-method, validation, matrix-effect, evidence-transfer]
  repeat_in_chunk: no

- id: f2-12
  title: EPIPT 监控三前提
  type: framework
  source_chapter: 第4章 4.3.1.1（Ch6 6.8 详述）
  source_quote: |
    "If you want to monitor EPIPT, you should: - Conduct a temperature distribution study within
    the heating system to identify any cold spots; - Conduct a heat penetration study that accounts
    for the slowest heating product under the worst case heating conditions covered by the
    scientific study; and - Identify other critical factors of processing and/or packaging that affect
    the rate of product heating when scientifically establishing a heat process."
  summary: |
    想用"终点内部产品温度（EPIPT）"替代全程时间-温度监控，必须先满足三个前提：
    ①热分布研究（找到设备冷点）；②热穿透研究（覆盖最慢加热产品、最坏条件）；
    ③识别其他影响升温速率的关键因素并设限。
    EPIPT 只在研究覆盖的条件下可用，这些条件本身成为被监控的工艺参数。
    思考模型：用"前期一次性科学研究"换取"日常只测一个点"的简化——简化监控的合法性来自研究的完备性。
  tags: [framework, decision-framework, EPIPT, monitoring-simplification, validation]
  repeat_in_chunk: yes

- id: f2-13
  title: 传导型食品不可抽样验证原理（大颗粒食品的过程确立要求）
  type: framework
  source_chapter: 第4章 4.3.1.1
  source_quote: |
    "Heating food with large particles... occurs primarily by conduction, rather than by convection...
    You cannot control cooking processes for products with large particles by periodically checking
    the internal temperature of some of the product particles as they leave the cooker because you
    cannot verify that each particle reached the appropriate temperature for adequate time.
    Therefore, you should establish the process scientifically and validate it through a scientific
    study..."
  summary: |
    按传热方式给食品分两类：对流型（搅拌液体）可以抽查中心温度推断整体；
    传导型（含大颗粒的炖菜、汤）抽查无法证明"每一颗都达标"，只能靠科学确立的工艺+验证研究来保证。
    思考规则：能否监控取决于传热的物理确定性——确定性不足时，监控义务前移为"验证关键因素"（颗粒大小、IT、装料深度等）。
    这是"物理机制决定监控方式"的推理结构。
  tags: [framework, reasoning-method, heat-transfer, monitoring-design]
  repeat_in_chunk: no

- id: f2-14
  title: 危险温区与迟滞期思维（4 小时规则及其科学化）
  type: framework
  source_chapter: 第4章 4.3.2.1
  source_quote: |
    "Bacterial pathogens go through a lag phase, where little or no growth occurs... The object is to
    prevent that from happening, ideally keeping pathogens in their lag phase. We call the
    temperature range of concern (41°F (5°C) to 135°F (57°C)) the 'danger zone.' Traditionally, the
    rule of thumb... has been no more than 4 hours in the danger zone... the actual maximum time
    that a product may be safely held in the danger zone depends on a number of factors..."
  summary: |
    时间-温度控制的本质是"别让病原菌走出迟滞期"：一旦进入对数生长期就难以挽回。
    41–135°F 为危险温区；经验规则"危险温区内不超过 4 小时"只是起点，
    真实限值取决于菌种、食品支持生长的能力等因素，可基于自己的产品研究另设限值。
    思考结构：把抽象的"及时冷藏"翻译成"温区 + 迟滞期预算 + 剩余时间"的可操作模型。
  tags: [framework, mental-model, time-temperature, danger-zone, lag-phase]
  repeat_in_chunk: no

- id: f2-15
  title: 两段式冷却协议
  type: framework
  source_chapter: 第4章 4.3.2.1
  source_quote: |
    "The U.S. Food Code specifies the application of a two part cooling protocol In order to cool
    foods safely and keep bacteria in the lag phase. First, drop the temperature from 135°F (57°C)
    to 70°F (21°C) within two hours... Second, after dropping the initial temperature to 70°F
    (21°C), you can take up to additional 4 hours to get the product down to 41°F (5°C)."
  summary: |
    烹后冷却不是"尽快变凉"一句话，而是两段限时曲线：
    第一段 57→21°C 必须在 2 小时内完成（此区间病原菌增殖最快）；
    第二段 21→5°C 可再给 4 小时。FSIS 对肉禽给出等价的另一组温度节点。
    思考方法：把冷却时间预算按"微生物风险密度"不均匀分配——最危险区间给最紧的约束。
    若热处理足以灭孢子且冷却中防再污染，冷却步骤才可不作关键控制。
  tags: [framework, decision-framework, cooling, time-temperature, protocol]
  repeat_in_chunk: no

- id: f2-16
  title: a_w 三分类控制框架（0.85/0.60 双分界）
  type: framework
  source_chapter: 第4章 4.3.3.1
  source_quote: |
    "Moist foods (i.e., foods with water activity above 0.85) require refrigeration or another barrier
    to control the growth of pathogens... Intermediate-moisture foods (i.e., foods with water
    activities between 0.60 and 0.85) do not require refrigeration to control pathogens, but they
    may have a limited shelf life because of spoilage... Low-moisture foods (i.e., foods with a
    water activity below 0.60) have an extended shelf life, even without refrigeration."
  summary: |
    按水分活度给食品三分类并绑定控制义务：>0.85 高湿（需冷藏或其他屏障）；
    0.60–0.85 中湿（病原无需冷藏控制，但货架期受酵母霉菌限制）；<0.60 低湿（无需冷藏，货架期长）。
    0.85 分界线的依据是 S. aureus 生长的最低 a_w；孢子出芽的对应线是 0.92。
    思考方法：测出/查出一个食品的 a_w，即读出它的病原控制义务档位；
    天然低 a_w 食品无需控制，"由高降低的"才需要工艺控制。
  tags: [framework, decision-framework, water-activity, classification, formulation]
  repeat_in_chunk: yes

- id: f2-17
  title: pH 4.6 分界线（酸/低酸食品与法规管辖判定）
  type: framework
  source_chapter: 第4章 4.3.3.2
  source_quote: |
    "when the pH of a food is 4.6 or below, spores of C. botulinum will not germinate and grow. As
    a result, the pH of 4.6 is a dividing line for the purpose of determining whether a food other
    than an acid food is subject to part 113 as an LACF or part 114 as an acidified food."
  summary: |
    pH 4.6 是 C. botulinum 孢子不能发芽生长的科学分界，被直接借用作法规分界：
    天然 ≤4.6 为酸食品（不受 LACF/酸化食品法规管）；>4.6 为低酸食品；
    低酸+加酸+a_w>0.85+终平衡 pH≤4.6 = 酸化食品（part 114）。
    酸化的两个实操要点：终平衡 pH 可能需数天达到（大颗粒食品须冷藏过渡）；
    必须同时控制腐败菌——腐败产碱会把 pH 拉回去，让肉毒风险复活。
    思考结构：一个科学阈值同时承担"抑菌依据+管辖权判据"双重角色。
  tags: [framework, decision-framework, pH, botulism, regulatory-boundary]
  repeat_in_chunk: no

- id: f2-18
  title: 配方控制的两条合规路径（跟随 vs 自建+验证）
  type: framework
  source_chapter: 第4章 4.3.3.1
  source_quote: |
    "There are two basic ways for how you can approach product formulation that uses control of
    water activity for food safety. One approach is to closely follow a scientifically established
    process for formulation that ensures a water activity of 0.85 or below. The other approach is to
    develop your own process for formulation and to validate it by taking finished product samples
    and testing them for water activity."
  summary: |
    用配方控制危害时有两条可选路径：①严格照搬已有科学确立的配方工艺（免自证）；
    ②自建工艺，但须用成品取样测 a_w 验证有效性。
    思考模型：合规负担可以交换——照抄权威工艺=省验证但失灵活性；自研=灵活但验证义务自负。
    该"借用 vs 自证"的二元选择同样适用于其他工艺控制的设计决策。
  tags: [framework, decision-framework, formulation, validation, tradeoff]
  repeat_in_chunk: no

- id: f2-19
  title: 清洁策略三选一（湿清洁/干清洁/受控湿清洁）
  type: framework
  source_chapter: 第4章 4.4.1
  source_quote: |
    "Wet Cleaning: Uses water-based and/or wet chemical cleaning solutions... you should use
    water on an as-needed basis... Dry Cleaning: Does not use any water... sweeping, brushing,
    scraping, or vacuuming... Controlled Wet Cleaning: Uses a limited amount of water, generally
    for dry operations. Complete drying should follow immediately after the controlled wet
    cleaning."
  summary: |
    清洁策略按环境性质三选一：湿区用湿清洁（但要限量用水、避免高压水枪气溶胶）；
    干区用干清洁（扫/刷/刮/吸尘，防止把粉尘扩散到别处）；
    干区确需湿清洁时用"受控湿清洁"——限量水+立即彻底干燥，或把设备搬出湿清洁后归还。
    决策锚点是 f2-01 的湿/干二分法：干区任何水都是沙门氏菌风险源，所以干燥紧随其后是硬约束。
  tags: [framework, decision-framework, cleaning, sanitation, wet-dry]
  repeat_in_chunk: no

- id: f2-20
  title: 卫生分区（hygienic zoning）设计框架
  type: framework
  source_chapter: 第4章 4.4.2
  source_quote: |
    "The objective of hygienic zoning is to reduce the potential for transient pathogens to enter
    sensitive areas in the facility, such as packing areas where an RTE product is exposed to the
    processing environment... You should determine the need for, and scope of, a hygienic zoning
    program based on your facility, the products you make, and the outcome of your hazard
    analysis."
  summary: |
    用分区把"脏"与"敏感"隔开：生vs在制品vs成品、湿vs干、人流与物流走向、气压平衡。
    目标是阻止瞬时病原进入 RTE 暴露区这类敏感区域；分区的必要性和范围不照抄别人，
    由自己的设施结构、产品和危害分析结论决定（面粉厂/RTE 冷食厂/酸化罐头厂的需求完全不同）。
    思考方法：先识别"最敏感区"，再反向设计隔离梯度（f2-02 的"阻断瞬时→敏感区"应用）。
  tags: [framework, design-framework, hygienic-zoning, RTE, sanitation]
  repeat_in_chunk: no

- id: f2-21
  title: 同一活动按危害分析分流为 CGMP 或卫生控制
  type: framework
  source_chapter: 第4章 4.4
  source_quote: |
    "You determine which hazards require a sanitation control, rather than CGMPs, through your
    hazard analysis. Thus, some – but not all - of your sanitation procedures, practices, and
    processes will be 'sanitation controls'; other sanitation procedures, practices, and processes
    will be CGMPs... your CGMP procedures, practices, and processes are sometimes called
    'prerequisite programs.'"
  summary: |
    同一个清洁动作可能有两个身份：由危害分析选中去控特定危害的=卫生控制（预防控制，
    带监控/纠正/验证义务）；其余=CGMP/前提程序（不带管理组件义务）。
    思考规则：身份不是按活动类型定的，而是按"它是否被危害分析指派去控一个需控危害"定的。
    前提程序是卫生控制的底座——设备可清洁性、设施设计不到位，控制无法有效执行。
    这决定了义务的"按需分配"而非"一刀切"。
  tags: [framework, decision-framework, CGMP, sanitation-control, prerequisite-programs]
  repeat_in_chunk: no

- id: f2-22
  title: 预防控制×危害类型适用性矩阵（控制手段的能力边界表）
  type: framework
  source_chapter: 第5章 5.2（Table 5-1）
  source_quote: |
    "Table 5-1 provides examples of the application of preventive controls to significantly minimize
    or prevent the occurrence of ingredient-related and process-related biological hazards... but is
    not intended to imply that a particular preventive control has been validated for control of
    specific pathogens in specific foods. You are responsible for validating specific preventive
    controls as appropriate..."
  summary: |
    把每种控制手段对四类生物危害（孢子/营养细胞/毒素/寄生虫）的适用性逐格标注：
    如热处理杀营养细胞但不灭孢子、不消除已形成的 S. aureus/B. cereus 毒素；
    a_w≤0.92 抑制孢子出芽、≤0.85 抑制营养细胞生长；
    冷冻能杀多细胞寄生虫却只是让细菌休眠。使用规则：矩阵是"能力方向"提示，
    不等于已验证——对具体食品/病原的验证责任仍在工厂。
    思考方法：选控制手段前先查该手段对靶危害的适用格，能力边界外的危害需另配屏障。
  tags: [framework, matrix, applicability, control-selection, limits]
  repeat_in_chunk: no

- id: f2-23
  title: 监控四问（What / How / How often / Who）
  type: framework
  source_chapter: 第5章 5.5.2
  source_quote: |
    "To fully describe your monitoring program, the procedures should answer four questions: (1)
    What will be monitored? (2) How will monitoring be done? (3) How often will monitoring be done
    (frequency)? and (4) Who will do the monitoring?"
  summary: |
    任何监控程序用四问补全：监控什么（必须与危害控制直接相关：参数或活动符合性）；
    怎么监控（仪器/目视/记录装置）；多久一次（能捕捉正常波动并发现偏离的频次；
    连续监控也须至少每日人工复核记录）；谁来监控（须具备培训/经验，书面指定岗位）。
    思考方法：四问是监控程序的完备性检验清单——任一问答不出，监控程序即不完整。
  tags: [framework, checklist-framework, monitoring, completeness-test]
  repeat_in_chunk: no

- id: f2-24
  title: 回溯暴露窗口假设（偏离即假定自上次合格点起失控）
  type: framework
  source_chapter: 第5章 5.5.2 / 5.5.4
  source_quote: |
    "If a measurement shows that a deviation from the control value has occurred, you should
    assume that the control value had not been met since the last check in which the value was
    acceptable. As a result, the greater the time span between measurements, the more products
    you are putting at risk... food safety plans with infrequent calibration or accuracy checks can
    place more products at risk than those with more frequent checks."
  summary: |
    发现偏离时的默认推理：不确定失控起点，就假定从"上一次合格记录"起全部未受控——
    受影响产品的范围=两次合格检查之间的全部产量。
    由此推出监控/校准频次的风险定价：间隔越长，一次偏离的暴露窗口越大，受牵连产品越多。
    思考模型：把监控频次理解为"暴露窗口宽度的旋钮"，频次决策变成风险-成本权衡而非形式要求。
  tags: [framework, mental-model, risk-window, monitoring-frequency, calibration]
  repeat_in_chunk: no

- id: f2-25
  title: Correction vs Corrective Action 判定边界
  type: framework
  source_chapter: 第5章 5.5.3
  source_quote: |
    "Corrections may be appropriate instead of corrective actions when minor, isolated problems
    occur that do not directly impact product safety... If you observe food residue on 'clean'
    equipment prior to production, corrections would involve re-cleaning and sanitizing the
    equipment before it is used... no food is affected and no actions are needed with respect to
    food."
  summary: |
    两个动作的分流用两个判据：①问题是否已影响到食品；②问题是孤立还是反复。
    生产前发现"干净"设备上有残渣→及时重清洁即可（correction，甚至可不记录）；
    已包装产品温度记录未达关键限→触发完整纠正措施四步程序（corrective action）。
    反复出现的"correction 级问题"会升格：说明程序无效，需重新分析。
    思考结构：先问"产品是否受影响"，再问"是否孤立"，两问定级别。
  tags: [framework, decision-framework, correction, corrective-action, escalation]
  repeat_in_chunk: yes

- id: f2-26
  title: 预定纠正措施程序的三优势（平时写、急时用）
  type: framework
  source_chapter: 第5章 5.5.3
  source_quote: |
    "A predetermined corrective action procedure has the following advantages: (1) It provides
    detailed instructions for an employee to follow in the event of a deviation in applying a
    preventive control; (2) it can be prepared at a time when an emergency situation is not calling
    for an immediate decision; and (3) it removes the obligation to reassess the food safety plan in
    response to a deviation."
  summary: |
    把纠正方案写成预案的理由有三：给员工现成的执行指令；在无压力时从容决策；
    偏离发生时免去当场重评 FSP 的义务。
    思考模型：决策质量与压力负相关——把"什么算合格、不合格怎么办"的判断前移到冷静时刻，
    危机时刻只需执行。未预见的意外问题则触发"临时纠正+事后重分析"的补充路径。
  tags: [framework, mental-model, pre-commitment, decision-under-pressure]
  repeat_in_chunk: no

- id: f2-27
  title: 纠正措施四要素（完整的 corrective action 程序骨架）
  type: framework
  source_chapter: 第5章 5.5.3
  source_quote: |
    "An appropriate corrective action procedure must accomplish the following goals: (1) Ensure
    that the appropriate action is taken to identify and correct the problem...; (2) ensure that the
    appropriate action is taken when necessary to reduce the likelihood that the problem will recur;
    (3) ensure that all affected food is evaluated for safety; and (4) ensure that all affected food is
    prevented from entering into commerce unless an evaluation has determined that the product is
    not adulterated..."
  summary: |
    纠正措施的完整骨架是四步：①找到并修复问题；②降低复发概率（查历史记录识别反复模式，
    频发时触发再分析）；③评估全部受影响食品的安全性（可能需要专门技术支持）；
    ④未经评估证明未掺假的受影响食品不得入市（放行决定须书面说明证据）。
    记录同样按四要素展开。思考方法：四步的顺序是"修机器→防再犯→算旧账→守住门"，
    第④步是不可跳过的默认封锁。
  tags: [framework, process-framework, corrective-action, four-step, documentation]
  repeat_in_chunk: no

- id: f2-28
  title: 例外记录（exception records）——只记异常
  type: framework
  source_chapter: 第5章 5.5.2
  source_quote: |
    "Although, as noted above, continuous monitoring (with associated records) is desirable, in some
    circumstances the monitoring records may be 'exception records' that document loss of control.
    See 21 CFR 117.145(c)(2)."
  summary: |
    记录义务允许反转：不是"每次检查都记"，而是"只在失控时才建记录"（exception record）。
    前提是监控本身（连续仪器或按频次执行）仍在运行——省掉的是正常情况下的记录笔墨，
    不是监控动作。
    思考模型：把记录负担与异常率挂钩，大幅降低文档成本；
    适用边界由控制手段的性质和管理组件的角色决定。
  tags: [framework, records, exception-record, efficiency]
  repeat_in_chunk: no

- id: f2-29
  title: 热处理设计与验证三步法
  type: framework
  source_chapter: 第6章 6.6
  source_quote: |
    "To control bacterial pathogens using a heat treatment adequate to ensure that the pathogens
    do not survive the process, you should: Scientifically establish a heat treatment that will
    significantly minimize the target bacterial pathogens...; Design and operate the heat treatment
    equipment so that every unit of product receives at least the established minimum heat
    treatment; and Monitor the established process parameters to verify achievement of the
    scientifically established heat treatment (e.g., time and temperature)."
  summary: |
    建立热控制的通用三步：①科学确立工艺（研究或 process authority 给出靶菌削减所需的参数与关键限值）；
    ②设计/运行设备，保证每一单位产品至少获得该最低处理（冷点覆盖、最坏条件覆盖）；
    ③监控既定参数，验证实际达成。
    三步各自独立缺一不可：科学依据→均匀投送→执行证明。
    思考模型：任何工艺控制都可套用"确立-投送-证明"三段式。
  tags: [framework, process-framework, heat-treatment, three-step, validation]
  repeat_in_chunk: yes

- id: f2-30
  title: 关键限值 vs 操作限 vs 调整（三级限值体系）
  type: framework
  source_chapter: 第6章 6.5
  source_quote: |
    "we use the term 'operating limit' to mean criteria that may be more stringent than critical limits
    and are established for reasons other than food safety... we use the term 'adjustment' when
    referring to an intervention that you take if you determine that there is a deviation from an
    operating limit, without a deviation from a critical limit."
  summary: |
    参数限值分两级：关键限值=食品安全红线（突破即偏离，触发纠正措施）；
    操作限=更严格的内控线（基于质量等非安全原因设立，如烘焙 13 分钟关键限 vs 15 分钟操作限）。
    突破操作限但未破关键限→只做"调整"（调设备参数），不触发纠正措施、不算食品安全偏离。
    思考模型：给红线加一层缓冲带，让小波动在碰线前被吸收，避免用食品安全程序处理质量问题。
  tags: [framework, decision-framework, critical-limit, operating-limit, adjustment]
  repeat_in_chunk: no

- id: f2-31
  title: 多重屏障与"先腐败后危害"思维（面包案例）
  type: framework
  source_chapter: 第4章 4.3.3.1（Table 4-12 说明）
  source_quote: |
    "Actually, the 'crumb' (interior) has a relatively high water activity. It is safe because of the
    multiple barriers of pH, water activity (the crust has a low water activity), and preferential
    growth by mold rather than pathogens. In other words, the bread spoils before it becomes
    hazardous."
  summary: |
    单看一个指标会误判安全性（面包瓤 a_w 高达 0.95）；
    面包安全是因为 pH、a_w（低 a_w 外壳）、霉菌优先竞争生长三重屏障叠加。
    设计上追求"腐败先于危害"：感官警讯（发霉）在病原风险到来之前出现，消费者天然被保护。
    思考模型：评估含有多参数的食品时做"屏障叠加"分析，并检查是否具备"先腐败"的预警属性；
    反例是无屏障的 ROP 产品（可能先产毒后腐败，无感官警讯）。
  tags: [framework, mental-model, hurdle-technology, multiple-barriers, spoilage-first]
  repeat_in_chunk: no

- id: f2-32
  title: HPP 技术适用性推理（短板匹配法）
  type: framework
  source_chapter: 第4章 4.3.1.2
  source_quote: |
    "Bacterial spores are well established as the most pressure-resistant biological forms known.
    Spores resist inactivation by high pressure alone and most require the addition of heat or some
    other mechanism to achieve appropriate levels of destruction... Because of this, the best
    candidates for HPP continue to be acid foods and foods that will be refrigerated following
    processing (which provide control of sporeformers)."
  summary: |
    选择杀菌技术时的思考方法：先找该技术杀不了的对手（HPP 对孢子几乎无效），
    再判断这个短板能否被产品的其他属性补上（酸性食品 pH 抑制孢子、冷藏食品孢子难生长）。
    能补上→技术适用；补不上（如低酸常温食品）→该技术不可独立使用。
    这是"技术能力边界 × 产品既有屏障"的匹配推理，与 f2-22 的适用性矩阵同源。
  tags: [framework, decision-framework, HPP, technology-fit, gap-matching]
  repeat_in_chunk: no
