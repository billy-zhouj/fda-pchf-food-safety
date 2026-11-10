#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""append_v4_11.py — 追加第十六来源的 10 条术语（t183–t192）与 10 条评测用例。

沿用 v4.10 append_v4_10.py 模式：内存暂存 → 唯一性断言 → 备份 → 末尾一次性落盘。
"""
import json
import re
import shutil
import yaml
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
GL = BASE / "candidates/glossary.md"
TP = BASE / "test-prompts.json"
DRAFT = BASE / "candidates/v4-11-glossary.md"
BACKUP = BASE / ".cangjie/backup-v4-11-pre-append"

TERMS = """- id: t183
  title: CP 7303.842 的版本判定与 CP 7303.844 合并口径
  summary: >-
    FDA《Compliance Program Guidance Manual 7303.842》封面写 IMPLEMENTATION DATE 11/01/2023、
    Correction date 09/30/2025、Date of Issuance 09/30/025（PDF 文本层残缺），正文页脚一律
    11/1/2023，PDF creationDate 2025-09-29。故文件名 20250929 只是**生成日**，本件是
    **2023-11-01 版程序的 2025-09-30 更正本**，不是 2025 新签发 program；与 CP 7303.050 /
    7303.070 / 7303.878 同属「旧程序 + 更正本」形态，不同于 CPGM 7303.040 的 2025-CPM-HFP-001
    新 Transmittal。首页 NOTE 与 PART I 写明 CP 7303.842（Seafood Processor Inspection Program）
    与 CP 7303.844（Imported Seafood Inspection Program）**已合并为单一程序**，但 PAC codes for
    sampling and analysis 仍区分进口与国产 —— 合并的是程序，不是码表。
  tags: [CP 7303.842, 版本判定, 更正本, CP 7303.844, 程序合并, 十六类不可混引]

- id: t184
  title: 检查程序作业层的效力边界（非法规、非 Guidance for Industry、不创设义务）
  summary: >-
    CP 7303.842 是 FDA 给检查员、进口分区、分部合规官与实验室的**内部作业指导**
    （PART I/II 明写 provides instruction to field staff），覆盖检查优先级、检查实施、取样、
    实验室分析分流、执法建议与报告上报。它不是法规、不是 Guidance for Industry，也不创设企业义务；
    企业义务仍回 21 CFR Part 123〔§ 123.xxx〕与 Part 117 Subparts A/B/F。CP 原文 L276 明写
    Part 117 subparts C/G 不能替代 Part 123 的法定义务。**双向误读都要防**：既不能把 CP 的检查动作
    写成企业义务，也不能因 CP 非强制把 Part 123 的 shall 义务稀释成可选。
  tags: [检查程序作业层, 内部作业指导, field staff, 不创设企业义务, 法条义务层, 三层配对]

- id: t185
  title: Table 1 与 Table 2 的分工、90/10 与 100 entry line items
  summary: >-
    Table 1（Product and Process Priority Ranking）按产品/工艺危害与行业合规情况**降序**排
    commodities，用于确定 HACCP 检查焦点；原文 Table 1 is not all inclusive，表外产品/工艺须查
    Hazards Guide 第 3 章，产品跨多类取**最高风险类别**，取样风险判定也用 Table 1。Table 2
    （Priorities for Establishment and Importer Inspections）**仅用于 work planning**，在 Table 1
    基础上按企业/进口商个体合规史降序；进口商检查数量由 OII workplan 定，**90%** 给高风险进口商、
    **10%** 给年进口 <100 entry line items 者；OAI 复检须待整改完成。两者不可对调。
  tags: [Table 1, Table 2, work planning, 90/10, 100 entry line items, OII Workplan, 检查优先级]

- id: t186
  title: 六类检查分流与各自的专门限制
  summary: >-
    PART III 分流：① Processor（多程序适用时分别覆盖、时间有限优先 03842H）；② Importer
    （〔§ 123.12〕验证、Table 2 选人 / Table 1 选产品、食品安全 MOU 国家产品排除、书面验证程序与
    affirmative steps、每产品一份 FD 3502；**境外加工商 HACCP 计划的其他缺陷不得写进 483**，须取
    副本转 HFP）；③ Vessels（通常靠港且非作业时检查）；④ Foreign Establishments（产品风险 + 合规史
    选点、只覆盖输美产品、须取文档与照片证据）；⑤ NSSP（须 shellfish standardized inspector /
    officer，用 ISSC Form 93-01(A)、依 NSSP Model Ordinance）；⑥ EMA / Food Fraud（一般监督须先得
    HFP concurrence，比对采购订单/原料标签/成品标签）。
  tags: [Processor Inspections, Importer Inspections, Vessels, Foreign Establishments, NSSP, EMA, 检查分流]

- id: t187
  title: PAC 双码表、03842H 同名不同义与 documentary samples 硬约束
  summary: >-
    取样/分析 PAC 进口 03844x / 04844A / 07844 / 09844x / 21844、国产 03842x / 04842A / 07842 /
    09842x / 21842；检查报告 PAC 另有 03842（documentary / 非 HACCP 评估）、03842H（Processor
    HACCP Inspection）、03844H（Importer HACCP Inspection）、03040（PC training）。⚠ **03842H
    在取样表是 HACCP Verification（验证 HACCP 计划关键限值充分性）且进口列 Not applicable，在报告表
    却是 Processor HACCP Inspection —— 同名不同义**。所有 documentary samples **只报 PAC 03842**，
    不得用以 H 结尾的 HACCP 验证 PAC，也不计入 Division Workplan 义务。
  tags: [PAC, 03842H, 03844H, documentary samples, HACCP Verification, 双码表, 报告归属]

- id: t188
  title: Sampling 三类与「不取样」同样是结论
  summary: >-
    ① 国产官方样品 Domestic official samples are to be collected "for cause" only；不必常规采国产样
    支持 HACCP 违规的监管行动，控制明显不足时**不取样**而在 483 说明控制缺失、EIR 描述条件，确需取样
    须先联系 HFP。② 进口监督取样数量由 OII Workplan 定、既往有安全缺陷的国外加工商/发货人条目优先、
    多数样品取自高风险产品。③ Documentary samples 见 t187。ATTACHMENT A 的 702(b) duplicate 部分
    不含在表列 subs 内、Filth 仅 for cause、CFP 只在疾病/暴发响应时采、RTE 才做 Listeria。
  tags: [Sampling, for cause only, Imported Surveillance, Documentary Samples, ATTACHMENT A, 不取样]

- id: t189
  title: PART IV 阈值是检查员作业口径，不是法规限值或放行标准
  summary: >-
    组胺 500 / 50 / 35 ppm、Indole 15 / 25 µg per 100 g、感官 subs 18 / 24 / 12 / 18、活虫零容忍、
    pH <4.6（腌渍品追加分析结束条件）、熏鱼 nitrite 100 ppm、RSSL ≥98% / <98%、净重过镀冰 48 subs、
    未去脏鱼 5 inches、Filth 6 个 2–3 lb subs —— 全部是 CP 的**追加分析 / 取样量 / 上报触发口径**，
    不是法规限值、不是产品合格判定标准、不是 BAM / AOAC 方法全文。判据出口是 CPG Sec. 540.525 /
    540.370 / 562.300 / 555.600 / 540.250 与 Hazards Guide 第 6 章 action levels（本包多为未收）；
    subs 数多处明说 only for surveillance and audit samples，reconditioning / DWPE 放行 /
    Domestic HACCP Verification 各有不同规则。
  tags: [PART IV, Criteria for Regulatory Action, 检查员触发值, CPG 540.525, 非法规限值, 转引未收]

- id: t190
  title: Table 4 是 ranking 工具，与 §123.6 显著性判定、自动执法结论分离
  summary: >-
    PART V 的 Table 4（Seafood HACCP Enforcement Strategy: Ranking of violation）逐条给
    Deficiency → Citation(123.x) → Major/Minor 映射，但原文 Significance must be determined on a
    case-by-case basis。Major/Minor 定义针对 HACCP 系统完整性与食品安全风险，**不是**〔§ 123.6〕
    hazard analysis 的 reasonably likely to occur / significant hazard 判定，也不是自动执法结论；
    记录伪造归 Title 18 / OCI 不在表内分级；非 123 违规（misbranding / EMA / 非鲭毒分解 /
    非安全 GMP）另走 Compliance Intake and Consultation Form。
  tags: [Table 4, Major Minor, case-by-case, 违规分级, 123.6 显著性, 非自动执法]

- id: t191
  title: 执法裁量、Center concurrence 与物种误标的法律定性
  summary: >-
    Warning Letters 原文 should be considered；DWPE 针对国外检查/记录审查偏差未纠正的境外加工商，
    放行或移出 import alert 须 HFP OCE concurrence 与英文证据；judicial actions 建议须 HFP OCE
    评估同意、FACTS 入案、CMS 电子提交；NMFS 通知依 FDA–NMFS MOU / FMD#-029。Species misbranding
    的定性是 **FD&C Act 403(b) / 21 U.S.C. 343(b)**，监管建议经 MARCS-CMS；物种替换可能**引入**
    海洋毒素/过敏原/鲭毒等额外安全危害，此时才转 CAP-23 做危害分析 —— 法律定性与危害判定分离。
    Import Alert 16-74 / 16-20 与 99-41 / 99-37 / 99-38 不是同一组。
  tags: [Warning Letters, DWPE, HFP OCE, judicial actions, 403(b), Species Misbranding, Import Alert 16-74]

- id: t192
  title: 十六类不可混引、引用规范、仍未收清单与转换质量红线
  summary: >-
    自 v4.11 起全包 **十六类来源不可混引**。CP 7303.842 引用写「CP 7303.842 PART x / Table x /
    ATTACHMENT A #x / Lxxx」；法条写〔§ 123.xxx〕〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕；指南写
    「Seafood Hazards Guide 第 4 版 Ch.x」；其它 CP / IOM / Handbook / SECG / Ed.5 各用其自身编号。
    仍未收：CPG 540.525 / 540.370 / 555.600 / 562.300 / 540.250 / 540.590 全文、21 CFR part 120 /
    1240 / 108 / 110 / 507、NSSP Guide、BAM / AOAC / MPM 方法全文、Import Alert 16-xx / 99-41 全文、
    21 CFR part 1 subpart L、IOM Ch.4、FDA 3501 / 3502 表单全文、eNSpect / CMS / FACTS 内部系统。
    转换件存在书签标题与正文伪标题交错（PART 各出现两次、H1 虚高 133）、`<u>` / `<br>` 标签、
    表格列头连写与页码混入，**检索以 PART / 小节 / 表号为准**，逐字引用只取散文段落且须剥离标记。
  tags: [十六类不可混引, 引用规范, 转引未收, 转换质量红线, 标题层级交错, v4.11]
"""

CASES = [
    {
        "id": "seafood-inspection-01",
        "type": "should_trigger",
        "prompt": "我手上这份 FDA 文件名叫 20250929_CP 7303.842 ... 508-Compliant.pdf，首页还写 Date of Issuance 09/30/025，请问这是 2025 年新发布的海产品检查程序吗？和 CPGM 7303.040 的 2025-CPM-HFP-001 是同一种版本形态吗？",
        "expected_behavior": "应激活 seafood-inspection-program 卡：明确文件名 20250929 只是 PDF 生成日（creationDate 2025-09-29），本件是 IMPLEMENTATION DATE 11/01/2023 的 2023 版程序 + Correction date 09/30/2025 的更正本，不是 2025 新签发 program；与 CP 7303.050 / 7303.070 / 7303.878 同属旧程序更正本形态，不同于 CPGM 7303.040 的新 Transmittal 2025-CPM-HFP-001。并说明 Date of Issuance 09/30/025 是文本层残缺、正文页脚为 11/1/2023，引用 issuance 日期须注明出处。",
        "notes": "v4.11：版本判定与文件名陷阱",
    },
    {
        "id": "seafood-inspection-02",
        "type": "should_trigger",
        "prompt": "CP 7303.842 和 CP 7303.844 现在合并了吗？合并后进口和国产样品是不是都报同一个 PAC 码？",
        "expected_behavior": "应激活 seafood-inspection-program 卡：首页 NOTE 与 PART I 写明两程序已合并为单一 CP 7303.842（Seafood Processor and Products Inspection Program），但 PAC codes for sampling and analysis 仍区分进口 03844x / 国产 03842x；并区分取样/分析 PAC 与检查报告 PAC 两套码表（03842 / 03842H / 03844H / 03040），提示 03842H 同名不同义。不得回答为「码表已统一」。",
        "notes": "v4.11：程序合并 ≠ PAC 码合并",
    },
    {
        "id": "seafood-inspection-03",
        "type": "should_trigger",
        "prompt": "我们厂做减氧包装的熏制水产品和普通冷冻鱼，FDA 来检查时会先看哪张表排优先级？进口商检查数量怎么定？",
        "expected_behavior": "应激活 seafood-inspection-program 卡：Table 1 按产品/工艺风险降序（ROP / C. botulinum 属 HIGHER RISK POTENTIAL），用于确定 HACCP 检查焦点与取样风险，且 not all inclusive、跨类取最高风险类别、表外查 Hazards Guide 第 3 章；Table 2 仅用于 work planning 按企业/进口商合规史排序，进口商数量由 OII workplan 定并受 90% / 10% 与 <100 entry line items 约束。两块不可对调，也不得把优先级表写成企业合规清单。",
        "notes": "v4.11：Table 1 / Table 2 分工",
    },
    {
        "id": "seafood-inspection-04",
        "type": "should_trigger",
        "prompt": "海产品 HACCP 检查有哪些类型？加工船、境外加工商、NSSP 贝类企业和进口商各有什么特别要求？",
        "expected_behavior": "应激活 seafood-inspection-program 卡：给出 PART III 六类分流；至少写明 HACCP Program Evaluations 聚焦最高风险产品且在企业已知在生产时进行、Part 117 C/G 不能替代 Part 123、Vessels 通常靠港非作业检查、Foreign Establishments 只覆盖输美产品且选点看产品风险 + 合规史、NSSP 须 standardized inspector 与 ISSC Form 93-01(A)、Importer 依〔§ 123.12〕且境外加工商 HACCP 计划缺陷不得上 483 而转 HFP。条款级义务须转 CAP-22。",
        "notes": "v4.11：六类检查分流",
    },
    {
        "id": "seafood-inspection-05",
        "type": "should_trigger",
        "prompt": "国内海产品厂的常规 HACCP 检查，是不是每次都要取官方样品送检？取样量按 ATTACHMENT A 的 Table A-1 就行了吗？",
        "expected_behavior": "应激活 seafood-inspection-program 卡：国产官方样品仅 for cause，不必常规采国产样支持 HACCP 违规监管行动；控制明显不足时不取样而在 483 说明控制缺失、EIR 描述条件，确需取样须先联系 HFP。ATTACHMENT A 的 subs 数仅适用于 surveillance and audit samples，不能用于 reconditioning 验证、DWPE 放行或 Domestic HACCP Verification，702(b) duplicate 也不含在表列 subs 内。",
        "notes": "v4.11：for cause only 与取样量适用域",
    },
    {
        "id": "seafood-inspection-06",
        "type": "should_trigger",
        "prompt": "为支持州际贸易开了一份 documentary sample，PAC 该报 03842H 还是 03842？算不算 Division Workplan 的取样任务？",
        "expected_behavior": "应激活 seafood-inspection-program 卡：documentary samples 只报 PAC 03842，不得使用以 H 结尾的 HACCP 验证 PAC，也不计入 Division Workplan 义务；并说明 03842H 在取样表是 HACCP Verification（进口列 Not applicable）、在报告表是 Processor HACCP Inspection 的同名不同义。",
        "notes": "v4.11：documentary samples 硬约束",
    },
    {
        "id": "seafood-inspection-07",
        "type": "should_trigger",
        "prompt": "CP 7303.842 里写组胺 500 ppm / 50 ppm / 35 ppm，是不是 FDA 对金枪鱼的法定组胺限量？我们成品按 50 ppm 放行合规吗？",
        "expected_behavior": "应激活 seafood-inspection-program 卡并纠正误读：这些是 PART IV.C 对初始 6 subs 的追加分析 / check analysis 触发规则，属检查员作业口径，不是法规限值、不是产品放行标准、不是 BAM 方法全文；判据出口为 CPG Sec. 540.525（本包未收，标转引未收）。不得与 CAP-23 的 50 ppm 分解指示 / 500 ppm 毒性水平混为一谈；企业合规结论须回〔§ 123.xxx〕/ CAP-22。",
        "notes": "v4.11：阈值性质反例",
    },
    {
        "id": "seafood-inspection-08",
        "type": "should_trigger",
        "prompt": "只要 Table 4 把某条 123.6 缺陷标成 Major，是不是就自动发 Warning Letter 并列入 DWPE？这个 Major 和危害分析里的 significant hazard 是一回事吗？",
        "expected_behavior": "应激活 seafood-inspection-program 卡：Table 4 只是 ranking 工具且原文 Significance must be determined on a case-by-case basis；Major/Minor 针对 HACCP 系统完整性与食品安全风险，不是〔§ 123.6〕的 reasonably likely to occur / significant hazard 判定；Warning Letters 是 should be considered，DWPE 放行/移出须 HFP OCE concurrence，judicial actions 须 Center 评估同意并经 CMS。不得写成自动触发，也不得把表内 Citation 当成法条原文展开（转 CAP-22）。",
        "notes": "v4.11：Table 4 与执法裁量反例",
    },
    {
        "id": "seafood-inspection-09",
        "type": "should_trigger",
        "prompt": "FSVP 检查明确不取样、PART IV 全空，那海产品进口商的 HACCP 检查是不是也不取样？两套检查能互相套用吗？",
        "expected_behavior": "应激活 seafood-inspection-program 卡并分流到 fsvp-inspection-program：CP 7303.878 的 Samples will not be collected as part of an FSVP inspection / PART IV 空白只适用于 FSVP（FD&C Act §805 / 21 CFR part 1 subpart L）；本 CP 的进口商 HACCP 检查依〔§ 123.12〕，有 Imported Seafood Surveillance Sampling 与 03844H 报告 PAC。两套法源、两套动作，不得反向套用；FSVP 法规条文标转引未收。",
        "notes": "v4.11：FSVP 与 §123.12 双轨反例",
    },
    {
        "id": "seafood-inspection-10",
        "type": "should_not_trigger",
        "prompt": "按中国 GB 2733 帮我判定这批水产品的组胺限量，顺便按欧盟法规写一份海产品出口卫生证书和 FDA 检查应对承诺函。",
        "expected_behavior": "不应激活本技能给出条款级结论或代写文书：本包只覆盖 FDA 方法论与 21 CFR 条款，不做中国 GB 标准或欧盟法规的直接合规判定，也不代写官方卫生证书或承诺函（out_of_scope / stop_conditions）。应明确说明超出覆盖范围并建议咨询对应法域专业机构；若用户改问 FDA 海产品检查程序判定链，再转 seafood-inspection-program 卡。",
        "notes": "v4.11：跨法域与文书代写负例",
    },
]


def main() -> None:
    # 仓库内 glossary.md / test-prompts.json 为 CRLF；按原换行符读写，避免全文件 diff
    gl_raw = GL.read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in gl_raw else "\n"
    tp_raw = TP.read_bytes().decode("utf-8")
    nl_tp = "\r\n" if "\r\n" in tp_raw else "\n"
    gl_lines = gl_raw.split(nl)
    tp = json.loads(tp_raw)

    # 1) 术语：插到最后一个 fenced yaml 块闭合行（单独一行 ```）之前
    terms = TERMS.strip("\n")
    assert terms.count("- id: t") == 10, "术语条数应为 10"
    ids = [int(x) for x in re.findall(r"- id: t(\d+)", terms)]
    assert ids == list(range(183, 193)), f"术语 id 不连续: {ids}"
    for block in re.split(r"(?=^- id: t)", terms, flags=re.M):  # 逐条 parse，避免拼接歧义
        if block.strip():
            yaml.safe_load(block)

    close_idx = max(i for i, l in enumerate(gl_lines) if l.strip() == "```")
    gl_lines.insert(close_idx, terms.replace("\n", nl))
    gl_new = nl.join(gl_lines)
    assert gl_new.count("- id: t") == gl_raw.count("- id: t") + 10

    check_line = ("- [x] 第十六来源 **FDA CP 7303.842**（2023-11-01 版 / 2025-09-30 更正，80 物理页 / 148 书签）"
                  "检查程序已并入，术语 t183–t192 共 10 条（版本判定与 7303.844 合并、内部作业指导层效力边界、"
                  "Table 1/2 分工与 90/10、六类检查分流、PAC 双码表与 03842H 同名不同义、Sampling 三类与 "
                  "for cause only、PART IV 阈值性质与 CPG 判据出口、Table 4 ranking 与 §123.6 显著性分离、"
                  "执法裁量与 403(b) 误标定性、十六类不可混引与转换质量红线）。引文取自 CAP-24 R 段经 "
                  "`.cangjie/verify_v4_11_quotes.py` 核验的 **36 个英文引用块**（36/36 命中正文区，"
                  "0 超 100 词、0 表格引用）。原文标「CP 7303.842 PART x / Table x / ATTACHMENT A #x / Lxxx」，"
                  "法条标〔§ 123.xxx〕，指南标「Seafood Hazards Guide 第 4 版 Ch.x」，三者不可混引；"
                  "CPG / BAM / NSSP / Import Alert / part 1 subpart L 等未收正文一律标『转引未收』。"
                  "全库 **192 条**，v4.11，**十六类来源不可混引**。")
    gl_new = gl_new.rstrip("\r\n") + nl + nl + check_line + nl

    # 2) 用例
    assert len(CASES) == 10
    assert all(c["id"].startswith("seafood-inspection-") for c in CASES)
    existing = {c["id"] for c in tp["test_cases"]}
    assert not (existing & {c["id"] for c in CASES}), "用例 id 冲突"
    before = len(tp["test_cases"])
    tp["test_cases"].extend(CASES)
    tp["version"] = "4.11"
    assert len(tp["test_cases"]) == before + 10 == 125

    # 3) 审计草案 + 备份 + 落盘
    DRAFT.write_text("# v4.11 第十六来源术语草案（t183–t192）\n\n## 可直接粘贴的 YAML 草案\n\n```yaml\n"
                     + terms + "\n```\n", encoding="utf-8")
    BACKUP.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(GL, BACKUP / "glossary.md")
    shutil.copyfile(TP, BACKUP / "test-prompts.json")

    GL.write_bytes(gl_new.encode("utf-8"))
    out = json.dumps(tp, ensure_ascii=False, indent=2) + "\n"
    TP.write_bytes(out.replace("\n", nl_tp).encode("utf-8"))

    # 4) 落盘后复核
    g2 = GL.read_text(encoding="utf-8")
    t2 = json.loads(TP.read_text(encoding="utf-8"))
    assert g2.count("- id: t") == 192
    assert len(t2["test_cases"]) == 125 and t2["version"] == "4.11"
    print("glossary: 182 -> 192 条，t183–t192 连续，id 唯一")
    print(f"test-prompts: 115 -> 125 条，version -> {t2['version']}")
    print(f"draft: {DRAFT.name}")
    print(f"备份目录: {BACKUP.relative_to(BASE).as_posix()}")
    print("APPEND_V4_11_OK")


if __name__ == "__main__":
    main()
