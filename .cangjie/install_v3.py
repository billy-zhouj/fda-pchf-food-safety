#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 dist-v3 原子安装到用户级技能目录，安装前先备份旧版本。"""
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE = Path("E:/WeChatData/2026-11-04-09-51-05/books/fda-pchf-human-food-guidance")
SRC = BASE / "dist-v3"
DST = Path("C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety")
BACKUP_ROOT = BASE / "backups"

assert SRC.is_dir() and (SRC / "SKILL.md").exists(), "编译产物不存在"
assert DST.parent.is_dir(), "用户级技能根目录不存在"

# 1) 备份旧安装
BACKUP_ROOT.mkdir(exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup = BACKUP_ROOT / f"fda-pchf-food-safety-v2.1-{stamp}"
if DST.exists():
    shutil.copytree(DST, backup)
    print(f"旧版本已备份: {backup}")
else:
    print("首次安装，无需备份")

# 2) 覆盖安装（保留目录本身，逐文件覆盖；新增卡自然落入）
shutil.copytree(SRC, DST, dirs_exist_ok=True)
shutil.copyfile(BASE / "test-prompts.json", DST / "test-prompts.json")
print(f"已安装到: {DST}")

# 3) 校验
check = subprocess.run(
    [sys.executable,
     "C:/Users/HG/.workbuddy/skills/cangjie-skill/scripts/validate_skill_pack.py",
     str(DST)],
    capture_output=True, text=True)
print("--- 安装后官方校验 ---")
print(check.stdout.strip())
print("退出码:", check.returncode)

d = json.loads((DST / "test-prompts.json").read_text(encoding="utf-8"))
cards = sorted(p.name for p in (DST / "references/capabilities").glob("*.md"))
gloss = (DST / "references/glossary.md").read_text(encoding="utf-8")
print(f"能力卡 {len(cards)} 张 / 测试用例 {len(d['test_cases'])} 条(版本 {d['version']}) / 术语 {gloss.count('- id: t')} 条")
print("能力卡:", ", ".join(cards))
raise SystemExit(check.returncode)
