"""apply_v4_12_residue.py — v4.12 口径回补：把「part 108 未收」的当前断言改为已收

顺序纪律（不能反）：
1. 先做**逐行改写**（这些 old 字符串里含「十六类」，若先跑全局替换就匹配不上）；
2. 再跑全局「十六类 → 十七类」（38 处，卡内无「第十六类」子串，已核对为 0，
   故不存在「第十五类」式误伤）；
3. 最后把紧邻「十七类」的 `v4.11 起` 校为 `v4.12 起`（v4.11 时该计数仍是十六类）。
"""
from __future__ import annotations

import sys
from pathlib import Path

CARDS = Path(".cangjie/capabilities/cards")

R = "lacf-statutory-requirements.md"
L = "lacf-inspection-program.md"
S = "seafood-haccp-statutory-requirements.md"
G = "seafood-hazards-controls-guide.md"
C = "cgmp-compliance-guide.md"
T = "reference-tools-discipline.md"
D = "defect-action-levels.md"

REWRITES: list[tuple[str, str, str, str]] = [
    # ── CAP-20 低酸法条卡：四处「未收」断言 + B1 缺口段 ──────────────────
    (
        R, "cap20-header",
        "*⚠ **正文本包仍未收**：21 CFR **part 108**（FCE 注册 / SID 定时工艺备案 / Emergency Permit Control / §108.35 BPCS 认可）与 **part 110**（旧 CGMP，含 §110.110）。两者在本卡里一律标「转引未收」，不得从 Part 113/114 或 CP 反推条文。*",
        "*⚠ **part 108 自 v4.12 起已收**（第十七来源，CAP-25 `emergency-permit-control`）：FCE 注册 / SID 定时工艺备案 / Emergency Permit Control / §108.35 BPCS 认可现按〔§ 108.xxx〕引用，不再标「转引未收」。**仍未收的是 part 110**（旧 CGMP，含 §110.110，正文未收）——涉及 §110.110 一律标「转引未收」，不得从 Part 113/114 或 CP 反推条文。*",
    ),
    (
        R, "cap20-a2-9",
        "9. 用户问「scheduled process 谁能定 / Process Authority 是法条要求吗」→ 〔§ 113.83〕〔§ 114.83〕；FCE/SID 备案在 part 108，**转引未收**。",
        "9. 用户问「scheduled process 谁能定 / Process Authority 是法条要求吗」→ 〔§ 113.83〕〔§ 114.83〕；FCE 注册与工艺备案（SID）在〔§ 108.25(c)〕〔§ 108.35(c)〕，**转 CAP-25**（v4.12 起已收）。",
    ),
    (
        R, "cap20-a2-10",
        "10. 用户问「BPCS 证书 / Better Process Control School 是哪个法条」→ 〔§ 113.10〕〔§ 114.10〕；§108.35 与 part 110 正文未收。",
        "10. 用户问「BPCS 证书 / Better Process Control School 是哪个法条」→ 〔§ 113.10〕〔§ 114.10〕，另〔§ 108.25(f)〕〔§ 108.35(g)〕的 `school approved by the Commissioner`（CAP-25）；part 110 正文仍未收。",
    ),
    (
        R, "cap20-a2-16",
        "16. 用户问「21 CFR part 108 的 FCE 注册 / SID / Emergency Permit 具体怎么备案」→ 正文未收，明确转出，不给条款级结论。",
        "16. 用户问「21 CFR part 108 的 FCE 注册 / SID / Emergency Permit 具体怎么备案」→ **转 CAP-25 `emergency-permit-control`**（v4.12 起已收），给〔§ 108.xxx〕条款级时限与表单；2541 系列表单栏目细则仍超本包。",
    ),
    (
        R, "cap20-step6",
        "**Step 6 — 收尾声明。** 每条结论标〔§ 113.xxx〕/〔§ 114.xxx〕/〔§ 117.xxx〕或「CP 7303.070 PART x」；涉及 part 108 / part 110 / part 120 / BAM / IOM Ch.4 / CPG / Import Alert 全文一律标「转引未收」（part 123 已收，写〔§ 123.xxx〕）。**十六类不可混引。**",
        "**Step 6 — 收尾声明。** 每条结论标〔§ 113.xxx〕/〔§ 114.xxx〕/〔§ 117.xxx〕/〔§ 108.xxx〕或「CP 7303.070 PART x」；涉及 part 110 / part 120 / BAM / IOM Ch.4 / CPG / Import Alert 全文一律标「转引未收」（part 123 已收，写〔§ 123.xxx〕；part 108 自 v4.12 起已收，写〔§ 108.xxx〕转 CAP-25）。**十七类不可混引。**",
    ),
    (
        R, "cap20-b1",
        "**B1 — 21 CFR part 108 正文仍未收，这是本卡最大缺口。** FCE（Food Canning Establishment）注册、SID / scheduled process 备案、Emergency Permit Control、§108.35 的 BPCS 认可都在 part 108；§114.10 明文回指 `§ 108.35 and part 113 of this chapter before March 16, 1979`，CP 7303.070 PART I/II 也反复援引。本包只有 CP 的转引，**不给备案流程、表单编号、时限或许可证结论**。用户已下载的 `CFR-2025-title21-vol2-part123.pdf` 已于 v4.9 纳入（见 CAP-22）；`part120.pdf` 正文本版仍未纳入。",
        "**B1 — 21 CFR part 108 的缺口已于 v4.12 闭合（本卡此前的最大缺口）。** FCE（Food Canning Establishment）注册、SID / scheduled process 备案、Emergency Permit Control、§108.35 的 BPCS 认可都在 part 108；§114.10 明文回指 `§ 108.35 and part 113 of this chapter before March 16, 1979`，CP 7303.070 PART I/II 也反复援引。该件自 v4.12 起已作为**第十七来源**纳入（`source-cfr-part108-2025.md`），条款级手续义务见 **CAP-25 `emergency-permit-control`**〔§ 108.xxx〕——含注册（Form FDA 2541，10 天内／外国加工者报检前）、工艺备案（2541e/2541d/2541f/2541g，60 天内）、许可裁定与中止恢复、无证生产的产品放行闸门。仍不给的是 2541 系列**表单栏目细则**与 FURLS / Center Views 操作。⚠ 本卡与 CAP-25 的分工：本卡＝实体工艺法条层（Part 113/114），CAP-25＝手续与程序法条层（Part 108），**不得互相反推**。`part120.pdf` 正文本版仍未纳入。",
    ),
    (
        R, "cap20-b10",
        "**B10 — 本卡不覆盖的内容。** 21 CFR part 108 / 110 / 120 正文（part 123 见 CAP-22）、F0/D/z 值与温度分布/热穿透研究设计、BAM / AOAC / MPM 方法正文、IOM Chapter 4 Sample Schedule Chart 2、CPG 全套、Import Alert 99-37/99-38 全文、FURLS / Center Views 系统操作、Form 2541e 表单细则、以及杀菌工艺计算与验证方案审批 —— 均须另行复核或由具备资质的 Process Authority / PCQI 判断。",
        "**B10 — 本卡不覆盖的内容。** 21 CFR part 110 / 120 正文（part 123 见 CAP-22；part 108 自 v4.12 起已收、手续义务见 CAP-25）、F0/D/z 值与温度分布/热穿透研究设计、BAM / AOAC / MPM 方法正文、IOM Chapter 4 Sample Schedule Chart 2、CPG 全套、Import Alert 99-37/99-38 全文、FURLS / Center Views 系统操作、2541 系列表单栏目细则、以及杀菌工艺计算与验证方案审批 —— 均须另行复核或由具备资质的 Process Authority / PCQI 判断。",
    ),
    # ── CAP-19 检查程序卡：四处 ─────────────────────────────────────────
    (
        L, "cap19-quote-tag",
        "> —— CP 7303.070 PART I（PDF p4；`21 CFR part 108` 正文未收）",
        "> —— CP 7303.070 PART I（PDF p4；`21 CFR part 108` 正文自 v4.12 起已收，见 CAP-25）",
    ),
    (
        L, "cap19-b11a",
        "`21 CFR part 108 / 110 / 120` 只能写「转引未收」（part 123 已收，写〔§ 123.xxx〕转 CAP-22）",
        "`21 CFR part 110 / 120` 只能写「转引未收」（part 123 已收，写〔§ 123.xxx〕转 CAP-22；part 108 自 v4.12 起已收，写〔§ 108.xxx〕转 CAP-25）",
    ),
    (
        L, "cap19-b11b",
        "遇到需要 part 108/110 条文、BAM 方法、IOM Ch.4 抽样表、CPG 520.200/520.300、Import Alert 全文的具体问题，直接转出本包；遇到需要 113/114 条文的问题，**转 CAP-20 而非转出本包**。",
        "遇到需要 part 110 条文、BAM 方法、IOM Ch.4 抽样表、CPG 520.200/520.300、Import Alert 全文的具体问题，直接转出本包；遇到需要 113/114 条文的问题**转 CAP-20**、需要 108 的手续与许可程序**转 CAP-25**，而非转出本包。",
    ),
    (
        L, "cap19-b2",
        "**B2 — 21 CFR Part 113 / 114 正文已收（v4.7）、part 123 已收（v4.9，CAP-22），part 108 / 110 / 120 仍未收。** 本卡所有涉及 FCE 注册、SID 备案、Emergency Permit 的内容，都是 **CP 里的转引**（法源 part 108，正文未收）；涉及 scheduled process、商业无菌、人员培训、记录保存、偏差处置等**法条义务**的内容，现应转 **CAP-20 `lacf-statutory-requirements`** 并按〔§ 113.xxx〕〔§ 114.xxx〕引用，不得再标「转引未收」。⚠ 仍需标「转引未收」的：21 CFR part 108（含 §108.35 BPCS 认可）、part 110（旧 CGMP，含 §110.110；**至今有效**、见 CAP-20 B2 纠错）、part 120（果汁 HACCP）、IOM Chapter 4（Sample Schedule Chart 2）、BAM Ch.13B/14/17/21A/22A–22D、CPG Sec. 520.200/520.300、Import Alert 99-37/99-38 全文、SOP-001642、RPM Ch.4/9、21 CFR part 507 正文（CP 7303.842 自 v4.11 起已收，见 CAP-24；但它回指的 CPG / BAM 判据全文仍未收）。不得从 CP 的检查动作反推法条，也不得用 CP 的检查动作替代法规要求。",
        "**B2 — 21 CFR Part 113 / 114 正文已收（v4.7）、part 123 已收（v4.9，CAP-22）、part 108 已收（v4.12，CAP-25），part 110 / 120 仍未收。** 本卡涉及 FCE 注册、SID 备案、Emergency Permit 的内容，此前只能作 **CP 里的转引**；**v4.12 起法源 part 108 正文已纳入**，这一类问题应给〔§ 108.xxx〕条款级时限与表单（CAP-25），不再标「转引未收」；涉及 scheduled process、商业无菌、人员培训、记录保存、偏差处置等**法条义务**的内容，转 **CAP-20 `lacf-statutory-requirements`** 并按〔§ 113.xxx〕〔§ 114.xxx〕引用。⚠ 仍需标「转引未收」的：part 110（旧 CGMP，含 §110.110；**至今有效**、见 CAP-20 B2 纠错）、part 120（果汁 HACCP）、IOM Chapter 4（Sample Schedule Chart 2）、BAM Ch.13B/14/17/21A/22A–22D、CPG Sec. 520.200/520.300、Import Alert 99-37/99-38 全文、SOP-001642、RPM Ch.4/9、21 CFR part 507 正文、2541 系列表单栏目细则（CP 7303.842 自 v4.11 起已收，见 CAP-24；但它回指的 CPG / BAM 判据全文仍未收）。不得从 CP 的检查动作反推法条，也不得用 CP 的检查动作替代法规要求。",
    ),
    (
        L, "cap19-b12",
        "**B12 — 超出 21 张能力卡路由范围时明确告知。** 用户要 **LACF/AF 的法规条文级义务清单 → 转 CAP-20 `lacf-statutory-requirements`**（v4.7 已收 Part 113/114 正文，不再转出本包）；但商业无菌计算、F0/D 值/z 值验证、TD/HP 研究设计、卷边解剖判读、BAM 培养步骤、part 108 备案流程、进口扣留应诉策略仍**超出本包覆盖**",
        "**B12 — 超出 25 张能力卡路由范围时明确告知。** 用户要 **LACF/AF 的法规条文级义务清单 → 转 CAP-20 `lacf-statutory-requirements`**（v4.7 已收 Part 113/114 正文，不再转出本包）；要**注册备案与紧急许可程序 → 转 CAP-25 `emergency-permit-control`**（v4.12 已收 Part 108 正文）；但商业无菌计算、F0/D 值/z 值验证、TD/HP 研究设计、卷边解剖判读、BAM 培养步骤、2541 表单栏目细则、进口扣留应诉策略仍**超出本包覆盖**",
    ),
    # ── CAP-22 / CAP-23 ───────────────────────────────────────────────
    (
        S, "cap22-header",
        "**part 108 / 110**、**NSSP Guide**。一律标「转引未收」；CP 7303.842 自 v4.11 起已收（CAP-24）",
        "**part 110**、**NSSP Guide**。一律标「转引未收」；part 108 自 v4.12 起已收（CAP-25），CP 7303.842 自 v4.11 起已收（CAP-24）",
    ),
    (
        S, "cap22-step7",
        "涉及 part 120 / 1240 / 108 / 110 / NSSP / BAM / CPG / Import Alert 全文一律标「转引未收」。指南层的危害分析判定链转 CAP-23 `seafood-hazards-controls-guide`，引用写「Seafood Hazards Guide 第 4 版 Ch.x / L####」，不得改写成条款号。**十六类不可混引。**",
        "涉及 part 120 / 1240 / 110 / NSSP / BAM / CPG / Import Alert 全文一律标「转引未收」（part 108 自 v4.12 起已收，写〔§ 108.xxx〕转 CAP-25）。指南层的危害分析判定链转 CAP-23 `seafood-hazards-controls-guide`，引用写「Seafood Hazards Guide 第 4 版 Ch.x / L####」，不得改写成条款号。**十七类不可混引。**",
    ),
    (
        G, "cap23-header",
        "21 CFR part 120（果汁 HACCP）／part 1240（贝类卫生）／part 108／part 110／part 507",
        "21 CFR part 120（果汁 HACCP）／part 1240（贝类卫生）／part 110／part 507（part 108 自 v4.12 起已收，见 CAP-25）",
    ),
    # ── CAP-15 cGMP / 参考工具纪律 ─────────────────────────────────────
    (
        C, "cap15-uncited",
        "**part 108（FCE/SID/Emergency Permit）、part 110（旧 CGMP，含 §110.110）、part 120 正文仍未收**，一律标「转引未收」",
        "**part 110（旧 CGMP，含 §110.110）、part 120 正文仍未收**，一律标「转引未收」；**part 108（FCE/SID/Emergency Permit）自 v4.12 起已收**（见 CAP-25，按〔§ 108.xxx〕引用）",
    ),
    (
        T, "ref-tools-108",
        "**21 CFR part 108 / 110 / 120 正文仍未收**（part 123 自 v4.9 起已收，见 CAP-22）",
        "**21 CFR part 110 / 120 正文仍未收**（part 123 自 v4.9 起已收，见 CAP-22；part 108 自 v4.12 起已收，见 CAP-25）",
    ),
    # ── 引用规范里的「四套」→「五套」（pack-level）─────────────────────
    (
        C, "cap15-b8-sets",
        "法规用〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 123.xxx〕（四套独立编号）",
        "法规用〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕（五套独立编号）",
    ),
    (
        "inspection-readiness.md", "cap16-b12-sets",
        "法规正文用〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 123.xxx〕四套独立编号",
        "法规正文用〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕五套独立编号",
    ),
    (
        R, "cap20-b8-sets",
        "〔§ 117.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕/〔§ 123.xxx〕四套法条各自独立",
        "〔§ 108.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕/〔§ 117.xxx〕/〔§ 123.xxx〕五套法条各自独立",
    ),
    (
        S, "cap22-b10-sets",
        "〔§ 117.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕/〔§ 123.xxx〕四套法条各自独立",
        "〔§ 108.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕/〔§ 117.xxx〕/〔§ 123.xxx〕五套法条各自独立",
    ),
    (
        D, "cap14-b4-sets",
        "法规正文层已扩为四套",
        "法规正文层已扩为五套（v4.12 加 Part 108〔§ 108.xxx〕，见 CAP-25）",
    ),
    (
        S, "cap22-header-sets",
        "*⚠ **本卡使全包效力分层再扩一层**：「法规正文层」现含 Part 117 / 113 / 114 / 123 **四套独立编号**。",
        "*⚠ **本卡使全包效力分层再扩一层**：「法规正文层」现含 Part 117 / 113 / 114 / 123 **四套独立编号**（**v4.12 起为五套：加 Part 108〔§ 108.xxx〕，见 CAP-25 `emergency-permit-control`**）。",
    ),
    (
        "fsvp-inspection-program.md", "cap21-b12",
        "**B12 — 超出 21 张能力卡路由范围时，明确告知超出本包覆盖，不要硬套。**",
        "**B12 — 超出 25 张能力卡路由范围时，明确告知超出本包覆盖，不要硬套。**",
    ),
]


def main() -> int:
    apply = "--apply" in sys.argv
    files: dict[Path, str] = {}
    for name, _label, _old, _new in REWRITES:
        p = CARDS / name
        if p not in files:
            files[p] = p.read_text(encoding="utf-8")

    # 阶段 1：逐行改写
    for name, label, old, new in REWRITES:
        p = CARDS / name
        t = files[p]
        n = t.count(old)
        if n != 1:
            print(f"FAIL [{label}] {name} 期望 1 处命中，实得 {n}", file=sys.stderr)
            print(f"      {old[:110]!r}", file=sys.stderr)
            return 1
        files[p] = t.replace(old, new, 1)
        print(f"OK   [rewrite] {label}")

    # 阶段 2：全局「十六类」→「十七类」
    total = 0
    for p, t in files.items():
        if "十六类" in t:
            n = t.count("十六类")
            total += n
            files[p] = t.replace("十六类", "十七类")
            print(f"OK   [count]   {p.name}: {n} 处")
    # 新卡本身也要扫
    for p in CARDS.glob("*.md"):
        if p in files:
            continue
        t = p.read_text(encoding="utf-8")
        if "十六类" in t:
            n = t.count("十六类")
            total += n
            files[p] = t.replace("十六类", "十七类")
            print(f"OK   [count]   {p.name}: {n} 处")
    print(f"OK   [count]   合计 {total} 处「十六类 → 十七类」")

    # 阶段 3：紧邻「十七类」的 v4.11 起 → v4.12 起
    fixed = 0
    for p, t in list(files.items()):
        buf = list(t)
        i = 0
        while True:
            j = t.find("十七类", i)
            if j < 0:
                break
            window_start = max(0, j - 30)
            k = t.rfind("v4.11 起", window_start, j)
            if k >= 0:
                buf[k:k + len("v4.11 起")] = list("v4.12 起")
                t = "".join(buf)
                fixed += 1
            i = j + 1
        files[p] = t
    print(f"OK   [version] {fixed} 处 `v4.11 起` 校为 `v4.12 起`")

    if not apply:
        print("\n[dry-run] 未写盘。加 --apply 落地。")
        return 0

    for p, t in files.items():
        p.write_text(t, encoding="utf-8")
    print(f"\n已写盘 {len(files)} 个文件。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
