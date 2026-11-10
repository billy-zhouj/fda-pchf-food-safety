"""check_v4_13_routing.py — v4.13 静态登记核对（不发请求、不调模型）

核对项：
 1. bundle 规模：26 卡 / 52 principles / 26 stops / 17 additional_sources（末条为 Part 120）
 2. CAP-26 身份：juice-haccp / active / extended / also_read 11 条
 3. 双向辅读链：CAP-26 与 CAP-15 / CAP-20 / CAP-22 / CAP-25 等反向引用均存在
 4. 产物：能力索引主行 1 行、SKILL.md 无「十七类」残留、含 CAP-26
 5. 卡片：26 个引用块、覆盖 8 个条款锚点、载明两处豁免与 §117.5(c) 未收
 6. 产物 == 安装目录：逐文件 sha256 差异 0
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parents[1]
WORKSPACE = BASE.parent
BUNDLE = BASE / ".cangjie/capabilities/verified.yaml"
DIST = BASE / "dist-v17"
INST = WORKSPACE / ".workbuddy/skills/fda-pchf-food-safety"
CARD = BASE / ".cangjie/capabilities/cards/juice-haccp.md"
META = BASE / ".cangjie/capabilities/cards/_meta-juice-haccp.yaml"

results: list[tuple[bool, str]] = []


def check(cond: bool, msg: str) -> None:
    results.append((bool(cond), msg))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


b = yaml.safe_load(BUNDLE.read_text(encoding="utf-8"))
caps = b["capabilities"]
entry = b["entry"]

# ── 1. 规模 ────────────────────────────────────────────────────────────
check(len(caps) == 26, f"能力卡 26 张（实得 {len(caps)}）")
check(len(entry["core_principles"]) == 52,
      f"core_principles 52 条（实得 {len(entry['core_principles'])}）")
check(len(entry["stop_conditions"]) == 26,
      f"stop_conditions 26 条（实得 {len(entry['stop_conditions'])}）")
srcs = b["book"]["additional_sources"]
check(len(srcs) == 17, f"additional_sources 17 条（实得 {len(srcs)}）")
check(srcs[-1]["source_id"] == "src-21-cfr-part-120-2025",
      f"末条来源为 Part 120（实得 {srcs[-1]['source_id']}）")

# ── 2. CAP-26 身份 ─────────────────────────────────────────────────────
c26 = next((c for c in caps if c["slug"] == "juice-haccp"), None)
check(c26 is not None, "CAP-26 已登记")
if c26:
    check(c26["capability_id"] == "CAP-26", f"编号为 CAP-26（实得 {c26['capability_id']}）")
    check(c26.get("status", "active") == "active", "status = active")
    check(c26["importance"] == "extended", f"importance = extended（实得 {c26['importance']}）")
    check(len(c26["also_read"]) == 11, f"also_read 11 条（实得 {len(c26['also_read'])}）")
    need = {"cgmp-compliance-guide", "lacf-statutory-requirements",
            "seafood-haccp-statutory-requirements", "emergency-permit-control",
            "hazard-analysis-method"}
    check(need <= set(c26["also_read"]), "also_read 覆盖 cGMP / LACF / 海产品 / Part 108 / 危害分析")

    by_slug = {c["slug"]: c for c in caps}
    back = [s for s in ("cgmp-compliance-guide", "lacf-statutory-requirements",
                        "seafood-haccp-statutory-requirements", "emergency-permit-control",
                        "hazard-analysis-method", "process-control-validation",
                        "allergen-program", "recall-plan", "regulatory-boundaries")
            if "juice-haccp" in by_slug[s]["also_read"]]
    check(len(back) == 9, f"反向辅读链 9 张（实得 {len(back)}: {back}）")

# ── 3. 产物 ────────────────────────────────────────────────────────────
skill = (DIST / "SKILL.md").read_text(encoding="utf-8")
index = (DIST / "references/capability-index.md").read_text(encoding="utf-8")
check(skill.count("juice-haccp") >= 1, "SKILL.md 含 CAP-26 slug")
check(skill.count("十七类") == 0, f"SKILL.md 无「十七类」残留（实得 {skill.count('十七类')}）")
check("十八类" in skill, "SKILL.md 含「十八类」口径")
check(index.count("juice-haccp") == 1,
      f"能力索引主行 1 行（实得 {index.count('juice-haccp')}）")

# ── 4. 卡片 ────────────────────────────────────────────────────────────
card = CARD.read_text(encoding="utf-8")
check(card.count('> "') == 26, f"CAP-26 引用块 26 个（实得 {card.count('> ' + chr(34))}）")
for sec in ("§ 120.1", "§ 120.3", "§ 120.5", "§ 120.7", "§ 120.8",
            "§ 120.9", "§ 120.11", "§ 120.12", "§ 120.14", "§ 120.24", "§ 120.25"):
    check(sec in card, f"卡片覆盖 {sec}")
check("pertinent microorganism" in card, "卡片载明目标菌定义")
check("117.5(c)" in card and "转引未收" in card, "卡片载明 §117.5(c) 未收")
check("10⁵" in card or "105" in card, "卡片处理了 10⁵ 文本层缺陷")
meta = yaml.safe_load(META.read_text(encoding="utf-8"))
check(meta["slug"] == "juice-haccp", "meta slug 一致")
check(len(meta["keywords"]) >= 120, f"meta keywords ≥120（实得 {len(meta['keywords'])}）")
check(len(meta["intents"]) >= 40, f"meta intents ≥40（实得 {len(meta['intents'])}）")
check(card.split("\n")[0].count("juice-haccp") == 1, "卡片标题含 slug")

# ── 5. 产物 == 安装目录 ───────────────────────────────────────────────
diffs = []
if INST.is_dir():
    for p in sorted(DIST.rglob("*")):
        if p.is_file():
            q = INST / p.relative_to(DIST)
            if not q.exists() or sha(p) != sha(q):
                diffs.append(str(p.relative_to(DIST)))
check(INST.is_dir(), "安装目录存在")
check(not diffs, f"产物与安装目录 hash 差异 0（实得 {len(diffs)}: {diffs[:5]}）")

passed = sum(1 for ok, _ in results if ok)
for ok, msg in results:
    print(("PASS  " if ok else "FAIL  ") + msg)
print(f"\n{passed}/{len(results)} PASS")
if passed != len(results):
    raise SystemExit(1)
print("RESULT: PASS")
