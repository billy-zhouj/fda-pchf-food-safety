# 危害分析方法（hazard-analysis-method）

*来源分层：本卡融合两类权威——FDA 行业指南（草案，方法论解释）与 21 CFR Part 117 法规正文（最终规则，法定义务）。标注〔§ 117.xxx〕的内容出自法规正文；其余出自指南。*

## R — Reading（原文）

> "If you do not conduct the hazard analysis correctly, and do not identify all hazards warranting preventive controls within the food safety plan, the food safety plan will not be effective in protecting consumers and preventing food safety issues, no matter how well your facility follows the plan."
> —— Ch2 §2.2

自译：如果危害分析做得不对、没有识别出所有需要预防控制的危害，那么无论工厂把计划执行得多好，这份食品安全计划都无法保护消费者。危害分析是整个 FSP 的阿基米德支点——它在，一切才有意义；它错，后面全部白做。

## I — Interpretation（自述）

这套方法把"我的产品里有什么危害、哪些必须管"从直觉判断变成一份可检查的书面推演。骨架分三层漏斗：**全集 → potential hazard（建议评估的起点）→ 需预防控制的危害**。前两层只做穷尽（防遗漏），第三层才做决策（严重性×概率 + 法定十类因素评估）。

落地工具是**六列工作表**：步骤 → 识别危害 → 是否需要预防控制（Yes/No）→ 判定理由 → 预防控制是什么 → 在哪一步控制。三个反直觉的设计：
1. **"No" 与 "Yes" 同等重要**——排除一项危害的书面理由，和决定控制它的理由承担同样的举证义务；空白的 No 等于没有评估过。
2. **发现点 ≠ 控制点**——危害在哪一步被发现，与在哪一步控制最有效，是两个独立决策，第 6 列强制显式选位。
3. **结论是状态机不是句号**——判定可以写成"不是需控危害，除非某信息出现"，触发条件本身就是分析结论的一部分。

法定建筑（法规正文）：危害分析只是 FSP 的第一部件——书面 FSP 必须包含且仅列七部件：危害分析、预防控制、供应链程序、召回计划，以及监控、纠正措施、验证三类程序〔§ 117.126(b)(1)–(7)〕；由 PCQI 编制或监督编制；FSP 整体是受 Subpart F 记录规则约束的记录〔§ 117.126(c)〕。注意 validation（确认）报告不在这份封闭清单里，走记录体系。预防控制包含 CCP 处的控制——但措辞是"if there are any CCPs"〔§ 117.135(a)(2)(i)〕：CCP 是可选而非强制，存量 HACCP 企业升级到 FSP 后可以不保留 CCP 概念，非 CCP 的工艺控制（process control）同样合格〔§ 117.135(a)(2)(ii)〕。所有预防控制的法定目标统一锚定在一句定义上：significantly minimize = "降到可接受水平，包括消除"〔§ 117.3〕——控制目标不必是零，"可接受水平 ≠ 零检出，消除只是特例"。

## A1 — Past Application（书中案例）

**案例 1：Cookie A 的六列全流程**
曲奇厂从原料（面粉、鸡蛋、花生酱）识别出沙门氏菌危害，经严重性×概率评估判为需控危害；控制落点不在接收步骤而在烘焙（致死处理）——第 6 列指向热处理而非"在哪发现在哪修"。最终落到三条关键限值（炉温≥350°F、时间≥13 min、面团≤28 g）。结论：识别、评估、判定、落点四层解耦后，每一步都可辩护、可检查。

**案例 2：Miller C 的条件性升格**
磨粉厂对小麦 DON 毒素的结论写成："不是需预防控制的危害——除非新麦检测或 USDA 周报显示可能超标"。平时物理清理按 CGMP 运行；触发信息一到，同一套清理立即按预防控制运行（配监控/验证/纠正/记录）。结果：危害分析从静态文档变成可随信息流切换的活规则。

**案例 3：Sandwich F 的"No"论证**
三明治厂对预切片面包的 DON 不重复上游功课，而是审查"面包师 D 如何评估磨粉厂程序"，据此书面判定"无需预防控制"。它示范了两件事：No 的理由可以是"上游保证链充分"，且这条理由与 Yes 结论同等书面化——不是省略，是结论。

**反例对照**：流程图不现场核实导致漏步骤；工作表上 Yes 写满理由、No 留空——空白的 No 在检查中等于没有评估过。

## A2 — Future Trigger（何时用 / 与相邻能力的区分）

**触发场景**：
- 用户要"给新产品/新产线做危害分析"（hazard analysis、识别危害、判定要不要控制）
- 用户问"这个危害要不要写进 FSP/要不要设控制措施"、"附录 1 表上没打 X 能不能判 No"
- 用户做体系升级："HACCP 计划怎么升到 FSP"、检查前自查危害分析
- 供应商或原料出了新信息，问"原来的分析还算数吗"

**与相邻卡的区分**：
- **预防控制管理组件闭环**：危害分析判完"Yes"之后，如何监控/纠正/验证/记录那个控制——那是管理组件的事；本卡止步于"识别出危害并选定控制"，产出的是六列工作表。
- **工艺控制与热处理验证**：第 6 列落点选了"致死/配方/时间温度"这类工艺控制之后，怎么定目标菌、定关键限值、做验证——本卡不管限值怎么来。
- **环境病原与卫生控制**：六列评估触发"RTE 食品暴露于环境"的强制项后，卫生战略怎么选是那边的领域。
- **食品过敏原程序**：过敏原危害识别出"防交叉接触+标签"双控制后的程序搭建是那边的领域；本卡只负责把过敏原判进/判出需控清单。
- 与**供应链控制**（化学危害卡）：第 6 列若选"接收前由供应商控制"，则触发供应链程序——判定在先，程序在后。

## E — Execution（可执行步骤）

**Step 1 前期三件套**（完成标准：三项书面件齐备）
- 组建小组（可 1 人兼多角，PCQI 编制或监督）、产品描述（含储运/预期用途/消费者）、流程图。
- 流程图必须**现场逐段核实**（含回掺、暂存、室温暴露等易漏步骤）——办公室画图直接进分析是已点名的失败模式。
- **品类输入用李斯特菌的品类清单，不用通用"湿/干"分类**（李斯特菌专项）。先判断产品是否落在"支持李斯特菌生长且已被发现受污染"的 RTE 品类内：
  > "Examples of RTE foods that support the growth of *L. monocytogenes* and that have been found to be contaminated with *L. monocytogenes* are unpasteurized and pasteurized milk, high fat dairy products, soft unripened cheese (Cottage Cheese, Cream Cheese, Ricotta), cooked ready-to-eat crustaceans (shrimp, crab), smoked seafood, fresh soft cheese (Queso Fresco), semi-soft cheese (Blue, Brick, Monterey), soft-ripened cheese (Brie, Camembert, Feta), delitype salads, sandwiches, fresh-cut fruits and vegetables, and raw molluscan shellfish (Ref. 7, Ref. 26, and Ref. 27)."
  > —— L.mono 指南 II.B（Characteristics of L. monocytogenes）

  > "An example of an RTE food that does not support the growth of ... , but has been found to be contaminated with *L. monocytogenes*, is ice cream (Ref. 28 and Ref. 6)."
  > —— L.mono 指南 II.B（原文首句的物种名跨行断开，此处从断点省略）
  清单是**起点不是答案**，反例比清单本身更重要：冰淇淋不支持李斯特菌生长却仍被检出污染——"不支持生长"只影响危害的**严重性**评估，不影响"是否需要控制"。按生长能力给 RTE 品类降档（把凉拌菜、鲜切果蔬当低风险处理）是典型误判。
- 法定证据基准：危害分析必须基于"经验、疾病数据、科学报告及其他信息"来识别和评估危害〔§ 117.130(a)〕——illness data（疾病数据）是法规单列的一类信息源，历史暴发记录按此归档引用。
- 法定 must：危害分析必须书面成文，无论分析结果如何〔§ 117.130(a)〕——"零危害结论"不豁免成文义务，一份"全部判 No"的书面分析本身就是法定记录。

**Step 2 逐步骤识别**（完成标准：每个步骤覆盖生物/化学/物理三类 + 原料/工艺/设施/人员四来源）
- 多组分产品按"Σ各原料危害 + 加工方式引入危害"分解评估。
- 危害是"配料×下游用途"的函数：干配料仅在复水/入高水分食品时评估芽孢菌。
- 加二阶链推理：本身无害之物若能改变屏障参数（如耗酸菌抬 pH 瓦解肉毒屏障），按危害处理。
- 参考附录 1 的 X 标记，但只当起点——X 可能不适用于你的产品，没 X 的可能因产地/用途而存在。
- **原料来源一侧先建"可能带菌"清单，再谈控制**（李斯特菌专项）：评估哪些原料与配料（生或最小加工食品）比其他更可能带李斯特菌，据此聚焦控制努力，并建立一份"可合理预见会被污染"的原料清单：
  > "We recommend that you assess which raw materials and other ingredients (such as raw or minimally processed foods) are more likely to be contaminated with *L. monocytogenes* than others and focus control efforts on these ingredients. Based on this assessment, you should establish a list of raw materials and other ingredients for which it is reasonably foreseeable that the ingredients could be contaminated with *L. monocytogenes* ."
  > —— L.mono 指南 VIII.A（Raw Materials and Other Ingredients That are Potential Sources of L. monocytogenes）
  清单每一项的默认状态由举证责任方向决定——**信息不足时按"可能污染"处理**，而不是按"未证明污染所以放行"处理：
  > "In the absence of adequate information about the risk presented by a particular ingredient, we recommend that you assume that the ingredient could be contaminated with *L. monocytogenes* ."
  > —— L.mono 指南 VIII.B（Controlling L. monocytogenes in Raw Materials and Other Ingredients When Contamination With L. monocytogenes Is Reasonably Foreseeable）
  这一步落在危害分析工作表的第 2 列（识别危害）：原料项列在"可能带菌清单"上，其控制主体是供应商还是本厂由供应链卡决定。
- 法定三分类枚举〔§ 117.130(b)〕：生物危害（含寄生虫与环境病原）、化学危害（含放射学危害、农兽药残、天然毒素、**腐败分解 decomposition**、未批准的食用或色素添加剂、过敏原）、物理危害（石块、玻璃、金属等）。来源三渠道：天然存在／无意引入／**为经济利益故意引入（EMA）**〔§ 117.130(b)〕。注意：decomposition 在法规里是法定化学危害——腐败在"致病/变质分界"上的归类要与 B1 条并读，别默认腐败一律踢出危害分析。

**Step 3 评估**（完成标准：每个 potential hazard 有严重性×概率双维结论 + 十类因素留痕）
- 严重性（致病/致伤程度）× 概率（历史暴发、配方、工艺、设施、消费者）。
- 法定参照系（方法学分水岭）：概率必须在反事实条件下评估——"假设不存在任何预防控制时该危害发生的概率"〔§ 117.130(c)(1)(i)〕。不得先用现有 CGMP/在运措施压低概率再判 No；"现有措施已控制住"不是把概率调低的理由，它属于 Step 4 的通道论证。
- 十因素的法定收口视角：评估的是上述因素"对**预期消费者**的**成品**安全性的影响"〔§ 117.130(c)(2)〕——不是对半成品、不是对工厂风险。
- 用 117.130(c)(2) 十类因素查漏：配方/设施设备/原辅料/运输/加工/包装标签/储运/预期用途/卫生与员工健康/其他——每类留痕即构成完备性证据。第 (x) 类兜底因素自带法定实例：某些危害具有**时间性/天气相关性**（temporal, e.g., weather-related），如某些天然毒素水平随季节波动〔§ 117.130(c)(2)(x)〕——DON、组胺、贝类毒素的季节性评估在此有法定锚点。
- 判定术语的法定定义："已知或可合理预见的危害"与"需预防控制的危害"均按严重性×概率（且概率按"无预防控制时"评估）锚定〔§ 117.3〕，评估义务来源为〔§ 117.130(c)(1)〕。
- **强制触发器**：IF RTE 食品 AND 包装前暴露于环境 AND 包装后无致死处理 THEN 必须评估环境病原〔§ 117.130(c)(1)(ii)〕——两个客观条件相与即触发，与"我觉得没风险"无关。RTE 的法定判定基准：可合理预期消费者将**不经进一步处理（即无显著最小化生物危害的处理）食用**〔§ 117.3〕。该触发器的完整排除条件还有第二支：除非企业"otherwise include a control measure (such as a formulation lethal to the pathogen)"——即配方本身对病原致死等其他控制措施同样关闭触发〔§ 117.130(c)(1)(ii)〕。
- **触发前的分流动作：先查包装后有没有致死处理**（李斯特菌专项，指南层）。触发器的三个条件里，"包装后无致死处理"是最常被含糊处理的一个——"我厂有末端杀菌"是不是算数，取决于杀菌发生在**哪一步**：
  > "This guidance is intended to help you comply with the CGMP and PCHF requirements of part 117 with respect to measures that can significantly minimize or prevent the contamination of RTE food with *L. monocytogenes* whenever a RTE food is exposed to the environment prior to packaging and the packaged food does not receive a treatment or otherwise include a control measure (such as a formulation lethal to *L. monocytogenes* ) that would significantly minimize *L. monocytogenes* ."
  > —— L.mono 指南 I（Introduction）
  分析步骤上分成三问，结论须书面落进第 2 列：①包装后是否接受处理或含致死型配方控制？②若致死措施施加在**最终包装内**、或施加在**紧邻包装前**且该系统能充分屏蔽产品与包装的食品接触面不受环境污染，则触发器不成立（此时本指南不适用于该处理器）；③若致死措施虽在包装前、但系统屏蔽不足或环境暴露仍能发生，触发器仍成立。指南适用边界的完整口径与两类不适用情形见 `regulatory-boundaries` 卡。
- **易感人群加权（"不支持生长"不能当降档理由）**：不支持李斯特菌生长的食品，若专供医院、养老院等场所（食用人群为李斯特菌病高危人群），其处置须与支持生长的食品同等严格：
  > "we recommend that for a food that does not support growth and that is specifically intended for establishments such as hospitals and nursing homes (where the food would be consumed by populations at high risk for listeriosis), you take corrective actions in a similar manner as for foods that support growth."
  > —— L.mono 指南 XIII.F（Corrective Actions If You Detect Listeria spp. on a Food-Contact Surface）
  落到本卡 Step 3 的严重性×概率评估：严重性一侧必须按**实际食用人群**加权——"本品不支持生长"只能在无高危人群指向时作为降档依据；一旦用途指向高危人群场所，严重性评估按支持生长的食品同等取值（处置阶梯的具体动作归 `management-components` 卡）。

**Step 4 判定 Yes/No**（判停点）
- 对每个"Yes"：书面理由 ≥ 引用评估结论；对每个"No"：理由同等书面化，且须可供官方查阅复制。
- **先分清两层**（旧版"合法 No 三通道"是混层表述，现按法规拆正）：
  - **第一层——评估层判 No**："该危害不构成需预防控制的危害"，是在 Step 3 反事实评估框架〔§ 117.130(c)(1)〕内直接论证出的结论。极强致死工艺（工艺的产品属性要求本身绑定致死条件，如 240°F 煮糖、250°C×4.5min 咸饼干）与"CGMP/前提程序已有效覆盖"都在这一层论证——引用工艺证据，不许静默跳过。有争议的项保守列入第 2 列再论证排除。
  - **第二层——判 Yes 但不实施 PC**〔§ 117.136(a)(1)–(5)〕：已识别出需预防控制的危害后，仍可不实施预防控制的五条法定出口：(a)(1) 食品若无适当控制处理即无法食用（法定示例为 RAC——可可豆、咖啡豆、谷物等，比"消费前制备"窄且条件不同）；(a)(2)–(4) 客户依赖通道——标签或随附文件披露 "not processed to control [identified hazard]"、每年取得客户书面保证（(a)(4) 还要求客户向下游传递披露与保证的链式义务）；(a)(5) 自主分销链通道——自行建立、文件化并运行"确保在后续分销环节控制危害"的体系。走第二层必须保存相应记录〔§ 117.136(b)〕。本层通道实操详见 supply-chain-verification 卡。
- **若全部为 No** → FSP 可只含书面危害分析（+召回计划如适用），其余管理组件不强制。这是合法出口，不是偷懒。

**Step 5 控制识别与落点**（完成标准：每个 Yes 危害至少一个控制 + 落点显式选位）
- 一个控制可覆盖多个危害：控最耐热/最难的支配性病原，顺带覆盖敏感者（如按沙门氏菌 6D 设计即覆盖志贺氏菌）——覆盖不成立时才需要第二个控制。
- 控制位置选"最有效处"而非"发现处"：可前移（供应商控制→走供应链程序）、可后移（成品检测）。自厂控制该危害则无须供应链程序——位置选择决定程序类型。

**Step 6 写入触发器并维持**（完成标准：结论含"默认态+触发条件+升格动作"三段式）
- 至少每 3 年整体再分析；变更/新危害信息/意外问题/控制无效四类事件触发局部再分析（可限于相关部分）。
- 升格动作预埋到合同层：高风险季逐批索 COA、附条件验收等条款写进采购协议（Miller C→Baker D 模式）。

## B — Boundary（边界）

1. **质量缺陷不进危害分析**：虫害、毛发、异味等不致病不致伤，按法定定义不是 hazard——hazard 指"有致病或致伤潜在可能的任何生物、化学（**含放射学**）或物理因子"〔§ 117.3〕；把它们塞进 FSP 会稀释监控与验证资源；反过来把真正的安全危害当质量问题处理则漏控。注意"腐败"需分读：指南把腐败一概归质量缺陷，但法规把**腐败分解（decomposition）列为法定化学危害**〔§ 117.130(b)〕——可能伴生致病因子/毒素的分解要进危害分析，仅感官劣变才留在线外（与 Step 2 并读）。质量缺陷本身另有持续法定义务：必须始终运行把天然不可避免缺陷降到"当前可达到的最低水平"（lowest level currently feasible——随行业整体水平移动的动态标准）的质量控制操作〔§ 117.110(a)〕；**用合格料掺混稀释超标批次违法**——把缺陷水平已达 adulterated 的食品与另一批混合，无论终产品缺陷水平多低，终产品即 adulterated〔§ 117.110(b)〕。"稀释救批次"没有合法出口。defect action level 是非危害性、天然不可避免缺陷的可执法界限〔§ 117.3〕——低于它是质量线，不是安全线。FSP 也不是格式竞赛：FDA 无标准化格式，审查对象是信息完备性而非排版。
2. **X 表不是答案表**：照表全抄控制会过度合规，不看表会违规——三问检验（只适用部分产品？产地依赖？用途改变特性？）逐项过；判定责任不可外包给表格或同行 FSP 模板。
3. **指南是草案且半成品**：Ch7（时间温度）/8（配方干燥）/9（过程验证）/10（卫生程序）/13（物理危害）/17（RTE 分类）仍是占位，相关领域的细节本指南给不完整；引用数据（辐照 2016、附录 1 截至 2022）滞后，定稿会变。用它做分析框架，别把它当唯一依据。
4. **监管者视角的成本盲点**：体系默认企业请得起 PCQI、process authority、第三方审核——极小企业的真实合规成本被轻描淡写；历史上真正的暴发（花生酱、巧克力）恰恰发生在文件齐全的企业，书面体系可能制造虚假安全感。危害分析的质量上限取决于 PCQI 个人水平，法定框架不保证这一点。
5. **美国法规语境**：全部建立在 FD&C Act / 21 CFR 之上；其他法域读者须自行映射本国体系（如 GB 14881），"以书面判定为核心的检查式合规"逻辑不能直接平移。
6. **再分析周期不是保险**：3 年周期+四类触发器仍可能漏掉新危害——2023 肉桂苹果酱铅事件靠儿童血铅异常才被发现，不是靠任何设施的再分析捕捉的。
7. **本卡新织入的李斯特菌判据属建议层**：以上标注〔L.mono 指南 …〕的内容出自 FDA《Control of Listeria monocytogenes in Ready-To-Eat Foods: Guidance for Industry（Draft，2017 年 1 月）》，正文一律 "we recommend that you…"，本身不设法律责任，可采用替代做法；本卡把它们当作**分析步骤的细化建议**，不当作法定触发条件——法定触发器仍只有〔§ 117.130(c)(1)(ii)〕那三个客观条件。凡本卡标〔§ 117.xxx〕的才是法定义务，两层不得混引。
