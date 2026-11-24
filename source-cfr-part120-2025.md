# 21 CFR Part 120 — Hazard Analysis and Critical Control Point (HACCP) Systems (4-1-25 Edition)

> **来源**：用户提供的 `CFR-2025-title21-vol2-part120.pdf`（176 KB，10 页），GPO/eCFR 印刷版 **21 CFR Ch. I (4–1–25 Edition)**，书页 439–448；PDF 元数据 creator `govinfo, U.S. Government Publishing Office`、creationDate `D:20250806205406Z`、modDate `D:20250806170339-04'00'`。经本包专用脚本 `.cangjie/convert_cfr_part.py` 按「页 → 左栏 → 右栏」重排转出（本轮同时修订该脚本两处缺陷，见「转换局限」），再用 `.cangjie/fix_part120_reflow.py` 定点修 **11 处**段界缺陷。自检：**15/15 条款命中**（120.1 / .3 / .5 / .6 / .7 / .8 / .9 / .10 / .11 / .12 / .13 / .14 / .20 / .24 / .25）、页眉与独立页码残留 **0**、裁掉首部 Part 119 残段 3 段与尾部 Part 121 残段 6 段、串栏 0。
> ⚠ **版本口径**：`4–1–25 Edition` 是 CFR **年度编纂版次**（修订至 2025-04-01），**不是**「2025 年新规则」。Part 120 的 SOURCE 为 `66 FR 6197, Jan. 19, 2001, unless otherwise noted`；§ 120.3 与 § 120.6 条末为 `[66 FR 6197, Jan. 19, 2001, as amended at 80 FR 56167, Sept. 17, 2015]`，§ 120.5 条末为 `[80 FR 56167, Sept. 17, 2015]`——后者是 PCHF 最终规则的 conforming amendment，把原指向 Part 110 的接口改成 `parts 110 and 117`。引用写「21 CFR part 120（4-1-25 Edition）」，不得写成「2025 新规」。AUTHORITY 栏为 `21 U.S.C. 321, 342, 343, 346, 348, 371, 374, 379e, 381, 393; 42 U.S.C. 241, 242l, 264`。

## 效力层级与使用边界（导入说明，非原文）

- 本件是 **联邦法规正文**，具法律约束力，且是**独立的 HACCP 体系法规**——不是「果汁版的 Part 117」，也不是 Part 117 的子集。全包「法规正文层」现含 **六套独立编号体系**：〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕，互不混引。
- **与 Part 117 / Part 110 的接口（关键，只有一句，且是条件性的）**：〔§ 120.5〕`Except as provided by § 117.5(c), parts 110 and 117 of this chapter apply in determining whether the facilities, methods, practices, and controls used to process juice are safe, and whether the food has been processed under sanitary conditions.` —— 这决定了三件事：① **Part 117 是默认适用**，果汁企业不因受 Part 120 管辖就整体脱离 CGMP 与 PCHF；② 唯一的出口是〔§ 117.5(c)〕，它是**条件性**豁免（与 part 113 的 §117.5(d)、part 123 的 §117.5(b) 同构）；③ **§ 117.5(c) 的条文原话自 v4.14 起已在包内**（`books/_inbox/21-CFR-Part-117-2025.md`）：`Subparts C and G of this part do not apply with respect to activities that are subject to part 120 of this chapter (Hazard Analysis and Critical Control Point (HACCP) Systems) at a facility if you are required to comply with, and are in compliance with, part 120 of this chapter with respect to such activities.` —— **两个并列条件**（合规才成立），且该款**没有 (d)(2) 那样的范围限缩**，故 part 120 活动范围内的 Subparts C/G 要求全部移出、边界止于受 part 120 管辖的 activities。⚠ v4.13 曾因该文件未随仓库分发而标「转引未收」，v4.14 已闭环；全包 23 处〔§ 117.xxx〕引文经 `.cangjie/verify_v4_14_part117_quotes.py` 追溯核验 23/23 命中。
- **5-log 削减是法定要求，不是指南建议**：〔§ 120.24(a)〕用 `shall include in their HACCP plans control measures that will consistently produce, at a minimum, a 5 log (i.e., 10⁵) reduction`，且要求覆盖 **货架期** 与 **正常及中度滥用条件**。目标菌是「pertinent microorganism」＝**果汁中可能出现的最耐热、具公共卫生意义的微生物**。凡把这句降格成「FDA 建议 5-log」即为效力误判。
- **5-log 有两处法定豁免，但豁免的是「5-log」不是「整套 HACCP」**：〔§ 120.24(a)(1)〕受 part 113 / 114 管辖者；〔§ 120.24(a)(2)〕用**单次热力步骤**即达货架稳定，或用**含全部配料热处理的浓缩工艺**，且须把该热力工艺副本放进〔§ 120.7〕的书面危害分析。这两类企业仍要满足 Subpart A 的 SSOP、危害分析、HACCP 计划、纠正措施、验证、记录、培训全部义务。
- **与 part 113 / 114 的第二处接口在危害分析里**：〔§ 120.7(e)〕`HACCP plans for juice need not address the food hazards associated with microorganisms and microbial toxins that are controlled by the requirements of part 113 or part 114 of this chapter.` —— 豁免范围**只到「微生物与微生物毒素」**，其余危害（化学、物理、过敏原等）仍须在果汁 HACCP 计划里控制。这与 part 123 的〔§ 123.16〕只排一条、part 113 的〔§ 117.5(d)(2)〕只限微生物危害是同一类「有限豁免」结构，但**条款号与范围都不同，不得互相套用**。
- **果汁 HACCP 的记录复审是「1 周（7 天）」而非「7 个工作日」**：〔§ 120.11(a)(1)(iv)(A)(B)〕两次都用 `within 1 week (7 days)`。这与 Part 117 的记录复审时限（工作日口径）不同，两套不可混用；同款 (C) 的校准与成品/在制品检验记录则只要求 `within a reasonable time`。
- **记录保存期是又一套口径**：〔§ 120.12(d)(1)〕易腐或冷藏果汁 **≥1 年**（自产品制备日起）；冷冻／保藏／货架稳定产品 **2 年或货架期，孰长**。此前全包已有〔§ 108.25(g)〕整段 3 年、〔§ 108.35(h)〕1+2 年、〔§ 113.100(g)〕1+2 年、〔§ 114.100(e)〕整段 3 年、〔§ 123.9(b)(1)〕1 年／2 年——**Part 120 的起算点与「孰长」规则又是独立的第六套**，不得合并成「都是 3 年」或「都是 2 年」。
- **§ 120.9 直接给法律定性**：未建立并实施符合 §120.6 / §120.7 / §120.8 的 HACCP 体系，或未按本 part 其他要求运行，其果汁产品 **依 FD&C Act 402(a)(4) 构成掺假**。这是法条直接给结论，不需要再经由「不符合 CGMP」间接推导。
- **§ 120.25 是「表面处理」专项验证，不是通用取样要求**：它只适用于**依赖未与果汁全部部分接触的处理**（即果面处理）来达成 5-log 的加工者，要求对成品做 **biotype I 大肠埃希菌** 检测——20 mL 样品（两个 10 mL 子样）／每 1,000 加仑／每个生产日；日产量不足 1,000 加仑时按每 1,000 加仑取样但**不少于每 5 个工作日一次**。**7 次检测中 2 次阳性即「控制措施被视为不足」**，须立即改用能在压榨后达成 5-log 的替代工艺。把这条当作所有果汁厂的常规出厂检验，即为超范围适用。
- 引用规范：本件标〔§ 120.xxx〕，Part 117 标〔§ 117.xxx〕，Part 108/113/114/123 标各自编号；CP 7303.047（果汁 program）等检查程序**未收**，涉及检查员取证口径一律标「转引未收」。全包自 v4.7 起十二类、v4.8 起十三类、v4.9 起十四类、v4.10 起十五类、v4.11 起十六类、v4.12 起十七类，**v4.13 起十八类不可混引**。

## 条款地图（逐字核对，勿沿用二手摘要）

| 条款 | 要点 |
|---|---|
| §120.1 | 适用范围：`Any juice sold as such or used as an ingredient in beverages shall be processed in accordance with the requirements of this part.` 定义 juice（水果/蔬菜榨取的水性液体、其可食部分果泥、或该液体/果泥的浓缩物）；**不论是否曾进入州际贸易均适用**；`Raw agricultural ingredients of juice are not subject to the requirements of this part`。生效日 2002-01-22；小企业（<500 人）2003-01-21；极小企业 2004-01-20（年销售额 <$500,000，或 >$500,000 但食品销售额 <$50,000；或平均 <100 全职等效员工且全美售出 <100,000 单位） |
| §120.3 | 定义：(a) `cleaned`；(b) `control`；(c) `control measure`；(d) **`critical control point`**（可施加控制措施、且控制对将已识别危害降至可接受水平**必需**的环节）；(e) `critical limit`；(f) `culled`（含柑橘果面处理者须为 USDA choice 及以上的完好树采果）；(g) **`food hazard`**（无控制时合理可能致病的生物/化学/物理因子）；(h) `importer`（入境时美国货主或收货人；无美国货主时为其美国代理；**通常不是报关行、货代、承运人、船公司代表**）；(i) `monitor`；(j) `processing`（与果汁产品生产直接相关的活动），**(j)(2) 不含**：(i) 不从事其他加工的采收/采摘/运输原料、(ii) 零售经营；**(k) `processor` 含境外加工者**与面向市场或消费者测试的加工者；(l) `retail establishment`（直接向消费者提供果汁；若同时向其他企业销售或分销则不属）；(m) `shall`；(n) `shelf-stable product`；(o) `should`；(p) **`validation`**（验证中专门收集评价科技信息、判定计划在正确实施时能否有效控制已识别危害的那一部分）；(q) **`verification`**（除监控之外、确立计划有效性与系统按计划运行的活动） |
| §120.5 | `Except as provided by § 117.5(c), parts 110 and 117 of this chapter apply in determining whether the facilities, methods, practices, and controls used to process juice are safe...`——Part 117 默认适用，§117.5(c) 为唯一例外出口（该款全文未收） |
| §120.6 | **SSOP**：(a) 须有并实施覆盖加工前、中、后的卫生条件与操作的书面 SSOP，至少含 **(1)–(8) 八项**：接触食品/食品接触面/制冰用水的安全；食品接触面（含器具、手套、外衣）状况与清洁；防止从不洁物及生熟交叉污染；洗手/手消毒/厕所设施维护；防止润滑剂、燃料、农药、清洁剂、消毒剂、冷凝水等污染；有毒化合物的标示储存使用；可能致微生物污染的员工健康状况控制；防虫害进入；(b) 监测频次须至少确保符合 part 110 与 part 117 subpart B 中**既适合本厂又适合所加工食品**的条件，不符须**及时**纠正；(c) SSOP 记录受 §120.12 约束；(d) SSOP **可**纳入 HACCP 计划，但按本条实施的部分**不必**纳入 |
| §120.7 | **危害分析**：(a) 须为**每种果汁**制定**书面**危害分析，含 (1) 识别危害、(2) 评估每个危害是否 `reasonably likely to occur`（判断标准：谨慎加工者会因经验、疾病数据、科学报告等认为无控制时该危害在**该specific产品**中有发生的合理可能），并**含严重性评估**、(3) 识别可施加的控制措施、(4) 审查现行工艺是否需修改、(5) 识别 CCP；(b) 须涵盖**厂内与厂外**引入的危害，含**采收前、采收中、采收后**可能发生的危害；须由按 §120.13 受训者制定，受 §120.12 记录约束；(c) 评估时`should` 至少考虑 **9 项**：微生物污染、寄生虫、化学污染、非法农药残留、与危害相关的腐败、天然毒素、未经批准的食品或着色添加剂使用、可能致敏的未申报配料、物理危害；(d) `should` 评估配料、加工程序、包装、储存、预期用途、厂房设备功能与设计、厂内卫生（含员工卫生）；(e) **HACCP 计划不必处理由 part 113 或 part 114 控制的微生物与微生物毒素危害**，但须处理其余合理可能发生的危害 |
| §120.8 | **HACCP 计划**：(a) 危害分析显示一个或多个合理可能发生的危害时须有并实施**书面**计划，由按 §120.13 受训者制定；(a)(1)(2) 须**按加工场所**与**按果汁种类**分别制定；可对危害、CCP、关键限值与程序**本质相同**的果汁或工艺分组，但**特定产品或工艺独有**的计划要素须在计划中清楚界定并实际遵守；(b) 计划至少含 **7 项**：(1) 列出每种产品须控制的全部合理可能发生危害；(2) 列出每个危害的 CCP，含 (i) 控制**厂内**引入危害的 CCP 与 (ii) 控制**厂外**（含采收前中后）引入危害的 CCP；(3) 各 CCP 须满足的关键限值；(4) 监控程序与频次；(5) 按 §120.10(a) 制定的纠正行动计划；(6) 按 §120.11 的验证与确认程序及频次；(7) 记录系统（须载明监控所得**实际值与观察**）；(c) 卫生控制可纳入计划，但按 §120.6 监测的部分不必纳入 |
| §120.9 | **法律定性**：未建立并实施符合 §§120.6 / 120.7 / 120.8 的 HACCP 体系，或未按本 part 要求运行 → 该加工者的果汁产品 **依 FD&C Act 402(a)(4) 构成掺假**；是否「一致于确保果汁安全」通过**体系整体实施情况**评价 |
| §120.10 | **纠正措施**：偏离关键限值时须走 (a) 或 (b)：(a) 可制定**书面纠正行动计划**并纳入计划〔§120.8(b)(5)〕，须描述步骤并**指定责任人**，确保 (1) 无因该偏离而致害或掺假的产品进入商业、(2) **偏离原因被纠正**；(b) 无适用计划时须 (1) **隔离扣留**受影响产品（至少到 (2)(3) 完成）、(2) 由**具备充分培训或经验者**评审产品可接受性、(3) 必要时对产品采取纠正措施、(4) 必要时纠正偏离原因、(5) 由按 §120.13 受训者按 §120.11 **及时验证**并视需要修改计划；(c) 全部纠正措施须完整记录，受 §120.11(a)(1)(iv)(B) 验证与 §120.12 约束 |
| §120.11 | **验证与确认**：(a) 须验证体系**按设计实施**；(a)(1) 六类活动：(i) 复审消费者投诉（判断是否关系计划绩效或揭示此前未识别的 CCP）、(ii) 过程监控仪器校准、(iii) **可选**的定期成品或在制品检验——**但全部或部分依赖果面处理的柑橘汁加工者必须按 §120.25 做成品检验**、(iv) 由按 §120.13 受训者**签字并注明日期**复审记录：(A) CCP 监控记录（须完整且值在关键限值内）**在记录形成后 1 周（7 天）内**、(B) 纠正措施记录（须完整且按 §120.10 采取）**同样 1 周（7 天）内**、(C) 校准与成品/在制品检验记录（须完整且按书面程序执行）**在合理时间内**、(v) 任何验证程序（含投诉复审）显示需纠正时**执行 §120.10 的程序**、(vi) §120.25 要求的附加工艺验证；(b) **计划确认**：须确认计划足以控制合理可能发生的危害，**实施后 12 个月内至少一次、此后至少每年一次**，或**工艺发生可能影响危害分析或改动计划的任何变化时**（原料或来源、配方、加工方法或系统含计算机与软件、包装、成品分销系统、预期用途或消费者）；须由受训者执行、受记录约束；确认显示计划不足以完全满足本 part 时**须立即修改**；(c) **危害分析确认**：无 HACCP 计划（危害分析未发现合理可能发生的危害）时，工艺发生可能合理影响危害存在性的变化时须**重新评估危害分析的充分性**，由受训者执行并记录 |
| §120.12 | **记录**：(a) 须保存五类记录：SSOP 实施记录、书面危害分析、书面 HACCP 计划、计划持续实施记录（含 (i) CCP 及关键限值的监控——须记录实际时间、温度或其他测量值、(ii) 纠正措施含对偏离的全部响应行动）、体系验证与计划/危害分析确认记录；(b) 全部记录须含：加工者或进口商名称与地点、活动日期与时间（**(a)(2)(3)(5) 三类可不含时间**）、操作或制记录者**签名或缩写**、适用时产品标识与生产代码；`Processing and other information shall be entered on records at the time that it is observed`；记录须载明监控所得实际值与观察；(c) (a)(2)(3) 记录须由**现场最高负责人或更高层官员签字并注明日期**，签名表示公司已接受；且须在**首次接受时、任何修改时、按 §120.11 验证与确认时**签字注明日期；(d) **保存期**：(1) 易腐或冷藏果汁 **≥1 年**（自产品制备日）；冷冻／保藏／货架稳定产品 **2 年或货架期，孰长**；存于加工设施或进口商美国营业地；(2) (a)(1)(4) 记录**监测发生后 6 个月**起可异地存放，条件是**请求官方审查后 24 小时内可调取并提供到现场**；符合 (g) 的电子记录**可视同在场**；(3) 季节性长停可在季末转移至其他合理可及地点，但须**应要求立即归还**加工设施供官方审查；(e) 全部记录须在合理时间**可供审查与复制**；(f) 一般不公开，除已公开或涉已放弃产品/配料；(g) **按 part 11 维护计算机化记录可接受** |
| §120.13 | **培训**：(a) 四类职能只能由满足 (b) 者承担：(1) 制定危害分析（含界定控制措施）、(2) 制定适合特定加工者的 HACCP 计划、(3) 按 §120.10(b)(5) 与 §§120.11(b)(c) 验证修改计划、(4) 执行 §120.11(a)(1)(iv) 的记录复审；(b) 须**成功完成**果汁加工 HACCP 原理应用培训（至少等效于 FDA 认可为充分的标准化课程）**或**通过岗位经验具备等效知识；`The trained individual need not be an employee of the processor.` |
| §120.14 | **进口果汁**：(a) 每个果汁进口商须**二选一**：(1) 从与 FDA 有**现行有效 MOU 或类似协议**、覆盖该食品、证明其检查体系等效、准确反映签署方关系、整体可执行的国家采购；或 (2) 建立并实施**书面程序**确保进口果汁按本 part 加工，至少含 (i) 产品规格（确保不属 §402 掺假）、(ii) **affirmative steps 至少一项**：(A) 从境外加工者取得与该批次相关的 HACCP 计划与前提程序 SOP 记录、(B) 取得境外政府检查机构或合格第三方的**持续或逐批证书**、(C) 定期检查境外加工者设施、(D) 存档**英文版**境外加工者危害分析与 HACCP 计划**及书面保证**、(E) 定期检测并留存**英文**书面保证、(F) 其他能提供等效保证的验证措施；(b) 进口商可聘**合格第三方**协助或代为执行全部或部分验证活动，**包括代写验证程序**；(c) 进口商须保存**英文**记录证明 affirmative steps 的执行与结果，受 §120.12 约束；(d) 须提供证据证明所有报检果汁在符合本 part 的条件下加工；**若不存在等效保证，产品将被视为掺假并拒绝入境** |
| §120.20 | Subpart B 是 Subpart A 的**增量**：`This subpart augments subpart A of this part by setting forth specific requirements for process controls.` |
| §120.24 | **工艺控制（5-log）**：(a) 为满足 Subpart A，加工者须在 HACCP 计划中纳入控制措施，**持续**产生至少 **5 log（10⁵）** 削减，覆盖**至少货架期**、在**正常与中度滥用条件**储存下，针对「pertinent microorganism」＝**果汁中可能出现的最耐热、具公共卫生意义的微生物**；**豁免 (a)(1)** 受 part 113 或 114 管辖者；**豁免 (a)(2)** 用**单次热力步骤**足以达成货架稳定，或用**含全部配料热处理的浓缩工艺**，条件是须把达成货架稳定或浓缩所用的热力工艺副本纳入〔§120.7〕的书面危害分析 |
| §120.25 | **特定加工者的工艺验证（果面处理专项）**：适用对象是**依赖未与果汁全部部分接触的处理**来满足 §120.24 者；须对成品检测 **biotype I Escherichia coli**：(a) **每 1,000 加仑**果汁 **20 mL 样品（两个 10 mL 子样）**，**每个生产日**取样；日产量不足 1,000 加仑时按每 1,000 加仑取但**不少于每 5 个工作日一次**；子样须随机选取**已可分销给消费者**的包装；(b) 生产多种受本条约束果汁时**每种**都要按 (a) 取样；(c) 检测方法为「Analysis for Escherichia coli in Citrus Juices—Modification of AOAC Official Method 992.30」或**准确度、精密度、灵敏度**至少等效的方法（20 mL＝两个 10 mL 等分；ColiComplete／AOAC 992.30 modified）；(d) **任一子样阳性即 20 mL 样品记为阳性**，加工者须 (1) 复审 5-log 控制措施的监控记录并纠正不符的条件与做法，**可选**加测关注病原体；(2) 若复审或加测显示 5-log 未达成，按 §120.10 采取纠正措施；(e) **7 次检测中 2 次阳性** → 5-log 控制措施**视为不足**，须立即：(1) 在纠正措施完成前改用**压榨后**达成 5-log 的替代工艺；(2) 复审监控记录（范围须足以判定无失控趋势），条件不符则纠正，条件符合则**确认 HACCP 计划相对 5-log 的充分性**；(3) 按 §120.10 采取纠正措施，**包括确保无致害产品进入商业** |

## 转换局限（已知，引用时注意）

- GPO 双栏印刷版的行末断词按**原样保留**（如 `proc- essing`、`dehy- drated`、`contam- ination`），未做 dehyphenate。逐字引文核对用 NFKC + 去非字母数字归一化，天然消除断词连字符。
- 卷首目录区（`Sec.` 后 15 条目录条目，跨 Part 119 尾部）已整段裁掉；条款标题以正文中的 `§ 120.xxx` 首行为准。
- 页码区（439–448）与页眉 `Food and Drug Administration, HHS` / `21 CFR Ch. I (4–1–25 Edition)` 已由裁剪区与 NOISE 规则双重排除，残留 0。
- ⚠ **本轮修订了 `.cangjie/convert_cfr_part.py` 两处缺陷（已回写脚本，非本文件特有）**：
  - **多行 part 标题的续行被目录裁剪吞掉**：印刷版 `PART 120—HAZARD ANALYSIS AND / CRITICAL / CONTROL / POINT / (HACCP) SYSTEMS` 中，续行落在 `[PART 行, Sec. 行)` 区间内，原实现整段裁切会把 `CRITICAL CONTROL POINT (HACCP) SYSTEMS` 一并删除，产出的 H2 只剩前半句。现改为**裁切前先把续行接回 PART 行**（遇 `Subpart` / `Sec.` 视为标题结束）。⚠ 该缺陷同样影响此前四份 CFR 来源文件的 part 标题（Part 108 的标题缺 `CONTROL`），但那四份已定稿发布，本轮**不回改**，仅在各自卡片的引用中避免用 part 标题做逐字引用。
  - **独占一行的数字被当页码丢弃**：NOISE 里的 `^\d{2,4}$` 使 §120.25(c)(4)(i) 的 `juice / into / 90 / mL / of` 丢掉 `90`，产出 `into mL of`（应为 `into 90 mL of`）。现新增 `--keep-standalone-numbers` 开关（默认关闭，保持前四份来源文件的可复现性；Part 120 用该开关转出）。页眉页脚已由 clip 的 `y0=170` 排除，开关开启后 `residual_standalone_pagenum` 仍为 0。
- `.cangjie/fix_part120_reflow.py` 修 **11 处**段界缺陷：§120.24(b) 一处句中断段（`as defined in` / `§ 120.3(a) and (f)`，因该处 § 编号被误判为条款起点），以及 10 处「编号项被并进上一段」——§120.3(j)(1)、§120.8(b)(6)、§120.10(b)(5)、§120.12(c)(1)、§120.12(d)(1)(2)、§120.12(f)(1)、§120.13(a)(3)、§120.25(c)(4)(iv)、§120.25(d)(2)。脚本幂等（已应用则 SKIP），原文措辞未改。

## PART 120—HAZARD ANALYSIS AND CRITICAL CONTROL POINT (HACCP) SYSTEMS

AUTHORITY: 21 U.S.C. 321, 342, 343, 346, 348, 371, 374, 379e, 381, 393; 42 U.S.C. 241, 242l, 264.

SOURCE: 66 FR 6197, Jan. 19, 2001, unless otherwise noted.

### Subpart A—General Provisions

## § 120.1 Applicability.

(a) Any juice sold as such or used as an ingredient in beverages shall be processed in accordance with the re- quirements of this part. Juice means the aqueous liquid expressed or ex- tracted from one or more fruits or vegetables, purees of the edible por- tions of one or more fruits or vegeta- bles, or any concentrates of such liquid or puree. The requirements of this part shall apply to any juice regardless of whether the juice, or any of its ingredi- ents, is or has been shipped in inter- state commerce (as defined in section 201(b) of the Federal Food, Drug, and Cosmetic Act, 21 U.S.C. 321(b)). Raw ag- ricultural ingredients of juice are not subject to the requirements of this part. Processors should apply existing agency guidance to minimize microbial food safety hazards for fresh fruits and vegetables in handling raw agricultural products.

(b) The regulations in this part shall be effective January 22, 2002. However, by its terms, this part is not binding on small and very small businesses until the dates listed in paragraphs (b)(1) and (b)(2) of this section.

(1) For small businesses employing fewer than 500 persons the regulations in this part are binding on January 21, 2003.

(2) For very small businesses that have either total annual sales of less than $500,000, or if their total annual sales are greater than $500,000 but their total food sales are less than $50,000; or the person claiming this exemption employed fewer than an average of 100 full-time equivalent employees and fewer than 100,000 units of juice were sold in the United States, the regula- tions are binding on January 20, 2004.

## § 120.3 Definitions.
The definitions of terms in section 201 of the Federal Food, Drug, and Cos- metic Act, § 101.9(j)(18)(vi) of this chap- ter, and parts 110 and 117 of this chap- ter are applicable to such terms when used in this part, except that the defi- nitions and terms in parts 110 and 117 do not govern such terms where such terms are redefined in this part and ex- cept that the terms facility, hazard, and manufacturing/processing in parts 110 and 117 do not govern such terms where used in this part. The following definitions shall also apply:

(a) Cleaned means washed with water of adequate sanitary quality.

(b) Control means to prevent, elimi- nate, or reduce.

(c) Control measure means any action or activity to prevent, reduce to ac- ceptable levels, or eliminate a hazard.

(d) Critical control point means a point, step, or procedure in a food proc- ess at which a control measure can be applied and at which control is essen- tial to reduce an identified food hazard to an acceptable level.

(e) Critical limit means the maximum or minimum value to which a physical, biological, or chemical parameter must be controlled at a critical control point to prevent, eliminate, or reduce to an acceptable level the occurrence of the identified food hazard.

(f) Culled means separation of dam- aged fruit from undamaged fruit. For processors of citrus juices using treat- ments to fruit surfaces to comply with § 120.24, culled means undamaged, tree- picked fruit that is U.S. Department of Agriculture choice or higher quality.

(g) Food hazard means any biological, chemical, or physical agent that is rea- sonably likely to cause illness or in- jury in the absence of its control.

(h) Importer means either the U.S. owner or consignee at the time of entry of a food product into the United States, or the U.S. agent or representa- tive of the foreign owner or consignee at the time of entry into the United States. The importer is responsible for ensuring that goods being offered for entry into the United States are in compliance with all applicable laws. For the purposes of this definition, the importer is ordinarily not the custom house broker, the freight forwarder, the carrier, or the steamship represent- ative.

(i) Monitor means to conduct a planned sequence of observations or measurements to assess whether a process, point, or procedure is under control and to produce an accurate record for use in verification.

(j)(1) Processing means activities that are directly related to the production of juice products.

(2) For purposes of this part, proc- essing does not include:

(i) Harvesting, picking, or trans- porting raw agricultural ingredients of juice products, without otherwise en- gaging in processing; and

(ii) The operation of a retail estab- lishment.

(k) Processor means any person en- gaged in commercial, custom, or insti- tutional processing of juice products, either in the United States or in a for- eign country, including any person en- gaged in the processing of juice prod- ucts that are intended for use in mar- ket or consumer tests.

(l) Retail establishment is an operation that provides juice directly to the con- sumers and does not include an estab- lishment that sells or distributes juice to other business entities as well as di- rectly to consumers. ‘‘Provides’’ in- cludes storing, preparing, packaging, serving, and vending.

(m) Shall is used to state mandatory requirements.

(n) Shelf-stable product means a prod- uct that is hermetically sealed and, when stored at room temperature, should not demonstrate any microbial growth.

(o) Should is used to state rec- ommended or advisory procedures or to identify recommended equipment.

(p) Validation means that element of verification focused on collecting and evaluating scientific and technical in- formation to determine whether the HACCP plan, when properly imple- mented, will effectively control the identified food hazards.

(q) Verification means those activi- ties, other than monitoring, that es- tablish the validity of the HACCP plan and that the system is operating ac- cording to the plan.

[66 FR 6197, Jan. 19, 2001, as amended at 80 FR 56167, Sept. 17, 2015]

## § 120.5 Current good manufacturing practice.
Except as provided by § 117.5(c), parts 110 and 117 of this chapter apply in de- termining whether the facilities, meth- ods, practices, and controls used to process juice are safe, and whether the food has been processed under sanitary conditions.

[80 FR 56167, Sept. 17, 2015]

## § 120.6 Sanitation standard operating procedures.

(a) Sanitation controls. Each processor shall have and implement a sanitation standard operating procedure (SSOP) that addresses sanitation conditions and practices before, during, and after processing. The SSOP shall address:

(1) Safety of the water that comes into contact with food or food contact surfaces or that is used in the manufac- ture of ice;

(2) Condition and cleanliness of food contact surfaces, including utensils, gloves, and outer garments;

(3) Prevention of cross contamination from insanitary objects to food, food packaging material, and other food contact surfaces, including utensils, gloves, and outer garments, and from raw product to processed product;

(4) Maintenance of hand washing, hand sanitizing, and toilet facilities;

(5) Protection of food, food packaging material, and food contact surfaces from adulteration with lubricants, fuel, pesticides, cleaning compounds, sani- tizing agents, condensate, and other chemical, physical, and biological con- taminants;

(6) Proper labeling, storage, and use of toxic compounds;

(7) Control of employee health condi- tions that could result in the micro- biological contamination of food, food packaging materials, and food contact surfaces; and

(8) Exclusion of pests from the food plant.

(b) Monitoring. The processor shall monitor the conditions and practices during processing with sufficient fre- quency to ensure, at a minimum, con- formance with those conditions and practices specified in part 110 of this chapter and in subpart B of part 117 of this chapter that are appropriate both to the plant and to the food being proc- essed. Each processor shall correct, in a timely manner, those conditions and practices that are not met.

(c) Records. Each processor shall maintain SSOP records that, at a min- imum, document the monitoring and corrections prescribed by paragraph (b) of this section. These records are sub- ject to the recordkeeping requirements of § 120.12.

(d) Relationship to Hazard Analysis and Critical Control Point (HACCP) plan. Sanitation standard operating proce- dure controls may be included in the HACCP plan required under § 120.8(b). However, to the extent that they are implemented in accordance with this section, they need not be included in the HACCP plan.

[66 FR 6197, Jan. 19, 2001, as amended at 80 FR 56167, Sept. 17, 2015]

## § 120.7 Hazard analysis.

(a) Each processor shall develop, or have developed for it, a written hazard analysis to determine whether there are food hazards that are reasonably likely to occur for each type of juice processed by that processor and to identify control measures that the processor can apply to control those hazards. The written hazard analysis shall consist of at least the following:

(1) Identification of food hazards;

(2) An evaluation of each food hazard identified to determine if the hazard is reasonably likely to occur and thus, constitutes a food hazard that must be addressed in the HACCP plan. A food hazard that is reasonably likely to occur is one for which a prudent proc- essor would establish controls because experience, illness data, scientific re- ports, or other information provide a basis to conclude that there is a rea- sonable possibility that, in the absence of those controls, the food hazard will occur in the particular type of product being processed. This evaluation shall include an assessment of the severity of the illness or injury if the food haz- ard occurs;

(3) Identification of the control meas- ures that the processor can apply to control the food hazards identified as reasonably likely to occur in paragraph (a)(2) of this section;

(4) Review of the current process to determine whether modifications are necessary; and

(5) Identification of critical control points.

(b) The hazard analysis shall include food hazards that can be introduced both within and outside the processing plant environment, including food haz- ards that can occur before, during, and after harvest. The hazard analysis shall be developed by an individual or indi- viduals who have been trained in ac- cordance with § 120.13 and shall be sub- ject to the recordkeeping requirements of § 120.12.

(c) In evaluating what food hazards are reasonably likely to occur, consid- eration should be given, at a minimum, to the following:

(1) Microbiological contamination;

(2) Parasites;

(3) Chemical contamination;

(4) Unlawful pesticides residues;

(5) Decomposition in food where a food hazard has been associated with decomposition;

(6) Natural toxins;

(7) Unapproved use of food or color additives;

(8) Presence of undeclared ingredi- ents that may be allergens; and

(9) Physical hazards.

(d) Processors should evaluate prod- uct ingredients, processing procedures, packaging, storage, and intended use; facility and equipment function and design; and plant sanitation, including employee hygiene, to determine the po- tential effect of each on the safety of the finished food for the intended con- sumer.

(e) HACCP plans for juice need not address the food hazards associated with microorganisms and microbial toxins that are controlled by the re- quirements of part 113 or part 114 of this chapter. A HACCP plan for such juice shall address any other food haz- ards that are reasonably likely to occur.

## § 120.8 Hazard Analysis and Critical Control Point (HACCP) plan.

(a) HACCP plan. Each processor shall have and implement a written HACCP plan whenever a hazard analysis re- veals one or more food hazards that are reasonably likely to occur during proc- essing, as described in § 120.7. The HACCP plan shall be developed by an individual or individuals who have been trained in accordance with § 120.13 and shall be subject to the record- keeping requirements of § 120.12. A HACCP plan shall be specific to:

(1) Each location where juice is proc- essed by that processor; and

(2) Each type of juice processed by the processor. The plan may group types of juice products together, or group types of production methods to- gether, if the food hazards, critical con- trol points, critical limits, and proce- dures required to be identified and per- formed by paragraph (b) of this section are essentially identical, provided that any required features of the plan that are unique to a specific product or method are clearly delineated in the plan and are observed in practice.

(b) The contents of the HACCP plan. The HACCP plan shall, at a minimum:

(1) List all food hazards that are rea- sonably likely to occur as identified in accordance with § 120.7, and that thus must be controlled for each type of product;

(2) List the critical control points for each of the identified food hazards that is reasonably likely to occur, including as appropriate:

(i) Critical control points designed to control food hazards that are reason- ably likely to occur and could be intro- duced inside the processing plant envi- ronment; and

(ii) Critical control points designed to control food hazards introduced out- side the processing plant environment, including food hazards that occur be- fore, during, and after harvest;

(3) List the critical limits that shall be met at each of the critical control points;

(4) List the procedures, and the fre- quency with which they are to be per- formed, that will be used to monitor each of the critical control points to ensure compliance with the critical limits;

(5) Include any corrective action plans that have been developed in ac- cordance with § 120.10(a), and that are to be followed in response to deviations from critical limits at critical control points;

(6) List the validation and verification procedures, and the fre- quency with which they are to be per- formed, that the processor will use in accordance with § 120.11; and

(7) Provide for a recordkeeping sys- tem that documents the monitoring of the critical control points in accord- ance with § 120.12. The records shall contain the actual values and observa- tions obtained during monitoring.

(c) Sanitation. Sanitation controls may be included in the HACCP plan. However, to the extent that they are monitored in accordance with § 120.6, they are not required to be included in the HACCP plan.

## § 120.9 Legal basis.
Failure of a processor to have and to implement a Hazard Analysis and Crit- ical Control Point (HACCP) system that complies with §§ 120.6, 120.7, and 120.8, or otherwise to operate in accord- ance with the requirements of this part, shall render the juice products of that processor adulterated under sec- tion 402(a)(4) of the Federal Food, Drug, and Cosmetic Act. Whether a processor’s actions are consistent with ensuring the safety of juice will be de- termined through an evaluation of the processor’s overall implementation of its HACCP system.

## § 120.10 Corrective actions.
Whenever a deviation from a critical limit occurs, a processor shall take corrective action by following the pro- cedures set forth in paragraph (a) or paragraph (b) of this section.

(a) Processors may develop written corrective action plans, which become part of their HACCP plans in accord- ance with § 120.8(b)(5), by which proc- essors predetermine the corrective ac- tions that they will take whenever there is a deviation from a critical limit. A corrective action plan that is appropriate for a particular deviation is one that describes the steps to be taken and assigns responsibility for taking those steps, to ensure that:

(1) No product enters commerce that is either injurious to health or is other- wise adulterated as a result of the devi- ation; and

(2) The cause of the deviation is cor- rected.

(b) When a deviation from a critical limit occurs, and the processor does not have a corrective action plan that is appropriate for that deviation, the processor shall:

(1) Segregate and hold the affected product, at least until the require- ments of paragraphs (b)(2) and (b)(3) of this section are met;

(2) Perform or obtain a review to de- termine the acceptability of the af- fected product for distribution. The re- view shall be performed by an indi- vidual or individuals who have ade- quate training or experience to perform such review;

(3) Take corrective action, when nec- essary, with respect to the affected product to ensure that no product en- ters commerce that is either injurious to health or is otherwise adulterated as a result of the deviation;

(4) Take corrective action, when nec- essary, to correct the cause of the devi- ation; and

(5) Perform or obtain timely verification in accordance with § 120.11, by an individual or individuals who have been trained in accordance with § 120.13, to determine whether modifica- tion of the HACCP plan is required to reduce the risk of recurrence of the de- viation, and to modify the HACCP plan as necessary.

(c) All corrective actions taken in ac- cordance with this section shall be fully documented in records that are subject to verification in accordance with § 120.11(a)(1)(iv)(B) and the record- keeping requirements of § 120.12.

## § 120.11 Verification and validation.

(a) Verification. Each processor shall verify that the Hazard Analysis and Critical Control Point (HACCP) system is being implemented according to de- sign.

(1) Verification activities shall in- clude:

(i) A review of any consumer com- plaints that have been received by the processor to determine whether such complaints relate to the performance of the HACCP plan or reveal previously unidentified critical control points;

(ii) The calibration of process moni- toring instruments;

(iii) At the option of the processor, the performance of periodic end-prod- uct or in-process testing; except that processors of citrus juice that rely in whole or in part on surface treatment of fruit shall perform end-product test- ing in accordance with § 120.25.

(iv) A review, including signing and dating, by an individual who has been trained in accordance with § 120.13, of the records that document:

(A) The monitoring of critical con- trol points. The purpose of this review shall be, at a minimum, to ensure that the records are complete and to verify that the records document values that are within the critical limits. This re- view shall occur within 1 week (7 days) of the day that the records are made;

(B) The taking of corrective actions. The purpose of this review shall be, at a minimum, to ensure that the records are complete and to verify that appro- priate corrective actions were taken in accordance with § 120.10. This review shall occur within 1 week (7 days) of the day that the records are made; and

(C) The calibrating of any process monitoring instruments used at crit- ical control points and the performance of any periodic end-product or in-proc- ess testing that is part of the proc- essor’s verification activities. The pur- pose of these reviews shall be, at a min- imum, to ensure that the records are complete and that these activities oc- curred in accordance with the proc- essor’s written procedures. These re- views shall occur within a reasonable time after the records are made; and

(v) The following of procedures in § 120.10 whenever any verification pro- cedure, including the review of con- sumer complaints, establishes the need to take a corrective action; and

(vi) Additional process verification if required by § 120.25.

(2) Records that document the cali- bration of process monitoring instru- ments, in accordance with paragraph (a)(1)(iv)(B) of this section, and the per- formance of any periodic end-product and in-process testing, in accordance with paragraph (a)(1)(iv)(C) of this sec- tion, are subject to the recordkeeping requirements of § 120.12.

(b) Validation of the HACCP plan. Each processor shall validate that the HACCP plan is adequate to control food hazards that are reasonably likely to occur; this validation shall occur at least once within 12 months after im- plementation and at least annually thereafter or whenever any changes in the process occur that could affect the hazard analysis or alter the HACCP plan in any way. Such changes may in- clude changes in the following: Raw materials or source of raw materials; product formulation; processing meth- ods or systems, including computers and their software; packaging; finished product distribution systems; or the in- tended use or consumers of the finished product. The validation shall be per- formed by an individual or individuals who have been trained in accordance with § 120.13 and shall be subject to the recordkeeping requirements of § 120.12. The HACCP plan shall be modified im- mediately whenever a validation re- veals that the plan is no longer ade- quate to fully meet the requirements of this part.

(c) Validation of the hazard analysis. Whenever a juice processor has no HACCP plan because a hazard analysis has revealed no food hazards that are reasonably likely to occur, the proc- essor shall reassess the adequacy of that hazard analysis whenever there are any changes in the process that could reasonably affect whether a food hazard exists. Such changes may in- clude changes in the following: Raw materials or source of raw materials; product formulation; processing meth- ods or systems, including computers and their software; packaging; finished product distribution systems; or the in- tended use or intended consumers of the finished product. The validation of the hazard analysis shall be performed by an individual or individuals who have been trained in accordance with § 120.13, and, records documenting the validation shall be subject to the rec- ordkeeping requirements of § 120.12.

## § 120.12 Records.

(a) Required records. Each processor shall maintain the following records documenting the processor’s Hazard Analysis and Critical Control Point (HACCP) system:

(1) Records documenting the imple- mentation of the sanitation standard operating procedures (SSOP’s) (see § 120.6);

(2) The written hazard analysis re- quired by § 120.7;

(3) The written HACCP plan required by § 120.8;

(4) Records documenting the ongoing application of the HACCP plan that in- clude:

(i) Monitoring of critical control points and their critical limits, includ- ing the recording of actual times, tem- peratures, or other measurements, as prescribed in the HACCP plan; and

(ii) Corrective actions, including all actions taken in response to a devi- ation; and

(5) Records documenting verification of the HACCP system and validation of the HACCP plan or hazard analysis, as appropriate.

(b) General requirements. All records required by this part shall include:

(1) The name of the processor or im- porter and the location of the processor or importer, if the processor or im- porter has more than one location;

(2) The date and time of the activity that the record reflects, except that records required by paragraphs (a)(2), (a)(3), and (a)(5) of this section need not include the time;

(3) The signature or initials of the person performing the operation or cre- ating the record; and

(4) Where appropriate, the identity of the product and the production code, if any. Processing and other information shall be entered on records at the time that it is observed. The records shall contain the actual values and observa- tions obtained during monitoring.

(c) Documentation.

(1) The records in paragraphs (a)(2) and (a)(3) of this sec- tion shall be signed and dated by the most responsible individual onsite at the processing facility or by a higher level official of the processor. These signatures shall signify that these records have been accepted by the firm.

(2) The records in paragraphs (a)(2) and (a)(3) of this section shall be signed and dated:

(i) Upon initial acceptance;

(ii) Upon any modification; and

(iii) Upon verification and validation in accordance with § 120.11.

(d) Record retention.

(1) All records re- quired by this part shall be retained at the processing facility or at the im- porter’s place of business in the United States for, in the case of perishable or refrigerated juices, at least 1 year after the date that such products were pre- pared, and for, in the case of frozen, preserved, or shelf stable products, 2 years or the shelf life of the product, whichever is greater, after the date that the products were prepared.

(2) Offsite storage of processing records required by paragraphs (a)(1) and (a)(4) of this section is permitted after 6 months following the date that the monitoring occurred, if such records can be retrieved and provided onsite within 24 hours of request for of- ficial review. Electronic records are considered to be onsite if they are ac- cessible from an onsite location and comply with paragraph (g) of this sec- tion.

(3) If the processing facility is closed for a prolonged period between sea- sonal packs, the records may be trans- ferred to some other reasonably acces- sible location at the end of the sea- sonal pack but shall be immediately returned to the processing facility for official review upon request.

(e) Official review. All records re- quired by this part shall be available for review and copying at reasonable times.

(f) Public disclosure.

(1) All records re- quired by this part are not available for public disclosure unless they have been previously disclosed to the public, as defined in § 20.81 of this chapter, or unless they relate to a product or in- gredient that has been abandoned and no longer represent a trade secret or confidential commercial or financial information as defined in § 20.61 of this chapter.

(2) Records required to be maintained by this part are subject to disclosure to the extent that they are otherwise pub- licly available, or that disclosure could not reasonably be expected to cause a competitive hardship, such as generic type HACCP plans that reflect stand- ard industry practices.

(g) Records maintained on computers. The maintenance of computerized records, in accordance with part 11 of this chapter, is acceptable.

## § 120.13 Training.

(a) Only an individual who has met the requirements of paragraph (b) of this section shall be responsible for the following functions:

(1) Developing the hazard analysis, including delineating control meas- ures, as required by § 120.7.

(2) Developing a Hazard Analysis and Critical Control Point (HACCP) plan that is appropriate for a specific proc- essor, in order to meet the require- ments of § 120.8;

(3) Verifying and modifying the HACCP plan in accordance with the corrective action procedures specified in § 120.10(b)(5) and the validation ac- tivities specified in §§ 120.11(b) and (c); and 120.7;

(4) Performing the record review re- quired by § 120.11(a)(1)(iv).

(b) The individual performing the functions listed in paragraph (a) of this section shall have successfully com- pleted training in the application of HACCP principles to juice processing at least equivalent to that received under standardized curriculum recog- nized as adequate by the Food and Drug Administration, or shall be other- wise qualified through job experience to perform these functions. Job experi- ence may qualify an individual to per- form these functions if such experience has provided knowledge at least equiv- alent to that provided through the standardized curriculum. The trained individual need not be an employee of the processor.

## § 120.14 Application of requirements to imported products.
This section sets forth specific re- quirements for imported juice.

(a) Importer requirements. Every im- porter of juice shall either:

(1) Obtain the juice from a country that has an active memorandum of un- derstanding (MOU) or similar agree- ment with the Food and Drug Adminis- tration, that covers the food and docu- ments the equivalency or compliance of the inspection system of the foreign country with the U.S. system, accu- rately reflects the relationship be- tween the signing parties, and is func- tioning and enforceable in its entirety; or

(2) Have and implement written pro- cedures for ensuring that the juice that such importer receives for import into the United States was processed in ac- cordance with the requirements of this part. The procedures shall provide, at a minimum:

(i) Product specifications that are de- signed to ensure that the juice is not adulterated under section 402 of the Federal Food, Drug, and Cosmetic Act because it may be injurious to health or because it may have been processed under insanitary conditions; and

(ii) Affirmative steps to ensure that the products being offered for entry were processed under controls that meet the requirements of this part. These steps may include any of the fol- lowing:

(A) Obtaining from the foreign proc- essor the Hazard Analysis and Critical Control Point (HACCP) plan and pre- requisite program of the standard oper- ating procedure records required by this part that relate to the specific lot of food being offered for import;

(B) Obtaining either a continuing or lot specific certificate from an appro- priate foreign government inspection authority or competent third party certifying that the imported food has been processed in accordance with the requirements of this part;

(C) Regularly inspecting the foreign processor’s facilities to ensure that the imported food is being processed in ac- cordance with the requirements of this part;

(D) Maintaining on file a copy, in English, of the foreign processor’s haz- ard analysis and HACCP plan, and a written guarantee from the foreign processor that the imported food is processed in accordance with the re- quirements of this part;

(E) Periodically testing the imported food, and maintaining on file a copy, in English, of a written guarantee from the foreign processor that the imported food is processed in accordance with the requirements of this part; or

(F) Other such verification measures as appropriate that provide an equiva- lent level of assurance of compliance with the requirements of this part.

(b) Competent third party. An importer may hire a competent third party to assist with or perform any or all of the verification activities specified in para- graph (a)(2) of this section, including writing the importer’s verification pro- cedures on the importer’s behalf.

(c) Records. The importer shall main- tain records, in English, that document the performance and results of the af- firmative steps specified in paragraph (a)(2)(ii) of this section. These records shall be subject to the applicable provi- sions of § 120.12.

(d) Determination of compliance. The importer shall provide evidence that all juice offered for entry into the United States has been processed under conditions that comply with this part. If assurances do not exist that an im- ported juice has been processed under conditions that are equivalent to those required of domestic processors under this part, the product will appear to be adulterated and will be denied entry.

### Subpart B—Pathogen Reduction

## § 120.20 General.
This subpart augments subpart A of this part by setting forth specific re- quirements for process controls.

## § 120.24 Process controls.

(a) In order to meet the requirements of subpart A of this part, processors of juice products shall include in their Hazard Analysis and Critical Control Point (HACCP) plans control measures that will consistently produce, at a minimum, a 5 log (i.e., 105) reduction, for a period at least as long as the shelf life of the product when stored under normal and moderate abuse conditions, in the pertinent microorganism. For the purposes of this regulation, the ‘‘pertinent microorganism’’ is the most resistant microorganism of public health significance that is likely to occur in the juice. The following juice processors are exempt from this para- graph:

(1) A juice processor that is subject to the requirements of part 113 or part 114 of this chapter; and

(2) A juice processor using a single thermal processing step sufficient to achieve shelf-stability of the juice or a thermal concentration process that in- cludes thermal treatment of all ingre- dients, provided that the processor in- cludes a copy of the thermal process used to achieve shelf-stability or con- centration in its written hazard anal- ysis required by § 120.7.

(b) All juice processors shall meet the requirements of paragraph (a) of this section through treatments that are applied directly to the juice, except that citrus juice processors may use treatments to fruit surfaces, provided that the 5-log reduction process begins after culling and cleaning as defined in § 120.3(a) and (f) and the reduction is ac- complished within a single production facility.

(c) All juice processors shall meet the requirements of paragraphs (a) and (b) of this section and perform final prod- uct packaging within a single produc- tion facility operating under current good manufacturing practices. Proc- essors claiming an exemption under paragraph (a)(1) or (a)(2) of this section shall also process and perform final product packaging of all juice subject to the claimed exemption within a sin- gle production facility operating under current good manufacturing practices.

## § 120.25 Process verification for cer- tain processors.
Each juice processor that relies on treatments that do not come into di- rect contact with all parts of the juice to achieve the requirements of § 120.24 shall analyze the finished product for biotype I Escherichia coli as follows:

(a) One 20 milliliter (mL) sample (consisting of two 10 mL subsamples) for each 1,000 gallons of juice produced shall be sampled each production day. If less than 1,000 gallons of juice is pro- duced per day, the sample must be taken for each 1,000 gallons produced but not less than once every 5 working days that the facility is producing that juice. Each subsample shall be taken by randomly selecting a package of juice ready for distribution to con- sumers.

(b) If the facility is producing more than one type of juice covered by this section, processors shall take subsam- ples according to paragraph (a) of this section for each of the covered juice products produced.

(c) Processors shall analyze each sub- sample for the presence of E. coli by the method entitled ‘‘Analysis for Esch- erichia coli in Citrus Juices—Modifica- tion of AOAC Official Method 992.30’’ or another method that is at least equiva- lent to this method in terms of accu- racy, precision, and sensitivity in de- tecting E. coli. This method is designed to detect the presence or absence of E. coli in a 20 mL sample of juice (con- sisting of two 10 mL subsamples). The method is as follows:

(1) Sample size. Total-20 mL of juice; perform analysis using two 10 mL aliquots.

(2) Media. Universal Preenrichment Broth (Difco, Detroit, MI), EC Broth (various manufacturers).

(3) Method. ColiComplete (AOAC Offi- cial Method 992.30—modified).

(4) Procedure. Perform the following procedure two times:

(i) Aseptically inoculate 10 mL of juice into 90 mL of Universal Preenrichment Broth (Difco) and incu- bate at 35 °C for 18 to 24 hours.

(ii) Next day, transfer 1 mL of preenriched sample into 10 mL of EC Broth, without durham gas vials. After inoculation, aseptically add a ColiComplete SSD disc into each tube.

(iii) Incubate at 44.5 °C for 18 to 24 hours.

(iv) Examine the tubes under longwave ultra violet light (366 nm). Fluorescent tubes indicate presence of E. coli.

(v) MUG positive and negative con- trols should be used as reference in in- terpreting fluorescence reactions. Use an E. coli for positive control and 2 neg- ative controls—a MUG negative strain and an uninoculated tube media.

(d) If either 10 mL subsample is posi- tive for E. coli, the 20 mL sample is re- corded as positive and the processor shall:

(1) Review monitoring records for the control measures to attain the 5-log re- duction standard and correct those conditions and practices that are not met. In addition, the processor may choose to test the sample for the pres- ence of pathogens of concern.

(2) If the review of monitoring records or the additional testing indi- cates that the 5-log reduction standard was not achieved (e.g., a sample is found to be positive for the presence of a pathogen or a deviation in the proc- ess or its delivery is identified), the processor shall take corrective action as set forth in § 120.10.

(e) If two samples in a series of seven tests are positive for E. coli, the control measures to attain the 5-log reduction standard shall be deemed to be inad- equate and the processor shall imme- diately:

(1) Until corrective actions are com- pleted, use an alternative process or processes that achieve the 5-log reduc- tion after the juice has been expressed;

(2) Perform a review of the moni- toring records for control measures to attain the 5-log reduction standard. The review shall be sufficiently exten- sive to determine that there are no trends towards loss of control;

(i) If the conditions and practices are not being met, correct those that do not conform to the HACCP plan; or

(ii) If the conditions and practices are being met, the processor shall vali- date the HACCP plan in relation to the 5-log reduction standard; and

(3) Take corrective action as set forth in § 120.10. Corrective actions shall include ensuring no product en- ters commerce that is injurious to health as set forth in § 120.10(a)(1).
