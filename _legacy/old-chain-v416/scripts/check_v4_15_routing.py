"""check_v4_15_routing.py — v4.15 静态登记核对（不发请求、不调模型）

核对项：
 1. bundle 规模：27 卡 / 54 principles / 28 stops / 18 additional_sources（末条为 CP 7303.847）
 2. CAP-27 身份：juice-inspection-program / active / extended / also_read 11 条
 3. 双向辅读链：CAP-27 与 CAP-26 / CAP-15 / CAP-20 / CAP-24 等反向引用均存在
 4. 产物：能力索引主行 1 行、SKILL.md 无「十八类」残留、含「十九类」
 5. 卡片：29 个引用块、覆盖 PART I–VII 与 ATTACHMENT A、载明 PAC 分流与 10/20 ppb
 6. 错误 CP 号 7303.047 仅出现在勘误说明中
 7. 产物 == 安装目录：逐文件 sha256 差异 0
"""
from __future__ import annotations

import hashlib
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parents[1]
WORKSPACE = BASE.parent
BUNDLE = BASE / ".cangjie/capabilities/verified.yaml"
DIST = BASE / "dist-v19"
INST = WORKSPACE / ".workbuddy/skills/fda-pchf-food-safety"
CARD = BASE / ".cangjie/capabilities/cards/juice-inspection-program.md"
META = BASE / ".cangjie/capabilities/cards/_meta-juice-inspection-program.yaml"

results: list[tuple[bool, str]] = []


def check(cond: bool, msg: str) -> None:
    results.append((bool(cond), msg))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


b = yaml.safe_load(BUNDLE.read_text(encoding="utf-8"))
caps = b["capabilities"]
entry = b["entry"]

# ── 1. 规模 ────────────────────────────────────────────────────────────
check(len(caps) == 27, f"能力卡 27 张（实得 {len(caps)}）")
check(len(entry["core_principles"]) == 54,
      f"core_principles 54 条（实得 {len(entry['core_principles'])}）")
check(len(entry["stop_conditions"]) == 28,
      f"stop_conditions 28 条（实得 {len(entry['stop_conditions'])}）")
srcs = b["book"]["additional_sources"]
check(len(srcs) == 18, f"additional_sources 18 条（实得 {len(srcs)}）")
check(srcs[-1]["source_id"] == "src-fda-cp-7303-847-2010",
      f"末条来源为 CP 7303.847（实得 {srcs[-1]['source_id']}）")

# ── 2. CAP-27 身份 ─────────────────────────────────────────────────────
c27 = next((c for c in caps if c["slug"] == "juice-inspection-program"), None)
check(c27 is not None, "CAP-27 已登记")
if c27:
    check(c27["capability_id"] == "CAP-27", f"编号为 CAP-27（实得 {c27['capability_id']}）")
    check(c27.get("status", "active") == "active", "status = active")
    check(c27["importance"] == "extended", f"importance = extended（实得 {c27['importance']}）")
    check(len(c27["also_read"]) == 11, f"also_read 11 条（实得 {len(c27['also_read'])}）")
    need = {"juice-haccp", "inspection-sampling", "investigator-authority-procedure",
            "inspection-readiness", "regulatory-boundaries"}
    check(need <= set(c27["also_read"]),
          "also_read 覆盖 Part 120 法条卡 / 抽样 / 检查员权限 / 检查准备 / 边界")

    by_slug = {c["slug"]: c for c in caps}
    back = [s for s, x in by_slug.items()
            if s != "juice-inspection-program" and "juice-inspection-program" in x["also_read"]]
    check(len(back) == 12, f"反向辅读链 12 张（实得 {len(back)}）")

# ── 3. 产物 ────────────────────────────────────────────────────────────
skill = (DIST / "SKILL.md").read_text(encoding="utf-8")
index = (DIST / "references/capability-index.md").read_text(encoding="utf-8")
check(skill.count("juice-inspection-program") >= 1, "SKILL.md 含 CAP-27 slug")
check(skill.count("十八类") == 0, f"SKILL.md 无「十八类」残留（实得 {skill.count('十八类')}）")
check("十九类" in skill, "SKILL.md 含「十九类」口径")
check(index.count("juice-inspection-program") == 1,
      f"能力索引主行 1 行（实得 {index.count('juice-inspection-program')}）")

# ── 4. 卡片 ────────────────────────────────────────────────────────────
card = CARD.read_text(encoding="utf-8")
check(card.count('> "') == 29, f"CAP-27 引用块 29 个（实得 {card.count('> ' + chr(34))}）")
for part in ("PART I", "PART II", "PART III", "PART IV", "PART V", "PART VI", "PART VII"):
    check(part in card, f"卡片覆盖 {part}")
check("ATTACHMENT A" in card, "卡片覆盖 ATTACHMENT A")
check("03847H" in card and "847H" in card, "卡片载明 PAC 分流")
check("10 ppb" in card and "20 ppb" in card, "卡片载明铅的 10/20 ppb 两档")
check("proposed action levels" in card, "卡片载明「拟议行动水平」性质")
check("7303.847" in card, "卡片使用正确 CP 号 7303.847")
check("No samples are to be collected" in card, "卡片载明进口商检查不取样")
check("60 days" in card, "卡片载明 60 天复检口径")

bad075 = 0
for ln in card.split("\n"):
    if "7303.047" in ln and not any(k in ln for k in ("误写", "曾把", "不得把")):
        bad075 += ln.count("7303.047")
check(bad075 == 0, f"卡片内 7303.047 仅出现在勘误说明（未说明处 {bad075}）")

meta = yaml.safe_load(META.read_text(encoding="utf-8"))
check(meta["slug"] == "juice-inspection-program", "meta slug 一致")
check(len(meta["keywords"]) >= 120, f"meta keywords ≥120（实得 {len(meta['keywords'])}）")
check(len(meta["intents"]) >= 40, f"meta intents ≥40（实得 {len(meta['intents'])}）")
check(len(set(meta["keywords"])) == len(meta["keywords"]), "meta keywords 无重复")
check(card.split("\n")[0].count("juice-inspection-program") == 1, "卡片标题含 slug")

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
