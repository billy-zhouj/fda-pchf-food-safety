"""apply_v4_9_docs.py — v4.9 状态文档同步（PIPELINE_STATE / BOOK_OVERVIEW / DIGEST）。

原子写盘：全部编辑先在内存完成，末尾一次性落盘。
"""
from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PS = BASE / "PIPELINE_STATE.md"
BO = BASE / "BOOK_OVERVIEW.md"
DG = BASE / "DIGEST.md"

_pending: dict[Path, str] = {}


def load(p: Path) -> str:
    if p not in _pending:
        _pending[p] = p.read_text(encoding="utf-8")
    return _pending[p]


def rep(p: Path, old: str, new: str, label: str) -> None:
    t = load(p)
    n = t.count(old)
    assert n == 1, f"{p.name} [{label}]: expected 1 hit, got {n}: {old[:80]!r}"
    _pending[p] = t.replace(old, new, 1)
    print(f"  {p.name:20s} {label}: ok")


V49_PS = """

## v4.9 — 海产品 HACCP 法条层（21 CFR Part 123）与 Part 117 条件性豁免接口

- **新增来源（第十四类）**：`source-cfr-part123-2025.md` — 21 CFR Part 123《Fish and Fishery Products》，**4–1–25 Edition**（修订至 2025-04-01，书页 456–464，9 页 / **13 条款**）。用户提供的 `CFR-2025-title21-vol2-part123.pdf`（170 KB）经 `.cangjie/convert_cfr_part.py` 双栏重排转出。自检：13/13 条款命中（123.3 / .5 / .6 / .7 / .8 / .9 / .10 / .11 / .12 / .15 / .16 / .20 / .28）、页眉与独立页码残留 0、卷首 Sec. 目录区裁 34 行（13 条目录条目）、尾部 Part 124 残段裁 19 段、串栏 0、最终 41,669 chars。
- **转换脚本两处缺陷与修复（本轮工程发现）**：
  1. **假 H2**：§123.8(b) 正文里的跨条引用 `§ 123.7 whenever any verification procedure ... reveals the need` 被 `start_patterns` 误判为条款标题，产出多余 H2。修法：§ 起点要求条号后同行接**大写起首**标题词，或**条号独占一行**（GPO 印刷版常见「§ 123.3 / Definitions.」两行式）。Part 113 / 114 回归测试条款数仍为 10 / 8，无回归。
  2. **卷首目录并段**：`Sec.` 后的目录条目不是段起点，被 `^\d{3}\.\d+\s+[A-Z]` 与 Subpart 规则反复拼接，产出 `### Subpart B—… 123.15 General. 123.16 Process controls.` 残行。新增 `drop_toc()` 整体裁掉 PART 行到 AUTHORITY/SOURCE 之间的目录区。
- **版本口径**：`4–1–25 Edition` 是 CFR **年度编纂版次**，**不是** 2025 新规则；SOURCE `60 FR 65197, Dec. 18, 1995`，§123.5 与 §123.11 经 `80 FR 56167 (2015-09-17)` 修订（PCHF conforming amendment）。本件**不是** CP 7303.842。
- **核心法条接口（双向锁定，逐字核对）**：
  - 〔§ 123.5(a)〕`Except as provided by § 117.5(b), parts 110 and 117 of this chapter apply in determining whether ...` —— Part 110/117 **默认适用**，§117.5(b) 是**唯一**例外出口。
  - 〔§ 117.5(b)〕`Subparts C and G of this part do not apply with respect to activities that are subject to part 123 ... if you are required to comply with, and are in compliance with, part 123 of this chapter with respect to such activities.` —— 与 part 113〔§ 117.5(d)(1)〕**同构**的条件性豁免。
  - ⚠ **关键差异**：part 113 有〔§ 117.5(d)(2)〕把豁免限缩到「part 113 管辖的微生物危害」；**§117.5(b) 没有对应限缩款**。故两向误读都会错：搬 part 113 口径 → 低估豁免；因无限缩就推成整厂免检 → 高估豁免（边界是受 part 123 管辖的 **activities**，〔§ 123.3(k)(2)〕三项排除不在内，且豁免不含 Part 117 **Subpart B** 的 CGMP）。
- **其它已钉死的口径**：〔§ 123.15〕〔§ 123.20〕`augments subpart A` 是**叠加非替代**；〔§ 123.16〕的 `except those subject to part 113 or 114` **只排该条**、Subpart A 全套仍适用（与〔§ 123.20〕整体不适用 Subpart C 的处理不同）；〔§ 123.6(c)(1)〕危害考虑清单为 **(i)–(ix) 九项**且措辞是 `Consideration should be given`（非强制穷举，但漏考虑属危害分析缺陷）；〔§ 123.7(c)(1)〕**先隔离扣留**再评审；〔§ 123.8(a)(3)(i)(ii)〕CCP 与纠正措施记录**1 周内**复审、(a)(1) 变更时及**至少每年**复审且不足时须立即改；〔§ 123.9(b)(1)〕记录期**冷藏 1 年 / 冷冻-保藏-货架稳定 2 年**；〔§ 123.11(a)〕SSOP 用 `should` 而 (b)(c) 监测记录用 `shall`（原文措辞，非转换错误）；〔§ 123.12〕进口商二选一 + affirmative steps (A)–(F)，competent third party 可代写程序，无等效保证即视为掺假并**拒绝入境**；〔§ 123.28〕贝类须来自 approved growing waters、shellstock 须附 tag 五要素、shucked 标签须符合 §1240.60(c)。
- **与 FSVP 的分工（易混点）**：§123.12 法源为 Part 123 + FD&C Act，FSVP 法源为 FD&C Act §805 + 21 CFR part 1 subpart L；两套可共用证据但**互不替代**；FSVP 的 deemed compliance 明文只免 FSVP 且保留 §1.509，**不覆盖 §123.12**。
- **新增能力卡 CAP-22**：`seafood-haccp-statutory-requirements`，importance `extended`，also_read 9 条，B1–B12 边界，A2 25 条触发。R 段 **33 个英文引用块全部逐字命中**（32 条 Part 123 + 1 条 §117.5(b)）。
- **引文核对脚本的自我验证缺陷（本轮重要发现）**：`verify_seafood_quotes.py` 初版直接对整份源文件做归一化匹配，而**文件头里我自己转述了 §117.5(b) 原文**，导致该条引文在「自己的文件头」里命中，形成自我验证循环。修法：`body_only()` 只取第一个 `## § ` 之后的正文区。修后第 2 条正确标为 `Part117`，其余 32 条 `Part123`，33/33 全中。同步核查了 `verify_fsvp_quotes.py`：它以第二个 H1 定位正文区，且 CP 878 文件头不含被核对引文，历史结论不受影响。
- **规模变化**：21 → **22 张卡**；162 → **172 条术语**（t163–t172）；95 → **105 条用例**（v4.9，`seafood-01..10`）；十三类 → **十四类来源**；core_principles 40 → **42**；out_of_scope 7 条（原「海产品 part 123 专项要求」条目已改为「CP 7303.842 正文 / NSSP Guide / part 120」）；stop_conditions 16 → **18**。
- **仍未收**：CP 7303.842 海产品检查程序正文、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、NSSP Guide、FDA《Fish and Fishery Products Hazards and Controls Guidance》4th ed.、Import Alert 16-xx 系列、BAM 海产品章节、组胺/河豚毒素/雪卡毒素限值。
- **评测状态**：本版**未重跑**触发 / 输出 / 路由评测；v4.7 的 F1 1.000 / 0.994、输出 10/10、路由 40/40 均为历史版本结论，**不得冒用**；10 条 `seafood-*` 用例与 CAP-22 路由待补测。
"""

V49_BO = """

## v4.9 — 海产品 HACCP 法条层（21 CFR Part 123）

**第十四来源**：`source-cfr-part123-2025.md` — 21 CFR Part 123《Fish and Fishery Products》，4-1-25 Edition（9 页 / 13 条款）。用户提供的 `CFR-2025-title21-vol2-part123.pdf` 经 `.cangjie/convert_cfr_part.py` 双栏重排转出；13/13 条款命中、页眉页码残留 0、卷首目录区裁 34 行、串栏 0。

**新增 CAP-22 `seafood-haccp-statutory-requirements`**：把水产品企业义务从「只能靠 CP 7303.842 反推」升级为条款级法定义务。B1–B12 边界、A2 25 条触发、R 段 33 个引用块逐字核验（32 条 Part 123 + 1 条 §117.5(b)）。

**五处高频误读已钉死**：
1. **默认适用，例外只有一扇门**：〔§ 123.5(a)〕`Except as provided by § 117.5(b), parts 110 and 117 ... apply`；不是「做水产品就只按 part 123 管」。
2. **§117.5(b) 无限缩款**：part 113 有〔§ 117.5(d)(2)〕把豁免限缩到微生物危害，**part 123 没有**。搬前者口径会低估豁免；因「没限缩」推成整厂免检会高估。边界是受 part 123 管辖的 activities（〔§ 123.3(k)(2)〕三项排除不在内），且豁免不含 Part 117 Subpart B 的 CGMP。
3. **Subpart B/C 是 augments 叠加**：〔§ 123.15〕〔§ 123.20〕原文 `augments subpart A`，漏 Subpart A 即漏项。
4. **§123.16 例外只排一条**：`except those subject to part 113 or 114` 只排除该条；Subpart A 全套仍适用（与〔§ 123.20〕整体不适用 Subpart C 不同）。
5. **记录期三套口径不可串**：〔§ 123.9(b)(1)〕冷藏 1 年 / 冷冻-保藏-货架稳定 2 年；Part 113〔§ 113.100(g)〕1+2 分段；Part 114〔§ 114.100(e)〕整段 3 年。

**另钉两处**：〔§ 123.11(a)〕SSOP 是 `should`、(b)(c) 监测记录是 `shall`（原文措辞，不得升格也不得说可以不做）；〔§ 123.12〕进口商验证与 FSVP 是**两套法源**，deemed compliance 不覆盖 §123.12。

**规模**：22 张能力卡 / 172 条术语 / 105 条测试用例 / **十四类来源**（v4.9）。

**本版未重跑评测**：v4.7 的 F1 1.000 / 0.994、输出 10/10、路由 40/40 均为历史结论，不得冒用；10 条 `seafood-*` 与新卡路由待测。
"""

V49_DG = """
**v4.9 再加第七张法条卡 `seafood-haccp-statutory-requirements`（CAP-22）**：纳入第十四来源 21 CFR Part 123《Fish and Fishery Products》（4-1-25 Edition，9 页 / 13 条款），把海产品义务从「靠 CP 7303.842 反推」升级为条款级法定义务。重点钉死 §123.5(a) 默认适用与 §117.5(b) 双向锁定、§117.5(b) 缺 part 113 的微生物危害限缩款、Subpart B/C 的 augments 叠加语义、§123.16 例外只排一条、三套记录期口径不可串用，以及 §123.12 与 FSVP 的双轨互不替代。同时修复转换脚本两处缺陷（跨条引用被误提升为 H2、卷首 Sec. 目录并段）与引文核对脚本的一处自我验证循环（文件头转述被当成原文命中）。
"""


def main() -> None:
    for p in (PS, BO, DG):
        assert p.exists(), p

    # ---------- PIPELINE_STATE ----------
    rep(PS,
        "- **当前版本**: v4.8 ✅ 全部完成，已安装到用户级技能目录（21 张卡 / 162 术语 / 95 用例 / 十三类来源 / dist-v12）",
        "- **当前版本**: v4.9 ✅ 编译校验并安装完成（22 张卡 / 172 术语 / 105 用例 / 十四类来源 / dist-v13）",
        "头部当前版本")

    t = load(PS)
    _pending[PS] = t.rstrip("\n") + "\n" + V49_PS
    print(f"  {PS.name:20s} 追加 v4.9 版本节: ok")

    # ---------- BOOK_OVERVIEW ----------
    rep(BO,
        "**当前规模**：21 张能力卡 / 162 条术语 / 95 条测试用例 / 十三类来源（v4.8，dist-v12）。",
        "**当时规模**：21 张能力卡 / 162 条术语 / 95 条测试用例 / 十三类来源（v4.8）；**当前规模见文末 v4.9 节**。",
        "当前规模改为当时规模")

    rep(BO,
        "**十三类不可混引**：21 CFR Part 117 / PCHF 行业指南 / L.mono Draft Guidance / SECG / 过敏原 Ed.5 / "
        "Food Defect Levels Handbook / CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / "
        "21 CFR Part 113 / 21 CFR Part 114 / **CP 7303.878**",
        "**十三类不可混引（v4.8 口径，v4.9 起为十四类）**：21 CFR Part 117 / PCHF 行业指南 / L.mono Draft Guidance / "
        "SECG / 过敏原 Ed.5 / Food Defect Levels Handbook / CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / "
        "CP 7303.070 / 21 CFR Part 113 / 21 CFR Part 114 / CP 7303.878",
        "十三类标注历史口径")

    t = load(BO)
    _pending[BO] = t.rstrip("\n") + "\n" + V49_BO
    print(f"  {BO.name:20s} 追加 v4.9 版本节: ok")

    # ---------- DIGEST ----------
    rep(DG,
        "> 以上是 Stage 5 初版（v1.x）的交付快照，**不是当前状态**。当前为 **v4.8：21 张能力卡 / 162 条术语 / 95 条测试用例 / 十三类来源**",
        "> 以上是 Stage 5 初版（v1.x）的交付快照，**不是当前状态**。当前为 **v4.9：22 张能力卡 / 172 条术语 / 105 条测试用例 / 十四类来源**",
        "DIGEST 当前版本")

    t = load(DG)
    _pending[DG] = t.rstrip("\n") + "\n" + V49_DG
    print(f"  {DG.name:20s} 追加 v4.9 段: ok")

    for p, t2 in _pending.items():
        p.write_text(t2, encoding="utf-8")
    print("\n三份状态文档 v4.9 同步完成")


if __name__ == "__main__":
    main()