import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
raw = (BASE / "lmono-chunks.md").read_text(encoding="utf-8", newline="")
lines = raw.split("\n")

rows = []
for i, ln in enumerate(lines, 1):
    m = re.match(r"^## \[([a-z0-9-]+)\] (.*)", ln)
    if m:
        rows.append((i, m.group(1), m.group(2)))
print("块数:", len(rows))

ROMAN = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX","XX","XXI"]
tops = []
for idx, (ln, cid, hp) in enumerate(rows):
    parts = hp.split(" / ")
    tail = parts[-1].strip()
    if len(parts) <= 2:
        for r in ROMAN:
            if tail.startswith(r + "."):
                tops.append((idx, ln, tail[:48]))
                break

print("顶层章数:", len(tops))
bounds = []
for k, (idx, ln, t) in enumerate(tops):
    end = tops[k+1][1] - 1 if k+1 < len(tops) else len(lines)
    bounds.append((ln, end, t))
    print(f"  {ln:>5}-{end:<5} ({end-ln+1:>4}行)  {t}")
