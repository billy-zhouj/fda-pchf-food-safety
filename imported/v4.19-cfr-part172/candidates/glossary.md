# 候选池：术语提取器 | 来源 21 CFR Part 172 eCFR 2026-11-05 | 全量扫描 chunk-01..04
# 编号接续已装包末尾 t277，本池自 t278 起。
# 纪律：source_quote 逐字取自 source-cfr-part172-2026.md（归一化空白后可命中）；16 张重建表格数值、§172.510/§172.515 名录内部行、IBR 外部文件内容属不可逐字引用区，本池只引其「存在与边界」，不引其内部数值。
# 本件为法规正文层，术语为「判读用语」而非 21 CFR 117.3 式法定定义；summary 写清「法定判据 + 常见误读」。

- id: t278
  title: direct food additive（直接食品添加剂）
  type: term
  source_chapter: 21 CFR Part 172 标题 / Authority
  source_quote: |
    "Food Additives Permitted for Direct Addition to Food for Human Consumption"
  summary: "直接加入食品、在成品中保留技术效果的添加剂，许可与限量由 Part 172 管；法源为 FD&C Act §201(s) 定义与 §409。与间接添加剂（包装材料迁移，Part 175–178）不同、与本包未收的 GRAS/临时许可不同。常见误读是把「直接添加剂」当成「可食用配料」或把间接添加剂混进来判定。"
  tags: [总则, 许可四元组, 效力层]

- id: t279
  title: good manufacturing practice（本部分的口径）
  type: term
  source_chapter: § 172.5(a)
  source_quote: |
    "Regulations prescribing conditions under which food additive substances may be safely used predicate usage under conditions of good manufacturing practice."
  summary: "本部分的 cGMP 不是泛泛口号，§172.5(a) 把它定义为两条具体限制：用量不超过合理需要量、物质须为食品级。它叠加在每一条 §172.xxx 之上，即使条款给了 ppm 上限也仍然生效。常见误读是把 GMP 当「建议层」，以为无法律约束力。"
  tags: [总则, GMP, 兜底限制]

- id: t280
  title: amount reasonably required（合理需要量）
  type: term
  source_chapter: § 172.5(a)(1)
  source_quote: |
    "The quantity of the substance added to food does not exceed the amount reasonably required to accomplish its intended physical, nutritive, or other technical effect in food."
  summary: "无 ppm 上限的条款由这条兜底：用量不得超过实现预期物理、营养或其他技术效果所合理需要的量。它是一条实质限制，主张者须能论证技术效果需要多少。常见误读是「没有数字＝不限量」。"
  tags: [总则, GMP, 用量判据]

- id: t281
  title: food grade（食品级）
  type: term
  source_chapter: § 172.5(a)(2)
  source_quote: |
    "Any substance intended for use in or on food is of appropriate food grade and is prepared and handled as a food ingredient."
  summary: "用于食品的物质须为适当食品级，并作为食品配料制备与处理。工业级或非食品级原料即使化学上等同也不合规。常见误读是只看纯度数值、不问是否按食品配料管理。"
  tags: [总则, GMP, 纯度]

- id: t282
  title: existence of a regulation（许可法规的效力边界）
  type: term
  source_chapter: § 172.5(b)
  source_quote: |
    "The existence of a regulation prescribing safe conditions of use for a food additive shall not be construed to relieve the use of the substance from compliance with any other provision of the Act."
  summary: "存在许可法规不得被解释为免除该物质受本法其他任何条款约束的义务。Part 172 只管许可与限量/规格层，标签归〔§ 101〕、过程控制归〔§ 117〕。常见误读是把「有 Part 172 条款」当成整体合规的免死金牌。"
  tags: [总则, 效力层, 不得混引]

- id: t283
  title: nutrient substance approval（营养物质许可 ≠ 有用性认定）
  type: term
  source_chapter: § 172.5(c)
  source_quote: |
    "The existence of any regulation prescribing safe conditions of use for a nutrient substance does not constitute a finding that the substance is useful or required as a supplement to the diet of humans."
  summary: "营养物质获许可只解决安全性，不构成其「对人类膳食有用或必需」的认定。据此做营养声称或膳食必要性主张属越界。常见误读是把「FDA 批准该营养素」当声称依据。"
  tags: [总则, 效力层, 营养声称]

- id: t284
  title: antioxidant（抗氧化剂功能）
  type: term
  source_chapter: § 172.110(b)
  source_quote: |
    "The BHA is used alone or in combination with BHT, as an antioxidant in foods, as follows:"
  summary: "抗氧化剂是本部分 Subpart B 的主功能之一，BHA 与 BHT 由同一表列头 total BHA and BHT 管、须合并计算。功能本身也是许可要件的一部分（超功能使用不获许可）。常见误读是把抗氧化剂与防腐剂混为一类从而套错限值表。"
  tags: [SubpartB, 抗氧化剂, 合并限量]

- id: t285
  title: in combination（合并限量）
  type: term
  source_chapter: § 172.120(b)(2)
  source_quote: |
    "With disodium EDTA (disodium ethylenediaminetetraacetate) in the following foods at not to exceed, in combination, the levels prescribed, calculated as anhydrous C10H12O8N2CaNa2:"
  summary: "「in combination」指两种或多种物质合用时的限量按合并值计，不得各自擦线合格。钙二钠 EDTA 与二钠 EDTA 即属此例。常见误读是各物质按各自表值独立计算。"
  tags: [SubpartB, 合并限量, 计量基准]

- id: t286
  title: parts per million calculated as（计量基准）
  type: term
  source_chapter: § 172.180
  source_quote: |
    "in an amount not to exceed 20 parts per million calculated as tin (Sn)"
  summary: "限值常附「以某元素计」（calculated as X）的换算基准，如以 Sn 计、以 Br 计、以无水物计。换算基准错了限值就错了。常见误读是按化合物整体质量而非指定元素/形态计算。"
  tags: [限值, 计量基准, 判读]

- id: t287
  title: as measured in the loin muscle（法定取样部位）
  type: term
  source_chapter: § 172.177(b)
  source_quote: |
    "as measured in the loin muscle"
  summary: "取样部位本身可以是法规要件。烟熏鲢条款要求盐与亚硝酸盐均在 loin muscle 测定；换部位测出的数据不满足法定判据。常见误读是把限值当成对成品整体的平均值要求。"
  tags: [SubpartB, 工艺参数, 取样判据]

- id: t288
  title: water phase portion（水相盐分）
  type: term
  source_chapter: § 172.177(b)
  source_quote: |
    "The brining procedure is controlled in such a manner that the water phase portion of the edible portion of the finished smoked product has a salt (NaCl) content of not less than 3.5 percent, as measured in the loin muscle"
  summary: "盐分判据按「可食部的水相部分」计，且为下限（≥3.5%），与通常只给上限的限量方向相反。常见误读是按整鱼重量算盐分或只查上限。"
  tags: [SubpartB, 工艺参数, 下限判据]

- id: t289
  title: treated malt use-locked labeling statement（用途锁定声明）
  type: term
  source_chapter: § 172.730(c)
  source_quote: |
    "the label or labeling of the treated malt shall bear, in addition to other information required by the Act, the statement, “Brewer's Malt—To be used in the production of fermented malt beverages only”, or “Distiller's Malt—To be used in the production of distilled spirits only”, whichever is the case."
  summary: "用途限制通过处理物标签上的逐字法定措辞执行，自拟措辞不产生同样效果。同款结构亦见〔§172.725〕对赤霉酸/赤霉酸钾处理的麦芽。常见误读是以为意思相同即可。"
  tags: [SubpartB, 标签义务, 用途锁定]

- id: t290
  title: bromate (calculated as Br)（以 Br 计的溴酸盐限值）
  type: term
  source_chapter: § 172.730(a)(1)
  source_quote: |
    "does not exceed 75 parts per million of bromate (calculated as Br)"
  summary: "溴酸钾在麦芽中的限值为 ≤75 ppm 溴酸盐、以 Br 计，属「限值算在中间品」。常见误读是误算在成品饮料上，或按溴酸钾分子量而非 Br 计。"
  tags: [SubpartB, 限值, 中间品]

- id: t291
  title: total residue of inorganic bromides（他源累计残留）
  type: term
  source_chapter: § 172.730(a)(2)
  source_quote: |
    "(2) The total residue of inorganic bromides in fermented malt beverages, resulting from the use of the treated malt plus additional residues of inorganic bromides that may be present from uses in accordance with other regulations in this chapter promulgated under sections 408 and/or 409 of the act, does not exceed 25 parts per million of bromide (calculated as Br)."
  summary: "成品溴化物总残留须把「按本章其他法规使用所产生的额外同类残留」一并计入（≤25 ppm，以 Br 计）——即跨法规累计。常见误读是只算自己添加剂的贡献。"
  tags: [SubpartB, 限值, 累计残留]

- id: t292
  title: carrier（载体）与浓度披露
  type: term
  source_chapter: § 172.110(c)(2)
  source_quote: |
    "When the additive is marketed in a suitable carrier, in addition to meeting the requirement of paragraph (c)(1) of this section, the label shall declare the percentage of the additive in the mixture."
  summary: "以合适载体形式售卖的添加剂，标签除名称外还须申报添加剂在混合物中的百分比。常见误读是只标混合物商品名，不披露有效成分浓度。"
  tags: [SubpartB, 标签义务, 复配物]

- id: t293
  title: intermediate mix（中间混合料）
  type: term
  source_chapter: § 172.804(d)(1)
  source_quote: |
    "The principal display panel of any intermediate mix of the additive for manufacturing purposes shall bear a statement of the concentration of the additive contained therein;"
  summary: "面向生产的中间混合料须在主展示面标明添加剂浓度，以便下游正确配料。常见误读是把中间混合料当半成品、不做浓度披露。"
  tags: [SubpartI, 标签义务, 复配物]

- id: t294
  title: adequate directions for use（足够使用说明）
  type: term
  source_chapter: § 172.120(c)(2)
  source_quote: |
    "The label or labeling of the additive container shall bear adequate use directions to provide a final food product that complies with the limitations provided in paragraph (b) of this section."
  summary: "「足够使用说明」是法定的间接管控手段：通过容器标签指导下游，使成品不超限。常见误读是以为限值只靠终端检测，忽略说明书义务。"
  tags: [标签义务, 使用说明, 间接管控]

- id: t295
  title: To assure safe use（标签义务段）
  type: term
  source_chapter: § 172.730(b) 对照 § 172.110(c) 等
  source_quote: |
    "(b) To assure safe use of the additive, the label or labeling of the food additive shall bear, in addition to the other information required by the Act, the following:"
  summary: "「To assure safe use」段是条款内的标签义务块，实测仅约 25% 条款带此段。有该段时必须落实（通常要求标添加剂名称与足够使用说明，如本处以 name of the additive 与 adequate directions for use 收口）；无该段时不得凭空补造。常见误读是默认条条都有标签义务。"
  tags: [标签义务, 条款语法, 判读]

- id: t296
  title: identity / specifications / conditions of use（三段式条款语法）
  type: term
  source_chapter: § 172.785
  source_quote: |
    "The additive may be safely used as an antimicrobial agent specific for Listeria monocytogenes (L. monocytogenes) in accordance with the following conditions:"
  summary: "条款常按 (a) Identity → (b) Specifications → (c) Conditions of use 三段展开：身份要件、纯度/效价规格、使用条件。判读时逐段核对，任一段不满足即不合规。常见误读是只看用量一段。"
  tags: [条款语法, 判读, 生物类]

- id: t297
  title: incorporated by reference (IBR)
  type: term
  source_chapter: § 172.185(b) / § 172.785(b)(1)
  source_quote: |
    "The analytical method for determining the potency of the additive entitled “Determination of Potency of LMP-102TM,” dated October 9, 2003, and printed by Intralytix, Inc., is incorporated by reference."
  summary: "IBR 指把外部文件（FCC 页码、厂商方法、菌株资料）并入法规，法律效力等同正文，但内容不在本件、不在本技能包内。只可引「须符合某文件某版某页」，绝不转述其内部数值。常见误读是凭记忆写出被引文件的数值。"
  tags: [效力层, IBR, 不可转述]

- id: t298
  title: Food Chemicals Codex (FCC)
  type: term
  source_chapter: § 172.831(b)
  source_quote: |
    "The additive meets the specifications of the Food Chemicals Codex, 7th ed. (2010), pp. 993-995, which is incorporated by reference."
  summary: "FCC 是 Part 172 最常被 IBR 引用的纯度规格来源，引用须写清版次与页码（FCC 7th ed.＝2010、9th ed.＝2014）。版本/页码张冠李戴即引用错误。常见误读是把 FCC 当法规正文直接引其数值。"
  tags: [效力层, IBR, 纯度规格]

- id: t299
  title: specifications（纯度规格直写）
  type: term
  source_chapter: § 172.110(a)
  source_quote: |
    "Assay (total BHA), 98.5 percent minimum. Melting point 48 °C minimum."
  summary: "部分条款把规格数值直接写在条文里（可核对），与整体 IBR 的条款并存于同一 Subpart。判定先问：这条给的是可读数值还是外转引用。常见误读是假设「有规格＝有可读数值」。"
  tags: [纯度规格, 判读, SubpartB]

- id: t300
  title: Use / Function 栏（功能限制）
  type: term
  source_chapter: § 172.120(b)(1)
  source_quote: |
    "(1) Alone, in the following foods at not to exceed the levels prescribed, calculated as the anhydrous compound:"
  summary: "限值表常带 Use/Function 栏，把物质的使用绑定到特定功能（如 retard struvite formation、promote color retention）。超功能使用不在许可内。常见误读是只核对 ppm、忽略功能要件；表内 Use 栏文字属表区，须回原 PDF 核对。"
  tags: [限值表, 功能限制, 判读]

- id: t301
  title: specified foods（指定食品，封闭清单）
  type: term
  source_chapter: § 172.110
  source_quote: |
    "The food additive BHA (butylated hydroxyanisole) alone or in combination with other antioxidants permitted in food for human consumption in this subpart B may be safely used in or on specified foods, as follows:"
  summary: "「specified foods」是封闭清单，须逐项对照；未列举的食品即不在许可内。常见误读是把列举当作举例、允许类推到「相近」食品。"
  tags: [许可四元组, 封闭清单, 判读]

- id: t302
  title: except in meat and poultry（肉禽除外）
  type: term
  source_chapter: § 172.829(c) / § 172.800
  source_quote: |
    "(c) The food additive neotame may be safely used as a sweetening agent and flavor enhancer in foods generally, except in meat and poultry, in accordance with current good manufacturing practice, in an amount not to exceed that reasonably required to accomplish the intended technical effect, in foods for which standards of identity established under section 401 of the Federal Food, Drug, and Cosmetic Act do not preclude such use."
  summary: "「食品一般、肉禽除外」是通用甜味剂类条款的常见范围句式。肉禽制品属 USDA/FSIS 管辖，另成体系，不得搬用 Part 172 许可。常见误读是见「foods generally」就认为无类别限制。"
  tags: [许可四元组, 食品类别, 管辖分工]

- id: t303
  title: standards of identity do not preclude such use（标准身份不排除）
  type: term
  source_chapter: § 172.829(c)
  source_quote: |
    "in foods for which standards of identity established under section 401 of the Federal Food, Drug, and Cosmetic Act do not preclude such use"
  summary: "即使有添加剂许可，若某标准化食品（section 401 标准身份）排除该用途，则仍不得使用。判定顺序是先过标准身份闸门、再过用量。常见误读是认为 FDA 许可优先于标准身份。"
  tags: [许可四元组, 标准身份, 判读]

- id: t304
  title: special dietary use（特殊膳食，part 105）
  type: term
  source_chapter: § 172.829(e)
  source_quote: |
    "(e) If the food containing the additive purports to be or is represented to be for special dietary use, it shall be labeled in compliance with part 105 of this chapter."
  summary: "条款内部指向 part 105 的特殊膳食标签义务：食品若宣称或表示为特殊膳食用途，须符合 part 105。这是跨部分义务，不因符合 Part 172 用量而免除。常见误读是把该指引当可有可无的提示。"
  tags: [标签义务, 跨部分指引, SubpartI]

- id: t305
  title: antimicrobial agent（抗菌剂）
  type: term
  source_chapter: § 172.785
  source_quote: |
    "The additive may be safely used as an antimicrobial agent specific for Listeria monocytogenes (L. monocytogenes) in accordance with the following conditions:"
  summary: "生物类抗菌剂（如李斯特菌噬菌体制剂）的许可对象是「针对特定致病菌的抗菌用途」，范围由靶菌与食品类别共同封闭。常见误读是当作广谱消毒剂或通用防腐剂使用。"
  tags: [SubpartH, 抗菌剂, 生物类]

- id: t306
  title: bacteriophage（噬菌体）身份要件
  type: term
  source_chapter: § 172.785(a)(1)
  source_quote: |
    "The additive consists of a mixture of equal proportions of six different individually purified lytic-type (lacking lysogenic activity) bacteriophages (phages) specific against L. monocytogenes."
  summary: "身份要件须逐条满足：6 种等比例、各自纯化、裂解型且无溶原活性、特异性针对 L. monocytogenes。常见误读是只看「含噬菌体」而不核数量、比例与溶原性。"
  tags: [SubpartH, 身份要件, 生物类]

- id: t307
  title: ready-to-eat（9 CFR 430.1）
  type: term
  source_chapter: § 172.785(c)
  source_quote: |
    "(c) Conditions of use. The additive is used in accordance with current good manufacturing practice to control L. monocytogenes by direct application to meat and poultry products that comply with the ready-to-eat definition in 9 CFR 430.1."
  summary: "适用范围边界外转到 9 CFR 430.1 的 ready-to-eat 定义：是否即食按该外部定义判定，不按「接近即食」的直觉。常见误读是以产品性质相近替代法定定义。"
  tags: [SubpartH, 使用条件, 外部定义]

- id: t308
  title: potency / lytic result（效价与裂解结果）
  type: term
  source_chapter: § 172.785(b)(1)
  source_quote: |
    "The additive achieves a positive lytic result (OD600 ≤0.06) when tested against any of the following L. monocytogenes isolates available from American Type Culture Collection (ATCC): ATCC 35152 (serogroup 1/2a), ATCC 19118 (serogroup 4b), and ATCC 15313 (serogroup 1/2b)."
  summary: "效价要件是「对指定 ATCC 菌株呈阳性裂解结果（OD600 ≤0.06）」，菌株编号与血清型是法定要件。测法多 IBR 外转。常见误读是只写「有抑菌效果」而不核指定菌株与阈值。"
  tags: [SubpartH, 规格, 效力层]

- id: t309
  title: nutrient compensation（强制营养补偿）
  type: term
  source_chapter: § 172.867(d)
  source_quote: |
    "(d) To compensate for any interference with absorption of fat soluble vitamins, the following vitamins shall be added to foods containing olestra:"
  summary: "脂肪替代物（Olestra）的许可以「强制补偿脂溶性维生素」为生效条件：须按规定量添加 A/D/E/K，否则不合规。常见误读是把补偿当推荐做法。"
  tags: [SubpartI, 脂肪替代物, 强制条件]

- id: t310
  title: Dietarily insignificant（膳食上不显著）
  type: term
  source_chapter: § 172.867(e)(1)(iii)
  source_quote: |
    "an asterisk and statement, “Dietarily insignificant” shall appear prominently and conspicuously as specified in § 101.2(c) of this chapter;"
  summary: "Olestra 补偿添加的 A/D/E/K 须在配料表用星号标注，并在配料表后紧随星号与 Dietarily insignificant 声明，不得计入营养标签或营养声称。常见误读是把补偿维生素算作产品营养含量。"
  tags: [SubpartI, 标签义务, 营养标签]

- id: t311
  title: natural flavoring substances（天然香料）
  type: term
  source_chapter: § 172.510
  source_quote: |
    "Natural flavoring substances and natural adjuvants may be safely used in food in accordance with the following conditions."
  summary: "天然香料是名录型条款（Common name / Scientific name / Limitations 三列约千行），条首仅给「最小需要量 + GMP」通用条件，具体限制须逐行看 Limitations 列。名录内部行属不可逐字引用区。常见误读是把「在清单里」当「无限制」。"
  tags: [SubpartF, 名录型条款, 导航]

- id: t312
  title: synthetic flavoring substances and adjuvants（合成香料与助剂）
  type: term
  source_chapter: § 172.515
  source_quote: |
    "Synthetic flavoring substances and adjuvants may be safely used in food in accordance with the following conditions."
  summary: "合成香料清单（约 30 页、上千条物质名）为纯名录，不含用量限制列，只解决「是否被许可」。用量回到条首的「最小需要量 + GMP」。常见误读是去名录里找 ppm。"
  tags: [SubpartF, 名录型条款, 导航]

- id: t313
  title: Do.（同上 / ditto）
  type: term
  source_chapter: § 172.510(b) 名录行示例
  source_quote: |
    "Arnica flowers Arnica montana L., A. fulgens Pursh, A. sororia Greene, or Do."
  summary: "Do. 是英文编纂惯用的「同上」，表示复制上一行同列的内容，绝非「无限制」。整列 Do. 还提示可能跨页续表被重置，须回原 PDF 逐格核对。示例行取自名录（名录内行属不可逐字引用区，此处仅引 Do. 语义）。常见误读是把 Do. 读成空白或免除。"
  tags: [限值表, 判读, 转换局限]

- id: t314
  title: multipurpose additive（多用途添加剂）
  type: term
  source_chapter: Subpart I
  source_quote: |
    "Subpart I — Multipurpose Additives"
  summary: "Subpart I 收录可按多种功能使用的添加剂（甜味剂、脂肪替代物、改性淀粉、乳化剂等），多为「食品一般 + cGMP」型或表格式限量。与前面按功能单列的子部分结构不同。常见误读是把它当作「无功能限制」。"
  tags: [SubpartI, 结构, 导航]

- id: t315
  title: residual limitation（成品残留限值）
  type: term
  source_chapter: § 172.892
  source_quote: |
    "The quantity of any substance employed to effect such modification shall not exceed the amount reasonably required to accomplish the intended physical or technical effect, nor exceed any limitation prescribed."
  summary: "改性淀粉类条款把「合理需要量」与「任何规定限值」并列，并常另设成品残留限值（如残锰、残磷）。限值可能落在处理剂、也可能落在成品残留。常见误读是只查处理剂用量、漏查成品残留。"
  tags: [SubpartI, 限值, 残留]

- id: t316
  title: food starch-modified（法定品名）
  type: term
  source_chapter: § 172.892
  source_quote: |
    "the label of the food additive container shall bear the name of the additive “food starch-modified” in addition to other information required by the Act."
  summary: "改性淀粉容器标签须逐字标示法定品名 food starch-modified。此类「法定品名」义务是条款自带义务的一种形态，与 To assure safe use 段不同。常见误读是自拟商品名代替法定品名。"
  tags: [SubpartI, 标签义务, 法定品名]

- id: t317
  title: generally recognized as safe（条款内 GRAS 指引）
  type: term
  source_chapter: § 172.510(b)
  source_quote: |
    "used alone or in combination with flavoring substances and adjuvants generally recognized as safe in food, previously sanctioned for such use, or regulated in any section of this part."
  summary: "Part 172 条款内部会指向 GRAS、prior-sanctioned 或其他条款所管物质，形成「与获准物质组合使用」的许可路径。GRAS 本体（Part 182 等）不在本包内，只可引「属于 GRAS」这一事实，不复述其清单。常见误读是把 GRAS 当可在 Part 172 内自行认定。"
  tags: [效力层, 跨部分指引, 名录型条款]

- id: t318
  title: prior-sanctioned（既往认可）
  type: term
  source_chapter: § 172.515(b)
  source_quote: |
    "used alone or in combination with flavoring substances and adjuvants generally recognized as safe in food, prior-sanctioned for such use, or regulated by an appropriate section in this part."
  summary: "prior-sanctioned 指 1958 年添加剂修正案前已获 FDA/USDA 认可的物质，与 GRAS 并列为另一条合法性来源。其清单不在本包内，只可引「属于 prior-sanctioned」这一事实。常见误读是把 prior-sanctioned 与 GRAS 混为一条路径。"
  tags: [效力层, 跨部分指引, 名录型条款]
