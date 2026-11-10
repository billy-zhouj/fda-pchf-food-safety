#!/usr/bin/env python3
"""能力卡路由正确性判分（官方评测器未覆盖，自建确定性判分）。

输入: routing-suite.json（含 expected_capability）+ results-routing/*.jsonl
输出: markdown 报告：top-1 命中率、重复一致性、逐例结果、混淆对、每卡被误选次数。
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

E = Path(__file__).resolve().parent / "v4-7-output-routing-eval"
suite = json.loads((E / "routing-suite.json").read_text(encoding="utf-8"))
truth = {c["case_id"]: c["expected_capability"] for c in suite["routing_cases"]}
cands = set(suite["candidate_capabilities"])

rows = []
for p in sorted((E / "results-routing").glob("*.jsonl")):
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
assert rows, "no routing results"

by_case = defaultdict(list)
bad_slug = []
for r in rows:
    cid, sel = r["case_id"], r.get("selected_capability", "")
    if sel not in cands:
        bad_slug.append((cid, sel))
    by_case[cid].append(sel)

hits = sum(1 for r in rows if r.get("selected_capability") == truth.get(r["case_id"]))
n = len(rows)
acc = hits / n if n else 0.0

per_case = []
for cid in sorted(truth):
    sels = by_case.get(cid, [])
    h = sum(1 for s in sels if s == truth[cid])
    per_case.append((cid, truth[cid], sels, h, len(sels)))

confusion = Counter()
mis_selected = Counter()
for r in rows:
    exp, sel = truth.get(r["case_id"]), r.get("selected_capability", "")
    if sel != exp:
        confusion[(exp, sel)] += 1
        mis_selected[sel] += 1

consistent = sum(1 for _, _, sels, _, _ in per_case if len(set(sels)) <= 1)

lines = [
    "# 能力卡路由正确性评测 — fda-pchf-food-safety v4.7",
    "",
    f"- 用例数 {len(truth)}（覆盖 20 张能力卡，每卡 1 条）",
    f"- 判分记录 {n} 条；每个用例重复 {n // len(truth) if len(truth) else 0} 次（不同干净 sub-agent）",
    f"- top-1 命中 {hits}/{n} = **{acc:.3f}**",
    f"- 重复判断一致的用例 {consistent}/{len(truth)}",
    f"- 非法 slug（不在候选清单）: {len(bad_slug)}",
    "",
    "## 逐例结果",
    "",
    "| case | expected | selected (按 run) | 命中 |",
    "|---|---|---|---|",
]
for cid, exp, sels, h, total in per_case:
    lines.append(f"| {cid} | `{exp}` | {' / '.join(f'`{s}`' for s in sels) or '—'} | {h}/{total} |")
lines += ["", "## 混淆对（expected → selected）", ""]
if confusion:
    lines += ["| 期望卡 | 误选卡 | 次数 |", "|---|---|---|"]
    for (exp, sel), k in confusion.most_common():
        lines.append(f"| `{exp}` | `{sel}` | {k} |")
else:
    lines.append("无错判。")
lines += ["", "## 被误选次数（按卡）", ""]
if mis_selected:
    lines += ["| 卡 | 次数 |", "|---|---|"]
    for s, k in mis_selected.most_common():
        lines.append(f"| `{s}` | {k} |")
else:
    lines.append("无。")
lines += [
    "",
    "> 本评测只测「给定 20 张卡候选时的 top-1 路由」，不测技能层是否触发，"
    "也不测答案内容质量（另见 output 评测报告）。judge 看到的是浓缩能力索引，不是完整卡片正文。",
    "",
]
report = "\n".join(lines)
out = E / "routing-eval-report.md"
out.write_text(report, encoding="utf-8")
print(report)
