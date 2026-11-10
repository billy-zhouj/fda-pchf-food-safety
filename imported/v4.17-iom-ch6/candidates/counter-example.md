# Counter-Example Candidates — IOM 2026 Chapter 6: Imports

> 阶段 1 · 反例提取器（counter-example-extractor）产出
> 取材路径：检索式取块 `.cangjie/index/*.txt`（关键词召回 + 邻接块），逐条回 `source/iom-ch6-full.txt` 核验引用
> 页码一律 `[p.N]`（物理 PDF 页，见 `PIPELINE_STATE.md` 约束 1）；英文原文 ≤100 词/段；中文自译为译者自译
> 英文引文排版规范化（不改词）：内层双引号记为单引号、弯撇号 `’` 记为直撇号 `'`；`"` 外层引号用于界定引文段落
> **`enterprise_avoidance` 字段一律标注【推导】：IOM 是 FDA 内部操作手册（监管者视角），不写企业侧义务，该字段为据判定逻辑反推，非原书主张**
> 产出 14 条：x01–x12 为手册明确警告的失败模式 / 违规行为 / 禁止做法 / 程序陷阱；x13–x14 为「效力层误读」型，供下游 Boundary (B) 段使用

## 取材覆盖自检

| 用户指定重点 | 命中条目 |
|---|---|
| Failure to Hold（含 health hazard / DWPE 加重）| x01, x02 |
| Substitution | x03 |
| Importer Misdeclaration | x04 |
| Filer Misdeclaration | x05 |
| 误发 IB Release 后 30 天窗口被错过 | x07 |
| 空泛备注 "May Proceed"/"N/A" 被明确禁止 | x06 |
| 未经 FDA 放行的分销 | x01, x08 |
| 未获批准的自行改标/重整 | x09 |
| 重整失败后不得轻易给第二次机会 | x09 |
| 拒绝入境后未出口/销毁的保证金行动 | x08 |
| 照片标识丢失导致证据链断裂 | x10 |
| Inadequate Prior Notice | x11 |
| IFE 缺少 IUC/A of C | x12 |
| filer 数据错误影响 PREDICT 筛查 | x12 |
| 效力层误读（当法规 / should→shall / May Proceed / DWPE / conditional release）| x13, x14 |

补充命中：`port shopping`（6.6.1 [p.42]，并入 x03/x05 的 warning_signs 与 tags）、`inadvertently`（6.4 续文 [p.33]，x07）、`rescind`（6.2.2.2.2 / 6.3.11，x07）、`inadequate`（6.1.5.5，x11）。

---

## 候选清单

```yaml
- id: x01
  title: "Failure to Hold：未获 FDA 放行即已分销（且被误定义为「货物移出港区」）"
  type: counter-example
  subtype: 违规模式（四类之首）/ 定义反直觉
  source_chapter: "IOM 6.6.4.1 [p.43]；术语 6.9.30 [p.53]；Bond Action 6.5.2.11 [p.42]"
  source_quote: |
    "Failure to hold means that the goods have been distributed by the
    importer/consignee without an FDA release from import status. *Please note
    that this is defined as distribution without a release, not merely moving
    the goods outside of the port area. FDA personnel may encounter this situation
    at various points in the importation process, including initial exam/inspection,
    sample collection, audit sample collection, reconciliation examination after
    a health hazard finding, verification of a reconditioning, and refusal
    verification. The following steps should be taken on all Failure to Hold cases:"
    (IOM 6.6.4.1 [p.43])
  quote_zh: |
    「Failure to Hold 指进口商/收货人在未取得 FDA 放行、货物仍处进口状态时就已将其分销。
    请注意：该违规定义为『无放行而分销』，而非『仅把货物移出港区』。FDA 人员可在进口流程的
    多个环节遇到此情形：初次查验、取样、审核取样、健康危害发现后的核对查验、重整复核、
    拒绝核验。以下各步骤应适用于所有 Failure to Hold 案件。」
  failure_mode: |
    把「条件放行 / 货已到仓」当成「已可销售」，在收到 FDA May Proceed / Notice of Release 之前
    即发货、上架或转售；或误以为「只要不把货搬出港区就不算违规」，因而只管位移、不管分销。
  mechanism: |
    手册把违规锚定在「分销（distribution）」这一法律动作上，而非物理位移——位置变化本身
    不构成该违规，但一旦货物离开进口商控制进入流通，redelivery（召回）事实上已不可能。
    固定的 8 步调查清单随之启动：①取单据（CBP 3461/7501、发票、装箱单、提单）②查分销记录
    ③查授权分销人 ④查进口商是否知悉健康危害 ⑤取授权人说明并作成 affidavit ⑥ORADSS
    检索历史 ⑦协调 CBP 发 4647 Demand for Redelivery（此情形期限 30 天而非拒绝后 90 天）
    ⑧核定 bond 类型与金额。调查结论可转成 CBP 制裁（行政扣押、民事罚款、取消条件放行特权、
    保证金行动）或 OCI 刑事调查输入（6.6.2 [p.43]）。
  consequence: |
    货物无法召回 → 触发 bond action / liquidated damages；进口商与授权人被作成 affidavit 追责；
    CBP 可施加民事罚款、行政扣押、取消条件放行特权；情节严重者移交 OCI 刑事调查。
  warning_signs:
    - "仓库/销售系统里货物状态已是『可售』，但 FDA Import System 里该 line 仍 pending"
    - "只有 CBP 的 immediate delivery / 条件放行回执，没有 FDA May Proceed 或 Notice of Release"
    - "把『货还在港区/保税仓』当作合规证明"
    - "同一 entry 多个 line 中部分已放行、部分未放行却整批发货"
  bound_to:
    - "条件放行 / 可采性判定能力卡（不可把 conditional release 当放行）"
    - "放行后处置链能力卡（收到放行文书才算闭环）"
  enterprise_avoidance: |
    【推导】企业应以「逐 line 收到 FDA 放行文书」为唯一发货闸门，把仓库 WMS 的放行状态与
    FDA 回执绑定，且在放行前保持货物完整可召回，不以「货未出港区」作为可分销的依据。
  tags: [counter-example, failure-to-hold, distribution-without-release, bond-action, investigation-8-steps]

- id: x02
  title: "Failure to Hold 遇健康危害 / DWPE 时未按最高优先级升级（把 DWPE 当低风险放过）"
  type: counter-example
  subtype: 违规模式（加重情节）/ 反直觉陷阱
  source_chapter: "IOM 6.6.4.2 [p.43-44]；6.6.4.3 [p.44]；PREDICT Priority Review 6.2.2.2 [p.16]"
  source_quote: |
    "Distribution of goods where there is direct evidence of a significant health
    hazard, such as an FDA finding of Salmonella contamination in a ready-to-eat
    food entry, should be regarded as a concern of the highest priority."
    (IOM 6.6.4.2 [p.43])

    "Distribution of goods where there is evidence of a significant health hazard
    that only meets the appearance of a violation evidentiary standard (the standard
    under the 801(a), admissibility process) --such as an entry of a ready-to-eat food
    detained without physical examination (DWPE) due to a history of Salmonella
    contamination--should still be regarded as a concern of high priority."
    (IOM 6.6.4.3 [p.44])
  quote_zh: |
    「分销的货物若存在重大健康危害的直接证据（如 FDA 在即食食品 entry 中检出沙门氏菌），
    应视为最高优先级事项。」「即便健康危害证据仅达到『外观违规』证明标准（§801(a) 可采性
    程序下的标准）——例如因沙门氏菌污染史而被 DWPE 扣留的即食食品 entry——仍应视为高优先级事项。」
  failure_mode: |
    把「只是 DWPE、没有实物查验阳性报告」理解为「证据不足、风险较低」，因而不启动召回协调、
    收货人通知与公共警告评估；或把健康危害案件当普通 Failure to Hold 走完 8 步即结案。
  mechanism: |
    手册区分两档加重：6.6.4.2（有直接证据，最高优先级）与 6.6.4.3（仅达 §801(a)「外观违规」
    标准，仍为高优先级）。两档都在 8 步之外追加：与主管/合规人员及分区 Recall and Emergency
    Coordinator 协商，处理向收货人追回/通知、评估是否发布公共警告；DWPE 档还须评估 FDA 是否
    另行取样分析。关键反直觉点：DWPE = 「不检查就扣住」，其背后的违规史本身就是风险信号，
    绝非「不检查就放过」。PREDICT 的 Priority Review flag 明确包含 DWPE 产品（6.2.2.2 [p.16]）。
  consequence: |
    受污染/高风险货已流入市场而未被追回 → 公共卫生事件；FDA 须追加取样、收货人追溯、
    公共警告，并可能升级为召回与 OCI 介入；进口商同时承担 x01 的全部 bond 与制裁后果。
  warning_signs:
    - "涉案产品命中 Import Alert / DWPE / PREDICT Priority Review flag"
    - "涉及即食食品、沙门氏菌等重大健康危害关键词"
    - "调查取证时只做 8 步清单、未联系 Recall and Emergency Coordinator"
    - "认为『没做实物检验就没有违规证据』"
  bound_to:
    - "Failure to Hold 调查清单能力卡（必须声明健康危害/DWPE 的加重分支）"
    - "DWPE / Import Alert 判定能力卡（不得把 DWPE 理解为免检放行）"
  enterprise_avoidance: |
    【推导】企业一旦发现自己或供应商命中 Import Alert/DWPE 或产品涉健康危害，应立即冻结
    同批次及关联批次的分销并主动追溯收货人，而不是等 FDA 实物检验结论出来再行动。
  tags: [counter-example, failure-to-hold, health-hazard, DWPE, recall, public-warning, priority-review]

- id: x03
  title: "Substitution：以他批货物顶替申报 entry 接受查验（常用于掩盖无放行分销）"
  type: counter-example
  subtype: 违规模式 / 禁止做法
  source_chapter: "IOM 6.6.4.4 [p.44]；术语 6.9.73 [p.58]；调查价值 6.6.1 [p.42]"
  source_quote: |
    "Substitution is an attempt by the importer or importer's agent to present goods
    to the FDA as corresponding to a particular entry when they are, in fact, not the
    goods from that entry. ... Substitution may occur as an attempt to hide distribution
    without FDA release (Failure to Hold). The investigation may reveal negligence, gross
    negligence, or fraud. ... Until it is determined otherwise, consider all substitution
    cases to involve distribution of the actual goods without FDA release."
    (IOM 6.6.4.4 [p.44])

    "Examine the entire shipment as this would minimize the possibility of the importer
    successfully claiming at a later time that the portion not examined was in fact not
    substituted." (IOM 6.6.4.4 [p.44])
  quote_zh: |
    「Substitution 指进口商或其代理人把并非该 entry 的货物，当作对应该 entry 的货物提交给
    FDA。……Substitution 可能是为掩盖『无 FDA 放行即分销』（Failure to Hold）。调查可能揭示
    过失、重大过失或欺诈。……在查明相反事实之前，应把所有 substitution 案件视为真实货物
    已在无 FDA 放行情况下被分销。」「应查验整批货物，以最大限度降低进口商事后辩称
    『未查验的那部分其实没有被顶替』的可能。」
  failure_mode: |
    在初验、取样、审核取样、健康危害后核对、重整复核、redelivery 查验任一环节，用外观相似
    的合格品摆到托盘前排/车厢前部、把被顶替品藏在托盘中心底部，冒充申报货物供 FDA 查验；
    或只让 FDA 看部分货物以便事后否认。
  mechanism: |
    Substitution 与 Failure to Hold 强耦合：真货往往已被分销，顶替品是为应付查验而摆出的。
    因此手册设定「举证责任倒置式」推定——在查明相反前，一律按真货已无放行分销处理（回到
    6.6.4.1 的 8 步）。取证要点：确认所呈货物被声称为对应某 entry；收集标签、批号、货物状态
    与照片（「Photos are invaluable in these instances」）；收集隐瞒顶替的证据（居中/底部/前排
    摆放）；取进口商/代理人对差异的说明并作成 affidavit；必须查验整批以封堵事后抗辩。
    6.6.1 [p.42] 另把 entry misdeclaration、product substitutions 与 "port shopping" 并列为
    进口调查要揭露的三类规避行为。
  consequence: |
    直接按 Failure to Hold 全套追责；调查定性可为过失 / 重大过失 / 欺诈，欺诈档移交 OCI 刑事；
    叠加 bond action、民事罚款、取消条件放行特权，以及 port shopping 触发的跨口岸重点监控。
  warning_signs:
    - "托盘中心/底部或车厢前排出现与其余货物标签、批号、包装不一致的货"
    - "进口商只愿开放部分货物供查验，或对『整批查验』设置阻碍"
    - "实物与申报的制造商、产品代码、数量、价值对不上"
    - "同一进口商在多个口岸反复出现类似申报（port shopping 信号）"
  bound_to:
    - "现场查验/取样执行能力卡（必须整批查验、留照片证据）"
    - "Failure to Hold 调查清单能力卡（substitution 一律并入该清单）"
  enterprise_avoidance: |
    【推导】企业应保证送检/待查货物与申报 entry 逐件一致、批号可追溯，禁止为「让查验通过」
    临时调换或补摆样品，并保留能自证整批一致性的装箱与影像记录。
  tags: [counter-example, substitution, failure-to-hold, port-shopping, fraud, affidavit, full-shipment-exam]

- id: x04
  title: "Importer Misdeclaration：进口商经 filer 向 FDA/CBP 提供错误或不完整信息"
  type: counter-example
  subtype: 违规模式
  source_chapter: "IOM 6.6.4.5 [p.44-45]；术语 6.9.47 [p.55]"
  source_quote: |
    "Importer misdeclaration refers to the importer's provision of incorrect and/or
    incomplete information to the FDA and CBP, usually via the filer. ... It may be the
    case that the investigation reveals negligence, gross negligence, or fraud. The
    following are examples of this kind of activity: The importer provides information
    to the filer that does NOT include a product that is present in the entry, and as a
    result, that product is not included in the declaration (undeclared goods)."
    (IOM 6.6.4.5 [p.44-45])

    "It may occur as an attempt to avoid FDA and/or CBP actions/regulations, such as
    DWPE, sampling, duties, etc." (IOM 6.9.47 [p.55])
  quote_zh: |
    「Importer misdeclaration 指进口商（通常经由 filer）向 FDA 与 CBP 提供错误和/或
    不完整信息。……调查可能揭示过失、重大过失或欺诈。此类行为例如：进口商向 filer 提供的
    信息未包含 entry 中实际存在的某产品，导致该产品未被申报（未申报货物）。」
    「其目的可能是规避 FDA 和/或 CBP 的措施/法规，如 DWPE、取样、关税等。」
  failure_mode: |
    少报产品（undeclared goods）、虚报制造商（申报 firm X 实为 firm Y）、错报产品代码/
    描述、制造商/发货人名称地址、数量与价值；动机常是绕开 DWPE、取样或关税。与 x05 的
    分界在于：**错在进口商提供的信息本身**。
  mechanism: |
    申报数据是 PREDICT 风险评分与 Import Alert 匹配的唯一输入，错报会直接改变筛查结果，
    使本应被 DWPE/取样命中的 line 被判为低风险放行。因此手册把它与 substitution、
    port shopping 并列为进口调查要揭露的规避链条（6.6.1 [p.42]）；定性分过失 / 重大过失 /
    欺诈三档，证据升级路径同 x03。常见发现于初次查验或取样环节。
  consequence: |
    错误数据污染可采性判定 → 违规货物被放行；调查定性为过失/重大过失/欺诈，欺诈移交 OCI；
    叠加 CBP 行政扣押、民事罚款、取消条件放行特权、bond action。
  warning_signs:
    - "发票/装箱单上的产品数量、品名与 ACE/ABI 申报不一致"
    - "申报制造商与实际标签、批号、COA 上的厂商不符"
    - "某产品命中 Import Alert，但申报被刻意拆成不触发警报的产品代码"
    - "进口商无法解释数据来源，或解释与随货单据矛盾"
  bound_to:
    - "申报数据完整性 / rescreen 能力卡（错数必须更正并重新筛查）"
    - "Import Alert / DWPE 匹配能力卡（错报会使匹配失效）"
  enterprise_avoidance: |
    【推导】企业应建立「随货单据 → 申报数据」的逐字段复核与留痕（发票、装箱单、标签、
    COA、制造商信息），由独立于报关行的人员签核后再提交，避免为了规避警报而调整申报口径。
  tags: [counter-example, importer-misdeclaration, undeclared-goods, PREDICT, DWPE-avoidance, fraud]

- id: x05
  title: "Filer Misdeclaration：filer 把进口商给的正确信息报错，且「进口商最终负责」"
  type: counter-example
  subtype: 违规模式 / 责任归属反直觉
  source_chapter: "IOM 6.6.4.6 [p.45]；6.6.4.6.1 [p.45]；6.7.1 [p.45]；6.2.5.2 [p.21]"
  source_quote: |
    "Although this section is oriented to filer interventions, it must always be
    recognized that the filer is the agent of the importer, and the importer is
    ultimately responsible. Filer misdeclaration refers to the importer's provision of
    correct information to the filer who then files an erroneous entry to CBP."
    (IOM 6.6.4.6 [p.45])

    "If the filer has a history of filing erroneous entries to FDA, and the filer
    continues to disregard FDA's attempts to provide guidance, train, and document
    guidance provided of filing entries through the Automated Broker Interface (ABI),
    the FDA should contact (CBP) to request that a broker penalty be assessed against
    the filer." (IOM 6.6.4.6.1 [p.45])
  quote_zh: |
    「尽管本节针对 filer 的干预，必须始终认识到：filer 是进口商的代理人，进口商承担最终
    责任。Filer misdeclaration 指进口商向 filer 提供了正确信息，而 filer 却向 CBP 提交了
    错误申报。」「若 filer 有反复向 FDA 错报的历史，且继续无视 FDA 通过 ABI 提供的指导、
    培训与已留痕的指导记录，FDA 应联系 CBP，请求对该 filer 课以报关行罚款。」
  failure_mode: |
    误以为「数据交给报关行就与进口商无关」「错在 filer 则由 filer 独自承担」；或长期容忍
    同一 filer 反复错报（漏报产品、制造商报错、产品 X 报成 Y、在信息不足时滥用食品
    PIC 代码）而不做 filer evaluation。
  mechanism: |
    与 x04 的分界是**错误发生在 filer 环节而非进口商提供的信息**。手册明确「filer 是进口商
    代理人、进口商最终负责」，故责任不因外包而转移。重复违规（6.6.4.6.1）有固定升级阶梯：
    ①记录 filer 当时掌握的信息 ②用标签/照片固定未申报或错报产品 ③affidavit 取 filer 说明
    ④必要时取进口商 affidavit ⑤执行 Filer Evaluation 并视历史分档：无历史 → 培训 / 退回
    phase 1 filing status、暂不请求罚款；有历史且持续无视指导 → 请求 CBP 课以 broker penalty。
    6.7.1 [p.45] 说明根因：FDA 的可采性判定完全依赖 filer 传输的电子数据，故 6.7 只做周期性
    filer evaluation 抽样监控（阶段 0 批判指出：抽样是否足以支撑逐批判定并未被论证）。
  consequence: |
    进口商承担最终责任（罚款、制裁、bond action 不因外包免除）；filer 可被退回 phase 1、
    被 CBP 课以 broker penalty；错误数据持续污染 PREDICT 筛查（6.2.5.2 [p.21]
    "Inaccurate data will affect PREDICT screening"）。
  warning_signs:
    - "同一 filer 多次出现同类错报（同一产品代码 / 同一制造商字段反复错）"
    - "进口商提供的发票正确，但 ABI/ACE 申报与之不符"
    - "在信息不足时选择『包装食品』通用 PIC 等兜底代码"
    - "把『已委托报关行』当作免责依据"
  bound_to:
    - "申报数据完整性能力卡（更正→指派责任→保存→rescreen）"
    - "filer/报关行管理能力卡（需周期性 evaluation，非一次性委托即完结）"
  enterprise_avoidance: |
    【推导】企业应把 filer 视为需持续受控的代理人：定期比对发票与申报回执、保留正确信息的
    送达证据、对反复错报的 filer 立即更换或升级复核，不能以外包合同转移最终责任。
  tags: [counter-example, filer-misdeclaration, importer-ultimately-responsible, broker-penalty, filer-evaluation, PREDICT]

- id: x06
  title: "用 \"May Proceed\" / \"N/A\" 作系统备注（手册明确禁止的空泛备注）"
  type: counter-example
  subtype: 明确禁止做法 / 留痕失败
  source_chapter: "IOM 6.2.1 [p.15]；6.2.2.2.2 [p.16]；6.2.3.1 [p.19]；6.2.5.1 [p.21]"
  source_quote: |
    "Avoid vague remarks like 'May Proceed' or 'N/A'" (IOM 6.2.1 [p.15])

    "If you decide to issue a 'May Proceed' for a line with a priority review flag,
    you must write a clear reason in the 'Remarks' field. Vague remarks do not provide
    enough information. Examples of Vague Remarks: 'Line is not subject to IA';
    'NA'; 'May Proceeded'" (IOM 6.2.2.2.2 [p.16])
  quote_zh: |
    「避免使用『May Proceed』或『N/A』这类空泛备注。」「若对带 Priority Review 标记的
    line 决定签发 May Proceed，必须在 Remarks 字段写出明确理由。空泛备注提供的信息不足。
    空泛备注示例：『Line is not subject to IA』『NA』『May Proceeded』。」
  failure_mode: |
    在三类决定上只写结论不写理由：请求扣留、请求现场工作、以及与 PREDICT 筛查结果相悖
    的 May Proceed；或用「N/A / May Proceed / Line is not subject to IA」这类循环复述动作的
    空话充当备注。
  mechanism: |
    备注是「可复核、可在听证与后续执法中站得住」的载体：与 PREDICT 结果相悖的放行、
    请求扣留、请求现场工作三类决定，必须在系统里写出**具体理由**。手册给出正例对照：
    「所报品牌不属于 DWPE 品牌」「产品为粉剂而非液体」「特定制造商/产品豁免于 IA XX-XX」
    「单据显示进口品不含肝素」——都是可被第三方检验的事实判断。空泛备注使后续审查员、
    Compliance Branch 与听证方无法重建判定依据，等于证据链断点。6.2.5.2 [p.21] 进一步要求
    「必须把所做的全部检索写进扣留建议的 Remarks」。
  consequence: |
    判定不可复核、扣留建议被退回；与 PREDICT 相悖的放行失去合法性说明；在听证、
    CBP 制裁或 OCI 刑事程序中举证链断裂。备注字段为 FDA 内部使用（6.2.1 [p.15]），
    但 DEF/INF 生成的 Narrative 会出现在公开的 Notice of FDA Action 上（6.2.3.3 [p.20]）。
  warning_signs:
    - "Remarks 里只有动作名或缩写，没有可验证的事实"
    - "放行决定与 PREDICT 风险评分 / Priority Review flag 相悖却无解释"
    - "扣留建议的 Remarks 未记录做过哪些数据库检索"
    - "用 N/A 跳过本应填写的理由字段"
  bound_to:
    - "入境审查决策树能力卡（输出必须含具体理由，不能只输出动作码）"
    - "DER/DTR 扣留建议能力卡（Remarks 必须含检索留痕）"
  enterprise_avoidance: |
    【推导】企业提交给 filer/FDA 的说明性材料（如豁免主张、成分/剂型说明）应给出可核验的
    具体事实与证据出处，避免「符合要求」「不适用」这类无信息量的表述被原样带进申报备注。
  tags: [counter-example, vague-remarks, explicitly-prohibited, PREDICT-override, audit-trail, remarks-field]

- id: x07
  title: "误发 IB Release / 撤消后错过 CBP 30 天 redelivery 窗口，且条件放行期不可重开、不可被常规动作延长"
  type: counter-example
  subtype: 程序陷阱 / 时限不可逆
  source_chapter: "IOM 6.2.2.2.2 [p.17-18]；6.3.11 [p.32]；6.3.11 续文（见 6.4 分块）[p.33]；6.2.4 [p.20-21]"
  source_quote: |
    "Once you issue a 'May Proceed,' the conditional release period for that entry
    ends permanently. Even if you rescind the notice, the period does not reopen. ...
    Instruct CBP to demand redelivery if the shipment has already been distributed.
    Act quickly, as CBP has a 30-day window to issue this demand."
    (IOM 6.2.2.2.2 [p.17-18])

    "CBP has 30 days to demand redelivery from the date the conditional release period
    ended (i.e., the 'IB Release' was issued.) Any delays compromise FDA's ability to
    request CBP issue a Notice to Redeliver. ... to document FDA follow-up when FDA
    issues an IB Release inadvertently." (IOM 6.3.11 续文 [p.33])

    "Important: The following actions do not extend the conditional release period:
    Requesting Documents (DRQ); Detention Requests (DTR or DER); Deficient Entry (DEF);
    Requesting Information (INF)" (IOM 6.2.4 [p.20])
  quote_zh: |
    「一旦签发 May Proceed，该 entry 的条件放行期即永久终止；即便撤消该通知，期限也不会重开。
    ……若货物已被分销，应指示 CBP 要求 redelivery；行动要快，因为 CBP 只有 30 天窗口
    可发出该要求。」「CBP 自条件放行期结束之日（即 IB Release 签发之日）起有 30 天要求
    redelivery；任何延误都会损害 FDA 请求 CBP 发出 Notice to Redeliver 的能力。……用以记录
    FDA 在误发 IB Release 后的跟进。」「重要：以下动作不延长条件放行期：DRQ、
    DTR 或 DER、DEF、INF。」
  failure_mode: |
    ①误把 IB Release / May Proceed 当成「可随时撤回重来」的中间动作，撤消后以为条件放行期
    会重新计时；②发现误放行后未在 24 小时内通知 filer、更新 NOA、请求 bond hold、发
    ABI「Do Not Distribute」码，导致 CBP 30 天 redelivery 窗口被错过；③以为发了 DRQ/DTR/
    DEF/INF 就等于「还在审」，从而拖延作出可采性决定，直到 30 天条件放行期自然届满。
  mechanism: |
    条件放行期是法定倒计时（通常 30 天），其终止条件是「先发生者」：FDA 签发 May Proceed、
    签发拒绝通知、或 30 天届满（6.2.4 [p.20]）。放行/撤消是**不可逆**动作：撤消 May Proceed
    或 IB Release 都「does not re-open」条件放行期，且撤消仅允许用于 compliance action 等
    例外情形、须立即完成、不得用于例行或工作计划查验（6.3.11 [p.32]）。撤消后的补救是
    一串 24 小时硬动作 + 30 天内请 CBP 发 4647 要求 redelivery；窗口一过，货物既已分销则
    无法召回。延长条件放行期只有一条路：在头 30 天内**书面**通知进口商并声明 FDA 将查验、
    取样或扣留（6.2.4 [p.20]）——DRQ/DTR/DER/DEF/INF 明确**不算**。
  consequence: |
    错过 30 天窗口 → 无法要求 redelivery、货物无法追回 → 直接落入 bond action /
    liquidated damages（6.5.2.11 [p.42]）；同时因「未作出可采性决定而条件放行期届满」
    造成程序瑕疵。误发 IB Release 的跟进还须写入 Entry Remarks / Miscellaneous Info
    以备审计（6.4 续文 [p.33]）。
  warning_signs:
    - "系统里出现 inadvertent IB Release，但 24 小时内没有对应的 NOA / bond hold / ABI 码"
    - "以『已发 DRQ / 已提交 DTR』为由认为审查时钟暂停"
    - "撤消放行后仍按原 30 天重新计算条件放行期"
    - "条件放行期临近届满却没有书面延长通知"
  bound_to:
    - "入境审查决策树能力卡（放行/撤消是不可逆动作，须有 24h + 30d 时限分支）"
    - "条件放行与 Failure to Hold 能力卡（30 天倒计时先到先算）"
    - "放行后处置链能力卡（撤消后补救步骤不可省略）"
  enterprise_avoidance: |
    【推导】企业收到任何形式放行通知后不应立即视作终局，仍应保留货物可召回状态直至确认
    FDA 决定稳定；若收到「Do Not Distribute / Decision Rescinded」码应立即冻结分销，
    并意识到对方追货的法律窗口只有 30 天、逾期企业将承担保证金与损害赔偿风险。
  tags: [counter-example, IB-release-inadvertently, rescind, 30-day-window, redelivery, conditional-release, irreversible, DRQ-DTR-DEF-INF]

- id: x08
  title: "拒绝入境后未出口/销毁即触发 Bond Action；FDA 档案不因发出拒绝通知而关闭"
  type: counter-example
  subtype: 程序陷阱 / 责任延续反直觉
  source_chapter: "IOM 6.5.2.8 [p.41]；6.5.2.10 [p.41-42]；6.5.2.11 [p.42]；6.6.4.1 第7步 [p.43]；术语 6.9.44 [p.55]"
  source_quote: |
    "The 'Notice of FDA Action - Refusal of Admission' provides for the exportation
    or destruction of the shipment, under CBP supervision, within 90 days of the date
    of the notice ... The FDA file remains open until the division receives notification
    indicating that the goods were either destroyed or exported. ... [FDA is] responsible
    for the protection of the U.S. public ... until the violative article is either
    destroyed or exported." (IOM 6.5.2.8 [p.41])

    "Bond actions are taken when an entry is distributed prior to FDA release and cannot
    be redelivered, or when an article has been detained and refused, and the article is
    not destroyed or exported in accordance with the requirements of the law."
    (IOM 6.5.2.11 [p.42])
  quote_zh: |
    「Notice of FDA Action - Refusal of Admission 要求在 CBP 监督下于通知之日起 90 天内
    出口或销毁货物……FDA 档案在分部收到货物已被销毁或出口的通知之前一直保持开启。……
    在违规物品被销毁或出口之前，FDA 对美国公众的保护责任持续存在。」「当 entry 在 FDA
    放行前已被分销且无法召回，或货物已被扣留并拒绝、却未依法销毁或出口时，即采取保证金行动。」
  failure_mode: |
    把 Refusal of Admission 当作流程终点：发出/收到拒绝通知后即认为「案子结了」，
    未在 CBP 监督下 90 天内完成出口或销毁、未回传销毁/出口证明；或在等待期间擅自处置、
    转售、挪作他用。另一路是 x01 的「放行前已分销且无法召回」，同样直接触发 bond action。
  mechanism: |
    手册把拒绝入境后的公共健康责任**延续到实物灭失为止**：档案关闭条件是「收到销毁或
    出口通知」，不是「发出通知」。6.5.2.10 [p.41-42] 要求：合理时间内未收到出口/销毁通知，
    分部应调查处置状态，必要时核实货物是否仍完整待处置、是否真的发生了再出口，并对见证的
    销毁与差异拍照。CBP 依 WI-000618 发 4647 Demand for Redelivery；若发现 4647 未发，
    须找 compliance officer 并通知 CBP CTAC。 bond 依据 FD&C Act §801(b) 与 19 CFR 113.62，
    CBP 的 liquidated damages 一般**不减轻**，除非 FDA 完全同意（21 CFR 1.97(b)，6.5.2.11 [p.42]）。
    注意 Failure to Hold 第 7 步的 4647 是 30 天期限（用于查验/取样），与拒绝后 90 天不同（6.6.4.1 [p.43]）。
  consequence: |
    Bond action / liquidated damages（且通常不予减免）；CBP 4647 redelivery；
    FDA 调查处置状态、核实是否实物仍完整；档案不关闭，持续监管；若货物已被分销则
    并联 x01 全部制裁与 OCI 路径。
  warning_signs:
    - "已收到 Refusal Notice 但系统里该 entry 仍显示未结案"
    - "90 天将届满却无 CBP 监督下的销毁/出口证明回执"
    - "把『已申请出口/已安排销毁』等同于『已完成并取证』"
    - "CBP 4647 未签发或签发后未上传至 entry/line"
  bound_to:
    - "扣留→听证→重整→拒绝处置链能力卡（拒绝不是终点，须含出口/销毁核验与结案条件）"
    - "Bond Action 能力卡（触发条件含『放行前分销且无法召回』）"
  enterprise_avoidance: |
    【推导】企业收到拒绝通知后应在 90 天内于 CBP 监督下完成出口或销毁并取得可回传的
    书面/影像证明，主动向相关方提交结案凭证，且在此之前保持货物完整、不得转售或挪用。
  tags: [counter-example, refusal-of-admission, bond-action, liquidated-damages, 90-days, export-or-destroy, file-remains-open, CBP-4647]

- id: x09
  title: "未获 FDA 批准自行改标/重整；且重整失败后不得轻易给第二次机会"
  type: counter-example
  subtype: 禁止做法 / 反直觉陷阱（整改不产生放行效力）
  source_chapter: "IOM 6.5.2.3 [p.40]；6.5.2.4 [p.40]；6.5.2.5 [p.40]；6.5.2.6 [p.40]；6.5.2.9 [p.41]"
  source_quote: |
    "The FDA may authorize relabeling or other remedial action upon the timely submission
    of an 'Application for Authorization to Relabel or To Recondition Non-Compliant
    Articles,' (Form FDA 766 ...). ... After review of the application, FDA will notify
    the importer of its approval or disapproval. If approved the original application
    will be returned outlining the conditions to be fulfilled and the time limit within
    which to fulfill them will be noted." (IOM 6.5.2.3 [p.40])

    "If the initial attempt at reconditioning is unsuccessful, a second attempt should
    not be considered unless a revised method of reconditioning shows a reasonable
    assurance of success." (IOM 6.5.2.6 [p.40])
  quote_zh: |
    「FDA 可基于及时提交的 Form FDA 766《改标或重整不合格品授权申请》，**批准**改标或
    其他补救措施。……审查申请后，FDA 将通知进口商批准或不批准；若批准，退回的原件会列明
    须满足的条件及完成期限。」「若首次重整不成功，除非修订后的重整方法能合理保证成功，
    否则不应考虑第二次尝试。」
  failure_mode: |
    认为「返工/改标是我方内部质量动作」，在 FDA 批准前自行撕标重贴、分选、返工、掺混，
    并以为整改完自然获得放行；或首次重整失败后原样再试一次碰运气；或把合格部分放行后，
    对不合格部分（rejects）不再单独出具拒绝通知、也不监督销毁/再出口。
  mechanism: |
    重整的法律效力来自「FDA 授权 + 按批准条件执行 + FDA/CBP 复核」三段，而非企业单方返工：
    须及时提交 FDA 766（或信件 + 足額 bond），FDA 批准并载明条件与时限；完成后提交
    Importer's Certificate（FDA 766 第 2 页）或告知完成，FDA 可后续查验/取样或径行接受
    声明（6.5.2.4 [p.40]）；满足条件才发 "Released after Reconditioning"（6.5.2.5 [p.40]）。
    手册用 "may authorize" / "approval or disapproval" 明示这是**机构裁量**而非企业权利——
    这正是 x13「把 should/may 当 shall」的具体体现。第二次机会的门槛是「修订方法能合理保证
    成功」，不是「再试一次」。监管费用另按 FDA 790 计收，且「Payment of supervisory charges
    should not be accepted by any FDA division offices」（6.5.2.9 [p.41]，须付 CBP）。
  consequence: |
    未经批准的自行整改不产生放行效力，货物仍按违规处理 → 拒绝入境 + 90 天出口/销毁 +
    bond action；首次重整失败且方法未实质改进 → 直接发 Notice of Refusal of Admission
    （6.5.2.6 [p.40]）；rejects 未单独处置同样触发拒绝与保证金责任。
  warning_signs:
    - "整改方案/时间表尚未收到 FDA 批准回执就动手"
    - "第二次重整申请与第一次方法几乎相同，只改了执行日期"
    - "把 FDA 766 当成『事后备案表』而非『事前授权申请』"
    - "合格部分已放行，但 rejects 无独立 Refusal Notice / 销毁记录"
  bound_to:
    - "扣留→听证→重整→拒绝处置链能力卡（重整必须含『批准』这一闸门）"
    - "任何『企业侧整改』推导能力卡（必须标注为推导并声明需 FDA 授权）"
    - "效力层 Boundary（may/should 属裁量，不构成企业权利）"
  enterprise_avoidance: |
    【推导】企业应在动手整改前取得 Form FDA 766 的书面批准并严格按列明条件与时限执行，
    首次失败后须提出实质修订且有成功保证的方法再申请复核，同时把监管费用付给 CBP 而非 FDA。
  tags: [counter-example, reconditioning, relabeling, FDA-766, unauthorized-rework, no-second-chance, rejects, supervisory-charges]

- id: x10
  title: "照片标识丢失 / 贴在照片上 → 证据链断裂（「never any loss of association」）"
  type: counter-example
  subtype: 禁止做法 / 证据链陷阱
  source_chapter: "IOM 6.1.8 [p.13-14]（标识规则续文落在 6.2 分块 [p.14]）；6.6.4.4 [p.44]（substitution 取证）"
  source_quote: |
    "All photographic evidence (including photographs of labeling) must be identified
    with the following required information: entry/line number, collection/examination
    date, investigator's initials, a brief description of the photo, and numbering that
    allows future reviewers to determine if any pages or photos are missing."
    (IOM 6.1.8 [p.14])

    "If photographic evidence is printed, ... the required information must be
    permanently affixed to the printed photos so that there is never any loss of
    association between the photographic evidence and the associated entry/line. This
    information must be recorded immediately above or below the photograph(s) (not
    directly on the photos) so that the integrity of the evidence is not compromised."
    (IOM 6.1.8 [p.14])
  quote_zh: |
    「所有照片证据（含标签照片）必须以以下必需信息标识：entry/line 号、采集/查验日期、
    调查员姓名缩写、照片简述，以及能让后续审查者判断是否有页/照片缺失的编号。」
    「若照片证据被打印，……必需信息必须**永久固定**在打印件上，使照片证据与对应
    entry/line 之间永不失去关联。该信息须记录在照片正上方或正下方（**不得直接贴在照片上**），
    以免损害证据完整性。」
  failure_mode: |
    照片用个人设备拍、未上传系统、文件名/Document Remarks 缺 entry/line 号或日期/缩写/序号；
    打印件把标识写在照片画面上、或用便利贴/回形针临时附着导致脱落；删除「模糊」照片前未确认
    已取得全部清晰可用照片；substitution 取证时只拍被顶替的局部而非整批。
  mechanism: |
    照片是「案件开发的关键要素」（crucial element in case development），其证明力一半在画面、
    一半在**与 entry/line 的关联标识**。手册要求：政务配发数字设备拍摄 → 拷入工作电脑 →
    加标识 → 上传 FDA Import System 的对应 entry/line（取样、Class 2/3 现场与标签查验、
    扣留建议、销毁、重整、拒绝核验差异等情形）；上传后本机副本才可删。序号（如
    "1 of 4"）用于让审查者发现缺页。标识写在照片上会遮改画面、破坏原始性；临时附着会
    在流转中丢失关联，造成「不知道这张照片属于哪票货」的不可逆断点。6.6.4.4 [p.44]
    特别指出 substitution 案件中「Photos are invaluable in these instances」。
  consequence: |
    证据与 entry/line 失去关联 → 扣留/拒绝/听证/bond action/OCI 刑事程序中照片不可采；
    无法证明整批已被查验，进口商可抗辩「未查验部分未被顶替」；涉 seizure/injunction/
    debarment/prosecution 时还须改按 IOM 5.6.7 / 5.7.3 的数字证据规程（6.1.8 [p.14]）。
  warning_signs:
    - "打印照片上直接压着标签文字/手写标注"
    - "文件名或 Document Remarks 里查不到 entry/line 号、日期或序号"
    - "照片只存在调查员本机、未上传到 FDA Import System"
    - "一组照片没有『第几张/共几张』的连续编号"
  bound_to:
    - "现场查验与取样证据链能力卡（照片标识、上传、序号为强制字段）"
    - "SCR / 文书—环节举证矩阵能力卡（照片是法定记录质量载体）"
  enterprise_avoidance: |
    【推导】企业自查/迎检留证时也应给每张照片固定附著 entry/line、日期、拍摄人、描述与
    连续序号（放在画面上下方而非画面内），并保留原始文件与上传回执，避免自证材料因
    「无法关联到具体批次」而在争议中失效。
  tags: [counter-example, photograph-identification, evidence-chain, loss-of-association, permanently-affixed, government-device, substitution-photos]

- id: x11
  title: "Inadequate Prior Notice：食品事先通知不充分 → 直接拒绝并扣留（且指导文件不豁免其他执法权）"
  type: counter-example
  subtype: 违规模式 / 前置法定义务
  source_chapter: "IOM 6.1.5 [p.10-11]；6.1.5.5 [p.11]；6.1.5.6 [p.11-12]；6.1.4.6.1 [p.8-9]"
  source_quote: |
    "Food that is imported or offered for import with inadequate prior notice is subject
    to refusal and holding at the port or in a secure storage facility. The FDA provided
    guidance to its stakeholders and CBP staff on enforcing such prior notice
    requirements in its Compliance Policy Guide ... This guidance, however, does not
    limit the FDA's ability to take actions that may be necessary ... This policy will
    also not affect the ability of CBP to assess penalties under 19 U.S.C. 1595a(b) or
    to take enforcement action under any other authority." (IOM 6.1.5.5 [p.11])
  quote_zh: |
    「事先通知不充分的进口或拟进口食品，将被拒绝并在港口或安全储存设施扣留。FDA 已在
    其 Compliance Policy Guide 中向利益相关方与 CBP 人员提供执行该要求的指导……但**该指导
    并不限制** FDA 采取必要行动的权力（包括为食品安防顾虑实施检查或依 FD&C Act 采取其他
    行动）。本政策也**不影响** CBP 依 19 U.S.C. 1595a(b) 课处罚款或依其他授权执法的权力。」
  failure_mode: |
    把 Prior Notice 当成「报关单里顺带填的一项」或以为「货到后补报即可」；漏报/错报
    15 项要素（提交人/传输人识别、食品完整 FDA 产品代码与通用名、制造商/发货人、
    承运人、运输方式、预期抵达时间、曾被拒绝入境的国家名、邮寄日期等）；或误以为 CPG
    指导文件给了宽限/豁免、可据此排除 FDA 检查与 CBP 罚款。
  mechanism: |
    Prior Notice 是《2002 年公共卫生安全与生物恐怖主义防范应对法》下**独立、有确认回执的
    法定前置义务**，按运输方式 2/4/8 小时提前提交，不是报关单的附属字段（21 CFR Part 1）。
    审查先经自动电子筛查，需要时由总部 DTA（7×24）人工复核，结果回传 CBP；DTA 可在
    抵达口岸或就近查验点发起查验，并负责与提交人就合规、因事先通知不足或未注册境外制造商
    而启动的拒绝/扣留、复核请求等进行沟通（6.1.5.6 [p.11-12]）。满足事先通知的食品**还要**
    再走 §801(a) 可采性审查（PREDICT / Import Alert），两道门互不替代。注意本段同时是
    x13「指导 ≠ 法规」的原文锚点：CPG「does not limit」FDA 权限、「will not affect」
    CBP 罚款权。
  consequence: |
    食品被拒绝 + 港口/安全设施扣留；CBP 可依 19 U.S.C. 1595a(b) 罚款；FDA 仍可依
    FD&C Act 另做检查与其他执法；货物滞期与仓储成本由进口方承担；且不因此免除后续
    §801(a) 可采性审查。
  warning_signs:
    - "把 Prior Notice 确认回执与 CBP 入境回执混为一谈"
    - "按 2/4/8 小时时限倒推的提交时间晚于实际抵达/装运"
    - "以『CPG 里有宽限说明』为由主张免检或免罚"
    - "境外制造商未注册却仍按一般食品申报"
  bound_to:
    - "Prior Notice 适用性判定能力卡（独立前置义务，须含时限与 15 项要素）"
    - "效力层 Boundary 能力卡（指导文件不构成豁免，真义务在 21 CFR Part 1）"
  enterprise_avoidance: |
    【推导】企业应把 Prior Notice 作为独立的发运前置闸门，按运输方式倒推时限提交并保存
    FDA 确认回执，逐项核对 15 项要素与境外制造商注册状态，不把 CPG 指导当作可不合规的依据。
  tags: [counter-example, inadequate-prior-notice, refusal-and-hold, 21-CFR-Part-1, CPG-not-a-waiver, DTA, 2-4-8-hours]

- id: x12
  title: "申报数据错误污染 PREDICT 筛查：IFE 缺 IUC/A of C、制造商/产品代码/数量错，必须「更正→指派责任→保存→rescreen」"
  type: counter-example
  subtype: 禁止做法 / 数据完整性陷阱（含 IFE 专用字段）
  source_chapter: "IOM 6.1.4.6.1 [p.8-9]；6.2.1 [p.14]；6.2.2.2.3 [p.18]；6.2.5.2 [p.21]；6.2.5.3 [p.22]；6.7.1 [p.45]"
  source_quote: |
    "Confirm that IFE or suspected IFE entry/lines are submitted with an intended use
    code (IUC) of 'Import for Export' and with the IFE in the Affirmation of Compliance
    (A of C). If the entry/line lacks the IUC IFE and/or the IFE A of C, update the
    entry/line, record the reason for the update, save, and rescreen the entry/line. ...
    entry reviewers should request detention, indicating the products ... are missing the
    required IFE documentation at the time of initial importation." (IOM 6.1.4.6.1 [p.9])

    "Correct any inaccurate data (manufacturer, shipper, product code, quantity, etc.)
    that could affect PREDICT screening. Assign fault to the responsible party. Save and
    rescreen the entry/line after making corrections." (IOM 6.2.1 [p.14])

    "Note: All information in 'Line Details' must be accurate. Inaccurate data will
    affect PREDICT screening." (IOM 6.2.5.2 [p.21])
  quote_zh: |
    「确认 IFE 或疑似 IFE 的 entry/line 已随附用途代码（IUC）『Import for Export』，
    且在 Affirmation of Compliance（A of C）中含 IFE。若 entry/line 缺少 IUC IFE 和/或
    IFE A of C，须更新该 entry/line、记录更新理由、保存并**重新筛查**。……审查员应请求
    扣留，指明产品在初次进口时缺少必需的 IFE 单据。」「更正任何可能影响 PREDICT 筛查的
    错误数据（制造商、发货人、产品代码、数量等）；指派责任方；保存并在更正后重新筛查。」
    「注意：Line Details 中所有信息必须准确。不准确的数据会影响 PREDICT 筛查。」
  failure_mode: |
    发现申报数据错却「先审后改」或改完不 rescreen；把 IUC / A of C 当无所谓的元数据；
    IFE（Import for Export，§801(d)(3)）申报缺 IUC「Import for Export」或缺 IFE A of C
    就放行；或以为更正只是改字段、不必指派责任方与留痕。
  mechanism: |
    PREDICT 的评分、mashup grid 与规则标记完全由 filer 传输的电子数据驱动（6.7.1 [p.45]：
    「FDA makes admissibility decisions based on the electronic entry data transmitted
    by the filers ... dependent on entry filers to submit the most accurate data」），
    因此任何影响筛查的字段错误都会让**后续所有判定建立在脏数据上**。手册给出的统一修复
    闭环是四步：更正 → 记录理由 / 指派责任方 → 保存 → rescreen（6.2.1 [p.14]、
    6.2.2.2.3 [p.18]、6.2.5.3 [p.22]「Update and rescreen the entry if you make
    corrections」）。IFE 是特例：IUC 与 A of C 看似元数据，实为可采性判定依据；缺件时先
    请求单据（6.2.3.1），单据仍不提供则请求扣留并注明「初次进口时缺 IFE 单据」；
    即便声称 IFE，若审核显示货物并非拟进一步加工后出口，也须改回相应 IUC/A of C 并 rescreen
    （6.1.4.6.1 [p.9]）。注意 6.2.2.2.1 [p.17] 的反向禁则：系统自动审查已清关的 line，
    **不要**再人工核 A of C 数据——避免无谓改动引入新脏数据。
  consequence: |
    脏数据使 PREDICT 误判风险 → 本应命中 Import Alert/DWPE 的 line 被放行，或合规 line 被
    误扣；扣留建议因 Line Details 不准被退回；IFE 缺件直接导致扣留与拒绝；错报责任被
    指派并记入 filer/进口商合规史，触发 x04/x05 的升级阶梯。
  warning_signs:
    - "改了制造商/产品代码/数量却没有对应的 rescreen 记录与理由留痕"
    - "IFE 申报里 IUC 不是『Import for Export』，或 A of C 无 IFE 标记"
    - "把 IUC / A of C 当成『填不填都行』的可选元数据"
    - "多处数据更正未指派责任方，导致无法判断是 importer 还是 filer 错报"
  bound_to:
    - "申报数据完整性与重新筛查能力卡（四步闭环不可省）"
    - "DER/DTR 分流能力卡（提交前须校正数据并 rescreen）"
    - "IFE / 入境类型判定能力卡（IUC 与 A of C 是判定字段）"
  enterprise_avoidance: |
    【推导】企业应在提交前逐字段核对 IUC、A of C、制造商、发货人、产品代码与数量，
    发现错误时坚持「更正并重新取得筛查结果」而非沿用旧筛查结论，同时保留谁提供、谁更正的
    书面记录以便区分 importer 与 filer 责任。
  tags: [counter-example, data-integrity, PREDICT, rescreen, IFE, IUC, affirmation-of-compliance, assign-fault, line-details]

- id: x13
  title: "效力层误读（一）：把 IOM 内部操作指导当法规、把 should / may / as warranted 当 shall"
  type: counter-example
  subtype: 效力层误读 / Boundary 核心素材
  source_chapter: "BOOK_OVERVIEW §3 最强反对意见（阶段 0 上下文）；原文锚点 IOM 6.1.5.5 [p.11]、6.2.2.2.2 [p.17]、6.5.2.3 [p.40]、6.6.4.1 [p.43]、6.5.2.11 [p.42]"
  source_quote: |
    "This guidance, however, does not limit the FDA's ability to take actions that may
    be necessary ... This policy will also not affect the ability of CBP to assess
    penalties under 19 U.S.C. 1595a(b) or to take enforcement action under any other
    authority." (IOM 6.1.5.5 [p.11])

    "You should only rescind a 'May Proceed' in rare cases ... You must act immediately,
    as this action is not for routine examinations." (IOM 6.2.2.2.2 [p.17])

    "Under the provisions of the FD&C Act (Section 801(b) ...) and CBP regulations
    (19 CFR 113.62), a bond is required" (IOM 6.5.2.11 [p.42])
  quote_zh: |
    「但该指导并不限制 FDA 采取必要行动的权力……本政策也不影响 CBP 依 19 U.S.C.
    1595a(b) 课处罚款或依其他授权执法的权力。」「你只应在罕见情形下撤消 May Proceed……
    但必须立即行动，因为该动作不用于例行查验。」「依据 FD&C Act §801(b) 及 CBP 法规
    19 CFR 113.62 的规定，须提交保证金。」
  failure_mode: |
    ①把 IOM 章节蒸馏成「合规规则引擎」，据此对企业主张「FDA 必须/不得如何」；②把手册
    密集出现的 "should / may / as warranted / where appropriate / if the facts warrant"
    读成对企业有约束力的 shall（或反过来把 must 读成可选项）；③把 CPG / IOM 指导文件
    当作豁免依据；④忽略 IOM 是 2026 版快照，系统编号（PREDICT、ITACS、ACE、WI-000618、
    SOP-000217 等）会随改版失效。
  mechanism: |
    阶段 0 批判（BOOK_OVERVIEW §3「最强反对意见」）原文定性：**IOM 是内部操作指导，不是
    法规，也不是可对外主张的法律依据**；真正义务来自 FD&C Act §801、21 CFR Part 1
    （Prior Notice、FSVP）、19 CFR 113.62 等；IOM 中的 "should" 与 "as warranted" 属
    机构裁量，不构成对企业的法定义务，FDA 在个案中偏离 IOM 通常也不产生可诉的权利。
    原文自身反复把义务锚回法条（6.5.2.11 引 §801(b) 与 19 CFR 113.62；6.1.4.6.1 引
    §801(d)(3)；6.9.47 引 21 CFR），并明确区分「guidance/policy」与「authority」
    （6.1.5.5）。同一段内 should 与 must 混用（6.2.2.2.2）、"The FDA **may** authorize"
    （6.5.2.3 [p.40]）、"The following steps **should** be taken"（6.6.4.1 [p.43]），
    正说明其裁量性质。立场盲点：全篇监管者视角，企业若照搬会把「检查清单」误当
    「合规义务清单」，且组织前提（FDA 授权、系统权限、Compliance Branch / OCI / CBP 通道）
    企业并不具备。
  consequence: |
    系统性高估法律位阶 → 据 IOM 作出错误合规判断、在听证/诉讼中主张不成立的权利；
    把随版本失效的 IT 系统与 SOP 编号固化进流程；忽略「应回到法条与当前版本 IOM/RPM
    复核」的复核锚点。
  warning_signs:
    - "能力卡或结论里出现『FDA 必须…』『企业有权…』却只引了 IOM 6.x.x"
    - "把 should / as warranted / where appropriate 直接译成『应/须』"
    - "用 CPG / IOM 的『指导』文字主张豁免或宽限"
    - "引用了具体系统界面/Job Aid/SOP 编号却未标注版本时效"
  bound_to:
    - "全部正面能力卡的 Boundary (B) 段（须写明法律位阶 + 版本时效 + 回到法条复核）"
    - "任何『企业侧义务/迎检清单』推导卡（必须标注为推导，且声明 IOM 不产生企业义务）"
    - "Prior Notice / 重整 / Bond Action 等含法条引用的能力卡（法条才是义务来源）"
  enterprise_avoidance: |
    【推导】企业应把 IOM 定位为「理解 FDA 判定逻辑与举证要求的操作地图」，任何合规结论
    都回到 FD&C Act §801、21 CFR Part 1、19 CFR 113.62 及当前版本 IOM/RPM 复核，
    不把手册中的 should / may 当作可对外主张的权利或义务。
  tags: [counter-example, effect-level-misreading, IOM-not-regulation, should-vs-shall, agency-discretion, legal-hierarchy, version-snapshot, boundary-core]

- id: x14
  title: "效力层误读（二）：把 May Proceed 当「继续办理」、DWPE 当「不检查就放过」、Conditional Release 当「已合格」"
  type: counter-example
  subtype: 效力层误读 / 术语口径陷阱 / Boundary 核心素材
  source_chapter: "IOM 6.9.56 [p.56]；6.2.2.2.1 [p.17]；6.9.22 [p.52]；6.2.2.2 [p.16]；6.9.13 [p.51-52]；6.9.41 [p.55]；BOOK_OVERVIEW §2 术语表"
  source_quote: |
    "May Proceed: The release performed after identifying and determining the line/entry
    meets certain admissibility requirements. This means the product can be distributed
    into U.S. commerce. However, a release does not preclude future FDA action if a
    problem is found later." (IOM 6.9.56 [p.56])

    "Detention Without Physical Examination (DWPE): An action directed against specific
    products manufactured or shipped by specific foreign firms. 'Import Alerts' list
    products that may be detained without physical examination due to their violative
    history or potential." (IOM 6.9.22 [p.52])

    "Even though CBP has allowed the immediate delivery, any FDA-regulated products are
    conditionally released until the FDA makes an admissibility decision. ... The goods may
    be moved but CBP can request redelivery within 30 days." (IOM 6.9.13 [p.51-52])
  quote_zh: |
    「May Proceed：在识别并判定 line/entry 满足特定可采性要求后执行的**放行**。这意味着
    产品可进入美国商业流通。但放行并不排除日后发现问题时 FDA 再采取行动。」「DWPE：
    针对特定境外厂商生产或发运的特定产品采取的行动。Import Alerts 列出因违规史或违规
    可能性而**可无需实物查验即予扣留**的产品。」「即便 CBP 已允许 immediate delivery，
    任何 FDA 监管产品在 FDA 作出可采性决定前都只是**条件放行**。……货物可以移动，
    但 CBP 可在 30 天内要求 redelivery。」
  failure_mode: |
    ①把 "May Proceed" 按字面理解成「准许继续办理/开始审查」，实为**终局性放行动作**
    （且可被 rescind，见 x07）；②把 "Detention Without Physical Examination" 理解成
    「不检查就放过」，实为「不检查就扣住」；③把 "Conditional Release" 理解成
    「有条件地合格/已通过」，实为货物仍处 FDA 管辖、须保持可召回状态；④把 CBP 的
    immediate delivery 当成 FDA 已放行；⑤以为拿到 May Proceed 就永久免责。
  mechanism: |
    三个术语的常见语义与 IOM 法定口径系统性错位，且错位方向都是**高估自身合规状态**：
    - May Proceed = release，"the product can be distributed into U.S. commerce"；
      6.2.2.2.1 [p.17] 补一句「This notice means the shipment can continue without
      further FDA examination」+「A product that is allowed to enter the country can
      still face legal action later if the FDA finds it violates the law (§304(d))」。
    - DWPE 的 "without physical examination" 修饰的是 detention（扣留），不是放行；
      触发依据是 Import Alert 上的违规史/潜力，且 PREDICT 的 Priority Review flag
      明确包含 DWPE 产品（6.2.2.2 [p.16]）——是**加重**而非减轻信号（呼应 x02）。
    - Conditional Release 的终止条件是 FDA "May Proceeds" 或发拒绝（6.9.41 [p.55]），
      期间 CBP 可 30 天内要求 redelivery（6.9.13 [p.51-52]）；货物「may be moved」
      恰恰是 x01 的定义陷阱——**位移不等于分销、更不等于放行**。
    阶段 0 术语表（BOOK_OVERVIEW §2）已逐条标注「和常识用法的差异」，本条即其 Boundary 化。
  consequence: |
    以「继续办理」理解 May Proceed → 在放行前误启动后续动作或错过撤消窗口；
    以「不检查就放过」理解 DWPE → 命中 Import Alert 仍按普通货物排产，遇 x02 加重情形
    未升级；以「已合格」理解 conditional release → 提前分销，直接落入 x01 Failure to Hold
    与 x08 Bond Action；误以为 May Proceed 永久免责 → 忽视 §304(d) 的后续执法可能。
  warning_signs:
    - "内部系统把 May Proceed 译为『可继续办理』或状态名含 proceed 而非 released"
    - "看到 DWPE / Import Alert 后反而降低查验优先级"
    - "仅有 CBP immediate delivery / 条件放行回执就安排上架销售"
    - "把『货可以移动』当成『货可以分销』"
  bound_to:
    - "入境审查决策树能力卡（动作码语义必须按 IOM 口径固化）"
    - "条件放行与 Failure to Hold 能力卡（边界定义：分销 vs 位移）"
    - "Import Alert / DWPE 判定能力卡（DWPE 是扣留而非免检）"
    - "全部能力卡的术语口径层（78 条 glossary 用于消除概念混淆）"
  enterprise_avoidance: |
    【推导】企业应在内部状态机中把 FDA 放行、CBP 条件放行、DWPE 命中三者显式区分，
    以「收到 FDA 放行文书」为唯一可分销状态，并把命中 Import Alert/DWPE 视为升级信号而非
    免检信号。
  tags: [counter-example, effect-level-misreading, may-proceed, conditional-release, DWPE, glossary, terminology-trap, boundary-core]
```

---

## 自检（对照 extractor 规范）

- [x] 每条都有 `failure_mode` 与 `mechanism`（不只是说「这是错的」），且含 8 步清单 / 分档 / 时限 / 责任链等可学习机制
- [x] 每条都有 `warning_signs`（让下游 B 段有信号）
- [x] 每条都有 `bound_to`（说明限制哪些正面 skill 的适用范围），x13/x14 显式指向全部能力卡的 Boundary
- [x] 每条都有原文引用，且每段 ≤100 英文词；已逐条回 `source/iom-ch6-full.txt` 与 `.cangjie/index/*.txt` 核验
- [x] 出处均含 `IOM 6.x.x + [p.N]`；`[p.N]` 依据各分块的页标记映射（见 `MANIFEST.md` / `PIPELINE_STATE.md` 约束 1）
- [x] `enterprise_avoidance` 一律以【推导】开头标注，一句话，不冒充原书主张（呼应 BOOK_OVERVIEW §3 立场盲点）
- [x] 覆盖率优先：对四类违规模式、30 天窗口、空泛备注、拒绝处置链、照片证据、Prior Notice、IFE、PREDICT、效力层误读各查了 2–4 轮并取邻接块；`port shopping` / `inadvertently` / `rescind` / `inadequate` 均有落点
- [x] 数量 14 条，落在目标 8–14 区间上限
