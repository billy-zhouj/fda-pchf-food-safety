# IOM 2026 Chapter 6 — Imports 正式术语词典（GLOSSARY）

> 本词典是 cangjie-skill 阶段 3 产物，由 `candidates/glossary.md`（28 条候选）整理提升而来，随 CAP-29 增量升级 `fda-pchf-food-safety` 技能包分发，是 10 张能力卡的**共享口径层**。
> 收录 28 条，按**中文译名主题**分 10 组。每条含：英文术语 / 中文译名 / IOM 定义（英文逐字引用，每段 ≤100 词 + 中文自译）/ 出处 / 与常识的差异 / 混淆后会导致的判定错误。
> **引用纪律**：出处一律 `IOM 6.x.x [p.N]`（小节号 + 页码）；本词典不把 IOM 内容改写成〔§ 117.xxx〕式法规引用。文内出现的 FD&C Act / CFR 条文号仅作「法条锚点」或英文原文引用内容，不是 IOM 引用。
> **定位**：服务于「理解 FDA 判定逻辑与举证要求」，不是企业合规义务清单；法律位阶限制见 `BOOK_OVERVIEW.md` §3 与能力卡 V10（`iom-effect-level-modality`）。

---

## 一、报关与判定单元

### g01 · Entry / Line / Entry Line Item — 报关 / 报关行项 / 报关分项

- **英文术语**：Entry；Line (Line Item)；Entry Line Item（对照：Lot）
- **中文译名**：报关（行为）/ 报关行项 / 报关分项
- **IOM 定义**：
  > `6.9.25 – Entry`："Delivery, or offer for delivery, of merchandise into the Customs Territory of the United States from an outside point." —— IOM 6.9.25 [p.53]
  > `6.9.28 – Entry Line Item`："Each portion of an entry that is listed as a separate item in an entry. An importer may identify merchandise in an entry in multiple portions; however, an item in the entry having a different tariff description must be listed separately." —— IOM 6.9.28 [p.53]
  - 中文自译：Entry 是货物自境外交付（或提出交付）进入美国关税领土的行为；Line 是一次报关中被单列为独立项目的每一部分，关税描述（及税率）不同者必须分开列项。
- **出处**：IOM 6.9.25 / 6.9.28 [p.53]、6.9.52 [p.56]；正文 IOM 6.9.57 "broken down by each entry line" [p.56]、6.4.3 "Lines Which May Proceed" [p.35]；Lot 对照 IOM 6.9.53 [p.56]。
- **与常识的差异**：≠「一批货 / 一个提单 / 一个集装箱」。Entry 是**报关行为**；Line 是**可单独审查、单独作出可采性判定的最小单元**——一个 entry 可含多个 line，各 line 可分别放行、分别扣留、分别出通知。Lot 是取样单元（可跨 entry），Import Status 是数据库「尚未放行」状态（6.9.46 [p.55]），粒度均不同。
- **混淆后会导致的判定错误**：把整票当单一判定单元 → 对未查验的 line 误放行或漏扣留；Notice of FDA Action 未按 line 拆分；把「Lines Which May Proceed」（6.4.3 [p.35]）单行放行误读为整票放行；Failure to Hold / Substitution 调查时错定责任货量范围。

---

## 二、放行与状态类

### g02 · May Proceed / Release — 准予放行 / 查验后放行（★ 系统内两种放行消息）

- **英文术语**：May Proceed；Release
- **中文译名**：准予放行 / 查验后放行
- **IOM 定义**：
  > `6.9.56 – May Proceed`："The release performed after identifying and determining the line/entry meets certain admissibility requirements. This means the product can be distributed into U.S. commerce. However, a release does not preclude future FDA action if a problem is found later." —— IOM 6.9.56 [p.56]
  > `6.4.3`（系统级定义）："May Proceed: 'Product may proceed without FDA examination. **FDA has made no determination the product complies** with all provisions of the Food, Drug, and Cosmetic Act...' **(No compliance decision has been made.)**" / "Release: 'The product is released **after FDA examination**... (A compliance decision has been made.)'" —— IOM 6.4.3 [p.35]
  - 中文自译：6.9 把 May Proceed 定义为「确认满足若干可采性要求后作出的放行、产品可进入美国流通、日后发现问题不排除再行动」；6.4.3 系统定义更严格：May Proceed = 未经查验、**未作合规判定**的放行消息，Release = 经查验、**已作合规判定**的放行消息。
- **出处**：IOM 6.9.56 [p.56]；**IOM 6.4.3 [p.35]**；6.2.2.2.1 [p.17]、6.2.2.2.2 [p.18]、6.2 第 85/83/176 行 [p.15]/[p.17]。
- **与常识的差异**：字面「可以开始继续办理」≠ 终局性放行动作（可进入流通、且可 rescind）；**≠「判定合规」**（6.4.3 明确 `No compliance decision has been made`，与 6.9.56 的宽松表述有口径张力，以 6.4.3 为准）；**May Proceed ≠ Release**（未经查验无合规判定 / 经查验已作合规判定，是系统两条消息，不可互换）；禁止把 "May Proceed" / "N/A" 当理由写进 Remarks。
- **混淆后会导致的判定错误**：把 May Proceed 当「FDA 已出具合规背书」→ 企业误以为免除后续责任（实际 `does not preclude future FDA action`）；与 PREDICT 相悖的放行不写具体理由 → 违反 6.2 明令；把「未作合规判定」当「已判定合格」→ 后续发现违规时误以为 FDA 已放弃追责；混淆二者 → 错判案卷里是否已存在合规决定，影响听证举证。

### g03 · Conditional Release / Immediate Delivery (ID) — 条件放行 / 即时交付

- **英文术语**：Conditional Release；Immediate Delivery (ID)
- **中文译名**：条件放行 / 即时交付
- **IOM 定义**：
  > `6.9.13 – Conditional Release`："Entry/Immediate Delivery must be filed within 15 calendar days of arrival... Even though CBP has allowed the immediate delivery, any FDA-regulated products are conditionally released until the FDA makes an admissibility decision. The conditional release period ends when the FDA 'May Proceeds' the entry or issues a refusal. The goods may be moved but CBP can request redelivery within 30 days." —— IOM 6.9.13 [p.51-52]
  > `6.2.4`："CBP may conditionally release a product while it awaits an FDA admissibility decision... This period typically lasts for 30 days. It ends as soon as one of these things happens first: The FDA issues a 'May Proceed' notice / The FDA issues a notice of refusal / The 30-day period expires." —— IOM 6.2.4 [p.20]
  - 中文自译：CBP 允许即时交付后，FDA 监管货物仍处「条件放行」状态直到 FDA 作出可采性判定；货**可以移动**但 CBP 可在 30 天内要求重新交付；条件放行期通常 30 天，以三事件中最先发生者结束。
- **出处**：IOM 6.9.13 [p.51-52]、6.9.41（重复条目）[p.55]；**IOM 6.2.4 [p.20]**；6.9.66 Redelivery Bond [p.57]。
- **与常识的差异**：≠「有条件地合格 / 附条件批准」——货已交进口商控制但**仍在 FDA 管辖下**，附带 redelivery bond 义务（6.9.66，货值 3 倍）；**「可移动」≠「可分销」**；三个「30 天」不是同一件事（条件放行期长度 / CBP 请求 redelivery 窗口 / FTH 下 4647 期限）；≠ May Proceed（条件放行是**等待判定的状态**，May Proceed 是**结束该状态的决定**）。
- **混淆后会导致的判定错误**：把条件放行当放行 → 提前分销，构成 Failure to Hold（g11）并触发 CBP 4647 与 Bond Action；把「可以移动」理解为「可以销售」→ 同一后果；错过 30 天窗口 → 无法 redelivery，只能追偿 liquidated damages；把三个 30 天混用 → 期限计算全错。

### g04 · IB Release — 调查分部放行（★ IB 为同形异义缩写）

- **英文术语**：IB Release（Investigations Branch Release）
- **中文译名**：调查分部放行
- **IOM 定义**：
  > `6.3.10.7 – Next Steps`："If the exam was classified as Class 1, you will have the option to IB Release or Add Work. If no other work needs to be added to the line, the line will be released by selecting IB Release and entering Remarks, including an appropriate summary of remarks entered in the Exam Results." —— IOM 6.3.10.7 [p.32]
  > `6.3.11`："Note that when an entry receives an IB Release, the conditional release period of the entry ends (See IOM 6.2.4) and does not re-open when IB Release is rescinded." —— IOM 6.3.11 [p.32]
  - 中文自译：现场查验（Class 1，或 Class 2 经裁量）完成、无需追加工作时，由**调查分部（Investigations Branch）**作出的放行；同样结束条件放行期、撤消后不重开。
- **出处**：IOM 6.3.10.7 / 6.3.11 [p.32]、6.3 Class 2 分类 [p.31]；缩写证据 IOM 6.2.2.2.6 "To send a line to the **Investigations Branch (IB)**" [p.19]；对照 IOM 6.2 第 95 行 "Import Alerts (IA) and **Import Bulletins (IB)**" [p.15]。
- **与常识的差异**：**★ IB 是同形异义缩写**——① 6.2 情报来源清单中 IB = Import Bulletin（g17）；② 6.2.2.2.6 中 IB = Investigations Branch；③「IB Release」的 IB 指 Investigations Branch，**与 Import Bulletin 无关**。≠ May Proceed（IB Release 是现场查验/取样后由调查分部作出，May Proceed 是电子审查阶段）；**Class 2 有 adverse findings 仍可 IB Release**，但须在 Summary / Remarks 详述理由；**6.9 术语表未收 IB Release**。
- **混淆后会导致的判定错误**：把 IB Release 读成「按 Import Bulletin 放行」→ 找不存在的文书、漏掉与 Import Alert 的分流；把 Class 2 有不良发现的裁量放行当「查验合格」→ 漏写法定放行理由、听证无法辩护；把 IB Release 当 May Proceed → 误判放行所处阶段与是否已形成合规决定。

### g28 · Release with Comment — 附意见放行

- **英文术语**：Release with Comment
- **中文译名**：附意见放行
- **IOM 定义**：
  > `6.9.69 – Release with Comment`："An FDA compliance action **releasing goods into interstate commerce** advising the importer of **violations with the FD&C Act that are not a health risk to the public**. It also advises that **future entries which continue to violate the Act may be refused**." —— IOM 6.9.69 [p.57]
  - 中文自译：FDA 在明知存在「不具公共健康风险」的违反 FD&C Act 情形时仍把货物放入州际商业，同时书面告知该违规，并预告后续同类违规的 entry 可能被拒。
- **出处**：IOM 6.9.69 [p.57]；对照 IOM 6.9.56 [p.56]、6.4.3 [p.35]、6.9.21 [p.52]、6.9.42 / 6.9.22（合规历史输入）。
- **与常识的差异**：**放行 ≠ 合规**——是「已明确认定存在违规（但无公共健康风险）仍放行」并**预告后续将被拒绝**；≠ May Proceed（未作合规判定）/ ≠ Release（查验后放行、未明说违规）/ ≠ Detention（g05，不扣留但留书面警告记录，构成后续 Refusal 的前科，会进入合规历史影响 PREDICT / DWPE / Import Alert 判定）。
- **混淆后会导致的判定错误**：把「放行」读成「没问题」→ 企业不整改，后续 entry 被拒时无预警无准备；把 Release with Comment 当无记录 → 漏掉它进入合规历史，误判该进口商过往「清白」、低估后续筛查风险。

### g05 · Detention — 扣留

- **英文术语**：Detention
- **中文译名**：扣留
- **IOM 定义**：
  > `6.9.21 – Detention`："A **temporary administrative action** taken by the FDA against articles offered for entry which are **not or appear not to be** in-compliance with the laws the FDA administers. Detained articles can be released if brought into compliance, or are refused entry or seized, if not brought into compliance." —— IOM 6.9.21 [p.52]
  - 中文自译：扣留是 FDA 对「不合规或**表面看来**不合规」的拟入境货物采取的**临时行政措施**；经整改达合规可放行，未达合规则被拒绝入境或扣押。
- **出处**：IOM 6.9.21 [p.52]；6.9.23 Detention and Hearing Process [p.52-53]、6.9.46 Import Status [p.55]、6.5.2.8 [p.41]。
- **与常识的差异**：三个限定词最关键——**temporary / administrative / "appear not to be"**（基于违规外观，非违规认定）；≠ Refusal of Admission（g08，Detention 可回转、Refusal 是 `final decision`）；≠ DWPE（g06，一般扣留通常伴随查验/取样证据）；≠ 流程终点（其后还有听证、举证、Reconditioning、复核、放行或拒绝）。
- **混淆后会导致的判定错误**：把扣留当「已判定不合格」→ 跳过听证与举证、直接出 Refusal；把扣留当流程终点 → 漏掉听证期、改标申请（FDA 766）、90 天出口/销毁、bond action，以及「FDA 档案保持开启」的义务。

### g06 · DWPE (Detention Without Physical Examination) — 免实物查验扣留

- **英文术语**：DWPE (Detention Without Physical Examination)
- **中文译名**：免实物查验扣留
- **IOM 定义**：
  > `6.9.22 – DWPE`："An action directed against specific products manufactured or shipped by specific foreign firms. 'Import Alerts' list products that may be detained without physical examination due to their violative history or potential." —— IOM 6.9.22 [p.52]
  > `6.9.6 – Audit Sample`（联动）："At least one FDA audit sample should be included as evidence when processing **removal** of a product, shipper, or country from DWPE." —— IOM 6.9.6 [p.51]
  - 中文自译：DWPE 是针对特定境外企业生产/发运的特定产品采取的扣留行动；Import Alerts 列出因违规历史或违规可能性而**可不经实物查验即予扣留**的产品；移除 DWPE 名单至少须一份 FDA 自采审核样品作为证据。
- **出处**：IOM 6.9.22 [p.52]、6.9.6 [p.51]、6.2.5.1 / 6.2.5.3 [p.21]、6.6.4.3 [p.44]。
- **与常识的差异**：★ 字面「不检查」极易误读为「不检查就放过」，**实际恰相反：不检查就扣住**（基于违规历史/外观，无需实物查验）；≠ Detention（g05，一般扣留通常需查验/取样证据）；≠ Import Alert（g17，Alert 是列名/指导文件，DWPE 是据此采取的行动）；触发 **DER** 而非 DTR（g07）；解除 DWPE 有硬性证据门槛（至少一份 **FDA** audit sample，非私人实验室报告）。
- **混淆后会导致的判定错误**：把 DWPE 当「免检放行」→ 放行本应自动扣留的货物、错过 DER 快速通道；把「企业自行送检合格」当解除条件 → 忽略 FDA 自采审核样品要求、DWPE 移除申请不成立；把 DWPE 与一般 Detention 混同 → 误要求现场查验、浪费资源且可能误放行。

### g08 · Refusal of Admission / Import Refusal — 拒绝入境

- **英文术语**：Refusal of Admission；Import Refusal
- **中文译名**：拒绝入境
- **IOM 定义**：
  > `6.9.44 – Import Refusal`："FDA's **final decision** that a detained shipment is in violation of FDA laws and regulations. A refused shipment must either be destroyed or exported under the supervision of CBP and the FDA **within 90 days** of the date of the Notice of FDA Action (Refusal Notice)." —— IOM 6.9.44 [p.55]
  > `6.5.2.8`："The 'Notice of FDA Action - Refusal of Admission' provides for the exportation or destruction of the shipment, under CBP supervision, within 90 days... **The FDA file remains open until the division receives notification indicating that the goods were either destroyed or exported.**" —— IOM 6.5.2.8 [p.41]
  - 中文自译：拒绝入境是 FDA 认定被扣货物违法的**终局决定**；须在通知日起 90 天内于 CBP 与 FDA 监督下出口或销毁；FDA 档案一直保持开启，直到收到销毁或出口的证明。
- **出处**：IOM 6.9.44 [p.55]、6.5.2.8 [p.41]、6.5.2.11 Bond Action [p.42]、6.6.4.1 第 7 步（CBP 4647）[p.43]。
- **与常识的差异**：≠ Detention（g05，Detention 临时可回转、Refusal 是 `final decision`）；★ **不是流程终点**——之后还有 90 天内出口/销毁、CBP 4647 红交货、销毁/出口核验、Bond Action，FDA 公共健康责任**延续到货物被销毁或出口为止**，档案不因发出通知而关闭；Refusal 通知上的 charge 须与原 Detained 通知**逐字一致**（6.5.2.8 [p.41]）；90 天（Refusal 后）≠ 30 天（FTH 下 CBP 4647 用于查验/取样的 redelivery 期限，6.6.4.1 [p.43]）；合格部分经 Reconditioning 放行时，不合格部分仍须单独出具 Refusal（6.5.2.5 [p.40]）。
- **混淆后会导致的判定错误**：发出 Refusal 即归档 → 未核验销毁/出口、未发 CBP 4647、错过 Bond Action 时效，违规货可能流入市场而 FDA 档案已关；把 90 天与 30 天混用 → redelivery 期限算错；把 Refusal 当 Detention → 误以为还可再给一次整改机会。

---

## 三、扣留分流与证据门槛

### g07 · DER vs DTR — 扣留建议的两种 work type（★ 成对，6.9 缺 DER）

- **英文术语**：DER (Detention without Physical Examination)；DTR (Detention Recommendation / All Other Detentions)
- **中文译名**：免实物查验扣留建议 / 其他一切扣留建议
- **IOM 定义**：
  > `6.2.5.1`："As an entry reviewer, you will use one of two work types to recommend detention: DER or DTR. **DER (Detention without Physical Examination): Use DER when a product is subject to Detention without Physical Examination (DWPE). DTR (All Other Detentions): Use DTR for all other situations where a product appears to be violative.**" —— IOM 6.2.5.1 [p.21]
  > `6.9.20 – Detention Recommendation (DTR)`："Used when review of the entry information cannot confirm that products being offered for import meet FDA's admissibility criteria. Examples include products in which the required registration, scheduled process filing, 510(k), or pre-market approval (PMA) cannot be verified at the entry review step." —— IOM 6.9.20 [p.52]
  - 中文自译：审查员向 Compliance Branch 推荐扣留时二选一：货物受 DWPE 约束 → DER；其余一切「看起来违规」（如无法核实注册、scheduled process filing、510(k)、PMA）→ DTR；DER 满足三项前提时可免索单据直接提交，若 Import Alert 要求特定证书（例 IA 28-02 印度黑胡椒）须先索取并审阅。
- **出处**：**IOM 6.2.5.1 [p.21]（DER 唯一定义处，6.9 无此条）**、6.2.5.3 [p.21-22]、6.2.5.4 [p.22]、6.2.5.2 [p.21]；IOM 6.9.20 [p.52]、6.2 第 418 行 "send a Detention Request (DTR)" [p.20]。
- **与常识的差异**：★ **不是严重度分级，而是「触发依据」分流**；★ 审查员提交的是 **recommendation / request（建议/请求）**、**不是终局扣留决定**，须交 Compliance Branch（6.2.5 [p.21]）；术语表口径不一致（6.9.20 称 Detention Recommendation、6.2 称 Detention Request、6.2.5 标题称 Detention Recommendations）；**6.9 完全没有 DER 条目**——只看术语表会以为只有一种扣留建议。
- **混淆后会导致的判定错误**：按「严重程度」选 work type → DWPE 货走 DTR（漏掉免单据快速扣留通道）或非 DWPE 货走 DER（错误免查验）；把建议当决定 → 审查员越权作出终局扣留、绕过 Compliance Branch；忽略「Alert 要求证书时须先索单据」→ DER 案卷证据不全、听证被击穿。

### g16 · Audit Sample — 审核样品

- **英文术语**：Audit Sample
- **中文译名**：审核样品
- **IOM 定义**：
  > `6.9.6 – Audit Sample`："A sample collected to **verify analytical results provided by a certificate of analysis, or private laboratory analysis** that purports to show a product complies with the FD&C Act and/or regulations. This sample type will usually be used with an import sample. **At least one FDA audit sample should be included as evidence when processing removal of a product, shipper, or country from DWPE.**" —— IOM 6.9.6 [p.51]
  - 中文自译：为核验 COA 或私人实验室「产品合规」分析结论而由 FDA 采集的样品；把产品/发货人/国家从 DWPE 名单移除时，至少须附一份 FDA 审核样品作为证据。
- **出处**：IOM 6.9.6 [p.51]（交叉引用 `IOM 4.1.4.2.8` 括号未闭合，见源层瑕疵节）、6.9.22 [p.52]、6.6.4.1 第 5 步 [p.43]。
- **与常识的差异**：★ ≠ 企业提交的 COA / 私人实验室报告——它恰恰是**用来核验这些外部结论的 FDA 自采样品**；≠ ADS（g15，补做原分析/加测）；≠ Private Laboratory（6.9.63 [p.57]）出具的结果；与 **DWPE 解除**强绑定，是硬性证据门槛（g06）。
- **混淆后会导致的判定错误**：把进口商提交的私人实验室合格报告当解除 DWPE 的证据 → 忽略「至少一份 FDA audit sample」、移除申请不成立；把 ADS 当 audit sample → 证据类型不符、案卷被退回。

---

## 四、违规模式与追责

### g11 · Failure to Hold — 未获放行即分销（★ 原文特意澄清）

- **英文术语**：Failure to Hold (FTH)
- **中文译名**：未获放行即分销
- **IOM 定义**：
  > `6.9.30 – Failure to Hold`："Failure to hold means that **the goods have been distributed by the importer/consignee without an FDA release from import status**. Such goods are usually subject to CBP's redelivery provisions." —— IOM 6.9.30 [p.53]
  > `6.6.4.1`（关键澄清，原文带 `*` 注）："***Please note that this is defined as distribution without a release, not merely moving the goods outside of the port area.**" —— IOM 6.6.4.1 [p.43]
  - 中文自译：Failure to Hold 指进口商/收货人在**未取得 FDA 解除进口状态的放行**之前已把货物分销；原文特别注明：定义要件是「无放行而分销」，**不是「货物被移出港区」**。
- **出处**：IOM 6.9.30 [p.53]；**IOM 6.6.4.1 [p.43]**（8 步清单）、6.6.4.2 / 6.6.4.3（健康危害、DWPE 加重）[p.43-44]。
- **与常识的差异**：★ 关键在**「分销」而非「位移」**——货物移出港区本身不构成该违规（原文特意加 `*` 注明），条件放行期内货物「may be moved」（6.9.13 [p.51]）；≠ Substitution（g12）；判定要件严格是「无 FDA release from import status 而分销」；加重分支（重大健康危害 / 仅达「违规外观」标准的 DWPE 情形）追加召回/收货人通知/公共警告协调；30 天 redelivery 窗口，区别于 Refusal 后的 90 天。
- **混淆后会导致的判定错误**：把「货物被移到港区外」即判 Failure to Hold → 误启动 8 步调查、CBP 4647 与保证金行动；反之把已分销误当「只是移库」→ 漏掉健康危害情形下的召回与公共警告协调、公共健康风险失控。

### g12 · Substitution — 调包

- **英文术语**：Substitution
- **中文译名**：调包
- **IOM 定义**：
  > `6.9.73 – Substitution`："An attempt by the importer/consignee to present goods to the FDA as corresponding to a particular entry when **they are in fact not the goods from that entry**. May occur as an attempt to hide distribution without an FDA release and avoid CBP bond actions." —— IOM 6.9.73 [p.58]
  > `6.6.4.4`："**Until it is determined otherwise, consider all substitution cases to involve distribution of the actual goods without FDA release.** (See IOM 6.6.4.1, FAILURE TO HOLD.)" —— IOM 6.6.4.4 [p.44]
  - 中文自译：进口商/收货人把并非某票报关项下的货物冒充该票货物提交给 FDA；常用于掩盖「无 FDA 放行即分销」并规避 CBP 保证金行动。在查明之前，一律先按 Failure to Hold 处理。
- **出处**：IOM 6.9.73 [p.58]、6.6.4.4 [p.44]、6.6.4.1 [p.43]。
- **与常识的差异**：≠ Importer/Filer Misdeclaration（g13，后两者是**申报数据**错误，Substitution 是**实物与报关对应关系**的伪造）；与 Failure to Hold（g11）是「手段—目的」关系、**默认按 FTH 处理直到查明**；举证硬要求（6.6.4.4 [p.44]）：须查验**整票**、照片 invaluable、须收集「隐瞒调包的证据」、差异说明作成 affidavit。
- **混淆后会导致的判定错误**：只核对单据不查实物 → 完全漏识别；只抽检部分货物 → 证据链被「未查验部分未调包」抗辩击穿；误归入 misdeclaration → 走错调查路径（filer evaluation 而非 8 步 FTH 清单 + CBP 4647 + bond 核定）。

### g13 · Importer Misdeclaration vs Filer Misdeclaration — 进口商误申报 vs 报关行误申报（★ 成对）

- **英文术语**：Importer Misdeclaration；Filer Misdeclaration
- **中文译名**：进口商误申报 / 报关行误申报
- **IOM 定义**：
  > `6.9.47 – Importer Misdeclaration`："Refers to **the importer's providing incorrect and/or incomplete information** to the FDA and CBP, usually via the filer. This misdeclaration may include incorrect product codes and/or product descriptions; incorrect/incomplete manufacturer/shipper name/address; and/or incorrect quantity and value." —— IOM 6.9.47 [p.55]
  > `6.9.35 – Filer Misdeclaration`："Refers to **the importer's provision of correct information to the filer, who then files an erroneous entry** to the FDA and CBP." —— IOM 6.9.35 [p.54]
  > `6.6.4.6`："Although this section is oriented to filer interventions, it must always be recognized that **the filer is the agent of the importer, and the importer is ultimately responsible.**" —— IOM 6.6.4.6 [p.45]
  - 中文自译：分界唯一标准是**错误信息源自谁**——进口商给 filer 的信息本身就不正确/不完整 → Importer Misdeclaration；进口商给的信息正确、但 filer 录入/申报出错 → Filer Misdeclaration。
- **出处**：IOM 6.9.47 [p.55]、6.9.35 [p.54]；6.6.4.5 [p.44-45]、6.6.4.6 / 6.6.4.6.1 [p.45]、6.7 Filer Evaluations [p.45]。
- **与常识的差异**：★ 不是「谁被处罚」的分类，而是**错误来源**的分类，且即便 filer 出错**进口商仍负最终责任**（6.6.4.6）；后续路径不同：Filer Misdeclaration 连到 6.7 periodic filer evaluation 与 6.6.4.6.1 Repeated Filer Misdeclaration，Importer Misdeclaration 走进口调查；≠ Substitution（g12，实物层面）；任何影响 PREDICT 的字段错误都必须更正 → 指派责任方 → 保存 → rescreen（g19）。
- **混淆后会导致的判定错误**：错分责任源 → 对进口商启动 filer evaluation（对象错）或漏掉对 filer 的 Repeated 处置；误以为 filer 出错可免除进口商责任 → 追责对象缺失；更正数据后忘记 rescreen → 后续判定建立在脏数据上。

### g10 · Bond Action / Redelivery Bond — 保证金行动 / 重新交付保证金

- **英文术语**：Bond Action；Redelivery Bond (AKA Entry Bond)
- **中文译名**：保证金行动 / 重新交付保证金
- **IOM 定义**：
  > `6.9.11 – Bond Action`："Action taken by **Customs** resulting in forfeiture of all, or a portion of, an entry bond when an importer fails to redeliver merchandise covered by such a bond." —— IOM 6.9.11 [p.51]
  > `6.9.66 – Redelivery Bond (AKA Entry Bond)`："A bond posted by the importer of record with CBP. For FDA-regulated products, this is currently in the amount of **three times the value of the imported product**, to insure redelivery of the product for examination, reconditioning, export, or destruction." —— IOM 6.9.66 [p.57]
  > `6.5.2.11`："Bond actions are taken when an entry is **distributed prior to FDA release and cannot be redelivered**, or when an article has been **detained and refused, and the article is not destroyed or exported** in accordance with the requirements of the law." —— IOM 6.5.2.11 [p.42]
  - 中文自译：Redelivery Bond 是 importer of record 向 CBP 提交、金额为货值 3 倍的保证金，担保货物可被重新交付以接受查验、重整、出口或销毁；Bond Action 则是当进口商未能重新交付时**由 CBP** 没收全部或部分保证金（liquidated damages）的行动。
- **出处**：IOM 6.9.11 [p.51]、6.9.66 [p.57]、6.5.2.11 [p.42]（引 FD&C Act §801(b)、19 CFR 113.62、21 CFR 1.97(b)）、6.3.11 [p.32]。
- **与常识的差异**：**Redelivery Bond = 工具/法定义务**（所有条件放行货物必附）；**Bond Action = CBP 的执行动作**——二者不是同义词，也不是「罚款」与「保证金」的关系；**主体是 CBP 不是 FDA**，且 CBP 减轻已核定损害通常须 FDA 完全同意（21 CFR 1.97(b)）；两个触发情形（放行前已分销且无法 redeliver = FTH 后果 / 已扣留并拒绝但未按期销毁出口 = Refusal 后果）；≠ Supervisory Charges（6.9.74 [p.58]，21 CFR 1.99）。
- **混淆后会导致的判定错误**：把 bond 当「FDA 开的罚款」→ 找错责任主体与救济（减免）路径；以为发出 Refusal 即自动完结 → 漏掉 Bond Action 与 liquidated damages 时效；把保证金与监督费用混记 → 费用核算与文书（FDA 790）错配。

---

## 五、文书与程序

### g24 · Notice of FDA Action — FDA 行动通知

- **英文术语**：Notice of FDA Action (NOA)
- **中文译名**：FDA 行动通知
- **IOM 定义**：
  > `6.9.57 – Notice of FDA Action`："Gives notice to the owner, operator, or agent-in-charge of an imported product, providing more specific information on the actions taken by the agency, **broken down by each entry line** (including, 'sample collected,' 'intended for sampling,' 'detained,' 'released,' or 'refused'). The notice provides notification of **the right to a hearing** on the detention of a product which appears violative to the FDA... The notice **identifies the charges** for which the product appears violative." —— IOM 6.9.57 [p.56]
  > `6.1.6.2`："FDA Import Systems will generate a 'Notice of FDA Action'... **As the status changes for a particular line, a new 'Notice of FDA Action' will be issued**" —— IOM 6.1.6.2 [p.13]
  - 中文自译：按每个 entry line 逐项告知 FDA 已采取动作（已取样 / 拟取样 / 扣留 / 放行 / 拒绝）的通知；扣留版本同时告知听证权并列出指控（charge）；状态每变化一次就出具新通知；抄送 filer、importer of record、consignee。
- **出处**：IOM 6.9.57 [p.56]、6.1.6.2 [p.13]、6.5.2.8（Refusal 版 charge 须与 Detained 版逐字一致）[p.41]、6.3.10.7（Remarks 不出现在通知上）[p.32]、6.2 第 439 行（narrative 字段出现在公开版）[p.20]。
- **与常识的差异**：★ ≠ 单一「扣留通知」——是**按 line 逐项、随状态变化反复出具**的系列通知（状态值有 5 类）；扣留版本同时是**听证权告知**与 **charge 列明**载体（与 g25 联动），Refusal 版 charge 必须与原始 Detained 版逐字一致；**Remarks 字段不出现在 NOA 上**（6.3.10.7 [p.32]），但 narrative 字段会出现在**公开版**通知（6.2 第 439 行 [p.20]）。
- **混淆后会导致的判定错误**：把一次通知当全流程唯一文书 → 漏掉状态变更后的新通知、漏掉按 line 拆分；把关键放行理由写进 Remarks 以为会送达进口商 → 正式通知中无据、听证无法辩护；charge 前后不一致 → Refusal 程序瑕疵。

### g25 · Detention and Hearing Process / Testimony — 扣留听证程序 / 证言

- **英文术语**：Detention and Hearing Process；Testimony；Affidavit
- **中文译名**：扣留听证程序 / 证言 / 宣誓书
- **IOM 定义**：
  > `6.9.23 – Detention and Hearing Process`："The opportunity for an importer or designee to **present evidence, or testimony, to overcome the appearance of a violation** and to give the FDA confidence that the product is in compliance... **The evidence must be provided during the hearing period.** The format for providing this evidence may vary from **a series of email or telephone conversations to a more formal meeting**." —— IOM 6.9.23 [p.52-53]
  > `6.9.75 – Testimony`："An individual's statement given in writing (such as an affidavit or a declaration) or by appearance under oath at a proceeding... Testimony may also be **information a firm submits to overcome the appearance of the violation**, or to otherwise support the release of their product. Testimony should be provided to the contact listed on the FDA Notice of Action, which is usually a **compliance officer**." —— IOM 6.9.75 [p.58]
  - 中文自译：听证是进口商在**听证期内**提交证据/证言以推翻「违规外观」的机会，形式可从一串邮件/电话到较正式会议，属非正式程序；Testimony 范围很宽（书面 affidavit/declaration、出庭宣誓、邮件、电话、传真、硬拷贝）；接收方通常是 Notice of Action 上列名的 compliance officer。
- **出处**：IOM 6.9.23 [p.52-53]、6.9.75 [p.58]、6.9.3 Affidavit [p.50]；6.9.57（通知告知听证权）[p.56]、6.6.4.1 第 5 步（说明作成 affidavit）[p.43]。
- **与常识的差异**：★ "hearing" 是**非正式**程序（informal meeting，甚至一串邮件/电话），≠ 行政法庭式听证，但**证据必须在听证期内**提交、逾期不补；举证目标是 "overcome the **appearance** of a violation"（与 Detention 的外观标准一致），不是证明「绝对合格」；Testimony ≠ 仅出庭作证（affidavit / declaration / 邮件 / 电话 / 传真 / 硬拷贝都算，affidavit 须向 FDA 授权官员宣誓、affiant 须对货物移动或状况有实质事实认知）；接收方是 **compliance officer**，不是 entry reviewer。
- **混淆后会导致的判定错误**：按正式听证准备 → 错过 informal 窗口期、证据逾期失权；把 testimony 只理解为出庭作证 → 漏掉书面 affidavit/declaration 这一主要举证形式；把材料发给审查员而非 compliance officer → 未进入案卷、视为未举证。

### g09 · Reconditioning / Relabeling — 重整 / 改标

- **英文术语**：Reconditioning；Relabeling
- **中文译名**：重整 / 改标
- **IOM 定义**：
  > `6.9.65 – Reconditioning`："When a product is detained because it violates FDA laws and regulations, **the importer of record may submit an application to the agency requesting permission** to re-label or recondition the product in an attempt to bring it into compliance." —— IOM 6.9.65 [p.57]
  > `6.9.68 – Relabeling`："The process of modifying labeling in order to come into compliance with FDA regulations. **Relabeling is considered a form of reconditioning.**" —— IOM 6.9.68 [p.57]
  - 中文自译：货物因违规被扣后，须由 **importer of record** 向 FDA **提交申请**（获批准并在监督下）以改标或重整使其达合规；改标是重整的一种形式。批准后复核，合格部分以「Released after Reconditioning」放行，不合格部分仍须销毁/再出口并单独出具拒绝通知。
- **出处**：IOM 6.9.65 / 6.9.68 [p.57]、6.5.2.4 / 6.5.2.5 / 6.5.2.6 [p.40]、6.9.74 Supervisory Charges [p.58]；表单 Form FDA 766 + bond（Exhibit 6-2，需查原件）。
- **与常识的差异**：★ ≠ 企业自行返工——须 **importer of record 申请 → FDA 批准并监督**，未经批准的自行整改**不产生放行效力**；申请主体是 **importer of record**（g14），不是 FSVP Importer，也不是境外生产商；**改标 ⊂ 重整**，不是并列动作；复核后「部分放行」时不合格部分仍须销毁/再出口 + 单独 Refusal（g08）；重整失败原则上不给第二次机会，除非修订后的方法能合理保证成功（6.5.2.6 [p.40]）。
- **混淆后会导致的判定错误**：把企业自行整改当合规完成 → 误放行；找错申请/签字主体（用 FSVP Importer 或境外厂商）→ 申请无效；把「部分放行」当整票放行 → 漏掉对不合格部分的销毁/出口与单独 Refusal、违规货流入市场。

### g18 · Prior Notice of Imported Foods — 进口食品事先通知

- **英文术语**：Prior Notice of Imported Foods (Prior Notice)
- **中文译名**：进口食品事先通知
- **IOM 定义**：
  > `6.9.62`："In the case of an article of food that is being imported or offered for import into the United States, a notice provided to the **FDA prior to entry**... with information about the article, manufacturer, shipper, grower, the country of origin, and anticipated port of entry. Prior notice must be submitted to the FDA **electronically, via either the CBP ACE or the FDA PNSI**." —— IOM 6.9.62 [p.57]
  > `6.1.5`（时限）："**Two hours** before arrival by land by road / **Four hours** before arrival by air or by land by rail / **Eight hours** before arrival by water" —— IOM 6.1.5.1 [p.9]
  - 中文自译：食品/动物饲料抵达前须向 FDA（经 CBP ACE 或 FDA PNSI）电子提交、含 15 项信息（21 CFR 1.281）并取得确认的独立预先通报；时限按运输方式为抵达前 2 / 4 / 8 小时；通报不充分本身即可构成拒绝与扣留理由。
- **出处**：IOM 6.9.62 [p.57]、6.1.5 / 6.1.5.1–6.1.5.6 [p.9]–[p.12]（6.1.5.4 列 15 项必填信息 [p.10-11]、6.1.5.5 inadequate → refusal and holding [p.11-12]）。
- **与常识的差异**：★ ≠ 报关单的一部分——是**发给 FDA**、有电子确认回执的**独立法定前置义务**，只是可搭 ACE 通道传输；时限是「抵达**前**」2/4/8 小时，不是抵达后补交、也不是统一 8 小时；仅适用于 **food / animal feed**（6.1.5 标题），不是所有 FDA 监管商品；有豁免/排除清单（6.1.5.3 [p.10]）与 IFE 特殊情形；Inadequate Prior Notice 本身即 refusal 理由，不需先证明产品不合格。
- **混淆后会导致的判定错误**：以为随报关单一起提交即可 → 未在法定时限内单独向 FDA 提交、货物被拒；把 2/4/8 记成统一时限或「抵达后」→ 时限判定错误；把 Food 之外商品套用或把豁免清单漏判 → 适用性判定错误；忽略 inadequate → 未及时出 Refusal / holding。

---

## 六、主体与身份

### g14 · FSVP (and/or HACCP) Importer vs Importer of Record — FSVP 进口商 vs 报关登记进口商（★ 成对）

- **英文术语**：FSVP and/or HACCP Importer；Importer of Record
- **中文译名**：FSVP 进口商 / 报关登记进口商
- **IOM 定义**：
  > `6.9.40 – FSVP and/or HACCP Importer`："The importer who, for a specific food, is subject to the importer requirements in FDA's FSVP regulation (21 CFR part 1, subpart L)... the importer is the **U.S. owner or consignee at the time of entry** into the United States or the **U.S. agent or representative** of the foreign owner or consignee... **An FSVP or HACCP importer must be physically located in the United States.**" —— IOM 6.9.40 [p.55]
  > `6.9.43 – Importer of Record`："The party **in whose name the entry is made**. Note that... a Customs House Broker might make an entry and become the 'importer of record' by using their importer ID and bond on behalf of their client, the true 'importer' of the goods. For FDA purposes, the 'importer of record' is the person or company **filing the redelivery bond** under Sections 802(b) and 536(b)." —— IOM 6.9.43 [p.55]
  - 中文自译：FSVP Importer 是 FSMA / 21 CFR 1 Subpart L（或 juice/seafood HACCP）下对境外供应商履行验证义务、须接受 FDA 记录审查的主体，须为入境时点的美国 owner/consignee 或其 U.S. agent/representative，且**必须位于美国境内**；Importer of Record 是 CBP 报关名义主体，报关行可用自己的 ID 与 bond 代为成为，FDA 语境下即提交 redelivery bond 者。
- **出处**：IOM 6.9.40 / 6.9.43 [p.55]、6.8.3.1.1（检查时逐产品验证 importer 定义）[p.50]、6.8 第 68 行（Very Small Importer, VSI）[p.47]；对照 6.9.65 Reconditioning 申请主体、6.9.66 bond 主体。
- **与常识的差异**：★ **两套法律身份、两个法域**——Importer of Record 属 CBP（报关/关税/保证金），FSVP Importer 属 FSMA（供应商验证/记录审查），**二者常非同一人**；**Reconditioning 申请主体 = importer of record**（6.9.65）、**FSVP 检查对象 = FSVP importer 的记录**（6.8）；`must be physically located in the United States` 是硬约束，境外货主不能直接当 FSVP importer；还有 HACCP importer（21 CFR 120.14 / 123.12）、VSI 变体。
- **混淆后会导致的判定错误**：把报关行当 FSVP 义务人 → FDA 483a / T-EIR 开错对象、记录审查无的放矢；把 Importer of Record 当 Reconditioning 申请人 → 找错签字与 bond 主体；忽略「须位于美国境内」→ 把境外货主误列为 FSVP importer、检查结论不成立。

---

## 七、申报数据与系统

### g19 · PREDICT — 预测性风险筛查系统

- **英文术语**：PREDICT (Predictive Risk-Based Evaluation for Dynamic Import Compliance Targeting)
- **中文译名**：预测性风险筛查系统
- **IOM 定义**：
  > `6.9.61 – PREDICT`："A **risk-based analytics tool** that the FDA uses to **electronically screen all regulated shipments** imported or offered for import into the United States." —— IOM 6.9.61 [p.57]
  > `6.2.2.1`："This system includes PREDICT, a screening tool that helps **identify high-risk shipments**. PREDICT does this by analyzing: [risk score, mashup grid, rule flags]" —— IOM 6.2.2.1 [p.16]
  - 中文自译：PREDICT 是 FDA 对所有拟入境监管货物进行电子风险筛查的分析工具，输出风险评分、mashup grid 与规则标记，用于识别高风险货物。
- **出处**：IOM 6.9.61 [p.57]、6.2.2.1 [p.16]、6.2 第 53/71/83/176/196/211 行 [p.14]–[p.17]、6.2.5.2 [p.21]、6.2.5.3 第 539 行 "Update and **rescreen** the entry if you make corrections" [p.22]、6.1.7 VQIP [p.13]。
- **与常识的差异**：★ **≠ 自动判决**——是审查的**输入**，不是可采性决定；审查员可作出与 PREDICT 相悖的 May Proceed，但**必须写明具体理由**（6.2 第 83/176 行 [p.15]/[p.17]）；必须与电子/纸质单据、Import Alert、历史合规记录**合用**，不能只凭其中一项；**数据脏 → 筛查失真**：任何影响筛查的字段错误（制造商、发货人、产品代码、数量）须更正 → 指派责任方 → 保存 → rescreen；≠ May Proceed（g02）；VQIP 通过在 PREDICT 中设筛查规则识别获批申请（6.1.7 [p.13]）。
- **混淆后会导致的判定错误**：把高风险评分当「已判定违规」→ 跳过人工审查与举证；把自动放行/低分当「FDA 已判定合规」→ 忽略 May Proceed 未作合规判定；更正数据后忘记 rescreen → 后续所有判定建立在脏数据上；相悖放行不写理由 → 违反 6.2 明令、案卷不可辩护。

### g20 · Affirmation of Compliance (A of C) vs Intended Use Code (IUC) — 合规申明 vs 用途代码（★ 成对，6.9 缺 IUC）

- **英文术语**：Affirmation of Compliance (A of C)；Intended Use Code (IUC)
- **中文译名**：合规申明 / 用途代码
- **IOM 定义**：
  > `6.9.4 – A of C`："**Data elements transmitted to FDA electronically that affirm a product meets a specific FDA regulation.** This value is provided to help expedite the FDA's review of product compliance in making an admissibility decision at time of entry. Some affirmations require a qualifier, which are numeric or alpha-numeric values representing a specific firm, product, certification, registration, application, or other value often on file with the FDA." —— IOM 6.9.4 [p.51]
  > `6.1.6.2`（IUC 唯一定义处）："FDA's system enhancements include establishing **Intended Use Codes (IUC) to assist entry reviewers in determining the end-use of the imported product**. Commodities will fall in one of the three categories: IUC is required / optional / not applicable... **A of C code requirements are dependent on the commodity being imported and can be impacted by the IUC.**" —— IOM 6.1.6.2 [p.13]
  - 中文自译：A of C 是 filer 电子传输、申明产品符合某项具体 FDA 法规的数据元素，可带 qualifier（企业/产品/认证/注册/申请号）；IUC 是帮助审查员判定进口产品最终用途的代码，按商品分「必需/可选/不适用」三类；**A of C 的适用要求会被 IUC 影响**。
- **出处**：IOM 6.9.4 [p.51]；**IOM 6.1.6.2 [p.13]（IUC 唯一定义，6.9 无此条）**；6.1 IFE 段（须同时具备 IUC "Import for Export" 与 IFE A of C）[p.9]、6.2 第 231/243 行 [p.17]、6.3 第 24 行（禁止仅凭 A of C 缺失扣留）[p.23]、6.9.64 Product Code [p.57]。
- **与常识的差异**：★ 看似元数据，**实为可采性判定依据**，且 **IUC 会改变 A of C 的要求**——二者不是独立字段，须联动校验；★ **但不能仅凭 A of C 缺失就扣留**（6.3 第 24 行 [p.23] 明确否定 "detention based solely on a failed data lookup or missing Affirmation of Compliance data"），且系统自动校验通过时不得再人工复核 A of C（6.2 第 243 行 [p.17]）；≠ Product Code（6.9.64 [p.57]，5–7 位字母数字码）；**6.9 未收 IUC**。
- **混淆后会导致的判定错误**：把 A of C / IUC 当无害元数据 → 填错不更正、不 rescreen，PREDICT 与后续判定全错；反过来仅因 A of C 缺失就扣留 → 违反 6.3 明确禁止的做法；把 IUC 与 A of C 当独立字段分别校验 → 漏掉用途变更引发的合规要求变化（如 IFE 情形，6.1 [p.9]）。

### g21 · ITACS — 进口贸易辅助通信系统

- **英文术语**：ITACS (Import Trade Auxiliary Communication System)
- **中文译名**：进口贸易辅助通信系统
- **IOM 定义**：
  > `6.9.50 – ITACS`："A system that provides the **import trade community** with four functions: the ability to check the status of FDA-regulated entries and lines, the ability to submit entry documentation electronically, the ability to electronically submit the location of goods availability for those lines targeted for FDA exam, and the ability to check the estimated laboratory analysis completion dates... ITACS account management functionality enables the electronic distribution of **Notices of FDA Action** via email and as downloads." —— IOM 6.9.50 [p.56]
  - 中文自译：面向进口贸易界提供四项功能的对外系统：查 entry/line 状态、电子提交单据、报送待查验货物的可用地点、查询取样行的实验室预计完成日期；并支持以邮件/下载方式分发 Notice of FDA Action。
- **出处**：IOM 6.9.50 [p.56]、6.9.27 Entry Documents [p.53]、6.2.2.1 第 146 行（ITACS 提交单据获初审优先）[p.16]、6.2 第 387/401-402/506 行（系统外收到单据须上传）[p.20]/[p.21]、6.1.6.2 [p.13]、6.3 第 442 行 [p.30]。
- **与常识的差异**：★ ≠ FDA 内部审查系统——PREDICT / OASIS / SERIO（6.9.31 [p.53-54]）是 FDA 侧，**ITACS 是对外接口**，使用方是 filer / 进口贸易界；但单据经 ITACS 提交会获得**初审排序优先**（6.2.2.1 [p.16]），系统外收到的单据**必须回传进 FDA Import System**（6.2 第 506 行 [p.21]）；**名称不一致**：6.9.50 标题作 `…Communication System`（单数），6.9.27 / 6.2 / 6.4 正文多处作 `…Communications System`（复数）。
- **混淆后会导致的判定错误**：把 ITACS 当审查决策系统 → 误以为「单据一提交即被审查/放行」；忽略 ITACS 提交优先 → 排程判断错误；把单复数名称差异当两个系统 → 检索与交叉引用漏项；系统外单据未上传 → 案卷缺件。

### g22 · OGA / PGA — 其他政府机构 / 合作政府机构

- **英文术语**：Other Government Agency (OGA)；Partnering/Partner Government Agencies (PGA)
- **中文译名**：其他政府机构 / 合作政府机构
- **IOM 定义**：
  > `6.2.2.2.6`："Use the OGI (Other Government Agency - Investigations) and OGC (Other Government Agency - Compliance) work types to **close an entry line without the FDA making an admissibility decision**. This is done when another government agency is handling the entry." —— IOM 6.2.2.2.6 [p.19]
  > `6.2` 第 105 行："Note: **Other Government Agencies (OGAs) are also known as Partnering Government Agencies (PGAs).**" —— IOM 6.2 第 105 行 [p.15]
  - 中文自译：OGA 与 PGA 指同一批机构（含 CBP 等，FDA 自身也以 FD1/FD2/FD3 flags 列为 PGA 之一）。OGA Referral 用 OGI / OGC 两种 work type，在**其他机构处理该票时让 FDA 不作可采性判定即关闭该 line**；Ad-Hoc 型只共享信息、不关闭 line。
- **出处**：**IOM 6.2.2.2.6 [p.19]**、6.2 第 93/103/105/114 行 [p.15]、6.1 第 93-94 行（PGA/OGA、OCI）[p.7]、6.1.6.2 第 378/402-403 行（PGA flags、46 个 PGA）[p.12]。
- **与常识的差异**：★ **OGA = PGA 是同一批机构**，不是两类；展开词不统一（6.1 `Partner` / 6.2 `Partnering`），FDA 自己也是 PGA 之一；★ **OGA Referral 的法律后果是「FDA 不作可采性判定就关闭 line」**——不是「转交协查，FDA 仍会出决定」；**Ad-Hoc OGA Referral 不关闭 line**（6.2 第 349 行 [p.19]），仅共享信息、FDA 仍作初始判定；OGI → Investigations Branch (**IB**)、OGC → Compliance Branch (**CB**)（见 g04 缩写）；关闭前须上传证明其他机构已如何处置货物的文件。
- **混淆后会导致的判定错误**：把 OGA Referral 当普通协查 → 误以为 FDA 仍会出可采性判定，结果 line 被关闭、无 FDA 决定；Ad-Hoc 与关闭型混用 → 该关的没关、不该关的被关；把 FDA 排除在 PGA 之外 → FD1/FD2/FD3 flags 归属判断错误。

### g23 · VQIP / QAP — 自愿合格进口商计划 / 质量保证计划

- **英文术语**：VQIP (Voluntary Qualified Importer Program)；QAP (VQIP Quality Assurance Program)
- **中文译名**：自愿合格进口商计划 / 质量保证计划
- **IOM 定义**：
  > `6.1.7`："The Voluntary Qualified Importer Program (VQIP) is a **voluntary, fee-based** program that provides **expedited review**... The FDA works with CBP to expedite entry of VQIP foods... The agency sets screening in its **PREDICT** import screening system to recognize shipments of food that are the subject of an **approved VQIP application**... The FDA **limits** its examination and/or sampling of VQIP food [to] obtain statistically necessary risk-based microbiological samples, and to **audit the effectiveness of VQIP**." —— IOM 6.1.7 [p.13]
  > `6.9.76 – VQIP Quality Assurance Program (QAP)`："A compilation of the written policies and procedures used to ensure adequate control over the safety and security of the foods being imported by the VQIP importer." —— IOM 6.9.76 [p.58]
  - 中文自译：VQIP 是自愿、付费的快速审查计划，经**获批申请**后由 PREDICT 设规则识别；FDA 仍保留为公共卫生理由查验/取样、统计性微生物取样与审计 VQIP 有效性的权利。QAP 只是 VQIP 要求的一套书面政策与程序汇编。
- **出处**：**IOM 6.1.7 [p.13]（VQIP 本体定义，6.9 无此条）**、6.9.76 [p.58]（仅 QAP）、6.1 第 137 行（PNSI）[p.8]。
- **与常识的差异**：★ **不是合规认证、不是豁免**——是「加速审查」资格，FDA 仍可为公共卫生理由查验/取样；且须有 **approved application** 且 PREDICT 已设识别规则；**QAP ≠ VQIP**（6.9 只收了 QAP，极易误以为「VQIP 就是那套文件」），文件齐备 ≠ 已获批；通过 PREDICT 规则识别（与 g19 联动），不是人工豁免名单；仅针对 **food**（6.1.7 标题 Entry Processing）。
- **混淆后会导致的判定错误**：把 VQIP 当「免检资格」→ 误以为可跳过 Prior Notice / 可采性判定 / 取样；把 QAP 文件齐备当「已获 VQIP 批准」→ 忽略 approved application 与 PREDICT 识别规则、误给加速待遇。

---

## 八、样品与证据链

### g15 · SDI vs ADS (vs DI Sample) — 特殊国内进口样品 vs 附加样品（★ 成对，6.9 缺 SDI）

- **英文术语**：Special Domestic Import Sample (SDI)；Additional Sample (ADS)；Domestic Import (DI) Sample
- **中文译名**：特殊国内进口样品 / 附加样品 / 放行后国内进口样品
- **IOM 定义**：
  > `6.4.9 – SDI`："The SDI sample work type should **only** be used when directed by a special sampling assignment, for certain perishable products collected for metal (MET) analysis or for products collected for nutritional analysis (NIS). **It should not be used when collecting samples for multiple PAFs, or if the product appears to be violative or has a history of being violative.**" —— IOM 6.4.9 [p.37]
  > `6.4.8 – ADS`："An additional sample (referred to as 'ADS' in FDA Import Systems) is a physical sample collected from a **previously sampled lot**... Additional import samples will have a **different sample number** from the original sample number... **The additional sample must be collected from the same entry line as originally sampled.**" —— IOM 6.4.8 [p.37]
  > `6.9.24 – DI Sample`："A sample of an imported article collected **after it has been released from import status**." —— IOM 6.9.24 [p.53]
  - 中文自译：ADS 是对**已取样批次的同一 entry line** 补采/加测的样品（样品号不同、须在 Remarks 关联原号）；DI Sample 是货物**已脱离进口状态后**才采集的进口货样品；SDI 是特殊抽样任务下、针对特定易腐品 MET/NIS 分析的国内进口样品，且明文禁止用于多 PAF 或已显违规/有违规史的产品。
- **出处**：**IOM 6.4.8 / 6.4.9 [p.37]**、6.4 第 59-60 行（ADS 须记同一 entry/line）[p.33]、6.5 第 11-32 行（SDI 额外要求）[p.39]；6.9.2 [p.50]、6.9.24 [p.53]。
- **与常识的差异**：★ 三者是**不同维度**，不是同义/递进关系（ADS = 补样同批同行 / DI = 放行后取样时点 / SDI = 特殊任务下用途 + 任务前提）；**SDI ≠ DI Sample 的缩写**——SDI 有独立适用前提且要求更严的证据（标签描述、官方封条 FDA 415a、采集人 ID），目的是 FDA 检出违规时**启用国内管辖权**；**6.9 术语表只收了 Additional Sample 与 DI Sample，没有 SDI**；SDI 明文禁用于「已显违规 / 有违规史」产品，靠 "special sampling assignment 指令" 限定；ADS 必须与原样同一 entry/line。
- **混淆后会导致的判定错误**：把 SDI 当普通补样 → 对已显违规产品误用该 work type、丢失国内管辖权证据链（封条/采集人 ID）、后续无法在国内追责；把 ADS 当全新样品 → 样品号与 entry/line 关联断裂、实验室结果无法并入原案；把「放行后取样」(DI) 与「放行前取样」混同 → 误判 FDA 管辖权基础。

---

## 九、情报来源

### g17 · Import Alert vs Import Bulletin — 进口警报 vs 进口通报（★ 成对，6.9 缺 Bulletin）

- **英文术语**：Import Alert (IA)；Import Bulletin (IB)
- **中文译名**：进口警报 / 进口通报
- **IOM 定义**：
  > `6.9.42 – Import Alerts`："Guidance documents concerning significant re-occurring, new, or unusual problems affecting import coverage. They can be found online here." —— IOM 6.9.42 [p.55]
  > `6.9.22 – DWPE`（补足 Alert 的实际效力）："'Import Alerts' list products that **may be detained without physical examination** due to their violative history or potential." —— IOM 6.9.22 [p.52]
  - Import Bulletin **6.9 无条目**；正文线索：`6.2` 情报来源清单 "Import Alerts (IA) and **Import Bulletins (IB)**" [p.15]；`6.2.2.2.x` "An **Import Bulletin directs you to do so**"（请求现场工作）[p.17]；`6.2.2.2.x` "**Import Alerts (IA): Do not routinely request work for a line that is already subject to an Import Alert.**" [p.17]。
  - 中文自译：Import Alert 是列名「因违规历史/可能性可免实物查验扣留」的产品/企业的指导文件；Import Bulletin 是**指示审查员对某 line 请求现场工作/查验**的指导文件。本章未给 Bulletin 正式定义，须由正文用法反推。
- **出处**：IOM 6.9.42 [p.55]、6.9.22 [p.52]；**6.2.2.2.x [p.15]/[p.17]、6.2.5.3 [p.21-22]、6.3 [p.31]**、6.4 第 266 行 [p.37]。
- **与常识的差异**：★ **Import Alert (IA)** 关联 **DWPE / DER**——命中后「不要例行请求现场工作」、走 DER 免查验扣留（g06/g07）；★ **Import Bulletin (IB)** 是**指示请求现场工作**的文件、**不触发 DWPE**；方向几乎相反（Alert → 别再查、直接扣；Bulletin → 去查）；6.9.42 措辞偏弱（"guidance documents... can be found online here"）**不能单读**，必须与 6.9.22 + 6.2.5.3 合读才能看到强制扣留效力；**★ 缩写陷阱**：IB 同时是 Import Bulletin **和** Investigations Branch（g04），「IB Release」属后者；DER 免单据提交的前提之一是「电子数据匹配 Import Alert 条件」，若 Alert 要求特定证书（如 IA 28-02）仍须先索单据（6.2.5.3 [p.21-22]）。
- **混淆后会导致的判定错误**：把 Bulletin 当 Alert → 对未受 DWPE 覆盖的货物误走 DER 免查验扣留；把 Alert 当 Bulletin → 对已受 DWPE 约束的货物又去请求现场查验（6.2 明确禁止）、浪费资源且可能误放行；把 "IB Release" 读成「按 Import Bulletin 放行」→ 完全找错文书与流程。

---

## 十、法定例外与边界

### g26 · Re-export — 再出口

- **英文术语**：Re-export
- **中文译名**：再出口
- **IOM 定义**：
  > `6.9.67 – Re-export`："A term used to identify goods shipped out of the United States **after being offered for entry**. This is **not the same as an export of U.S. manufactured goods** and is **not covered by the restrictions in Section 801(e)** of the FD&C Act." —— IOM 6.9.67 [p.57]
  - 中文自译：指货物**已申报入境之后**又运出美国；不同于美国制造品的出口，且**不适用** FD&C Act §801(e) 的出口限制。
- **出处**：IOM 6.9.67 [p.57]；对照 6.9.1 AGR [p.50]、6.9.44 / 6.5.2.8（Refusal 后出口）[p.55]/[p.41]。
- **与常识的差异**：与 "export" 的法律后果完全不同——Re-export 是「已申报入境后又运出」的外国货（常见于 Refusal 后处置），**不适用 §801(e)** 对美国制造品出口的限制；与 **AGR**（g27）方向相反却同属法定例外：AGR 是「美国货出去又回来」**被视为进口**（§801(d)(1)），Re-export 是「外国货进来又出去」**不受 §801(e) 约束**。
- **混淆后会导致的判定错误**：把 Refusal 后的再出口当普通出口 → 误套 §801(e) 限制、错开文书；把 AGR 与 Re-export 混用 → §801(d)(1) 与 §801(e) 适用颠倒、审查范围错判。

### g27 · American/US Goods Returned (AGR / USGR) — 美国货退回

- **英文术语**：American/US Goods Returned (AGR or USGR)
- **中文译名**：美国货退回
- **IOM 定义**：
  > `6.9.1 – AGR`："Goods produced in the U.S. which are exported, and then returned to the United States. **They are considered imports.** (See Sec. 801(d)(1) of the FD&C Act [21 U.S.C. 381])." —— IOM 6.9.1 [p.50]
  - 中文自译：美国生产、出口后又返回美国的货物，**在法律上被视为进口货物**，适用 §801(d)(1)。
- **出处**：IOM 6.9.1 [p.50]（6.9 首条）；对照 6.9.67 Re-export [p.57]。
- **与常识的差异**：★ 常识以为「国货返销不算进口」，作者明确 `They are considered imports` 并挂 §801(d)(1)；与 **Re-export**（g26）是方向相反的两条例外，须成对记忆。
- **混淆后会导致的判定错误**：把 AGR 排除在入境审查外 → 漏掉 Prior Notice / 可采性判定 / 取样；把 AGR 与 Re-export 混用 → §801(d)(1) 与 §801(e) 适用颠倒。

---

## 附：成对易混概念速查矩阵

| # | 成对概念 | 分界判据（一句话） | 混淆后的典型判定错误 | 条目 |
|---|---|---|---|---|
| 1 | **DER vs DTR** | 触发依据（受 DWPE/IA 约束 → DER；其余无法确认可采性 → DTR），非严重度 | DWPE 货走 DTR 漏快速扣留；把建议当终局决定 | g07 |
| 2 | **DWPE vs Detention** | 是否需实物查验证据（DWPE 凭历史/Alert 即扣） | 把「不检查」读成「不检查就放过」→ 误放行 | g05 / g06 |
| 3 | **Conditional Release vs May Proceed** | 前者是等待判定期间的状态（可移动不可分销、附 bond）；后者是结束该状态的决定 | 把条件放行当放行 → FTH + Bond Action | g03 / g02 |
| 4 | **Refusal vs Detention** | Detention 临时可回转；Refusal 是 `final decision` 且之后仍有 90 天处置链 | 发出 Refusal 即归档 → 漏核验销毁/出口、漏 CBP 4647 / bond | g05 / g08 |
| 5 | **FSVP Importer vs Importer of Record** | 法域不同：FSMA 供应商验证义务主体（须在美国境内） vs CBP 报关/关税/bond 主体 | 483a/EIR 开错对象；Reconditioning 申请找错签字方 | g14 |
| 6 | **Importer vs Filer Misdeclaration** | 错误信息源自谁（进口商给错 vs filer 录错），非「谁被罚」 | 启动错误的评估路径；误以为 filer 出错可免进口商责任 | g13 |
| 7 | **SDI vs ADS** | SDI = 特殊抽样任务下的国内进口样品（禁用于已显违规品）；ADS = 同批同行补样 | 误用 SDI 丢失国内管辖权证据链；ADS 关联号断裂 | g15 |
| 8 | **Import Alert vs Import Bulletin** | Alert → 命中 DWPE、别再请求现场工作、走 DER；Bulletin → 指示去请求现场工作、不触发 DWPE | 误走 DER / 对已 DWPE 货又去查验；`IB` 缩写误读 | g17 / g04 |
| 9 | **May Proceed vs Release**（补充） | 系统内两条消息：未经查验无合规判定 / 经查验已作合规判定 | 把 May Proceed 当「FDA 已判定合规」 | g02 |
| 10 | **Re-export vs AGR**（补充） | 外国货「进来又出去」不适用 §801(e) / 美国货「出去又回来」视为进口 §801(d)(1) | 两条法定例外适用颠倒 | g26 / g27 |

**缩写同形异义警示（贯穿 g04 / g17 / g22）**

| 缩写 | 含义 A | 含义 B | 判别法 |
|---|---|---|---|
| **IB** | Import Bulletin（6.2 情报来源清单 [p.15]） | **Investigations Branch**（6.2.2.2.6 [p.19]、6.3 [p.31]） | 「**IB Release**」= 调查分部放行，与 Import Bulletin 无关 |
| **IA** | Import Alert | — | 与 DWPE / DER 绑定 |
| **OGA / PGA** | 同一批机构（6.2 第 105 行明言互为别称） | — | 展开词 `Partner` / `Partnering` 不统一，勿当两类 |

---

## 附：源层瑕疵（如实标注，不修正、不静默规范化）

> 本词典逐条回原文（`candidates/glossary.md`）核验，以下为 6.9 术语表及切块本身的可追溯性结论，供下游自动化解析与引用时显式兼容。

1. **规模与自认非穷尽**：IOM 6.9 – Glossary of Import Terms 共 **78 条**，编号自 `6.9.1`（American/US Goods Returned）至末条，跨 [p.50]–[p.58]。6.9 开篇自述 *"Note common import language and their meanings below. (Refer to the 'Regulatory Procedures Manual Glossary' for a more complete listing of import terms.)"* [p.50]——本章术语表**自认不是穷尽清单**，完整口径在 RPM Glossary。遇 6.9 未收词条时应回 RPM / 正文，不可据「6.9 没有」推断「不存在」。
2. **★ 末条编号不一致**：末条编号写作 **`6-9.78`**（源文件 `6.9-Glossary.txt` 第 463 行 `6-9.78 – Relabler`），与前 77 条一律 `6.9.1 … 6.9.77`（点号分隔两层）不一致，改用连字符 `6-9.78`（连字符 + 点号混用）。这是**源文件编号瑕疵**（排版/编号一致性问题，不影响该条内容 Relabeler / 改标商定义完整），本词典引用该条时保留原样 **`6-9.78`**；下游自动化解析须显式兼容此变体，否则会漏掉第 78 条或把它误归入别的章节。
3. **★ 6.9 未收、但正文定义且直接决定判定的关键术语（必须回 6.1–6.8 取定义）**：**只看 6.9 会缺失一半的高风险术语**——
   | 术语 | 6.9 是否有条目 | 实际定义出处 |
   |---|---|---|
   | **DER** | 无（只有 6.9.20 DTR） | IOM 6.2.5.1 [p.21]、6.2.5.3 [p.21-22] |
   | **IUC**（Intended Use Code） | 无 | IOM 6.1.6.2 [p.13]、6.1 IFE 段 [p.9] |
   | **Import Bulletin (IB)** | 无（只有 6.9.42 Import Alerts） | IOM 6.2.2.2.x [p.15]/[p.17]、6.3 [p.31] |
   | **SDI**（Special Domestic Import Sample） | 无（只有 6.9.24 DI Sample） | IOM 6.4.9 [p.37]、6.5 [p.39] |
   | **IB Release** | 无 | IOM 6.3.10.7 / 6.3.11 [p.32]、6.3 Class 2 [p.31] |
   | **VQIP 本体** | 无（只有 6.9.76 QAP） | IOM 6.1.7 [p.13] |
   | **May Proceed / Release 的系统级区分** | 6.9.56 只给 May Proceed 一条 | IOM 6.4.3 [p.35] |
   | **Conditional Release Period 的 30 天规则** | 6.9.13/6.9.41 只给结束条件 | IOM 6.2.4 [p.20] |
4. **`IB` 同形异义**：① 6.2 情报来源清单中 **IB = Import Bulletin** [p.15]；② 6.2.2.2.6 中 **IB = Investigations Branch** [p.19]；③ 6.3 "investigations branch is using discretionary authority to release the product" [p.31] 证实「**IB Release**」的 IB 指 Investigations Branch，与 Import Bulletin 无关。此外 **6.9 术语表未收 IB Release**。
5. **同批观察到的其他源层瑕疵（一并留痕）**：编号连接符不统一（部分条目用半角 ` - ` 而非 ` – `，如 6.9.22 [p.52]、6.9.52 [p.56]，按 ` – ` 硬切会漏条）；标题带尾随连字符 / 正文另起一行（6.9.66 / 6.9.68 / 6.9.70 [p.57]）；交叉引用括号未闭合（6.9.6 结尾 `*(See IOM 4.1.4.2.8*` [p.51] 缺右括号）；OCR 噪字（6.9.7 "required9import data" [p.51] 应为 "required import data"）；定义内留占位链接（6.9.42 "They can be found online here." [p.55]、6.9.54 [p.56]）；重复条目（6.9.13 [p.51-52] 与 6.9.41 [p.55] 文字近乎相同，计数 78 含重复项）；一条内打包多个概念（6.9.31 同条含 SERIO 与 OASIS [p.53-54]、6.9.29 含 7 类主体 [p.53]）；缩略语展开前后不一致（PGA 在 6.1.6.2 作 `Partner` [p.12] / 6.2 作 `Partnering` [p.15]；ITACS 标题单数 [p.56] / 正文复数）；术语表序与正文不完全对应（6.9.20 称 `Detention Recommendation` [p.52]、6.2 第 418 行称 `Detention Request (DTR)` [p.20]、6.2.5 标题称 `Detention Recommendations` [p.21]）。
6. **切块重叠提示（非源文件问题，仅防误判重复）**：`6.9-Glossary.txt` 开头 [p.50] 含 6.8.3.1 / 6.8.3.1.1（EIR、FSVP Records Review）尾部内容，`6.8-FSVP.txt` 第 264 行又出现 `6.9.2 – Additional Sample`——这是 `.cangjie/index` 按 6.1–6.9 切块时的邻接重叠，不是 6.9 多出条目；计数 78 条仍以 `6.9.1`–`6-9.78` 为准。**引用按小节号而非分块文件名**（另见 `dist/capabilities/iom-imports-procedure.md` 边界与判停节关于 6.2.5.5 跨页落在 [p.23] 的说明）。
7. **口径冲突时以系统定义 / 正文细则为准**：May Proceed 以 6.4.3 系统定义（`No compliance decision has been made`）优先于 6.9.56 的宽松表述；Import Alert 的强制效力须以 6.9.22 + 6.2.5.3 补足 6.9.42。

---

*本词典服务于「理解 FDA 判定逻辑」，不是企业合规义务清单；法律位阶限制见 `BOOK_OVERVIEW.md` §3、能力卡 V10 与 CAP-29 来源路由入口的「边界与判停」。所有 IOM 引用统一 `IOM 6.x.x [p.N]`。*
