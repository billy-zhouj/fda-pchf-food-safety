"""apply_v4_9_bundle_arrays.py — v4.9 补 assemble_bundle.py 的三个入口数组。

只新增/修正条目，不动已有条目内容；原子写盘。
"""
from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
AB = BASE / ".cangjie/assemble_bundle.py"

_pending: dict[Path, str] = {}


def load(p: Path) -> str:
    if p not in _pending:
        _pending[p] = p.read_text(encoding="utf-8")
    return _pending[p]


def rep(p: Path, old: str, new: str, label: str) -> None:
    t = load(p)
    n = t.count(old)
    assert n == 1, f"[{label}] expected 1 hit, got {n}: {old[:80]!r}"
    _pending[p] = t.replace(old, new, 1)


def main() -> None:
    # ---------- 1. core_principles：法规正文层由三套升为四套 ----------
    old_cp = ("先分层再引用：**法规正文层自 v4.7 起含三套独立编号**——21 CFR Part 117〔§ 117.xxx〕、"
              "Part 113〔§ 113.xxx〕、Part 114〔§ 114.xxx〕，均为最终规则、具法律约束力")
    new_cp = ("先分层再引用：**法规正文层自 v4.9 起含四套独立编号**——21 CFR Part 117〔§ 117.xxx〕、"
              "Part 113〔§ 113.xxx〕、Part 114〔§ 114.xxx〕、Part 123〔§ 123.xxx〕，均为最终规则、具法律约束力")
    rep(AB, old_cp, new_cp, "core_principles 三套→四套")

    # 在 core_principles 末尾（"三套法规正文…" 那条之后）追加两条 FSVP/海产品原则
    anchor_cp = ('"三套法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕各自独立编号')
    t = load(AB)
    # 取该行整行
    import re
    m = re.search(r"(?m)^(\s*)" + re.escape(anchor_cp) + r".*$", t)
    assert m, "找不到三套法规正文整行"
    indent = m.group(1)
    line = m.group(0)
    add = (line + "\n"
           + indent + '"海产品 part 123 与 Part 117 的接口是双向锁定：〔§ 123.5(a)〕明文 `Except as provided by § 117.5(b), '
           + 'parts 110 and 117 of this chapter apply`（默认适用），〔§ 117.5(b)〕给 `required to comply with, and are in '
           + 'compliance with, part 123` 的条件性豁免；但 §117.5(b) 没有 part 113〔§ 117.5(d)(2)〕那样的『仅限微生物危害』'
           + '限缩款——既不得把 part 113 口径搬来低估豁免，也不得因无限缩就推成整厂免检，边界是〔§ 123.3(k)〕的 processing '
           + '及其 (k)(2) 三项排除",\n'
           + indent + '"[§ 123.15〕〔§ 123.20〕的 `augments subpart A` 是叠加而非替代（漏 Subpart A 的 HACCP 计划/纠正措施/验证/记录/培训即漏项）；'
           + '〔§ 123.16〕的 `except those subject to part 113 or 114` 只排除该条自身，Subpart A 全套义务仍适用；'
           + '〔§ 123.12〕的进口商验证与 FSVP 是两套法源两套结构，deemed compliance 不覆盖 §123.12；'
           + '记录期〔§ 123.9(b)(1)〕冷藏 1 年 / 冷冻-保藏-货架稳定 2 年，与 Part 113 的 1+2 年、Part 114 的整段 3 年是三套口径不可串用",')
    _pending[AB] = t.replace(line, add, 1)
    print("core_principles +2 条")

    # ---------- 2. out_of_scope：海产品已收，改为 CP 7303.842 ----------
    rep(AB,
        '"海产品 HACCP（21 CFR part 123）与果汁 HACCP（21 CFR part 120）的专项要求",',
        '"果汁 HACCP（21 CFR part 120）的专项要求正文、海产品检查程序 CP 7303.842 正文与 NSSP Guide'
        '（海产品企业义务已由 CAP-22 覆盖〔§ 123.xxx〕正文，但检查员侧取证口径与贝类州际销售许可仍属未收）",',
        "out_of_scope 海产品改口")

    # ---------- 3. stop_conditions：追加两条 ----------
    anchor_sc = ('"LACF/AF 的管辖判定三禁：')
    t = load(AB)
    m2 = re.search(r"(?m)^(\s*)" + re.escape(anchor_sc) + r".*$", t)
    assert m2, "找不到 LACF/AF 管辖判定三禁行"
    ind = m2.group(1)
    line2 = m2.group(0)
    add2 = (line2 + "\n"
            + ind + '"海产品管辖判定三禁：① 禁止把〔§ 117.5(b)〕的豁免套用 part 113〔§ 117.5(d)(2)〕的『仅限微生物危害』限缩——'
            + 'part 123 无该限缩款，两向误读都会错；② 禁止因『§117.5(b) 无限缩』就推成整厂免 Subparts C/G——边界是受 '
            + 'part 123 管辖的 activities，〔§ 123.3(k)(2)〕三项排除（纯捕捞或运输、船上暂存处理、零售）不在内，且豁免不含 '
            + 'Part 117 Subpart B 的 CGMP；③ 禁止把〔§ 123.16〕的 `except those subject to part 113 or 114` 读成『属 LACF/AF 就免 '
            + 'part 123』——排除的只是该条，Subpart A 全套仍适用",\n'
            + ind + '"Part 123 记录期不得写成统一 3 年：〔§ 123.9(b)(1)〕按产品类型分冷藏 1 年 / 冷冻-保藏-货架稳定 2 年，'
            + '(b)(2) 适宜性记录 2 年且起算点是其对产品的适用性；与〔§ 113.100(g)〕的 1+2 分段、〔§ 114.100(e)〕的整段 3 年是三套口径。'
            + '另 CP 7303.842 海产品检查程序、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、NSSP Guide、'
            + 'FDA Fish and Fishery Products Hazards and Controls Guidance 均未收，凡涉检查员取证量、贝类生长区分类、'
            + '组胺与河豚毒素限值一律标『转引未收』，不得从 Part 123 反推",')
    _pending[AB] = _pending[AB].replace(line2, add2, 1)
    print("stop_conditions +2 条")

    for p, t in _pending.items():
        p.write_text(t, encoding="utf-8")
        print(f"写入 {p.name} ({len(t)} chars)")


if __name__ == "__main__":
    main()