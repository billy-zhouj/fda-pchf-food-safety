#!/usr/bin/env python3
"""生成 v4.10 补测套件（只读正式套件/历史套件，不改 dist-v14 / 已安装技能）。

产出（全部落在 .cangjie/v4-10-eval/）:
  trigger-suite.json   10 条 seafood-hazards-* + v4.7 的 8 sibling + 10 负例 = 28 条, runs=3
  output-suite.json    10 条 output case + 机械断言（锚定 v4.10 新增知识点）
  routing-suite.json   23 张卡各 1 条 + CAP-23 定向 7 条 + CAP-22 定向 3 条 = 33 条
  packets-trigger/     官方 run_trigger_evals.py prepare 生成的盲判包
  packets-output/      官方 run_output_evals.py prepare + 条件注入
  packets-routing/     自建盲判包（仿 v4.7 finalize_eval_packets.py）

口径沿用 v4.7，保证数字可比:
  - edge_case → should_trigger（v4.7 适配器口径；08/09 的 expected_behavior 确实要求激活技能）
  - 5-skill catalog 与 v4.7 完全一致（评测设定，非本机实际安装清单，报告中标注）
  - sibling / 负例原文复用 v4.7 trigger-suite-v2.json，不改写
  - 正式 test-prompts.json、SKILL.md、dist-v14、已安装技能一律不改动
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

CANGJIE = Path(__file__).resolve().parent
BOOK = CANGJIE.parent
E = CANGJIE / "v4-10-eval"
E.mkdir(parents=True, exist_ok=True)

OFFICIAL = Path("C:/Users/周至/.workbuddy/skills/cangjie-skill/scripts")
TRIGGER = OFFICIAL / "run_trigger_evals.py"
OUTPUT = OFFICIAL / "run_output_evals.py"

INSTALLED = BOOK.parent / ".workbuddy/skills/fda-pchf-food-safety"
CAP_INDEX = (INSTALLED / "references/capability-index.md").as_posix()
assert (INSTALLED / "SKILL.md").exists(), f"已安装技能不存在: {INSTALLED}"
assert Path(CAP_INDEX).exists(), f"能力索引不存在: {CAP_INDEX}"

V47 = CANGJIE / "v4-7-output-routing-eval"
SUITE_V2 = V47 / "trigger-suite-v2.json"
SUITE_ROUTE_V47 = V47 / "routing-suite.json"
FORMAL = BOOK / "test-prompts.json"

CATALOG = {
    "fda-pchf-food-safety":
        "FDA 人类食品危害分析与基于风险的预防控制（PCHF / 21 CFR Part 117 / FSMA）；"
        "食品危害分析、cGMP、过敏原控制、李斯特菌与环境卫生、缺陷行动水平、"
        "FDA 现场检查迎检/取样/483/检查员权限、低酸罐头与酸化食品（21 CFR Part 113/114）"
        "管辖分流与条款级法定义务、FSVP 进口商检查、21 CFR Part 123 海产品 HACCP 法定义务、"
        "FDA 海产品危害与控制指南第 4 版危害分析判定链。面向食品工厂质量合规、工艺研发、"
        "跨境食品贸易合规咨询。",
    "brand-ip": "根据品牌/Logo/真人/宠物/草图生成 IP 角色主视觉与角色设定卡、吉祥物设计。",
    "cangjie-skill": "把书籍/长视频/播客/课程蒸馏成一组可执行 skills（拆书、RIA 阅读法、能力卡）。不是普通摘要或书评。",
    "officecli1098": "用 officecli 命令行创建、分析、校对、修改 Office 文档（.docx/.xlsx/.pptx）。",
    "pdf2md-pro": "高保真 PDF→Markdown 转换，保留表格与书签标题层级、清除页眉页脚，附转换质量自检报告。",
}
SKILLS = list(CATALOG)


def dump(name: str, obj: dict) -> None:
    p = E / name
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    key = next((k for k in ("trigger_cases", "output_cases", "routing_cases") if k in obj), "?")
    print(f"wrote {name}: {len(obj[key])} {key}")


# ---------------------------------------------------------------- 1. 触发套件
formal = json.loads(FORMAL.read_text(encoding="utf-8"))
new = [c for c in formal["test_cases"] if c["id"].startswith("seafood-hazards-")]
assert len(new) == 10, f"v4.10 新增用例应为 10 条，实得 {len(new)}"
assert formal["version"] == "4.10"

# v4.7 适配器口径：edge_case 在 single 模式下仍应激活技能。
# 本次 08/09 两条的 expected_behavior 明确写「必须同时纠正两个方向的误读」「必须分清可答与转引未收」，
# 确属应触发，故映射为 should_trigger 是语义正确的，不是 v4.7 secg-edge-02 那类错配。
MAP = {"should_trigger": "should_trigger",
       "edge_case": "should_trigger",
       "should_not_trigger": "should_not_trigger"}
cases = [
    {"case_id": c["id"], "prompt": c["prompt"], "expected": MAP[c["type"]], "runs": 3}
    for c in new
]
dist = {k: sum(1 for c in cases if c["expected"] == k) for k in sorted({c["expected"] for c in cases})}
print("v4.10 新用例映射分布:", dist)

v2 = json.loads(SUITE_V2.read_text(encoding="utf-8"))
controls = [c for c in v2["trigger_cases"] if c["case_id"].startswith(("sib-", "neg-"))]
assert len([c for c in controls if c["case_id"].startswith("sib-")]) == 8
assert len([c for c in controls if c["case_id"].startswith("neg-")]) == 10
for c in controls:
    cases.append({"case_id": c["case_id"], "prompt": c["prompt"],
                  "expected": c["expected"], "runs": 3,
                  **({"sibling_target": c["sibling_target"]} if "sibling_target" in c else {})})

assert len(cases) == 28 and len({c["case_id"] for c in cases}) == 28
dump("trigger-suite.json", {
    "suite_id": "fda-pchf-v4-10-trigger-seafood-hazards",
    "target": "fda-pchf-food-safety",
    "split_seed": 42,
    "train_ratio": 0.6,
    "trigger_cases": cases,
})
(E / "skill-catalog.txt").write_text(
    "CATALOG（与 v4.7 完全一致，评测设定；本机实际安装清单另见报告局限说明）\n"
    + "\n".join(f"- {k}: {v}" for k, v in CATALOG.items()) + "\n",
    encoding="utf-8")


# ---------------------------------------------------------------- 2. 输出质量套件
# 断言锚定 v4.10 新增知识点，全部为官方 check_assertion 支持的 contains/not_contains/regex。
OUTPUT_CASES = [
    {
        "case_id": "sh-out-01",
        "prompt": "我们做冷冻金枪鱼排，查了 Ch.3 的 Table 3-2，表里这个鱼种组胺那栏没打勾，"
                  "是不是危害分析里就可以直接写「组胺不显著」？",
        "assertions": [
            {"kind": "regex", "value": r"Table 3-2|三表|三张表"},
            {"kind": "regex", "value": r"潜在危害|potential hazard|只列潜在"},
            {"kind": "regex", "value": r"无控制|absence of controls|reasonably likely to occur|合理(发生)?(的)?可能性"},
            {"kind": "regex", "value": r"第\s*4\s*栏|Column 4|理由"},
        ],
    },
    {
        "case_id": "sh-out-02",
        "prompt": "我们船上一直有时间温度控制，这几年从没检出过组胺，是不是就能判定组胺不是显著危害、"
                  "不用写进 HACCP 计划？",
        "assertions": [
            {"kind": "regex", "value": r"无控制|absence of controls"},
            {"kind": "regex", "value": r"组胺|scombrotoxin|histamine"},
            {"kind": "regex", "value": r"第\s*4\s*栏|Column 4|书面理由"},
            {"kind": "regex", "value": r"转引未收|540\.525|CPG"},
        ],
    },
    {
        "case_id": "sh-out-03",
        "prompt": "接收步骤判定组胺显著，是不是 CCP 就必须设在接收这一步？",
        "assertions": [
            {"kind": "regex", "value": r"Step\s*11|STEP\s*11|判定树|decision tree"},
            {"kind": "regex", "value": r"123\.6\(c\)\(2\)|至少一个|at least one"},
            {"kind": "regex", "value": r"Appendix 3|残表|塌陷|逐字"},
            {"kind": "regex", "value": r"控制策略|control strategy|漂移"},
        ],
    },
    {
        "case_id": "sh-out-04",
        "prompt": "危害分析工作表第 3 栏填了 No 的那些步骤，第 4 栏还要写理由吗？后面 18 步是不是都得走完？",
        "assertions": [
            {"kind": "regex", "value": r"第\s*4\s*栏|Column 4"},
            {"kind": "regex", "value": r"跳过|Steps?\s*1[128]|剪枝"},
            {"kind": "regex", "value": r"十栏|HACCP Plan Form|映射"},
            {"kind": "regex", "value": r"十五类不可混引|123\.6|不得(把|将)"},
        ],
    },
    {
        "case_id": "sh-out-05",
        "prompt": "帮我把海产品 HACCP 危害分析从头到尾走一遍：从描述产品到定监控频率，完整判定链是什么？",
        "assertions": [
            {"kind": "regex", "value": r"Table 3-2|Table 3-3|三表"},
            {"kind": "regex", "value": r"Table 3-4"},
            {"kind": "regex", "value": r"Step\s*10|STEP\s*10|第\s*10\s*步|无控制|absence of controls"},
            {"kind": "regex", "value": r"What|How|Frequency|Who|监控四问"},
        ],
    },
    {
        "case_id": "sh-out-06",
        "prompt": "指南里写了组胺 50 ppm / 500 ppm、寄生虫 -20°C 7 天，我们直接把这些数抄进 HACCP 计划"
                  "当关键限值，检查员是不是就认了？",
        "assertions": [
            {"kind": "regex", "value": r"非约束性|legally enforceable|不(具|设).{0,10}(法律|强制)|should"},
            {"kind": "regex", "value": r"540\.525|NSSP|40 CFR 180|转引未收"},
            {"kind": "regex", "value": r"-20|-35|7\s*天|6\s*英寸|盐渍|醋渍"},
            {"kind": "regex", "value": r"CAP-22|123\.|科学|scientifically"},
        ],
    },
    {
        "case_id": "sh-out-07",
        "prompt": "同一个组胺危害，Ch.7 给了好几条 Control Strategy Example，我们换一条控制策略，"
                  "CCP 和关键限值要不要跟着改？",
        "assertions": [
            {"kind": "regex", "value": r"control strategy|Control Strategy|控制策略"},
            {"kind": "regex", "value": r"CCP|Step\s*11|第\s*5\s*栏|第\s*6\s*栏"},
            {"kind": "regex", "value": r"四段式|Understand|Determine Significant|Identify CCPs|Develop Control Strategy"},
            {"kind": "regex", "value": r"科学|scientifically|充分性"},
        ],
    },
    {
        "case_id": "sh-out-08",
        "prompt": "既然这份指南自己说没有法律约束力、可以用别的控制策略，那我们是不是连 Part 123 要求的"
                  "书面 HACCP 计划和危害分析都可以不做？",
        "assertions": [
            {"kind": "regex", "value": r"123\.6"},
            {"kind": "regex", "value": r"shall|法定义务|法条层"},
            {"kind": "regex", "value": r"非约束性|should|legally enforceable|建议层"},
            {"kind": "regex", "value": r"十五类不可混引|CAP-22|反向误读"},
        ],
    },
    {
        "case_id": "sh-out-09",
        "prompt": "2022 年 6 月第 4 版是新规吧？麻烦把 Appendix 3 的 CCP 判定树逐字原文、"
                  "CPG 540.525 全文、以及 NSSP 贝类生长区分类都列出来。",
        "assertions": [
            {"kind": "regex", "value": r"June 2021|2021|滚动修订|分章"},
            {"kind": "regex", "value": r"转引未收"},
            {"kind": "regex", "value": r"Appendix 3|残表|塌陷|逐字|不得"},
            {"kind": "regex", "value": r"June 2022|第\s*4\s*版|4th"},
        ],
    },
    {
        "case_id": "sh-out-10",
        "prompt": "按中国 GB 2733 帮我判定这批鲜冻动物性水产品的组胺限量和感官要求，顺便写一份出口欧盟的卫生证书。",
        "assertions": [
            {"kind": "regex", "value": r"超出|不适用|不覆盖|不(提供|代写)|无法(提供|给出)|建议咨询|停(用|止)"},
            {"kind": "regex", "value": r"GB 2733|欧盟|FDA|本包"},
            {"kind": "not_contains", "value": "卫生证书编号："},
            {"kind": "not_contains", "value": "组胺限量为"},
        ],
    },
]
assert len({c["case_id"] for c in OUTPUT_CASES}) == 10
assert all(c["assertions"] for c in OUTPUT_CASES)
dump("output-suite.json", {
    "suite_id": "fda-pchf-v4-10-output-seafood-hazards",
    "target": "fda-pchf-food-safety",
    "split_seed": 42,
    "output_cases": OUTPUT_CASES,
})


# ---------------------------------------------------------------- 3. 能力卡路由套件
v47route = json.loads(SUITE_ROUTE_V47.read_text(encoding="utf-8"))
base_cases = [dict(c) for c in v47route["routing_cases"]]
assert len(base_cases) == 20

EXTRA_BASE = [
    ("CAP-21", "fsvp-inspection-program",
     "CP 7303.878 检查 FSVP 进口商时，PART IV 为什么全空、不取样？§1.509 每 entry line 要申报什么？"),
    ("CAP-22", "seafood-haccp-statutory-requirements",
     "21 CFR Part 123 的 §123.12 进口商验证有哪两条可选路径？affirmative steps 列在哪一款？"),
    ("CAP-23", "seafood-hazards-controls-guide",
     "我们做冷冻金枪鱼排，Ch.3 的 Table 3-2 里组胺那栏没打勾，危害分析能不能直接写「不显著」？"),
]
for cid, slug, prompt in EXTRA_BASE:
    base_cases.append({"case_id": f"route-{cid[4:]}", "capability_id": cid,
                       "prompt": prompt, "expected_capability": slug})

# CAP-23 定向：7 个不同角度，检验「完整判定链」这张卡是否稳定承接而非偶发命中
CAP23_FOCUS = [
    ("cap23-a", "从描述产品、画流程图一直到定监控频率，帮我把海产品 HACCP 危害分析完整判定链走一遍。"),
    ("cap23-b", "Table 3-4 是按成品形态、包装类型和储运方式来识别工艺相关潜在危害的吗？要怎么查？"),
    ("cap23-c", "Hazard Analysis Worksheet 第 3 栏填 No 的步骤，第 4 栏理由还要不要写？后面哪些步骤能跳过？"),
    ("cap23-d", "船上一直有时间温度控制、几年没检出组胺，这样能不能判定组胺不是显著危害？"),
    ("cap23-e", "同一个组胺危害换一条 Ch.7 的 Control Strategy Example，CCP 位置要不要重跑判定树？"),
    ("cap23-f", "指南 Appendix 5 的 50 ppm / 500 ppm 能不能直接抄进 HACCP 计划当关键限值？"),
    ("cap23-g", "June 2022 第 4 版是不是新规？Appendix 3 的 CCP 判定树逐字原文能给吗？"),
]
for cid, prompt in CAP23_FOCUS:
    base_cases.append({"case_id": cid, "capability_id": "CAP-23",
                       "prompt": prompt, "expected_capability": "seafood-hazards-controls-guide"})

# CAP-22 定向：反向检验 CAP-23 不会把「法条层」问题吃掉（最易混的一对）
CAP22_FOCUS = [
    ("cap22-a", "〔§ 123.9(b)(1)〕冷藏与冷冻、保藏、货架稳定水产品的 HACCP 记录各要保存多久？"),
    ("cap22-b", "按〔§ 117.5(b)〕，水产品加工厂要满足哪两个条件才免 Part 117 的 Subparts C/G？"),
    ("cap22-c", "〔§ 123.11(a)〕SSOP 的 should 与 (b)(c) 监测记录的 shall，法条上的措辞区别是什么？"),
]
for cid, prompt in CAP22_FOCUS:
    base_cases.append({"case_id": cid, "capability_id": "CAP-22",
                       "prompt": prompt, "expected_capability": "seafood-haccp-statutory-requirements"})

# 候选清单取自已安装能力索引（真实编译产物），不手写
index_text = Path(CAP_INDEX).read_text(encoding="utf-8")
import re as _re
slugs = sorted(set(_re.findall(r"capabilities/([a-z0-9-]+)\.md", index_text)))
assert len(slugs) == 23, f"能力索引应含 23 张卡，实得 {len(slugs)}"
assert all(c["expected_capability"] in slugs for c in base_cases)

assert len(base_cases) == 33 and len({c["case_id"] for c in base_cases}) == 33
dump("routing-suite.json", {
    "suite_id": "fda-pchf-v4-10-routing-v1",
    "target": "fda-pchf-food-safety",
    "candidate_capabilities": slugs,
    "routing_cases": base_cases,
})


# ---------------------------------------------------------------- 4. 官方 prepare + 盲判包
def run(cmd: list[str]) -> None:
    print("+", " ".join(str(x) for x in cmd))
    subprocess.run([sys.executable] + [str(x) for x in cmd], check=True)


run([TRIGGER, "prepare", E / "trigger-suite.json",
     "--skills", ",".join(SKILLS), "--out", E / "packets-trigger", "--set", "all"])
run([OUTPUT, "prepare", E / "output-suite.json",
     "--out", E / "packets-output", "--variants", "v410_skill,without_skill"])

# output 条件注入（仿 v4.7 finalize_eval_packets.py；mapping 不交给评审 agent）
mapping = json.loads((E / "packets-output/mapping.json").read_text(encoding="utf-8"))
HINTS = {
    "v410_skill": (
        f"可用参考材料（请先读取再作答）：{INSTALLED.as_posix()}/SKILL.md 与其 references/ 下的能力卡、"
        "capability-index.md、glossary.md。遇到判定链步骤、栏目编号、来源分层、转引未收等问题请以材料为准。"
    ),
    "without_skill": (
        "不要读取本机任何技能包、能力卡或参考文件；仅凭你自身知识作答，不要调用文件读取工具去查资料。"
    ),
}
n = 0
for case_id, label_map in mapping.items():
    for label, variant in label_map.items():
        p = E / "packets-output" / case_id / f"task-{label}.json"
        d = json.loads(p.read_text(encoding="utf-8"))
        d["condition_hint"] = HINTS[variant]
        d["output_file"] = (E / "packets-output" / case_id / f"{label}.md").as_posix()
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
print(f"injected condition_hint into {n} output task packets")
assert n == 20

ROUTP = E / "packets-routing"
ROUTP.mkdir(parents=True, exist_ok=True)
INSTR = (
    "你是一个未参与蒸馏的干净 agent。已安装技能 fda-pchf-food-safety 内含 23 张能力卡，"
    f"候选清单（卡 id / 标题 / 重要度 / 意图 / 关键词 / 卡文件）见：{CAP_INDEX}；请先读取该文件。"
    "对用户 prompt 只判断应加载哪一张能力卡（top-1），不得输出多张。"
    "注意 CAP-22 是 21 CFR Part 123 法条义务层、CAP-23 是 FDA 技术指南层的危害分析判定链，"
    "按问题实际问的是「法定义务/条款号」还是「怎么判/怎么填表/怎么定 CCP」来区分，不要按关键词一概论。"
    "输出一行 JSON："
    '{"case_id": "...", "selected_capability": "<候选清单中的 slug>", "reason": "<=30字"}。'
    "slug 必须严格取自候选清单中的 capabilities/<slug>.md 文件名，不要编造。"
)
for c in base_cases:
    (ROUTP / f"{c['case_id']}.json").write_text(json.dumps({
        "case_id": c["case_id"], "prompt": c["prompt"], "instruction": INSTR,
        "candidates_file": CAP_INDEX, "candidate_capabilities": slugs,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"wrote {len(base_cases)} routing blind packets")

(ROUTP / "README.md").write_text(
    "# 盲判说明（v4.10 补测）\n\n"
    "- 触发：`packets-trigger/*.json` 共 28 条，3 个干净 sub-agent 各完整判一遍，"
    "分别写 results-run1/2/3.jsonl，构成每例 3 次重复。\n"
    "- 输出：`packets-output/<case_id>/task-<label>.json` 共 20 个，按包内 output_file 写出 <label>.md；"
    "mapping.json 不得交给评审 sub-agent。\n"
    "- 路由：本目录 route-*.json / cap2*.json 共 33 条，3 个干净 sub-agent 分批盲判。\n"
    "- 所有 judge 只看 prompt + 候选索引，**不得**看到 suite 中的 expected / expected_capability。\n",
    encoding="utf-8")

print("\nBUILD_V4_10_EVAL_OK")
print(f"catalog skills : {len(SKILLS)}")
print(f"trigger cases  : {len(cases)} (10 new + 8 sibling + 10 negative), x3 = {len(cases)*3} 判")
print(f"output cases   : {len(OUTPUT_CASES)} x2 变体 = 20 份答案")
print(f"routing cases  : {len(base_cases)} (23 基础 + 7 CAP-23 定向 + 3 CAP-22 定向), x3 = {len(base_cases)*3} 判")
