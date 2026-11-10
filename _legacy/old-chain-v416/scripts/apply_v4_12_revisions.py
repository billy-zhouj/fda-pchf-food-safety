"""apply_v4_12_revisions.py — 把 CAP-25（21 CFR Part 108）接入 Capability Bundle

改动面（21 CFR Part 108 作为第十七来源）：
1. SLUGS 追加 emergency-permit-control（→ CAP-25）
2. ALSO_READ 双向链：与 CAP-20 / CAP-19 / CAP-22 及通用卡互连
3. additional_sources 追加第十七来源 src-21-cfr-part-108-2025
4. core_principles +2、stop_conditions +2
5. 全包「十六类 → 十七类」「24 张 → 25 张」「四套法规正文 → 五套」等**当前口径**同步
6. 清除既有条文中把 part 108 写成「未收」的**当前断言**（历史限定句保留）

纪律：所有替换走 rep_once（命中数必须为 1），结构性追加走结构定位 + 断言，
dry-run 全过才允许 --apply。
"""
from __future__ import annotations

import sys
from pathlib import Path

TARGET = Path(".cangjie/assemble_bundle.py")

# ── 定点替换（必须唯一命中）──────────────────────────────────────────────
REPLACEMENTS: list[tuple[str, str, str]] = [
    (
        "docstring-24->25",
        '"""assemble_bundle.py — 从 24 张 _meta-*.yaml',
        '"""assemble_bundle.py — 从 25 张 _meta-*.yaml',
    ),
    (
        "slugs-append",
        '         "seafood-inspection-program"]',
        '         "seafood-inspection-program",\n         "emergency-permit-control"]',
    ),
    # 描述层：第十七来源
    (
        "desc-count",
        "以及十六类来源不可混引与三层配对（法条 CAP-22 / 指南 CAP-23 / 检查程序 CAP-24）。",
        "以及十七类来源不可混引与三层配对（法条 CAP-22 / 指南 CAP-23 / 检查程序 CAP-24）。"
        "\"\n"
        "            \"另覆盖 LACF／酸化食品的紧急许可控制与注册备案（21 CFR Part 108 法规正文，4-1-25 Edition，11 页 / 9 条款）："
        "把「手续层」与「实体层」分开——Subpart A（§108.3/.5/.6/.7/.10/.12/.19）给许可裁定（3 个工作日异议、5 个工作日听证、"
        "听证后 5 个工作日裁定）、紧急性健康危害下的立即生效、许可签发或拒绝（10 个工作日可再延 10）、中止与恢复（立即中止 + 10 个工作日答复）、"
        "无证生产的产品扣留与事先书面批准（须证明 free from microorganisms of public health significance，20 个工作日答复）、"
        "以及「全部满足才豁免」的许可豁免；Subpart B 给注册（Form FDA 2541，首次从事后 10 天内，外国加工者报检前）与工艺备案"
        "（酸化食品 2541e / LACF 2541d·2541f·2541g，注册后 60 天内且包装新产品前）、停业 90 天通知、腐败与偏差报告、"
        "LACF 独立的微生物污染报告、召回程序文件、BPCS 受训主管、记录保存（108.25(g) 整段 3 年 vs 108.35(h) 1+2 年）。"
        "**核心纠偏：紧急许可不是常态义务**——108.25(a)/108.35(a) 均为 `may be required`，未履行义务只构成 `prima facie basis`；"
        "Subpart A 全是 working days、Subpart B 全是日历天，不可互换；外国加工者走 §801 拒绝入境而非紧急许可；"
        "108.35 独有的 FSIS 连续检验豁免、加州视为合规与 FOIA 豁免不得套到酸化食品。"
        "",
    ),
    # 原则 1：分层表述（四套 → 五套）
    (
        "principle-five-sets-a",
        "四套法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 123.xxx〕各自独立编号",
        "五套法规正文〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕各自独立编号",
    ),
    (
        "principle-count-a",
        "合计**十六类不可混引**（v4.8 新增第十三来源、v4.9 新增第十四来源 21 CFR Part 123、v4.10 新增第十五来源 FDA 海产品危害与控制指南、v4.11 新增第十六来源 CP 7303.842）",
        "合计**十七类不可混引**（v4.8 新增第十三来源、v4.9 新增第十四来源 21 CFR Part 123、v4.10 新增第十五来源 FDA 海产品危害与控制指南、v4.11 新增第十六来源 CP 7303.842、v4.12 新增第十七来源 21 CFR Part 108）",
    ),
    # 原则 2：引用规范
    (
        "principle-five-sets-b",
        "四套法规正文分别以〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 123.xxx〕标注",
        "五套法规正文分别以〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕标注",
    ),
    (
        "principle-uncited-list",
        "21 CFR part 1 subpart L / 108 / 110 / 120（part 123 自 v4.9 起已收）、",
        "21 CFR part 1 subpart L / 110 / 120（part 123 自 v4.9 起已收、part 108 自 v4.12 起已收）、",
    ),
    (
        "principle-count-b",
        "**十六类不可混引**，且 §114.5 并列 `parts 110 and 117` 不得改写或判为笔误",
        "**十七类不可混引**，且 §114.5 并列 `parts 110 and 117` 不得改写或判为笔误",
    ),
    # 停止条件：路由
    (
        "stop-routing",
        "用户任务超出 24 张能力卡路由范围时，明确告知超出本包覆盖，不要硬套；LACF/AF 的法规条文级义务先转 CAP-20，检查员侧取证转 CAP-19",
        "用户任务超出 25 张能力卡路由范围时，明确告知超出本包覆盖，不要硬套；LACF/AF 的实体工艺法条义务先转 CAP-20，注册备案与紧急许可程序转 CAP-25，检查员侧取证转 CAP-19",
    ),
    (
        "stop-count",
        "全包自 v4.11 起**十六类不可混引**，当前为 24 张能力卡",
        "全包自 v4.12 起**十七类不可混引**，当前为 25 张能力卡",
    ),
    # 清除「part 108 未收」的当前断言（保留 v4.11/CP 7303.070 条中已收项表述）
    (
        "uncited-part108-a",
        "**仍未收的是 21 CFR part 108**（FCE 注册、SID 定时工艺备案、Emergency Permit、§108.35 BPCS 认可）与 part 110 / 120（part 123 自 v4.9 起已收，见 CAP-22），一律标「转引未收」",
        "**21 CFR part 108 自 v4.12 起已收（见 CAP-25）**：FCE 注册、SID 定时工艺备案、Emergency Permit、§108.35 BPCS 认可现按〔§ 108.xxx〕引用；**仍未收的是** part 110 / 120（part 123 自 v4.9 起已收，见 CAP-22）与 2541 系列表单栏目细则，一律标「转引未收」",
    ),
    (
        "uncited-part108-b",
        "**仍未收** part 108（FCE/SID 备案、Emergency Permit、§108.35）、part 110 / 120（part 123 自 v4.9 起已收，见 CAP-22）",
        "**仍未收** part 110 / 120（part 123 自 v4.9 起已收，见 CAP-22；part 108 自 v4.12 起已收，见 CAP-25）",
    ),
    (
        "uncited-part108-c",
        "另 21 CFR part 120 / 1240 / 108 / 110 / 507 正文与 NSSP Guide 仍未收",
        "另 21 CFR part 120 / 1240 / 110 / 507 正文与 NSSP Guide 仍未收（part 108 自 v4.12 起已收，见 CAP-25）",
    ),
    # out_of_scope：108 从「超出覆盖」改为「表单细则超出覆盖」
    (
        "out-of-scope-108",
        "以及 21 CFR part 108 的 FCE/SID 备案与 Emergency Permit 程序（**21 CFR Part 113 / 114 法规正文自 v4.7 起已收，条款级义务清单见 CAP-20 `lacf-statutory-requirements`**；CP 7303.070 只给管辖分流与检查员取证口径）",
        "以及 2541 系列表单的栏目细则填写、FURLS / Center Views 的实际提交操作与许可申请举证材料组织（**21 CFR Part 113 / 114 法规正文自 v4.7 起已收，条款级义务清单见 CAP-20 `lacf-statutory-requirements`；21 CFR Part 108 自 v4.12 起已收，注册备案与紧急许可程序见 CAP-25 `emergency-permit-control`**；CP 7303.070 只给管辖分流与检查员取证口径）",
    ),
]

# 「21 CFR part 120 / 1240 / 108 / 110 / 507」在多处出现，全部移除 108（已收）
BULK = [
    ("uncited-list-108", "21 CFR part 120 / 1240 / 108 / 110 / 507", "21 CFR part 120 / 1240 / 110 / 507"),
]

NEW_ALSO_READ = '''
# v4.12：CAP-25 紧急许可控制（21 CFR Part 108）。与 CAP-20（Part 113/114 实体层）、
# CAP-19（CP 7303.070 检查员侧）构成 LACF/AF 的三层分工；另须连到监管边界、迎检、
# 取样、工艺验证、召回与 cGMP，以及海产品法条层（生食贝类与 LACF 交界）。
ALSO_READ["emergency-permit-control"] = [
    "lacf-statutory-requirements", "lacf-inspection-program",
    "regulatory-boundaries", "inspection-readiness", "inspection-sampling",
    "process-control-validation", "recall-plan", "cgmp-compliance-guide",
    "seafood-haccp-statutory-requirements",
]
for _s in ("lacf-statutory-requirements", "lacf-inspection-program",
           "regulatory-boundaries", "inspection-readiness", "inspection-sampling",
           "process-control-validation", "recall-plan", "cgmp-compliance-guide",
           "seafood-haccp-statutory-requirements", "hazard-analysis-method",
           "defect-action-levels"):
    if "emergency-permit-control" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("emergency-permit-control")

'''

NEW_SOURCE = '''            {
                "title": "21 CFR Part 108（2025 版）法规正文 — Emergency Permit Control",
                "author": "U.S. FDA（eCFR/GPO 现行文本）",
                "year": "2025",
                "content_type": "regulation（最终规则，具法律约束力）",
                "source_id": "src-21-cfr-part-108-2025",
                "source_file": "source-cfr-part108-2025.md",
                "note": "由用户提供的 GPO 印刷版 CFR-2025-title21-vol2-part108.pdf（175 KB，11 页，书页 248–258）经本包专用脚本 .cangjie/convert_cfr_part.py 双栏重排转出，再用 fix_part108_reflow.py 定点修 6 处重排缺陷（1 处正文句被误升为条款标题、4 处句中断段、1 处两编号项并段）。自检：9/9 条款命中（108.3/.5/.6/.7/.10/.12/.19/.25/.35）、页眉与独立页码残留 0、裁掉首部 Part 107 残段 9 段与尾部 Part 109 残段 14 段、串栏 0；逐字引用核对 27/27 命中、0 超 100 词、0 表格引用。⚠ 4–1–25 Edition 是 CFR 年度编纂版次（修订至 2025-04-01），不是 2025 新规；SOURCE 为 42 FR 14334, Mar. 15, 1977, unless otherwise noted。**法条定位**：Part 108 是 FD&C Act §404 的实施细则（AUTHORITY 21 U.S.C. 342, 344, 371），与 CAP-20 的 Part 113/114 构成「手续层 + 实体层」同一链条——Subpart A（108.3/.5/.6/.7/.10/.12/.19）给许可裁定/撤销/签发/中止/无证生产/豁免程序，Subpart B（108.25 酸化食品 / 108.35 LACF）给注册（Form FDA 2541，首次从事后 10 天内，外国加工者报检前）与工艺备案（2541e / 2541d / 2541f / 2541g，注册后 60 天内且包装新产品前）。**最易错处**：紧急许可是 `may be required` 的救济手段而非常态义务，触发前提是未履行 108.25/108.35 的义务（prima facie basis）；Subpart A 全是 working days（3/5/10/20），Subpart B 全是日历天（10/30/60/90），不可互换；记录保存 108.25(g) 整段 3 年 vs 108.35(h) 1+2 年，与 113.100(g)/114.100(e) 共四套口径；外国加工者走 §801 拒绝入境而非紧急许可。仍未收：2541 系列表单栏目细则、FURLS / Center Views 操作、21 CFR part 110 / 120 正文、CPG 全套、Import Alert 全文、BAM / AOAC / MPM 方法正文、IOM Ch.4",
            },
'''

NEW_PRINCIPLES = [
    "LACF/AF 的「手续层」与「实体层」必须分开答：21 CFR Part 108〔§ 108.xxx〕管注册（Form FDA 2541，首次从事后 10 天内；外国加工者报检前）、工艺备案（2541e/2541d/2541f/2541g，注册后 60 天内且包装新产品前）、停业 90 天通知、腐败与偏差与污染报告、召回程序文件、BPCS 受训主管、记录保存；CAP-20 的 Part 113/114 管 scheduled process、商业无菌、偏差处置等实体要求。**紧急许可不是常态义务**——108.25(a)/108.35(a) 均为 `may be required whenever the Commissioner finds ... that the commercial processor has failed to fulfill all the requirements of this section`，未履行只构成 `prima facie basis`，不是自动生效的许可；「LACF 企业必须持紧急许可证」是错误陈述",
    "Part 108 的时限有两种「日」，混用即答错：Subpart A 程序时限全是 working days（3 个工作日提异议、5 个工作日听证、听证后 5 个工作日裁定、许可申请 10 个工作日可再延 10、恢复申请 10 个工作日、无证产品放行 20 个工作日）；Subpart B 申报时限全是日历天（注册 10 天、备案 60 天、停业通知 90 天、工艺变更报送 30 天、延期批复 30 个工作日）。记录保存四套口径不得合并：108.25(g) 整段 3 年自生产日、108.35(h) 厂内 ≥1 年 + 另 2 年、113.100(g) 1+2 且可用 part 11 电子记录、114.100(e) 整段 3 年无 part 11 条款",
]

NEW_STOPS = [
    "回答 LACF／酸化食品的许可问题不得把紧急许可写成常态义务：108.25(a)／108.35(a) 的 `may be required` 触发前提是未履行注册、备案、报告、召回程序、BPCS 主管与记录义务，且只构成 `prima facie basis`；不得把 Subpart A 的 working days（3/5/10/20）套到 Subpart B 的日历天（10/30/60/90）上；不得把 108.25(g) 的整段 3 年与 108.35(h) 的 1+2 年、113.100(g) 的 1+2 年、114.100(e) 的整段 3 年合并成「3 年」一句；不得把外国加工者的 §801 拒绝入境路径（108.25(j)／108.35(k)）与国内企业的紧急许可路径混答；不得把 108.35 独有的 FSIS 连续检验豁免 (i)、加州视为合规 (j)(2)、FOIA 豁免 (l) 套到酸化食品上",
    "Part 108 的引用写「〔§ 108.xxx〕」并与〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕并列，不得混编号；108.25(a) 的 `§§ 114.10, 114.80(a) (1) and (2), and (b), 114.83, 114.89, and 114.100 (b), (c), and (d)` 不得简写成「§§ 114.10–114.100」（印刷版括号内空格是原文形态，简写即失去逐字性）；备案 `Filing of this information does not constitute approval` 不得读成「等 FDA 批准才能生产」；108.35(c)(2)(ii) 的「升参数不算变更」与 (c)(2)(iii) 的「operating process 不算修改」不得反推为「任何工艺调整都无需报告」——降初温／降杀菌温度／缩短时间／改配方仍须事前证实 + 30 天内报送",
]


def rep_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"FAIL [{label}] 期望 1 处命中，实得 {n} 处：{old[:80]!r}")
    return text.replace(old, new, 1)


def insert_before_block_close(text: str, header: str, payload: str, label: str) -> str:
    """在 `"<header>": [` 对应的列表闭合处（8 空格 + `],`）之前插入 payload。"""
    i = text.find(header)
    if i < 0:
        raise SystemExit(f"FAIL [{label}] 找不到锚点 {header!r}")
    j = text.find("\n        ],", i)
    if j < 0:
        raise SystemExit(f"FAIL [{label}] 找不到列表闭合")
    return text[:j] + payload + text[j:]


def main() -> int:
    apply = "--apply" in sys.argv
    text = TARGET.read_text(encoding="utf-8")
    original = text

    for label, old, new in REPLACEMENTS:
        text = rep_once(text, old, new, label)
        print(f"OK   [rep]  {label}")

    for label, old, new in BULK:
        n = text.count(old)
        if n == 0:
            raise SystemExit(f"FAIL [{label}] 未命中")
        text = text.replace(old, new)
        print(f"OK   [bulk] {label} × {n}")

    # ALSO_READ 插入到 ROUTER_GATE 之前
    anchor = "ROUTER_GATE = {"
    if text.count(anchor) != 1:
        raise SystemExit("FAIL [also-read] ROUTER_GATE 锚点不唯一")
    text = text.replace(anchor, NEW_ALSO_READ.lstrip("\n") + "\n" + anchor, 1)
    print("OK   [struct] also_read 12 条链")

    # additional_sources 追加第十七来源
    text = insert_before_block_close(
        text, '"additional_sources": [', NEW_SOURCE, "additional-sources")
    print("OK   [struct] additional_sources +1（src-21-cfr-part-108-2025）")

    # core_principles +2
    payload = "".join(f'            "{p}",\n' for p in NEW_PRINCIPLES)
    text = insert_before_block_close(
        text, '"core_principles": [', payload, "core-principles")
    print(f"OK   [struct] core_principles +{len(NEW_PRINCIPLES)}")

    # stop_conditions +2
    payload = "".join(f'            "{p}",\n' for p in NEW_STOPS)
    text = insert_before_block_close(
        text, '"stop_conditions": [', payload, "stop-conditions")
    print(f"OK   [struct] stop_conditions +{len(NEW_STOPS)}")

    if not apply:
        print(f"\n[dry-run] 变更后长度 {len(text)}（原 {len(original)}），未写盘。"
              f"加 --apply 落地。")
        return 0

    TARGET.write_text(text, encoding="utf-8")
    print(f"\n已写盘：{TARGET}（{len(text)} 字节）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
