#!/usr/bin/env python3
"""v4.8 / v4.9 历史补测的能力卡路由判分（沿用 score_v4_10_routing.py 口径）。

输入: v4-8-v4-9-legacy-eval/routing-suite.json + results-routing/run*.jsonl
输出: v4-8-v4-9-legacy-eval/routing-eval-report.md
统计: top-1 命中、重复一致性、非法 slug、混淆对、每卡命中、
      CAP-21 / CAP-22 / CAP-23 专项与三卡交叉混淆、
      open boundary 题 seafood-10 单独统计 + 不含该条的稳健数字。
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

E = Path(__file__).resolve().parent / "v4-8-v4-9-legacy-eval"
suite = json.loads((E / "routing-suite.json").read_text(encoding="utf-8"))
truth = {c["case_id"]: c["expected_capability"] for c in suite["routing_cases"]}
cap_of = {c["case_id"]: c["capability_id"] for c in suite["routing_cases"]}
cands = set(suite["candidate_capabilities"])
OPEN = set(suite.get("open_boundary_cases", []))
S21, S22, S23 = ("fsvp-inspection-program", "seafood-haccp-statutory-requirements",
                 "seafood-hazards-controls-guide")

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
rounds = n // len(truth) if truth else 0
acc = hits / n if n else 0.0
consistent = sum(1 for cid, sels in by_case.items() if len(set(sels)) <= 1)

# 不含开放边界题的稳健数字
rows_wo = [r for r in rows if r["case_id"] not in OPEN]
hits_wo = sum(1 for r in rows_wo if r.get("selected_capability") == truth.get(r["case_id"]))

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


def focus(cap_id: str, slug: str) -> tuple[int, int, int]:
    ids = {cid for cid, c in cap_of.items() if c == cap_id}
    tot = sum(1 for r in rows if r["case_id"] in ids)
    h = sum(1 for r in rows if r["case_id"] in ids and r.get("selected_capability") == slug)
    return len(ids), h, tot


n21, h21, t21 = focus("CAP-21", S21)
n22, h22, t22 = focus("CAP-22", S22)
n23, h23, t23 = focus("CAP-23", S23)

cross = Counter()
for r in rows:
    exp, sel = truth.get(r["case_id"]), r.get("selected_capability")
    if exp in (S21, S22, S23) and sel in (S21, S22, S23) and sel != exp:
        cross[(exp, sel)] += 1

lines = [
    "# 能力卡路由正确性评测 — v4.8 / v4.9 历史用例补测（当前产物 v4.10）",
    "",
    f"- 用例数 {len(truth)}（23 张卡基础各 1 条 + 20 条历史 prompt + 3 条 CAP-23 对照）",
    f"- 判分记录 {n} 条；每例重复 {rounds} 次（3 个干净 sub-agent）",
    f"- top-1 命中 {hits}/{n} = **{acc:.3f}**",
    f"- 排除开放边界题 `seafood-10` 后：{hits_wo}/{len(rows_wo)} = **{hits_wo/len(rows_wo):.3f}**",
    f"- 重复判断一致的用例 {consistent}/{len(truth)}",
    f"- 非法 slug（不在候选清单）: {len(bad_slug)}",
    "",
    "## CAP-21 / CAP-22 专项（本次历史欠账）",
    "",
    f"- CAP-21 定向/基础用例 {n21} 条 × {rounds} 轮 = {t21} 判，命中 **{h21}/{t21}**",
    f"- CAP-22 定向/基础用例 {n22} 条 × {rounds} 轮 = {t22} 判，命中 **{h22}/{t22}**",
    f"- CAP-23 对照/基础用例 {n23} 条 × {rounds} 轮 = {t23} 判，命中 **{h23}/{t23}**",
    f"- 三卡之间交叉错判：{sum(cross.values())}"
    + (f"（{'；'.join(f'`{a}`→`{b}` ×{k}' for (a, b), k in cross.most_common())}）" if cross else ""),
    "",
    "## 开放边界题 `seafood-10`（notes 明说分流 CAP-22 与 CAP-20，top-1 无唯一解）",
    "",
    f"- 3 轮选卡分布：{dict(Counter(by_case.get('seafood-10', [])))}",
    "- 该条计入主指标仅为口径一致性，其选卡分布单独披露，不作为「路由错误」的证据。",
    "",
    "## 逐例结果",
    "",
    "| case | cap | expected | selected (按 run) | 命中 |",
    "|---|---|---|---|---|",
]
for cid in sorted(truth):
    sels = by_case.get(cid, [])
    h = sum(1 for s in sels if s == truth[cid])
    lines.append(f"| {cid}{' (open)' if cid in OPEN else ''} | {cap_of[cid]} | `{truth[cid]}` | "
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
    "> 本评测只测「给定 23 张卡候选时的 top-1 路由」，不测技能层是否触发、"
    "也不测答案内容质量（另见 output 评测报告）。judge 看到的是能力索引，不是完整卡片正文；"
    "且 instruction 中已提示 CAP-21 / CAP-22 / CAP-23 三层分工（与 v4.7、v4.10 的做法一致，"
    "为可比性保留），可能高估真实口语场景准确率。",
    "",
]
report = "\n".join(lines)
(E / "routing-eval-report.md").write_text(report, encoding="utf-8")
print("\n".join(lines[:22]))
print("...")
print(f"CAP-21: {h21}/{t21} | CAP-22: {h22}/{t22} | CAP-23: {h23}/{t23} | top-1: {hits}/{n}")
