#!/usr/bin/env python3
"""历史补测的输出评测「严格化敏感性分析」。

动机：主套件 20 条 output case 的断言锚定 expected_behavior / notes，
      多为条款号 + 常见结论，71/81 条两变体都通过（零区分度），
      `v410_skill 20/20` 有虚高嫌疑。本脚本给每条 case **追加 1 条**
      「卡片独占锚点」断言（CAP-21 / CAP-22 卡片正文里的精确原文或精确款号，
      baseline 难以仅凭常识写出），只加不减、不放宽，看分数与分离度如何变化。

产出：output-suite-strict.json + output-eval-report-strict.md
主结果仍以 output-suite.json / output-eval-report.md 的 20/20 为准。
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

E = Path(__file__).resolve().parent / "v4-8-v4-9-legacy-eval"
OFFICIAL = Path("C:/Users/周至/.workbuddy/skills/cangjie-skill/scripts/run_output_evals.py")

STRICT = {
    "fsvp-out-01": r"except they must comply with section 1\.509|PART II\.3\.A|CPGM 7303\.040 PART III|An importer that is not a receiving facility",
    "fsvp-out-02": r"Samples will not be collected as part of an FSVP inspection|PART III\.1\.C|PART IV\s*[–-]?\s*ANALYTICAL",
    "fsvp-out-03": r"for each entry line of food|each entry line of food|PART I\.1|PART V\.1\.A",
    "fsvp-out-04": r"1\.501\((b|c|d|e|f|g|h)\)|§1\.501\(b\)|有条件豁免|条件性豁免",
    "fsvp-out-05": r"may choose to follow standard requirements|PART III\.1\.A\.ii|§1\.512|资格证明",
    "fsvp-out-06": r"PART V\.1\.A|PART V\.1\.C|六类|最重大",
    "fsvp-out-07": r"Initial FSVP violations should be prioritized|known food safety risks|to obtain industry compliance|SAHCODHA",
    "fsvp-out-08": r"PART V\.3\.C\.i|specific food and specific foreign supplier|prior to attempting to import|CMS",
    "fsvp-out-09": r"PART V\.2|FURLS|FCE|SID|Center Views",
    "fsvp-out-10": r"FSVP Implementation Work Instructions|IP guidance tabs|HFP Enforcement Bulletin #13|RPM 4-1-8|7303\.819",
    "sf-out-01": r"except those subject to the requirements of part 113 or 114|至少整个货架期|at least through|整个货架期",
    "sf-out-02": r"required to comply with, and are in compliance with|123\.3\(k\)\(2\)|CGMP 不在豁免",
    "sf-out-03": r"applicable only with respect to the microbiological hazards|117\.5\(d\)\(2\)|专为.{0,6}part 113",
    "sf-out-04": r"123\.9\(b\)\(2\)|at least 2 years after their applicability|Part 114|三套",
    "sf-out-05": r"123\.12\(a\)\(2\)\(ii\)\(D\)|competent third party|FD&C Act §805|两套法源",
    "sf-out-06": r"123\.28\(c\)|五要素|approved growing waters|采捕许可",
    "sf-out-07": r"within 1 week of the day that the records are made|123\.8\(a\)\(3\)\(ii\)|123\.8\(a\)\(1\)|shall be modified immediately",
    "sf-out-08": r"123\.7\(c\)\(1\)|123\.7\(b\)\(1\)|segregate and hold|隔离并扣留",
    "sf-out-09": r"123\.3\(q\)|recommended or advisory|123\.11\(c\)|sufficient frequency",
    "sf-out-10": r"113\.3\(n\)|114\.3\(b\)|123\.6|至少整个货架期",
}

suite = json.loads((E / "output-suite.json").read_text(encoding="utf-8"))
assert len(suite["output_cases"]) == 20
assert set(STRICT) == {c["case_id"] for c in suite["output_cases"]}
for c in suite["output_cases"]:
    c["assertions"].append({"kind": "regex", "value": STRICT[c["case_id"]]})
suite["suite_id"] += "-strict"
(E / "output-suite-strict.json").write_text(
    json.dumps(suite, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"wrote output-suite-strict.json: 101 assertions (81 + 20 card-exclusive anchors)")

subprocess.run([sys.executable, str(OFFICIAL), "score",
                str(E / "output-suite-strict.json"),
                "--outputs", str(E / "packets-output"),
                "--mapping", str(E / "packets-output/mapping.json"),
                "--out", str(E / "output-eval-report-strict.md")], check=True)
print("\n".join((E / "output-eval-report-strict.md").read_text(encoding="utf-8")
                .splitlines()[-6:]))
