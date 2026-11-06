#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 dist-v11（v4.7，第十一/第十二来源 21 CFR Part 113 / 114 / CAP-20）原子安装到用户级技能目录，安装前先备份 v4.6。"""
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE = Path("E:/WeChatData/2026-11-04-09-51-05/books/fda-pchf-human-food-guidance")
SRC = BASE / "dist-v11"
DST = Path("C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety")
BACKUP_ROOT = BASE / "backups"
VALIDATOR = "C:/Users/HG/.workbuddy/skills/cangjie-skill/scripts/validate_skill_pack.py"

assert SRC.is_dir() and (SRC / "SKILL.md").exists(), "编译产物不存在"
assert DST.parent.is_dir(), "用户级技能根目录不存在"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


# 1) 备份旧安装（v4.6）
BACKUP_ROOT.mkdir(exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup = BACKUP_ROOT / f"fda-pchf-food-safety-v4.6-{stamp}"
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
print(f"能力卡 {len(cards)} 张 / 测试用例 {len(d['test_cases'])} 条(版本 {d['version']}) / 术语 {gloss.count('- id: t')} 条")
print("CAP-20 lacf-statutory-requirements 路由命中:", skill.count("lacf-statutory-requirements"))
print("十二类不可混引命中:", skill.count("十二类") + overview.count("十二类"))
print("十类旧口径残留(SKILL):", skill.count("十类不可混引"))
print("第十一/十二来源登记:", "第十一与第十二来源" in overview, "第十二来源" in overview)
print("Part 110 纠错登记:", "Part 110 至今有效" in skill or "Part 110 至今有效" in overview)
print("113/114 条款标注:", "113.xxx" in skill, "114.xxx" in skill)
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

ok = check.returncode == 0 and len(cards) == 20 and len(d["test_cases"]) == 85 and not diffs
print("安装结果:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
