#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""apply_v4_10_revisions.py — v4.10 口径回补与 Bundle 事实源更新。

沿用 v4.9 的教训（PIPELINE_STATE L239）：**绝不做全局字符串替换**。
「第十四类」含「十四类」子串、历史编译记录里的「22 张」都会污染版本陈述。
本脚本的策略：
  1. assemble_bundle.py：逐条精确替换（每条带唯一性断言）+ 结构性插入；
  2. 其余源码文件：逐行替换「十四类不可混引」→「十五类不可混引」，
     命中历史标记的行整行跳过；
  3. 实质错误「该指南仍未收」按精确字符串修正；
  4. 内存暂存 + 末尾一次性落盘，并输出审计日志。
"""
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
BACKUP = BASE / ".cangjie/backup-v4-10-pre-revisions"
BACKUP.mkdir(parents=True, exist_ok=True)
pending = {}
audit = []


def load(rel):
    p = BASE / rel
    return p.read_text(encoding="utf-8")


def stage(rel, text):
    pending[BASE / rel] = text


def rep_once(rel, old, new, label):
    t = pending.get(BASE / rel) or load(rel)
    n = t.count(old)
    assert n == 1, f"[{label}] 期望 1 处命中，实得 {n} 处：{old[:70]!r}"
    t = t.replace(old, new, 1)
    stage(rel, t)
    audit.append({"file": rel, "action": "exact_replace", "label": label, "old": old[:100], "new": new[:100]})


AB = ".cangjie/assemble_bundle.py"

# ------------------------------------------------------------------ 1. 事实源结构性更新
rep_once(AB,
         'BASE = Path("E:/WeChatData/2026-11-04-09-51-05/books/fda-pchf-human-food-guidance")',
         'BASE = Path(__file__).resolve().parents[1]  # v4.10：改为脚本相对推导，原硬编码原开发机路径在本机不可用',
         "BASE 相对化")

rep_once(AB,
         '"""assemble_bundle.py — 从 22 张 _meta-*.yaml 汇总构造 Capability Bundle（verified.yaml + destinations.json + book/）"""',
         '"""assemble_bundle.py — 从 23 张 _meta-*.yaml 汇总构造 Capability Bundle（verified.yaml + destinations.json + book/）"""',
         "docstring 卡数 22→23")

rep_once(AB,
         '         "seafood-haccp-statutory-requirements"]',
         '         "seafood-haccp-statutory-requirements",\n         "seafood-hazards-controls-guide"]',
         "SLUGS 追加 CAP-23")

ALSO_BLOCK = '''
# v4.10：CAP-23 海产品危害分析判定链。与 CAP-22（Part 123 法条层）配对，
# 还须可跳转到危害分析、化学危害、工艺控制、过敏原、监管边界、取样等卡。
ALSO_READ["seafood-hazards-controls-guide"] = [
    "seafood-haccp-statutory-requirements", "hazard-analysis-method",
    "chemical-hazard-controls", "process-control-validation",
    "allergen-program", "regulatory-boundaries", "inspection-sampling",
    "cgmp-compliance-guide", "reference-tools-discipline",
]
for _s in ("seafood-haccp-statutory-requirements", "hazard-analysis-method",
           "chemical-hazard-controls", "process-control-validation",
           "allergen-program", "regulatory-boundaries", "inspection-sampling",
           "reference-tools-discipline"):
    if "seafood-hazards-controls-guide" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("seafood-hazards-controls-guide")

'''
t = pending.get(BASE / AB) or load(AB)
anchor = "ROUTER_GATE = {"
assert t.count(anchor) == 1
stage(AB, t.replace(anchor, ALSO_BLOCK + anchor, 1))
audit.append({"file": AB, "action": "insert", "label": "ALSO_READ 双向链"})

NEW_SOURCE = '''            {
                "title": "Fish and Fishery Products Hazards and Controls Guidance (4th ed., June 2022) — Seafood Hazards Guide",
                "author": "U.S. FDA, HHS / PHS / CFSAN / Office of Food Safety, Division of Seafood Safety",
                "year": "June 2022 第 4 版（SGR 129）；正文多章页脚仍为 June 2021，Appendix 3 / 5 为 A3-1 / A5-1 (June 2021)，Ch.19 书目 August 2019，属分章滚动修订",
                "content_type": "regulatory-guidance（Guidance for Industry，非约束性；should 仅为建议，可用替代控制策略但须科学论证其充分性）",
                "source_id": "src-fda-seafood-hazards-guide-2022",
                "source_file": "books/fda-pchf-human-food-guidance/source-seafood-hazards-guide-2022.md",
                "note": "由 WorkBuddy 资料库节点 XMsRyrFL0wM1hesg8X6K9u 导出，1,709,446 字节 / 31,321 行；正文 21 章 + 12 附录 + 2 份附加法规全文转录。本件是 21 CFR Part 123 的配套**技术指南层**（how to 判定），与 CAP-22 的**法条义务层**配对而非合并：Ch.2 的 18 步 HACCP 计划开发流程、Ch.3 三张潜在危害表（品种相关 Table 3-2 / 3-3、工艺相关 Table 3-4）与 Ch.4–21 联动、Step 10 在无控制条件下按 `reasonably likely to occur` 逐步判显著性且 Yes/No 都要写第 4 栏理由、Step 11 用 Appendix 3 判定树定 CCP、控制策略示例的 CCP 漂移、关键限值与监控四问。⚠ 三项红线：① 表不得单独使用、指南不替代危害分析、须警觉新出现危害与物种替换；② Appendix 5 的组胺 50/500 ppm 等数值回指 CPG / 21 CFR 556 / 40 CFR 180 / NSSP Guide，是外部法源快照而非本指南新设限值，一律标转引未收；③ 导出件表格列头连写、词条粘连、字符丢失、页码混入、Appendix 3 的 CCP 判定树塌陷成残表，逐字引用只能取散文段落（CAP-23 R 段 37 块经 .cangjie/verify_v4_10_quotes.py 核验 37/37 命中）。引用用「Seafood Hazards Guide 第 4 版 Ch.x / Appendix x / L####」，法条用〔§ 123.xxx〕，不可混引。仍未收：CP 7303.842、NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、Import Alert 16-xx、BAM 海产品章节",
            },
'''
t = pending.get(BASE / AB) or load(AB)
anchor = '        ],\n    },\n    "entry": {'
assert t.count(anchor) == 1, "additional_sources 结束锚点不唯一"
stage(AB, t.replace(anchor, NEW_SOURCE + anchor, 1))
audit.append({"file": AB, "action": "insert", "label": "additional_sources 第十五来源"})

DESC_LINE = (
    '            "另覆盖海产品危害分析与控制的完整判定链（FDA《Fish and Fishery Products Hazards and Controls Guidance》'
    '第 4 版 June 2022，技术指南层）：18 步 HACCP 计划开发流程、Ch.3 品种相关与工艺相关危害三表与 Ch.4–21 联动、'
    '在**无控制条件下**按 reasonably likely to occur 逐步判定显著性且 Yes/No 均须书面写理由、'
    '显著不等于本步设 CCP、Appendix 3 判定树定 CCP、control strategy example 的 CCP 位置漂移、'
    '关键限值可替代但须科学论证充分性、监控四问 What/How/Frequency/Who，'
    '以及组胺与寄生虫等建议参数适用边界和『指南非强制 vs Part 123 法定义务』双向分流。"\n'
)
t = pending.get(BASE / AB) or load(AB)
anchor = '            "适用于食品工厂质量/合规人员'
assert t.count(anchor) == 1
stage(AB, t.replace(anchor, DESC_LINE + anchor, 1))
audit.append({"file": AB, "action": "insert", "label": "entry.description 追加 CAP-23 段"})

CP_LINES = '''            "海产品危害分析判定链以『无控制条件』为闸门：指南要求 The likelihood of a hazard occurring should be judged in the absence of controls——已有控制有效恰恰可能证明该危害 reasonably likely to occur 且控制须纳入 HACCP 计划；把『没出过事』当成『不显著』会跳过整条 CCP 链",
            "Ch.3 的 Table 3-2 / 3-3 / 3-4 只列潜在危害且明文不得单独使用，必须叠加 Ch.4–21 的 Understand the Potential Hazard 与自身/外部专家判断；Worksheet 第 3 栏 Yes/No **都**要在第 4 栏写理由，第 3 栏 No 可跳过 Steps 11–18、第 6 栏 No 可跳过 Steps 12–18；显著≠必须在该步控制，CCP 由 Step 11 判定树另定",
            "第十五来源 FDA 海产品危害与控制指南是**非约束性技术指南层**：should 仅为建议、可另选控制策略与关键限值但须科学论证充分性；Appendix 5 的 50/500 ppm 等数值回指 CPG / CFR / NSSP 外部法源（转引未收），不是新设法定限值；它与 CAP-22 的 Part 123 `shall` 法定义务配对，既不得把指南当法规，也不得因指南非强制把法条义务稀释成可选",
'''
t = pending.get(BASE / AB) or load(AB)
anchor = '        ],\n        "out_of_scope": ['
assert t.count(anchor) == 1
stage(AB, t.replace(anchor, CP_LINES + anchor, 1))
audit.append({"file": AB, "action": "insert", "label": "core_principles +3（42→45）"})

STOP_LINES = '''            "Seafood Hazards Guide 第 4 版的引用须写「Ch.x / Appendix x / L####」，不得写成〔§ 123.xxx〕；法条义务一律回 CAP-22。导出件表格列头连写、词条粘连、`fsh`/`Pufer` 字符丢失、页码混入单元格、Appendix 3 的 CCP 判定树塌陷成残表——**逐字引用只能取散文段落**，判定树仅可复原逻辑，须回查 PDF 原版。封面 June 2022 但多章页脚 June 2021 属分章滚动修订，不得写成 2022 新规",
            "回答海产品危害分析问题时不得把 Ch.3 勾选表、控制策略示例的关键限值、Appendix 5 的 50/500 ppm 或寄生虫冻结三条件写成法定限值或合规清单；也不得因指南非强制就免除〔§ 123.6〕的危害分析与书面 HACCP 计划义务。CP 7303.842、NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507、Import Alert 16-xx、BAM 海产品章节、CPG Sec. 540.525 / 555.300 / 575.100 与 Appendix 5 回指的外部法源一律标「转引未收」；全包自 v4.10 起**十五类不可混引**，当前为 23 张能力卡",
'''
t = pending.get(BASE / AB) or load(AB)
anchor = '        ],\n    },\n    "router_entry": {'
assert t.count(anchor) == 1
stage(AB, t.replace(anchor, STOP_LINES + anchor, 1))
audit.append({"file": AB, "action": "insert", "label": "stop_conditions +2（18→20）"})

# ------------------------------------------------------------------ 2. 事实源精确口径
rep_once(AB,
         '合计**十四类不可混引**（v4.8 新增第十三来源、v4.9 新增第十四来源 21 CFR Part 123）',
         '合计**十五类不可混引**（v4.8 新增第十三来源、v4.9 新增第十四来源 21 CFR Part 123、v4.10 新增第十五来源 FDA 海产品危害与控制指南）',
         "core_principles 来源阶梯")
rep_once(AB,
         '**十四类不可混引**，且 §114.5 并列',
         '**十五类不可混引**，且 §114.5 并列',
         "stop_conditions 引用规范")
rep_once(AB,
         '用户任务超出 22 张能力卡路由范围时',
         '用户任务超出 23 张能力卡路由范围时',
         "stop_conditions 卡数")
rep_once(AB,
         'NSSP Guide、FDA Fish and Fishery Products Hazards and Controls Guidance。引用用〔§ 123.xxx〕。',
         'NSSP Guide（FDA《Fish and Fishery Products Hazards and Controls Guidance》自 v4.10 起已收，见 CAP-23）。引用用〔§ 123.xxx〕。',
         "Part 123 来源 note 移除未收")
rep_once(AB,
         'NSSP Guide、FDA Fish and Fishery Products Hazards and Controls Guidance 均未收，凡涉检查员取证量、贝类生长区分类、组胺与河豚毒素限值一律标『转引未收』',
         'NSSP Guide 仍未收，凡涉检查员取证量、贝类生长区分类一律标『转引未收』；FDA 海产品危害与控制指南自 v4.10 起已收（见 CAP-23），其建议参数与限值回指的外部法源仍须标『转引未收』',
         "stop_conditions 移除指南未收")

# ------------------------------------------------------------------ 3. CAP-22 与新卡分工的实质修正
S22 = ".cangjie/capabilities/cards/seafood-haccp-statutory-requirements.md"
rep_once(S22,
         '、CP 7303.878 合计 **十四类不可混引**。*',
         '、CP 7303.878 与第十五来源 FDA 海产品危害与控制指南合计 **十五类不可混引**。*',
         "CAP-22 开头口径")
rep_once(S22,
         '**Step 7 — 收尾声明。** 每条结论标〔§ 123.xxx〕/〔§ 117.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕或「CP 7303.842 PART x」（后者标未收）；涉及 part 120 / 1240 / 108 / 110 / NSSP / BAM / CPG / Import Alert 全文一律标「转引未收」。**十四类不可混引。**',
         '**Step 7 — 收尾声明。** 每条结论标〔§ 123.xxx〕/〔§ 117.xxx〕/〔§ 113.xxx〕/〔§ 114.xxx〕或「CP 7303.842 PART x」（后者标未收）；涉及 part 120 / 1240 / 108 / 110 / NSSP / BAM / CPG / Import Alert 全文一律标「转引未收」。指南层的危害分析判定链转 CAP-23 `seafood-hazards-controls-guide`，引用写「Seafood Hazards Guide 第 4 版 Ch.x / L####」，不得改写成条款号。**十五类不可混引。**',
         "CAP-22 E 段收尾声明")
rep_once(S22,
         '**B10 — 引用规范（全包统一，十四类不可混引）。**',
         '**B10 — 引用规范（全包统一，十五类不可混引；v4.9 时为十四类）。**',
         "CAP-22 B10")
rep_once(S22,
         'HACCP 模型计划（FDA Fish and Fishery Products Hazards and Controls Guidance 4th ed.）、感官检验与分解判定细则',
         '危害分析判定链与 HACCP 计划表单方法（FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版自 v4.10 起已收，见 CAP-23 `seafood-hazards-controls-guide`）、感官检验与分解判定细则',
         "CAP-22 B12 移除指南未收")
rep_once(S22,
         '25. 用户要「代写 HACCP 计划或出法定身份结论」→ 超出本包，转出（B8）。',
         '25. 用户要「代写 HACCP 计划或出法定身份结论」→ 超出本包，转出（B8）。\n26. 用户问「某个鱼种该考虑哪些危害 / 怎么判显著 / CCP 设在哪 / 关键限值怎么定」→ 转 CAP-23 `seafood-hazards-controls-guide`（指南层判定链）；本卡只回答 Part 123 的**法条义务**，不代替危害分析判定。',
         "CAP-22 A2 追加分流")

M22 = ".cangjie/capabilities/cards/_meta-seafood-haccp-statutory-requirements.yaml"
rep_once(M22,
         '  - 判断哪些问题超出本包（CP 7303.842、part 120/1240/108/110/507、NSSP、BAM、HACCP 模型计划指南、Import Alert 全文）',
         '  - 判断哪些问题超出本包（CP 7303.842、part 120/1240/108/110/507、NSSP、BAM、Import Alert 全文）；FDA 海产品危害与控制指南自 v4.10 起已收，危害分析判定链转 CAP-23',
         "CAP-22 meta intents")
rep_once(M22,
         '  - "十四类不可混引"',
         '  - "十五类不可混引"',
         "CAP-22 meta keyword")
rep_once(M22,
         'NSSP Guide、FDA Fish and Fishery Products Hazards and Controls Guidance 一律「转引未收」',
         'NSSP Guide 一律「转引未收」；FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版自 v4.10 起已收（第十五来源，见 CAP-23），全包十五类不可混引',
         "CAP-22 meta source_label")

# ------------------------------------------------------------------ 4. 其余源码文件的当前口径（逐行、严格排除历史）
HIST_LINE = re.compile(r'v[234]\.\d|第十四类|第十三类|→|历史|当时|升为|起为|起扩为|旧口径|快照|此前|上一版本|初版|changelog|Changelog|dist-v1[23]|口径；|口径）')
EXCLUDE_PREFIX = ('.git/', 'dist-v12/', 'dist-v13/', 'backup-', '.cangjie/apply_v4_',
                  '.cangjie/append_v4_', '.cangjie/install_', '.cangjie/v4-9-',
                  'candidates/v4-10-', 'BOOK_OVERVIEW-seafood-', '.cangjie/verify_v4_10',
                  '.cangjie/assemble_bundle.py', '.cangjie/capabilities/verified.yaml',
                  '.cangjie/capabilities/cards/seafood-haccp-statutory-requirements.md',
                  '.cangjie/capabilities/cards/_meta-seafood-haccp-statutory-requirements.yaml',
                  'source-seafood-hazards-guide-2022.md')
TARGET_SUFFIX = {'.md', '.yaml', '.json', '.py'}

for p in sorted(BASE.rglob('*')):
    if not p.is_file() or p.suffix not in TARGET_SUFFIX:
        continue
    rel = str(p.relative_to(BASE)).replace('\\', '/')
    if any(rel.startswith(x) or x in rel for x in EXCLUDE_PREFIX):
        continue
    t = pending.get(p) or p.read_text(encoding='utf-8', errors='replace')
    if '十四类不可混引' not in t:
        continue
    lines = t.splitlines(keepends=True)
    changed = 0
    for i, line in enumerate(lines):
        if '十四类不可混引' not in line or HIST_LINE.search(line):
            continue
        lines[i] = line.replace('十四类不可混引', '十五类不可混引')
        changed += 1
        audit.append({"file": rel, "action": "line_replace", "line": i + 1,
                      "old": "十四类不可混引", "new": "十五类不可混引"})
    if changed:
        stage(rel, ''.join(lines))

# ------------------------------------------------------------------ 5. version 字段回正
TP = "test-prompts.json"
t = pending.get(BASE / TP) or load(TP)
assert '"version": "v4.10"' in t
stage(TP, t.replace('"version": "v4.10"', '"version": "4.10"', 1))
audit.append({"file": TP, "action": "exact_replace", "label": "version 恢复纯数字格式"})

# ------------------------------------------------------------------ 6. 落盘
for p in pending:
    shutil.copyfile(p, BACKUP / p.relative_to(BASE).as_posix().replace('/', '__'))
for p, text in pending.items():
    p.write_text(text, encoding='utf-8')

report = {
    "version": "v4.10",
    "generated_at": datetime.now().astimezone().isoformat(timespec='seconds'),
    "files_touched": len(pending),
    "actions": len(audit),
    "quote_verification": {"tool": ".cangjie/verify_v4_10_quotes.py",
                           "quotes": 37, "verbatim_hits": 37, "over_100_words": 0, "table_quotes": 0,
                           "body_only": True},
    "audit": audit,
}
(BASE / ".cangjie/v4-10-sources-qa-report.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')

print(f"touched files: {len(pending)}; actions: {len(audit)}")
for a in audit[:14]:
    print(f"  {a['file']:<62} {a.get('label', a.get('line',''))}")
print(f"backup: {BACKUP}")
print("APPLY_V4_10_REVISIONS_OK")
