# 候选池：框架提取器 | 来源 21 CFR Part 101 eCFR 2026-11-05 | 全量扫描 chunk-01..09

> 说明：本候选池由框架提取器产出，只收「决策框架 / 判定链 / 思维模型 / 分流闸门」，不写能力卡。所有英文引用均逐字取自 `source-cfr-part101-2026.md`（对应分块），引用时已把硬换行归一化为空格，标点与弯引号保留原样，可作为原文子串命中。`pdf-page N` 取转换件中该引用所在位置之前最近的 `<!-- pdf-page N -->` 标记；chunk 起始无标记者按首个标记（pdf-page 3）计，与 BOOK_OVERVIEW「正文始于第 3 页」一致。§101.12 的 Table 1/Table 2 数值、Appendix B/C/D 图形、9 个纯图形页（44/45/51/239/240/344/347/348/351）为不可逐字引用区，只写「回原表核对」类规则。

### CAND-FW-01: PDP 面积「容器形状三分叉」判定链
- 条款出处：〔§ 101.1〕 + pdf-page 3（首段），（a)(b)(c) 同页
- 原文引用（英文逐字，≤100 词/段）：
> The term principal display panel as it applies to food in package form and as used in this part, means the part of a label that is most likely to be displayed, presented, shown, or examined under customary conditions of display for retail sale. The principal display panel shall be large enough to accommodate all the mandatory label information required to be placed thereon by this part with clarity and conspicuousness and without obscuring design, vignettes, or crowding.
> (a) In the case of a rectangular package where one entire side properly can be considered to be the principal display panel side, the product of the height times the width of that side; (b) In the case of a cylindrical or nearly cylindrical container, 40 percent of the product of the height of the container times the circumference; (c) In the case of any otherwise shaped container, 40 percent of the total surface of the container: Provided, however, That where such container presents an obvious “principal display panel” such
> as the top of a triangular or circular package of cheese, the area shall consist of the entire top surface.
> In determining the area of the principal display panel, exclude tops, bottoms, flanges at tops and bottoms of cans, and shoulders and necks of bottles or jars. In the case of cylindrical or nearly cylindrical containers, information required by this part to appear on the principal display panel shall appear within that 40 percent of the circumference which is most likely to be displayed, presented, shown, or examined under customary conditions of display for retail sale.
- 方法论陈述：先按「零售陈列条件下最可能被展示」定性圈出 PDP，再进入面积计算闸门：矩形整面 → 高×宽；圆柱形/近圆柱形 → 高×周长的 40%；其余形状 → 总表面的 40%（但若有「明显主展示面」如三角/圆形奶酪顶面，则改取整面顶面）。算出面积后还有两道收尾：计算面积时排除顶底、罐口翻边、瓶肩瓶颈；圆柱容器的强制信息必须落回那 40% 周长内且落在最可能被展示的弧段。面积数值不是装饰，它直接驱动下游 §101.7(i) 的字号档位与 §101.2 的落位判断。
- 可回答的新问题：一个「方形纸盒但侧面带弧形收腰」的包装该用 (a) 还是 (c)？同一产品换成易拉罐后再算出的 PDP 面积变小，净含量声明的最小字号是否需要同步降级？「封面有醒目顶面的圆柱形奶酪」为什么可以突破 40% 公式？
- 跨域佐证：〔§ 101.7(i)〕按 PDP 面积分四档规定最小字号；〔§ 101.2(b)(c)〕落位与显著性下限同以 PDP 为锚；〔§ 101.1〕alternate PDP 须把强制信息复制到每个 PDP。
- 建议归属子卡：基础架构

### CAND-FW-02: 信息面板「默认右侧 + 三项列举例外」判定链
- 条款出处：〔§ 101.2(a)〕 + pdf-page 3（(1)(2)(3) 在 `pdf-page 3` 标记之后）
- 原文引用（英文逐字，≤100 词/段）：
> The term information panel as it applies to packaged food means that part of the label immediately contiguous and to the right of the principal display panel as observed by an individual facing the principal display panel with the following exceptions:
> (1) If the part of the label immediately contiguous and to the right of the principal display panel is too small to accommodate the necessary information or is otherwise unusable label space, e.g., folded flaps or can ends, the panel immediately contiguous and to the right of this part of the label may be used.
> (2) If the package has one or more alternate principal display panels, the information panel is immediately contiguous and to the right of any principal display panel. (3) If the top of the container is the principal display panel and the package has no alternate principal display panel, the information panel is any panel adjacent to the principal display panel.
- 方法论陈述：先固定观察基准——以「面向 PDP 的人」为视角，默认信息面板是紧邻 PDP 右侧那一块。再依次测试三项列举例外：紧邻右面太小/不可用（折页、罐端）→ 顺延到再右侧那一面；存在一个或多个 alternate PDP → 任一 PDP 的右侧都可作为信息面板；顶面就是 PDP 且无 alternate PDP → 任一与 PDP 相邻的面皆可。三项例外是「条件命中即改判」，不是任选空白面；位置本身是法定相对方位，可开观察项。
- 可回答的新问题：软饮料罐把营养信息印在罐盖是否合法？「右侧」是按人面对货架还是按包装自身朝向定义？有双 PDP 的枕形袋能否把营养标签放在任一 PDP 右边？
- 跨域佐证：〔§ 101.2(b)〕把 §101.4/101.5/101.9/101.13/101.17/101.36/Subpart D 等强制信息统一收拢到 PDP 或信息面板；〔§ 101.2(d)(2)〕盖身分离容器（lid 可作 PDP）另设 placement 例外；〔§ 101.1〕alternate PDP 定义是 (2) 的前置条件。
- 建议归属子卡：基础架构

### CAND-FW-03: 强制信息「PDP 或信息面板二选一」总落位闸门 + 显著性下限
- 条款出处：〔§ 101.2(b)(c)〕 + pdf-page 3
- 原文引用（英文逐字，≤100 词/段）：
> All information required to appear on the label of any package of food under §§ 101.4, 101.5, 101.8, 101.9, 101.13, 101.17, 101.36, subpart D of part 101, and part 105 of this chapter shall appear either on the principal display panel or on the information panel, unless otherwise specified by regulations in this chapter.
> All information appearing on the principal display panel or the information panel pursuant to this section shall appear prominently and conspicuously, but in no case may the letters and/or numbers be less than one-sixteenth inch in height unless an exemption pursuant to paragraph (f) of this section is established. The requirements for conspicuousness and legibility shall include the specifications of §§ 101.7(h)(1) and (2) and 101.15.
- 方法论陈述：把散落在 Subpart A、Subpart D、part 105 的强制信息先「列清单」再「定落位」：一律只能落在 PDP 或信息面板两面之一，除非本章另有明文指定。落位确定后立刻叠加显著性闸门——prominent/conspicuous，且字母/数字高度不得低于 1/16 英寸，唯一例外是依 (f) 建立的豁免。显著性不是主观感觉，它被显式指向 §101.7(h)(1)(2) 的字形规格与 §101.15 的显著性条款，形成一个「清单 → 二选一 → 显著性 → 硬性下限 → 例外」五段链。
- 可回答的新问题：把配料表印在包装背面（既非 PDP 也非信息面板）为何直接构成错标风险？「1/16 英寸」下限与 §101.7(i) 按面积递增的字号是什么关系（取大还是取小）？§101.2(f) 的替代传播豁免能否覆盖全部强制信息？
- 跨域佐证：〔§ 101.15〕显著性/醒目性的统一规格；〔§ 101.7(h)(1)(2)〕高宽比与大小写字母高度；〔§ 101.2(f)〕小包装经请愿建立替代传播方式。
- 建议归属子卡：基础架构

### CAND-FW-04: 「同一面板」默认 + 空间不足拆分的二次分流
- 条款出处：〔§ 101.2(d)(1)〕 + pdf-page 4
- 原文引用（英文逐字，≤100 词/段）：
> Except as provided by §§ 101.9(j)(13) and (j)(17) and 101.36(i)(2) and (i)(5), all information required to appear on the principal display panel or on the information panel under this section shall appear on the same panel unless there is insufficient space. In determining the sufficiency of the available space, except as provided by §§ 101.9(j)(17) and 101.36(i)(5), any vignettes, designs, and other nonmandatory label information shall not be considered.
> If there is insufficient space for all of this information to appear on a single panel, it may be divided between these two panels, except that the information required under any given section or part shall all appear on the same panel. A food whose label is required to bear the ingredient statement on the principal display panel may bear all other information specified in paragraph (b) of this section on the information panel.
- 方法论陈述：在 FW-03 确定「两面之一」之后，本链再问「能否塞进同一面」。默认强制信息集中在同一面板；判断「空间是否足够」时，vignettes、装饰图案、其他非强制信息一律不计入可用空间（防止用留白做借口），且 §101.9(j)(13)/(j)(17)、§101.36(i)(2)/(i)(5) 的小包装/简化格式先被排除在默认之外。若确实不足，允许在 PDP 与信息面板之间拆分，但有一条硬约束：同一 section/part 要求的信息必须整体留在同一面板，不得把一个条款下的信息切两半。配料表被迫放 PDP 的食品，其余 (b) 信息可以全部放信息面板。
- 可回答的新问题：厂商想用「版面留白不够」把营养标签拆到两个面，但把装饰图算进可用面积——这个理由为什么不成立？「同一 section 不拆」会让 §101.9 的 Nutrition Facts 被允许跨页吗？简化格式食品是否绕开了「同一面板」默认？
- 跨域佐证：〔§ 101.9(j)(13)(j)(17)〕小包装与简化格式的 placement 例外；〔§ 101.36(i)(2)(i)(5)〕膳食补充剂对应例外；〔§ 101.2(d)(2)〕盖身分离容器的 placement 例外。
- 建议归属子卡：基础架构

### CAND-FW-05: 小包装「空间不足 → 请愿替代传播」闸门与瓶盖信息优先级
- 条款出处：〔§ 101.2(f)〕〔§ 101.2(c)(2)(3)〕 + pdf-page 4–5
- 原文引用（英文逐字，≤100 词/段）：
> If the label of any package of food is too small to accommodate all of the information required by §§ 101.4, 101.5, 101.8, 101.9, 101.13, 101.17, 101.36, subpart D of part 101, and part 105 of this chapter, the Commissioner may establish by regulation an acceptable alternative method of disseminating such information to the public, e.g., a type size smaller than one-sixteenth inch in height, or labeling attached to or inserted in the package or available at the point of purchase. A petition requesting such a regulation, as an amendment
> to this paragraph, shall be submitted under part 10 of this chapter.
> Upon the petition of any interested person demonstrating that the bottle closure is too small to accommodate this information, the Commissioner may by regulation establish an alternative method of disseminating such information. Information appearing on the closure shall appear in the following priority: (i) The statement of ingredients. (ii) The name and address of the manufacturer, packer, or distributor. (iii) The statement of identity.
- 方法论陈述：当且仅当「标签太小装不下 (b) 清单全部强制信息」时才进入本闸门，且企业不能自行减免——必须由 FDA 通过规章确立可接受的替代传播方式（缩小字号、附签/插页、销售点提供），企业须按 part 10 提交请愿来修订该款。软饮料瓶盖是同一逻辑的具象化：瓶盖太小时按请愿另定方法，并给出强制信息的法定「优先级」——配料表 → 厂商名址 → 品名，装不下时从末尾裁。这是「默认全标 → 证明空间不足 → 请愿 → 按优先级取舍」的四段链，与 §101.9(j)(13) 的小包装简化格式是两套不同通道。
- 可回答的新问题：3 平方英寸以下的餐厅单份包装能否直接不印厂商名址？瓶盖空间只够两行时先砍哪一项？「销售点提供」是否等同于可不在包装上留任何信息？
- 跨域佐证：〔§ 101.2(c)(2)〕餐厅/机构用单份小包装 type-size 豁免（3 sq in、1⁄32 in）；〔§ 101.9(j)(13)〕小包装简化营养格式；〔§ 101.2(c)(1)(i)(ii)〕1975 年前玻璃瓶软饮的既存豁免。
- 建议归属子卡：基础架构

### CAND-FW-06: 品名（statement of identity）「法定名 → 通用名 → 描述/幻想名」三级递补链
- 条款出处：〔§ 101.3(b)〕〔§ 101.3(a)(d)〕 + pdf-page 5
- 原文引用（英文逐字，≤100 词/段）：
> The principal display panel of a food in package form shall bear as one of its principal features a statement of the identity of the commodity.
> Such statement of identity shall be in terms of: (1) The name now or hereafter specified in or required by any applicable Federal law or regulation; or, in the absence thereof, (2) The common or usual name of the food; or, in the absence thereof, (3) An appropriately descriptive term, or when the nature of the food is obvious, a fanciful name commonly used by the public for such food.
> This statement of identity shall be presented in bold type on the principal display panel, shall be in a size reasonably related to the most prominent printed matter on such panel, and shall be in lines generally parallel to the base on which the package rests as it is designed to be displayed.
- 方法论陈述：先在 PDP 上确立「必须有品名且为主特征之一」，再按顺序递补选名：有联邦法律/规章指定名 → 用它；无 → 用通用/惯用名；再无 → 用恰切描述词，若食品性质显而易见可用公众惯用的幻想名。每一级以「in the absence thereof」为分岔条件，不可跳级、不可因营销偏好改用幻想名。选名之后叠加形式义务：粗体、字号与 PDP 最醒目文字成合理比例、字行平行于包装陈列时的底面。
- 可回答的新问题：已有 standard of identity 的食品能否用自创品牌名代替法定名？「性质显而易见」由谁判断、与 §101.3(e) 的 imitation 判定是否同一套证据？品名字号与净含量字号冲突时以哪条为准？
- 跨域佐证：〔§ 101.3(c)〕可选形态（whole/slices/diced）须作为品名必要部分（可见或 vignette 时例外）；〔§ 101.3(e)(2)(ii)〕非 imitation 食品须用符合 §102.5 的通用名；〔§ 101.3(f)〕品名中可被要求标注特征配料百分比。
- 建议归属子卡：基础架构

### CAND-FW-07: imitation（仿制食品）「替代+相似+营养劣势」正反双向判定链
- 条款出处：〔§ 101.3(e)(1)(2)(3)(4)〕 + pdf-page 5–6
- 原文引用（英文逐字，≤100 词/段）：
> Under the provisions of section 403(c) of the Federal Food, Drug, and Cosmetic Act, a food shall be deemed to be misbranded if it is an imitation of another food unless its label bears, in type of uniform size and prominence, the word “imitation” and, immediately thereafter, the name of the food imitated. (1) A food shall be deemed to be an imitation and thus subject to the requirements of section 403(c) of the act if it is a substitute for and resembles another food but is nutritionally inferior to that food.
> (2) A food that is a substitute for and resembles another food shall not be deemed to be an imitation provided it meets each of the following requirements: (i) It is not nutritionally inferior to the food for which it substitutes and which it resembles. (ii) Its label bears a common or usual name that complies with the provisions of § 102.5 of this chapter and that is not false or misleading, or in the absence of an existing common or usual name, an appropriately descriptive term that is not false or misleading.
> (ii) For the purpose of this section, a measurable amount of an essential nutrient in a food shall be considered to be 2 percent or more of the Daily Reference Value (DRV) of protein listed under § 101.9(c)(7)(iii) and of potassium listed under § 101.9(c)(9) per reference amount customarily consumed and 2 percent or more of the Reference Daily Intake (RDI) of any vitamin or mineral listed under § 101.9(c)(8)(iv) per reference amount customarily consumed, except that selenium, molybdenum, chromium, and chloride need not be considered.
- 方法论陈述：先跑正向判定：同时满足「是替代品 + 相似 + 营养劣势」三要件才落入 imitation，后果是必须标 “imitation” 加被仿食品名，否则按 FD&C Act 403(c) 错标。再跑反向豁免：即便「替代+相似」，只要逐项满足「不营养劣势」+「有合规且不误导的通用名/描述词」即可不当作 imitation；已有法规通用名或标准身份且全部合规者也直接排除。营养劣势的量化靠 (4)：任一必需营养素以 per RACC 计下降，且「可测量量」被定义为 ≥2% DRV/RDI（硒、钼、铬、氯化物除外），热量/脂肪下降且按 §101.9 标示时另有出路。
- 可回答的新问题：只减了脂肪并据 §101.9 如实标示的「低脂仿制品」还算营养劣势吗？「per RACC」把 2% 阈值与 §101.12 参考量绑在一起，产品改小包装会不会改变 imitation 结论？(4)(iii) 的「其他理由劣势」由谁启动修订？
- 跨域佐证：〔§ 101.3(e)(3)〕已有标准身份/通用名/营养质量指南且合规者不视为 imitation；〔§ 101.9(c)(7)(iii)(c)(8)(iv)(c)(9)〕DRV/RDI 数值来源；〔§ 101.12〕RACC 是 per reference amount 的分母。
- 建议归属子卡：基础架构

### CAND-FW-08: 配料名称「默认具体名 + 集体名列举例外」闸门
- 条款出处：〔§ 101.4(b)〕〔§ 101.4(b)(1)(2)(14)〕 + pdf-page 7–8
- 原文引用（英文逐字，≤100 词/段）：
> The name of an ingredient shall be a specific name and not a collective (generic) name, except that: (1) Spices, flavorings, colorings and chemical preservatives shall be declared according to the provisions of § 101.22.
> (2) An ingredient which itself contains two or more ingredients and which has an established common or usual name, conforms to a standard established pursuant to the Meat Inspection or Poultry Products Inspection Acts by the U.S. Department of Agriculture, or conforms to a definition and standard of identity established pursuant to section 401 of the Federal Food, Drug, and Cosmetic Act, shall be designated in the statement of ingredients on the label of such food by either of the following alternatives:
> (14) Each individual fat and/or oil ingredient of a food intended for human consumption shall be declared by its specific common or usual name (e.g., “beef fat”, “cottonseed oil”) in its order of predominance in the food except that blends of fats and/or oils may be designated in their order of predominance in the foods as “______ shortening” or “blend of ______ oils”
- 方法论陈述：先立默认——每种配料用具体名，不得用集合/通用类名。再查列举例外：香料/调味/色素/化学防腐剂转 §101.22 处理；复合配料若有既定通用名、符合 USDA 肉类/禽类标准、或符合 FD&C Act 401 标准身份，可在「通用名+括号内按降序列全部组分」与「把各组分直接并入成品配料表」两条替代路径中二选一。油脂是强化的具体名规则：每种脂肪/油须单独具名，只有 blends 才允许 “______ shortening / blend of ______ oils” 统称，且须紧跟括号内逐一列出各来源油，并随氢化程度加 hydrogenated / partially hydrogenated。例外的共同结构是「具体名义务 + 穷举式可统称清单 + 附带条件」。
- 可回答的新问题：一个「植物起酥油」标签只写统称不写括号来源，缺的是哪一段要件？复合配料用「并入法」时，成品配料表的降序该按组分还是按复合配料整体排？§101.22 允许统称的香料能否再套用 (b)(2) 的复合配料替代？
- 跨域佐证：〔§ 101.22〕香料/调味/色素/化学防腐剂的统称规则；〔§ 101.4(b)(16)(17)(18)(19)〕膨松剂/酵母营养剂/面团调节剂/固化剂的「集体名+括号列名」同类结构；〔§ 101.100(a)(3)〕incidental additive 是配料表申报豁免而非命名豁免。
- 建议归属子卡：基础架构

### CAND-FW-09: 配料表「重量降序默认 + 2% 量化例外」判定链
- 条款出处：〔§ 101.4(a)(1)(2)〕〔§ 101.4(e)(f)〕 + pdf-page 7
- 原文引用（英文逐字，≤100 词/段）：
> Ingredients required to be declared on the label or labeling of a food, including foods that comply with standards of identity, except those ingredients exempted by § 101.100, shall be listed by common or usual name in descending order of predominance by weight on either the principal display panel or the information panel in accordance with the provisions of § 101.2, except that ingredients in dietary supplements that are listed in the nutrition label in accordance with § 101.36 need not be repeated in the ingredient list.
> The descending order of predominance requirements of paragraph (a)(1) of this section do not apply to ingredients present in amounts of 2 percent or less by weight when a listing of these ingredients is placed at the end of the ingredient statement following an appropriate quantifying statement, e.g., “Contains __ percent or less of ______” or “Less than __ percent of ______.” The blank percentage within the quantifying statement shall be filled in with a threshold level of 2 percent, or, if desired, 1.5 percent, 1.0 percent, or 0.5 percent,
> as appropriate. No ingredient to which the quantifying phrase applies may be present in an amount greater than the stated threshold.
- 方法论陈述：先定「哪些配料要申报」——默认全部，扣掉 §101.100 豁免项（含符合标准身份的食品也要列），膳食补充剂中已在营养标签列出的可免重复。再定顺序：一律按重量降序、用通用名、落在 PDP 或信息面板（回到 §101.2）。然后进入 2% 例外：含量 ≤2% 的配料可脱离降序，统一挪到配料表末尾，但必须前置一句量化声明（“Contains 2% or less of …”），声明里的阈值只能取 2/1.5/1.0/0.5%，且任何被归入该句的配料实际含量不得超过所写阈值。若加了 (e) 的百分比声明，则须按重量百分比、就近取 1%，≤2% 的仍可并入量化句。
- 可回答的新问题：把 1.8% 的香辛料写进 “Contains 2% or less of …” 句后，还能不能在句首单独列一次？膳补产品把某成分从营养标签移到配料表后，降序义务是否恢复？「按重量降序」在复水配料 (§101.4(c)) 下该按干重还是复水后重？
- 跨域佐证：〔§ 101.4(c)〕复水配料的排序按「未复水配料+复原用水量」计，超出部分另标 water；〔§ 101.4(e)〕百分比声明须按重量、就近 1%；〔§ 101.100〕配料表申报豁免清单（与降序义务是不同层）。
- 建议归属子卡：基础架构

### CAND-FW-10: 净含量「物态 → 计量单位」分流 + 惯例/专员兜底
- 条款出处：〔§ 101.7(a)〕〔§ 101.7(b)(c)〕 + pdf-page 12
- 原文引用（英文逐字，≤100 词/段）：
> The principal display panel of a food in package form shall bear a declaration of the net quantity of contents. This shall be expressed in the terms of weight, measure, numerical count, or a combination of numerical count and weight or measure. The statement shall be in terms of fluid measure if the food is liquid, or in terms of weight if the food is solid, semisolid, or viscous, or a mixture of solid and liquid; except that such statement may be in terms of dry measure if the food
> is a fresh fruit, fresh vegetable, or other dry commodity that is customarily sold by dry measure.
> If there is a firmly established general consumer usage and trade custom of declaring the contents of a liquid by weight, or a solid, semisolid, or viscous product by fluid measure, it may be used. Whenever the Commissioner determines that an existing practice of declaring net quantity of contents by weight, measure, numerical count, or a combination in the case of a specific packaged food does not facilitate value comparisons by consumers and offers opportunity for consumer confusion, he will by regulation designate the appropriate term or terms to be used for such commodity.
- 方法论陈述：先在 PDP 上确立「必须有净含量声明」，再按食品物态分流：液体 → 液量单位；固体/半固体/黏稠/固液混合 → 重量单位；鲜果蔬或按干量惯例出售的干货 → 可用干量。随后两道修正：若存在「 firmly established 消费者用法与行业惯例」按重量标液体（或反过来），可沿用惯例；若 FDA 专员认定某具体食品的现行做法不利于比价且易致混淆，则由规章另行指定术语。最后才落到 (b) 的单位制（常衡磅/盎司、231 立方英寸加仑、2150.42 立方英寸蒲式耳）与 (c) 数值计数不足时须补重量/尺寸。
- 可回答的新问题：番茄罐头（固液混合）为何不能只标液量？「按干量惯例出售」由谁举证？专员指定术语的规章与 §101.7(r) 泡菜按液量的特别规定冲突时谁优先？
- 跨域佐证：〔§ 101.7(b)(2)(b)(3)〕液量/干量的法定单位与温度基准；〔§ 101.7(r)〕泡菜类强制按加仑/夸脱/品脱/液量盎司；〔§ 101.7(j)(k)〕<4 lb/1 gal 与 ≥4 lb/1 gal 的表达格式分界。
- 建议归属子卡：基础架构

### CAND-FW-11: 净含量字号「按 PDP 面积四档递增」的量化阶梯
- 条款出处：〔§ 101.7(i)〕〔§ 101.7(f)〕 + pdf-page 13–14
- 原文引用（英文逐字，≤100 词/段）：
> The declaration shall be in letters and numerals in a type size established in relationship to the area of the principal display panel of the package and shall be uniform for all packages of substantially the same size by complying with the following type specifications:
> (1) Not less than one-sixteenth inch in height on packages the principal display panel of which has an area of 5 square inches or less. (2) Not less than one-eighth inch in height on packages the principal display panel of which has an area of more than 5 but not more than 25 square inches. (3) Not less than three-sixteenths inch in height on packages the principal display panel of which has an area of more than 25 but not more than 100 square inches. (4) Not less than one-fourth
> inch in height on packages the principal display panel of which has an area of more than 100 square inches, except not less than 1⁄2 inch in height if the area is more than 400 square inches.
- 方法论陈述：把净含量字号做成「面积 → 最小字号」的离散阶梯：≤5 sq in → 1/16 in；>5–25 → 1/8 in；>25–100 → 3/16 in；>100 → 1/4 in，>400 → 1/2 in；并要求同尺寸包装之间字号统一。阶梯的输入正是 FW-01 算出的 PDP 面积，故形状判定错会连带字号错。另有两条修正：吹制/压印/模塑在玻璃或塑料表面时，各档字号再统一加 1/16 in；(f) 规定声明须位于 PDP 底部 30% 区域内且与其他文字留出法定间距，但 PDP ≤5 sq in 时底部 30% 要求不适用。
- 可回答的新问题：圆柱形容器按 40% 公式算出的面积落在 25 sq in 边界时，字号取哪一档？「同尺寸包装字号统一」能否用来挑战同一产品线不同口味用不同字号？模塑字加 1/16 in 与 §101.2(c) 的 1/16 in 下限是叠加还是取大？
- 跨域佐证：〔§ 101.1〕PDP 面积计算是本阶梯的输入；〔§ 101.7(f)〕底部 30% 落位与间距；〔§ 101.2(c)〕1/16 in 通用显著性下限。
- 建议归属子卡：基础架构

### CAND-FW-12: 自动售货机「covered vending machine food」双层主体+可见性闸门
- 条款出处：〔§ 101.8(b)〕〔§ 101.8(c)(1)〕〔§ 101.8(d)(1)〕 + pdf-page 17–18
- 原文引用（英文逐字，≤100 词/段）：
> Articles of food sold from a vending machine are not covered vending machine food if: (1) The prospective purchaser can view: (i) The calories, serving size, and servings per container listed in the Nutrition Facts label on the vending machine food without any obstruction. The Nutrition Facts label must be in the format required in § 101.9(c) and (d). The Nutrition Facts label must be in a size that permits the prospective purchaser to be able to easily read the nutrition information contained in the Nutrition Facts label on the article of food in the vending machine.
> For the purposes of this section, the term “covered vending machine food” means an article of food that is: (i) Sold from a vending machine that does not permit the prospective purchaser to examine the Nutrition Facts label prior to purchase as provided in paragraph (b)(1) of this section or otherwise provide visible nutrition information at the point of purchase as provided in paragraph (b)(2) of this section; and
> (ii) Sold from a vending machine that: (A) Is operated by a person engaged in the business of owning or operating 20 or more vending machines; or (B) Is operated by a vending machine operator that has voluntarily elected to be subject to the requirements of this section by registering with FDA under paragraph (d) of this section.
- 方法论陈述：先用「反向排除」判定：购买前能无遮挡读到符合 §101.9(c)(d) 格式的 Nutrition Facts，或购买前机器已显示 calories/serving size/servings per container 复制件，或包装本身有清晰可见（字号≥§101.7(i) 的 150%）的卡路里信息 → 不是 covered food，无需额外卡路里声明。未落入排除者再过正向两要件：(i) 购前无法查看 Nutrition Facts 且无销售点可见营养信息；(ii) 运营者拥有/运营 ≥20 台机器，或已按 (d) 自愿注册受约束。两要件同时成立才触发 (c)(2) 的卡路里声明义务；这是「20 台阈值 + 自愿注册」主体闸门与「可见性」行为闸门的交集。
- 可回答的新问题：19 台机器的运营商自愿注册后是否从「不受约束」翻转为「受约束且须标卡路里」？在机器屏幕购前显示卡路里，是否即可把食品排除出 covered？「自愿注册换取排除州地方法规」与 §101.11(d)(1) 餐馆自愿注册是不是同一制度？
- 跨域佐证：〔§ 101.8(d)(1)〕非强制主体可自愿注册、注册后不再受不一致的州/地方营养标签要求；〔§ 101.11(a)〕covered establishment 同样含「20+ 连锁」与「已注册」两分支；〔§ 101.9(c)(d)〕Nutrition Facts 格式是 (b)(1)(i) 可见性判定的依据。
- 建议归属子卡：特定品类与警示

### CAND-FW-13: 净含量错标产品「默认禁售 → 满足三条件可定向售政府机构」例外通道
- 条款出处：〔§ 101.7(t)〕〔§ 101.7(q)〕 + pdf-page 16
- 原文引用（英文逐字，≤100 词/段）：
> Where the declaration of net quantity of contents is in terms of net weight and/or drained weight or volume and does not accurately reflect the actual quantity of the contents or the product falls below the applicable standard of fill of container because of equipment malfunction or otherwise unintentional product variation, and the label conforms in all other respects to the requirements of this chapter (except the requirement that food falling below the applicable standard of fill of container shall bear the general statement of substandard fill specified in §
> 130.14(b) of this chapter), the mislabeled food product, including any food product that fails to bear the general statement of substandard fill specified in § 130.14(b) of this chapter, may be sold by the manufacturer or processor directly to institutions operated by Federal, State or local governments (schools, prisons, hospitals, etc.): Provided, That:
> (1) The purchaser shall sign a statement at the time of sale stating that he is aware that the product is mislabeled to include acknowledgment of the nature and extent of the mislabeling, (e.g., “Actual net weight may be as low as __% below labeled quantity”) and that any subsequent distribution by him of said product except for his own institutional use is unlawful. This statement shall be kept on file at the principal place of business of the manufacturer or processor for 2 years subsequent to the date of
> shipment of the product and shall be available to the Food and Drug Administration upon request.
- 方法论陈述：先把触发条件限定为「设备失灵或非故意产品波动」造成的净含量不准 / 低于装填标准，且标签在其余各方面合规；在此之外一律按错标处理。满足前提后才打开一条极窄通道：只能由制造商/加工商直接卖给联邦/州/地方政府机构（学校、监狱、医院），且必须逐项满足 (1) 购买者签署知悉错标性质与程度的声明、留存 2 年备 FDA 查验、承诺不得再分销；(2) 外箱标注 “Product Mislabeled… This Product Not for Retail Distribution” 及最大偏差百分比；(3) 该声明须醒目、粗体、对比底色。这是「默认禁止 → 限定前提 → 限定对象 → 三项留痕条件」的条件豁免链，与 §101.100/§101.9(j)/§101.108 的标签义务豁免又不同源。
- 可回答的新问题：主动少灌装（非设备失灵）能否援引本通道？购买机构把产品转给另一家公立学校是否还算「own institutional use」？留存 2 年的起算点是销售日还是发运日？
- 跨域佐证：〔§ 101.7(q)〕合理水分得失/GMP 偏差被认可、偏差不得过大（界定「何种不准」可被容忍）；〔§ 130.14(b)〕substandard fill 通用声明（转引未收）；〔§ 101.18〕misbranding 总纲（本通道是总纲下的极窄例外）。
- 建议归属子卡：豁免与效力层

### CAND-FW-14: 餐馆食品「声称触发营养标签」闸门（声称 → 义务）
- 条款出处：〔§ 101.10〕 + pdf-page 68（跨入 `pdf-page 69` 段落）
- 原文引用（英文逐字，≤100 词/段）：
> Nutrition labeling in accordance with § 101.9 shall be provided upon request for any restaurant food or meal for which a nutrient content claim (as defined in § 101.13 or in subpart D of this part) or a health claim (as defined in § 101.14 and permitted by a regulation in subpart E of this part) is made, except that information on the nutrient amounts that are the basis for the claim (e.g., “low fat, this meal provides less than 10 grams of fat”) may serve as the functional equivalent of complete nutrition information as described in § 101.9.
> For standard menu items that are offered for sale in covered establishments (as defined in § 101.11(a)), the information in the written nutrition information required by § 101.11(b)(2)(ii)(A) will serve to meet the requirements of this section. Nutrient levels may be determined by nutrient databases, cookbooks, or analyses or by other reasonable bases that provide assurance that the food or meal meets the nutrient requirements for the claim.
- 方法论陈述：餐馆食品本来不强制贴 Nutrition Facts，本链把「作了声称」设为触发器：只要对某道菜/餐作了 §101.13/Subpart D 的营养素含量声称，或 §101.14 且经 Subpart E 允许的健康声称，就须「应请求提供」§101.9 口径的营养信息。分岔有三：① 只给出「作为声称基础的营养素量」（如 “low fat, this meal provides less than 10 grams of fat”）即可充当完整营养信息的功能等价物，不必铺全套 Nutrition Facts；② 若是 covered establishment 的标准菜单项，§101.11(b)(2)(ii)(A) 的书面营养信息即视为满足本节；③ 营养素水平可用数据库、食谱书、分析或其他合理依据，但须能保证满足该声称的营养素要求。
- 可回答的新问题：菜单上写 “heart healthy” 但无 Subpart E 授权，触发的是 §101.10 的提供义务还是直接落入未授权声称？餐馆在广告（labeling）里作声称而菜单不写，是否仍触发？「功能等价物」给出基础营养素量后，还需不需要给 %DV？
- 跨域佐证：〔§ 101.13〕营养素含量声称定义；〔§ 101.14〕健康声称定义与 Subpart E 授权前提；〔§ 101.11(b)(2)(ii)(B)〕即便书面信息因「insignificant amounts」可免，作了声称仍须提供该声称营养素信息。
- 建议归属子卡：声称闸门

### CAND-FW-15: 连锁餐饮「covered establishment 主体闸门」+「标准菜单项 vs 排除清单」双层
- 条款出处：〔§ 101.11(a)〕〔§ 101.11(b)(1)〕〔§ 101.11(d)(1)〕 + pdf-page 69–71
- 原文引用（英文逐字，≤100 词/段）：
> Covered establishment means a restaurant or similar retail food establishment that is a part of a chain with 20 or more locations doing business under the same name (regardless of the type of ownership, e.g., individual franchises) and offering for sale substantially the same menu items, as well as a restaurant or similar retail food establishment that is registered to be covered under paragraph (d) of this section.
> The labeling requirements in this paragraph (b) apply to standard menu items offered for sale in covered establishments. (ii)(A) The labeling requirements in this paragraph (b) do not apply to foods that are not standard menu items, including: (1) Items such as condiments that are for general use, including those placed on the table or on or behind the counter; daily specials; temporary menu items; custom orders; food that is part of a customary market test; and (2) Self-service food and food on display that is offered for sale for
> less than a total of 60 days per calendar year or fewer than 90 consecutive days in order to test consumer acceptance.
> The labeling requirements of paragraph (b)(2)(iii) of this section do not apply to alcoholic beverages that are foods on display and are not self-service foods.
- 方法论陈述：第一层判主体：连锁「≥20 家、同名（含轻微变体）、提供实质相同菜单项」即 covered；不达标的主体也可按 (d) 自愿注册成为 covered（并换取排除不一致的州地方法规）。第二层判客体：只对「standard menu item」（常规列于菜单/菜单板、常规自助或陈列）施加卡路里与书面营养义务，并用穷举排除清单剪掉 condiments、daily specials、temporary menu items（<60 天/年）、custom orders、 customary market test（<90 连续天）、短期自助/陈列食品；陈列的非自助酒精饮料另免 (b)(2)(iii) 的标识要求。两层是「与」关系：主体不 covered 或客体非标准菜单项，任一命中即不触发 (b)。
- 可回答的新问题：19 家同名但菜单相同的连锁是否完全不受约束？把某菜品改名为「区域限定」是否足以构成 §101.11(a) 的 “slight variations” 而仍算同名？临时菜单项上架到第 61 天时，卡路里义务从哪一天起算？
- 跨域佐证：〔§ 101.8(c)(1)(ii)(A)〕自动售货机同样以「20 台」为强制阈值、以自愿注册为补充；〔§ 101.11(d)(1)〕自愿注册主体范围与法律后果；〔§ 101.11(f)〕不符 (b)/(c) 即按 201(n)/403(a)/403(f)/403(q) 错标。
- 建议归属子卡：营养标签与份量

### CAND-FW-16: 菜单卡路里「二选项斜线 / 三以上区间 / 无上限转介」格式分流
- 条款出处：〔§ 101.11(b)(2)(i)(A)(4)(5)(6)(7)(8)(9)〕 + pdf-page 72–74
- 原文引用（英文逐字，≤100 词/段）：
> (ii) When the menu or menu board does not list flavors or varieties for an entire individual variable menu item, and only includes a general description of the variable menu item (e.g., “soft drinks”), the calories must be declared for each option with a slash between the two calorie declarations where only two options are available (e.g., “150/250 calories”) or as a range in accordance with the requirements of paragraph (b)(2)(i)(A)(7) of this section where more than two options are available (e.g., “100-250 calories”).
> (7) Additional format requirements for declaring calories for an individual variable menu item, a combination meal, and toppings as a range, if applicable. Calories declared as a range must be in the format “xx-yy,” where “xx” is the caloric content of the lowest calorie variety, flavor, or combination, and “yy” is the caloric content of the highest calorie variety, flavor, or combination.
> (8) Exception for a variable menu item that has no clearly identifiable upper bound to the range of calories: If the variable menu item appears on the menu or menu board and is a self-service food or food on display, and there is no clearly identifiable upper bound to the range, e.g., all-you-can-eat buffet, then the menu or menu board must include a statement, adjacent to the name or price of the item, referring customers to the self-service facility for calorie information, e.g., “See buffet for calorie declarations.”
- 方法论陈述：当菜单项带变量（口味/品种/组合/加料/尺寸）时，先判断菜单是否逐项列出：逐项列出 → 每个变量单独标（相同卡路里经舍入后可合并为一个值但须注明）；只给统称 → 按选项数量分流：恰好两个用斜线 “150/250 calories”，三个及以上用区间。区间再受 (7) 约束：格式必须为 “xx-yy”，xx 为最低、yy 为最高卡路里品种。最后一道兜底：若变量项无明确上限（自助、陈列、all-you-can-eat buffet），区间无法封顶，则改为「转介声明」——在名称/价格旁写 “See buffet for calorie declarations.”，并满足字号/颜色/底色要求。组合餐 (6) 与加料 (5) 复用同一「2→斜线、≥3→区间」分岔。
- 可回答的新问题：五种口味里有三种卡路里相同，能否只写两个端点区间而不逐一列？「all-you-can-eat」用转介声明后，自助区是否仍须按 (b)(2)(iii) 标每份卡路里？区间 “xx-yy” 的两端是否也要先按 5/10 卡路里舍入？
- 跨域佐证：〔§ 101.11(b)(2)(i)(A)(2)〕5/50/10 卡路里舍入规则是区间端点的前置；〔§ 101.11(b)(2)(iii)(A)〕自助/陈列食品按每展示单位或每份标卡路里；〔§ 101.8(c)(2)(i)(D)〕售货机「按选项或按最终产品」标卡路里的同类分流。
- 建议归属子卡：营养标签与份量

### CAND-FW-17: 书面营养信息「全不显著→免 / ≥6 项不显著→简化 / 有声称→仍须给」三层分流
- 条款出处：〔§ 101.11(b)(2)(ii)(A)(B)〕 + pdf-page 75–76
- 原文引用（英文逐字，≤100 词/段）：
> The following nutrition information for a standard menu item must be available in written form on the premises of the covered establishment and provided to the customer upon request. This nutrition information must be presented in the order listed and using the measurements listed, except as provided in paragraph (b)(2)(ii)(B) of this section.
> (B) If a standard menu item contains insignificant amounts of all the nutrients required to be disclosed in paragraph (b)(2)(ii)(A) of this section, the establishment is not required to include nutrition information regarding the standard menu item in the written form. However, if the covered establishment makes a nutrient content claim or health claim, the establishment is required to provide nutrition information on the nutrient that is the subject of the claim in accordance with § 101.10. For standard menu items that contain insignificant amounts of six or more of
> the required nutrients, the declaration of nutrition information required by paragraph (b)(2)(ii)(A) of this section may be presented in a simplified format.
> (1) An insignificant amount is defined as that amount that allows a declaration of zero in nutrition labeling, except that for total carbohydrates, dietary fiber, and protein, it must be an amount that allows a declaration of “less than one gram.”
- 方法论陈述：默认书面营养信息须按 (A) 的固定 11 项顺序与单位提供、应请求可取。再按「不显著项数量」三级分流：全部 11 项都不显著 → 完全免书面信息；≥6 项不显著 → 可改用简化格式（只列总卡/总脂/总碳/蛋白/钠 + 脂肪卡路里及显著项，并加 “Not a significant source of ____”）；其余情形维持完整格式。最关键的反向闸门：只要对该菜品作了营养素含量/健康声称，即便整体符合免标或简化，仍须按 §101.10 提供该声称所涉营养素的信息。「不显著」由 (B)(1) 定量定义——允许标零，但总碳/膳食纤维/蛋白须「允许标 less than one gram」。
- 可回答的新问题：某菜品恰好 5 项不显著，能否用简化格式？已用简化格式的菜品加了 “low sodium” 声称，是否必须补齐钠信息？「less than one gram」与 §101.9(c) 的舍入规则是否同一口径？
- 跨域佐证：〔§ 101.10〕声称触发时须提供声称所涉营养素信息；〔§ 101.11(b)(2)(ii)(A)〕11 项固定清单与顺序；〔§ 101.9(c)〕营养素舍入规则（书面信息 rounding 须合规）。
- 建议归属子卡：营养标签与份量

### CAND-FW-18: 营养数据「合理依据 + 按所用方法分流举证」链
- 条款出处：〔§ 101.11(c)(1)(2)(3)〕〔§ 101.10〕 + pdf-page 78–81
- 原文引用（英文逐字，≤100 词/段）：
> A covered establishment must have a reasonable basis for its nutrient declarations. Nutrient values may be determined by using nutrient databases (with or without computer software programs), cookbooks, laboratory analyses, or other reasonable means, including the use of Nutrition Facts on labels on packaged foods that comply with the nutrition labeling requirements of section 403(q)(1) of the Federal Food, Drug, and Cosmetic Act and § 101.9, FDA nutrient values for raw fruits and vegetables in Appendix C of this part, or FDA nutrient values for cooked fish in Appendix D of this part.
> (2) Nutrient declarations for standard menu items must be accurate and consistent with the specific basis used to determine nutrient values. A covered establishment must take reasonable steps to ensure that the method of preparation (e.g., types and amounts of ingredients, cooking temperatures) and amount of a standard menu item offered for sale adhere to the factors on which its nutrient values were determined. (3) A covered establishment must provide to FDA, within a reasonable period of time upon request, information substantiating nutrient values including the method and data used to derive these nutrient values.
- 方法论陈述：先立总义务——任何卡路里/营养素声明都须有「reasonable basis」，且声明值须与所采用的那套依据一致，并须用合理步骤保证实际制备（配料种类用量、烹饪温度、份量）与定值时的因素一致。再按「选了哪条依据」分流举证清单：数据库（(i)：名称版本、配方、各配料贡献、 worksheets/printouts、营养值明细、两份签名声明）／含营养信息的食谱书（(ii)：书名作者出版者、营养信息获取方式、配方复印件、签名声明）／实验室分析（(iii)：配方、实验室名址、分析工作单与方法、两份签名声明）／其他合理方法（(iv)：方法详述、配方、衍生数据、两份签名声明）。FDA 请求时须在合理期限内提交对应材料。
- 可回答的新问题：用 §101.9 合规包装 Nutrition Facts 作为依据时，还要不要另备配方与签名声明？更换食用油品牌但卡路里不变，是否触发「制备因素一致」重核？Appendix C/D 的图形数值可否直接引作依据（转引未收问题）？
- 跨域佐证：〔§ 101.10〕餐馆声称数据可用 nutrient databases / cookbooks / analyses / other reasonable bases；〔§ 101.11(f)〕不符 (b)/(c) 即错标；〔§ 101.9〕包装食品 Nutrition Facts 作为可采依据之一。
- 建议归属子卡：营养标签与份量

### CAND-FW-19: 「自愿受联邦约束 ↔ 排除不一致州地方法规」的权衡闸门
- 条款出处：〔§ 101.11(d)(1)〕〔§ 101.8(d)(1)〕〔§ 101.11(a)〕 + pdf-page 81（§101.8 在 pdf-page 18）
- 原文引用（英文逐字，≤100 词/段）：
> A restaurant or similar retail food establishment that is not part of a chain with 20 or more locations doing business under the same name and offering for sale substantially the same menu items may voluntarily register to be subject to the requirements established in this section. Restaurants and similar retail food establishments that voluntarily register will no longer be subject to non-identical State or local nutrition labeling requirements.
> A vending machine operator that is not subject to the requirements of section 403(q)(5)(H)(viii) of the Federal Food, Drug, and Cosmetic Act may, through its authorized official, voluntarily register with FDA to be subject to the requirements established in paragraph (c)(2) of this section. An authorized official of a vending machine operator that voluntarily registers cannot be subject to any State or local nutrition labeling requirements that are not identical to the requirements in 403(q)(5)(H) of the Federal Food, Drug, and Cosmetic Act.
- 方法论陈述：本链处理「本不在强制范围内」的主体如何主动进入联邦体系：前提是本不受 §403(q)(5)(H)（连锁 <20 家 / 售货机 <20 台或未被覆盖）；动作是由 authorized official 向 FDA 注册、承诺受本节要求约束；法律后果是「不再受与联邦不一致的州/地方营养标签要求」。它是一个交换结构：以承担联邦义务换取排除州法碎片化，且注册有维持成本——每两年在到期前 60 天内续注册，否则自动失效。§101.11 与 §101.8 用完全同构的措辞把该闸门分别套到餐馆与自动售货机上。
- 可回答的新问题：自愿注册后能否「撤回」以重新适用更宽松的州法？「non-identical」由谁认定、州法更严格是否也被排除？注册失效（未续期）当天的卡路里声明义务与州法适用如何衔接？
- 跨域佐证：〔§ 101.11(a)〕covered establishment 定义本身把「已按 (d) 注册」列为第二分支；〔§ 101.8(c)(1)(ii)(B)〕售货机 covered food 同样把「自愿注册」列为主体要件；〔§ 101.11(d)(5)〕/〔§ 101.8(d)(4)(vii)〕两年续注册、自动失效。
- 建议归属子卡：豁免与效力层

### CAND-FW-20: RACC 推导方法论「消费调查 → 参考量 → 标签份量 → 声称分母」链起点
- 条款出处：〔§ 101.12(a)(1)–(9)〕 + pdf-page 82–83（(b) 表格区不可逐字引用）
- 原文引用（英文逐字，≤100 词/段）：
> (a) The general principles and factors that the Food and Drug Administration (FDA) considered in arriving at the reference amounts customarily consumed per eating occasion (reference amounts) which are set forth in paragraph (b) of this section, are that:
> (1) FDA calculated the reference amounts for persons 4 years of age or older to reflect the amount of food customarily consumed per eating occasion by persons in this population group. These reference amounts are based on data set forth in appropriate national food consumption surveys. (2) FDA calculated the reference amounts for an infant or child under 4 years of age to reflect the amount of food customarily consumed per eating occasion by infants up to 12 months of age or by children 1 through 3 years of age,
> respectively. These reference amounts are based on data set forth in appropriate national food consumption surveys. Such reference amounts are to be used only when the food is specially formulated or processed for use by an infant or by a child under 4 years of age.
> (4) To determine the amount of food customarily consumed per eating occasion, FDA considered the mean, median, and mode of the consumed amount per eating occasion. (5) When survey data were insufficient, FDA took various other sources of information on serving sizes of food into consideration. These other sources of information included: (i) Serving sizes used in dietary guidance recommendations or recommended by other authoritative systems or organizations; (ii) Serving sizes recommended in comments; (iii) Serving sizes used by manufacturers and grocers; and (iv) Serving sizes used by other countries.
> (6) Because they reflect the amount customarily consumed, the reference amount and, in turn, the serving size declared on the product label are based on only the edible portion of food, and not bone, seed, shell, or other inedible components. (7) The reference amount is based on the major intended use of the food (e.g., milk as a beverage and not as an addition to cereal). (8) The reference amounts for products that are consumed as an ingredient of other foods, but that may also be consumed in the form
> in which they are purchased (e.g., butter), are based on use in the form purchased. (9) FDA sought to ensure that foods that have similar dietary usage, product characteristics, and customarily consumed amounts have a uniform reference amount.
- 方法论陈述：本链是整部 part 的「比较基准生成器」：先按人群切分（≥4 岁 / 婴儿≤12 月 / 幼儿 1–3 岁，后两者仅在食品专为该人群配制或加工时启用），再以「适当全国食物消费调查」的 mean/median/mode 定「每次食用惯常消费量」；调查数据不足时按 (5) 的四级补充来源（膳食指南/权威机构、评议意见、厂商与零售商、他国份量）依次取用。随后三条校正：只算可食部分（排除骨/籽/壳）、按主要预期用途（牛奶作饮品而非加进麦片）、相似膳食用途/产品特性/惯常消费量的食品给统一 RACC。产物 (b) 的 Table 1/Table 2 把「产品类别 → RACC → label statement」钉死，再由 §101.9(b) 把 RACC 转成标签 serving size，而 serving size/RACC 又是 §101.13 含量声称、§101.14 disqualifying level 的共同分母。**表格数值不可逐字引用，须回原表按产品类别核对，并复核快照日期与 FR citation。**
- 可回答的新问题：一款「既可直接吃也可作配料」的黄油按哪条用途定 RACC？带壳坚果的 RACC 是否要扣壳重？某新品类在 Table 2 找不到对应，能否用 (9) 的「相似性」类推到相近类别、还是须走请愿？
- 跨域佐证：〔§ 101.9(b)〕RACC → 标签 serving size 的法定转换程序（表格脚注 3 明示「using the procedures in 21 CFR 101.9(b)」）；〔§ 101.13〕/〔§ 101.14〕声称阈值与 disqualifying level 以 RACC / per labeled serving 表述；〔§ 101.3(e)(4)(ii)〕imitation 的 2% 阈值按 per reference amount customarily consumed 计。
- 建议归属子卡：营养标签与份量

### CAND-FW-21: 营养标签义务「默认适用 + 列举豁免」总闸门
- 条款出处：〔§ 101.9(a)〕〔§ 101.9(j)〕 + pdf-page 20 / 58
- 原文引用（英文逐字，≤100 词/段）：
> Nutrition information relating to food shall be provided for all products intended for human consumption and offered for sale unless an exemption is provided for the product in paragraph (j) of this section.
> (1) When food is in package form, the required nutrition labeling information shall appear on the label in the format specified in this section. (2) When food is not in package form, the required nutrition labeling information shall be displayed clearly at the point of purchase (e.g., on a counter card, sign, tag affixed to the product, or some other appropriate device). Alternatively, the required information may be placed in a booklet, looseleaf binder, or other appropriate format that is available at the point of purchase.
> The following foods are exempt from this section or are subject to special labeling requirements:
- 方法论陈述：先立全称义务——凡「供人食用且要约出售」的产品一律提供营养信息；唯一出口是 (j) 为该产品明文列出的豁免或特殊标签要求。举证方向因此反转：不是企业证明「我该标」，而是主张豁免者须证明自己精确落入 (j) 的某一项及其全部附带条件。落入义务后再按包装形态分流呈现：包装食品 → 标签上按本节格式；非包装食品 → 销售点清晰展示（柜台卡/标牌/吊签）或置于销售点可取的册子/活页夹。这是整部 part 的「默认适用 + 封闭列举豁免」母结构，§101.100、§101.108 各自只切走自己那一条义务，不能借它免营养标签。
- 可回答的新问题：一个「我们产品很特殊」的概括理由能否构成豁免？非包装食品把营养册子放在后台办公室而非销售点，是否满足 (a)(2)？(j) 中写着「subject to special labeling requirements」的项目（如婴幼儿食品）到底是豁免还是加重义务？
- 跨域佐证：〔§ 101.9(j)(1)–(18)〕18 项豁免/特殊要求的封闭清单；〔§ 101.100〕豁免的是 403(i)(2) 配料表义务；〔§ 101.9(k)〕即便标了营养信息，暗示疾病预防表述仍另受 §101.14/Subpart E 约束。
- 建议归属子卡：营养标签与份量

### CAND-FW-22: 「作声称/给营养信息即使豁免失效」的反复元闸门
- 条款出处：〔§ 101.9(j)(1)(i)〕〔§ 101.9(j)(2)(i)(ii)(iii)〕〔§ 101.9(j)(3)〕〔§ 101.9(j)(4)〕〔§ 101.9(j)(10)〕〔§ 101.9(j)(13)(i)〕〔§ 101.9(j)(18)〕 + pdf-page 58–65
- 原文引用（英文逐字，≤100 词/段）：
> Food offered for sale by a person who makes direct sales to consumers (e.g., a retailer) who has annual gross sales made or business done in sales to consumers that is not more than $500,000 or has annual gross sales made or business done in sales of food to consumers of not more than $50,000, Provided, That the food bears no nutrition claims or other nutrition information in any context on the label or in labeling or advertising. Claims or other nutrition information subject the food to the provisions of this section, § 101.10, or § 101.11, as applicable.
> Except as provided in § 101.11, foods that contain insignificant amounts of all of the nutrients and food components required to be included in the declaration of nutrition information under paragraph (c) of this section, Provided, That the food bears no nutrition claims or other nutrition information in any context on the label or in labeling or advertising. Claims or other nutrition information, except as provided in § 101.8(c), subject the food to the provisions of this section.
> This exemption is contingent on the food bearing no nutrition claims or other nutrition information in any context on the label or in labeling or advertising. Claims or other nutrition information subject the food to nutrition labeling in accordance with § 101.45.
- 方法论陈述：这是全书重复次数最多的条件结构——几乎每一项 (j) 豁免都挂同一个 Provided 条件：食品在 label、labeling 或 advertising 的任何语境中「不得带有营养声称或其他营养信息」；一旦带有，该豁免即被击穿，产品回到 §101.9（或 §101.10 / §101.11 / §101.45）的完整义务。判定顺序是：先确认主体/客体落入某项豁免 → 再扫全部 label/labeling/advertising 是否出现任何营养声称或营养信息 → 命中即「豁免失效、义务回归」。它把「沉默」设为豁免的持续对价，是「豁免对象精确 + 条件持续满足」的元规则；§101.8(c) 是少数明文例外。
- 可回答的新问题：官网产品页（advertising）写了一句「富含维生素C」，会不会让小企业直销豁免整体失效？豁免失效后是只补 Nutrition Facts，还是连同 §101.10 的声称触发义务一起回来？「其他营养信息」与「营养声称」的边界在哪（例如只写卡路里数字）？
- 跨域佐证：〔§ 101.10〕餐馆食品作声称即触发应请求提供营养信息；〔§ 101.11(b)(2)(ii)(B)〕书面营养信息本可因「insignificant amounts」免，但作声称仍须给该营养素信息；〔§ 101.9(b)(12)(ii)〕双列产品作声称须附依据声明。
- 建议归属子卡：豁免与效力层

### CAND-FW-23: 「包装 / 非包装 / 应请求提供」三种呈现与豁免的关系链
- 条款出处：〔§ 101.9(a)(1)(2)(3)〕 + pdf-page 20
- 原文引用（英文逐字，≤100 词/段）：
> Solicitation of requests for nutrition information by a statement “For nutrition information write to ______________________ ” on the label or in the labeling or advertising for a food, or providing such information in a direct written reply to a solicited or unsolicited request, does not subject the label or the labeling of a food exempted under paragraph (j) of this section to the requirements of this section if the reply to the request conforms to the requirements of this section.
- 方法论陈述：在 (a)(1)/(a)(2) 的「包装→标签、非包装→销售点」二分之外，(a)(3) 单开一条支路：已被 (j) 豁免的食品，即便在标签/labeling/advertising 上邀约索取营养信息（"For nutrition information write to …"），或应主动/被动请求直接书面回复，也不因此丧失豁免——前提是回复内容本身符合本节要求。这条与 FW-22 形成对照：主动「作出声称/给出营养信息」击穿豁免，而「提供索取渠道 + 合规回复」不击穿。判定时要区分「信息是主动宣传」还是「被动响应式提供」。
- 可回答的新问题：豁免企业在包装上印「扫码查营养」是否落入 (a)(3) 的安全港？回复里多写了一句营销性营养描述，会不会从 (a)(3) 翻到 FW-22 的失效？§101.45 的自愿标签与 (a)(3) 的回复能否共用同一份材料？
- 跨域佐证：〔§ 101.9(j)(13)(i)(A)〕小包装豁免要求提供可索取营养信息的地址/电话；〔§ 101.9(a)(2)〕非包装食品销售点可取册子；〔§ 101.10〕「upon request」提供营养信息的同类结构。
- 建议归属子卡：营养标签与份量

### CAND-FW-24: 「添加营养素 ≥50% RDI → 转入特殊膳食用途」再定性闸门
- 条款出处：〔§ 101.9(a)(4)〕 + pdf-page 20
- 原文引用（英文逐字，≤100 词/段）：
> If any vitamin or mineral is added to a food so that a single serving provides 50 percent or more of the Reference Daily Intake (RDI) for the age group for which the product is intended, as specified in paragraph (c)(8)(iv) of this section, of any one of the added vitamins or minerals, unless such addition is permitted or required in other regulations, e.g., a standard of identity or nutritional quality guideline, or is otherwise exempted by the Commissioner, the food shall be considered a food for special dietary use within the meaning of § 105.3(a)(1)(iii) of this chapter.
- 方法论陈述：这是一个「定量触发再定性」链条：先看是否添加维生素/矿物质 → 再算单份是否达到该产品目标人群 RDI 的 ≥50%（RDI 表在 (c)(8)(iv)）→ 命中即把该食品改判为 §105.3(a)(1)(iii) 意义上的「特殊膳食用途食品」。但有两条排除：该添加若为其他规章（标准身份、营养质量指南）允许或要求，或经专员豁免，则不改判。再定性会牵动后续适用哪套标签规则，因此判定要「先量化、后查排除、再改类别」。
- 可回答的新问题：强化面粉按标准身份添加硫胺素是否会被本款改判？目标人群是婴幼儿时用哪一组 RDI 作分母？「special dietary use」改判后是否还要同时满足普通 Nutrition Facts？
- 跨域佐证：〔§ 101.9(c)(8)(iv)〕四组人群 RDI 表是 50% 的分母；〔§ 101.9(c)(8)(i)〕不同目标人群用对应 RDI；〔§ 101.3(g)〕膳食补充剂的品名标识是另一套类别规则（转引 §105 未收）。
- 建议归属子卡：营养标签与份量

### CAND-FW-25: serving size 由 RACC 推导「单位重量占 RACC 百分比」五档分流 ★
- 条款出处：〔§ 101.9(b)(2)〕〔§ 101.9(b)(2)(i)(A)–(D)(H)〕 + pdf-page 21–22
- 原文引用（英文逐字，≤100 词/段）：
> Except as provided in paragraphs (b)(3), (b)(4), and (b)(6) of this section and for products that are intended for weight control and are available only through a weight-control or weight-maintenance program, serving size declared on a product label shall be determined from the “Reference Amounts Customarily Consumed Per Eating Occasion * * * *” (reference amounts) that appear in § 101.12(b) using the procedures described below.
> (A) If a unit weighs 50 percent or less of the reference amount, the serving size shall be the number of whole units that most closely approximates the reference amount for the product category; (B) If a unit weighs more than 50 percent, but less than 67 percent of the reference amount, the manufacturer may declare one unit or two units as the serving size; (C) If a unit weighs 67 percent or more, but less than 200 percent of the reference amount, the serving size shall be one unit;
> (D) If a unit weighs at least 200 percent and up to and including 300 percent of the applicable reference amount, the serving size shall be the amount that approximates the reference amount. In addition to providing a column within the Nutrition Facts label that lists the quantitative amounts and percent Daily Values per serving size, the manufacturer shall provide a column within the Nutrition Facts label that lists the quantitative amounts and percent Daily Values per individual unit.
- 方法论陈述：这是「产品类别 → §101.12(b) RACC → 标签 serving size」的法定转换核心。先查产品是否在 (b)(3)/(b)(4)/(b)(6) 或体重控制专属产品的排除之列；否则对离散单元产品，计算「单个单元重量 ÷ RACC」的百分比并落到五档：≤50% → 取最接近 RACC 的整数个单元；>50% 且 <67% → 厂商可择一单元或两单元；≥67% 且 <200% → 一单元；≥200% 且 ≤300% → 取近似 RACC 的量，并强制双列（per serving + per individual unit）；(H) 多个已完整标注的单份容器 → serving size = 1 unit。体重控制专属产品可自定份量，但评估声称资格仍须回到 §101.12(b) RACC。
- 可回答的新问题：一个 60% RACC 的松饼，厂商选「2 个」后 %DV 与声称阈值按哪个份量算？200–300% 档的双列与 (b)(12)(i) 的「整包双列」如何叠加？体重控制产品自定份量后还能不能作「低脂」声称？
- 跨域佐证：〔§ 101.12(b)〕RACC 表是分母（数值须回原表核对）；〔§ 101.12(g)〕声称资格按 RACC 判定，且 serving size≠RACC 时须附依据声明；〔§ 101.9(b)(6)(b)(12)(i)〕单份容器与 200–300% 双列闸门。
- 建议归属子卡：营养标签与份量

### CAND-FW-26: 大离散单元 / 散装 / 组合产品的 serving size 三分流与 RACC 求和
- 条款出处：〔§ 101.9(b)(2)(ii)(iii)〕〔§ 101.12(f)(1)(2)〕 + pdf-page 22 / 197
- 原文引用（英文逐字，≤100 词/段）：
> (ii) For products in large discrete units that are usually divided for consumption (e.g., cake, pie, pizza, melon, cabbage), for unprepared products where the entire contents of the package is used to prepare large discrete units that are usually divided for consumption (e.g., cake mix, pizza kit), and for products which consist of two or more foods packaged and presented to be consumed together where the ingredient represented as the main ingredient is a large discrete unit usually divided for consumption (e.g., prepared cake packaged with a can of frosting),
> the serving size shall be the fractional slice of the ready-to-eat product (e.g., 1⁄12 cake, 1⁄8 pie, 1⁄4 pizza, 1⁄4 melon, 1⁄6 cabbage) that most closely approximates the reference amount for the product category
> (iii) For nondiscrete bulk products (e.g., breakfast cereal, flour, sugar, dry mixes, concentrates, pancake mixes, macaroni and cheese kits), and for products which consist of two or more foods packaged and presented to be consumed together where the ingredient represented as the main ingredient is a bulk product (e.g., peanut butter and jelly), the serving size shall be the amount in household measure that most closely approximates the reference amount for the product category
> (1) The reference amount for the combined product must be the reference amount, as established in paragraph (b) of this section, for the ingredient that is represented as the main ingredient (e.g., peanut butter, pancakes, cake) plus proportioned amounts of all minor ingredients. (2) If the reference amounts are in compatible units, the weights or volumes must be summed
> If the reference amounts are in incompatible units, all amounts must be converted to weights and summed
- 方法论陈述：当产品不是「小离散单元」时，按物理形态三分流：大单元通常切分食用（蛋糕/派/披萨）→ 用最接近 RACC 的「分数切片」（1⁄12 cake 等，且只能用 1⁄2、1⁄3、1⁄4、1⁄5、1⁄6 或再除以 2/3 的更小分数）；非离散散装（麦片、面粉、干混料）→ 用最接近 RACC 的 household measure；组合食品（花生酱+果冻、煎饼+糖浆）→ 主成分 RACC + 按比例次要成分，单位相容则直接求和，不相容则统一换算为重量再求和（§101.12(f)）。三条都仍以 §101.12 的 RACC 为锚，只是把「按单元数」换成「按分数/按量/按主成分求和」。
- 可回答的新问题：「1⁄5 pizza」是否属于允许的分数集合？组合食品里主成分 RACC 用克、次要成分用毫升，该如何换算？未制备产品（蛋糕粉）的分数应基于整包还是制成的成品？
- 跨域佐证：〔§ 101.12(c)〕未制备产品 RACC = 制成制备态 RACC 所需的未制备量；〔§ 101.9(b)(5)(vii)〕多组分产品可「逐组分」或「composite」声明；〔§ 101.9(h)(1)〕分别包装配料的营养标签落位。
- 建议归属子卡：营养标签与份量

### CAND-FW-27: common household measure 的「可用即优先」递补层级
- 条款出处：〔§ 101.9(b)(5)(i)(ii)(iii)(viii)(ix)〕 + pdf-page 23
- 原文引用（英文逐字，≤100 词/段）：
> For labeling purposes, the term common household measure or common household unit means cup, tablespoon, teaspoon, piece, slice, fraction (e.g., 1⁄4 pizza), ounce (oz), fluid ounce (fl oz), or other common household equipment used to package food products (e.g., jar, tray). In expressing serving size in household measures, except as specified in paragraphs (b)(5)(iv), (b)(5)(v), (b)(5)(vi), and (b)(5)(vii) of this section, the following rules shall be used:
> (i) Cups, tablespoons, or teaspoons shall be used wherever possible and appropriate except for beverages. For beverages, a manufacturer may use fluid ounces. Cups shall be expressed in 1/4- or 1/3-cup increments. ... (ii) If cups, tablespoons or teaspoons are not applicable, units such as piece, slice, tray, jar, and fraction shall be used. (iii) If paragraphs (b)(5)(i) and (b)(5)(ii) of this section are not applicable, ounces may be used with an appropriate visual unit of measure such as a dimension of a piece, e.g., 1 oz (28 g/about 1⁄2 pickle).
> (viii) For nutrition labeling purposes, a teaspoon means 5 milliliters (mL), a tablespoon means 15 mL, a cup means 240 mL, 1 fl oz means 30 mL, and 1 oz in weight means 28 g. (ix) When a serving size, determined from the reference amount in § 101.12(b) and the procedures described in this section, falls exactly half way between two serving sizes, e.g., 2.5 tbsp, manufacturers shall round the serving size up to the next incremental size.
- 方法论陈述：把「serving size 用哪种家用单位写」做成严格递补：第一优先 cup/tbsp/tsp（饮料可用 fl oz，但杯须按 1/4 或 1/3 杯递增）；不适用时降到 piece/slice/tray/jar/fraction；再不适用才允许用 ounce，且必须配一个视觉单位（如 1 oz (28 g/about 1⁄2 pickle)）。(iv)–(vii) 是单份容器、未制备整包、自然变异尺寸、多组分产品的专门改写。收尾两道量化：单位换算由 (viii) 钉死（1 tsp=5 mL、1 cup=240 mL、1 oz=28 g）；落在两档正中时 (ix) 强制向上取整。
- 可回答的新问题：2.5 tbsp 必须向上取到 3 tbsp，会不会因此突破 RACC 而改写声称资格？饮料用 fl oz 时可以再挂 cup 吗？「1 oz (28 g/about 1⁄2 pickle)」里的视觉单位缺失是否构成格式违规？
- 跨域佐证：〔§ 101.9(b)(7)〕serving size 须后接公制等量（fluids 用 mL、其余用 g）；〔§ 101.9(b)(8)〕每容器份数舍入；〔§ 101.12(a)(6)〕RACC 只算可食部分，与视觉单位口径需一致。
- 建议归属子卡：营养标签与份量

### CAND-FW-28: 单份容器 / 促销用途 / 200–300% 的「双列营养标签」触发闸门
- 条款出处：〔§ 101.9(b)(6)〕〔§ 101.9(b)(11)〕〔§ 101.9(b)(12)(i)〕 + pdf-page 24–26
- 原文引用（英文逐字，≤100 词/段）：
> (6) A product that is packaged and sold individually that contains less than 200 percent of the applicable reference amount must be considered to be a single-serving container, and the entire content of the product must be labeled as one serving.
> (11) If a product is promoted on the label, labeling, or advertising for a use that differs in quantity by twofold or greater from the use upon which the reference amount in § 101.12(b) was based (e.g., liquid cream substitutes promoted for use with breakfast cereals), the manufacturer shall provide a second column of nutrition information based on the amount customarily consumed in the promoted use, in addition to the nutrition information per serving derived from the reference amount in § 101.12(b), except that nondiscrete bulk products that are used
> primarily as ingredients (e.g., flour, sweeteners, shortenings, oils), or traditionally used for multipurposes (e.g., eggs, butter, margarine), and multipurpose baking mixes are exempt from this requirement.
> (12)(i) Products that are packaged and sold individually and that contain at least 200 percent and up to and including 300 percent of the applicable reference amount must provide an additional column within the Nutrition Facts label that lists the quantitative amounts and percent Daily Values for the entire package, as well as a column listing the quantitative amounts and percent Daily Values for a serving that is less than the entire package (i.e., the serving size derived from the reference amount).
- 方法论陈述：用「含量相对 RACC 的百分比」和「是否被促销为另一种用量」两条独立触发器决定是否加第二列。① <200% RACC 且独立售卖 → 必须视为单份容器，整包标为一份（不再拆份）；② 200%–300% RACC → 强制双列：一列 per serving（由 RACC 推出），一列 per entire package；③ 产品在 label/labeling/advertising 上被促销的用量与 RACC 依据的用量相差 ≥2 倍 → 须加一列按「促销用量」计算，但主要作配料用的散装品、传统多用途品（蛋、黄油、人造黄油）与多用途烘焙预拌粉豁免。三者可叠加，且 (12)(i)(A)–(C) 又列出 tabular/linear、生鲜自愿标签、已加 (e) 附加列等排除项。
- 可回答的新问题：150%–200% RACC 的产品可以「自愿」加 household measure 列吗？同一产品既 200–300% 又被促销为 2 倍用量，要加几列？「multipurpose」由谁认定，厂商自证还是 FDA 列举？
- 跨域佐证：〔§ 101.9(e)(6)〕双列（per serving / per container / per unit）的格式规格；〔§ 101.9(b)(12)(ii)〕双列产品作声称须附依据声明；〔§ 101.9(d)(11)(j)(13)(ii)(A)〕空间不足时的 tabular/linear 例外。
- 建议归属子卡：营养标签与份量

### CAND-FW-29: 营养素「封闭清单 + 自愿项因作声称/添加而转强制」反转闸门
- 条款出处：〔§ 101.9(c)〕〔§ 101.9(c)(2)(i)(ii)(iii)(iv)〕〔§ 101.9(c)(5)〕〔§ 101.9(c)(6)(i)(A)(B)(iv)〕〔§ 101.9(c)(8)(ii)〕 + pdf-page 26–33
- 原文引用（英文逐字，≤100 词/段）：
> The declaration of nutrition information on the label and in labeling of a food shall contain information about the level of the following nutrients, except for those nutrients whose inclusion, and the declaration of amounts, is voluntary as set forth in this paragraph. No nutrients or food components other than those listed in this paragraph as either mandatory or voluntary may be included within the nutrition label. Except as provided for in paragraphs (f) or (j) of this section, nutrient information shall be presented using the nutrient names specified and
> in the following order in the formats specified in paragraphs (d) or (e) of this section.
> “Fluoride” (VOLUNTARY): A statement of the number of milligrams of fluoride in a specified serving of food may be declared voluntarily, except that when a claim is made about fluoride content, label declaration shall be required.
> “Soluble fiber” (VOLUNTARY): A statement of the number of grams of soluble dietary fiber in a serving may be declared voluntarily except that when a claim is made on the label or in labeling about soluble fiber, label declaration shall be required.
> The declaration of vitamins and minerals shall include any of the other vitamins and minerals listed in paragraph (c)(8)(iv) of this section as a statement of the amount per serving of the vitamins and minerals as described in this paragraph (c)(8)(ii), calculated as a percent of the RDI and expressed as a percent of the Daily Value, when they are added as a nutrient supplement, or when a claim is made about them
- 方法论陈述：先立「封闭清单」——营养标签里只能出现 (c) 列为 mandatory 或 voluntary 的营养素，不得自行增加，且须用规定名称、规定顺序、规定格式。再对每个营养素做二分：强制项照标；标为 (VOLUNTARY) 的项（饱和脂肪附条件、多/单不饱和脂肪、氟化物、可溶/不可溶纤维、糖醇、其他维生素矿物质等）默认可不标，但挂同两条反转条件——「对该营养素作了声称」或「作为营养补充剂添加」即从自愿翻转为强制。这条结构在 (c) 中重复十余次，是判断「某营养素该不该出现在标签上」的通用闸门，也与 FW-22 的「声称击穿豁免」同源。
- 可回答的新问题：标签写了「含膳食纤维」但没声明 soluble fiber，是否漏标？企业能否在 Nutrition Facts 里自行加一项「胶原蛋白」？(c)(2)(iii)/(iv) 的「声明了多不饱和脂肪就须同时标单不饱和脂肪」是双向绑定吗？
- 跨域佐证：〔§ 101.9(f)(2)(iii)(iv)〕简化格式下「作为补充剂添加」的维生素矿物质仍须列入；〔§ 101.9(c)(8)(iii)〕<2% RDI 的维生素矿物质可免标或转底部声明；〔§ 101.13(q)(8)〕瓶装水加氟声明须用简化格式。
- 建议归属子卡：营养标签与份量

### CAND-FW-30: 「不强制申报 → 须置 Not a significant source of __」补偿闸门
- 条款出处：〔§ 101.9(c)(2)(i)(ii)(3)(6)(i)(6)(ii)(6)(iii)(8)(iii)〕〔§ 101.9(f)(4)〕 + pdf-page 27–32 / 53
- 原文引用（英文逐字，≤100 词/段）：
> Except as provided for in paragraph (f) of this section, if a statement of the saturated fat content is not required and, as a result, not declared, the statement “Not a significant source of saturated fat” shall be placed at the bottom of the table of nutrient values.
> Alternatively, except as provided for in paragraph (f) of this section, if vitamin D, calcium, iron, or potassium is present in amounts less than 2 percent of the RDI, label declaration of the nutrient(s) is not required if the statement “Not a significant source of—(listing the vitamins or minerals omitted)” is placed at the bottom of the table of nutrient values.
> If any nutrients are declared as provided in paragraphs (f)(2)(iii), (f)(2)(iv), or (f)(3) of this section as part of the simplified format or if any nutrition claims are made on the label or in labeling, the statement “Not a significant source of ________” (with the blank filled in with the name(s) of any nutrient(s) identified in paragraph (f) of this section that are present in insignificant amounts) shall be included at the bottom of the nutrition label.
- 方法论陈述：与 FW-29 配对使用——当某营养素因「含量低于阈值且未作相关声称」而不必申报时，并非静默省略，而是要在营养表底部补一句 “Not a significant source of …” 把被省略的项列出来，防止消费者误以为「未列＝不含」或「已检测为零」。判定顺序：先判定是否触发免标（如总脂 <0.5 g 且无脂/胆固醇声称、<2 mg 胆固醇、维生素矿物质 <2% RDI）→ 若免标则检查是否有 (f) 简化格式的例外 → 否则加底部声明；(f)(4) 还规定简化格式下只要声明了任何自愿营养素或作了任何营养声称，就必须补该句。
- 可回答的新问题：一个产品同时免标饱和脂肪、反式脂肪、胆固醇，底部要写三句还是合并一句？用了简化格式后底部声明能否省略？把免标项改成自愿声明（标 0 g）后是否仍需底部声明？
- 跨域佐证：〔§ 101.9(c)(8)(iii)〕<2% RDI 可标零/星号或转底部声明的二选一；〔§ 101.9(f)(1)〕「insignificant amount」定义；〔§ 101.11(b)(2)(ii)(B)(3)〕菜单书面营养信息简化格式下同样要求 “Not a significant source of ____”。
- 建议归属子卡：营养标签与份量

### CAND-FW-31: 营养素 / %DV 舍入「按量级分档」阶梯
- 条款出处：〔§ 101.9(c)(1)〕〔§ 101.9(c)(2)〕〔§ 101.9(c)(4)〕〔§ 101.9(c)(8)(iii)〕 + pdf-page 27–33
- 原文引用（英文逐字，≤100 词/段）：
> “Calories, total,” “Total calories,” or “Calories”: A statement of the caloric content per serving, expressed to the nearest 5-calorie increment up to and including 50 calories, and 10-calorie increment above 50 calories, except that amounts less than 5 calories may be expressed as zero.
> “Sodium”: A statement of the number of milligrams of sodium in a specified serving of food expressed as zero when the serving contains less than 5 milligrams of sodium, to the nearest 5-milligram increment when the serving contains 5 to 140 milligrams of sodium, and to the nearest 10-milligram increment when the serving contains greater than 140 milligrams.
> The percentages for vitamins and minerals shall be expressed to the nearest 2-percent increment up to and including the 10-percent level, the nearest 5-percent increment above 10 percent and up to and including the 50-percent level, and the nearest 10-percent increment above the 50-percent level.
- 方法论陈述：把「数值怎么写」做成按量级分段的离散阶梯，而非统一四舍五入：卡路里 ≤50 取 5 卡增量、>50 取 10 卡增量、<5 可写 0；钠 <5 mg 写 0、5–140 mg 取 5 mg 增量、>140 mg 取 10 mg 增量；总脂/饱和脂/反式脂 <5 g 取 0.5 g 增量、>5 g 取 1 g、<0.5 g 写 0；维生素矿物质 %DV ≤10% 取 2% 增量、>10–50% 取 5%、>50% 取 10%。判定时先读实际量 → 落入对应区间 → 按该区间增量表达 → 再检查是否有「可写 0 / less than 1 gram / <2% 可免标」的替代。舍入结果又反过来作 %DV 与声称阈值的输入。
- 可回答的新问题：48 卡是写 50 还是 45？钠 142 mg 该写 140 还是 150？舍入后的标签值能否直接拿来判定 §101.60 的「free」阈值，还是须用 (g)(4)/(5) 的「实际量/复合样」？
- 跨域佐证：〔§ 101.9(d)(7)(ii)〕%DV 按标签声明量或实际量除以 DRV 计算；〔§ 101.9(g)(4)(5)〕合规判定基于复合样的实测值与 80%/120% 容差；〔§ 101.11(b)(2)(i)(A)(2)〕菜单卡路里沿用同一 5/50/10 递增规则。
- 建议归属子卡：营养标签与份量

### CAND-FW-32: 简化格式「≥8 项不显著（婴幼儿 ≥6 项）」触发分流
- 条款出处：〔§ 101.9(f)〕〔§ 101.9(f)(1)(2)(5)〕 + pdf-page 52–53
- 原文引用（英文逐字，≤100 词/段）：
> The declaration of nutrition information may be presented in the simplified format set forth herein when a food product contains insignificant amounts of eight or more of the following: Calories, total fat, saturated fat, trans fat, cholesterol, sodium, total carbohydrate, dietary fiber, total sugars, added sugars, protein, vitamin D, calcium, iron, and potassium; except that for foods intended for infants through 12 months of age and children 1 through 3 years of age to which paragraph (j)(5)(i) of this section applies, nutrition information may be presented in the simplified format
> when a food product contains insignificant amounts of six or more of the following: Calories, total fat, sodium, total carbohydrate, dietary fiber, total sugars, added sugars, protein, vitamin D, calcium, iron, and potassium.
> (1) An “insignificant amount” shall be defined as that amount that allows a declaration of zero in nutrition labeling, except that for total carbohydrate, dietary fiber, and protein, it shall be an amount that allows a declaration of “less than 1 gram.”
> (2) The simplified format shall include information on the following nutrients: (i) Total calories, total fat, total carbohydrate, protein, and sodium; (ii) Any other nutrients identified in paragraph (f) of this section that are present in the food in more than insignificant amounts
- 方法论陈述：先数「不显著项」：在 (f) 列举的 15 项里，达到 ≥8 项不显著（婴幼儿/1–3 岁食品按 (j)(5)(i) 缩短为 12 项里 ≥6 项）才允许启用简化格式。「不显著」由 (f)(1) 定量定义——允许标零，但总碳/膳食纤维/蛋白须「允许标 less than 1 gram」。启用后内容被压缩为：总卡、总脂、总碳、蛋白、钠 + 所有「超过不显著量」的其他项 + 作为补充剂添加或自愿添加的维生素矿物质；其余不显著项不单列，但按 (f)(4)/FW-30 须在底部加 “Not a significant source of ____”。(f)(5) 规定简化格式仍按 (d)/(e) 呈现，只是可省 (d)(9) 脚注。
- 可回答的新问题：恰好 7 项不显著能否用简化格式？婴幼儿食品与普通食品的不显著项清单不同，跨年龄段产品按哪组算？简化格式下作了声称，底部声明与 §101.10 的应请求信息是否双重触发？
- 跨域佐证：〔§ 101.9(j)(4)〕「全部营养素均不显著」是更彻底的整节豁免（仍受 FW-22 声称击穿）；〔§ 101.11(b)(2)(ii)(B)〕菜单书面营养信息用「≥6 项」简化格式，是同构但独立阈值；〔§ 101.9(f)(4)〕简化格式下底部声明义务。
- 建议归属子卡：营养标签与份量

### CAND-FW-33: 营养标签合规「lot → 12 子样 → Class I/II → 80%/120% 容差」判定链
- 条款出处：〔§ 101.9(g)(1)–(6)〕 + pdf-page 53–54
- 原文引用（英文逐字，≤100 词/段）：
> (1) A collection of primary containers or units of the same size, type, and style produced under conditions as nearly uniform as possible, designated by a common container code or marking, or in the absence of any common container code or marking, a day's production, constitutes a “lot.” (2) The sample for nutrient analysis shall consist of a composite of 12 subsamples (consumer units), taken 1 from each of 12 different randomly chosen shipping cases, to be representative of a lot.
> (3) Two classes of nutrients are defined for purposes of compliance: (i) Class I. Added nutrients in fortified or fabricated foods; and (ii) Class II. Naturally occurring (indigenous) nutrients.
> (ii) When a vitamin, mineral, protein, total carbohydrate, polyunsaturated or monounsaturated fat, or dietary fiber meets the definition of a Class II nutrient, the nutrient content of the composite must be at least equal to 80 percent of the value for that nutrient declared on the label.
> (5) A food with a label declaration of calories, total sugars, added sugars (when the only source of sugars in the food is added sugars), total fat, saturated fat, trans fat, cholesterol, or sodium shall be deemed to be misbranded under section 403(a) of the act if the nutrient content of the composite is greater than 20 percent in excess of the value for that nutrient declared on the label.
- 方法论陈述：这是把「标签数字是否属实」变成可执法检查的判定链。① 先定义 lot（同规格、近似均匀条件、共同容器代码，无代码则按一天产量）；② 取样固定为 12 个 consumer units 的复合样，分别取自 12 个随机挑选的运输箱；③ 把营养素分两类：Class I＝强化/配制食品中添加的营养素（要求复合样 ≥ 标签值），Class II＝天然固有营养素（要求复合样 ≥ 标签值的 80%）；④ 对「应限制」的项（卡路里、糖、总脂、饱和脂、反式脂、胆固醇、钠）反向设 120% 上限——实测超过标签值 20% 即按 403(a) 错标。⑤ (g)(4)/(g)(5) 都附「分析方法固有变异内不采取监管行动」的缓冲，(g)(6) 允许 cGMP 下的合理过量/不足，(g)(7) 指定以标签 serving size 的公制量为基准。
- 可回答的新问题：一批产品既有天然维C又外源添加维C，按 Class I 还是 Class II 判定？12 子样复合后平均值合格但个别单元偏低，是否仍可开观察项？(g)(5) 的 120% 上限与 §101.60 的「free」阈值能否互相替代？
- 跨域佐证：〔§ 101.9(g)(8)〕FDA 批准数据库可替代 (g)(1)–(6) 的取样合规；〔§ 101.9(g)(10)(11)〕膳食纤维/添加糖/叶酸等须留存 2 年记录，缺失即按 403(a)(1) 错标；〔§ 101.11(c)(2)(3)〕菜单营养数据「合理依据 + 按方法举证」是同构但不同制度。
- 建议归属子卡：营养标签与份量

### CAND-FW-34: 「技术不可行 / FDA 批准数据库 / 请愿」三条替代合规通道
- 条款出处：〔§ 101.9(g)(8)〕〔§ 101.9(g)(9)〕〔§ 101.9(g)(10)(v)(C)〕 + pdf-page 55–56
- 原文引用（英文逐字，≤100 词/段）：
> Alternatively, compliance with the provisions set forth in paragraphs (g)(1) through (6) of this section may be provided by use of an FDA approved database that has been computed following FDA guideline procedures and where food samples have been handled in accordance with current good manufacturing practice to prevent nutrition loss. FDA approval of a database shall not be considered granted until the Center for Food Safety and Applied Nutrition has agreed to all aspects of the database in writing.
> When it is not technologically feasible, or some other circumstance makes it impracticable, for firms to comply with the requirements of this section (e.g., to develop adequate nutrient profiles to comply with the requirements of paragraph (c) of this section), FDA may permit alternative means of compliance or additional exemptions to deal with the situation. Firms in need of such special allowances shall make their request in writing to the Center for Food Safety and Applied Nutrition
> (C) Submit a petition, under 21 CFR 10.30, to request an alternative means of compliance.
- 方法论陈述：当 FW-33 的常规取样/分析方法不可行时，开三条互斥或并行的替代通道：① 用经 FDA 书面批准的营养数据库替代 (g)(1)–(6) 的复合样合规（须按 FDA 指南计算、样品按 cGMP 处理防营养损失、批准有期限如 10 年且可续、请求按 §10.30 提交）；② 因技术上不可行或其他情形不切实际（如无法建立足够营养剖面）→ 书面请求 FDA 给予替代合规手段或额外豁免；③ 具体难题（如发酵/非酶褐变导致添加糖无法合理估算）→ 按 21 CFR 10.30 请愿请求替代合规手段，并附科学数据说明为何无法合理近似。共同结构是「默认合规路径 → 证明不可行 → 书面/请愿 → FDA 个案裁量」，企业不得自行减免。
- 可回答的新问题：用了未获书面批准的商业数据库，能否在检查时抗辩？「技术上不可行」由谁举证、与 §101.12(h) 的 RACC 请愿是同一程序吗？数据库批准 10 年到期后未续，期间标签是否立即失合规？
- 跨域佐证：〔§ 101.12(h)〕专员可依职权或依 part 10 请愿修订 RACC；〔§ 101.2(f)〕小包装替代传播方式须按 part 10 请愿；〔§ 101.108〕FDA 书面提案批准下的临时标签实验豁免（另一类「个案裁量」通道）。
- 建议归属子卡：豁免与效力层

### CAND-FW-35: 多包装 / 组合 / 礼品包 / 需制备食品的营养标签落位分流
- 条款出处：〔§ 101.9(h)(1)(2)(3)(4)〕 + pdf-page 56–57
- 原文引用（英文逐字，≤100 词/段）：
> (1) If a product consists of two or more separately packaged ingredients enclosed in an outer container or of assortments of the same type of food (e.g., assorted nuts or candy mixtures) in the same retail package, nutrition labeling shall be located on the outer container or retail package (as the case may be) to provide information for the consumer at the point of purchase. However, when two or more food products are simply combined together in such a manner that no outer container is used, or no outer label
> is available, each product shall have its own nutrition information, e.g., two boxes taped together or two cans combined in a clear plastic overwrap.
> (2) If a product consists of two or more separately packaged foods that are intended to be eaten individually and that are enclosed in an outer container (e.g., variety packs of cereals or snack foods), the nutrition information shall: (i) Be specified per serving for each food in a location that is clearly visible to the consumer at the point of purchase; and (ii) Be presented in separate nutrition labels or in one aggregate nutrition label with separate columns for the quantitative amount by weight and the percent Daily Value for each food.
> (ii) In the absence of a reference amount customarily consumed in § 101.12(b) that is appropriate for the variety or assortment of foods in a gift package, the following may be used as the standard serving size for purposes of nutrition labeling of foods subject to this paragraph: 1 ounce for solid foods; 2 fluid ounces for nonbeverage liquids (e.g., syrups); 8 ounces for beverages that consist of milk and fruit juices, nectars and fruit drinks; and 12 fluid ounces for other beverages. However, the reference amounts customarily consumed in
> § 101.12(b) shall be used for purposes of evaluating whether individual foods in a gift package qualify for nutrient content claims or health claims.
- 方法论陈述：按「有没有外容器/外标签」和「是否分别食用」两条轴分流：有外容器 → 营养标签放外容器（购买点可见）；无外容器（两盒胶带捆绑、透明收缩膜）→ 每个产品各自带营养信息；分别食用的 variety pack → 每种食品按份列出，或用一张 aggregate 标签为每种食品各列一列。礼品包 (h)(3) 更进一步：§101.12(b) 无合适 RACC 时，允许用法定「替代标准份量」（固体 1 oz、非饮料液体 2 fl oz、含乳/果汁饮料 8 oz、其他饮料 12 fl oz），但**判定单个食品是否有资格作含量/健康声称，仍必须回到 §101.12(b) RACC**——替代份量只解决「标签怎么写」，不解决「声称能不能作」。(h)(4) 对需加配料/烹调的食品允许加「as consumed」列，但须显著标明所加配料与制法。
- 可回答的新问题：礼品包用 1 oz 标准份量写的 Nutrition Facts，能否据以宣称「low calorie」？两盒胶带捆绑销售但共用一张外贴标签，是否算「有 outer label」？aggregate 标签与 (d)(13) 的 aggregate display 是同一规则吗？
- 跨域佐证：〔§ 101.9(d)(13)〕variety pack 的 aggregate display 格式；〔§ 101.12(f)〕组合产品 RACC 求和；〔§ 101.9(b)(2)(iii)〕散装/组合产品 serving size 按 household measure 取近似 RACC。
- 建议归属子卡：营养标签与份量

### CAND-FW-36: §101.9(j) 豁免清单「主体 / 客体 / 附带条件」三层切分
- 条款出处：〔§ 101.9(j)(1)–(18)〕 + pdf-page 58–66
- 原文引用（英文逐字，≤100 词/段）：
> The following foods are exempt from this section or are subject to special labeling requirements:
> (6) Dietary supplements, except that such foods shall be labeled in compliance with § 101.36. (7) Infant formula subject to section 412 of the act, as amended, except that such foods shall be labeled in compliance with part 107 of this chapter.
> (8) Medical foods as defined in section 5(b) of the Orphan Drug Act (21 U.S.C. 360ee(b)(3)). ... A food is subject to this exemption only if: (i) It is a specially formulated and processed product (as opposed to a naturally occurring foodstuff used in its natural state) for the partial or exclusive feeding of a patient by means of oral intake or enteral feeding by tube; (ii) It is intended for the dietary management of a patient who, because of therapeutic or chronic medical needs, has limited or impaired capacity
> to ingest, digest, absorb, or metabolize ordinary foodstuffs or certain nutrients
> (13)(i) Foods in small packages that have a total surface area available to bear labeling of less than 12 square inches, Provided, That the labels for these foods bear no nutrition claims or other nutrition information in any context on the label or in labeling or advertising, except as provided in § 101.8(c).
- 方法论陈述：(j) 的 18 项不是同质清单，判定要分三层：① 主体豁免——(j)(1) 小企业直销（$500,000 / $50,000 销售额）、(j)(18) 低产量小企业（员工数 + 销量）；② 客体/场景豁免——(j)(2)(3) 餐馆/即食场所、(j)(9) 散装、(j)(10) 生鲜果蔬鱼、(j)(13) 小包装、(j)(14) 蛋盒、(j)(15) multiunit 内单元、(j)(16) 散装容器；③ 转介式豁免——(j)(5) 婴幼儿食品/配方「改为须标」、(j)(6) 膳补转 §101.36、(j)(7) 婴儿配方转 part 107、(j)(8) medical foods 须逐项满足 (i)–(v) 五条件才免。每项再挂 FW-22 的「无声称/无营养信息」持续条件与 (j)(13)(i)(A) 的「提供地址/电话可索取信息」等附带义务。这套豁免只免 §101.9 营养标签，与 §101.100 免配料表、§101.108 免临时实验、Part 117 主体豁免互不通用。
- 可回答的新问题：medical foods 少满足 (v)「持续医疗监督」一项，是否整体回落 §101.9？膳补产品「免 §101.9」是不是等于「免一切标签义务」？multiunit 内单元未印 “This Unit Not Labeled For Retail Sale” 时豁免是否失效？
- 跨域佐证：〔§ 101.36〕膳补专用营养标签；〔§ 101.100〕配料表义务豁免（不同对象）；〔§ 101.108〕临时标签实验豁免（不同对象）；〔§ 101.9(j)(18)(iv)〕低产量豁免须提交 notice。
- 建议归属子卡：豁免与效力层

### CAND-FW-37: 小企业低产量豁免「双阈值 + 事前申报 + 失效后 18 个月」链
- 条款出处：〔§ 101.9(j)(18)(i)–(vi)〕 + pdf-page 65–67
- 原文引用（英文逐字，≤100 词/段）：
> (18) Food products that are low-volume (that is, they meet the requirements for units sold in paragraphs (j)(18)(i) or (j)(18)(ii) of this section); that, except as provided in paragraph (j)(18)(iv) of this section, are the subject of a claim for an exemption that provides the information required under paragraph (j)(18)(iv) of this section, that is filed before the beginning of the time period for which the exemption is claimed, and that is filed by a person, whether it is the manufacturer, packer, or distributor, that qualifies to claim the exemption
> under the requirements for average full-time equivalent employees in paragraphs (j)(18)(i) or (j)(18)(ii) of this section; and whose labels, labeling, and advertising do not provide nutrition information or make a nutrient content or health claim.
> (ii) For all other food products, the product shall be eligible for an exemption for any 12-month period if, for the preceding 12 months, the person claiming the exemption employed fewer than an average of 100 full-time equivalent employees and fewer than 100,000 units of that product were sold in the United States
> (iii) If a person claims an exemption under paragraphs (j)(18)(i) or (j)(18)(ii) of this section for a food product and then, during the period of such exemption, the number of full-time equivalent employees of such person exceeds the appropriate number, or the number of food products sold in the United States exceeds the appropriate number, or, if at the end of the period of such exemption, the food product no longer qualifies for an exemption under the provisions of paragraphs (j)(18)(i) or (j)(18)(ii) of this section, such person shall have
> 18 months from the date that the product was no longer qualified as a low-volume product of a small business to comply with this section.
- 方法论陈述：四道串联要件：① 双阈值同时满足——平均全职当量员工数（(i)/(ii) 按产品首次进入州际 commerce 的年代分 300/200/100 人档）与在美销量（400,000/200,000/100,000 单位档），FTE 按「全年工资小时数 ÷ 2,080」算且含境内外关联方；② 事前申报——在所主张期间开始前，由合格主体向 FDA 提交含 (iv)(A)–(F) 信息的 notice 并由负责人签字认证（<10 FTE 且年销量 <10,000 单位的非进口商可免申报）；③ 持续条件——label/labeling/advertising 不提供营养信息、不作含量或健康声称（回到 FW-22）；④ 失效补救——员工数或销量超标、或期末不再合格时，自「不再合格之日」起有 18 个月完成合规。这是「阈值 → 申报 → 持续沉默 → 失效宽限」的时间轴框架。
- 可回答的新问题：外资企业在美销量与全球员工数如何折算进阈值？notice 晚交一天是否整体失权，还是只是该期间不生效？18 个月宽限期内产品已在零售架上，是否算错标？
- 跨域佐证：〔§ 101.9(j)(1)(ii)〕销售额按最近 2 年平均、外资按在美业务计——同类「主体规模量化」；〔§ 101.9(g)(11)〕记录留存 2 年；〔§ 101.11(d)(5)〕/〔§ 101.8(d)(4)(vii)〕注册每两年续期、自动失效（另一类时间轴）。
- 建议归属子卡：豁免与效力层

### CAND-FW-38: 「暗示/建议/隐含疾病预防表述 → 只能走 §101.14 + Subpart E」闸门
- 条款出处：〔§ 101.9(k)〕 + pdf-page 67
- 原文引用（英文逐字，≤100 词/段）：
> A food labeled under the provisions of this section shall be deemed to be misbranded under sections 201(n) and 403(a) of the act if its label or labeling represents, suggests, or implies: (1) That the food, because of the presence or absence of certain dietary properties, is adequate or effective in the prevention, cure, mitigation, or treatment of any disease or symptom. Information about the relationship of a dietary property to a disease or health-related condition may only be provided in conformance with the requirements of § 101.14 and part 101, subpart E.
> (2) That the lack of optimum nutritive quality of a food, by reason of the soil on which that food was grown, is or may be responsible for an inadequacy or deficiency in the quality of the daily diet. (3) That the storage, transportation, processing, or cooking of a food is or may be responsible for an inadequacy or deficiency in the quality of the daily diet. (4) That a natural vitamin in a food is superior to an added or synthetic vitamin.
- 方法论陈述：这是从「营养标签合规」跨到「声称闸门」的接口。即便 Nutrition Facts 完全合规，只要 label/labeling 以 represents / suggests / implies 三种方式之一暗示食品能预防、治愈、缓解、治疗疾病或症状，即按 201(n)/403(a) 错标；唯一合法出口是「按 §101.14 与 Subpart E 已授权健康声称的模型措辞与条件」提供该物质—疾病关系信息。另列三类绝对禁止的暗示（土壤导致营养不足、储运加工烹调导致日常膳食不足、天然维生素优于添加/合成维生素）。判定关键是「暗示与明示同等受管」，而非只查有没有直白说「治癌」。
- 可回答的新问题：包装上一个心形符号 + 「heart healthy」是否落入 suggests/implies？「天然维C优于合成维C」为何被单独列为错标而非交给声称授权？合规 Nutrition Facts 能否为 (k)(1) 的暗示提供抗辩？
- 跨域佐证：〔§ 101.14(a)(1)〕健康声称定义含 heart 符号、品牌名、第三方文献引用等暗示形式；〔§ 101.14(e)〕未授权声称的错标后果；〔§ 101.70〕请愿授权新健康声称是唯一扩张通道。
- 建议归属子卡：声称闸门

### CAND-FW-39: RACC 派生链「未制备 / 仿制改型 / 充气 / 组合」四类改写
- 条款出处：〔§ 101.12(c)(d)(e)(f)〕 + pdf-page 196–197
- 原文引用（英文逐字，≤100 词/段）：
> (c) If a product requires further preparation, e.g., cooking or the addition of water or other ingredients, and if paragraph (b) of this section provides a reference amount for the product in the prepared form, but not the unprepared form, then the reference amount for the unprepared product must be the amount of the unprepared product required to make the reference amount for the prepared product as established in paragraph (b) of this section.
> (d) The reference amount for an imitation or substitute food or altered food, such as a “low calorie” version, shall be the same as for the food for which it is offered as a substitute.
> (e) If a food is modified by incorporating air (aerated), and thereby the density of the food is lowered by 25 percent or more in weight than that of an appropriate reference regular food as described in § 101.13(j)(1)(ii)(A), and the reference amount of the regular food is in grams, the manufacturer may determine the reference amount of the aerated food by adjusting for the difference in density of the aerated food relative to the density of the appropriate reference food provided that the manufacturer will show FDA detailed protocol
> and records of all data that were used to determine the density-adjusted reference amount for the aerated food.
> (1) The reference amount for the combined product must be the reference amount, as established in paragraph (b) of this section, for the ingredient that is represented as the main ingredient (e.g., peanut butter, pancakes, cake) plus proportioned amounts of all minor ingredients. (2) If the reference amounts are in compatible units, the weights or volumes must be summed
- 方法论陈述：当 §101.12(b) 表里查不到该产品形态时，按四类派生规则补出 RACC：① 未制备产品 → 取「制成制备态 RACC 所需的未制备产品量」；② 仿制/替代/改型（如 low calorie 版）→ 直接沿用被替代食品的 RACC（防止靠改配方洗掉比较基准）；③ 充气使密度比参照常规食品低 ≥25% 且参照 RACC 以克计 → 可按密度差调整 RACC、就近取 5 g 增量，但须标 whipped/aerated 描述词、向 FDA 出示完整方案与记录，且蛋糕类除芝士蛋糕外禁用；④ 组合食品 → 主成分 RACC + 按比例次要成分，单位相容直接求和、不相容统一换算为重量求和。四条都是「先查表 → 查不到才派生 → 派生须可举证」的补链。
- 可回答的新问题：「低脂版」饼干的 RACC 能否因配方变轻而下调？充气产品密度差 24.9% 时能否援引 (e)？组合产品主成分用杯、次要成分用克，(f)(2) 要求换算成重量后是否还与 (a)(6) 的「可食部分」一致？
- 跨域佐证：〔§ 101.9(b)(2)(ii)(iii)〕serving size 对大离散单元/散装/组合产品的分流；〔§ 101.13(j)(1)(ii)(A)〕(e) 转引的参照常规食品定义；〔§ 101.3(e)〕imitation 判定（(d) 的「替代」前提）。
- 建议归属子卡：营养标签与份量

### CAND-FW-40: RACC 作为声称资格分母 + 「serving size≠RACC 须附依据声明」★
- 条款出处：〔§ 101.12(g)〕〔§ 101.9(b)(12)(ii)〕 + pdf-page 197 / 26
- 原文引用（英文逐字，≤100 词/段）：
> (g) The reference amounts set forth in paragraphs (b) through (f) of this section shall be used in determining whether a product meets the criteria for nutrient content claims, such as “low calorie,” and for health claims. If the serving size declared on the product label differs from the reference amount, and the product meets the criteria for the claim only on the basis of the reference amount, the claim shall be followed by a statement that sets forth the basis on which the claim is made. That statement shall
> include the reference amount as it appears in paragraph (b) of this section followed, in parenthesis, by the amount in common household measure if the reference amount is expressed in measures other than common household measures (e.g., for a beverage, “Very low sodium, 35 mg or less per 240 mL (8 fl oz)”).
> When a nutrient content claim or health claim is made on the label of a product that uses a dual column as required in paragraph (b)(2)(i)(D) or (b)(12)(i) of this section, the claim must be followed by a statement that sets forth the basis on which the claim is made, except that the statement is not required for products when the nutrient that is the subject of the claim meets the criteria for the claim based on the reference amount for the product and the entire container or the unit
> amount. When a nutrient content claim is made, the statement must express that the claim refers to the amount of the nutrient per serving (e.g., “good source of calcium per serving” or “per X [insert unit]__serving”) or per reference amount
- 方法论陈述：这是「份量体系」与「声称闸门」的法定接口。第一句把 §101.12(b)–(f) 的 RACC 钉为判定含量声称（如 low calorie）与健康声称资格的分母——不是厂商自定的标签 serving size。由此产生分岔：若标签 serving size ≠ RACC，且产品「仅在 RACC 基础上」才满足声称条件，则声称后必须附「依据声明」，写明 RACC 并在非家用单位时括注 household measure（如 “Very low sodium, 35 mg or less per 240 mL (8 fl oz)”）。双列产品 (b)(12)(ii) 复用同一逻辑：作声称须附依据声明，但若该营养素按 RACC 与整包/单元量都满足声称条件则可免。含量声称的依据声明要写「per serving」或「per reference amount」，健康声称则用固定句式 “A serving of __ounces of this product conforms to such a diet.”
- 可回答的新问题：产品把 serving size 调小到刚好让「低钠」成立，能否绕开 RACC 分母？依据声明写「per serving」还是「per RACC」由谁决定？双列产品两种口径都合格时厂商能否自愿省略依据声明？
- 跨域佐证：〔§ 101.9(b)(2)〕serving size 由 RACC 推导的程序；〔§ 101.13〕/〔§ 101.14〕含量与健康声称阈值以 RACC/per labeled serving 表述；〔§ 101.9(b)(11)(b)(12)(i)〕双列触发条件。
- 建议归属子卡：声称闸门

### CAND-FW-41: 请愿建立 / 修订 RACC 的「14 项要件 + 新子类别额外数据」程序闸门
- 条款出处：〔§ 101.12(h)〕〔§ 101.12(h)(11)(12)(13)(14)〕 + pdf-page 197–198
- 原文引用（英文逐字，≤100 词/段）：
> (h) The Commissioner of Food and Drugs, either on his or her own initiative or in response to a petition submitted pursuant to part 10 of this chapter, may issue a proposal to establish or amend a reference amount in paragraph (b) of this section. A petition to establish or amend a reference amount shall include: (1) Objective of the petition; (2) A description of the product; (3) A complete sample product label including nutrition label, using the format established by regulation; (4) A description of the form (e.g., dry
> mix, frozen dough) in which the product will be marketed; (5) The intended dietary uses of the product with the major use identified (e.g., milk as a beverage and chips as a snack);
> (9) The suggested reference amount (the amount of edible portion of food as consumed, excluding bone, seed, shell, or other inedible components) for the population group for which the product is intended with full description of the methodology and procedures that were used to determine the suggested reference amount. In determining the reference amount, general principles and factors in paragraph (a) of this section should be followed.
> (11) A petition to create a new subcategory of food with its own reference amount shall include the following additional information: (i) Data that demonstrate that the new subcategory of food will be consumed in amounts that differ enough from the reference amount for the parent category to warrant a separate reference amount. Data must include sample size; and the mean, standard deviation, median, and modal consumed amount per eating occasion for the petitioned product and for other products in the category, excluding the petitioned product. All data must be derived from the same survey data.
- 方法论陈述：RACC 表不是厂商可自行解释的开放清单，扩张只有两条入口：专员依职权，或利害关系人按 part 10 请愿。请愿须逐项提交 (1)–(14)：目标、产品描述、完整样标、上市形态、预期膳食用途（须标主要用途）、作配料时的食品类别与优先序、目标人群、最相近产品（替代/仿制则列被替代对象）、建议 RACC（只算可食部分）及完整方法论（须遵循 (a) 的一般原则）、公制表达（液体 mL、>30 mL 取 30 倍数、克数 >10 g 取最近 5 g 增量）、环境评估或 categorical exclusion、消费数据研究指南、协商立法可行性声明。若还要「新建子类别」，(11) 追加硬证据：同一调查数据下的样本量、均值/标准差/中位数/众数，证明该子类别惯常消费量与母类别差异足够大。
- 可回答的新问题：一个 Table 2 查不到的新品类，能否直接按 (a)(9)「相似性」类推而不请愿？请愿数据用了两套不同调查来源会不会被 (11)(i) 直接驳回？建议 RACC 写成「杯」而非公制是否符合 (10)？
- 跨域佐证：〔§ 101.12(a)〕(1)–(9) 一般原则与因素是 (9) 的方法论依据；〔§ 101.2(f)〕/〔§ 101.9(g)(10)(v)(C)〕其他 part 10 / §10.30 请愿通道；〔§ 101.69〕/〔§ 101.70〕营养素含量声称与健康声称请愿（同一「请愿扩张授权清单」家族）。
- 建议归属子卡：豁免与效力层

### CAND-FW-42: 营养素含量声称「默认禁止 + 须依规章授权」+ express/implied 二分
- 条款出处：〔§ 101.13(b)(1)(2)(3)〕 + pdf-page 199
- 原文引用（英文逐字，≤100 词/段）：
> A claim that expressly or implicitly characterizes the level of a nutrient of the type required to be in nutrition labeling under § 101.9 or under § 101.36 (that is, a nutrient content claim) may not be made on the label or in labeling of foods unless the claim is made in accordance with this regulation and with the applicable regulations in subpart D of this part or in part 105 or part 107 of this chapter.
> (1) An expressed nutrient content claim is any direct statement about the level (or range) of a nutrient in the food, e.g., “low sodium” or “contains 100 calories.” (2) An implied nutrient content claim is any claim that: (i) Describes the food or an ingredient therein in a manner that suggests that a nutrient is absent or present in a certain amount (e.g., “high in oat bran”); or (ii) Suggests that a food, because of its nutrient content, may be useful in maintaining healthy dietary practices, where there is also
> implied or explicit information about the nutrition content of the food (e.g., “healthy”).
> (3) Except for claims regarding vitamins and minerals described in paragraph (q)(3) of this section, no nutrient content claims may be made on food intended specifically for use by infants and children less than 2 years of age unless the claim is specifically provided for in parts 101, 105, or 107 of this chapter.
- 方法论陈述：先立负面清单——凡表征 §101.9/§101.36 要求标示营养素水平的声称，一律不得作，除非「按本规章 + Subpart D 逐词定义（或 part 105/107）」作出。再对「什么算声称」二分：expressed＝直说水平或范围（"low sodium"、"contains 100 calories"）；implied＝描述方式暗示某营养素有无/多少（"high in oat bran"），或暗示因营养内容有助于维持健康膳食且伴随营养信息（"healthy"）。两者同等受管，判定不看措辞直白与否。再叠加两道特殊闸门：婴幼儿（<2 岁）食品除 (q)(3) 维生素矿物质百分比外一律不得作含量声称；膳补对卡路里/脂肪等的声称另有 (b)(5) 限制；(b)(4) 只允许不误导的拼写变体（hi/lo）。
- 可回答的新问题：品牌名里含 "Light" 但没写营养素，算不算 implied claim？「healthy」这个词为何要等 Subpart D 定义才能用？<2 岁食品写「含钙」是否能套 (q)(3)？
- 跨域佐证：〔§ 101.13(q)(7)〕品牌名中的 implied claim 须经 FDA 授权、按 §101.69(o) 请愿；〔§ 101.14(a)(1)〕健康声称同样把 brand name/符号/vignette 纳入 implied；〔§ 101.13(n)〕作含量声称即须提供营养标签。
- 建议归属子卡：声称闸门

### CAND-FW-43: 「营养标签内 ≠ 声称；营养标签外 = 声称」位置判定链
- 条款出处：〔§ 101.13(c)〕 + pdf-page 199
- 原文引用（英文逐字，≤100 词/段）：
> Information that is required or permitted by § 101.9 or § 101.36, as applicable, to be declared in nutrition labeling, and that appears as part of the nutrition label, is not a nutrient content claim and is not subject to the requirements of this section. If such information is declared elsewhere on the label or in labeling, it is a nutrient content claim and is subject to the requirements for nutrient content claims.
- 方法论陈述：同一串数字（如 "0 g fat"、"200 mg sodium"）是否构成受管声称，取决于它「出现在哪」。判定顺序：先确认该信息是 §101.9/§101.36 要求或允许在营养标签中申报的项目 → 若它作为 Nutrition Facts 的一部分出现 → 不是声称、不受 §101.13 约束；若同一信息出现在标签/labeling 的其他任何位置（正面、广告、宣传单）→ 立即 becoming 含量声称，须满足 §101.13 与 Subpart D 的全部定义与披露义务。这是一条纯「位置分流」闸门，与信息内容无关。
- 可回答的新问题：把 Nutrition Facts 里的 "0 g trans fat" 原样印到包装正面，是否需要满足 "trans fat free" 的逐词定义？官网产品页引用营养标签数字算不算「elsewhere in labeling」？§101.9(j)(13)(i)(A) 提供的电话索取营养信息是否落入本款？
- 跨域佐证：〔§ 101.13(i)〕在别处陈述营养素量/百分比的三分岔；〔§ 101.9(a)(3)〕营养信息回复不使豁免失效；〔§ 101.10〕餐馆声称触发营养信息义务。
- 建议归属子卡：声称闸门

### CAND-FW-44: 「free / low 须经特殊加工，否则须改说 inherent + 指向全类」判定链
- 条款出处：〔§ 101.13(e)(1)(2)〕 + pdf-page 199
- 原文引用（英文逐字，≤100 词/段）：
> Because the use of a “free” or “low” claim before the name of a food implies that the food differs from other foods of the same type by virtue of its having a lower amount of the nutrient, only foods that have been specially processed, altered, formulated, or reformulated so as to lower the amount of the nutrient in the food, remove the nutrient from the food, or not include the nutrient in the food, may bear such a claim (e.g., “low sodium potato chips”).
> (2) Any claim for the absence of a nutrient in a food, or that a food is low in a nutrient when the food has not been specially processed, altered, formulated, or reformulated to qualify for that claim shall indicate that the food inherently meets the criteria and shall clearly refer to all foods of that type and not merely to the particular brand to which the labeling attaches (e.g., “corn oil, a sodium-free food”).
- 方法论陈述：先解释立法理由——把 "free/low" 放在品名前会暗示「本产品比同类低」，因此只有经 specially processed / altered / formulated / reformulated 以降低、去除或不加入该营养素的食品才可作此声称。分岔：若产品天生就低/不含（未作特殊加工），仍可说，但必须改为「该食品 inherent 满足标准」并且措辞指向该类型全部食品，而不能只绑定自己的品牌（如 "corn oil, a sodium-free food"，不能写 "Brand X sodium free"）。这是「声称资格 → 加工史举证 → 措辞范围」三段链。
- 可回答的新问题：天然无钠的矿泉水写 "Brand X sodium free" 为什么违规？「低脂」声称的举证材料是配方记录还是检测结果？把天生低脂产品做了一道无关工序，能否算 specially processed？
- 跨域佐证：〔§ 101.13(d)〕substitute 食品定义与 disclaimer（同为「相对差异」类判定）；〔§ 101.13(j)(3)〕参照食品已达 low 标准时不得再作 reduced 声称；〔§ 101.62(b)(1)〕"fat free" 的逐词阈值。
- 建议归属子卡：声称闸门

### CAND-FW-45: 高脂/高钠触发 disclosure + 「most prominent claim」四级定位
- 条款出处：〔§ 101.13(h)(1)(4)〕〔§ 101.13(j)(2)(iii)〕 + pdf-page 199–203
- 原文引用（英文逐字，≤100 词/段）：
> (1) If a food, except a meal product as defined in § 101.13(l), a main dish product as defined in § 101.13(m), or food intended specifically for use by infants and children less than 2 years of age, contains more than 13.0 g of fat, 4.0 g of saturated fat, 60 milligrams (mg) of cholesterol, or 480 mg of sodium per reference amount customarily consumed, per labeled serving, or, for a food with a reference amount customarily consumed of 30 g or less or 2 tablespoons or less, per 50 g
> then that food must bear a statement disclosing that the nutrient exceeding the specified level is present in the food as follows: “See nutrition information for ____ content” with the blank filled in with the identity of the nutrient exceeding the specified level, e.g., “See nutrition information for fat content.”
> (iii) The determination of which use of the claim is in the most prominent location on the label or labeling will be made based on the following factors, considered in order: (A) A claim on the principal display panel adjacent to the statement of identity; (B) A claim elsewhere on the principal display panel; (C) A claim on the information panel; or (D) A claim elsewhere on the label or labeling.
- 方法论陈述：两条量化/定位闸门。① 只要产品（排除 meal/main dish/<2 岁食品）任一指标超过 13.0 g 脂 / 4.0 g 饱和脂 / 60 mg 胆固醇 / 480 mg 钠（按 per RACC、per labeled serving，小 RACC 食品按 per 50 g），一旦又作了含量声称，就须在紧邻处加 disclosure "See nutrition information for ___ content"；meal/main dish 用 (h)(2)(3) 的加倍阈值。② 所有「须紧邻最显著声称」的附加信息（disclosure、relative claim 的参照食品与百分比）落位靠 (j)(2)(iii) 的四级优先顺序判定：PDP 上紧邻品名 > PDP 其他位置 > 信息面板 > 其他标签/labeling。(h)(4)(ii)(iii) 再规定紧邻、无插入材料、多声称时可只放一处且对齐最大字号那条。
- 可回答的新问题：一个产品同时超脂肪和钠阈值，disclosure 要写两句吗？同一声称在 PDP 与信息面板各出现一次，disclosure 放哪？"(h)(1)" 的 13 g 与 §101.14(a)(4) 的 disqualifying level 是同一组数，结论是否相同？
- 跨域佐证：〔§ 101.14(a)(4)(e)(3)〕同一组数值作为健康声称 disqualifying level，且 (e)(3) 允许在超阈值时以 §101.13(h) disclosure 换取声称；〔§ 101.13(i)(2)〕不符定义陈述的 disclaimer 也须紧邻；〔§ 101.7(i)〕disclosure 字号下限回指净含量字号规格。
- 建议归属子卡：声称闸门

### CAND-FW-46: 陈述营养素量/百分比「符合定义 / 不符定义带 disclaimer / 完全不暗示」三分岔
- 条款出处：〔§ 101.13(i)(1)(2)(3)(4)〕 + pdf-page 201
- 原文引用（英文逐字，≤100 词/段）：
> Except as provided in § 101.9 or § 101.36, as applicable, or in paragraph (q)(3) of this section, the label or labeling of a product may contain a statement about the amount or percentage of a nutrient if:
> (2) The use of the statement on the food implicitly characterizes the level of the nutrient in the food and is not consistent with such a definition, but the label carries a disclaimer adjacent to the statement that the food is not “low” in or a “good source” of the nutrient, such as “only 200 mg sodium per serving, not a low sodium food.”
> (3) The statement does not in any way implicitly characterize the level of the nutrient in the food and it is not false or misleading in any respect (e.g., “100 calories” or “5 grams of fat”), in which case no disclaimer is required.
> (4) “Percent fat free” claims are not authorized by this paragraph. Such claims shall comply with § 101.62(b)(6).
- 方法论陈述：在营养标签之外写「某营养素含量/百分比」时，按「是否隐含表征水平 + 是否符合 Subpart D 定义」两轴三分流：① 暗示水平且符合某声称定义 → 该陈述本身就是含量声称，按该定义走（如 "less than 3 g of fat per serving"）；② 暗示水平但不符合定义 → 须紧邻加 disclaimer 声明「并非 low / 并非 good source」（如 "only 200 mg sodium per serving, not a low sodium food"）；③ 完全不暗示水平且不误导（如中性陈述 "100 calories"、"5 grams of fat"）→ 无需 disclaimer。收尾 (4) 单独封死 "percent fat free"：不归本款，须按 §101.62(b)(6)。disclaimer 的字号下限回指 §101.7(i)。
- 可回答的新问题："只有 5 g 脂肪" 里的「只有」是否把中性陈述推入 (2)？(3) 的中性陈述放在 PDP 大字是否仍算「不暗示」？"% fat free" 为什么被单独排除而不许用 disclaimer 救？
- 跨域佐证：〔§ 101.13(c)〕营养标签内/外位置判定；〔§ 101.13(h)〕disclosure 与 disclaimer 的同一字号/紧邻规格；〔§ 101.62(b)(6)〕percent fat free 的逐词定义。
- 建议归属子卡：声称闸门

### CAND-FW-47: relative claims 参照食品「similar / dissimilar」选择闸门 + 四要素
- 条款出处：〔§ 101.13(j)(1)(2)(3)〕 + pdf-page 201–203
- 原文引用（英文逐字，≤100 词/段）：
> A food may bear a statement that compares the level of a nutrient in the food with the level of a nutrient in a reference food. These statements shall be known as “relative claims” and include “light,” “reduced,” “less” (or “fewer”), and “more” claims. (1) To bear a relative claim about the level of a nutrient, the amount of that nutrient in the food must be compared to an amount of nutrient in an appropriate reference food as specified below.
> (A) For “less” (or “fewer”) and “more” claims, the reference food may be a dissimilar food within a product category that can generally be substituted for one another in the diet (e.g., potato chips as reference for pretzels, orange juice as a reference for vitamin C tablets) or a similar food
> (B) For “light,” “reduced,” “added,” “extra,” “plus,” “fortified,” and “enriched” claims, the reference food shall be a similar food (e.g., potato chips as a reference for potato chips, one brand of multivitamin for another brand of multivitamin)
> (3) A relative claim for decreased levels of a nutrient may not be made on the label or in labeling of a food if the nutrient content of the reference food meets the requirement for a “low” claim for that nutrient (e.g., 3 g fat or less).
- 方法论陈述：先按描述符类型选参照食品："less/fewer/more" 可用同类可互换的 dissimilar food 或 similar food；"light/reduced/added/extra/plus/fortified/enriched" 只能用 similar food。再按 (j)(1)(ii) 定参照值来源："light" 须代表该类型食品的广基值（有效数据库、前三全国品牌均值、market basket norm、market leader），并须应请求向消费者与监管者提供依据；其他相对声称还可用本厂常规产品或其他厂长期在售产品，但数值须与营养标签内部一致且实际改变量 ≥ 声称定义所定百分比。作声称后须按 (j)(2) 标注四要素：参照食品身份、差异百分比/分数、紧邻最显著声称、定量对比信息。最后 (j)(3) 设反向禁止：参照食品本身已达该营养素 "low" 标准时，不得再作「减少」类相对声称。
- 可回答的新问题：用「薯片」作「椒盐卷饼」的 "less fat" 参照是否合法？"light" 用 market leader 作参照时须留哪些证据？参照食品已是 low fat，还能不能写 "reduced fat"？
- 跨域佐证：〔§ 101.13(d)〕substitute 食品定义（organoleptically/physically/functionally similar）；〔§ 101.13(h)(4)(i)(j)(2)(iii)〕字号与 most prominent 落位；〔§ 101.13(q)(3)(ii)(B)〕膳补 comparative percentage claims 的同类参照食品要求。
- 建议归属子卡：声称闸门

### CAND-FW-48: meal / main dish 定义 → disqualifying level 分档闸门
- 条款出处：〔§ 101.13(l)(m)〕〔§ 101.14(a)(4)(i)(ii)〕 + pdf-page 203–207
- 原文引用（英文逐字，≤100 词/段）：
> (l) For purposes of making a claim, a “meal product shall be defined as a food that: (1) Makes a major contribution to the total diet by: (i) Weighing at least 10 ounces (oz) per labeled serving; and (ii) Containing not less than three 40-g portions of food, or combinations of foods, from two or more of the following four food groups... (2) Is represented as, or is in a form commonly understood to be, a breakfast, lunch, dinner, or meal. Such representations may be made either by statements, photographs, or vignettes.
> (m) For purposes of making a claim, a “main dish product” shall be defined as a food that: (1) Makes a major contribution to a meal by (i) Weighing at least 6 oz per labeled serving; and (ii) Containing not less than 40 g of food, or combinations of foods, from each of at least two of the following four food groups
> (i) The levels for a meal product as defined in § 101.13(l) are 26.0 g of fat, 8.0 g of saturated fat, 120 mg of cholesterol, or 960 mg of sodium per label serving size, and (ii) The levels for a main dish product as defined in § 101.13(m) are 19.5 g of fat, 6.0 g of saturated fat, 90 mg of cholesterol, or 720 mg of sodium per label serving size.
- 方法论陈述：这是一条「先分类、后套阈值」的闸门：先用 (l)/(m) 的重量门槛（meal ≥10 oz/份、含 ≥3 个 40 g 份且来自 ≥2 个食物组；main dish ≥6 oz/份、每个 ≥2 食物组各 ≥40 g）+ 表征方式（statements/photographs/vignettes 表明是早/午/晚餐或主菜）把产品归入「普通食品 / meal / main dish」。类别一旦确定，disclosure 阈值 (§101.13(h)) 与 disqualifying level (§101.14(a)(4)) 都按类别取三套不同数值：普通 13/4/60/480，meal 26/8/120/960，main dish 19.5/6/90/720。分类错会连带把声称资格判反。
- 可回答的新问题：一份 9 oz 的冷冻餐按 meal 还是 main dish 判？用照片暗示「晚餐」但重量不足，能否仍算 meal？酱汁/调味料被 (l)(1)(ii)(E) 排除后，是否还能凑够食物组数？
- 跨域佐证：〔§ 101.13(h)(1)(2)(3)〕三类产品各自的 disclosure 阈值；〔§ 101.14(a)(4)〕disqualifying level 主阈值；〔§ 101.9(b)(3)〕meal/main dish 单份容器的 serving size 规则。
- 建议归属子卡：声称闸门

### CAND-FW-49: §101.13(q) 含量声称豁免清单与「品牌名 / 餐馆 / 百分比」特例
- 条款出处：〔§ 101.13(q)(1)(2)(3)(4)(5)(6)(7)(8)〕 + pdf-page 204–206
- 原文引用（英文逐字，≤100 词/段）：
> (q) The following exemptions apply: (1) Nutrient content claims that have not been defined by regulation and that are contained in the brand name of a specific food product that was the brand name in use on such food before October 25, 1989, may continue to be used as part of that brand name for such product, provided that they are not false or misleading under section 403(a) of the Federal Food, Drug, and Cosmetic Act (the act).
> (3)(i) A statement that describes the percentage of a vitamin or mineral in the food, including foods intended specifically for use by infants and children less than 2 years of age, in relation to a Reference Daily Intake (RDI) as defined in § 101.9 may be made on the label or in labeling of a food without a regulation authorizing such a claim for a specific vitamin or mineral unless such claim is expressly prohibited by regulation under section 403(r)(2)(A)(vi) of the act.
> (ii) In lieu of analytical testing, compliance may be determined using a reasonable basis for concluding that the food that bears the claim meets the definition for the claim. This reasonable basis may derive from recognized data bases for raw and processed foods, recipes, and other means to compute nutrient levels in the foods or meals
> (7) Implied nutrient content claims may be used as part of a brand name, provided that the use of the claim has been authorized by the Food and Drug Administration. Petitions requesting approval of such a claim may be submitted under § 101.69(o).
- 方法论陈述：(q) 是 §101.13 通则的封闭豁免口，按「豁免对象」切分：① 1989-10-25 前已在用、未被规章定义的品牌名声称可沿用（仍须不误导、且须守 403(f)(g)(h)）；② "diet" 软饮品牌名旧例（(q)(2)）；③ 维生素/矿物质相对 RDI 的百分比声明无须专门授权（除非被 403(r)(2)(A)(vi) 明文禁止），膳补中无 RDI/DRV 的膳食成分百分比声明按 (q)(3)(ii) 附「实际量并列 / 参照食品并列」条件；④ 婴儿配方与 medical foods 整节不适用（(q)(4)）；⑤ 餐馆食品免 (h) disclosure、可用 reasonable basis 代替检测（(q)(5)(i)(ii)）、术语/符号只要不表征营养素水平且附解释即不算声称（(q)(5)(iii) "lite fare" 例）；⑥ 1990-11-08 前有标准身份的通用名中的声称免 (b)/(h)（(q)(6)）；⑦ 品牌名中的 implied claim 须 FDA 授权、按 §101.69(o) 请愿（(q)(7)）。
- 可回答的新问题：新品牌想用 "Healthy Choice" 能否援引 (q)(1)？餐馆用 "lite fare" 加注「份量较小」为何不构成含量声称？(q)(3)(i) 的「无须授权」与 §101.14 健康声称「必须授权」是否冲突？
- 跨域佐证：〔§ 101.14(f)〕健康声称同样豁免婴儿配方与 medical foods；〔§ 101.69(o)〕请愿授权品牌名 implied claim 的程序；〔§ 101.9(j)(22)〕餐馆/即食场所的营养标签豁免（另一套对象）。
- 建议归属子卡：声称闸门

### CAND-FW-50: 健康声称「暗示同等受管」的定义闸门
- 条款出处：〔§ 101.14(a)(1)(5)〕〔§ 101.9(k)〕 + pdf-page 206–207
- 原文引用（英文逐字，≤100 词/段）：
> Health claim means any claim made on the label or in labeling of a food, including a dietary supplement, that expressly or by implication, including “third party” references, written statements (e.g., a brand name including a term such as “heart”), symbols (e.g., a heart symbol), or vignettes, characterizes the relationship of any substance to a disease or health-related condition. Implied health claims include those statements, symbols, vignettes, or other forms of communication that suggest, within the context in which they are presented, that a relationship exists between the presence or
> level of a substance in the food and a disease or health-related condition.
> (5) Disease or health-related condition means damage to an organ, part, structure, or system of the body such that it does not function properly (e.g., cardiovascular disease), or a state of health leading to such dysfunctioning (e.g., hypertension); except that diseases resulting from essential nutrient deficiencies (e.g., scurvy, pellagra) are not included in this definition (claims pertaining to such diseases are thereby not subject to § 101.14 or § 101.70).
- 方法论陈述：先把「什么算健康声称」扩到最大：express 或 by implication 均可，且明文列举 third party references、含 "heart" 的品牌名、心形符号、vignettes，只要在其呈现语境中暗示「物质存在/水平 ↔ 疾病或健康相关状况」的关系即构成。再给「疾病」下定义并开一个反向排除：必需营养素缺乏症（坏血病、糙皮病）不属本定义，因此相关声称不受 §101.14/§101.70 约束。判定时不看有没有直白说「预防」，而看整体沟通印象。
- 可回答的新问题：包装印一个心形符号但无文字，是否落入 health claim？引用第三方文献说「某成分有助心血管」算不算 third party reference？「防坏血病」为何不需要走健康声称授权？
- 跨域佐证：〔§ 101.9(k)(1)〕暗示疾病预防表述按 201(n)/403(a) 错标，合法出口只有 §101.14 + Subpart E；〔§ 101.13(b)(2)〕含量声称的 implied 定义同构但客体不同（营养素水平 vs 物质-疾病关系）；〔§ 101.14(e)〕未授权健康声称的禁止。
- 建议归属子卡：声称闸门

### CAND-FW-51: 「SSA 证据门槛 → FDA 立规章授权 → 企业依规章作声称」三层闸门 ★
- 条款出处：〔§ 101.14(c)〕〔§ 101.14(d)(1)(2)〕 + pdf-page 207–208
- 原文引用（英文逐字，≤100 词/段）：
> (c) Validity requirement. FDA will promulgate regulations authorizing a health claim only when it determines, based on the totality of publicly available scientific evidence (including evidence from well-designed studies conducted in a manner which is consistent with generally recognized scientific procedures and principles), that there is significant scientific agreement, among experts qualified by scientific training and experience to evaluate such claims, that the claim is supported by such evidence.
> (1) When FDA determines that a health claim meets the validity requirements of paragraph (c) of this section, FDA will propose a regulation in subpart E of this part to authorize the use of that claim. If the claim pertains to a substance not provided for in § 101.9 or § 101.36, FDA will propose amending that regulation to include declaration of the substance.
> (2) When FDA has adopted a regulation in subpart E of this part providing for a health claim, firms may make claims based on the regulation in subpart E of this part, provided that: (i) All label or labeling statements about the substance-disease relationship that is the subject of the claim are based on, and consistent with, the conclusions set forth in the regulations in subpart E of this part; (ii) The claim is limited to describing the value that ingestion (or reduced ingestion) of the substance, as part of
> a total dietary pattern, may have on a particular disease or health-related condition; (iii) The claim is complete, truthful, and not misleading.
- 方法论陈述：这是「声称三层闸门」的中枢，顺序不可颠倒。第一层（证据）：FDA 基于「全部公开可得科学证据的总体」判定合格科学专家间存在 significant scientific agreement (SSA) 支持该声称——不是「有论文支持」，而是法规级证据门槛。第二层（授权）：只有满足 (c)，FDA 才在 Subpart E 提议并采纳规章授权该声称；若涉及 §101.9/§101.36 未列的物质，还须同步修订营养标签规章。第三层（企业使用）：企业不能自创健康声称，只能在已授权规章的模型措辞与条件下作，且 (d)(2)(i)–(vii) 逐项约束——与 Subpart E 结论一致、限于「作为总膳食模式一部分」对特定疾病的价值、完整真实不误导、信息集中一处、公众可理解、物质水平足够低/足够高、必要时附 RACC 依据声明。扩张授权清单只有 §101.70 请愿一条路。
- 可回答的新问题：企业手上有 3 篇 RCT 能否自行上「降低某病风险」？Subpart E 已授权某声称，企业改写成更吸引人的同义句是否仍合规？(d)(1) 的「同步修订 §101.9」是不是把营养标签与声称闸门绑定的接口？
- 跨域佐证：〔§ 101.14(e)(1)(2)〕未落入 Subpart E 授权或未符合通则/专条即禁止；〔§ 101.70〕健康声称请愿程序；〔§ 101.14(d)(2)(iv)〕PDP 可用 "See ___ for information about the relationship between ___ and ___" 转介声明。
- 建议归属子卡：声称闸门

### CAND-FW-52: §101.14(e) 健康声称「六要件累积」禁止闸门 ★
- 条款出处：〔§ 101.14(e)(1)–(6)〕 + pdf-page 209
- 原文引用（英文逐字，≤100 词/段）：
> (e) Prohibited health claims. No expressed or implied health claim may be made on the label or in labeling for a food, regardless of whether the food is in conventional food form or dietary supplement form, unless: (1) The claim is specifically provided for in subpart E of this part; and (2) The claim conforms to all general provisions of this section as well as to all specific provisions in the appropriate section of subpart E of this part;
> (3) None of the disqualifying levels identified in paragraph (a)(4) of this section is exceeded in the food, unless specific alternative levels have been established for the substance in subpart E of this part; or unless FDA has permitted a claim despite the fact that a disqualifying level of a nutrient is present in the food based on a finding that such a claim will assist consumers in maintaining healthy dietary practices, and, in accordance with the regulation in subpart E of this part that makes such a finding, the
> label bears a disclosure statement that complies with § 101.13(h), highlighting the nutrient that exceeds the disqualifying level;
> (6) Except for dietary supplements or where provided for in other regulations in part 101, subpart E, the food contains 10 percent or more of the Reference Daily Intake or the Daily Reference Value for vitamin A, vitamin C, iron, calcium, protein, or fiber per reference amount customarily consumed prior to any nutrient addition.
- 方法论陈述：这是把三层闸门压成一张「全部满足才可作」的检查表，六要件是「与」关系，任一不满足即禁止：① 声称已由 Subpart E 明文授权；② 符合本节通则与该 Subpart E 专条全部规定；③ 未超 (a)(4) disqualifying level（除非 Subpart E 另定替代水平，或 FDA 特别认定该声称有助健康膳食并加 §101.13(h) disclosure 突显超标营养素）；④ 无 Subpart E 认定为不适当的物质水平；⑤ 非宣称供 <2 岁婴幼儿（除非 Subpart E 特别授权）；⑥ 食品在**任何营养强化之前**按 per RACC 含维生素A/C、铁、钙、蛋白或纤维 ≥10% RDI/DRV（膳补或 Subpart E 另定者除外）。第 ⑥ 项最易漏：它先设「营养充足」正面门槛，再叠加 ③ 的负面门槛。
- 可回答的新问题：产品靠「后添加钙」凑到 10% DV，能否满足 (e)(6)？Subpart E 已授权、但钠超 480 mg，靠加 disclosure 能否救回？(e)(3) 的「FDA permitted」与 (e)(1) 的「Subpart E 授权」是同一道程序吗？
- 跨域佐证：〔§ 101.14(a)(4)〕disqualifying level 数值；〔§ 101.13(h)〕disclosure 语句与字号；〔§ 101.14(f)〕婴儿配方与 medical foods 整节不适用；〔§ 101.14(d)(3)〕作健康声称须提供营养标签。
- 建议归属子卡：声称闸门

### CAND-FW-53: disqualifying nutrient level「先过负面门槛」+ meal/main dish 分档
- 条款出处：〔§ 101.14(a)(4)〕〔§ 101.14(e)(3)〕 + pdf-page 206–207
- 原文引用（英文逐字，≤100 词/段）：
> (4) Disqualifying nutrient levels means the levels of total fat, saturated fat, cholesterol, or sodium in a food above which the food will be disqualified from making a health claim. These levels are 13.0 grams (g) of fat, 4.0 g of saturated fat, 60 milligrams (mg) of cholesterol, or 480 mg of sodium, per reference amount customarily consumed, per label serving size, and, only for foods with reference amounts customarily consumed of 30 g or less or 2 tablespoons or less, per 50 g.
> Any one of the levels, on a per reference amount customarily consumed, a per label serving size or, when applicable, a per 50 g basis, will disqualify a food from making a health claim unless an exception is provided in subpart E of this part, except that: (i) The levels for a meal product as defined in § 101.13(l) are 26.0 g of fat, 8.0 g of saturated fat, 120 mg of cholesterol, or 960 mg of sodium per label serving size
- 方法论陈述：把「能否作健康声称」设计成先过一道纯负面门槛：只要总脂/饱和脂/胆固醇/钠任一项在 per RACC、per labeled serving 或（小 RACC 食品）per 50 g 口径下超过 13 g / 4 g / 60 mg / 480 mg，食品即**丧失**作任何健康声称的资格——即便已满足 SSA 与 Subpart E 授权。脱水食品按 as prepared 判。meal/main dish 按 FW-48 的分类换用 26/8/120/960 与 19.5/6/90/720。唯一出口有二：Subpart E 为该物质定了替代水平；或 FDA 作出「该声称有助消费者维持健康膳食」的认定，并在标签加 §101.13(h) disclosure 突显超标营养素。
- 可回答的新问题：产品钠 479 mg 与 481 mg 的合规结论为何完全不同？同一产品按 per RACC 合格但 per labeled serving 超标，以哪个为准？做了 5-log 果汁工艺能否影响 disqualifying level 判定？
- 跨域佐证：〔§ 101.14(e)(3)〕超阈值时的两条例外；〔§ 101.13(h)(1)〕同一组 13/4/60/480 数值触发 disclosure（而非禁声称）；〔§ 101.12(g)〕RACC/serving size 是阈值的分母。
- 建议归属子卡：声称闸门

### CAND-FW-54: 健康声称「物质适格性」按摄入水平两分支
- 条款出处：〔§ 101.14(b)(1)(2)(3)〕 + pdf-page 207
- 原文引用（英文逐字，≤100 词/段）：
> (b) Eligibility. For a substance to be eligible for a health claim: (1) The substance must be associated with a disease or health-related condition for which the general U.S. population, or an identified U.S. population subgroup (e.g., the elderly) is at risk, or, alternatively, the petition submitted by the proponent of the claim otherwise explains the prevalence of the disease or health-related condition in the U.S. population and the relevance of the claim in the context of the total daily diet and satisfies the other requirements of this section.
> (2) If the substance is to be consumed as a component of a conventional food at decreased dietary levels, the substance must be a nutrient listed in 21 U.S.C. 343(q)(1)(C) or (q)(1)(D), or one that the Food and Drug Administration (FDA) has required to be included in the label or labeling under 21 U.S.C. 343(q)(2)(A); or
> (3) If the substance is to be consumed at other than decreased dietary levels: (i) The substance must, regardless of whether the food is a conventional food or a dietary supplement, contribute taste, aroma, or nutritive value, or any other technical effect listed in § 170.3(o) of this chapter, to the food and must retain that attribute when consumed at levels that are necessary to justify a claim; and (ii) The substance must be a food or a food ingredient or a component of a food ingredient whose use at
> the levels necessary to justify a claim has been demonstrated by the proponent of the claim, to FDA's satisfaction, to be safe and lawful
- 方法论陈述：在 SSA 之前先判「物质本身有没有资格进健康声称体系」。第一问是疾病关联：该物质所关联的疾病/健康状况须使美国一般人群或可识别亚群（如老年人）处于风险中，或请愿方在请愿中说明患病率与在总日膳食中的相关性。第二问按摄入方向分岔：若声称是「减少摄入该物质」（decreased dietary levels）→ 该物质必须是 21 U.S.C. 343(q)(1)(C)/(D) 所列营养素或 FDA 依 343(q)(2)(A) 要求标示者；若是「非减少摄入」（即增加/维持摄入）→ 该物质须在常规食品或膳补中贡献味道、香气、营养价值或 §170.3(o) 技术效果且在声称所需摄入水平上仍保该属性，并由请愿方向 FDA 证明该水平下安全合法。
- 可回答的新问题：一个草本成分想作「降低某病风险」声称，为何还要先证明它在食品里有技术效果？「减少摄入钠」与「增加摄入钙」走的是不是同一套适格条件？请愿里说明患病率能否替代「人群处于风险」的证明？
- 跨域佐证：〔§ 101.14(c)〕SSA 是适格之后的证据门槛；〔§ 101.70〕请愿须含物质适格性材料；〔§ 101.14(d)(2)(vi)(vii)〕"low/high" 水平要求按同一摄入方向分岔。
- 建议归属子卡：声称闸门

### CAND-FW-55: 「减少摄入 → 须够 low / 非减少摄入 → 须够 high」水平双向分流
- 条款出处：〔§ 101.14(d)(2)(vi)(vii)〕 + pdf-page 208–209
- 原文引用（英文逐字，≤100 词/段）：
> (vi) If the claim is about the effects of consuming the substance at decreased dietary levels, the level of the substance in the food is sufficiently low to justify the claim. To meet this requirement, if a definition for use of the term low has been established for that substance under this part, the substance must be present at a level that meets the requirements for use of that term, unless a specific alternative level has been established for the substance in subpart E of this part. If no definition
> for “low” has been established, the level of the substance must meet the level established in the regulation authorizing the claim; or
> (vii) If the claim is about the effects of consuming the substance at other than decreased dietary levels, the level of the substance is sufficiently high and in an appropriate form to justify the claim. To meet this requirement, if a definition for use of the term high for that substance has been established under this part, the substance must be present at a level that meets the requirements for use of that term
- 方法论陈述：作已授权健康声称时，按声称主张的摄入方向二选一地校核物质水平：① 声称「减少摄入该物质有价值」→ 物质水平须足够低：若本 part 已定义 "low"（如 §101.62 等），须满足该定义；Subpart E 另定替代水平则从其规定；若无 "low" 定义，须达到授权规章所定水平。② 声称「非减少摄入」（增加/维持）→ 水平须足够高且形态适当：有 "high" 定义则满足之，无定义（全食物或作配料）则须按授权规章写明达到声称效果所需的每日膳食摄入量。两分支都接到 (d)(2)(vii)(A)：若按 RACC 达标但 labeled serving 与 RACC 不同，须附「声称基于 RACC」的说明（如 "A serving of __ ounces of this product conforms to such a diet."）；餐馆食品 (B) 可用 reasonable basis 代替。
- 可回答的新问题：「低钠降低高血压风险」声称里，产品钠水平按 §101.61 的 "low sodium" 定义还是授权规章另定？声称基于全食物（如燕麦）而无 "high" 定义时，标签要不要写每日摄入克数？(d)(2)(vii)(A) 与 §101.12(g) 的依据声明是否重复？
- 跨域佐证：〔§ 101.12(g)〕serving size≠RACC 时的依据声明；〔§ 101.9(b)(12)(ii)〕双列产品作声称的依据声明；〔§ 101.13(q)(5)(ii)〕餐馆声称的 reasonable basis。
- 建议归属子卡：声称闸门

### CAND-FW-56: 「作声称 → 必须提供营养标签」的跨体系触发闸门
- 条款出处：〔§ 101.13(n)〕〔§ 101.14(d)(3)〕〔§ 101.10〕 + pdf-page 204 / 209 / 68
- 原文引用（英文逐字，≤100 词/段）：
> (n) Nutrition labeling in accordance with § 101.9, § 101.10, or § 101.36, as applicable, shall be provided for any food for which a nutrient content claim is made.
> (3) Nutrition labeling shall be provided in the label or labeling of any food for which a health claim is made in accordance with § 101.9; for restaurant foods, in accordance with § 101.10; or for dietary supplements, in accordance with § 101.36.
> Nutrition labeling in accordance with § 101.9 shall be provided upon request for any restaurant food or meal for which a nutrient content claim (as defined in § 101.13 or in subpart D of this part) or a health claim (as defined in § 101.14 and permitted by a regulation in subpart E of this part) is made
- 方法论陈述：把「声称」设为营养标签义务的触发器，并按食品形态分流到三套标签规章：普通包装食品 → §101.9；餐馆食品 → §101.10（应请求提供，可用「声称基础营养素量」作功能等价物）；膳食补充剂 → §101.36。§101.13(n) 管含量声称、§101.14(d)(3) 管健康声称、§101.10 管餐馆，三条措辞同构。它与 FW-22（声称击穿豁免）、FW-29（声称把自愿营养素转强制）共同构成「声称是义务放大器」这一反复出现的思维模型：只要开口说营养素/健康，就同时拉起营养标签、自愿项申报、披露声明与举证义务。
- 可回答的新问题：一个本可依 §101.9(j) 豁免的小包装食品作了 "low fat"，要补哪几样东西？餐馆只给「本餐 <10 g 脂肪」是否同时满足 §101.10 与 §101.13(n)？膳补作健康声称时，§101.36 与 §101.9 的营养标签能否择一？
- 跨域佐证：〔§ 101.9(j)(13)(i)(B)〕小包装一旦作声称即须按 6 pt 标全营养信息；〔§ 101.11(b)(2)(ii)(B)〕菜单书面信息本可免但作声称仍须给该营养素；〔§ 101.9(k)〕暗示疾病表述另受 §101.14/Subpart E 约束。
- 建议归属子卡：声称闸门

### CAND-FW-57: 显著性不足的六种归因 + 「空间不足豁免」的因果反排除
- 条款出处：〔§ 101.15(a)(1)–(6)〕〔§ 101.15(b)(1)–(3)〕 + pdf-page 210
- 原文引用（英文逐字，≤100 词/段）：
> A word, statement, or other information required by or under authority of the act to appear on the label may lack that prominence and conspicuousness required by section 403(f) of the act by reason (among other reasons) of: (1) The failure of such word, statement, or information to appear on the part or panel of the label which is presented or displayed under customary conditions of purchase;
> (4) Insufficiency of label space (for the prominent placing of such word, statement, or information) resulting from the use of label space for any word, statement, design, or device which is not required by or under authority of the act to appear on the label; (5) Insufficiency of label space (for the prominent placing of such word, statement, or information) resulting from the use of label space to give materially greater conspicuousness to any other word, statement, or information, or to any design or device; or (6) Smallness or style
> of type in which such word, statement, or information appears, insufficient background contrast, obscuring designs or vignettes, or crowding with other written, printed, or graphic matter.
> (b) No exemption depending on insufficiency of label space, as prescribed in regulations promulgated under section 403 (e) or (i) of the act, shall apply if such insufficiency is caused by: (1) The use of label space for any word, statement, design, or device which is not required by or under authority of the act to appear on the label; (2) The use of label space to give greater conspicuousness to any word, statement, or other information than is required by section 403(f) of the act; or (3) The use of label space for any representation in a foreign language.
- 方法论陈述：先给出「强制信息不够醒目」的六类可开观察项归因：没放在 customary purchase 条件下会展示的面、没在多个同样可能展示的面重复、标签未覆盖可用面积、把空间给了非强制内容、把空间用来过度突出别的内容、字号/对比度/装饰遮挡/拥挤。然后一条关键的因果反排除：凡依赖「空间不足」的豁免（403(e)/(i) 下的规章豁免），若空间不足正是由上述 (b)(1) 非强制内容、(b)(2) 过度显著、(b)(3) 外语表述造成的，则**不得**主张豁免。判定顺序是「先问空间为何不足 → 若因厂商自找的装饰/外语/夸大 → 豁免关门」，防止用排版设计制造豁免。
- 可回答的新问题：厂商把正面留给大幅图案、把营养信息挤到 6 pt，能否援引小包装豁免？双语标签导致空间不足，是否反而堵死豁免？(a)(2)「两个以上可能展示的面各须重复」与 §101.2(d)(1)「同一面板」如何协调？
- 跨域佐证：〔§ 101.2(d)(1)〕判断空间是否足够时不计入 vignettes/designs/非强制信息（同一因果逻辑）；〔§ 101.9(j)(17)〕>40 sq in 但 PDP/信息面板不足时可改用其他面板，且明确「vignettes 可计入 PDP 空间判断、信息面板的非强制信息不计入」；〔§ 101.7(h)(1)(2)〕显著性字形规格。
- 建议归属子卡：基础架构

### CAND-FW-58: 「出现外语 → 全部强制信息须以该语言再现」触发闸门
- 条款出处：〔§ 101.15(c)(1)(2)(3)〕 + pdf-page 210–211
- 原文引用（英文逐字，≤100 词/段）：
> (1) All words, statements, and other information required by or under authority of the act to appear on the label or labeling shall appear thereon in the English language: Provided, however, That in the case of articles distributed solely in the Commonwealth of Puerto Rico or in a Territory where the predominant language is one other than English, the predominant language may be substituted for English.
> (2) If the label contains any representation in a foreign language, all words, statements, and other information required by or under authority of the act to appear on the label shall appear thereon in the foreign language: Provided, however, That individual serving-size packages of foods containing no more than 11⁄2 avoirdupois ounces or no more than 11⁄2 fluid ounces served with meals in restaurants, institutions, and passenger carriers and not intended for sale at retail are exempt from the requirements of this paragraph (c)(2), if the only representation in the foreign language(s) is the name of the food.
> (3) If any article of labeling (other than a label) contains any representation in a foreign language, all words, statements, and other information required by or under authority of the act to appear on the label or labeling shall appear on such article of labeling.
- 方法论陈述：默认英语；一旦 label 出现任何外语表述，全部强制信息须以该外语再现；若 labeling（非 label，如随附单张/广告）出现外语，则该件 labeling 上须含全部强制信息。例外有三：仅在波多黎各或非英语主导地区销售可用当地主要语言替代英语；≤1½ oz 的餐厅/机构/客运单份小包装若外语只有品名可免 (c)(2)。这与 FW-57 的 (b)(3) 形成闭环：外语不仅触发全量再现，还会堵死「空间不足」豁免。
- 可回答的新问题：只把品牌名译成西语、其余仍英语，是否触发 (c)(2) 全量再现？(c)(3) 对「随附宣传单」的要求是否等于要在广告里印完整 Nutrition Facts？§101.9(d)(14) 的双语 Nutrition Facts 与本款如何叠加？
- 跨域佐证：〔§ 101.9(d)(14)〕营养标签第二语言的两种呈现方式；〔§ 101.15(b)(3)〕外语占用空间不得作为豁免理由；〔§ 101.2(c)(2)〕餐厅单份小包装的 type-size 豁免（同一对象）。
- 建议归属子卡：基础架构

### CAND-FW-59: 强制警示「按风险场景逐款立法，条件与豁免互不借用」
- 条款出处：〔§ 101.17(a)(b)(d)(e)(f)(g)(h)〕 + pdf-page 211–215
- 原文引用（英文逐字，≤100 词/段）：
> (1) In addition to the warning required by paragraph (a) of this section, the label of a food packaged in a self-pressurized container in which the propellant consists in whole or in part of a halocarbon or a hydrocarbon shall bear the following warning: WARNING—Use only as directed. Intentional misuse by deliberately concentrating and inhaling the contents can be harmful or fatal. (2) The warning required by paragraph (b)(1) of this section is not required for the following products: (i) Products expelled in the form of a foam or cream, which contain less than 10 percent propellant in the container.
> (1) The label and labeling of any food product in liquid, powdered, tablet, capsule, or similar forms that derives more than 50 percent of its total caloric value from either whole protein, protein hydrolysates, amino acid mixtures, or a combination of these, and that is represented for use in reducing weight shall bear the following warning: WARNING: Very low calorie protein diets (below 400 Calories per day) may cause serious illness or death. Do Not Use for Weight Reduction in Such Diets Without Medical Supervision. Not for use by infants, children, or pregnant or nursing women.
> (3) The label and labeling of food products represented or intended for dietery (food) supplementation that derive more than 50 percent of their total caloric value from either whole protein, protein hydrolysates, amino acid mixtures, or a combination of these, that are represented specifically for purposes other than weight reduction; and that are not covered by the requirements of paragraph (d) (1) and (2) of this section; shall bear the following statement: NOTICE: Use this product as a food supplement only. Do not use for weight reduction.
> (1) Foods containing dry or incompletely hydrated psyllium husk, also known as psyllium seed husk, and bearing a health claim on the association between soluble fiber from psyllium husk and reduced risk of coronary heart disease, shall bear a label statement informing consumers that the appropriate use of such foods requires consumption with adequate amounts of fluids
- 方法论陈述：§101.17 不是一条统一警示规则，而是按风险场景逐款立法：自加压容器 (a) 与卤烃/烃推进剂 (b) 叠加、极低热量蛋白膳食 (d)、铁含剂 (e)、psyllium husk 配健康声称 (f)、未巴氏果汁 (g)、壳蛋 (h)，各有独立 (1)–(n) 触发条件、独立措辞与独立豁免。以 (d) 为例，先按「>50% 热量来自蛋白 + 表征用途」分三支：用于减重 → 死伤警示；属于营养均衡膳食计划（≥400 Cal/日并写明计划）→ 改用 Notice 且免死伤警示；作膳食补充且非减重 → "Use this product as a food supplement only"。判定纪律是：不能把 (b) 的 <10% 推进剂豁免借到 (a)，也不能把 (g) 的 5-log 工艺豁免借到 (h) 的沙门氏菌处理。
- 可回答的新问题：一款蛋白粉既作减重又作补剂，按 (d)(1) 还是 (d)(3)？(f) 的 psyllium 警示为何绑定「作了某健康声称」这一前提？(a) 与 (b) 两条警示能否合并成一句？
- 跨域佐证：〔§ 101.17(g)(7)〕5-log 工艺豁免（仅适用于 (g)）；〔§ 101.17(h)(4)〕灭活沙门氏菌豁免（仅适用于 (h)）；〔§ 101.100(a)(4)〕亚硫酸盐 10 ppm 阈值是另一套独立判据；〔§ 101.14(d)(2)〕健康声称一般要求（(f) 的接口）。
- 建议归属子卡：特定品类与警示

### CAND-FW-60: 未巴氏果汁警示 ↔ 5-log 工艺豁免 ↔ Part 120 三层接口 ★
- 条款出处：〔§ 101.17(g)(2)(3)(7)〕 + pdf-page 213–214（BOOK_OVERVIEW 点名的 Part 120 接口）
- 原文引用（英文逐字，≤100 词/段）：
> (2) The label of: (i) Any juice that has not been processed in the manner described in paragraph (g)(7) of this section; or (ii) Any beverage containing juice where neither the juice ingredient nor the beverage has been processed in the manner described in paragraph (g)(7) of this section, shall bear the following warning statement: WARNING: This product has not been pasteurized and, therefore, may contain harmful bacteria that can cause serious illness in children, the elderly, and persons with weakened immune systems.
> (3) The warning statement required by this paragraph (g) shall not apply to juice that is not for distribution to retail consumers in the form shipped and that is for use solely in the manufacture of other foods or that is to be processed, labeled, or repacked at a site other than originally processed, provided that for juice that has not been processed in the manner described in paragraph (g)(7) of this section, the lack of such processing is disclosed in documents accompanying the juice, in accordance with the practice of the trade.
> (7)(i) The requirements in this paragraph (g) shall not apply to a juice that has been processed in a manner that will produce, at a minimum, a reduction in the pertinent microorganism for a period at least as long as the shelf life of the product when stored under normal and moderate abuse conditions, of the following magnitude: (A) A 5-log (i.e., 100,000-fold) reduction; or (B) A reduction that is equal to, or greater than, the criterion established for process controls by any final regulation requiring the application of Hazard
> Analysis and Critical Control Point (HACCP) principles to the processing of juice. (ii) For the purposes of this paragraph (g), the “pertinent microorganism” is the most resistant microorganism of public health significance that is likely to occur in the juice.
- 方法论陈述：默认闸门是「未经 (g)(7) 工艺处理的果汁/含汁饮料 → 必须带未巴氏警示」；两条出口：① 非零售、仅供再加工/异地贴标的散装果汁可免警示，但**必须在随附单据中披露未处理**；② 经工艺处理、在货架期（含正常与适度滥用条件）内对「pertinent microorganism」（最耐受且具公共卫生意义的微生物）达到 ≥5-log（100,000 倍）下降，或达到任何果汁 HACCP 最终规章所定工艺控制标准，则整体不适用 (g)。这与 21 CFR Part 120〔§ 120.24〕的 5-log 法定工艺义务、CP 7303.847 检查取证构成「工艺义务 → 标签义务 → 检查取证」三层。**红线：警示声明不替代 5-log 工艺义务；做了 5-log 也不自动免除 §101.9 营养标签、§101.30 果汁百分比声明等所有其他标签义务。**
- 可回答的新问题：果汁做了 4.9-log 只能挂警示，还是可申请 FDA 个案认定？含 10% 果汁的饮料，其果汁配料做了 5-log 但饮料未做，是否仍须挂警示？出口转内销的散装浓缩汁在随货单据披露未处理后，进口商灌装零售时警示义务落在谁身上？
- 跨域佐证：〔§ 101.30〕同一果汁产品的百分比声明义务（另一条独立标签义务）；〔§ 101.9(j)(10)〕生鲜果蔬鱼的自愿营养标签豁免（不同对象）；〔§ 101.17(h)(4)〕壳蛋经灭沙门氏菌处理即免安全操作声明——同构的「工艺换标签豁免」但条款独立，不可借用；〔21 CFR 120.24〕5-log 工艺要求（转引未收）。
- 建议归属子卡：特定品类与警示

### CAND-FW-61: 壳蛋安全操作声明 + 「relabel / divert / destroy」行政执行程序
- 条款出处：〔§ 101.17(h)(1)(4)(6)(7)(9)〕 + pdf-page 214–218
- 原文引用（英文逐字，≤100 词/段）：
> (1) The label of all shell eggs, whether in intrastate or interstate commerce, shall bear the following statement: SAFE HANDLING INSTRUCTIONS: To prevent illness from bacteria: keep eggs refrigerated, cook eggs until yolks are firm, and cook foods containing eggs thoroughly.
> (4) Shell eggs that have been, before distribution to consumers, specifically processed to destroy all viable Salmonella shall be exempt from the requirements of paragraph (h) of this section.
> (6) Under sections 311 and 361 of the Public Health Service Act (PHS Act), any State or locality that is willing and able to assist the agency in the enforcement of paragraphs (h)(1) through (h)(5) of this section, and is authorized to inspect or regulate establishments handling packed shell eggs, may in its own jurisdiction, enforce paragraphs (h)(1) through (h)(5) of this section through inspections under paragraph (h)(8) of this section
> (9) No State or local governing entity shall establish or continue in effect any law, rule, regulation, or other requirement requiring safe handling instructions on unpasteurized shell eggs that are less stringent than those required in paragraphs (h)(1) through (h)(5) of this section.
- 方法论陈述：义务层是「所有壳蛋（含州内流通）须带 SAFE HANDLING INSTRUCTIONS」，例外是分销前经专门处理杀灭全部活沙门氏菌 (h)(4)，以及非直接售消费者者可把声明放在纸箱或发票/提单等 labeling 上 (h)(5)。执行层则是一条独立于 FD&C Act 的 PHS Act 行政链：FDA 或经授权州/地方发现违规 → 书面命令 relabel / divert（按 EPIA 加工）/ destroy → 命令须含 (h)(7)(i)(B) 的 11 项要素并经主任批准 → 当事人可 5 个工作日内书面申诉或请求 informal hearing → 主持官员作书面报告与建议决定 → 维持则 10 个工作日内执行，决定为最终行政行为可诉诸法院 (h)(7)(ii)(E)(F)。(h)(6) 授权州/地方协助执法，(h)(9) 又禁止州/地方设更宽松要求（联邦下限 + 州可更严）。
- 可回答的新问题：州法要求比联邦更宽松的安全操作声明，是否被 (h)(9) 排除？行政 detain 命令与 §101.18 misbranding 没收是两条并行执法钩子吗？"(h)(7)" 的 informal hearing 是否给企业提供了一个「先扣留后申辩」的程序位？
- 跨域佐证：〔§ 101.17(a)(e)〕其他警示语句的落位规格（PDP/信息面板、hairline box）；〔§ 101.18〕misbranding 总纲（FD&C Act 钩子）；〔§ 101.15(a)〕显著性归因（安全操作声明须 prominent and conspicuous）。
- 建议归属子卡：特定品类与警示

### CAND-FW-62: misbranding 三类归因 + 地理来源暗示的四例外
- 条款出处：〔§ 101.18(a)(b)(c)(1)–(4)〕 + pdf-page 219
- 原文引用（英文逐字，≤100 词/段）：
> (a) Among representations in the labeling of a food which render such food misbranded is a false or misleading representation with respect to another food or a drug, device, or cosmetic. (b) The labeling of a food which contains two or more ingredients may be misleading by reason (among other reasons) of the designation of such food in such labeling by a name which includes or suggests the name of one or more but not all such ingredients, even though the names of all such ingredients are stated elsewhere in the labeling.
> (c) Among representations in the labeling of a food which render such food misbranded is any representation that expresses or implies a geographical origin of the food or any ingredient of the food except when such representation is either: (1) A truthful representation of geographical origin. (2) A trademark or trade name provided that as applied to the article in question its use is not deceptively misdescriptive.
> (3) A part of the name required by applicable Federal law or regulation. (4) A name whose market significance is generally understood by the consumer to connote a particular class, kind, type, or style of food rather than to indicate geographical origin.
- 方法论陈述：§101.18 是 Subpart A 的 misbranding 总纲，给出三类可致错标的归因：对他种食品/药品/器械/化妆品作虚假或误导表述；多配料食品的品名只提部分配料（即便配料表在别处已全列，仍可能误导）；表达或暗示地理来源。第三类又开四条例外做「合法/非法地理表述」分流：真实地理来源；商标/商号且非欺骗性误描述（(c)(2)(i) 长期使用已被消费者理解为特定厂商、(ii) 任意/幻想词不致联想地理）；联邦法律或规章要求的品名组成部分；消费者普遍理解为某一类别/类型/风格而非地理来源的名称。判定重点是「整体印象是否误导」而非逐字真假。
- 可回答的新问题：品名写「草莓酸奶」但配料表显示只有香精，是否落入 (b)？"Swiss" 用于巧克力算 (c)(4) 的类别名还是地理暗示？(c)(2)(i) 的「长期排他使用」由谁举证？
- 跨域佐证：〔§ 101.3(b)(e)〕品名递补与 imitation 判定；〔§ 101.22(i)〕characterizing flavor 的品名伴随词（同为品名误导的专门规则）；〔§ 101.9(k)〕暗示疾病预防表述按 201(n)/403(a) 错标；〔§ 101.13(c)〕位置决定信息是否构成声称。
- 建议归属子卡：基础架构

### CAND-FW-63: 香料/调味/色素/防腐剂「默认具名 + 列举可统称」判定链
- 条款出处：〔§ 101.22(h)(j)(k)〕〔§ 101.4(b)(1)〕 + pdf-page 220–223
- 原文引用（英文逐字，≤100 词/段）：
> (h) The label of a food to which flavor is added shall declare the flavor in the statement of ingredients in the following way: (1) Spice, natural flavor, and artificial flavor may be declared as “spice”, “natural flavor”, or “artificial flavor”, or any combination thereof, as the case may be.
> (j) A food to which a chemical preservative(s) is added shall, except when exempt pursuant to § 101.100 bear a label declaration stating both the common or usual name of the ingredient(s) and a separate description of its function, e.g., “preservative”, “to retard spoilage”, “a mold inhibitor”, “to help protect flavor” or “to promote color retention”.
> (1) A color additive or the lake of a color additive subject to certification under 721(c) of the act shall be declared by the name of the color additive listed in the applicable regulation in part 74 or part 82 of this chapter, except that it is not necessary to include the “FD&C” prefix or the term “No.” in the declaration
> (2) Color additives not subject to certification and not otherwise required by applicable regulations in part 73 of this chapter to be declared by their respective common or usual names may be declared as “Artificial Color,” “Artificial Color Added,” or “Color Added” (or by an equally informative term that makes clear that a color additive has been used in the food).
> (7) Because protein hydrolysates function in foods as both flavorings and flavor enhancers, no protein hydrolysate used in food for its effects on flavor may be declared simply as “flavor,” “natural flavor,” or “flavoring.” The ingredient shall be declared by its specific common or usual name as provided in § 102.22 of this chapter.
- 方法论陈述：承接 FW-08 的「具体名默认」，§101.22 是 §101.4(b)(1) 转介后的专门规则：香料/天然香料/人造香料可用统称 "spice"/"natural flavor"/"artificial flavor"；化学防腐剂须同时写通用名 + 功能描述（且先扣 §101.100 豁免）；色素按是否需 certification 分两支——需认证的按 part 74/82 名称逐一具名（可省 FD&C 前缀与 No.，lake 须带 "Lake"），免认证且 part 73 未要求具名者可用 "Artificial Color/Color Added" 或 "Colored with ____"；(k)(3) 对黄油/奶酪/冰淇淋的色素又给免申报。反向封死：蛋白水解物不得笼统写 "flavor"，须按 §102.22 具名；洋葱粉/蒜粉等被 (h)(3) 认定消费者理解为食品，须具名；盐、MSG 须具名 (h)(4)(5)。这是「统称许可清单 + 逐项具名反例」的分流闸门。
- 可回答的新问题：把 MSG 写成 "natural flavor" 为什么不行？一款用免认证色素的饮料写 "Color Added" 是否还需列具体色素名？(h)(2) 的 incidental additive 免申报要回到 §101.100(a)(3) 的什么前提？
- 跨域佐证：〔§ 101.4(b)(1)(14)〕配料具体名默认与油脂具名；〔§ 101.100(a)(3)〕incidental additive 免申报（无技术或功能效果前提）；〔§ 101.22(a)(1)–(5)〕artificial flavor / spice / natural flavor / chemical preservative 的定义（术语边界，非框架）。
- 建议归属子卡：特定品类与警示

### CAND-FW-64: characterizing flavor「有无人工香料」两分支的品名标注链
- 条款出处：〔§ 101.22(i)(1)(2)(3)(4)〕 + pdf-page 221–223
- 原文引用（英文逐字，≤100 词/段）：
> (i) If the label, labeling, or advertising of a food makes any direct or indirect representations with respect to the primary recognizable flavor(s), by word, vignette, e.g., depiction of a fruit, or other means, or if for any other reason the manufacturer or distributor of a food wishes to designate the type of flavor in the food other than through the statement of ingredients, such flavor shall be considered the characterizing flavor and shall be declared in the following way:
> (1) If the food contains no artificial flavor which simulates, resembles or reinforces the characterizing flavor, the name of the food on the principal display panel or panels of the label shall be accompanied by the common or usual name of the characterizing flavor, e.g., “vanilla”, in letters not less than one-half the height of the letters used in the name of the food, except that:
> (2) If the food contains any artificial flavor which simulates, resembles or reinforces the characterizing flavor, the name of the food on the principal display panel or panels of the label shall be accompanied by the common or usual name(s) of the characterizing flavor, in letters not less than one-half the height of the letters used in the name of the food and the name of the characterizing flavor shall be accompanied by the word(s) “artificial” or “artificially flavored”
> (i) If the food is one that is commonly expected to contain a characterizing food ingredient, e.g., strawberries in “strawberry shortcake”, and the food contains natural flavor derived from such ingredient and an amount of characterizing ingredient insufficient to independently characterize the food, or the food contains no such ingredient, the name of the characterizing flavor may be immediately preceded by the word “natural” and shall be immediately followed by the word “flavored”
- 方法论陈述：先判「是否存在 characterizing flavor」——只要 label/labeling/advertising 以文字、vignette（水果图案）或其他方式直接或间接表征可识别主风味，或厂商想在配料表之外指明风味类型，即触发。再按「是否含模拟/强化该风味的人工香料」二分：无 → 品名旁加该风味通用名（字号 ≥ 品名字高 1/2）；有 → 品名旁加风味名且必须伴随 "artificial"/"artificially flavored"（字号同样 ≥1/2）。第一支里再嵌 (i)(1)(i) 子分岔：消费者通常预期含该配料但含量不足以独立表征（或根本不含）→ 用 "natural ... flavored" / "... flavored"；(i)(1)(ii) 天然香料并非来自被模拟产品 → 须标来源或 "artificially flavored"；(i)(1)(iii) 混合 → 加 "with other natural flavor"。(i)(3) 规定伴随词须紧邻、无插入材料，(i)(4) 要求供应商书面认证「不含人工香料」并留存 3 年。
- 可回答的新问题：包装印了草莓图案但品名没写「草莓」，是否触发 (i)？用天然香精但不含草莓的 "strawberry shortcake" 为何要写 "strawberry flavored"？三种以上可辨风味为何可用 "artificially flavored fruit punch" 概括？
- 跨域佐证：〔§ 101.18(b)〕品名只提部分配料可致 misbranding；〔§ 101.3(c)〕可选形态可见或 vignette 时可省；〔§ 101.30(a)〕果汁饮料以 vignette 表征即触发百分比声明——同构的「图形触发」逻辑。
- 建议归属子卡：特定品类与警示

### CAND-FW-65: §101.22 的 403(k) 豁免三场景 + B2B 香料标注分流
- 条款出处：〔§ 101.22(d)(e)(f)(g)〕 + pdf-page 220–221
- 原文引用（英文逐字，≤100 词/段）：
> (d) A food shall be exempt from compliance with the requirements of section 403(k) of the act if it is not in package form and the units thereof are so small that a statement of artificial flavoring, artificial coloring, or chemical preservative, as the case may be, cannot be placed on such units with such conspicuousness as to render it likely to be read by the ordinary individual under customary conditions of purchase and use.
> (e) A food shall be exempt while held for sale from the requirements of section 403(k) of the act (requiring label statement of any artificial flavoring, artificial coloring, or chemical preservatives) if said food, having been received in bulk containers at a retail establishment, is displayed to the purchaser with either (1) the labeling of the bulk container plainly in view or (2) a counter card, sign, or other appropriate device bearing prominently and conspicuously the information required to be stated on the label pursuant to section 403(k).
> (f) A fruit or vegetable shall be exempt from compliance with the requirements of section 403(k) of the act with respect to a chemical preservative applied to the fruit or vegetable as a pesticide chemical prior to harvest.
> (g) A flavor shall be labeled in the following way when shipped to a food manufacturer or processor (but not a consumer) for use in the manufacture of a fabricated food, unless it is a flavor for which a standard of identity has been promulgated, in which case it shall be labeled as provided in the standard: (1) If the flavor consists of one ingredient, it shall be declared by its common or usual name. (2) If the flavor consists of two or more ingredients, the label either may declare
> each ingredient by its common or usual name or may state “All flavor ingredients contained in this product are approved for use in a regulation of the Food and Drug Administration.”
- 方法论陈述：§101.22 的豁免只针对 403(k)（人工香料/色素/化学防腐剂声明）这一条义务，按场景切三支：① 非包装且单元太小、无法以足够显著性标注 → 免；② 零售店散装容器陈列时，只要「散装容器标签清晰可见」或「柜台卡/标牌显著载明 403(k) 信息」→ 免；③ 果蔬收获前作为农药施用的化学防腐剂 → 免（对象限定为该防腐剂）。另有 (g) 的 B2B 分流：香料运给食品制造商（非消费者）时，单一成分用通用名；多成分可逐一具名或统一声明「全部香料成分均经 FDA 规章批准使用」，但未列入规章的香料成分与非香料成分仍须单列；已有标准身份者从标准。这套豁免与 §101.100/§101.9(j)/§101.108 又不同源。
- 可回答的新问题：小颗散装糖果印不下 "artificial color"，是否可既援引 (d) 又在柜台上放卡？(f) 的采前农药豁免能否延伸到采后保鲜剂？(g) 的「批准声明」能否用在直接售消费者的香料瓶上？
- 跨域佐证：〔§ 101.100〕配料表义务豁免（different object）；〔§ 101.9(j)(16)〕散装容器食品的营养标签豁免（同场景、不同义务）；〔§ 101.2(f)〕标签太小须请愿替代传播方式（另一处理路径）。
- 建议归属子卡：特定品类与警示

### CAND-FW-66: 「purports to contain juice」触发 + 百分比声明四分支
- 条款出处：〔§ 101.30(a)(b)(1)(2)(3)(c)(d)〕 + pdf-page 224–225
- 原文引用（英文逐字，≤100 词/段）：
> (a) This section applies to any food that purports to be a beverage that contains any fruit or vegetable juice (i.e., the product's advertising, label, or labeling bears the name of, or variation on the name of, or makes any other direct or indirect representation with respect to, any fruit or vegetable juice), or the label or labeling bears any vignette (i.e., depiction of a fruit or vegetable) or other pictorial representation of any fruit or vegetable, or the product contains color and flavor that gives the beverage the appearance
> and taste of containing a fruit or vegetable juice. The beverage may be carbonated or noncarbonated, concentrated, full-strength, diluted, or contain no juice.
> (b)(1) If the beverage contains fruit or vegetable juice, the percentage shall be declared by the words “Contains __ percent (or %) ______ juice” or “__ percent (or %) juice,” or a similar phrase, with the first blank filled in with the percentage expressed as a whole number not greater than the actual percentage of the juice
> (2) If the beverage contains less than 1 percent juice, the total percentage juice shall be declared as “less than 1 percent juice” or “less than 1 percent ______ juice” with the blank filled in with the name of the particular fruit or vegetable.
> (d) If the beverage does not meet the criteria for exemption from total juice percentage declaration as described in paragraph (c) of this section and contains no fruit or vegetable juice, but the labeling or color and flavor of the beverage represents, suggests, or implies that fruit or vegetable juice may be present... then the label shall declare “contains zero (0) percent (or %) juice”.
- 方法论陈述：先用极宽的「purports」闸门判定本条是否适用：advertising/label/labeling 出现果蔬汁名称或其变体或任何直接/间接表征，或出现水果/蔬菜 vignette/图形，或产品色素与风味使其外观口味像含汁——不论是否碳酸、浓缩、稀释甚至完全不含汁，都进入。进入后按实际含汁量四分支：含汁 → 声明百分比（整数且不得高于实际，可写 "Contains 50 percent apple juice"）；<1% → "less than 1 percent juice"；100% 且含非汁成分但未降低可溶性固形物/体积、且该声明与配料表不在同面 → 须加 "with added ____"；完全不含汁但曾触发 purports → "contains zero (0) percent juice" 或 "contains no ____ juice"。唯一出口是 (c)：少量汁仅作调味、用 "flavor/flavored/flavoring" 描述，且不含 "juice" 字样（配料表除外）、无果汁渗出的显式 vignette、无果肉/汁状物理特征 → 免百分比声明。
- 可回答的新问题：一瓶完全不含果汁但印了桃子图案的汽水要不要标 "0% juice"？"strawberry flavored" 饮料加了一张草莓照片，还能援引 (c) 豁免吗？(b)(1) 的「整数且不得高于实际」是否允许把 49.8% 写成 50%？
- 跨域佐证：〔§ 101.22(i)〕characterizing flavor 的 vignette 触发（同构）；〔§ 101.3(f)〕品名中可被要求标注特征配料百分比；〔§ 101.18(b)(c)〕品名/地理暗示的误导判定；〔§ 101.30(e)(f)(g)〕百分比声明的落位（信息面板优先、无信息面板则 PDP）。
- 建议归属子卡：特定品类与警示

### CAND-FW-67: 果汁百分比「Brix / 可溶性固形物 / 体积比」计算链与反规避
- 条款出处：〔§ 101.30(h)(1)(2)(i)(j)(k)(l)〕 + pdf-page 226–228（(h)(1) Brix 表为数值区，回原表核对）
- 原文引用（英文逐字，≤100 词/段）：
> (1) In enforcing these regulations, the Food and Drug Administration will calculate the labeled percentage of juice from concentrate found in a juice or juice beverage using the minimum Brix levels listed below where single-strength (100 percent) juice has at least the specified minimum Brix listed below:
> (2) If there is no Brix level specified in paragraph (h)(1) of this section, the labeled percentage of that juice from concentrate in a juice or juice beverage will be calculated on the basis of the soluble solids content of the single-strength (unconcentrated) juice used to produce such concentrated juice.
> (i) Juices directly expressed from a fruit or vegetable (i.e., not concentrated and reconstituted) shall be considered to be 100 percent juice and shall be declared as “100 percent juice.”
> (j) Calculations of the percentage of juice in a juice blend or a diluted juice product made directly from expressed juice (i.e., not from concentrate) shall be based on the percentage of the expressed juice in the product computed on a volume/volume basis.
> (k) If the product is a beverage that contains a juice whose color, taste, or other organoleptic properties have been modified to the extent that the original juice is no longer recognizable at the time processing is complete, or if its nutrient profile has been diminished to a level below the normal nutrient range for the juice, then that juice to which such a major modification has been made shall not be included in the total percentage juice declaration.
> (l) A beverage required to bear a percentage juice declaration on its label, that contains less than 100 percent juice, shall not bear any other percentage declaration that describes the juice content of the beverage in its label or in its labeling (e.g., “100 percent natural” or “100 percent pure”). However, the label or labeling may bear percentage statements clearly unrelated to juice content (e.g., “provides 100 percent of U.S. RDA of vitamin C”).
- 方法论陈述：把 fW-66 声明的「百分比」变成可核对计算：① 浓缩还原汁 → FDA 按 (h)(1) 的 minimum Brix 表折算（**该表为流式数值，文本层不可逐字引用，须回原表核对具体 Brix 值并复核快照日期**）；② 表中无对应 Brix → 按用于制浓缩汁的 single-strength 汁的可溶性固形物含量计算 (h)(2)；③ 直接压榨、未经浓缩复原的汁 → 视为 100% 汁、标 "100 percent juice" (i)；④ 直接以压榨汁配的混合/稀释汁 → 按体积/体积比计算 (j)。两条反规避：(k) 色素/口味/感官被改到原汁不可辨识、或营养剖面低于该汁正常范围 → 该汁不得计入总百分比；(l) 含汁 <100% 的产品不得再出现任何其他描述汁含量的百分比（"100 percent natural"/"100 percent pure"），但明确与汁含量无关的百分比（如 "100% U.S. RDA of vitamin C"）允许。
- 可回答的新问题：把橙汁脱色脱酸后重新加香，还能计进 "100% juice" 吗？一款 30% 汁饮料同时印 "100% pure" 与 "provides 100% DV vitamin C"，哪句违规？(h)(1) 表内某果汁 Brix 值在 2026 快照与旧版不同时以哪个为准？
- 跨域佐证：〔§ 101.30(b)(3)〕100% 汁含非汁成分时 "with added ____" 的措辞规则；〔§ 101.30(e)(f)(g)〕声明落位；〔§ 101.9(b)(9)〕营养素按 as packaged / drained solids 基准（另一套「基准」判定）。
- 建议归属子卡：特定品类与警示

### CAND-FW-68: 膳补营养标签「默认 + (h) 豁免」+ 按有无 RDI/DRV 二分流
- 条款出处：〔§ 101.36(a)(b)(1)(b)(2)〕 + pdf-page 228–230
- 原文引用（英文逐字，≤100 词/段）：
> The label of a dietary supplement that is offered for sale shall bear nutrition labeling in accordance with this regulation unless an exemption is provided for the product in paragraph (h) of this section.
> The serving size shall be determined in accordance with §§ 101.9(b) and 101.12(b), Table 2. Serving size for dietary supplements shall be expressed using a term that is appropriate for the form of the supplement, such as “tablets,” “capsules,” “packets,” or “teaspoonfuls.”
> The (b)(2)-dietary ingredients to be declared, that is, total calories, total fat, saturated fat, trans fat, cholesterol, sodium, total carbohydrate, dietary fiber, total sugars, added sugars, protein, vitamin D, calcium, iron, and potassium, shall be declared when they are present in a dietary supplement in quantitative amounts by weight that exceed the amount that can be declared as zero in nutrition labeling of foods in accordance with § 101.9(c). Calories from saturated fat, polyunsaturated fat, monounsaturated fat, soluble fiber, insoluble fiber, and sugar alcohol may be declared, but they shall be declared when a claim is made about them.
- 方法论陈述：先把 §101.9(a) 的「默认适用 + 列举豁免」原样套到膳食补充剂（唯一出口是 (h) 豁免），但格式改用 Supplement Facts 而非 Nutrition Facts。再按「该膳食成分有没有 RDI/DRV」二分：(b)(2)-dietary ingredients（有 RDI/DRV 的 15 项及子成分）按 §101.9(c) 的「能否标零」判定是否申报，且自愿项一作声称即转强制；其他膳食成分按 (b)(3) 走另一套（无 %DV、须列来源等）。serving size 仍回到 §101.9(b) 与 §101.12(b) Table 2，只是单位改用 tablets/capsules 等形态词。判定顺序：先定豁免 → 再定份量 → 再按 RDI/DRV 有无分流申报内容 → 最后查「是否作声称」把自愿项翻成强制。
- 可回答的新问题：一款只含氨基酸的膳补为何不许申报 protein？膳补的 "tablets" 份量与 §101.12 Table 2 的 RACC 如何对应？§101.9(j)(6) 把膳补转介到 §101.36，是否意味着膳补同时免 §101.9 与 §101.13？
- 跨域佐证：〔§ 101.9(j)(6)〕膳补免 §101.9 但须按 §101.36 标；〔§ 101.36(b)(2)(iii)〕无 DRV/RDI 的子成分不得给 %DV；〔§ 101.13(q)(3)(ii)〕膳补中无 RDI/DRV 成分的百分比声明须并列实际量。
- 建议归属子卡：营养标签与份量

### CAND-FW-69: 生鲜果蔬鱼「自愿标签 → substantial compliance 评估 → 不达标转强制」自我监管闸门
- 条款出处：〔§ 101.42(a)(d)(e)(f)〕〔§ 101.43(a)(b)(c)(d)〕 + pdf-page 243–244
- 原文引用（英文逐字，≤100 词/段）：
> The Food and Drug Administration (FDA) urges food retailers to provide nutrition information, as provided in § 101.9(c), for raw fruit, vegetables, and fish at the point-of-purchase. If retailers choose to provide such information, they should do so in a manner that conforms to the guidelines in § 101.45.
> (f) If FDA determines that there is not substantial compliance with the guidelines for raw fruit and vegetables or for raw fish, the agency will at that time issue proposed regulations requiring that any person who offers raw fruit and vegetables or fish to consumers provide, in a manner prescribed by regulations, the nutrition information required by § 101.9. Final regulations would have to be issued 6 months after issuance of proposed regulations, and they would become effective 6 months after the date of their promulgation.
> (a) The Food and Drug Administration (FDA) will judge a food retailer who sells raw agricultural commodities or raw fish to be in compliance with the guidelines in § 101.45 with respect to raw agricultural commodities if the retailer displays or provides nutrition labeling for at least 90 percent of the raw agricultural commodities listed in § 101.44 that it sells
> (c) FDA will find that there is substantial compliance with the guidelines in § 101.45 if it finds based on paragraph (a) of this section that at least 60 percent of all stores that are evaluated are in compliance.
- 方法论陈述：这是一条「市场自律 → 量化评估 → 条件性转强制」的时间轴闸门。起点是自愿：FDA 只 urges 零售商按 §101.45 在销售点提供 §101.9(c) 口径营养信息，对象限定 §101.44 的 20 种最常消费品类。评估分两层阈值：单店层面须对所列品类的 ≥90% 提供合规标签；行业层面 FDA 抽 2,000 家代表性门店，若 ≥60% 门店达标即认定 substantial compliance，指南维持、每 2 年复评；若不达标 → 启动强制规章（提案后 6 个月出最终规则、再 6 个月生效）。果蔬与鱼分别评估 (d)。
- 可回答的新问题：一家只卖 15 种 top-20 品类的店，「90%」按 15 种还是 20 种算？若 FDA 认定果蔬达标但生鱼不达标，强制规章只覆盖鱼吗？§101.45 的自愿标签数值来自 Appendix C/D（图形、转引未收），能否用企业自有数据库替代？
- 跨域佐证：〔§ 101.45(b)(c)〕top-20 用 FDA 附录数据、非 top-20 可用数据库且受 §101.9(g) 合规约束；〔§ 101.9(j)(10)〕生鲜果蔬鱼在「无声称/无营养信息」条件下免营养标签（本自愿体系的强制底线）；〔§ 101.9(g)(8)〕FDA 批准数据库替代取样合规。
- 建议归属子卡：营养标签与份量

### CAND-FW-70: Subpart D 逐词声称「三要件通用门 + 逐词定量阈值」元框架
- 条款出处：〔§ 101.54(a)〕〔§ 101.56(a)〕〔§ 101.60(a)〕〔§ 101.61(a)〕〔§ 101.62(a)〕 + pdf-page 247 / 250 / 253
- 原文引用（英文逐字，≤100 词/段）：
> (a) General requirements. Except as provided in paragraph (e) of this section, a claim about the level of a nutrient in a food in relation to the Reference Daily Intake (RDI) established for that nutrient in § 101.9(c)(8)(iv) or Daily Reference Value (DRV) established for that nutrient in § 101.9(c)(9), (excluding total carbohydrates) may only be made on the label or in labeling of the food if: (1) The claim uses one of the terms defined in this section in accordance with the definition for that term; (2) The claim
> is made in accordance with the general requirements for nutrient content claims in § 101.13; and (3) The food for which the claim is made is labeled in accordance with § 101.9, § 101.10, or § 101.36, as applicable.
> A claim about the calorie or sugar content of a food may only be made on the label or in the labeling of a food if: (1) The claim uses one of the terms defined in this section in accordance with the definition for that term; (2) The claim is made in accordance with the general requirements for nutrient content claims in § 101.13; (3) The food for which the claim is made is labeled in accordance with § 101.9, § 101.10, or § 101.36, as applicable; and (4) For
> dietary supplements, claims regarding calories may not be made on products that meet the criteria in § 101.60(b)(1) or (b)(2) for “calorie free” or “low calorie” claims
> The terms “calorie free,” “free of calories,” “no calories,” “zero calories,” “without calories,” “trivial source of calories,” “negligible source of calories,” or “dietarily insignificant source of calories” may be used on the label or in the labeling of foods, provided that: (i) The food contains less than 5 calories per reference amount customarily consumed and per labeled serving.
> The terms “high,” “rich in,” or “excellent source of” may be used on the label and in the labeling of foods, except meal products as defined in § 101.13(l) and main dish products as defined in § 101.13(m), provided that the food contains 20 percent or more of the RDI or the DRV per reference amount customarily consumed.
- 方法论陈述：Subpart D 每条都用同一个三段门：① 所用词必须是本节逐词定义的术语（同义词须在此列或经 §101.69 请愿）；② 必须符合 §101.13 通则（express/implied、disclosure、relative claims、位置）；③ 该食品已按 §101.9/§101.10/§101.36 标营养标签。通过三门后才进入该描述符的定量阈值："high" ≥20% RDI/DRV per RACC、"good source" 10–19%、"calorie free" <5 cal per RACC 且 per labeled serving、"light" 按脂肪供能比 ≥50% 与否分 50% 脂降 / 1/3 卡降、低热量 ≤40 cal 等。meal/main dish 常另设数值。判定纪律是「先过通用门、再对号入座阈值、最后查类别例外」，不能只拿一个数值就说合规。
- 可回答的新问题：产品达到 "high" 的 20% 阈值但没做 Nutrition Facts，能否作 "high in calcium"？"light" 的 1/3 卡降与 50% 脂降是「或」还是「且」？§101.60(b)(1) 的 <5 cal 与 §101.9(c)(1) 的「<5 cal 可标零」是不是同一判据？
- 跨域佐证：〔§ 101.13(b)〕含量声称通则（三门之一）；〔§ 101.13(h)(j)(l)(m)〕disclosure、relative claims、meal/main dish 定义；〔§ 101.12(g)〕/〔§ 101.13(p)〕RACC 是阈值分母、serving size≠RACC 须附依据声明；〔§ 101.69〕新描述符/同义词须请愿授权。
- 建议归属子卡：声称闸门

### CAND-FW-71: 「不构成 implied claim」六类负面清单（避免误伤的非营养陈述）
- 条款出处：〔§ 101.65(b)(1)–(6)〕 + pdf-page 272–273
- 原文引用（英文逐字，≤100 词/段）：
> Label statements that are not implied claims. Certain label statements about the nature of a product are not nutrient content claims unless such statements are made in a context that would make them an implied claim under § 101.13(b)(2). The following types of label statements are generally not implied nutrient content claims and, as such, are not subject to the requirements of § 101.13 and this section:
> (1) A claim that a specific ingredient or food component is absent from a product, provided that the purpose of such claim is to facilitate avoidance of the substances because of food allergies (see § 105.62 of this chapter), food intolerance, religious beliefs, or dietary practices such as vegetarianism or other nonnutrition related reason, e.g., “100 percent milk free;”
> (2) A claim about a substance that is nonnutritive or that does not have a nutritive function, e.g., “contains no preservatives,” “no artificial colors;”
> (4) A statement of identity for a food in which an ingredient constitutes essentially 100 percent of a food (e.g., “corn oil,” “oat bran,” “dietary supplement of vitamin C 60 mg tablet”).
> (5) A statement of identity that names as a characterizing ingredient, an ingredient associated with a nutrient benefit (e.g., “corn oil margarine,” “oat bran muffins,” or “whole wheat bagels”), unless such claim is made in a context in which label or labeling statements, symbols, vignettes, or other forms of communication suggest that a nutrient is absent or present in a certain amount
- 方法论陈述：这是 FW-42/FW-50「暗示同等受管」的必要反向配平，防止把普通产品描述误判成含量声称。六类默认安全的陈述：(1) 为过敏/不耐受/宗教/素食等**非营养**原因声明某成分不存在（"100 percent milk free"）；(2) 关于非营养性或无营养功能物质的陈述（"no preservatives"）；(3) 增值配料陈述（"made with real butter"）；(4) 单配料食品的品名（"corn oil"）；(5) 以表征配料命名的品名（"oat bran muffins"）；(6) 依 part 105 说明特殊膳食用途。共同前提是「语境不使其落入 §101.13(b)(2) 的 implied」——(5) 明文加了「除非符号/vignette 等暗示某营养素有无」的回扣。判定顺序：先扫六类安全港 → 再看整体语境有无暗示营养素水平 → 有则拉回 §101.13/本节。
- 可回答的新问题："no gluten" 是否可援引 (1) 的过敏避免安全港，还是须按 §101.91 单独判定？"oat bran muffins" 旁边印了高纤图标，(5) 的安全港还在吗？"made with real butter" 与 §101.13(c) 的「营养标签外陈述」如何区分？
- 跨域佐证：〔§ 101.91〕gluten-free 是独立的 20 ppm 定量定义（不靠本清单）；〔§ 101.13(b)(2)〕implied claim 定义是本清单的回扣条件；〔§ 101.65(a)〕若确属 implied claim 仍须过三要件；〔§ 101.14(a)(1)〕健康声称侧的同类「语境暗示」判定。
- 建议归属子卡：声称闸门

### CAND-FW-72: 「含某配料 / 某制法 → 自动转译为 low 或 good source」隐含声称闸门
- 条款出处：〔§ 101.65(c)(1)(2)(3)〕 + pdf-page 273
- 原文引用（英文逐字，≤100 词/段）：
> (1) Claims about the food or an ingredient therein that suggest that a nutrient or an ingredient is absent or present in a certain amount (e.g., “high in oat bran”) are implied nutrient content claims and must comply with paragraph (a) of this section.
> (2) The phrases “contains the same amount of [nutrient] as a [food]” and “as much [nutrient] as a [food]” may be used on the label or in the labeling of foods, provided that the amount of the nutrient in the reference food is enough to qualify that food as a “good source” of that nutrient, and the labeled food, on a per serving basis, is an equivalent, good source of that nutrient
> (3) Claims may be made that a food contains or is made with an ingredient that is known to contain a particular nutrient, or is prepared in a way that affects the content of a particular nutrient in the food, if the finished food is either “low” in or a “good source” of the nutrient that is associated with the ingredient or type of preparation. If a more specific level is claimed (e.g., “high in ______), that level of the nutrient must be present in the food. For example, a
> claim that a food contains oat bran is a claim that it is a good source of dietary fiber; that a food is made only with vegetable oil is a claim that it is low in saturated fat; and that a food contains no oil is a claim that it is fat free.
- 方法论陈述：把「看起来只是在说配料/工艺」的陈述映射成法定的营养素水平声称。三条规则：① 描述食品或配料暗示某营养素有无/多少（"high in oat bran"）→ 直接是 implied claim，须过 §101.65(a) 三要件；② "as much [nutrient] as a [food]" 句式 → 双重门槛：参照食品该营养素须够 "good source"，且本食品按 per serving 也是等效 good source；③ 「含某已知含该营养素的配料」或「某制法影响该营养素含量」→ 成品须真的达到 "low" 或 "good source"；若声称了更具体水平（"high in …"）则须真有那个水平。法规给的转译表：含燕麦麸＝声称 good source of dietary fiber；只用植物油＝声称 low saturated fat；不含油＝声称 fat free。
- 可回答的新问题：写「含菠菜」是否等于作了某营养素声称、要不要按 Subpart D 核对阈值？"as much calcium as a glass of milk" 里的参照牛奶若本身不够 good source，句式还能用吗？「不含油」被转译为 fat free 后，是否还要过 §101.62(b)(1) 的 <0.5 g 阈值？
- 跨域佐证：〔§ 101.13(b)(2)(i)〕implied claim 定义；〔§ 101.54(c)(1)〕"good source" 的 10–19% 阈值；〔§ 101.62(b)(1)(2)〕"fat free"/"low fat" 阈值；〔§ 101.13(j)(1)(ii)(B)〕relative claim 参照食品取值规则。
- 建议归属子卡：声称闸门

### CAND-FW-73: "healthy" 声称的 food group equivalent 门槛（回原表核对）
- 条款出处：〔§ 101.65(d)(1)(2)(3)〕 + pdf-page 273–274
- 原文引用（英文逐字，≤100 词/段）：
> (1) This paragraph covers labeling claims that are implied nutrient content claims because they suggest that a food may help consumers maintain healthy dietary practices due to its nutrient content, where there is also implied or explicit information about the nutrition content of the food.
> (2) For purposes of this section, a “food group equivalent” identifies qualifying amounts of foods from each food group based on nutritional content. A food group equivalent is equal to the following: TABLE 1 TO PARAGRAPH (d)(2)
> (3) You may use the term “healthy” or derivative terms “health,” “healthful,” “healthfully,” “healthfulness,” “healthier,” “healthiest,” “healthily,” and “healthiness” as an implied nutrient content claim on the label
- 方法论陈述：把 "healthy" 及 8 个派生词统一当作 implied nutrient content claim，不能当普通营销词。判定链：先确认语境满足 §101.13(b)(2)(ii)（暗示有助维持健康膳食 + 伴随营养信息）→ 再用 (d)(2) 的 food group equivalent 概念核算食品是否含有规定量的各食物组（蔬菜/水果/谷物/乳制品/蛋白食品）→ 再叠加具体的营养素限量门槛。**TABLE 1 及各当量数值属表值／图形区，文本层不可逐字引用，须回原表核对并复核 2024 修订（89 FR 106162）后的现行阈值。**
- 可回答的新问题：把品牌名注册成 "Healthiest" 能否绕开 (d)(3)？(d)(2) 的食物组当量与 §101.13(l)(m) 的 meal/main dish「40 g 份」是不是同一套量纲？(d)(3) 的派生词清单是否与 §101.69(b)(2) 的「同义词请愿」冲突？
- 跨域佐证：〔§ 101.13(q)(7)〕品牌名中的 implied claim 须 FDA 授权、按 §101.69(o) 请愿；〔§ 101.13(l)(m)〕meal/main dish 的食物组定义；〔§ 101.65(a)〕implied claim 三要件。
- 建议归属子卡：声称闸门

### CAND-FW-74: §101.69 含量声称请愿「三分流 + 时限链」★
- 条款出处：〔§ 101.69(a)(b)(k)(m)(n)(o)〕 + pdf-page 283–290
- 原文引用（英文逐字，≤100 词/段）：
> (b) Petitions included in this section are: (1) Petitions for a new (heretofore unauthorized) nutrient content claim; (2) Petitions for a synonymous term (i.e., one that is consistent with a term defined by regulation) for characterizing the level of a nutrient; and (3) Petitions for the use of an implied claim in a brand name.
> (k) The petition shall include a statement signed by the person responsible for the petition, that to the best of his knowledge, it is a representative and balanced submission that includes unfavorable information, as well as favorable information, known to him pertinent to the evaluation of the petition.
> (m)(1) Petitions for a new nutrient content claim shall include the following data and be submitted in the following form. ... A. A statement identifying the descriptive term and the nutrient that the term is intended to characterize with respect to the level of such nutrient. ... B. A detailed explanation, supported by any necessary data, of why use of the food component characterized by the claim is of importance in human nutrition ... C. Analytical data ... D. A detailed analysis of the potential effect of the use of the proposed claim on food consumption ...
> (3) Within 100 days of the date of receipt of the petition, FDA will notify the petitioner by letter that the petition has either been filed or denied. If denied, the notification shall state the reasons therefor. ... If FDA does not act within such 100 days, the petition shall be deemed to be denied unless an extension is mutually agreed upon by the FDA and the petitioner. ... (5) If FDA issues a proposal, the rulemaking shall be completed within 540 days of the date of receipt of the petition.
> Should FDA not notify the petitioner of his decision on the petition within 100 days, the petition shall be considered to be granted.
- 方法论陈述：扩张「允许使用的含量声称词表」只能经 §101.69 请愿，按目标三分流：① 新描述符（(m)，须交 A 描述符与营养素及条件、B 营养重要性与现有术语为何不足、C AOAC 分析数据、D 对食物消费与营养摄入的影响、E 环境评估）；② 同义词（(n)，须证明与已有定义术语一致且不误导，FDA 90 天内准予或否决、并在 FR 公告）；③ 品牌名中的 implied claim（(o)，须证明不误导、附数据证明实际营养素水平达标，FR 公示 30 天征求意见）。共通要件：材料分栏、外语附英译、GLP/IRB/知情同意声明、环境评估、签名与「代表性且平衡（含不利信息）」陈述 (k)。时限链：15 天收件通知 → 100 天 filed/denied（不作为视为否决）→ 90 天提案或否决 → 540 天完成 rulemaking；**特例：(o)(4) 品牌名请愿 100 天不作为「视为准予」，与 (m)(3) 相反。**
- 可回答的新问题：企业想用自创词 "lite-ish" 应走 (m) 还是 (n)？品牌名请愿与同义词请愿的「逾期后果」为何相反？"代表性且平衡"陈述漏交不利数据，是形式驳回还是实体驳回？
- 跨域佐证：〔§ 101.13(q)(7)〕品牌名 implied claim 授权后按 §101.69(o) 请愿；〔§ 101.13(b)(4)〕不误导的拼写变体可直接使用、无需请愿；〔§ 101.70〕健康声称请愿的 A–F 要件与时限链同构；〔§ 101.12(h)〕RACC 请愿的 14 项要件。
- 建议归属子卡：豁免与效力层

### CAND-FW-75: §101.70 健康声称请愿「A–F 要件 + SSA 摘要 + 四段时限」★
- 条款出处：〔§ 101.70(a)(b)(f)(h)(j)〕 + pdf-page 290–295
- 原文引用（英文逐字，≤100 词/段）：
> Any interested person may petition the Food and Drug Administration (FDA) to issue a regulation regarding a health claim.
> A. Preliminary requirements. A complete explanation of how the substance conforms to the requirements of § 101.14(b) (21 CFR 101.14(b)).
> B. Summary of scientific data. The summary of scientific data provides the basis upon which authorizing a health claim can be justified as providing the health benefit. The summary must establish that, based on the totality of publicly available scientific evidence (including evidence from well-designed studies conducted in a manner which is consistent with generally recognized scientific procedures and principles), there is significant scientific agreement among experts qualified by scientific training and experience to evaluate such claims, that the claim is supported by such evidence.
> D. Model health claim. One or more model health claims that represent label statements that may be used on a food label or in labeling for a food to characterize the relationship between the substance in a food to a disease or health-related condition that is justified by the summary of scientific data provided in section C of the petition.
> (2) Within 100 days of the date of receipt of the petition, FDA will notify the petitioner by letter that the petition has either been filed for comprehensive review or denied. The agency will deny a petition without reviewing the information contained in “B. Summary of Scientific Data” if the information in “A. Preliminary Requirements” is inadequate in explaining how the substance conforms to the requirements of § 101.14(b).
> (4)(i) Within 270 of the date of publication of the proposal, FDA will publish a final rule that either authorizes use of the health claim or explains why the agency has decided not to authorize one.
- 方法论陈述：这是「把未授权健康声称变成已授权」的唯一合法通道（对应 §101.14(e)(1) 的禁止）。请愿须按 (f) 的 A–F 六栏提交：A 初步要求（物质如何符合 §101.14(b) 适格性，含配料 GRAS/食品添加剂/先前 sanction 依据）→ B 科学数据摘要（须基于「全部公开可得科学证据的总体」证明 SSA，并回答最适摄入量、不良反应水平、特殊人群、其他正负营养因素四个问题，分析对食物消费与营养摄入的影响）→ C 代表性食品中该物质的 AOAC 分析数据 → D 模型健康声称（含结论简述 + 如何助消费者达成总膳食目标）→ E 文献检索与全部支持/不利资料附件 → F 环境评估。另加 GLP/IRB/知情同意、公开披露 (e)、平衡性陈述 (h)、签名 (i)。时限：15 天收件 → 100 天 filed/denied（A 不合格可直接不看 B）→ 90 天提案或否决 → 提案公布后 270 天出最终规则（最多两次各 90 天展期，但不得超收件后 540 天）。
- 可回答的新问题：请愿 A 栏没讲清物质适格性，FDA 是否还会审 B 栏的 SSA 证据？企业提交的模型声称与 §101.72–83 已有模型措辞冲突时如何处理？「全部公开可得证据」是否允许只提交支持性论文？
- 跨域佐证：〔§ 101.14(b)(c)〕物质适格性与 SSA 是 A/B 栏的实体依据；〔§ 101.14(d)(1)〕FDA 依 (c) 才在 Subpart E 提议授权；〔§ 101.69〕含量声称请愿的三分流与时限链同构；〔§ 101.71〕被否决/未授权声称的负面清单。
- 建议归属子卡：豁免与效力层

### CAND-FW-76: 已授权健康声称「六段结构」+ 未授权负面清单（不逐条做能力）
- 条款出处：〔§ 101.71〕〔§ 101.72(a)(b)(c)(d)(e)〕〔§ 101.83(e)〕 + pdf-page 295–297 / 329–330
- 原文引用（英文逐字，≤100 词/段）：
> Health claims not authorized for foods in conventional food form or for dietary supplements of vitamins, minerals, herbs, or other similar substances: (a) Dietary fiber and cardiovascular disease. (b) Zinc and immune function in the elderly.
> (1) All requirements set forth in § 101.14 shall be met. (2) Specific requirements — (i) Nature of the claim. A health claim associating calcium or, when appropriate, calcium and vitamin D with a reduced risk of osteoporosis may be made on the label or labeling of a food described in paragraphs (c)(2)(ii) and (d)(1) of this section, provided that:
> (e) Model health claims. The following model health claims may be used in food labeling to describe the relationship between calcium and osteoporosis: Adequate calcium throughout life, as part of a well-balanced diet, may reduce the risk of osteoporosis.
> Model health claim. The following model health claims may be used in food labeling to describe the relationship between diets that include plant sterol or stanol esters and reduced risk of heart disease:
- 方法论陈述：Subpart E 的 §101.72–83 不是 12 条各自为政的规则，而是可复用的六段模板：(a) Relationship（物质—疾病的科学关系与机制）→ (b) Significance（公共卫生意义）→ (c) Requirements（(1) 声明「§101.14 全部要求须满足」+ (2) Specific requirements：Nature of the claim 逐条允许/禁止措辞、Nature of the substance、Nature of the food eligible 的定量门槛）→ (d) Optional information（可附加的风险因素、机制、膳食指南引用等）→ (e) Model health claims（可直接照抄的模型句）→ 末尾 FR citation。使用时的判定链：先查 §101.71 未授权负面清单（如 dietary fiber & CVD、zinc & immune function）→ 若落入则禁止；否则找对应专条 → 先过 §101.14 通用门 → 再过该专条的 Nature of claim/food 门槛 → 最后用模型措辞或等价表述。**BOOK_OVERVIEW 明确：§101.72–83 逐条模型措辞全文只作可检索条文保留，不逐条做成能力卡。**
- 可回答的新问题：企业自创一句「科学上等价但更顺口」的健康声称，是否合规？§101.71 只列 2 项，是否意味着其他未列组合都自动授权？(c)(1)「§101.14 全部要求」与 (c)(2) 专条门槛冲突时谁优先？
- 跨域佐证：〔§ 101.14(d)(2)(e)〕依规章作声称的七项一般要求与六要件禁止；〔§ 101.70〕请愿是扩张该清单的唯一通道；〔§ 101.83(c)(1)〕个别专条明文对 §101.14 开例外（见 FW-77）。
- 建议归属子卡：声称闸门

### CAND-FW-77: 已授权健康声称专条「对 §101.14 通用门的逐条除外」闸门
- 条款出处：〔§ 101.83(c)(1)〕〔§ 101.83(c)(2)(i)(iii)〕 + pdf-page 326–329
- 原文引用（英文逐字，≤100 词/段）：
> (1) General. All requirements set forth in § 101.14 shall be met, except § 101.14(a)(4) with respect to the disqualifying level for total fat per 50 grams (g) in dressings for salad and spreads and § 101.14(e)(6) with respect to dressings for salad.
> (C) The food must meet the limit for total fat in § 101.14(a)(4), except that spreads and dressings for salad are not required to meet the limit for total fat per 50 g if the label of the food bears a disclosure statement that complies with § 101.13(h); and (D) The food must meet the minimum nutrient contribution requirement in § 101.14(e)(6) unless it is a dressing for salad.
> (i) Nature of the claim. A health claim associating diets that include plant sterol/stanol esters with reduced risk of heart disease may be made on the label or labeling of a food described in paragraph (c)(2)(iii) of this section, provided that: (A) The claim states that plant sterol/stanol esters should be consumed as part of a diet low in saturated fat and cholesterol; (B) The claim states that diets that include plant sterol/stanol esters “may” or “might” reduce the risk of heart disease; ... (E) The claim does not attribute
> any degree of risk reduction for CHD to diets that include plant sterol/stanol esters; (F) The claim does not imply that consumption of diets that include plant sterol/stanol esters is the only recognized means of achieving a reduced risk of CHD
- 方法论陈述：FW-76 的六段模板里，「(c)(1) 通用门」并非绝对——个别专条会在开头明文写出「§101.14 全部要求须满足，**except** …」。以 §101.83 为例，它把 §101.14(a)(4) 的 per 50 g 总脂 disqualifying level 与 §101.14(e)(6) 的 10% 营养贡献门槛，对沙拉酱/涂抹酱作了除外，并在 (c)(2)(iii)(C)(D) 复述该除外、同时把「加 §101.13(h) disclosure」设为交换条件。判定顺序因此是：先读专条 (c)(1) 有无 except → 有则只对被点名的款项与品类放宽 → 未被点名的 §101.14 要件仍全部适用 → 再走 (c)(2) Nature of the claim 的逐条措辞限制（may/might、疾病用语、不得量化风险降低、不得暗示唯一手段、须写每日摄入量）。**不可把某一条的除外「借」到另一条。**
- 可回答的新问题：§101.83 对沙拉酱放宽 disqualifying level，能否类推到 §101.82 大豆蛋白声称？"(c)(1)" 没提 §101.14(e)(3)，是否意味着沙拉酱仍须过其余 disqualifying 项？(B) 强制 "may/might" 与 (E) 禁止量化风险降低是什么关系？
- 跨域佐证：〔§ 101.14(e)(3)〕超 disqualifying level 时以 §101.13(h) disclosure 换取声称的通用例外；〔§ 101.72(c)(1)〕多数专条写「All requirements set forth in § 101.14 shall be met」无除外；〔§ 101.13(h)〕disclosure 语句规格。
- 建议归属子卡：声称闸门

### CAND-FW-78: gluten-free「20 ppm 定量定义 + 合规方法分流 + 联邦优先」★
- 条款出处：〔§ 101.91(a)(3)(b)(c)(d)〕 + pdf-page 330–332
- 原文引用（英文逐字，≤100 词/段）：
> (3) The labeling claim “gluten-free” means: (i) That the food bearing the claim in its labeling: (A) Does not contain any one of the following: (1) An ingredient that is a gluten-containing grain (e.g., spelt wheat); (2) An ingredient that is derived from a gluten-containing grain and that has not been processed to remove gluten (e.g., wheat flour); or (3) An ingredient that is derived from a gluten-containing grain and that has been processed to remove gluten (e.g., wheat starch), if the use of that ingredient results in the presence
> of 20 parts per million (ppm) or more gluten in the food (i.e., 20 milligrams (mg) or more gluten per kilogram (kg) of food); or (B) Inherently does not contain gluten; and (ii) Any unavoidable presence of gluten in the food bearing the claim in its labeling is below 20 ppm gluten (i.e., below 20 mg gluten per kg of food).
> (2) A food that bears the claim “no gluten,” “free of gluten,” or “without gluten” in its labeling and fails to meet the requirements of paragraph (a)(3) of this section and, if applicable, paragraphs (c)(2) through (4) of this section will be deemed misbranded.
> (1) When compliance with paragraph (b) of this section is based on an analysis of the food, FDA will use a scientifically valid method that can reliably detect and quantify the presence of 20 ppm gluten in a variety of food matrices, including both raw and cooked or baked products. (2) When a scientifically valid method pursuant to paragraph (c)(1) of this section is not available because the food is fermented or hydrolyzed, the manufacturer of such foods bearing the claim must make and keep records regarding the fermented or
> hydrolyzed food demonstrating adequate assurance that: (i) The food is “gluten-free” in compliance with paragraph (a)(3) of this section before fermentation or hydrolysis
> (d) Preemption. A State or political subdivision of a State may not establish or continue into effect any law, rule, regulation, or other requirement that is different from the requirements in this section for the definition and use of the claim “gluten-free,” as well as the claims “no gluten,” “free of gluten,” or “without gluten.”
- 方法论陈述：Subpart F 的「既非含量声称也非健康声称」第三类，用纯定量阈值取代营销词判定。① 定义闸门：食品须 (A) 不含含麸质谷物、不含未去麸质的衍生配料、且含「已去麸质但致成品 ≥20 ppm」的衍生配料者不得标——或 (B) 天生不含麸质；并且 (ii) 任何不可避免的麸质存在 **below 20 ppm**。② 措辞同义 (b)(2)："no gluten"/"free of gluten"/"without gluten" 与 "gluten-free" 同义务，不符即错标；(b)(3) 若配料表/Contains wheat 声明中出现 "wheat"，须加星号并附「该小麦经处理使本食品符合 FDA gluten-free 要求」。③ 合规方法分流 (c)：有科学有效方法可直接检 20 ppm → 用检测；发酵/水解食品无有效方法 → 改以记录证明（发酵前合规、评估交叉接触、已采取防引入措施，记录留存 ≥2 年）；蒸馏食品 (c)(5) → 验证无蛋白。④ (d) 联邦优先：州/地方不得设不同要求。
- 可回答的新问题：「无添加麸质配料」但成品检出 19 ppm，能否标 gluten-free？发酵酱油无可用检测方法时，企业须留哪些记录才算「adequate assurance」？(a)(3)(A)(3) 的「已去麸质小麦淀粉」与 (b)(3) 的 "Contains wheat" 星号声明如何同时满足？
- 跨域佐证：〔§ 101.100(a)(4)〕亚硫酸盐 10 ppm 是**另一条款**的独立可检出阈值，不得与 20 ppm 混算；〔§ 101.65(b)(1)〕过敏/不耐受的「不含某成分」陈述默认不算 implied claim；〔§ 101.9(c)(6)(i)〕膳食纤维定义（同属定量型定义）；〔§ 101.13(b)〕含量声称通则（gluten-free 明确不在其列）。
- 建议归属子卡：特定品类与警示

### CAND-FW-79: 膳补「structure/function 声明 ↔ disease claim」闸门（落入即按药品监管）★
- 条款出处：〔§ 101.93(a)(b)(c)(d)(f)(g)〕 + pdf-page 332–334
- 原文引用（英文逐字，≤100 词/段）：
> (f) Permitted structure/function statements. Dietary supplement labels or labeling may, subject to the requirements in paragraphs (a) through (e) of this section, bear statements that describe the role of a nutrient or dietary ingredient intended to affect the structure or function in humans or that characterize the documented mechanism by which a nutrient or dietary ingredient acts to maintain such structure or function, provided that such statements are not disease claims under paragraph (g) of this section. If the label or labeling of a product marketed as a dietary supplement
> bears a disease claim as defined in paragraph (g) of this section, the product will be subject to regulation as a drug unless the claim is an authorized health claim for which the product qualifies.
> (2) FDA will find that a statement about a product claims to diagnose, mitigate, treat, cure, or prevent disease (other than a classical nutrient deficiency disease) under 21 U.S.C. 343(r)(6) if it meets one or more of the criteria listed below. These criteria are not intended to classify as disease claims statements that refer to the ability of a product to maintain healthy structure or function, unless the statement implies disease prevention or treatment. In determining whether a statement is a disease claim under these criteria, FDA will consider the context in which the claim is presented.
> (b) Disclaimer. The requirements in this section apply to the label or labeling of dietary supplements where the dietary supplement bears a statement that is provided for by section 403(r)(6) of the Federal Food, Drug, and Cosmetic Act (the act), and the manufacturer, packer, or distributor wishes to take advantage of the exemption to section 201(g)(1)(C) of the act that is provided by compliance with section 403(r)(6) of the act. ... This statement has not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.
> (a)(1) No later than 30 days after the first marketing of a dietary supplement that bears one of the statements listed in section 403(r)(6) ... the manufacturer, packer, or distributor of the dietary supplement shall notify the Office of Dietary Supplement Programs ... that it has included such a statement on the label or in the labeling of its product.
- 方法论陈述：把膳补标签上的一句话按「是否 disease claim」二分，后果极不对称。合法支（structure/function）：描述营养素/膳食成分对人体结构或功能的作用、或描述其维持该结构功能的机制，且须满足 (a) 首次上市 30 天内向 FDA 报备（含文本、成分、产品名、签名与真实性保证）、(b)(c) 附固定 disclaimer「未经 FDA 评估…不用于诊断、治疗、治愈或预防任何疾病」、(d) 紧邻或星号链接且每个有该声明的面板/页面都要有、(e) 粗体 ≥1/16 in。非法支（disease claim）：(g)(2) 列十项判据（对特定疾病/症状有作用、对异常状态有作用、通过产品名/配方/文献引用/"disease" 字样/图片符号等暗示、属于某类产品、替代疗法、增强疗法、影响疾病载体反应等），FDA 结合语境判断，命中任一即把产品按**药品**监管——唯一例外是「该产品符合的已授权健康声称」。必需营养素缺乏症（坏血病等）被 (g)(1) 排除在 disease 定义外。
- 可回答的新问题：写「支持免疫系统健康」是 structure/function 还是 disease claim？引用一篇关于某病的论文放在包装上，是否触发 (g)(2)(iv)(C)？已按 §101.93 报备并加 disclaimer，能否同时免 §101.70 的健康声称授权？
- 跨域佐证：〔§ 101.14(a)(5)〕/〔§ 101.93(g)(1)〕疾病定义同样排除必需营养素缺乏症（同构例外）；〔§ 101.14(e)(1)〕健康声称须 Subpart E 授权；〔§ 101.9(k)〕暗示疾病预防表述按 201(n)/403(a) 错标；〔§ 101.65(b)(1)〕过敏避免类「不含」陈述不算 implied claim。
- 建议归属子卡：声称闸门

### CAND-FW-80: "fresh" 前置「是否暗示未加工/未保存」闸门 + 四例外
- 条款出处：〔§ 101.95(a)(b)(c)(1)(2)〕 + pdf-page 334–335
- 原文引用（英文逐字，≤100 词/段）：
> The terms defined in this section may be used on the label or in labeling of a food in conformity with the provisions of this section. The requirements of the section pertain to any use of the subject terms as described in paragraphs (a) and (b) of this section that expressly or implicitly refers to the food on labels or labeling, including use in a brand name and use as a sensory modifier. However, the use of the term “fresh” on labels or labeling is not subject to the requirements
> of paragraph (a) of this section if the term does not suggest or imply that a food is unprocessed or unpreserved.
> (a) The term “fresh,” when used on the label or in labeling of a food in a manner that suggests or implies that the food is unprocessed, means that the food is in its raw state and has not been frozen or subjected to any form of thermal processing or any other form of preservation, except as provided in paragraph (c) of this section.
> (b) The terms “fresh frozen” and “frozen fresh,” when used on the label or in labeling of a food, mean that the food was quickly frozen while still fresh (i.e., the food had been recently harvested when frozen). Blanching of the food before freezing will not preclude use of the term “fresh frozen” to describe the food.
> (1) The following do not preclude the food from use of the term “fresh:” (i) The addition of approved waxes or coatings; (ii) The post-harvest use of approved pesticides; (iii) The application of a mild chlorine wash or mild acid wash on produce; or (iv) The treatment of raw foods with ionizing radiation not to exceed the maximum dose of 1 kiloGray in accordance with § 179.26 of this chapter.
- 方法论陈述：先跑一道纯语境闸门：「fresh」是否暗示食品未加工/未保存？不暗示（如 "fresh" 用于巴氏杀菌全脂奶，因消费者普遍知道牛奶几乎总经巴氏杀菌）→ 不受 (a) 约束，回到 FD&C Act 403(a) 一般误导规则；暗示（如用于已巴氏杀菌的意面酱）→ 进入 (a) 的硬定义：原料态、未冷冻、未受任何热处理或任何形式保藏。再查 (c)(1) 四项法定不排除事由（获批蜡/涂层、采后获批农药、温和氯/酸洗、≤1 kGy 辐照）与 (c)(2) 冷藏不排除。"fresh frozen"/"frozen fresh" 走 (b) 的独立定义（采收后快速冷冻，blanching 不排除）。判定要点：品牌名与感官修饰词同样受管，不能靠改成品牌名规避。
- 可回答的新问题："Fresh Taste" 用作饼干品牌名是否暗示未加工？经温和氯洗的鲜切果蔬还能标 fresh 吗？"fresh frozen" 里的 "quickly frozen" 由谁用何种设备举证（(b) 给了 blast-freezing 例）？
- 跨域佐证：〔§ 101.18(b)(c)〕品名与地理来源暗示的误导判定；〔§ 101.65(b)(5)〕以表征配料命名的品名默认不算 implied claim（但语境可回扣）；〔§ 101.22(i)〕characterizing flavor 的品牌名同样受管。
- 建议归属子卡：特定品类与警示

### CAND-FW-81: §101.100 配料表义务豁免「精确到 403 条款」的对象切分 ★
- 条款出处：〔§ 101.100(a)(1)(2)〕〔§ 101.100(b)(c)(g)(h)(i)〕 + pdf-page 335–340
- 原文引用（英文逐字，≤100 词/段）：
> (a) The following foods are exempt from compliance with the requirements of section 403(i)(2) of the act (requiring a declaration on the label of the common or usual name of each ingredient when the food is fabricated from two or more ingredients).
> (1) An assortment of different items of food, when variations in the items that make up different packages packed from such assortment normally occur in good packing practice and when such variations result in variations in the ingredients in different packages, with respect to any ingredient that is not common to all packages. Such exemption, however, shall be on the condition that the label shall bear, in conjunction with the names of such ingredients as are common to all packages, a statement (in terms that are as informative as practicable
> and that are not misleading) indicating by name other ingredients which may be present.
> (2) A food having been received in bulk containers at a retail establishment, if displayed to the purchaser with either: (i) The labeling of the bulk container plainly in view, provided ingredient information appears prominently and conspicuously in lettering of not less than one-fourth of an inch in height; or (ii) A counter card, sign, or other appropriate device bearing prominently and conspicuously, but in no case with lettering of less than one-fourth of an inch in height, the information required to be stated on the label pursuant to section 403(i)(2)
> (b) A food repackaged in a retail establishment is exempt from the following provisions of the act if the conditions specified are met. (1) Section 403(e)(1) of the act (requiring a statement on the label of the name and place of business of the manufacturer, packer, or distributor).
> (c) An open container (a container of rigid or semirigid construction, which is not closed by lid, wrapper, or otherwise other than by an uncolored transparent wrapper which does not obscure the contents) of a fresh fruit or fresh vegetable, the quantity of contents of which is not more than 1 dry quart, shall be exempt from the labeling requirements of sections 403(e), (g)(2) ... and (i)(1) of the act
- 方法论陈述：Subpart G 的第一句就把豁免对象钉死——免的是 **403(i)(2) 配料表义务**（且只针对「由两种以上配料制成」的食品），不是整个标签义务。(a) 四款按场景切：什锦组合装（仅对「非各包共有」的配料免，且须列出可能存在的其他配料）、零售店散装陈列（散装容器标签清晰可见或柜台卡 ≥1/4 in 字号）、incidental additives（见 FW-82）、亚硫酸盐（见 FW-82）。(b) 零售重新包装另免 403(e)(1)/403(g)(2)/403(i(1) 三条**指定**义务且各附条件；(c) ≤1 dry quart 的开放容器鲜果蔬免 403(e)/(g)(2)/(i)(1)；(g) 商业秘密 marker 须先向专员提交资料并取得「无害且准予豁免」的书面认定；(h)(i) 非均匀重量鱼片/香蕉在零售称重前免 403(e)(2) 且须在外箱标总净重、内包标 "To be weighed at or before time of sale"。**每款都精确指向某一 FD&C Act 条款号，不能串用。**
- 可回答的新问题：一款散装食品用柜台卡公示了配料表，是否也自动免 §101.9 营养标签？(b)(1) 免厂商名址后，§101.5 的义务是否还在？(g) 的「 harmless marker」认定与 §101.108 的书面批准是不是同一程序？
- 跨域佐证：〔§ 101.9(j)〕营养标签豁免（只免 §101.9）；〔§ 101.108〕临时实验豁免（只免 §§101.9/105.66 的特定要求）；〔§ 101.4(a)(1)〕配料表义务正文明确「except those ingredients exempted by § 101.100」；〔§ 101.100(d)〕州际再加工豁免另指向 403(c)(e)(g)(h)(i)(k)(q) 七款（见 FW-83）。
- 建议归属子卡：豁免与效力层

### CAND-FW-82: incidental additive「无技术/功能效果」前提 + 亚硫酸盐 10 ppm 独立判据 ★
- 条款出处：〔§ 101.100(a)(3)(4)〕 + pdf-page 336
- 原文引用（英文逐字，≤100 词/段）：
> (3) Incidental additives that are present in a food at insignificant levels and do not have any technical or functional effect in that food. For the purposes of this paragraph (a)(3), incidental additives are: (i) Substances that have no technical or functional effect but are present in a food by reason of having been incorporated into the food as an ingredient of another food, in which the substance did have a functional or technical effect.
> (ii) Processing aids, which are as follows: (a) Substances that are added to a food during the processing of such food but are removed in some manner from the food before it is packaged in its finished form. (b) Substances that are added to a food during processing, are converted into constituents normally present in the food, and do not significantly increase the amount of the constituents naturally found in the food. (c) Substances that are added to a food for their technical or functional effect in the processing but
> are present in the finished food at insignificant levels and do not have any technical or functional effect in that food.
> (4) For the purposes of paragraph (a)(3) of this section, any sulfiting agent (sulfur dioxide, sodium sulfite, sodium bisulfite, potassium bisulfite, sodium metabisulfite, and potassium metabisulfite) that has been added to any food or to any ingredient in any food and that has no technical effect in that food will be considered to be present in an insignificant amount only if no detectable amount of the agent is present in the finished food. A detectable amount of sulfiting agent is 10 parts per million (ppm or mg/kg) or more of the sulfite in the finished food.
- 方法论陈述：先立双重前提——「insignificant level」+「在该食品中无任何技术或功能效果」，缺一不可；再把 incidental additive 穷举为三类（(i) 随另一食品配料带入且在该食品中已无功能效果、(ii) 加工助剂 a/b/c 三亚类、(iii) 从设备/包装迁移且非 201(s) 食品添加剂或已按 409 规章使用）。最关键是 (4) 的独立判据：亚硫酸盐**不因落入 (a)(3) 就自动免申报**——即便无技术效果，仍须成品中「无可检出量」才算不显著，而「可检出」被定量定义为 **≥10 ppm**，且须用指定方法（LC-MS/MS 或 AOAC 990.28）判定。这是「一般豁免 + 特定物质另设可检出阈值」的双层闸门，10 ppm 与 §101.91 的 20 ppm、§101.60 的 5 calories 各属不同条款，不可混算。
- 可回答的新问题：某亚硫酸盐在成品中既有防腐功能又检出 5 ppm，能否援引 (a)(3) 免申报？(ii)(c) 的「加工中有效、成品中无效」由谁举证？10 ppm 阈值与 §101.17 各警示条款的触发条件是否共用？
- 跨域佐证：〔§ 101.4(h)(2)〕香料带入的 incidental additive 免申报须回到 §101.100(a)(3)；〔§ 101.91(a)(3)〕gluten-free 20 ppm 是另一独立阈值；〔§ 101.22(j)〕化学防腐剂须同时写通用名与功能描述（与免申报前提互补）；〔§ 101.100(j)〕检测方法并入材料。
- 建议归属子卡：豁免与效力层

### CAND-FW-83: 州际「再加工/异地贴标」豁免 + void ab initio 失效规则
- 条款出处：〔§ 101.100(d)(1)(2)〕〔§ 101.100(e)(1)(2)(3)〕〔§ 101.100(f)(h)(3)(i)(3)〕 + pdf-page 337–340
- 原文引用（英文逐字，≤100 词/段）：
> (d) Except as provided by paragraphs (e) and (f) of this section, a shipment or other delivery of a food which is, in accordance with the practice of the trade, to be processed, labeled, or repacked in substantial quantity at an establishment other than that where originally processed or packed, shall be exempt, during the time of introduction into and movement in interstate commerce and the time of holding in such establishment, from compliance with the labeling requirements of section 403 (c), (e), (g), (h), (i), (k), and (q) of
> the act if: (1) The person who introduced such shipment or delivery into interstate commerce is the operator of the establishment where such food is to be processed, labeled, or repacked; or
> (2) In case such person is not such operator, such shipment or delivery is made to such establishment under a written agreement, signed by and containing the post office addresses of such person and such operator, and containing such specifications for the processing, labeling, or repacking, as the case may be, of such food in such establishment as will ensure, if such specifications are followed, that such food will not be adulterated or misbranded within the meaning of the act upon completion of such processing, labeling, or repacking. Such person
> and such operator shall each keep a copy of such agreement until 2 years after the final shipment or delivery of such food from such establishment
> (1) An exemption of a shipment or other delivery of a food under paragraph (d) (1) or (3) of this section shall, at the beginning of the act of removing such shipment or delivery, or any part thereof, from such establishment become void ab initio if the food comprising such shipment, delivery, or part is adulterated or misbranded within the meaning of the act when so removed.
> (2) An exemption of a shipment or other delivery of a food under paragraph (d) (2) or (3) of this section shall become void ab initio with respect to the person who introduced such shipment or delivery into interstate commerce upon refusal by such person to make available for inspection a copy of the agreement, as required by paragraph (d) (2) or (3) of this section.
- 方法论陈述：这是一条「时间/空间限定 + 书面协议 + 追溯失效」的豁免链。前提：食品按行业惯例将在**原加工/包装以外的场所**大量再加工、贴标或重新包装；豁免只在「进入及在州际 commerce 中移动 + 在该场所持有期间」有效，且只免 403(c)(e)(g)(h)(i)(k)(q) 七款**列举**义务。满足前提后二选一：(d)(1) 引入州际 commerce 者本人就是该场所经营者；或 (d)(2) 双方签署含邮址与加工/贴标/重包规格的书面协议（规格须保证完成后不掺假、不错标），各留存至最后发运后 2 年备查。最关键的是 (e) 的 **void ab initio**：一旦移出该场所时食品已掺假/错标，或拒绝出示协议副本，豁免**自始无效**（不是自违规日起失效），把整段州际流通的合规责任追溯回来。(f) 把「加工」扩展到奶酪在 ≥35 °F 仓库熟成并附标签识别规则；(h)(3)/(i)(3) 则规定非均匀重量鱼片/香蕉若在零售时未正确标净重，即构成 held for sale 的错标行为。
- 可回答的新问题：协议留存满 2 年后销毁，若之后追溯检查发现当年错标，豁免是否已因 (e)(2) 早失效？(d)(1) 与 (d)(2) 的失效条件为何不同（(e)(1) 只覆盖 (1)/(3)）？(f) 的奶酪熟成为何也算「processed」？
- 跨域佐证：〔§ 101.17(g)(3)〕未处理果汁异地加工须在随附单据披露未处理（同场景、不同义务）；〔§ 101.9(j)(9)〕散装食品仅用于制造其他食品免营养标签；〔§ 101.100(a)(2)〕零售散装陈列豁免（同一「异地/陈列」家族但对象不同）。
- 建议归属子卡：豁免与效力层

### CAND-FW-84: 临时标签实验豁免「书面提案 9 项 + citizen petition + 书面批准」★
- 条款出处：〔§ 101.108(a)(b)(c)(d)〕 + pdf-page 340–341
- 原文引用（英文逐字，≤100 词/段）：
> (a) The food industry is encouraged to experiment voluntarily, under controlled conditions and in collaboration with the Food and Drug Administration, with and other formats for presenting nutrition and other related food labeling information that is consistent with the current quantitative system in §§ 101.9 and 105.66 of this chapter.
> (b) Any firm that intends to undertake a labeling experiment that requires exemptions from certain requirements of §§ 101.9 and 105.66 of this chapter should submit a written proposal containing a thorough discussion of each of the following information items that apply to the particular experiment: (1) A description of the labeling format to be tested; (2) A statement of the criteria to be used in the experiment for assigning foods to categories, e.g., nutrient or other values defining “low” and “reduced”; (3) A draft of the material to be
> used in the store ... (9) A statement of the sections of the regulations for which an exemption is sought.
> (c) The written proposal should be sent to the Dockets Management Staff ... The proposal should be clearly identified as a request for a temporary exemption for purposes of conducting authorized food labeling experiments and submitted as a citizen petition under § 10.30 of this chapter.
> (d) Approval for food labeling experiments will be given by FDA in writing. Foods labeled in violation of existing regulations will be subject to regulatory action unless an FDA-approved exemption to the specific regulation has been granted for that specific product.
- 方法论陈述：这是唯一一条「为做实验而临时免 §§101.9/105.66 特定要求」的通道，且是**事前书面批准制**。判定链：① 实验须在受控条件、与 FDA 协作下进行，且新格式不得脱离现行定量体系（§§101.9/105.66）；② 须提交书面提案，逐项讨论 (b)(1)–(9)：待测格式、分类判据（如 "low"/"reduced" 的定义值）、店内材料草案、起止日期与报告提交日及「不经批准不延期」承诺、地理区域、效果测量机制、实验期间如何向消费者传达被豁免的信息、声称所用营养数据的确定方法、**所求豁免的具体规章条款**；③ 提案按 §10.30 作为 citizen petition 提交并明确标识为临时实验豁免请求；④ FDA **书面**批准；⑤ 未获针对该具体规章、该具体产品的批准，标签违反现行规定者一律可被采取监管行动。
- 可回答的新问题：企业先上线实验再补提案是否可行？(b)(9)「写明所求豁免条款」是否意味着未点名的条款一律不免？(d) 的「for that specific product」能否让同一格式覆盖全线产品？本豁免与 §101.9(g)(9) 的「技术不可行书面请求」是同一通道吗？
- 跨域佐证：〔§ 101.2(f)〕小包装替代传播方式须按 part 10 请愿（同属「个案书面裁量」）；〔§ 101.9(g)(9)(g)(10)(v)(C)〕技术不可行/替代合规的书面请求与 §10.30 请愿；〔§ 101.12(h)〕RACC 修订请愿；〔§ 101.100(g)〕harmless marker 须取得专员书面认定。
- 建议归属子卡：豁免与效力层

### CAND-FW-85: 「豁免对象精确切分」元规则（§101.9(j) / §101.100 / §101.108 / Part 117）★
- 条款出处：〔§ 101.9(a)〕〔§ 101.100(a)〕〔§ 101.108(d)〕〔§ 101.100(d)〕 + pdf-page 20 / 335 / 337 / 341
- 原文引用（英文逐字，≤100 词/段）：
> Nutrition information relating to food shall be provided for all products intended for human consumption and offered for sale unless an exemption is provided for the product in paragraph (j) of this section.
> The following foods are exempt from compliance with the requirements of section 403(i)(2) of the act (requiring a declaration on the label of the common or usual name of each ingredient when the food is fabricated from two or more ingredients).
> Approval for food labeling experiments will be given by FDA in writing. Foods labeled in violation of existing regulations will be subject to regulatory action unless an FDA-approved exemption to the specific regulation has been granted for that specific product.
> shall be exempt, during the time of introduction into and movement in interstate commerce and the time of holding in such establishment, from compliance with the labeling requirements of section 403 (c), (e), (g), (h), (i), (k), and (q) of the act
- 方法论陈述：这是全书最易误用的一条元规则，用户点名的「豁免对象切分」。判定任何「我们能不能不标」的问题，第一步永远是问「**具体免的是哪一条义务**」：§101.9(j) 免的是**营养标签**（§101.9）；§101.100(a) 免的是 **FD&C Act 403(i)(2) 配料表**；§101.100(b)(c)(d)(h)(i) 各指向 403 的**指定条款**；§101.108 免的是经 FDA 书面批准的**临时实验**中 §§101.9/105.66 的**指定要求**；Part 117 的 qualified facility 等是**主体豁免**（免的是整套 PCHF 义务，不是标签义务）。四套互不通用：拿了 §101.9(j)(1) 小企业豁免不代表可免配料表，拿了 §101.100(a)(2) 散装陈列豁免不代表可免 §101.9 营养标签，§101.108 的实验豁免也不代表可免 §101.17 强制警示。第二步再问「该豁免的附带条件是否持续满足」——绝大多数都挂 FW-22 的「无声称/无营养信息」条件或书面协议/批准条件。
- 可回答的新问题：一个同时落入 §101.9(j)(1) 与 §101.100(a)(2) 的散装零售食品，标签上还剩哪些义务？Part 117 的 qualified facility 能否拿来免 §101.9 营养标签？§101.100 的配料表豁免能否与 §101.9(j)(13) 小包装豁免叠加成「什么都不标」？
- 跨域佐证：〔§ 101.9(j)(1)(13)(18)〕营养标签豁免各款及「无声称」持续条件；〔§ 101.100(a)(1)–(4)(b)(c)(g)〕配料表与指定 403 条款豁免；〔§ 101.108(d)〕实验豁免的书面批准与「specific regulation / specific product」限定；〔§ 101.4(a)(1)(f)〕配料表义务正文两处回指 §101.100；BOOK_OVERVIEW 第 5 节接口清单（Part 117 主体豁免 vs 标签义务豁免）。
- 建议归属子卡：豁免与效力层

### CAND-FW-86: 「扩张授权清单 / 减免法定义务只能经 FDA 请愿」程序家族 ★
- 条款出处：〔§ 101.70(a)〕〔§ 101.69(b)〕〔§ 101.12(h)〕〔§ 101.108(c)〕〔§ 101.2(f)〕〔§ 101.9(g)(10)(v)(C)〕 + pdf-page 290 / 283 / 197 / 341 / 5 / 56
- 原文引用（英文逐字，≤100 词/段）：
> Any interested person may petition the Food and Drug Administration (FDA) to issue a regulation regarding a health claim.
> (b) Petitions included in this section are: (1) Petitions for a new (heretofore unauthorized) nutrient content claim; (2) Petitions for a synonymous term ... and (3) Petitions for the use of an implied claim in a brand name.
> The Commissioner of Food and Drugs, either on his or her own initiative or in response to a petition submitted pursuant to part 10 of this chapter, may issue a proposal to establish or amend a reference amount in paragraph (b) of this section.
> The proposal should be clearly identified as a request for a temporary exemption for purposes of conducting authorized food labeling experiments and submitted as a citizen petition under § 10.30 of this chapter.
> A petition requesting such a regulation, as an amendment to this paragraph, shall be submitted under part 10 of this chapter.
> (C) Submit a petition, under 21 CFR 10.30, to request an alternative means of compliance.
- 方法论陈述：把散落全书、措辞同构的「请愿/书面请求」通道归为一个思维模型：凡要**扩张授权清单**（新健康声称 §101.70、新含量声称/同义词/品牌名 §101.69、新建 RACC 子类别 §101.12(h)）或**减免法定义务**（小包装替代传播 §101.2(f)、技术不可行替代合规 §101.9(g)(9)/(10)(v)(C)、临时标签实验 §101.108），企业都不得自行裁量，唯一入口是向 FDA 提交书面请愿/提案（多为 part 10 或 §10.30 citizen petition），由 FDA 通过规章或书面批准作个案裁量。共通结构：① 列明所求的具体条款/具体产品；② 附科学或事实依据（SSA、分析数据、完整样标、影响分析）；③ 附「代表性且平衡（含不利信息）」陈述与环境评估；④ 遵守法定时限与公开披露；⑤ 未获书面批准前，现行义务一律继续适用。区分「依职权」与「依请愿」两种启动方式，也区分「逾期视为否决」（§101.69(m)/§101.70(j)）与「逾期视为准予」（§101.69(o)(4)）两类例外。
- 可回答的新问题：企业能否用「行业惯例」替代请愿来启用一个新描述符？§101.12(h) 的 RACC 请愿与 §101.70 的健康声称请愿能否合并成一份材料？「逾期视为准予」只在品牌名请愿出现，是否可类推到其他请愿？
- 跨域佐证：〔§ 101.14(d)(1)〕/〔§ 101.14(e)(1)〕授权只能来自 Subpart E 规章；〔§ 101.13(b)(4)〕不误导的拼写变体是唯一无需请愿的例外；〔§ 101.9(g)(8)〕FDA 批准数据库须书面同意；〔§ 101.100(g)〕harmless marker 须专员书面认定。
- 建议归属子卡：豁免与效力层

### CAND-FW-87: butter 营养素含量声称「(a)(1)–(4) 四要件累积 + 80% milkfat 法定基准」闸门
- 条款出处：〔§ 101.67(a)(1)(2)(3)(4)〕〔§ 101.67(b)(c)(1)(2)〕 + pdf-page 283
- 原文引用（英文逐字，≤100 词/段）：
> Claims may be made to characterize the level of nutrients, including fat, in butter if: (1) The claim complies with the requirements of § 101.13 and with the requirements of the regulations in this subpart that define the particular nutrient content claim that is used and how it is to be presented. In determining whether a claim is appropriate, the calculation of the percent fat reduction in milkfat shall be based on the 80 percent milkfat requirement provided by the statutory standard for butter (21 U.S.C. 321a);
> (3) The product is not nutritionally inferior, as defined in § 101.3(e)(4), to butter as produced under 21 U.S.C. 321a; and (4) If the product would violate 21 U.S.C. 321a but for the nutrient content claim that characterizes the level of nutrients, that claim shall be an explicit claim that is included as part of the common or usual name of the product.
> Deviations from the ingredient provisions of 21 U.S.C. 321a must be the minimum necessary to achieve similar performance characteristics as butter as produced under 21 U.S.C. 321a, or the food will be deemed to be adulterated under section 402(b) of the act.
- 方法论陈述：这是「法定标准食品作减量声称」的专门闸门，四要件累积缺一不可。① (a)(1) 声称须同时合规 §101.13 通则与 Subpart D 对该词的逐词定义，且「乳脂减少百分比」必须以 21 U.S.C. 321a 的 **80% milkfat 法定标准**为分母，不得以产品自身实际乳脂为基准。② (a)(2) 配方闸：产品须含 cream/milk 或其成分（乳清、酪蛋白等），可加盐、色素、发酵剂及改善质构/防脱水/增味/延长货架期/改善外观/增甜的安全适用配料；可用水替代乳脂，但**水量须少于奶油/乳/乳成分量**。③ (a)(3) 营养不得低于按 321a 生产的黄油（回指 §101.3(e)(4) 的 nutritionally inferior 定义）。④ (a)(4) 若产品仅因该声称才不违反 321a，声称须为 explicit 且写进**通用或惯用名**本身，不能只印在旁边。再进 (b) 性能闸：偏离 321a 配料规定的幅度须为实现相似性能所必需的最小限度，否则按 402(b) 掺假；性能存在实质限制用途的显著差异时须加差异声明（符合 §101.13(d)），且产品须至少实质完成黄油的一项主要功能。最后 (c)：所有配料照章标示，改善性配料与替代乳脂的水须加星号并紧接同字号的 "*Ingredients not in regular butter" 声明。
- 可回答的新问题：某「低脂黄油」把乳脂降到 60%，"reduced fat" 的百分比该按 80% 还是按 60% 算？加水量超过乳成分量是否直接失格，还是仅影响 (a)(2) 一项？产品仅因 "light" 声称才不违反 321a 时，把该词放在品名旁的醒目方框是否算「included as part of the common or usual name」？(b) 的「至少一项主要功能」由谁用什么方法举证？
- 跨域佐证：〔§ 101.13〕含量声称通则与 (d) 差异声明规格；〔§ 101.3(e)(4)〕nutritionally inferior 的 2% 阈值定义（(a)(3) 的回指对象）；〔§ 101.62〕脂肪/脂肪酸含量声称逐词阈值；〔§ 101.4(a)(1)〕配料表义务（(c)(1) 的落点）。
- 建议归属子卡：声称闸门

### CAND-FW-88: §101.72–§101.83 已授权健康声称专条群「物质—疾病对 → 选专条」分流清单
- 条款出处：〔§ 101.72〕〔§ 101.73〕〔§ 101.74〕〔§ 101.75〕〔§ 101.76〕〔§ 101.77〕〔§ 101.78〕〔§ 101.79〕〔§ 101.80〕〔§ 101.81〕〔§ 101.82〕〔§ 101.83〕 + pdf-page 295–330
- 原文引用（英文逐字，≤100 词/段）：
> Among dietary factors, the strongest positive association has been found between total fat intake and risk of some types of cancer. Based on the totality of the publicly available scientific evidence, there is significant scientific agreement among experts, qualified by training and experience to evaluate such evidence, that diets high in total fat are associated with an increased cancer risk.
> Health claims not authorized for foods in conventional food form or for dietary supplements of vitamins, minerals, herbs, or other similar substances: (a) Dietary fiber and cardiovascular disease. (b) Zinc and immune function in the elderly.
- 方法论陈述：Subpart E 的 §101.72–83 不是可自由组合的词表，而是 12 条「物质/成分 → 疾病或健康状态」一一对应的授权专条，本候选把此前按模板归并（FW-76/FW-77）而未单列编号的 §101.73–81 显式钉入分流链。判定顺序：① 先查 §101.71 未授权负面清单（如 dietary fiber & CVD、zinc & immune function），落入即禁止；② 按拟声称的物质—疾病对锁定**唯一**专条（钙/骨质疏松 §101.72、膳食脂/癌 §101.73、钠/高血压 §101.74、膳食纤维/癌 §101.76、叶酸/神经管缺陷 §101.79、植物甾醇/心脏病 §101.83 等），**不得把甲专条的模型措辞借到乙物质**；③ 每条 (c)(1) 先声明「§101.14 全部要求须满足」，个别专条（如 §101.83）以 except 对被点名款项开例外（见 FW-77）；④ 再过该专条 (c)(2) 的 Nature of claim / substance / food eligible 定量门槛；⑤ 措辞取 (e) 段 model health claims 或等价表述。**BOOK_OVERVIEW 明确：§101.72–83 逐条模型措辞全文只作可检索条文保留，不逐条做能力卡**，故本候选只给分流规则；各专条的具体门槛、except 与模型句须按条款号回原条文核对，不可凭候选池照抄。
- 可回答的新问题：产品同时符合钙/骨质疏松与维生素 D/骨质疏松，能否在一条声称里合并两个专条？(e) 模型句改成同义但更顺口的表述是否仍算「等价」？§101.71 只列 2 项，是否意味着其他未列物质—疾病对自动授权？某专条 (c)(1) 写「All requirements set forth in § 101.14 shall be met」而无 except，能否援引 §101.83 的沙拉酱放宽？
- 跨域佐证：〔§ 101.14〕健康声称通用门与 (e) 六要件禁止；〔§ 101.70〕扩张授权清单只能经请愿；〔§ 101.71〕未授权负面清单（分流的入口闸门）；〔§ 101.83(c)(1)〕个别专条对 §101.14 的 except（FW-77 的例外样本）；〔§ 101.13(h)〕disclosure 语句规格。
- 建议归属子卡：声称闸门


