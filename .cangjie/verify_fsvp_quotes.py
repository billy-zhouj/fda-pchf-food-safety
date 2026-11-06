#!/usr/bin/env python3
"""逐字核对 CAP-21 fsvp-inspection-program 的 R 段英文引用块。

基准文本 = source-cp-7303-878-2023.md 的正文区（去掉导入说明文件头），
剥离 <u>/</u>、Markdown 强调与链接标记后做 NFKC + 去非字母数字归一化，
检查每条引用是否为连续子串；MISS 时用滑窗定位失配点。
同时校验 meta YAML 的字段类型。
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
CARD = BOOK / ".cangjie/capabilities/cards/fsvp-inspection-program.md"
META = BOOK / ".cangjie/capabilities/cards/_meta-fsvp-inspection-program.yaml"
SRC = BOOK / "source-cp-7303-878-2023.md"


def strip_markup(s: str) -> str:
    # HTML 标签（<u>、<br>、<sup> 等）先整体剥离，否则 <br> 的 "br" 会混进归一化串
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("**", "").replace("__", "")
    s = re.sub(r"[*_`#]", "", s)
    return s


def norm(s: str) -> str:
    s = strip_markup(s)
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"[^0-9A-Za-z]+", "", s).lower()


def main() -> int:
    card = CARD.read_text(encoding="utf-8")
    r_sec = card.split("## R — 原文", 1)[1].split("## I — 自述", 1)[0]
    quotes = [m.group(1) for m in re.finditer(r'(?m)^> "(.*)"\s*$', r_sec)]
    print(f"R 段引用块: {len(quotes)}")

    raw = SRC.read_text(encoding="utf-8")
    # 文件头之后才是正文：找第二处 H1
    first = raw.find("# FDA Compliance Program 7303.878")
    second = raw.find("# FDA Compliance Program 7303.878", first + 10)
    body = raw[second:] if second > 0 else raw
    print(f"正文区起点字符位置: {second}  长度: {len(body)}")
    hay = norm(body)

    miss = []
    for i, q in enumerate(quotes, 1):
        needle = norm(q)
        if needle and needle in hay:
            print(f"  {i:2d} HIT  ({len(needle):4d}) {q[:62]}")
        else:
            miss.append((i, q, needle))
            print(f"  {i:2d} MISS ({len(needle):4d}) {q[:62]}")
            # 找最长匹配前缀，定位失配点
            lo, hi = 0, len(needle)
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if needle[:mid] in hay:
                    lo = mid
                else:
                    hi = mid - 1
            print(f"      最长匹配前缀 {lo}/{len(needle)} → 失配处: ...{needle[max(0,lo-30):lo+40]}")

    # meta 类型检查
    try:
        import yaml
        d = yaml.safe_load(META.read_text(encoding="utf-8"))
        problems = []
        for k in ("slug", "title", "importance", "importance_rationale", "one_liner", "source_label"):
            if not isinstance(d.get(k), str):
                problems.append(f"{k}: {type(d.get(k)).__name__}")
        for k in ("intents", "keywords", "member_units"):
            v = d.get(k, [])
            if not isinstance(v, list) or any(not isinstance(x, (str, int, float)) for x in v):
                problems.append(f"{k}: 含非标量")
        print("meta YAML:", "problems 0" if not problems else problems)
    except ImportError:
        print("meta YAML: PyYAML 不可用，跳过")
        problems = []

    print(f"\n逐字命中 {len(quotes) - len(miss)}/{len(quotes)}")
    return 1 if miss or problems else 0


if __name__ == "__main__":
    sys.exit(main())
