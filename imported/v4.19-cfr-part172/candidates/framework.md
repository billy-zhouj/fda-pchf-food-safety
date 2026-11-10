# 候选池：框架提取器 | 来源 21 CFR Part 172 eCFR 2026-11-05 | 全量扫描 chunk-01..04

> 主代理顺序执行（并行子代理被上游限流）。扫描覆盖：chunk-01（§172.5–385）、chunk-02（§172.395–660）、chunk-03（§172.665–844）、chunk-04（§172.846–898），154/154 条款。
> 纪律：引用逐字来自 `source-cfr-part172-2026.md`；16 张重建表格数值、§172.510/§172.515 名录、IBR 外部文件内容标不可逐字引用区。

---

### CAND-FW-01: 「物质 × 用途 × 用量 × 规格」四元组许可闸门

- 条款出处：〔§ 172.5(a)〕〔§ 172.110〕〔§ 172.175〕〔§ 172.210〕 + pdf-page 5 / 7 / 18 / 20
- 原文引用（英文逐字）：
  > "Regulations prescribing conditions under which food additive substances may be safely used predicate usage under conditions of good manufacturing practice."
  > —— 〔§ 172.5(a)〕[pdf-page 5]
- 方法论陈述：Part 172 许可的从来不是「某物质」，而是「物质 + 用途（哪类食品 / 什么功能）+ 用量（上限或 GMP）+ 纯度规格」四元组。判定顺序：① 先定位该物质是否有〔§ 172.xxx〕条款；② 再判目标食品是否落在该条列举的用途范围（范围是封闭清单，不是举例）；③ 再判用量是否在限值内（或无数字则受 GMP 兜底）；④ 再判纯度是否满足规格（含 IBR 引用）；⑤ 四者缺一，即不在许可范围内。任何一步跳跃（例如只因物质名对得上就认定可用）都会得出错误结论。
- 可回答的新问题：同一物质能用在这款产品、是否也能用在另一款？把两种被许可用途叠加使用是否累计超限？
- 跨域佐证：〔§ 172.175(a)(1)(2)(3)〕同一物质（亚硝酸钠）按食品分三档给不同限值；〔§ 172.730(a)(1)〕限量算在**麦芽**而残留算在**成品饮料**，两个载体不同。
- 建议归属子卡：V01

---

### CAND-FW-02: 限制条件的五形态判读链（本件最重要的判读框架）

- 条款出处：〔§ 172.5(a)(1)〕+ 全 Part 154 条实测分布 + pdf-page 5
- 原文引用（英文逐字）：
  > "The quantity of the substance added to food does not exceed the amount reasonably required to accomplish its intended physical, nutritive, or other technical effect in food."
  > —— 〔§ 172.5(a)(1)〕[pdf-page 5]
- 方法论陈述：154 条的限制语实测只有五种形态，判定时必须先归类再取值：① **ppm/百分比数值上限（80 条）**——有明确红线，须对成品检测；② **仅受 GMP 约束（34 条）**——只有「不超过实现预期效果所需量」，**没有任何数字**，合规判定靠工艺合理性与记录，不靠检验；③ **仅限特定食品/用途（8 条）**——食品范围封闭，用量靠 GMP；④ **功能限定（11 条）**——只能以某功能身份使用；⑤ **无明显限制语（21 条）**——仅 GMP 总则兜底。**关键推论：有条款 ≠ 有剂量上限**。把 ②③④⑤ 当成 ① 会虚构出不存在的红线；把 ① 的数值当成全食品通用会越界使用。
- 可回答的新问题：这条法规到底有没有给我一个可以检测的限值？我该按检验放行还是按工艺合理性放行？
- 跨域佐证：〔§ 172.235〕Morpholine 仅「不超过实现效果所需」；〔§ 172.160〕硝酸钾只有一句「不超过 200 ppm 成品鱼籽」；〔§ 172.892〕开头同时写 GMP 与「nor exceed any limitation prescribed」——两种限制叠加。
- 建议归属子卡：V01

---

### CAND-FW-03: 四段式条款语法（Identity → Specifications → Use → To assure safe use）

- 条款出处：〔§ 172.110〕〔§ 172.175〕〔§ 172.804〕〔§ 172.831〕 + pdf-page 7 / 18 / 113 / 127
- 原文引用（英文逐字）：
  > "To assure safe use of the additive, in addition to the other information required by the Act:"
  > —— 〔§ 172.175(b)〕[pdf-page 18]
- 方法论陈述：几乎每条都按同一模板展开：(a) Identity 给化学身份/CAS/制备方式；(b) Specifications 给 assay 区间与杂质上限（常以 IBR 引用）；(c) Use 给食品范围与限值；(d) To assure safe use 给标签与使用说明义务。**读条款时按段定位**，不要通读后凭印象。实测覆盖率：量化限制 66%、身份定义 44%、纯度规格 40%、IBR 27%、「To assure safe use」25%——即**约 3/4 的条款没有 (d) 段**，不能一律假定有标签义务。
- 可回答的新问题：这条法规要求我在添加剂包装上写什么？为什么有的物质有标签要求、有的没有？
- 跨域佐证：〔§ 172.730〕有 (b) 与 (c) **两处**标签义务，分别针对添加剂本身与处理过的麦芽；〔§ 172.831〕(d) 把特殊膳食用途标签义务外转 Part 105。
- 建议归属子卡：V01

---

### CAND-FW-04: 「Do.（同上）」延续语义与列内嵌限制

- 条款出处：〔§ 172.210(b)(2)〕〔§ 172.892〕〔§ 172.615〕 + pdf-page 20 / 173 / 93
- 原文引用（英文逐字）：
  > "Do Acid number of 176-186; drop-softening point of 110 °C-118 °C; saponification number of less than 280; and a color of M or paler."
  > —— 〔§ 172.210(b)(2)〕[pdf-page 20]
- 方法论陈述：表格型条款里 `Do.`（同上）表示「沿用上一行的**主体**」，但**右列限制条件是新写的、必须单独读**。典型误读是把整行都当「同上」，从而漏掉新的限制。另有**限制内嵌在左列**的形态：〔§ 172.892〕把「Chlorine, as calcium hypochlorite, not to exceed 0.036 percent of dry starch」与「The finished food starch-modified is limited to use only as a component of batter...」放在同一行，即**用量限制与用途限制同时绑定**。
- 可回答的新问题：这一行 `Do.` 到底继承了什么、又新加了什么？左列里的「limited to use only as」是数量限制还是用途限制？
- 跨域佐证：〔§ 172.210〕多行 `Do` 各带不同酸值/软化点区间；〔§ 172.892〕多行 `Limitations` 表头逐页重复，属版式重复而非新表。
- 建议归属子卡：V04

---

### CAND-FW-05: 载体转换链（限值算在中间品、残留算在成品）

- 条款出处：〔§ 172.730(a)(1)(2)〕 + pdf-page 104
- 原文引用（英文逐字）：
  > "the amount of the additive present in the malt from the treatment does not exceed 75 parts per million of bromate (calculated as Br), and the treated malt is used only in the production of fermented malt beverages or distilled spirits."
  > —— 〔§ 172.730(a)(1)〕[pdf-page 104]
- 方法论陈述：部分条款的限制对象不是最终食品，而是**中间处理物**（麦芽），同时对最终食品另给残留限值（啤酒 25 ppm 溴化物），并明确「蒸馏酒不设残留限值，因为有证据表明无机溴化物不随蒸馏转移」。判定时必须区分三个层次：添加剂在处理物中的量 / 成品的残留量 / 副产物（溴化物）的累计量——且**第三条还要叠加其他法规来源的同类残留**（原文写明 plus additional residues from uses in accordance with other regulations）。这类条款不能只看一个数字就放行。
- 可回答的新问题：我的限值该测在哪一段工艺？成品检测值里有多少来自我这个添加剂、多少来自同批其他原料？
- 跨域佐证：〔§ 172.177(b)〕亚硝酸盐限值明确「as measured in the loin muscle」——**取样部位本身是法规要件**；〔§ 172.892〕「Residual manganese, not to exceed 50 ppm in food starch-modified」是反应副产物残留。
- 建议归属子卡：V01

---

### CAND-FW-06: 多栅栏工艺参数条款（§172.177 烟熏鲢）

- 条款出处：〔§ 172.177(a)–(e)〕 + pdf-page 19
- 原文引用（英文逐字）：
  > "the sodium nitrite content of the edible portion of the finished smoked product is not less than 100 parts per million and not greater than 200 parts per million, as measured in the loin muscle."
  > —— 〔§ 172.177(b)〕[pdf-page 19]
- 方法论陈述：这是全 Part 唯一给出**完整多栅栏控制**的条款：盐 ≥3.5%（水相）、亚硝酸盐 100–200 ppm（**有下限也有上限**，因为要抑菌就必须够量）、热加工每尾鱼中心 ≥160 °F 持续 ≥30 min 且须多点监控、熏后 3 h 内降至 ≤50 °F 且 12 h 内降至 ≤38 °F、此后全程 ≤38 °F 储运、包装与运输记录须标明易腐并注明冷藏。判定要点：**这是「许可条款」却规定了工艺参数**，因此做烟熏鲢时它同时是添加剂许可依据与工艺合规依据；但**不得据此推广到其他烟熏鱼种**（条款只覆盖 smoked chub）。
- 可回答的新问题：我的烟熏鱼工艺参数是否足够？亚硝酸盐为什么有下限？取样为什么必须在 loin muscle？
- 跨域佐证：〔§ 172.175〕只给亚硝酸钠的一般限量、无工艺参数；〔§ 172.177〕才是带工艺的专条——同一物质两条并行、适用对象不同。与 Part 113/114（LACF/AF，另套编号）不互替。
- 建议归属子卡：V02

---

### CAND-FW-07: 生物类抗菌剂的「许可 vs 程序」双轨

- 条款出处：〔§ 172.785〕 + pdf-page 109
- 原文引用（英文逐字）：
  > "The additive may be safely used as an antimicrobial agent specific for Listeria monocytogenes (L. monocytogenes) in accordance with the following conditions:"
  > —— 〔§ 172.785〕[pdf-page 109]
- 方法论陈述：李斯特菌噬菌体是**被许可的食品添加剂**（六株等比例裂解型噬菌体、须保藏于认可菌种保藏中心、效力以 OD600 ≤0.06 对三株 ATCC 菌判定），不是「环境监测程序」。判定分流：**「这东西能不能作为抗菌剂用在食品上」→ 本卡；「我的 RTE 车间环境监测怎么做、检出后怎么处置」→ 环境病原控制能力**。两者不可互替：有许可不代表可以替代清洁与分区；做了环境监测也不代表该添加剂自动被许可用于该产品。同理不得因「它是噬菌体、属生物制剂」而误认为归药品或生物制品法规管辖。
- 可回答的新问题：噬菌体产品作为食品添加剂需要满足什么身份与效力要求？它能替代环境监测吗？
- 跨域佐证：〔§ 172.5(b)〕——即使有本许可，仍须遵守本法其他规定（含 CGMP 与预防控制）；〔§ 172.110〕等化学防腐剂条款无「针对特定病原」的效力判定，本条的效力判定（OD600、指定菌株）在 Part 172 中是特例。
- 建议归属子卡：V02

---

### CAND-FW-08: 甜味剂的「三重限制形态」分化

- 条款出处：〔§ 172.804〕〔§ 172.829〕〔§ 172.831〕〔§ 172.800〕 + pdf-page 113 / 125 / 127 / 111
- 原文引用（英文逐字）：
  > "The additive may be used as a sweetener in foods generally, in accordance with current good manufacturing practice in an amount not to exceed that reasonably required to accomplish the intended effect."
  > —— 〔§ 172.831(c)〕[pdf-page 127]
- 方法论陈述：同为高倍甜味剂，限制形态完全不同，不能互相套用：**三氯蔗糖**是「食品通用 + GMP 无量」；**阿斯巴甜**是「食品通用但受标准身份限制」，且对具体用途另给数值（片剂中亮氨酸 ≤3.5%、焙烤食品中 ≤0.5% 重量）；**纽甜**给的是纯度规格（assay 97.0–102.0%、铅 ≤2.0 mg/kg 等）而非用量限制。判定时必须逐条读该物质的限制属于五形态中的哪一种，**不可因「都是甜味剂」而推定同类**。
- 可回答的新问题：这三种甜味剂的合规判定方式为什么不同？哪个需要成品检测、哪个只需工艺论证？
- 跨域佐证：〔§ 172.804〕开头即写明「for which standards of identity established under section 401 ... do not preclude such use」——**标准身份优先于添加剂许可**（Part 130 未收）；〔§ 172.831(d)〕把特殊膳食用途标签义务外转 Part 105。
- 建议归属子卡：V03

---

### CAND-FW-09: 脂肪替代物的「强制营养补偿」条款

- 条款出处：〔§ 172.867(c)(d)〕 + pdf-page 154
- 原文引用（英文逐字）：
  > "To compensate for any interference with absorption of fat soluble vitamins, the following vitamins shall be added to foods containing olestra:"
  > —— 〔§ 172.867(d)〕[pdf-page 154]
- 方法论陈述：Olestra 是极少数**把「营养补偿」写成许可条件**的条款：因阻断脂溶性维生素吸收，法规要求按每克 olestra 强制添加 α-生育酚当量、视黄醇当量、维生素 D 与维生素 K1。判定要点：① 用途本身封闭（仅预包装即食咸味零食与预包装待加热爆米花仁）；② 补偿添加**不是自愿强化、是许可生效条件**，不做即属违规使用；③ 因此该产品的标签必然同时牵动营养标签与配料表（→ Part 101 层），但**补偿量本身属 Part 172 层**。这是「添加剂许可条款直接改写配方义务」的范例。
- 可回答的新问题：用 Olestra 时配方上有什么强制动作？能否以「已做营养强化」为由省略某些标签？
- 跨域佐证：〔§ 172.5(c)〕营养物质的许可不构成膳食补充有用性认定——与本条「强制补偿」形成对照：一个是「许可不等于必要」，一个是「许可附带必要」；〔§ 172.379/380〕维生素 D2/D3 属营养强化剂，其限量与用途另有限定。
- 建议归属子卡：V03

---

### CAND-FW-10: IBR 引用作为规格判定的外部依赖

- 条款出处：〔§ 172.804(b)〕〔§ 172.831(b)〕〔§ 172.785(b)(1)〕 + pdf-page 113 / 127 / 109
- 原文引用（英文逐字）：
  > "The additive meets the specifications of the Food Chemicals Codex, 7th ed. (2010), pp. 993-995, which is incorporated by reference."
  > —— 〔§ 172.831(b)〕[pdf-page 127]
- 方法论陈述：27%（43 条）的条款把纯度规格整体 `incorporated by reference` 到外部文件（Food Chemicals Codex 各版页码、厂商分析方法、ATCC 菌株）。法律上这些文件与法规正文同等效力，但**其内容既不在本 PDF、也不在本技能包**。判定纪律：只能引「须符合某文件某版本某页」，**绝不可转述具体 assay 或杂质数值**；回答用户时必须明确「规格数值需查该 IBR 文件」。这一点与「表格数值不可逐字引」是两条独立纪律。
- 可回答的新问题：这条法规有没有给我可直接核对的纯度数值？如果没有，我该去哪查？
- 跨域佐证：〔§ 172.829(b)(1)–(6)〕纽甜**不**用 IBR，而是把 6 项规格直接写在条文里——同一 Subpart 内两种做法并存；〔§ 172.785(b)(1)〕IBR 到厂商方法（Intralytix）并给 ATCC 菌株号。
- 建议归属子卡：V05

---

### CAND-FW-11: 长尾名录条款的定位规则（§172.510 / §172.515）

- 条款出处：〔§ 172.510〕〔§ 172.515〕 + pdf-page 49 / 58
- 原文引用（英文逐字，仅引结构句）：
  > "Natural flavoring substances and natural substances used in conjunction with flavors."
  > —— 〔§ 172.510〕[pdf-page 49]
- 方法论陈述：这两条约占全文 26%（366 + 834 行），主体是**上千种物质的平铺名录**，每条只给名称（部分给同义名/FEMA/CAS），用量统一回落到 GMP。因此本包**不逐物质收录**，只给三条定位规则：① 判某香料是否被许可 = 查该名录是否收录（须回原文核对拼写与同义名，本包不背书「收录状态」）；② 收录≠可任意用，仍受 §172.5(a) GMP 与「不得用于规避标准身份」等约束；③ 未收录不等于非法——可能是 GRAS（另套制度）或属其他条款。这三条规则的目的是**防止把「名录查不到」直接判成「不能用」**。
- 可回答的新问题：某个香料物质该去哪查是否被许可？查不到时能否直接判不可用？
- 跨域佐证：〔§ 172.520/530/535/540/560/575/580/585/590〕是**逐个具名**的香料类条款（有各自限值），与两条名录条款并存——即「具名条款优先于名录」。
- 建议归属子卡：V04

---

### CAND-FW-12: 食品类别封闭性 —— 「in or on specified foods」的判定含义

- 条款出处：〔§ 172.170〕〔§ 172.175〕〔§ 172.177〕〔§ 172.730〕 + pdf-page 18 / 19 / 104
- 原文引用（英文逐字）：
  > "The food additive sodium nitrate may be safely used in or on specified foods in accordance with the following prescribed conditions:"
  > —— 〔§ 172.170〕[pdf-page 18]
- 方法论陈述：`specified foods` 不是泛称，而是**紧跟其后的封闭清单**。判定链：把用户的食品逐一对照条款列举（如亚硝酸钠仅限 smoked cured tunafish / sablefish / salmon / shad + 家庭腌肉制剂），**不在清单内即不可用**，即使「同类食品」也不行（烟熏鲢有专条 §172.177，不能拿 §172.175 的 200 ppm 去套其他鱼种）。反向也成立：某条款用了 `foods generally`（如三氯蔗糖）才是开放范围。
- 可回答的新问题：我的产品算不算条款里说的那类食品？「同类不同种」能不能套用？
- 跨域佐证：〔§ 172.831(c)〕`foods generally` 开放式；〔§ 172.867(c)〕只限两类预包装零食；〔§ 172.210〕只限 fresh citrus fruit 的表面涂层。
- 建议归属子卡：V01

---

### CAND-FW-13: 二级引用链（条款之间互相指引）

- 条款出处：〔§ 172.210(b)(1)(2)〕〔§ 172.615〕〔§ 172.892〕 + pdf-page 20 / 93 / 173
- 原文引用（英文逐字）：
  > "Substances generally recognized as safe for the purpose or previously sanctioned for the purpose."
  > —— 〔§ 172.210(b)(1)〕[pdf-page 20]
- 方法论陈述：条款常以三种方式把合规条件外转：① 指向**其他 Part 172 条款**（"Complying with § 172.860" / "§ 172.862" / "§ 172.820"）；② 指向**其他制度**（GRAS / prior sanctioned，均不在本 Part）；③ 指向**其他 Part**（如特殊膳食标签转 Part 105）。判定时必须顺着引用走到终点，**不能停在第一层**——例如涂层配方合规要先解 §172.210，再解 §172.860 脂肪酸规格，再解其 IBR。这是「一个产品要满足多条 Part 172 条款」的常见成因。
- 可回答的新问题：我的配方要同时满足几条法规？引用链的终点是什么制度？
- 跨域佐证：〔§ 172.210〕多条并列引用 §172.860/862/820；〔§ 172.615〕胶基由多类物质组成、各类另有规格。
- 建议归属子卡：V04

---

### CAND-FW-14: 中间品/复配物的浓度披露义务

- 条款出处：〔§ 172.170(b)(1)(ii)〕〔§ 172.175(b)(1)(ii)〕 + pdf-page 18 / 18
- 原文引用（英文逐字）：
  > "When the additive is marketed in a suitable carrier, in addition to meeting the requirement of paragraph (c)(1) of this section, the label shall declare the percentage of the additive in the mixture."
  > —— 〔§ 172.115(c)(2)〕[pdf-page 7]
- 方法论陈述：当添加剂以**复配物/载体形式**销售（而非纯品）时，标签除名称外还须声明**该添加剂在混合物中的百分比**；若为家庭用零售包装，还须给足使用说明以保证成品不超限，部分条款另要求「Keep out of the reach of children」。判定要点：这是**对添加剂卖方的义务**，不是对成品食品标签的义务——两者常被混淆（成品配料表写法 → Part 101）。
- 可回答的新问题：我卖的是复配添加剂，标签要写什么？这些要求是给我还是给我的客户？
- 跨域佐证：〔§ 172.175(b)(1)(ii)〕同款结构；〔§ 172.730(b)(1)(2)〕只要求名称与使用说明、无浓度要求——**同类义务并非条条相同**。
- 建议归属子卡：V05

---

### CAND-FW-15: 处理物标签的「用途锁定声明」

- 条款出处：〔§ 172.730(c)〕 + pdf-page 104
- 原文引用（英文逐字）：
  > "the statement, “Brewer's Malt—To be used in the production of fermented malt beverages only”, or “Distiller's Malt—To be used in the production of distilled spirits only”, whichever is the case."
  > —— 〔§ 172.730(c)〕[pdf-page 104]
- 方法论陈述：当许可把用途锁死在一个下游行业时，法规用**处理物标签上的强制声明**来执行这个锁定。判定要点：① 这是**逐字措辞**义务（两个版本择一），不可改写成同义句；② 义务对象是**处理物（麦芽）的标签**，不是添加剂标签、也不是最终饮料标签；③ 违反后果是处理物本身失去许可前提。这是「用标签实现用途管制」的典型，和 Part 101 的「标签内容规则」是不同机制——**一个是管制手段，一个是标示义务**。
- 可回答的新问题：法规怎么保证这个添加剂不会被用到别的行业？我作为下游买家看到这句话意味着什么？
- 跨域佐证：〔§ 172.177(e)(2)〕添加剂容器须给足使用说明以保证成品合规；〔§ 172.785〕无用途锁定声明——**只有部分条款用这种机制**。
- 建议归属子卡：V05

---

### CAND-FW-16: 「不得推定安全」的三条否定式元规则

- 条款出处：〔§ 172.5(b)(c)〕 + pdf-page 5
- 原文引用（英文逐字）：
  > "The existence of a regulation prescribing safe conditions of use for a food additive shall not be construed to relieve the use of the substance from compliance with any other provision of the Act."
  > —— 〔§ 172.5(b)〕[pdf-page 5]
- 方法论陈述：§172.5 用三句否定式划定许可的边界：(a) 正向——任何许可都以 GMP 为前提；(b) 反向——许可**不免除**本法其他任何规定（危害分析、CGMP、过敏原、标签、掺假 prohibition 全部照旧）；(c) 限定——营养物质的许可**不构成**其作为膳食补充有用或必需的认定。判定要点：把这三条当**回答任何 Part 172 问题时的默认前插语**，避免用户把「法规允许」读成「安全且充分」。
- 可回答的新问题：我用了被许可的添加剂，是不是就不用做危害分析了？是不是就可以宣称有营养必要性？
- 跨域佐证：〔§ 172.5(c)〕与〔§ 172.867(d)〕强制补偿形成对照；〔§ 172.804〕标准身份限制是 (b) 的具体化实例。
- 建议归属子卡：V05

---

## 覆盖自检

| Subpart | 条款 | 覆盖的候选 |
|---|---|---|
| A | §172.5 | FW-01/02/03/16 |
| B | §172.110/115/160/170/175/177/185 | FW-01/05/06/12/14 |
| C | §172.210/215/250 | FW-04/13 |
| D | §172.320/379/380 | FW-09（对照） |
| E | §172.410/480 | FW-02（形态⑤） |
| F | §172.510/515 | FW-11 |
| G | §172.615/620/695 | FW-04/13 |
| H | §172.730/785 | FW-05/07/15 |
| I | §172.800/804/829/831/867 | FW-08/09/10/12 |

**未逐条展开的长尾**（按用户「分层主次」决策）：§172.225–280、§172.310–399、§172.520–660、§172.710–780、§172.802–898 中的低风险物质条款。这些条款**共享 FW-02/03/10/13 的模板与限制形态**，由 V04 的统一判定链覆盖，不单独出候选。