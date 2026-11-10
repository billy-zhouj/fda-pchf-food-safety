"""verify_v4_14_part117_quotes.py — 对全包所有〔§ 117.xxx〕引文做追溯核验

背景：Part 117 正文此前只在 metadata 里声明为「第二来源」，文件从未入库，
凡引用〔§ 117.xxx〕的卡片实际都无法在本仓库内复核（v4.13 的 CAP-26 因此把
§117.5(c) 标为「转引未收」）。v4.14 把该文件落到 books/_inbox/ 后，本脚本把
历史上所有〔§ 117.xxx〕引文一次性对账。

方法：
- 在每张卡片里找「> "引文"」块，且其后 4 行内出现〔§ 117.
- 归一化（NFKC + 只留字母数字 + 小写）后在本文件全文内查找
- 同时输出未命中的引文，供人工判定是「真错」还是「跨页断词/省略号省略」
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / "books/_inbox/21-CFR-Part-117-2025.md"
CARDS = BASE / ".cangjie/capabilities/cards"


def norm(s: str) -> str:
    # 折叠 Markdown 里 `[url](url)` 的重复链接：源文件把同一 URL 写了两遍，
    # 卡片转录时去重，归一化若不先折叠会造出假差异。
    s = re.sub(r"\[([^\]]+)\]\(\1\)", r"\1", s)
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"[^0-9a-z]", "", s.lower())


def main() -> int:
    body = norm(SRC.read_text(encoding="utf-8"))
    hits = 0
    misses: list[tuple[str, str, str, str]] = []

    for card in sorted(CARDS.glob("*.md")):
        lines = card.read_text(encoding="utf-8").split("\n")
        i = 0
        while i < len(lines):
            s = lines[i].strip()
            if not s.startswith('> "'):
                i += 1
                continue
            q = s[2:].strip()
            # 引文可能跨多行，收集到下一个非 > 行为止
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith(">"):
                nxt = lines[j].strip()[1:].strip()
                if nxt.startswith("——"):
                    break
                q += " " + nxt
                j += 1
            # 找引用标注：必须是紧接引文块的归属行（以 "> —— 〔§ 117." 开头）
            cite = ""
            if j < len(lines):
                attr = lines[j].strip()
                if attr.startswith("> —— 〔§ 117."):
                    cite = attr
            if cite:
                qq = q.strip().strip('"').strip()
                if len(qq) < 40:
                    i = j + 1
                    continue
                # 节引（含 ... / …）按省略号切段，逐段必须在原文命中，且顺序一致
                segs = [s for s in re.split(r"\.\.\.|…", qq) if len(norm(s)) >= 15]
                if not segs:
                    segs = [qq]
                pos = 0
                ok = True
                for seg in segs:
                    ns = norm(seg)
                    k = body.find(ns, pos)
                    if k < 0:
                        ok = False
                        break
                    pos = k + len(ns)
                if ok:
                    hits += 1
                else:
                    misses.append((card.name, qq, cite, seg if not ok else ""))
            i = j + 1

    print(f"〔§ 117.xxx〕引文命中 : {hits}")
    print(f"未命中              : {len(misses)}")
    for name, q, cite, badseg in misses:
        print(f"\n  [{name}]")
        print(f"    引文: {q[:150]}")
        print(f"    标注: {cite[:110]}")
        if badseg:
            print(f"    未命中片段: {badseg[:120]}")

    verdict = "PASS" if not misses else "REVIEW"
    print(f"\nRESULT: {verdict}")
    return 0 if not misses else 1


if __name__ == "__main__":
    sys.exit(main())
