"""v4.9 口径残留回补（第二批）：十三类 → 十四类 + Part 123 已收。

第一批（apply_v4_9_revisions.py）只处理了 SLUGS / ALSO_READ / 卡片里字面的
「十三类」。全库扫描后发现两类更实质的残留：

A. 版本演进被 v4.8 的批量替换污染成事实错误：
   v4.7 原文「v4.7 起十二类不可混引：三套法规正文 + 九类 = 12」被无差别
   替换成「十三类」，出现「十三类：列 12 项」的自相矛盾。这类按 v4.7 当年
   口径复原为十二类，并补上完整的版本阶梯。

B. Part 123 已收但多处仍标「未收」：
   8 张卡 + 3 份 meta + verified.yaml + overview/glossary/test-prompts 里
   还有「21 CFR part 108 / 110 / 120 / 123 仍未收」。CAP-22 已经在按
   〔§ 123.xxx〕给义务，同包内自相矛盾，必须改。

判定原则（沿用 v4.8 同类处理）：
- 明确版本限定的陈述（v4.6 / v4.7 / v4.8 节、changelog 的 [x] 行）保留原数字，
  但数字必须对该版本成立；
- 描述当前状态的标题、tags、expected_behavior、引用规范段，一律同步到 v4.9。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(".")
CJ = ROOT / ".cangjie"
CARDS = CJ / "capabilities/cards"
CAP = CJ / "capabilities"

_pending: dict[Path, str] = {}
ERRORS: list[str] = []


def load(p: Path) -> str:
    return _pending.get(p) or p.read_text(encoding="utf-8")


def rep(p: Path, old: str, new: str, n: int | None = 1, label: str = "") -> None:
    """n 为期望命中数；给 None 表示「替换全部出现」，但会打印实际数量。

    命中数不符只记入 ERRORS 并跳过，便于一次性拿到全部真实计数
    （flush 在最后执行，任何 ERRORS 都会中止落盘，因此仍然原子）。
    """
    t = load(p)
    c = t.count(old)
    if n is None:
        if c == 0:
            ERRORS.append(f"{p}: [{label}] expected >=1 hit, got 0 for {old[:70]!r}")
            return
        print(f"    · {label}: {c} hit(s) (replace-all)")
        _pending[p] = t.replace(old, new)
        return
    if c != n:
        ERRORS.append(f"{p}: [{label}] expected {n} hit(s), got {c} for {old[:70]!r}")
        return
    _pending[p] = t.replace(old, new)


def flush() -> None:
    for p, t in _pending.items():
        p.write_text(t, encoding="utf-8")
        print(f"  wrote {p} ({len(t)} chars)")
    _pending.clear()


# ---------------------------------------------------------------- glossary ×3
GLOSSARY = [ROOT / "GLOSSARY.md", ROOT / "candidates/glossary.md", CAP / "book/glossary.md"]

GLOSSARY_EDITS = [
    # t135 tags（CP 7303.070，版本陷阱）
    ("tags: [CP 7303.070, 版本陷阱, 更正本, PAC, PAF, 十三类不可混引]",
     "tags: [CP 7303.070, 版本陷阱, 更正本, PAC, PAF, 十四类不可混引]",
     "t135 tags"),
    # t142 标题
    ("title: RRA 程序性定义、Keep Refrigerated / brites 路由与十三类不可混引（v4.7 更新）",
     "title: RRA 程序性定义、Keep Refrigerated / brites 路由与十四类不可混引（v4.7 定稿 / v4.9 口径）",
     "t142 title"),
    # t142 summary：阶梯收口 + 剔掉 part 123（已收）
    ("全包口径为 v4.6 十类 → v4.7 十二类 → **v4.8 十三类不可混引**。仍未收：21 CFR part 108（FCE/SID/Emergency Permit）、**part 110（旧 CGMP，至今有效但正文未收）**、part 120 / 123、IOM Ch.4 Chart 2",
     "全包口径为 v4.6 十类 → v4.7 十二类 → v4.8 十三类 → **v4.9 十四类不可混引**。仍未收：21 CFR part 108（FCE/SID/Emergency Permit）、**part 110（旧 CGMP，至今有效但正文未收）**、part 120（**part 123 自 v4.9 起已收，见 CAP-22**）、IOM Ch.4 Chart 2",
     "t142 summary"),
    ("tags: [RRA, Keep Refrigerated, brites, 7303.050, 7303.040, 十三类不可混引, 收录边界, v4.6, v4.7]",
     "tags: [RRA, Keep Refrigerated, brites, 7303.050, 7303.040, 十四类不可混引, 收录边界, v4.6, v4.7]",
     "t142 tags"),
    # t151 三套 / 四套
    ("v4.7 起本包有三套独立编号的法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕，彼此并行",
     "v4.7 起本包有三套独立编号的法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕（**v4.9 增为四套：加〔§ 123.xxx〕，见 CAP-22**），彼此并行",
     "t151 summary"),
    ("tags: [117.1(c), 并行适用, 三套法规正文, LACF, 酸化食品, v4.7]",
     "tags: [117.1(c), 并行适用, 四套法规正文, LACF, 酸化食品, v4.7]",
     "t151 tags"),
    # t152 标题
    ("title: Shall / Should 的法定语义、4-1-25 Edition 版次与十三类不可混引",
     "title: Shall / Should 的法定语义、4-1-25 Edition 版次与十四类不可混引",
     "t152 title"),
    # t152 summary：复原 v4.7 的十二类（原清单确实只有 12 项）
    ("v4.7 起**十三类不可混引**：三套法规正文",
     "v4.7 起**十二类不可混引**（v4.8 增至十三类、v4.9 增至十四类）：三套法规正文",
     "t152 summary"),
    ("tags: [shall, should, 4-1-25 Edition, FR citation, 双栏转换, 十三类不可混引, v4.7]",
     "tags: [shall, should, 4-1-25 Edition, FR citation, 双栏转换, 十四类不可混引, v4.7]",
     "t152 tags"),
    # t162 标题
    ("title: CP 7303.878 版本口径、CP 7303.819 状态与十三类不可混引",
     "title: CP 7303.878 版本口径、CP 7303.819 状态与十四类不可混引",
     "t162 title"),
    # t162 summary：三套 → 四套，并写清 v4.8/v4.9 两段
    ("全包自 v4.8 起为**十三类不可混引**：三套法规正文〔§ 117/113/114.xxx〕",
     "全包自 v4.8 起十三类、**v4.9 起十四类不可混引**：四套法规正文〔§ 117/113/114/123.xxx〕",
     "t162 summary"),
    ("tags: [7303.878, 版本陷阱, 7303.819, 十三类不可混引, 收录边界, v4.8]",
     "tags: [7303.878, 版本陷阱, 7303.819, 十四类不可混引, 收录边界, v4.8]",
     "t162 tags"),
    # 自检记录里的 v4.7 条目：复原十二类
    ("shall/should 与十三类不可混引）；引文全部取自 CAP-20 R 段",
     "shall/should 与十二类不可混引）；引文全部取自 CAP-20 R 段",
     "selftest v4.7"),
]

for g in GLOSSARY:
    for old, new, label in GLOSSARY_EDITS:
        rep(g, old, new, 1, label)
print(f"glossary: 3 份 × {len(GLOSSARY_EDITS)} 处")


# --------------------------------------------------------------------- cards
C = CARDS

# lacf-inspection-program
rep(C / "lacf-inspection-program.md",
    "**21 CFR part 108 / 110 / 120 / 123 正文本包仍未收**，一律标「转引未收」",
    "**21 CFR part 108 / 110 / 120 正文本包仍未收**（**part 123 自 v4.9 起已收，见 CAP-22 `seafood-haccp-statutory-requirements`**），一律标「转引未收」",
    label="lacf-inspection 来源分层")
rep(C / "lacf-inspection-program.md",
    "**v4.7 起 part 113 / 114 正文已收（转 CAP-20 `lacf-statutory-requirements`），但 part 108 / 110 / 120 / 123 仍未收**",
    "**v4.7 起 part 113 / 114 正文已收（转 CAP-20 `lacf-statutory-requirements`）、v4.9 起 part 123 已收（转 CAP-22 `seafood-haccp-statutory-requirements`），但 part 108 / 110 / 120 仍未收**",
    label="lacf-inspection A1")
rep(C / "lacf-inspection-program.md",
    "`21 CFR part 108 / 110 / 120 / 123` 只能写「转引未收」",
    "`21 CFR part 108 / 110 / 120` 只能写「转引未收」（part 123 已收，写〔§ 123.xxx〕转 CAP-22）",
    label="lacf-inspection E")
rep(C / "lacf-inspection-program.md",
    "**B2 — 21 CFR Part 113 / 114 正文已收（v4.7），part 108 / 110 / 120 / 123 仍未收。**",
    "**B2 — 21 CFR Part 113 / 114 正文已收（v4.7）、part 123 已收（v4.9，CAP-22），part 108 / 110 / 120 仍未收。**",
    label="lacf-inspection B2")
rep(C / "lacf-inspection-program.md",
    "part 120 / 123（果汁/海产品 HACCP）",
    "part 120（果汁 HACCP）",
    label="lacf-inspection B2 list")
rep(C / "lacf-inspection-program.md",
    "**B11 — 引用规范（十四类不可混引，v4.8）。** 法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕；",
    "**B11 — 引用规范（十四类不可混引，v4.9）。** 法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 123.xxx〕；",
    label="lacf-inspection B11")

# lacf-statutory-requirements
rep(C / "lacf-statutory-requirements.md",
    '自此「法规正文层」含 Part 117 / 113 / 114 三套独立编号。',
    '自此「法规正文层」含 Part 117 / 113 / 114 三套独立编号（**v4.9 增为四套：加 Part 123〔§ 123.xxx〕，见 CAP-22 `seafood-haccp-statutory-requirements`**）。',
    label="lacf-stat 分层")
rep(C / "lacf-statutory-requirements.md",
    "但两份正文本包未收（用户已下载但本版未纳入），只给接口不展开。",
    "但 part 120 正文本包未收、**part 123 自 v4.9 起已收（见 CAP-22）**，后者给条款、前者只给接口不展开。",
    label="lacf-stat A2-18")
rep(C / "lacf-statutory-requirements.md",
    "涉及 part 108 / part 110 / part 120 / part 123 / BAM / IOM Ch.4 / CPG / Import Alert 全文一律标「转引未收」",
    "涉及 part 108 / part 110 / part 120 / BAM / IOM Ch.4 / CPG / Import Alert 全文一律标「转引未收」（part 123 已收，写〔§ 123.xxx〕）",
    label="lacf-stat Step6")
rep(C / "lacf-statutory-requirements.md",
    "用户已下载的 `CFR-2025-title21-vol2-part120.pdf` / `part123.pdf` 正文本版亦未纳入。",
    "用户已下载的 `CFR-2025-title21-vol2-part123.pdf` 已于 v4.9 纳入（见 CAP-22）；`part120.pdf` 正文本版仍未纳入。",
    label="lacf-stat B1")
rep(C / "lacf-statutory-requirements.md",
    "〔§ 117.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕三套法条各自独立；",
    "〔§ 117.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕/〔§ 123.xxx〕四套法条各自独立；",
    label="lacf-stat B8")
rep(C / "lacf-statutory-requirements.md",
    "**B10 — 本卡不覆盖的内容。** 21 CFR part 108 / 110 / 120 / 123 正文、",
    "**B10 — 本卡不覆盖的内容。** 21 CFR part 108 / 110 / 120 正文（part 123 见 CAP-22）、",
    label="lacf-stat B10")

# cgmp-compliance-guide
rep(C / "cgmp-compliance-guide.md",
    "**part 108（FCE/SID/Emergency Permit）、part 110（旧 CGMP，含 §110.110）、part 120 / 123 正文仍未收**",
    "**part 108（FCE/SID/Emergency Permit）、part 110（旧 CGMP，含 §110.110）、part 120 正文仍未收**（**part 123 自 v4.9 起已收，见 CAP-22**），且 **21 CFR Part 123 与〔§ 117.5(b)〕的接口只给结论不展开**",
    label="cgmp 未收段")
rep(C / "cgmp-compliance-guide.md",
    "法规用〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕（三套独立编号）",
    "法规用〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 123.xxx〕（四套独立编号）",
    label="cgmp B8")

# defect-action-levels
rep(C / "defect-action-levels.md",
    "**B4 — 检查员视角已补四卡，法规正文层已扩为三套，方法与制样仍缺。**",
    "**B4 — 检查员视角已补四卡，法规正文层已扩为四套，方法与制样仍缺。**",
    label="defect B4 标题")
rep(C / "defect-action-levels.md",
    "给企业法定义务与〔§ 117.1(c)〕〔§ 117.5(d)〕接口。本卡则给**阈值出处与义务边界**。",
    "给企业法定义务与〔§ 117.1(c)〕〔§ 117.5(d)〕接口；**第十四来源 21 CFR Part 123（Fish and Fishery Products，4-1-25 Edition）已收**，见 CAP-22 `seafood-haccp-statutory-requirements`：给海产品 HACCP 义务、〔§ 117.5(b)〕双向锁定与与 FSVP 的分轨。本卡则给**阈值出处与义务边界**。",
    label="defect B4 第十四来源")
rep(C / "defect-action-levels.md",
    "**仍未收**：21 CFR part 108 / 110 / 120 / 123 正文、",
    "**仍未收**：21 CFR part 108 / 110 / 120 正文（part 123 自 v4.9 起已收）、",
    label="defect B4 未收")

# inspection-sampling
rep(C / "inspection-sampling.md",
    "**B10 — 引用规范（十四类不可混引，v4.8）。** 法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕；",
    "**B10 — 引用规范（十四类不可混引，v4.9）。** 法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 123.xxx〕；",
    label="sampling B10 头")
rep(C / "inspection-sampling.md",
    "十四类不可混引；21 CFR part 108 / 110 / 120 / 123 正文未收，标「转引未收」；",
    "十四类不可混引；21 CFR part 108 / 110 / 120 正文未收，标「转引未收」（part 123 已收，写〔§ 123.xxx〕）；",
    label="sampling B10 尾")

# reference-tools-discipline
rep(C / "reference-tools-discipline.md",
    "**21 CFR part 108 / 110 / 120 / 123 正文仍未收**。",
    "**21 CFR part 108 / 110 / 120 正文仍未收**（part 123 自 v4.9 起已收，见 CAP-22）。",
    label="reference-tools 12")

# regulatory-boundaries
rep(C / "regulatory-boundaries.md",
    "自此「法规正文层」含 Part 117 / 113 / 114 三套独立编号",
    "自此「法规正文层」含 Part 117 / 113 / 114 三套独立编号（**v4.9 增为四套：加 Part 123，见 CAP-22**）",
    label="reg-bound 三套→四套")
rep(C / "regulatory-boundaries.md",
    "**仍未收**：21 CFR part 108 / 110 / 120 / 123 正文，",
    "**仍未收**：21 CFR part 108 / 110 / 120 正文（part 123 自 v4.9 起已收），",
    label="reg-bound 未收")

# inspection-readiness
rep(C / "inspection-readiness.md",
    "但 **part 108（FCE/SID/Emergency Permit）、part 110、part 120 / 123 正文仍未收**。",
    "但 **part 108（FCE/SID/Emergency Permit）、part 110、part 120 正文仍未收**（part 123 自 v4.9 起已收，见 CAP-22）。",
    label="readiness B10")
rep(C / "inspection-readiness.md",
    "法规正文用〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕三套独立编号；",
    "法规正文用〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 123.xxx〕四套独立编号；",
    label="readiness B12")

# fsvp-inspection-program
rep(C / "fsvp-inspection-program.md",
    "> —— PART I.2；**part 120 / 123 正文本包未收，转引未收**",
    "> —— PART I.2；**part 120 正文本包未收（标「转引未收」）、part 123 自 v4.9 起已收（见 CAP-22）**",
    label="fsvp R")
rep(C / "fsvp-inspection-program.md",
    "本卡（part 120/123 转引未收）",
    "本卡（part 120 转引未收；part 123 见 CAP-22）",
    label="fsvp 表格")
rep(C / "fsvp-inspection-program.md",
    "21 CFR part 111 / 112 / 120 / 123 / 507 正文",
    "21 CFR part 111 / 112 / 120 / 507 正文（part 123 已收，见 CAP-22）",
    label="fsvp B12")

# --------------------------------------------------------------- meta yaml
rep(C / "_meta-fsvp-inspection-program.yaml",
    "- 列出 §1.501(b)–(h) 的八类 FSVP 豁免并指出 part 120 / 123 正文未收",
    "- 列出 §1.501(b)–(h) 的八类 FSVP 豁免并指出 part 120 正文未收（part 123 自 v4.9 起已收）",
    label="meta-fsvp intent")
rep(C / "_meta-fsvp-inspection-program.yaml",
    "part 111/112/120/123/507 正文",
    "part 111/112/120/507 正文（part 123 已收）",
    label="meta-fsvp out_of_scope")
rep(C / "_meta-fsvp-inspection-program.yaml",
    "  - 十三类不可混引",
    "  - 十四类不可混引",
    label="meta-fsvp keyword")

rep(C / "_meta-lacf-inspection-program.yaml",
    "+ 21 CFR part 108 / 110 / 120 / 123（转引未收）",
    "+ 21 CFR part 108 / 110 / 120（转引未收）+ 21 CFR Part 123（v4.9 已收，见 CAP-22）",
    label="meta-lacf-insp label")

rep(C / "_meta-lacf-statutory-requirements.yaml",
    "part 108 的 FCE/SID/Emergency Permit、part 110/120/123 正文",
    "part 108 的 FCE/SID/Emergency Permit、part 110/120 正文（part 123 自 v4.9 起已收）",
    label="meta-lacf-stat out_of_scope")
rep(C / "_meta-lacf-statutory-requirements.yaml",
    "21 CFR part 108 / 110 / 120 / 123 正文一律「转引未收」",
    "21 CFR part 108 / 110 / 120 正文一律「转引未收」（part 123 自 v4.9 起已收，见 CAP-22）",
    label="meta-lacf-stat label")
print("cards + meta: done")


# -------------------------------------------------------------- verified.yaml
V = CAP / "verified.yaml"
rep(V, "part 110 / 120 / 123、IOM Ch.4 Sample",
    "part 110 / 120（part 123 自 v4.9 起已收，见 CAP-22）、IOM Ch.4 Sample",
    n=2, label="v 105×2")
rep(V, "part 110\n    / 120 / 123，一律标「转引未收」",
    "part 110\n    / 120（part 123 自 v4.9 起已收，见 CAP-22），一律标「转引未收」",
    label="v 257")
rep(V, "+ 21 CFR part 108 / 110 / 120 / 123（转引未收）+",
    "+ 21 CFR part 108 / 110 / 120（转引未收）+ 21 CFR Part 123（v4.9 已收，见 CAP-22）+",
    n=2, label="v 1895/1907")
# 2072 与 2084 是同一句话的两种折行形态：先处理带「21 」的整行，再处理被折到下一行的。
rep(V, "；21 CFR part 108 / 110 / 120 / 123 正文一律「转引未收」；来源定位见卡片 R 段）",
    "；21 CFR part 108 / 110 / 120 正文一律「转引未收」（part 123 自 v4.9 起已收，见 CAP-22）；来源定位见卡片 R 段）",
    label="v 2072")
rep(V, "CFR part 108 / 110 / 120 / 123 正文一律「转引未收」",
    "CFR part 108 / 110 / 120 正文一律「转引未收」（part 123 自 v4.9 起已收，见 CAP-22）",
    label="v 2084 折行")
rep(V, "- 列出 §1.501(b)–(h) 的八类 FSVP 豁免并指出 part 120 / 123 正文未收",
    "- 列出 §1.501(b)–(h) 的八类 FSVP 豁免并指出 part 120 正文未收（part 123 自 v4.9 起已收）",
    label="v 2116")
rep(V, "21 CFR part 1 subpart L / 108 / 110 / 120 / 123、IOM Chapter 4",
    "21 CFR part 1 subpart L / 108 / 110 / 120、IOM Chapter 4（part 123 自 v4.9 起已收）",
    label="v 305")
rep(V, "  - 十三类不可混引", "  - 十四类不可混引", label="v 2252")
rep(V, "- 三套法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕各自独立编号",
    "- 四套法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 123.xxx〕各自独立编号",
    label="v 266")
rep(V, "三套法规正文分别以〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕标注",
    "四套法规正文分别以〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 123.xxx〕标注",
    label="v 301")


# ----------------------------------------------------------------- overview ×2
OVERVIEW = [ROOT / "BOOK_OVERVIEW.md", CAP / "book/overview.md"]
OV_EDITS = [
    ("以及 part 110（至今有效但正文未收）、part 120 / 123。",
     "以及 part 110（至今有效但正文未收）、part 120（**part 123 自 v4.9 起已收，见 CAP-22**）。",
     "ov 215"),
    ("**v4.8 起扩为「十三类不可混引」**（新增 CP 7303.878 检查程序，见文末节）；21 CFR part 108 / 110 / 120 / 123、IOM Ch.4",
     "v4.8 扩为「十三类不可混引」（新增 CP 7303.878 检查程序）、**v4.9 起扩为「十四类不可混引」**（新增 21 CFR Part 123 法规正文，见文末节）；21 CFR part 108 / 110 / 120、IOM Ch.4",
     "ov 217 阶梯"),
    ("21 CFR part 108 / 110 / 120 / 123（**part 113 / 114 正文自 v4.7 起已收**）",
     "21 CFR part 108 / 110 / 120（**part 113 / 114 正文自 v4.7 起已收、part 123 自 v4.9 起已收**）",
     "ov 219"),
    ("**仍未收**：21 CFR part 108 / 110 / 120 / 123 正文、F0/D/z",
     "**仍未收**：21 CFR part 108 / 110 / 120 正文（part 123 自 v4.9 起已收，见 CAP-22）、F0/D/z",
     "ov 236"),
    ("**十三类不可混引（v4.8 口径，v4.9 起为十四类）**：21 CFR Part 117 / PCHF 行业指南",
     "**十四类不可混引（v4.9 口径；v4.8 时为十三类）**：21 CFR Part 117 / PCHF 行业指南",
     "ov 251 头"),
    ("21 CFR Part 114 / CP 7303.878。检查员作业指导一律不创设企业义务",
     "21 CFR Part 114 / CP 7303.878 / **21 CFR Part 123**。检查员作业指导一律不创设企业义务",
     "ov 251 尾"),
    ("21 CFR part 108 / 110 / 120 / 123 / 507 正文、IOM Ch.4、BAM / CPG 全套",
     "21 CFR part 108 / 110 / 120 / 507 正文（part 123 自 v4.9 起已收）、IOM Ch.4、BAM / CPG 全套",
     "ov 253"),
]
for o in OVERVIEW:
    for old, new, label in OV_EDITS:
        rep(o, old, new, 1, label)
print(f"overview: 2 份 × {len(OV_EDITS)} 处")


# ---------------------------------------------------------- PIPELINE_STATE.md
PS = ROOT / "PIPELINE_STATE.md"
rep(PS, "全书均衡提取；十三次来源合并均沿用 single",
    "全书均衡提取；十四次来源合并均沿用 single", label="ps 输出模式")
rep(PS,
    "当前为 **v4.8：21 张卡 / 162 术语 / 95 用例 / 十三类来源 / dist-v12**，见本文件顶部与末尾 v4.8 节；v4.7 的 20 卡 / 152 术语 / 85 用例 / 十二类来源 / dist-v11、",
    "当前为 **v4.9：22 张卡 / 172 术语 / 105 用例 / 十四类来源 / dist-v13**，见本文件顶部与末尾 v4.9 节；v4.8 的 21 卡 / 162 术语 / 95 用例 / 十三类来源 / dist-v12、v4.7 的 20 卡 / 152 术语 / 85 用例 / 十二类来源 / dist-v11、",
    label="ps 阶段快照注")
rep(PS,
    "**仍未收的是 part 108（FCE/SID/Emergency Permit/§108.35）、part 110（至今有效但正文未收）、part 120 / 123、BAM",
    "**仍未收的是 part 108（FCE/SID/Emergency Permit/§108.35）、part 110（至今有效但正文未收）、part 120（part 123 自 v4.9 起已收，见 CAP-22）、BAM",
    label="ps 111")


# ------------------------------------------------------------ test-prompts.json
TP = ROOT / "test-prompts.json"
KEEP = "\u00a7KEEP13\u00a7"
rep(TP, "全包十三类不可混引。v4.7 的触发盲测", KEEP + "。v4.7 的触发盲测", label="tp notes 占位")
t = load(TP)
c = t.count("十三类不可混引")
assert c == 13, f"test-prompts 十三类不可混引 expected 13, got {c}"
_pending[TP] = t.replace("十三类不可混引", "十四类不可混引")
print("test-prompts: 13 处 expected_behavior → 十四类")
rep(TP, "part 110 / 120 / 123、BAM 各章",
    "part 110 / 120（part 123 自 v4.9 起已收，见 CAP-22）、BAM 各章",
    label="tp 599")
rep(TP, "本版未重跑评测。",
    "本版未重跑评测。 | v4.9 追加 10 条 seafood-* 用例（seafood-01..10：fish 与 fishery product 的法定范围、§123.5(a) 默认适用与 §117.5(b) 双向锁定、§123.6(c)(1)(i)–(ix) 九项危害考虑清单、§123.8 验证与 1 周/年度复审、§123.9 记录 1 年/2 年、§123.12 与 FSVP 双轨、§1240.60(c) 转引未收、CP 7303.842 未收、4-1-25 Edition 版本口径与十四类不可混引）；新增第 22 张卡 seafood-haccp-statutory-requirements，第十四来源为 21 CFR Part 123（4-1-25 Edition，9 页 / 13 条款），全包十四类不可混引，全库 172 条术语 / 105 条用例。",
    label="tp notes v4.9")
rep(TP, KEEP, "全包十三类不可混引", label="tp notes 复原")

if ERRORS:
    print("\n命中数不符（未落盘）：")
    for e in ERRORS:
        print("  !", e)
    sys.exit(1)

flush()
print("v4.9 残留回补完成")
