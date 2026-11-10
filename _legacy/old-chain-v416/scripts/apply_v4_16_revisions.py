"""apply_v4_16_revisions.py — v4.16 全包口径回补（第二十来源 IOM 2026 Chapter 4）

顺序纪律（沿用 v4.8 起的教训）：
1. 先做**逐条精确改写**（含「十九类」「27 张」的 old 串按完整句改写），
   避免事后全局替换把「当时口径」阶梯污染。
2. 再做**当前态计数替换**：十九类→二十类、27 张→28 张（仅作用于
   cards/ 与 assemble_bundle.py，历史版本文档 BOOK_OVERVIEW / PIPELINE_STATE
   的 v4.x 阶梯保留不改）。
3. 最后做残留自检：IOM Ch.4 不应再出现在「未收」清单里。

支持 --apply 才写盘；默认 dry-run。
"""
from __future__ import annotations

import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
C = BASE / ".cangjie/capabilities/cards"
AB = BASE / ".cangjie/assemble_bundle.py"

# (相对路径, 标签, old, new, 期望出现次数)
REWRITES: list[tuple[str, str, str, str, int]] = [
    # ══════════════════ assemble_bundle.py ══════════════════
    (".cangjie/assemble_bundle.py", "ab-7303.050-note",
     "IOM Chapter 4、eBAM / BAM / AOAC / MPM 方法正文、SOP-001052、SOP-000529 FMD-147、CPG Sec. 527.300、RPM Ch.9 与 Import Alert 正文仍未收",
     "**IOM Chapter 4 自 v4.16 起已收（第二十来源，见 CAP-28）**；eBAM / BAM / AOAC / MPM 方法正文、SOP-001052、SOP-000529 FMD-147、CPG Sec. 527.300、RPM Ch.9 与 Import Alert 正文仍未收", 1),
    (".cangjie/assemble_bundle.py", "ab-7303.070-note",
     "仍未收的是 part 108（FCE/SID/Emergency Permit/§108.35）、part 110 / 120（part 123 自 v4.9 起已收，见 CAP-22）、IOM Ch.4 Sample Schedule Chart 2、BAM Ch.13B/14/17/21A/22A-22D",
     "仍未收的是 part 110（part 108 自 v4.12 起已收，见 CAP-25；part 120 自 v4.13 起已收，见 CAP-26；part 123 自 v4.9 起已收，见 CAP-22）、BAM Ch.13B/14/17/21A/22A-22D", 1),
    (".cangjie/assemble_bundle.py", "ab-7303.070-note-tail",
     "不得从本 CP 反推未收法条",
     "不得从本 CP 反推未收法条；**IOM Ch.4 Sample Schedule Chart 2 自 v4.16 起已收（第二十来源，见 CAP-28）**", 1),
    (".cangjie/assemble_bundle.py", "ab-7303.842-note",
     "、21 CFR part 1 subpart L、IOM Ch.4、FDA 3501/3502 表单全文与 eNSpect / CMS / FACTS 内部系统 —— 一律标转引未收",
     "、21 CFR part 1 subpart L、FDA 3501/3502 表单全文与 eNSpect / CMS / FACTS 内部系统 —— 一律标转引未收；**IOM Ch.4 自 v4.16 起已收（见 CAP-28）**", 1),
    (".cangjie/assemble_bundle.py", "ab-part108-note",
     "、CPG 全套、Import Alert 全文、BAM / AOAC / MPM 方法正文、IOM Ch.4",
     "、CPG 全套、Import Alert 全文、BAM / AOAC / MPM 方法正文（**IOM Ch.4 自 v4.16 起已收，见 CAP-28**）", 1),
    (".cangjie/assemble_bundle.py", "ab-description-842",
     "以及十九类来源不可混引与三层配对",
     "以及二十类来源不可混引与三层配对", 1),
    (".cangjie/assemble_bundle.py", "ab-principle-count-list",
     "CP 7303.070 与 CP 7303.878 合计**十九类不可混引**",
     "CP 7303.070、CP 7303.878 与 IOM 2026 Ch.4 合计**二十类不可混引**", 1),
    (".cangjie/assemble_bundle.py", "ab-principle-version-chain",
     "v4.15 新增第十九来源 CP 7303.847）",
     "v4.15 新增第十九来源 CP 7303.847、v4.16 新增第二十来源 IOM 2026 Ch.4）", 1),
    (".cangjie/assemble_bundle.py", "ab-out-of-scope",
     "、制样与显微判读、702(b) 分割留样规则（IOM Chapter 4 / RPM / CPG 全套 / Import Alerts / eBAM-BAM-AOAC-MPM 与 BAM Ch.13B/14/17/21A/22A-22D / SOP-001052 / SOP-001642 / FMD-147 未收；CP 7303.050、CP 7303.070 与 IOM Chapter 5 正文已收，给的是抽样量、检查程序与管辖分流，不是实验室方法，也不替代 part 108 的备案条文；113/114 条款级义务见 CAP-20）",
     "、制样与显微判读、702(b) 分割留样规则（**IOM Chapter 4 自 v4.16 起已收，见 CAP-28**；仍未收的是 RPM / CPG 全套 / Import Alerts / eBAM-BAM-AOAC-MPM 与 BAM Ch.13B/14/17/21A/22A-22D / SOP-001052 / SOP-001642 / FMD-147；CP 7303.050、CP 7303.070 与 IOM Chapter 5 / Chapter 4 正文已收，给的是抽样量、检查程序、取样形式要件与管辖分流，不是实验室方法，也不替代 part 108 的备案条文；113/114 条款级义务见 CAP-20）", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-citation",
     "IOM 用「IOM 5.x.x / IOM Exhibit 5-x」标注",
     "IOM 按章号分别标注：Chapter 4 用「IOM 4.x.x / IOM Exhibit 4-xx / IOM Sample Schedule Chart x」、Chapter 5 用「IOM 5.x.x / IOM Exhibit 5-x」", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-uncollected",
     "、IOM Chapter 4、BAM、CPG、Import Alert 等未收正文一律标「转引未收」；**十九类不可混引**",
     "、IOM 其余各章（2/3/6/7/8/9/10）、BAM、CPG、Import Alert 等未收正文一律标「转引未收」；**二十类不可混引**", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-route",
     "检查员侧取证转 CAP-19",
     "检查员侧取证转 CAP-19，取样形式要件与 702(b) 转 CAP-28", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-cgmp-head",
     "Handbook、CPGM 7303.040、CP 7303.050、CP 7303.070 与 IOM Chapter 5 正文虽已收（CAP-15 / CAP-16 / CAP-17 / CAP-19 / CAP-18）",
     "Handbook、CPGM 7303.040、CP 7303.050、CP 7303.070、IOM Chapter 5 与 IOM Chapter 4 正文虽已收（CAP-15 / CAP-16 / CAP-17 / CAP-19 / CAP-18 / CAP-28）", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-cgmp-mid",
     "、调查员权限与证据规则，都不是实验室方法或企业内控标准。仍未收：IOM Chapter 3/4/6/7/8/9/10（尤其 Ch.4 的 702(b) 分割留样与制样、Sample Schedule Chart 2）",
     "、调查员权限与证据规则、取样作为证据的形式要件，都不是实验室方法或企业内控标准。**IOM Ch.4 的 702(b) 分割留样与 Sample Schedule Chart 2 自 v4.16 起已收（CAP-28）**；仍未收：IOM Chapter 2/3/6/7/8/9/10", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-cgmp-cfr",
     "、21 CFR part 108 / 110 / 120（Part 113 / 114 正文自 v4.7 起已收、Part 123 自 v4.9 起已收）与 21 CFR 2.10 / 133 / 1240.61 / 507 正文",
     "、21 CFR part 110（Part 113 / 114 自 v4.7、Part 123 自 v4.9、Part 108 自 v4.12、Part 120 自 v4.13 已收）与 21 CFR 133 / 1240.61 / 507 正文（2.10 三条件在 IOM 4.1.4 有逐字转引）", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-cgmp-form",
     "、Form FDA 484 / 1551 表单细则",
     "、Form FDA 484 / 1551 表单栏目细则（Ch.4 只给签发时点与适用情形）", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-iom-chapters",
     "IOM 只收了 2026 版 Chapter 5 单章，遇文中 IOM 3.2 / 4.x / 6.4 / 8.1 等跨章引用一律标注「转引未收」，不得代填",
     "IOM 收了 2026 版 Chapter 5 与 Chapter 4 两个单章：遇文中 IOM 2.x / 3.2 / 6.4 / 8.1 等跨章引用一律标注「转引未收」，不得代填；4.x 则转 CAP-28", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-7303.070",
     "）、IOM Ch.4 Sample Schedule Chart 2、BAM 各章、CPG Sec. 520.200/520.300",
     "）、BAM 各章、CPG Sec. 520.200/520.300", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-7303.070-tail",
     "F0/D/z 计算与卷边解剖判读仍不得从 CP 反推",
     "F0/D/z 计算与卷边解剖判读仍不得从 CP 反推；**IOM Ch.4 Sample Schedule Chart 2 自 v4.16 起已收（见 CAP-28），但仍属取样计划、不是实验室判读**", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-seafood-hazards-version",
     "全包自 v4.15 起**十九类不可混引**，当前为 27 张能力卡",
     "全包自 v4.16 起**二十类不可混引**，当前为 28 张能力卡", 1),
    (".cangjie/assemble_bundle.py", "ab-stop-7303.842-uncollected",
     "、IOM Ch.4、FDA 3501/3502 表单全文一律标「转引未收」",
     "、FDA 3501/3502 表单全文一律标「转引未收」；**IOM Ch.4 自 v4.16 起已收（见 CAP-28）**", 1),

    # ══════════════════ CAP-16 inspection-readiness ══════════════════
    (".cangjie/capabilities/cards/inspection-readiness.md", "cap16-a2-6",
     "（CP 7303.050 正文已收）；仅 AOAC/MPM 方法正文、IOM Ch.4 与 SOP-001052 未收。",
     "（CP 7303.050 正文已收）；**IOM Ch.4 自 v4.16 起已收，转 CAP-28 `iom-sampling-procedure`** 查 Zone 1–4、子样数、不得预告与 24 小时到实验室；仅 AOAC/MPM 方法正文与 SOP-001052 未收。", 1),
    (".cangjie/capabilities/cards/inspection-readiness.md", "cap16-a2-13",
     "（IOM 2026 Ch.5 正文已收：482/484 表单、电子记录与照片证据规则）；仅 702(b) 分割留样规则（IOM Ch.4）未收。",
     "（IOM 2026 Ch.5 正文已收：482/484 表单、电子记录与照片证据规则）；**702(b) 分割留样规则与取样的形式要件自 v4.16 起已收**，转 **CAP-28 `iom-sampling-procedure`**（IOM 2026 Ch.4：七项豁免、污秽样品反向例外、FDA 415a 单签名）。", 1),
    (".cangjie/capabilities/cards/inspection-readiness.md", "cap16-b5",
     "**仍未收**：IOM Chapter 3/4/6/7/8/9/10（尤其 Ch.4 的 702(b) 分割留样与制样）",
     "**已收（v4.16）**：**IOM 2026 Chapter 4**（189 页）全文（CAP-28，给取样类别、702(b) 与七项豁免、环境取样 Zone/子样数、表单链、封条与运输、Chart 2 取样计划）。**仍未收**：IOM Chapter 2/3/6/7/8/9/10（尤其 Ch.3 的 3.2 权限与 Ch.6 的 6.4 进口取样；Ch.4 已不在此列，但**制样与实验室方法仍不在内**）", 1),
    (".cangjie/capabilities/cards/inspection-readiness.md", "cap16-b5-tail",
     "因此**制样与显微判读、检验方法检出限、702(b) 分割规则、警告信判定阈值",
     "因此**制样与显微判读、检验方法检出限、警告信判定阈值", 1),

    # ══════════════════ CAP-17 inspection-sampling ══════════════════
    (".cangjie/capabilities/cards/inspection-sampling.md", "cap17-position",
     "**不是企业内控抽样标准，也不替代 IOM Chapter 4 / eBAM / AOAC / MPM 方法正文**。",
     "**不是企业内控抽样标准，也不替代 eBAM / AOAC / MPM 方法正文**。⚠ **IOM 2026 Chapter 4 自 v4.16 起已收（第二十来源，CAP-28 `iom-sampling-procedure`）**：本卡管「某 program 抽样时用哪张 Table、报哪个 PAC、阳性后走哪条升级路径」，CAP-28 管「样品作为证据成立的形式要件」，二者是同一件事的两层，不得互替。", 1),
    (".cangjie/capabilities/cards/inspection-sampling.md", "cap17-i-3",
     "企业常问「能不能要一份平行样」——法定分割留样规则在 IOM Chapter 4 与 21 CFR 2.10，本包未收其正文，只能给出「向检查员索取 Form FDA 484 并自行做内部平行留样」的准备原则。",
     "企业常问「能不能要一份平行样」——**自 v4.16 起法定分割留样规则已有原文出处**：`IOM 4.3.2.2` 的 `702(b)` 七项豁免（含「可采量不足分析量两倍」「两倍量成本超 $150」「无法以可行手段保存，明列 fresh produce / water / environmental swabs」「进口样品」等）、`IOM 4.3.2.3` 的 `at least twice` 留样量，以及 **污秽样品 `Regardless of the exemptions ... collect the 702(b) portion for filth samples` 这一反向例外**，一律转 **CAP-28**。⚠ 但索取 Form FDA 484 与 `702(b)` 是两件事：484 是取样凭证，且不发 DOC sample、不发 induced/undercover/online（IOM 4.2.5）。", 1),
    (".cangjie/capabilities/cards/inspection-sampling.md", "cap17-a2-3",
     "3. 用户问「我们被抽了，能要一份平行样吗 / 702(b) 是什么」→ 来源与边界说明 + IOM Chapter 4 未收。",
     "3. 用户问「我们被抽了，能要一份平行样吗 / 702(b) 是什么」→ **转 CAP-28**（IOM 2026 Ch.4 自 v4.16 起已收）：`702(b)` 是 FD&C Act 的法定分割留样请求权（`upon request, provide a part of such official sample`）；默认留分析量两倍，七项豁免逐条排除，污秽样品反向仍须留；21 CFR 2.10 三条件与 official/DOC/INV 类别判定亦在 CAP-28。", 1),
    (".cangjie/capabilities/cards/inspection-sampling.md", "cap17-b4",
     "**未收**：IOM Chapter 4（Sampling，含 702(b) 与 IOM 4.2.5 / 4.3.6.6 / 4.6 / 4.7）、IOM Ch.3/6/7/8/9/10",
     "**已收（v4.16）**：IOM 2026 Chapter 4（Sampling，含 702(b) 与 IOM 4.2.5 / 4.3.6.6 / 4.6 / 4.7 / Sample Schedule Chart 2），见 **CAP-28**。**未收**：IOM Ch.2/3/6/7/8/9/10", 1),
    (".cangjie/capabilities/cards/inspection-sampling.md", "cap17-b4-tail",
     "故**制样与显微判读、702(b) 分割留样规则、分析方法的检出限与确认流程、证据充分性标准、进口扣留应诉**仍须另行复核。",
     "故**制样与显微判读、分析方法的检出限与确认流程、证据充分性标准、进口扣留应诉**仍须另行复核；**702(b) 分割留样规则自 v4.16 起已有原文出处，转 CAP-28**。", 1),
    (".cangjie/capabilities/cards/inspection-sampling.md", "cap17-b10",
     "**IOM 用「IOM 5.x.x」**；**CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」**。十四类不可混引；21 CFR part 108 / 110 / 120 正文未收，标「转引未收」（part 123 已收，写〔§ 123.xxx〕）",
     "**IOM 按章号：Ch.5 用「IOM 5.x.x」、Ch.4 用「IOM 4.x.x / IOM Exhibit 4-xx / IOM Sample Schedule Chart x」（自 v4.16 起已收，转 CAP-28）**；**CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」**。二十类不可混引；21 CFR part 110 正文未收，标「转引未收」（part 108 自 v4.12、part 120 自 v4.13、part 123 自 v4.9 已收）", 1),

    # ══════════════════ CAP-18 investigator-authority-procedure ══════════════════
    (".cangjie/capabilities/cards/investigator-authority-procedure.md", "cap18-a2-9",
     "也不替代 702(b) 分割留样规则（IOM Ch.4 未收）。",
     "也不替代 702(b) 分割留样规则（**IOM Ch.4 自 v4.16 起已收，转 CAP-28**）。另注意 IOM 4.2.5 的两条例外：DOC sample 不发 FDA 484、induced/undercover/online 通常不发 482+484——所以「取了样却没收到 484」未必是程序瑕疵，先判样品类别。", 1),
    (".cangjie/capabilities/cards/investigator-authority-procedure.md", "cap18-table-row",
     "| 702(b) 分割留样、制样、检验方法 | IOM Ch.4 / eBAM / AOAC / MPM——**未收** |",
     "| 702(b) 分割留样 | **IOM Ch.4 自 v4.16 起已收 → CAP-28**（4.3.2.2 七项豁免、4.3.2.3 两倍量、4.7.4 独立容器封条） |\n| 制样、检验方法 | eBAM / AOAC / MPM——**未收** |", 1),
    (".cangjie/capabilities/cards/investigator-authority-procedure.md", "cap18-b10",
     "**IOM 用「IOM 5.x.x」或「IOM Exhibit 5-x」**；**CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」**。十四类不可混引；",
     "**IOM 按章号：Ch.5 用「IOM 5.x.x」或「IOM Exhibit 5-x」；Ch.4 用「IOM 4.x.x / IOM Exhibit 4-xx / IOM Sample Schedule Chart x」（自 v4.16 起已收，转 CAP-28）**；**CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」**。二十类不可混引；", 1),

    # ══════════════════ CAP-19 lacf-inspection-program ══════════════════
    (".cangjie/capabilities/cards/lacf-inspection-program.md", "cap19-r-quote-note",
     "> —— PART IV.2 pH 分析取样；具体抽样计划出处仍是 IOM Ch.4 Sample Schedule Chart 2（**正文未收**）",
     "> —— PART IV.2 pH 分析取样；**具体抽样计划出处自 v4.16 起已有原文**：IOM Ch.4 `Sample Schedule Chart 2`（见 CAP-28）——LACF official sample = 全部异常罐 + 规定正常罐、investigational/import = 全部异常 + 12 正常罐、AF 的 pH 取样 >795 g 取 12 罐 / ≤795 g 取 24 罐且**不含 702(b)**。⚠ Chart 2 是取样计划，本卡的 4.40 / 4.65 / 4.75 是实验室触发线，两层不得混写", 1),
    (".cangjie/capabilities/cards/lacf-inspection-program.md", "cap19-e-table",
     "| **795 g / 24 罐、其余 12 罐** | pH 分析总样品量 | CP 7303.070 PART IV.2；抽样计划出处 IOM Ch.4 Chart 2 **未收** |",
     "| **795 g / 24 罐、其余 12 罐** | pH 分析总样品量 | CP 7303.070 PART IV.2；**抽样计划出处 IOM Ch.4 Sample Schedule Chart 2 自 v4.16 起已收（见 CAP-28）** |", 1),
    (".cangjie/capabilities/cards/lacf-inspection-program.md", "cap19-citation",
     "IOM 写「IOM 5.x.x」；其余各类按各自编号。**十九类不可混引**。遇到需要 part 110 条文、BAM 方法、IOM Ch.4 抽样表、CPG 520.200/520.300、Import Alert 全文的具体问题，直接转出本包",
     "IOM 按章号写「IOM 5.x.x」或「IOM 4.x.x / IOM Sample Schedule Chart x」（后者自 v4.16 起已收，转 CAP-28）；其余各类按各自编号。**二十类不可混引**。遇到需要 part 110 条文、BAM 方法、CPG 520.200/520.300、Import Alert 全文的具体问题，直接转出本包；**IOM Ch.4 抽样表问题转 CAP-28 而非转出本包**", 1),
    (".cangjie/capabilities/cards/lacf-inspection-program.md", "cap19-b2",
     "）、IOM Chapter 4（Sample Schedule Chart 2）、BAM Ch.13B/14/17/21A/22A–22D",
     "）、BAM Ch.13B/14/17/21A/22A–22D", 1),
    (".cangjie/capabilities/cards/lacf-inspection-program.md", "cap19-b2-tail",
     "不得从 CP 的检查动作反推法条，也不得用 CP 的检查动作替代法规要求。",
     "不得从 CP 的检查动作反推法条，也不得用 CP 的检查动作替代法规要求。**IOM Chapter 4 / Sample Schedule Chart 2 自 v4.16 起已收（第二十来源，见 CAP-28）**，不再属「转引未收」；但 Chart 2 只给取样计划，不给实验室判读。", 1),
    (".cangjie/capabilities/cards/lacf-inspection-program.md", "cap19-b11",
     "IOM 2026 Ch.5「IOM 5.x.x / Exhibit 5-x」；**CP 7303.070「PART x / ATTACHMENT x」**。`21 CFR part 108 / 110 / 120` 与 IOM Ch.4、BAM、CPG、Import Alert 一律标「转引未收」（part 123 已收，写〔§ 123.xxx〕）",
     "IOM 2026 Ch.5「IOM 5.x.x / Exhibit 5-x」、Ch.4「IOM 4.x.x / IOM Sample Schedule Chart x」（自 v4.16 起已收，转 CAP-28）；**CP 7303.070「PART x / ATTACHMENT x」**。`21 CFR part 110` 与 BAM、CPG、Import Alert 一律标「转引未收」（part 108 自 v4.12、part 120 自 v4.13、part 123 自 v4.9 已收）", 1),

    # ══════════════════ CAP-20 lacf-statutory-requirements ══════════════════
    (".cangjie/capabilities/cards/lacf-statutory-requirements.md", "cap20-step6",
     "涉及 part 110 / BAM / IOM Ch.4 / CPG / Import Alert 全文一律标「转引未收」",
     "涉及 part 110 / BAM / CPG / Import Alert 全文一律标「转引未收」（**IOM Ch.4 自 v4.16 起已收，样品形式要件转 CAP-28**）", 1),
    (".cangjie/capabilities/cards/lacf-statutory-requirements.md", "cap20-b10",
     "、BAM / AOAC / MPM 方法正文、IOM Chapter 4 Sample Schedule Chart 2、CPG 全套",
     "、BAM / AOAC / MPM 方法正文、CPG 全套", 1),
    (".cangjie/capabilities/cards/lacf-statutory-requirements.md", "cap20-b10-tail",
     "以及杀菌工艺计算与验证方案审批 —— 均须另行复核或由具备资质的 Process Authority / PCQI 判断。",
     "以及杀菌工艺计算与验证方案审批 —— 均须另行复核或由具备资质的 Process Authority / PCQI 判断。**IOM Chapter 4 Sample Schedule Chart 2 自 v4.16 起已收（见 CAP-28）**，但它是取样计划而非本卡的法条义务。", 1),

    # ══════════════════ CAP-25 emergency-permit-control ══════════════════
    (".cangjie/capabilities/cards/emergency-permit-control.md", "cap25-header",
     "、BAM / AOAC / MPM 方法正文、IOM Ch.4 与 FURLS 系操作系统。",
     "、BAM / AOAC / MPM 方法正文与 FURLS 系操作系统（**IOM Ch.4 自 v4.16 起已收，见 CAP-28**）。", 1),
    (".cangjie/capabilities/cards/emergency-permit-control.md", "cap25-b10",
     "、BAM／AOAC／MPM 方法正文、IOM Chapter 4 Sample Schedule Chart 2、CPG 全套",
     "、BAM／AOAC／MPM 方法正文、CPG 全套", 1),
    (".cangjie/capabilities/cards/emergency-permit-control.md", "cap25-b10-tail",
     "—— 均须另行复核或由具备资质的 Process Authority／PCQI／法规顾问判断。",
     "—— 均须另行复核或由具备资质的 Process Authority／PCQI／法规顾问判断。**IOM Chapter 4 Sample Schedule Chart 2 自 v4.16 起已收（见 CAP-28）**，不属本卡覆盖。", 1),

    # ══════════════════ CAP-21 fsvp-inspection-program ══════════════════
    (".cangjie/capabilities/cards/fsvp-inspection-program.md", "cap21-citation",
     "IOM 写「IOM 5.x.x」。**十九类不可混引**",
     "IOM 按章号写「IOM 5.x.x」或「IOM 4.x.x」（Ch.4 自 v4.16 起已收，转 CAP-28）。**二十类不可混引**", 1),

    # ══════════════════ CAP-26 / CAP-27 ══════════════════
    (".cangjie/capabilities/cards/juice-haccp.md", "cap26-step6",
     "**全包自 v4.15 起十九类不可混引，当前为 27 张能力卡。**",
     "**全包自 v4.16 起二十类不可混引，当前为 28 张能力卡（取样形式要件转 CAP-28）。**", 1),
    (".cangjie/capabilities/cards/juice-haccp.md", "cap26-b10",
     "**十九类不可混引，当前 27 张能力卡。**",
     "**二十类不可混引，当前 28 张能力卡；取样形式要件转 CAP-28。**", 1),
    (".cangjie/capabilities/cards/juice-inspection-program.md", "cap27-step6",
     "**全包自 v4.15 起十九类不可混引，当前为 27 张能力卡。**",
     "**全包自 v4.16 起二十类不可混引，当前为 28 张能力卡；取样形式要件转 CAP-28。**", 1),
    (".cangjie/capabilities/cards/juice-inspection-program.md", "cap27-b10",
     "**十九类不可混引，当前 27 张能力卡。**",
     "**二十类不可混引，当前 28 张能力卡；取样形式要件转 CAP-28。**", 1),

    # ══════════════════ CAP-24 seafood-inspection-program ══════════════════
    (".cangjie/capabilities/cards/seafood-inspection-program.md", "cap24-header",
     "*全包自 v4.15 起「**十九类来源不可混引**」。",
     "*全包自 v4.16 起「**二十类来源不可混引**」。", 1),
    (".cangjie/capabilities/cards/seafood-inspection-program.md", "cap24-uncollected",
     "、21 CFR part 1 subpart L（FSVP 法规）、IOM Chapter 4、FDA 3501 / 3502 表单全文",
     "、21 CFR part 1 subpart L（FSVP 法规）、FDA 3501 / 3502 表单全文", 1),
    (".cangjie/capabilities/cards/seafood-inspection-program.md", "cap24-uncollected-tail",
     "不得从本 CP 反推。本卡与",
     "不得从本 CP 反推（**IOM Chapter 4 自 v4.16 起已收，见 CAP-28**）。本卡与", 1),
    (".cangjie/capabilities/cards/seafood-inspection-program.md", "cap24-b11",
     "全包自 v4.15 起**十九类来源不可混引**：",
     "全包自 v4.16 起**二十类来源不可混引**：", 1),
    (".cangjie/capabilities/cards/seafood-inspection-program.md", "cap24-b11-iom",
     "IOM 用「IOM 5.x.x / Exhibit 5-x」。",
     "IOM 按章号：Ch.5 用「IOM 5.x.x / Exhibit 5-x」、Ch.4 用「IOM 4.x.x / IOM Exhibit 4-xx / IOM Sample Schedule Chart x」（自 v4.16 起已收，转 CAP-28）。", 1),
    (".cangjie/capabilities/cards/seafood-inspection-program.md", "cap24-b12-uncollected",
     "、21 CFR part 1 subpart L、IOM Chapter 4、FDA 3501/3502 表单全文",
     "、21 CFR part 1 subpart L、FDA 3501/3502 表单全文", 1),
    (".cangjie/capabilities/cards/seafood-inspection-program.md", "cap24-b12-tail",
     "FDA–NMFS MOU —— 一律标「转引未收」。",
     "FDA–NMFS MOU —— 一律标「转引未收」（**IOM Chapter 4 自 v4.16 起已收，见 CAP-28**）。", 1),

    # ══════════════════ meta 中的「超范围」intents ══════════════════
    (".cangjie/capabilities/cards/_meta-inspection-sampling.yaml", "meta17-intent",
     "  - 判断哪些问题超出本包（IOM Chapter 4、702(b) 分割留样、eBAM/AOAC/MPM 方法正文、CPG 527.300、SOP-001052、FMD-147）",
     "  - 判断哪些问题超出本包（eBAM/AOAC/MPM 方法正文、CPG 527.300、SOP-001052、FMD-147）；IOM Chapter 4 与 702(b) 分割留样自 v4.16 起已收，转 CAP-28", 1),
    (".cangjie/capabilities/cards/_meta-lacf-inspection-program.yaml", "meta19-intent",
     "  - 判断哪些问题超出本卡（IOM Ch.4 Chart 2、BAM、CPG 520.200/520.300、Import Alert 全文、F0/D/z 与 TD/HP 研究设计）",
     "  - 判断哪些问题超出本卡（BAM、CPG 520.200/520.300、Import Alert 全文、F0/D/z 与 TD/HP 研究设计）；IOM Ch.4 Chart 2 自 v4.16 起已收，转 CAP-28", 1),
    (".cangjie/capabilities/cards/_meta-lacf-statutory-requirements.yaml", "meta20-intent",
     "  - 判断哪些问题超出本卡（part 110/120 正文、F0-D-z 计算、BAM、IOM Ch.4、Import Alert 全文）",
     "  - 判断哪些问题超出本卡（part 110 正文、F0-D-z 计算、BAM、Import Alert 全文）；IOM Ch.4 自 v4.16 起已收，转 CAP-28", 1),
    (".cangjie/capabilities/cards/_meta-seafood-inspection-program.yaml", "meta24-sourcelabel",
     "16-20 / 99-41 全文、21 CFR part 1 subpart L、IOM Chapter 4、FDA 3501 / 3502 表单全文、",
     "16-20 / 99-41 全文、21 CFR part 1 subpart L、FDA 3501 / 3502 表单全文（IOM Chapter 4 自 v4.16 起已收，见 CAP-28）、", 1),
    (".cangjie/capabilities/cards/_meta-emergency-permit-control.yaml", "meta25-sourcelabel",
     "、BAM / AOAC / MPM 方法正文、IOM Ch.4",
     "、BAM / AOAC / MPM 方法正文（IOM Ch.4 自 v4.16 起已收，见 CAP-28）", 1),
]

# 当前态计数替换（仅 cards/ 与 assemble_bundle.py，历史阶梯文档不动）
COUNTED_FILES = sorted(list(C.glob("*.md")) + list(C.glob("_meta-*.yaml"))) + [AB]
COUNT_REPLACEMENTS = [
    ("全包自 v4.15 起十九类", "全包自 v4.16 起二十类"),
    ("自 v4.15 起「**十九类来源", "自 v4.16 起「**二十类来源"),
    ("v4.15 起**十九类", "v4.16 起**二十类"),
    ("十九类", "二十类"),
    ("27 张", "28 张"),
]


def main() -> int:
    apply = "--apply" in sys.argv
    files: dict[Path, str] = {}

    def get(p: Path) -> str:
        if p not in files:
            files[p] = p.read_text(encoding="utf-8")
        return files[p]

    # ① 精确改写
    for rel, label, old, new, want in REWRITES:
        p = BASE / rel
        t = get(p)
        got = t.count(old)
        if got != want:
            print(f"FAIL [{label}] {rel}: old 命中 {got} 次，期望 {want}", file=sys.stderr)
            print(f"     old={old[:120]!r}", file=sys.stderr)
            return 1
        files[p] = t.replace(old, new)
        print(f"OK   [{label}] {rel}")

    # ② 当前态计数替换
    for old, new in COUNT_REPLACEMENTS:
        total = 0
        for p in COUNTED_FILES:
            t = get(p)
            n = t.count(old)
            if n:
                total += n
                files[p] = t.replace(old, new)
        print(f"OK   [count] {old!r} → {new!r} × {total}")

    # ③ 残留自检：IOM Ch.4 / Chapter 4 不应再与「未收」「转引未收」同句
    bad: list[tuple[str, str]] = []
    for p in COUNTED_FILES:
        t = get(p)
        for ln in t.split("\n"):
            if ("IOM Ch.4" in ln or "IOM Chapter 4" in ln or "IOM Chapter 3/4" in ln):
                if ("未收" in ln or "转引未收" in ln) and "已收" not in ln and "不属" not in ln and "v4.16" not in ln:
                    bad.append((p.name, ln[:160]))
    if bad:
        print(f"FAIL 仍有 {len(bad)} 处把 IOM Ch.4 写作未收：", file=sys.stderr)
        for name, ln in bad:
            print(f"  {name}: {ln}", file=sys.stderr)
        return 1
    print("OK   [check] 当前态文件已无「IOM Ch.4 未收」的裸断言")

    # ④ 规模自检
    for p in COUNTED_FILES:
        t = get(p)
        if "十九类" in t or "27 张" in t:
            print(f"FAIL {p.name} 仍有旧计数", file=sys.stderr)
            return 1
    print("OK   [check] cards/ 与 assemble_bundle.py 无「十九类 / 27 张」残留")

    if not apply:
        print(f"\n[dry-run] 涉及 {len(files)} 个文件，未写盘。加 --apply 落地。")
        return 0
    for p, t in files.items():
        p.write_text(t, encoding="utf-8")
    print(f"\n已写盘 {len(files)} 个文件。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())