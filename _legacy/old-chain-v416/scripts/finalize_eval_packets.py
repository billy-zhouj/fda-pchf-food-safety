#!/usr/bin/env python3
"""补齐评测任务包：为 output 匿名变体注入参考条件，生成 routing 盲判包。

注意：output 的变体映射表 mapping.json 只用于此处注入 reference_hint，
不会交给评审 sub-agent。本次只跑官方脚本的确定性机械断言环节，
不做 A/B 偏好盲评，也不作版本非劣声明。
"""
from __future__ import annotations

import json
from pathlib import Path

CANGJIE = Path(__file__).resolve().parent
BOOK = CANGJIE.parent
E = CANGJIE / "v4-7-output-routing-eval"
OUTP = E / "packets-output"
ROUTP = E / "packets-routing"
ROUTP.mkdir(parents=True, exist_ok=True)

V47 = "C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety"
V46 = str(BOOK / "backups" / "fda-pchf-food-safety-v4.6-20261106-132910").replace("\\", "/")
CAP_INDEX = f"{V47}/references/capability-index.md"

HINTS = {
    "v47_skill": (
        f"可用参考材料（请先读取再作答）：{V47}/SKILL.md 与该目录下 references/ 中的能力卡。"
        "遇到条款号、保存期限、来源分层等问题，请以材料为准。"
    ),
    "v46_skill": (
        f"可用参考材料（请先读取再作答）：{V46}/SKILL.md 与该目录下 references/ 中的能力卡。"
        "遇到条款号、保存期限、来源分层等问题，请以材料为准。"
    ),
    "without_skill": (
        "不要读取本机任何技能包、能力卡或参考文件；仅凭你自身知识作答，不要调用文件读取工具去查资料。"
    ),
}

# ---------------------------------------------------------------- output 变体条件注入
mapping = json.loads((OUTP / "mapping.json").read_text(encoding="utf-8"))
n = 0
for case_id, label_map in mapping.items():
    for label, variant in label_map.items():
        p = OUTP / case_id / f"task-{label}.json"
        d = json.loads(p.read_text(encoding="utf-8"))
        d["condition_hint"] = HINTS[variant]
        d["output_file"] = str(OUTP / case_id / f"{label}.md").replace("\\", "/")
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
print(f"injected condition_hint into {n} output task packets")
assert n == 30
assert (Path(V46) / "SKILL.md").exists(), "v4.6 backup missing"
assert Path(CAP_INDEX).exists(), "capability-index missing"

# ---------------------------------------------------------------- routing 盲判包
suite = json.loads((E / "routing-suite.json").read_text(encoding="utf-8"))
cands = suite["candidate_capabilities"]
INSTR = (
    "你是一个未参与蒸馏的干净 agent。已安装技能 fda-pchf-food-safety 内含 20 张能力卡，"
    f"候选清单（卡 id / 标题 / 意图 / 关键词 / 卡文件）见：{CAP_INDEX}；请先读取该文件。"
    "对用户 prompt 只判断应加载哪一张能力卡（top-1），不得输出多张。"
    "输出一行 JSON："
    '{"case_id": "...", "selected_capability": "<候选清单中的 slug>", "reason": "<=30字"}。'
    "slug 必须严格取自候选清单中的 capabilities/<slug>.md 文件名，不要编造。"
)
for c in suite["routing_cases"]:
    d = {
        "case_id": c["case_id"],
        "prompt": c["prompt"],
        "instruction": INSTR,
        "candidates_file": CAP_INDEX,
        "candidate_capabilities": cands,
    }
    (ROUTP / f"{c['case_id']}.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"wrote {len(suite['routing_cases'])} routing blind packets")

# ---------------------------------------------------------------- 触发盲判说明
(ROUTP / "README.md").write_text(
    "# 盲判说明\n\n"
    "- 触发：`packets-trigger/*.json` 共 103 条，3 个干净 sub-agent 各完整判一遍，"
    "分别写 results-run1/2/3.jsonl，即构成每例 3 次重复。\n"
    "- 输出：`packets-output/<case_id>/task-<label>.json` 共 30 个，"
    "按包内 output_file 写出 <label>.md；映射表不得交给 sub-agent。\n"
    "- 路由：本目录 route-*.json 共 20 条，2 个干净 sub-agent 分批盲判。\n",
    encoding="utf-8",
)
