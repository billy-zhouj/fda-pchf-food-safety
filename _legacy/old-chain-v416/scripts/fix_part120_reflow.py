"""fix_part120_reflow.py — 修补 convert_cfr_part.py 在 Part 120 上的 7 处重排缺陷

转换器两处**内容级**缺陷已在 v4.13 修好（多行 part 标题续行被目录裁剪吞掉、
独占一行的数字被当页码丢弃），本脚本只负责剩余的**段落边界**问题：

  R1  §120.24(b) 句中的跨条引用被切断：
      "...as defined in" / "§ 120.3(a) and (f) and the reduction is..."
      这是 § 120.3(a) 被当条款起点导致的（start_patterns 已按 part 号拦过一层，
      但此处 part 号相同，仍需在正文层还原段落）。

  R2–R7  段内合并的编号项：GPO 双栏重排时 "(c) Documentation." 与其下 "(1)" 被
      并入同一段（START 规则对 "(c) Documentation." 未命中，因为该行前面是
      上一段末尾的换行，而非空行）。逐条断开，原文措辞不改。

纪律：全部走逐条断言（命中数必须为 1），任何一条没命中就 fail。
"""
from __future__ import annotations

import sys
from pathlib import Path

SRC = Path(".cangjie/tmp-part120.md")

NL = chr(10)
REPAIRS: list[tuple[str, str, str]] = [
    (
        "R1-120.24b-join",
        "culling and cleaning as defined in" + NL + NL + "§ 120.3(a) and (f)",
        "culling and cleaning as defined in § 120.3(a) and (f)",
    ),
    (
        "R2-120.12c-split",
        "(c) Documentation. (1) The records",
        "(c) Documentation." + NL + NL + "(1) The records",
    ),
    (
        "R3-120.12d-split",
        "(d) Record retention. (1) All records",
        "(d) Record retention." + NL + NL + "(1) All records",
    ),
    (
        "R4-120.12d-2-split",
        "prepared. (2) Offsite storage",
        "prepared." + NL + NL + "(2) Offsite storage",
    ),
    (
        "R5-120.12f-split",
        "(f) Public disclosure. (1) All records",
        "(f) Public disclosure." + NL + NL + "(1) All records",
    ),
    (
        "R6-120.25c-iv-split",
        "18 to 24 hours. (iv) Examine",
        "18 to 24 hours." + NL + NL + "(iv) Examine",
    ),
    (
        "R7-120.25d-2-split",
        "pathogens of concern. (2) If the review",
        "pathogens of concern." + NL + NL + "(2) If the review",
    ),
    (
        "R8-120.3-j-1-split",
        "for use in verification. (j)(1) Processing",
        "for use in verification." + NL + NL + "(j)(1) Processing",
    ),
    (
        "R9-120.8b-6-split",
        "critical control points; (6) List",
        "critical control points;" + NL + NL + "(6) List",
    ),
    (
        "R10-120.10b-5-split",
        "devi- ation; and (5) Perform",
        "devi- ation; and" + NL + NL + "(5) Perform",
    ),
    (
        "R11-120.13-3-split",
        "ments of § 120.8; (3) Verifying",
        "ments of § 120.8;" + NL + NL + "(3) Verifying",
    ),
]


def main() -> int:
    if not SRC.exists():
        print(f"FATAL: 找不到 {SRC}，请先跑 convert_cfr_part.py", file=sys.stderr)
        return 1
    text = SRC.read_text(encoding="utf-8")
    applied = skipped = 0
    for label, old, new in REPAIRS:
        n = text.count(old)
        if n == 0 and new in text:
            print(f"SKIP [{label}] 已应用")
            skipped += 1
            continue
        if n != 1:
            print(f"FAIL [{label}] 期望 1 处命中，实得 {n} 处", file=sys.stderr)
            print(f"      片段: {old[:100]!r}", file=sys.stderr)
            return 1
        text = text.replace(old, new, 1)
        applied += 1
        print(f"OK   [{label}]")
    SRC.write_text(text, encoding="utf-8")
    print(f"\n修补完成：新应用 {applied} 处 / 跳过 {skipped} 处，输出 {SRC}（{len(text)} 字符）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
