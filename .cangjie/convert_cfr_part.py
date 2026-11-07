"""convert_cfr_part.py — eCFR/GPO 双栏 CFR PDF → Markdown

与 pdf2md-pro 的差别：CFR 印刷版是双栏、无书签、有页眉页脚与页边页码，
pymupdf4llm 会把同一 y 坐标的左右栏并成一行（导致 §114.3(b) 定义串栏）。
本脚本按页按栏裁剪，重排为「页 → 左栏 → 右栏」，再按段落起点重组。

断词处理：印刷版行末连字符（proc- / essing）按原样保留，不做 dehyphenate，
避免把 low-acid foods 这类真实复合词误并成 low-acidfoods。逐字引文核对
使用 NFKC + 去除所有非字母数字的归一化，天然同时消除换行、空格与断词连字符。
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import fitz

LEFT = fitz.Rect(120, 170, 306, 712)
RIGHT = fitz.Rect(306, 170, 495, 712)

# 页眉 / 页脚 / 页码。页眉主体已被 clip 的 y0=170 排除，这里做兜底。
NOISE = [
    re.compile(r"^Food and Drug Administration, HHS\s*$"),
    re.compile(r"^21 CFR Ch\. I \(4[–-]1[–-]25 Edition\)\s*$"),
    re.compile(r"^Pt\.\s*\d+\s*$"),
    re.compile(r"^\d{2,4}\s*$"),
]

# 段落起点：命中则另起一行，否则接入上一段。
START = [
    re.compile(r"^§\s*\d+\.\d+"),
    re.compile(r"^PART\s+\d+"),
    re.compile(r"^Subpart[s]?\s+[A-Z]"),
    re.compile(r"^AUTHORITY:"),
    re.compile(r"^SOURCE:"),
    re.compile(r"^\[\d+\s+FR\b"),
    re.compile(r"^\([a-zA-Z0-9]{1,3}\)\s"),
    re.compile(r"^Sec\.\s*$"),
    # 目录条款号形如 "113.40 Equipment..."，须三位整数部分 + 大写标题词；
    # 否则会把正文里以 0.85 / 4.6 开头的续行误判成新段落。
    re.compile(r"^\d{3}\.\d+\s+[A-Z]"),
]

# ⚠ v4.13 修订：`^\d{2,4}$` 这条原本是兜底页码，但对数字密集的法规有害——
# Part 120 §120.25(c)(4)(i) 被 GPO 排成「juice / into / 90 / mL / of」，
# 独占一行的 "90" 会被当页码丢掉，产出 "into mL of"。页眉页脚已由 clip 的
# y0=170 排除，故该规则改为按需启用（--keep-standalone-numbers）。
NOISE_KEEP_NUMBERS = [p for p in NOISE if p.pattern != r"^\d{2,4}\s*$"]

SECTION = re.compile(r"^(§\s*\d+\.\d+)\s+(.*)$")


def extract_lines(pdf: Path) -> tuple[list[str], dict]:
    doc = fitz.open(pdf)
    raw: list[str] = []
    per_col = {"L": 0, "R": 0}
    hyphen_ends = 0
    for page in doc:
        for tag, clip in (("L", LEFT), ("R", RIGHT)):
            text = page.get_text("text", clip=clip)
            for line in text.splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                per_col[tag] += 1
                if re.search(r"[A-Za-z]{2}-$", stripped):
                    hyphen_ends += 1
                raw.append(stripped)
    meta = {
        "pages": doc.page_count,
        "lines_left": per_col["L"],
        "lines_right": per_col["R"],
        "hyphenated_line_ends_preserved": hyphen_ends,
        "metadata": {k: doc.metadata.get(k) for k in ("title", "author", "creationDate", "modDate") if doc.metadata.get(k)},
    }
    doc.close()
    return raw, meta


def start_patterns(part: str | None):
    """§ 条款起点只认目标 part 的条款号；跨 part 引用（如 § 114.90 of this
    chapter should be used.）必须保持为续行，否则会被误提升成条款标题。

    条号后若同行有标题词，须大写起首（CFR 条款标题一律首字母大写）；若条号
    独占一行（GPO 印刷版常见「§ 123.3 / Definitions.」两行式），也视为条款
    起点。仅排除「§ 123.7 whenever ...」这类正文小写续接的跨条引用。
    """
    num = re.escape(part) if part else r"\d+"
    sec = rf"^§\s*{num}\.\d+\s*(?:$|[A-Z(])"
    return [re.compile(sec)] + START[1:]


def drop_toc(raw: list[str]) -> tuple[list[str], dict]:
    """裁掉卷首的 Sec. 目录区。

    GPO 印刷版的 part 首页会先列出全 part 的条款目录：
        PART 123—FISH AND FISHERY PRODUCTS
        Subpart A—General Provisions
        Sec.
        123.3
        Definitions.
        ...
        Subpart B—Smoked and Smoke-Flavored Fishery Products
        123.15
        General.
        AUTHORITY: ...
    目录条目被 `^\\d{3}\\.\\d+\\s+[A-Z]` 与 Subpart 规则反复拼接，会产出
    `### Subpart B—... 123.15 General. 123.16 Process controls.` 这类残行。
    目录信息与正文条款标题重复，整体裁掉即可。
    """
    idx_sec = next((i for i, s in enumerate(raw) if re.fullmatch(r"Sec\.", s)), None)
    if idx_sec is None:
        return raw, {"toc_dropped": False}
    # 向前找最近的 PART 行（限 80 行内，避免误伤正文深处的 Sec.）
    idx_part = None
    for j in range(idx_sec, max(-1, idx_sec - 80), -1):
        if re.match(r"^PART\s+\d+", raw[j]):
            idx_part = j
            break
    # ⚠ v4.13 修订：多行 part 标题的续行正好落在目录区 [idx_part, idx_sec) 内，
    # 例如 PART 120 在印刷版是
    #   PART 120—HAZARD ANALYSIS AND / CRITICAL / CONTROL / POINT / (HACCP) SYSTEMS
    # 整段裁目录会把 CRITICAL…SYSTEMS 一起吞掉，产出的 H2 只剩前半句。
    # 先在裁切前把续行接回 PART 行（遇到 Subpart / Sec. 视为标题结束）。
    title_parts: list[str] = []
    k = idx_part + 1 if idx_part is not None else idx_sec
    while k < idx_sec and not re.match(r"^(Subpart|Sec\.)", raw[k]):
        title_parts.append(raw[k])
        k += 1
    if title_parts and idx_part is not None:
        raw = raw[:idx_part] + [raw[idx_part] + " " + " ".join(title_parts)] + raw[k:]
        idx_sec -= len(title_parts)
    # 向后找 AUTHORITY: / SOURCE:（必须在标题接回之后，否则索引会错位）
    idx_auth = None
    for j in range(idx_sec, min(len(raw), idx_sec + 200)):
        if re.match(r"^(AUTHORITY:|SOURCE:)", raw[j]):
            idx_auth = j
            break
    if idx_part is None or idx_auth is None:
        return raw, {"toc_dropped": False, "toc_reason": "part or authority anchor missing"}
    removed = idx_auth - idx_part - 1
    kept = raw[: idx_part + 1] + raw[idx_auth:]
    return kept, {
        "toc_dropped": True,
        "toc_start_index": idx_part,
        "toc_lines_removed": removed,
        "toc_entries_removed": sum(1 for s in raw[idx_part + 1 : idx_auth]
                                   if re.fullmatch(r"\d{3}\.\d+", s)),
    }


def compose(raw: list[str], part: str | None = None,
            keep_numbers: bool = False) -> tuple[list[str], int]:
    out: list[str] = []
    dropped = 0
    pats = start_patterns(part)
    noise = NOISE_KEEP_NUMBERS if keep_numbers else NOISE
    for s in raw:
        if any(p.match(s) for p in noise):
            dropped += 1
            continue
        is_start = any(p.match(s) for p in pats)
        if out and not is_start:
            out[-1] = out[-1] + " " + s
        else:
            out.append(s)
    return out, dropped


def trim_to_part(paragraphs: list[str], part: str) -> tuple[list[str], dict]:
    """eCFR/GPO 印刷版是连续页截取，首尾会带相邻 part 的残段，只保留目标 part。"""
    start = None
    end = len(paragraphs)
    for i, p in enumerate(paragraphs):
        m = re.match(r"^PART\s+(\d+)", p)
        if not m:
            continue
        if m.group(1) == part and start is None:
            start = i
        elif m.group(1) != part and start is not None and i > start:
            end = i
            break
    if start is None:
        return paragraphs, {"trim_start": 0, "trim_end": 0, "part_found": False}
    return paragraphs[start:end], {
        "trim_start": start,
        "trim_end": len(paragraphs) - end,
        "part_found": True,
    }


def render(paragraphs: list[str], title: str, part: str | None = None) -> tuple[str, dict]:
    sect = re.compile(rf"^(§\s*{re.escape(part)}\.\d+)\s+(.*)$") if part else SECTION
    body_split = re.compile(rf"^(§\s*{re.escape(part)}\.\d+)\s+(.*)$") if part else re.compile(r"^(§\s*\d+\.\d+)\s+(.*)$")
    lines = [f"# {title}", ""]
    sections = 0
    parts = 0
    split_bodies = 0
    for p in paragraphs:
        m = sect.match(p)
        if m:
            # 条款标题与正文首句常被拼成一行，在第一个句点处切开。
            mm = body_split.match(p)
            body = mm.group(2)
            t = re.match(r"(.+?\.)(\s+(.+))?$", body, re.S)
            if t:
                lines.append(f"## {mm.group(1)} {t.group(1)}")
                if t.group(3):
                    lines.append(t.group(3).strip())
                    split_bodies += 1
            else:
                lines.append(f"## {p}")
            sections += 1
        elif re.match(r"^PART\s+\d+", p):
            lines.append(f"## {p}")
            parts += 1
        elif re.match(r"^Subpart[s]?\s+[A-Z]", p):
            lines.append(f"### {p}")
        else:
            lines.append(p)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n", {
        "h2_sections": sections,
        "part_headings": parts,
        "section_bodies_split": split_bodies,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--part", help="目标 part 号，用于裁掉连续页截取带入的相邻 part 残段")
    ap.add_argument("--report")
    ap.add_argument("--keep-standalone-numbers", action="store_true",
                    help="保留独占一行的 2-4 位数字（数字密集法规必需，如 Part 120 的 90 mL）")
    args = ap.parse_args()

    src = Path(args.input)
    raw, meta = extract_lines(src)
    raw, toc = drop_toc(raw)
    paragraphs, dropped = compose(raw, args.part, args.keep_standalone_numbers)
    trim = {}
    if args.part:
        paragraphs, trim = trim_to_part(paragraphs, args.part)
    text, stats = render(paragraphs, args.title, args.part)
    dst = Path(args.output)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")

    report = {
        "input": str(src),
        "output": str(dst),
        "method": "page → left column → right column clip; paragraph recombination; hyphenated line breaks preserved",
        **meta,
        "toc": toc,
        "raw_lines": len(raw),
        "paragraphs_before_trim": len(raw) and len(paragraphs) + trim.get("trim_start", 0) + trim.get("trim_end", 0),
        "paragraphs_kept": len(paragraphs),
        "trim": trim or {"trim_start": 0, "trim_end": 0, "note": "no --part given, adjacent part fragments retained"},
        "noise_lines_dropped": dropped,
        "chars": len(text),
        "md_lines": text.count("\n") + 1,
        **stats,
        "residual_header_lines": sum(
            1 for l in text.splitlines()
            if "Food and Drug Administration, HHS" in l or "21 CFR Ch. I (4" in l
        ),
        "residual_standalone_pagenum": sum(
            1 for l in text.splitlines() if re.fullmatch(r"\s*\d{2,4}\s*", l)
        ),
    }
    if args.report:
        rp = Path(args.report)
        rp.parent.mkdir(parents=True, exist_ok=True)
        rp.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
