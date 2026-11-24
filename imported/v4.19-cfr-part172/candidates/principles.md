# 候选池：原则提取器 | 来源 21 CFR Part 172 eCFR 2026-11-05 | 全量扫描 chunk-01..04

> 主代理顺序执行。154/154 条款覆盖。引用逐字来自 `source-cfr-part172-2026.md`，已过 `verify_part172_quotes.py`。

---

### CAND-PR-01: 许可的客体是四元组，不是物质

- 条款出处：〔§ 172.5(a)〕〔§ 172.170〕〔§ 172.175〕〔§ 172.177〕 + pdf-page 5 / 18 / 19
- 原文引用（英文逐字）：
  > "The food additive sodium nitrite may be safely used in or on specified foods in accordance with the following prescribed conditions:"
  > —— 〔§ 172.175〕[pdf-page 18]
- 原则陈述：法规许可的单元是「物质 + 用途 + 用量 + 规格」。同一物质在三条条款下有三个不同许可范围：〔§ 172.175〕给亚硝酸钠的一般限量（烟熏金枪鱼 ≤10 ppm；烟熏鲑/鲭/鲱 ≤200 ppm 且硝酸钠 ≤500 ppm；家庭腌肉制剂同理）；〔§ 172.177〕只给烟熏鲢且带完整工艺参数；〔§ 172.160/170〕分别给硝酸钾（鱼籽 200 ppm）与硝酸钠。换食品、换用途、超量、规格不达标，任一项越界即不在许可内。例外/边界：条款未列的功能用途一律不可推定。
- 复现位置：〔§ 172.177〕（同物质专条）、〔§ 172.730〕（限量算在麦芽、残留算在成品）、〔§ 172.867(c)〕（用途封闭为两类零食）
- 可回答的新问题：这个物质我能不能用到另一款产品上？两个被许可用途能不能叠加？
- 建议归属子卡：V01

---

### CAND-PR-02: GMP 是叠加在一切条款之上的兜底限制

- 条款出处：〔§ 172.5(a)(1)(2)〕 + pdf-page 5
- 原文引用（英文逐字）：
  > "Any substance intended for use in or on food is of appropriate food grade and is prepared and handled as a food ingredient."
  > —— 〔§ 172.5(a)(2)〕[pdf-page 5]
- 原则陈述：§172.5(a) 定义了两条**对全 Part 生效**的 GMP 限制：用量不得超过实现预期物理/营养/其他技术效果所需量；物质须为适当食品级并按食品配料制备与处理。这意味着**即使某条款没有给任何数值，也有可执行的合规约束**——只是判定方式从「检测比对」变成「工艺合理性 + 记录论证」。反向也成立：条款给了 ppm 上限时，GMP 仍在其上叠加（不得因为没超限就用到超出功能所需）。
- 复现位置：〔§ 172.892〕明写「shall not exceed the amount reasonably required ... nor exceed any limitation prescribed」（双重叠加）、〔§ 172.210(a)(b)〕「minimum amount required」、〔§ 172.235〕仅 GMP
- 可回答的新问题：没有数字限制的条款怎么判合规？有 ppm 上限时还要不要论证「用量合理」？
- 建议归属子卡：V01 / V05

---

### CAND-PR-03: 许可不免除本法其他任何义务

- 条款出处：〔§ 172.5(b)〕 + pdf-page 5
- 原文引用（英文逐字）：
  > "The existence of a regulation prescribing safe conditions of use for a food additive shall not be construed to relieve the use of the substance from compliance with any other provision of the Act."
  > —— 〔§ 172.5(b)〕[pdf-page 5]
- 原则陈述：这是 Part 172 与整个 PCHF 体系之间的**法定搭扣**。用了被许可的添加剂，仍须：做危害分析、符合 CGMP、控制过敏原、标签合规、不得掺假（402）、不得错标（403）。因此「法规允许使用」在任何回答里都不能被表述为「安全且合规」。例外/边界：无——本条无例外，是全 Part 最硬的元规则。
- 复现位置：〔§ 172.785〕噬菌体有许可但不替代环境监测；〔§ 172.110〕限量表不替代成品微生物控制；〔§ 172.5(c)〕营养许可不构成必要性认定
- 可回答的新问题：用了许可添加剂是否还要做危害分析？是否能因此简化预防控制？
- 建议归属子卡：V05

---

### CAND-PR-04: 营养物质的许可 ≠ 膳食有用性认定

- 条款出处：〔§ 172.5(c)〕 + pdf-page 5
- 原文引用（英文逐字）：
  > "The existence of any regulation prescribing safe conditions of use for a nutrient substance does not constitute a finding that the substance is useful or required as a supplement to the diet of humans."
  > —— 〔§ 172.5(c)〕[pdf-page 5]
- 原则陈述：Subpart D（特殊膳食与营养添加剂）的许可只解决「安全性」，**不解决「有没有用、要不要补」**。因此不能据「某维生素有 §172 条款」推出「该产品需要强化」或「可以宣称补充必要性」。声称与营养含量表述完全是另一层（Part 101）。例外：〔§ 172.867(d)〕是相反的极端——那里法规**强制**补偿添加，但那是许可条件而非「有用性认定」。
- 复现位置：〔§ 172.867(d)〕（强制补偿的对照）、〔§ 172.804〕（甜味剂许可不涉营养声称）、〔§ 172.831(d)〕（特殊膳食用途转 Part 105 标签）
- 可回答的新问题：有 §172 条款的营养素能否直接用于营养声称？强化是不是「法规要求」？
- 建议归属子卡：V05

---

### CAND-PR-05: 限制形态决定合规判定方式

- 条款出处：〔§ 172.5(a)(1)〕+ 全 Part 实测 + pdf-page 5
- 原文引用（英文逐字）：
  > "The quantity of the substance added to food does not exceed the amount reasonably required to accomplish its intended physical, nutritive, or other technical effect in food."
  > —— 〔§ 172.5(a)(1)〕[pdf-page 5]
- 原则陈述：五形态（ppm 数值 80 / 仅 GMP 34 / 仅限食品 8 / 功能限定 11 / 无限制语 21）不是分类游戏，而是**决定你怎么证明合规**：① ppm 型 → 成品检验 + 不确定度余量；② GMP 型 → 工艺论证 + 添加量记录 + 功能必要性说明；③ 仅限食品型 → 配方与食品类别核对；④ 功能限定型 → 用途身份与声称一致性；⑤ 无限制语型 → 依赖 §172.5 兜底。判错形态会直接导致**用错举证方式**。
- 复现位置：〔§ 172.831(c)〕GMP 无量 vs 〔§ 172.804(c)(2)〕焙烤食品 0.5% 数值 vs 〔§ 172.829(b)〕只有纯度规格
- 可回答的新问题：这款添加剂我该建检验项还是建工艺论证档？
- 建议归属子卡：V01

---

### CAND-PR-06: 食品范围是封闭清单，`specified foods` 须逐项对照

- 条款出处：〔§ 172.170〕〔§ 172.175〕〔§ 172.867(c)〕〔§ 172.210〕 + pdf-page 18 / 154 / 20
- 原文引用（英文逐字）：
  > "Olestra may be used in place of fats and oils in prepackaged ready-to-eat savory (i.e., salty or piquant but not sweet) snacks and prepackaged, unpopped popcorn kernels that are ready-to-heat."
  > —— 〔§ 172.867(c)〕[pdf-page 154]
- 原则陈述：条款里的食品表述分两类，含义相反：**封闭清单**（"specified foods"、"in the following foods"、逐一列举）——不在其中即不可用，且「同类不同种」不可套用；**开放范围**（"foods generally"、"in food"）——才可推广。判定时必须回到条款原文定位属于哪类，不能凭物质名推断。例外：开放范围仍可能被标准身份（Part 130，未收）或标签规则限制。
- 复现位置：〔§ 172.831(c)〕`foods generally`（开放）／〔§ 172.175(a)〕逐项列举（封闭）／〔§ 172.210〕仅 citrus 表面
- 可回答的新问题：我的产品算不算条款说的那类食品？「类似产品」能不能类推？
- 建议归属子卡：V01

---

### CAND-PR-07: 限值的作用点可能在中间品，不在成品

- 条款出处：〔§ 172.730(a)(1)(2)〕〔§ 172.177(b)〕〔§ 172.892〕 + pdf-page 104 / 19 / 173
- 原文引用（英文逐字）：
  > "(2) The total residue of inorganic bromides in fermented malt beverages, resulting from the use of the treated malt plus additional residues of inorganic bromides that may be present from uses in accordance with other regulations in this chapter promulgated under sections 408 and/or 409 of the act, does not exceed 25 parts per million of bromide (calculated as Br)."
  > —— 〔§ 172.730(a)(2)〕[pdf-page 104]
- 原则陈述：限值的作用点有三种：添加剂在处理物中的量（麦芽 75 ppm 溴酸盐）、成品中的残留（啤酒 25 ppm 溴化物）、以及**因其他法规来源产生的同类残留须累计**。第三种最易漏：原文明确要求把「按本章其他法规（408/409 条下）使用所产生的额外残留」一并计入。另外取样部位本身可以是法规要件（loin muscle）。判定时必须先问：这个数字测在哪、测什么、要不要累计他源。
- 复现位置：〔§ 172.177(b)〕「as measured in the loin muscle」；〔§ 172.892〕「Residual manganese ... in food starch-modified」
- 可回答的新问题：限值该测在哪一段？成品检测值里哪些来自我的添加剂？要不要并入其他来源？
- 建议归属子卡：V01 / V02

---

### CAND-PR-08: 纯度规格常以 IBR 外转，不可转述数值

- 条款出处：〔§ 172.831(b)〕〔§ 172.804(b)〕〔§ 172.867(b)〕〔§ 172.829(b)〕 + pdf-page 127 / 113 / 154 / 125
- 原文引用（英文逐字）：
  > "(b) The additive meets the specifications of the Food Chemicals Codex, 7th ed. (2010), pp. 993-995, which is incorporated by reference."
  > —— 〔§ 172.831(b)〕[pdf-page 127]
- 原则陈述：43 条（27%）把规格整体 IBR 到 FCC 页码、厂商方法或菌种保藏。法律上 IBR 文件与法规正文同等效力，但内容不在本件。纪律：只可引「须符合某文件某版某页」，**绝不转述其 assay/杂质数值**。对照：〔§ 172.829〕把 6 项规格直接写在条文里——同一 Subpart 内两种做法并存，所以**不能假设「有规格就等于有可读数值」**。
- 复现位置：〔§ 172.804(b)〕FCC 7th ed. pp.73-74；〔§ 172.785(b)(1)〕厂商方法 + ATCC 菌株；〔§ 172.829(b)(1)–(6)〕直写数值
- 可回答的新问题：这条法规给了我可直接核对的纯度数值吗？没有的话去哪查？
- 建议归属子卡：V05

---

### CAND-PR-09: 标准身份优先于添加剂许可

- 条款出处：〔§ 172.804〕 + pdf-page 113
- 原文引用（英文逐字）：
  > "The food additive aspartame may be safely used in food in accordance with good manufacturing practice as a sweetening agent and a flavor enhancer in foods for which standards of identity established under section 401 of the Federal Food, Drug, and Cosmetic Act do not preclude such use under the following conditions:"
  > —— 〔§ 172.804〕[pdf-page 113]
- 原则陈述：添加剂许可的适用范围被**标准身份（standard of identity）**再削一层：只有标准身份「不排除该用途」的食品才可用。因此存在这样的结构——某物质有 §172 许可，但目标食品的标准身份（如某些乳制品、面包标准）禁止或限制其使用，则**许可在此失效**。例外：无标准的食品不受此限。边界：标准身份在 21 CFR Part 130 等（本包未收），须标「转引未收」。
- 复现位置：〔§ 172.831(c)〕三氯蔗糖未提标准身份（对比：并非条条都有此限制）；〔§ 172.867(c)〕以用途封闭替代标准身份限制
- 可回答的新问题：某物质有 §172 条款，为什么用在这款产品上仍可能违规？
- 建议归属子卡：V03 / V05

---

### CAND-PR-10: 强制营养补偿是许可的生效条件

- 条款出处：〔§ 172.867(d)〕 + pdf-page 154
- 原文引用（英文逐字）：
  > "To compensate for any interference with absorption of fat soluble vitamins, the following vitamins shall be added to foods containing olestra:"
  > —— 〔§ 172.867(d)〕[pdf-page 154]
- 原则陈述：Olestra 因阻断脂溶性维生素吸收，法规把「按每克 olestra 添加 α-生育酚当量、视黄醇当量、维生素 D、维生素 K1」写成许可条件。判定要点：① 这是**强制**（shall），不是可选强化；② 换算基准是「每克 olestra」而非每份食品，故配方一变补偿量随之变；③ 未补偿即属未按许可条件使用；④ 补偿与营养标签是两个层面（标签 → Part 101），不可互相替代。这是全 Part 唯一「许可附带配方强制」的典型。
- 复现位置：〔§ 172.5(c)〕（营养许可不等于必要性——反向对照）；〔§ 172.379/380〕维生素 D 另有限量
- 可回答的新问题：用 Olestra 时配方上有什么不可省的强制动作？单位怎么换算？
- 建议归属子卡：V03

---

### CAND-PR-11: 长尾名录条款只解决「是否收录」，不解决「怎么用」

- 条款出处：〔§ 172.510〕〔§ 172.515〕 + pdf-page 49 / 58
- 原文引用（英文逐字，仅结构句）：
  > "Synthetic flavoring substances and adjuvants."
  > —— 〔§ 172.515〕[pdf-page 58]
- 原则陈述：两条合计约 1,200 行、上千物质名，每条只给名称与（部分）同义名/FEMA 号，用量统一回落 GMP。原则：① 收录 = 该物质可作为该用途使用，**不等于可任意用**（仍受 §172.5(a) GMP）；② 未收录**不等于禁止**——可能属 GRAS（另一制度）或另有具名条款；③ 具名条款（如 §172.520/560/575）优先于名录；④ 本包不背书任何具体物质的收录状态，须回原文核对拼写与同义名。这四条的目的是防止把「名录查不到」误判为「不可用」。
- 复现位置：〔§ 172.520/530/535/560/575/580/585/590〕具名香料类条款另有限值
- 可回答的新问题：某香料是否被许可？查不到时结论该怎么下？
- 建议归属子卡：V04

---

### CAND-PR-12: 标签义务的三种触发，且并非条条都有

- 条款出处：〔§ 172.175(b)(1)(2)〕〔§ 172.115(c)〕〔§ 172.730(b)(c)〕 + pdf-page 18 / 7 / 104
- 原文引用（英文逐字）：
  > "The label of the additive or of a mixture containing the additive shall bear:"
  > —— 〔§ 172.175(b)(1)〕[pdf-page 18]
- 原则陈述：Part 172 的标签义务有三种触发，须分别识别：① **添加剂名称**（几乎凡有 (d) 段者皆有）；② **混合物中的浓度百分比**（以载体/复配形式销售时）；③ **使用说明**（保证成品不超限，家庭零售包装尤甚，部分条款另要求「Keep out of the reach of children」）。关键：实测仅 25% 的条款有「To assure safe use」段——**不能假定每条都有标签义务**；且这些义务对象是**添加剂卖方**，不是成品食品标签（成品标签 → Part 101）。
- 复现位置：〔§ 172.730(b)(1)(2)〕只要求名称与使用说明、无浓度要求；〔§ 172.730(c)〕对处理物麦芽另给逐字用途声明
- 可回答的新问题：我卖复配添加剂要写什么？这些要求是给我还是给我的客户？
- 建议归属子卡：V05

---

### CAND-PR-13: 引用链须走到终点

- 条款出处：〔§ 172.210(b)(1)(2)〕〔§ 172.831(d)〕〔§ 172.785(b)(1)〕 + pdf-page 20 / 127 / 109
- 原文引用（英文逐字）：
  > "Substances generally recognized as safe for the purpose or previously sanctioned for the purpose."
  > —— 〔§ 172.210(b)(1)〕[pdf-page 20]
- 原则陈述：条款以三类引用把条件外转：① 指向其他 §172 条款（"Complying with § 172.860"）；② 指向其他制度（GRAS / prior sanctioned，均不在本 Part）；③ 指向其他 Part（特殊膳食标签 → Part 105）。判定必须顺链走到终点：一个涂层配方可能要先解 §172.210，再解 §172.860 脂肪酸规格，再解其 IBR 文件。这正是「一个产品同时受多条法规约束」的成因。
- 复现位置：〔§ 172.210〕并列引用 §172.860/862/820；〔§ 172.615〕胶基由多类物质构成、各类另有规格
- 可回答的新问题：这个配方总共要满足几条法规？引用链终点落在哪个制度？
- 建议归属子卡：V04

---

### CAND-PR-14: 「有条款」不等于「有剂量上限」

- 条款出处：〔§ 172.235〕〔§ 172.160〕〔§ 172.831(c)〕 + pdf-page 25 / 16 / 127
- 原文引用（英文逐字）：
  > "The food additive potassium nitrate may be safely used as a curing agent in the processing of cod roe, in an amount not to exceed 200 parts per million of the finished roe."
  > —— 〔§ 172.160〕[pdf-page 16]
- 原则陈述：实测 154 条中仅 80 条（52%）含量化限值，34 条只有 GMP，21 条连限制语都不明显。因此**「查到了条款」不能推出「查到了限值」**。判定纪律：先归类五形态，再决定举证方式；若为 GMP 型则回答「无法规数值上限，但受 §172.5(a) 合理用量约束，需工艺论证」。反向误读同样危险：把 §172.160 的「200 ppm 成品鱼籽」当成「硝酸钾通用上限」。
- 复现位置：〔§ 172.235〕仅 GMP；〔§ 172.831(c)〕食品通用 + GMP 无量；〔§ 172.255〕无限制语
- 可回答的新问题：这条到底有没有可检测的限值？没有的话我该怎么证明合规？
- 建议归属子卡：V01 / V04

---

### CAND-PR-15: 用途锁定通过处理物标签措辞执行

- 条款出处：〔§ 172.730(c)〕 + pdf-page 104
- 原文引用（英文逐字）：
  > "“Brewer's Malt—To be used in the production of fermented malt beverages only”, or “Distiller's Malt—To be used in the production of distilled spirits only”, whichever is the case."
  > —— 〔§ 172.730(c)〕[pdf-page 104]
- 原则陈述：当许可把用途锁死在某一下游行业时，法规用**处理物标签上的逐字声明**来执法：① 措辞是法定的两个版本择一，不可改写；② 义务对象是处理物（麦芽）标签；③ 违反即处理物失去许可前提。这是「以标签实现用途管制」的机制——与 Part 101 的「标示义务」性质不同：**前者是管制手段，后者是告知义务**，两者不可混为一谈。
- 复现位置：〔§ 172.177(e)(2)〕容器须给足使用说明以保证成品合规（同类但非逐字锁定）；〔§ 172.785〕无用途锁定（对照）
- 可回答的新问题：法规怎么防止这个添加剂流入其他行业？下游买家看到这句话意味着什么？
- 建议归属子卡：V05

---

## 复现次数最多的三条

1. **CAND-PR-01 四元组 / PR-06 食品范围封闭**（在 §172.110/115/160/170/175/177/210/730/785/804/831/867 共 12+ 处复现）——Part 172 全部误读的根源。
2. **CAND-PR-02 GMP 兜底**（§172.5 总则 + §172.210/235/255/330/831/892 明写「minimum/reasonably required」）——覆盖所有无数字条款。
3. **CAND-PR-03 不免除其他义务**（与 §172.785、§172.867(d)、§172.5(c) 三处形成张力）——全包接口的法定依据。