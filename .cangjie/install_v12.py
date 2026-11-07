#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""install_v12.py — 把 dist-v16（v4.12，第十七来源 21 CFR Part 108 / CAP-25）安装到工作区级技能目录。

与 install_v11.py 的差别：
- SRC 换成 dist-v16；备份标签 v4.11。
- 指标改为 25 卡 / 202 术语 / 135 用例 / version 4.12 / 十七类 / CAP-25。
- 新增两条断言：CAP-25 的 27 个引用块、以及 SKILL.md 里「十六类」旧口径必须为 0。
- 其余（路径推导、逐文件 hash 对比、5 份 glossary 副本一致性、严格 YAML）沿用 v4.11。
"""
import hashlib
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
WORKSPACE = BASE.parent
SRC = BASE / "dist-v16"
DST = WORKSPACE / ".workbuddy/skills/fda-pchf-food-safety"
BACKUP_ROOT = WORKSPACE / ".workbuddy/skills/backups"
VALIDATOR = Path.home() / ".workbuddy/skills/cangjie-skill/scripts/validate_skill_pack.py"

assert SRC.is_dir() and (SRC / "SKILL.md").exists(), "编译产物不存在"
assert DST.is_dir(), "工作区级技能安装目录不存在"
assert VALIDATOR.is_file(), f"官方校验脚本不存在: {VALIDATOR}"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


# 1) 备份旧安装（v4.11）
BACKUP_ROOT.mkdir(parents=True, exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup = BACKUP_ROOT / f"fda-pchf-food-safety-v4.11-{stamp}"
shutil.copytree(DST, backup)
print(f"旧版本已备份: {backup}")

# 2) 覆盖安装
shutil.copytree(SRC, DST, dirs_exist_ok=True)
print(f"已安装到: {DST}")

# 3) 安装后官方校验
check = subprocess.run([sys.executable, str(VALIDATOR), str(DST)],
                       capture_output=True, text=True)
print("--- 安装后官方校验 ---")
print(check.stdout.strip())
if check.stderr.strip():
    print("stderr:", check.stderr.strip())
print("退出码:", check.returncode)

# 4) 关键指标
cards = sorted(p.name for p in (DST / "references/capabilities").glob("*.md"))
gloss = (DST / "references/glossary.md").read_text(encoding="utf-8")
skill = (DST / "SKILL.md").read_text(encoding="utf-8")
overview = (DST / "references/overview.md").read_text(encoding="utf-8")
index = (DST / "references/capability-index.md").read_text(encoding="utf-8")
cheat = (DST / "references/cheatsheet.md").read_text(encoding="utf-8")
card25 = (DST / "references/capabilities/emergency-permit-control.md").read_text(encoding="utf-8")
term_count = len(re.findall(r"^\s*- id: t\d+", gloss, re.M))
print(f"能力卡 {len(cards)} 张 / 术语 {term_count} 条")
print("CAP-25 slug 命中（SKILL / index / cheatsheet）:",
      skill.count("emergency-permit-control"),
      index.count("emergency-permit-control"),
      cheat.count("emergency-permit-control"))
print("十七类出现（SKILL / overview）:", skill.count("十七类"), overview.count("十七类"))
print("十六类旧口径剩余（SKILL）:", skill.count("十六类"))
print("CAP-25 引用块:", card25.count('> "'), "| 含 108.25/108.35:",
      "108.25" in card25 and "108.35" in card25)

# 5) 逐文件 hash 对比
diffs = []
for p in sorted(SRC.rglob("*")):
    if not p.is_file():
        continue
    rel = p.relative_to(SRC)
    q = DST / rel
    if not q.exists():
        diffs.append(f"missing {rel}")
    elif sha(p) != sha(q):
        diffs.append(f"hash mismatch {rel}")
print("files:",
      len([p for p in SRC.rglob('*') if p.is_file()]), "/",
      len([p for p in DST.rglob('*') if p.is_file()]),
      "| 产物与安装目录逐文件 hash 差异:", len(diffs))
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
    strict_ok = isinstance(g, list) and len(g) == 202 and len({x["id"] for x in g}) == 202
    print(f"安装目录 glossary 严格解析: {'OK' if strict_ok else 'FAIL'} ({len(g) if isinstance(g, list) else 'n/a'} 条)")
except Exception as exc:
    strict_ok = False
    print("安装目录 glossary 严格解析: FAIL", exc)

ok = (
    check.returncode == 0
    and "0 errors, 0 warnings" in check.stdout
    and len(cards) == 25
    and term_count == 202
    and not diffs
    and len(set(ghashes.values())) == 1
    and strict_ok
    and "emergency-permit-control" in skill
    and "emergency-permit-control" in index
    and skill.count("十六类") == 0
    and card25.count('> "') == 27
)
print("安装结果:", "PASS" if ok else "FAIL")
if ok:
    print("FINAL_INSTALL_OK")
raise SystemExit(0 if ok else 1)
