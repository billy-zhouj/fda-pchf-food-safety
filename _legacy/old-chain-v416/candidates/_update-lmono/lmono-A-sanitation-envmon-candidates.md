# L.mono 增量候选 A：卫生控制与环境监测（来源标注 chunk id）

> 来源文件：FDA《Control of Listeria monocytogenes in Ready-To-Eat Foods: Guidance for Industry (Draft, 2017年1月)》
> 负责范围：VII. Sanitation（956–1248）／XIII. Environmental Monitoring（1831–2524）／XV. Analysis of Data for Trends（2591–2706）
> 现有技能基线：`environmental-pathogen-sanitation`（已通读）、`management-components`（E/B 段）、`recall-plan`、`supply-chain-verification`（仅 one_liner/标题）
>
> **chunk id 错位提示（重要）**：本文件的 chunk 切分存在标题与正文错配（例如"ck-e0bbb1e83fca / C. Sanitizers"标题下实际是 VII.B 地漏段落尾部；"ck-849cc429dc91 / F. Relevant Sections of Part 117"标题下实际是 VII.A.4 蒸汽/热水内容；"ck-30a8e65f8e6d / XV.A"标题下实际是 XIV.B 产品阳性处置内容）。下文每条均按**正文实际归属的章节号**标注，并保留该 chunk id，合并时以章节号为准。

---

## 一、新知识候选（现有技能没有或本指南更精确的）

### nA-01 书面卫生程序的七步固定序列（含"先干清"而非"干式清洁优先"）
- 出处: VII.A.1；chunk: ck-df42de7cda8e
- 原文关键句: "1. Dry Clean – Using appropriate tools (such as brushes, scrapers), remove heavy soils or debris from equipment, then floors; 2. Pre-Rinse … 3. Soap and Scour … 4. Post-Rinse … 5. Prepare for Inspection … 6. Pre-Op Inspection … 7. Sanitize and Assemble – … using ATP bioluminescence or other appropriate testing as a sanitation check."
- 中文大意：设备→地面干清（刷/刮）→自上而下预冲洗→自下而上泡沫清洗并刷洗（不得让泡沫干燥）→同序冲洗→去除顶部冷凝水与积水→开机前目视检查并整改→消毒+组装，可用 ATP 生物发光做卫生检查。
- 类型: procedure
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 3 清洁策略选择）
- 为什么是现有技能缺口: 现有卡只有"湿区三原则/干区三原则"的原则层，没有可照抄的作业顺序；B4 自认"具体清洁程序细节须依赖其他资源"。

### nA-02 清洁频次的四个决定因素 + 附录4可裁剪的例行时间表
- 出处: VII.A.2；chunk: ck-e758db4c9dc8
- 原文关键句: "To determine the cleaning frequency, you should review the sanitary design of the room and equipment, the microbiological profile during a production run, the history of Listeria spp. in the room and on the line, and the degree of product exposure to the line and the environment. See Appendix 4 for examples of schedules for routine cleaning and sanitation."
- 中文大意：频次由①房间与设备卫生设计 ②一次生产期间的微生物学剖面 ③房间/产线 Listeria spp. 历史 ④产品对产线与环境的暴露程度 共同决定；附录4给出例行清洁消毒时间表模板，须按本厂状况、卫生设计、生产排程与产品特性修改；房间应尽可能保持干燥（水分助长李斯特菌生长与转移）。
- 类型: rule / tool
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 3，卫生分区/频次）+ 建议新增"清洁消毒程序模板"子节
- 为什么是现有技能缺口: 现有卡说"频次表须依赖其他资源"，未给频次的**决定变量集合**，也未指出可用附录式模板再裁剪。

### nA-03 书面卫生程序必须写明的八项要素（含清洁剂浓度与工具颜色编码）
- 出处: VII.A.1；chunk: ck-df42de7cda8e
- 原文关键句: "Written sanitation procedures for cleaning equipment and floors identify: Equipment or area to be cleaned; Disassembly of equipment, if applicable; Frequency of cleaning; Type and concentration of cleaning compounds and sanitizers; Type of cleaning tools to be used …; Color coding of tools (e.g., red for those related to raw materials … blue for those related to RTE areas); Time/temperature of cleaning solutions; and Flow rate (velocity) or pressure of cleaning solution, if applicable."
- 中文大意：设备/区域、是否拆装、清洁频次、清洁剂与消毒剂类型及浓度、清洁工具类型、工具颜色编码、清洗液时间/温度、清洗液流速或压力——八项缺一不可。
- 类型: procedure
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 3）或 `management-components`（Step 1 监控设计/书面化清单）
- 为什么是现有技能缺口: 现有卡讲"清洁先于消毒、按标签用 EPA 注册消毒剂"，但没有"程序文本本身要写哪些字段"的清单——这是 FDA 检查表级别的可核对项。

### nA-04 工具与布巾的具体处置规则（一次性、弃置频率、专用化与色标）
- 出处: VII.B；chunk: ck-09084c3dfe50
- 原文关键句: "We recommend that all wipes be disposable and discarded after each use on RTE food-contact surfaces and that scouring pads be discarded frequently. When scouring pads are not in use during the day, we recommend they be kept dry or placed in a sanitizer solution."
- 中文大意：接触 RTE 接触面的所有擦拭布一次性使用、用后丢弃；百洁布须频繁更换，不使用时保持干燥或浸在消毒液中；地面/地漏用清洁工具不得用于 FCS；清洁设备（刷子、拖把、地刷、水槽、槽、吸尘器）须维护清洁消毒以免成为污染源；清洁工具应按 RTE 区与原料区专用化并用色标区分。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 3 工具与设施）
- 为什么是现有技能缺口: 现有卡只列"老旧/密合/中空设备为难清洁重点"，没有布巾/百洁布这类**消耗性工具**的处置规则（用后丢弃、干燥或浸消毒液）。

### nA-05 湿式清洁的硬禁止：RTE 食品或包装暴露的房间内不得湿洗（覆盖也不行）
- 出处: VII.A.3；chunk: ck-22b7c984be1e
- 原文关键句: "Not perform wet cleaning of equipment (e.g., down lines, storage and spiral coolers, and spiral freezers) in a room where RTE food or packaging is exposed, even if you cover the RTE food or packaging (e.g., with plastic or paper). If wet cleaning does occur, you should remove all exposed RTE food or packaging from a room before beginning any wet cleaning."
- 中文大意：在 RTE 食品或包装暴露的房间内不得进行设备湿式清洁（下料线、储存段、螺旋冷却器、螺旋冷冻机），**即使覆盖塑料或纸也不允许**；若确需湿洗，必须先移出所有暴露的 RTE 食品与包装；清洁冷藏/冷冻库、制冷冷凝机组、滴水盘与软管前必须移出所有暴露 RTE 食品。湿洗须验证不危及相邻设备。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 3 湿区原则 + B3 "更干净的冲动可能有害"）
- 为什么是现有技能缺口: 现有卡禁的是高压水/压缩空气这类**扩散性**清洁，未把"在 RTE 暴露房间内湿洗本身"列为禁止项，也未给"覆盖即可"的反例。

### nA-06 过度喷溅（overspray）的距离-压力判据
- 出处: VII.A.3；chunk: ck-22b7c984be1e
- 原文关键句: "The proximity of equipment and lines influences the risk of overspray; in general, the risk of contamination from overspray increases when using low pressure within 20 feet and when using high pressure within 30 feet. One mechanism to reduce the potential for contamination from overspray is to erect clean curtains or temporary walls."
- 中文大意：清洗相邻产线时，低压喷淋在 **20 英尺内**、高压喷淋在 **30 英尺内**风险升高；缓解手段为搭清洁帘或临时隔墙。同时须控制：冷凝（充分排掉蒸汽/雾/水雾产生的冷凝水）、排水（不得造成共用地漏回涌、化学品不得流向运转设备）、环境（不得扰乱室温/相对湿度/空气压平衡）、人流物流（清洁期动线变化不得污染产品）。
- 类型: threshold
- 建议归属: 并入 `environmental-pathogen-sanitation`（B3 反向操作清单）
- 为什么是现有技能缺口: 现有卡只有定性禁令，无**可测的距离/压力阈值**；这是可现场量化的判据。

### nA-07 共用 CIP 系统的温度底线与 CIP/COP 监控参数
- 出处: VII.A.3；chunk: ck-22b7c984be1e
- 原文关键句: "If you are unable to designate separate CIP systems and, thus, use a common CIP system, we recommend that you maintain the temperature of an alkaline cleaning solution at or above 71 degrees C (160 degrees F)."（另：CIP 监控清洗液与消毒剂浓度并验证流速、清洗周期时长与温度；COP 监控浓度与温度；共用 COP 时须另设洗涤顺序、洗涤温度等程序。）
- 中文大意：RTE 与原料设备应分别专用 CIP；无法专用而共用时，碱性清洗液温度须保持 **≥71 °C（160 °F）**；CIP 监控浓度/流速/周期时长/温度，COP 监控浓度与温度；共用 COP 时 RTE 侧 COP 系统应设于或靠近 RTE 区，否则须用洗涤顺序与温度等程序控制交叉污染；组装好的洁净设备不得直接放在地面或非清洁表面。
- 类型: threshold / rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 3）+ `process-control-validation`（CIP 参数监控）
- 为什么是现有技能缺口: 现有卡未提 CIP/COP 之分与 71 °C 这一可验证的共用系统底线数值。

### nA-08 地漏清洁的四个防溅要点 + 溢水处置五步 + 人员换装要求
- 出处: VII.B（chunk 标题误标为 C. Sanitizers）；chunk: ck-e0bbb1e83fca（另见 ck-09084c3dfe50）
- 原文关键句: "Using brushes that are at least ¼ inch (0.64 cm) smaller than the diameter of a drain opening to prevent splattering during cleaning of floor drains"；"Avoiding use of high-pressure hoses to clear or clean a drain, because use of such hoses could create aerosols"
- 中文大意：地漏清洁须避开 RTE 加工/暴露时段与未使用包装在场时段；禁高压水管疏通或清洗（气溶胶扩散）；刷子直径至少比地漏开口小 **1/4 英寸（0.64 cm）** 以防飞溅；加挡水板；地漏专用工具须色标区分。溢水处置五步：停产→移走受影响区所有未覆盖 RTE 食品→疏通地漏→用有效清洁剂清洁并冲洗消毒→清除地面余水；清洁地漏的人员须换衣换手套并洗手消毒后才可接触 FCS；使用杀菌型地漏环者须监测并适时更换。
- 类型: procedure / threshold
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 3 排水沟 + 卫生分区）
- 为什么是现有技能缺口: 现有卡只在"工厂设计"层面提排水沟（归属其他代理），无**清洁动作层面的地漏作业规则与 1/4 英寸刷具判据**。

### nA-09 消毒剂选择判据、轮换策略与"必须接触缝隙和 niche"
- 出处: VII.C；chunk: ck-e0bbb1e83fca
- 原文关键句: "Rotating sanitizers has been reported to provide for greater long term effectiveness and prevention of Listeria monocytogenes becoming established in niches in the environment and in forming biofilms. However, the most important considerations for selecting a sanitizer include: regulatory approval for the intended purpose, efficacy against the target organism, and efficacy under conditions of use (concentration, temperature, pH, and water hardness)."
- 中文大意：QAC、过氧乙酸、碘、氯均被用于控制李斯特菌；QAC 对李斯特菌有效且在表面留有残留杀菌作用，过氧乙酸已被证明对含李斯特菌的生物膜有效；**轮换使用消毒剂**据报有助长期有效并防止在 niche 定殖与形成生物膜；选择消毒剂的首要考虑为：目标用途的法规批准、对靶菌效力、使用条件（浓度/温度/pH/水硬度）下的效力；须确保消毒剂与被消毒表面接触，**包括缝隙与 niche**；消毒剂受 FIFRA 注册管理，按产品标签使用条件施用。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 3 消毒剂选择）
- 为什么是现有技能缺口: 现有卡只有"按 EPA 注册标签使用、清洁先于消毒"；未给候选药剂清单、轮换策略、残留效应、生物膜有效性判据，也未点明"必须接触 niche"这一与 resident 定殖直接相关的施用要求。

### nA-10 蒸汽/热水用于难清洁的架子设备，并作为针对 harborage site 的强化卫生手段
- 出处: VII.A.4（chunk 标题误标为 F. Relevant Sections）；chunk: ck-849cc429dc91
- 原文关键句: "You can use hot water or steam to sanitize racks and equipment that are difficult to clean. Using hot water or steam also can enhance sanitation efforts when addressing harborage sites for Listeria monocytogenes."
- 中文大意：可用热水或蒸汽对难以清洁的架子与设备消毒；热水/蒸汽也能强化针对李斯特菌藏匿点（harborage site）的卫生措施。
- 类型: procedure
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5 强化卫生程序 / resident 处置）
- 为什么是现有技能缺口: 现有卡提"拆机清洁、深入 niche"，但未给出可用的物理强化手段（蒸汽/热水）这一具体工具选项。

### nA-11 卫生监测与卫生记录的四类留痕（附 Part 117 条款映射）
- 出处: VII.D / VII.E / VII.F；chunk: ck-df4c057f4daf、ck-89531a7ee9ba、ck-8bae7134d09f
- 原文关键句: "We recommend that you establish and maintain sanitation records that document: Your written sanitation procedures; Your written procedures for monitoring sanitation conditions and practices; Your sanitation monitoring; and Corrections of monitored sanitation conditions and practices that are not implemented in accordance with your written sanitation procedures."
- 中文大意：卫生记录须含四类——书面卫生程序、书面卫生监测程序、卫生监测结果、以及对不符合程序的卫生状况与实践所作的纠正。监测要求三条：建立并实施含频次的书面程序；加工过程中以足够频次监控卫生状况与实践以确保 FCS 清洁并防止交叉污染；及时纠正不符合程序的情形。Part 117 映射：一般卫生程序 117.35(a)、117.35(d)(1)、117.135(d)(3)、117.80(c)(1)(c)(7)；地漏 117.10(b)(1)(b)(3)、117.35(a)、117.37(b)(3)；消毒程序与溶液 117.35(a)(b)(d)(1)(d)(2)；卫生监测 117.35(a)、117.145；卫生记录 117.145(c)、117.190。
- 类型: procedure / rule
- 建议归属: 并入 `management-components`（Step 1/Step 5 记录与监控）+ `environmental-pathogen-sanitation`
- 为什么是现有技能缺口: 现有卡把环境监测归为 verification 活动，但**卫生程序本身的记录字段**与 Part 117 条款号未列；且缺少"卫生监测"作为独立监控活动（与 EM 不同）的记录要件。

### nA-12 环境监测的三个目标与三段式设计（优于仅做产品检测）
- 出处: XIII.A；chunk: ck-4d1f6c0f0e58
- 原文关键句: "The goal of an environmental monitoring program is to: Verify the effectiveness of your control programs for Listeria monocytogenes; Find Listeria monocytogenes and harborage sites if present in your plant; and Ensure that corrective actions have eliminated Listeria monocytogenes and harborage sites when found in your plant."
- 中文大意：三目标＝验证控制措施有效性；找出厂内的李斯特菌与藏匿点；确认纠正措施已消除李斯特菌与藏匿点。设计三要素＝从 FCS 与 non-FCS 采样→检测识别潜在污染源→检出时采取适当纠正措施。良好的 EM 程序能提升对"可导致产品污染的环境状况"的认知，比仅做产品检测更有效。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5 环境监测设计）
- 为什么是现有技能缺口: 现有卡 Step 5 只讲"监测设计/法定充分性判准/分诊判定"，未把"EM 优于产品检测"这一比较结论与"第三目标=确认纠正措施已消除藏匿点"这一闭环判据写出。

### nA-13 建立监测策略的六个风险问题（Table 3）→ 低/高风险 → 采样频次与纠正严格度
- 出处: XIII.B；chunk: ck-677d93c65d79
- 原文关键句: "In general, the greater the risk that an RTE food could become contaminated with Listeria monocytogenes and support growth of the organism, the greater the frequency of environmental sampling and testing, and the more stringent the corrective actions if you detect Listeria spp."
- 中文大意：六问（表3）逐条 Yes/No 判定高/低风险：①食品是否接受充分的李斯特菌致死处理 ②配方是否抑制李斯特菌生长或致死（pH、水活度等内在特性）③减菌步骤后至包装前的处理量（少=低风险，多=高风险）④包装内是否有李斯特菌控制措施 ⑤冷藏货架期长短（短=低风险）⑥包装后食品在常规储存条件下是否支持生长（否=低风险）。风险越高 → 采样频次越高 + 检出后纠正措施越严格。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5），可与 `hazard-analysis-method` 交叉引用
- 为什么是现有技能缺口: 现有卡没有"风险分级 → 频次/严格度"的可操作评分器；这是把危害分析结论转化为采样方案的具体问句集。

### nA-14 四区（Zone 1–4）分区示例与"无分区系统时的替代要求"
- 出处: XIII.C（表4）；chunk: ck-a4c213694388、ck-fbeb6a78b06b
- 原文关键句: "If you do not establish and use a zone-based system, we recommend that you otherwise characterize areas where you will collect environmental samples according to potential for contamination, and that you distinguish between FCSs and non-FCSs."
- 中文大意：Zone 1＝食品接触面（器具、台面、切片机、管道内壁、罐内壁、灌装碗、包装与输送机、料斗）；Zone 2＝紧邻食品与 FCS 的非接触面（设备外壳/框架、部分墙面地面与地漏、紧邻 FCS 的推车）；Zone 3＝较远的非接触面（叉车、手推车、生产区内或附近的部分墙面地面与地漏），它们可污染 Zone 1/2；Zone 4＝生产区外的远端非接触面（更衣室、食堂、生产区外走廊、原料或成品储运区外区域），是病原进入加工环境的入口。不建分区系统时，仍须按污染潜势表征采样区域并区分 FCS / non-FCS。
- 类型: tool
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 4 卫生分区）
- 为什么是现有技能缺口: 现有卡 Step 4 只给"按设施/产品/危害分析划定敏感区边界"的定性规则，无**可直接照抄的四区定义与实例**，也无 Zone 4"外部引入源"的定位概念。

### nA-15 书面环境监测程序必须写明的七项内容
- 出处: XIII.D；chunk: ck-fbeb6a78b06b
- 原文关键句: "Your written procedures should: Be scientifically valid; Specify whether you are testing for Listeria spp. or Listeria monocytogenes; Identify the locations from which samples will be collected and the number of sites to be tested …; Identify the timing and frequency …; Identify the test(s) conducted, including the analytical method(s) …; Identify the laboratory you are using …; and Include corrective action procedures you will use when Listeria spp. or Listeria monocytogenes is found."
- 中文大意：书面 EM 程序七要素——科学有效；明确检测目标是 Listeria spp 还是 L. monocytogenes；采样位置与例行监测的点数（数量与位置须足以判定李斯特菌控制措施是否有效）；采样时机与频次（同样须"足以判定控制有效"）；检测项目与分析方法；检测实验室；以及检出 Listeria spp 或 L. monocytogenes 时的纠正措施程序。
- 类型: procedure
- 建议归属: 并入 `management-components`（Step 1/Step 4 书面化与验证）+ `environmental-pathogen-sanitation`（Step 5）
- 为什么是现有技能缺口: 现有卡引〔§ 117.165(b)(3)〕说明"点位数量/位置/时机/频次"须足以判定有效性，但**七要素全文清单**与其余五项（方法、实验室、纠正措施、目标菌、科学有效性）在现有卡未列。

### nA-16 为什么常规监测检 Listeria spp 而不是 L. monocytogenes（含阳性不等于 L. mono 的法律含义）
- 出处: XIII.D.2；chunk: ck-73765899c847
- 原文关键句: "We recommend that you test for Listeria spp. because doing so will detect both Listeria monocytogenes as well as species of Listeria that are more common than Listeria monocytogenes and allow you to correct situations that could potentially lead to contamination with Listeria monocytogenes. A positive test result for the presence of Listeria spp. on an FCS or a non-FCS does not establish the presence of Listeria monocytogenes on an FCS or non-FCS."
- 中文大意：检 Listeria spp 能同时检出 L. monocytogenes 与更常见的其他 Listeria 种，从而在"可能导致 L. mono 污染"的情形出现前就纠正；FCS 或 non-FCS 上 Listeria spp 阳性**并不等于**该表面存在 L. monocytogenes，但说明存在 L. mono 污染的潜势，且环境条件适合 L. mono 存活和/或生长。Part 117 允许在适当情形下以适当指示菌（如 Listeria spp）替代 L. mono 做环境监测〔§ 117.165(a)(3)〕。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）+ `management-components`（Step 4 验证活动裁剪）
- 为什么是现有技能缺口: 现有卡未区分"指示菌 Listeria spp"与"目标菌 L. mono"两个角色，也未给出"指示菌阳性的正确解读边界"（不是 L. mono 阳性，但必须处置）——这是判定"何时需要做菌种判定"的前提。

### nA-17 采样点位数量下限与"周期内测完全部点位"的程序设计
- 出处: XIII.D.3；chunk: ck-f71a9c177cf9
- 原文关键句: "We recommend that even the smallest processors collect samples from at least 5 sites of FCS and 5 sites of non-FCS on each production line for RTE foods."；"We recommend that such a program be designed to test all sites on the list within a defined period of time, e.g., one month."
- 中文大意：点位数量按厂区规模、设施特征、产品流、RTE 食品特性、加工方法与既往采样结果确定；Zone 1、2 点位通常更多（污染风险更高）；**即使最小的加工者**，每条 RTE 产线也应至少采集 **5 个 FCS 点位 + 5 个 non-FCS 点位**；若采用"从候选清单随机抽 N 个"的做法，程序须设计为在明确周期内（如 1 个月）把清单上**全部点位**都测一遍。
- 类型: threshold / procedure
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）
- 为什么是现有技能缺口: 现有卡只有"点位偏少即不合格"的定性问题，无最小点位基数与"随机抽样须配全测周期"的程序约束。

### nA-18 长期全阴时必须修订监测程序（防止漏掉污染源）
- 出处: XIII.D.3；chunk: ck-f71a9c177cf9
- 原文关键句: "If you consistently see negative test results in environmental samples collected from your plant, we recommend that you revise your environmental monitoring procedures to add, substitute, or both add and substitute other surfaces in your plant for sample collection and testing to ensure you are not missing a source of contamination."
- 中文大意：由于 L. mono 在环境中普遍存在、已从食品包装与加工环境中分离、并在设备与加工环境的藏匿点中持续存在，偶发检出 Listeria spp 属预期；但若持续全阴，应修订监测程序，增补/替换厂内其他表面继续采检，以确保没有漏掉污染源。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（B5 "监测阴性不证明环境无病原"）
- 为什么是现有技能缺口: 现有卡只把"阴性不等于无病原"作为边界提醒，未给**全阴情形下程序必须主动改版**这一动作要求。

### nA-19 采样时机：生产开始后 3–4 小时或清洁前；过早采样会因消毒剂未中和而干扰检测
- 出处: XIII.D.4；chunk: ck-eb954eb61140
- 原文关键句: "The most important time to collect environmental samples is at a time that is several hours into production (e.g., 3 to 4 hours) or preferably just prior to cleanup, because this allows time for Listeria monocytogenes (if present) to work its way out of harborage sites and contaminate the environment, the processing line …"
- 中文大意：最应采样的时点是投产数小时后（如 3–4 小时）或最好在清洁前——这样给 L. mono（若存在）时间从藏匿点逸出并污染环境、产线（含 FCS 点位）及潜在 RTE 产品；若采样紧贴消毒之后，消毒剂可能未被充分中和而干扰分析检测。
- 类型: procedure / threshold
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）
- 为什么是现有技能缺口: 现有卡讲"取样时机须足以判定有效性"的法定标准，但没有**具体时点数值**、也没有"消毒剂残留会假阴性"这一方法学陷阱。

### nA-20 采样频次区间与两套可照抄的书面频次方案（FCS / non-FCS）
- 出处: XIII.D.4；chunk: ck-eb954eb61140
- 原文关键句: "We recommend the lowest frequency (e.g., monthly) of routine sample collection be for those RTE foods that do not support growth of Listeria monocytogenes. We recommend that the highest frequency (e.g., weekly) of routine sample collection be for those RTE foods that support growth of Listeria monocytogenes."
- 中文大意：常规频次按风险定；最低档＝不支持生长的 RTE 食品每月；最高档＝支持生长的 RTE 食品每周；发现 Listeria spp 阳性须提高频次。**FCS 方案示例**：工厂运行时至少每周从指定 FCS 采样一次，且工厂内每个 FCS 至少每月测一次。**non-FCS 方案示例**：Zone 2 每周、Zone 3 每两周、Zone 4 每月各采代表性点位一次，且监测计划中列出的全部 non-FCS 点位至少每季度测一遍。
- 类型: threshold / procedure
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）
- 为什么是现有技能缺口: 现有卡无任何具体频次数值与"周/月/季"节律；这是写 FSP 环境监测频次条款时最直接可用的数值。

### nA-21 合样上限 5 个，且定位污染源时禁止合样
- 出处: XIII.D.5；chunk: ck-5758babfb8b7
- 原文关键句: "you should not composite more than 5 environmental samples, because methods have not been validated to show that this does not reduce the sensitivity of detecting the presence of the organism… we do NOT recommend compositing environmental samples when the purpose of your sampling is to locate the source of contamination (e.g., if you are conducting follow-up sampling after finding a positive test result)."
- 中文大意：单个样品检测或合并检测均可，但**合样不得超过 5 个**（方法未经验证证明超过 5 不会降低检出灵敏度）；生产中取样时合样须在投产 3–4 小时后；**以定位污染源为目的的采样（含阳性后跟进采样）禁止合样**；FCS 一般也不合样（合样会延长污染源识别时间）。
- 类型: threshold / rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）+ `management-components`（Step 4 验证活动）
- 为什么是现有技能缺口: 现有卡未涉及环境样品的合样规则与 5 个上限，也未区分"例行监测可合样/溯源不可合样"。

### nA-22 实验室资质核查要点（ISO 17025 参照）
- 出处: XIII.D.6；chunk: ck-c998b99df607
- 原文关键句: "One way to do so is to determine whether the laboratory is accredited (e.g., to a laboratory testing standard such as ISO 17025). Because multiple, scientifically-valid analytical methods could be available for a particular application, the analytical methods used could differ among laboratories."
- 中文大意：可用自有实验室或外部商业实验室；书面程序中须指明所用实验室；须确认实验室掌握**当前最科学有效**的适用于环境样品的方法，核实方式之一是查其是否获得认可（如 ISO 17025）；因存在多种有效方法，不同实验室所用方法可能不同（故须在程序中写明方法而非默认）。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）+ `supply-chain-verification`（参照其第三方验证独立性铁律）
- 为什么是现有技能缺口: 现有卡完全没有"环境监测实验室资质/方法一致性"的核验动作（供应链卡有独立性铁律，环境监测这边是空白）。

### nA-23 纠正措施的风险化四个维度与措施类型库
- 出处: XIII.D.7；chunk: ck-ec52c429de28
- 原文关键句: "We recommend that your corrective action procedures be risk-based from the perspectives of: The environmental monitoring strategy for the food; Whether the environmental contamination is on an FCS or a non-FCS; Whether testing environmental samples results in an isolated positive result or multiple positive results; and The proximity of a contaminated non-FCS to FCSs."
- 中文大意：书面纠正措施程序须写明步骤并指派责任人，确保找到并纠正污染原因、尽量降低任何来源（设备、人员、加工或包装环境）导致 RTE 食品被污染的潜势；风险化从四维度判断：①该食品的监测策略 ②污染在 FCS 还是 non-FCS ③孤立阳性还是多点阳性 ④被污染 non-FCS 与 FCS 的邻近度。措施类型库：强化清洁消毒、强化采样检测、根因分析、"留置并检测"（hold and test）。指南声明不可能穷举全部情形，行动须基于食品被污染与致病的风险。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5 两态处置）+ `management-components`（Step 3 纠正措施）
- 为什么是现有技能缺口: 现有卡的分诊判据是"时间持续性+株型指纹"，本指南给的是**四维风险化框架**（含"孤立 vs 多点""non-FCS 与 FCS 距离"），两者可互补；现有卡未给措施类型库，也未把"isolated vs multiple positives"写成判定输入。

### nA-24 non-FCS 阳性的升级决策树（Zone 2 为重点）
- 出处: XIII.E；chunk: ck-d496a5eb6369、ck-977b46371f34
- 原文关键句: "If the follow-up samples are negative for Listeria spp., assume the contamination has been eliminated and resume routine environmental monitoring during subsequent production."；"If any of the follow-up samples show the presence of Listeria spp. (i.e., if you obtain a second positive result), conduct intensified cleaning and sanitizing, with intensified sampling and testing to identify the source of the contamination."
- 中文大意：程序为——①收到 routine non-FCS 阳性通知后，在**生产结束时**对该点位及周边区域重点清洁消毒，并在**下一次生产运行中至少 3 小时后**复检该点位及周边区域；②复检全阴 → 假定污染已消除，恢复常规监测；③出现第二次阳性 → 强化清洁消毒 + 强化采样检测；④支持生长的食品，强化措施可包括**拆解**受影响或潜在受影响设备，**在清洁消毒之前**先采样检测拆解暴露面以判定来源；不支持生长的食品，除非第二次阳性后又出现第三次阳性，否则较少拆解设备；⑤强化采样仍非全阴 → 做根因分析、升级缓解措施、并考虑咨询李斯特菌控制专家，采取基于风险行动查清点位如何被污染（如判定/修复或更换损坏设备与厂房构造），必要时参考 XIII.F 的综合调查。Zone 3、4 阳性同样要处置以防向 Zone 1/2 迁移，但可较 Zone 2 宽松。复合样阳性时须追加检测定位具体点位，或按该合样代表的每个点位均阳性处置。
- 类型: procedure
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5 升级路径）
- 为什么是现有技能缺口: 现有卡只给"transient→常规清洁+追溯 / resident→强化卫生程序"两级路径，无**按阳性次数递进（1→2→3）**的具体动作序列与时点（生产结束时清洁、次生产 3 小时后复检）。

### nA-25 "强化采样"与"强化清洁消毒"的定义（可判定，非口号）
- 出处: XIII.E 脚注 12、13；chunk: ck-977b46371f34
- 原文关键句: "The follow-up samples should include the positive site and at least 3 surrounding sites, which could include both FCSs and non-FCSs in close proximity to the positive site."；"Intensified cleaning and sanitizing includes sanitation measures that are performed in addition to normal sanitation procedures and are escalated in response to continuing findings of positives … can include increasing the frequency of cleaning and sanitizing for certain pieces of equipment, breaking down the equipment into its parts for further cleaning, and steam treating equipment."
- 中文大意：强化采样＝对阳性点位**及其至少 3 个周边点位**采集跟进样（可含邻近的 FCS 与 non-FCS）。强化清洁消毒＝在常规程序之外、因持续阳性而升级的措施，具体形态包括：提高特定设备的清洁消毒频次、把设备拆成零件进一步清洁、蒸汽处理设备。
- 类型: procedure / threshold
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）
- 为什么是现有技能缺口: 现有卡用"强化卫生程序"这一词但未定义其构成与判定边界（周边点位数量、拆解、蒸汽、加密频次）。

### nA-26 FCS 阳性的升级决策树与解除条件（连续 3 日阴性）
- 出处: XIII.F.1；chunk: ck-31ea7af3b3c6
- 原文关键句: "When you receive notification of a positive result of a routine sample for an FCS site, pay particular attention to cleaning and sanitizing that site at the end of production and retest the FCS and surrounding area … at least 3 hours into the next production run."；"If results from the product lot that was tested … are negative for Listeria monocytogenes and the retest of the FCS is negative for three sequential days, release that product lot."
- 中文大意：①FCS routine 阳性 → 生产结束时重点清洁消毒该点位，并在**下次生产至少 3 小时后**复检该 FCS 及周边；②跟进样全阴 → 假定已消除，恢复常规监测；③第二次 FCS 阳性 → 强化清洁消毒（含可行时拆解设备，**拆解暴露面须在清洁消毒前采样检测**）+ 强化采样检测 + 按情况执行 hold and test（支持生长的食品：按统计学抽样方案、以企业按风险自定的置信水平检测，例如"若存在则以 95% 置信度检出"；不支持生长的食品：基于污染可能性与消费者风险考虑是否 hold and test）+ 做综合调查以查明并缓解来源、修改程序；④**接下来的两个生产日**继续强化措施并**留置这两天产品**（处置取决于 FCS 环境检测结果与前一日产品检测结果）；⑤产品阴性且 FCS 复检**连续 3 天阴性** → 放行该批；⑥全部 FCS 样品在**3 个连续生产日**均阴性 → 恢复正常生产、放行其余留置产品、回到常规监测。指南假设"一批（lot）"= **一条产线一天的产量**，批间进行清洁消毒。
- 类型: procedure / threshold
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）+ `management-components`（Step 3 受影响范围与解除条件）
- 为什么是现有技能缺口: 现有卡讲"判据是时间持续性+株型指纹"，无**连续 3 日阴性作为解除条件**、无"两日留置"这类具体时序、无"lot=一天产量"的批定义。

### nA-27 第三次阳性＝判定存在藏匿点（harborage site）：停产 + 专家 + 连续 3 次阴性才复产
- 出处: XIII.F.1；chunk: ck-31ea7af3b3c6
- 原文关键句: "If a follow-up sample from intensified sampling and testing continues to detect Listeria spp. (third positive) on an FCS site, assume that you have a harborage site."
- 中文大意：第三次阳性 → **假定存在藏匿点**。对支持生长的食品：**停产**，咨询熟悉工厂内李斯特菌污染排查的食品安全专家做综合调查并据其建议采取措施；纠正措施完成后复产，须 hold and test 产品并持续强化采样检测，直到 FCS 与产品**连续三次阴性**。对不支持生长的食品：第三次 FCS 阳性后采取与"支持生长食品第二次阳性"相同的措施（含同样的 hold and test 程序）。
- 类型: rule / threshold / procedure
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5 resident 定殖判定 + 停产决策）
- 为什么是现有技能缺口: 现有卡的 resident 判定靠"同点位反复检出同型菌株"这一**推断**，本指南给出**次数阈值 + 停产门槛 + 复产验证条件**——这是"何时判定为需要全面停产清理"这个问题的直接答案，现有卡未回答。

### nA-28 hold and test 的 ICMSF 抽样方案表与 25 g 建议
- 出处: XIII.F.3（表5）；chunk: ck-4e07897db1ec、ck-e10b0750b2c1
- 原文关键句: "We recommend analyzing a 25 g sample. If the risk of the population is unknown, we recommend that you use cases 13-15."
- 中文大意：ICMSF 按风险把危害分三级（Moderate/Serious/Severe）；L. mono 在普通人群食品中属 Serious、在高危人群（医院、养老院）食品中属 Severe，**不存在适用 Moderate 的情形**；15 种抽样方案中，Serious 用 case 10/11/12，Severe 用 case 13/14/15（case 13–15 专门用于高度易感人群，因其中很大比例个体易感，故加严）。表5（n=样品数，c=允许阳性数）：case 10 n=5,c=0（平均浓度 1 cfu/32 g）；case 11 n=10,c=0（1 cfu/83 g）；case 12 n=20,c=0（1 cfu/185 g）；case 13 n=15,c=0（1 cfu/135 g）；case 14 n=30,c=0（1 cfu/278 g）；case 15 n=60,c=0（1 cfu/526 g）。三档条件含义：条件降低风险（食用前加热灭活）、条件不变风险（既不死亡也不增殖）、条件增加风险（可在 L. mono 增殖条件下存放）。建议分析 **25 g** 样品；人群风险未知时用 case 13–15。留置检测的样品应在**一天内**采完，受影响产品在检测期间全部留置；检测可用 Listeria spp 或 L. monocytogenes；一旦出现任何阳性，须做更深入的污染原因调查与更严格的纠正措施。
- 类型: threshold / procedure / tool
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5 升级路径）+ `process-control-validation` 或新增"L. mono 留置检测抽样"子节
- 为什么是现有技能缺口: 现有卡完全无产品留置检测的抽样方案数值（n/c/浓度），也未说明食品检测应检 L. mono 而环境检测宜检 Listeria spp 的方向性差异。

### nA-29 单个采样期内多点阳性的整体判读（卫生程序不足 + 可能已建立藏匿点）
- 出处: XIII.F（Figure 2 说明）；chunk: ck-fee12f3c7760（另见 ck-df0a88553668）
- 原文关键句: "Detecting Listeria spp. at several FCS sampling locations during the same sampling period could indicate that your routine sanitation procedures are inadequate, and could indicate that the Listeria spp. has become established in one or more harborage sites that are FCS or in Zone 2 nearby FCS."
- 中文大意：同一采样期内多个 FCS 点位同时阳性 → 可能意味着常规卫生程序不充分，且可能已在 FCS 或邻近 FCS 的 Zone 2 的一个或多个藏匿点定殖；**污染 FCS 点位越多，污染向食品交叉污染的风险越大**；此时应立即复核书面卫生程序、落实更有效的例行卫生程序、升级纠正措施并做根因分析。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）
- 为什么是现有技能缺口: 现有卡分诊判据是"点位持续性"（时间维度），本指南补充**同一期内横向分布密度**这一维度（数量→风险），两者构成互补判据。

### nA-30 多次出现在同一区域 → 根因分析并评估卫生程序有效性（不必区分是否 L. mono）
- 出处: XIII.F；chunk: ck-df0a88553668
- 原文关键句: "In general, there is minimal value in determining whether Listeria spp. detected on a non-FCS is Listeria monocytogenes, because you should eliminate the Listeria spp. regardless of whether it is Listeria monocytogenes."
- 中文大意：non-FCS 上一般**没有太大必要**去判定是否 L. monocytogenes（无论是不是都要清除）；若在 non-FCS 或同一大致区域的**多个不同场合**再次发现 Listeria spp，须做根因分析查清该区域为何持续产出阳性，并采取消除污染的行动（如评估现行卫生程序的有效性并据此修改）；须建立并保存所有纠正措施记录。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5 两态处置 + 记录）
- 为什么是现有技能缺口: 现有卡把"株型指纹一致性"作为 resident 判据，但未指出**指示菌层面无需分型**这一实务简化（减少不必要的分型投入），也未给"多次出现"与"单次出现"在决策上的差别。

### nA-31 纠正措施汇总矩阵（Table 6：4 档阳性 × FCS/non-FCS × 支持生长/不支持生长）
- 出处: XIII.G（表6）；chunk: ck-28faf6170a79、ck-e45938e79e0d
- 原文关键句: "For each type of surface (i.e., non-FCS and FCS), Table 6 also compares the corrective actions for growth foods to the corrective actions for non-growth foods."
- 中文大意：矩阵维度＝①常规采样阳性 #1 ②跟进采样阳性 #2 ③跟进采样阳性 #3 ④跟进采样阳性 #4 × {non-FCS, FCS} × {支持生长, 不支持生长}。要点：#1 一律"清洁消毒该区域 + 下个生产周期复检"，FCS 再加"综合调查"；#2 non-FCS 为"强化清洁消毒 + 强化采样检测"，FCS 再加"留置检测产品 + 产品阳性则再加工/改用途/销毁 + 综合调查"，不支持生长的 FCS 改为"考虑留置检测"；#3 non-FCS 为"根因分析"，FCS 支持生长为"停产并咨询专家做综合调查 + 升级强化清洁消毒（如蒸汽处理设备）+ 强化采样 + 复产后 hold and test 直至产品与 FCS 连续 3 日阴性"，不支持生长的 FCS 走与"支持生长第二次阳性"同等的 hold and test 与综合调查；#4 仅列在"不支持生长的 FCS"→"停产并咨询专家做综合调查"。
- 类型: tool / procedure
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5，建议以表格化工具形式落地）
- 为什么是现有技能缺口: 现有卡的两态处置是叙述性二分，没有可打印执行的**分档决策矩阵**；这张表是可直接改写为厂内 SOP 的骨架。

### nA-32 高危人群用途的非生长食品按生长食品同等严格处置
- 出处: XIII.F / 表6 注；chunk: ck-d496a5eb6369（XIII.F 段）、ck-e45938e79e0d
- 原文关键句: "we recommend that for a food that does not support growth and that is specifically intended for establishments such as hospitals and nursing homes (where the food would be consumed by populations at high risk for listeriosis), you take corrective actions in a similar manner as for foods that support growth."
- 中文大意：不支持李斯特菌生长、但专供医院与养老院等高危人群的食品，其纠正措施应与支持生长的食品**同等严格**。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）+ `hazard-analysis-method`（易感人群加权）
- 为什么是现有技能缺口: 现有卡的风险二分只按"支持生长/不支持生长"，未处理"人群易感性"这一维度的降级约束（这是为何"不支持生长"可以降档的唯一例外）。

### nA-33 FCS 阳性后"何时需要判定是否为 L. monocytogenes"的判据
- 出处: XIII.F.2；chunk: ck-957334e01bc5
- 原文关键句: "In general, the greater the risk of foodborne illness presented by the RTE food being produced on an FCS that has tested positive for Listeria spp., the greater the importance of determining whether any Listeria spp. you detect on an FCS is Listeria monocytogenes."
- 中文大意：书面纠正措施程序须规定"FCS 检出 Listeria spp 后何时去判定它是否为 L. monocytogenes"；一般规律＝该 FCS 上生产的 RTE 食品带来的食源性疾病风险越大，判定越重要。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）
- 为什么是现有技能缺口: 现有卡未区分"指示菌阳性必须处置"与"是否需要追加菌种判定"两个层次，也未给判定必要性的风险依据。

### nA-34 监测程序的周期性加密验证（点位设置是否合适要自己验）
- 出处: XIII.D.8；chunk: ck-93ec955ffca9、ck-b64944015876
- 原文关键句: "We recommend that you periodically verify your written environmental monitoring procedures by increased and intensive environmental sampling of the plant to assess whether the sampling sites are appropriate."
- 中文大意：应周期性通过**加密、加深的全厂环境采样**来验证书面 EM 程序，评估采样点位设置是否适当。
- 类型: procedure
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）+ `management-components`（Step 4 verification）
- 为什么是现有技能缺口: 现有卡把 EM 归为 verification 活动，但未提"验证 EM 程序本身（点位设置）"这一元层验证动作。

### nA-35 趋势分析的三类上升信号（含"非连续多次出现"这一关键模式）
- 出处: XV.A；chunk: ck-e67680f96bf6（另见 ck-f758a81be9c0）
- 原文关键句: "Examples of trends that could indicate that Listeria monocytogenes in your plant is not being controlled are: Increases in positive environmental samples in particular sites or areas; Finding Listeria in the same area on multiple but non-consecutive sampling occasions (e.g., positive one week and negative the next, appearing to be isolated positives); and An increase in the percentage of overall positive environmental samples in the plant."
- 中文大意：三类趋势信号＝①特定点位或区域阳性样品数上升；②**同一区域在多个非连续采样场合反复出现**（例：本周阳性、下周阴性，看似孤立阳性）；③全厂阳性环境样品百分比上升。即使已对个别阳性点位采取适当纠正措施，若该区域持续产出阳性，仍可能意味着存在**未识别的藏匿点**，应做更完整的调查；若趋势分析显示厂内 Listeria spp 发生率上升，须调查原因并采取纠正措施降低发生率。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5 趋势）+ `management-components`（Step 6 再分析触发）
- 为什么是现有技能缺口: 现有卡只用"同一点位反复检出同型菌株"识别 resident，未识别**"隔周交替式非连续重复"这一最具迷惑性的模式**，也未给"全厂阳性率"作为可跟踪的总体指标。

### nA-36 趋势分析的用途定义与产品检测趋势的历史基准作用
- 出处: XV.A / XV.B；chunk: ck-f758a81be9c0、ck-2b1cc488789d
- 原文关键句: "we recommend that you analyze the data you collect through your environmental monitoring program over time for trends that can help you to continuously improve sanitation conditions in your plant by reducing the percentage of overall positive environmental samples in your plant."
- 中文大意：趋势分析的目标指标＝**降低全厂阳性环境样品百分比**，用于持续改进工厂卫生状况；趋势分析本身可作为"李斯特菌未被控制"的证据（例如某 resident 菌株已在 niche 环境定殖），从而触发控制措施。产品检测趋势：定期抽检 RTE 食品可提供工厂的历史绩效参考，验证 L. mono 控制随时间的充分性；若产品阳性率上升，须调查原因并采取纠正措施降低发生率。
- 类型: rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（Step 5）+ `management-components`（Step 6）
- 为什么是现有技能缺口: 现有卡无趋势分析这一验证工具；`management-components` 提到记录可用于趋势分析但未给分析对象与指标定义。

### nA-37 趋势分析结果本身要留记录
- 出处: XV.C；chunk: ck-81d9ef93ac59
- 原文关键句: "We recommend that you establish and maintain a record of any trend analysis that you conduct."
- 中文大意：须建立并保存**所进行的任何趋势分析**的记录。
- 类型: procedure
- 建议归属: 并入 `management-components`（Step 5 记录）+ `environmental-pathogen-sanitation`
- 为什么是现有技能缺口: 现有卡记录清单只列程序/监控/纠正/检测结果四类，未把"趋势分析记录"列为独立记录类别。

---

## 二、近重复（现有技能已覆盖，本指南可补细则/出处）

- rA-01: **transient / resident 两态模型** ↔ 现有卡 `environmental-pathogen-sanitation` Step 5（"分诊判定：时间持续性+株型指纹一致性"）。本指南用词是 harborage site / niche（不区分 transient/resident），但给出**resident 判定的操作化门槛**：FCS 第三次阳性即"假定存在藏匿点"→停产+专家+连续三次阴性才复产（nA-27）。可把该门槛补为现有卡两态模型的**判定阈值**。
- rA-02: **湿区"尽量保持干燥"+禁高压水/压缩空气等扩散性清洁** ↔ 现有卡 Step 3 湿区三原则 / B3。可补的具体数值与判据：低压喷淋 <20 英尺、高压 <30 英尺、清洁帘或临时隔墙；RTE 暴露房间内禁止湿洗（含覆盖也不行）；共用 CIP 时碱性清洗液 ≥71 °C；共用 COP 时 RTE 侧 COP 尽量设在 RTE 区。
- rA-03: **卫生分区（hygienic zoning）** ↔ 现有卡 Step 4（"按设施、产品、危害分析输出划定敏感区边界"）。可补：Zone 1–4 的具体定义与实例、Zone 4 作为"外部引入源"的定位、以及"Zone 3/4 阳性也须处置以防向 Zone 1/2 迁移"。
- rA-04: **环境监测书面程序须规定点位数量与位置、时机与频次且足以判定有效性**〔§ 117.165(b)(3)〕 ↔ 现有卡 Step 5（法定充分性判准）。可补：最小 5 FCS + 5 non-FCS/产线、Zone1/2 点位更多、"周期内测完全部点位"、3–4 小时或清洁前采样、monthly/weekly 频次带、Zone2 周/Zone3 双周/Zone4 月/全部 non-FCS 季。
- rA-05: **监测阴性不证明环境无病原**（监测是趋势工具） ↔ 现有卡 B5。本指南补的是**动作**：持续全阴须修订程序增补/替换采样面（nA-18），且需周期性加密采样验证点位设置（nA-34）。
- rA-06: **阳性即触发 corrective action；书面程序须含纠正措施并指派责任人** ↔ `management-components` Step 3（分诊/corrective action 四步）。可补：风险化四维度（监测策略、FCS vs non-FCS、孤立 vs 多点、non-FCS 与 FCS 距离）、措施类型库（强化清洁/强化采样/根因分析/hold and test）、以及"指南不应穷举、须按风险自定"的边界声明。
- rA-07: **产品阳性的处置四路（再加工/转非食用/动物饲料/销毁）+ 考虑召回** ↔ `recall-plan`（SAHCODH 判定后 Class I/RFR 联动）与 `management-components` 处置阶梯。可补：hold and test 的 ICMSF 数值表（case 10–15 的 n/c 与平均浓度，25 g 样品）、"批=一条产线一天产量，批间清洁消毒"、以及"两次清洁消毒周期之间的批次视为被牵连"。
- rA-08: **环境监测须科学有效、可参考 BAM/ICMSF/APHA，实验室资质** ↔ `supply-chain-verification` 的第三方验证独立性铁律（独立性铁律在那张卡，方法学与实验室资质在本指南）。可补：BAM ch.10 快速筛查法、Appendix 5 采样制备方法、"Testing Methodology for Listeria species or L. monocytogenes in Environmental Samples"、ISO 17025 认可核查、合样不超过 5 个。
- rA-09: **记录字段与 Part 117 条款映射**（环境监测记录四类：书面程序含采样/制备/分析方法/纠正措施程序、纠正措施、检测结果） ↔ `management-components` Step 5 记录要件。本指南在 XIII.I 给出同一四类清单，可作为该卡记录清单的交叉引用出处。

---

## 三、潜在矛盾（现有技能说法 vs 本指南措辞不一致）

1. **"干式清洁优先" vs 七步湿式清洁程序**：现有卡 `environmental-pathogen-sanitation` Step 3 的湿区第一杠杆是"减少漫水"，通篇隐含"干式清洁优先"；本指南 VII.A.1（ck-df42de7cda8e）给出的是**固定的湿式七步序列**（干清只是第一步，随后必做预冲洗/泡沫清洗/冲洗），并在 VII.A.3 给出 CIP/COP 与湿洗场景的具体规范。两者不必然冲突（"减少漫水"≠"禁止湿洗"），但合并时须明确：现有卡的"干式优先"是**判据层**（在同等效果下优先保持干燥），本指南的"七步"是**湿式清洁的执行层**；不得让读者得出"L. mono 湿区不得湿洗"的误读（本指南只禁"在 RTE 暴露房间内湿洗"）。
2. **resident 判据机制不同（指纹/持续性 vs 阳性次数）**：现有卡 Step 5 明确"判据是时间持续性+株型指纹一致性，不是频次"；本指南的升级决策树完全按**阳性次数**递进（第一次→第二次→第三次），且未把株型指纹作为触发输入（仅在 XIII.F 提到多次出现在同一区域才做根因分析）。两者是**不同触发器**而非同一条判据：合并时应保留现有卡的"指纹一致性"作为**同点位同型重复**的判别器，同时引入本指南的"次数阶梯"作为**处置强度阶梯**，避免出现"指南说三次就停产、现有卡说看指纹"的对立表述。
3. **"监测设计"边界 vs 本指南的程序内细节**：现有卡 B4 明确写"Ch10 未发布……具体清洁程序细节（频次表、药剂清单、采样方案模板）须依赖其他资源"。本指南提供了附录 4 的例行清洁消毒时间表引用（ck-e758db4c9dc8）、药剂清单（ck-e0bbb1e83fca）与采样方案（ck-eb954eb61140），但**附录 4/5/6 的正文不在本次负责范围**，故 B4 的"缺口"只能部分关闭——合并时应把 B4 改写为"细节已由 L. mono 专项指南（VII/XIII/XV 章）补齐主体部分，附录 4/5/6 的表格模板仍待补"，不要直接删除该边界条目。
4. **"强化卫生程序"的构成未定义 vs 指南给出定义与物理手段**：现有卡 Step 5 把"强化卫生程序"当作既定动作（拆机清洁、深入 niche、根除调查），本指南额外定义了强度形态（加密频次、拆成零件、蒸汽处理）与边界（蒸汽/热水用于难清洁架子设备）。属于补充而非矛盾，但若不写入定义，现有卡的"强化"仍不可执行。
5. **本指南的 should 层 vs 法规 must 层**：XIII.D.4 的频次数值（每周/每月/季度）、5+5 点位下限、Zone 划分等均为指南建议（should），〔§ 117.165〕只要求"足以判定有效性"。现有卡在 Step 5 已把后者标为 must 级判准；合并时须保持这一分层，不要把本指南数值升格为法定义务（现有卡 B6 的"should 与 must 分层阅读"原则须延续到本卡内容）。

（除上述外未发现其他实质冲突；两卡在"环境监测须书面化、须科学有效、记录四要素、污染后须做纠正措施并留痕"上完全同向。）

---

## 四、跨章节提示（属于其他代理负责的 IV/V/VI/VIII 章）

1. **人员控制**：XIII.F.1（ck-31ea7af3b3c6）要求"检查人员卫生程序依从性"、"审查人流模式与设备布局、人员在岗卫生程序"——具体的手/手套/鞋、泡脚器、干粉消毒剂、衣物与更衣管理要点属 V 章，建议由负责人员控制的代理出主卡，本卡仅留引用。
2. **工厂设计与气流/水系统/排水沟构型**：XIII.E 末段（ck-977b46371f34）"Repairing or replacing broken equipment and plant construction may be needed to remedy problems"、XIII.F.1 要求审查设备布局——排水沟坡度、地漏位置、空气压差与气流方向、冷凝水管理的设计要点属 VI 章；本清单只收了"地漏清洁作业规则"（nA-08），设计侧留给对应代理。
3. **附录章节需独立提取**：本指南的 **附录 1**（L. mono 污染源分类 A–E，XIII.F.1 明确引用 Categories C、D、E）、**附录 2**（污染原因情景，XIII.F.1 引用）、**附录 4**（例行清洁与消毒时间表）、**附录 5**（环境采样方法与样品制备）、**附录 6**（纠正措施）——均落在本次负责的三段之外，是填补现有卡 B4 缺口的最后一块，建议派专门提取。
4. **卫生运输**：XIII 章开头（ck-ca8730348639）交叉引用 21 CFR part 1 subpart O（§ 1.906 车辆与运输设备、§ 1.908 运输操作）与 117.93、117.130(c)(2)(iv)——属储运/供应链代理的交界，本卡不收。
5. **产品抽样与检测（XIV 章）**：XIII.F.3 的 hold and test 引用 XIV.A（ck-8ed5f7ced929：产品建议检 L. mono 而非 Listeria spp、留置范围为 cleanup to cleanup、程序须含频次与抽样方案）——与本清单 nA-28 配套，但 XIV 章主体归另一代理，本清单仅保留数值表作为交叉引用。
