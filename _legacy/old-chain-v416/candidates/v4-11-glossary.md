# v4.11 第十六来源术语草案（t183–t192）

## 可直接粘贴的 YAML 草案

```yaml
- id: t183
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
```
