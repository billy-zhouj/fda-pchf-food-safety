# FDA PCHF 指南 · 反例提取（阶段 1 / counter-example extractor）

> 来源：books/fda-pchf-human-food-guidance/source.md（19461 行）
> 方法：检索式取块 —— 先读阶段 0 笔记 notes-1~6 的"警告/常见错误"章节，再以警告信号词 Grep 原文定位并逐条核验摘录原句。
> 说明：不做筛选（宁错杀）；所有 source_quote 均为原文逐字摘录（≤100 英文单词）并回原文核验。

```yaml
- id: x01
  title: 危害分析做错则整个 FSP 无效
  type: counter-example
  source_chapter: Ch2.2 Conducting a Hazard Analysis (约 L2089-2092)
  source_quote: |
    "If you do not conduct the hazard analysis correctly, and do not identify all hazards
     warranting preventive controls within the food safety plan, the food safety plan will not
     be effective in protecting consumers and preventing food safety issues, no matter how well
     your facility follows the plan."
  summary: |
    错误做法：认为只要工厂把计划执行到位，FSP 就算合格；把危害分析当作走形式的表格填写。
    为什么错：危害分析是全体系的支点，漏识别需控危害则后续所有监控/纠正/验证都建立在错误前提上，
    执行得再好也无法保护消费者。
    正确做法：投入足够的专业判断、原料/工艺知识，必要时引入外部专家，把危害分析当成最核心的
    质量环节对待，并对"Yes/No"判定留有可辩护的书面理由。
  tags: [counter-example, hazard-analysis, food-safety-plan, foundation]

- id: x02
  title: 工艺流程图不现场核实导致漏步骤
  type: counter-example
  source_chapter: Ch2.3.1 Recommended Activities Prior to Conducting a Hazard Analysis (约 L2145)
  source_quote: |
    "You should verify the process flow diagram onsite in order to ensure no steps have been
     overlooked."
  summary: |
    错误做法：坐在办公室里凭记忆或旧文件画流程图，直接进入危害分析。
    为什么错：流程图上漏掉的每个步骤（回掺、暂存、室温暴露）都是危害分析盲区，
    后续所有评估都绕过这段真实工艺。
    正确做法：绘制后到现场逐段核实（含设备、收货与储存步骤），确认无遗漏步骤后再开展识别与评估。
  tags: [counter-example, hazard-analysis, flow-diagram, verification]

- id: x03
  title: 只解释"Yes"不解释"No"
  type: counter-example
  source_chapter: Ch2.3.2 六列工作表 · 列 4 (约 L2168-2175)
  source_quote: |
    "Explaining your reasons for a “No” conclusion can be just as important as explaining your
     reasons for a “Yes” conclusion."
  summary: |
    错误做法：危害分析工作表上对判定为"需要控制"的危害写满理由，对判定"No"的危害留空或一笔带过。
    为什么错："No"的书面理由是应对检查员/审核员质疑的直接证据；空白的"No"在检查中等于没有评估过，
    会被要求重新论证甚至被认定 FSP 不完整。
    正确做法：对每个"No"写明判定依据；对有争议的危害可保守地列入第 2 列并解释"No"，
    便于自查和在检查时快速给出答案。
  tags: [counter-example, hazard-analysis, documentation, inspection]

- id: x04
  title: 以为热处理能消除已形成的毒素
  type: counter-example
  source_chapter: Ch5.2 Table 5-1 预防控制适用性矩阵 (约 L5867)
  source_quote: |
    "ProcessControl –LethalTreatments | Heat (e.g.,cooking,roasting,baking) | ... Will not eliminate
     preformed toxins of S. aureus and B. cereus emetic toxin"
  summary: |
    错误做法：温度滥用的蛋奶派等食品在后续工序里"再加热一下就安全了"；把致死步骤当作万能补救。
    为什么错：S. aureus 肠毒素和 B. cereus 催吐毒素一旦在温度滥用阶段形成，常规热处理无法破坏，
    吃下去照样中毒（毒素起效可快至 30 分钟）。
    正确做法：把温度滥用视为不可逆问题——重点是预防生长产毒（时间/温度控制），而非事后热处理；
    已滥用的产品应评估后销毁或转安全用途。
  tags: [counter-example, heat-treatment, toxin, S-aureus, B-cereus]

- id: x05
  title: 冷却失控——产品降到 140°F 以下孢子即萌发
  type: counter-example
  source_chapter: Ch3.3.4.2.2 热处理后冷却不当 (约 L3089-3092)
  source_quote: |
    "it is spores that survive the cooking process if they are present, and they begin to germinate
     when the product temperature begins to drop below 140°F."
  summary: |
    错误做法：以为"煮熟了"就万事大吉，热食品在室温下慢慢放凉、大锅深盆久置。
    为什么错：烹调杀不死孢子；产品一降到 140°F 以下孢子就开始萌发，且竞争菌已被杀灭、孢子反而
    长得更快；非蛋白水解 C. botulinum 和部分 B. cereus 甚至能在冷藏温度缓慢萌发。
    正确做法：执行两段式快速冷却（135→70°F 2 小时内、再 4 小时内降到 41°F），用冷却隧道、
    冰水翻滚槽等加速冷却，并把冷却本身当作受控的关键工序。
  tags: [counter-example, cooling, spores, C-perfringens, C-botulinum]

- id: x06
  title: ROP 包装"先产毒后腐败"——无感官警讯
  type: counter-example
  source_chapter: Ch3.3.4.2.4 减氧包装 (约 L3158-3163)
  source_quote: |
    "Lower oxygen levels favor pathogens that can grow in the absence of oxygen over the aerobic
     spoilage organisms that require oxygen for growth. For this reason, you may get toxin
     production before you get spoilage - something that is less likely to happen in traditional
     packaging."
  summary: |
    错误做法：把 ROP（真空/气调包装）单纯当作延长货架期的质量手段，沿用"闻着没坏就能吃"的传统判断。
    为什么错：低氧环境抑制的是需要氧气的好氧腐败菌，却偏爱厌氧病原菌——肉毒毒素可能在产品
    看起来、闻起来完全正常时已经产生，消费者没有任何感官预警。
    正确做法：使用 ROP 前必须确认存在 C. botulinum 屏障之一（aw<0.93、pH<4.6、盐>10%、
    最终容器内热处理、冷冻储运），并把 ROP 纳入危害分析。
  tags: [counter-example, packaging, ROP, C-botulinum, sensory-limitation]

- id: x07
  title: 把冷藏温度当作 ROP 的唯一屏障
  type: counter-example
  source_chapter: Ch3.3.4.2.4 减氧包装 (约 L3170-3172)
  source_quote: |
    "Refrigeration below 38°F (3.33°C) can prevent growth of all strains of C. botulinum, but
     because temperatures above this are commonly employed for refrigeration, temperature should
     not be relied on as the only control."
  summary: |
    错误做法：以为产品"一直是冷藏的"就敢上 ROP，把温度当成唯一的肉毒屏障。
    为什么错：38°F/3.33°C 以下才能抑制所有肉毒菌株，而常规冷藏温度普遍高于此值；
    冷链一旦短暂断裂，屏障即告失效且无法察觉。
    正确做法：以 aw/pH/盐分/容器内热处理/冷冻储运等结构性屏障为主，温度只作为辅助手段，
    屏障可组合协同但不可单靠温度。
  tags: [counter-example, ROP, temperature-control, single-point-of-failure]

- id: x08
  title: 多组分界面——各组分单独达标不等于组合达标（泡芙）
  type: counter-example
  source_chapter: Ch3.3.4.2.3 配方控制不当 (约 L3126-3133)
  source_quote: |
    "Layering product components of significantly different pH or a w values alters the
     microenvironments at the interfaces of the components. A simple example is an éclair filled
     with a cream filling. The pH and a w at the interface of the pastry and the filling will be
     affected by the difference..."
  summary: |
    错误做法：按各组分的 pH/aw 查表分别判定安全，就认为整支奶油泡芙安全。
    为什么错：酥皮（高 pH 低 aw）与奶油馅（低 pH 高水分）的界面会形成与任一组分都不同的
    微环境，可能恰好利于微生物生长——填馅里的菌不长，界面上的菌却长。
    正确做法：配方控制要评估组分组合后的界面微环境与成品平衡 pH/aw，必要时加酸化或防腐措施。
  tags: [counter-example, formulation, multi-component, interface, aw]

- id: x09
  title: 顶部装饰改变鹰嘴豆泥的界面微环境
  type: counter-example
  source_chapter: Ch3.3.4.2.3 配方控制不当 (约 L3139-3144)
  source_quote: |
    "If a topping of pine nuts, or oil, or diced red peppers is added to the top in the container
     as “decoration” then those additions could then significantly change the microenvironment at
     the [interfaces]."
  summary: |
    错误做法： homogeneous 混合的鹰嘴豆泥做过平衡 pH 评估后，随手加松子、油、红椒丁做装饰，
    不再重新做危害分析。
    为什么错：装饰物会局部改变顶部界面的 pH/aw 微环境，可能需要额外的酸化控制；
    均质平衡值无法代表界面处的真实条件。
    正确做法：任何后添加的配料/装饰都要作为配方变更重新评估，必要时酸化该装饰层或改设计。
  tags: [counter-example, formulation, rework, hazard-analysis, design-change]

- id: x10
  title: 孢子能在冷藏温度萌发生长——"冷藏了就不长菌"是错觉
  type: counter-example
  source_chapter: Ch3.3.4.2.2 / Ch4.3.2.1 (约 L3091-3092)
  source_quote: |
    "Some spores such as those from pathogens such as non-proteolytic C. botulinum and some
     strains of B. cereus have the ability to germinate and grow at refrigeration temperatures,
     although long times are required."
  summary: |
    错误做法：把"放冰箱"当成终点性安全措施，用延长冷藏货架期来代替真正的杀灭或抑制控制。
    为什么错：非蛋白水解 C. botulinum 与部分 B. cereus 菌株可在冷藏温度萌发生长（需时长但仍会到达），
    长货架期冷藏 RTE 产品由此积累风险。
    正确做法：对长货架期冷藏产品，把非蛋白水解 C. botulinum 列入目标菌评估（参考 Table 3-B
    的各温度累计暴露时限），配合配方/热处理屏障而非只靠冷链。
  tags: [counter-example, refrigeration, spores, shelf-life, C-botulinum]

- id: x11
  title: 冷藏挡不住李斯特菌——近冰点也能生长
  type: counter-example
  source_chapter: Ch4.3.2.1 Use of Refrigeration as a Time-Temperature Process Control (约 L4876-4878)
  source_quote: |
    "Refrigeration works well for controlling the growth of most pathogenic bacteria. However,
     some pathogens, like L. monocytogenes and Yersinia enterocolitica, can grow at temperatures
     close to freezing."
  summary: |
    错误做法：认为"全程冷链=安全"，对冷藏 RTE 食品不再评估环境病原风险。
    为什么错：L. monocytogenes（最低生长温度约 -0.4°C）和 Y. enterocolitica 在接近冰点的温度
    仍能生长，冷链只是延缓而非阻止；冷藏 RTE 食品恰是李斯特菌暴发的高发品类。
    正确做法：对暴露于环境的 RTE 产品，环境病原评估是强制项（117.130(c)(1)(ii)），
    需靠卫生控制+环境监测+货架期设计综合控制，冷链只是其中一环。
  tags: [counter-example, refrigeration, Listeria, RTE, false-sense-of-security]

- id: x12
  title: 冷冻不能消灭病原
  type: counter-example
  source_chapter: Ch4.3.2.2 Use of Freezing (约 L4992-4995)
  source_quote: |
    "Foods are microbiologically stable when held at temperatures below 17.6 [o]F (-8 [o]C)...
     Most viruses, bacterial spores, and some bacterial vegetative cells survive freezing
     unchanged."
  summary: |
    错误做法：把"冻起来"当成杀菌手段，认为冷冻产品无需再做病原控制。
    为什么错：冷冻只是让微生物休眠（微生物学稳定），多数病毒、孢子甚至部分营养细胞解冻后
    活力不变；冷冻产品一旦解冻滥用，风险原样重现。
    正确做法：冷冻只作为时间/温度控制的一种储存形式，病原的杀灭仍要靠致死性处理；
    解冻环节也要纳入时间/温度控制。
  tags: [counter-example, freezing, spores, time-temperature]

- id: x13
  title: "4 小时危险区规则"只是经验法则
  type: counter-example
  source_chapter: Ch4.3.2.1 Time/Temperature (约 L4903-4911)
  source_quote: |
    "Traditionally, the rule of thumb for foods that will support microbial growth has been no
     more than 4 hours in the danger zone... Therefore, the actual maximum time that a product
     may be safely held in the danger zone depends on a number of factors... rather than relying
     on the 4-hour rule of thumb."
  summary: |
    错误做法：把"危险区不超过 4 小时"当成普适安全红线写进程序或用于辩护。
    为什么错：不同病原生长速率不同、食品支持生长的能力不同，4 小时既可能过于宽松
    （如高浓度 S. aureus 场景）也可能过于保守；FDA 明确提示不要依赖这条经验法则。
    正确做法：按具体病原与食品特性查 Food Code 与附录 3 Table 3-B，或用自己产品的实测研究
    设定时间/温度限值；检查员同样按这些因素评估温度滥用 significance。
  tags: [counter-example, time-temperature, rule-of-thumb, danger-zone]

- id: x14
  title: 水浴冷却时封口缺陷吸入污染冷却水
  type: counter-example
  source_chapter: Ch3.3.4.4 容器完整性缺失 (约 L3194-3200)
  source_quote: |
    "The primary causes of recontamination of foods after a process control step and packaging
     are defective container closures and contaminated cooling water... As the product cools, a
     vacuum is drawn in the container. Contaminated cooling water can enter through the container
     closure, especially if the closure is defective."
  summary: |
    错误做法：热处理+热灌装后认为"已经杀菌"，不再关注封口质量与冷却水卫生。
    为什么错：产品冷却时容器内形成真空，会把冷却水经缺陷封口吸入容器——致死步骤之后
    的再污染直接引入 C. botulinum、L. mono 等病原。
    正确做法：把封口完整性作为预防控制监控（酸化食品法规 114.80(a)(4) 即此要求），
    保持冷却水卫生，封口检测频次足以确保容器密封有效。
  tags: [counter-example, container-integrity, cooling-water, recontamination, acidified-foods]

- id: x15
  title: 大颗粒食品的平衡 pH 需要数天——不冷藏就有肉毒风险
  type: counter-example
  source_chapter: Ch4.3.3.2 Acidity (pH) (约 L5190-5193)
  source_quote: |
    "An equilibrium pH is achieved when a natural pH balance has been reached by all ingredients
     - which can take several days in foods with very large particulates... You should refrigerate
     products that require several days to reach equilibrium pH to prevent the growth of
     C. botulinum or other pathogens."
  summary: |
    错误做法：酸化大颗粒食品（如整根腌菜、大块蔬菜）时，测得表面/液相 pH≤4.6 就判定安全并常温存放。
    为什么错：颗粒内部达到平衡 pH 可能需要数天，期间颗粒中心仍是低酸环境，肉毒梭菌可生长产毒。
    正确做法：平衡 pH 达成前对产品实施冷藏；或减小颗粒尺寸（如 Salsa A 厂的 ≤1.0 cm 关键限值）
    使颗粒与液体同步达标，并将颗粒尺寸设为关键限值。
  tags: [counter-example, acidification, equilibrium-pH, particulate, C-botulinum]

- id: x16
  title: 腐败菌抬升 pH——"只是坏了"可能致命
  type: counter-example
  source_chapter: Ch4.3.3.2 Acidity (约 L5202-5206)
  source_quote: |
    "Acidified foods must be treated sufficiently to control spoilage microorganisms in addition
     to vegetative pathogens... the food safety reason is that the action of the spoilage
     organisms can raise the pH, compromising the safety of the product because any spores of
     C. botulinum that are in the food can germinate, grow, and produce botulinum toxin."
  summary: |
    错误做法：认为杀灭致病菌（营养细胞）就够了，腐败菌"顶多让产品变质报废"，不值得专门热处理控制。
    为什么错：腐败产酸菌在酸性环境里生长会使 pH 回升突破 4.6，反过来解锁肉毒孢子的萌发产毒——
    质量问题被放大为安全致命问题。
    正确做法：酸化食品的热处理必须同时控制腐败菌（这正是 200°F/2min 货架期限值作为操作限
    存在的原因），或用许可防腐剂替代。
  tags: [counter-example, acidified-foods, spoilage, pH-shift, C-botulinum]

- id: x17
  title: 加酸只能抑菌不能杀菌
  type: counter-example
  source_chapter: Ch5.2 Table 5-1 酸化行 (约 L5883)
  source_quote: |
    "you cannot rely on added acid to eliminate vegetative cells of bacterial pathogens";
    "E. coli O157:H7 可在酸性条件下长期存活"（Ch4.3.3.2）
  summary: |
    错误做法：以为产品够酸（pH 低）就不需要热处理，把 pH 当成杀灭步骤。
    为什么错：降 pH 主要是抑制生长而非杀灭；E. coli O157:H7 等可在酸性环境长期存活，
    一旦后续条件变化（如进入高 aw 界面）即可恢复风险。
    正确做法：酸化作为非致死处理（抑制生长）使用；杀灭营养细胞病原仍需致死性处理
    （如 Salsa A 的 158°F/1.5min 5D 工艺）。
  tags: [counter-example, pH, acidification, E-coli-O157, non-lethality]

- id: x18
  title: 常规热处理杀不死孢子
  type: counter-example
  source_chapter: Ch6.2 / Ch5.2 Table 5-1 (约 L5867)
  source_quote: |
    "In general, heat processes will not eliminate spores of bacterial pathogens";
    "The doses approved in the U.S. will not eliminate spores of bacterial pathogens in most
     foods"（辐照行）
  summary: |
    错误做法：做完普通烘焙/烹调后认定孢子形成菌（C. botulinum、C. perfringens、B. cereus）
    已被消灭，不再做孢子萌发控制。
    为什么错：商业级常压热处理只能杀营养细胞，灭活孢子需要加压高温；
    孢子在冷却与储存阶段萌发的风险始终存在（见 x05、x10）。
    正确做法：识别产品中孢子形成菌危害后，用 pH/aw/盐/冷藏等抑制萌发的屏障组合来控制，
    而非指望热处理一步到位。
  tags: [counter-example, heat-treatment, spores, lethality-limit]

- id: x19
  title: 常规清洁对定殖菌（resident strain）无效
  type: counter-example
  source_chapter: Ch3.3.5.2 Transient vs. resident (约 L3301-3308)
  source_quote: |
    "while common cleaning and sanitation practices are adequate to control the presence of
     transient contaminants, such practices do not control the presence of resident contaminants
     once they have become established... The facility will need to use intensified sanitation
     procedures to eliminate the contamination."
  summary: |
    错误做法：环境监测反复检出同一菌株时，仍按常规 SSOP 加班多做几遍清洁消毒了事。
    为什么错：病原一旦在设备接缝、裂纹、死角等藏匿点定殖（Salmonella 与 L. mono 定殖史最长），
    可持续数月甚至数年，藏匿点庇护其逃过常规清洁——重复常规手段只是自我安慰。
    正确做法：识别 resident strain 后启动强化卫生程序（拆解清洁、寻找根除藏匿点），
    这也是环境监测被法定化为卫生控制组件的原因。
  tags: [counter-example, sanitation, resident-strain, EMP, niche]

- id: x20
  title: 高压水枪清洁反而散播李斯特菌
  type: counter-example
  source_chapter: Ch3.3.5.3.1 Wet process environments (约 L3361-3363)
  source_quote: |
    "L. monocytogenes does not spread alone through the air; however, in wet environments,
     aerosols from high pressure water hoses used during cleaning operations help spread
     L. monocytogenes throughout the environment and from one surface (e.g., floors) to another
     surface (e.g., food contact surfaces)."
  summary: |
    错误做法：卫生班组为追求"冲得干净"加大水压，把高压水枪当万能清洁工具。
    为什么错：高压水产生的气溶胶会把地面的李斯特菌扬起并播散到输送带、台面等食品接触面——
    清洁动作本身成了污染传播途径。
    正确做法：湿区清洁用低压水管，控制积水与气溶胶；湿环境防李斯特菌的根本策略是尽量保持干燥。
  tags: [counter-example, sanitation, aerosol, Listeria, wet-environment]

- id: x21
  title: 金属检测器的取向与干扰盲区
  type: counter-example
  source_chapter: Ch4.3.8.1 Exclusion Strategies – Metal (约 L5351-5358)
  source_quote: |
    "The use of electronic metal detectors is complex, especially with regard to stainless steel,
     which is difficult to detect. The orientation of the metal object in the food affects the
     ability of the equipment to detect it. For example, if a detector is not properly calibrated
     and is set to detect a sphere 0.08 inch (2 mm) in diameter, it may fail to detect a
     stainless steel wire that is smaller in diameter but up to 0.9 inch (24 mm) long."
  summary: |
    错误做法：用 2mm 球试块校准一次就认为金属检测器"全覆盖"，且只靠这一道防线。
    为什么错：不锈钢难检出；检出能力随金属物取向变化——校准为 2mm 球的检测器可能漏掉
    更细但长 24mm 的钢丝；环境湿度与产品酸度还会产生干扰信号掩盖金属信号。
    正确做法：校准试块须覆盖线形/异形金属的最坏取向，定期校准并考虑产品效应；
    复杂设备（部件多且不可见）不适合目视检查，应搭配 X 光机或预防性维护（定期检查易损部件）。
  tags: [counter-example, physical-hazard, metal-detection, calibration, false-negative]

- id: x22
  title: ATP/蛋白拭子阴性≠特定过敏原已清除
  type: counter-example
  source_chapter: Ch11.6.1.1 脚注 21 (约 L8907-8911)
  source_quote: |
    "ATP tests are considered “non-specific” tests for cleanliness because ATP is found in all
     living cells and its presence could reflect diverse sources such as food, microorganisms,
     or even human skin. ATP tests and other “non-specific” tests... have the potential to be
     more sensitive than visual observation but may not be sensitive enough to detect levels of
     a particular allergenic protein."
  summary: |
    错误做法：换产后用 ATP 拭子测出阴性，就宣布产线对牛奶/花生等特定过敏原"清洁合格"并开产。
    为什么错：ATP 是非特异检测，来源可以是任何活细胞（食品、微生物甚至人的皮肤）；
    其灵敏度可能达不到特定致敏蛋白的关心水平——阴性不等于该过敏原不存在。
    正确做法：ATP 只能作为清洁步骤的快速筛查工具；对特定过敏原的验证应使用过敏原特异性
    检测盒（FCS 拭子或 CIP 末次冲洗水）、push-through 物料或首件产品检测。
  tags: [counter-example, allergen, cleaning-validation, ATP, test-limitation]

- id: x23
  title: 把反复性问题当"correction"轻处理
  type: counter-example
  source_chapter: Ch5.5.3 / 11.5.3 correction vs corrective action (约 L8697-8700)
  source_quote: |
    "you do not need to take corrective actions if you take action, in a timely manner, to
     identify and correct a minor and isolated problem that [does not directly affect product
     safety]."
  summary: |
    错误做法：预检发现标签错误、CIP 温度不达标等问题时，每次都"改一下、重跑一遍"了事，
    不区分孤立问题与反复问题。
    为什么错：correction 的法定适用边界是"轻微+孤立+未影响产品"；反复出现说明程序本身无效，
    已触发纠正措施四步程序与再分析义务，继续轻处理会积累成系统性失效。
    正确做法：判定以"问题是否已影响食品"+"孤立还是反复"为界；影响过食品的走纠正措施
    （查根因→防复发→评估受影响食品→阻止入市/召回），反复问题触发 FSP 再分析。
  tags: [counter-example, correction, corrective-action, recurring-problem, reanalysis]

- id: x24
  title: 受影响批次只算"检出后"的
  type: counter-example
  source_chapter: Ch11.6.1.2 过敏原清洁的纠正措施 (约 L8915-8916)
  source_quote: |
    "In determining which food is affected, we recommend that you consider all food lots
     produced from cleanup to cleanup."
  summary: |
    错误做法：换产清洁后检出过敏原阳性，只隔离"检出之后"生产的产品。
    为什么错：检出点只说明"现在脏"，污染可能始于上次清洁之后的第一批；
    少算批次意味着受污染产品继续在市。
    正确做法：把"从上次清洁到本次检出之间生产的所有批次"都视为可能受影响，
    逐一评估安全性并阻止未受控产品入市（已入市则召回）。
  tags: [counter-example, allergen, batch-tracing, corrective-action]

- id: x25
  title: 发现偏差只处理"当下这一刻"的产品
  type: counter-example
  source_chapter: Ch5.5.2 Monitoring (约 L6033-6036)
  source_quote: |
    "If a measurement shows that a deviation from the control value has occurred, you should
     assume that the control value had not been met since the last check in which the value was
     acceptable. As a result, the greater the time span between measurements, the more products
     you are putting at risk."
  summary: |
    错误做法：连续温度记录显示当前超标，只把"正在加工的这锅"隔离处理。
    为什么错：测得偏差的那一刻无法知道失控从何时开始——推定自上次合格检查起全部未受控；
    监控间隔越长，风险敞口越大。
    正确做法：以"自上次合格读数起"为界圈定受影响产品并全部评估处置；
    这也是连续监控+至少每日回查记录被推荐的原因。
  tags: [counter-example, monitoring, deviation, product-hold]

- id: x26
  title: 校准频次太低——失准时风险敞口巨大
  type: counter-example
  source_chapter: Ch5.5.4 Verification (约 L6153-6157)
  source_quote: |
    "When calibration or an accuracy check of a preventive control monitoring instrument shows
     that the instrument is not accurate, you should evaluate the monitoring records since the
     last instrument calibration... food safety plans with infrequent calibration or accuracy
     checks can place more products at risk than those with more frequent checks."
  summary: |
    错误做法：为省事把温度计/记录仪校准拉长到一年一次以上，认为"设备看着正常就行"。
    为什么错：一旦发现失准，必须回溯评估上次校准以来的全部监控记录——校准间隔越长，
    存疑产品越多，处置成本和召回风险呈比例放大。
    正确做法：按仪器漂移特性设定合理校准/精度核查频次（如 Soup A 每日核查、每年 NIST 对照校准），
    并保留可回溯的校准日志。
  tags: [counter-example, calibration, verification, risk-exposure]

- id: x27
  title: "May contain"过敏原声明不是护身符
  type: counter-example
  source_chapter: Ch11.1 / 11.9.1 Allergen Advisory Statements (约 L8234-8239)
  source_quote: |
    "we advised that labeling such as “may contain [allergen]” is not a substitute for, and
     should not be used in lieu of, adherence to CGMPs. Our allergen labeling guidance also
     advises that labeling such as “may contain [allergen]” is not a substitute for adherence to
     food allergen preventive controls and that any such statement must be truthful and not
     misleading."
  summary: |
    错误做法：清洁和交叉接触控制做不彻底，就在标签上印"may contain milk"当作免责声明；
    采购时看到供应商带声明就照单全收。
    为什么错：FDA 明确声明不能替代 CGMP 与过敏原预防控制；虚假或误导性声明本身违规；
    放过带声明的供应商等于把交叉风险采购进门。
    正确做法：使用声明需 PCQI 在 FSP 中书面论证"为何交叉接触控制仍不能确保保护"；
    批准供应商前核实其声明未替代控制，并对是否传递声明做三选一书面决定。
  tags: [counter-example, allergen, advisory-statement, labeling, supply-chain]

- id: x28
  title: 供应商自我验证不能算数
  type: counter-example
  source_chapter: Ch15.8.3 (21 CFR 117.415(b)) (约 L14883-14893)
  source_quote: |
    "Section 117.415(b) specifies that a receiving facility may not accept any of the following
     as a supplier verification activity from its supplier: A determination by its supplier of
     the appropriate supplier verification activities for that supplier...; An audit conducted by
     its supplier of that supplier...; A review by its supplier of that supplier's own relevant
     food safety records."
  summary: |
    错误做法：供应商递交一份"我们自查合格"的报告或自行安排的记录审查，买方就归档当作验证证据。
    为什么错：法规明令不得接受供应商自行决定验证活动、自审、审查自己记录等任何自我验证——
    既当运动员又当裁判无法提供独立性保证。
    正确做法：验证活动由收货设施（或其委托的合格第三方）确定并执行；
    供应商能提供的只有 COA 抽样检测和由 qualified auditor 实施的第三方审核。
  tags: [counter-example, supply-chain, self-audit, conflict-of-interest, verification]

- id: x29
  title: 把经纪商/分销商当作"供应商"来批准
  type: counter-example
  source_chapter: Ch15.8.1 Responsibilities of the Receiving Facility (约 L14833-14839)
  source_quote: |
    "the definition of “supplier” in part 117 means that a broker or distributor is not a
     supplier; the supplier is the establishment that manufactures/processes the food...
     Thus, if you buy raw materials or other ingredients from a broker or distributor, you should
     ask the broker or distributor to provide you with information that allows you to approve the
     establishment that manufactures/processes the food."
  summary: |
    错误做法：只对贸易公司/分销商做问卷和审核就批准"供应商"，从未触达真正的制造/种植企业。
    为什么错：法规意义上的供应商是实际制造/加工/饲养/种植者；经纪商不控制任何危害，
    批准它等于验证了一个不实施控制的空壳。
    正确做法：要求经纪商提供实际制造商的信息，批准并验证真正的 Establishment；
    经纪商只能作为代表收货设施开展活动的服务方，且其文档须被收货设施审查评估。
  tags: [counter-example, supply-chain, broker, supplier-approval]

- id: x30
  title: USDA 有机认证检查不能替代现场审核
  type: counter-example
  source_chapter: Ch15.12.3 Substitution of an Inspection for an Audit (约 L15485-15489)
  source_quote: |
    "inspection by USDA to determine whether a farm satisfies the requirements of the produce
     safety regulation could constitute an appropriate inspection that could substitute for an
     audit, but an inspection by USDA to determine whether a farm satisfies the requirements of
     the National Organic Program could not."
  summary: |
    错误做法：供应商持有 USDA Organic 证书，就认为可以免掉供应链年度现场审核。
    为什么错：有机认证检查针对的是 National Organic Program 的合规（农艺/投入品/标识），
    与 FDA 食品安全法规的合规性不是一回事——"适当检查"必须是足够关联 FDA 食品安全法规的检查。
    正确做法：只有针对适用 FDA 食品安全法规（如农产品安全法规）且在应审核日期 1 年内的
    监管检查结果才能替代审核；各类认证证书（有机、GFSI 等）只能作为补充信息。
  tags: [counter-example, supply-chain, onsite-audit, organic-certification, substitution]

- id: x31
  title: 外国政府 HACCP 证书不能直接替代现场审核
  type: counter-example
  source_chapter: Ch15.12.3 (约 L15496-15503)
  source_quote: |
    "We would not accept a HACCP certificate issued by a foreign government as a substitute for
     an onsite audit because HACCP requirements are not identical to the PCHF requirements, and
     it would not be clear as to what basis was used to issue a HACCP certificate."
  summary: |
    错误做法：进口原料时收一张外国政府颁发的 HACCP 证书归档，认定供应链验证已完成。
    为什么错：HACCP 要求与 PCHF 不完全相同，且发证依据不明——证书无法证明 PCHF 层面的
    危害受控（如供应商书面计划及其执行情况）。
    正确做法：现场审核仍须由 qualified auditor 执行并审查供应商书面计划及实施；
    HACCP 证书只能作为免年审/降频审核书面论证的一部分证据。
  tags: [counter-example, supply-chain, HACCP-certificate, foreign-supplier, onsite-audit]

- id: x32
  title: 把抽样检测当唯一验证手段
  type: counter-example
  source_chapter: Ch15.7.2.2 Sampling and testing (约 L14439-14449)
  source_quote: |
    "you should use scientifically-based sampling plans that provide reasonable assurance... and
     that address known limitations of sampling and testing foods as a verification activity.
     For example, your sampling plan should take into consideration whether a hazard is
     homogeneously distributed throughout the lot, and your selection of an analytical method
     should consider whether food components could interfere with the method."
  summary: |
    错误做法：买一批测一批"全阴"就认定供应商合格，省掉现场审核和记录审查。
    为什么错：危害在批次内常呈非均匀分布（如树坚果交叉接触），抽样天然有漏检风险；
    食品基质可能干扰检测方法、灵敏度可能不足以检出低浓度危害。
    正确做法：检测只能作为其他验证活动的补充；抽样方案须考虑分布均匀性、方法灵敏度与
    基质干扰，与现场审核/记录审查组合使用（过敏原验证同理，见 Ch11.8.3.2）。
  tags: [counter-example, supply-chain, sampling, testing-limitation, verification]

- id: x33
  title: EPIPT 超出研究覆盖条件使用
  type: counter-example
  source_chapter: Ch4.3.1.1 EPIPT 三前提 (约 L4656-4671)
  source_quote: |
    "This approach is suitable if you have conducted a scientific study to validate that the
     EPIPT... will provide an appropriate reduction (e.g., 6D) in the numbers of the target
     pathogen in the slowest heating unit or portion of product under the worst set of heating
     conditions... You should use the EPIPT as a monitoring technique only under those conditions
     that were evaluated by the scientific study."
  summary: |
    错误做法：看到别厂用"终点内部温度"简化监控，直接抄来用，不做温度分布/热穿透研究。
    为什么错：EPIPT 只在最慢加热单元、最坏加热条件被研究覆盖时成立；换产品、换颗粒尺寸、
    换装载方式都会使等效性失效，监控通过但产品未达致死率。
    正确做法：使用 EPIPT 前完成三项研究（热分布找冷点、热穿透覆盖最慢加热单元、识别其他
    影响升温速率的关键因素），并把研究覆盖的条件设为监控参数/关键限值。
  tags: [counter-example, heat-treatment, EPIPT, validation, monitoring]

- id: x34
  title: 对时间/温度指导值做线性内插
  type: counter-example
  source_chapter: Appendix 3, Tables 3-A/3-B/3-C 使用说明 (约 L18822-18826)
  source_quote: |
    "Because the nature of bacterial growth is logarithmic, linear interpolation using the time
     and temperature guidance may not be appropriate. Furthermore, the food matrix affects
     bacterial growth (e.g., presence of competing microorganisms, available nutrients,
     growth-restrictive agents)."
  summary: |
    错误做法：查 Table 3-B/3-C 时,温度落在表格两档之间就线性折算允许暴露时间。
    为什么错：细菌生长是对数性质，线性内插可能严重高估安全时限；食品基质（竞争菌群、
    营养、抑制物）还会进一步改变生长行为。
    正确做法：按表格区间就保守档取值；区间之间（如 40–50°F 无默认限值）需基于自身产品
    研究设定关键限值，而非内插。
  tags: [counter-example, time-temperature, interpolation, appendix-3]

- id: x35
  title: 把 Table 3-A 生长极限当设计依据
  type: counter-example
  source_chapter: Appendix 3, Table 3-A 说明 (约 L18814-18816)
  source_quote: |
    "The data shown in Table 3-A are the extreme limits reported among the references cited.
     These values may not apply to your food or processing conditions."
  summary: |
    错误做法：直接拿附录 3 的 aw/pH/温度极值当产品配方的安全边界，不做适用性判断。
    为什么错：这些数值是文献报道的极端值且多来自实验室培养基，未必适用于具体食品基质
    与加工条件；照抄可能在实际产品上失守。
    正确做法：把极值表当作筛查起点，结合自身产品的实测/攻击试验或已确立的科学配方流程
    确定控制参数；对争议场景保守取值。
  tags: [counter-example, appendix-3, growth-limits, data-applicability]

- id: x36
  title: 预测模型（PMP/ComBase）输出直接当关键限值
  type: counter-example
  source_chapter: Appendix 3, Predictive Modeling Programs (约 L18945-18950)
  source_quote: |
    "you should be aware that significant deviations between actual microbiological data in
     specific products and the predictions may occur, including those for the lag phase of
     growth. Therefore, you should validate the time and temperature limits derived from such
     predictive models if growth of pathogens during processing requires a preventive control."
  summary: |
    错误做法：用 PMP/ComBase 跑一组 pH/温度/盐分条件，把模型预测的迟滞期与倍增时间
    直接写成 FSP 的时间/温度限值。
    为什么错：模型是相对风险估计，实际数据可能出现显著偏差（尤其迟滞期）；FDA 不背书也不要求使用。
    正确做法：模型输出只用于初筛和方向判断；凡模型导出的限值用于预防控制，必须经自身产品
    的验证研究确认。
  tags: [counter-example, predictive-model, PMP, ComBase, validation]

- id: x37
  title: 把 FDA 召回公告当"公众警告"完成义务
  type: counter-example
  source_chapter: Ch14.5.2 Notify the Public When Appropriate (约 L13801-13809)
  source_quote: |
    "[Recalls] are not necessarily used to alert the public about the risk or hazard of a product
     under recall... When FDA posts removal or correction information that has been publicized by
     a firm, we do so as a public service and it does not necessarily mean that the situation is
     urgent or that the product presents a serious hazard to health, such that it would be
     considered a “public warning.”"
  summary: |
    错误做法：召回时认为"FDA 官网发了 Enforcement Report/召回页面"就等于履行了公众警告义务。
    为什么错：公众警告专指通过大众/专业媒体发布的紧急健康危害通告，是召回计划中的独立程序；
    FDA 网站转载只是公共服务，不构成也不替代企业义务。
    正确做法：召回计划中写明判定公众警告适当性的标准与发布步骤，并预置示范新闻稿
    （过敏原、李斯特菌、肉毒、沙门氏菌、O157:H7 模板）。
  tags: [counter-example, recall, public-warning, plan-gap]

- id: x38
  title: 照抄附录 1 的 X 标记定控制
  type: counter-example
  source_chapter: Appendix 1, A1.8.2 X 标记适用性 (约 L17570-17596)
  source_quote: |
    "the recommendations of SMEs in the Tables in Appendix 1 may not always apply to all food
     products in that Food Subcategory. For example, a hazard marked with an X could: Be a known
     or reasonably foreseeable (“potential”) hazard only for some products... Only be a... hazard
     when a food ingredient is used in a food that changes its characteristics (e.g., B. cereus
     in cooked (hydrated) rice but not dried rice)."
  summary: |
    错误做法：两个方向都错——照表全抄控制导致过度合规；或反过来以"表上有 X"为由机械堆控制。
    为什么错：X 标记只是 SME 建议评估的起点，可能仅适用于子类内部分产品、特定地理来源或
    特定用途（干米 vs 熟米）；判定责任永远在每家工厂自己的危害分析。
    正确做法：用三种适用性检验（部分产品/地理来源/用途改变特性）逐项判断，并把 Yes/No
    理由写入 Form 2-B 第 4 列。
  tags: [counter-example, appendix-1, x-marker, hazard-analysis, over-compliance]
```
