#!/usr/bin/env python3
"""阶段 5 静态校验 — fda-pchf-food-safety v4.18 → v4.19（新增 CAP-31 21 CFR Part 172）

检查 10 组不变量：
  G1  安装文件存在与计数（入口卡 / 5 子卡 / 术语块 / 测试用例）
  G2  SKILL.md frontmatter（capability-count=31）与版本口径
  G3  SKILL.md 描述块含 CAP-31 段
  G4  核心原则 #58 存在且含八套编号与三条元规则
  G5  路由表含 CAP-31 行且指向 additives/
  G6  全局计数一致性（八套编号 / 二十三类不可混引 / 31 张能力卡）
  G7  纪律段含 Part 172 分流规则（v4.19 起已收）
  G8  capability-index.md / cheatsheet.md / overview.md 已更新
  G9  glossary.md YAML 块 t01–t318 连续、318 条、tags 含 Part 172
  G10 test-prompts.json version=4.19、204 条、含 part172-01..13
  G11 destinations.json 与 verified.yaml 一致且卡片路径全部落地
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

try:
    import yaml
except Exception:
    yaml = None

SKILL = Path.home() / ".workbuddy" / "skills" / "fda-pchf-food-safety"
AUDIT = Path("E:/WeChatData/2026-11-09-15-05-22/books/cfr-part172-2026")

fails: list[str] = []
warns: list[str] = []
def chk(cond, msg, warn=False):
    if cond:
        return True
    (warns if warn else fails).append(msg)
    return False

# ---------- G1 文件存在 ----------
entry = SKILL / "references/capabilities/direct-food-additives.md"
subs = ["permission-gate-limitation-forms", "preservatives-antimicrobials",
        "sweeteners-fat-substitutes", "quality-functionals-longtail-index",
        "effect-level-ibr-boundary"]
chk(entry.is_file(), "G1 缺入口卡 direct-food-additives.md")
for s in subs:
    f = SKILL / "references/capabilities/additives" / f"{s}.md"
    chk(f.is_file(), f"G1 缺子卡 additives/{s}.md")
    if f.is_file():
        t = f.read_text(encoding="utf-8")
        for sec in ["## R — 原文", "## I — 自述", "## A1 — ", "## A2 — ", "## E — ", "## B — "]:
            chk(sec in t, f"G1 {s}.md 缺章节 {sec.strip()}")

# ---------- G2 SKILL.md frontmatter ----------
skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
chk("cangjie.capability-count: 31" in skill, "G2 capability-count 不是 31")
chk("cangjie.entrypoint-count: 1" in skill, "G2 entrypoint-count 不是 1")

# ---------- G3 描述块 ----------
chk("v4.19 新增 CAP-31 `direct-food-additives`" in skill, "G3 描述块缺 CAP-31 段")

# ---------- G4 核心原则 #58 ----------
chk("58. **v4.19 新增第八套法规编号〔§ 172.xxx〕**" in skill, "G4 缺核心原则 #58")
chk("§172.5 三条元规则" in skill and "有条款 ≠ 有剂量上限" in skill, "G4 #58 缺三条元规则/五形态口径")

# ---------- G5 路由表 ----------
chk("| 判定 21 CFR Part 172 直接食品添加剂许可与限量/规格" in skill, "G5 路由表缺 CAP-31 行")
chk("references/capabilities/direct-food-additives.md" in skill, "G5 路由表未指向入口卡")
chk("references/capabilities/additives/*.md（5 张子卡" in skill, "G5 路由表未指向 additives/ 子卡")

# ---------- G6 全局计数 ----------
chk("八套法规正文〔§ 101.xxx〕〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕〔§ 172.xxx〕" in skill,
    "G6 原则 #37 未更新为八套编号")
chk("合计**二十三类不可混引**" in skill, "G6 原则 #37 未更新为二十三类")
chk("与〔§ 101/108/113/114/117/120/123.xxx〕并列共**八套独立编号**" in skill, "G6 #58 未写八套编号列表")
chk("超出 31 张能力卡路由范围" in skill, "G6 未更新为 31 张能力卡")
chk("八套法规正文分别以" in skill and "〔§ 172.xxx〕标注" in skill, "G6 条款引用纪律未含〔§ 172.xxx〕")
chk("21 CFR Part 172 自 v4.19 起已收，见 CAP-31" in skill, "G6 二十三类不可混引未标注 Part 172")

# ---------- G7 纪律段 ----------
chk("**21 CFR Part 172 法规正文自 v4.19 起已收**" in skill, "G7 缺 Part 172 纪律段")
chk("绝不转述其内部数值" in skill and "FCC 7th ed.=2010 / 9th ed.=2014" in skill, "G7 纪律段缺 IBR 边界口径")
chk("添加剂被许可 ≠ 产品安全合规" in skill, "G7 纪律段缺许可≠安全红线")

# ---------- G8 索引文件 ----------
ci = (SKILL / "references/capability-index.md").read_text(encoding="utf-8")
cs = (SKILL / "references/cheatsheet.md").read_text(encoding="utf-8")
ov = (SKILL / "references/overview.md").read_text(encoding="utf-8")
chk("| CAP-31 | 21 CFR Part 172" in ci, "G8 capability-index 缺 CAP-31 行")
chk("capabilities/direct-food-additives.md（+ additives/ 下 5 张子卡）" in ci, "G8 capability-index 路径错")
chk("21 CFR Part 172 直接食品添加剂许可、限量与规格判定链" in cs, "G8 cheatsheet 缺 CAP-31 行")
chk("## v4.19 追加：第二十三来源 21 CFR Part 172" in ov, "G8 overview 缺 v4.19 区块")
chk("**31 张主卡 + 10 张 imports 子卡 + 5 张 labeling 子卡 + 5 张 additives 子卡" in ov, "G8 overview 规模数错")
chk("318 条术语（YAML 块 t01–t318）" in ov and "204 条测试用例" in ov, "G8 overview 术语/用例数错")

# ---------- G9 glossary ----------
gl = (SKILL / "references/glossary.md").read_text(encoding="utf-8")
chk(yaml is not None, "G9 无 pyyaml，跳过 YAML 解析", warn=True)
if yaml is not None:
    block = gl.split("```yaml", 1)[1].split("```", 1)[0]
    try:
        terms = yaml.safe_load(block)
        chk(isinstance(terms, list), "G9 glossary YAML 根不是 list")
        chk(len(terms) == 318, f"G9 glossary 条数 {len(terms)} ≠ 318")
        ids = [t["id"] for t in terms]
        chk(ids[0] == "t01" and ids[-1] == "t318", f"G9 id 边界 {ids[0]}..{ids[-1]}")
        expect = ["t%02d" % i if i < 100 else "t%d" % i for i in range(1, 319)]
        chk(ids == expect, "G9 id 不连续 t01..t318")
        t318 = [t for t in terms if t["id"] == "t318"][0]
        chk("Part 172" in t318.get("tags", []), "G9 t318 tags 缺 Part 172")
        chk("v4.19" in t318.get("tags", []), "G9 t318 tags 缺 v4.19")
    except Exception as e:
        chk(False, f"G9 glossary YAML 解析失败: {e}")
chk("## v4.19 增量术语 — 21 CFR Part 172" in gl, "G9 glossary 缺 v4.19 增量表")

# ---------- G10 test-prompts ----------
tp = json.loads((SKILL / "test-prompts.json").read_text(encoding="utf-8"))
chk(tp["version"] == "4.19", f"G10 version {tp['version']} ≠ 4.19")
chk(len(tp["test_cases"]) == 204, f"G10 用例数 {len(tp['test_cases'])} ≠ 204")
ids = {c["id"] for c in tp["test_cases"]}
p172 = {f"part172-{i:02d}" for i in range(1, 14)}
chk(p172 <= ids, f"G10 缺 part172 用例: {sorted(p172 - ids)}")
chk("21 CFR Part 172" in tp["source_book"], "G10 source_book 未追加 Part 172")
chk(tp.get("minimum_pass_rate") == 0.8, "G10 minimum_pass_rate ≠ 0.8")

# ---------- G11 destinations / verified.yaml ----------
dj = json.loads((AUDIT / ".cangjie/capabilities/destinations.json").read_text(encoding="utf-8"))
vy = yaml.safe_load((AUDIT / ".cangjie/capabilities/verified.yaml").read_text(encoding="utf-8")) if yaml else None
chk(dj["router_entry"]["name"] == "CAP-31", "G11 router_entry ≠ CAP-31")
chk(len(dj["destinations"]) == 5, "G11 destinations ≠ 5")
for d in dj["destinations"]:
    card = d["card"]
    # card path is relative to skill root ("references/capabilities/...")
    chk((SKILL / card).is_file(), f"G11 卡片未落地: {card}")
    chk(d["served_by"] == "CAP-31", f"G11 {d['capability_id']} served_by ≠ CAP-31")
if vy is not None:
    chk(len(vy["capabilities"]) == 5, "G11 verified.yaml ≠ 5 能力")
    chk({c["capability_id"] for c in vy["capabilities"]} == {d["capability_id"] for d in dj["destinations"]},
        "G11 destinations 与 verified.yaml 能力 id 不一致")

# ---------- 汇总 ----------
print(f"安装目录: {SKILL}")
print(f"FAILS: {len(fails)} / WARNS: {len(warns)}")
for m in fails:
    print("  FAIL", m)
for m in warns:
    print("  WARN", m)
print("RESULT:", "PASS" if not fails else "FAIL")
sys.exit(0 if not fails else 1)
