#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把资料库导出的 SECG 在线文档（WorkBuddy block 标记）转换为可逐字核对的纯 Markdown 来源。

用法：python3 .cangjie/convert_secg.py <raw_txt> <out_md>
"""
import re
import sys
from pathlib import Path

raw = Path(sys.argv[1]).read_text(encoding="utf-8")
out = Path(sys.argv[2])

HEADER = """# What You Need to Know About the FDA Regulation: 21 CFR Part 117 — Small Entity Compliance Guide (Guidance for Industry)

> 本地来源文件 `source-secg.md`，由 WorkBuddy 资料库文档
> `FDA-SECG-21CFR117-Small-Entity-Compliance-Guide` 转换而来。
> 原件：U.S. Department of Health and Human Services / Food and Drug Administration /
> Center for Food Safety and Applied Nutrition，**October 2016**，Docket No. FDA-2011-N-0920，
> 依《Small Business Regulatory Enforcement Fairness Act》第 212 条编制。
> 文档性质：Guidance for Industry（非约束性，代表 FDA current thinking）。
>
> 转换说明：剥离在线文档的 block/mark 标记并合并换行，正文措辞与数值未改动。
> 原 PDF 分页表格在导入时出现两处已知错位——（1）XIII 章标题后紧接的若干项目符号实为 XII 章
> 低风险活动清单的尾部；（2）XIII.H「Defect Action Levels」的正文落在 XIV 章标题之后。
> 引用时以章节标题与条款号为准，不以邻接关系为准。
> 法定义务的最终依据仍是 21 CFR Part 117 法规正文（本地 `books/_inbox/21-CFR-Part-117-2025.md`）。

---

"""

TAG = re.compile(r"</?(?:Mark|Paragraph|BulletedList|Heading|Table|TableRow|TableCell|br|Mark)[^>]*>")
HEADING_OPEN = re.compile(r'<Heading[^>]*level="(\d+)"[^>]*>')


def clean(text: str) -> str:
    text = TAG.sub("", text)
    text = text.replace("\\", " ")
    text = text.replace("`o`", "-")
    text = text.replace("•", "-")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


lines = raw.splitlines()
result = []
i = 0
while i < len(lines):
    line = lines[i]
    m = HEADING_OPEN.match(line.strip())
    if m:
        level = min(int(m.group(1)), 4)
        buf = []
        i += 1
        while i < len(lines) and not lines[i].strip().startswith("</Heading"):
            buf.append(lines[i])
            i += 1
        title = clean(" ".join(buf))
        if title:
            result.append("#" * level + " " + title)
            result.append("")
        i += 1
        continue
    if re.match(r"<Table(?:\s|>)", line.strip()):
        # 表格：逐 TableRow 抽取 TableCell 内文本，输出 GFM 行
        rows, row, cell = [], [], []
        j = i
        while j < len(lines):
            l = lines[j].strip()
            if l.startswith("</Table>"):
                break
            if re.match(r"<TableRow(?:\s|>)", l):
                row, cell = [], []
            elif l.startswith("</TableRow>"):
                if cell:
                    row.append(clean(" ".join(cell)))
                    cell = []
                if row:
                    rows.append(row)
            elif re.match(r"<TableCell(?:\s|>)", l):
                cell = []
            elif l.startswith("</TableCell>"):
                if cell:
                    row.append(clean(" ".join(cell)))
                    cell = []
            elif not l.startswith(("<Paragraph", "</Paragraph>")) and l:
                cell.append(l)
            j += 1
        for k, r in enumerate(rows):
            r = [c.replace("|", "\\|") for c in r]
            result.append("| " + " | ".join(r) + " |")
            if k == 0:
                result.append("|" + "---|" * len(r))
        result.append("")
        i = j + 1
        continue
    if line.strip().startswith(("<Paragraph", "<BulletedList")):
        opener = "Paragraph" if "Paragraph" in line else "BulletedList"
        closer = "</" + opener + ">"
        buf = []
        i += 1
        while i < len(lines) and lines[i].strip() != closer:
            buf.append(lines[i])
            i += 1
        body = clean(" ".join(buf))
        if body:
            if opener == "BulletedList":
                result.append("- " + body)
            else:
                result.append(body)
            result.append("")
        i += 1
        continue
    i += 1

text = HEADER + "\n".join(result) + "\n"
text = re.sub(r"\n{3,}", "\n\n", text)
out.write_text(text, encoding="utf-8")
print(f"written: {out} | {len(text)} chars | headings={len(re.findall(r'^#{1,4} ', text, re.M))} | table_rows={text.count('| ---|')}")
