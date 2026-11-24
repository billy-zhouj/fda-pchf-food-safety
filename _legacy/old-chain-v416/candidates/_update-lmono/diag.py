import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
raw = (BASE / "lmono-chunks.md").read_text(encoding="utf-8", newline="")
lines = raw.split("\n")

print("总行数:", len(lines))
first = lines[0]
print("首行 repr:", repr(first[:40]))

# 逐步验证正则
pats = [
    r"^## \[",
    r"^## \[([a-z0-9]+)\]",
    r"^## \[([a-z0-9]+)\] (.*)",
]
for p in pats:
    m = re.match(p, first)
    print(f"  pattern {p!r:40} -> {m.groups() if m else None}")

rows = []
for i, ln in enumerate(lines, 1):
    m = re.match(r"^## \[([a-z0-9]+)\] (.*)", ln)
    if m:
        rows.append((i, m.group(1), m.group(2)))
print("块数:", len(rows))
