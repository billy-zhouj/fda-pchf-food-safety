# IOM 2026 Chapter 6 — Imports：关键概念词典候选

> **阶段 1 · 术语提取器（glossary-extractor）产出**
> 本文件不独立成 skill，作为后续所有能力卡的**共享口径层**被引用。
> 提取器规范：`C:/Users/HG/.workbuddy/skills/cangjie-skill/extractors/glossary-extractor.md`
> 阶段 0 上下文：`BOOK_OVERVIEW.md`（第 2 节已有 12 条术语，本文在其上扩展并逐条回原文核验）
> 主要来源：`.cangjie/index/6.9-Glossary.txt`（IOM 6.9 术语表，78 条，含 `[p.N]` 标记）
> 辅助核验：`.cangjie/index/6.1…6.8-*.txt` 全量 Grep + 定点回读原文

## 字段约定（与 extractor 规范的映射）

规范给出 YAML 字段 `author_definition` / `key_distinction` / `why_it_matters` / `tags`。
本文按任务要求改用可读的 Markdown 分节，对应关系如下，下游可机械转换：

| 本文字段 | 规范字段 |
|---|---|
| **作者定义**（英文引用 ≤100 词/段 + 中文自译） | `author_definition` |
| **与常识/相邻概念的混淆点** | `key_distinction` |
| **混淆后会导致什么判定错误** | `why_it_matters` |
| **出处** | `source_chapter` |
| **tags** | `tags` |

英文引用均逐字取自切块原文，每段控制在 100 词以内；成对概念分列两段引用。页码 `[p.N]` 依据各切块内的页码标记定位（6.9 跨 `[p.50]`–`[p.58]`，正文 6.1 `[p.6]`–`[p.13]`、6.2 `[p.14]`–`[p.22]`、6.3 `[p.23]`–`[p.32]`、6.4 `[p.33]`–`[p.38]`、6.5 `[p.39]`–`[p.42]`、6.6 `[p.42]`–`[p.45]`、6.8 `[p.46]`–`[p.50]`）。

---

## 0. 术语表自身的可追溯性与源文件瑕疵（如实标注）

### 0.1 规模与编号

- IOM **6.9 – Glossary of Import Terms** 共 **78 条**，编号自 `6.9.1`（American/US Goods Returned）至末条，`[p.50]`–`[p.58]`。
- 6.9 开篇自述其定位：*"Note common import language and their meanings below. (Refer to the 'Regulatory Procedures Manual Glossary' for a more complete listing of import terms.)"* `[p.50]` — 即本章术语表**自认不是穷尽清单**，完整口径在 RPM Glossary。下游遇 6.9 未收词条时应回 RPM / 正文，不可据"6.9 没有"推断"不存在"。
- 阶段 0 `BOOK_OVERVIEW.md` 第 1 节骨架第 8 项亦记为「6.9 Glossary（78 条术语）」，与本文计数一致。

### 0.2 ★ 任务指出的编号瑕疵（如实记录，不修正、不静默规范化）

> **末条编号写作 `6-9.78`，与前 77 条的 `6.9.x` 不一致。**
> 源文件 `6.9-Glossary.txt` 第 463 行原文：`6-9.78 – Relabler`。
> 前序 77 条一律为 `6.9.1` … `6.9.77`（点号分隔两层），末条改用连字符 `6-9.78`（连字符 + 点号混用）。
> 这是**源文件编号瑕疵**，属于排版/编号一致性问题，不影响该条内容（Relabeler / 改标商定义完整）。
> 本文在引用该条时保留原样写作 **`6-9.78`**；下游若做自动化解析，须显式兼容此变体，否则会漏掉第 78 条或把它误归入别的章节。

### 0.3 同批观察到的其他源层瑕疵（一并留痕）

| # | 瑕疵 | 原文证据 | 影响 |
|---|---|---|---|
| a | 编号连接符不统一：部分条目用 ` - `（半角连字符）而非 ` – ` | `6.9.22 - Detention Without Physical Examination` `[p.52]`、`6.9.23 - Detention and Hearing Process`、`6.9.24 - Domestic Import (DI) Sample`、`6.9.27 - Entry Documents`、`6.9.52 - Line (Line Item)` `[p.56]`、`6.9.72 - Stripping (Of Containers)` `[p.58]` | 按 ` – ` 硬切会漏条 |
| b | 标题带尾随连字符 / 标题后空行 | `6.9.66 – Redelivery Bond (AKA Entry Bond) -`、`6.9.68 – Relabeling -`、`6.9.70 – Release with Comment -`（`[p.57]`），`6.9.70` 正文另起一行 | 标题解析易带脏字符 |
| c | 交叉引用括号未闭合 | `6.9.6 – Audit Sample` 结尾 `*(See IOM 4.1.4.2.8*` `[p.51]` 缺右括号 | 引用目标需人工补全 |
| d | OCR 噪字 | `6.9.7 – ABI` 中 `"electronically file required9import data with Customs"` `[p.51]` | 引用时需校正为 `required import data` |
| e | 定义内留占位链接 | `6.9.42 – Import Alerts`：`"They can be found online here."` `[p.55]`；`6.9.54 Mail Entry`：`"Industry guidance can be found here."` `[p.56]` | 无实质定义内容，须回正文补 |
| f | 重复条目 | `6.9.13 – Conditional Release` `[p.51–52]` 与 `6.9.41 – Immediate Delivery (ID)/ Conditional Release` `[p.55]` 文字近乎相同 | 计数 78 含重复项；易误当两个术语 |
| g | 一条内打包多个概念 | `6.9.31 – FDA Import Systems` 同条含 SERIO 与 OASIS 两套系统 `[p.53–54]`；`6.9.29 – Establishment` 含 7 类主体 `[p.53]` | 按"一条=一术语"解析会丢子概念 |
| h | 缩略语展开前后不一致 | PGA：6.1.6.2 作 `Partner Government Agencies (PGA) flags` `[p.12]`；6.2 作 `Partnering Government Agencies (PGAs)` `[p.15]`。ITACS：6.9.50 标题作 `…Communication System`（单数）`[p.56]`，6.9.27 / 6.2 / 6.4 正文多处作 `…Communications System`（复数） | 检索漏项 |
| i | 术语表序与正文不完全对应 | DTR 称 `Detention Recommendation`（6.9.20 `[p.52]`），6.2 第 418 行称 `Detention Request (DTR)` `[p.20]`，6.2.5 标题称 `Detention Recommendations` `[p.21]` | 见 g07 |

### 0.4 ★ 6.9 未收录、但正文定义且直接决定判定的关键术语（必须回正文取定义）

这是本次核对最重要的可追溯性结论：**只看 6.9 会缺失一半的高风险术语**。

| 术语 | 6.9 是否有条目 | 实际定义出处 |
|---|---|---|
| **DER** | **无**（只有 6.9.20 DTR） | IOM **6.2.5.1** `[p.21]`、6.2.5.3 `[p.21–22]` |
| **IUC**（Intended Use Code） | **无** | IOM **6.1.6.2** `[p.13]`、6.1 IFE 段 `[p.9]` |
| **Import Bulletin (IB)** | **无**（只有 6.9.42 Import Alerts） | IOM **6.2.2.2.x** `[p.15]`/`[p.17]`、6.3 `[p.31]` |
| **SDI**（Special Domestic Import Sample） | **无**（只有 6.9.24 DI Sample） | IOM **6.4.9** `[p.37]`、6.5 `[p.39]` |
| **IB Release** | **无** | IOM **6.3.10.7 / 6.3.11** `[p.32]`、6.3 Class 2 `[p.31]` |
| **VQIP 本体** | **无**（只有 6.9.76 QAP） | IOM **6.1.7** `[p.13]` |
| **May Proceed / Release 的系统级区分** | 6.9.56 只给 May Proceed 一条 | IOM **6.4.3** `[p.35]`（两条系统消息定义） |
| **Conditional Release Period 的 30 天规则** | 6.9.13/6.9.41 只给"结束条件" | IOM **6.2.4** `[p.20]` |

### 0.5 切块重叠提示（非源文件问题，仅防误判重复）

`6.9-Glossary.txt` 开头 `[p.50]` 处包含 **6.8.3.1 / 6.8.3.1.1**（EIR、FSVP Records Review）尾部内容，`6.8-FSVP.txt` 第 264 行又出现 `6.9.2 – Additional Sample`。这是 `.cangjie/index` **按 6.1–6.9 切块时的邻接重叠**，不是 6.9 术语表多出条目；计数 78 条仍以 `6.9.1`–`6-9.78` 为准。

---

## 1. 选词说明

- **共选 28 条**（g01–g28），落在任务要求的 20–30 条区间内，**未机械抄完 78 条**。
- 选词判据对应规范第 18 行的四条，并按本任务收窄为一条主判据：**「与常识用法不同、一旦混淆即造成判定错误」**。据此剔除了纯运输/单证类低风险词条（Air Waybill、Bill of Lading、Break-Bulk Cargo、CFS、CBW、DUNS、Marks、Stripping、Section 321、Warehouse Entry 等）与纯法条/机构名（FSMA、Import Sections、FTZ、Personal Baggage Entry）。
- 阶段 0 第 2 节 **12 条全部纳入并加深**（Entry/Line、May Proceed、Conditional Release、Failure to Hold、DWPE、DER/DTR、Prior Notice、Reconditioning、Refusal、PREDICT、FSVP Importer、A of C/IUC），另补 16 条正文高风险术语。
- **成对易混概念以相邻/合并条目组织**，便于下游 `key_distinction` 直接引用；速查矩阵见第 3 节。

---

## 2. 词典候选（g01–g28）

### g01 · Entry / Line / Entry Line Item — 报关 / 报关行项 / 报关分项

**作者定义**
> `6.9.25 – Entry`："Delivery, or offer for delivery, of merchandise into the Customs Territory of the United States from an outside point." `[p.53]`
> `6.9.28 – Entry Line Item`："Each portion of an entry that is listed as a separate item in an entry. An importer may identify merchandise in an entry in multiple portions; however, an item in the entry having a different tariff description must be listed separately." `[p.53]`
> `6.9.52 – Line (Line Item)` 同义补充：`"...except for items in the entry having a different tariff description and rate, which must be listed separately."` `[p.56]`

**中文自译**：Entry 指货物自境外交付（或提出交付）进入美国关税领土的行为；Line / Entry Line Item 指一次报关中被单列为独立项目的每一部分——进口商可自行把一票货拆成多项，但**关税描述（及税率）不同者必须分开列项**。

**出处**：IOM 6.9.25 / 6.9.28 `[p.53]`、6.9.52 `[p.56]`；正文 6.9.57 Notice of FDA Action "broken down by each entry line" `[p.56]`、6.4.3 "Lines Which May Proceed" `[p.35]`。

**与常识/相邻概念的混淆点**
- ≠「一批货 / 一个提单 / 一个集装箱」。Entry 是**报关行为**，Line 是**可单独审查、单独作出可采性判定的最小单元**；一个 entry 可含多个 line，各 line 可分别放行、分别扣留、分别出通知。
- ≠ **Lot**（6.9.53 `[p.56]`："an entry, group of entries, or a portion of an entry of goods that can clearly be defined as appropriate for FDA sampling"）——Lot 是**取样单元**，可跨 entry，粒度与 line 不同。
- ≠ **Import Status**（6.9.46 `[p.55]`，指数据库中"尚未放行"的状态）。

**混淆后会导致什么判定错误**：把整票当单一判定单元 → 对未查验的 line 误放行或漏扣留；Notice of FDA Action 未按 line 拆分；把 6.4.3 的「Lines Which May Proceed」单行放行误读为整票放行；Failure to Hold / Substitution 调查时错定责任货量范围。

**tags**：`[term, core-concept, granularity]`

---

### g02 · May Proceed / Release — 准予放行 / 查验后放行（★ 系统内两种放行消息）

**作者定义**
> `6.9.56 – May Proceed`："The release performed after identifying and determining the line/entry meets certain admissibility requirements. This means the product can be distributed into U.S. commerce. However, a release does not preclude future FDA action if a problem is found later." `[p.56]`
> `6.4.3`（系统级定义，关键）："May Proceed: 'Product may proceed without FDA examination. **FDA has made no determination the product complies** with all provisions of the Food, Drug, and Cosmetic Act... This message does not preclude action should the products later be found violative.' **(No compliance decision has been made.)**" / "Release: 'The product is released **after FDA examination**... (A compliance decision has been made.)'" `[p.35]`

**中文自译**：6.9 把 May Proceed 定义为「确认该行/票满足若干可采性要求后作出的放行，产品可进入美国流通，但日后发现问题不排除 FDA 再采取行动」。而 6.4.3 的系统定义更严格：May Proceed = **未经 FDA 查验、未作合规判定**的放行消息；Release = **经查验后、已作合规判定**的放行消息。

**出处**：IOM 6.9.56 `[p.56]`；**IOM 6.4.3 `[p.35]`**；6.2.2.2.1 Manual "May Proceed" `[p.17]`、6.2.2.2.2 Rescinding `[p.18]`、6.2 第 85 行（禁止空泛备注）`[p.15]`、6.2 第 83/176 行（与 PREDICT 相悖须写理由）`[p.15]/[p.17]`。

**与常识/相邻概念的混淆点**
- 字面「可以开始继续办理」≠ 实际是**终局性放行动作**（货物可进入流通），且**可 rescind**。
- **≠「判定合规」**：6.4.3 明确 `No compliance decision has been made`；6.9.56 的 "meets certain admissibility requirements" 是较宽松的表述，两处存在口径张力，**下游应以 6.4.3 系统定义为准**。
- **May Proceed ≠ Release**：前者未经查验、无合规判定；后者经查验、已作合规判定。二者是系统里两条不同消息，不可互换。
- 二者与 **IB Release**（g04）共同点：都**结束条件放行期**，且撤消后该期**不重开**（6.2.2.2.2 `[p.18]`、6.3.11 `[p.32]`）。
- 禁止把 "May Proceed" / "N/A" 当作系统备注写进 Remarks（6.2 第 85 行）。

**混淆后会导致什么判定错误**：把 May Proceed 当「FDA 已出具合规背书」→ 企业误以为免除后续责任（实际 `does not preclude future FDA action`）；与 PREDICT 结果相悖的放行不写具体理由 → 违反 6.2 明令；把「未作合规判定」当「已判定合格」→ 后续发现违规时误以为 FDA 已放弃追责；混淆 May Proceed / Release → 错误判断案卷里是否已存在合规决定，影响听证举证。

**tags**：`[term, core-concept, decision-action, paired]`

---

### g03 · Conditional Release / Immediate Delivery (ID) — 条件放行 / 即时交付

**作者定义**
> `6.9.13 – Conditional Release`："Entry/Immediate Delivery must be filed within 15 calendar days of arrival... Even though CBP has allowed the immediate delivery, any FDA-regulated products are conditionally released until the FDA makes an admissibility decision. The conditional release period ends when the FDA 'May Proceeds' the entry or issues a refusal. The goods may be moved but CBP can request redelivery within 30 days." `[p.51–52]`
> `6.2.4 – Conditional Release Period`："CBP may conditionally release a product while it awaits an FDA admissibility decision... This period typically lasts for 30 days. It ends as soon as one of these things happens first: The FDA issues a 'May Proceed' notice / The FDA issues a notice of refusal / The 30-day period expires." `[p.20]`

**中文自译**：CBP 允许即时交付后，FDA 监管货物仍处于「条件放行」状态，直到 FDA 作出可采性判定；货**可以移动**，但 CBP 可在 30 天内要求重新交付（redelivery）。条件放行期通常 30 天，以「May Proceed / 拒绝通知 / 30 天届满」三者中最先发生者结束。

**出处**：IOM 6.9.13 `[p.51–52]`、6.9.41（重复条目）`[p.55]`、**6.2.4 `[p.20]`**；6.9.66 Redelivery Bond `[p.57]`。

**与常识/相邻概念的混淆点**
- ≠「有条件地合格 / 附条件批准」。**货已交进口商控制，但仍在 FDA 管辖下**，附带的是 **redelivery bond 义务**（6.9.66，金额为货值 3 倍）。
- **「可移动」≠「可分销」**：无 FDA 放行即分销 = Failure to Hold（g11）。
- **两个「30 天」不是同一件事**：6.9.13 的 30 天是 CBP 请求 redelivery 的窗口；6.2.4 的 30 天是条件放行期**本身长度**；6.6.4.1 的 30 天是 Failure to Hold 下 CBP 4647 的 redelivery 期限（区别于 Refusal 后的 90 天）。
- ≠ May Proceed：条件放行是**等待判定期间的状态**，May Proceed 是**结束该状态的决定**。

**混淆后会导致什么判定错误**：把条件放行当放行 → 提前分销，构成 Failure to Hold，触发 CBP 4647 与 Bond Action；把「可以移动」理解为「可以销售」→ 同一后果；错过 30 天窗口 → 无法 redelivery，只能追偿 liquidated damages；把三个 30 天混用 → 期限计算全错。

**tags**：`[term, core-concept, status, time-window, paired]`

---

### g04 · IB Release — 调查分部放行（★ IB 为同形异义缩写）

**作者定义**
> `6.3.10.7 – Next Steps`："If the exam was classified as Class 1, you will have the option to IB Release or Add Work. If no other work needs to be added to the line, the line will be released by selecting IB Release and entering Remarks, including an appropriate summary of remarks entered in the Exam Results." `[p.32]`
> `6.3.11 – Rescinding an IB Release`："Note that when an entry receives an IB Release, the conditional release period of the entry ends (See IOM 6.2.4) and does not re-open when IB Release is rescinded." `[p.32]`
> `6.3`（Class 2 语境）："...however, investigations branch is using discretionary authority to release the product." `[p.31]`

**中文自译**：现场查验（Class 1，或 Class 2 经裁量）完成、无需追加工作时，由**调查分部（Investigations Branch）**作出的放行；它同样结束条件放行期，撤消后不重开。

**出处**：IOM 6.3.10.7 / 6.3.11 `[p.32]`、6.3 Class 2 分类 `[p.31]`；**缩写证据**：6.2.2.2.6 "To send a line to the **Investigations Branch (IB)**" `[p.19]`、6.3 第 70 行 "the investigations branch conducts a label review (LBL)" `[p.23]`；对照 6.2 第 95 行 "Import Alerts (IA) and **Import Bulletins (IB)**" `[p.15]`。

**与常识/相邻概念的混淆点**
- **★ IB 在本章是同形异义缩写**：① `6.2` 情报来源清单中 **IB = Import Bulletin**（g17）；② `6.2.2.2.6` 中 **IB = Investigations Branch**；③ `6.3` "investigations branch is using discretionary authority to release the product" 证实 **「IB Release」的 IB 指 Investigations Branch，与 Import Bulletin 无关**。
- ≠ **May Proceed**：IB Release 是**现场查验/取样完成后**由调查分部作出的放行；May Proceed 是**电子审查阶段**的放行。二者结束条件放行期的效果相同，但阶段、主体、是否经查验均不同。
- **Class 2 有 adverse findings 仍可 IB Release**，但必须在 Summary / Remarks 详述放行理由（6.3.10.7 `[p.32]`、6.3 第 536 行 `[p.32]`）。
- 撤消属例外，须主管批准、24 小时内通知 filer、生成更新版 Notice of FDA Action，并请 CBP 在 24 小时内 Unset/Hold bond（6.3.11 `[p.32]`）。
- **6.9 术语表未收 IB Release**。

**混淆后会导致什么判定错误**：把 IB Release 读成「按 Import Bulletin 放行」→ 满世界找不存在的文书，且漏掉与 Import Alert 的分流；把 Class 2 有不良发现的裁量放行当「查验合格」→ 漏写法定放行理由，听证时无法辩护；把 IB Release 当 May Proceed → 误判放行所处阶段与是否已形成合规决定。

**tags**：`[term, homonym, decision-action, core-concept]`

---

### g05 · Detention — 扣留

**作者定义**
> `6.9.21 – Detention`："A **temporary administrative action** taken by the FDA against articles offered for entry which are **not or appear not to be** in-compliance with the laws the FDA administers. Detained articles can be released if brought into compliance, or are refused entry or seized, if not brought into compliance." `[p.52]`

**中文自译**：扣留是 FDA 对「不合规或**表面看来**不合规」的拟入境货物采取的**临时行政措施**；经整改达合规可放行，未达合规则被拒绝入境或扣押。

**出处**：IOM 6.9.21 `[p.52]`；6.9.23 Detention and Hearing Process `[p.52–53]`、6.9.46 Import Status `[p.55]`、6.5.2.8 `[p.41]`。

**与常识/相邻概念的混淆点**
- 三个限定词最关键：**temporary**（临时）、**administrative**（行政措施）、**"appear not to be"**（基于违规外观，非违规认定）。
- ≠ **Refusal of Admission**（g08）：Detention 可回转（放行 / 拒绝 / 扣押三选一），Refusal 是 `final decision`。
- ≠ **DWPE**（g06）：一般扣留通常伴随查验/取样证据；DWPE 凭历史与 Import Alert 即可扣。
- ≠ 流程终点：其后还有听证、举证、Reconditioning、复核、放行或拒绝。

**混淆后会导致什么判定错误**：把扣留当「已判定不合格」→ 跳过听证与举证、直接出 Refusal；把扣留当流程终点 → 漏掉听证期、改标申请（FDA 766）、90 天出口/销毁、bond action，以及「FDA 档案保持开启」的义务。

**tags**：`[term, core-concept, legal-status, paired]`

---

### g06 · DWPE (Detention Without Physical Examination) — 免实物查验扣留

**作者定义**
> `6.9.22 – DWPE`："An action directed against specific products manufactured or shipped by specific foreign firms. 'Import Alerts' list products that may be detained without physical examination due to their violative history or potential." `[p.52]`
> `6.9.6 – Audit Sample`（联动条款）："At least one FDA audit sample should be included as evidence when processing **removal** of a product, shipper, or country from DWPE." `[p.51]`
> `6.2.5.3`："Use a DER when an entry is subject to DWPE." `[p.21]`

**中文自译**：DWPE 是针对特定境外企业生产/发运的特定产品采取的扣留行动；Import Alerts 列出因违规历史或违规可能性而**可不经实物查验即予扣留**的产品。至少须有一份 FDA 自采审核样品，才能作为把产品/发货人/国家从 DWPE 名单移除的证据。

**出处**：IOM 6.9.22 `[p.52]`、6.9.6 `[p.51]`、6.2.5.1 / 6.2.5.3 `[p.21]`、6.6.4.3 `[p.44]`。

**与常识/相邻概念的混淆点**
- ★ 字面「不检查」极易误读为「不检查就放过」，**实际恰相反：不检查就扣住**（基于违规历史/外观，无需实物查验）。
- ≠ **Detention**（g05）：一般扣留通常需查验/取样证据；DWPE 凭 Import Alert 与历史即可自动扣。
- ≠ **Import Alert**（g17）：Alert 是列名/指导文件，DWPE 是据此采取的**行动**。
- 触发 **DER** 而非 DTR（g07）；解除 DWPE 有硬性证据门槛（至少一份 **FDA** audit sample，非私人实验室报告）。

**混淆后会导致什么判定错误**：把 DWPE 当「免检放行」→ 放行本应自动扣留的货物、错过 DER 快速通道；把「企业自行送检合格」当解除条件 → 忽略 FDA 自采审核样品的硬性要求，DWPE 移除申请不成立；把 DWPE 与一般 Detention 混同 → 误要求现场查验，浪费资源且可能误放行。

**tags**：`[term, core-concept, counterintuitive, paired]`

---

### g07 · DER vs DTR — 扣留建议的两种 work type（★ 成对，6.9 缺 DER）

**作者定义**
> `6.2.5.1 – Submission of Detention Recommendations to the Compliance Branch`："As an entry reviewer, you will use one of two work types to recommend detention: DER or DTR. **DER (Detention without Physical Examination): Use DER when a product is subject to Detention without Physical Examination (DWPE). DTR (All Other Detentions): Use DTR for all other situations where a product appears to be violative.**" `[p.21]`
> `6.9.20 – Detention Recommendation (DTR)`："Used when review of the entry information cannot confirm that products being offered for import meet FDA's admissibility criteria. Examples include products in which the required registration, scheduled process filing, 510(k), or pre-market approval (PMA) cannot be verified at the entry review step." `[p.52]`
> `6.2.5.3`（DER 免单据前提）："You can submit a DER to the Compliance Branch (CB) without requesting entry documents if... The electronic data matches the Import Alert criteria... The Import Alert does not require specific documents... You do not need any additional information." `[p.21]`

**中文自译**：审查员向 Compliance Branch 推荐扣留时二选一：货物受 DWPE 约束 → **DER**；其余一切「看起来违规」情形（如无法核实注册、scheduled process filing、510(k)、PMA）→ **DTR**。DER 在满足三项前提时可免索单据直接提交；若 Import Alert 要求特定证书（例：IA 28-02 要求印度黑胡椒附证书），必须先索取并审阅单据。

**出处**：**IOM 6.2.5.1 `[p.21]`（DER 唯一定义处，6.9 无此条）**、6.2.5.3 `[p.21–22]`、6.2.5.4 `[p.22]`、6.2.5.2 `[p.21]`；6.9.20 `[p.52]`；6.2 第 418 行 "send a Detention Request (DTR)" `[p.20]`。

**与常识/相邻概念的混淆点**
- ★ **不是严重度分级，而是「触发依据」的分流**：`受 DWPE/Import Alert 约束 → DER`；`其余无法确认可采性 → DTR`。
- ★ 审查员提交的是 **recommendation / request（建议/请求）**，**不是终局扣留决定**；须交 Compliance Branch（6.2.5 `[p.21]` "Recommend detention to the Compliance Branch (CB)"）。
- 术语表口径不一致：6.9.20 称 `Detention Recommendation`，6.2 第 418 行称 `Detention Request`，6.2.5 标题称 `Detention Recommendations`（见 0.3-i）。
- **6.9 完全没有 DER 条目**——只看术语表会以为只有一种扣留建议（见 0.4）。

**混淆后会导致什么判定错误**：按「严重程度」选 work type → DWPE 货走 DTR（漏掉免单据快速扣留通道）或非 DWPE 货走 DER（错误免查验）；把建议当决定 → 审查员越权作出终局扣留，绕过 Compliance Branch；忽略「Alert 要求证书时须先索单据」→ DER 案卷证据不全，听证被击穿。

**tags**：`[term, paired, routing, source-gap, core-concept]`

---

### g08 · Refusal of Admission / Import Refusal — 拒绝入境

**作者定义**
> `6.9.44 – Import Refusal`："FDA's **final decision** that a detained shipment is in violation of FDA laws and regulations. A refused shipment must either be destroyed or exported under the supervision of CBP and the FDA **within 90 days** of the date of the Notice of FDA Action (Refusal Notice)." `[p.55]`
> `6.5.2.8 – Procedure after Hearing - Refusal of Admission`："The 'Notice of FDA Action - Refusal of Admission' provides for the exportation or destruction of the shipment, under CBP supervision, within 90 days... **The FDA file remains open until the division receives notification indicating that the goods were either destroyed or exported.**" `[p.41]`

**中文自译**：拒绝入境是 FDA 认定被扣货物违法的**终局决定**；须在通知日起 90 天内于 CBP 与 FDA 监督下出口或销毁；FDA 档案一直保持开启，直到收到销毁或出口的证明。

**出处**：IOM 6.9.44 `[p.55]`、6.5.2.8 `[p.41]`、6.5.2.11 Bond Action `[p.42]`、6.6.4.1 第 7 步（CBP 4647）`[p.43]`。

**与常识/相邻概念的混淆点**
- ≠ **Detention**（g05）：Detention 临时、可回转；Refusal 是 `final decision`。
- ★ **不是流程终点**：之后还有 90 天内出口/销毁、CBP 4647 红交货、销毁/出口核验、Bond Action；FDA 的公共健康责任**延续到货物被销毁或出口为止**（6.5.2.8 `[p.41]`），档案不因发出通知而关闭。
- Refusal 通知上的 charge 须与原始（或修订后）`Notice of FDA Action - Detained` **逐字一致**（6.5.2.8 `[p.41]`）。
- **90 天（Refusal 后）≠ 30 天**（Failure to Hold 下 CBP 4647 用于查验/取样时的 redelivery 期限，6.6.4.1 第 7 步 `[p.43]`）。
- 合格部分经 Reconditioning 放行时，**不合格部分仍须单独出具 Refusal**（6.5.2.5 `[p.40]`）。

**混淆后会导致什么判定错误**：发出 Refusal 即归档 → 未核验销毁/出口、未发 CBP 4647、错过 Bond Action 时效，违规货可能流入市场而 FDA 档案已关；把 90 天与 30 天混用 → redelivery 期限算错；把 Refusal 当 Detention → 误以为还可再给一次整改机会。

**tags**：`[term, core-concept, legal-status, time-window, paired]`

---

### g09 · Reconditioning / Relabeling — 重整 / 改标

**作者定义**
> `6.9.65 – Reconditioning`："When a product is detained because it violates FDA laws and regulations, **the importer of record may submit an application to the agency requesting permission** to re-label or recondition the product in an attempt to bring it into compliance." `[p.57]`
> `6.9.68 – Relabeling`："The process of modifying labeling in order to come into compliance with FDA regulations. **Relabeling is considered a form of reconditioning.**" `[p.57]`
> `6.5.2.5`："...consignee by Notice of Release. This notice is usually identified as '**Released after Reconditioning**.'... A Notice of Refusal of Admission should also be issued for the **rejected portion**." `[p.40]`

**中文自译**：货物因违规被扣后，须由 **importer of record** 向 FDA **提交申请**（获批准并在监督下）以改标或重整使其达合规；改标是重整的一种形式。批准后复核，合格部分以「Released after Reconditioning」放行，不合格部分仍须销毁/再出口并单独出具拒绝通知。

**出处**：IOM 6.9.65 / 6.9.68 `[p.57]`、6.5.2.4 / 6.5.2.5 / 6.5.2.6 `[p.40]`、6.9.74 Supervisory Charges `[p.58]`；表单 Form FDA 766 + bond（BOOK_OVERVIEW 第 1 节第 5 项）。

**与常识/相邻概念的混淆点**
- ★ ≠ 企业自行返工：须 **importer of record 申请 → FDA 批准并监督**；未经批准的自行整改**不产生放行效力**。
- 申请主体是 **importer of record**（g14），不是 FSVP Importer，也不是境外生产商。
- **改标 ⊂ 重整**，不是并列的两个动作。
- 复核后「部分放行」时，不合格部分仍须销毁/再出口 + 单独 Refusal（g08）。
- 重整失败原则上不给第二次机会，除非修订后的方法能合理保证成功（BOOK_OVERVIEW 命题 9）。

**混淆后会导致什么判定错误**：把企业自行整改当合规完成 → 误放行；找错申请/签字主体（用 FSVP Importer 或境外厂商）→ 申请无效；把「部分放行」当整票放行 → 漏掉对不合格部分的销毁/出口与单独 Refusal，违规货流入市场。

**tags**：`[term, core-concept, procedure]`

---

### g10 · Bond Action / Redelivery Bond — 保证金行动 / 重新交付保证金

**作者定义**
> `6.9.11 – Bond Action`："Action taken by **Customs** resulting in forfeiture of all, or a portion of, an entry bond when an importer fails to redeliver merchandise covered by such a bond." `[p.51]`
> `6.9.66 – Redelivery Bond (AKA Entry Bond)`："A bond posted by the importer of record with CBP. For FDA-regulated products, this is currently in the amount of **three times the value of the imported product**, to insure redelivery of the product for examination, reconditioning, export, or destruction." `[p.57]`
> `6.5.2.11 – Bond Action`："Bond actions are taken when an entry is **distributed prior to FDA release and cannot be redelivered**, or when an article has been **detained and refused, and the article is not destroyed or exported** in accordance with the requirements of the law." `[p.42]`

**中文自译**：Redelivery Bond 是 importer of record 向 CBP 提交、金额为货值 3 倍的保证金，担保货物可被重新交付以接受查验、重整、出口或销毁；Bond Action 则是当进口商未能重新交付时，**由 CBP** 没收全部或部分保证金（liquidated damages）的行动。

**出处**：IOM 6.9.11 `[p.51]`、6.9.66 `[p.57]`、6.5.2.11 `[p.42]`（引 §801(b)、19 CFR 113.62、21 CFR 1.97(b)）、6.3.11（撤消 IB Release 后 24 小时内请 CBP Unset/Hold bond）`[p.32]`。

**与常识/相邻概念的混淆点**
- **Redelivery Bond = 工具/法定义务**（所有条件放行货物必附）；**Bond Action = CBP 的执行动作**。二者不是同义词，也不是「罚款」与「保证金」的关系。
- **主体是 CBP，不是 FDA**；FDA 提供责任说明，且 CBP 减轻已核定损害通常须 FDA 完全同意（21 CFR 1.97(b)）。
- 两个触发情形：① 放行前已分销且无法 redeliver（= Failure to Hold 后果）；② 已扣留并拒绝但未按期销毁/出口（= Refusal 后果）。
- ≠ **Supervisory Charges**（6.9.74 `[p.58]`，FDA 监督重整/查验的费用，21 CFR 1.99）。

**混淆后会导致什么判定错误**：把 bond 当「FDA 开的罚款」→ 找错责任主体与救济（减免）路径；以为发出 Refusal 即自动完结 → 漏掉 Bond Action 与 liquidated damages 时效；把保证金与监督费用混记 → 费用核算与文书（FDA 790）错配。

**tags**：`[term, paired, enforcement, procedure]`

---

### g11 · Failure to Hold — 未获放行即分销（★ 原文特意澄清）

**作者定义**
> `6.9.30 – Failure to Hold`："Failure to hold means that **the goods have been distributed by the importer/consignee without an FDA release from import status**. Such goods are usually subject to CBP's redelivery provisions." `[p.53]`
> `6.6.4.1`（关键澄清，原文带 `*` 注）："***Please note that this is defined as distribution without a release, not merely moving the goods outside of the port area.**" `[p.43]`
> `6.6.4.1` 八步清单第 7 步："Coordinate with CBP the issuance of a Demand for Redelivery (form 4647) if one has not already issued per a refusal. Form 4647 can be issued for the purposes of examination/sampling, not merely because of an FDA refusal. In such circumstances, **the deadline for redelivery is 30 days, instead of the 90 days post-refusal.**" `[p.43]`

**中文自译**：Failure to Hold 指进口商/收货人在**未取得 FDA 解除进口状态的放行**之前已把货物分销；通常触发 CBP 的重新交付条款。原文特别注明：定义要件是「无放行而分销」，**不是「货物被移出港区」**。

**出处**：IOM 6.9.30 `[p.53]`、**6.6.4.1 `[p.43]`**（8 步清单）、6.6.4.2 / 6.6.4.3（健康危害、DWPE 加重步骤）`[p.43–44]`。

**与常识/相邻概念的混淆点**
- ★ 关键在**「分销」而非「位移」**：货物移出港区本身**不构成**该违规（原文特意加 `*` 注明）。
- ≠ **Substitution**（g12）：Substitution 是伪造实物与报关的对应关系，且常是掩盖 Failure to Hold 的手段（6.6.4.4 `[p.44]`）。
- ≠ 一般「违反扣留令」：判定要件严格是「无 FDA release from import status 而分销」。
- 加重分支：存在重大健康危害，或仅达「违规外观」标准的 DWPE 情形（如即食食品沙门氏菌史）→ 追加召回/收货人通知/公共警告协调（6.6.4.2 / 6.6.4.3）。
- 30 天 redelivery 窗口，区别于 Refusal 后的 90 天（g08）。

**混淆后会导致什么判定错误**：把「货物被移到港区外」即判 Failure to Hold → 误启动 8 步调查、CBP 4647 与保证金行动；反之把已分销误当「只是移库」→ 漏掉健康危害情形下的召回与公共警告协调，公共健康风险失控。

**tags**：`[term, core-concept, counterintuitive, violation-pattern]`

---

### g12 · Substitution — 调包

**作者定义**
> `6.9.73 – Substitution`："An attempt by the importer/consignee to present goods to the FDA as corresponding to a particular entry when **they are in fact not the goods from that entry**. May occur as an attempt to hide distribution without an FDA release and avoid CBP bond actions." `[p.58]`
> `6.6.4.4`："**Until it is determined otherwise, consider all substitution cases to involve distribution of the actual goods without FDA release.** (See IOM 6.6.4.1, FAILURE TO HOLD.)" `[p.44]`

**中文自译**：进口商/收货人把并非某票报关项下的货物，冒充该票货物提交给 FDA；常用于掩盖「无 FDA 放行即分销」并规避 CBP 保证金行动。在查明之前，一律先按 Failure to Hold 处理。

**出处**：IOM 6.9.73 `[p.58]`、6.6.4.4 `[p.44]`、6.6.4.1 `[p.43]`。

**与常识/相邻概念的混淆点**
- ≠ **Importer/Filer Misdeclaration**（g13）：后两者是**申报数据**错误；Substitution 是**实物与报关对应关系**的伪造。
- 与 Failure to Hold（g11）是「手段—目的」关系，**默认按 Failure to Hold 处理直到查明**；调查结论可能落到 negligence / gross negligence / fraud。
- 举证硬要求（6.6.4.4 `[p.44]`）：须查验**整票**（否则进口商可事后主张未查验部分未被调包）、照片 invaluable、须收集「隐瞒调包的证据」（调包物常置于托盘中央/底部或车厢前部）、差异说明作成 affidavit。

**混淆后会导致什么判定错误**：只核对单据不查实物 → 完全漏识别；只抽检部分货物 → 证据链被「未查验部分未调包」抗辩击穿；误归入 misdeclaration → 走错调查路径（filer evaluation 而非 8 步 Failure to Hold 清单 + CBP 4647 + bond 核定）。

**tags**：`[term, violation-pattern, evidence-chain]`

---

### g13 · Importer Misdeclaration vs Filer Misdeclaration — 进口商误申报 vs 报关行误申报（★ 成对）

**作者定义**
> `6.9.47 – Importer Misdeclaration`："Refers to **the importer's providing incorrect and/or incomplete information** to the FDA and CBP, usually via the filer. This misdeclaration may include incorrect product codes and/or product descriptions; incorrect/incomplete manufacturer/shipper name/address; and/or incorrect quantity and value. It may occur as an attempt to avoid FDA and/or CBP actions/regulations, such as DWPE, sampling, duties, etc." `[p.55]`
> `6.9.35 – Filer Misdeclaration`："Refers to **the importer's provision of correct information to the filer, who then files an erroneous entry** to the FDA and CBP." `[p.54]`
> `6.6.4.6`（责任归属）："Although this section is oriented to filer interventions, it must always be recognized that **the filer is the agent of the importer, and the importer is ultimately responsible.**" `[p.45]`

**中文自译**：分界唯一标准是**错误信息源自谁**——进口商给 filer 的信息本身就不正确/不完整 → Importer Misdeclaration；进口商给的信息正确、但 filer 录入/申报出错 → Filer Misdeclaration。

**出处**：IOM 6.9.47 `[p.55]`、6.9.35 `[p.54]`；6.6.4.5 `[p.44–45]`、6.6.4.6 / 6.6.4.6.1（Repeated Filer Misdeclaration）`[p.45]`、6.7 Filer Evaluations `[p.45]`。

**与常识/相邻概念的混淆点**
- ★ 不是「谁被处罚」的分类，而是**错误来源**的分类；且即便 filer 出错，**进口商仍负最终责任**（6.6.4.6）。
- 后续路径不同：Filer Misdeclaration 连到 6.7 **periodic filer evaluation** 与 6.6.4.6.1 Repeated Filer Misdeclaration；Importer Misdeclaration 走进口调查。
- 常见诱因是规避 DWPE、取样、关税（6.9.47）——与 g06 / g19 联动。
- ≠ Substitution（g12，实物层面）。
- 任何影响 PREDICT 的字段错误都必须**更正 → 指派责任方 → 保存 → rescreen**（g19）。

**混淆后会导致什么判定错误**：错分责任源 → 对进口商启动 filer evaluation（对象错）或漏掉对 filer 的 Repeated 处置；误以为 filer 出错可免除进口商责任 → 追责对象缺失；更正数据后忘记 rescreen → 后续判定建立在脏数据上。

**tags**：`[term, paired, liability, violation-pattern]`

---

### g14 · FSVP (and/or HACCP) Importer vs Importer of Record — FSVP 进口商 vs 报关登记进口商（★ 成对）

**作者定义**
> `6.9.40 – FSVP and/or HACCP Importer`："The importer who, for a specific food, is subject to the importer requirements in FDA's FSVP regulation (21 CFR part 1, subpart L)... the importer is the **U.S. owner or consignee at the time of entry** into the United States or the **U.S. agent or representative** of the foreign owner or consignee... **An FSVP or HACCP importer must be physically located in the United States.**" `[p.55]`
> `6.9.43 – Importer of Record`："The party **in whose name the entry is made**. Note that... a Customs House Broker might make an entry and become the 'importer of record' by using their importer ID and bond on behalf of their client, the true 'importer' of the goods. For FDA purposes, the 'importer of record' is the person or company **filing the redelivery bond** under Sections 802(b) and 536(b)." `[p.55]`
> `6.8.3.1.1`（检查时逐产品验证）："For each product covered during the inspection, **verify that the importer meets the definition of 'importer'**... If the importer was the U.S. agent or representative... attach a copy of the written agreement to serve as the FSVP importer." `[p.50]`

**中文自译**：FSVP Importer 是 FSMA / 21 CFR 1 Subpart L（或 juice/seafood HACCP）下对境外供应商履行验证义务、须接受 FDA 记录审查的主体，须为入境时点的美国 owner/consignee 或其 U.S. agent/representative，且**必须位于美国境内**；Importer of Record 是 CBP 报关名义主体，报关行可用自己的 ID 与 bond 代为成为，FDA 语境下即提交 redelivery bond 者。

**出处**：IOM 6.9.40 / 6.9.43 `[p.55]`、6.8.3.1.1 `[p.50]`、6.8 第 68 行（Very Small Importer, VSI）`[p.47]`；对照 6.9.65 Reconditioning 申请主体、6.9.66 bond 主体。

**与常识/相邻概念的混淆点**
- ★ **两套法律身份、两个法域**：Importer of Record 属 CBP（报关/关税/保证金）；FSVP Importer 属 FSMA（供应商验证/记录审查）。**二者常常不是同一人**；术语表还刻意区分 "importer of record" 与 "true 'importer'"。
- **Reconditioning 申请主体 = importer of record**（6.9.65）；**FSVP 检查对象 = FSVP importer 的记录**（6.8）。用错主体，文书与检查都无效。
- `must be physically located in the United States` 是硬约束，境外货主不能直接当 FSVP importer。
- 还有变体：HACCP importer（21 CFR 120.14 / 123.12）、Very Small Importer (VSI)。

**混淆后会导致什么判定错误**：把报关行当 FSVP 义务人 → FDA 483a / T-EIR 开错对象、记录审查无的放矢；把 Importer of Record 当 Reconditioning 申请人 → 找错签字与 bond 主体；忽略「须位于美国境内」→ 把境外货主误列为 FSVP importer，检查结论不成立。

**tags**：`[term, paired, legal-identity, core-concept]`

---

### g15 · SDI vs ADS (vs DI Sample) — 特殊国内进口样品 vs 附加样品（★ 成对，6.9 缺 SDI）

**作者定义**
> `6.4.9 – Special Domestic Import Samples (SDI)`："The SDI sample work type should **only** be used when directed by a special sampling assignment, for certain perishable products collected for metal (MET) analysis or for products collected for nutritional analysis (NIS). **It should not be used when collecting samples for multiple PAFs, or if the product appears to be violative or has a history of being violative.**" `[p.37]`
> `6.4.8 – Additional Samples (ADS)`："An additional sample (referred to as 'ADS' in FDA Import Systems) is a physical sample collected from a **previously sampled lot**... Additional import samples will have a **different sample number** from the original sample number... **The additional sample must be collected from the same entry line as originally sampled.**" `[p.37]`
> `6.9.24 – Domestic Import (DI) Sample`："A sample of an imported article collected **after it has been released from import status**." `[p.53]`；`6.9.2 – Additional Sample` `[p.50]`

**中文自译**：ADS 是对**已取样批次的同一 entry line** 补采/加测的样品，样品号与原样不同、须在 Remarks 关联原号；DI Sample 是货物**已脱离进口状态后**才采集的进口货样品；SDI 是特殊抽样任务下、针对特定易腐品 MET/NIS 分析的国内进口样品，且明文禁止用于多 PAF 或已显违规/有违规史的产品。

**出处**：IOM **6.4.8 / 6.4.9 `[p.37]`**、6.4 第 59–60 行（ADS 须记同一 entry/line）`[p.33]`、6.5 第 11–32 行（SDI 额外要求）`[p.39]`；6.9.2 `[p.50]`、6.9.24 `[p.53]`。

**与常识/相邻概念的混淆点**
- ★ 三者是**不同维度**，不是同义/递进关系：ADS = 补样（同批同行）；DI = 放行后取样（时点）；SDI = 特殊任务下的国内进口样品（用途 + 任务前提）。
- **SDI ≠ DI Sample 的缩写**：SDI 有独立适用前提，且要求更严的证据（标签描述、官方封条 FDA 415a、采集人 ID），目的是 FDA 检出违规时**启用国内管辖权**（BOOK_OVERVIEW 命题 7、6.5 `[p.39]`）。
- **6.9 术语表只收了 Additional Sample 与 DI Sample，没有 SDI**（见 0.4）。
- SDI 明文禁用于「已显违规 / 有违规史」产品——与「检出违规后启用国内管辖权」的用途看似矛盾，靠"special sampling assignment 指令"限定。
- ADS 必须与原样同一 entry/line（6.4 第 60 行 `[p.33]`）。

**混淆后会导致什么判定错误**：把 SDI 当普通补样 → 对已显违规产品误用该 work type，丢失国内管辖权证据链（封条/采集人 ID），后续无法在国内追责；把 ADS 当全新样品 → 样品号与 entry/line 关联断裂，实验室结果无法并入原案；把「放行后取样」(DI) 与「放行前取样」混同 → 误判 FDA 管辖权基础。

**tags**：`[term, paired, sample-type, source-gap, evidence-chain]`

---

### g16 · Audit Sample — 审核样品

**作者定义**
> `6.9.6 – Audit Sample`："A sample collected to **verify analytical results provided by a certificate of analysis, or private laboratory analysis** that purports to show a product complies with the FD&C Act and/or regulations. This sample type will usually be used with an import sample. **At least one FDA audit sample should be included as evidence when processing removal of a product, shipper, or country from DWPE.**" `[p.51]`

**中文自译**：为核验 COA 或私人实验室「产品合规」分析结论而由 FDA 采集的样品；把产品/发货人/国家从 DWPE 名单移除时，至少须附一份 FDA 审核样品作为证据。

**出处**：IOM 6.9.6 `[p.51]`（交叉引用 `IOM 4.1.4.2.8` 括号未闭合，见 0.3-c）、6.9.22 `[p.52]`、6.6.4.1 第 5 步提及 audit sample collection 场景 `[p.43]`。

**与常识/相邻概念的混淆点**
- ★ ≠ 企业提交的 COA / 私人实验室报告——它恰恰是**用来核验这些外部结论的 FDA 自采样品**。
- ≠ **ADS**（g15）：ADS 是补做原分析/加测；Audit Sample 是验证外部分析结论。
- ≠ **Private Laboratory**（6.9.63 `[p.57]`）出具的结果。
- 与 **DWPE 解除**强绑定，是硬性证据门槛（g06）。

**混淆后会导致什么判定错误**：把进口商提交的私人实验室合格报告当解除 DWPE 的证据 → 忽略「至少一份 FDA audit sample」，移除申请不成立；把 ADS 当 audit sample → 证据类型不符，案卷被退回。

**tags**：`[term, sample-type, dwpe-removal]`

---

### g17 · Import Alert vs Import Bulletin — 进口警报 vs 进口通报（★ 成对，6.9 缺 Bulletin）

**作者定义**
> `6.9.42 – Import Alerts`："Guidance documents concerning significant re-occurring, new, or unusual problems affecting import coverage. They can be found online here." `[p.55]`
> `6.9.22 – DWPE`（补足 Alert 的实际效力）："'Import Alerts' list products that **may be detained without physical examination** due to their violative history or potential." `[p.52]`
> Import Bulletin **6.9 无条目**；正文线索：
> `6.2` 情报来源清单："Import Alerts (IA) and **Import Bulletins (IB)**" `[p.15]`；
> `6.2.2.2.x` 请求现场工作的情形之一："**An Import Bulletin directs you to do so.**" `[p.17]`；
> `6.2.2.2.x` 重要提示："**Import Alerts (IA): Do not routinely request work for a line that is already subject to an Import Alert.**" `[p.17]`；
> `6.3`："examination was performed due to an assignment, **import bulletin, or import alert**" `[p.31]`；`6.4` 第 266 行 "Alert/Bulletin requires" `[p.37]`。

**中文自译**：Import Alert 是列名「因违规历史/可能性可免实物查验扣留」的产品/企业的指导文件；Import Bulletin 是**指示审查员对某 line 请求现场工作/查验**的指导文件。本章未给 Bulletin 正式定义，须由正文用法反推。

**出处**：IOM 6.9.42 `[p.55]`、6.9.22 `[p.52]`；**6.2.2.2.x `[p.15]/[p.17]`、6.2.5.3 `[p.21–22]`、6.3 `[p.31]`**。

**与常识/相邻概念的混淆点**
- ★ **Import Alert (IA)** 关联 **DWPE / DER**：命中后「不要例行请求现场工作」，走 DER 免查验扣留（g06/g07）。
- ★ **Import Bulletin (IB)** 是**指示请求现场工作**的文件，**不触发 DWPE**；6.2 把它列为请求现场工作的合法理由之一。
- 方向几乎相反：Alert → 别再查、直接扣；Bulletin → 去查。
- 6.9.42 措辞偏弱（"guidance documents... can be found online here"），**不能单读**，必须与 6.9.22 + 6.2.5.3 合读才能看到强制扣留效力。
- **★ 缩写陷阱**：IB 同时是 Import Bulletin **和** Investigations Branch（g04）；"IB Release" 属于后者。
- DER 免单据提交的前提之一是「电子数据匹配 Import Alert 条件」；若 Alert 要求特定证书（如 IA 28-02）仍须先索单据（6.2.5.3 `[p.21–22]`）。

**混淆后会导致什么判定错误**：把 Bulletin 当 Alert → 对未受 DWPE 覆盖的货物误走 DER 免查验扣留；把 Alert 当 Bulletin → 对已受 DWPE 约束的货物又去请求现场查验（6.2 明确禁止），浪费资源且可能误放行；把 "IB Release" 读成「按 Import Bulletin 放行」→ 完全找错文书与流程。

**tags**：`[term, paired, routing, homonym, source-gap, core-concept]`

---

### g18 · Prior Notice of Imported Foods — 进口食品事先通知

**作者定义**
> `6.9.62 – Prior Notice of Imported Foods (Prior Notice)`："In the case of an article of food that is being imported or offered for import into the United States, a notice provided to the **FDA prior to entry**... with information about the article, manufacturer, shipper, grower, the country of origin, and anticipated port of entry. Prior notice must be submitted to the FDA **electronically, via either the CBP ACE or the FDA PNSI**." `[p.57]`
> `6.1.5`（时限）："**Two hours** before arrival by land by road / **Four hours** before arrival by air or by land by rail / **Eight hours** before arrival by water" `[p.9]`
> `6.1.5.5`："Food that is imported or offered for import with **inadequate prior notice is subject to refusal and holding**..." `[p.11–12]`

**中文自译**：食品/动物饲料抵达前须向 FDA（经 CBP ACE 或 FDA PNSI）电子提交、含 15 项信息（21 CFR 1.281）并取得确认的独立预先通报；时限按运输方式为抵达前 2 / 4 / 8 小时；通报不充分本身即可构成拒绝与扣留理由。

**出处**：IOM 6.9.62 `[p.57]`、6.1.5 / 6.1.5.1–6.1.5.6 `[p.9]–[p.12]`（6.1.5.4 列 15 项必填信息 `[p.10–11]`）。

**与常识/相邻概念的混淆点**
- ★ ≠ 报关单的一部分：是**发给 FDA**、有电子确认回执的**独立法定前置义务**（21 CFR 1.281），只是可搭 ACE 通道传输。
- 时限是「抵达**前**」2/4/8 小时，不是抵达后补交，也不是统一 8 小时。
- 仅适用于 **food / animal feed**（6.1.5 标题），不是所有 FDA 监管商品。
- 有豁免/排除清单（6.1.5.3 `[p.10]`）与 IFE（Import for Export）等特殊情形（6.1 `[p.9]` 要求 IUC 与 A of C 同时具备）。
- Inadequate Prior Notice 本身即 refusal 理由，不需先证明产品不合格。

**混淆后会导致什么判定错误**：以为随报关单一起提交即可 → 未在法定时限内单独向 FDA 提交，货物被拒；把 2/4/8 记成统一时限或「抵达后」→ 时限判定错误；把 Food 之外商品套用或把豁免清单漏判 → 适用性判定错误；忽略 inadequate → 未及时出 Refusal / holding。

**tags**：`[term, core-concept, time-window, legal-obligation]`

---

### g19 · PREDICT — 预测性风险筛查系统

**作者定义**
> `6.9.61 – Predictive Risk-Based Evaluation for Dynamic Import Compliance Targeting (PREDICT)`："A **risk-based analytics tool** that the FDA uses to **electronically screen all regulated shipments** imported or offered for import into the United States." `[p.57]`
> `6.2.2.1`："This system includes PREDICT, a screening tool that helps **identify high-risk shipments**. PREDICT does this by analyzing: [risk score, mashup grid, rule flags]" `[p.16]`
> `6.2.5.2`："Note: All information in 'Line Details' must be accurate. **Inaccurate data will affect PREDICT screening.**" `[p.21]`

**中文自译**：PREDICT 是 FDA 对所有拟入境监管货物进行电子风险筛查的分析工具，输出风险评分、mashup grid 与规则标记，用于识别高风险货物。

**出处**：IOM 6.9.61 `[p.57]`、6.2.2.1 `[p.16]`、6.2 第 53 / 71 / 83 / 176 / 196 / 211 行 `[p.14]–[p.17]`、6.2.5.2 `[p.21]`、6.2.5.3 第 539 行 "Update and **rescreen** the entry if you make corrections" `[p.22]`、6.1.7 VQIP `[p.13]`。

**与常识/相邻概念的混淆点**
- ★ **≠ 自动判决**：是审查的**输入**，不是可采性决定。审查员可作出与 PREDICT 相悖的 May Proceed，但**必须写明具体理由**（6.2 第 83 行 "Issue a may proceed that contradicts PREDICT screening results" `[p.15]`、第 176 行 `[p.17]`）。
- 必须与电子/纸质单据、Import Alert、历史合规记录**合用**，不能只凭其中一项（BOOK_OVERVIEW 命题 1）。
- **数据脏 → 筛查失真**：任何影响筛查的字段错误（制造商、发货人、产品代码、数量）须 **更正 → 指派责任方 → 保存 → rescreen**（6.2 第 53 行 `[p.14]`、6.2.5.3 `[p.22]`）。
- ≠ May Proceed（g02）：筛查结果与放行决定是两件事；PREDICT 规则出错须用系统反馈功能上报（6.2 第 211 行 `[p.17]`）。
- VQIP 通过在 PREDICT 中设筛查规则识别获批申请（6.1.7 `[p.13]`）。

**混淆后会导致什么判定错误**：把高风险评分当「已判定违规」→ 跳过人工审查与举证；把自动放行/低分当「FDA 已判定合规」→ 忽略 May Proceed 未作合规判定；更正数据后忘记 rescreen → 后续所有判定建立在脏数据上；相悖放行不写理由 → 违反 6.2 明令，案卷不可辩护。

**tags**：`[term, core-concept, screening, data-integrity]`

---

### g20 · Affirmation of Compliance (A of C) vs Intended Use Code (IUC) — 合规申明 vs 用途代码（★ 成对，6.9 缺 IUC）

**作者定义**
> `6.9.4 – Affirmation of Compliance (A of C)`："**Data elements transmitted to FDA electronically that affirm a product meets a specific FDA regulation.** This value is provided to help expedite the FDA's review of product compliance in making an admissibility decision at time of entry. Some affirmations require a qualifier, which are numeric or alpha-numeric values representing a specific firm, product, certification, registration, application, or other value often on file with the FDA." `[p.51]`
> `6.1.6.2`（IUC 唯一定义处）："FDA's system enhancements include establishing **Intended Use Codes (IUC) to assist entry reviewers in determining the end-use of the imported product**. Commodities will fall in one of the three categories: IUC is required / optional / not applicable. Affirmation of Compliance (or A of C) codes... are also used by filers to affirm that the firm and/or product identified in an FDA line meet the requirements specific to the product being imported. **A of C code requirements are dependent on the commodity being imported and can be impacted by the IUC.**" `[p.13]`

**中文自译**：A of C 是 filer 电子传输、申明产品符合某项具体 FDA 法规的数据元素，可带 qualifier（企业/产品/认证/注册/申请号）；IUC 是帮助审查员判定进口产品最终用途的代码，按商品分「必需/可选/不适用」三类；**A of C 的适用要求会被 IUC 影响**。

**出处**：IOM 6.9.4 `[p.51]`、**6.1.6.2 `[p.13]`（IUC 唯一定义，6.9 无此条）**；6.1 IFE 段（须同时具备 IUC "Import for Export" 与 IFE A of C）`[p.9]`、6.2 第 231 / 243 行 `[p.17]`、6.3 第 24 行（禁止仅凭 A of C 缺失扣留）`[p.23]`、6.9.64 Product Code `[p.57]`。

**与常识/相邻概念的混淆点**
- ★ 看似元数据，**实为可采性判定依据**；且 **IUC 会改变 A of C 的要求**——二者不是独立字段，须联动校验。
- ★ **但不能仅凭 A of C 缺失就扣留**：6.3 第 24 行明确否定 "detention based solely on a failed data lookup or **missing Affirmation of Compliance data**" `[p.23]`；且系统自动校验通过时**不得再人工复核** A of C（6.2 第 243 行 `[p.17]`）。这两条与「A of C 是判定依据」形成看似矛盾的边界。
- ≠ **Product Code**（6.9.64 `[p.57]`，描述具体产品的 5–7 位字母数字码，须与实际品名/发票描述一致）。
- ≠ PREDICT 评分（g19），但 A of C / IUC 填错会影响筛查 → 须更正并 rescreen。
- 6.9 未收 IUC（见 0.4）。

**混淆后会导致什么判定错误**：把 A of C / IUC 当无害元数据 → 填错不更正、不 rescreen，PREDICT 与后续判定全错；反过来仅因 A of C 缺失就扣留 → 违反 6.3 明确禁止的做法；把 IUC 与 A of C 当独立字段分别校验 → 漏掉用途变更引发的合规要求变化（如 IFE 情形，6.1 `[p.9]`）。

**tags**：`[term, paired, data-element, source-gap, admissibility]`

---

### g21 · ITACS — 进口贸易辅助通信系统

**作者定义**
> `6.9.50 – Import Trade Auxiliary Communication System (ITACS)`："A system that provides the **import trade community** with four functions: the ability to check the status of FDA-regulated entries and lines, the ability to submit entry documentation electronically, the ability to electronically submit the location of goods availability for those lines targeted for FDA exam, and the ability to check the estimated laboratory analysis completion dates... ITACS account management functionality enables the electronic distribution of **Notices of FDA Action** via email and as downloads." `[p.56]`

**中文自译**：面向进口贸易界提供四项功能的对外系统：查 entry/line 状态、电子提交单据、报送待查验货物的可用地点、查询取样行的实验室预计完成日期；并支持以邮件/下载方式分发 Notice of FDA Action。

**出处**：IOM 6.9.50 `[p.56]`、6.9.27 Entry Documents `[p.53]`、6.2.2.1 第 146 行（ITACS 提交单据获初审优先）`[p.16]`、6.2 第 387 / 401–402 / 506 行（系统外收到单据须上传）`[p.20]/[p.21]`、6.1.6.2 `[p.13]`、6.3 第 442 行 `[p.30]`。

**与常识/相邻概念的混淆点**
- ★ ≠ FDA 内部审查系统：PREDICT / OASIS / SERIO（6.9.31 `[p.53–54]`）是 FDA 侧；**ITACS 是对外接口**，使用方是 filer / 进口贸易界。
- 但单据经 ITACS 提交会获得**初审排序优先**（6.2.2.1 `[p.16]`），因此间接影响审查时序；系统外收到的单据**必须回传进 FDA Import System**（6.2 第 506 行 `[p.21]`）。
- **名称不一致**：6.9.50 标题作 `…Communication System`（单数），6.9.27 / 6.2 / 6.4 正文多处作 `…Communications System`（复数）（见 0.3-h）。
- 有 ITACS 账户者可选邮件/下载接收 Notice of FDA Action（6.1.6.2 `[p.13]`）——与「通知送达」相关。

**混淆后会导致什么判定错误**：把 ITACS 当审查决策系统 → 误以为「单据一提交即被审查/放行」；忽略 ITACS 提交优先 → 排程判断错误；把单复数名称差异当两个系统 → 检索与交叉引用漏项；系统外单据未上传 → 案卷缺件。

**tags**：`[term, system-interface, naming-inconsistency]`

---

### g22 · OGA / PGA — 其他政府机构 / 合作政府机构

**作者定义**
> `6.2.2.2.6 – Partner/Other Government Agency (OGA) Referral`："Use the OGI (Other Government Agency - Investigations) and OGC (Other Government Agency - Compliance) work types to **close an entry line without the FDA making an admissibility decision**. This is done when another government agency is handling the entry." `[p.19]`
> `6.2` 第 105 行："Note: **Other Government Agencies (OGAs) are also known as Partnering Government Agencies (PGAs).**" `[p.15]`
> `6.2.2.2.6`："You can close a line with an OGA referral when another agency (like CBP) has decided to refuse or seize a shipment. **Before you close the line, you must obtain and upload documents** that show what the other agency did with the product." / "If you only need to share information... use an **Ad-Hoc OGA Referral (an Ad-Hoc referral does not close the line)**." `[p.19]`

**中文自译**：OGA 与 PGA 指同一批机构（含 CBP 等，FDA 自身也以 FD1/FD2/FD3 flags 列为 PGA 之一）。OGA Referral 用 OGI / OGC 两种 work type，在**其他机构处理该票时让 FDA 不作可采性判定即关闭该 line**；Ad-Hoc 型只共享信息、不关闭 line。

**出处**：IOM **6.2.2.2.6 `[p.19]`**、6.2 第 93 / 103 / 105 / 114 行 `[p.15]`、6.1 第 93–94 行（PGA/OGA、OCI）`[p.7]`、6.1.6.2 第 378 / 402–403 行（PGA flags、46 个 PGA）`[p.12]`。

**与常识/相邻概念的混淆点**
- ★ **OGA = PGA 是同一批机构**，不是两类；展开词不统一（6.1 `Partner Government Agencies` / 6.2 `Partnering Government Agencies`，见 0.3-h）。FDA 自己也是 PGA 之一。
- ★ **OGA Referral 的法律后果是「FDA 不作可采性判定就关闭 line」**——不是「转交协查，FDA 仍会出决定」。
- **Ad-Hoc OGA Referral 不关闭 line**（6.2 第 349 行 `[p.19]`），仅共享信息、FDA 仍作初始判定；两者不可混用。
- OGI → Investigations Branch (**IB**)，OGC → Compliance Branch (**CB**)（见 g04 缩写）。
- 关闭前须上传证明其他机构已如何处置货物的文件。

**混淆后会导致什么判定错误**：把 OGA Referral 当普通协查 → 误以为 FDA 仍会出可采性判定，结果 line 被关闭、无 FDA 决定；Ad-Hoc 与关闭型混用 → 该关的没关、不该关的被关；把 FDA 排除在 PGA 之外 → FD1/FD2/FD3 flags 归属判断错误。

**tags**：`[term, paired, routing, jurisdiction]`

---

### g23 · VQIP / QAP — 自愿合格进口商计划 / 质量保证计划

**作者定义**
> `6.1.7 – Voluntary Qualified Importer Program (VQIP) Entry Processing`："The Voluntary Qualified Importer Program (VQIP) is a **voluntary, fee-based** program that provides **expedited review**... The FDA works with CBP to expedite entry of VQIP foods... The agency sets screening in its **PREDICT** import screening system to recognize shipments of food that are the subject of an **approved VQIP application**... The FDA **limits** its examination and/or sampling of VQIP food [to] obtain statistically necessary risk-based microbiological samples, and to **audit the effectiveness of VQIP**." `[p.13]`
> `6.9.76 – VQIP Quality Assurance Program (QAP)`："A compilation of the written policies and procedures used to ensure adequate control over the safety and security of the foods being imported by the VQIP importer." `[p.58]`

**中文自译**：VQIP 是自愿、付费的快速审查计划，经**获批申请**后由 PREDICT 设规则识别；FDA 仍保留为公共卫生理由查验/取样、统计性微生物取样与审计 VQIP 有效性的权利。QAP 只是 VQIP 要求的一套书面政策与程序汇编。

**出处**：IOM **6.1.7 `[p.13]`（VQIP 本体定义，6.9 无此条）**、6.9.76 `[p.58]`（仅 QAP）、6.1 第 137 行（PNSI）`[p.8]`。

**与常识/相邻概念的混淆点**
- ★ **不是合规认证、不是豁免**：是"加速审查"资格，FDA 仍可为公共卫生理由查验/取样；且须有 **approved application** 且 PREDICT 已设识别规则。
- **QAP ≠ VQIP**：6.9 只收了 QAP，极易让人误以为「VQIP 就是那套文件」；文件齐备 ≠ 已获批。
- 通过 PREDICT 规则识别（与 g19 联动），不是人工豁免名单。
- 仅针对 **food**（6.1.7 标题 Entry Processing）。

**混淆后会导致什么判定错误**：把 VQIP 当「免检资格」→ 误以为可跳过 Prior Notice / 可采性判定 / 取样；把 QAP 文件齐备当「已获 VQIP 批准」→ 忽略 approved application 与 PREDICT 识别规则，误给加速待遇。

**tags**：`[term, source-gap, program-vs-document]`

---

### g24 · Notice of FDA Action — FDA 行动通知

**作者定义**
> `6.9.57 – Notice of FDA Action`："Gives notice to the owner, operator, or agent-in-charge of an imported product, providing more specific information on the actions taken by the agency, **broken down by each entry line** (including, 'sample collected,' 'intended for sampling,' 'detained,' 'released,' or 'refused'). The notice provides notification of **the right to a hearing** on the detention of a product which appears violative to the FDA... The notice **identifies the charges** for which the product appears violative." `[p.56]`
> `6.1.6.2`："FDA Import Systems will generate a 'Notice of FDA Action'... **As the status changes for a particular line, a new 'Notice of FDA Action' will be issued**" `[p.13]`

**中文自译**：按每个 entry line 逐项告知 FDA 已采取动作（已取样 / 拟取样 / 扣留 / 放行 / 拒绝）的通知；扣留版本同时告知听证权并列出指控（charge）；状态每变化一次就出具新通知；抄送 filer、importer of record、consignee。

**出处**：IOM 6.9.57 `[p.56]`、6.1.6.2 `[p.13]`、6.5.2.8（Refusal 版 charge 须与 Detained 版逐字一致）`[p.41]`、6.3.10.7（Remarks 不出现在通知上）`[p.32]`、6.2 第 439 行（narrative 字段出现在公开版）`[p.20]`。

**与常识/相邻概念的混淆点**
- ★ ≠ 单一「扣留通知」：是**按 line 逐项、随状态变化反复出具**的系列通知；状态值有 5 类。
- 扣留版本同时是**听证权告知**与 **charge 列明**载体（与 g25 联动）；Refusal 版 charge 必须与原始 Detained 版逐字一致。
- **Remarks 字段不出现在 Notice of FDA Action 上**（6.3.10.7 `[p.32]`），但 narrative 字段会出现在**公开版**通知（6.2 第 439 行 `[p.20]`）——记录位置选错等于没送达。

**混淆后会导致什么判定错误**：把一次通知当全流程唯一文书 → 漏掉状态变更后的新通知、漏掉按 line 拆分；把关键放行理由写进 Remarks 以为会送达进口商 → 正式通知中无据，听证无法辩护；charge 前后不一致 → Refusal 程序瑕疵。

**tags**：`[term, document, per-line, hearing-right]`

---

### g25 · Detention and Hearing Process / Testimony — 扣留听证程序 / 证言

**作者定义**
> `6.9.23 – Detention and Hearing Process`："The opportunity for an importer or designee to **present evidence, or testimony, to overcome the appearance of a violation** and to give the FDA confidence that the product is in compliance... **The evidence must be provided during the hearing period.** The format for providing this evidence may vary from **a series of email or telephone conversations to a more formal meeting**." `[p.52–53]`
> `6.9.75 – Testimony`："An individual's statement given in writing (such as an affidavit or a declaration) or by appearance under oath at a proceeding... Testimony may also be **information a firm submits to overcome the appearance of the violation**, or to otherwise support the release of their product. Testimony should be provided to the contact listed on the FDA Notice of Action, which is usually a **compliance officer**." `[p.58]`
> `6.9.3 – Affidavit`："...a written document for which the signer swears before an authorized official (FDA)... The signer is referred to as the **affiant** and has knowledge of material facts relating to the movement or condition of the goods." `[p.50]`

**中文自译**：听证是进口商在**听证期内**提交证据/证言以推翻「违规外观」的机会，形式可从一串邮件/电话到较正式会议，属非正式程序；Testimony 范围很宽（书面 affidavit/declaration、出庭宣誓、邮件、电话、传真、硬拷贝），企业为支持放行提交的信息也算；接收方通常是 Notice of Action 上列名的 compliance officer。

**出处**：IOM 6.9.23 `[p.52–53]`、6.9.75 `[p.58]`、6.9.3 `[p.50]`；6.9.57（通知告知听证权）`[p.56]`、6.6.4.1 第 5 步（说明作成 affidavit）`[p.43]`。

**与常识/相邻概念的混淆点**
- ★ "hearing" 是**非正式**程序（informal meeting，甚至一串邮件/电话），≠ 行政法庭式听证；但**证据必须在听证期内**提交，逾期不补。
- 举证目标是 "overcome the **appearance** of a violation"，与 Detention 的临时性/外观标准（g05）一致，不是证明「绝对合格」。
- Testimony ≠ 仅出庭作证：书面 affidavit / declaration / 邮件 / 电话 / 传真 / 硬拷贝都算；affidavit 须向 FDA 授权官员宣誓、affiant 须对货物移动或状况有实质事实认知。
- 接收方是 **compliance officer**，不是 entry reviewer。

**混淆后会导致什么判定错误**：按正式听证准备 → 错过 informal 窗口期、证据逾期失权；把 testimony 只理解为出庭作证 → 漏掉书面 affidavit/declaration 这一主要举证形式；把材料发给审查员而非 compliance officer → 未进入案卷，视为未举证。

**tags**：`[term, procedure, evidence, informality]`

---

### g26 · Re-export — 再出口

**作者定义**
> `6.9.67 – Re-export`："A term used to identify goods shipped out of the United States **after being offered for entry**. This is **not the same as an export of U.S. manufactured goods** and is **not covered by the restrictions in Section 801(e)** of the FD&C Act." `[p.57]`

**中文自译**：指货物**已申报入境之后**又运出美国；不同于美国制造品的出口，且**不适用** FD&C Act §801(e) 的出口限制。

**出处**：IOM 6.9.67 `[p.57]`；对照 6.9.1 AGR `[p.50]`、6.9.44 / 6.5.2.8（Refusal 后出口）`[p.55]/[p.41]`。

**与常识/相邻概念的混淆点**
- 与 "export" 的法律后果完全不同：Re-export 是「已申报入境后又运出」的外国货（常见于 Refusal 后处置），**不适用 §801(e)** 对美国制造品出口的限制。
- 与 **AGR**（g27）方向相反却同属法定例外：AGR 是「美国货出去又回来」，**被视为进口**（§801(d)(1)）；Re-export 是「外国货进来又出去」，**不受 §801(e) 约束**。两条极易串用。

**混淆后会导致什么判定错误**：把 Refusal 后的再出口当普通出口 → 误套 §801(e) 限制、错开文书；把 AGR 与 Re-export 混用 → §801(d)(1) 与 §801(e) 适用颠倒，审查范围错判。

**tags**：`[term, legal-exception, paired]`

---

### g27 · American/US Goods Returned (AGR / USGR) — 美国货退回

**作者定义**
> `6.9.1 – American/US Goods Returned (AGR or USGR)`："Goods produced in the U.S. which are exported, and then returned to the United States. **They are considered imports.** (See Sec. 801(d)(1) of the FD&C Act [21 U.S.C. 381])." `[p.50]`

**中文自译**：美国生产、出口后又返回美国的货物，**在法律上被视为进口货物**，适用 §801(d)(1)。

**出处**：IOM 6.9.1 `[p.50]`（6.9 首条）；对照 6.9.67 Re-export `[p.57]`。

**与常识/相邻概念的混淆点**
- ★ 常识以为「国货返销不算进口」，作者明确 `They are considered imports` 并挂 §801(d)(1)。
- 与 **Re-export**（g26）是方向相反的两条例外，须成对记忆。

**混淆后会导致什么判定错误**：把 AGR 排除在入境审查外 → 漏掉 Prior Notice / 可采性判定 / 取样；把 AGR 与 Re-export 混用 → §801(d)(1) 与 §801(e) 适用颠倒。

**tags**：`[term, counterintuitive, legal-exception, paired]`

---

### g28 · Release with Comment — 附意见放行

**作者定义**
> `6.9.69 – Release with Comment`："An FDA compliance action **releasing goods into interstate commerce** advising the importer of **violations with the FD&C Act that are not a health risk to the public**. It also advises that **future entries which continue to violate the Act may be refused**." `[p.57]`

**中文自译**：FDA 在明知存在「不具公共健康风险」的违反 FD&C Act 情形时，仍把货物放入州际商业，同时书面告知进口商该违规，并预告后续同类违规的 entry 可能被拒绝。

**出处**：IOM 6.9.69 `[p.57]`；对照 6.9.56 May Proceed `[p.56]`、6.4.3 Release `[p.35]`、6.9.21 Detention `[p.52]`、6.9.42 Import Alert / 6.9.22 DWPE（合规历史输入）。

**与常识/相邻概念的混淆点**
- ★ **放行 ≠ 合规**：这是「已明确认定存在违规（但无公共健康风险）仍放行」的动作，并**预告后续将被拒绝**。
- ≠ **May Proceed**（g02，未作合规判定）／≠ **Release**（6.4.3，查验后放行，未明说违规）：它已明确认定违规。
- ≠ **Detention**（g05）：不扣留，但留下书面警告记录，构成后续 Refusal 的**前科**，会进入合规历史并影响 PREDICT / DWPE / Import Alert 判定。

**混淆后会导致什么判定错误**：把「放行」读成「没问题」→ 企业不整改，后续 entry 被拒时无预警、无准备；把 Release with Comment 当无记录 → 漏掉它会进入合规历史，误判该进口商过往"清白"，低估后续筛查风险。

**tags**：`[term, counterintuitive, compliance-action]`

---

## 3. 成对易混概念速查矩阵（任务点名的 8 对 + 2 对补充）

| # | 成对概念 | 分界判据（一句话） | 混淆后的典型判定错误 | 条目 |
|---|---|---|---|---|
| 1 | **DER vs DTR** | 触发依据（受 DWPE/IA 约束 → DER；其余无法确认可采性 → DTR），**非**严重度 | DWPE 货走 DTR 漏快速扣留；把建议当终局决定 | g07 |
| 2 | **DWPE vs Detention** | 是否需实物查验证据（DWPE 凭历史/Alert 即扣） | 把「不检查」读成「不检查就放过」→ 误放行 | g05 / g06 |
| 3 | **Conditional Release vs May Proceed** | 前者是**等待判定期间的状态**（可移动不可分销、附 bond）；后者是**结束该状态的决定** | 把条件放行当放行 → Failure to Hold + Bond Action | g03 / g02 |
| 4 | **Refusal vs Detention** | Detention 临时可回转；Refusal 是 `final decision` 且之后仍有 90 天处置链 | 发出 Refusal 即归档 → 漏核验销毁/出口、漏 CBP 4647 / bond | g05 / g08 |
| 5 | **FSVP Importer vs Importer of Record** | 法域不同：FSMA 供应商验证义务主体（须在美国境内） vs CBP 报关/关税/bond 主体 | 483a/EIR 开错对象；Reconditioning 申请找错签字方 | g14 |
| 6 | **Importer Misdeclaration vs Filer Misdeclaration** | **错误信息源自谁**（进口商给错 vs filer 录错），非「谁被罚」 | 启动错误的评估路径；误以为 filer 出错可免进口商责任 | g13 |
| 7 | **SDI vs ADS** | SDI = 特殊抽样任务下的国内进口样品（禁用于已显违规品）；ADS = 同批同行补样 | 误用 SDI 丢失国内管辖权证据链；ADS 关联号断裂 | g15 |
| 8 | **Import Alert vs Import Bulletin** | Alert → 命中 DWPE、别再请求现场工作、走 DER；Bulletin → **指示去请求现场工作**、不触发 DWPE | 误走 DER / 对已 DWPE 货又去查验；`IB` 缩写误读 | g17 / g04 |
| 9 | **May Proceed vs Release**（补充） | 系统内两条消息：未经查验无合规判定 / 经查验已作合规判定 | 把 May Proceed 当「FDA 已判定合规」 | g02 |
| 10 | **Re-export vs AGR**（补充） | 外国货「进来又出去」不适用 §801(e) / 美国货「出去又回来」视为进口 §801(d)(1) | 两条法定例外适用颠倒 | g26 / g27 |

**缩写同形异义警示（贯穿 g04 / g17 / g22）**

| 缩写 | 含义 A | 含义 B | 判别法 |
|---|---|---|---|
| **IB** | Import Bulletin（6.2 情报来源清单 `[p.15]`） | **Investigations Branch**（6.2.2.2.6 `[p.19]`、6.3 `[p.31]`） | 「**IB Release**」= 调查分部放行，与 Import Bulletin 无关 |
| **IA** | Import Alert | — | 与 DWPE / DER 绑定 |
| **OGA / PGA** | 同一批机构（6.2 第 105 行明言互为别称） | — | 展开词 `Partner` / `Partnering` 不统一，勿当两类 |

---

## 4. 给下游 skill 的使用提示

1. **6.9 不是穷尽清单**（0.1、0.4）：DER、IUC、Import Bulletin、SDI、IB Release、VQIP 本体均**不在 6.9**，任何"术语表查无此词"的推断都必须先回 6.1–6.8 正文复核。
2. **口径冲突时以系统定义/正文细则为准**：May Proceed 以 6.4.3 系统定义（`No compliance decision has been made`）优先于 6.9.56 的宽松表述；Import Alert 的强制效力须以 6.9.22 + 6.2.5.3 补足 6.9.42。
3. **三个「30 天」与一个「90 天」必须显式区分**：条件放行期长度（6.2.4）/ CBP 请求 redelivery 窗口（6.9.13）/ Failure to Hold 下 4647 期限（6.6.4.1）/ Refusal 后出口销毁（6.9.44、6.5.2.8）。
4. **放行类动作有四种且法律含义不同**：May Proceed、Release、IB Release、Release with Comment；不可统一映射为「放行 = 合规」。
5. **主体字段必须与动作匹配**：Reconditioning / bond / Importer of Record 一组；FSVP 记录审查 / 483a / T-EIR / FSVP Importer 一组。
6. **本词典服务于「理解 FDA 判定逻辑」**，不是企业合规义务清单；法律位阶限制见 `BOOK_OVERVIEW.md` 第 3 节「最强反对意见」，应作为下游能力卡 Boundary (B) 字段来源。

---

## 5. 自检（对照 extractor 规范第 45–49 行）

- [x] `author_definition` 全部使用书中原文片段（英文逐字引用，每段 ≤100 词），并附中文自译。
- [x] `key_distinction` 每条均说明与**常识用法**或**相邻概念**的差异；成对概念以相邻/合并条目组织，8 对点名概念全部覆盖。
- [x] `why_it_matters` 每条均落到**具体判定错误**（放行/扣留/主体/时限/证据链），而非泛泛而谈。
- [x] 数量 28 条，落在任务要求 20–30 条、规范「多于 30 条说明收了一般词汇」的区间内；未机械抄完 78 条。
- [x] 每条记录出处（IOM 6.9.x / 6.x.x + `[p.N]`）；引用前均回原文/切块核验。
- [x] 术语表可追溯性已记录：**6.9 共 78 条；末条 `6-9.78` 与前 77 条 `6.9.x` 编号不一致，属源文件编号瑕疵，已如实标注且未静默修正**（0.2）。
- [x] 覆盖任务列出的全部核对术语：Entry / Line、May Proceed、Conditional Release、Failure to Hold、DWPE、DER、DTR、Prior Notice、Reconditioning、Refusal of Admission、PREDICT、A of C、IUC、FSVP Importer、SDI、ADS、IB Release、Affirmation of Compliance、Import Alert、VQIP、ITACS、OGA/PGA、Bond Action。
