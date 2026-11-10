# 进口状态概念区分树（放行 / 扣留 / 条件放行）（admission-status-concept-tree）

*来源分层与定位：IOM 2026 Ch.6 是 FDA 内部操作指导、不是法规，不创设企业义务；与 IOM Ch.4/Ch.5、CP 7303.878、CP 7303.050 分层，不得混引。本卡是**口径判定层（glossary-framework）**，材料集中在 IOM 6.9 Glossary（横切全链的术语层）与 6.4.3（系统两条放行消息定义）、6.3.10.7 / 6.3.11（IB Release）等正文定义处；它服务「二十类不可混引」的防混引约束，**不产出业务判定、不单独抢路由**，也不与 V01 / V04 / V05 / V07 的动作层互相替代。*

## R — 原文

> "May Proceed: 'Product may proceed without FDA examination. FDA has made no determination the product complies with all provisions of the Food, Drug, and Cosmetic Act, or other related acts. This message does not preclude action should the products later be found violative.' (No compliance decision has been made.)"
> "Release: 'The product is released after FDA examination. This message does not constitute assurance the product complies with all provisions of the Food, Drug and Cosmetic Act, or other related Acts, and does not preclude action should the product later be found violative.' (A compliance decision has been made.)"
> —— IOM 6.4.3 [p.35]
> 中文自译：系统里是**两条不同的放行消息**。May Proceed = 未经 FDA 查验、**未作合规判定**（No compliance decision has been made）；Release = **经查验后**放行、**已作合规判定**（A compliance decision has been made）。两条都写明「日后发现违规不排除再采取行动」，但「有没有形成合规决定」这一范畴截然不同，不可互换。

> "In FDA Import Systems, the following are definitions used to describe 'May Proceed' or 'Release' actions ..."
> —— IOM 6.4.3 [p.35]
> "The release performed after identifying and determining the line/entry meets certain admissibility requirements. This means the product can be distributed into U.S. commerce. However, a release does not preclude future FDA action if a problem is found later."
> —— IOM 6.9.56 [p.56]
> "An FDA compliance action releasing goods into interstate commerce advising the importer of violations with the FD&C Act that are not a health risk to the public. It also advises that future entries which continue to violate the Act may be refused."
> —— IOM 6.9.69 [p.57]
> 中文自译：6.9.56 把 May Proceed 定义为「放行、产品可进入美国流通，但放行不排除日后发现问题时 FDA 再采取行动」；6.9.69 的 **Release with Comment** 则是「已明确告知存在（不具公共健康风险的）违反 FD&C Act 情形，仍把货放入州际商业，并预告后续继续违规的 entry 可能被拒绝」——**放行 ≠ 没问题**，且这一条反而预示下一批会被拒。口径冲突时以 6.4.3 的系统定义为准（见 glossary g02）。

> "Even though CBP has allowed the immediate delivery, any FDA-regulated products are conditionally released until the FDA makes an admissibility decision. The conditional release period ends when the FDA 'May Proceeds' the entry or issues a refusal. The goods may be moved but CBP can request redelivery within 30 days."
> —— IOM 6.9.13 [p.51]
> "The conditional release period ends when FDA 'May Proceeds' the entry or issues a refusal."
> —— IOM 6.9.41 [p.55]
> 中文自译：即便 CBP 已允许 immediate delivery，FDA 监管货物在 FDA 作出可采性决定前**仍只是条件放行**；该期以「FDA 发 May Proceed / 发拒绝」结束。货物**可以移动**，但 CBP 可在 30 天内要求 redelivery。「可移动」与「可分销」被刻意分开——Conditional Release 是**等待判定期间的状态**，不是「结束该状态的决定」。

> "A temporary administrative action taken by the FDA against articles offered for entry which are not or appear not to be in-compliance with the laws the FDA administers. Detained articles can be released if brought into compliance, or are refused entry or seized, if not brought into compliance."
> —— IOM 6.9.21 [p.52]
> "FDA's final decision that a detained shipment is in violation of FDA laws and regulations. A refused shipment must either be destroyed or exported under the supervision of CBP and the FDA within 90 days of the date of the Notice of FDA Action (Refusal Notice)."
> —— IOM 6.9.44 [p.55]
> "The FDA file remains open until the division receives notification indicating that the goods were either destroyed or exported."
> —— IOM 6.5.2.8 [p.41]
> 中文自译：**Detention 是临时行政措施**，基于「不合规或**表面看来**不合规」的外观标准，可回转（经整改放行 / 拒绝 / 扣押三选一）；**Refusal of Admission 是终局决定**（final decision），须 90 天内于 CBP 与 FDA 监督下出口或销毁。但「终局」不等于「终点」：FDA 档案在分部收到销毁/出口证明之前**保持开放**。

> "If the exam was classified as Class 1, you will have the option to IB Release or Add Work. If no other work needs to be added to the line, the line will be released by selecting IB Release and entering Remarks, including an appropriate summary of remarks entered in the Exam Results."
> —— IOM 6.3.10.7 [p.32]
> "If the exam was class 2 with adverse findings, but IB is using discretionary authority to IB Release the line, remarks should include a detailed description of why the product was released when adverse findings were found."
> —— IOM 6.3.10.7 [p.32]
> "Note that when an entry receives an IB Release, the conditional release period of the entry ends (See IOM 6.2.4) and does not re-open when IB Release is rescinded."
> —— IOM 6.3.11 [p.32]
> 中文自译：**IB Release** 是现场查验完成后、由调查分部（Investigations Branch）作出的放行；Class 2 即便有 adverse findings，调查分部仍可**裁量放行**，但须在 Remarks 详述「为何在有不良发现时仍放行」。它同样结束条件放行期，且撤消后该期**不重开**。注意「IB」在本章是同形异义缩写：IOM 6.2 [p.15] 把 **IB 用作 Import Bulletin**，而 IB Release 里的 IB 指 **Investigations Branch**（6.3.10.7 [p.32]「IB is using discretionary authority」），与 Import Bulletin 无关。

> "Goods produced in the U.S. which are exported, and then returned to the United States. They are considered imports. (See Sec. 801(d)(1) of the FD&C Act [21 U.S.C. 381])."
> —— IOM 6.9.1 [p.50]
> "A term used to identify goods shipped out of the United States after being offered for entry. This is not the same as an export of U.S. manufactured goods and is not covered by the restrictions in Section 801(e) of the FD&C Act."
> —— IOM 6.9.67 [p.57]
> "Delivery, or offer for delivery, of merchandise into the Customs Territory of the United States from an outside point." / "Each portion of an entry that is listed as a separate item in an entry."
> —— IOM 6.9.25 / 6.9.28 [p.53]
> 中文自译：**AGR（美国货退回）被视为进口**（§801(d)(1)）；**Re-export（外国货申报入境后又运出）不适用 §801(e)**——两条法定例外方向相反却成对出现，极易串用。粒度层：**Entry 是报关行为**，**Line / Entry Line Item 是可单独审查、单独判定的最小单元**；一个 entry 可含多个 line，各 line 可分别放行、分别扣留、分别出通知。

**引文覆盖对照（verified.md `source_evidence` 关键口径 → R 组）**

| source_evidence 关键口径 | 落点 |
|---|---|
| 6.4.3 [p.35] May Proceed 未作合规判定 / Release 已作合规判定 | 组 1 |
| 6.9.56 [p.56] May Proceed 可进入流通但不排除后续行动 | 组 2 |
| 6.9.13 / 6.9.41 [p.51]/[p.55] Conditional Release 可移动不可分销、以 MP/拒绝结束 | 组 3 |
| 6.9.21 [p.52] Detention 临时、行政、外观标准 | 组 4 |
| 6.9.44 / 6.5.2.8 [p.55]/[p.41] Refusal 终局但档案保持开放 | 组 4 |
| 6.3.10.7 / 6.3.11 [p.32] IB Release（IB=Investigations Branch）、撤消不重开 | 组 5 |
| 6.9.69 [p.57] Release with Comment 已认定违规仍放行并预告后续被拒 | 组 2 |
| 6.9.1 / 6.9.67 [p.50]/[p.57] AGR 视为进口 / Re-export 不适用 §801(e) | 组 6 |
| 6.9.25 / 6.9.28 [p.53] Entry 报关行为 / Line 最小判定单元 | 组 6 |

## I — 自述

这张卡只做一件事：把一排长得很像的 FDA 状态词各自归位，回答三个问题——这个状态意味着什么、货物能不能分销、它属于哪个时间窗口。它不决定放行、不扣留、不算倒计时、不认定违规；是把这些动作交给别的卡之前的**口径前置层**。

最容易出错的地方是「放行」根本不是一个词，而是四种法律含义不同的动作。May Proceed 是电子审查后的放行，系统定义明说「未作合规判定」；Release 是查验后的放行，「已作合规判定」；IB Release 是现场查验后由调查分部作出，Class 2 有不良发现时还能裁量放行但须详述理由；Release with Comment 更反直觉——它是**已明确认定存在违规（只是无公共健康风险）仍放行**，并预告后续同类 entry 可能被拒。把这四种统一映射成「放行 = 合格 + 结案」，会同时踩中四个坑。

第二组坑是「状态」与「结束状态的决定」被混为一谈。Conditional Release 不是「有条件地合格」，而是货物已交进口商控制、仍处 FDA 管辖、须保持可召回、附货值 3 倍 redelivery bond 的**等待状态**；它以 May Proceed 或拒绝结束。原文「The goods may be moved」是合法的位移许可，绝不是分销许可——把它读成「可以销售」直接落入 Failure to Hold。

第三组是 Detention 与 Refusal。前者是临时的、行政的、基于「表面看来不合规」的外观标准，可回转；后者是终局决定。但「终局」仍不是终点：拒绝后还有 90 天出口/销毁、4647、销毁/出口核验、Bond Action，FDA 档案到拿到证明才关闭。

最后是数字陷阱：三个「30 天」和一个「90 天」同数异义，分别属于条件放行期长度、CBP 请求 redelivery 窗口、FTH 下 4647 期限、Refusal 后出口销毁窗口。再加上 AGR / Re-export 两条例外与 Entry / Line 的粒度差，构成一整套「字面语义整体反转」的机构口径树——而且错位方向一致：**都让人误以为自己更合规**。

**四种放行对照（不可统一映射为「放行 = 合格」）**

| 放行种类 | 作出阶段 / 主体 | 是否经查验 | 是否形成合规判定 | 隐藏后果 |
|---|---|---|---|---|
| **May Proceed** | 电子审查阶段 / entry reviewer | 否 | **否**（No compliance decision） | 可被 rescind；不排除 §304(d) 后续执法 |
| **Release** | 查验后 / 系统消息 | 是 | **是**（A compliance decision） | 仍不保证合规、不排除后续行动 |
| **IB Release** | 现场查验后 / **Investigations Branch** | 是 | 视 Class 而定 | Class 2 有不良发现仍可裁量放行、须详述理由；撤消不重开 |
| **Release with Comment** | 合规行动 / FDA | — | **已明确认定存在违规**（无公共健康风险） | 进入合规史；**预告后续同类 entry 可能被拒** |

## A1 — 书中用法

**情景一：产品无法取样或查验时系统给出什么状态（IOM 6.4.3 [p.35]）**
- 问题：entry 仍在进口分部控制下但取样无法完成，或已发查验/取样通知却两项操作都未执行。
- 动作：分部可在通知上批注「未采集产品」并把 entry 退回 filer，指定 **May Proceed**；系统会在 Line Summary 打印 "May Proceed" 状态并给出 "Lines Which May Proceed" 明细。手册随后列出 6.4.3 的两条系统定义，用来区分 May Proceed 与 Release 两类放行消息。
- 判定/后果：May Proceed = 未作合规判定；Release = 已作合规判定。把两者互换会误判案卷里「是否已经形成过合规决定」，直接影响听证举证；且两条都「不排除日后发现违规再采取行动」。

**情景二：Class 2 有不良发现仍被现场放行（IOM 6.3.10.7 [p.32]、IOM 6.3.11 [p.32]）**
- 问题：现场查验 Class 2 出现 adverse findings，调查分部仍拟放行该 line。
- 动作：可选 IB Release，但 Remarks 须**详述为何在存在不良发现时仍放行**（裁量放行）；该放行由 Investigations Branch 作出，不是 Import Bulletin。
- 判定/后果：IB Release 结束条件放行期，撤消后不重开（6.3.11）；把它当成「查验合格」或当成 May Proceed，会漏写法定放行理由、并在撤消窗口上算错。

**情景三：CBP 已允许 immediate delivery，企业据此安排上架销售（IOM 6.9.13 [p.51]、IOM 6.9.41 [p.55]）**
- 问题：手里只有 CBP 的 immediate delivery / 条件放行回执，能不能把货当已放行处理。
- 动作：按 6.9.13 归位——FDA 监管货物在 FDA 作出可采性决定前仍处 Conditional Release；「may be moved」只是位移许可。
- 判定/后果：以它安排分销即构成 Failure to Hold（V07）并触发 Bond Action；且条件放行期以 May Proceed / 拒绝结束，与 CBP 30 天 redelivery 窗口是两件事。

（Refusal「终局 ≠ 终点」与 90 天窗口按 IOM 6.9.44 [p.55]、6.5.2.8 [p.41] 并入 E Step 2 判定表与 B 段，不单列为第 4 条情景。）

## A2 — 未来触发 ★

**触发场景（3–5 条）**
1. 内部 WMS / 状态机要把 FDA 文书映射成「可否销售」，需要先分清 May Proceed、Release、IB Release、Release with Comment 四种放行。
2. 手里只有 CBP immediate delivery / 条件放行回执，要判断「能不能上架/发货」或「货可以移动是不是等于可以分销」。
3. 要区分 Conditional Release（等待状态）与 May Proceed（结束该状态的决定），或区分 Detention（临时可回转）与 Refusal（终局但非终点）。
4. 文档里同时出现多个「30 天」和一个「90 天」，需要判断某个倒计时到底属于哪个窗口。
5. 出现 AGR / Re-export、IB（Import Bulletin vs Investigations Branch）、Entry / Line 等同形异义或粒度词，需要口径归位；或为阶段 4 设计「把 Conditional Release 当放行」「把 Release with Comment 当无记录」「把 30 天与 90 天混用」负例找依据。

**语言信号（中英双写）**
- 中文：「这个状态能不能卖」「算不算已经放行」「条件放行是不是合格了」「May Proceed 和 Release 有什么区别」「IB Release 的 IB 是什么意思」「放行是不是就结案了」「30 天还是 90 天」「货可以移动就等于可以分销吗」「收到拒绝通知能不能归档」「附意见放行」
- English: "May Proceed", "Release", "IB Release", "Release with Comment", "Conditional Release", "Immediate Delivery", "Detention", "Refusal of Admission", "No compliance decision has been made", "can be distributed into U.S. commerce", "may be moved", "not admissible", "final decision", "file remains open", "three 30-day windows vs 90 days", "AGR / American Goods Returned", "Re-export", "Entry vs Line", "Investigations Branch vs Import Bulletin"

**与相邻能力的区分（依 verified.md differentiator）**
- **本卡是口径判定层 / 边界层，不产出业务判定、不单独抢路由。** 只回答「这个状态词意味着什么、能不能分销、属于哪个窗口、是否形成过合规判定」，**不产出动作**（V01）、**不算时限倒计时**（V04）、**不展开处置链**（V05）、**不认定违规**（V07）。状态词贯穿全链，因此与 V01 / V04 / V05 / V07 **全部**存在抢路由风险，是阶段 1.6 晋级门重点审视对象；命中动作类问题时须让位给对应业务卡。
- 与 **V01（入境审查决策门）**：V01 决定发哪张动作、备注怎么写；本卡只解释动作名/状态名的语义。
- 与 **V04（时间窗体系）**：V04 计算 30 天 / 90 天的起算、终止、不延长、不重开；本卡只指出「三个 30 天 + 一个 90 天」分属不同窗口、**不可混用**，不替用户算天数。
- 与 **V05（违规处置主链）**：V05 展开 Detained→听证→766→放行/拒绝→90 天→Bond；本卡只给 Detention / Refusal 的口径分界。
- 与 **V07（Failure to Hold）**：「把 Conditional Release 当放行而分销」的**违规认定与 8 步调查**归 V07；本卡只提供「可移动 ≠ 可分销」的口径。
- 与 **V02（DER/DTR）**：DWPE / Import Alert 的分流归 V02；本卡只解释 DWPE「不检查就扣住」这类术语字面反转。
- **本卡自身也最易被误当成业务判定卡**——它是「二十类不可混引」的防混引口径前置层，必须保持前置/边界定位。

**路由决策表（用户问法 → 该去哪张卡）**

| 用户问法 | 本卡 | 让位给 |
|---|---|---|
| 「May Proceed / Release / IB Release / Release with Comment 各是什么意思」 | ✅ 本卡（口径） | — |
| 「Conditional Release 能不能分销 / 属于哪个窗口」 | ✅ 本卡（口径） | — |
| 「这个状态词该发哪张动作 / 备注怎么写」 | 只给语义 | **V01** |
| 「条件放行期还剩几天 / 撤消后重不重开」 | 只给窗口归属 | **V04** |
| 「被扣后听证、766、90 天出口销毁」 | 只给 Detention/Refusal 分界 | **V05 / V06** |
| 「条件放行后未收 MP 就发货算不算违规」 | 只给「可移动 ≠ 可分销」 | **V07** |
| 「受 DWPE 约束该走 DER 还是 DTR」 | 只给术语字面 | **V02** |
| 「这个结论的法律位阶 / should 怎么读」 | — | **V10** |

## E — 执行步骤

**Step 1 — 归位：这个状态词属于哪一格**
- 动作：把用户给的词先归入四格之一——(a) **等待状态**（Conditional Release / Immediate Delivery）；(b) **四种放行**（May Proceed / Release / IB Release / Release with Comment）；(c) **不利状态**（Detention / DWPE / Refusal of Admission）；(d) **法定例外或粒度词**（AGR / Re-export / Entry / Line）。
- 完成标准：能说出归入哪一格，并给出该格的 IOM 6.x.x [p.N] 定义出处。
- **判停点**：若用户要的是「该发哪张动作 / 还剩几天 / 是不是违规 / 下一步出哪份文书」，**立即停止归位、转交 V01 / V04 / V07 / V05**，本卡不产出业务判定。

**Step 2 — 查判定表（状态词 → 能否分销 → 是否合规判定 → 所属窗口）**

| 状态词 | 能否分销 | 是否合规判定 | 所属窗口 / 关键后果 | 出处 |
|---|---|---|---|---|
| **Conditional Release / Immediate Delivery (ID)** | **否**（可移动、不可分销） | 未作（等待 FDA 可采性决定） | 条件放行期典型 30 天，以 May Proceed / 拒绝 / 30 天届满三者最先发生者结束；CBP 可 30 天内要求 redelivery；附货值 3 倍 redelivery bond | IOM 6.9.13 [p.51]、6.9.41 [p.55]、6.9.66 [p.57]、6.2.4 [p.20] |
| **May Proceed** | 是（可进入美国流通） | **否**（No compliance decision has been made） | 结束条件放行期；**可被 rescind**，撤消后 24h 硬动作 + CBP 30 天 redelivery；不排除日后依 §304(d) 执法 | IOM 6.4.3 [p.35]、6.9.56 [p.56]、6.2.2.2.1 [p.17] |
| **Release** | 是 | **是**（A compliance decision has been made，查验后） | 结束条件放行期；仍「不保证合规、不排除后续行动」 | IOM 6.4.3 [p.35] |
| **IB Release** | 是 | 视 Class 而定；Class 2 有不良发现时属**裁量放行**、须详述理由 | 结束条件放行期且**撤消不重开**；30 天从 IB Release 签发日起算 | IOM 6.3.10.7 / 6.3.11 [p.32] |
| **Release with Comment** | 是（放入州际商业） | **已明确认定存在违规**（不具公共健康风险）仍放行 | 进入合规历史，影响 PREDICT / DWPE / Import Alert；**预告后续同类 entry 可能被拒** | IOM 6.9.69 [p.57] |
| **Detention** | 否 | 临时行政措施，基于「not or **appear not to be**」外观标准 | 听证（一般 10 工作日）→ 整改/放行/拒绝；**可回转**，不是终点 | IOM 6.9.21 [p.52]、6.5.2.1 [p.39] |
| **DWPE** | 否（**不检查就扣住**） | 凭违规史 / Import Alert 免实物查验即扣 | 触发 DER；解除须至少一份 **FDA 自采 audit sample**，企业私人实验室报告无效 | IOM 6.9.22 [p.52]、6.9.6 [p.51]、6.2.5.1 [p.21] |
| **Refusal of Admission** | 否 | **final decision**（终局） | **90 天**内 CBP 监督下出口或销毁 + 4647 + 核验 + Bond Action；档案到销毁/出口证明才关闭，**非终点** | IOM 6.9.44 [p.55]、6.5.2.8 [p.41] |
| **AGR（美国货退回）** | 按进口处理 | 视为进口 | §801(d)(1)；不得排除在入境审查外 | IOM 6.9.1 [p.50] |
| **Re-export** | 不适用 | 已申报入境后又运出的外国货 | **不适用 §801(e)** 对美国制造品出口的限制 | IOM 6.9.67 [p.57] |
| **Entry / Line** | 不适用 | 粒度词，非状态 | Entry = 报关行为；Line = 可单独判定的最小单元，各 line 分别放行/扣留/出通知 | IOM 6.9.25 / 6.9.28 [p.53]、6.9.57 [p.56] |

- 完成标准：用户给的每个词都能在表中定位，且「能否分销」与「是否合规判定」两列答案明确、不靠猜。
- **判停点**：「放行」类词一律不得统一映射为「可销售 + 已合规 + 结案」；若发现用户在做这种统一映射，逐行指出四种放行各自的差异（见 V09 V2 预测题）。

**Step 3 — 拆数字：三个 30 天 + 一个 90 天**
- 动作：遇到「30 天 / 90 天」先问**它属于哪个窗口**，不按数值归并：
  1. **30 天（A）**＝条件放行期本身长度（IOM 6.2.4 [p.20]）；
  2. **30 天（B）**＝CBP 请求 redelivery 的窗口（IOM 6.9.13 [p.51]）；
  3. **30 天（C）**＝FTH 下因查验/取样签发的 4647 redelivery 期限（IOM 6.6.4.1 [p.43] 第 7 步）；
  4. **90 天**＝Refusal 后出口/销毁窗口（IOM 6.9.44 [p.55]、6.5.2.8 [p.41]）。
- 完成标准：能说出「本案这个数字 = 哪一窗口」，且不与撤消后 24 小时硬动作、10 工作日听证期混用。
- **判停点**：需要**实际计算**某个倒计时还剩几天 → 转 **V04**；本卡只做窗口归属判定。

**Step 4 — 查同形异义与字面反转**
- 动作：逐项核对——`IB`（Import Bulletin，IOM 6.2 [p.15]）vs `IB`（Investigations Branch，IB Release，IOM 6.3.10.7 [p.32]）；`DWPE`（不检查就**扣住**，非放过）；`Conditional Release`（仍处管辖、须可召回，非「有条件合格」）；`May Proceed`（终局放行动作，非「准许继续办理」）；`may be moved`（位移许可，非分销许可）；`AGR` vs `Re-export`（§801(d)(1) vs §801(e)，方向相反）。
- 完成标准：每个易混词都能给出「常识义 → IOM 义 → 混淆后误判」三元组。
- **判停点**：三种术语误读方向一致——**都高估自身合规状态**；凡结论让用户显得「更合规 / 更没事」，须回到本表复核，不可直接采信。

**Step 5 — 边界收口**
- 本卡不代写正式法律文书、不出合规结论、不预测个案结果；不产出 May Proceed / 扣留 / 拒绝等任何动作，不算时限倒计时，不认定违规。
- **〔推导·非原书主张〕** 企业侧（进口商 / 境外生产商）可据上述口径反推的理解：内部状态机应把 FDA 放行、CBP 条件放行、DWPE 命中、Release with Comment 显式区分，以「逐 line 收到 FDA 放行文书」为唯一可分销状态，并把命中 Import Alert / DWPE 视为升级信号而非免检信号。**此为据监管者口径反推，IOM 是 FDA 内部操作手册、不写企业侧义务，不构成原书主张，也不产生合规结论。**

**判停点汇总（E 段全部闸门）**

| # | 判停位置 | 触发条件 | 动作 |
|---|---|---|---|
| 1 | Step 1 | 用户要动作 / 倒计时 / 违规认定 / 处置链 | 停止归位，转交 V01 / V04 / V07 / V05 |
| 2 | Step 2 | 发现「放行 = 合格 + 结案」统一映射 | 逐行指出四种放行差异 |
| 3 | Step 3 | 需要**实际计算**还剩几天 | 转 V04，本卡只做窗口归属 |
| 4 | Step 4 | 结论让用户显得「更合规 / 更没事」 | 回表复核，不直接采信 |
| 5 | Step 5 | 需要正式文书 / 合规结论 / 个案预测 | 收口，交回有权限人员 |

**三个 30 天 + 一个 90 天窗口归属表**

| 数值 | 窗口 | 出处 | 常见混用 |
|---|---|---|---|
| 30 天（A） | 条件放行期本身长度 | IOM 6.2.4 [p.20] | 与 CBP redelivery 窗口混 |
| 30 天（B） | CBP 请求 redelivery 窗口 | IOM 6.9.13 [p.51] | 与条件放行期长度混 |
| 30 天（C） | FTH 下 4647（查验/取样）redelivery 期限 | IOM 6.6.4.1 [p.43] | 与拒绝后 90 天混 |
| 90 天 | Refusal 后出口/销毁窗口 | IOM 6.9.44 [p.55]、6.5.2.8 [p.41] | 与 30 天（C）混 |

（另有撤消后 24 小时硬动作、10 工作日听证期、FSVP 483a 15 工作日回应，均不属这四个窗口。）

## B — 边界

**反场景（不要用本卡）**
- 用户要的是**动作**：「这条 line 该发 May Proceed 还是请求扣留」→ V01；「DER 还是 DTR」→ V02。
- 用户要的是**倒计时**：「条件放行期还剩几天 / 撤消后怎么算」→ V04；「拒绝后 90 天怎么处置」→ V05。
- 用户要的是**违规认定**：「条件放行后未收 May Proceed 就发经销商算不算违规、要查什么」→ V07。
- 用户要的是**法规实体义务**：「FSVP 规则到底要求什么」→ 法条 / CP 7303.878，不是 IOM 口径层。
- 需要出具正式法律文书、给出合规结论或预测个案结果时，本卡只提供口径，不能代写、不能下结论。

**作者警告的失败模式（来自 counter-example x14、glossary g02/g03/g04/g28、V2 预测题）**
- 把内部 WMS 的四种 FDA 文书（May Proceed / Release / IB Release / Release with Comment）统一映射成「放行 = 可销售 + 已合规 + 此批结案」，并把 CBP immediate delivery 回执归到同一状态——至少四处误判：May Proceed 不是合规背书且可被 rescind；Release with Comment 已认定违规并预告后续被拒；IB Release 的 IB 不是 Import Bulletin 且 Class 2 裁量放行须详述理由；CBP immediate delivery 根本不是 FDA 放行。
- 把 `Conditional Release` 读成「有条件地合格 / 已通过」，把 `may be moved` 读成「可以分销」→ 直接落入 Failure to Hold + Bond Action。
- 把 `DWPE` 读成「不检查就放过」→ 命中 Import Alert 仍按普通货物排产，遇健康危害加重情形未升级。
- 把 `May Proceed` 按字面读成「准许继续办理 / 开始审查」→ 在放行前误启动后续动作或错过撤消窗口；以为拿到 May Proceed 就永久免责 → 忽视 §304(d) 后续执法。
- 发出 Refusal Notice 即归档 → 未核验销毁/出口、未发 4647、错过 Bond Action 时效。
- 把三个「30 天」与一个「90 天」混用 → 所有倒计时计算全错；把 AGR 与 Re-export 混用 → §801(d)(1) 与 §801(e) 适用颠倒。
- 把 `IB Release` 读成「按 Import Bulletin 放行」→ 满世界找不存在的文书；把「货可以移动」当成「货可以分销」。
- **本卡自身最易被误当成业务判定卡**——它是防混引的口径前置层，须保持「不产出动作」的定位，否则会与 V01/V04/V05/V07 抢路由。

**阶段 0 批判（BOOK_OVERVIEW §3，作为本卡 Boundary 来源）**
- **IOM 非法规**：IOM 2026 Ch.6 是 FDA 内部操作指导，不是法规、不是可对外主张的法律依据，不创设企业义务。本卡的所有定义都是「理解 FDA 判定逻辑的操作地图」，不是企业合规义务清单；真义务来源在 FD&C Act §801、21 CFR Part 1、19 CFR 113.62 等法条，须回当前版本 IOM / RPM 复核（见 V10）。
- **2026 版快照**：PREDICT、ITACS、ACE、OASIS、SERIO、eNSpect、RPM Chapter 9 等系统与文档编号会随改版失效；6.9 术语表自身也明说「Refer to the RPM Glossary for a more complete listing」，**不是穷尽清单**——遇 6.9 未收词条（DER、IUC、Import Bulletin、SDI、IB Release、VQIP 本体）不得据「6.9 没有」推断「不存在」，须回 6.1–6.8 正文复核。
- **系统绑定 / 跨章引用**：本卡的定义分散在 6.2 / 6.3 / 6.4 / 6.5 / 6.6 / 6.9，且 6.9.56 与 6.4.3 对 May Proceed 存在口径张力（以 6.4.3 系统定义为准）；单读术语表会得到「有骨架、缺细则」的闭环幻觉。
- **监管者视角**：全篇写「FDA 如何判定」，不写进口商如何理解与应对；企业照搬会把「检查清单」误当「合规义务清单」。组织前提（FDA 授权、系统权限、Compliance Branch / OCI / CBP 通道）企业不具备。
- **裁量判据缺失**：`as warranted` / `where appropriate` / `in general` 不给阈值；本卡不补写判据。另源文件有编号瑕疵（末条 `6-9.78` 与前 77 条 `6.9.x` 不一致）、6.9.13 与 6.9.41 近乎重复、IB / PGA 展开词不统一，自动化解析须兼容变体，引用时如实标注。
- **Exhibit 6-1~6-4 为扫描件、无文本层**（Notice of FDA Action / Form FDA 766 / Form FDA 790 / Form FDA 463a）；凡涉及这些表单的**字段一律标「需查原件」**，不得据蒸馏文本推断字段内容。

**相邻混淆**
- 与 V01 / V04 / V05 / V07 **全部**抢路由（状态词贯穿全链）——本卡是前置/边界层，命中动作类问题须让位。
- 与 V02：DWPE / Detention 术语口径 vs DER/DTR 分流；与 V10：口径层 vs 效力/边界层（两者都不产出业务判定）。
- 与包内既有【放行 / 状态判定】类 CAP：企业侧「可分销闸门」语境不得与本卡的 FDA 口径层互相替代。

**误判信号 → 正确口径速查**

| 危险信号 | 直觉结论 | IOM 正确口径 |
|---|---|---|
| 「放行 = 已合规、可以结案」 | 统一映射 | 四种放行法律含义不同；May Proceed **未作合规判定**（IOM 6.4.3 [p.35]） |
| 「Release with Comment = 没问题」 | 无记录、不整改 | 已认定违规仍放行，并**预告后续同类 entry 可能被拒**（IOM 6.9.69 [p.57]） |
| 「Conditional Release = 有条件合格」 | 可上架销售 | 仍在 FDA 管辖、可移动不可分销（IOM 6.9.13 [p.51]） |
| 「货可以移动 = 货可以分销」 | 可发货 | 位移许可 ≠ 分销许可；提前分销 = Failure to Hold（V07） |
| 「DWPE = 不检查就放过」 | 降低查验优先级 | **不检查就扣住**，是加重信号（IOM 6.9.22 [p.52]） |
| 「IB Release 的 IB 是 Import Bulletin」 | 找通报文书 | IB = **Investigations Branch**（IOM 6.3.10.7 [p.32]） |
| 「收到 Refusal 就归档」 | 终局 = 终点 | 档案到销毁/出口证明才关闭（IOM 6.5.2.8 [p.41]） |
| 「30 天和 90 天差不多」 | 混用 | 三个 30 天 + 一个 90 天分属不同窗口 |
| 「AGR / Re-export 都是出口」 | 串用 | AGR 视为进口 §801(d)(1)；Re-export 不适用 §801(e)（IOM 6.9.1 / 6.9.67） |

**本卡 IOM 引用索引（均为 `IOM 6.x.x [p.N]`，非法规引用）**

| 出处 | 本卡用途 |
|---|---|
| IOM 6.4.3 [p.35] | May Proceed / Release 两条系统消息定义 |
| IOM 6.9.56 [p.56] / 6.9.69 [p.57] | May Proceed 放行、Release with Comment |
| IOM 6.9.13 [p.51] / 6.9.41 [p.55] / 6.9.66 [p.57] | Conditional Release、ID、3 倍 redelivery bond |
| IOM 6.9.21 [p.52] / 6.9.23 [p.52-53] | Detention 临时外观标准、听证 |
| IOM 6.9.44 [p.55] / 6.5.2.8 [p.41] / 6.5.2.11 [p.42] | Refusal 终局、档案开放、Bond Action |
| IOM 6.3.10.7 / 6.3.11 [p.32] | IB Release、Class 2 裁量放行、撤消不重开 |
| IOM 6.9.22 [p.52] / 6.9.6 [p.51] | DWPE、audit sample 解除门槛 |
| IOM 6.9.1 [p.50] / 6.9.67 [p.57] | AGR / Re-export 两条例外 |
| IOM 6.9.25 / 6.9.28 / 6.9.57 [p.53]/[p.56] | Entry / Line 粒度、逐 line 通知 |
| IOM 6.2.4 [p.20] / 6.2.2.2.1 [p.17] | 条件放行期 30 天、§304(d) 后续执法 |
| IOM 6.6.4.1 [p.43] / 6.9.30 [p.53]（仅交叉） | FTH 30 天 4647、术语复述 |

（法条仅作 Boundary 复核锚点：FD&C Act §801 / §801(d)(1) / §801(e)、21 CFR Part 1、19 CFR 113.62；详见 V10。）
