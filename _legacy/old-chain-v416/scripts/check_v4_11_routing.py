#!/usr/bin/env python3
"""v4.11 路由命中的确定性静态核对（不依赖 LLM judge，可重复复现）。

检查两层：
  A. 编译产物登记完整性：CAP-24 是否登记在 verified.yaml / destinations.json /
     capability-index.md / cheatsheet.md / SKILL.md 路由表，卡片文件是否落在 dist-v15
     与已安装目录，产物与安装目录是否仍逐文件一致。
  B. 词面代理 top-1：用 verified.yaml 里 24 张卡的 keywords 做 IDF 加权打分，
     对 10 条新用例 + CAP-24/CAP-23/CAP-22 定向 prompt 看是否正确排第一。

B 只是弱代理，不作为准确率结论，只用来说明「为什么仍需要干净 sub-agent 盲判」。
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
E = BOOK / ".cangjie/v4-11-eval"
DIST = BOOK / "dist-v15"
INST = ROOT / ".workbuddy/skills/fda-pchf-food-safety"
SLUG = "seafood-inspection-program"
REPORT = E / "static-routing-check.md"

lines: list[str] = ["# CAP-24 路由命中 — 确定性静态核对（v4.11）", ""]
fail: list[str] = []


def chk(label: str, ok: bool, detail: str = "") -> None:
    lines.append(f"- {'PASS' if ok else 'FAIL'} | {label}" + (f" | {detail}" if detail else ""))
    if not ok:
        fail.append(label)


# ---------------------------------------------------------------- A. 登记完整性
bundle = yaml.safe_load((BOOK / ".cangjie/capabilities/verified.yaml").read_text(encoding="utf-8"))
caps = bundle["capabilities"]
by_slug = {c["slug"]: c for c in caps}
chk("verified.yaml 共 24 张卡", len(caps) == 24, f"实得 {len(caps)}")
chk("verified.yaml 含 CAP-24 且 capability_id 正确",
    by_slug.get(SLUG, {}).get("capability_id") == "CAP-24",
    str(by_slug.get(SLUG, {}).get("capability_id")))
chk("CAP-24 importance / status", by_slug.get(SLUG, {}).get("importance") == "extended"
    and by_slug.get(SLUG, {}).get("status") == "active",
    f"importance={by_slug.get(SLUG, {}).get('importance')} status={by_slug.get(SLUG, {}).get('status')}")
chk("CAP-24 also_read 9 条", len(by_slug.get(SLUG, {}).get("also_read", [])) == 9,
    str(len(by_slug.get(SLUG, {}).get("also_read", []))))
chk("book.additional_sources 15 条（+主来源 = 十六类）",
    len(bundle["book"]["additional_sources"]) == 15,
    str(len(bundle["book"]["additional_sources"])))
chk("第十六来源 source_id 正确",
    bundle["book"]["additional_sources"][-1]["source_id"] == "src-fda-cp-7303-842-2023")
chk("core_principles 48 / stop_conditions 22",
    len(bundle["entry"]["core_principles"]) == 48 and len(bundle["entry"]["stop_conditions"]) == 22,
    f"{len(bundle['entry']['core_principles'])} / {len(bundle['entry']['stop_conditions'])}")

dest = json.loads((BOOK / ".cangjie/capabilities/destinations.json").read_text(encoding="utf-8"))["destinations"]
chk("destinations.json 共 24 个去向", len(dest) == 24, f"实得 {len(dest)}")
chk("destinations.json CAP-24 → fda-pchf-food-safety",
    dest.get("CAP-24", {}).get("served_by") == "fda-pchf-food-safety")

index = (INST / "references/capability-index.md").read_text(encoding="utf-8")
rows24 = [l for l in index.splitlines() if l.startswith("| CAP-24 |")]
chk("已安装 capability-index.md 含 CAP-24 行", len(rows24) == 1)
chk("capability-index 的 CAP-24 行指向正确卡片",
    bool(rows24) and f"capabilities/{SLUG}.md" in rows24[0])

# cheatsheet 用「卡片标题 | 一句话规则」登记，不含 CAP-xx 编号也不含 slug
cheat = (INST / "references/cheatsheet.md").read_text(encoding="utf-8")
cap24_cheat_rows = [l for l in cheat.splitlines() if "CP 7303.842 海产品检查程序整书导航" in l]
cheat_ok = len(cap24_cheat_rows) == 1 and "CAP-22" in cap24_cheat_rows[0]
chk("cheatsheet.md 含 CAP-24 一句话规则行", cheat_ok,
    f"命中 {len(cap24_cheat_rows)} 行")

skill = (INST / "SKILL.md").read_text(encoding="utf-8")
main_rows, also_rows = [], []
for l in skill.splitlines():
    if not l.startswith("|"):
        continue
    cols = [c.strip() for c in l.split("|")]
    if len(cols) >= 4 and cols[2] == f"references/capabilities/{SLUG}.md":
        main_rows.append(cols)
    if f"capabilities/{SLUG}.md" in l:
        also_rows.append(l)
chk("SKILL.md 路由表含 CAP-24 主行（第 2 列为该卡）", len(main_rows) == 1,
    f"命中 {len(main_rows)} 行主行")
chk("SKILL.md 中 CAP-24 被其它卡列为辅读（双向链）", len(also_rows) >= 9,
    f"共 {len(also_rows)} 行含该 slug")
chk("SKILL.md 已无「十五类」当前口径", "十五类" not in skill)
chk("SKILL.md 含「24 张能力卡」与「十六类不可混引」",
    "24 张能力卡" in skill and "十六类不可混引" in skill)

card_a = DIST / f"references/capabilities/{SLUG}.md"
card_b = INST / f"references/capabilities/{SLUG}.md"
chk("CAP-24 卡片文件在 dist-v15 与已安装目录均存在", card_a.exists() and card_b.exists())
if card_a.exists() and card_b.exists():
    chk("两份 CAP-24 卡片内容一致", card_a.read_bytes() == card_b.read_bytes())
    chk("CAP-24 卡含 36 个逐字引用块", card_b.read_text(encoding="utf-8").count('> "') == 36)


def digest(root: Path) -> dict[str, str]:
    return {str(p.relative_to(root)).replace("\\", "/"): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()}


a, b = digest(DIST), digest(INST)
diff = [k for k in set(a) | set(b) if a.get(k) != b.get(k)]
chk("dist-v15 与已安装目录逐文件 hash 一致", not diff and len(a) == 29,
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
    return hit / math.sqrt(len(kws))


suite = json.loads((E / "routing-suite.json").read_text(encoding="utf-8"))
prompts = [(c["case_id"], c["prompt"], c["expected_capability"], c["capability_id"])
           for c in suite["routing_cases"] if c["capability_id"] in ("CAP-24", "CAP-23", "CAP-22")]
formal = json.loads((BOOK / "test-prompts.json").read_text(encoding="utf-8"))
for c in formal["test_cases"]:
    if c["id"].startswith("seafood-inspection-"):
        prompts.append((c["id"], c["prompt"], SLUG, "CAP-24"))

lines += ["", "## 词面代理 top-1（弱证据，仅作诊断）", "",
          "| case | 期望 | 词面 top-1 | 是否命中 | CAP-24 分 / top-1 分 |",
          "|---|---|---|---|---|"]
agent_hit = 0
for cid, prompt, exp, cap_id in prompts:
    ranked = sorted(((score(prompt, s), s) for s in kw_by_slug), reverse=True)
    top_slug = ranked[0][1]
    s24 = score(prompt, SLUG)
    ok = top_slug == exp
    agent_hit += ok
    lines.append(f"| {cid} | `{exp}` | `{top_slug}` | {'✓' if ok else '✗'} | "
                 f"{s24:.3f} / {ranked[0][0]:.3f} |")

cap24_cases = [p for p in prompts if p[3] == "CAP-24"]
cap24_top = sum(1 for cid, pr, exp, ci in cap24_cases
                if sorted(((score(pr, s), s) for s in kw_by_slug), reverse=True)[0][1] == SLUG)
lines += ["",
          f"- 词面代理总体 top-1：{agent_hit}/{len(prompts)}",
          f"- 其中 CAP-24 定向/新用例：{cap24_top}/{len(cap24_cases)}",
          "- 说明：CAP-22（法条层）、CAP-23（指南判定链）、CAP-24（检查程序层）的关键词高度重叠"
          "（hazard analysis / CCP / histamine / 500 ppm / §123.6 等），纯词面无法表达"
          "「问的是法定义务、危害判定方法，还是 FDA 检查作业」这一语义差别；"
          "本层只证明登记完整，准确率结论以干净 sub-agent 盲判为准。",
          ""]

lines += ["## 结论", "",
          f"- 登记完整性：{'全部 PASS' if not fail else '存在 FAIL：' + ', '.join(fail)}",
          "- 词面代理结果见上表，不用于宣布路由准确率。", ""]

REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines[:24]))
print("...")
print("\nSTATIC_CHECK_OK" if not fail else "\nSTATIC_CHECK_FAILED")
raise SystemExit(1 if fail else 0)
