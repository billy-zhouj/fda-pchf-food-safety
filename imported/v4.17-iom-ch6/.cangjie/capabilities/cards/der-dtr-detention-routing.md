# DER/DTR 按触发依据分流与 DWPE「不检查就扣住」（der-dtr-detention-routing）

*来源分层与定位：IOM 2026 Ch.6 是 FDA 内部操作指导（Investigations Operations Manual，OII 机构 SOP），不是法规，不创设企业义务；与 IOM Ch.4（取样全流程）、IOM Ch.5（检查员权限与 483）、CP 7303.878（FSVP 检查）、CP 7303.050（取样量）分层，不得混引。本卡只落在 IOM 6.2.5（审查员向 Compliance Branch 提交扣留建议的分流与提交前核实义务）、6.2.2.2.3（IA 命中后不请求现场工作）、6.3.10.5（现场查验 Class 3 的同构分流）与 6.9.20 / 6.9.22 / 6.9.6（DTR / DWPE / Audit Sample 术语与证据门槛）。本卡**唯一的产物是 work type（DER 或 DTR）及其提交前的核实与留痕**，不管决策门选哪个动作（V01）、不定义状态词（V09）、不产出 483 观察项（CAP-18）、不执行取样（CAP-28）。Import Alert / DWPE 判定直接决定货物是否免查验即扣，是全章预测力最强的分流点。*

## R — 原文

> "As an entry reviewer, you will use one of two work types to recommend detention: DER or DTR. DER (Detention without Physical Examination): Use DER when a product is subject to Detention without Physical Examination (DWPE). DTR (All Other Detentions): Use DTR for all other situations where a product appears to be violative." / "Before sending the detention request to the Compliance Branch (CB), you must: Gather all necessary documents to support your case. Add clear comments explaining the reason for detention for each line. Include photos when needed to support the violation."
> —— IOM 6.2.5.1 [p.21]
> 中文自译：审查员向 Compliance Branch 建议扣留时用两种 work type 之一：DER（免实物查验扣留）用于产品**受 DWPE 约束**时；DTR（其他一切扣留）用于其余一切「产品看似违规」的情形。提交 CB 之前必须：收齐支持案卷的全部单据、逐 line 写清扣留理由、必要时附照片支持违规认定。注意原文用的是 recommend / request（建议/请求），审查员不作终局扣留。

> "Use a DER when an entry is subject to DWPE. You can submit a DER to the Compliance Branch (CB) without requesting entry documents if all the following are true: The electronic data matches the Import Alert criteria (e.g., country, manufacturer, product). The Import Alert does not require specific documents. You do not need any additional information." / "You must request and review documents before submitting a DER if the Import Alert requires specific paperwork for a product to be released."
> —— IOM 6.2.5.3 [p.21]
> "For example, IA 28-02 requires a certificate for all shipments of black pepper from India. If the certificate is missing, you must request it before recommending detention." / "1. Confirm that all the electronic information (country, firm name, product description) matches the criteria in the Import Alert. Update and rescreen the entry if you make corrections. 2. In the 'Instruction Text' field, explain why you are recommending detention... 3. Submit to the Compliance Branch (CB)."
> —— IOM 6.2.5.3 [p.22]
> 中文自译：受 DWPE 约束时用 DER。**免索单据直接提交**只在三条件同时成立时允许：电子数据与 IA 标准（国家、制造商、产品）匹配、该 IA 不要求特定文书、无需额外信息。若 IA 要求特定放行文件，则必须先索取并审阅——例：IA 28-02 要求所有印度黑胡椒货随附证书，缺证书须先索取再建议扣留。提交三步为：确认电子信息匹配 IA 并在更正时 rescreen、在 Instruction Text 说明扣留理由、提交 CB。

> "You must make a reasonable effort to verify compliance using the information provided. Do not recommend detention based solely on a failed data lookup or missing Affirmation of Compliance data." / "Add comments in the 'Instruction Text' field detailing the databases you reviewed and the information that did not match."
> —— IOM 6.2.5.5 [p.23]
> "Used when review of the entry information cannot confirm that products being offered for import meet FDA's admissibility criteria. Examples include products in which the required registration, scheduled process filing, 510(k), or pre-market approval (PMA) cannot be verified at the entry review step."
> —— IOM 6.9.20 [p.52]
> 中文自译：必须用手上信息作**合理努力**核实合规；**不得仅凭数据库查询失败或 A of C 数据缺失就建议扣留**，并须在 Instruction Text 写明检索过哪些数据库、哪些信息不匹配。术语表把「注册、scheduled process filing、510(k)、PMA 在审查阶段无法核实」明确列为 DTR 的示例——即「查不到」归入 DTR 语境，而不是违规结论本身。（6.2.5.5 条文号属 6.2，但物理落在 [p.23] 的 6.3 分块开头，检索时勿按分块漏掉。）

> "Important: You must document all the research you conduct in the detention recommendation's 'Remarks' section." / "Note: All information in 'Line Details' must be accurate. Inaccurate data will affect PREDICT screening." / "If a product has multiple violations (for example, it is subject to more than one Import Alert), you must include all applicable alerts and problem area flags (PAFs) in your detention recommendation."
> —— IOM 6.2.5.2 [p.21]
> "When you select the detention option (DER or DTR), choose an 'Entry Option' from the drop-down menu that also requests documents. For example, select 'Hold Designated, Others Go, Docs Required.' This automatically tells the filer to submit the needed paperwork."
> —— IOM 6.2.5.2.1 [p.21]
> 中文自译：扣留建议的 Remarks 必须记录所做的**全部**检索；Line Details 全部信息必须准确，脏数据会影响 PREDICT 筛查；产品有多个违规（如命中多个 Import Alert）时，须把**全部** applicable alerts 与 PAF 一并列入。选择扣留选项时还要从下拉菜单挑一个同时索取单据的 Entry Option（如 "Hold Designated, Others Go, Docs Required"），自动通知 filer 补件。

> "Import Alerts (IA): Do not routinely request work for a line that is already subject to an Import Alert."
> —— IOM 6.2.2.2.3 [p.18]
> "Use a DTR when you cannot confirm that a product meets the FDA's admissibility requirements. To make this decision, first review all available information, including: The electronic submission / Internal FDA databases / Any documents submitted by the filer." / "If the entry line does not match the IA listing: Continue your initial admissibility review. Using the feedback functionality in SERIO Entry Review, explain why it was not subject to the IA. For example: 'Flagged for IA XX-XX, but manufacturer not listed on IA'."
> —— IOM 6.2.5.4 [p.22]、IOM 6.2.5.4.1 [p.22]
> 中文自译：对已受 Import Alert 约束的 line，**不要例行请求现场工作**——方向是「别再查、走 DER」。DTR 用于无法确认产品满足可采性要求的情形，须先审阅电子申报、内部数据库与 filer 单据。疑似命中 IA 但信息不足时先取单据、更正数据并 rescreen；确认**不命中** IA 名单时，继续初始可采性审查，还要用系统 feedback 功能写明为何不受该 IA 约束（例：「已被 IA XX-XX 标记，但制造商未列入该 IA」）。

> "An action directed against specific products manufactured or shipped by specific foreign firms. 'Import Alerts' list products that may be detained without physical examination due to their violative history or potential."
> —— IOM 6.9.22 [p.52]
> "At least one FDA audit sample should be included as evidence when processing removal of a product, shipper, or country from DWPE."
> —— IOM 6.9.6 [p.51]
> "NOTE: If a FEX/LEX is conducted and the examination identifies a violation, you should record the findings as a Class 3 FEX/LEX and submit to compliance as a DTR with the appropriate PAF."
> —— IOM 6.3.10.5 [p.31]
> 中文自译：DWPE 是针对特定境外厂商生产/发运的特定产品采取的行动；Import Alerts 列出因**违规史或违规可能性**而可**不经实物查验即予扣留**的产品。把产品/发货人/国家从 DWPE 名单移除，至少须有一份 **FDA 自采 audit sample** 作为证据。现场查验中 FEX/LEX 发现违规时，记录为 Class 3 并以 **DTR + 相应 PAF** 提交 compliance——同一「按触发依据分流」思想从 6.2 电子审查延伸到 6.3 现场查验，但对象与结论不同。

**引文覆盖对照（verified.md V02 `source_evidence` 关键口径 → R 组）**

| source_evidence 关键口径 | 落点 |
|---|---|
| 6.2.5.1 [p.21] Use DER when a product is subject to DWPE / Use DTR for all other situations | 组 1 |
| 6.2.5.3 [p.21-22] DER 免单据三条件、IA 28-02 印度黑胡椒须先索证书、提交 3 步 | 组 2 |
| 6.2.5.5 [p.23] reasonable effort / 不得仅凭 failed data lookup 或 missing A of C 建议扣留 | 组 3 |
| 6.2.5.2 [p.21] 多违规须列全 alerts 与 PAF、全部研究写入 Remarks | 组 4 |
| 6.3.10.5 [p.31] Class 3 FEX/LEX 发现违规 → 记录并提交 DTR + 相应 PAF | 组 6 |
| 6.9.22 [p.52] / 6.9.6 [p.51] DWPE 凭违规史免查验扣留、移除须至少一份 FDA audit sample | 组 6 |
| 6.2.2.2.x [p.17] Import Alerts: 不要对已受 IA 约束的 line 例行请求现场工作 | 组 5（原文核对为 IOM 6.2.2.2.3 [p.18]） |
| V1 跨域佐证：6.6.4.3 [p.44] / 6.2.2.2 [p.16] DWPE 是 Priority Review 加重信号；6.9.20 [p.52] DTR 示例 | I 段 / B 段 |

**本卡反直觉口径清单（V3 机构特定校准，非聪明人常识）**
1. DER/DTR 是**按触发依据**分流，不是按严重程度分级——直觉上极易当成轻重档。
2. DWPE = 「不检查就扣住」（凭历史/Import Alert 免实物查验即扣），字面「不检查」极易被读成「不检查就放过」。
3. 「查不到 ≠ 违规」：数据库查询失败、A of C 缺失只是核实起点，直接建议扣留被明文禁止。
4. Import Alert 与 Import Bulletin 方向几乎相反：Alert → 别再请求现场工作、走 DER；Bulletin → 指示去请求现场工作、不触发 DWPE。
5. 审查员提交的是 recommendation / request，不是终局扣留决定，须交 Compliance Branch。
6. 解除 DWPE 的证据门槛是「至少一份 FDA 自采 audit sample」，企业私人实验室合格报告无效。
7. 不命中 IA 也要用 feedback 写明为何不适用——「不命中」不是「什么都不写」。
8. DER 的「免索单据」是条件式例外：三条件全满足才免；IA 要求证书时缺证必须先索，直接提交会在听证被击穿。
9. 6.9 术语表**完全没有 DER 条目**，只看术语表会以为只有一种扣留建议；DTR 在 6.9.20 / 6.2.3.3 / 6.2.5 标题中有三种称法。

## I — 自述

这套方法只回答一个问题：审查员决定「建议扣留」之后，该往 Compliance Branch 递哪一种 work type。答案不是看违规多严重，而是看**触发依据**——受 DWPE / Import Alert 约束走 DER，其余一切「无法确认可采性」走 DTR。把 DER 当成「更严重的快档」是外行最容易犯的错，它与严重程度无关。

第二处反转是 DWPE 的字面。Detention Without Physical Examination 里的「不检查」修饰的是**扣留**：凭违规史或 Import Alert 列名，不取样、不查验就扣住。它绝不是「不检查就放过」。随之而来的是 Import Alert 与 Import Bulletin 方向几乎相反：Alert 命中后「不要例行请求现场工作」，直接走 DER；Bulletin 反而是指示审查员去请求现场工作的文件，且不触发 DWPE。

第三处反转是「查不到 ≠ 违规」。数据库查不到注册、列名、510(k)、PMA，或 filer 的 A of C 缺失，都只是**核实的起点**，不是违规结论。手册明文禁止仅凭 failed data lookup 或 missing A of C 就建议扣留；审查员须先用手上信息作 reasonable effort——电子申报、内部数据库、filer 单据，必要时索取单据或请求 FEX/SAM——并在 Instruction Text 写明查过哪些库、什么不匹配。核实后确需扣留，触发依据也仍是「无法确认可采性」，应走 DTR（6.9.20 正是以注册、scheduled process filing、510(k)、PMA 无法核实为 DTR 示例）。

DER 的「免索单据」是条件式例外：电子数据匹配 IA 标准、IA 不要求特定文书、无需额外信息，三者全满足才可免；一旦 IA 要求证书（如 IA 28-02 印度黑胡椒），缺证须先索取再建议扣留。命中多个 IA 时，扣留建议须把全部 alerts 与 PAF 列全，全部检索写进 Remarks；不命中 IA 也要用 feedback 写明为何不适用。

还有一层证据门槛常被误读：解除 DWPE 至少须一份 **FDA 自采 audit sample**，企业自行送检的私人实验室合格报告不构成移除证据。全程产物只是 recommendation / request，须交 Compliance Branch；审查员不自行作终局扣留决定。这套分流从 6.2 电子审查延伸到 6.3 现场查验（Class 3 FEX/LEX 发现违规 → DTR + PAF），但对象与结论各不相同。

## A1 — 书中用法

**情景一：IA 28-02 印度黑胡椒缺证书（IOM 6.2.5.3 [p.21-22]；case c06）**
- 问题：某 line 命中要求随附证书的 Import Alert，电子数据匹配 IA 标准，但证书缺失；审查员能否走 DER 免单据快速提交。
- 动作：判定触发依据为「受 DWPE/IA 约束」→ DER；但因该 IA **要求特定放行文书**，按 6.2.5.3 [p.21] 必须先索取并审阅证书，不得免单据。
- 判定/后果：证书缺失即先索取，再建议扣留；直接免单据提交会留下案卷证据缺口，听证中易被击穿。提交时还须确认国家/厂商/品名匹配 IA、在 Instruction Text 写明理由（如 "Manufacturer is subject to IA XX-XX"）、并交 Compliance Branch。

**情景二：数据库查不到 510(k) 与注册、A of C 缺失，审查员想直接扣留并走 DER（IOM 6.2.5.5 [p.23]、IOM 6.9.20 [p.52]；V2 预测题）**
- 问题：「查无记录」能不能当违规证据，DER 能不能当更严重的快通道。
- 动作：两步都纠偏。① 按 6.2.5.5 先作 reasonable effort 核实（电子申报 + 内部数据库 + filer 单据，必要时请求 DRQ/FEX/SAM），并在 Instruction Text 记录检索过的库与不匹配项；② 核实后确需扣留，触发依据是「无法确认可采性」而非「受 DWPE 约束」，应走 **DTR**。
- 判定/后果：**不得仅凭 failed data lookup 或 missing A of C 建议扣留**（明文禁止），直接扣留与走 DER 均错。若检索后确认不匹配任何 IA，还须用系统 feedback 写明为何该 IA 不适用，并把全部研究写进 Remarks。查不到只是核实起点，不是结论。

**情景三：疑似命中 IA 但信息不足 / 确认不命中（IOM 6.2.5.4 [p.22]、IOM 6.2.5.4.1 [p.22]）**
- 问题：line 看起来像 IA 名单上的货，但缺信息确认；或核对后发现其实不命中。
- 动作：先请求并审阅 entry 单据，发现电子数据有误则更正并 rescreen；命中 IA 名单（红/绿/黄）则按该 IA 的 guidance 办理；不命中则继续初始可采性审查，并用 SERIO feedback 写明不适用理由。
- 判定/后果：不命中不等于「什么都不写」——「Flagged for IA XX-XX, but manufacturer not listed on IA」这类具体说明是硬要求；全部研究写入 Remarks。与 6.2.2.2.3 [p.18]「不要对已受 IA 约束的 line 例行请求现场工作」合起来，构成 Alert 命中后的方向判据。

**佐证：现场查验 Class 3 的同构分流（IOM 6.3.10.5 [p.31]）**
- 问题：FEX/LEX 实际查出违规时，是否另走一套 work type。
- 动作：记录为 Class 3 FEX/LEX，以 **DTR + 相应 PAF** 提交 compliance。
- 判定/后果：分流规则不因阶段改变——DWPE 触发 DER，其余违规（含现场发现）归 DTR；但对象从「电子审查 line」变成「已完成物理查验的 line」，结论也不构成新的放行/扣留决定。

**情景四：与既往违规 entry 同产品同制造商、但尚未正式列入 DWPE（IOM 6.2.5.4.2 [p.22]）**
- 问题：该票能否因「看起来像 DWPE」直接走 DER。
- 动作：先看 OII 是否具 direct reference authority（DIO Advisory #1）且电子申报与既往违规 entry **完全一致**；是 → 建议 DER，并在 Instruction Text 记既往发现、CMS/work activity 号或 entry 号、IA 引用与所收集证据；否 → entry 独立成立，与主管及 CB 商议走单据或现场工作（SAM/FEX/LEX）。
- 判定/后果：不能因「像 DWPE」就套 DER；无授权时该票不自动继承既往违规结论，分流依据仍要逐票成立。CO 可另设筛查标准提示审查员注意既往违规发现（6.2.5.4.2 [p.22] 注）。

**情景五：企业列在 DWPE 名单并提交私人实验室合格报告申请移除（IOM 6.9.6 [p.51]、IOM 6.9.22 [p.52]）**
- 问题：企业自行送检的合格报告是否足以解除 DWPE。
- 动作：核对移除证据是否含**至少一份 FDA 自采 audit sample**——该样品用于验证 COA 或私人实验室分析所声称的合规结论，通常与一份 import sample 并用。
- 判定/后果：私人实验室报告**不构成**移除证据，DWPE 移除申请不成立。反向也要防：把 ADS（同批补样/加测）误当 audit sample 同样证据类型不符，案卷会被退回；把企业送检合格理解为「自动解除」是本卡第二处高估自身合规状态的误读。

## A2 — 未来触发 ★

**触发场景（3–5 条）**
1. 某条疑似违规的 line 要提交扣留建议，需要判断用 DER 还是 DTR。
2. 命中 Import Alert / DWPE，需要判断可否免索单据直接 DER、或何时必须先索取证书（如 IA 28-02 类要求）。
3. 数据库查不到注册 / 列名 / 510(k) / PMA，或 A of C 缺失，需要判断能否直接建议扣留、以及该走哪个 work type。
4. 企业自行送检合格报告，或被列入 DWPE 后想申请移除，需要判断证据门槛。
5. 需要区分 Import Alert（别再请求现场工作、走 DER）与 Import Bulletin（指示去请求现场工作、不触发 DWPE），或判断命中多个 IA 时扣留建议要列哪些内容。
6. 现场查验 Class 3 FEX/LEX 发现违规，需要确认提交 compliance 的 work type 与 PAF。

**语言信号（中英双写）**
- 中文：「这条该走 DER 还是 DTR」「命中进口警报了能不能直接扣」「查不到 510(k)/注册能不能扣」「A of C 缺失」「DWPE 是不是不用检查就放过」「免实物查验扣留」「我们送检合格了能不能解除警报」「Import Alert 和 Import Bulletin 区别」「多个警报要列几个」「不命中也要写理由吗」「提交给 Compliance Branch」
- English: "DER vs DTR", "Detention without Physical Examination (DWPE)", "Import Alert (IA)", "Import Bulletin (IB)", "detention recommendation / request", "Compliance Branch (CB)", "reasonable effort to verify compliance", "failed data lookup", "missing Affirmation of Compliance (A of C)", "IA 28-02 / black pepper certificate", "audit sample", "removal from DWPE", "private laboratory", "PAF / problem area flag", "feedback functionality", "Do not routinely request work", "Hold Designated, Others Go, Docs Required"

**与相邻能力的区分（依 verified.md differentiator）**
- 本卡只输出**向 Compliance Branch 提交的 work type（DER 或 DTR）及其提交前核实义务**，不管决策门选哪个动作、不管状态词定义、不产出 483 观察项、不执行取样。
- 与 **V01（决策门）**：同属 6.2，V01 是上游——先决定「是否建议扣留」；本卡只接 V01「请求扣留」这一支的下游分流。V01 在选出该动作处交棒，本卡不选放行/现场工作/OGA 关闭。
- 与 **V09（进口状态概念区分树）**：DWPE / Detention / Conditional Release 的**术语口径**归 V09；本卡只在「触发依据」意义上使用 DWPE，不定义状态词、不回答「能不能分销」。
- 与 **CAP-18（IOM Ch.5 检查员权限与 483）**：483 是 Ch.5 现场检查观察项，与 6.2 扣留建议是**不同章节、不同文书序列**；本卡不产出 483，也不把扣留建议当成检查观察项。
- 与 **CAP-28（IOM Ch.4 取样全流程）**：Ch.4 是取样执行与证据链；本卡「必要时请求 FEX/SAM」只是核实手段的指向，不执行取样、不填 SCR、不拍照片。
- 与 **CAP-17（CP 7303.050 取样量）**：取样量属现场取样计划，与 6.2 扣留建议分流无交集，不得混引。
- 与 **CAP-21（CP 7303.878 FSVP 检查）**：FSVP 检查对象是进口商记录、走 483a/T-EIR，是与货物准入并行的独立合规轨；本卡对象是 entry line 的扣留建议。
- 与包内既有【Import Alert / 进口警报】相关 CAP（若存在）：本卡只答「警报命中后**提交哪个 work type 及提交前核实什么**」，不展开警报内容、列名规则或企业侧整改方案。
- 与 **V10（效力层元规则）**：`You can submit a DER … if all the following are true`、`may recommend detention` 属机构裁量，是否可对企业主张为权利/义务由 V10 判定，本卡不下位阶结论。

## E — 执行步骤

**E 段总览（输入 → 输出 → 交棒）**
- 输入：一条已由 V01 决策门选出「建议扣留」的 entry line + 电子申报 + 内部数据库结果 + filer 单据 + Import Alert/Bulletin 命中情况 + 既往违规历史。
- 输出：一个 work type（DER 或 DTR）+ 提交前的核实记录（数据库清单、不匹配项、feedback 理由）+ 全部 alerts/PAF + 全部研究写入的 Remarks + rescreen 记录。
- 交棒：提交 Compliance Branch 即本卡动作终止；CB 的终局可采性决定、Detained→听证→拒绝链交 V05；状态词语义交 V09；位阶交 V10。
- 全程硬约束：先判触发依据、再作合理努力核实，二者顺序不可倒；任何「查不到」不得直接作为扣留依据；`may recommend detention` 属机构裁量，不升格为企业权利或绝对规则。

**Step 1 — 判触发依据（第一问，不看严重度）**
- 动作：问「触发本条扣留建议的依据是不是受 DWPE / Import Alert 约束」。受约束 → DER；其余一切「产品看似违规 / 无法确认可采性」→ DTR（6.2.5.1 [p.21]）。
- 完成标准：能用一句话写出「触发依据 = ___，故 work type = DER / DTR」，且理由中不含「情节严重」「风险更高」这类严重度措辞。
- **判停点**：**不得按严重程度分档**。DER 不是「更重的快通道」，DTR 不是「较轻档」；若发现自己在按严重度选，立即回到本步重判。已受 IA 约束的 line 按 6.2.2.2.3 [p.18] 不再例行请求现场工作。

**Step 2 — 合理努力核实（查不到 ≠ 违规，先于任何提交）**
- 动作：用手上信息核实合规——电子申报、内部 FDA 数据库、filer 提交单据；必要时索取单据（DRQ / Entry Option "Docs Required"）或请求 FEX/SAM。在 Instruction Text 写明检索过哪些数据库、哪些信息不匹配（6.2.5.5 [p.23]、6.2.5.4 [p.22]）。
- 完成标准：能列出「已查渠道清单 + 不匹配项 + 是否仍无法确认可采性」；检索记录已写入案卷。
- **判停点**：**不得仅凭 failed data lookup 或 missing A of C 建议扣留**（6.2.5.5 [p.23] 明文禁止）。核实未穷尽、或只是「数据库没记录」而无其他核实动作 → 停在本步，不得进入 Step 3/4。同时注意反向禁则：系统自动筛查已清关的 line 不要再人工复核 A of C（6.2.2.2.1 [p.17]）。

**Step 3 — DER 分支（受 DWPE/IA 约束时）**
- 动作：
  1. 核免单据三条件：电子数据匹配 IA 标准（国家/制造商/产品）、该 IA 不要求特定文书、无需额外信息（6.2.5.3 [p.21]）。三条件全满足才可免索单据；任一不满足（尤其 IA 要求证书，如 IA 28-02 印度黑胡椒）→ **必须先索取并审阅单据**再提交。
  2. 确认电子信息匹配 IA；若作过更正，先 **更新并 rescreen**（6.2.5.3 [p.22]）。
  3. 在 Instruction Text 写明扣留理由（如 "Manufacturer is subject to IA XX-XX"）与所做数据库检索；命中多个 IA 时列全 **all applicable alerts 与 PAFs**，并把全部研究写入 Remarks（6.2.5.2 [p.21]）。
  4. Submit to Compliance Branch。
- 完成标准：DER 案卷含「IA 匹配结论 + 单据处置结论 + 全部 alerts/PAF + 全部检索留痕 + rescreen 记录」。
- **判停点**：IA 要求特定文书而证书缺失 → 停在索单据，不得提交 DER；审查员**不作终局扣留决定**，提交 CB 即本卡动作终止。Pending Addition to DWPE 仅在 OII 具 direct reference authority 且电子申报与既往违规 entry 完全一致时走 DER，否则 entry 独立成立、与主管及 CB 商议走单据或现场工作（6.2.5.4.2 [p.22]）。

**Step 4 — DTR 分支（其余一切疑似违规）**
- 动作：先审阅全部可用信息（电子申报、内部数据库、filer 单据，6.2.5.4 [p.22]）；仍不足可请求 FEX/SAM；疑似命中 IA 但不确定时先索取单据、更正数据并 rescreen，再按 IA guidance 办理；**确认不命中 IA 时，用 SERIO feedback 写明为何不适用**（6.2.5.4.1 [p.22]），并把全部研究写入 Remarks。
- 完成标准：案卷能回答「为何无法确认可采性」且「不命中 IA 的理由」已留痕；Line Details 字段准确（6.2.5.2 [p.21]）。
- **判停点**：不命中 IA 不等于「什么都不写」——缺 feedback 说明视为未完成本分支。现场查验 Class 3 FEX/LEX 发现违规时同样以 **DTR + 相应 PAF** 提交 compliance（6.3.10.5 [p.31]），不另起一套 work type。

**Step 5 — 证据门槛与本卡终点（DWPE 解除语境）**
- 动作：若问题转向「如何把产品/发货人/国家从 DWPE 移除」，核验证据是否含**至少一份 FDA 自采 audit sample**（6.9.6 [p.51]、6.9.22 [p.52]）。
- 完成标准：能明确写出「移除证据 = FDA audit sample」，并识别企业私人实验室报告**不构成**移除证据。
- **判停点**：**本卡到此为止**——不代写正式法律文书、不出合规结论、不预测个案结果；不判定产品是否可采（V01）、不定义 DWPE/Detention 状态词（V09）、不产出 483 观察项（CAP-18）、不执行取样（CAP-28）、不下法律位阶结论（V10）。Exhibit 6-1~6-4 为扫描件，涉及任何表单字段一律「需查原件」。

**work type 选型速查（只按触发依据，不按严重度）**

| 触发依据 | work type | 关键前置 | 原文锚点 |
|---|---|---|---|
| 受 DWPE / Import Alert 约束 | **DER** | 电子数据匹配 IA；IA 要求证书时先索单据；多 IA 列全 alerts/PAF | IOM 6.2.5.1 [p.21]、IOM 6.2.5.3 [p.21-22] |
| 无法确认可采性（注册/列名/510(k)/PMA、A of C 缺失等） | **DTR** | 先 reasonable effort 核实；不命中 IA 须 feedback 写理由 | IOM 6.2.5.5 [p.23]、IOM 6.9.20 [p.52]、IOM 6.2.5.4.1 [p.22] |
| 现场查验 Class 3 FEX/LEX 发现违规 | **DTR + PAF** | 记录为 Class 3，交 compliance | IOM 6.3.10.5 [p.31] |
| 命中 Import Alert 后需更多工作 | **不要再例行请求现场工作** | 走 DER 分流，不叠加现场工作 | IOM 6.2.2.2.3 [p.18] |
| Import Bulletin 指示 | **请求现场工作** | 不触发 DWPE | IOM 6.2.2.2.3 [p.18] |
| 同产品同制造商、既往违规 entry 待列入 DWPE | 有 direct reference authority → DER；无 → entry 独立成立 | 与主管/CB 商议走单据或现场工作 | IOM 6.2.5.4.2 [p.22] |

**提交前清单（DER / DTR 通用，缺项不得提交）**
- [ ] 已判触发依据并写出一句话理由（不含严重度措辞）
- [ ] 已作 reasonable effort 核实，Instruction Text 写明查过哪些库、哪些信息不匹配
- [ ] 影响筛查的数据已更正 → 记录原因 → 保存 → rescreen
- [ ] 全部数据库检索已写入 Remarks；多违规已列全 applicable alerts 与 PAF
- [ ] 不命中 IA 已用 feedback 写明不适用理由
- [ ] 逐 line 写明扣留理由；需要时附照片与单据
- [ ] 选择同时索取单据的 Entry Option（如 "Hold Designated, Others Go, Docs Required"）
- [ ] 明确产物是 recommendation / request，交 Compliance Branch，不作终局扣留

**〔推导·非原书主张〕** 企业侧（进口商 / 境外生产商）可据上述 FDA 判定动作反推的理解：被列入 Import Alert / DWPE 时，举证重点是「本批与警报标准的**差异证据**」（品牌、剂型、制造商豁免、成分检测），正对应 6.2.2.2 [p.16] 的 Clear Remarks 示例；未被列入但注册/列名/510(k)/PMA 无法核实时，应预置 NDA、510(k)、PMA、注册列名等可核验证明，因为「查不到」会触发对方的核实义务而非直接违规结论；企业自行送检的私人实验室合格报告不构成 DWPE 移除证据。**以上是从 FDA 分流与核实动作反推出来的；IOM 是监管者视角的内部 SOP，不写企业侧义务，不构成原书主张，也不产生任何合规结论。**

## B — 边界

**反场景（不要用本卡）**
- 用户问的是「这条 line 该放行 / 现场工作 / 扣留建议 / OGA 关闭」→ 路由 V01；问 DWPE / Detention / Conditional Release 的字面含义或能否分销 → V09；问条件放行期、30 天窗口 → V04；问拒绝后 90 天处置链 → V05；问 FSVP 记录审查 → CAP-21 / V08。
- 需要出具正式法律文书、给出合规结论或预测个案结果时，本卡只提供分流口径与核实判据，不能代写、不能下结论。
- 纯取样执行、SCR 字段、取样量 → CAP-28 / CAP-17；现场检查观察项 483 → CAP-18。

**作者警告的失败模式（counter-example x02 / x13 / x14；principle p13；case c06；glossary g06 / g07 / g16 / g17）**
- 把 DER/DTR 按**严重程度**分档——本卡最核心的反直觉：分流依据是「是否列名 Import Alert / 受 DWPE 约束」，与严重度无关。
- 把 DWPE 的「不检查」读成「不检查就放过」——实为「不检查就扣住」；命中 Import Alert 后反而降低查验优先级、或仍去例行请求现场工作（6.2.2.2.3 [p.18] 明确禁止）。
- 把「查不到注册/510(k)/PMA」或「A of C 缺失」当违规证据，直接建议扣留——6.2.5.5 [p.23] 明文禁止；或把 DER 当「查无记录」的快速通道（应走 DTR）。
- 把 Import Alert 与 Import Bulletin 混为一谈：Alert → 别再查、走 DER；Bulletin → 指示去请求现场工作、不触发 DWPE，方向几乎相反。
- DER 免单据三条件未逐项核对就提交；IA 要求证书（IA 28-02）时缺证仍直接提交，案卷证据不全、听证被击穿。
- 命中多个 IA 只列一个 alert / 漏列 PAF；全部数据库检索未写进 Remarks；不命中 IA 时漏写 feedback 理由；更正数据后忘记 rescreen。
- 把企业私人实验室合格报告当 DWPE 移除证据（门槛是至少一份 FDA audit sample）；把审查员提交的 recommendation 当成终局扣留决定、绕过 Compliance Branch。
- 把 `you can submit … if all the following are true`、`may recommend detention` 读成企业权利或绝对规则——见下方效力层。

**阶段 0 批判（BOOK_OVERVIEW §3，本卡 Boundary 来源）与法律位阶锚点**
- **IOM 非法规**：IOM 2026 Ch.6 是 FDA 内部操作指导（OII 机构 SOP），**不是法规，不创设企业义务，也不是可对外主张的法律依据**。真正的义务来源是 **FD&C Act §801、21 CFR Part 1（含 Prior Notice、FSVP）、19 CFR 113.62** 等法条与 CBP 法规；6.2.5.5 的 `must make a reasonable effort`、6.2.5.2 的 `must include all applicable alerts` 约束的是 **FDA 审查员的内部作业**，不产生企业的可诉权利。本卡任何结论都须回到上述法条与**当前版本 IOM / RPM** 复核。
- **should 与 as warranted 的裁量缺口**：章内密集使用 `should` / `as warranted` / `where appropriate` / `if the facts warrant`，却几乎不给判据——「请求扣留 vs 请求现场工作」的选择标准、照片 warranted 的情形、Pending Addition to DWPE 的处置，都留给分部惯例与 direct reference authority 的授权状态。本卡**不补写判据**，只把裁量缺口标为复核锚点。
- **2026 版快照**：PREDICT、ITACS、ACE、OASIS、SERIO、ER Job Aid、Import Alert 编号（如 IA 28-02）与 SOP 编号会随改版失效；本卡的 IA 例示与 work type 名是 2026 版快照，不是稳定规则。
- **监管者视角与组织前提**：全篇写「FDA 如何作出并执行决定」，默认使用者有 FDA 授权、系统权限、Division / Compliance Branch / OCI / CBP 协作通道；企业不具这些前提，照搬会把「检查清单」误当「合规义务清单」。本卡不写进口商/境外生产商如何举证或避免被扣（凡涉及一律见 E 段〔推导·非原书主张〕）。
- **系统绑定与跨章引用**：6.2 的细则大量靠 IOM 4.x（取样、audit sample 制备）、5.x（证据/报告）、RPM Chapter 9、各 CPGM 与 Import Alert 全文承载；单读第 6 章会得到「有骨架、缺细则」的闭环幻觉，且 6.9 术语表**完全没有 DER 条目**（只看术语表会以为只有一种扣留建议）。
- **不谈相对方权利与救济成本**：手册不提供进口商在听证中的举证成本、滞期与保证金风险权衡。
- **Exhibit 6-1~6-4 为扫描件、无文本层**（Notice of FDA Action / Form FDA 766 / Form FDA 790 / Form FDA 463a）；本卡涉及的扣留建议与任何表单**字段一律标「需查原件」**，不得据蒸馏文本推断字段内容。
- **条文号/分块与页码复核提示**：verified.md V02 把「Import Alerts: Do not routinely request work …」标为 `6.2.2.2.x [p.17]`，原文核对为 **IOM 6.2.2.2.3 [p.18]**；`6.2.5.5 - Registration/Listing/Approval` 条文号属 6.2，但正文落在 [p.23] 的 6.3 分块开头（MANIFEST 记 6.2 为 p.14-22）。主流程统一页码/条文号时须回原文确认。

**复核锚点清单（交主流程 / 阶段 1.6 晋级门）**
- **页码与条文号**：verified.md V02 把「Import Alerts: Do not routinely request work …」标为 `6.2.2.2.x [p.17]`，原文核对为 **IOM 6.2.2.2.3 [p.18]**；`6.2.5.5 - Registration/Listing/Approval` 条文号属 6.2，但正文落在 [p.23] 的 `6.3-Field-Examination.txt` 开头（MANIFEST 记 6.2 为 p.14-22），按分块检索会漏掉。主流程统一时须回原文确认。
- **法条**：任何义务/权利结论回 FD&C Act §801、21 CFR Part 1、19 CFR 113.62 与当前版本 IOM / RPM 复核；本卡不据 IOM 单独下义务。
- **系统编号**：PREDICT、ITACS、ACE、SERIO、ER Job Aid、Import Alert 编号（IA 28-02）、work type 名（DER/DTR、OGI/OGC）为 2026 版快照。
- **裁量缺口**：`You can submit a DER … if all the following are true`、`may recommend detention`、`as warranted` 的判据留给分部惯例与 direct reference authority 授权状态，本卡不补写。
- **术语表缺口**：6.9 无 DER 条目；DTR 有 Detention Recommendation（6.9.20）/ Detention Request（6.2.3.3 [p.20]）/ Detention Recommendations（6.2.5 标题）三种称法，自动化解析须兼容。
- **表单**：Exhibit 6-1~6-4 为扫描件，扣留建议与任何表单字段「需查原件」。
- **共享字样**：V01 复用「扣留」作决策门动作、V09 复用 DWPE / Detention 作状态词、V07 把 DWPE 作事后调查加重信号——三处均按 differentiator 分流。
- **企业侧**：E 段〔推导·非原书主张〕内容是从 FDA 分流与核实动作反推，非原书主张。

**相邻混淆**
- 与 V01 共享「扣留」字样但层次不同：V01 选「是否建议扣留」，本卡选「建议用 DER 还是 DTR」；审查员提交的始终是 recommendation / request，终局权在 Compliance Branch。
- 与 V09 共享 DWPE / Detention 术语：本卡只在「触发依据」意义上使用，V09 才是口径层；「DWPE 是扣留而非免检」的术语纠偏以 V09 / x14 为准。
- 与 CAP-18 的 483、V08 的 483a：扣留建议与检查观察项是不同章节、不同文书序列，正对应「二十类不可混引」。
- 三个「同形/同数」陷阱：IB = Import Bulletin（6.2 情报来源）vs IB = Investigations Branch（IB Release）；Alert vs Bulletin 方向相反；`Detention Recommendation`（6.9.20）/ `Detention Request`（6.2.3.3 [p.20]）/ `Detention Recommendations`（6.2.5 标题）为同一 work type 的三种称法，检索时勿当三个对象。
