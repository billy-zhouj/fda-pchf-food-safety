#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 dist-v3 原子安装到用户级技能目录，安装前先备份旧版本。"""


# ⛔ DEPRECATED (2026-11-10 v4.19 收口)：本脚本属旧构建链 / 旧版安装器，禁止日常执行。
#    当前权威产物 = dist-v21 (v4.19)；安装只走 install_v18.py。
#    误跑后果：assemble_bundle.py 会用 v4.16 的 28 卡数据覆盖 .cangjie/capabilities/ 的
#    verified.yaml + destinations.json + book/；install_vN.py (N<=17) 会把用户级已装技能
#    回退到 v4.9~v4.16 的旧版。详见 .cangjie/README.md。
#    仅「路线 A 全量移植」工作可设 ALLOW_DEPRECATED_CANGJIE=1 强制执行。
import os as _os, sys as _sys
if not _os.environ.get("ALLOW_DEPRECATED_CANGJIE"):
    _sys.stderr.write("DEPRECATED: " + __file__.replace("\\", "/").rsplit("/", 1)[-1] + " — 旧构建链/旧版安装器已弃用，禁止执行。详见 .cangjie/README.md。如确需强跑（仅路线 A），先 export ALLOW_DEPRECATED_CANGJIE=1")
    _sys.exit(2)
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
