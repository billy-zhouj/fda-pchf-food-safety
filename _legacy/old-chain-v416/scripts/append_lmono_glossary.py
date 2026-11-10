#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 L.mono 指南 XIX Glossary 的 t86–t100 追加进 candidates/glossary.md 的 YAML 代码块。"""
from pathlib import Path

BASE = Path("E:/WeChatData/2026-11-04-09-51-05/books/fda-pchf-human-food-guidance")
GLOSS = BASE / "candidates/glossary.md"

ENTRIES = """- id: t86
  title: listeristatic formulation（抑制型配方）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B（定义与 IX 一致）
  source_quote: |
    "Listeristatic formulation: pH less than or equal to 4.4; water activity less than or equal
    to 0.92; and formulations (including those established in whole or in part through processes
    such as fermentation or culturing) containing a combination of factors scientifically
    demonstrated to be effective in preventing growth."
  summary: 三条路径并列的**抑制型**配方定义。只承诺"阻止生长"，不承诺"杀灭"；与法规 acid foods（平衡 pH≤4.6）**不是同一基准**——4.4 是李斯特菌专用的抑制目标。典型形态为发酵/培养型配方。与 t87 成对阅读。
  tags: [指南自定义, 配方控制, 核心概念, Lmono专有, 高频误读]

- id: t87
  title: listericidal control（致死型控制）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B；定义另见 X.A
  source_quote: |
    "Listericidal control: a control that will consistently destroy viable cells of
    *L. monocytogenes* and consistently leads to a finished food that contains less than 0.04
    colony forming units (CFU) of *L. monocytogenes* per gram (g) of food."
  summary: 定义用**成品可检出性**（<0.04 CFU/g，即 <1 CFU/25 g）而非 log 数表述——是"结果定义"而非"强度定义"，因此必须与所用方法的检出灵敏度绑定阅读。常见误读：把"5 log"当成 listericidal 的定义；实际 5/6 log 是**兜底路径**（按工艺前初始负荷 ≤/>100 CFU/g 切换），且只在无科学研究时使用。
  tags: [指南自定义, 致死工艺, 核心概念, Lmono专有, 高频误读]

- id: t88
  title: adequately reduce（充分减少）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Adequately reduce: capable of reducing the presence of *L. monocytogenes* to an extent
    sufficient to prevent illness."
  summary: 本指南对"减少到什么程度算够"的**结果导向**表述——标准是"足以预防发病"，不是"降了多少 log"。与法定 significantly minimize（t23，"降到可接受水平，包括消除"）不同：本条锚定**发病后果**（prevent illness），更适合判断某个 listericidal 工艺是否够格。三者分工见 t100。
  tags: [指南自定义, 核心概念, Lmono专有, 易混术语]

- id: t89
  title: zone（分区）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Zone means a designation about a surface or area reflecting how near that surface or area
    is to a ready-to-eat food and the risk the surface or area poses to ready-to-eat food if the
    surface or area is contaminated with *L. monocytogenes*."
  summary: 按"**离 RTE 食品有多近**"给表面/区域打的等级标签，是环境监测采样频次与纠正措施严格度的分配依据（四区示例见附录 Table 4）。与既有 t35 hygienic zoning（按生/熟/湿/干做物理分隔）是两回事：zone 是**风险分级标签**，不必然有物理隔离。
  tags: [指南自定义, 环境监测, 卫生分区, Lmono专有]

- id: t90
  title: non-food-contact surface (non-FCS)（非食品接触面）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Non-food-contact surface (non-FCS) any surface that, under normal operating procedures,
    does not contact food or the food-contact surfaces of equipment. Examples … equipment, vents,
    fixtures, drains, walls, floors, and employee clothing, shoes, and accessories."
  summary: 判定式定义——"在**正常操作程序下**不接触食品、也不接触设备的食品接触面"。两个易错点：①判定前提是"正常操作程序"，异常工况（溢流、泄漏、飞溅）可使非 FCS 变成实际接触面；②示例包含员工衣物鞋履与配件——所以它同时是人员控制与手套更换规则的挂钩点。
  tags: [指南自定义, 环境监测, 卫生, Lmono专有]

- id: t91
  title: hold and test procedures（暂扣待检程序）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B；用法见 XIII.F.3 与 XIV.B
  source_quote: |
    "Hold and test procedures: procedures establishing the criteria for releasing product after
    receiving the results of tests conducted to determine the presence of a pathogen on an FCS."
  summary: **先暂扣、后凭检测结果放行**的成文程序。关键点：它不是"检出才隔离"，而是**事先写好放行准则**（什么结果放行、什么结果处置），所以必须在产品流向市场之前就已存在——事后再补就失去意义。与管理组件里的"暂存待 PCQI 评估"不同：hold and test 的放行依据是**检测结果**。
  tags: [指南自定义, 环境监测, 记录, Lmono专有, 高频误读]

- id: t92
  title: environmental sample（环境样品）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Environmental sample: A sample that is collected from a surface or area of the plant for
    the purpose of testing the surface or area for the presence of microorganisms, usually
    environmental pathogens."
  summary: 从厂房**表面或区域**采集、用于检验该表面/区域上微生物（通常是环境病原）的样品。定义里"**区域**"这一项易被忽略——擦拭取样之外还有整块区域取样（如地漏、地沟），二者的前处理与判定不同。环境监测优于产品检测的理由：环境监测能定位污染源，产品检测只能给出历史基准。
  tags: [指南自定义, 环境监测, Lmono专有]

- id: t93
  title: control point (CP)（控制点）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Control point (CP): Any step at which biological, physical, or chemical factors can be
    controlled."
  summary: 可施加控制的步骤——**比 CCP 宽**。与 t11（CCP：控制对预防/消除危害 essential）与 t12（critical limit：安全红线）构成三级：步骤（CP）→ 关键点（CCP）→ 关键限值（CL）。常见误读：把"可控制"直接等同于"关键控制点"——CP 只说明该步骤在技术上可干预，不说明它对特定危害是关键。
  tags: [指南自定义, HACCP, 易混术语]

- id: t94
  title: severity（严重性）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Severity: The seriousness of the effects of a hazard."
  summary: 危害后果的严重程度——是危害分析严重性×概率双维评估的第一维。定义极简，故意不列举等级：FDA 在 Part 117 语境下把等级划分留给评估者与 PCQI，但要求**书面**。可与 t67（SAHCODH：一个可操作化的严重性门槛）配读。与另两种"够不够"判据的分工见 t100。
  tags: [指南自定义, 危害层级]

- id: t95
  title: Listeria species (Listeria spp.)（李斯特菌属）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Listeria species (Listeria spp.): microorganisms within the genus *Listeria*, including
    the species *L. monocytogenes*."
  summary: 属级概念——**包含** L. monocytogenes。用途边界：环境监测与部分成品筛查用 spp. 层级（覆盖面广、便于识别定殖），但成品检测应指向 L. mono 本身；成品检 spp. 阳性时须判定是否 L. mono，否则按 L. mono 污染处理。与 t100 及工艺控制卡的"两套检测方向"配读。
  tags: [指南自定义, 检测, Lmono专有, 高频误读]

- id: t96
  title: food safety system（食品安全体系）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Food Safety System: The result of the implementation of a food safety plan."
  summary: FSP（t08，文档）**落地运行后的结果**——文档与体系是两件事。与 t08 配读可避免"文件齐了=体系有效"的误读（供应链卡 B3 已点名这种"书面体系≠真实安全"的失败模式）。
  tags: [指南自定义, 核心概念, 高频误读]

- id: t97
  title: clean in place (CIP) / clean out of place (COP)（原位清洗 / 拆位清洗）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B
  source_quote: |
    "Clean in place (CIP): The removal of soil from product contact surfaces in their process
    position by circulating, spraying, or flowing chemical solutions and water rinses onto and
    over the surfaces to be cleaned." / "Clean out of place (COP): A system (e.g., cleaning
    tanks) used to clean equipment parts, piping, etc. after disassembly."
  summary: 两种清洗形态的官方定义——CIP 不拆设备就地清洗；COP 拆开后清洗。选型判据不在本术语里而在环境控制逻辑里：能拆的优先 COP（可触达缝隙），不能拆的走 CIP（须验证喷淋覆盖与残留）。共用 CIP 系统另有温度与监控参数要求（见环境病原卡 nA-07）。
  tags: [指南自定义, 卫生, 清洗, Lmono专有]

- id: t98
  title: certificate of analysis (COA) / certificate of conformance (COC)（L.mono 专项精确定义）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B；专项内容要求见 VIII.B.3
  source_quote: |
    "Certificate of Analysis: a document, provided for a food prior to or upon receipt of the
    food, that documents certain characteristics and attributes of the food." / "Certificate of
    Conformance: a supplier's guarantee stating that raw materials and ingredients conform to a
    product safety specification."
  summary: **与 t64 同源但更精确**，两者须配读：t64 给通用定义与"检测不能作唯一手段"的纪律，本条给 L.mono 专项字段——COA 强调"**接收前或接收时**提供"（接收环节的闸门文件），COC 强调"**供应商的保证**"（conform to a product safety specification），两者都不等于"第三方证明"。专项补充：COC 须含保证期 + 产品安全规格 + 符合本指南与 part 117 的声明，并至少每年取得 + 每年现场审核；COA 须含抽样方案、分析结果、方法及**检出限**。
  tags: [指南自定义, 供应链, 记录, Lmono专有, 高频误读]

- id: t99
  title: high efficiency particulate air (HEPA) filter（高效颗粒空气过滤器）
  type: term
  source_chapter: L.mono 指南 XIX Glossary B；使用要求见厂房工程控制卡
  source_quote: |
    "High efficiency particulate air (HEPA) filter: an air filter that has an efficiency of
    99.97 percent to 99.99 percent when tested using the dioctylphthalate (DOP) test with a
    particle size of 0.3 microns. Such filters can remove all yeast, mold, bacteria and other
    particles that are larger than 0.3 microns."
  summary: HEPA 的**判定性规格**——DOP 法、0.3 µm、效率 99.97–99.99%。注意这是"≥0.3 µm 粒径"的去除承诺，对更小的粒径（如气溶胶化的更细颗粒）不作保证；这是"HEPA ≠ 零穿透"的正确读法。空气过滤选型（ASHRAE 终级 vs HEPA）见 `environmental-engineering-controls` 卡。
  tags: [指南自定义, 空气过滤, 术语澄清, 高频误读]

- id: t100
  title: severity vs. adequately reduce vs. significantly minimize（三种"够不够"判据不可混用）
  type: term
  source_chapter: 综合 L.mono 指南 XIX.B 与 21 CFR 117.3（t23）
  source_quote: |
    "Adequately reduce: capable of reducing the presence of *L. monocytogenes* to an extent
    sufficient to prevent illness." / "Significantly minimize: To eliminate or reduce to an
    acceptable level, including to eliminate."
  summary: 三种判据的分工——**severity**（t94，后果有多重，用于危害分析）、**significantly minimize**（t23，法定预防控制目标：降到可接受水平，含消除）、**adequately reduce**（t88，本指南的工艺充分性判据：足以预防发病）。混用的典型后果：把"降到可接受水平"读成"降 5 log"（一个数都不是），或把"足以预防发病"读成"可检出即合格"（忽略 0.04 CFU/g 的方法灵敏度前提）。
  tags: [指南自定义加法定定义, 易混术语, 核心概念, Lmono专有]
"""

text = GLOSS.read_text(encoding="utf-8")

# 1) 在 YAML 代码块结束围栏前插入新条目（t85 之后）
marker = '  tags: [指南自定义, 标签]\n```'
assert text.count(marker) == 1, "YAML 代码块结束定位失败"
text = text.replace(marker, '  tags: [指南自定义, 标签]\n\n' + ENTRIES + '```')

# 2) t64 补交叉引用（保留 t64 原有内容，不删除）
old64 = 'COA 数据须与其他活动配合使用——检测只能是补充，永远不能是唯一手段。'
new64 = ('COA 数据须与其他活动配合使用——检测只能是补充，永远不能是唯一手段。'
         'L.mono 专项的更精确定义与字段要求（接收前/接收时提供、COC 须含保证期与产品安全规格、COA 须含检出限）见 t98。')
assert text.count(old64) == 1, "t64 summary 定位失败"
text = text.replace(old64, new64)

# 3) 自检记录更新
text = text.replace(
    '- [x] 84 条（目标 40–70，按"宁错杀"原则超额收录，多为同一词条的法定/自定义双轨或成对辨析条目）',
    '- [x] 100 条（原始 84 条 + 21 CFR Part 117 增量 1 条 + L.mono 指南 XIX Glossary 增量 15 条；按"宁错杀"原则超额收录，多为同一词条的法定/自定义双轨或成对辨析条目）\n'
    '- [x] 第三来源《Control of Listeria monocytogenes in RTE Foods (Draft, 2017-01)》术语 t86–t100 已并入；'
    't64 与 t98 为同源词条的通用定义/专项精确定义双轨，已互链；'
    'harborage site / lethality treatment / operating limits / prerequisite programs / cleaning-sanitize / '
    'correction / validation / verification / FSP 等已有等价条目，不重复新增 id')

GLOSS.write_text(text, encoding="utf-8")

import re
ids = re.findall(r'^- id: (t\d+)$', text, re.M)
print(f"glossary 写入完成：{len(ids)} 条，id 范围 {ids[0]}–{ids[-1]}")
print(f"重复 id: {[x for x in set(ids) if ids.count(x) > 1] or '无'}")
print(f"字节数: {GLOSS.stat().st_size}")
