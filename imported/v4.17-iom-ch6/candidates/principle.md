# 原则 / 清单候选 — FDA IOM 2026 · Chapter 6: Imports
## 阶段 1 · principle-extractor 产出

### 扫描范围与口径声明

- **全量扫描**：已逐块读取 `.cangjie/index/` 下全部 9 个含文本章节块，覆盖 6.1（`[p.6]`–`[p.13]`）、6.2（`[p.14]`–`[p.22]`）、6.3（`[p.23]`–`[p.33]`）、6.4（`[p.33]`–`[p.39]`）、6.5（`[p.39]`–`[p.42]`）、6.6（`[p.42]`–`[p.45]`）、6.7（`[p.45]`）、6.8（`[p.46]`–`[p.50]`）、6.9（`[p.50]`–`[p.58]`）；另核对 `MANIFEST.md`、`Exhibits-6-1-to-6-4.txt`（扫描件，无文本层，不产出候选）。
- **force 分类图例**（下游 Boundary 关键字段，每条均标注）：
  - `硬性 hard` — `must` / `shall` / 祈使句 / `Do not` / `only if` / `must be…`；构成不可省略的动作。
  - `裁量 discretionary` — `should` / `as warranted` / `where appropriate` / `if the facts warrant` / `may` / `can` / `ultimately your discretion` / `in general`；属机构判断空间。
  - `混合 mixed` — 同一单元内硬性动作与裁量措辞并存（须拆开读，见 p03/p04/p11/p15）。
  - `定义型 definitional` — `means that…` 的口径定义，本身即硬性判定基准。
  - `元规则 meta` — 用于判读全篇 force 的语用规则（p12）。
- **排除声明**：未把内部 SOP/Job Aid/CPGM/Work Instruction 编号、系统界面点击级操作（如 "click OK"、"double click the work type field"、"navigate to Work Results"）、组织职责分工（Compliance Branch / DTA / OCI / CBP 的职权归属）写成原则。原文引用中出现的表单号（FDA 766、FDA 415a、CBP 3461/7501/4647）、系统名（PREDICT、ITACS、OASIS）仅作为**证据载体/触发依据**出现，不构成原则本身；原则落点是"改不改数据、写不写理由、何时记录、按什么分流"这类可复用的规范性判断。
- **共 15 条**（p01–p15），其中含成体系清单 5 组：照片标识 5 要素（p05）、SCR 九字段（p06）、初审排序（p07）、Prior Notice 时限+豁免（p08）、Failure to Hold 8 步（p09）。
- **引用纪律**：每段英文原文 ≤100 词，多段用多个 `>` 分隔；`…` 为节略号，未改写原意。

---

### p01 · 数据更正链：更正 → 记录理由 → 指派责任 → 保存 → 重新筛查（rescreen）

- **id**: p01
- **type**: principle（规范性动作链）
- **force**: **硬性 hard**（`Correct` / `Assign fault` / `Save and rescreen` 均为祈使；6.2.5.2 用 `must be accurate`）
- **source**: IOM 6.2.1 [p.14]（总纲）；复现于 6.1.4.6.1 [p.9]、6.2.2.2.3 [p.18]、6.2.5.2 [p.21]、6.2.5.3 [p.22]、6.2.5.4.1 [p.22]、6.3.10 [p.30]、6.4.6 [p.35–36]、6.7.1 [p.45]（理据）
- **source_quote**:
  > "Correct any inaccurate data (manufacturer, shipper, product code, quantity, etc.) that could affect PREDICT screening. • Assign fault to the responsible party. • Save and rescreen the entry/line after making corrections." (6.2.1 [p.14])
  > "If the entry/line lacks the IUC IFE and/or the IFE A of C, update the entry/line, record the reason for the update, save, and rescreen the entry/line." (6.1.4.6.1 [p.9])
  > "All information in 'Line Details' must be accurate. Inaccurate data will affect PREDICT screening." (6.2.5.2 [p.21])
- **中文自译**：凡可能影响 PREDICT 筛查的申报数据错误（制造商、发货人、产品代码、数量等）都须更正 → 把错误归属指派给责任方 → 保存 → 重新筛查该 entry/line。IFE 申报缺 IUC/A of C 时同样：更新、记录更新理由、保存、rescreen。"Line Details" 全部信息必须准确，脏数据会污染 PREDICT 筛查。
- **反直觉 / 易错**：① 改完数据**不等于**改完判定，不 rescreen 则后续所有决定建立在旧 flag 上；② "assign fault" 不是处分追责，而是数据归属标注，易被误读为处罚程序；③ 四步是固定顺序，缺"记录理由"或"保存"都会在复核链上断掉；④ 手动录入的 notes 里"记录理由"与系统备注不是一回事。
- **跨章节重复证据（供 V1 验证）**：同一四步链在 **6.1**（IFE 申报）、**6.2**（审查员职责 / 请求现场工作 / DER / 疑似 IA 四类）、**6.3**（查验结果录入）、**6.4**（样品采集报告录入）四个不同环节被逐字复用；6.2.5.2 与 6.7.1 给出理据版（数据质量决定风险判定）。这是全章复现次数最高的操作原则。
- **tags**: [principle, data-integrity, rescreen, hard, cross-chapter-6.1/6.2/6.3/6.4]

---

### p02 · 与系统建议相悖 / 三类判定动作必须写具体理由，禁止 "May Proceed" / "N/A" 空泛备注

- **id**: p02
- **type**: principle（留痕规则 + 禁止性规则）
- **force**: **硬性 hard**（`must write a clear reason` / `Avoid vague remarks` / `must give … clear directions` / `must document all the research`）
- **source**: IOM 6.2.2.2 [p.16–17]（主）；6.2.1 [p.14]（总纲）；复现于 6.2.2.2.3 [p.18]、6.2.3.1 [p.19]、6.2.3.3 [p.20]、6.2.5.1 [p.21]、6.2.5.2 [p.21]、6.2.5.5 [p.23]、6.2.5.4.1 [p.22]、6.3.10.5 [p.31]、6.3.10.7 [p.32]、6.5.2.7 [p.40]
- **source_quote**:
  > "If you decide to issue a 'May Proceed' for a line with a priority review flag, you must write a clear reason in the 'Remarks' field. Vague remarks do not provide enough information." (6.2.2.2 [p.16])
  > "Provide clear remarks in the FDA Import System when you: Request a detention / Request field work / Issue a may proceed that contradicts PREDICT screening results. • Avoid vague remarks like 'May Proceed' or 'N/A'." (6.2.1 [p.14])
  > "Examples of Vague Remarks: 'Line is not subject to IA' / 'NA' / 'May Proceeded'." (6.2.2.2 [p.17])
  > "For any non-routine work, you must give the investigator clear directions in the 'Instruction Text' field." (6.2.2.2.3 [p.18])
- **中文自译**：三类决定（请求扣留、请求现场工作、以及**与 PREDICT 筛查结果相悖**的 May Proceed）都必须在系统备注里写清具体理由；"May Proceed"、"N/A"、"NA"、"May Proceeded"、"Line is not subject to IA" 这类空泛备注被明确禁止。非例行现场工作还须在 Instruction Text 给调查员明确指令。手册同时给出"清晰备注"的正例（"所报品牌不属 DWPE 名单"、"产品为粉剂而非液剂"、"文件证明不含肝素"等），说明合格理由是**可核验的具体事实**，不是结论复述。
- **反直觉 / 易错**：① "May Proceed" 本身是放行动作，把它当备注内容写等于没写理由——这正是被点名的头号错误；② 即使放行是终局动作，也须留下可被听证/复核的具体事实依据；③ 空泛备注的判据不是"字数少"，而是"未提供可核验的具体差异"；④ 这条与 p01 互补：p01 管数据正确性，p02 管决定可辩护性。
- **跨章节重复证据（供 V1 验证）**：**6.2** 内部出现 ≥8 次（总纲、优先级标志、现场请求、DRQ、单据审查、扣留建议、DER 说明、IA 不匹配说明）；**6.3** 把同一逻辑用于"发现违规却裁量放行"（Class 2 须在 Summary 详述理由，[p.31–32]）；**6.5.2.7** 放行改变须"explain the reason for the change of action"。跨 6.2 / 6.3 / 6.5。
- **tags**: [principle, remarks, no-vague-remarks, PREDICT-override, hard, cross-chapter-6.2/6.3/6.5]

---

### p03 · 放行非终局且可撤消；但撤消不重启条件放行期

- **id**: p03
- **type**: principle（判定规则）
- **force**: **混合 mixed** — 撤消触发为 `裁量`（`should only rescind … in rare cases` / `should only occur … in exceptional cases`）；撤消后的动作与期限为 `硬性`（`must act immediately`、`within 24 hours`、CBP `30-day window`、`ends permanently … does not reopen`）；放行含义为 `定义型`（"no compliance decision has been made"）
- **source**: IOM 6.2.2.2.2 [p.17–18]（主）；6.4.3 [p.35]（定义）；复现于 6.2.2.2.1 [p.17]、6.2.4 [p.20]、6.3.11 [p.32–33]、6.5.2.11 [p.42]、6.9.13 [p.51]、6.9.41 [p.55]、6.9.56 [p.56]
- **source_quote**:
  > "You should only rescind a 'May Proceed' in rare cases, such as when a product requires a compliance action. You must act immediately, as this action is not for routine examinations." (6.2.2.2.2 [p.17])
  > "Once you issue a 'May Proceed,' the conditional release period for that entry ends permanently. Even if you rescind the notice, the period does not reopen." (6.2.2.2.2 [p.17])
  > "May Proceed: 'Product may proceed without FDA examination. FDA has made no determination the product complies with all provisions … This message does not preclude action should the products later be found violative.' (No compliance decision has been made.)" (6.4.3 [p.35])
  > "Important: A product that is allowed to enter the country can still face legal action later if the FDA finds it violates the law." (6.2.2.2.1 [p.17])
- **中文自译**：May Proceed 与 IB Release 都可撤消，但仅限"需采取合规行动"等罕见/例外情形，且必须立即执行（主管批准、24 小时内通知 filer 并更新 Notice、24 小时内请求 CBP 设 bond hold、已分销则要求 redelivery，CBP 仅有 30 天窗口）。关键：**发出放行即永久终结条件放行期，撤消也不重开**。且 "May Proceed" 明确表示"未作合规判定"，不排除日后发现违规再采取法律行动。
- **反直觉 / 易错**：① 最易错点——撤消放行**不会**把条件放行期"退回去"，bond/redelivery 的 30 天窗口反而从放行日起算，拖延即丧失救济；② "May Proceed" 字面像"准许继续办理"，实为终局性放行动作，且字面义与定义相反（BOOK_OVERVIEW 术语表已标此差异）；③ 放行 ≠ 合规判定，不产生"已合格"的豁免；④ 硬性动作与裁量触发必须分开读：`should`（是否撤消）与 `must`（撤消后 24h/30d）不可混为一谈。
- **跨章节重复证据（供 V1 验证）**：**6.2.2.2.2**（May Proceed 撤消 7 步）与 **6.3.11**（IB Release 撤消，[p.32–33]）是同一程序的两次完整书写，后者显式引用前者；**6.2.4** 与 **6.9.13 / 6.9.41** 三处重复"条件放行期因 May Proceed/拒绝而结束"；**6.9.56** 重复"放行不排除后续行动"；**6.4.3** 给出 May Proceed / Release 的正式定义对照；**6.5.2.11** 给出 bond 后果。跨 6.2 / 6.3 / 6.4 / 6.5 / 6.9，共 ≥7 处。
- **tags**: [principle, rescind, conditional-release, no-reopen, 30-day-window, mixed, cross-chapter-6.2/6.3/6.4/6.5/6.9]

---

### p04 · 照片证据：政务设备拍摄、上传范围、打印件标识须固定在照片上下方而非照片上

- **id**: p04
- **type**: principle（证据链规则）
- **force**: **混合 mixed，核心为硬性** — 设备/标识/固定位置/上传用 `must`；**触发拍照的情形**用 `裁量`（`when warranted` / `other situations as warranted`，以及 6.3/6.4/6.5 的 `should take` / `as warranted`）
- **source**: IOM 6.1.8 [p.13–14]（枢纽）；复现于 6.3.1 [p.24]、6.3.10.3 [p.30]、6.4.1 [p.33]、6.4.6.8 [p.37]、6.5.2.4 [p.40]、6.5.2.10 [p.41]、6.6.4.4 [p.44]、IOM 5.6.7 / 5.7.3（升级为执法证据，[p.14]）
- **source_quote**:
  > "Photographic evidence must be captured with a government-issued digital device and copied to your work computer's hard drive to prepare it for labeling and uploading to an FDA Import System." (6.1.8 [p.14])
  > "Photographic evidence must be uploaded electronically to the entry/line via FDA Import Systems for all sample collections, Class 2 and Class 3 field/label exams, detention requests (when warranted), destructions, reconditioning, refusal verification discrepancies, and other situations as warranted." (6.1.8 [p.14])
  > "If photographic evidence is printed … the required information must be permanently affixed to the printed photos so that there is never any loss of association … This information must be recorded immediately above or below the photograph(s) (not directly on the photos) so that the integrity of the evidence is not compromised." (6.1.8 [p.14])
- **中文自译**：照片必须用政务配发数字设备拍摄；所有取样、Class 2/3 查验、销毁、重整、拒绝核验差异等情形（及"as warranted"的其他情形）都必须电子上传到对应 entry/line。若打印，标识信息须永久固定在照片**正上方或正下方**（不得写在照片上），以免破坏证据完整性、并永久保持与 entry/line 的关联。
- **反直觉 / 易错**：① "标识固定在照片上下方而非照片上"极反直觉——直觉是把编号写在照片角落，手册明确禁止，理由是"compromise the integrity of the evidence"；② 不得用个人设备；③ 打印件与电子件的标识要求不同（电子设备上传时因系统自动关联，可省略 entry/line 号）；④ 拟采取扣押/禁令/追诉等执法行动时须转用 IOM 5.6.7 / 5.7.3 的更严格程序——同一照片在"行政记录"与"执法证据"下标准不同；⑤ 硬性的是"怎么拍、怎么标、怎么传"，裁量的是"何时值得拍"。
- **跨章节重复证据（供 V1 验证）**：6.1.8 是全章被引用最多的枢纽——**6.3.1**（Class 2/3 查验）、**6.4.1**（所有取样）、**6.5.2.4**（重整后复核）、**6.5.2.10**（销毁/出口核验）、**6.6.4.4**（替换调查，"Photos are invaluable"）五处均以 "(See 6.1.8 PHOTOGRAPHS…)" 回指；6.3.10.3 / 6.4.6.8 把"已拍照片"列为结果字段必填项。跨 6.1 / 6.3 / 6.4 / 6.5 / 6.6。
- **tags**: [principle, photo-evidence, government-device, affix-above-or-below, mixed, hard-core, cross-chapter-6.1/6.3/6.4/6.5/6.6]

---

### p05 · [清单] 照片逐张标识 5 要素

- **id**: p05
- **type**: checklist（成体系清单）
- **force**: **硬性 hard**（`must be identified with the following required information`）
- **source**: IOM 6.1.8 [p.14]；复现于 6.1.8 示例、6.4.1 [p.33]（样品容器外部标识）、6.4.6.7 [p.37]（Hand Ship 的 subs id）、6.3.2 [p.24]（开箱容器标识 FDA/division/日期/主导调查员缩写）
- **source_quote**:
  > "All photographic evidence (including photographs of labeling) must be identified with the following required information: entry/line number, collection/examination date, investigator's initials, a brief description of the photo, and numbering that allows future reviewers to determine if any pages or photos are missing." (6.1.8 [p.14])
  > "(An example of an adequately identified photographic notation: 123-456789-1/11/1; 8/10/20; RS, information panel, right side, 1 of 4)." (6.1.8 [p.14])
  > "However, there is no need to include the entry/line number when uploading from a mobile device or computer file as the photograph(s) will be directly associated to the entry/line." (6.1.8 [p.14])
- **中文自译**：每张照片（含标签照片）必须标注 5 项：① entry/line 号；② 采集/查验日期；③ 调查员姓名缩写；④ 照片内容的简短描述；⑤ 序号（如 "1 of 4"），使后续复核者能判断有无缺页/缺张。标准示例：`123-456789-1/11/1; 8/10/20; RS, information panel, right side, 1 of 4`。从政务移动设备/电脑文件上传时因系统直接关联 entry/line，可省略第 ① 项。
- **清单（5 要素）**：`entry/line 号` | `采集/查验日期` | `调查员缩写` | `照片简述` | `序号（可判缺失）`。
- **反直觉 / 易错**：① 第 ⑤ 项"可判缺失的编号"最易漏——目的不是美观而是让审查者发现"少了哪一张"；② 标签照片同样要标，不是只对实物照片；③ 电子设备上传有例外（免 entry/line 号），打印件无此例外；④ 同类"逐项标识"逻辑在 6.4.1（样品容器外部 7 项）、6.3.2（开箱容器 4 项）复现，说明这是一条贯穿证据链的通用原则而非照片专用。
- **跨章节重复证据（供 V1 验证）**：6.1.8 给出 5 要素+示例+例外；**6.4.1** 把同一"外部标识"逻辑用于样品容器（sample number / entry-line / PAC-PAF / 采集日 / 储存条件 / Lead CSO 缩写 / 箱数与 sub 编号）；**6.3.2** 用于现场开箱容器（FDA、division 缩写、查验日、主导调查员缩写）；**6.4.6.7** 的 Hand Ship 示例仍带 `123-1234567-1,JD, 1/1/2024` 式标识。跨 6.1 / 6.3 / 6.4。
- **tags**: [checklist, photo-identification, 5-elements, hard, cross-chapter-6.1/6.3/6.4]

---

### p06 · [清单] SCR 九字段 + 每份样品必须有采集报告

- **id**: p06
- **type**: checklist（成体系清单）+ principle（记录义务）
- **force**: **硬性 hard**（`must be completed` / `For every sample collected` / 各字段 `Enter…` 祈使 / `must be generated`）
- **source**: IOM 6.4.6 [p.35–38]（主，6.4.6.1–6.4.6.9 逐字段）；复现于 6.4.1 [p.33]、6.4.7 [p.38]、6.4.9 [p.38–39]、6.3.10 [p.30–32]（平行字段规范）、6.8.3.1.1 [p.50]（记录充分性）
- **source_quote**:
  > "For every sample collected, a corresponding electronic collection report must be completed in FDA Import Systems … You are responsible for making sure all fields in the Line Details screen are complete and correct." (6.4.6 [p.35])
  > "6.4.6.1 Date Collected / 6.4.6.2 Episode / 6.4.6.3 Submitted To / 6.4.6.4 Quantity Collected / 6.4.6.5 Units / 6.4.6.6 DescText / 6.4.6.7 Hand Ship / 6.4.6.8 Remarks / 6.4.6.9 Record Time Screen." (6.4.6 [p.36–38]，节录小节标题)
  > "Note that a collection report may only be corrected once … If a change was made to the Quantity Collected, Units, or Desc Text, a new Notice of FDA Action must be generated." (6.4.7 [p.38])
  > "Note that any text you enter in this field will be printed on the 'Notice of FDA Action.'" (6.4.6.6 [p.37])
- **中文自译**：每采集一份样品都须在系统完成一份电子采集报告（SCR），且须先复核 Line Details 全部字段。九字段逐一有规范：Date Collected（实际采集日，非录入日）、Episode（同一违规发现及其后续样品归为同一 episode）、Submitted To（按 LST 选有产能的实验室）、Quantity Collected、Units、DescText（subs 数/单重/品名/容器/批号/取样方式）、Hand Ship（保存→制备→运输→sub 标识与完整 chain of custody）、Remarks（特殊处理、依据文件、分析指令、controls/photos）、Record Time。报告**只能更正一次**；若改动 Quantity/Units/DescText 必须重发 Notice of FDA Action；仅改 Hand Ship 或 Remarks 则不必。
- **清单（SCR 九字段）**：`Date Collected` | `Episode` | `Submitted To` | `Quantity Collected` | `Units` | `DescText` | `Hand Ship` | `Remarks` | `Record Time Screen`。
- **反直觉 / 易错**：① "Date Collected ≠ 录入日"是硬约束（跨多日取最后一日），记录时间与实际时间被明确分离；② DescText 与 Remarks 的**对外可见性不同**——DescText 会印在公开 Notice 上，Hand Ship 仅进入 FACTS 的实验室内屏、实验室人员不易看到，故特殊处理指令必须写进 Remarks（手册明说）；③ "只能更正一次"极易漏；④ 改哪几个字段会触发重发通知是分级的；⑤ SDI 样品在九字段之外还须加标签描述、FDA 415a 官方封条、采集人 ID，理由是"检出违规时 FDA 才能启用国内管辖权"。
- **跨章节重复证据（供 V1 验证）**：**6.4** 内部 ≥4 处（6.4.1 "as soon as possible"、6.4.6 主规范、6.4.7 更正、6.4.9 SDI 附加）；**6.3.10** 给出结构平行的"查验结果七字段"（Date Completed / Location / Remarks / Summary / Exam Class / Record Time / Next Steps），并重复"数据改动→备注→指派责任→rescreen"（见 p01）；**6.8.3.1.1** 用 `must be documented with sufficient detail` 表达同一"记录充分性"要求。跨 6.3 / 6.4 / 6.8。
- **tags**: [checklist, SCR, nine-fields, chain-of-custody, hard, cross-chapter-6.3/6.4/6.8]

---

### p07 · [清单] 初审排序规则（优先级阶梯）

- **id**: p07
- **type**: checklist（成体系清单 / 判定规则）
- **force**: **硬性 hard 为主**（`have priority over` / `take priority over` / `take precedence over all others` / `apply the same decision-making criteria` / `only if`）；其中 `In general` / `typically` 为软化措辞，须在 Boundary 标注
- **source**: IOM 6.2.2 [p.15–16]、6.2.2.1 [p.16]（主）；复现于 6.1.4.5 [p.8]、6.2.3.2 [p.19]、6.1.6 [p.12]、6.4.2.1 [p.34]
- **source_quote**:
  > "In general, prioritize lines as follows: 1. Lines with a QAV work type have priority over those with an NQV work type. 2. Lines with documents submitted through the Import Trade Auxiliary Communications System (ITACS) take priority over lines with documents sent by other methods." (6.2.2 [p.15–16])
  > "Trucks: Actual arrival date and time. • Air, Rail, and Sea: Submission date and time." (6.2.2 [p.15])
  > "Emergency and perishable products are time sensitive and take precedence over all others." / "Release device shipments only if the entry documents show CDRH approval." (6.2.2.1 [p.16])
  > "… though the FDA accepts entry data submitted via non-ABI (paper/manual) means, electronically filed entries do take priority." (6.1.4.5 [p.8])
  > "Documents sent through ITACS receive priority over those sent by other methods." (6.2.3.2 [p.19])
- **中文自译**：初审优先级阶梯（自高到低）：① 紧急/易腐货物压倒一切；② QAV（有数量与价值）> NQV；③ 经 ITACS 提交单据 > 其他方式；④ 电子申报 > 纸质/manual。排序所用时间戳按运输方式区分：卡车用**实际到港时间**，空/铁/海运用**申报提交时间**。纸质（non-ABI）entry 与电子 entry 适用**同一套判定标准**。器械 shipment 仅在单据能显示 CDRH 批准时才可放行，无法核实时须联系 CDRH。
- **清单（排序阶梯）**：`紧急/易腐 > 全部` → `QAV > NQV` → `ITACS 单据 > 其他单据` → `电子 > 纸质`；计时口径 `卡车=实际到港 / 空铁海=提交时间`；硬闸门 `器械须见 CDRH 批准文件`。
- **反直觉 / 易错**：① "紧急/易腐优先"由各 division 自行界定以防滥用，是裁量嵌入硬性阶梯的典型；② 计时口径随运输方式切换（卡车看到港、其余看提交），误用会直接排错序；③ "纸质与电子适用同一判定标准"与"电子优先"并存——优先是**排队顺序**，不是判定标准差异；④ `In general` 表明阶梯是默认而非绝对，这是 Boundary 必须保留的软化标记。
- **跨章节重复证据（供 V1 验证）**：**6.2.2** 给出完整阶梯；**6.2.3.2** 单独重复"ITACS 单据优先"；**6.1.4.5** 重复"电子申报优先"；**6.1.6 / 6.4.2.1** 补充远程审查与口岸管辖的排队前提。跨 6.1 / 6.2 / 6.4。
- **tags**: [checklist, prioritization, QAV-NQV, ITACS, hard-with-in-general, cross-chapter-6.1/6.2/6.4]

---

### p08 · [清单] Prior Notice 时限框架与豁免清单

- **id**: p08
- **type**: checklist（成体系清单 / 硬时限 + 豁免判定）
- **force**: **硬性 hard**（`must be received and confirmed electronically` / `no fewer than` / `must be submitted electronically` / `is subject to refusal and holding`）；豁免清单为 `定义型 definitional`
- **source**: IOM 6.1.5.1 [p.9]、6.1.5.3 [p.10]（主）；复现于 6.1.5.2 [p.9–10]、6.1.5.4 [p.10–11]、6.1.5.5 [p.11]、6.1.4.5 [p.8]、6.1.6.1 [p.12]、6.9.62 [p.57]、6.9.13/6.9.41 [p.51/55]
- **source_quote**:
  > "Prior notice … must be received and confirmed electronically by the FDA no more than 15 calendar days before the anticipated date of arrival for submission made through the PNSI, and no more than 30 calendar days before … ABI/ACE, and … no fewer than: Two hours before arrival by land by road; Four hours before arrival by air or by land by rail; Eight hours before arrival by water." (6.1.5.1 [p.9])
  > "In addition, prior notice must be received and confirmed electronically by FDA before food is mailed by international mail." (6.1.5.1 [p.9])
  > "Foods that are excluded from the prior notice requirement include: Food carried by … an individual … for that individual's personal use; Food that is exported without leaving the port of arrival until export; Meat products, poultry products, and egg products … under the exclusive jurisdiction of … USDA; Food made by an individual in their personal residence and sent … as a personal gift; Articles of food subject to Article 27.3 of the Vienna Convention on Diplomatic Relations (1961)." (6.1.5.3 [p.10]，节录)
  > "Food that is imported or offered for import with inadequate prior notice is subject to refusal and holding at the port or in a secure storage facility." (6.1.5.5 [p.11])
- **中文自译**：事先通知须经 FDA **电子接收并确认**（不只是提交）：上限 PNSI 15 个日历日 / ABI-ACE 30 个日历日；下限按运输方式 2 小时（公路）/ 4 小时（空运、铁路）/ 8 小时（水运）；国际邮寄须在寄出前确认，且包裹须随附确认回执。豁免 5 类（见清单）。通知不充分 → 拒绝并在口岸或安全库扣留，且不限制 FDA 依 FD&C Act 采取其他行动、也不限制 CBP 处罚。
- **清单（豁免 5 类）**：`个人抵达随身携带、供本人/家人/朋友食用且非销售` | `未离开抵达口岸即原状出口的食品` | `USDA 专属管辖的肉/禽/蛋制品` | `个人在住所自制、作为非商业个人礼物寄送` | `《维也纳外交关系公约》第 27.3 条外交邮袋物品`。提交信息另有 15 项（6.1.5.4 [p.10–11]）。
- **反直觉 / 易错**：① 关键是"**接收并确认**（received and confirmed）"而非"已提交"，缺确认回执即属 inadequate；② 上限/下限是双向窗口，早于 15/30 天提交同样不合规；③ Prior Notice **独立于报关方式**——6.1.4.5 明说 manual/paper entry 的人用或动物用食品仍须提前通报（可走 PNSI），这是最易被忽略的交叉点；④ 15 天数字的另义：6.9.13/6.9.41 的 "Entry/Immediate Delivery must be filed within 15 calendar days of arrival" 是 CBP 报关义务，与 PN 的 15 天上限不是同一件事，术语表同页易混；⑤ 豁免是"不适用 PN 要求"，不等于免除 FDA 依 §801(a) 的可采性审查。
- **跨章节重复证据（供 V1 验证）**：**6.1.5.1/5.3/5.5** 三处构成"时限—豁免—后果"闭环；**6.1.4.5** [p.8] 把 PN 义务跨接到 manual entry；**6.1.6.1** [p.12] 用 FD3/FD4 flag 与 PND A of C 代码落实"是否需 PN"的申报判定；**6.9.62** [p.57] 术语表重复"must be submitted electronically"；**6.9.13/6.9.41** 重复条件放行/15 天口径。跨 6.1 / 6.9。
- **tags**: [checklist, prior-notice, time-window, exemptions, hard, cross-chapter-6.1/6.9]

---

### p09 · [清单] Failure to Hold 8 步调查 + 健康危害 / DWPE 加重步骤

- **id**: p09
- **type**: checklist（成体系清单）
- **force**: **裁量措辞、准硬性适用** — 原文用 `The following steps should be taken on all Failure to Hold cases` / `should be regarded as a concern of the highest priority` / `the following additional step should be taken`；但 "**on all … cases**" 与 "in addition to the eight common steps" 使其在实务上覆盖全部个案。这是 `should` 与 `all` 并存的张力点，须在 Boundary 显式标注（见 p12）
- **source**: IOM 6.6.4.1 [p.43]（主）；6.6.4.2 [p.43–44]、6.6.4.3 [p.44]（加重）；复现于 6.6.4 [p.43]、6.6.4.4 [p.44]、6.6.4.6.1 [p.45]、6.6.3 [p.43]、6.9.30 [p.53]、6.5.2.11 [p.42]、6.3.11 [p.33]
- **source_quote**:
  > "The following steps should be taken on all Failure to Hold cases: 1. Collect entry documentation (CBP form 3461 or 7501, invoice, packing list, bill of lading). 2. Determine distribution, by collecting and analyzing pertinent distribution records. 3. Determine who authorized the distribution. 4. Determine if the importer was aware of the health hazard associated with the product. 5. Obtain the authorizing person's explanation … (Items (1), (2), (3), (4), and (5) should be covered in one or more affidavits.)" (6.6.4.1 [p.43]，节录)
  > "6. Perform a data search via ORADSS … 7. Coordinate with CBP the issuance of a Demand for Redelivery (form 4647) … the deadline for redelivery is 30 days, instead of the 90 days post-refusal. 8. Determine the importer's bond type and amount." (6.6.4.1 [p.43]，节录，步骤标题保留原序)
  > "Distribution of goods where there is direct evidence of a significant health hazard … should be regarded as a concern of the highest priority. In addition to the eight common steps listed above, the following additional step should be taken: Consult with supervisory staff, compliance staff, and the division's Recall and Emergency Coordinator … to address retrieval from and/or notification to the consignees, as well as consideration for any public warning." (6.6.4.2 [p.43–44]，节录)
- **中文自译**：所有 Failure to Hold 个案须走 8 步：① 收集报关单据（3461/7501、发票、装箱单、提单）；② 用分销记录确定分销事实；③ 确定谁授权分销（可能不止一个责任方）；④ 判断进口商是否知悉产品健康危害；⑤ 取得授权人书面说明（①–⑤ 须落入一份或多份 affidavit）；⑥ 用 ORADSS 等检索进口商历史并与主管/合规讨论；⑦ 协调 CBP 签发 4647 redelivery 要求——此情形下期限为 **30 天**而非拒绝后的 90 天，且 4647 可为查验/取样而发、不必先有拒绝；⑧ 核定进口商 bond 类型与金额。存在直接重大健康危害证据时在 8 步外追加召回/收货人通知/公共警告协调；仅达到"外观违规"标准（如 DWPE 历史）时追加是否取样分析及同样的召回协调。
- **清单（8 步 + 2 组加重）**：`单据` → `分销记录` → `授权人` → `健康危害知悉` → `授权人说明+affidavit` → `历史检索` → `CBP 4647（30 天）` → `bond 核定`；加重 A（直接健康危害）：`召回/通知/公共警告`；加重 B（DWPE 外观违规）：`是否取样` + `召回/通知/公共警告`。
- **反直觉 / 易错**：① 第 ⑦ 步的 **30 天 vs 90 天**最易错：因查验/取样发出的 4647 是 30 天，拒绝入境后的出口/销毁才是 90 天（6.9.44 [p.55]）；② "Form 4647 可仅为查验/取样而签发，不必先有 FDA 拒绝"与直觉相反；③ ⑤ 要求把前 5 项固化成 affidavit（宣誓书），不是普通访谈记录；④ ③ 明说"可能不止一个责任方"；⑤ 6.6.4.4 规定替换案在查明前一律按"无放行而分销"处理，直接回指本 8 步；⑥ 全清单用 `should` 却写 "on **all** … cases"，正是 p12 元规则的典型样本。
- **跨章节重复证据（供 V1 验证）**：**6.6.4.1/4.2/4.3** 三层（8 步 + 健康危害 + DWPE）共享同一 "eight common steps" 基座；**6.6.4** 列出四类违规模式并声明"任一情形可能重叠多个模式、清单非穷尽"；**6.6.4.4**（替换）、**6.6.4.6.1**（反复 filer 误报）复用同一"单据→标签/照片→affidavit→历史"取证骨架；**6.6.3** 给 10+5 个工作日的 memo 时限；**6.5.2.11 / 6.9.30 / 6.3.11** 重复 bond 与 30 天 redelivery。跨 6.3 / 6.5 / 6.6 / 6.9。
- **tags**: [checklist, failure-to-hold, 8-steps, affidavit, 30-day-vs-90-day, should-on-all-cases, cross-chapter-6.3/6.5/6.6/6.9]

---

### p10 · Failure to Hold 定义为"无放行而分销"，而非"移出港区"

- **id**: p10
- **type**: principle（口径定义 / 判定规则）
- **force**: **定义型 definitional，构成硬性判定基准**（`means that…` / `*Please note that this is defined as … not merely …`）
- **source**: IOM 6.6.4.1 [p.43]（主）；6.9.30 [p.53]（术语表复述）；复现于 6.9.13 [p.51]、6.5.2.11 [p.42]、6.6.4.4 [p.44]、6.9.73 [p.58]
- **source_quote**:
  > "Failure to hold means that the goods have been distributed by the importer/consignee without an FDA release from import status. *Please note that this is defined as distribution without a release, not merely moving the goods outside of the port area." (6.6.4.1 [p.43])
  > "Failure to hold means that the goods have been distributed by the importer/consignee without an FDA release from import status. Such goods are usually subject to CBP's redelivery provisions." (6.9.30 [p.53])
  > "The goods may be moved but CBP can request redelivery within 30 days." (6.9.13 [p.51])
  > "Bond actions are taken when an entry is distributed prior to FDA release and cannot be redelivered." (6.5.2.11 [p.42])
- **中文自译**：Failure to Hold 指进口商/收货人在**未获 FDA 放行**的情况下已把货物**分销**出去。手册特意加注：定义是"无放行而分销"，**不是**"把货物移出港区"。条件放行期内货物**可以被移动**，只是 CBP 可在 30 天内要求 redelivery；只有"放行前已分销且无法追回"才触发 bond action。
- **反直觉 / 易错**：① 这是全章最典型的反直觉定义——直觉按"位置/位移"判断违规，手册按"是否有放行 + 是否分销"判断；货物搬出港区本身**不构成**该违规（6.9.13 明说 "may be moved"）；② 与"Conditional Release"（货物已交进口商控制但仍处 FDA 管辖、须保持可召回）强绑定，位置变化与法律状态变化被刻意解耦；③ 术语表 6.9.30 与正文 6.6.4.1 两次重复定义，且正文用 `*Please note` 显式纠偏，说明作者预期读者会弄错；④ 与 DWPE 同类术语误读相反（DWPE 是"不检查就扣住"而非"不检查就放过"），二者共同构成"看字面会反"的一组。
- **跨章节重复证据（供 V1 验证）**：正文 **6.6.4.1** 与术语表 **6.9.30** 逐字重复定义；**6.9.13 / 6.9.41** 从正面确认"可移动 + 30 天 redelivery"；**6.5.2.11** 用 "distributed prior to FDA release" 复述触发条件；**6.6.4.4 / 6.9.73**（Substitution）把"隐藏无放行分销"列为替换动机，回指本定义。跨 6.5 / 6.6 / 6.9，≥6 处。
- **tags**: [principle, definition, failure-to-hold, distribution-not-movement, counter-intuitive, definitional, cross-chapter-6.5/6.6/6.9]

---

### p11 · 记录须在监测 / 观察当时形成（当时记录）

- **id**: p11
- **type**: principle（记录时点规则）
- **force**: **混合 mixed，核心为硬性** — `Record … at the time of the field exam` / `Include the date, contact person …` / `Document all your actions` 为祈使（硬性）；6.4.6.1 用 `should reflect the date the sample was collected, not the date the sample was recorded`（裁量措辞但语义为硬约束）；6.5.2.10 / 6.8 的 `should investigate` / `as warranted` 为裁量
- **source**: IOM 6.3.1 [p.24]（主）；复现于 6.1.8 [p.14]、6.4.6.1 [p.36]、6.2.3.3 [p.20]、6.2.2.2.2 [p.18]、6.3.11 [p.33]、6.6.3 [p.43]、6.8.1.4.1 [p.48]、6.8.3.1.1 [p.50]
- **source_quote**:
  > "Record your observations in your regulatory notebook at the time of the field exam, including such information as: Date, Entry number, Name and address of the location where the exam is taking place, Name and title of the persons providing information, Information from the product labeling, Number of units examined, Documentation of any photos or labels collected, Any abnormalities or discrepancies observed … A record of the quantity of any product that was destroyed in the field." (6.3.1 [p.24]，节录)
  > "The Date Collected should reflect the date the sample was collected, not the date the sample was recorded. Only one date can be entered. If the sample collection was accomplished over several days, use the last date of collection." (6.4.6.1 [p.36])
  > "Document all your actions and communications in the FDA's Import system to maintain a clear record." (6.2.2.2.2 [p.18]，撤消第 7 步)
  > "Log all direct communications in the 'Remarks' field … Include the date, contact person, information requested, and your initials." (6.2.3.3 [p.20])
- **中文自译**：现场观察必须在**查验当时**记入 regulatory notebook，且须含日期、entry 号、查验地点名称地址、提供信息者的姓名与职务、标签信息（品名、批号/代码）、查验件数、所拍照片/所取标签的记录、任何异常或不符、以及现场销毁数量。采集日期须记**实际采集日**而非录入日（跨多日取最后一日）。所有直接沟通（电话/邮件）须当次登记日期、联系人、所索信息、本人缩写；撤消放行全过程须记入系统以维持清晰记录。
- **反直觉 / 易错**：① "记录时间 ≠ 事件时间"被明确分离，补记/事后汇总不符合规范；② regulatory notes（private，IOM 2.1）与系统 Remarks（internal FDA use only，6.2.1 [p.14]）、Narrative（**会出现在公开 Notice 上**，6.2.3.3 [p.20]）三种记录载体可见性不同，误填会泄露或留痕失效；③ 6.4.6.6 的 DescText 印在公开 Notice、Hand Ship 仅进 FACTS 内屏（见 p06），同属"记录分层"；④ 裁量词 `should` 在此承载的是硬要求，是 p12 元规则的又一佐证。
- **跨章节重复证据（供 V1 验证）**：**6.3.1**（现场当时记录清单）、**6.4.6.1**（采集日≠录入日）、**6.2.3.3**（沟通当次登记、单据按到达顺序审）、**6.2.2.2.2**（撤消全过程记录）、**6.3.11**（撤消 IB Release 记录）、**6.1.8**（拍照须在 regulatory notes 中留痕）、**6.8.1.4.1 / 6.8.3.1.1**（所有讨论与纠正动作记入 T-EIR，且 `must be documented with sufficient detail`）、**6.6.3**（末次调查活动后 10 工作日出 memo、5 工作日背书）——跨 6.1 / 6.2 / 6.3 / 6.4 / 6.6 / 6.8，是全章分布最广的记录原则。
- **tags**: [principle, contemporaneous-record, at-the-time, date-collected-vs-recorded, mixed, cross-chapter-6.1/6.2/6.3/6.4/6.6/6.8]

---

### p12 · 元规则：must / shall = 硬性动作，should / as warranted / where appropriate = 机构裁量

- **id**: p12
- **type**: principle（元规则 / 语用判读规则）—— **下游 Boundary 的直接来源**
- **force**: **meta**（本身不是操作动作，而是判读全篇 force 的规则）
- **source**: 全篇分布；取样点 6.2.2.2 [p.16]、6.2.4 [p.20]、6.5.2.9 [p.41]、6.4.6 [p.35]、6.1.8 [p.14]、6.3.1 [p.24]、6.5.2.4 [p.40]、6.5.2.10 [p.41]、6.5.2.11 [p.42]、6.6.4.1 [p.43]、6.8.2.1 [p.48]、6.5.2.6 [p.40]；BOOK_OVERVIEW §3「未被证明的假设」已标注同一现象
- **source_quote**:
  > "Before you take any action, you must review and consider the recommendations from the FDA Import System, including the PREDICT risk score and any rule flags." (6.2.2.2 [p.16]) / "You must make this decision before the conditional release period ends." (6.2.4 [p.20]) / "The expenses shall be computed based upon the following" (6.5.2.9 [p.41]) / "a corresponding electronic collection report must be completed" (6.4.6 [p.35])
  > "… detention requests (when warranted), destructions, reconditioning … and other situations as warranted." (6.1.8 [p.14]) / "A decision to collect samples should be made … but is ultimately your discretion" (6.3.1 [p.24]) / "Photographs should also be taken as warranted" (6.5.2.4 [p.40]) / "as warranted" (6.5.2.10 [p.41]) / "If the facts warrant" (6.5.2.11 [p.42]) / "The following steps should be taken on all Failure to Hold cases" (6.6.4.1 [p.43])
  > "The FDA 483a should only be issued at the conclusion of the inspection." (6.8.2.1 [p.48]) / "a second attempt should not be considered unless" (6.5.2.6 [p.40]) / "Payment of supervisory charges should not be accepted by any FDA division offices." (6.5.2.9 [p.41])
- **中文自译**：本手册用情态动词严格分层：`must` / `shall` / 祈使句 / `Do not` 是**不可省略的硬性动作**；`should` / `as warranted` / `where appropriate` / `if the facts warrant` / `may` / `can` / `ultimately your discretion` / `in general` 是**机构裁量空间**，且章内几乎不给出裁量判据（留给分部惯例）。因此 IOM 属内部操作指导而非可对外主张的法定义务，蒸馏成"合规规则引擎"会系统性高估其法律位阶。
- **反直觉 / 易错**：① **映射不是纯机械的**——`should only` / `should not` / `should only be issued at the conclusion` 形式上是 `should`，语义却是**禁止/唯一时点**（483a 只能在检查结束签发、第二次重整原则上不考虑、监管费不得由 FDA 分部收取）；② 反向也有：`should be taken on **all** … cases`（p09）用裁量词覆盖全部个案；③ 同一句内可硬软并存（p03 "should only rescind … You **must** act immediately"、p04 "must be uploaded … (when warranted)"）；④ 判据缺失本身是作者假设（BOOK_OVERVIEW §3："请求扣留 vs 请求现场工作"的选择标准、"adverse conditions" 阈值、照片 "warranted" 情形都留给分部惯例），应作为 Boundary 的复核锚点，而非补写成规则。
- **跨章节重复证据（供 V1 验证）**：硬性样本散布 6.1.8 / 6.2.2.2 / 6.2.4 / 6.4.6 / 6.5.2.9；裁量样本散布 6.1.8 / 6.1.4.4 / 6.2.2.2.1 / 6.2.5.4 / 6.3.1 / 6.5.2.4 / 6.5.2.10 / 6.5.2.11 / 6.6.4.1 / 6.6.4.5 / 6.8.2.1——几乎每节都有，属"全篇级"重复；阶段 0 `BOOK_OVERVIEW.md` §3 与 §4「不适合 skill 化的内容」已独立确认为边界来源。跨 6.1 / 6.2 / 6.3 / 6.4 / 6.5 / 6.6 / 6.8。
- **tags**: [meta, modality, must-vs-should, discretion, boundary-source, whole-book]

---

### p13 · 扣留建议判定规则：须先合理核实，不得仅凭查询失败 / A of C 缺失即建议扣留；DER 与 DTR 按触发依据分流

- **id**: p13
- **type**: principle（判断规则 / 禁止性规则）
- **force**: **硬性 hard 为主**（`must make a reasonable effort` / `Do not recommend detention based solely on…` / `Use DER when… Use DTR for…` / `must include all applicable alerts and PAFs` / `must request and review documents before submitting a DER if…`）；`You can submit a DER … if all the following are true` 与 `you may recommend detention` 为 `裁量 discretionary`
- **source**: IOM 6.2.5.5 [p.23]、6.2.5.1 [p.21]（主）；复现于 6.2.5.2 [p.21]、6.2.5.3 [p.21–22]、6.2.5.4 [p.22]、6.2.5.4.1 [p.22]、6.2.3.3 [p.20]、6.3.10.5 [p.31]、6.9.20 [p.52]、6.9.22 [p.52]
- **source_quote**:
  > "You must make a reasonable effort to verify compliance using the information provided. Do not recommend detention based solely on a failed data lookup or missing Affirmation of Compliance data." (6.2.5.5 [p.23])
  > "DER (Detention without Physical Examination): Use DER when a product is subject to Detention without Physical Examination (DWPE). DTR (All Other Detentions): Use DTR for all other situations where a product appears to be violative." (6.2.5.1 [p.21])
  > "If a product has multiple violations (for example, it is subject to more than one Import Alert), you must include all applicable alerts and problem area flags (PAFs) in your detention recommendation." (6.2.5.2 [p.21])
  > "You must request and review documents before submitting a DER if the Import Alert requires specific paperwork for a product to be released." (6.2.5.3 [p.22])
- **中文自译**：不得仅因数据库查询失败或 A of C 数据缺失就建议扣留——须先用手上信息作"合理努力"核实（查电子数据 + 内部数据库 + 单据，必要时请求单据/现场/取样）。扣留建议按**触发依据**分流：受 DWPE（Import Alert）约束用 DER，其余"无法确认符合可采性要求"用 DTR；二者不是严重度分级。多重违规须把全部 IA 与 PAF 一并列入；IA 要求特定证书（如 IA 28-02 黑胡椒证书）时，缺证书须先索取再建议扣留。
- **反直觉 / 易错**：① **"查不到 ≠ 违规"**——数据库无记录、A of C 缺失都只是核实起点，直接建议扣留是被明文禁止的；② DER/DTR 是"触发依据"分流而非"严重程度"分级，直觉上易当成轻重档；③ 即使"不匹配 Import Alert"也须用 feedback 功能写明为何不适用（6.2.5.4.1），与 p02 同源；④ DER 可在电子数据完全匹配 IA 且 IA 不要求单据、无需额外信息时**免索单据**提交，但一旦 IA 要求单据则必须先索——条件式例外；⑤ "提交 Compliance Branch"是组织分工，已按排除声明从原则中剥离，原则落点是"核不核实、按什么分流"。
- **跨章节重复证据（供 V1 验证）**：**6.2.5** 全节（5.1/5.2/5.3/5.4/5.4.1/5.5）反复书写分流与"须先核实/须写理由"；**6.2.3.3** [p.20] 把 "cannot confirm compliance → DTR" 前置到单据审查环节；**6.3.10.5** [p.31] 把 Class 3 FEX/LEX 发现违规接到 "submit to compliance as a DTR with the appropriate PAF"；**6.9.20 / 6.9.22** 术语表复述 DTR / DWPE 口径。跨 6.2 / 6.3 / 6.9。
- **tags**: [principle, detention-recommendation, DER-vs-DTR, reasonable-effort, no-detention-on-lookup-failure, hard, cross-chapter-6.2/6.3/6.9]

---

### p14 · 重整失败原则上不给第二次机会，除非修订后的方法能合理保证成功

- **id**: p14
- **type**: principle（判断规则）
- **force**: **裁量 discretionary**（`should not be considered unless … shows a reasonable assurance of success`）；相邻条款含 `硬性`（rejects `must be destroyed or re-exported`）
- **source**: IOM 6.5.2.6 [p.40]（主）；复现于 6.5.2.5 [p.40]、6.5.2.3 [p.40]、6.5.2.4 [p.40]、6.1.3 [p.6]、6.9.65 [p.57]
- **source_quote**:
  > "If the initial attempt at reconditioning is unsuccessful, a second attempt should not be considered unless a revised method of reconditioning shows a reasonable assurance of success." (6.5.2.6 [p.40])
  > "Where there is a non-admissible portion (or rejects), they must be destroyed or re-exported under FDA or CBP supervision. A Notice of Refusal of Admission should also be issued for the rejected portion." (6.5.2.5 [p.40])
  > "The FDA determines if an article complies with the Acts it enforces. It also determines whether the article can be brought into compliance with the appropriate statute and authorizes reconditioning for that purpose." (6.1.3 [p.6])
- **中文自译**：首次改标/重整失败后，原则上不考虑第二次，除非**修订后的方法本身**能合理保证成功。条件满足而放行时，不合格部分（rejects）仍须在 FDA/CBP 监督下销毁或再出口，并**单独**就该部分出具拒绝入境通知；FDA 还可在批准时规定 rejects 只销毁、不得出口。重整须经 FDA 批准并监督（Form FDA 766 + bond），企业自行返工不产生放行效力。
- **反直觉 / 易错**：① 门槛落在"**修订后的方法**能否合理保证成功"，不是"企业愿不愿意再试一次"——举证对象是方法而非态度；② 合格部分放行 ≠ 整批结案，不合格部分仍走独立拒绝/销毁链，并单独发通知（易漏）；③ 与 6.5.2.8 的"90 天出口/销毁"衔接；④ 这是全书 `should not … unless` 型"裁量式禁止"的样本，须按 p12 判读，不宜写成绝对"永不给第二次"。
- **跨章节重复证据（供 V1 验证）**：**6.5.2.3**（766 授权与 bond）、**6.5.2.4**（完成后复核，`may … or it may accept the statement` 为裁量）、**6.5.2.5**（条件满足，rejects 单独处理）、**6.5.2.6**（条件不满足，本条）、**6.5.2.7/5.2.8**（放行/拒绝）构成闭环；**6.1.3** [p.6] 从授权层规定"FDA 才有权判定能否被带入合规并批准重整"；**6.9.65** 术语表复述"须申请并经许可"。跨 6.1 / 6.5 / 6.9。
- **tags**: [principle, reconditioning, no-second-attempt, revised-method, rejects-separate-refusal, discretionary, cross-chapter-6.1/6.5/6.9]

---

### p15 · 发出拒绝通知不是终点：档案须保持开放直到收到销毁 / 出口证明

- **id**: p15
- **type**: principle（流程终局规则 / 记录义务）
- **force**: **混合 mixed，核心为硬性** — `The FDA file remains open until…` / `is responsible … until the violative article is either destroyed or exported` / `must either be destroyed or exported … within 90 days` 为硬性；`should investigate` / `should also consider … verifying` / `as warranted` 为裁量
- **source**: IOM 6.5.2.8 [p.41]（主）；复现于 6.5.2.10 [p.41–42]、6.5.2.11 [p.42]、6.9.44 [p.55]、6.6.2 [p.42–43]、6.9.30 [p.53]、6.9.11 [p.51]
- **source_quote**:
  > "The FDA file remains open until the division receives notification indicating that the goods were either destroyed or exported." / "Keep in mind that, throughout this process, the FDA is responsible for the protection of the U.S. public regarding foods, drugs, cosmetics, tobacco products, etc., until the violative article is either destroyed or exported." (6.5.2.8 [p.41])
  > "… if after a reasonable time, the FDA has not received notification of exportation or destruction, the Division should investigate the status of disposition. Divisions should also consider … verifying that the refused goods have, in fact, been held intact pending exportation or destruction, or that a re-export actually occurred." (6.5.2.10 [p.41])
  > "A refused shipment must either be destroyed or exported under the supervision of CBP and the FDA within 90 days of the date of the Notice of FDA Action (Refusal Notice)." (6.9.44 [p.55])
- **中文自译**：拒绝入境通知发出后，FDA 档案**不关闭**，须一直保持开放直到分部收到货物已被销毁或出口的证明；FDA 对公众的保护责任延续到该违规品被销毁或出口为止。若合理期限内未收到处置通知，须调查处置状态，并（按条件）核实货物确被完整留存待出口/销毁、或再出口确已发生；销毁见证与差异应"as warranted"拍照（见 p04）。被拒货物须在通知日起 90 天内于 CBP 与 FDA 监督下出口或销毁。
- **反直觉 / 易错**：① 直觉把 "Refusal of Admission" 当流程终点，手册明确说之后还有 4647 redelivery、出口/销毁核验、bond action，档案才关闭；② "发出通知"与"责任解除"被解耦，与 p10 "位置变化 ≠ 法律状态变化"、p03 "放行 ≠ 合规判定"同构；③ 6.6.2 规定刑事证据的取得**不得改变**监管处置顺序——产品须先走完 FDA 拒绝/销毁或 CBP 扣押没收程序，OCI 才能为取证接管，避免"因可能成为证据就另走一套标准"；④ 90 天（拒绝后）与 30 天（放行/条件放行期结束后的 redelivery，p03/p09）是两套窗口，勿混。
- **跨章节重复证据（供 V1 验证）**：**6.5.2.8**（档案开放 + 责任延续）、**6.5.2.10**（未获通知须调查、核实 intact / re-export）、**6.5.2.11**（bond action，"not destroyed or exported" 触发立即调查）、**6.9.44**（90 天硬时限）、**6.6.2**（刑事取证顺序不改变）、**6.9.30 / 6.9.11**（术语层复述）。跨 6.5 / 6.6 / 6.9。
- **tags**: [principle, refusal-not-final, file-remains-open, until-destroyed-or-exported, 90-day, mixed, cross-chapter-6.5/6.6/6.9]

---

### 汇总表（供阶段 1.5 三重验证 / 1.6 晋级门快速索引）

| id | 标题（简） | type | force | 主出处 | 跨章复现 |
|---|---|---|---|---|---|
| p01 | 数据更正→指派责任→保存→rescreen | principle | 硬性 | 6.2.1 [p.14] | 6.1/6.2/6.3/6.4/6.7 |
| p02 | 相悖判定须具体理由、禁空泛备注 | principle | 硬性 | 6.2.2.2 [p.16] | 6.2/6.3/6.5 |
| p03 | 放行可撤消、条件放行期不重开 | principle | 混合 | 6.2.2.2.2 [p.17] | 6.2/6.3/6.4/6.5/6.9 |
| p04 | 照片证据设备/上传/打印标识位置 | principle | 混合（硬性核心） | 6.1.8 [p.14] | 6.1/6.3/6.4/6.5/6.6 |
| p05 | 照片标识 5 要素 | checklist | 硬性 | 6.1.8 [p.14] | 6.1/6.3/6.4 |
| p06 | SCR 九字段 + 每样必有报告 | checklist | 硬性 | 6.4.6 [p.35] | 6.3/6.4/6.8 |
| p07 | 初审排序阶梯 | checklist | 硬性（含 `in general`） | 6.2.2 [p.15] | 6.1/6.2/6.4 |
| p08 | Prior Notice 时限 + 豁免清单 | checklist | 硬性 | 6.1.5.1/5.3 [p.9/10] | 6.1/6.9 |
| p09 | Failure to Hold 8 步 + 加重 | checklist | 裁量措辞·准硬性 | 6.6.4.1 [p.43] | 6.3/6.5/6.6/6.9 |
| p10 | FTH＝无放行而分销 ≠ 移出港区 | principle | 定义型 | 6.6.4.1 [p.43] | 6.5/6.6/6.9 |
| p11 | 记录须在观察当时形成 | principle | 混合（硬性核心） | 6.3.1 [p.24] | 6.1/6.2/6.3/6.4/6.6/6.8 |
| p12 | must/shall vs should/as warranted 元规则 | principle | meta | 全篇 | 6.1–6.8 全篇 |
| p13 | 扣留建议：先合理核实 + DER/DTR 分流 | principle | 硬性 | 6.2.5.5 [p.23] | 6.2/6.3/6.9 |
| p14 | 重整失败不给第二次机会 | principle | 裁量 | 6.5.2.6 [p.40] | 6.1/6.5/6.9 |
| p15 | 拒绝后档案开放至销毁/出口证明 | principle | 混合（硬性核心） | 6.5.2.8 [p.41] | 6.5/6.6/6.9 |

**给下游 Boundary 的三点提示**：① p12 为判读总纲，p03/p04/p09/p11/p15 是"同单元硬软并存"的具体样本，不可整条标成单一 force；② p09 与 p14 的 `should` 分别承载"覆盖全部个案"与"裁量式禁止"，说明 `should` 不可一律译为"建议"；③ p08 的 15 天（PN 上限）与 6.9.13 的 15 天（CBP 报关）同数异义，p03 的 30 天与 p09 的 30 天 / p15 的 90 天为三套独立窗口，蒸馏时须锚回法条与当前版本 IOM/RPM 复核。
