"""fix_glossary_yaml.py — 修复 glossary.md fenced YAML 块的严格可解析性（v4.8 QA）

背景：
  GLOSSARY.md / candidates/glossary.md 的 ```yaml 代码块长期有 7 行 summary
  因「整段用双引号包住 + 内部又有未转义 ASCII 双引号」或「plain scalar 内含
  冒号+空格」而无法被 yaml.safe_load 解析。该问题在 v4.7 基线即存在（已用
  .cangjie/backup-v4-8-pre-revisions/glossary.md 复核），不是 v4.8 引入的回归；
  编译/官方校验并不解析这个 fenced 块，因此不阻断发版，但严格 QA 应消除。

做法：
  迭代调用 yaml.safe_load，取错误信息里**最后一个** line N（第一个是上下文行），
  把该行 value 改写成 YAML 块标量 `|-`，内容逐字保留；仅当原 value 以双引号
  开头且结尾时剥掉这对语法性外引号。收敛后断言 162 条、id 唯一、t153..t162 齐备。

  candidates/glossary.md 是主本；写回后由 assemble_bundle.py 生成 GLOSSARY.md
  与 .cangjie/capabilities/book/glossary.md，保证多副本一致。
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
MASTER = BASE / "candidates" / "glossary.md"
MIRROR = BASE / "GLOSSARY.md"
BACKUP = BASE / ".cangjie" / "backup-v4-8-pre-revisions"
BACKUP.mkdir(parents=True, exist_ok=True)

FENCE = re.compile(r"(```ya?ml\n)(.*?)(\n```)", re.S)
KEY_LINE = re.compile(r"^(\s*)([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")


def parse(lines: list[str]):
    return yaml.safe_load("\n".join(lines))


def main() -> None:
    raw = MASTER.read_text(encoding="utf-8")
    m = FENCE.search(raw)
    assert m, "glossary.md 找不到 ```yaml fenced 块"
    lines = m.group(2).splitlines()
    assert len(lines) > 1500

    fixes: list[tuple[int, str, str]] = []
    for _ in range(40):
        try:
            data = parse(lines)
            break
        except yaml.YAMLError as exc:
            found = re.findall(r"line (\d+), column (\d+)", str(exc))
            assert found, f"无法从错误信息定位行号: {exc}"
            idx = int(found[-1][0]) - 1  # 最后一个才是问题行；第一个是上下文行
            assert 0 <= idx < len(lines)
            line = lines[idx]
            mt = KEY_LINE.match(line)
            assert mt, f"问题行不是 key: value 形式，无法安全改写: {line[:120]}"
            indent, key, val = mt.group(1), mt.group(2), mt.group(3)
            if len(val) > 1 and val.startswith('"') and val.endswith('"'):
                val = val[1:-1].replace('\\"', '"').replace("\\'", "'")
            lines[idx:idx + 1] = [f"{indent}{key}: |-", f"{indent}  {val}"]
            fixes.append((idx + 1, key, val[:60]))
    else:
        raise AssertionError("40 次迭代后仍未收敛")

    assert isinstance(data, list), f"解析结果不是 list: {type(data)}"
    ids = [d["id"] for d in data]
    assert len(data) == 162, f"术语数应为 162，实际 {len(data)}"
    assert len(set(ids)) == 162, "术语 id 有重复"
    for n in range(153, 163):
        assert f"t{n}" in ids, f"缺 t{n}"

    # 备份主本与镜像（各自独立，避免覆盖已有 v4.8 前备份）
    for p in (MASTER, MIRROR):
        dst = BACKUP / (p.name + ".pre-yamlfix")
        if not dst.exists():
            shutil.copyfile(p, dst)

    new_body = "\n".join(lines)
    new_raw = raw[:m.start(2)] + new_body + raw[m.end(2):]
    MASTER.write_text(new_raw, encoding="utf-8")
    MIRROR.write_text(new_raw, encoding="utf-8")

    print(f"yaml.safe_load OK: {len(data)} entries, ids unique, t153..t162 present")
    print(f"fixed lines: {len(fixes)}")
    for ln, key, preview in fixes:
        print(f"  line {ln:5d}  {key}: {preview}")
    print(f"master == mirror: {MASTER.read_bytes() == MIRROR.read_bytes()}")


if __name__ == "__main__":
    main()
