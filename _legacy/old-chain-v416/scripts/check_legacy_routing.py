#!/usr/bin/env python3
"""CAP-21 / CAP-22 路由命中的确定性静态核对（不依赖 LLM，可重复复现）。

与 v4.10 的 check_v4_10_routing.py 同型，改查 v4.8 的 CAP-21 与 v4.9 的 CAP-22：
  A. 编译产物登记完整性（verified.yaml / destinations.json / capability-index.md /
     cheatsheet.md / SKILL.md 路由表 / 卡片文件 / 产物与安装目录 hash）
  B. 词面代理 top-1：用 verified.yaml 的 keywords 做 IDF 加权打分，对 20 条历史
     prompt 看 CAP-21 / CAP-22 是否排第一（弱证据，只作诊断）
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
E = BOOK / ".cangjie/v4-8-v4-9-legacy-eval"
DIST = BOOK / "dist-v14"
INST = ROOT / ".workbuddy/skills/fda-pchf-food-safety"
TARGETS = {"CAP-21": "fsvp-inspection-program", "CAP-22": "seafood-haccp-statutory-requirements"}
REPORT = E / "static-routing-check.md"

lines: list[str] = ["# CAP-21 / CAP-22 路由命中 — 确定性静态核对（v4.8 / v4.9 历史补测）", ""]
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
for cap_id, slug in TARGETS.items():
    c = by_slug.get(slug, {})
    chk(f"verified.yaml {cap_id} capability_id 正确", c.get("capability_id") == cap_id,
        str(c.get("capability_id")))
    chk(f"{cap_id} status=active 且 also_read 非空",
        c.get("status") == "active" and len(c.get("also_read", [])) > 0,
        f"status={c.get('status')} also_read={len(c.get('also_read', []))}")

dest = json.loads((BOOK / ".cangjie/capabilities/destinations.json").read_text(encoding="utf-8"))["destinations"]
chk("destinations.json 共 23 个去向", len(dest) == 23, f"实得 {len(dest)}")
for cap_id in TARGETS:
    chk(f"destinations.json {cap_id} → fda-pchf-food-safety",
        dest.get(cap_id, {}).get("served_by") == "fda-pchf-food-safety")

index = (INST / "references/capability-index.md").read_text(encoding="utf-8")
cheat = (INST / "references/cheatsheet.md").read_text(encoding="utf-8")
skill = (INST / "SKILL.md").read_text(encoding="utf-8")
skill_rows = [[c.strip() for c in l.split("|")] for l in skill.splitlines() if l.startswith("|")]

for cap_id, slug in TARGETS.items():
    idx_rows = [l for l in index.splitlines() if l.startswith(f"| {cap_id} |")]
    chk(f"capability-index.md 含唯一 {cap_id} 行", len(idx_rows) == 1, f"命中 {len(idx_rows)} 行")
    if idx_rows:
        chk(f"capability-index 的 {cap_id} 行指向正确卡片", f"capabilities/{slug}.md" in idx_rows[0])
    # cheatsheet 用卡片标题登记，不含 CAP 编号；按标题片段判定
    title_frag = {"CAP-21": "FSVP 进口商检查", "CAP-22": "海产品 HACCP 的法定要求"}[cap_id]
    cheat_rows = [l for l in cheat.splitlines() if l.startswith("| " + title_frag)]
    chk(f"cheatsheet.md 含 {cap_id} 一句话规则行", len(cheat_rows) == 1,
        f"命中 {len(cheat_rows)} 行")
    main_rows = [r for r in skill_rows if len(r) >= 4 and r[2] == f"references/capabilities/{slug}.md"]
    chk(f"SKILL.md 路由表含唯一 {cap_id} 主行（第 2 列）", len(main_rows) == 1,
        f"命中 {len(main_rows)} 行")
    a, b = DIST / f"references/capabilities/{slug}.md", INST / f"references/capabilities/{slug}.md"
    chk(f"{cap_id} 卡片在 dist-v14 与已安装目录均存在", a.exists() and b.exists())
    if a.exists() and b.exists():
        chk(f"两份 {cap_id} 卡片内容一致", a.read_bytes() == b.read_bytes())
    card = b.read_text(encoding="utf-8") if b.exists() else ""
    chk(f"{cap_id} 卡片开头按当前口径标「十五类不可混引」", "十五类不可混引" in card[:1500])


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
    hit = sum(math.log((N + 1) / (df[k] + 1)) + 0.1 for k in set(kws) if k in p)
    return hit / math.sqrt(len(kws))


formal = json.loads((BOOK / "test-prompts.json").read_text(encoding="utf-8"))
prompts = [(c["id"], c["prompt"], TARGETS["CAP-21" if c["id"].startswith("fsvp-") else "CAP-22"])
           for c in formal["test_cases"]
           if c["id"].startswith("fsvp-")
           or (c["id"].startswith("seafood-") and not c["id"].startswith("seafood-hazards-"))]
assert len(prompts) == 20

lines += ["", "## 词面代理 top-1（弱证据，仅作诊断）", "",
          "| case | 期望 | 词面 top-1 | 是否命中 |", "|---|---|---|---|"]
hit = 0
for cid, prompt, exp in prompts:
    ranked = sorted(((score(prompt, s), s) for s in kw_by_slug), reverse=True)
    top = ranked[0][1]
    ok = top == exp
    hit += ok
    lines.append(f"| {cid} | `{exp}` | `{top}` | {'✓' if ok else '✗'} |")
lines += ["", f"- 词面代理 top-1 总体：{hit}/{len(prompts)}",
          f"- 其中 CAP-21（fsvp-*）：{sum(1 for cid, p, e in prompts if cid.startswith('fsvp-') and sorted(((score(p, s), s) for s in kw_by_slug), reverse=True)[0][1] == e)}/10；"
          f"CAP-22（seafood-*）：{sum(1 for cid, p, e in prompts if cid.startswith('seafood-') and sorted(((score(p, s), s) for s in kw_by_slug), reverse=True)[0][1] == e)}/10",
          "- 说明：中文口语化 prompt 与英文 keyword 表错位，且 CAP-21 / CAP-22 / CAP-23 在 "
          "hazard analysis / importer / HACCP 等词上重叠；本层只证明登记完整，"
          "准确率结论以干净 sub-agent 语义盲判为准。", ""]

lines += ["## 结论", "",
          f"- 登记完整性：{'全部 PASS' if not fail else '存在 FAIL：' + ', '.join(fail)}",
          "- 词面代理结果见上表，不用于宣布路由准确率。", ""]

REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
print("\nSTATIC_CHECK_OK" if not fail else "\nSTATIC_CHECK_FAILED")
raise SystemExit(1 if fail else 0)
