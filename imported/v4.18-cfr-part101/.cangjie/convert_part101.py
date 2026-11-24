#!/usr/bin/env python3
"""Convert the eCFR '21 CFR Part 101 (up to date as of 11-05-2026)' PDF to
searchable markdown for the cangjie-skill RIA-TV++ pipeline.

Design notes
------------
* The PDF is single-column HTML rendered by Prince 16.2, NOT the two-column
  GPO annual-edition layout handled by the legacy convert_cfr_part.py.
* Every page carries 4-5 fixed footer/header lines; those are dropped.
* Section headings are already present in the text layer as ``§ 101.x ...``
  lines, so no bookmark injection is needed (bookmarks are used only to
  verify coverage).
* Hard line breaks are preserved verbatim. Quote verification normalises
  whitespace, so no reflow is attempted (this avoids the reflow defects seen
  on the GPO two-column editions).
* IMPORTANT: Prince emits floating section headings EARLY in the content
  stream. Plain ``page.get_text()`` therefore puts e.g. the § 101.2 heading
  before § 101.1's paragraphs (a)(b)(c). We use ``get_text("blocks")``
  sorted by (y0, x0) to recover the true visual/CFR reading order.
* Table regions (notably § 101.12 Table 1 / Table 2, Appendices B-D) are
  stream-of-text in the text layer and are explicitly marked as NOT
  quotable verbatim in the file header.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pymupdf as fitz

SRC = Path(r"G:\下载\21 CFR Part 101 (up to date as of 11-05-2026).pdf")
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "source-cfr-part101-2026.md"
REPORT = ROOT / ".cangjie" / "part101-convert-report.json"

NOISE = [
    re.compile(r"^21 CFR Part 101 \(up to date as of .*\)$"),
    re.compile(r"^Food Labeling$"),
    re.compile(r"^21 CFR Part 101 \(Nov\..*$"),
    re.compile(r"^21 CFR 101\.\d+.*$"),
    re.compile(r"^page \d+ of \d+$"),
    re.compile(r"^This content is from the eCFR.*$"),
]

RE_PART = re.compile(r"^PART 101[—-]FOOD LABELING$")
RE_SUBPART = re.compile(r"^Subpart ([A-G])[—-]\s*(.+)$")
RE_SECTION = re.compile(r"^§ 101\.(\d+)\s+(.+)$")
RE_APPENDIX = re.compile(r"^Appendix ([A-D]) to Part 101[—-]\s*(.*)$")
RE_APPENDIX_RESERVED = re.compile(r"^Appendix ([A-D]) to Part 101 \[Reserved\]$")
# Subpart F's heading wraps onto a second line in the PDF text layer.
SUBPART_F_CONT = "Claims nor Health Claims"
RE_TABLE = re.compile(r"^TABLE \d+[—-]")

HEADER = """# 21 CFR Part 101 — Food Labeling (eCFR, up to date as of 11/05/2026)

> **来源**：`G:/下载/21 CFR Part 101 (up to date as of 11-05-2026).pdf`，eCFR 导出 PDF（Prince 16.2 生成，352 页 / 70 书签）。页脚自述 `This content is from the eCFR and is authoritative but unofficial`，即**权威但非官方正式文本**（正式文本为 GPO 年度编纂版 eCFR/GPO）。PDF 页眉版本标注 `21 CFR Part 101 (Nov. 5, 2026)`，是当前快照日期，**不是修订生效日、不是新规发布日**；条文末尾的 FR citation 才是修订出处。
>
> **效力层级**：**法规正文层**（联邦法规，具法律约束力）。在本技能包内为**第七套独立编号**〔§ 101.xxx〕，与〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕并列——各管各自义务，不是上下位、不是新旧替代。Part 101 管**标签（labeling）**，法源含 FD&C Act §403（misbranding）、§201(n)（labeling 定义）、§403(q)（营养标签）、§403(r)（声称）、NLEA / DSHEA / FALCPA / ACA §4205 等；Part 117 管**生产过程的危害分析与预防控制**。两者接口为「厂内控制（含过敏原标签控制这一预防控制）↔ 标签内容与形式的法定义务」，不得互引条款号替代。
>
> **关键口径**：① 引用写〔§ 101.xxx〕，不得写成〔§ 117.xxx〕或「21 CFR 101.x（指南）」；② 本件是 **2026-11-05 现行快照**，与 4-1-25 Edition 年度编纂版不同，涉及具体数值（RACC、DV、声称阈值）时须核对快照日期；③ `Subpart G` 的〔§ 101.100〕是**标签要求豁免**，与 Part 117 的 `qualified facility` 等**主体豁免**是两套完全不同制度；④ 本件不涵盖 FALCPA 的法定过敏原定义本身（在 FD&C Act §201(qq) / §403(w)，正文未收），也不涵盖 §101.9 引用的 §104.20 强化政策、21 CFR part 102 通用名、part 130 标准身份、part 107 婴儿配方等外部法源，一律标「转引未收」。
>
> **转换局限（不可逐字引用区）**：① 文件前 2 页为目录、已裁；第 3 页开头仍有目录续行残段、已裁至 `PART 101—FOOD LABELING`；另有 9 页（44 / 45 / 51 / 239 / 240 / 344 / 347 / 348 / 351）在文本层只剩页眉页脚，系 Nutrition Facts 图形示例页，正文为图片、不可引；② PDF 每行是硬换行，转换件**保留原始行界、不做重排**，引用时须归一化空白；③ **§ 101.12 的 Table 1 / Table 2（约 113 页）与 Appendix B/C/D 的 Nutrition Facts 图形在文本层是流式列值**，表头与脚注逐页重复、列可能错列，**只可引「产品类别 → RACC → label statement」对应关系，不得逐字引表格数值或版式**；④ 表格页脚注编号（1–13）逐页重复，属版式重复而非独立条文；⑤ 页眉当前条款号（如 `21 CFR 101.12(b) (enhanced display)`）已随页脚一并清除，不得当作条文出处；⑥ 上标/下标（如 `10⁵`、`ft²`、`µg`）在部分页丢失为普通数字，引用须还原并注明。
>
> **不可混引**：本件与 PCHF 行业指南、L.mono 草案、SECG、过敏原 Ed.5、Food Defect Levels Handbook、CPGM 7303.040、CP 7303.050 / 7303.070 / 7303.842 / 7303.847 / 7303.878、IOM 2026 Ch.4 / Ch.5 / Ch.6、21 CFR Part 108 / 113 / 114 / 117 / 120 / 123 合计**二十二类来源**，效力栈为：法规正文（七套编号）＞ FDA 指南（should 建议层）＞ CPGM／CP／IOM 检查程序（检查员视角、不创设企业义务）。

---

"""


def norm(s: str) -> str:
    """Collapse whitespace for title-continuation matching."""
    return " ".join(s.split())


def is_noise(line: str) -> bool:
    s = line.strip()
    if not s:
        return True
    return any(p.match(s) for p in NOISE)


def main() -> int:
    doc = fitz.open(SRC)
    toc = doc.get_toc()
    bookmark_sections = [t[1] for t in toc if t[1].startswith("§ 101.")]
    full_titles: dict[str, str] = {}
    for t in toc:
        if t[1].startswith("§ 101."):
            parts = t[1].split(" ", 2)
            if len(parts) == 3:
                full_titles[parts[1]] = parts[2].strip()

    out_lines: list[str] = []
    seen_sections: dict[str, int] = {}
    subparts: list[str] = []
    noise_removed = 0
    started = False
    pages_kept = 0
    blank_pages: list[int] = []

    for pno in range(doc.page_count):
        blocks = [b for b in doc[pno].get_text("blocks") if b[6] == 0]
        blocks.sort(key=lambda b: (round(b[1], 1), b[0]))
        raw: list[str] = []
        for blk in blocks:
            raw.extend(blk[4].splitlines())
        # Trim the two TOC pages and the TOC residue at the top of page 3.
        if not started:
            idx = next((i for i, ln in enumerate(raw) if RE_PART.match(ln.strip())), None)
            if idx is None:
                continue
            raw = raw[idx:]
            started = True

        kept: list[str] = []
        skip_next = False
        skip_before = -1
        for pos, ln in enumerate(raw):
            s = ln.strip()
            if pos < skip_before:
                continue
            if skip_next:
                skip_next = False
                continue
            if is_noise(ln):
                noise_removed += 1
                continue
            # Preserve original hard line breaks; only insert blank lines
            # around promoted headings for markdown readability.
            m_sec = RE_SECTION.match(s)
            if m_sec:
                num = "101." + m_sec.group(1)
                head = m_sec.group(2).strip()
                title = full_titles.get(num, head)
                remainder = title[len(head):].strip() if title.startswith(head) else ""
                skip_before = pos + 1
                if remainder:
                    acc = ""
                    k = pos + 1
                    while k < len(raw):
                        cand = raw[k].strip()
                        if not cand or is_noise(raw[k]):
                            break
                        nxt = (acc + " " + cand).strip() if acc else cand
                        if norm(remainder).startswith(norm(nxt)):
                            acc = nxt
                            k += 1
                            if norm(acc) == norm(remainder):
                                break
                        else:
                            break
                    if norm(acc) == norm(remainder):
                        skip_before = k
                seen_sections.setdefault(num, pno + 1)
                kept.append("")
                kept.append(f"### § {num} {title}")
                kept.append("")
                continue
            m_sub = RE_SUBPART.match(s)
            if m_sub:
                title = m_sub.group(2).strip()
                # Continuation line for the wrapped Subpart F heading.
                if m_sub.group(1) == "F" and pos + 1 < len(raw) \
                        and raw[pos + 1].strip() == SUBPART_F_CONT:
                    title += " " + SUBPART_F_CONT
                    skip_next = True
                subparts.append(f"Subpart {m_sub.group(1)} — {title}")
                kept.append("")
                kept.append(f"## Subpart {m_sub.group(1)} — {title}")
                kept.append("")
                continue
            m_app = RE_APPENDIX.match(s)
            if m_app:
                kept.append("")
                kept.append(f"## Appendix {m_app.group(1)} to Part 101 — {m_app.group(2).strip()}")
                kept.append("")
                continue
            m_res = RE_APPENDIX_RESERVED.match(s)
            if m_res:
                kept.append("")
                kept.append(f"## Appendix {m_res.group(1)} to Part 101 — [Reserved]")
                kept.append("")
                continue
            if RE_PART.match(s):
                kept.append("")
                kept.append("# PART 101 — FOOD LABELING")
                kept.append("")
                continue
            if RE_TABLE.match(s):
                kept.append("")
                kept.append(f"**{s}**  <!-- TABLE REGION: not quotable verbatim -->")
                kept.append("")
                continue
            kept.append(s.rstrip())
        if kept:
            out_lines.extend(kept)
            out_lines.append("")
            out_lines.append(f"<!-- pdf-page {pno + 1} -->")
            out_lines.append("")
            pages_kept += 1
        else:
            blank_pages.append(pno + 1)

    text = HEADER + "\n".join(out_lines).rstrip() + "\n"
    OUT.write_text(text, encoding="utf-8")

    # Self-check: every § bookmark title's number should appear as a heading.
    missing = []
    for title in bookmark_sections:
        num = title.split(" ")[1]
        if num not in seen_sections:
            missing.append(num)
    residual = []
    for pat in NOISE:
        residual += [ln for ln in text.splitlines() if pat.match(ln.strip())]

    report = {
        "source": str(SRC),
        "output": str(OUT),
        "pdf_pages": doc.page_count,
        "pages_kept": pages_kept,
        "bookmarks_total": len(toc),
        "bookmark_sections": len(bookmark_sections),
        "sections_found": len(seen_sections),
        "sections_missing": missing,
        "subparts_found": subparts,
        "noise_lines_removed": noise_removed,
        "noise_residual": len(residual),
        "blank_pages_text_layer": blank_pages,
        "output_bytes": OUT.stat().st_size,
        "output_lines": len(text.splitlines()),
        "first_section_pages": dict(list(seen_sections.items())[:5]),
        "last_section_pages": dict(list(seen_sections.items())[-5:]),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not missing and not residual else 1


if __name__ == "__main__":
    sys.exit(main())
