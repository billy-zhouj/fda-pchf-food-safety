"""convert_cp847.py — CP 7303.847 专用转换器（按字体/行距重建结构）

为什么不用 pdf2md-pro：它的书签注入在本件上把 7 个书签标题插进段落中间，且把书签
大纲整块前置、顺序错乱；本件版面很规整（固定 3 行页眉 + `— Page N` 页标记 +
全部加粗的标题 + 统一字号正文），按字体信息直接重建比事后修补更可靠。

规则：
- 页眉：读到含 `—  Page` 的页标记行为止全部跳过；另跳过封面 `FOOD AND DRUG
  ADMINISTRATION` 行。
- 标题：整行全部 span 加粗且字号 ≥ 11 → 标题候选；连续候选行**合并**为一条
  （GPO 常把「4. / Sampling – Finished Product」或多行 NOTE 拆成多条）。
- 定级：以 `PART ` 开头 → `##`；其余 → `###`；合并后若是长句（> 90 字符且含句号）
  则降级为 `**粗体段**`，避免把整段 NOTE 变成小节标题。
- 段落：相邻两行 y 间距 > 1.55 × 行高 → 断开。
- 列表：行首 `•` / `·` / `` `n.` `` → `- ` 或 `n.`；PAC 行（5 位码 + 2 空格 + 描述）
  → `- ` 列表项。
- 目录块（`Contents` 起至 `PART I` 前）整段丢弃——它是带页码的 TOC，与正文标题重复。
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pymupdf

PDF = Path("D:/周至/Downloads/20250922_CP 7303.847 Juice HACCP  508-Compliant.pdf")
OUT = Path(".cangjie/tmp-cp847.md")
REPORT = Path(".cangjie/tmp-cp847-report.json")

HDR_DROP = re.compile(
    r"^(FOOD AND DRUG ADMINISTRATION|COMPLIANCE PROGRAM GUIDANCE MANUAL|"
    r"PROGRAM\s+7303\.847|Date of Issuance:|Correction date:)\s*$"
)
PAGE_MARK = re.compile(r"—\s*Page\b")
H = "@@H@@ "


def main() -> int:
    doc = pymupdf.open(PDF)
    out: list[str] = []
    stats = {"pages": doc.page_count, "heading_lines": 0, "paras": 0, "dropped_header": 0}

    for page in doc:
        dd = page.get_text("dict")
        lines: list[dict] = []
        for b in dd["blocks"]:
            if b.get("type") != 0:
                continue
            for l in b["lines"]:
                txt = "".join(s["text"] for s in l["spans"]).strip()
                if not txt:
                    continue
                bold = all((s["flags"] & 16) for s in l["spans"] if s["text"].strip())
                size = max(s["size"] for s in l["spans"])
                lines.append({"t": txt, "b": bold, "s": size,
                              "y": l["bbox"][1], "h": l["bbox"][3] - l["bbox"][1]})
        start = 0
        for i, l in enumerate(lines):
            if PAGE_MARK.search(l["t"]):
                start = i + 1
                break
        stats["dropped_header"] += start
        body = lines[start:]
        while body and HDR_DROP.match(body[0]["t"]):
            stats["dropped_header"] += 1
            body.pop(0)

        para: list[str] = []
        prev = None

        def flush():
            nonlocal para
            if para:
                out.append(" ".join(para))
                out.append("")
                stats["paras"] += 1
                para = []

        def incomplete(prev_title: str, nxt: str) -> bool:
            """上一标题行是否明显没写完——只有这种情况才与下一行合并。

            印刷版把一条标题拆成多行的典型信号：极短（"4."/"A"/"2."）、
            以顿号/逗号收尾、以 and/or/the/of 等虚词收尾、或下一行小写起首。
            反之，Part IV 的粗体项目清单逐条都是完整标题，不得合并。
            """
            if len(prev_title) < 25:
                return True
            if prev_title.endswith(","):
                return True
            if re.search(r"\b(and|or|the|of|to|for|with|in|on|from)$", prev_title):
                return True
            if nxt[:1].islower():
                return True
            return False

        def push_head(title: str):
            # out 的末尾是上一标题后的空行，故要看倒数第二项
            prev_is_part = len(out) >= 2 and out[-2][len(H):].upper().startswith("PART ")
            if (len(out) >= 2 and out[-2].startswith(H) and not prev_is_part
                    and incomplete(out[-2][len(H):], title)):
                out[-2] = out[-2] + " " + title
            else:
                out.append(H + title)
                out.append("")

        for l in body:
            is_head = l["b"] and l["s"] >= 11 and len(l["t"]) <= 130
            if is_head:
                flush()
                push_head(l["t"].rstrip(":").strip())
                stats["heading_lines"] += 1
                prev = None
                continue
            if prev is not None and (l["y"] - prev["y"]) > 1.55 * max(prev["h"], 1):
                flush()
            m = re.match(r"^(\d{5}[A-Z]?)\s{2,}(\S.*)$", l["t"])
            if m:
                flush()
                out.append(f"- `{m.group(1)}` {m.group(2).strip()}")
                prev = None
                continue
            m = re.match(r"^[•·]\s*(.+)$", l["t"])
            if m:
                flush()
                out.append(f"- {m.group(1).strip()}")
                prev = None
                continue
            m = re.match(r"^`(\d+\.)`\s*(.*)$", l["t"])
            if m:
                flush()
                out.append(f"{m.group(1)} {m.group(2).strip()}")
                prev = None
                continue
            if re.fullmatch(r"\d{1,3}", l["t"]):
                # 孤立页码（页标记未覆盖到的情形）
                stats["dropped_header"] += 1
                prev = None
                continue
            para.append(l["t"])
            prev = l

        flush()

    # ── 后处理：定级 / 长句降级 / 丢目录块
    final: list[str] = []
    in_toc = False
    demoted = 0
    heads = 0
    for ln in out:
        if ln.startswith(H):
            title = ln[len(H):].strip()
            if re.match(r"^Contents", title, re.I):
                in_toc = True
                continue
            if in_toc and not title.upper().startswith("PART I"):
                continue
            in_toc = False
            is_sentence = (len(title) > 50 and title.endswith(".")) or \
                len(title) > 90 or title.startswith("NOTE") or " NOTE: " in title
            if is_sentence:
                final.append(f"**{title}**")
                final.append("")
                demoted += 1
            else:
                level = "##" if title.upper().startswith("PART ") else "###"
                final.append(f"{level} {title}")
                final.append("")
                heads += 1
            continue
        final.append(ln)

    # PART II 的「1. Objective」标题同样缺失（文本层无字），用书签补回
    idx_ii = vi.find("## PART II") if (vi := "\n".join(final)) else -1
    if idx_ii >= 0:
        head, tail = vi[:idx_ii], vi[idx_ii:]
        tail = tail.replace("### 1.\n", "### 1. Objective\n", 1)
        vi = head + tail

    # PART VI 的 1./2. 标题文字在文本层缺失（渲染为图形），用书签补回
    idx_vi = vi.find("## PART VI")
    if idx_vi >= 0:
        head, tail = vi[:idx_vi], vi[idx_vi:]
        tail = tail.replace("### 1.\n", "### 1. References\n", 1)
        tail = tail.replace("### 2.\n", "### 2. Attachments\n", 1)
        vi = head + tail
    text = vi

    # 多项目符号段落拆成列表项（pymupdf 会把并排的 • 合成一行）
    fixed: list[str] = []
    for ln in text.split("\n"):
        if (ln.count(" • ") >= 1 or ln.lstrip().startswith("• ")) and not ln.startswith("#"):
            parts = [x.strip(" •") for x in ln.split("•") if x.strip()]
            fixed.extend(f"- {x}" for x in parts)
            continue
        fixed.append(ln)
    text = "\n".join(fixed)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    OUT.write_text(text, encoding="utf-8")
    stats.update({"headings": heads, "demoted_to_bold": demoted,
                  "chars": len(text), "lines": text.count("\n") + 1})
    REPORT.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
