#!/usr/bin/env python3
"""v4.8 口径回补：十二类→十三类、20 卡→21 卡，并把 CP 7303.878 接入 bundle。

规则沿用 v4.7 经验：
- 全局字符串替换打印命中数（不静默）
- 结构性插入一律 `assert text.count(anchor) == 1`
- 执行前把受影响文件备份到 .cangjie/backup-v4-8-pre-revisions/
"""
from __future__ import annotations

import shutil
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
CJ = BOOK / ".cangjie"
BACKUP = CJ / "backup-v4-8-pre-revisions"
BACKUP.mkdir(exist_ok=True)

BUNDLE = CJ / "assemble_bundle.py"
CARD_DIR = CJ / "capabilities" / "cards"

# ---------------------------------------------------------------- 备份
files = [BUNDLE, BOOK / "candidates/glossary.md", BOOK / "GLOSSARY.md",
         BOOK / "test-prompts.json", BOOK / "PIPELINE_STATE.md",
         BOOK / "BOOK_OVERVIEW.md", BOOK / "DIGEST.md",
         BOOK / "source-cp-7303-070-2024.md", BOOK / "source-cfr-part113-2025.md",
         BOOK / "source-cfr-part114-2025.md"]
files += sorted(CARD_DIR.glob("*.md"))
for f in files:
    if f.exists():
        shutil.copy2(f, BACKUP / f.name)
print(f"backed up {len(files)} files -> {BACKUP.name}")


def replace_one(path: Path, old: str, new: str, label: str = "") -> None:
    t = path.read_text(encoding="utf-8")
    n = t.count(old)
    assert n == 1, f"{path.name} [{label}]: expected 1 hit, got {n} for {old[:60]!r}"
    path.write_text(t.replace(old, new, 1), encoding="utf-8")
    print(f"  {path.name:42s} {label or old[:28]:36s} OK")


def append_line(path: Path, prefix: str, suffix: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    idx = [i for i, l in enumerate(lines) if l.lstrip().startswith(prefix)]
    assert len(idx) == 1, f"{path.name}: {len(idx)} hits for prefix {prefix[:40]!r}"
    i = idx[0]
    nl = "\n" if lines[i].endswith("\n") else ""
    body = lines[i].rstrip("\r\n")
    if body.endswith("*"):  # 斜体来源分层段：插在闭合星号之前
        lines[i] = body[:-1] + suffix + "*" + nl
    else:
        lines[i] = body + suffix + nl
    path.write_text("".join(lines), encoding="utf-8")
    print(f"  {path.name:42s} append after {prefix[:28]:30s} OK")


# ---------------------------------------------------------------- 1. 卡片：当前口径
print("\n[1] 卡片口径回补")
for f in sorted(CARD_DIR.glob("*.md")):
    t = f.read_text(encoding="utf-8")
    n12 = t.count("十二类")
    n20 = t.count("20 张")
    if not (n12 or n20):
        continue
    t = t.replace("十二类", "十三类")
    t = t.replace("20 张能力卡", "21 张能力卡")
    t = t.replace("20 张卡", "21 张卡")
    t = t.replace("十三类不可混引，v4.7", "十三类不可混引，v4.8")
    t = t.replace("v4.7 起全包统一「**十三类不可混引**」", "v4.7 起十二类、**v4.8 起全包统一「十三类不可混引」**")
    f.write_text(t, encoding="utf-8")
    print(f"  {f.name:52s} 十二类 {n12} / 20 张 {n20}")

# 两张来源分层段补上第十三类
append_line(CARD_DIR / "inspection-readiness.md", "*来源分层：",
            "（**v4.8 起第十三类来源为 CP 7303.878 FSVP 检查程序**，见 CAP-21 `fsvp-inspection-program`；21 CFR part 1 subpart L 正文仍未收。）")
append_line(CARD_DIR / "cgmp-compliance-guide.md", "*来源分层：",
            "（**v4.8 起第十三类来源为 CP 7303.878 FSVP 检查程序**，见 CAP-21 `fsvp-inspection-program`。）")

# ---------------------------------------------------------------- 2. 来源文件头
print("\n[2] 来源文件头引用规范")
for name in ["source-cp-7303-070-2024.md", "source-cfr-part113-2025.md", "source-cfr-part114-2025.md"]:
    p = BOOK / name
    t = p.read_text(encoding="utf-8")
    assert t.count("十二类") == 1, f"{name}: 十二类 count != 1"
    t = t.replace("十二类", "十三类", 1)
    t = t.replace("全包自 v4.7 起「", "全包自 v4.7 起十二类、v4.8 起「", 1)
    t = t.replace("**十二类来源不可混引**", "**十三类来源不可混引（v4.8 新增 CP 7303.878）**", 1)
    p.write_text(t, encoding="utf-8")
    print(f"  {name} OK")

# ---------------------------------------------------------------- 3. assemble_bundle.py 全局口径
print("\n[3] assemble_bundle.py 口径与结构")
t = BUNDLE.read_text(encoding="utf-8")
assert t.count("十二类") == 2, f"bundle 十二类 count {t.count('十二类')}"
t = t.replace("十二类", "十三类")
assert t.count("20 张") == 2, f"bundle 20 张 count {t.count('20 张')}"
t = t.replace("20 张 _meta", "21 张 _meta")
t = t.replace("用户任务超出 20 张能力卡", "用户任务超出 21 张能力卡")
BUNDLE.write_text(t, encoding="utf-8")
print("  全局口径替换 OK")

replace_one(BUNDLE,
            '         "inspection-sampling", "investigator-authority-procedure", "lacf-inspection-program",\n'
            '         "lacf-statutory-requirements"]',
            '         "inspection-sampling", "investigator-authority-procedure", "lacf-inspection-program",\n'
            '         "lacf-statutory-requirements", "fsvp-inspection-program"]',
            "SLUGS +CAP-21")

# ALSO_READ 后处理：新键 + 反向链
anchor_router = 'ROUTER_GATE = {"independent_intent": False,'
read_block = '''ALSO_READ["fsvp-inspection-program"] = [
    "supply-chain-verification", "regulatory-boundaries", "inspection-readiness",
    "inspection-sampling", "investigator-authority-procedure",
    "lacf-inspection-program", "cgmp-compliance-guide",
]
for _s in ("supply-chain-verification", "regulatory-boundaries", "inspection-readiness",
           "investigator-authority-procedure", "lacf-inspection-program",
           "cgmp-compliance-guide"):
    if "fsvp-inspection-program" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("fsvp-inspection-program")

'''
replace_one(BUNDLE, anchor_router, read_block + anchor_router, "ALSO_READ 双向链")

# 第十三来源
anchor_close = '        ],\n    },\n    "entry": {'
src_block = '''            {
                "title": "Compliance Program 7303.878 - Foreign Supplier Verification Programs Inspections",
                "author": "U.S. FDA, Human Foods Program (HFP) / Office of Inspections and Investigations (OII)",
                "year": "Transmittal 2023-CPM-CFSAN-003；Implementation Date 09/27/2023；Date of Issuance 08/28/2025（更正）；33 页 / 20 书签",
                "content_type": "inspection-program（FDA 给检查员、进口分区合规官与中心审评人员的内部作业指导；非法规、非 Guidance for Industry、不创设企业义务）",
                "source_id": "src-fda-cp-7303-878-2023",
                "source_file": "books/fda-pchf-human-food-guidance/source-cp-7303-878-2023.md",
                "note": "由用户提供的官方 508-Compliant PDF 经 pdf2md-pro 转换并清除 62 行页眉。⚠ 版本判定：Change History 为 2021-10-20 首发 → 2023-09-27 Update（改名 FSVP Inspections、补 7303.803A / 7303.080 程序交互、Part V 执法澄清）→ 2024-08-20 Pen/Ink → 2025-08-28 Corrections（仅 POC 与机构名称缩写更新）；故为 2023 版程序的 2025 更正版，不是 2025 新 program。法源为 FSMA §301 增订的 FD&C Act §805 与 21 CFR part 1, subpart L（§§1.500-1.514），**该法规正文本包未收，一律标转引未收**。PART II.3.A 给 deemed compliance：进口商同时为 manufacturer/processor 且符合 21 CFR part 117 / 507 供应链要求时视为符合 FSVP，但 except they must comply with section 1.509；不是 receiving facility 的进口商仍须完整 FSVP。PART III.1.C 明写 Samples will not be collected as part of an FSVP inspection、PART IV 四节 Intentionally Left Blank。PART V 给 483a 观察分级、NAI/VAI/OAI、§801(a)(3) / §1.514(a) 拒绝入境与 §301(zz) / §1.514(b) 禁止行为、direct reference authority 仅限有限情形、Import Alert 99-41 Red List 按『食品+境外供应商』组合列入与移除流程。⚠ 99-41 与 CP 7303.070 的 99-37 / 99-38 不是同一个 Import Alert。引用用「CP 7303.878 PART x」。仍未收：21 CFR part 1 subpart L / 111 / 112 / 120 / 123 / 507 正文、Import Alert 99-41 全文、FSVP Guidance for Industry、FSVP Implementation Work Instructions 与 IP guidance tabs、HFP Enforcement Bulletin #13/#6、RPM 4-1-8、SOP-001642",
            },
'''
replace_one(BUNDLE, anchor_close, src_block + anchor_close, "additional_sources +1")

# entry.description 追加 FSVP 覆盖段
anchor_apply = '            "适用于食品工厂质量/合规人员、采购与供应商管理者'
desc_line = ('            "另覆盖 FSVP 进口商检查（CP 7303.878，2023 版 / 2025-08-28 更正）：按 §1.500 判定 FSVPI 身份、'
             'FSVP（FD&C Act §805 / 21 CFR part 1 subpart L）与 Part 117 Subpart G 供应链程序的主体分流、'
             'deemed compliance 但不免 §1.509 每一 entry line 的 UFI/DUNS 申报、§1.501 八类豁免与 standard / modified requirements 分节、'
             'FSVP 检查不取样与 PART IV 全空、483a 观察分级与 NAI/VAI/OAI、§801(a)(3) 拒绝入境与 §301(zz) 禁止行为、'
             'Warning Letter → Import Alert 99-41 Red List 加/删名单与「未上 Red List 仍可进口」等反直觉限制。"\n')
replace_one(BUNDLE, anchor_apply, desc_line + anchor_apply, "entry.description +FSVP")

# core_principles 补充
replace_one(BUNDLE, "合计**十三类不可混引**；CP 7303.070 的 4.40",
            "与 CP 7303.878 合计**十三类不可混引**（v4.8 新增第十三来源）；CP 7303.070 的 4.40",
            "core_principles 十三类")

anchor_oos = '        ],\n        "out_of_scope": ['
core_new = '''            "FSVP 与 Part 117 Subpart G 供应链程序是两套法源、两类主体：FD&C Act §805 / 21 CFR part 1 subpart L 管进口商 FSVPI，FD&C Act §418 / 21 CFR part 117 Subpart G 管接收设施 receiving facility；CP 7303.878 PART II.3.A 的 deemed compliance 只覆盖前者对进口食品的义务，且原文 `except they must comply with section 1.509`——UFI/DUNS 每一 entry line 电子申报不因此免除。不是 receiving facility 的纯贸易进口商没有该通道",
            "CP 7303.878 是检查员内部作业指导，PART III.1.C 明写 `Samples will not be collected as part of an FSVP inspection.`、PART IV 四节 Intentionally Left Blank；FSVP 检查查的是 FSVP/危害分析/供应商批准评价/验证活动/§1.509/纠正措施记录，不得套 CP 7303.050 的样品量与环境拭子，也不得从 CP 反推 21 CFR part 1 subpart L 条文",
            "Import Alert 99-41（FSVP 不合规进口商）与 CP 7303.070 的 99-37/99-38（LACF/AF 备案与过程控制）不是同一个 Alert：99-41 按『具体食品 + 具体境外供应商组合』或全部食品列入 Red List，未列组合在不受其他掺假/误标 Alert 约束时仍可进口；移除须按 99-41 指示提交证据并先于再次进口。direct reference authority 仅在有限情形授予，其余案件须经 CMS 送 Center 并取得分类一致；首次违法不默认优先执法；§1.507 disclosure 不能替代 §801(b)/§1.95 整改提案资料",
'''
replace_one(BUNDLE, anchor_oos, core_new + anchor_oos, "core_principles +3")

# out_of_scope +1
anchor_cn = '            "中国 GB 14881 等非美国法规的直接合规判定（本技能只提供 FDA 方法论与条款，跨体系映射需人工判断）",'
oos_new = ('            "21 CFR part 1, subpart L（FSVP 法规 §§1.500-1.514）正文、Import Alert 99-41 全文、'
           'FSVP Guidance for Industry 与 FSVP Implementation Work Instructions / Inspection Protocol guidance tabs、'
           'HFP Enforcement Bulletin #13/#6、RPM 4-1-8、21 CFR part 111/112/120/123/507 正文'
           '（CP 7303.878 只给检查员作业口径，法条义务一律标「转引未收」，不得从 CP 反推）",\n')
replace_one(BUNDLE, anchor_cn, oos_new + anchor_cn, "out_of_scope +1")

# stop_conditions：引用规范补 CP 7303.878 与 part 1 subpart L
replace_one(BUNDLE, 'CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」标注；21 CFR part 108 / 110 / 120 / 123',
            'CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」标注，CP 7303.878 用「CP 7303.878 PART x」标注；'
            '21 CFR part 1 subpart L / 108 / 110 / 120 / 123',
            "stop_conditions 引用规范")

replace_one(BUNDLE, '其他 Compliance Programs（7303.878 / 7303.080', '其他 Compliance Programs（7303.080',
            "stop_conditions 移除 7303.878 未收表述")

anchor_last = '引用须注明是 Federal Register 规则而非本包来源",\n        ],'
stop_new = '''            "CP 7303.878 的版本口径锁定 2023-09-27 版 / 2025-08-28 更正（Transmittal 2023-CPM-CFSAN-003，Change History 的 2025 条目只改 POC 与机构名称缩写），不得写成「2025 版 7303.878」或套用 CPGM 7303.040 的 2025-CPM-HFP-001 Transmittal 形态；CP 7303.819 是 2006 FY06-08 旧程序、已过 COMPLETION DATE 9/30/08 而非现行，准确说法不是「法规意义上废止」。FSVP 法规条文、Import Alert 99-41 全文、FSVP Guidance Q&A、IP guidance tabs 一律标「转引未收」",
            "回答 FSVP 问题时不得把 CP 7303.878 的 483a 观察分级、NAI/VAI/OAI、WL / Import Alert 99-41 建议流程写成企业法定义务或必然法律后果；不得把 §117.5(d)（part 113 活动的 Subparts C/G 豁免）套到 FSVP 轨道；不得把 Import Alert 99-41 与 99-37 / 99-38 混引",
'''
replace_one(BUNDLE, anchor_last, anchor_last.replace('\n        ],', '\n' + stop_new + '        ],'), "stop_conditions +2")

print("\n[3] done")
