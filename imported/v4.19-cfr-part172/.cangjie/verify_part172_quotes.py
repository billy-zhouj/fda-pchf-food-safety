#!/usr/bin/env python3
"""Verify that every block-quoted English passage in a card/candidate file
appears verbatim (whitespace-normalised) in the converted Part 172 markdown.

Usage:  python verify_part172_quotes.py FILE [FILE ...]

Quote block convention accepted in this project:
    > "quoted text ..."
or  > quoted text ...        (any indented '>' line that is not a citation line)
Citation lines are ignored:  > —— 〔§ 172.x〕[pdf-page N]
                             > 中文自译：...
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "source-cfr-part172-2026.md"

SKIP_PREFIX = (
    "——", "—", "中文自译", "来源", "效力", "关键口径", "转换局限", "不可混引",
    "本卡", "⚠", "注", "说明", "原文", "格式", "本段", "以下", "**",
    "TABLE REGION", "<!--", "主代理", "纪律：", "扫描覆盖", "本件", "取材", "覆盖自检", "条款出处",
)


def norm(s: str) -> str:
    return " ".join(s.split())


def main(paths: list[str]) -> int:
    src = norm(SRC.read_text(encoding="utf-8"))
    total = ok = 0
    misses: list[tuple[str, str, str]] = []

    for p in paths:
        f = Path(p)
        if not f.is_file():
            print(f"  [SKIP] not a file: {p}")
            continue
        n_this = k_this = 0
        for lineno, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            s = line.strip()
            if not s.startswith(">"):
                continue
            body = s.lstrip(">").strip()
            if not body or body.startswith(SKIP_PREFIX):
                continue
            # strip wrapping quotes if present
            q = body
            if len(q) >= 2 and q[0] in "\"“" and q[-1] in "\"”":
                q = q[1:-1]
            q = q.strip()
            if len(q) < 25:           # too short to be a meaningful citation
                continue
            if not re.search(r"[A-Za-z]{3}", q):
                continue
            n_this += 1
            if norm(q) in src:
                k_this += 1
            else:
                misses.append((f.name, str(lineno), q[:110]))
        print(f"  {f.name}: {k_this}/{n_this} verified")
        total += n_this
        ok += k_this

    if misses:
        print("\n  MISSES:")
        for name, ln, q in misses:
            print(f"    {name}:{ln}  {q}")
    print(f"\nTOTAL: {ok}/{total} verified")
    print("RESULT: " + ("PASS" if ok == total else "FAIL"))
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))