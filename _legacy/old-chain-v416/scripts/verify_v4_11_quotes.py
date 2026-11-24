#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_v4_11_quotes.py — v4.11 CAP-24 R 段英文引用块逐字核对。

沿用 v4.10 verify_v4_10_quotes.py 的纪律：
1. body_only()：只取 source-cp-7303-842-2023.md 中「## 正文（转换原文，未改写）」之后，
   文件头是我方转述，绝不参与匹配，否则形成自我验证循环。
2. 不依赖行号匹配；行号只是给人看的定位标签。
3. 归一化只做「控制字符清理 + 空白合并」，不做 NFKC，避免弯引号与标点被改写而误判。
4. 本件是 pdf2md-pro 转换产物，正文含 ** / <u> / <br> / # / `o` / • 等 Markdown 标记；
   因此先 strip_md() 去标记再比对，引用块本身是纯文本（candidates/v4-11-quotes.md 已按此口径提取）。
"""
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CARD = BASE / ".cangjie/capabilities/cards/seafood-inspection-program.md"
SRC = BASE / "source-cp-7303-842-2023.md"
MARKER = "## 正文（转换原文，未改写）"


def body_only(raw: str) -> str:
    if MARKER not in raw:
        raise SystemExit("FATAL: 源文件缺少正文分界标题，拒绝核对")
    return raw.split(MARKER, 1)[1]


def strip_md(s: str) -> str:
    s = s.replace("**", "").replace("<u>", "").replace("</u>", "")
    s = s.replace("`", "").replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    s = re.sub(r"(?m)^#{1,6}\s*", "", s)
    s = re.sub(r"(?m)^[o•§]\s+", "", s)
    return s


def norm(s: str) -> str:
    s = s.replace("\x03", "").replace("\u00ad", "").replace("\uf0b7", "")
    return re.sub(r"\s+", " ", s).strip()


def main() -> int:
    card = CARD.read_text(encoding="utf-8")
    body = norm(strip_md(body_only(SRC.read_text(encoding="utf-8"))))

    quotes = re.findall(r'^> "(.+)"\s*$', card, flags=re.M)
    if not quotes:
        print("FATAL: 卡片中未找到任何引用块")
        return 2

    hits, misses = [], []
    for i, q in enumerate(quotes, 1):
        qn = norm(q)
        (hits if qn in body else misses).append((i, qn))

    print(f"CAP-24 R 段引用块总数 : {len(quotes)}")
    print(f"逐字命中（正文区）    : {len(hits)}")
    print(f"未命中                : {len(misses)}")
    for i, q in misses:
        print(f"  [MISS #{i}] {q[:180]}")

    over = [(i, len(q.split())) for i, q in enumerate(quotes, 1) if len(q.split()) > 100]
    print(f"超过 100 词的引用块   : {len(over)} {over if over else ''}")

    table_like = [(i, q) for i, q in enumerate(quotes, 1) if re.search(r'\|.*\|', q)]
    print(f"疑似含表格管道的引用  : {len(table_like)}")
    for i, q in table_like:
        print(f"  [TABLE #{i}] {q[:160]}")

    ok = not misses and not over and not table_like
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
