"""check_v4_12_routing.py — v4.12 静态登记核对（不发请求、不调模型）

核对项：
 1. bundle 规模：25 卡 / 50 principles / 24 stops / 16 additional_sources（末条为 Part 108）
 2. CAP-25 身份：emergency-permit-control / active / extended / also_read 9 条
 3. 双向辅读链：CAP-25 ↔ CAP-20 / CAP-19 / CAP-22 等反向引用均存在
 4. 产物：能力索引主行各 1 行、SKILL.md 无「十六类」残留、SKILL.md 含 CAP-25
 5. 卡片：27 个引用块、含〔§ 108.xxx〕编号、与 meta 标题一致
 6. 产物 == 安装目录：逐文件 sha256 差异 0
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parents[1]
WORKSPACE = BASE.parent
BUNDLE = BASE / ".cangjie/capabilities/verified.yaml"
DIST = BASE / "dist-v16"
INST = WORKSPACE / ".workbuddy/skills/fda-pchf-food-safety"
CARD = BASE / ".cangjie/capabilities/cards/emergency-permit-control.md"
META = BASE / ".cangjie/capabilities/cards/_meta-emergency-permit-control.yaml"

results: list[tuple[bool, str]] = []


def check(cond: bool, msg: str) -> None:
    results.append((bool(cond), msg))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


b = yaml.safe_load(BUNDLE.read_text(encoding="utf-8"))
caps = b["capabilities"]
entry = b["entry"]

# ── 1. 规模 ────────────────────────────────────────────────────────────
check(len(caps) == 25, f"能力卡 25 张（实得 {len(caps)}）")
check(len(entry["core_principles"]) == 50,
      f"core_principles 50 条（实得 {len(entry['core_principles'])}）")
check(len(entry["stop_conditions"]) == 24,
      f"stop_conditions 24 条（实得 {len(entry['stop_conditions'])}）")
srcs = b["book"]["additional_sources"]
check(len(srcs) == 16, f"additional_sources 16 条（实得 {len(srcs)}）")
check(srcs[-1]["source_id"] == "src-21-cfr-part-108-2025",
      f"末条来源为 Part 108（实得 {srcs[-1]['source_id']}）")
check(any(s["source_id"] == "src-21-cfr-part-108-2025" for s in srcs),
      "Part 108 来源条目存在")

# ── 2. CAP-25 身份 ─────────────────────────────────────────────────────
c25 = next((c for c in caps if c["slug"] == "emergency-permit-control"), None)
check(c25 is not None, "CAP-25 已登记")
if c25:
    check(c25["capability_id"] == "CAP-25", f"编号为 CAP-25（实得 {c25['capability_id']}）")
    check(c25.get("status", "active") == "active", "status = active")
    check(c25["importance"] == "extended", f"importance = extended（实得 {c25['importance']}）")
    check(len(c25["also_read"]) == 9, f"also_read 9 条（实得 {len(c25['also_read'])}）")
    need = {"lacf-statutory-requirements", "lacf-inspection-program",
            "regulatory-boundaries", "inspection-readiness", "cgmp-compliance-guide"}
    check(need <= set(c25["also_read"]), "also_read 覆盖 LACF 双卡 + 边界 + 迎检")

    # 3. 反向链
    by_slug = {c["slug"]: c for c in caps}
    back = [s for s in ("lacf-statutory-requirements", "lacf-inspection-program",
                        "regulatory-boundaries", "inspection-readiness",
                        "cgmp-compliance-guide", "seafood-haccp-statutory-requirements",
                        "hazard-analysis-method", "defect-action-levels")
            if "emergency-permit-control" in by_slug[s]["also_read"]]
    check(len(back) == 8, f"反向辅读链 8 张（实得 {len(back)}: {back}）")

# ── 4. 产物 ────────────────────────────────────────────────────────────
skill = (DIST / "SKILL.md").read_text(encoding="utf-8")
index = (DIST / "references/capability-index.md").read_text(encoding="utf-8")
check(skill.count("emergency-permit-control") >= 1, "SKILL.md 含 CAP-25 slug")
check(skill.count("十六类") == 0, f"SKILL.md 无「十六类」残留（实得 {skill.count('十六类')}）")
check("十七类" in skill, "SKILL.md 含「十七类」口径")
check(index.count("emergency-permit-control") >= 1, "能力索引含 CAP-25")
check(index.count("emergency-permit-control") == 1,
      f"能力索引主行 1 行（实得 {index.count('emergency-permit-control')}）")

# ── 5. 卡片 ────────────────────────────────────────────────────────────
card = CARD.read_text(encoding="utf-8")
check(card.count('> "') == 27, f"CAP-25 引用块 27 个（实得 {card.count('> ' + chr(34))}）")
for sec in ("§ 108.3", "§ 108.5", "§ 108.7", "§ 108.10", "§ 108.12",
            "§ 108.19", "§ 108.25", "§ 108.35"):
    check(sec in card, f"卡片覆盖 {sec}")
check("prima facie" in card and "may be required" in card,
      "卡片载明「许可=救济」的核心纠偏")
meta = yaml.safe_load(META.read_text(encoding="utf-8"))
check(meta["slug"] == "emergency-permit-control", "meta slug 一致")
check(len(meta["keywords"]) >= 120, f"meta keywords ≥120（实得 {len(meta['keywords'])}）")
check(len(meta["intents"]) >= 40, f"meta intents ≥40（实得 {len(meta['intents'])}）")
check(meta["title"] in card or card.split("\n")[0].count("emergency-permit-control") == 1,
      "卡片标题含 slug")

# ── 6. 产物 == 安装目录 ───────────────────────────────────────────────
diffs = []
if INST.is_dir():
    for p in sorted(DIST.rglob("*")):
        if p.is_file():
            q = INST / p.relative_to(DIST)
            if not q.exists() or sha(p) != sha(q):
                diffs.append(str(p.relative_to(DIST)))
check(INST.is_dir(), "安装目录存在")
check(not diffs, f"产物与安装目录 hash 差异 0（实得 {len(diffs)}: {diffs[:5]}）")

# ── 输出 ───────────────────────────────────────────────────────────────
passed = sum(1 for ok, _ in results if ok)
for ok, msg in results:
    print(("PASS  " if ok else "FAIL  ") + msg)
print(f"\n{passed}/{len(results)} PASS")
if passed != len(results):
    raise SystemExit(1)
print("RESULT: PASS")
