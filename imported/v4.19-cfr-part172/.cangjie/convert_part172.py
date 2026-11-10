#!/usr/bin/env python3
"""Convert the eCFR '21 CFR Part 172 (up to date as of 11-05-2026)' PDF to
searchable markdown for the cangjie-skill RIA-TV++ pipeline.

Why a separate converter from convert_part101.py
------------------------------------------------
Part 172's substance is TABLES ("food -> limitation ppm", "component ->
limitation"), plus a ~30-page flat list of flavouring substances (Sec. 172.515).
Block-level text extraction (used for Part 101) loses the column structure of
those tables because a table row is ONE block whose internal lines are
"Food | 50" splits. So this converter goes one level finer: it rebuilds each
visual line from word boxes, then splits the line into cells on horizontal
gaps > 20 pt (within-word gaps stay under 10 pt; real column gutters are 44+).

Detected table runs (>= 2 consecutive multi-cell lines) are emitted as GFM
tables and annotated as NOT quotable verbatim.

Other inherited defects from Prince 16.2 (same generator as Part 101):
* floating section headings get emitted early in the plain-text stream
  -> avoided entirely by rebuilding from word coordinates;
* footer block repeats 4-5 lines per page -> dropped;
* the first 4 pages are the eCFR table of contents -> dropped up to the
  'PART 172 - FOOD ADDITIVES ...' heading.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pymupdf as fitz

SRC = Path(r"G:\下载\21 CFR Part 172 (up to date as of 11-05-2026).pdf")
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "source-cfr-part172-2026.md"
REPORT = ROOT / ".cangjie" / "part172-convert-report.json"

GAP_CELL = 20.0      # horizontal gap that separates table cells
LINE_TOL = 3.0       # y tolerance when grouping words into one visual line
TOP_MARGIN = 55.0    # drop the running header
BOTTOM_MARGIN = 733.0  # drop the footer block

NOISE = [
    re.compile(r"^21 CFR Part 172 \(up to date as of .*\)$"),
    re.compile(r"^Food Additives Permitted for Direct Addition to Food for Human Consumption$"),
    re.compile(r"^21 CFR Part 172 \(Nov\..*$"),
    re.compile(r"^21 CFR 172\.\d+.*$"),
    re.compile(r"^page \d+ of \d+$"),
    re.compile(r"^This content is from the eCFR.*$"),
]

RE_PART = re.compile(r"^PART 172[—-]FOOD ADDITIVES PERMITTED FOR DIRECT ADDITION TO$")
RE_PART_CONT = "FOOD FOR HUMAN CONSUMPTION"
RE_SUBPART = re.compile(r"^Subpart ([A-I])[—-]\s*(.+)$")
RE_SECTION = re.compile(r"^§ 172\.(\d+)\s+(.+)$")
RE_HEADER_WORDS = re.compile(r"^(Food|Component|Limitations?|Substance|Use|Assay)\b", re.I)
# "(4) In lieu of ..." / "(c) To assure safe use ..." reopen prose inside a section.
RE_ENUM_START = re.compile(r"^\((?:[a-z]|\d{1,2}|[ivx]{1,5})\) \S")

HEADER = """# 21 CFR Part 172 — Food Additives Permitted for Direct Addition to Food for Human Consumption (eCFR, up to date as of 11/05/2026)

> **来源**：`G:/下载/21 CFR Part 172 (up to date as of 11-05-2026).pdf`，eCFR 导出 PDF（Prince 16.2 生成，178 页 / 198 书签 / 154 条款 / 9 Subpart）。页脚自述 `This content is from the eCFR and is authoritative but unofficial`，即**权威但非官方正式文本**（正式文本为 GPO 年度编纂版）。页眉版本标注 `21 CFR Part 172 (Nov. 5, 2026)`，是当前快照日期，**不是修订生效日、不是新规发布日**；条文末尾的 FR citation 才是修订出处。
>
> **效力层级**：**法规正文层**（联邦法规，具法律约束力）。本技能包内为**第八套独立编号**〔§ 172.xxx〕，与〔§ 101.xxx〕〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕并列——各管各自义务，不是上下位、不是新旧替代。Part 172 管**直接加入食品的添加剂：某物质能不能用、用在什么食品、用多少、须符合什么纯度规格**；法源为 FD&C Act §402(c) / §409（food additive）与 §201(s)（定义），本件条文依据 `21 U.S.C. 321, 341, 342, 348, 371, 379e`。
>
> **与相邻编号的分工（不得互引替代）**：① **Part 172 是「许可与限量」**，管某种直接添加剂在特定食品中的最大用量与纯度、以及「安全使用所必需」的标签/使用说明；② **Part 101 是「标签内容」**（第七套编号），管配料表怎么写、PDP/信息面板、营养标签、声称；③ **Part 117 是「过程预防控制」**，管危害分析与预防控制、过敏原控制；④ **Part 170/171/180 未收**：food additive petition 程序、间接添加剂（Part 175–178）与「一般公认安全/临时许可」在别处。添加剂「能用」不等于「用了就安全」——§172.5 明文要求 GMP 双重限制，且另有条款要求符合本 Act 其他规定。
>
> **转换局限（不可逐字引用区）**：① 文件前 4 页为 eCFR 目录、已裁至 `PART 172—FOOD ADDITIVES ...`；② 表格（`食品 → 限量 ppm` / `Component → Limitations`）在 PDF 文本层原本是流式列值，本转换器已按词级坐标重建成 GFM 表格，**但列边界为启发式推断（水平空隙 > 20 pt），跨页续表与 `Do.`（同上）行存在归属歧义；任何数值与限量一律回原 PDF 核对，不得逐字引用为本包结论**；③ **§ 172.515 合成香料清单（约 30 页、上千条物质名）为纯名录，不含用量条件**，只可引「某物质在/不在该清单」这一事实并注明须回原文核对拼写与收录状态；④ 每条末尾 `[42 FR 14491, ... ]` 为 Federal Register 编纂注记，属版式脚注、不是独立条文；⑤ 页眉当前条款号（如 `21 CFR 172.515(b) (enhanced display)`）已随页脚清除，不得当作条文出处；⑥ 上标/下标（如 `10⁵`、`°C`、`α-`）在部分页可能丢失或降级，引用须回原 PDF 还原。
>
> **不可混引**：本件与 PCHF 行业指南、L.mono 草案、SECG、过敏原 Ed.5、Food Defect Levels Handbook、CPGM 7303.040、CP 7303.050 / 7303.070 / 7303.842 / 7303.847 / 7303.878、IOM 2026 Ch.4 / Ch.5 / Ch.6、21 CFR Part 101 / 108 / 113 / 114 / 117 / 120 / 123 合计**二十三类来源**，效力栈为：法规正文（八套编号）＞ FDA 指南（should 建议层）＞ CPGM／CP／IOM 检查程序（检查员视角、不创设企业义务）。

---

"""


def norm(s: str) -> str:
    return " ".join(s.split())


def lines_from_words(page) -> list[list[dict]]:
    """Group word boxes into visual lines, each a list of word dicts sorted by x."""
    ws = [w for w in page.get_text("words") if TOP_MARGIN < w[1] and w[3] < BOTTOM_MARGIN]
    ws.sort(key=lambda w: (round(w[1], 1), w[0]))
    groups: list[list[tuple]] = []
    for w in ws:
        if groups and abs(w[1] - groups[-1][-1][1]) <= LINE_TOL:
            groups[-1].append(w)
        else:
            groups.append([w])
    out = []
    for g in groups:
        g.sort(key=lambda w: w[0])
        out.append([{"x0": w[0], "x1": w[2], "y0": w[1], "t": w[4]} for w in g])
    return out


def split_cells(words: list[dict]) -> tuple[list[str], bool]:
    """Split one visual line into cells on wide horizontal gaps.

    Returns (cells, has_gutter) where has_gutter records whether at least one
    gap exceeded GAP_CELL -- the only reliable signal that the line is a table
    row rather than ordinary running text that happens to contain numbers.
    """
    if not words:
        return [], False
    cells, cur = [], [words[0]]
    has_gutter = False
    for w in words[1:]:
        if w["x0"] - cur[-1]["x1"] > GAP_CELL:
            has_gutter = True
            cells.append(" ".join(x["t"] for x in cur))
            cur = [w]
        else:
            cur.append(w)
    cells.append(" ".join(x["t"] for x in cur))
    return [c.strip() for c in cells if c.strip()], has_gutter


def is_noise(line: str) -> bool:
    s = line.strip()
    if not s:
        return True
    return any(p.match(s) for p in NOISE)


def render_table(rows: list[list[str]], header: list[str] | None = None) -> list[str]:
    """Render reconstructed rows as a GFM table.

    ``header`` is supplied when the column captions were emitted by the PDF as
    a separate non-gutter line (e.g. "Food" / "Limitations ... parts per
    million" stacked above the first data row). Without it the first data row
    would be consumed as the markdown header, silently losing one limit value.
    """
    if not rows:
        return []
    width = max([len(r) for r in rows] + ([len(header)] if header else []))
    body = [r + [""] * (width - len(r)) for r in rows]
    out = ["<!-- TABLE REGION: reconstructed from word coordinates; not quotable verbatim -->", ""]
    if header:
        head = header + [""] * (width - len(header))
        out.append("| " + " | ".join(c.replace("|", "\\|") for c in head) + " |")
    else:
        out.append("| " + " | ".join(body[0]) + " |")
        body = body[1:]
    out.append("|" + "|".join(["---"] * width) + "|")
    for r in body:
        out.append("| " + " | ".join(c.replace("|", "\\|") for c in r) + " |")
    out.append("")
    return out


def main() -> int:
    doc = fitz.open(SRC)
    toc = doc.get_toc()
    bm_sections: list[str] = [t[1] for t in toc if t[1].startswith("§ 172.")]
    full_titles: dict[str, str] = {}
    for t in toc:
        if t[1].startswith("§ 172."):
            parts = t[1].split(" ", 2)
            if len(parts) == 3:
                full_titles["172." + parts[1].split(".")[1]] = parts[2].strip()

    out: list[str] = []
    seen: dict[str, int] = {}
    subparts: list[str] = []
    noise_removed = 0
    started = False
    pages_kept = 0
    blank_pages: list[int] = []
    table_blocks = 0

    for pno in range(doc.page_count):
        parsed = [split_cells(ln) for ln in lines_from_words(doc[pno])]
        parsed = [(c, g) for c, g in parsed if c]
        rows = [c for c, _ in parsed]
        gutters = [g for _, g in parsed]
        if not started:
            hit = next((i for i, r in enumerate(rows) if RE_PART.match(r[0])), None)
            if hit is None:
                continue
            rows, gutters = rows[hit:], gutters[hit:]
            started = True

        kept: list[str] = []
        pending_table: list[list[str]] = []
        table_header: list[str] | None = None
        # Column captions stack above the first data row as non-gutter lines
        # ("Food" then "Limitations ... parts per million"). Remember recent
        # prose lines so they can be lifted into the markdown header instead of
        # being consumed as a data row.
        recent_prose: list[int] = []       # indices into kept
        skip_until = 0
        i = 0

        def flush_table() -> None:
            nonlocal pending_table, table_header, table_blocks
            if not pending_table:
                table_header = None
                return
            # Only substantial runs are worth a GFM table. Isolated 1-2 row
            # fragments are usually the tail of a table broken by a page or an
            # enumerator; rendering them as tables would fabricate structure.
            if len(pending_table) >= 3 or (len(pending_table) >= 2 and table_header):
                kept.extend(render_table(pending_table, table_header))
                table_blocks += 1
            else:
                for r in pending_table:
                    kept.append(" | ".join(r))
            pending_table = []
            table_header = None

        while i < len(rows):
            cells = rows[i]
            if i < skip_until:
                i += 1
                continue
            joined = " ".join(cells)
            if is_noise(joined):
                noise_removed += 1
                i += 1
                continue

            # --- part heading (wraps onto a second line) ---
            if RE_PART.match(cells[0]):
                if i + 1 < len(rows) and norm(" ".join(rows[i + 1])) == RE_PART_CONT:
                    skip_until = i + 2
                kept += ["", "# PART 172 — FOOD ADDITIVES PERMITTED FOR DIRECT ADDITION TO FOOD FOR HUMAN CONSUMPTION", ""]
                i += 1
                continue

            # --- subpart heading ---
            m_sub = RE_SUBPART.match(cells[0])
            if m_sub:
                flush_table()
                recent_prose = []
                subparts.append(f"Subpart {m_sub.group(1)} — {m_sub.group(2).strip()}")
                kept += ["", f"## Subpart {m_sub.group(1)} — {m_sub.group(2).strip()}", ""]
                i += 1
                continue

            # --- section heading (title may wrap over following visual lines) ---
            m_sec = RE_SECTION.match(cells[0])
            if m_sec:
                num = "172." + m_sec.group(1)
                head = m_sec.group(2).strip()
                title = full_titles.get(num, head)
                remainder = title[len(head):].strip() if title.startswith(head) else ""
                if remainder:
                    acc = ""
                    k = i + 1
                    while k < len(rows):
                        cand = " ".join(rows[k]).strip()
                        if not cand or is_noise(cand):
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
                        skip_until = k
                flush_table()
                recent_prose = []
                seen.setdefault(num, pno + 1)
                kept += ["", f"### § {num} {title}", ""]
                i += 1
                continue

            # --- table row detection: a real column gutter plus row shape ---
            is_row = gutters[i] and len(cells) >= 2 and (
                RE_HEADER_WORDS.match(cells[0]) is not None
                or cells[-1].startswith("Do.")
                or re.match(r"^[\d,.\s]+$", cells[-1]) is not None
                or len(cells) >= 3
            )

            if is_row:
                if not pending_table and recent_prose:
                    # Lift the stacked captions that sit immediately above the
                    # first data row (at most 3) into the markdown header.
                    take = [k for k in recent_prose if kept[k].strip()
                            and not kept[k].startswith("<!--")
                            and RE_HEADER_WORDS.match(kept[k].strip()) is not None
                            or re.match(r"^parts per million$", kept[k].strip()) is not None]
                    take.sort()
                    if take:
                        caps = [kept[k].strip() for k in take]
                        # The PDF stacks the right-hand caption one line above
                        # the left-hand one; restore left-to-right order. A
                        # caption is "wide" when it ends in a connector word,
                        # which also identifies where a wrapped fragment goes.
                        caps.sort(key=len, reverse=True)
                        if len(caps) == 2 and len(caps[0]) >= len(caps[1]):
                            pass  # already widest-first == stacked order
                        conn = re.compile(r"\b(per|of|and|or|to|in|the|for)$", re.I)
                        tail_probe = 1
                        while take[-1] + tail_probe < len(kept):
                            frag = kept[take[-1] + tail_probe].strip()
                            if not frag or len(frag) > 12 or not frag.islower():
                                break
                            target = next((n for n, c in enumerate(caps)
                                           if conn.search(c)), None)
                            if target is None:
                                break
                            caps[target] = f"{caps[target]} {frag}"
                            kept.pop(take[-1] + tail_probe)
                        # Left-to-right = short caption first.
                        caps.sort(key=len)
                        table_header = caps
                        for k in reversed(take):
                            kept.pop(k)
                    recent_prose = []
                pending_table.append(cells)
                i += 1
                continue

            # A line that opens a new enumerated paragraph always terminates
            # the running table (the tables are per-paragraph, per-section).
            if pending_table and RE_ENUM_START.match(joined):
                flush_table()

            # A one-cell line with no gutter inside a table run is a wrapped
            # continuation of the previous row's first column (e.g. "mixes").
            if pending_table and len(cells) == 1 and not gutters[i] \
                    and RE_HEADER_WORDS.match(cells[0]) is None \
                    and re.match(r"^\d+\s+[A-Z]", joined) is None \
                    and not joined.rstrip().endswith(":"):
                pending_table[-1][0] = (pending_table[-1][0] + " " + joined).strip()
                i += 1
                continue

            flush_table()
            recent_prose = (recent_prose + [len(kept)])[-3:]
            kept.append(joined)
            i += 1

        if pending_table:
            if len(pending_table) >= 2:
                kept += render_table(pending_table); table_blocks += 1
            else:
                for r in pending_table:
                    kept.append(" | ".join(r))

        if kept:
            out.extend(kept)
            out += ["", f"<!-- pdf-page {pno + 1} -->", ""]
            pages_kept += 1
        else:
            blank_pages.append(pno + 1)

    text = HEADER + "\n".join(out).rstrip() + "\n"
    OUT.write_text(text, encoding="utf-8")

    missing = [t.split(" ")[1] for t in bm_sections
               if "172." + t.split(" ")[1].split(".")[1] not in seen]
    residual = [ln for ln in text.splitlines()
                if any(p.match(ln.strip()) for p in NOISE)]

    report = {
        "source": str(SRC),
        "output": str(OUT),
        "pdf_pages": doc.page_count,
        "pages_kept": pages_kept,
        "bookmarks_total": len(toc),
        "bookmark_sections": len(bm_sections),
        "sections_found": len(seen),
        "sections_missing": missing,
        "subparts_found": subparts,
        "tables_reconstructed": table_blocks,
        "noise_lines_removed": noise_removed,
        "noise_residual": len(residual),
        "blank_pages_text_layer": blank_pages,
        "output_bytes": OUT.stat().st_size,
        "output_lines": len(text.splitlines()),
        "first_section_pages": dict(list(seen.items())[:5]),
        "last_section_pages": dict(list(seen.items())[-5:]),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not missing and not residual else 1


if __name__ == "__main__":
    sys.exit(main())