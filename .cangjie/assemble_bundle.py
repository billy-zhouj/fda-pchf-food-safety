#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""assemble_bundle.py — 从 26 张 _meta-*.yaml 汇总构造 Capability Bundle（verified.yaml + destinations.json + book/）"""
import yaml, json, shutil
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]  # v4.10：改为脚本相对推导，原硬编码原开发机路径在本机不可用
CAPS_DIR = BASE / ".cangjie/capabilities"
CARDS = CAPS_DIR / "cards"

SLUGS = ["hazard-analysis-method", "management-components", "process-control-validation",
         "environmental-pathogen-sanitation", "allergen-program", "chemical-hazard-controls",
         "supply-chain-verification", "recall-plan", "regulatory-boundaries", "reference-tools-discipline",
         "exemption-withdrawal-procedure", "environmental-engineering-controls", "personnel-hygiene-controls",
         "cgmp-compliance-guide", "defect-action-levels", "inspection-readiness",
         "inspection-sampling", "investigator-authority-procedure", "lacf-inspection-program",
         "lacf-statutory-requirements", "fsvp-inspection-program",
         "seafood-haccp-statutory-requirements",
         "seafood-hazards-controls-guide",
         "seafood-inspection-program",
         "emergency-permit-control",
         "juice-haccp"]

ALSO_READ = {
    "hazard-analysis-method": ["management-components", "process-control-validation", "reference-tools-discipline"],
    "management-components": ["hazard-analysis-method", "process-control-validation", "supply-chain-verification"],
    "process-control-validation": ["management-components", "hazard-analysis-method", "environmental-pathogen-sanitation", "cgmp-compliance-guide", "lacf-inspection-program", "lacf-statutory-requirements"],
    "environmental-pathogen-sanitation": ["process-control-validation", "allergen-program", "environmental-engineering-controls", "personnel-hygiene-controls", "inspection-readiness", "inspection-sampling"],
    "allergen-program": ["environmental-pathogen-sanitation", "supply-chain-verification", "hazard-analysis-method"],
    "chemical-hazard-controls": ["supply-chain-verification", "hazard-analysis-method", "cgmp-compliance-guide", "defect-action-levels"],
    "supply-chain-verification": ["chemical-hazard-controls", "allergen-program", "recall-plan", "defect-action-levels", "inspection-readiness"],
    "recall-plan": ["supply-chain-verification", "chemical-hazard-controls", "management-components", "inspection-readiness"],
    "regulatory-boundaries": ["reference-tools-discipline", "hazard-analysis-method", "exemption-withdrawal-procedure", "cgmp-compliance-guide", "defect-action-levels", "inspection-readiness", "investigator-authority-procedure", "lacf-inspection-program", "lacf-statutory-requirements"],
    "reference-tools-discipline": ["hazard-analysis-method", "regulatory-boundaries", "process-control-validation", "cgmp-compliance-guide", "defect-action-levels", "inspection-readiness", "investigator-authority-procedure"],
    "exemption-withdrawal-procedure": ["regulatory-boundaries", "management-components"],
    "environmental-engineering-controls": ["environmental-pathogen-sanitation", "personnel-hygiene-controls", "process-control-validation", "cgmp-compliance-guide"],
    "personnel-hygiene-controls": ["environmental-pathogen-sanitation", "environmental-engineering-controls", "allergen-program", "cgmp-compliance-guide"],
    "cgmp-compliance-guide": ["regulatory-boundaries", "environmental-engineering-controls", "reference-tools-discipline", "process-control-validation", "defect-action-levels", "inspection-readiness", "investigator-authority-procedure", "lacf-inspection-program", "lacf-statutory-requirements"],
    "defect-action-levels": ["cgmp-compliance-guide", "chemical-hazard-controls", "supply-chain-verification", "hazard-analysis-method", "regulatory-boundaries", "inspection-readiness", "inspection-sampling", "lacf-inspection-program", "lacf-statutory-requirements"],
    "inspection-readiness": ["cgmp-compliance-guide", "defect-action-levels", "regulatory-boundaries", "environmental-pathogen-sanitation", "supply-chain-verification", "recall-plan", "inspection-sampling", "investigator-authority-procedure", "lacf-inspection-program"],
    "inspection-sampling": ["inspection-readiness", "investigator-authority-procedure", "environmental-pathogen-sanitation", "defect-action-levels", "chemical-hazard-controls", "management-components", "lacf-inspection-program"],
    "investigator-authority-procedure": ["inspection-readiness", "inspection-sampling", "regulatory-boundaries", "cgmp-compliance-guide", "reference-tools-discipline", "defect-action-levels", "lacf-inspection-program"],
    "lacf-inspection-program": ["regulatory-boundaries", "inspection-readiness", "inspection-sampling", "investigator-authority-procedure", "process-control-validation", "cgmp-compliance-guide", "defect-action-levels", "lacf-statutory-requirements"],
    "lacf-statutory-requirements": ["lacf-inspection-program", "regulatory-boundaries", "cgmp-compliance-guide", "defect-action-levels", "process-control-validation", "hazard-analysis-method"],
}

ALSO_READ["seafood-haccp-statutory-requirements"] = [
    "lacf-statutory-requirements", "fsvp-inspection-program", "regulatory-boundaries",
    "hazard-analysis-method", "chemical-hazard-controls", "supply-chain-verification",
    "cgmp-compliance-guide", "inspection-readiness", "inspection-sampling",
]

ALSO_READ["fsvp-inspection-program"] = [
    "supply-chain-verification", "regulatory-boundaries", "inspection-readiness",
    "inspection-sampling", "investigator-authority-procedure",
    "lacf-inspection-program", "cgmp-compliance-guide",
]
for _s in ("supply-chain-verification", "regulatory-boundaries", "inspection-readiness",
           "investigator-authority-procedure", "lacf-inspection-program",
           "cgmp-compliance-guide"):
    if "fsvp-inspection-program" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("fsvp-inspection-program")

# v4.9：Part 123 反向链。生食贝类/熏制水产品与 LACF 交界最紧，故 lacf 系与
# regulatory-boundaries / hazard-analysis-method / chemical-hazard-controls
# 都补反向引用；inspection-readiness 与 inspection-sampling 亦需可跳转。
for _s in ("lacf-statutory-requirements", "fsvp-inspection-program",
           "regulatory-boundaries", "hazard-analysis-method",
           "chemical-hazard-controls", "supply-chain-verification",
           "cgmp-compliance-guide", "inspection-readiness",
           "inspection-sampling"):
    if "seafood-haccp-statutory-requirements" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("seafood-haccp-statutory-requirements")


# v4.10：CAP-23 海产品危害分析判定链。与 CAP-22（Part 123 法条层）配对，
# 还须可跳转到危害分析、化学危害、工艺控制、过敏原、监管边界、取样等卡。
ALSO_READ["seafood-hazards-controls-guide"] = [
    "seafood-haccp-statutory-requirements", "hazard-analysis-method",
    "chemical-hazard-controls", "process-control-validation",
    "allergen-program", "regulatory-boundaries", "inspection-sampling",
    "cgmp-compliance-guide", "reference-tools-discipline",
]
for _s in ("seafood-haccp-statutory-requirements", "hazard-analysis-method",
           "chemical-hazard-controls", "process-control-validation",
           "allergen-program", "regulatory-boundaries", "inspection-sampling",
           "reference-tools-discipline"):
    if "seafood-hazards-controls-guide" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("seafood-hazards-controls-guide")

# v4.11：CAP-24 海产品检查程序层。与 CAP-22（法条层）、CAP-23（指南层）三层配对，
# 另须双向连到通用取样、FSVP、LACF、迎检、检查员权限、化学危害与缺陷行动水平。
ALSO_READ["seafood-inspection-program"] = [
    "seafood-haccp-statutory-requirements", "seafood-hazards-controls-guide",
    "inspection-sampling", "fsvp-inspection-program", "lacf-inspection-program",
    "inspection-readiness", "investigator-authority-procedure",
    "chemical-hazard-controls", "defect-action-levels",
]
for _s in ("seafood-haccp-statutory-requirements", "seafood-hazards-controls-guide",
           "inspection-sampling", "fsvp-inspection-program", "lacf-inspection-program",
           "inspection-readiness", "investigator-authority-procedure",
           "chemical-hazard-controls", "defect-action-levels"):
    if "seafood-inspection-program" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("seafood-inspection-program")

# v4.12：CAP-25 紧急许可控制（21 CFR Part 108）。与 CAP-20（Part 113/114 实体层）、
# CAP-19（CP 7303.070 检查员侧）构成 LACF/AF 的三层分工；另须连到监管边界、迎检、
# 取样、工艺验证、召回与 cGMP，以及海产品法条层（生食贝类与 LACF 交界）。
ALSO_READ["emergency-permit-control"] = [
    "lacf-statutory-requirements", "lacf-inspection-program",
    "regulatory-boundaries", "inspection-readiness", "inspection-sampling",
    "process-control-validation", "recall-plan", "cgmp-compliance-guide",
    "seafood-haccp-statutory-requirements",
]
for _s in ("lacf-statutory-requirements", "lacf-inspection-program",
           "regulatory-boundaries", "inspection-readiness", "inspection-sampling",
           "process-control-validation", "recall-plan", "cgmp-compliance-guide",
           "seafood-haccp-statutory-requirements", "hazard-analysis-method",
           "defect-action-levels"):
    if "emergency-permit-control" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("emergency-permit-control")


# v4.13：CAP-26 果汁 HACCP（21 CFR Part 120）。与 CAP-15（cGMP 底座）、CAP-20（Part 113/114）、
# CAP-22（Part 123 海产品 HACCP，同为 HACCP 体系但另立编号）、CAP-25（Part 108 手续层）交叉；
# 危害分析方法与验证、纠正措施、记录、过敏原、供应链、召回亦须可达。
ALSO_READ["juice-haccp"] = [
    "hazard-analysis-method", "process-control-validation", "cgmp-compliance-guide",
    "lacf-statutory-requirements", "seafood-haccp-statutory-requirements",
    "emergency-permit-control", "allergen-program", "recall-plan",
    "supply-chain-verification", "regulatory-boundaries", "inspection-readiness",
]
for _s in ("hazard-analysis-method", "process-control-validation", "cgmp-compliance-guide",
           "lacf-statutory-requirements", "seafood-haccp-statutory-requirements",
           "emergency-permit-control", "allergen-program", "recall-plan",
           "supply-chain-verification", "regulatory-boundaries", "inspection-readiness",
           "chemical-hazard-controls", "defect-action-levels"):
    if "juice-haccp" not in ALSO_READ[_s]:
        ALSO_READ[_s].append("juice-haccp")


ROUTER_GATE = {"independent_intent": False, "independent_contract": True, "independent_run": True,
               "independent_reuse": False, "independent_eval": True}

capabilities = []
for i, slug in enumerate(SLUGS, 1):
    meta = yaml.safe_load((CARDS / f"_meta-{slug}.yaml").read_text(encoding="utf-8"))
    units = meta.get("member_units", [])
    unit_txt = f"成员单元 {len(units)} 个" if units else "来源定位见卡片 R 段"
    src_label = meta.get("source_label", "FDA PCHF 指南")
    desc = f"{meta['title']}——{meta['one_liner']}（来源：{src_label}；{unit_txt}）"
    capabilities.append({
        "capability_id": f"CAP-{i:02d}",
        "revision": 1,
        "status": "active",
        "aliases": [],
        "supersedes": [],
        "merged_into": None,
        "split_into": [],
        "slug": slug,
        "title": meta["title"],
        "importance": meta["importance"],
        "importance_rationale": meta["importance_rationale"],
        "one_liner": meta["one_liner"],
        "intents": meta["intents"],
        "keywords": meta["keywords"],
        "also_read": ALSO_READ[slug],
        "card": f"cards/{slug}.md",
        "frontmatter": {"description": desc, "tags": meta["keywords"][:6]},
        "source_evidence": [{"source_id": "src-main-book", "location": f"member_units={','.join(units)[:180]}" if units else src_label}],
        "promotion": {
            "destination": "router",
            "gate": dict(ROUTER_GATE),
            "notes": "输出模式为 single（用户确认）：全部能力经唯一入口路由，不设独立可发现入口；五判据评审记录见卡片 A2/E 段与 PIPELINE_STATE.md",
        },
    })

bundle = {
    "schema_version": 1,
    "bundle_id": "bundle.fda-pchf-human-food",
    "book": {
        "title": "Hazard Analysis and Risk-Based Preventive Controls for Human Food: Guidance for Industry (Draft)",
        "author": "U.S. FDA, CFSAN Office of Food Safety",
        "year": "2024（滚动草案；引用数据截至 2016–2022）",
        "content_type": "regulatory-guidance",
        "source_id": "src-main-book",
        "source_file": "books/fda-pchf-human-food-guidance/source.md",
        "additional_sources": [
            {
                "title": "21 CFR Part 117（2025 版）法规正文",
                "author": "U.S. FDA（eCFR 现行文本）",
                "year": "2025",
                "content_type": "regulation（最终规则，具法律约束力）",
                "source_id": "src-21-cfr-part-117-2025",
                "source_file": "books/_inbox/21-CFR-Part-117-2025.md",
                "note": "Subparts A–G 全量条文（160,825 字节 / 3,577 行），用于提供法定义务、法定例外与时限的权威出处；卡内以〔§ 117.xxx〕标注。⚠ 该文件此前只在 metadata 里声明、**未随仓库分发**（v1–v4.13），致全包〔§ 117.xxx〕引文无法在本仓库内复核；v4.14 已入库并经 `.cangjie/verify_v4_14_part117_quotes.py` 追溯核验 23/23 命中。其中〔§ 117.5(c)〕是 Part 120 的豁免出口：**双条件（required to comply with 且 in compliance with）+ 无限缩款**，与 (d)(2) 的『仅限微生物危害』不同；§117.5(b)（part 123）同样无限缩款。",
            },
            {
                "title": "Control of Listeria monocytogenes in Ready-To-Eat Foods: Guidance for Industry (Draft)",
                "author": "U.S. FDA, CFSAN",
                "year": "2017-01（Draft – Not for Implementation）",
                "content_type": "regulatory-guidance（草案，建议层；正文一律 we recommend）",
                "source_id": "src-fda-lmono-rte-2017-draft",
                "source_file": "books/fda-pchf-human-food-guidance/source-lmono.md",
                "note": "21 章 + 5 附录，用于补齐 RTE 即食食品李斯特菌专项的卫生程序、环境监测、厂房工程、人员卫生、抑制型/致死型配方、储运与术语；正文出现 must 处均为其引述 Part 117 的法定义务",
            },
            {
                "title": "What You Need to Know About the FDA Regulation: 21 CFR Part 117 — Small Entity Compliance Guide (Guidance for Industry)",
                "author": "U.S. FDA, CFSAN（Office of Food Safety / Office of Analytics and Outreach）",
                "year": "2016-10（依 SBREFA § 212 编制；Docket FDA-2011-N-0920）",
                "content_type": "regulatory-guidance（合规指南，非约束性，代表 FDA current thinking；明确允许满足法规的替代方案）",
                "source_id": "src-fda-secc-part117-2016",
                "source_file": "books/fda-pchf-human-food-guidance/source-secg.md",
                "note": "15 章，由 WorkBuddy 资料库文档转换而来；XIII 章逐条白话转述 Subpart B 的 § 117.10/.20/.35/.37/.40/.80/.93/.110，XIV 章对应 § 117.95；I 章为效力声明（rule binding / guidance not enforceable / should 非必须）；VI 章 Table 4 的合规日期为 2016 年过渡安排，现已全部生效，不得用作当前时限依据",
            },
            {
                "title": "Questions and Answers Regarding Food Allergens, Including the Food Allergen Labeling Requirements of the FD&C Act (Edition 5): Guidance for Industry",
                "author": "U.S. FDA, Human Foods Program",
                "year": "2025-01（Edition 5 修订终版；Docket FDA-2022-D-0099；90 FR 1133）",
                "content_type": "regulatory-guidance（标签解释，非约束性；Contains Nonbinding Recommendations）",
                "source_id": "src-fda-allergen-qa-ed5-2025",
                "source_file": "books/fda-pchf-human-food-guidance/source-allergen-ed5.md",
                "note": "27 页 / 68 书签，由用户提供的官方 PDF 经 pdf2md-pro 转换；解释 FD&C Act 201(qq)/403(w) 的标签义务，不是 21 CFR Part 117 的预防控制义务。合并替代 2022-11-30 发布的 Ed.5 草案与终版两份文件；仅 Table 1 所列 12 种树坚果按主要食物过敏原处理；milk/eggs 扩展至其他反刍动物/禽类",
            },
            {
                "title": "Food Defect Levels Handbook（Levels of natural or unavoidable defects in foods that present no health hazards for humans）",
                "author": "U.S. FDA, CFSAN（网页版）",
                "year": "页面标注 Content current as of 09/07/2018；正文 May 1995，修订 1997-03 / 1998-05，2005-02 两处方法来源更正",
                "content_type": "enforcement-reference（FDA 汇编的 defect action levels 一览与术语表；执法裁量参考，非法规、非 guidance 建议层）",
                "source_id": "src-fda-defect-levels-handbook",
                "source_file": "books/fda-pchf-human-food-guidance/source-defect-levels-handbook.md",
                "note": "由用户提供的官方页面 MHTML 存档转出；6 章 + GLOSSARY 27 词条 + COMMODITIES 表（111 个产品 / 173 条行动水平 / 111 条 DEFECT SOURCE-SIGNIFICANCE）+ 拆出的树坚果容许百分比表。法定对应条款为〔§ 117.110〕（Subpart B）、〔§ 117.3〕定义、〔§ 117.80(b)(3)(4)〕与 FD&C Act 402(a)(3)/(4)。⚠ v4.7 纠错：网页 INTRODUCTION 首句仍写 21 CFR 110.110，2015 规则拟于 2018-09-17 删除 part 110 的 amendatory instruction 13 已被 FDA 2018-09-12 最终规则（FR Doc. 2018-19855）撤回，Part 110 至今有效；它只是正文本包未收，须标「转引未收」，不得判为过时引用。Part 117 侧对应条款仍是〔§ 117.110〕，且 §110.110(c) 不得标成〔§ 117.110(c)〕；action level 是 FDA 执法裁量线，不是合规安全港、不是平均值、不是内控目标",
            },
            {
                "title": "Compliance Program Guidance Manual 7303.040 — Preventive Controls and Sanitary Human Food Operations",
                "author": "U.S. FDA, Human Foods Program (HFP) / Office of Inspections and Investigations (OII)",
                "year": "现行版 2025-CPM-HFP-001，Date of Issuance 08/29/2025，IMPLEMENTATION DATE 05/23/2024；50 页 / 91 书签（取代 2020-CPGM-CFSAN-003，10/15/2020，47 页）",
                "content_type": "inspection-program（FDA 给检查员/分部的内部作业指导；非法规、非 Guidance for Industry、不创设企业义务）",
                "source_id": "src-fda-cpgm-7303-040-2025",
                "source_file": "books/fda-pchf-human-food-guidance/source-cpgm-7303-040-2025.md",
                "note": "由用户提供的官方 508-Compliant PDF 经 pdf2md-pro 转换；已废止的历史对照见 books/fda-pchf-human-food-guidance/source-cpgm-7303-040-2020.md。8 个 FDA PAC（03040 / 03040A / 03040L / 03040F / 03040Q / 03040R / 03040T / 03040U）+ 8 个州合同码；PART III 检查类型与取证、PART V 观察项/检查分级与 OAI-VAI-NAI 执法阶梯、ATTACHMENT A 卫生运输（属 21 CFR 1 Subpart O，非 Part 117）。⚠ 现行版把 critical/major/minor 挂在『整次检查』，单条观察项在 eNSpect 只有 major/minor 且 investigators do not make this categorization；03040U 已从 PCHF Follow-Up 改为 Focused PCHF；483 回复期望 15 个工作日并设境外专用邮箱。合规结论仍回〔§ 117.xxx〕；引用用「CPGM 7303.040 PART x」。⚠ FDA 网页列表日期与 PDF 首页 IMPLEMENTATION DATE 不一致，以 PDF 首页为准",
            },
            {
                "title": "Compliance Program Guidance Manual 7303.050 — Sampling for Foodborne Biological Hazards and Filth (Domestic and Import)",
                "author": "U.S. FDA, Human Foods Program / Office of Compliance and Enforcement (HFP/OCE)",
                "year": "Date of Issuance 06/03/2022；IMPLEMENTATION DATE 06/03/2022；Correction date 09/10/2025；62 页 / 75 书签",
                "content_type": "sampling-program（FDA 给检查员/分部/实验室的内部抽样作业指导；非法规、非 Guidance for Industry、不创设企业义务）",
                "source_id": "src-fda-cp-7303-050-2025",
                "source_file": "books/fda-pchf-human-food-guidance/source-cp-7303-050-2025.md",
                "note": "由用户提供的官方 508-Compliant PDF 经 pdf2md-pro 转换。⚠ 文件名 20250915 与 Correction date 09/10/2025 表示 2022 版程序的 2025 年更正本，不是 2025 年新签发的 program，不得套用 7303.040 的 2025-CPM-HFP-001 Transmittal 格式。PART III.1.A 明说 Inspections are not planned under this compliance program；PART III.1.C / Table 2、3 给产品样品 subs 数（不含 702(b) 部分）；ATTACHMENT A 给环境拭子 Listeria ≥50（理想 100）/ Salmonella ≥100（理想 300）与 Zone 1–3 / 2–3、WGS + GenomeTrakr、三档 Findings；ATTACHMENT B 给污秽/霉变抽样；PART V 表 7/8 是逐案、非穷尽的可能 FDA 响应清单，指控为 402(a)(1)/(3)/(4)、801(a)(3)。引用用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」。IOM Chapter 4、eBAM / BAM / AOAC / MPM 方法正文、SOP-001052、SOP-000529 FMD-147、CPG Sec. 527.300、RPM Ch.9 与 Import Alert 正文仍未收",
            },
            {
                "title": "Investigations Operations Manual (IOM) 2026 — Chapter 5: Inspections",
                "author": "U.S. FDA, Office of Inspections and Investigations (OII)",
                "year": "2026 版 Chapter 5（PDF creationDate 2026-07-13）；221 页 / 410 书签",
                "content_type": "investigator-manual（FDA 给调查员的内部作业手册；非法规、非 Guidance for Industry、不创设企业义务）",
                "source_id": "src-fda-iom-2026-ch5",
                "source_file": "books/fda-pchf-human-food-guidance/source-iom-ch5-2026.md",
                "note": "由用户提供的官方 PDF 经 pdf2md-pro 转换。仅 Chapter 5 单章，含 5.1–5.16 与 Exhibit 5-1…5-23；IOM Ch.3/4/6/7/8/9/10 未收。法定基础 FD&C Act 704(a)(1)；国内到场出示 credentials + 签 FDA 482，境外一般不发 482；5.2.7 预告三层口径（医疗器械与部分 BIMO 强制、食品企业一般不预告由 program division 裁量、境外通常提前告知、国内不少于 5 个日历日且改期不晚于原日期 +5 天、预告不是预约）；5.5.10 / 5.5.11.3 的 483 措辞纪律——不引法规原文、不纳入标准、不引 policy/guidance 偏离、不写 opinions/violative，仅偏离 guidance 属 Category 3 non-reportable observation；5.5.12.3 与 5.5.12.5 给 15 个工作日与 Form FDA 484；5.6 给记录/电子记录/照片的证据固定规则；5.5.2 给 301(e)/(f) 与境外 807(b)。引用用「IOM 5.x.x / IOM Exhibit 5-x」",
            },
            {
                "title": "Compliance Program Guidance Manual 7303.070 — Acidified and Low-Acid Canned Foods Program (Import & Domestic)",
                "author": "U.S. FDA, Human Foods Program (HFP) / Office of Inspections and Investigations (OII)",
                "year": "Date of Issuance 09/26/2024；IMPLEMENTATION DATE 9/26/2024；Correction Date 9/26/2025；61 页 / 40 书签",
                "content_type": "inspection-program（FDA 给检查员、实验室分析员与合规官的内部作业指导；非法规、非 Guidance for Industry、不创设企业义务）",
                "source_id": "src-fda-cp-7303-070-2024",
                "source_file": "books/fda-pchf-human-food-guidance/source-cp-7303-070-2024.md",
                "note": "由用户提供的官方 508-Compliant PDF 经 pdf2md-pro 转换。⚠ 文件名 20250929 是 PDF 生成日；本件为 2024-09-26 版程序的 2025-09-26 更正本，不是 2025 年新签发 program，与 CP 7303.050（2022 签发 / 2025-09-10 更正）同属更正本形态，也不同于 CPGM 7303.040 的 2025-CPM-HFP-001 新 Transmittal。PART II.2.C(1) 官方写明 LACF 受 Part 117 约束、但 subparts C/G 不适用于 part 113 覆盖活动，且〔§ 117.5(d)(2)〕该豁免仅限 part 113 管辖的微生物危害；未被热处理控制且需预防控制的危害（金葡生长产毒、化学、物理）仍归 C/G；酸化食品 Acidified foods are subject to the CGMP & PCHF rule，PCHF 覆盖转 7303.040，检查重点仍在 part 108/114。PART II.2.C(2) Products labeled Keep Refrigerated are exempt from 21 CFR 113/114 → 转 7303.050；brites 中央仓报 PAC 03040；PART II.2.B(2) 明确 RRAs are not considered inspections、不满足 704(a)(1) 法定检查场景。PART III.1.A 给酸化判定三步（Maximum Equilibrium pH）、AF/LACF/Aseptic LACF 三类检查目标；PART IV.2 给 795 g/24 罐与 12 罐、pH 4.40/4.65 双分析师触发与 Never average the two analysts' results together、异常罐 4.75 与肉毒毒素/PCR；PART V.2 给 Import Alert 99-37/99-38 与「不得仅因未注册未备案建议 DWPE」。引用用「CP 7303.070 PART x / ATTACHMENT x」。⚠ v4.7 起 21 CFR part 113 / 114 法规正文已收（第十一/十二来源，CAP-20）；仍未收的是 part 108（FCE/SID/Emergency Permit/§108.35）、part 110 / 120（part 123 自 v4.9 起已收，见 CAP-22）、IOM Ch.4 Sample Schedule Chart 2、BAM Ch.13B/14/17/21A/22A-22D、CPG Sec. 520.200/520.300、Import Alert 全文、SOP-001642、RPM Ch.4/9，不得从本 CP 反推未收法条",
            },
            {
                "title": "21 CFR Part 113 — Thermally Processed Low-Acid Foods Packaged in Hermetically Sealed Containers (4-1-25 Edition)",
                "author": "U.S. Government Publishing Office / eCFR, 21 CFR Ch. I (4-1-25 Edition)",
                "year": "4–1–25 Edition（CFR 年度编纂版次，修订至 2025-04-01；书页 344–379，36 页 / 10 条款）",
                "content_type": "regulation（联邦法规正文，最终规则，具法律约束力；本包首次纳入 Part 117 之外的法规正文）",
                "source_id": "src-fda-cfr-part113-2025",
                "source_file": "books/fda-pchf-human-food-guidance/source-cfr-part113-2025.md",
                "note": "由用户提供的 GPO/eCFR 双栏印刷版 PDF 经本包专用脚本 .cangjie/convert_cfr_part.py 按「页 → 左栏 → 右栏」重排转出（pdf2md-pro 会串栏）。§113.3(n) 给 4.6 / 0.85 法定低酸食品定义与番茄 pH <4.7 例外；§113.5 列八个判据条款；§113.10 BPCS 人员；§113.40 设备与 NIST 溯源校准；§113.60 容器；§113.81 产品制备；§113.83 scheduled process 与 critical factors；§113.87 杀菌室规程、product traffic control 与 FDA 调阅权；§113.89 偏差；§113.100 记录（(g) 厂内 ≥1 年 + 另 2 年，(h) 电子记录须符合 part 11）。引用用〔§ 113.xxx〕，独立于〔§ 117.xxx〕〔§ 114.xxx〕。",
            },
            {
                "title": "21 CFR Part 114 — Acidified Foods (4-1-25 Edition)",
                "author": "U.S. Government Publishing Office / eCFR, 21 CFR Ch. I (4-1-25 Edition)",
                "year": "4–1–25 Edition（修订至 2025-04-01；书页 379–385，7 页 / 8 条款）",
                "content_type": "regulation（联邦法规正文，最终规则，具法律约束力）",
                "source_id": "src-fda-cfr-part114-2025",
                "source_file": "books/fda-pchf-human-food-guidance/source-cfr-part114-2025.md",
                "note": "同一专用双栏脚本转出。§114.3 给 acid foods / acidified foods 定义与 4.6 / 0.85 边界及排除项；§114.5 明文把 §§114.10/114.80/114.83/114.89/114.100 与 parts 110 and 117 一并列为掺假判定依据；§114.10 BPCS（课程含 pH controls and critical factors in acidification）；§114.80 成品 pH ≤4.6 按时达到并维持 + 热处理杀 vegetative cells + pH >4.0 用电位法；§114.83 scheduled process；§114.89 三条偏差路径（含按 part 113 热处理）；§114.90 方法；§114.100 记录（(e) 加工厂或其他合理可及地点整段 3 年，无 1+2 分段、无 part 11 条款）。⚠ 本件还锁死一处纠错：parts 110 and 117 是现行文本、不是笔误——FDA 2018-09-12 最终规则（FR Doc. 2018-19855）撤回了 2015 规则拟删除 part 110 的 amendatory instruction 13，Part 110 至今有效但正文本包未收。引用用〔§ 114.xxx〕。",
            },
            {
                "title": "Compliance Program 7303.878 - Foreign Supplier Verification Programs Inspections",
                "author": "U.S. FDA, Human Foods Program (HFP) / Office of Inspections and Investigations (OII)",
                "year": "Transmittal 2023-CPM-CFSAN-003；Implementation Date 09/27/2023；Date of Issuance 08/28/2025（更正）；33 页 / 20 书签",
                "content_type": "inspection-program（FDA 给检查员、进口分区合规官与中心审评人员的内部作业指导；非法规、非 Guidance for Industry、不创设企业义务）",
                "source_id": "src-fda-cp-7303-878-2023",
                "source_file": "books/fda-pchf-human-food-guidance/source-cp-7303-878-2023.md",
                "note": "由用户提供的官方 508-Compliant PDF 经 pdf2md-pro 转换并清除 62 行页眉。⚠ 版本判定：Change History 为 2021-10-20 首发 → 2023-09-27 Update（改名 FSVP Inspections、补 7303.803A / 7303.080 程序交互、Part V 执法澄清）→ 2024-08-20 Pen/Ink → 2025-08-28 Corrections（仅 POC 与机构名称缩写更新）；故为 2023 版程序的 2025 更正版，不是 2025 新 program。法源为 FSMA §301 增订的 FD&C Act §805 与 21 CFR part 1, subpart L（§§1.500-1.514），**该法规正文本包未收，一律标转引未收**。PART II.3.A 给 deemed compliance：进口商同时为 manufacturer/processor 且符合 21 CFR part 117 / 507 供应链要求时视为符合 FSVP，但 except they must comply with section 1.509；不是 receiving facility 的进口商仍须完整 FSVP。PART III.1.C 明写 Samples will not be collected as part of an FSVP inspection、PART IV 四节 Intentionally Left Blank。PART V 给 483a 观察分级、NAI/VAI/OAI、§801(a)(3) / §1.514(a) 拒绝入境与 §301(zz) / §1.514(b) 禁止行为、direct reference authority 仅限有限情形、Import Alert 99-41 Red List 按『食品+境外供应商』组合列入与移除流程。⚠ 99-41 与 CP 7303.070 的 99-37 / 99-38 不是同一个 Import Alert。引用用「CP 7303.878 PART x」。仍未收：21 CFR part 1 subpart L / 111 / 112 / 120 / 507 正文（part 123 自 v4.9 起已收）、Import Alert 99-41 全文、FSVP Guidance for Industry、FSVP Implementation Work Instructions 与 IP guidance tabs、HFP Enforcement Bulletin #13/#6、RPM 4-1-8、SOP-001642",
            },
            {
                "title": "21 CFR Part 123 - Fish and Fishery Products (4-1-25 Edition)",
                "author": "U.S. Government Publishing Office / eCFR, 21 CFR Ch. I (4-1-25 Edition)",
                "year": "4–1–25 Edition（修订至 2025-04-01；书页 456–464，9 页 / 13 条款）",
                "content_type": "regulation（联邦法规正文，最终规则，具法律约束力）",
                "source_id": "src-fda-cfr-part123-2025",
                "source_file": "books/fda-pchf-human-food-guidance/source-cfr-part123-2025.md",
                "note": "由用户提供的 CFR-2025-title21-vol2-part123.pdf 经本包专用脚本 .cangjie/convert_cfr_part.py 双栏重排转出（未用 pdf2md-pro，后者会把同一 y 坐标的左右栏并成一行）。自检：13/13 条款命中、页眉与独立页码残留 0、卷首 Sec. 目录区裁掉 34 行、尾部 Part 124 残段裁 19 段、串栏 0。⚠ 版本判定：4–1–25 Edition 是 CFR 年度编纂版次（修订至 2025-04-01），不是 2025 新规则；SOURCE 60 FR 65197 (1995-12-18)，§123.5 与 §123.11 经 80 FR 56167 (2015-09-17) 修订。核心接口双向锁定：§123.5(a) 明写 `Except as provided by § 117.5(b), parts 110 and 117 of this chapter apply`，§117.5(b) 则给 `if you are required to comply with, and are in compliance with, part 123` 的条件性豁免 —— 与 part 113 的 §117.5(d)(1) 同构，但 §117.5(b) 没有 §117.5(d)(2) 那样的『仅限微生物危害』限缩款，两个方向的误读都要纠正。Subpart B/C 是 augments subpart A 的叠加而非替代。§123.16 的 except part 113/114 只排除该条、不排整 part。§123.12 进口商验证与 FSVP 是两套法源，deemed compliance 不覆盖 §123.12。§123.9(b)(1) 记录期为冷藏 1 年 / 冷冻-保藏-货架稳定 2 年，与 Part 113 的 1+2 年、Part 114 的整段 3 年是三套口径。仍未收：21 CFR part 1240 / 110 / 507 正文、NSSP Guide（FDA《Fish and Fishery Products Hazards and Controls Guidance》自 v4.10 起已收，见 CAP-23）。引用用〔§ 123.xxx〕。",
            },
            {
                "title": "Fish and Fishery Products Hazards and Controls Guidance (4th ed., June 2022) — Seafood Hazards Guide",
                "author": "U.S. FDA, HHS / PHS / CFSAN / Office of Food Safety, Division of Seafood Safety",
                "year": "June 2022 第 4 版（SGR 129）；正文多章页脚仍为 June 2021，Appendix 3 / 5 为 A3-1 / A5-1 (June 2021)，Ch.19 书目 August 2019，属分章滚动修订",
                "content_type": "regulatory-guidance（Guidance for Industry，非约束性；should 仅为建议，可用替代控制策略但须科学论证其充分性）",
                "source_id": "src-fda-seafood-hazards-guide-2022",
                "source_file": "books/fda-pchf-human-food-guidance/source-seafood-hazards-guide-2022.md",
                "note": "由 WorkBuddy 资料库节点 XMsRyrFL0wM1hesg8X6K9u 导出，1,709,446 字节 / 31,321 行；正文 21 章 + 12 附录 + 2 份附加法规全文转录。本件是 21 CFR Part 123 的配套**技术指南层**（how to 判定），与 CAP-22 的**法条义务层**配对而非合并：Ch.2 的 18 步 HACCP 计划开发流程、Ch.3 三张潜在危害表（品种相关 Table 3-2 / 3-3、工艺相关 Table 3-4）与 Ch.4–21 联动、Step 10 在无控制条件下按 `reasonably likely to occur` 逐步判显著性且 Yes/No 都要写第 4 栏理由、Step 11 用 Appendix 3 判定树定 CCP、控制策略示例的 CCP 漂移、关键限值与监控四问。⚠ 三项红线：① 表不得单独使用、指南不替代危害分析、须警觉新出现危害与物种替换；② Appendix 5 的组胺 50/500 ppm 等数值回指 CPG / 21 CFR 556 / 40 CFR 180 / NSSP Guide，是外部法源快照而非本指南新设限值，一律标转引未收；③ 导出件表格列头连写、词条粘连、字符丢失、页码混入、Appendix 3 的 CCP 判定树塌陷成残表，逐字引用只能取散文段落（CAP-23 R 段 37 块经 .cangjie/verify_v4_10_quotes.py 核验 37/37 命中）。引用用「Seafood Hazards Guide 第 4 版 Ch.x / Appendix x / L####」，法条用〔§ 123.xxx〕，不可混引。仍未收：NSSP Guide、21 CFR part 1240 / 110 / 507 正文、Import Alert 16-xx、BAM 海产品章节",
            },
            {
                "title": "Compliance Program Guidance Manual 7303.842 - Seafood Processor, Products, and Importer Inspection Program",
                "author": "U.S. FDA, Human Foods Program (HFP) / Office of Inspections and Investigations (OII)",
                "year": "IMPLEMENTATION DATE 11/01/2023；Correction date 09/30/2025；80 物理页 / 148 书签（首页标 Page 1 of 86）",
                "content_type": "inspection-program（FDA 给检查员、进口分区、分部合规官与实验室的内部作业指导；非法规、非 Guidance for Industry、不创设企业义务）",
                "source_id": "src-fda-cp-7303-842-2023",
                "source_file": "books/fda-pchf-human-food-guidance/source-cp-7303-842-2023.md",
                "note": "由用户提供的官方 508-Compliant PDF 经用户级技能 pdf2md-pro（pymupdf4llm 2.1）转换，正文 179,812 字节 / 1,334 行；148 书签全命中、203 表格行、残留页码 0。⚠ 文件名 20250929 只是 PDF 生成日（creationDate 2025-09-29），本件是 2023-11-01 版程序的 2025-09-30 更正本，不是 2025 新签发 program；封面 Date of Issuance 09/30/025 为文本层残缺，正文页脚 11/1/2023。首页 NOTE 与 PART I 写明 CP 7303.842 与 CP 7303.844 已合并为单一程序，但 PAC 仍分进口 03844x / 国产 03842x。PART II Table 1 产品/工艺风险与 Table 2 企业/进口商 work planning（90/10、100 entry line items）不可对调；PART III 六类检查分流与 Sampling 三类（国产 for cause only、进口监督、documentary 只报 03842）；PART IV A–G 的 500/50/35 ppm、15/25 µg/100g、48 subs 等全是检查员触发值而非法规限值，判据出口为 CPG 540.525 / 540.370 / 562.300 等（未收）；PART V Table 4 是 ranking 且 case-by-case，WL / DWPE / judicial actions 须 HFP OCE concurrence；FIELD REPORTING 用 FACTS / CMS / FDA 3501·3502；ATTACHMENT A 样品量仅 surveillance and audit。引用用「CP 7303.842 PART x / Table x / ATTACHMENT A #x / Lxxx」，逐字引证以原文字符串为准。⚠ 转换件存在书签标题与正文伪标题交错（PART 各出现两次、H1 虚高 133），检索以 PART / 小节 / 表号为准，表格与页眉不可逐字引用。仍未收：CPG 全文、21 CFR part 1240 / 110 / 507、NSSP Guide、BAM / AOAC / MPM 方法全文、Import Alert 16-xx 全文、21 CFR part 1 subpart L、IOM Ch.4、FDA 3501/3502 表单全文与 eNSpect / CMS / FACTS 内部系统 —— 一律标转引未收",
            },            {
                "title": "21 CFR Part 108（2025 版）法规正文 — Emergency Permit Control",
                "author": "U.S. FDA（eCFR/GPO 现行文本）",
                "year": "2025",
                "content_type": "regulation（最终规则，具法律约束力）",
                "source_id": "src-21-cfr-part-108-2025",
                "source_file": "source-cfr-part108-2025.md",
                "note": "由用户提供的 GPO 印刷版 CFR-2025-title21-vol2-part108.pdf（175 KB，11 页，书页 248–258）经本包专用脚本 .cangjie/convert_cfr_part.py 双栏重排转出，再用 fix_part108_reflow.py 定点修 6 处重排缺陷（1 处正文句被误升为条款标题、4 处句中断段、1 处两编号项并段）。自检：9/9 条款命中（108.3/.5/.6/.7/.10/.12/.19/.25/.35）、页眉与独立页码残留 0、裁掉首部 Part 107 残段 9 段与尾部 Part 109 残段 14 段、串栏 0；逐字引用核对 27/27 命中、0 超 100 词、0 表格引用。⚠ 4–1–25 Edition 是 CFR 年度编纂版次（修订至 2025-04-01），不是 2025 新规；SOURCE 为 42 FR 14334, Mar. 15, 1977, unless otherwise noted。**法条定位**：Part 108 是 FD&C Act §404 的实施细则（AUTHORITY 21 U.S.C. 342, 344, 371），与 CAP-20 的 Part 113/114 构成「手续层 + 实体层」同一链条——Subpart A（108.3/.5/.6/.7/.10/.12/.19）给许可裁定/撤销/签发/中止/无证生产/豁免程序，Subpart B（108.25 酸化食品 / 108.35 LACF）给注册（Form FDA 2541，首次从事后 10 天内，外国加工者报检前）与工艺备案（2541e / 2541d / 2541f / 2541g，注册后 60 天内且包装新产品前）。**最易错处**：紧急许可是 `may be required` 的救济手段而非常态义务，触发前提是未履行 108.25/108.35 的义务（prima facie basis）；Subpart A 全是 working days（3/5/10/20），Subpart B 全是日历天（10/30/60/90），不可互换；记录保存 108.25(g) 整段 3 年 vs 108.35(h) 1+2 年，与 113.100(g)/114.100(e) 共四套口径；外国加工者走 §801 拒绝入境而非紧急许可。仍未收：2541 系列表单栏目细则、FURLS / Center Views 操作、21 CFR part 110 / 120 正文、CPG 全套、Import Alert 全文、BAM / AOAC / MPM 方法正文、IOM Ch.4",
            },
            {
                "title": "21 CFR Part 120（2025 版）法规正文 — Hazard Analysis and Critical Control Point (HACCP) Systems",
                "author": "U.S. FDA（eCFR/GPO 现行文本）",
                "year": "2025",
                "content_type": "regulation（最终规则，具法律约束力）",
                "source_id": "src-21-cfr-part-120-2025",
                "source_file": "source-cfr-part120-2025.md",
                "note": "由用户提供的 GPO 印刷版 CFR-2025-title21-vol2-part120.pdf（176 KB，10 页，书页 439–448）经本包专用脚本 .cangjie/convert_cfr_part.py 双栏重排转出，再用 fix_part120_reflow.py 定点修 11 处段界缺陷（1 处句中断段 + 10 处编号项并段）。自检：15/15 条款命中（120.1/.3/.5/.6/.7/.8/.9/.10/.11/.12/.13/.14/.20/.24/.25）、页眉与独立页码残留 0、裁掉首部 Part 119 残段 3 段与尾部 Part 121 残段 6 段、串栏 0；逐字引用核对 26/26 命中、0 超 100 词、0 表格引用。⚠ 4–1–25 Edition 是 CFR 年度编纂版次（修订至 2025-04-01），不是 2025 新规；SOURCE 为 66 FR 6197, Jan. 19, 2001, unless otherwise noted，§120.5/§120.6 的 80 FR 56167（2015-09-17）是 PCHF 最终规则的 conforming amendment。**法条定位**：Part 120 是独立的果汁 HACCP 体系法规（不是「果汁版 Part 117」）；〔§ 120.5〕一句话锁定接口——`Except as provided by § 117.5(c), parts 110 and 117 ... apply`，即 Part 117 默认适用、§117.5(c) 为唯一条件性出口（**该款全文未收**，不得反推措辞）。**最易错五处**：① 5-log 是〔§ 120.24(a)〕的 shall（须持续、覆盖货架期、正常与中度滥用条件），不是指南建议；② 目标菌是 pertinent microorganism（最耐热＋具公共卫生意义＋可能出现于该果汁），不是沙门氏菌/O157；③ §120.25 的 biotype I E. coli 检测只适用于果面处理者（20 mL/1,000 加仑/生产日，7 次 2 阳性即视为不足），非通用出厂检验；④ 两处豁免对象不同——120.24(a)(1)(2) 免 5-log 指标、120.7(e) 免「part 113/114 已控制的微生物与微生物毒素」危害的计划处理；⑤ 记录复审是 `within 1 week (7 days)`（日历天，非 7 个工作日），记录期为易腐/冷藏 ≥1 年、冷冻/保藏/货架稳定 2 年或货架期孰长、起算点产品制备日，是独立第六套口径。⚠ 文本层缺陷：`5 log (i.e., 105)` 的 `105` 实为 10⁵ 上标丢失，引用须还原并注明。仍未收：§117.5(c) 逐字文本、21 CFR part 110 正文、CP 7303.047 果汁 program、CPG 与 Import Alert 全文、BAM / AOAC 方法全文",
            },

        ],
    },
    "entry": {
        "name": "fda-pchf-food-safety",
        "description": (
            "FDA 人类食品危害分析与基于风险的预防控制（PCHF / 21 CFR Part 117 / FSMA）技能，融合行业指南方法论与法规正文法定义务。"
            "当用户需要：做食品危害分析（六列工作表）、判定法定义务与法定豁免（条款级）、设计或验证热处理/工艺控制、"
            "设计过敏原控制与排产、环境病原（李斯特菌/沙门氏菌）与卫生控制策略、化学危害与经济掺假判定、"
            "供应商批准与验证活动选择、召回计划与报告食品义务、FDA 食品法规适用边界判断、"
            "qualified facility 豁免撤销应诉（上诉/听证/时限）、美国食品安全计划（FSP）要素设计时触发。"
            "尤其覆盖 RTE 即食食品李斯特菌专项：抑制型（listeristatic）与致死型（listericidal）配方设计及验证、"
            "环境监测点位/频次/阳性升级决策树、卫生程序与清洁消毒作业、厂房分区与气流排水及设备卫生设计、"
            "人员手套与工服及动线控制、成品抽检与 hold and test、储运温度控制。"
            "另覆盖 cGMP（21 CFR Part 117 Subpart B）合规资料分层与内审分诊：判断该看哪份官方文件、"
            "FDA 行业指南/小企业合规指南/执法口径文件的效力层级、Subpart B 九条逐条取证要点、"
            "cGMP 与 PCHF 的分层关系、以及指南 should 与法规 must 的主体分流读法。"
            "另覆盖过敏原标签口径（FDA 食品过敏原问答 Ed.5，2025-01 修订终版）：Big 9 类别、Table 1 封闭树坚果清单、非牛乳/非鸡蛋的动物来源标注、allergen-free 声明与 advisory 声明的互斥判别。"
            "另覆盖食品缺陷行动水平（FDA Food Defect Levels Handbook）：虫碎片/鼠毛/霉变等天然不可避免缺陷的 111 个产品阈值与 SIGNIFICANCE 判读、〔§ 117.110〕最低可行水平义务与掺混稀释禁令、110.110 引用纠偏（v4.7 更正：Part 110 至今有效、正文未收）、表内无产品时的逐案评估，以及霉菌类缺陷与真菌毒素化学危害的联动分诊。"
            "另覆盖 FDA 现场检查迎检（CPGM 7303.040 现行版）：8 类检查与 PAC 码识别、Limited Scope / Full Scope / Focused PCHF 的取证深度与转换条件、〔§ 117.320〕official review 与〔§ 117.315(c)〕FSP 现场/24 小时记录举证矩阵、FDA 483 的 15 个工作日回复骨架、eNSpect 观察项与 OAI/VAI/NAI 三层分级、OAI 后 6 个月跟进检查，以及 2020 版旧口径纠偏。"
            "另覆盖 FDA 现场取样（CP 7303.050，2022 签发 / 2025-09-10 更正）：PAC/PAF 归属识别、Table 2/3 的产品样品 subs 数与 702(b) 部分、ATTACHMENT A 环境拭子 Listeria ≥50 / Salmonella ≥100 与 Zone 1–3 分区、湿干区目标菌选择、WGS 与 GenomeTrakr、ATTACHMENT A Part V 三档 Findings 与 PART V 表 7/8 的逐案执法响应清单、进口状态样品与 ATTACHMENT B 污秽/霉变抽样。"
            "另覆盖 FDA 检查员权限与文书（IOM 2026 Chapter 5）：FD&C Act 704(a)(1) 与合理时间/合理方式、FDA 482/482c/482d/483/483a/484/4056 表单地图、境内预告 5 个日历日与境外通常提前告知的口径、拒绝入场/拒绝记录与 807(b) 拒绝入境后果、483 只写事实且不引法规原文也不引 guidance 偏离的措辞纪律、non-reportable observations、15 个工作日双出处、电子记录与照片的证据固定规则，以及「样品合格不阻碍 cGMP 指控」。"
            "另覆盖低酸罐头与酸化食品检查（CP 7303.070，2024 签发 / 2025-09-26 更正）：按〔§ 117.5(d)(1)(2)〕把 part 113 管辖的微生物危害与仍需 PCHF 的化学/物理/金葡危害切开、酸化食品不免 Subparts C/G 的分流、〔§ 117.1(c)〕专项 CGMP 与 Part 117 并行、Keep Refrigerated 与 brites 的 program 路由、RRA 不是 704(a)(1) inspection 的法定地位、酸化食品判定三步与 Maximum Equilibrium pH、FCE/SID 与 Process Authority 及温度分布/热穿透/卷边/异常罐的取证清单、pH 4.40/4.65 双分析师规则与 4.6 法定边界的三套数字区分、24 罐/12 罐取样量、异常罐 1% 与 pH 4.75 肉毒毒素升级、Import Alert 99-37/99-38 与「未备案本身不构成 DWPE」的反直觉限制。"
            "另覆盖低酸罐头与酸化食品的条款级法定义务（21 CFR Part 113 / 114 法规正文，4-1-25 Edition）：按〔§ 113.3(n)〕〔§ 114.3(b)(d)〕的成品平衡 pH 4.6 / aw 0.85 判定 LACF / AF / 酸性食品身份，〔§ 117.1(c)〕专项 CGMP 与 Part 117 并行、〔§ 117.5(d)(1)(2)〕双条件且仅限微生物危害的有限豁免、part 114 不在豁免清单内、〔§ 114.5〕并列 parts 110 and 117 的掺假判据，Part 113 的 §113.10/40/60/81/83/87/89/100 与 Part 114 的 §114.10/80/83/89/90/100 义务清单，成品 pH >4.0 用电位法〔§ 114.80(a)(2)〕、酸化不等于免除热处理〔§ 114.80(a)(1)〕、§114.89 三条偏差路径、scheduled process 的 FDA 调阅权〔§ 113.87(b)〕、两 part 记录保存口径差异（§113.100(g)(h) 1+2 年且可用 part 11 电子记录；§114.100(e) 整段 3 年且无 part 11 条款），以及 4.6/0.85/4.0 法定数字与 CP 7303.070 的 4.40/4.65 检查员触发线、L.mono ≤4.4/≤0.92 建议层基准的三层区分。"
            "另覆盖海产品 HACCP 的条款级法定义务（21 CFR Part 123 法规正文，4-1-25 Edition）：按〔§ 123.3(d)(e)(k)〕判定 fish / fishery product 与 processing 范围及 (k)(2) 三项排除，〔§ 123.5(a)〕Part 110/117 默认适用与〔§ 117.5(b)〕双条件豁免（并指出该款无 part 113 §117.5(d)(2) 的微生物危害限缩），〔§ 123.15〕〔§ 123.20〕Subpart B/C 的 augments 叠加而非替代，〔§ 123.6〕危害分析与 HACCP 计划及 (c)(1) 九项危害考虑清单、〔§ 123.7〕纠正措施三条路径、〔§ 123.8〕验证含 1 周记录复审与至少每年复审、〔§ 123.9〕记录分类 1 年/2 年与即时报录、〔§ 123.10〕培训课程等效或岗位经验、〔§ 123.11〕SSOP 的 should 与监测记录的 shall 之别及八项卫生条件、〔§ 123.16〕熏制水产品肉毒控制覆盖货架期且 except 仅排 part 113/114 管辖者、〔§ 123.28〕双壳贝类源头控制与 tag 五要素、〔§ 123.12〕进口商二选一与 affirmative steps 及拒绝入境后果，并区分 §123.12 与 FSVP 双轨互不替代、三套记录期口径不可串用。"
            "另覆盖 FSVP 进口商检查（CP 7303.878，2023 版 / 2025-08-28 更正）：按 §1.500 判定 FSVPI 身份、FSVP（FD&C Act §805 / 21 CFR part 1 subpart L）与 Part 117 Subpart G 供应链程序的主体分流、deemed compliance 但不免 §1.509 每一 entry line 的 UFI/DUNS 申报、§1.501 八类豁免与 standard / modified requirements 分节、FSVP 检查不取样与 PART IV 全空、483a 观察分级与 NAI/VAI/OAI、§801(a)(3) 拒绝入境与 §301(zz) 禁止行为、Warning Letter → Import Alert 99-41 Red List 加/删名单与「未上 Red List 仍可进口」等反直觉限制。"
            "另覆盖海产品危害分析与控制的完整判定链（FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版 June 2022，技术指南层）：18 步 HACCP 计划开发流程、Ch.3 品种相关与工艺相关危害三表与 Ch.4–21 联动、在**无控制条件下**按 reasonably likely to occur 逐步判定显著性且 Yes/No 均须书面写理由、显著不等于本步设 CCP、Appendix 3 判定树定 CCP、control strategy example 的 CCP 位置漂移、关键限值可替代但须科学论证充分性、监控四问 What/How/Frequency/Who，以及组胺与寄生虫等建议参数适用边界和『指南非强制 vs Part 123 法定义务』双向分流。"
            "另覆盖海产品检查程序的完整判定链（FDA CP 7303.842，2023 版 / 2025-09-30 更正，检查程序作业层）：CP 7303.842 与 7303.844 已合并但 PAC 仍分进口/国产、Table 1 产品/工艺风险与 Table 2 企业/进口商 work planning 的分工及 90/10 规则、六类检查分流（Processor / Importer / Vessels / Foreign Establishment / NSSP / EMA）与 HACCP Program Evaluations、Sampling 三类与国产 for cause only、PAC 双码表与 03842H 同名不同义、PART IV A–G 实验室分流与『触发值不是法规限值』、Table 4 违规分级与 case-by-case、WL / DWPE / judicial actions 的 HFP OCE concurrence、Species misbranding 的 FD&C Act 403(b) 定性、FIELD REPORTING 的 FACTS / CMS / FDA 3501·3502 出口、ATTACHMENT A 样品量适用域，以及十八类来源不可混引与三层配对（法条 CAP-22 / 指南 CAP-23 / 检查程序 CAP-24）。"
            "另覆盖果汁 HACCP 体系的完整法定义务链（21 CFR Part 120 法规正文，4-1-25 Edition，10 页 / 15 条款）：先按〔§ 120.1(a)〕定义 juice（含浓缩物与果泥、作饮料配料也算）并用〔§ 120.3(j)(2)〕排除采收采摘运输与零售经营、〔§ 120.3(l)〕判零售 establishment，再按〔§ 120.5〕确认 **Part 117 默认适用、〔§ 117.5(c)〕为唯一条件性出口（该款全文未收）**；Subpart A 给 SSOP 八项、书面危害分析五项与 prudent processor 判定、九项应考虑危害、HACCP 计划七要素（厂内/厂外 CCP 分列）、纠正措施五步（隔离扣留优先）、六类验证活动与 12 个月/每年确认、五类记录与通用要素、培训四职能、进口商二选一 + 六项 affirmative steps；Subpart B 给 **5-log（10⁵）法定削减**（持续、覆盖货架期、正常与中度滥用条件，目标菌为 pertinent microorganism）与**果面处理者专项的 biotype I E. coli 验证**（20 mL/1,000 加仑/生产日，7 次 2 阳性即视为控制措施不足）。**核心纠偏**：5-log 是 shall 不是建议；§120.25 只适用于果面处理者；120.24(a) 免的是 5-log 指标、120.7(e) 免的是 113/114 已控制的微生物类危害，两者对象不同；记录复审是 1 周（7 日历天）而非 7 个工作日；记录期为易腐 1 年 / 冷冻-保藏-货架稳定 2 年或货架期孰长，起算点为产品制备日"
            "另覆盖 LACF／酸化食品的紧急许可控制与注册备案（21 CFR Part 108 法规正文，4-1-25 Edition，11 页 / 9 条款）：把「手续层」与「实体层」分开——Subpart A（§108.3/.5/.6/.7/.10/.12/.19）给许可裁定（3 个工作日异议、5 个工作日听证、听证后 5 个工作日裁定）、紧急性健康危害下的立即生效、许可签发或拒绝（10 个工作日可再延 10）、中止与恢复（立即中止 + 10 个工作日答复）、无证生产的产品扣留与事先书面批准（须证明 free from microorganisms of public health significance，20 个工作日答复）、以及「全部满足才豁免」的许可豁免；Subpart B 给注册（Form FDA 2541，首次从事后 10 天内，外国加工者报检前）与工艺备案（酸化食品 2541e / LACF 2541d·2541f·2541g，注册后 60 天内且包装新产品前）、停业 90 天通知、腐败与偏差报告、LACF 独立的微生物污染报告、召回程序文件、BPCS 受训主管、记录保存（108.25(g) 整段 3 年 vs 108.35(h) 1+2 年）。**核心纠偏：紧急许可不是常态义务**——108.25(a)/108.35(a) 均为 `may be required`，未履行义务只构成 `prima facie basis`；Subpart A 全是 working days、Subpart B 全是日历天，不可互换；外国加工者走 §801 拒绝入境而非紧急许可；108.35 独有的 FSIS 连续检验豁免、加州视为合规与 FOIA 豁免不得套到酸化食品。"
            "适用于食品工厂质量/合规人员、采购与供应商管理者、食品工艺研发、跨境食品贸易合规咨询，以及需要准备 FDA 现场检查、取样配合、483 回应与低酸/酸化罐头产品管辖判定的团队。"
        ),
        "core_principles": [
            "先分层再引用：**法规正文层自 v4.9 起含四套独立编号**——21 CFR Part 117〔§ 117.xxx〕、Part 113〔§ 113.xxx〕、Part 114〔§ 114.xxx〕、Part 123〔§ 123.xxx〕，均为最终规则、具法律约束力，各管各自义务；FDA 行业指南（草案，should 级方法论建议）为另一层。冲突时法规为准，指南只作解释与例证；「Part 117 是唯一判定基准」只能理解为**判定 Part 117 义务**的唯一基准，不能解释成全包唯一法条",
            "危害分析做错或漏识别，整个 FSP 无效——无论执行得多好；判定必须书面，解释 No 与解释 Yes 同等重要",
            "危害判定分三层级：hazard → potential hazard（附录 X 标记仅为起点）→ hazard requiring a preventive control，最终责任在每个工厂",
            "判 No（不构成需控危害）与判 Yes 但不实施预防控制（§ 117.136 五情形出口）是两层不同的事，混层会得出错误结论",
            "发现点不等于控制点：在识别出危害的步骤之外控制往往是更优解（六列工作表第 6 列）",
            "RTE 食品包装前暴露于环境且包装后无致死处理，必须评估环境病原体（117.130(c)(1)(ii)）；法定'环境病原'明确排除产芽孢菌芽孢",
            "热处理只杀营养细胞不灭孢子、不消除已形成毒素；控制目标用 D/z 值与 6D 削减倍数表达（L. mono 70°C/2min；非蛋白分解 C. botulinum 90°C/10min）",
            "监控四问（What/How/How often/Who）；发现偏差应假定自上次合格检查起全部未受控；记录审查是 7 个工作日不是 7 天",
            "correction vs corrective action 的法定分诊是两条并列通道：过敏原交叉接触/卫生控制的条件与实践不一致（及时纠正即可）、轻微且孤立不影响安全的问题",
            "检测只能作为供应商验证的补充手段（这是指南的保守解读，法规未禁止其作唯一手段）；SAHCODH 危害要求首次使用前 + 每年现场审核，除非书面认定替代方案",
            "湿/干环境二分法决定环境病原战略：湿区防李斯特菌靠保持干燥，干区防沙门氏菌靠严格控水",
            "FSP 至少每 3 年再分析；变更、新危害信息、意外问题、控制无效均触发（可限于相关部分）；FDA 也可指令再分析",
            "法定义务常带硬时限与法定出口：豁免日历、15/90/120 日窗口、7 工作日记录审查——答复前先查条款，别凭印象给数",
            "本技能有三层权威，先分层再引用：21 CFR Part 117 法规正文（最终规则，must 级法定义务，标注〔§ 117.xxx〕）；FDA PCHF 行业指南（草案，should 级方法论）；FDA《Control of Listeria monocytogenes in RTE Foods》(2017-01 Draft，一律 we recommend，建议层)。第三层指南正文出现 must 时，均是该指南在引述 Part 117 的法定义务——不得把建议层内容升格为法定义务",
            "两套 pH/aw 基准用途不同、不得互相替换：pH 4.6 / aw 0.85 是 Part 117 酸化食品管辖边界与安全水分水平（法定/通用口径）；pH ≤4.4 / aw ≤0.92 是 L.mono 抑制型配方设计基准（2017 草案建议层）。同一个 0.92 在芽孢萌发视角与李斯特菌营养细胞生长视角下含义不同",
            "抑制 ≠ 杀灭：listeristatic 只承诺阻止生长（货架期重复生长研究增幅 <1 log），listericidal 才承诺破坏活菌并使成品达到 <0.04 CFU/g 的不可检出性；两者都不能简化成'pH 低'或'有热处理'一句话",
            "工艺闭环之外还有环境闭环：listericidal 工艺无法解决工艺后再污染，环境病原防线（工程控制、卫生程序、环境监测、人员卫生）须与工艺控制成对设计",
            "成品检测与环境监测方向相反：成品应检 L. monocytogenes，环境常规监测检 Listeria spp. 以指示定殖；成品检 spp. 阳性须判定是否 L. mono，否则按 L. mono 污染处理",
            "cGMP 合规资料按四层效力栈使用：Part 117 法规正文（唯一判定基准）＞ FDA 小企业合规指南 SECG（2016-10，白话转述、明确允许替代方案、不创设义务）＞ 专项行业指南（草案建议层）＞ CPG/Compliance Programs（检查视角，非企业义务清单）；合规结论必须能回指〔§ 117.xxx〕，禁止把指南 should 写成 must",
            "cGMP 是观察型结果义务：adequate 的法定定义见〔§ 117.3〕，法规不给数值只给结果；检查看现场状态、实际运行与必要记录，完美的 FSP 不能抵现场卫生失守；cGMP 失守对应 FD&C Act § 402(a)(3)/(4) 掺假认定，与 Subparts C–G 的 prohibited act 是两条不同执法钩子",
            "SECG 的合规日期表（2016/2017/2018 分档）是历史过渡安排，现已全部生效；SECG 是 2016 年 10 月而非 11 月；80 FR 55907（发布通知首页）与 80 FR 56145（条文部分首页）属同一份 2015-09-17 最终规则，不是两份规则",
            "过敏原标签问答 Ed.5（2025-01）解释的是 FD&C Act 201(qq)/403(w) 的标签义务，属 guidance 建议层；Part 117 的过敏原预防控制〔117.135(c)(2)〕与防交叉接触 CGMP〔117.20(b)(2)〕不因标签口径收窄而减少，两套法源不得混引",
            "Big 9 的食物类别未变，变的是类别内的物种口径：树坚果以 Ed.5 Table 1 的 12 种封闭清单为准（官方全文未点名 coconut，仅规定未列入表者不得进 Contains、但仍须按通用名列入配料表）；milk 含牛/山羊/绵羊及其他反刍动物，eggs 含鸡/鸭/鹅/鹌鹑及其他禽类",
            "缺陷行动水平是 FDA 依 402(a)(3) 执法的裁量参考，不是法规上限、不是平均值、不是内控目标：法定义务是〔§ 117.110(a)〕must ... reduce natural or unavoidable defects to the lowest level currently feasible；〔§ 117.110(b)〕禁止掺混稀释且终产品检测值不影响掺假认定；低于阈值仍可因 402(a)(4) 卫生失守被判掺假",
            "**v4.7 实质性纠错：Part 110 至今有效**。Handbook 网页的 21 CFR 110.110 不是过时引用：2015-09-17 PCHF 最终规则（80 FR 56144）的 amendatory instruction 13 本拟于 2018-09-17 `remove and reserve part 110`，但 FDA 2018-09-12 最终规则（FR Doc. 2018-19855）撤回该指令（`amendatory instruction 13 ... is withdrawn`），因合规日期延长会造成 4–16 个月 CGMP 空档；eCFR 现行版 Part 110 仍列 11 个 sections（含 §110.110），§114.5 并列 `parts 110 and 117` 也是现行文本。正确处理是「现行仍有效、但正文本包未收 → 转引未收」；Part 117 侧对应〔§ 117.110〕（仅 (a)(b) 两款）＋〔§ 117.3〕＋〔§ 117.80(b)(3)(4)〕，手册那句『不良生产实践可不论行动水平执法』是 §110.110(c) 意译，**仍不得标成〔§ 117.110(c)〕**，但理由是「那是 part 110 的 (c) 款」；SIGNIFICANCE 标 Potential health hazard 的霉菌类缺陷须联动真菌毒素化学危害分析",
            "迎检先分三层再谈准备：CPGM 7303.040（2025-CPM-HFP-001）是 FDA 给检查员/分部的内部作业指导，不创设企业义务；单条观察项在 eNSpect 只有 major (significant) / minor (not significant)，整次检查才 categorized as critical / major / minor 且 investigators do not make this categorization，检查分类另为 OAI / VAI / NAI。2020 版把三级挂在观察项上已废止，03040U 也已从 PCHF Follow-Up 改为 Focused PCHF；CPGM 的 6 个月复检、Direct Reference、OCIC 流程不是企业法定时限",
            "记录举证是迎检硬义务：〔§ 117.320〕口头或书面请求即须 promptly 提供并可供复制；〔§ 117.315(c)〕FSP 必须在现场、其余异地记录须 24 小时内取回现场；〔§ 117.305〕记录须与实际活动同步生成、含实际观测值与签名批号；〔§ 117.310〕FSP 初次完成与每次修改均须 owner/operator/agent in charge 签字注日期；〔§ 117.190(a)〕六类实施记录。CPGM 的 15 个工作日 483 回复期望不是法定时限，不得与 7 工作日记录审核、豁免撤销 15/90/120 日窗口混算",
            "CP 7303.050 是抽样 program 不是检查 program：原文 Inspections are not planned under this compliance program；抽样发生在 7303.040 等检查中。Table 2/3 的 subs 数是 FDA 取证量（不含 702(b) 部分），不是企业批放行标准；环境拭子 Listeria 最少 50 subs（理想 100）、Salmonella 最少 100 subs（理想 300），Listeria 主要 Zone 1–3、Salmonella 主要 Zone 2–3；确认阳性一律 WGS 并进 GenomeTrakr；PART V 表 7/8 是逐案、非穷尽的可能 FDA 响应清单，不是法定后果表",
            "IOM 2026 Chapter 5 从检查员侧反证效力分层：483 只写事实性、显著观察项，不得引用法规原文、不得纳入标准、不得引用 policy/guidance 偏离，也不得写 opinions 或 characterize conditions as violative；仅偏离官方 guidance 而未违反法规的属 Category 3 non-reportable observation，只能口头讨论并写入 EIR。这证明 Guidance / SECG / Handbook / CPGM / CP 7303.050 都不是可直接开观察项的法定义务——但同一事实若同时构成〔§ 117.xxx〕失守，仍会被写成事实性观察项",
            "预告口径不得说绝对：IOM 5.2.7 写明医疗器械 surveillance 与部分 BIMO 强制预告、常规 produce farm 检查应预告、食品企业检查 it may be inappropriate to pre-announce（由 program division 裁量）、而 the Agency usually announces foreign inspections in advance（签证与成本原因）。国内预告一般不少于 5 个日历日、改期不晚于原日期 +5 天，且预告不是预约（It is not to make an appointment for the inspection）。2025 年境外无预告检查扩张属政策层且 FDA 公告原文未收，只作随时可被检查的准备原则",
            "检查员文书与证据规则：国内到场出示 credentials 并签 FDA 482（境外一般不发 482 但仍须出示证件）；采集任何实体样品必发 Form FDA 484；检查员不得取走企业唯一记录副本、不得亲自登录企业系统查电子记录、照片是 exhibit 而非样品且只能用 FDA 配发设备；拒绝提供法规未强制要求的信息（配方、发货清单、生产编码）不构成 inspection refusal，境外拒绝检查可触发 FD&C Act 807(b) 拒绝入境。样品合格不阻碍 cGMP 指控（IOM 5.6.4）",
            "LACF/AF 与 Part 117 的管辖按危害类别切分、不做全有全无判断：〔§ 117.5(d)(1)(2)〕只免 part 113 覆盖活动的 Subparts C/G 且仅限其管辖的微生物危害，未被热处理控制且需预防控制的危害（金葡生长产毒、化学、物理）仍归 C/G（CP 7303.070 PART II.2.C(1)）；〔§ 117.1(c)〕明定受专项 CGMP 管辖的食品同时受 Part 117 约束。**酸化食品不在该豁免内**——Acidified foods are subject to the CGMP & PCHF rule，PCHF 覆盖转 7303.040，但检查重点仍在 21 CFR part 108/114；**〔§ 117.201〕是 qualified facility 的 modified requirements，不是 LACF 条款，不得误引**。Keep Refrigerated 产品免 113/114 并转 7303.050，brites 中央仓报 PAC 03040",
            "三套 pH/aw 数值用途不同、不可互替：pH 4.6（平衡 pH）/ aw 0.85 是〔§ 117.3〕〔§ 117.80(c)(14)(15)〕的法定边界与持续维持义务；pH 4.40/4.65/4.75、aw 0.90/0.93、异常罐 1%、795 g/24 罐与 12 罐是 CP 7303.070 的实验室复测、升级与取证触发线，属检查员作业口径、不是企业放行标准；pH ≤4.4 / aw ≤0.92 是 L.mono 草案抑制型配方基准（建议层）。FDA 实验室另守 Never average the two analysts' results together：original analysis 与 check analysis 分别判定",
            "CP 7303.070 依据的 **21 CFR part 113 / 114 法规正文自 v4.7 起已收（CAP-20）**：scheduled process、商业无菌、BPCS、成品 pH、偏差处置、记录保存等法定义务现按〔§ 113.xxx〕〔§ 114.xxx〕引用，不再标「转引未收」；**21 CFR part 108 自 v4.12 起已收（见 CAP-25）**：FCE 注册、SID 定时工艺备案、Emergency Permit、§108.35 BPCS 认可现按〔§ 108.xxx〕引用；**仍未收的是** part 110 与 §117.5(c) 逐字文本（part 123 自 v4.9 起已收，见 CAP-22；part 120 自 v4.13 起已收，见 CAP-26）以及 2541 系列表单栏目细则，一律标「转引未收」，不得从 CP 反推法条或把检查动作写成企业义务。PART II.2.B(2) 给出 RRA 自愿、远程、RRAs are not considered inspections 且不满足 FD&C Act 704 法定检查场景（510(h)/503B(b)），但 FDA 扩大 RRA / 境外无预告检查的政策公告原文仍未收；PART V.2 明写不得仅因未注册/未备案就建议 Import Alert/DWPE",
            "低酸罐头与酸化食品是**并行法条**，不是二选一：〔§ 117.1(c)〕明定受专项 CGMP 管辖的食品同时受 Part 117 约束；〔§ 117.5(d)(1)〕的 Subparts C/G 豁免须同时满足 `required to comply with` 且 `in compliance with` part 113，〔§ 117.5(d)(2)〕又把它限定在 part 113 管辖的**微生物危害**；**part 114 完全不在 §117.5 豁免清单内**，〔§ 114.5〕还反向把 parts 110 and 117 拉进掺假判定。输出必须按危害逐条切分，不能给「整厂免检 / 不免检」的二值结论",
            "21 CFR Part 113 / 114 的义务清单须按条引：〔§ 113.10〕〔§ 114.10〕BPCS 监督（后者课程含 pH controls and critical factors in acidification）、〔§ 113.40〕NIST 溯源校准、〔§ 113.83〕〔§ 114.83〕scheduled process 由 qualified person 确立、〔§ 113.87(b)〕FDA 有权调阅 scheduled process、〔§ 114.80(a)(1)〕酸化不等于免除热处理、〔§ 114.80(a)(2)〕成品 pH >4.0 须用电位法、〔§ 114.89〕三条偏差路径（含按 part 113 热处理）。**〔§ 113.100(g)〕是厂内 ≥1 年 + 另 2 年且 (h) 允许 part 11 电子记录；〔§ 114.100(e)〕只要求加工厂或合理可及地点整段 3 年，无分段、无 part 11 条款**——两处记录口径不得串用",
            "六套法规正文〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕各自独立编号，与 PCHF 指南、L.mono 指南、SECG、Ed.5、Handbook、CPGM 7303.040、CP 7303.050、IOM 2026 Ch.5、CP 7303.070 与 CP 7303.878 合计**十八类不可混引**（v4.8 新增第十三来源、v4.9 新增第十四来源 21 CFR Part 123、v4.10 新增第十五来源 FDA 海产品危害与控制指南、v4.11 新增第十六来源 CP 7303.842、v4.12 新增第十七来源 21 CFR Part 108、v4.13 新增第十八来源 21 CFR Part 120）；CP 7303.070 的 4.40 / 4.65 / 24 罐是检查员实验室触发线，法规里是 4.6 / 0.85 / 4.0，L.mono 草案是 ≤4.4 / ≤0.92，三层数字不得互替",
            "海产品 part 123 与 Part 117 的接口是双向锁定：〔§ 123.5(a)〕明文 `Except as provided by § 117.5(b), parts 110 and 117 of this chapter apply`（默认适用），〔§ 117.5(b)〕给 `required to comply with, and are in compliance with, part 123` 的条件性豁免；但 §117.5(b) 没有 part 113〔§ 117.5(d)(2)〕那样的『仅限微生物危害』限缩款——既不得把 part 113 口径搬来低估豁免，也不得因无限缩就推成整厂免检，边界是〔§ 123.3(k)〕的 processing 及其 (k)(2) 三项排除",
            "[§ 123.15〕〔§ 123.20〕的 `augments subpart A` 是叠加而非替代（漏 Subpart A 的 HACCP 计划/纠正措施/验证/记录/培训即漏项）；〔§ 123.16〕的 `except those subject to part 113 or 114` 只排除该条自身，Subpart A 全套义务仍适用；〔§ 123.12〕的进口商验证与 FSVP 是两套法源两套结构，deemed compliance 不覆盖 §123.12；记录期〔§ 123.9(b)(1)〕冷藏 1 年 / 冷冻-保藏-货架稳定 2 年，与 Part 113 的 1+2 年、Part 114 的整段 3 年是三套口径不可串用",
            "FSVP 与 Part 117 Subpart G 供应链程序是两套法源、两类主体：FD&C Act §805 / 21 CFR part 1 subpart L 管进口商 FSVPI，FD&C Act §418 / 21 CFR part 117 Subpart G 管接收设施 receiving facility；CP 7303.878 PART II.3.A 的 deemed compliance 只覆盖前者对进口食品的义务，且原文 `except they must comply with section 1.509`——UFI/DUNS 每一 entry line 电子申报不因此免除。不是 receiving facility 的纯贸易进口商没有该通道",
            "CP 7303.878 是检查员内部作业指导，PART III.1.C 明写 `Samples will not be collected as part of an FSVP inspection.`、PART IV 四节 Intentionally Left Blank；FSVP 检查查的是 FSVP/危害分析/供应商批准评价/验证活动/§1.509/纠正措施记录，不得套 CP 7303.050 的样品量与环境拭子，也不得从 CP 反推 21 CFR part 1 subpart L 条文",
            "Import Alert 99-41（FSVP 不合规进口商）与 CP 7303.070 的 99-37/99-38（LACF/AF 备案与过程控制）不是同一个 Alert：99-41 按『具体食品 + 具体境外供应商组合』或全部食品列入 Red List，未列组合在不受其他掺假/误标 Alert 约束时仍可进口；移除须按 99-41 指示提交证据并先于再次进口。direct reference authority 仅在有限情形授予，其余案件须经 CMS 送 Center 并取得分类一致；首次违法不默认优先执法；§1.507 disclosure 不能替代 §801(b)/§1.95 整改提案资料",
            "海产品危害分析判定链以『无控制条件』为闸门：指南要求 The likelihood of a hazard occurring should be judged in the absence of controls——已有控制有效恰恰可能证明该危害 reasonably likely to occur 且控制须纳入 HACCP 计划；把『没出过事』当成『不显著』会跳过整条 CCP 链",
            "Ch.3 的 Table 3-2 / 3-3 / 3-4 只列潜在危害且明文不得单独使用，必须叠加 Ch.4–21 的 Understand the Potential Hazard 与自身/外部专家判断；Worksheet 第 3 栏 Yes/No **都**要在第 4 栏写理由，第 3 栏 No 可跳过 Steps 11–18、第 6 栏 No 可跳过 Steps 12–18；显著≠必须在该步控制，CCP 由 Step 11 判定树另定",
            "第十五来源 FDA 海产品危害与控制指南是**非约束性技术指南层**：should 仅为建议、可另选控制策略与关键限值但须科学论证充分性；Appendix 5 的 50/500 ppm 等数值回指 CPG / CFR / NSSP 外部法源（转引未收），不是新设法定限值；它与 CAP-22 的 Part 123 `shall` 法定义务配对，既不得把指南当法规，也不得因指南非强制把法条义务稀释成可选",
            "第十六来源 CP 7303.842 是**给 field staff 的内部作业指导层**：不创设企业义务、不是法规也不是 Guidance for Industry。全包效力栈为法规正文〔§ 117/113/114/123.xxx〕＞ FDA 指南（should 建议层）＞ CPGM / CP / IOM 检查程序（检查员视角）。既不把 CP 的检查动作、Table 1/2 优先级、PART IV 触发值写成企业义务或放行标准，也不因 CP 非强制把 Part 123 的 `shall` 义务稀释成可选",
            "检查判定链按『Table 1 选产品/工艺风险 → Table 2 做 work planning → 六类检查分流 → HACCP Program Evaluations → Sampling 三类与 PAC 上报 → PART IV A–G 与 CPG 判据出口 → PART V Table 4 ranking（case-by-case）→ FIELD REPORTING 收口』推进；Table 4 的 Major/Minor 不是〔§ 123.6〕的 significant hazard 判定，WL / DWPE / judicial actions 也不是达到某值自动触发",
            "CP 7303.842 的两处硬口径：**合并的是程序不是码表**（7303.844 已并入，但取样/分析 PAC 仍分 03844x / 03842x，且 03842H 在取样表与报告表同名不同义，documentary samples 只报 03842）；**ATTACHMENT A 样品量只适用于 surveillance and audit**，不得用于 reconditioning、DWPE 放行或 Domestic HACCP Verification",            "LACF/AF 的「手续层」与「实体层」必须分开答：21 CFR Part 108〔§ 108.xxx〕管注册（Form FDA 2541，首次从事后 10 天内；外国加工者报检前）、工艺备案（2541e/2541d/2541f/2541g，注册后 60 天内且包装新产品前）、停业 90 天通知、腐败与偏差与污染报告、召回程序文件、BPCS 受训主管、记录保存；CAP-20 的 Part 113/114 管 scheduled process、商业无菌、偏差处置等实体要求。**紧急许可不是常态义务**——108.25(a)/108.35(a) 均为 `may be required whenever the Commissioner finds ... that the commercial processor has failed to fulfill all the requirements of this section`，未履行只构成 `prima facie basis`，不是自动生效的许可；「LACF 企业必须持紧急许可证」是错误陈述",
            "Part 108 的时限有两种「日」，混用即答错：Subpart A 程序时限全是 working days（3 个工作日提异议、5 个工作日听证、听证后 5 个工作日裁定、许可申请 10 个工作日可再延 10、恢复申请 10 个工作日、无证产品放行 20 个工作日）；Subpart B 申报时限全是日历天（注册 10 天、备案 60 天、停业通知 90 天、工艺变更报送 30 天、延期批复 30 个工作日）。记录保存四套口径不得合并：108.25(g) 整段 3 年自生产日、108.35(h) 厂内 ≥1 年 + 另 2 年、113.100(g) 1+2 且可用 part 11 电子记录、114.100(e) 整段 3 年无 part 11 条款",
            "果汁 HACCP 必须先分层再引条款：21 CFR Part 120〔§ 120.xxx〕是**独立 HACCP 体系法规**，与 Part 117〔§ 117.xxx〕的关系由〔§ 120.5〕一句话锁定——`Except as provided by § 117.5(c), parts 110 and 117 ... apply`，即 **Part 117 默认适用**、〔§ 117.5(c)〕为唯一且**条件性**的出口（该款全文未收，不得据 §120.5 反推其措辞，也不得套用 §117.5(b)/(d) 的写法）。受 Part 120 管辖只换出口不换默认；违反 §120.6/§120.7/§120.8 由〔§ 120.9〕**直接**构成 FD&C Act 402(a)(4) 掺假，不经「不符合 CGMP」中转",
            "果汁的 5-log 是法定指标，两处豁免对象不同且都极窄：〔§ 120.24(a)〕`shall ... consistently produce, at a minimum, a 5 log (i.e., 10⁵) reduction`，须覆盖 **货架期**、在**正常与中度滥用条件**下成立，目标菌为 `pertinent microorganism`（最耐热＋具公共卫生意义＋可能出现在该果汁中）。豁免 (a)(1) 是受 part 113/114 管辖者、豁免 (a)(2) 是单次热力达货架稳定或含全部配料热处理的浓缩工艺（须把热力工艺副本放进〔§ 120.7〕危害分析）——**两者免的都只是 5-log 这一指标**，另有〔§ 120.7(e)〕免的是「part 113/114 已控制的微生物与微生物毒素」危害的计划处理，不减化学/物理/过敏原危害。§120.25 的 biotype I E. coli 检测只适用果面处理者（20 mL/1,000 加仑/生产日），不是通用出厂检验",

        ],
        "out_of_scope": [
            "USDA FSIS 独家管辖的肉、禽与加工蛋制品的独立合规（作为配料时的危害分析除外）",
            "果汁 HACCP 的检查员取证口径（CP 7303.047 未收，法条义务见 CAP-26）与 NSSP Guide（海产品企业义务已由 CAP-22 覆盖〔§ 123.xxx〕正文、检查员侧程序自 v4.11 起由 CAP-24 覆盖 CP 7303.842；但 CPG / BAM / Import Alert 全文与贝类州际销售许可仍属未收）",
            "杀菌釜/无菌线工艺设计、F0 与 D/z 值计算、温度分布与热穿透研究设计、卷边解剖判读、商业无菌验证与验证方案审批，以及 2541 系列表单的栏目细则填写、FURLS / Center Views 的实际提交操作与许可申请举证材料组织（**21 CFR Part 113 / 114 法规正文自 v4.7 起已收，条款级义务清单见 CAP-20 `lacf-statutory-requirements`；21 CFR Part 108 自 v4.12 起已收，注册备案与紧急许可程序见 CAP-25 `emergency-permit-control`**；CP 7303.070 只给管辖分流与检查员取证口径）",
            "21 CFR part 1, subpart L（FSVP 法规 §§1.500-1.514）正文、Import Alert 99-41 全文、FSVP Guidance for Industry 与 FSVP Implementation Work Instructions / Inspection Protocol guidance tabs、HFP Enforcement Bulletin #13/#6、RPM 4-1-8、21 CFR part 111/112/120/507 正文（part 123 自 v4.9 起已收；CP 7303.878 只给检查员作业口径，法条义务一律标「转引未收」，不得从 CP 反推）",
            "中国 GB 14881 等非美国法规的直接合规判定（本技能只提供 FDA 方法论与条款，跨体系映射需人工判断）",
            "虫害防治、分拣筛分等质量缺陷的工程控制方案（defect-action-levels 卡只给〔§ 117.110〕义务边界与 FDA 阈值出处；霉菌类缺陷涉及真菌毒素时仍须转入危害分析）",
            "具体行政程序文书代写（豁免撤销应诉由 exemption-withdrawal-procedure 卡给出路径与时限，不代写正式法律文书）；FDA 483 回复/警告信答复/进口扣留应诉文书、检查结果预测与保证、制样与显微判读、702(b) 分割留样规则（IOM Chapter 4 / RPM / CPG 全套 / Import Alerts / eBAM-BAM-AOAC-MPM 与 BAM Ch.13B/14/17/21A/22A-22D / SOP-001052 / SOP-001642 / FMD-147 未收；CP 7303.050、CP 7303.070 与 IOM Chapter 5 正文已收，给的是抽样量、检查程序与管辖分流，不是实验室方法，也不替代 part 108 的备案条文；113/114 条款级义务见 CAP-20）",
        ],
        "stop_conditions": [
            "指南为草案（Draft – Not for Implementation）且 6 个章节未发布（Ch7/8/9/10/13/17）：涉及这些主题时明确说明来源缺口，不要编造细节；注意法规正文对这些主题仍有效，可优先引条款",
            "数值界限（6D 表、a_w、pH、冷却协议）必须注明出处小节并提示'文献极端值，未必适用于具体产品'；禁止凭记忆给数值",
            "条款引用必须核对原文：六套法规正文分别以〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕标注，PCHF 指南引用以 Ch/小节号标注，L.mono 专项指南引用以该指南章节号（如 IX.A.2、XIII.D.4）标注，SECG 引用以 SECG 章号（如 SECG XIII.C）标注，Ed.5 用问答编号（如 C.8、D.13），Food Defect Levels Handbook 用「Handbook 章名 + 产品名」标注，CPGM 7303.040 用「CPGM 7303.040 PART x」（附件须带 ATTACHMENT A 前缀）标注，CP 7303.050 用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」标注（其 ATTACHMENT A Part V 与主文 PART V 同名但不同口径），IOM 用「IOM 5.x.x / IOM Exhibit 5-x」标注，CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」标注，CP 7303.878 用「CP 7303.878 PART x」标注；21 CFR part 1 subpart L / 110、§117.5(c) 逐字文本（part 123 自 v4.9 起已收、part 108 自 v4.12 起已收、part 120 自 v4.13 起已收）、IOM Chapter 4、BAM、CPG、Import Alert 等未收正文一律标「转引未收」；**十八类不可混引**，且 §114.5 并列 `parts 110 and 117` 不得改写或判为笔误",
            "用户任务超出 26 张能力卡路由范围时，明确告知超出本包覆盖，不要硬套；LACF/AF 的实体工艺法条义务先转 CAP-20，注册备案与紧急许可程序转 CAP-25，果汁 HACCP 转 CAP-26，检查员侧取证转 CAP-19",
            "李斯特菌专项指南的附录 4/5/6（例行清洁消毒时间表、环境采样制备方法、纠正措施表）正文未纳入本次蒸馏，涉及具体表格模板时须回原始 PDF 取，不要编造",
            "cGMP 内审结论不得只凭 SECG 白话转述签发：Handbook、CPGM 7303.040、CP 7303.050、CP 7303.070 与 IOM Chapter 5 正文虽已收（CAP-15 / CAP-16 / CAP-17 / CAP-19 / CAP-18），但依次给的是缺陷行动水平阈值出处、检查类型与分级口径、检查员抽样量与阳性升级路径、LACF/AF 管辖分流与专门体系取证口径、调查员权限与证据规则，都不是实验室方法或企业内控标准。仍未收：IOM Chapter 3/4/6/7/8/9/10（尤其 Ch.4 的 702(b) 分割留样与制样、Sample Schedule Chart 2）、RPM、FMD-86、FMD-147 / SOP-001052 / SOP-000529 / SOP-001642、CPG 全套（含 Sec. 527.300、Sec. 130.100、Sec. 520.200/520.300）、Import Alerts / Import Bulletins 与 Import Alert 99-37/99-38 正文、其他 Compliance Programs（7303.080 / 7371.000 / 7321.006 / 7304.019 / 7304.004A / 7309.006 等）、eBAM / BAM / AOAC / MPM 方法正文、21 CFR part 108 / 110 / 120（Part 113 / 114 正文自 v4.7 起已收、Part 123 自 v4.9 起已收）与 21 CFR 2.10 / 133 / 1240.61 / 507 正文、Form FDA 484 / 1551 表单细则、21 CFR part 117 citations table、SOFO job aid 与 eNSpect / CAR / CMS 内部系统。制样与显微判读、检验方法检出限、杀菌工艺计算、证据充分性标准与警告信判定阈值须另行复核",
            "CP 7303.050 现行文件是 2022-06-03 签发 / IMPLEMENTATION DATE 06/03/2022 / Correction date 09/10/2025 的更正本（62 页），不是 2025 年新签发 program；文件名 20250915 与美国律所快讯里的「2025 DIMS 抽样计划」不得当作版本依据。它不安排检查（Inspections are not planned under this compliance program）；Table 2/3 的 subs 数是 FDA 取证量而不是企业放行标准，PART V 表 7/8 是逐案、非穷尽的可能响应清单而不是法定后果表。IOM 只收了 2026 版 Chapter 5 单章，遇文中 IOM 3.2 / 4.x / 6.4 / 8.1 等跨章引用一律标注「转引未收」，不得代填",
            "预告与无预告都不得写成绝对规则：IOM 5.2.7 的原文口径是食品企业检查一般不预告（由 program division 裁量）、境外检查通常提前告知、医疗器械 surveillance 与部分 BIMO 强制预告、国内预告一般不少于 5 个日历日且改期不晚于原日期 +5 天、预告不是预约。2025 年 FDA 扩大境外无预告检查、RRA 适用范围与 FD&C Act 704(a)(4) 检查前索取记录属政策层且 FDA 公告原文未收，只作准备原则提示，不得写成条款级结论；CP 7303.070 PART II.2.B(2) 已给出 RRA 的**程序性定义**（自愿、全程远程、RRAs are not considered inspections、不满足 510(h)/503B(b) 等 704 条法定检查场景），可以据此回答「RRA 算不算现场检查」，但**不得**据此推导 FDA 的 RRA 适用政策、扩大范围或取代 IOM 5.2.7 的预告口径；CPGM 7303.040 PART V.1 明说 OCIC/DCC 咨询流程暂不适用于 foreign inspection case routing",
            "过敏原标签问答 Ed.5 的内容不得标注为〔117.xxx〕；引用须用 Ed.5 问答编号（如 C.8、D.13），并说明其属 FD&C Act 标签解释而非 Part 117 预防控制义务。遇旧口径（Ed.4 把椰子列为树坚果、2022 版 Ed.5 或二手摘要）须提示版本已被 2025-01 修订终版替代并回 Table 1 复核",
            "CPGM 7303.040 现行版为 2025-CPM-HFP-001（签发 08/29/2025，IMPLEMENTATION DATE 05/23/2024），2020-CPGM-CFSAN-003 已废止；遇 2020–2024 迎检 SOP、律所快讯、或 FDA 网页 Food Compliance Programs 列表日期，一律以 PDF 首页 Transmittal / Date of Issuance / IMPLEMENTATION DATE 为准",
            "CP 7303.070 现行文件是 2024-09-26 签发 / IMPLEMENTATION DATE 9/26/2024 / Correction Date 9/26/2025 的更正本（61 页），文件名 20250929 只是 PDF 生成日，不是 2025 年新签发 program，也不得套用 7303.040 的 2025-CPM-HFP-001 Transmittal 格式。它依据的 **21 CFR part 113 / 114 法规正文自 v4.7 起已收**（见 CAP-20，涉及 scheduled process、商业无菌、BPCS、成品 pH、偏差与记录保存按〔§ 113.xxx〕〔§ 114.xxx〕引用）；**仍未收** part 110（part 123 自 v4.9 起已收，见 CAP-22；part 108 自 v4.12 起已收，见 CAP-25；part 120 自 v4.13 起已收，见 CAP-26）、IOM Ch.4 Sample Schedule Chart 2、BAM 各章、CPG Sec. 520.200/520.300、Import Alert 99-37/99-38 全文、Form 2541e 细则：这些内容一律标「转引未收」，F0/D/z 计算与卷边解剖判读仍不得从 CP 反推",
            "LACF/AF 的管辖判定三禁：① 禁止把〔§ 117.5(d)〕的 Subparts C/G 豁免扩到酸化食品（part 114）或扩到化学/物理/金葡等未被热处理控制的危害；② 禁止把〔§ 117.201〕（qualified facility 的 modified requirements）当作 LACF 条款；③ 禁止把 CP 7303.070 的 4.40/4.65/4.75、aw 0.90/0.93、异常罐 1%、24 罐/12 罐、3 个月/6 个月/12 个月写成企业法定义务或放行标准。酸化食品是否属 AF 由 HFP 依「Maximum Equilibrium pH」判定三步给结论，不得由本包替企业下法定身份结论；Import Alert/DWPE 不得仅因未注册/未备案建议",
            "海产品管辖判定三禁：① 禁止把〔§ 117.5(b)〕的豁免套用 part 113〔§ 117.5(d)(2)〕的『仅限微生物危害』限缩——part 123 无该限缩款，两向误读都会错；② 禁止因『§117.5(b) 无限缩』就推成整厂免 Subparts C/G——边界是受 part 123 管辖的 activities，〔§ 123.3(k)(2)〕三项排除（纯捕捞或运输、船上暂存处理、零售）不在内，且豁免不含 Part 117 Subpart B 的 CGMP；③ 禁止把〔§ 123.16〕的 `except those subject to part 113 or 114` 读成『属 LACF/AF 就免 part 123』——排除的只是该条，Subpart A 全套仍适用",
            "Part 123 记录期不得写成统一 3 年：〔§ 123.9(b)(1)〕按产品类型分冷藏 1 年 / 冷冻-保藏-货架稳定 2 年，(b)(2) 适宜性记录 2 年且起算点是其对产品的适用性；与〔§ 113.100(g)〕的 1+2 分段、〔§ 114.100(e)〕的整段 3 年是三套口径。另 21 CFR part 1240 / 110 / 507 正文与 NSSP Guide 仍未收（part 108 自 v4.12 起、part 120 自 v4.13 起已收，见 CAP-25 / CAP-26）；CP 7303.842 自 v4.11 起已收（见 CAP-24），凡涉检查员取证量、贝类生长区分类一律标『转引未收』；FDA 海产品危害与控制指南自 v4.10 起已收（见 CAP-23），其建议参数与限值回指的外部法源仍须标『转引未收』，不得从 Part 123 反推",
            "LACF/AF 记录保存口径不得串用：〔§ 113.100(g)〕是厂内 ≥1 年 + 加工厂或其他合理可及地点再 2 年（合计 3 年，季节包停产可提前转移），〔§ 113.100(h)〕另许符合 part 11 的电子记录；〔§ 114.100(e)〕只有「加工厂或其他合理可及地点自生产日起 3 年」一句，**没有分段、没有 (h) 款、没有 part 11 电子记录条款**（Part 114 全文无 electronic / part 11 字样）。回答「两 part 记录怎么存」必须分列，不得合并成一条",
            "涉及 21 CFR part 110 时不得沿用 v4.3 的旧结论：Part 110 未被删除（FDA 2018-09-12 FR Doc. 2018-19855 撤回 amendatory instruction 13），至今有效但正文本包未收，须标「转引未收」；手册那句是 §110.110(c) 意译，仍不得标成〔§ 117.110(c)〕。2018-19855 正文属外部核实、本包未收，引用须注明是 Federal Register 规则而非本包来源",
            "CP 7303.878 的版本口径锁定 2023-09-27 版 / 2025-08-28 更正（Transmittal 2023-CPM-CFSAN-003，Change History 的 2025 条目只改 POC 与机构名称缩写），不得写成「2025 版 7303.878」或套用 CPGM 7303.040 的 2025-CPM-HFP-001 Transmittal 形态；CP 7303.819 是 2006 FY06-08 旧程序、已过 COMPLETION DATE 9/30/08 而非现行，准确说法不是「法规意义上废止」。FSVP 法规条文、Import Alert 99-41 全文、FSVP Guidance Q&A、IP guidance tabs 一律标「转引未收」",
            "回答 FSVP 问题时不得把 CP 7303.878 的 483a 观察分级、NAI/VAI/OAI、WL / Import Alert 99-41 建议流程写成企业法定义务或必然法律后果；不得把 §117.5(d)（part 113 活动的 Subparts C/G 豁免）套到 FSVP 轨道；不得把 Import Alert 99-41 与 99-37 / 99-38 混引",
            "Seafood Hazards Guide 第 4 版的引用须写「Ch.x / Appendix x / L####」，不得写成〔§ 123.xxx〕；法条义务一律回 CAP-22。导出件表格列头连写、词条粘连、`fsh`/`Pufer` 字符丢失、页码混入单元格、Appendix 3 的 CCP 判定树塌陷成残表——**逐字引用只能取散文段落**，判定树仅可复原逻辑，须回查 PDF 原版。封面 June 2022 但多章页脚 June 2021 属分章滚动修订，不得写成 2022 新规",
            "回答海产品危害分析问题时不得把 Ch.3 勾选表、控制策略示例的关键限值、Appendix 5 的 50/500 ppm 或寄生虫冻结三条件写成法定限值或合规清单；也不得因指南非强制就免除〔§ 123.6〕的危害分析与书面 HACCP 计划义务。NSSP Guide、21 CFR part 1240 / 110 / 507、Import Alert 16-xx、BAM 海产品章节、CPG Sec. 540.525 / 555.300 / 575.100 与 Appendix 5 回指的外部法源一律标「转引未收」；CP 7303.842 自 v4.11 起已收（见 CAP-24）；全包自 v4.13 起**十八类不可混引**，当前为 26 张能力卡",
            "回答 CP 7303.842 相关问题时不得把 Table 1/2 优先级、PART IV 的 500/50/35 ppm 与 15/25 µg/100g、48 subs、pH 4.6、98% RSSL 等检查员触发值写成法规限值、产品放行标准或 BAM 方法全文；Table 4 的 Major/Minor 只作 case-by-case ranking，不是〔§ 123.6〕的 significant hazard 判定；WL / DWPE / judicial actions 须 HFP OCE concurrence 而非自动触发。CPG 540.525 / 540.370 / 562.300 / 555.600、21 CFR part 1240 / 110 / 507、NSSP Guide、BAM / AOAC / MPM、Import Alert 16-xx 与 99-41 全文、21 CFR part 1 subpart L、IOM Ch.4、FDA 3501/3502 表单全文一律标「转引未收」；引用写「CP 7303.842 PART x / Table x / ATTACHMENT A #x / Lxxx」，不得与〔§ 123.xxx〕或 Seafood Hazards Guide Ch.x 混引",
            "CP 7303.842 的版本口径锁定 2023-11-01 版 / 2025-09-30 更正，文件名 20250929 只是 PDF 生成日，封面 Date of Issuance 09/30/025 为文本层残缺，正文页脚 11/1/2023；与 CP 7303.050 / 7303.070 / 7303.878 同属旧程序更正本，不得套 CPGM 7303.040 的 2025-CPM-HFP-001 Transmittal 形态。转换件书签标题与正文伪标题交错（PART 各出现两次、H1 虚高 133），检索以 PART / 小节 / 表号为准，表格、页码、页眉不可逐字引用；凡法条义务转 CAP-22、危害技术判定转 CAP-23、FSVP 转 CAP-21、通用取样转 CAP-17",            "回答 LACF／酸化食品的许可问题不得把紧急许可写成常态义务：108.25(a)／108.35(a) 的 `may be required` 触发前提是未履行注册、备案、报告、召回程序、BPCS 主管与记录义务，且只构成 `prima facie basis`；不得把 Subpart A 的 working days（3/5/10/20）套到 Subpart B 的日历天（10/30/60/90）上；不得把 108.25(g) 的整段 3 年与 108.35(h) 的 1+2 年、113.100(g) 的 1+2 年、114.100(e) 的整段 3 年合并成「3 年」一句；不得把外国加工者的 §801 拒绝入境路径（108.25(j)／108.35(k)）与国内企业的紧急许可路径混答；不得把 108.35 独有的 FSIS 连续检验豁免 (i)、加州视为合规 (j)(2)、FOIA 豁免 (l) 套到酸化食品上",
            "Part 108 的引用写「〔§ 108.xxx〕」并与〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕并列，不得混编号；108.25(a) 的 `§§ 114.10, 114.80(a) (1) and (2), and (b), 114.83, 114.89, and 114.100 (b), (c), and (d)` 不得简写成「§§ 114.10–114.100」（印刷版括号内空格是原文形态，简写即失去逐字性）；备案 `Filing of this information does not constitute approval` 不得读成「等 FDA 批准才能生产」；108.35(c)(2)(ii) 的「升参数不算变更」与 (c)(2)(iii) 的「operating process 不算修改」不得反推为「任何工艺调整都无需报告」——降初温／降杀菌温度／缩短时间／改配方仍须事前证实 + 30 天内报送",
            "回答果汁 HACCP 问题不得把 5-log 降格为建议层（〔§ 120.24(a)〕是 shall，且须持续、覆盖货架期、正常与中度滥用条件）；不得把目标菌答成沙门氏菌或大肠杆菌 O157（应为 pertinent microorganism，三条件同时成立）；不得把〔§ 120.25〕的 biotype I E. coli 检测写成所有果汁厂的强制出厂检验（仅果面处理者适用），也不得把果面处理厂的检测写成可选；不得据〔§ 120.5〕反推〔§ 117.5(c)〕的条文措辞；不得把两处豁免合并成「受 113/114 管辖就不用做果汁 HACCP」；不得把记录复审写成 7 个工作日（果汁是 1 week / 7 日历天）；不得把果汁记录期套成 3 年或统一 2 年（易腐/冷藏 ≥1 年、冷冻/保藏/货架稳定 2 年或货架期孰长，起算点产品制备日）；不得把〔§ 120.14〕与 FSVP 互相替代",
            "果汁 HACCP 的引用写「〔§ 120.xxx〕」并与〔§ 108.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 117.xxx〕〔§ 123.xxx〕并列，六套编号互不混引；`5 log (i.e., 105)` 的 `105` 是 PDF 文本层上标丢失，逐字引用须还原为 10⁵ 并注明是文本层缺陷，不得照抄成「105 倍」；〔§ 117.5(c)〕逐字文本、part 110 正文、CP 7303.047 果汁 program、CPG 与 Import Alert 全文、BAM/AOAC 方法全文一律标「转引未收」；〔§ 120.24(a)(2)〕的豁免以「热力工艺副本已纳入书面危害分析」为条件，答豁免时不得省略该条件",

        ],
    },
    "router_entry": {
        "name": "fda-pchf-food-safety",
        "description": "同 single 入口（本 bundle 采用 single 输出，无独立晋级 Skill）。",
    },
    "promotion_budget": 8,
    "capabilities": capabilities,
}

(CAPS_DIR / "verified.yaml").write_text(
    yaml.safe_dump(bundle, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")

dump = {"bundle_id": bundle["bundle_id"],
        "destinations": {c["capability_id"]: {"served_by": "fda-pchf-food-safety"} for c in capabilities}}
(CAPS_DIR / "destinations.json").write_text(json.dumps(dump, ensure_ascii=False, indent=2), encoding="utf-8")

# book/ 层：overview + glossary
(CAPS_DIR / "book").mkdir(exist_ok=True)
shutil.copyfile(BASE / "BOOK_OVERVIEW.md", CAPS_DIR / "book/overview.md")
shutil.copyfile(BASE / "candidates/glossary.md", CAPS_DIR / "book/glossary.md")
shutil.copyfile(BASE / "candidates/glossary.md", BASE / "GLOSSARY.md")

print(f"bundle ok: {len(capabilities)} capabilities")
for c in capabilities:
    n = len(json.dumps(c, ensure_ascii=False))
    print(f"  {c['capability_id']} {c['slug']} importance={c['importance']} also_read={len(c['also_read'])}")
