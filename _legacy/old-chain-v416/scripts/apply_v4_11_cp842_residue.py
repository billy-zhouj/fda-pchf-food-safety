#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""apply_v4_11_cp842_residue.py — v4.11 第二轮：清除「CP 7303.842 正文本包未收」的当前断言。

背景：v4.11 把 CP 7303.842 纳入为第十六来源并新增 CAP-24。主脚本只处理了少数
明确点名的句子，但既有 16 张卡 / meta 里还有约 20 处把该 CP 写成「未收 / 转引未收 /
请提供后纳入」的**当前断言**，若不同步，会与新卡直接冲突并导致错误分流。

纪律（沿用 v4.10 apply_v4_10_residue.py）：
- 每条精确子串 rep_once()，命中数必须恰为 1；内存暂存、备份、末尾一次性落盘。
- 历史陈述一律保留：明确带「在 v4.8 及以前」「本包此前」的句子，以及 v4.10 及更早的
  版本演进记录 / 自检行 / 评测报告，都不在本脚本范围内。
- 只把「未收」改成「已收且属检查程序作业层 + 转 CAP-24 + 双向误读防护」，
  不改写任何法条义务、不把 CP 触发值升格为法规限值。
"""
import json
import shutil
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CARDS = BASE / ".cangjie/capabilities/cards"
BACKUP = BASE / ".cangjie/backup-v4-11-pre-cp842-residue"
AUDIT = BASE / ".cangjie/v4-11-sources-qa-report.json"

C = ".cangjie/capabilities/cards/"
pending = {}
log = []


def read(rel):
    if rel in pending:
        return pending[rel][0]
    raw = (BASE / rel).read_bytes().decode("utf-8")
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
    log.append({"label": label, "file": rel, "kind": "cp842_residue"})


# ------------------------------------------------------------------ 1) 相邻卡的分工与清单
rep_once(C + "fsvp-inspection-program.md",
         "也不收 7303.080 / 7303.803A / 7321.008 / 7371.000 / 7303.842 等 program 全文。",
         "也不收 7303.080 / 7303.803A / 7321.008 / 7371.000 等 program 全文；"
         "**7303.842 自 v4.11 起已收**（第十六来源，CAP-24 `seafood-inspection-program`），"
         "但它仍是检查程序作业层，不是 FSVP 法规正文，也不改变本卡的 FSVP 判定链。",
         "FSVP B10 未收清单")

rep_once(C + "inspection-readiness.md",
         "其他 Compliance Programs（7303.878 FSVP、7303.080 Produce Safety、7304.019 / 7303.842 / 7371.000 / 7321.006 等；**7303.070 已由 CAP-19 收入**）",
         "其他 Compliance Programs（7303.080 Produce Safety、7304.019 / 7371.000 / 7321.006 等；"
         "**7303.070 已由 CAP-19、7303.878 已由 CAP-21、7303.842 自 v4.11 起已由 CAP-24 收入**）",
         "迎检 B5 已收/未收清单")

rep_once(C + "inspection-readiness.md",
         "但除 **7303.050 已收（CAP-17）** 与 **7303.070 已收（CAP-19）** 外，本包没有其余这些 program 的正文",
         "但除 **7303.050（CAP-17）**、**7303.070（CAP-19）**、**7303.878（CAP-21）** "
         "与 **7303.842（自 v4.11 起，CAP-24）** 已收外，本包没有其余这些 program 的正文",
         "迎检 B10 相邻 program 正文")

rep_once(C + "lacf-inspection-program.md",
         "| 海产品 LACF | 7303.070 + 7303.842 | 本卡（仅分流，HACCP 正文未收） |",
         "| 海产品 LACF | 7303.070 + 7303.842 | 本卡（仅分流）；7303.842 检查程序转 CAP-24、"
         "Part 123 法条转 CAP-22、危害分析判定链转 CAP-23 |",
         "LACF 海产品分流表")

rep_once(C + "lacf-inspection-program.md",
         "21 CFR part 507 与 7303.842 正文。不得从 CP 的检查动作反推法条",
         "21 CFR part 507 正文（CP 7303.842 自 v4.11 起已收，见 CAP-24；"
         "但它回指的 CPG / BAM 判据全文仍未收）。不得从 CP 的检查动作反推法条",
         "LACF B2 转引未收清单")

rep_once(C + "lacf-inspection-program.md",
         "本包**只收了前两者**；",
         "本包已收其中的 7303.040 / 7303.050 / 7303.842（分别 CAP-16 / CAP-17 / CAP-24，"
         "其中 7303.842 自 v4.11 起），另已收 7303.070（CAP-19）与 7303.878（CAP-21），"
         "其余 7371.000 / 7321.002 / 7321.005 / 7321.006 / 7304.004A / 7309.006 等仍未收；",
         "LACF B10 只收前两者")

# ------------------------------------------------------------------ 2) CAP-22 法条卡
S = C + "seafood-haccp-statutory-requirements.md"
rep_once(S,
         "问「FDA 来查水产品查什么」→ 转 CP 7303.842（**正文本包未收**，只给接口）。",
         "问「FDA 来查水产品查什么」→ 转 CAP-24 `seafood-inspection-program`"
         "（CP 7303.842 自 v4.11 起已收，承载完整检查判定链）。",
         "CAP-22 A2 路由")

rep_once(S,
         "检查员层：CP 7303.842 的取样与判定（**正文本包未收，不得引用其数值**）。",
         "检查员层：CP 7303.842 的取样与判定（自 v4.11 起已收，转 CAP-24；"
         "其 500/50/35 ppm 等是检查员触发值，不是法规限值，不得写成本卡的法条数字）。",
         "CAP-22 Step 6 数字分层")

rep_once(S,
         "或「CP 7303.842 PART x」（后者标未收）",
         "或「CP 7303.842 PART x」（后者自 v4.11 起已收，转 CAP-24）",
         "CAP-22 Step 7 收尾声明")

rep_once(S,
         "**B1 — CP 7303.842（海产品检查程序）正文本包未收，这是本卡最大缺口。** "
         "用户下载目录里有 `20250929_CP 7303.842...pdf` 但本版未纳入。"
         "凡涉「FDA 来查水产品查什么、抽样多少、什么情况开 483、何时建议 Import Alert」的问题，"
         "只能回答「该 CP 正文本包未收，请提供后纳入」，**不得凭 Part 123 反推检查员作业口径**，"
         "也不得用 CP 7303.050 / 7303.070 的数值替代。",
         "**B1 — CP 7303.842 自 v4.11 起已收，但它是检查程序层、不是法条层。** "
         "第十六来源（2023-11-01 版 / 2025-09-30 更正）落在 CAP-24 `seafood-inspection-program`。"
         "凡涉「FDA 来查水产品查什么、抽样多少、什么情况开 483、何时建议 Import Alert」的问题，"
         "转 CAP-24 按「CP 7303.842 PART x / Table x」回答；**不得凭 Part 123 反推检查员作业口径**，"
         "也不得把 CP 的检查动作、Table 1/2 优先级、PART IV 触发值反写成〔§ 123.xxx〕的企业义务，"
         "更不得用 CP 7303.050 / 7303.070 的数值替代。反向同理：不能因 CP 非强制而把 Part 123 的 `shall` 义务稀释成可选。",
         "CAP-22 B1 最大缺口（整段改写）")

rep_once(S,
         "**part 120 / 1240 / 108 / 110 / 507 与 CP 7303.842、NSSP Guide 一律标「转引未收」。**",
         "**part 120 / 1240 / 108 / 110 / 507 与 NSSP Guide 一律标「转引未收」；"
         "CP 7303.842 自 v4.11 起已收（CAP-24），按「CP 7303.842 PART x / Table x / ATTACHMENT A #x / Lxxx」"
         "引用，不得改写成条款号，也不得与本卡的〔§ 123.xxx〕混引。**",
         "CAP-22 B10 引用规范")

rep_once(S,
         "21 CFR part 120 / 1240 / 108 / 110 / 507 正文、CP 7303.842 正文、NSSP Guide 全文、",
         "21 CFR part 120 / 1240 / 108 / 110 / 507 正文、NSSP Guide 全文、"
         "CP 7303.842 回指的 CPG / BAM 方法全文（CP 7303.842 检查程序正文自 v4.11 起已收于 CAP-24，本卡不代答）、",
         "CAP-22 B12 不覆盖清单")

# ------------------------------------------------------------------ 3) CAP-23 指南卡
G = C + "seafood-hazards-controls-guide.md"
rep_once(G,
         "*正文本包**仍未收**：NSSP Guide（软体贝类）；CP 7303.842 自 v4.11 起已收（CAP-24）、"
         "21 CFR part 120（果汁 HACCP）／part 1240（贝类卫生）／part 108／part 110／part 507、"
         "Import Alert 16-xx 系列、BAM 海产品章节，以及本指南 Appendix 5 回指的 "
         "CPG Sec. 540.525／555.300／575.100、21 CFR 556 系列、40 CFR 180 系列、Import Tolerance 等外部法源。"
         "涉及其具体数值与条款级结论一律标「转引未收」。",
         "*正文本包**仍未收**：NSSP Guide（软体贝类）、21 CFR part 120（果汁 HACCP）／"
         "part 1240（贝类卫生）／part 108／part 110／part 507、Import Alert 16-xx 系列、BAM 海产品章节，"
         "以及本指南 Appendix 5 回指的 CPG Sec. 540.525／555.300／575.100、21 CFR 556 系列、"
         "40 CFR 180 系列、Import Tolerance 等外部法源。涉及其具体数值与条款级结论一律标「转引未收」。"
         "CP 7303.842 检查程序正文自 v4.11 起已收（CAP-24，检查程序作业层），但其回指的 CPG / BAM 判据全文仍未收，"
         "且不得与本指南建议层混引。",
         "CAP-23 开头仍未收清单（重写）")

rep_once(G,
         "③ **外部法源转引未收**（Appendix 5 回指的 CPG / 21 CFR 556 / 40 CFR 180 / NSSP Guide / "
         "Import Tolerance、FD&C Act 掺假条款、CP 7303.842、part 120/1240/108/110/507、"
         "Import Alert 16-xx、BAM 海产品章节）。",
         "③ **外部法源转引未收**（Appendix 5 回指的 CPG / 21 CFR 556 / 40 CFR 180 / NSSP Guide / "
         "Import Tolerance、FD&C Act 掺假条款、part 120/1240/108/110/507、Import Alert 16-xx、"
         "BAM 海产品章节；CP 7303.842 检查程序正文自 v4.11 起已收但属检查程序层，见 CAP-24，"
         "仍不得把其触发值当成本指南的建议限值）。",
         "CAP-23 Step 8 三层标签")

rep_once(G,
         "回指对象：CPG Sec. 540.525（组胺）／540.250／540.600／555.300／555.425／575.100、"
         "Compliance Program 7303.842、21 CFR 556 系列、40 CFR 180 系列、NSSP Guide、"
         "Import Tolerance、ICMSF、FD&C Act 21 U.S.C. 342 —— 本包多数未收，"
         "涉具体数值合规结论一律标「转引未收」",
         "回指对象：CPG Sec. 540.525（组胺）／540.250／540.600／555.300／555.425／575.100、"
         "21 CFR 556 系列、40 CFR 180 系列、NSSP Guide、Import Tolerance、ICMSF、"
         "FD&C Act 21 U.S.C. 342 —— 本包多数未收（Compliance Program 7303.842 检查程序正文自 v4.11 起"
         "已收于 CAP-24，但它回指的 CPG / BAM 判据全文仍未收），涉具体数值合规结论一律标「转引未收」",
         "CAP-23 B7 Appendix 5 回指")

rep_once(G,
         "part 120 / 1240 / 108 / 110 / 507、CP 7303.842、NSSP Guide 一律标「转引未收」。",
         "part 120 / 1240 / 108 / 110 / 507、NSSP Guide 一律标「转引未收」；"
         "CP 7303.842 自 v4.11 起已收（CAP-24），按「CP 7303.842 PART x / Table x / Lxxx」引用，"
         "属检查程序作业层，不得与指南建议层混引。",
         "CAP-23 B11 引用规范尾部")

rep_once(G,
         "正文本包仍未收：CP 7303.842、NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、",
         "正文本包仍未收：NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、"
         "CP 7303.842 回指的 CPG / BAM 判据全文（CP 7303.842 检查程序正文自 v4.11 起已收于 CAP-24）、",
         "CAP-23 B12 仍未收清单")

# ------------------------------------------------------------------ 4) CAP-22 meta
M = C + "_meta-seafood-haccp-statutory-requirements.yaml"
rep_once(M,
         "CP 7303.842 与 part 120/1240/NSSP 正文仍未收。",
         "part 120/1240/NSSP 正文仍未收；CP 7303.842 自 v4.11 起已收（检查程序层，转 CAP-24），"
         "仍不得反推法条。",
         "CAP-22 meta one_liner")

rep_once(M,
         "CP 7303.842 海产品检查程序、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、"
         "NSSP Guide 一律「转引未收」；",
         "21 CFR part 120 / 1240 / 108 / 110 / 507 正文、NSSP Guide 与 CP 7303.842 回指的 "
         "CPG / BAM 判据全文一律「转引未收」（CP 7303.842 检查程序正文自 v4.11 起已收于 CAP-24，"
         "但不得反推法条）；",
         "CAP-22 meta source_label")

# ------------------------------------------------------------------ 5) dry-run / 落盘
print(f"touched files: {len(pending)}")
for rel in sorted(pending):
    print("  ", rel)
print("residue fixes:", len(log))

if "--apply" not in sys.argv:
    print("\nDRY RUN ONLY (pass --apply to write)")
    sys.exit(0)

BACKUP.mkdir(parents=True, exist_ok=True)
for rel in pending:
    shutil.copyfile(BASE / rel, BACKUP / rel.replace("/", "__"))
for rel, (text, nl) in pending.items():
    (BASE / rel).write_bytes(text.replace("\n", nl).encode("utf-8"))

if AUDIT.exists():
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    audit["residue_fixes"] = log
    audit["files_touched"] = sorted(set(audit.get("files_touched", [])) | set(pending))
    audit["actions"] = audit.get("actions", []) + log
    audit["policy"] += "；第二轮清除「CP 7303.842 未收」当前断言，历史陈述保留"
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"backup: {BACKUP.relative_to(BASE).as_posix()}")
print("APPLY_V4_11_CP842_RESIDUE_OK")
