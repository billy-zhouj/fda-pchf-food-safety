#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_v4_10_quotes.py — v4.10 CAP-23 R 段英文引用块逐字核对。

设计要点（沿用 v4.9 verify_seafood_quotes.py 的教训）：
1. body_only()：只取 `source-seafood-hazards-guide-2022.md` 中「## 正文（导出原文，未改写）」
   之后的文本。文件头是我方转述，绝不能参与匹配，否则形成自我验证循环。
2. 不依赖行号匹配：行号是给人看的定位标签，落地文件因文件头有行号偏移。
3. 归一化只做「控制字符清理 + 空白合并」，不做 NFKC，避免弯引号/标点被改写而误判。
4. 附录 8 / Addendum 1 / Additional Document 1–2 的法规转录区不排除（它们也是正文），
   但本卡的引用块均来自散文段落，不会命中表格；报告里另列「疑似表格引用」告警。
"""
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CARD = BASE / ".cangjie/capabilities/cards/seafood-hazards-controls-guide.md"
SRC = BASE / "source-seafood-hazards-guide-2022.md"
MARKER = "## 正文（导出原文，未改写）"


def body_only(raw: str) -> str:
    if MARKER not in raw:
        raise SystemExit("FATAL: 源文件缺少正文分界标题，拒绝核对")
    return raw.split(MARKER, 1)[1]


def norm(s: str) -> str:
    s = s.replace("\x03", "").replace("\u00ad", "")
    return re.sub(r"\s+", " ", s).strip()


def main() -> int:
    card = CARD.read_text(encoding="utf-8")
    body = norm(body_only(SRC.read_text(encoding="utf-8")))

    # 引用块格式：> "英文原句"，紧随其后的 > —— 出处 不计入
    quotes = re.findall(r'^> "(.+)"\s*$', card, flags=re.M)
    if not quotes:
        print("FATAL: 卡片中未找到任何引用块")
        return 2

    hits, misses = [], []
    for i, q in enumerate(quotes, 1):
        qn = norm(q)
        (hits if qn in body else misses).append((i, qn))

    print(f"CAP-23 R 段引用块总数 : {len(quotes)}")
    print(f"逐字命中（正文区）    : {len(hits)}")
    print(f"未命中                : {len(misses)}")
    for i, q in misses:
        print(f"  [MISS #{i}] {q[:180]}")

    # 词数红线：英文引用块每段 ≤100 词
    over = [(i, len(q.split())) for i, q in enumerate(quotes, 1) if len(q.split()) > 100]
    print(f"超过 100 词的引用块   : {len(over)} {over if over else ''}")

    # 表格/页眉红线：只做提示，命中表格行不算通过
    table_like = [(i, q) for i, q in enumerate(quotes, 1) if re.search(r'\|.*\|', q)]
    print(f"疑似含表格管道的引用  : {len(table_like)}")
    for i, q in table_like:
        print(f"  [TABLE #{i}] {q[:160]}")

    ok = not misses and not over and not table_like
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
