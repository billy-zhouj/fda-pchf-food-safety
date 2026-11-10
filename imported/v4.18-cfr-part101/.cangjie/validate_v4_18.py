#!/usr/bin/env python3
"""Phase 5 static registry + consistency validation for the v4.18 installed package."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

SKILL = Path(r"C:\Users\HG\.workbuddy\skills\fda-pchf-food-safety")
ROOT = Path(__file__).resolve().parents[1]

fails: list[str] = []
warns: list[str] = []


def check(cond: bool, msg: str) -> None:
    print(("  [OK] " if cond else "  [FAIL] ") + msg)
    if not cond:
        fails.append(msg)


def warn(cond: bool, msg: str) -> None:
    if not cond:
        print("  [WARN] " + msg)
        warns.append(msg)


print("=== 1. required files exist ===")
req = [
    "SKILL.md", "references/capability-index.md", "references/cheatsheet.md",
    "references/glossary.md", "references/overview.md", "test-prompts.json",
    "references/capabilities/food-labeling-requirements.md",
    "references/capabilities/labeling/labeling-architecture.md",
    "references/capabilities/labeling/nutrition-labeling-serving-size.md",
    "references/capabilities/labeling/claims-authorization-gates.md",
    "references/capabilities/labeling/specific-foods-warning-statements.md",
    "references/capabilities/labeling/labeling-exemptions-effect-level.md",
]
for r in req:
    check((SKILL / r).is_file(), f"exists: {r}")

print("\n=== 2. SKILL.md frontmatter & structure ===")
s = (SKILL / "SKILL.md").read_text(encoding="utf-8")
check("cangjie.capability-count: 30" in s, "frontmatter capability-count: 30")
check("v4.18" in s, "SKILL.md mentions v4.18")
check("57. **v4.18 新增第七套法规编号〔§ 101.xxx〕**" in s, "core principle #57 present")
check("| 判定 21 CFR Part 101 食品标签法定义务" in s, "route row for CAP-30 present")
check("food-labeling-requirements.md" in s, "route row points at entry card")
check(s.count("CAP-30") >= 3, f"CAP-30 referenced {s.count('CAP-30')} times")
check("二十二类不可混引" in s, "SKILL.md states 二十二类不可混引")
check("七套法规正文" in s, "SKILL.md states 七套法规正文")
check("二十一类不可混引" not in s, "no stale 二十一类不可混引 as current wording")
check("六套法规正文" not in s, "no stale 六套法规正文")
check("全包自 v4.18 起" in s, "boundary wording bumped to v4.18")

print("\n=== 3. capability-index ===")
idx = (SKILL / "references/capability-index.md").read_text(encoding="utf-8")
check(idx.count("| CAP-30 |") == 1, "index has exactly 1 CAP-30 row")
check(idx.count("| CAP-29 |") == 1, "index has exactly 1 CAP-29 row")
check("labeling/" in idx, "index CAP-30 row points at labeling subcards")

print("\n=== 4. cheatsheet ===")
cs = (SKILL / "references/cheatsheet.md").read_text(encoding="utf-8")
check(cs.count("21 CFR Part 101 食品标签法定义务与判定链") == 1, "cheatsheet has 1 CAP-30 row")

print("\n=== 5. glossary (strict YAML) ===")
g = (SKILL / "references" / "glossary.md").read_text(encoding="utf-8")
block = g.split("```yaml", 1)[1].split("\n```", 1)[0]
data = yaml.safe_load(block)
check(isinstance(data, list), "glossary yaml parses to list")
ids = [x["id"] for x in data]
check(len(ids) == 277, f"glossary has 277 entries (got {len(ids)})")
check(len(ids) == len(set(ids)), "glossary ids unique")
check(ids[-1] == "t277", f"last glossary id t277 (got {ids[-1]})")
part101 = [x for x in data if any(t in (x.get("tags") or []) for t in ("Part 101",))]
check(len(part101) == 44, f"44 Part 101 glossary entries (got {len(part101)})")
check(all(str(x.get("source_chapter", "")).startswith("21 CFR Part 101") for x in part101),
      "all Part 101 entries carry 21 CFR Part 101 source_chapter")

print("\n=== 6. test-prompts.json ===")
t = json.loads((SKILL / "test-prompts.json").read_text(encoding="utf-8"))
check(t["version"] == "4.18", f"version 4.18 (got {t['version']})")
check(len(t["test_cases"]) == 191, f"191 test cases (got {len(t['test_cases'])})")
p101 = [x for x in t["test_cases"] if str(x["id"]).startswith("part101-")]
check(len(p101) == 10, f"10 part101 test cases (got {len(p101)})")
types = {}
for x in p101:
    types[x["type"]] = types.get(x["type"], 0) + 1
print("      part101 case types:", types)
check(types.get("should_not_trigger", 0) >= 1, "has >=1 mutually-exclusive negative case")

print("\n=== 7. cross-file path integrity ===")
# collect references/... paths from SKILL.md and capability-index.md and the entry card
pat = re.compile(r"references/capabilities/[A-Za-z0-9_./-]+\.md")
seen: dict[str, set[str]] = {}
for fname in ["SKILL.md", "references/capability-index.md",
              "references/capabilities/food-labeling-requirements.md"]:
    txt = (SKILL / fname).read_text(encoding="utf-8")
    for m in pat.findall(txt):
        if "*" in m:
            continue
        seen.setdefault(m, set()).add(fname)
missing = []
for rel, srcs in sorted(seen.items()):
    if not (SKILL / rel).is_file():
        missing.append(f"{rel} (referenced by {','.join(sorted(srcs))})")
check(not missing, "every concrete capability path referenced exists")
for m in missing:
    print("        missing:", m)

print("\n=== 8. subcard self-registration ===")
lab = SKILL / "references" / "capabilities" / "labeling"
for p in sorted(lab.glob("*.md")):
    txt = p.read_text(encoding="utf-8")
    ok_hdr = "food-labeling-requirements.md" in txt.splitlines()[0]
    ok_six = all(f"## {k} —" in txt for k in ["R", "I", "A1", "A2", "E", "B"])
    print(f"      {p.name}: header={ok_hdr} six-sections={ok_six} lines={len(txt.splitlines())}")
    if not (ok_hdr and ok_six):
        fails.append(f"subcard structure: {p.name}")

print("\n=== 9. main card census ===")
caps = SKILL / "references" / "capabilities"
top = [p for p in caps.glob("*.md")]
imports = list((caps / "imports").glob("*.md")) if (caps / "imports").is_dir() else []
labeling = list(lab.glob("*.md"))
print(f"      top-level cards: {len(top)} | imports subcards: {len(imports)} | labeling subcards: {len(labeling)}")
check(len(top) == 30, f"30 top-level cards (got {len(top)})")

print("\n=== 10. audit artifacts ===")
for r in ["GLOSSARY.md", "DIGEST.md", "verified.md", "BOOK_OVERVIEW.md", "PIPELINE_STATE.md",
          "rejected/merged-duplicates.md", "test-results/phase4-cases.json",
          ".cangjie/capabilities/verified.yaml", ".cangjie/capabilities/destinations.json",
          ".cangjie/apply_v4_18_report.json"]:
    check((ROOT / r).is_file(), f"audit: {r}")

print("\n=== SUMMARY ===")
print(f"  FAILS: {len(fails)}   WARNS: {len(warns)}")
for f in fails:
    print("   -", f)
sys.exit(1 if fails else 0)
