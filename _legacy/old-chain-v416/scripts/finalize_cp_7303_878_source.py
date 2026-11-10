#!/usr/bin/env python3
"""清理 pdf2md-pro 转出的 CP 7303.878 来源 md，并前置导入说明文件头。

- 删除每页重复的 **Date of Issuance** / **Transmittal Number** 页眉行
- 折叠由此产生的连续空行
- 前置「效力层级 / 版本判定 / 法源三角 / 关键口径 / 引用规范 / 转换局限」
- 更新 .cangjie/cp-7303-878-convert-report.json
"""
from __future__ import annotations

import json
import re
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
SRC = BOOK / "source-cp-7303-878-2023.md"
REPORT = BOOK / ".cangjie" / "cp-7303-878-convert-report.json"

HEADER = """# FDA Compliance Program 7303.878 — Foreign Supplier Verification Programs Inspections（2023 版程序 / 2025-08-28 更正）

> **来源**：用户提供的官方 508-Compliant PDF `CP7303.878 Foreign Supplier Verification Programs Inspections 508-Compliant.pdf`（490 KB，33 页 / 20 书签），经 `pdf2md-pro` 转换，保留英文原文以便逐字引证。
> PDF 首页元信息：**`Transmittal Number: 2023-CPM-CFSAN-003`；`Date of Issuance: 08/28/2025`；`Implementation Date: 09/27/2023`**；CHAPTER 03 – FOODBORNE MICROBIOLOGICAL HAZARDS；SUBJECT: Foreign Supplier Verification Programs Inspections。Product/Assignment Codes：`03878`（人类食品 FSVP 检查）、`03878D`（膳食补充剂）、`03878P`（农产品）、`71878`（动物食品）。FIELD REPORTING REQUIREMENTS 要求用 **eNSpect** 完成 EIR 与 Inspection Protocol（检查 OP12 / 调查 OP13），例外需主管背书；纠正措施记入 **CAR**。
> ⚠ **版本判定（勿按文件名或首页签发日误读）**：Change History（PDF p4）依次列：Initial Issuance **10/20/2021** → Update **09/27/2023**（标题由 Import Food Operations 改为 FSVP Inspections、补 7303.803A / 7303.080 程序交互、Part V 执法流程澄清）→ Pen/Ink（updates in red）**08/20/2024**（修 FSPCA 课程链接、明确部分 FSVP 案件获 direct reference authority、更新 POC）→ **Corrections 08/28/2025（仅重组后的 POC 与机构名称/缩写更新）**。故本件是 **2023-09-27 版程序（Transmittal 2023-CPM-CFSAN-003）的 2025-08-28 更正版**，不是 2025 新 program；与 CP 7303.050（2022 签发 / 2025-09-10 更正）、CP 7303.070（2024 签发 / 2025-09-26 更正）同属「旧程序 + 更正本」形态，也不同于 CPGM 7303.040 的 `2025-CPM-HFP-001`（新 Transmittal）。引用写「CP 7303.878（2023 版 / 2025-08-28 更正）」。

## 效力层级与使用边界（导入说明，非原文）

- 本件是 **FDA Compliance Program Guidance Manual / Manual 第 7303.878 章**，是 FDA 给**检查员、进口分区合规官与中心审评人员**的内部作业指导（PART I 明写 `provides instruction to field staff`），覆盖检查优先级、检查实施、报告与执法建议。**不是法规、不是 Guidance for Industry、不创设企业义务**；企业用它理解「FSVP 检查会查什么、什么情况会升级到 Warning Letter / Import Alert」，合规结论仍须回指法规条文。
- ⚠ **法源三角：21 CFR part 1, subpart L（§§ 1.500–1.514）正文未收**：FSVP 法规由 FSMA §301 增订的 **FD&C Act §805** 授权，2015-11 发布（`21 CFR part 1, subpart L or 21 CFR 1.500 - 1.514`）；执法还援引 **§801(a)(3) 拒绝入境**、**§301(zz) 禁止行为**、§302 禁令 / §303 刑事 / §306 debarment。**本包未收 21 CFR part 1 subpart L 正文**，凡引 §1.5xx 条款一律标「转引未收」，**不得从本 CP 反推条文原文**，也不得把 CP 的检查动作写成法定义务。同样未收：21 CFR part 111（膳食补充剂 CGMP）、part 112（农产品安全）、part 113 / 114 之外的 part 120 / 123、part 507（动物食品 PC）、Import Alert 99-41 全文、FSVP Guidance for Industry 全文、FSVP Implementation Work Instructions、Inspection Protocol（IP）guidance tabs、HFP Enforcement Bulletin #13 / #6、RPM 4-1-8、SOP-001642、IOM 5.11 / 8.1.9 之外的章节。
- **与本包既有来源的接口（最易误用处）**：① **FSVP ≠ Part 117 Subpart G 供应链程序**。FSVP 是**进口商（FSVPI，§1.500 定义）**对境外供应商的义务；Supply-Chain Program 是**接收设施（receiving facility）**在〔§ 117.135〕及 Subpart G 下的义务。CP `PART II.3.A` 与 CPGM 7303.040 `PART III` 原文一致：制造商/加工商同时是进口商且**符合 21 CFR part 117（或 507）供应链要求**时，**deemed to be in compliance with the FSVP requirements**（**但 §1.509 入境标识义务不因此免除**）；反之「不是 receiving facility」的进口商仍须完整履行 FSVP。② CPGM 7303.040 的 Program Interactions 已列 `CP 7303.878` 为第 (15) 项，并要求首次检查向兼进口商的设施提供 FSVP handout。③ `PART II.3.D` 给 LACF 的 §1.502(a)-(b) 特殊分流，可与 v4.7 的〔§ 113.xxx〕〔§ 114.xxx〕正文对照。④ 与 CP 7303.050（取样）、CP 7303.070（LACF/AF）、CP 7303.080（农产品）、CP 7303.803A（境内 LACF/AF）、CP 7321.008（膳食补充剂）、CP 7371.000（动物食品）分工见 `PART II.3`。
- **CP 7303.819 状态更正**：v4.6 收尾时曾把 `PDF--CP-7303.819.pdf` 概括为「已废止」。本件 Change History 的 2023 Update 原文写 `Instead of adding general import operations content to this CP, CP 7303.819 Import Foods General is being updated.`；本地那份 7303.819 是 **FY06/07/08 的 2006 年旧程序（IMPLEMENTATION DATE 9/5/06，COMPLETION DATE 9/30/08）**。故准确表述是「**2006 旧程序、已过 completion date、非现行；7303.878 把一般进口作业内容交由其更新版承接**」，而不是「法规意义上报废」。该份仍未纳入本包。
- 引用规范：本件内容标注「**CP 7303.878 PART I.1**」「**CP 7303.878 PART III.1.C**」「**CP 7303.878 PART V.3.C**」这类章/节号；Part 117 法规标〔§ 117.xxx〕，Part 113 / 114 标〔§ 113.xxx〕〔§ 114.xxx〕；**21 CFR part 1 subpart L 及上述未收正文一律注明「转引未收」**。全包 **十三类来源不可混引**（21 CFR Part 117 法规正文 / PCHF 行业指南 / L.mono Draft / SECG / Ed.5 / Food Defect Levels Handbook / CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / 21 CFR Part 113 法规正文 / 21 CFR Part 114 法规正文 / **CP 7303.878**）。

## 关键口径（逐字核对，勿沿用二手摘要）

- `PART I.1`：**§1.500** 定义 importer = 入境时美国货主/收货人；无美国货主/收货人时为经签署同意书确认的美国代理/代表，缩写 **FSVPI**。**§1.502(a)** 要求对每一种进口食品 develop, maintain, and follow FSVP，保证境外供应商遵循至少与美国同等公共卫生保护水平的过程（FD&C Act §418 危害分析与风险预防控制 / §419 农产品安全），并确保符合 §402（掺假）与 §403(w)（主要食物过敏原标签）。**§1.509** 要求每一 entry line 报关时电子提供名称、邮箱与 **UFI（FDA 认可的 DUNS 号码）**。
- `PART I.1.B/C` FDA 把 FSVP 条款分为 **standard requirements**（§1.502 / 1.503 / 1.504 / 1.505 / 1.506 / 1.508 / 1.509 / 1.510）与 **modified requirements**（§1.507 危害在进口后受控 / §1.511 膳食补充剂 / §1.512 极小进口商 VSI 或小境外供应商 / §1.513 官方认可或等效食品安全体系国家）；原文明确 `FSVPIs who meet the criteria for modified requirements may choose to follow standard requirements`。
- `PART I.2` **§1.501 豁免**：果汁与水产/水产品且供应商符合 part 120 / 123（(b)(1)）、用于制造上述产品的原料且 FSVPI 符合 part 120 / 123（(b)(2)）、研究或评估用（(c)）、个人消费（(d)）、酒精饮料及特定相关食品（(e)）、转运过境（(f)(1)）与进口加工后复出口且不在美销售（(f)(2)）、美国生产出口后未再境外加工而退回（(g)）、进口时受 USDA 管辖的特定肉/禽/蛋制品（(h)）。
- `PART II.3.A` **deemed compliance 的边界**：进口原料自用的 manufacturer/processor 若被认定符合 21 CFR part 117 / 507 供应链要求，则对该进口食品 deemed in compliance with FSVP，**但 `except they must comply with section 1.509`**；不是 receiving facility 的进口商、以及仅受 Subpart B CGMP 或 §117.206 / §507.51 modified requirements 约束的仓储设施，仍可能单独接受 FSVP 检查。
- `PART III.1.A` 检查可 **on-site or remote**（RRA 另见 Remote Regulatory Assessments Q&A 草案）；检查员须确认是否开发了 FSVP、是否有 hazard analysis 与 supplier verification 记录，鼓励现场纠正并把纠正措施同时记入 EIR 与 **CAR**；重大观察列 **Form FDA 483a / FSVP Observations**，其他观察也应讨论并记入 EIR（IOM 5.2.3）。
- `PART III.1.A.ii` **modified requirements 取证**：EIR 必须写明该 FSVPI 适用哪套要求，**即使企业声称 "No FSVP" 或未出示记录**；VSI / 小供应商情形若**完全没有**任何 modified requirement 记录（含资格证明），可引用「No FSVP」records under **§1.502(a)**；有任一 §1.512 记录即按 modified requirements 检查。§1.511(c) 膳食补充剂须先排除 1.511(a)/(b)（进口商或其客户为制造商）并考虑转 OP13。
- `PART III.1.C` 原文：**`Samples will not be collected as part of an FSVP inspection.`** ——与 CP 7303.050 的抽样程序截然不同；`PART IV – ANALYTICAL` 四节全部 `Intentionally Left Blank`。不得把 7303.050 的样品量/PAF 套到 FSVP 检查。
- `PART V.1.A` 最重大观察：未 develop/maintain/follow FSVP；未做书面危害分析或未记录对他方危害分析的审阅（尤其 SAHCODHA 危害未做相应供应商验证）；未做/未记录供应商批准评价；未做/未记录供应商验证活动；未履行 modified requirement 的 FSVP 活动（如 §1.507 disclosure statement、书面保证）；**FDA 书面要求后未及时以电子或其他方式提供 FSVP 记录**。较轻一档包括未记录供应商批准、未建立书面程序、未记录 FSVP 变更、未确保 §1.509 入境标识信息。
- `PART V.1.C` 执法裁量因素：违法史；是否涉 RTE 人食/宠物食品与零食/已知 SAHCODHA 风险的农产品（与暴发、召回、掺假或过敏原误标相关者**风险最高、优先执法**）；进口量；是否首次检查（**首次违法仅在已知食品安全风险时才优先执法**）；偏差是局限还是持续扩大；是否有持续自愿合规与渐进改善；是否与另一被执法 FSVPI 共用所有权/责任人、或换新商号继续进口。
- `PART V.1.D` 检查分类 **NAI / VAI / OAI**；OAI 的执法建议经 CMS 上报，分类依 SOP-001642。
- `PART V.2` Charges：不合规即违反 §805；**§801(a)(3) / §1.514(a) 拒绝入境**，指控措辞原文为 `The food article is subject to refusal of admission pursuant to section 801(a)(3) of the FD&C Act in that it appears that the importer (as defined in section 805 of the FD&C Act) is in violation of section 805 of the FD&C Act.`；无合规 FSVP 而进口另构成 **§301(zz)（21 U.S.C. 331(zz)）/ §1.514(b) 禁止行为**。另有 §302 禁令、§303 刑事、§306 debarment 与虚假陈述责任。
- ⚠ `PART V.Note` **反直觉限制**：FDA 明确 `does not view compliance with the disclosure requirement under 21 CFR 1.507 as a substitute for the information required under section 801(b) of the FD&C Act and 21 CFR 1.95 for reconditioning proposals`（例如对受污染食品加 kill step 的整改提案），详见 FSVP Guidance Q&A G.8。不得把 §1.507 disclosure 当作 §801(b)/§1.95 整改资料的替代。
- `PART V.3` **direct reference authority 只在有限情形授予**（HFP Enforcement Bulletin #13）；未覆盖的案件，WL / Untitled Letter / Import Alert 99-41 建议须经 CMS 送 HFP OCE OE Imports Enforcement Branch（动物食品送 CVM OSC DFC），且 OAI 及伴随 advisory action 的 VAI 均须与 Center 取得分类一致。
- `PART V.3.C` **Import Alert 99-41**（DWPE：进口商不符合 FSVP 时扣留人食/动物食品）：WL 后未纠正、无回复或回复不充分 → 可按「**具体食品 + 具体境外供应商组合**」或「全部食品」列入 Red List；**未上 Red List 的 FSVPI 仍可继续进口同一食品或同一被列供应商的其他食品**（前提是不受其他掺假/误标 Import Alert 约束）；移除须由 FSVPI 按 99-41 指示向原发函 Division 提交证据，Division 经 CMS 建议 OIO/DIO，并咨询 HFP OCE OE / CVM OSC DFC。注意与 CP 7303.070 的 **99-37 / 99-38**（LACF/AF 备案与过程控制）**不是同一个 Import Alert**。
- `PART II.5 / II.D` 协调：FDA **currently not assigning FSVP inspections to State and Local counterparts**；与外国主管机关的 **SRA**（Systems Recognition Arrangement）仅对「不再进一步加工/制造且在 SRA 范围内」的人类食品适用 §1.513 modified requirements；Import Divisions 与 OHFI 须协调避免同一设施/农场一年内重复检查（for-cause 除外），FY 初共享任务、每季度交换进度；rTAN 人类食品走 `FSVPrTAN@fda.hhs.gov`、动物食品走 CVM。

## 转换局限

- `pdf2md-pro` 自检：33 页 / 20 书签全部命中（bookmarks_dropped 0）、表格 93 行、残留独立页码 0、`- Page N` 0、H1–H4 共 50 个标题。
- 已清除每页重复的 `**Date of Issuance** : 08/28/2025` 与 `**Transmittal Number** : 2023-CPM-CFSAN-003` 页眉行共 62 行（含 4 行两字段并排），并折叠由此产生的连续空行；**个别跨页段落仍被切成两段**（例如 PART I.1 的 §1.502(a) 句），逐字引证须按「剥离 `<u>` 标签 + NFKC + 去非字母数字」归一化 squash 后核对，不要按 Markdown 行边界核对。
- 正文含 **92 处 `<u>…</u>`** 超链接/下划线标记（PDF 版面产物），引用时须剥离标签；书签标题与正文粗体小节同时被提升为标题，故 `PART II`、`PART VI` 各出现两次、部分小节层级交错（与 CP 7303.070 同型局限）。**检索以 PART / 小节号为准**。
- 目录页（Contents）与 Change History 表格保留；`Import Alert 9941` 为 PDF 转录连写（正文别处为 `99-41`），引用以 `99-41` 为准；`Op 13` / `OP13` 为同一作业代码的不同写法。
- 文件头为导入说明，非原文；转换报告中的 chars/lines 为加文件头与清页眉之前的数值。转换运行时出现过一次 Windows 子进程 stdout 的 `UnicodeDecodeError` 告警（pymupdf4llm 内部线程读控制台），不影响输出。

"""


def main() -> None:
    raw = SRC.read_text(encoding="utf-8")
    lines = raw.splitlines()
    kept, removed = [], []
    for line in lines:
        s = line.strip()
        if (s.startswith("**Transmittal Number**") or s.startswith("**Date of Issuance**")
                or re.fullmatch(r"(PROGRAM 7303\.878|COMPLIANCE PROGRAM MANUAL|FOOD AND DRUG ADMINISTRATION)", s)):
            removed.append(s)
            continue
        kept.append(line)
    out: list[str] = []
    for line in kept:
        if not line.strip() and out and not out[-1].strip():
            continue
        out.append(line)
    body = "\n".join(out).strip() + "\n"
    SRC.write_text(HEADER + body, encoding="utf-8")

    report = json.loads(REPORT.read_text(encoding="utf-8"))
    report["header_lines_removed"] = len(removed)
    report["header_removed_samples"] = sorted(set(removed))[:4]
    report["underline_tags"] = body.count("<u>")
    report["final_chars"] = len(HEADER) + len(body)
    report["final_lines"] = len((HEADER + body).splitlines())
    report["version_judgement"] = "2023-09-27 program (Transmittal 2023-CPM-CFSAN-003), corrected 2025-08-28; not a 2025 new program"
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"removed {len(removed)} header lines; underline tags {body.count('<u>')}; "
          f"final {report['final_chars']} chars / {report['final_lines']} lines")


if __name__ == "__main__":
    main()
