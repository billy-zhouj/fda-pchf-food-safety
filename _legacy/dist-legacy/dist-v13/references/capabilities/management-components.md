# 预防控制管理组件闭环（management-components）

*来源分层：21 CFR Part 117 法规正文（最终规则，法定义务，标〔§ 117.xxx〕）；本书所据 FDA 行业指南 Ch5（草案，标 Ch/小节号）；FDA《Control of Listeria monocytogenes in Ready-To-Eat Foods》指南 (Draft, 2017年1月)（标〔L.mono 章.节〕，正文一律为建议表述，属建议层；句中 must 是引述 Part 117 的法定义务）。冲突以法规为准。*

## R — Reading（原文）

> "If a measurement shows that a deviation from the control value has occurred, you should assume that the control value had not been met since the last check in which the value was acceptable. As a result, the greater the time span between measurements, the more products you are putting at risk."
> —— Ch5 §5.5.2

自译：一旦测得偏离控制值，就应当假定自上次合格检查以来控制一直未被满足——检查间隔越长，被置于风险中的产品越多。监控频次不是合规参数，而是风险敞口的旋钮；发现偏差时，受影响范围默认回溯到上次合格点，而不是"发现多少处理多少"。

## I — Interpretation（自述）

危害分析判定"Yes"之后，每个预防控制都要挂一套管理组件才能运行：**监控 → 纠正/纠正措施 → 验证 → 记录 → 再分析**。这张卡管的是这套闭环怎么设计、怎么闭环、什么时候升级。

核心骨架五条：
1. **双线设计**：关键限值是食品安全红线（偏离触发纠正措施），操作限是更严的内控线（偏离只做 adjustment）——用缓冲带吸收日常波动，保住安全程序的严肃性。
2. **分诊而非分级**：correction 的法定入口是两条并列通道〔§ 117.150(c)〕——过敏原交叉接触/卫生控制不一致的"条件与实践"及时纠正即可（**无"孤立"限定**），或轻微且孤立、不直接影响产品安全的问题；其余一律走完整 corrective action。同一错误因发现时机（投产前/投产后）不同走完全不同路径。
3. **两类证据不可互替**：validation（科学证明方法有效，实施前/法定窗口内做）与 verification（证明执行有效，日常核查）是五层验证体系里不同的层；实验室报告不能代替校准记录。
4. **动态维护三件套**：周期全量复审兜底（≥3 年）+ 事件触发增量复审（变更/新信息/意外/失效/FDA 指令/科学进展）+ 反复偏差=程序无效=强制再分析。
5. **两条正交轴 + 一处口径扩用**：回溯推定已扩到成品 L. mono 阳性场景（**同一条 cleanup to cleanup 口径**，非新增平行规则）；**时点轴**（偏差落在包装前还是包装后）与**检测方向轴**（环境监测检 Listeria spp. vs 成品抽检检 L. monocytogenes）。

## A1 — Past Application（书中案例）

**案例 1：Cookie A 的双线监控与记录体系**
在关键限（350°F/13min/28g）之上另设操作限（352°F/15min/27g）并按操作限生产——偏离操作限只做调整，不触发产品处置。监控四问落位：连续温度记录每批人工目视核查、每 2 小时查挤料设定、每班 2 次称重、仪表至少每年校准。结果：波动在缓冲带被吸收。

**案例 2：Bakery B 的分诊判定**
花生品误入非花生区：若生产尚未开始，只需 correction（纠正后可不记录）；若面团已投产，则触发完整 corrective action——评估面团、改做花生酱饼干或转动物饲料。"生产是否已开始"这个时间代理把同一错误切成两条路径；Soup B 还预写了"可/不可再加工清单"，紧急时刻查表执行、专家判断只留"清单未覆盖的安全问题"一权。

**案例 3：供应商召回传导买方义务**
供应商召回含意外大豆的奶粉：未使用的库存按供应商指令处理（correction 层）；但召回前已用该粉生产的产品必须走完整四步 corrective action——查根因、防复发（换供应商或整改）、评估全部受影响食品、确保不入市（已出货则召回）。偏差三角色分工贯穿 5 个示例厂：PCQI 判安全、经理查根因、操作工再培训。

**反例对照**：把反复性问题当 correction 轻处理会积累系统性失效；清洁后检出过敏原阳性只隔离"检出之后"批次是少算——受影响批次=cleanup to cleanup；校准拉长到一年以上会使失准时的风险敞口按比例放大。

## A2 — Future Trigger（何时用 / 与相邻能力的区分）

**触发场景**：
- 用户问"这个控制怎么监控、多久记一次、谁来负责"（monitoring、corrective action、verification、validation）
- 用户发生了偏差："温度超标了/清洁失败/标签贴错了，怎么处理、要隔离多少产品"
- 用户在设计记录表单或想减负："能不能少记点"、exception record 怎么用
- 用户问"什么情况下要重做危害分析/改 FSP"、反复出问题怎么办
- 用户问记录合规："记录有什么法定要件、保存多久、FDA 调记录怎么应对、电子系统受不受 Part 11 管"
- 用户问 PCQI 边界："哪些事必须 PCQI 亲自做、放宽时限的论证 QA 能不能签、能不能请外部 PCQI"

**与相邻卡的区分**：
- **危害分析方法**：那边回答"有哪些危害、要不要控制"；本卡假设控制已选定，回答"控制怎么运行、失守了怎么办"。判定 Yes/No 回危害分析卡，处置已发生的偏差归本卡。
- **工艺控制与热处理验证**：热处理类控制的具体关键限值怎么算、validation 研究怎么做（热分布/热穿透）是那边的领域；本卡管的是任何控制通用的管理框架，不产出限值数值。
- **环境病原与卫生控制 / 食品过敏原程序**：这两类控制的**特有**监控工具（环境监测、过敏原特异性检测）在各自卡内；本卡只讲它们共享的闭环结构，且明确它们的 validation 豁免与裁剪规则。
- 与**召回计划**（化学危害卡）：corrective action 的"阻止入市"升级为主动召回执行时，转向召回响应能力。

## E — Execution（可执行步骤）

**Step 1 监控设计——四问框架**（完成标准：每个控制有 What/How/How often/Who 四答）
- What/How：测什么参数、用什么手段（连续仪表 vs 人工观察 vs 检测）。**监控对象可二选一**（建议层）：抑制型（listeristatic）配方若依赖 pH 或水活度单一参数，"you should either monitor pH or water activity of each batch or monitor that all ingredients in the formulation have been added in the appropriate proportions"〔L.mono IX.B.1〕；组合型配方"you should monitor applicable process control parameters"（抗菌成分加入量、hurdles 中其他参数、配料加入比例）〔L.mono IX.B.1〕。走"配料比例"路线须比例正确性被独立核查（见 Step 4）。
- 书面程序要写明的字段（缺项即程序不完整）：
  - 卫生程序八项：设备或区域、是否拆装、清洁频次、清洁剂与消毒剂的类型及浓度、清洁工具类型、工具颜色编码（如原料区红、RTE 区蓝）、清洗液的时间/温度、清洗液的流速或压力〔L.mono VII.A.1〕。
  - 环境监测程序七项：科学有效、检测目标是 Listeria spp. 还是 L. monocytogenes、采样位置与例行监测的点数（"sampling sites should be adequate to determine whether Listeria control measures are effective"）、采样时机与频次（同样须足以判定控制有效）、检测项目与分析方法、检测实验室、检出时的纠正措施程序〔L.mono XIII.D〕。点位/时机/频次须"足以判定有效性"在法规层是 must〔§ 117.165(b)(3)〕，其余为建议层。
  - 纠正措施程序须写明**步骤与责任人**（"include corrective action procedures that describe the steps to be taken and assign responsibility for taking those steps"）〔L.mono XIII.D.7〕，并**基于风险**定维度：监测策略、FCS 还是 non-FCS、孤立阳性还是多点阳性、被污染 non-FCS 与 FCS 的邻近度；措施类型库（强化清洁消毒、强化采样检测、根因分析、hold and test）是**举例不是穷举**——"it is not possible to provide a comprehensive set of corrective actions"，按污染致消费者发病的风险定〔L.mono XIII.D.7〕。
- How often（频次基线）：连续记录→至少每批（批式）或每日（连续）人工核查偏离；批次参数→每批；泵速→每班两次；仪表校准/精度核查→至少每年（漂移快的加密）。**检测的效力定位**（建议层）：单批检测"is of limited value in establishing the acceptability of that lot and cannot substitute for appropriate controls on its manufacture/processing"，其价值在"a history of test results that is used to verify the adequacy of control measures over time"〔L.mono VIII.B.5〕。单批合格≠该批安全；检测是补充手段与趋势证据，不是工艺控制的替代品。
- Who：具名到角色，自动化不取消人工核查义务。法定基线：所有参与制造/加工/包装/贮存的人（**含临时与季节工**）须具备资质并接受食品卫生与食品安全培训〔§ 117.4〕；管理层对 Subpart B/F 负确保责任，owner/operator/agent-in-charge 对 C–G 负责；培训记录是受 Subpart F 约束的法定记录〔§ 117.9(b)(2)〕。**专项培训（李斯特菌场景，建议层）**：对象覆盖"all personnel and contractors who enter production and storage areas"（含承包商及生产、维护、QA/QC、仓储人员），内容讲清每个人的角色、为何重要、管理层对遵守的期待；**上岗前**完成，"with refresher training on at least an annual basis"〔L.mono XVI〕。四类须**成功完成**培训的主管职责：①保证 listericidal 与 listeristatic 控制有效运行；②采集与检测环境样品及 RTE 成品样品；③判定并采取纠正措施；④建立并使用书面卫生程序并执行相关监测〔L.mono XVI〕。

**Step 2 双线限值**（完成标准：关键限+操作限分离，分层依据=失效后果是否触及安全）
- 关键限=安全红线；操作限=更严内控线，偏离只 adjustment（建议记录用于趋势分析）。
- 判停规则：若"操作限"的失效后果最终触及安全（如货架期操作限），则视同关键限从严（Salsa A 规则）。

**Step 3 偏差发生时的标准动作**（判定规则显式化）
- 圈定受影响范围：默认推定**自上次合格检查/上次校准/上次清洁起**全部未受控；过敏原=cleanup to cleanup，要缩小范围须自证中间时点合格。**该口径的适用范围已扩展**到成品 L. monocytogenes 阳性场景（同一条口径扩用，非新增平行规则）："We recommend that you hold all product that is represented by the food you test, e.g., food lots produced from cleanup to cleanup."〔L.mono XIV.A〕受牵连范围的操作边界是"两次清洁消毒之间的批次"——"You should consider lots produced between two cleaning and sanitizing cycles to be implicated by the product positive"〔L.mono XIV.B〕；"批"＝"production on a processing line, with cleaning and sanitizing between production lots"〔L.mono XIII.F.1〕。
- 分诊——法定两条并列通道〔§ 117.150(c)〕，任一成立即可走 correction 免完整纠正措施：(1) 及时识别并纠正与过敏原**交叉接触控制**〔§ 117.135(c)(2)(i)〕或卫生控制〔§ 117.135(c)(3)(i)(ii)〕不一致的"条件与实践"——**无"孤立"限定**，反复发生仍可走此通道；(2) 及时纠正轻微且孤立、不直接影响产品安全的问题。注意：过敏原标签控制〔(c)(2)(ii)〕**走不了通道 1**，贴错标签必须做完整纠正措施。其余→corrective action 四步〔§ 117.150(a)(2)〕：识别并纠正、降低复发可能、评估全部受影响食品、**cannot ensure not adulterated or misbranded** 即阻止入市。
- 未预期食品安全问题三情形（须升级评估）〔§ 117.150(b)〕：预防控制不当且无预案/控制或 FSP 整体无效/记录审查发现记录不完备、活动未按 FSP 执行或纠正决定不当。
- 处置阶梯（先救回再降级）：补足处理 → 再加工 → 暂存待 PCQI 评估 → 降级改用途（RTE→非 RTE）→ 转饲料 → 销毁；每级以"能否用证据证明该用途下危害不成立"为准，安全判定权归 PCQI。再调理（reconditioning）法定下限〔§ 117.80(c)(9)〕：只能用经证明有效的方法再处理，或再处理后**复检确认不再 adulterated** 才可并入其他食品——"经验上应该没问题"不是法定出口。
- 处置阶梯在成品 L. monocytogenes 阳性场景的具体化（四条路径，建议层）〔L.mono XIV.B〕："You reprocess with a validated listericidal control measure, divert to a use in which the food will not be consumed by humans or animals, send for use in food to be consumed by animals where appropriate, or destroy the lot(s) of RTE food in which L. monocytogenes has been detected."——**再加工须用已验证的 listericidal 控制措施**（"validated"是硬字眼，不是"再加热一下"）。其他可能受污染批次须"segregate and hold"并走 **hold and test** 程序（数值归环境病原卡）；工厂侧纠正措施为"intensified sampling and testing of FCSs and non-FCSs"直至找到并消除污染源，并判定已入市产品是否须召回。
- 配方型偏差的**时点分叉**（建议层，与上条并列而非替代）：抑制型配方参数（pH、水活度、抗菌成分加入量）在**生产中**发现不对，"you can take appropriate actions to adjust the parameter to the appropriate value"；**包装后**才发现不对，"you should evaluate the food for safety and not release the food into commerce unless determined to be safe"，判定安全才放行（判定人见 Step 7），并查明原因、防止再发〔L.mono IX.B.3〕。分叉点是**包装前后**。致死型侧同构：温度低于工艺控制温度时"you may be able to increase the time to achieve an equivalent lethality"，建议 PCQI 参与该纠正；包装后才发现且已入市、评估提示安全顾虑时应召回该产品〔L.mono XI〕。
- "暂存待评估"的第二个触发点（隔离暂扣）：待检原料与受检结果影响的产品须有流程隔离暂扣——"You should have a process in place to segregate and hold all raw materials or other ingredients that are tested prior to use and products that will be affected by test results."〔L.mono VIII.B.5〕与处置阶梯的"暂存待 PCQI 评估"是同一动作的两种触发：偏差触发与检测结果触发。
- 成品抽检的**检测方向**与阳性判定（建议层）：成品应检 L. monocytogenes 而非 Listeria spp.——"because of the risk to public health from L. monocytogenes in food"；若选检 Listeria spp. 且阳性，"we recommend you determine whether the Listeria spp. is L. monocytogenes or treat the food as if it were contaminated with L. monocytogenes"〔L.mono XIV.A〕。**方向与环境保护相反**（环境监测检 spp.、成品检 L. monocytogenes），不可互相照搬。
- 反复出现=程序无效 → 强制对该部分做 FSP 再分析（不是再修一次机器）。

**Step 4 验证体系**（完成标准：validation 与 verification 分别有归档证据）
- validation 法定时段窗〔§ 117.160(b)(1)〕：FSP 实施前完成；或（证明控制可按设计实施）首批投产后 **90 个日历日内**；超 90 天须 PCQI 书面论证。证据顺序〔§ 117.160(b)(2)〕：以获取并评估科学技术证据为先，证据不可得或不充分时才自行研究——文献够用就不做厂内研究。
- validation 豁免〔§ 117.160(c)〕=四类列举（过敏原控制、卫生控制、召回计划、供应链程序）**+ (c)(5) PCQI 书面论证兜底通道**（按危害性质+控制性质及其在体系中的角色论证"validation 不适用"）——口径是"四+一兜底"，不是只有四类。
- 管理组件映射**法定不对称**〔§ 117.140〕，不能一刀切说"免 validation 就不免管理组件"：过程/卫生/过敏原控制=免 validation 但管理组件全套仍在；供应链程序只挂**三件**——纠正措施、记录审查〔§ 117.165(a)(4)〕、再分析，**无监控**、无 validation〔§ 117.140(b)〕；召回计划则**整体不受 (a) 款**（监控/纠正/验证）约束〔§ 117.140(c)〕。
- verification（证明执行有效，日常）：校准/精度核查、产品检测、环境监测（如适用）、记录审查——监控与纠正记录须在产生后 **7 个工作日**内由 PCQI 或 PCQI 监督下审查，超期须 PCQI 书面论证〔§ 117.165(a)(4)(i)〕；校准/检测/供应链验证记录在"合理时间内"审查〔§ 117.165(a)(4)(ii)〕——双轨时限不可混同。
- 验证活动（抑制型配方，建议层）〔L.mono IX.B.2〕：四类措施任选组合，目标是"any formulation or process is consistently applied and the applicable control is consistently achieved"——①按厂商或权威来源校准 pH/水活度测量设备，**或**由非当批操作责任人员定期旁观 pH/水活度测定过程以核查测法；②由非当批操作责任人员偶尔旁观抗菌成分按规定量加入以核查批次控制；③若控制依赖配料比例正确，定期抽测一批成品的 pH/水活度；④审查测量记录，确认准确且数值落在工艺控制参数的最小/最大值之内。②是最低成本的有效性核查手段——防"量对了但测错了"，与校准防的"仪器失准"不是同一失效模式。
- 成品抽检的频次与抽样方案（建议层）〔L.mono XIV.A〕：须有书面程序规定抽样频次（如 monthly、quarterly）与抽样方案，取决于三方面——客户要求、成品被 L. monocytogenes 污染后引发食源性疾病的风险、**环境样品中 Listeria spp. 的检出频率**。第三条是跨程序联动：环境数据反哺成品抽检频次，不是可独立设定的一次性参数。
- 书面程序的周期性验证（建议层）：环境监测书面程序本身也要被验证——"We recommend that you periodically verify your written environmental monitoring procedures by increased and intensive environmental sampling of the plant to assess whether the sampling sites are appropriate."〔L.mono XIII.D.8〕程序写对不等于点位选对。
- 五类法定验证活动为封闭清单〔§ 117.155(a)(1)–(5)〕，裁剪（如免产品检测/环境监测）须以暴露史论证并书面化。

**Step 5 记录体系与减负**（完成标准：减负方案有合法性前提）
- 六项法定一般要件〔§ 117.305(a)–(f)〕：原件/真实副本（复印/拍照/扫描/缩微）/电子记录；载入监控与验证活动的**实际数值与观察结果**；准确、不可擦改、清晰可读；**与所记录活动同时创建**；含设施标识、日期（及时间）、执行人签名或 initials、产品与批次号。FSP 在初次完成与每次修改时须由负责人签署并注明日期〔§ 117.310(b)〕。
- 记录要件**按控制类型分组**，不是一张通用表（建议层，各组自带 Part 117 映射）：  - 卫生控制（4 类）〔L.mono VII.E〕：书面卫生程序、书面卫生监测程序、卫生监测结果、"对不符合书面卫生程序的已监控卫生状况与实践所作的纠正"。映射〔L.mono VII.F〕：一般卫生程序〔§ 117.35(a)(d)(1)〕〔§ 117.135(d)(3)〕〔§ 117.80(c)(1)(c)(7)〕、地漏〔§ 117.10(b)(1)(b)(3)〕〔§ 117.37(b)(3)〕、消毒程序与溶液〔§ 117.35(a)(b)(d)(1)(d)(2)〕、卫生监测〔§ 117.145〕、卫生记录〔§ 117.145(c)〕〔§ 117.190〕。
  - 抑制型配方（6 项）〔L.mono IX.C〕：工艺控制参数（pH、水活度、抗菌成分浓度）、设备校准、抑制型控制的 validation、监控与/或 verification 记录、记录审查、任何纠正措施或纠正。映射〔L.mono IX.D〕〔§ 117.80(c)(4)〕〔§ 117.135(c)(1)〕〔§ 117.145〕〔§ 117.150〕〔§ 117.155〕〔§ 117.160〕〔§ 117.165〕〔§ 117.190〕。
  - 原料与配料（6 项）〔L.mono VIII.C〕：可预见被 L. monocytogenes 污染的原料清单、书面供应商程序、供应商审核结果、所依赖的 COA 或 COC、原料取样与检测的书面程序（含抽样方案与采样/制备/分析方法）、原料检测结果。映射〔L.mono VIII.D〕〔§ 117.80(a)(b)(2)(c)(4)〕及 Subpart G。
  - 环境监测（3 类）与成品抽检（3 类）：各自的书面程序（含采样、制备、分析方法、纠正措施程序）、污染检出后采取的纠正措施、检测结果〔L.mono XIII.I〕〔XIV.C〕；映射〔§ 117.80(a)(5)(6)〕〔§ 117.150〕〔§ 117.155〕〔§ 117.165〕〔L.mono XIII.J〕〔XIV.D〕。
- 趋势分析本身也要留记录："We recommend that you establish and maintain a record of any trend analysis that you conduct."〔L.mono XV.C〕只留原始检测数据不算留痕——分析动作与结论本身是独立的记录类别。
- 记录内容 vs 记录保存：L.mono 第十八章只列"该记录什么"，**不新增保存期限**——期限仍以〔§ 117.315〕为准（见 B3）。
- 电子记录边界〔§ 117.305(g)〕：**仅为满足 Part 117** 建立/保存的电子记录豁免 21 CFR Part 11；同一记录若还被其他法规要求，仍受 Part 11——上 LIMS/电子批记录前先查记录的双源属性。
- 例外记录（exception record）：正常态有连续自动化背书（自动条码扫描、CIP）时，只在失控时建记录——省的是正常态记录，不是监控动作。法定依据：需时间/温度控制食品的冷藏温度监控可用肯定记录**或**例外记录，其他情形例外记录"may be adequate"（一般许可句）〔§ 117.145(c)(2)〕。
- 披露接口〔§ 117.325〕：FDA 依本部分获取的记录适用 21 CFR Part 20 公开披露框架——Part 117 不赋予自动保密，商业机密须在提交时**主动主张保密**。
- 预授权决策预案：按产品/情境穷举处置选项书面预授权（Soup B 可/不可再加工清单），紧急时刻查表执行。

**Step 6 动态维护**（完成标准：触发器清单写入 FSP）
- 周期轨：整体至少每 3 年一次（3 年时钟只约束"整体"再分析）〔§ 117.170(a)〕；事件轨：重大变更/新危害信息/意外问题〔§ 117.150(b)〕/控制无效→可限于适用部分做**局部**再分析〔§ 117.170(b)(1)–(4)〕。第五类触发器：FDA 认定需应对新危害或科学进展时**指令**再分析〔§ 117.170(f)〕——企业清单之外多一条监管方发起的强制通道。时段锚点：预防控制适格性锚定"分析当时的科学认知"〔§ 117.3〕——科学进展本身构成法定再评估理由，不必等其他事件发生。
- **两个复审时钟不可互相顶替**：3 年管"整体再分析"，1 年管"书面程序本身的复审与按需更新"——"We recommend that you review and update, as needed, your written procedures at least once a year."〔L.mono XVIII〕（建议层）。程序写完就长期不动是常见失效模式：产品线、供应商、危害谱变了而程序文本没变，属于程序与现实脱节，不必然触发〔§ 117.170(b)〕的事件轨，却仍然违规。两钟各自独立走。
- 完成时限〔§ 117.170(c)〕：事件触发的再分析（含新增控制的 validation）须在**变更生效前**完成，或首批投产后 90 个日历日内，超期须 PCQI 书面论证；再分析产出=修订 FSP，**或书面记录"无需修订"的结论依据**〔§ 117.170(d)〕——改不改，结论都要留痕。
- 升格最小操作〔§ 117.135(c)(6)〕：有法定背书——"卫生培训及其他 CGMP"即"其他控制"的法定示例；CGMP 措施+捆绑管理组件（监控/记录）即成预防控制——义务按风险分配而非一刀切。

**Step 7 PCQI 法定专属职能**（完成标准：封闭清单落实到具名 PCQI）
- 八项职能必须由 PCQI 执行或监督〔§ 117.180(a)(1)–(8)〕：编制 FSP、验证、记录审查、再分析等；其中三项"延长时限书面论证"（validation 超 90 日窗、记录审查超 7 工作日、再分析完成超 90 日窗）及"免 validation 认定"**不可下放**——放宽时限的论证不能让 QA 经理签字。
- PCQI **可以不是雇员**〔§ 117.180(c)(1)〕：经 FDA 认可的标准化课程培训、或以同等工作经验取得资格；培训记录须含日期、类型、受训人三要素〔§ 117.180(d)〕。
- PCQI 是包装后配方偏差的**放行判定人**（建议层）：Step 3 时点分叉中"判定安全"这一步落在 PCQI 身上，不在产线主管身上；不属 subpart C 的场所则由其食品安全负责人承担同一判定〔L.mono IX.B.3〕。
- PCQI 的**不可下放清单不因建议层而缩短**：上述四项"不可下放"是〔§ 117.180〕的法定边界，L.mono 指南的建议层内容不能扩写或缩减它；反之指南把"成功完成培训"要求施加到 Step 1 所列四类主管职责上〔L.mono XVI〕——承担者须**successfully complete**培训，而不是"参加过"。

## B — Boundary（边界）

1. **闭环不能替代危害分析**：管理组件是执行的保障，不是识别危害的工具；危害分析做错则整套闭环在错误前提上空转（x01）。用户在"要不要控制"阶段求助时，先回危害分析卡。
2. **验证强度有天花板也有地板**：五类验证活动〔§ 117.155(a)(1)–(5)〕是封闭清单，不能自创第六类；也不能以"越多越好"过度堆叠——每项裁剪都要书面依据，过度工程与偷工减料两头都被封住；管理组件挂装本身按控制类型法定不对称〔§ 117.140(b)(c)〕（见 Step 4），裁剪照控制类型查表。
3. **记录保存与官方调阅**：保存三类期限〔§ 117.315〕——一般记录厂内保存自创建起至少 2 年；支撑 qualified facility 身份的记录须保存至足以支撑相关日历年身份；设备/工艺总体适宜性记录（含研究结果）停用后至少再存 2 年。官方调阅法定措辞〔§ 117.320〕：所有记录在**口头或书面请求**下须 **promptly available** 供审查和复制——现场记录**无延时窗口**；"24 小时"仅适用**异地存储件的取回**〔§ 117.315(c)〕与工厂长期关闭时转移的 FSP〔§ 117.315(d)〕。**FSP 必须驻场**（电子记录现场可及即算现场）——执行可外置（顾问 PCQI、集团代管），但 FSP 不能离场、没有"24 小时救回"的余地。
4. **频次裁剪不能拍脑袋**：回溯推定规则使监控/校准间隔直接等于单次失效的最大损失——频次是风险定价变量；示例给出的 15 批连续合格才降频（Soup A/Salsa A）是照抄级别的数值协议，"改了就好"不构成降频理由。
5. **书面化是弹性的代价**：默认参数（7 个工作日审查、validation 90 日窗等）可经 PCQI 书面论证偏离，且书面论证职能本身不可下放给非 PCQI；但"'风险不存在'的豁免也是结论而非省略"——口头放宽、邮件里的"应该没事"都不算。
6. **草案与语境限制**：指南部分为 Draft 且 Ch9（过程验证专章）未发布，validation 方法学细节不完整；should 与 must 分层阅读，纯建议不构成法定义务，但被"must+条款号"引用的（如 SAHCODH 年审）是硬规则。本卡〔§ 117.xxx〕括注均为最终规则法定义务，与指南 should 冲突时一律以法规为准。
