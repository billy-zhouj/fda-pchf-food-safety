# L.mono 增量候选 B：人员控制、厂房与设备设计（来源标注 chunk id）

> 负责范围：chunk 第 223–955 行（II. Background / III. 适用性分流 / IV. 人员控制 / V. 厂房设计建造与运行 / VI. 设备设计建造与维护）+ 附录 1（ck-bf70888a9266）、附录 2（ck-3a1870594911）、附录 3 标题层（ck-f992414846ca、ck-61dcce305dde、ck-9f84693a19ff、ck-4f7aed8701fb）。
> 未读 sources：books/ 下指南全文、source.md。附录 4（ck-ec83f3e7e46e 起）与附录 5（ck-db5f8a7358e8 起）仅在跨章节提示中点名。
> 说明：本指南为 Draft（2017-01），正文用 "should"（建议），除非明确引用法规条款；引用时须保留这层效力区分。

---

## 一、新知识候选

### nB-01 L. mono 生长的"内在特性"三阈值与"hurdles"组合概念
- 出处: II.B Characteristics of L. monocytogenes；chunk: ck-9e6d4d150cd2
- 原文关键句: "L. monocytogenes does not grow when: The pH of the food is less than or equal to 4.4; The water activity of the food is less than or equal to 0.92; and The food is formulated to contain a combination of factors scientifically demonstrated to be effective in preventing the growth (the 'hurdles' concept)."
- 中文大意: 李斯特菌不生长的三个条件：pH≤4.4、aw≤0.92、或配方含经科学证明有效的组合抑菌因子（hurdles 概念）。三者可单独成立，也可由"内在特性×加工温度×配方"的交互作用实现（例：加醋使 pH≤4.4）。
- 类型: threshold
- 建议归属: 并入 `process-control-validation`（配方屏障参数锚点）
- 为什么是现有技能缺口: 现有工艺卡只给 a_w≤0.85/0.92 与 pH<4.6（法规/酸化管辖口径），**缺 pH≤4.4 这个"李斯特菌专用的更严阈值"**，也缺"hurdles 组合"这一多因子交互概念；更缺 §117.3 的"显著最小化"锚点与"抑制≠杀灭"（防李斯特菌配方不等于杀菌）的区分。

### nB-02 抑制性配方有效性判定基准：货架期内多点取样、重复生长研究 <1 log 增长
- 出处: II.B；chunk: ck-9e6d4d150cd2
- 原文关键句: "A formulation is generally considered to be effective in preventing the growth of L. monocytogenes if replicate growth studies having samples pulled at various time periods throughout product shelf life show less than a one log increase in the number of L. monocytogenes."
- 中文大意: 判定"配方能抑制李斯特菌"的通用基准：重复生长研究、在整个货架期内多个时间点取样、且李斯特菌数量增幅 <1 log。
- 类型: threshold / procedure
- 建议归属: 并入 `process-control-validation`（validation 证据设计）
- 为什么是现有技能缺口: 现有卡给的是"热处理致死度"的 5D/7D 判据，没有给**抑制型（listeristatic）控制**的验证判据——这是李斯特菌控制的特有难点（杀灭易、抑制难判）。1 log 增幅判据可直接用作验证方案里的接受准则。

### nB-03 高风险 RTE 品类清单与"不支持生长但仍被污染"的反直觉品类
- 出处: II.B；chunk: ck-9e6d4d150cd2
- 原文关键句: "Examples of RTE foods that support the growth of L. monocytogenes and that have been found to be contaminated ... are unpasteurized and pasteurized milk, high fat dairy products, soft unripened cheese ..., cooked ready-to-eat crustaceans (shrimp, crab), smoked seafood, deli-type salads, sandwiches, fresh-cut fruits and vegetables, and raw molluscan shellfish. An example of an RTE food that does not support the growth ... but has been found to be contaminated ... is ice cream."
- 中文大意: 支持李斯特菌生长且已被污染的 RTE 品类清单（生/巴氏杀菌乳、高脂乳制品、未成熟软奶酪、加热即食甲壳类、烟熏海鲜、熟食色拉、三明治、鲜切果蔬、生贝类）；冰淇淋**不支持生长**却仍被污染——说明"无增长"不等于"无污染"，不能据此免环境控制。
- 类型: fact
- 建议归属: 并入 `hazard-analysis-method`（Step 1/2 的品类输入）或 `environmental-pathogen-sanitation`（A1 案例素材）
- 为什么是现有技能缺口: 现有卡只有"湿环境→李斯特菌/干环境→沙门氏菌"的粗分类，没有**品类级的风险清单**；尤其"冰淇淋不支持生长但被污染"是纠正"按增长能力免控"这种直觉误判的关键反例。

### nB-04 人员进入 RTE 区的手部/手套/鞋履控制规格（手套不是万能，接触非食品接触面即须换）
- 出处: IV.A Hands, Gloves and Footwear；chunk: ck-7a00d933ac44
- 原文关键句: "When gloves are used, we recommend that: Personnel wash their hands before putting the gloves on; Multi-use gloves be washed and sanitized before use and after the employee touches any non-food-contact surface (non-FCS) ...; Single use gloves be discarded and replaced after an individual touches any non-FCS; and Gloves worn outside areas where RTE foods are processed or exposed (e.g., restrooms) be discarded before returning to the RTE area."
- 中文大意: 四条手套使用规则：戴前洗手；重复使用手套在接触任何非食品接触面（衣物、门把手、设备控制面板、工具）前后都要洗+消毒；一次性手套接触非 FCS 后必须丢弃更换；在 RTE 区外（如洗手间）戴过的手套进入 RTE 区前必须丢弃。手套与鞋履须不透气（impermeable）、完好、易清洁或一次性；**禁止钉齿鞋（cleated footwear）**（除非安全必需），因其会携带厂内外污物颗粒；RTE 区的手套鞋履只在该区使用，不得跨区。
- 类型: rule / procedure
- 建议归属: 并入 `environmental-pathogen-sanitation`（新增"人员控制"工程化小节）或新建 `personnel-hygiene-controls`
- 为什么是现有技能缺口: 现有环境卡完全没有人员控制层。关键增量是**手套本身可成为污染源**这一反直觉点，以及"接触非 FCS 即换手套"的**触发式规则**（而非笼统的"勤换手套"）。

### nB-05 泡脚器/泡沫消毒器 vs 干粉消毒剂：按干湿环境选型 + 防绕过设计 + 失效巡检
- 出处: IV.B Foamers, Footbaths, and Dry Powdered Sanitizers；chunk: ck-aab28bb1de46、ck-68b8e48bdf21
- 原文关键句: "Foamers or footbaths (which are wet) generally are more appropriate in a wet processing environment. A dry powdered sanitizer generally is more appropriate in a dry processing environment to keep the environment dry; in dry processing environments, the absence of water prevents the growth of L. monocytogenes. When using foamers, footbaths, or a dry powdered sanitizer, we recommend you ensure that personnel cannot avoid walking through them and cannot jump over them when entering the RTE area."
- 中文大意: 泡脚器（footbath，低矮平容器或地面凹槽，防滑面，注消毒液）与泡沫器（foamer，地面自动喷雾泡沫消毒，可覆盖人员与推车/叉车）属**湿式**手段，适合湿加工环境；干粉消毒剂适合干加工环境（保持干燥以抑制李斯特菌）。两条工程性要求：①**布局上必须让人无法绕过或跨过**（不能被跳过）；②非自动泡脚器应**定期（如每小时）检查**液位与消毒剂浓度是否达标；泡沫器需维护以保证喷洒量与覆盖面积正确。
- 类型: design-spec / rule / procedure
- 建议归属: 新能力建议 `environmental-engineering-controls`，或并入 `environmental-pathogen-sanitation` 新增"人员/化学屏障"小节
- 为什么是现有技能缺口: 现有卡完全没有化学屏障（chemical barrier）这一物理防线手段，也没有"湿区用湿式屏障、干区用干粉"的**选型判据**（干区用湿泡脚器会被水活化反而助长李斯特菌——这与现有卡"干区严格控水"原则同源但本指南给出具体器材）。"每小时检查"是可直接照做的巡检频次。

### nB-06 衣物/工服规则：分区专用、每日洗涤处置、按任务色码区分
- 出处: IV.C Clothing；chunk: ck-5f03b10a3729
- 原文关键句: "Smocks and uniforms are laundered or disposed of daily; Smocks or uniforms that will be used in areas where RTE foods are processed or exposed are distinguished from those that will be used in other areas (particularly areas where raw foods are processed or exposed) using a mechanism such as color coding; and Smocks or uniforms are distinguished according to the task that the personnel perform (e.g., production or maintenance)."
- 中文大意: RTE 区人员不得穿街服（除非膝部以上被洁净罩衣覆盖）；RTE 区罩衣**只**在指定 RTE 区及相邻前室（vestibule，更衣穿戴区）内穿；进入 RTE 区前换洁净制服；罩衣与工服**每日洗涤或处置**；用**色码**区分 RTE 区用与生区用（尤其生料区）；并按**任务**区分（生产 vs 维修），以肉眼识别受限进入人员。
- 类型: rule
- 建议归属: 新能力建议 `personnel-hygiene-controls`，或并入 `environmental-pathogen-sanitation`
- 为什么是现有技能缺口: 完全缺失。增量点：**"每日洗涤或处置"是频次硬要求**；**按任务色码**是可直接落地的管理设计（用颜色就能在车间里识别谁有 RTE 区受限进入权）；前室（vestibule）概念也缺失。

### nB-07 分隔不切实际时的三条替代措施：动线环境监测 + "c captive shoe" 政策 + 进入顺序管理
- 出处: IV.D Controls on Personnel Associated with Specific Areas；chunk: ck-4b77c257c586（另 ck-82d67cafa4fd 补充"进入间/化学屏障"选项）
- 原文关键句: "When doing so is not practical, we recommend that: Your environmental monitoring program (see section XIII of this guidance) include monitoring of the travel paths and service areas to show when extra cleaning or a procedural modification is needed; You establish a 'captive shoe' policy in which footwear for the RTE area is only worn in that area; and ..."
- 中文大意: 分设更衣室/休息区/cafeteria 不可行时，三条替代路径：①把**人员动线与服务区纳入环境监测**（用 EM 数据决定是否加做清洁或改程序）；②建立 **"c captive shoe"（在厂内固定穿着、不得带出厂区的专用鞋）政策**，RTE 区鞋只在该区穿；③把管控前移为其他措施（区分 RTE 区与生区工服、提供进入间存放 RTE 区工服鞋履、设置化学屏障如泡脚器/泡沫器）。
- 类型: rule / procedure
- 建议归属: 新能力建议 `personnel-hygiene-controls`；跨卡引用 `environmental-pathogen-sanitation` E Step 5（EM）
- 为什么是现有技能缺口: 现有卡的卫生分区 Step 4 只要求"分区图有人流/物流/气流方向"，没有给出**当物理隔断做不到时怎么办**（这是绝大多数老厂的真实约束）；"动线纳入 EM 采样范围"是把环境监测从设备点位扩展到人员路径的实用设计。

### nB-08 维修/卫生人员与废弃物接触人员：同标准、专用工具、接触废弃物后须四项全做
- 出处: IV.E Personnel Who Perform Sanitation, Maintenance, and Similar Functions；chunk: ck-26e0c121d1ce
- 原文关键句: "We recommend that you ensure that personnel who handle trash, offal, floor sweepings, drains, production waste, or scrap product do not handle RTE food, and do not touch RTE food-contact surfaces or food packaging material, unless they first change their smocks or uniforms, wash and sanitize hands, wear clean gloves, and don and sanitize footwear."
- 中文大意: ①在 RTE 区工作的卫生与维修人员须遵守与生产人员**同一套卫生要求**；②尽可能为 RTE 区配**专用工具**（不可行则入区前清洗消毒，考虑连工具一起消毒）；③处理垃圾/内脏/地扫物/地沟/生产废料/残次品的人**不得接触 RTE 食品、FCS 或包装材料**，除非先完成四项：换工服 → 洗手消毒 → 戴洁净手套 → 换上并消毒鞋履。
- 类型: rule / procedure
- 建议归属: 新能力建议 `personnel-hygiene-controls`
- 为什么是现有技能缺口: 完全缺失。"四项全做"是可直接写成 SOP 切换步骤的清单式规则；"垃圾/地沟清扫人员不得接触 RTE 食品"是与现有卡"污染源追踪"逻辑相反方向的**污染携带者分类**。

### nB-09 厂房物理分区清单：RTE 区须与八类区域隔离
- 出处: V.A.1 General；chunk: ck-9064017884c4
- 原文关键句: "we recommend that you separate areas where RTE foods are processed, exposed or stored from areas where raw foods are processed, exposed or stored, and from equipment washing areas, microbiological laboratories, maintenance areas, waste areas, offices, lockers and toilet facilities."
- 中文大意: 新建/改造时，RTE 食品加工、暴露、贮存区须与以下八类区域分隔：①生食品加工/暴露/贮存区 ②设备清洗区 ③微生物实验室 ④维修区 ⑤废物区 ⑥办公室 ⑦更衣室 ⑧厕所设施。**实验室应尽可能远、最好另设一栋建筑**——理由：常规微生物检测的富集步骤会先让微生物繁殖，若样品含李斯特菌，富集会放大菌量。
- 类型: design-spec
- 建议归属: 建议新能力 `environmental-engineering-controls`（厂房工程）
- 为什么是现有技能缺口: 现有卡 Step 4 卫生分区只给"按设施/产品/危害分析划定敏感区边界"的抽象要求，没有**可照做的排除清单**，也没有"检测实验室本身是放大源、须远离加工区"这条反直觉设计规则。

### nB-10 施工/改造期间的污染控制措施分级（小型作业 vs 大面积施工）
- 出处: V.A.1 General；chunk: ck-9064017884c4
- 原文关键句: "Certain activities such as installing small pieces of equipment, painting or caulking windows and doors, or replacing parts on equipment are less likely to result in the introduction of L. monocytogenes than activities that are more extensive. When construction activities are more extensive, such as removing/replacing walls, floors or ceilings or installing major equipment or new processing lines, extra measures to ensure control of Listeria are needed."
- 中文大意: 改造/新建会打乱气流、墙面、天花、地面，显著增加交叉污染风险。措施按施工强度分级：小作业（装小设备、刷漆/密封门窗、换零件）风险低；大面积作业（拆换墙/地/天花、装大型设备或新产线）须额外措施：**搭临时屏障隔离施工区、修订动线、强化清洁与消毒、强化环境监测**。设备原位改造或新设备安装同样视为高风险，须参照 V.A.1。
- 类型: procedure / rule
- 建议归属: 新能力 `environmental-engineering-controls`；或 `environmental-pathogen-sanitation` 新增"变更/施工期控制"小节
- 为什么是现有技能缺口: 完全缺失。现有卡无"施工期"概念。这条把"设计施工"与"运行期卫生"接起来，是老厂改造场景的**可执行分级清单**。

### nB-11 RTE 区建筑材料与表面：耐腐蚀、防冷凝积垢、不用多孔吸水材料、禁用可开启窗
- 出处: V.A.1 General；chunk: ck-9064017884c4
- 原文关键句: "We recommend that you design and construct the plant so that walls, ceilings, windows, doors, floors, drains, and overhead fixtures (e.g., pipes, air vents, and lights) in areas where RTE foods are processed or exposed resist deterioration by product or cleaning chemicals, and prevent condensate buildup and harborage of microorganisms. We also recommend that you design and construct the roof so that it drains freely and does not leak. We recommend that you not place windows that can be opened in areas where RTE foods are processed or exposed."
- 中文大意: RTE 区墙体、天花、窗、门、地面、地沟、顶部设施（管道/风口/灯具）须耐产品与清洁化学品腐蚀、防冷凝堆积、防微生物藏匿；屋顶自由排水不渗漏；**RTE 区不得设可开启窗**；**不得使用多孔或吸水材料（如木材、泡沫）**于 RTE 区及其他湿加工区；已存在的多孔材料按第 XIII 章做环境监测，直到更换。
- 类型: design-spec
- 建议归属: 建议新能力 `environmental-engineering-controls`
- 为什么是现有技能缺口: 完全缺失，且是**新建/改造工程图级别的硬性约束**。"木材/泡沫禁用 + 既有则靠 EM 过渡"给老厂一条现实的过渡路径。

### nB-12 气流与压差设计：RTE 侧正压、生区负压；两种替代方案（隔断 vs 气流分离）
- 出处: V.A.2 Air and air flow；chunk: ck-8d0c7fdddb83（附录 3 图示见 ck-4f7aed8701fb、ck-61dcce305dde、ck-9f84693a19ff）
- 原文关键句: "We recommend that you design the air flow in your plant to maintain positive air pressure on the RTE side of the operation relative to the 'raw' side ... Appendix 3 ... Figure 1 ... shows that the recommended air flow should have negative pressure in the raw processing area rather than in the RTE processing area."
- 中文大意: ①RTE 区相对生区维持**正压**（生区负压）——气流方向永远是**从清洁区流向污染区**；②附录 3 给出两种等效设计路线：**图 2 = 生/RTE 之间加实体隔断（partitions）**；**图 3 = 不设隔断、纯靠 RTE 区正压**（图 1 是"不推荐"：Raw Area 为正压）；③进气口不得紧邻排风口或其他空气污染源（废物处置区）；④请具备工程能力的人确定气流平衡与换气率、进风/排风风扇的数量/尺寸/位置；⑤须考虑室温对冷凝的影响。
- 类型: design-spec
- 建议归属: 建议新能力 `environmental-engineering-controls`；与 `environmental-pathogen-sanitation` Step 4 卫生分区联动
- 为什么是现有技能缺口: 现有卡 Step 4 只列"压差方向"为一个应标注要素，**完全没有工程实现路径**（谁是正压、隔断还是气流、进气口布置、与换气率/温度/冷凝的联动）。附录 3 三张图是现成的设计模板——正好补上"物理防线"这一层。

### nB-13 RTE 区空气过滤规格：ASHRAE 52.2-2012 终级 ≥90–95%@1µm，必要时 HEPA 99.97–99.99%@0.3µm
- 出处: V.A.2 Air and air flow；chunk: ck-8d0c7fdddb83
- 原文关键句: "we recommend that the final filter have an efficiency of at least 90-95 percent at 1 micron as rated in American Society of Heating Refrigerating and Air-Conditioning Engineers (ASHRAE) standard 52.2-2012 ... it may be appropriate to use High Efficiency Particulate Air (HEPA) filters that have an efficiency of 99.97-99.99 percent at 0.3 micron for removing bacteria, yeasts and molds."
- 中文大意: 建议对 RTE 加工/暴露区房间空气做过滤；终级滤效按 ASHRAE 52.2-2012 额定值 ≥90–95% @1µm；按产品与工艺需要可上 HEPA（99.97–99.99% @0.3µm）。**有隔离报道**称压缩空气管路内的空气污染，源头是使用点附近的滤器 niche（滤器内滋生）——所以滤器本身是藏匿点，须纳入监测与更换。
- 类型: threshold / design-spec
- 建议归属: 建议新能力 `environmental-engineering-controls`
- 为什么是现有技能缺口: 完全缺失，且带**可查的数值标准**（ASHRAE 标准号 + 效率百分比），是本批中少见的可直接写进采购规格的条款。

### nB-14 水系统与排水沟设计：不得用明沟（trench drain）、排水不得从生区流向 RTE 区、地漏坡度与可清洁性
- 出处: V.A.3 Water systems（含 V.B 续）；chunk: ck-5f8efc49f1e1、ck-d1edd5e497a3
- 原文关键句: "Not installing trench drains in areas where RTE foods are processed or exposed and, where practical, replacing existing trench drains with enclosed plumbing to a floor drain. ... Designing and constructing drains so that the drains do not flow from areas where raw foods are processed or exposed to areas where RTE foods are processed or exposed."
- 中文大意: 水/排水设计清单：①RTE 加工或暴露区**不得设明沟（trench drain）**，可行时把既有明沟改为**封闭管道接地漏**；②明沟不可改时保持清洁并考虑**自动冲洗**（须确保冲洗不产生气溶胶污染产品）；③地漏必须功能良好、**便于清洁可达**；④**排水流向不得从生区流向 RTE 区**（老厂有反向流须建立李斯特菌环境控制体系或重新配管）；⑤**厕所地漏不得与 RTE 区地漏相连**；⑥地面坡向地漏，**自由排水不积水**；⑦污水管线不得位于 RTE 食品/FCS/包装材料上方，不可行时须遮蔽或引流防漏。根因：**积水是李斯特菌温床**。
- 类型: design-spec
- 建议归属: 建议新能力 `environmental-engineering-controls`
- 为什么是现有技能缺口: 现有卡只在"湿区尽量保持干燥"层面提过水，**没有排水沟/地漏/流向/坡度的工程细则**。"厕所地漏不得与 RTE 地漏相连""明沟改封闭管道""自动冲洗须防气溶胶"三条都是极具体、可照做且极易被漏项的项。

### nB-15 冷凝控制：法定锚点 117.20(b)(4) + 四项工程措施
- 出处: V.B General Operation of the Plant；chunk: ck-d1edd5e497a3
- 原文关键句: "Part 117 requires that your plant be designed and constructed in such a manner that drip or condensate from fixtures, ducts and pipes does not contaminate food, FCSs, or food packaging material (21 CFR 117.20(b)(4)). Measures that can help prevent the formation of condensate include exhausting vapors from cooking operations, using dehumidifiers, and providing adequate ventilation."
- 中文大意: 冷凝水/滴液不得污染食品、FCS、包装〔§ 117.20(b)(4)〕。防冷凝措施：①烹饪操作排蒸汽 ②用除湿机 ③充足通风 ④清洁期间**排风以管理湿度**。评估冷凝时须一并考虑：室温、**送风相对湿度**、正压、换气率。
- 类型: rule / design-spec
- 建议归属: 建议新能力 `environmental-engineering-controls`；法规锚点可与 `regulatory-boundaries` 交叉引用
- 为什么是现有技能缺口: 现有卡只在湿区"保持干燥"原则层面触及，没有把冷凝变成**可设计的参数组**（相对湿度 + 换气率 + 排风），也没有点出"送风相对湿度"这个常被忽略的变量。

### nB-16 托盘/运输设备/周转容器：分区专用 + 材质与环境的匹配 + 车轮喷溅风险
- 出处: V.B General Operation of the Plant（含续段）；chunk: ck-d1edd5e497a3、ck-c36cd8f8c3b1
- 原文关键句: "Both plastic and wooden pallets may be a source of Listeria contamination; in general, plastic pallets are better suited than wooden pallets for wet areas. ... We also recommend that you designate one set of equipment (such as carts, forklifts, mobile racks, and pallets) to areas where raw foods are processed or exposed and designate a separate set of such containers to areas where RTE foods are processed or exposed."
- 中文大意: ①RTE 区要有**托盘管理程序**（检查、清洁、状态良好，不得成为污染源）；②**塑料托盘优于木托盘用于湿区**（木托盘宜限于干区/仓库），原因是托盘本身可成为李斯特菌来源（与 nB-11 木材禁用同源）；③**托盘/推车/叉车/移动货架分区专用**（生区一套、RTE 区一套），不可行则进入 RTE 区前**清洁消毒车轮**；④周转容器（totes）按**区域**专用并按**功能**（产品/返工/废料）专用，用**色码或标签**区分，不可行则入区前清洗消毒。
- 类型: design-spec / rule
- 建议归属: 建议新能力 `environmental-engineering-controls`
- 为什么是现有技能缺口: 现有卡完全没有物流器具（托盘/叉车/周转箱/返工容器）这一层。增量价值：**返工（rework）容器专用化 + 色码**是常被忽略的污染路径（返工料把生区菌带回 RTE 线）；"塑料优于木托盘"给出可采购的选型结论。

### nB-17 压缩空气/气体与直接接触 RTE 食品的气体：除湿在源头、过滤在使用点、滤材 >0.3µm
- 出处: V.B（续）；chunk: ck-c36cd8f8c3b1
- 原文关键句: "We recommend that you implement procedures to ensure that compressed gases or air used directly in or on RTE food, or on RTE food-contact surfaces, not become a source of L. monocytogenes. Examples of such procedures are drying and filtration. We recommend that dehydration be done at the source of gas or air supply and that filtration be done at the point of use, using a filter that can retain particles larger than 0.3 micron."
- 中文大意: 直接或间接接触 RTE 食品/FCS 的压缩气体与空气不得成为李斯特菌来源。控制原理：**脱水在气源端做、过滤在使用点做**，滤材须能截留 **>0.3 µm** 颗粒；须有滤器维护措施（否则滤器本身成为 niche，见 nB-13 的隔离报道）。另：水系统须维护检查以免成为污染源；**冰与冰铲的生产/处理/存放须防微生物污染**，冰铲与冰勺**不得直接接触地面或其他非 FCS**。
- 类型: design-spec / rule
- 建议归属: 建议新能力 `environmental-engineering-controls`；与 `environmental-pathogen-sanitation` Step 3（禁压缩空气吹扫）形成对照
- 为什么是现有技能缺口: 现有卡只说"禁压缩空气吹扫残留"（禁止性），缺**允许性工程做法**（源头除湿 + 使用点过滤 + 滤材规格），也缺"冰铲不得触地"这类具体卫生设计。

### nB-18 生产期间禁用水枪冲洗；连续使用的盐卤与回收工艺水须定期处理
- 出处: V.B（续）；chunk: ck-c36cd8f8c3b1
- 原文关键句: "To prevent aerosols from contacting RTE food, FCSs, and food packaging materials, personnel should not use high-pressure water hoses during production in areas where RTE foods are exposed or after equipment has been cleaned and sanitized. We recommend that you discard or treat continuous use brines and recycled process water used in direct contact with RTE foods with sufficient frequency to control L. monocytogenes."
- 中文大意: ①RTE 暴露区**生产期间**以及**设备已清洁消毒之后**，不得使用高压水枪（水雾/气溶胶会污染 RTE 食品、FCS 与包装）；②与 RTE 食品直接接触的**连续使用盐卤与回收工艺水**须以足够频率**弃置或处理**（氯化、臭氧、热处理或其他有效处理），**处理频率应参考 L. mono 环境监测结果**确定。
- 类型: rule / threshold(procedural) / procedure
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 3 湿区三原则的细化）
- 为什么是现有技能缺口: 现有卡已点出"禁高压水/压缩空气等扩散性清洁"，但**没有覆盖"已清洁消毒后"这一时间窗**，也没有"盐卤/回收水处理频率由 EM 结果驱动"这一**闭环设计**。李斯特菌耐高盐（非氯溴盐卤水）这一点也出自同段（ck-0cd39fecb3c1）——**耐盐 + 低温**是李斯特菌在冷链盐卤系统中的生存优势。

### nB-19 设备设计总则：RTE 接触面光滑/不吸水/密封/可排空、接合处覆盖、无死端与生熟交叉连接
- 出处: VI.A Design and Construction of Equipment；chunk: ck-ba50e22228a7
- 原文关键句: "We recommend that RTE FCSs be smooth, non-absorbent, sealed, and sloped, where feasible, in order to drain freely, and that junctures in RTE FCSs be covered. Piping used to convey RTE foods should not have dead ends or cross-connections between conveyance of raw and RTE foods. The sanitary standards inventoried by 3-A Sanitary Standards, Inc. can be useful when designing and constructing equipment containing FCSs."
- 中文大意: 设备采购与改造的验收清单：①RTE 食品接触面须**光滑、不吸水、密封，并在可行处带坡度以自由排空**；②接触面**接合处须被覆盖**（不留积垢缝）；③输送 RTE 食品的管路**不得有死端（dead ends）**，也**不得在生料与 RTE 食品输送之间存在交叉连接（cross-connections）**；④新建/改造 RTE 设备的图纸须由企业或设备制造商**审查是否减少藏匿与繁殖场所**；⑤**引用 3-A Sanitary Standards**（行业卫生标准清单）作为 FCS 设备设计参照。
- 类型: design-spec
- 建议归属: 建议新能力 `environmental-engineering-controls`（设备分部）
- 为什么是现有技能缺口: 现有卡只有"老旧/密合/中空结构设备列为难清洁重点"这一**存量清单式**判断，没有**采购/改造阶段的图纸级验收标准**（不吸水、接合覆盖、无死端、无生熟交叉连接），也没给出 **3-A 标准**这个可直接引用的行业规范指针。注意：本指南未给"圆角半径 ≥X"这类尺寸数值，工程细化需借 3-A 与其他科学文献。

### nB-20 非 FCS 结构件不得空心/泡沫填充（走道支架、桌腿、输送辊、货架）
- 出处: VI.A；chunk: ck-ba50e22228a7
- 原文关键句: "We recommend that you design and construct equipment such as catwalk framework, table legs, conveyor rollers, and racks so that they cannot collect water that could harbor L. monocytogenes (e.g., they should not be hollow or foam filled). You should either modify or replace existing equipment not designed this way, or establish and use some other method to reduce the risk ... including a schedule for periodic cleaning and sanitizing combined with an environmental monitoring program."
- 中文大意: 走道支架、桌腿、输送辊、货架等**不得设计成能积水**（**不得空心、不得泡沫填充**）。既有不合规设备有三条合法出路：①改造 ②更换 ③其他等效方法（定期清洁消毒计划 **+** 环境监测程序）——第三条是给无法改造的老厂留的正式出口。
- 类型: design-spec / rule
- 建议归属: 建议新能力 `environmental-engineering-controls`
- 为什么是现有技能缺口: 现有卡无"空心/泡沫"这一具体结构缺陷判据。且**第三条出路（清洁+EM 替代结构性整改）**是一个可辩护的合规路径——可与现有卡 Step 5 的 transient/resident 分诊衔接。

### nB-21 走道与楼梯：不得用开放格栅位于暴露 RTE 食品/FCS 正上方；替代做法与清洁排程
- 出处: VI.A；chunk: ck-ba50e22228a7
- 原文关键句: "We recommend that you not position catwalks and stairs with open grating over exposed RTE food or FCSs ... If this is not practical, you should use ladders and stairs designed to prevent debris from shoes or other personal items from falling onto the processing line (e.g., plating covering the underside of the stairs, or side plates along the stairs). Plate coverings should be on a cleaning schedule."
- 中文大意: 开放式格栅走道/楼梯不得位于暴露的 RTE 食品或 FCS 正上方（格栅上藏匿的菌与鞋底碎屑会落到产品上）；不可行时改用能防止碎屑掉落的设计：**楼梯底面加盖板（plating covering the underside）、或加侧板（side plates）**；**盖板须纳入清洁排程**。
- 类型: design-spec
- 建议归属: 建议新能力 `environmental-engineering-controls`
- 为什么是现有技能缺口: 完全缺失。典型"容易漏掉的构造细节"，且替代方案（盖板/侧板 + 清洁排程）是可直接施工与写进清洁表的。

### nB-22 固定设备不得位于地漏上方；FCS/输送带须抬高；避免空中输送线
- 出处: VI.A 与 VI.B 续；chunk: ck-ba50e22228a7、ck-e6698ed235e5
- 原文关键句: "We recommend that you not install stationary equipment used to process RTE foods over floor drains. ... We recommend that you sufficiently elevate FCSs (including conveyors) above the floor. ... Although we are recommending that conveyors be elevated, we also recommend that you avoid overhead conveyors whenever practical. If overhead conveyors cannot be avoided, they should be designed to be easily accessible for cleaning; note that part 117 requires that they be constructed in such a manner that drip or condensate from them does not contaminate food, FCSs, or food-packaging materials (21 CFR 117.20(b)(4))."
- 中文大意: ①处理 RTE 食品的**固定设备不得装在地漏上方**（地漏是李斯特菌藏匿点）；不可行时须用其他方法防止地漏污染并**监测该地漏**；②FCS（含输送带）须**充分离地**，以减少地面飞溅/过喷污染；不可行时覆盖 FCS 并监测地面；③**尽量避免空中输送线**；不可避免时须设计成**易于清洁**，且其滴液/冷凝不得污染食品、FCS、包装〔§ 117.20(b)(4)〕。
- 类型: design-spec / rule
- 建议归属: 建议新能力 `environmental-engineering-controls`
- 为什么是现有技能缺口: 完全缺失。"固定设备不压地漏""FCS 离地""避免空中输送线"三条是布局图级别的硬约束；且都带"不可行时的替代路径 + 监测该点位"，与现有卡 EM 体系可闭环。

### nB-23 轮式设备设计：轮罩、全封闭轴承、最下层货架高于溅水高度
- 出处: VI.B 续（maintenance/design 段）；chunk: ck-e6698ed235e5
- 原文关键句: "We recommend that you use wheeled devices that are designed to reduce the risk of contamination of RTE foods and FCSs from wheel spray (e.g., guards over the wheels, fully enclosed/encased bearings, lowest shelf on the wheeled rack is located above splash height)."
- 中文大意: 轮式器具（推车、叉车、移动货架）须按**防轮溅**设计：①轮子上方设护罩（guards over the wheels）②轴承**全封闭/包壳**（fully enclosed/encased bearings）③移动货架**最下层板面高于溅水高度**。另：冷藏蒸发器冷凝水须用软管导入卫生地漏（或先入盘再经软管/管道排入），**排水管须设空气隔断或防倒流装置**防止污水回流至滴漏盘；须定期检查盘与管路防堵，软管与滴漏盘须有清洁排程。
- 类型: design-spec
- 建议归属: 建议新能力 `environmental-engineering-controls`
- 为什么是现有技能缺口: 完全缺失。"轮溅"是 RTE 车间高频污染机制（现有卡的 nB-16 也涉及车轮消毒，但这里给的是**结构性预防**）；"空气隔断防倒流"是排水/冷凝系统的具体工程细节。

### nB-24 板式换热器用生料冷却 RTE 产品时：RTE 侧压力须高于生料侧
- 出处: VI.B 续；chunk: ck-e6698ed235e5
- 原文关键句: "If you use raw product to cool RTE product in a heat exchanger, we recommend that heat exchangers have higher pressure on the RTE side than on the raw side."
- 中文大意: 用生料给 RTE 产品降温的换热器，**RTE 侧压力必须高于生料侧**——防止生料侧破裂/渗漏时污染 RTE 产品（与 nB-19 的"无生熟交叉连接"同源的压差防逆流设计）。
- 类型: design-spec / rule
- 建议归属: 建议新能力 `environmental-engineering-controls`；可与 `process-control-validation` 交叉引用
- 为什么是现有技能缺口: 现有工艺卡讨论冷却协议与"真空吸入"陷阱，但没有这条**换热器压差方向**规则。

### nB-25 预防性维护程序：防止维修期污染、滤器更换频次、工具专用化、维修后必须清洁消毒才可投产
- 出处: VI.B Maintenance of Equipment；chunk: ck-e6698ed235e5
- 原文关键句: "We recommend that you establish and use a preventive maintenance program that is designed to minimize breakdowns and prevent contamination that could occur during repair of equipment. ... We recommend that you examine and change filters used on intake air and for compressed air systems either at a frequency based on the manufacturer's specification or more frequently based on pressure differentials or the results of environmental monitoring. ... Equipment and FCSs ... should be cleaned and sanitized after maintenance and prior to use in production consistent with the requirements of 21 CFR 117.35(d)."
- 中文大意: ①建立预防性维护程序，目标是**减少故障停机**并**防止维修期间的污染**（维修是"设备停机+人员进入+暴露"的三重污染窗口）；②进气与压缩空气系统的滤器，按**厂商规格频率**更换，或**按压差/环境监测结果更频繁**更换；③进入 RTE 区使用的**维修工具应专用**，不可行时须充分清洗**并考虑消毒**；④维修后（尤其公用工程如空气/水系统、厂房改造可能带来的污染）的设备与 FCS，**使用前必须清洁消毒**〔§ 117.35(d)〕。
- 类型: rule / procedure
- 建议归属: 建议新能力 `environmental-engineering-controls`；法规锚点接 `management-components`（monitoring/records）
- 为什么是现有技能缺口: 现有卡完全没有"**维修期是一个污染事件窗口**"这一概念，也没有"**维修后必须清洁消毒才可投产**"这条可审计的放行规则。滤器更换频率由"压差/EM 结果"驱动，也是 EM 反哺工程设计的范例。

### nB-26 设备维护记录必须列出具体部件清单（阀门、垫片、O 型圈、泵、筛网、过滤器、换热器板片）
- 出处: VI.C Records；chunk: ck-90ebb33c24ab
- 原文关键句: "We recommend that your written program for equipment maintenance include defined schedules for examination and maintenance of equipment such as valves, gaskets, O-rings, pumps, screens, filters, and heat exchanger plates."
- 中文大意: 书面设备维护程序须为下列部件定义**检查与维护的既定频次表**：阀门（valves）、垫片（gaskets）、O 型圈（O-rings）、泵、筛网（screens）、过滤器、换热器板片（heat exchanger plates）。
- 类型: procedure / rule
- 建议归属: 建议新能力 `environmental-engineering-controls`；或 `management-components` Step 1（What/How often 的对象清单）
- 为什么是现有技能缺口: 现有管理卡给的是**通用监控四问与频次基线**，没有**部件级对象清单**。这是可直接抄进 SOP 的 7 类部件清单——尤其垫片/O 型圈/换热器板片这类"可藏匿但不出现在设备台账上"的部件。

### nB-27 附录 1 五类潜在污染源清单（Ingredients / Processing materials / RTE 接触面 / 非接触面 / 厂区环境）——可改写为"藏匿点巡检表"
- 出处: 附录 1 Potential Sources of L. monocytogenes；chunk: ck-bf70888a9266
- 原文关键句: "E | Plant environment | •Floors, especially cracks and crevices •Walls •Drains •Ceilings, overhead structures, and catwalks •Wash areas (e.g., sinks), condensate, and standing water •Wet insulation in walls or around pipes and cooling units •Rubber seals around doors, especially in coolers •Metal joints, especially welds and bolts •Contents of vacuum cleaners"
- 中文大意: 附录 1（改编自 Ref. 43）把李斯特菌潜在来源分成 **A 配料 / B 加工材料 / C RTE 食品接触面 / D 通常不接触 RTE 食品的表面 / E 厂区环境** 五类，每类给出点名清单。要点摘录：B 类含**压缩空气、冰、冷藏 RTE 用的盐卤液**；C 类含**纤维/多孔输送带、灌装包装设备、皮带/削皮机/分选机、容器/盆/桶/篮、切片机/切丁机/碎切机/搅拌机、器具、手套**；D 类含**地磅、开裂软管、中空输送辊、设备框架、湿/锈/中空框架、外露轴承、维护不良的压缩空气滤器、冷凝滴漏盘、电机壳、维修工具、叉车/手推车/推车/货架、开关、真空吸尘器与洗地机、垃圾桶、清洁工具（刷/百洁布）、螺旋速冻机/ blasting freezer、制冰机、围裙**；E 类含**地面裂缝缝隙、墙、地漏、天花与顶部结构与走道、清洗区与冷凝水与积水、墙内或管道/冷凝单元周围的湿保温层、冷库门胶条、金属接缝（焊缝与螺栓）、吸尘器内容物**。
- 类型: fact / procedure（可直接工具化）
- 建议归属: 新能力建议 `environmental-engineering-controls`（或 `environmental-pathogen-sanitation` 作为"藏匿点巡检清单"附录）
- 为什么是现有技能缺口: 现有卡有"transient vs resident"的分诊判据，但**没有具名的藏匿点清单**——这是本指南最高价值的现成工具，可直接转成巡检表/EM 点位扩充清单/设备采购审查表（注意它与第 XIII 章的 Zone 1–4 分区可交叉使用）。

### nB-28 附录 2 污染场景推演清单——把"可能出事的地方"写成事件清单
- 出处: 附录 2 Examples of Scenarios That Could Lead to Contamination of RTE Foods；chunk: ck-3a1870594911
- 原文关键句: "The examples below of scenarios that could lead to contamination of RTE foods with L. monocytogenes are adapted from Ref. 43 and Ref. 47. A packaging line is moved or modified significantly. Used equipment is brought from storage or another plant and installed into the process flow. An equipment breakdown occurs. Construction or major modifications are made to an area where RTE foods are processed or exposed ... A drain backs up. Product is caught or hung-up on equipment. (Stagnant product in a system can be a major site of microbial growth during production.)"
- 中文大意: 附录 2（改编自 Ref. 43 与 Ref. 47）列出 21 个会导致 RTE 食品被李斯特菌污染的**场景剧本**（按性质归并）：①产线迁移或重大改造 ②从库存/其他工厂调入旧设备 ③设备故障 ④RTE 区施工或大改造（换制冷机组/地面、换或建墙、改污水管线）⑤新员工入职（不熟悉李斯特菌控制）⑥人员接触可能污染的表面/设备（地面、垃圾桶）后未换手套 ⑦高产量期冷藏区地面无法按计划清洁 ⑧**地漏返水** ⑨**产品滞留/卡料（滞料是生产期间主要的微生物生长场所）** ⑩生/未充分加工食品被放进"熟制区" ⑪换产频繁导致频繁更换膜/标签/成型口袋/模具与线速 ⑫包装人员与生/熟人员互换 ⑬增产导致停线产线湿洗与在产产线同室 ⑭换热器被破坏（如出现针孔） ⑮设备零件/盆/筛在地面上清洁 ⑯RTE 区废物桶维护/清洁消毒不当 ⑰循环泵与管线未清洁消毒 ⑱无差别使用高压水枪 ⑲**在干加工区不当使用泡脚器** ⑳**对运输车轮喷水时在制品存放在车轮附近**。
- 类型: procedure / fact（可直接工具化为"变更与事件触发的再评估触发器"清单）
- 建议归属: 新能力建议 `environmental-engineering-controls`；也可与 `management-components` E Step 6（再分析触发器）联动
- 为什么是现有技能缺口: 现有卡的再分析触发器（§ 117.170）是**法规层事件**（变更/新信息/意外/失效），而本附录给的是**李斯特菌专属的微观事件剧本清单**（如"卡料""地漏返水""换热器针孔""湿洗与在产同室"）——可直接改写成"哪些日常/异常事件必须触发一次卫生复评与 EM 加强"。附录 2 第 ⑲ 条与 nB-05（干区禁用湿式泡脚器）互为印证。

### nB-29 适用性分流：CGMP 主体 vs PCHF 主体，以及"指南写建议但法规要求必须"的效力错位
- 出处: II.A Regulatory Framework 与 III（附表 1/表 2）；chunk: ck-ddd9e8ac1c50、ck-273341c1a2ac
- 原文关键句: "Because some persons who are subject to the CGMP requirements in subpart B are exempt from the PCHF requirements in subparts C and G, this guidance: Is written as a set of recommendations even though in some cases part 117 includes an explicit requirement. ... If you are a facility subject to the PCHF requirements of part 117, you must comply with 21 CFR 117.160(a) even though this guidance 'recommends' validation..."
- 中文大意: 这份指南的效力结构（**第三章的权威答案**）：①只受 CGMP（part 117 subpart B）约束的主体（因某些豁免而免 subpart C 与 G 的 PCHF 要求）读到的全部是"建议"；②受 PCHF 约束的主体，即使指南写"recommends"，只要 part 117 有明文要求（如 § 117.160(a) 验证）**就是 must**；③指南用"control/control measure"这类泛称指代 preventive control——**术语层也做了合并，读时须自行判断其法定身份**；④本指南与专项指南**互补而非取代**（寿司用鱼仍应遵循 part 123 的鱼类 HACCP 指南；鲜切果蔬另有专门指南）；⑤表 1 列出讨论的 CGMP 条款（117.10 人员、117.20 厂房与场地、117.35 卫生操作、117.37 卫生设施与控制、117.40 设备与器具、117.80 过程与控制、117.93 仓储与配送），表 2 列出 PCHF 条款（117.126/130/135/139/140/145/150/155/160/165/170/190）。
- 类型: rule / fact
- 建议归属: 并入 `regulatory-boundaries`（豁免与效力边界）
- 为什么是现有技能缺口: 现有卡讲清了 PCHF/CGMP 义务边界与豁免通道，但**没有"读指南时如何判断某句话是建议还是义务"这一元规则**；也没有给出"哪些条款被本指南逐条对照"的索引表（表 1/表 2），后者是把它接进现有技能体系的对接点。

---

## 二、近重复（现有技能已覆盖，本指南可补细则）

- rB-01: RTE 食品包装前暴露环境且包装后无致死处理 → 强制评估环境病原〔§ 117.130(c)(1)(ii)〕 ↔ 现有卡 `hazard-analysis-method` E Step 3「强制触发器」+ `environmental-pathogen-sanitation` E Step 1「判定适用性三条件」。本指南 II.B/II.C（ck-9e6d4d150cd2、ck-0cd39fecb3c1）重述同一触发逻辑，**增量仅为**：可加"包装后含致死性配方（如 pH≤4.4）同样关闭触发器"的举例说明。
- rB-02: 湿区（李斯特菌）vs 干区（沙门氏菌）的对策分野；"尽量保持干燥"优先于增加冲洗；禁高压水/压缩空气等扩散性清洁 ↔ 现有卡 `environmental-pathogen-sanitation` E Step 3 湿区/干区三原则。本指南 V.B 续段（ck-c36cd8f8c3b1）与附录 2 第 ⑱ 条（ck-3a1870594911）提供**细则**：生产期间禁用 + 已清洁消毒后禁用；无差别使用高压水枪列为污染剧本。
- rB-03: transient vs resident 的分诊判据（时间持续性 + 株型指纹一致性）、环境监测点位与频次须"足以判定预防控制是否有效"〔§ 117.165(b)(3)〕 ↔ 现有卡 `environmental-pathogen-sanitation` E Step 5。本指南增量：第 XIII 章的 **Zone 1–4 分区**（Zone 1 FCS；Zone 2 近区 FCS 的非接触面如设备框架、紧邻 FCS 的部分墙面地面与地漏；Zone 3 较远的非接触面如叉车手推车与非邻接墙面地面；Zone 4 区外如更衣室/cafeteria/走廊）与附录 1 的 E 类（厂区环境）清单**可以拼成一张 EM 点位设计表**（另一代理负责 XIII 章正文，此处仅记接口）。
- rB-04: 洁净区/污染区人流物流分离、压差方向须标注在分区图上 ↔ 现有卡 `environmental-pathogen-sanitation` E Step 4「卫生分区」。本指南 nB-12/nB-14 补**工程实现**：正压/负压方向、生熟隔断 vs 气流分离两条路线、明沟改封闭管道、地漏流向不得生→RTE。
- rB-05: 验证（validation）与实施前/90 日窗、证据优先级为"先获取科学证据"〔§ 117.160(b)(1)(2)〕 ↔ 现有卡 `process-control-validation` E Step 3、`management-components` E Step 4。本指南 III 章（ck-273341c1a2ac）只重述"受 PCHF 约束者 § 117.160(a) 是 must"，无新方法学。
- rB-06: 记录要素与保存期限、监控/纠正记录 7 个工作日审查、异常记录与减负 ↔ 现有卡 `management-components` E Step 5、Step 7。本指南 VI.C（ck-90ebb33c24ab）只补"部件级维护频次表"这一对象清单（见 nB-26），记录法本身无增量。
- rB-07: 危害分析需覆盖"环境病原"的边界定义（§ 117.3 排除芽孢） ↔ 现有卡 `environmental-pathogen-sanitation` E Step 2、`hazard-analysis-method` E Step 3。本指南增量：II.C（ck-0cd39fecb3c1）列举**物理防线控制手段清单**——原料控制、listericidal、listeristatic、生熟隔离、卫生控制、卫生设备设计、物理屏障（分离）——可作为"可选控制手段目录"补进现有卡 Step 5。
- rB-08: 冷藏不能作为李斯特菌对策（近冰点仍生长、冷冻仅休眠） ↔ 现有卡 `environmental-pathogen-sanitation` B 边界 6。本指南增量：II.C 补两条**耐性数据**——耐高盐（**非氯溴盐卤冷却液**）、耐酸、耐热较多数营养细胞强（但巴氏杀菌可杀灭），冷藏温度下仍能缓慢繁殖 ⇒ 冷藏对李斯特菌的效力低于对沙门氏菌。

---

## 三、潜在矛盾

- **未发现**与现有卡片在工程要求层面的实质矛盾。以下三处为**本指南自身的表述不一致/需谨慎**，供合并时注意：
  1. **指南内部章节交叉引用错位（笔误）**：ck-e6698ed235e5 中"See section IV.C for recommendations for a written preventive maintenance program"，但按本文件目录结构，IV.C 是 Clothing，预防性维护程序实际位于 IV.E/VI.B 一线；同时 nB-08 引用了"section V.A.1"（ck-26e0c121d1ce），而 V.A.1 实为"General（厂房设计）"，并非 IV.D 的前半引用。引用时须核对原始 PDF 目录，不要照抄章节号。
  2. **"改建/改造"的责任归属重叠**：ck-ba50e22228a7 说设备原位改造或新设备安装风险升高，须参照 V.A.1 的施工期控制；而 V.A.1（ck-9064017884c4）本身讲的是建筑施工。工程规范层面二者一致，但执行时须把"设备改造"也纳入"施工期临时屏障 + 强化 EM"的触发条件，否则会漏掉只换设备不动墙的常见情形。
  3. **"冰"在两处定位不同**：附录 1（ck-bf70888a9266）把"冰"列在 B 类"加工材料"（直接接触 RTE 的投入物），而 ck-c36cd8f8c3b1 的运行条款把冰归为"公用介质/器具卫生"（冰铲不落地）。二者不冲突，但工具化时冰应同时出现在"EM/物料来源清单"与"器具卫生清单"两处。
  4. **潜在冲突（本指南 vs 现有卡语气）**：现有卡 `environmental-pathogen-sanitation` Step 3 写"湿区第一杠杆是减少漫水而非增加冲洗"，本指南 IV.B 却在湿区推荐 foamers/footbaths（含液）这类**额外引入水**的化学屏障。二者并不对立（屏障是入口定点消毒，非产线漫水），但合并时应显式写明"化学屏障用水量是受控小体积定点使用，不属湿区漫水"，否则读者会判为矛盾。

---

## 四、跨章节提示（属于其他代理负责的章节）

1. **附录 4 清洁消毒时间表**（ck-ec83f3e46e / ck-ec83f3e7e46e 起，约第 3330 行起）：本批的设备维护与工程设计条目（nB-20 盖板清洁排程、nB-23 软管与滴漏盘清洁排程、nB-25 维修后放行）需要与附录 4 的 **FCS 至少每 24 小时清洁消毒一次**、以及非接触面按表列频次（该表改编自 Ref. 43）配套才能形成闭环，建议合并时互相引用。
2. **附录 5 环境采样程序**（ck-db5f8a7358e8 起，约第 3394 行起，含表面采样 / 冲洗液 / 地漏流出液液体采样 / 海绵拭子合并 / 液体样品制备）：nB-14 的"监测地漏"、nB-20 的"结合 EM 替代结构整改"、nB-22 的"监测地漏与地面"、nB-27 附录 1 清单的落地采样方式，全部指向附录 5 的具体采样程序——**附录 1 是"找什么"，附录 5 是"怎么取"**，合并时应成对引用。
3. **第 XIII 章 环境监测（Zone 1–4 分区 + 检出后纠正措施流程图）**：nB-05 的"每小时检查泡脚器"、nB-18 的"处理频率参考 EM 结果"、nB-25 的"按压差/EM 结果换滤器"三条都把 EM 结果作为工程参数的反馈输入，Zone 1–4 分区表（约第 1929–1939 行）与本批附录 1 清单应对齐成同一套点位语言。
4. **第 VII 章 卫生程序（Sanitation）**：ck-c36cd8f8c3b1（禁止生产期间/清洁消毒后用高压水枪）、ck-3a1870594911（无差别使用高压水枪、湿洗与在产同室）实际是**卫生程序章节的执行细则**，合并时宜由卫生程序卡承载步骤，本批工程卡只保留"设计层面禁止产生气溶胶"的设计要求（避免重复）。
5. **第 IV.C / IV.E 与第 X 章（工艺控制：listericidal/listeristatic 验证）**：nB-01/nB-02（pH≤4.4、aw≤0.92、hurdles、<1 log 增幅判据）属第 IX/X 章（过程控制与验证）内容，本批只作指针，**验证方法学请由负责 IX/X 的代理定稿**，避免两处各自展开。
6. **附录 3 三张气流/厂房示意图**（ck-4f7aed8701fb 图 1 "Not Recommended—Raw Area has 'Positive Air Pressure'"、ck-61dcce305dde 图 2 生/RTE 隔断、ck-9f84693a19ff 图 3 纯气流分离）：chunk 中只有图题与图 1 的文字标注，**图形本体未进入 chunk**；若技能要提供"照着图做"的厂房布局模板，需回到指南 PDF 取附录 3 原图（并核对附录 4/5 的图片处理方式）。
