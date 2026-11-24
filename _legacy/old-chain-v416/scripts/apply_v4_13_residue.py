"""apply_v4_13_residue.py — v4.13 口径回补：把「part 120 未收」的当前断言改为已收

顺序纪律（同 v4.12）：
1. 先做**逐行改写**（这些 old 串里含「十七类」，若先跑全局计数替换就匹配不上）；
2. 再跑批量列表清理（`part 120 / 1240 / 108 / 110 / 507` → 去掉 120 与已收的 108）；
3. 再跑全局「十七类 → 十八类」（卡内无「第十七类」子串，已核对为 0）；
4. 最后把紧邻「十八类」的 `v4.12 起` 校为 `v4.13 起`，并处理「五套 → 六套」。
"""
from __future__ import annotations

import sys
from pathlib import Path

C = Path(".cangjie/capabilities/cards")

FS = "fsvp-inspection-program.md"
FSM = "_meta-fsvp-inspection-program.yaml"
L20 = "lacf-statutory-requirements.md"
L19 = "lacf-inspection-program.md"
S22 = "seafood-haccp-statutory-requirements.md"
G23 = "seafood-hazards-controls-guide.md"
S24 = "seafood-inspection-program.md"
C15 = "cgmp-compliance-guide.md"
R16 = "inspection-readiness.md"
D14 = "defect-action-levels.md"
E25 = "emergency-permit-control.md"
J26 = "juice-haccp.md"

REWRITES: list[tuple[str, str, str, str]] = [
    # ── CAP-21 FSVP：两处 + meta 一处 ────────────────────────────────
    (
        FS, "cap21-quote-tag",
        "> —— PART I.2；**part 120 正文本包未收（标「转引未收」）、part 123 自 v4.9 起已收（见 CAP-22）**",
        "> —— PART I.2；**part 120 自 v4.13 起已收（见 CAP-26）、part 123 自 v4.9 起已收（见 CAP-22）**",
    ),
    (
        FS, "cap21-table",
        "| 果汁 / 水产且供应商符合 part 120 / 123 | **§1.501(b) 豁免** | 本卡（part 120 转引未收；part 123 见 CAP-22） |",
        "| 果汁 / 水产且供应商符合 part 120 / 123 | **§1.501(b) 豁免** | 本卡（part 120 见 CAP-26；part 123 见 CAP-22） |",
    ),
    (
        FSM, "cap21-intent",
        "  - 列出 §1.501(b)–(h) 的八类 FSVP 豁免并指出 part 120 正文未收（part 123 自 v4.9 起已收）",
        "  - 列出 §1.501(b)–(h) 的八类 FSVP 豁免；其中 part 120 自 v4.13 起已收（转 CAP-26）、part 123 自 v4.9 起已收（转 CAP-22）",
    ),
    # ── CAP-20 低酸法条卡：两处 ─────────────────────────────────────
    (
        L20, "cap20-a2-18",
        "18. 用户问「Part 120 / 123 是不是也有豁免」→ 〔§ 117.5(b)(c)〕有同类**条件性**豁免，但 part 120 正文本包未收、**part 123 自 v4.9 起已收（见 CAP-22）**，后者给条款、前者只给接口不展开。",
        "18. 用户问「Part 120 / 123 是不是也有豁免」→ 〔§ 117.5(b)(c)〕有同类**条件性**豁免；part 123 自 v4.9 起已收（CAP-22）、**part 120 自 v4.13 起已收（CAP-26）**，两者都给条款；⚠ 但〔§ 117.5(c)〕本身的逐字文本仍未收，引用其措辞须标「转引未收」。",
    ),
    (
        L20, "cap20-step6",
        "涉及 part 110 / part 120 / BAM / IOM Ch.4 / CPG / Import Alert 全文一律标「转引未收」（part 123 已收，写〔§ 123.xxx〕；part 108 自 v4.12 起已收，写〔§ 108.xxx〕转 CAP-25）",
        "涉及 part 110 / §117.5(c) 逐字文本 / BAM / IOM Ch.4 / CPG / Import Alert 全文一律标「转引未收」（part 123 已收，写〔§ 123.xxx〕；part 108 自 v4.12 起已收，写〔§ 108.xxx〕转 CAP-25；part 120 自 v4.13 起已收，写〔§ 120.xxx〕转 CAP-26）",
    ),
    # ── CAP-22 海鲜法条卡：四处 ─────────────────────────────────────
    (
        S22, "cap22-header-uncited",
        "*⚠ **正文本包仍未收**：21 CFR **part 120**（果汁 HACCP）、**part 1240**（贝类卫生，§123.28(d) 回指 `§ 1240.60(c)`）、**part 110**、**NSSP Guide**。一律标「转引未收」；part 108 自 v4.12 起已收（CAP-25），",
        "*⚠ **正文本包仍未收**：21 CFR **part 1240**（贝类卫生，§123.28(d) 回指 `§ 1240.60(c)`）、**part 110**、**NSSP Guide**、**〔§ 117.5(c)〕逐字文本**。一律标「转引未收」；part 108 自 v4.12 起已收（CAP-25）、part 120 自 v4.13 起已收（CAP-26），",
    ),
    (
        S22, "cap22-a2-22",
        "22. 用户问「21 CFR part 120（果汁）是不是也一样」→ 〔§ 117.5(c)〕有同类条件性豁免，但 part 120 **正文本包未收**，只给接口不展开。",
        "22. 用户问「21 CFR part 120（果汁）是不是也一样」→ 〔§ 117.5(c)〕有同类条件性豁免；part 120 自 v4.13 起已收，**转 CAP-26 `juice-haccp`** 给条款（5-log、§120.25 E. coli、记录期等），但〔§ 117.5(c)〕本身逐字文本仍未收。",
    ),
    (
        S22, "cap22-step7",
        "涉及 part 120 / 1240 / 110 / NSSP / BAM / CPG / Import Alert 全文一律标「转引未收」（part 108 自 v4.12 起已收，写〔§ 108.xxx〕转 CAP-25）。",
        "涉及 part 1240 / 110 / NSSP / BAM / CPG / Import Alert 全文一律标「转引未收」（part 108 自 v4.12 起已收，写〔§ 108.xxx〕转 CAP-25；part 120 自 v4.13 起已收，写〔§ 120.xxx〕转 CAP-26）。",
    ),
    (
        S22, "cap22-i-refuse",
        "从 Part 123 反推 part 120 / 1240 / NSSP 的条文",
        "从 Part 123 反推 part 1240 / NSSP 的条文",
    ),
    # ── CAP-23 海鲜指南卡：头注 ─────────────────────────────────────
    (
        G23, "cap23-header-uncited",
        "NSSP Guide（软体贝类）、21 CFR part 120（果汁 HACCP）／part 1240（贝类卫生）／part 110／part 507（part 108 自 v4.12 起已收，见 CAP-25）",
        "NSSP Guide（软体贝类）、21 CFR part 1240（贝类卫生）／part 110／part 507（part 108 自 v4.12 起、part 120 自 v4.13 起已收，见 CAP-25 / CAP-26）",
    ),
    # ── CAP-15 cGMP / CAP-16 迎检 / CAP-19 检查程序 ──────────────────
    (
        C15, "cap15-uncited",
        "**part 110（旧 CGMP，含 §110.110）、part 120 正文仍未收**，一律标「转引未收」",
        "**part 110（旧 CGMP，含 §110.110）正文仍未收**，一律标「转引未收」",
    ),
    (
        R16, "cap16-uncited",
        "但 **part 108（FCE/SID/Emergency Permit）、part 110、part 120 正文仍未收**（part 123 自 v4.9 起已收，见 CAP-22）",
        "但 **part 110 正文仍未收**（part 108 自 v4.12 起已收，见 CAP-25；part 120 自 v4.13 起已收，见 CAP-26；part 123 自 v4.9 起已收，见 CAP-22）",
    ),
    (
        L19, "cap19-b2-uncited",
        "part 120（果汁 HACCP）、IOM Chapter 4（Sample Schedule Chart 2）",
        "IOM Chapter 4（Sample Schedule Chart 2）",
    ),
    # ── meta 两处 ──────────────────────────────────────────────────
    (
        "_meta-seafood-haccp-statutory-requirements.yaml", "meta-cap22-uncited",
        "part 120/1240/NSSP 正文仍未收",
        "part 1240 / NSSP 正文与 §117.5(c) 逐字文本仍未收（part 120 自 v4.13 起已收，见 CAP-26）",
    ),
    (
        "_meta-seafood-haccp-statutory-requirements.yaml", "meta-cap22-scope",
        "判断哪些问题超出本包（part 120/1240/108/110/507、NSSP、BAM、Import Alert 全文；",
        "判断哪些问题超出本包（part 1240/110/507、NSSP、BAM、Import Alert 全文；",
    ),
]

BULK = [
    ("list-120-108",
     "part 120 / 1240 / 108 / 110 / 507",
     "part 1240 / 110 / 507（part 108 自 v4.12 起、part 120 自 v4.13 起已收）"),
    ("list-compact",
     "part 120/1240/108/110/507",
     "part 1240/110/507"),
]

# 五套 → 六套（只在列举六部法规正文的引用规范处）
SIX_SETS = [
    (
        C15,
        "〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕（五套独立编号）",
        "〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕（六套独立编号）",
    ),
    (
        R16,
        "〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕五套独立编号",
        "〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕六套独立编号",
    ),
    (
        L20,
        "〔§ 108.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕/〔§ 117.xxx〕/〔§ 123.xxx〕五套法条各自独立",
        "〔§ 108.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕/〔§ 117.xxx〕/〔§ 120.xxx〕/〔§ 123.xxx〕六套法条各自独立",
    ),
    (
        S22,
        "〔§ 108.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕/〔§ 117.xxx〕/〔§ 123.xxx〕五套法条各自独立",
        "〔§ 108.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕/〔§ 117.xxx〕/〔§ 120.xxx〕/〔§ 123.xxx〕六套法条各自独立",
    ),
    (
        E25,
        "〔§ 108.xxx〕／〔§ 113.xxx〕／〔§ 114.xxx〕／〔§ 117.xxx〕／〔§ 123.xxx〕五套法条各自独立",
        "〔§ 108.xxx〕／〔§ 113.xxx〕／〔§ 114.xxx〕／〔§ 117.xxx〕／〔§ 120.xxx〕／〔§ 123.xxx〕六套法条各自独立",
    ),
    (
        D14,
        "法规正文层已扩为五套（v4.12 加 Part 108〔§ 108.xxx〕，见 CAP-25）",
        "法规正文层已扩为六套（v4.12 加 Part 108〔§ 108.xxx〕、v4.13 加 Part 120〔§ 120.xxx〕，见 CAP-25 / CAP-26）",
    ),
    (
        S22,
        "（**v4.12 起为五套：加 Part 108〔§ 108.xxx〕，见 CAP-25 `emergency-permit-control`**）",
        "（**v4.12 起为五套：加 Part 108〔§ 108.xxx〕；v4.13 起为六套：再加 Part 120〔§ 120.xxx〕，见 CAP-25 / CAP-26**）",
    ),
]


def main() -> int:
    apply = "--apply" in sys.argv
    files: dict[Path, str] = {}

    def get(name: str) -> str:
        p = C / name
        if p not in files:
            files[p] = p.read_text(encoding="utf-8")
        return files[p]

    for name, label, old, new in REWRITES:
        t = get(name)
        n = t.count(old)
        if n != 1:
            print(f"FAIL [{label}] {name} 期望 1 处命中，实得 {n}", file=sys.stderr)
            print(f"      {old[:110]!r}", file=sys.stderr)
            return 1
        files[C / name] = t.replace(old, new, 1)
        print(f"OK   [rewrite] {label}")

    for name, old, new in SIX_SETS:
        t = get(name)
        n = t.count(old)
        if n != 1:
            print(f"FAIL [six-sets] {name} 期望 1 处命中，实得 {n}", file=sys.stderr)
            print(f"      {old[:110]!r}", file=sys.stderr)
            return 1
        files[C / name] = t.replace(old, new, 1)
        print(f"OK   [six-sets] {name}: {old[:38]!r}")

    for label, old, new in BULK:
        total = 0
        for p, t in list(files.items()):
            n = t.count(old)
            if n:
                files[p] = t.replace(old, new)
                total += n
        print(f"OK   [bulk]    {label} × {total}")

    # 全局「十七类」→「十八类」：卡目录全部文件
    total = 0
    for p in sorted(C.glob("*")):
        if not p.is_file():
            continue
        t = files.get(p) or p.read_text(encoding="utf-8")
        if "十七类" in t:
            n = t.count("十七类")
            total += n
            files[p] = t.replace("十七类", "十八类")
    print(f"OK   [count]   合计 {total} 处「十七类 → 十八类」")

    # 25 张 → 26 张
    total = 0
    for p, t in list(files.items()):
        if "25 张" in t:
            n = t.count("25 张")
            total += n
            files[p] = t.replace("25 张", "26 张")
    print(f"OK   [count]   合计 {total} 处「25 张 → 26 张」")

    # 紧邻「十八类」的 v4.12 起 → v4.13 起
    fixed = 0
    for p, t in list(files.items()):
        buf = list(t)
        i = 0
        while True:
            j = t.find("十八类", i)
            if j < 0:
                break
            k = t.rfind("v4.12 起", max(0, j - 30), j)
            if k >= 0:
                buf[k:k + len("v4.12 起")] = list("v4.13 起")
                t = "".join(buf)
                fixed += 1
            i = j + 1
        files[p] = t
    print(f"OK   [version] {fixed} 处 `v4.12 起` 校为 `v4.13 起`")

    if not apply:
        print(f"\n[dry-run] 涉及 {len(files)} 个文件，未写盘。加 --apply 落地。")
        return 0

    for p, t in files.items():
        p.write_text(t, encoding="utf-8")
    print(f"\n已写盘 {len(files)} 个文件。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
