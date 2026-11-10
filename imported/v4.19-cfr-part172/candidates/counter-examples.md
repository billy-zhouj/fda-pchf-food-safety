# 候选池：反例提取器 | 来源 21 CFR Part 172 eCFR 2026-11-05 | 全量扫描 chunk-01..04

> 主代理顺序执行（并行子代理被上游限流）。扫描覆盖：chunk-01–04，154/154 条款；以 `shall not be construed` / `except` / `does not preclude` / `only` / `Do.` / `not for` / `in combination` / `specified foods` / `as measured in` / `incorporated by reference` 等禁止性·例外·限定锚点 Grep 命中后回读。
> 纪律：引用逐字来自 `source-cfr-part172-2026.md`（归一化空白后可命中）；16 张重建表格数值、§172.510/§172.515 名录、IBR 外部文件内容属**不可逐字引用区**，本池只写「存在与边界」，不引其内部数值与版式。
> 条款出处统一为〔§ 172.xxx〕；pdf-page N 按 `<!-- pdf-page N -->` 标记核定。建议归属子卡为五选一。

---

### CAND-CE-01: 以为「有条款 + 不超限」就等于一切合规
- 错误说法（一句）：只要该物质在 Part 172 里有条款、且用量没超表列数值，这个产品就合规了。
- 正确判定（3–6 句，写清依据与边界）：§172.5(b) 明文否定了这一推论——「存在许可法规」不得被解释为**免除**该物质受本法其他任何条款约束的义务。Part 172 只管「物质 × 用途 × 用量 × 规格」这一层：标签内容归〔§ 101〕、过程预防控制归〔§ 117〕、包装材料归间接添加剂部分（本包未收）。此外 §172.5(a) 的 GMP 双重限制本身也叠加在每条之上。正确口径是「在其管辖范围内合规」而非「整体合规」。
- 条款出处：〔§ 172.5(a)(b)〕pdf-page 5
- 原文引用（英文逐字）：
  > "(b) The existence of a regulation prescribing safe conditions of use for a food additive shall not be construed to relieve the use of the substance from compliance with any other provision of the Act."
  > —— 〔§ 172.5(b)〕[pdf-page 5]
- 后果（答错会导致什么）：把 Part 172 当成免死金牌，漏判标签、卫生与过程控制义务，产出一份「添加剂层合规、整体不合规」的结论，且答不出跨编号分工。
- 建议归属子卡：V01

### CAND-CE-02: 以为「没写 ppm 数字 = 不限量」
- 错误说法（一句）：某条款只写了 `in accordance with good manufacturing practice`、没有 ppm 上限，说明可以随便加。
- 正确判定（3–6 句，写清依据与边界）：无数字的条款由 GMP 兜底，而 GMP 是被**定义**的：§172.5(a)(1) 把用量上限定为「不超过实现预期物理、营养或其他技术效果所合理需要的量」。这是一条实质限制，不是空白授权；大多数既有 ppm 上限的条款其实是「GMP 上限 + 安全上限」双闸门取严格者。判定时要能说出「超过多少就超出合理需要量」，并保留技术效果的论证链。
- 条款出处：〔§ 172.5(a)(1)〕〔§ 172.829(c)〕〔§ 172.510(a)〕pdf-page 5 / 124 / 48
- 原文引用（英文逐字）：
  > "(1) The quantity of the substance added to food does not exceed the amount reasonably required to accomplish its intended physical, nutritive, or other technical effect in food."
  > —— 〔§ 172.5(a)(1)〕[pdf-page 5]
- 后果（答错会导致什么）：在无数字条款上放任用量，构成 GMP 违规；反向也常错——把「有条款」误读成「必须给数字」，从而在 GMP 条款上凭空编造 ppm 上限。
- 建议归属子卡：V01

### CAND-CE-03: 以为同一物质来自多个来源的限量可以各自独立计算
- 错误说法（一句）：BHA 按 BHA 的限量、BHT 按 BHT 的限量，各算各的，不用合并。
- 正确判定（3–6 句，写清依据与边界）：§172.110 的限量表列头就是 `total BHA and BHT`，BHA 与 BHT **合计**不得超列值；§172.120 对钙二钠 EDTA 更直接，其 (b)(2) 规定与二钠 EDTA「in combination」按合并限值计。§172.730(a)(2) 还把「按本章其他法规使用所产生的额外同类残留」一并计入成品残留。判定顺序：先问有没有共用限量表或 in combination 措辞，再问是否有「他源累计」要求。
- 条款出处：〔§ 172.110(b)〕〔§ 172.120(b)(2)〕〔§ 172.730(a)(2)〕pdf-page 6 / 9 / 104
- 原文引用（英文逐字）：
  > "The BHA is used alone or in combination with BHT, as an antioxidant in foods, as follows:"
  > "(2) With disodium EDTA (disodium ethylenediaminetetraacetate) in the following foods at not to exceed, in combination, the levels prescribed, calculated as anhydrous C10H12O8N2CaNa2:"
  > —— 〔§ 172.110(b)〕〔§ 172.120(b)(2)〕[pdf-page 6 / 9]
- 后果（答错会导致什么）：两种抗氧化剂、两种 EDTA 分别「擦线合格」，合计却超标；成品残留也因未并入他源而被低估。
- 建议归属子卡：V02

### CAND-CE-04: 以为添加剂许可可以突破食品标准身份
- 错误说法（一句）：既然 FDA 许可了该添加剂，凡是食品都能加，标准身份（standard of identity）挡不住。
- 正确判定（3–6 句，写清依据与边界）：甜味剂等条款的许可句式是 `foods generally, except in meat and poultry ... in foods for which standards of identity established under section 401 ... do not preclude such use`——许可**以标准身份不排除为条件**。肉类与禽类另有 USDA 管辖，Part 172 的许可在其上无效。因此「FDA 许可」≠「在任何食品、任何类别中可用」；肉禽与标准化食品须单独过闸。
- 条款出处：〔§ 172.829(c)〕〔§ 172.800〕pdf-page 124 / 109
- 原文引用（英文逐字）：
  > "(c) The food additive neotame may be safely used as a sweetening agent and flavor enhancer in foods generally, except in meat and poultry, in accordance with current good manufacturing practice, in an amount not to exceed that reasonably required to accomplish the intended technical effect, in foods for which standards of identity established under section 401 of the Federal Food, Drug, and Cosmetic Act do not preclude such use."
  > —— 〔§ 172.829(c)〕[pdf-page 124]
- 后果（答错会导致什么）：把 FCS 甜味剂直接开进肉制品配方，既违反 Part 172 的类别除外、又落入 USDA 管辖；在标准化食品中还会因标准身份不允许而违法。
- 建议归属子卡：V03

### CAND-CE-05: 以为名录收录 = 可以任意用量
- 错误说法（一句）：某香料在 §172.515 清单里，所以想加多少加多少。
- 正确判定（3–6 句，写清依据与边界）：名录型条款（§172.510 天然 / §172.515 合成）条首只给「minimum quantity required + GMP」这一通用条件，**名录本身不含用量数值**；§172.515(b) 连 `Limitations` 列都没有，只为「是否存在」背书。用量判据始终回到条首的 GMP。反过来说，清单里有名也只解决「是否被许可」，不解决「该怎么用、能不能用在某食品」。名单严格讲仍需回原文核对拼写与收录状态。
- 条款出处：〔§ 172.510(a)〕〔§ 172.515(a)(b)〕pdf-page 48 / 55
- 原文引用（英文逐字）：
  > "They are used in the minimum quantity required to produce their intended effect, and otherwise in accordance with all the principles of good manufacturing practice."
  > —— 〔§ 172.515(a)〕[pdf-page 55]
- 后果（答错会导致什么）：把「在清单里」当成「无限制」，得出无上限结论；或反向把名录当用量表，去名录里找一个根本不存在的 ppm 值。
- 建议归属子卡：V04

### CAND-CE-06: 以为「符合 FCC 规格」就是合规的全部
- 错误说法（一句）：只要纯度符合 Food Chemicals Codex，这个添加剂就合法可用了。
- 正确判定（3–6 句，写清依据与边界）：规格只是四元组中的一元。§172.831 这类条款把规格整体 IBR 到 FCC 页码，但另有用途范围与用量/工艺条件；§172.185 甚至保留「或等效方法」的替代空间。满足纯度不满足用途，或满足用途不满足用量，都仍不合规。IBR 文件的内容不在本件内，只可引「须符合某文件某版某页」。
- 条款出处：〔§ 172.831(b)〕〔§ 172.185(b)〕pdf-page 127 / 19
- 原文引用（英文逐字）：
  > "(b) The additive meets the specifications of the Food Chemicals Codex, 7th ed. (2010), pp. 993-995, which is incorporated by reference."
  > —— 〔§ 172.831(b)〕[pdf-page 127]
- 后果（答错会导致什么）：只交一份纯度报告就宣称合规，漏掉用途/用量判定；或反向把 FCC 页码里的数值直接抄进结论（越界引用）。
- 建议归属子卡：V05

### CAND-CE-07: 以为肉禽可类比其他食品使用「食品一般」类甜味剂
- 错误说法（一句）：纽甜、安赛蜜、阿斯巴甜都是「食品一般（foods generally）」许可，肉制品里也能用。
- 正确判定（3–6 句，写清依据与边界）：这些条款的许可范围是 `foods generally, except in meat and poultry`——肉与禽类被**明文排除**。肉禽制品归 USDA/FSIS 管辖，其允许使用的添加剂清单另成体系，不能把 Part 172 的许可搬过去。判定时必须先做「食品类别闸门」，类别落在除外项即止，不必再算用量。
- 条款出处：〔§ 172.829(c)〕〔§ 172.800〕〔§ 172.804〕pdf-page 124 / 109 / 112
- 原文引用（英文逐字）：
  > "(c) The food additive neotame may be safely used as a sweetening agent and flavor enhancer in foods generally, except in meat and poultry, in accordance with current good manufacturing practice, in an amount not to exceed that reasonably required to accomplish the intended technical effect, in foods for which standards of identity established under section 401 of the Federal Food, Drug, and Cosmetic Act do not preclude such use."
  > —— 〔§ 172.829(c)〕[pdf-page 124]
- 后果（答错会导致什么）：把 FCS 甜味剂写进肉制品配方表，既触 Part 172 类别除外，又越权引用 USDA 管辖；在出口合规审核中会被直接判定不合规。
- 建议归属子卡：V03

### CAND-CE-08: 以为 IBR 引用文件里的数值可以随意转述
- 错误说法（一句）：条款说「incorporated by reference」，那把被引用文件里的规格数值写进结论也没问题。
- 正确判定（3–6 句，写清依据与边界）：IBR 文件（FCC 页码、厂商方法、ATCC 菌株资料）与法规正文**效力同等**，但其内容**不在本件**、也不在本技能包内。可引用的只是「须符合某文件某版某页」这一义务本身；一旦转述其内部 assay/杂质数值，就变成凭记忆写法规、且可能引用错版本（FCC 7th ed.＝2010、9th ed.＝2014）。§172.785 的噬菌体规格更是把测法、菌株、日期全外转，只可照抄其「方法名称 + 日期 + 出具方」。
- 条款出处：〔§ 172.185(b)〕〔§ 172.785(b)(1)〕pdf-page 19 / 109
- 原文引用（英文逐字）：
  > "The percentage of TBHQ in the food additive is not less than 99.0 percent when tested by the assay described in the Food Chemicals Codex, 9th ed. (2014), pp. 1192-1194, which is incorporated by reference, or an equivalent method."
  > —— 〔§ 172.185(b)〕[pdf-page 19]
- 后果（答错会导致什么）：把外部文件数值当成法规原文引用，属编造法规内容；版次/页码张冠李戴会在审核中被证伪，损害整份结论的可信度。
- 建议归属子卡：V05

### CAND-CE-09: 以为限量一律测成品
- 错误说法（一句）：限量都是对最终成品定的，在成品上测一次就够了。
- 正确判定（3–6 句，写清依据与边界）：限值的**作用点**不固定。§172.730(a)(1) 把溴酸盐限制在**麦芽**（≤75 ppm），成品另限溴化物总残留；§172.892 的某些改性方式限的是**处理剂**、另一些限的是**成品残留**（如残锰 ≤50 ppm 在改性淀粉中）；§172.177 明写取样部位为 `loin muscle`。判定须先问「这个数字测在哪个载体、哪个部位、测什么物质」。
- 条款出处：〔§ 172.730(a)(1)〕〔§ 172.177(b)〕〔§ 172.892〕pdf-page 104 / 18 / 173
- 原文引用（英文逐字）：
  > "the sodium nitrite content of the edible portion of the finished smoked product is not less than 100 parts per million and not greater than 200 parts per million, as measured in the loin muscle."
  > —— 〔§ 172.177(b)〕[pdf-page 18]
- 后果（答错会导致什么）：在成品上测出合格就放行，中间品却严重超标（或反之）；取样部位不合法定部位，检测数据不被采信。
- 建议归属子卡：V01

### CAND-CE-10: 以为每条 §172.xxx 都带标签义务段
- 错误说法（一句）：凡添加剂法规，都会有一段 `To assure safe use` 讲标签怎么写。
- 正确判定（3–6 句，写清依据与边界）：实测 154 条中只有约四分之一（25%）带 `To assure safe use` 段。§172.180 氯化亚锡一句话到底，既无限量外义务、也无标签义务；§172.892 的义务是**法定品名** `food starch-modified`。当条款没写标签义务时，**不得凭空补造**；有写时则通常要求标签载明添加剂名称与足够的使用说明。数学上「有没有标签义务」是可先判定的，别默认有。
- 条款出处：〔§ 172.180〕〔§ 172.892〕pdf-page 19 / 173
- 原文引用（英文逐字）：
  > "The food additive stannous chloride may be safely used for color retention in asparagus packed in glass, with lids lined with an inert material, in an amount not to exceed 20 parts per million calculated as tin (Sn)."
  > —— 〔§ 172.180〕[pdf-page 19]
- 后果（答错会导致什么）：给无义务条款的产品强加不存在的标签要求（过度合规、成本上升）；或反过来在有义务条款上漏写法定声明（如 PHENYLKETONURICS 警示语）。
- 建议归属子卡：V01 / V04

### CAND-CE-11: 以为「用途锁定声明」可以自己拟措辞
- 错误说法（一句）：标签上写一句「仅用于啤酒酿造」表达同样意思就行。
- 正确判定（3–6 句，写清依据与边界）：§172.730(c) 给的是**逐字法定措辞**：「`Brewer's Malt—To be used in the production of fermented malt beverages only`」或「`Distiller's Malt—To be used in the production of distilled spirits only`」，并须载于**处理过的麦芽**标签。用途限制靠这条法定措辞实现，自拟措辞不产生同样的合规效果。§172.725 对赤霉酸/赤霉酸钾处理的麦芽采用同款结构。
- 条款出处：〔§ 172.730(c)〕pdf-page 104
- 原文引用（英文逐字）：
  > "(c) To assure safe use of the additive, the label or labeling of the treated malt shall bear, in addition to other information required by the Act, the statement, “Brewer's Malt—To be used in the production of fermented malt beverages only”, or “Distiller's Malt—To be used in the production of distilled spirits only”, whichever is the case."
  > —— 〔§ 172.730(c)〕[pdf-page 104]
- 后果（答错会导致什么）：标签措辞不合规导致用途锁定失效，产品可能被转用；自拟声明也会在审核中不被认可。
- 建议归属子卡：V01

### CAND-CE-12: 以为表格里的「Do.」表示该行无限制
- 错误说法（一句）：限量表里某行写着 `Do.`，是说这一行没有限制。
- 正确判定（3–6 句，写清依据与边界）：`Do.` 是英文编纂惯用的「同上/ditto」，指**复制上一格的内容**。在 §172.120 与 §172.892 的表中，`Do.` 出现在 `Use` 栏或 `Limitations` 栏时，是把上一行的功能或限制原样套用，绝非「无限制」。整列 `Do.` 的情况还提示该列可能因跨页续表而被重置——必须回原 PDF 逐格核对，不得凭重建件推断。
- 条款出处：〔§ 172.120(b)〕〔§ 172.892(b)〕pdf-page 9 / 173
- 原文引用（英文逐字）：
  > "(2) With disodium EDTA (disodium ethylenediaminetetraacetate) in the following foods at not to exceed, in combination, the levels prescribed, calculated as anhydrous C10H12O8N2CaNa2:"
  > —— 〔§ 172.120(b)(2)〕[pdf-page 9]
- 后果（答错会导致什么）：把复制来的限制当成空白，得出「此食品无限制」的错误结论；或忽略跨页列重置导致限值串行。
- 建议归属子卡：V04

### CAND-CE-13: 以为重建表格的数值可以直接引用
- 错误说法（一句）：转换件里已经有 GFM 表格了，直接把表里的 ppm 抄进结论即可。
- 正确判定（3–6 句，写清依据与边界）：本件 16 张表是**按词级坐标启发式重建**（水平空隙 > 20 pt 判列边界），跨页续表与 `Do.` 行存在归属歧义，属转换局限标注的**不可逐字引用区**。工程纪律是：只写「食品 → 限量 → 功能」的**判读关系**，任何具体数值一律回原 PDF 核对；本技能包内不逐字引表值。这条与「有条款 ≠ 有剂量上限」配套使用。
- 条款出处：〔§ 172.110(b)〕〔§ 172.120(b)〕〔§ 172.892〕＋转换局限声明 pdf-page 6 / 9 / 173
- 原文引用（英文逐字）：
  > "The quantity of any substance employed to effect such modification shall not exceed the amount reasonably required to accomplish the intended physical or technical effect, nor exceed any limitation prescribed."
  > —— 〔§ 172.892〕[pdf-page 173]
- 后果（答错会导致什么）：把启发式重建的数值当权威值输出，一旦列边界误判就会给出错误限量；此类错误在合规审查中风险极高。
- 建议归属子卡：V04 / V05

### CAND-CE-14: 以为营养物质获批 = 可以做膳食必要性主张
- 错误说法（一句）：这个氨基酸/维生素被 FDA 批准作营养添加剂了，所以可以宣称它「有用、膳食必需」。
- 正确判定（3–6 句，写清依据与边界）：§172.5(c) 明文否定：营养物质许可法规的存在**不构成**其「对人类膳食有用或必需」的认定。营养声称要走〔§ 101〕的授权路径与显著性/失格水平闸门，与 Part 172 的物质许可不同法源。把许可当声称依据，属跨编号乱引。
- 条款出处：〔§ 172.5(c)〕〔§ 172.320〕pdf-page 5 / 30
- 原文引用（英文逐字）：
  > "(c) The existence of any regulation prescribing safe conditions of use for a nutrient substance does not constitute a finding that the substance is useful or required as a supplement to the diet of humans."
  > —— 〔§ 172.5(c)〕[pdf-page 5]
- 后果（答错会导致什么）：以「FDA 批准」为据做营养/健康声称，构成 §403 意义上的错标；把 Part 172 条款号写进声称判定，污染效力层。
- 建议归属子卡：V01

### CAND-CE-15: 以为特殊膳食标签只看 Part 172
- 错误说法（一句）：含该甜味剂的特殊膳食食品，只要符合 Part 172 的用量就行，标签不用管别的。
- 正确判定（3–6 句，写清依据与边界）：多条甜味剂条款（如 §172.829(e)）明写：若食品宣称或表示为特殊膳食用途，须**符合 part 105 的标签要求**。这是条款内部指向另一部分的义务，不能因「已符合 Part 172 用量」而免除。判定顺序：先过 Part 172 用途/用量，再过 part 105 标签。
- 条款出处：〔§ 172.829(e)〕〔§ 172.800(c)〕pdf-page 125 / 109
- 原文引用（英文逐字）：
  > "(e) If the food containing the additive purports to be or is represented to be for special dietary use, it shall be labeled in compliance with part 105 of this chapter."
  > —— 〔§ 172.829(e)〕[pdf-page 125]
- 后果（答错会导致什么）：特殊膳食产品漏掉 part 105 标签义务；把跨部分指引误当作可有可无的「提示」。
- 建议归属子卡：V03

### CAND-CE-16: 以为氨基酸类可以给婴幼儿食品通用
- 错误说法（一句）：氨基酸都是营养强化剂，婴幼儿食品也能按同一清单添加。
- 正确判定（3–6 句，写清依据与边界）：§172.320(a) 是 22 项列举式许可，其中第 (14) 项 `DL-Methionine (not for infant foods)` **在列举项内自带人群限制**。限制可能嵌在物质名录里而不是另起一段，逐项读名录时必须读到行内括号。婴幼儿另有专门规则与人群适用性，不能由「在清单里」直接推出可用。
- 条款出处：〔§ 172.320(a)〕pdf-page 30
- 原文引用（英文逐字）：
  > "(14) DL-Methionine (not for infant foods)"
  > —— 〔§ 172.320(a)(14)〕[pdf-page 30]
- 后果（答错会导致什么）：把 DL-蛋氨酸用于婴幼儿食品，直接违反条款明文限制；这类「行内限制」最易被名录式阅读漏掉。
- 建议归属子卡：V04

### CAND-CE-17: 以为许可范围里的食品/定义是举例，可以类推
- 错误说法（一句）：条款说适用于「即食肉禽」，那我的产品也接近即食，应该可以套用。
- 正确判定（3–6 句，写清依据与边界）：范围多为**封闭**且边界**外转**。§172.785(c) 把适用对象钉在 `products that comply with the ready-to-eat definition in 9 CFR 430.1`——是否即食由 9 CFR 430.1 定义判定，不是「接近就算」。§172.867(c) 同样把 Olestra 限定为「预包装即食咸/辛非甜零食 + 预包装待加热未爆玉米粒」。类推无效，必须逐项对照外部定义。
- 条款出处：〔§ 172.785(c)〕〔§ 172.867(c)〕pdf-page 109 / 153
- 原文引用（英文逐字）：
  > "(c) Conditions of use. The additive is used in accordance with current good manufacturing practice to control L. monocytogenes by direct application to meat and poultry products that comply with the ready-to-eat definition in 9 CFR 430.1."
  > —— 〔§ 172.785(c)〕[pdf-page 109]
- 后果（答错会导致什么）：把适用范围类推到未获许可的产品，超范围使用；或在审核中以「性质相近」代替法定定义，结论站不住脚。
- 建议归属子卡：V01 / V02

### CAND-CE-18: 以为 Olestra 的营养补偿是可选的、补进去的维生素可计入营养标签
- 错误说法（一句）：用 Olestra 时补维生素是推荐做法；补进去的维生素算作产品的营养含量。
- 正确判定（3–6 句，写清依据与边界）：§172.867(d) 用 `shall be added` 规定**强制补偿**，并把每克 Olestra 须补的 A/D/E/K 量写死——不加即不合规，且这是许可的生效条件。§172.867(e)(1) 又规定：这些维生素须在配料表标注、且**不得计入**营养标签或任何营养声称；配料表后须打星号并标 `Dietarily insignificant`；同条 (e)(2) 规定 Olestra **不计作**脂肪或热量来源。补偿是义务、计价方式是法定的。
- 条款出处：〔§ 172.867(d)(e)〕pdf-page 153–154
- 原文引用（英文逐字）：
  > "(d) To compensate for any interference with absorption of fat soluble vitamins, the following vitamins shall be added to foods containing olestra: 1.9 milligrams alpha-tocopherol equivalents per gram olestra; 51 retinol equivalents per gram olestra (as retinyl acetate or retinyl palmitate); 12 IU vitamin D per gram olestra; and 8 µg vitamin K1 per gram olestra."
  > —— 〔§ 172.867(d)〕[pdf-page 153]
- 后果（答错会导致什么）：不补或少补维生素→许可失效；把补偿维生素计入营养标签或声称→标签错误；把 Olestra 当脂肪/热量计入→营养标签与声称连锁出错。
- 建议归属子卡：V03

### CAND-CE-19: 以为包装/容器前提不是许可要件
- 错误说法（一句）：氯化亚锡能护色，什么包装的芦笋都能用。
- 正确判定（3–6 句，写清依据与边界）：§172.180 把许可绑在具体载体前提上——`asparagus packed in glass, with lids lined with an inert material`。换了包装（非玻璃罐）或盖内衬非惰性材料，即**不在许可范围内**，与用量多少无关。判定时要把「载体前提」当作独立的合规要件逐项核对。
- 条款出处：〔§ 172.180〕pdf-page 19
- 原文引用（英文逐字）：
  > "The food additive stannous chloride may be safely used for color retention in asparagus packed in glass, with lids lined with an inert material, in an amount not to exceed 20 parts per million calculated as tin (Sn)."
  > —— 〔§ 172.180〕[pdf-page 19]
- 后果（答错会导致什么）：在非允许包装上使用，超范围违规；也常因忽略「以 Sn 计」而把限值算错基准。
- 建议归属子卡：V01

---

## 覆盖自检

| 子卡 | 覆盖的反例 |
|---|---|
| V01 许可判定链与限制五形态 | CE-01, CE-02, CE-09, CE-10, CE-11, CE-14, CE-17, CE-19 |
| V02 防腐剂与抗菌剂 | CE-03, CE-17 |
| V03 甜味剂与脂肪替代物 | CE-04, CE-07, CE-15, CE-18 |
| V04 品质功能类与长尾名录导航 | CE-05, CE-10, CE-12, CE-13, CE-16 |
| V05 效力层与 IBR 边界 | CE-06, CE-08, CE-13 |
