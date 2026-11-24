# 候选池：案例提取器 | 来源 21 CFR Part 101 eCFR 2026-11-05 | 检索式取块

> 取材路径：以 `e.g.` / `for example` / `such as` / `WARNING` / `shall bear the following` / `model health claim` / 具体产品名 / 数值场景为锚词，Grep 命中后回读 chunk-01/02/05/06/07/08/09 段落；chunk-04（§101.12 RACC 表）只读开头 120 行。
> 本件的「案例」＝法规正文亲自给出的**规定措辞、模型句式、阈值示例、豁免适用场景、请愿材料清单**（联邦法规无叙事案例），供能力卡 A1「照着做」段取用。
> 引用纪律：全部英文引用逐字取自 `source-cfr-part101-2026.md`（归一化空白后可命中），未凭记忆补写；`§ 101.12` Table 1/Table 2 数值与 Appendix B/C/D 的 Nutrition Facts 图形版式属**不可逐字引用区**，只写「产品类别 → RACC → label statement」对应关系（见 CAND-CS-05）。
> 条款号一律写〔§ 101.xxx〕，pdf-page 为转换件 `<!-- pdf-page N -->` 标记对应页。

---

### CAND-CS-01: PDP 主展示面面积的三套法定计算公式
- 条款出处：〔§ 101.1〕pdf-page 2
- 原文引用（英文逐字，≤100 词/段）：
> (a) In the case of a rectangular package where one entire side properly can be considered to be the principal display panel side, the product of the height times the width of that side; (b) In the case of a cylindrical or nearly cylindrical container, 40 percent of the product of the height of the container times the circumference; (c) In the case of any otherwise shaped container, 40 percent of the total surface of the container
> In the case of cylindrical or nearly cylindrical containers, information required by this part to appear on the principal display panel shall appear within that 40 percent of the circumference which is most likely to be displayed, presented, shown, or examined under customary conditions of display for retail sale.
- 场景（这是一件什么事、谁要用）：包装设计师/法规事务要给罐装、瓶装、异形盒食品确定「主展示面有多大、强制信息必须落在哪一块」。这不是视觉直觉，是法定公式；圆柱容器尤其易错（不是整圈面积，是 40% 周长带）。
- 可照抄的动作/措辞：矩形＝高×宽；圆柱/近圆柱＝40%×高×周长；其他形状＝40%×总表面积（有明显主展示面如三角/圆形干酪顶面则取整面）；计算时排除顶面、底面、罐 flange、瓶肩瓶颈；圆柱容器强制信息须落在「最可能被展示的那 40% 周长」内。
- 可回答的新问题：一个圆柱形饮料罐的净含量字号该按多大面积算？强制信息能否放在罐背面那半圈？PDP 面积要不要把瓶肩算进去？
- 建议归属子卡（五选一）：基础架构

### CAND-CS-02: 配料表「集体名 + 括号内具体名」的逐字示例
- 条款出处：〔§ 101.4〕pdf-page 8–9
- 原文引用（英文逐字，≤100 词/段）：
> the term “hydrogenated” may precede the term(s) describing the blend, e.g., “hydrogenated vegetable oil (soybean, cottonseed, and palm oils)”, rather than preceding the name of each individual fat and/or oil
> Ingredients that act as leavening agents in food may be declared in the ingredient statement by stating the specific common or usual name of each individual leavening agent in parentheses following the collective name “leavening”, e.g., “leavening (baking soda, monocalcium phosphate, and calcium carbonate)”.
> Such ingredients shall be identified by words indicating that they may not be present, such as “or”, “and/or”, “contains one or more of the following:”, e.g., “vegetable oil shortening (contains one or more of the following: cottonseed oil, palm oil, soybean oil)”.
- 场景（这是一件什么事、谁要用）：配方含多种油脂/膨松剂/酵母营养剂/面团改良剂的食品厂，在写配料表时判断「能不能用集合名简写、括号里要不要按重量降序、可能不存在的原料怎么标」。
- 可照抄的动作/措辞：用 `“______ shortening”` / `“blend of ______ oils”` + 括号内逐个通用名；完全氢化把 `hydrogenated` 放在集合名前（不必逐个加）；对「有时用有时不用」的原料加 `contains one or more of the following:`；膨松剂写 `leavening (…)`、酵母营养剂写 `yeast nutrients (…)`、面团改良剂写 `dough conditioners (…)`，括号内按 predominance 降序（除非常量模式无法保持）。
- 可回答的新问题：混合植物油能不能只写「vegetable oil」？「partially hydrogenated」该标在哪？配方随批次变化的油脂如何合法列名？
- 建议归属子卡（五选一）：基础架构

### CAND-CS-03: 自动售货机食品的卡路里声明舍入与标注
- 条款出处：〔§ 101.8〕pdf-page 18
- 原文引用（英文逐字，≤100 词/段）：
> To the nearest 5-calorie increment up to and including 50 calories and 10-calorie increment above 50 calories, except that amounts less than 5 calories may be expressed as zero.
> The term “Calories” or “Cal” must appear adjacent to the caloric content value for each food in the vending machine.
> The calorie declaration for a packaged food must include the total calories present in the packaged food, regardless of whether the packaged food contains a single serving or multiple servings.
- 场景（这是一件什么事、谁要用）：自动售货机运营商（≥20 台且自愿注册受 ACA §4205 约束，或买家购前无法看到 Nutrition Facts 的机器）要在选购前把卡路里显示出来。
- 可照抄的动作/措辞：≤50 cal 取最近 5-cal 增量，>50 cal 取最近 10-cal 增量，<5 cal 可写 0；数值旁必须紧邻 `Calories` 或 `Cal`；包装食品按「整包总卡路里」标（不论单份多份），可另自愿加每份；现调饮品（咖啡/热巧/茶加糖奶）按每个选项或最终成品标。
- 可回答的新问题：一包 47 cal 的售货机薯片该标 45 还是 50？「Cal」缩写合法吗？多份包装标总热量还是单份热量？
- 建议归属子卡（五选一）：营养标签与份量

### CAND-CS-04: serving size 的 household 度量、舍入与份数示例
- 条款出处：〔§ 101.9(b)〕pdf-page 24–25
- 原文引用（英文逐字，≤100 词/段）：
> serving size may be declared in ounce and fluid ounce, in parenthesis, following the metric measure separated by a slash where other common household measures are used as the primary unit for serving size, e.g., 1 slice (28 g/1 oz) for sliced bread.
> The gram or milliliter quantity equivalent to the household measure should be rounded to the nearest whole number except for quantities that are less than 5 g (mL). The gram (mL) quantity between 2 and 5 g (mL) should be rounded to the nearest 0.5 g (mL) and the g (mL) quantity less than 2 g (mL) should be expressed in 0.1-g (mL) increments.
> Rounding should be indicated by the use of the term about (e.g., about 2 servings, about 3.5 servings).
- 场景（这是一件什么事、谁要用）：给切片面包、浓缩汤、随机重量干酪、腌樱桃等定 Nutrition Facts 的 serving size 与「每容器份数」，并做 metric↔household 换算与舍入。
- 可照抄的动作/措辞：主单位用 household measure，格式 `1 slice (28 g/1 oz)`；克/毫升 <5 时按 <2→0.1 增量、2–5→0.5 舍入；份数 2–5 之间取 0.5 并加 `about`；缩写固定 `tbsp / tsp / g / mL / oz / fl oz`；只加水即可复水且营养不变的可写 `(e.g., 1⁄2 cup (120 mL) concentrated soup (makes 1 cup prepared))`；份量须与净含量 metric 一致。
- 可回答的新问题：面包一片 28 g 该怎么并列公制与英制？每容器 2.5 份怎么写？「varied」什么时候能用？
- 建议归属子卡（五选一）：营养标签与份量

### CAND-CS-05: RACC 表的原则与「产品类别 → RACC → label statement」对应关系
- 条款出处：〔§ 101.12〕pdf-page 82–83
- 原文引用（英文逐字，≤100 词/段）：
> The reference amount is based on the major intended use of the food (e.g., milk as a beverage and not as an addition to cereal).
> The reference amounts for products that are consumed as an ingredient of other foods, but that may also be consumed in the form in which they are purchased (e.g., butter), are based on use in the form purchased.
> Because they reflect the amount customarily consumed, the reference amount and, in turn, the serving size declared on the product label are based on only the edible portion of food, and not bone, seed, shell, or other inedible components.
- 场景（这是一件什么事、谁要用）：判断某产品该查 Table 1 还是 Table 2、按「主要预期用途」还是「购买形态」取 RACC，再由 RACC 推 serving size 与声称资格。
- 可照抄的动作/措辞：**〔不可逐字引用区〕**§101.12 的 Table 1（婴幼儿/幼儿）/ Table 2（一般食品）共约 113 页是流式列值，表头脚注逐页重复、列可能错列，且 Appendix B/C/D 为图形版式——一律**只写「产品类别 → RACC → label statement」对应关系，回原表核对快照日期与 FR citation，不得逐字引表格数值或版式**。叙述层原则可引用：按主要预期用途、按可食部分、按购买形态（butter 例）、婴儿/≤4 岁儿童专用 RACC 仅在专为该人群配方/加工时使用。
- 可回答的新问题：butter 既可直接吃又做配料，RACC 按哪个用途？带骨/带壳食品算不算进份量？「label statement」栏的 `__ cup(s) (__ g)` 是示例还是强制措辞？
- 建议归属子卡（五选一）：营养标签与份量

### CAND-CS-06: 相对声称「modified + 比较句」的逐字句式
- 条款出处：〔§ 101.13(k)〕pdf-page 203
- 原文引用（英文逐字，≤100 词/段）：
> The term “modified” may be used in the statement of identity of a food that bears a relative claim that complies with the requirements of this part, followed immediately by the name of the nutrient whose content has been altered (e.g., “Modified fat cheesecake”). This statement of identity must be immediately followed by the comparative statement such as “Contains 35 percent less fat than ______.”
> A relative claim for decreased levels of a nutrient may not be made on the label or in labeling of a food if the nutrient content of the reference food meets the requirement for a “low” claim for that nutrient (e.g., 3 g fat or less).
- 场景（这是一件什么事、谁要用）：厂商改了配方想写「减脂/低脂」类相对声称，审查品名与紧跟的比较声明是否合规、参照食品是否本身已「low」（低到不能再做相对声称）。
- 可照抄的动作/措辞：品名格式 `Modified fat cheesecake` → 必须紧接 `Contains 35 percent less fat than ______.`；参照食品的营养水平若已满足 `low`（如 `3 g fat or less`），则**不得**再做该营养素的减少型相对声称。
- 可回答的新问题：「Modified fat + 含 35% 少脂」之间能不能插品牌名？参照物本身是低脂食品时还能说「less fat」吗？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-07: 「reduced fat」逐词阈值与标注示例
- 条款出处：〔§ 101.62(b)(4)〕pdf-page 261–262
- 原文引用（英文逐字，≤100 词/段）：
> The terms “reduced fat,” “reduced in fat,” “fat reduced,” “less fat,” “lower fat,” or “lower in fat” may be used on the label or in the labeling of foods, except meal products as defined in § 101.13(l) and main dish products as defined in § 101.13(m), provided that:
> The food contains at least 25 percent less fat per reference amount customarily consumed than an appropriate reference food as described in § 101.13(j)(1); and
> The identity of the reference food and the percent (or fraction) that the fat differs between the two foods and are declared in immediate proximity to the most prominent such claim (e.g., “reduced fat—50 percent less fat than our regular brownies”); and
> Quantitative information comparing the level of fat in the product per labeled serving with that of the reference food that it replaces (e.g., “Fat content has been reduced from 8 g to 4 g per serving.”) is declared adjacent to the most prominent claim or to the nutrition label
- 场景（这是一件什么事、谁要用）：饼干/布朗尼/菠菜蛋奶酥等做「减脂」声称，需要同时给出阈值、参照食品身份、百分比差异、定量对比三件套。
- 可照抄的动作/措辞：可用词表 `reduced fat / reduced in fat / fat reduced / less fat / lower fat / lower in fat`；门槛 `at least 25 percent less fat per RACC`；示例 `reduced fat—50 percent less fat than our regular brownies` 与 `Fat content has been reduced from 8 g to 4 g per serving.`；meal/main dish 产品改按 `25 percent less fat per 100 g`（示例 `33 percent less fat per 3 oz than our regular spinach souffle`）。
- 可回答的新问题：标了「50% less fat」还必须在旁边写 8 g→4 g 的定量对比吗？参照食品是自家常规款还是同类通用款？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-08: 「light/lite」的定量对比与钠减示例
- 条款出处：〔§ 101.56(b)(c)〕pdf-page 250–251
- 原文引用（英文逐字，≤100 词/段）：
> The identity of the reference food and the percent (or fraction) that the calories and the fat were reduced are declared in immediate proximity to the most prominent such claim, (e.g., “1/3 fewer calories and 50 percent less fat than our regular cheese cake”);
> Quantitative information comparing the level of calories and fat content in the product per labeled serving size with that of the reference food that it replaces (e.g., “lite cheesecake—200 calories, 4 grams (g) fat per serving; regular cheesecake—300 calories, 8 g fat per serving”) is declared adjacent to the most prominent claim or to the nutrition label
> The identity of the reference food and the percent (or fraction) that the sodium was reduced shall be declared in immediate proximity to the most prominent such claim (e.g., 50 percent less sodium than our regular soy sauce); and
> Quantitative information comparing the level of sodium per labeled serving size with that of the reference food that it replaces (e.g., “lite soy sauce 500 milligrams (mg) sodium per serving; regular soy sauce 1,000 mg per serving”) is declared adjacent to the most prominent claim or to the nutrition label
- 场景（这是一件什么事、谁要用）：芝士蛋糕、酱油等用 `light/lite` 或 `lite in sodium`，须先判「≥50% 热量来自脂肪」走哪条门槛，再配齐比较声明与定量对比。
- 可照抄的动作/措辞：高脂基准（≥50% 热量来自脂肪）→ 脂肪减 ≥50%；否则 → 热量减 ≥1/3 或脂肪减 ≥50%；示例 `1/3 fewer calories and 50 percent less fat than our regular cheese cake`、`lite cheesecake—200 calories, 4 grams (g) fat per serving; regular cheesecake—300 calories, 8 g fat per serving`、`50 percent less sodium than our regular soy sauce`、`lite soy sauce 500 milligrams (mg) sodium per serving; regular soy sauce 1,000 mg per serving`；标注食品 <40 cal 或 <3 g fat per RACC 时可免写百分比降幅。
- 可回答的新问题：低脂基准食品能不能再叫「light」？「lite in sodium」的 `in sodium` 必须紧挨 `lite` 吗？定量对比放在营养标签旁算不算合规？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-09: 「通常不算 / 算」隐含营养素含量声称的逐字示例
- 条款出处：〔§ 101.65(b)(c)〕pdf-page 273
- 原文引用（英文逐字，≤100 词/段）：
> A claim about the presence of an ingredient that is perceived to add value to the product, e.g., “made with real butter,” “made with whole fruit,” or “contains honey,”
> Claims about the food or an ingredient therein that suggest that a nutrient or an ingredient is absent or present in a certain amount (e.g., “high in oat bran”) are implied nutrient content claims and must comply with paragraph (a) of this section.
> The phrases “contains the same amount of [nutrient] as a [food]” and “as much [nutrient] as a [food]” may be used on the label or in the labeling of foods, provided that the amount of the nutrient in the reference food is enough to qualify that food as a “good source” of that nutrient, and the labeled food, on a per serving basis, is an equivalent, good source of that nutrient (e.g., “as much fiber as an apple,” “Contains the same amount of Vitamin C as an 8 oz glass of orange juice.”).
> A statement of identity that names as a characterizing ingredient, an ingredient associated with a nutrient benefit (e.g., “corn oil margarine,” “oat bran muffins,” or “whole wheat bagels”), unless such claim is made in a context in which label or labeling statements, symbols, vignettes, or other forms of communication suggest that a nutrient is absent or present in a certain amount; and
- 场景（这是一件什么事、谁要用）：审核看似 innocuous 的营销语（`made with real butter`、`100 percent milk free`、`high in oat bran`、`as much fiber as an apple`）是否构成 implied claim 而触发 §101.13 全套义务；这是最易漏判的一类。
- 可照抄的动作/措辞：白名单式「一般不算」——过敏/宗教/素食原因的 `100 percent milk free`、`contains no preservatives`、`no artificial colors`、`made with real butter`、`corn oil`、`oat bran muffins`（前提：上下文无符号/vignette 暗示某营养素含量）；黑名单式「算」——`high in oat bran`、`as much fiber as an apple`、`Contains the same amount of Vitamin C as an 8 oz glass of orange juice.`（须参照物够 `good source` 且本品每份等效）。
- 可回答的新问题：品名里带「oat bran」会不会被当成高纤声称？「as much Vitamin C as orange juice」需满足什么定量前提？品牌名/心形符号算不算隐含声称？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-10: 健康声称请愿书的材料清单与模型声称要求
- 条款出处：〔§ 101.70〕pdf-page 292–293
- 原文引用（英文逐字，≤100 词/段）：
> B. Summary of scientific data. The summary of scientific data provides the basis upon which authorizing a health claim can be justified as providing the health benefit. The summary must establish that, based on the totality of publicly available scientific evidence (including evidence from well-designed studies conducted in a manner which is consistent with generally recognized scientific procedures and principles), there is significant scientific agreement among experts qualified by scientific training and experience to evaluate such claims, that the claim is supported by such evidence.
> D. Model health claim. One or more model health claims that represent label statements that may be used on a food label or in labeling for a food to characterize the relationship between the substance in a food to a disease or health-related condition that is justified by the summary of scientific data provided in section C of the petition. The model health claim shall include:
> E. The petition shall include the following attachments: 1. Copies of any computer literature searches done by the petitioner (e.g., Medline). 2. Copies of articles cited in the literature searches and other information as follows:
> F. The petitioner is required to submit either a claim for categorical exclusion under § 25.30 or § 25.32 of this chapter or an environmental assessment under § 25.40 of this chapter.
> Within 100 days of the date of receipt of the petition, FDA will notify the petitioner by letter that the petition has either been filed for comprehensive review or denied.
- 场景（这是一件什么事、谁要用）：企业要为一种新物质/新关系申请健康声称授权（SSA 门槛），或监管机构审查请愿是否齐备；§101.69 另管营养素含量声称请愿（新词/同义词/品牌名隐含声称）。
- 可照抄的动作/措辞：按 lettered headings 分页提交 `A. Preliminary Requirements`（物质符合 §101.14(b)、成分 GRAS/食品添加剂/prior sanction 依据）、`B. Summary of Scientific Data`（须论证 significant scientific agreement，并回答最佳摄入量/不良反应水平/特殊人群/其他营养因素四问）、`C. Analytical Data`（AOAC 方法或自报 assay + 效度数据）、`D. Model Health Claim`、`E. Attachments`（Medline 检索副本、所引文献全文、不利信息、美国人群信息）、`F.` 环境排除声明或评估；另附 signed balanced submission 声明、按 §101.69 提交原件+一份副本或 ASCII 磁盘、外文附英译。FDA 15 天回执、100 天内 filed 或 denied。
- 可回答的新问题：请愿书里「模型健康声称」必须包含哪两项内容？没有 AOAC 方法时要补什么？请愿被 deemed denied 的时限是多久？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-11: 钙/维生素 D 与骨质疏松的模型健康声称
- 条款出处：〔§ 101.72(e)(f)〕pdf-page 297
- 原文引用（英文逐字，≤100 词/段）：
> Model health claims. The following model health claims may be used in food labeling to describe the relationship between calcium and osteoporosis: Adequate calcium throughout life, as part of a well-balanced diet, may reduce the risk of osteoporosis. Adequate calcium as part of a healthful diet, along with physical activity, may reduce the risk of osteoporosis in later life.
> Model additional health claims for calcium and vitamin D. The following model health claims may be used in food labeling to describe the relationship between calcium, vitamin D, and osteoporosis: Adequate calcium and vitamin D throughout life, as part of a well-balanced diet, may reduce the risk of osteoporosis.
- 场景（这是一件什么事、谁要用）：高钙食品/强化食品想写「预防骨质疏松」类健康声称，必须落在已授权模型措辞内，不能自行改写因果强度。
- 可照抄的动作/措辞：逐字用 `Adequate calcium throughout life, as part of a well-balanced diet, may reduce the risk of osteoporosis.` / `Adequate calcium as part of a healthful diet, along with physical activity, may reduce the risk of osteoporosis in later life.`；钙+维 D 版用 `Adequate calcium and vitamin D throughout life, as part of a well-balanced diet, may reduce the risk of osteoporosis.`；可用 `build and maintain good bone health` 表达峰值骨量概念。
- 可回答的新问题：把 `may reduce the risk` 改成 `prevents` 行不行？只加维生素 D 不提钙能沿用同一句吗？「later life」措辞可省吗？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-12: 果蔬谷物可溶性纤维与心脏病风险模型声称
- 条款出处：〔§ 101.77(e)〕pdf-page 308
- 原文引用（英文逐字，≤100 词/段）：
> Model health claims. The following model health claims may be used in food labeling to characterize the relationship between diets low in saturated fat and cholesterol and high in fruits, vegetables, and grain products that contain soluble fiber: (1) Diets low in saturated fat and cholesterol and rich in fruits, vegetables, and grain products that contain some types of dietary fiber, particularly soluble fiber, may reduce the risk of heart disease, a disease associated with many factors.
> (2) Development of heart disease depends on many factors. Eating a diet low in saturated fat and cholesterol and high in fruits, vegetables, and grain products that contain fiber may lower blood cholesterol levels and reduce your risk of heart disease.
- 场景（这是一件什么事、谁要用）：全谷物/果蔬产品做「降低心脏病风险」健康声称，须用已授权模型句并保留「多因素疾病」限定语。
- 可照抄的动作/措辞：逐字用模型 (1)/(2)；必须带 `a disease associated with many factors` / `depends on many factors`；可用 `dietary fiber` / `some dietary fibers` / `some fibers` / `soluble fiber` 等法定术语；资格前提含 `without fortification, at least 0.6 g of soluble fiber per reference amount`。
- 可回答的新问题：删掉「many factors」限定语会怎样？强化添加的可溶性纤维算不算资格？声称里能不能点名具体纤维来源？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-13: §101.81 填空式模型健康声称模板
- 条款出处：〔§ 101.81(e)〕pdf-page 323
- 原文引用（英文逐字，≤100 词/段）：
> Soluble fiber from foods such as [name of soluble fiber source from paragraph (c)(2)(ii) of this section and, if desired, the name of food product], as part of a diet low in saturated fat and cholesterol, may reduce the risk of heart disease. A serving of [ name of food] supplies ________ grams of the [grams of soluble fiber specified in paragraph (c)(2)(i)(G) of this section] soluble fiber from [name of the soluble fiber source from paragraph (c)(2)(ii) of this section] necessary per day to have this effect.
> Diets low in saturated fat and cholesterol that include [________ grams of soluble fiber specified in paragraph (c)(2)(i)(G) of this section] of soluble fiber per day from [name of soluble fiber source from paragraph (c)(2)(ii) of this section and, if desired, the name of the food product] may reduce the risk of heart disease. One serving of [name of food] provides ________ grams of this soluble fiber.
- 场景（这是一件什么事、谁要用）：燕麦/大麦 β-葡聚糖、洋车前子壳等「特定来源可溶性纤维」产品做健康声称，法规给的是带方括号填空的模板，不是自由造句。
- 可照抄的动作/措辞：按模板填 `[name of soluble fiber source]`、`[name of food]`、`________ grams`（对应 (c)(2)(i)(G) 的每日摄入量，如 `3 g or more per day of β-glucan soluble fiber from either whole oats or barley` 或 `7 g or more per day of soluble fiber from psyllium seed husk`）；保留 `as part of a diet low in saturated fat and cholesterol` 与 `may reduce the risk of heart disease`；每份提供量必须填空且真实。
- 可回答的新问题：方括号内容能不能改成营销词？每日 3 g / 7 g 两个门槛分别对应哪种纤维来源？模板里 `supplies` 与 `provides` 两句可否只用其一？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-14: 大豆蛋白 25 g/日 模型健康声称
- 条款出处：〔§ 101.82(e)〕pdf-page 326
- 原文引用（英文逐字，≤100 词/段）：
> 25 grams of soy protein a day, as part of a diet low in saturated fat and cholesterol, may reduce the risk of heart disease. A serving of [name of food] supplies ____ grams of soy protein.
> Diets low in saturated fat and cholesterol that include 25 grams of soy protein a day may reduce the risk of heart disease. One serving of [name of food] provides ____ grams of soy protein.
- 场景（这是一件什么事、谁要用）：豆制品/大豆蛋白强化食品做 CHD 风险声称，须用已授权模型句并填每份大豆蛋白克数。
- 可照抄的动作/措辞：逐字用两句之一，数字 `25 grams of soy protein a day` 与 `as part of a diet low in saturated fat and cholesterol` 不可改；`[name of food]` 与 `____ grams` 按实填写；仍须先过 §101.14 disqualifying level 门槛。
- 可回答的新问题：把 25 g 写成「约 25 g」行不行？产品每份只提供 6 g 能否仍用此句？与 §101.81 模板能否混用？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-15: 植物甾醇/甾烷醇酯模型健康声称与每日剂量
- 条款出处：〔§ 101.83(e)〕pdf-page 329–330
- 原文引用（英文逐字，≤100 词/段）：
> Foods containing at least 0.65 g per serving of plant sterol esters, eaten twice a day with meals for a daily total intake of at least 1.3 g, as part of a diet low in saturated fat and cholesterol, may reduce the risk of heart disease. A serving of [name of the food] supplies ______grams of vegetable oil sterol esters.
> Foods containing at least 1.7 g per serving of plant stanol esters, eaten twice a day with meals for a total daily intake of at least 3.4 g, as part of a diet low in saturated fat and cholesterol, may reduce the risk of heart disease. A serving of [name of the food] supplies ______grams of plant stanol esters.
- 场景（这是一件什么事、谁要用）：添加植物甾醇酯/甾烷醇酯的人造黄油、果汁、膳食补充剂做 CHD 风险声称，须同时满足每份下限、每日两餐总量、低饱和脂低胆固醇饮食限定。
- 可照抄的动作/措辞：甾醇酯 `at least 0.65 g per serving` + `twice a day with meals` + `daily total intake of at least 1.3 g`；甾烷醇酯 `at least 1.7 g per serving` + `at least 3.4 g`；逐字带 `as part of a diet low in saturated fat and cholesterol`；填空 `[name of the food]` 与 `______grams`；物质名用 `plant sterol esters` / `plant stanol esters`（唯一来源为植物油时另有 `vegetable oil sterol esters` 用语）。
- 可回答的新问题：0.65 g 与 1.7 g 分别对应哪一类酯？「twice a day with meals」能不能省？软胶囊膳食补充剂适用哪套剂量？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-16: 自加压容器与卤代烃/烃推进剂的逐字警示
- 条款出处：〔§ 101.17(a)(b)〕pdf-page 211
- 原文引用（英文逐字，≤100 词/段）：
> WARNING—Avoid spraying in eyes. Contents under pressure. Do not puncture or incinerate. Do not store at temperature above 120 °F. Keep out of reach of children.
> WARNING—Use only as directed. Intentional misuse by deliberately concentrating and inhaling the contents can be harmful or fatal.
> The warning required by paragraph (b)(1) of this section is not required for the following products: (i) Products expelled in the form of a foam or cream, which contain less than 10 percent propellant in the container.
- 场景（这是一件什么事、谁要用）：喷雾奶油、气雾式食品等自加压容器贴警示；含卤代烃/烃推进剂时须**叠加**第二句警示。
- 可照抄的动作/措辞：(a) 逐字 `WARNING—Avoid spraying in eyes. Contents under pressure. Do not puncture or incinerate. Do not store at temperature above 120 °F. Keep out of reach of children.`；儿童用可加 `except under adult supervision`，玻璃容器 `puncture` 可换 `break`，非喷雾产品可删 `Avoid spraying in eyes`；(b) 逐字 `WARNING—Use only as directed. Intentional misuse by deliberately concentrating and inhaling the contents can be harmful or fatal.`；(b) 豁免：泡沫/奶油且推进剂 <10%、有物理屏障、净含量 <2 oz 定量阀、净含量 <0.5 oz。
- 可回答的新问题：120 °F 储存上限是哪一款的专属措辞？玻璃瓶喷雾该改哪个词？泡沫型产品为什么可以免第二句？
- 建议归属子卡（五选一）：特定品类与警示

### CAND-CS-17: 极低热量蛋白膳食的 400 Calories 警示与豁免 Notice
- 条款出处：〔§ 101.17(d)〕pdf-page 212
- 原文引用（英文逐字，≤100 词/段）：
> WARNING: Very low calorie protein diets (below 400 Calories per day) may cause serious illness or death. Do Not Use for Weight Reduction in Such Diets Without Medical Supervision. Not for use by infants, children, or pregnant or nursing women.
> Notice: For weight reduction, use only as directed in the accompanying diet plan (the name and specific location in labeling of the diet plan may be included in this statement in place of “accompanying diet plan”). Do not use in diets supplying less than 400 Calories per day without medical supervision.
> NOTICE: Use this product as a food supplement only. Do not use for weight reduction.
- 场景（这是一件什么事、谁要用）：液体/粉/片/胶囊蛋白减肥产品（>50% 热量来自蛋白且用于减重）；若作为 ≥400 Calories 均衡膳食计划的一部分，可改用 Notice 而非 WARNING；非减重用途的蛋白补充剂又用第三句。
- 可照抄的动作/措辞：WARNING 逐字（含 `below 400 Calories per day`）；(d)(2) 豁免 Notice 逐字；(d)(3) 非减重 `NOTICE: Use this product as a food supplement only. Do not use for weight reduction.`；三句警示/notice 须在 PDP 及所有 labeling 显著标示；散装仅供再加工、不面向消费者的可免。
- 可回答的新问题：400 Calories 是警示触发线还是豁免线？「搭配饮食计划」版本能删掉 WARNING 吗？三款措辞能不能互相借用？
- 建议归属子卡（五选一）：特定品类与警示

### CAND-CS-18: 含铁膳食补充剂与 psyllium 食品的逐字警示
- 条款出处：〔§ 101.17(e)(f)〕pdf-page 213
- 原文引用（英文逐字，≤100 词/段）：
> WARNING: Accidental overdose of iron-containing products is a leading cause of fatal poisoning in children under 6. Keep this product out of reach of children. In case of accidental overdose, call a doctor or poison control center immediately.
> NOTICE: This food should be eaten with at least a full glass of liquid. Eating this product without enough liquid may cause choking. Do not eat this product if you have difficulty in swallowing.
> The statement shall be preceded by the word “NOTICE” in capital letters.
- 场景（这是一件什么事、谁要用）：固体口服含铁补充剂（片/胶囊）；以及含干/未充分水化洋车前子壳且作可溶性纤维健康声称的食品。
- 可照抄的动作/措辞：含铁 WARNING 逐字，位置＝即时容器信息面板（零售包装非即时容器时还要在零售包装信息面板），并 `set off in a box by use of hairlines`；psyllium NOTICE 逐字，`NOTICE` 全大写，常规食品形态若不形成黏性团块可免。
- 可回答的新问题：含铁警示为什么强制「hairlines 框」？unit-dose 包装无 label 时警示放哪？psyllium 豁免的判据是什么？
- 建议归属子卡（五选一）：特定品类与警示

### CAND-CS-19: 未巴氏杀菌果汁的逐字警示（与 Part 120 接口）
- 条款出处：〔§ 101.17(g)〕pdf-page 214
- 原文引用（英文逐字，≤100 词/段）：
> WARNING: This product has not been pasteurized and, therefore, may contain harmful bacteria that can cause serious illness in children, the elderly, and persons with weakened immune systems.
> The word “WARNING” shall be capitalized and shall appear in bold type.
> The warning statement required by paragraph (g)(2) of this section, when on a label, shall be set off in a box by use of hairlines.
> The warning statement required by this paragraph (g) shall not apply to juice that is not for distribution to retail consumers in the form shipped and that is for use solely in the manufacture of other foods or that is to be processed, labeled, or repacked at a site other than originally processed, provided that for juice that has not been processed in the manner described in paragraph (g)(7) of this section, the lack of such processing is disclosed in documents accompanying the juice, in accordance with the practice of the trade.
- 场景（这是一件什么事、谁要用）：未按 (g)(7) 工艺处理（对应 §120.24 的 5-log 病原减少）的果汁、或含此类果汁的饮料，须在信息面板/PDP 带警示；这是「工艺义务 → 标签义务 → 检查取证」三层接口的标签层。
- 可照抄的动作/措辞：逐字用 WARNING 句；`WARNING` 全大写加粗、其余按 (g)(4) 在信息面板或 PDP 显著、label 上用 hairlines 框；豁免＝不面向零售消费者、仅供再制造/异地加工贴标改包，且**随货单据须披露未处理**；(g)(7) 工艺须达到 shelf life 内至少 5-log 相关微生物减少。警示声明不替代 5-log 工艺，做了 5-log 也不自动免全部标签义务。
- 可回答的新问题：做了 5-log 还要不要贴这句？散装运给另一家厂复配能不能免警示？豁免时随货文件要写什么？WARNING 排版有哪些硬性要求？
- 建议归属子卡（五选一）：特定品类与警示

### CAND-CS-20: 带壳蛋的安全操作声明
- 条款出处：〔§ 101.17(h)〕pdf-page 214
- 原文引用（英文逐字，≤100 词/段）：
> SAFE HANDLING INSTRUCTIONS: To prevent illness from bacteria: keep eggs refrigerated, cook eggs until yolks are firm, and cook foods containing eggs thoroughly.
> The label statement required by paragraph (h)(1) of this section shall appear prominently and conspicuously, with the words “SAFE HANDLING INSTRUCTIONS” in bold type, on the principal display panel, the information panel, or on the inside of the lid of egg cartons. If this statement appears on the inside of the lid, the words “Keep Refrigerated” must appear on the principal display panel or information panel.
- 场景（这是一件什么事、谁要用）：无论州际还是州内销售的带壳蛋，均须在标签/盒盖内侧带安全操作声明。
- 可照抄的动作/措辞：逐字 `SAFE HANDLING INSTRUCTIONS: To prevent illness from bacteria: keep eggs refrigerated, cook eggs until yolks are firm, and cook foods containing eggs thoroughly.`；`SAFE HANDLING INSTRUCTIONS` 加粗，位置＝PDP / 信息面板 / 盒盖内侧；若放盒盖内侧，PDP 或信息面板另须写 `Keep Refrigerated`；用 hairlines 框。
- 可回答的新问题：声明放盒盖内侧时外面还必须写什么？经杀菌处理过的带壳蛋是否可免？州内销售能不能不标？
- 建议归属子卡（五选一）：特定品类与警示

### CAND-CS-21: 果汁百分比声明的格式与「100 percent juice」判定
- 条款出处：〔§ 101.30(b)(i)〕pdf-page 224–225、227
- 原文引用（英文逐字，≤100 词/段）：
> If the beverage contains fruit or vegetable juice, the percentage shall be declared by the words “Contains __ percent (or %) ______ juice” or “__ percent (or %) juice,” or a similar phrase, with the first blank filled in with the percentage expressed as a whole number not greater than the actual percentage of the juice and the second blank (if used) filled in with the name of the particular fruit or vegetable (e.g., “Contains 50 percent apple juice” or “50 percent juice”).
> If the beverage contains less than 1 percent juice, the total percentage juice shall be declared as “less than 1 percent juice” or “less than 1 percent ______ juice” with the blank filled in with the name of the particular fruit or vegetable.
> If the beverage contains 100 percent juice and also contains non-juice ingredients that do not result in a diminution of the juice soluble solids or, in the case of expressed juice, in a change in the volume, when the 100 percent juice declaration appears on a panel of the label that does not also bear the ingredient statement, it must be accompanied by the phrase “with added ______,”
> Juices directly expressed from a fruit or vegetable (i.e., not concentrated and reconstituted) shall be considered to be 100 percent juice and shall be declared as “100 percent juice.”
- 场景（这是一件什么事、谁要用）：果汁饮料、含少量果汁的调味饮料、软饮料判定要不要标百分比、标成什么句式；与 §101.17(g) 未巴氏警示并列适用。
- 可照抄的动作/措辞：`Contains __ percent (or %) ______ juice` / `__ percent (or %) juice`，百分比取**不超过实际值**的整数；示例 `Contains 50 percent apple juice` / `50 percent juice`；<1% 写 `less than 1 percent juice`；100% 但含非果汁成分且声明所在面无配料表时加 `with added ______`（如 `100% juice with added sweetener`）；直接压榨（非浓缩复原）汁一律 `100 percent juice`；软饮料若名称/标签/广告均不暗示含果汁则**无需**百分比声明。
- 可回答的新问题：标 50% 但实际 47% 可以吗？只写 `50 percent juice` 不写果名行不行？100% 汁加甜味剂时 `with added` 何时可省？
- 建议归属子卡（五选一）：特定品类与警示

### CAND-CS-22: 膳食补充剂结构/功能声明的免责声明逐字措辞
- 条款出处：〔§ 101.93(c)(d)(e)〕pdf-page 332–333
- 原文引用（英文逐字，≤100 词/段）：
> This statement has not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.
> These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.
> The disclaimer shall be placed adjacent to the statement with no intervening material or linked to the statement with a symbol (e.g., an asterisk) at the end of each such statement that refers to the same symbol placed adjacent to the disclaimer specified in paragraphs (c)(1) or (c)(2) of this section.
> Typesize. The disclaimer in paragraph (c) of this section shall appear in boldface type in letters of a typesize no smaller than one-sixteenth inch.
- 场景（这是一件什么事、谁要用）：膳食补充剂标签/小册子/目录里写 structure/function 声明（§403(r)(6)）并主张免于「疾病声称→药品」定性时，必须配免责声明；首次上市后 30 天内还要向 FDA 通知。
- 可照抄的动作/措辞：单条声明用 `This statement has not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.`；多条用复数 `These statements …` 或每条各配一份；位置紧邻无插入材料、或用星号符号链接；每个有该声明的 panel/page 都要出现；不相邻时加框；黑体字不小于 `one-sixteenth inch`；另 §101.93(a) 要求首次营销后 30 天内通知 Office of Dietary Supplement Programs（含厂商名址、声明文本、品牌名等）。
- 可回答的新问题：两条结构功能声明能不能共用一段免责？字号下限是多少？小册子每一页都要印吗？30 天通知包含哪些字段？
- 建议归属子卡（五选一）：特定品类与警示

### CAND-CS-23: gluten-free 的 20 ppm 定量定义与「Contains wheat」星号声明
- 条款出处：〔§ 101.91(a)(3)(b)(3)〕pdf-page 330–331
- 原文引用（英文逐字，≤100 词/段）：
> An ingredient that is a gluten-containing grain (e.g., spelt wheat);
> Any unavoidable presence of gluten in the food bearing the claim in its labeling is below 20 ppm gluten (i.e., below 20 mg gluten per kg of food).
> The wheat has been processed to allow this food to meet the Food and Drug Administration (FDA) requirements for gluten-free foods.
> A food that bears the claim “no gluten,” “free of gluten,” or “without gluten” in its labeling and fails to meet the requirements of paragraph (a)(3) of this section and, if applicable, paragraphs (c)(2) through (4) of this section will be deemed misbranded.
- 场景（这是一件什么事、谁要用）：无麸质声称的定量判定（20 ppm 阈值），以及配料表按 FALCPA 标了 `Contains wheat` 却又想同时标 `gluten-free` 时的强制星号说明；与过敏原 Ed.5 的 allergen-free 声明不同源。
- 可照抄的动作/措辞：阈值 `below 20 ppm gluten (i.e., below 20 mg gluten per kg of food)`；含麸质谷物例 `spelt wheat`、未去麸质衍生 `wheat flour`、去麸质但导致 ≥20 ppm 的 `wheat starch` 均不得；`no gluten / free of gluten / without gluten` 同义受管；若标 `Contains wheat` 又标 `gluten-free`，`wheat` 后须紧跟星号并指向 `The wheat has been processed to allow this food to meet the Food and Drug Administration (FDA) requirements for gluten-free foods.`；合规可用能可靠检出 20 ppm 的科学有效方法。
- 可回答的新问题：20 ppm 是「无添加」还是定量上限？发酵/水解成分怎么验证？标了「Contains wheat」还能写 gluten-free 吗（需什么附加措辞）？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-24: 「fresh」用语的 pasteurized milk / pasta sauce 二分示例
- 条款出处：〔§ 101.95〕pdf-page 334–335
- 原文引用（英文逐字，≤100 词/段）：
> For example, the term “fresh” used to describe pasteurized whole milk is not subject to paragraph (a) of this section because the term does not imply that the food is unprocessed (consumers commonly understand that milk is nearly always pasteurized). However, the term “fresh” to describe pasta sauce that has been pasteurized or that contains pasteurized ingredients would be subject to paragraph (a) of this section because the term implies that the food is not processed or preserved.
> The following do not preclude the food from use of the term “fresh:” (i) The addition of approved waxes or coatings; (ii) The post-harvest use of approved pesticides; (iii) The application of a mild chlorine wash or mild acid wash on produce; or (iv) The treatment of raw foods with ionizing radiation not to exceed the maximum dose of 1 kiloGray in accordance with § 179.26 of this chapter.
> A food meeting the definition in paragraph (a) of this section that is refrigerated is not precluded from use of “fresh” as provided by this section.
- 场景（这是一件什么事、谁要用）：判断是否可用 `fresh / fresh frozen / freshly frozen`，尤其是巴氏杀菌乳（可用）与巴氏杀菌意面酱（不可用）的对照；品牌名与感官修饰词也算「用语」。
- 可照抄的动作/措辞：判据＝该词是否**暗示未加工/未保存**；`fresh`＝raw state、未冷冻、未热加工/未保存（(c) 例外除外）；`fresh frozen / frozen fresh`＝still fresh 时快速冷冻（含 blast-freezing 定义），烫漂不排除；允许项：被批准蜡/涂层、采后农药、温和氯/酸洗、≤1 kiloGray 电离辐射、冷藏；不受本条规管的 `fresh` 由 §403(a) 一般错标条款管。
- 可回答的新问题：巴氏奶写「fresh」为什么合法而意面酱不行？冷藏会不会让食品失去 `fresh` 资格？1 kiloGray 辐照限量是哪一款的？
- 建议归属子卡（五选一）：声称闸门

### CAND-CS-25: 配料表豁免中「亚硫酸盐 10 ppm 可检出」阈值
- 条款出处：〔§ 101.100(a)(4)〕pdf-page 336
- 原文引用（英文逐字，≤100 词/段）：
> any sulfiting agent (sulfur dioxide, sodium sulfite, sodium bisulfite, potassium bisulfite, sodium metabisulfite, and potassium metabisulfite) that has been added to any food or to any ingredient in any food and that has no technical effect in that food will be considered to be present in an insignificant amount only if no detectable amount of the agent is present in the finished food.
> A detectable amount of sulfiting agent is 10 parts per million (ppm or mg/kg) or more of the sulfite in the finished food.
> Compliance with this paragraph (a)(4) will be determined using either: (i) Determination of Sulfite in Food by Liquid Chromatography Tandem Mass Spectrometry; or (ii) AOAC Official Method 990.28.
- 场景（这是一件什么事、谁要用）：判断 incidental additive（存在量不显著、无技术功能效果）能否免于 §403(i)(2) 配料表申报；亚硫酸盐是**独立按 10 ppm 可检出线**判的例外，不因「incidental」自动免。
- 可照抄的动作/措辞：亚硫酸盐清单逐字（sulfur dioxide / sodium sulfite / sodium bisulfite / potassium bisulfite / sodium metabisulfite / potassium metabisulfite）；判据 `10 parts per million (ppm or mg/kg) or more`＝可检出→**须申报**；检测方法二选一（LC-MS/MS 或 AOAC 990.28）；注意 §101.100 免的是**配料表要求**，不是 §101.9 营养标签，也不是 Part 117 主体豁免。
- 可回答的新问题：10 ppm 与 gluten-free 的 20 ppm 是不是同一制度？亚硫酸盐 <10 ppm 就能免配料表吗？用哪个检测方法判定？
- 建议归属子卡（五选一）：豁免与效力层

### CAND-CS-26: 临时标签实验豁免的书面提案 9 项材料清单
- 条款出处：〔§ 101.108(b)(c)〕pdf-page 340–341
- 原文引用（英文逐字，≤100 词/段）：
> Any firm that intends to undertake a labeling experiment that requires exemptions from certain requirements of §§ 101.9 and 105.66 of this chapter should submit a written proposal containing a thorough discussion of each of the following information items that apply to the particular experiment:
> (1) A description of the labeling format to be tested; (2) A statement of the criteria to be used in the experiment for assigning foods to categories, e.g., nutrient or other values defining “low” and “reduced”; (3) A draft of the material to be used in the store, e.g., shelf tags, booklets, posters, etc.;
> The dates on which the experiment will begin and end and on which a written report of analysis of the experimental data will be submitted to FDA, together with a commitment not to continue the experiment beyond the proposed ending date without FDA approval;
> The proposal should be clearly identified as a request for a temporary exemption for purposes of conducting authorized food labeling experiments and submitted as a citizen petition under § 10.30 of this chapter.
> Approval for food labeling experiments will be given by FDA in writing. Foods labeled in violation of existing regulations will be subject to regulatory action unless an FDA-approved exemption to the specific regulation has been granted for that specific product.
- 场景（这是一件什么事、谁要用）：食品企业/行业组织想试新营养标签格式，需要临时豁免 §101.9 / §105.66 的具体要求；必须走 FDA 书面批准，不能自行试。
- 可照抄的动作/措辞：书面提案 9 项＝①待测格式描述 ②分类判据（如定义 `low`/`reduced` 的数值）③店内材料草案（shelf tags/booklets/posters）④起止日期与提交分析报告日期＋不超期承诺 ⑤地理区域 ⑥有效性测量机制 ⑦实验期间向消费者传达被豁免信息的替代方式 ⑧营养特性测定方法 ⑨申请豁免的具体条款号；寄 Dockets Management Staff (HFA-305)，标注为 temporary exemption 请求并按 §10.30 citizen petition 提交；**FDA 书面批准**才生效，且豁免只针对特定法规+特定产品。
- 可回答的新问题：能不能先上架试卖再补申请？提案里「分类判据」举例是什么？没拿到书面批准就改标签会怎样？此豁免与 §101.100 免配料表、§101.9(j) 免营养标签能否互相替代？
- 建议归属子卡（五选一）：豁免与效力层

---

## 自检
- [x] 每条候选都有「建议归属子卡」字段，明确归属五张子卡之一
- [x] 每条都有英文逐字原文引用作为证据（均可在 `source-cfr-part101-2026.md` 归一化空白后命中）
- [x] 表格数值/图形示例（§101.12 Table 1/2、Appendix B/C/D）在 CAND-CS-05 标为不可逐字引用区，只写对应关系
- [x] 不做筛选，宁多勿漏（26 条）
- [x] 覆盖条款：101.1 / 101.4 / 101.8 / 101.9 / 101.12 / 101.13 / 101.17 / 101.30 / 101.56 / 101.62 / 101.65 / 101.70 / 101.72 / 101.77 / 101.81 / 101.82 / 101.83 / 101.91 / 101.93 / 101.95 / 101.100 / 101.108
