#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_v4_11_card.py — 生成 CAP-24 能力卡。

R 段 36 个英文引用块从 candidates/v4-11-quotes.md 解析注入（零手工转录），
其余 I/A1/A2/E/B 段由本脚本模板提供。引用出处按 Q 编号映射 CP 7303.842 部/节号。
"""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
QUOTES = BASE / ".cangjie/candidates/v4-11-quotes.md"
OUT = BASE / ".cangjie/capabilities/cards/seafood-inspection-program.md"

LOC = {
    1: "FIELD REPORTING REQUIREMENTS / EMA", 2: "FIELD REPORTING REQUIREMENTS / Samples Supporting Regulatory Action",
    3: "PART I", 4: "PART I", 5: "PART II / Program Management Instructions",
    6: "PART II / Table 1", 7: "PART II / Table 2", 8: "PART III.C / Processor Inspections",
    9: "PART III.C / HACCP Program Evaluations", 10: "PART III.C / HACCP Program Evaluations",
    11: "PART III.C / Vessels", 12: "PART III.C / Foreign Establishments",
    13: "PART III.E / NSSP", 14: "PART III.D / Importer Inspections",
    15: "PART III.F / Domestic For Cause Sampling", 16: "PART III.F / Imported Surveillance Sampling",
    17: "PART III.F / Documentary Samples", 18: "PART IV.A / Filth",
    19: "PART IV.B / Parasites", 20: "PART IV.C / Reporting",
    21: "PART IV.C / Organoleptic", 22: "PART IV / ATTACHMENT A #16 / Import Alert 16-74",
    23: "PART IV.D / Clostridium", 24: "PART IV.D / Additional Analyses",
    25: "PART IV.E / Natural Toxins", 26: "PART IV.G / PAC",
    27: "PART IV.G / Net Weight", 28: "PART V / Table 4",
    29: "PART V / NMFS Notification", 30: "PART V / Warning Letters",
    31: "PART V / DWPE", 32: "PART V / Judicial Actions",
    33: "PART V / Species Misbranding", 34: "PART V / Regulatory Guidance – Sources",
    35: "PART VII / Program Evaluation", 36: "ATTACHMENT A / General Information",
}
GROUPS = [
    (1, 4, "① 程序范围、合并与报告出口"),
    (5, 7, "② 检查优先级：Table 1 与 Table 2"),
    (8, 17, "③ 检查类型分流与 Sampling 三类"),
    (18, 27, "④ PART IV 实验室分析、判据与 PAC"),
    (28, 34, "⑤ PART V 执法策略与裁量"),
    (35, 36, "⑥ 项目评估与 ATTACHMENT A"),
]

raw = QUOTES.read_text(encoding="utf-8")
found = re.findall(r'### Q-(\d+)\s+([^\n]+)\n> "(.+)"\n> —— L(\d+)', raw)
assert len(found) == 36, f"期望 36 段引用，实得 {len(found)}"
by_id = {int(n): (topic.strip(), quote, int(line)) for n, topic, quote, line in found}
assert sorted(by_id) == list(range(1, 37)), "Q 编号不连续"

r_parts = ["## R — 原文（36 个英文逐字引用块，均取自正文区散文段落）\n"]
for lo, hi, title in GROUPS:
    r_parts.append(f"\n**{title}（逐字）**：\n")
    for i in range(lo, hi + 1):
        topic, quote, line = by_id[i]
        r_parts.append(f'\n> "{quote}"\n> —— CP 7303.842 {LOC[i]} / L{line}\n')
r_section = "\n".join(r_parts)

TEMPLATE = r"""# 海产品检查程序层：CP 7303.842 整书导航与检查判定链（seafood-inspection-program）

*来源分层：本卡（CAP-24）取用**第 16 类来源**——FDA《Compliance Program Guidance Manual 7303.842: Seafood Processor, Products, and Importer Inspection Program》，**2023-11-01 版程序的 2025-09-30 更正本**（本地 `source-cp-7303-842-2023.md`，80 物理页 / 148 书签 / 转换正文 179,812 字节）。它是 FDA 给**检查员、进口分区、分部合规官与实验室**的内部作业指导（PART I 明写 `provides instruction to field staff`）：负责「检查怎么排、怎么分流、怎么评价 HACCP、怎么取样、怎么报、怎么建议执法」。**不是法规、不是 Guidance for Industry、不创设企业义务**；企业义务仍须回指 21 CFR Part 123〔§ 123.xxx〕与 Part 117 Subparts A/B/F。*

*三层配对而非合并：**CAP-22** `seafood-haccp-statutory-requirements` 是**法条义务层**（Part 123，`shall`，违反即法规不符合）；**CAP-23** `seafood-hazards-controls-guide` 是**技术指南层**（`should`，18 步危害分析判定链、Ch.3 三表、CCP 与关键限值）；**本卡**是**检查程序层**（给 field staff 的作业指令、Table 1/2/4、PAC/PAF、取样与执法建议）。必须同时防三个方向的误读：① 把 CP 的检查动作、优先级表、实验室触发值写成企业法定义务或产品放行标准；② 把 Table 4 的 Major/Minor 违规分级当成〔§ 123.6〕的 significant hazard 判定或自动执法结论；③ 反过来因「CP 非强制」就把 Part 123 的 `shall` 义务稀释成可选。CP 原文 L276 自己就写着 `the requirements for subparts C and G of part 117 cannot replace the requirements defined in part 123`。*

*全包自 v4.11 起「**十六类来源不可混引**」。本卡引用一律写「CP 7303.842 PART x / Table x / ATTACHMENT A #x / Lxxx」（L 号为转换产物正文区相对行号，仅作定位辅助，**逐字引证以原文字符串为准、不以行号为准**），法条一律写〔§ 123.xxx〕〔§ 117.xxx〕，指南写「Seafood Hazards Guide 第 4 版 Ch.x」，其它 CP 各自用其 PART 号。层次为：法规正文 ＞ FDA 指南 ＞ CPGM／CP／IOM 检查程序（仅检查员视角）。首页 NOTE 明确 **CP 7303.842 与 CP 7303.844 已合并为单一程序**，但 `PAC codes for sampling and analysis will still reflect whether the product is imported or domestic`——合并的是程序，不是码表。*

*正文本包**仍未收**：CPG Sec. 540.525 / 540.370 / 555.600 / 562.300 / 540.250 / 540.590 全文、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、NSSP Guide 与 Model Ordinance、BAM / AOAC / LIB / MPM 方法全文、Import Alert 16-74 / 16-20 / 99-41 全文、21 CFR part 1 subpart L（FSVP 法规）、IOM Chapter 4、FDA 3501 / 3502 表单全文、Seafood List、eNSpect / CMS / FACTS / MARCS-CMS 内部系统、FDA–NMFS MOU / FMD#-029。涉及其具体数值、条文原文、方法 SOP 与条款级结论一律标「转引未收」，不得从本 CP 反推。本卡与 `seafood-haccp-statutory-requirements`、`seafood-hazards-controls-guide`、`inspection-sampling`、`fsvp-inspection-program`、`lacf-inspection-program`、`inspection-readiness`、`investigator-authority-procedure`、`chemical-hazard-controls`、`defect-action-levels` 双向辅读，见 B12。*

__R_SECTION__

## I — 自述

我是「拿到一份海产品 FDA 合规程序，能定位到正确小节、并沿完整检查判定链给出下一步」的能力。输入可以是「某产品/工艺该排第几优先」「这次检查查加工商还是进口商」「要不要取样、报哪个 PAC」「某个实验室结果意味着什么」「这种情况会不会直接警告信」这类问题；输出必须同时给出：① 当前落在 **PART I–VII / FIELD REPORTING REQUIREMENTS / ATTACHMENT A** 的哪一段；② 判定链的**上一步与下一步**；③ 这一结论属于**法条义务层 / 技术指南层 / 检查程序作业层 / 外部法源转引未收层**中的哪一层；④ 需要分流到 CAP-22、CAP-23 还是其它卡。我不写企业合规结论、不代填 FDA 3501/3502、不预测检查结果、不把阈值写成放行标准。

## A1 — 书中案例

1. **Table 1 与 Table 2 被对调**：有人拿 Table 2 去判断「生食软体贝类比熟制 RTE 风险高」。正确：Table 1 才是产品/工艺风险降序表（L158–L189），Table 2 **仅用于 work planning**、按企业/进口商合规史排序（L196）；取样风险判定也用 Table 1（L334）。且 `Table 1 is not all inclusive`，表外产品须查 Hazards Guide 第 3 章。
2. **7303.844 被当成现行独立程序**：封面 NOTE 与 PART I 均写明两程序已合并为单一 CP 7303.842（L7、L142）；但 PAC 仍分进口 `03844x` 与国产 `03842x`（L12–L25）。「程序合并」不等于「码表统一」。
3. **组胺 500 / 50 / 35 ppm 被写成法定限量**：L510–L526 给的是初始 6 subs 的追加分析/check analysis 触发规则，判据出口是 CPG Sec. 540.525（L544，本包未收）；这些数字是**检查员作业口径**，不是法规限值、不是产品放行标准，更不能与 CAP-23 的 50 ppm 分解指示 / 500 ppm 毒性水平混为一谈。
4. **FSVP「不取样」被反套到海产品进口商检查**：CP 7303.878 明写 `Samples will not be collected as part of an FSVP inspection`、PART IV 全空；本 CP 的进口商 HACCP 检查依〔§ 123.12〕，且有 Imported Seafood Surveillance Sampling（L329–L337）与 `03844H` 报告 PAC。两套法源、两套动作。
5. **`03842H` 同名不同义**：L18 它是 `HACCP Verification (i.e., verification of adequacy of HACCP plan critical limits)` 且进口列 `Not applicable`；L31 它是 `Processor HACCP Inspection` 的报告 PAC。更硬的坑：documentary samples **只报 03842**，不得用以 `H` 结尾的 PAC，也不计入 Division Workplan 义务（L339）。
6. **Table 4 被当成自动执法结论或 §123.6 显著性判定**：Table 4 逐条给 `Deficiency → Citation(123.x) → Major/Minor`（L989–L1056），但原文 `Significance must be determined on a case-by-case basis`（L1057）；Major/Minor 针对 HACCP 系统完整性与食品安全风险，不是危害分析里的 `reasonably likely to occur`。记录伪造归 Title 18 / OCI（L1008）。
7. **物种替换被当成 HACCP 危害**：物种替代在 PART V 的定性是 **FD&C Act 403(b) / 21 U.S.C. 343(b) misbranding**（L1088–L1090），监管建议经 MARCS-CMS；但它可能**引入**额外安全危害（海洋毒素、过敏原、鲭毒，L297），此时才转 CAP-23 做危害分析。法律定性与危害判定是两件事。
8. **ATTACHMENT A 的 subs 数被用于 reconditioning 验证**：Table A-1 的样品量多处明说 `only for surveillance and audit samples`（L465、L546、L565、L1210 #3），reconditioning（#3）、DWPE 放行（#4）、Domestic HACCP Verification（#5 须先咨询 HFP）各有不同规则；702(b) duplicate 部分不含在表列 subs 内（#6）。
9. **文件名当版本**：`20250929` 是 PDF 生成日，封面 `Date of Issuance: 09/30/025` 是文本层残缺形态，真正的口径是 IMPLEMENTATION DATE `11/01/2023` + Correction date `09/30/2025`（L6、L8），正文页脚一律 `11/1/2023`。与 CP 7303.050 / 7303.070 / 7303.878 同属「旧程序 + 更正本」，不同于 CPGM 7303.040 的 `2025-CPM-HFP-001`。
10. **pH 4.6 与 7303.070 的 4.40 / 4.65 混用**：本 CP 的 pH <4.6 是「Keep Refrigerated」腌渍海产品追加分析的**结束条件**（L782，≥4.6 再查 WPS 与 nitrite）；CP 7303.070 的 4.40 / 4.65 是 LACF/AF 实验室双分析师触发线，Part 113/114 的 4.6 是法定边界。三套数字、三套用途。

## A2 — 未来触发

- 复述 CP 7303.842 的完整检查判定链（Table 1/2 → 检查分流 → HACCP 评价 → 取样 → PART IV → PART V → 报告）
- 说明 CP 7303.842 与 CP 7303.844 的合并关系及 PAC 码仍分进口/国产
- 判定某产品/工艺在 Table 1 的风险位置并处理表外产品
- 判断产品跨 Table 1 多个类别时取哪一类
- 用 Table 2 排检查先后并说明 90% / 10% 与 100 entry line items 规则
- 区分 Table 1 与 Table 2 的适用域并指出取样风险用哪张表
- 分流 Processor / Importer / Vessels / Foreign Establishment / NSSP / EMA 六类检查
- 说明加工检查同时适用多个 compliance program 时的处理方式
- 说明 HACCP Program Evaluations 须聚焦最高风险产品且在生产时进行
- 说明未在生产时的替代取证与 OAI/VAI 复检规则
- 解释 Part 117 subparts C/G 不能替代 Part 123 义务
- 区分 significant observations 与自愿纠正项、483 与 EIR 的列示顺序
- 判断国产官方样品何时可采并说明「for cause only」
- 判断进口监督取样由谁定数量、哪些条目优先
- 处理 documentary samples 的 PAC 与 workplan 归属
- 分辨取样/分析 PAC 与检查报告 PAC 两套码表
- 解释 `03842H` 在两处同名不同义
- 说明 HACCP Verification PAC 进口列 `Not applicable` 的含义
- 按 PART IV A–G Project 分流实验室分析并给出判据出口编号
- 判断组胺 500 / 50 / 35 ppm 各自触发什么动作
- 判断 Indole 15 / 25 µg/100 g 与感官 unanimous decision 的角色
- 说明 RTE 活虫零容忍与 fish in the round / dried fish 排除项
- 说明 pH <4.6 / ≥4.6 在腌渍海产品追加分析中的作用
- 说明天然毒素超限后的通知路径与 action level 出处
- 说明净重过镀冰 48 subs 与 AOAC 963.18、CPG 562.300 的关系
- 解释物种鉴定 Table 3 的 Lab Class 1/3 与 8 subs/lot
- 判断某个 CP 阈值能否写成法规限值、放行标准或 BAM 方法
- 用 Table 4 定位 `Deficiency → Citation → Ranking` 并说明 case-by-case
- 说明 NAI/VAI/OAI、Warning Letters、DWPE、judicial actions 的裁量与 Center concurrence
- 区分 Import Alert 16-74 / 16-20 与 99-41 / 99-37 / 99-38
- 说明物种误标 403(b) 的法律定性与额外危害的转介
- 定位 FIELD REPORTING REQUIREMENTS 各结果类型的上报出口（FACTS / CMS / FDA 3501·3502）
- 判断 ATTACHMENT A 样品量能否用于 reconditioning / DWPE 放行
- 说明 702(b) duplicate、Filth for cause、CFP 疾病响应、RTE Listeria 的取样限制
- 标注某结论属于法条义务层 / 指南建议层 / 检查程序层 / 转引未收层
- 分流条款级判定至 CAP-22、危害判定至 CAP-23、FSVP 至 CAP-21、通用取样至 CAP-17
- 纠正把 CP 检查动作写成企业法定义务的误读
- 纠正把 CP 优先级表或违规分级当合规清单的误读
- 拒绝代填表单、拒绝预测检查结果、拒绝出法律结论

## E — 执行要点

**Step 1 · 先分效力层，再谈内容。** 收到问题先判：问「企业有没有义务、条款号、法定时限、是否违法」→ CAP-22〔§ 123.xxx〕；问「某鱼种/工艺有哪些危害、Ch.3 表、CCP、关键限值」→ CAP-23；问「FSVP / part 1 subpart L」→ CAP-21；问「通用取样量与环境拭子」→ CAP-17；只有问「检查怎么排、查哪类对象、取样/上报/执法建议」才留在本卡。凡输出必须标注效力层标签。

**Step 2 · 锁定版本与范围。** 本件是 **2023-11-01 版 / 2025-09-30 更正**，文件名 `20250929` 只是生成日；PART I–VII + 目录前的 FIELD REPORTING REQUIREMENTS + ATTACHMENT A；CP 7303.844 已并入。引用写「CP 7303.842（2023 版 / 2025-09-30 更正）」，不得写「2025 版 7303.842」。

**Step 3 · 检查优先级（PART II）。** Table 1 选**产品/工艺**风险（降序、非穷尽、跨类取最高、表外查 Hazards Guide Ch.3）→ Table 2 按**企业/进口商合规史**做 work planning（90% / 10%、<100 entry line items、OAI 复检待整改）→ 取样风险再用 Table 1。

**Step 4 · 检查类型分流（PART III）。** 六类：Processor（多程序分别覆盖、时间有限优先 03842H）／Importer（〔§ 123.12〕、Table 2 选人 + Table 1 选产品、MOU 国家产品排除、境外计划缺陷不得上 483 而转 HFP、每产品一份 FD 3502）／Vessels（靠港非作业）／Foreign Establishments（产品风险 + 合规史、只覆盖输美产品）／NSSP（standardized inspector、ISSC Form 93-01(A)）／EMA（一般监督须 HFP concurrence）。

**Step 5 · HACCP Program Evaluations（PART III.C）。** 聚焦最高风险产品 + 已知在生产；walk-through、访谈、观察、记录审查；Part 117 C/G 不替代 Part 123；significant observations 与自愿纠正项分开；483 与叙述性 EIR 按监管重要性降序；未在生产时的替代取证与复检规则。

**Step 6 · Sampling（PART III.F）与 PAC/PAF。** 三类：国产 `for cause only`（不常规取样支持 HACCP 违规、控制明显不足时不取样而在 483 说明、确需取样先联系 HFP）／进口监督（OII Workplan 定数量、既往缺陷条目优先、多数取自高风险产品）／documentary（只报 03842、不用 H 结尾 PAC、不计入 workplan）。分析 PAC 进口 03844x / 国产 03842x；报告 PAC 03842 / 03842H / 03844H / 03040。

**Step 7 · PART IV 实验室分流与阈值性质。** A Filth / B Parasites / C Decomposition / D Microbiological / E Natural Toxins / F Food & Color Additives / G Composition·Labeling·Fraud；统一链路 METHODOLOGY → REPORTING（FACTS + PAC + PAF）→ **CRITERIA FOR REGULATORY ACTION**（出口为 CPG 编号或 Hazards Guide 第 6 章，本包未收）。所有数字只作触发/样品量，输出时必附「不是法规限值、不是放行标准、不是方法全文」声明。

**Step 8 · PART V 执法策略与 FIELD REPORTING 收口。** Table 4 的 `Deficiency → Citation(123.x) → Major/Minor` 只作 ranking，原文 `case-by-case`；WL `should be considered`、DWPE 与 judicial actions 须 HFP OCE concurrence / CMS；NMFS 依 MOU；Species misbranding 是 403(b) 误标。最后按结果类型落到 FACTS / CMS / FDA 3501（Processors）·3502（Importers）/ FDA 483 / Species Substitution Questionnaire，并写明「FIELD REPORTING REQUIREMENTS 物理上位于目录之前、不在 PART I–VII 内」。

**完整判定链一览：**

| 环节 | 定位 | 产出 | 常见误用 |
|---|---|---|---|
| 产品/工艺风险 | PART II Table 1（L161–L189） | 检查焦点与取样风险 | 当危害清单、当穷尽表 |
| 企业/进口商优先级 | PART II Table 2（L191–L206） | work planning 顺序 | 当产品风险表、当检查数量依据 |
| 检查类型分流 | PART III.C/D/E（L272–L324） | 六类检查动作 | 把 FSVP 不取样套过来 |
| HACCP 评价 | PART III.C（L274–L287） | 483 / EIR / 3501·3502 | 用 Part 117 C/G 替代 123 |
| 取样 | PART III.F（L325–L339） | 三类取样与 PAC | 常规采国产样、混用 H 码 |
| 实验室与判据 | PART IV（L346–L971） | A–G 分流 + CPG 出口编号 | 把触发值当法定限值 |
| 执法分级 | PART V Table 4（L989–L1060） | Major/Minor + case-by-case | 当自动执法结论 |
| 报告上报 | FIELD REPORTING（L44–L115） | FACTS / CMS / 3501·3502 | 漏报或错归 PART |
| 取样量细则 | ATTACHMENT A（L1193–L1334） | subs 数与处理运输 | 用于 reconditioning / DWPE 放行 |

**输出格式要求**：每条结论写「CP 7303.842 PART x / Table x / Lxxx」定位 + 效力层标签；法条另写〔§ 123.xxx〕并转 CAP-22；指南另写「Seafood Hazards Guide 第 4 版 Ch.x」并转 CAP-23；未收正文一律标「转引未收」并说明为什么不展开。

## B — 边界

**B1 — CP 不是企业义务清单。** 本件是给 field staff 的内部作业指导，不创设义务；合规结论必须回〔§ 123.xxx〕〔§ 117.xxx〕。CP 的 `should` / `consult` / `should be considered` 都不能改写成 `must`。反向也要防：不能因 CP 非强制就把 Part 123 的 `shall`（危害分析、书面 HACCP 计划、纠正措施、验证、记录、培训、卫生、进口商验证）说成可选。

**B2 — PART IV 全部数字是检查员作业口径。** 组胺 500/50/35 ppm、Indole 15/25 µg/100g、感官 subs 18/24/12、活虫零容忍、pH 4.6、熏鱼 nitrite 100 ppm、RSSL 98%、48 subs、6 个 2–3 lb subs、5 inches——都是追加分析、取样量、上报或触发条件，不是法规限值、不是产品放行标准、不是 BAM/AOAC 方法 SOP。判据出口（CPG 540.525 / 540.370 / 562.300 / 555.600 / 540.250、Hazards Guide 第 6 章）本包未收，一律标「转引未收」。

**B3 — PAC 体系：程序合并 ≠ 码表合并，且 `H` 后缀两处语义不同。** 取样/分析 `03844x`（进口）与 `03842x`（国产）；检查报告另有 03842 / 03842H / 03844H / 03040；`03842H` 在 L18 是 HACCP Verification（进口列 Not applicable）、在 L31 是 Processor HACCP Inspection。Documentary samples 只报 03842，不得用 H 结尾 PAC、不计入 workplan（L339）。

**B4 — Table 1 / Table 2 / Table 4 / ATTACHMENT A 适用域不可扩大。** Table 1 产品风险、非穷尽、跨类取最高；Table 2 只做 work planning 且数量由 OII workplan 与 90/10 规则定；Table 4 只给 Part 123 缺陷的 ranking、case-by-case、不覆盖非 123 违规、不含记录伪造；ATTACHMENT A 只给 surveillance/audit 的样品量与处理，不能用作 reconditioning、DWPE 放行或 Domestic HACCP Verification 的取样量。

**B5 — 7303.844 已合并；〔§ 123.12〕与 FSVP 是双轨。** 首页 NOTE 与 PART I 写明合并；进口商 HACCP 检查依〔§ 123.12〕（written verification procedures、affirmative steps、product specifications、MOU 国家产品排除、for cause 索取境外 HACCP 文档），与 FSVP（FD&C Act §805 / 21 CFR part 1 subpart L）不是同一套；CP 7303.878 的不取样 / PART IV 空白不得反套。

**B6 — 版本口径：2023 版 / 2025-09-30 更正。** 文件名 `20250929` 是生成日；封面 `Date of Issuance: 09/30/025` 为文本层残缺；IMPLEMENTATION DATE 11/01/2023、Correction date 09/30/2025、正文页脚 11/1/2023。与 7303.050 / 7303.070 / 7303.878 同形态，不同于 CPGM 7303.040 的 `2025-CPM-HFP-001`。引用 issuance 日期须说明取自哪一处。

**B7 — 检查分流各有专门限制。** Vessels 通常靠港非作业检查；Foreign Establishments 选点看产品风险 + 合规史、只覆盖输美产品、须取文档与照片证据；NSSP 须 shellfish standardized inspector / officer 并用 ISSC Form 93-01(A)；EMA 一般监督须先得 HFP concurrence；境外加工商 HACCP 计划的其他缺陷不得写进 483，须取副本转 HFP。

**B8 — Sampling 三类与「不取样」同样是结论。** 国产仅 for cause，且控制明显不足时**不取样**、在 483 说明控制缺失、EIR 描述条件；确需取样先联系 HFP。进口监督取样数量由 OII Workplan 定、既往安全缺陷条目优先。Documentary samples 见 B3。ATTACHMENT A 的 702(b) duplicate、Filth for cause、CFP 仅疾病响应、RTE 才做 Listeria 都是硬限制。

**B9 — 执法动作须裁量与 Center 一致。** Warning Letters `should be considered`；DWPE 放行/移出须 HFP OCE concurrence 与英文证据；judicial actions 须 HFP OCE 评估同意、FACTS 入案、CMS 电子提交；NMFS 通知依 MOU / FMD#-029；非 123 违规（misbranding / EMA / 非鲭毒分解 / 非安全 GMP）走 L1068–L1070 的 Compliance Intake and Consultation Form。不得写成「达到某值自动发警告信 / 自动扣留」。

**B10 — 物种替换的法律定性与危害判定分开。** PART V 定性为 FD&C Act 403(b) / 21 U.S.C. 343(b) misbranding，监管建议经 MARCS-CMS；PART IV.G 给 Table 3 Lab Classifications（≥98% RSSL Class 1 / <98% Class 3）与 8 subs/lot 不混合取样；物种替换可能**引入**海洋毒素、过敏原、鲭毒等额外安全危害，此时转 CAP-23，但不得把误标本身写成 HACCP 危害或 CCP。

**B11 — 转换质量红线与十六类不可混引引用规范。** 转换件存在书签 `##/###/####` 与正文 `# **…**` 伪标题并存导致的标题交错（PART II/III/IV/V 各出现两次、H1 统计虚高 133）、`<u>…</u>` 与 `<br>` 标签、表格列头连写、页码混入单元格、`09/30/025` 与 `021842` 转录残缺。**检索与引用一律以 PART 号 / 小节号 / 表号为准，不以 Markdown `#` 层级为准**；逐字引用只取散文段落，每段 ≤100 词，需剥离 Markdown 标记后核对；表格单元、页眉页脚、纯数字行不得作逐字引用。全包自 v4.11 起**十六类来源不可混引**：本件写「CP 7303.842 PART x / Table x / ATTACHMENT A #x / Lxxx」，法条写〔§ 123.xxx〕〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕，指南写「Seafood Hazards Guide 第 4 版 Ch.x」，PCHF 指南用 Ch/小节号，L.mono 用其章节号，SECG 用 SECG 章号，Ed.5 用问答编号，Handbook 用「Handbook 章名 + 产品名」，CPGM 7303.040 / CP 7303.050 / CP 7303.070 / CP 7303.878 各用其 PART x，IOM 用「IOM 5.x.x / Exhibit 5-x」。

**B12 — 与其它卡的分工、不代写、仍未收清单。** 本卡＝第 16 类来源的**检查程序层／整书导航与检查判定链**。问「法条义务、条款级判定、法定时限、是否违法」→ CAP-22 `seafood-haccp-statutory-requirements`；问「Ch.3 三表、reasonably likely to occur、CCP / 关键限值、危害技术细节」→ CAP-23 `seafood-hazards-controls-guide`；问「FSVP 与 part 1 subpart L」→ `fsvp-inspection-program`；问「CP 7303.050 的通用取样量与环境拭子」→ `inspection-sampling`；问「LACF/AF 与 Import Alert 99-37/99-38」→ `lacf-inspection-program` / `lacf-statutory-requirements`；问「PCHF 迎检、483 措辞与证据固定」→ `inspection-readiness` / `investigator-authority-procedure`；问「组胺/化学危害限值出处与缺陷行动水平效力层」→ `chemical-hazard-controls` / `defect-action-levels`。**本卡不代填 FDA 3501/3502、不代写 483 回复或警告信答复、不预测检查分类、不判法定身份、不承诺合规、不出法律结论**。仍未收：CPG 540.525 / 540.370 / 555.600 / 562.300 / 540.250 / 540.590 全文、21 CFR part 120 / 1240 / 108 / 110 / 507、NSSP Guide / Model Ordinance、BAM / AOAC / LIB / MPM 方法全文、Import Alert 16-74 / 16-20 / 99-41 全文、21 CFR part 1 subpart L、IOM Chapter 4、FDA 3501/3502 表单全文、Seafood List、eNSpect / CMS / FACTS 内部系统、FDA–NMFS MOU —— 一律标「转引未收」。
"""

card = TEMPLATE.replace("__R_SECTION__", r_section)
OUT.write_text(card, encoding="utf-8")
print(f"wrote {OUT.name}: {len(card.encode('utf-8')):,} bytes / {card.count(chr(10))+1:,} lines")
print("quote blocks:", card.count('> "'))
