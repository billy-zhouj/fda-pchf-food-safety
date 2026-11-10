# L.mono 增量候选 C：配方工艺、原料控制、储存运输与术语（来源标注 chunk id）

> 来源文件：FDA《Control of Listeria monocytogenes in Ready-To-Eat Foods: Guidance for Industry (Draft, 2017年1月)》
> 负责范围：I. Introduction（177–222）／VIII. Controls on Raw Materials and Other Ingredients（1249–1460）／IX. Process Control Based on Formulating an RTE Food to Have Intrinsic Characteristics（1461–1623）／X. Listericidal Process Control（1624–1732）／XI. Storage Practices and Time/Temperature Controls（1733–1786）／XII. Transportation（1787–1830）／XIV. Sampling and Testing of RTE Foods（2525–2590）／XV. Analysis of Data for Trends（2591–2706）／XVI. Training（2707–2710）／XVII. Sampling/Preparing/Testing（2711–2758）／XVIII. Records（2759–2800）／XIX. Glossary（2801–3031）
> 未读：`books/` 下指南全文、`source.md`
>
> **效力层级提示**：本指南是 **Draft（2017-01）**，正文一律用 "we recommend that you…"（建议层），本身不设法律责任；凡句中出现 "must" 的，是它在引述 21 CFR Part 117 的法定义务（原文用 "Part 117 requires…"）。合并进卡时须保留这层区分。
>
> **chunk id 错位提示（与 A/B 文件同源问题）**：本文件切分存在标题与正文错配（如 "ck-6423f9faad61 / D. Relevant Sections of part 117" 标题下实际是 VIII.B.5「Testing as the only control」的正文；"ck-16497f94f9de / XII. Transportation" 标题下实际是 XI 的尾部与 XII 全文；"ck-57471f7d75bc / XX. Table of Abbreviations" 标题下实际是 XIX.B 术语表的后半段）。下文每条按**正文实际归属的章节号**标注，并保留该 chunk id，合并时以章节号为准。
>
> **与 A/B 候选文件的关系**：A 负责 VII 卫生与 XIII 环境监测，B 负责 II–VI 背景/人员/厂房设备。本文件负责 VIII–XII、XIV–XIX。跨文件重复项已在各条内注明（尤其 nB-01/nB-02 与本文件 nC-05/nC-08）。

---

## 一、新知识候选

### nC-01 本指南的适用与不适用边界：先看有没有"包装后致死处理"，再看是否适用本指南
- 出处: I. Introduction；chunk: ck-a2fe455930cb（正文见 ck-7b3b44e66ced 段内）
- 原文关键句: "This guidance is intended to help you comply with the CGMP and PCHF requirements of part 117 with respect to measures that can significantly minimize or prevent the contamination of RTE food with *L. monocytogenes* whenever a RTE food is exposed to the environment prior to packaging and the packaged food does not receive a treatment or otherwise include a control measure (such as a formulation lethal to *L. monocytogenes*)…"
- 中文大意：指南适用于受 Part 117 约束（CGMP 主体、PCHF 主体或两者）的 RTE 食品生产/加工/包装/持有者，聚焦"RTE 食品在**包装前**暴露于环境、而**包装后**没有致死处理或致死型配方控制"的场景；**明确不适用于**：①在最终包装内、或紧邻包装前施加致死措施且该系统能充分屏蔽产品与包装的食品接触面不受环境污染的加工者；②不受 Part 117 约束的场所（如农场）。
- 类型: fact / rule
- 建议归属: 并入 `hazard-analysis-method`（Step 3 的 § 117.130(c)(1)(ii) 强制触发器旁，补"本指南的适用分流"），或并入 `regulatory-boundaries`
- 为什么是现有技能缺口: 现有卡写出了法规的强制触发条件（"RTE + 包装前暴露 + 包装后无致死处理"），但**没有把"包装后致死处理"与"包装前致死处理但屏蔽不足"这两种边界情形分开**——用户拿这套指南去回答"我厂做了最后一道巴氏杀菌还适不适用"时会得到含糊答案。

### nC-02 严重依赖"内在特性"的食物是食源性李斯特菌病风险最低的一类——配方控制是风险分级的第一杠杆
- 出处: IX 开头；chunk: ck-6e733495e327
- 原文关键句: "…it is well established that the foods that pose the lowest risk of foodborne listeriosis have intrinsic (physical or chemical) characteristics that do not support the growth of *L. monocytogenes*. Formulating your food product to have one or more such intrinsic characteristics can enhance the safety of your product."
- 中文大意：公认的事实是——食源性李斯特菌病风险最低的食品，恰好是那些具备不支持李斯特菌生长的内在（物理或化学）特性的食品；把 RTE 食品配成具有一种或多种这样的内在特性，可以提升产品安全。指南建议在**产品开发阶段**（"as part of the process of developing an RTE food"）就评估是否可采用 listeristatic 配方作为工艺控制。
- 类型: fact
- 建议归属: 并入 `process-control-validation`（I 段/Step 1 前置：配方控制 vs 致死控制的取舍）
- 为什么是现有技能缺口: 现有工艺控制卡的推理链起点是"选目标菌"，隐含前提是"一定有一个 kill step"。本指南给出的是**先问产品该长成什么样、再决定要不要 kill step** 的前置问题——对货架期长、冷藏、无法热处理的 RTE（如鲜切果蔬、熟食色拉），这才是主路径。

### nC-03 listeristatic 三条路径的官方列举（pH ≤ 4.4 / aw ≤ 0.92 / 含抑菌物质）及其"与致死型配方并列"的定位
- 出处: IX；chunk: ck-6e733495e327
- 原文关键句: "…we recommend that, as part of the process of developing an RTE food, you consider whether it is practical to use one or more of the following listeristatic formulations as a process control for *L. monocytogenes*: pH less than or equal to 4.4; Water activity less than or equal to 0.92; Formulated to contain one or more inhibitory substances that, alone or in combination, prevent the growth of *L. monocytogenes*, including formulation through processes such as fermentation or culturing."
- 中文大意：三条 listeristatic（抑制型）配方路径——①pH ≤ 4.4；②aw ≤ 0.92；③配方中含有一种或多种抑菌物质（单独或组合即可），包括通过发酵/培养工艺形成的配方。指南同时要求：采用任何 listeristatic 配方，**既要证明其有效（initial demonstration），也要持续验证（ongoing verification）**。
- 类型: threshold / rule
- 建议归属: 并入 `process-control-validation`（Step 4 配方屏障数值处，与 4.6/0.85 基准并列加"两套基准"框）；**注意与候选 B 的 nB-01 同源**（B 引 II.B 的三阈值表述）——合并时二选一，以本条（IX 章官方列举 + "must also demonstrate and verify"）为准，B 的 nB-01 保留 hurdles 概念部分
- 为什么是现有技能缺口: 现有卡 Step 5 只写 `a_w≤0.85 控营养细胞 / ≤0.92 抑孢子萌发`、`pH<4.6 控肉毒`，**没有 pH 4.4 这个李斯特菌专用更严阈值**，用户会误以为按 pH 4.6 酸化即自动满足 L. mono 控制——这是本指南必须显式区分的两套基准（详见第三节 kC-01）。

### nC-04 listeristatic 配方的初始有效性证明有五类可组合证据路径（含"历史确立的配方控制"这一最短路径）
- 出处: IX.A；chunk: ck-763ce49a6c2a
- 原文关键句: "Available approaches for demonstrating that your formulation consistently prevents growth of *L. monocytogenes* include (Ref. 53): Historically established formulation controls (e.g., pH less than or equal to 4.4 or water activity less than or equal to 0.92); Reference to scientific or technical information…; Previous validation studies…; Mathematical modelling…; Scientifically valid experimental data (e.g., data from challenge studies…)… commonly used alone or in combination."
- 中文大意：证明"配方持续抑制李斯特菌生长"的五条可并列或组合使用的证据路径——①历史确立的配方控制（pH≤4.4 或 aw≤0.92）；②引用已发表的同行评议研究（如证明某种抗菌成分在自家品类如熟食色拉中有效）；③既往验证研究（公开的或本厂内部的，如某配方验证研究至少部分适用于第二个配方）；④数学建模（用李斯特菌生长抑制模型辅助设计挑战试验）；⑤科学有效的实验数据（自做挑战试验）。指南明确指出两类配方的证据结构不同：单参数配方（只靠 pH 或只靠 aw）vs 组合参数配方（如抗菌成分 + pH）。
- 类型: procedure
- 建议归属: 并入 `process-control-validation`（Step 3 "两层验证"旁新增"抑制型配方的证据路径"分支）
- 为什么是现有技能缺口: 现有卡的两层验证框架（文献层 + 设备层）是为**热处理**设计的（热分布 + 热穿透）；抑制型配方没有"设备层"概念，它的对应物是"证据类型清单"。缺这份清单，用户会误以为必须自做挑战试验（成本最高的那条）。

### nC-05 pH ≤ 4.4 / aw ≤ 0.92 有"文献即足够"的快捷通道——不必自做挑战试验
- 出处: IX.A.1；chunk: ck-565cf7b1a2b0
- 原文关键句: "You may rely on data and information available in the scientific literature (e.g., Ref. 12, Ref. 15, Ref. 16, and Ref. 18 through Ref. 20) as an adequate demonstration that a listeristatic formulation that uses a pH less than or equal to 4.4, or water activity less than 0.92, is effective."
- 中文大意：可以**仅凭**科学文献中的数据与信息（指南列出 Ref. 12/15/16/18–20）即认为使用 pH ≤ 4.4 或 aw ≤ 0.92 的 listeristatic 配方是有效的，无需自做挑战试验。（与之相对，组合型配方走 IX.A.2 的完整科学证明路径。）这也与 Part 117 的证据优先级一致：证据可得且充分时不自做研究〔§ 117.160(b)(2)〕。
- 类型: procedure / rule
- 建议归属: 并入 `process-control-validation`（Step 3 证据顺序），并在 `reference-tools-discipline` Step 3 的"数值使用纪律"处加一句交叉引用
- 为什么是现有技能缺口: 现有卡只给了"文献层证据"这一层，没有说明"对于 pH≤4.4 / aw≤0.92 这两个**已被文献确立**的数值，文献本身就是充分的初始证明"——这是可以显著降低验证成本的判定。

### nC-06 抑制型配方有效性判据：货架期内多个时间点、重复生长研究、两个以上时间间隔、增幅 < 1 log
- 出处: IX.A.2；chunk: ck-9494b3697fde
- 原文关键句: "A listeristatic formulation is generally considered to be effective if growth studies that include samples at various points during product shelf life show an increase of less than 1 log cycle over two or more time intervals in the number of *L. monocytogenes* during replicate trials with the food of interest."
- 中文大意：通用判据——在**货架期多个时间点**取样的生长研究中，李斯特菌数量在**两个以上时间间隔**内、在**重复试验**中的增幅 **< 1 log**，即视为该 listeristatic 配方有效。此外：这类研究应由**懂食品微生物与病原控制**的微生物学家或食品安全专家（如 process authority）实施；研究结果应给出**可监控的参数及其最小/最大值**；指南并建议**操作参数取值带安全裕度**（在评估工艺偏差时有用）。
- 类型: threshold / procedure
- 建议归属: 并入 `process-control-validation`（Step 3/新增"抑制型验证"子节，Step 4 的"参数+裕度"写法）
- 为什么是现有技能缺口: 现有卡只有**致死型**的接受准则（5D–7D、附录 3 表值），没有**抑制型**的接受准则（< 1 log）。缺它就无法为冷藏即食色拉这类产品设计验证方案。
- **与候选 B 的 nB-02 关系**：B 引 II.B 的同一条判据但无"两个以上时间间隔"与"安全裕度"两处限定；合并时取本条（IX 章为正式表述），nB-02 可降级为引用。

### nC-07 抑制型配方的监控：可测参数与"配料比例正确"二选一，以及组合配型的监控清单
- 出处: IX.B.1；chunk: ck-c1d39dd9fa4f
- 原文关键句: "If your formulation control depends upon pH or water activity alone, you should either monitor pH or water activity of each batch or monitor that all ingredients in the formulation have been added in the appropriate proportions to achieve the desired pH or water activity. For other listeristatic formulations, you should monitor applicable process control parameters. Examples … monitoring the amount of antimicrobial ingredient added, and/or the pH and any other parameter that is part of the hurdles that control *L. monocytogenes*, and monitoring that all ingredients in the formulation have been added in the appropriate proportions."
- 中文大意：监控有两条路——①直接测（每批测 pH 或 aw）；②间接证（监控所有配料是否按正确比例加入，从而达到目标 pH/aw）。组合型配方监控"适用的工艺控制参数"，示例包括：抗菌成分的加入量、pH、构成"hurdles"的任何其他参数，以及配料加入比例是否正确。
- 类型: procedure
- 建议归属: 并入 `process-control-validation`（Step 4 代理参数转译的镜像用法）并入 `management-components`（Step 1 监控四问的 What 栏）
- 为什么是现有技能缺口: 现有卡的"代理参数转译"是**从不可测量→可测量**（时间→带速）；本条是**从可测量→可测量替代**（不测成品 pH，改测配料比例），方向相反但同样是合法简化，缺失会让用户以为 pH 必须逐批实测。

### nC-08 抑制型配方的验证活动清单（含"由他人旁观测量过程"这一低成本有效性核查）
- 出处: IX.B.2；chunk: ck-f6c3538256fe
- 原文关键句: "…these measures should ensure that any formulation or process is consistently applied and the applicable control is consistently achieved. Examples of such measures include: Calibrating equipment used to measure pH or water activity … or having someone other than those responsible for batch operations periodically observe the determination of pH or water activity measurement to verify the test is conducted correctly…; Having someone other than those responsible for batch operations occasionally observe the addition of particular antimicrobial ingredients in specific amounts to verify batch control…; Periodically testing a batch of your food product for pH or water activity, if your listeristatic control relies on adding ingredients in the formulation in the appropriate proportions; or Reviewing records of measurements to ensure the records are accurate and meet the minimum or maximum values for the process control parameters."
- 中文大意：抑制型配方的持续验证四类措施——①校准 pH/aw 测量设备，**或**由非当批操作人员定期旁观 pH/aw 测定过程以核查测法正确；②由非当批操作人员偶尔旁观抗菌成分按规定量加入以核查批次控制；③若控制依赖配料比例，则定期抽测一批成品的 pH/aw；④审查测量记录，确认数值准确且落在工艺控制参数的最小/最大值之内。
- 类型: procedure
- 建议归属: 并入 `process-control-validation`（Step 4）或 `management-components`（Step 1 监控设计 + Step 4 验证体系）
- 为什么是现有技能缺口: "由独立于操作者的人旁观测量过程"这一验证手法在现有卡里没有——它比校准更便宜、比实验室检测更贴近现场，可直接补进验证活动清单。

### nC-09 抑制型配方的偏差处置分叉：生产中可回调 vs 包装后必须先做安全性评估
- 出处: IX.B.3 / IX.D；chunk: ck-678a45e38434
- 原文关键句: "If you have determined the pH, water activity or addition of antimicrobial ingredients of a batch is not correct during production, you can take appropriate actions to adjust the parameter to the appropriate value. If you have determined the pH, water activity or addition of antimicrobial ingredients of a batch is not correct after packaging, you should evaluate the food for safety and not release the food into commerce unless determined to be safe (e.g., by a Preventive Controls Qualified Individual (PCQI))… You should determine what caused the problem and take steps to prevent it from reoccurring."
- 中文大意：分叉点在于**偏差发生在包装前还是包装后**——生产中发现 pH/aw/抗菌成分量不对，可就地调整到目标值；包装后才发现不对，须评估食品安全性、**未经判定安全不得进入流通**（可由 PCQI 判定），并查明原因、防止再发。
- 类型: procedure / rule
- 建议归属: 并入 `management-components`（Step 3 偏差分诊：新增"配方型偏差"的时点分叉）
- 为什么是现有技能缺口: 现有卡的分诊维度是"过敏原/卫生 vs 常规 + 是否已投产 + 孤立 vs 反复"，**没有"偏差发生于包装前/包装后"这个对配方型控制具有决定性的时点轴**（现有卡只在冷却工艺里提过"投产后"）。

### nC-10 抑制型配方的记录清单（5 项）与 Part 117 条款映射
- 出处: IX.C / IX.D；chunk: ck-cfb42cd92efc（记录）、ck-c65884b6e4ab（条款）
- 原文关键句: "We recommend that you establish and maintain records of: Process control parameters applicable to the listeristatic formulation, such as pH, water activity, and concentration of antimicrobial ingredient; Equipment calibration; Your validation of listeristatic process controls; Your monitoring and/or verification of listeristatic process control parameters …; Your review of listeristatic process control records; and Any corrective actions or corrections taken."
- 中文大意：记录六项——适用的工艺控制参数（pH、aw、抗菌成分浓度）、设备校准、listeristatic 控制的**验证**、监控/验证记录、对 listeristatic 控制记录的**审查**、以及采取的纠正措施或纠正。相关 Part 117 条款：§ 117.80(c)(4)、117.135(c)(1)、117.145、117.150、117.155、117.160、117.165、117.190。
- 类型: procedure
- 建议归属: 并入 `management-components`（Step 5 记录体系：按控制类型分组的记录清单）
- 为什么是现有技能缺口: 现有卡给的是"六项法定一般要件"（形式要件），缺"按控制类型逐类列出该留什么记录"的**内容清单**——本指南对 listeristatic / listericidal / 环境监测 / RTE 抽检四类各给了一份，可直接作为记录表单设计底稿。

### nC-11 listericidal 控制的验证目标写成了"可检出下限"而非"削减 log 数"：≤0.04 CFU/g（<1 CFU/25 g）
- 出处: X.A；chunk: ck-1d32883482a3
- 原文关键句: "…demonstrate that a listericidal process control … consistently destroys viable cells of *L. monocytogenes* and consistently leads to a food product that does not contain detectable *L. monocytogenes* using a method that has a sensitivity of detection of at least 0.04 CFU of *L. monocytogenes* per gram of food (<1 CFU/25 g)."
- 中文大意：listericidal 控制的验证目标**不用 log 表述，而用成品可检出性表述**——工艺须一致地摧毁活菌并一致地使成品**不含可检出的李斯特菌**，所用方法的检出灵敏度须**至少 0.04 CFU/g（即 <1 CFU/25 g）**。工艺所需强度部分取决于工艺前李斯特菌的可能水平。
- 类型: threshold
- 建议归属: 并入 `process-control-validation`（Step 2 定削减倍数：新增"目标 = 成品不可检出 + 方法灵敏度 ≥0.04 CFU/g"这一层）
- 为什么是现有技能缺口: 现有卡的目标函数是"降 5D–7D"，没有"**方法灵敏度**"这个维度——同样是 5 log 工艺，用灵敏度 10 CFU/g 的方法验证与用 0.04 CFU/g 的方法验证，结论强度完全不同。这一维度现有技能完全缺失。

### nC-12 listericidal 的默认 log 数由"工艺前初始负荷"决定：≤100 CFU/g → 5 log；>100 CFU/g 可预见 → 6 log
- 出处: X.A；chunk: ck-1d32883482a3
- 原文关键句: "In the absence of scientific studies, a listericidal process control that provides a reduction of the number of viable cells of *L. monocytogenes* of five orders of magnitude (five logarithms or 99.999%) could achieve that goal, particularly if the food is unlikely to be contaminated with more than 100 CFU/g. If it is reasonably foreseeable that ingredients you use could be contaminated with more than 100 CFU/g, then reducing the number of viable cells … by six orders of magnitude (six logarithms or 99.9999%) could be necessary…"
- 中文大意：无科学研究支撑时的兜底规则——**5 log**（99.999%）在"食品不太可能被污染到超过 100 CFU/g"时可达成目标；若**可合理预见**所用配料可能被污染到 **>100 CFU/g**，则可能需要 **6 log**（99.9999%）。其他 log 数若经适当验证，也可将风险降到足以预防发病的程度。
- 类型: threshold / rule
- 建议归属: 并入 `process-control-validation`（Step 2 定削减倍数：与"营养细胞病原 5D–7D、孢子 6D"的默认值并列，加"初始负荷"这一自变量）
- 为什么是现有技能缺口: 现有卡的 5D–7D 区间是**通用默认值**，其依据是"病原类型"；本指南给出的是**李斯特菌专用**的兜底值，且明确把"**工艺前初始负荷**"作为决定 log 数的第二个自变量——这正是现有卡 Step 2"双向优化"里提到的"自身初始菌量"，但没有具体到数值断点（100 CFU/g）与 log 数映射。

### nC-13 "工艺只能解决进入产品之前的污染"——listericidal 之后仍会再污染的官方论证与两个工具指针
- 出处: X 开头；chunk: ck-2c7761af6908
- 原文关键句: "*L. monocytogenes* has been shown to persist in equipment and the processing environment in harborage sites, and can lead to recontamination of your RTE food after you apply a listericidal process control. … We recommend that you consider the information in Appendices 1 and 2 to prevent recontamination of your RTE food product after you apply a listericidal process control."
- 中文大意：李斯特菌已被证实在设备与加工环境的**藏匿点（harborage sites）**中持续存在，**施加 listericidal 工艺控制之后仍可造成 RTE 食品再污染**；指南要求参照**附录 1（潜在污染源清单）**与**附录 2（污染场景清单）**来防止工艺后的再污染。
- 类型: fact / rule
- 建议归属: 并入 `process-control-validation`（B 段边界：kill step 之后的再污染）+ `environmental-pathogen-sanitation`（接口）
- 为什么是现有技能缺口: 现有卡 B1 边界写的是"热处理只杀营养细胞、不灭孢子、不消除已形成毒素"——那是**工艺内部的技术上限**；本条是**工艺外部的闭环缺口**：即便工艺 100% 有效，环境再污染仍会独立地把产品打回不合格，且指南给了两个可查的清单（附录1/2）作为检查表入口。现有卡 A2 里"环境病原与卫生控制：热处理之后的再污染转那边"的分工，正好需要这条作为交接凭据。

### nC-14 listericidal 的候选技术清单：热处理、辐照（须为直接食品添加剂且列于 21 CFR part 179）、静水压处理、致死型配方
- 出处: X.A；chunk: ck-b3e954575ce0
- 原文关键句: "In looking for listericidal process controls, we recommend that you consult a food safety expert (such as a microbiologist or process authority) knowledgeable in food microbiology and pathogen control and consider measures, alone or in combination, such as thermal treatment, irradiation (provided that irradiation has been approved as a direct food additive and listed in 21 CFR part 179), hydrostatic pressure processing, or product formulations that are listericidal. The information from validation studies should provide the parameters (and associated minimum or maximum values) that you would monitor…"
- 中文大意：寻找 listericidal 控制时应咨询懂食品微生物与病原控制的食品安全专家（微生物学家或 process authority），并考虑单独或组合使用：热处理、**辐照（前提是已获批为直接食品添加剂并列于 21 CFR part 179）**、静水压（hydrostatic pressure）处理、以及致死型产品配方。验证研究的结果应给出可监控的参数及其最小/最大值。
- 类型: procedure / fact
- 建议归属: 并入 `process-control-validation`（Step 1/Step 3：技术选项清单 + 辐照的法定前置条件）
- 为什么是现有技能缺口: 现有卡的技术视野基本是"热处理 + 代理参数"。**静水压**这一非热致死技术、以及**辐照必须先过 part 179 批准**这一法定前置条件，现有技能里没有——用户提"用辐照"时，现有卡无法回答"能不能用"。

### nC-15 listericidal 工艺的监控参数清单与"尽可能连续监控并记录"的倾向
- 出处: X.B.1；chunk: ck-f2a6433fddcf
- 原文关键句: "We recommend that you monitor parameters such as time, temperature, water activity, pH, and concentration of a listericidal ingredient with sufficient frequency to ensure that control is achieved. When practical, we recommend continuous monitoring and recording of such parameters."
- 中文大意：监控时间、温度、水分活度、pH、以及致死成分的浓度，频次须足以确保控制达成；**在可行时建议连续监控并记录**。（注意：同一句式在抑制型章节只写"监控适用的工艺控制参数"，此处才点出"尽可能连续"。）
- 类型: procedure / rule
- 建议归属: 并入 `process-control-validation`（Step 4 关键限值）+ `management-components`（Step 1 监控频次）
- 为什么是现有技能缺口: 现有卡的监控频次基线是通用四问（连续记录→至少每批/每日人工核查）。本条给出**李斯特菌致死工艺的专门倾向**：可行时连续监控并记录（记录密度更高），并明确了 aw/pH/致死成分浓度也是被监控的工艺参数——现有卡未把这三项列入致死工艺的监控对象。

### nC-16 listericidal 的验证活动清单（含热穿透相关参数的现场核查与"配方比例正确性"核查）
- 出处: X.B.2；chunk: ck-d7cfa3659e1a
- 原文关键句: "…Calibrating process monitoring and verification equipment; Checking recorder charts, bed depths, pump or conveyor belt speeds, particle size (for heat penetration), and other parameters as appropriate during production to ensure they are functioning properly; Establishing a standard operating procedure in which an individual is responsible for periodically observing the addition of particular antimicrobial ingredients in specific amounts…; Verifying that all ingredients in the formulation have been added in the appropriate proportions, if you have established a process control parameter (such as pH or water activity); and Reviewing records of measurements…"
- 中文大意：五类验证措施——①校准过程监控与验证设备；②**生产过程中**检查记录曲线、料层深度（bed depths）、泵速或输送带速度、颗粒尺寸（用于热穿透）等参数是否正常运作；③建立 SOP 指定专人定期旁观抗菌成分按规定量加入；④若设立了 pH/aw 类工艺控制参数，核查所有配料是否按正确比例加入；⑤审查测量记录是否准确且满足参数最小/最大值。
- 类型: procedure
- 建议归属: 并入 `process-control-validation`（Step 3/Step 4）+ `management-components`（Step 4 验证体系）
- 为什么是现有技能缺口: 现有卡讲"代理参数须可测可记录"，但没有给出**验证这些代理参数在生产中是否真在运作**的具体动作清单（尤其"生产中检查记录曲线/料层深度/泵速/带速"这一组——它是把 EPIPT/代理转译从纸面拉回现场的动作）。

### nC-17 listericidal 的偏差处置：温度不足可延长时间补足等效致死量（PCQI 参与）
- 出处: XI 开头（实为 X.B.3）；chunk: ck-0105b5e603d4
- 原文关键句: "If you have determined during processing that a process control parameter has not been met, you may be able to correct that during operations. For example, if temperature is found to be lower than the process control temperature, you may be able to increase the time to achieve an equivalent lethality. If you are subject to subpart C, we recommend that your PCQI be involved in making this correction. If you have determined after packaging that the process parameter was not met, you should evaluate the food for safety and not release the food into commerce unless determined to be safe… If the product evaluation indicates a safety concern and the product has been released into commerce, you should recall the product."
- 中文大意：生产中发现工艺参数未达标可在过程中纠正——例如温度低于工艺控制温度时，**可延长时间以达到等效致死量**（等效致死换算的现场用法）；受 subpart C 约束者建议 PCQI 参与该纠正。包装后才发现参数未达标：评估安全性、未判定安全不得入市（PCQI 判定）、查明原因防复发；**若已入市且评估提示安全顾虑，应召回该产品**。
- 类型: procedure
- 建议归属: 并入 `process-control-validation`（Step 6 偏差处置：新增"等效致死量补偿"这一动作）+ `management-components`（Step 3/召回升级接口）
- 为什么是现有技能缺口: 现有卡 Step 6 的处置阶梯是"补足处理 → 再加工 → 暂存 → 降级 → 转饲料 → 销毁"，**没有"用延长时间补足温度不足"这一具体且合法的现场动作**，也没把"已入市且评估提示安全顾虑 → 应召回"这条从偏差直接通向召回的触发链写出来。

### nC-18 原料控制的前提：识别"很可能携带李斯特菌"的原料并建立清单；无充分信息时按"可能污染"处理
- 出处: VIII.A / VIII.B；chunk: ck-2c3026fd4fb8（VIII 开头）、ck-4e09be35f298（VIII.B 前提）
- 原文关键句: "We recommend that you assess which raw materials and other ingredients (such as raw or minimally processed foods) are more likely to be contaminated with *L. monocytogenes* than others and focus control efforts on these ingredients. Based on this assessment, you should establish a list of raw materials and other ingredients for which it is reasonably foreseeable that the ingredients could be contaminated…"
- 中文大意：评估哪些原料与配料（生或最小加工食品）比其他更可能带李斯特菌，据此建立一份"**可合理预见会被污染**"的原料清单并聚焦控制；对该清单中每一项，"在缺乏关于该配料所呈现风险的充分信息时，建议**假定该配料可能被李斯特菌污染**"（treat as if contaminated）。
- 类型: procedure / rule
- 建议归属: 并入 `supply-chain-verification`（Step 1 前置：控制主体映射之前先做"配料风险分层"）+ `hazard-analysis-method`（Step 2 原料来源）
- 为什么是现有技能缺口: 现有供应链卡从"控制主体映射"直接起步，缺**配料侧的风险分层**这一前置动作；而本指南的规则是"信息不足即按污染处理"——这是一个**举证责任倒置**的默认值，现有卡未收录。

### nC-19 原料清单的三因素风险画像：内在特性（pH/aw）、配料制造工艺、供应商控制与验证体系
- 出处: VIII.A；chunk: ck-6a6ee7557ee9
- 原文关键句: "Factors that impact the potential for an ingredient to be a source of contamination include: The nature of an ingredient, including intrinsic factors such as pH and water activity; The manufacturing process for the ingredient; Supplier approval programs, programs that follow the practices described in this guidance for control of *L. monocytogenes*, and verification programs."
- 中文大意：决定"某配料是否可能成为污染源"的三个因素——①配料本身的性质（含 pH、aw 等内在特性）；②该配料的制造工艺；③供应商批准程序、遵循本指南李斯特菌控制实践的程序，以及验证程序。
- 类型: procedure
- 建议归属: 并入 `supply-chain-verification`（Step 1 或新增"配料风险画像"小节）
- 为什么是现有技能缺口: 现有供应链卡的批准四因素〔§ 117.410(d)〕是**通用法规四因素**（危害分析/控制实体/表现/储运），没有"**从李斯特菌视角看配料本身有多危险**"这套判据——例如一个 pH 4.2 的酸性配料与一个鲜切蔬果的 L. mono 携带概率完全不同。缺这条会把所有配料当成同质风险源。

### nC-20 已实施有效 listericidal 措施的原料可视为"不太可能带菌"——但须核实供应商的验证与持续防再污染
- 出处: VIII.A；chunk: ck-6a6ee7557ee9
- 原文关键句: "Raw materials and other ingredients processed with an adequate listericidal control measure that has been validated are not likely to contain *L. monocytogenes*. Examples of adequate listericidal control measures include: Aseptically processed and packaged; Retorted (e.g., canned); Ethylene oxide treated or irradiated in the package; Pasteurized (or equivalent treatment) in the package… We recommend that you verify that your supplier has validated the process and has programs to ensure that the process is being appropriately implemented and that recontamination is prevented on an ongoing basis."
- 中文大意：经过**已验证的**充分 listericidal 措施处理的原料与配料不太可能含李斯特菌；充分 listericidal 措施的示例包括：无菌加工并包装、retort（罐头）、环氧乙烷处理或包装内辐照、包装内巴氏杀菌（或等效处理）、包装内其他获批致死技术。但须核实供应商**已验证该工艺、且有程序保证工艺被适当实施并持续防止再污染**。
- 类型: fact / procedure
- 建议归属: 并入 `supply-chain-verification`（Step 1/2：可接受的"已控制"原料类型清单）
- 为什么是现有技能缺口: 现有卡讲的是"危害由供应商控制时怎么办"，**没有给出"哪些类型的原料可以视为已被上游解决"的白名单**——这是供应链控制的第一道分流，能显著减少不必要的后续验证负荷。

### nC-21 原料控制的首选顺序：优先对原料施加 listericidal 措施，其次才是供应链控制
- 出处: VIII.B.1 / VIII.B.2；chunk: ck-27fac5369252（防交叉污染）、ck-a10793caa296（施加 listericidal）
- 原文关键句: "We recommend that you establish measures to prevent cross-contamination of finished RTE food by raw materials and other ingredients. In the absence of adequate information … handle raw foods, and any other food raw materials and other ingredients that could be contaminated with *L. monocytogenes*, as if they are contaminated with *L. monocytogenes*." / "We recommend that, where practical, you treat raw materials and other ingredients for which it is reasonably foreseeable that they will be contaminated with *L. monocytogenes* with a listericidal control measure during the manufacturing process, e.g., before a specific raw material or other ingredient is used in manufacture, or at an in-process stage of manufacture when the raw material or other ingredient is part of a mixture of ingredients."
- 中文大意：①对可能带菌的原料按"视同已污染"处理（防交叉污染）；②**在可行时**（where practical），对可预见会带菌的原料在制造过程中施加 listericidal 控制措施——可以在该配料**投入使用之前**，或在配料已并入混合物后的**某个在制品工序节点**实施。
- 类型: procedure / rule
- 建议归属: 并入 `supply-chain-verification`（Step 1 控制主体映射的"上移"选项）
- 为什么是现有技能缺口: 现有卡的控制主体选项主要是"供应商控制 vs 本厂控制"，本条给出**第三种更优先的做法**：本厂在配料进入制造前或在制品阶段就把它杀掉——它同时解决了供应链验证负担。现有卡未把这一选项排在供应链程序之前。

### nC-22 供应链控制优先于逐批检测（指南明确表态），检测只是验证控制有效性的补充工具
- 出处: VIII.B.3；chunk: ck-79ee16d62224
- 原文关键句: "We recommend that you establish and implement supply-chain controls designed to reduce the potential that the ingredient or other raw material received from a supplier is contaminated with *L. monocytogenes*. We recommend controls established in collaboration with your suppliers, rather than testing individual lots of raw materials or other ingredients, because limitations on product sampling make product testing a tool that primarily adds value in verifying the adequacy of control measures over time."
- 中文大意：应建立并实施**与供应商协同制定**的供应链控制，而不是逐批检测原料；理由是**产品抽样的固有局限**使产品检测主要只能作为"随时间验证控制措施是否充分"的工具。
- 类型: rule
- 建议归属: 并入 `supply-chain-verification`（B1 边界：检测能否作唯一手段 → 补 L. mono 专项口径）
- 为什么是现有技能缺口: 现有卡 B1 已有"法规允许但指南不鼓励"的分层表述，但那是**通用**（引 PCHF 指南）；本条是**李斯特菌专项**且给出了明确理由（抽样局限），措辞更硬。对 L. mono 尤其实用，因为单批抽检阴性几乎无法排除低水平、分布不均的污染。

### nC-23 供应商控制的三件套要求：书面批准程序（含审核其环境监测）、现场审核、COA/COC 的具体内容要求
- 出处: VIII.B.3；chunk: ck-79ee16d62224
- 原文关键句: "Developing a written supplier approval program based in part on control measures the supplier has implemented for *L. monocytogenes*… As part of this program, we recommend that you verify any applicable supplier environmental monitoring program, including results. Auditing the supplier's plant… Obtaining the raw material or other ingredient under a supplier's Certificate of Conformance (COC)… Any COC that you rely on include the period of guarantee, product safety specifications, and a statement that the supplier's raw materials … are produced under conditions that are consistent with this guidance and in compliance with part 117 … You obtain that COC and conduct an onsite audit of the supplier on at least an annual basis."
- 中文大意：①建立**书面**供应商批准程序，依据供应商针对李斯特菌实施的措施，并核实其环境监测程序**及其结果**；②现场审核供应商工厂，评估其原料生产条件是否与本指南一致；③若用 COC：COC 须含保证期、产品安全规格、以及"原料在符合本指南且符合 part 117 的条件下生产"的声明，并且**至少每年**取得该 COC 并做一次现场审核；④若用 COA：COA 须含**抽样方案、检测结果、所用分析方法及该方法的检出限**，并须留意检测局限（§ VIII.B.5）。
- 类型: procedure / rule
- 建议归属: 并入 `supply-chain-verification`（Step 2 批准 / Step 3 持续验证：COA/COC 的李斯特菌专项字段清单）
- 为什么是现有技能缺口: 现有卡给了**法规层**的保证格式要件〔§ 117.335〕与记录字段〔§ 117.475(c)〕，但没有**李斯特菌专项**的 COA/COA 内容要求——尤其"COC 至少每年取得一次 + 每年现场审核"这一对，以及"COA 须写明检出限"这一项。缺这些，用户拿到供应商 COA 时无法判断该接受还是该加验。

### nC-24 COC 与 COA 两种原料控制路径的差异化验证节奏（信任曲线）
- 出处: VIII.B.4；chunk: ck-0c12442e8de9
- 原文关键句: "If your controls … include a COC … we recommend that you periodically test raw materials and other ingredients received under the COC to verify the efficacy of the supplier's control programs. The frequency … should be sufficient to maintain confidence that the supplier's control programs are effective and could be reduced if the results of your audits and verification tests demonstrate compliance… If … include a supplier's COA … we recommend that you verify the results of the supplier's COA on multiple lots … until you have enough experience with that supplier to be confident in the results provided on the COA. After you have established confidence in your supplier, we recommend that you continue to test … (e.g., weekly, monthly, or quarterly, based on risk)…"
- 中文大意：COC 路径——**周期性**抽测以验证供应商控制体系的有效性，频次以维持信心为准；若审核与验证检测结果持续符合规格与 COC，频次**可以降低**。COA 路径——先在**多批**上核实 COA 结果直至对供应商建立信心，之后仍按风险**定期**（周/月/季）抽测。两条路径都要求建立并遵循书面的取样与检测程序（抽样方案、取样程序、前处理程序、分析方法），并参照第 XVII 章。
- 类型: procedure
- 建议归属: 并入 `supply-chain-verification`（Step 3 持续验证：把"检测信任曲线"拆成 COC / COA 两套节奏）
- 为什么是现有技能缺口: 现有卡 Step 2 只有一条通用的"检测信任曲线：批准前多批实测→逐批→建立信心后季度"。本指南把信任曲线**按 COC 与 COA 分成两条不同逻辑**（COC 路径允许降频，COA 路径要求建立信心后仍定期），这是可直接落进 SOP 的差别。

### nC-25 原料侧记录清单（6 项）与"仅以检测作为原料控制手段"时的三条附加要求
- 出处: VIII.C / VIII.D；chunk: ck-40ee4cb1cbd5（记录）、ck-6423f9faad61（检测作为唯一控制）、ck-dff89a0b65e1（条款）
- 原文关键句: "We emphasize that testing a single lot of a food product for *L. monocytogenes* is of limited value in establishing the acceptability of that lot and cannot substitute for appropriate controls on its manufacture/processing. The primary value of product testing is as part of a history of test results that is used to verify the adequacy of control measures over time." / "Such testing should be more frequent if your final product is not formulated to prevent the growth of *L. monocytogenes*. You should have a process in place to segregate and hold all raw materials or other ingredients that are tested prior to use and products that will be affected by test results."
- 中文大意：(a) 单批检测在判定该批可否接受上**价值有限**，不能替代对制造/加工过程的适当控制；检测的主要价值是构成"随时间验证控制措施充分性"的历史序列。(b) 若选择只检测而不建立供应商控制，则检测频次应与供应商既往结果所显示的降低能力相称，**且当成品配方不能抑制李斯特菌生长时须更频繁**。(c) 须建立**隔离并暂扣**流程：待检原料以及会受检测结果影响的产品，全部隔离暂扣。
- 类型: rule / procedure
- 建议归属: 并入 `supply-chain-verification`（Step 3/Step 4：检测作为唯一手段时的三附加条件）+ `management-components`（Step 3 暂存待评估）
- 为什么是现有技能缺口: 现有卡有"检测信任曲线"但没有这三条例外规则。其中"**成品配方不能抑制李斯特菌生长 → 原料检测须更频繁**"是本指南独有的耦合规则：原料检测频次由**成品抑制能力**反向决定。

### nC-26 储存控制：FIFO 与"最短 use by 优先"作为程序要求，以及时间/温度控制须"验证其持续达成"
- 出处: XI；chunk: ck-5eeb6c957c8a
- 原文关键句: "…we recommend that you establish and implement procedures to minimize the potential for an increase in numbers of any *L. monocytogenes* that could be present. An example … minimizing the amount of time that ingredients and other raw materials, in-process materials, and finished foods are stored under conditions that allow growth… In particular, we recommend that you establish and follow procedures to use such materials on a first-in, first-out basis or to use those with the shortest 'use by' date first." / "We also recommend that you establish and implement measures to verify time/temperature control on an ongoing basis."
- 中文大意：①李斯特菌**在冷藏温度下仍能缓慢繁殖**，但冷藏仍是一项关键控制措施；②建立并实施程序，尽量缩短原料、在制品与成品处于允许生长条件下的存放时间，**特别地**建立并执行**先入先出（FIFO）**或**最短"use by"日期优先**的使用程序；③建立并实施**持续验证时间/温度控制**的措施，确保其被一致地应用与达成。
- 类型: procedure / rule
- 建议归属: 并入 `process-control-validation`（新增"储存时间/温度控制"小节）或 `management-components`（Step 1 监控 + Step 4 验证）
- 为什么是现有技能缺口: 现有卡 Step 5 只把冷却协议（135→70→41°F 两段式）作为工艺危害陷阱处理，**没有覆盖成品/原料的常规储存期**这一段；FIFO 与"最短 use by 优先"是可写进 SOP 的具体程序，缺失。

### nC-27 储存温度缺省值 4°C（约 40°F）或以下；更高温度须以 PMO/Food Code 为依据；冷冻抑生长但不灭菌
- 出处: XI 尾部；chunk: ck-16497f94f9de（该 chunk 标题错位为 XII. Transportation）
- 原文关键句: "In the absence of specific data or other information about appropriate time/temperature controls for your particular operations, we recommend that RTE foods be stored at 4°C (~40°F) or below; higher temperatures may be appropriate when consistent with the Pasteurized Milk Ordinance or Food Code. … *L. monocytogenes* does not grow at temperatures below freezing. Therefore, freezing is a particularly effective temperature control measure to prevent growth during storage. Freezing will not eliminate *L. monocytogenes* from foods and cannot be relied upon as a control measure for the elimination or reduction of *Listeria monocytogenes*."
- 中文大意：缺乏针对本厂作业的特定数据或信息时，建议 RTE 食品在 **4°C（约 40°F）或以下**储存；更高温度在符合《Pasteurized Milk Ordinance》或《Food Code》时可能适当。李斯特菌在冰点以下不生长，故**冷冻是特别有效的温度控制措施**（防止储存期生长）；但冷冻**不会消除**食品中的李斯特菌，**不能**作为消除或减少李斯特菌的控制措施。
- 类型: threshold / rule
- 建议归属: 并入 `process-control-validation`（Step 5 工艺危害陷阱）或 `environmental-pathogen-sanitation`（储存环节）
- 为什么是现有技能缺口: 现有卡的冷藏基准来自 PCHF 指南的"危险区 41–135°F（5–57°C）"与冷却协议（终点 41°F）。本指南给出**储存缺省值 4°C（40°F）**，比危险区下限 5°C 更严——两者是不同用途的数值（见第三节 kC-04）。"冷冻不是消除措施"这一句在现有卡里只有"冷冻储运是 ROP 五屏障之一"的正面表述，没有反面的否定句。

### nC-28 运输控制：装卸前检查车辆、预冷并记录装车前温度、槽车/散装容器的专用化或防交叉污染程序
- 出处: XII；chunk: ck-16497f94f9de（正文后半，同上 chunk）
- 原文关键句: "We recommend that you inspect transportation vehicles (trailers and tankers) for structural integrity, cleanliness, and overall suitability when unloading ingredients and prior to loading finished products. … You should ensure food products are at the target temperature before loading the product into refrigerated trucks, which are designed to maintain a temperature but not to cool a product to the target temperature. Refrigerated vehicles should be pre-cooled with the pre-loading temperature documented prior to loading product. We recommend that you either dedicate any tankers or repeat use bulk containers … to those specific uses or that you establish and implement procedures to prevent contamination from previously transported products. You should verify that the tanker or container has been adequately cleaned and sanitized prior to use (e.g., via wash tag from tanker wash facilities with validated washing procedures)."
- 中文大意：①**卸原料时**与**装成品前**检查运输车辆（拖车、槽车）的结构完整性、清洁度与整体适用性；②**产品须在装车前已达到目标温度**——冷藏车只维持温度、不负责把产品冷却到目标温度；冷藏车须**预冷**并**记录装车前温度**；③槽车或重复使用的散装容器应**专用化**，否则须建立防止前载货物污染的程序，并核实使用前已充分清洁消毒（可用有验证清洗程序的槽车清洗厂出具的**洗车标签 wash tag** 佐证）。
- 类型: procedure / rule
- 建议归属: 并入 `supply-chain-verification`（Step 4 储运条件 / 成品配送）或建议新能力 `transportation-and-distribution-controls`
- 为什么是现有技能缺口: 现有供应链卡只在批准四因素里提过"储运条件"一词，**没有运输环节的可执行要求**；尤其"**装车前产品须已达目标温度**"与"**预冷温度须留记录**"是两条能直接落成表单的要求，"洗车标签"还是一个具体的、可被审计的记录物。

### nC-29 成品抽检：应检 L. monocytogenes 而非 Listeria spp.；spp. 阳性须判定是否 L. mono，否则按 L. mono 污染处理
- 出处: XIV.A；chunk: ck-8ed5f7ced929
- 原文关键句: "We recommend that you test food products for *L. monocytogenes* rather than for *Listeria* spp. because of the risk to public health from *L. monocytogenes* in food. If you choose to test food for *Listeria* spp. and find it to be positive, we recommend you determine whether the *Listeria* spp. is *L. monocytogenes* or treat the food as if it were contaminated with *L. monocytogenes*. We recommend that you hold all product that is represented by the food you test, e.g., food lots produced from cleanup to cleanup."
- 中文大意：成品检测**应针对 L. monocytogenes** 而非 Listeria spp.（因前者对公共健康的风险）；若选择检 Listeria spp. 且呈阳性，须判定是否 L. monocytogenes，**否则按 L. monocytogenes 污染处理**；须暂扣**由被检样所代表的所有产品**，例如同一 cleanup 到 cleanup 之间的批次。
- 类型: rule / procedure
- 建议归属: 并入 `management-components`（Step 4 验证活动：产品检测）+ `environmental-pathogen-sanitation`（cleanup to cleanup 口径）
- 为什么是现有技能缺口: 现有卡讲的是"环境监测检 Listeria spp. 而非 L. mono"（理由是环境监测关注定殖与指示物），但**成品检测方向相反**——成品应直接检 L. mono。这个"同一个病原、两种检测方向、理由相反"的对比是本指南的高价值增量，缺了会导致用户把环境监测的做法照搬到成品检测上。

### nC-30 成品抽检频次与抽样方案的三个决定变量（客户要求 / 食源性疾病风险 / 环境样品中 Listeria spp. 的检出频率）
- 出处: XIV.A；chunk: ck-8ed5f7ced929
- 原文关键句: "We recommend that you establish and implement a written procedure for the periodic collection of samples of your RTE food product… Your written procedure should include the frequency of sampling (e.g., monthly, quarterly) and the sampling plan. The frequency of sampling and the sampling plan will depend on many things, such as customer requirements, the risk of foodborne illness if the finished product is contaminated with *L. monocytogenes*, and the frequency of detection of *Listeria* spp. in environmental samples."
- 中文大意：建立并实施书面的周期性取样程序，程序应写明**抽样频次**（如每月、每季）与**抽样方案**；频次与方案的确定依赖三方面——①客户要求；②成品被污染后引发食源性疾病的风险；③**环境样品中 Listeria spp. 的检出频率**。
- 类型: procedure
- 建议归属: 并入 `management-components`（Step 4 验证活动选择：频次裁剪须书面依据）+ `environmental-pathogen-sanitation`（环境数据反哺成品抽检频次）
- 为什么是现有技能缺口: 现有卡要求"频次裁剪须以暴露史论证并书面化"〔§ 117.155〕，但没有给出**李斯特菌场景下频次由什么决定**的可操作变量集；尤其第三条（环境检出频率驱动成品抽检频次）是一条**跨程序联动规则**，现有卡完全没有。

### nC-31 成品阳性后的处置与"两次清洁消毒之间批次" implicated 规则、hold and test 与召回判定
- 出处: XIV.B；chunk: ck-30a8e65f8e6d（该 chunk 标题错位为 XV.A）
- 原文关键句: "You reprocess with a validated listericidal control measure, divert to a use in which the food will not be consumed by humans or animals, send for use in food to be consumed by animals where appropriate, or destroy the lot(s) of RTE food in which *L. monocytogenes* has been detected. You should consider lots produced between two cleaning and sanitizing cycles to be implicated by the product positive… We recommend that you subject potentially contaminated lots to 'hold and test' procedures… Your corrective actions regarding your plant and your procedures include intensified sampling and testing of FCSs and non-FCSs … until you find the source of contamination and eliminate it; and You determine whether food in commerce would be subject to a recall."
- 中文大意：成品检出 L. mono 时的四条处置路径——①用**已验证的 listericidal 控制措施再加工**；②改作人类/动物不食用的用途（改作动物食用饲料、转饲料）；③销毁检出批次。**应把两次清洁消毒周期之间生产的所有批次视为受牵连**；其他可能受污染批次须**隔离暂扣**并按"hold and test"程序处理；针对工厂与程序的纠正措施包括**强化 FCS 与 non-FCS 的采样检测**直到找到并消除污染源；并判定已入市产品是否须**召回**。
- 类型: procedure
- 建议归属: 并入 `management-components`（Step 3 处置阶梯：新增"已验证 listericidal 再加工"作为首选路径）+ `recall-plan`（召回判定触发）
- 为什么是现有技能缺口: 现有卡的处置阶梯里"再加工"没有指明**再加工必须用已验证的 listericidal 措施**；且"cleanup to cleanup"的牵连口径在现有卡里只出现在过敏原场景（管理组件卡 Step 3），未推广到**成品 L. mono 阳性**这一场景。

### nC-32 趋势分析：环境数据与产品数据两套趋势，及"耐受株已在 niche 定殖"的判读
- 出处: XV.A / XV.B；chunk: ck-e67680f96bf6（环境趋势）、ck-2b1cc488789d（产品趋势）
- 原文关键句: "We recommend that you analyze the data you collect through your environmental monitoring program over time for trends that can help you to continuously improve sanitation conditions in your plant by reducing the percentage of overall positive environmental samples in your plant. This trend analysis could provide evidence that *L. monocytogenes* in your plant is not being controlled (e.g., if a resident strain has become established in a niche environment)…"
- 中文大意：环境监测数据须**随时间做趋势分析**，目标是持续降低全厂环境样品阳性率；趋势分析可作为"李斯特菌未被控制"的**证据**——典型如**耐受株（resident strain）已在某个 niche 环境中定殖**。三类上升信号：特定点位/区域阳性数增加；同一区域在**多个但非连续**采样时点反复检出 Listeria（看似孤立阳性）；全厂环境样品阳性率上升。产品检测数据同样须做趋势分析：阳性检出率上升即须调查原因并采取纠正措施。
- 类型: procedure / rule
- 建议归属: 并入 `environmental-pathogen-sanitation`（趋势分析）+ `management-components`（Step 6 动态维护：趋势作为再分析触发器）
- 为什么是现有技能缺口: 现有卡的"动态维护"只列了**事件触发器**与 3 年周期，没有把**趋势分析本身**列为一项须主动执行的法定活动；本指南明确"趋势分析能提供李斯特菌未被控制的证据"并给出三类信号，是可执行的诊断工具。

### nC-33 培训：李斯特菌专项培训的对象、时机、频次，以及四类须"成功完成"培训的主管职责
- 出处: XVI；chunk: ck-063336b7fe8a
- 原文关键句: "We recommend that you provide training in health and hygienic practices specific to control of *L. monocytogenes* for all personnel and contractors who enter production and storage areas … The training should emphasize each individual's role in control of *L. monocytogenes*, why that role is important, and management's expectations for adherence to the program. We also recommend that the training be conducted before the individual performs job activities, with refresher training on at least an annual basis. We recommend that personnel who supervise or are otherwise responsible for the activities listed below successfully complete training in the application of the principles of the practices recommended in this guidance… [e]stablishing effective listericidal and listeristatic controls …; [c]ollecting and testing environmental samples and samples of RTE food products; [d]etermining and taking corrective actions; and [e]stablishing and using written sanitation procedures and conducting associated monitoring."
- 中文大意：①**专项培训对象**＝所有进入生产区与储存区的人员**及承包商**（含生产、维护、QA/QC、仓储人员）；内容强调"我的角色在李斯特菌控制中是什么、为什么重要、管理层对遵守的期待"；②**时机**＝上岗前完成，**至少每年**复训；③四类须**成功完成**本指南原则应用培训的人员：建立并保证 listericidal 与 listeristatic 控制有效运行者、采集与检测环境样品及 RTE 成品样品者、判定并采取纠正措施者、建立与使用书面卫生程序并执行相关监测者。
- 类型: procedure / rule
- 建议归属: 并入 `management-components`（Step 1 监控设计的 Who 栏 / Step 7 PCQI 职能：培训矩阵）
- 为什么是现有技能缺口: 现有卡只引了通用义务〔§ 117.4(b)(2)〕（含临时/季节工培训、7 个工作日记录审查等）。本条给出**李斯特菌专项培训的对象范围（承包商）、上岗前+年度复训节奏、以及按"控制类型"划分的四类职责人清单**——可直接做出一张培训矩阵表。

### nC-34 采样/前处理/检测的方法指定：环境样、食品样各用哪套官方方法，以及"替代方法"的法定式门槛
- 出处: XVII；chunk: ck-8796ee572efb（方法指定）、ck-0621164c6659（自检与替代方法）
- 原文关键句: "Use the procedures described in Appendix 5 for preparing environmental samples for analysis. Use FDA's 'Testing Methodology for *Listeria* species or *L. monocytogenes* in Environmental Samples' (Ref. 60) for testing environmental samples. Use the procedures described in FDA's Bacteriological Analytical Manual Online (BAM) … for preparing food samples and testing them for the presence of *L. monocytogenes*." / "If you or an outside commercial testing laboratory use an analytical method other than those we recommend in this section, we recommend that the method be a written, scientifically valid method that is at least equivalent to the recommended method in accuracy, precision, and sensitivity for detecting *Listeria* spp. and *L. monocytogenes*."
- 中文大意：环境样品——按**附录 5** 前处理，按 FDA《Testing Methodology for *Listeria* species or *L. monocytogenes* in Environmental Samples》（Ref. 60）检测；食品样品——按 **FDA BAM（在线版）** 前处理并检测。检测可自做，也可委托外部商业实验室。若采用**非推荐方法**，该方法必须是**书面的、科学有效的**，且在**准确性、精密度、检出灵敏度**上**至少等同**于推荐方法。
- 类型: procedure / rule
- 建议归属: 并入 `reference-tools-discipline`（数据与方法的合格性判据）+ `environmental-pathogen-sanitation`（检测方法指定）
- 为什么是现有技能缺口: 现有卡讲"权威工具自带失真警告"，但没有"**什么算合格的方法**"这一可核验的三维判据（准确/精密/灵敏），也没给环境样与食品样各用哪套官方方法的分工——而选错方法（前处理按食品 BAM 用于环境样）会直接毁掉监测结果的意义。

### nC-35 书面程序须至少每年复审更新一次（指南在记录章末尾给出的周期性要求）
- 出处: XVIII；chunk: ck-e02f6b4f7d7c
- 原文关键句: "We recommend that you review and update, as needed, your written procedures at least once a year."
- 中文大意：应**至少每年**复审并按需更新书面程序。
- 类型: rule / procedure
- 建议归属: 并入 `management-components`（Step 5 记录体系 / Step 6 动态维护：程序年度复审）
- 为什么是现有技能缺口: 现有卡的动态维护只有 **3 年**整体再分析与事件触发增量再分析，**没有"书面程序每年复审"这一更密的程序性节奏**（3 年是 FSP 整体再分析时钟，1 年是程序文件复审时钟，两者不同）。缺这条用户会以为程序写完就长期不动。

---

## 二、近重复（现有技能已覆盖，本指南可补细则/出处）

- rC-01: 抑制型配方有效性判据（<1 log 增幅）↔ 现有卡 `process-control-validation` 无对应；与候选 B 的 **nB-02**（引 II.B 同判据）重复——取本文件 nC-06 的 IX 章正式表述（多两个限定：两个以上时间间隔、重复试验 + 安全裕度）。
- rC-02: L. mono 生长三阈值 pH≤4.4 / aw≤0.92 / hurdles ↔ 候选 B 的 **nB-01**（引 II.B）——本文件 nC-03 为 IX 章官方列举，合并时去重。
- rC-03: 产品检测的效力定位（"主要价值是随时间验证控制措施充分性"）↔ 现有卡 `supply-chain-verification` B1（检测不能作唯一手段）+ `reference-tools-discipline`（权威表的先验性质）——本文件 nC-25 补"单批检测价值有限"这一层。
- rC-04: COA/COC 作为供应商验证活动与格式要件 ↔ 现有卡 `supply-chain-verification`（t64 COA/COC 词条、Step 2 保证与记录核对）——本文件 nC-23 补李斯特菌专项字段（COC 保证期+年度现场审核、COA 须含检出限）与 nC-24 的两套节奏。
- rC-05: 供应商年度现场审核与 SAHCODH 年审规则 ↔ 现有卡 `supply-chain-verification` Step 3（法规基线 + 书面认定通道）——本指南只要求"至少每年取得 COC 并现场审核"，未给偏离通道；**属细化而非新规则**，且不得与 § 117.430(b)(1) 的偏离机制混淆。
- rC-06: 记录保存期限与调阅义务（一般 2 年、设备/工艺记录停用后 2 年、FSP 须驻场）↔ 现有卡 `management-components` B3——本指南第十八章只列"记录什么"，未给期限；**期限仍以 Part 117 为准**，本指南不构成新依据。
- rC-07: 纠正措施四步（纠正并查明原因 / 降复发 / 评估全部受影响食品 / 阻止入市）↔ 现有卡 `management-components` Step 3〔§ 117.150〕——本文件 nC-09、nC-17 补充"包装前/包装后"这一时点分叉与"等效致死量补偿"这一具体动作。
- rC-08: 环境监测检 Listeria spp. 而非 L. mono 的理由（指示物 + 定殖判断）↔ 现有卡 `environmental-pathogen-sanitation` / 候选 A 的 nA-16——但成品检测方向相反（nC-29），两者须成对出现，避免用户混用。
- rC-09: 冷藏与冷冻作为控制手段 ↔ 现有卡 `process-control-validation` Step 5（ROP 五屏障含冷冻储运）+ `reference-tools-discipline` t81（a_w 0.85/0.92/0.93 三个数）——本文件 nC-27 补"冷冻不灭菌"的否定句与 4°C 缺省值。
- rC-10: hold and test 程序 ↔ 现有卡 `management-components` Step 3 + 候选 A 的 nA-28（ICMSF 抽样方案表）——本文件 nC-31 只引用其存在（"须走 hold and test 程序"），细节归 A。
- rC-11: zone 分区（FCS / non-FCS / Zone 1–4）与合样上限 5 个 ↔ 候选 A 的 nA-14、nA-21——本文件范围（XIV/XVII）未涉及，不重复。
- rC-12: 危害分析中 § 117.130(c)(1)(ii) 的强制触发器 ↔ 现有卡 `hazard-analysis-method` Step 3——本文件 nC-01 只补"适用/不适用分流"这一指南层判定。

---

## 三、潜在矛盾（⚠️ 数值基准差异是重点）

- **kC-01 ⚠️ pH 两套基准：4.6（法规通用/酸化管辖）vs 4.4（李斯特菌抑制型配方）**
  - 本指南侧：IX（ck-6e733495e327）："pH less than or equal to 4.4" 被列为 listeristatic 配方的三条路径之一；XIX.B 术语表（ck-57471f7d75bc）把 "Listeristatic formulation" 定义为 pH≤4.4 / aw≤0.92 / 组合抑菌因子。
  - 现有卡侧：`process-control-validation` Step 4：「酸/酸化食品的法定定义以**平衡 pH 4.6 或以下**为准（equilibrium pH，非初始或表观 pH）〔§ 117.3〕」；Step 5：「pH<4.6 控肉毒并兼 LACF/酸化管辖分界」；`glossary` t78/t80 同源。
  - 判定：**不是数值冲突，而是两套用途不同的基准**。4.6 = Part 117 酸化食品管辖边界（法定）；4.4 = 针对李斯特菌的抑制型配方设计目标（指南建议）。必须显式并列，否则用户会用"我做到 pH 4.5"同时误以为满足酸化食品法规要求 **和** 满足 L. mono 抑制目标——前者勉强成立，后者不成立（L. mono 在 pH 4.5 仍可生长）。

- **kC-02 ⚠️ aw 两套基准：0.85（安全水分水平/病原不生长）vs 0.92（抑孢子萌发 vs 抑制李斯特菌生长）**
  - 本指南侧：IX（ck-6e733495e327）与 XIX.B（ck-57471f7d75bc）：aw ≤ 0.92 是 listeristatic 配方的基准。
  - 现有卡侧：`process-control-validation` Step 5：「a_w≤0.85 控营养细胞 / ≤0.92 抑孢子萌发」；`reference-tools-discipline` t81：「a_w≤0.85 病原不能生长（S. aureus 界限）；a_w≤0.92 抑制芽孢萌发」。
  - 判定：**同一个数字 0.92 在两处含义不同**——现有卡把它绑定到"抑制芽孢萌发"（肉毒视角），本指南把它绑定到"抑制李斯特菌营养细胞生长"（李斯特视角）。合并时须在工艺控制卡的 0.92 旁补注"该值同时是 L. mono 抑制型配方的指南基准"；两个 0.85/0.92 不得互相替换使用。

- **kC-03 ⚠️ 致死度默认档位：5D–7D / 6D（通用默认）vs 5 log / 6 log（L. mono 专项兜底，按初始负荷切换）**
  - 本指南侧：X.A（ck-1d32883482a3）：初始负荷 ≤100 CFU/g → 5 log；>100 CFU/g 可预见 → 6 log；其他 log 数经适当验证亦可。
  - 现有卡侧：`process-control-validation` Step 2：「营养细胞病原 5D–7D；孢子目标 6D（锚点：L. mono 70°C/2.0 min）」。
  - 判定：**不矛盾，但本指南给出了现有卡缺的第二个自变量（初始负荷）**。危险误读：用户看到"5 log 就够"就按 5 log 设计，而忘了 100 CFU/g 的前提；或看到"6D 锚点"就以为 L. mono 必须 6D 而过度设计。两处须同时出现。

- **kC-04 ⚠️ 冷藏温度基准：4°C（40°F，本指南储存缺省值）vs 5°C（41°F，危险区下限 / 冷却终点 / Food Code）**
  - 本指南侧：XI（ck-16497f94f9de）："RTE foods be stored at 4°C (~40°F) or below"，更高温度须符合 PMO 或 Food Code。
  - 现有卡侧：`glossary` t37（危险区 41–135°F / 5–57°C）；`process-control-validation` Step 5（冷却 135→70°F ≤2h、70→41°F ≤4h）。
  - 判定：**用途不同导致的数值差**——41°F/5°C 是危险区下限与冷却终点（法规与 Food Code 口径），4°C/40°F 是本指南针对李斯特菌储存的**建议缺省值**（更严）。二者不冲突，但同一份 FSP 里出现两个冷藏数字会造成解释混乱，须标明用途。另外本指南把"更高温度"挂到 PMO/Food Code 上，即 4°C 是**建议缺省**而非法定门槛。

- **kC-05 ⚠️ 成品检测对象：Listeria spp.（环境监测）vs L. monocytogenes（成品检测）**
  - 本指南侧：XIII.A（候选 A nA-16）检 Listeria spp.；XIV.A（ck-8ed5f7ced929）"We recommend that you test food products for *L. monocytogenes* rather than for *Listeria* spp."。
  - 现有卡侧：`environmental-pathogen-sanitation` 强调环境监测检 spp. 以指示定殖。
  - 判定：**同一病原、两种检测方向、理由相反**——不是矛盾而是分工，但极易被用户混用，须成对呈现。

- **kC-06 成品阳性后的牵连范围：cleanup to cleanup（过敏原场景已覆盖）vs 本指南把它用于 L. mono 成品阳性**
  - 本指南侧：XIV.B（ck-30a8e65f8e6d）"lots produced between two cleaning and sanitizing cycles to be implicated by the product positive"。
  - 现有卡侧：`management-components` Step 3 有 cleanup to cleanup 口径，但明确挂在过敏原场景下。
  - 判定：**扩展而非冲突**，须把该口径的适用范围扩到成品 L. mono 阳性场景。

- **kC-07 抽样检测能否作为唯一控制手段**
  - 本指南侧：VIII.B.3/B.5（ck-79ee16d62224、ck-6423f9faad61）：优先供应链控制而非逐批检测；若坚持以检测为唯一手段，须加频次规则与隔离暂扣流程。
  - 现有卡侧：`supply-chain-verification` B1：法规允许（除 SAHCODH 年审外），但指南不鼓励。
  - 判定：**未发现实质矛盾**；本指南比通用表述更硬，且补了"成品不能抑制李斯特菌生长时须更频繁"这一增量条件。

- **kC-08 培训义务层级：§ 117.4 通用卫生培训 vs 本指南李斯特菌专项培训**
  - 本指南侧：XVI（ck-063336b7fe8a）：专项培训 + 上岗前 + 年度复训 + 四类职责人"成功完成"。
  - 现有卡侧：`management-components` Step 1 仅引〔§ 117.4〕。
  - 判定：**未发现矛盾**——属叠加（Draft 建议层），但引用时须标明"指南建议"而非"法规要求"。

- **kC-09 记录保存期限**
  - 本指南侧：XVIII（ck-e02f6b4f7d7c）只列记录内容与"每年复审书面程序"，**未给期限**。
  - 现有卡侧：`management-components` B3 给出 Part 117 三类期限（2 年 / 支撑 qualified facility 身份 / 停用后 2 年）。
  - 判定：**未发现矛盾**；不得用本指南的"年度复审"去覆盖或替代法规的保存期限义务。

---

## 四、术语表新增建议（来自 XIX Glossary）

> 现有 glossary 共 85 条（t01–t85，见 `.cangjie/capabilities/book/glossary.md`）。下列条目按"现有 glossary 缺失"筛选；已存在同义条目的（t33 harborage site/niche、t64 COA/COC、t38 lethality treatment、t13 operating limits、t24 prerequisite programs、t83 cleaning/sanitize、t08 FSP、t21 validation、t22 verification）列入第四节末尾的"跳过项"并说明理由。术语格式沿用现有：`id / title / type / source_chapter / source_quote / summary / tags`。

- **t86** / title: listeristatic formulation（抑制型配方）/ type: term / source_chapter: XIX Glossary B（ck-57471f7d75bc）；定义与 IX 一致（ck-6e733495e327）
  - source_quote: "Listeristatic formulation: pH less than or equal to 4.4; water activity less than or equal to 0.92; and formulations (including those established in whole or in part through processes such as fermentation or culturing) containing a combination of factors scientifically demonstrated to be effective in preventing growth."
  - summary: 三条路径并列的**抑制型**配方定义。与 listericidal control 的区别是本术语只承诺"阻止生长"不承诺"杀灭"；与法规的 acid foods（平衡 pH≤4.6）**不是同一基准**——4.4 是李斯特菌专用的抑制目标。典型形态：发酵/培养型配方。
  - tags: [指南自定义, 配方控制, 核心概念, Lmono专有, 高频误读]

- **t87** / title: listericidal control（致死型控制）/ type: term / source_chapter: XIX Glossary B（ck-57471f7d75bc）；定义另见 X.A（ck-1d32883482a3）
  - source_quote: "Listericidal control: a control that will consistently destroy viable cells of *L. monocytogenes* and consistently leads to a finished food that contains less than 0.04 colony forming units (CFU) of *L. monocytogenes* per gram (g) of food."
  - summary: 定义用**成品可检出性**（<0.04 CFU/g，即 <1 CFU/25 g）而非 log 数表述——是"结果定义"而非"强度定义"，因此必须与所用方法的检出灵敏度绑定阅读。常见误读：把"5 log"当成 listericidal 的定义；实际 5/6 log 是**兜底路径**（按工艺前初始负荷 ≤/>100 CFU/g 切换），且只在无科学研究时使用。
  - tags: [指南自定义, 致死工艺, 核心概念, Lmono专有, 高频误读]

- **t88** / title: adequately reduce（充分减少）/ type: term / source_chapter: XIX Glossary B（ck-c042068fe0ff）
  - source_quote: "Adequately reduce: capable of reducing the presence of *L. monocytogenes* to an extent sufficient to prevent illness."
  - summary: 本指南对"减少到什么程度算够"的**结果导向**表述——标准是"足以预防发病"，不是"降了多少 log"。与法定 significantly minimize（t23，"降到可接受水平，包括消除"）不同：本条锚定**发病后果**（prevent illness），更适合用来判断某个 listericidal 工艺是否够格。
  - tags: [指南自定义, 核心概念, Lmono专有, 易混术语]

- **t89** / title: zone（分区）/ type: term / source_chapter: XIX Glossary B（ck-57471f7d75bc）
  - source_quote: "Zone means a designation about a surface or area reflecting how near that surface or area is to a ready-to-eat food and the risk the surface or area poses to ready-to-eat food if the surface or area is contaminated with *L. monocytogenes*."
  - summary: 按"**离 RTE 食品有多近**"给表面/区域打的等级标签，是环境监测采样频次与纠正措施严格度的分配依据（四区示例见附录 Table 4）。与既有 t35 hygienic zoning（按生/熟/湿/干做物理分隔）是两回事：zone 是**风险分级标签**，不必然有物理隔离。
  - tags: [指南自定义, 环境监测, 卫生分区, Lmono专有]

- **t90** / title: non-food-contact surface (non-FCS)（非食品接触面）/ type: term / source_chapter: XIX Glossary B（ck-57471f7d75bc）
  - source_quote: "Non-food-contact surface (non-FCS) any surface that, under normal operating procedures, does not contact food or the food-contact surfaces of equipment. Examples … equipment, vents, fixtures, drains, walls, floors, and employee clothing, shoes, and accessories."
  - summary: 判定式定义——"在**正常操作程序下**不接触食品、也不接触设备的食品接触面"。两个易错点：①判定前提是"正常操作程序"，异常工况（溢流、泄漏、飞溅）可使非 FCS 变成实际接触面；②示例包含员工衣物鞋履与配件——所以它同时是人员控制与手套更换规则的挂钩点。
  - tags: [指南自定义, 环境监测, 卫生, Lmono专有]

- **t91** / title: hold and test procedures（暂扣待检程序）/ type: term / source_chapter: XIX Glossary B（ck-57471f7d75bc）；用法见 XIII.F.3 与 XIV.B（ck-30a8e65f8e6d）
  - source_quote: "Hold and test procedures: procedures establishing the criteria for releasing product after receiving the results of tests conducted to determine the presence of a pathogen on an FCS."
  - summary: **先暂扣、后凭检测结果放行**的成文程序。关键点：它不是"检出才隔离"，而是**事先写好放行准则**（什么结果放行、什么结果处置），所以必须在产品流向市场之前就已存在——事后再补就失去意义。与管理组件里的"暂存待 PCQI 评估"不同：hold and test 的放行依据是**检测结果**。
  - tags: [指南自定义, 环境监测, 记录, Lmono专有, 高频误读]

- **t92** / title: environmental sample（环境样品）/ type: term / source_chapter: XIX Glossary B（ck-c042068fe0ff）；脚注 9 交叉引用见 ck-2c7761af6908 段内
  - source_quote: "Environmental sample: A sample that is collected from a surface or area of the plant for the purpose of testing the surface or area for the presence of microorganisms, usually environmental pathogens."
  - summary: 从厂房**表面或区域**采集、用于检验该表面/区域上微生物（通常是环境病原）的样品。定义里"**区域**"这一项易被忽略——擦拭取样之外还有整块区域取样（如地漏、地沟），二者的前处理与判定不同。环境监测优于产品检测的理由：环境监测能定位污染源，产品检测只能给出历史基准。
  - tags: [指南自定义, 环境监测, Lmono专有]

- **t93** / title: control point (CP)（控制点）/ type: term / source_chapter: XIX Glossary B（ck-c042068fe0ff）
  - source_quote: "Control point (CP): Any step at which biological, physical, or chemical factors can be controlled."
  - summary: 可施加控制的步骤——**比 CCP 宽**。与 t11（CCP：控制对预防/消除危害 essential）与 t12（critical limit：安全红线）构成三级：步骤（CP）→ 关键点（CCP）→ 关键限值（CL）。常见误读：把"可控制"直接等同于"关键控制点"——CP 只说明该步骤在技术上可干预，不说明它对特定危害是关键。
  - tags: [指南自定义, HACCP, 易混术语]

- **t94** / title: severity（严重性）/ type: term / source_chapter: XIX Glossary B（ck-57471f7d75bc）
  - source_quote: "Severity: The seriousness of the effects of a hazard."
  - summary: 危害后果的严重程度——是危害分析严重性×概率双维评估的第一维。定义极简，故意不列举等级：FDA 在 Part 117 语境下把等级划分留给评估者与 PCQI，但要求**书面**。可与 t67（SAHCODH：一个可操作化的严重性门槛）配读。
  - tags: [指南自定义, 危害层级]

- **t95** / title: Listeria species (Listeria spp.)（李斯特菌属）/ type: term / source_chapter: XIX Glossary B（ck-57471f7d75bc）
  - source_quote: "Listeria species (Listeria spp.): microorganisms within the genus *Listeria*, including the species *L. monocytogenes*."
  - summary: 属级概念——**包含** L. monocytogenes。用途边界：环境监测与部分成品筛查用 spp. 层级（覆盖面广、便于识别定殖），但成品检测应指向 L. mono 本身；成品检 spp. 阳性时须判定是否 L. mono，否则按 L. mono 污染处理。
  - tags: [指南自定义, 检测, Lmono专有, 高频误读]

- **t96** / title: food safety system（食品安全体系）/ type: term / source_chapter: XIX Glossary B（ck-c042068fe0ff）
  - source_quote: "Food Safety System: The result of the implementation of a food safety plan."
  - summary: FSP（t08，文档）**落地运行后的结果**——文档与体系是两件事。与 t08 配读可避免"文件齐了=体系有效"的误读（现有卡供应链 B3 已点名这种"书面体系≠真实安全"的失败模式）。
  - tags: [指南自定义, 核心概念, 高频误读]

- **t97** / title: clean in place (CIP) / clean out of place (COP)（原位清洗 / 拆位清洗）/ type: term / source_chapter: XIX Glossary B（ck-c042068fe0ff）
  - source_quote: "Clean in place (CIP): The removal of soil from product contact surfaces in their process position by circulating, spraying, or flowing chemical solutions and water rinses onto and over the surfaces to be cleaned." / "Clean out of place (COP): A system (e.g., cleaning tanks) used to clean equipment parts, piping, etc. after disassembly."
  - summary: 两种清洗形态的官方定义——CIP 不拆设备就地清洗；COP 拆开后清洗。选型判据不在本术语里而在环境控制逻辑里：能拆的优先 COP（可触达缝隙），不能拆的走 CIP（须验证喷淋覆盖与残留）。共用 CIP 系统另有温度与监控参数要求（见候选 A nA-07）。
  - tags: [指南自定义, 卫生, 清洗]

- **t98** / title: certificate of analysis (COA) / certificate of conformance (COC)（分析证书 / 符合性证书）/ type: term / source_chapter: XIX Glossary B（ck-c042068fe0ff）；李斯特菌专项内容要求见 VIII.B.3（ck-79ee16d62224）
  - source_quote: "Certificate of Analysis: a document, provided for a food prior to or upon receipt of the food, that documents certain characteristics and attributes of the food." / "Certificate of Conformance: a supplier's guarantee stating that raw materials and ingredients conform to a product safety specification."
  - summary: **本指南的定义比 t64 更精确**：COA 强调"**接收前或接收时**提供"（是接收环节的闸门文件），COC 强调"**供应商的保证**"（conform to a product safety specification），两者都不等于"第三方证明"。专项补充（本指南）：COC 须含保证期 + 产品安全规格 + 符合本指南与 part 117 的声明，并至少每年取得 + 每年现场审核；COA 须含抽样方案、分析结果、方法及**检出限**。
  - tags: [指南自定义, 供应链, 记录, Lmono专有, 高频误读]

- **t99** / title: high efficiency particulate air (HEPA) filter（高效颗粒空气过滤器）/ type: term / source_chapter: XIX Glossary B（ck-57471f7d75bc）；使用要求见候选 B nB-13
  - source_quote: "High efficiency particulate air (HEPA) filter: an air filter that has an efficiency of 99.97 percent to 99.99 percent when tested using the dioctylphthalate (DOP) test with a particle size of 0.3 microns. Such filters can remove all yeast, mold, bacteria and other particles that are larger than 0.3 microns."
  - summary: HEPA 的**判定性规格**——DOP 法、0.3 µm、效率 99.97–99.99%。注意这是"≥0.3 µm 粒径"的去除承诺，对更小的粒径（如气溶胶化的更细颗粒）不作保证；这是"HEPA ≠ 零穿透"的正确读法。空气过滤选型（ASHRAE 终级 vs HEPA）见候选 B nB-13。
  - tags: [指南自定义, 空气过滤, 术语澄清, 高频误读]

- **t100** / title: severity vs. adequately reduce vs. significantly minimize（三种"够不够"的判据不可混用）/ type: term / source_chapter: 综合 XIX.B（ck-c042068fe0ff、ck-57471f7d75bc）与 21 CFR 117.3（glossary t23）
  - source_quote: "Adequately reduce: capable of reducing the presence of *L. monocytogenes* to an extent sufficient to prevent illness." / "Significantly minimize: To eliminate or reduce to an acceptable level, including to eliminate."
  - summary: 三种判据的分工——**severity**（后果有多重，用于危害分析）、**significantly minimize**（法定预防控制目标：降到可接受水平，含消除）、**adequately reduce**（本指南的工艺充分性判据：足以预防发病）。混用的典型后果：把"降到可接受水平"读成"降 5 log"（一个数都不是），或把"足以预防发病"读成"可检出即合格"（忽略 0.04 CFU/g 的方法灵敏度前提）。
  - tags: [指南自定义+法定定义, 易混术语, 核心概念, Lmono专有]

**跳过项（现有 glossary 已有等价条目，仅补出处/细节，不新增 id）**：
- *harborage site / niche* → t33 已有（引 Ch3 §3.3.5.2.2）；本指南 XIX 未给新定义，X 与 XV 的用法（藏匿点导致工艺后再污染、niche 中耐受株定殖）作为 t33 的 source_chapter 补注。
- *lethality treatment* → t38 已有；本指南 XIX.B 的措辞与之一致（eliminate or reduce the number of pathogens），不重复。
- *operating limits* → t13 已有；本指南 XIX.B 措辞一致。
- *prerequisite programs* → t24 已有；措辞一致。
- *cleaning / sanitize / controlled wet cleaning* → t83 已有；CIP/COP 单列 t97（现有 glossary 未含）。
- *COA / COC* → t64 已有，本文件以 t98 替代（因本指南定义更精确且含李斯特菌专项字段要求），合并时二选一或把 t98 作为 t64 的来源补充。
- *control, control measure: See Preventive controls* → t07（preventive controls）已覆盖，映射说明即可，不单列。
- *We, us, and our / You* → 指南人称定义，无独立知识价值，不列。
- *correction / corrective action / monitor / validation / verification / food safety plan / prerequisite programs* → 现有 glossary t19/t20/t18/t21/t22/t08/t24 已覆盖，且本指南措辞与 Part 117 一致，不列。

---

## 五、合并时须守住的四条纪律

1. **两套 pH/aw 基准不得混用**（kC-01、kC-02）：4.6/0.85 是法规通用与酸化管辖口径，4.4/0.92 是本指南针对李斯特菌的抑制型配方基准。工艺控制卡更新时，Step 4 与 Step 5 必须同时出现两组数字并各自标注用途。
2. **抑制 ≠ 杀灭**（t86、t87、kC-02）：listeristatic 只承诺阻止生长（<1 log 增幅），listericidal 才承诺破坏活菌并达到 <0.04 CFU/g 的成品可检出性；两者都不能被简化成"pH 低"或"有热处理"一句话。
3. **工艺闭环之外还有环境闭环**（nC-13）：工艺只能解决进入产品之前的污染，解决不了环境再定殖；建议在工艺控制卡的边界段与 nC-31 的成品阳性处置之间建立显式互链（这是两个能力卡的接口，须双方一致）。
4. **Draft 效力层**（文件头提示）：本指南一律 "we recommend"（建议），凡含 "must" 处均为 Part 117 引述。合并进现有卡时必须沿用现有卡的 `〔§ 117.xxx〕` 标注体系，把建议层内容明确标为指南建议，避免与法定义务混为一谈。
