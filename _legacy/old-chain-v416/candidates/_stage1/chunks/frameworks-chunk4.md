# 阶段 1 框架候选 — 第 4 块（第 9901–13200 行：Ch11 尾部 + 附录 11-1~3 + Ch12 前半）

> 提取人：framework-extractor 分块扫描员（chunk 4/6）。不做筛选，宁错杀；"是否反复出现"仅就本段判断。

```yaml
- id: f4-01
  title: 过敏原排产时间分隔决策（无过敏原→少→多、同谱系聚类）
  type: framework
  source_chapter: 第11章 11.12.2.1 / 附录 11-1.F.2
  source_quote: |
    "Implement production scheduling to separate by time the manufacture of products with
    different food allergen profiles. For example, you could produce the foods in a sequence
    whereby the food with no allergen or the fewest allergens is produced first and the food
    with the most allergens is produced last. As another example, you could cluster runs of
    products containing the same food allergen profile to reduce the number of changeovers."
  summary: |
    当多条产品共用一条产线且过敏原谱系不同时，用生产排程本身作为控制手段。
    排序规则：不含过敏原的产品最先做、过敏原最少其次、过敏原最多的最后做，
    使"后续产品包含前序产品的全部过敏原"成为不变式，从而把清洁需求压到最小。
    辅助规则：把相同过敏原谱系的产品批次聚在一起跑，减少换产（changeover）次数。
    这是一个典型的"用顺序设计替代硬件投入"的决策框架：先排产、再看残余风险决定是否需要强化清洁。
    Dessert A 完整示例：raspberry sorbet→vanilla ice cream→vanilla custard→vanilla custard with almonds。
  tags: [scheduling, allergen-control, decision-framework, production-planning]

- id: f4-02
  title: 过敏原配料最下游添加原则
  type: framework
  source_chapter: 第11章 附录 11-1.F.2（Dessert A 11.12.2.1 应用）
  source_quote: |
    "Add allergenic ingredients as late in the production process as possible, and as far
    downstream as possible in the processing line (e.g., closest to the filling and packaging
    equipment), to minimize the amount of equipment in the production area that comes in
    contact with the allergen."
  summary: |
    工艺设计层面的通用思考结构：让高危/致敏物料尽可能晚地进入流程、尽可能靠近灌装端。
    逻辑是"接触该物料的设备数量越少，需要清洁、验证和防交叉接触的面积越小"。
    Dessert A 把杏仁放到灌装步骤才加入，就是该原则的实例化。
    可迁移到任何"危险输入应最小化暴露面"的流程设计问题：
    把不可控/高后果的要素推迟到链条末端注入，从而把隔离成本压缩到一个点。
  tags: [process-design, allergen-control, minimization, mental-model]

- id: f4-03
  title: 排产序列驱动的清洁强度判定（通用清洁 vs 过敏原专项清洁）
  type: framework
  source_chapter: 第11章 11.12.3.1
  source_quote: |
    "The production sequence, coupled with general cleaning measures established in accordance
    with the CGMP requirements of 21 CFR 117.35, is adequate to prevent allergen cross-contact
    after the processing of each of the first three products in the production sequence ...
    General cleaning measures ... alone are not adequate to prevent allergen cross-contact
    after the processing of the final product ... because the production sequence begins again
    with raspberry sorbet, which contains no allergenic ingredients."
  summary: |
    判定"CGMP 通用清洁是否够用"的思维路径：沿排产序列逐段检查。
    若下一产品包含上一产品的全部过敏原，通用清洁即可；若序列末尾（过敏原最多的产品）
    之后又回到无过敏原产品，则必须升级为靶向去除所有过敏原残留的专项清洁（预防控制）。
    附加条件分支：一旦正常排产顺序被打乱，只要前序产品含有后续产品没有的任一过敏原，
    就触发专项清洁。本质是"前序危害集合 ⊆ 后序危害集合？"的集合包含判断，
    把清洁决策从经验直觉变成可推导的规则。
  tags: [cleaning-validation, allergen-control, decision-framework, if-then]

- id: f4-04
  title: 标签内容控制 vs 标签管理控制的生命周期二分
  type: framework
  source_chapter: 第11章 11.11 / 11.12.4 / 11.13.4
  source_quote: |
    "Label controls have a role in ensuring that the finished food will not be misbranded under
    section 403(w) of the FD&C Act. Putting a label control in place to prevent such
    misbranding is more important than classifying that control in a particular way (e.g., as
    a label content control or a label management control)."
  summary: |
    把标签防错按生命周期切成两段：标签内容控制管"标签上写什么"——
    开发阶段（配方→过敏原识别→标签规范→mock-up 确认）与订购阶段；
    标签管理控制管"对的标签用在对的产品上"——储存、备料（staging）、生产、生产后回收。
    两个示例厂展示了同一框架的两种实现：预印包装厂（Dessert A，色码带+条码扫描）
    与生产中电子打印标签厂（Bakery B，电子文件核对+在线打印核对）。
    关键态度：分类本身（content vs management）不改变监管后果，先有控制、分类可灵活——
    单一活动/记录甚至可同时服务于两类控制。
  tags: [label-control, lifecycle, classification, allergen-control]

- id: f4-05
  title: "执行不力 vs 程序无效"双路径根因调查
  type: framework
  source_chapter: 第11章 11.12.3.3（同一结构亦见于 11.12.4.3、11.13.4.3、附录 11-1.A）
  source_quote: |
    "The Production Manager conducts a root cause investigation to try to determine whether:
    Allergen cleaning procedures were not properly implemented (e.g., a complete clean was not
    conducted during an out-of-sequence changeover to raspberry sorbet to fulfill an order);
    or The allergen cleaning procedures are not effective (e.g., if it is determined that there
    is a place where a particle can get hung up on the equipment ...)"
  summary: |
    出问题后先问"程序设计错了，还是人没照做"——把一切失败拆成两个正交根因。
    若是执行不力：再培训人员，程序不动；若是程序无效：修订程序本身（如设备有颗粒滞留点，
    需拆解清洁）。两条路径对应的补救动作完全不同，混判会修错地方。
    本段内该结构在 Dessert A 清洁控制、标签内容/标签管理纠正、Bakery B 标签纠正、
    附录 11-1.A（CGMP 失败也建议 correction/corrective action）中至少出现 4 次，是本段反复出现的元框架。
    可迁移：任何 SOP 失效排查都应先做"设计缺陷 vs 执行缺陷"的分流。
  tags: [root-cause, corrective-action, dichotomy, mental-model]

- id: f4-06
  title: 色码可视化防错体系
  type: framework
  source_chapter: 第11章 11.12.2.1 / 11.12.4.1.1 / 11.13.3.1（附录 11-1.F.1 亦推荐）
  source_quote: |
    "Bakery B dedicates all utensils (e.g., scoops, spatulas) and tools (e.g., scrapers,
    brushes) used in the production of the peanut butter cookies so that they are not used for
    the production of oatmeal cookies or caramel chip cookies. Bakery B color-codes all
    utensils and tools (peanut - blue; non-peanut - white) to make it visibly obvious if the
    incorrect utensil or tool is brought into the production area."
  summary: |
    用颜色作为"身份编码"让错误状态肉眼可见：原料容器色码贴签（奶=白、蛋=黄、杏仁=棕）、
    量具/容器与所盛过敏原同色、工服/发网按区域配色（花生线=蓝、非花生线=白）、
    成品桶/盖边缘色带与产品一一对应。设计逻辑是"专用 + 可区分"：
    专用品类一旦被误拿，颜色错配会立即暴露，无需依赖人的记忆或记录追溯。
    本段内 Dessert A 与 Bakery B 各自实现一遍，附录 11-1 又将色码列为通用 CGMP 建议——
    本段内反复出现。可迁移为任何"用物理可见标识降低人为混淆概率"的防错设计。
  tags: [color-coding, error-proofing, visual-management, allergen-control]

- id: f4-07
  title: 严重性驱动的分隔策略选择（物理分隔 vs 时间分隔+人员管控）
  type: framework
  source_chapter: 第11章 11.13.2.1 / 11.13.3.1（对照 Dessert A 11.12）
  source_quote: |
    "However, due to the severity of allergic reactions in consumers who are allergic to
    peanuts, Bakery B's PCQI determined that allergen cross-contact controls on utensils,
    tools, apparel, and movement of personnel are necessary to ensure protection of the
    oatmeal cookies and caramel chip cookies from allergen cross-contact with peanut protein."
  summary: |
    两个示例厂给出同一问题的两条解法及其选择依据：
    Dessert A 过敏原均为常规严重度→用排产时间分隔+换产清洁即可；
    Bakery B 面对花生（严重过敏反应）→升格为空间物理分隔：独立产线/设备/工具、
    称量与备料区用墙+门隔开、专用色码器具与工服、人员按班次固定在某一条线。
    决策变量是"危害后果的严重性"：后果越重，越要从"时间隔离"升级到"空间隔离+人员隔离"。
    附录 11-1.C 则给出空间分隔的完整设计菜单（专用车间、封闭设备、阀门、气流控制、缓冲间）。
    这是一个"按风险等级选择隔离强度"的可迁移框架。
  tags: [segregation, risk-tiering, allergen-control, decision-framework]

- id: f4-08
  title: 与供应商控制方式匹配的验证强度
  type: framework
  source_chapter: 第11章 11.13.5.2 / 11.13.5.3
  source_quote: |
    "Requires Supplier A to provide a Certificate of Conformance that the caramel chips are
    produced on a dedicated processing line each year and a third-party audit every three
    years; Requires Supplier B to provide a third-party audit each year; and Samples and tests
    caramel chips from Supplier B quarterly."
  summary: |
    Bakery B 评估两家素焦糖片供应商：A 用专线生产（低风险），B 与含奶产品共线、
    靠排产+推扫清洁+FCS 奶检测（中等风险）。批准后对两者要求不同的持续验证组合：
    供应商控制越"结构性"（专线物理隔离），买方验证越轻（年度 COA+三年一审）；
    供应商越依赖"操作性"措施（共线清洁验证），买方验证越重（年审+每季抽样检测）。
    核心思路：验证强度应与供应商风险控制方式的可靠性成反比，
    而不是对所有供应商一刀切。可迁移到任何外包/采购的风险分级管理。
  tags: [supplier-verification, risk-based, supply-chain, decision-framework]

- id: f4-09
  title: 信任递减抽测（每批验证→建立信任后降频）
  type: framework
  source_chapter: 第12章 12.10.2（脚注 33）
  source_quote: |
    "Analytical testing to verify supplier control of toxic elements and to confirm the
    results in the supplier's COA are conducted on every lot until Manufacturer A develops
    confidence in the supplier's program; at that point, verification testing is reduced to
    quarterly."
  summary: |
    对新供应商或新危害先做"全批检测"积累信任数据，一旦确信其程序受控，
    即降为定期抽测（季度）。这是验证资源的自适应分配策略：
    初期高成本低信任，随证据积累逐步降低干预频率，但仍保留周期性抽查以发现漂移。
    与 f4-08 互补：f4-08 讲"按供应商控制方式定强度"，本条讲"按时间维度动态调频"。
    可迁移到任何"新关系从严、老关系抽查"的质量管理场景。
  tags: [supplier-verification, adaptive-sampling, trust-calibration, verification]

- id: f4-10
  title: 化学危害 CGMP vs 预防控制四因素判定
  type: framework
  source_chapter: 第12章 12.3.4
  source_quote: |
    "Your hazard analysis should consider which known or reasonably foreseeable ('potential')
    hazards can be effectively managed through the application of CGMPs and other prerequisite
    programs, and which hazards require one or more preventive controls. Factors that you
    should consider during your hazard analysis include: ... the probability that a known or
    reasonably foreseeable ('potential') hazard will occur in the absence of preventive
    controls ... the severity of the illness or injury if the hazard were to occur."
  summary: |
    每个潜在化学危害都要过一道分流闸门：归 CGMP/前提程序管理，还是升格为预防控制。
    判定因素四类：①危害本身的信息；②食品与工艺信息（关联病史、原料来源、配方/工艺/设备、
    易感人群的合理预期用途）；③无预防控制时的发生概率（本厂历史失误、检测数据、
    其他法规与自愿计划的覆盖）；④一旦发生的疾病/伤害严重性。
    12.3.5–12.3.13 的九类危害评估全部以这组因素为公共底座，再叠加类别专属考虑——
    本段内反复出现的判定框架。PCQI 的判断（是否受益于管理组件）也是正式因素之一。
  tags: [hazard-analysis, decision-framework, cgm-vs-pc, chemical-hazards]

- id: f4-11
  title: 九类化学危害分路由评估法（共性因素+类别专属考虑）
  type: framework
  source_chapter: 第12章 12.3.5–12.3.13
  source_quote: |
    "In evaluating whether a pesticide hazard in a food ingredient could be a hazard requiring
    a preventive control, we recommend that you consider: the factors we identified in section
    12.3.4; and whether the food has a history of violative pesticide residues."
  summary: |
    面对九类化学危害（环境污染物、真菌毒素、植物毒素、农药残留、兽药残留、
    未批准食品/色素添加剂、生物胺、经济利益掺假物、过程污染物+设施相关化学品），
    统一句式是"先过 12.3.4 四因素，再加该类别专属的一个问题"：
    环境污染物→能否地理性规避采购；真菌毒素→USDA 市场令/谷物分级与官方检测体系；
    农药→违规残留历史（进口警报）；兽药→是否超耐受/禁用超标签用药；
    添加剂→法规身份核查清单；生物胺→分解史；经济掺假→该品类过往掺假模式；
    过程污染物（3-MCPDE/GE、3-MCPD、4-MEI、丙烯酰胺）→是否流入婴幼儿食品等易感用途；
    设施化学品→FDA 未见需要预防控制的情形（CGMP 足够）。
    这是一个"公共判定器 + 每类一个杀手问题"的路由框架。
  tags: [chemical-hazards, routing, evaluation-path, decision-framework]

- id: f4-12
  title: 婴幼儿食品毒元素"供应链控制优先"逻辑
  type: framework
  source_chapter: 第12章 12.3.5 / 12.10.1 / 12.11.1
  source_quote: |
    "A priority for FDA is reducing dietary exposure to contaminants to as low as possible ...
    FDA has prioritized foods commonly eaten by babies and young children because their
    smaller body sizes and metabolism make them more vulnerable to the harmful effects of
    these contaminants. If you manufacture foods intended for babies and young children, we
    recommend that you identify applicable toxic elements that are known or reasonably
    foreseeable ('potential') hazards in ingredients of such foods as hazards requiring a
    supply-chain program as a preventive control."
  summary: |
    环境污染物（砷镉铅）的一般策略是"规避"——远离已知污染区采购即可，
    无需升格为预防控制；但一旦消费对象是婴幼儿，判定被强制翻转为
    "把毒元素识别为需要预防控制的危害，且用供应链控制（接收前管控）实现"。
    同时保留双轨：已定为预防控制的元素走供应链程序；未定级的元素仍以 QC 操作管理——
    首批到货前审查检测数据+采购协议要求供应商年度周期检测+成品季度测试喂给再分析。
    本质是"易感人群触发判定升级"的思考结构：同一危害，消费人群不同，控制等级不同。
  tags: [toxic-elements, vulnerable-population, supply-chain-control, baby-food]

- id: f4-13
  title: Closer to Zero 半年监管查新机制
  type: framework
  source_chapter: 第12章 12.10.2 / 12.11.2（两示例厂均设此机制）
  source_quote: |
    "Manufacturer A's PCQI reviews FDA's 'Closer to Zero' website for updates to applicable
    FDA recommendations on a semi-annual basis and whenever Manufacturer A's PCQI receives a
    communication from FDA regarding such updates."
  summary: |
    把"外部监管环境会漂移"制度化为两个触发器：固定节奏（每半年）
    主动扫描监管来源（FDA 行动水平、Planned Action Items），加上事件触发（收到 FDA 来函）立即查新。
    查新结果喂入再分析：监管行动可能改变企业为污染物设定的规格，进而影响
    "哪些危害归 CGMP、哪些需要预防控制"的既有判定（12.3.4 末尾明确要求再分析时考虑）。
    这是"外部信息保鲜"的可迁移框架：对任何依赖外部标准/阈值的决策体系，
    设固定扫描周期+事件驱动双通道，把变化接到再评估流程上。
  tags: [regulatory-watch, reanalysis, horizon-scanning, Closer-to-Zero]

- id: f4-14
  title: 受影响食品的分级处置阶梯（转用途→转动物饲料→销毁）
  type: framework
  source_chapter: 第12章 12.6.5（Bakery B 11.13.3.3 同构）
  source_quote: |
    "evaluate the product for safety; based on the evaluation, determine disposition of the
    product, e.g.: divert the product to a different use ... to a product (such as a fully or
    partially cooked adult entrée) that is unlikely to be consumed by babies and young
    children); divert the product to animal food ...; destroy the product."
  summary: |
    产品超标不等于立即销毁：先做安全评估，再沿"降级处置阶梯"逐级选择——
    转作不涉易感人群的普通食品（铅超婴幼儿规格的根茎菜→成人餐食）、
    转作动物食品（需符合对应物种限量）、最后才是销毁。
    Bakery B 同构：误接触花生蛋白的面团可重加工为花生酱饼干（跨谱系降级），
    或转作动物饲料。核心是"按暴露人群的脆弱性重新匹配产品与用途"，
    在安全边界内最大化保留价值。可迁移为任何不合格品的分级处置思路。
  tags: [product-disposition, diversion, risk-matching, corrective-action]

- id: f4-15
  title: 监控/验证分类的实质主义原则（叫什么不重要，管用才重要）
  type: framework
  source_chapter: 第12章 12.6.4.3（第11章 11.11 同款表述）
  source_quote: |
    "it generally makes little difference whether you consider some activities (such as visual
    observation) to be monitoring or verification for the purposes of your process control as
    long as you comply with requirements applicable to monitoring or verification. Regardless
    of what you call them, your preventive control management component(s) must be appropriate
    to ensure the effectiveness of the preventive controls (see 21 CFR 117.140(a))."
  summary: |
    部分活动（目视观察、批次过程检测）天然落在监控与验证的分类边界上。
    指南给出的元规则：分类标签是自由变量，实质约束是"活动组合必须足以保证控制有效"。
    落到操作层：一旦你给某个活动定了性（监控或验证），就要在全部示例中保持一致并满足
    对应要求； Bakery B 甚至用一张打印标签同时充当内容控制与管理控制的验证记录。
    可迁移的思考结构：当制度对标签的分类不敏感时，把精力从"归哪类"转到"覆盖够不够"。
    本段内在第 11、12 两章各出现一次，属跨章结构（本段内两见）。
  tags: [monitoring-vs-verification, classification-flexibility, pragmatism, meta-rule]

- id: f4-16
  title: 供应商批准前五维审核
  type: framework
  source_chapter: 第12章 12.10.2 / 12.11.2（Bakery B 11.13.5.3 同构）
  source_quote: |
    "Approves suppliers by: reviewing a supplier's procedures, processes, and practices
    related to the presence of lead in the raw materials ...; reviewing information relevant
    to a supplier's compliance with applicable FDA food safety regulations, including an FDA
    warning letter or import alert ...; reviewing 'food fraud' resources ...; obtaining
    historical data from the supplier ...; and obtaining several lots ... and testing them for
    lead prior to final approval of the supplier."
  summary: |
    正式批准供应商前的五个信息面：①供应商自己的程序/过程/实践（含土壤水检测、低富集品种）；
    ②合规记录（FDA 警告信、进口警报等执法历史）；③食品欺诈资源库（防经济掺假）；
    ④供应商的历史检测数据（产品/土壤/水）；⑤买方亲自取多批样品检测通过后才批准。
    Bakery B 版本：问卷（过敏原程序+咨询声明依据）、FDA Supplier Evaluation Resources 检索、
    第三方审核、多批送检。共性：批准基于多源证据交叉，绝不依赖供应商单方声明。
    可迁移为"新供应商准入尽调"的通用清单框架。
  tags: [supplier-approval, due-diligence, multi-source-evidence, supply-chain]

- id: f4-17
  title: 供应商不符合的双路径处置（疑虑隔离 vs 确证升级）
  type: framework
  source_chapter: 第11章 11.13.5.4（第12章 12.10.2/12.11.2 同构）
  source_quote: |
    "If the results of an onsite audit raise questions about whether a supplier is controlling
    for unintended milk presence in the caramel chips, but it seems unlikely that allergen
    cross-contact has occurred, Bakery B temporarily stops using the caramel chips from that
    supplier until the supplier addresses the questions raised by the audit. If it appears
    that the supplier is not able to address the questions in a timely fashion, Bakery B takes
    steps to approve a new supplier, relying in the meantime on the remaining supplier."
  summary: |
    供应商出问题后的分流：①疑虑但尚未证实交叉接触→correction 路径：暂停用货、
    等供应商答复；答复不及时→启动备选供应商切换；②已证实交叉接触或检测阳性→
    corrective action 路径：暂停用货+评估已产成品（检测未用原料批次）+评估召回。
    Manufacturer A 版本补充判定维度："物料是否已投入生产"决定 correction 还是
    corrective action，并随整改表现决定是否加大抽测或终止合作。
    框架核心：按"证据确定性×物料已用与否"两个维度分流处置力度，
    同时永远保留双供应商冗余作为退出通道。
  tags: [supplier-nonconformance, escalation, corrective-action, supply-chain]

- id: f4-18
  title: 经济掺假特征触发的升级处置
  type: framework
  source_chapter: 第12章 12.10.2（肉桂铅超标专项）
  source_quote: |
    "Takes specific corrective action(s) if levels of lead in an incoming shipment of ground
    cinnamon exceed specifications at a level that suggests the possible addition of lead
    (e.g., as lead chromate) to ground cinnamon for purposes of economic gain. Examples
    include: Stopping production ...; Segregating any product already made with this shipment
    ...; Notifying the supplier; Immediately discontinuing use of the supplier; and Performing
    or repeating analytical tests for lead on available inventory ..."
  summary: |
    普通"超标"走常规纠正；但超标幅度/形态指向人为掺假（铅盐增重增色）时，
    处置逻辑整体切换为"欺诈应对"：立即停产相关产品、隔离已产产品评估、
    通知供应商、立即终止合作（不给整改机会）、并回头把已有库存全部复检。
    判定线索来自历史上的掺假模式库（12.3.11：肉桂/姜黄铅盐、三聚氰胺、苏丹红Ⅰ；
    2023 肉桂苹果酱事件即实例）。思维结构：同一检测异常，
    按"自然超标 vs 掺假签名"分诊为两类完全不同性质的事件。
    可迁移：把"异常是否符合已知欺诈模式"作为独立的分诊维度。
  tags: [economically-motivated-adulteration, triage, escalation, food-fraud]

- id: f4-19
  title: 逐原料排除法评估供应商交叉接触
  type: framework
  source_chapter: 第11章 11.12.2.3 / 11.13.2.3
  source_quote: |
    "Through its supply-chain programs for the control of biological hazards in cream, milk
    powder, and pasteurized liquid eggs, Dessert Manufacturer A has determined that the
    suppliers of cream, milk powder, and pasteurized liquid eggs do not process other food
    allergens. Therefore, Dessert Manufacturer A's PCQI determined that Manufacturer A does
    not need to assess the potential for allergen cross-contact at the suppliers for the
    cream, milk powder, and pasteurized liquid eggs."
  summary: |
    判断"是否需要为某原料的供应商建立过敏原供应链控制"的推理路径：
    对每种原料单独问"该供应商是否还处理其他过敏原"——
    是（如 Bakery B 的素焦糖片，供应商同厂产含奶片）→需要供应链控制；
    否（奶油/奶粉/蛋液/面粉/花生酱等）→明确记录"无需评估"，排除出控制范围。
    情报来源可复用既有供应链程序（为生物危害做的供应商调查顺带回答了过敏原问题）。
    特殊分支：供应商使用咨询声明→要求其提供使用依据（脚注 42）。
    排除结论本身要留书面记录——"No" 的论证与 "Yes" 同等重要。
  tags: [supply-chain-assessment, elimination-reasoning, allergen-control, per-ingredient]

- id: f4-20
  title: CGMP 基线 + 预防控制增强的双层防御
  type: framework
  source_chapter: 第11章 附录 11-1.A（第12章 12.3.4 同构）
  source_quote: |
    "your hazard analysis should consider how your CGMP measures prevent allergen
    cross-contact, and the preventive controls that you establish and implement to address a
    food allergen hazard should complement and enhance your CGMP measures for preventing
    allergen cross-contact."
  summary: |
    体系设计的分层思考：CGMP 措施（人员、厂房设计、卫生操作、器具、原料、制造、仓储运输
    八大类，见附录 11-1.B–G）是必须先就位的基线层；预防控制不是另起炉灶，
    而是在基线上"查漏+加强"——找出 CGMP 覆盖不住的残余风险，
    对那些点位加装管理组件（监控/纠正/验证/记录）升格为预防控制。
    两个示例厂都按此顺序展开：先盘 CGMP 措施，再决定需要哪些过敏原控制。
    即使 CGMP 层失败也建议做 correction/corrective action。
    可迁移为"前提程序打底、关键点加控"的通用安全体系架构思路。
  tags: [layered-defense, cgm-baseline, preventive-control, system-architecture]

- id: f4-21
  title: 全员通识 + 岗位定制的两层培训矩阵
  type: framework
  source_chapter: 第11章 11.10（Table 11-5）
  source_quote: |
    "we recommend that all individuals (including individuals with responsibility for
    management, research and development, marketing, procurement, legal/regulatory issues,
    auditing, product development, design engineering, production, quality assurance, consumer
    complaints, and warehousing and distribution) receive general allergen awareness training."
  summary: |
    培训设计框架：第一层全员通识（过敏原意义、标签控制、防交叉接触通用实践、
    发现疑似意外过敏原时的行动），覆盖从研发、市场、采购到仓储的全链条岗位——
    因为过敏原控制成败取决于"所有阶段的所有人"；第二层按岗位职能定制
    （Table 11-5）：采购→供应链控制意识、收货→标识储存程序、生产→本岗位预防措施与纠正、
    WIP/返工管理、维修→工具带菌风险、清洁、主管→本厂过敏原程序。
    底层依据 117.4(b)：每个人须具备与其指派职责相称的资质，培训记录必须保存。
    可迁移为任何"共同底线 + 角色深化"的能力建设矩阵。
  tags: [training-matrix, role-based, two-layer, allergen-control]

- id: f4-22
  title: 配方→成分→过敏原食品来源溯源展开
  type: framework
  source_chapter: 第11章 11.12.4.1.1 / 11.13.4.1.1
  source_quote: |
    "The Label Team develops a food allergen label specification by reviewing the ingredients
    listed in the recipe or formulation, and the components listed by suppliers for all
    ingredients, to identify all food allergens in each product and the food source of each
    allergenic ingredient or component."
  summary: |
    标签内容控制的起点推理：从配方逐层向下展开——每个成分是什么、
    每个成分的供应商又声明其组分含什么——直到穷尽每个产品携带的全部过敏原及其食品来源。
    再处理两个特殊判定：①食品来源是否已含在常用名里（"milk powder" 已含 milk，
    无需重复声明；"flour" 不含 wheat，需要 Contains 声明补充）；
    ②豁免判断（高度精炼大豆油不属过敏原标示范围）。
    输出固化为书面的"过敏原标签规范"并有专人签批。
    这是从"配方树"推导"声明集合"的系统性方法，本段内 Dessert A 与 Bakery B 各演一遍。
  tags: [label-specification, traceability, recipe-decomposition, allergen-control]

- id: f4-23
  title: 以"生产是否已开始"为界的 correction / corrective action 分界
  type: framework
  source_chapter: 第11章 11.13.3.3（附录 11-2/11-3 汇总表中重复呈现）
  source_quote: |
    "Corrections: If production has not begun, these activities are corrections and the
    Production Supervisor does not document the correction on the Checklist for Allergen
    Cross-Contact Controls. ... Corrective actions: If production has begun, these activities
    are corrective actions and are documented on the Checklist ... determines whether product
    may have been affected (i.e. whether product may have come in contact with peanut
    protein), and, if so, evaluates any affected cookies for safety and prevents affected food
    from entering commerce ..."
  summary: |
    同一个异常（错误颜色的工具/工服出现在错误区域），处置路径由时间分界决定：
    生产开始前发现→correction，纠正即可且不必记录；生产中/后发现→corrective action，
    必须记录，且追加完整链条：判定产品是否可能受影响→安全评估→阻止入市
    （重加工为其他谱系产品或转动物饲料）→必要时召回。
    与全书 correction vs corrective action 的两个判定维度一致：
    "问题是否已影响食品"（时间分界是其可操作代理）+"孤立还是反复"。
    Bakery B 在器具、工服、电子标签文件三处都用同一条时间分界，本段内反复出现。
  tags: [correction-vs-corrective-action, boundary-condition, documentation, allergen-control]
```

## 自检

- [x] 23 条候选，每条均有原文摘录依据（引用自 9901–13200 行原文）
- [x] 引用均为 ≤100 英文单词的原文节选
- [x] 覆盖指定主题：排产决策（f4-01/02/03）、标签生命周期（f4-04）、双路径纠正（f4-05/23）、色码与分隔（f4-06/07）、供应商批准与验证（f4-08/09/16/17/18/19）、附录 11-1 CGMP 清单（f4-20）、化学危害四因素与九类路由（f4-10/11）、婴幼儿毒元素与 Closer to Zero（f4-12/13）
- [x] "是否反复出现"的判断仅基于本段文本
