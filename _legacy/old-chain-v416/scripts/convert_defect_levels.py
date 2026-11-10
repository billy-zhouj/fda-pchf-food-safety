# -*- coding: utf-8 -*-
"""把 FDA《Food Defect Levels Handbook》网页存档（.mhtml）正文转成 Markdown。

用法:
    python convert_defect_levels.py <input.mhtml> <output.md>

说明:
- 只取正文（从页面副标题 h2 到 "Related Information" h3 之前），丢弃导航/页脚/反馈表单。
- 保留英文原文逐字，便于后续引用块核对。
- 商品表含 rowspan / colspan，GFM 表格不支持，这里做展开：
  rowspan 的产品名向下重复；"DEFECT SOURCE / SIGNIFICANCE" 说明行单独成行。
"""
from __future__ import annotations

import html as html_lib
import re
import sys
from email import policy
from email.parser import BytesParser
from html.parser import HTMLParser
from pathlib import Path


class BlockParser(HTMLParser):
    BLOCK = {'p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr', 'table',
             'hr', 'ul', 'ol', 'blockquote', 'thead', 'tbody', 'br'}
    SKIP = {'script', 'style', 'noscript'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.cur: list[str] = []
        self.tag_stack: list[str] = []
        self.skip_depth = 0
        self.list_depth = 0
        self.table_mode = False
        self.tables: list[list[list[dict]]] = []
        self.rows: list[list[dict]] = []
        self.cells: list[dict] | None = None
        self.cell_buf: list[str] | None = None
        self.cell_tag: str | None = None
        self.emphasis: list[str] = []
        self.heading: str | None = None

    # ---------- helpers ----------
    def flush_text(self):
        if self.cur:
            txt = ''.join(self.cur)
            txt = re.sub(r'[ \t\r\n]+', ' ', txt).strip()
            if txt:
                self.out.append(txt)
            self.cur = []

    def emit(self, line: str = ''):
        self.flush_text()
        self.out.append(line)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.SKIP:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        self.tag_stack.append(tag)

        if tag == 'br':
            self.cur.append('<br>' if self.table_mode else ' ')
            return
        if tag in ('em', 'i'):
            self.cur.append('*')
            self.emphasis.append('*')
            return
        if tag in ('strong', 'b'):
            self.cur.append('**')
            self.emphasis.append('**')
            return

        if tag == 'table':
            self.emit()
            self.table_mode = True
            self.tables.append([])
            return
        if tag == 'tr' and self.table_mode:
            self.cells = []
            return
        if tag in ('td', 'th') and self.table_mode and self.cells is not None:
            self.cell_buf = []
            self.cell_tag = tag
            self.cell_rowspan = int(a.get('rowspan', 1) or 1)
            self.cell_colspan = int(a.get('colspan', 1) or 1)
            return

        if re.fullmatch(r'h[1-6]', tag):
            self.emit()
            self.heading = tag
            return
        if tag == 'p':
            if not self.table_mode:
                self.emit()
            return
        if tag in ('ul', 'ol'):
            self.emit()
            self.list_depth += 1
            return
        if tag == 'li':
            self.emit()
            self.cur.append('- ')
            return
        if tag == 'hr':
            self.emit('---')
            return
        if tag == 'a':
            # 锚点 / 外链只保留文字
            return

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if self.tag_stack and tag in self.tag_stack:
            while self.tag_stack:
                t = self.tag_stack.pop()
                if t == tag:
                    break
        if tag in ('em', 'i', 'strong', 'b') and self.emphasis:
            self.cur.append(self.emphasis.pop())
            return

        if tag in ('td', 'th') and self.table_mode and self.cell_buf is not None:
            txt = ''.join(self.cell_buf)
            txt = re.sub(r'[ \t\r\n]+', ' ', txt).strip()
            txt = re.sub(r'(<br>\s*)+', '<br>', txt).strip()
            txt = txt.replace('|', r'\|')
            self.cells.append({'text': txt, 'rowspan': self.cell_rowspan,
                               'colspan': self.cell_colspan, 'tag': self.cell_tag,
                               'pending': [txt]})
            self.cell_buf = None
            return
        if tag == 'tr' and self.table_mode and self.cells is not None:
            if self.cells:
                self.rows.append(self.cells)
            self.cells = None
            return
        if tag == 'table' and self.table_mode:
            self.tables[-1] = self.rows
            self.rows = []
            self.table_mode = False
            self.emit()
            return
        if re.fullmatch(r'h[1-6]', tag):
            self.flush_text()
            if self.out and self.out[-1]:
                level = {'h1': '#', 'h2': '##', 'h3': '###', 'h4': '####',
                         'h5': '#####', 'h6': '######'}[tag]
                # 去掉标题里的锚点残留文字
                self.out[-1] = f'{level} {self.out[-1]}'
            self.out.append('')
            self.heading = None
            return
        if tag == 'p' and not self.table_mode:
            self.emit()
            return
        if tag == 'li':
            self.emit()
            return
        if tag in ('ul', 'ol'):
            self.emit()
            self.list_depth = max(0, self.list_depth - 1)
            return

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.cell_buf is not None:
            self.cell_buf.append(data)
        else:
            self.cur.append(data)

    def result_text(self) -> str:
        self.flush_text()
        lines = [re.sub(r'[ \t]+', ' ', x).strip() for x in self.out]
        cleaned = []
        for line in lines:
            if line == '' and cleaned and cleaned[-1] == '':
                continue
            cleaned.append(line)
        return '\n'.join(cleaned).strip() + '\n'


def render_table(rows: list[list[dict]]) -> str:
    """展开 rowspan / colspan，输出 GFM 表格。"""
    if not rows:
        return ''
    grid: dict[tuple[int, int], str] = {}
    nrows = len(rows)
    for r, cells in enumerate(rows):
        c = 0
        for cell in cells:
            while (r, c) in grid:
                c += 1
            rs, cs = cell['rowspan'], cell['colspan']
            text = cell['text']
            for dr in range(rs):
                for dc in range(cs):
                    if dr == 0 and dc == 0:
                        grid[(r + dr, c + dc)] = text
                    elif dc == 0 and rs > 1:
                        # rowspan 的产品名向下重复，避免空Cell造成歧义
                        grid[(r + dr, c + dc)] = text
                    else:
                        grid.setdefault((r + dr, c + dc), '')
            c += cs
    width = max((c for _, c in grid), default=0) + 1
    out_rows: list[list[str]] = []
    for r in range(nrows):
        out_rows.append([grid.get((r, c), '') for c in range(width)])
    # 列数以表头为准（原表 3 列；多余的列是嵌套表造成的解析噪声）
    ncols = max(3, len([v for v in out_rows[0] if v]))
    # 说明行（DEFECT SOURCE / SIGNIFICANCE）原本 colspan=2 落在第 2 列，
    # 移到 ACTION LEVEL 列，避免与缺陷/方法列混淆。
    for row in out_rows[1:]:
        if len(row) >= 3 and re.match(r'\s*DEFECT SOURCE', row[1], re.I):
            row[2] = row[1]
            row[1] = '—'
    head = (out_rows[0] + [''] * ncols)[:ncols]
    lines = ['| ' + ' | '.join(head) + ' |',
             '|' + '|'.join(['---'] * ncols) + '|']
    for row in out_rows[1:]:
        lines.append('| ' + ' | '.join((row + [''] * ncols)[:ncols]) + ' |')
    return '\n'.join(lines) + '\n'


def main():
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    msg = BytesParser(policy=policy.default).parsebytes(src.read_bytes())
    page = ''
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            s = part.get_payload(decode=True).decode('utf-8', 'replace')
            if len(s) > len(page):
                page = s

    m_start = next((m for m in re.finditer(r'<h2[^>]*>', page)
                    if 'Levels of natural or unavoidable defects'
                    in page[m.end():m.end() + 200]), None)
    assert m_start, 'cannot find subtitle h2'
    start = m_start.start()
    m_end = re.search(r'<h3[^>]*>\s*Related Information\s*</h3>', page[start:])
    assert m_end, 'cannot find Related Information h3'
    end = start + m_end.start()
    assert start > 0 and end > start, f'bad slice {start} {end}'
    body = page[start:end]

    # 商品表内嵌了一张「树坚果容许百分比表」，GFM 无法嵌套表格，
    # 把它摘出单独成节，原位留交叉引用，避免外层表格被提前闭合。
    nested_html: list[str] = []
    while True:
        starts = [mm.start() for mm in re.finditer(r'<table\b', body)]
        if len(starts) < 2:
            break
        s2 = starts[1]
        e2 = body.find('</table>', s2)
        assert e2 > s2, 'malformed nested table'
        nested_html.append(body[s2:e2 + 8])
        body = (body[:s2] + '（树坚果容许百分比表见本节末）' + body[e2 + 8:])

    # 正文中表格位置写成占位符，再把渲染好的 GFM 表格插回原位
    class MarkerParser(BlockParser):
        def __init__(self):
            super().__init__()
            self.n = 0

        def handle_starttag(self, tag, attrs):
            if tag == 'table':
                self.emit(f'<<<TABLE:{self.n}>>>')
                self.n += 1
            super().handle_starttag(tag, attrs)

    m = MarkerParser()
    m.feed(body)
    text = m.result_text()

    tables_md = [render_table(t) for t in m.tables]
    nested_md = []
    for h in nested_html:
        np_ = BlockParser()
        np_.feed(h)
        if np_.tables:
            nested_md.append(render_table(np_.tables[0]))

    def sub(mo):
        i = int(mo.group(1))
        return tables_md[i].strip() if i < len(tables_md) else ''

    text = re.sub(r'<<<TABLE:(\d+)>>>', sub, text)
    if nested_md:
        text += ('\n\n#### 树坚果容许百分比表（原网页嵌于商品表内，'
                 '此处拆为独立表格）\n\n' + '\n'.join(nested_md))

    # 网页在商品表后用大量空 <br> 填充版面；整行只剩 <br>/*/空格的删掉
    def is_layout_noise(line: str) -> bool:
        if not line.strip():
            return False
        return re.sub(r'<br>|\*|\s', '', line) == ''

    text = '\n'.join(x for x in text.split('\n') if not is_layout_noise(x))
    # 网页脚注里的字面 ** 会被 Markdown 吃成粗体起始，转义之
    text = text.replace('**February 2005', r'\*\*February 2005')
    text = re.sub(r'\n{3,}', '\n\n', text)

    header = '''# Food Defect Levels Handbook（FDA 食品缺陷行动水平手册）

> **来源**：FDA 官网页面存档 `Food Defect Levels Handbook _ FDA.mhtml`（用户于 2026-11-05 提供，Blink 单页 MHTML）。
> 原始 URL：https://www.fda.gov/food/current-good-manufacturing-practices-cgmps-food-and-dietary-supplements/food-defect-levels-handbook
> 页面标注 **Content current as of: 09/07/2018**；正文末尾版本行：May 1995; Revised March 1997 and May 1998; February 2005 两处来源更正（MPM-V92→MPM-V32、955.46→965.41）。
> 由 `.cangjie/convert_defect_levels.py` 从 MHTML 正文转出，保留英文原文以便逐字引证。

## 效力层级与使用边界（导入说明，非原文）

- 本文是 **FDA 汇编的 defect action levels 一览 + 术语表**，用于 FDA 决定是否建议执法，属**执法裁量参考**，不是法规条文，也不是 guidance 意义上的「建议层」。§ 117.3 定义：defect action level 是 FDA **may regard** 食品 `"adulterated"` 并据 FD&C Act § 402(a)(3) 采取行动的水平。
- **现行法定义务在 21 CFR Part 117 Subpart B**：〔§ 117.110(a)〕要求 `must at all times utilize quality control operations that reduce natural or unavoidable defects to the lowest level currently feasible`；〔§ 117.110(b)〕禁止把掺假批与另一批混合稀释；〔§ 117.80(b)(4)〕要求易受害虫/异物污染的原料与返工品符合天然或不可避免缺陷的 FDA 规定。
- **⚠ 网页 INTRODUCTION 首句仍写 "21 CFR Part 110.110"，该引用已过时**：Part 110 依 2015-09-17 最终规则（80 FR 56144）于 **2018-09-17 被移除**，现代 CGMP 为 Part 117。本包引用一律用〔§ 117.110〕，不得照抄 110.110；SECG XIII.H 也是按 117.110 讲的。
- 手册中 "Poor manufacturing practices may result in enforcement action without regard to the action level" 是旧 § 110.110(c) 的意译；现行法源是 FD&C Act § 402(a)(4)（不卫生条件）＋ Part 117 Subpart B，**§ 117.110 本身只有 (a)(b) 两款**，不要把手册白话当作法条原文。
- 措辞差异：手册说混合「at or above the current defect action level」不合法，〔§ 117.110(b)〕写的是「at levels that render that food adulterated」——**以法规措辞为准**，前者是简化转述。
- **action level 不是合规安全港、不是平均值、也不是目标值**：手册明说 `The defect levels do not represent an average ... the averages are actually much lower`；低于 action level 不免除〔§ 117.110(a)〕的 "lowest level currently feasible" 义务，也不免除 402(a)(4) 卫生义务。技术上可行时可随技术进步修订，修订以 Federal Register Notices 发布。

## 转换局限

- 商品表含 rowspan（产品名跨行）与 colspan（DEFECT SOURCE / SIGNIFICANCE 说明行）：rowspan 已向下展开重复产品名；说明行从「缺陷/方法」列移到「ACTION LEVEL」列，原「缺陷/方法」列置 `—`。
- 原网页有一张表格嵌套在商品表内（坚果 Unshelled %/Shelled %），已拆为文末独立小节，原位留交叉引用。
- 链接只保留锚文本（AOAC / MPM 方法编号保留）；`<br>` 压为空格；图片、导航、页脚、反馈表单已剔除。
- GLOSSARY 术语按原字母顺序保留为加粗词条 + 释义；检索以英文术语或章节名（INTRODUCTION / GLOSSARY / COMMODITIES AND DEFECT ACTION LEVELS）为准。

---

'''
    dst.write_text(header + text, encoding='utf-8')
    print(f'OK {dst}  chars={len(header + text)}  main_tables={len(tables_md)}  '
          f'nested_tables={len(nested_md)}  '
          f'headings={len(re.findall(r"^#{1,6} ", header + text, re.M))}')


if __name__ == '__main__':
    main()
