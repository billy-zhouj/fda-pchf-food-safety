#!/usr/bin/env python3
"""生成 v4.7 增强评测套件（只读正式套件，不改已安装技能包）。

产出（全部落在 .cangjie/v4-7-output-routing-eval/）:
  trigger-suite-v2.json  85 条原用例(runs=3) + 8 sibling + 10 负例 = 103 条
  output-suite.json      10 条 output case + 机械断言
  routing-suite.json     20 条能力卡路由用例（每张卡 1 条）+ 候选卡清单

设计约束:
  - 正式 test-prompts.json 与已安装 v4.7 均不改动
  - edge_case 沿用 v4.7 的 should_trigger 映射（single 模式下仍应激活技能）
  - sibling_target 必须是本机真实已安装的技能 slug
"""
from __future__ import annotations

import json
from pathlib import Path

CANGJIE = Path(__file__).resolve().parent
OUT = CANGJIE / "v4-7-output-routing-eval"
OUT.mkdir(parents=True, exist_ok=True)
BASE = CANGJIE / "v4-7-trigger-eval" / "trigger-suite.json"

base = json.loads(BASE.read_text(encoding="utf-8"))
TARGET = base["target"]


def dump(name: str, obj: dict) -> None:
    p = OUT / name
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {p.name}: {len(obj.get('trigger_cases', obj.get('output_cases', obj.get('routing_cases', []))))} cases")


# ---------------------------------------------------------------- 1. 触发增强套件
cases = [
    {"case_id": c["case_id"], "prompt": c["prompt"], "expected": c["expected"], "runs": 3}
    for c in base["trigger_cases"]
]
assert len(cases) == 85 and sum(c["runs"] == 3 for c in cases) == 85

SIBLINGS = [
    ("sib-01", "这份 GPO 出的双栏 CFR PDF，用 markitdown 转出来表格全丢了，帮我高保真转成 Markdown，表格要保留、书签标题层级要还原、页眉页脚要清掉。", "pdf2md-pro"),
    ("sib-02", "把这个品牌 Logo 做成一套 IP 吉祥物角色设定卡，要一张主视觉，再配性格设定和三视图。", "brand-ip"),
    ("sib-03", "我想把手里这本食品法规指南蒸馏成一个可复用的 skill，按 cangjie 的流程该怎么做？", "cangjie-skill"),
    ("sib-04", "打开我桌面那份 Excel，把 B 列按数值降序排，再基于 C 列生成一个柱状图。", "officecli1098"),
    ("sib-05", "一份 300 页的扫描版法规 PDF，帮我批量转 md，要求按 PDF 内置书签重建标题层级并附转换质量自检报告。", "pdf2md-pro"),
    ("sib-06", "给我家柯基设计一套宠物 IP 形象，含表情包和角色设定卡。", "brand-ip"),
    ("sib-07", "把这段课程录像的文字稿拆成若干条可执行 skill，做成技能包。", "cangjie-skill"),
    ("sib-08", "帮我在这个 csv 里加一列求和公式，并把前两行合并单元格。", "officecli1098"),
]
for cid, prompt, sib in SIBLINGS:
    cases.append({
        "case_id": cid, "prompt": prompt, "expected": "sibling",
        "sibling_target": sib, "runs": 3,
    })

NEGATIVES = [
    ("neg-01", "帮我查一下今天上证指数收盘点位和涨跌幅。"),
    ("neg-02", "用 Python 写一个快速排序，并解释它的平均时间复杂度。"),
    ("neg-03", "21 CFR 210/211 药品 cGMP 对洁净区相邻房间的压差有什么要求？"),
    ("neg-04", "9 CFR 416/417 对肉类屠宰厂的 SSOP 与 HACCP 计划分别要求写哪些内容？"),
    ("neg-05", "GB 2763-2021 里茶叶的农药最大残留限量是多少？"),
    ("neg-06", "欧盟 Regulation (EC) No 852/2004 对食品经营者的注册义务怎么规定？"),
    ("neg-07", "化妆品 GMP（ISO 22716）对灌装车间微生物监控频次的要求是什么？"),
    ("neg-08", "帮我拟一份设备采购合同模板，含交货期与违约责任条款。"),
    ("neg-09", "明天上海天气怎么样，需要带伞吗？"),
    ("neg-10", "把这段产品介绍翻译成日语，语气要正式。"),
]
for cid, prompt in NEGATIVES:
    cases.append({"case_id": cid, "prompt": prompt, "expected": "should_not_trigger", "runs": 3})

assert len(cases) == 103
assert len({c["case_id"] for c in cases}) == 103
dump("trigger-suite-v2.json", {
    "suite_id": "fda-pchf-v4-7-trigger-v2",
    "target": TARGET,
    "split_seed": base.get("split_seed", 42),
    "train_ratio": base.get("train_ratio", 0.6),
    "trigger_cases": cases,
})


# ---------------------------------------------------------------- 2. 输出质量套件
OUTPUT_CASES = [
    {
        "case_id": "out-01",
        "prompt": "低酸罐头（21 CFR Part 113）的杀菌与容器封口记录要保存多久？可以用电子记录吗，需要满足什么额外条件？请给出条款号。",
        "assertions": [
            {"kind": "regex", "value": r"113\.100\(g\)"},
            {"kind": "regex", "value": r"113\.100\(h\)|part\s*11"},
            {"kind": "regex", "value": r"1\s*年"},
        ],
    },
    {
        "case_id": "out-02",
        "prompt": "酸化食品（21 CFR Part 114）的记录保存期限到底是几年？是不是也和低酸罐头一样「厂内 1 年 + 异地再 2 年」并且可用 part 11 电子记录？请给出条款号并说明与 Part 113 的差别。",
        "assertions": [
            {"kind": "regex", "value": r"114\.100\(e\)"},
            {"kind": "regex", "value": r"3\s*年"},
            {"kind": "not_contains", "value": "§ 114.100(h)"},
            {"kind": "not_contains", "value": "两 part 都是 1+2 年"},
        ],
    },
    {
        "case_id": "out-03",
        "prompt": "21 CFR 114.5 里写掺假判定要同时适用 parts 110 and 117，Part 110 不是早就被 PCHF 最终规则删掉了吗？这是不是印刷错误？请说明现行状态与依据。",
        "assertions": [
            {"kind": "regex", "value": r"110\s*and\s*117"},
            {"kind": "regex", "value": r"2018|撤回|withdraw"},
            {"kind": "not_contains", "value": "Part 110 已移除"},
        ],
    },
    {
        "case_id": "out-04",
        "prompt": "我们既做低酸罐头又做普通即食食品，是不是做了 Part 113 的 scheduled process 就不用管 21 CFR Part 117 的 Subparts C 和 G 了？请从条款层面回答。",
        "assertions": [
            {"kind": "regex", "value": r"117\.1\(c\)"},
            {"kind": "regex", "value": r"117\.5\(d\)"},
            {"kind": "regex", "value": r"条件|豁免|并行"},
        ],
    },
    {
        "case_id": "out-05",
        "prompt": "低酸食品定义里的 equilibrium pH > 4.6 和 water activity > 0.85 分别出自哪个条款？这两个数值在 Part 117 里扮演什么角色？",
        "assertions": [
            {"kind": "regex", "value": r"113\.3"},
            {"kind": "regex", "value": r"4\.6"},
            {"kind": "regex", "value": r"0\.85"},
        ],
    },
    {
        "case_id": "out-06",
        "prompt": "什么是 scheduled process？低酸罐头企业必须把它归档吗，FDA 检查时能不能调阅？请给出条款依据。",
        "assertions": [
            {"kind": "regex", "value": r"(?i)scheduled process"},
            {"kind": "regex", "value": r"113\.|114\."},
        ],
    },
    {
        "case_id": "out-07",
        "prompt": "本技能包说来源不可混引，请列出当前共有几类来源、法规正文有哪几套编号，并示范一个规范的条款引用写法。",
        "assertions": [
            {"kind": "contains", "value": "十二类"},
            {"kind": "regex", "value": r"〔§\s*(117|113|114)\."},
            {"kind": "not_contains", "value": "十类不可混引"},
        ],
    },
    {
        "case_id": "out-08",
        "prompt": "新上一条坚果烘焙线，帮我说明危害分析六列工作表怎么填，以及哪些危害需要设预防控制。",
        "assertions": [
            {"kind": "contains", "value": "危害分析"},
            {"kind": "regex", "value": r"117\.130|六列"},
        ],
    },
    {
        "case_id": "out-09",
        "prompt": "食品过敏原标签问答 Ed.5 对「may contain」这类预防性标签和主要过敏原清单是怎么说的？",
        "assertions": [
            {"kind": "contains", "value": "过敏原"},
            {"kind": "regex", "value": r"Ed\.5|第五版|2025"},
        ],
    },
    {
        "case_id": "out-10",
        "prompt": "FDA 明天来现场检查，FSP 与记录举证要提前准备什么？PCQI 当天不在厂里可以吗？",
        "assertions": [
            {"kind": "contains", "value": "记录"},
            {"kind": "regex", "value": r"FDA|检查"},
        ],
    },
]
assert len({c["case_id"] for c in OUTPUT_CASES}) == 10
dump("output-suite.json", {
    "suite_id": "fda-pchf-v4-7-output-v1",
    "target": TARGET,
    "split_seed": 42,
    "output_cases": OUTPUT_CASES,
})


# ---------------------------------------------------------------- 3. 能力卡路由套件
CAPS = [
    ("CAP-01", "hazard-analysis-method", "新上一条坚果烘焙线，帮我按六列工作表做危害分析，判断哪些危害必须写进 FSP、哪些要设预防控制。"),
    ("CAP-02", "management-components", "杀菌温度监控记录发现偏离，怎么判定走 correction 还是 corrective action？隔离范围、记录审查和 7 working days 怎么落？"),
    ("CAP-03", "process-control-validation", "巴杀工艺关键限值怎么定？文献里的 D 值能直接拿来用吗，validation 研究（热分布/热穿透）要怎么做？"),
    ("CAP-04", "environmental-pathogen-sanitation", "RTE 车间湿区检出李斯特菌，环境监测要怎么升级？transient 与 resident 菌株怎么区分和根除？"),
    ("CAP-05", "allergen-program", "共线生产含花生与不含花生的产品，排产顺序怎么排？换产清洁等级怎么判，什么时候要专项过敏原清洁？"),
    ("CAP-06", "chemical-hazard-controls", "婴幼儿米粉的无机砷风险怎么在供应链端控制？Closer to Zero 的进展要不要持续查新？"),
    ("CAP-07", "supply-chain-verification", "供应商原料存在 SAHCODH 危害，验证活动怎么选？年度审查是默认权利吗，检测能不能当唯一手段？"),
    ("CAP-08", "recall-plan", "Class I 召回时书面通讯要包含哪些要素？Reportable Food Registry 的 24 小时报告怎么联动？"),
    ("CAP-09", "regulatory-boundaries", "我们做酸化食品，还要不要遵守 21 CFR Part 117 的 Subparts C/G？哪些法定义务是绝对不能免的？"),
    ("CAP-10", "reference-tools-discipline", "附录 1 Table 1K 打了 X，是不是就直接写进 FSP？干配料水合之后要不要重新判，书面 No 理由怎么写？"),
    ("CAP-11", "exemption-withdrawal-procedure", "FDA 要撤销我们的 qualified facility 豁免，申辩和上诉各有多少天？什么情况下逾期自动生效？"),
    ("CAP-12", "environmental-engineering-controls", "厂房地面排水坡度与天花板冷凝水怎么设计才符合 cGMP？设备布局要留多大检修与清洁空间？"),
    ("CAP-13", "personnel-hygiene-controls", "员工手部卫生与疾病报告制度怎么写？戴手套能不能替代洗手，首饰和假睫毛怎么管？"),
    ("CAP-14", "cgmp-compliance-guide", "做一次 cGMP 内审，SECG 按主题的分诊索引怎么查？哪些内容仍是旧 part 110 的、哪些已经是 117 法条？"),
    ("CAP-15", "defect-action-levels", "一批冷冻菠菜检出蚜虫数量偏高，Food Defect Levels Handbook 的行动水平怎么判？能不能靠混合稀释达标？"),
    ("CAP-16", "inspection-readiness", "FDA 明天来现场检查，前台接待、FSP 与记录举证怎么准备？PCQI 不在场怎么办？"),
    ("CAP-17", "inspection-sampling", "检查员现场要取样，样品量与份数怎么定？阳性结果出来后的应对与申诉流程是什么？"),
    ("CAP-18", "investigator-authority-procedure", "检查员要求进生产线拍照并复印记录，权限边界在哪？Form 482/483 该怎么签收与回应？"),
    ("CAP-19", "lacf-inspection-program", "CP 7303.070 对低酸/酸化罐头企业的检查怎么分流到 Part 117 或专项程序？RRA 算不算一次 inspection？"),
    ("CAP-20", "lacf-statutory-requirements", "§ 113.100(g) 和 § 114.100(e) 的记录保存期限到底有什么不同？part 11 电子记录条款适用于哪一部？"),
]
routing_cases = [
    {"case_id": f"route-{cid[4:]}", "capability_id": cid, "prompt": prompt,
     "expected_capability": slug}
    for cid, slug, prompt in CAPS
]
assert len(routing_cases) == 20
assert len({c["expected_capability"] for c in routing_cases}) == 20
dump("routing-suite.json", {
    "suite_id": "fda-pchf-v4-7-routing-v1",
    "target": TARGET,
    "candidate_capabilities": [slug for _, slug, _ in CAPS],
    "routing_cases": routing_cases,
})

print("\nsibling targets:", sorted({c["sibling_target"] for c in cases if c["expected"] == "sibling"}))
print("trigger expected dist:", {
    k: sum(1 for c in cases if c["expected"] == k)
    for k in sorted({c["expected"] for c in cases})
})
