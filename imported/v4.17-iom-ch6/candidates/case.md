# 案例候选池 — FDA IOM 2026, Chapter 6: Imports（阶段 1 · 案例提取器产出）

> 供阶段 1.5 的 V1 跨域验证与阶段 2 的 A1（Past Application）段使用。
> 取材：`.cangjie/index/*.txt`（含 `[p.N]` 页码标记），以 Grep 定位 `For example / e.g. / such as / Note: / Examples` 等锚点后回原文 Read 核验。
> 口径说明：本章是机构 SOP，**没有叙事型"作者亲历案例"**。按用户指定的口径，"案例"指手册**亲自给出的具体判定示例 / 具体违规情景 / 带数值或表单编号的例示**，每条都按「遇到问题 → 手册规定的动作 → 判定/后果」组织。
> 页码映射：`[p.N]` 位于分块文件中该页文本的起始行；例如 6.1 中行 175 `[p.9]` 到行 232 同属 p.9，行 233 `[p.10]` 起为 p.10。

```yaml
- id: c01
  title: Prior Notice 时限按运输方式分档（陆路 2 / 空运铁路 4 / 水运 8 小时）
  type: case
  source_chapter: IOM 6.1.5.1 [p.9]；后果见 6.1.5.5 [p.11]
  problem: |
    一批食品（含动物饲料）拟入境，FDA 须判断事先通报是否落在法定窗口内——既不能过早、
    也不能过晚，且必须是"FDA 电子接收并确认"而非仅由报关行提交。
  source_quote: |
    "Prior notice for food articles subject to the rule must be received and confirmed
    electronically by the FDA no more than 15 calendar days before the anticipated date
    of arrival for submission made through the PNSI, and no more than 30 calendar days
    before the anticipated date of arrival for submission made through ABI/ACE, and,
    dependent on the mode of transportation below, no fewer than: Two hours before
    arrival by land by road; Four hours before arrival by air or by land by rail;
    Eight hours before arrival by water."

    "Food that is imported or offered for import with inadequate prior notice is
    subject to refusal and holding at the port or in a secure storage facility."
  source_quote_zh: |
    "受该规则约束的食品，其事先通报须由 FDA 电子接收并确认：经 PNSI 提交的不得早于预计
    抵达日前 15 个日历日，经 ABI/ACE 提交的不得早于 30 个日历日；且依运输方式不得晚于：
    公路陆运抵达前 2 小时、空运或铁路陆运 4 小时、水运 8 小时。"
    "事先通报不充分而进口或拟进口的食品，须被拒绝并在港口或安全储存设施内扣留。"
  action: |
    按运输方式套用 2/4/8 小时下限，并核对 15/30 天上限；通报须经 PNSI 或 ABI/ACE 提交
    并取得 FDA 确认回执；国际邮件还须在寄出前确认、且包裹附 FDA 接收确认。总部 DTA
    （24/7）做自动筛查，必要时人工复核，结果回传 CBP。
  outcome: |
    通报不充分 → 拒绝入境 + 港口/安全设施扣留（6.1.5.5）；DTA 可据此在抵达港或其他
    地点（铁路运输则在最近合适查验点）启动 FDA/CBP 查验。时限是可机械判定的硬约束。
  bound_to:
    - "Prior Notice 适用性判定：时限 2/4/8 小时 + 15/30 天上限（优先级 5 的可 skill 化点）"
    - "法定前置义务独立于报关单、须有 FDA 确认回执（核心术语表 Prior Notice 条）"
  tags: [case, prior-notice, time-limit, admissibility, refusal, hard-constraint]

- id: c02
  title: 紧急/易腐货物优先审查（生鲜海产品、新鲜果蔬）
  type: case
  source_chapter: IOM 6.2.2 / 6.2.2.1 [p.16]
  problem: |
    待审 line 数量远大于查验能力，审查员须决定初审排序；同时要防止"紧急"名义被滥用、
    且不能因赶时效而豁免法定文件。
  source_quote: |
    "Emergency and perishable products are time sensitive and take precedence over
    all others. Emergency products are when one or more items need immediate review
    due to an urgent situation. Import divisions decide how to handle these entries
    to prevent abuse. Perishable products are items that can spoil or lose quality if
    stored too long under normal conditions. Examples include: Raw/fresh seafood;
    Fresh fruits and vegetables."
  source_quote_zh: |
    "紧急和易腐产品具有时效性，优先于所有其他货物。紧急产品指因急迫情况需立即复核的
    一项或多项货物，由进口分部决定如何处置以防滥用。易腐产品指在常规条件下存放过久会
    腐败或品质下降的物品，例如：生鲜/鲜海产品、新鲜果蔬。"
  action: |
    6.2.2 规定 QAV 工作类型优先于 NQV、经 ITACS 提交文档者优先；6.2.2.1 再将
    紧急/易腐货物置于"优先于所有其他"的最高位，由 Centers 标识时间敏感产品帮助分部排序。
    对器械类另有硬门槛："Release device shipments only if the entry documents show
    CDRH approval"——无法核验批准文件即联系 cdrhimport@fda.hhs.gov。
  outcome: |
    时间敏感货物进入最高优先级；但优先级不豁免文件要求，缺 CDRH 批准文件的器械仍不放行。
    这是"风险分 + 时效"双重排序，且由分部裁量防止"紧急"标签被滥用。
  bound_to:
    - "入境审查决策树：初审排序（QAV > NQV、ITACS 优先、紧急/易腐最高）"
    - "优先级不豁免法定文件/合规申明（批判：'as warranted' 裁量留给分部惯例）"
  tags: [case, entry-review, prioritization, perishable, emergency]

- id: c03
  title: 照片证据标识示例（123-456789-1/11/1; 8/10/20; RS, information panel, right side, 1 of 4）
  type: case
  source_chapter: IOM 6.1.8 [p.14]（示例文本位于 6.2-Entry-Review.txt 行 21–31）
  problem: |
    现场查验、取样、销毁、重整、拒绝核验产生的照片要作为听证与执法证据，如何保证
    逐张可追溯、不缺页、且永不与 entry/line 失去关联。
  source_quote: |
    "All photographic evidence (including photographs of labeling) must be identified
    with the following required information: entry/line number, collection/examination
    date, investigator's initials, a brief description of the photo, and numbering that
    allows future reviewers to determine if any pages or photos are missing. (An example
    of an adequately identified photographic notation: 123-456789-1/11/1; 8/10/20;
    RS, information panel, right side, 1 of 4)."

    "As such and using the example given above, the file name or Document Remarks
    section would be fulfilled by simply including the remarks: 'information panel/
    right side, 1 of 4.'"
  source_quote_zh: |
    "所有照片证据（含标签照片）须标注：entry/line 编号、采集/查验日期、检查员姓名缩写、
    照片简述，以及能让后续审阅者判断有无缺页缺片的序号。（标识充分的示例：
    123-456789-1/11/1；8/10/20；RS，information panel，右侧，第 1 张/共 4 张。）"
    "因此按上例，从移动设备或电脑文件上传时，文件名或 Document Remarks 只需写明
    'information panel/right side, 1 of 4' 即可（entry/line 号由系统直接自动关联）。"
  action: |
    须用政务配发数字设备拍摄、拷入工作电脑、标注后上传 FDA Import System；按上例逐张
    标识五要素；模糊/不可用照片在确认已拍全清晰照片后方可删除并在监管笔记记录。
    打印件须把标识**永久固定**在照片正上方或正下方（不得直接写在照片上），以免破坏
    证据完整性。
  outcome: |
    标识齐全才构成 "adequately identified photographic notation"；若案件拟走扣押、
    禁令、取消资格或起诉，还须转按 IOM 5.6.7 / 5.7.3 的数字照片与视频证据规程。
  bound_to:
    - "取样与照片证据链规范：逐张标识（entry/line、日期、缩写、描述、序号）+ 上传"
    - "证据可追溯性优先于取证便利（核心命题 6：证据链占查验价值一半）"
  tags: [case, evidence, photography, chain-of-custody, identifiability]

- id: c04
  title: Import for Export（IFE）必备文件与缺件即扣留
  type: case
  source_chapter: IOM 6.1.4.6 [p.8]；6.1.4.6.1 [p.9]
  problem: |
    一批本属违规的 FDA 监管品（人用/兽药或其成分、需进一步加工的器械组件、散装食品
    添加剂/色素/膳食补充剂）声称"进口后加工或并入其他产品再出口"，能否按
    FD&C Act §801(d)(3) 条件准入。
  source_quote: |
    "The following documentation is required at the time of importation according to
    section 801(d)(3) ... includes: 1. A statement that the article is intended to be
    further processed or incorporated ... and will be exported under sections 801(e)
    or 802 ...; 2. Information/documentation that identifies the manufacturer ...
    as well as each processor, packer, distributor, and/or other entity in the chain
    of possession from manufacturer to importer; 3. Such certificates of analysis as
    necessary to identify the article ... In addition, a good and sufficient bond
    must be executed."

    "If the required documents are not provided after they are requested, entry
    reviewers should request detention, indicating the products ... are missing the
    required IFE documentation at the time of initial importation. ... If all required
    documents are provided, including the IUC ... a 'May Proceed' may be issued."
  source_quote_zh: |
    "依 §801(d)(3)，进口时须提交：1. 声明该物品拟进一步加工或并入药物/生物制品/器械/
    食品/添加剂/色素/膳食补充剂，并将依 §801(e)、§802 或 PHS Act §351(h) 出口；
    2. 标识制造商及从制造商到进口商占有链上每一加工商、包装商、经销商等实体（尽量
    收集各实体名称地址）的资料；3. 识别该物品所需的分析证书。此外须订立足额保证金。"
    "若索取后仍未提交所需文件，审查员应请求扣留，注明产品不符合法规要求、系按 IFE
    条款申报、且初次进口时缺少 IFE 文件。……若所需文件（含 IUC）齐备，可签发
    'May Proceed'。"
  action: |
    确认 entry/line 的 IUC 为 "Import for Export" 且 A of C 含 IFE；缺则更新 entry/line、
    记录更新原因、保存并 rescreen。缺支持文档按 IOM 6.2.3.1 索取。若申报为 IFE，
    但单据显示并非"进一步加工并出口"，则改回正确 IUC/A of C、记录原因、保存、
    rescreen、按适用要求重新审查。作可采性判定前须确保全部文档已上传到 entry/line。
  outcome: |
    文件齐备且符合 §801(d)(3) → 可 May Proceed；索取后仍缺 → 请求扣留（RPM 9-17-3）。
    部分 entry 类型可能无 bond 随附，手册明确提示。
  bound_to:
    - "入境类型判定：IFE（§801(d)(3)）适用性与三类必备文件 + bond"
    - "数据完整性规则：更正 → 指派/记录原因 → 保存 → rescreen（核心命题 2）"
  tags: [case, IFE, documentation, admissibility, bond, rescreen]

- id: c05
  title: 误发 May Proceed 后撤消（24 小时 / CBP 30 天 redelivery 窗口）
  type: case
  source_chapter: IOM 6.2.2.2.2 [p.17–18]
  problem: |
    "May Proceed" 系误发，或放行后出现需重新审查的新信息；此时货物可能已被进口商
    控制甚至分销，而条件放行期已经结束。
  source_quote: |
    "You should only rescind a 'May Proceed' in rare cases, such as when a product
    requires a compliance action. You must act immediately ... Once you issue a
    'May Proceed,' the conditional release period for that entry ends permanently.
    Even if you rescind the notice, the period does not reopen."

    "3. Send an updated 'Notice of FDA Action' to the filer, importer, and consignee
    within 24 hours. 4. Request a bond hold from CBP within 24 hours to protect
    against financial loss if the product is refused. 5. Confirm the system sends
    the ABI codes to the filer, which tells them not to distribute the product.
    6. Instruct CBP to demand redelivery if the shipment has already been
    distributed. Act quickly, as CBP has a 30-day window to issue this demand."
  source_quote_zh: |
    "仅在极少数情况下（如产品需采取合规行动）才撤消 'May Proceed'，且须立即行动……
    一旦签发 'May Proceed'，该 entry 的条件放行期即永久结束；即便撤消通知，该期限
    也不会重新开启。"
    "3. 24 小时内向 filer、importer、consignee 发出更新后的 'Notice of FDA Action'；
    4. 24 小时内向 CBP 请求 bond hold，以防产品被拒时产生财务损失；5. 确认系统向
    filer 发出禁止分销的 ABI codes；6. 若货物已分销，指示 CBP 要求 redelivery——
    动作要快，CBP 只有 30 天窗口发出该要求。"
  action: |
    先取主管批准 → 立即通知 filer 已撤消并重新作可采性判定 → 24h 内发更新 NOA +
    24h 内请求 bond hold → 确认 ABI codes 禁止分销 → 已分销则指示 CBP demand
    redelivery → 全过程在 FDA Import System 留痕。
  outcome: |
    条件放行期永久结束、不重开；redelivery 窗口为 **30 天**（区别于拒绝入境后的
    **90 天**）；若货物已无法召回，转入 Bond Action（见 c11）。撤消属"罕见"而非
    例行查验手段。
  bound_to:
    - "放行可撤消：May Proceed / IB Release 均有明确撤消程序（核心命题 4）"
    - "条件放行与 redelivery 窗口：30 天（撤消）/ 90 天（拒绝）"
    - "误放行后立即通知 CBP 请求 redelivery 并留痕"
  tags: [case, may-proceed, rescind, conditional-release, redelivery, 30-days]

- id: c06
  title: DER vs DTR 分流、IA 28-02 印度黑胡椒证书、IA 命中/不命中分流
  type: case
  source_chapter: IOM 6.2.5.1 / 6.2.5.2 / 6.2.5.3 / 6.2.5.4.1 [p.21–22]
  problem: |
    某 line 疑似违规或命中 Import Alert，审查员须决定：用哪种 work type 向 Compliance
    Branch 提交扣留建议、是否必须先索取文档、命中/不命中 IA 时分别如何处置。
  source_quote: |
    "As an entry reviewer, you will use one of two work types to recommend detention:
    DER or DTR. DER (Detention without Physical Examination): Use DER when a product
    is subject to Detention without Physical Examination (DWPE). DTR (All Other
    Detentions): Use DTR for all other situations where a product appears to be
    violative."

    "When you select the detention option (DER or DTR), choose an 'Entry Option' from
    the drop-down menu that also requests documents. For example, select 'Hold
    Designated, Others Go, Docs Required.' This automatically tells the filer to
    submit the needed paperwork."

    "For example, IA 28-02 requires a certificate for all shipments of black pepper
    from India. If the certificate is missing, you must request it before recommending
    detention."

    "If the entry line is matches an IA listing (red/green/yellow list) follow the
    guidance section in the IA. If the entry line does not match the IA listing:
    Continue your initial admissibility review. ... explain why it was not subject
    to the IA. For example: 'Flagged for IA XX-XX, but manufacturer not listed on IA'."
  source_quote_zh: |
    "审查员用两种 work type 之一提交扣留建议：DER 或 DTR。DER（无需实物查验扣留）
    用于产品受 DWPE 约束时；DTR（其他一切扣留）用于其余疑似违规情形。"
    "选择扣留选项（DER 或 DTR）时，从下拉菜单选一个同时索取文档的 'Entry Option'，
    例如 'Hold Designated, Others Go, Docs Required'，这会自动告知 filer 提交所需文件。"
    "例如，IA 28-02 要求所有来自印度的黑胡椒货随附证书；若证书缺失，必须先索取，
    再建议扣留。"
    "若 entry line 命中 IA 名单（红/绿/黄名单），按该 IA 的 guidance 章节办理；
    若未命中，继续初始可采性审查，并说明为何不受该 IA 约束，例如：
    '已被 IA XX-XX 标记，但制造商未列入该 IA'。"
  action: |
    按**触发依据**分流（非严重度分级）：DWPE → DER，其余疑似违规 → DTR；提交前
    收集全部支持文档、逐 line 写清扣留理由、必要时附照片、把所有检索记录写入 Remarks。
    IA 不要求特定文件且电子数据匹配 IA 条件（国家/制造商/产品）又无需额外信息时，
    可免文档直接 DER；IA 要求放行文件（如 28-02 黑胡椒证书）则必须先索取审阅。
    疑似命中但不确定的，先索取文档、修正电子数据并 rescreen。
  outcome: |
    产品有多个违规（命中多个 IA）时，须在扣留建议中列入全部 alerts 与 PAF；
    "Manufacturer is subject to IA XX-XX" 这类具体理由写入 Instruction Text；
    扣留建议一律提交 Compliance Branch，审查员不自行作终局扣留。
  bound_to:
    - "入境审查决策树 + DER/DTR 按触发依据分流（优先级 1，BOOK_OVERVIEW 核心命题 5）"
    - "Import Alert / DWPE 具体分流：文档前置、数据匹配、rescreen、写明理由"
    - "多违规须列全部 alerts/PAF；提交 CB 而非自行终局扣留"
  tags: [case, DER, DTR, import-alert, DWPE, detention, compliance-branch]

- id: c07
  title: Priority Review flag 下放行的"合格 vs 空泛"备注（含肝素/heparin 例）
  type: case
  source_chapter: IOM 6.2.2.2 [p.16]
  problem: |
    某 line 带 Priority Review flag（指向重大公共安全风险，含受 DWPE 约束产品），
    审查员仍拟签发 May Proceed；备注必须写到什么程度才算合格。
  source_quote: |
    "A 'Priority Review' flag points to a major public safety risk. This includes
    products that are subject to Detention Without Physical Examination (DWPE). If
    you decide to issue a 'May Proceed' for a line with a priority review flag, you
    must write a clear reason in the 'Remarks' field. Vague remarks do not provide
    enough information. Examples of Clear Remarks: 'The product brand submitted for
    entry is not a brand name subject to DWPE.' ... 'Documentation shows imported
    item does not contain heparin.' Examples of Vague Remarks: 'Line is not subject
    to IA', 'NA', 'May Proceeded'."
  source_quote_zh: |
    "'Priority Review' 标记指向重大公共安全风险，包括受 DWPE 约束的产品。若对带
    此标记的 line 签发 'May Proceed'，必须在 'Remarks' 栏写出明确理由，空泛备注
    信息不足。合格备注示例：'所申报品牌并非受 DWPE 约束的品牌名'、'产品为粉剂
    而非液剂'、'某制造商/产品豁免于 IA XX-XX'、'单据显示进口品不含肝素'。
    空泛备注示例：'Line is not subject to IA'、'NA'、'May Proceeded'。"
  action: |
    放行决定须落到可复核的具体事实（品牌、物理形态、豁免依据、成分检测结果），
    逐条对应 flag 的触发条件；同时先审阅并考虑 FDA Import System 的 PREDICT 风险分
    与规则标记。
  outcome: |
    空泛备注不予接受；与筛查/flag 相悖的放行、请求扣留、请求现场工作三类决定，
    都必须在系统备注写出具体理由，"May Proceed"/"N/A" 这类空泛备注被明确禁止。
  bound_to:
    - "与 PREDICT 结果相悖的放行必须写明理由（核心命题 3）"
    - "判定须由有资质人员基于单据 + PREDICT + IA + 历史记录共同作出（核心命题 1）"
  tags: [case, remarks, PREDICT, may-proceed, priority-review, evidence]

- id: c08
  title: 重整完成后的合格部分放行与 rejects 处置（及"不给第二次机会"）
  type: case
  source_chapter: IOM 6.5.2.5 / 6.5.2.6 [p.40]
  problem: |
    经 FDA 批准并监督的改标/重整完成后，同一批货中既有已达可采状态的部分，
    也有不合格部分（rejects）；或首次重整失败，申请人想再试一次。
  source_quote: |
    "If the conditions of the approved reconditioning application have been fulfilled,
    the division will notify the owner or consignee by Notice of Release. This notice
    is usually identified as 'Released after Reconditioning.' ... Where there is a
    non-admissible portion (or rejects), they must be destroyed or re-exported under
    FDA or CBP supervision. A Notice of Refusal of Admission should also be issued for
    the rejected portion. Additionally, the FDA may include in its approval ... a
    provision for the non-admissible portions (rejects) ... to be destroyed and not
    exported."

    "If the initial attempt at reconditioning is unsuccessful, a second attempt
    should not be considered unless a revised method of reconditioning shows a
    reasonable assurance of success. If the conditions ... have not been fulfilled,
    a 'Notice of Refusal of Admission' is issued ... with a copy also sent to CBP."
  source_quote_zh: |
    "若已满足批准的重整申请条件，分部以 Notice of Release 通知货主或收货人，该通知
    通常标注为 'Released after Reconditioning'，副本送 filer。若存在不可采部分
    （rejects），须在 FDA 或 CBP 监督下销毁或再出口，并就该被拒部分另行签发
    Notice of Refusal of Admission。FDA 还可在批准书中规定 rejects 只销毁、不得出口。"
    "若首次重整失败，除非修订后的方法能合理保证成功，否则不应考虑第二次尝试；
    若未满足批准条件，则签发 'Notice of Refusal of Admission'……副本送 CBP。"
  action: |
    条件满足：合格部分发 Notice of Release（"Released after Reconditioning"）；
    rejects 在 FDA 或 CBP 监督下销毁或再出口并单独出拒绝通知；FDA 可限定只销毁
    不得出口。条件未满足：发拒绝入境通知（副本送 CBP）。重整前须提交 Form FDA 766
    （见 c10），完成后可作后续查验/取样或仅接受进口商声明。
  outcome: |
    合格与不合格部分分别出具放行/拒绝文书；重整失败原则上不给第二次机会，
    除非修订方法"能合理保证成功"。
  bound_to:
    - "扣留→听证→改标/重整→复核→放行或拒绝的处置链与文书矩阵（优先级 2）"
    - "重整失败不给第二次机会；合格部分放行时不合格部分仍须销毁/再出口并单独出拒绝通知（核心命题 9）"
  tags: [case, reconditioning, rejects, refusal, release, one-chance]

- id: c09
  title: 拒绝入境后 90 天出口/销毁、CBP form 4647 与"档案不关闭"
  type: case
  source_chapter: IOM 6.5.2.8 [p.41]；6.5.2.10 [p.42]
  problem: |
    听证后仍判违规、或进口商本人请求拒绝，货物可能已处于进口商控制之下，
    FDA 须保证违规品被彻底清出美国市场而非仅"发一纸通知"。
  source_quote: |
    "The 'Notice of FDA Action - Refusal of Admission' provides for the exportation
    or destruction of the shipment, under CBP supervision, within 90 days of the date
    of the notice ... The FDA file remains open until the division receives
    notification indicating that the goods were either destroyed or exported.
    Following issuance of the 'Notice of FDA Action - Refusal of Admission,' the entry
    refusal is communicated with CBP for the issuance of the CBP form 4647 Notice to
    Mark and/or Redeliver (CBP form 4647) ..."

    "Exportation and destruction of refused goods are done under CBP supervision.
    However, if after a reasonable time, the FDA has not received notification of
    exportation or destruction, the Division should investigate the status of
    disposition."
  source_quote_zh: |
    "'Notice of FDA Action - Refusal of Admission' 规定货物须在通知发出之日起 90 天内
    （或 CBP 规定延长期内）在 CBP 监督下出口或销毁……FDA 档案一直保持开放，
    直到分部收到货物已销毁或已出口的通知。发出拒绝通知后，须将拒绝通报 CBP，
    以签发 CBP form 4647（Notice to Mark and/or Redeliver）。"
    "被拒货物的出口与销毁在 CBP 监督下进行；但若合理期限内 FDA 仍未收到出口或销毁
    通知，分部应调查处置状态。"
  action: |
    签发拒绝通知（指控措辞须与原扣留通知一致，副本送 CBP）；通报 CBP 签发
    CBP form 4647（Demand for Redelivery）；分部收到 4647 邮件后按本港 post-refusal
    流程处理并把副本上传到 entry/line；若发现 4647 未签发，联系 compliance officer
    并通知 CBP CTAC。合理期限未收到处置通知则主动调查，并视情况核验货物是否完好
    待处置或确已再出口，销毁见证须拍照。
  outcome: |
    90 天内在 CBP 监督下出口或销毁；FDA 档案在收到销毁/出口证明前保持开放；
    FDA 对食品、药品、化妆品、烟草等的公众健康责任延续到违规品被销毁或出口为止。
  bound_to:
    - "拒绝入境后 FDA 公共健康责任延续到销毁/出口，档案不因发通知而关闭（核心命题 10）"
    - "CBP 4647 红交货 + 90 天出口/销毁窗口（与 Failure to Hold 的 30 天区分）"
    - "文书—环节举证矩阵"
  tags: [case, refusal, CBP-4647, destruction, export, 90-days, public-health]

- id: c10
  title: 四张表单的具体使用场景（FDA 766 / FDA 790 / FDA 415a / FDA 483a）
  type: case
  source_chapter: IOM 6.5.2.3 / 6.5.2.4 [p.40]；6.5.2.9 [p.41]；6.4.6(SDI) [p.39]；6.8.2 [p.48]
  problem: |
    不同环节该用哪张表、由谁出具、触发条件是什么——这是把判定转成可复核证据的关键，
    也是 IOM 中"带表单编号"的例示最集中的地方。
  source_quote: |
    "The FDA may authorize relabeling or other remedial action upon the timely
    submission of an 'Application for Authorization to Relabel or To Recondition
    Non-Compliant Articles,' (Form FDA 766 - See Exhibit 6-2). ... The redelivery
    bond on file with the Port Director of CBP for the particular importation applies
    to any relabeling or other action authorized; a new bond will not have to be
    filed."

    "After the relabeling or reconditioning operation has been completed, the
    applicant will submit the 'Importer's Certificate' (page 2 of Form FDA 766) or
    advise the division that reconditioning is complete. ... The 'Report of
    Investigator/Inspector' (section 4, page 2 of Form FDA 766) ... should be
    forwarded to the appropriate FDA office."

    "After completion of the authorized relabeling or other action, the FDA will
    submit a detailed statement of expenses incurred, including travel, per diem or
    subsistence, and supervisory charges on a Form FDA 790 ... The expenses shall
    include charges for supervision of destruction of the article or rejects. ...
    Payment of supervisory charges should not be accepted by any FDA division offices."

    "SDI samples require the following: ... An official seal (Form FDA 415a) on the
    sample container(s). ... Collector's ID on the seal ... Note: This information
    is required so that the FDA can utilize its domestic authority if the sample
    analysis results are violative."

    "The FDA 483a, FSVP Observations is intended to assist firms inspected in
    complying with the laws and regulations enforced by the FDA. ... The issuance
    of written inspectional observations is mandated by law and by OII policy."
  source_quote_zh: |
    "FDA 可在及时提交《改标或重整不合规品授权申请》（Form FDA 766，见 Exhibit 6-2）
    后授权改标或其他补救措施。……已在 CBP 口岸主管处备案的该批 redelivery bond
    适用于任何获批的改标或行动，无须另立新 bond。"
    "改标/重整完成后，申请人须提交 'Importer's Certificate'（FDA 766 第 2 页）或告知
    分部重整完成；'Report of Investigator/Inspector'（FDA 766 第 2 页第 4 节）或等效
    重整总结应转送相应 FDA 办公室。"
    "获批改标/行动完成后，FDA 用 Form FDA 790 向 CBP–Revenue Division 提交费用明细
    （差旅、per diem/膳食、监督费），费用含对货物或 rejects 销毁的监督费；
    任何 FDA 分部办公室不得代收监督费。"
    "SDI 样品另需：样品容器加官方封条（Form FDA 415a）、封条上采集人 ID……
    注：此信息是必需的，以便样品分析结果为违规时 FDA 可启用其国内管辖权。"
    "FDA 483a（FSVP Observations）用于协助被检查企业遵守 FDA 执行的法律法规……
    书面检查观察项的签发由法律与 OII 政策强制要求。"
  action: |
    - 扣留后拟改标/重整 → 及时提交 Form FDA 766（也可来函 + 足额保证金），
      批准后退回原件列明条件与时限。
    - 重整完成 → 提交 FDA 766 第 2 页 Importer's Certificate 或告知完成；FDA 可复核
      查验/取样，并把第 2 页第 4 节报告转送相应办公室。
    - 监管费用 → 完成后用 Form FDA 790 向 CBP 列明细；由 CBP 向进口商发缴款通知。
    - SDI 国内进口特殊样品 → 容器加 Form FDA 415a 官方封条 + 采集人 ID + Remarks
      内标签描述/批号，以启用国内管辖权。
    - FSVP 检查观察项 → Form FDA 483a，报告走 T-EIR / EIR。
  outcome: |
    每张表绑定固定环节与责任方，构成"环节—文书—签字/字段"举证矩阵；
    Exhibit 6-1~6-4 为扫描件、无文本层，表单字段细节须查原件（阶段 0 已标注）。
    FDA 790 未来若改为电子处理将停用；483a 观察项与报告是独立于货物查验的合规轨。
  bound_to:
    - "文书—环节举证矩阵：每个环节应产出哪张表 / 哪个字段 / 谁签字"
    - "SDI 样品 + 415a 官方封条用于检出违规时启用国内管辖权（核心命题 7）"
    - "FSVP 观察项走 FDA 483a、报告走 T-EIR/EIR（核心命题 13）"
  tags: [case, forms, FDA-766, FDA-790, FDA-415a, FDA-483a, SDI, FSVP, evidence]

- id: c11
  title: Bond Action 的两类触发情景与 CBP 违约金
  type: case
  source_chapter: IOM 6.5.2.11 [p.42]
  problem: |
    某批条件放行货物在 FDA 放行前已被分销且无法 redeliver；或已被扣留并拒绝，
    却未按法律要求销毁/出口。此时货物已失控，须转向经济追责。
  source_quote: |
    "Bond actions are taken when an entry is distributed prior to FDA release and
    cannot be redelivered, or when an article has been detained and refused, and the
    article is not destroyed or exported in accordance with the requirements of the
    law. ... If the division has evidence that the entry, or any portion of an entry
    subject to FDA jurisdiction, was disposed of in violation of the terms of the
    appropriate Act ... it should immediately contact the appropriate Customs office."

    "Upon the receipt of an application for relief (appeal for Mitigation or
    Cancellation of Assessed Liquidated Damages), CBP may agree to mitigate the
    damages assessed. However, in cases involving FDA goods, CBP does not usually
    mitigate unless the FDA is in full agreement with the action [see 21 CFR
    section 1.97 (b)]."
  source_quote_zh: |
    "以下情形启动 Bond Action：entry 在 FDA 放行前已被分销且无法 redeliver；或货物
    已被扣留并拒绝、却未按法律要求销毁或出口。……若分部有证据表明某 entry 或其中
    受 FDA 管辖的部分被违反法案/法规/bond 条款处置，应立即联系相应海关办公室。"
    "收到减免申请（对已核定违约金的 Mitigation 或 Cancellation 上诉）时，CBP 可同意
    减免；但涉及 FDA 货物的案件，除非 FDA 完全同意该行动，CBP 通常不予减免
    [见 21 CFR 1.97(b)]。"
  action: |
    一有证据立即联系相应 Customs office；收到"未出口/销毁"证据立即调查；向负责
    CBP 办公室送交说明进口商在 redelivery bond（或其他适用海关 bond）下责任的
    详细声明；若事实成立且货物仍在扣留、尚未发拒绝通知，立即补发 Notice of Refusal
    （副本送 CBP）。bond 依据 FD&C Act §801(b) 与 19 CFR 113.62，所有条件放行品
    均须有 bond。
  outcome: |
    触发 CBP 按 CBP Notice of Assessment 追缴违约金（liquidated damages）；
    CBP 可依申请减免，但涉及 FDA 货物一般须 FDA 完全同意才减免。与 6.7 的
    filer evaluation、6.6 的 CBP 制裁（行政扣押、民事罚款、取消条件放行特权、
    提高 bond 金额/单笔 bond）相接。
  bound_to:
    - "条件放行 bond / Failure to Hold 的经济后果（优先级 3）"
    - "拒绝后公共健康责任延续到销毁/出口，bond action 是兜底（核心命题 10）"
    - "进口调查把个案证据转成 CBP 制裁输入（核心命题 12）"
  tags: [case, bond-action, liquidated-damages, redelivery, 19-CFR-113.62]

- id: c12
  title: Failure to Hold 的 8 步调查 + 健康危害/DWPE 加重（RTE 食品 Salmonella 例）
  type: case
  source_chapter: IOM 6.6.4.1 [p.43]；6.6.4.2 [p.43–44]；6.6.4.3 [p.44]
  problem: |
    货物在 FDA 放行前已被进口商/收货人分销（Failure to Hold）。若其中涉及重大
    健康危害，或该批仅因 DWPE 历史被扣（证据标准只到"外观违规"），处置优先级
    与追加动作是否不同——手册用两类 Salmonella 情景作了明确分级。
  source_quote: |
    "Failure to hold means that the goods have been distributed by the
    importer/consignee without an FDA release from import status. *Please note that
    this is defined as distribution without a release, not merely moving the goods
    outside of the port area."

    "1. Collect entry documentation (CBP form 3461 or 7501, invoice, packing list,
    bill of lading). 2. Determine distribution ... 3. Determine who authorized the
    distribution. 4. Determine if the importer was aware of the health hazard ...
    5. Obtain the authorizing person's explanation ... (Items (1)-(5) should be
    covered in one or more affidavits.) 6. Perform a data search via ORADSS ... to
    determine the importer's history ... 7. Coordinate with CBP the issuance of a
    Demand for Redelivery (form 4647) ... In such circumstances, the deadline for
    redelivery is 30 days, instead of the 90 days post-refusal. 8. Determine the
    importer's bond type and amount."

    "Distribution of goods where there is direct evidence of a significant health
    hazard, such as an FDA finding of Salmonella contamination in a ready-to-eat
    food entry, should be regarded as a concern of the highest priority."

    "Distribution of goods where there is evidence of a significant health hazard
    that only meets the appearance of a violation evidentiary standard ... --such as
    an entry of a ready-to-eat food detained without physical examination (DWPE) due
    to a history of Salmonella contamination--should still be regarded as a concern
    of high priority."

    "Consult with supervisory staff, compliance staff, and the division's Recall
    and Emergency Coordinator as needed to address retrieval from and/or
    notification to the consignees, as well as consideration for any public warning."
  source_quote_zh: |
    "Failure to Hold 指货物在未获 FDA 从进口状态放行前，已被进口商/收货人分销。
    请注意：定义是'无放行而分销'，而非仅仅把货物移出港区。"
    "8 步：1. 收集 entry 单据（CBP 3461 或 7501、发票、装箱单、提单）；2. 分析
    分销记录确定分销；3. 查明谁授权分销；4. 判断进口商是否知悉产品健康危害；
    5. 取得授权人说明（1–5 项须作成一份或多份 affidavit）；6. 经 ORADSS 等检索
    进口商历史并与主管/compliance 讨论；7. 与 CBP 协调签发 form 4647（此时
    redelivery 期限为 30 天，而非拒绝后的 90 天）；8. 核定进口商 bond 类型与金额。"
    "分销货物存在重大健康危害直接证据的——例如 FDA 在某即食（RTE）食品 entry 中
    检出 Salmonella 污染——应视为最高优先级事项。"
    "分销货物存在重大健康危害、但证据仅达到'外观违规'标准（§801(a) 可采性程序
    标准）的——例如某即食食品因既往 Salmonella 污染史被 DWPE 扣留——仍应视为
    高优先级事项。"
    "按需与主管、compliance 及分部 Recall and Emergency Coordinator 协商，
    处理向收货人追回/通知，并考虑是否发布公共警告。"
  action: |
    所有 Failure to Hold 案统一走上述 8 步；第 4 步（是否知悉健康危害）与第 6 步
    （历史检索）是分级输入。健康危害案追加：与主管、compliance、Recall and
    Emergency Coordinator 协商收货人追回/通知及公共警告。DWPE 情形再追加：
    协商 FDA 是否取样分析，以及同样的追回/通知/公共警告。
  outcome: |
    直接证据型（RTE 食品检出 Salmonella）= **最高优先级**；仅达外观违规证据标准的
    DWPE 历史型（因既往 Salmonella 史被 DWPE 扣留的 RTE 食品）= **高优先级**；
    两者都在 8 步基础上加召回/公共警告协调，并可转入 CBP 制裁（Title 19）或
    OCI 刑事调查输入。调查 memo 须在末次调查活动后 10 个工作日报主管背书、
    主管 5 个工作日内背书。
  bound_to:
    - "Failure to Hold 判定（关键是'分销'而非'位移'）与 8 步调查清单（优先级 3，核心命题 11）"
    - "健康危害 / DWPE 加重步骤：召回、收货人通知、公共警告、是否取样"
    - "30 天 redelivery（Failure to Hold）vs 90 天（拒绝后）"
    - "进口调查把个案证据转成 CBP 制裁 / OCI 刑事调查输入（核心命题 12）"
  tags: [case, failure-to-hold, health-hazard, Salmonella, RTE, DWPE, recall, investigation]
```

## 覆盖说明与缺口（如实标注）

**口径**：本章无"某进口商/某企业"的具名个案，也无叙事型结局；`outcome` 字段均为
**程序性后果**（放行/扣留/拒绝/违约金/优先级），不是商业结果。已按原书口径提取，
未编造场景。

**因数量上限（目标 6–12 条）未单列、但确实存在的同类具体例示**（阶段 2 A1 段如需可回原文取用）：

- SCR 字段填写示例（6.4.6.6 [p.37]）："Sample consists of 12 subs /16 oz. (1lb) each of IQF Cod Fillets collected at random from lot B129A1. Sample was collected aseptically from 12 master cases and packed in 12 whirl-pak bags."；Hand Ship 冷链示例（6.4.6.7 [p.37]）："Transported from firm in a closed cooler with gel packs ... until shipped via UPS to PRL-NW in a cooler with Gel packs."；Remarks 示例（6.4.6.8 [p.37]）："Store frozen. Master case code: PRODUCTION DATE 1319 ... Analyze for milk protein per IB XX-BXX" 与 "Examined 200 units from lot 1234 for defects and identified 6 with pitting"；Record Time 小数例（6.4.6.9 [p.38]）："6 min = 0.1, 12 min = 0.2, 18 min = 0.3, 24 min = 0.4"。
- Substitution 藏货位置（6.6.4.4 [p.44]）："in a partially substituted entry, the substituted goods are in the center, bottom position on a pallet; or placement of the substituted goods is in the front position of the trailer."
- Importer / Filer misdeclaration（6.6.4.5 [p.44]、6.6.4.6 [p.45]）：申报由 firm X 生产实为 firm Y；未申报货物；"if a filer declares a cosmetic product code for fluoridated toothpaste because the importer failed to provide the filer information about whether the toothpaste did or did not contain fluoride, it may be necessary to collect that information via an affidavit from the importer."
- FSVP 记录审查（6.8.1 [p.48]）："if an importer's sampling and testing records indicate that a sample was positive for Salmonella, determine if the importer took appropriate corrective actions (for example, importer did not import the food, imported food was recalled, importer worked with the foreign supplier to address the problem, importer discontinued use of the foreign supplier)."
- 条件放行期延长（6.2 [p.20]）："To extend the conditional release period, you must notify the importer in writing within the first 30 days."
- 多次违规/类似 IA 清单分流（6.2.5.2 [p.21]、6.2.5.4.2 [p.22]）："If a product has multiple violations (for example, it is subject to more than one Import Alert), you must include all applicable alerts and problem area flags (PAFs)"；以及"previous entry may be pending addition to DWPE"下有/无 Direct Reference Authority 的分叉。

**稀少/缺失**：表单版式（Exhibit 6-1~6-4）为扫描件、无文本层，字段细节只能标注
"需查原件"；本章不提供进口商视角的举证/应对情景；"as warranted / where appropriate"
类裁量未给出阈值，故相关条目只记录手册明确写出的触发条件。
