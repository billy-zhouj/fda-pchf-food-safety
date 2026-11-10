#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v4.0 增量：追加 SECG/cGMP 测试用例与术语条目。"""
import json
from pathlib import Path

BASE = Path("E:/WeChatData/2026-11-04-09-51-05/books/fda-pchf-human-food-guidance")

# ---------- 1. test-prompts.json ----------
p = BASE / "test-prompts.json"
d = json.loads(p.read_text(encoding="utf-8"))
existing = {c["id"] for c in d["test_cases"]}

cases = [
    {
        "id": "secg-trigger-01",
        "type": "should_trigger",
        "prompt": "cGMP 合规到底有没有官方指南？我们厂要做一次 Subpart B 内审，九条逐条该看什么、证据怎么留？",
        "expected_behavior": "应激活本技能并加载 cgmp-compliance-guide 卡：先给四层效力栈（Part 117 法规正文为唯一判定基准 / FDA 小企业合规指南 SECG 为白话转述不创设义务 / 专项行业指南为草案建议层 / CPG 与 Compliance Programs 为检查视角非企业义务清单）；点名 2016-10 SECG、XIII 章逐条对应 § 117.10/.20/.35/.37/.40/.80/.93/.110、XIV 章对应 § 117.95；用「条款—法规结果义务—现场观察点」三列索引逐条给取证要点；强调 adequate 是〔§ 117.3〕的结果义务、cGMP 是观察型义务（看现场状态/实际运行/必要记录），并说明 SECG 不是可直接签发的逐条内审清单",
        "notes": "正面场景：cGMP 合规资料定位 + 内审索引，验证四层效力栈与九条索引表",
    },
    {
        "id": "secg-trigger-02",
        "type": "should_trigger",
        "prompt": "FDA 那份小企业合规指南里通篇写的是 should，我们是不是可以不做？能不能用别的做法替代？",
        "expected_behavior": "应激活本技能并加载 cgmp-compliance-guide / regulatory-boundaries 卡：引用 SECG I 章效力声明（rule binding and has the full force and effect of law；guidances do not establish legally enforceable responsibilities；should 表示建议而非要求）；指出 SECG 明确允许满足法规的 alternative approach 但举证责任在企业；先分流主体身份（是否受 Subparts C/G 约束），再判断同一句 should 背后是否站着 Part 117 的 must（典型如验证〔§ 117.160(a)〕）；结论须回指具体条款，不得把指南建议改写成法定义务",
        "notes": "正面场景：指南效力分层与替代方案，验证『效力错位』元规则",
    },
    {
        "id": "secg-trigger-03",
        "type": "should_trigger",
        "prompt": "我们是 qualified facility，也已经有 HACCP 计划了，cGMP 是不是就免了？FDA 来检查会看什么？",
        "expected_behavior": "应激活本技能并加载 cgmp-compliance-guide 卡（辅读 regulatory-boundaries）：明确豁免切的是上层 Subparts C/G、不是底层 Subpart B，qualified facility 仍受 cGMP 约束并须履行替代义务，FSP/HACCP 不能抵现场卫生；给出观察型取证三要素（现场状态、实际运行、必要记录）与两条不同执法钩子（cGMP 失守 → FD&C Act § 402(a)(3)/(4) adulterated；不遵守 C–G → § 301(uu) prohibited act）；提示 Subpart B 本身记录负担轻、重记录义务在 FSP 侧",
        "notes": "正面场景：豁免与分层的常见误读，验证『豁免实为减配』",
    },
    {
        "id": "secg-trigger-04",
        "type": "should_trigger",
        "prompt": "有一批原料缺陷超标，掺到合格批次里之后终产品检测是合格的，这样处理算违法吗？",
        "expected_behavior": "应激活本技能并加载 cgmp-compliance-guide / chemical-hazard-controls 卡：引用〔§ 117.110(b)〕掺混稀释禁令原文 regardless of the defect level of the final food，明确终产品检测合格不影响掺假认定；区分『掺混稀释处理超标批次』（禁止）与『经证明有效方法 reconditioning 后复验合格再使用』〔§ 117.80(c)(9)〕（允许）；点名 Food Defect Levels Handbook 为行动水平实例来源，且本包未收其正文，不得编造具体数值",
        "notes": "正面场景：掺混稀释禁令，验证『结果无罪也照样违法』",
    },
    {
        "id": "secg-trigger-05",
        "type": "should_trigger",
        "prompt": "我记得那份 Small Entity Compliance Guide 是 2016 年 11 月发的？还有 80 FR 55907 和 80 FR 56145 是不是两份不同的规则？",
        "expected_behavior": "应激活本技能并加载 cgmp-compliance-guide 卡并纠正两处事实：SECG 首页为 October 2016（Docket FDA-2011-N-0920，依 SBREFA § 212 编制），不是 2016 年 11 月；2018-05 另有一份同名近似 SECG（Docket FDA-2018-D-1378）只讲合规日期延长与澄清，不是操作手册。80 FR 55907 与 80 FR 56145 属同一份 2015-09-17 PCHF 最终规则，前者是 Federal Register 发布通知首页（SECG I 章引用），后者是同一通知中 Part 117 法规条文部分首页（CFR 各条 source note 引用），不得判为两份规则",
        "notes": "正面场景：事实纠错，验证 B8 引用规范与版本口径",
    },
    {
        "id": "secg-trigger-06",
        "type": "should_trigger",
        "prompt": "我们要做 cGMP 迎检，怎么把 § 117.20 的厂房要求和 § 117.40 的设备要求落成检查要点？法规里没写具体数值怎么判？",
        "expected_behavior": "应激活本技能并加载 cgmp-compliance-guide 卡（辅读 environmental-engineering-controls）：用 adequate 的〔§ 117.3〕法定定义解释『法规不给数值只给结果义务』，法规没写数值不是免责理由；§ 117.20 需看冷凝水落点、防碎灯具、分区手段（location/time/partition/air flow/dust control/enclosed systems 任选其一或组合即可，不指定唯一答案）；§ 117.40 需看仪表 accurate and precise 且数量充足、焊缝平滑 bonded、CIP 死角；观察点列是检查视角归纳，不得写成法规新增 must",
        "notes": "正面场景：结果义务的取证方法，验证『法规给手段清单不给唯一答案』",
    },
    {
        "id": "secg-edge-01",
        "type": "edge_case",
        "prompt": "SECG 的 Table 4 写着 qualified facility 合规日期是 2018 年 9 月 17 日，我们现在是不是还没到期限、可以先不合规？",
        "expected_behavior": "应激活本技能并加载 cgmp-compliance-guide 卡，但必须判定该文件时点已过期：Table 4 与 IX.B / X 章的日期（2016-01-01 记录义务、2017-09-18 小企业、2018-09-17 qualified facility 等）是 2016 年编制的过渡安排，到今天全部已生效，不得用作『尚未到合规期限』的依据；当前时限类问题回法规正文与最新 eCFR 文本；同时不得用指南的『年度复审』覆盖或替代 Part 117 Subpart F 的法定记录保存期限",
        "notes": "边界场景：文件本身正确但时点已过期，验证 B2/B5",
    },
    {
        "id": "secg-edge-02",
        "type": "edge_case",
        "prompt": "帮我按中国 GB 14881 出一份可直接签发的食品厂 cGMP 内审检查表，顺便把药品 21 CFR 211 的偏差调查要求也写进去。",
        "expected_behavior": "应明确告知超出本包覆盖，不硬套：本卡与全包只提供 FDA 口径；中国 GB 14881 功能上大致对应 Subpart B 但条款体系与法定口径不同，跨体系直接合规判定需人工判断；药品 cGMP 是 21 CFR Parts 210/211，与人类食品 Part 117 不是同一体系；SECG 不是可直接签发的内审清单，CPG / Compliance Programs / Import Alerts 的检查视角本包未收全文。可给出 FDA 口径的三列索引作为参考，但须标注不可直接用于 GB 14881 或药品体系签发",
        "notes": "边界场景：跨体系与跨行业混用，验证 B3/B6/B9",
    },
    {
        "id": "secg-negative-01",
        "type": "should_not_trigger",
        "prompt": "帮我查一下 2026 年国内食品生产许可证 SC 证的续证材料清单和办理窗口。",
        "expected_behavior": "不应激活本技能：本包覆盖 FDA 21 CFR Part 117 / PCHF / L.mono / SECG 口径，不含中国食品生产许可（SC）行政程序；应直接说明超出覆盖范围",
        "notes": "反例：非 FDA 行政程序，避免把 cGMP 索引硬套到国内许可事项",
    },
]

new = [c for c in cases if c["id"] not in existing]
d["test_cases"].extend(new)
d["version"] = "4.0"
d["notes"] = (d.get("notes", "") +
              " | v4.0 追加 9 条 SECG/cGMP 合规分诊用例（6 正例、2 边界、1 反例），"
              "覆盖四层效力栈、九条索引、替代方案、豁免分层、掺混禁令、事实纠错与跨体系边界；"
              "第四来源为 FDA《Small Entity Compliance Guide》(2016-10)。").strip(" |")
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"test-prompts: {len(d['test_cases'])} cases, version {d['version']}, +{len(new)}")

# ---------- 2. candidates/glossary.md ----------
g = BASE / "candidates/glossary.md"
t = g.read_text(encoding="utf-8")
entries = """
- id: t101
  title: Small Entity Compliance Guide (SECG)
  type: term
  source_chapter: SECG I. Introduction（2016-10, Docket FDA-2011-N-0920）
  source_quote: |
    "We have prepared this Small Entity Compliance Guide in accordance with section 212 of the
    Small Business Regulatory Enforcement Fairness Act (Pub. Law 104-121)." / "The rule is binding
    and has the full force and effect of law."
  summary: FDA 依 SBREFA § 212 为境内外食品设施编写的白话版规则说明，**不是法规、不是认证、不是内审清单**。常见误读：把它当成义务来源（其实它自己声明不创设法律责任）、把它当成 2016-11 发布（首页为 **October 2016**）、把 2018-05 那份只讲合规日期延长的同名近似件当成操作手册。正确用法是拿它逐条建 GAP，再把每条结论回指〔§ 117.xxx〕。SECG XIII 章逐条转述 Subpart B 八条，XIV 章对应 § 117.95。
  tags: [SECG, 效力层级, 合规指南, 高频误读, 2016-10]

- id: t102
  title: adequate（法定结果义务，非「差不多就行」）
  type: term
  source_chapter: 21 CFR 117.3 Definitions
  source_quote: |
    "Adequate means that which is needed to accomplish the intended purpose in keeping with
    good public health practice."
  summary: cGMP 通篇用 adequate / as necessary / suitable / appropriate 而不给数字，其法定含义是**「足以按良好公共卫生实践达成预期目的」**。这是结果义务，解释权不在企业：「法规没写数值」不是免责理由，检查员看现场状态与运行结果。与 t100 的 adequately reduce（李斯特菌工艺充分性判据）不是同一层级——后者是指南自定义，本条是 Part 117 法定定义。
  tags: [法定定义, cGMP, 结果义务, 21CFR117.3]

- id: t103
  title: current thinking / should（FDA 指南的标准免责措辞）
  type: term
  source_chapter: SECG I. Introduction
  source_quote: |
    "This guidance represents the Food and Drug Administration's (FDA or Agency) current thinking
    on this topic. It does not establish any rights for any person and does not bind FDA or the
    public." / "The use of the word should in FDA guidances means that something is suggested or
    recommended, but not required."
  summary: 「represent current thinking + does not bind FDA or the public + should 非必须」是 FDA 指南的标准免责三件套，与 cGMP 里的 **current**（Current Good Manufacturing Practice，指跟上当前可行技术的持续义务）是**两个不同的 current**，不可混淆。效力错位：同一句 recommend 对只受 Subpart B 约束的主体是真建议，对受 PCHF 约束的主体背后可能站着 Part 117 的 must，须先分流主体身份。
  tags: [效力层级, 指南免责, should-vs-must, 易混术语]

- id: t104
  title: alternative approach（指南允许的替代方案）
  type: term
  source_chapter: SECG I. Introduction
  source_quote: |
    "You can use an alternative approach if it satisfies the requirements of the applicable
    statutes and regulations."
  summary: FDA 指南允许的合法出口，但**举证责任在企业**：须证明替代做法同样满足法规的结果义务，而不是「指南没写所以我随便做」。与 § 117.136 的法定出口不是一回事——后者是「不实施预防控制」的条款级通道，本条是「满足同一法规要求的另一种做法」。
  tags: [效力层级, 合规出口, 举证责任, SECG]

- id: t105
  title: 80 FR 55907 vs. 80 FR 56145（同一份规则的两个页码）
  type: term
  source_chapter: SECG I. Introduction + 21 CFR Part 117 各条 source note
  source_quote: |
    "On September 17, 2015, FDA published the final rule ... (PCHF rule) (80 FR 55907)." /
    "[80 FR 56145, Sept. 17, 2015, as amended at 81 FR 3715, Jan. 22, 2016]"
  summary: 二者是 **2015-09-17 同一份 PCHF 最终规则**的两个起始页：55907 是 Federal Register 规则发布通知的首页（SECG I 章引用它），56145 是同一通知中 **Part 117 法规条文部分**的首页（CFR 各条末尾 source note 引用它）。见到两个数字不要判成两份规则，也不要互相「纠错」。SECG 首页同时写明该规则 **2015-11-16 生效**、合规日期分档（现已全部过期）。
  tags: [出处核对, 高频误读, 法规沿革, SECG]

- id: t106
  title: adulterated vs. prohibited act（cGMP 失守与 C–G 不合规是两条执法钩子）
  type: term
  source_chapter: 21 CFR 117.1(a)(1), (b)；FD&C Act § 402(a)(3)/(4)、§ 301(uu)
  source_quote: |
    "Adulterated within the meaning of: (i) Section 402(a)(3) ... the food has been manufactured
    under such conditions that it is unfit for food; or (ii) Section 402(a)(4) ... under insanitary
    conditions whereby it may have become contaminated with filth" / "is a prohibited act under
    section 301(uu) of the Federal Food, Drug, and Cosmetic Act."
  summary: **cGMP 失守 → 食品被认定为 adulterated**（〔§ 117.1(a)(1)〕引 FD&C Act § 402(a)(3)/(4)）；**不遵守 Subparts C–G → 设施运营本身构成 prohibited act**（〔§ 117.1(b)〕引 § 301(uu)）。两者后续都可接警告信、扣押、禁令、进口扣留，但法律定性不同，写不符合项或整改报告时不可混用。本包 regulatory-boundaries 卡称其为「执法钩子」。
  tags: [法定后果, 执法钩子, cGMP, 易混术语]
"""
marker = "\n```\n\n## 自检记录"
assert marker in t, "glossary YAML 围栏定位失败"
t = t.replace(marker, entries + marker, 1)
t = t.replace(
    "- [x] 高频误读类术语",
    "- [x] 第四来源 FDA《Small Entity Compliance Guide》(2016-10) 术语 t101–t106 已并入；SECG 章节号与〔§ 117.xxx〕分列标注，四层效力栈见 cgmp-compliance-guide 卡；allergen cross-contact 已有既有条目，不重复新增 id\n"
    "- [x] 高频误读类术语", 1)
g.write_text(t, encoding="utf-8")
print(f"glossary: {t.count('- id: t')} entries, +6 (t101-t106)")
