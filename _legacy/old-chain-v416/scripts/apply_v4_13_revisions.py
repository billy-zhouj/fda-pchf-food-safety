"""apply_v4_13_revisions.py — 把 CAP-26（21 CFR Part 120 果汁 HACCP）接入 Capability Bundle

改动面（第十八来源）：
1. SLUGS 追加 juice-haccp（→ CAP-26）
2. ALSO_READ 双向链：与 CAP-15 / CAP-20 / CAP-22 / CAP-23 / CAP-24 / CAP-25 等互连
3. additional_sources 追加第十八来源 src-21-cfr-part-120-2025
4. core_principles +2、stop_conditions +2
5. 「十七类 → 十八类」「25 张 → 26 张」「五套法规正文 → 六套」等**当前口径**同步
6. 清除既有条文中把 part 120 写成「未收 / 超出覆盖」的**当前断言**

纪律：定点替换走 rep_once（命中数必须为 1），结构性追加走结构定位 + 断言，
dry-run 全过才允许 --apply。
"""
from __future__ import annotations

import sys
from pathlib import Path

TARGET = Path(".cangjie/assemble_bundle.py")

REPLACEMENTS: list[tuple[str, str, str]] = [
    ("docstring-25->26",
     '"""assemble_bundle.py — 从 25 张 _meta-*.yaml',
     '"""assemble_bundle.py — 从 26 张 _meta-*.yaml'),
    ("slugs-append",
     '         "emergency-permit-control"]',
     '         "emergency-permit-control",\n         "juice-haccp"]'),
    # 描述层：第十八来源
    ("desc-count",
     "以及十七类来源不可混引与三层配对（法条 CAP-22 / 指南 CAP-23 / 检查程序 CAP-24）。",
     "以及十八类来源不可混引与三层配对（法条 CAP-22 / 指南 CAP-23 / 检查程序 CAP-24）。"
     '"\n'
     '            "另覆盖果汁 HACCP 体系的完整法定义务链（21 CFR Part 120 法规正文，4-1-25 Edition，10 页 / 15 条款）：'
     "先按〔§ 120.1(a)〕定义 juice（含浓缩物与果泥、作饮料配料也算）并用〔§ 120.3(j)(2)〕排除采收采摘运输与零售经营、"
     "〔§ 120.3(l)〕判零售 establishment，再按〔§ 120.5〕确认 **Part 117 默认适用、〔§ 117.5(c)〕为唯一条件性出口（该款全文未收）**；"
     "Subpart A 给 SSOP 八项、书面危害分析五项与 prudent processor 判定、九项应考虑危害、HACCP 计划七要素（厂内/厂外 CCP 分列）、"
     "纠正措施五步（隔离扣留优先）、六类验证活动与 12 个月/每年确认、五类记录与通用要素、培训四职能、进口商二选一 + 六项 affirmative steps；"
     "Subpart B 给 **5-log（10⁵）法定削减**（持续、覆盖货架期、正常与中度滥用条件，目标菌为 pertinent microorganism）与"
     "**果面处理者专项的 biotype I E. coli 验证**（20 mL/1,000 加仑/生产日，7 次 2 阳性即视为控制措施不足）。"
     "**核心纠偏**：5-log 是 shall 不是建议；§120.25 只适用于果面处理者；120.24(a) 免的是 5-log 指标、120.7(e) 免的是 113/114 已控制的微生物类危害，两者对象不同；"
     "记录复审是 1 周（7 日历天）而非 7 个工作日；记录期为易腐 1 年 / 冷冻-保藏-货架稳定 2 年或货架期孰长，起算点为产品制备日"
     '"'),
    # 原则 1：分层（五套 → 六套）
    ("principle-six-sets-a",
     "五套法规正文〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕各自独立编号",
     "六套法规正文〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕各自独立编号"),
    ("principle-count-a",
     "合计**十七类不可混引**（v4.8 新增第十三来源、v4.9 新增第十四来源 21 CFR Part 123、v4.10 新增第十五来源 FDA 海产品危害与控制指南、v4.11 新增第十六来源 CP 7303.842、v4.12 新增第十七来源 21 CFR Part 108）",
     "合计**十八类不可混引**（v4.8 新增第十三来源、v4.9 新增第十四来源 21 CFR Part 123、v4.10 新增第十五来源 FDA 海产品危害与控制指南、v4.11 新增第十六来源 CP 7303.842、v4.12 新增第十七来源 21 CFR Part 108、v4.13 新增第十八来源 21 CFR Part 120）"),
    # 原则 2：引用规范
    ("principle-six-sets-b",
     "五套法规正文分别以〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕标注",
     "六套法规正文分别以〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕标注"),
    ("principle-uncited-120",
     "21 CFR part 1 subpart L / 110 / 120（part 123 自 v4.9 起已收、part 108 自 v4.12 起已收）、",
     "21 CFR part 1 subpart L / 110、§117.5(c) 逐字文本（part 123 自 v4.9 起已收、part 108 自 v4.12 起已收、part 120 自 v4.13 起已收）、"),
    # 停止条件：路由与计数
    ("stop-routing",
     "用户任务超出 25 张能力卡路由范围时，明确告知超出本包覆盖，不要硬套；LACF/AF 的实体工艺法条义务先转 CAP-20，注册备案与紧急许可程序转 CAP-25，检查员侧取证转 CAP-19",
     "用户任务超出 26 张能力卡路由范围时，明确告知超出本包覆盖，不要硬套；LACF/AF 的实体工艺法条义务先转 CAP-20，注册备案与紧急许可程序转 CAP-25，果汁 HACCP 转 CAP-26，检查员侧取证转 CAP-19"),
    ("stop-count",
     "全包自 v4.12 起**十七类不可混引**，当前为 25 张能力卡",
     "全包自 v4.13 起**十八类不可混引**，当前为 26 张能力卡"),
    # 清除「part 120 未收 / 超出覆盖」的当前断言
    ("uncited-120-a",
     "**仍未收的是** part 110 / 120（part 123 自 v4.9 起已收，见 CAP-22）与 2541 系列表单栏目细则",
     "**仍未收的是** part 110 与 §117.5(c) 逐字文本（part 123 自 v4.9 起已收，见 CAP-22；part 120 自 v4.13 起已收，见 CAP-26）以及 2541 系列表单栏目细则"),
    ("uncited-120-b",
     "**仍未收** part 110 / 120（part 123 自 v4.9 起已收，见 CAP-22；part 108 自 v4.12 起已收，见 CAP-25）",
     "**仍未收** part 110（part 123 自 v4.9 起已收，见 CAP-22；part 108 自 v4.12 起已收，见 CAP-25；part 120 自 v4.13 起已收，见 CAP-26）"),
    ("uncited-120-c",
     "另 21 CFR part 120 / 1240 / 110 / 507 正文与 NSSP Guide 仍未收（part 108 自 v4.12 起已收，见 CAP-25）",
     "另 21 CFR part 1240 / 110 / 507 正文与 NSSP Guide 仍未收（part 108 自 v4.12 起、part 120 自 v4.13 起已收，见 CAP-25 / CAP-26）"),
    # out_of_scope：120 从「专项要求正文超覆盖」改为「检查员口径超覆盖」
    ("out-of-scope-120",
     "果汁 HACCP（21 CFR part 120）的专项要求正文与 NSSP Guide",
     "果汁 HACCP 的检查员取证口径（CP 7303.047 未收，法条义务见 CAP-26）与 NSSP Guide"),
]

BULK = [
    ("uncited-list-120", "21 CFR part 120 / 1240 / 110 / 507", "21 CFR part 1240 / 110 / 507"),
]

NEW_ALSO_READ = '''
# v4.13：CAP-26 果汁 HACCP（21 CFR Part 120）。与 CAP-15（cGMP 底座）、CAP-20（Part 113/114）、
# CAP-22（Part 123 海产品 HACCP，同为 HACCP 体系但另立编号）、CAP-25（Part 108 手续层）交叉；
# 危害分析方法与验证、纠正措施、记录、过敏原、供应链、召回亦须可达。
ALSO_READ["juice-haccp"] = [
    "hazard-analysis-method", "process-control-validation", "cgmp-compliance-guide",
    "lacf-statutory-requirements", "seafood-haccp-statutory-requirements",
    "emergency-permit-control", "allergen-program", "recall-plan",
    "supply-chain-verification", "regulatory-boundaries", "inspection-readiness",
]
for _s in ("hazard-analysis-method", "process-control-validation", "cgmp-compliance-guide",
           "lacf-statutory-requirements", "seafood-haccp-statutory-requirements",
           "emergency-permit-control", "allergen-program", "recall-plan",
           "supply-chain-verification", "regulatory-boundaries", "inspection-readiness",
           "chemical-hazard-controls", "defect-action-levels"):
    if "juice-haccp" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("juice-haccp")

'''

NEW_SOURCE = '''            {
                "title": "21 CFR Part 120（2025 版）法规正文 — Hazard Analysis and Critical Control Point (HACCP) Systems",
                "author": "U.S. FDA（eCFR/GPO 现行文本）",
                "year": "2025",
                "content_type": "regulation（最终规则，具法律约束力）",
                "source_id": "src-21-cfr-part-120-2025",
                "source_file": "source-cfr-part120-2025.md",
                "note": "由用户提供的 GPO 印刷版 CFR-2025-title21-vol2-part120.pdf（176 KB，10 页，书页 439–448）经本包专用脚本 .cangjie/convert_cfr_part.py 双栏重排转出，再用 fix_part120_reflow.py 定点修 11 处段界缺陷（1 处句中断段 + 10 处编号项并段）。自检：15/15 条款命中（120.1/.3/.5/.6/.7/.8/.9/.10/.11/.12/.13/.14/.20/.24/.25）、页眉与独立页码残留 0、裁掉首部 Part 119 残段 3 段与尾部 Part 121 残段 6 段、串栏 0；逐字引用核对 26/26 命中、0 超 100 词、0 表格引用。⚠ 4–1–25 Edition 是 CFR 年度编纂版次（修订至 2025-04-01），不是 2025 新规；SOURCE 为 66 FR 6197, Jan. 19, 2001, unless otherwise noted，§120.5/§120.6 的 80 FR 56167（2015-09-17）是 PCHF 最终规则的 conforming amendment。**法条定位**：Part 120 是独立的果汁 HACCP 体系法规（不是「果汁版 Part 117」）；〔§ 120.5〕一句话锁定接口——`Except as provided by § 117.5(c), parts 110 and 117 ... apply`，即 Part 117 默认适用、§117.5(c) 为唯一条件性出口（**该款全文未收**，不得反推措辞）。**最易错五处**：① 5-log 是〔§ 120.24(a)〕的 shall（须持续、覆盖货架期、正常与中度滥用条件），不是指南建议；② 目标菌是 pertinent microorganism（最耐热＋具公共卫生意义＋可能出现于该果汁），不是沙门氏菌/O157；③ §120.25 的 biotype I E. coli 检测只适用于果面处理者（20 mL/1,000 加仑/生产日，7 次 2 阳性即视为不足），非通用出厂检验；④ 两处豁免对象不同——120.24(a)(1)(2) 免 5-log 指标、120.7(e) 免「part 113/114 已控制的微生物与微生物毒素」危害的计划处理；⑤ 记录复审是 `within 1 week (7 days)`（日历天，非 7 个工作日），记录期为易腐/冷藏 ≥1 年、冷冻/保藏/货架稳定 2 年或货架期孰长、起算点产品制备日，是独立第六套口径。⚠ 文本层缺陷：`5 log (i.e., 105)` 的 `105` 实为 10⁵ 上标丢失，引用须还原并注明。仍未收：§117.5(c) 逐字文本、21 CFR part 110 正文、CP 7303.047 果汁 program、CPG 与 Import Alert 全文、BAM / AOAC 方法全文",
            },
'''

NEW_PRINCIPLES = [
    "果汁 HACCP 必须先分层再引条款：21 CFR Part 120〔§ 120.xxx〕是**独立 HACCP 体系法规**，与 Part 117〔§ 117.xxx〕的关系由〔§ 120.5〕一句话锁定——`Except as provided by § 117.5(c), parts 110 and 117 ... apply`，即 **Part 117 默认适用**、〔§ 117.5(c)〕为唯一且**条件性**的出口（该款全文未收，不得据 §120.5 反推其措辞，也不得套用 §117.5(b)/(d) 的写法）。受 Part 120 管辖只换出口不换默认；违反 §120.6/§120.7/§120.8 由〔§ 120.9〕**直接**构成 FD&C Act 402(a)(4) 掺假，不经「不符合 CGMP」中转",
    "果汁的 5-log 是法定指标，两处豁免对象不同且都极窄：〔§ 120.24(a)〕`shall ... consistently produce, at a minimum, a 5 log (i.e., 10⁵) reduction`，须覆盖 **货架期**、在**正常与中度滥用条件**下成立，目标菌为 `pertinent microorganism`（最耐热＋具公共卫生意义＋可能出现在该果汁中）。豁免 (a)(1) 是受 part 113/114 管辖者、豁免 (a)(2) 是单次热力达货架稳定或含全部配料热处理的浓缩工艺（须把热力工艺副本放进〔§ 120.7〕危害分析）——**两者免的都只是 5-log 这一指标**，另有〔§ 120.7(e)〕免的是「part 113/114 已控制的微生物与微生物毒素」危害的计划处理，不减化学/物理/过敏原危害。§120.25 的 biotype I E. coli 检测只适用果面处理者（20 mL/1,000 加仑/生产日），不是通用出厂检验",
]

NEW_STOPS = [
    "回答果汁 HACCP 问题不得把 5-log 降格为建议层（〔§ 120.24(a)〕是 shall，且须持续、覆盖货架期、正常与中度滥用条件）；不得把目标菌答成沙门氏菌或大肠杆菌 O157（应为 pertinent microorganism，三条件同时成立）；不得把〔§ 120.25〕的 biotype I E. coli 检测写成所有果汁厂的强制出厂检验（仅果面处理者适用），也不得把果面处理厂的检测写成可选；不得据〔§ 120.5〕反推〔§ 117.5(c)〕的条文措辞；不得把两处豁免合并成「受 113/114 管辖就不用做果汁 HACCP」；不得把记录复审写成 7 个工作日（果汁是 1 week / 7 日历天）；不得把果汁记录期套成 3 年或统一 2 年（易腐/冷藏 ≥1 年、冷冻/保藏/货架稳定 2 年或货架期孰长，起算点产品制备日）；不得把〔§ 120.14〕与 FSVP 互相替代",
    "果汁 HACCP 的引用写「〔§ 120.xxx〕」并与〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕并列，六套编号互不混引；`5 log (i.e., 105)` 的 `105` 是 PDF 文本层上标丢失，逐字引用须还原为 10⁵ 并注明是文本层缺陷，不得照抄成「105 倍」；〔§ 117.5(c)〕逐字文本、part 110 正文、CP 7303.047 果汁 program、CPG 与 Import Alert 全文、BAM/AOAC 方法全文一律标「转引未收」；〔§ 120.24(a)(2)〕的豁免以「热力工艺副本已纳入书面危害分析」为条件，答豁免时不得省略该条件",
]


def rep_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"FAIL [{label}] 期望 1 处命中，实得 {n} 处：{old[:80]!r}")
    return text.replace(old, new, 1)


def insert_before_block_close(text: str, header: str, payload: str, label: str) -> str:
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

    anchor = "ROUTER_GATE = {"
    if text.count(anchor) != 1:
        raise SystemExit("FAIL [also-read] ROUTER_GATE 锚点不唯一")
    text = text.replace(anchor, NEW_ALSO_READ.lstrip("\n") + "\n" + anchor, 1)
    print("OK   [struct] also_read 13 条链")

    text = insert_before_block_close(
        text, '"additional_sources": [', NEW_SOURCE, "additional-sources")
    print("OK   [struct] additional_sources +1（src-21-cfr-part-120-2025）")

    payload = "".join(f'            "{p}",\n' for p in NEW_PRINCIPLES)
    text = insert_before_block_close(
        text, '"core_principles": [', payload, "core-principles")
    print(f"OK   [struct] core_principles +{len(NEW_PRINCIPLES)}")

    payload = "".join(f'            "{p}",\n' for p in NEW_STOPS)
    text = insert_before_block_close(
        text, '"stop_conditions": [', payload, "stop-conditions")
    print(f"OK   [struct] stop_conditions +{len(NEW_STOPS)}")

    if not apply:
        print(f"\n[dry-run] 变更后长度 {len(text)}（原 {len(original)}），未写盘。加 --apply 落地。")
        return 0

    TARGET.write_text(text, encoding="utf-8")
    print(f"\n已写盘：{TARGET}（{len(text)} 字节）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
