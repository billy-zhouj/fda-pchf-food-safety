"""check_v4_16_routing.py — v4.16 静态登记核对（不发请求、不调模型）

核对项：
 1. Bundle 规模：28 卡 / 56 principles / 30 stops / 19 additional_sources（末条 IOM Ch.4）
 2. CAP-28 身份：iom-sampling-procedure / active / extended / also_read 12 条
 3. 双向辅读链：CAP-28 正向 12 条、反向 13 张卡
 4. 产物：能力索引主行 1 行、SKILL.md 无「十九类」残留且含「二十类」、
          overview 含 v4.16 节、glossary 233 条、33 个 .md
 5. 卡片：60 个引用块、RIA++ 六段齐全、4.1–4.7 七节、六类反直觉锚点、
          Chart 2 与 4.40/4.65/4.75 两层不得混引、转换件四处红线
 6. meta：slug / 85 intents / 170 keywords / 无重复 / 标题含 slug
 7. 来源与事实源：source 文件头、转换报告 361/361 书签、术语 233 条严格解析
 8. 测试套件：168 条 / version 4.16 / 10 条 iom-sampling-*
 9. 文档：BOOK_OVERVIEW / DIGEST / PIPELINE_STATE 的 v4.16 当前态
10. 产物 == 安装目录：逐文件 sha256 差异 0；glossary 五副本 hash 一致
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parents[1]
BUNDLE = BASE / ".cangjie/capabilities/verified.yaml"
DIST = BASE / "dist-v20"
INST = Path.home() / ".workbuddy/skills/fda-pchf-food-safety"
CARD = BASE / ".cangjie/capabilities/cards/iom-sampling-procedure.md"
META = BASE / ".cangjie/capabilities/cards/_meta-iom-sampling-procedure.yaml"
SRC_MD = BASE / "source-iom-ch4-2026.md"
SRC_REPORT = BASE / ".cangjie/iom-ch4-convert-report.json"

results: list[tuple[bool, str]] = []


def check(cond: bool, msg: str) -> None:
    results.append((bool(cond), msg))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


b = yaml.safe_load(BUNDLE.read_text(encoding="utf-8"))
caps = b["capabilities"]
entry = b["entry"]
by_slug = {c["slug"]: c for c in caps}

# ── 1. Bundle 规模 ──────────────────────────────────────────────────────
check(len(caps) == 28, f"能力卡 28 张（实得 {len(caps)}）")
check(len(entry["core_principles"]) == 56,
      f"core_principles 56 条（实得 {len(entry['core_principles'])}）")
check(len(entry["stop_conditions"]) == 30,
      f"stop_conditions 30 条（实得 {len(entry['stop_conditions'])}）")
srcs = b["book"]["additional_sources"]
check(len(srcs) == 19, f"additional_sources 19 条（实得 {len(srcs)}）")
check(srcs[-1]["source_id"] == "src-fda-iom-ch4-2026",
      f"末条来源为 IOM Ch.4（实得 {srcs[-1]['source_id']}）")
check(srcs[-1]["source_file"] == "source-iom-ch4-2026.md", "末条来源文件登记正确")
check("IOM 2026 Chapter 4" in " ".join(entry["core_principles"]),
      "core_principles 载明 IOM Ch.4 已收为第二十来源")
check(any("IOM" in s and "4" in s for s in entry["stop_conditions"]),
      "stop_conditions 载明 IOM Ch.4 引用规范")

# ── 2. CAP-28 身份 ──────────────────────────────────────────────────────
c28 = by_slug.get("iom-sampling-procedure")
check(c28 is not None, "CAP-28 已登记")
if c28:
    check(c28["capability_id"] == "CAP-28", f"编号为 CAP-28（实得 {c28['capability_id']}）")
    check(c28.get("status", "active") == "active", "status = active")
    check(c28["importance"] == "extended", f"importance = extended（实得 {c28['importance']}）")
    check(len(c28["also_read"]) == 12, f"also_read 12 条（实得 {len(c28['also_read'])}）")
    need = {"inspection-sampling", "investigator-authority-procedure", "inspection-readiness",
            "lacf-inspection-program", "lacf-statutory-requirements",
            "environmental-pathogen-sanitation", "regulatory-boundaries"}
    check(need <= set(c28["also_read"]), "also_read 覆盖 CAP-17/18/16/19/20/04/09")
    back = [s for s, x in by_slug.items()
            if s != "iom-sampling-procedure" and "iom-sampling-procedure" in x["also_read"]]
    check(len(back) == 13, f"反向辅读链 13 张（实得 {len(back)}）")

# ── 3. 产物 ─────────────────────────────────────────────────────────────
skill = (DIST / "SKILL.md").read_text(encoding="utf-8")
index = (DIST / "references/capability-index.md").read_text(encoding="utf-8")
overview = (DIST / "references/overview.md").read_text(encoding="utf-8")
gloss = (DIST / "references/glossary.md").read_text(encoding="utf-8")
cheatsheet = (DIST / "references/cheatsheet.md").read_text(encoding="utf-8")
md_files = sorted(p for p in DIST.rglob("*.md"))
check(len(md_files) == 33, f"产物 33 个 .md（实得 {len(md_files)}）")
check((DIST / "references/capabilities/iom-sampling-procedure.md").is_file(), "产物含 CAP-28 卡片")
check(skill.count("iom-sampling-procedure") >= 1, "SKILL.md 含 CAP-28 slug")
check(skill.count("十九类") == 0, f"SKILL.md 无「十九类」残留（实得 {skill.count('十九类')}）")
check("二十类" in skill, "SKILL.md 含「二十类」口径")
check(index.count("iom-sampling-procedure") == 1,
      f"能力索引主行 1 行（实得 {index.count('iom-sampling-procedure')}）")
check("## v4.16 追加" in overview, "产物 overview 含 v4.16 增量节")
check("FDA 取样全流程作业程序（IOM 2026 Chapter 4）" in cheatsheet,
      "cheatsheet 含 CAP-28 决策规则行")
term_count = len(re.findall(r"^\s*- id: t\d+", gloss, re.M))
check(term_count == 233, f"产物 glossary 233 条（实得 {term_count}）")
check("- id: t224" in gloss and "- id: t233" in gloss, "产物 glossary 含 t224–t233")
check(sha(DIST / "references/glossary.md") == sha(BASE / "candidates/glossary.md"),
      "产物 glossary == candidates/glossary.md")
check(sha(DIST / "references/overview.md") == sha(BASE / "BOOK_OVERVIEW.md"),
      "产物 overview == BOOK_OVERVIEW.md")

# ── 4. CAP-28 卡片 ──────────────────────────────────────────────────────
card = CARD.read_text(encoding="utf-8")
check(card.count('> "') == 60, f"CAP-28 引用块 60 个（实得 {card.count('> ' + chr(34))}）")
for seg in ("## R — 原文", "## I — 自述", "## A1 — 书中案例",
            "## A2 — 未来触发", "## E — 执行要点", "## B — 边界"):
    check(seg in card, f"卡片含 {seg}")
for i in range(1, 8):
    check(f"4.{i}" in card, f"卡片覆盖 IOM 4.{i}")
anchors = {
    "DOC 不是记录复印件": "A DOC sample is not a sample of records",
    "DOC 不发 484": "Because no product is collected, a Form FDA 484",
    "INV 不是 official": "Investigational (INV) samples are _not_ official samples",
    "INV 仍须封条": "must be sealed",
    "702(b) 污秽反向例外": "Note regarding filth samples",
    "Salmonella ≥100 子样": "at least 100 swabs/subs",
    "Listeria ≥50 子样": "at least 50 swabs/subs",
    "环境取样不得预告": "not to mention FDA's intent to collect environmental samples",
    "D/E 中和液": "Dey-Engley",
    "24 小时到实验室": "24 hours",
    "Chart 2": "Sample Schedule Chart 2",
    "704(d)": "704(d)",
    "FDA 483": "FDA 483",
    "转换件表单占位": "picture intentionally omitted",
    "转换件点线目录": "点线目录",
}
for label, needle in anchors.items():
    check(needle in card, f"卡片载明「{label}」")
check("4.40" in card and "4.65" in card and "4.75" in card,
      "卡片载明 CP 7303.070 三条实验室触发线")
check("两层" in card or "不得混" in card, "卡片钉死 Chart 2 与触发线分属两层")
check("不创设企业义务" in card, "卡片声明检查程序不创设企业义务")
check(card.split("\n")[0].count("iom-sampling-procedure") == 1, "卡片标题含 slug")

# ── 5. meta ─────────────────────────────────────────────────────────────
meta = yaml.safe_load(META.read_text(encoding="utf-8"))
check(meta["slug"] == "iom-sampling-procedure", "meta slug 一致")
check(len(meta["intents"]) == 85, f"meta intents 85 条（实得 {len(meta['intents'])}）")
check(len(meta["keywords"]) == 170, f"meta keywords 170 条（实得 {len(meta['keywords'])}）")
check(len(set(meta["keywords"])) == len(meta["keywords"]), "meta keywords 无重复")
check("IOM Chapter 2" in meta["source_label"], "meta 保留「仍未收 IOM Ch.2/3/6…」边界")

# ── 6. 来源与事实源 ─────────────────────────────────────────────────────
check(SRC_MD.is_file(), "source-iom-ch4-2026.md 存在")
src_head = SRC_MD.read_text(encoding="utf-8")[:8000]
check("效力层级与使用边界" in src_head and "转换局限" in src_head,
      "source 文件头含效力层级 / 转换局限说明块")
check(SRC_REPORT.is_file(), "转换自检报告存在")
rep = json.loads(SRC_REPORT.read_text(encoding="utf-8"))
check(rep.get("bookmarks_used") == 361 and rep.get("bookmarks_dropped") == 0,
      f"转换报告 361 书签全用 / 0 丢弃（实得 used={rep.get('bookmarks_used')}, dropped={rep.get('bookmarks_dropped')}）")
check(rep.get("total_headings") == 405 and rep.get("table_lines") == 345,
      "转换报告 405 标题 / 345 行表格")
g = yaml.safe_load(re.search(r"```ya?ml\n(.*?)\n```", gloss, re.S).group(1))
check(isinstance(g, list) and len(g) == 233 and len({x["id"] for x in g}) == 233,
      "glossary 严格 YAML 解析 233 条 id 唯一")

# ── 7. 测试套件 ─────────────────────────────────────────────────────────
d = json.loads((BASE / "test-prompts.json").read_text(encoding="utf-8"))
check(d["version"] == "4.16", f"测试套件 version 4.16（实得 {d['version']}）")
check(len(d["test_cases"]) == 168, f"测试用例 168 条（实得 {len(d['test_cases'])}）")
check(len({c["id"] for c in d["test_cases"]}) == 168, "测试用例 id 唯一")
check(sum(1 for c in d["test_cases"] if c["id"].startswith("iom-sampling-")) == 10,
      "iom-sampling-* 用例 10 条")
check("v4.16 追加 10 条" in d["notes"], "测试套件 notes 含 v4.16 尾注")

# ── 8. 文档当前态 ───────────────────────────────────────────────────────
for name, marker in (("BOOK_OVERVIEW.md", "## v4.16 追加"),
                     ("DIGEST.md", "版本说明（v4.16"),
                     ("PIPELINE_STATE.md", "## v4.16 —")):
    t = (BASE / name).read_text(encoding="utf-8")
    check(marker in t, f"{name} 含 v4.16 增量节")
check("**当前版本**: v4.16" in (BASE / "PIPELINE_STATE.md").read_text(encoding="utf-8"),
      "PIPELINE_STATE 顶部当前版本 = v4.16")
check("当前为 **v4.16：28 张能力卡" in (BASE / "DIGEST.md").read_text(encoding="utf-8"),
      "DIGEST 当前态 = v4.16 / 28 卡")

# ── 9. 产物 == 安装目录 ─────────────────────────────────────────────────
diffs = []
if INST.is_dir():
    for p in sorted(DIST.rglob("*")):
        if p.is_file():
            q = INST / p.relative_to(DIST)
            if not q.exists() or sha(p) != sha(q):
                diffs.append(str(p.relative_to(DIST)))
check(INST.is_dir(), "用户级安装目录存在")
check(not diffs, f"产物与安装目录 hash 差异 0（实得 {len(diffs)}: {diffs[:5]}）")
gpaths = [BASE / "candidates/glossary.md", BASE / "GLOSSARY.md",
          BASE / ".cangjie/capabilities/book/glossary.md",
          DIST / "references/glossary.md", INST / "references/glossary.md"]
ghashes = [sha(p) for p in gpaths if p.exists()]
check(len(ghashes) == 5 and len(set(ghashes)) == 1,
      f"glossary 五副本 hash 一致（实得 {len(ghashes)} 份 / {len(set(ghashes))} 种）")

passed = sum(1 for ok, _ in results if ok)
for ok, msg in results:
    print(("PASS  " if ok else "FAIL  ") + msg)
print(f"\n{passed}/{len(results)} PASS")
if passed != len(results):
    raise SystemExit(1)
print("RESULT: PASS")
