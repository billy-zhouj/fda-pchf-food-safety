"""fix_part108_reflow.py — 修补 convert_cfr_part.py 在 Part 108 上的 6 处重排缺陷

背景：convert_cfr_part.py 的 START 规则把「行首 § x.y」一律当作条款起点，
而 Part 108 正文里恰好有跨行引用的句子（"conducted in accordance with § 108.5"
换行接 "(b) and (c) as to whether..."），于是把正文句提升成了 H2 条款标题；
另有 4 处跨栏/跨页把一句话切成两段，1 处把两个编号项并成一段。

原则：不做自由重排，只做**逐条断言**的定点替换（命中数必须为 1），
任何一条没命中就直接 fail —— 与 apply_v4_11_revisions.py 的 rep_once 同款纪律。
断词连字符（"per- mit"、"Commis- sioner"）按原样保留，与 Part 113/114/123 一致。
"""
from __future__ import annotations

import sys
from pathlib import Path

SRC = Path(".cangjie/tmp-part108.md")

REPAIRS: list[tuple[str, str, str]] = [
    # R1 §108.3(a) 跨页丢句号：原文为 "...used in this part."
    (
        "R1-108.3a-period",
        "applicable to such terms when used in this part\n\n(b) Commissioner",
        "applicable to such terms when used in this part.\n\n(b) Commissioner",
    ),
    # R2 §108.6(b) 句中断段："...with § 108.5" / "(b) and (c) as soon as practicable."
    (
        "R2-108.6b-join",
        "ing conducted in accordance with § 108.5\n\n(b) and (c) as soon as practicable.",
        "ing conducted in accordance with § 108.5 (b) and (c) as soon as practicable.",
    ),
    # R3 §108.7(a) 句中断段："...pursuant to" / "§ 108.12(a)."
    (
        "R3-108.7a-join",
        "Administration pursuant to\n\n§ 108.12(a).",
        "Administration pursuant to § 108.12(a).",
    ),
    # R4 伪条款标题：§108.7(b) 句中的 "§ 108.5 (b) and (c) as to whether..." 被升成 H2，
    #    并与后续段落割裂。还原为同一段正文。
    (
        "R4-false-heading",
        "hearing conducted in accordance with\n\n"
        "## § 108.5 (b) and (c) as to whether the per- mit should be issued.\n"
        "The Commis-",
        "hearing conducted in accordance with § 108.5 (b) and (c) as to whether "
        "the per- mit should be issued. The Commis-",
    ),
    # R5 §108.12(b) 句中断段："Except as provided in paragraph" / "(a) of this section,"
    (
        "R5-108.12b-join",
        "(b) Except as provided in paragraph\n\n(a) of this section, no manufacturer",
        "(b) Except as provided in paragraph (a) of this section, no manufacturer",
    ),
    # R6 §108.25(b) 与 (c)(1) 并段：定义款与注册款是两个独立款，须断开
    (
        "R6-108.25b-split",
        "are applicable when those terms are used in this section. (c)(1) Registration.",
        "are applicable when those terms are used in this section.\n\n(c)(1) Registration.",
    ),
]


def main() -> int:
    if not SRC.exists():
        print(f"FATAL: 找不到 {SRC}，请先跑 convert_cfr_part.py", file=sys.stderr)
        return 1
    text = SRC.read_text(encoding="utf-8")
    for label, old, new in REPAIRS:
        n = text.count(old)
        if n != 1:
            print(f"FAIL [{label}] 期望 1 处命中，实得 {n} 处", file=sys.stderr)
            print(f"      片段: {old[:100]!r}", file=sys.stderr)
            return 1
        text = text.replace(old, new, 1)
        print(f"OK   [{label}]")
    SRC.write_text(text, encoding="utf-8")
    print(f"\n修补完成：{len(REPAIRS)} 处，输出 {SRC}（{len(text)} 字符）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
