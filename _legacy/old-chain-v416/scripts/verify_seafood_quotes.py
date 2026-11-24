"""verify_seafood_quotes.py — 核对 CAP-22 R 段英文引用块是否逐字来自 Part 123 原文。

归一化口径与 CAP-20 / CAP-21 一致：剥离 markup → NFKC → 去所有非字母数字 → 小写。
印刷版行末断词连字符（`proc- essing`）与换行、空格在此口径下自然消除。
Part 117 引文（§117.5(b)）另用 21-CFR-Part-117-2025.md 作对照源。
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent
CARD = BASE / "capabilities/cards/seafood-haccp-statutory-requirements.md"
META = BASE / "capabilities/cards/_meta-seafood-haccp-statutory-requirements.yaml"
SRC_123 = BASE.parent / "source-cfr-part123-2025.md"
SRC_117 = BASE.parent.parent / "_inbox/21-CFR-Part-117-2025.md"


def strip_markup(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("**", "").replace("__", "")
    s = re.sub(r"[*_`#]", "", s)
    return s


def norm(s: str) -> str:
    s = strip_markup(s)
    s = unicodedata.normalize("NFKC", s)
    # 弯引号统一
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"[^0-9A-Za-z]+", "", s).lower()


def extract_quotes(card_text: str) -> list[str]:
    body = card_text.split("## R — 原文", 1)[1].split("## I — 自述", 1)[0]
    out = []
    for m in re.finditer(r'^>\s*"(.*?)"\s*$', body, re.M | re.S):
        q = m.group(1).strip()
        q = re.sub(r"\s*\n\s*", " ", q)
        if q:
            out.append(q)
    return out


def body_only(path: Path) -> str:
    """只取法规正文区，剔除本包自己写的导入说明/条款地图。

    关键：文件头里会转述并引用其他 part 的原文（如 §117.5(b)），若不剔除，
    核对时会出现「引文在我自己写的文件头里命中」的自我验证循环。
    正文起点为第一个 `## § ` 条款标题。
    """
    t = path.read_text(encoding="utf-8")
    m = re.search(r"(?m)^## § \d+\.", t)
    return t[m.start():] if m else t


def main() -> int:
    card = CARD.read_text(encoding="utf-8")
    quotes = extract_quotes(card)
    # 正文区起点：Part 123 第一个 § 条款
    src123 = norm(body_only(SRC_123))
    src117 = norm(body_only(SRC_117)) if SRC_117.exists() else ""
    both = src123 + "||" + src117

    print(f"抽取引用块: {len(quotes)}")
    print(f"Part123 正文起点已剔除文件头，归一化长度 {len(src123)}")
    print(f"Part117 正文起点已剔除文件头，归一化长度 {len(src117)}\n")
    hit = miss = 0
    failures = []
    for i, q in enumerate(quotes, 1):
        n = norm(q)
        if not n:
            print(f"  [{i:2d}] SKIP (归一化后为空)")
            continue
        if n in src123:
            hit += 1
            src = "Part123"
        elif n in both:
            hit += 1
            src = "Part117"
        else:
            miss += 1
            failures.append((i, q, n))
            src = "MISS"
        print(f"  [{i:2d}] {src:8s} {q[:88]!r}")

    print(f"\n命中 {hit} / {len(quotes)}，失配 {miss}")
    for i, q, n in failures:
        print(f"\n--- MISMATCH [{i}] ---\n原文引文: {q[:300]}")
        # sliding window 定位首个失配点
        window = 40
        best = -1
        for start in range(0, max(1, len(n) - window), 8):
            if n[start:start + window] in both:
                best = start
        if best >= 0:
            print(f"前 {best} 字符可在源中定位，失配从此处附近开始: {n[max(0,best-20):best+60]!r}")
        else:
            print("整段均无法定位（可能跨段引用或含改动）")

    # meta 类型检查
    md = yaml.safe_load(META.read_text(encoding="utf-8"))
    problems = []
    for k in ("keywords", "intents", "member_units"):
        if k in md and not isinstance(md[k], list):
            problems.append((k, "not list", type(md[k]).__name__))
        elif k in md:
            bad = [x for x in md[k] if not isinstance(x, str)]
            if bad:
                problems.append((k, "non-str items", bad[:3]))
    for k in ("slug", "title", "importance", "one_liner", "source_label"):
        if not isinstance(md.get(k), str):
            problems.append((k, "not str", type(md.get(k)).__name__))
    print(f"\nmeta 类型 problems: {len(problems)} {problems if problems else ''}")

    return 0 if (miss == 0 and not problems) else 1


if __name__ == "__main__":
    raise SystemExit(main())