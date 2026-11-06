#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v4.6 回补：把第十来源 CP 7303.070 的已收状态、十类不可混引、CAP-19 分工
与 RRA 程序性定义同步到既有卡片。每条替换带唯一性断言，失败即中止。"""
from pathlib import Path

BASE = Path("E:/WeChatData/2026-11-04-09-51-05/books/fda-pchf-human-food-guidance")
CARDS = BASE / ".cangjie/capabilities/cards"

# (相对文件名, old, new, 期望命中次数)
R = [

# ---------- cgmp-compliance-guide ----------
("cgmp-compliance-guide.md",
 "v4.5 起全包统一「**九类不可混引**」（本卡之外另有 CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / 过敏原 Ed.5），检查视角分别见 CAP-16 / CAP-17 / CAP-18。",
 "v4.6 起全包统一「**十类不可混引**」（本卡之外另有 CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / 过敏原 Ed.5），检查视角分别见 CAP-16 / CAP-17 / CAP-18 / CAP-19；低酸/酸化罐头与 Part 117 的管辖分流另见 CAP-19 `lacf-inspection-program`。", 1),
("cgmp-compliance-guide.md",
 "其他 Compliance Programs（7303.878 FSVP、7303.080 Produce Safety、7303.070 低酸/酸化、7304.019 等）、",
 "其他 Compliance Programs（7303.878 FSVP、7303.080 Produce Safety、7304.019 等；**7303.070 低酸/酸化已由 CAP-19 收入**，但只给管辖分流与检查员取证口径，其依据的 21 CFR part 108/113/114 正文仍未收）、", 1),
("cgmp-compliance-guide.md",
 "；IOM 用「IOM 5.x.x / IOM Exhibit 5-x」。九类**不可混引**",
 "；IOM 用「IOM 5.x.x / IOM Exhibit 5-x」；CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」，其 21 CFR part 108/113/114 引用一律标「转引未收」。十类**不可混引**", 1),
("cgmp-compliance-guide.md",
 "本卡只提供 FDA 口径，跨体系映射需人工判断。",
 "本卡只提供 FDA 口径，跨体系映射需人工判断。**低酸罐头 / 酸化食品与 Part 117 的具体管辖分流（〔§ 117.5(d)(1)(2)〕、〔§ 117.1(c)〕、Keep Refrigerated 路由、酸化食品不免 Subparts C/G）见 CAP-19 `lacf-inspection-program`**；注意〔§ 117.201〕是 qualified facility 的 modified requirements，不是 LACF 条款。", 1),

# ---------- defect-action-levels ----------
("defect-action-levels.md",
 "**B4 — 检查员视角已补三卡，方法与制样仍缺。**",
 "**B4 — 检查员视角已补四卡，方法与制样仍缺。**", 1),
("defect-action-levels.md",
 "；本卡则给**阈值出处与义务边界**。",
 "；**第十来源 CP 7303.070（2024 签发 / 2025-09-26 更正）已收**，见 CAP-19 `lacf-inspection-program`：给 LACF/AF 管辖分流、酸化判定三步、pH/aw 实验室判读与 Import Alert 升级；本卡则给**阈值出处与义务边界**。", 1),
("defect-action-levels.md",
 "其他 Compliance Programs（7303.878 / 7303.080 / 7303.070）、",
 "其他 Compliance Programs（7303.878 / 7303.080 / 7304.019 等；7303.070 已由 CAP-19 收入、其 108/113/114 法源正文仍未收）、", 1),
("defect-action-levels.md",
 "**九类不可混引**（CPGM 7303.040 用「CPGM 7303.040 PART x」、CP 7303.050 用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」、IOM 用「IOM 5.x.x」标注）",
 "**十类不可混引**（CPGM 7303.040 用「CPGM 7303.040 PART x」、CP 7303.050 用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」、IOM 用「IOM 5.x.x」、CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」标注）", 1),

# ---------- inspection-readiness ----------
("inspection-readiness.md",
 "v4.5 起再加 CP 7303.050 与 IOM 2026 Ch.5，全包统一「**九类不可混引**」。",
 "v4.5 起再加 CP 7303.050 与 IOM 2026 Ch.5，v4.6 起再加 CP 7303.070，全包统一「**十类不可混引**」。", 1),
("inspection-readiness.md",
 "三卡构成完整的迎检链，勿把后两卡的内容当成本卡缺失。",
 "四卡构成完整的迎检链（低酸/酸化罐头 program 的管辖分流与专门取证转 **CAP-19 `lacf-inspection-program`**，CP 7303.070），勿把后三卡的内容当成本卡缺失。", 1),
("inspection-readiness.md",
 "不得写成「FDA 从不预告」或「境外一律无预告」。",
 "不得写成「FDA 从不预告」或「境外一律无预告」。v4.6 补入的 **CP 7303.070 PART II.2.B(2)** 另给出 RRA 的官方程序性定义：自愿、全程远程、`RRAs are not considered inspections`、不满足 FD&C Act 704 条要求现场 inspection 的法定场景（510(h)/503B(b)）；可据此回答「RRA 算不算检查」，但**不得**据此推导 FDA 的 RRA 适用政策或替换 IOM 5.2.7 口径，详见 `lacf-inspection-program`。", 1),
("inspection-readiness.md",
 "→ 政策层提示 + 明确本包未收原文，须复核现行版本。",
 "→ 政策层提示 + CP 7303.070 PART II.2.B(2) 的 RRA 程序性定义 + 明确 FDA 政策公告原文仍未收，须复核现行版本。", 1),
("inspection-readiness.md",
 "**B5 — 迎检三卡的分工与仍缺的文件（本卡无法替代）。**",
 "**B5 — 迎检四卡的分工与仍缺的文件（本卡无法替代）。**", 1),
("inspection-readiness.md",
 "**IOM 2026 Chapter 5**（221 页）全文（CAP-18，给权限、表单、483 措辞纪律与证据链）。",
 "**IOM 2026 Chapter 5**（221 页）全文（CAP-18，给权限、表单、483 措辞纪律与证据链）；**CP 7303.070**（2024 签发 / 2025-09-26 更正，61 页）全文（CAP-19，给 LACF/AF 管辖分流、酸化判定、FCE/SID 与 Process Authority 取证、pH/aw 实验室判读、Import 升级）。", 1),
("inspection-readiness.md",
 "其他 Compliance Programs（7303.878 FSVP、7303.080 Produce Safety、7303.070 低酸/酸化、7304.019 等）、",
 "其他 Compliance Programs（7303.878 FSVP、7303.080 Produce Safety、7304.019 / 7303.842 / 7371.000 / 7321.006 等；**7303.070 已由 CAP-19 收入**）、", 1),
("inspection-readiness.md",
 "但除 **7303.050 已收（CAP-17）** 外，本包没有其余这些 program 的正文；",
 "但除 **7303.050 已收（CAP-17）** 与 **7303.070 已收（CAP-19 `lacf-inspection-program`；其依据的 21 CFR part 108/113/114 正文仍未收）** 外，本包没有其余这些 program 的正文；", 1),
("inspection-readiness.md",
 "；IOM 用「IOM 5.x.x / IOM Exhibit 5-x」。**九类不可混引**；本卡与 CAP-17 / CAP-18 的内容须按此分源引用。",
 "；IOM 用「IOM 5.x.x / IOM Exhibit 5-x」；CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」。**十类不可混引**；本卡与 CAP-17 / CAP-18 / CAP-19 的内容须按此分源引用。", 1),
("inspection-readiness.md",
 "v4.5 补入的 IOM 5.2.7 正文则明确：食品企业检查一般不宜预告（program division 裁量）、境外检查通常提前告知、国内预告一般不少于 5 个日历日、预告不是预约；境外检查一般不签发 FDA 482 但仍须出示证件。引用这些须标「IOM 5.2.7 / 5.1.4.2.1」，政策层部分仍须核对 FDA 现行公告。",
 "v4.5 补入的 IOM 5.2.7 正文则明确：食品企业检查一般不宜预告（program division 裁量）、境外检查通常提前告知、国内预告一般不少于 5 个日历日、预告不是预约；境外检查一般不签发 FDA 482 但仍须出示证件。v4.6 补入的 CP 7303.070 PART II.2.B(2) 明确 RRA 自愿、远程、`RRAs are not considered inspections` 且不满足 704 条法定检查场景——**RRA 可替代监督动作，不能替代法定检查**。引用这些须标「IOM 5.2.7 / 5.1.4.2.1」与「CP 7303.070 PART II.2.B(2)」，FDA 政策公告层部分仍须核对现行公告。", 1),
("inspection-readiness.md",
 "2025 年境外无预告检查扩张、RRA、704(a)(4) 检查前索取记录属**政策层且 FDA 公告原文未收**，只作准备原则提示，须核对 FDA 当前公告，不得写成条款级结论。",
 "2025 年境外无预告检查扩张、RRA 适用范围、704(a)(4) 检查前索取记录属**政策层且 FDA 公告原文未收**，只作准备原则提示，须核对 FDA 当前公告，不得写成条款级结论；例外是 CP 7303.070 PART II.2.B(2) 已给 RRA 的程序性定义（不是 inspection、不满足 510(h)/503B(b)），该段可作条款级引用，详见 CAP-19 `lacf-inspection-program` B5。", 1),

# ---------- inspection-sampling ----------
("inspection-sampling.md",
 "与 PCHF 指南、L.mono 指南、SECG、Ed.5、Handbook、CPGM 7303.040 合计**九类不可混引**。",
 "与 PCHF 指南、L.mono 指南、SECG、Ed.5、Handbook、CPGM 7303.040、IOM 2026 Ch.5、CP 7303.070 合计**十类不可混引**。⚠ CP 7303.070 PART II.2.C(2) 把标 `Keep Refrigerated` 的产品（免 21 CFR 113/114）路由到本 program，分流细节见 CAP-19 `lacf-inspection-program`。", 1),
("inspection-sampling.md",
 "**B10 — 引用规范（九类不可混引）。**",
 "**B10 — 引用规范（十类不可混引）。**", 1),
("inspection-sampling.md",
 "**IOM 用「IOM 5.x.x」**。九类不可混引；",
 "**IOM 用「IOM 5.x.x」**；**CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」**。十类不可混引；", 1),

# ---------- investigator-authority-procedure ----------
("investigator-authority-procedure.md",
 "与 PCHF 指南、L.mono 指南、SECG、Ed.5、Handbook、CPGM 7303.040、CP 7303.050 合计**九类不可混引**。",
 "与 PCHF 指南、L.mono 指南、SECG、Ed.5、Handbook、CPGM 7303.040、CP 7303.050、CP 7303.070 合计**十类不可混引**。⚠ CP 7303.070 PART II.2.B(2) 补上 RRA 的官方程序性定义（`RRAs are not considered inspections`），见 CAP-19 `lacf-inspection-program`；它不改变 IOM 5.2.7 的预告三层口径。", 1),
("investigator-authority-procedure.md",
 "**B10 — 引用规范（九类不可混引）。**",
 "**B10 — 引用规范（十类不可混引）。**", 1),
("investigator-authority-procedure.md",
 "**IOM 用「IOM 5.x.x」或「IOM Exhibit 5-x」**。九类不可混引；",
 "**IOM 用「IOM 5.x.x」或「IOM Exhibit 5-x」**；**CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」**。十类不可混引；", 1),
("investigator-authority-procedure.md",
 "→ 政策层提示，明确 FDA 公告原文未收，须复核现行版本。",
 "→ 政策层提示 + CP 7303.070 PART II.2.B(2) 的 RRA 程序性定义（不是 inspection、不满足 510(h)/503B(b)），仍明确 FDA 政策公告原文未收、须复核现行版本。", 1),
("investigator-authority-procedure.md",
 "不得写成「FDA 从不预告」「境外一律无预告」「无预告检查有法定 5 天例外」。",
 "不得写成「FDA 从不预告」「境外一律无预告」「无预告检查有法定 5 天例外」。CP 7303.070 PART II.2.B(2) 另可回答「RRA 算不算检查」——不算，且不满足 704 条法定检查场景；但该段不是 FDA 的 RRA 适用政策原文。", 1),

# ---------- regulatory-boundaries ----------
("regulatory-boundaries.md",
 "引用分别用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」与「IOM 5.x.x」，全包九类不可混引。详见 CAP-17 / CAP-18。",
 "引用分别用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」与「IOM 5.x.x」，全包十类不可混引。详见 CAP-17 / CAP-18 / CAP-19。\n10. **v4.6 补入 CP 7303.070，把本卡第 1 条的双法规并集落到检查员侧**：CP PART II.2.C(1) 与法规正文一致地写明，LACF 产品受 Part 117 约束，但〔§ 117.5(d)(1)〕豁免 Subparts C/G **仅限 part 113 覆盖的活动**，〔§ 117.5(d)(2)〕进一步限定**仅限 part 113 管辖的微生物危害**；未被热处理控制且需预防控制的危害（`Staphylococcus aureus` 生长产毒、化学、物理）仍归 Subparts C/G。⚠ **酸化食品不在该豁免内**：CP 原文 `Acidified foods are subject to the CGMP & PCHF rule`，PCHF 覆盖转 7303.040，检查重点仍在 21 CFR part 108/114；**〔§ 117.201〕是 qualified facility 的 modified requirements，不是 LACF 条款**。CP PART II.2.C(2) 另给 `Keep Refrigerated` 免 113/114 → 7303.050、brites 中央仓 → `PAC 03040` 两条路由。21 CFR part 108/113/114 正文本包未收，CP 内相关表述一律标「转引未收」；完整判定见 CAP-19 `lacf-inspection-program`。", 1),
("regulatory-boundaries.md",
 "1. **按危害类别拆分法规适用性**——LACF（低酸罐装食品）的生物危害由 part 113 专门体系管，PCHF 豁免；但同一产品的化学/物理危害 PCHF 仍适用。",
 "1. **按危害类别拆分法规适用性**——LACF（低酸罐装食品）的生物危害由 part 113 专门体系管，〔§ 117.5(d)(1)(2)〕据此免其 Subparts C/G 且**仅限 part 113 管辖的微生物危害**；但同一产品的化学/物理危害、以及未被热处理控制的金葡生长产毒 PCHF 仍适用（CP 7303.070 PART II.2.C(1) 逐字确认，见 B10）。", 1),

# ---------- reference-tools-discipline ----------
("reference-tools-discipline.md",
 "完整判定见 `inspection-sampling`（CAP-17）与 `investigator-authority-procedure`（CAP-18）。\n\n---",
 "完整判定见 `inspection-sampling`（CAP-17）与 `investigator-authority-procedure`（CAP-18）。\n12. **CP 7303.070 是第十类资料，同样不在效力栈内**：现行件为 2024-09-26 签发 / 2025-09-26 更正（文件名 20250929 只是生成日），是 FDA 给检查员、实验室分析员与合规官的**低酸/酸化罐头专门体系作业指导**。用它只能回答「LACF/AF 走哪条 program、检查员查哪些记录、什么数值触发升级」，不能回答「我是否合规」——后者回〔§ 117.5(d)(1)(2)〕〔§ 117.1(c)〕与 21 CFR part 108/113/114（**三套正文未收**）。⚠ 三类数字不可互替：4.6/0.85 是法定边界，4.40/4.65/4.75、0.90/0.93、异常罐 1%、24 罐/12 罐是 CP 的实验室与取证触发线，≤4.4/≤0.92 是 L.mono 草案抑制型配方基准。`Acidified foods are subject to the CGMP & PCHF rule`——**不得把 AF 一并免掉 Subparts C/G**；也不要把〔§ 117.201〕误当 LACF 条款。完整判定见 `lacf-inspection-program`（CAP-19）。\n\n---", 1),

# ---------- process-control-validation ----------
("process-control-validation.md",
 "> - **二者用途不同、不得互相替换或合并**。",
 "> - **第三套数字（CP 7303.070 PART IV.2，检查员作业口径）**：pH **4.40 / 4.65** 是实验室第二分析师复测与扩测触发线、**4.75** 是异常罐肉毒毒素/PCR 触发线、aw **0.90 / 0.93** 是 aw 筛查复测触发线，`Never average the two analysts' results together`。它们既不是法定边界，也不是配方设计基准，**不得与前两套互相替换**；详见 CAP-19 `lacf-inspection-program`。\n> - **二者用途不同、不得互相替换或合并**。", 1),
]

changed = {}
for name, old, new, expected in R:
    p = CARDS / name
    s = p.read_text(encoding="utf-8")
    n = s.count(old)
    assert n == expected, f"{name}: expected {expected} hit(s), got {n} for {old[:80]!r}"
    s = s.replace(old, new, expected)
    p.write_text(s, encoding="utf-8")
    changed[name] = changed.get(name, 0) + 1

for k, v in sorted(changed.items()):
    print(f"  {k}: {v} 处")
print(f"完成：{len(R)} 条替换，覆盖 {len(changed)} 张既有卡")
