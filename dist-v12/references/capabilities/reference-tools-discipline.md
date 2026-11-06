# 权威参考表与数据使用纪律（reference-tools-discipline）

*来源分层：本卡融合两类权威——FDA 行业指南（草案，方法论解释）与 21 CFR Part 117 法规正文（最终规则，法定义务）。标注〔§ 117.xxx〕的内容出自法规正文；其余出自指南。*

## R — 原文

> "The data shown in Table 3-A are the extreme limits reported among the references cited. These values may not apply to your food or processing conditions." ——附录 3，Table 3-A 使用说明

> "Because the nature of bacterial growth is logarithmic, linear interpolation using the time and temperature guidance may not be appropriate. Furthermore, the food matrix affects bacterial growth..." ——附录 3，Tables 3-A/3-B/3-C 使用说明（另见预测模型节：迟滞期预测与实测可能显著偏离，模型导出的限值须验证后才可用）

中文大意：附录 3 的生长极限表是文献报道的极端值、多来自实验室培养基，未必适用于你的食品；细菌生长是对数性质，温度档之间不许线性内插；预测模型（PMP/ComBase）输出是假设不是结论。权威工具自带失真警告——"照表抄会过度，不看表会违规"。

## I — 自述

FDA 指南提供三类权威工具：附录 1 的 16 张分层危害表（X 标记）、附录 3 的生长/灭活速查数据（Table 3-A/3-B/3-C/3-D/3-E）、以及 PMP/ComBase 等预测模型。这套卡讲的不是工具内容，而是**使用纪律**——指南对自家工具的失真警告比工具本身更值得学：

1. **表是先验起点，不是答案**：X 标记只是专家（SME）建议评估的起点，附录 1 自己声明"表中不含任何需控危害判定"，判定责任在每个工厂。三层漏斗：全部危害 → potential hazard（建议评估）→ 需预防控制（评估后行动集），"查表打钩"跳过了中间层的适用性检验。
2. **三种适用性检验**：X 标记可能只适用于子类内部分产品、特定地理来源、或特定用途（干米无 B. cereus 问题、水合煮熟的米才有）——危害随"配料×下游状态轨迹"切换。
3. **数值的三条修正**：极端值≠设计值（保守起点，可用自身数据双向优化）；对数过程禁线性内插（取更严档）；基质修正（培养基数据≠真实食品）。
4. **模型的法定地位**：模型输出须经验证后才可作关键限值依据，且最易失真的量是迟滞期——模型的价值是把验证范围从全空间压缩到边界附近。
5. **数据合格性之外还有方法合格性**：同一批样品，方法选错则数据无意义。环境样与食品样各有一套官方前处理与检测方法（不能交叉套用），采用替代方法要过"书面 + 科学有效 + 准确性/精密度/检出灵敏度至少等同"三道门——这是可核验的三维判据，不是"实验室说合格就行"（见 E 段 Step 6）。
6. **有些数值已被文献确立，不必自做挑战试验**：当配方控制正好落在已被科学文献确立的数值基准上，文献本身就是充分的初始证明。

## A1 — 书中案例

**案例 1：Soup Processor A 查表定限值（第 6 章 §6.14.2）**
RTE 冷冻蔬菜汤以 L. monocytogenes 为目标菌，直接查附录 3 Table 3-D 得 180°F/3 秒即 6D——表值作为保守起点，再利用升降温途中额外致死量采用 EPIPT 只监控终点温度。查表与厂内验证衔接的标准范式：表给方向，厂内研究给结论。

**案例 2：面包的"惊喜"（第 4 章 §4.3.3.1）**
面包瓤水分活度高达 0.95（与牛奶同级的"湿食品"），却不需要冷藏——因为 pH、外壳低 a_w、霉菌优先生长三重屏障叠加，"spoils before it becomes hazardous"。若照抄"高 a_w=需控菌"的表格直觉会误判；反之酱油 a_w 0.80 看似湿食品实为中间水分食品。a_w 单一数值不能判定安全性，必须看多屏障组合。

**案例 3：Ackee（西非荔枝果）hypoglycin A（第 3 章 §3.4.1.5 / Table 12-2）**
天然毒素热稳定、随果实成熟而降低；控制点前移到原料成熟度筛选（CPG 阈值 100 ppm 判定加工不当）。附录工具无法覆盖的特殊配料须查 TDS/FCC/GRAS 补齐——表内空白≠无危害。

## A2 — 未来触发

**用户情境：**
1. 拿附录 1 危害表/行业速查表给自己的产品定危害清单，问 X 标记能不能直接抄。
2. 查到生长极限表/行业基准数值，问能不能直接当设计依据或关键限值。
3. 用 PMP/ComBase/仿真模型算出结果，问能不能直接写成 FSP 限值。
4. 新原料（植物基蛋白、特殊配料）在附录 1 查不到，问怎么办。
5. 干配料/多组分产品问"危害清单是否随用途变化"。

**语言信号**："附录 1/X 标记/危害表"、"Table 3-A/3-B/3-C/3-D"、"水分活度/pH 极限值"、"ComBase/PMP/预测模型"、"内插/插值"、"查不到怎么办"；英文：Appendix 1, X marker, growth limits, predictive model, ComBase, interpolation。

**与相邻卡的区分**：与《危害分析方法》（hazard-analysis-method）区分——六列工作表、严重性×概率评估的执行在那张卡；本卡只管评估的输入端（怎么正确使用速查表与数据，什么数值可作依据）。与《双法规与豁免边界》（regulatory-boundaries）区分——附录 1 表背后的法规适用性矩阵在那张卡。与《工艺控制与验证》（process-control-validation）区分——D/z 值换算与 6D 工艺设计在工艺控制卡；本卡讲的是这些数值的使用纪律（禁内插、极端值警示）而非换算本身。

## E — 执行要点

**Step 1 查表（生成候选集）**
- 附录 1：按产品找对应食品组表（16 组），收集 X 标记危害；含夹杂物叠加查夹杂物自身表；多组分按"部件表×组装方式"分解，缺总表不是免评估理由。
- 完成标准：候选危害清单 = X 标记 + 表外强制项（过敏原/辐射/未批准添加剂/工艺设施危害自行补齐）+ 本厂历史危害。

**Step 2 三问适用性检验（逐项过滤）**
- 一问：该 X 覆盖我这条产品吗（子类内部分产品）？
- 二问：产地条件吻合吗（地理来源依赖危害）？
- 三问：我的用途/状态会改变危害吗（干配料水合、蜂蜜仅婴儿用途、未酸化浸泡油、奶粉用于婴儿配方粉加 Cronobacter）？
- 判定规则：任一为否→只作先验起点，进入自己评估；三个"是"→列为 potential hazard 进入正式评估（评估本身走危害分析方法卡）。
- 完成标准：每项有检验记录，Yes/No 理由书面化。

**Step 3 数值使用（三条硬纪律）**
- 极端值（Table 3-A）只作筛查与方向判断，不直当设计依据；要以它定配方/工艺参数，须用自身产品实测或已确立的科学配方流程确认。
- 禁线性内插：温度/时间落在表档之间时取更严档；档间空白区（如 40–50°F 无默认限值）须自身研究设限。
- 模型输出（PMP/ComBase）：只用于初筛；凡导出的时间温度限值要进 FSP，必须先经自身产品验证研究——重点核最易失真的迟滞期。
- 完成标准：写入 FSP 的每个数值可追溯到"表值+本地验证"两段证据。

**Step 3 补充判据（李斯特菌专项：两套基准 + 文献快捷通道）**
- **同一数字的两种基准不可互换**。以下三组数值分属不同用途与不同效力层，混用会直接改变结论：
  - **pH 4.6 vs pH ≤ 4.4**：4.6 是 Part 117 酸化食品管辖边界（**法定**，平衡 pH，非初始或表观 pH）〔§ 117.3〕；4.4 是 L. mono 抑制型配方（listeristatic formulation）的**指南基准**〔L.mono 指南 IX〕。两套用途不同："做到 pH 4.5"只能勉强满足酸化食品法规一侧，抑制李斯特菌生长一侧不成立（pH 4.5 仍可生长）。
  - **a_w 0.85 vs a_w ≤ 0.92**：0.85 是安全水分水平/病原不生长一侧（**法定**）；0.92 有两义——工艺侧读作"抑制芽孢萌发"，在李斯特菌语境下读作**抑制李斯特菌营养细胞生长**，即 L. mono 抑制型配方的指南基准〔L.mono 指南 IX / XIX.B〕。引用 0.92 必须写明用的哪一义。
  - **冷藏 4°C vs 5°C**：4°C（约 40°F）是本指南对 RTE 储存的**建议缺省值**（更高温度须符合 PMO 或 Food Code）〔L.mono 指南 XI〕；5°C（41°F）是危险区下限与冷却终点（法规与 Food Code 口径）。同一份 FSP 出现两个冷藏数字须标明用途。
- **已被文献确立的数值不必自做挑战试验**：配方控制正好落在 pH ≤ 4.4 或 a_w ≤ 0.92 这一基准上时，可仅凭科学文献认定其有效：
  > "You may rely on data and information available in the scientific literature (e.g., Ref. 12, Ref. 15, Ref. 16, and Ref. 18 through Ref. 20) as an adequate demonstration that a listeristatic formulation that uses a pH less than or equal to 4.4, or water activity less than 0.92, is effective."
  > —— L.mono 指南 IX.A.1
  （小节标题写作 "pH less than or equal to 4.4 or water activity less than or equal to 0.92"，正文句为 "less than 0.92"；引用时以正文句为准。）
  与 Part 117 的证据优先级同向——证据可得且充分时不自做研究〔§ 117.160(b)(2)〕。注意这是**单参数配方**（单靠 pH 或单靠 aw）的快捷通道；组合型配方走指南 IX.A.2 的完整科学证明路径，不能套用。

**Step 4 空白与冲突处理**
- 附录 1 查不到→用供应商 TDS、Food Chemicals Codex、FDA 规格、GRAS 回复补齐；数据截至 2022 的年份意识随身携带。
- 表值与自家数据冲突→以自身验证数据为准并书面记录差异理由。

**Step 5 数据的法定资格（法规正文补足的一层）**
- 图表的法定地位已由法规正文写明：附录 1 属参考性材料，其 X 标记不构成任何"需预防控制危害"的判定结论；危害分析必须基于"经验、疾病数据、科学报告及其他信息"作出，且**无论结论如何都必须书面**〔§ 117.130(a)(1)(2)〕。数据不足时不能用"表里没有"结案——必须补充评估并留下记录。
- 严重性×概率的法定评估框架：严重性按"若危害发生时的 illness/injury 程度"，概率按"**在不存在预防控制的情况下**该危害发生的概率"〔§ 117.130(c)(1)(i)〕。这条措辞决定数据怎么用：概率评估不能拿"现有控制已在运行"来压低数字，否则判 No 的推理从起点就错了。
- 十因素评估的收口视角是"对预期消费者的成品安全性"，兜底因素（(x)）法规自带实例——某些危害具时间性/天气相关性，如部分天然毒素水平随季节变化〔§ 117.130(c)(2)〕。这给季节性数据（如 DON、贝类毒素）一个法定的落点。
- 关键限值的法定形态：工艺控制（process control）须含危害控制相关参数，及须控制的生物/化学/物理参数的**最大值、最小值或其组合**〔§ 117.135(c)(1)(i)(ii)〕。数值进 FSP 时须能对应到这一法定结构。
- validation 的证据优先级是法定的：以获取并评估科学技术证据为主，证据不可得或不充分时才自行开展研究〔§ 117.160(b)(2)〕。这决定了"先查文献再决定是否做研究"的顺序不是偏好而是义务顺序。
- 生态位提醒：法规把"预防控制"定义为"与**当前**科学认知一致"的措施〔§ 117.3〕——表格数据过期不只是引用风险，也构成控制本身不再适格的理由，可触发再分析。

**Step 6 方法的合格性判据（李斯特菌专项：数据合格 ≠ 方法合格）**
- **方法分两套，不可交叉套用**：环境样与食品样的前处理与检测各走一套官方方法——环境样按附录 5 的程序制备、按 FDA《Testing Methodology for *Listeria* species or *L. monocytogenes* in Environmental Samples》(Ref. 60) 检测；食品样按 FDA《Bacteriological Analytical Manual》(BAM) 的程序制备并检测：
  > "Use the procedures described in Appendix 5 for preparing environmental samples for analysis."
  > —— L.mono 指南 XVII

  > "Use FDA’s “Testing Methodology for *Listeria* species or *L. monocytogenes* in Environmental Samples” (Ref. 60) for testing environmental samples."
  > —— L.mono 指南 XVII

  食品样一侧用 FDA BAM 在线版（原文该句的章节标题在源文件中 OCR 缺损，引用时只取可核验的连续片段）："for preparing food samples and testing them for the presence of *L. monocytogenes* ."〔L.mono 指南 XVII〕**判据要点**：把食品样的方法搬到环境样上（或反之），结果不可用于判定——方法错配毁掉的是监测结果的全部意义。
- **替代方法须过三道门**：可自检，也可委托外部商业实验室；若采用非推荐方法，该方法必须是**书面的**、**科学有效的**，且在**准确性（accuracy）、精密度（precision）、检出灵敏度（sensitivity）**上**至少等同**于推荐方法：
  > "If you or an outside commercial testing laboratory use an analytical method other than those we recommend in this section, we recommend that the method be a written, scientifically valid method that is at least equivalent to the recommended method in accuracy, precision, and sensitivity for detecting *Listeria* spp. and *L. monocytogenes* ."
  > —— L.mono 指南 XVII
  这是可核验的三维判据，不是"实验室说合格就行"——外部实验室资质与独立性核查归供应链卡，本卡只管方法本身的三项属性。
- **成品检测与成品处置的方向不可混用**：环境监测检 *Listeria* spp.（指示物用途，判断定殖），成品检测检 *L. monocytogenes*（公共卫生风险用途）——指南建议对成品检测 *L. monocytogenes* 而非 *Listeria* spp.，因食品中 *L. monocytogenes* 的公共卫生风险不同；若检测 *Listeria* spp. 且为阳性，应判定其是否为 *L. monocytogenes*，或**按已污染处理**〔L.mono 指南 XIV.A〕。
- 完成标准：每份送检/自检委托单上写明三件事——样品类型（环境/食品）、前处理与检测方法出处、替代方法的三维等同性论证；成品检测单上写明检测对象是 *L. monocytogenes*。

## B — 边界

1. **两个方向的错都算错**：照表全抄导致过度合规（成本浪费）与不看表导致漏控（违规），FDA 把双错框架写进了使用说明——表格自我声明不含判定结论，判定责任不可外包。
2. **指南数据有保质期**：附录 1 数据截至 2022、Table 3-A 是文献极端值且多来自实验室培养基、行动水平持续迭代；引用本卡数值时必须核对现行版本。
3. **模型不是敌人也不是真理**：既不要"有模型就信模型"，也不要"模型不可靠就不用"——正确定位是假设生成器+验证范围压缩器；跳过验证环节直接用输出是本书明确的失败模式。
4. **表格不覆盖质量与欺诈**：X 表只列安全危害；过敏原/辐射/二噁英/未批准添加剂刻意不在化学表中，EMA 掺假要查模式库而非速查表——用错工具类别会得出"无危害"的假阴性。
5. **速查数据不替代专业判断**：指南假设使用者有 PCQI 级判断力；没有能力判断适用性时，正确动作是引入外部专家而不是降低表格用法。
6. **方法与数值都不可跨场景借用**（李斯特菌专项）：环境样的制备/检测方法不能挪给食品样，反之亦然（Step 6）；pH 4.6 与 4.4、a_w 0.85 与 0.92、冷藏 4°C 与 5°C 各属不同用途与不同效力层（Step 3 补充判据）。**"数值看起来对"不等于"用对了地方"**——跨场景借用会让一个正确数字支撑一个错误结论。
7. **记录保存期限不因指南而变**：本指南只列"记录什么"与"至少每年复审书面程序"的建议性要求〔L.mono 指南 XVIII〕，**保存期限仍以 Part 117 的记录规则为准**——不得用指南的年度复审节奏覆盖或替代法定期限义务（期限细节归 `management-components` 卡）。
8. **《Food Defect Levels Handbook》是第六类资料，不在效力栈内**：它是 FDA 汇编的 defect action levels 一览与术语表（执法裁量参考），页面标注 Content current as of 09/07/2018、正文 May 1995 修订版。⚠ **v4.7 纠错**：其法规引用 `21 CFR 110.110` **不是过时引用**——FDA 2018-09-12 撤回了 2015 规则拟删除 part 110 的指令，Part 110 至今有效；但 **part 110 正文本包未收**，讨论时标「转引未收」，Part 117 侧义务回〔§ 117.110〕核对，且手册那句是 §110.110(c) 的意译、不得标成〔§ 117.110(c)〕。用它只能回答「FDA 对该产品的行动水平是多少、缺陷来源与 SIGNIFICANCE 是什么」，不能回答「我是否合规」——后者回〔§ 117.110(a)〕`lowest level currently feasible`、〔§ 117.80(b)(3)(4)〕与 402(a)(4)。表内数值绑定 AOAC / MPM 方法编号与取样量，方法正文未收；引用具体数值前须核对 Federal Register Notices 是否有修订。完整判定见 `defect-action-levels` 卡与 CAP-20 B2。
9. **CPGM 7303.040 是第七类资料，也不在效力栈内**：现行版 `2025-CPM-HFP-001`（签发 08/29/2025）是 FDA 给检查员/分部的内部作业指导，规定检查类型、PAC 码、观察项与检查分级、483 回复期望与执法上报链，**不创设企业义务、不是合规判定基准**。用它只能回答「检查员会怎么看、什么会升级、当场要拿出什么记录」，不能回答「我是否合规」——后者回〔§ 117.320〕〔§ 117.315(c)〕〔§ 117.305〕〔§ 117.190(a)〕等法规正文与自身 FSP。`2020-CPGM-CFSAN-003` 已废止，其「critical observation」三级口径不得沿用。完整判定见 `inspection-readiness` 卡。
10. **本卡新增的 L.mono 判据属建议层**：〔L.mono 指南 …〕出自 FDA《Control of Listeria monocytogenes in Ready-To-Eat Foods: Guidance for Industry（Draft，2017 年 1 月）》，正文一律 "we recommend that you…"，本身不设法律责任；本卡标〔§ 117.xxx〕的才是法定义务（效力分层归 `regulatory-boundaries` 卡）。
11. **第八与第九类资料同样不在效力栈内**：CP 7303.050（2022 签发 / 2025-09-10 更正）是 FDA 给检查员/实验室的**抽样作业指导**——Table 2/3 的 subs 数、ATTACHMENT A 的 50/100 拭子是**取证量**，不是企业检验规程或放行标准，PART V 表 7/8 是逐案、非穷尽的可能响应清单；IOM 2026 Chapter 5 是 FDA 给调查员的**内部作业手册**——482/483/484 表单、15 个工作日、证据固定规则都不是企业法定义务。⚠ IOM 5.5.10.7 与 5.5.11.3 从检查员侧印证本卡的分层纪律：`Do not cite deviations from policy or guidance documents on the FDA 483`，只偏离 guidance 未违反法规的属 non-reportable observation；但同一事实若同时构成〔§ 117.xxx〕失守仍会被写成事实性观察项。完整判定见 `inspection-sampling`（CAP-17）与 `investigator-authority-procedure`（CAP-18）。
12. **CP 7303.070 是第十类资料，同样不在效力栈内**：现行件为 2024-09-26 签发 / 2025-09-26 更正（文件名 20250929 只是生成日），是 FDA 给检查员、实验室分析员与合规官的**低酸/酸化罐头专门体系作业指导**。用它只能回答「LACF/AF 走哪条 program、检查员查哪些记录、什么数值触发升级」，不能回答「我是否合规」——后者**v4.7 起回 CAP-20 的〔§ 113.xxx〕〔§ 114.xxx〕法规正文**与〔§ 117.5(d)(1)(2)〕〔§ 117.1(c)〕；**21 CFR part 108 / 110 / 120 / 123 正文仍未收**。⚠ 三类数字不可互替：4.6/0.85 是法定边界（〔§ 113.3(n)〕〔§ 114.3(b)〕），4.40/4.65/4.75、0.90/0.93、异常罐 1%、24 罐/12 罐是 CP 的实验室与取证触发线，≤4.4/≤0.92 是 L.mono 草案抑制型配方基准。`Acidified foods are subject to the CGMP & PCHF rule`——**不得把 AF 一并免掉 Subparts C/G**；也不要把〔§ 117.201〕误当 LACF 条款。完整判定见 `lacf-inspection-program`（CAP-19，检查员侧）与 `lacf-statutory-requirements`（CAP-20，法条侧）。

---
