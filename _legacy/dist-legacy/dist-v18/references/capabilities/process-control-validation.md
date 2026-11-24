# 工艺控制与热处理验证（process-control-validation）

*来源分层：① FDA PCHF 行业指南（含 Ch4 §4.3.1.1、附录 3 表值）；②《Control of Listeria monocytogenes in Ready-To-Eat Foods: Guidance for Industry》**Draft（2017-01）**，下称"L.mono 指南"；③ 21 CFR Part 117 法规正文。〔§ 117.xxx〕= 法规；"L.mono 指南 <章节号>" = 该 Draft 建议层；其余出自 PCHF 指南。*

*效力分层：L.mono 指南为 Draft，正文一律 "we recommend that you…"／"should"，属**建议层**；凡出现 "must" 均为引述 Part 117 法定义务，另以〔§ 117.xxx〕标注，不把建议层写成 must。原文 XI 章标题在转写中错位（listericidal 纠正措施段被置于 "XI" 下），本卡按内容归位到 X.B.3。*

## R — Reading（原文）

> "This approach is suitable if you have conducted a scientific study to validate that the EPIPT... will provide an appropriate reduction (e.g., 6D) in the numbers of the target pathogen in the slowest heating unit or portion of product under the worst set of heating conditions... You should use the EPIPT as a monitoring technique only under those conditions that were evaluated by the scientific study."
> —— Ch4 §4.3.1.1

自译：用"终点内部温度"替代全程时间-温度监控，前提是用科学研究验证过：在最慢加热单元、最坏加热条件下，该终点状态确实给出足够的病原削减（如 6D）。且只能在研究覆盖的条件内使用——换产品、换颗粒尺寸、换装载方式，等效性即失效。监控简化是可以买到的，但卖家是前期研究。

> "it is well established that the foods that pose the lowest risk of foodborne listeriosis have intrinsic (physical or chemical) characteristics that do not support the growth of *L. monocytogenes*"
> "Formulating your food product to have one or more such intrinsic characteristics can enhance the safety of your product."
> —— L.mono 指南 IX（Draft 2017-01，建议层）

自译：食源性李斯特菌病风险最低的食品，恰是具备"不支持 L. mono 生长"之内在特性的食品；把产品配成具有这类内在特性，本身就能提升安全。**这是本卡推理链的前置问题**：先问产品该长成什么样，再决定要不要 kill step。

## I — Interpretation（自述）

这张卡回答一个工艺研发问题：**如何为一个致死/抑制型工艺控制定出科学有效的关键限值，并证明它在我的设备上成立**。

推理链改为**先做配方/致死路径分流，再走四步**：

**前置分流（nC-02，L.mono 指南 IX）**：配方控制是风险分级第一杠杆。产品开发阶段就评估能否用 listeristatic 配方（不支持 L. mono 生长的内在特性）作为工艺控制，从而**不设 kill step**；若做不到或选 listericidal 路线，才进入下面四步。这一步决定后续走"抑制型证据链"还是"致死型验证链"；对货架期长、冷藏、无法热处理的 RTE（鲜切果蔬、熟食色拉等），前置分流是主路径。

**原四步（保留）**：**选目标菌 → 定削减倍数 → 两层验证 → 转译成可监控参数**。
1. **目标菌**由产品情境推出：最耐热 × 能在该产品环境（包装氧环境×储运温度）里生长的那个。热灌装 ROP+冷藏 → 非蛋白分解 C. botulinum；酸化 pH≤4.1 → 只需控营养细胞。
2. **削减倍数**查保守默认表（5D–7D；孢子 6D），再用 D/z 值做温度换算、用自身初始菌落数双向优化；L.mono 场景下另叠加"成品不可检出 + 方法灵敏度"与"初始负荷决定 log 数"两层（见 Step 2）。
3. **验证分两层**：发表研究证明"原理上可行"（别人基质上的结论），厂内热分布（找冷点）+热穿透（最坏工况满载）证明"我的设备做得到"——取交集才是可承诺的限值。**注意**：该框架**为热处理/致死型设计**，抑制型无"设备层"、改用"证据类型清单"（见 Step 3）。
4. **代理参数转译**：连续工艺里"时间"不可直测，就转译成有确定函数关系的可测量（带速 RPM、泵速、持留管尺寸、颗粒尺寸），并把代理成立的前提（原料温度史、装载方式）用 SOP 固化；抑制型配方还有**方向相反**的"从可测量→可测量替代"（不测成品 pH、改测配料比例，见 Step 4 / nC-07）。

贯穿的硬边界：热处理只杀营养细胞、不灭孢子、不消除已形成的毒素——控制设计必须覆盖 kill step 之后的冷却窗口与屏障接力；且**工艺闭环之外还有环境闭环**（见 A2 / B）。

## A1 — Past Application（书中案例）

**案例 1：Soup A 的 EPIPT 落地**
冷冻蔬菜汤以 L. mono 为目标菌，查附录 3 Table 3-D 得 180°F/3 秒即 6D；利用升降温途中额外致死量，采用 EPIPT——只监控终点 180°F，免除全程记录。第二条关键限值：颗粒≤½ 英寸（厂内研究证明颗粒与液体同步达温），前提是来料冷藏 33–40°F——前提本身进 SOP。监控测锅内最冷的上层 1 英寸，每 10 分钟一次。

**案例 2：Soup B 的目标菌推理**
连续换热器+5 加仑袋热灌装（ROP）+冷藏分销的组合推出目标菌=耐冷的非蛋白分解 C. bot B 型，据此选 205°F/2.5 min（等效 90°C/10min）6D 工艺，185°F 热灌装防再污染；五条关键限值（初温/泵速/持留管/出口温/暂存罐温）覆盖连续系统每个关键因素，并预写可/不可再加工清单。

**案例 3：Salsa A 的"双限值"分工**
pH 4.1 控肉毒萌发（文献 sporeformers 在 pH≤4.2 不生长），热处理 158°F/1.5 min 只对营养细胞病原达 5D；另加 200°F/2 min 杀腐败芽孢菌、防其代谢产碱把 pH 抬回 4.6 以上反扑——安全限与货架期限并存，且颗粒≤1.0 cm 保证同步达温。

**反例对照**：温度滥用的蛋奶派"再烤一下"救不回已形成的 S. aureus 毒素；大桶汤自然放凉过夜给孢子萌发敞开时窗；水浴冷却的真空会把污染冷却水经缺陷封口吸入；Table 3-B/C 区间之间禁线性内插（对数生长）。

## A2 — Future Trigger（何时用 / 与相邻能力的区分）

**触发场景**：
- 用户设计/修改热处理、巴杀、酸化、干燥、ROP 配方等工艺，问"温度/时间/pH/a_w 定多少才算安全"
- 问"文献参数能直接抄吗"、"新设备/新配方要不要重做验证"、validation 怎么做
- 问"颗粒尺寸/泵速/冷藏温度这些参数怎么变成关键限值"、连续工艺怎么监控
- 涉及 D 值/z 值/6D、附录 3 表格换算、EPIPT 简化监控
- 问"listeristatic / listericidal 怎么选"、"抑制型配方要不要自做挑战试验"、"成品该检什么菌"、"储存温度定几度"

**与相邻卡的区分与接口**：
- **危害分析方法**：那边产出"该危害走工艺控制"这个判定；本卡从选目标菌开始做工艺设计。危害分析只到第 6 列选位为止。
- **适用边界（nC-01，仅指针）**：L.mono 指南适用于"RTE 食品在**包装前**暴露于环境、且**包装后**没有致死处理或致死型配方控制"的场景；明确不适用于①在最终包装内、或紧邻包装前施加致死措施且系统能充分屏蔽产品与包装食品接触面不受环境污染的加工者，②不受 Part 117 约束的场所（如农场）。属**指南层适用分流**，正文见 `hazard-analysis-method` / `regulatory-boundaries` 卡（§ 117.130(c)(1)(ii) 触发器）。
- **预防控制管理组件闭环**：监控四问、偏差处置、记录审查归那边；本卡偏差处置阶梯只在"限值怎么来的"语境下引用。时点分叉细则、cleanup to cleanup 牵连口径、培训矩阵、记录期限均在那边（见 B 段 kC-06/08/09）。
- **环境病原与卫生控制（显式互链，nC-13）**：本卡只管工艺参数；施加 listericidal 后李斯特菌仍可经 harborage sites 造成**工艺后再污染**——这是"工艺闭环之外还有环境闭环"的交接凭据。指南要求参照**附录 1（潜在污染源清单）**与**附录 2（污染场景清单）**；环境战略、监测方法、CIP 参数主体转 `environmental-pathogen-sanitation` 卡。
- **检测方向成对（kC-05，极易混用）**：**成品检测应检 L. monocytogenes**——"We recommend that you test food products for *L. monocytogenes* rather than for *Listeria* spp."〔L.mono 指南 XIV.A〕（因前者公共健康风险；若改检 Listeria spp. 阳性须判定是否 L. mono，否则按 L. mono 污染处理）；**环境监测则应检 Listeria spp.**（指示物 + 定殖判断）。同一病原、两种方向、理由相反，须成对记住，不得把环境监测做法照搬到成品检测；频次/抽样细则见 `management-components` / `environmental-pathogen-sanitation` 卡。
- 与**化学危害归途判定**：天然毒素（如 hypoglycin A）与已形成毒素热稳定，热处理无效时控制点前移到原料选择——遇到"热稳定毒物"先想前置控制而非加温。
- **供应链验证**：检测能否作唯一控制手段（kC-07）正文在 `supply-chain-verification` 卡。

## E — Execution（可执行步骤）

**Step 1 选目标菌**（完成标准：写出"包装氧环境×储运温度×最耐热"三因素论证）
- **前置决策（nC-02，L.mono 指南 IX，建议层）**：先做配方/致死路径分流——产品开发阶段评估是否用 listeristatic 配方作工艺控制；若走抑制型，Step 2/3/4 切换为"抑制型证据链"（<1 log 判据、五类证据路径、pH/aw 或配料比例监控），不选目标菌、不做 kill step 设计；若走致死型才进入下面推理。
- 候选=能在该产品最终环境（ROP/常压、冷藏/常温、货架期长短）中生长的病原里最耐热者。
- 排除规则：漂烫去皮不算杀灭步骤；pH 文献值≤4.1–4.2 可把范围收窄到营养细胞；冷藏长货架期 RTE 必查非蛋白分解 C. bot（Table 3-B 累计暴露时限）。
- 致死型候选技术清单见 Step 3 / nC-14（含辐照的 21 CFR part 179 前置、静水压处理），须咨询微生物学家或 process authority。

**Step 2 定削减倍数**（完成标准：写出目标 log 数与温度-时间组合）
- **通用默认值（保留）**：营养细胞病原 5D–7D；孢子目标 6D（锚点：L. mono 70°C/2.0 min；非蛋白分解 C. bot 90°C/10 min）。换算：用 z 值把 lethal rate 折算到目标温度（只许在参数有效域内外推，跨基质重验）。双向优化：自身初始菌量常年 <100 CFU/g 可降杀灭度；初始负荷高须收紧——表值是保守下限起点，个性须付费（本地数据）。
- **⚠️ 两套 log 基准并列、不矛盾（kC-03）**：上面 5D–7D/6D 是**按病原类型的通用默认**；下面是**无科学研究时**的 **L.mono 专项兜底**，按**工艺前初始负荷**切换（L.mono 指南 X.A，建议层）：
  - 工艺前初始负荷 ≤100 CFU/g（食品不太可能被污染到超过 100 CFU/g）→ **5 log（99.999%）**："five orders of magnitude (five logarithms or 99.999%) could achieve that goal, particularly if the food is unlikely to be contaminated with more than 100 CFU/g"〔L.mono 指南 X.A〕
  - 可合理预见配料可能被污染到 >100 CFU/g → **6 log（99.9999%）**："six orders of magnitude (six logarithms or 99.9999%) could be necessary to achieve that goal."〔L.mono 指南 X.A〕
  - 其他 log 数若经适当验证、能把风险降到足以预防发病，亦可。
  - **显式结论：初始负荷是决定 log 数的第二个自变量**（第一个是病原类型）。危险误读（kC-03）：看到"5 log 就够"却忘了 100 CFU/g 前提；或看到"6D 锚点"就以为 L. mono 必须 6D 而过度设计——两处须同时出现。
- **新增维度：验证目标写成"成品可检出下限"而非只写 log 数（nC-11，L.mono 指南 X.A）**：listericidal 验证目标须是"工艺一致地摧毁活菌并使成品**不含可检出 L. mono**"，且所用方法检出灵敏度须**至少 0.04 CFU/g（即 <1 CFU/25 g）**："consistently leads to a food product that does not contain detectable *L. monocytogenes* using a method that has a sensitivity of detection of at least 0.04 CFU of *L. monocytogenes* per gram of food (<1 CFU/25 g)"〔L.mono 指南 X.A〕。**方法灵敏度是既有判据缺失的维度**：同一 5 log 工艺，用 10 CFU/g 与 0.04 CFU/g 灵敏度验证，结论强度不同。

**Step 3 两层验证**（完成标准：致死型走"文献层+设备层"；抑制型走"证据类型清单"；证据齐备）
- **致死型/热处理（原有两层，保留）**：
  - 文献层：发表研究/推广专家/行业验证库（如加州杏仁 4-log 营销令）定位科学需求——别人基质上的结论只是起点假设。
  - 设备层：厂内热分布（找冷点，满载最坏工况）+热穿透（最慢加热单元/最大颗粒中心），跨 3 天多次试验更稳。
  - 配方/设备/初始温度变更 → 触发重评（新烤箱不能沿用旧关键限）。
- **⚠️ 抑制型（listeristatic）配方没有"设备层"——对应物是"证据类型清单"（nC-04 / nC-05 / nC-06，L.mono 指南 IX.A）**：两层框架为热处理设计；抑制型不测热分布/热穿透，而从下列五类可组合证据路径证明"配方持续抑制生长"，并区分**单参数配方**（只靠 pH 或只靠 aw）与**组合参数配方**（抗菌成分 + pH 等）的证据结构：
  1. "Historically established formulation controls (e.g., pH less than or equal to 4.4 or water activity less than or equal to 0.92)"〔L.mono 指南 IX.A〕（历史确立的配方控制）；
  2. 引用已发表同行评议研究（证明某抗菌成分在自家品类如熟食色拉有效）；
  3. 既往验证研究（公开或本厂内部，如某配方研究至少部分适用于第二配方）；
  4. 数学建模（生长抑制模型辅助设计挑战试验）；
  5. 科学有效的实验数据/自做挑战试验。
  - **hurdles 概念（nB-01，仅保留概念、不重复数值）**：抑制可由"内在特性 × 加工温度 × 配方"的多因子交互（hurdles）实现，不必依赖单一阈值；三类数值阈值以 L.mono 指南 IX 为准（见 Step 4 两套基准框）。nB-02 的 <1 log 表述被 nC-06 的 IX 章正式表述取代，此处不另写数值。
  - **快捷通道（nC-05，L.mono 指南 IX.A.1）**：pH ≤ 4.4 / aw ≤ 0.92 已被文献确立，**仅凭科学文献即可构成充分初始证明，不必自做挑战试验**："…as an adequate demonstration that a listeristatic formulation that uses a pH less than or equal to 4.4, or water activity less than 0.92, is effective"〔L.mono 指南 IX.A.1〕。与 § 117.160(b)(2) 证据优先级一致；组合型配方须走完整科学证明路径。
  - **抑制型有效性判据（nC-06，L.mono 指南 IX.A.2）**："…show an increase of less than 1 log cycle over two or more time intervals in the number of *L. monocytogenes* during replicate trials with the food of interest"〔L.mono 指南 IX.A.2〕——即**货架期多个时间点取样的生长研究、两个以上时间间隔、重复试验、增幅 < 1 log** 视为有效。研究由懂食品微生物与病原控制的微生物学家或 process authority 实施；结果须给出可监控参数及 min/max；操作参数**带安全裕度**——"We recommend that you use values for operating parameters that incorporate a margin of safety"〔L.mono 指南 IX.A.2〕。这是对照致死型 5D–7D 的**抑制型接受准则**。
- **致死型（listericidal）两块补充**：
  - **候选技术清单（nC-14，L.mono 指南 X.A）**：咨询微生物学家或 process authority；单独或组合考虑热处理、"irradiation (provided that irradiation has been approved as a direct food additive and listed in 21 CFR part 179), hydrostatic pressure processing, or product formulations that are listericidal"〔L.mono 指南 X.A〕——**辐照须先过 21 CFR part 179 批准**、静水压属非热致死技术；验证研究须给出可监控参数及 min/max 值。
  - **五类验证活动（nC-16，L.mono 指南 X.B.2）**：①校准过程监控与验证设备；②**生产中**检查记录曲线、料层深度（bed depths）、泵速/输送带速度、颗粒尺寸（热穿透）等是否正常运作（把 EPIPT/代理转译从纸面拉回现场）；③建立 SOP 指定专人定期旁观抗菌成分按规定量加入；④若设 pH/aw 类控制参数，核查所有配料按正确比例加入；⑤审查测量记录是否准确且满足参数 min/max。
- **法定时序与证据优先级（保留）**：validation 须在 FSP 实施前完成，或在首批适用食品投产后 90 个日历日内完成；超过 90 日的须由 PCQI 准备书面论证（写明更长时间的理由）〔§ 117.160(b)(1)〕。证据取得顺序也是法定的——validation 以获取并评估科学技术证据为主，证据不可得或不充分时才自行开展研究〔§ 117.160(b)(2)〕：自做研究是缺位时的补充，不是首选路径。

**Step 4 关键限值+代理转译**（完成标准：每个 CL 可测可记录，代理前提 SOP 化）
- 批式：炉温/时间/单件质量；连续：带速 RPM、泵速、持留管编号与配方一一对应。
- **关键限值的法定定义**：工艺控制（process control）须包含与危害控制相关的参数，以及须控制的生物、化学或物理参数的**最大值、最小值或其组合**〔§ 117.135(c)(1)(i)(ii)〕——这就是"关键限值"在法规里的正式形态，双限值（关键限+操作限）设计时须能对应到 max/min 的法定结构。
- **屏障类参数的法定基准与持续义务（保留）**：酸/酸化食品的法定定义以**平衡 pH 4.6 或以下**为准（equilibrium pH，非初始或表观 pH）〔§ 117.3〕；依赖 pH 调控的食品须被**监测并维持**在 pH 4.6 或以下，依赖水分活度的须加工至并维持于**安全水分水平**（须有充分数据证明该 aw 下不良微生物不增殖）〔§ 117.80(c)(14)(15)〕。这给"酸化完测 4.5、货架期 pH 回升怎么办"确定答案：屏障是持续监测义务且以平衡值为准，不是出锅时的一次性测量。
- **抑制型配方三条官方路径（nC-03，L.mono 指南 IX，建议层）**：① pH ≤ 4.4；② aw ≤ 0.92；③含一种或多种抑菌物质（单独或组合即可，含发酵/培养形成的配方）。采用任何 listeristatic 配方**既要 initial demonstration 也要 ongoing verification**——"we also recommend that you demonstrate that any listeristatic formulation you use is effective and verify your formulation control on an ongoing basis"〔L.mono 指南 IX〕。
- **抑制型监控两条路（nC-07，L.mono 指南 IX.B.1）**：控制只依赖 pH 或 aw 时——①**直接测**每批 pH/aw，或 ②**间接证**"所有配料按正确比例加入"以达到目标 pH/aw。组合型配方监控抗菌成分加入量、pH、构成 hurdles 的其他参数及配料比例。**⚠️ 方向相反**：现有代理转译是"不可测量→可测量"（时间→带速），此处是"可测量→可测量替代"（改测配料比例），同为合法简化。
- **抑制型持续验证四类措施（nC-08，L.mono 指南 IX.B.2）**：①校准 pH/aw 测量设备，**或**由非当批操作人员定期旁观 pH/aw 测定过程核查测法正确（低成本手法）；②由非当批操作人员偶尔旁观抗菌成分按规定量加入；③若控制依赖配料比例，定期抽测一批成品 pH/aw；④审查测量记录，确认准确且落在参数 min/max 之内。
- **致死型监控参数清单（nC-15，L.mono 指南 X.B.1）**：监控时间、温度、aw、pH、致死成分浓度，频次须足以确保控制达成；**可行时建议连续监控并记录**——"When practical, we recommend continuous monitoring and recording of such parameters."〔L.mono 指南 X.B.1〕
- **不可测量→代理（保留）**：颗粒尺寸≤½英寸/≤1.0cm、冷藏不冻结、糖盐配比，代理成立的前提写进 SOP 成为关键因素。EPIPT 简化：热分布+热穿透+其他关键因素三前提齐备、且升降温冗余致死量经量化后 ≥ 全部需求时才可用；只测终点温度，每批必测。
- **CIP 参数监控（nA-07，仅指针）**：共用 CIP 系统碱性清洗液须 ≥71°C（160°F）〔L.mono 指南 VII.A.3，建议层〕；CIP/COP 浓度、流速、周期时长、温度监控主体在 `environmental-pathogen-sanitation` 卡。

> **【两套基准框 · 覆盖 Step 4 与 Step 5 · 不得互相替换】（kC-01 / kC-02，本卡最关键增量）**
> - **pH 4.6 / a_w 0.85** —— Part 117 酸化食品管辖边界与安全水分水平（**法定/通用口径**）：平衡 pH 4.6 或以下〔§ 117.3〕、pH 4.6 或以下维持〔§ 117.80(c)(14)〕、a_w 须加工至并维持于安全水分水平〔§ 117.80(c)(15)〕。用途：判定酸化/LACF 管辖、设定通用安全水分。
> - **pH ≤ 4.4 / a_w ≤ 0.92** —— L. mono 抑制型（listeristatic）配方设计基准（**L.mono 指南建议层**）〔L.mono 指南 IX〕。用途：判定配方能否阻止 L. mono 生长。
> - **第三套数字（CP 7303.070 PART IV.2，检查员作业口径）**：pH **4.40 / 4.65** 是实验室第二分析师复测与扩测触发线、**4.75** 是异常罐肉毒毒素/PCR 触发线、aw **0.90 / 0.93** 是 aw 筛查复测触发线，`Never average the two analysts' results together`。它们既不是法定边界，也不是配方设计基准，**不得与前两套互相替换**；详见 CAP-19 `lacf-inspection-program`。
> - **二者用途不同、不得互相替换或合并**。典型误读："我做到 pH 4.5"同时以为满足酸化法规要求**和**满足 L. mono 抑制目标——前者勉强成立（4.5 ≤ 4.6），后者**不成立**（L. mono 在 pH 4.5 仍可生长）。
> - **同一个数字 0.92 在两处含义不同**：现有卡把它绑定到"抑制芽孢萌发"（肉毒视角，见 Step 5 配方屏障数值），L.mono 指南把它绑定到"抑制李斯特菌营养细胞生长"（李斯特视角）。**两个 0.85/0.92 不得互相替换**。

**Step 5 工艺危害陷阱核查**（完成标准：逐项过清单）
- 已形成毒素（S. aureus/B. cereus 催吐毒素）热稳定——产毒前时序控制是独立于 kill step 的必要控制。
- 冷却协议：135→70°F≤2h、70→41°F≤4h，两段式+防再污染三通道（手接触/冷凝水/交叉接触）；冷却后封口完整性与冷却水卫生（真空吸入陷阱）。
- **配方屏障数值（保留 + 补注）**：a_w≤0.85 控营养细胞 / ≤0.92 抑孢子萌发〔**补注：该 0.92 同时是 L.mono 抑制型配方基准（李斯特视角），见【两套基准】框；两个 0.85/0.92 不得互相替换**〕；pH<4.6 控肉毒并兼 LACF/酸化管辖分界；ROP 须五屏障居其一（a_w<0.93 / pH<4.6 / 盐>10% / 终容器热处理 / 冷冻储运），冷藏不得为唯一屏障。
- **⚠️ 抑制 ≠ 杀灭（保留并展开）**：加酸不能杀营养细胞。listeristatic 只承诺**阻止生长**（判据：货架期增幅 < 1 log，见 Step 3 / nC-06）；listericidal 才承诺**破坏活菌并使成品达到 <0.04 CFU/g 的不可检出性**（见 Step 2 / nC-11）。两者都不能简化成"pH 低"或"有热处理"一句话。
- **工艺后再污染 / 环境闭环（nC-13，L.mono 指南 X，建议层）**："*L. monocytogenes* has been shown to persist in equipment and the processing environment in harborage sites, and can lead to recontamination of your RTE food after you apply a listericidal process control"〔L.mono 指南 X〕——李斯特菌在设备与加工环境的 harborage sites 中持续存在，**施加 listericidal 工艺控制之后仍可造成 RTE 食品再污染**；指南要求参照**附录 1（潜在污染源清单）**与**附录 2（污染场景清单）**防止工艺后再污染（"工艺闭环之外还有环境闭环"接口，见 A2 / B）。
- **储存控制（nC-26 / nC-27，L.mono 指南 XI，建议层）**：
  - 李斯特菌**在冷藏温度仍能缓慢繁殖**，但冷藏仍是关键控制；建立程序缩短原料、在制品、成品处于允许生长条件的时间，执行 **FIFO** 或**最短 "use by" 日期优先**程序，并**持续验证时间/温度控制**。
  - 储存缺省值 **4°C（约 40°F）或以下**："…we recommend that RTE foods be stored at 4°C (~40°F) or below; higher temperatures may be appropriate when consistent with the Pasteurized Milk Ordinance (Ref. 54) or Food Code (Ref. 55)"〔L.mono 指南 XI〕。
  - **冷冻**：李斯特菌在冰点以下不生长，故冷冻是有效的**防生长**措施；但"Freezing will not eliminate *L. monocytogenes* from foods and cannot be relied upon as a control measure for the elimination or reduction of *Listeria monocytogenes*"〔L.mono 指南 XI〕——冷冻**不会消除**李斯特菌、**不能**作为消除或减少的控制措施。
  - **⚠️ 冷藏温度两套基准（kC-04）**：**4°C / 40°F** 是 L.mono 指南针对李斯特菌储存的**建议缺省值**（更严、**非法定门槛**）；**41°F / 5°C** 是危险区下限与冷却终点（法规/Food Code 口径，本卡冷却协议用值）。二者用途不同、不冲突，同一份 FSP 须标明用途。
- **多组分界面（保留）**：单组分 pH/a_w 合格≠成品合格，测成品界面均衡值（泡芙/鹰嘴豆泥顶料陷阱）；任何后添加配料按配方变更重评。
- **附录 3 纪律（保留）**：Table 3-A 极端值当筛查起点不当设计依据；区间间禁线性内插（取更严档）；PMP/ComBase 模型输出是假设，作关键限值前必须实测验证。

**Step 6 偏差处置**（完成标准：预写处置预案）
- 沿阶梯（保留）：补足处理 → 再加工（可/不可再加工清单预授权）→ 暂存待评估 → 降级改用途 → 转饲料 → 销毁；安全判定归 PCQI。
- **等效致死量补偿（nC-17，L.mono 指南 X.B.3，建议层；原文该段标题错位入 XI）**：生产中发现工艺参数未达标可在过程中纠正——例如温度低于工艺控制温度时，"you may be able to increase the time to achieve an equivalent lethality"〔L.mono 指南 X.B.3〕；受 subpart C 约束者建议 PCQI 参与该纠正。包装后才发现参数未达标：评估安全性、未判定安全不得入市（PCQI 判定）、查明原因防复发；若已入市且评估提示安全顾虑，"you should recall the product"〔L.mono 指南 X.B.3〕——**应召回**。
- **抑制型配方偏差的时点分叉（nC-09，仅写工艺视角指针）**：生产中发现 pH/aw/抗菌成分量不对可就地调整；包装后才发现须评估安全性、未经 PCQI 判定安全不得进入流通——本卡只记这一句**时点分叉**指针，执行细则在 `management-components` 卡。

## B — Boundary（边界）

1. **致死度有技术上限**：不可能降到零；常压热处理不灭孢子、不消除已形成的毒素——指望 kill step 一步到位的设计从根上错（x04/x18）。对热稳定毒物（天然毒素、真菌毒素、毒元素），本卡的加温思路整体不适用，控制前移到原料与供应商。
2. **权威表只是先验**：附录 3 数值来自文献极端值与实验室培养基，FDA 自认"未必适用于你的食品"；预测模型输出、行业基准同理——照抄会失守，不用表也会违规，本地验证不可省（x35/x36）。
3. **监控简化有审计链**：EPIPT、代理参数、查表定限全部以一次性研究的完备性为代价换日常简率；研究没覆盖的条件（换颗粒/冻结来料/换装载）下继续用就是"监控通过但产品未达致死率"（x33）。
4. **章节缺位（改写保留）**：Ch7（时间/温度控制）、Ch8（配方/干燥）、Ch9（过程验证专章）**仍未发布**——但 **L.mono 专项指南的 IX / X / XI 章已补齐抑制型与致死型配方的验证方法学主体**（五类证据路径、<1 log 判据、致死型验证活动、储存时间/温度控制）；附录 4/5/6 的表格模板**仍待补**。细节仍须依赖其他权威资源（process authority、行业验证库）。
5. **跨法域须换算**：D/z、6D、a_w/pH 数值是微生物学通用语言可迁移；但 5D/6D 档位、酸化食品管辖分界（pH 4.6 ↔ part 114）绑定美国法规，其他法域读者须对应本国标准。
6. **工艺优化诱发新危害**：致死步骤清场后幸存孢子获得竞争真空（冷却窗口风险）；"杀灭即安全"的直觉在这类工序交接处正好相反。

**效力分层与跨卡指针（kC-05~kC-09 的落位；均为"指南建议层 / 指针"，不得改写为法定义务）**：
- **kC-05 成品检 L. mono vs 环境检 Listeria spp.**：同一病原、两种方向、理由相反，须成对呈现（已在 A2 写明）；细则见 `environmental-pathogen-sanitation` / `management-components` 卡。
- **kC-06 cleanup to cleanup 扩展**：本指南把它从过敏原场景**扩展**到成品 L. mono 阳性——"You should consider lots produced between two cleaning and sanitizing cycles to be implicated by the product positive"〔L.mono 指南 XIV.B〕；**只写指针**，正文在 `management-components` 卡。
- **kC-07 检测能否作唯一控制手段**：本指南优先供应链控制而非逐批检测，以检测为唯一手段须加频次规则与隔离暂扣流程；**未发现实质矛盾**，正文在 `supply-chain-verification` 卡。
- **kC-08 培训义务层级**：§ 117.4 通用卫生培训 vs L.mono 指南 XVI 李斯特菌专项培训（含承包商、上岗前+至少每年复训、四类职责人须"成功完成"）——属 Draft 建议层叠加，**非法规要求**，引用须标"指南建议"；培训矩阵正文在 `management-components` 卡。
- **kC-09 记录保存期限**：L.mono 指南 XVIII 只列"记录什么"与"至少每年复审书面程序"，**未给期限**；期限仍以 Part 117 为准（一般 2 年、设备/工艺记录停用后 2 年、FSP 须驻场，见 `management-components` B3）——**不得用本指南"年度复审"覆盖或替代 Part 117 的保存期限义务**。

**边界互链（nC-13）**：工艺闭环之外还有环境闭环——listericidal 工艺 100% 有效也不能豁免工艺后再污染（harborage sites → 附录 1/2 → `environmental-pathogen-sanitation` 卡）；本卡只管工艺参数本身，不管车间卫生战略。
