#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 dist-v13（v4.9，第十四来源 21 CFR Part 123 / CAP-22）原子安装到用户级技能目录，安装前先备份 v4.8。"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE = Path("E:/WeChatData/2026-11-04-09-51-05/books/fda-pchf-human-food-guidance")
SRC = BASE / "dist-v13"
DST = Path("C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety")
BACKUP_ROOT = BASE / "backups"
VALIDATOR = "C:/Users/HG/.workbuddy/skills/cangjie-skill/scripts/validate_skill_pack.py"

assert SRC.is_dir() and (SRC / "SKILL.md").exists(), "编译产物不存在"
assert DST.parent.is_dir(), "用户级技能根目录不存在"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


# 1) 备份旧安装（v4.8）
BACKUP_ROOT.mkdir(exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup = BACKUP_ROOT / f"fda-pchf-food-safety-v4.8-{stamp}"
if DST.exists():
    shutil.copytree(DST, backup)
    print(f"旧版本已备份: {backup}")
else:
    print("首次安装，无需备份")

# 2) 覆盖安装（保留目录本身，逐文件覆盖；新增卡自然落入）
shutil.copytree(SRC, DST, dirs_exist_ok=True)
shutil.copyfile(BASE / "test-prompts.json", DST / "test-prompts.json")
print(f"已安装到: {DST}")

# 3) 官方校验
check = subprocess.run([sys.executable, VALIDATOR, str(DST)], capture_output=True, text=True)
print("--- 安装后官方校验 ---")
print(check.stdout.strip())
if check.stderr.strip():
    print("stderr:", check.stderr.strip())
print("退出码:", check.returncode)

# 4) 关键指标核对
d = json.loads((DST / "test-prompts.json").read_text(encoding="utf-8"))
cards = sorted(p.name for p in (DST / "references/capabilities").glob("*.md"))
gloss = (DST / "references/glossary.md").read_text(encoding="utf-8")
skill = (DST / "SKILL.md").read_text(encoding="utf-8")
overview = (DST / "references/overview.md").read_text(encoding="utf-8")
index = (DST / "references/capability-index.md").read_text(encoding="utf-8")
term_count = len(re.findall(r"^\s*- id: t\d+", gloss, re.M))
seafood_card = (DST / "references/capabilities/seafood-haccp-statutory-requirements.md").read_text(encoding="utf-8")
print(f"能力卡 {len(cards)} 张 / 测试用例 {len(d['test_cases'])} 条(版本 {d['version']}) / 术语 {term_count} 条")
print("CAP-22 seafood-haccp 路由命中:", skill.count("seafood-haccp-statutory-requirements") + index.count("seafood-haccp-statutory-requirements"))
print("十四类不可混引命中(SKILL+overview):", skill.count("十四类") + overview.count("十四类"))
print("十三类旧口径剩余(SKILL):", skill.count("十三类"))
print("第十四来源登记:", "第十四来源" in overview or "Part 123" in overview, "| 123.5(a) in card:", "123.5(a)" in seafood_card)
print("Part 123 引用规范:", "〔§ 123." in skill or "〔§ 123." in overview)
print("CP 7303.842 未收声明:", "7303.842" in seafood_card)
print("能力卡:", ", ".join(cards))

# 5) 逐文件 hash 对比（产物 == 安装目录）
extra = {"test-prompts.json"}  # 由安装脚本单独拷入，不在编译产物中
diffs = []
for p in sorted(SRC.rglob("*")):
    if not p.is_file():
        continue
    rel = p.relative_to(SRC)
    q = DST / rel
    if not q.exists():
        diffs.append(f"missing {rel}")
    elif sha(p) != sha(q) and str(rel) not in extra:
        diffs.append(f"hash mismatch {rel}")
print("产物与安装目录逐文件 hash 差异:", len(diffs))
for x in diffs[:10]:
    print("  ", x)

# 6) 5 份 glossary 副本一致性
gpaths = [
    BASE / "candidates/glossary.md",
    BASE / "GLOSSARY.md",
    BASE / ".cangjie/capabilities/book/glossary.md",
    SRC / "references/glossary.md",
    DST / "references/glossary.md",
]
ghashes = {str(p): sha(p) for p in gpaths}
print("glossary 副本数:", len(ghashes), "唯一 hash 数:", len(set(ghashes.values())))
for p, h in ghashes.items():
    print("  ", h[:16], p)

# 7) 安装目录 glossary 严格 YAML 解析
try:
    import yaml
    g = yaml.safe_load(re.search(r"```ya?ml\n(.*?)\n```", gloss, re.S).group(1))
    strict_ok = isinstance(g, list) and len(g) == 172 and len({x["id"] for x in g}) == 172
    print(f"安装目录 glossary 严格解析: {'OK' if strict_ok else 'FAIL'} ({len(g) if isinstance(g, list) else 'n/a'} 条)")
except Exception as exc:  # pragma: no cover
    strict_ok = False
    print("安装目录 glossary 严格解析: FAIL", exc)

ok = (
    check.returncode == 0
    and "0 errors, 0 warnings" in check.stdout
    and len(cards) == 22
    and len(d["test_cases"]) == 105
    and d["version"] == "4.9"
    and term_count == 172
    and not diffs
    and len(set(ghashes.values())) == 1
    and strict_ok
)
print("安装结果:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
