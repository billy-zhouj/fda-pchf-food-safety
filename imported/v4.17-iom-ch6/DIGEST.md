# FDA Investigations Operations Manual 2026, Chapter 6: Imports — 精华 (DIGEST)

> 本文由 cangjie-skill 蒸馏生成，只呈现**通过三重验证**的方法论——不是全书摘要，是筛过水分的精华。
> 全书是 FDA 给入境审查员 / 调查员的内部作业手册，不是写给进口商的合规指南；读它正确的姿势是「理解 FDA 判定逻辑与举证要求的操作地图」，不是「合规规则引擎」。
> 想深入某个方法论时，点小节末尾的能力卡链接；想看全貌，读 `BOOK_OVERVIEW.md`；想查术语，读 [GLOSSARY.md](./GLOSSARY.md)。
> 作者: U.S. FDA, Office of Inspections and Investigations (OII)（机构出版物，无个人作者） | 2026 版 | 全文约 8000 字，预计阅读 25 分钟。
> 引用统一 `IOM 6.x.x [p.N]`；企业侧推导一律冠〔推导·非原书主张〕。

---

## 这本书在讲什么

美国每年面对的进口货物量远远大于 FDA 能动手查验的能力。第 6 章处理的就是这道算术题背后的制度设计：**在绝大多数货物根本不会被开箱查验的前提下，怎样让「这一批货能不能合法进美国」这个决定既合法、又能在听证和后续执法里站得住**。它的答案不是一套标准，而是一条把动作、顺序、字段、签字、时限全部固定下来的链条——从入境申报、电子审查、现场查验与取样，到可采性判定、放行或扣留拒绝，再到违规调查。

值得注意的是这本书「不是什么」。它是 Investigations Operations Manual（调查作业手册）的一章，读者是 FDA 自己人：入境审查员（entry reviewer）、调查员（investigator / CSO）、Compliance Branch 的合规官。它写的是「FDA 如何作出并执行决定」，不是「进口商如何准备举证、如何避免被扣、如何回应 483a」。全篇以 FD&C Act §801 等法定授权为公理，以流程顺序为推导，支撑材料是法条编号、CBP/FDA 表单编号、内部 SOP 与逐字段填写规范，而不是案例推演或理论论证。作者不「论证」，只是把一套判定动作钉死。

这就决定了它的价值与陷阱同源。它的浓度恰恰来自那些**反直觉的机构特定口径**：DWPE 的「不检查就扣住」、Failure to Hold 的「无放行即分销而非移出港区」、DER/DTR 按触发依据而非严重度分流、May Proceed 是终局放行而非「准许继续办理」、放行可撤消但条件放行期不重开、拒绝不是终点。这些东西外行说不出，聪明人也猜不中——它们不是「措辞文雅」，而是 FDA 内部的判定校准。可一旦把这本手册当成法规、把里面每一句 `must` 当成企业义务、把 `should` 当成建议，就会系统性高估它的法律位阶。所以本 DIGEST 在讲清楚每个方法论怎么运作之后，都会补一段「什么时候会失效」，并在最后专列「作者的局限」——只报喜不报忧的精华是软文，不是蒸馏。

本轮蒸馏把整章收敛为 **1 个来源路由入口（CAP-29）+ 10 个能力单元**：按章的骨架，它们分属「进口准入判定链（6.1–6.4）」「违规处置与追责（6.5–6.8）」「口径层（6.9 / 元规则）」三段。下面按这个骨架走，不按能力清单走。

---

## 进口准入判定链（6.1–6.4）

> 6.1→6.2→6.3/6.4 是一条不可逆的时间链：每一步的产物是下一步的输入。这四张卡共同回答同一组问题——一批货进来时，FDA 先读什么、能选哪几个动作、选错之后时钟怎么走。

### 事先通知：食品入境前的硬时限门（6.1）

**它解决什么问题**：判断某批食品/动物饲料是否须提交 Prior Notice、是否落在豁免清单，以及按运输方式与提交渠道算出来的合法时间窗到底是多少。这是整条链上最「可机械判定」的一张卡，也是几乎不与既有技能包重叠的干净增量。

**核心逻辑**：先判是不是 §201(f) 意义的 food 且不在免列，再取双向窗口——**上限**由提交渠道定（PNSI 15 天 / ABI-ACE 30 天，不得早于预计抵达日这么多天），**下限**由运输方式定（公路 2 小时 / 空运铁路 4 小时 / 水运 8 小时，均是抵达前）。关键在完成点是「FDA 电子**接收并确认**（received and confirmed）」，不是「已提交」；不满足即 inadequate → refusal + hold。指导文件（CPG / IOM）不构成豁免。

**书中的用法**：验证时用的反例是「境外企业经国际邮件向美国个人寄自家工厂生产的肉松零食，声称是个人礼物」。两处都错：① 「个人礼物」豁免要求「个人在其**住所自制**、作为非商业个人礼物寄送」，企业规模化生产不适用；② 国际邮件根本不走抵达前 2/4/8 小时口径，而是「**寄出前**须由 FDA 电子接收并确认，且包裹须随附确认回执」。缺回执即 inadequate，直接拒绝并在口岸/安全设施扣留，援引 CPG 宽限无效。

> "Food that is imported or offered for import with inadequate prior notice is subject to refusal and holding at the port or in a secure storage facility." —— IOM 6.1.5.5 [p.11]

**什么时候会失效**：适用面只限 food / animal feed，套到器械、化妆品上是错的；「早报总没错」的直觉在这里反着来——早于上限提交同样不合规；两个「15 天」同数异义（PN 上限 vs CBP Entry/Immediate Delivery 申报义务），混用即算错。

→ 深入: [`prior-notice-eligibility-gate`](dist/capabilities/imports/prior-notice-eligibility-gate.md)

### 入境审查决策门：有限动作集与可辩护留痕（6.2）

**它解决什么问题**：判断某条 entry line 在电子审查阶段该发 May Proceed、请求现场工作、提交扣留建议、以 OGA Referral 关闭，还是撤消；以及当决定与 PREDICT 筛查结果相悖时，备注写到什么程度才合格。6.2 是整条进口链的决策中枢，动作一旦选错，下游全链不可逆。

**核心逻辑**：自动筛查没发 May Proceed 就强制人工审查，审查前必须先看 PREDICT 风险分与全部 rule flags。产品看似不合规时**只有两个选项**——请求现场工作，或向 Compliance Branch 建议扣留，审查员不自行终局扣留。三类决定（请求扣留、请求现场工作、与 PREDICT 相悖的 May Proceed）必须写具体理由，`May Proceed` / `N/A` 这类空泛备注被点名禁止。合格备注的判据是「可核验的具体差异事实」（品牌不在 DWPE 名单、粉剂非液剂、单据证明不含肝素），不是字数、不是结论复述。

**书中的用法**：一个反直觉场景是「PREDICT 标高风险，但 CBP 已以走私为由扣押该批货并把扣押证明上传」。直觉会认为两个机关各自都要出决定、或「已被扣押＝不用管了」；手册的口径是走 OGA Referral（OGI/OGC）**关闭该 line，FDA 主动放弃作出可采性判定**，且关闭的硬前提是「他机关处置证明已上传」。签 May Proceed 等于 FDA 自己作了判定，提交扣留建议则与已扣押状态重复且越权。

> "Provide clear remarks in the FDA Import System when you: Request a detention / Request field work / Issue a may proceed that contradicts PREDICT screening results. Avoid vague remarks like 'May Proceed' or 'N/A'." —— IOM 6.2.1 [p.15]

**什么时候会失效**：本卡只管 6.2 电子审查阶段的准入动作与理由可辩护性，不产出 483 观察项（那是 IOM Ch.5 / CAP-18）、不执行取样（IOM Ch.4 / CAP-28）、不决定扣留建议走哪个 work type（交给下一张卡）。把「请求现场工作」里的「取样」字样当成取样执行，是典型越界。

→ 深入: [`entry-review-admissibility-decision-gate`](dist/capabilities/imports/entry-review-admissibility-decision-gate.md)

### DER / DTR 分流：按触发依据，不按严重度（6.2）

**它解决什么问题**：当某个疑似违规的 line 要提交扣留建议时，判断该用 DER 还是 DTR；命中 Import Alert 时能否免索单据直接 DER；数据库查不到注册/510(k)/PMA 或 A of C 缺失时能否直接建议扣留；企业自行送检的合格报告能否解除 DWPE。

**核心逻辑**：分流的唯一判据是**触发依据**——受 DWPE / Import Alert 约束用 DER，其余一切「看起来违规」用 DTR。这是本章被点名的头号反直觉口径：DER/DTR 不是轻重档位，快通道由「是否列名 Import Alert」触发，与严重度无关。而且「查不到 ≠ 违规」：数据库查询失败、A of C 缺失都只是核实起点，直接据此建议扣留被明文禁止，须先作 reasonable effort 核实；即便确需扣留，无法确认可采性也应走 DTR 而非 DER。

**书中的用法**：场景是「某产品在 FDA 数据库查不到 510(k) 与注册，filer 的 A of C 也缺失，审查员想直接扣留并走 DER 快速通道」。两步都错：① 6.2.5.5 明令不得仅凭 failed data lookup 或 missing A of C 建议扣留，须先用手上信息作合理努力核实（必要时请求 DRQ/FEX/SAM）；② 即便核实后确需扣留，触发依据是「无法确认可采性」而非「受 DWPE 约束」，应走 DTR（6.9.20 正是以注册、scheduled process filing、510(k)、PMA 无法核实为 DTR 示例）。若检索后确认不匹配任何 IA，还须用系统 feedback 写明为何不适用，并把全部研究写进 Remarks。

> "Use DER when a product is subject to Detention without Physical Examination (DWPE). DTR (All Other Detentions): Use DTR for all other situations where a product appears to be violative." —— IOM 6.2.5.1 [p.21]

> "You must make a reasonable effort to verify compliance using the information provided. Do not recommend detention based solely on a failed data lookup or missing Affirmation of Compliance data." —— IOM 6.2.5.5 [p.23]

**什么时候会失效**：本卡只输出向 Compliance Branch 提交的 work type 及其提交前核实义务，不管决策门选哪个动作、不定义状态词、不产出 483 观察项。另外 Import Alert 与 Import Bulletin 方向几乎相反（Alert → 别再请求现场工作、走 DER；Bulletin → 指示去请求现场工作、不触发 DWPE），把两者搞反会直接走错通道。须注意 6.2.5.5 这条 reasonable effort 条款的正文物理落在 [p.23]、与 6.3 起始页重叠，引用一律按小节号 `IOM 6.2.5.5 [p.23]`，不要按切块文件名。

→ 深入: [`der-dtr-detention-routing`](dist/capabilities/imports/der-dtr-detention-routing.md)

### 条件放行 / 撤消 / redelivery：一套不可逆的时间法（6.2–6.3）

**它解决什么问题**：算某批条件放行货物还剩多少可采性决定时间；判断哪些动作会/不会延长 30 天；误发 May Proceed 或 IB Release 后 24 小时、30 天内必须完成什么；撤消放行后期间能否重开；30 天与 90 天如何分。这是全章后果最不可挽回的一张卡——错过窗口，货无法召回，只能追偿 liquidated damages。

**核心逻辑**：条件放行期通常 30 天，以 May Proceed / 拒绝通知 / 30 天届满**三者最先发生者永久结束**；DRQ、DTR/DER、DEF、INF **都不延长**它，唯一延长路径是在首个 30 天内**书面**通知进口商且声明 FDA 将查验、取样或扣留。更反直觉的是「可逆」与「不可逆」同时成立：放行**可以撤消**，但撤消**不重开**条件放行期；而 CBP 请求 redelivery 的 30 天窗口**反而从放行日**起算，拖延会同时吃掉这个窗口。

**书中的用法**：场景是「进口商以为已提交 DTR 扣留请求＝审查时钟暂停，拖到第 35 天才追问为何条件放行期已过」。错在把请求动作当成延期——6.2.4 明确列出四类请求一个都不延期，第 35 天窗口已因届满永久关闭，FDA 事实上丧失在该期内作可采性决定的程序基础。若此前曾误发 May Proceed，期间同样已永久结束、撤消也不重开；货物一旦分销即无法召回，只能转入 Bond Action。

> "Once you issue a 'May Proceed,' the conditional release period for that entry ends permanently. Even if you rescind the notice, the period does not reopen." —— IOM 6.2.2.2.2 [p.17]

**什么时候会失效**：本卡只管时间窗的起算、终止、不延长、不重开与撤消后 24h/30d 补救动作序列，不认定是否构成违规、不定义状态词、不展开 Refusal 后处置链。用户示例「货已条件放行但未收 May Proceed 就发经销商」应路由到 Failure to Hold 那张卡，本卡只提供其 30 天窗口背景。三个「30 天」（条件放行期长度 / CBP redelivery 窗口 / FTH 下 4647 期限）与一个「90 天」（Refusal 后出口销毁）同数异义，混用即所有倒计时全错。

→ 深入: [`conditional-release-rescission-windows`](dist/capabilities/imports/conditional-release-rescission-windows.md)

---

## 违规处置与追责（6.5–6.8）

> 6.5 是货物被扣之后的全链；6.6–6.8 是对链条失效或延伸的并行追责支路。这四张卡共同回答：决定作完之后，文书、时限、保证金、刑事取证和进口商记录审查怎么收尾——以及为什么「发了通知」从来不等于「结案」。

### 违规处置主链：拒绝不是终点（6.5）

**它解决什么问题**：判断某批被扣货物下一步该出哪张通知/文书、由谁签字；算听证期与 90 天出口/销毁期；判断收到 Refusal Notice 后企业内部能否结案；理解 Detention（临时可回转）与 Refusal（终局）的分界；判断拒绝后未按期处置的经济后果。

**核心逻辑**：扣留后走听证 → 举证 → 重整 → 复核 → 放行或拒绝，每一步绑定固定文书（Notice of FDA Action、FDA 766、Importer's Certificate、Notice of Release / Refusal、FDA 790、CBP 4647）与经济后果（Bond Action）。最核心的校准是「发出通知」与「责任解除」被解耦：**Refusal of Admission 不是流程终点**，之后还有 90 天内于 CBP 监督下出口或销毁、4647 redelivery、销毁/出口核验、Bond Action；FDA 档案在分部收到销毁/出口证明之前保持开放，公共健康责任延续到违规品实物灭失为止。Detention 是 temporary / administrative / 基于「appear not to be」外观标准，Refusal 才是 final decision；Refusal 通知的 charge 须与原 Detained 通知逐字一致。

**书中的用法**：场景是「收到 Refusal 后第 80 天才安排出口，证明预计第 100 天回传；进口商想把货先转内销减损」。都不行：① 90 天约束的是「出口或销毁**完成**」而非「已安排」；② 档案未关闭；③ 转内销既属「已扣留并拒绝却未依法销毁/出口」又属放行前分销，直接触发 Bond Action（主体是 CBP，追缴 liquidated damages）。「安排」与「完成并取证」之间的差距，正是 Bond Action 的触发点。

> "The FDA file remains open until the division receives notification indicating that the goods were either destroyed or exported." —— IOM 6.5.2.8 [p.41]

**什么时候会失效**：本卡管 6.5 下游处置链的全貌与文书/时限矩阵，不放行 766 授权门的内部判据、不算条件放行期、不认定 FTH 违规。483 是 IOM Ch.5 的现场检查观察项，与本卡 Notice of FDA Action 是完全不同的文书序列。另 OCI 刑事取证不得改变 FDA 处置顺序——不能「因为可能成为证据就另走一套标准」（IOM 6.6.2 [p.42-43]）。

→ 深入: [`violation-disposition-chain`](dist/capabilities/imports/violation-disposition-chain.md)

### 改标 / 重整：Form FDA 766 授权门（6.5）

**它解决什么问题**：收到 Detained 通知后能否自行改标/返工再申报；重整申请由谁提交、要不要新 bond；首次失败后能否再试、要举证什么；合格部分放行后 rejects 怎么处置。它直接命中用户给的「进口商收到 Detained 后想自行改标再申报」场景。

**核心逻辑**：重整效力来自「importer of record **申请** → FDA 766 **批准并载明条件与时限** → 复核」三段，企业自行返工无效。手册用 `may authorize` / `approval or disapproval` 明示这是**机构裁量**而非企业权利。首次失败后第二次机会的门槛是「**修订后的方法本身能合理保证成功**」，举证对象是方法而非意愿；即便条件满足放行，rejects 仍须在监督下销毁或再出口并**单独**出具 Refusal。

**书中的用法**：场景是「进口商不等 FDA 回复就自行撕标重贴、分选返工，按原申报重新提交，认为整改完自然放行；首次被拒后又原样再试一次」。四处错：① 自行整改不产生放行效力、货物仍按违规处理；② 申请主体是 importer of record（不是 FSVP Importer、不是境外生产商），改标 ⊂ 重整；③ 原样再试（只改日期）不构成「修订方法」，原则上不予考虑；④ 部分放行 ≠ 整批结案。

> "A second attempt should not be considered unless a revised method of reconditioning shows a reasonable assurance of success." —— IOM 6.5.2.6 [p.40]

**什么时候会失效**：本卡只管 766 授权门及其内部判据，不展开听证→拒绝→90 天→Bond 全链、不定义术语、不下法律位阶结论。企业侧「返工」在本卡被明确标注为不产生放行效力，与包内生产返工类卡的语境不同；已备案的 redelivery bond 适用于获批改标、无须另立新 bond。

→ 深入: [`fda-766-reconditioning-authorization`](dist/capabilities/imports/fda-766-reconditioning-authorization.md)

### Failure to Hold：按「分销」而非「位移」判定（6.6）

**它解决什么问题**：判断某批条件放行货物是否已构成 Failure to Hold；区分「移库/位移」与「分销」在违规认定上的差别；列出所有 FTH 案件必做的 8 步取证与 affidavit；判断健康危害 / DWPE 情形是否追加召回与公共警告；判断 CBP 4647 该用 30 天还是 90 天。这是用户点名的头号反直觉口径。

**核心逻辑**：判定要件是「**未获 FDA 放行即已分销**」，**不是**「货物被移出港区」——原文特意用 `*Please note` 纠偏，说明作者预期读者会弄错。条件放行期内货物「may be moved」（位移合法、法律状态未变），位置与法律状态被刻意解耦。一旦成立，8 步清单对**所有**该类案件必做：取单据 → 分析分销记录 → 确定授权人 → 判断是否知悉健康危害 → 取授权人说明并作成 affidavit → ORADSS 检索历史 → 协调 CBP 签发 4647 → 核定 bond；①–⑤ 须固化为**宣誓书**而非普通访谈记录。健康危害/DWPE 情形再追加召回、收货人通知、公共警告协调。

**书中的用法**：场景是「冷冻罗非鱼片已条件放行但尚未收到 May Proceed 就发给经销商，企业辩称货一直在保税仓/港区内、只是移库」。辩解恰好踩中手册纠偏的误读：① 要件是「无放行而分销」，位置变化不构成该违规，所以「还在港区」不是抗辩；反过来「发往经销商」已构成 distribution，即便物理上仍在港区内也成立；② 8 步必做；③ 4647 若因查验/取样签发，期限是 30 天而非拒绝后的 90 天，且 4647 可为查验/取样而发、不必先有 FDA 拒绝；④ 命中 Import Alert/DWPE 或涉 Salmonella 时即便仅达外观违规标准仍属高优先级。

> "Please note that this is defined as distribution without a release, not merely moving the goods outside of the port area." —— IOM 6.6.4.1 [p.43]

**什么时候会失效**：本卡只认定 FTH 违规要件并给出 8 步取证下限与加重分支，不算条件放行期倒计时、不定义状态词。Substitution（调包）在查明前一律按 FTH 处理且须查验整批。〔推导·非原书主张〕企业侧由此可反推一条理解：放行前须保持货物 intact 且不进入分销，WMS 发货闸门应以「是否收到 FDA 放行」而非「是否已移库」为触发——这是从 FDA 判定动作反推的理解，非手册主张。

→ 深入: [`failure-to-hold-investigation`](dist/capabilities/imports/failure-to-hold-investigation.md)

### FSVP 检查链与 FDA 483a 签发门（6.8）

**它解决什么问题**：判断 FSVP 检查对象与 Importer of Record 的区别；现场检查期间能否向企业展示 483a 草稿；观察项该写进 483a、T-EIR 还是 CARS；理解危害分析比对与差异追问；计算 15 工作日回应窗口；判断 importer 不满足定义时 EIR 怎么处理。

**核心逻辑**：FSVP 检查**对象是进口商的记录，不是货物**，是与货物查验并行的独立合规轨。检查动作是先把监管方自己的「潜在危害初步评估」与进口商危害分析**比对**、有差异先讨论确定其**理由**，而不是直接下「漏了危害」的结论。483a **只在检查结束（closeout）时签发且只签已签名版**，检查期间不得向管理层展示任何 draft / unsigned / 屏幕电子稿；存疑重要性的观察项不列入 483a（当场讨论、记 T-EIR）；纠正措施不写在 483a 上，须报 T-EIR 并把纠正措施及预计完成日期记入 CARS。

**书中的用法**：场景是「调查员在 FSVP 检查第 2 天发现进口商危害分析漏了某过敏原危害，当场打印未签名 483a 草稿交管理层『先看着准备』，并把企业承诺的整改措施写进草稿」。至少四处违规：① 草稿不得示人且只能 closeout 签已签名版；② 检查顺序反了（应先比对追问理由）；③ 存疑重要性的观察项不列入 483a；④ 纠正措施走 T-EIR / CARS 而非 483a。

> "The FDA 483a should only be issued at the conclusion of the inspection... Use care, during the inspection, to not show or reveal to the firm's management any draft, unsigned copy... or electronic copy." —— IOM 6.8.2.1 [p.48]

**什么时候会失效**：这是与既有技能包重叠风险最高的一张卡。**CAP-21 管 FSVP 合规程序 / 检查依据（CP 7303.878 / §1.500 主体定义 / subpart L 条款级）**，本卡只是 IOM 6.8 的检查执行 SOP；**483a（IOM 6.8 FSVP 观察项）≠ 483（IOM Ch.5 / CAP-18 现场检查观察项）**，二者名称相近、章节与文书序列都不同。发出 483a 后应告知进口商在检查结束日后 15 个工作日内回应。

→ 深入: [`fsvp-inspection-483a-gate`](dist/capabilities/imports/fsvp-inspection-483a-gate.md)

---

## 口径层（6.9 与元规则）

> 6.9 是横切全链的术语层，还有一张不落在任何 6.x 小节、却是全部卡 Boundary 来源的元规则。这两张卡**都不产出业务判定**：它们回答「这个词意味着什么」「这条结论能不能据此主张」，专门服务「不可混引」。

### 进口状态概念区分树（6.9）

**它解决什么问题**：判断某个 FDA 状态词到底意味着「能不能分销」；区分 May Proceed / Release / IB Release / Release with Comment 四种放行；区分 Conditional Release 与 May Proceed；区分 Detention 与 Refusal；区分三个 30 天与一个 90 天；判断「货可以移动」是否等于「可以销售」。本轮唯一允许术语独立成能力卡的例外——这组术语本身构成判定框架。

**核心逻辑**：先把状态词归位。**Conditional Release 是等待判定的状态**（可移动不可分销、附 3 倍货值 redelivery bond）；**May Proceed / Release / IB Release / Release with Comment 是四种法律含义不同的放行**——May Proceed 未作合规判定、Release 已作合规判定、IB Release 由调查分部在查验后裁量作出、Release with Comment 是「已明确认定存在违规（无公共健康风险）仍放行」并**预告后续同类 entry 可能被拒**；**Detention 临时可回转**、**Refusal 终局但非终点**。三种术语误读方向高度一致：**都让人高估自身合规状态**——这是全书最系统的一组反直觉。

**书中的用法**：场景是「企业把 WMS 状态机里四种 FDA 文书统一映射成『放行 = 可销售 + 已合规 + 此批结案』，并把 CBP immediate delivery 回执也归到同一状态」。至少四处误判：把 May Proceed 当合规背书（错过撤消窗口）、把 Release with Comment 当没问题（不整改、后续被拒毫无准备）、把 IB Release 当 May Proceed（误判阶段与是否已形成合规决定）、把 Conditional Release / immediate delivery 当放行安排上架（直接构成 Failure to Hold + Bond Action）。

> "May Proceed: 'Product may proceed without FDA examination. FDA has made no determination the product complies...' (No compliance decision has been made.)" / "Release: 'The product is released after FDA examination... (A compliance decision has been made.)'" —— IOM 6.4.3 [p.35]

**什么时候会失效**：本卡是**口径判定层**，只回答「这个状态词意味着什么、能不能分销、属于哪个窗口」，不产出动作、不算时限倒计时、不展开处置链、不认定违规，须依附业务卡使用。「IB」同形异义（Import Bulletin vs Investigations Branch）、「货可以移动」≠「货可以分销」、三个 30 天与一个 90 天、AGR（美国货退回视为进口）与 Re-export（不适用 §801(e)）方向相反——这些都要靠它归位。

→ 深入: [`admission-status-concept-tree`](dist/capabilities/imports/admission-status-concept-tree.md)

### IOM 效力层判读元规则（元规则，全包 Boundary 来源）

**它解决什么问题**：判断某条 IOM 表述能否对企业主张为法定义务或权利；把 should / as warranted / may 与 must / shall 分开读；识别 `should only` / `should not` 这类「用裁量词承载禁止/唯一时点」的反向陷阱；判断指导文件（CPG / IOM）是否构成豁免；理解 2026 版快照；为企业侧迎检推导内容标注〔推导·非原书主张〕。

**核心逻辑**：**IOM 是内部操作指导、不是法规、不是可对外主张的法律依据**。`must` / `shall` / 祈使约束的是 FDA 审查员的内部作业动作；`should` / `as warranted` / `may` 属机构裁量且章内几乎不给判据。映射不是纯机械的：`should only` / `should not` 形式软、语义却是禁止或唯一时点，`should … on all cases` 反而用裁量词覆盖全部个案，同一句内还可硬软并存（should only rescind / You must act immediately）。任何结论须回到 FD&C Act §801、21 CFR Part 1、19 CFR 113.62 与当前版本 IOM/RPM 复核。

**书中的用法**：场景是「企业法务引用 IOM 6.2.4 的 `must`，主张『FDA 逾期未作可采性决定即丧失扣留权、企业可自行分销』，并援引 CPG 指导里的宽限说明主张免检」。不成立且是典型效力层误读：① 该 `must` 约束的是 FDA 审查员的内部作业时限，不产生企业可诉权利，FDA 个案偏离 IOM 通常也不产生可诉权利；② 条件放行期届满不等于已放行，自行分销反成 FTH 并触发 Bond Action；③ CPG / IOM 指导 `does not limit` FDA、`will not affect` CBP 处罚权，不构成豁免；④ 2026 版是快照，系统/SOP 编号会随改版失效。

> "This guidance, however, does not limit the FDA's ability to take actions that may be necessary... This policy will also not affect the ability of CBP to assess penalties under 19 U.S.C. 1595a(b)." —— IOM 6.1.5.5 [p.11]

**什么时候会失效**：本卡**唯一的输出是「该结论的法律位阶与可主张性」**，不回答任何业务判定（不放行、不扣留、不算时限、不认定违规），须依附业务卡的 B 段或作为判读前置步骤。它是「不可混引」约束的法律位阶依据：把 IOM 当法规、把 `should` 当 `shall`、把指导当豁免，都会把不同章节 / 不同位阶的内容错误串成一条规则。

→ 深入: [`iom-effect-level-modality`](dist/capabilities/imports/iom-effect-level-modality.md)

---

## 陷阱与反例

这些是整章最容易被聪明人答错、也最该写进负例库的失败模式。每条讲清「陷阱是什么 → 为什么人会掉进去 → 预警信号」。

1. **把「不检查」读成「不检查就放过」**。DWPE 的英文是 Detention **Without Physical Examination**，字面「不检查」极易被当成免检放行的福利，实际恰相反——基于违规史 / Import Alert 免实物查验**即扣**。人会掉进去是因为「without examination」在其它语境里几乎总是好事。预警信号：凡是出现 DWPE / Import Alert 命中，正确方向是走 DER、别再请求现场工作，而不是去安排查验或放行。〔IOM 6.9.22 [p.52]、6.2.5.1 [p.21]〕

2. **把「查无记录」当违规证据、把 DER 当更严重的档位**。数据库查不到注册 / 510(k) / PMA、A of C 缺失，直觉会当成「有问题」直接扣留；DER 听起来像快速通道、像「严重案件专用」，于是想当然走 DER。实际明文禁止「仅凭 failed data lookup 或 missing A of C 建议扣留」，须先作合理努力核实；核实后确需扣留也该走 DTR。预警信号：出现「查不到」「缺字段」「快速通道」这些词时，先问「触发依据是 DWPE 还是无法确认可采性」。〔IOM 6.2.5.5 [p.23]、6.2.5.1 [p.21]〕

3. **按位置而非放行状态判断违规**。「货物被移出港区」听起来才像出事，「还在保税仓里」听起来就没事，于是把「已发经销商但货仍在港区」当成移库放过。手册特意用 `*Please note` 纠偏：要件是「无放行而分销」，不是位移。预警信号：任何「货没动 / 还在港区 / 只是移库」的辩解，都要改问「有没有 FDA 放行、有没有进入分销」。〔IOM 6.6.4.1 [p.43]〕

4. **把「收到通知 / 发了通知」当终点**。收到 Refusal Notice 就归档、发出 Refusal 就结案，是最自然的行政直觉；实际 FDA 档案保持开启到销毁/出口证明到手，责任延续到违规品实物灭失。预警信号：「已安排出口」「等证明回传」「先转内销减损」——「安排」与「完成并取证」之间的差距正是 Bond Action 的触发点。〔IOM 6.5.2.8 [p.41]〕

5. **发现错误就撤回来重来、案子还在审时钟就该停**。「撤消」听起来像回退，「提交请求」听起来像暂停。实际放行撤消后条件放行期**不重开**，DRQ/DTR/DER/DEF/INF 一个都不延期，CBP 的 30 天 redelivery 反而从放行日起算——这是一套不可逆的时间法。预警信号：「撤回重做」「时钟暂停」「拖到第 35 天再问」。〔IOM 6.2.2.2.2 [p.17]、6.2.4 [p.20]〕

6. **把四种放行统一映射成「放行 = 合规」**。把 May Proceed / Release / IB Release / Release with Comment 一律当成「已合格、此批结案」，尤其把 Release with Comment 当「没问题」。实际它是「已明确认定存在违规仍放行」并预告后续可能被拒，会进入合规历史影响 PREDICT / DWPE 判定。预警信号：状态机里只有一个「放行」终态、或把 CBP immediate delivery 回执也归到「放行」。〔IOM 6.4.3 [p.35]、6.9.69 [p.57]〕

7. **把 `should` 一律译成建议、把 `must` 读成企业义务**。「手册写了 must，对方没做到我就获得权利」是最典型的效力层误读；`should only` / `should not` / `should … on all cases` 则形式软、语义硬。预警信号：结论里出现「FDA 必须」「企业有权」却只引了 IOM 6.x.x，或把 CPG / IOM 指导里的宽限当豁免依据。〔IOM 6.2.2.2.2 [p.17]、6.6.4.1 [p.43]、6.1.5.5 [p.11]〕

8. **483 / 483a 混用**。名称相近到几乎必然串：483 是 IOM Ch.5 现场检查观察项，483a 是 IOM 6.8 FSVP 观察项，章节、对象、签发时点、配套报告（EIR vs T-EIR/EIR/CARS）全不同。预警信号：在 FSVP 语境里出现「483」、或把「检查期间先给草稿让企业准备」当成贴心服务。〔IOM 6.8.2.1 [p.48]、CAP-18 分流〕

---

## 作者的局限（读这本书要打的折扣）

只报喜不报忧的精华是软文。这一章有四处必须打的折扣，它们直接构成本轮 10 张能力卡 Boundary (B) 字段的来源。

- **它不是法规，也不产生企业权利**（最强反对意见）。IOM 是内部操作指导，真正义务来自 FD&C Act §801、21 CFR Part 1（含 Prior Notice、FSVP）、19 CFR 113.62 等；`should` / `as warranted` 属机构裁量，FDA 个案偏离 IOM 通常不产生可诉权利。把本章蒸馏成「合规规则引擎」会系统性高估法律位阶。任何结论须回到法条与当前版本 IOM/RPM 复核。〔BOOK_OVERVIEW §3、能力卡 V10〕

- **强绑定 2026 年的 IT 系统与内部文书（时代局限）**。PREDICT、OASIS、ITACS、eNSpect、ACE、SERIO 与 WI-000618、SOP-000217、ER Job Aid 等界面 / 流程 / SOP 编号会随系统改版失效；2026 版是快照而非稳定规则。更要命的是**大量结论靠跨章引用承载**——IOM 4.x（取样）、5.x（证据/报告）、8.x（调查备忘录）、RPM Chapter 9（放行/听证/拒绝/保证金）、各 CPGM 才是细则所在；单读第 6 章会得到一个「有骨架、缺细则」的闭环幻觉。Exhibit 6-1~6-4（Notice of FDA Action、FDA 766、FDA 790、FDA 463a）在本次 PDF 中是扫描图像、无文本层，表单字段只能标「需查原件」。

- **全篇监管者视角，组织前提被隐去（立场盲点）**。写的是「FDA 如何作出并执行决定」，不写「进口商 / 境外生产商如何准备举证、如何避免被扣、如何回应 483a」；默认使用者有 FDA 授权、系统权限、Division / Compliance Branch / OCI / CBP 协作通道。企业或个人照搬，会把「检查清单」误当「合规义务清单」。手册也几乎不谈相对方的权利与救济成本：听证被描述为 informal meeting，但对进口商而言是举证、时间、滞期与保证金风险的集中点。本 DIGEST 里所有企业侧理解因此一律冠〔推导·非原书主张〕。

- **把自由裁量当自明、假设数据可靠、假设「有记录＝有合规」（未被证明的假设）**。`as warranted` / `where appropriate` / `should` 密集出现却很少给判据（请求扣留 vs 现场工作的选择标准、adverse conditions 阈值、照片 warranted 情形都留给分部惯例）；整套流程建立在 filer 传输数据准确之上，而 6.7 的 filer evaluation 只是周期性抽样监控，并未论证抽样足以支撑逐批判定；SCR 字段、备注、照片标识被高度规范化，但记录齐备与实际可采性之间的差距未被讨论。裁量判据缺失应作为复核锚点，**不应补写成规则**。

---

## 关键术语速查

| 术语 | 作者的用法 | 和常识的差异 |
|---|---|---|
| Entry / Line | 一次报关中可单独审查、单独判定的最小单元 | 不是「一批货」；一个 entry 多 line 可分别放行/扣留 |
| May Proceed | 未经查验、未作合规判定的终局放行 | 不是「可以开始办理」，也不是「已判定合规」，且可 rescind |
| Conditional Release | 等待判定期间的状态，可移动不可分销、附 3 倍货值 bond | 不是「有条件地合格」；「可移动」≠「可销售」 |
| Failure to Hold | 未获 FDA 放行即已分销 | 不是「货物被移出港区」；关键在分销非位移 |
| DWPE | 凭违规史/Import Alert 免实物查验即扣 | 不是「不检查就放过」，恰相反 |
| DER / DTR | 扣留建议的两种 work type，按触发依据分流 | 不是严重度分级，且审查员提交的是建议非决定 |
| Prior Notice | 发给 FDA、有确认回执的独立法定前置义务 | 不是报关单的一部分；早报同样违规 |
| Reconditioning | importer of record 申请 → FDA 766 批准并监督 | 不是企业自行返工；未经批准的整改不产生放行效力 |
| Refusal of Admission | 终局决定，90 天内出口/销毁，档案到证明到手才关闭 | 不是流程终点 |
| PREDICT | 风险筛查输入，可被有理由的 May Proceed 覆盖 | 不是自动判决；相悖放行必须写明理由 |
| FSVP Importer | FSMA 供应商验证义务主体，须在美国境内 | 与 Importer of Record（CBP 报关/bond 主体）常非同一人 |
| 483a | IOM 6.8 FSVP 观察项，只 closeout 签已签名版 | ≠ 483（IOM Ch.5 现场检查观察项） |

完整 28 条词典、成对易混矩阵与源层瑕疵（6.9 共 78 条、末条 `6-9.78` 编号不一致、DER/IUC/Import Bulletin/SDI/IB Release/VQIP 本体 6.9 未收须回 6.1–6.8 取定义、`IB` 同形异义）见 [GLOSSARY.md](./GLOSSARY.md)。

---

## 如果只带走三句话

1. **这是一张「FDA 怎么判」的操作地图，不是法规、不是企业义务清单**——`must` 约束的是审查员内部作业，`should` 是机构裁量，任何结论都要回到 FD&C Act §801、21 CFR Part 1、19 CFR 113.62 与当前版本 IOM/RPM 复核；企业侧理解一律冠〔推导·非原书主张〕。

2. **全章最值钱的是一组方向一致的反直觉：都让人高估自己的合规状态**——DWPE 是「不检查就扣住」、Failure to Hold 是「无放行而分销」、May Proceed 是「未作合规判定」、Release with Comment 是「已认定违规仍放行且预告后续被拒」、条件放行是「可移动不可分销」。把字面语义整体反转，才读得懂这本手册。

3. **时间不可逆、通知不等于结案、快通道看触发依据不看严重度**——发出 May Proceed 即永久终结条件放行期（撤消不重开）、四类请求一个都不延期、Refusal 之后还有 90 天出口销毁与 Bond Action、DER 只因列名 Import Alert 而触发、「查无记录」被禁止当作扣留依据。选错动作、错过窗口，后果是货召不回、只能追偿 liquidated damages。

---

*本文只写通过三重验证的 10 个能力单元；每个方法论小节末尾链接到 `dist/capabilities/imports/<slug>.md` 对应能力卡。引用统一 `IOM 6.x.x [p.N]`，英文引用每段 ≤100 词，企业侧内容冠〔推导·非原书主张〕。*
