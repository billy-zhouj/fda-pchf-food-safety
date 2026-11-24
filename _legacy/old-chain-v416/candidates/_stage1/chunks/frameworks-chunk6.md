# Framework Extractor — Chunk 6 候选（第 16501–19461 行：附录 1 / 附录 2 / 附录 3）

> 扫描员：framework-extractor（6/6）。本段覆盖附录 1（分层危害表）、附录 2（FSP 表单）、附录 3（生长/灭活数据）。
> 未做筛选，宁错杀；每条含原文摘录（≤100 英文词）。"是否反复出现"仅在本段内判断。

```yaml
- id: f6-01
  title: 分层危害分析三层级法（universe → potential → requiring preventive control）
  type: framework
  source_chapter: 附录 1（A1.3 / A1.8.1）
  source_quote: |
    "This tiered approach considers three levels of hazards: - The universe of hazards most
    relevant to food safety; - Known or reasonably foreseeable hazards ("potential hazards");
    and - Hazards requiring a preventive control. ... you conduct your hazard analysis by first
    broadly considering the universe of all hazards relevant to food safety and then, through
    the process of hazard identification, narrowing that broad list of hazards..."
  summary: |
    任何风险评估都可以搭成三级漏斗：第一层是"与食品安全相关的全部危害"的全集；
    第二层通过"危害识别"收窄为对本厂/本食品"已知或可合理预见"的危害（potential hazard）；
    第三层通过"危害评估"再收窄为"需要预防控制的危害"子集。
    每一层都有明确的输入和操作：识别靠问题清单+潜在危害表，评估靠严重性×概率。
    这是一个可迁移的"全集→相关集→行动集"漏斗结构，适用于任何从开放空间收敛到决策的场合。
  tags: [mental-model, funnel, hazard-analysis, tiered-approach]

- id: f6-02
  title: 术语即思维阶段提示（合并术语法）
  type: framework
  source_chapter: 附录 1（A1.1）
  source_quote: |
    "we use the combined term "known or reasonably foreseeable hazard ("potential hazard")" ...
    so that this guidance: consistently uses the term used in the regulatory text of part 117
    ...; consistently uses a term that could be more familiar to some users ...; and consistently
    reminds you that a known or reasonably foreseeable hazard is still being evaluated to
    determine whether it is a hazard requiring a preventive control for a food."
  summary: |
    FDA 故意并置两个术语——法规术语和 HACCP 圈熟悉的"potential hazard"——做成一个合并词。
    目的不是文字游戏，而是让术语本身每次出现都提醒使用者：这个危害还在评估中，尚未判定需要控制。
    这是"用语言设计承载思维状态"的方法：当你想防止读者跳过中间判断时，把判断状态写进术语。
    可迁移到任何流程文档：术语选择本身就是防跳步的提示器。
  tags: [mental-model, language-design, terminology, hazard-analysis]

- id: f6-03
  title: 查表是起点不是终点（SME 建议与工厂责任分离）
  type: framework
  source_chapter: 附录 1（A1.5 / A1.10 表头）
  source_quote: |
    "While Appendix 1 is a comprehensive starting point, each facility has the ultimate
    responsibility to identify the hazards relevant to food manufactured, processed, packed, or
    held at that facility, such as hazards that are associated with its facility-specific history
    even though they are not identified as known or reasonably foreseeable ("potential") hazards
    in the tables."
  summary: |
    附录 1 的 X 标记表由主题专家（SME）基于文献、召回数据和监管数据库编制，但它只回答
    "哪些危害值得评估"，绝不回答"哪些危害需要控制"——后者永远是每个工厂自己的责任。
    表中未列出的本厂历史危害、设施特有危害仍必须自行识别；表中的 X 也不等于要控制。
    这是一个通用的"权威速查表"使用范式：速查表提供先验起点，个体情境判定不可外包。
    "照表抄控制"会过度，"不看表"会违规——两边都是错。
  tags: [decision-framework, reference-usage, responsibility, hazard-analysis]

- id: f6-04
  title: 多组分食品分解评估法（配料×工艺两个维度）
  type: framework
  source_chapter: 附录 1（A1.5.4）
  source_quote: |
    "Most foods contain multiple raw materials and other ingredients. ... it is not practical to
    include all multi-component foods in the tables, because the ingredients and processing
    methods can vary widely ... To assess the biological and chemical hazards for these
    multi-component foods, you should consider the hazards associated with the individual raw
    materials/ingredients, as well as the hazards that may arise from the processing methods
    used in making them."
  summary: |
    不可能为每种多组分食品（三明治、冷冻餐、糖果含果粒）单独建危害表，于是把问题分解：
    危害 = Σ（各原料/配料自身的危害）+（加工方式引入的危害）。
    表格脚注把这条逻辑反复实例化——"如果产品含 inclusion（坚果、巧克力豆、果粒），
    请查对应配料表"。同一条配料在不同用途下危害不同（见干配料水合条目）。
    这是一个可迁移的组合系统评估法：组合物查不了总表时，拆成部件表×组装方式二维求解。
  tags: [framework, decomposition, multi-component, hazard-analysis]

- id: f6-05
  title: 干配料水合才考虑芽孢菌（用途条件化危害判定）
  type: framework
  source_chapter: 附录 1（A1.5.4 及 Table 1F/1H/1J/1N/1O 脚注）
  source_quote: |
    "You should consider Bacillus cereus as a known or reasonably foreseeable hazard
    ("potential hazard") when you use the whole grains to manufacture/process a cooked
    high-moisture product (where B. cereus could grow), but not when you distribute dry whole
    grains to consumers or use the dry whole grains to manufacture/process a dry mix that
    consumers will cook."
  summary: |
    同一种配料（干谷物、香料、干汤粉、脱水蔬菜、奶粉）的芽孢菌危害是否成立，取决于它
    之后会不会被水合到允许生长的水分活度——dry 状态下 X 不适用，hydrated 状态下才适用。
    多张表的脚注反复出现同一句式："仅在 rehydrated and/or used as an ingredient in a
    high-moisture food 时适用"。
    这是一个可迁移的思维结构：危害的适用性不是配料的固有属性，而是"配料×下游使用场景"
    的函数——评估时要顺着产品的一生往下看，而不是孤立看原料。
  tags: [framework, conditional-hazard, water-activity, sporeformers, use-context]

- id: f6-06
  title: 极强致死工艺豁免逻辑（产品可行性反推危害豁免）
  type: framework
  source_chapter: 附录 1（A1.6.1.3）
  source_quote: |
    "Some food products can only be produced using exceptionally lethal processes that
    adequately control biological hazards. If the processing is not conducted in a way that
    adequately controls biological hazards, the product would not be suitable for distribution.
    Due to the exceptional lethality of the processes ... in some instances the SMEs did not
    identify any known or reasonably foreseeable ("potential") biological hazards for these
    foods (e.g., sugar confections in Table 1D and crackers in Table 1M)."
  summary: |
    焦糖要煮到 240°F 数分钟、果酱要熬煮变稠、饼干要在 250°C 烘 4.5 分钟——不做这些
    致死处理，产品根本做不成。工艺的物理必要性与食品安全控制在此重合。
    于是出现两种结果：强案例（糖食、饼干）SME 干脆不标任何潜在危害；弱案例（汤酱）
    仍标 X，但工厂可以基于"工艺极强致死"判定不需控制。
    可迁移点：当"做对产品"与"控住危害"是同一动作时，危害判定可走豁免路径——
    但前提是工艺本身稳定受控，且要写下理由。
  tags: [framework, exceptional-lethality, exemption-logic, process-control]

- id: f6-07
  title: 控主亦控次（支配性病原覆盖推理）
  type: framework
  source_chapter: 附录 1（A1.6.1.1 / A1.6.1.2.2）
  source_quote: |
    "If you identify Salmonella and/or pathogenic E. coli as a hazard requiring a preventive
    control, a preventive control that you establish and implement to significantly minimize or
    prevent Salmonella or pathogenic E. coli generally would also significantly minimize or
    prevent Shigella spp. Therefore, we decided that it was not necessary to separately identify
    Shigella spp. ... in any Food Group, and none of the Tables ... list Shigella spp."
  summary: |
    生可可豆的最主要危害是沙门氏菌，控制沙门氏菌的处理同样杀灭较不常见的李斯特菌和
    致病性大肠杆菌——所以 Table 1D 只标沙门氏菌。同理 FDA 把志贺氏菌从所有表中删除，
    理由是控制沙门氏菌/致病性大肠杆菌的措施一般也控制志贺氏菌。
    这是一个可迁移的"支配性风险"推理：在多个并列风险中识别出最严苛/最主导的一个，
    控制它即顺带控制其余，从而精简清单、避免重复工程。
  tags: [mental-model, dominant-hazard, simplification, pathogen-coverage]

- id: f6-08
  title: X 标记的三种适用性检验
  type: framework
  source_chapter: 附录 1（A1.8.2）
  source_quote: |
    "a hazard marked with an X could: - Be a known or reasonably foreseeable ("potential")
    hazard only for some products in a Food Subcategory ...; - Only be a known or reasonably
    foreseeable ("potential") hazard when a food ingredient is sourced from a specific
    geographic location ...; or - Only be a known or reasonably foreseeable ("potential") hazard
    when a food ingredient is used in a food that changes its characteristics (e.g., B. cereus in
    cooked (hydrated) rice but not dried rice)."
  summary: |
    面对表中的 X 标记，FDA 给出三问检验法：①我的具体产品是否属于该亚类中被标记覆盖
    的那部分（如 Cyclospora 只对部分香草适用）？②我的配料是否来自有污染史的特定产地
    （毒元素、农药）？③我的使用方式是否改变配料特性（干米→煮饭）？
    三问中任一为"否"，X 就可能不适用于你——但结论要写进危害分析。
    这是一个通用的"参考数据适用性检验"框架：任何统计/专家建议用到个体场景前先问
    覆盖范围、来源条件、状态改变三个维度。
  tags: [decision-framework, applicability-test, reference-usage, hazard-analysis]

- id: f6-09
  title: 判定不需控制的三条路径
  type: framework
  source_chapter: 附录 1（A1.8.3）
  source_quote: |
    "a hazard marked with an X in the Tables could be a hazard that does not require a
    preventive control if it has a low probability of occurring in your food product in light of
    your facility and your food due to: - a process control that has exceptional lethality ...;
    - the effectiveness of your CGMP practices in addressing the hazard ...; - likely preparation
    and handling steps before consumption (e.g., if your product is not an RTE food ... and
    your product label provides the end user with cooking instructions ...)"
  summary: |
    即便 X 标记适用，仍有一条通向"不需预防控制"的合法路径，FDA 列出三种情形：
    ①工艺具极强致死性（焦糖）；②CGMP 实践已有效覆盖该危害（员工卫生控制病毒/寄生虫）；
    ③消费前的制备环节会控制它（非即食食品+充分烹调说明）。
    注意这是"低概率成立"而非"危害不存在"，判定必须基于本厂、本产品情境并书面记录。
    可迁移为一个"已覆盖即免控"的检查结构：上游工艺、基础合规、下游用户三处任一
    已系统性控制时，可免设专门控制——但需论证。
  tags: [decision-framework, exemption, cgmp, consumer-use, hazard-analysis]

- id: f6-10
  title: 保守列名策略（把"否"也写进表）
  type: framework
  source_chapter: 附录 1（A1.8.2）
  source_quote: |
    "you may find it useful to take a conservative approach by listing in Column 2 several known
    or reasonably foreseeable ("potential") hazards even though they clearly do not require a
    preventive control (especially when there has been significant debate over whether something
    is actually a ... hazard for the facility), and explain the reasons for your "No" conclusion.
    This can be useful both during your own review ... and during review ... by others - e.g., if
    an inspector or auditor questions whether a particular hazard was considered."
  summary: |
    即使某危害明显不需要控制，当存在争议或质疑可能时，仍建议把它列进危害分析表第 2 列
    并写明"否"的理由。这不是过度合规，而是创建"已考虑过"的证据：自查时展示思考链，
    检查/审核质疑时能立即回答"我们考虑过，理由是……"。
    可迁移的思维结构：对高争议决策，与其事后辩解"没想到"，不如事前留痕"想过并排除"。
    与全书反复强调的"'No' 的解释与 'Yes' 同等重要"一脉相承。
  tags: [decision-framework, documentation, defensive-thinking, controversy]

- id: f6-11
  title: 按危害类别拆分法规适用性（LACF 边界切分法）
  type: framework
  source_chapter: 附录 1（A1.5.5）
  source_quote: |
    "The PCHF requirements do not apply with respect to activities that are subject to the LACF
    regulations (21 CFR part 113) for the control of biological hazards and, thus, LACF foods
    are not covered by the Food Categories/Food Subcategories in Tables 1A through 1P ... The
    PCHF requirements do apply to chemical and physical hazards that could be associated with
    an LACF food."
  summary: |
    同一罐装食品（LACF），生物危害归 part 113 管辖、由供应商的灭菌工艺控制，PCHF 不适用；
    但化学和物理危害 PCHF 仍然适用——查 Table 2H 而不是直接豁免。
    思维结构：法规/规则的适用性不是食品级别的"全有或全无"，而是"食品×危害类别"二维
    矩阵上的逐格判定。遇到重叠管辖或多体系时，把对象按维度拆开，逐格问"这条规则管不管
    这一类"。
  tags: [framework, jurisdiction, applicability-matrix, lacf, boundary]

- id: f6-12
  title: 化学危害配料分解法（无表食品组 → 查配料表）
  type: framework
  source_chapter: 附录 1（A1.11 / Food Group 2A、2F、2M、2N）
  source_quote: |
    "This Appendix does not include a Table of known or reasonably foreseeable ("potential")
    food-related chemical hazards for Bakery Items. Instead, for known or reasonably
    foreseeable ("potential") food-related chemical hazards for Bakery Items, you should see the
    Table(s) associated with the ingredients in your Bakery Item. - If your Bakery Item contains
    chocolate, you should consult Table 2D ... - If your Bakery Item contains eggs, you should
    consult Table 2G ..."
  summary: |
    16 个食品组中有 4 个（烘焙、调味酱、零食、汤酱）的化学危害完全取决于所用配料，
    FDA 干脆不建化学危害表，只留一个入口条目并给出"含巧克力查 2D、含蛋查 2G、
    含面粉查 2J、含果蔬查 2H"的路由规则。
    背后逻辑：化学危害（毒元素、真菌毒素、农药）主要通过供应链控制配料，所以按"可被
    当作配料的食品"组织表格。可迁移点：当组合物的风险由成分决定时，建成分级路由表
    而非穷举组合表。
  tags: [framework, ingredient-routing, supply-chain, chemical-hazards]

- id: f6-13
  title: FSP 渐进式编排逻辑（先论证再展开）
  type: framework
  source_chapter: 附录 2（Introduction）
  source_quote: |
    "we recommend that you arrange the information in your food safety plan in a progressive
    manner that clearly explains the thought process for the hazard analysis and the individual
    steps in the Food Safety Plan. ... Your hazard analysis should contain information to justify:
    Your identification of each hazard requiring a preventive control; and The types of preventive
    controls applied; - You should explain the details for each preventive control."
  summary: |
    表单体系 2-A 到 2-I 的排列不是随机的：产品描述（2-A）→危害分析（2-B）→按控制类型
    分列的过程/卫生/过敏原/供应链表单（2-C 至 2-I）——正是"思维过程→识别论证→控制细节"
    的渐进结构。FDA 明说格式不强制，但信息必须按此逻辑可追溯。
    可迁移点：任何合规/设计文档的编排原则是让读者能重走作者的推理路径——
    先给判定依据，再给判定结果，最后给实施细节。文档结构即推理结构的显影。
  tags: [framework, document-structure, progressive-arrangement, fsp]

- id: f6-14
  title: 过敏原四表工作流（配料分析→标签核对→产线评估→控制汇总）
  type: framework
  source_chapter: 附录 2（Forms 2-E 至 2-H）
  source_quote: |
    "Form 2-E: ... Use for conducting an allergen-specific hazard analysis of food ingredients.
    Form 2-F: ... Use to list the specific allergens to be listed in the "Contains" declaration on
    the product label. Form 2-G: ... Use to identify common and unique food allergens for
    products produced on a production line for the purpose of making decisions on scheduling
    (e.g., run unique allergens last) ... Form 2-H: ... Use to describe any food allergen controls
    and associated preventive control management components."
  summary: |
    过敏原控制被拆成四个有依赖顺序的表单：2-E 逐原料分析含哪些过敏原（含"May Contain"
    声明）→ 2-F 由分析结果确定标签"Contains"声明 → 2-G 按产线盘点共同/独有过敏原，
    以此决定排产顺序（独有过敏原最后跑）和清洗策略 → 2-H 用与工艺控制表同构的格式
    汇总控制与管理组件。前一步的输出是后一步的输入，构成完整决策链。
    可迁移点：把一个复合控制问题拆成"底数盘点→对外声明→现场调度→控制落地"四段式流水线。
  tags: [framework, workflow, allergen, form-chain, scheduling]

- id: f6-15
  title: D/z 值比较耐热性方法
  type: framework
  source_chapter: 附录 3（D-value / z-value 定义）
  source_quote: |
    "A "z-value" is derived from the reciprocal of the slope of the best straight line and is equal
    to the increase in the number of degrees (from a given starting temperature) that results in a
    90 percent reduction in the D-value ... Therefore, D-values and z-values provide a means to
    compare the thermal resistance of different microorganisms, or different strains of the same
    microorganism, at one or more temperatures."
  summary: |
    D 值=指定温度下杀灭 90% 微生物所需时间（对数递减）；z 值=使 D 值缩短 10 倍所需的
    温度增量。两者合起来把"这个菌多耐热"变成两个可比较、可换算的数。
    推理方法：知道目标菌的 D/z 后，可在任意温度间换算等效致死时间（ lethal rate 概念），
    从参考点（如 70°C/2 分钟杀李斯特菌）推导出全温度谱的 6D 工艺参数。
    可迁移点：把难以直接测量的属性（耐热性）参数化为两个系数，即可外推到未测条件。
  tags: [method, thermal-resistance, d-value, z-value, extrapolation]

- id: f6-16
  title: 6D 工艺查表法及其放宽/收紧边界
  type: framework
  source_chapter: 附录 3（Table 3-D / 3-E）
  source_quote: |
    "The length of time at a particular internal product temperature needed to accomplish a 6D
    reduction ... depends, in part, upon the food that is being heated. The values in the table
    are generally conservative and apply to all foods. You may be able to establish a shorter
    process time for your food by conducting scientific thermal death time studies. Additionally,
    lower degrees of destruction may be acceptable in your food if supported by a scientific
    study of the normal initial levels in the food."
  summary: |
    查表法：李斯特菌 6D=70°C/2 分钟（Table 3-D），非蛋白分解肉毒梭菌 6D=90°C/10 分钟
    （Table 3-E），中间温度按 lethal rate 换算。表值"一般保守、适用于所有食品"。
    但 FDA 同时给出双向边界：可放宽——用热致死时间研究证明本食品可缩短时间，或用
    初始菌落数研究证明更低还原度可接受；可收紧——预期初始负荷高时需更高还原度。
    可迁移点：默认参数=安全上界，个体化调整必须以本地数据为代价换取。
  tags: [method, 6d-process, lookup-table, validation, conservative-default]

- id: f6-17
  title: 生长极限表是极端值不是设计值（矩阵效应与禁插值警告）
  type: framework
  source_chapter: 附录 3（Table 3-A / 3-B / 3-C 使用说明）
  source_quote: |
    "The data shown in Table 3-A are the extreme limits reported among the references cited.
    These values may not apply to your food or processing conditions. ... Because the nature of
    bacterial growth is logarithmic, linear interpolation using the time and temperature guidance
    may not be appropriate. Furthermore, the food matrix affects bacterial growth (e.g., presence
    of competing microorganisms, available nutrients, growth-restrictive agents)."
  summary: |
    Table 3-A（a_w/pH/温度生长极限）、3-B（各温度段最大累积暴露时间）、3-C（速查版）
    提供的是文献报道的极端值，FDA 两处降级警告：①极端值未必适用于你的食品和工艺
    条件；②细菌生长是对数的，时间/温度数据之间不能线性插值；③食品基质（竞争菌群、
    营养、抑制剂）会改变生长行为。
    可迁移点：使用任何"极限值速查表"时的三条纪律——当它是边界参考而非设计依据、
    不在数据点之间插值、考虑载体本身的修正效应。
  tags: [method, growth-limits, lookup-table, interpolation-warning, matrix-effect]

- id: f6-18
  title: 预测模型须验证原则（模型输出是假设不是结论）
  type: framework
  source_chapter: 附录 3（PMP / ComBase 使用说明）
  source_quote: |
    "FDA does not endorse or require the use of such modeling programs, but recognizes that the
    predictive growth information they provide may be helpful to some processors. However, you
    should be aware that significant deviations between actual microbiological data in specific
    products and the predictions may occur, including those for the lag phase of growth.
    Therefore, you should validate the time and temperature limits derived from such predictive
    models if growth of pathogens during processing requires a preventive control."
  summary: |
    PMP 和 ComBase 等预测微生物学程序可按 pH/温度/盐浓度输出生长曲线、迟滞期、倍增
    时间，FDA 不背书也不禁止使用。但明确警告：模型预测与真实产品中的实测数据可能
    显著偏离——尤其是迟滞期。因此，若预测出的时间/温度限值要用作预防控制的关键限值，
    必须先用本产品实测数据验证。
    可迁移点：模型是生成假设的工具，不是产生结论的工具——凡进入受控参数的模型输出，
    必须经实际系统验证，迟滞期这类对初始条件敏感的量尤其如此。
  tags: [method, predictive-modeling, validation, model-risk, lag-phase]
```

## 自检

- [x] 每条均有原文摘录依据（行号区间见 summary/quote 对应关系）
- [x] 引用均为原文逐字摘录且 ≤100 英文词
- [x] 每条至少 1 个 tag
- [x] 未做筛选（f6-02 术语设计、f6-10 保守列名属边界候选，交阶段 1.5 验证）
- [x] "是否反复出现"判断仅基于本段：f6-05（水合条件化）在本段 5+ 张表脚注中反复出现；f6-06（极强致死）在 A1.6.1.3 及 5 张表脚注反复出现；f6-07 在 A1.6.1.1 与 A1.6.1.2.2 两处出现；其余多为单点结构
