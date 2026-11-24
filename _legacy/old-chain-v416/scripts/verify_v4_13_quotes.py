"""verify_v4_13_quotes.py — CAP-26 逐字引用与体例核对

口径与 verify_v4_12_quotes.py 一致：
1. body_only()：只取 source-cfr-part120-2025.md 中「## PART 120—...」之后，
   头部「条款地图」不得充当引文来源。
2. 归一化：NFKC + 只留字母数字 + 小写（自动消除断词连字符、换行、空格）。
3. 每段引文 ≤100 词；引文不得取自表格行。
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / "source-cfr-part120-2025.md"
CARD = BASE / ".cangjie/capabilities/cards/juice-haccp.md"
MARKER = "## PART 120—HAZARD ANALYSIS AND CRITICAL CONTROL POINT (HACCP) SYSTEMS"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
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
    lines = CARD.read_text(encoding="utf-8").split("\n")

    quotes: list[tuple[int, str]] = []
    raw = CARD.read_text(encoding="utf-8").split("\n")
    for n, ln in enumerate(raw, 1):
        s = ln.strip()
        if not s.startswith("> "):
            continue
        q = s[2:].strip()
        if q.startswith("——") or len(q) < 40:
            continue
        # 归属为〔§ 117.xxx〕的引文由 verify_v4_14_part117_quotes.py 负责，此处跳过
        if n < len(raw) and raw[n].strip().startswith("> —— 〔§ 117."):
            continue
        quotes.append((n, q))

    ok = 0
    bad: list[tuple[int, str, str]] = []
    for n, q in quotes:
        if len(q) > 2000:
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
