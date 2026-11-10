"""apply_v4_15_revisions.py — 把 CAP-27（CP 7303.847 果汁检查程序）接入 Bundle

改动面（第十九来源）：
1. SLUGS 追加 juice-inspection-program（→ CAP-27）
2. ALSO_READ 双向链：与 CAP-26（法条层）配对，并连到通用迎检链
3. additional_sources 追加第十九来源 src-fda-cp-7303-847-2010
4. core_principles +2、stop_conditions +2
5. 「十八类 → 十九类」「26 张 → 27 张」等当前口径同步
6. **订正 v4.13 的错误 CP 号**：果汁检查程序是 CP **7303.847**，此前误写为 `7303.047`；
   同时清除「〔§ 117.5(c)〕逐字文本未收」（v4.14 已收）的残留断言。

纪律：rep_once（命中数必须为 1）；结构追加走结构定位 + 断言；dry-run 全过才 --apply。
"""
from __future__ import annotations

import sys
from pathlib import Path

TARGET = Path(".cangjie/assemble_bundle.py")

REPLACEMENTS: list[tuple[str, str, str]] = [
    ("docstring-26->27",
     '"""assemble_bundle.py — 从 26 张 _meta-*.yaml',
     '"""assemble_bundle.py — 从 27 张 _meta-*.yaml'),
    ("slugs-append",
     '         "juice-haccp"]',
     '         "juice-haccp",\n         "juice-inspection-program"]'),
    # 描述层
    ("desc-count",
     "以及十八类来源不可混引与三层配对（法条 CAP-22 / 指南 CAP-23 / 检查程序 CAP-24）。",
     "以及十九类来源不可混引与三层配对（法条 CAP-22 / 指南 CAP-23 / 检查程序 CAP-24）。"
     '"\n'
     '            "另覆盖果汁 HACCP 的检查程序判定链（FDA CP 7303.847，2010-11-02 版 / 2025-09-18 更正，检查程序作业层）：'
     "先分主体——**加工者检查 = HACCP 系统检查 + 非 HACCP（GMP/污秽/标签/经济欺诈）覆盖**，"
     "**进口商检查 = 纯记录审查且不取样**（`No samples are to be collected`，核 21 CFR 120.14 的规格与 affirmative steps，"
     "报 `03847H` 且 Establishment Type 用 A）；再分样品——验证样品**只在预期 NAI/VAI 时取**且须分析计划中全部相关危害、"
     "走 `847H` 系列；有因样品**非常规**、PAC 限 `03847`/`04847`/`07847`/`09847`；文档性样品**只报 `03847`** 且不计工作计划；"
     "采样量按 ATTACHMENT A 逐项对表（微生物 10×≥32 fl oz、铅 12×≥4 oz、巴氏毒素冷冻浓缩 6×≥400 ml / 单倍浓度 6×≥500 ml、"
     "污秽与硬锐物逐子样单独分析 no compositing）。**四类纠偏**：① 没取样 ≠ 没问题（三条独立理由）；② PAC 混用是硬错；"
     "③ 铅 10/20 ppb 是 2022-04 草案**拟议行动水平**，非法规限值；④ 本件不创设企业义务，企业义务回 CAP-26。"
     "升级路径：高风险/CCP 缺陷 → CMS + RPM Ch.4；巴氏企业不回应 → 最后通信日后 **60 天**复检；病原阳性 → 州际判定 → HFP/Recalls"
     '"'),
    ("principle-count",
     "合计**十八类不可混引**（v4.8 新增第十三来源、v4.9 新增第十四来源 21 CFR Part 123、v4.10 新增第十五来源 FDA 海产品危害与控制指南、v4.11 新增第十六来源 CP 7303.842、v4.12 新增第十七来源 21 CFR Part 108、v4.13 新增第十八来源 21 CFR Part 120）",
     "合计**十九类不可混引**（v4.8 新增第十三来源、v4.9 新增第十四来源 21 CFR Part 123、v4.10 新增第十五来源 FDA 海产品危害与控制指南、v4.11 新增第十六来源 CP 7303.842、v4.12 新增第十七来源 21 CFR Part 108、v4.13 新增第十八来源 21 CFR Part 120、v4.15 新增第十九来源 CP 7303.847）"),
    ("principle-count-b",
     "**十八类不可混引**，且 §114.5 并列 `parts 110 and 117` 不得改写或判为笔误",
     "**十九类不可混引**，且 §114.5 并列 `parts 110 and 117` 不得改写或判为笔误"),
    ("stop-routing",
     "用户任务超出 26 张能力卡路由范围时，明确告知超出本包覆盖，不要硬套；LACF/AF 的实体工艺法条义务先转 CAP-20，注册备案与紧急许可程序转 CAP-25，果汁 HACCP 转 CAP-26，检查员侧取证转 CAP-19",
     "用户任务超出 27 张能力卡路由范围时，明确告知超出本包覆盖，不要硬套；LACF/AF 的实体工艺法条义务先转 CAP-20，注册备案与紧急许可程序转 CAP-25，果汁 HACCP 的法条义务转 CAP-26、检查程序转 CAP-27，检查员侧取证转 CAP-19"),
    ("stop-count",
     "全包自 v4.13 起**十八类不可混引**，当前为 26 张能力卡",
     "全包自 v4.15 起**十九类不可混引**，当前为 27 张能力卡"),
    # 订正错误 CP 号 + 清除 v4.14 已收项的残留断言
    ("fix-cp-number-scope",
     "果汁 HACCP 的检查员取证口径（CP 7303.047 未收，法条义务见 CAP-26）与 NSSP Guide",
     "果汁检查程序的 CPG 全文（510.150 / 555.425）与 NSSP Guide（法条义务见 CAP-26，检查程序自 v4.15 起见 CAP-27）"),
    ("fix-uncited-residue",
     "〔§ 117.5(c)〕逐字文本、part 110 正文、CP 7303.047 果汁 program、CPG 与 Import Alert 全文、BAM/AOAC 方法全文一律标「转引未收」",
     "part 110 正文、CPG 与 Import Alert 全文、BAM/AOAC 方法全文一律标「转引未收」（〔§ 117.5(c)〕原文自 v4.14 起已在包内、CP 7303.847 自 v4.15 起已收——**v4.13 曾把果汁检查程序误写为 CP 7303.047，正确号是 7303.847**）"),
]

NEW_ALSO_READ = '''
# v4.15：CAP-27 果汁 HACCP 检查程序（FDA CP 7303.847）。与 CAP-26（Part 120 法条层）
# 强配对；另连到通用迎检链（CAP-16/17/18）、cGMP、LACF 双卡、海产品检查卡与召回。
ALSO_READ["juice-inspection-program"] = [
    "juice-haccp", "inspection-readiness", "inspection-sampling",
    "investigator-authority-procedure", "cgmp-compliance-guide",
    "lacf-inspection-program", "lacf-statutory-requirements",
    "seafood-inspection-program", "recall-plan", "defect-action-levels",
    "regulatory-boundaries",
]
for _s in ("juice-haccp", "inspection-readiness", "inspection-sampling",
           "investigator-authority-procedure", "cgmp-compliance-guide",
           "lacf-inspection-program", "seafood-inspection-program",
           "recall-plan", "defect-action-levels", "regulatory-boundaries",
           "hazard-analysis-method", "chemical-hazard-controls"):
    if "juice-inspection-program" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("juice-inspection-program")

'''

NEW_SOURCE = '''            {
                "title": "Compliance Program Guidance Manual 7303.847 — Juice HACCP Inspection Program (Processor and Importer Inspections)",
                "author": "U.S. FDA, Human Foods Program (HFP) / Office of Inspections and Investigations (OII)",
                "year": "2010-11-02（Date of Issuance 与 IMPLEMENTATION DATE 均为 11/02/2010；Correction date 09/18/2025）",
                "content_type": "inspection-program（FDA 给检查员/分区的内部作业指导；非法规、非 Guidance for Industry、不创设企业义务）",
                "source_id": "src-fda-cp-7303-847-2010",
                "source_file": "source-cp-7303-847-2025.md",
                "note": "由用户提供的官方 508-Compliant PDF（26 页 / 35 书签）经**本包专用脚本** .cangjie/convert_cp847.py 转换：按「固定 3 行页眉 + `— Page N` 页标记 + 全加粗标题 + 字号 ≥11」重建、行距 >1.55×行高断段；**未用 pdf2md-pro**——其书签注入会把 7 个标题插进段落中间并把大纲块前置乱序（H2 虚高到 60）。自检：7 个 PART、66 个小节、605 行 / 50,345 字符、页眉与页码残留 0、目录块已裁。⚠ 文件名 20250922 只是 PDF 生成日（creationDate 2025-09-22），**不是 2025 新版 program**：本件是 2010-11-02 版程序的 2025-09-18 更正本，与 CP 7303.050/7303.070/7303.842/7303.878 同属「旧程序 + 近期更正」形态，不得套 CPGM 7303.040 的 2025-CPM-HFP-001 Transmittal 写法。**四类纠偏**：① 进口商检查不取样、验证样品只在预期 NAI/VAI 时取、多数法规缺陷不需实物样品——「没取样」不能反推「没问题」；② PAC 分流是硬错高发区（`847H` 只服务实物验证样品、文档性样品只报 `03847` 且不计工作计划、进口商报 `03847H` + Establishment Type A）；③ 铅 10/20 ppb 是 2022-04 草案**拟议行动水平**（proposed），非法规限值；④ CPGM 不创设企业义务，企业义务回 CAP-26〔§ 120.xxx〕。⚠ 两处标题在文本层无字（PART II `1. Objective`、PART VI `1. References`/`2. Attachments`），已用书签补回、不可当逐字原文引；封面 PAF 表因双栏排版被合成一行、字母交错，引用须按字母逐项还原。逐字引用核对 28/28 命中（verify_v4_15_quotes.py）。仍未收：CPG 510.150 / 555.425 全文、CP 7307.001 / 7304.019 / 7309.006 / 7321.005 全文、BAM / AOAC 方法全文、Import Alert 全文、FACTS / eNSpect / CMS 内部操作",
            },
'''

NEW_PRINCIPLES = [
    "果汁 HACCP 必须把「法条层」与「检查程序层」分开答：企业义务在 21 CFR Part 120〔§ 120.xxx〕（CAP-26），检查员取证在 FDA CP 7303.847（CAP-27）——后者是 CPGM 内部作业指导，**不创设企业义务**。三件事不可混：企业要做什么（CAP-26）／FDA 来查什么（CAP-27）／抽样量与表单怎么走（CAP-17/18 通用部分）。与 LACF 的 CAP-20/CAP-19、海产品的 CAP-22/23/24 同构",
    "「没取样」不能反推「没问题」，三条独立理由：进口商检查**根本不取样**（CP 7303.847 PART II.2.A.2 `No samples are to be collected`）；验证样品**只在检查员预期结果为 NAI 或 VAI 时取**；且原文注明 `Most deficiencies of the Juice HACCP regulation do not require a physical sample to confirm or document them`。PAC 分流同样是硬错高发区：`847H` 系列只服务实物验证样品，文档性样品只报 `03847` 且不计入工作计划，进口商报 `03847H` 且 Establishment Type 必须用 A。⚠ 果汁检查程序号是 CP **7303.847**（v4.13 曾误写为 7303.047）",
]

NEW_STOPS = [
    "回答果汁检查问题不得把 CP 7303.847 的检查动作写成企业义务（CPGM 不创设义务）；不得把「没取样」读成「合规」或「被放过」（进口商检查不取样、验证样品仅限预期 NAI/VAI、多数缺陷不需实物样品）；不得把文档性样品报在 `847H` 系列或计入工作计划、不得把进口商的 Establishment Type 写成非 A；不得把铅的 10/20 ppb「拟议行动水平」写成法规限值或安全港（2022-04 草案，超值由 HFP 逐案审查）；不得把 LACF 的 4.40/4.65、24 罐/12 罐触发线套到果汁（那是 CP 7303.070）；不得把本件写成「2025 版 program」（2010-11-02 版 / 2025-09-18 更正，文件名 20250922 只是 PDF 生成日）；不得把 CP 号写成 7303.047",
    "果汁检查的引用写「CP 7303.847 PART x / ATTACHMENT A」，企业义务写〔§ 120.xxx〕，其他程序写其 CP 号（7303.040 / 7303.070 / 7303.878 / 7307.001 / 7304.019 / 7309.006 / 7321.005），三者不得混引；CAP-27 的两处标题（PART II `1. Objective`、PART VI `1. References`/`2. Attachments`）在文本层无字、系书签补回，**不可当逐字原文引**；封面 PAF 表因双栏排版被合成一行、字母顺序交错，引用须按「字母→类别→PAF」逐项还原，不得按行序引用",
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

    anchor = "ROUTER_GATE = {"
    if text.count(anchor) != 1:
        raise SystemExit("FAIL [also-read] ROUTER_GATE 锚点不唯一")
    text = text.replace(anchor, NEW_ALSO_READ.lstrip("\n") + "\n" + anchor, 1)
    print("OK   [struct] also_read 12 条链")

    text = insert_before_block_close(text, '"additional_sources": [', NEW_SOURCE, "additional-sources")
    print("OK   [struct] additional_sources +1（src-fda-cp-7303-847-2010）")

    payload = "".join(f'            "{p}",\n' for p in NEW_PRINCIPLES)
    text = insert_before_block_close(text, '"core_principles": [', payload, "core-principles")
    print(f"OK   [struct] core_principles +{len(NEW_PRINCIPLES)}")

    payload = "".join(f'            "{p}",\n' for p in NEW_STOPS)
    text = insert_before_block_close(text, '"stop_conditions": [', payload, "stop-conditions")
    print(f"OK   [struct] stop_conditions +{len(NEW_STOPS)}")

    if not apply:
        print(f"\n[dry-run] 变更后长度 {len(text)}（原 {len(original)}），未写盘。加 --apply 落地。")
        return 0
    TARGET.write_text(text, encoding="utf-8")
    print(f"\n已写盘：{TARGET}（{len(text)} 字节）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
