# 候选池：案例提取器 | 来源 21 CFR Part 172 eCFR 2026-11-05 | 全量扫描 chunk-01..04

> 主代理顺序执行（并行子代理被上游限流）。扫描覆盖：chunk-01（§172.5–385）/ chunk-02（§172.395–660）/ chunk-03（§172.665–844）/ chunk-04（§172.846–898），154/154 条款；以 `shall bear` / `not to exceed` / `incorporated by reference` / `Do.` / `may be safely used` / 具体产品名 / 数值场景为锚词 Grep 命中后回读。
> 纪律：引用逐字来自 `source-cfr-part172-2026.md`（归一化空白后可命中）；16 张重建表格数值、§172.510/§172.515 名录、IBR 外部文件内容标**不可逐字引用区**，本件只引其「存在与边界」不引其内部数值。
> 本件的「案例」＝法规正文亲自给出的**许可四元组实例、限量/工艺参数句式、标签义务措辞、名录导航场景**（联邦法规无叙事案例），供能力卡 A1「照着做」段取用。条款号一律写〔§ 172.xxx〕，pdf-page 为 `<!-- pdf-page N -->` 标记对应页。

---

### CAND-CS-01: §172.5 三条元规则原文（GMP 双重限制 + 两条否定式）

- 条款出处：〔§ 172.5(a)(b)(c)〕pdf-page 5
- 原文引用（英文逐字）：
  > "(a) Regulations prescribing conditions under which food additive substances may be safely used predicate usage under conditions of good manufacturing practice. For the purposes of this part, good manufacturing practice shall be defined to include the following restrictions. (1) The quantity of the substance added to food does not exceed the amount reasonably required to accomplish its intended physical, nutritive, or other technical effect in food. (2) Any substance intended for use in or on food is of appropriate food grade and is prepared and handled as a food ingredient."
  > —— 〔§ 172.5(a)〕[pdf-page 5]
  > "(b) The existence of a regulation prescribing safe conditions of use for a food additive shall not be construed to relieve the use of the substance from compliance with any other provision of the Act. (c) The existence of any regulation prescribing safe conditions of use for a nutrient substance does not constitute a finding that the substance is useful or required as a supplement to the diet of humans."
  > —— 〔§ 172.5(b)(c)〕[pdf-page 5]
- 场景（这是一件什么事、谁要用）：任何要用直接添加剂的产品开发/法规事务人员。判「我这个用量合不合法」时，§172.5 是压在**每一条** §172.xxx 之上的兜底；无论具体条款给不给数字，这两条 GMP 限制都在。
- 可照抄的动作/措辞：用量判据＝**不超过实现预期技术效果所合理需要的量**（不是「有上限就能用满」）；物质须为**食品级**并作食品配料制备与处理；说法条「许可」不解除本法其他条款（如标签、掺假、卫生）义务；营养物质获批**不等于**被认定膳食有用或必需（不得据此做营养声称）。
- 可回答的新问题：某添加剂条款没给 ppm 上限，是不是就能无限量用？拿到许可后是否还要满足 Part 101 标签与 Part 117 过程控制？能否引用「FDA 批准了该营养素」做膳食必要性主张？
- 建议归属子卡：V01

### CAND-CS-02: §172.110 BHA —— 表内限量 + 载体浓度披露 + 干燥混合料的使用说明义务

- 条款出处：〔§ 172.110〕pdf-page 6
- 原文引用（英文逐字）：
  > "Assay (total BHA), 98.5 percent minimum. Melting point 48 °C minimum."
  > "(b) The BHA is used alone or in combination with BHT, as an antioxidant in foods, as follows:"
  > "(2) When the additive is marketed in a suitable carrier, in addition to meeting the requirement of paragraph (c)(1) of this section, the label shall declare the percentage of the additive in the mixture."
  > "(3) The label or labeling of dry mixes for beverages and desserts shall bear adequate directions for use to provide that beverages and desserts prepared from the dry mixes contain no more than 2 parts per million BHA."
  > —— 〔§ 172.110(a)(b)(c)〕[pdf-page 6]
- 场景（这是一件什么事、谁要用）：抗氧化剂供应商与使用方。BHA 与 BHT **共用同一张限量表**（列头即 “total BHA and BHT”），故两者叠加须合并计算；以载体形式售卖时要标浓度；卖「饮料/甜点干混粉」时还得把「冲调后 ≤2 ppm」写进使用说明。
- 可照抄的动作/措辞：纯度 `Assay (total BHA), 98.5 percent minimum`；限量表数值属**不可逐字引用区**（回原 PDF 核对，含脚注 `1 BHA only.`）；载体售卖→标签申报**添加剂在混合物中的百分比**；干混料→标签或说明书须含足以保证成品 ≤2 ppm 的使用指南。
- 可回答的新问题：BHA 和 BHT 同时加要不要合并算限量？我从经销商买的「含 BHA 的抗氧化剂复配物」标签上必须写什么？卖冲调粉要附什么说明？
- 建议归属子卡：V02

### CAND-CS-03: §172.120 钙二钠 EDTA —— 「单用」与「与二钠 EDTA 合用」两套限值

- 条款出处：〔§ 172.120(b)〕pdf-page 7–9
- 原文引用（英文逐字）：
  > "(1) Alone, in the following foods at not to exceed the levels prescribed, calculated as the anhydrous compound:"
  > "(2) With disodium EDTA (disodium ethylenediaminetetraacetate) in the following foods at not to exceed, in combination, the levels prescribed, calculated as anhydrous C10H12O8N2CaNa2:"
  > "(2) The label or labeling of the additive container shall bear adequate use directions to provide a final food product that complies with the limitations provided in paragraph (b) of this section."
  > —— 〔§ 172.120(b)(c)〕[pdf-page 7–9]
- 场景（这是一件什么事、谁要用）：罐头蔬菜/贝类/蛋黄酱/沙拉酱/调料/发酵麦芽饮料的配方与法规人员。钙二钠 EDTA 与二钠 EDTA 是**两个物质、两条限值**，但当二者**合用**时按 (b)(2) 的「in combination」合并计数，且计量基础是**无水物**。
- 可照抄的动作/措辞：先判是「单用」还是「与二钠 EDTA 合用」，合用时用 (b)(2) 的合并限值；计量一律换算成无水物；表列 `Use` 栏（如 `Retard struvite formation; promote color retention.`）是**功能限制**，不能超出该功能使用；表数值属不可逐字引用区；容器标签须附保证成品不超限的使用说明。
- 可回答的新问题：两种 EDTA 同时用怎么算限量？罐头蟹肉用 EDTA 是为了什么功能，能否改作其他功能？限值按水合物还是无水物计？
- 建议归属子卡：V02

### CAND-CS-04: §172.177 烟熏鲢用亚硝酸钠 —— 多栅栏工艺参数条款

- 条款出处：〔§ 172.177〕pdf-page 18–19
- 原文引用（英文逐字）：
  > "(b) The brining procedure is controlled in such a manner that the water phase portion of the edible portion of the finished smoked product has a salt (NaCl) content of not less than 3.5 percent, as measured in the loin muscle, and the sodium nitrite content of the edible portion of the finished smoked product is not less than 100 parts per million and not greater than 200 parts per million, as measured in the loin muscle."
  > "(c) Smoked chub shall be heated by a controlled heat process which provides a monitoring system positioned in as many strategic locations in the smokehouse as necessary to assure a continuous temperature throughout each fish of at least 160 °F for a minimum of 30 minutes."
  > "(d) The finished product shall be cooled to a temperature of 50 °F or below within 3 hours after smoking and further cooled to a temperature of 38 °F or below within 12 hours after smoking."
  > —— 〔§ 172.177(b)(c)(d)〕[pdf-page 18]
- 场景（这是一件什么事、谁要用）：做冷熏鲢的加工厂。这不是「加多少」的单点条款，而是**盐浓度下限 + 亚硝酸盐区间 + 加热曲线 + 冷却曲线**四条栅栏同时生效；任何一条不达标即不合规，且**取样部位法定**（loin muscle）。
- 可照抄的动作/措辞：盐（NaCl）水相 ≥3.5%、亚硝酸盐 100–200 ppm，两者均**在 loin muscle 测定**；烟熏房须布置足够监控点保证每尾鱼芯温 ≥160 °F 持续 ≥30 min；熏后 3 h 内降至 ≤50 °F、12 h 内降至 ≤38 °F 并全程冷链；运输容器/零售包装/运输记录须注明易腐并标示 ≤38 °F 冷藏直至食用。
- 可回答的新问题：亚硝酸盐 250 ppm 是否更保险？能否用测得 3.2% 盐的产品？温度探点不够行不行？取样测哪块肉？
- 建议归属子卡：V02

### CAND-CS-05: §172.730 溴酸钾 —— 限值在中间品、残留算成品、用途靠标签锁定

- 条款出处：〔§ 172.730〕pdf-page 104
- 原文引用（英文逐字）：
  > "(1) It is used or intended for use in the malting of barley under conditions whereby the amount of the additive present in the malt from the treatment does not exceed 75 parts per million of bromate (calculated as Br), and the treated malt is used only in the production of fermented malt beverages or distilled spirits."
  > "(c) To assure safe use of the additive, the label or labeling of the treated malt shall bear, in addition to other information required by the Act, the statement, “Brewer's Malt—To be used in the production of fermented malt beverages only”, or “Distiller's Malt—To be used in the production of distilled spirits only”, whichever is the case."
  > —— 〔§ 172.730(a)(c)〕[pdf-page 104]
- 场景（这是一件什么事、谁要用）：麦芽厂与酒厂。溴酸钾的合法用量限在**麦芽**（≤75 ppm 溴酸盐，以 Br 计），成品饮料里限的是**溴化物总残留**（≤25 ppm，含其他法规来源的溴化物，见〔§172.730(a)(2)〕）；「只能用于啤酒或蒸馏酒」这条用途限制**靠处理物标签的法定措辞实现**。
- 可照抄的动作/措辞：限值测**麦芽**不测成品；成品另受溴化物总残留限制且须并入他源；处理过的麦芽标签须逐字写 `Brewer's Malt—To be used in the production of fermented malt beverages only` 或 `Distiller's Malt—To be used in the production of distilled spirits only`（择一）。同款「用途锁定声明」亦见于〔§172.725〕对赤霉酸/赤霉酸钾处理麦芽的规定。
- 可回答的新问题：限值是测麦芽还是测啤酒？被单独摄入的麦芽（非酿酒）合不合规？标签上怎么把用途锁死？
- 建议归属子卡：V01 / V02

### CAND-CS-06: §172.785 李斯特菌噬菌体制剂 —— 生物类抗菌剂的「三段式」条款

- 条款出处：〔§ 172.785〕pdf-page 108–109
- 原文引用（英文逐字）：
  > "The additive consists of a mixture of equal proportions of six different individually purified lytic-type (lacking lysogenic activity) bacteriophages (phages) specific against L. monocytogenes."
  > "The mean phage titer of each monophage in the additive is 1 × 109 plaque forming units (PFU)/ml."
  > "(c) Conditions of use. The additive is used in accordance with current good manufacturing practice to control L. monocytogenes by direct application to meat and poultry products that comply with the ready-to-eat definition in 9 CFR 430.1. Current good manufacturing practice is consistent with direct spray application of the additive at a rate of approximately 1 mL of the additive per 500 cm2 product surface area."
  > —— 〔§ 172.785(a)(b)(c)〕[pdf-page 108–109]
- 场景（这是一件什么事、谁要用）：即食肉禽制品厂的食品安全/法规人员。生物类抗菌剂条款的结构是 **Identity（a）+ Specifications（b）+ Conditions of use（c）**；用量不是硬 ppm，而是「按 cGMP + 约 1 mL / 500 cm²」的**近似施用率**，且适用范围由「符合 9 CFR 430.1 RTE 定义」这一**外部引用**封闭。
- 可照抄的动作/措辞：身份要件须逐条满足（6 种等比例、纯化裂解型、无溶原性、菌种保藏可溯源）；规格须可测（效价 OD600 ≤0.06 对 ATCC 35152/19118/15313、每单噬菌体滴度 1×10⁹ PFU/ml、LLO ≤5 HU/ml、TOC ≤36 mg/kg）——**方法多以 IBR 外转**，数值不可转述；使用条件＝RTE 肉禽直接喷淋，≈1 mL/500 cm²。
- 可回答的新问题：噬菌体喷淋量有没有硬上限？「即食」范围怎么界定？规格指标去哪查测法？
- 建议归属子卡：V02 / V05

### CAND-CS-07: §172.804 阿斯巴甜 —— 强制警示语 + 中间品浓度披露

- 条款出处：〔§ 172.804(c)(d)〕pdf-page 112–113
- 原文引用（英文逐字）：
  > "(2) When aspartame is used in baked goods and baking mixes, the amount of the additive is not to exceed 0.5 percent by weight of ready-to-bake products or of finished formulations prior to baking."
  > "(1) The principal display panel of any intermediate mix of the additive for manufacturing purposes shall bear a statement of the concentration of the additive contained therein;"
  > "(2) The label of any food containing the additive shall bear, either on the principal display panel or on the information panel, the following statement: PHENYLKETONURICS: CONTAINS PHENYLALANINE"
  > —— 〔§ 172.804(c)(2)(d)(1)(2)〕[pdf-page 112–113]
- 场景（这是一件什么事、谁要用）：甜味剂使用方与标签设计。阿斯巴甜除用途/限量外，还背一条**特定警示语**与一条**中间品浓度披露**义务；警示语措辞、位置、字体都有法定要求（`bold type` / `clear contrasting background`）。
- 可照抄的动作/措辞：烘焙品中 ≤0.5%（按入炉前成品或配方重）；面向生产的**中间混合料**须在主展示面标浓度；含阿斯巴甜的食品标签须在主展示面或信息面板载明 `PHENYLKETONURICS: CONTAINS PHENYLALANINE`，并**显著、粗体、清晰对比**。此警示语属**标签法条层**，具体排版本体见〔§ 101〕。
- 可回答的新问题：烘焙用阿斯巴甜上限是多少？卖给工厂的预混料要标什么？苯丙酮尿症警示语写在哪、什么字体？
- 建议归属子卡：V03 / V01

### CAND-CS-08: §172.829 纽甜 —— 同一 Subpart 内「直写数值」与「整体 IBR」并存

- 条款出处：〔§ 172.829〕pdf-page 124–125
- 原文引用（英文逐字）：
  > "(1) Assay for neotame, not less than 97.0 percent and not more than 102.0 percent on a dry basis. (2) Free dipeptide acid (N-[N-(3,3-dimethylbutyl)-L-α-aspartyl]-L-phenylalanine), not more than 1.5 percent. (3) Other related substances, not more than 2.0 percent. (4) Lead, not more than 2.0 milligrams per kilogram. (5) Water, not more than 5.0 percent."
  > "(c) The food additive neotame may be safely used as a sweetening agent and flavor enhancer in foods generally, except in meat and poultry, in accordance with current good manufacturing practice, in an amount not to exceed that reasonably required to accomplish the intended technical effect, in foods for which standards of identity established under section 401 of the Federal Food, Drug, and Cosmetic Act do not preclude such use."
  > "(e) If the food containing the additive purports to be or is represented to be for special dietary use, it shall be labeled in compliance with part 105 of this chapter."
  > —— 〔§ 172.829(b)(c)(e)〕[pdf-page 124–125]
- 场景（这是一件什么事、谁要用）：甜味剂合规判定。纽甜把 7 项规格**直接写在条文里**（可直接核对），而许可范围是「食品一般、肉禽除外 + cGMP + 不超过合理需要量 + 标准身份不排除」——**没有 ppm 上限**，靠 GMP 兜底。这与同 Subpart 的〔§172.831〕磺胺类代糖（规格整体 IBR 到 FCC 页码）形成对照。
- 可照抄的动作/措辞：规格可直写数值的照抄（assay 97.0–102.0%、游离二肽酸 ≤1.5%、其他相关物质 ≤2.0%、铅 ≤2.0 mg/kg、水 ≤5.0%）；用途判据＝`foods generally, except in meat and poultry` + GMP + 标准身份不排除；作为糖替代片剂时 L-亮氨酸 ≤3.5% 片重；供特殊膳食须符合 part 105 标签。
- 可回答的新问题：纽甜有没有 ppm 上限？「标准身份排除了吗」怎么判？纽甜糖片里能加什么润滑剂、多少？
- 建议归属子卡：V03 / V05

### CAND-CS-09: §172.867 Olestra —— 强制营养补偿与「不计入脂肪/热量」

- 条款出处：〔§ 172.867(c)(d)(e)〕pdf-page 153–154
- 原文引用（英文逐字）：
  > "(c) Olestra may be used in place of fats and oils in prepackaged ready-to-eat savory (i.e., salty or piquant but not sweet) snacks and prepackaged, unpopped popcorn kernels that are ready-to-heat."
  > "(d) To compensate for any interference with absorption of fat soluble vitamins, the following vitamins shall be added to foods containing olestra: 1.9 milligrams alpha-tocopherol equivalents per gram olestra; 51 retinol equivalents per gram olestra (as retinyl acetate or retinyl palmitate); 12 IU vitamin D per gram olestra; and 8 µg vitamin K1 per gram olestra."
  > "(1) Vitamins A, D, E, and K present in foods as a result of the requirement in paragraph (d) of this section shall be declared in the listing of ingredients. Such vitamins shall not be considered in determining nutrient content for the nutritional label or for any nutrient claims, express or implied."
  > "(iii) Immediately following the ingredient list an asterisk and statement, “Dietarily insignificant” shall appear prominently and conspicuously as specified in § 101.2(c) of this chapter;"
  > "(2) Olestra shall not be considered as a source of fat or calories for purposes of §§ 101.9 and 101.13 of this chapter."
  > —— 〔§ 172.867(c)(d)(e)〕[pdf-page 153–154]
- 场景（这是一件什么事、谁要用）：用 Olestra 替代油脂做膨化零食/爆米花的厂商。这里的「营养补偿」不是建议而是**许可的生效条件**：不加就违法。而且补偿维生素的标注方式也是法定的（必须打星号 + `Dietarily insignificant`，且不得计入营养标签或任何营养声称）。
- 可照抄的动作/措辞：适用范围＝预包装即食咸/辛非甜零食 + 预包装待加热未爆玉米粒；每克 Olestra 须补 α-生育酚当量 1.9 mg、视黄醇当量 51 RE、维 D 12 IU、维 K1 8 µg；A/D/E/K 在配料表标注、加星号上标、配料表后紧随星号 + `Dietarily insignificant`；Olestra **不计作**脂肪或热量来源（对接 §§101.9/101.13）。
- 可回答的新问题：用 Olestra 必须补哪些维生素、补多少？补进去的维生素算不算营养含量？营养标签上 Olestra 的脂肪/热量怎么处理？
- 建议归属子卡：V03 / V01

### CAND-CS-10: §172.812 甘氨酸 —— 用途-限制双列表 + 饮料基料使用说明

- 条款出处：〔§ 172.812〕pdf-page 118
- 原文引用（英文逐字）：
  > "The additive meets the specifications of the Food Chemicals Codex, 7th ed. (2010), pp. 457-458, which is incorporated by reference."
  > "The labeling of beverage bases containing the additive shall bear adequate directions for use to provide that beverages prepared therefrom shall contain no more than 0.2 percent glycine."
  > —— 〔§ 172.812(a)(c)(2)〕[pdf-page 118]
- 场景（这是一件什么事、谁要用）：做无糖饮料/单甘酯的厂商。甘氨酸条款的用途是**逐功能限定的**：只许做「糖精苦后味的掩蔽剂（成品 ≤0.2%）」与「单/双甘酯的稳定剂（≤0.02%）」，不是通用配料。
- 可照抄的动作/措辞：规格整体 IBR 到 FCC 7th ed. pp. 457-458（**数值不可转述**）；用途-限值为两行对照（掩蔽剂 ≤0.2% 成品 / 稳定剂 ≤0.02% 单双甘酯）；**饮料基料**标签须附使用说明以保证冲调后 ≤0.2%。注意 (b) 表在本转换件中为双列交叉行（非独立重建表），引用只取可逐字命中的散文句，表内值回原 PDF 核对。
- 可回答的新问题：甘氨酸能当通用甜味剂吗？饮料基料要附什么说明？限值 0.2% 是按成品还是按基料？
- 建议归属子卡：V04

### CAND-CS-11: §172.892 改性食品淀粉 —— 「不超过合理需要量 + 不超任何规定限制」的双重兜底与法定品名

- 条款出处：〔§ 172.892〕pdf-page 173
- 原文引用（英文逐字）：
  > "The quantity of any substance employed to effect such modification shall not exceed the amount reasonably required to accomplish the intended physical or technical effect, nor exceed any limitation prescribed."
  > "To insure safe use of the food starch-modified, the label of the food additive container shall bear the name of the additive “food starch-modified” in addition to other information required by the Act."
  > —— 〔§ 172.892〕[pdf-page 173]
- 场景（这是一件什么事、谁要用）：改性淀粉厂与配方师。这条把「双重兜底」写得最直白：处理剂用量既受 GMP「合理需要量」管，也受具体规定限值管；并且**法定品名 `food starch-modified`** 必须写在容器标签上。
- 可照抄的动作/措辞：处理剂用量 = min(合理需要量, 规定限值)；容器标签须逐字写 `food starch-modified`；后续 (b)–(g) 各改性方式（酸改、漂白、氧化、酯化、醚化等）的数值与 `Do.`（同上）行属**不可逐字引用区**，须回原 PDF 逐格核对（存在跨页续表与列内嵌限制，例：某漂白剂旁的 `The finished food starch-modified is limited to use only as a component of batter for commercially processed foods.`）。
- 可回答的新问题：改性淀粉处理剂有没有上限？容器上品名必须怎么写？某处理方式的附带使用限制在哪看？
- 建议归属子卡：V04

### CAND-CS-12: §172.510 / §172.515 长尾名录条款 —— 「怎么导航」而不是「引哪一行」

- 条款出处：〔§ 172.510〕pdf-page 48–49；〔§ 172.515〕pdf-page 55
- 原文引用（英文逐字）：
  > "They are used in the minimum quantity required to produce their intended physical or technical effect and in accordance with all the principles of good manufacturing practice."
  > "they consist of one or more of the following, used alone or in combination with flavoring substances and adjuvants generally recognized as safe in food, previously sanctioned for such use, or regulated in any section of this part."
  > —— 〔§ 172.510(a)(b)〕[pdf-page 48–49]
  > "They are used in the minimum quantity required to produce their intended effect, and otherwise in accordance with all the principles of good manufacturing practice."
  > "They consist of one or more of the following, used alone or in combination with flavoring substances and adjuvants generally recognized as safe in food, prior-sanctioned for such use, or regulated by an appropriate section in this part."
  > —— 〔§ 172.515(a)(b)〕[pdf-page 55]
- 场景（这是一件什么事、谁要用）：香精香料配方师判「某物质是不是被许可」。这两条是**名录型条款**：条文本身只给「按最小需要量 + GMP」的通用条件，具体物质是否有条件限制要**逐行看该名录里那一行的 `Limitations` 列**（例：天然香料行的 `In alcoholic beverages only` 与 `Do.`）。
- 可照抄的动作/措辞：**〔不可逐字引用区〕**§172.510（天然，含 `Common name / Scientific name / Limitations` 三列约千行）与 §172.515（合成，纯物质名约 30 页、不含用量条件）一律**只做「在/不在清单」的存在性判断与导航**，不得逐字引用其中某行、不得凭名录推定用量；用量判据回到条首的「最小需要量 + GMP」。名录物质若用在**标准化食品**中，还要过标准身份这一关。
- 可回答的新问题：某天然香料有没有用量限制？「Amyris」这类原名对应哪个学名？合成香料清单能告诉我用量吗？
- 建议归属子卡：V04

### CAND-CS-13: §172.320 氨基酸 —— 列举式身份 + 二级引用链（FCC 页码 / NAS-NRC）

- 条款出处：〔§ 172.320〕pdf-page 30–31
- 原文引用（英文逐字）：
  > "The food additive consists of one or more of the following individual amino acids in the free, hydrated, or anhydrous form, or as the hydrochloride, sodium, or potassium salts:"
  > "(14) DL-Methionine (not for infant foods)"
  > —— 〔§ 172.320(a)〕[pdf-page 30]
- 场景（这是一件什么事、谁要用）：营养强化型配料厂。氨基酸条款是**列举式许可**：22 种氨基酸（含盐形式）被许可作营养添加剂，逐项给出规格来源；其中 DL-蛋氨酸带**人群限制** `(not for infant foods)`——限制直接嵌在列举项内。
- 可照抄的动作/措辞：许可范围＝列举内的 22 种（含 free/hydrated/anhydrous 与盐酸盐/钠盐/钾盐）；DL-蛋氨酸**不得用于婴幼儿食品**；规格走**二级引用链**——(b)(1) 指向 FCC 具体页码（如 `L-Alanine, pages 28 and 29.`），(b)(2) 指向 `Specifications and Criteria for Biochemical Compounds`（NAS/NRC），**这些页码与外部文件内容均不可逐字转述**，只可引「须符合某文件某页」。
- 可回答的新问题：哪种氨基酸能用于婴幼儿食品？氨基酸的纯度标准在哪？我引的 FCC 页码对不对？
- 建议归属子卡：V04 / V05

### CAND-CS-14: §172.180 氯化亚锡 —— 最短条款：一句话就是完整四元组

- 条款出处：〔§ 172.180〕pdf-page 19
- 原文引用（英文逐字）：
  > "The food additive stannous chloride may be safely used for color retention in asparagus packed in glass, with lids lined with an inert material, in an amount not to exceed 20 parts per million calculated as tin (Sn)."
  > —— 〔§ 172.180〕[pdf-page 19]
- 场景（这是一件什么事、谁要用）：玻璃罐装芦笋的护色。这是「物质 × 用途 × 用量 × 包装前提」压在一句话里的极端例：物质＝氯化亚锡；用途＝护色；载体前提＝玻璃罐装且盖内衬惰性材料；限值＝≤20 ppm（以 Sn 计）。**没有任何标签义务段**，说明「有条款 ≠ 有条条都有的模板」。
- 可照抄的动作/措辞：换包装（非玻璃罐/非惰性衬里）即**不在许可内**；限值以 **Sn** 计；本条无 `To assure safe use` 段，不得凭空补造标签义务。
- 可回答的新问题：塑料罐装芦笋能用氯化亚锡吗？限值按锡还是按氯化亚锡计？这条要不要写标签声明？
- 建议归属子卡：V01

### CAND-CS-15: §172.185 TBHQ —— 与 §172.831 对照的「不可转述」IBR 句式

- 条款出处：〔§ 172.185〕pdf-page 19–20；〔§ 172.831〕pdf-page 127
- 原文引用（英文逐字）：
  > "The percentage of TBHQ in the food additive is not less than 99.0 percent when tested by the assay described in the Food Chemicals Codex, 9th ed. (2014), pp. 1192-1194, which is incorporated by reference, or an equivalent method."
  > —— 〔§ 172.185(b)〕[pdf-page 19–20]
  > "(b) The additive meets the specifications of the Food Chemicals Codex, 7th ed. (2010), pp. 993-995, which is incorporated by reference."
  > —— 〔§ 172.831(b)〕[pdf-page 127]
- 场景（这是一件什么事、谁要用）：复核纯度规格的 QA/法规人员。这两条代表两种常见 IBR 句式：**半开放**（给一个可判的下限数值 + 「或等效方法」）与**整体外转**（规格全在外部文件，条文不给任何数值）。判读时必须区分：能否引用到具体数值。
- 可照抄的动作/措辞：TBHQ 可引 `not less than 99.0 percent`（半开放，允许等效方法）；磺胺类代糖（§172.831）只能引「须符合 FCC 7th ed. (2010) pp. 993-995」，**不得转述其内部 assay/杂质数值**；注意版本与页码不可张冠李戴（FCC 7th ed.＝2010、FCC 9th ed.＝2014）。
- 可回答的新问题：这条法规给了我能直接核对的纯度数值吗？没有的话该引哪一句？FCC 版本与页码对得上吗？
- 建议归属子卡：V05

---

## 覆盖自检

| 子卡 | 覆盖的案例 | 说明 |
|---|---|---|
| V01 许可判定链与限制五形态 | CS-01, CS-05, CS-07, CS-09, CS-14 | 四元组、用途锁定、警示语义务触发、强制补偿、最短条款 |
| V02 防腐剂与抗菌剂 | CS-02, CS-03, CS-04, CS-06 | 抗氧化剂合并限量、双物质合用、多栅栏工艺、生物类三段式 |
| V03 甜味剂与脂肪替代物 | CS-07, CS-08, CS-09 | 警示语、直写数值 vs IBR、营养补偿 |
| V04 品质功能类与长尾名录导航 | CS-10, CS-11, CS-12, CS-13 | 用途-限制双列、双重兜底、名录导航、列举+二级引用 |
| V05 效力层与 IBR 边界 | CS-06, CS-08, CS-13, CS-15 | IBR 两种句式、二级引用链、不可转述区 |

9 Subpart 覆盖：Subpart A（CS-01）/ B 防腐剂（CS-02, CS-03, CS-04）/ C 涂层（表内见 CS-11 同型）/ D 特殊膳食与营养（CS-13）/ E 胶体（—）/ F 风味（CS-12）/ G 加工助剂（CS-05 同型）/ H 抗菌（CS-06）/ I 多用途（CS-07, CS-08, CS-09, CS-10, CS-11, CS-14, CS-15）。长尾物质名录（§172.515、§172.510 主体）为**不可逐字引用区**，由 CS-12 统一承担导航规则。
