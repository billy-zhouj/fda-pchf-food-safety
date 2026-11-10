"""verify_v4_15_quotes.py — CAP-27 逐字引用核对（CP 7303.847）

口径：
1. body_only()：只取 `source-cp-7303-847-2025.md` 中 `### CHAPTER 03 – FOODBORNE
   BIOLOGICAL HAZARDS` 之后（即转换出的原件正文，含封面页），头部「条款地图」的
   转述不得充当引文来源。
2. 归一化：NFKC + 只留字母数字 + 小写（消除断行、空格、连字符差异）。
3. 节引（含 `...`／`…`）按段核验，逐段必须命中且顺序一致。
4. 每段引文 ≤100 词；不得取自表格行。
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / "source-cp-7303-847-2025.md"
CARD = BASE / ".cangjie/capabilities/cards/juice-inspection-program.md"
MARKER = "### CHAPTER 03 – FOODBORNE BIOLOGICAL HAZARDS"


def norm(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\(\1\)", r"\1", s)
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"[^0-9a-z]", "", s.lower())


def body_only() -> str:
    t = SRC.read_text(encoding="utf-8")
    i = t.find(MARKER)
    if i < 0:
        raise SystemExit("FATAL: 源文件缺少正文分界标记，拒绝核对")
    return t[i:]


def word_count(s: str) -> int:
    cjk = len(re.findall(r"[\u4e00-\u9fff]", s))
    latin = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-.()]*", s))
    return cjk + latin


def main() -> int:
    body = norm(body_only())
    lines = CARD.read_text(encoding="utf-8").split("\n")

    quotes: list[tuple[int, str]] = []
    for n, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s.startswith("> "):
            continue
        q = s[2:].strip()
        if q.startswith("——") or len(q) < 20:
            continue
        # 归属为法规正文的引文由 Part 120 / Part 117 的校验器负责
        if n < len(lines) and lines[n].strip().startswith("> —— 〔§ "):
            continue
        quotes.append((n, q.strip('"').strip()))

    ok = 0
    bad: list[tuple[int, str, str]] = []
    for n, q in quotes:
        segs = [x for x in re.split(r"\.\.\.|…", q) if len(norm(x)) >= 15] or [q]
        pos, good = 0, True
        for seg in segs:
            ns = norm(seg)
            k = body.find(ns, pos)
            if k < 0:
                good = False
                bad.append((n, q, seg))
                break
            pos = k + len(ns)
        if good:
            ok += 1

    long_quotes = [(n, word_count(q)) for n, q in quotes if word_count(q) > 100]
    table_rows = [n for n, q in quotes if q.startswith("|")]

    print(f"引文总数              : {len(quotes)}")
    print(f"逐字命中（正文区）    : {ok}")
    print(f"未命中                : {len(bad)}")
    for n, q, seg in bad:
        print(f"  L{n}: {q[:90]!r}")
        print(f"       失配段={seg[:80]!r}")
    print(f"超 100 词的引文       : {len(long_quotes)} {long_quotes}")
    print(f"取自表格行的引文      : {len(table_rows)} {table_rows}")
    verdict = "PASS" if not bad and not long_quotes and not table_rows else "FAIL"
    print(f"RESULT: {verdict}")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
