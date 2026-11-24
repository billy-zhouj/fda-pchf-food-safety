# Stage 1 · Principles Chunk 3（source.md 第 6601–9900 行）
# 覆盖：Ch6 后半（§6.9–6.16 + 附录 6-A~E 热处理示例）+ Ch11 前半（§11.1–11.9 过敏原程序）
# 提取者：principle-extractor（分块 3/6）；"是否反复出现"仅限本段判断

```yaml
- id: p3-01
  title: 纠正措施四目标（corrective action 必须保证的四件事）
  type: principle
  source_chapter: Ch6 §6.9（21 CFR 117.150(a)）
  source_quote: |
    "The corrective action procedures must describe the steps to be taken to ensure that:
    (1) Appropriate action is taken to identify and correct a problem... (2) ...reduce the
    likelihood that the problem will recur; (3) All affected food is evaluated for safety; and
    (4) All affected food is prevented from entering into commerce, if you cannot ensure that
    the affected food is not adulterated or misbranded."
  summary: |
    纠正措施程序必须覆盖四个目标：①识别并纠正已发生的问题；②必要时降低问题
    复发的可能性；③对所有受影响食品做安全性评估；④无法确保不受掺杂/错标时
    阻止其进入商业流通。这是热处理、过敏原、供应链等所有预防控制共用的
    纠正措施骨架，本段在 Ch6 §6.9 与 Ch11 §11.5.3 逐字重复出现。
    判定产品处置时四项缺一不可，尤其第④项是防止问题产品流入市场的最后闸门。
  tags: [corrective-action, rule, regulatory, pchf-core]

- id: p3-02
  title: 热处理偏差的纠正措施选项清单
  type: principle
  source_chapter: Ch6 §6.9
  source_quote: |
    "Continue heating a product that has not reached the specified temperature...; Extend
    the length of the heat cycle...; Reprocess the product...; Chill and hold the product
    for an evaluation...; Divert the product to a use in which the critical limits...are not
    applicable (e.g., an RTE product may become a not-RTE product...); Divert the product
    to animal food...; Destroy the product."
  summary: |
    热处理未达规定温度/时间时的处置阶梯：继续加热补足→延长热循环（可用 process
    authority 的替代工艺）→完全重新加工→冷却留评估→改变用途（RTE 降为非 RTE
    或转原料）→转动物饲料（非宠物）→销毁。选项按"能否恢复安全性"排序，
    核心逻辑是产品在确认安全之前不得放行；RTE 降级为非 RTE 是常被忽略的合法选项。
  tags: [corrective-action, heat-treatment, checklist, disposition]

- id: p3-03
  title: 偏离操作限≠偏离关键限：只需质量评估，不触发纠正措施
  type: principle
  source_chapter: Ch6 §6.9
  source_quote: |
    "part 117 neither establishes requirements applicable to any assessment that you do for
    food quality if a process parameter deviates from an operating limit but does not deviate
    from a critical limit (e.g., if you have a procedure to assess food quality if the baking
    temperature for cookies is more than 5-10 degrees above the temperature set as a
    critical limit)."
  summary: |
    关键限是食品安全红线，操作限是基于质量原因的更严格内控线。偏离操作限但未
    破关键限时只做"调整（adjustment）"和质量评估，不触发法定纠正措施，也不强制
    记录。本段 Cookie A/B 均演示了该边界（15 分钟操作限 vs 13 分钟关键限）。
    设计操作限的目的是在碰红线之前就拦截偏差。
  tags: [critical-limit, operating-limit, rule, adjustment]

- id: p3-04
  title: 验证包含五类法定活动
  type: principle
  source_chapter: Ch6 §6.10 / Ch11 §11.5.2.2（21 CFR 117.155）
  source_quote: |
    "verification activities include, as appropriate to the nature of the preventive control
    and its role in your food safety system: (1) Validation; (2) Verification that monitoring
    is being conducted; (3) Verification that appropriate decisions about corrective actions
    are being made; (4) Verification of implementation and effectiveness; and (5) reanalysis."
  summary: |
    验证不是单一动作而是五类活动的统称：①validation（科学确认控制措施本身有效）；
    ②核实监控确被执行；③核实纠正措施决策恰当；④核实控制持续实施且有效；
    ⑤再分析。本段在 Ch6 和 Ch11 各出现一次，逐字一致。
    五类活动按"控制设计→日常执行→异常处置→整体有效→周期回顾"闭环排列。
  tags: [verification, framework-checklist, pchf-core]

- id: p3-05
  title: 日常验证四件套：校准、产品检测、环境监测、PCQI 记录审查
  type: principle
  source_chapter: Ch6 §6.10（21 CFR 117.165(a)）
  source_quote: |
    "Calibration of process monitoring instruments and verification instruments...; Product
    testing, for a pathogen...; Environmental monitoring...if contamination of a ready-to-eat
    food with an environmental pathogen is a hazard requiring a preventive control...; and
    Review of certain records by (or under the oversight of) a PCQI..."
  summary: |
    为确认控制"持续实施且有效"，必须（按适用性）开展：①监控/验证仪器校准；
    ②病原或危害的产品检测；③RTE 环境病原危害时的环境监测；④PCQI（或其监督
    下）的记录审查。四项均"as appropriate"，不是全选，但记录审查几乎是普适项。
    Ch6 与 Ch11 重复出现，是全书验证体系的操作层清单。
  tags: [verification, calibration, testing, records-review]

- id: p3-06
  title: 管理组件全部要记录：监控、纠正、验证三类记录缺一不可
  type: principle
  source_chapter: Ch6 §6.11 / Ch11 §11.5.6（21 CFR 117.145(b)-(c) 等）
  source_quote: |
    "you must document the preventive control management components as follows: (1) The
    monitoring of preventive controls in records that are subject to verification and records
    review; (2) all corrective actions (and, when appropriate, corrections) in records...;
    and (3) all verification activities."
  summary: |
    三类管理组件必须留痕：①监控记录（须经验证和记录审查）；②所有纠正措施
    （适当时含 correction）的记录；③所有验证活动的记录。记录不是附产品而是
    法定组件——"没有记录=没有做"。例外是监控可用 exception records（见 p3-24）。
  tags: [records, documentation, rule]

- id: p3-07
  title: PCQI 7 天记录审查规则
  type: principle
  source_chapter: Ch6 §6.12.5 / §6.13.5（Cookie Processor A/B 示例）
  source_quote: |
    "Within 7 days of their creation the PCQI reviews the following records, dates and
    initials the records or a verification cover sheet to document that review, and then
    files the records: o The calibration logs...; and o The oven recording thermometer
    charts, operator's baking log, tachometer charts, and dough weight sheets..."
  summary: |
    监控、校准等记录须由 PCQI 在创建后 7 天内（示例中"within a week"）审查、
    签注日期和缩写并归档；纠正措施记录须在偏差发生后一周内审查。7 天是示例
    给出的"合理时限"基准，Soup A 因偏差极少而书面论证采用更长的出货前审查
    周期（见 p3-15）——时限可论证调整但须记录依据。
  tags: [records-review, pcqi, timeline-rule, numeric]

- id: p3-08
  title: Cookie A/B 三关键限 + 三操作限（350°F/13min/28g）
  type: principle
  source_chapter: Ch6 §6.12.2 / §6.13.2
  source_quote: |
    "The critical limit (minimum value) for the baking temperature is 350°F (177°C); The
    critical limit (minimum value) for the baking time is 13 minutes; and The critical limit
    (maximum value) for the cookie dough portion size is 28 g. ... The operating limit for
    the baking temperature is 352°F (178°C); The operating limit for the baking time is
    15 minutes; and The operating limit for cookie dough portion size is 27 g."
  summary: |
    批式与连续烘焙两条产线采用完全相同的关键限（炉温≥350°F、烘焙≥13 分钟、
    面团份量≤28g）与操作限（352°F / 15min / 27g）。依据是 Lathrop 2014 发表研究
    （13 分钟达 5.2 log 减少沙门氏菌）+ 本厂热分布/热穿透验证。
    关键限必须同时锁定温度、时间、份量三个参数——只控温度会因份量超标而失效。
  tags: [critical-limit, numeric, heat-treatment, validation]

- id: p3-09
  title: 关键限确立 = 发表研究 + 厂内热分布/热穿透双重验证
  type: principle
  source_chapter: Ch6 §6.12.2 / §6.13.2（Cookie A/B 验证路径）
  source_quote: |
    "the extension specialist conducted in-house heat distribution tests on Cookie Processor
    A's ovens and heat penetration tests on the cookies using a fully loaded oven... These
    in-house heat distribution and heat penetration tests showed that all parts of each of
    Cookie Processor A's oven were at or above 350°F (177°C)... and that the coldest cookie
    temperature was above 230°F (110°C) after 13 minutes."
  summary: |
    确立热处理关键限的两步法：①引用针对同类食品/配方的发表致死率研究；
    ②在本厂设备做热分布（最冷点确认）和热穿透（产品内部温度）研究，且须用
    满载烤箱作最坏情况。发表研究只证明"工艺原理可行"，厂内研究证明"我的设备
    做得到"——两者缺一不可。配方后续任何变更都须重新评估是否影响结论。
  tags: [validation, heat-treatment, process-design, method]

- id: p3-10
  title: 配方/工艺变更须重新评估关键限
  type: principle
  source_chapter: Ch6 §6.12.2
  source_quote: |
    "The extension specialist informed Cookie Processor A that any subsequent change to the
    cookie recipe should be evaluated to determine whether it would impact these
    determinations."
  summary: |
    验证结论只对"被验证的配方和条件"有效。任何配方变更（水分活度、份量、
    成分）都可能改变致死率需求，必须重新评估原关键限是否仍然成立。
    这是"validation 是有条件的结论"的直接体现，也是再分析触发器的微观版本。
  tags: [validation, change-control, rule]

- id: p3-11
  title: EPIPT 适用条件：升温/降温附加致死量可被计入
  type: principle
  source_chapter: Ch6 §6.14.2（Soup Processor A）
  source_quote: |
    "Because of the additional lethality during the heating time needed for the soup to
    reach 180°F (82°C), and because more than 3 seconds would elapse before cooling from
    180°F could begin, Soup Processor A's PCQI decided to use an EPIPT and cook the soups
    until the temperature reaches 180°F rather than to continuously monitor temperature
    during cooking."
  summary: |
    当升温和降温阶段的附加致死量使得"到达目标温度即等效达标"时，可用终点内部
    产品温度（EPIPT）替代全程时间-温度监控：只需监控"何时达到 180°F"，无需
    连续记录保温时间。EPIPT 大幅简化监控，但前提是致死需求极小（本例 6D 仅需
    3 秒），由升降温冗余覆盖——冗余不足时不可使用。
  tags: [epipt, monitoring, heat-treatment, rule]

- id: p3-12
  title: Soup A 关键限：EPIPT 180°F + 颗粒≤½英寸（前提冷藏不冻）
  type: principle
  source_chapter: Ch6 §6.14.2
  source_quote: |
    "as long as vegetable particles in the soup did not exceed ½ inch (13 mm) square, the
    particles would also be at 180°F when the liquid portion of the soup reached that
    temperature, provided that the particles were stored refrigerated (i.e., at least 33°F)
    and not frozen. ... Soup Processor A established two critical limits...: Minimum EPIPT
    of 180°F (82°C); and Maximum size of vegetable particles (½ inch (13 mm))."
  summary: |
    多组分食品的热穿透由颗粒尺寸决定：颗粒≤½英寸且保持冷藏（33–40°F、不冻结）
    时，颗粒与液体同步达到 180°F。因此关键限是"EPIPT≥180°F + 颗粒最大尺寸
    ≤½英寸"，而颗粒温度本身无需关键限——条件（冷藏 SOP）被写入判定前提。
    粒径超标意味着热穿透失效，即使汤温达标也不安全。
  tags: [critical-limit, numeric, heat-penetration, multi-component]

- id: p3-13
  title: 目标菌选择规则：ROP+冷藏→非蛋白分解 C. botulinum B 型
  type: principle
  source_chapter: Ch6 §6.15.1（Soup Processor B）
  source_quote: |
    "Because hot-filling into 5-gallon bags would result in reduced oxygen packaging, and
    because the soups will be distributed refrigerated, Soup Processor B's PCQI/food
    processing expert determined that C. botulinum non-proteolytic type B is an appropriate
    target organism for the soup heat treatment."
  summary: |
    目标菌按"最耐热且能在该产品中生长的病原"选取：热灌装=减氧包装（厌氧）+
    冷藏流通→蛋白分解型肉毒梭菌可生长，其中非蛋白分解 B 型最耐热，故以其为
    目标菌。针对 B 型的工艺自动覆盖沙门氏菌和李斯特菌。规则本质：
    包装氧环境 × 储运温度 × 耐热性三因素共同决定目标菌，不能按惯例照搬他人工艺。
  tags: [target-organism, rop, clostridium, rule, heat-treatment]

- id: p3-14
  title: Soup B 工艺：205°F×2.5min（等效 194°F/90°C×10min）达 6D
  type: principle
  source_chapter: Ch6 §6.15.2
  source_quote: |
    "Soup Processor B's PCQI/food processing expert decided to use a process of 205°F (96°C)
    for 2.5 minutes (equivalent to a minimum temperature of 194°F (90°C) for a minimum of
    10 minutes) based on Table 3-E... This time and temperature combination will deliver a
    6D process for the most heat resistant spores for strains of C. botulinum non-proteolytic
    type B."
  summary: |
    连续热交换工艺选用 205°F×2.5 分钟（维持管），等效于 90°C×10 分钟，对非蛋白
    分解 B 型肉毒最耐热孢子实现 6D。五个关键参数：初始温度 IT 40–45°F、计量泵
    转速（流量）、维持管规格（≥2.5min）、维持管出口温度≥205°F、热保温罐
    ≥185°F。任一参数失控都可能使名义工艺不成立——连续系统须锁全部参数。
  tags: [numeric, critical-limit, 6d, continuous-process]

- id: p3-15
  title: 热处理后不暴露环境→可不做产品检测与环境监测；审查时限可书面论证放宽
  type: principle
  source_chapter: Ch6 §6.15.5 / §6.14.5（Soup B / Soup A）
  source_quote: |
    "Soup Processor B does not conduct product testing for pathogens or environmental
    monitoring because the product, which is subjected to a heat treatment validated to be
    highly lethal to vegetative pathogens and filled hot, is not exposed to the environment
    after the heat treatment. ... the PCQI has determined and documented that this timeframe,
    rather than 7 working days, is reasonable."
  summary: |
    验证活动的取舍依据"暴露史"：热处理+热灌装后不再暴露于环境的产品，无需
    病原检测和环境监测——验证强度与风险路径匹配，不是越多越好。同理，Soup A
    的 PCQI 书面论证并以记录支持"出货前审查"替代 7 天时限。两条规则共同表明：
    法定要求可按 facility/食品/控制性质弹性裁剪，但每项裁剪都要书面化。
  tags: [verification, product-testing, flexibility, documented-justification]

- id: p3-16
  title: 酸化食品致死目标：158°F×1.5min 达 5D（pH≤4.1 下针对营养细胞）
  type: principle
  source_chapter: Ch6 §6.16.2（Salsa Processor A）
  source_quote: |
    "Salsa Processor A's PCQI/process authority selected a process (158°F (70°C) for 1.5
    minutes) that will deliver a 5D process for Salmonella, E. coli O157:H7, and Listeria
    monocytogenes at a product pH of no higher than 4.1 (Breidt et al., 2010)."
  summary: |
    pH≤4.1 的酸化食品中肉毒孢子不能萌发，致死工艺只需针对营养细胞病原
    （沙门氏菌、E. coli O157:H7、李斯特菌），158°F×1.5 分钟即达 5D。货架期
    稳定性所需的更高工艺（200°F×2min 杀腐败孢子）作为操作限，但因涉及商业
    可储性，企业将其"视同关键限"管理——安全限与货架期限叠加时的从严原则。
  tags: [numeric, acidified-food, 5d, lethality]

- id: p3-17
  title: pH 界限决定目标菌：孢子菌 pH 4.2 以下不生长
  type: principle
  source_chapter: Ch6 §6.16.1（Salsa Processor A，引 Rodriguez et al. 1992）
  source_quote: |
    "the scientific literature indicated that these sporeformers do not grow at pH 4.2 or
    less and require oxygen for growth at pH 4.4. Salsa Processor A's salsa is acidified to
    pH 4.1; thus Salsa Processor A's PCQI/process authority determined that the heat
    treatment should target vegetative pathogens..."
  summary: |
    目标菌选择要有文献数值支撑：致腐败孢子菌（B. subtilis 等）pH≤4.2 不生长、
    pH 4.4 需氧生长，故酸化至 pH 4.1 的莎莎酱无需针对孢子设计致死工艺，但要
    防止孢子菌产氨把 pH 抬回 4.6 以上（pHovertake 风险）。规则：先定 pH 屏障，
    再定热处理目标——屏障和致死是互补控制而非二选一。
  tags: [ph, target-organism, acidified-food, rule]

- id: p3-18
  title: 冷却陷阱：颗粒冷藏条件不达标即热穿透失效
  type: principle
  source_chapter: Ch6 §6.14.2 / §6.16.2（Soup A 与 Salsa A 共同模式）
  source_quote: |
    "Salsa Processor A determined that the size of the particles in the vegetable salsa is a
    parameter requiring a critical limit (i.e., a maximum value of 1.0 cm square). However,
    ...a critical limit for the temperature of the particles...is not necessary as long as the
    production line follows the SOP to store the particles refrigerated."
  summary: |
    Soup A（≤½ 英寸）与 Salsa A（≤1.0cm）采用同一判定模式：粒径关键限的成立
    以"颗粒冷藏（≥33°F）且不冻结"为前提。颗粒初始温度若冻结或升温，热穿透
    时间改变，名义工艺失效。规则：粒径这一看得见的参数背后藏着一个看不见的
    前提（原料温度史），SOP 本身成为关键限成立的条件链。
  tags: [particle-size, refrigeration, hidden-assumption, heat-penetration]

- id: p3-19
  title: 15 批强化监测规则：超标后逐批检验，连续 15 批合格才降频
  type: principle
  source_chapter: Ch6 §6.14.4 / §6.16.4（Soup A / Salsa A 纠正措施）
  source_quote: |
    "The formulation control operator will check the vegetable particle size of every lot for
    the next 15 lots to verify particle sizes meet specification. If all 15 lots meet
    specification, the formulation control operator will return to monitoring every third
    lot."
  summary: |
    颗粒尺寸失控后的监测升级协议：从"每 3 批抽 1"立即升为"逐批检验"，连续
    15 批全部合格方可恢复原频率；同时退货、与供应商查找根因。数值化的降级
    条件消除了"何时放松"的主观判断。适用于任何以抽样为基础的监控参数：
    一次失察=信任破产，须用连续合格记录重新赢得降频资格。
  tags: [monitoring-frequency, numeric, corrective-action, escalation]

- id: p3-20
  title: 校准年度底线：仪表至少每年校准，日常做准确性核查
  type: principle
  source_chapter: Ch6 §6.12.5 / §6.13.5 / §6.15.5（各示例共同模式）
  source_quote: |
    "The following are calibrated at least annually: o The recording thermometer that
    monitors oven temperature; o The dough depositor; and o The scales used to check the
    weights of cookie portions."
  summary: |
    所有示例厂对本段出现的监控/验证设备（记录温度计、转速计、面团 depositor、
    天平、RTD）执行"至少每年一次校准"（部分由外部计量机构现场进行），同时
    以更高频的准确性核查（如温度计每日对 NIST 参考温度计核查、卡尺使用前
    归零检查）托底。校准记录须注明执行人、方法、日期、合格与否及所做调整。
  tags: [calibration, numeric, verification, annual]

- id: p3-21
  title: 偏差处置三角色分工：PCQI 判安全、经理查根因、培训操作工
  type: principle
  source_chapter: Ch6 §6.12.4 / §6.15.4 / §6.16.4（示例共同模式）
  source_quote: |
    "The PCQI will assess the safety of the product to determine appropriate disposition...
    The production manager will investigate why the pump speed was too fast and take
    appropriate actions to prevent the situation from reoccurring... Employees will be
    retrained if necessary..."
  summary: |
    偏差响应的标准角色分工：产品是否安全、如何处置由 PCQI 判定（技术判断权）；
    根因调查与防复发整改由生产经理负责（管理权）；必要时对操作工再培训
    （执行层）。三者不可互相替代——PCQI 不代替管理整改，管理层不代替安全
    判定。本段 5 个示例厂全部采用此模式，属本段反复出现的规则。
  tags: [corrective-action, roles, division-of-labor, pattern]

- id: p3-22
  title: 过程日志（process log）最低要素：设施标识+日期+操作工签名+审查证据
  type: principle
  source_chapter: Ch6 §6.11.1.1 / §6.11.1.2
  source_quote: |
    "You should keep these records in a 'process log' for each production line, with
    information to identify the plant or facility, dates (and when appropriate, the time)
    of monitoring, the signature or initials of the person performing the monitoring
    (e.g., operator initials) and evidence of review (i.e., the initials of the PCQI or
    designee)."
  summary: |
    每条产线的过程日志须包含四要素：设施/工厂标识、监控日期（适当时含时间）、
    监控执行人签名或缩写、审查证据（PCQI 或其指定人的缩写）。批式与连续设备
    的日志要素相同，仅记录内容不同（温度/时间/记录纸 vs 转速/维持管号）。
    四要素缺任何一项，记录都无法自证其链路完整性。
  tags: [records, process-log, checklist, minimum-elements]

- id: p3-23
  title: 调整（adjustment）记录虽非强制但应保留，用于识别系统性问题
  type: principle
  source_chapter: Ch6 §6.12.7 / §6.13.7（Cookie A/B）
  source_quote: |
    "Cookie Processor A also keeps records of adjustments, because such records could be
    useful in identifying ongoing production problems that could demonstrate a need to
    review and change applicable production procedures."
  summary: |
    偏离操作限（未破关键限）的调整不强制记录，但两个示例厂均保留：调整记录
    的累积模式能暴露系统性生产问题，从而触发程序复审与变更。规则延伸：
    "不强制"不等于"无价值"——低强制要求的记录往往正是趋势分析的原料。
  tags: [records, adjustment, trend-analysis, voluntary-practice]

- id: p3-24
  title: 过敏原控制不需要 validation
  type: principle
  source_chapter: Ch11 §11.5.2.2 脚注 18（21 CFR 117.160(c)(1)）
  source_quote: |
    "During the rulemaking to establish part 117, we acknowledged that it is premature to
    require validation of food allergen controls... As a result, part 117 does not require
    validation of food allergen controls... However, nothing in part 117 would prevent you
    from validating a food allergen control, if you choose to do so..."
  summary: |
    法规明确豁免：食品过敏原控制不要求 validation（不同于工艺控制），因为
    过敏原交叉接触控制的"有效性证据"尚不成熟。企业自愿做验证不被禁止，
    指南中的某些验证程序稍加修改即可构成 validation 研究的一部分。
    注意区分：不需要 validation ≠ 不需要 verification——过敏原控制仍需监控、
    纠正、日常验证全套管理组件。
  tags: [allergen, validation, exemption, rule]

- id: p3-25
  title: 咨询声明（may contain）不能替代 CGMP 或预防控制
  type: principle
  source_chapter: Ch11 §11.1 / §11.4.3 / §11.9.1
  source_quote: |
    "You should not use allergen advisory statements (formerly called allergen precautionary
    labeling) in lieu of adherence to CGMPs or in lieu of the requirements for allergen
    cross-contact controls; If you use allergen advisory statements, they must be truthful
    and not misleading."
  summary: |
    "可能含有"类咨询声明是最后手段而非免责工具：不得用来替代 CGMP 或交叉接触
    预防控制；一旦使用必须真实且不误导。本规则在 Ch11 至少四处重复（§11.1、
    §11.4.3、§11.8.3.1、§11.9.1），是本章出现频次最高的原则。监管逻辑：
    允许声明存在是为了承认控制有极限，而不是给控制不到位开后门。
  tags: [allergen, advisory-statement, rule, repeated-in-chunk]

- id: p3-26
  title: 使用咨询声明须 PCQI 书面论证
  type: principle
  source_chapter: Ch11 §11.1 / §11.9.2
  source_quote: |
    "If you use allergen advisory statements, your preventive controls qualified individual
    (PCQI) should provide a written justification, in your food safety plan, for why
    allergen cross-contact controls cannot ensure protection of food from allergen
    cross-contact."
  summary: |
    咨询声明的使用门槛是 PCQI 在 FSP 中的书面论证：说明为什么已实施的交叉接触
    控制仍无法保证保护食品。论证把"贴声明"从随意行为变成有据可查的技术决定，
    检查时可被质询。声明设计还须考虑消费者的实际阅读习惯（见 §11.9.4 关于
    复购者不再阅读配料表的警告）。
  tags: [allergen, advisory-statement, pcqi, written-justification]

- id: p3-27
  title: 供应商用咨询声明→须先谈原因，不用作 CGMP 替代才可批准
  type: principle
  source_chapter: Ch11 §11.8.3.1 / §11.9.3
  source_quote: |
    "You should approve a supplier that provides allergen advisory statements for its
    products only if you determine that such statements are not being used in lieu of
    adherence to CGMPs or in lieu of adherence to the requirements for allergen
    cross-contact controls."
  summary: |
    供应商批准规则：潜在供应商若对其原料出具过敏原咨询声明，须先与其讨论声明
    的原因；仅当确认声明不是 CGMP/预防控制的替代品时方可批准。接收方的批准
    责任延伸到了供应商的声明动机—— blindly 接受带声明的原料等于替供应商的
    控制漏洞买单。
  tags: [allergen, supplier-approval, advisory-statement, rule]

- id: p3-28
  title: 供应商咨询声明的三选一书面决定
  type: principle
  source_chapter: Ch11 §11.8.4 / §11.9.3
  source_quote: |
    "your PCQI should provide, in your food safety plan, a written determination of whether:
    - The allergen advisory statement has no impact on the food allergen profile of your
    products...; - You will carry an allergen advisory statement forward to one or more of
    your food products...; or - You will rely on a scientifically valid determination...that
    the amount of food allergen...is low enough..."
  summary: |
    批准出具咨询声明的供应商后，PCQI 必须书面决定：①不传递（自己产品本就
    含该过敏原、标签已声明）；②传递（把声明带上自己的产品标签，并按含过敏原
    原料管理该原料）；③阈值论证（用科学有效评估证明残留量低到不致敏）。
    三个选项互斥且必须书面化——沉默不构成决定。
  tags: [allergen, advisory-statement, decision-rule, three-options]

- id: p3-29
  title: 过敏原危害=SAHCODH→首次使用前审计+每年现场审计
  type: principle
  source_chapter: Ch11 §11.8.1 / §11.8.3.2（21 CFR 117.430(b)）
  source_quote: |
    "When a hazard that requires a supply-chain applied control is a SAHCODH hazard..., an
    audit is required as a supplier verification activity in most circumstances, before using
    the raw material or other ingredient from the supplier and at least annually thereafter...
    a food allergen hazard will be a SAHCODH hazard and generally an annual audit will be
    required..."
  summary: |
    过敏原反应可致严重后果或死亡（如过敏性休克），故过敏原危害通常属 SAHCODH
    危害，触发供应链硬要求：使用该供应商原料之前做审计，此后至少每年一次。
    唯一出口是 PCQI 书面认定其他验证活动/更低频现场审计足以保证危害受控
    （117.430(b)(2)）。审计间隔无法定"13–14 个月宽限"的明文，但年度要求在
    本段以"at least annually"表述为刚性底线。
  tags: [sahcodh, supply-chain, annual-audit, numeric, rule]

- id: p3-30
  title: 检测只能是供应商验证的补充，永远不能是唯一手段
  type: principle
  source_chapter: Ch11 §11.8.3.2
  source_quote: |
    "Due to limitations in product testing, testing that you conduct as a supplier approval
    or verification activity should be in addition to other supplier approval and
    verification activities rather than the sole supplier approval and verification
    activity."
  summary: |
    产品检测存在固有局限（过敏原/病原分布不均匀，抽样天然有漏检风险），因此
    检测只能作为其他批准/验证活动之外的补充，不能单独承担供应商把关。
    本段与全书主题一致（Ch15 亦强调），属跨章原则。检测频率还应随供应商
    控制水平浮动：控制好→年检，控制差→月检/季检（见 p3-31）。
  tags: [testing, supplier-verification, limitation, rule]

- id: p3-31
  title: 检测频率与供应商控制水平挂钩：年检 vs 月/季检
  type: principle
  source_chapter: Ch11 §11.8.3.2
  source_quote: |
    "if a supplier that processes food products with different food allergen profiles on the
    same processing line combines scheduling, allergen cleaning procedures, and frequent
    verification testing in its food safety plan, your PCQI could determine that annual
    testing is appropriate. However, if a supplier...does not do verification testing, more
    frequent testing (such as monthly or quarterly) could be appropriate."
  summary: |
    接收方检测频率的定价规则：供应商用排产+过敏原清洁+高频验证测试组合控制
    →年检即可；供应商同线生产且不做验证测试→月检或季检。检测成本被精确
    转嫁给控制差的供应商。配套设计：取样计划须考虑食品是否均质、交叉接触
    过敏原是否均匀分布（液体均质 vs 坚果碎块非均质）。
  tags: [testing-frequency, supplier, risk-based, numeric]

- id: p3-32
  title: 两类情形无需建立过敏原供应链程序
  type: principle
  source_chapter: Ch11 §11.8.2
  source_quote: |
    "In general, we see no reason for you to establish and implement a supply-chain program
    for the control of food allergen hazards if: - You will receive a raw material or other
    ingredient from a supplier that does not manufacture, process, or pack any food
    allergens; or - ...that food allergen is the only food allergen that the supplier
    manufactures/processes."
  summary: |
    供应链程序的豁免边界：①供应商完全不做任何过敏原；②供应商只做你要的那
    一种过敏原（如杏仁商只处理杏仁、不做其他坚果/乳/豆）。两种情形下不存在
    "不同过敏原档案的交叉接触"，无需评估其防交叉措施。规则本质：
    供应链控制针对的是"供应商厂内的过敏原多样性"，不是过敏原本身。
  tags: [supply-chain, exemption, allergen, rule]

- id: p3-33
  title: 供应链程序只适用管理组件的子集（无监控组件）
  type: principle
  source_chapter: Ch11 §11.5.4（21 CFR 117.140(b)）
  source_quote: |
    "the supply-chain program as a whole is subject to a subset of preventive control
    management components – i.e., corrective actions and corrections, review of records,
    and reanalysis. (See 21 CFR 117.140(b).)"
  summary: |
    供应链程序作为预防控制，只受三个管理组件约束：纠正措施与纠正、记录审查、
    再分析——不含"监控"组件（因为供应商端活动由供应商执行，接收方无法直接
    监控）。这是管理组件"按控制性质裁剪"的法定范例，与过敏原控制豁免
    validation 形成对照。
  tags: [supply-chain, management-components, subset, rule]

- id: p3-34
  title: Exception record 灵活性：监控记录可只记异常
  type: principle
  source_chapter: Ch11 §11.5.6 / §11.7.5（21 CFR 117.145(c)(2)）
  source_quote: |
    "part 117 provides flexibility for records of monitoring to be 'exception records' -
    i.e., records that you establish only when there is loss of control. ... if you use an
    automated barcode scanner to monitor that the correct label is applied..., it may be
    adequate to generate exception records when the scanner detects that the wrong label is
    applied..."
  summary: |
    监控记录允许采用"例外记录"模式：控制正常时无记录，仅在失控时建立记录。
    典型场景：条码扫描器持续监控标签正确性→只在检出错标时生成记录；或用
    检查清单证明监控已做+例外记录记不符项。该机制大幅降低高频自动化监控的
    记录负担，但要求监控手段本身可靠（自动化/连续）。
  tags: [exception-record, records, flexibility, allergen-label]

- id: p3-35
  title: 同一活动可归为监控或验证——不许重复建设，但必须足够
  type: principle
  source_chapter: Ch11 §11.5.2.3 / §11.6.1.1 / §11.7.2
  source_quote: |
    "it generally makes little difference whether you consider such an activity to be
    monitoring or verification... part 117 does not require that you establish and implement
    both a monitoring activity and a verification activity if the same activity (such as
    visual observation) would be used as both... Regardless of what you call them, you must
    have procedures that are adequate to ensure the effectiveness of the preventive controls."
  summary: |
    对过敏原控制和标签控制，同一活动（如目视观察 FCS 是否可见洁净、核对标签
    内容）可自由归类为监控或验证——名称不重要，充分性才重要；不得为同一活动
    建两套平行体系。惯例参考：清洁水温检查≈监控，校准和记录审查=法定验证。
    该规则把管理组件从"形式分类"解放为"效果导向"。
  tags: [monitoring, verification, flexibility, naming-irrelevant]

- id: p3-36
  title: 及时纠正=免于纠正措施的两种情形
  type: principle
  source_chapter: Ch11 §11.5.3（21 CFR 117.150(c)）
  source_quote: |
    "you do not need to take corrective actions if you take action, in a timely manner, to
    identify and correct conditions and practices that are not consistent with the food
    allergen controls..., or if you take action, in a timely manner, to identify and correct
    a minor and isolated problem that does not directly impact product safety (i.e., make
    corrections)."
  summary: |
    两种情形只需 correction（纠正）无需 formal corrective action：①及时纠正与
    过敏原控制不一致的条件/做法（如 CIP 温度失准但在投产前查明根因、调温并
    重跑完整 CIP）；②及时纠正不直接影响产品安全的轻微孤立问题（如标签使用前
    发现错标并纠正）。边界判定：问题是否已触及产品 + 是否孤立。
  tags: [correction, corrective-action, allergen, boundary-rule]

- id: p3-37
  title: 错标已用于生产=错标（misbrand），必须走纠正措施并可能召回
  type: principle
  source_chapter: Ch11 §11.7.3
  source_quote: |
    "Determining that the content of a product label/package is incorrect...after using the
    label/package in production. Because an incorrect label...would misbrand the food under
    section 403(w)..., the incorrect label content is not a minor problem... - Ensuring that
    any food with an incorrect label does not enter commerce...and - Recalling food with an
    incorrect label if the food has already entered commerce."
  summary: |
    标签错误的时间点决定处理等级：使用前发现→correction 即可；已用于生产→
    食品依法错标，必须启动纠正措施（查明原因、防复发、评估产品、阻止入市），
    已流入市场的须召回。处置选项含返工、重贴标、重包装、转动物饲料、销毁。
    规则：过敏原标签错误的严重性与"是否已接触产品"绑定，而非错误大小。
  tags: [label-control, misbrand, recall, corrective-action]

- id: p3-38
  title: 受影响批次范围界定：从清洁到清洁（cleanup to cleanup）
  type: principle
  source_chapter: Ch11 §11.6.1.2
  source_quote: |
    "Determining whether food is affected and, if so, evaluating that food for safety, and
    ensuring that the food with an unintended allergen does not enter commerce... In
    determining which food is affected, we recommend that you consider all food lots
    produced from cleanup to cleanup."
  summary: |
    清洁失效检出过敏原残留时，受影响食品的推定范围是"上次合格清洁到下次清洁
    之间生产的所有批次"——因为交叉接触的边界由清洁事件定义，而非由发现时点
    定义。该推定规则把举证负担放回企业：要缩小范围，须证明中间清洁确实有效。
  tags: [allergen, affected-lots, cleanup-boundary, rule]

- id: p3-39
  title: 反复发生=程序无效→触发再分析（本段三种场景）
  type: principle
  source_chapter: Ch11 §11.6.1.2/§11.6.1.3 / §11.7.4 / §11.8.6
  source_quote: |
    "if repeated findings of product residue on a cleaned FCS lead you to determine that the
    cleaning procedure is not effective, your corrective action procedures should include
    reanalysis of your food safety plan... Reanalysis of your label controls is appropriate
    if, for example, you have recurring problems with your label content controls or label
    management controls."
  summary: |
    "孤立 vs 反复"的判定后果在再分析环节兑现：清洁面反复检出残留、标签控制
    反复出问题、供应商持续不合规——任一反复都表明程序本身无效，须对 FSP
    相应部分再分析（而非继续逐次 correction）。再分析结论甚至可能反转：
    证明控制确实无法避免交叉接触→转为使用咨询声明（见 p3-40）。
  tags: [reanalysis, recurring-problem, trigger, rule]

- id: p3-40
  title: 再分析可反向推出"咨询声明此时才合适"
  type: principle
  source_chapter: Ch11 §11.6.1.3 / §11.8.6 / §11.9.4
  source_quote: |
    "reanalysis of your allergen cleaning procedures could lead you to conclude that allergen
    advisory statements are appropriate because, despite using appropriate CGMPs and
    preventive controls, residues or allergen cross-contact cannot be avoided."
  summary: |
    咨询声明的正当使用路径是"再分析的产物"：已用适当 CGMP 和预防控制仍无法
    避免交叉接触→修订 FSP 加入书面论证→标签披露可能的非预期过敏原存在。
    与 p3-25 合并看构成完整规则：声明不能是起点，只能是控制极限被证明后的
    出口；且声明设计要让过敏消费者第一眼可见（包括复购场景）。
  tags: [advisory-statement, reanalysis, last-resort, rule]

- id: p3-41
  title: FSP 至少每 3 年再分析 + 四类事件触发
  type: principle
  source_chapter: Ch11 §11.5.5（21 CFR 117.170）
  source_quote: |
    "conduct a reanalysis of the food safety plan as a whole at least once every 3 years...
    (1) Whenever a significant change...creates a reasonable potential for a new hazard...;
    (2) whenever you become aware of new information about potential hazards...; (3)
    whenever appropriate after an unanticipated food safety problem; and (4) whenever you
    find that a preventive control...is ineffective."
  summary: |
    再分析双轨制：周期轨（至少每 3 年一次全计划）+ 事件轨（①设施活动重大变化
    引入新危害/加重已知危害；②获知危害新信息；③意外食品安全问题后酌情；
    ④发现控制或计划整体无效）。事件轨再分析可限于 FSP 相关部分。
    本段在 Ch11 作为过敏原各节再分析义务的总纲出现。
  tags: [reanalysis, 3-year, trigger, numeric]

- id: p3-42
  title: 表格即程序：用于记录的表单可充当书面程序
  type: principle
  source_chapter: Ch11 §11.6.1 / §11.7.1
  source_quote: |
    "a form that you would use to document a monitoring activity could function as a written
    procedure for the monitoring activity, because the person who conducts the monitoring
    could use the form as a guide for what to monitor."
  summary: |
    书面程序要求的务实解法：设计良好的记录表单（检查清单、SSOP 附表）本身
    就能充当书面监控/验证/纠正程序，因为执行者可照表操作。前提是表单字段
    完整指引了"做什么、怎么判、不符怎么办"。该规则显著降低小企业的文书
    负担——程序文件与记录表可以二合一。
  tags: [written-procedures, forms, practical, flexibility]

- id: p3-43
  title: 过敏原清洁 SSOP 的七要素
  type: principle
  source_chapter: Ch11 §11.6.1
  source_quote: |
    "We recommend that your SSOP for allergen cleaning procedures include the following...
    - The purpose of the cleaning procedure...; - The frequency of cleaning...; - Who is
    responsible...; - Instructions to perform the specific cleaning procedure...; - A list
    of monitoring/verification activities...; - Corrections or corrective actions to take...;
    and - Any forms that you will use..."
  summary: |
    过敏原清洁程序文件（SSOP）推荐七要素：目的、清洁频率（含与换产的时序
    关系）、责任人、具体操作指令（清洁剂类型/浓度/工具/步骤/是否拆机）、
    监控与验证活动清单、不符时的纠正/纠正措施、所用表单。文件按湿清洁/干清洁
    分别定制——干清洁的控水逻辑（防沙门氏菌）与湿清洁的化学逻辑不同。
  tags: [allergen-cleaning, ssop, checklist, seven-elements]

- id: p3-44
  title: 清洁验证的检测工具分级：ATP/蛋白拭子非特异，过敏原专用试剂盒才特异
  type: principle
  source_chapter: Ch11 §11.6.1.1 脚注 21
  source_quote: |
    "ATP tests are considered 'non-specific' tests for cleanliness because ATP is found in
    all living cells... ATP tests and other 'non-specific' tests...have the potential to be
    more sensitive than visual observation but may not be sensitive enough to detect levels
    of a particular allergenic protein."
  summary: |
    清洁效果验证工具的能力边界：目视检查（可见洁净）< ATP/蛋白拭子（非特异，
    灵敏度高于目视但可能检不出特定过敏原蛋白水平）< 过敏原专用检测试剂盒
    （特异）。工具选择须与"要证明什么"匹配：证明一般清洁用 ATP，证明特定
    过敏原去除须用专用试剂盒或冲洗水检测；push-through 物料也可检测。
  tags: [cleaning-verification, atp, test-kit, tool-capability]

- id: p3-45
  title: 标签控制覆盖全生命周期：开发→订购→生产→接收→储存→产线→产后
  type: principle
  source_chapter: Ch11 §11.7.1
  source_quote: |
    "we recommend that you establish and implement label controls and associated preventive
    control management components for: - The content of the product label at the following
    stages: o Development of labels; o Ordering labels; o Production of labels; and o
    Receipt of labels. - Managing printed labels, including storage, use, and disposition..."
  summary: |
    标签控制分两条线：标签内容控制（开发/订购/生产/接收四阶段）+ 标签管理
    控制（储存/产线使用（staging 与贴标）/产后三阶段）。关键设计：订购文件须
    写明过敏原标签规格文本、要求提供 proofs 供审核、防混料措施；电子自印标签
    要控制文件使用权限与正确文件调用。内容控制与标签管理高度关联，可共用
    一份监控活动/记录。
  tags: [label-control, lifecycle, checklist, allergen]

- id: p3-46
  title: 标签内容核对时点：接收时/放行前/投产前至少其一
  type: principle
  source_chapter: Ch11 §11.7.2.3
  source_quote: |
    "We recommend that you monitor or verify the content of the product label before you use
    it for production by comparing the product labels/packages to your food allergen label
    specification at one or more of the following stages: - Upon receipt of the label...;
    - Before new batches of labels are released for use during production; or - Immediately
    prior to production."
  summary: |
    标签内容与过敏原标签规格的核对必须在投产前完成，可选时点：标签接收时
    （自印标签为打印后）、新批次放行前、投产前即时。FDA 注释点明核心逻辑：
    "投产前核对内容这一动作"比"在哪个时点核对"更重要——早发现可避免停产
    等待期损失。正确标签应用到正确产品的确认则须在生产开始时及每次上新标签时做。
  tags: [label-content, timing, before-production, rule]

- id: p3-47
  title: 条码扫描器的监控频率规则：连续扫描=连续监控，人工扫描按间隔
  type: principle
  source_chapter: Ch11 §11.7.2.3.2
  source_quote: |
    "Monitor or verify continuously during production if the barcode scanner scans
    continuously, or at regular intervals if you manually operate the barcode scanner or
    manually confirm that the correct label/package is applied to/used for the correct
    product (e.g., 1-, 2-, or 4-hour intervals)."
  summary: |
    确认"正确标签贴到正确产品"的频率取决于手段：连续扫描器=连续监控；人工
    操作扫描或人工核对=固定间隔（示例 1/2/4 小时），且人工核对至少在生产开始
    时和每次新标签上产线时进行。手段的自动化水平直接兑换为监控频率的放宽，
    例外记录机制（p3-34）与之配套。
  tags: [label-management, barcode, monitoring-frequency, numeric]

- id: p3-48
  title: FDA 未设过敏原阈值上限；阈值数据可由企业科学评估使用
  type: principle
  source_chapter: Ch11 §11.3 / §11.8.3.2
  source_quote: |
    "FDA has not established a maximum amount of food allergen that may be present in
    labeled food products without need for declaration. However, FDA recognizes that
    published data on population threshold dose responses...raise the possibility that some
    low-level exposures...may not cause allergic reactions in most consumers who have that
    food allergy."
  summary: |
    监管现状：无法定"免声明阈值"。企业可用人群阈值剂量响应数据（风险评估等
    科学有效评估）为自身产品做控制决策——特别是咨询声明三选一中的"阈值论证"
    选项（p3-28）。但责任与不确定性由企业承担：评估须写入 FSP、可被检查质询，
    且表 11-4 中检测仅判"是否检出"而非"水平高低"。
  tags: [allergen-threshold, no-maximum, risk-assessment, responsibility]

- id: p3-49
  title: CGMP 措施不受管理组件约束，但可"升格"为预防控制
  type: principle
  source_chapter: Ch11 §11.4.1 / §11.5.1
  source_quote: |
    "Our recommended CGMP measures in Appendix 11-1 to prevent allergen cross-contact are
    not subject to preventive control management components. However, ...you could develop
    and implement appropriate preventive control management components for any CGMP measure
    that you adapt to function as a preventive control."
  summary: |
    附录 11-1 的 CGMP 措施（人员、厂房设计、卫生作业、设备器具、原料、生产
    操作、仓储配送）本身不需要监控/纠正/验证组件；但把任一 CGMP 措施与监控
    或验证（如目视观察）组合后，即升格为预防控制。升级路径示例：清洁作业
    （CGMP）→加监控的过敏原清洁程序（预防控制）；颜色标识→加定期目视验证。
    规则本质：CGMP 是底盘，管理组件是使其成为"控制"的传动装置。
  tags: [cgmp, preventive-control, upgrade-path, allergen]

- id: p3-50
  title: 供应商过敏原现场审计的评估清单
  type: principle
  source_chapter: Ch11 §11.8.3.3（引 GMA 2009）
  source_quote: |
    "examples of activities to evaluate during the audit are: - Storage and handling
    practices...; - Methods used for physical separation, product containment, and product
    identification; - Production practices, including procedures for use of rework and WIP;
    - Production scheduling; - Movement of raw materials...; - Use and segregation of
    specific utensils...; - Procedures for the approval of labels...; - ...Sanitation
    procedures; - Post-cleaning verification...; and - Review of records..."
  summary: |
    对 117 管辖供应商的过敏原审计评估面：储存与搬运、物理隔离/产品容纳/标识
    方法、生产实践（含返工与 WIP）、排产、过敏原物料流转、专用器具与隔离、
    标签与含印刷标签包装的批准程序、正确标签应用保障、过时标签处置、卫生
    程序、清洁后验证、监控程序、记录审查（含既往审计报告与整改闭环）。
    审计员须为 qualified auditor 且具备过敏原技术专长。
  tags: [supplier-audit, checklist, allergen, qualified-auditor]

- id: p3-51
  title: 供应商不合规的处置分级：correction vs corrective action vs 换供应商
  type: principle
  source_chapter: Ch11 §11.8.5 / §11.8.6
  source_quote: |
    "Corrections could be appropriate if...a supplier has an implementation issue with
    certain allergen controls...but the observations indicate that cross-contact was
    unlikely. ... Corrective actions (rather than corrections) are appropriate when the
    problem with a supplier's control of food allergen hazards impacts (or has the potential
    to impact) the safety of your product."
  summary: |
    供应商问题处置三级：①影响未及产品的执行性问题→correction（评估供应商
    解释与防复发步骤）；②影响或可能影响自己产品安全（如供应商因非预期大豆
    召回乳粉）→corrective action（查明供应商失败原因、协同整改或换供应商、
    评估并扣留所有受影响食品）；③持续不合规→再分析，PCQI 决定是否停用该
    供应商。检测或消费者投诉也是发现渠道。
  tags: [supplier-nonconformance, correction, escalation, supply-chain]

- id: p3-52
  title: 供应链记录须由 PCQI 在创建后合理时间内审查
  type: principle
  source_chapter: Ch11 §11.8.8（21 CFR 117.475(b)）
  source_quote: |
    "you must review the records for your supply-chain program in accordance with
    §117.165(a)(4), which requires that a PCQI review (or oversee the review of) your
    supply-chain records within a reasonable time after the records were created to ensure
    that the records are complete, the activities reflected in the records occurred in
    accordance with the food safety plan..."
  summary: |
    供应链程序记录（供应商批准、验证活动、审计报告等）须由 PCQI 审查或监督
    审查，时限为"记录创建后的合理时间"（与 Ch6 的 7 天惯例一致），审查目的
    四项：记录完整、活动符合 FSP、预防控制有效、纠正决策恰当。供应链记录
    的完整性要求与工艺控制记录相同——外包的控制不豁免审查义务。
  tags: [records-review, pcqi, supply-chain, timeline-rule]

- id: p3-53
  title: 均匀性决定抽样与声明策略：液体均质 vs 坚果非均质
  type: principle
  source_chapter: Ch11 §11.8.2 / §11.8.3.2 脚注
  source_quote: |
    "whether the allergen cross-contact is likely to be extensive (such as when an allergen
    present due to cross-contact could be distributed homogeneously in the product) or
    limited (such as when an allergen present due to cross-contact is more likely to be
    distributed non-homogeneously)."
  summary: |
    过敏原在原料中的分布形态决定供应链程序的深度与检测设计：液体产品中的
    交叉接触过敏原趋于均匀分布（牛奶/豆奶），检出概率高、风险面广；坚果碎块
    等非均质分布则检出概率低但局部浓度高。抽样计划、测试频率、咨询声明
    传递决策都要先回答"分布是否均匀"这一问题。
  tags: [homogeneity, sampling, allergen, design-factor]

- id: p3-54
  title: 供应商自身 PCQI 的书面论证是高交叉接触风险的标志信号
  type: principle
  source_chapter: Ch11 §11.8.3.2（表 11-4 高风险行）
  source_quote: |
    "The supplier's PCQI provides a written justification, in the supplier's food safety
    plan, for why allergen cross-contact controls are not always able to ensure protection
    of food from allergen cross-contact... Because the supplier provides allergen advisory
    statements, the supplier does not routinely do verification testing..."
  summary: |
    表 11-4 的判定模式：供应商出咨询声明=其自身 PCQI 已书面承认控制有极限
    （验证测试周期性阳性、清洁不总是有效）。此时接收方若要在自己产品上不传递
    声明，须测试多批次掌握频率与水平数据；若传递声明，则按含过敏原原料管理。
    供应商的声明行为本身是接收方风险评估的输入信号。
  tags: [supplier-signal, advisory-statement, table-11-4, risk-assessment]

- id: p3-55
  title: 货架期操作限视同关键限（酸化食品的从严原则）
  type: principle
  source_chapter: Ch6 §6.16.2
  source_quote: |
    "Because Salsa Processor A needs to make a shelf-stable food, Salsa Processor A treats
    the operating limits established for shelf-stability as if they were the critical limits
    established for food safety."
  summary: |
    当操作限承载的不仅是质量而是货架期稳定性（商业可储性）时，应将其按关键限
    的严格程度管理——因为货架期失效（腐败孢子菌生长、pH 反升）会间接制造
    安全风险（肉毒萌发）。规则：操作限与关键限的区分以"失效后果是否最终
    触及安全"为准，而非以参数名义用途为准。
  tags: [shelf-stability, operating-limit, acidified-food, strictness-rule]
```

## 本段覆盖说明

- **Ch6 后半**（§6.9–6.16 + 附录 6-A~E）：p3-01 至 p3-23（纠正措施四目标、验证五类活动、记录要求、7 天审查、EPIPT、目标菌选择、各数值关键限、15 批升级规则、年度校准、偏差三角色分工）。
- **Ch11 前半**（§11.1–11.9）：p3-24 至 p3-55（过敏原免 validation、咨询声明不替代 CGMP、SAHCODH 年审、检测仅补充、exception record、监控/验证命名灵活性、错标=错标、cleanup-to-cleanup、再分析触发、供应商批准与审计）。
- **反复出现判断（仅限本段）**：纠正式 vs 纠正措施边界（p3-36/37/51）在本段出现 3+ 次；"监测/验证可互换"（p3-35）出现 3 次（§11.5.2.3、§11.6.1.1、§11.7.2）；咨询声明禁替代 CGMP（p3-25）出现 4 次（§11.1、§11.4.3、§11.8.3.1、§11.9.1）；偏差三角色分工（p3-21）在全部 5 个示例厂重复。
- 注意：监控频次的通则（§6.8"监控频率须保证控制持续实施"）主体位于上一分块（6601 行之前），本段仅见其尾部；相关内容以示例形式落在 p3-19、p3-47。
