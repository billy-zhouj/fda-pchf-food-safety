"""verify_v4_16_quotes.py — CAP-28 逐字引用核对（IOM 2026 Chapter 4）

口径：
1. body_only()：只取 `source-iom-ch4-2026.md` 中 Word 点线目录（TOC）起点
   `**4.1 – GENERAL ....` 之后的内容。**该文件头部（L2–L60）是本包自写的
   「来源 / 效力层级 / 关键口径 / 转换局限」说明块，其中大量英文片段与卡片引文
   同形**——若把它算进正文，就成了自我验证循环，必须排除。
2. 归一化：NFKC + 弯引号归一 + 只留字母数字 + 小写（消除断行、空格、连字符、
   下划线 emphasis、破折号差异）。
3. 节引（含 `...`／`…`）按段核验，逐段必须命中且顺序一致。
4. 每段引文 ≤100 词；不得取自表格行（`|` 开头）。
5. 阈值 20 字符，短于阈值的引文不参与核验（多为表单号罗列）。
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / "source-iom-ch4-2026.md"
CARD = BASE / ".cangjie/capabilities/cards/iom-sampling-procedure.md"
MARKER = "**4.1 – GENERAL ...."


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
    if i < 200:
        raise SystemExit("FATAL: 正文分界标记出现在文件头部之前，口径失效")
    return t[i:]


def word_count(s: str) -> int:
    cjk = len(re.findall(r"[\u4e00-\u9fff]", s))
    latin = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-.()]*", s))
    return cjk + latin


def main() -> int:
    raw = SRC.read_text(encoding="utf-8")
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
        # 归属为法规正文的引文由 Part 117 /113/114/123/108/120 各自的校验器负责
        nxt = lines[n].strip() if n < len(lines) else ""
        if nxt.startswith("> —— 〔§ "):
            continue
        quotes.append((n, q.strip('"').strip()))

    ok = 0
    bad: list[tuple[int, str, str]] = []
    for n, q in quotes:
        segs = [x for x in re.split(r"\.\.\.|…", q) if len(norm(x)) >= 20] or [q]
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

    # 自验证循环探测：卡片引文若只能在本包自写的文件头里找到，须报警
    head = norm(raw[: raw.find(MARKER)])
    head_only = []
    for n, q in quotes:
        segs = [x for x in re.split(r"\.\.\.|…", q) if len(norm(x)) >= 20]
        if not segs:
            continue
        if all(norm(x) in head for x in segs) and not all(
            norm(x) in body for x in segs
        ):
            head_only.append(n)

    print(f"文件头（已排除）字符数    : {raw.find(MARKER)}")
    print(f"引文总数                  : {len(quotes)}")
    print(f"逐字命中（正文区）        : {ok}")
    print(f"未命中                    : {len(bad)}")
    for n, q, seg in bad:
        print(f"  L{n}: {q[:90]!r}")
        print(f"       失配段={seg[:80]!r}")
    print(f"超 100 词的引文           : {len(long_quotes)} {long_quotes}")
    print(f"取自表格行的引文          : {len(table_rows)} {table_rows}")
    print(f"仅命中文件头的引文        : {len(head_only)} {head_only}")

    verdict = (
        "PASS" if not bad and not long_quotes and not table_rows and not head_only else "FAIL"
    )
    print(f"RESULT: {verdict}")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())