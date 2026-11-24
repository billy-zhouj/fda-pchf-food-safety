#!/usr/bin/env python3
"""生成 v4.11 补测套件（只读正式套件/历史套件，不改 dist-v15 / 已安装技能）。

产出（全部落在 .cangjie/v4-11-eval/）:
  trigger-suite.json        10 条 seafood-inspection-* + v4.7 的 8 sibling + 10 负例 = 28 条, runs=3
  output-suite.json         10 条 output case + 机械断言（锚定 CAP-24 新增知识点）
  output-suite-strict.json  同 10 条，每条只**追加** 1 条卡片独占锚点 = 50 断言（区分度敏感性）
  routing-suite.json        24 张卡各 1 条 + CAP-24 定向 7 + CAP-23 定向 3 + CAP-22 定向 3 = 37 条
  packets-trigger/          官方 run_trigger_evals.py prepare 生成的盲判包
  packets-output/           官方 run_output_evals.py prepare + 条件注入
  packets-routing/          自建盲判包（仿 v4.10）

口径沿用 v4.7 / v4.10，保证数字可比：
  - edge_case → should_trigger（single 模式）
  - 5-skill catalog 与 v4.7 / v4.10 完全一致（评测设定，非本机实际安装清单）
  - sibling / 负例原文复用 v4.7 trigger-suite-v2.json，不改写
  - 正式 test-prompts.json、SKILL.md、dist-v15、已安装技能一律不改动
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

CANGJIE = Path(__file__).resolve().parent
BOOK = CANGJIE.parent
E = CANGJIE / "v4-11-eval"
E.mkdir(parents=True, exist_ok=True)

OFFICIAL = Path.home() / ".workbuddy/skills/cangjie-skill/scripts"
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
        "FDA 海产品危害与控制指南第 4 版危害分析判定链、FDA CP 7303.842 海产品检查程序判定链。"
        "面向食品工厂质量合规、工艺研发、跨境食品贸易合规咨询。",
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
new = [c for c in formal["test_cases"] if c["id"].startswith("seafood-inspection-")]
assert len(new) == 10, f"v4.11 新用例应为 10 条，实得 {len(new)}"
assert formal["version"] == "4.11"

MAP = {"should_trigger": "should_trigger",
       "edge_case": "should_trigger",
       "should_not_trigger": "should_not_trigger"}
cases = [
    {"case_id": c["id"], "prompt": c["prompt"], "expected": MAP[c["type"]], "runs": 3}
    for c in new
]
dist = {k: sum(1 for c in cases if c["expected"] == k) for k in sorted({c["expected"] for c in cases})}
print("v4.11 新用例映射分布:", dist)

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
    "suite_id": "fda-pchf-v4-11-trigger-seafood-inspection",
    "target": "fda-pchf-food-safety",
    "split_seed": 42,
    "train_ratio": 0.6,
    "trigger_cases": cases,
})
(E / "skill-catalog.txt").write_text(
    "CATALOG（与 v4.7 / v4.10 完全一致，评测设定；本机实际安装清单另见报告局限说明）\n"
    + "\n".join(f"- {k}: {v}" for k, v in CATALOG.items()) + "\n",
    encoding="utf-8")


# ---------------------------------------------------------------- 2. 输出质量套件
OUTPUT_CASES = [
    {
        "case_id": "si-out-01",
        "prompt": "我手上这份 FDA 文件名叫 20250929_CP 7303.842 ... 508-Compliant.pdf，"
                  "首页还写 Date of Issuance 09/30/025，这是 2025 年新发布的海产品检查程序吗？"
                  "和 CPGM 7303.040 的 2025-CPM-HFP-001 是同一种版本形态吗？",
        "assertions": [
            {"kind": "regex", "value": r"2023|11/01/2023|11/1/2023"},
            {"kind": "regex", "value": r"更正|Correction date|09/30/2025"},
            {"kind": "regex", "value": r"生成日|creationDate|20250929|文件名"},
            {"kind": "regex", "value": r"CPGM|Transmittal|2025-CPM-HFP-001|不同"},
        ],
    },
    {
        "case_id": "si-out-02",
        "prompt": "CP 7303.842 和 CP 7303.844 现在合并了吗？合并后进口和国产样品是不是都报同一个 PAC 码？",
        "assertions": [
            {"kind": "regex", "value": r"合并|combination|single"},
            {"kind": "regex", "value": r"7303\.844"},
            {"kind": "regex", "value": r"03844|03842"},
            {"kind": "regex", "value": r"PAC|码表|取样|分析"},
        ],
    },
    {
        "case_id": "si-out-03",
        "prompt": "我们厂做减氧包装的熏制水产品和普通冷冻鱼，FDA 来检查时会先看哪张表排优先级？"
                  "进口商检查数量怎么定？",
        "assertions": [
            {"kind": "regex", "value": r"Table\s*1|表\s*1"},
            {"kind": "regex", "value": r"Table\s*2|表\s*2"},
            {"kind": "regex", "value": r"work planning|工作计划|合规史|排序"},
            {"kind": "regex", "value": r"90|10|100 entry|不对调|不可对调|适用域|分工"},
        ],
    },
    {
        "case_id": "si-out-04",
        "prompt": "海产品 HACCP 检查有哪些类型？加工船、境外加工商、NSSP 贝类企业和进口商各有什么特别要求？",
        "assertions": [
            {"kind": "regex", "value": r"六类|6\s*类|Processor|Importer"},
            {"kind": "regex", "value": r"Vessels|加工船|靠港"},
            {"kind": "regex", "value": r"NSSP|贝类|93-01"},
            {"kind": "regex", "value": r"HACCP Program Evaluation|最高风险|生产时"},
        ],
    },
    {
        "case_id": "si-out-05",
        "prompt": "国内海产品厂的常规 HACCP 检查，是不是每次都要取官方样品送检？"
                  "取样量按 ATTACHMENT A 的 Table A-1 就行了吗？",
        "assertions": [
            {"kind": "regex", "value": r"for cause|for-cause|因由|仅.{0,6}有因"},
            {"kind": "regex", "value": r"ATTACHMENT A|附件 A"},
            {"kind": "regex", "value": r"surveillance|audit|监督"},
            {"kind": "regex", "value": r"reconditioning|DWPE|不得|不适用|不能用于"},
        ],
    },
    {
        "case_id": "si-out-06",
        "prompt": "为支持州际贸易开了一份 documentary sample，PAC 该报 03842H 还是 03842？"
                  "算不算 Division Workplan 的取样任务？",
        "assertions": [
            {"kind": "regex", "value": r"03842"},
            {"kind": "regex", "value": r"03842H|H\s*结尾"},
            {"kind": "regex", "value": r"documentary|证明文件|书面"},
            {"kind": "regex", "value": r"Workplan|workplan|不计入|同名不同义"},
        ],
    },
    {
        "case_id": "si-out-07",
        "prompt": "CP 7303.842 里写组胺 500 ppm / 50 ppm / 35 ppm，是不是 FDA 对金枪鱼的法定组胺限量？"
                  "我们成品按 50 ppm 放行合规吗？",
        "assertions": [
            {"kind": "regex", "value": r"500|50|35"},
            {"kind": "regex", "value": r"触发|追加分析|check analysis|检查员"},
            {"kind": "regex", "value": r"不是.{0,12}(法规|法定|限量|放行)|不得.{0,10}(写成|当作)|非.{0,6}(法规|限值)"},
            {"kind": "regex", "value": r"540\.525|CPG|转引未收"},
        ],
    },
    {
        "case_id": "si-out-08",
        "prompt": "只要 Table 4 把某条 123.6 缺陷标成 Major，是不是就自动发 Warning Letter 并列入 DWPE？"
                  "这个 Major 和危害分析里的 significant hazard 是一回事吗？",
        "assertions": [
            {"kind": "regex", "value": r"Table\s*4|表\s*4"},
            {"kind": "regex", "value": r"case.by.case|逐案|个案"},
            {"kind": "regex", "value": r"123\.6|significant hazard|显著危害|reasonably likely"},
            {"kind": "regex", "value": r"concurrence|HFP|自动|不得"},
        ],
    },
    {
        "case_id": "si-out-09",
        "prompt": "FSVP 检查明确不取样、PART IV 全空，那海产品进口商的 HACCP 检查是不是也不取样？"
                  "两套检查能互相套用吗？",
        "assertions": [
            {"kind": "regex", "value": r"FSVP|7303\.878"},
            {"kind": "regex", "value": r"123\.12|进口商"},
            {"kind": "regex", "value": r"03844H|Surveillance|监督取样|取样"},
            {"kind": "regex", "value": r"两套|不得|不能|不适用|法源"},
        ],
    },
    {
        "case_id": "si-out-10",
        "prompt": "按中国 GB 2733 帮我判定这批水产品的组胺限量，顺便按欧盟法规写一份海产品出口卫生证书"
                  "和 FDA 检查应对承诺函。",
        "assertions": [
            {"kind": "regex", "value": r"超出|不适用|不覆盖|不(提供|代写)|无法(提供|给出)|建议咨询|拒绝"},
            {"kind": "regex", "value": r"GB 2733|欧盟|FDA|本包"},
            {"kind": "not_contains", "value": "卫生证书编号："},
            {"kind": "not_contains", "value": "组胺限量为"},
        ],
    },
]
assert len({c["case_id"] for c in OUTPUT_CASES}) == 10
assert all(len(c["assertions"]) == 4 for c in OUTPUT_CASES)

# 严格化敏感性套件：只**加** 1 条卡片独占锚点，不删改主套件任何断言。
# 目的：量化主套件 40 断言可能的虚高幅度（仿 v4.8/v4.9 历史补测口径）。
EXCLUSIVE = {
    "si-out-01": {"kind": "regex", "value": r"IMPLEMENTATION DATE|09/30/025|文本层残缺|页脚"},
    "si-out-02": {"kind": "regex", "value": r"03842H|同名不同义|两套码表|取样/分析 PAC"},
    "si-out-03": {"kind": "regex", "value": r"HIGHER RISK|not all inclusive|最高风险类别|Hazards Guide"},
    "si-out-04": {"kind": "regex", "value": r"Foreign Establishment|ISSC|483|HFP"},
    "si-out-05": {"kind": "regex", "value": r"702\(b\)|Domestic HACCP Verification|EIR|483"},
    "si-out-06": {"kind": "regex", "value": r"HACCP Verification|报告表|取样表|Not applicable"},
    "si-out-07": {"kind": "regex", "value": r"PART IV|6 subs|初始|CAP-22|CAP-23|分解指示|毒性水平"},
    "si-out-08": {"kind": "regex", "value": r"Significance must be determined|should be considered|judicial actions|CMS"},
    "si-out-09": {"kind": "regex", "value": r"part 1 subpart L|§805|805|转引未收|PART IV"},
    "si-out-10": {"kind": "regex", "value": r"out_of_scope|stop_conditions|边界|法域|专业机构"},
}
strict = [{"case_id": c["case_id"], "prompt": c["prompt"],
           "assertions": c["assertions"] + [EXCLUSIVE[c["case_id"]]]}
          for c in OUTPUT_CASES]

dump("output-suite.json", {
    "suite_id": "fda-pchf-v4-11-output-seafood-inspection",
    "target": "fda-pchf-food-safety",
    "split_seed": 42,
    "output_cases": OUTPUT_CASES,
})
dump("output-suite-strict.json", {
    "suite_id": "fda-pchf-v4-11-output-seafood-inspection-strict",
    "target": "fda-pchf-food-safety",
    "split_seed": 42,
    "output_cases": strict,
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
    ("CAP-24", "seafood-inspection-program",
     "CP 7303.842 的 Table 1 和 Table 2 分别用来做什么？进口商检查数量按哪张表定？"),
]
for cid, slug, prompt in EXTRA_BASE:
    base_cases.append({"case_id": f"route-{cid[4:]}", "capability_id": cid,
                       "prompt": prompt, "expected_capability": slug})

# CAP-24 定向：7 个不同角度，检验「完整检查判定链」这张卡是否稳定承接
CAP24_FOCUS = [
    ("cap24-a", "文件名 20250929_CP 7303.842，首页 Date of Issuance 09/30/025，这是 2025 新签发的 program 吗？"),
    ("cap24-b", "CP 7303.842 与 7303.844 合并后，进口和国产样品的 PAC 码是不是统一了？03842H 是什么？"),
    ("cap24-c", "国产海产品厂常规 HACCP 检查是不是每次都要取官方样品？ATTACHMENT A 的 subs 数能用在哪？"),
    ("cap24-d", "PART IV 组胺 500/50/35 ppm 是法规限量吗？判据出口转到哪个 CPG？"),
    ("cap24-e", "Table 4 的 Major/Minor 和 §123.6 的 significant hazard 是一回事吗？Warning Letter 会自动发吗？"),
    ("cap24-f", "海产品 HACCP 检查分哪六类？加工船、境外企业、NSSP 与进口商各查什么？"),
    ("cap24-g", "FSVP 检查不取样、PART IV 全空，海产品进口商 HACCP 检查是不是也一样？"),
]
for cid, prompt in CAP24_FOCUS:
    base_cases.append({"case_id": cid, "capability_id": "CAP-24",
                       "prompt": prompt, "expected_capability": "seafood-inspection-program"})

# CAP-23 / CAP-22 定向：反向检验 CAP-24 不吃掉「指南判定方法」与「法条义务」问题
CAP23_FOCUS = [
    ("cap23-a", "从描述产品、画流程图到定监控频率，海产品 HACCP 危害分析完整 18 步判定链怎么走？"),
    ("cap23-b", "Hazard Analysis Worksheet 第 3 栏填 No 的步骤，第 4 栏理由还要不要写？"),
    ("cap23-c", "指南 Appendix 5 的 50 ppm / 500 ppm 能不能直接抄进 HACCP 计划当关键限值？"),
]
CAP22_FOCUS = [
    ("cap22-a", "〔§ 123.9(b)(1)〕冷藏与冷冻、保藏、货架稳定水产品的 HACCP 记录各保存多久？"),
    ("cap22-b", "按〔§ 117.5(b)〕，水产品加工厂免 Part 117 Subparts C/G 要满足哪两个条件？"),
    ("cap22-c", "〔§ 123.11(a)〕SSOP 的 should 与 (b)(c) 监测记录的 shall 在法条上有什么区别？"),
]
for cid, prompt in CAP23_FOCUS:
    base_cases.append({"case_id": cid, "capability_id": "CAP-23",
                       "prompt": prompt, "expected_capability": "seafood-hazards-controls-guide"})
for cid, prompt in CAP22_FOCUS:
    base_cases.append({"case_id": cid, "capability_id": "CAP-22",
                       "prompt": prompt, "expected_capability": "seafood-haccp-statutory-requirements"})

index_text = Path(CAP_INDEX).read_text(encoding="utf-8")
slugs = sorted(set(re.findall(r"capabilities/([a-z0-9-]+)\.md", index_text)))
assert len(slugs) == 24, f"能力索引应含 24 张卡，实得 {len(slugs)}"
assert all(c["expected_capability"] in slugs for c in base_cases)
assert len(base_cases) == 37 and len({c["case_id"] for c in base_cases}) == 37
dump("routing-suite.json", {
    "suite_id": "fda-pchf-v4-11-routing-v1",
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
     "--out", E / "packets-output", "--variants", "v411_skill,without_skill"])

mapping = json.loads((E / "packets-output/mapping.json").read_text(encoding="utf-8"))
HINTS = {
    "v411_skill": (
        f"可用参考材料（请先读取再作答）：{INSTALLED.as_posix()}/SKILL.md 与其 references/ 下的能力卡、"
        "capability-index.md、glossary.md。遇到检查判定链、Table / PART 编号、PAC 码表、来源分层、"
        "转引未收等问题请以材料为准；尤其先读 seafood-inspection-program 卡。"
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
    "你是一个未参与蒸馏的干净 agent。已安装技能 fda-pchf-food-safety 内含 24 张能力卡，"
    f"候选清单（卡 id / 标题 / 重要度 / 意图 / 关键词 / 卡文件）见：{CAP_INDEX}；请先读取该文件。"
    "对用户 prompt 只判断应加载哪一张能力卡（top-1），不得输出多张。"
    "注意三层配对：CAP-22 是 21 CFR Part 123 法条义务层、CAP-23 是 FDA 技术指南层的危害分析判定链、"
    "CAP-24 是 FDA CP 7303.842 给 field staff 的检查程序作业层。"
    "按问题实际问的是「法定义务/条款号」「怎么判危害/怎么填表」还是「FDA 检查怎么排优先级/取样/PAC/上报」来区分，"
    "不要按关键词一概论。FSVP 专属问题走 CAP-21，通用取样走 CAP-17。"
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
    "# 盲判说明（v4.11 补测）\n\n"
    "- 触发：`packets-trigger/*.json` 共 28 条，3 个干净 sub-agent 各完整判一遍，"
    "分别写 results-trigger/run1/2/3.jsonl，构成每例 3 次重复。\n"
    "- 输出：`packets-output/<case_id>/task-<label>.json` 共 20 个，按包内 output_file 写出 <label>.md；"
    "mapping.json 不得交给评审 sub-agent。\n"
    "- 路由：本目录 *.json 共 37 条，3 个干净 sub-agent 分批盲判，写 results-routing/run1/2/3.jsonl。\n"
    "- 所有 judge 只看 prompt + 候选索引，**不得**看到 suite 中的 expected / expected_capability。\n",
    encoding="utf-8")

print("\nBUILD_V4_11_EVAL_OK")
print(f"catalog skills : {len(SKILLS)}")
print(f"trigger cases  : {len(cases)} (10 new + 8 sibling + 10 negative), x3 = {len(cases)*3} 判")
print(f"output cases   : {len(OUTPUT_CASES)} x2 变体 = 20 份答案；严格套件 {sum(len(c['assertions']) for c in strict)} 断言")
print(f"routing cases  : {len(base_cases)} (24 基础 + 7 CAP-24 + 3 CAP-23 + 3 CAP-22), x3 = {len(base_cases)*3} 判")
