# Stage 1 框架候选 — 分块 3/6（source.md 第 6601–9900 行）

> 覆盖范围：Ch6 后半（6.9–6.17 热处理偏差处置、验证、记录 + 5 个示例厂 Cookie A/B、Soup A/B、Salsa A + Appendix 6-A~6-E）+ Ch7/8/9/10 占位页 + Ch11 前半（11.1–11.9 过敏原程序、交叉接触控制、标签控制、供应链程序、咨询声明）。
> 说明：本分块"是否反复出现"仅在本分块内判断（在 summary 中标注 [本段重现]）。

```yaml
- id: f3-01
  title: 热处理偏差处置决策链（偏差后产品去向的递进选项谱系）
  type: framework
  source_chapter: Ch6 §6.9（行 6625–6644）
  source_quote: |
    "Examples of steps identified in corrective action procedures applicable to a heat treatment
    include: Continue heating a product that has not reached the specified temperature...;
    Reprocess the product (deliver the full process as if no heating had already occurred);
    Chill and hold the product for an evaluation of the adequacy of the heat treatment...;
    Divert the product to a use in which the critical limits for the parameter are not
    applicable...; Divert the product to animal food...; and Destroy the product."
  summary: |
    当工艺控制（热处理）偏离关键限值时，不要二选一"放行/销毁"，而是沿一条由轻到重的处置阶梯评估：
    补足处理（继续加热/延长时间/降速）→ 全程再加工 → 降温暂存待评估 → 改作非 RTE 用途或转原料
    → 转动物饲料 → 销毁。选择依据是"能否用科学依据证明危害已被消除/该参数对该用途不再适用"。
    这是一个可迁移的"偏差后资产处置阶梯"思维：先救回、再降级、最后销毁，每一级都要有评估主体（PCQI）。
    [本段重现] Cookie A/B、Soup A/B、Salsa A 五个示例的纠正措施程序全部套用此阶梯，仅选项组合不同。
  tags: [decision-framework, deviation-disposition, heat-treatment, corrective-action]

- id: f3-02
  title: 验证活动五分类（validation 与四类 ongoing verification 的分层）
  type: framework
  source_chapter: Ch6 §6.10（行 6658–6681）
  source_quote: |
    "Part 117 requires that verification activities include, as appropriate to the nature of the
    preventive control and its role in your food safety system: (1) Validation; (2) Verification
    that monitoring is being conducted; (3) Verification that appropriate decisions about
    corrective actions are being made; (4) Verification of implementation and effectiveness;
    and (5) reanalysis."
  summary: |
    把"验证"这个笼统概念拆成五个功能不同的层级：(1) validation=用科学证据确认控制措施本身有效
    （一次性/变更时）；(2) 核查监控确实在被执行；(3) 核查纠偏决策本身是否正确；(4) 核查控制被
    一致实施且有效（校准/产品检测/环境监测/记录审查）；(5) 再分析。前三层是"对体系的验证"，
    第四层是"对运行的验证"，第五层是"对验证的更新"。
    可迁移模式：任何控制体系都需要区分"证明方法有效"与"证明执行有效"两类证据，不能互相替代。
  tags: [verification, validation, mental-model, process-control]

- id: f3-03
  title: 两步验证法（外部文献定致死性 × 厂内研究证可达性）
  type: framework
  source_chapter: Ch6 §6.12.2 / §6.13.2（行 6814–6839、6986–7034）
  source_quote: |
    "The extension specialist provided Cookie Processor A's PCQI with a published study by Lathrop
    et al., (2014)... To determine critical limits for those processing parameters... and
    demonstrate that these critical limits can be achieved in Cookie Processor A's convection
    oven, the extension specialist conducted in-house heat distribution tests on Cookie
    Processor A's ovens and heat penetration tests on the cookies using a fully loaded oven."
  summary: |
    确定关键限值的推理路径分两步：第一步用已发表的同行评审研究（文献数据：菌种/基质/温度/时间/
    log 下降）确定"科学上需要什么"；第二步在本厂设备上做热分布+热穿透研究，证明"我的设备实际
    能达到什么"。两者的交集才是本厂的关键限值。任何一环缺失（只有文献没有厂内验证，或反之）
    都不能称为 validation。
    可迁移模式：引用外部基准后必须做本地可行性验证；"科学要求"与"设备可达"要分别取证再取交集。
    [本段重现] Cookie A（大学 extension 专家）、Cookie B（咨询公司专家）、Soup B、Salsa A 均走同一路径。
  tags: [validation, evidence-reasoning, heat-treatment, critical-limits]

- id: f3-04
  title: 关键限值/操作限双线设计（用质量缓冲保护安全红线）
  type: framework
  source_chapter: Ch6 §6.12.2（行 6837–6856）
  source_quote: |
    "the extension specialist determined that the baking process of 350°F or greater for a minimum
    of 13 minutes (operating limit of 15 minutes) would provide adequate lethality for Salmonella
    ... The operating limit for the baking temperature is 352°F (178°C); The operating limit for
    the baking time is 15 minutes; and The operating limit for cookie dough portion size is 27 g."
  summary: |
    为每个关键参数同时设两条线：关键限值（食品安全红线，偏离触发纠正措施+产品处置）和操作限
    （更严格、基于质量/稳定运行考虑的内控线，偏离只需 adjustment，不触发产品处置）。日常按操作限
    生产，使工艺波动在碰到红线之前就被日常调整吸收。
    可迁移模式：给任何"不可逾越的红线"配一条更严的预警线，把偏差消灭在缓冲区，避免频繁触发
    高成本的正经纠偏程序。
  tags: [critical-limits, operating-limits, decision-framework, buffer-design]

- id: f3-05
  title: 批式/连续工艺的监控参数映射
  type: framework
  source_chapter: Ch6 §6.13 / §6.15（行 6994–7000、7381–7390）
  source_quote: |
    "Band oven temperature ([o]F) to achieve specified minimum product temperature; Baking time
    in oven (minutes) controlled by the speed of the conveyor belt through the continuous band
    oven; ... Metering pump speed (RPM) to deliver process-specified flow rate (gal/min); Hold
    tube size (must deliver a minimum 2.5 minute product hold time prior to hot-filling)."
  summary: |
    同一个食品安全目标（足够的时间×温度）在不同工艺形态下分解为完全不同的可监控参数：
    批式→每批的起止时间记录；连续带式炉→传送带转速（RPM）换算停留时间；连续流热交换器→
    计量泵流速+保压管几何尺寸。方法论是"把不可直接监控的量（致死时间）转译成线上可直接
    观察的代理参数（转速/流速/管径）"。
    可迁移模式：当目标量不可实时测量时，找到与它有确定函数关系的可测代理量并把代理量设为关键限值。
  tags: [monitoring, parameterization, continuous-process, batch-process]

- id: f3-06
  title: EPIPT 替代逻辑（用终点温度替代全程时间-温度监控）
  type: framework
  source_chapter: Ch6 §6.14.2（行 7196–7202）
  source_quote: |
    "Soup Processor A's PCQI determined that 0.05 minutes (3 seconds) at 180°F achieves an
    acceptable 6-log... reduction... Because of the additional lethality during the heating time
    needed for the soup to reach 180°F (82°C), and because more than 3 seconds would elapse
    before cooling from 180°F could begin, Soup Processor A's PCQI decided to use an EPIPT and
    cook the soups until the temperature reaches 180°F rather than to continuously monitor
    temperature during cooking."
  summary: |
    当致死处理的"安全裕量主要来自升温和降温阶段的额外杀灭"时，可以只监控终点内部产品温度
    （EPIPT），无需全程记录时间-温度曲线。前提是：量化升降温阶段的免费致死量（来自查表或研究）、
    确认它们足以覆盖所需 log 下降、并确认没有其他关键因素（如颗粒尺寸）被忽略。
    可迁移模式：当要求的指标远小于过程自然提供的裕量时，用"终点状态"替代"全程轨迹"作为监控对象，
    大幅降低监控与记录负担——但替代论证必须书面成立。
  tags: [EPIPT, monitoring-simplification, heat-treatment, margin-reasoning]

- id: f3-07
  title: 颗粒尺寸临界参数判定逻辑（传热约束转译为尺寸上限）
  type: framework
  source_chapter: Ch6 §6.14.2 / §6.16.2（行 7204–7217、7613–7622）
  source_quote: |
    "Food scientists at Soup Processor A conducted in-house studies to determine the critical
    limit for vegetable particle size. Based on those studies... as long as vegetable particles
    in the soup did not exceed ½ inch (13 mm) square, the particles would also be at 180°F when
    the liquid portion of the soup reached that temperature, provided that the particles were
    stored refrigerated... Soup Processor A determined that a critical limit for the temperature
    of the particles in the soup is not necessary as long as the production line follows the SOP
    to store the particles refrigerated."
  summary: |
    固体颗粒内部的温度不可实时测量，于是用厂内研究确定一个尺寸上限：只要颗粒不超过该尺寸且
    储存条件（冷藏不冷冻）满足，颗粒中心就会与液相同步达到目标温度。由此把"测颗粒温度"这个
    不可行任务转译为"测颗粒尺寸+守冷藏 SOP"两个可行任务；且当尺寸关键限值以冷藏为前提时，
    温度本身可不必再设关键限值。
    可迁移模式：对不可直接测量的对象，用实验确定"几何/状态前提"，使前提成立时代理测量等价于
    直接测量；前提本身用 SOP 固化而非另设关键限值。
    [本段重现] Soup A（½ inch/13 mm）与 Salsa A（1.0 cm）用同一逻辑，尺寸值因基质和温度而不同。
  tags: [critical-parameters, heat-transfer, proxy-measurement, particle-size]

- id: f3-08
  title: 目标菌选择逻辑（按最耐热+产品储存/包装情境选靶）
  type: framework
  source_chapter: Ch6 §6.15.1–6.15.2（行 7326–7357）
  source_quote: |
    "Because hot-filling into 5-gallon bags would result in reduced oxygen packaging, and because
    the soups will be distributed refrigerated, Soup Processor B's PCQI/food processing expert
    determined that C. botulinum non-proteolytic type B is an appropriate target organism for the
    soup heat treatment. ... a heat treatment that targeted C. botulinum non-proteolytic type B
    as the most heat resistant pathogen would also address Salmonella and L. monocytogenes."
  summary: |
    多病原并存的工艺不必对每种病原分别设计处理：先由产品情境（包装方式是否减氧、分销储存温度）
    推出"哪类病原会成为约束"（减氧+冷藏→非蛋白分解型肉毒梭菌），再选其中最耐热者作为目标菌，
    按它设计 6D 工艺，其余较不耐热的病原被自动覆盖；残余风险（如蛋白分解型肉毒）交给后置控制
    （冷藏）处理。
    可迁移模式：约束情境→最严苛对象→按最严苛者设计→剩余风险显式分配给其他控制，而非全部堆进
    一个处理。
  tags: [target-organism, worst-case-design, pathogen-selection, heat-treatment]

- id: f3-09
  title: 可再加工/不可再加工清单（偏差处置的事前预授权）
  type: framework
  source_chapter: Ch6 §6.15.4（行 7434–7438）
  source_quote: |
    "A list of: Those soups that can be fully reprocessed in instances where soup was
    underprocessed; and Those soups that cannot be fully reprocessed and therefore will be
    diverted to animal food (non-pet food) or destroyed if the PCQI determines that the process
    delivered was inadequate to ensure product safety."
  summary: |
    Soup B 在纠正措施程序里预先写好一份清单：哪些产品配方出偏差后可以全程再加工（因基质耐受
    二次热处理），哪些不能（再加工会毁掉品质，只能转饲料或销毁）。偏差发生时 PCQI 不用临场争论
    可行性，直接按清单执行，只保留"过程是否充分"的安全评估权。
    可迁移模式：对高频偏差，事先把处置选项按产品/情境穷举并书面化，把紧急决策降级为查表执行，
    保留专家判断仅用于清单未覆盖的安全问题。
  tags: [corrective-action, pre-authorization, rework, decision-list]

- id: f3-10
  title: 放行前审查替代 7 天记录审查的书面论证
  type: framework
  source_chapter: Ch6 §6.14.5（行 7284–7287）
  source_quote: |
    "Before a lot of soup is released, the PCQI reviews corrective action records as part of a
    pre-shipment review to ensure all lot records are in order. (Because Soup Processor A uses an
    EPIPT and employees have been with Soup Processor A for many years, Soup Processor A
    experiences few deviations, so the PCQI has determined and documented that this timeframe,
    rather than 7 working days, is reasonable.)"
  summary: |
    法规默认"记录创建后 7 个工作日内由 PCQI 审查"，但允许企业用书面论证改用替代时限。Soup A 的
    论证链是：EPIPT 简化了监控+员工资深→偏差极少→7 天周期形同虚设→改为每批放行前审查（更贴合
    风险）。关键在于：替代方案不是随意放宽，而是"陈述事实基础 + 说明为何同样或更充分 + PCQI
    书面记录"。
    可迁移模式：对任何"默认时限/默认频次"类合规要求，可用同等或更优的替代方案，但必须完成
    "事实—推理—书面化"三段论证。
  tags: [records-review, documented-justification, flexibility, verification]

- id: f3-11
  title: 15 批加严抽样回归逻辑（偏离后加严—连续合格—恢复常态）
  type: framework
  source_chapter: Ch6 §6.14.4 / §6.16.4（行 7256–7262、7710–7718）
  source_quote: |
    "If it is determined that the mean plus 2.5 standard deviation of the vegetable particle sizes
    exceeds ½ inch (13 mm) the lot of vegetables is rejected... The formulation control operator
    will check the vegetable particle size of every lot for the next 15 lots to verify particle
    sizes meet specification. If all 15 lots meet specification, the formulation control operator
    will return to monitoring every third lot."
  summary: |
    抽样监控频次的动态调节规则：常态下按 1/3 批抽查；一旦发现不合格（判据用 mean+2.5SD 而非单点
    超标，吸收测量变异），立即转为逐批全检并向供应商追溯根因；连续 15 批全部合格后恢复常态频次。
    这实质是一个简易的统计工艺控制状态机：正常态→报警态（加严+溯源）→验证态（连续 N 批合格）→
    回到正常态。
    可迁移模式：任何"抽检型"监控都可以配上"偏离→加严→连续 N 次通过→回归"的有限状态机，避免
    一出问题就永久加严或出了问题还照常抽检两个极端。
    [本段重现] Soup A（来料批）与 Salsa A（在制品批）均使用同一 15 批规则。
  tags: [sampling-plan, state-machine, monitoring-frequency, spc]

- id: f3-12
  title: 免除产品检测/环境监测的暴露剖面论证
  type: framework
  source_chapter: Ch6 §6.15.5 / §6.16.5（行 7496–7499、7764–7767）
  source_quote: |
    "Soup Processor B does not conduct product testing for pathogens or environmental monitoring
    because the product, which is subjected to a heat treatment validated to be highly lethal to
    vegetative pathogens and filled hot, is not exposed to the environment after the heat
    treatment."
  summary: |
    验证活动的"种类与数量"不是固定清单，而是由产品在工艺后是否暴露于环境这一事实决定：
    热处理高度致死+热灌装+之后不接触环境→无需产品检测和环境监测（环境病原控制的对象根本
    不存在）。推理链为：验证的对象是"特定危害×暴露途径"，两者任一不成立则对应验证活动失去
    意义，但论证必须写在 FSP 里而不是口头省略。
    可迁移模式：合规义务可以按"风险不存在"而豁免，但豁免本身是一条需要书面证据链的结论。
    [本段重现] Soup B 与 Salsa A（酸化+热灌装）均以同一逻辑免除。
  tags: [verification-scope, exposure-assessment, documented-justification, exemption]

- id: f3-13
  title: 最坏情况验证研究设计（冷点/几何中心/最保守参数组合）
  type: framework
  source_chapter: Ch6 §6.13.2（行 7006–7017）
  source_quote: |
    "The in-house heat penetration studies... used thermocouples with the sensors placed in the
    geometric center of the cookie dough portions (in 16 cookie dough portions deposited in 28 g
    portions at different points across the width of the oven band, in each of 3 trials conducted
    over 3 days). The speed of the conveyor belt... was set to result in a residence time of
    cookies in the oven of 13.0 minutes (as a worst case, or conservative, speed setting)."
  summary: |
    验证研究要覆盖所有"最坏情况"维度并叠加：位置上测设备冷点与产品几何中心；空间上横跨炉带
    宽度多点布探头；时间上分 3 天 3 次试验以吸收日间波动；工艺上故意用最保守（最短停留时间）
    设置。只有当"最坏组合"仍达标时，常规运行才算有保证。
    可迁移模式：任何验证/测试设计都先穷举"哪些因素会让结果变差"，然后主动把测试条件设在这些
    因素的最不利组合上，而不是在理想条件下测出漂亮数据。
  tags: [validation-design, worst-case, heat-penetration, experimental-design]

- id: f3-14
  title: 过敏原程序三支柱（CGMP 底座 + 双控制 + 供应链）
  type: framework
  source_chapter: Ch11 §11.1（行 8158–8199）
  source_quote: |
    "A food allergen program could include, as appropriate to the facility and its food products:
    CGMP measures that you take to comply with the requirements of part 117, subpart B, to
    prevent allergen cross-contact...; Food allergen controls...: Allergen cross-contact controls...
    and Label controls...; A supply-chain program as required by part 117, subpart G for those
    raw materials and other ingredients for which a manufacturing/processing facility has
    identified a food allergen hazard that is controlled before its receipt."
  summary: |
    过敏原管理不是单一程序而是三层结构：底层是 CGMP 基线措施（人员/厂房设计/卫生/设备/原料/
    操作/仓储七个方面，不强制管理组件）；中层是两类预防控制——交叉接触控制（防不该有的进）+
    标签控制（防该声明的不声明），各配监控/纠正/验证组件；顶层是供应链程序（把控制前移到接收
    之前，仅当危害需 supply-chain-applied control 时）。三支柱的分工是：CGMP 铺底、预防控制
    增强并管理、供应链覆盖厂外环节。
    可迁移模式：任何风险管理都可以分层为"基线实践（不需逐项监控）—重点控制（需管理组件）—
    外部前移（需供应商管理）"。
  tags: [allergen-program, layered-architecture, cgmp, preventive-controls]

- id: f3-15
  title: CGMP 措施升格为预防控制的适配法
  type: framework
  source_chapter: Ch11 §11.4.1（行 8471–8478）
  source_quote: |
    "The allergen cross-contact controls that you establish and implement as preventive controls
    should complement and enhance the measures you have in place to comply with the CGMP
    requirements... we recommend that you consider adapting one or more of the measures for
    complying with the CGMP requirements to function as a preventive control by combining a CGMP
    measure with one or more preventive control management components such as monitoring or
    verifying through, e.g., visual observation."
  summary: |
    同一项实践（如色标区分原料、清洁、WIP/回用工管理）可以有两重身份：作为 CGMP 履行基线义务
    （不强制监控记录），或"升格"为预防控制——方法是把该实践与至少一个管理组件（监控/验证，如
    定期目视核查并记录）捆绑。升格的判据是该措施在危害分析中被认定为针对特定危害的预防控制。
    这给了企业一个渐进化路径：先全厂铺 CGMP，再挑选风险最高的几项升格加管理组件。
    可迁移模式：同一实践可有"基线身份"与"受管身份"两种存在方式，升格的最小操作是+监控+记录。
  tags: [cgmp, upgrade-path, preventive-controls, monitoring]

- id: f3-16
  title: correction vs corrective action 判定（"使用前/使用后"边界）
  type: framework
  source_chapter: Ch11 §11.7.3（行 9326–9377；另见 §11.5.3 行 8697–8709）
  source_quote: |
    "Determining that the content of a product label/package is incorrect... before using the
    label/package in production. If you correct the label before using it such that no food is
    affected, you could consider the problem to be a minor and isolated problem... [versus]
    after using the label/package in production. Because an incorrect label... would misbrand
    the food under section 403(w)..., the incorrect label content is not a minor problem."
  summary: |
    轻微处置（correction）与完整纠正措施（corrective action 四步）的判定边界有两个维度：
    ① 问题是否已实际影响食品（标签错误在贴标前发现=correction；贴标后发现=已致错标误品牌，
    必须 corrective action+评估/下架/召回）；② 孤立还是反复（反复出现即程序无效，必须走完整
    程序并触发再分析）。同样的客观错误，因发现时机不同而走完全不同的处置路径。
    可迁移模式：偏差分级不看错误本身的严重度，而看"损害是否已发生"+"是否成模式"两个后验维度。
    [本段重现] §11.5.3（CIP 温度/标签示例）、§11.6.1.2（清洁）、§11.6.2（投料）、§11.8.5（供应商）
    反复使用同一判定。
  tags: [correction, corrective-action, decision-boundary, allergen]

- id: f3-17
  title: 实施失败 vs 设计失效二分（偶发→再培训，重复→再分析）
  type: framework
  source_chapter: Ch11 §11.6.1.2–11.6.1.3（行 8917–8933）
  source_quote: |
    "we recommend that your corrective action procedures distinguish between those corrective
    actions you would take if you determine that the problem was due to improper implementation
    of the allergen cleaning procedure and those corrective actions you would take if you
    determine that the allergen cleaning procedure is not effective. For example, if an occasional
    finding of product residue... you could limit your corrective action procedures to retraining
    the personnel... However, if repeated findings... your corrective action procedures should
    include reanalysis of your food safety plan."
  summary: |
    控制失效后先诊断失效类型：程序没问题但没被执行（implementation failure）→ 对人的再培训/
    现场纠正即可；程序被执行了但本身无效（design failure）→ 修人是无效的，必须触发 FSP 再分析、
    修订程序，甚至（在清洁案例中）得出需要咨询声明的结论。判定信号是频率：偶发=前者，重复=后者。
    可迁移模式：遇到失效先问"是人没做对，还是做对了也没用"，两类问题的 remedies 完全不同，
    用重复频率作为切换信号。
  tags: [failure-diagnosis, reanalysis, implementation-vs-design, corrective-action]

- id: f3-18
  title: 供应商咨询声明三选一决定（不传递/传递/阈值论证）
  type: framework
  source_chapter: Ch11 §11.9.3（行 9848–9864；另见 §11.8.4 行 9675–9696）
  source_quote: |
    "your PCQI should provide, in your food safety plan, a written determination of whether:
    The allergen advisory statement has no impact on the food allergen profile of your products,
    because all products that would contain the affected ingredient also include an ingredient
    that is (or contains) the food allergen...; You will carry an allergen advisory statement
    forward to one or more of your food products...; or You will rely on a scientifically valid
    determination... that the amount of food allergen... is low enough..."
  summary: |
    当供应商对原料附"may contain X"声明而你的产品配方不含 X 时，PCQI 必须书面三选一：
    (a) 不传递——我的所有用到该原料的产品本就含 X，标签已声明，声明对我的产品无影响；
    (b) 传递——把该原料当作含 X 过敏原对待，在 Label Content Procedures 中规定同等管控；
    (c) 阈值论证——用科学有效的风险评估确定可能的残留量低于致敏阈值，不声明亦安全。
    三个出口都要求书面化并进 FSP。若产品配方本就含 X，则自动落入 (a) 无需论证。
    可迁移模式：上游的不确定性声明传入下游时，必须显式做出"吸收/透传/量化豁免"三选一，禁止
    默认忽略。
    [本段重现] §11.8.4 与 §11.9.3 两处以几乎相同文字给出该三选一。
  tags: [advisory-statement, three-way-decision, supply-chain, allergen-labeling]

- id: f3-19
  title: 供应链批准/验证活动选择谱系（风险梯度 ↔ 验证强度匹配表）
  type: framework
  source_chapter: Ch11 §11.8.3.2 + Table 11-4（行 9585–9634）
  source_quote: |
    "if a supplier that processes food products with different food allergen profiles on the same
    processing line combines scheduling, allergen cleaning procedures, and frequent verification
    testing in its food safety plan, your PCQI could determine that annual testing is appropriate.
    However, if a supplier... does not do verification testing, more frequent testing (such as
    monthly or quarterly) could be appropriate."
  summary: |
    Table 11-4 用 8 个供应商情境展示一条验证强度谱系：供应商用独立产线/独立建筑（风险低）→
    问卷+资源库检索+现场审核，后续仅年度符合性声明、审核可拉长到 3 年一审；共线但组合排产/
    清洁/验证测试（风险中）→ 年度现场审核+周期性抽测；共线且清洁无法保证、供应商改用咨询
    声明（风险高）→ 多批检测频率/水平以支撑是否传递声明的决定。核心规则：检测永远只能作为
    其他验证活动的补充，不能是唯一手段（分布不均使抽样天然有漏检风险）。
    可迁移模式：供应商验证的严谨度是因变量，自变量是"供应商端的交叉暴露潜力 + 供应商自身
    程序的强度"，用矩阵而非一刀切。
  tags: [supply-chain, verification-spectrum, risk-gradation, supplier-approval]

- id: f3-20
  title: 供应商交叉接触风险分级逻辑（空间分离→时空分离→共线的梯度）
  type: framework
  source_chapter: Ch11 §11.8.2 + Table 11-4（行 9482–9502、9612–9627）
  source_quote: |
    "Low, because the supplier stores and processes almonds and peanuts in separate buildings.
    ... [另一情境] Low, because the supplier has CGMP measures for separation in both space and
    time, has allergen cross-contact controls for ingredients, apparel, portable equipment,
    utensils, and tools, and during development of the food safety plan verification testing...
    is consistently negative. Therefore, the supplier does not use allergen advisory statements."
  summary: |
    评估供应商端交叉接触潜力时按分离维度的完备性分级：不同建筑（空间完全分离）= 低；
    同一建筑不同房间+专用品具+色标+人流/物流限制（空间分离+管理措施）= 低到中；
    同房间但叠加时间分离（错峰排产）+验证测试历史阴性 = 低到中；同一产线仅靠清洁+排产 = 中；
    清洁验证历史阳性、改用咨询声明 = 高。级别决定你方批准活动与后续验证频率。
    可迁移模式：把"隔离程度"拆成空间/时间/管理/验证证据四个可独立打分的维度再合成风险级别，
    而不是凭供应商有无咨询标签单点判断。
  tags: [risk-grading, supplier-assessment, allergen-cross-contact, separation]

- id: f3-21
  title: 监控/验证分类的灵活性原则（叫什么不重要，充分性才重要）
  type: framework
  source_chapter: Ch11 §11.5.2.3（行 8664–8679）
  source_quote: |
    "In many cases, the nature of an activity (such as visual observation) conducted as a
    preventive control management component for an allergen cross-contact control or a label
    control could be classified as either monitoring or as verification... it generally makes
    little difference whether you consider such an activity to be monitoring or verification...
    Regardless of what you call them, you must have procedures that are adequate to ensure the
    effectiveness of the preventive controls."
  summary: |
    目视观察这类活动既可以归为监控也可以归为验证，法规不要求同一活动重复做两遍以同时满足
    两个名义类别。判定标准不是分类学而是充分性：活动的性质与数量必须足以确保控制有效，且
    结果必须经记录审查验证。这把企业从"给活动贴正确标签"的焦虑中解放出来，转向"活动的
    风险覆盖是否够"的实质判断。
    可迁移模式：当两个合规类别对同一活动都适用时，按实质充分性设计一次到位的活动组合，
    不要为分类学而重复劳动。
  tags: [monitoring, verification, classification-flexibility, adequacy]

- id: f3-22
  title: 供应链程序必要性判定（无过敏原/单过敏原供应商豁免）
  type: framework
  source_chapter: Ch11 §11.8.2（行 9491–9502）
  source_quote: |
    "we see no reason for you to establish and implement a supply-chain program for the control
    of food allergen hazards if: You will receive a raw material or other ingredient from a
    supplier that does not manufacture, process, or pack any food allergens; or You will receive
    a raw material or other ingredient that is (or contains) a food allergen from a supplier,
    and that food allergen is the only food allergen that the supplier manufactures/processes."
  summary: |
    并非所有含过敏原的原料都触发供应链程序：若供应商根本不加工任何过敏原，或其厂内只加工
    这一种过敏原（如只处理杏仁的杏仁商），则厂内不存在"不同过敏原剖面之间的交叉接触"问题，
    无需评估其防交叉措施。判定先于设计——先确认危害情境是否存在，再决定是否建体系。
    可迁移模式：在启动一套管理程序之前，先用两个快速排除性问题（有无风险源？风险源之间
    会否相互作用？）筛查适用范围，避免对不存在风险的环节空转流程。
  tags: [supply-chain, applicability-test, exemption, screening]

- id: f3-23
  title: 供应商咨询声明审批门槛（声明≠免检，须证其未替代 CGMP）
  type: framework
  source_chapter: Ch11 §11.8.3.1 / §11.9.3（行 9508–9522、9836–9844）
  source_quote: |
    "we recommend that your supplier approval and verification activities include an evaluation
    of whether a potential supplier provides allergen advisory statements... When a potential
    supplier would provide an allergen advisory statement on the applicable raw materials...,
    we recommend that you discuss the reasons for the allergen advisory statements with the
    potential supplier before approving the supplier. You should approve a supplier that provides
    allergen advisory statements for its products only if you determine that such statements are
    not being used in lieu of adherence to CGMPs..."
  summary: |
    供应商附"may contain"声明本身不是取消资格项，但也不可作为放水通道：批准前必须与供应商
    讨论声明背后的原因（是清洁做不到？还是过度谨慎？），并形成书面判断——该声明不是在替代
    CGMP/交叉接触控制。若供应商以声明替代控制，则要么不批准，要么把更高验证强度（多批检测）
    作为补偿。
    可迁移模式：上游的免责声明必须被"解码"而不是被"透传"——追问声明的成因，区分真实技术限制
    与管理惰性，再决定接受条件。
    [本段重现] §11.8.3.1 与 §11.9.3 重复给出同一规则；Table 11-4 高风险情境是该规则的实例化。
  tags: [supplier-approval, advisory-statement, due-diligence, supply-chain]

- id: f3-24
  title: 标签控制全生命周期分段模型（内容线×管理线×七阶段）
  type: framework
  source_chapter: Ch11 §11.7.1（行 9026–9091）
  source_quote: |
    "we recommend that you establish and implement label controls and associated preventive
    control management components for: The content of the product label at the following stages:
    Development of labels; Ordering labels; Production of labels; and Receipt of labels. Managing
    printed labels, including storage, use, and disposition of product labels at the following
    stages: Storage of labels; Food production (including staging and packaging/labeling); and
    Post-production."
  summary: |
    防错标用两条正交的线覆盖标签全生命周期：内容线（标签上写什么对不对）管开发→订购→印制→
    接收四阶段（如订购合同规定标签文字、要求打样审核、限制电子文件编辑权限）；管理线（对的标签
    有没有被用到对的产品上）管储存→生产（备料/贴标）→生产后三阶段（如防混放、贴样于货位、
    换型时切换标签、及时报废旧版）。FDA 明示两线分类只是组织工具，可合并记录。
    可迁移模式：防错型控制可拆解为"制品正确性（内容）"与"过程正确性（使用）"两条正交维度，
    各沿时间轴分段布点。
  tags: [label-controls, lifecycle-model, error-proofing, allergen]

- id: f3-25
  title: 例外记录模式（只记异常的记录负担削减）
  type: framework
  source_chapter: Ch11 §11.5.6 / §11.7.5（行 8743–8746、9405–9415）
  source_quote: |
    "part 117 provides flexibility for records of monitoring to be 'exception records' - i.e.,
    records that you establish only when there is loss of control. ... if you use an automated
    barcode scanner to monitor that the correct label is applied to/used for the correct product,
    it may be adequate to generate exception records when the scanner detects that the wrong
    label is applied to the product."
  summary: |
    监控记录不必逐次全记：当监控由可靠的自动化手段（连续条码扫描、自动 CIP 记录）承担时，
    只在失控发生时生成记录即可；人工核查场景可用"检查单证明查过 + 例外记录记异常"的混合式。
    前提是正常态由设备/检查单背书，异常态有据可查。这把记录成本从 O(每次) 降到 O(每次异常)，
    同时不牺牲可追溯性。
    可迁移模式：高频重复性监控优先寻找"正常态的机器背书"，把人工记录仅留给异常，从而把记录
    从合规负担转化为异常信号。
  tags: [exception-records, record-keeping, automation, monitoring]
```

## 自检

- [x] 每条均有原文依据，引文摘自 source.md 行 6601–9900
- [x] 每条为可迁移思维结构（非单案例/金句）
- [x] 引文 ≤100 英文单词（部分以省略号截断）
- [x] 每条 ≥1 个 tag
- [x] 未做筛选（宁错杀，交阶段 1.5 三重验证）
- [x] 本段内"是否反复出现"仅基于本段（已以 [本段重现] 标注）
