#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""install_v16.py — 把 dist-v19（v4.15.1，来源十九类 / 27 卡）安装到**用户级**技能目录。

为什么不用 install_v15.py：
- v4.11 之后的脚本改成了「工作区级」目标 `WORKSPACE/.workbuddy/skills/fda-pchf-food-safety`，
  那是另一台开发机的部署形态；本机 `.workbuddy/` 下没有 `skills/`，
  而本会话实际加载的是用户级 `~/.workbuddy/skills/fda-pchf-food-safety`（即 install_v10 装的那份 v4.9）。
- 因此本脚本沿用 install_v10 的目标路径，只把产物换成 dist-v19。

与 install_v10 的差别：
- 先备份 → 校验备份完整 → 清空目标目录再整目录复制，保证安装目录是产物的**字节级镜像**
  （不会残留旧版被删除的文件）。
- 指标：27 卡 / 223 术语 / 158 用例 / version 4.15.1 / 0 errors 0 warnings。
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / "dist-v19"
DST = Path.home() / ".workbuddy/skills/fda-pchf-food-safety"
BACKUP_ROOT = BASE / "backups"
VALIDATOR = Path.home() / ".workbuddy/skills/cangjie-skill/scripts/validate_skill_pack.py"

assert SRC.is_dir() and (SRC / "SKILL.md").exists(), "编译产物不存在"
assert DST.parent.is_dir(), "用户级技能根目录不存在"
assert VALIDATOR.is_file(), f"官方校验脚本不存在: {VALIDATOR}"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def card_count(p: Path) -> int:
    return len(list((p / "references/capabilities").glob("*.md")))


# 1) 备份当前安装（v4.9）
BACKUP_ROOT.mkdir(exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup = BACKUP_ROOT / f"fda-pchf-food-safety-v4.9-{stamp}"
before = card_count(DST) if DST.exists() else 0
if DST.exists():
    shutil.copytree(DST, backup)
    assert (backup / "SKILL.md").exists(), "备份缺少 SKILL.md"
    assert card_count(backup) == before, "备份卡数与被备份目录不一致"
    print(f"旧版本已备份: {backup}（{before} 张卡）")
else:
    print("首次安装，无需备份")

# 2) 清空目标后整目录复制（镜像，不残留旧版文件）
if DST.exists():
    shutil.rmtree(DST)
shutil.copytree(SRC, DST)
shutil.copyfile(BASE / "test-prompts.json", DST / "test-prompts.json")
print(f"已安装到: {DST}")

# 3) 官方校验
check = subprocess.run([sys.executable, str(VALIDATOR), str(DST)], capture_output=True, text=True)
print("--- 安装后官方校验 ---")
print(check.stdout.strip())
if check.stderr.strip():
    print("stderr:", check.stderr.strip())

# 4) 指标核对
d = json.loads((DST / "test-prompts.json").read_text(encoding="utf-8"))
cards = sorted(p.name for p in (DST / "references/capabilities").glob("*.md"))
gloss = (DST / "references/glossary.md").read_text(encoding="utf-8")
skill = (DST / "SKILL.md").read_text(encoding="utf-8")
term_count = len(re.findall(r"^\s*- id: t\d+", gloss, re.M))
print(f"能力卡 {len(cards)} 张 / 测试用例 {len(d['test_cases'])} 条(版本 {d['version']}) / 术语 {term_count} 条")
print("十九类标注:", "十九类" in skill, "| SKILL 字节:", (DST / "SKILL.md").stat().st_size)
for k in ["seafood-hazards-controls-guide", "seafood-inspection-program", "juice-inspection"]:
    print(f"  新卡 {k}: {'在' if any(k in c for c in cards) else '不在'}")

# 5) 逐文件 hash 对比
diffs = [f"hash mismatch {p.relative_to(SRC)}" for p in sorted(SRC.rglob("*"))
         if p.is_file() and str(p.relative_to(SRC)) != "test-prompts.json"
         and (not (DST / p.relative_to(SRC)).exists() or sha(p) != sha(DST / p.relative_to(SRC)))]
extra = [p.relative_to(DST).as_posix() for p in DST.rglob("*")
         if p.is_file() and not (SRC / p.relative_to(DST)).exists()
         and p.relative_to(DST).as_posix() != "test-prompts.json"]
print("产物与安装目录逐文件 hash 差异:", len(diffs), "| 安装目录独有文件:", extra)

# 6) glossary 副本一致性
gpaths = [BASE / "candidates/glossary.md", BASE / "GLOSSARY.md",
          BASE / ".cangjie/capabilities/book/glossary.md",
          SRC / "references/glossary.md", DST / "references/glossary.md"]
ghashes = {str(p): sha(p) for p in gpaths if p.exists()}
print("glossary 副本数:", len(ghashes), "唯一 hash 数:", len(set(ghashes.values())))
for p, h in ghashes.items():
    print("  ", h[:16], p)

# 7) 严格 YAML 解析
try:
    import yaml
    g = yaml.safe_load(re.search(r"```ya?ml\n(.*?)\n```", gloss, re.S).group(1))
    strict_ok = isinstance(g, list) and len(g) == term_count == 223 and len({x["id"] for x in g}) == 223
    print(f"安装目录 glossary 严格解析: {'OK' if strict_ok else 'FAIL'} ({len(g) if isinstance(g, list) else 'n/a'} 条)")
except Exception as exc:  # pragma: no cover
    strict_ok = False
    print("安装目录 glossary 严格解析: FAIL", exc)

ok = (check.returncode == 0 and "0 errors, 0 warnings" in check.stdout
      and len(cards) == 27 and len(d["test_cases"]) == 158 and d["version"] == "4.15.1"
      and term_count == 223 and not diffs and not extra
      and len(set(ghashes.values())) == 1 and strict_ok)
print("安装结果:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
