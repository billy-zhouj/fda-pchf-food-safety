# 候选池：反例提取器 | 来源 21 CFR Part 101 eCFR 2026-11-05 | 检索式取块

> 取材路径：Grep 定位 may not / shall not / no claim / does not apply / except / unless / provided that / not authorized / fails to meet / deemed misbranded / disqualifying / not exempt / shall be exempt only / prohibited / not required 等禁止性·例外·失效锚点，按局部命中读取 chunk-02 / 05 / 06 / 08 / 09 段落；chunk-04（§101.12 RACC 表）按约定只读开头 120 行。
> 引用均为转换件 `source-cfr-part101-2026.md` 的英文逐字（硬换行已归一化为空格）；§101.12 Table 1/2 数值、Appendix B/C/D 图形示例属不可逐字引用区，本池未引其数值与版式。涉及既有技能包条款（〔§ 117.xxx〕〔§ 120.xxx〕）仅写条款号，不编造该包引文。
> 条款出处统一为〔§ 101.xxx〕；pdf-page N 按转换件 `<!-- pdf-page N -->` 标记核定。建议归属子卡为五选一。

---

### CAND-CE-01: 把〔§ 101.100〕配料表豁免当成营养标签豁免
- 错误说法（一句）：产品落入 §101.100 的豁免清单，就既不用列配料表、也不用做 Nutrition Facts 营养标签。
- 正确判定（3–6 句，写清依据与边界）：§101.100(a) 开头把豁免对象钉死在 FD&C Act 403(i)(2)，即"由两种以上配料制成时逐一申报各配料通用名"的配料表义务，与营养标签无关。营养标签是普遍义务：§101.9(a) 明写凡供人食用并销售的产品一律提供营养信息，除非 (j) 给出豁免；§101.9(j) 才是营养标签的豁免清单（(1) 小额直销、(2) 餐馆食品、(18) 小企业低产量等）。两套豁免的对象、条件、法源都不同，绝不互相替代。主张豁免者必须能说出"免的是哪一条义务"，不能用"我们产品属于豁免食品"一句概括。
- 条款出处：〔§ 101.100(a)〕〔§ 101.9(a)〕〔§ 101.9(j)〕 + pdf-page 335 / 20 / 58
- 原文引用（英文逐字，≤100 词/段）：
  > The following foods are exempt from compliance with the requirements of section 403(i)(2) of the act (requiring a declaration on the label of the common or usual name of each ingredient when the food is fabricated from two or more ingredients).
  > Nutrition information relating to food shall be provided for all products intended for human consumption and offered for sale unless an exemption is provided for the product in paragraph (j) of this section.
  > The following foods are exempt from this section or are subject to special labeling requirements:
  （§101.100(a), pdf-page 335；§101.9(a), pdf-page 20；§101.9(j), pdf-page 58）
- 后果（答错会导致什么）：直接漏做 Nutrition Facts，构成 §403(q) 意义上的错标；在进口扣留与标签审核中会被判整批不合规，且因豁免对象搞错而答不出举证依据。
- 建议归属子卡：豁免与效力层

---

### CAND-CE-02: 把 Part 117 qualified facility 主体豁免与 Part 101 标签义务豁免混为一谈
- 错误说法（一句）：企业是 Part 117 的 qualified facility（合格设施/主体豁免），所以 Part 101 的标签义务也一并免除。
- 正确判定（3–6 句，写清依据与边界）：Part 101 的豁免都是"针对具体标签义务、针对具体产品"的精确豁免：§101.100 免 403(i)(2) 配料表，§101.9(j) 免营养标签，§101.108 免经 FDA 书面批准的临时实验，且 §101.108(d) 明写豁免须"针对具体法规、具体产品"授予。§101.9(j)(18) 的小企业低产量豁免本身以雇员数与销量为条件、须事先申报，并非对"企业主体"一次性授予的资格。Part 117 的 qualified facility 属于另一套制度的主体豁免〔§ 117.5〕，与标签义务豁免不在同一法源、不互相推出。两套条款号不得互引替代。
- 条款出处：〔§ 101.100(a)〕〔§ 101.9(j)(18)〕〔§ 101.108(d)〕；并列既有包〔§ 117.5〕（仅条款号，不引该包文字） + pdf-page 335 / 65 / 341
- 原文引用（英文逐字，≤100 词/段）：
  > Approval for food labeling experiments will be given by FDA in writing. Foods labeled in violation of existing regulations will be subject to regulatory action unless an FDA-approved exemption to the specific regulation has been granted for that specific product.
  > whose labels, labeling, and advertising do not provide nutrition information or make a nutrient content or health claim.
  （§101.108(d), pdf-page 341；§101.9(j)(18), pdf-page 65）
- 后果（答错会导致什么）：把主体豁免错当标签免死金牌，导致营养标签、配料表、声称闸门整体漏判；同时会把 Part 117 条款号写进 Part 101 判定，污染效力层与路由表。
- 建议归属子卡：豁免与效力层

---

### CAND-CE-03: 以为「标签合规」等于「食品安全合规」（403 misbranding vs 402 adulteration 两条钩子）
- 错误说法（一句）：Nutrition Facts 和配料表都做对了，这个产品就"合规/安全"了。
- 正确判定（3–6 句，写清依据与边界）：Part 101 全篇的执法落点是 FD&C Act §403 misbranding（错标）：§101.9(k) 写"deemed to be misbranded under sections 201(n) and 403(a)"，§101.18、§101.91(b) 同样以 misbranded 收口。产品是否被污染、是否掺假属 FD&C Act §402 adulteration 与 Part 117 预防控制领域。§101.100(d)(2)/(e)(1) 把 "adulterated or misbranded" 并列，正说明二者是彼此独立的判定：一张完全合规的 Nutrition Facts 完全可能伴随高危产品（BOOK_OVERVIEW 第 3 节"最强反对意见"）。标签正确不豁免危害分析、过敏原标签控制〔§ 117.135(c)(2)〕、5-log 工艺等过程义务；反过来标签写错也不必然意味着产品掺假。
- 条款出处：〔§ 101.9(k)〕〔§ 101.18(a)〕〔§ 101.100(d)(2)〕〔§ 101.100(e)(1)〕；并列既有包〔§ 117.135(c)(2)〕（仅条款号） + pdf-page 67 / 219 / 337 / 338
- 原文引用（英文逐字，≤100 词/段）：
  > A food labeled under the provisions of this section shall be deemed to be misbranded under sections 201(n) and 403(a) of the act if its label or labeling represents, suggests, or implies:
  > as will ensure, if such specifications are followed, that such food will not be adulterated or misbranded within the meaning of the act upon completion of such processing, labeling, or repacking.
  > An exemption of a shipment or other delivery of a food under paragraph (d) (1) or (3) of this section shall, at the beginning of the act of removing such shipment or delivery, or any part thereof, from such establishment become void ab initio if the food comprising such shipment, delivery, or part is adulterated or misbranded within the meaning of the act when so removed.
  （§101.9(k), pdf-page 67；§101.100(d)(2), pdf-page 337；§101.100(e)(1), pdf-page 338）
- 后果（答错会导致什么）：这是本次升级最危险的红线——把"信息合规"当"食品安全"，会诱导用户跳过危害分析与预防控制，产出"标签漂亮但产品高危"的合规假象，正是阶段 0 要求写进每个能力卡 B 段的反面。
- 建议归属子卡：豁免与效力层

---

### CAND-CE-04: 以为暗示性表述 / 品牌名 / 符号不算 claim
- 错误说法（一句）：只要不直说"low fat""low sodium"，用"healthy"、含 heart 的品牌名、心形符号或第三方文献引用就不算声称。
- 正确判定（3–6 句，写清依据与边界）：§101.13(b) 明写"expressly or implicitly"表征营养素水平的说法都受管，§101.13(b)(2) 进一步定义 implied claim 包括"描述食品暗示某营养素缺失或存在某量（如 high in oat bran）"与"暗示有助维持健康饮食习惯（如 healthy）"。§101.14(a)(1) 对健康声称把 "third party" references、含 heart 字样的品牌名、heart symbol、vignettes 逐项明文算作 claim。品牌名里使用暗示性营养素含量声称还须 FDA 授权（§101.13(q)(7)）。仅在餐厅等极窄场景、且不表征营养素水平并有紧邻说明时，符号才可能不算（§101.13(q)(5)(iii)），不能推广到零售包装。
- 条款出处：〔§ 101.13(b)〕〔§ 101.13(b)(2)〕〔§ 101.14(a)(1)〕〔§ 101.13(q)(7)〕 + pdf-page 199 / 206
- 原文引用（英文逐字，≤100 词/段）：
  > A claim that expressly or implicitly characterizes the level of a nutrient of the type required to be in nutrition labeling under § 101.9 or under § 101.36 (that is, a nutrient content claim) may not be made on the label or in labeling of foods unless the claim is made in accordance with this regulation and with the applicable regulations in subpart D of this part or in part 105 or part 107 of this chapter.
  > An implied nutrient content claim is any claim that: (i) Describes the food or an ingredient therein in a manner that suggests that a nutrient is absent or present in a certain amount (e.g., “high in oat bran”); or (ii) Suggests that a food, because of its nutrient content, may be useful in maintaining healthy dietary practices, where there is also implied or explicit information about the nutrition content of the food (e.g., “healthy”).
  > Health claim means any claim made on the label or in labeling of a food, including a dietary supplement, that expressly or by implication, including “third party” references, written statements (e.g., a brand name including a term such as “heart”), symbols (e.g., a heart symbol), or vignettes, characterizes the relationship of any substance to a disease or health-related condition.
  > Implied nutrient content claims may be used as part of a brand name, provided that the use of the claim has been authorized by the Food and Drug Administration.
  （§101.13(b)/(b)(2), pdf-page 199；§101.14(a)(1)/§101.13(q)(7), pdf-page 206）
- 后果（答错会导致什么）：整条声称闸门被绕过——品牌名、包装图形、随附宣传单里的暗示语全部漏审，构成未授权声称并触发 misbranding；这是最易漏判的一类。
- 建议归属子卡：声称闸门

---

### CAND-CE-05: 以为做了 Part 120 5-log 就免〔§ 101.17(g)〕警示，或反过来以为贴了警示就等于做了 5-log
- 错误说法（一句）：果汁已按 Part 120 做 5-log 就不需要警示；或者贴了未巴氏杀菌警示就等于完成了杀菌工艺要求。
- 正确判定（3–6 句，写清依据与边界）：§101.17(g)(2) 要求未按 (g)(7) 方式处理的果汁/含果汁饮料带固定 WARNING 声明；§101.17(g)(7)(i) 规定达到"至少 5-log 减少"或"不低于果汁 HACCP 最终规则所定过程控制准则"的工艺，可使 (g) 的警示要求不适用。但这是"标签警示义务的免除条件"，不是"工艺义务已完成的证明"。贴警示只履行 §403 标签义务，Part 120〔§ 120.24〕的 5-log/HACCP 义务仍独立存在；达到 5-log 仅使 (g) 警示不适用，不自动免除 §101.30 果汁百分比声明等其它标签义务，且 (g)(3) 对非零售/异地加工果汁即便不带警示也须随附单据披露未处理事实。(g)(7) 还要求该减少量在整个货架期（含正常与中度滥用条件）维持，不是一次性检测值。
- 条款出处：〔§ 101.17(g)(2)〕〔§ 101.17(g)(3)〕〔§ 101.17(g)(7)〕〔§ 101.30〕；并列既有包〔§ 120.24〕（仅条款号） + pdf-page 214
- 原文引用（英文逐字，≤100 词/段）：
  > WARNING: This product has not been pasteurized and, therefore, may contain harmful bacteria that can cause serious illness in children, the elderly, and persons with weakened immune systems.
  > The warning statement required by this paragraph (g) shall not apply to juice that is not for distribution to retail consumers in the form shipped and that is for use solely in the manufacture of other foods or that is to be processed, labeled, or repacked at a site other than originally processed, provided that for juice that has not been processed in the manner described in paragraph (g)(7) of this section, the lack of such processing is disclosed in documents accompanying the juice, in accordance with the practice of the trade.
  > The requirements in this paragraph (g) shall not apply to a juice that has been processed in a manner that will produce, at a minimum, a reduction in the pertinent microorganism for a period at least as long as the shelf life of the product when stored under normal and moderate abuse conditions, of the following magnitude: (A) A 5-log (i.e., 100,000-fold) reduction;
  > (B) A reduction that is equal to, or greater than, the criterion established for process controls by any final regulation requiring the application of Hazard Analysis and Critical Control Point (HACCP) principles to the processing of juice.
  （§101.17(g)(2)/(g)(3)/(g)(7)(i), pdf-page 214）
- 后果（答错会导致什么）：双向误判——或把"贴了警示"当"做了 5-log"而实际跳过 Part 120 工艺控制，或把"5-log 达标"当"所有标签义务免除"而漏掉果汁百分比声明与随单披露；三层接口（工艺→标签→检查取证）任一层断点都会造成执法漏洞。
- 建议归属子卡：特定品类与警示

---

### CAND-CE-06: 以为 incidental additives 一律免申报（亚硫酸盐 10 ppm 例外）
- 错误说法（一句）：只要是" incidental additive / 加工助剂"，配料表里就一律不用写。
- 正确判定（3–6 句，写清依据与边界）：§101.100(a)(3) 免的是"存在量不显著且在该食品中无技术或功能效果"的 incidental additives，有两个并列前提，并列举三类（随其它食品配料带入、加工助剂、设备/包装迁移物）。亚硫酸盐另按 (a)(4) 特别判定：即便无技术效果，也只有在成品中"无可检出量"才算 insignificant；而"可检出量"被定义为 ≥10 ppm。因此 ≥10 ppm 的亚硫酸盐必须申报，不因"incidental"自动免。这是定量阈值压倒一般性豁免的例外，不得把 (a)(3) 的宽松口径套到 (a)(4)。
- 条款出处：〔§ 101.100(a)(3)〕〔§ 101.100(a)(4)〕 + pdf-page 336
- 原文引用（英文逐字，≤100 词/段）：
  > Incidental additives that are present in a food at insignificant levels and do not have any technical or functional effect in that food.
  > For the purposes of paragraph (a)(3) of this section, any sulfiting agent (sulfur dioxide, sodium sulfite, sodium bisulfite, potassium bisulfite, sodium metabisulfite, and potassium metabisulfite) that has been added to any food or to any ingredient in any food and that has no technical effect in that food will be considered to be present in an insignificant amount only if no detectable amount of the agent is present in the finished food. A detectable amount of sulfiting agent is 10 parts per million (ppm or mg/kg) or more of the sulfite in the finished food.
  （§101.100(a)(3)/(a)(4), pdf-page 336）
- 后果（答错会导致什么）：亚硫酸盐过敏人群暴露风险直接漏标；配料表因漏申报构成错标，并与 §101.17 的亚硫酸盐警示义务、过敏原控制〔§ 117.135(c)(2)〕同时失守。
- 建议归属子卡：豁免与效力层

---

### CAND-CE-07: 以为健康声称只要「有研究支持」即可（须 SSA + 不超 disqualifying level + 落在已授权模型）
- 错误说法（一句）：某物质与疾病的关系有论文/有研究支持，就可以在标签上写健康声称。
- 正确判定（3–6 句，写清依据与边界）：健康声称是"负面清单 + 正面授权"双闸。§101.14(c) 要求 FDA 基于"全部公开可得科学证据"认定存在 significant scientific agreement（SSA，合格科学专家间的显著科学一致）才会制定授权法规，这不是"有论文"。§101.14(e) 明写任何明示或暗示健康声称均不得作出，除非：① 落在 Subpart E 已授权模型内；② 符合通则与 Subpart E 具体条款；③ 未超 §101.14(a)(4) 的 disqualifying level；④ 不含不适当水平物质；⑤ 非婴幼儿食品；⑥ 营养充足性门槛（含 ≥10% RDI/DRV 的维生素 A/C/铁/钙/蛋白/纤维，添加前）。§101.71 还明文列出"未授权"的声称（膳食纤维与心血管病、锌与老年人免疫功能），有研究也不可用。声称资格是"先过负面门槛"，不是只满足正面条件。
- 条款出处：〔§ 101.14(c)〕〔§ 101.14(e)〕〔§ 101.14(a)(4)〕〔§ 101.71〕〔§ 101.70〕 + pdf-page 207 / 209 / 206 / 295
- 原文引用（英文逐字，≤100 词/段）：
  > FDA will promulgate regulations authorizing a health claim only when it determines, based on the totality of publicly available scientific evidence (including evidence from well-designed studies conducted in a manner which is consistent with generally recognized scientific procedures and principles), that there is significant scientific agreement, among experts qualified by scientific training and experience to evaluate such claims, that the claim is supported by such evidence.
  > Prohibited health claims. No expressed or implied health claim may be made on the label or in labeling for a food, regardless of whether the food is in conventional food form or dietary supplement form, unless: (1) The claim is specifically provided for in subpart E of this part; and
  > Disqualifying nutrient levels means the levels of total fat, saturated fat, cholesterol, or sodium in a food above which the food will be disqualified from making a health claim.
  > Health claims not authorized for foods in conventional food form or for dietary supplements of vitamins, minerals, herbs, or other similar substances: (a) Dietary fiber and cardiovascular disease. (b) Zinc and immune function in the elderly.
  （§101.14(c), pdf-page 207；§101.14(e), pdf-page 209；§101.14(a)(4), pdf-page 206；§101.71, pdf-page 295）
- 后果（答错会导致什么）：作出未授权疾病关系声称，直接触发 §101.9(k) 的"防治疾病"类 deemed misbranded；还会因忽略 disqualifying level 把高脂/高钠产品错误放行到健康声称。
- 建议归属子卡：声称闸门

---

### CAND-CE-08: 以为「免标」= 可以随意写营养 / 健康声称
- 错误说法（一句）：我们产品本来就不用贴营养标签，那标签上写点"低脂""高钙""有助健康"也不受管。
- 正确判定（3–6 句，写清依据与边界）：§101.9(j) 的营养标签豁免几乎都以"不作任何营养声称或营养信息"为存续条件。§101.9(j)(1)(i) 小额直销、(j)(2)(i) 餐馆食品、(j)(18) 小企业低产量豁免，都写 "Provided, That the food bears no nutrition claims or other nutrition information in any context on the label or in labeling or advertising"，且明写一旦作声称即"subject the food to the provisions of this section"。也就是说，作声称的那一刻豁免即丧失，须回全套 §101.9 / §101.10 / §101.11。§101.9(k) 还规定即便按本节标注，只要标签/标签说明"代表、暗示或意味"食品可防治疾病，仍 deemed misbranded，疾病关系信息只能依 §101.14 与 Subpart E 提供。免的是"标"，不是"说"。
- 条款出处：〔§ 101.9(j)(1)〕〔§ 101.9(j)(2)〕〔§ 101.9(j)(18)〕〔§ 101.9(k)〕 + pdf-page 58 / 65 / 67
- 原文引用（英文逐字，≤100 词/段）：
  > Provided, That the food bears no nutrition claims or other nutrition information in any context on the label or in labeling or advertising. Claims or other nutrition information subject the food to the provisions of this section, § 101.10, or § 101.11, as applicable.
  > Served in restaurants, Provided, That the food bears no nutrition claims or other nutrition information in any context on the label or in labeling or advertising. Claims or other nutrition information subject the food to the provisions of this section;
  > (1) That the food, because of the presence or absence of certain dietary properties, is adequate or effective in the prevention, cure, mitigation, or treatment of any disease or symptom. Information about the relationship of a dietary property to a disease or health-related condition may only be provided in conformance with the requirements of § 101.14 and part 101, subpart E.
  （§101.9(j)(1)(i)/(j)(2)(i), pdf-page 58；§101.9(k)(1), pdf-page 67）
- 后果（答错会导致什么）：误把豁免当"表达自由"，作出声称后既不补营养标签也不受声称闸门约束，一处措辞同时击穿豁免条件与 misbranding 两条；小企业还会因此丧失本可主张的低产量豁免。
- 建议归属子卡：营养标签与份量

---

### CAND-CE-09: 把〔§ 101.12〕RACC 表值当企业内控限值 / 把 serving size 当厂商建议食用量
- 错误说法（一句）：§101.12 的 RACC 表就是份量标准，可以直接抄进企业内控规格、危害分析限值或"建议食用量"。
- 正确判定（3–6 句，写清依据与边界）：§101.9(b)(1) 把 serving/serving size 定义为"4 岁以上人群每次进食惯常消费量"，以适宜的家庭常用量表达，不是营养建议、不是厂商自由裁量；§101.9(b)(2) 规定标签 serving size 须由 §101.12(b) 的 RACC 推导。§101.12(a)(1) 说明 RACC 来自全国食物消费调查、反映惯常消费量，是监管比较基准，被声称阈值、Daily Value、disqualifying level 反复引用。它是比较分母，不是工艺参数、不是危害分析输入，也不能当企业内控限值。§101.12 的 Table 1/2 数值在转换件中属不可逐字引用区，须回原表并核对快照日期（BOOK_OVERVIEW 第 1/4 节）。脱离 RACC 谈"低脂/高纤"无意义。
- 条款出处：〔§ 101.9(b)(1)〕〔§ 101.9(b)(2)〕〔§ 101.12(a)(1)〕〔§ 101.12(b)〕〔§ 101.13(h)(1)〕 + pdf-page 21 / 20 / 82 / 83
- 原文引用（英文逐字，≤100 词/段）：
  > The term serving or serving size means an amount of food customarily consumed per eating occasion by persons 4 years of age or older which is expressed in a common household measure that is appropriate to the food.
  > serving size declared on a product label shall be determined from the “Reference Amounts Customarily Consumed Per Eating Occasion * * * *” (reference amounts) that appear in § 101.12(b)
  > FDA calculated the reference amounts for persons 4 years of age or older to reflect the amount of food customarily consumed per eating occasion by persons in this population group. These reference amounts are based on data set forth in appropriate national food consumption surveys.
  > The following reference amounts shall be used as the basis for determining serving sizes for specific products:
  （§101.9(b)(1)/(b)(2), pdf-page 21；§101.12(a)(1), pdf-page 82；§101.12(b), pdf-page 83）
- 后果（答错会导致什么）：把监管比较基准误当生产控制限值，会让危害分析与声称资格计算全盘错位；还会去逐字引 §101.12 表格数值（不可引用区）或把 2016 新规前的旧 RACC 当成现行值。
- 建议归属子卡：营养标签与份量

---

### CAND-CE-10: 把 Ed.5 guidance 的 Big 9 / allergen-free 规则写成〔§ 101.xxx〕（法源不同）
- 错误说法（一句）：过敏原 Ed.5 指南的 Big 9、allergen-free / "不含过敏原"声明规则，就是 §101.xxx 的法规要求。
- 正确判定（3–6 句，写清依据与边界）：本包内〔§ 101.xxx〕是第七套独立编号、法规正文层；Ed.5 guidance 属"指南（should 建议层）"，Big 9 与 allergen-free 声明规则不在 Part 101 正文，效力栈不同，不得写成〔§ 101.xxx〕。Part 101 中与"无过敏原"最接近的是 §101.91 的 gluten-free：它是独立的定量阈值定义（不含特定谷物/成分，且不可避免麸质存在 below 20 ppm），并有专门失格条款 §101.91(b)；它不等于 FALCPA 的法定过敏原定义（在 FD&C Act §201(qq)/§403(w)，本件"转引未收"），也不等于 Ed.5 的 allergen-free。§101.91(d) 还规定联邦优先，州不得另设不同定义。把指南规则贴成法条号，会直接污染 CAP-14 的效力栈与 CAP-30 的来源路由。
- 条款出处：〔§ 101.91(a)(3)〕〔§ 101.91(b)〕〔§ 101.91(d)〕〔§ 101.100(a)〕；并列既有包〔§ 117.135(c)(2)〕（仅条款号） + pdf-page 331 / 332 / 335
- 原文引用（英文逐字，≤100 词/段）：
  > Any unavoidable presence of gluten in the food bearing the claim in its labeling is below 20 ppm gluten (i.e., below 20 mg gluten per kg of food).
  > A food that bears the claim “gluten-free” in its labeling and fails to meet the requirements of paragraph (a)(3) of this section and, if applicable, paragraphs (c)(2) through (4) of this section will be deemed misbranded.
  > A State or political subdivision of a State may not establish or continue into effect any law, rule, regulation, or other requirement that is different from the requirements in this section for the definition and use of the claim “gluten-free,” as well as the claims “no gluten,” “free of gluten,” or “without gluten.”
  （§101.91(a)(3)(B)(ii)/(b)(1), pdf-page 331；§101.91(d), pdf-page 332）
- 后果（答错会导致什么）：法源错配——把建议层当法规义务、把 gluten-free 阈值当 allergen-free 判据，会在能力卡里写入不存在的〔§ 101.xxx〕条款号，并误导过敏原标签控制〔§ 117.135(c)(2)〕的取证依据。
- 建议归属子卡：豁免与效力层

---

### CAND-CE-11: 以为 "light"/"lite"/"percent fat free" 只要真实就能用
- 错误说法（一句）：产品确实比参照食品淡/低，"light""lite""95% fat free" 如实写就合规。
- 正确判定（3–6 句，写清依据与边界）：§101.60(e) 明写除 (b)–(d) 情形外，"light"/"lite" 不得用于未减脂 50%（或热量减 1/3、钠减 50%）的食品，除非它只描述物理/感官属性（如 light in color）且限定词与 "light" 同字号、同色、紧邻；§101.60(b)(4) 还禁止在参照食品已属"低脂且低热量"时作 light 声称。§101.13(i)(4) 明写 "Percent fat free" claims are not authorized by this paragraph，须按 §101.62(b)(6)。逐词描述符不是"真实即可"，而是必须落在 Subpart D 的授权定义内；真实但未定义/未授权的措辞同样构成未授权声称。
- 条款出处：〔§ 101.60(e)〕〔§ 101.60(b)(4)〕〔§ 101.13(i)(4)〕〔§ 101.62(b)(6)〕 + pdf-page 252 / 251 / 201
- 原文引用（英文逐字，≤100 词/段）：
  > Except as provided in paragraphs (b) through (d) of this section, the term “light” or “lite” may not be used to refer to a food that is not reduced in fat by 50 percent, or, if applicable, in calories by 1⁄3 or, when properly qualified, in sodium by 50 percent unless:
  > A “light” claim may not be made on a food for which the reference food meets the definition of “low fat” and “low calorie.”
  > “Percent fat free” claims are not authorized by this paragraph. Such claims shall comply with § 101.62(b)(6).
  （§101.60(e), pdf-page 252；§101.60(b)(4), pdf-page 251；§101.13(i)(4), pdf-page 201）
- 后果（答错会导致什么）：把"事实陈述"误当"授权描述符"，作出 Subpart D 未定义的相对/百分比声称，触发 §101.13(b) 的未合规声称与 misbranding。
- 建议归属子卡：声称闸门

---

### CAND-CE-12: 以为健康声称里的 heart 符号 / 第三方引用不必配完整声称
- 错误说法（一句）：在正面放个心形符号或引一句第三方研究即可，完整健康声称放在附页/背面就行。
- 正确判定（3–6 句，写清依据与边界）：§101.14(a)(1) 已把符号、vignette、第三方引用本身算作健康声称（见 CAND-CE-04）。§101.14(d)(2)(iv) 进一步要求：若构成明示或暗示健康声称的图形材料（如 heart symbol）出现在 label 或 labeling 上，则 reference statement 或完整声称须"紧邻"该图形出现；同时完整声称的所有信息须集中一处、无其它插入材料。§101.14(d)(2)(iii) 还要求声称 complete、truthful、not misleading。因此不能"符号吸睛、完整声称藏附页"。
- 条款出处：〔§ 101.14(a)(1)〕〔§ 101.14(d)(2)(iii)〕〔§ 101.14(d)(2)(iv)〕 + pdf-page 206 / 208
- 原文引用（英文逐字，≤100 词/段）：
  > All information required to be included in the claim appears in one place without other intervening material, except that the principal display panel of the label or labeling may bear the reference statement,
  > The claim is complete, truthful, and not misleading.
  > Provided that, where any graphic material (e.g., a heart symbol) constituting an explicit or implied health claim appears on the label or labeling, the reference statement or the complete claim shall appear in immediate proximity to such graphic material;
  （§101.14(d)(2)(iii)/(iv), pdf-page 208）
- 后果（答错会导致什么）：图形本身构成未完整配置的健康声称，被判误导性错标；即便文字声称本身已授权，也会因位置/显著性不合规而失守。
- 建议归属子卡：声称闸门

---

### CAND-CE-13: 以为 §101.108 临时实验豁免可自行实施 / 免标即可偏离现行法规
- 错误说法（一句）：想试新版 Nutrition Facts 版式，先在货架上改着用、边卖边报备 FDA 即可。
- 正确判定（3–6 句，写清依据与边界）：§101.108 的临时豁免须企业主动提交书面提案，逐项说明格式、起止日期、地域、有效性度量、被豁免条款清单等九项信息（(b)），且按 §10.30 以 citizen petition 提交（(c)）。§101.108(d) 明写"FDA 书面批准"才生效，并规定"Foods labeled in violation of existing regulations will be subject to regulatory action unless an FDA-approved exemption to the specific regulation has been granted for that specific product"。豁免严格限于"具体法规 + 具体产品"，不得自行扩张、不得超出提案结束日期（(b)(4) 要求承诺不经批准不延长）。
- 条款出处：〔§ 101.108(b)〕〔§ 101.108(c)〕〔§ 101.108(d)〕 + pdf-page 341
- 原文引用（英文逐字，≤100 词/段）：
  > Any firm that intends to undertake a labeling experiment that requires exemptions from certain requirements of §§ 101.9 and 105.66 of this chapter should submit a written proposal containing a thorough discussion of each of the following information items that apply to the particular experiment:
  > The proposal should be clearly identified as a request for a temporary exemption for purposes of conducting authorized food labeling experiments and submitted as a citizen petition under § 10.30 of this chapter.
  > Approval for food labeling experiments will be given by FDA in writing. Foods labeled in violation of existing regulations will be subject to regulatory action unless an FDA-approved exemption to the specific regulation has been granted for that specific product.
  （§101.108(b)/(c)/(d), pdf-page 341）
- 后果（答错会导致什么）：未经批准即偏离现行 Nutrition Facts 格式，整批按违反现行法规处置；把"实验"当"免标"还会连带引出 CAND-CE-08 的声称失效问题。
- 建议归属子卡：豁免与效力层

---

### CAND-CE-14: 以为异地加工 / 散装豁免一次授予便永久有效，期间 adulterated 或 misbranded 也不受影响
- 错误说法（一句）：签了异地加工/再包装协议，货在途和暂存期间怎么标、甚至掺假错标都无所谓，豁免一直有效。
- 正确判定（3–6 句，写清依据与边界）：§101.100(d) 的异地加工/贴标/再包装豁免以书面协议为条件（含加工规格、双方留存 2 年备查），且规格须"确保完成后食品不 adulterated or misbranded"（(d)(2)）。§101.100(e)(1) 明写：一旦移出该场所时食品 adulterated 或 misbranded，豁免"自始无效（void ab initio）"；(e)(2) 规定拒绝出示协议即对该引入人自始无效；(e)(3) 规定移出时掺假/错标或拒查即到期。豁免是有条件、可追溯撤销的，不是一次授予的永久护身符，且再次印证掺假（§402）与错标（§403）是两条独立钩子。
- 条款出处：〔§ 101.100(d)〕〔§ 101.100(e)(1)〕〔§ 101.100(e)(2)〕〔§ 101.100(e)(3)〕 + pdf-page 337 / 338
- 原文引用（英文逐字，≤100 词/段）：
  > An exemption of a shipment or other delivery of a food under paragraph (d) (1) or (3) of this section shall, at the beginning of the act of removing such shipment or delivery, or any part thereof, from such establishment become void ab initio if the food comprising such shipment, delivery, or part is adulterated or misbranded within the meaning of the act when so removed.
  > An exemption of a shipment or other delivery of a food under paragraph (d) (2) or (3) of this section shall become void ab initio with respect to the person who introduced such shipment or delivery into interstate commerce upon refusal by such person to make available for inspection a copy of the agreement, as required by paragraph (d) (2) or (3) of this section.
  （§101.100(e)(1)/(e)(2), pdf-page 338）
- 后果（答错会导致什么）：把在途/暂存豁免当"无监管区"，一旦出问题豁免自始无效、追溯全批；协议未留存 2 年还会当场失效，进口与异地加工环节极易踩中。
- 建议归属子卡：豁免与效力层

---

### CAND-CE-15: 以为「gluten-free」只是「无添加」营销词 / 失格不算错标
- 错误说法（一句）：没主动加含麸质原料就能标 gluten-free，标了不达标也只是措辞问题、不算违法。
- 正确判定（3–6 句，写清依据与边界）：§101.91(a)(3) 给的是定量定义：不含特定谷物/成分，且不可避免的麸质存在 below 20 ppm（(a)(3)(B)(ii)）。§101.91(b)(1)(2) 明写用 "gluten-free"/"no gluten"/"free of gluten"/"without gluten" 而不满足 (a)(3) 者 will be deemed misbranded；§101.91(b)(3) 还规定配料表或 "Contains wheat" 中出现 wheat 又标 gluten-free 同样 deemed misbranded，除非按该款加星号说明"小麦已经过处理以符合 FDA 无麸质要求"。§101.91(c) 对发酵/水解/蒸馏食品在无可检测方法时要求留存记录至少 2 年备查。20 ppm 是法定阈值，不是营销口径，"无添加"不等于"合规"。
- 条款出处：〔§ 101.91(a)(3)〕〔§ 101.91(b)(1)〕〔§ 101.91(b)(2)〕〔§ 101.91(b)(3)〕〔§ 101.91(c)(4)〕 + pdf-page 330 / 331
- 原文引用（英文逐字，≤100 词/段）：
  > Any unavoidable presence of gluten in the food bearing the claim in its labeling is below 20 ppm gluten (i.e., below 20 mg gluten per kg of food).
  > A food that bears the claim “gluten-free” in its labeling and fails to meet the requirements of paragraph (a)(3) of this section and, if applicable, paragraphs (c)(2) through (4) of this section will be deemed misbranded.
  > A food that bears the claim “no gluten,” “free of gluten,” or “without gluten” in its labeling and fails to meet the requirements of paragraph (a)(3) of this section and, if applicable, paragraphs (c)(2) through (4) of this section will be deemed misbranded.
  > A food that bears the term “wheat” in the ingredient list or in a separate “Contains wheat” statement in its labeling, as required by 21 U.S.C. 343(w)(1)(A), and also bears the claim “gluten-free” or a claim identified in paragraph (b)(2) of this section will be deemed misbranded unless
  （§101.91(a)(3)(B)(ii)/(b)(1)/(b)(2)/(b)(3), pdf-page 331）
- 后果（答错会导致什么）：麸质相关疾病人群暴露风险，且"失格即 deemed misbranded"是法规明文，不是可协商的措辞瑕疵；漏做 20 ppm 验证或记录留存会同时失守 §101.91(b) 与 (c)。
- 建议归属子卡：声称闸门

---

### CAND-CE-16: 以为婴幼儿 / 幼儿食品可作营养素含量或健康声称
- 错误说法（一句）：婴幼儿辅食标"强化钙""高纤""有助发育"是常见卖点，Part 101 管不着。
- 正确判定（3–6 句，写清依据与边界）：§101.13(b)(3) 明写除 (q)(3) 的维矿物质百分比声称外，不得对专供 2 岁以下婴幼儿的食品作营养素含量声称，除非 parts 101/105/107 有专门规定。§101.14(e)(5) 对健康声称同样要求"标签不得代表或意味食品供 2 岁以下婴幼儿"，除非 Subpart E 专门授权。§101.13(q)(7) 另要求品牌名中的暗示性声称须经 FDA 授权。这是硬禁区，不是"真实即可"或"有研究即可"能打通的。
- 条款出处：〔§ 101.13(b)(3)〕〔§ 101.14(e)(5)〕〔§ 101.13(q)(7)〕 + pdf-page 199 / 209 / 206
- 原文引用（英文逐字，≤100 词/段）：
  > Except for claims regarding vitamins and minerals described in paragraph (q)(3) of this section, no nutrient content claims may be made on food intended specifically for use by infants and children less than 2 years of age unless the claim is specifically provided for in parts 101, 105, or 107 of this chapter.
  > The label does not represent or purport that the food is for infants and toddlers less than 2 years of age except if the claim is specifically provided for in subpart E of this part; and
  （§101.13(b)(3), pdf-page 199；§101.14(e)(5), pdf-page 209）
- 后果（答错会导致什么）：儿童食品最常被营销话术踩中的禁区，答错会直接放行法规明文禁止的声称，构成 misbranding 并可能牵连特殊膳食用途判定。
- 建议归属子卡：声称闸门

---

### CAND-CE-17: 以为 shell eggs 贴了 safe handling 就等于已杀菌 / 或经过杀菌仍须贴
- 错误说法（一句）：带壳蛋贴了 SAFE HANDLING INSTRUCTIONS 就等于做过杀菌；或反过来，已杀菌的蛋也必须照贴。
- 正确判定（3–6 句，写清依据与边界）：§101.17(h)(1) 要求所有带壳蛋（无论州际内）带 SAFE HANDLING INSTRUCTIONS 声明；但 §101.17(h)(4) 明写"在分销给消费者前经专门处理杀灭所有活沙门氏菌的带壳蛋，豁免 (h) 要求"。所以"贴警示"是标签义务，"已完成杀菌处理"是工艺事实且可反向免除该标签义务，二者不能互推。这与果汁 §101.17(g) 的 5-log 逻辑同构：警示不替代工艺，工艺达标可使警示不适用（但仍受其它标签义务约束，如 (h)(5) 对非直售蛋允许随发票/提单提供声明）。
- 条款出处：〔§ 101.17(h)(1)〕〔§ 101.17(h)(4)〕〔§ 101.17(h)(5)〕 + pdf-page 214 / 215
- 原文引用（英文逐字，≤100 词/段）：
  > The label of all shell eggs, whether in intrastate or interstate commerce, shall bear the following statement:
  > Shell eggs that have been, before distribution to consumers, specifically processed to destroy all viable Salmonella shall be exempt from the requirements of paragraph (h) of this section.
  （§101.17(h)(1), pdf-page 214；§101.17(h)(4), pdf-page 215）
- 后果（答错会导致什么）：或把"贴了警示"当"已杀菌"而放松 Salmonella 控制，或对已杀菌蛋多贴/错贴造成声明冲突；两类都误读了"工艺义务 ↔ 标签义务"的分层。
- 建议归属子卡：特定品类与警示

---

### CAND-CE-18: 以为 §101.18 misbranding 只管「瓶身那张标签」/ 品名含部分配料名不算误导
- 错误说法（一句）：所有配料名都在别处如实列了，品名里只提一两种配料（或暗示产地）就不会误导。
- 正确判定（3–6 句，写清依据与边界）：§101.18(b) 明写 labeling 中含两种以上配料食品，若其名称"包含或暗示一种或多种但非全部配料的名称"，即便全部配料名在 labeling 别处已列出，仍可构成 misleading 并致 misbranded；§101.18(a) 把"对另一食品或药品、器械、化妆品的虚假或误导性陈述"列为错标情形。这印证 "labeling" 含随附全部文字/图形/宣传物（FD&C Act §201(n) 定义，本件转引未收），不是只有 PDP 那张标签。"别处已如实列出"不能治愈品名本身的误导；§101.15 的显著性要求同样适用于 label or labeling。
- 条款出处：〔§ 101.18(a)〕〔§ 101.18(b)〕〔§ 101.15(a)〕 + pdf-page 219 / 210
- 原文引用（英文逐字，≤100 词/段）：
  > Among representations in the labeling of a food which render such food misbranded is a false or misleading representation with respect to another food or a drug, device, or cosmetic.
  > The labeling of a food which contains two or more ingredients may be misleading by reason (among other reasons) of the designation of such food in such labeling by a name which includes or suggests the name of one or more but not all such ingredients, even though the names of all such ingredients are stated elsewhere in the labeling.
  （§101.18(a)/(b), pdf-page 219）
- 后果（答错会导致什么）：把审核范围缩到瓶身标签，漏审随附单张、菜单、广告、品名本身，导致"配料表全对但整体印象误导"被漏判；这是 PCHF 用户最容易低估的 labeling 边界。
- 建议归属子卡：基础架构

---

### CAND-CE-19: 以为版面被装饰 / 非强制信息挤满也能取得「空间不足」豁免
- 错误说法（一句）：包装放不下就缩小强制信息或申请空间不足豁免，装饰性图案、外文、放大的营销语不算原因。
- 正确判定（3–6 句，写清依据与边界）：§101.15(b) 明写"因版面空间不足而取得的豁免……不适用"，若该不足由① 非强制的文字/声明/设计/图案占用、② 给其它信息超出 §403(f) 要求的显著性、③ 外文表述占用所致。§101.15(a) 也把"为非强制设计/vignette 让出空间导致强制信息不显著""字号过小、对比不足、被装饰遮挡或与其它图文拥挤"列为缺 prominence 的情形。位置、格式、显著性本身就是可开观察项的法定义务，不能靠堆装饰把强制信息挤小再主张豁免。
- 条款出处：〔§ 101.15(a)〕〔§ 101.15(b)〕〔§ 101.1〕 + pdf-page 210
- 原文引用（英文逐字，≤100 词/段）：
  > No exemption depending on insufficiency of label space, as prescribed in regulations promulgated under section 403 (e) or (i) of the act, shall apply if such insufficiency is caused by: (1) The use of label space for any word, statement, design, or device which is not required by or under authority of the act to appear on the label;
  > Insufficiency of label space (for the prominent placing of such word, statement, or information) resulting from the use of label space for any word, statement, design, or device which is not required by or under authority of the act to appear on the label;
  > Smallness or style of type in which such word, statement, or information appears, insufficient background contrast, obscuring designs or vignettes, or crowding with other written, printed, or graphic matter.
  （§101.15(b)/(a)(4)/(a)(6), pdf-page 210）
- 后果（答错会导致什么）：显著性/位置类观察项被误判为可用豁免抵销，标签审核放过本可开单的硬缺陷；PDP 面积公式（§101.1 圆柱 40%）与信息面板方位也会被一并误读为排版偏好。
- 建议归属子卡：基础架构

---

### CAND-CE-20: 以为果汁贴了警示或写「100% natural」就等于合规百分比声明
- 错误说法（一句）：含果汁饮料只要贴了 §101.17(g) 警示、或写"100% natural / 100% pure"，就算交代了果汁含量。
- 正确判定（3–6 句，写清依据与边界）：§101.30 对果汁百分比声明另设独立义务，与 §101.17(g) 的病原警示是两条不相替代的标签义务（见 BOOK_OVERVIEW 接口清单 juice-haccp CAP-26 行）。§101.30(l) 明写：须标百分比果汁声明且实际不足 100% 果汁的饮料，不得在 label 或 labeling 上再标任何描述果汁含量的其它百分比声明（如 "100 percent natural" "100 percent pure"），但可标与果汁含量无关的百分比（如"提供 100% 维生素 C RDA"）。§101.30(k) 还规定经重大改性、原果汁已不可辨认或营养剖面低于正常范围的果汁，不得计入总百分比。警示解决的是病原风险，百分比声明解决的是含量真实性，二者不得互借。
- 条款出处：〔§ 101.30(l)〕〔§ 101.30(k)〕〔§ 101.17(g)(2)〕；并列既有包〔§ 120.24〕（仅条款号） + pdf-page 228 / 214
- 原文引用（英文逐字，≤100 词/段）：
  > A beverage required to bear a percentage juice declaration on its label, that contains less than 100 percent juice, shall not bear any other percentage declaration that describes the juice content of the beverage in its label or in its labeling (e.g., “100 percent natural” or “100 percent pure”).
  > If the product is a beverage that contains a juice whose color, taste, or other organoleptic properties have been modified to the extent that the original juice is no longer recognizable at the time processing is complete, or if its nutrient profile has been diminished to a level below the normal nutrient range for the juice, then that juice to which such a major modification has been made shall not be included in the total percentage juice declaration.
  （§101.30(l)/(k), pdf-page 228）
- 后果（答错会导致什么）：把"警示 / 营销百分比"当"合规果汁百分比声明"，漏做 §101.30 计算与声明；同时印证"每层标签义务各有豁免口、豁免对象互不通用"这一豁免体系总原则。
- 建议归属子卡：特定品类与警示

---

## 附：覆盖条款与归属分布（供阶段 2 B 段取用）

- 覆盖条款号：§101.1、§101.9(a)(b)(j)(k)、§101.12(a)(b)、§101.13(b)(h)(i)(q)、§101.14(a)(c)(d)(e)、§101.15(a)(b)、§101.17(g)(h)、§101.18(a)(b)、§101.30(k)(l)、§101.60(b)(e)、§101.62(b)、§101.70、§101.71、§101.91(a)(b)(c)(d)、§101.100(a)(d)(e)、§101.108(b)(c)(d)。
- 并列既有包条款号（仅写号、未引该包文字）：〔§ 117.5〕〔§ 117.135(c)(2)〕〔§ 120.24〕；法条钩子 FD&C Act §402（adulteration）/ §403（misbranding）/ §201(n)（labeling 定义，转引未收）。
- 五张子卡归属分布：基础架构 2（CE-18/19）、营养标签与份量 2（CE-08/09）、声称闸门 6（CE-04/07/11/12/15/16）、特定品类与警示 3（CE-05/17/20）、豁免与效力层 7（CE-01/02/03/06/10/13/14），合计 20 条。
- 引用核验：以上全部 `>` 段落均逐字取自 `source-cfr-part101-2026.md`（硬换行归一化为空格）；未引 §101.12 Table 1/2 数值与 Appendix B/C/D 图形版式；未引任何既有技能包内的英文条文。
