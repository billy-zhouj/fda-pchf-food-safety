#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_v4.19.py — 权威全量构建链（v4.19，可复现）。

从 v4.16 基线重放 v4.17→v4.19 三步增量，产出完整 51 卡技能包，
并逐文件 sha256 对齐 dist-v21（权威参考产物）。这是主仓库**唯一**的全量构建入口。

血缘说明（详见 .cangjie/README.md）：
  基线 = dist-v20（33 文件，v4.16）+ 根 test-prompts.json（v4.16，168 用例）
  增量 = build/v4.19/{v4.17,v4.18,v4.19}/capabilities/*.md（23 张卡，冻结副本）
  最终态 = build/v4.19/final/*（6 个被三步修改的文件的 v4.19 终态）
  校验 = 产物与 dist-v21 全部 57 文件 sha256 逐一相等

用法：
  python .cangjie/build_v4.19.py            # 构建到 .staging-run-build/ 并校验
  python .cangjie/build_v4.19.py --out DIR  # 指定产物目录

为什么用「冻结增量」而不是重跑 3 个 book 的 apply 脚本：
  v4.17 apply 依赖原 book 的 dist/（归档未收）且路径硬编码原开发机；
  v4.19 的变更是交互式手工完成、从未脚本化（原 book 无 apply 脚本）。
  冻结增量把「当时实际写入的内容」固化为不可变输入，构建因此确定性、零外部依赖。
  build/v4.19/ 下每个文件在生成时已断言与 dist-v21 对应文件 hash 相等。
"""
import hashlib
import json
import shutil
import sys
import tempfile
import time
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
BASELINE_DIR = BASE / "build/v4.16-baseline"                  # v4.16 基线（dist-v20 33 文件）
BASELINE_TP = BASE / "build/v4.16-baseline/test-prompts.json"  # v4.16 基线 test-prompts（168 用例）
DELTA = BASE / "build/v4.19"              # 冻结增量（23 卡 + 6 最终态）
REF = BASE / "dist-v21"                   # 权威参考产物（57 文件）

DEFAULT_OUT = Path(tempfile.gettempdir()) / f"fda-build-v419-{time.strftime('%Y%m%d-%H%M%S')}"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def build(out: Path) -> None:
    # 0. 前置检查
    assert BASELINE_DIR.is_dir() and (BASELINE_DIR / "SKILL.md").exists(), "基线 dist-v20 缺失"
    assert BASELINE_TP.is_file(), "基线根 test-prompts.json 缺失"
    assert DELTA.is_dir(), "冻结增量 build/v4.19 缺失"
    assert REF.is_dir(), "权威参考产物 dist-v21 缺失"
    tp0 = json.loads(BASELINE_TP.read_text(encoding="utf-8"))
    assert tp0["version"] == "4.16" and len(tp0["test_cases"]) == 168, \
        f"基线 test-prompts 不是 v4.16/168 用例: {tp0['version']}/{len(tp0['test_cases'])}"

    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"输出目录非空，拒绝覆盖（换一个 --out）：{out}")
    out.mkdir(parents=True, exist_ok=True)

    # 1. 铺基线（dist-v20 全量 + 根 test-prompts.json 归位到产物根）
    for f in sorted(BASELINE_DIR.rglob("*")):
        if f.is_file():
            dest = out / f.relative_to(BASELINE_DIR)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)
    shutil.copy2(BASELINE_TP, out / "test-prompts.json")
    n_base = sum(1 for _ in out.rglob("*") if _.is_file())
    assert n_base == 34, f"基线应铺 34 文件，实际 {n_base}"
    print(f"[1] 基线铺入 {n_base} 文件（dist-v20 33 + test-prompts.json）")

    # 2. 叠加 23 张增量卡（v4.17 11 张 / v4.18 6 张 / v4.19 6 张）
    cap = out / "references/capabilities"
    n_cards = 0
    for gen in ("v4.17", "v4.18", "v4.19"):
        g = DELTA / gen / "capabilities"
        for f in sorted(g.rglob("*.md")):
            dest = cap / f.relative_to(g)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)
            n_cards += 1
    assert n_cards == 23, f"增量卡应 23 张，实际 {n_cards}"
    print(f"[2] 增量卡叠加 {n_cards} 张（v4.17=11, v4.18=6, v4.19=6）")

    # 3. 覆盖 6 个最终态文件（SKILL.md / test-prompts.json / 索引 / 速查 / 术语 / 概览）
    n_final = 0
    for f in sorted((DELTA / "final").rglob("*")):
        if f.is_file():
            dest = out / f.relative_to(DELTA / "final")
            shutil.copy2(f, dest)
            n_final += 1
    assert n_final == 6, f"最终态应 6 文件，实际 {n_final}"
    print(f"[3] 最终态覆盖 {n_final} 文件")

    # 4. 逐文件对齐 dist-v21
    built = {f.relative_to(out) for f in out.rglob("*") if f.is_file()}
    ref = {f.relative_to(REF) for f in REF.rglob("*") if f.is_file()}
    missing = sorted(ref - built)
    extra = sorted(built - ref)
    assert not missing, f"产物缺文件: {missing}"
    assert not extra, f"产物多文件: {extra}"
    bad = [r for r in sorted(ref) if sha(out / r) != sha(REF / r)]
    assert not bad, f"hash 不一致: {bad}"
    print(f"[4] 与 dist-v21 对齐：{len(ref)} 文件 sha256 全部一致")

    # 5. 指标快照
    tp = json.loads((out / "test-prompts.json").read_text(encoding="utf-8"))
    gloss = (out / "references/glossary.md").read_text(encoding="utf-8")
    term_count = len(__import__("re").findall(r"^\s*- id: t\d+", gloss, __import__("re").M))
    card_files = len(list((out / "references/capabilities").rglob("*.md")))
    assert tp["version"] == "4.19" and len(tp["test_cases"]) == 204
    assert card_files == 51 and term_count == 318
    print(f"[5] 指标：version {tp['version']} / 能力卡 {card_files} 文件 / 术语 {term_count} / 用例 {len(tp['test_cases'])}")
    print(f"\nBUILD OK -> {out}")


if __name__ == "__main__":
    arg_out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
    build(Path(arg_out) if arg_out else DEFAULT_OUT)
