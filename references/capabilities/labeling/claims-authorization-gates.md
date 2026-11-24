> 本卡隶属 CAP-30 来源路由入口 references/capabilities/food-labeling-requirements.md；加载前先读该入口卡。

# 声称三层闸门与逐词授权（claims-authorization-gates）

*来源分层与定位：本卡落在 **21 CFR Part 101《Food Labeling》法规正文层**（eCFR 现行快照 `up to date as of 11/05/2026`，自述 authoritative but unofficial，联邦法规最终规则、具法律约束力），是 v4.18 增量并入的**第二十二类来源**、**第七套法规编号〔§ 101.xxx〕**，与既有六套〔§ 108 / 113 / 114 / 117 / 120 / 123.xxx〕并列，全包既有二十一类来源 + 本件 = **二十五类不可混引**。效力栈为**法规正文 ＞ 指南（should 建议层）＞ 检查程序 / 内部作业层**；本卡与 **Ed.5 guidance（Big 9 / allergen-free / advisory 声明）是不同法源**——Ed.5 属指南／`should` 建议层，Big 9 与 allergen-free、advisory 声明规则不在 Part 101 正文，绝不可写成〔§ 101.xxx〕。与 **Part 117 预防控制层分工**：〔§ 117.135(c)(2)〕只把「标签控制」作为过敏原预防控制来**管理**（确保标签内容正确、正确标签用到正确产品），Part 101 则规定标签**内容本身**该是什么；企业两套都要满足，条款号不得互引，且「标签合规」不等于「食品安全合规」（403 misbranding 与 402 adulteration 是两条独立执法钩子）。本卡判定对象是「某一句表述是不是 claim、落在哪套授权闸门、是否过负面门槛与正面授权」；**不判**标签载体与版式（PDP／信息面板／品名／配料表／净含量／显著性 → **V01**）、不判营养标签义务与 serving size↔§101.12 RACC 份量体系（→ **V02**）、不判 §101.17 各款强制警示与特定品类声明（→ **V04**）、不判 §101.100／§101.9(j)／§101.108 豁免对象切分与效力层元规则（→ **V05**）。*

## R — 原文

> "A claim that expressly or implicitly characterizes the level of a nutrient of the type required to be in nutrition labeling under § 101.9 or under § 101.36 (that is, a nutrient content claim) may not be made on the label or in labeling of foods unless the claim is made in accordance with this regulation and with the applicable regulations in subpart D of this part or in part 105 or part 107 of this chapter."
> —— 〔§ 101.13(b)〕[pdf-page 199]
> 中文自译：凡「明示或暗示」表征 §101.9／§101.36 要求标示营养素水平的表述（即营养素含量声称），一律不得出现在 label 或 labeling，除非依本规章及 Subpart D（或 part 105／107）的相应规则作出。总闸门是「默认禁止＋列举授权」，`expressly or implicitly` 并列，暗示与直说同等受管。

> "An implied nutrient content claim is any claim that: (i) Describes the food or an ingredient therein in a manner that suggests that a nutrient is absent or present in a certain amount (e.g., “high in oat bran”); or (ii) Suggests that a food, because of its nutrient content, may be useful in maintaining healthy dietary practices, where there is also implied or explicit information about the nutrition content of the food (e.g., “healthy”)."
> —— 〔§ 101.13(b)(2)〕[pdf-page 199]
> 中文自译：暗示型含量声称有两类——以描述食品／配料的方式暗示某营养素有无或达某量（如 `high in oat bran`）；或暗示因营养内容有助维持健康膳食、且伴随明示／暗示的营养信息（如 `healthy`）。判准是「语境是否暗示营养素水平」，不是措辞直白与否。

> "Except for claims regarding vitamins and minerals described in paragraph (q)(3) of this section, no nutrient content claims may be made on food intended specifically for use by infants and children less than 2 years of age unless the claim is specifically provided for in parts 101, 105, or 107 of this chapter."
> —— 〔§ 101.13(b)(3)〕[pdf-page 199]
> 中文自译：除 (q)(3) 的维生素／矿物质相对 RDI 百分比声明外，专供 2 岁以下婴幼儿的食品一律不得作营养素含量声称，除非 parts 101／105／107 有专门规定。这是硬禁区，不是「真实即可」能打通。

> "Information that is required or permitted by § 101.9 or § 101.36, as applicable, to be declared in nutrition labeling, and that appears as part of the nutrition label, is not a nutrient content claim and is not subject to the requirements of this section. If such information is declared elsewhere on the label or in labeling, it is a nutrient content claim and is subject to the requirements for nutrient content claims."
> —— 〔§ 101.13(c)〕[pdf-page 199]
> 中文自译：同一串营养素数字，作为 Nutrition Facts 的一部分出现时不是声称、不受 §101.13 约束；一旦移到 label／labeling 的其他任何位置（正面、广告、随附宣传单），立即构成含量声称。位置决定性质，与数字内容无关。

> "Health claim means any claim made on the label or in labeling of a food, including a dietary supplement, that expressly or by implication, including “third party” references, written statements (e.g., a brand name including a term such as “heart”), symbols (e.g., a heart symbol), or vignettes, characterizes the relationship of any substance to a disease or health-related condition."
> —— 〔§ 101.14(a)(1)〕[pdf-page 206]
> 中文自译：健康声称＝表征「某物质 ↔ 某疾病／健康相关状况」关系的任何表述，明示或暗示均可，并明文列举第三方引用、含 `heart` 字样的品牌名、心形符号、vignettes（图示）。判准是「是否表征物质—疾病关系」，不是是否出现法定模型措辞。

> "Disqualifying nutrient levels means the levels of total fat, saturated fat, cholesterol, or sodium in a food above which the food will be disqualified from making a health claim. These levels are 13.0 grams (g) of fat, 4.0 g of saturated fat, 60 milligrams (mg) of cholesterol, or 480 mg of sodium, per reference amount customarily consumed, per label serving size, and, only for foods with reference amounts customarily consumed of 30 g or less or 2 tablespoons or less, per 50 g."
> —— 〔§ 101.14(a)(4)〕[pdf-page 206]
> 中文自译：总脂／饱和脂／胆固醇／钠任一超过阈值，食品即**丧失**作任何健康声称的资格：13.0 g 脂、4.0 g 饱和脂、60 mg 胆固醇、480 mg 钠，按 per RACC、per label serving size，且仅对 RACC ≤30 g 或 ≤2 汤匙的食品加按 per 50 g。这是「先过负面门槛」，不是只满足正面条件。

> "FDA will promulgate regulations authorizing a health claim only when it determines, based on the totality of publicly available scientific evidence (including evidence from well-designed studies conducted in a manner which is consistent with generally recognized scientific procedures and principles), that there is significant scientific agreement, among experts qualified by scientific training and experience to evaluate such claims, that the claim is supported by such evidence."
> —— 〔§ 101.14(c)〕[pdf-page 207]
> 中文自译：FDA 仅在基于「全部公开可得科学证据的总体」认定合格科学专家间存在 significant scientific agreement（SSA，显著科学一致）支持该声称时，才制定授权法规。这是法规级证据门槛，不是「有论文／有 RCT 支持」，企业自判「有科学支持」无效。

> "Prohibited health claims. No expressed or implied health claim may be made on the label or in labeling for a food, regardless of whether the food is in conventional food form or dietary supplement form, unless: (1) The claim is specifically provided for in subpart E of this part; and (2) The claim conforms to all general provisions of this section as well as to all specific provisions in the appropriate section of subpart E of this part;"
> —— 〔§ 101.14(e)〕[pdf-page 209]
> 中文自译：任何明示或暗示健康声称（常规食品与膳食补充剂同标准）均不得作出，除非累积满足六要件，开头两条即「已由 Subpart E 明文授权」＋「符合本节通则与该专条全部规定」；其后还要求未超 disqualifying level、无不当物质水平、非婴幼儿食品、营养充足性门槛等，任一不满足即禁止。

> "Health claims not authorized for foods in conventional food form or for dietary supplements of vitamins, minerals, herbs, or other similar substances: (a) Dietary fiber and cardiovascular disease. (b) Zinc and immune function in the elderly."
> —— 〔§ 101.71〕[pdf-page 295]
> 中文自译：§101.71 是「未授权健康声称」负面清单，明文否决膳食纤维与心血管疾病、锌与老年人免疫功能等关系。但**清单不是授权清单**——未列入不等于可用；合法出口只有 Subpart E 已授权专条或 §101.70 请愿新授权。

> "Any interested person may petition the Food and Drug Administration (FDA) to issue a regulation regarding a health claim."
> —— 〔§ 101.70(a)〕[pdf-page 290]
> 中文自译：任何利害关系人可就健康声称向 FDA 请愿制定法规，这是把「未授权声称」变成「已授权」的唯一合法通道（A–F 六栏材料、SSA 摘要、100 天 filed／denied 等时限）。企业不得自创健康声称后「先上市再补请愿」。

> "(a) General requirements. Except as provided in paragraph (e) of this section, a claim about the level of a nutrient in a food in relation to the Reference Daily Intake (RDI)...may only be made on the label or in labeling of the food if: (1) The claim uses one of the terms defined in this section in accordance with the definition for that term"
> —— 〔§ 101.54(a)〕[pdf-page 247]
> 中文自译：Subpart D 每条逐词声称共用同一「通用门」：所用词必须是本节按定义的术语，且须符合 §101.13 通则、且食品已按 §101.9／§101.10／§101.36 完成营养标签。过完通用门才对号入座该词的定量阈值——「达到数值」只是其中一步。

> "The terms “calorie free,” “free of calories,” “no calories,” “zero calories,” “without calories,” “trivial source of calories,” “negligible source of calories,” or “dietarily insignificant source of calories” may be used on the label or in the labeling of foods, provided that: (i) The food contains less than 5 calories per reference amount customarily consumed and per labeled serving."
> —— 〔§ 101.60(b)(1)〕[pdf-page 253]
> 中文自译：`calorie free` 等八个同义词可用，前提是食品 per RACC 且 per labeled serving 均 **less than 5 calories**。这是 §101.60 的逐词门槛；`5 calories` 是声称资格线，与 §101.9(c)(1)「<5 cal 可标零」是不同判据，不可混算。

> "The terms “fat free,” “free of fat,” “no fat,” “zero fat,” “without fat,” “negligible source of fat,” or “dietarily insignificant source of fat”...may be used on the label or in labeling of foods, provided that: (i) The food contains less than 0.5 gram (g) of fat per reference amount customarily consumed and per labeled serving"
> —— 〔§ 101.62(b)(1)〕[pdf-page 260]
> 中文自译：`fat free` 等词可用，门槛是 per RACC 且 per labeled serving 脂肪 **less than 0.5 g**（meal／main dish 另有分档）。Subpart D 的 `free`／`low`／`reduced`／`light` 各有独立逐词阈值与分档，须逐词对号，不能只拿一个数值说合规。

> "A claim about the presence of an ingredient that is perceived to add value to the product, e.g., “made with real butter,” “made with whole fruit,” or “contains honey,”"
> —— 〔§ 101.65(b)(3)〕[pdf-page 273]
> 中文自译：§101.65(b) 的「一般不构成暗示声称」安全港之一：声明含某「被感知为增值」的配料（如 `made with real butter`），在中性语境下通常不是营养素含量声称——前提是上下文没有符号／vignette 暗示某营养素水平。

> "Claims about the food or an ingredient therein that suggest that a nutrient or an ingredient is absent or present in a certain amount (e.g., “high in oat bran”) are implied nutrient content claims and must comply with paragraph (a) of this section."
> —— 〔§ 101.65(c)(1)〕[pdf-page 273]
> 中文自译：与上块成对的反面：暗示某营养素／配料有无或达某量的表述（如 `high in oat bran`）**就是**暗示型含量声称，须过 §101.65(a) 三要件。同一「oat bran」话题，中性增值陈述与 `high in …` 暗示水平陈述结论相反，分水岭是语境。

> "Any unavoidable presence of gluten in the food bearing the claim in its labeling is below 20 ppm gluten (i.e., below 20 mg gluten per kg of food)."
> —— 〔§ 101.91(a)(3)〕[pdf-page 331]
> 中文自译：`gluten-free` 是 §101.91 的**定量定义**：不含特定含麸质谷物／成分，且任何不可避免的麸质存在低于 20 ppm（20 mg/kg）。`no gluten`／`free of gluten`／`without gluten` 同义受管，不符即 deemed misbranded。它不是「无添加」营销词。

> "A detectable amount of sulfiting agent is 10 parts per million (ppm or mg/kg) or more of the sulfite in the finished food."
> —— 〔§ 101.100(a)(4)〕[pdf-page 336]
> 中文自译：亚硫酸盐「可检出量」定义为成品中 ≥10 ppm，属 §101.100(a)(4) incidental additive 配料表豁免语境——≥10 ppm 即须申报。它与 §101.91 的 20 ppm 分属不同条款、不同物质、不同法律后果、不同检测方法，不得混算或换算。

> "This statement has not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease."
> —— 〔§ 101.93(c)〕[pdf-page 332]
> 中文自译：§101.93 给膳食补充剂 §403(r)(6) 结构／功能声明配的**法定免责声明**（单条用 `This statement`，多条用复数 `These statements`），换取不被当作药品的待遇；须紧邻声明或用星号链接、每个含该声明的面板／页面都有、粗体不小于 1/16 in，另首次上市 30 天内通知 FDA。它不是可选营销话术。

> "For example, the term “fresh” used to describe pasteurized whole milk is not subject to paragraph (a) of this section because the term does not imply that the food is unprocessed (consumers commonly understand that milk is nearly always pasteurized). However, the term “fresh” to describe pasta sauce that has been pasteurized or that contains pasteurized ingredients would be subject to paragraph (a) of this section because the term implies that the food is not processed or preserved."
> —— 〔§ 101.95〕[pdf-page 334]
> 中文自译：§101.95 的前置闸门是「用语是否暗示未加工／未保存」：巴氏杀菌全脂奶用 `fresh` 不暗示（消费者普遍知道牛奶几乎总经巴氏杀菌）→ 不受 (a) 约束；经巴氏杀菌的意面酱用 `fresh` 则暗示未加工 → 落入 (a) 的硬定义（原料态、未冷冻、未热处理／未保存）。品牌名与感官修饰词同样受管。

> "Adequate calcium throughout life, as part of a well-balanced diet, may reduce the risk of osteoporosis."
> —— 〔§ 101.72(e)〕[pdf-page 297]
> 中文自译：Subpart E 已授权专条给的是可照抄的**模型健康声称**（此处为钙／骨质疏松），因果强度限定为 `may reduce the risk`、须带 `as part of a well-balanced diet`。企业不能自改成 `prevents` 等更强或更顺口的同义句；须按「物质—疾病对」选唯一专条。

**本卡反直觉口径清单**（法规级校准，非聪明人常识）

1. 「暗示」与「明示」同等受管：品牌名、心形符号、vignette、第三方文献引用都可能构成 claim，不直说 `low fat` 也落闸（§101.13(b)(2)、§101.14(a)(1)）。
2. 同一串营养素数字放在 Nutrition Facts 内不是声称，移到 PDP／广告／随附宣传单立即变成声称（§101.13(c)，位置决定性质）。
3. SSA 是 FDA 基于「全部公开可得科学证据的总体」作出的法规级认定，不是「有论文／RCT 支持」；企业自判「有科学支持」不能替代 FDA 授权（§101.14(c)）。
4. §101.71「未授权清单」不是授权清单——不在清单上不等于可用；合法出口只有 Subpart E 已授权专条或 §101.70 请愿。
5. 健康声称资格是「先过负面门槛」：SSA 与 Subpart E 都满足，只要 disqualifying level 任一项超标即丧失资格（§101.14(a)(4)／(e)(3)）。
6. §101.91 的 20 ppm（gluten-free）与 §101.100(a)(4) 的 10 ppm（亚硫酸盐可检出）是不同条款、不同物质、不同后果、不同检测方法，不得混算；同理 5 cal／RACC、40% 圆柱面积、120 °F 各有法源。
7. gluten-free 是定量阈值定义（below 20 ppm），不是「无添加」营销词；不符者 `deemed misbranded` 是自执行后果，不是可协商的措辞瑕疵。
8. §101.9(j) 等营养标签豁免几乎都以「不作任何营养声称或营养信息」为存续条件——作声称的那一刻豁免即丧失，须补全套营养标签；「免的是标，不是说」。
9. Subpart D 逐词阈值（<5 cal／RACC、<0.5 g fat、`high` ≥20% RDI/DRV 等）是声称资格门槛，不是企业放行／内控标准；脱离 RACC 分母谈数值无意义。
10. `made with real butter`／`oat bran muffins` 在中性语境一般不算 implied claim，但 `high in oat bran`／`as much fiber as an apple` 算——分水岭是语境是否暗示营养素水平，而非出现哪个词。
11. 婴幼儿（<2 岁）食品除 (q)(3) 维矿物质百分比外一律不得作含量声称，健康声称侧亦禁——硬禁区，不是「有研究即可」能打通。
12. 用了 Subpart E 已授权模型措辞 ≠ 绕过 §101.14：各专条 (c)(1) 都回引「All requirements set forth in § 101.14 shall be met」，个别专条的 `except` 只对被点名款项与品类放宽，不可借到另一条。

## I — 自述

这套方法判的是「一句表述能不能说、凭什么说」，不是标签放哪里、份量怎么算。核心判定链是五步：先判「这是不是 claim（明示／暗示／品牌名／符号／第三方引用）」→ 再分「营养素含量声称／健康声称／描述性声称」→ 再过「负面门槛」→ 再过「正面授权」→ 最后套「模型措辞／定量条件」。顺序不可颠倒，任一步不过即止；把「有研究支持」「如实陈述」「本来免标」当成绕过任何一步的理由，都会判反。

第一道分流是「是不是 claim」。§101.13(b)(2) 与 §101.14(a)(1) 把 express 与 implied 并列，且后者明文列举第三方引用、含 `heart` 的品牌名、心形符号、vignettes。一个心形 logo 落在高纤谷物盒上就可能构成健康声称；把声称藏进品牌名也不是法外空间——§101.13(q)(7) 要求品牌名中的 implied claim 须经 FDA 授权、按 §101.69(o) 请愿。判定看的是整体沟通印象，不是有没有直白说出「低脂」「治癌」。

还要判「写在哪里」。§101.13(c)：同一营养素数字作为 Nutrition Facts 的一部分不是声称，移到其他任何位置即成为含量声称。这是纯位置分流，与内容无关；把 `0 g trans fat` 从营养标签搬到正面，等于主动开启整套 §101.13 与 Subpart D 义务，并顺带触发营养标签义务。合规判断不能只看「写了什么」，必须看「写在哪里」。

第二类分流是「哪一体系」。营养素含量声称表征的是「营养素水平」（§101.13／Subpart D）；健康声称表征的是「物质 ↔ 疾病／健康相关状况的关系」（§101.14／Subpart E），两套授权体系不可互套。此外 Subpart F 的 `gluten-free`（§101.91）、`fresh`（§101.95）、膳补结构／功能声明免责（§101.93）各自定义，既非含量声称也非健康声称，须各按专条判。暗示疾病预防／治疗的表述，合法出口只有 §101.14＋Subpart E（§101.9(k)），否则按 201(n)／403(a) 错标；必需营养素缺乏症（坏血病、糙皮病）被 §101.14(a)(5) 排除在 disease 定义外，是少数的反向出口。

SSA 是法规级证据门槛。§101.14(c) 与 §101.70 请愿的「Summary of scientific data」用几乎逐字相同的句式，要求基于「全部公开可得科学证据的总体」证明合格专家间存在 significant scientific agreement。它不是「有论文支持」，更不是企业自查结论；FDA 未据此在 Subpart E 制定授权法规前，任何「某成分降低某病风险」都不得使用。请愿端与授权端对称，说明门槛由 FDA 认定而非企业主张。

负面门槛先于正面条件。§101.14(a)(4) 的 disqualifying level 是「取消资格」阈值：总脂 13.0 g／饱和脂 4.0 g／胆固醇 60 mg／钠 480 mg（按 per RACC、per labeled serving，小 RACC 食品加 per 50 g），任一项超标即丧失作任何健康声称的资格；meal／main dish 按 §101.13(l)(m) 分类换用 26/8/120/960 与 19.5/6/90/720。§101.14(e) 把「Subpart E 已授权＋通则＋未超 disqualifying＋无不当物质水平＋非婴幼儿＋营养充足性（任何强化前 ≥10% RDI/DRV 的维 A/C、铁、钙、蛋白或纤维）」压成六要件累积，任一不满足即禁。第 ⑥ 项最易漏：它先设「营养充足」正面门槛，再叠加第 ③ 项的负面门槛。

§101.71 与 §101.70 是「未授权／授权」的两端。§101.71 以负面清单明文否决膳食纤维与心血管病、锌与老年人免疫功能等关系；但清单不是授权清单，未列入仍须回 §101.14 判断。把「未授权声称」变成「已授权」的唯一通道是 §101.70 请愿：A–F 六栏材料（物质适格性、SSA 科学摘要、分析数据、模型声称、文献与不利资料附件、环境评估），15 天收件、100 天 filed／denied、提案公布后 270 天最终规则。§101.69 另管营养素含量声称请愿（新描述符／同义词／品牌名暗示声称），两者同属「扩张授权清单只能经 FDA 请愿」的程序家族。

Subpart D 是「逐词授权」。§101.54／56／60／61／62／65／67／69 每条共用同一通用门：所用词须是本节按定义给出的术语、须符合 §101.13 通则、食品须已按 §101.9／§101.10／§101.36 标营养标签；过完三门才进入该词的定量阈值。例如 §101.60 的 `calorie free` 须 per RACC 且 per labeled serving 均 <5 calories；§101.62 的 `fat free` 须 <0.5 g fat，而 `low fat`／`reduced fat`／`light` 各有独立分档（相对声称还须配参照食品身份、差异百分比与定量对比）；§101.54 的 `high` 须 ≥20% RDI/DRV per RACC、`good source` 为 10–19%。阈值是「声称资格」不是企业放行标准，且所有比较都锚定 RACC／per labeled serving。

隐含声称的正负界线在 §101.65。`made with real butter`、`100 percent milk free`、`corn oil`、`oat bran muffins` 在中性语境一般不算 implied claim（(b) 款安全港），但 `high in oat bran`、`as much fiber as an apple` 算（(c) 款）；(c)(3) 还把「含燕麦麸」转译为 `good source of dietary fiber`、「只用植物油」转译为 `low saturated fat`、「不含油」转译为 `fat free`。分水岭永远是语境是否暗示营养素水平，安全港 (b)(5) 自己就写明「除非符号／vignette 等暗示某营养素有无」。

两个 ppm 不可混算。§101.91 的 `gluten-free` 是 below 20 ppm 的定量定义（成分排除＋不可避免残留两路），`no/free of/without gluten` 同义受管，不符即 `deemed misbranded`，发酵／水解食品无可用检测方法时改以记录证明（留存 ≥2 年）；§101.100(a)(4) 的 10 ppm 是亚硫酸盐在 incidental additive 配料表豁免语境下的「可检出」线，须用 LC-MS/MS 或 AOAC 990.28 测定。前者管「能不能标 gluten-free」，后者管「亚硫酸盐要不要进配料表」，物质、条款、后果、方法全不同。同理 §101.93 的免责声明是换取 §403(r)(6) 待遇的法定对价，§101.95 的 `fresh` 仅在暗示未加工／未保存时才受 (a) 硬定义约束（巴氏奶 vs 意面酱的二分），二者与含量／健康声称都不是同一套。

最后两处硬禁区与接口。§101.13(b)(3) 明文：除 (q)(3) 维矿物质百分比外，<2 岁婴幼儿食品不得作营养素含量声称；§101.14(e)(5) 对健康声称侧同样禁止。而作任何含量／健康声称都会反向触发营养标签义务（§101.13(n)／§101.14(d)(3)），并可能击穿 §101.9(j) 豁免——声称是「义务放大器」，不是「表达自由」。本卡到「表述能否作、落在哪条授权」为止，不下个案合规结论。

## A1 — 书中用法

**情景一：隐含声称正负对照——`made with real butter` 与 `high in oat bran`（cases.md CAND-CS-09；§101.65(b)(3)／(c)(1)／(c)(3)、§101.13(b)(2)）**
- 问题：某松饼标签同时印 `made with real butter`（配料卖点）与 `high in oat bran`（营养卖点），旁边还有一枚高纤图标。这两句是否都受 §101.13 全套义务约束？
- 动作：先按 §101.13(b)(2) 判「是不是 implied claim」，再查 §101.65(b) 安全港与 (c) 黑名单。`made with real butter` 属 (b)(3)「含被感知为增值的配料」的中性陈述，若上下文无符号／vignette 暗示某营养素水平，一般不算含量声称；`high in oat bran` 属 (c)(1) 明列的「暗示某营养素／配料达某量」，**就是** implied nutrient content claim，须过 §101.65(a) 三要件（用本节定义词、符合 §101.13 通则、已标营养标签），并按 (c)(3) 转译为 `good source of dietary fiber` 去核 §101.54 的 10–19% 阈值。那枚高纤图标还会把原本安全的 `made with real butter`／`oat bran muffins` 语境「回扣」成暗示，须一并审。
- 判定/后果：两句结论相反。正例不触发（前提：语境中性），负例触发全套声称闸门；若产品未做 Nutrition Facts 或纤维未达 good source，则该声称不得使用，硬印即构成未授权声称与 misbranding。这正是「暗示与明示同等受管」最易漏判的一类，也是 cases.md 特别标出的正负对照。

**情景二：健康声称「有研究支持但未获授权」（§101.14(c)／(e)、§101.71、§101.70、§101.83）**
- 问题：企业手上有 3 篇 RCT 显示「某植物甾醇有助降低冠心病风险」，想在标签写「临床证明降低心脏病风险」，并主张「有研究支持即可」。
- 动作：按五步链逐关判。① 是 claim：明示表征「物质 ↔ 疾病」关系，落 §101.14(a)(1) 健康声称。② 分类：健康声称体系，不是含量声称。③ 负面门槛：先核 §101.14(a)(4) disqualifying level 与 (e) 六要件。④ 正面授权：查 §101.71 未授权清单、再查 Subpart E 是否有对应专条与模型措辞；SSA 须由 FDA 基于「全部公开可得证据的总体」认定（§101.14(c)），企业 3 篇 RCT 不构成 SSA，更不构成授权。⑤ 模型措辞：即便 §101.83 已授权植物甾醇／心脏病关系，也须逐字用其模型句（带 `may reduce the risk of heart disease`、`as part of a diet low in saturated fat and cholesterol`、每份／每日剂量），不能写「临床证明」或改因果强度。
- 判定/后果：主张不成立。§101.14(e) 明写任何明示／暗示健康声称均禁，除非「Subpart E 明文授权」且符合通则与专条全部规定；「有研究支持」既不等于 SSA，也不等于授权。若该关系未获专条授权（或落在 §101.71 否决清单），唯一合法动作是走 §101.70 请愿，请愿获批前不得上市使用；擅自使用按 §101.9(k) 的「防治疾病」类 deemed misbranded 处置。

**情景三：已授权模型仍被 disqualifying level 拦下（§101.14(a)(4)／(e)(3)、§101.72(e)、§101.13(h)）**
- 问题：一款高钙汤品拟用 §101.72(e) 的钙／骨质疏松模型句，科学关系与模型措辞都合规，但每 labeled serving 钠 520 mg。
- 动作：先确认「是不是健康声称」「落在 §101.72 专条」，再**先过负面门槛**：§101.14(a)(4) 钠阈值 480 mg（per RACC／per labeled serving），520 mg 已超；§101.14(e)(3) 规定超 disqualifying level 即禁，除非 Subpart E 为该物质定了替代水平，或 FDA 特别认定该声称有助健康膳食且标签加 §101.13(h) disclosure 突显超标营养素。普通食品 13/4/60/480、meal 26/8/120/960、main dish 19.5/6/90/720 按 §101.13(l)(m) 分类取三套值。
- 判定/后果：模型措辞合规救不回资格——「先过负面门槛」意味着正面授权满足也不足。除非该产品能援引 §101.72 专条明文例外或 FDA 的 (e)(3) 认定并配 disclosure，否则该健康声称不得作。错判会把高钠产品放行到健康声称，是 §101.14 最典型的反向失守。

**情景四：`gluten-free`「无添加」误读与两个 ppm（§101.91(a)(3)／(b)／(c)、§101.100(a)(4)）**
- 问题：某酱油「未主动添加含麸质原料」，企业想标 `gluten-free`，并以「发酵产品检不出就不用测」为由不留记录；同时把配料表里亚硫酸盐 10 ppm 与麸质 20 ppm 合并算「污染物总量」。
- 动作：按 §101.91 独立判，不套 §101.65(b)(1) 过敏避免安全港、也不套 Ed.5 的 allergen-free。① `gluten-free` 是 below 20 ppm 的定量定义，`no/free of/without gluten` 同义受管，不符即 `deemed misbranded`（§101.91(b)）。② 发酵／水解食品无科学有效方法可检 20 ppm 时，§101.91(c) 要求企业留存记录证明发酵前合规、评估交叉接触、已采取防引入措施（≥2 年），「检不出」不等于「免举证」。③ 若配料表按 FALCPA 标 `Contains wheat` 又标 `gluten-free`，`wheat` 后须加星号并附 (b)(3) 的处理说明。④ §101.100(a)(4) 的 10 ppm 是亚硫酸盐配料表申报的可检出线，用 LC-MS/MS 或 AOAC 990.28 测，与 20 ppm 物质／条款／后果／方法全不同。
- 判定/后果：「无添加」不成立，「合并算 ppm」不成立。两个阈值各自独立判定、各自留证；漏做 20 ppm 验证或记录留存会同时失守 §101.91(b)(c)，并因把 guidance 层 allergen-free 规则写成〔§ 101.xxx〕而污染来源分层。

## A2 — 触发与执行

**语言信号（中英双写）**
- 中文：「这算不算声称」「暗示算不算」「品牌名能不能用」「心形符号／第三方引用」「低脂／高纤／healthy」「有助健康」「降低某病风险」「有研究支持能不能写」「SSA」「disqualifying level」「未授权清单」「怎么申请新声称」「gluten-free 是不是没加就行」「20 ppm」「亚硫酸盐 10 ppm」「免标能不能写低脂」「婴幼儿能不能标高钙」「fresh 巴氏奶」「light／lite／95% fat free」「calorie free 门槛」「免责声明」「帮我把这句改顺口」
- English: "nutrient content claim", "expressed or implied claim", "health claim", "significant scientific agreement / SSA", "disqualifying nutrient levels", "subpart E authorized", "model health claim", "not authorized list", "petition", "third party references", "heart symbol / vignettes", "gluten-free / below 20 ppm", "detectable amount of sulfiting agent / 10 ppm", "structure/function statement", "disclaimer", "fresh / fresh frozen", "calorie free / less than 5 calories", "fat free / less than 0.5 g", "light / lite / percent fat free", "brand name implied claim", "deemed misbranded"

**与相邻能力的区分（differentiator）**
- 本卡判定对象是**一句表述的声称资格与授权归属**，产物是「是否 claim → 三类分流 → 负面门槛 → 正面授权 → 模型措辞／定量条件」；不判标签载体与版式 → **V01**、不判营养标签义务与份量／RACC → **V02**、不判 §101.17 强制警示与特定品类声明 → **V04**、不判豁免对象切分与效力层元规则 → **V05**。
- 与 **V01（标签基础架构）**：PDP／信息面板／品名／配料表／显著性是「信息放哪里、写多大多清楚」；本卡不管版式，只管「这句话能不能说」。把 `0 g fat` 印到正面既涉及 V01 的显著性落位，也因 §101.13(c) 触发本卡——版式归 V01、声称资格归本卡，不互相替代。
- 与 **V02（营养标签与份量）**：§101.12 RACC、serving size、§101.9(j) 豁免清单是份量体系；本卡反复引用 RACC 作声称阈值分母，但「分母取多少、表值怎么查」归 V02，本卡只判「过没过门槛」。
- 与 **V04（特定品类与强制警示）**：§101.17 各款 WARNING／NOTICE、§101.22／§101.30 是风险场景逐款立法；§101.93 免责声明、§101.95 `fresh` 在部分候选池里被归到 V04，但它们是「描述性声称各自定义」，归本卡；V04 只接强制警示与品类声明，两者不混引。
- 与 **V05（豁免与效力层）**：§101.100／§101.9(j)／§101.108 免的是**哪一条义务**、§101.108 书面批准、二十五类不可混引的元规则归 V05；本卡只在「免标是否等于可随意作声称」这一后果侧提示豁免失效，不下位阶与豁免对象结论。
- 与 **allergen-program CAP-05**：Ed.5 的 allergen-free 与 advisory 声明互斥属 **guidance 层**，Part 117〔§ 117.135(c)(2)〕只给「标签控制」管理义务，二者都不在 Part 101 正文；本卡只保留法规正文层的 `gluten-free`（§101.91），不得把 Ed.5 规则写成〔§ 101.xxx〕。
- 与 **cgmp-compliance-guide CAP-14**：效力栈（法规正文 ＞ 指南 ＞ 检查程序）与第七套编号登记归 CAP-14；本卡引用其结论但不判位阶。
- 与 **defect-action-levels CAP-15**：402(a)(3) 掺假裁量阈值不是声称资格，403 misbranding 与 402 adulteration 是两条执法钩子；「缺陷阈值能否当标签合规结论」交 CAP-15，本卡不接。
- 与 **regulatory-boundaries CAP-09**：Part 117 qualified facility 等**主体豁免**与 §101.100／§101.9(j) 的**标签义务豁免**不同制度，不在本卡判定范围。

**触发 → 动作／分流（≥20 条）**

1. 用户问「包装上印 `healthy`／`high in oat bran` 算不算声称」→ 按 §101.13(b)(2) 判 implied claim，再查 §101.65(b) 安全港与 (c) 黑名单，落本卡 Step 1；不转 V01。
2. 「品牌名叫 `Heart Healthy`／`Light` 要不要紧」→ §101.13(q)(7)（品牌名 implied claim 须 FDA 授权、按 §101.69(o) 请愿）＋§101.14(a)(1)（含 `heart` 品牌名可构成健康声称）；不转 V01 的品名版式判定。
3. 「放个心形符号／引用一篇第三方论文算不算」→ §101.14(a)(1) 明文算 health claim；若用了图形，还须按 §101.14(d)(2)(iv) 让完整声称或转介声明紧邻该图形。
4. 「把 Nutrition Facts 里的 `0 g fat` 印到正面大字」→ §101.13(c) 位置分流：移出营养标签即成为含量声称，转本卡 Subpart D 逐词门槛；同时提示会触发营养标签义务（§101.13(n)）。
5. 「我们产品本来免营养标签，能不能写 `low fat`」→ 本卡判声称资格；同时提示 §101.9(j) 豁免以「不作任何营养声称」为存续条件，作声称即丧失豁免 → 豁免对象切分交 V05。
6. 「有 3 篇 RCT，能不能写降低某病风险」→ §101.14(c) SSA 是法规级门槛而非「有论文」；查 §101.71 负面清单与 Subpart E 授权，未授权只能走 §101.70 请愿。
7. 「这句健康声称 Subpart E 有模型句，能不能改顺口点」→ 按「物质—疾病对」选唯一专条，逐字用 (e) 模型措辞或等价表述，不得把 `may reduce the risk` 改成 `prevents`；本卡不逐条展开 §101.72–83 全文。
8. 「钙／骨质疏松声称，钠 520 mg 行不行」→ 先过 §101.14(a)(4) disqualifying level（480 mg），再核 (e)(3) 例外与 §101.13(h) disclosure；顺序是先负面后正面。
9. 「怎么申请一个新的健康声称」→ §101.70 请愿 A–F 六栏与 100 天／270 天时限；含量声称新词／同义词／品牌名走 §101.69 三分流。
10. 「§101.71 没列这个组合，是不是就能用」→ 纠偏：负面清单不是授权清单，仍须回 §101.14 与 Subpart E 判断。
11. 「`gluten-free` 是不是没加麸质原料就行」→ §101.91 below 20 ppm 定量定义＋(b) deemed misbranded＋(c) 发酵／水解记录；不套 §101.65(b) 安全港、不套 Ed.5 allergen-free。
12. 「20 ppm 和亚硫酸盐 10 ppm 能不能一起算」→ 纠偏：§101.91 与 §101.100(a)(4) 不同条款不同判据，分开登记、各自留证，不得写成同一个〔§ 101.xxx〕。
13. 「标了 `Contains wheat` 还能写 gluten-free 吗」→ §101.91(b)(3) 星号＋「小麦经处理符合 FDA gluten-free 要求」说明；配料表版式本体归 V01。
14. 「膳补写 `支持免疫健康` 要不要加免责声明」→ §101.93 structure/function 声明 ↔ disease claim 二分；合法支须附固定 disclaimer、30 天通知 FDA；落入 disease claim 即按药品监管，除非是已授权健康声称。
15. 「巴氏奶写 `fresh` 合法，意面酱为什么不行」→ §101.95 前置「是否暗示未加工／未保存」闸门＋(c) 四项不排除事由；品牌名与感官修饰词同样受管。
16. 「`light`／`lite`／`95% fat free` 如实写行不行」→ Subpart D 逐词授权：§101.60(e)／(b)(4) 与 §101.13(i)(4)（`percent fat free` 须按 §101.62(b)(6)）；「真实即可」不成立。
17. 「`calorie free` 门槛多少」→ §101.60(b)(1) <5 cal per RACC 且 per labeled serving；提醒与 §101.9(c)(1)「<5 cal 可标零」不同判据，份量分母归 V02。
18. 「`fat free`／`low fat`／`reduced fat` 各差多少」→ §101.62 逐词分档（<0.5 g、≤3 g、≥25% 减脂等）＋§101.13(j) relative claim 参照食品；阈值为声称资格而非企业放行标准。
19. 「婴幼儿辅食标 `强化钙`／`高纤`」→ §101.13(b)(3) 与 §101.14(e)(5) 硬禁区（除 (q)(3) 维矿物质百分比外不得作），直接判停。
20. 「问一下 RACC 表数值／Table 2 某类别」→ 不在本卡：§101.12 表值与 Appendix 图形、9 个纯图形页不可逐字引，回原表核对 → V02。
21. 「Big 9／allergen-free／advisory 声明是不是 §101.xxx」→ 纠偏：Ed.5 guidance 与法规正文不同法源，不得写成〔§ 101.xxx〕；`allergen-program` **CAP-05**（Ed.5 的 allergen-free 与 advisory 声明互斥属 guidance 层）与 Part 117〔§ 117.135(c)(2)〕标签控制管理义务在此分流，本卡只保留法规正文层。
22. 「这套标签义务在效力栈里排第几／402(a)(3) 阈值能不能当声称资格」→ `cgmp-compliance-guide` **CAP-14** 管效力栈与第七套编号，本卡不判位阶；`defect-action-levels` **CAP-15** 的 402(a)(3) 掺假裁量阈值不是声称资格，403 misbranding 与 402 adulteration 是两条钩子 → 交 CAP-14／CAP-15。
23. 「标签合规是不是就等于食品安全合规」→ 纠偏红线：Part 101 是信息合规，Part 117／402 是危害与工艺合规；本卡不下安全结论（见 B 段）。
24. 「帮我写一句合规的标签文案／出个合规结论」→ 判停：不代写文案、不出个案合规结论，只给判定链与条款落点（见 B 段）。

## E — 边界与误读

1. **以为暗示／品牌名／符号不算 claim**：§101.13(b) 明写 `expressly or implicitly`，§101.13(b)(2) 把 `high in oat bran`／`healthy` 列为 implied claim，§101.14(a)(1) 把第三方引用、含 `heart` 的品牌名、心形符号、vignettes 逐项算作健康声称，§101.13(q)(7) 还要求品牌名中的 implied claim 须 FDA 授权。整条闸门被绕过是最易漏判的一类。
2. **以为有研究即可作健康声称**：健康声称是「负面清单＋正面授权」双闸。§101.14(c) 的 SSA 是 FDA 基于「全部公开可得科学证据」的法规级认定，不是「有论文」；§101.14(e) 六要件累积（Subpart E 授权、通则与专条、未超 disqualifying、无不当物质水平、非婴幼儿、营养充足性），§101.71 还明文否决膳食纤维与心血管病、锌与老年人免疫功能。有研究不可用，未授权不可用。
3. **以为 gluten-free 是「无添加」**：§101.91(a)(3) 给的是 below 20 ppm 的定量定义（不含特定谷物／成分＋不可避免残留两路），§101.91(b) 明写不符即 `deemed misbranded`（自执行后果，不是措辞瑕疵），§101.91(c) 对发酵／水解食品要求记录举证。「没主动加含麸质原料」不等于合规，「标了不达标只是措辞问题」更是错判。
4. **把 20 ppm 与亚硫酸盐 10 ppm 混算**：§101.91 的 20 ppm 管「能不能标 gluten-free」（麸质、声称资格、deemed misbranded、可检 20 ppm 的科学有效方法）；§101.100(a)(4) 的 10 ppm 管「亚硫酸盐要不要进配料表」（incidental additive 豁免、LC-MS/MS 或 AOAC 990.28）。物质、条款、后果、方法全不同，「都是 ppm、都约 10–20」不构成互相援引或换算依据。
5. **把 Ed.5 的 advisory 声明规则写成〔§ 101.xxx〕**：本包〔§ 101.xxx〕是第七套独立编号、法规正文层；Ed.5 guidance 属指南／`should` 建议层，Big 9、allergen-free 与 advisory 声明互斥规则不在 Part 101 正文。把它们贴成法条号会污染 CAP-14 的效力栈、CAP-05 的过敏原控制取证依据与 CAP-30 的来源路由。
6. **以为免标即可随意作声称**：§101.9(j) 的营养标签豁免几乎都以「bears no nutrition claims or other nutrition information」为存续条件，作声称的那一刻豁免即丧失、须回全套 §101.9／§101.10／§101.11；§101.9(k) 还规定即便按本节标注，暗示防治疾病仍 deemed misbranded，疾病关系信息只能依 §101.14＋Subpart E 提供。免的是「标」，不是「说」。
7. **把 Subpart D 阈值当企业放行标准**：<5 cal／RACC、<0.5 g fat、`high` ≥20% RDI/DRV 等是「声称资格门槛」，不是内控限值、不是危害分析输入、不是工艺参数；所有比较锚定 §101.12 RACC／per labeled serving，脱离分母谈「13 g 脂肪」「减少 50%」无意义。§101.12 表值本身属不可逐字引用区。
8. **以为 §101.71 未列即获授权**：§101.71 是「claims not authorized」负面清单，不是授权清单；未列入仍须满足 §101.14 适格性、SSA、disqualifying levels，且通常须有 Subpart E 授权法规或经 §101.70 请愿新授权。
9. **以为 Subpart E 已授权即绕过 §101.14**：§101.72–83 各专条 (c)(1) 都回引「All requirements set forth in § 101.14 shall be met」；少数条款（如 §101.83 对沙拉酱／涂抹酱）以 `except` 对被点名款项开例外，但只对被点名款项与品类放宽，未被点名的要件仍全部适用，且不可把某条的除外借到另一条。
10. **以为 heart 符号／第三方引用不必配完整声称**：§101.14(a)(1) 已把符号／vignette／第三方引用本身算作健康声称，§101.14(d)(2)(iv) 进一步要求完整声称或转介声明须紧邻该图形、所有信息集中一处无插入材料。不能「符号吸睛、完整声称藏附页」。
11. **以为婴幼儿食品可作含量／健康声称**：§101.13(b)(3) 除 (q)(3) 维矿物质百分比外一律禁止，§101.14(e)(5) 对健康声称侧同样禁止「代表或意味供 <2 岁婴幼儿」，除非 Subpart E 专门授权。这是硬禁区，不是「真实即可」「有研究即可」能打通的。
12. **以为 `fresh` 巴氏奶与意面酱同判、或以为不受 §101.95 管即无风险**：§101.95 的触发是「用语是否 suggest or imply 未加工／未保存」，品牌名与感官修饰词同样受管；不受本条约束的用法仍受 FD&C Act §403(a) 一般误导规则管辖。
13. **以为 `light`／`lite`／`percent fat free` 真实即可用**：§101.60(e) 限制 `light/lite` 须减脂 50%（或热量减 1/3、钠减 50%），§101.60(b)(4) 禁止参照食品已属 low fat／low calorie 时作 light 声称，§101.13(i)(4) 明写 `Percent fat free` 不归该款、须按 §101.62(b)(6)。逐词描述符不是「真实即可」，真实但未定义／未授权同样构成未授权声称。

## B — 判停

1. **不代写标签文案、不出个案合规结论、不预测个案结果**：本卡只给「是否 claim → 三类分流 → 负面门槛 → 正面授权 → 模型措辞／定量条件」的判定链与条款落点；任何「这句能不能印、这个产品合不合规」的最终结论都须回现行条文与个案事实复核。
2. **不逐条展开 §101.72–83 全部 12 类已授权健康声称模型措辞全文**：保留为可检索条文，按「物质—疾病对」锁定**唯一**专条后回原条文核 (c) 门槛、(c)(1) 的 `except` 与 (e) 模型句；不得把甲专条的模型措辞借到乙物质，不得把「科学上等价但更顺口」的自创句当作已授权。
3. **§101.12 表值、Appendix 图形、9 个纯图形页不可逐字引**：Table 1（婴幼儿／幼儿）／Table 2（一般食品）共约 113 页为流式列值，Appendix B/C/D 的 Nutrition Facts 为图形版式，转换件文本层失真；只保留「产品类别 → RACC → label statement」对应关系，回原表核对，不得逐字引表格数值或版式。
4. **eCFR 快照、定量阈值须复核 FR citation**：本件是 `up to date as of 11/05/2026` 现行快照，自述 authoritative but unofficial，与 4-1-25 Edition 年度编纂版／GPO 正式文本排版与条款编号可能不同；20 ppm、10 ppm、13/4/60/480 及分档、<5 cal、<0.5 g、§101.12 RACC 表值与 DV 值属持续修订对象，条文末尾 FR citation 从 42 FR 14308（1977）延至 88 FR 17718（2023），引用具体数值须复核快照日期与 FR citation，不得当作稳定规则。
5. **「转引未收」，不得当作本卡可引原文**：FD&C Act §403(r)（含 403(r)(6)、403(q)、403(w) FALCPA 过敏原定义）、§104.20 强化政策、21 CFR part 102 通用名、part 130 标准身份、part 105／105.66、§170.3(o)、§179.26、§25.30／25.32／25.40、§10.30 citizen petition、AOAC／检测方法正文、1 CFR part 51 并入材料、请愿表格栏目与联系地址一律「需查原件／转引未收」，本卡只标注不补写其内容。
6. **全包二十五类不可混引**：〔§ 101.xxx〕是第七套法规编号，与 Part 117 预防控制〔§ 117.xxx〕、Part 120〔§ 120.24〕5-log 工艺、IOM／CP 检查程序、Ed.5 guidance、SECG、CPG 各自分层；尤其不得把 Ed.5 的 Big 9／allergen-free／advisory 声明规则贴成〔§ 101.xxx〕，也不得把 Part 117〔§ 117.135(c)(2)〕的「标签控制」管理义务与 Part 101 标签内容义务互引条款号替换。
7. **数值型阈值散落且各有法源，不可混算**：20 ppm（gluten-free，§101.91）、10 ppm（亚硫酸盐可检出，§101.100(a)(4)）、5 calories／RACC（§101.60）、13/4/60/480 及 meal 26/8/120/960、main dish 19.5/6/90/720（§101.14(a)(4)）、40%（§101.1 圆柱 PDP 面积）、120 °F（§101.17(a) 自加压容器）、1 kGy（§101.95(c)(1)(iv) 辐照）、5-log（§101.17(g)(7) 工艺）——各自条款、各自判据、各自检测方法。
8. **本卡不判**：标签载体与版式（PDP／信息面板／品名／配料表／净含量／显著性／misbranding 总纲）→ **V01**；营养标签义务与 (j) 豁免、serving size↔§101.12 RACC、§101.36 膳补标签、§101.11 菜单标签 → **V02**；§101.17 各款强制警示、§101.22／§101.30 特定品类与声明（含 §101.17(g) 与 Part 120 的接口）→ **V04**；§101.100／§101.9(j)／§101.108 豁免对象切分与「豁免对象不可互替」→ **V05**。
9. **与既有 CAP 的分流边界**：`allergen-program` **CAP-05**（Ed.5 的 allergen-free 与 advisory 声明互斥属 guidance 层，Part 117〔§ 117.135(c)(2)〕只给标签控制管理义务）、`cgmp-compliance-guide` **CAP-14**（效力栈与第七套编号登记）、`defect-action-levels` **CAP-15**（402(a)(3) 掺假裁量阈值不是声称资格）、`regulatory-boundaries` **CAP-09**（主体豁免与标签义务豁免不同制度），均不在本卡判定范围，不得因「过敏原」「合规」「阈值」字样抢路由。
10. **「标签合规 ≠ 食品安全合规」红线**：Part 101 是信息合规（403 misbranding），产品危害／工艺／掺假属 Part 117／402（adulteration）；一张完全合规的 Nutrition Facts 完全可能伴随高危产品。本卡任何结论不得被读成安全合规结论——这是 BOOK_OVERVIEW §3 最强反对意见写进每张 labeling 子卡的边界。
11. **不提供检测方案、不替企业举证、不计算个案数值**：涉及具体产品定量检测、营养数据库、配方与加工史举证、检测方法选择、请愿材料填写、个案标签版面设计，一律「回原条文／回原表／需查原件」；本卡只判定口径，不承担举证与计算。
12. **本卡到此为止**：到「这句表述能否作、落在哪条授权、须过哪些门槛」为止；不判产品是否可采／是否放行，不下法律位阶与可主张性结论，不展开危害分析、供应商批准、验证活动或记录保存（包内既有 PCHF 类 CAP），不代写正式法律文书。
