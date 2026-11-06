"""apply_v4_7_revisions.py — v4.7 旧口径批量回补（带唯一性断言）

两类实质改动：
1) 21 CFR Part 113 / 114 法规正文入库 → 「108/113/114 正文未收」收窄为只剩 108
   （另加 110/120/123），「十类不可混引」→「十二类」，19 卡 → 20 卡。
2) Part 110 纠错：FDA 2018-09-12 撤回 2015 规则的 amendatory instruction 13，
   Part 110 至今有效；v4.3「110.110 是过时引用」结论作废。
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / ".cangjie/capabilities/cards"


def load(p: Path) -> tuple[str, bool]:
    b = p.read_bytes()
    crlf = b'\r\n' in b
    return b.decode("utf-8").replace("\r\n", "\n"), crlf


def save(p: Path, text: str, crlf: bool) -> None:
    if crlf:
        text = text.replace("\n", "\r\n")
    p.write_bytes(text.encode("utf-8"))


# (文件, 行首前缀, 新整行)。前缀必须唯一命中一行。
LINE_REPLACEMENTS: list[tuple[str, str, str]] = [
    # ---------- cgmp-compliance-guide ----------
    ("cgmp-compliance-guide.md", "*来源分层：本卡同时取用四类权威",
     "*来源分层：本卡同时取用四类权威，引用前先分层。① **21 CFR Part 117 法规正文**（2015 最终规则，具法律约束力）标注〔§ 117.xxx〕；② **FDA《Small Entity Compliance Guide》**（2016-10，Guidance for Industry，非约束性白话版规则说明）标注「SECG 章号」；③ **FDA PCHF 行业指南**（滚动草案，建议层）标注「PCHF 指南 Ch/小节号」；④ **L.mono 专项指南**（2017-01 Draft – Not for Implementation，建议层）标注「L.mono 指南章号」；⑤ **FDA《Food Defect Levels Handbook》**（执法裁量参考，非法规非 guidance）标注「Handbook 章名 + 产品名」，其法定义务锚点是〔§ 117.110〕。五类不可混引；缺陷阈值与放行的完整判定见 CAP-15 `defect-action-levels`。v4.7 起全包统一「**十二类不可混引**」——法规正文层新增 **21 CFR Part 113〔§ 113.xxx〕与 Part 114〔§ 114.xxx〕** 两套（第十一、第十二来源，见 CAP-20 `lacf-statutory-requirements`），自此〔§ 117.xxx〕只能理解为「判定 **Part 117 义务**的唯一基准」；本卡之外另有 CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / 过敏原 Ed.5，检查视角分别见 CAP-16 / CAP-17 / CAP-18 / CAP-19。*"),
    ("cgmp-compliance-guide.md", "1. **四层效力栈，一层都不能跳**",
     "1. **四层效力栈，一层都不能跳**。① 21 CFR Part 117 法规正文（最终规则，must，判定 **Part 117 义务**的唯一判定基准；Part 113/114 的法定要求另见 CAP-20）→ ② SECG（2016-10，面向境内境外食品设施的白话版规则说明，represent current thinking，不创设义务）→ ③ 专项行业指南（PCHF 指南、L.mono 指南均为 Draft，一律建议层）→ ④ 执法口径文件（CPG、Compliance Programs、Import Alerts，是 FDA 检查员的作业指令，不是企业义务清单）。用户说「找一份 cGMP 合规指南」时，真正想要的多半是第 ② 层；但合规结论必须能回指法规正文。**栈外另有一类并列参考**：《Food Defect Levels Handbook》是 FDA 汇编的 defect action levels 一览与术语表，§ 117.3 定义用的是 `may regard ... adulterated`，属执法裁量参考；〔§ 117.110(b)〕明文指向它取「可能使食品掺假的行动水平实例」。不要把它塞进效力栈排序，也不要把它的数值写成法定义务（见 CAP-15）。"),
    ("cgmp-compliance-guide.md", "把缺陷超标的批次掺进合格批次",
     "把缺陷超标的批次掺进合格批次，即使终产品检测值落在行动水平以内，法规仍认定终产品 adulterated——原文 `regardless of the defect level of the final food`。SECG 在同一段指向 *Defect Levels Handbook* 作为行动水平实例来源（该手册正文已收为第六来源，见 CAP-15 `defect-action-levels`：111 个产品 / 173 条行动水平）。⚠ 网页引言的 `21 CFR 110.110` **不是过时引用**：Part 110 至今有效（FDA 2018-09-12 撤回了删除指令），只是**正文本包未收**；Part 117 侧对应条款是〔§ 117.110〕。详见 CAP-20 B2 的 v4.7 纠错。本包 `chemical-hazard-controls` 卡把这条归入「不得用掺混稀释处理超标批次」纪律，不得与「返工 reconditioning 经证明有效后可再用」混为一谈（后者见〔§ 117.80(c)(9)〕与 SECG XIII.F Manufacturing Operations (9)）。"),
    ("cgmp-compliance-guide.md", "- 未收：IOM 其余章节",
     "- 未收：IOM 其余章节（尤其 Ch.3/4/6/7/8，Ch.4 含 702(b) 分割留样与制样）、RPM、FMD-86 / FMD-147、SOP-001052 / SOP-000529、CPG 全套（含 Sec. 130.100 / 527.300）、其他 Compliance Programs（7303.878 FSVP、7303.080 Produce Safety、7304.019 等）、Import Alerts / Import Bulletins 正文、AOAC Official Methods / eBAM / BAM / MPM 方法正文、21 CFR 2.10 / 133 / 1240.61 正文、Form FDA 483/484 数据库、21 CFR part 117 citations table、SOFO job aid、Human Food By-Products GFI #239 全文。**低酸/酸化体系**：CP 7303.070 已由 CAP-19 收入；其依据的 **21 CFR part 113 / 114 法规正文已由 CAP-20 收入**；**part 108（FCE/SID/Emergency Permit）、part 110（旧 CGMP，含 §110.110）、part 120 / 123 正文仍未收**，一律标「转引未收」；21 CFR Part 120 / 123 与 21 CFR part 117〔§ 117.5(b)(c)〕的接口只给结论不展开。"),
    ("cgmp-compliance-guide.md", "**B8 — 引用标注规范（全包统一）。**",
     "**B8 — 引用标注规范（全包统一，v4.7）。** 法规用〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕（三套独立编号）；SECG 用章号（如 SECG XIII.C）；PCHF 指南用 Ch/小节号；L.mono 指南用其章节号；Ed.5 用问答编号；Handbook 用「Handbook 章名 + 产品名」；CPGM 7303.040 用「CPGM 7303.040 PART x」（附件须带 `ATTACHMENT A` 前缀）；CP 7303.050 用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」；IOM 用「IOM 5.x.x / IOM Exhibit 5-x」；CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」。**21 CFR part 108 / 110 / 120 / 123 等未收正文一律标「转引未收」；十二类不可混引**，也不得把 SECG 的 80 FR 55907 与 CFR 条文 source note 的 80 FR 56145 判为两份不同规则——同一份 2015-09-17 最终规则，前者是发布通知首页，后者是条文部分首页。⚠ 特别注意〔§ 114.5〕现行原文并列 `parts 110 and 117`，**不得改写成只有 part 117 或判为笔误**。"),
    ("cgmp-compliance-guide.md", "**B11 — 缺陷行动水平的两处引用陷阱",
     "**B11 — 缺陷行动水平的引用陷阱（v4.7 更正，与 CAP-15 / CAP-20 共守）。** ① **Part 110 至今有效**：v4.6 及以前本卡写「Part 110 依 2015-09-17 最终规则于 2018-09-17 移除、Handbook 的 `21 CFR 110.110` 是过时引用」，该结论**不成立**。FDA 2018-09-12 最终规则（FR Doc. 2018-19855）撤回了 2015 规则的 amendatory instruction 13（`amendatory instruction 13 ... is withdrawn`），因合规日期延长会造成 4–16 个月 CGMP 空档；eCFR 现行版 Part 110 仍列 11 个 sections（含 §110.110）。因此手册引言指向的是**仍有效、但正文本包未收**的旧 CGMP 条款，须标「转引未收」；§114.5 并列 `parts 110 and 117` 同样是现行文本。② 手册那句 \"Poor manufacturing practices may result in enforcement action without regard to the action level\" 是 **§110.110(c)** 的意译，**仍不得标成〔§ 117.110(c)〕**（Part 117 的 §117.110 只有 (a)(b) 两款），但理由从「part 110 已删」更正为「那是 part 110 的 (c) 款、不是 part 117 的」；该层约束在 Part 117 体系下来自 FD&C Act § 402(a)(4) 与 Subpart B 整体。③ **措辞差异**：手册写混合「at or above the current defect action level」不合法，〔§ 117.110(b)〕写「at levels that render that food adulterated」——以法规措辞为准。索引表里〔§ 117.110〕一行的判定基准是 `lowest level currently feasible`，不是手册表内数字；手册是 FDA 执法裁量参考，不是合规上限或放行标准。2018-19855 正文属外部核实、本包未收。"),

    # ---------- defect-action-levels ----------
    ("defect-action-levels.md", "> —— Handbook INTRODUCTION（原文照录；",
     "> —— Handbook INTRODUCTION（原文照录；**v4.7 更正**：`21 CFR Part 110.110` 指向的是**至今仍有效**的 Part 110——FDA 2018-09-12 撤回了 2015 规则拟于 2018-09-17 删除 part 110 的 amendatory instruction 13；但 part 110 **正文本包未收**，须标「转引未收」。Part 117 侧对应条款为〔§ 117.110〕，详见 B2 与 CAP-20 B2）"),
    ("defect-action-levels.md", "3. **`110.110` 是过时的法规引用**",
     "3. **`110.110` 不是过时的法规引用（v4.7 更正）**。网页 INTRODUCTION 首句写 `21 CFR Part 110.110`；§110.110(c) 那句 \"Compliance with defect action levels does not excuse violation of ... 402(a)(4) ... or ... current good manufacturing practice\" 正是手册 \"Poor manufacturing practices may result in enforcement action without regard to the action level\" 的出处。2015-09-17 PCHF 最终规则的 amendatory instruction 13（80 FR 56144）本拟于 2018-09-17 移除 part 110，但 **FDA 2018-09-12 最终规则（FR Doc. 2018-19855）撤回该指令**，Part 110 至今有效、eCFR 仍列 11 个 sections。所以对 `110.110` 的正确处理是「**现行仍有效，但正文本包未收 → 转引未收**」，不是「判为过时」。〔§ 117.110〕**只有 (a)(b) 两款**，没有复述 110.110(c) 的免责例外句；那句**不得标成〔§ 117.110(c)〕**，理由是它是 part 110 的 (c) 款，而非「part 110 已删」。Part 117 体系下该层约束来自 402(a)(4) 与 Subpart B 整体。本包给 Part 117 义务时一律写〔§ 117.110〕。"),
    ("defect-action-levels.md", "4. 看到资料引用 `21 CFR 110.110`",
     "4. 看到资料引用 `21 CFR 110.110` 或 \"Part 110\"，需要判断：该条款**现行仍有效**（2018 删除指令已撤回），但**正文本包未收**；若讨论 Part 117 体系下的义务，回〔§ 117.110〕〔§ 117.3〕〔§ 117.80(b)(3)(4)〕核对，不要照抄手册白话当法条原文，也不要把 §110.110(c) 标成〔§ 117.110(c)〕。"),
    ("defect-action-levels.md", "**Step 1 — 先过法源关（不许跳）**",
     "**Step 1 — 先过法源关（不许跳）**。问三件事：① 这是法规义务还是 FDA 执法裁量？答案：Part 117 义务在〔§ 117.110〕〔§ 117.80(b)(3)(4)〕，裁量在 Handbook 表；② 引用的是 `110.110` 还是 `117.110`？前者**现行仍有效但正文未收**，标「转引未收」并回 Part 117 侧法条核对，不要判为过时（v4.7 更正）；③ 用户要的是'数值'还是'合规结论'？数值可给但必须附义务层说明，合规结论必须能回指〔§ 117.xxx〕。"),
    ("defect-action-levels.md", "**B2 — `110.110` 是过时引用。**",
     "**B2 — Part 110 至今有效；`110.110` 不是过时引用（v4.7 实质性纠错）。** Handbook 网页 INTRODUCTION 首句仍写 21 CFR Part 110.110。2015-09-17 PCHF 最终规则（80 FR 55908）的 **amendatory instruction 13**（56144 页）指示 Federal Register 于 2018-09-17 `remove and reserve part 110`；**FDA 2018-09-12 最终规则（FR Doc. 2018-19855，同日生效）撤回该指令**，官方措辞 `amendatory instruction 13 in the third column on page 56144 is withdrawn`，理由是部分小/极小微企业 part 117 合规日期延长至 2020-01-27，若删除会有 4–16 个月 CGMP 空档。`Retaining the Human Food CGMP regulation will maintain the status quo ... and will avoid an unintended gap in public health protection.`；FDA 并称将在所有企业达到 part 117 CGMP 合规日后另案移除。**eCFR 现行版 Part 110 仍列 11 个 sections（含 §110.110）**，§114.5 并列 `parts 110 and 117` 也是现行文本。由此：① 手册那句 \"Poor manufacturing practices may result in enforcement action without regard to the action level\" 是 **§110.110(c)** 的意译，**仍不得标成〔§ 117.110(c)〕**，但理由是「那是 part 110 的 (c) 款」，不再是「part 110 已删」；② Part 117 侧现行法条仍是〔§ 117.110〕（Subpart B，仅 (a)(b) 两款）＋〔§ 117.3〕定义＋〔§ 117.80(b)(3)(4)〕原料要求＋FD&C Act § 402(a)(3)/(4)，`lowest level currently feasible` 与掺混稀释禁令**结论不变**；③ part 110 正文本包未收，讨论时标「转引未收」；④ 2018-19855 正文属**外部核实、本包未收**。完整事实链见 CAP-20 B2。"),
    ("defect-action-levels.md", "**B4 — 检查员视角已补四卡，方法与制样仍缺。**",
     "**B4 — 检查员视角已补四卡，法规正文层已扩为三套，方法与制样仍缺。** 第七来源 CPGM 7303.040 现行版（`2025-CPM-HFP-001`）已收，见 CAP-16 `inspection-readiness`：给检查类型、取证深度、观察项分级与记录举证矩阵；**第八来源 CP 7303.050（2022 签发 / 2025-09-10 更正）已收**，见 CAP-17 `inspection-sampling`：给污秽/霉变抽样、产品样品量与 PART V 逐案执法阶梯；**第九来源 IOM 2026 Ch.5 已收**，见 CAP-18；**第十来源 CP 7303.070（2024 签发 / 2025-09-26 更正）已收**，见 CAP-19：给 LACF/AF 管辖分流、酸化判定三步、pH/aw 实验室判读与 Import Alert 升级；**第十一、十二来源 21 CFR Part 113 / 114 法规正文已收**，见 CAP-20 `lacf-statutory-requirements`：给企业法定义务与〔§ 117.1(c)〕〔§ 117.5(d)〕接口。本卡则给**阈值出处与义务边界**。**仍未收**：21 CFR part 108 / 110 / 120 / 123 正文、IOM 其余章节（尤其 Ch.4 的 702(b) 与制样）、RPM、FMD-86 / FMD-147、SOP-001052、CPG 全套、其他 Compliance Programs（7303.878 / 7303.080 / 7304.019 等）、Import Alerts 正文、AOAC / MPM 方法正文、21 CFR part 117 citations table 与 SOFO job aid；分析方法检出限、显微判读、证据充分性标准与警告信判定阈值须另行复核。"),
    ("defect-action-levels.md", "**B8 — 引用标注规范（全包统一，本卡新增第六来源）。**",
     "**B8 — 引用标注规范（全包统一，v4.7）。** 法规用〔§ 117.110〕〔§ 117.80(b)(3)〕〔§ 117.3〕，LACF/AF 法条另用〔§ 113.xxx〕〔§ 114.xxx〕；手册用「Handbook INTRODUCTION / PRODUCTS WITHOUT DEFECT LEVELS / GLOSSARY / COMMODITIES AND DEFECT ACTION LEVELS + 产品名」；SECG 用章号；PCHF 指南用 Ch/小节号；Ed.5 用问答编号；L.mono 指南用其章节号。**十二类不可混引**（CPGM 7303.040 用「PART x」、CP 7303.050 用「PART x / ATTACHMENT A Part x / Table x」、IOM 用「IOM 5.x.x」、CP 7303.070 用「PART x / ATTACHMENT x」标注），尤其不得把手册原文标成〔§ 117.xxx〕，不得把 § 117.110(b) 的措辞换成手册的 \"at or above the current defect action level\"，也不得把 §110.110(c) 标成〔§ 117.110(c)〕。"),

    # ---------- inspection-readiness ----------
    ("inspection-readiness.md", "*来源分层：本卡取用三类权威",
     "*来源分层：本卡取用三类权威，引用前先分层。① **21 CFR Part 117 法规正文**（〔§ 117.xxx〕，具法律约束力，是判定 **Part 117 义务与记录要求**的唯一判定基准；Part 113 / 114 法条另见 CAP-20）；② **FDA CPGM 7303.040《Preventive Controls and Sanitary Human Food Operations》现行版**（Transmittal `2025-CPM-HFP-001`，签发 08/29/2025，IMPLEMENTATION DATE 05/23/2024，50 页），是 **FDA 给检查员与分部的内部作业指导**，标注「CPGM 7303.040 PART x」，不创设企业义务；③ `source-cpgm-7303-040-2020.md`（`2020-CPGM-CFSAN-003`，10/15/2020，47 页）仅为**已废止的历史对照**。三类不可混引；全包来源自 v4.7 起为**十二类**：Part 117 / 113 / 114 三套法规正文 + PCHF 指南 / L.mono 指南 / SECG / Ed.5 / Handbook 五类参考与指南层 + CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 四类检查员作业层，统一「**十二类不可混引**」。*"),
    ("inspection-readiness.md", "**B10 — 相邻 program 可能同日并行。**",
     "**B10 — 相邻 program 可能同日并行。** CPGM PART II.2.D 列 17 项交互 program（海产品 7303.842、果汁 7303.847、低酸/酸化 7303.070、膳食补充剂 7321.008、婴儿配方 7321.006、标签 7321.005、FSVP 7303.878、Produce Safety 7303.080、真菌毒素 7307.001、动物食品 7371.000 等）。`regulatory-boundaries` 卡能判边界，但除 **7303.050 已收（CAP-17）** 与 **7303.070 已收（CAP-19）** 外，本包没有其余这些 program 的正文；LACF/AF 的**法规正文**已由 CAP-20 收入 21 CFR Part 113 / 114，但 **part 108（FCE/SID/Emergency Permit）、part 110、part 120 / 123 正文仍未收**。一次检查可能同时按多个 program 取证。"),
    ("inspection-readiness.md", "**B12 — 引用规范。**",
     "**B12 — 引用规范（v4.7）。** 法规正文用〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕三套独立编号；CPGM 用「CPGM 7303.040 PART x」（附件须带 `ATTACHMENT A`）；PCHF 指南用 Ch/小节号；L.mono 指南用其章节号；SECG 用 SECG 章号；Ed.5 用问答编号；Handbook 用「Handbook 章名 + 产品名」；CP 7303.050 用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」；IOM 用「IOM 5.x.x / IOM Exhibit 5-x」；CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」。**十二类不可混引**；本卡与 CAP-17 / CAP-18 / CAP-19 / CAP-20 的内容须按此分源引用。"),

    # ---------- inspection-sampling ----------
    ("inspection-sampling.md", "*来源分层：本卡取用三类权威",
     "*来源分层：本卡取用三类权威，引用前先分层。① **21 CFR Part 117 法规正文**（〔§ 117.xxx〕，具法律约束力，是判定 **Part 117 义务**的唯一判定基准；Part 113 / 114 法条另见 CAP-20）与 **FD&C Act**（`402(a)(1)/(3)/(4)`、`801(a)(3)`、`704(d)`、`702(b)`）；② **FDA Compliance Program Guidance Manual 7303.050**《Sampling for Foodborne Biological Hazards and Filth – Domestic and Import》（**Date of Issuance 06/03/2022，IMPLEMENTATION DATE 06/03/2022，Correction date 09/10/2025**，62 页），是 **FDA 给检查员/分部/实验室的内部抽样作业指导**，标注「CP 7303.050 PART x / ATTACHMENT x / Table x」，不创设企业义务；③ **IOM 2026 Chapter 5**（取样时的表单与证据链，标注「IOM 5.x.x」，见 `investigator-authority-procedure` 卡）。全包自 v4.7 起**十二类不可混引**（法规正文层新增〔§ 113.xxx〕〔§ 114.xxx〕）。⚠ CP 7303.070 PART II.2.C(2) 把标 `Keep Refrigerated` 的产品（免 21 CFR 113/114）路由到本 program，分流细节见 CAP-19，法条依据见 CAP-20。*"),
    ("inspection-sampling.md", "**B10 — 引用规范（十类不可混引）。**",
     "**B10 — 引用规范（十二类不可混引，v4.7）。** 法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕；FD&C Act 用 `402(a)(4)` / `801(a)(3)`；PCHF 指南用 Ch/小节号；L.mono 指南用其章节号；SECG 用 SECG 章号；Ed.5 用问答编号；Handbook 用「Handbook 章名 + 产品名」；CPGM 7303.040 用「CPGM 7303.040 PART x」（附件带 `ATTACHMENT A` 前缀）；**CP 7303.050 用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」**；**IOM 用「IOM 5.x.x」**；**CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」**。十二类不可混引；21 CFR part 108 / 110 / 120 / 123 正文未收，标「转引未收」；PD 文件内部还有 `PART V`（主文）与 `ATTACHMENT A Part V`（环境取样）同名不同口径，引用须带附件前缀。"),

    # ---------- investigator-authority-procedure ----------
    ("investigator-authority-procedure.md", "*来源分层：本卡取用两类权威",
     "*来源分层：本卡取用两类权威，引用前先分层。① **FD&C Act**（`704(a)(1)`、`301(e)/(f)`、`807(b)`、`414(a)`、`402(a)(4)`）与 **21 CFR Part 117 法规正文**〔§ 117.xxx〕——只有这一层创设企业义务（Part 113 / 114 法规正文另见 CAP-20〔§ 113.xxx〕〔§ 114.xxx〕）；② **FDA Investigations Operations Manual 2026, Chapter 5 – Inspections**（221 页 / 410 书签，含 5.1–5.16 与 Exhibit 5-1…5-23），是 **FDA 给调查员的内部作业手册**，标注「IOM 5.x.x / IOM Exhibit 5-x」，规定到场、表单、取证、写 EIR 与签发 FDA 483 的规则，**不是法规、不是 Guidance for Industry、不创设企业义务**。全包自 v4.7 起**十二类不可混引**。⚠ CP 7303.070 PART II.2.B(2) 补上 RRA 的官方程序性定义（`RRAs are not considered inspections`），见 CAP-19；它不改变 IOM 5.2.7 的预告三层口径。*"),
    ("investigator-authority-procedure.md", "**B10 — 引用规范（十类不可混引）。**",
     "**B10 — 引用规范（十二类不可混引，v4.7）。** 法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕；FD&C Act 用 `704(a)(1)` / `301(f)` / `807(b)` / `402(a)(4)`；PCHF 指南用 Ch/小节号；L.mono 指南用其章节号；SECG 用 SECG 章号；Ed.5 用问答编号；Handbook 用「Handbook 章名 + 产品名」；CPGM 7303.040 用「CPGM 7303.040 PART x」（附件带 `ATTACHMENT A`）；CP 7303.050 用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」；**IOM 用「IOM 5.x.x」或「IOM Exhibit 5-x」**；**CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」**。十二类不可混引；IOM 的 Exhibit 编号与 IOM 正文小节号也不同层，勿把 Exhibit 5-5 写成 IOM 5.5.5。"),

    # ---------- lacf-inspection-program（CAP-19）----------
    ("lacf-inspection-program.md", "*来源分层：本卡取用四类权威",
     "*来源分层：本卡取用四类权威，引用前先分层。① **21 CFR Part 117 法规正文**（〔§ 117.xxx〕，具法律约束力，是判定 **Part 117 义务**的唯一基准）——关键接口为〔§ 117.5(d)(1)(2)〕「part 113 活动的 Subparts C/G 豁免、且仅限其管辖的微生物危害」与〔§ 117.1(c)〕「受专项 CGMP 法规管辖的食品同时受 Part 117 约束」；② **FDA Compliance Program Guidance Manual 7303.070**（**Date of Issuance 09/26/2024，IMPLEMENTATION DATE 9/26/2024，Correction Date 9/26/2025**，61 页），是 **FDA 给检查员、实验室分析员与合规官的内部作业指导**，标注「CP 7303.070 PART x / ATTACHMENT x」，**不创设企业义务**；③ **21 CFR Part 113 / 114 法规正文**（〔§ 113.xxx〕〔§ 114.xxx〕，4-1-25 Edition）——**v4.7 已由 CAP-20 `lacf-statutory-requirements` 收入**，本卡涉及法条义务时须转该卡；**21 CFR part 108 / 110 / 120 / 123 正文本包仍未收**，一律标「转引未收」；④ IOM 2026 Ch.5（表单与证据链，见 `investigator-authority-procedure`）。与其余各类合计**十二类不可混引**。*"),
    ("lacf-inspection-program.md", "*本卡定位：v4.4–v4.5 已把",
     "*本卡定位：v4.4–v4.5 已把「检查类型/记录举证」（7303.040）、「取样量/环境拭子」（7303.050）、「权限/表单/483 措辞」（IOM Ch.5）补齐，v4.6 补上本卡的检查员侧落地；**v4.7 再由 CAP-20 补上 Part 113 / 114 法规正文的法定义务层**。本卡给的是**检查员作业口径与出处**——一个产品/设施何时进 LACF/AF 轨道、检查会查哪些记录与样品、什么数值触发升级；**不是**法条义务清单，也不是企业内控放行标准。两张卡必须并用。*"),
    ("lacf-inspection-program.md", "我明确拒绝两件事：",
     "我明确拒绝两件事：把 CP 7303.070 的检查动作写成企业法定义务；以及**从 CP 反推 21 CFR 法条**。**v4.7 起 part 113 / 114 正文已收（转 CAP-20 `lacf-statutory-requirements`），但 part 108 / 110 / 120 / 123 仍未收**，这几套只能标「转引未收」。本卡的价值是检查视角与升级阶梯；法规义务请回 CAP-20 的〔§ 113.xxx〕〔§ 114.xxx〕。"),
    ("lacf-inspection-program.md", "法规义务写〔§ 117.xxx〕；CP 内容写",
     "法规义务写〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕（后两套转 CAP-20）；CP 内容写「CP 7303.070 PART x」；`21 CFR part 108 / 110 / 120 / 123` 只能写「转引未收」；IOM 写「IOM 5.x.x」；其余各类按各自编号。**十二类不可混引**。遇到需要 part 108/110 条文、BAM 方法、IOM Ch.4 抽样表、CPG 520.200/520.300、Import Alert 全文的具体问题，直接转出本包；遇到需要 113/114 条文的问题，**转 CAP-20 而非转出本包**。"),
    ("lacf-inspection-program.md", "**B2 — 21 CFR part 108 / 113 / 114 正文本包未收。**",
     "**B2 — 21 CFR Part 113 / 114 正文已收（v4.7），part 108 / 110 / 120 / 123 仍未收。** 本卡所有涉及 FCE 注册、SID 备案、Emergency Permit 的内容，都是 **CP 里的转引**（法源 part 108，正文未收）；涉及 scheduled process、商业无菌、人员培训、记录保存、偏差处置等**法条义务**的内容，现应转 **CAP-20 `lacf-statutory-requirements`** 并按〔§ 113.xxx〕〔§ 114.xxx〕引用，不得再标「转引未收」。⚠ 仍需标「转引未收」的：21 CFR part 108（含 §108.35 BPCS 认可）、part 110（旧 CGMP，含 §110.110；**至今有效**、见 CAP-20 B2 纠错）、part 120 / 123（果汁/海产品 HACCP）、IOM Chapter 4（Sample Schedule Chart 2）、BAM Ch.13B/14/17/21A/22A–22D、CPG Sec. 520.200/520.300、Import Alert 99-37/99-38 全文、SOP-001642、RPM Ch.4/9、21 CFR part 507 与 7303.842 正文。不得从 CP 的检查动作反推法条，也不得用 CP 的检查动作替代法规要求。"),
    ("lacf-inspection-program.md", "**B11 — 引用规范（十类不可混引）。**",
     "**B11 — 引用规范（十二类不可混引，v4.7）。** 法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕；PCHF 指南 Ch/小节号；L.mono 指南其章节号；SECG 章号；Ed.5 问答编号；Handbook「章名 + 产品名」；CPGM 7303.040「PART x」（附件带 `ATTACHMENT A`）；CP 7303.050「PART x / ATTACHMENT A Part x / Table x」；IOM 2026 Ch.5「IOM 5.x.x / Exhibit 5-x」；**CP 7303.070「PART x / ATTACHMENT x」**。`21 CFR part 108 / 110 / 120 / 123` 与 IOM Ch.4、BAM、CPG、Import Alert 一律标「转引未收」。⚠〔§ 114.5〕现行原文并列 `parts 110 and 117`，不得改写或判为笔误。"),
    ("lacf-inspection-program.md", "**B12 — 超出 19 张能力卡路由范围时明确告知。**",
     "**B12 — 超出 20 张能力卡路由范围时明确告知。** 用户要 **LACF/AF 的法规条文级义务清单 → 转 CAP-20 `lacf-statutory-requirements`**（v4.7 已收 Part 113/114 正文，不再转出本包）；但商业无菌计算、F0/D 值/z 值验证、TD/HP 研究设计、卷边解剖判读、BAM 培养步骤、part 108 备案流程、进口扣留应诉策略仍**超出本包覆盖**，应说明缺口并建议由具备资质的 Process Authority / PCQI / 审核员与法规正文核对，不要硬套 CP 的检查动作。"),

    # ---------- regulatory-boundaries ----------
    ("regulatory-boundaries.md", "6. **执法裁量参考不是义务来源**",
     "6. **执法裁量参考不是义务来源**：FDA《Food Defect Levels Handbook》给的是 defect action level（§ 117.3 定义为 FDA `may regard ... adulterated` 的水平），与「企业必须做什么」分属两层。法定义务在〔§ 117.110(a)〕的 `must ... reduce ... to the lowest level currently feasible`、〔§ 117.110(b)〕掺混禁令与〔§ 117.80(b)(3)(4)〕原料要求；低于行动水平仍可因 FD&C Act 402(a)(4) 不卫生条件被判掺假。⚠ **v4.7 纠错**：网页首句的 `21 CFR 110.110` **不是过时引用**——FDA 2018-09-12 撤回了 2015 规则拟删除 part 110 的 amendatory instruction 13，Part 110 至今有效、eCFR 仍列 11 个 sections；但 **part 110 正文本包未收**，须标「转引未收」，Part 117 侧义务仍回〔§ 117.110〕核对，且手册那句 'Poor manufacturing practices...' 是 §110.110(c) 的意译、**不得标成〔§ 117.110(c)〕**（§117.110 只有 (a)(b) 两款）。另注意过敏原标签问答 Ed.5 与缺陷行动水平虽然都是「FDA 给的数值」，法源分别是 FD&C Act 403(w) 与 402(a)(3)，与 Part 117 预防控制互不减免。详见 `defect-action-levels` B2 与 CAP-20 B2。"),
    ("regulatory-boundaries.md", "10. **v4.6 补入 CP 7303.070",
     "10. **v4.6 补入 CP 7303.070，把本卡第 1 条的双法规并集落到检查员侧**：CP PART II.2.C(1) 与法规正文一致地写明，LACF 产品受 Part 117 约束，但〔§ 117.5(d)(1)〕豁免 Subparts C/G **仅限 part 113 覆盖的活动**、且须 `required to comply with, and are in compliance with` part 113，〔§ 117.5(d)(2)〕进一步限定**仅限 part 113 管辖的微生物危害**；未被热处理控制且需预防控制的危害（`Staphylococcus aureus` 生长产毒、化学、物理）仍归 Subparts C/G。⚠ **酸化食品不在该豁免内**：CP 原文 `Acidified foods are subject to the CGMP & PCHF rule`，PCHF 覆盖转 7303.040，检查重点仍在 21 CFR part 108/114；**〔§ 117.201〕是 qualified facility 的 modified requirements，不是 LACF 条款**。CP PART II.2.C(2) 另给 `Keep Refrigerated` 免 113/114 → 7303.050、brites 中央仓 → `PAC 03040` 两条路由。**v4.7 更新**：21 CFR Part 113 / 114 法规正文已收（CAP-20），自此「法规正文层」含 Part 117 / 113 / 114 三套独立编号，本卡第 1 条「Part 117 是唯一法定义务判定基准」须理解为「判定 **Part 117 义务**的唯一基准」；〔§ 114.5〕还明文并列 `parts 110 and 117` 用于酸化食品掺假判定（Part 110 至今有效，正文未收）。**仍未收**：21 CFR part 108 / 110 / 120 / 123 正文，CP 内相关表述一律标「转引未收」。完整判定见 CAP-19（检查员侧）与 CAP-20（法条侧）。"),

    # ---------- reference-tools-discipline ----------
    ("reference-tools-discipline.md", "8. **《Food Defect Levels Handbook》是第六类资料",
     "8. **《Food Defect Levels Handbook》是第六类资料，不在效力栈内**：它是 FDA 汇编的 defect action levels 一览与术语表（执法裁量参考），页面标注 Content current as of 09/07/2018、正文 May 1995 修订版。⚠ **v4.7 纠错**：其法规引用 `21 CFR 110.110` **不是过时引用**——FDA 2018-09-12 撤回了 2015 规则拟删除 part 110 的指令，Part 110 至今有效；但 **part 110 正文本包未收**，讨论时标「转引未收」，Part 117 侧义务回〔§ 117.110〕核对，且手册那句是 §110.110(c) 的意译、不得标成〔§ 117.110(c)〕。用它只能回答「FDA 对该产品的行动水平是多少、缺陷来源与 SIGNIFICANCE 是什么」，不能回答「我是否合规」——后者回〔§ 117.110(a)〕`lowest level currently feasible`、〔§ 117.80(b)(3)(4)〕与 402(a)(4)。表内数值绑定 AOAC / MPM 方法编号与取样量，方法正文未收；引用具体数值前须核对 Federal Register Notices 是否有修订。完整判定见 `defect-action-levels` 卡与 CAP-20 B2。"),
    ("reference-tools-discipline.md", "12. **CP 7303.070 是第十类资料",
     "12. **CP 7303.070 是第十类资料，同样不在效力栈内**：现行件为 2024-09-26 签发 / 2025-09-26 更正（文件名 20250929 只是生成日），是 FDA 给检查员、实验室分析员与合规官的**低酸/酸化罐头专门体系作业指导**。用它只能回答「LACF/AF 走哪条 program、检查员查哪些记录、什么数值触发升级」，不能回答「我是否合规」——后者**v4.7 起回 CAP-20 的〔§ 113.xxx〕〔§ 114.xxx〕法规正文**与〔§ 117.5(d)(1)(2)〕〔§ 117.1(c)〕；**21 CFR part 108 / 110 / 120 / 123 正文仍未收**。⚠ 三类数字不可互替：4.6/0.85 是法定边界（〔§ 113.3(n)〕〔§ 114.3(b)〕），4.40/4.65/4.75、0.90/0.93、异常罐 1%、24 罐/12 罐是 CP 的实验室与取证触发线，≤4.4/≤0.92 是 L.mono 草案抑制型配方基准。`Acidified foods are subject to the CGMP & PCHF rule`——**不得把 AF 一并免掉 Subparts C/G**；也不要把〔§ 117.201〕误当 LACF 条款。完整判定见 `lacf-inspection-program`（CAP-19，检查员侧）与 `lacf-statutory-requirements`（CAP-20，法条侧）。"),

    # ---------- 来源文件头（CP 7303.070）----------
    ("@root/source-cp-7303-070-2024.md", "- ⚠ **法源三角正文本包未收**",
     "- ⚠ **法源三角：part 113 / 114 正文已收（v4.7），part 108 仍未收**：本 program 判定合规所依据的是 **21 CFR part 108（Emergency Permit Control，含 FCE 注册与 SID 定时工艺备案）、part 113（Thermally Processed Low-Acid Foods Packaged in Hermetically Sealed Containers）、part 114（Acidified Foods）**（`PART I`、`PART II.1`）。**v4.7 已把 part 113 / 114 法规正文（4-1-25 Edition）收为第十一、第十二来源，见 `source-cfr-part113-2025.md` / `source-cfr-part114-2025.md` 与 CAP-20 `lacf-statutory-requirements`**；下面 CP 正文中涉及 scheduled process、商业无菌、记录保存等法条义务的表述，现可回〔§ 113.xxx〕〔§ 114.xxx〕核对。**仍未收**：part 108（含 §108.35）、**part 110（旧 CGMP，含 §110.110；至今有效——FDA 2018-09-12 撤回了 2015 规则的删除指令，见 CAP-20 B2）**、part 120 / 123、IOM Chapter 4 Sample Schedule Chart 2、BAM Ch.13B/14/17/21A/22A–22D、CPG Sec. 520.200 / 520.300、Import Alert 99-37 / 99-38 原文、SOP-001642、RPM Ch.4/9。不得从本 CP 反推未收正文的条文，也不得把 CP 的检查动作写成企业法定义务。"),
]


def main() -> None:
    changed: dict[str, int] = {}
    for rel, prefix, new_line in LINE_REPLACEMENTS:
        if rel.startswith("@root/"):
            p = (ROOT / rel[len("@root/"):]).resolve()
        else:
            p = (CARDS / rel).resolve()
        assert p.exists(), f'missing file: {p}'
        text, crlf = load(p)
        pat = re.compile(rf'(?m)^{re.escape(prefix)}.*$')
        hits = list(pat.finditer(text))
        assert len(hits) == 1, f'{p.name}: {len(hits)} hits for prefix {prefix[:40]!r}'
        text = pat.sub(lambda m: new_line, text, count=1)
        save(p, text, crlf)
        changed[p.name] = changed.get(p.name, 0) + 1

    # 全局简单口径替换（只在指定文件内，且断言命中数）
    GLOBAL = [
        "cgmp-compliance-guide.md", "defect-action-levels.md", "inspection-readiness.md",
        "inspection-sampling.md", "investigator-authority-procedure.md",
        "lacf-inspection-program.md", "regulatory-boundaries.md", "reference-tools-discipline.md",
    ]
    for name in GLOBAL:
        p = CARDS / name
        text, crlf = load(p)
        before = text
        text = text.replace("十类不可混引", "十二类不可混引")
        text = text.replace("十类**不可混引**", "十二类**不可混引**")
        text = text.replace("19 张能力卡", "20 张能力卡")
        if text != before:
            save(p, text, crlf)
            changed[name] = changed.get(name, 0) + 1
    print("v4.7 revisions applied:")
    for k, v in sorted(changed.items()):
        print(f'  {k}: {v} pass(es)')
    print(f'  line replacements: {len(LINE_REPLACEMENTS)}')


if __name__ == '__main__':
    main()
