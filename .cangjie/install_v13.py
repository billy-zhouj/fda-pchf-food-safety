#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""install_v13.py — 把 dist-v17（v4.13，第十八来源 21 CFR Part 120 / CAP-26）安装到工作区级技能目录。

与 install_v12.py 的差别：
- SRC 换成 dist-v17；备份标签 v4.12。
- 指标改为 26 卡 / 212 术语 / 145 用例 / version 4.13 / 十八类 / CAP-26。
- 断言改为：CAP-26 的 26 个引用块、SKILL.md 里「十七类」旧口径必须为 0。
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
SRC = BASE / "dist-v17"
DST = WORKSPACE / ".workbuddy/skills/fda-pchf-food-safety"
BACKUP_ROOT = WORKSPACE / ".workbuddy/skills/backups"
VALIDATOR = Path.home() / ".workbuddy/skills/cangjie-skill/scripts/validate_skill_pack.py"

assert SRC.is_dir() and (SRC / "SKILL.md").exists(), "编译产物不存在"
assert DST.is_dir(), "工作区级技能安装目录不存在"
assert VALIDATOR.is_file(), f"官方校验脚本不存在: {VALIDATOR}"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


# 1) 备份旧安装（v4.12）
BACKUP_ROOT.mkdir(parents=True, exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup = BACKUP_ROOT / f"fda-pchf-food-safety-v4.12-{stamp}"
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
card26 = (DST / "references/capabilities/juice-haccp.md").read_text(encoding="utf-8")
term_count = len(re.findall(r"^\s*- id: t\d+", gloss, re.M))
print(f"能力卡 {len(cards)} 张 / 术语 {term_count} 条")
print("CAP-26 slug 命中（SKILL / index）:",
      skill.count("juice-haccp"), index.count("juice-haccp"))
print("十八类出现（SKILL / overview）:", skill.count("十八类"), overview.count("十八类"))
print("十七类旧口径剩余（SKILL）:", skill.count("十七类"))
print("CAP-26 引用块:", card26.count('> "'),
      "| 含 120.24/120.25:", "120.24" in card26 and "120.25" in card26)

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
    strict_ok = (isinstance(g, list) and len(g) == 212
                 and len({x["id"] for x in g}) == 212)
    print(f"安装目录 glossary 严格解析: {'OK' if strict_ok else 'FAIL'} "
          f"({len(g) if isinstance(g, list) else 'n/a'} 条)")
except Exception as exc:
    strict_ok = False
    print("安装目录 glossary 严格解析: FAIL", exc)

ok = (
    check.returncode == 0
    and "0 errors, 0 warnings" in check.stdout
    and len(cards) == 26
    and term_count == 212
    and not diffs
    and len(set(ghashes.values())) == 1
    and strict_ok
    and "juice-haccp" in skill
    and "juice-haccp" in index
    and skill.count("十七类") == 0
    and card26.count('> "') == 26
)
print("安装结果:", "PASS" if ok else "FAIL")
if ok:
    print("FINAL_INSTALL_OK")
raise SystemExit(0 if ok else 1)
