"""apply_v4_15_residue.py — v4.15 卡内口径回补

三件事：
1. **订正错误 CP 号**：果汁检查程序是 CP **7303.847**，v4.13 在 CAP-26 及 meta 里
   写成了 `7303.047`（7 处）——这是硬错，逐条改写而非批量替换，避免误伤。
2. 清除「CP 7303.047 果汁 program 未收」的当前断言（本版已收为第十九来源）。
3. 计数口径：十八类 → 十九类（44 处）、26 张 → 27 张（5 处）；紧邻的
   `v4.13 起` 校为 `v4.15 起`。

顺序纪律同前：先逐行改写（含「十八类」的 old 串），再跑全局计数替换。
"""
from __future__ import annotations

import sys
from pathlib import Path

C = Path(".cangjie/capabilities/cards")
J26 = "juice-haccp.md"
M26 = "_meta-juice-haccp.yaml"

REWRITES: list[tuple[str, str, str, str]] = [
    # ── CAP-26 头注：未收清单里去掉检查程序，并订正 CP 号 ────────────────
    (
        J26, "cap26-header",
        "仍属「转引未收」的是：part 110 正文、CP 7303.047 果汁 program 全文、CPG / Import Alert 全文、BAM 方法全文。",
        "仍属「转引未收」的是：part 110 正文、CPG / Import Alert 全文、BAM 方法全文。⚠ **果汁检查程序（CP 7303.847）自 v4.15 起已收**，检查员取证口径见 CAP-27 `juice-inspection-program`——v4.13 曾把该程序号误写为 `7303.047`，正确号是 **7303.847**。",
    ),
    (
        J26, "cap26-position",
        "不覆盖：检查员取证口径（CP 7303.047 未收）、F0/D/z 计算、BAM 检测方法全文、以及基于 GC/MS 的香气成分等质量指标。",
        "不覆盖：检查员取证口径（CP 7303.847，自 v4.15 起已收，见 CAP-27）、F0/D/z 计算、BAM 检测方法全文、以及基于 GC/MS 的香气成分等质量指标。",
    ),
    # ── A2 第 30 条 ────────────────────────────────────────────────────
    (
        J26, "cap26-a2-30",
        "30. 用户问「CP 7303.047 果汁 program 查什么」→ 未收，转出本包（只给「检查员取证口径不在本卡」）。",
        "30. 用户问「CP 7303.847 果汁检查程序查什么」→ **转 CAP-27 `juice-inspection-program`**（v4.15 起已收）；含检查优先级、三类样品分流（验证/有因/文档性）、ATTACHMENT A 采样量、铅与巴氏毒素触发值、60 天复检口径。",
    ),
    # ── Step 6 ─────────────────────────────────────────────────────────
    (
        J26, "cap26-step6",
        "每条结论标〔§ 120.xxx〕或「CP 7303.047（转引未收）」；part 110 正文、BAM 方法、CPG / Import Alert 全文一律标「转引未收」。",
        "每条结论标〔§ 120.xxx〕（法条层）；检查员侧标「CP 7303.847 PART x / ATTACHMENT A」（v4.15 起已收，见 CAP-27）；part 110 正文、BAM 方法、CPG / Import Alert 全文一律标「转引未收」。",
    ),
    # ── B10 ────────────────────────────────────────────────────────────
    (
        J26, "cap26-b10",
        "⚠ part 110 正文未收、CP 7303.047（果汁 program）未收、CPG 与 Import Alert 全文未收、BAM / AOAC 检测方法全文未收——凡涉这些内容一律标「转引未收」。",
        "⚠ part 110 正文未收、CPG 与 Import Alert 全文未收、BAM / AOAC 检测方法全文未收——凡涉这些内容一律标「转引未收」。果汁检查程序 CP **7303.847** 自 v4.15 起已收，检查员侧一律转 CAP-27。（v4.13 曾误写为 `7303.047`。）",
    ),
    # ── CAP-26 meta：intent 与 source_label ─────────────────────────────
    (
        M26, "cap26-meta-intent",
        "  - 判断哪些问题超出本卡（CP 7303.047、BAM 方法、CPG、Import Alert、F0 计算）",
        "  - 判断哪些问题超出本卡（BAM 方法、CPG、Import Alert、F0 计算）；检查员取证口径自 v4.15 起转 CAP-27（CP 7303.847）",
    ),
    (
        M26, "cap26-meta-label",
        "CP 7303.047 果汁 program、CPG 与 Import Alert 全文、BAM / AOAC 方法全文",
        "CPG 与 Import Alert 全文、BAM / AOAC 方法全文（果汁检查程序 CP 7303.847 自 v4.15 起已收，见 CAP-27）",
    ),
]


def main() -> int:
    apply = "--apply" in sys.argv
    files: dict[Path, str] = {}

    def get(name: str) -> str:
        p = C / name
        if p not in files:
            files[p] = p.read_text(encoding="utf-8")
        return files[p]

    for name, label, old, new in REWRITES:
        t = get(name)
        n = t.count(old)
        if n != 1:
            print(f"FAIL [{label}] {name} 期望 1 处命中，实得 {n}", file=sys.stderr)
            print(f"      {old[:110]!r}", file=sys.stderr)
            return 1
        files[C / name] = t.replace(old, new, 1)
        print(f"OK   [rewrite] {label}")

    # 全局计数替换（在逐行改写之后）
    total = 0
    for p in sorted(C.glob("*")):
        if not p.is_file():
            continue
        t = files.get(p) or p.read_text(encoding="utf-8")
        if "十八类" in t:
            n = t.count("十八类")
            total += n
            files[p] = t.replace("十八类", "十九类")
    print(f"OK   [count]   十八类 → 十九类 × {total}")

    total = 0
    for p, t in list(files.items()):
        if "26 张" in t:
            n = t.count("26 张")
            total += n
            files[p] = t.replace("26 张", "27 张")
    print(f"OK   [count]   26 张 → 27 张 × {total}")

    # 紧邻「十九类」的 v4.13 起 → v4.15 起
    fixed = 0
    for p, t in list(files.items()):
        buf = list(t)
        i = 0
        while True:
            j = t.find("十九类", i)
            if j < 0:
                break
            k = t.rfind("v4.13 起", max(0, j - 30), j)
            if k >= 0:
                buf[k:k + len("v4.13 起")] = list("v4.15 起")
                t = "".join(buf)
                fixed += 1
            i = j + 1
        files[p] = t
    print(f"OK   [version] v4.13 起 → v4.15 起 × {fixed}")

    # 残留检查：不应再有「未加勘误说明」的 7303.047。
    # 本版会在正文里显式记录「v4.13 曾误写为 7303.047」，这类句子允许保留。
    bad: list[tuple[str, int]] = []
    for p, t in files.items():
        cnt = 0
        for ln in t.split("\n"):
            if "7303.047" in ln and not ("误写" in ln or "曾把" in ln):
                cnt += ln.count("7303.047")
        if cnt:
            bad.append((p.name, cnt))
    if bad:
        print(f"FAIL 仍有未说明的错误 CP 号 7303.047：{bad}", file=sys.stderr)
        return 1
    print("OK   [check]   卡目录的 7303.047 仅出现在勘误说明中")

    if not apply:
        print(f"\n[dry-run] 涉及 {len(files)} 个文件，未写盘。加 --apply 落地。")
        return 0
    for p, t in files.items():
        p.write_text(t, encoding="utf-8")
    print(f"\n已写盘 {len(files)} 个文件。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
