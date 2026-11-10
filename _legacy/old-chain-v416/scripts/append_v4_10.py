#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""append_v4_10.py — v4.10 增量追加：术语 t173–t182 + 10 条评测用例。

沿用包内 append_v4_9.py 的约定：
- 唯一性断言 + 内存暂存 + 末尾一次性落盘；
- 先备份到 .cangjie/backup-v4-10-pre-append/；
- 只改 candidates/glossary.md（GLOSSARY.md 与 book/glossary.md 由 assemble_bundle.py 复制同步），
  不手改生成物。
"""
import json
import re
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
BACKUP = BASE / ".cangjie/backup-v4-10-pre-append"
GLOSS = BASE / "candidates/glossary.md"
DRAFT = BASE / "candidates/v4-10-glossary.md"
TESTS = BASE / "test-prompts.json"

BACKUP.mkdir(parents=True, exist_ok=True)
pending = {}

# ---------------------------------------------------------------- 1. 术语
g = GLOSS.read_text(encoding="utf-8")
draft = DRAFT.read_text(encoding="utf-8")
m = re.search(r"## 可直接粘贴的 YAML 草案\s*\n\s*```yaml\n(.*?)\n```", draft, re.S)
assert m, "术语草案中未找到 YAML 块"
terms = "\n".join(l for l in m.group(1).splitlines() if not l.lstrip().startswith("#")).strip("\n")
assert terms.count("- id: t") == 10, f"术语条数应为 10，实得 {terms.count('- id: t')}"
assert not any(f"- id: t{i}" in g for i in range(173, 183)), "t173–t182 已存在，拒绝重复追加"

fences = [x.start() for x in re.finditer(r"^```", g, re.M)]
assert len(fences) >= 2, "glossary.md 的 fenced YAML 块结构异常"
insert_at = fences[1]
g2 = g[:insert_at] + terms + "\n\n" + g[insert_at:]

selfcheck = (
    "\n- [x] 第十五来源 **FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版"
    "（June 2022，SGR 129）** 技术指南已并入，术语 t173–t182 共 10 条，围绕**完整危害分析判定链**排布："
    "should 的效力层级 → hazard analysis 与 HACCP plan 书面化义务不对称 → species/process-related 二分 → "
    "reasonably likely to occur 与无控制假设态 → significant hazard 等价且不等于本步设 CCP → "
    "Worksheet 六栏 → control strategy example 与 CCP 漂移 → CCP 至少一个 → critical limit 与替代限值论证 → "
    "监控四问。引文取自 CAP-23 R 段经 `.cangjie/verify_v4_10_quotes.py` 逐字核验的 **37 个英文引用块**"
    "（37/37 命中源文件正文区，0 超 100 词，0 表格引用）。原文标「Seafood Hazards Guide 第 4 版 Ch.x / L####」，"
    "法条标〔§ 123.xxx〕，两者不可混引；CP 7303.842、NSSP Guide、part 120/1240/108/110/507、"
    "Appendix 5 回指的 CPG 与 CFR 外部法源一律标『转引未收』。全库 **182 条**，v4.10，**十五类来源不可混引**。\n"
)
assert "第十五来源" not in g2, "自检记录已存在，拒绝重复追加"
g2 += selfcheck
pending[GLOSS] = g2

# ---------------------------------------------------------------- 2. 用例
d = json.loads(TESTS.read_text(encoding="utf-8"))
assert len(d["test_cases"]) == 105, f"基线用例应为 105，实得 {len(d['test_cases'])}"
assert not any(c["id"].startswith("seafood-hazards-") for c in d["test_cases"]), "v4.10 用例已存在"

CASES = [
    {
        "id": "seafood-hazards-01", "type": "should_trigger",
        "prompt": "我们做冷冻金枪鱼排，查了 Ch.3 的 Table 3-2，表里这个鱼种组胺那栏没打勾，是不是危害分析里就可以直接写「组胺不显著」？",
        "expected_behavior": "应激活本技能并加载 seafood-hazards-controls-guide 卡：① Ch.3 三张表只列**潜在**危害，指南明文 `the tables should not be used separately for this purpose`，必须结合 Ch.4–21 各章与自身/外部专家判断；② 显著性闸门是 `reasonably likely to occur`，且须在**无控制条件下**判定；③ 表未打勾不等于该危害在本厂工艺下不发生，新出现危害与物种替换由加工者自行警觉；④ 结论落在 Worksheet 第 3 栏 Yes/No，且**第 4 栏无论 Yes/No 都要写理由**；⑤ 法定义务回〔§ 123.6〕/CAP-22，不得把指南表当合规清单。全包十五类不可混引。",
        "notes": "v4.10：表不可单独用 + 潜在危害≠显著危害",
    },
    {
        "id": "seafood-hazards-02", "type": "should_trigger",
        "prompt": "我们船上一直有时间温度控制，这几年从没检出过组胺，是不是就能判定组胺不是显著危害、不用写进 HACCP 计划？",
        "expected_behavior": "应激活并加载 seafood-hazards-controls-guide 卡：① 指南 Ch.2/Ch.3 要求 `The likelihood of a hazard occurring should be judged in the absence of controls`；② 已有控制有效恰恰可能是「鱼本身不能产组胺」或「控制压住了危害」两种情形之一——**前者才判不显著，后者仍属 reasonably likely to occur 且控制须纳入 HACCP 计划**；③ 把「没出过事」当「不显著」是本卡头号误读；④ 书面理由写入第 4 栏；⑤ 组胺 50/500 ppm 出自 CPG Sec. 540.525（转引未收），不是本指南新设限值。",
        "notes": "v4.10：无控制条件下判定与组胺二选一实例",
    },
    {
        "id": "seafood-hazards-03", "type": "should_trigger",
        "prompt": "接收步骤判定组胺显著，是不是 CCP 就必须设在接收这一步？",
        "expected_behavior": "应激活并加载 seafood-hazards-controls-guide 卡：① 指南 Step 10 判显著、Step 11 独立定位 CCP，`identifying a hazard as significant at a processing step does not mean that it must be controlled at that processing step`；② 用 Appendix 3 的 CCP 判定树判断是否该步必需控制；③ 每个显著危害**至少一个** CCP（法源〔§ 123.6(c)(2)〕，回 CAP-22），可多于一个，一步骤也可兼多个危害的 CCP；④ 同一危害换一条 control strategy example，CCP 位置会变；⑤ Appendix 3 判定树在导出件里塌陷成残表，只可复原逻辑、不得逐字引用。",
        "notes": "v4.10：显著≠该步控制 + CCP 判定树 + 策略漂移",
    },
    {
        "id": "seafood-hazards-04", "type": "should_trigger",
        "prompt": "危害分析工作表第 3 栏填了 No 的那些步骤，第 4 栏还要写理由吗？后面 18 步是不是都得走完？",
        "expected_behavior": "应激活并加载 seafood-hazards-controls-guide 卡：① 第 4 栏理由对 `Yes` 与 `No` **同等必填**，是后续强制复审与监管质询的唯一举证位；② 第 3 栏答 No 的步骤**可跳过 Steps 11–18**，第 6 栏答 No 的步骤可跳过 Steps 12–18；③ 六栏工作表（步骤/潜在危害/是否显著/理由/预防措施/是否 CCP）与 HACCP Plan Form 十栏的映射要说清；④ 法规〔§ 123.6〕不要求危害分析书面化，但 FDA 期望书面化以便举证——不得把 PCHF 的书面危害分析义务套到 Part 123；⑤ 全包十五类不可混引。",
        "notes": "v4.10：六栏工作表、理由必填与步骤跳过规则",
    },
    {
        "id": "seafood-hazards-05", "type": "should_trigger",
        "prompt": "帮我把海产品 HACCP 危害分析从头到尾走一遍：从描述产品到定监控频率，完整判定链是什么？",
        "expected_behavior": "应激活并加载 seafood-hazards-controls-guide 卡，给出**完整判定链**：① Preliminary Steps（一般信息/描述食品、分销储存、预期用途与消费者/流程图）→ ② Step 6 设 Worksheet → ③ Step 7 查 Table 3-2/3-3 品种相关、Step 8 查 Table 3-4 工艺相关（成品形态+包装+储运）→ ④ Step 9 用 Ch.4–21「Understand the Potential Hazard」理解危害 → ⑤ Step 10 在无控制条件下按三情形逐步判显著并写第 3/4 栏 → ⑥ Step 11 判定树定 CCP、写第 5/6 栏 → ⑦ Step 12–13 HACCP Plan Form 设关键限值 → ⑧ Step 14 监控四问 What/How/Frequency/Who → ⑨ Steps 15–18 纠正措施/记录/验证。每步标「指南建议层」；法定义务回〔§ 123.xxx〕/CAP-22；附录 1 表单非强制但可加快监管审查。",
        "notes": "v4.10：完整危害分析判定链主干（用户明确要求）",
    },
    {
        "id": "seafood-hazards-06", "type": "should_trigger",
        "prompt": "指南里写了组胺 50 ppm / 500 ppm、寄生虫 -20°C 7 天，我们直接把这些数抄进 HACCP 计划当关键限值，检查员是不是就认了？",
        "expected_behavior": "应激活并加载 seafood-hazards-controls-guide 卡：① 指南非约束性，`should` 只是建议，`Processors may choose to use other control strategies ... should scientifically establish their adequacy`；② Appendix 5 的 50/500 ppm 回指 CPG Sec. 540.525、兽药残留回指 21 CFR 556、农药回指 40 CFR 180、贝类弧菌回指 NSSP Guide——**是本包转引未收的外部法源快照，不是 FDA 在本指南新设的限值**，且原文提示 `may not always be suitable for critical limits`；③ 关键限值须对应**被监控的参数**，换示例限值须科学论证充分性并符合适用法规；④ 冻结三条件（-20°C 7 天 / -35°C 15 小时 / -35°C 冻实后 -20°C 24 小时）对厚于 6 英寸的大鱼可能不适用，盐渍/醋渍/柠檬汁腌渍**不能**消除寄生虫；⑤ 法条义务回 CAP-22。",
        "notes": "v4.10：建议参数≠法定限值 + 外部法源转引未收 + 控制有效性边界",
    },
    {
        "id": "seafood-hazards-07", "type": "should_trigger",
        "prompt": "同一个组胺危害，Ch.7 给了好几条 Control Strategy Example，我们换一条控制策略，CCP 和关键限值要不要跟着改？",
        "expected_behavior": "应激活并加载 seafood-hazards-controls-guide 卡：① 指南各章对同一危害给一条或多条 control strategy example，`there are often more ways than one to control a hazard. CCP(s) for one control strategy example often differ from those of another example for the same hazard`；② CCP **不是危害的固有属性**，换策略须重跑 Step 11 并重写 Worksheet 第 5/6 栏与 Plan Form 的关键限值、监控四问；③ 示例不是标准答案，可另选但须科学论证充分性；④ Ch.4–21 统一四段式（Understand → Determine Significant → Identify CCPs → Develop Control Strategy）要点明；⑤ 不得把某一章示例写成法定义务。",
        "notes": "v4.10：控制策略示例与 CCP 位置漂移",
    },
    {
        "id": "seafood-hazards-08", "type": "edge_case",
        "prompt": "既然这份指南自己说没有法律约束力、可以用别的控制策略，那我们是不是连 Part 123 要求的书面 HACCP 计划和危害分析都可以不做？",
        "expected_behavior": "必须同时纠正**两个方向**的误读：① 指南非强制（不设 legally enforceable responsibilities、should 只是建议、可替代控制策略）——所以不能把指南的示例表单/限值/表格当合规清单；② **但** 21 CFR Part 123 的 `shall` 义务（〔§ 123.6(a)〕危害分析、〔§ 123.6(b)〕书面 HACCP 计划、〔§ 123.7〕纠正措施、〔§ 123.8〕验证、〔§ 123.9〕记录、〔§ 123.10〕培训）是法条层，不因指南非强制而变成可选，转 CAP-22；③ 指南内凡出现 must / require 多为回指法规，其强制力来自法规；④ 「可用替代控制策略」的前提是 `as long as they comply with the requirements of the applicable food safety laws and regulations` 且 `scientifically establish their adequacy`；⑤ 十五类不可混引。",
        "notes": "v4.10：双向误读——把指南当法规 / 把法条义务稀释成可选",
    },
    {
        "id": "seafood-hazards-09", "type": "edge_case",
        "prompt": "2022 年 6 月第 4 版是新规吧？麻烦把 Appendix 3 的 CCP 判定树逐字原文、CPG 540.525 全文、以及 NSSP 贝类生长区分类都列出来。",
        "expected_behavior": "必须分清可答与转引未收：① **版本口径**——封面 June 2022 第 4 版，但 Ch.3 页脚 `3 - 1 (June 2021)`、Appendix 3 为 `A3-1 (June 2021)`、Appendix 5 为 `A5-1 (June 2021)`、Ch.19 书目为 August 2019，属**分章滚动修订**，不是 2022 新规则；② **转换质量红线**——Appendix 3 的 CCP 判定树在导出件里塌陷成残缺表格，Q1/Q2/Q3 与分支框无法逐字复原，只能给逻辑、须回查 PDF 原版，表格列头连写/页码混入/字符丢失也不得作逐字引用；③ CPG Sec. 540.525 / 555.300 / 575.100、NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507、CP 7303.842、Import Alert 16-xx、BAM 海产品章节**一律标转引未收**；④ 可给的是本指南内的判定方法与出处；⑤ 十五类不可混引。",
        "notes": "v4.10：版本陷阱 + 转换质量红线 + 转引未收边界",
    },
    {
        "id": "seafood-hazards-10", "type": "should_not_trigger",
        "prompt": "按中国 GB 2733 帮我判定这批鲜冻动物性水产品的组胺限量和感官要求，顺便写一份出口欧盟的卫生证书。",
        "expected_behavior": "不应激活本技能给出条款级结论：本包只覆盖 FDA 方法论与 21 CFR 条款，不做中国 GB 标准或欧盟法规的直接合规判定，也不代写官方卫生证书（跨体系映射与文书代写属 out_of_scope / stop_conditions）。应明确说明超出覆盖范围并建议咨询对应法域的专业机构；若用户改问 FDA 海产品危害分析判定链，再转 seafood-hazards-controls-guide 卡。",
        "notes": "v4.10：跨法域与文书代写负例（来源路由互斥）",
    },
]

d["test_cases"].extend(CASES)
old_version = d.get("version")
d["version"] = "v4.10"
d["notes"] = d["notes"] + (
    " | v4.10 追加 10 条 seafood-hazards-* 用例（Ch.3 表不可单独用、无控制条件判定与组胺二选一、"
    "显著≠该步控制与 CCP 判定树、六栏工作表与 Yes/No 理由、完整 18 步判定链、建议参数≠法定限值与外部法源回指、"
    "control strategy example 与 CCP 漂移、双向误读边界、版本陷阱与转引未收、跨法域负例）；"
    "新增第 23 张卡 seafood-hazards-controls-guide，第十五来源为 FDA《Fish and Fishery Products Hazards "
    "and Controls Guidance》第 4 版 June 2022（技术指南层，与 CAP-22 法条层配对），"
    "全包十五类不可混引，全库 182 条术语 / 115 条用例。本版未重跑触发/输出/路由评测。"
)
pending[TESTS] = json.dumps(d, ensure_ascii=False, indent=2) + "\n"

# ---------------------------------------------------------------- 落盘
for p in pending:
    shutil.copyfile(p, BACKUP / p.name)
for p, text in pending.items():
    p.write_text(text, encoding="utf-8")

# ---------------------------------------------------------------- 自检
import yaml
gfinal = GLOSS.read_text(encoding="utf-8")
fences = [x.start() for x in re.finditer(r"^```", gfinal, re.M)]
block = gfinal[fences[0]:fences[1]].split("```yaml\n", 1)[1]
items = yaml.safe_load(block)
assert isinstance(items, list) and len(items) == 182, f"术语应 182 条，实得 {len(items) if isinstance(items, list) else '解析失败'}"
ids = [x["id"] for x in items]
assert len(set(ids)) == 182, "术语 id 存在重复"
assert ids[-10:] == [f"t{i}" for i in range(173, 183)], "末 10 条 id 不是 t173–t182"
d2 = json.loads(TESTS.read_text(encoding="utf-8"))
assert len(d2["test_cases"]) == 115 and d2["version"] == "v4.10"

print(f"glossary: 172 -> {len(items)} 条，t173–t182 连续、id 唯一、yaml.safe_load 通过")
print(f"test-prompts: 105 -> {len(d2['test_cases'])} 条，version {old_version} -> {d2['version']}")
print(f"备份目录: {BACKUP}")
print("APPEND_V4_10_OK")
