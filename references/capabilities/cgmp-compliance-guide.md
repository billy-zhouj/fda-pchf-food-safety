# cGMP 合规分诊与内审索引（cgmp-compliance-guide）

*来源分层：本卡同时取用四类权威，引用前先分层。① **21 CFR Part 117 法规正文**（2015 最终规则，具法律约束力）标注〔§ 117.xxx〕；② **FDA《Small Entity Compliance Guide》**（2016-10，Guidance for Industry，非约束性白话版规则说明）标注「SECG 章号」；③ **FDA PCHF 行业指南**（滚动草案，建议层）标注「PCHF 指南 Ch/小节号」；④ **L.mono 专项指南**（2017-01 Draft – Not for Implementation，建议层）标注「L.mono 指南章号」；⑤ **FDA《Food Defect Levels Handbook》**（执法裁量参考，非法规非 guidance）标注「Handbook 章名 + 产品名」，其法定义务锚点是〔§ 117.110〕。五类不可混引；缺陷阈值与放行的完整判定见 CAP-15 `defect-action-levels`。v4.7 起十二类、**v4.15 起全包统一「二十八类不可混引」（v4.10 时为十五类，v4.8 时为十三类）**——法规正文层新增 **21 CFR Part 113〔§ 113.xxx〕与 Part 114〔§ 114.xxx〕** 两套（第十一、第十二来源，见 CAP-20 `lacf-statutory-requirements`），自此〔§ 117.xxx〕只能理解为「判定 **Part 117 义务**的唯一基准」；本卡之外另有 CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / 过敏原 Ed.5，检查视角分别见 CAP-16 / CAP-17 / CAP-18 / CAP-19。（**v4.8 起第十四类来源为 CP 7303.878 FSVP 检查程序**，见 CAP-21 `fsvp-inspection-program`。）*

*本卡的定位：把「cGMP 合规有没有指南」从一个找文件的问题，变成一个**效力分层 + 主体分流 + 逐条取证**的判定问题。它给的是判定路径与条款级索引，不是一份可以直接签发的内审结论。*

## R — 原文

**① 效力声明——SECG 自己写在首页的那段话（SECG I. Introduction）**，这是整张卡的地基：

> "This guidance represents the Food and Drug Administration’s (FDA or Agency) current thinking on this topic. It does not establish any rights for any person and does not bind FDA or the public. You can use an alternative approach if it satisfies the requirements of the applicable statutes and regulations."
> —— SECG I. Introduction

> "The rule is binding and has the full force and effect of law. FDA’s guidance documents, including this guidance, do not establish legally enforceable responsibilities. Instead, guidances describe our current thinking on a topic and should be viewed only as recommendation, unless specific regulatory or statutory requirements are cited. The use of the word should in FDA guidances means that something is suggested or recommended, but not required."
> —— SECG I. Introduction

> "On September 17, 2015, FDA published the final rule Current Good Manufacturing Practice, Hazard Analysis, and Risk-Based Preventive Controls for Human Food (PCHF rule) (80 FR 55907). This final rule became effective on November 16, 2015."
> —— SECG I. Introduction

> "3. Covered facilities must meet updated Current Good Manufacturing Practice (CGMP) requirements (21 CFR, Part 117, subpart B)."
> —— SECG I. Introduction, Key Requirements

**② 法规侧的判据定义**——cGMP 通篇用 `adequate` / `as necessary` / `suitable` / `appropriate` 而不给数字，这个词的法定含义在定义条款里：

> "*Adequate* means that which is needed to accomplish the intended purpose in keeping with good public health practice."
> —— 〔§ 117.3〕

> "The criteria and definitions in this part apply in determining whether a food is: (1) Adulterated within the meaning of: (i) Section 402(a)(3) of the Federal Food, Drug, and Cosmetic Act in that the food has been manufactured under such conditions that it is unfit for food; or (ii) Section 402(a)(4) ... under insanitary conditions whereby it may have become contaminated with filth ..."（节选，省略号处为原文连续片段的省略）
> —— 〔§ 117.1(a)(1)〕

**③ SECG 第 XIII 章的形态**——它把 Subpart B 逐条改写成白话清单，八个小节标题就是条款号，这是「cGMP 条款—指南—检查要点」三列索引的直接依据：

SECG XIII 章标题及 A–H 小节标题清单如下（**并列摘录，非连续引文**；小节标题即条款号，这是三列索引的直接依据）：

- 章标题：`XIII. UPDATED AND CLARIFIED CURRENT GOOD MANUFACTURING PRACTICE (CGMP)`
- `A. Personnel (21 CFR 117.10)` · `B. Plant and Grounds (21 CFR 117.20)` · `C. Sanitary Operations (21 CFR 117.35)` · `D. Sanitary Facilities and Controls (21 CFR 117.37)`
- `E. Equipment and Utensils (21 CFR 117.40)` · `F. Processes and Controls (21 CFR 117.80)` · `G. Warehousing and Distribution (21 CFR 117.93)` · `H. Defect Action Levels (21 CFR 117.110)`
- —— SECG XIII 章

> "The management of the establishment must take reasonable measures and precautions to ensure:"
> —— SECG XIII.A（人员）

> "Food-contact surfaces used for manufacturing/processing, packing, or holding low-moisture food must be in a clean, dry, sanitary condition before use."
> —— SECG XIII.C

> "Instruments and controls used for measuring, regulating, or recording temperatures, pH, acidity, water activity, or other conditions that control or prevent the growth of undesirable microorganisms in food must be accurate and precise and adequately maintained, and adequate in number for their designated uses."
> —— SECG XIII.E

**④ SECG 三处实质简化的法规对照**——SECG 是白话版，凡它把「唯一路径」写成「多个选项」的地方，必须回法规正文取原口径。三处对照如下（左为 SECG 措辞，右为法规原口径）：

*简化 1：供应商验证活动被列成「四选一」。* SECG IX.A 把 `onsite audits` / `sampling and testing` / `review of the supplier's relevant food safety records` / `other appropriate supplier verification activities` 并列为可选项，读起来像自由选择。法规另设强制升级：

> "(b)(1) Except as provided by paragraph (b)(2) of this section, when a hazard in a raw material or other ingredient will be controlled by the supplier and is one for which there is a reasonable probability that exposure to the hazard will result in serious adverse health consequences or death to humans: (i) The appropriate supplier verification activity is an onsite audit of the supplier; and (ii) The audit must be conducted before using the raw material or other ingredient from the supplier and at least annually thereafter."
> —— 〔§ 117.430(b)(1)〕

> "(2) The requirements of paragraph (b)(1) of this section do not apply if there is a written determination that other verification activities and/or less frequent onsite auditing of the supplier provide adequate assurance that the hazards are controlled."
> —— 〔§ 117.430(b)(2)〕

*简化 2：qualified facility 状态变更通知只写了「由是变非」一个方向。* SECG XI.D 只写 `When the status of a facility changes from "qualified facility" to "not a qualified facility"`。但首次申报义务本身包含第三个触发点——由「非」变「是」：

> "(i) Submitted to FDA initially: ... (C) By July 31 of the applicable calendar year, when the status of a facility changes from "not a qualified facility" to "qualified facility" based on the annual determination required by paragraph (c)(1) of this section."
> —— 〔§ 117.201(c)(2)(i)(C)〕（本地来源文件中该处引号在 PDF 导入后表现为连写单引号，此处按原意以直双引号转录；措辞与数值未改动）

*简化 3：撤销豁免的程序讲到 15 日答复即止。* SECG XI.E 停在 15 个日历日的书面答复窗口，读起来像程序终点。法规另有批准层级、令件内容、以及一整套上诉与听证程序（§§ 117.254、117.257、117.260、117.264、117.267、117.270、117.277）：

> "(a) An FDA Division Director in whose division the qualified facility is located (or, in the case of a foreign facility, the Director of the Office of Compliance in the Center for Food Safety and Applied Nutrition), or an FDA official senior to either such Director, must approve an order to withdraw the exemption before the order is issued."
> —— 〔§ 117.254(a)〕

**⑤ 掺混稀释禁令**——规则里少见的一条「结果无罪也照样违法」：

> "(b) The mixing of a food containing defects at levels that render that food adulterated with another lot of food is not permitted and renders the final food adulterated, regardless of the defect level of the final food."
> —— 〔§ 117.110(b)〕；SECG XIII.H 用白话复述了同一条，并指向 *Defect Levels Handbook*

**⑥ 记录口径的两条「不必」**——Subpart F 里最常被误读为「要为 PCHF 另建一套记录」的两处：

> "(a) Existing records (e.g., records that are kept to comply with other Federal, State, or local regulations, or for any other reason) do not need to be duplicated if they contain all of the required information and satisfy the requirements of this subpart. Existing records may be supplemented as necessary to include all of the required information and satisfy the requirements of this subpart."
> —— 〔§ 117.330(a)〕；既有记录**不必复制**，缺什么补什么

> "(b) The requirements of § 117.310 apply only to the written food safety plan."
> —— 〔§ 117.301(b)〕

> "(c) The requirements of § 117.305(b), (d), (e), and (f) do not apply to the records required by § 117.201."
> —— 〔§ 117.301(c)〕；qualified facility 的 modified requirements 记录不受「实际值/同步记录/详细程度/签署与批号」四项约束

**中文大意**：判定 cGMP 合规的基准是法规，不是指南。SECG 的价值是「把法规讲清楚」，它自己反复声明不创设义务、允许替代方案；而法规的 `adequate` 是一个**结果义务**——「足以按良好公共卫生实践达成预期目的」，解释权不在企业手里。做不到时，食品依 FD&C Act § 402(a)(3)/(a)(4) 被认定为 adulterated，而不是仅仅「扣个分」。

## I — 自述

这一卡处理的是**效力分层与合规取证的元问题**，与「某条 cGMP 具体怎么做」分属两层。七条结构化判定：

1. **四层效力栈，一层都不能跳**。① 21 CFR Part 117 法规正文（最终规则，must，判定 **Part 117 义务**的唯一判定基准；Part 113/114 的法定要求另见 CAP-20）→ ② SECG（2016-10，面向境内境外食品设施的白话版规则说明，represent current thinking，不创设义务）→ ③ 专项行业指南（PCHF 指南、L.mono 指南均为 Draft，一律建议层）→ ④ 执法口径文件（CPG、Compliance Programs、Import Alerts，是 FDA 检查员的作业指令，不是企业义务清单）。用户说「找一份 cGMP 合规指南」时，真正想要的多半是第 ② 层；但合规结论必须能回指法规正文。**栈外另有一类并列参考**：《Food Defect Levels Handbook》是 FDA 汇编的 defect action levels 一览与术语表，§ 117.3 定义用的是 `may regard ... adulterated`，属执法裁量参考；〔§ 117.110(b)〕明文指向它取「可能使食品掺假的行动水平实例」。不要把它塞进效力栈排序，也不要把它的数值写成法定义务（见 CAP-15）。
2. **`current` 是持续义务，不是版本号**。cGMP = Current Good Manufacturing Practice。法规不给参数的数字，只给 `adequate`（〔§ 117.3〕定义如上）。「法规没写数值」从来不是免责理由——它意味着你必须跟上当前行业公认、技术上可行的做法，检查员看的是**现场状态与运行结果**，不是你有没有一份漂亮的书面程序。
3. **SECG 的两项真实用途，一项不该指望的用途，以及一个计数陷阱**。用途一：把 Subpart B 按工厂语言重排（XIII.A–H 共**八个**小节），便于逐条建 GAP；用途二：用加粗标记凸显 2015 现代化新增/强化的措辞，最典型是 `protect against allergen cross-contact and against contamination` 在人员、厂房、清洁、工艺、仓储各节反复出现——2015 年前这只是执法立场，现在是明文义务。不该指望的用途：**它不是逐条内审清单**，不含检查员的观察要点、抽样逻辑与判定阈值，也不替代 CPG / Compliance Programs 的检查视角。**计数陷阱**：Subpart B 是**九条**（§§ 117.10、.20、.35、.37、.40、.80、.93、.95、.110），但 SECG XIII 章只覆盖**八条**——第九条 § 117.95（人类食品副产物转动物饲料）被排到了 XIV 章。说「XIII 章九条」是错的，说「Subpart B 九条」才对。
4. **cGMP 与 PCHF 是分层，不是并列**。判据一句话：**不看具体产品就能判不合格的是 cGMP；必须先问「这个产品有什么危害」才能判的是 PCHF**。豁免通常切的是上层（Subparts C/G），不是底层（Subpart B）；qualified facility〔§ 117.5(a)〕、仅存放未暴露包装食品〔§ 117.7〕、海产品/果汁 HACCP、LACF、膳食补充剂等主体仍受 Subpart B 约束，qualified facility 另须履行〔§ 117.201〕的 modified requirements 替代义务。**但「豁免不切底层」有例外，且是唯一的例外**：〔§ 117.5(k)(1)〕明定 subpart B 也不适用于 ① farms（§ 1.227 定义）② 不受注册要求的渔船 ③ **仅从事一种或多种初级农产品存放和/或运输的场所** ④ 属于 farm 定义的 farm mixed-type 设施活动 ⑤ **仅从事坚果去壳、脱壳、干燥、包装和/或存放（不做烘烤等进一步加工）的场所**。〔117.5(k)(2)〕另设回拉条款：farm 或 farm mixed-type 设施若干燥/脱水属于 covered produce 的初级农产品以形成 distinct commodity，则 subpart B 适用于该干燥品的包装、打包与存放。**判「CGMP 到底适不适用」时须先过 § 117.5(k)**，这一步 SECG 只在 Table 4 脚注 2 用一行字带过，极易漏。交汇处在卫生控制：〔§ 117.135(c)(3)〕允许把针对具体危害的卫生控制升格为 preventive control，一旦升格就要补齐监控、纠正措施、验证、记录全套管理组件〔§ 117.140〕，举证责任与成本完全不同。
5. **记录负担是错配的**。Subpart B 本身要求很轻（主要是培训记录〔§ 117.9(a)〕，且受 Subpart F 记录规则约束），重记录义务在 FSP 那一侧。「cGMP 没要求写」不等于不用留痕，「FSP 记录齐全」也不能抵现场卫生失守。
6. **效力错位在读指南时必须逐句处理**。L.mono 指南 III 章自己说明：因部分主体只受 Subpart B 约束而免于 PCHF，整份指南写成 recommendations；但受 PCHF 约束的主体，即使指南用 *recommend*，〔§ 117.160(a)〕的 must 照样必须遵守。SECG 的效力声明更进一步：它明确允许满足法规要求的**替代方案**（alternative approach）。所以「这句话我能不能不做」必须先问主体身份，再问背后有没有法条。
7. **三处高频事实错误，本卡统一口径**。① **SECG 是 2016 年 10 月**（October 2016，Docket FDA-2011-N-0920，依 SBREFA § 212 编制），不是 2016 年 11 月；2018-05 那份同名近似 SECG（Docket FDA-2018-D-1378）只讲合规日期延长与澄清，不是操作手册。② **80 FR 55907 与 80 FR 56145 是同一份 2015-09-17 最终规则的两个页码**：55907 是 Federal Register 规则发布通知的起始页（SECG I 章引用它），56145 是同一通知中 **Part 117 法规条文部分**的起始页（CFR 各条末尾的 source note 引用它）。见到两个数字不要判成两份规则，也不要互相「纠错」。③ SECG 不是认证、不是 ISO 标准、不发证；GFSI 认可的 BRCGS / FSSC 22000 / SQF 是私人标准，其 PRP 大致对应 cGMP 但不能替代法定义务。

## A1 — 书中案例

**案例 1：一份指南把自己写成了「不算数」（SECG I. Introduction）**
FDA 在小企业合规指南首页同时写了两句看似矛盾的话：`The rule is binding and has the full force and effect of law.` 与 `FDA’s guidance documents, including this guidance, do not establish legally enforceable responsibilities.` 这不矛盾——前句说的是被解释的对象（Part 117 最终规则），后句说的是解释者（本指南）。实务推论：拿 SECG 做内审 GAP 时，每一行的结论都必须能回指一条〔§ 117.xxx〕；只在 SECG 里出现、法规里无对应义务的措辞，不得写成「不符合项」。

**案例 2：低水分食品 FCS 的湿洗后果（SECG XIII.C / 〔§ 117.35〕）**
SECG 把法规拆成两句可执行判据：`Food-contact surfaces used for manufacturing/processing, packing, or holding low-moisture food must be in a clean, dry, sanitary condition before use.`，湿洗后 `they must, when necessary, be sanitized and thoroughly dried before subsequent use.` 这正是「adequate 是结果义务」的具体形态：法规没规定干燥到多少 a_w、干燥多久，但湿洗后未彻底干燥就投料，在沙门氏菌/低水分食品语境下直接构成失守。本包 `environmental-pathogen-sanitation` 卡给出的「湿/干环境二分法」（湿区防李斯特菌靠保持干燥，干区防沙门氏菌靠严格控水）是它的执行层展开。

**案例 3：法规给手段清单，不给唯一答案（〔§ 117.20(b)(2)〕 / SECG XIII.B）**
对易发生过敏原交叉接触或污染的工序，法规允许用 `location, time, partition, air flow systems, dust control systems, enclosed systems, or other effective means` 中的**一种或多种**分隔。检查时不能问「你有没有上隔墙」，只能问「你选的手段在这个产品/布局下是否足以防止交叉接触」。这也是 SECG 把整段加粗的原因——2015 现代化把「防过敏原交叉接触」写进了每一条相关 cGMP。本包 `environmental-engineering-controls` 卡负责工程手段的选型与验证。

**案例 4：终检合格也救不了的批次（〔§ 117.110(b)〕 / SECG XIII.H）**
把缺陷超标的批次掺进合格批次，即使终产品检测值落在行动水平以内，法规仍认定终产品 adulterated——原文 `regardless of the defect level of the final food`。SECG 在同一段指向 *Defect Levels Handbook* 作为行动水平实例来源（该手册正文已收为第六来源，见 CAP-15 `defect-action-levels`：111 个产品 / 173 条行动水平）。⚠ 网页引言的 `21 CFR 110.110` **不是过时引用**：Part 110 至今有效（FDA 2018-09-12 撤回了删除指令），只是**正文本包未收**；Part 117 侧对应条款是〔§ 117.110〕。详见 CAP-20 B2 的 v4.7 纠错。本包 `chemical-hazard-controls` 卡把这条归入「不得用掺混稀释处理超标批次」纪律，不得与「返工 reconditioning 经证明有效后可再用」混为一谈（后者见〔§ 117.80(c)(9)〕与 SECG XIII.F Manufacturing Operations (9)）。

**案例 5：合规日期表的时效性（SECG VI. / Table 4）**
SECG Table 4 列出分档合规日期（qualified facilities 2018-09-17、small businesses 2017-09-18、记录义务 2016-01-01 等），是 2016 年编制时的过渡安排。**这些日期到今天已全部生效**，不得再当作「我现在还没到合规期限」的依据；当前时限类问题一律回法规正文与最新 eCFR 文本，不用 SECG 的日历。这类「文件本身正确、但时点已过期」的情形，是本卡 B 段单列一条边界的原因。

**案例 6：四类验证活动被读成「随便挑一个」（SECG IX.A / 〔§ 117.430〕）**
一家厂从供应商处采购即食原料，该原料的致病菌危害由供应商控制。厂方的验证方案是「每批取 COA + 每年看一次供应商记录」，理由是 SECG IX.A 把四类活动并列写成可选项。若该危害属于「暴露后有可能导致严重健康后果或死亡」那一档，这个方案不成立：〔§ 117.430(b)(1)〕规定此时 `The appropriate supplier verification activity is an onsite audit of the supplier`，且须在首次使用前做、之后至少每年一次。要走别的路，唯一合法出口是〔§ 117.430(b)(2)〕的 **written determination**——书面判定「其他活动或更低频的现场审核能提供足够保证」。**门槛不在「做没做验证」，而在「这个危害的严重性档位」+「有没有那份书面判定」。** 例外还有三类（qualified facility 供应商、不受 part 112 约束的农场、少于 3000 只蛋鸡的带壳蛋生产商），SECG 完全未写，见〔§ 117.430(c)(d)(e)〕。

**案例 7：SECG 讲到一半就停的程序（SECG XI.E / §§ 117.251–117.277）**
厂方收到 FDA 的撤销豁免意向通知，法务按 SECG XI.E 的理解准备「15 日内书面答复，之后等结果」。这条路径漏掉后半个程序：撤销令须经 FDA 分区主任（境外设施为 CFSAN 合规办公室主任）或其上级**批准**才能发出〔§ 117.254(a)〕；令件须载明法定内容〔§ 117.257〕；收到令后还可依〔§ 117.260〕选择**遵守或上诉**，上诉程序见〔§ 117.264〕，可申请**非正式听证**〔§ 117.267、§ 117.270〕，决定时限见〔§ 117.277〕。15 日答复只是撤销**之前**的陈述机会，不是全部救济手段。凡涉及行政时限与救济的问题，一律以法规条款为准，不以 SECG 的叙述长度为准。

## A2 — 未来触发

**用户情境**：
1. 问「cGMP 合规有没有指南 / 该看哪份文件 / 有没有官方中文材料」。
2. 要做 cGMP 内审、建 GAP 清单、迎检准备，问九条逐条看什么、证据怎么留。
3. 拿到一份 FDA 指南，问「这条算不算必须做」「我厂在不在适用范围内」「能不能用替代做法」。
4. 问 cGMP 与 HACCP / FSP / PCHF 的关系、有 FSP 是否还要管现场卫生。
5. 问「我们是 qualified facility / 只做仓储 / 有 HACCP，cGMP 是不是免了」。
6. 问 cGMP 失守的法律后果、检查员会怎么看、警告信/进口扣留的依据。
7. 问某个数值（pH 4.6、a_w、冷藏温度）到底是法规要求还是指南建议。
8. 拿 SECG 里的合规日期或页码（80 FR 55907 / 56145）来核对事实。
9. 问「供应商验证能不能只靠 COA、能不能不现场审核、审核频次能不能降」——须转 § 117.430 判定严重性档位，不能按 SECG IX.A 的四选项直接答。
10. 问「qualified facility 状态变了要不要通知 FDA、怎么通知、什么时候」——两个方向（是→非、非→是）与三个时限都在 § 117.201(c)，SECG 只写了其中一个方向。
11. 问「豁免被撤销了还能不能申辩、听证、上诉」——须查 §§ 117.251–117.277，SECG XI.E 只到 15 日答复。
12. 问「我们只做仓储 / 只做坚果去壳 / 是农场，CGMP 是不是完全不适用」——须先过〔§ 117.5(k)(1)〕五类情形，这是唯一能连 subpart B 一起免掉的条款。

**语言信号**："cGMP / CGMP / 现行良好生产规范"、"Subpart B"、"合规指南 / Small Entity Compliance Guide / SECG"、"内审 / GAP / 迎检 / 检查要点"、"adequate / as necessary"、"alternative approach"、"qualified facility 豁免"、"80 FR"、"cross-contact vs cross-contamination"；英文：cGMP compliance guide, subpart B, gap assessment, inspection readiness, current thinking, notice of availability。

**与相邻卡的区分**：
- `regulatory-boundaries` 管的是**整套法规的适用性矩阵**（豁免、双法规并集、执法钩子、指南效力错位的元规则）；本卡只管**cGMP 这一层的合规取证与资料分层**，并在需要判豁免时把读者送回该卡。
- `environmental-engineering-controls` / `personnel-hygiene-controls` / `environmental-pathogen-sanitation` 是**执行层**，讲 § 117.20/37/40、§ 117.10、§ 117.35 具体怎么做；本卡只给条款索引与「该翻哪张卡」的指针，不重复工程参数或采样方案。
- `reference-tools-discipline` 管**数据与方法合格性判据**；本卡管**文件效力层级**。两者都会说「先分层再引用」，但分的是不同的层。
- `process-control-validation` 管 § 117.80(c)(14)(15) 的屏障持续义务与工艺验证；本卡只把这两款登记进索引表并标注两套 pH/aw 基准不得互替。

## E — 执行要点

**Step 1 — 先分流主体，再分流文件。** 顺序不可颠倒：① 该设施是否须按 FD&C Act § 415 注册（境内境外一致，制造/加工/包装/存放都算，**无规模豁免**）→ ② 是否落入〔§ 117.5(k)(1)〕那五类**连 subpart B 都不适用**的情形（farm、不受注册要求的渔船、仅存放/运输初级农产品的场所、farm mixed-type 设施中属 farm 定义的活动、仅做坚果去壳干燥包装存放而不烘烤的场所）→ ③ 是否属于豁免 Subparts C/G 的主体（判定细则见 `regulatory-boundaries` 卡）→ ④ 无论③结论如何，Subpart B 是否适用（除②所列情形外，答案通常适用）。第②步是全流程唯一能把 CGMP 也免掉的关口，SECG 只在 Table 4 脚注 2 用一行字带过，不可跳过。主体身份同时决定同一句 `we recommend` / `should` 对它是不是 just a recommendation。SECG II 章原文：「The requirements of this rule apply to businesses – either in the U.S. or any other country – that are required to register with FDA as food facilities because they manufacture/process, pack, or hold food for consumption in the U.S.」

**Step 2 — 给每条结论打效力标签。** 输出时用四选一：`〔§ 117.xxx〕法定义务` / `SECG 章号，白话转述（不创设义务）` / `PCHF 或 L.mono 指南章号，建议层` / `CPG 或 Compliance Program，检查视角（非企业义务）`。**禁止**把指南的 should 改写成 must，也禁止用 SECG 的措辞替代法规原文作判定依据。SECG 自己给出例外通道：`You can use an alternative approach if it satisfies the requirements of the applicable statutes and regulations.` —— 替代方案合法，但举证责任在企业，须证明同样满足法规的结果义务。

**Step 3 — 三列索引：条款 / 法规结果义务 / 现场观察点（含 SECG 强调）。** 下表是本卡主体，第四列仅为路由指针。观察点列是「检查员看什么」的归纳，**不是法规新增义务**，措辞上不得写成 must。

| 条款 | 法规结果义务（要点） | 现场观察点 + SECG XIII/XIV 的强调 | 本包对应卡 |
|---|---|---|---|
| 〔§ 117.10〕人员 | 有传染病/开放性病灶且可能污染者须调离（除非妥善覆盖）；员工主动上报；上岗前、离岗后、手脏时彻底洗手；去不牢靠首饰；手套完好清洁；发网；私人物品与饮食吸烟不得进入暴露区 | 看交接班洗手实际执行、手套更换触发、工服色码与动线；SECG XIII.A 把 `Disease control` / `Cleanliness` 拆成 9 项，并把 `protect against allergen cross-contact` 写进每一项 | `personnel-hygiene-controls` |
| 〔§ 117.20〕厂房与场地 | 场地排水除草、废弃物不成虫害源；墙地顶可清洁；**管道与风管的 drip or condensate 不得污染食品**；暴露食品上方灯具须防碎；允许用 location / time / partition / air flow / dust control / enclosed systems 分隔 | 看冷凝水实际落点、灯具是否为 shatter-resistant、分区是否靠物理+时序+气流共同成立；SECG XIII.B 逐项列出 7 类构造要求 | `environmental-engineering-controls` |
| 〔§ 117.35〕卫生操作 | 清洁剂/消毒剂安全适用；有毒物料限用并隔离存放；**低水分食品 FCS 用前须 clean, dry, sanitary，湿洗后必要时消毒并彻底干燥**；湿加工中断后 FCS 可能受污染须重新清洁消毒；一次性用品与洁净器具存放 | 看湿洗后的干燥证据、消毒剂浓度记录、洁净器具离地存放；SECG XIII.C 另列虫害控制与 non-FCS 清洁频次 | `environmental-pathogen-sanitation` |
| 〔§ 117.37〕卫生设施 | 供水安全足量；**禁止污水管与食品用水管之间 backflow 或 cross-connection**；地面排水、洗手、厕所、垃圾处置 | 看交叉连接实物、地漏回水、洗手设施可得性与水温；SECG XIII.D 把 plumbing 的 5 项要求逐条列出 | `environmental-engineering-controls` |
| 〔§ 117.40〕设备与用具 | 可清洁设计、耐腐蚀无毒材质、焊缝平滑 bonded；冷藏室须装温度指示装置；**控制温度/pH/酸度/aw 的仪表须 accurate and precise 且数量充足**；压缩空气不得带入非法间接食品添加剂 | 看仪表校准记录与布点数量、焊缝积料、CIP 覆盖死角；SECG XIII.E 明确 `accurate and precise and adequately maintained, and adequate in number` | `environmental-engineering-controls` + `process-control-validation` |
| 〔§ 117.80〕工艺与控制 | 全厂卫生须有专人负责；原料验收/隔离/复用水；热烫后须速冷或立即转序；返工品标识；金属异物防护；**两条硬数值：靠 aw 控菌者须加工并维持 safe moisture level〔(c)(14)〕，靠 pH 控菌者须监控并维持 pH 4.6 或以下〔(c)(15)〕** | 看卫生责任人是否实到岗、复用水水质判定、返工标识、金检；SECG XIII.F 把原料 8 项 + 制造作业 16 项拆开，过敏原识别与隔离单列 | `process-control-validation` + `chemical-hazard-controls` + `allergen-program` |
| 〔§ 117.93〕仓储与配送 | 一句话条款：防过敏原交叉接触、防生物/化学（含放射性）/物理污染、防变质与容器破损 | 看混放、托盘破损、温湿度记录、退货与待判品隔离；SECG XIII.G 为整句转述，无附加数值 | `supply-chain-verification` + `recall-plan` |
| 〔§ 117.95〕副产物转动物饲料 | 标签注明通用名称；容器、桶、散装车辆使用前须检查 | 看标识与容器检查记录；**SECG 把这部分放在 XIV 章，不在 XIII 章**——做索引时别漏条 | `supply-chain-verification` |
| 〔§ 117.110〕缺陷行动水平 | 天然不可避免缺陷须降到**当前可行的最低水平**；**掺混稀释禁令**（终产品检测值不影响掺假认定） | 看不合格批处置单、有无「掺一批稀释」的做法；配套实例来源为 *Food Defect Levels Handbook*（正文已收，见 CAP-15 `defect-action-levels`；阈值是 FDA 执法裁量线而非合规上限） | `chemical-hazard-controls`, `defect-action-levels` |

**Step 4 — 取证按观察型义务组织，不按文件型义务组织。** cGMP 检查看三样：现场状态（发霉天花板、冷凝水、地漏、虫害）、实际运行（洗手、换手套、分区动线、湿洗后干燥）、必要记录（培训〔§ 117.9(a)〕、仪表校准、清洁消毒、虫害、不合格批处置）。一份完美的 FSP 配一个失守的现场，仍然不合规；反之，也不能因为「cGMP 没写要留这个记录」就不留客观证据。每一条不符合项要能落到具体条款 + 具体观察事实，而不是「程序文件不够完善」。

**Step 5 — Gap 闭环与两层执法钩子分开写。** 整改按「条款 → 观察事实 → 纠正动作 → 有效性证据 → 复核时点」五要素建表。后果侧不要混：cGMP 失守对应 FD&C Act § 402(a)(3)/(a)(4) 的 **adulterated** 认定〔§ 117.1(a)(1)〕；不遵守 Subparts C–G 则设施运营本身构成 **prohibited act**（FD&C Act § 301(uu)，〔§ 117.1(b)〕）。两者后续都可接警告信、扣押、禁令、进口扣留，但法律定性不同。

**Step 6 — 升级判据：什么时候从 cGMP 升到 PCHF。** 若某卫生控制是针对具体危害、且需要「显著最小化或预防」该危害，〔§ 117.135(c)(3)〕允许把它作为 preventive control 管理；升格后须补齐监控、纠正措施、验证、记录〔§ 117.140〕全套，且验证受〔§ 117.160(a)〕约束。这一步决定成本与举证责任，必须在书面 FSP 里显式记录理由，不能靠口头惯例。反向也成立：不要把本属通用卫生底线的项目硬塞进 FSP，制造不必要的验证负担。

**Step 7 — 数值纪律（本卡与全包共用）。** 凡涉及 pH / a_w / 温度，先标明是哪一套基准：
- **pH 4.6 / a_w 0.85**：Part 117 酸化食品管辖边界与安全水分水平（法定/通用口径）；〔§ 117.80(c)(15)〕的 `pH of 4.6 or below` 是法定工艺维持义务。
- **pH ≤ 4.4 / a_w ≤ 0.92**：L.mono 指南抑制型（listeristatic）配方的**建议层**设计基准，与酸化法规管辖不是一回事。
- 同一个 `0.92` 在「抑制芽孢萌发」（肉毒视角）与「抑制李斯特菌营养细胞生长」（李斯特视角）下含义不同，不得互相替换。
- `4°C / 40°F` 是 L.mono 指南针对李斯特菌储存的**建议缺省值**；`41°F / 5°C` 是危险区下限与冷却终点（法规/Food Code 口径）。4°C 不是法定门槛。
- **抑制 ≠ 杀灭**：listeristatic 只承诺阻止生长（货架期重复生长研究增幅 <1 log），listericidal 才承诺破坏活菌并使成品达到 <0.04 CFU/g 的不可检出性（须绑定方法检出灵敏度）。两者都不能简化成「pH 低」或「有热处理」一句话。
- 所有数值须注明出处小节并提示「文献极端值，未必适用于具体产品」；**禁止凭记忆给数**。

**Step 8 — 资料清单与缺口（按四层栈点名）。**
- 已收（**本仓库**可逐字核对，v4.14 起该文件随仓库分发）：`books/_inbox/21-CFR-Part-117-2025.md`（Subparts A–G 全文）、`source-secg.md`（2016-10 SECG 全章，由资料库文档转换）、`source.md`（PCHF 指南，Introduction 的 Table 3–8 是 FDA 配套资源总目录）、`source-lmono.md`（L.mono 指南，II.A 的 Table 1 逐条列出它涉及的 7 条 CGMP 要求）。
- 已收（补）：`source-defect-levels-handbook.md`（Food Defect Levels Handbook 网页正文，第六来源，见 CAP-15）、`source-allergen-ed5.md`（过敏原 Q&A Ed.5 2025-01 修订终版，替代 2022 草案/终版）。注意 Handbook 给的是阈值出处，不是抽样与检验作业指导。
- 已收（补，第七来源）：`source-cpgm-7303-040-2025.md`（CPGM 7303.040 现行版 `2025-CPM-HFP-001`，签发 08/29/2025，50 页；见 CAP-16 `inspection-readiness`）与 `source-cpgm-7303-040-2020.md`（`2020-CPGM-CFSAN-003`，**已废止的历史对照**）。注意 CPGM 是 FDA 给检查员的内部作业指导，给的是检查类型、分级口径与记录举证路径，不是抽样与制样作业指导。
- 已收（检查视角）：CPGM 7303.040 现行版（CAP-16）、CP 7303.050 抽样 program（CAP-17）、IOM 2026 Chapter 5（CAP-18）。
- 未收：IOM 其余章节（尤其 Ch.3/4/6/7/8，Ch.4 含 702(b) 分割留样与制样）、RPM、FMD-86 / FMD-147、SOP-001052 / SOP-000529、CPG 全套（含 Sec. 130.100 / 527.300）、其他 Compliance Programs（7303.878 FSVP、7303.080 Produce Safety、7304.019 等）、Import Alerts / Import Bulletins 正文、AOAC Official Methods / eBAM / BAM / MPM 方法正文、21 CFR 2.10 / 133 / 1240.61 正文、Form FDA 483/484 数据库、21 CFR part 117 citations table、SOFO job aid、Human Food By-Products GFI #239 全文。**低酸/酸化体系**：CP 7303.070 已由 CAP-19 收入；其依据的 **21 CFR part 113 / 114 法规正文已由 CAP-20 收入**；**part 110（旧 CGMP，含 §110.110）正文仍未收**，一律标「转引未收」；**part 108（FCE/SID/Emergency Permit）自 v4.12 起已收**（见 CAP-25，按〔§ 108.xxx〕引用）；**part 123 自 v4.9 起已收**（见 CAP-22，按〔§ 123.xxx〕引用，与〔§ 117.5(b)〕的接口只给结论不展开）；21 CFR Part 120 与 21 CFR part 117〔§ 117.5(b)(c)〕的接口只给结论不展开。
- 实操顺序：法规 Subpart B 九条逐条建 GAP → 用 SECG 做白话核对 → 按产品风险挂专项指南（RTE 挂 L.mono、过敏原挂 Q&A、化学危害挂行动水平系列）→ 用 CPGM 7303.040（CAP-16 `inspection-readiness`）反查检查视角与记录举证要求 → 用 IOM Ch.5（CAP-18 `investigator-authority-procedure`）核对检查员权限与 483 措辞纪律、用 CP 7303.050（CAP-17 `inspection-sampling`）核对现场取样量与环境拭子 → 每条结论标注来源层级。PCHF 指南 Introduction 另提醒：这些资源的政策与建议会变，须定期复核其官网。

## B — 边界

**B1 — SECG 不是义务来源，也不是认证。** 它是依 SBREFA § 212 编制的 Guidance for Industry，代表 FDA current thinking，明确「不约束 FDA 或公众」「允许替代方案」。合规结论必须回指〔§ 117.xxx〕；把 SECG 的白话措辞写成「FDA 要求你必须……」是效力层的错误。它也不是证书、不是 ISO/GFSI 私人标准，不存在「通过 cGMP 认证」这回事。

**B2 — 2016 SECG 的合规日期表已全部过期。** Table 4 与 IX.B、X 章的日期是 2016 年编制时的过渡安排（2016-01-01 记录义务、2017-09-18 小企业、2018-09-17 qualified facility 等），到今天**全部已生效**。不得用它回答「我现在是否已达合规期限」；当前时限类问题一律回法规正文与最新 eCFR 文本。 ⚠ v4.23 另收 **CAP-36** 的 **2017-08 IA rule SECG**（Docket FDA-2013-N-1425，Table 3 三档日期 2019-07-26 / 2020-07-27 / 2021-07-26）——两份 SECG 分属 cGMP 与食品防护两个不同规则，**日期表不得互引**，页码基准也不同（本卡为 SECG 章号，CAP-36 为 0-based 提取件标记）。

**B3 — 本卡不是可直接签发的逐条内审清单。** 索引表的「现场观察点」列是归纳，不含检查员抽样逻辑、判定阈值与证据充分性标准。检查视角**已完整补入三张卡**：CPGM 7303.040 现行版（第七来源，CAP-16）给检查类型、取证深度、观察项分级与记录举证矩阵；CP 7303.050（第八来源，CAP-17）给样品量、环境拭子、WGS 与逐案执法阶梯；IOM 2026 Ch.5（第九来源，CAP-18）给权限、表单、483 措辞纪律与证据链；Handbook（第六来源，CAP-15）给缺陷行动水平阈值与 DEFECT SOURCE / SIGNIFICANCE。但四者都**不等于补上检验作业指导或企业内控标准**：IOM 其余章节（尤其 Ch.4）、RPM、FMD-86 / FMD-147、SOP-001052 / SOP-000529、CPG 全套、Import Alerts 正文、AOAC / eBAM / MPM 方法正文、21 CFR part 117 citations table 与 SOFO job aid 本包仍未收，制样与显微判读、方法检出限、702(b) 分割留样规则与警告信判定阈值须另行复核；action level 是 FDA 执法裁量线、不是放行标准；CP 7303.050 的 subs 数是 FDA 取证量、不是企业批放行标准。真要出内审报告，须由具备资质的 PCQI 或审核员结合现场复核，并回到法规正文〔§ 117.110(a)〕的 `lowest level currently feasible` 逐条确认。SECG XIII 章本身也只是法规的白话转述，不含观察要点。

**B4 — 草案不可当现行法定义务引用。** PCHF 行业指南为 Draft 且 Ch7/8/9/10/13/17 未发布；L.mono 指南为 2017-01 Draft – Not for Implementation，通篇 `we recommend`，正文出现 `must` 处均为其引述 Part 117 的法定义务。XIII.D.4 的频次数值、5+5 点位下限、Zone 划分均为**指南建议（should）**，〔§ 117.165〕只要求「足以判定有效性」（must）——不得把建议层数值升格为法定义务。本卡沿用全包的「should 与 must 分层阅读」原则。

**B5 — 两套基准不得互替，且不得用指南的「年度复审」覆盖法定记录保存期限。** pH 4.6 / a_w 0.85 与 pH ≤ 4.4 / a_w ≤ 0.92 用途不同（见 Step 7）；同一份 FSP 里须标明每个数字的用途。Part 117 Subpart F 的记录保存期限是法定义务，任何指南中的「至少每年复审更新一次」都是再加一层，不是替代。三条配套边界：

1. **不必为 PCHF 另建一套记录**。〔§ 117.330(a)〕明写既有记录只要**含全部所需信息且满足本子部分要求**就 `do not need to be duplicated`，缺的部分 `may be supplemented` 补进去即可；(b) 进一步规定信息**不必集中在同一套记录里**。企业为其他联邦/州/地方要求保存的记录可以复用——这是最常见的问法，也是被指南反复暗示「另建体系」造成的误解。
2. **但「不必复制」≠「可以不满足」**。复用是**格式与载体**的豁免，不是**内容**的豁免：所需信息一项都不能少，只是允许分散、允许补充。三条通用要求对全部记录仍然成立——原件/真实副本/电子记录〔§ 117.305(a)〕；准确、不可擦除、清晰〔§ 117.305(c)〕；电子记录若**仅为满足本部分**而建且符合 § 11.3(b)(6) 定义则**免于 part 11**，但**兼为其他法规要求**的记录**仍受 part 11 约束**〔§ 117.305(g)〕。
3. **qualified facility 的记录负担确实更轻，但轻在四款、不是全免**。〔§ 117.301(c)〕把 § 117.305 的 (b)(d)(e)(f) 从 § 117.201 要求的记录中排除——即不要求记**监控的实际值与观察**、不要求**与活动同步创建**、不要求**详细到能还原工作史**、不要求列**设施标识/日期/签署/批号**；但 (a)(c)(g) 仍在，所以「准确、清晰、不擦除」照样要求。另〔§ 117.301(b)〕把 § 117.310 的额外要求**限定在书面食品安全计划**上，不外溢到其他记录。

**B6 — 不做跨体系合规判定。** 药品 cGMP 是 21 CFR Parts 210/211；食品专项另有 Part 111（膳食补充剂）、106（婴儿配方）、113（LACF）、114（酸化食品）、129（瓶装水）、123（海产品）、120（果汁）；中国 GB 14881 功能上大致对应 Subpart B，但条款体系与法定口径不同。本卡只提供 FDA 口径，跨体系映射需人工判断。**低酸罐头 / 酸化食品与 Part 117 的具体管辖分流（〔§ 117.5(d)(1)(2)〕、〔§ 117.1(c)〕、Keep Refrigerated 路由、酸化食品不免 Subparts C/G）见 CAP-19 `lacf-inspection-program`**；注意〔§ 117.201〕是 qualified facility 的 modified requirements，不是 LACF 条款。GFSI/BRCGS/FSSC 22000/SQF 的 PRP 与 cGMP 有重叠，但属私人标准，不能替代法定义务。

**B7 — 来源文件的已知排版错位。** `source-secg.md` 由资料库在线文档转换而来，原 PDF 分页表格在导入时出现两处错位：XIII 章标题后紧接的若干项目符号实为 XII 章低风险活动清单的尾部；XIII.H「Defect Action Levels」的正文落在 XIV 章标题之后。引用时**以章节标题与条款号为准，不以邻接关系为准**。转换过程剥离了排版标记、合并了换行，正文措辞与数值未改动；个别 PDF 连字（如 `atone general physical location`）为导入残留，遇到可疑英文一律回法规正文核对。

**B8 — 引用标注规范（全包统一，v4.7）。** 法规用〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕（六套独立编号）；SECG 用章号（如 SECG XIII.C）；PCHF 指南用 Ch/小节号；L.mono 指南用其章节号；Ed.5 用问答编号；Handbook 用「Handbook 章名 + 产品名」；CPGM 7303.040 用「CPGM 7303.040 PART x」（附件须带 `ATTACHMENT A` 前缀）；CP 7303.050 用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」；IOM 用「IOM 5.x.x / IOM Exhibit 5-x」；CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」。**21 CFR part 108 / 110 / 120 等未收正文一律标「转引未收」（part 123 自 v4.9 起已收，见 CAP-22）；二十八类不可混引**，也不得把 SECG 的 80 FR 55907 与 CFR 条文 source note 的 80 FR 56145 判为两份不同规则——同一份 2015-09-17 最终规则，前者是发布通知首页，后者是条文部分首页。⚠ 特别注意〔§ 114.5〕现行原文并列 `parts 110 and 117`，**不得改写成只有 part 117 或判为笔误**。

**B9 — 覆盖范围边界。** 本卡与全包一样，主体是 PCHF 指南 + L.mono 专项指南的蒸馏，cGMP 条款在其中是法定义务锚点与索引；本卡补上了 SECG 这一层「白话合规说明」与四层效力栈，并指向 CAP-15 处理缺陷行动水平这一执法裁量参考；检查类型、三层分级、记录举证矩阵与 483 回复骨架由 **CAP-16 `inspection-readiness`** 承担，取样量与阳性升级由 **CAP-17 `inspection-sampling`** 承担，检查员权限/表单/证据链由 **CAP-18 `investigator-authority-procedure`** 承担；仍**不提供** IOM 其余章节（尤其 Ch.4 的 702(b) 与制样）、实验室方法正文、警告信答复策略、进口扣留应诉、具体行政文书代写，也不预测 NAI/VAI/OAI 结果。用户任务超出能力卡路由范围时，明确告知超出本包覆盖，不要硬套。

**B10 — SECG 的三处已知简化，凡涉及即须回法规正文。** SECG 的编制目的是让中小企业读懂规则，代价是若干处把「唯一强制路径」或「完整程序」压缩成了可选项或半截流程。已核出三处，**不是 SECG 出错，而是它选择不展开**：
- **供应商验证活动**：SECG IX.A 把四类活动并列成可选项，未提〔§ 117.430(b)(1)〕的强制现场审核升级（严重后果/死亡风险档位）与〔§ 117.430(b)(2)〕的书面判定出口，也未提〔§ 117.430(c)(d)(e)〕三类特殊供应商豁免。涉及「我能不能不现场审核」时必须查 § 117.430。
- **qualified facility 状态变更**：SECG XI.D 只写「由是变非」的通知与合规时限，未写〔§ 117.201(c)(2)(i)(C)〕「由非变是」须在当年 7 月 31 日前完成首次申报。两个方向都要查。
- **撤销豁免程序**：SECG XI.E 止于 15 个日历日答复窗口，未展开〔§ 117.254〕的批准层级、〔§ 117.257〕的令件内容、〔§ 117.260〕起的上诉与〔§ 117.267/117.270〕的非正式听证、〔§ 117.277〕的决定时限。凡问「撤销后还能不能申辩」，必须查到 § 117.277。
此外 SECG 的量化表述也有粗糙处：第 IV 章 Table 2 写 qualified facility 的本地销售占比为 `at least half`，而〔§ 117.3〕定义与 SECG 自身第 XI.A 节的写法是 `exceeded`（超过）。**以 `exceeded` 为准**——恰好等于一半不构成 qualified facility。凡遇 SECG 与法规在量词强弱上不一致，一律以法规为准并保留法规用词。

**B11 — 缺陷行动水平的引用陷阱（v4.7 更正，与 CAP-15 / CAP-20 共守）。** ① **Part 110 至今有效**：v4.6 及以前本卡写「Part 110 依 2015-09-17 最终规则于 2018-09-17 移除、Handbook 的 `21 CFR 110.110` 是过时引用」，该结论**不成立**。FDA 2018-09-12 最终规则（FR Doc. 2018-19855）撤回了 2015 规则的 amendatory instruction 13（`amendatory instruction 13 ... is withdrawn`），因合规日期延长会造成 4–16 个月 CGMP 空档；eCFR 现行版 Part 110 仍列 11 个 sections（含 §110.110）。因此手册引言指向的是**仍有效、但正文本包未收**的旧 CGMP 条款，须标「转引未收」；§114.5 并列 `parts 110 and 117` 同样是现行文本。② 手册那句 "Poor manufacturing practices may result in enforcement action without regard to the action level" 是 **§110.110(c)** 的意译，**仍不得标成〔§ 117.110(c)〕**（Part 117 的 §117.110 只有 (a)(b) 两款），但理由从「part 110 已删」更正为「那是 part 110 的 (c) 款、不是 part 117 的」；该层约束在 Part 117 体系下来自 FD&C Act § 402(a)(4) 与 Subpart B 整体。③ **措辞差异**：手册写混合「at or above the current defect action level」不合法，〔§ 117.110(b)〕写「at levels that render that food adulterated」——以法规措辞为准。索引表里〔§ 117.110〕一行的判定基准是 `lowest level currently feasible`，不是手册表内数字；手册是 FDA 执法裁量参考，不是合规上限或放行标准。2018-19855 正文属外部核实、本包未收。

**B12 — 第七来源 CPGM 7303.040 的两处版本陷阱（与 CAP-16 共守）。** ① **旧版已废止**：`2020-CPGM-CFSAN-003`（10/15/2020，47 页）把 critical/major/minor 挂在**单条观察项**上、`03040U` 是 `PCHF FOLLOW-UP INSPECTIONS`、联系人为 CFSAN / ORA；现行 `2025-CPM-HFP-001`（签发 08/29/2025，IMPLEMENTATION DATE 05/23/2024，50 页）改为单条观察项只有 eNSpect 的 major/minor、整次检查才分三级且调查员不做整体分级，`03040U` 改为 `FOCUSED PCHF INSPECTIONS`，机构改为 HFP / OII。凡 2020–2024 迎检 SOP 或二手摘要须先判版本。② **日期以 PDF 首页为准**：FDA 网页 Food Compliance Programs 列表所示日期与首页 IMPLEMENTATION DATE 不一致，属页面字段/更新时间，不得当作法规生效日；另 CPGM ATTACHMENT A 的 `1. Findings / 2. Charges / 3. Actions / 4. Follow-Up` 讲卫生运输（21 CFR 1 Subpart O），与主 PART V **同名不同口径**，引用须带 `ATTACHMENT A`。

**B13 — 第八/第九来源的两处口径陷阱（与 CAP-17 / CAP-18 共守）。** ① **CP 7303.050 是 2022 版程序的 2025 年更正本**：PDF 首页 `Date of Issuance 06/03/2022`、`IMPLEMENTATION DATE 06/03/2022`、`Correction date 09/10/2025`（62 页），文件名里的 `20250915` 不是新签发日期；不得套用 7303.040 的 `2025-CPM-HFP-001` Transmittal 格式。且 `Inspections are not planned under this compliance program`——它是抽样 program，不是检查 program；Table 2/3 的 subs 数是 FDA 取证量，不是企业内控放行标准。② **IOM 2026 只收 Chapter 5**：483 措辞纪律（IOM 5.5.10 / 5.5.11.3）从检查员侧反证四层效力栈——`Do not cite deviations from policy or guidance documents on the FDA 483`，仅偏离官方 guidance 而不违反法规的属 Category 3 non-reportable observation，只能口头讨论并写进 EIR。**但不得反过来读成「指南可以不做」**：同一事实若同时构成〔§ 117.xxx〕失守（如 `adequate`、〔§ 117.110(a)〕），仍是事实性观察项。IOM 正文的 Ch.3/4/6/7/8 等跨章引用一律标「转引未收」。
