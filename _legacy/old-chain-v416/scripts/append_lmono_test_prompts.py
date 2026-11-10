#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 L.mono 第三来源的测试用例追加到 test-prompts.json，并升版到 3.0。"""
import json
from pathlib import Path

BASE = Path("E:/WeChatData/2026-11-04-09-51-05/books/fda-pchf-human-food-guidance")
P = BASE / "test-prompts.json"
d = json.loads(P.read_text(encoding="utf-8"))

NEW = [
    {
        "id": "lmono-trigger-01",
        "type": "should_trigger",
        "prompt": "我们要新建一条冷藏即食色拉产线，车间怎么分区、RTE 区要不要做正压、排水沟和地漏怎么设计才不会把李斯特菌带进来？",
        "expected_behavior": "应激活本技能并加载 environmental-engineering-controls 卡（辅读 environmental-pathogen-sanitation）：物理分区与气流压差设计、排水流向与明沟禁用、地漏位置与可清洁性、冷凝控制〔§ 117.20(b)(4)〕、空气过滤规格；须区分厂房工程设计与建成后的清洁/监测策略",
        "notes": "正面场景：新增第 12 张卡的独立意图（厂房与设备卫生设计）"
    },
    {
        "id": "lmono-trigger-02",
        "type": "should_trigger",
        "prompt": "工人从原料区走到 RTE 包装区，手套什么时候必须换？泡脚器应该怎么选、怎么防止有人绕过去？工服能不能穿回家洗？",
        "expected_behavior": "应激活本技能并加载 personnel-hygiene-controls 卡：手套接触非食品接触面即须更换的规则、按干湿环境选型泡脚器/泡沫消毒器/干粉消毒剂、防绕过设计与失效巡检、工服分区专用与每日洗涤、色码区分、维修与废弃物接触人员的额外要求",
        "notes": "正面场景：新增第 13 张卡的独立意图（人员卫生控制）"
    },
    {
        "id": "lmono-trigger-03",
        "type": "should_trigger",
        "prompt": "我们做冷藏即食甜点，没法加热杀菌，能不能靠调低 pH 或水分活度来控李斯特菌？验证要怎么做，必须自己做挑战试验吗？",
        "expected_behavior": "应激活本技能并加载 process-control-validation 卡：产品开发阶段先做配方/致死路径分流；listeristatic 三条路径（pH≤4.4 / aw≤0.92 / 抑菌物质含发酵培养型）；五类可组合证据路径与'文献即足够'快捷通道〔§ 117.160(b)(2)〕；抑制型有效性判据为货架期重复生长研究两个以上时间间隔增幅 <1 log；须同时做 initial demonstration 与 ongoing verification",
        "notes": "正面场景：抑制型配方验证，覆盖现有卡原有缺口（前置决策 + 证据清单 + <1 log 判据）"
    },
    {
        "id": "lmono-trigger-04",
        "type": "should_trigger",
        "prompt": "环境监测这个月同一个点位第三次检出李斯特菌，前面两次加强清洁都过了，现在要不要停产？复产条件是什么？",
        "expected_behavior": "应激活本技能并加载 environmental-pathogen-sanitation 卡：阳性次数阶梯作为处置强度阶梯（第三次阳性＝假定存在 harborage site → 停产 + 专家介入 + 连续 3 次阴性才复产）；须保留株型指纹一致性作为同点位同型重复的判别器，不得把次数阶梯与指纹判据写成互相否定；指南建议层的数值不得升格为法定义务〔§ 117.165(b)(3) 只要求足以判定有效性〕",
        "notes": "正面场景：阳性升级决策树 + 矛盾 2（指纹判据 vs 次数阶梯）的正确处理"
    },
    {
        "id": "lmono-edge-01",
        "type": "edge_case",
        "prompt": "我们的 RTE 产品做到 pH 4.5，酸化食品法规的 4.6 门槛是不是就满足了？李斯特菌是不是也算控制住了？",
        "expected_behavior": "应激活本技能并加载 process-control-validation 卡并显式给出'两套基准'：pH 4.6 是 Part 117 酸化食品管辖边界（法定/通用口径，且以平衡 pH 为准〔§ 117.3〕、须监测维持〔§ 117.80(c)(14)〕）；pH ≤4.4 才是 L.mono 抑制型配方的指南设计基准（2017 Draft 建议层）。pH 4.5 对前者勉强成立、对后者不成立（L. mono 在 pH 4.5 仍可生长）。不得把两套数值互相替换",
        "notes": "边界（本次最关键误用防线）：kC-01 pH 两套基准 + kC-02 aw 0.92 双含义；答成'一个 pH 值管两件事'即判失败"
    },
    {
        "id": "lmono-edge-02",
        "type": "edge_case",
        "prompt": "我们成品抽检想直接套环境监测那套，检 Listeria spp. 就行了吧？环境样品和成品样品的前处理方法能通用吗？",
        "expected_behavior": "应激活本技能并加载 reference-tools-discipline 卡（辅读 environmental-pathogen-sanitation 与 management-components）：成品应检 L. monocytogenes 而非 Listeria spp.；若检 spp. 阳性须判定是否 L. mono，否则按 L. mono 污染处理；环境监测常规检 spp. 是为指示定殖，两者方向相反、理由不同。方法分工上环境样按该指南附录 5 前处理 + FDA《Testing Methodology for Listeria species or L. monocytogenes in Environmental Samples》，食品样按 FDA BAM 在线版；替代方法须书面、科学有效且在准确性/精密度/检出灵敏度上至少等同",
        "notes": "边界：kC-05 两种检测方向 + nC-34 方法合格性判据；把环境做法照搬到成品检测即判失败"
    },
    {
        "id": "lmono-edge-03",
        "type": "edge_case",
        "prompt": "FDA 那份李斯特菌指南里说每个产线至少采 5 个食品接触面加 5 个非食品接触面点位，我们只做了 3 个，检查会不会直接判不合格？",
        "expected_behavior": "应激活本技能并加载 environmental-pathogen-sanitation 卡并明确效力分层：5+5 点位下限、每周/每月频次与 Zone 划分均出自 2017 年 Draft 指南，正文为 'we recommend'（建议层），本身不设法律责任；must 级判准是〔§ 117.165(b)(3)〕要求书面环境监测程序规定点位数量与位置、时机与频次且'足以判定预防控制是否有效'。不得以建议层数值作为法定合格线，也不得反过来用法规的概括性要求否定该指南的操作价值",
        "notes": "边界：Draft 建议层 vs 法规 must 层（矛盾 5）；把指南数值升格为法定义务即判失败"
    },
    {
        "id": "lmono-edge-04",
        "type": "edge_case",
        "prompt": "我们杀菌工序验证做到了 5 log 削减，成品用灵敏度 10 CFU/g 的方法检不出李斯特菌，能算这个致死工艺验证通过了吗？",
        "expected_behavior": "应激活本技能并加载 process-control-validation 卡：listericidal 的验证目标用成品可检出性表述——须一致地摧毁活菌并使成品不含可检出 L. mono，且所用方法检出灵敏度须至少 0.04 CFU/g（<1 CFU/25 g）。灵敏度 10 CFU/g 的方法不足以支撑该结论；5/6 log 只是无科学研究时的兜底路径，且须按工艺前初始负荷切换（≤100 CFU/g → 5 log；可合理预见 >100 CFU/g → 6 log）。不得把 5 log 当成 listericidal 的定义",
        "notes": "边界：方法灵敏度维度 + 初始负荷自变量（kC-03）；忽略检出限即判失败"
    },
    {
        "id": "lmono-edge-05",
        "type": "edge_case",
        "prompt": "我们的 RTE 产品杀菌后整线都不暴露环境了，是不是还要按李斯特菌专项指南做全套环境监测和产品抽检？",
        "expected_behavior": "应激活本技能并加载 hazard-analysis-method / regulatory-boundaries 卡（辅读 environmental-pathogen-sanitation）：先用三条件核对（RTE + 包装前暴露于环境 + 包装后无致死处理）；处理后不再暴露可书面论证豁免（Soup B/Salsa A 模式）。同时须说明李斯特菌专项指南的适用边界：它聚焦'包装前暴露且包装后无致死处理或致死型配方控制'的场景，明确不适用于在最终包装内或紧邻包装前施加致死措施且系统能充分屏蔽 FCS 不受环境污染的加工者，也不适用于不受 Part 117 约束的场所（如农场）",
        "notes": "边界：nC-01 指南适用分流 + 包装后致死处理的两种边界情形；直接套用全套监测即判失败"
    },
    {
        "id": "lmono-edge-06",
        "type": "edge_case",
        "prompt": "我们把成品冷藏库设成 4°C，可冷却协议写的是降到 41°F（5°C）就行，同一份食品安全计划里两个冷藏数字是不是写错了？",
        "expected_behavior": "应激活本技能并加载 process-control-validation 卡并说明用途不同：4°C（约 40°F）是李斯特菌专项指南针对 RTE 储存的**建议缺省值**（更严，且更高温度须符合 PMO 或 Food Code）；41°F/5°C 是危险区下限与冷却终点（法规/Food Code 口径，对应 135→70°F ≤2h、70→41°F ≤4h 两段式冷却）。两者不冲突，但须在同一份 FSP 中各自标明用途；并须提示冷冻只能防生长、不能作为消除或减少李斯特菌的控制措施",
        "notes": "边界：kC-04 冷藏温度两套基准；删掉其中一个数字或混用即判失败"
    },
    {
        "id": "lmono-trigger-05",
        "type": "should_trigger",
        "prompt": "槽车拉原料、冷藏车配送成品，装车前要不要预冷并记录温度？洗车标签能不能当清洁消毒的证明？",
        "expected_behavior": "应激活本技能并加载 supply-chain-verification 卡：卸原料时与装成品前检查车辆结构完整性/清洁度/适用性；产品须在装车前已达目标温度（冷藏车只维持温度、不负责冷却）；车辆须预冷并**记录装车前温度**；槽车或重复使用的散装容器应专用化，否则须建立防前载货物污染程序并核实清洁消毒（可用有验证清洗程序的洗车厂出具的 wash tag 佐证）",
        "notes": "正面场景：nC-28 运输环节可执行要求，补现有供应链卡'储运条件'只有一词的缺口"
    },
    {
        "id": "lmono-trigger-06",
        "type": "should_trigger",
        "prompt": "我们要给冷藏即食食品写环境监测程序，采样点位数、时机、频次和阳性后的升级路径具体怎么定？清洁消毒程序里必须写哪些字段？",
        "expected_behavior": "应激活本技能并加载 environmental-pathogen-sanitation 卡（辅读 management-components）：书面程序七项内容；点位数量下限 5 FCS + 5 non-FCS/产线、周期内测完全部点位；采样时机为生产开始后 3–4 小时或清洁前（过早采样会因消毒剂未中和干扰检测）；两套可照抄的频次方案；合样上限 5 个且定位污染源时禁止合样；书面卫生程序八项要素（清洁剂类型及浓度、工具颜色编码、清洗液时间/温度、流速或压力等）；七步湿式清洁序列与'RTE 暴露房间内不得湿洗（覆盖也不行）'",
        "notes": "正面场景：书面程序字段清单与监测设计参数，验证 B4 缺口被部分关闭"
    },
]

existing = {c["id"] for c in d["test_cases"]}
dup = [c["id"] for c in NEW if c["id"] in existing]
assert not dup, f"重复用例 id: {dup}"

d["test_cases"].extend(NEW)
d["version"] = "3.0"
d["source_book"] = (
    "Hazard Analysis and Risk-Based Preventive Controls for Human Food: Guidance for Industry (Draft) "
    "+ 21 CFR Part 117 (2025) 法规正文 "
    "+ Control of Listeria monocytogenes in Ready-To-Eat Foods: Guidance for Industry (Draft, 2017-01)"
)
d["notes"] = (
    "single 模式：所有能力卡经唯一入口路由，'兄弟混淆'体现在能力卡路由层（edge 用例验证卡选择）。"
    "should_not_trigger 容错为 0。本套件可直接接入 darwin-skill 自动进化。"
    "v2.0 新增 7 条法规层用例（cfr-*）。v2.1 术语统一：全库'过程控制'→'工艺控制'，"
    "glossary 新增 t27 process control（工艺控制）中英对照锚点；新增 term-rename-01 验证中英双语触发。"
    "v3.0 并入第三来源 FDA《Control of Listeria monocytogenes in RTE Foods》(2017-01 Draft)："
    "能力卡 11→13 张（新增 environmental-engineering-controls 厂房与设备工程控制、"
    "personnel-hygiene-controls 人员卫生控制），glossary 85→100 条；"
    "新增 12 条 lmono-* 用例，覆盖两张新卡独立触发、抑制型配方验证、阳性升级决策树、"
    "以及五条关键边界——pH 4.6/4.4 两套基准、成品检测与环境监测方向相反、"
    "Draft 建议层 vs 法规 must 层、0.04 CFU/g 方法灵敏度、4°C/5°C 冷藏双基准。"
    "盲测尚未运行——可用 run_trigger_evals.py prepare + score 在安装后补跑。"
)

P.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

from collections import Counter
print(f"test-prompts.json 升版 {d['version']}：{len(d['test_cases'])} 条")
print("类型分布:", dict(Counter(c["type"] for c in d["test_cases"])))
print("重复 id:", [k for k, v in Counter(c["id"] for c in d["test_cases"]).items() if v > 1] or "无")
