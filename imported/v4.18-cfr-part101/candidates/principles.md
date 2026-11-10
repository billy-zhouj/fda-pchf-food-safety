# 候选池：原则提取器 | 来源 21 CFR Part 101 eCFR 2026-11-05 | 全量扫描 chunk-01..09

> 扫描完整性：chunk-01..09 共 9 块全部覆盖（50 条款）。chunk-04（§ 101.12 RACC 表，6100 行 / 440KB）按约定仅读开头 150 行与结尾 60 行，不逐行读取表格数值；§ 101.12 Table 1/2 数值、Appendix B/C/D 图形、9 个纯图形页（44/45/51/239/240/344/347/348/351）为不可逐字引用区，未作为引用来源。所有 `>` 引用均为 `source-cfr-part101-2026.md` 中的英文原文、归一化空白后可逐字命中，单段 ≤100 词。本文件只含候选池，不做去重、不做三重验证、不写能力卡。

---

### CAND-PR-01: 「label 或 labeling」是并列作用域，labeling 覆盖标签之外的一切随附表述
- 条款出处：〔§ 101.13〕〔§ 101.4〕〔§ 101.9〕〔§ 101.18〕〔§ 101.30〕〔§ 101.95〕+ pdf-page 199 / 7 / 20 / 219 / 224 / 334
- 原文引用（英文逐字，≤100 词/段）：
> A claim that expressly or implicitly characterizes the level of a nutrient of the type required to be in nutrition labeling under § 101.9 or under § 101.36 (that is, a nutrient content claim) may not be made on the label or in labeling of foods unless the claim is made in accordance with this regulation and with the applicable regulations in subpart D of this part or in part 105 or part 107 of this chapter.
> Ingredients required to be declared on the label or labeling of a food, including foods that comply with standards of identity, except those ingredients exempted by § 101.100, shall be listed by common or usual name in descending order of predominance by weight
- 原则陈述：Part 101 几乎不用孤立的 `label`，而是反复使用 `label or in labeling` / `on the label or in labeling` / `label or labeling` 这一并列结构，说明义务载体是「贴附标签 + 随附的全部文字、图形、宣传物」两层，而非仅贴在容器上的那一面。因此把声称或强制信息搬到随附说明书、货架卡、广告、品牌名、心形符号或水果图示上，并不使其脱离管辖。反之，法规若只写 `on the label`（部分位置条款），该条才仅限标签本身。判断某义务是否适用于某载体，必须先读出该条用的是 `label` 还是 `label or labeling`，不得默认二者等价；例外是 § 101.15(c) 立法者有意把 `label` 与 `other article of labeling` 分开设定义务，属刻意的载体分层。
- 复现位置：§ 101.9(a)(3)「on the label or in the labeling or advertising」（pdf-page 21）；§ 101.13(c)「elsewhere on the label or in labeling」（pdf-page 199）；§ 101.14(a)(1)「on the label or in labeling of a food」（pdf-page 206）；§ 101.18(a)(b)(c)「in the labeling of a food」（pdf-page 219）；§ 101.30(a)「the product's advertising, label, or labeling」（pdf-page 224）；§ 101.95「on the label or in labeling」（pdf-page 334）。≥2 处，为全书最高频复现。
- 可回答的新问题：把「低脂」印在随附宣传册而不印在瓶身是否仍构成受管声称？品牌名中的「heart」字样、心形符号是否落入健康声称管辖？某条写 `on the label` 时能否只放标签而忽略随附材料？
- 建议归属子卡：基础架构

### CAND-PR-02: PDP 由「最可能被陈列」定义，且必须足够大以容纳全部强制信息
- 条款出处：〔§ 101.1〕〔§ 101.2〕〔§ 101.3〕〔§ 101.7〕+ pdf-page 3 / 3 / 5 / 12
- 原文引用（英文逐字，≤100 词/段）：
> The term principal display panel as it applies to food in package form and as used in this part, means the part of a label that is most likely to be displayed, presented, shown, or examined under customary conditions of display for retail sale. The principal display panel shall be large enough to accommodate all the mandatory label information required to be placed thereon by this part with clarity and conspicuousness and without obscuring design, vignettes, or crowding.
- 原则陈述：主展示面（PDP）的法定判据是「惯常零售陈列条件下最可能被展示/呈现/观看/检视」，是行为判据而非视觉上「正面」的直觉，厂商不得自由指定。PDP 本身负有容纳义务：必须足够大，能清晰、显著、不被图案/装饰/拥挤遮挡地放下本 part 要求置于其上的全部强制信息。面积按矩形高×宽、圆柱或近圆柱容器高度×周长的 40%、其他形状总表面积的 40% 计算；圆柱容器的强制信息必须落在这 40% 内。有备选主展示面时，强制信息须逐面重复。例外：容器呈现明显主展示面（如三角/圆形干酪顶面）时，面积取整个顶面。
- 复现位置：§ 101.2 以 PDP 为基准定义信息面板方位（pdf-page 3）；§ 101.3(a)(d) 品名须作为 PDP 主要特征并以粗体、平行基线呈现（pdf-page 5）；§ 101.7(a) 净含量须置于 PDP 且备选面重复（pdf-page 12）；§ 101.15(a) 把「未出现在惯常购买条件下呈现的面板」列为显著性不足事由（pdf-page 210）；§ 101.2(c) PDP/信息面板信息须显著（pdf-page 3）。≥2 处。
- 可回答的新问题：圆柱罐的强制信息贴在 40% 之外的背面是否违规？「正面」由营销部门指定、但实际陈列时朝内，算不算 PDP？多个备选 PDP 时信息只印一面是否足够？
- 建议归属子卡：基础架构

### CAND-PR-03: 信息面板是 PDP 右侧紧邻面，位置本身是可开观察项的法定义务
- 条款出处：〔§ 101.2〕〔§ 101.4〕+ pdf-page 3 / 7
- 原文引用（英文逐字，≤100 词/段）：
> All information required to appear on the label of any package of food under §§ 101.4, 101.5, 101.8, 101.9, 101.13, 101.17, 101.36, subpart D of part 101, and part 105 of this chapter shall appear either on the principal display panel or on the information panel, unless otherwise specified by regulations in this chapter.
> The term information panel as it applies to packaged food means that part of the label immediately contiguous and to the right of the principal display panel as observed by an individual facing the principal display panel with the following exceptions:
- 原则陈述：信息面板的法定判据是「观察者面对 PDP 时，紧邻且位于 PDP 右侧」的相对方位，不是任意一块空白标签面。§ 101.2(b) 把 § 101.4/5/8/9/13/17/36、Subpart D、part 105 的强制信息统一收拢到「PDP 或信息面板」二选一，除非本章另有规定。法定例外有三：右侧紧邻面过小或不可用（折叠翻盖、罐端）可顺延至再右侧下一面；有备选 PDP 时以任一 PDP 右侧为准；顶面为 PDP 且无备选面时取相邻任一面板。把配料表或营养标签随意挪到「背面」而该面并非上述方位，即属位置违规。
- 复现位置：§ 101.4(a)(1) 配料表「on either the principal display panel or the information panel in accordance with the provisions of § 101.2」（pdf-page 7）；§ 101.2(c) 两面板信息须显著并满足最小字号（pdf-page 3）；§ 101.2(b) 自身列举的 8 类条款 + part 105（pdf-page 3）；§ 101.17(g)(4) 果汁警示须在信息面板或 PDP（pdf-page 214）；§ 101.17(h)(2) 壳蛋声明可在 PDP、信息面板或盒盖内（pdf-page 214）。≥2 处。
- 可回答的新问题：营养标签放在与 PDP 相对的背面是否合规？右侧是折叠翻盖时顺延到再右侧需要什么条件？「unless otherwise specified」允许哪些条款把强制信息放到别处？
- 建议归属子卡：基础架构

### CAND-PR-04: 位置、显著性、字号、对比、留白本身即法定义务，不是排版偏好
- 条款出处：〔§ 101.2〕〔§ 101.15〕〔§ 101.3〕〔§ 101.7〕+ pdf-page 3 / 210 / 5 / 12
- 原文引用（英文逐字，≤100 词/段）：
> All information appearing on the principal display panel or the information panel pursuant to this section shall appear prominently and conspicuously, but in no case may the letters and/or numbers be less than one-sixteenth inch in height unless an exemption pursuant to paragraph (f) of this section is established.
> A word, statement, or other information required by or under authority of the act to appear on the label may lack that prominence and conspicuousness required by section 403(f) of the act by reason (among other reasons) of:
> Smallness or style of type in which such word, statement, or information appears, insufficient background contrast, obscuring designs or vignettes, or crowding with other written, printed, or graphic matter.
- 原则陈述：§ 101.15(a) 把「显著性/醒目性」锚定在 FD&C Act § 403(f)，并列举六类致其不足的事由：未出现在惯常陈列面板、未在各可能呈现面板重复、标签未铺满可用面积、为非必需内容挤占空间、给其他内容过分显著性、字号/字体/对比/装饰/拥挤。§ 101.2(c) 进一步给出硬下限 1/16 英寸、并回引 § 101.7(h)(1)(2) 与 § 101.15。因此字号、颜色、背景对比、加粗、留白、平行基线都是可审计的法定义务，而非设计选择。关键反跳规则在 § 101.15(b)：若空间不足是由「非必需内容、过度显著性或外语表述」造成的，则不得以空间不足为由主张 § 403(e)/(i) 豁免。
- 复现位置：§ 101.3(d) 品名须粗体、字号与最显著印刷品相称、行与基线平行（pdf-page 5）；§ 101.7(h) 净含量字号与放置（pdf-page 13–15）；§ 101.13(d)(2) 免责声明字号不得小于净含量声明（pdf-page 199）；§ 101.17(g)(5)(6) WARNING 大写加粗、加框（pdf-page 214）；§ 101.17(h)(2) SAFE HANDLING INSTRUCTIONS 加粗（pdf-page 214）；§ 101.100(a)(2) 散装容器配料信息不小于 1/4 英寸（pdf-page 335）；§ 101.15(c) 外语触发全量翻译（pdf-page 210）。≥2 处。
- 可回答的新问题：把强制信息缩到 1/32 英寸但声称「版面紧张」能否成立？为突出品牌 logo 挤掉强制信息空间，能否援引空间不足豁免？哪些条款给出了可用字号豁免（§ 101.2(f)）？
- 建议归属子卡：基础架构

### CAND-PR-05: 强制陈述须用英语；一旦出现任何外语表述，全部强制信息须同步译出
- 条款出处：〔§ 101.15〕+ pdf-page 210
- 原文引用（英文逐字，≤100 词/段）：
> All words, statements, and other information required by or under authority of the act to appear on the label or labeling shall appear thereon in the English language: Provided, however, That in the case of articles distributed solely in the Commonwealth of Puerto Rico or in a Territory where the predominant language is one other than English, the predominant language may be substituted for English.
> If the label contains any representation in a foreign language, all words, statements, and other information required by or under authority of the act to appear on the label shall appear thereon in the foreign language
- 原则陈述：面向美国流通的包装食品，强制信息默认须用英语。触发规则是「一旦标签含任何外语表述，全部强制信息须以该外语同时出现」，不是只译被外语写的那几句；随附 labeling（非 label）含外语表述时，全部强制信息须出现在该件 labeling 上。地域例外：仅在波多黎各或主要语言非英语的领地分销，可用当地主要语言替代英语。零售餐饮用单人份小包装（≤1½ oz）且外语仅为食品名称时，豁免 (c)(2)。§ 101.15(b)(3) 还规定：为外语表述占用空间所致的空间不足，不得作为 § 403(e)/(i) 豁免理由。
- 复现位置：§ 101.15(c)(2) 外语须全量出现在 label（pdf-page 210）；§ 101.15(c)(3) 非 label 的 labeling 含外语时全量义务落在该件 labeling（pdf-page 210）；§ 101.15(b)(3) 外语占用空间不得主张豁免（pdf-page 210）；§ 101.2(c) 显著性下限（pdf-page 3）。≥2 处。
- 可回答的新问题：标签上只印了一句西班牙语营销语，是否必须把所有强制信息译成西班牙语？波多黎各专供产品能否只留西班牙语？外语仅出现在随附 pamphlet 时义务落在瓶身还是 pamphlet？
- 建议归属子卡：基础架构

### CAND-PR-06: 品名（statement of identity）按「法定名→通用名→描述名/臆造名」三级顺位，且形态、粗体、基线均受管
- 条款出处：〔§ 101.3〕+ pdf-page 5
- 原文引用（英文逐字，≤100 词/段）：
> The principal display panel of a food in package form shall bear as one of its principal features a statement of the identity of the commodity.
> This statement of identity shall be presented in bold type on the principal display panel, shall be in a size reasonably related to the most prominent printed matter on such panel, and shall be in lines generally parallel to the base on which the package rests as it is designed to be displayed.
- 原则陈述：品名须作为 PDP 的主要特征之一载明，名称取用有强制顺位：先取适用法律/法规已规定或要求的名称；缺失时用该食品通用或常用名；再缺失时用适当描述性用语，或食品性质显而易见时用公众惯用的臆造名。可选形态（整、片、丁等）属品名必要部分，须以与其他成分相称的字号标示；但若形态透过容器可见或已由适当图示表现，则可省略（§ 101.3(c) 例外）。呈现形式为：PDP 上粗体、字号与最显著印刷品相称、字行与包装设计陈列基线平行。§ 101.3(b)(1) 的「Federal law or regulation」把标准化食品（part 130 等）的法定名置于最优先。
- 复现位置：§ 101.3(c) 形态须作为品名必要部分（pdf-page 5）；§ 101.67(a)(4) 黄油声称须作为 common or usual name 一部分（pdf-page 282）；§ 101.18(b) 名称只含部分配料即可能误导、即便配料表在别处列全（pdf-page 219）；§ 101.3(e)(4) 仿制食品 nutritionally inferior 须标 imitation（pdf-page 6）；§ 101.67(a)(3)(b) 回引 § 101.3(e)(4)（pdf-page 282）。≥2 处。
- 可回答的新问题：品牌名能否顶替品名？「strawberry yogurt」只含一种配料暗示是否会因 § 101.18(b) 构成误导？形态已用图示表现时能否省略文字？
- 建议归属子卡：基础架构

### CAND-PR-07: 配料表须按重量占比降序、用通用或常用名，且受 § 101.100 豁免与膳食补充剂例外约束
- 条款出处：〔§ 101.4〕〔§ 101.100〕+ pdf-page 7 / 335
- 原文引用（英文逐字，≤100 词/段）：
> Ingredients required to be declared on the label or labeling of a food, including foods that comply with standards of identity, except those ingredients exempted by § 101.100, shall be listed by common or usual name in descending order of predominance by weight on either the principal display panel or the information panel in accordance with the provisions of § 101.2, except that ingredients in dietary supplements that are listed in the nutrition label in accordance with § 101.36 need not be repeated in the ingredient list.
- 原则陈述：配料申报的基本规则是「按通用或常用名、依重量占比降序、列于 PDP 或信息面板（按 § 101.2）」，且即便食品符合身份标准（standard of identity）也不免除。三类例外必须单独记：① § 101.100 明确列出的豁免对象（散装、 incidental additives、亚硫酸盐阈值等）；② 膳食补充剂中已在 § 101.36 营养标签列出的配料，不必在配料表重复；③ 香料/调味/色素/防腐剂按 § 101.22 与 § 101.4(b) 的特殊声明规则。本条是 Part 101 的标签内容义务，与 Part 117 中「确保正确标签用到正确产品」的过敏原标签预防控制不是同一层义务，不得互引条款号替代。
- 复现位置：§ 101.100(a) 明列「exempt from compliance with the requirements of section 403(i)(2)」的对象（pdf-page 335）；§ 101.4(a)(1) 自身「except those ingredients exempted by § 101.100」（pdf-page 7）；§ 101.36(b)/§ 101.4(g) 膳食补充剂配料表特则（pdf-page 228）；§ 101.22 香料/色素/防腐剂声明（pdf-page 219）；§ 101.2(b) 把 § 101.4 收进 PDP/信息面板二选一（pdf-page 3）。≥2 处。
- 可回答的新问题：某配料已列在 Supplement Facts 里，配料表还要不要重复？「含 2% 以下」的合并列示与降序规则如何共存？符合标准身份的食品能否以「标准已定配方」为由不列配料？
- 建议归属子卡：基础架构

### CAND-PR-08: 厂商名址须显著载明，非实际制造者须以「Manufactured for / Distributed by」限定
- 条款出处：〔§ 101.5〕+ pdf-page 11
- 原文引用（英文逐字，≤100 词/段）：
> The label of a food in packaged form shall specify conspicuously the name and place of business of the manufacturer, packer, or distributor.
> Where the food is not manufactured by the person whose name appears on the label, the name shall be qualified by a phrase that reveals the connection such person has with such food; such as “Manufactured for ______”, “Distributed by ______”, or any other wording that expresses the facts.
- 原则陈述：包装食品标签须显著载明制造商、包装商或经销商的名称与营业地，主体三选一即可，但必须真实揭示与该食品的连接关系。公司须用实际法人名（可前后附加事业部名），个体/合伙/社团用经营所用名号（§ 101.5(b)）。当标签具名者并非实际制造者时，必须用「Manufactured for」「Distributed by」或同等表述限定，否则构成误导。本义务落在 `label`（非 labeling），且 § 101.2(b) 把它收进 PDP/信息面板二选一。§ 101.100(b)(1) 对零售店内重新包装食品给出 § 403(e)(1) 名址义务的豁免情形。
- 复现位置：§ 101.2(b) 把 § 101.5 列入 PDP/信息面板收拢清单（pdf-page 3）；§ 101.100(b)(1) 零售店重包装可免 § 403(e)(1) 名址（pdf-page 336）；§ 101.2(a)(3) 小包装软饮名址可置于瓶盖/罐盖且不小于规定字号（pdf-page 3）；§ 101.18(a)(b) 标签中的虚假或误导表述构成 misbranding（pdf-page 219）。≥2 处。
- 可回答的新问题：委托代工时只印品牌商名称不写「Distributed by」是否违规？公司能否只印品牌商标而不印法人名？零售店内分装食品是否仍须印名址？
- 建议归属子卡：基础架构

### CAND-PR-09: 净含量须置于 PDP，并按液态/固态/干量分别取法定单位
- 条款出处：〔§ 101.7〕+ pdf-page 12
- 原文引用（英文逐字，≤100 词/段）：
> The principal display panel of a food in package form shall bear a declaration of the net quantity of contents. This shall be expressed in the terms of weight, measure, numerical count, or a combination of numerical count and weight or measure. The statement shall be in terms of fluid measure if the food is liquid, or in terms of weight if the food is solid, semisolid, or viscous, or a mixture of solid and liquid;
- 原则陈述：净含量声明须置于 PDP，表达方式限重量、度量、计数或其组合，且介质决定单位：液体用液量、固体/半固体/黏稠/固液混合物用重量；鲜果蔬等惯按干量出售者可用干量（例外）。有稳固的通用消费与贸易惯例时，液体可按重量、固体可按其他方式（§ 101.7(a) 续文）。声明须位于 PDP，备选 PDP 时逐面重复（§ 101.7(a) 续、§ 101.7 定位条款）。§ 101.2(c) 回引 § 101.7(h)(1)(2) 作为显著性/易读性规格，§ 101.15 把字号不足列为显著性缺陷。
- 复现位置：§ 101.2(c)「The requirements for conspicuousness and legibility shall include the specifications of §§ 101.7(h)(1) and (2) and 101.15」（pdf-page 3）；§ 101.3(d) 品名字号与最显著印刷品相称（pdf-page 5）；§ 101.13(d)(2) 免责声明字号不小于 § 101.7(i) 净含量声明（pdf-page 199）；§ 101.2(b) 把 § 101.7 相关信息收进面板规则（pdf-page 3）。≥2 处。
- 可回答的新问题：液体食品按重量标净含量是否一律禁止？固液混合物（如罐头水果）该用重量还是液量？备选 PDP 时净含量只印一面是否违规？
- 建议归属子卡：基础架构

### CAND-PR-10: 自加压容器强制警示（含温度上限与儿童隔离），属特定风险品类的标签义务
- 条款出处：〔§ 101.17〕+ pdf-page 211
- 原文引用（英文逐字，≤100 词/段）：
> The label of a food packaged in a self-pressurized container and intended to be expelled from the package under pressure shall bear the following warning: WARNING—Avoid spraying in eyes. Contents under pressure. Do not puncture or incinerate. Do not store at temperature above 120 °F. Keep out of reach of children.
- 原则陈述：凡自加压容器、且拟在压力下喷出的食品，其标签必须逐字载明该警示，内容包括避免喷入眼睛、内容物带压、不得刺穿或焚烧、储存温度不得高于 120 °F、置于儿童接触不到处。允许的三类有限变体：儿童用产品可在末句加「except under adult supervision」；玻璃容器可用「break」替「puncture」；非喷雾产品可删「Avoid spraying in eyes」。这是 § 101.17 一系列「warning / notice / safe handling statements」中的第一项，是标签义务，不以产品已安全为条件、也不替代任何工艺控制义务。
- 复现位置：§ 101.17(g)(2) 未巴氏果汁 WARNING 声明（pdf-page 214）；§ 101.17(h)(1) 壳蛋 SAFE HANDLING INSTRUCTIONS（pdf-page 214）；§ 101.17 标题「Food labeling warning, notice, and safe handling statements」（pdf-page 211）；§ 101.17(g)(4)(5)(6) 警示须显著、WARNING 大写加粗、加框（pdf-page 214）；§ 101.2(b) 把 § 101.17 收进 PDP/信息面板清单（pdf-page 3）。≥2 处。
- 可回答的新问题：喷罐奶油（whipped topping）是否必须带 120 °F 警示？玻璃瓶加压产品用「break」替换后其余文字能否改动？警示声明放在随附说明书而非罐身是否足够？
- 建议归属子卡：特定品类与警示

### CAND-PR-11: 香料/调味/色素/防腐剂按专门定义与声明规则处理，不按普通配料逐名列示
- 条款出处：〔§ 101.22〕〔§ 101.4〕+ pdf-page 219 / 7
- 原文引用（英文逐字，≤100 词/段）：
> The term artificial flavor or artificial flavoring means any substance, the function of which is to impart flavor, which is not derived from a spice, fruit or fruit juice, vegetable or vegetable juice, edible yeast, herb, bark, bud, root, leaf or similar plant material, meat, fish, poultry, eggs, dairy products, or fermentation products thereof.
> Spices, flavorings, colorings and chemical preservatives shall be declared according to the
- 原则陈述：§ 101.22 以「来源清单」反向定义 artificial flavor（凡非来自香料、果蔬及其汁、食用酵母、草本、树皮、芽、根、叶、肉、鱼、禽、蛋、乳制品或其发酵产物者即为人工香料），并给出 spice 的定义（以调味而非营养为显著功能、真实具名、未去除挥发油者，洋葱/大蒜/芹菜等传统视为食品者除外）。§ 101.4(b) 规定香料、调味、色素、化学防腐剂不按普通配料逐名降序，而按本条专门规则以类别名声明并标注功能。因此「含人工香料」与「含某种具体植物提取物」的法律后果不同，须先判定物质是否落入 § 101.22 定义。
- 复现位置：§ 101.4(a)(1)「Ingredients required to be declared ... shall be listed by common or usual name」为本条特则的对照基线（pdf-page 7）；§ 101.4(a)(14) 单一脂肪/油配料须具体名声明（pdf-page 8）；§ 101.100(a)(3) incidental additives / processing aids 的豁免（pdf-page 335）；§ 101.100(a)(4) 亚硫酸盐 10 ppm 阈值（pdf-page 336）；§ 101.2(b) 把 § 101.4 收进面板规则（pdf-page 3）。≥2 处。
- 可回答的新问题：从酵母提取物获得的增味剂算 natural 还是 artificial flavor？化学防腐剂能否只写「preservative」不写具体名？香料提取物去除了挥发油后是否仍属 spice？
- 建议归属子卡：基础架构

### CAND-PR-12: 果汁百分比声明由「purport to be」触发，名称、图示、外观任一即可
- 条款出处：〔§ 101.30〕+ pdf-page 224
- 原文引用（英文逐字，≤100 词/段）：
> This section applies to any food that purports to be a beverage that contains any fruit or vegetable juice (i.e., the product's advertising, label, or labeling bears the name of, or variation on the name of, or makes any other direct or indirect representation with respect to, any fruit or vegetable juice), or the label or labeling bears any vignette (i.e., depiction of a fruit or vegetable) or other pictorial representation of any fruit or vegetable, or the product contains color and flavor that gives the beverage the appearance and taste of containing a fruit or vegetable juice.
- 原则陈述：百分比果汁声明义务的触发不是「实际含果汁」，而是「purport to be（声称/表现为含果汁饮料）」：广告、标签或 labeling 出现果汁名称或其变体、任何直接或间接表述，或标签出现水果/蔬菜图示、或其他图示表征，或产品用色素与香精使其外观口味像含果汁——任一即触发。法规明示反例：软饮（soda）若其物理特性、名称、labeling、配料表、广告均不表征或暗示含果汁，则不 purport、无需百分比声明。声明格式为「Contains __ percent ___ juice」或「__ percent juice」，百分比为不大于实际值的整数。该条是「暗示与明示同等受管」在品类层的具体化。
- 复现位置：§ 101.30(b)(1) 百分比声明措辞（pdf-page 224）；§ 101.13(b)(2) 暗示声称定义（pdf-page 199）；§ 101.14(a)(1) 健康声称含符号/vignettes（pdf-page 206）；§ 101.18(a)(b)(c) 标签中的虚假/误导/产地暗示（pdf-page 219）；§ 101.95 用语「expressly or implicitly」判断（pdf-page 334）。≥2 处。
- 可回答的新问题：包装上只画了一个橙子图案、配料表无果汁，是否必须标 0% 果汁？「fruit-flavored」字样是否触发？用色素+香精做出橙味但名称不提水果，算不算 purport？
- 建议归属子卡：特定品类与警示

### CAND-PR-13: 非零售/即时消费场景（自动售货机、餐馆、连锁菜单）是标签义务的延伸而非豁免
- 条款出处：〔§ 101.8〕〔§ 101.10〕〔§ 101.11〕+ pdf-page 16 / 68 / 69
- 原文引用（英文逐字，≤100 词/段）：
> Vending machine means a self-service machine that, upon insertion of a coin, paper currency, token, card, or key, or by optional manual operation, dispenses servings of food in bulk or in packages, or prepared by the machine, without the necessity of replenishing the machine between each vending
> Nutrition labeling in accordance with § 101.9 shall be provided upon request for any restaurant food or meal for which a nutrient content claim (as defined in § 101.13 or in subpart D of this part) or a health claim (as defined in § 101.14 and permitted by a regulation in subpart E of this part) is made
- 原则陈述：Part 101 不因「非包装零售」而整体退出：§ 101.8 把自动售货机纳入定义并设经营主体注册（§ 403(q)(5)(H)(viii) 相关），§ 101.10 对餐馆食品在作出声称时要求「应请求提供 § 101.9 营养信息」，§ 101.11 对 covered establishment 的标准菜单项设强制卡路里等声明。三者共同说明销售渠道改变的是「义务形式」（柜台卡、菜单、书面营养信息、注册），不是「有无义务」。§ 101.9(j)(2) 把餐馆/即时消费食品列为豁免，但明确「except as provided in § 101.11」且「Claims ... subject the food to the provisions of this section」——豁免是有条件、可被声称击穿的。
- 复现位置：§ 101.9(j)(2) 餐馆/即时消费食品豁免及其声称击穿条件（pdf-page 58）；§ 101.10 声称触发应请求营养信息（pdf-page 68）；§ 101.11(b)(2)(ii)(A) 书面营养信息可满足 § 101.10（pdf-page 69–70）；§ 101.11(f) 标准菜单项不合规即 misbranded（pdf-page 82）；§ 101.9(a)(2) 非包装食品须在销售点清晰展示（pdf-page 20）。≥2 处。
- 可回答的新问题：自动售货机食品是否因「无传统标签」而免于卡路里披露？餐馆菜单写「low fat」但只在顾客索要时给营养数据，是否足够？covered establishment 的判定门槛在哪？
- 建议归属子卡：豁免与效力层

### CAND-PR-14: misbranding 总纲——labeling 中的虚假、误导、部分命名、产地暗示均可致食品 misbranded
- 条款出处：〔§ 101.18〕+ pdf-page 219
- 原文引用（英文逐字，≤100 词/段）：
> Among representations in the labeling of a food which render such food misbranded is a false or misleading representation with respect to another food or a drug, device, or cosmetic.
> The labeling of a food which contains two or more ingredients may be misleading by reason (among other reasons) of the designation of such food in such labeling by a name which includes or suggests the name of one or more but not all such ingredients, even though the names of all such ingredients are stated elsewhere in the labeling.
- 原则陈述：§ 101.18 是 Part 101 在 Subpart B 的 misbranding 总纲：labeling 中对另一食品或药品/器械/化妆品作虚假或误导表述、名称只含部分配料（即便配料表在别处列全）、或表达/暗示地理产地，均可使食品 misbranded。产地表述有四类法定例外：真实产地、非欺骗性误述的商标/商号（长期专属使用已被理解为特定厂商、或任意臆造不致联想产地）、联邦法律要求的名称、以及市场含义被理解为品类/风格而非产地的名称。判断落点是「labeling 中的 representation」而非仅标签文字，与 CAND-PR-01 的作用域原则一致。
- 复现位置：§ 101.9(k) 营养标签下 label/labeling 的疾病暗示即 misbranded（pdf-page 67）；§ 101.11(f) 标准菜单项 misbranded（pdf-page 82）；§ 101.91(b) gluten-free 不符即 deemed misbranded（pdf-page 330）；§ 101.18(c) 产地暗示四类例外（pdf-page 219）；§ 101.3(b)/§ 101.18(b) 品名与部分配料命名（pdf-page 5 / 219）。≥2 处。
- 可回答的新问题：品名只提「草莓」但配料表列全其他水果，是否仍属误导？长期使用已使消费者联想特定厂商的地名商标能否保留？「瑞士风格」算产地还是品类风格？
- 建议归属子卡：豁免与效力层

### CAND-PR-15: 营养标签「默认适用 + 列举豁免」结构，举证责任在援引豁免方
- 条款出处：〔§ 101.9〕〔§ 101.36〕〔§ 101.13〕+ pdf-page 20 / 228 / 199
- 原文引用（英文逐字，≤100 词/段）：
> Nutrition information relating to food shall be provided for all products intended for human consumption and offered for sale unless an exemption is provided for the product in paragraph (j) of this section.
> The label of a dietary supplement that is offered for sale shall bear nutrition labeling in accordance with this regulation unless an exemption is provided for the product in paragraph (h) of this section.
- 原则陈述：§ 101.9(a) 与 § 101.36(a) 用完全同构的句式确立「默认适用」：凡拟供人食用且要约销售的产品均须营养标签，除非在各自豁免段（§ 101.9(j) / § 101.36(h)）为该产品列有豁免。§ 101.13(a) 又以「apply to foods that are intended for human consumption and that are offered for sale」把声称规则锚到同一适用范围。因此合规判断顺序是「先假定须标 → 再找特定豁免条款 → 核对该豁免的全部条件」，而非「先找理由不标」。豁免是列举式、附条件的，且可被声称行为击穿（见 CAND-PR-16）。§ 101.9(a)(3) 还规定：对被豁免食品主动征集营养信息请求，只要回复符合本节，不使该豁免食品重新落入本节要求——这是「豁免不因提供信息而丧失」的有限例外。
- 复现位置：§ 101.9(j) 逐项豁免清单（pdf-page 58–60）；§ 101.36(h) 膳食补充剂豁免（pdf-page 231–232）；§ 101.13(a) 声称规则适用范围（pdf-page 199）；§ 101.9(a)(3) 征集请求不破豁免（pdf-page 20）；§ 101.100/§ 101.108 各针对特定义务的豁免（pdf-page 335 / 340）。≥2 处。
- 可回答的新问题：小企业年销售额低于门槛是否自动免标？被豁免食品主动寄送营养资料会不会「自愿入局」？膳食补充剂的豁免段与常规食品豁免段能否互相援引？
- 建议归属子卡：豁免与效力层

### CAND-PR-16: 作出声称即触发营养标签义务 / 击穿既有豁免（「声称使豁免失效」）
- 条款出处：〔§ 101.9〕〔§ 101.10〕〔§ 101.11〕〔§ 101.36〕+ pdf-page 58 / 68 / 69 / 228
- 原文引用（英文逐字，≤100 词/段）：
> Provided, That the food bears no nutrition claims or other nutrition information in any context on the label or in labeling or advertising. Claims or other nutrition information subject the food to the provisions of this section, § 101.10, or § 101.11, as applicable.
> Nutrition labeling in accordance with § 101.9 shall be provided upon request for any restaurant food or meal for which a nutrient content claim (as defined in § 101.13 or in subpart D of this part) or a health claim (as defined in § 101.14 and permitted by a regulation in subpart E of this part) is made
- 原则陈述：§ 101.9(j) 的多项豁免（小企业直销、餐馆食品、即时消费场所食品等）都以「the food bears no nutrition claims or other nutrition information in any context」为持续条件；一旦在 label、labeling 或 advertising 任何场合出现声称或其他营养信息，该食品即被「subject the food to」§ 101.9 / § 101.10 / § 101.11 的营养标签义务。§ 101.10 独立规定：餐馆食品作出营养素含量声称或健康声称时，须应请求提供 § 101.9 营养信息（可以声称依据的营养素量作功能等价）。因此声称行为是「豁免的击穿器」，且触发范围覆盖广告而不止标签。§ 101.9(a)(3) 是反向例外：仅被动回复征集请求不破豁免。
- 复现位置：§ 101.9(j)(1)(i) 小企业豁免的「bears no nutrition claims」条件（pdf-page 58）；§ 101.9(j)(2)(i) 餐馆食品豁免同款条件（pdf-page 58）；§ 101.9(j) 续文多处「Claims or other nutrition information subject the food」（pdf-page 58–60）；§ 101.10 声称触发应请求营养信息（pdf-page 68）；§ 101.11 覆盖场所的强制声明（pdf-page 69）；§ 101.36(h) 膳食补充剂豁免的同类条件（pdf-page 231）。≥2 处，为高频复现。
- 可回答的新问题：小企业豁免产品印了一句「低钠」是否立即必须做完整营养标签？餐馆在外卖平台广告写「高蛋白」算不算「advertising」触发？仅回复顾客邮件询问营养数据是否破豁免？
- 建议归属子卡：豁免与效力层

### CAND-PR-17: serving size 以「每次食用习惯消费量（RACC）」为基础，按 household measure 表达
- 条款出处：〔§ 101.9〕〔§ 101.12〕〔§ 101.36〕+ pdf-page 21 / 83 / 228
- 原文引用（英文逐字，≤100 词/段）：
> The term serving or serving size means an amount of food customarily consumed per eating occasion by persons 4 years of age or older which is expressed in a common household measure that is appropriate to the food.
> The following reference amounts shall be used as the basis for determining serving sizes for specific products:
> The serving size shall be determined in accordance with §§ 101.9(b) and 101.12(b), Table 2.
- 原则陈述：serving size 不是厂商可自由定的「建议食用量」，而是以 § 101.12 的 reference amount customarily consumed（RACC，按 4 岁及以上人群每次食用习惯消费量、源自全国食物消费调查）为基础，经 § 101.9(b) 程序换算成适合该食品的 household measure（杯、片、勺等）。§ 101.36(b)(1)(i) 把膳食补充剂 serving size 也回引 § 101.9(b) 与 § 101.12(b) Table 2。婴幼儿/1–3 岁儿童用专门 RACC，且仅当食品专为该人群配制或加工时适用（§ 101.12(a)(2)）。§ 101.12(b) 表格数值属不可逐字引用区，本候选只引其「作为 basis」的 prose 规则与回引关系。
- 复现位置：§ 101.9(b)(2) 起各款把 RACC 换算为 label serving size 的程序（pdf-page 21）；§ 101.12(a) RACC 制定原则与调查数据（pdf-page 82）；§ 101.12(b) prose 引导句（pdf-page 83）；§ 101.36(b)(1)(i) 补充剂回引（pdf-page 228）；§ 101.45(a)(2) 生鲜自愿标签 serving size 回引 § 101.9(b)(c)（pdf-page 245）；§ 101.14(a)(4) 以 RACC 为 disqualifying 分母（pdf-page 206）。≥2 处。
- 可回答的新问题：厂商能否把「每份」定得比 RACC 小以美化数值？婴幼儿食品何时切换用儿童 RACC？膳食补充剂的「每份 2 片」是否也要回 § 101.12 Table 2？
- 建议归属子卡：营养标签与份量

### CAND-PR-18: 所有营养素与食品成分量须「相对一份」申报，且单位/格式法定
- 条款出处：〔§ 101.9〕〔§ 101.36〕+ pdf-page 20 / 228
- 原文引用（英文逐字，≤100 词/段）：
> Except as provided in § 101.9(h)(3), all nutrient and food component quantities shall be declared in relation to a serving as defined in this section.
- 原则陈述：营养标签中每一项营养素/食品成分的数值都须相对「本节定义的一份（serving）」申报，而一份又由 RACC 推导（CAND-PR-17），因此 RACC→serving→所有数值是一条不可断的链。§ 101.9(a)(1) 规定包装食品须用本节指定格式，§ 101.9(a)(2) 规定非包装食品须在销售点清晰展示（柜台卡、标牌、吊牌或小册子）。§ 101.9(h)(3) 为列明的例外。§ 101.36(b) 对膳食补充剂要求按 (e) 款指定小标题与格式（Supplement Facts）申报。数值口径错配（按 100 g、按整包、按 RACC 但未换算）都会导致标签不实。
- 复现位置：§ 101.9(c) 各营养素「A statement of the ... in a serving」（pdf-page 21 起）；§ 101.36(b) Supplement Facts 申报清单（pdf-page 228）；§ 101.9(b)「all nutrient and food component quantities shall be declared in relation to a serving」（pdf-page 20）；§ 101.45(a)(2) 生鲜自愿标签同样以 serving 为基准（pdf-page 245）；§ 101.10 声称依据的营养素量作功能等价（pdf-page 68）。≥2 处。
- 可回答的新问题：能否额外按「每 100 g」并列标示主数值？非包装食品把营养信息放进小册子是否属「at the point of purchase」？§ 101.9(h)(3) 例外覆盖哪些情形？
- 建议归属子卡：营养标签与份量

### CAND-PR-19: 膳食补充剂用 Supplement Facts 独立体系，但与 § 101.9/§ 101.12 共用份量基座
- 条款出处：〔§ 101.36〕〔§ 101.9〕〔§ 101.12〕+ pdf-page 228 / 20 / 83
- 原文引用（英文逐字，≤100 词/段）：
> The label of a dietary supplement that is offered for sale shall bear nutrition labeling in accordance with this regulation unless an exemption is provided for the product in paragraph (h) of this section.
> The serving size shall be determined in accordance with §§ 101.9(b) and 101.12(b), Table 2.
- 原则陈述：膳食补充剂不直接套用常规食品 Nutrition Facts，而适用 § 101.36 的 Supplement Facts 体系：小标题、格式、申报项由 (b)/(e) 规定，且有 § 101.4(g) 的配料表特则与 § 101.93 的 403(r)(6) 声明免责声明。但份量基座与常规食品共用——§ 101.36(b)(1)(i) 明确回引 § 101.9(b) 与 § 101.12(b) Table 2，且 § 101.13(a) 把膳食补充剂纳入声称通则适用对象。因此「体系独立、基座共享」：不能用 supplement 的格式特则否定 RACC/serving 的通用约束，也不能用 § 101.9 的格式要求覆盖 Supplement Facts 的专门版式。
- 复现位置：§ 101.9(j)/§ 101.36(h) 两套并列的豁免段（pdf-page 58 / 231）；§ 101.13(b)「under § 101.9 or under § 101.36」并列（pdf-page 199）；§ 101.13(b)(5) 补充剂热量/脂肪/胆固醇声称特则（pdf-page 199）；§ 101.65(a)(3) 暗示声称回引 § 101.36（pdf-page 272）；§ 101.4(a)(1) 补充剂配料表特则（pdf-page 7）；§ 101.93 免责声明（pdf-page 332）。≥2 处。
- 可回答的新问题：膳食补充剂能否用常规 Nutrition Facts 版式？「每份 2 片」是否受 RACC 约束？补充剂作出「high potency」声称时适用 § 101.13 还是 § 101.36？
- 建议归属子卡：营养标签与份量

### CAND-PR-20: 生鲜果蔬鱼的营养标签是「自愿 + 指南（should）层」，不设强制义务
- 条款出处：〔§ 101.42〕〔§ 101.43〕〔§ 101.44〕〔§ 101.45〕+ pdf-page 243 / 243 / 244 / 244
- 原文引用（英文逐字，≤100 词/段）：
> The Food and Drug Administration (FDA) urges food retailers to provide nutrition information, as provided in § 101.9(c), for raw fruit, vegetables, and fish at the point-of-purchase. If retailers choose to provide such information, they should do so in a manner that conforms to the guidelines in § 101.45.
> Nutrition labeling for raw fruits, vegetables, and fish listed in § 101.44 should be presented to the public in the following manner:
- 原则陈述：§ 101.42–45 对生鲜果蔬鱼采用与 § 101.9 完全不同的效力层：动词是 `urges`、`should`、`If retailers choose to`，即自愿指南，不创设强制义务；§ 101.43 定义「substantial compliance」、§ 101.44 列出 20 种最常消费品种、§ 101.45 给出陈列与份量/营养素指南。零售商一旦选择提供，则「should」按 § 101.45 方式呈现，且 § 101.45(a)(2) 仍回引 § 101.9(b)(c) 的份量与营养素口径（生鲜按 raw edible portion、鱼按 cooked edible portion）。因此本簇是「法规正文内的自愿指南层」，须与 § 101.9 的 `shall` 强制层、以及 FDA 行业指南/检查程序层严格区分，不得把 `should` 读成 `shall`。
- 复现位置：§ 101.43 substantial compliance 定义（pdf-page 243）；§ 101.44 20 种最常消费清单（pdf-page 244）；§ 101.45(a) 各款 `should` 陈列方式（pdf-page 244）；§ 101.42(b)(c)(d) 回引 §§ 101.44/101.43/101.45（pdf-page 243）；§ 101.10 声称触发时（餐馆/生鲜邻近场景）`shall` 与 `should` 的对照（pdf-page 68）；§ 101.9(a)(2) 非包装食品 `shall ... displayed clearly at the point of purchase`（pdf-page 20）。≥2 处。
- 可回答的新问题：零售商未提供生鲜营养信息是否构成违规？提供了但版式与 § 101.45 不符，法律后果与 § 101.9 不合规是否相同？「substantial compliance」是否产生可强制执行的义务？
- 建议归属子卡：营养标签与份量

### CAND-PR-21: 餐馆食品作出声称时须「应请求」提供营养信息，可用声称依据量作功能等价
- 条款出处：〔§ 101.10〕〔§ 101.11〕+ pdf-page 68 / 69
- 原文引用（英文逐字，≤100 词/段）：
> Nutrition labeling in accordance with § 101.9 shall be provided upon request for any restaurant food or meal for which a nutrient content claim (as defined in § 101.13 or in subpart D of this part) or a health claim (as defined in § 101.14 and permitted by a regulation in subpart E of this part) is made, except that information on the nutrient amounts that are the basis for the claim (e.g., “low fat, this meal provides less than 10 grams of fat”) may serve as the functional equivalent of complete nutrition information as described in § 101.9.
- 原则陈述：§ 101.10 的触发条件是「作出营养素含量声称（§ 101.13/Subpart D）或健康声称（§ 101.14 且经 Subpart E 授权）」，义务形式是「upon request 提供 § 101.9 营养信息」，而非预先印在菜单上。法定替代：提供作为声称依据的营养素量（如「low fat, this meal provides less than 10 grams of fat」）可作为完整营养信息的功能等价。§ 101.10 还允许用营养数据库、食谱、分析或其他合理基础确定营养素水平，并明示 covered establishment 标准菜单项的 § 101.11(b)(2)(ii)(A) 书面营养信息即可满足本条。§ 101.9(j)(2)(i) 的餐馆豁免以「无声称」为条件，与本条构成「声称击穿豁免」的闭环。
- 复现位置：§ 101.9(j)(2)(i) 餐馆豁免的「Claims ... subject the food」条件（pdf-page 58）；§ 101.11(b)(2)(ii)(A) 书面营养信息满足 § 101.10（pdf-page 70）；§ 101.9(a)(2) 非包装食品销售点展示（pdf-page 20）；§ 101.45 呈现方式可被 § 101.10 引用（pdf-page 244）；§ 101.13 声称定义（pdf-page 199）。≥2 处。
- 可回答的新问题：餐馆菜单写「low fat」但只在顾客索要时给数据是否足够？「less than 10 grams of fat」能否替代完整 Nutrition Facts？用第三方营养数据库估算是否合规？
- 建议归属子卡：营养标签与份量

### CAND-PR-22: 连锁餐饮标准菜单项强制卡路里等声明，不合规即构成 misbranded
- 条款出处：〔§ 101.11〕+ pdf-page 82
- 原文引用（英文逐字，≤100 词/段）：
> Misbranding. A standard menu item offered for sale in a covered establishment shall be deemed misbranded under sections 201(n), 403(a), 403(f) and/or 403(q) of the Federal Food, Drug, and Cosmetic Act if its label or labeling is not in conformity with paragraph (b) or (c) of this section.
- 原则陈述：§ 101.11 对 covered establishment 的 standard menu item 设强制声明（卡路里等，(b)/(c) 款），并把不合规直接挂钩 FD&C Act §§ 201(n)、403(a)、403(f)、403(q) 的 misbranded 执法钩子——这是 Part 101 中「条款级明文写出 misbranded 后果」的少数位置之一。适用对象是「standard menu item」与「covered establishment」两个法定定义项，不是所有餐饮食品；§ 101.9(j)(2) 的餐馆豁免明确「except as provided in § 101.11」，说明本条优先于一般餐馆豁免。§ 101.10 的书面营养信息可满足本条，二者是「强制声明 ↔ 应请求信息」的接口。
- 复现位置：§ 101.9(j)(2)「Except as provided in § 101.11」（pdf-page 58）；§ 101.10 末段回引 § 101.11(b)(2)(ii)(A)（pdf-page 69）；§ 101.11(a) covered establishment 定义（pdf-page 69）；§ 101.9(k) 另一处 misbranded 明文（pdf-page 67）；§ 101.91(b) gluten-free 不符即 deemed misbranded（pdf-page 330）。≥2 处。
- 可回答的新问题：标准菜单项漏标卡路里，执法依据是 § 101.11 还是 § 403(q)？「covered establishment」门槛（连锁店数）如何判定？§ 101.10 的应请求信息能否替代 § 101.11 的菜单强制声明？
- 建议归属子卡：营养标签与份量

### CAND-PR-23: 营养素含量声称通则——明示与暗示同等受管，且须依 Subpart D 逐词定义作出
- 条款出处：〔§ 101.13〕+ pdf-page 199
- 原文引用（英文逐字，≤100 词/段）：
> A claim that expressly or implicitly characterizes the level of a nutrient of the type required to be in nutrition labeling under § 101.9 or under § 101.36 (that is, a nutrient content claim) may not be made on the label or in labeling of foods unless the claim is made in accordance with this regulation and with the applicable regulations in subpart D of this part or in part 105 or part 107 of this chapter.
- 原则陈述：§ 101.13(b) 是营养素含量声称的总闸门：凡「expressly or implicitly」表征 § 101.9/§ 101.36 要求申报的营养素水平，均属 nutrient content claim，除非依本条及 Subpart D（或 part 105/107）相应规则作出，否则不得出现在 label 或 labeling。关键在 `expressly or implicitly` 并列——暗示表述与直接数值声称受同一套约束。§ 101.13(b)(1)(2) 随即把 expressed / implied 各下定义，§ 101.13(b)(3) 对 2 岁以下婴幼儿食品设「除非 parts 101/105/107 明文规定否则不得声称」的禁止，§ 101.13(b)(4) 允许不误导的拼写变体（如 hi/lo）。本条把 § 101.9/§ 101.36 两套营养标签体系并列，与 CAND-PR-19 呼应。
- 复现位置：§ 101.13(b)(2) 暗示声称定义（pdf-page 199）；§ 101.14(a)(1) 健康声称同样「expressly or by implication」（pdf-page 206）；§ 101.54/56/60/61/62/65 各条「made in accordance with the general requirements for nutrient content claims in § 101.13」（pdf-page 247/250/253/257/260/272）；§ 101.67(a)(1) 黄油声称回引 § 101.13（pdf-page 282）；§ 101.10 声称定义回引 § 101.13（pdf-page 68）。≥2 处，为高频复现。
- 可回答的新问题：「high in oat bran」未写数值是否仍需满足 Subpart D 阈值？2 岁以下食品能否作任何营养素声称？「hi」「lo」这类拼写变体是否一律允许？
- 建议归属子卡：声称闸门

### CAND-PR-24: 暗示声称分「描述式」与「healthy 式」两类，均按明示声称同等合规
- 条款出处：〔§ 101.13〕〔§ 101.65〕+ pdf-page 199 / 272
- 原文引用（英文逐字，≤100 词/段）：
> An implied nutrient content claim is any claim that: (i) Describes the food or an ingredient therein in a manner that suggests that a nutrient is absent or present in a certain amount (e.g., “high in oat bran”); or (ii) Suggests that a food, because of its nutrient content, may be useful in maintaining healthy dietary practices, where there is also implied or explicit information about the nutrition content of the food (e.g., “healthy”).
> General requirements. An implied nutrient content claim can only be made on the label and in labeling of the food if:
- 原则陈述：§ 101.13(b)(2) 把 implied claim 分为两类：① 以描述食品或某配料的方式暗示某营养素缺失或达某含量（如「high in oat bran」）；② 暗示因营养素含量而有助于维持健康饮食习惯、且同时带有明示或暗示的营养内容信息（如「healthy」）。§ 101.65 专条处理 implied claims，其 (a) 款以「can only be made ... if」设三条件闸门（用本节定义词、符合 § 101.13 通则、食品按 § 101.9/§ 101.10/§ 101.36 标注），(b) 款列出「一般不构成暗示声称」的负面清单——但前提是「不处于 § 101.13(b)(2) 会使其成为暗示声称的语境」。因此语境（context）是暗示声称的判准，同一句话在不同上下文可能受管或不受管。
- 复现位置：§ 101.65(a)(1)(2)(3) 暗示声称三条件（pdf-page 272）；§ 101.65(b) 非暗示声称负面清单与「context」限定（pdf-page 272）；§ 101.14(a)(1) 健康声称的 implied 定义（pdf-page 206）；§ 101.95「expressly or implicitly」「suggest or imply」判断（pdf-page 334）；§ 101.30(a) 图示/名称表征触发（pdf-page 224）；§ 101.13(c) 营养标签内 vs 移出（pdf-page 199）。≥2 处。
- 可回答的新问题：品牌名里用「healthy」是否落入 § 101.13(b)(2)(ii)？§ 101.65(b) 的某项陈述换到促销语境后是否变成暗示声称？「healthy」声称的记录保存义务挂在哪个条款？
- 建议归属子卡：声称闸门

### CAND-PR-25: 营养标签内的法定信息不算声称；同一信息移出标签即变声称
- 条款出处：〔§ 101.13〕+ pdf-page 199
- 原文引用（英文逐字，≤100 词/段）：
> Information that is required or permitted by § 101.9 or § 101.36, as applicable, to be declared in nutrition labeling, and that appears as part of the nutrition label, is not a nutrient content claim and is not subject to the requirements of this section. If such information is declared elsewhere on the label or in labeling, it is a nutrient content claim and is subject to the requirements for nutrient content claims.
- 原则陈述：§ 101.13(c) 给出一条「位置决定性质」的元规则：同一营养素数值，若作为 nutrition label 的一部分出现，是标签法定内容、不视为声称、不受 § 101.13 约束；若出现在 label 或 labeling 的其他位置（如正面营销语「仅含 100 卡」），则立即构成 nutrient content claim 并落入声称要求。因此合规判断不能只看「写了什么」，必须看「写在哪里」。该规则与 CAND-PR-01（label/labeling 作用域）、CAND-PR-23（声称闸门）联动：把数值从 Nutrition Facts 搬到 PDP，等于主动开启声称闸门与营养标签触发义务。
- 复现位置：§ 101.13(b) 声称定义以「of the type required to be in nutrition labeling under § 101.9 or under § 101.36」为界（pdf-page 199）；§ 101.9(a)(1)(2) 包装/非包装营养信息格式（pdf-page 20）；§ 101.36(b) Supplement Facts 申报项（pdf-page 228）；§ 101.10 声称依据量可作功能等价（pdf-page 68）；§ 101.9(j) 豁免的「no nutrition claims or other nutrition information」条件（pdf-page 58）。≥2 处。
- 可回答的新问题：把 Nutrition Facts 里的「0 g sat fat」印到正面是否触发声称合规？营养标签内数值用彩色高亮算不算「elsewhere」？非包装食品销售点柜台卡上的数值适用哪一套？
- 建议归属子卡：声称闸门

### CAND-PR-26: 健康声称定义「expressly or by implication」涵盖品牌名、符号、图形、第三方引用
- 条款出处：〔§ 101.14〕+ pdf-page 206
- 原文引用（英文逐字，≤100 词/段）：
> Health claim means any claim made on the label or in labeling of a food, including a dietary supplement, that expressly or by implication, including “third party” references, written statements (e.g., a brand name including a term such as “heart”), symbols (e.g., a heart symbol), or vignettes, characterizes the relationship of any substance to a disease or health-related condition.
- 原则陈述：§ 101.14(a)(1) 把健康声称定义为「表征某物质与某疾病或健康相关状况之间关系」的任何声称，并明确覆盖 expressly or by implication 的全部形式：第三方引用、书面陈述（如含「heart」的品牌名）、符号（心形符号）、vignettes（图示）。第二句进一步把「在呈现语境中暗示该关系存在」的陈述/符号/图示都纳入 implied health claim。因此健康声称的判准是「是否表征物质—疾病关系」，而非是否出现法定模型措辞；一个心形 logo 落在高纤维谷物盒上就可能构成健康声称。§ 101.14(a)(5) 把「必需营养素缺乏症（坏血病、糙皮病）」排除在 disease 定义之外，从而不落入 § 101.14/§ 101.70。
- 复现位置：§ 101.14(a)(1) 第二句 implied health claims 细化（pdf-page 206）；§ 101.14(d)(2)(iv) 图形材料构成明示或暗示健康声称时参考声明须紧邻（pdf-page 208）；§ 101.13(b)(2) 暗示营养素含量声称（pdf-page 199）；§ 101.69(a)「petitions for claims, expressed or implied」（pdf-page 283）；§ 101.14(a)(5) 疾病定义排除项（pdf-page 207）；§ 101.9(k)(1) 疾病预防/治疗暗示即 misbranded（pdf-page 67）。≥2 处。
- 可回答的新问题：包装上的心形符号是否必然构成健康声称？品牌名含「heart」但产品与心脏病无关，是否落入 § 101.14？必需营养素缺乏症相关表述为何不受 § 101.14 管辖？
- 建议归属子卡：声称闸门

### CAND-PR-27: 显著科学共识（SSA）是 FDA 授权健康声称的效力门槛
- 条款出处：〔§ 101.14〕〔§ 101.70〕〔§ 101.73〕+ pdf-page 207 / 291 / 297
- 原文引用（英文逐字，≤100 词/段）：
> FDA will promulgate regulations authorizing a health claim only when it determines, based on the totality of publicly available scientific evidence (including evidence from well-designed studies conducted in a manner which is consistent with generally recognized scientific procedures and principles), that there is significant scientific agreement, among experts qualified by scientific training and experience to evaluate such claims, that the claim is supported by such evidence.
> The summary must establish that, based on the totality of publicly available scientific evidence (including evidence from well-designed studies conducted in a manner which is consistent with generally recognized scientific procedures and principles), there is significant scientific agreement among experts qualified by scientific training and experience to evaluate such claims, that the claim is supported by such evidence.
- 原则陈述：§ 101.14(c) 规定 FDA 仅在「基于全部公开可得科学证据、且合格专家之间存在 significant scientific agreement（SSA）支持该声称」时才制定授权法规，这是健康声称从「请愿」升格为「subpart E 授权」的效力门槛。§ 101.70 的请愿「Summary of scientific data」段以几乎逐字相同的句式要求请愿人证明 SSA，说明门槛在请愿端与授权端对称。因此企业自行判断「有科学支持」不能替代 FDA 的 SSA 认定；未达 SSA 或未获 subpart E 授权的声称不得使用（§ 101.71 负面清单、§ 101.14(d)(2)）。证据口径是「totality of publicly available scientific evidence」而非单篇研究。
- 复现位置：§ 101.70 请愿科学数据摘要（pdf-page 291）；§ 101.73 已授权声称模型中的「there is significant scientific agreement among experts, qualified by training and experience」（pdf-page 297）；§ 101.14(d)(1) 达有效性要求后 FDA 才提议 subpart E 法规（pdf-page 207）；§ 101.71 未授权声称清单（pdf-page 295）；§ 101.14(b) 物质适格性（pdf-page 206）。≥2 处。
- 可回答的新问题：企业能否凭一篇 RCT 自行作出健康声称？SSA 与「substantial evidence」是否同一门槛？请愿被拒后产品能否继续用该声称？
- 建议归属子卡：声称闸门

### CAND-PR-28: disqualifying nutrient levels 以 RACC / 标签份量 / 50 g 为分母，任一超标即取消健康声称资格
- 条款出处：〔§ 101.14〕+ pdf-page 206
- 原文引用（英文逐字，≤100 词/段）：
> Disqualifying nutrient levels means the levels of total fat, saturated fat, cholesterol, or sodium in a food above which the food will be disqualified from making a health claim. These levels are 13.0 grams (g) of fat, 4.0 g of saturated fat, 60 milligrams (mg) of cholesterol, or 480 mg of sodium, per reference amount customarily consumed, per label serving size, and, only for foods with reference amounts customarily consumed of 30 g or less or 2 tablespoons or less, per 50 g.
- 原则陈述：§ 101.14(a)(4) 设「取消资格营养素水平」：总脂肪、饱和脂肪、胆固醇、钠任一超过阈值，食品即被取消作健康声称的资格。判据分母是三选一并列——per RACC、per label serving size，且仅对 RACC ≤30 g 或 ≤2 汤匙的食品再加 per 50 g；脱水食品以 as prepared 为准。§ 101.14(a)(4) 续文把 meal product（§ 101.13(l)）与主菜 product（§ 101.13(m)）的阈值提高，并允许 subpart E 设例外。该条把「RACC 是所有声称阈值共同分母」具体化（与 CAND-PR-33 联动）：脱离 RACC/份量口径谈「脂肪 13 g」没有意义。
- 复现位置：§ 101.14(a)(4) 续文「Any one of the levels, on a per reference amount customarily consumed, a per label serving size or ... per 50 g basis, will disqualify」（pdf-page 207）；§ 101.14(d)(2)(vi)(vii) 声称物质水平须足够低/高并以 RACC 为基准（pdf-page 208–209）；§ 101.83「except § 101.14(a)(4) with respect to the」的例外（pdf-page 326）；§ 101.13(l)(m) meal/main dish 定义（pdf-page 204–205）；§ 101.56(b) 相对声称以 per reference amount customarily consumed 比较（pdf-page 250）。≥2 处。
- 可回答的新问题：某食品脂肪 14 g/RACC 但 10 g/label serving，是否被取消资格？RACC 30 g 以下的食品为何要额外查 per 50 g？subpart E 的例外如何覆盖 disqualifying levels？
- 建议归属子卡：声称闸门

### CAND-PR-29: 已授权健康声称模型措辞逐条回引「§ 101.14 全部要求须满足」
- 条款出处：〔§ 101.72〕〔§ 101.73〕〔§ 101.74〕〔§ 101.75〕〔§ 101.76〕〔§ 101.77〕〔§ 101.78〕〔§ 101.79〕〔§ 101.80〕〔§ 101.81〕〔§ 101.82〕〔§ 101.83〕+ pdf-page 295–326
- 原文引用（英文逐字，≤100 词/段）：
> All requirements set forth in § 101.14 shall be met.
> General. All requirements set forth in § 101.14 shall be met, except § 101.14(a)(4) with respect to the
- 原则陈述：Subpart E 的每一条已授权健康声称（§ 101.72 钙/维生素D/骨质疏松、§ 101.73 膳食脂类与癌症、§ 101.74 钠与高血压、§ 101.75 饱和脂肪胆固醇与冠心病、§ 101.76/77/78 纤维果蔬、§ 101.79 叶酸、§ 101.80 非致龋甜味剂、§ 101.81 可溶性纤维、§ 101.82 大豆蛋白、§ 101.83 植物甾醇）都在其 (c)(1) 或「General」款以「All requirements set forth in § 101.14 shall be met」回引通则，并另给模型措辞、适用条件、 disqualifying 例外。因此「用 subpart E 授权声称」不等于「绕过 § 101.14」：适格性、SSA、disqualifying levels、一般标签要求仍全部适用。少数条款（如 § 101.76 raw fruit、§ 101.80、§ 101.83）以「except」明文列出对 § 101.14 特定款的偏离，偏离必须逐字读出、不得泛化。
- 复现位置：§ 101.72(c)(1)（pdf-page 296）、§ 101.73(c)(1)（pdf-page 298）、§ 101.74(c)(1)（pdf-page 300）、§ 101.75(c)(1)（pdf-page 302）、§ 101.76(c)(1)（pdf-page 304）、§ 101.77(c)(1)（pdf-page 306）、§ 101.78(c)(1)（pdf-page 309）、§ 101.79(c)(1)（pdf-page 311）、§ 101.80(c)(1)（pdf-page 314）、§ 101.81(c)(1)（pdf-page 318）、§ 101.82(c)(1)（pdf-page 323）、§ 101.83（pdf-page 326）均为同一句式复现，≥2 处且为全书最密集复现之一。
- 可回答的新问题：用了 § 101.72 的模型措辞是否还需逐项核 § 101.14？某条写「except § 101.14(a)(4)」时，其他 § 101.14 款是否仍适用？模型措辞能否由企业自行改写？
- 建议归属子卡：声称闸门

### CAND-PR-30: 健康声称/声称请愿是「任何利害关系人可提 → citizen petition → 书面批准」的程序闸门
- 条款出处：〔§ 101.70〕〔§ 101.69〕〔§ 101.108〕+ pdf-page 290 / 283 / 340
- 原文引用（英文逐字，≤100 词/段）：
> Any interested person may petition the Food and Drug Administration (FDA) to issue a regulation regarding a health claim.
> This section pertains to petitions for claims, expressed or implied, that:
> Any firm that intends to undertake a labeling experiment that requires exemptions from certain requirements of §§ 101.9 and 105.66 of this chapter should submit a written proposal
- 原则陈述：Part 101 把「创造新声称/新豁免」收拢为正式行政程序：§ 101.70(a) 任何 interested person 可就健康声称请愿，材料须含科学依据摘要（SSA，CAND-PR-27）、须以 citizen petition（§ 10.30）形式提交；§ 101.69(a) 对营养素含量声称请愿（含 expressed or implied、品牌名暗示声称）设同类入口，§ 101.69(b) 列三类请愿（新声称、同义词、品牌名暗示声称）。§ 101.108 把「标签实验所需豁免」也设为书面提案 + FDA 书面批准。共同规则是：企业不得自行创设声称或自行宣布豁免，未经授权/书面批准即使用将落入 § 101.71 未授权清单或被视为违规标签。
- 复现位置：§ 101.69(b)(1)(2)(3) 三类声称请愿（pdf-page 283–284）；§ 101.70(b)(c) 请愿纳入材料与 nonclinical 研究要求（pdf-page 291–292）；§ 101.108(c) citizen petition 与提交地址（pdf-page 341）；§ 101.108(d) FDA 书面批准才生效（pdf-page 341）；§ 101.71 未授权声称清单（pdf-page 295）；§ 101.14(d)(1)(2) 授权后才可用（pdf-page 207–208）。≥2 处。
- 可回答的新问题：企业能否先在市场测试一个自创声称再补请愿？请愿中的科学摘要与 § 101.14(c) 的 SSA 是什么关系？临时标签实验豁免口头同意是否有效？
- 建议归属子卡：声称闸门

### CAND-PR-31: 未授权健康声称以负面清单明示，清单之外仍须回 § 101.14 判断
- 条款出处：〔§ 101.71〕〔§ 101.14〕〔§ 101.70〕+ pdf-page 295 / 207 / 290
- 原文引用（英文逐字，≤100 词/段）：
> Health claims not authorized for foods in conventional food form or for dietary supplements of vitamins, minerals, herbs, or other similar substances: (a) Dietary fiber and cardiovascular disease. (b) Zinc and immune function in the elderly.
- 原则陈述：§ 101.71 以「claims not authorized」标题列出被 FDA 明确否决的健康声称（膳食纤维与心血管疾病、锌与老年人免疫功能），属负面清单式禁止。但清单不是授权清单——未列入 § 101.71 不代表可用：仍须满足 § 101.14 的适格性、SSA、disqualifying levels，且通常须有 subpart E 授权法规（§ 101.14(d)(2)）或经 § 101.70 请愿新授权。因此判断顺序是「先查 § 101.71 是否已否决 → 再查 subpart E 是否已授权 → 再核 § 101.14 全部要求」。把「不在负面清单」误读为「获准」是典型错误。
- 复现位置：§ 101.14(d)(2)「When FDA has adopted a regulation in subpart E ... firms may make claims」（pdf-page 208）；§ 101.14(c) SSA 门槛（pdf-page 207）；§ 101.70(a) 请愿入口（pdf-page 290）；§ 101.72–83 subpart E 正面授权模型（pdf-page 295–326）；§ 101.9(k)(1) 疾病关系信息仅可依 § 101.14 与 subpart E 提供（pdf-page 67）。≥2 处。
- 可回答的新问题：「不在 § 101.71 清单上」是否等于可用该健康声称？被否决的声称经新证据能否通过 § 101.70 复活？膳食补充剂与常规食品在 § 101.71 下是否同一标准？
- 建议归属子卡：声称闸门

### CAND-PR-32: Subpart D 逐词声称统一采用「may only be made ... if」三条件闸门
- 条款出处：〔§ 101.54〕〔§ 101.56〕〔§ 101.60〕〔§ 101.61〕〔§ 101.62〕〔§ 101.65〕+ pdf-page 247 / 250 / 253 / 257 / 260 / 272
- 原文引用（英文逐字，≤100 词/段）：
> General requirements. A claim using the term light or lite to describe a food may only be made on the label or in labeling of the food if: (1) The claim uses one of the terms defined in this section in accordance with the definition for that term; (2) The claim is made in accordance with the general requirements for nutrient content claims in § 101.13; and (3) The food is labeled in accordance with § 101.9 or § 101.10, where applicable.
> General requirements. A claim about the level of fat, fatty acid, and cholesterol in a food may only be made on the label or in the labeling of foods if:
- 原则陈述：Subpart D 对每一组逐词声称（good source/high/more/high potency § 101.54、light/lite § 101.56、calorie/sugar § 101.60、sodium/salt § 101.61、fat/fatty acid/cholesterol § 101.62、implied § 101.65）都用同构的「may only be made ... if」三条件闸门：① 用本节按定义词/定义作出；② 符合 § 101.13 营养素含量声称通则；③ 食品按 § 101.9/§ 101.10/§ 101.36 完成营养标签。三者是 cumu­lative（并列全满足），不是三选一。因此「达到阈值数值」只是条件①的一部分，单靠配方达标仍不能作出声称——若该产品本可豁免营养标签，则须先因声称而补全标签（CAND-PR-16）。§ 101.54 另有 RDI/DRV 口径与 (e) 款例外。
- 复现位置：§ 101.54(a)(1)(2)(3)（pdf-page 247）；§ 101.56(a)（pdf-page 250）；§ 101.60(a)（pdf-page 253）；§ 101.61(a)（pdf-page 257）；§ 101.62(a)(1)(2)(3)（pdf-page 260）；§ 101.65(a)(1)(2)(3)（pdf-page 272）；§ 101.67(a)(1) 黄油声称「complies with the requirements of § 101.13 and ... regulations in this subpart」（pdf-page 282）。≥2 处，为高频复现。
- 可回答的新问题：产品钠含量达标但未做营养标签，能否标「low sodium」？第③条件的「where applicable / as applicable」如何判定？某词未被 Subpart D 定义时能否按普通语义使用？
- 建议归属子卡：声称闸门

### CAND-PR-33: RACC（reference amount customarily consumed）是所有声称阈值的共同分母
- 条款出处：〔§ 101.12〕〔§ 101.9〕〔§ 101.14〕〔§ 101.56〕〔§ 101.36〕+ pdf-page 83 / 21 / 206 / 250 / 228
- 原文引用（英文逐字，≤100 词/段）：
> The following reference amounts shall be used as the basis for determining serving sizes for specific products:
> Disqualifying nutrient levels means the levels of total fat, saturated fat, cholesterol, or sodium in a food above which the food will be disqualified from making a health claim. These levels are 13.0 grams (g) of fat, 4.0 g of saturated fat, 60 milligrams (mg) of cholesterol, or 480 mg of sodium, per reference amount customarily consumed, per label serving size
> If the food derives 50 percent or more of its calories from fat, its fat content is reduced by 50 percent or more per reference amount customarily consumed compared to an appropriate reference food as specified in § 101.13(j)(1); or
- 原则陈述：RACC 是贯穿 Part 101 的「共同分母」：§ 101.12(b) 把它定为 serving size 的基础（→ § 101.9(b) → 所有营养数值按份申报）；§ 101.14(a)(4) 的 disqualifying levels 以 per RACC / per label serving size /（小 RACC 时）per 50 g 判定；§ 101.56(b)、§ 101.54、§ 101.60–62 的相对声称（reduced / light / more）以「per reference amount customarily consumed compared to an appropriate reference food」比较；§ 101.14(d)(2)(vi)(vii) 健康声称的物质水平也以 RACC 为基准。因此任何声称阈值的合规计算都必须先锁定该产品的 RACC 与对应的 label serving size，脱离分母谈「13 g 脂肪」「减少 50%」无效；§ 101.14(d)(2)(vi)(A) 还规定 label serving 与 RACC 不一致时须附说明。§ 101.12 表格数值为不可逐字引用区，本候选只引 prose 规则与回引关系。
- 复现位置：§ 101.9(b)(1)(2) serving 由 RACC 推导（pdf-page 21）；§ 101.36(b)(1)(i) 补充剂回引 § 101.12(b) Table 2（pdf-page 228）；§ 101.14(a)(4) disqualifying 三分母（pdf-page 206）；§ 101.56(b)(1)(2) light 相对声称 per RACC（pdf-page 250）；§ 101.13(j)(1) reference food 比较基准（pdf-page 203）；§ 101.14(d)(2)(vi)(A) RACC 与 label serving 不一致时须说明（pdf-page 209）；§ 101.45(a)(2) 生鲜自愿标签回引 § 101.9(b)(c)（pdf-page 245）。≥2 处，为跨域最核心复现。
- 可回答的新问题：「脂肪减少 50%」是相对 RACC、每份还是每 100 g？label serving 与 RACC 不同时，健康声称如何标注？小 RACC 食品为何要额外按 per 50 g 判定 disqualifying？
- 建议归属子卡：声称闸门

### CAND-PR-34: 声称请愿可请求「新声称 / 同义词 / 品牌名暗示声称」三类，且明示覆盖 expressed or implied
- 条款出处：〔§ 101.69〕〔§ 101.13〕+ pdf-page 283 / 199
- 原文引用（英文逐字，≤100 词/段）：
> This section pertains to petitions for claims, expressed or implied, that: (1) Characterize the level of any nutrient which is of the type required to be in the label or labeling of food by section 403(q)(1) or (q)(2) of the Federal Food, Drug, and Cosmetic Act (the act); and
> Petitions included in this section are: (1) Petitions for a new (heretofore unauthorized) nutrient content claim;
- 原则陈述：§ 101.69(a) 把请愿对象锚定到 FD&C Act § 403(q)(1)/(q)(2) 要求申报的营养素水平，且明写「expressed or implied」，并排除 § 403(r)(5)(A)–(C) 已豁免的声称。§ 101.69(b) 列三类请愿：新（此前未授权）营养素含量声称、与已定义词一致的同义词、在品牌名中使用暗示声称。因此「品牌名里藏一个暗示声称」不是法外空间，而须走请愿程序；同时也说明立法者预期「同义词」「暗示」与「明示定义词」受同一套授权逻辑约束。与 § 101.13(b)(4) 的「不误导的拼写变体（hi/lo）」不同：后者是法规已容许的微小变体，前者须请愿。
- 复现位置：§ 101.69(b)(2)(3) 同义词请愿、品牌名暗示声称请愿（pdf-page 284）；§ 101.13(b)(4) 拼写变体（pdf-page 199）；§ 101.13(b)(2) 暗示声称定义（pdf-page 199）；§ 101.70 健康声称请愿（pdf-page 290）；§ 101.14(a)(1) 品牌名含「heart」即可能构成健康声称（pdf-page 206）。≥2 处。
- 可回答的新问题：把「low fat」写成「lo fat」是否需要请愿？品牌名「HeartHealthy」要上市须走 § 101.69 还是 § 101.70？§ 403(r)(5)(A)–(C) 豁免的声称有哪些？
- 建议归属子卡：声称闸门

### CAND-PR-35: 未巴氏 / 未达 5-log 处理果汁必须带警示声明，且警示有显著性与版式硬要求
- 条款出处：〔§ 101.17〕+ pdf-page 214
- 原文引用（英文逐字，≤100 词/段）：
> processed in the manner described in paragraph (g)(7) of this section, shall bear the following warning statement: WARNING: This product has not been pasteurized and, therefore, may contain harmful bacteria that can cause serious illness in children, the elderly, and persons with weakened immune systems.
> The warning statement required by paragraph (g)(2) of this section shall appear prominently and conspicuously on the information panel or on the principal display panel of the label of the container.
- 原则陈述：§ 101.17(g)(2) 规定：未按 (g)(7) 方式处理（即未达 5-log / HACCP 等效）的果汁，须逐字载明未巴氏警示，点名儿童、老年人、免疫低下者风险。版式义务独立且硬性：须显著出现在信息面板或 PDP、(g)(5)「WARNING」大写加粗、(g)(6) 在标签上时须用细线加框、(g)(4) 位置限定。(g)(3) 给出例外：不面向零售消费者、仅供进一步加工/在他处贴标或再包装的果汁可不带警示，但未处理事实须随货文件披露。这是「标签义务」层，与 CAND-PR-36 的「工艺义务」层必须分开。
- 复现位置：§ 101.17(g)(3) 非零售果汁例外与随货披露（pdf-page 214）；§ 101.17(g)(4)(5)(6) 位置/大写加粗/加框（pdf-page 214）；§ 101.17(a)(1) 自加压容器 WARNING（pdf-page 211）；§ 101.17(h)(2) 壳蛋声明显著性（pdf-page 214）；§ 101.2(b) 把 § 101.17 收进 PDP/信息面板清单（pdf-page 3）。≥2 处。
- 可回答的新问题：警示只印在随附箱单而非瓶身是否合规？「WARNING」用小写或细体是否违规？仅供餐饮后厨进一步加工的桶装果汁能否免警示？
- 建议归属子卡：特定品类与警示

### CAND-PR-36: 果汁警示声明不替代 Part 120 / HACCP 的 5-log 工艺义务（两层义务接口）
- 条款出处：〔§ 101.17〕+ pdf-page 214
- 原文引用（英文逐字，≤100 词/段）：
> The requirements in this paragraph (g) shall not apply to a juice that has been processed in a manner that will produce, at a minimum, a reduction in the pertinent microorganism for a period at least as long as the shelf life of the product when stored under normal and moderate abuse conditions, of the following magnitude:
> (A) A 5-log (i.e., 100,000-fold) reduction; or (B) A reduction that is equal to, or greater than, the criterion established for process controls by any final regulation requiring the application of Hazard Analysis and Critical Control Point (HACCP) principles to the processing of juice.
- 原则陈述：§ 101.17(g)(7)(i) 是「标签义务 ↔ 工艺义务」的接口条款：(g) 的警示要求不适用于「已按能产生至少 5-log（10 万倍）目标微生物削减、或达到任何要求对果汁加工应用 HACCP 原则的最终法规所定工艺控制判据」处理的果汁，(g)(7)(ii) 把 pertinent microorganism 定义为「最可能出现、最具公共卫生意义、最具抗性」的微生物。关键结论：贴了警示 ≠ 履行了 5-log / Part 120 § 120.24 的工艺控制义务；反之做了 5-log 处理则免除的是「警示标签义务」，不是免于 HACCP。两条义务分别挂在 Part 101（标签）与 Part 120（工艺），不得互引条款号替代。本条 (B) 项以「any final regulation ... HACCP」把接口指向果汁 HACCP 最终规则。
- 复现位置：§ 101.17(g)(2) 警示义务本体（pdf-page 214）；§ 101.17(g)(3) 未处理果汁须随货披露（pdf-page 214）；§ 101.17(g)(7)(ii) pertinent microorganism 定义（pdf-page 214）；§ 101.17(h) 壳蛋 SAFE HANDLING INSTRUCTIONS 同为标签义务、不替代加工卫生（pdf-page 214）；§ 101.100(a)(4) 亚硫酸盐阈值属另一义务（pdf-page 336）。条款内 (2)/(3)/(7) 相互复现；跨条款以「标签义务 vs 工艺义务」结构复现于 § 101.17(a)/(h)。≥2 处。
- 可回答的新问题：已贴警示的未巴氏果汁是否仍须执行 5-log / Part 120？做了 5-log 是否连 HACCP 记录都免了？(B) 项的「final regulation」指哪一部？
- 建议归属子卡：特定品类与警示

### CAND-PR-37: 壳蛋须载明 SAFE HANDLING INSTRUCTIONS，位置与加粗受管
- 条款出处：〔§ 101.17〕+ pdf-page 214
- 原文引用（英文逐字，≤100 词/段）：
> The label of all shell eggs, whether in intrastate or interstate commerce, shall bear the following statement: SAFE HANDLING INSTRUCTIONS: To prevent illness from bacteria: keep eggs refrigerated, cook eggs until yolks are firm, and cook foods containing eggs thoroughly.
> The label statement required by paragraph (h)(1) of this section shall appear prominently and conspicuously, with the words “SAFE HANDLING INSTRUCTIONS” in bold type, on the principal display panel, the information panel, or on the inside of the lid of egg cartons.
- 原则陈述：§ 101.17(h)(1) 对「所有壳蛋，无论州内或州际商业」设统一强制声明（冷藏、蛋黄煮至凝固、含蛋食品彻底加热），(h)(2) 规定须显著、SAFE HANDLING INSTRUCTIONS 加粗，位置限 PDP、信息面板或蛋盒盖内侧三选一。适用范围「whether in intrastate or interstate commerce」把纯州内销售也纳入，是少数明示覆盖 intrastate 的标签义务。本条同为标签义务层，与未巴氏果汁警示（CAND-PR-35/36）同属 § 101.17 的 warning/notice/safe handling 体系；不替代养殖、加工、冷藏等生产过程义务。
- 复现位置：§ 101.17(a) 自加压容器警示（pdf-page 211）；§ 101.17(g)(4)(5)(6) 果汁警示显著性与版式（pdf-page 214）；§ 101.2(b) 把 § 101.17 收进 PDP/信息面板清单（pdf-page 3）；§ 101.100(d) 未巴氏蛋制品用于酸性调料的相关条款（pdf-page 337）；§ 101.15(a) 显著性总纲（pdf-page 210）。≥2 处。
- 可回答的新问题：仅州内销售的农场鸡蛋是否须带该声明？声明印在蛋盒盖内侧是否满足「显著」？加粗要求只覆盖标题词还是整段？
- 建议归属子卡：特定品类与警示

### CAND-PR-38: gluten-free 的 20 ppm 判据由 § 101.91 独立定义，含成分与不可避免残留两路
- 条款出处：〔§ 101.91〕+ pdf-page 330
- 原文引用（英文逐字，≤100 词/段）：
> processed to remove gluten (e.g., wheat starch), if the use of that ingredient results in the presence of 20 parts per million (ppm) or more gluten in the food (i.e., 20 milligrams (mg) or more gluten per kilogram (kg) of food); or
> Any unavoidable presence of gluten in the food bearing the claim in its labeling is below 20 ppm gluten (i.e., below 20 mg gluten per kg of food).
- 原则陈述：§ 101.91(a)(3) 把「gluten-free」定义为两路并列：① 食品不含任何含麸质谷物、或未经去麸质处理的衍生物、或经去麸处理但使用该配料导致食品中麸质 ≥20 ppm 者；或本身不含麸质；② 任何不可避免的麸质残留须低于 20 ppm（= 20 mg/kg）。两路都用同一 20 ppm 阈值，但对象不同（配料导致的存在量 vs 不可避免残留）。§ 101.91 另对发酵/水解食品设合规方法要求（§ 101.91(c)）、对「no gluten / free of gluten / without gluten」同等对待（(b)(2)）、并规定与「wheat」标注的交互（(b)(3)）。该 20 ppm 是 § 101.91 的声称判据，与亚硫酸盐 10 ppm（CAND-PR-40）分属不同条款、不同判据，不得混算。
- 复现位置：§ 101.91(a)(1)(2) 含麸质谷物/麸质定义（pdf-page 330）；§ 101.91(b)(1)(2) 不符即 misbranded（pdf-page 330）；§ 101.91(b)(3)「Contains wheat」交互（pdf-page 330）；§ 101.91(c) 发酵/水解食品记录与检测方法（pdf-page 331）；§ 101.91(a)(3) 续文「20 ppm gluten」第二次出现（pdf-page 331）。≥2 处。
- 可回答的新问题：某配料经去麸处理后残留 15 ppm，能否标 gluten-free？发酵酱油类如何证明符合 20 ppm？「no gluten」与「gluten-free」是否同一判据？
- 建议归属子卡：特定品类与警示

### CAND-PR-39: gluten-free 及相关同义声称不符要求即 deemed misbranded
- 条款出处：〔§ 101.91〕〔§ 101.18〕+ pdf-page 330 / 219
- 原文引用（英文逐字，≤100 词/段）：
> A food that bears the claim “gluten-free” in its labeling and fails to meet the requirements of paragraph (a)(3) of this section and, if applicable, paragraphs (c)(2) through (4) of this section will be deemed misbranded.
> A food that bears the claim “no gluten,” “free of gluten,” or “without gluten” in its labeling and fails to meet the requirements of paragraph (a)(3) of this section and, if applicable, paragraphs (c)(2) through (4) of this section will be deemed misbranded.
- 原则陈述：§ 101.91(b)(1)(2) 把不符 § 101.91(a)(3)（及适用时 (c)(2)–(4)）的 gluten-free / no gluten / free of gluten / without gluten 声称直接定性为「deemed misbranded」，即自执行（self-executing）的 misbranding 后果，不待另行认定。§ 101.91(b)(3) 进一步规定：配料表或「Contains wheat」声明中出现「wheat」却又标 gluten-free 时，须按 (b)(2) 处理（除非 wheat 一词经 § 101.91 要求的说明澄清）。这把 § 101.91 与 § 101.4 配料表、FALCPA 的 wheat 标注连成一条链。该后果与 § 101.9(k)、§ 101.11(f) 同属 misbranding 执法钩子（CAND-PR-47）。
- 复现位置：§ 101.91(b)(3) wheat 交互（pdf-page 330）；§ 101.9(k) 营养标签 misbranded（pdf-page 67）；§ 101.11(f) 标准菜单项 misbranded（pdf-page 82）；§ 101.18(a)(b)(c) misbranding 总纲（pdf-page 219）；§ 101.14/§ 101.13 声称不合规的执法路径（pdf-page 199/206）。≥2 处。
- 可回答的新问题：标「without gluten」但检出 25 ppm，执法依据是否仍须回到 § 403？配料表有「wheat」又标 gluten-free 时如何补救？「deemed misbranded」是否还需证明误导？
- 建议归属子卡：豁免与效力层

### CAND-PR-40: gluten-free 20 ppm（§ 101.91）与亚硫酸盐 10 ppm（§ 101.100）是不同条款的不同判据，不得混算
- 条款出处：〔§ 101.91〕〔§ 101.100〕+ pdf-page 330 / 336
- 原文引用（英文逐字，≤100 词/段）：
> Any unavoidable presence of gluten in the food bearing the claim in its labeling is below 20 ppm gluten (i.e., below 20 mg gluten per kg of food).
> A detectable amount of sulfiting agent is 10 parts per million (ppm or mg/kg) or more of the sulfite in the finished food.
- 原则陈述：两个 ppm 阈值分属完全不同的制度：§ 101.91 的 20 ppm 是「gluten-free 声称」的合规判据（针对麸质、作用于声称、不符即 misbranded）；§ 101.100(a)(4) 的 10 ppm 是「incidental additives 豁免」语境下判定亚硫酸盐是否「无可检测量、因而可视为不显著、免于配料申报」的阈值，且合规须用指定方法（LC-MS/MS 或 AOAC 990.28）测定。前者管「能不能标 gluten-free」，后者管「亚硫酸盐要不要进配料表」，物质、条款、法律后果、检测方法全不同。§ 101.100(a)(4) 明列五种亚硫酸盐制剂。因此「都是 ppm、都约 10–20」不构成任何互相援引或数值换算的依据；同理，§ 101.17(g) 的 5-log、§ 101.1 的 40% 圆柱面积、§ 101.17(a) 的 120 °F 都是各自条款的独立判据。
- 复现位置：§ 101.100(a)(3) incidental additives / processing aids 豁免框架（pdf-page 335）；§ 101.100(a)(4) 五种亚硫酸盐与两种检测方法（pdf-page 336）；§ 101.91(b)(1)(2) 不符即 misbranded（pdf-page 330）；§ 101.22/§ 101.4(b) 防腐剂声明规则（pdf-page 219/7）；§ 101.17(g)(7) 5-log 为工艺判据、§ 101.1 40% 为面积判据（pdf-page 214/3），作为「数值判据不可混算」的旁证。≥2 处。
- 可回答的新问题：某食品同时标 gluten-free 又含亚硫酸盐，两个 ppm 能否一起算进「污染物总量」？亚硫酸盐 10 ppm 以下是否等于可标 gluten-free？用 AOAC 990.28 测麸质是否合规？
- 建议归属子卡：特定品类与警示

### CAND-PR-41: 膳食补充剂 403(r)(6) 声须附法定免责声明，且位置/符号/多条声明规则受管
- 条款出处：〔§ 101.93〕+ pdf-page 332
- 原文引用（英文逐字，≤100 词/段）：
> The requirements in this section apply to the label or labeling of dietary supplements where the dietary supplement bears a statement that is provided for by section 403(r)(6) of the Federal Food, Drug, and Cosmetic Act (the act), and the manufacturer, packer, or distributor wishes to take advantage of
> This statement has not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.
- 原则陈述：§ 101.93 适用于「带有 FD&C Act § 403(r)(6) 结构/功能声明、且厂商希望援引 § 201(g)(1)(C) 豁免（不因该声明被当作药品）」的膳食补充剂 label 或 labeling。代价是必须逐字附免责声明：单条声明用「This statement has not been evaluated...not intended to diagnose, treat, cure, or prevent any disease」，多条声明用复数版或每条各附。§ 101.93(d) 规定位置：须紧邻该声明、无插入材料，或用符号（星号）把声明与免责声明链接。§ 101.93(a) 还要求首次上市后 30 天内向 FDA 提交通知（含声明文本、配料/补充剂名称、责任人签署并证明真实不误导）。因此免责声明不是可选营销话术，而是换取 § 403(r)(6) 待遇的法定对价。
- 复现位置：§ 101.93(a)(1)(2)(3) 30 天通知、内容、签署与 substantiation（pdf-page 332）；§ 101.93(c)(2) 多条声明的复数免责声明（pdf-page 332）；§ 101.93(d) 位置与符号链接（pdf-page 332）；§ 101.36 补充剂营养标签体系（pdf-page 228）；§ 101.14(a)(5)/§ 101.9(k)(1) 疾病关系声称的边界（pdf-page 207/67）；§ 101.69(a) 排除 § 403(r)(5)(A)–(C) 豁免的声称（pdf-page 283）。≥2 处。
- 可回答的新问题：只印了结构/功能声明却漏了免责声明，是否失去 § 403(r)(6) 待遇？多条声明能否共用一个带星号的免责声明？30 天通知逾期是否影响已上市产品？
- 建议归属子卡：特定品类与警示

### CAND-PR-42: 「fresh」等用语仅当暗示「未加工/未防腐」时才受 § 101.95 约束
- 条款出处：〔§ 101.95〕+ pdf-page 334
- 原文引用（英文逐字，≤100 词/段）：
> However, the use of the term “fresh” on labels or labeling is not subject to the requirements of paragraph (a) of this section if the term does not suggest or imply that a food is unprocessed or unpreserved.
> The term “fresh,” when used on the label or in labeling of a food in a manner that suggests or implies that the food is unprocessed, means that the food is in its raw state and has not been frozen or subjected to any form of thermal processing or any other form of preservation, except as provided in paragraph (c) of this section.
- 原则陈述：§ 101.95 的管辖触发是「用语是否 suggest or imply 食品未加工/未防腐」，而非字面是否出现「fresh」。开篇明文举例：巴氏杀菌全脂牛奶用「fresh」不暗示未加工（消费者普遍知道牛奶几乎都经巴氏杀菌），故不受 (a) 款约束；但经巴氏杀菌或含巴氏配料的意面酱用「fresh」则暗示未加工/未防腐，落入 (a) 款。落入后 (a) 定义「fresh」为原生状态、未冷冻、未经任何热处理或任何其他防腐（(c) 款例外除外）；不受本条约束的用法仍受 FD&C Act § 403(a) 一般误导规则管辖。§ 101.95 还覆盖 brand name 与 sensory modifier 中的用语，并把「fresh frozen/frozen fresh」单独定义（快速冷冻、可经 blanching）。这是「语境决定受管与否」的又一处具体化（参 CAND-PR-24）。
- 复现位置：§ 101.95 开篇「including use in a brand name and use as a sensory modifier」与「governed by the provisions of 403(a)」（pdf-page 334）；§ 101.95(b) fresh frozen 定义（pdf-page 334）；§ 101.95(c) 限制与例外（pdf-page 335）；§ 101.13(b)(2) 暗示声称的语境判准（pdf-page 199）；§ 101.14(a)(1) 品牌名/符号构成健康声称（pdf-page 206）；§ 101.30(a) 表征触发（pdf-page 224）。≥2 处。
- 可回答的新问题：「fresh」用在巴氏牛奶上是否一律合规？「fresh frozen」经焯水（blanching）后能否保留该用语？不受 § 101.95 约束的「fresh」是否就完全无风险？
- 建议归属子卡：特定品类与警示

### CAND-PR-43: 黄油声称偏离法定成分须「最小必要」，否则依 § 402(b) 视为 adulterated
- 条款出处：〔§ 101.67〕+ pdf-page 282
- 原文引用（英文逐字，≤100 词/段）：
> Deviations from the ingredient provisions of 21 U.S.C. 321a must be the minimum necessary to achieve similar performance characteristics as butter as produced under 21 U.S.C. 321a, or the food will be deemed to be adulterated under section 402(b) of the act.
- 原则陈述：§ 101.67 允许对黄油作营养素含量声称，但以 § 101.13、Subpart D 相应定义、以及 21 U.S.C. 321a 法定黄油标准为界。(b) 款把「偏离法定成分」限缩为「为达到与法定黄油相似性能所必需的最小偏离」，否则食品依 FD&C Act § 402(b) 被认定为 adulterated（掺假）——这是 Part 101 中少数明文挂 § 402 而非 § 403 的位置。配套义务：性能须相似（物理、感官、功能、货架期），有显著差异且实质限制用途时须在标签声明（如「not recommended for baking purposes」）并符合 § 101.13(d)，且产品至少须实质完成黄油的一项主要功能。§ 101.67(a)(1) 把脂肪削减百分比的计算基准锚到 321a 的 80% 乳脂要求，(a)(4) 要求偏离所赖的声称须作为 common or usual name 一部分的明示声称。
- 复现位置：§ 101.67(a)(1)(2)(3)(4) 四项条件与 80% 乳脂基准（pdf-page 282）；§ 101.67(b) 续文性能相似、差异声明、至少一项主要功能（pdf-page 283）；§ 101.13(d) 免责声明（pdf-page 199）；§ 101.3(e)(4) nutritionally inferior / imitation（pdf-page 6）；§ 101.14(a)(4) 另一处「deemed」式自执行后果对照（pdf-page 206）。≥2 处。
- 可回答的新问题：减脂黄油偏离 321a 配方后，标签合规是否足以避免 adulterated？「最小必要」由谁举证？性能差异声明能否补救 § 402(b) 掺假认定？
- 建议归属子卡：特定品类与警示

### CAND-PR-44: 豁免必须指明「免的是哪一条义务」，不同豁免对象不可互替
- 条款出处：〔§ 101.9〕〔§ 101.100〕〔§ 101.108〕〔§ 101.36〕+ pdf-page 58 / 335 / 340 / 231
- 原文引用（英文逐字，≤100 词/段）：
> The following foods are exempt from compliance with the requirements of section 403(i)(2) of the act (requiring a declaration on the label of the common or usual name of each ingredient when the food is fabricated from two or more ingredients).
> Any firm that intends to undertake a labeling experiment that requires exemptions from certain requirements of §§ 101.9 and 105.66 of this chapter should submit a written proposal
> A statement of the sections of the regulations for which an exemption is sought.
- 原则陈述：Part 101 的豁免都是「特定义务的豁免」，援引时必须精确指出免的是哪一条：§ 101.9(j) 免的是 § 101.9 营养标签义务、§ 101.36(h) 免的是 § 101.36 补充剂营养标签义务、§ 101.100(a) 免的是 FD&C Act § 403(i)(2) 配料表义务、§ 101.108 免的是 §§ 101.9/105.66 的特定要求且须在提案中「A statement of the sections of the regulations for which an exemption is sought」逐条列明。因此「有豁免」不是笼统状态：拿到配料表豁免不等于免营养标签，拿到小企业营养标签豁免不等于免声称规则。§ 101.108(d) 更强调「FDA-approved exemption to the specific regulation ... for that specific product」。Part 101 的标签义务豁免与 Part 117 的 qualified facility 等「主体豁免」是两套完全不同制度，不得互引。
- 复现位置：§ 101.9(j) 逐项营养标签豁免（pdf-page 58）；§ 101.36(h) 补充剂营养标签豁免（pdf-page 231）；§ 101.100(b) 零售店重包装对 § 403(e)(1) 名址等条文的逐项豁免（pdf-page 336）；§ 101.108(b)(9)(d) 指明所免条款与「specific regulation」（pdf-page 341）；§ 101.9(a)(3) 被豁免食品回复征集请求不破豁免（pdf-page 20）；§ 101.15(b) 空间不足豁免及其反跳条件（pdf-page 210）。≥2 处，为高频复现。
- 可回答的新问题：拿到 § 101.100 配料表豁免后能否连带免做 Nutrition Facts？§ 101.9(j) 小企业豁免能否援引到膳食补充剂？§ 101.108 提案未列明所免具体条款会怎样？
- 建议归属子卡：豁免与效力层

### CAND-PR-45: § 101.100 的豁免对象是 § 403(i)(2) 配料表要求，且多为附条件豁免
- 条款出处：〔§ 101.100〕〔§ 101.4〕+ pdf-page 335 / 7
- 原文引用（英文逐字，≤100 词/段）：
> The following foods are exempt from compliance with the requirements of section 403(i)(2) of the act (requiring a declaration on the label of the common or usual name of each ingredient when the food is fabricated from two or more ingredients).
> An assortment of different items of food, when variations in the items that make up different packages packed from such assortment normally occur in good packing practice and when such variations result in variations in the ingredients in different packages, with respect to any ingredient that is not common to all packages.
> Such exemption, however, shall be on the condition that the label shall bear, in conjunction with the names of such ingredients as are common to all packages, a statement (in terms that are as informative as practicable and that are not misleading) indicating by name other ingredients which may be present.
- 原则陈述：§ 101.100(a) 开篇即把豁免对象限定为 FD&C Act § 403(i)(2) 的「配料表（各配料通用/常用名）」要求，不是免整个标签。列举对象包括： assortment 中非共有配料（但须附带「可能含有的其他配料」说明）、零售店散装容器（须配料信息显著且 ≥1/4 英寸，或用柜台卡等）、incidental additives（无技术功能且含量不显著，含加工助剂、迁移物）、以及 § 101.100(a)(4) 的亚硫酸盐 10 ppm 阈值。§ 101.100(b) 另对零售店重包装食品逐项豁免 § 403(e)(1) 名址等条文。共同特征是「豁免 + 条件/替代披露」：免的是原义务，但常以另一种披露义务替代，条件不满足则豁免不成立。
- 复现位置：§ 101.4(a)(1)「except those ingredients exempted by § 101.100」回引（pdf-page 7）；§ 101.100(a)(2)(i)(ii) 散装替代披露（pdf-page 335）；§ 101.100(a)(3) incidental additives（pdf-page 335）；§ 101.100(a)(4) 亚硫酸盐 10 ppm（pdf-page 336）；§ 101.100(b)(1) 逐项列明所免条文（pdf-page 336）；§ 101.22/§ 101.4(b) 防腐剂声明（pdf-page 219/7）。≥2 处。
- 可回答的新问题：散装食品用柜台卡披露配料时字号要求是什么？incidental additive「无技术功能」由谁判定？§ 101.100 豁免能否覆盖营养标签或过敏原标注？
- 建议归属子卡：豁免与效力层

### CAND-PR-46: 临时标签实验豁免须书面提案 + FDA 书面批准，且逐条指明所免条款
- 条款出处：〔§ 101.108〕〔§ 101.100〕+ pdf-page 340 / 335
- 原文引用（英文逐字，≤100 词/段）：
> Any firm that intends to undertake a labeling experiment that requires exemptions from certain requirements of §§ 101.9 and 105.66 of this chapter should submit a written proposal containing a thorough discussion of each of the following information items that apply to the particular experiment:
> Approval for food labeling experiments will be given by FDA in writing. Foods labeled in violation of existing regulations will be subject to regulatory action unless an FDA-approved exemption to the specific regulation has been granted for that specific product.
- 原则陈述：§ 101.108 是「为开展经授权标签实验而设的临时豁免」，程序要件密集：书面提案须含 (b)(1)–(9) 各项（测试版式、分类判据、店内材料、起止日期与承诺不超期、地理范围、效果测量机制、实验期间向消费者传达被豁免信息的替代方式、营养特性测定方法、以及 (b)(9)「A statement of the sections of the regulations for which an exemption is sought」），以 citizen petition（§ 10.30）提交至 Dockets Management Staff。(d) 款给出效力规则：批准须 FDA 书面作出；在获得针对「该具体产品、该具体法规」的 FDA 批准豁免之前，违反现行法规的标签仍受监管行动。因此口头同意、行业惯例、自行试运行都不产生豁免。§ 101.108(a) 用 `encouraged`、§ 101.108(b) 用 `should`，但 (d) 用 `will be subject to regulatory action` 把未批准后果硬化。
- 复现位置：§ 101.108(a) 鼓励在 FDA 协作下实验（pdf-page 340）；§ 101.108(b)(1)–(9) 提案九项（pdf-page 340–341）；§ 101.108(c) citizen petition 与提交方式（pdf-page 341）；§ 101.70(a) 健康声称请愿（pdf-page 290）；§ 101.69(b) 声称请愿（pdf-page 283）；§ 101.44/§ 101.100 其他「列举式豁免」对照（pdf-page 244/335）。≥2 处。
- 可回答的新问题：实验期超过提案结束日期但 FDA 未回复，能否继续？提案写了「豁免营养标签」但未列具体条款是否足够？书面批准覆盖同企业其他产品吗？
- 建议归属子卡：豁免与效力层

### CAND-PR-47: misbranding（§ 403 系）与 adulteration（§ 402 系）是两条独立执法钩子
- 条款出处：〔§ 101.9〕〔§ 101.11〕〔§ 101.67〕〔§ 101.91〕〔§ 101.18〕+ pdf-page 67 / 82 / 282 / 330 / 219
- 原文引用（英文逐字，≤100 词/段）：
> A food labeled under the provisions of this section shall be deemed to be misbranded under sections 201(n) and 403(a) of the act if its label or labeling represents, suggests, or implies:
> Deviations from the ingredient provisions of 21 U.S.C. 321a must be the minimum necessary to achieve similar performance characteristics as butter as produced under 21 U.S.C. 321a, or the food will be deemed to be adulterated under section 402(b) of the act.
- 原则陈述：Part 101 的不合规后果分挂两条互不替代的 FD&C Act 钩子：misbranding 主要连 § 403（及 § 201(n) 的 labeling 定义）——§ 101.9(k) 营养标签的疾病暗示、§ 101.11(f) 标准菜单项、§ 101.91(b) gluten-free 不符、§ 101.18 虚假/误导表述、§ 101.15(a) 显著性连 § 403(f)、§ 101.100 连 § 403(i)(2)；adulteration 连 § 402——§ 101.67(b) 黄油成分偏离即明写「deemed to be adulterated under section 402(b)」。两者触发事实不同：前者是「标签/标示内容不实或不合规」，后者是「食品本身成分/状态不合规」。因此标签写对并不洗掉 § 402 掺假，反之成分达标也不豁免 § 403 标示义务。判断任一违规时必须先选对钩子，不能把 § 101.67 的 § 402(b) 读成 misbranding，也不能把 § 101.91 的 misbranded 读成 adulteration。
- 复现位置：§ 101.11(f) §§ 201(n)、403(a)、403(f)、403(q)（pdf-page 82）；§ 101.91(b)(1)(2) deemed misbranded（pdf-page 330）；§ 101.18(a)(b)(c) misbranding 总纲（pdf-page 219）；§ 101.15(a) § 403(f) 显著性（pdf-page 210）；§ 101.9(k)(1) 仅可依 § 101.14/subpart E 提供疾病关系信息（pdf-page 67）；§ 101.100(a) § 403(i)(2)（pdf-page 335）；§ 101.67(a)(3)(b) § 402(b)（pdf-page 282）。≥2 处。
- 可回答的新问题：减脂黄油标签完全合规但成分偏离 321a，是否仍被查处？gluten-free 检出 25 ppm 走的是哪一条执法钩子？把 § 101.67(b) 的后果写成「misbranded」错在哪里？
- 建议归属子卡：豁免与效力层

### CAND-PR-48: 法规正文层（联邦法规、具法律约束力）与 FDA 指南 / 检查程序层须分层引用
- 条款出处：〔§ 101.9〕〔§ 101.108〕〔§ 101.71〕（各条末 FR citation / 前言 Authority / Source 行）+ pdf-page 20 / 340 / 295 / 1 / 3
- 原文引用（英文逐字，≤100 词/段）：
> Authority: 15 U.S.C. 1453, 1454, 1455; 21 U.S.C. 321, 331, 342, 343, 348, 371; 42 U.S.C. 243, 264, 271.
> Source: 42 FR 14308, Mar. 15, 1977, unless otherwise noted.
> This content is from the eCFR and is authoritative but unofficial
- 原则陈述：本转换件是「法规正文层」——由国会授权法源（21 U.S.C. 等）支撑、以 Federal Register 最终规则 promulgated、具法律约束力的联邦法规（21 CFR Part 101），eCFR 快照为「authoritative but unofficial」，不是正式 GPO 年度编纂版。其条文以 `shall` / `may not` / `unless` 设定义务，并以各条末尾的 `[XX FR ...]` FR citation 记录修订出处。在本技能包内，Part 101 是第七套独立编号〔§ 101.xxx〕，与 Part 108/113/114/117/120/123 并列，各管各自义务、不是上下位或新旧替代。效力栈为：法规正文（七套编号，shall 义务层）＞ FDA 指南（should 建议层）＞ CPGM/CP/IOM 检查程序（检查员视角、不创设企业义务）；Part 101 内部又含 `shall` 强制层（§ 101.9）、`should` 自愿指南层（§ 101.42–45）、`urges/encouraged` 倡导层（§ 101.42/§ 101.108(a)）。引用时必须带效力层标签，禁止把指南或检查程序写成「21 CFR 101.x（指南）」，也禁止用 `should` 层创设 `shall` 义务。
- 复现位置：§ 101.9/§ 101.11/§ 101.13 等条的 `[79 FR 71253, Dec. 1, 2014]` 式 FR citation（pdf-page 68/82/68）；§ 101.108 末 `[48 FR 15240, Apr. 8, 1983, as amended at ... 88 FR 17718, Mar. 24, 2023]`（pdf-page 341）；§ 101.71 末 `[58 FR 2534, Jan. 6, 1993, as amended at ...]`（pdf-page 295）；各条 Authority/FR citation 逐条复现；§ 101.42/§ 101.45 的 `urges/should` 与 § 101.9 的 `shall` 形成层内对照（pdf-page 243/244/20）。≥2 处。
- 可回答的新问题：把 FDA 行业指南的「should」写成企业「shall」义务错在哪？eCFR 快照与 GPO 年度版冲突时以何为准？检查程序（CPGM）能否作为对企业处罚的直接法源？Part 101 与 Part 117 的条款号能否互引替代？
- 建议归属子卡：豁免与效力层
