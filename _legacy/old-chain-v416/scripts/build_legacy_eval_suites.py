#!/usr/bin/env python3
"""生成 v4.8 / v4.9 历史用例补测套件（只读正式套件/历史套件，不改任何正式产物）。

背景：
  PIPELINE_STATE.md 的 v4.8 / v4.9 段各自留了「10 条用例与 CAP-21 / CAP-22
  路由正确性待后续补测」的欠账；v4.10 补测报告也把它列为「仍未关闭」。
  本脚本按 v4.10 完全相同的框架把 20 条历史用例跑一遍。

产出（全部落在 .cangjie/v4-8-v4-9-legacy-eval/）:
  trigger-suite.json   20 条历史用例 + v4.7 的 8 sibling + 10 负例 = 38 条, runs=3
  output-suite.json    20 条 output case，每条 4 条机械断言（共 80 条）
  routing-suite.json   23 张卡基础 + 20 条历史 prompt + 3 条 CAP-23 对照 = 46 条
  packets-trigger/     官方 run_trigger_evals.py prepare 生成的盲判包
  packets-output/      官方 run_output_evals.py prepare + 条件注入
  packets-routing/     自建盲判包（仿 v4.7 finalize_eval_packets.py）

口径沿用 v4.7 / v4.10，保证数字可比:
  - edge_case → should_trigger（v4.7 适配器口径；这 20 条的 notes/expected_behavior
    都明确要求激活技能，无一条是「不应触发」）
  - 5-skill catalog 与 v4.7 完全一致（评测设定，非本机实际安装清单，报告中标注）
  - sibling / 负例原文复用 v4.7 trigger-suite-v2.json，不改写
  - 输出变体沿用 v410_skill / without_skill（跑的是当前 v4.10 已安装产物）
  - 正式 test-prompts.json、SKILL.md、dist-v14、已安装技能一律不改动

两个历史文本差异（重要，报告中须说明）:
  1. v4.9 的 10 条 seafood-* 只有 notes、没有 expected_behavior；其 4 条断言改由
     notes + 已安装 CAP-22 卡片正文的知识点锚定，不臆造 expected_behavior。
  2. 部分 v4.8 expected_behavior 仍写「全包十四类不可混引」（v4.8 当时口径），
     当前 v4.10 已升为十五类。相关断言写成 十[四五]类，且正式用例原文一字不改。
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

CANGJIE = Path(__file__).resolve().parent
BOOK = CANGJIE.parent
E = CANGJIE / "v4-8-v4-9-legacy-eval"
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

CAP21 = "fsvp-inspection-program"
CAP22 = "seafood-haccp-statutory-requirements"
CAP23 = "seafood-hazards-controls-guide"

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
    (E / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    key = next((k for k in ("trigger_cases", "output_cases", "routing_cases") if k in obj), "?")
    print(f"wrote {name}: {len(obj[key])} {key}")


# ---------------------------------------------------------------- 0. 历史用例
formal = json.loads(FORMAL.read_text(encoding="utf-8"))
assert formal["version"] == "4.10", "正式套件版本应为 4.10（当前产物）"
legacy = [c for c in formal["test_cases"]
          if c["id"].startswith("fsvp-")
          or (c["id"].startswith("seafood-") and not c["id"].startswith("seafood-hazards-"))]
assert len(legacy) == 20, f"历史用例应为 20 条，实得 {len(legacy)}"
fsvp = [c for c in legacy if c["id"].startswith("fsvp-")]
sf = [c for c in legacy if c["id"].startswith("seafood-")]
assert len(fsvp) == 10 and len(sf) == 10
assert all("expected_behavior" in c for c in fsvp)
assert all("expected_behavior" not in c and "notes" in c for c in sf)
print("历史用例: v4.8 fsvp-* 10 条（有 expected_behavior） + v4.9 seafood-* 10 条（仅 notes）")


# ---------------------------------------------------------------- 1. 触发套件
MAP = {"should_trigger": "should_trigger",
       "edge_case": "should_trigger",
       "should_not_trigger": "should_not_trigger"}
cases = [{"case_id": c["id"], "prompt": c["prompt"],
          "expected": MAP[c["type"]], "runs": 3} for c in legacy]
assert all(c["expected"] == "should_trigger" for c in cases), "20 条历史用例均要求激活技能"

v2 = json.loads(SUITE_V2.read_text(encoding="utf-8"))
controls = [c for c in v2["trigger_cases"] if c["case_id"].startswith(("sib-", "neg-"))]
assert len([c for c in controls if c["case_id"].startswith("sib-")]) == 8
assert len([c for c in controls if c["case_id"].startswith("neg-")]) == 10
for c in controls:
    cases.append({"case_id": c["case_id"], "prompt": c["prompt"],
                  "expected": c["expected"], "runs": 3,
                  **({"sibling_target": c["sibling_target"]} if "sibling_target" in c else {})})
assert len(cases) == 38 and len({c["case_id"] for c in cases}) == 38
dump("trigger-suite.json", {
    "suite_id": "fda-pchf-v4-8-v4-9-legacy-trigger",
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
# 每条 4 条断言：v4.8 的 10 条按 expected_behavior 逐点抽取；
# v4.9 的 10 条按 notes + 已安装 CAP-22 卡片正文的知识点锚定。
# 全部为官方 check_assertion 支持的 regex，尽量给合法别名，避免 v4.10 那种
# 「断言写死 Table 3-4、答案用简写 3-4」的措辞缺陷。
def R(*alts: str) -> dict:
    return {"kind": "regex", "value": "|".join(alts)}


OUTPUT_CASES = [
    # ---------------- v4.8 / CAP-21 ----------------
    {"case_id": "fsvp-out-01", "source_case": "fsvp-01",
     "prompt": "我们公司既做进口也是加工厂，已经按 21 CFR Part 117 做了完整的供应链验证，是不是就不用单独建 FSVP 了？",
     "assertions": [
         R(r"deemed|视为符合|视为已符合"),
         R(r"1\.509|section 1\.509"),
         R(r"DUNS|UFI|entry line|每一条|每一 entry|入境标识"),
         R(r"Part 117|part 117|117\.135|Subpart G|供应链"),
         R(r"805|subpart L|两套|不同.{0,8}(法源|主体)|receiving facility|不是.{0,6}进口商"),
     ]},
    {"case_id": "fsvp-out-02", "source_case": "fsvp-02",
     "prompt": "FDA 通知下周来做 FSVP 检查，我们要按 CP 7303.050 准备多少 subs 样品、环境拭子怎么布点？",
     "assertions": [
         R(r"不取样|不(会|应|能).{0,6}取(样|集)|Samples will not|Intentionally Left Blank|PART IV|全(部|节)?(留)?空"),
         R(r"7303\.050|subs|环境拭子|Zone\s*1|WGS|串轨|另一个 program"),
         R(r"危害分析|供应商(批准|评价)|验证活动|纠正措施|483a|六组|记录"),
         R(r"on-site|remote|现场|远程|EIR|CAR"),
     ]},
    {"case_id": "fsvp-out-03", "source_case": "fsvp-03",
     "prompt": "报关时那个 UFI 到底填什么？是每家企业报一次还是每次进口都要报？",
     "assertions": [
         R(r"entry line|每一条|每一(次)?(报关|进口)|each entry|每次"),
         R(r"DUNS|UFI"),
         R(r"1\.509|CBP|电子|electronically|名称|邮箱"),
         R(r"deemed|例外|不免|不能免|仍(然|须|要)|不是.{0,8}(一次|每年)|PART V"),
     ]},
    {"case_id": "fsvp-out-04", "source_case": "fsvp-04",
     "prompt": "我们进口果汁、水产品、酒精饮料，还有一批只过境转运的货，哪些可以不做 FSVP？",
     "assertions": [
         R(r"1\.501|八类|豁免"),
         R(r"part 120|120|果汁|水产|part 123|123|有条件|条件性"),
         R(r"转运|过境|酒精|研究|个人消费|USDA|复出口|退回"),
         R(r"十[四五]类|不可混引|转引未收|1\.509|不取样"),
     ]},
    {"case_id": "fsvp-out-05", "source_case": "fsvp-05",
     "prompt": "我们符合极小进口商 VSI 的条件，是不是就必须走 modified requirements？standard 那套还能选吗？",
     "assertions": [
         R(r"standard|标准.{0,4}要求"),
         R(r"modified|1\.507|1\.511|1\.512|1\.513|VSI|膳食补充剂|SRA"),
         R(r"可以(选择|选)|may choose|可选|不是强制|非强制|并非.{0,6}必须"),
         R(r"EIR|独立|No FSVP|资格证明|PART III"),
     ]},
    {"case_id": "fsvp-out-06", "source_case": "fsvp-06",
     "prompt": "刚收到 FSVP 检查的 Form FDA 483a，哪些观察项算最严重、会怎么升级？",
     "assertions": [
         R(r"PART V|483a|观察|重大"),
         R(r"危害分析|供应商(批准|评价)|验证活动|书面索取|及时提供|记录"),
         R(r"Warning Letter|警告信|99-41|Import Alert|801\(a\)\(3\)|拒绝入境|regulatory meeting|Untitled Letter"),
         R(r"direct reference|有限情形|CMS|Center|自愿纠正|NAI|VAI|OAI|裁量"),
     ]},
    {"case_id": "fsvp-out-07", "source_case": "fsvp-07",
     "prompt": "第一次 FSVP 检查被开了缺陷，是不是马上会收到警告信、货也会被扣？",
     "assertions": [
         R(r"首次|initial|Initial"),
         R(r"不默认|不(一定|必然)|only when|仅在|已知.{0,10}风险|prioritized|优先执法"),
         R(r"voluntary|自愿|纠正|compliance|裁量|违法史"),
         R(r"十[四五]类|不创设|作业指导|不得|不是必然|不得写成"),
     ]},
    {"case_id": "fsvp-out-08", "source_case": "fsvp-08",
     "prompt": "公司被列进 Import Alert 99-41 了，是不是所有进口食品都进不来？要怎么才能移除？",
     "assertions": [
         R(r"99-41|Red List"),
         R(r"具体食品|食品.{0,8}供应商|组合|或全部食品|all food"),
         R(r"未(被)?列(入|名)|不在|may continue|仍(可|能)|不是所有|并非所有|可以继续"),
         R(r"移除|removal|Division|CMS|先.{0,6}申请|prior to attempting"),
     ]},
    {"case_id": "fsvp-out-09", "source_case": "fsvp-09",
     "prompt": "Import Alert 99-41 和做低酸罐头时说的 99-37/99-38 是一回事吗？没备案是不是就自动 DWPE？",
     "assertions": [
         R(r"99-37|99-38"),
         R(r"7303\.070|LACF|低酸|酸化|scheduled process|备案"),
         R(r"不得仅因|不能仅|未注册|未备案|DWPE|FURLS|FCE|SID|Center Views"),
         R(r"801\(a\)\(3\)|法律 hook|触发条件|不同|不得混|十[四五]类"),
     ]},
    {"case_id": "fsvp-out-10", "source_case": "fsvp-10",
     "prompt": "CP 7303.878 首页写着 2025 年签发，是新规吧？顺便把 21 CFR 1.505 原文、Import Alert 99-41 全文和 FSVP Guidance Q&A G.8 列出来。",
     "assertions": [
         R(r"不是.{0,10}(新规|新程序|新 ?program)|2023 版|2023-09-27|09/27/2023|Transmittal|2023-CPM"),
         R(r"Corrections|更正|POC|机构名称|2025-08-28|08/28/2025|Change History|2021"),
         R(r"转引未收|未收|不得(从|反推)"),
         R(r"1\.505|Import Alert 99-41|Q&A|G\.8|subpart L|1\.500|Guidance"),
     ]},
    # ---------------- v4.9 / CAP-22 ----------------
    {"case_id": "sf-out-01", "source_case": "seafood-01",
     "prompt": "我们做烟熏三文鱼，厂长说按 21 CFR 123.16 控制肉毒就够，不用做完整 HACCP。这样对吗？",
     "assertions": [
         R(r"123\.16"),
         R(r"part 113|part 114|113|114|LACF|酸化|密封容器"),
         R(r"只(是|排|排除|限于)|例外|不(是|代表|等于)|仍(然|须|要)|Subpart A|123\.6"),
         R(r"HACCP 计划|危害分析|货架期|123\.6|至少整个"),
     ]},
    {"case_id": "sf-out-02", "source_case": "seafood-02",
     "prompt": "水产品厂是不是只要符合 part 123 就免了 PCHF 的 Subparts C 和 G？",
     "assertions": [
         R(r"123\.5\(a\)|默认|Except as provided"),
         R(r"117\.5\(b\)|两个|双条件|required to comply|in compliance"),
         R(r"Subparts? C|Subpart G|C/G|CGMP|Subpart B"),
         R(r"activities|活动|按活动|不是整厂|受.{0,8}管辖|只免"),
     ]},
    {"case_id": "sf-out-03", "source_case": "seafood-03",
     "prompt": "part 113 的豁免只限微生物危害，那水产品的 117.5(b) 是不是也只限微生物危害？",
     "assertions": [
         R(r"117\.5\(b\)"),
         R(r"117\.5\(d\)\(2\)|part 113|微生物|microbiological"),
         R(r"没有.{0,10}(限缩|对应)|不限缩|无限缩|不(只|仅)限|无.{0,4}限缩款"),
         R(r"两个方向|两头都错|高估|低估|不是整厂|不能.{0,6}整厂|activities|活动|化学|物理"),
     ]},
    {"case_id": "sf-out-04", "source_case": "seafood-04",
     "prompt": "21 CFR 123.9 的 HACCP 记录要保存几年？冷藏和冷冻一样吗？",
     "assertions": [
         R(r"123\.9"),
         R(r"冷藏|refrigerated"),
         R(r"1\s*年|一年"),
         R(r"2\s*年|两年|冷冻|保藏|货架稳定|Part 113|Part 114|三套"),
     ]},
    {"case_id": "sf-out-05", "source_case": "seafood-05",
     "prompt": "进口冷冻虾，我们拿到了境外厂的 HACCP 计划副本，是不是 123.12 和 FSVP 都算满足了？",
     "assertions": [
         R(r"123\.12"),
         R(r"FSVP|805|subpart L|part 1"),
         R(r"两套|双轨|互不替代|不(等于|自动)|不能.{0,8}(替代|满足)|不是一回事"),
         R(r"deemed|1\.509|拒绝入境|123\.12\(d\)|HACCP 计划副本|affirmative step"),
     ]},
    {"case_id": "sf-out-06", "source_case": "seafood-06",
     "prompt": "生食牡蛎的 shellstock 容器上那个 tag 要写哪些内容？要不要保存记录？",
     "assertions": [
         R(r"123\.28|shellstock|tag|标牌"),
         R(r"五(项|个|要素)|采捕|harvester|dealer|认证加工者|approved growing waters|生长区"),
         R(r"123\.9\(e\)|不受|除非|例外|保存|记录"),
         R(r"1240\.60|NSSP|转引未收|未收|不得|贝类|牡蛎"),
     ]},
    {"case_id": "sf-out-07", "source_case": "seafood-07",
     "prompt": "CCP 监控记录最晚多久要有人复核签字？",
     "assertions": [
         R(r"123\.8"),
         R(r"1\s*周|一周|7\s*天|within 1 week"),
         R(r"每年|至少每年|annual|至少.{0,4}一年|复审|重新评价"),
         R(r"监控记录|CCP|纠正措施记录|123\.8\(a\)\(1\)|记录"),
     ]},
    {"case_id": "sf-out-08", "source_case": "seafood-08",
     "prompt": "烟熏鱼偏离了关键限值，我们组长直接把产品放行了，说反正后面还要检。合规吗？",
     "assertions": [
         R(r"123\.7"),
         R(r"隔离|扣留|segregate|hold|不得放行|不能放行|不合规|不可以"),
         R(r"关键限值|偏离|critical limit|deviation|CL"),
         R(r"商业|commerce|不合格品|不得使|123\.7\(b\)\(1\)|评价|评估"),
     ]},
    {"case_id": "sf-out-09", "source_case": "seafood-09",
     "prompt": "21 CFR 123 里 SSOP 写的是 should，是不是可以不建立？",
     "assertions": [
         R(r"123\.11"),
         R(r"should"),
         R(r"shall"),
         R(r"不(得|能).{0,10}(升格|当成|说成)|也不(能|得).{0,10}(不做|可以不)|监测|记录|八项|sufficient frequency|不能.{0,6}不做"),
     ]},
    {"case_id": "sf-out-10", "source_case": "seafood-10",
     "prompt": "我们厂既做烟熏鱼又做低酸罐头，HACCP 计划要不要分两套？肉毒控制按哪个法条？",
     "assertions": [
         R(r"123\.16"),
         R(r"part 113|113|LACF|低酸罐头|密封容器|pH|114"),
         R(r"只(排|排除|是)|例外|Subpart A|仍(然|须|要)|不(是|等于).{0,6}免"),
         R(r"两套|分(两套|开)|分别|分流|CAP-20|123\.6|货架期"),
     ]},
]
assert len({c["case_id"] for c in OUTPUT_CASES}) == 20
assert all(len(c["assertions"]) >= 4 for c in OUTPUT_CASES)
N_ASSERT = sum(len(c["assertions"]) for c in OUTPUT_CASES)
for c in OUTPUT_CASES:                       # 正则合法性自检
    for a in c["assertions"]:
        re.compile(a["value"])
suite_out = {"suite_id": "fda-pchf-v4-8-v4-9-legacy-output",
             "target": "fda-pchf-food-safety", "split_seed": 42,
             "output_cases": [{k: v for k, v in c.items() if k != "source_case"}
                              for c in OUTPUT_CASES]}
dump("output-suite.json", suite_out)
(E / "output-case-map.json").write_text(json.dumps(
    {c["case_id"]: {"source_case": c["source_case"], "prompt": c["prompt"]}
     for c in OUTPUT_CASES}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- 3. 能力卡路由套件
v47route = json.loads(SUITE_ROUTE_V47.read_text(encoding="utf-8"))
base_cases = [dict(c) for c in v47route["routing_cases"]]
assert len(base_cases) == 20
EXTRA_BASE = [
    ("CAP-21", CAP21, "CP 7303.878 检查 FSVP 进口商时，PART IV 为什么全空、不取样？§1.509 每 entry line 要申报什么？"),
    ("CAP-22", CAP22, "21 CFR Part 123 的 §123.12 进口商验证有哪两条可选路径？affirmative steps 列在哪一款？"),
    ("CAP-23", CAP23, "我们做冷冻金枪鱼排，Ch.3 的 Table 3-2 里组胺那栏没打勾，危害分析能不能直接写「不显著」？"),
]
for cid, slug, prompt in EXTRA_BASE:
    base_cases.append({"case_id": f"route-{cid[4:]}", "capability_id": cid,
                       "prompt": prompt, "expected_capability": slug})
assert len(base_cases) == 23

# 20 条历史用例 prompt 直接作为路由题：v4.8 10 条的 expected_behavior 均明写主卡 CAP-21；
# v4.9 9 条的 notes 均考 Part 123 法条层 → CAP-22；seafood-10 是 CAP-22/CAP-20 分流边界题，
# 按 notes 主卡记 CAP-22，但报告中单独标注多解、另给「不含该条」的稳健数字。
LEGACY_ROUTE_META = {}
for c in fsvp:
    base_cases.append({"case_id": c["id"], "capability_id": "CAP-21",
                       "prompt": c["prompt"], "expected_capability": CAP21})
    LEGACY_ROUTE_META[c["id"]] = {"capability_id": "CAP-21", "version": "v4.8",
                                  "basis": "expected_behavior 明写主卡 fsvp-inspection-program"}
for c in sf:
    base_cases.append({"case_id": c["id"], "capability_id": "CAP-22",
                       "prompt": c["prompt"], "expected_capability": CAP22})
    LEGACY_ROUTE_META[c["id"]] = {"capability_id": "CAP-22", "version": "v4.9",
                                  "basis": "notes 考 Part 123 法条层"}
LEGACY_ROUTE_META["seafood-10"]["open_boundary"] = True
LEGACY_ROUTE_META["seafood-10"]["note"] = "notes 明说分流 CAP-22 与 CAP-20，top-1 无唯一解；单独统计"

# CAP-23 对照 3 条：确认历史用例的定向不会把新卡吃掉（v4.10 已验证，这里作退化回归）
for cid, prompt in [
    ("lcap23-a", "从描述产品、画流程图到定监控频率，把海产品 HACCP 危害分析完整判定链走一遍。"),
    ("lcap23-b", "Hazard Analysis Worksheet 第 3 栏填 No，第 4 栏还要写理由吗？后面哪些步骤能跳过？"),
    ("lcap23-c", "指南 Appendix 5 的 50 ppm / 500 ppm 能不能直接抄进 HACCP 计划当关键限值？"),
]:
    base_cases.append({"case_id": cid, "capability_id": "CAP-23",
                       "prompt": prompt, "expected_capability": CAP23})

index_text = Path(CAP_INDEX).read_text(encoding="utf-8")
slugs = sorted(set(re.findall(r"capabilities/([a-z0-9-]+)\.md", index_text)))
assert len(slugs) == 23, f"能力索引应含 23 张卡，实得 {len(slugs)}"
assert all(c["expected_capability"] in slugs for c in base_cases)
assert len(base_cases) == 46 and len({c["case_id"] for c in base_cases}) == 46
dump("routing-suite.json", {
    "suite_id": "fda-pchf-v4-8-v4-9-legacy-routing-v1",
    "target": "fda-pchf-food-safety",
    "candidate_capabilities": slugs,
    "open_boundary_cases": ["seafood-10"],
    "routing_cases": base_cases,
})
(E / "routing-legacy-meta.json").write_text(
    json.dumps(LEGACY_ROUTE_META, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- 4. 官方 prepare + 盲判包
def run(cmd: list[str]) -> None:
    print("+", " ".join(str(x) for x in cmd))
    subprocess.run([sys.executable] + [str(x) for x in cmd], check=True)


run([TRIGGER, "prepare", E / "trigger-suite.json",
     "--skills", ",".join(SKILLS), "--out", E / "packets-trigger", "--set", "all"])
run([OUTPUT, "prepare", E / "output-suite.json",
     "--out", E / "packets-output", "--variants", "v410_skill,without_skill"])

mapping = json.loads((E / "packets-output/mapping.json").read_text(encoding="utf-8"))
HINTS = {
    "v410_skill": (
        f"可用参考材料（请先读取再作答）：{INSTALLED.as_posix()}/SKILL.md 与其 references/ 下的能力卡、"
        "capability-index.md、glossary.md。遇到条款号、期限、来源分层、转引未收等问题请以材料为准。"
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
assert n == 40

ROUTP = E / "packets-routing"
ROUTP.mkdir(parents=True, exist_ok=True)
# instruction 沿用 v4.10 的原句（已点名 CAP-22/23 分工，为可比性保留），补 CAP-21 一层。
INSTR = (
    "你是一个未参与蒸馏的干净 agent。已安装技能 fda-pchf-food-safety 内含 23 张能力卡，"
    f"候选清单（卡 id / 标题 / 重要度 / 意图 / 关键词 / 卡文件）见：{CAP_INDEX}；请先读取该文件。"
    "对用户 prompt 只判断应加载哪一张能力卡（top-1），不得输出多张。"
    "注意 CAP-21 是 FSVP 进口商检查程序层（CP 7303.878）、CAP-22 是 21 CFR Part 123 法条义务层、"
    "CAP-23 是 FDA 技术指南层的危害分析判定链，"
    "按问题实际问的是「法定义务/条款号」还是「进口商检查/执法程序」还是「怎么判/怎么填表/怎么定 CCP」来区分，"
    "不要按关键词一概论。"
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
    "# 盲判说明（v4.8 / v4.9 历史用例补测）\n\n"
    "- 触发：`packets-trigger/*.json` 共 38 条，3 个干净 sub-agent 各完整判一遍 → results-trigger/run{1,2,3}.jsonl。\n"
    "- 输出：`packets-output/<case_id>/task-<label>.json` 共 40 个 → 按包内 output_file 写出 <label>.md；"
    "mapping.json 不得交给评审 sub-agent。\n"
    "- 路由：本目录共 46 条，3 个干净 sub-agent 各完整判一遍 → results-routing/run{1,2,3}.jsonl。\n"
    "- 所有 judge 只看 prompt + 候选索引，**不得**看到 suite 中的 expected / expected_capability。\n",
    encoding="utf-8")

print("\nBUILD_LEGACY_EVAL_OK")
print(f"catalog skills : {len(SKILLS)}")
print(f"trigger cases  : {len(cases)} (20 legacy + 8 sibling + 10 negative), x3 = {len(cases)*3} 判")
print(f"output cases   : {len(OUTPUT_CASES)} x2 变体 = 40 份答案 / {N_ASSERT} 条断言")
print(f"routing cases  : {len(base_cases)} (23 基础 + 20 历史 + 3 CAP-23 对照), x3 = {len(base_cases)*3} 判")
