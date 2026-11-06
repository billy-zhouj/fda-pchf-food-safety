#!/usr/bin/env python3
"""v4.10 路由命中的确定性静态核对（不依赖 LLM judge，可重复复现）。

检查两层：
  A. 编译产物登记完整性：CAP-23 是否登记在 verified.yaml / destinations.json /
     capability-index.md / cheatsheet.md / SKILL.md 路由表，卡片文件是否落在 dist-v14
     与已安装目录，产物与安装目录是否仍逐文件一致。
  B. 词面代理 top-1：用 verified.yaml 里 23 张卡的 keywords 做 IDF 加权打分，
     对 10 条新用例 + 7 条 CAP-23 定向 prompt 看 CAP-23 是否排第一。

B 只是弱代理（关键词有重叠、短词噪声、中文 prompt 与英文 keyword 错位），
不作为准确率结论，只用来说明「为什么仍需要干净 sub-agent 盲判」。
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from collections import Counter
from pathlib import Path

import yaml

BOOK = Path(__file__).resolve().parents[1]
ROOT = BOOK.parent
E = BOOK / ".cangjie/v4-10-eval"
DIST = BOOK / "dist-v14"
INST = ROOT / ".workbuddy/skills/fda-pchf-food-safety"
SLUG = "seafood-hazards-controls-guide"
REPORT = E / "static-routing-check.md"

lines: list[str] = ["# CAP-23 路由命中 — 确定性静态核对（v4.10）", ""]
fail: list[str] = []


def chk(label: str, ok: bool, detail: str = "") -> None:
    lines.append(f"- {'PASS' if ok else 'FAIL'} | {label}" + (f" | {detail}" if detail else ""))
    if not ok:
        fail.append(label)


# ---------------------------------------------------------------- A. 登记完整性
bundle = yaml.safe_load((BOOK / ".cangjie/capabilities/verified.yaml").read_text(encoding="utf-8"))
caps = bundle["capabilities"]
by_slug = {c["slug"]: c for c in caps}
chk("verified.yaml 共 23 张卡", len(caps) == 23, f"实得 {len(caps)}")
chk("verified.yaml 含 CAP-23 且 capability_id 正确",
    by_slug.get(SLUG, {}).get("capability_id") == "CAP-23",
    str(by_slug.get(SLUG, {}).get("capability_id")))
chk("CAP-23 importance / status", by_slug.get(SLUG, {}).get("importance") == "extended"
    and by_slug.get(SLUG, {}).get("status") == "active",
    f"importance={by_slug.get(SLUG, {}).get('importance')} status={by_slug.get(SLUG, {}).get('status')}")
chk("CAP-23 also_read 9 条", len(by_slug.get(SLUG, {}).get("also_read", [])) == 9,
    str(len(by_slug.get(SLUG, {}).get("also_read", []))))

dest = json.loads((BOOK / ".cangjie/capabilities/destinations.json").read_text(encoding="utf-8"))["destinations"]
chk("destinations.json 共 23 个去向", len(dest) == 23, f"实得 {len(dest)}")
chk("destinations.json CAP-23 → fda-pchf-food-safety",
    dest.get("CAP-23", {}).get("served_by") == "fda-pchf-food-safety")

index = (INST / "references/capability-index.md").read_text(encoding="utf-8")
chk("已安装 capability-index.md 含 CAP-23 行",
    len([l for l in index.splitlines() if l.startswith("| CAP-23 |")]) == 1)
chk("capability-index 的 CAP-23 行指向正确卡片",
    f"capabilities/{SLUG}.md" in next(l for l in index.splitlines() if l.startswith("| CAP-23 |")))

# cheatsheet 用「卡片标题 | 一句话规则」登记，不含 CAP-xx 编号也不含 slug，
# 故按 CAP-23 标题片段 + 该行回指 CAP-22 来判定（v4.10 首次核对时曾因条件过窄误报 FAIL）。
cheat = (INST / "references/cheatsheet.md").read_text(encoding="utf-8")
cap23_cheat_rows = [l for l in cheat.splitlines() if "海产品危害分析与控制的完整判定链" in l]
cheat_ok = len(cap23_cheat_rows) == 1 and "CAP-22" in cap23_cheat_rows[0]
chk("cheatsheet.md 含 CAP-23 一句话规则行", cheat_ok,
    f"命中 {len(cap23_cheat_rows)} 行")

skill = (INST / "SKILL.md").read_text(encoding="utf-8")
# 主行判据：第 2 列（split 后 index 2）恰为该卡；不能用子串匹配，
# 否则会把「辅读列最后一个是 CAP-23」的 8 行一起算作主行。
main_rows = []
also_rows = []
for l in skill.splitlines():
    if not l.startswith("|"):
        continue
    cols = [c.strip() for c in l.split("|")]
    if len(cols) >= 4 and cols[2] == f"references/capabilities/{SLUG}.md":
        main_rows.append(cols)
    if f"capabilities/{SLUG}.md" in l:
        also_rows.append(l)
chk("SKILL.md 路由表含 CAP-23 主行（第 2 列为该卡）", len(main_rows) == 1,
    f"命中 {len(main_rows)} 行主行")
chk("SKILL.md 中 CAP-23 被其它卡列为辅读（双向链）", len(also_rows) >= 9,
    f"共 {len(also_rows)} 行含该 slug")

card_a = DIST / f"references/capabilities/{SLUG}.md"
card_b = INST / f"references/capabilities/{SLUG}.md"
chk("CAP-23 卡片文件在 dist-v14 与已安装目录均存在", card_a.exists() and card_b.exists())
if card_a.exists() and card_b.exists():
    chk("两份 CAP-23 卡片内容一致", card_a.read_bytes() == card_b.read_bytes())


def digest(root: Path) -> dict[str, str]:
    return {str(p.relative_to(root)).replace("\\", "/"): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()}


a, b = digest(DIST), digest(INST)
diff = [k for k in set(a) | set(b) if a.get(k) != b.get(k)]
chk("dist-v14 与已安装目录逐文件 hash 一致", not diff and len(a) == 28,
    f"files={len(a)} diff={len(diff)}")

# ---------------------------------------------------------------- B. 词面代理 top-1
kw_by_slug = {c["slug"]: [str(k).strip().lower() for k in c["keywords"] if str(k).strip()]
              for c in caps}
df = Counter(kw for kws in kw_by_slug.values() for kw in set(kws))
N = len(kw_by_slug)


def score(prompt: str, slug: str) -> float:
    p = prompt.lower()
    kws = [k for k in kw_by_slug[slug] if len(k) >= 3]
    if not kws:
        return 0.0
    hit = 0.0
    for k in set(kws):
        if k in p:
            hit += math.log((N + 1) / (df[k] + 1)) + 0.1
    return hit / math.sqrt(len(kws))  # 按关键词表长度归一，避免大表天然占优


suite = json.loads((E / "routing-suite.json").read_text(encoding="utf-8"))
prompts = [(c["case_id"], c["prompt"], c["expected_capability"], c["capability_id"])
           for c in suite["routing_cases"] if c["capability_id"] in ("CAP-23", "CAP-22")]
formal = json.loads((BOOK / "test-prompts.json").read_text(encoding="utf-8"))
for c in formal["test_cases"]:
    if c["id"].startswith("seafood-hazards-"):
        prompts.append((c["id"], c["prompt"], SLUG, "CAP-23"))

lines += ["", "## 词面代理 top-1（弱证据，仅作诊断）", "",
          "| case | 期望 | 词面 top-1 | 是否命中 | CAP-23 分 / top-1 分 |",
          "|---|---|---|---|---|"]
agent_hit = 0
for cid, prompt, exp, cap_id in prompts:
    ranked = sorted(((score(prompt, s), s) for s in kw_by_slug), reverse=True)
    top_slug = ranked[0][1]
    s23 = score(prompt, SLUG)
    ok = top_slug == exp
    agent_hit += ok
    lines.append(f"| {cid} | `{exp}` | `{top_slug}` | {'✓' if ok else '✗'} | "
                 f"{s23:.3f} / {ranked[0][0]:.3f} |")

cap23_cases = [p for p in prompts if p[3] == "CAP-23"]
cap23_top = sum(1 for cid, pr, exp, ci in cap23_cases
                if sorted(((score(pr, s), s) for s in kw_by_slug), reverse=True)[0][1] == SLUG)
lines += ["",
          f"- 词面代理总体 top-1：{agent_hit}/{len(prompts)}",
          f"- 其中 CAP-23 定向/新用例：{cap23_top}/{len(cap23_cases)}",
          "- 说明：关键词表在 CAP-22（法条层）与 CAP-23（指南判定链）之间大量重叠"
          "（hazard analysis / CCP / critical limit / reasonably likely to occur 等），"
          "纯词面无法表达「问的是法定义务还是判定方法」这一语义差别；"
          "本层只证明登记完整，准确率结论以干净 sub-agent 盲判为准。",
          ""]

lines += ["## 结论", "",
          f"- 登记完整性：{'全部 PASS' if not fail else '存在 FAIL：' + ', '.join(fail)}",
          "- 词面代理结果见上表，不用于宣布路由准确率。", ""]

REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
print("\nSTATIC_CHECK_OK" if not fail else "\nSTATIC_CHECK_FAILED")
raise SystemExit(1 if fail else 0)
