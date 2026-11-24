# FDA 进口准入判定与处置链（IOM 2026 Chapter 6）（iom-imports-procedure）

*来源分层：本卡取用**单套进口作业程序**——FDA **Investigations Operations Manual 2026, Chapter 6「Imports」**（70 页 / 235 书签 / 约 24 万字符，Exhibit 6-1~6-4 为扫描表单、无文本层）。它是 FDA 给**入境审查员（Entry Reviewer）与调查员（Investigator / CSO）的内部作业手册**：规定怎样把一条 entry line 判入有限动作集、怎样按触发依据分 DER/DTR、怎样撤消放行、怎样在被扣后走听证→重整→拒绝→保证金、怎样对进口商作 FSVP 记录审查。**非法规、非 Guidance for Industry、不创设企业义务**；企业义务回 FD&C Act §801、21 CFR Part 1（Prior Notice / FSVP）、19 CFR 113.62 及包内〔§ 117.xxx〕等法规正文。与 IOM Ch.4（取样全流程 / CAP-28）、IOM Ch.5（检查员权限与 483 / CAP-18）、CP 7303.878（FSVP 检查 / CAP-21）、CP 7303.050（取样量 / CAP-17）分层，不得混引。*

*⚠ **效力层与版本口径**：本卡是 v4.17 为本包新增的**第二十一来源**（原「二十类不可混引」自本轮起为**二十一类不可混引**）。`must` / `shall` / 祈使句约束的是 **FDA 内部作业动作**，不产生企业的可诉权利或义务；`should` / `as warranted` / `may` / `where appropriate` 属**机构裁量**且章内几乎不给判据（留给分部惯例），更不构成企业法定义务——注意 `should only` / `should not` 形式软、语义却是禁止或唯一时点，`should … on all cases` 反而用裁量词覆盖全部个案，不可机械映射。2026 版是**快照**，强绑定 PREDICT / OASIS / ITACS / eNSpect / ACE / SERIO 与 WI-000618、SOP-000217、ER Job Aid 等内部系统与 SOP 编号，编号随系统改版失效；大量细则靠跨章引用承载（IOM 4.x 取样、5.x 证据/报告、8.x 调查备忘录、RPM Chapter 9 放行/听证/拒绝/保证金、各 CPGM）。Exhibit 6-1~6-4（Notice of FDA Action / Form FDA 766 / Form FDA 790 / Form FDA 463a AFFIDAVIT）为扫描件、无文本层，**字段一律标「需查原件」**，不得据蒸馏文本推断字段内容。凡本卡与法规正文冲突，以法规正文为准；企业不能以「IOM 没这么写」主张免责，也不能把 IOM 的作业时限当成自己的放行标准。全卡引用统一 `IOM 6.x.x [p.N]`，不得写成〔§ 117.xxx〕式法规引用。*

*本卡定位：**1 个可发现入口 + 10 个能力单元**，由本入口卡按意图路由到 10 张子卡（包内惯例「一个 IOM 单章 = 一张 CAP 卡」，CAP-28 = IOM Ch.4，本卡 CAP-29 = IOM Ch.6）。与既有 CAP 的分流要点：**483a（IOM 6.8 FSVP 观察项）≠ 483（IOM Ch.5 / CAP-18）**——二者名称相近、章节与文书序列都不同，是「二十七类不可混引」的重点负例；**取样形式要件与 702(b) 分割留样转 CAP-28**（本卡只「请求现场工作/取样」，不执行、不填 SCR、不拍照片）；**FSVP 合规程序层转 CAP-21**（本卡 V08 只是 IOM 6.8 的检查执行 SOP，不判 §1.500 主体定义、不写 subpart L 条款级结论）。**⚠ 触发判别（避免 483 / 483a 字形吸附）**：凡问 `483a` / FSVP Observations / closeout 唯一签发时点 / 检查期间能否展示草稿 / 15 工作日 FSVP 回应 / importer 定义三类证明 / T-EIR·CARS 分流 → **本卡 V08**；凡问 `FDA 483` 现场检查观察项措辞纪律 / 483 回复骨架 / Ch.5 检查员权限与 482·484 → **转 CAP-18，不进本卡**。同一串数字加一个字母 a，归属两套完全不同的文书序列，不得因字形相近合并路由。本卡对象是 entry line 的货物准入与事后追责，产物是 FDA 内部的决定、文书与时间窗，不是进口商的合规义务清单。*

---

## 能力单元路由表

> 加载规则：每次任务先读本入口卡，再按本表加载 **1 张**子卡；任务明确跨域时最多加载 2 张。V09（口径层）与 V10（效力层）是前置/边界层，**不单独抢路由**，须依附业务卡使用。所有子卡相对路径以本入口卡所在目录为基准。

| 单元 id | 中文标题 | 触发意图（浓缩） | 子卡相对路径 |
|---|---|---|---|
| V01 | 入境审查决策门与可辩护判定留痕 | 判某条 line 发 May Proceed / 请求现场工作 / 提交扣留建议 / OGA Referral 关闭 / 撤消；与 PREDICT 相悖的放行备注写什么才合格；他机关已扣押时 FDA 是否仍作可采性判定 | `references/capabilities/imports/entry-review-admissibility-decision-gate.md` |
| V02 | DER/DTR 按触发依据分流与 DWPE「不检查就扣住」 | 疑似违规的 line 该用 DER 还是 DTR；命中 Import Alert 能否免索单据直接 DER；数据库查不到注册/510(k)/PMA 或 A of C 缺失能否直接建议扣留；企业送检合格报告能否解除 DWPE | `references/capabilities/imports/der-dtr-detention-routing.md` |
| V03 | 事先通知（Prior Notice）适用性硬时限判定 | 某批食品是否须 PN、是否落在豁免清单；按运输方式×提交渠道算 2/4/8 小时与 15/30 天合法窗；「已提交但无 FDA 确认回执」是否算合规；国际邮件/随身行李/外交邮袋口径 | `references/capabilities/imports/prior-notice-eligibility-gate.md` |
| V04 | 条件放行 / 撤消 / redelivery 时间窗体系 | 条件放行货物还剩多少可采性决定时间；哪些动作会/不会延长 30 天；误发 May Proceed 或 IB Release 后 24 小时/30 天内必须完成什么；撤消后期间能否重开；30 天与 90 天如何分 | `references/capabilities/imports/conditional-release-rescission-windows.md` |
| V05 | 违规处置主链与文书矩阵（拒绝不是终点） | 被扣货物下一步出哪张通知/文书、由谁签字；听证期与 90 天出口/销毁期；收到 Refusal 后能否结案；Detention 与 Refusal 分界；拒绝后未按期处置的经济后果；charge 是否合法 | `references/capabilities/imports/violation-disposition-chain.md` |
| V06 | 改标 / 重整 Form FDA 766 授权门 | 收到 Detained 通知后能否自行改标/返工再申报；重整申请由谁提交、要不要新 bond；首次失败后能否再试、举证什么；合格部分放行后 rejects 怎么处置；766 / Importer's Certificate / 790 的位置 | `references/capabilities/imports/fda-766-reconditioning-authorization.md` |
| V07 | Failure to Hold 判定与 8 步调查清单 | 条件放行货物是否已构成 FTH；「移库/位移」与「分销」的认定差别；所有 FTH 案件必做的 8 步取证与 affidavit；健康危害/DWPE 是否追加召回与公共警告；4647 用 30 天还是 90 天 | `references/capabilities/imports/failure-to-hold-investigation.md` |
| V08 ★ | FSVP 检查链与 FDA 483a 签发门（⚠ 483a≠483，不转 CAP-18） | FSVP 检查对象与 Importer of Record 的区别；检查期间能否展示 483a 草稿；观察项写进 483a、T-EIR 还是 CARS；危害分析比对与差异追问；15 工作日回应；importer 不满足定义时 EIR 怎么处理 | `references/capabilities/imports/fsvp-inspection-483a-gate.md` |
| V09 | 进口状态概念区分树（放行 / 扣留 / 条件放行） | 某个 FDA 状态词到底意味着「能不能分销」；四种放行的法律含义差别；Conditional Release 与 May Proceed 的范畴差；Detention 与 Refusal 分界；三个 30 天与一个 90 天；「货可以移动」是否等于「可以销售」 | `references/capabilities/imports/admission-status-concept-tree.md` |
| V10 | IOM 效力层判读元规则（法律位阶与情态分层） | 某条 IOM 表述能否对企业主张为义务或权利；把 should / as warranted / may 与 must / shall 分开读；识别 `should only` / `should not` 反向陷阱；指导文件（CPG / IOM）是否构成豁免；2026 版快照；为企业侧推导标注〔推导·非原书主张〕 | `references/capabilities/imports/iom-effect-level-modality.md` |

**用户示例的既定路由**（供阶段 4 负例设计核对）：
- 「条件放行后未收 May Proceed 即发经销商」→ **V07**（FTH 认定），V04 只提供 30 天窗口背景。
- 「收到 Detained 通知后想自行改标再申报」→ **V06**（766 授权门），V05 提供其上下游链。
- 「PREDICT 高风险 + CBP 已以走私扣押」→ **V01**（OGA Referral 关闭、FDA 不作可采性判定）。
- 「483 与 483a 混用」「把 Conditional Release 当放行」「把 30 天与 90 天混用」→ 分别由 V09 / V10 提供口径与位阶纠偏，业务判定仍回各自业务卡。

---

## 硬时限与硬数字速查

> 全部为 IOM 内部作业口径，`IOM 6.x.x [p.N]` 为小节号 + 页码；「所属单元」指本入口卡下路由到的能力单元。数字相同不等于同一件事， especially 三处「30 天」同数异义。

| 数字 | 含义 | 出处 | 所属单元 |
|---|---|---|---|
| **2 / 4 / 8 小时** | Prior Notice 抵达**前**下限：公路 2h / 空运·铁路 4h / 水运 8h；国际邮件改为「寄出前须 FDA 接收并确认」 | IOM 6.1.5.1 [p.9] | V03 |
| **15 天（calendar days）** | Prior Notice 经 **PNSI** 提交的上限（不得早于预计抵达 15 天）；早于上限提交同样不合规 | IOM 6.1.5.1 [p.9] | V03 |
| **30 天（calendar days）** | Prior Notice 经 **ABI/ACE** 提交的上限（不得早于预计抵达 30 天） | IOM 6.1.5.1 [p.9] | V03 |
| **15 天（同数异义·其一）** | CBP Entry / Immediate Delivery 须在抵达后 **15 calendar days** 内申报——与 PN 的 15 天上限是两件事 | IOM 6.9.13 / 6.9.41 [p.51]/[p.55] | V04 / V09 |
| **10 工作日（working days）** | Notice of FDA Action - Detained 通常允许到场的听证期；有 compelling reason 可延长 | IOM 6.5.2.1 [p.39] | V05 |
| **24 小时** | 撤消 May Proceed 后：24h 内发更新 NOA、24h 内请 CBP bond hold、确认 ABI「勿分销」码、已分销则请求 redelivery | IOM 6.2.2.2.2 [p.17-18] | V04 |
| **24 小时（同构）** | 撤消 IB Release 后：24h 内通知 filer、生成更新版 NOA、请 CBP 在 24h 内 Unset/Hold bond | IOM 6.3.11 [p.32] | V04 |
| **30 天（同数异义·A）** | **条件放行期本身长度**：以 May Proceed / 拒绝通知 / 30 天届满三者最先发生者结束；DRQ/DTR/DER/DEF/INF 均不延长 | IOM 6.2.4 [p.20] | V04 |
| **30 天（同数异义·B）** | **CBP 请求 redelivery 的窗口**：货物 may be moved，但 CBP 可在 30 天内要求重新交付；从放行日（非发现误放行日）起算 | IOM 6.9.13 / 6.9.41 [p.51]/[p.55]；6.3.11 [p.32-33] | V04 / V09 |
| **30 天（同数异义·C）** | **Failure to Hold 下 4647 的 redelivery 期限**：因查验/取样签发 4647 时用 30 天，而非 Refusal 后的 90 天 | IOM 6.6.4.1 第 7 步 [p.43] | V07 |
| **90 天** | Refusal 后须在 90 天内于 CBP 监督下**完成**出口或销毁；「已安排」不算，档案到销毁/出口证明才关闭 | IOM 6.5.2.8 [p.41] / 6.9.44 [p.55] | V05 |
| **10 + 5 工作日** | 进口调查备忘录：末次调查活动后 **10 business days** 内提交主管背书，主管在 **5 business days** 内背书 | IOM 6.6.3 [p.43] | V07（6.6 事后追责域，背景数字） |
| **15 工作日（business days）** | FDA 483a 发出后，进口商应在检查结束日后 15 个工作日内回应；回应可能影响 FDA 是否采取后续行动 | IOM 6.8.2.1 [p.48-49] | V08 |

**数字陷阱**：三个「30 天」（条件放行期长度 / CBP redelivery 窗口 / FTH 下 4647 期限）与一个「90 天」（Refusal 后出口销毁）分属不同窗口，混用即所有倒计时计算全错（口径见 V09）；两个「15 天」（PN 上限 / CBP Entry 申报）也同数异义（V03）。

---

## 状态口径速查

> 「能否分销」以是否取得 FDA 解除进口状态的放行为准；「是否合规判定」区分「未作合规判定 / 已作合规判定 / 已明确认定违规 / 临时外观 / 终局」；「所属窗口」指该状态绑定的时间链。完整概念树见 V09。

| 状态词 | 能否分销 | 是否合规判定 | 所属窗口 / 出处 |
|---|---|---|---|
| **May Proceed** | 可分销 | **未作合规判定**（"No compliance decision has been made"），仅凭电子单据确认满足若干可采性要求；可被 rescind、不排除后续 §304(d) 执法 | 结束条件放行期；IOM 6.4.3 [p.35]、6.9.56 [p.56]、6.2.2.2.1 [p.17] |
| **Release** | 可分销 | **已作合规判定**（"A compliance decision has been made"）——FDA 查验后放行 | 结束条件放行期；IOM 6.4.3 [p.35] |
| **IB Release** | 可分销 | 现场查验完成后由**调查分部（Investigations Branch）**作出；Class 1 可径行、Class 2 有不良发现仍可裁量放行但须在 Summary 详述理由 | 结束条件放行期、撤消不重开；IOM 6.3.10.7 / 6.3.11 [p.32]、6.3 Class 2 [p.31] |
| **Release with Comment** | 可分销 | **已明确认定存在违规**（不具公共健康风险）仍放行，并**预告后续同类 entry 可能被拒**；会进入合规历史 | 预告后续拒绝；IOM 6.9.69 [p.57] |
| **Conditional Release** | **不可分销**（可移动不可分销） | 等待可采性判定期间的**状态**，不是「附条件合格」；货已交进口商控制但仍在 FDA 管辖，附 3 倍货值 redelivery bond | 通常 30 天，三事件先到者结束；IOM 6.9.13 / 6.9.41 [p.51]/[p.55]、6.2.4 [p.20] |
| **Detention** | 不可分销 | **临时行政措施**，基于 "not or **appear not to be**" 的外观标准，非违规认定；可回转（放行 / 拒绝 / 扣押） | 10 工作日听证；IOM 6.9.21 [p.52]、6.5.2.1 [p.39] |
| **DWPE** | 不可分销（免实物查验即扣） | 凭违规史 / Import Alert 即扣，**非逐批合规判定**；「不检查就扣住」而非「不检查就放过」 | 走 DER；解除须至少一份 FDA audit sample；IOM 6.9.22 [p.52]、6.2.5.1 [p.21]、6.9.6 [p.51] |
| **Refusal** | 不可分销 | **终局决定**（"final decision"），但**不是流程终点**：之后仍有 90 天出口/销毁、4647、Bond Action，档案到销毁/出口证明才关闭 | 90 天出口/销毁 + Bond Action；IOM 6.9.44 [p.55]、6.5.2.8 [p.41] |

**四条放行不可统一映射**：May Proceed（未作合规判定）、Release（已作合规判定）、IB Release（现场调查分部裁量）、Release with Comment（已认定违规并预告后续拒绝）法律含义各不相同；把它们一律映射成「放行 = 可销售 + 已合规 + 此批结案」是全书最系统的一组反直觉误读（V09）。**「货可以移动」≠「货可以销售」**：把 Conditional Release 或 CBP immediate delivery 回执当放行安排上架，直接构成 Failure to Hold（V07）+ Bond Action。

---

## 环节—文书矩阵

> 顺序严格递进：每一步的产物是下一步的输入。「需查原件」= 对应 Exhibit 6-1~6-4 为扫描件、无文本层，字段不得据蒸馏文本推断。文书本体与字段级规范大量转引未收（见末节）。

| # | 环节 | 触发 / 判定 | 产出文书 | 出具 / 签字方 | 出处 | 单元 |
|---|---|---|---|---|---|---|
| 1 | **Prior Notice 确认** | 食品/饲料是否须 PN、按渠道取上限、按运输方式取下限 | PN 电子提交 + **FDA 接收并确认回执**（received and confirmed）；FD3/FD4 PGA flag、A of C 码 PND 申明豁免 | filer 经 PNSI 或 ABI/ACE 提交，FDA 电子确认 | IOM 6.1.5.1 [p.9]、6.1.6.1 [p.12]、6.1.5.5 [p.11] | V03 |
| 2 | **May Proceed / NOA** | 电子单据确认全部合规且无需扣留/现场；或状态变化 | **Notice of FDA Action**（按每个 entry line 逐项、随状态变化**反复出具**；状态值含 sample collected / intended for sampling / detained / released / refused）+ May Proceed Notice | FDA Import Systems 自动生成，发 CBP 与 filer，filer 转告 importer | IOM 6.2.2.2.1 [p.17]、6.9.57 [p.56]、6.1.6.2 [p.13]；**Exhibit 6-1（需查原件）** | V01 / V05 |
| 3 | **Detained** | 听证后认定「看似违规」 | **Notice of FDA Action - Detained**：告知听证权、列出 charge | FDA；副本送 CBP | IOM 6.5.2.1 [p.39]、6.9.57 [p.56]；**Exhibit 6-1（需查原件）** | V05 |
| 4 | **FDA 766 重整申请** | 被扣后拟改标/重整 | **Form FDA 766**（Application for Authorization to Relabel or Recondition）；FDA 批准并退回原件列明 conditions 与 time limit；已备案 redelivery bond 适用、无须新 bond | **importer of record** 提交，FDA 批准 | IOM 6.5.2.3 [p.40]、6.1.3 [p.6]；**Exhibit 6-2（需查原件）** | V06 |
| 5 | **Importer's Certificate** | 按批准条件完成重整 | **Importer's Certificate**（766 第 2 页）或告知完成；FDA 可复核查验/取样或仅接受声明 | importer of record 提交，FDA 复核 | IOM 6.5.2.4 [p.40]；**表单字段需查原件** | V06 |
| 6 | **Notice of Release / Refusal** | 条件满足 → 放行；不满足或逾期 → 拒绝 | **Notice of Release「Released after Reconditioning」** 或 **Refusal of Admission**（charge 须与原 Detained 通知**逐字一致**）；rejects 仍须单独 Refusal + 监督销毁/再出口 | FDA | IOM 6.5.2.5 [p.40]、6.5.2.8 [p.41]；**Exhibit 6-1（需查原件）** | V05 / V06 |
| 7 | **CBP 4647** | 放行前已分销 / Refusal 后未按期处置 / 需查验或取样 | **Demand for Redelivery（Form CBP 4647）**；因查验/取样签发时 redelivery 期限 30 天（非 90 天） | CBP（FDA 协调、compliance officer 配合，缺件时通知 CBP CTAC） | IOM 6.6.4.1 第 7 步 [p.43]、6.5.2.8 [p.41]、6.5.2.10 [p.41-42] | V05 / V07 |
| 8 | **FDA 790** | 重整/查验产生监督费用 | **Form FDA 790（Charges for Supervision）**；费用向 CBP 收取，**任何 FDA 分部办公室不得代收** | FDA 计、付给 CBP | IOM 6.5.2.9 [p.41]；**Exhibit 6-3（需查原件）** | V05 / V06 |
| 9 | **Bond Action** | 放行前已分销且无法 redelivery，或已扣留并拒绝却未按期销毁/出口 | CBP 没收全部/部分 entry bond（liquidated damages）；涉 FDA 货物时 CBP 减免通常须 FDA 完全同意 | **CBP**（非 FDA） | IOM 6.5.2.11 [p.42]、6.9.11 [p.51]、6.9.66 [p.57] | V05 / V07 |
| 10 | **Affidavit（并行取证）** | FTH 8 步清单 ①–⑤、Substitution 差异说明 | **Form FDA 463a AFFIDAVIT**（书面宣誓，affiant 须对货物移动/状况有实质事实认知） | 授权人说明作成 affidavit，向 FDA 授权官员宣誓 | IOM 6.6.4.1 [p.43]、6.9.3 [p.50]、6.9.75 [p.58]；**Exhibit 6-4（需查原件）** | V07 |

**矩阵读法**：放行类动作（#2）与处置类文书（#3–#9）是两条不同的文书序列；483a（FSVP 观察项 / V08）与 483（IOM Ch.5 / CAP-18）都不在本矩阵的货物准入链上，属并行的合规检查轨，不得混引。

---

## 与既有 CAP 的分流（不得混引）

> 「二十七类不可混引」自 v4.17 起含 IOM Ch.6。本卡 6.x.x 引用不得与〔§ 117.xxx〕等法规正文、CP 7303.xxx 检查程序、IOM Ch.4/Ch.5 交叉混引；遇边界问题回 V10（效力层）与 V09（口径层）。

- **CAP-17（FDA 现场取样、样品量与阳性结果应对 / CP 7303.050）**：管「取多少 subs、每 sub 多少克、阳性怎么升级、702(b) 是否计入」。本卡只**请求**现场工作/取样、按 6.2 / 6.4 提到 SCR 字段与 SDI/ADS 形式要件，**不执行取样、不定样品量**；CAP-17 已注明 IOM Ch.4 与 702(b) 自 v4.16 起转 CAP-28。「请求现场工作」字样不得成为把 CAP-17 取样量混进 6.2 审查动作的借口。
- **CAP-18（FDA 检查员权限、文书与证据链 / IOM Ch.5）**：管现场检查法定基础、Form FDA 482/482a/482b/482c/482d/**483**/483a/484/4056 的签发时机与证据链、拒绝入场后果、483 回复 15 工作日。**483a（本卡 V08 / IOM 6.8 FSVP 观察项）≠ 483（IOM Ch.5 现场检查观察项）**：前者只在 closeout 签发且只签已签名版、检查期间不得展示草稿，对象是进口商的 FSVP 记录；后者是 Ch.5 现场检查观察项。二者的货物准入链文书是 Notice of FDA Action（本卡），与 483/483a 是不同序列。阶段 4 应专设「483 / 483a 混用」负例。
- **CAP-21（FSVP 进口商检查 / CP 7303.878 与 Part 117 供应链程序分流）**：管 **FSVP 合规程序层**——§1.500 FSVPI 主体定义、21 CFR part 1 subpart L 条款级判定、standard/modified requirements、Import Alert 99-41 与 Red List、direct reference authority。本卡 V08 是 **IOM 6.8 检查执行 SOP**：483a 的 closeout 唯一签发门与签署政策、监管方初步危害评估 vs 进口商危害分析的比对追问、importer 定义三类证明、15 工作日回应、T-EIR/EIR/CARS 分流。凡「某主体是不是 FSVPI」「§1.5xx 要求什么」「part 1 正文」一律转 CAP-21；本卡不判主体定义、不写条款级结论。
- **CAP-28（FDA 取样全流程作业程序 / IOM Ch.4）**：管样品类别（official / DOC / INV / survey）、取样数量、702(b) 留样七项豁免、表单链（482/472/484/415a/525/463a/1664）、封条与运输、阳性结果与 483。本卡涉及**取样形式要件**（请求现场工作、SCR 九字段、照片标识、ADS / SDI、官方封条 FDA 415a 与采集人 ID）一律转 CAP-28；本卡不展开取样执行。「取样形式要件与 702(b) 转 CAP-28」是硬分流。
- **CAP-16（FDA 现场检查迎检与记录举证）**：管迎检记录举证矩阵、483 回复骨架、OAI/VAI/NAI 分类。与本卡的货物准入轨、进口商 FSVP 记录审查轨（483a）不同；483 回复时限（15 工作日）与本卡 483a 回应（15 工作日）数值相同但文书、章节、对象不同，不得互套。
- **CAP-14（cGMP 合规分诊与内审索引）**：管 cGMP 指南里 should/recommend 对企业是否必须做。本卡 V10 是 **IOM 的效力层元规则**（must/shall 约束 FDA 内部、should 属机构裁量），两者来源不同、约束对象不同，不得因「should 怎么读」混引。
- **CAP-08（召回计划与报告义务）**：本卡 V07 在健康危害 / DWPE 加重情形下标出「须追加召回、收货人通知、公共警告协调」（IOM 6.6.4.2 / 6.6.4.3 [p.43-44]），但**召回计划本体、RFR 24 小时报告、Class I 判定转 CAP-08**；本卡只给触发条件，不写召回内容。
- **CAP-01…CAP-28 其余 PCHF / 危害分析 / 供应商批准 / 记录保存类卡**：本卡 V03 的「发运前置校验」、V08 的「危害分析比对」可能在企业侧抢路由，但本卡对象是 FDA 对 entry line 的判定，不是企业的 FSP / 危害分析 / 供应链验证义务；企业侧理解一律冠〔推导·非原书主张〕并回对应法规正文卡。

---

## 边界与判停（B 段汇总）

**反场景（不要用本卡 / 不要加载子卡）**
- 用户要的是**企业法定义务、合规结论或个案结果预测** → 本卡不代写法律文书、不出合规结论、不预测个案；回 FD&C Act §801、21 CFR Part 1（Prior Notice / FSVP）、19 CFR 113.62 等法规正文与包内〔§ 117.xxx〕卡。
- 用户要的是**取样执行 / 样品量 / 702(b) / 现场检查权限与 483** → 分别转 CAP-28 / CAP-17 / CAP-18；要 **FSVP 合规程序 / §1.500 主体 / subpart L 条款级** → 转 CAP-21。
- 用户已明确在**法规层**（FD&C Act / CFR）提问并给出法条 → 不必套 IOM 情态判读，直接回法条。
- 把 V09（口径层）或 V10（效力层）当「第 11 张业务卡」独立路由 → 错误；它们是前置/边界层，须依附业务卡使用。

**来源与位阶边界**
- **IOM 非法规**：IOM 2026 Ch.6 是 FDA/OII 机构内部标准作业程序，不是法规、不是可对外主张的法律依据，不创设企业义务。`must` / `shall` 约束的是 FDA 审查员/调查员内部作业，`should` / `as warranted` / `may` 属机构裁量；FDA 个案偏离 IOM 通常不产生可诉权利。正确定位是「理解 FDA 判定逻辑与举证要求的操作地图」。
- **指导文件不构成豁免**：IOM 6.1.5.5 [p.11] 明确 CPG 指导 "does not limit the FDA's ability … will not affect the ability of CBP to assess penalties under 19 U.S.C. 1595a(b)"——不构成豁免、不削弱任一机关执法权。
- **监管者视角 / 组织前提隐去**：全篇写「FDA 如何作出并执行决定」，不写进口商/境外生产商如何准备举证、如何避免被扣、如何回应 483a；默认使用者有 FDA 授权、系统权限、Division / Compliance Branch / OCI / CBP 协作通道。企业照搬会把「检查清单」误当「合规义务清单」。
- **裁量判据缺失**：`as warranted` / `where appropriate` / `should` 密集出现却很少给判据（请求扣留 vs 现场工作的选择标准、adverse conditions 阈值、照片 warranted 情形留给分部惯例）；另「电子数据可靠且完整」「有记录＝有合规」等假设未被论证（6.7 filer evaluation 只是周期性抽样监控）。判据缺失应作为复核锚点，**不应补写成规则**。
- **2026 版快照**：PREDICT / OASIS / ITACS / eNSpect / ACE / SERIO 与 WI-000618、SOP-000217、ER Job Aid 等界面与编号随改版失效；大量结论靠跨章引用承载（IOM 4.x / 5.x / 8.x、RPM Chapter 9、各 CPGM），单读第 6 章会得到「有骨架、缺细则」的闭环幻觉。
- **企业侧内容须冠〔推导·非原书主张〕**：一切「从 FDA 判定动作反推进口商/境外生产商应怎样准备」的理解都是推导，不是手册主张；10 张子卡的 A2 段已逐条标注，不得删除。

**引用纪律（本轮特别复核项）**
- 全卡引用统一 `IOM 6.x.x [p.N]`（小节号 + 页码），**不得**写成〔§ 117.xxx〕式法规引用，也不得把法条编号当成 IOM 章节号混引。
- **6.2.5.5 的 reasonable effort 条款正文跨页落在 p.23**：该小节（Registration/Listing/Approval，"You must make a reasonable effort to verify compliance … Do not recommend detention based solely on a failed data lookup or missing Affirmation of Compliance data"）的正文在本轮 `.cangjie/index` 切块里**物理落在 `[p.23]`，恰与 6.3 Field Examination 的起始页重叠**——这是按 6.1–6.9 切块时的邻接重叠，不是 6.3 的内容，也不是 6.2.5.5 有两个版本。**因此凡引用一律按小节号 `IOM 6.2.5.5 [p.23]`，不得按分块文件名（如「6.3 切块里那条」）引用**，否则会把扣留建议的核实义务误挂到现场查验章节。同类重叠：6.9 切块开头 `[p.50]` 含 6.8.3.1 尾部、6.8 切块出现 6.9.2，均按小节号而非分块名引用。
- **6.9 术语表自身瑕疵**：共 78 条，末条编号 `6-9.78`（连字符）与前 77 条 `6.9.x`（点号）不一致；且 DER / IUC / Import Bulletin / SDI / IB Release / VQIP 本体、May Proceed vs Release 的系统级区分、Conditional Release 的 30 天规则均**不在 6.9**，须回 6.1–6.8 正文取定义。详见 `GLOSSARY.md` 源层瑕疵节。
- **凡结论回当前版本 IOM / RPM 与法条复核**：只引 IOM 6.x.x 就下合规结论，依据不充分；Exhibit 6-1~6-4 表单字段「需查原件」。

---

## 未收与转引未收

> 一律标「转引未收」：本卡只覆盖 IOM 2026 Ch.6 经三重验证的 10 个能力单元，下列内容不在本轮蒸馏范围，遇相关提问明确告知超出本卡，不硬套、不据推断补写。

| 项 | 状态 | 去向 / 说明 |
|---|---|---|
| IOM Chapter 2 / 3 / 7 / 8 / 9 / 10 正文 | **转引未收** | 本章靠跨章引用承载；如 8.1.9.2 与 Exhibit 8-3-1（调查备忘录）仅在 6.6.3 [p.43] 被引用 |
| RPM Chapter 9（放行 / 听证 / 拒绝 / 保证金细则） | **转引未收** | 6.5 处置链的细则所在，单读 Ch.6 会缺细则 |
| CPG / CPGM 各指导文件全文（含 CPG Sec. 527.300、130.100 等） | **转引未收** | 6.1.5.5 [p.11] 只引其效力句（does not limit / will not affect），不收正文 |
| Import Alert 全文（IA 28-02、99-41、99-37/38、16-74、16-20 等） | **转引未收** | 本卡只收「命中 Alert → 走 DER / 不例行请求现场工作」的判定口径（V02 / V09），不收名单与列名规则；FSVP 相关转 CAP-21 |
| Import Bulletin 全文与正式定义 | **转引未收** | 6.9 无条目，仅由 6.2 / 6.3 用法反推「指示请求现场工作」 |
| 21 CFR part 1 subpart L 正文（FSVP 法条层） | **已收（v4.21）** | 企业义务见 CAP-33 `fsvp-statutory-requirements`；程序层转 CAP-21；本卡 V08 只收 IOM 6.8 检查 SOP |
| FD&C Act §801（含 a/b/d(1)/d(3)/e）、19 CFR 113.62、21 CFR 1.97(b)/1.99、19 U.S.C. 1595a(b) 法条正文 | **转引未收** | 仅作 V10 的复核锚点与「义务来源」标注，本卡不释义、不判条款级 |
| Exhibit 6-1~6-4 表单字段（Notice of FDA Action / Form FDA 766 / Form FDA 790 / Form FDA 463a AFFIDAVIT） | **转引未收** | 扫描件、无文本层，矩阵中已标「需查原件」 |
| PREDICT / OASIS / ITACS / SERIO / eNSpect / ACE 系统界面、WI-000618、SOP-000217、ER Job Aid 编号 | **转引未收** | 2026 版快照，点击级操作与内部 SOP 编号无迁移价值 |
| 6.3 各产品类别（食品/化妆品/药品/器械/生物制品/动物产品/辐射健康/烟草）查验要点清单 | **转引未收** | 纯列举性清单，仅可作某卡 example，不独立成卡 |
| 6.7 filer evaluation 完整程序、6.6.4.5/6.6.4.6 importer/filer misdeclaration 责任分流全谱 | **转引未收** | 作为 V07 佐证并入，不展开为独立能力 |
| 6.9 未收的 DER / IUC / Import Bulletin / SDI / IB Release / VQIP 本体定义 | **转引未收（已回正文补足）** | 定义回 6.1–6.8 取，本包 `GLOSSARY.md` 已补；「6.9 查无此词」不得推断「不存在」 |
| 企业侧迎检举证清单、WMS 状态机映射、合规义务清单 | **推导·非原书主张** | 由 FDA 判定动作反推，非手册主张；本卡不提供，须回法规正文卡并标注 |

---

*本入口卡与 10 张子卡同属 CAP-29（IOM 2026 Chapter 6 = 第二十一来源）。加载任一子卡前先读本卡；结论回当前版本 IOM / RPM 与法条复核；引用统一 `IOM 6.x.x [p.N]`。*
