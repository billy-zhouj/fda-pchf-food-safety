"""v4.9 口径残留回补（第三批）：收尾 5 处折行/上下文不自洽。

第二批的批量替换在 cgmp 卡里留下了重复且自相矛盾的一句（先写「part 123 已收」
又写「Part 123 接口只给结论不展开」），另外 4 处因 YAML/正文折行没被命中。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(".")
CARDS = ROOT / ".cangjie/capabilities/cards"
_pending: dict[Path, str] = {}
ERRORS: list[str] = []


def rep(p: Path, old: str, new: str, label: str = "") -> None:
    t = _pending.get(p) or p.read_text(encoding="utf-8")
    c = t.count(old)
    if c != 1:
        ERRORS.append(f"{p}: [{label}] expected 1, got {c} for {old[:60]!r}")
        return
    _pending[p] = t.replace(old, new, 1)


# 1) cgmp：把我上一批插进去的重句整理成一句
rep(
    CARDS / "cgmp-compliance-guide.md",
    "**part 108（FCE/SID/Emergency Permit）、part 110（旧 CGMP，含 §110.110）、part 120 正文仍未收**"
    "（**part 123 自 v4.9 起已收，见 CAP-22**），且 **21 CFR Part 123 与〔§ 117.5(b)〕的接口只给结论不展开**，"
    "一律标「转引未收」；21 CFR Part 120 / 123 与 21 CFR part 117〔§ 117.5(b)(c)〕的接口只给结论不展开。",
    "**part 108（FCE/SID/Emergency Permit）、part 110（旧 CGMP，含 §110.110）、part 120 正文仍未收**，"
    "一律标「转引未收」；**part 123 自 v4.9 起已收**（见 CAP-22，按〔§ 123.xxx〕引用，"
    "与〔§ 117.5(b)〕的接口只给结论不展开）；21 CFR Part 120 与 21 CFR part 117〔§ 117.5(b)(c)〕的接口只给结论不展开。",
    "cgmp 未收段收口",
)

# 2) PIPELINE_STATE 第十来源行
rep(
    ROOT / "PIPELINE_STATE.md",
    "其依据的 21 CFR part 113 / 114 法规正文自 v4.7 起已收；part 108 / 110 / 120 / 123 正文仍未收）",
    "其依据的 21 CFR part 113 / 114 法规正文自 v4.7 起已收；part 108 / 110 / 120 正文仍未收、part 123 自 v4.9 起已收，见 CAP-22）",
    "ps 第十来源",
)

# 3) source-cp-7303-070 文件头两处
rep(
    ROOT / "source-cp-7303-070-2024.md",
    "part 120 / 123、IOM Chapter 4 Sample Schedule Chart 2",
    "part 120（**part 123 自 v4.9 起已收，见 CAP-22 `seafood-haccp-statutory-requirements`**）、IOM Chapter 4 Sample Schedule Chart 2",
    "cp070 头 11",
)
rep(
    ROOT / "source-cp-7303-070-2024.md",
    "**part 108 / 110 / 120 / 123 仍未收正文、须注明「转引未收」**",
    "**part 108 / 110 / 120 仍未收正文、须注明「转引未收」（part 123 自 v4.9 起已收，标〔§ 123.xxx〕）**",
    "cp070 头 15",
)

# 4) source-cp-7303-878 文件头
rep(
    ROOT / "source-cp-7303-878-2023.md",
    "part 113 / 114 之外的 part 120 / 123、",
    "part 113 / 114 / 123 之外的 part 120、",
    "cp878 头 10",
)

# 5) test-prompts 旧用例的「仍未收」清单
rep(
    ROOT / "test-prompts.json",
    "仍未收的是 part 108 / 110 / 120 / 123，相关表述标「转引未收」",
    "仍未收的是 part 108 / 110 / 120（part 123 自 v4.9 起已收，见 CAP-22），相关表述标「转引未收」",
    "tp 480",
)

# 6) glossary 自检记录 v4.7 条目补一句，避免与 v4.9 已收相矛盾
for g in [ROOT / "GLOSSARY.md", ROOT / "candidates/glossary.md", ROOT / ".cangjie/capabilities/book/glossary.md"]:
    rep(
        g,
        "21 CFR part 108 / 110 / 120 / 123 等未收正文一律标『转引未收』",
        "21 CFR part 108 / 110 / 120 / 123 等未收正文一律标『转引未收』（其中 Part 123 自 v4.9 起已收）",
        "glossary 自检 v4.7",
    )

if ERRORS:
    print("命中数不符（未落盘）：")
    for e in ERRORS:
        print("  !", e)
    sys.exit(1)

for p, t in _pending.items():
    p.write_text(t, encoding="utf-8")
    print(f"  wrote {p}")
print("收尾完成")
