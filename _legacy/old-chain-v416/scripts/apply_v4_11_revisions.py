#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""apply_v4_11_revisions.py — v4.11 结构性接入 + 当前口径回补。

纪律（沿用 v4.10 apply_*_revisions.py）：
- rep_once() 唯一性断言；内存暂存；备份；末尾一次性落盘；审计 JSON。
- **不做「十五类 → 十六类」全局替换**：「第十五类」含「十五类」子串，且历史编译记录里的
  「十五类 / 23 张 / CP 7303.842 未收」是当时口径，须原样保留（v4.10 产物亦保留 24 处旧口径）。
- 只改确定性当前口径短语 + 明确点名的当前版本行 + 结构性接入。
"""
import json
import shutil
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
BACKUP = BASE / ".cangjie/backup-v4-11-pre-revisions"
AUDIT = BASE / ".cangjie/v4-11-sources-qa-report.json"

AB = ".cangjie/assemble_bundle.py"

pending = {}   # rel -> (text_lf, nl)
audit = []


def read(rel):
    if rel in pending:
        return pending[rel][0]
    raw = (BASE / rel).read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    return raw.replace("\r\n", "\n")


def nl_of(rel):
    raw = (BASE / rel).read_bytes().decode("utf-8")
    return "\r\n" if "\r\n" in raw else "\n"


def stage(rel, text):
    pending[rel] = (text, nl_of(rel))


def rep_once(rel, old, new, label):
    t = read(rel)
    n = t.count(old)
    assert n == 1, f"[{label}] 期望 1 处命中，实得 {n} 处：{old[:90]!r}"
    stage(rel, t.replace(old, new, 1))
    audit.append({"label": label, "file": rel, "kind": "rep_once"})


# ---------------------------------------------------------------- 1) 结构接入
rep_once(AB,
         '"""assemble_bundle.py — 从 23 张 _meta-*.yaml 汇总构造 Capability Bundle',
         '"""assemble_bundle.py — 从 24 张 _meta-*.yaml 汇总构造 Capability Bundle',
         "docstring 23 → 24")

rep_once(AB,
         '         "seafood-hazards-controls-guide"]',
         '         "seafood-hazards-controls-guide",\n         "seafood-inspection-program"]',
         "SLUGS 追加 CAP-24")

rep_once(AB,
         'ROUTER_GATE = {"independent_intent": False,',
         '''# v4.11：CAP-24 海产品检查程序层。与 CAP-22（法条层）、CAP-23（指南层）三层配对，
# 另须双向连到通用取样、FSVP、LACF、迎检、检查员权限、化学危害与缺陷行动水平。
ALSO_READ["seafood-inspection-program"] = [
    "seafood-haccp-statutory-requirements", "seafood-hazards-controls-guide",
    "inspection-sampling", "fsvp-inspection-program", "lacf-inspection-program",
    "inspection-readiness", "investigator-authority-procedure",
    "chemical-hazard-controls", "defect-action-levels",
]
for _s in ("seafood-haccp-statutory-requirements", "seafood-hazards-controls-guide",
           "inspection-sampling", "fsvp-inspection-program", "lacf-inspection-program",
           "inspection-readiness", "investigator-authority-procedure",
           "chemical-hazard-controls", "defect-action-levels"):
    if "seafood-inspection-program" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("seafood-inspection-program")

ROUTER_GATE = {"independent_intent": False,''',
         "CAP-24 ALSO_READ 双向链")

NEW_SOURCE = '''            {
                "title": "Compliance Program Guidance Manual 7303.842 - Seafood Processor, Products, and Importer Inspection Program",
                "author": "U.S. FDA, Human Foods Program (HFP) / Office of Inspections and Investigations (OII)",
                "year": "IMPLEMENTATION DATE 11/01/2023；Correction date 09/30/2025；80 物理页 / 148 书签（首页标 Page 1 of 86）",
                "content_type": "inspection-program（FDA 给检查员、进口分区、分部合规官与实验室的内部作业指导；非法规、非 Guidance for Industry、不创设企业义务）",
                "source_id": "src-fda-cp-7303-842-2023",
                "source_file": "books/fda-pchf-human-food-guidance/source-cp-7303-842-2023.md",
                "note": "由用户提供的官方 508-Compliant PDF 经用户级技能 pdf2md-pro（pymupdf4llm 2.1）转换，正文 179,812 字节 / 1,334 行；148 书签全命中、203 表格行、残留页码 0。⚠ 文件名 20250929 只是 PDF 生成日（creationDate 2025-09-29），本件是 2023-11-01 版程序的 2025-09-30 更正本，不是 2025 新签发 program；封面 Date of Issuance 09/30/025 为文本层残缺，正文页脚 11/1/2023。首页 NOTE 与 PART I 写明 CP 7303.842 与 CP 7303.844 已合并为单一程序，但 PAC 仍分进口 03844x / 国产 03842x。PART II Table 1 产品/工艺风险与 Table 2 企业/进口商 work planning（90/10、100 entry line items）不可对调；PART III 六类检查分流与 Sampling 三类（国产 for cause only、进口监督、documentary 只报 03842）；PART IV A–G 的 500/50/35 ppm、15/25 µg/100g、48 subs 等全是检查员触发值而非法规限值，判据出口为 CPG 540.525 / 540.370 / 562.300 等（未收）；PART V Table 4 是 ranking 且 case-by-case，WL / DWPE / judicial actions 须 HFP OCE concurrence；FIELD REPORTING 用 FACTS / CMS / FDA 3501·3502；ATTACHMENT A 样品量仅 surveillance and audit。引用用「CP 7303.842 PART x / Table x / ATTACHMENT A #x / Lxxx」，逐字引证以原文字符串为准。⚠ 转换件存在书签标题与正文伪标题交错（PART 各出现两次、H1 虚高 133），检索以 PART / 小节 / 表号为准，表格与页眉不可逐字引用。仍未收：CPG 全文、21 CFR part 120 / 1240 / 108 / 110 / 507、NSSP Guide、BAM / AOAC / MPM 方法全文、Import Alert 16-xx 全文、21 CFR part 1 subpart L、IOM Ch.4、FDA 3501/3502 表单全文与 eNSpect / CMS / FACTS 内部系统 —— 一律标转引未收",
            },
'''
rep_once(AB,
         '            },\n        ],\n    },\n    "entry": {',
         '            },\n' + NEW_SOURCE + '        ],\n    },\n    "entry": {',
         "additional_sources 追加第十六来源")

rep_once(AB,
         '            "适用于食品工厂质量/合规人员、采购与供应商管理者',
         '''            "另覆盖海产品检查程序的完整判定链（FDA CP 7303.842，2023 版 / 2025-09-30 更正，检查程序作业层）：CP 7303.842 与 7303.844 已合并但 PAC 仍分进口/国产、Table 1 产品/工艺风险与 Table 2 企业/进口商 work planning 的分工及 90/10 规则、六类检查分流（Processor / Importer / Vessels / Foreign Establishment / NSSP / EMA）与 HACCP Program Evaluations、Sampling 三类与国产 for cause only、PAC 双码表与 03842H 同名不同义、PART IV A–G 实验室分流与『触发值不是法规限值』、Table 4 违规分级与 case-by-case、WL / DWPE / judicial actions 的 HFP OCE concurrence、Species misbranding 的 FD&C Act 403(b) 定性、FIELD REPORTING 的 FACTS / CMS / FDA 3501·3502 出口、ATTACHMENT A 样品量适用域，以及十六类来源不可混引与三层配对（法条 CAP-22 / 指南 CAP-23 / 检查程序 CAP-24）。"
            "适用于食品工厂质量/合规人员、采购与供应商管理者''',
         "entry.description 追加 CAP-24 段")

NEW_PRINCIPLES = '''            "第十六来源 CP 7303.842 是**给 field staff 的内部作业指导层**：不创设企业义务、不是法规也不是 Guidance for Industry。全包效力栈为法规正文〔§ 117/113/114/123.xxx〕＞ FDA 指南（should 建议层）＞ CPGM / CP / IOM 检查程序（检查员视角）。既不把 CP 的检查动作、Table 1/2 优先级、PART IV 触发值写成企业义务或放行标准，也不因 CP 非强制把 Part 123 的 `shall` 义务稀释成可选",
            "检查判定链按『Table 1 选产品/工艺风险 → Table 2 做 work planning → 六类检查分流 → HACCP Program Evaluations → Sampling 三类与 PAC 上报 → PART IV A–G 与 CPG 判据出口 → PART V Table 4 ranking（case-by-case）→ FIELD REPORTING 收口』推进；Table 4 的 Major/Minor 不是〔§ 123.6〕的 significant hazard 判定，WL / DWPE / judicial actions 也不是达到某值自动触发",
            "CP 7303.842 的两处硬口径：**合并的是程序不是码表**（7303.844 已并入，但取样/分析 PAC 仍分 03844x / 03842x，且 03842H 在取样表与报告表同名不同义，documentary samples 只报 03842）；**ATTACHMENT A 样品量只适用于 surveillance and audit**，不得用于 reconditioning、DWPE 放行或 Domestic HACCP Verification",
'''
rep_once(AB,
         '        ],\n        "out_of_scope": [',
         NEW_PRINCIPLES + '        ],\n        "out_of_scope": [',
         "core_principles +3")

rep_once(AB,
         '            "果汁 HACCP（21 CFR part 120）的专项要求正文、海产品检查程序 CP 7303.842 正文与 NSSP Guide（海产品企业义务已由 CAP-22 覆盖〔§ 123.xxx〕正文，但检查员侧取证口径与贝类州际销售许可仍属未收）",',
         '            "果汁 HACCP（21 CFR part 120）的专项要求正文与 NSSP Guide（海产品企业义务已由 CAP-22 覆盖〔§ 123.xxx〕正文、检查员侧程序自 v4.11 起由 CAP-24 覆盖 CP 7303.842；但 CPG / BAM / Import Alert 全文与贝类州际销售许可仍属未收）",',
         "out_of_scope 第 2 条移除 CP 7303.842 未收")

NEW_STOPS = '''            "回答 CP 7303.842 相关问题时不得把 Table 1/2 优先级、PART IV 的 500/50/35 ppm 与 15/25 µg/100g、48 subs、pH 4.6、98% RSSL 等检查员触发值写成法规限值、产品放行标准或 BAM 方法全文；Table 4 的 Major/Minor 只作 case-by-case ranking，不是〔§ 123.6〕的 significant hazard 判定；WL / DWPE / judicial actions 须 HFP OCE concurrence 而非自动触发。CPG 540.525 / 540.370 / 562.300 / 555.600、21 CFR part 120 / 1240 / 108 / 110 / 507、NSSP Guide、BAM / AOAC / MPM、Import Alert 16-xx 与 99-41 全文、21 CFR part 1 subpart L、IOM Ch.4、FDA 3501/3502 表单全文一律标「转引未收」；引用写「CP 7303.842 PART x / Table x / ATTACHMENT A #x / Lxxx」，不得与〔§ 123.xxx〕或 Seafood Hazards Guide Ch.x 混引",
            "CP 7303.842 的版本口径锁定 2023-11-01 版 / 2025-09-30 更正，文件名 20250929 只是 PDF 生成日，封面 Date of Issuance 09/30/025 为文本层残缺，正文页脚 11/1/2023；与 CP 7303.050 / 7303.070 / 7303.878 同属旧程序更正本，不得套 CPGM 7303.040 的 2025-CPM-HFP-001 Transmittal 形态。转换件书签标题与正文伪标题交错（PART 各出现两次、H1 虚高 133），检索以 PART / 小节 / 表号为准，表格、页码、页眉不可逐字引用；凡法条义务转 CAP-22、危害技术判定转 CAP-23、FSVP 转 CAP-21、通用取样转 CAP-17",
'''
rep_once(AB,
         '        ],\n    },\n    "router_entry": {',
         NEW_STOPS + '        ],\n    },\n    "router_entry": {',
         "stop_conditions +2")

# ------------------------------------------------- 2) assemble_bundle 当前口径
AB_RULES = [
    ("合计**十五类不可混引**（v4.8 新增第十三来源、v4.9 新增第十四来源 21 CFR Part 123、v4.10 新增第十五来源 FDA 海产品危害与控制指南）",
     "合计**十六类不可混引**（v4.8 新增第十三来源、v4.9 新增第十四来源 21 CFR Part 123、v4.10 新增第十五来源 FDA 海产品危害与控制指南、v4.11 新增第十六来源 CP 7303.842）"),
    ("；**十五类不可混引**，且 §114.5", "；**十六类不可混引**，且 §114.5"),
    ("用户任务超出 23 张能力卡路由范围时", "用户任务超出 24 张能力卡路由范围时"),
    ("仍未收：CP 7303.842 海产品检查程序、21 CFR part 120",
     "仍未收：21 CFR part 120"),
    ("仍未收：CP 7303.842、NSSP Guide、21 CFR part 120",
     "仍未收：NSSP Guide、21 CFR part 120"),
    ("其他 Compliance Programs（7303.080 / 7303.842 / 7371.000",
     "其他 Compliance Programs（7303.080 / 7371.000"),
    ("另 CP 7303.842 海产品检查程序、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、NSSP Guide 仍未收",
     "另 21 CFR part 120 / 1240 / 108 / 110 / 507 正文与 NSSP Guide 仍未收；CP 7303.842 自 v4.11 起已收（见 CAP-24）"),
    ("CP 7303.842、NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507、Import Alert 16-xx、BAM 海产品章节、CPG Sec. 540.525 / 555.300 / 575.100 与 Appendix 5 回指的外部法源一律标「转引未收」；全包自 v4.10 起**十五类不可混引**，当前为 23 张能力卡",
     "NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507、Import Alert 16-xx、BAM 海产品章节、CPG Sec. 540.525 / 555.300 / 575.100 与 Appendix 5 回指的外部法源一律标「转引未收」；CP 7303.842 自 v4.11 起已收（见 CAP-24）；全包自 v4.11 起**十六类不可混引**，当前为 24 张能力卡"),
]
for old, new in AB_RULES:
    rep_once(AB, old, new, f"AB 口径: {old[:42]}")

# --------------------------------------------- 3) 卡片 / meta / glossary 当前口径短语
# 只做确定性短语替换；历史陈述里的「十五类 / 23 张 / CP 7303.842 未收」按 v4.10 口径保留。
PHRASE_RULES = [
    ("十五类来源不可混引", "十六类来源不可混引"),
    ("十五类不可混引", "十六类不可混引"),
    ("十五类来源", "十六类来源"),
    ("23 张能力卡", "24 张能力卡"),
    ("23 张卡", "24 张卡"),
]
# 含 v4.10 版本注记、notes 演进说明、术语自检记录的行是历史陈述，整行跳过。
# v4.10 先例：改术语 tags/title 与 expected_behavior，保留 notes 与自检行。
HARD_SKIP = ("v4.10", '"notes":', "全库 **182 条**")

# 3a) 先精确改写带旧版本归属的「当前陈述」；改写后行内旧口径已消失或由 HARD_SKIP 保护。
VERSIONED = [
    (".cangjie/capabilities/cards/cgmp-compliance-guide.md",
     "v4.10 起全包统一「十五类不可混引」（v4.8 时为十三类）",
     "v4.11 起全包统一「十六类不可混引」（v4.10 时为十五类，v4.8 时为十三类）"),
    (".cangjie/capabilities/cards/inspection-sampling.md",
     "全包自 v4.7 起**十五类不可混引**",
     "全包自 v4.11 起**十六类不可混引**（v4.7 时为十二类）"),
    (".cangjie/capabilities/cards/investigator-authority-procedure.md",
     "全包自 v4.7 起**十五类不可混引**",
     "全包自 v4.11 起**十六类不可混引**（v4.7 时为十二类）"),
    (".cangjie/capabilities/cards/seafood-hazards-controls-guide.md",
     "*全包自 v4.10 起「**十五类来源不可混引**」。",
     "*全包自 v4.11 起「**十六类来源不可混引**」（v4.10 时为十五类）。"),
    (".cangjie/capabilities/cards/seafood-hazards-controls-guide.md",
     "**B11 — 导出件转换质量红线与十五类不可混引引用规范。**",
     "**B11 — 导出件转换质量红线与十六类不可混引引用规范。**"),
    (".cangjie/capabilities/cards/seafood-hazards-controls-guide.md",
     "全包自 v4.10 起**十五类来源不可混引**：",
     "全包自 v4.11 起**十六类来源不可混引**（v4.10 时为十五类）："),
    (".cangjie/capabilities/cards/_meta-seafood-haccp-statutory-requirements.yaml",
     "第 4 版自 v4.10 起已收（第十五来源，见 CAP-23），全包十五类不可混引",
     "第 4 版自 v4.10 起已收（第十五来源，见 CAP-23）；CP 7303.842 自 v4.11 起已收（第十六来源，见 CAP-24）；全包自 v4.11 起十六类不可混引（v4.10 时为十五类）"),
]
for rel, old, new in VERSIONED:
    rep_once(rel, old, new, f"版本归属: {old[:30]}")

# PIPELINE_STATE / BOOK_OVERVIEW / DIGEST 是历史演进文档，不改其历史行里的「十五类 / 23 张」，
# 只在下方精确替换「当前为 / 当前版本」行并追加 v4.11 段。
phrase_files = sorted((BASE / ".cangjie/capabilities/cards").glob("*.md")) + \
               sorted((BASE / ".cangjie/capabilities/cards").glob("_meta-*.yaml")) + \
               [BASE / "candidates/glossary.md", BASE / "test-prompts.json"]
phrase_files = [p for p in phrase_files if p.name not in ("seafood-inspection-program.md", "_meta-seafood-inspection-program.yaml")]

for p in phrase_files:
    rel = p.relative_to(BASE).as_posix()
    lines = read(rel).split("\n")
    changed = 0
    for i, line in enumerate(lines):
        if any(k in line for k in HARD_SKIP):
            continue
        new = line
        for old, rep in PHRASE_RULES:
            new = new.replace(old, rep)
        if new != line:
            lines[i] = new
            changed += 1
    if changed:
        stage(rel, "\n".join(lines))
        audit.append({"label": "当前口径短语", "file": rel,
                      "lines": changed, "kind": "phrase"})

# 3b) test-prompts.json notes 追加 v4.11 演进句（v4.10 先例），不改历史句子本身。
rep_once("test-prompts.json",
         '全包十五类不可混引，全库 182 条术语 / 115 条用例。本版未重跑触发/输出/路由评测。"',
         '全包十五类不可混引，全库 182 条术语 / 115 条用例。本版未重跑触发/输出/路由评测。 | v4.11 追加 10 条 seafood-inspection-* 用例（CP 7303.842 版本判定与 7303.844 合并、Table 1/2 分工与 90/10、六类检查分流、PAC 双码表与 03842H 同名不同义、Sampling 三类与国产 for cause only、PART IV 触发值性质与 CPG 判据出口、Table 4 ranking 与 §123.6 显著性分离、WL/DWPE 的 HFP OCE concurrence、ATTACHMENT A 适用域、十六类不可混引与版本陷阱）；新增第 24 张卡 seafood-inspection-program，第十六来源为 FDA CP 7303.842（2023-11-01 版 / 2025-09-30 更正，检查程序作业层），与 CAP-22 法条层 / CAP-23 指南层三层配对，全包十六类不可混引，全库 192 条术语 / 125 条用例。"',
         "notes 追加 v4.11 演进句")

# --------------------------------------------- 4) 明确点名的「仍未收 CP 7303.842」当前句
EXACT = [
    ("PIPELINE_STATE.md",
     "- **当前版本**: v4.10 ✅ 编译校验并安装完成（23 张卡 / 182 术语 / 115 用例 / 十五类来源 / dist-v14）",
     "- **当前版本**: v4.11 🔄 编译校验与安装进行中（24 张卡 / 192 术语 / 125 用例 / 十六类来源 / dist-v15）"),
    (".cangjie/capabilities/cards/seafood-haccp-statutory-requirements.md",
     "与 CP 7303.842（海产品检查程序，**正文本包未收**）、",
     "与 CAP-24 的 CP 7303.842（第十六来源，检查程序作业层）、"),
    (".cangjie/capabilities/cards/seafood-haccp-statutory-requirements.md",
     "**NSSP Guide**、**CP 7303.842**。一律标「转引未收」",
     "**NSSP Guide**。一律标「转引未收」；CP 7303.842 自 v4.11 起已收（CAP-24），但仍是检查程序层、不得反推法条"),
    (".cangjie/capabilities/cards/seafood-hazards-controls-guide.md",
     "*正文本包**仍未收**：CP 7303.842（海产品检查程序）、NSSP Guide（软体贝类）",
     "*正文本包**仍未收**：NSSP Guide（软体贝类）；CP 7303.842 自 v4.11 起已收（CAP-24）"),
    (".cangjie/capabilities/cards/seafood-hazards-controls-guide.md",
     "CP 7303.842 **正文本包未收**。",
     "CP 7303.842 自 v4.11 起已收（见 CAP-24 `seafood-inspection-program`）。"),
    (".cangjie/capabilities/cards/_meta-seafood-hazards-controls-guide.yaml",
     "法条义务层配对而非合并。仍未收清单：CP 7303.842 海产品检查程序、NSSP Guide、",
     "法条义务层配对而非合并；CP 7303.842 检查程序自 v4.11 起已收（CAP-24）。仍未收清单：NSSP Guide、"),
    (".cangjie/capabilities/cards/_meta-seafood-haccp-statutory-requirements.yaml",
     "  - 判断哪些问题超出本包（CP 7303.842、part 120/1240/108/110/507、NSSP、BAM、Import Alert 全文）",
     "  - 判断哪些问题超出本包（part 120/1240/108/110/507、NSSP、BAM、Import Alert 全文；CP 7303.842 自 v4.11 起已收，转 CAP-24）"),
]
for rel, old, new in EXACT:
    rep_once(rel, old, new, f"精确: {rel.split('/')[-1]} / {old[:38]}")

# --------------------------------------------- 5) 当前版本说明行（快照注记里的「当前为」）
for rel in ("PIPELINE_STATE.md", "DIGEST.md", "BOOK_OVERVIEW.md"):
    t = read(rel)
    old = "当前为 **v4.10：23 张卡 / 182 术语 / 115 用例 / 十五类来源 / dist-v14**"
    old2 = "当前为 **v4.10：23 张能力卡 / 182 条术语 / 115 条测试用例 / 十五类来源**"
    n = t.count(old) + t.count(old2)
    if n:
        t2 = t.replace(old, "当前为 **v4.11：24 张卡 / 192 术语 / 125 用例 / 十六类来源 / dist-v15**")
        t2 = t2.replace(old2, "当前为 **v4.11：24 张能力卡 / 192 条术语 / 125 条测试用例 / 十六类来源**")
        stage(rel, t2)
        audit.append({"label": "当前版本说明行", "file": rel, "hits": n, "kind": "version-line"})

# --------------------------------------------- 6) 追加 v4.11 状态段
STATE_SECTION = '''

## v4.11 — CP 7303.842 落为第十六来源 + 海产品检查判定链（24 张卡）

- **触发与范围**：用户先安装用户级技能 `pdf2md-pro`，随后提供官方 508-Compliant PDF `20250929_CP 7303.842 Seafood Processor, Products, And Importer Inspection Program 508-Compliant.pdf`。该件是 `PIPELINE_STATE.md` v4.10 段「仍未收」清单的**第一项**，且 v4.6 / v4.7 / v4.8 三次明确暂缓未纳入。经选项确认，用户选择「纳入为第十六来源 + 1 张卡」，继续 single 输出、不另起技能包。
- **版本判定（第四次同型纠错）**：封面 `IMPLEMENTATION DATE 11/01/2023`、`Correction date: 09/30/2025`、`Date of Issuance: 09/30/025`（PDF 文本层残缺），正文页脚 `11/1/2023`，PDF creationDate `2025-09-29` → 文件名 `20250929` **只是生成日**，本件是 **2023-11-01 版程序的 2025-09-30 更正本**，与 CP 7303.050 / 7303.070 / 7303.878 同形态，不同于 CPGM 7303.040 的 `2025-CPM-HFP-001`。首页 NOTE 与 PART I 另写明 **CP 7303.842 与 CP 7303.844 已合并为单一程序**，但 PAC 仍分进口 `03844x` / 国产 `03842x`。
- **转换**：为跑技能第 0 步，在 `python3`（3.13.14）安装 `pymupdf4llm 2.1` / `pymupdf 2.1`；`PYTHONUTF8=1` 下转出 179,812 字节 / 1,334 行 / 203 表格行 / 148 书签全命中 / 0 残留页码。正式来源 `source-cp-7303-842-2023.md`（194,080 字节 / 1,373 行）= 文件头（版本、效力层级、与既有来源接口、关键口径、转换局限、十六类引用规范）+ `## 正文（转换原文，未改写）` + 原文。已知局限与 `source-cp-7303-878-2023.md` 同型：书签标题与 `# **…**` 伪标题并存导致 PART 各出现两次、H1 虚高 133，检索以 PART / 小节 / 表号为准；`UnicodeDecodeError` 与 RapidOCR 提示不影响文本层输出。
- **阶段 0–5**：并行产出 `candidates/v4-11-framework.md`（整书理解 / 完整检查判定链 / 阈值清单）、`v4-11-quotes.md`（36 段逐字引用候选）、`v4-11-counter-examples.md`（14 条反例 + 9 张卡 also_read 建议）；阶段 1.6 决定只新增 1 张卡、不晋级独立 Skill。
- **CAP-24 `seafood-inspection-program`**（33,921 字节 / 294 行 / 36 个引用块 + 44 intents / 182 keywords）：主题是**完整检查判定链**——Table 1 产品/工艺风险 + Table 2 work planning → 六类检查分流 → HACCP Program Evaluations → Sampling 三类与 PAC/PAF → PART IV A–G 与 CPG 判据出口 → PART V Table 4 ranking（case-by-case）→ FIELD REPORTING 收口；并给出三层配对（CAP-22 法条层 / CAP-23 指南层 / 本卡检查程序层）、双向误读防护、PAC 双码表与 `03842H` 同名不同义、阈值性质、ATTACHMENT A 适用域、十六类不可混引与转换质量红线。
- **引文核验**：`.cangjie/verify_v4_11_quotes.py` 用 `body_only()` 只取正文分界之后、先 `strip_md()` 剥离 `**`、`<u>`、`<br>`、`#`、行首 `o` / `•` 等转换标记再归一化比对，避免文件头自我验证循环。结果 **36/36 逐字命中正文区**，0 超 100 词、0 表格管道引用 → `RESULT: PASS`。
- **规模变化**：23 → **24 张卡**；182 → **192 条术语**（t183–t192）；115 → **125 条用例**（`seafood-inspection-01..10`）；十五类 → **十六类来源**；core_principles 45 → **48**；stop_conditions 20 → **22**；additional_sources +1；`verified.yaml` / `destinations.json` / `book/` 由 `.cangjie/assemble_bundle.py` 重生成，未手改生成物。
- **两轮口径回补策略**：`apply_v4_11_revisions.py` 用 `rep_once()` 唯一性断言 + 内存暂存 + 备份 + 末尾一次性落盘；**禁止「十五类 → 十六类」全局替换**（「第十五类」含该子串），历史编译记录与评测报告里的「十五类 / 23 张 / CP 7303.842 未收」是当时口径，按 v4.10 先例原样保留，只改确定性当前口径短语与明确点名的当前版本行。
- **评测状态**：本版**未重跑**触发 / 输出 / 路由评测；10 条 `seafood-inspection-*` 用例与 CAP-24 路由正确性待后续补测，v4.7 / v4.10 / 历史补测的既有结论不得冒用。
- **仍未收**：CPG Sec. 540.525 / 540.370 / 555.600 / 562.300 / 540.250 / 540.590 全文、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、NSSP Guide 与 Model Ordinance、BAM / AOAC / LIB / MPM 方法全文、Import Alert 16-74 / 16-20 / 99-41 全文、21 CFR part 1 subpart L、IOM Chapter 4、FDA 3501 / 3502 表单全文、Seafood List、eNSpect / CMS / FACTS / MARCS-CMS 内部系统、FDA–NMFS MOU / FMD#-029。
- **编译与安装**：`compile_single.py --bundle .cangjie/capabilities --out dist-v15 --variant single`；`validate_skill_pack.py dist-v15`；覆盖安装到工作区级 `.workbuddy/skills/fda-pchf-food-safety/`，旧版备份 `backups/fda-pchf-food-safety-v4.10-*`；产物与安装目录逐文件 sha256 差异 0、glossary 5 份副本一致。完整审计见 `.cangjie/v4-11-sources-qa-report.json`。
'''
t = read("PIPELINE_STATE.md")
assert "## v4.11" not in t
stage("PIPELINE_STATE.md", t.rstrip("\n") + STATE_SECTION)

BOOK_SECTION = '''

## v4.11 追加：第十六来源 CP 7303.842（海产品检查程序）

- 上表与各节「仍未收 CP 7303.842」为 **v4.10 及以前**的当时口径，自 v4.11 起该件已纳入为**第十六来源**，见 `source-cp-7303-842-2023.md` 与 CAP-24 `seafood-inspection-program`。当前全包 **十六类来源不可混引**、24 张能力卡 / 192 术语 / 125 用例 / `dist-v15`。
- 该件是 **2023-11-01 版程序的 2025-09-30 更正本**（文件名 `20250929` 只是 PDF 生成日），CP 7303.842 与 CP 7303.844 已合并但 PAC 仍分进口/国产。层次为**检查程序作业层**：法规正文〔§ 123.xxx〕（CAP-22）＞ 技术指南（CAP-23）＞ 本 CP 的 field staff 指令（CAP-24）；CP 不创设企业义务，其 PART IV 触发值也不是法规限值。
- 历史「仍未收」清单中除 CP 7303.842 外的项目（part 120 / 1240 / 108 / 110 / 507、NSSP Guide、CPG 与 Import Alert 全文、BAM 方法、IOM Ch.4 等）**仍然未收**。
'''
t = read("BOOK_OVERVIEW.md")
assert "## v4.11 追加" not in t
stage("BOOK_OVERVIEW.md", t.rstrip("\n") + BOOK_SECTION)

DIGEST_SECTION = '''

> **版本说明（v4.11，2026-11-06 追加）**：技能包纳入第十六来源 FDA **CP 7303.842**（2023-11-01 版 / 2025-09-30 更正，80 物理页 / 148 书签），新增第 24 张卡 `seafood-inspection-program`，承载**完整海产品检查判定链**并作为检查程序作业层与 CAP-22（Part 123 法条层）、CAP-23（危害指南层）三层配对。该 CP 由用户提供的官方 508-Compliant PDF 经用户级技能 `pdf2md-pro` 转换，CAP-24 的 36 个英文引用块经 `.cangjie/verify_v4_11_quotes.py` 逐字核验 36/36 命中。上文 v4.10 及更早的「十五类 / 23 张 / CP 7303.842 未收」均为当时口径；当前为 **v4.11：24 张卡 / 192 术语 / 125 用例 / 十六类来源 / dist-v15**，逐版本演进见 `PIPELINE_STATE.md`。
'''
t = read("DIGEST.md")
assert "版本说明（v4.11" not in t
stage("DIGEST.md", t.rstrip("\n") + DIGEST_SECTION)

# --------------------------------------------- 7) dry-run / 落盘
print(f"touched files: {len(pending)}")
for rel in sorted(pending):
    print("  ", rel)
print("actions:", len(audit))

if "--apply" not in sys.argv:
    print("\nDRY RUN ONLY (pass --apply to write)")
    sys.exit(0)

BACKUP.mkdir(parents=True, exist_ok=True)
for rel in pending:
    src = BASE / rel
    dst = BACKUP / rel.replace("/", "__")
    shutil.copyfile(src, dst)

for rel, (text, nl) in pending.items():
    (BASE / rel).write_bytes(text.replace("\n", nl).encode("utf-8"))

AUDIT.write_text(json.dumps({
    "version": "v4.11",
    "files_touched": sorted(pending),
    "actions": audit,
    "quote_verification": {"quotes": 36, "verbatim_hits": 36, "over_100_words": 0,
                           "table_quotes": 0, "body_only": True, "strip_md": True},
    "policy": "历史陈述中的十五类/23 张/CP 7303.842 未收按 v4.10 先例保留；仅改确定性当前口径",
}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"backup: {BACKUP.relative_to(BASE).as_posix()}")
print("APPLY_V4_11_REVISIONS_OK")
