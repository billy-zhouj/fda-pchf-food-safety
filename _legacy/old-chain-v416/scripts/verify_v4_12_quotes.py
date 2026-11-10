"""verify_v4_12_quotes.py — CAP-25 逐字引用与体例核对

沿用 verify_v4_11_quotes.py 的口径：
1. body_only()：只取 source-cfr-part108-2025.md 中「## PART 108—EMERGENCY PERMIT」之后，
   头部「条款地图」里的二手摘要不得充当引文来源。
2. 归一化：NFKC + 只留字母数字 + 小写。印刷版双栏断词（per- mit）与换行、空格、
   连字符在归一化后自然消除，因此「原文有断词连字符」不构成失配理由。
3. 每段引文 ≤100 词（中文按字计）；引文不得取自表格行。
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / "source-cfr-part108-2025.md"
CARD = BASE / ".cangjie/capabilities/cards/emergency-permit-control.md"
MARKER = "## PART 108—EMERGENCY PERMIT"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'")
    return re.sub(r"[^0-9a-z]", "", s.lower())


def body_only() -> str:
    t = SRC.read_text(encoding="utf-8")
    i = t.find(MARKER)
    if i < 0:
        raise SystemExit("FATAL: 源文件缺少正文分界标题，拒绝核对")
    return t[i:]


def word_count(s: str) -> int:
    cjk = len(re.findall(r"[\u4e00-\u9fff]", s))
    latin = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-.()]*", s))
    return cjk + latin


def main() -> int:
    body = norm(body_only())
    text = CARD.read_text(encoding="utf-8")
    lines = text.split("\n")

    quotes: list[tuple[int, str]] = []
    for n, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s.startswith("> "):
            continue
        q = s[2:].strip()
        if q.startswith("——") or len(q) < 40:
            continue
        quotes.append((n, q))

    ok = 0
    bad: list[tuple[int, str, str]] = []
    for n, q in quotes:
        if len(q) > 2000:  # 中文体例说明段，不是引文
            continue
        hit = norm(q)
        if hit and hit in body:
            ok += 1
        else:
            bad.append((n, q, hit[:60]))

    long_quotes = [(n, word_count(q)) for n, q in quotes if word_count(q) > 100]
    table_rows = [n for n, q in quotes if q.startswith("|")]

    print(f"引文总数              : {len(quotes)}")
    print(f"逐字命中（正文区）    : {ok}")
    print(f"未命中                : {len(bad)}")
    for n, q, h in bad:
        print(f"  L{n}: {q[:90]!r}")
        print(f"        norm={h!r}")
    print(f"超 100 词的引文       : {len(long_quotes)} {long_quotes}")
    print(f"取自表格行的引文      : {len(table_rows)} {table_rows}")
    verdict = "PASS" if not bad and not long_quotes and not table_rows else "FAIL"
    print(f"RESULT: {verdict}")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
