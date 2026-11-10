# CP 7303.842 整书理解框架（v4-11）

> 数据来源（只读）：`cp-7303-842-full.md`（pdf2md-pro 产物，1334 行）与 `convert-report.json`。
> 行号一律写作 `Lxxx`。由于 PDF 书签标题（如 `## PART II - IMPLEMENTATION`）与正文大写伪标题（如 `# **PART II - IMPLEMENTATION**`）交错并存，同一 PART 常出现两个相邻标题行（例：PART II 在 L147 与 L153、PART III 在 L242 与 L250、FIELD REPORTING REQUIREMENTS 在 L44/L50/L51），**检索与引用一律以 PART 号 / 小节号 / 表号为准，不以 markdown `#` 层级为准**（L117–L138 目录、convert-report.json L5–L13）。

---

## 1. 文档基本信息

| 项 | 内容 | 行号 |
|---|---|---|
| 标题（markdown 首行） | CP 7303.842 Seafood Processor, Products, and Importer Inspection Program | L1 |
| 封面 SUBJECT | SEAFOOD PROCESSOR, PRODUCTS, AND IMPORTER INSPECTION PROGRAM | L4 |
| 合并后正式程序名 | CP 7303.842, Seafood Processor and Products Inspection Program | L7 |
| 文档属性 | FOOD AND DRUG ADMINISTRATION COMPLIANCE PROGRAM GUIDANCE MANUAL | L3 |
| PROGRAM 编号 | 7303.842（页眉重复出现 PROGRAM 7303.842） | L1、L7、L989、L1207、L1212、L1225、L1246、L1261、L1271、L1281、L1296 |
| IMPLEMENTATION DATE | 11/01/2023 | L6 |
| Correction date | 09/30/2025 | L6 |
| Date of Issuance（封面） | 09/30/025 —— 疑似 OCR 缺位（应为 09/30/2025 或 11/1/2023），与页脚不一致 | L8 |
| Date of Issuance（正文页脚） | 11/1/2023（多处重复） | L1182、L1191、L1201、L1213、L1224、L1247、L1260、L1270、L1282、L1295 |
| Data Reporting | 见 PRODUCT CODES 单元格内 `**DATA REPORTING**` 标注 | L6 |
| Industry Code | 16（USE APPLICABLE CLASS, SUBCLASS, PIC, AND GROUP PRODUCT CODES） | L7 |

**物理页数与首页标注的逻辑页码（需区分，勿混）**

- 物理页数：两份输入**均未直接给出 PDF 物理总页数**——`convert-report.json` 无 page/page_count 字段（L2–L19 只有 chars/lines/headings/table_lines/bookmarks），markdown 内也无 "Page N of M" 字样。可用的物理规模代理量：`chars` 179111、`lines` 1334、`table_lines` 203、`total_headings` 290（convert-report.json L3、L4、L14、L13）。由 ATTACHMENT A 内页眉/页脚块 `PROGRAM 7303.842` + `November 1, 2023` 重复出现（L1207、L1212、L1225、L1246、L1261、L1271、L1281、L1296 等 8+ 处）可推断 ATTACHMENT A 至少跨 8 个物理页，但无确数。
- 首页（目录页）标注的逻辑页码：**Contents 目录给出的是逻辑页码，不是物理页**（L117–L138）：PART I = 7（L118）、PART II = 8（L120，Objective/Program Management 同 8，L121–L122）、PART III = 17（L123，Operations 17 / A 17 / B 17 / C 18 / D 21 / E 22，L124–L129）、PART IV = 24（L130，Analyzing Laboratories 24，L131；2. Adverse findings 53，L132）、PART V = 54（L133）、PART VI = 62（L134，Attachments 62 / Program Contacts 63，L135–L136）、PART VII = 65（L137）、ATTACHMENT A = 66（L138）。即正文逻辑页 7–66（约 60 页范围），前置逻辑页 1–6 对应封面、PAC 码表、FIELD REPORTING REQUIREMENTS、Contents（L1–L116，均无显式页码）。

**书签数与标题交错**

- 书签：`bookmarks_used` 148、`bookmarks_dropped` 0（convert-report.json L15–L16）。
- 标题统计：H1 133 / H2 48 / H3 83 / H4 26 / H5 0 / H6 0，合计 `total_headings` 290（convert-report.json L6–L13）。290 个标题标记 = 148 个 PDF 书签 + 约 142 个正文大写伪标题（如 `# **<u>Laboratory Reporting</u>**` L51、`# **PART IV - ANALYTICAL**` L345、`# **<u>Importer Inspections</u>**` L310）被识别为标题；`auto_detected_noise_lines` 3、`residual_standalone_pagenum` 0、`residual_dash_page` 0（L17–L19）。

**CP 7303.842 与 CP 7303.844 合并说明**

- 封面 PRODUCT CODES 单元格：CP 7303.842（Seafood Processor Inspection Program）与 CP 7303.844（Imported Seafood Inspection Program）**已合并为单一合规程序 CP 7303.842, Seafood Processor and Products Inspection Program**；但 **PAC codes for sampling and analysis will still reflect whether the product is imported or domestic**（L7）。
- PART I 复述合并：current Seafood Processor and Imported Seafood Inspection Program, CP 7303.842, is a combination of the previous CP 7303.842 与 CP 7303.844（L142）。
- 该程序同时覆盖国内与国外（domestic and foreign）进口/加工鱼及制品企业（L142）；FDA 依据 **21 CFR Part 123（Seafood HACCP Regulation）** 及 **21 CFR Part 117 subparts A、B、F** 检查国内外加工商与进口商（L143）；HFP 整合进口商与国外加工商调查活动（L144–L145）。

**PAC 码进口 / 国产区分**（合并后仍保留，勿以为合并即统一）

- 取样/分析 PAC（REPORT COLLECTIONS AND ANALYSIS，L11–L25）：进口一律 `03844x` / `04844A` / `07844` / `09844x` / `21844`，国产一律 `03842x` / `04842A` / `07842` / `09842x` / `21842`（表 L12–L25）。逐项：化学分解 Indole/histamines 03844A/03842A（L14）、Filth 03844B/03842B（L15）、Scombrotoxin 分解 03844C/03842C（L16）、Microbiological（含 WPS/pH/aw）03844D/03842D（L17）、HACCP Verification（验证 HACCP 计划关键限值充分性）03842H、进口列 "Not applicable"（L18）、Chemical Contamination 04844A/04842A（L19）、Natural toxins（ASP/DSP/NSP/AZP/CFP/TTX/PSP）07844/07842（L20）、Color Additives 09844E/09842E（L21）、Food Additives 09844F/09842F（L22）、Economically motivated adulteration/Misbranding 21844/021842（L23，后者疑为 21842 的 OCR 变形）、Nutritional Health Fraud 21R829、Label Reviews 21005（L24–L25，进口国产共用）。
- 检查报告 PAC（REPORT INSPECTIONS，L26–L42）：03842 = Documentary samples 或非 HACCP 评估的海产品检查活动（L30）、03842H = Processor HACCP Inspection（L31）、03844H = Importer HACCP Inspection（L32）、03040 = PC training（L33）；FDA 与 State Partnership 工作均报 03842 与 03842H（L27）。附加报告用 PAC：03R833 Entry Review、99R833 Filer Evaluation OP95、03R824/04R824/07R824/09R824 Follow-up to Refusals（L34–L42）。
- 硬性口径：所有 documentary samples 只用 PAC 03842，**不得使用以 "H" 结尾的 HACCP 验证 PAC，也不计入 Division Workplan 义务**（L339）。

---

## 2. PART I–VII 逐部（含 FIELD REPORTING REQUIREMENTS、ATTACHMENT A 单列）

> 目录给出的逻辑页码见 L118–L138；下表"定位行号"取书签标题/伪标题首现行与正文起止。

### PART I – BACKGROUND（L140 书签标题；正文 L142–L145；目录逻辑页 7，L118）
- 目的：为本程序建立监管覆盖对象与法律基础——覆盖国内与国外进口/加工鱼及制品企业，确保美国海产品供应安全卫生；明确现场人员所需培训与技能；给出产品、工艺、企业的检查优先级指令；给出样品采集与分析指令（L142）。
- 关键内容：21 CFR Part 123（含 eCFR 链接）与 21 CFR Part 117 subparts A/B/F 的适用（L143）；Fish and Fishery Products Hazards and Controls Guidance（Seafood HACCP Guide）用于协助制定 HACCP 计划（L143）；HFP 整合进口商与国外加工商调查，进口商调查数据用于分配国外检查资源、国外调查数据反哺识别不合规进口商/地区/第三方认证可靠性（L144–L145）；合并说明（L142）。

### PART II - IMPLEMENTATION（L147 书签 / L153 伪标题；正文 L154–L240；目录逻辑页 8，L120）
- 目的（Objective，L154–L155）：确保美国鱼及制品安全卫生供应；通过对进口商及国内外加工商检查确认符合 FD&C Act 及实施法规；提供基于风险选择产品、工艺、进口商的工具；指导其他合规程序如何适用于海产品加工商/进口商。
- 关键小节清单：
  - Program Management Instructions（L156–L157）：OII workplan 资源覆盖 PPS 03/04/07/09/21，除大量时间花在特定领域外无需逐项归属（L157）。
  - Product Prioritization for Inspection by Risk（L151、L158–L159）。
  - **Table 1 - Product and Process Priority Ranking**（L161；表体 L163–L189；补充口径 Allergens / Natural marine toxins / Lower regulatory priority hazards，L187–L189）。
  - **Table 2 – Priorities for Establishment and Importer Inspections**（L191 书签 / L200 伪标题；说明 L193–L199；表体 L201–L206）。
  - Inspection Prioritization for Establishments (Processor and Importer) by Risk（L193–L199，含 90%/10% 与 100 lines 规则 L197、主动申请 Approved List 的低优先设施仍须尽快检查 L198、OAI 复检须待整改完成 L199）。
  - Interaction with Other Programs/Assignments（L208–L231）：CP 7303.070 酸化/低酸罐头（L212–L214）、CP 7318.004 软体贝类/NSSP（L215–L217）、CP 7321.005 标签（L218–L220）、CP 7304.004 农药（L224–L225）、CP 7304.019 毒性元素（L226–L227）、CP 7304.018 化疗药（L228–L229）、CP 7321.008 膳食补充剂（L230–L231）。
  - Federal/State Contracts and Partnerships（L222、L232–L238，含 FD 249 与 Seafood HACCP Alliance 3-day 课程、FDA 3501 要求，L234–L238）。
  - National Marine Fisheries Services (NMFS)（L236、L239–L240，MOU 与 FMD#-029）。

### PART III - INSPECTIONAL（L242 书签 / L250 伪标题；正文 L251–L339；目录逻辑页 17，L123）
- 目的（Operations，L251–L252）：检查须由受训（FDA 或 State）人员按 Conducting Seafood Inspections Training Course（FD 249）与 IOM 进行；国内/国外 HACCP 检查按后续指令执行并填 Form FDA 3501 或 3502。
- 关键小节清单：
  - Technical References（L246、L253–L260）：FD 249 手册、Importer Verification 手册、Hazards Guide、Sanitation Control Procedures、Part VI 参考文献（L256–L260）。
  - Training Requirements（L244、L261–L271）：Seafood HACCP Alliance 3-day 或等效（L263）、FD 249（L264）、IM 239 + FD249W200（L270）、推荐 Sanitation Control Procedures Course（L271）。
  - C. Processor Inspections（L266、L272–L287）：多程序适用时分别覆盖、时间有限时优先 03842H（L273）；**HACCP Program Evaluations**（L268、L274–L287）；Special Instructions for Vessels（L279、L288–L289）；Special Instructions for Economically Motivated Adulteration or Food Fraud（L293、L295–L297）；Special Instructions for Foreign Establishment Inspections（L291、L298–L301）。
  - D. Importer Inspections（L303、L310–L324）：21 CFR 123.12 验证义务、Table 2 选人 / Table 1 选产品、MOU 国家产品排除、书面验证程序与 affirmative steps / product specifications 审查、FD 3502 每产品一份（L311–L324）。
  - E. NSSP Establishment Inspections（L305、L307–L309）：须 shellfish standardized inspector/officer，ISSC Form 93-01(A)，依 NSSP Model Ordinance，含 HACCP 计划、卫生监控记录、设施巡检（L308）。
  - **Sampling**（L316、L325–L339）：Domestic "For Cause" Sampling（L320、L326–L328）、Imported Seafood Surveillance Sampling（L318、L329–L337）、Documentary Samples（L332、L338–L339）。

### PART IV - ANALYTICAL（L341 书签 / L345 伪标题；正文 L346–L971；目录逻辑页 24，L130）
- 目的（Analyzing Laboratories，L343、L346–L355）：按"监测样品分析"给出方法、实验室、报告、判据；分节 A–G（L348–L352）：A Filth/Mold/Foreign Objects（Micro/Macro，Project 03）、B Parasites（03）、C Decomposition（Scombrotoxin/histamine、indole、organoleptic，03）、D Microbiological（03）、E Natural Toxins（07）、F Food and Color Additives（09）、G Food Composition, Standards, Labeling & Fraud（21）。化疗药分析归 CP 7304.018、化学污染物归 CP 7304.004 / 7304.019（L353–L354）。
- 每 Project 的固定结构（伪标题簇 L356–L364）：FIELD LABORATORIES / METHODOLOGY / REPORTING / CONTACTS / **CRITERIA FOR REGULATORY ACTION**。
- 关键小节清单（定位行号）：A Filth（L368–L442，含 Disease Carrying Insects L405–L442、Flies/Ants 清单 L413–L442）；B Parasite Analysis（L430–L463，含 NOTE 零容忍 L447–L448、Parasite Identification L449–L452）；C Decomposition Analysis（L461–L610，含 Organoleptic/Indole/Histamine 方法 L470–L473、Scombrotoxin 形成种 L488–L543、Shrimp L534–L589、Other Products L593–L610）；D Microbiological（L595–L795，含 Listeria L629/L644–L668、Salmonella L663–L687、Staphylococcus L679–L708、Vibrio L703–L736、Clostridium L726–L754、Additional Analyses WPS/pH/aw/nitrite L745–L784、Molluscan Shellfish L773–L795）；E Natural Toxins（L807–L873，含 PSP L822–L826、ASP L834–L841、DSP L832–L846、NSP L830–L848、AZP L828–L860、CFP L857–L863、TTX L855–L870、REPORTING L871–L873）；F Food and Color Additives（L883–L935，含亚硫酸盐虾/金枪鱼 L906–L921）；G Project 21（L931–L971，含 Net Weight - Overglazing L929–L945、Species Substitution L933–L955、CRITERIA FOR REGULATORY ACTION (Species substitution) L953、**Table 3 Lab Classifications L960–L967**、报告 L968–L971）。
- CRITERIA FOR REGULATORY ACTION 节点：Filth L381–L396；Parasites L447–L448；Scombrotoxin/Decomp/Histamine → CPG Sec. 540.525（L543–L544）；Shrimp/Indole → CPG Sec. 540.370（L588–L589）；Other Products → CPG Sec. 540.370（L609–L610）；Net Weight → CPG Sec 562.300（L944–L945）；Natural Toxins → action levels 在 Seafood HACCP Guide 第 6 章（L873）；Species substitution → Table 3 分类（L960–L967）+ 403(b)（L1088）。

### PART V - REGULATORY/ADMINISTRATIVE STRATEGY（L975 书签 / L979 伪标题；正文 L980–L1127；目录逻辑页 54，L133）
- 目的（L980）：同时处理 HACCP 与非 HACCP 缺陷；当 OHFI Division 认为产品构成迫近公共卫生危害、或检查趋势 OAI 时，走 OCIC 咨询或与 OE compliance officer 协作。
- 关键小节清单：
  - SEAFOOD HACCP VIOLATIONS INCLUDING SANITATION MONITORING（L973、L981–L986）：可依 402(a)(4) 单独建议监管行动，无须叠加 402(a)(1)/(a)(3)（L982）；案例优先级 L984–L986。
  - **Table 4, Seafood HACCP Enforcement Strategy: Ranking of violation**（L977、L987、L989–L1057；Ranking Definitions L1057–L1060）。
  - VIOLATIONS OF REGULATIONS OTHER THAN 21 CFR 123（L1068–L1070）：misbranding、EMA、非鲭毒分解、非安全相关 GMP 等，用 Compliance Intake and Consultation Form，Warning Letter 不限于 123 违规。
  - NATIONAL MARINE FISHERIES SERVICE (NMFS) NOTIFICATION（L1066、L1071–L1072，MOU / FMD#-029）。
  - ADVISORY ACTIONS – WARNING LETTERS（L1064、L1073–L1075）。
  - DETENTION WITHOUT PHYSICAL EXAMINATION (DWPE)（L1062、L1076–L1078）。
  - SPECIES MISBRANDING（L1080、L1087–L1092，403(b)/21 U.S.C. 343(b)、MARCS-CMS、Domestic-Import samples 的 DWPE L1091–L1092）。
  - JUDICIAL ACTIONS（L1082–L1086，seizure/injunction/prosecution，须 HFP OCE concurrence，Preliminary Assessment Calls，L1084–L1086）。
  - REGULATORY GUIDANCE – SOURCES / CPG 清单（L1096、L1102–L1127）；HFP REGULATORY CONTACTS（L1098–L1101）。

### PART VI REFERENCES, ATTACHMENTS, AND PROGRAM CONTACTS（L1129；目录逻辑页 62，L134）
- 目的：集中列出附件、参考文献与程序联系人，不在正文展开。ATTACHMENTS – Tables A-1 and A-2 Sampling Guide（L1131）、REFERENCES 清单（L1133–L1149，含 Hazards Guide、Final Rule Part 123、CGMP Part 117 Subpart B、Sanitation Control Procedures Manual、IOM、RPM、CPG Manual、Environmental Sampling for Listeria/Salmonella、Seafood List、拒绝检查/HACCP 记录指引、1991 镀冰信函、Food Defect Levels Handbook 等）；PROGRAM CONTACTS（L1167–L1181，按 General Program / Investigational / Enforcement / Scientific-Technical-HACCP Policy / Analytical / Laboratory 分类对口人）。

### PART VII - CENTER RESPONSIBILITIES（L1184 书签 / L1188 伪标题；正文 L1189–L1191；目录逻辑页 65，L137）
- 目的（Program Evaluation，L1186、L1189–L1190）：HFP 在程序运行中识别运行/质量缺陷；Division of Seafood Safety **每四年**提交一次项目评估（L1190）；页脚 Date of Issuance 11/1/2023（L1191）。

### FIELD REPORTING REQUIREMENTS（单列；全部集中在目录之前的前置部分，L44–L115）
> 重要：该组内容物理上位于 Contents（L117）**之前**，不在 PART I–VII 之内，是判定链的"末端出口"。书签/伪标题交错：L44（`## FIELD REPORTING REQUIREMENTS:`）、L50（`# **FIELD REPORTING REQUIREMENTS:**`）、L51（`# **<u>Laboratory Reporting</u>**`）、L74、L90、L95、L104、L114。
- Laboratory Reporting（L48、L52–L73）：分析结果报 FACTS，PAF 对照表（BIO/COL/DEC/FIL/FAD/MIC/SAL/ABR/GSA/GLI/GVC/GVP/GCB/WPS-NTR/NAR/PAR/PES，L53–L73）。
- Economically Motivated Adulteration (or food fraud)（L46、L74–L83）：一般监督须先得 HFP concurrence（L75）；PAF FDL/FDF/FDE/FDQ/FDI（L77–L83）。
- Inspection/Investigation Reporting（L88、L90–L94）：processor/importer 检查被判 **OAI** 且 Division 建议行动时，经 CMS 提交 EIR、FDA 483、EIR endorsement（含封面页）（L91–L93）；报告内容见 Part III（L94）。
- Samples Supporting Regulatory Action（L86、L95–L103）：支持扣留或 DWPE 申请的样品，经 CMS 提交 CO 备忘录、产品标签、entry documents（CBP 3461/7501、发票、装箱单、提单）、实验室工作表、Collection report、email 等（L96–L103）。
- Special HACCP Reporting（L84、L104–L112）：使用 **FDA 3501（Processors）/ FDA 3502（Importers）**（L105）；每个被评估产品各填一份，含现场与技术审查，进入 National Seafood HACCP Inspection Database 用于行业合规跟踪与产品/工艺风险排序（L106–L107）；"actively processing" 仅为 FDA 3501 Question 10 的特设定义（L108、L112）；系统问题联系人 L113。
- Special Misbranding and Species Substitution Reporting（L110、L114–L115）：misbranding 证据写入 FDA 483 并记录于 Species Substitution Questionnaire（L115）。

### ATTACHMENT A – Sampling Information（单列；L1193 书签标题，目录逻辑页 66，L138；正文 L1195–L1334）
- 作用：给出取样量、样品数、样品处理/运输的**操作指令**（非判据、非方法）。构成：TABLE A-1: Surveillance Sampling for Fish and Fishery Products（L1195–L1205）、General Information 第 1–20 条（L1209–L1305，含图片文本 L1210 与 #5/#9/#11/#14/#15/#16/#17/#18/#19/#20 各条）、TABLE A-2: ADDITIONAL SAMPLING INSTRUCTIONS（L1307–L1334，非鲭毒 finfish / 鲭毒 finfish / 罐袋杯 / 甲壳类 / 软体贝类 / 其他无脊椎类 6 个商品组）。

---

## 3. 完整海产品检查判定链（逐步、标行号）

```
Table 1 产品/工艺风险 + Table 2 企业/进口商优先级
        ↓
检查类型分流（Processor / Importer / Vessels / Foreign Establishment / NSSP）
        ↓
HACCP Program Evaluations（483 / EIR / FDA 3501·3502）
        ↓
Sampling（进口监督取样 / 国产 For Cause / Documentary）
        ↓
PART IV 实验室分析（A–G Project）→ CRITERIA FOR REGULATORY ACTION（CPG / Guide 第 6 章）
        ↓
PART V 执法策略（Table 4 分级 → DWPE / Warning Letters / NMFS / 司法 / Species Misbranding）
        ↓
FIELD REPORTING REQUIREMENTS（FACTS / CMS / FDA 3501·3502 / PAF·PAC）
```

### 步骤 1 · 检查优先级：Table 1 与 Table 2
- **Table 1（产品/工艺风险降序，L158–L189）**：按产品相关危害与行业合规情况对具体海产品 commodities 降序排列，用作"确定 HACCP 检查焦点"的指南（L159）。自 **HIGHER RISK POTENTIAL** 起：ROP（减氧包装）海产品 → `C. botulinum`（L165）；未去脏/部分去脏加工 finfish（>5 in 考虑 expedited action，L166，续 L170）→ `C. botulinum`；生食软体贝类 → Vibrio spp./Salmonella/甲肝/诺如/海洋毒素（L171）；熟制 RTE → 加工后交叉污染/病原存活（L172）；生 RTE（寿司等）→ 甲肝/Vibrio/Salmonella/`L. monocytogenes`/寄生虫（L173–L177）；鲭毒形成种（Table 3-2，L178）；RTE 与非 RTE 干制品（L179）；水产养殖初级加工者 → 未批准养殖药物（L180，续 L184）；至 **LOWER RISK POTENTIAL**：需烹调后食用/低监管优先危害/无需 HACCP 计划（L185）、冷冻与干货仓储（PAC 03842，L186）。
  - 规则：`Table 1 is not all inclusive`（L159）；产品跨多类时取**最高风险类别**为优先级（L159）；表外产品/工艺查 Hazards Guide 第 3 章（L159）；补充口径：过敏原（多成分/隐性过敏原风险更高，L187）、天然海洋毒素（初级加工者检查时处理，L188）、低监管优先危害（金属/玻璃碎片、环境化学物、甲基汞，L189）。
- **Table 2（企业/进口商优先级降序，L191–L206）**：用于 **work planning purposes**，在 Table 1 产品风险基础上按企业个体合规史降序排列国内外加工商与进口商（L196）；Table 1 用于每个 Row 内按产品风险再排序（L196）；国外优先级可因国别问题/进口数据/新发问题而不同（L196）。表体按列分 Processors 与 Importers（L201–L206）：OAI 复查 / 移除 red list 或加入 green list / 从未检查 / VAI(HACCP) / NAI（L202–L206）；进口商侧含"高风险产品且从未检查或年均 ≥100 行""高风险产品 <100 行""低风险产品"（L203–L205）。
  - 硬约束：进口商检查数量由 OII workplan 定，**90%** 计划检查用于高风险进口商、**10%** 用于年进口 <100 entry line items 的进口商（L197）；OAI 复检须待企业完成整改（L199）。

### 步骤 2 · 检查类型分流
| 分流 | 定位 | 要点 |
|---|---|---|
| **Processor Inspections** | L266、L272–L287 | 多程序适用（如金枪鱼罐头）须分别覆盖；时间有限（如国外检查）优先 HACCP（PAC 03842H），其余限量覆盖并在 EIR 体现时间分配（L273） |
| **Importer Inspections** | L303、L310–L324 | 依 21 CFR 123.12 验证国外加工商合规与危害受控（L311）；选人用 Table 2、选产品用 Table 1（L311）；FD 239 / FD 249 程序（L311）；**有食品安全 MOU 国家的产品排除**（L311）；现场审查书面验证程序、affirmative steps、product specifications（L312–L315、L322）；affirmative step 未列重大健康危害 → 记入 FDA 483（L323）；**境外加工商 HACCP 计划的其他缺陷不得写进 483，须收计划副本转 HFP 跟进**（L323）；每产品填 FD 3502，仅 FD 249 合格者可填 HACCP 计划缺陷栏（L324） |
| **Vessels** | L279、L288–L289 | 多数加工船无法在海上作业状态检查，通常在**靠港且非作业**时进行（L289） |
| **Foreign Establishment Inspections** | L291、L298–L301 | 选点理由同国内（产品风险 + 合规史，L299）；检查前审查出口/检查史并按 Table 1 选目标产品（L300）；目标产品未生产则选同风险/同控制产品（L300）；只覆盖输美产品（L300）；须取得文档与照片证据（L300） |
| **NSSP Establishment Inspections** | L305、L307–L309 | 须 shellfish standardized inspector/officer，用 ISSC Form 93-01(A)，依 NSSP Model Ordinance（L308）；PART II 另注：参与 NSSP 的州，FDA State contract 检查**不覆盖**生软体贝类（L216）；非 NSSP 但位于参与州的加工商报当地 shellfish authority（L217、L309） |
| 特殊分支：EMA / Food Fraud | L293、L295–L297 | 加工商 HACCP/GMP 检查中比对采购订单、原料标签与成品标签，misbranding 证据写入 FDA 483（L296）；物种替代可引入海洋毒素/过敏原/鲭毒等额外安全危害（L297） |

### 步骤 3 · HACCP Program Evaluations（L268、L274–L287）
- 聚焦企业**最高风险产品**、且须在企业**已知在生产时**进行（L275）；必要时先查生产计划（L275）。
- 合规范围提醒：21 CFR 123 只是其中一元，还须符合 Part 117 subpart B（GMP）及 subparts A/F；**Part 117 subparts C 与 G 不能替代 Part 123 对海产品加工商的法定义务**（L276）。
- 方法：全流程 walk-through（含返工/转序步骤）、访谈员工、观察操作、获取加工/卫生/员工操作信息、评估 HACCP 监控-验证-纠偏-卫生监控的实施（L277）；书面 HACCP 计划须对照企业自身危害分析与实施情况、访谈并审记录（L277–L281）；计划不充分或无书面计划时，判定是否有并实施能防止已识别危害的控制（L282）。
- 记录与分级：significant observations（影响 HACCP 整体完整性或恶劣不卫生条件）与自愿纠正项区分（L283）； adequacy 疑问找 SME / National Expert / HFP expert（L284）；重大 123 与 GMP 缺陷上 FDA 483，与安全直接相关的 GMP 缺陷记为 HACCP 卫生监控缺陷、非安全 GMP 缺陷记为 Part 117 subpart B；483 与叙述性 EIR 按监管重要性**降序**列示（L285）；可用 Seafood Inspection and EIR Template Tool（L285）。
- 未在生产：尽量改期；不可改期（国外/短汛期）则巡检 + 访谈 + 记录审查（HACCP 计划、监控、验证、纠偏、卫生监控记录），缺陷仍上 483（L286）。OAI/VAI 某产品复检无法完成时，仍须尽早复检该产品或同 HACCP 计划下相同 CCP 的产品，分类保持 open 至满意检查（L287）。

### 步骤 4 · Sampling（L316、L325–L339）
- **Domestic "For Cause" Sampling**（L320、L326–L328）：国产官方样品**仅 "for cause"** 采集；**不必常规采集国产样品支持 HACCP 违规的监管行动**（L327）；适用情形：疾病暴发、消费者/行业投诉跟进、取样任务（L327）；其余国产检查中取样应少见；控制明显不足时**不取样**，而在 483 说明控制缺失、EIR 描述条件（L327）；认为确需取样须**先联系 HFP**（L327）；Attachment A 给样品量/样品数（L328，另 L1195+）。
- **Imported Seafood Surveillance Sampling**（L318、L329–L337）：OII Workplan 规定每 Division 进口样品采集数（L330）；OII 自动监督系统标记加工商/产品，现场也可人工选择（L330）；**既往有安全缺陷的特定国外加工商/发货人的条目取样优先级最高**（L330）；审条目时参照 **Part II Table 1** 定风险与优先级、Hazards Guide 第 3 章定危害、**Attachment A** 定特殊取样指令（L334）；样品多数应取自高风险产品（L334）；送当年 OII Field Workplan 指定 servicing laboratory（L335）；被 import alert 扣留产品按 alert/bulletin/SCOPE 特殊指令（L336）；多分析项目先联系实验室确认样品量（L337）。
- **Documentary Samples**（L332、L338–L339）：如支持州际贸易的文件样品**只报 PAC 03842**；不得用 "H" 结尾的 HACCP 验证 PAC，也不计入 Division Workplan 义务（L339）。

### 步骤 5 · PART IV 实验室分析与 Criteria for Regulatory Action
- 分流（L347–L354）：A Filth/Mold/Foreign Objects、B Parasites、C Decomposition（Scombrotoxin/indole/organoleptic）、D Microbiological、E Natural Toxins、F Food and Color Additives、G Food Composition/Standards/Labeling & Fraud；化疗药归 CP 7304.018、化学污染物归 7304.004/7304.019（L353–L354）。
- 统一链路：METHODOLOGY（BAM / AOAC / LIB / CPG）→ REPORTING（FACTS + 进口 03844x / 国产 03842x 的 PAC + PAF/sub-PAF）→ **CRITERIA FOR REGULATORY ACTION**。
- 关键判据出口：
  - Filth：6 个 2–3 lb subs 的毛/昆虫/碎片水平（L382–L404）+ CPG Sec 555.600（L406、L1105）。
  - Parasites：BAM Ch.19 candling（L446）；**"fish in the round" 或 "dried fish" 中的寄生虫不考虑监管行动**（L447）；**RTE 带寄生虫危害产品活（主动活动）蠕虫零容忍**（L448）；报告 PAF "PAR"（L463）。
  - Decomposition / Scombrotoxin / Histamine：感官为主（合格分析师集体一致判定，L473），组胺按 subs 阈值触发 check analysis（L510–L526），判据 **CPG Sec. 540.525**（L543–L544、L1105）；Shrimp/Indole：判据 **CPG Sec. 540.370**（L588–L589）；其他产品分解：**CPG Sec. 540.370**（L609–L610）。
  - 微生物：Listeria 仅 RTE（L629、L650、L1215）、Salmonella BAM Ch5（L672）、Staphylococcus 肠毒素触发量（L701）、Vibrio 仅 RTE/涉病（L710）、`C. botulinum` 10 subs（L738）；生鲜软体贝类 **24 小时内**分析（L786、L1265）。
  - Natural Toxins：结果 PAF "BIO" + PAC 07842（国产）/07844（进口）（L872）；**超过 action level 立即通知 Division Compliance Branch；FDA action levels 在 Seafood HACCP Guide 第 6 章**（L873，另 L1125 CPG 540.250 PSP）。
  - Net Weight - Overglazing：**48 subs**（L942、L1234），AOAC 963.18（L943），判据 **CPG Sec 562.300**（L944–L945）。
  - Species Substitution：Table 3 Lab Classifications（Class 1 ≥98% RSSL / Class 3 <98%，L963–L965）；不混合取样、8 subs/lot（L951、L1239–L1240）。
  - Lab Class 3（Adverse Findings）后与货主往来的处理归 Division Compliance Branch（L466）；DWPE/reconditioning 样品量另见 Attachment A #3/#4（L1210）。

### 步骤 6 · PART V 执法策略
- **Table 4 违规分级**（L977、L987、L989–L1057）：按 Hazard Analysis / HACCP Plan / Corrective Actions / Verification / Records / Training / Sanitation / Imported Seafood 分组，逐条给 `Citation`（123.6(a)、123.6(b)(1)(2)、123.6(c)(1)–(7)、123.6(d)、123.7(a)(b)(d)、123.8(a)(1)–(3)/123.8(b)(c)(d)、123.9(a)(4)/(b)(1)/(c)、123.10(b)、123.11(b)(c)、123.12(a)(2)/(a)(2)(i)(ii)/(c)/(d)）与 `Ranking`（Major/Minor，L991–L1056）。**Significance must be determined on a case-by-case basis**（L1057）；Major = 若不纠正可能危及 HACCP 系统完整性/显著增加食品安全风险，Minor = 不太可能（L1059–L1060）；记录伪造归 Title 18 / OCI，不在本表分级（L1008）。
- 案例优先级：高风险潜在产品/工艺、OAI 复查或疾病事件优先；低监管优先危害或不与产品相关的危害优先级低（除非恶劣）（L984–L986）。402(a)(4) 可单独建议行动（L982）。
- **DWPE**（L1062、L1076–L1078）：国外加工商在国外检查或 HFP OCE 记录审查中发现的偏差未纠正时可被 DWPE；放行/移出 import alert 须 HFP OCE concurrence，申请人提供英文证据与监控记录（L1077）。Species misbranding 涉 foreign origin 的 Domestic-Import 样品可走 DIOP 的 DWPE 考虑（L1091–L1092）。
- **ADVISORY ACTIONS – WARNING LETTERS**（L1064、L1073–L1075）：对 123 重大偏差考虑 Warning Letter；模板见 Model Warning and Untitled Letters（L1075）。警告信不限于 123 违规（L1070）。
- **NMFS NOTIFICATION**（L1066、L1071–L1072）：依 FDA–NMFS MOU 与 FMD#-029，在涉及 NMFS 合同加工商的检查及后续监管行动后执行（L1072，另 L239–L240）。
- **JUDICIAL ACTIONS**（L1082–L1086）：seizure/injunction 建议须 HFP OCE 评估同意、FACTS 入案、CMS 电子提交（L1084）；含 Preliminary Assessment Calls、OII/HFP OCE/HFP OMFS/OCC 协作、RPM 第 6/10 章简化程序（L1085）；涉嫌刑事（伪造 HACCP 或卫生监控记录）须与 HFP OCE 及 OII OCI 讨论（L1086）。
- **SPECIES MISBRANDING**（L1080、L1087–L1092）：违反 FD&C Act 403(b) / 21 U.S.C. 343(b)（L1088）；监管建议经 MARCS-CMS 提交 Division of Enforcement（L1088，联系人 L1088）；Specimen charge 措辞（L1089–L1090）；非 123 违规（misbranding、EMA、非鲭毒分解等）总体见 L1068–L1070 与 CPG 清单 L1102–L1127。

### 步骤 7 · FIELD REPORTING REQUIREMENTS（L44–L115）
- 末尾出口，按结果类型分别落地：分析结果 → FACTS（PAF 对照 L52–L73）；OAI 且建议行动 → CMS 提交 EIR/483/endorsement（L90–L94）；支持扣留/DWPE 的样品 → CMS 提交标签、entry docs、发票/装箱单/提单、实验室工作表、Collection report（L95–L103）；HACCP 部分 → **FDA 3501（Processors）/ FDA 3502（Importers）** 每产品一份，进 National Seafood HACCP Inspection Database（L104–L107）；EMA → PAF FDL/FDF/FDE/FDQ/FDI（L74–L83）；misbranding/物种替代 → FDA 483 + Species Substitution Questionnaire（L114–L115）。

---

## 4. Table 1 / Table 2 / Table 4 / ATTACHMENT A：作用与不可误用处

| 表 | 定位 | 作用 | 不可误用处 |
|---|---|---|---|
| **Table 1** Product and Process Priority Ranking | L161 标题；表体 L163–L189；定义 L158–L159；目录逻辑页 8 区段 | 按产品/工艺危害与行业合规情况**降序**排列，用于"识别海产品 HACCP 检查的焦点"（L158–L159）；被 Table 2（L196）、Processor HACCP Evaluations（L275、L324）、Imported Surveillance Sampling（L334）、Foreign Establishment（L300）、PART V 案例优先级（L984）反复引用 | ① **非穷尽清单**（L159 "not all inclusive"），只覆盖 broad categories of market forms；② 表外产品/工艺须查 Hazards Guide 第 3 章识别物种/工艺相关危害（L159），不能拿表当危害清单；③ 产品跨多类别（如 ROP 鲭毒鱼）取**最高风险类别**（L159）；④ 它是**产品**优先级，不是企业/进口商优先级（后者 Table 2，L196）；⑤ 取样风险判定用 Table 1（L334）而非 Table 2；⑥ 表外的 Allergens / Natural marine toxins / Lower regulatory priority hazards 是补充口径（L187–L189），漏读会误判风险；⑦ 不能当法规限值表用 |
| **Table 2** Priorities for Establishment and Importer Inspections | L191 书签 / L200 伪标题；说明 L193–L199；表体 L201–L206 | **仅用于 work planning**（L196），按企业/进口商合规史降序排检查先后；Table 1 在每个 Row 内再按产品风险排序（L196） | ① 不是产品风险表、不是取样风险表（取样用 Table 1，L334）；② 进口商检查**数量由 OII workplan 定**，不由 Table 2 定（L197）；③ 90% / 10% 与 "100 entry line items" 是硬约束（L197、L204），不可忽略；④ 国外检查优先级可因国别问题/进口数据/新发问题变动（L196），不可机械套用国内顺序；⑤ OAI 复检须待企业整改完成（L199）；⑥ 低优先但为进入外国 Approved List 而主动申请检查者仍须尽快检查（L198） |
| **Table 4** Seafood HACCP Enforcement Strategy: Ranking of violation | L977 标题；L987 说明；表体 L989–L1057；定义 L1057–L1060 | 判定 Part 123 各缺陷的**重要性/分级**（Major/Minor），辅助优先排列海产品 HACCP 执法案例（L983、L987）；逐条给出 `Deficiency → Citation(123.x) → Ranking` 映射（L991–L1056） | ① 只是 **ranking 工具，不是自动执法结论**——"Significance must be determined on a case-by-case basis"（L1057）；② Major/Minor 定义针对"HACCP 系统完整性 / 食品安全风险"（L1059–L1060），**不是产品掺假或违规的数值判据**，别与第 5 节阈值混用；③ Citation 全部指向 **21 CFR 123.x**，不是 Part 117（L991–L1056）；④ 不覆盖非 HACCP 违规（misbranding / EMA / 非鲭毒分解 / 非安全 GMP 在 L1068–L1070）；⑤ 记录伪造归 Title 18 / OCI，不在表内分级（L1008）；⑥ 优先级还要叠加 PART V 的 L984–L986 规则 |
| **ATTACHMENT A** Sampling Information | L1193 标题；目录逻辑页 66（L138）；Table A-1 L1195–L1205；General Information 1–20 条 L1209–L1305；Table A-2 L1307–L1334 | **取样量 / 样品数 / 样品处理与运输**的操作指令：A-1 按产品形态给分解与微生物取样 subs 数（L1198–L1205）；#1–#20 为通用与专项（L1210–L1305）；A-2 按 6 个商品组给 Filth/Parasites/Decomposition/Micro/Natural Toxins 取样（L1310–L1334） | ① **Table A-1 样品量仅用于 surveillance 与 audit**（L1210 #3、L465），**不可作为 reconditioning（整批整改）验证成功的样品量**（L1210 #3 指向 Reconditioning by Segregation 指引）；② DWPE 放行/移出样品另有 Draft Guidance（L1210 #4），不能用 A-1 替代；③ **Domestic HACCP Verification Samples 采集前须先咨询 HFP**，且"不必要为支持 HACCP 违规而采国产样"（L1210 #5、L327）；④ 702(b) duplicate 部分**不含**在表列 subsample 数量内（L1210 #6）；⑤ Filth **仅 for cause** 采、且不采成品去支持 402(a)(4)，应采受污染原料与 filth exhibits（L1217 #11）；⑥ **CFP 只在疾病/暴发响应时采**（L1221 #14）；⑦ 多毒素须**分别取样**（L1328、L1333）；⑧ RTE 才做 Listeria（L1215 #9、L1198–L1205）；⑨ 它是"采多少/怎么采"，不是"何时采 / 是否采"（由 Part III Sampling L325–L339 + OII workplan 决定），也不是分析方法或判据（方法在 Part IV 的 BAM/AOAC，判据在 CPG / Guide 第 6 章）；⑩ ATTACHMENT A 不含"检查优先级"（那是 Table 1/2） |

---

## 5. 关键数字与阈值清单

> **统一声明：以下全部是 CP 7303.842 的「检查 / 取样 / 实验室分析 / 执法判定触发阈值与样品量」，不是法规限值（法规限值 / action levels 见 Seafood HACCP Guide 第 6 章 L873 及所引 CPG），也不是 BAM / AOAC 方法全文（本文只引用 BAM 章节号与 AOAC 方法号）。用于判定"何时追加分析 / 何时触发 check analysis / 采几个 subs / 是否上报"，不可当作产品合格-不合格的法定标准，也不可当作方法 SOP。**

### 组胺 / 鲭鱼毒素（Scombrotoxin，PART IV C，L488–L543）
| 数值 | 含义 | 行号 |
|---|---|---|
| **500 ppm** | 单个 subsample ≥500 ppm 即触发 check histamine analysis / 支撑监管行动；且初始 6 subs 中检出 ≥500 ppm 时**无需再分析剩余 subs** | L510、L515、L522、L526 |
| **50 ppm** | 两个 subs ≥50 ppm 触发 check analysis；或"1 个感官分解 sub + 另 1 个 ≥50 ppm" | L515、L522、L526 |
| **35 ppm** | 初始 6 subs 任一 ≥35 ppm 时须分析剩余 subsamples | L510 |
| 30–49（100 mm sensory scale） | mid-pass / borderline-pass 区间，须纳入组胺检测 | L510 |
| 40–49（100 mm sensory scale） | low-pass / borderline-pass 区间（虾/Indole 情形） | L569 |
| 18 / 24 / 18 subs | 感官检查最少 subs：Raw/Fresh/Frozen 18、Processed 24、≥1361 g(3 lb) 罐/袋金枪鱼（常规监督）18 | L498、L1200、L1205 |
| 100 g | 送组胺/Indole 检测的 pieces 最小量（不必测整个 subsample） | L503、L513、L538、L560、L571、L586 |
| 10 g / 10-gram aliquot | 组胺与 check analysis 的均质取样量 | L507、L515、L524、L526 |
| 250–500 g / 454 g | 全鱼横向切片、罐/杯/袋 subs 研磨量 | L528、L537、L540–L541 |
| 1361 g (3 lb) | 罐/袋金枪鱼容器阈值（≥则 18 subs） | L498、L1205 |
| 40 °F | 冷藏品温度超过 40 °F 须取感官+组胺样 | L1279 |
| — | 判据出口 **CPG Sec. 540.525**（截至实施日在修订中，若已修订按新版，否则联系 HFP） | L544、L1105 |
| — | 报告：organoleptic → PAF DEC + 03842C/03844C；组胺/Indole → PAF DEC + 03842A/03844A | L484、L14、L16 |

### 感官 / Indole（虾与其他分解，L534–L610）
| 数值 | 含义 | 行号 |
|---|---|---|
| **15 µg/100 g** | 初始 6 subs 任一 Indole ≥15 时须分析剩余 subs | L559、L572 |
| **25 µg/100 g** | ≥2 subs ≥25 触发 check indole analysis / 支撑监管行动 | L561、L573–L574、L582、L587 |
| 12 / 18 subs | 虾感官最少 subs：Raw 12、Processed 18 | L552、L1198–L1199 |
| 12 / 18 subs | 其他非鲭毒/非虾产品感官最少 subs | L603–L605 |
| unanimous decision | 合格分析师集体检查，须**全体一致**才能判某 subsample fail | L473 |
| NSSE (Level III) | 异常/非典型感官发现时由 National Seafood Sensory Expert 确认后再定 Lab Class | L479–L481 |
| — | 判据出口 **CPG Sec. 540.370**（虾与其他产品） | L589、L610、L1105 |

### 寄生虫（PART IV B，L443–L463）
| 数值 | 含义 | 行号 |
|---|---|---|
| **零容忍（live / actively moving worms）** | RTE 且带寄生虫危害的产品中活（主动活动）蠕虫无容许量 | L448 |
| 排除项 | "fish in the round" 或 "dried fish" 中发现的寄生虫不考虑监管行动 | L447 |
| ≥3 条完整虫体 | 送鉴定最少数量（每种）+ 全部头/尾碎片 | L451 |
| 15 subs / 200 g | A-2 中寄生虫取样量（For Cause，部分商品组） | L1312、L1316、L1333 |
| — | BAM Ch.19 candling（L446）；CPG 540.590 仅对列明淡水鱼种有 action levels，未列种 case-by-case | L446、L1126–L1127 |

### Filth（PART IV A，L368–L442）
| 数值 | 含义 | 行号 |
|---|---|---|
| 6 个 2–3 lb subs | 鲜/冻生虾 filth 监管行动建议的取样基数 | L382 |
| 平均 1 / 平均 4 | 鼠/小鼠毛（任意大小）均值 1；条纹非鼠毛均值 4 / sub | L384、L395 |
| 2 / 3 | 带病昆虫 2 只/样；同种其他昆虫 3 只/样 | L398–L400 |
| 5 片段 / 1 大体部件 | 带病昆虫碎片 5 片段（≥2/6 subs）；大体部件 1（≥2/6 subs） | L402–L404 |
| — | Disease Carrying Insects 定义 6 要素 + 蝇/蚁清单（CPG Sec 555.600） | L406–L442、L1105 |

### 净重 / 过镀冰（Overglazing，L929–L945、L1234）
| 数值 | 含义 | 行号 |
|---|---|---|
| **48 subsamples** | 冷冻镀冰海产品净重分析所需 subs 数 | L942、L1234 |
| AOAC 963.18 | Net Contents of Frozen Seafoods, Drained Weight Procedure | L943 |
| — | 判据出口 **CPG Sec 562.300 Foods - Net Weight**（另见 555.875） | L945、L1121 |
| 10–30 / 3–15 subs | Breading Standards 按包装规格的 subs 数 | L1236–L1238 |

### WPS / pH / aw / 亚硝酸盐（PART IV D Additional Analyses，L745–L784）
| 数值 | 含义 | 行号 |
|---|---|---|
| **pH < 4.6** | "Keep Refrigerated" 腌渍海产品：pH<4.6 分析结束 | L782 |
| **pH ≥ 4.6** | 须再查 Water Phase Salt，必要时查 nitrite（ppm） | L782 |
| **100 ppm（smoked fish）** | 微生物安全所需的亚硝酸盐充足水平（防肉毒神经毒素），10 个 subs 各自单独分析 | L770 |
| WPS 公式 | `% salt aqueous phase (WPS) = % salt × 100 / (% water + % salt)` | L764–L766 |
| 10 subs × 454 g | ROP/干制非 LACF/AF 产品的 aw/pH/WPS/nitrite 取样量 | L1312、L1316、L1324、L1333 |
| — | 方法：AOAC 952.08（水分）、937.09（盐）、973.31（亚硝酸盐）；CPG 540.200 / 540.500（亚硝酸盐过量） | L760、L763、L771、L770、L1110–L1111 |
| — | 报告：PAF MIC + sub-PAF **NAR**（aw/pH）、**WPS-NTR**（WPS/nitrite） | L784、L69–L71 |

### 微生物（PART IV D，L611–L795）
| 数值 | 含义 | 行号 |
|---|---|---|
| **≥10,000 CFU/gram E. coli** | 达到才做 ETEC 分析 | L634 |
| **1×10⁴ organisms/g (DPC) / 11,000 MPN** | 达到才做葡萄球菌肠毒素检测 | L701 |
| <100 (MPN) | MPN 设计检出 <100 的菌量，既不触发监管行动也不触发毒素分析，故不必与 DPC 同做 | L696 |
| 10 individual subs | `C. botulinum` 检查 10 个单独 subs；除非食物中毒/罐头腐败典型形态否则不测孢子/毒素 | L738、L740 |
| 2 composites × 250 g | Listeria 仅 composite basis：6 subs 取 83.3 g×3，或 10 subs 取 50 g×5 | L655–L659 |
| 25 g + 225 mL BLEB / 30 °C 48 h | Listeria 增菌条件（前 4 h 后加选择剂） | L660、L666 |
| 35 ±2 °C，6–8 h / 18–21 h | Vibrio APW 增菌与过夜再孵育 | L730–L732 |
| 24 hours | 生鲜软体贝类微生物样品须采集后 24 小时内分析 | L786、L1265 |
| RTE 30 subs×227 g（Listeria 10×114 g + Salmonella 30×114 g）；非 RTE 15 subs×114 g（仅 Salmonella） | Table A-1 微生物取样量 | L1198–L1205 |
| 200 g / 25 g / 100 g | 贝类均质、Vibrio / Listeria 分取、APC 用剩余匀浆 | L790–L795 |
| — | 仅 RTE 测 Listeria（L629、L650、L1215）、Vibrio（L710）；BAM 章节号 Ch1/2/4/5/9/10/12/13A/17/21A/24/28 被引用但方法全文不在本 CP | L617、L631–L634、L672、L715–L717、L739、L1215 |

### 天然毒素（PSP / DSP / ASP / NSP / AZP / CFP / TTX，PART IV E，L807–L873）
| 数值/项 | 含义 | 行号 |
|---|---|---|
| **PAC 07842 国产 / 07844 进口，PAF "BIO"** | 天然毒素报告码 | L20、L53、L872 |
| **action levels** | 超 action level 立即通知 Division Compliance Branch；**FDA action levels 在 Seafood HACCP Guide 第 6 章**（本 CP 不给具体数值） | L873 |
| PSP (saxitoxins) | AOAC 959.08（mouse bioassay，NSSP 接受）、2011.02、2005.06；NIST 标准 | L822–L826 |
| ASP (domoic acid) | AOAC 991.26（NSSP 接受）；提取一律用 AOAC 2006.02 | L836–L839 |
| DSP (Okadaic Acid / DTX1 / DTX2) | LC-MS/MS（NSSP approved for clams）；NRC 标准品 | L842–L846 |
| NSP (Brevetoxins) | APHA Mouse Bioassay（NSSP approved）；无 certified reference | L847–L848 |
| AZP (Azaspiracids) | EU-RL LC-MS/MS SOP v2；**无 NSSP 批准方法** | L849–L851、L859–L860 |
| CFP (Ciguatoxin) | tiered in vitro cytotoxicity + LC-MS/MS 验证中；无 certified reference；**仅疾病/暴发响应取样** | L861–L863、L1221 |
| TTX (Tetrodotoxin) | FDA HACCP 无控制建议；AOAC 959.08 mouse bioassay / NSSP RBA；Import Alert 16-20（河豚误标） | L855、L864–L870 |
| 3 subs × 227 g + 25 g viscera | A-2 中 ASP/PSP 取样量；CTX/TTX finfish subs 不混合 | L821、L1312、L1316、L1324、L1328、L1333 |
| 3 次分析 / subs | 软体贝类整体匀浆、蟹/龙虾肝胰腺分开、蟹煮 15 min | L814、L817–L818 |
| — | CPG 540.250（PSP） | L1125 |

### 物种替代 / 误标（Table 3、L960–L971、L1087–L1092）
| 数值 | 含义 | 行号 |
|---|---|---|
| **≥98% RSSL match（4 subs 全满足）** | Lab Class 1 In Compliance | L963 |
| **<98% RSSL（任一 single sub）** | Lab Class 3 Adverse findings | L965 |
| Class 2 / 4 / 5 | 监管行动未指示 / 无需分类 / 未分析或取消 | L964、L966–L967 |
| **8 subs / lot（4 容器×2），不混合取样** | 物种鉴定取样方案 | L951、L1239–L1240 |
| 1 lb | subsample >1 lb 时取 1 lb 部分 | L951、L1241 |
| — | 方法 AOAC 980.16（IEF）/ DNA barcode（J.AOAC 94(1) 201-210）；403(b) / 21 U.S.C. 343(b) 误标 | L948–L949、L1088–L1090 |
| — | 报告：PAC 21842 + PAF FDF + sub-PAF FDE | L937、L971 |

### 其他结构性数字
| 数值 | 含义 | 行号 |
|---|---|---|
| **5 inches** | 未去脏鱼 <5 in（含头尾）视为未去脏、≥5 in 须开腹检内脏；>5 in 加工鱼考虑 expedited regulatory action；IA 16-74 Red/Green List | L166、L638、L647、L1229–L1230、L637、L1227–L1231 |
| **90% / 10% / 100 lines** | 进口商检查资源分配规则 | L197、L204 |
| 66.5 oz | 金枪鱼亚硫酸盐取样：小罐 6 cans / 66.5 oz 罐 3 cans | L917、L1257 |
| every fourth year | DSS 每四年提交项目评估 | L1190 |
| 15 minutes boiling | 蟹样取组织前须煮沸 15 分钟 | L818 |

---

## 6. 建议 1 张能力卡

### 主题
**「CP 7303.842 海产品检查程序 · 整书导航与检查判定链」** —— 面向"拿到一份 FDA 海产品合规程序，如何按优先级 → 检查分流 → HACCP 评估 → 取样 → 实验室判据 → 执法分级 → 报告上报"一步步定位到正确小节与正确表格，并正确区分程序指令、法条义务、技术指南与方法全文。

### 覆盖边界（IN / OUT）
- **IN（本卡负责）**：仅这一份 CP 7303.842（Implementation 11/01/2023，Correction 09/30/2025，L6）的**程序性指令**：
  - 封面/前言：合并说明、PAC 码进口国产对照、三个日期、FIELD REPORTING REQUIREMENTS（L1–L115）；
  - 优先级工具：Table 1（L161–L189）、Table 2（L191–L206）及其使用规则（L158–L159、L196–L199）；
  - 检查分流：Processor / Importer / Vessels / Foreign Establishment / NSSP / EMA（L272–L324）；
  - HACCP Program Evaluations 与 483/EIR/FDA 3501·3502 口径（L274–L287、L104–L112）；
  - Sampling 三类（进口监督 / 国产 For Cause / Documentary，L325–L339）；
  - PART IV 的 A–G Project 分流、REPORTING（PAC/PAF）、CRITERIA FOR REGULATORY ACTION（引用 CPG 编号，L346–L971）；
  - PART V Table 4 分级、DWPE / Warning Letters / NMFS / 司法 / Species Misbranding（L975–L1127）；
  - ATTACHMENT A 取样量、General Information 20 条（L1193–L1334）；
  - 本文第 5 节全部"检查/执法判定阈值与样品量"。
- **OUT（不负责，须分流）**：
  - 21 CFR Part 123 各条的**法条义务原文、定义（123.3）、HACCP 计划法定要素** → CAP-22；
  - FSVP（21 CFR Part 1 Subpart L）进口商义务、FSVP 记录、VQIP、外国供应商验证程序 → CAP-21；
  - Fish and Fishery Products Hazards and Controls Guidance 的**物种-危害-控制技术细节**、Table 3-2/3-3/3-4、Chapter 3/4/6/13 内容、天然毒素 action level 具体数值 → CAP-23；
  - BAM / AOAC / LIB 的**方法全文与 SOP**、CPG 全文（本卡只引章节号/编号）；
  - 21 CFR Part 117 全文、Part 113/114、其他 CP（7303.070、7304.004/018/019、7318.004、7321.005/008 等）的实体要求。

### 与 CAP-21 / CAP-22 / CAP-23 的分流规则
| 来问的问题落在… | 转给 | 判据（本卡内锚点） |
|---|---|---|
| 传统海产品进口商验证：**21 CFR 123.12** 的 written verification procedures、affirmative steps、product specifications、HACCP 计划作为 affirmative step、MOU 国家产品排除、"for cause" 索取境外加工商 HACCP 文档 | 留在本卡 | L311–L324、L1052–L1056、L323（境外加工商计划缺陷不得上 483，转 HFP） |
| FSVP 进口商义务：Part 1 Subpart L、FSVP 记录、外国供应商验证、VQIP、进口商识别与豁免 | **CAP-21** | 本 CP 全文只出现 123.12，从未出现 FSVP / Part 1 Subpart L；且本卡明确保留"MOU 国家产品排除"（L311）与 123.12(d) "for cause"（L1056）这类**海产品专属口径**，FSVP 无对应，不能互相套用 |
| 需要逐条解释 123.6/123.7/123.8/123.9/123.10/123.11/123.12 的**法条义务、法律定义、HACCP 计划法定要素** | **CAP-22** | 本卡只给 Table 4 的 `Deficiency → Citation → Major/Minor` 映射（L991–L1056）与 case-by-case 提示（L1057），**不展开法条原文**（L143 仅给 eCFR 链接） |
| 某鱼种/工艺有哪些危害、CCP/CL 怎么设、Table 3-2/3-3/3-4 内容、PSP/DSP/ASP action level 具体数值、Chapter 3/4/6/13 技术细节 | **CAP-23** | 本卡在多处**只做指向**：Hazards Guide 第 3 章（L159、L334、L495、L939、L1210 #2、L1312）、第 4/6 章（L171、L873、L1126）、第 13 章（L165、L170）；且明确 "FDA established action levels for natural toxins can be found in Chapter 6 of the Seafood HACCP Guide"（L873）——本 CP 不给数值 |
| 检查/取样/执法判定链的"下一步去哪一节"、PAC/PAF 怎么报、Table 1/2/4/A 怎么选 | 留在本卡 | 本文第 3、4 节 |

### 最易误读的三处口径
1. **PAC 体系：合并了程序 ≠ 合并了码，且 "H" 后缀在两处语义不同。** CP 7303.844 已并入 7303.842，但 PAC 仍分进口/国产（L7、L142）；取样/分析用 `03844x / 03842x`（L12–L25），而检查报告用 `03842 / 03842H / 03844H / 03040`（L26–L33）；其中 **03842H 在 L18 是 "HACCP Verification (i.e., verification of adequacy of HACCP plan critical limits)"、进口列 Not applicable，在 L31 却是 "Processor HACCP Inspection" 报告 PAC**——同名不同义。更硬的坑：**Documentary samples 只能用 03842，绝不能用 "H" 结尾 PAC，也不计入 workplan 义务**（L339）；03842H 与 03844H 分别是 Processor / Importer HACCP Inspection，别与取样 PAC 混报（L30–L32）。
2. **阈值性质：把 CP 的"判定触发值/样品量"当成法规限值或 BAM 方法全文。** 组胺 500/50/35 ppm（L510–L526）、Indole 15/25 µg/100g（L559–L587）、pH 4.6（L782）、熏鱼亚硝酸盐 100 ppm（L770）、RSSL 98%（L963–L965）、活虫零容忍（L448）、5 inches（L638、L647）、48 subs（L942）、30/15/18/24 subs（L498、L1198–L1205）全部是**检查/取样/追加分析/上报触发口径**；法规限值/action levels 在 Seafood HACCP Guide 第 6 章与 CPG（L873、L1102–L1127），BAM/AOAC 只以章节号/方法号被引用（L617、L446、L470–L472、L823–L850），本 CP 不含方法全文；且 PART IV 多处明说这些 subs 数"仅适用于 surveillance and audit samples"（L465、L546、L565、L508、L1210 #3），reconditioning / audit / 疾病调查各有不同规则（L465、L508、L519、L525）。
3. **Table 1/2/4 与 ATTACHMENT A 的适用域被扩大或串用。** Table 1 是产品/工艺风险、**非穷尽**、用来"选产品与定检查焦点"（L158–L159），Table 2 **只用于 work planning**（L196）且数量受 OII workplan 与 90/10 规则约束（L197），取样风险判断用 Table 1 而非 Table 2（L334）；国产样品**仅 "for cause"、不常规取样支持 HACCP 违规**（L327、L1210 #5），进口监督取样由 OII workplan 定数量（L330）；ATTACHMENT A / Table A-1 的样品量**仅 surveillance & audit**，不能用作 reconditioning 验证（L1210 #3）、DWPE 放行（#4）、Domestic HACCP Verification（#5 须先咨询 HFP）；Table 4 是 **ranking 而非自动执法结论**（L1057 case-by-case、L1059–L1060 定义），且只覆盖 21 CFR 123 缺陷，非 123 违规在 L1068–L1070。另配套易错：三个日期口径不一（封面 L6 Implementation 11/01/2023 + Correction 09/30/2025、封面 L8 "Date of Issuance: 09/30/025" 疑 OCR 残缺、正文页脚一律 11/1/2023，L1182 等），引用 issuance 日期时须注明取自哪一处。

---

*本文件为「整书理解」中间产物，仅依据 `cp-7303-842-full.md` 与 `convert-report.json` 两份只读输入撰写；所有结论以 `Lxxx` 标注行号，物理页数因输入未含 page 字段而明确标注为不可直接读取。*
