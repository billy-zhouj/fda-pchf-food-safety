#!/usr/bin/env python3
"""v4.11 能力卡路由判分（沿用 v4.10 / v4.7 口径，增加 CAP-24 专项与三层混淆矩阵）。

输入: v4-11-eval/routing-suite.json + results-routing/run*.jsonl
输出: v4-11-eval/routing-eval-report.md
统计: top-1 命中、重复一致性、非法 slug、混淆对、每卡命中、CAP-24 定向命中、
      CAP-22 / CAP-23 / CAP-24 三层交叉错判。
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

E = Path(__file__).resolve().parent / "v4-11-eval"
suite = json.loads((E / "routing-suite.json").read_text(encoding="utf-8"))
truth = {c["case_id"]: c["expected_capability"] for c in suite["routing_cases"]}
cap_of = {c["case_id"]: c["capability_id"] for c in suite["routing_cases"]}
cands = set(suite["candidate_capabilities"])
SLUG24 = "seafood-inspection-program"
SLUG23 = "seafood-hazards-controls-guide"
SLUG22 = "seafood-haccp-statutory-requirements"

rows = []
for p in sorted((E / "results-routing").glob("run*.jsonl")):
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
assert rows, "no routing results"

by_case = defaultdict(list)
bad_slug = []
for r in rows:
    by_case[r["case_id"]].append(r.get("selected_capability", ""))
    if r.get("selected_capability", "") not in cands:
        bad_slug.append((r["case_id"], r.get("selected_capability", "")))

hits = sum(1 for r in rows if r.get("selected_capability") == truth.get(r["case_id"]))
n = len(rows)
acc = hits / n if n else 0.0
consistent = sum(1 for cid, sels in by_case.items() if len(set(sels)) <= 1)

confusion = Counter()
mis_selected = Counter()
for r in rows:
    exp, sel = truth.get(r["case_id"]), r.get("selected_capability", "")
    if sel != exp:
        confusion[(exp, sel)] += 1
        mis_selected[sel] += 1

per_cap = defaultdict(lambda: [0, 0])
for r in rows:
    cid = r["case_id"]
    per_cap[cap_of[cid]][1] += 1
    if r.get("selected_capability") == truth.get(cid):
        per_cap[cap_of[cid]][0] += 1

focus = {}
for cap in ("CAP-24", "CAP-23", "CAP-22"):
    ids = [cid for cid, c in cap_of.items() if c == cap]
    focus[cap] = (sum(1 for r in rows if r["case_id"] in ids and r.get("selected_capability") == truth[r["case_id"]]),
                  sum(1 for r in rows if r["case_id"] in ids))

c24 = [cid for cid, c in cap_of.items() if c == "CAP-24"]
c23 = [cid for cid, c in cap_of.items() if c == "CAP-23"]
c22 = [cid for cid, c in cap_of.items() if c == "CAP-22"]
cross = {
    "CAP-24 题 → CAP-23": sum(1 for r in rows if r["case_id"] in c24 and r.get("selected_capability") == SLUG23),
    "CAP-24 题 → CAP-22": sum(1 for r in rows if r["case_id"] in c24 and r.get("selected_capability") == SLUG22),
    "CAP-23 题 → CAP-24": sum(1 for r in rows if r["case_id"] in c23 and r.get("selected_capability") == SLUG24),
    "CAP-22 题 → CAP-24": sum(1 for r in rows if r["case_id"] in c22 and r.get("selected_capability") == SLUG24),
    "CAP-23 题 → CAP-22": sum(1 for r in rows if r["case_id"] in c23 and r.get("selected_capability") == SLUG22),
    "CAP-22 题 → CAP-23": sum(1 for r in rows if r["case_id"] in c22 and r.get("selected_capability") == SLUG23),
}
runs = n // len(truth) if truth else 0

lines = [
    "# 能力卡路由正确性评测 — fda-pchf-food-safety v4.11",
    "",
    f"- 用例数 {len(truth)}（24 张卡各 1 条 + CAP-24 定向 7 条 + CAP-23 定向 3 条 + CAP-22 定向 3 条）",
    f"- 判分记录 {n} 条；每个用例重复 {runs} 次（3 个干净 sub-agent）",
    f"- top-1 命中 {hits}/{n} = **{acc:.3f}**",
    f"- 重复判断一致的用例 {consistent}/{len(truth)}",
    f"- 非法 slug（不在候选清单）: {len(bad_slug)}",
    "",
    "## CAP-24 专项（v4.11 新增项）",
    "",
    f"- CAP-24 定向/基础用例 {len(c24)} 条 × {runs} 轮 = {focus['CAP-24'][1]} 判，命中 **{focus['CAP-24'][0]}/{focus['CAP-24'][1]}**",
    f"- CAP-23 用例命中 **{focus['CAP-23'][0]}/{focus['CAP-23'][1]}**；CAP-22 用例命中 **{focus['CAP-22'][0]}/{focus['CAP-22'][1]}**",
    "",
    "## 三层配对交叉错判",
    "",
    "| 方向 | 次数 |", "|---|---|",
]
for k, v in cross.items():
    lines.append(f"| {k} | {v} |")

lines += ["", "## 逐例结果", "",
          "| case | cap | expected | selected (按 run) | 命中 |", "|---|---|---|---|---|"]
for cid in sorted(truth):
    sels = by_case.get(cid, [])
    h = sum(1 for s in sels if s == truth[cid])
    lines.append(f"| {cid} | {cap_of[cid]} | `{truth[cid]}` | "
                 f"{' / '.join(f'`{s}`' for s in sels) or '—'} | {h}/{len(sels)} |")

lines += ["", "## 每卡命中（按 capability_id 聚合）", "", "| cap | 命中/判数 |", "|---|---|"]
for cap in sorted(per_cap):
    h, t = per_cap[cap]
    lines.append(f"| {cap} | {h}/{t} |")

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
    "> 本评测只测「给定 24 张卡候选时的 top-1 路由」，不测技能层是否触发、"
    "也不测答案内容质量（另见 output / trigger 评测报告）。judge 看到的是能力索引，不是完整卡片正文；"
    "且 instruction 中已提示 CAP-22 / CAP-23 / CAP-24 的三层分工，可能高估真实口语场景准确率。",
    "",
]
report = "\n".join(lines)
(E / "routing-eval-report.md").write_text(report, encoding="utf-8")
print("\n".join(lines[:20]))
print("...")
print(f"CAP-24: {focus['CAP-24'][0]}/{focus['CAP-24'][1]} | CAP-23: {focus['CAP-23'][0]}/{focus['CAP-23'][1]} "
      f"| CAP-22: {focus['CAP-22'][0]}/{focus['CAP-22'][1]} | cross: {sum(cross.values())}")
