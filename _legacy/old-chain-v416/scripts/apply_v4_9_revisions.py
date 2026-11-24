"""apply_v4_9_revisions.py — v4.9 回补：Part 123 → 第十四来源 / CAP-22 / 22 卡。

设计要点（沿用 v4.8 教训）：
  1. 每个替换 `assert count == 1`，锚点不唯一立即失败；
  2. 全部编辑先在内存 dict 中完成，末尾 flush() 一次性写盘 —— 避免第 N 处失败时
     前 N-1 处已写盘的半改状态；
  3. 失败时不留任何痕迹（原文件未动）。
"""
from __future__ import annotations

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CJ = BASE / ".cangjie"
CARDS = CJ / "capabilities/cards"

_pending: dict[Path, str] = {}


def load(p: Path) -> str:
    if p not in _pending:
        _pending[p] = p.read_text(encoding="utf-8")
    return _pending[p]


def rep(p: Path, old: str, new: str, label: str = "") -> None:
    t = load(p)
    n = t.count(old)
    assert n == 1, f"{p.name} [{label}]: expected 1 hit, got {n} for {old[:70]!r}"
    _pending[p] = t.replace(old, new, 1)


def rep_all(p: Path, old: str, new: str, expect: int, label: str = "") -> None:
    t = load(p)
    n = t.count(old)
    assert n == expect, f"{p.name} [{label}]: expected {expect} hits, got {n}"
    _pending[p] = t.replace(old, new)


def flush() -> None:
    for p, t in _pending.items():
        p.write_text(t, encoding="utf-8")
        print(f"  写入 {p.relative_to(BASE)}  ({len(t)} chars)")


def main() -> None:
    ab = CJ / "assemble_bundle.py"

    # ---------- 1. assemble_bundle.py ----------
    rep(ab, '         "lacf-statutory-requirements", "fsvp-inspection-program"]',
        '         "lacf-statutory-requirements", "fsvp-inspection-program",\n'
        '         "seafood-haccp-statutory-requirements"]',
        "SLUGS +seafood")

    # docstring 张数
    rep_all(ab, "21 张", "22 张", 2, "docstring/注释张数")

    # ALSO_READ 正向
    rep(ab, 'ALSO_READ["fsvp-inspection-program"] = [',
        'ALSO_READ["seafood-haccp-statutory-requirements"] = [\n'
        '    "lacf-statutory-requirements", "fsvp-inspection-program", "regulatory-boundaries",\n'
        '    "hazard-analysis-method", "chemical-hazard-controls", "supply-chain-verification",\n'
        '    "cgmp-compliance-guide", "inspection-readiness", "inspection-sampling",\n'
        ']\n\nALSO_READ["fsvp-inspection-program"] = [',
        "ALSO_READ 正向")

    # ALSO_READ 反向
    rep(ab,
        'for _s in ("supply-chain-verification", "regulatory-boundaries", "inspection-readiness",\n'
        '           "investigator-authority-procedure", "lacf-inspection-program",\n'
        '           "cgmp-compliance-guide"):\n'
        '    if "fsvp-inspection-program" not in ALSO_READ[_s]:\n'
        '        ALSO_READ[_s].append("fsvp-inspection-program")',
        'for _s in ("supply-chain-verification", "regulatory-boundaries", "inspection-readiness",\n'
        '           "investigator-authority-procedure", "lacf-inspection-program",\n'
        '           "cgmp-compliance-guide"):\n'
        '    if "fsvp-inspection-program" not in ALSO_READ[_s]:\n'
        '        ALSO_READ[_s].append("fsvp-inspection-program")\n\n'
        '# v4.9：Part 123 反向链。生食贝类/熏制水产品与 LACF 交界最紧，故 lacf 系与\n'
        '# regulatory-boundaries / hazard-analysis-method / chemical-hazard-controls\n'
        '# 都补反向引用；inspection-readiness 与 inspection-sampling 亦需可跳转。\n'
        'for _s in ("lacf-statutory-requirements", "fsvp-inspection-program",\n'
        '           "regulatory-boundaries", "hazard-analysis-method",\n'
        '           "chemical-hazard-controls", "supply-chain-verification",\n'
        '           "cgmp-compliance-guide", "inspection-readiness",\n'
        '           "inspection-sampling"):\n'
        '    if "seafood-haccp-statutory-requirements" not in ALSO_READ[_s]:\n'
        '        ALSO_READ[_s].append("seafood-haccp-statutory-requirements")',
        "ALSO_READ 反向")

    print("  assemble_bundle.py: SLUGS / ALSO_READ 完成")

    # additional_sources：插在 CP 7303.878 之后
    cp878_note_tail = (
        '仍未收：21 CFR part 1 subpart L / 111 / 112 / 120 / 123 / 507 正文、'
        'Import Alert 99-41 全文、FSVP Guidance for Industry、FSVP Implementation Work Instructions '
        '与 IP guidance tabs、HFP Enforcement Bulletin #13/#6、RPM 4-1-8、SOP-001642",')
    new_src = cp878_note_tail + '''
            {
                "title": "21 CFR Part 123 - Fish and Fishery Products (4-1-25 Edition)",
                "author": "U.S. Government Publishing Office / eCFR, 21 CFR Ch. I (4-1-25 Edition)",
                "year": "4–1–25 Edition（修订至 2025-04-01；书页 456–464，9 页 / 13 条款）",
                "content_type": "regulation（联邦法规正文，最终规则，具法律约束力）",
                "source_id": "src-fda-cfr-part123-2025",
                "source_file": "books/fda-pchf-human-food-guidance/source-cfr-part123-2025.md",
                "note": "由用户提供的 CFR-2025-title21-vol2-part123.pdf 经本包专用脚本 .cangjie/convert_cfr_part.py 双栏重排转出（未用 pdf2md-pro，后者会把同一 y 坐标的左右栏并成一行）。自检：13/13 条款命中、页眉与独立页码残留 0、卷首 Sec. 目录区裁掉 34 行、尾部 Part 124 残段裁 19 段、串栏 0。⚠ 版本判定：4–1–25 Edition 是 CFR 年度编纂版次（修订至 2025-04-01），不是 2025 新规则；SOURCE 60 FR 65197 (1995-12-18)，§123.5 与 §123.11 经 80 FR 56167 (2015-09-17) 修订。核心接口双向锁定：§123.5(a) 明写 `Except as provided by § 117.5(b), parts 110 and 117 of this chapter apply`，§117.5(b) 则给 `if you are required to comply with, and are in compliance with, part 123` 的条件性豁免 —— 与 part 113 的 §117.5(d)(1) 同构，但 §117.5(b) 没有 §117.5(d)(2) 那样的『仅限微生物危害』限缩款，两个方向的误读都要纠正。Subpart B/C 是 augments subpart A 的叠加而非替代。§123.16 的 except part 113/114 只排除该条、不排整 part。§123.12 进口商验证与 FSVP 是两套法源，deemed compliance 不覆盖 §123.12。§123.9(b)(1) 记录期为冷藏 1 年 / 冷冻-保藏-货架稳定 2 年，与 Part 113 的 1+2 年、Part 114 的整段 3 年是三套口径。仍未收：CP 7303.842 海产品检查程序、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、NSSP Guide、FDA Fish and Fishery Products Hazards and Controls Guidance。引用用〔§ 123.xxx〕。",
            },'''
    rep(ab, cp878_note_tail, new_src, "additional_sources +part123")

    # entry.description 追加
    desc_tail = ('以及 4.6/0.85/4.0 法定数字与 CP 7303.070 的 4.40/4.65 检查员触发线、'
                 'L.mono ≤4.4/≤0.92 建议层基准的三层区分。"')
    desc_new = ('以及 4.6/0.85/4.0 法定数字与 CP 7303.070 的 4.40/4.65 检查员触发线、'
                'L.mono ≤4.4/≤0.92 建议层基准的三层区分。"\n'
                '            "另覆盖海产品 HACCP 的条款级法定义务（21 CFR Part 123 法规正文，4-1-25 Edition）：'
                '按〔§ 123.3(d)(e)(k)〕判定 fish / fishery product 与 processing 范围及 (k)(2) 三项排除，'
                '〔§ 123.5(a)〕Part 110/117 默认适用与〔§ 117.5(b)〕双条件豁免（并指出该款无 part 113 §117.5(d)(2) 的微生物危害限缩），'
                '〔§ 123.15〕〔§ 123.20〕Subpart B/C 的 augments 叠加而非替代，'
                '〔§ 123.6〕危害分析与 HACCP 计划及 (c)(1) 九项危害考虑清单、〔§ 123.7〕纠正措施三条路径、'
                '〔§ 123.8〕验证含 1 周记录复审与至少每年复审、〔§ 123.9〕记录分类 1 年/2 年与即时报录、〔§ 123.10〕培训课程等效或岗位经验、'
                '〔§ 123.11〕SSOP 的 should 与监测记录的 shall 之别及八项卫生条件、'
                '〔§ 123.16〕熏制水产品肉毒控制覆盖货架期且 except 仅排 part 113/114 管辖者、'
                '〔§ 123.28〕双壳贝类源头控制与 tag 五要素、〔§ 123.12〕进口商二选一与 affirmative steps 及拒绝入境后果，'
                '并区分 §123.12 与 FSVP 双轨互不替代、三套记录期口径不可串用。"')
    rep(ab, desc_tail, desc_new, "entry.description +seafood")

    print("  assemble_bundle.py: additional_sources / description 完成")

    # 十三类 → 十四类
    rep_all(ab, "十三类", "十四类", 2, "全局十三类→十四类")

    # ---------- 2. 各卡 十三类 → 十四类 ----------
    card_hits = 0
    for c in sorted(CARDS.glob("*.md")):
        t = c.read_text(encoding="utf-8")
        if "十三类" in t:
            n = t.count("十三类")
            _pending[c] = t.replace("十三类", "十四类")
            card_hits += n
    print(f"  卡片 十三类→十四类: {card_hits} 处")

    # 新增卡自身已是十四类，无需处理；meta 里的过期关键词
    meta20 = CARDS / "_meta-lacf-statutory-requirements.yaml"
    t = meta20.read_text(encoding="utf-8")
    if "十三类不可混引" in t:
        _pending[meta20] = t.replace("十三类不可混引", "十四类不可混引")
        print("  CAP-20 meta 关键词同步")

    # ---------- 3. 来源文件头 ----------
    src_hits = 0
    for name in ("source-cfr-part113-2025.md", "source-cfr-part114-2025.md",
                 "source-cp-7303-070-2024.md", "source-cp-7303-878-2023.md"):
        p = BASE / name
        if not p.exists():
            print(f"  ⚠ 缺 {name}")
            continue
        t = p.read_text(encoding="utf-8")
        if "十三类" in t:
            n = t.count("十三类")
            _pending[p] = t.replace("十三类", "十四类")
            src_hits += n
    print(f"  来源文件头 十三类→十四类: {src_hits} 处")

    flush()
    print("\nv4.9 assemble 回补完成（内存暂存已全部落盘）")


if __name__ == "__main__":
    main()