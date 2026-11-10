"""v4.9 口径残留回补（第四批）：把「X 正文未收」句式中仍含 Part 123 的收干净。

前三批按「清单式」（108 / 110 / 120 / 123）扫，漏掉了「part 120 / 123 正文本包未收」
这种对句式。本批补 6 处，并把第二批在 glossary 自检行留下的括号叠句理顺。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(".")
CARDS = ROOT / ".cangjie/capabilities/cards"
_pending: dict[Path, str] = {}
ERRORS: list[str] = []


def rep(p: Path, old: str, new: str, label: str = "", n: int = 1) -> None:
    t = _pending.get(p) or p.read_text(encoding="utf-8")
    c = t.count(old)
    if c != n:
        ERRORS.append(f"{p}: [{label}] expected {n}, got {c} for {old[:60]!r}")
        return
    _pending[p] = t.replace(old, new)


# glossary ×3：t162 的收录边界句 + 自检行叠括号
for g in [ROOT / "GLOSSARY.md", ROOT / "candidates/glossary.md", ROOT / ".cangjie/capabilities/book/glossary.md"]:
    rep(g,
        "part 120 / 123 正文本包未收。",
        "part 120 正文本包未收、**part 123 自 v4.9 起已收（见 CAP-22）**。",
        "t162 边界句")
    rep(g,
        "21 CFR part 108 / 110 / 120 / 123 等未收正文一律标『转引未收』（其中 Part 123 自 v4.9 起已收）（Part 113 / 114 正文自 v4.7 起已收）",
        "21 CFR part 108 / 110 / 120 等未收正文一律标『转引未收』（其中 Part 113 / 114 正文自 v4.7 起已收、Part 123 自 v4.9 起已收）",
        "自检 v4.7 括号")

rep(CARDS / "cgmp-compliance-guide.md",
    "**21 CFR part 108 / 110 / 120 / 123 等未收正文一律标「转引未收」；十四类不可混引**",
    "**21 CFR part 108 / 110 / 120 等未收正文一律标「转引未收」（part 123 自 v4.9 起已收，见 CAP-22）；十四类不可混引**",
    "cgmp B8 引用纪律")

rep(CARDS / "lacf-inspection-program.md",
    "`21 CFR part 108 / 110 / 120 / 123` 与 IOM Ch.4、BAM、CPG、Import Alert 一律标「转引未收」。",
    "`21 CFR part 108 / 110 / 120` 与 IOM Ch.4、BAM、CPG、Import Alert 一律标「转引未收」（part 123 已收，写〔§ 123.xxx〕）。",
    "lacf-inspection B11 尾")

rep(CARDS / "lacf-statutory-requirements.md",
    "part 108 / 110 / 120 / 123 与其他未收正文一律标「转引未收」",
    "part 108 / 110 / 120 与其他未收正文一律标「转引未收」（part 123 自 v4.9 起已收）",
    "lacf-stat B8 尾")

rep(ROOT / "test-prompts.json",
    "④ part 120 / 123 正文本包未收，标转引未收；",
    "④ part 120 正文本包未收，标转引未收；part 123 自 v4.9 起已收（见 CAP-22）；",
    "tp 627")

if ERRORS:
    print("命中数不符（未落盘）：")
    for e in ERRORS:
        print("  !", e)
    sys.exit(1)

for p, t in _pending.items():
    p.write_text(t, encoding="utf-8")
    print(f"  wrote {p}")
print("第四批完成")
