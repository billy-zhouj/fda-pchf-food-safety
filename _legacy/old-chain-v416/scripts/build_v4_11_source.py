#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_v4_11_source.py — 把 CP 7303.842 的 pdf2md-pro 转换产物落为第十六来源正式文件。

输入：用户提供的官方 508-Compliant PDF 经 pdf2md-pro 转出的 Markdown
      （本机暂存 C:/Users/周至/AppData/Local/Temp/cp7303842/cp-7303-842-full.md）
输出：source-cp-7303-842-2023.md = 文件头（导入说明）+ `## 正文（转换原文，未改写）` + 原文

沿用 v4.10 纪律：文件头是我方转述、绝不参与逐字引文匹配；正文分界标题之后才是原文。
"""
import hashlib
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
RAW = Path(r"C:/Users/周至/AppData/Local/Temp/cp7303842/cp-7303-842-full.md")
OUT = BASE / "source-cp-7303-842-2023.md"
MARKER = "## 正文（转换原文，未改写）"

if not RAW.is_file():
    raise SystemExit(f"FATAL: 找不到转换产物 {RAW}；请先用 pdf2md-pro 重跑转换")
raw = RAW.read_text(encoding="utf-8")
assert MARKER not in raw, "转换产物不应已含正文分界标题"
h = hashlib.sha256(raw.encode("utf-8")).hexdigest()
size = len(raw.encode("utf-8"))
lines = raw.count("\n") + 1

header = f"""# FDA Compliance Program 7303.842 — Seafood Processor, Products, and Importer Inspection Program（2023 版程序 / 2025-09-30 更正）

> **来源**：用户提供的官方 508-Compliant PDF `20250929_CP 7303.842 Seafood Processor, Products, And Importer Inspection Program 508-Compliant.pdf`（912 KB / **80 个物理页**，首页标 `Page 1 of 86` / **148 个 PDF 书签** / 文本层完好），经用户级技能 `pdf2md-pro`（本机 `pymupdf4llm 2.1` + `pymupdf 2.1`，`PYTHONUTF8=1`）转换，保留英文原文以便逐字引证。转换产物 {size:,} 字节 / {lines:,} 行，sha256 `{h}`。
> PDF 元信息：title `Food Compliance Program Guidance Manual 7303.842: Seafood Processor, Products, and Importer Inspection Program`，author `FDA`，creator `Acrobat PDFMaker 25 for Word`，creationDate `D:20250929135237-04'00'`，modDate `D:20250929142349-04'00'`。
> ⚠ **版本判定（勿按文件名或首页签发日误读）**：封面写 `IMPLEMENTATION DATE 11/01/2023`、`Correction date: 09/30/2025`、`Date of Issuance: 09/30/025`（末项 PDF 文本层疑似缺字），正文多处页脚为 `Date of Issuance 11/1/2023`；PDF creationDate 为 **2025-09-29**。故文件名 `20250929` **只是 PDF 生成日**，本件是 **2023-11-01 版程序的 2025-09-30 更正本**，不是 2025 年新签发的 program。与 CP 7303.050（2022 签发 / 2025-09-10 更正）、CP 7303.070（2024 签发 / 2025-09-26 更正）、CP 7303.878（2023 版 / 2025-08-28 更正）同属「旧程序 + 更正本」形态，也不同于 CPGM 7303.040 的 `2025-CPM-HFP-001` 新 Transmittal。引用写「CP 7303.842（2023 版 / 2025-09-30 更正）」。
> ⚠ **程序合并**：封面 PRODUCT CODES 与 PART I 均写明 **CP 7303.842（Seafood Processor Inspection Program）与 CP 7303.844（Imported Seafood Inspection Program）已合并为单一合规程序 CP 7303.842**；但 `PAC codes for sampling and analysis will still reflect whether the product is imported or domestic`——合并的是程序，不是 PAC 码体系。

## 效力层级与使用边界（导入说明，非原文）

- 本件是 **FDA Compliance Program Guidance Manual 第 7303.842 章**，是 FDA 给**检查员、进口分区、分部合规官与实验室**的内部作业指导（PART I/II/III 明写 `provides instruction to field staff`、Program Management Instructions），覆盖检查优先级、检查实施、取样、实验室分析分流、执法建议与报告上报。**不是法规、不是 Guidance for Industry、不创设企业义务**；企业义务仍须回指 **21 CFR Part 123〔§ 123.xxx〕**（本包第十四来源，CAP-22）与 **Part 117 Subparts A/B/F**，进口商验证另按〔§ 123.12〕。CP 原文 L276 明确 `the requirements for subparts C and G of part 117 cannot replace the requirements defined in part 123`。
- ⚠ **法源三角与「转引未收」**：本 CP 大量回指 **CPG Sec. 540.525 / 540.370 / 555.600 / 562.300 / 540.250 / 540.590**、**21 CFR part 120 / 1240 / 108 / 110 / 507**、**NSSP Guide / Model Ordinance**、**BAM / AOAC / LIB / MPM 方法全文**、**Import Alert 16-74 / 16-20 / 99-41 全文**、**IOM Chapter 4**、**FDA 3501 / 3502 表单全文**、**Seafood List**、**eNSpect / CMS / FACTS / MARCS-CMS 内部系统**、**FDA–NMFS MOU / FMD#-029** 与 **FSVP 法规 21 CFR part 1 subpart L** —— 这些正文**本包仍未收**，一律标「转引未收」，**不得从本 CP 反推条文原文、方法 SOP 或企业义务**。已收的 **《Fish and Fishery Products Hazards and Controls Guidance》第 4 版**（第十五来源，CAP-23）是配套技术指南层，CP 多处只作指向（Ch.3 / Ch.6），其 Appendix 5 回指的外部法源仍须标「转引未收」。
- **与本包既有来源的接口（最易误用处）**：① **Part 123 法条层 → CAP-22**：条款级义务、法定定义、HACCP 计划要素、法定时限、是否违法，一律转 CAP-22；本卡只给 Table 4 的 `Deficiency → Citation → Major/Minor` 映射与 case-by-case 提示。② **海产品危害判定链 → CAP-23**：某鱼种/工艺有哪些危害、Ch.3 三表、reasonably likely to occur、CCP/关键限值、天然毒素 action level 具体数值，一律转 CAP-23；本 CP 只指向 Hazards Guide 章节，不给技术判定。③ **FSVP 进口商检查 → CAP-21**：FSVP（FD&C Act §805 / 21 CFR part 1 subpart L）与本 CP 的〔§ 123.12〕进口商验证是两套法源；CP 7303.878 明写 `Samples will not be collected as part of an FSVP inspection`、PART IV 全空，而本 CP 的进口商 HACCP 检查会取样，不得反向套用。④ **通用取样 → CAP-17**：CP 7303.050 的样品量与环境拭子（Listeria ≥50 / Salmonella ≥100）是另一套，不得与本 CP 的 surveillance 取样量互套。⑤ **LACF/AF → CAP-19/20**：CP 7303.070 的 pH 4.40/4.65/24 罐与本 CP 的 pH 4.6（腌渍海产品追加分析触发）用途不同；Import Alert 99-37/99-38 与 16-74/16-20 不是同一组。
- **引用规范**：本件内容标注「**CP 7303.842 PART II Table 1**」「**CP 7303.842 PART III.E**」「**CP 7303.842 PART IV.C**」「**CP 7303.842 PART V Table 4**」「**CP 7303.842 ATTACHMENT A #3**」这类部/节/表/附件号；因导出件存在书签标题与正文伪标题交错，可另附 `Lxxx` 行号辅助定位（行号指本文件**正文区**相对转换产物的行号，落地文件因文件头有偏移，逐字引证须以原文字符串为准、不以行号为准）。全包自 v4.11 起 **十六类来源不可混引**（21 CFR Part 117 / PCHF 行业指南 / L.mono Draft / SECG / Ed.5 / Food Defect Levels Handbook / CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / 21 CFR Part 113 / 21 CFR Part 114 / CP 7303.878 / 21 CFR Part 123 / Seafood Hazards Guide 第 4 版 / **CP 7303.842**）。

## 关键口径（逐字核对，勿沿用二手摘要）

- **合并 ≠ 统一 PAC**：取样/分析 PAC 进口 `03844x / 04844A / 07844 / 09844x / 21844`、国产 `03842x / 04842A / 07842 / 09842x / 21842`（L12–L25）；检查报告 PAC 另有 `03842`（documentary / 非 HACCP 评估）、`03842H`（Processor HACCP Inspection）、`03844H`（Importer HACCP Inspection）、`03040`（PC training）（L26–L33）。⚠ `03842H` 在 L18 是 `HACCP Verification (i.e., verification of adequacy of HACCP plan critical limits)` 且进口列 `Not applicable`，在 L31 却是 Processor HACCP Inspection 报告 PAC，**同名不同义**。所有 documentary samples **只报 PAC 03842**，不得用以 `H` 结尾的 HACCP 验证 PAC，也不计入 Division Workplan 义务（L339）。
- **Table 1 / Table 2 分工**：Table 1 按产品/工艺危害与行业合规情况降序排海产品 commodities，用于「确定 HACCP 检查焦点」，且 `Table 1 is not all inclusive`、表外产品/工艺须查 Hazards Guide 第 3 章、产品跨多类取**最高风险类别**（L158–L159、L161–L189）；Table 2 **仅用于 work planning**，在 Table 1 基础上按企业/进口商个体合规史降序，进口商检查数量由 OII workplan 定、**90%** 计划检查给高风险进口商、**10%** 给年进口 <100 entry line items 者，OAI 复检须待整改完成（L191–L206）。取样风险判断用 **Table 1**（L334），不是 Table 2。
- **检查类型分流**：Processor（多程序适用时分别覆盖、时间有限优先 `03842H`，L273）；Importer（〔§ 123.12〕验证、Table 2 选人 / Table 1 选产品、食品安全 MOU 国家产品排除、书面验证程序与 affirmative steps、每产品一份 FD 3502；**境外加工商 HACCP 计划的其他缺陷不得写进 483**，须取计划副本转 HFP，L311–L324）；Vessels（通常靠港且非作业时检查，L289）；Foreign Establishments（产品风险 + 合规史选点、只覆盖输美产品，L299–L301）；NSSP（须 shellfish standardized inspector / officer，用 ISSC Form 93-01(A)、依 NSSP Model Ordinance，L308）；EMA / Food Fraud（一般监督须先得 HFP concurrence，L75；比对采购订单/原料标签/成品标签，L296）。
- **HACCP Program Evaluations**：聚焦企业**最高风险产品**且须在企业**已知在生产**时进行（L275）；Part 117 subparts C/G **不能替代** Part 123 法定义务（L276）；significant observations 与自愿纠正项区分，重大 123 与 GMP 缺陷上 **FDA 483**、叙述性 EIR 按监管重要性降序（L283–L285）。
- **Sampling 三类**：国产官方样品 `Domestic official samples are to be collected "for cause" only.`，不必常规采国产样支持 HACCP 违规监管行动、控制明显不足时不取样而在 483 说明、确需取样须先联系 HFP（L327）；进口监督取样数量由 OII Workplan 定、既往有安全缺陷的国外加工商/发货人条目优先、样品多数取自高风险产品（L330、L334）；documentary samples 见上（L339）。
- **PART IV 阈值性质（最高频误读）**：组胺 **500 / 50 / 35 ppm**（L510–L526）、Indole **15 / 25 µg/100 g**（L559–L587）、感官 subs 数 18 / 24 / 12 / 18（L498、L552、L603）、活虫零容忍（L448）、pH <4.6 结束分析 / ≥4.6 再查 WPS 与 nitrite（L782）、熏鱼亚硝酸盐 100 ppm（L770）、RSSL ≥98% / <98% 物种鉴定 Lab Class 1/3 与 8 subs/lot（L951、L963–L965）、净重过镀冰 **48 subs** + AOAC 963.18（L942–L943）、5 inches 未去脏鱼（L166、L638）、Filth 6 个 2–3 lb subs（L382）——**全部是 CP 的检查/取样/追加分析/上报触发阈值与样品量，不是法规限值、不是产品放行标准、不是 BAM/AOAC 方法全文**。判据出口分别是 CPG Sec. 540.525 / 540.370 / 562.300 / 555.600 与 Hazards Guide 第 6 章 action levels（L544、L589、L610、L873、L945、L1105）；subs 数多处明说 `only for surveillance and audit samples`（L465、L546、L565、L1210 #3），reconditioning / DWPE 放行 / Domestic HACCP Verification 各有不同规则。
- **PART V Table 4 是 ranking 不是自动执法结论**：逐条给 `Deficiency → Citation(123.x) → Major/Minor`（L989–L1056），但原文 `Significance must be determined on a case-by-case basis`（L1057）；Major/Minor 定义针对 HACCP 系统完整性与食品安全风险（L1059–L1060），不是 §123.6 的 significant hazard 判定。记录伪造归 Title 18 / OCI，不在表内分级（L1008）。非 123 违规（misbranding / EMA / 非鲭毒分解 / 非安全 GMP）在 L1068–L1070。
- **执法动作须裁量与 Center 一致**：Warning Letters `should be considered` for significant deviations（L1074）；DWPE 针对国外检查/记录审查偏差未纠正的境外加工商，放行或移出 import alert 须 HFP OCE concurrence（L1077）；Judicial actions 建议须 HFP OCE 评估同意、FACTS 入案、CMS 电子提交（L1084）；NMFS 通知依 MOU / FMD#-029（L1072）；Species misbranding 违反 **FD&C Act 403(b) / 21 U.S.C. 343(b)**，监管建议经 MARCS-CMS 提交（L1088–L1090）。
- **FIELD REPORTING REQUIREMENTS（目录之前，L44–L115）**：分析结果报 FACTS（PAF 对照 L53–L73）；OAI 且建议行动时经 CMS 提交 EIR / FDA 483 / endorsement（L91–L93）；支持扣留或 DWPE 的样品经 CMS 提交标签、entry docs、实验室工作表、Collection report（L96–L103）；HACCP 部分用 **FDA 3501（Processors）/ FDA 3502（Importers）**，每个被评估产品各一份，进 National Seafood HACCP Inspection Database（L104–L107）；misbranding / 物种替代证据写入 FDA 483 与 Species Substitution Questionnaire（L114–L115）。
- **ATTACHMENT A 适用域**：Table A-1 / A-2 给取样量与样品处理（L1195–L1205、L1307–L1334），General Information 20 条给专项指令；但样品量**仅适用于 surveillance and audit samples**（L1210 #3），不可作为 reconditioning 验证成功、DWPE 放行（#4）或 Domestic HACCP Verification（#5 须先咨询 HFP）的取样量；702(b) duplicate 部分不含在表列 subs 内（#6）；Filth 仅 for cause（#11）；CFP 只在疾病/暴发响应时采（#14）；RTE 才做 Listeria（#9）。

## 转换局限

- `pdf2md-pro` 自检：148 个书签全部命中（`bookmarks_dropped` 0）、表格行 203、残留独立页码 0、`- Page N` 0、自动探测噪音 3 行。转换时 `pymupdf4llm 2.1` 内部 OCR 探测线程抛过一次 Windows 子进程 stdout 的 `UnicodeDecodeError` 告警，并提示 `RapidOCR is missing`，**均不影响文本层输出**（与 CP 7303.878 文件的历史记录同型）。
- ⚠ **标题层级交错（与 CP 7303.878 / CP 7303.070 同型）**：PDF 书签被提升为 `##/###/####`，正文里原有的全大写/加粗小节同时被 `pymupdf4llm` 识别成 `# **…**` 伪标题，故 PART II / III / IV / V 等各出现两次、H1 统计虚高至 133（合计 290 个标题标记）。**检索与引用一律以 PART 号 / 小节号 / 表号为准，不以 Markdown `#` 层级为准**；未对导出件做手工改写，以保持原文可逐字核验。
- 正文含 `<u>…</u>` 下划线/超链接标记与 `<br>` 折行标签；表格列头存在连写、单元格内换行与页码混入；封面 `Date of Issuance: 09/30/025` 为 PDF 文本层残缺形态，PAC 表内 `021842` 疑为 `21842` 转录变形，Import Alert 16-74 一句存在重复词。**逐字引证须按「剥离 Markdown 标记 + 空白归一化」核对，不要按 Markdown 行边界或表格单元格边界核对**；表格、页码、页眉、纯数字行不得用作逐字引用。
- 矢量绘制的表格标记（如勾选符号）会丢失；跨页断表在分页处截断；合并单元格 Markdown 无法表达。涉及勾选项、跨页表或版面判读时须回 PDF 原件视觉核对。
- 文件头为导入说明，非原文；转换报告中的 chars/lines 为加文件头之前的数值。

{MARKER}

> ⚠ 以下为 `pdf2md-pro` 转换产物原文，未做任何改写。逐字引文校验请从本标题**之后**取值（`body_only()`），文件头一律不得参与匹配，否则形成自我验证循环。行号标签 `Lxxx` 指本正文区相对转换产物的原始行号。

"""

out = header + raw
OUT.write_text(out, encoding="utf-8")
print(f"wrote {OUT.name}: {len(out.encode('utf-8')):,} bytes / {out.count(chr(10))+1:,} lines")
print(f"raw sha256: {h}")
print("body marker count:", out.count(MARKER))
