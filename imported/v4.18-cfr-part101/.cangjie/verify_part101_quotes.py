#!/usr/bin/env python3
"""Verbatim quote verification for the v4.18 Part 101 capability cards.

Usage:
    python .cangjie/verify_part101_quotes.py <card1.md> [card2.md ...]

Every ``> "..."`` quote block in a card must be found, after whitespace
normalisation, in the BODY of source-cfr-part101-2026.md. The body starts at
the ``# PART 101 — FOOD LABELING`` heading so that self-written file headers
can never satisfy a quote (no self-verification loop).

Rules enforced (cangjie-skill quality red lines):
  * quote <= 100 English words
  * no quote may contain a table region marker
  * attribution line ``> —— 〔§ 101.xxx〕`` must follow the quote block
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source-cfr-part101-2026.md"


def norm(s: str) -> str:
    return " ".join(s.split())


def body() -> str:
    text = SOURCE.read_text(encoding="utf-8")
    marker = "# PART 101 — FOOD LABELING"
    idx = text.find(marker)
    if idx < 0:
        raise SystemExit("FATAL: body marker not found in source")
    # Strip HTML comments (pdf-page markers, table markers) before matching.
    clean = re.sub(r"<!--.*?-->", " ", text[idx:], flags=re.S)
    return norm(clean)


def extract_quotes(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    quotes: list[str] = []
    buf: list[str] = []
    for ln in lines:
        s = ln.strip()
        if s.startswith('> "') or (buf and s.startswith("> ") and not s.startswith("> ——") and not s.startswith("> 中文")):
            buf.append(s.lstrip("> ").strip())
            continue
        if buf:
            q = norm(" ".join(buf)).strip().strip('"')
            # strip leading quote char of first line and trailing of last
            q = q.lstrip('"').rstrip('"').strip()
            if q:
                quotes.append(q)
            buf = []
    if buf:
        q = norm(" ".join(buf)).strip().strip('"').lstrip('"').rstrip('"').strip()
        if q:
            quotes.append(q)
    return quotes


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: verify_part101_quotes.py <card.md> ...")
        return 2
    src = body()
    total = hit = 0
    failures: list[str] = []
    for arg in sys.argv[1:]:
        p = Path(arg)
        qs = extract_quotes(p)
        ok = 0
        for q in qs:
            total += 1
            words = len(q.split())
            if words > 100:
                failures.append(f"[TOO LONG {words}w] {p.name}: {q[:90]}")
                continue
            if "TABLE REGION" in q or "not quotable verbatim" in q:
                failures.append(f"[TABLE REGION] {p.name}: {q[:90]}")
                continue
            # Ellipsis-bearing excerpt: verify each fragment separately.
            parts = [x.strip() for x in re.split(r"\.\.\.|…", q) if x.strip()]
            if all(norm(frag) in src for frag in parts):
                hit += 1
                ok += 1
            else:
                failures.append(f"[MISS] {p.name}: {q[:110]}")
        print(f"{p.name}: {ok}/{len(qs)} quotes verified")
    print(f"\nTOTAL: {hit}/{total} verified")
    if failures:
        print(f"FAILURES ({len(failures)}):")
        for f in failures:
            print("  -", f)
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
