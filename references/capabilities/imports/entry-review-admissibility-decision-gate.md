> 本卡隶属 CAP-29 来源路由入口 references/capabilities/iom-imports-procedure.md；加载前先读该入口卡。

# 入境审查决策门与可辩护判定留痕（entry-review-admissibility-decision-gate）

*来源分层与定位：IOM 2026 Ch.6 是 FDA 内部操作指导（Investigations Operations Manual，OII 机构 SOP），不是法规，不创设企业义务；与 IOM Ch.4（取样全流程）、IOM Ch.5（检查员权限与 483）、CP 7303.878（FSVP 检查）、CP 7303.050（取样量）分层，不得混引。本卡只落在 IOM 6.2 Entry Review 的**电子审查阶段准入决策门**，以及 6.1.6.2 / 6.9.57 的 Notice of FDA Action 口径层。6.2 是整条进口链的决策中枢，其动作集与「决定须可被听证/复核」是后续所有处置的输入；一旦动作选错，下游全链不可逆。本卡产物是 May Proceed / 请求现场工作 / 提交扣留建议 / OGA Referral 关闭 / 撤消五类动作及其理由留痕，不产出 483 观察项、不执行取样、不决定扣留建议走 DER 还是 DTR（V02）、不计算条件放行期（V04）、不定义状态词（V09）。*

## R — 原文

> "When the FDA's initial automated screening does not issue a 'May Proceed,' an entry reviewer must manually review it." / "Before you take any action, you must review and consider the recommendations from the FDA Import System, including the PREDICT risk score and any rule flags." / "A 'Priority Review' flag points to a major public safety risk. This includes products that are subject to Detention Without Physical Examination (DWPE). If you decide to issue a 'May Proceed' for a line with a priority review flag, you must write a clear reason in the 'Remarks' field. Vague remarks do not provide enough information."
> —— IOM 6.2.2.2 [p.16]
> 中文自译：当 FDA 的初始自动筛查没有签发「May Proceed」时，入境审查员必须转为人工审查。在采取任何动作之前，你必须审阅并考虑 FDA 进口系统给出的建议，其中包括 PREDICT 风险评分与全部规则标记。「Priority Review」标记指向重大公共安全风险，其中就包括受 DWPE（免实物查验扣留）约束的产品；若决定对带此标记的 line 签发 May Proceed，必须在 Remarks 栏写出明确理由——空泛备注提供的信息量不够。

> "Examples of Clear Remarks: 'The product brand submitted for entry is not a brand name subject to DWPE.' 'Product is in powdered rather than liquid form.' 'Specific manufacturer and/or product is exempt from IA XX-XX.' 'Documentation shows imported item does not contain heparin.'" / "Examples of Vague Remarks: 'Line is not subject to IA', 'NA', 'May Proceeded'."
> —— IOM 6.2.2.2 [p.16]
> 中文自译：手册给出的「合格备注」示例是「所申报品牌不属于受 DWPE 约束的品牌名」「产品为粉剂而非液剂」「特定制造商/产品豁免于 IA XX-XX」「单据显示进口品不含肝素」；「空泛备注」示例是「本 line 不受 IA 约束」「NA」「May Proceeded」。前者都是可由第三方核验的具体差异事实，后者只是结论或动作的复述。

> "Provide clear remarks in the FDA Import System when you: Request a detention / Request field work / Issue a may proceed that contradicts PREDICT screening results. Avoid vague remarks like 'May Proceed' or 'N/A'." / "Note: remarks field is for internal FDA use only."
> —— IOM 6.2.1 [p.15]
> "Correct any inaccurate data (manufacturer, shipper, product code, quantity, etc.) that could affect PREDICT screening. Assign fault to the responsible party. Save and rescreen the entry/line after making corrections."
> —— IOM 6.2.1 [p.14]
> 中文自译：三类决定必须在系统里写清具体理由——请求扣留、请求现场工作、以及与 PREDICT 筛查结果相悖的 May Proceed；「May Proceed」「N/A」这类空泛备注被明确禁止，且备注字段仅供 FDA 内部使用。另有一条前置硬动作：更正任何可能影响 PREDICT 筛查的不准确数据（制造商、发货人、产品代码、数量等），把错误归属指派给责任方，更正后保存并重新筛查（rescreen）该 entry/line。该节标题在 [p.14] 而备注段落在 [p.15]，本卡按各自所在页分别标注。

> "You should issue a 'May Proceed' for an entry line if you can confirm it meets all regulatory requirements using the electronic information and documents, and you see no need to detain it or request field work." / "The FDA automatically sends a 'May Proceed Notice' to both Customs and Border Protection (CBP) and the filer. The filer is then responsible for telling the importer. This notice means the shipment can continue without further FDA examination." / "Important: A product that is allowed to enter the country can still face legal action later if the FDA finds it violates the law (as stated in section 304(d) of the FD&C Act)."
> —— IOM 6.2.2.2.1 [p.17]
> 中文自译：只有能凭电子信息与单据确认某 line 满足全部法规要求，且认为既无需扣留、也无需请求现场工作，才应签发 May Proceed。系统会自动把 May Proceed Notice 发给 CBP 与 filer，再由 filer 转告进口商；该通知意味着货物无需 FDA 进一步查验即可继续。但获准入境的产品日后若被发现违法，仍可依 FD&C Act §304(d) 被追究。

> "If a product appears non-compliant, you have two options: 1. Request field work. 2. Recommend detention to the Compliance Branch (CB)."
> —— IOM 6.2.5 [p.21]
> "Use the OGI (Other Government Agency - Investigations) and OGC (Other Government Agency - Compliance) work types to close an entry line without the FDA making an admissibility decision. This is done when another government agency is handling the entry." / "You can close a line with an OGA referral when another agency (like CBP) has decided to refuse or seize a shipment. Before you close the line, you must obtain and upload documents that show what the other agency did with the product." / "If you only need to share information with another agency but the FDA will make an initial admissibility decision, use an Ad-Hoc OGA Referral (an Ad-Hoc referral does not close the line)."
> —— IOM 6.2.2.2.6 [p.19]
> 中文自译：产品一旦看似不合规，审查员只有两个选项：请求现场工作，或向 Compliance Branch 建议扣留——没有「审查员自行终局扣留」这一支。当另一政府机关正在处理该票时，用 OGI / OGC 两种 work type 关闭该 line，**而 FDA 不作可采性判定**；关闭的硬前提是「他机关已拒绝或扣押」且「已取得并上传其处置证明」。若只是共享信息、FDA 仍要作初始可采性判定，则用 Ad-Hoc OGA Referral——它不关闭 line。

> "Gives notice to the owner, operator, or agent-in-charge of an imported product, providing more specific information on the actions taken by the agency, broken down by each entry line (including, 'sample collected,' 'intended for sampling,' 'detained,' 'released,' or 'refused')."
> —— IOM 6.9.57 [p.56]
> "FDA Import Systems will generate a 'Notice of FDA Action,' which will provide more specific information on the actions taken, broken down by each entry line... As the status changes for a particular line, a new 'Notice of FDA Action' will be issued to advise appropriate parties of the changes."
> —— IOM 6.1.6.2 [p.13]
> "You should only rescind a 'May Proceed' in rare cases, such as when a product requires a compliance action. You must act immediately, as this action is not for routine examinations. Once you issue a 'May Proceed,' the conditional release period for that entry ends permanently. Even if you rescind the notice, the period does not reopen."
> —— IOM 6.2.2.2.2 [p.17]
> 中文自译：Notice of FDA Action 是**按每个 entry line 逐项**告知已采取动作（已取样／拟取样／扣留／放行／拒绝）的通知；某条 line 的状态每变化一次，就重新出具一份新通知告知相关方——它不是「一次扣留通知」，而是随状态反复出具的系列文书。撤消 May Proceed 只应限于罕见情形（如产品需采取合规行动），且必须立即行动，不得用于例行查验；一旦签发 May Proceed，该 entry 的条件放行期即永久结束，即便撤消通知，该期间也不会重新开启。

**引文覆盖对照（verified.md V01 `source_evidence` 关键口径 → R 组）**

| source_evidence 关键口径 | 落点 |
|---|---|
| 6.2.2.2 [p.16] 自动筛查未发 May Proceed 即强制人工审查；Priority Review flag 放行须 clear reason | 组 1 |
| 6.2.2.2 [p.16] Clear / Vague Remarks 正例与反例 | 组 2 |
| 6.2.1 [p.15] 三类决定须 clear remarks、禁 "May Proceed"/"N/A"；6.2.1 [p.14] 数据更正四步 | 组 3 |
| 6.2.2.2.1 [p.17] 电子单据确认全部合规且无需扣留/现场 → 签发 May Proceed | 组 4 |
| 6.2.5 [p.21] 疑似不合规只有两选项；6.2.2.2.6 [p.19] OGA 关闭与他机关处置证明 | 组 5 |
| 6.9.57 [p.56] / 6.1.6.2 [p.13] NOA 逐 line、随状态反复出具；6.2.2.2.2 [p.17] 撤消不重开 | 组 6 |
| V1 跨域佐证：6.3.10.7 [p.32] 按 Exam Class 收窄 Next Steps、6.1.4.6.1 [p.9] IFE 决策门、6.5.2.7 [p.40] 改判须写理由 | I 段 / A1 情景三 / B 段 |

**本卡反直觉口径清单（V3 机构特定校准，非聪明人常识）**
1. "May Proceed" 字面像「准许继续办理」，实为终局放行动作、可 rescind，且系统定义明确「未作合规判定」。
2. 把放行动作名写进 Remarks 当理由，是手册点名的头号错误——动作 ≠ 判定依据。
3. 合格备注的判据是「可核验的具体差异事实」（品牌、剂型、成分检测），不是字数、不是结论复述。
4. PREDICT 是输入不是判决；高风险分不构成自动判决，与筛查相悖的放行必须写明理由。
5. OGA Referral 的法律后果是「FDA 不作可采性判定就关闭 line」，而非「转交协查、FDA 仍出决定」。
6. 存在一条「主动放弃判定并关闭」的合法分支，且带「他机关处置证明已上传」的文书前提；直觉上的「两机关各出决定」与「已扣押=不用管」都不成立。
7. Remarks 仅供 FDA 内部使用、不出现在 NOA 上；需对外送达的内容须写进 DEF/INF 的 Narrative（6.2.3.3 [p.20]）——写错载体等于没送达。
8. 「决定须可辩护」跨到 6.5 仍成立：听证后改判放行须 explain the reason for the change of action（6.5.2.7 [p.40]）。

## I — 自述

这套方法把「一批货能不能进」拆成一道**有限动作集的决策门**，再给每个动作配一条可辩护的留痕要求。

第一层是门槛：系统自动筛查若已放行，本轮即结束；没放行就必须转人工。人工审查员拿到的是 PREDICT 风险分、规则标记、Priority Review flag、Import Alert / Bulletin、电子与纸质单据、数据库与历史合规记录——这些是**输入**，不是判决。手册要求先读完、先考虑，但允许审查员作出与之相反的决定；代价是必须把差异写成可核验的具体事实。

第二层是动作集，只有五支：确认全部合规且无需扣留/现场 → May Proceed（终局放行，可撤消，但系统定义明确「未作合规判定」）；请求现场工作 LEX/FEX/SAM；向 Compliance Branch 提交扣留建议（审查员不自行扣留）；他机关已在处理时走 OGI/OGC **关闭 line 且不作可采性判定**；以及误放行后的撤消。看似不合规时只剩「请求现场工作」与「建议扣留」两条路，没有第三条。

第三层是可辩护性。请求扣留、请求现场工作、与 PREDICT 相悖的放行三类决定，系统备注必须写具体理由；把放行动作名「May Proceed」或「N/A」写进备注是被点名的头号错误——动作不等于依据。合格备注的判据不是字数，而是「第三方能否据此重建判定」：品牌不在 DWPE 名单、粉剂非液剂、单据证明不含肝素，都是可核验的差异事实。

还有一条贯穿全链的前置闭环：任何影响筛查的申报数据错误，都必须更正 → 指派责任方 → 保存 → 重新筛查，然后才能作任何判定。不 rescreen 就往下走，等于把后续所有决定建在旧 flag 上。「指派责任方」是数据归属标注，用来区分 importer 与 filer 错报，不是处分程序。

最后一处最反直觉：存在一条「主动放弃判定并关闭」的合法分支。他机关已扣押时，FDA 既不出可采性判定、也不重复扣留，而是关闭 line 并留文书前提；直觉上的「两个机关各出决定」或「已扣押=不用管了」都不对。整套设计的目标是让决定在听证、复核、后续执法中站得住，而不只是让系统里多一个动作码。

## A1 — 书中用法

**情景一：带 Priority Review flag 的 line 仍拟放行，备注写到什么程度才合格（IOM 6.2.2.2 [p.16]；case c07）**
- 问题：该 line 被标为重大公共安全风险（含受 DWPE 约束产品），审查员却要签 May Proceed，备注栏填什么。
- 动作：先审阅 PREDICT 风险分与全部 flags，再逐条对应 flag 的触发条件写出差异；手册直接给出四组合格示例与三组空泛示例作对照。
- 判定/后果：「所报品牌不属 DWPE 品牌」「粉剂而非液剂」「某制造商豁免于 IA XX-XX」「单据证明不含肝素」属可核验的具体事实，合格；「Line is not subject to IA」「NA」「May Proceeded」只是结论/动作复述，不合格。空泛备注使后续审查员、Compliance Branch 与听证方无法重建判定依据，等于证据链断点。

**情景二：CBP 已以走私为由扣押同一批货并上传扣押证明，审查员该继续走扣留建议还是签 May Proceed（IOM 6.2.2.2.6 [p.19]；V2 预测题）**
- 问题：PREDICT 标高风险、他机关又已处置，两个机关是否都要出决定。
- 动作：按 6.2.2.2.6 走 OGI/OGC 的 OGA Referral，核验「他机关处置证明已上传」这一硬前提后关闭该 line。
- 判定/后果：**FDA 主动放弃可采性判定并关闭 line**。签发 May Proceed 等于 FDA 自己作出了可采性决定，与「不作判定」冲突；提交扣留建议则与已扣押状态重复、且审查员本就无权终局扣留。两者都不对。若反而要对该 line 作 May Proceed，还须因与 PREDICT 高风险相悖而在 Remarks 写出可核验的具体理由。

**情景三：IFE（Import for Export）申报缺 IUC / A of C 或支持文件（IOM 6.1.4.6.1 [p.9]、IOM 6.2.1 [p.14]、IOM 6.2.3.1 [p.19]；case c04）**
- 问题：声称「进口后加工再出口」的 entry/line，缺用途代码 IUC「Import for Export」或 IFE A of C，或支持文件不齐。
- 动作：更新 entry/line、记录更新原因、保存并 rescreen；缺支持文件按 6.2.3.1 发 DRQ 索取；索取后仍缺则请求扣留并注明「初次进口时缺 IFE 文件」。
- 判定/后果：文件（含 IUC）齐备且符合 FD&C Act §801(d)(3) 条件 → 可签发 May Proceed；缺件 → 请求扣留。同一「更正 → 记录原因 → 保存 → rescreen」闭环在 6.2.2.2.3 [p.18]（请求现场工作前）、6.2.5.3 [p.22]（DER 前）、6.2.5.4.1 [p.22]（疑似命中 IA 前）反复出现，是全章复现次数最高的操作原则。

**情景四：待审 line 排队 + 请求现场工作前的数据更正（IOM 6.2.2 [p.15-16]、IOM 6.2.2.2.3 [p.18]；case c02）**
- 问题：待审 line 多于查验能力，且发现传输数据有误又要请求 FEX/SAM，先改数据还是先设 work request。
- 动作：按 6.2.2 排优先级（紧急/易腐 > QAV > ITACS 单据 > 电子申报；卡车按实际到港时间、空/铁/海运按申报提交时间），但优先级**不豁免**文件要求（器械 shipment 仅在单据显示 CDRH 批准时才可放行，无法核实即联系 CDRH）；到 6.2.2.2.3 第 1 步先更正数据、记录原因、保存、rescreen，再设 work type 与 PAF，非例行工作在 Instruction Text 给清晰指令。
- 判定/后果：顺序反了会把工作请求建在脏数据上；「紧急/易腐」由各分部自行界定以防滥用，是裁量嵌入硬性阶梯的典型；已受 IA 约束的 line 不再例行请求现场工作（6.2.2.2.3 [p.18]），方向交 V02。

**情景五：单据审查后发现违规或无法确认合规（IOM 6.2.3.3 [p.20]）**
- 问题：按到达顺序审完 filer 单据后，下一步动作怎么选。
- 动作：发现违规证据或无法确认合规 → 向 Compliance Branch 发 DTR；若需查验/取样 → 设 work request（LEX/FEX/SAM）；单据不足则三选一跟进（直接联系 filer / DEF / INF），并在信息中写明所需具体内容与「不提供则审查照常推进」。
- 判定/后果：3 个工作日未收到单据，系统自动发 "Second and Final Request"（DR2）——它是电子消息、**不是正式 Notice of FDA Action**；DEF/INF 才生成正式 NOA，且 Narrative 会出现在公开版通知上，与内部 Remarks 是不同载体（6.2.3.3 [p.20]）。误把 DR2 当正式通知、或把理由写进 Remarks 以为已送达，都会造成程序断点。

## A2 — 未来触发 ★

**触发场景（3–5 条）**
1. 要判断某条 entry line 在电子审查阶段应发 May Proceed、请求现场工作、提交扣留建议，还是以 OGA Referral 关闭。
2. 系统给出 PREDICT 高分 / Priority Review flag / Import Alert 命中，但审查员仍拟放行，需要判断备注写到什么程度才可在听证或复核中站得住。
3. 他机关（CBP 等）已拒绝或扣押同一批货，需要判断 FDA 是否还应作出可采性判定、以及关闭 line 前要补齐什么文书。
4. 申报数据（制造商、发货人、产品代码、数量、IUC、A of C）被发现有误，需要判断更正后还必须做哪些动作才能继续判定。
5. 误发 May Proceed，需要判断能否撤消、撤消后哪些动作立即到期、条件放行期是否重开。
6. 〔推导·非原书主张〕企业侧想理解 FDA 电子审查阶段会读哪些输入、为何申报数据要自洽、为何「已提交说明」不等于「已留痕」——这是从 FDA 判定动作反推的理解，非手册主张。

**语言信号（中英双写）**
- 中文：「这条 line 该放行还是扣」「PREDICT 标了高风险还能放行吗」「备注写 N/A 行不行」「CBP 已经扣了，FDA 还要不要出决定」「改了制造商/产品代码要不要重新筛查」「May Proceed 能不能撤」「撤消后 30 天怎么算」「他机关扣押证明」「空泛备注」「决策门」
- English: "May Proceed", "entry review / entry reviewer", "PREDICT risk score", "rule flags", "Priority Review flag", "clear remarks / vague remarks", "remarks field", "contradicts PREDICT screening results", "request field work", "recommend detention to Compliance Branch", "OGA / OGI / OGC Referral", "close the line without an admissibility decision", "Ad-Hoc OGA Referral", "rescind a May Proceed", "rescreen the entry/line", "assign fault", "Notice of FDA Action", "decision gate"

**与相邻能力的区分（依 verified.md differentiator）**
- 本卡只管 **6.2 电子审查阶段的准入决策门与判定理由的可辩护性**，产物是 May Proceed / 现场工作请求 / 扣留建议 / OGA 关闭 / 撤消；不产出 483 观察项、不执行取样、不决定扣留建议走哪个 work type。
- 与 **V02（DER/DTR 分流）**：同属 6.2，但 V02 只接本卡「请求扣留」这一支的**下游**——决定向 Compliance Branch 提交哪个 work type 及提交前的核实义务；本卡在选出「建议扣留」处即交棒，不选 work type。
- 与 **CAP-18（IOM Ch.5 检查员权限与 483）**：Ch.5 是现场检查权限与 483 观察项，阶段（现场 vs 电子审查）、主体（调查员 vs 入境审查员）、产物（观察项 vs 准入动作）全不同；本卡不产出 483，也不把扣留建议当成检查观察项。
- 与 **CAP-28（IOM Ch.4 取样全流程）**：Ch.4 是取样的执行流程与证据链；本卡只「请求」现场工作/取样，不执行、不填 SCR、不拍照片。请求动作发出即本卡终点。
- 与 **CAP-17（CP 7303.050 取样量）**：取样量属现场取样计划，与 6.2 电子审查动作集无交集，不得因「请求现场工作」字样混引。
- 与 **CAP-21（CP 7303.878 FSVP 检查）**：FSVP 检查对象是进口商的记录、走 483a/T-EIR，是与货物准入并行的独立合规轨；本卡对象是 entry line 的货物准入。
- 与 **V03（事先通知硬时限）**：6.1.6.1 的 FD3/FD4 PGA flag 与 PND 码是 6.1 申报字段判定，不是 6.2 审查动作；用户问「要不要 Prior Notice / 2-4-8 小时」应路由 V03。
- 与 **V04（时间窗）/ V05（处置主链）/ V09（状态概念树）/ V10（效力层）**：本卡不算条件放行期倒计时、不展开 Detained→Refusal 链、不定义 May Proceed/Conditional Release 的状态词含义、不下法律位阶结论；只提供「决定及其理由」这一输入。

## E — 执行步骤

**E 段总览（输入 → 输出 → 交棒）**
- 输入：一条未自动放行、进入人工审查的 entry line + PREDICT 分数/flags + 电子与纸质单据 + IA/IB + 数据库与历史合规记录。
- 输出：五支动作择一 + 三类决定的具体 Remarks + 按 line 的 NOA 序列 + （如适用）rescreen 记录与撤消 24h 动作。
- 交棒：扣留建议 → V02（DER/DTR）；现场工作请求 → CAP-28 取样执行语境；条件放行期 → V04；状态词语义 → V09；位阶 → V10。
- 全程硬约束：任何影响筛查的数据更正未完成「更正 → 指派责任方 → 保存 → rescreen」四步，不得进入任何判定；备注只写进内部 Remarks，需对外送达的内容另走 Narrative。

**Step 1 — 数据完整性前置闭环（更正 → 指派责任方 → 保存 → rescreen，四步不可省、不可换序）**
依 IOM 6.2.1 [p.14]，凡发现影响 PREDICT 筛查的申报数据错误（制造商、发货人、产品代码、数量、IUC、A of C 等）：
1. **更正数据**：改正字段，并记录更正原因（6.2.2.2.3 [p.18]、6.1.4.6.1 [p.9] 均要求 record the reason for the update）。完成标准：错误字段已改且改因已留痕。
2. **指派责任方**：`Assign fault to the responsible party`——这是数据归属标注，不是处罚程序；用于区分 importer 与 filer 错报。完成标准：每个更正都对应一个已登记的责任方。
3. **保存**：Save the entry/line。完成标准：更正已写入系统，非停留在草稿或监管笔记。
4. **rescreen（重新筛查）**：Save and rescreen the entry/line after making corrections。完成标准：rescreen 已实际执行，且已复核新产生的 flags / 筛查命中是否变化。
- **判停点 A**：**未执行 rescreen 不得进入 Step 2**；不 rescreen 就判定，后续所有决定建立在旧 flag 上（6.2.5.2 [p.21] "Inaccurate data will affect PREDICT screening"）。
- **判停点 B**：rescreen 后若新增命中或 Line Details 仍有缺项，回到第 1 步重新更正；直到「无新增命中 + 字段齐备」才停。若系统自动筛查已清关该 line，按 6.2.2.2.1 [p.17] 注 **不要再人工复核 A of C 数据**，避免无谓改动引入新脏数据。

**Step 2 — 读输入（先审阅、后动作）**
- 动作：确认自动筛查是否已发 May Proceed；若未发，强制人工审查（6.2.2.2 [p.16]）。审阅并考虑 PREDICT 风险分、全部 rule flags、Priority Review flag；分析风险、核对 Import Alert / Import Bulletin 与 DWPE 适用性、检索相关中心数据库、必要时人工核实失败的数据库查询、按到达顺序审阅单据（6.2.1 [p.15]、6.2.3.3 [p.20]）。
- 完成标准：能列出「本次判定所依据的全部输入」及其出处；PREDICT 结果被记为**输入**而非结论。
- **判停点**：自动筛查已发 May Proceed → 本轮审查终止（但依 FD&C Act §304(d) 入境后仍可执法）；不得以低风险分为由跳过人工审阅，也不得把高风险分直接当违规判决。

**Step 3 — 落入五分支有限动作集（择一，不自由发挥）**
依 6.2.2.2.1 [p.17]、6.2.5 [p.21]、6.2.2.2.6 [p.19]：
1. **May Proceed**：能凭电子单据确认满足全部法规要求，且无需扣留、无需现场工作。
2. **请求现场工作**（LEX/FEX/SAM）：设正确 work type 与 PAF，非例行工作须在 Instruction Text 给清晰指令（6.2.2.2.3 [p.18]）。
3. **提交扣留建议**：向 Compliance Branch 提交，审查员不自行终局扣留。
4. **OGA Referral 关闭**（OGI/OGC）：他机关已在处理该票；**硬前提**是已取得并上传他机关处置证明（6.2.2.2.6 [p.19]）。仅共享信息、FDA 仍要作初始判定 → 用 **Ad-Hoc**，不关闭 line。
5. **撤消 May Proceed**：仅限需合规行动／误放行／新信息等罕见情形，须主管批准并立即执行（6.2.2.2.2 [p.17-18]）。
- 完成标准：五支中**恰好一支**被选中，且选中依据可回指 Step 2 的某项输入。
- **判停点**：产品看似不合规时只有「请求现场工作」与「建议扣留」两支（6.2.5 [p.21]），不得新造第三支；May Proceed 一经发出，本轮审查即终止；扣留建议提交 CB 后审查员动作终止，由 CB 作可采性终局决定；OGA 关闭以「他机关处置证明已上传」为前提，未上传不得关闭。

**Step 4 — 写可辩护理由（三类决定强制）**
- 动作：对①请求扣留、②请求现场工作、③与 PREDICT 相悖的 May Proceed（含带 Priority Review flag 的放行），在 Remarks 写出**可核验的具体差异事实**（6.2.1 [p.15]、6.2.2.2 [p.16]）。扣留建议还须把所做全部数据库检索写入 Remarks、多违规须列全 applicable alerts 与 PAF（6.2.5.2 [p.21]）。
- 完成标准：把备注交给未参与本案的第三方，能据其重建「为什么这个输入导向这个动作」；不含 "May Proceed" / "N/A" / "NA" / "Line is not subject to IA" / 结论复述。
- **判停点**：备注是**内部 FDA 使用**（6.2.1 [p.15] "remarks field is for internal FDA use only"），**不出现在 Notice of FDA Action 上**；需对外送达的内容须写进 DEF/INF 的 Narrative（6.2.3.3 [p.20]）。写错载体等于没送达。

**Step 5 — 撤消分支的立即动作（仅当 Step 3 选第 5 支）**
- 动作（6.2.2.2.2 [p.17-18] 七步）：主管批准 → 立即通知 filer 已撤消并重新作可采性判定 → 24 小时内发更新 NOA → 24 小时内请求 CBP bond hold → 确认 ABI「勿分销」码 → 已分销则请求 CBP redelivery（30 天窗口）→ 全程留痕。
- 完成标准：24 小时两项硬动作均有时间戳记录；已分销时 redelivery 请求已发出。
- **判停点**：撤消**不得用于例行或工作计划性查验**；发出 May Proceed 已使条件放行期永久结束，**撤消不重开**（6.2.2.2.2 [p.17]）。CBP 30 天窗口从放行日起算，逾期无法追货，转入 V04 / V07 / V05 的 Bond Action 语境。

**Step 6 — 文书闭环与本卡终点**
- 动作：确认系统按每个 entry line 出具 Notice of FDA Action，状态每次变化重出一份（6.1.6.2 [p.13]、6.9.57 [p.56]）；通知由 FDA 分发给 filer / importer of record / consignee。
- 完成标准：案卷中每个 line 的动作都有对应通知，且状态变更有连续通知序列；Exhibit 6-1（Notice of FDA Action 样张）为扫描件，**表单字段一律「需查原件」**，不得据蒸馏文本推断。
- **判停点**：**本卡到此为止**——不代写正式法律文书、不出合规结论、不预测个案结果；扣留建议的 work type 选型交 V02，条件放行期计算交 V04，状态词语义交 V09，法律位阶与可主张性交 V10。

**五分支动作集速查（择一，不自由发挥）**

| 分支 | 触发条件 | 完成标准 | 判停 / 交棒 |
|---|---|---|---|
| May Proceed | 电子单据确认全部合规、无需扣留/现场 | NOA 自动发 CBP 与 filer | 本轮终止；可 rescind，不排除 §304(d) 后续执法 |
| 请求现场工作 | 需查验/取样 | 正确 work type + PAF + 非例行指令 | 交 CAP-28 执行；IA 已约束时不再例行请求 |
| 提交扣留建议 | 疑似不合规且选择扣留 | 具体理由 + 全部检索留痕 + 交 CB | 交 V02 选 DER/DTR；审查员不终局扣留 |
| OGA 关闭（OGI/OGC） | 他机关已拒绝/扣押 | 处置证明已上传 | FDA 不作可采性判定；Ad-Hoc 不关闭 line |
| 撤消 May Proceed | 需合规行动/误放行/新信息 | 主管批准 + 24h 两项硬动作 | 条件放行期不重开；30 天窗口交 V04 |

**触发场景 → 卡内落点（路由自检）**

| 用户问题 | 落点 |
|---|---|
| 该放行 / 现场 / 扣留建议 / OGA 关闭 | Step 2 → Step 3 |
| 备注写什么才合格 | Step 4（R 组 2 正例/反例） |
| 改了数据还要做什么 | Step 1 四步闭环 |
| 他机关已扣押、FDA 还要不要出决定 | Step 3 第 4 支（R 组 5） |
| 误发 May Proceed 能否撤、时钟怎么算 | Step 5（R 组 6）→ V04 |
| 证书/单据齐备、DER 还是 DTR | 交 V02，本卡不选 work type |

**〔推导·非原书主张〕** 企业侧（进口商 / 境外生产商）可据上述 FDA 判定动作反推的理解：申报数据（A of C、IUC、产品代码、制造商、数量）在进入审查前须自洽，任何更正都应能回答「改了什么／为什么改／谁的责任」并预期会触发重新风险评分；对 PREDICT 命中项预先备齐可核验的可采性证据（品牌、剂型、成分检测、豁免依据），有助于缩短人工审查；提交给 filer/FDA 的说明性材料应给具体事实与证据出处，避免「符合要求」「不适用」这类无信息量表述被原样带进申报备注。**以上是从 FDA 判定动作与留痕要求反推出来的；IOM 是监管者视角的内部 SOP，不写企业侧义务，不构成原书主张，也不产生任何合规结论。**

## B — 边界

**反场景（不要用本卡）**
- 用户问的是 DER 还是 DTR、命中 Import Alert 后能不能免单据 → 路由 V02；问条件放行期还剩几天、撤消后时钟怎么算 → V04；问 May Proceed / Conditional Release / Detention 的字面含义与能否分销 → V09；问拒绝后 90 天或 Bond Action → V05；问 FSVP 记录审查或 483a → CAP-21 / V08；问 Prior Notice 时限 → V03。
- 需要出具正式法律文书、给出合规结论或预测个案结果时，本卡只提供判定口径与留痕判据，不能代写、不能下结论。
- 纯现场查验/取样执行、SCR 字段、照片标识、取样量 → CAP-28 / CAP-17；检查员权限与 483 观察项 → CAP-18。

**作者警告的失败模式（counter-example x06 / x07 / x12 / x13 / x14；principle p01 / p02 / p03）**
- 把放行动作名 "May Proceed" 或 "N/A" 写进 Remarks 当理由——手册点名的头号错误；合格备注的判据是「可核验的具体差异事实」，不是字数、不是结论复述。
- 只改数据不 rescreen，或改完不记录原因、不指派责任方 → 后续所有判定建立在旧 flag 上（x12）；把 IUC / A of C 当无所谓的元数据；误以为更正只是改字段。
- 把 PREDICT 高风险评分当「已判违规」直接扣留，或把自动放行/低分当「FDA 已判合规」；与筛查相悖的放行不写理由。
- 把 OGA Referral 当普通协查（以为 FDA 仍会出决定），或 Ad-Hoc 与关闭型混用；关闭前未上传他机关处置证明。
- 把 May Proceed 按字面读成「准许继续办理」，忽略它是终局放行、可撤消、不排除 §304(d) 后续执法；撤消后误以为条件放行期会重开。
- 把关键理由写进 Remarks 以为会送达进口商——Remarks 是内部字段、不出现在 NOA 上；把一次通知当全流程唯一文书，漏掉按 line 拆分与状态变更后的新通知。
- 把 `should`（should issue / should only rescind）一律读成「可酌情」，或读成对企业有约束力的 `shall`——见下方效力层。

**阶段 0 批判（BOOK_OVERVIEW §3，本卡 Boundary 来源）与法律位阶锚点**
- **IOM 非法规**：IOM 2026 Ch.6 是 FDA 内部操作指导（OII 机构 SOP），**不是法规，不创设企业义务，也不是可对外主张的法律依据**。真正的义务来源是 **FD&C Act §801、21 CFR Part 1（含 Prior Notice、FSVP）、19 CFR 113.62** 等法条与 CBP 法规；6.2.1 的 `must`、6.2.2.2 的 `must write a clear reason` 约束的是 **FDA 审查员的内部作业**，不产生企业的可诉权利，FDA 在个案中偏离 IOM 通常也不产生可诉权利。本卡任何结论都须回到上述法条与**当前版本 IOM / RPM** 复核。
- **should 与 as warranted 的裁量缺口**：章内密集使用 `should` / `as warranted` / `where appropriate` / `if the facts warrant`，却几乎不给判据——「请求扣留 vs 请求现场工作」的选择标准、Priority Review 下放行理由的充分程度、PREDICT 规则出错的处置，都留给分部惯例。同一句可硬软并存（6.2.2.2.2 [p.17] "should only rescind … You **must** act immediately"）。本卡**不补写判据**，只把裁量缺口标为复核锚点，不把 `should` 升格为规则。
- **2026 版快照**：PREDICT、ITACS、ACE、OASIS、SERIO、eNSpect、ER Job Aid、SOP 编号会随改版失效；本卡的 work type 名（OGI/OGC、LEX/FEX/SAM、DRQ/DEF/INF）与系统界面口径是 2026 版快照，不是稳定规则。
- **监管者视角与组织前提**：全篇写「FDA 如何作出并执行决定」，默认使用者有 FDA 授权、系统权限、Division / Compliance Branch / OCI / CBP 协作通道；企业不具这些前提，照搬会把「检查清单」误当「合规义务清单」。本卡不写进口商/境外生产商如何举证或避免被扣（凡涉及一律见 E 段〔推导·非原书主张〕）。
- **系统绑定与跨章引用**：6.2 的细则大量靠 IOM 4.x（取样）、5.x（证据/报告）、RPM Chapter 9（放行/听证/拒绝/保证金）、CPGM 与 PREDICT Guide 承载；单读第 6 章会得到「有骨架、缺细则」的闭环幻觉。
- **不谈相对方权利与救济成本**：手册不提供进口商在听证中的举证成本、滞期与保证金风险权衡。
- **Exhibit 6-1~6-4 为扫描件、无文本层**（Notice of FDA Action / Form FDA 766 / Form FDA 790 / Form FDA 463a）；本卡涉及的 NOA 与任何表单**字段一律标「需查原件」**，不得据蒸馏文本推断字段内容。
- **页码归属复核提示**：6.2.1 节标题在 [p.14]，而「Document Your Decisions / Avoid vague remarks」段落落在 [p.15]；verified.md V01 将该段统一标为 [p.14]。本卡按原文分块逐段标注 [p.14] / [p.15]，主流程统一页码时须回原文确认。

**复核锚点清单（交主流程 / 阶段 1.6 晋级门）**
- **页码与条文号**：6.2.1 节标题在 [p.14]、备注段落（Provide clear remarks / Avoid vague remarks）在 [p.15]，verified.md V01 统一标为 [p.14]；主流程统一页码时须回 `.cangjie/index/6.2-Entry-Review.txt` 与 `source/iom-ch6-full.txt` 的 `[PAGE 15]` 标记确认。
- **法条**：任何义务/权利结论回 FD&C Act §801、21 CFR Part 1、19 CFR 113.62 与当前版本 IOM / RPM 复核；本卡不据 IOM 单独下义务。
- **系统编号**：PREDICT、ITACS、ACE、OASIS、SERIO、ER Job Aid、work type 名（OGI/OGC、LEX/FEX/SAM、DRQ/DEF/INF）为 2026 版快照。
- **裁量缺口**：`should`（should issue / should only rescind）/ `as warranted` / `where appropriate` 的判据留给分部惯例，本卡不补写。
- **表单**：Exhibit 6-1~6-4 为扫描件，NOA 及任何表单字段「需查原件」。
- **共享字样**：V09 复用 May Proceed / Conditional Release 作状态词、V02 复用「扣留」作 work type、V04 复用 30 天作时间窗——三处均须按 differentiator 分流，不得互相替代。
- **企业侧**：E 段与 A2 触发场景第 6 条的〔推导·非原书主张〕内容是从 FDA 判定动作反推，非原书主张；阶段 4 负例设计不得据此生成「企业合规义务清单」。

**相邻混淆**
- 与 V02 共享「扣留」字样但层次不同：本卡选「是否建议扣留」，V02 选「建议用 DER 还是 DTR」；审查员提交的是 recommendation，不是终局扣留决定。
- 与 CAP-18 的 483、V08 的 483a：三者是不同章节、不同阶段的文书（Ch.5 观察项 / FSVP 观察项 / 6.2 准入动作），正对应「二十八类不可混引」。
- 与 V09 共享 May Proceed / Conditional Release 术语：本卡用它们作**动作**，V09 用它们作**状态词口径**，不互相替代。
- 「May Proceed 字面 ≠ 终局放行」「DWPE 字面 ≠ 免检」「Conditional Release 字面 ≠ 已合格」是一组同向误读（都高估自身合规状态），见 x14 与 V09；本卡只处理第一项在决策门中的后果。
