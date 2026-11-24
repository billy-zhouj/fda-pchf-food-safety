# 阶段 1 · 原则提取候选 · 第 6 块（第 16501–19461 行）
# 覆盖：附录 1（危害表注释 A1.1–A1.8 + 生物危害表 1A–1P + 化学危害表 2A–2P）、附录 2（FSPCA 表单 2-A 至 2-I）、附录 3（病原生长与灭活数据 + 参考文献）
# 说明：按角色要求"宁错杀"不做筛选；本段内"是否反复出现"仅基于本段判断

- id: p6-01
  title: X 标记只是建议评估的起点，判定责任在每个工厂
  type: principle
  source_chapter: 附录 1 · A1.8.3 / A1.10 表头
  source_quote: |
    "Tables 1A through 1P do not identify any hazards requiring a preventive control in any Food
    Subcategory. It is the responsibility of the owner, operator, or agent in charge of each food
    facility to determine, through hazard analysis, whether a biological hazard identified in
    Tables 1A through 1P ... is a hazard requiring a preventive control."
  summary: |
    附录 1 的 16 组危害表（1A–1P、2B–2P）中每个 X 标记都不是"需要控制"的判定，
    而只是 SME（主题专家）建议进入后续危害评估的"潜在危害"。
    表格明确声明：任何表中都不标识任何"需要预防控制的危害"；
    是否需要控制由每个设施的所有者/经营者通过自己的危害分析决定。
    该规则在 A1.5.2、A1.8.1、A1.8.3、A1.10 表头、A1.11 表头重复出现至少 5 次，
    是附录 1 使用的第一原则："照表抄控制"会过度控制，"不看表"可能漏识别。
    判定责任不可外包给表格、顾问或供应商。
  tags: [principle, hazard-analysis, appendix1, responsibility, x-marks]

- id: p6-02
  title: 危害分析的三层漏斗：全部危害 → 潜在危害 → 需预防控制的危害
  type: principle
  source_chapter: 附录 1 · A1.3 / A1.8.1
  source_quote: |
    "Part 117 defines and uses three terms (i.e., 'hazard,' 'known or reasonably foreseeable
    hazard,' and 'hazard requiring a preventive control') to establish a tiered approach to the
    requirements for hazard analysis and risk-based preventive controls."
  summary: |
    21 CFR 117 用三个术语建立分层方法：先从"与食品安全相关的全部危害"出发，
    通过危害识别缩小到"已知或合理可预见的危害（潜在危害）"——即与本设施/食品相关的危害；
    再通过危害评估确定其子集"需要预防控制的危害"——知情者基于严重性×概率会建立
    一个或多个预防控制及其管理组件的危害。
    本段（A1.3 与 A1.8.1）两次完整重述该三层漏斗，是全书危害分析方法的法规骨架。
    使用附录 1 的任何表格前必须先理解：表格只覆盖中间层。
  tags: [principle, hazard-analysis, tiered-approach, appendix1, regulation]

- id: p6-03
  title: 控制 Salmonella/致病性 E. coli 即同时控制 Shigella，故表格不再单列
  type: principle
  source_chapter: 附录 1 · A1.6.1.2.2
  source_quote: |
    "If you identify Salmonella and/or pathogenic E. coli as a hazard requiring a preventive
    control, a preventive control that you establish and implement to significantly minimize or
    prevent Salmonella or pathogenic E. coli generally would also significantly minimize or
    prevent Shigella spp. Therefore, we decided that it was not necessary to separately identify
    Shigella spp."
  summary: |
    附录 1 选择了 12 种与美国食源性疾病相关的主要病原，随后又把 Shigella 从表中删除。
    逻辑：Shigella 与 Salmonella/致病性 E. coli 的污染来源（粪便/操作人员卫生）与控制手段
    高度重合——针对后者建立的预防控制通常同样显著减小或预防 Shigella。
    推论规则：如果某危害的控制在技术上必然覆盖另一危害，则后者无需独立判定条目。
    该"控制覆盖即豁免单列"的思路可用于企业自查是否遗漏次要病原。
    病毒与寄生虫同理：多数由 CGMP（117.10 人员卫生）与 part 112 农产品法规处理。
  tags: [principle, pathogen-logic, shigella, appendix1, control-coverage]

- id: p6-04
  title: Cronobacter 不列表，但用于婴儿配方粉的奶粉必须考虑
  type: principle
  source_chapter: 附录 1 · A1.6.1.1 / Table 1E 脚注 4
  source_quote: |
    "Tables 1A through 1P do not include ... Cronobacter spp. (including C. sakazakii) because
    Cronobacter spp. ... is largely a hazard for powdered infant formula rather than a hazard
    applicable to foods for the general population. ... Table 1E ... notes that the SMEs recommend
    considering Cronobacter spp. ... in powdered milk intended for use in infant formula."
  summary: |
    表格选择"对普通人群食品相关"的病原：Cronobacter 主要危害对象是粉末婴儿配方粉，
    故不作为通用潜在危害列出——但这是排除而非否定。
    规则：当奶粉（dry milk products） destined 用于干混婴儿配方粉时，必须把
    Cronobacter（含 C. sakazakii）作为潜在生物危害考虑。
    本段两次出现（A1.6.1.1 正文 + Table 1E 脚注 4），强调婴儿配方粉供应链的特殊性。
    适用边界：表格的"适用性检验"之一——危害是否取决于产品的下游用途。
  tags: [principle, cronobacter, infant-formula, appendix1, end-use-dependence]

- id: p6-05
  title: 粉末婴儿配方粉的 Cronobacter/Salmonella 强制微生物标准（21 CFR 106.55(e)）
  type: principle
  source_chapter: 附录 1 · A1.6.1.5
  source_quote: |
    "the controls to prevent adulteration from microorganisms in our infant formula regulations
    in 21 CFR part 106 specify criteria for when a powdered infant formula that contains
    Cronobacter spp. or Salmonella spp. will be deemed adulterated under sections 402(a)(1),
    402(a)(4), and 412(a)(3) of the FD&C Act. You must comply with these microbiological criteria."
  summary: |
    唯一一条"必须（must）"级别的硬性微生物标准：生产/加工粉末婴儿配方粉时，
    必须遵守 21 CFR 106.55(e) 的微生物标准——含 Cronobacter 或 Salmonella 的粉末
    婴儿配方粉将依据 FD&C Act 402(a)(1)、402(a)(4)、412(a)(3) 被认定为掺假。
    与附录其他"建议（recommend）"形成鲜明对比。
    提醒婴儿食品供应链：附录 1 表格不列婴儿配方粉，但法规另有专门强制要求，
    不可因表格空白而误判无要求。
  tags: [rule, infant-formula, cronobacter, salmonella, mandatory, 21-cfr-106]

- id: p6-06
  title: 极强致死工艺可使潜在危害"无需控制"（焦糖 116°C、饼干 250°C 等实例）
  type: principle
  source_chapter: 附录 1 · A1.6.1.3 / A1.8.3 脚注 24
  source_quote: |
    "A process of making caramel by boiling ingredients such as sugar, butter, and sweetened
    condensed milk for several minutes to about 240 [o]F (116 [o]C) would provide exceptional
    lethality for biological hazards (e.g., Listeria monocytogenes); without boiling for several
    minutes, the ingredients will not result in a chewy caramel when cooled."
  summary: |
    某些食品只能用"极强致死工艺"生产：若工艺不能充分控制生物危害，产品根本无法
    合格分销（产品质地/稠度与致死性绑定）。实例：焦糖煮沸数分钟至约 240°F/116°C、
    果酱/果冻/酸辣酱的煮沸、货架期稳定酸性果什锦、肉汁的熬煮浓缩、咸饼干
    482°F/250°C 烘烤 4.5 分钟。对这类产品 SME 未标识任何潜在危害（糖制糖果、
    果酱、苏打饼干），或在其他产品（汤/酱/肉汁）中可判定"不需要预防控制"。
    规则：工艺本身的产品属性要求即可作为危害结论"No"的科学依据。
  tags: [principle, exceptional-lethality, process-control, appendix1, numerical]

- id: p6-07
  title: 干配料水合后（a_w 允许生长）才考虑芽孢菌危害
  type: principle
  source_chapter: 附录 1 · A1.5.4 / Table 1J 脚注 1
  source_quote: |
    "The SMEs identified this as a known or reasonably foreseeable ('potential') biological hazard
    applicable only when the food becomes hydrated to an aw that allows growth or is used as an
    ingredient in another product where the grains/pulse/flour/starch become hydrated to an aw
    that allows growth."
  summary: |
    干谷物/面粉/淀粉/豆类/香料/干汤料中的 B. cereus、C. perfringens 等芽孢菌，
    仅在产品被水合到 a_w 允许生长、或作为配料进入水合产品时才成为潜在危害；
    分发干品给消费者或制造消费者自行烹煮的干混料时不考虑。
    本规则以"水合前提"形式在 Table 1J 脚注 1、1N 脚注 1、1O 脚注 1、1F 脚注 2、
    1H 脚注 8、1E 脚注 5 反复出现 6+ 次，是附录 1 最高频的适用性限定。
    推论：接收干配料时，其下游用途决定芽孢菌是否进入危害分析。
  tags: [principle, sporeformers, hydration, water-activity, appendix1, repeated]

- id: p6-08
  title: 过敏原、辐射、二噁英、未批准添加剂不在化学危害表中——须用第 3 章自行评估
  type: principle
  source_chapter: 附录 1 · A1.6.2.2–A1.6.2.4
  source_quote: |
    "a food allergen hazard could be identified as a known or reasonably foreseeable ('potential')
    chemical hazard for a majority of food products. Rather than identifying food allergen hazards
    ... for most food subcategories, the Tables of food-related chemical hazards do not address
    food allergen hazards."
  summary: |
    化学危害表刻意排除五类：食物过敏原（9 大过敏原 + 芝麻，2023-01-01 生效）、
    不耐受物质（亚硫酸盐 <10 ppm 且无技术效应才算 incidental）、辐射危害（主要来源：
    特定地区井水中的镭-226/228 与铀、核设施事故）、二噁英/PCB、未批准食品/色素添加剂
    （如香豆素、黄樟素、FD&C Red No. 4）。理由：过敏原对多数食品都潜在（列了等于
    全列）、辐射/二噁英罕见且多为事故性。
    规则：使用化学危害表后必须另用第 3 章信息补查这五类——表格空白≠无危害。
  tags: [principle, allergen, radiological, unapproved-additives, appendix1, gap-list]

- id: p6-09
  title: 多组分食品按"单个原料危害 + 工艺危害"评估
  type: principle
  source_chapter: 附录 1 · A1.5.4
  source_quote: |
    "To assess the biological and chemical hazards for these multi-component foods, you should
    consider the hazards associated with the individual raw materials/ingredients, as well as the
    hazards that may arise from the processing methods used in making them."
  summary: |
    多组分食品（主菜、三明治、配菜等）无法逐一进表，因为配料与工艺组合无穷。
    规则：对其危害评估 = 每种原料/配料的危害（查对应原料组表）+ 制造工艺带来的危害。
    同一原料的危害还取决于用途：全谷物做熟制高水分食品要考虑 B. cereus，
    干分销或做干混则不用；香料进高水分蘸酱/冷冻餐要考虑芽孢菌，做干香料混合物则不用。
    与 p6-07 配合使用：原料表 + 用途 + 工艺三者共同决定危害集。
  tags: [principle, multi-component, ingredient-based, appendix1]

- id: p6-10
  title: 工艺相关与设施相关危害不在附录 1 中，须每厂基于自身历史识别
  type: principle
  source_chapter: 附录 1 · A1.7（2016 修订版删除第三组表）
  source_quote: |
    "This revised Appendix 1 no longer includes a table of ... process-related biological, chemical,
    and physical hazards, because process-related hazards generally are unique to each facility
    based on its operations and processes. Instead, section A1.7 recommends that each facility
    identify ... process related hazards for its products based on its knowledge, experience, and
    history of hazards associated with its operations."
  summary: |
    2016 初稿曾有第三组表（工艺相关危害表），修订版删除：工艺/设施相关危害因厂而异，
    无法通用列表。规则：每个设施须基于自身的知识、经验与危害历史，用第 2 章方法
    + 第 3 章信息自行识别工艺相关（致死步骤失控、时间温度失控、配方失当、ROP、
    工艺后加料、容器完整性）与设施相关危害（环境病原再污染、交叉接触）。
    A1.7.1–A1.7.3 提供最相关的清单作起点（如刀片碎裂引金属、玻璃包装碎裂引玻璃、
    塑料工具疲劳碎裂引硬塑料）。
  tags: [principle, process-hazards, facility-hazards, self-identification, appendix1]

- id: p6-11
  title: "No"结论与"Yes"同等重要；争议大时保守列入并解释 No
  type: principle
  source_chapter: 附录 1 · A1.8.2 末段
  source_quote: |
    "you may find it useful to take a conservative approach by listing in Column 2 several known
    or reasonably foreseeable ('potential') hazards even though they clearly do not require a
    preventive control ... and explain the reasons for your 'No' conclusion. This can be useful
    both during your own review ... and during review ... by others – e.g., if an inspector or
    auditor questions whether a particular hazard was considered."
  summary: |
    X 标记的危害可能只适用于子类别中部分产品、特定产地或特定用途。
    判定"Yes/No"时，解释"No"的理由与解释"Yes"同等重要。
    保守做法：即使明显不需要控制，也把有争议的潜在危害列入危害分析表第 2 列，
    并在第 4 列写明"No"理由——这在自查、检查员或审核员质疑时提供即答证据。
    该规则呼应全书第 2 章"书面理由是对抗检查质疑的防线"的立场。
  tags: [principle, hazard-evaluation, no-justification, documentation, appendix1]

- id: p6-12
  title: 蜂蜜的 C. botulinum 仅当用作婴儿食品配料时才考虑
  type: principle
  source_chapter: 附录 1 · Table 1P 脚注 1
  source_quote: |
    "The SMEs identified this as a known or reasonably foreseeable ('potential') biological hazard
    applicable only if honey is used as an ingredient in infant foods."
  summary: |
    液体蜂蜜在表 1P 中几乎所有病原列为空白，唯独 C. botulinum 打 X，且附严格限定：
    仅当蜂蜜用作婴儿食品的配料时才是潜在危害。
    原理：婴儿肠道菌群尚未建立，肉毒梭菌芽孢可在婴儿肠道定植产毒；
    成人食用含芽孢蜂蜜不构成危害。
    与 p6-07（干配料水合才考虑芽孢菌）并列，是"用途决定危害"的第二个典型实例。
  tags: [principle, honey, botulinum, infant-food, end-use-dependence, appendix1]

- id: p6-13
  title: 控制最常见病原即覆盖少见病原（生可可豆只列 Salmonella）
  type: principle
  source_chapter: 附录 1 · A1.6.1.1
  source_quote: |
    "the most common ... biological hazard for raw cocoa beans is Salmonella. Processing to
    control Salmonella would also control less common ... biological hazards for raw cocoa beans
    (such as L. monocytogenes and pathogenic E. coli). Therefore, Table 1D only identifies
    Salmonella as a ... potential biological hazard for raw cocoa beans."
  summary: |
    原料常同时携带多种潜在生物危害；在许多情况下，针对该子类别最常见病原的加工
    控制也会控制较少见的病原。故表格只为生可可豆标 Salmonella，不标
    L. monocytogenes 与致病性 E. coli。
    规则：识别危害时先找"主病原"，验证主病原控制措施是否在技术上同时覆盖次要
    病原，可避免重复设计控制（与 p6-03 的 Shigella 逻辑同源）。
  tags: [principle, pathogen-logic, control-coverage, cocoa, appendix1]

- id: p6-14
  title: 霉菌毒素与商品的固定对应关系（查表速查）
  type: principle
  source_chapter: 附录 1 · A1.6.2.6 / Table 2B/2D/2H/2J/2K/2L/2O 脚注
  source_quote: |
    "Specific mycotoxins are most commonly associated with certain commodities as follows:
    aflatoxin: peanuts, dried corn, tree nuts, and some edible seeds ...; ochratoxin: cocoa, coffee,
    raisins, dried figs, cereal grains; fumonisins: dried corn; deoxynivalenol (vomitoxin): wheat,
    barley; and patulin: apples."
  summary: |
    霉菌毒素按商品归类速查：黄曲霉毒素→花生/干玉米/树坚果/部分食用种子；
    赭曲霉毒素→可可/咖啡/葡萄干/无花果干/谷物；伏马毒素→干玉米；
    脱氧雪腐镰刀菌烯醇（DON/呕吐毒素）→小麦/大麦；棒曲霉素→苹果。
    毒元素四重金属性质：砷、镉、铅、汞（汞主要是海产，本指南不覆盖）。
    规则：化学危害表中"mycotoxin"打 X 时，脚注指明适用的是哪一种——
    直接按原料-毒素对应表锁定供应链验证对象。
  tags: [checklist, mycotoxins, commodities, appendix1, supply-chain, quick-reference]

- id: p6-15
  title: LACF 食品：生物危害豁免 PCHF，化学/物理危害仍适用
  type: principle
  source_chapter: 附录 1 · A1.5.5
  source_quote: |
    "The PCHF requirements do not apply with respect to activities that are subject to the LACF
    regulations (21 CFR part 113) for the control of biological hazards ... C. botulinum would be
    the biological hazard associated with an LACF used as an ingredient; the hazard would be
    controlled by the supplier. The PCHF requirements do apply to chemical and physical hazards
    that could be associated with an LACF food."
  summary: |
    受 21 CFR part 113（低酸罐装食品）管辖的生物危害控制活动不适用 PCHF，
    故 Tables 1A–1P 不覆盖 LACF 食品——用作配料时 C. botulinum 危害由供应商控制。
    但化学与物理危害的 PCHF 要求仍适用：罐装蔬菜的化学危害查表 2H（果蔬组）。
    本段多个表格脚注（1B 脚注 3、1E 脚注 3/7、1F 脚注 1、1H 脚注 3、1J 脚注 4、
    1M 脚注 5）反复重申"排除 LACF 产品"。
    规则：货架期稳定产品先判 LACF 归属，再决定生物危害是否进入危害分析。
  tags: [principle, LACF, jurisdiction-split, appendix1, repeated]

- id: p6-16
  title: USDA FSIS 管辖产品作配料时仍须做自己的危害分析
  type: principle
  source_chapter: 附录 1 · A1.6.1.4
  source_quote: |
    "If you use a food product that is produced under the jurisdiction of USDA's FSIS as an
    ingredient in your food product, you should determine, through your hazard analysis, whether
    a hazard you identify as a ... potential biological hazard in that ingredient is a hazard
    requiring a preventive control."
  summary: |
    附录 1 的 16 组食品均不针对 FSIS 单独管辖的产品（某些肉类、禽类、加工蛋制品如
    巴氏杀菌液态全蛋）。但这些 FSIS 管辖产品常被用作受 FD&C Act/part 117 管辖食品的
    配料（如蛋饼用于早餐三明治）。
    规则：供应商已被 USDA 检查不能替代收货方的危害分析——仍须判定配料中的潜在
    生物危害是否为需要预防控制的危害。
    另：2020-10-29 FSIS 最终规则（2023-10-30 生效）将蛋替代品与冻干产品纳入 FSIS
    检查，"蛋与蛋制品"组不再包含这两类。
  tags: [principle, USDA-FSIS, ingredient, hazard-analysis, appendix1]

- id: p6-17
  title: 供应商已巴氏杀菌/处理的配料危害仍须进入分析（表格列出与控制方无关）
  type: principle
  source_chapter: 附录 1 · A1.6.1.6
  source_quote: |
    "Tables 1A through 1P list the ... potential biological hazards that could be in a food product
    due to the ingredients in the food product regardless of whether the outcome of the hazard
    analysis is that a hazard that requires a preventive control is controlled by you (e.g., by a
    process control) or by your supplier."
  summary: |
    许多配料危害（如乳基配料、蛋基配料）由供应商的巴氏杀菌或其他处理控制。
    表格列出的是"可能存在于食品中的潜在危害"——无论最终由你（工艺控制）还是
    由供应商（供应链控制）控制，都先列出来。
    规则：表格与控制主体解耦；控制主体（自控 vs 供应链控制）是危害分析输出端的
    决策，不是识别端的筛选条件。
    类似地：消费者烹煮（如未烤水果派）也可作为"No"的理由（A1.6.1.7）。
  tags: [principle, supplier-control, pasteurization, appendix1, decoupling]

- id: p6-18
  title: 附录 1 非穷尽、仅反映 2022 年数据；特殊配料查供应商 TDS/FCC/GRAS
  type: principle
  source_chapter: 附录 1 · A1.4 / A1.5.4
  source_quote: |
    "Although Appendix 1 is comprehensive, it is not exhaustive and only reflects data and
    information available as of 2022. New information about hazards that could be associated with
    certain types of food products could become available in the future. In addition, Appendix 1
    does not address specialty ingredients such as seaweed ... proteins extracted from plants ..."
  summary: |
    附录 1 虽全面但不穷尽，只反映截至 2022 年的数据；新危害信息随时可能出现。
    明确不覆盖特殊配料：海藻（卡拉胶等海藻提取物除外）、植物提取蛋白（如豌豆蛋白）、
    微生物发酵蛋白（如酵母发酵蛋清蛋白）、微生物本身（双歧杆菌、乳杆菌）。
    评估这些配料的信息来源：供应商技术数据表、Food Chemicals Codex 标准、FDA 法规
    设定的规格、GRAS 通知回复；查不到时直接询问供应商。
    规则：表格不是危害识别的终点，是起点+底线。
  tags: [principle, non-exhaustive, specialty-ingredients, appendix1, supplier-TDS]

- id: p6-19
  title: 四个食品组无化学危害表，按所用配料查对应表
  type: principle
  source_chapter: 附录 1 · Food Group 2A/2F/2M/2N
  source_quote: |
    "This Appendix does not include a Table of ... food-related chemical hazards for Bakery Items.
    Instead, ... you should see the Table(s) associated with the ingredients in your Bakery Item.
    For example: - If your Bakery Item contains chocolate, you should consult Table 2D ..."
  summary: |
    焙烤食品（2A）、调味酱/佐料/蘸酱（2F）、零食（2M）、汤与酱（2N）四个食品组的
    化学危害取决于所用配料，故不设独立表格，只设指引条目：含巧克力查 2D、含蛋查 2G、
    含小麦粉查 2J、含水果/蔬菜查 2H、含花生/树坚果查 2K、含乳基查 2E。
    规则：化学危害识别以配料为轴而非以成品为轴（因化学危害多通过供应链程序而非
    工艺控制解决——A1.11 前言说明此设计理由）。
  tags: [principle, chemical-hazards, ingredient-based, appendix1, referral-tables]

- id: p6-20
  title: 含包材/夹杂物（inclusions）的产品须同时考虑夹杂物自身的危害
  type: principle
  source_chapter: 附录 1 · Table 1A 脚注 1（同类脚注见 1D/1E/1H/1J/1M）
  source_quote: |
    "If your food product includes an inclusion, your hazard analysis should also consider known
    or reasonably foreseeable ('potential') biological hazards associated with the inclusion (e.g.,
    hazards for nuts, chocolate chips, fruit). The other tables in section A1.10 are resources that
    could be applicable to the inclusion."
  summary: |
    产品含夹杂物（坚果、巧克力豆、果粒、糖霜/浇头）时，危害分析必须叠加夹杂物
    自身的危害——即使基料经极强致死工艺（如巧克力糖果）。例：巧克力涂层水果查
    涂层（巧克力）与被涂水果两表；含夹什物的巧克力糖果（3b/3d）无 X 标记是因为
    仅指基料，夹杂物须另查；谷物早餐含坚果/巧克力须另查对应表。
    该规则在表 1A、1D、1E、1H、1J、1M 脚注反复出现 6 次。
  tags: [principle, inclusions, cross-table-lookup, appendix1, repeated]

- id: p6-21
  title: FSP 无标准化/强制格式，但自定义格式必须涵盖全部法定要素
  type: principle
  source_chapter: 附录 2 · Introduction
  source_quote: |
    "There is no standardized or mandated format for documenting the food safety plan. ...
    Other formats are entirely acceptable if they work for your organization. If you use another
    format, you should ensure that your format provides all of the information that the preventive
    controls rule requires for each required component of the food safety plan. See 21 CFR
    117.126, 117.305, and 117.310."
  summary: |
    食品安全计划的文档格式无标准化、无强制要求；可不用 FSPCA 表单。
    两个使用 FSPCA 表单的理由：(1) FSPCA 培训使用这些表单；(2) 与 HACCP 计划
    及前提方案常用格式相似。
    硬性规则：任何自定义格式必须提供法规（21 CFR 117.126、117.305、117.310）要求的
    每个必需组件的全部信息——格式自由，内容不自由。
    一般建议：以递进方式组织信息，清楚展示危害分析的思考过程。
  tags: [principle, FSP-format, FSPCA-forms, appendix2, flexibility-with-rigor]

- id: p6-22
  title: 无论用何种格式，都应做过敏原配料分析并纳入 FSP
  type: principle
  source_chapter: 附录 2 · FSPCA Food Allergen Control Forms / Form 2-E
  source_quote: |
    "Regardless of whether you use these FSPCA Food Allergen forms, we recommend that you
    conduct a food allergen ingredient analysis and include information such as you see in Form
    2E in your food safety plan."
  summary: |
    过敏原控制的四张 FSPCA 表单各司其职：2-E 过敏原配料分析（逐原料列出配方中
    过敏原 + 预防性标签如"May Contain"中的过敏原）；2-F 标签核对清单（每个产品
    的"Contains"声明）；2-G 产线过敏原评估（识别产线共有/独有过敏原，支撑排产
    决策如"独有过敏原最后排产"与清洁决策）；2-H 过敏原控制表（控制步骤/危害/
    准则/监控四问/纠正/验证/记录）。
    规则：过敏原配料分析（2-E）是无条件建议——是后续标签与清洁决策的输入。
  tags: [principle, allergen, ingredient-analysis, appendix2, forms]

- id: p6-23
  title: 卫生控制通常用 correction 即可，但要预先列出触发 corrective action 的情形
  type: principle
  source_chapter: 附录 2 · Form 2-D 说明
  source_quote: |
    "Corrections (Corrective Actions Where Appropriate) - e.g., recleaning equipment that is not
    visibly clean prior to production. In most cases, corrections are appropriate. However, you
    may want to include circumstances that would trigger corrective actions."
  summary: |
    卫生控制表（Form 2-D）字段：位置、目的（去除过敏原/减少环境病原污染）、频率、
    执行人、程序（可引 SOP）、监控、纠正（corrections，多数情况适用，如投产前对
    不洁设备重新清洁）、记录、验证。
    规则：卫生控制的偏离多数走 correction 通道，但计划中应预先写明哪些情形升级为
    corrective action（如反复检出环境病原）。与第 5 章"correction vs corrective action"
    判定边界呼应：孤立且未影响产品→correction；反复或已影响→corrective action。
  tags: [principle, sanitation-control, correction-vs-corrective-action, appendix2]

- id: p6-24
  title: Table 3-A 生长极限是文献极端值，未必适用于你的食品
  type: principle
  source_chapter: 附录 3 · Table 3-A 引言
  source_quote: |
    "The data shown in Table 3-A are the extreme limits reported among the references cited.
    These values may not apply to your food or processing conditions. ... the food matrix affects
    bacterial growth (e.g., presence of competing microorganisms, available nutrients,
    growth-restrictive agents)."
  summary: |
    表 3-A 汇总各病原生长的极限 a_w、pH、温度与最大水相盐浓度——全部取自所引
    文献中报告的"极端值"，FDA 明确警告：未必适用于你的食品或加工条件。
    细菌生长还受食品基质影响（竞争菌群、可用营养物、抑菌剂）。
    规则：不得把 Table 3-A 极端值直接当作配方/工艺设计依据当"安全边界"；
    使用时应作为筛选与方向性判断工具，关键限值需用自身产品的科学研究支撑。
    与全书批判段落"使用者常直接当设计依据"的隐患对应。
  tags: [principle, growth-limits, literature-extremes, appendix3, caution]

- id: p6-25
  title: Table 3-A 数值界限速查（L. mono -0.4°C 仍可生长、S. aureus a_w 0.83 等）
  type: principle
  source_chapter: 附录 3 · Table 3-A
  source_quote: |
    "Listeria monocytogenes | 0.92 | 4.4 | 9.4 | 10 | 31.3°F -0.4°C | 113°F 45°C |
    Staphylococcus aureus growth | 0.83 | 4 | 10 | 20 | 44.6°F 7°C | 122°F 50°C |
    Clostridium botulinum, type E, and non-proteolytic types B and F | 0.97 | 5 | 9 | 5 | 37.9°F 3.3°C | 113°F 45°C"
  summary: |
    关键数值界限：L. monocytogenes 最低生长温度 -0.4°C（冷藏下仍生长）、a_w≥0.92、
    pH 4.4–9.4、最高 45°C；S. aureus 生长 a_w≥0.83（产毒 ≥0.85）、最高耐 20% 水相盐；
    非蛋白分解 C. botulinum 最低 3.3°C（可在冷藏生长）、a_w≥0.97；蛋白分解型
    最低 10°C；B. cereus a_w≥0.92、pH 4.3–9.3；Salmonella 最低 5.2°C、pH≥3.7；
    Yersinia enterocolitica 最低 -1.3°C。用途：判断配方（a_w/pH/盐）能否抑制某病原、
    判断冷藏/冷冻温度是否构成生长屏障。
  tags: [principle, numerical, growth-limits, table-3a, appendix3, quick-reference]

- id: p6-26
  title: 6D 工艺查表：L. mono 70°C 2 分钟；非蛋白分解 C. botulinum 90°C 10 分钟
  type: principle
  source_chapter: 附录 3 · Table 3-D / Table 3-E
  source_quote: |
    "The times provided are the length of time at the designated internal product temperature
    necessary to deliver a '6D' process for L. monocytogenes (i.e., a process that will accomplish
    a 6 logarithm (factor of 1,000,000) reduction ...) ... 158°F (70°C) | 1.000 | 2.0 [minutes]"
    "Table 3-E ... 194°F (90°C) | 1.000 | 10.0 [minutes] — Inactivation of Non-Proteolytic Clostridium botulinum Type B"
  summary: |
    L. mono 6D（百万倍减少）：内部温度 70°C 保持 2.0 分钟为基准（z=13.5°F/7.5°C）；
    63°C 需 17.0 分钟，80°C 仅 0.09 分钟，85°C 0.02 分钟。非蛋白分解 C. botulinum
    B 型 6D：90°C 保持 10.0 分钟为基准（<90°C 时 z=7.0°C，>90°C 时 z=10°C）；
    85°C 需 51.8 分钟，100°C 仅 1.0 分钟。
    表值为保守值、适用所有食品；可通过热致死时间研究缩短，或依据初始水平研究
    采用更低/更高杀灭度。
    这是热处理工艺控制设计验证的速查锚点。
  tags: [principle, numerical, 6D, lethality, table-3d-3e, appendix3, thermal-process]

- id: p6-27
  title: 细菌生长是对数的：时间-温度数据线性内插不可靠
  type: principle
  source_chapter: 附录 3 · Table 3-C 引言
  source_quote: |
    "Because the nature of bacterial growth is logarithmic, linear interpolation using the time
    and temperature guidance may not be appropriate. Furthermore, the food matrix affects
    bacterial growth (e.g., presence of competing microorganisms, available nutrients,
    growth-restrictive agents). You should consider such attributes when using the information
    in Tables 3-A, 3-B, and 3-C."
  summary: |
    使用 Table 3-A/3-B/3-C 的两条禁令：(1) 禁止线性内插——细菌生长是对数的，
    在温度档位之间按比例折算暴露时间可能严重高估安全裕度；
    (2) 食品基质改变生长动力学（竞争菌群、营养物、抑菌剂），表格数值不能脱离
    基质直接套用。
    规则：落在两个温度档之间时，取更严档位的限值或做产品特异性研究，不做折算。
  tags: [principle, interpolation, logarithmic-growth, time-temperature, appendix3, caution]

- id: p6-28
  title: 预测模型（PMP/ComBase）不背书、须验证后才能用作关键限值依据
  type: principle
  source_chapter: 附录 3 · Table 3-C 后讨论
  source_quote: |
    "FDA does not endorse or require the use of such modeling programs ... you should be aware
    that significant deviations between actual microbiological data in specific products and the
    predictions may occur, including those for the lag phase of growth. Therefore, you should
    validate the time and temperature limits derived from such predictive models if growth of
    pathogens during processing requires a preventive control."
  summary: |
    USDA PMP 与 ComBase/Predictor 可按 pH/温度/盐浓度给出预测生长曲线
    （倍增时间、迟滞期、世代时间）。FDA 不背书也不强制使用，且明确警告：
    特定产品实测数据与预测之间可出现显著偏差，迟滞期尤其如此。
    规则：若加工过程中病原生长需要预防控制，则由预测模型导出的时间/温度限值
    必须经过验证（validation）——模型输出是假设，不是关键限值。
  tags: [principle, predictive-models, validation, appendix3, caution]

- id: p6-29
  title: Table 3-B/3-C 时间-温度累计暴露限（生/熟 RTE 分档）
  type: principle
  source_chapter: 附录 3 · Table 3-B / Table 3-C
  source_quote: |
    "Raw, RTE ingredient or food product | Above 70°F (21.1°C) | 4 hours ...
    Cooked, RTE ingredient or food product | At any time above 80°F (26.7°C) | 1 hour ...
    Cooked, RTE ... | At any time above 50°F (10°C) but never above 70°F (21.1°C) | 5 hours"
  summary: |
    累计暴露时间上限（普通情况下安全）：生 RTE 在 >70°F/21.1°C 累计 4 小时
    （60-70°F 为 6 小时）；熟 RTE 在 >80°F/26.7°C 累计 1 小时（S. aureus 为唯一
    关注病原时 3 小时）、21.1–26.7°C 之间 2 小时、10–21.1°C 之间 5 小时
    （S. aureus 12 小时）；全程 ≤10°C 无限制。
    B. cereus >21°C 限 3 小时；蛋白分解 C. botulinum >21°C 限 2 小时；
    C. perfringens >21°C 限 12 小时；L. mono >30°C 限 1 小时。
    累计=多次暴露求和，非单次。
  tags: [principle, numerical, time-temperature, cumulative-exposure, table-3c, appendix3]

- id: p6-30
  title: 4.4–10°C 区间无推荐限值的理由与例外（接近 Table 3-B 极限须自立关键限值）
  type: principle
  source_chapter: 附录 3 · Table 3-C 注
  source_quote: |
    "the preceding recommended critical limits do not address internal product temperatures
    between 40°F (4.4°C), which is the recommended maximum storage temperature for
    refrigerated food products, and 50°F (10°C). ... if you have processing steps that occur at
    these temperatures that approach the maximum cumulative exposure times listed in Table 3-B
    ... you should consider development of a critical limit for control at these temperatures."
  summary: |
    Table 3-C 的关键限值不覆盖 4.4–10°C 区间，因为此温度段病原生长极慢、显著生长
    所需时间超过多数加工步骤的合理时长；40°F/4.4°C 是冷藏食品推荐最高储存温度。
    例外规则：若加工步骤在此温度段停留时间接近 Table 3-B 中相应病原的最大累计
    暴露时间，则应为该温度段建立专门关键限值。
    规则结构："通用豁免 + 触发条件即收回豁免"。
  tags: [principle, refrigeration, critical-limit, conditional, appendix3, numerical]

- id: p6-31
  title: 非蛋白分解 C. botulinum 可在冷藏温度生长——长期冷藏食品的强制考量
  type: principle
  source_chapter: 附录 3 · Table 3-E 引言
  source_quote: |
    "(The non-proteolytic strains of C. botulinum can grow at refrigeration temperatures and may
    be a hazard requiring a preventive control in some foods intended to be held refrigerated for
    extended periods of time.)"
  summary: |
    表 3-E 针对非蛋白分解 C. botulinum B 型（最耐热的非蛋白分解型）：最低生长温度
    3.3°C，意味着冷藏本身不构成其对长货架期冷藏食品的屏障。
    规则：拟长期冷藏保存的食品（如 sous-vide、冷藏即食食品），若货架期足以让
    非蛋白分解型肉毒梭菌萌发生长，则该危害可能需要预防控制（如 90°C/10 分钟
    级别的 6D 热处理或其他屏障组合）。
    与 ROP 章节"可能先产毒后腐败"的警示同源。
  tags: [principle, botulinum, refrigerated-shelf-stable, table-3e, appendix3]

- id: p6-32
  title: 6D 表值为保守通值——可用热致死时间研究缩短，按初始水平调整杀灭度
  type: principle
  source_chapter: 附录 3 · Table 3-D 引言
  source_quote: |
    "The values in the table are generally conservative and apply to all foods. You may be able to
    establish a shorter process time for your food by conducting scientific thermal death time
    studies. Additionally, lower degrees of destruction may be acceptable in your food if supported
    by a scientific study of the normal initial levels in the food. It is also possible that higher
    levels of destruction may be necessary in some foods, if you anticipate relatively high initial
    levels."
  summary: |
    表 3-D/3-E 的 6D 数值是"保守 + 适用所有食品"的通值。优化路径：
    (1) 对自己的食品做科学热致死时间研究可缩短工艺时间；
    (2) 若用科学研究证明食品中正常初始水平较低，可接受低于 6D 的杀灭度；
    (3) 若预期初始水平较高（如原料严重污染），则需要更高的杀灭度。
    规则：查表值是下限起点而非最优解；工艺设计的科学依据始终是自身产品的
    微生物数据，不是表本身。
  tags: [principle, 6D, thermal-death-time, validation, appendix3, optimization]

- id: p6-33
  title: 蜂蜜/糖浆等甜味剂几乎无生物危害，C. botulinum 例外仅限婴儿用途
  type: principle
  source_chapter: 附录 1 · Table 1P
  source_quote: |
    "Food Sweeteners ... Sugars (Dry) | Ambient | [no X in any pathogen column] ... Honey (Liquid) | Ambient | [X only in C. botulinum column, footnote:] applicable only if honey is used as an ingredient in infant foods."
  summary: |
    表 1P 显示全部甜味剂（干糖、糖浆/糖蜜、仿制糖浆、营养性与非营养性代糖）
    在 12 种病原列全为空白——糖的高渗透压/低 a_w 构成强屏障。
    唯一例外：液体蜂蜜的 C. botulinum（仅婴儿用途）。规则：甜味剂作为配料时，
    生物危害分析通常可为"No"，但进入婴儿食品供应链的蜂蜜必须按肉毒芽孢处理
    （供应商验证 + 用途声明）。
  tags: [principle, sweeteners, honey, aw-barrier, appendix1]

- id: p6-34
  title: 未酸化浸泡油（infused oils）才考虑 C. botulinum
  type: principle
  source_chapter: 附录 1 · Table 1L 脚注 1
  source_quote: |
    "The SMEs only identified C. botulinum as a known or reasonably foreseeable ('potential') hazard
    for oils infused with an ingredient that has not been acidified."
  summary: |
    油与油制品组（表 1L）几乎全空白——纯油不支持任何病原生长。
    唯一例外：浸泡油（蒜油、香草油等）在浸泡配料未酸化时须考虑 C. botulinum
    （厌氧油环境 + 配料带入芽孢与营养）。
    规则：油基产品的危害分析只看浸泡/混合进油中的非油成分及其酸化状态；
    酸化配料消除该危害。与风味膏（flavor paste，表 1C 需查 Salmonella/E. coli/L. mono）
    形成对照——水相含量决定危害集。
  tags: [principle, infused-oils, botulinum, acidification, appendix1]

- id: p6-35
  title: 婴幼儿食品毒元素无附录内行动水平，须持续跟踪 Closer to Zero 动态
  type: principle
  source_chapter: 附录 1 · A1.6.2.5
  source_quote: |
    "This guidance does not identify specific action levels for any toxic element hazards in foods
    for infants and toddlers. Instead, we identify action levels or other recommendations ... in
    more specific guidance such as Compliance Policy Guides ... and Guidance for Industry ...
    because the action plan's iterative approach can lead to adjustments in any announced action
    levels on an ongoing basis."
  summary: |
    附录 1 不给出婴幼儿食品毒元素的具体行动水平——这些水平散布于 CPG 与行业指南
    （发布时已覆盖：米糊砷、果汁砷、果汁铅、婴幼儿食品铅、儿童高频糖果铅），
    且 Closer to Zero 行动计划的迭代方式意味着任何已公布水平都可能持续调整。
    规则：婴幼儿食品生产者必须定期核查 FDA 网站（Closer to Zero 专页 + CPG/GFI
    列表）获取现行水平，不能把任何单一快照当作永久标准。
  tags: [principle, toxic-elements, closer-to-zero, infant-foods, dynamic-standards, appendix1]

- id: p6-36
  title: 危害表排除商品专属性之外的产地/来源依赖危害（毒元素与农药按产地触发）
  type: principle
  source_chapter: 附录 1 · A1.8.2
  source_quote: |
    "Only be a known or reasonably foreseeable ('potential') hazard when a food ingredient is
    sourced from a specific geographic location (e.g., for chemical hazards such as toxic elements
    and pesticides sourced from locations where there has been a history of such contamination) ..."
  summary: |
    X 标记危害可能只在三种情形下适用于具体产品：(1) 仅适用子类别中部分产品
    （如表 1O 只对部分香草标 Cyclospora；表 1C 仅对 HVP 标 Salmonella）；(2) 仅当
    配料来自特定地理位置（毒元素、农药污染史地区）；(3) 仅当配料被用于改变其
    特性的食品（如熟制水合米饭的 B. cereus）。
    配套规则：含水源食品来自毒元素污染地区时须考虑毒元素危害（如 Keurig Dr
    Pepper 案例、Import Alert 99-42）。
    三种检验构成附录 1 表格的"适用性过滤器"。
  tags: [principle, applicability-test, geographic-sourcing, appendix1, three-tests]

- id: p6-37
  title: 亚硫酸盐低于 10 ppm 且无技术效应才算 incidental（标签豁免界限）
  type: principle
  source_chapter: 附录 1 · A1.6.2.2
  source_quote: |
    "some sulfiting agents must be listed on the ingredient label unless they are added to food as
    an 'incidental substance'; sulfiting agents are considered to be incidental only if they have no
    technical effect in the finished food and are present at less than 10 parts per million (ppm)
    (21 CFR 101.100(a)(4))."
  summary: |
    亚硫酸盐类（不耐受物质代表）必须在配料标签上声明，除非作为"incidental substance"
    加入——而 incidental 的法定双重判据：对成品无技术效应 且 含量 <10 ppm
    （21 CFR 101.100(a)(4)）。
    规则：误配料（mis-formulation）是工艺相关化学危害——同时生产含/不含亚硫酸盐
    的产品时，无意把亚硫酸盐加进不含它的产品即构成危害（A1.7.2）。
    数值界限：10 ppm 是标签豁免与危害关注之间的分界线。
  tags: [rule, sulfites, labeling, 10-ppm, mis-formulation, appendix1]

- id: p6-38
  title: 婴儿配方粉/婴幼儿食品不在表中——须用更宽泛术语映射到对应子类别
  type: principle
  source_chapter: 附录 1 · A1.5.6
  source_quote: |
    "The Food Categories/Food Subcategories in the Tables in Appendix 1 do not specifically identify
    'baby food' ... When you manufacture/process a food intended for consumption by infants or
    toddlers, you should look for a broader term applicable to that food. For example, for 'baby
    food' that contains fruit, you could look at the Heat-Treated Fruit Products Subcategory ..."
  summary: |
    附录 1 不单列婴儿配方粉与婴幼儿食品（"baby food"如婴幼儿果蔬泥）。
    规则：生产婴幼儿食品时用更宽泛术语映射到对应子类别——含水果的婴儿食品查
    表 1H/2H 的热处理水果制品或其他水果子类别；含蔬菜查蔬菜相关子类别。
    映射只是识别起点，婴儿食品的敏感性要求额外考虑：Closer to Zero 毒元素动态
    标准（p6-35）、蜂蜜肉毒例外（p6-12/33）、婴儿配方粉 106.55(e) 强制标准（p6-05）。
  tags: [principle, baby-food, mapping, appendix1, infant-formula]
