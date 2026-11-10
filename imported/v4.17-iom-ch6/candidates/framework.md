# 框架提取候选 — FDA IOM 2026 Chapter 6: Imports

> 阶段 1「框架提取器」产出。用途：增量升级 `fda-pchf-food-safety` 技能包（企业合规/迎检导向）。

## 说明与约定

- **来源定位**：本书是监管机构内部 SOP 手册，不是方法论书籍。因此本文件的「框架」= 条件→判定的分流规则、按法定时限推进的处置链、字段级记录要求、多分支决策门。纯叙述性文字与系统界面点击步骤不予提取。
- **全量扫描**：已逐块读取 `.cangjie/index/` 下全部 10 个分块（6.1 / 6.2 / 6.3 / 6.4 / 6.5 / 6.6 / 6.7 / 6.8 / 6.9 / Exhibits-6-1-to-6-4）。Exhibits 6-1~6-4 为扫描表单，**无文本层**（仅含 "EXHIBIT 6-N" 与表单标题），无法提取字段，相关文书细节一律标注「需查原件」。
- **页码**：`[p.N]` 为印刷页码（物理页=印刷页码），与 `source/toc.txt` 一致。
- **引用规范**：每段英文原文引用 ≤100 词，附中文翻译；出处精确标注小节号 + 页码。
- **严禁虚构**：所有「判定步骤 / 判停条件」均可在上引原文或同章相邻小节逐句回溯。凡由 FDA 判定动作反推到企业侧迎检动作的内容，统一冠以前缀 **〔推导·非原书主张〕**，仅作下游能力卡参考，不代表 IOM 主张、也不构成法定义务（IOM 属机构裁量，非法条）。
- **硬时限/硬数字索引**：2/4/8 小时 Prior Notice（f08）、15/30 天 PN 上限与条件放行期（f08/f04）、10 工作日听证（f06）、30 天 redelivery（f04/f05/f11）、90 天出口销毁（f06）、10+5 工作日调查备忘录（f12）、24 小时撤消通知（f05）、15 工作日 483a 回应（f13）、3 工作日 DR2（f01 佐证）。

---

## f01 — 入境审查主决策门（May Proceed / 撤消 / 请求现场工作 / 请求扣留 / OGA 关闭）

- **类型**：framework / 多分支决策门（decision-gate）
- **出处**：IOM 6.2.2.2、6.2.2.2.1、6.2.2.2.2、6.2.2.2.3、6.2.2.2.6、6.2.5；[p.16–19]、[p.21]
- **原文引用（每段 ≤100 词）**：
  > "When the FDA's initial automated screening does not issue a 'May Proceed,' an entry reviewer must manually review it." — 6.2.2.2 [p.16]
  >
  > "You should issue a 'May Proceed' for an entry line if you can confirm it meets all regulatory requirements using the electronic information and documents, and you see no need to detain it or request field work." — 6.2.2.2.1 [p.17]
  >
  > "If a product appears non-compliant, you have two options: 1. Request field work. 2. Recommend detention to the Compliance Branch (CB)." — 6.2.5 [p.21]

  **中译**：
  > 「当 FDA 的初始自动筛查未签发『May Proceed』时，入境审查员必须对其进行人工审查。」
  > 「若你能依据电子信息与单据确认某 entry line 满足全部法规要求，且认为无需扣留、也无需请求现场工作，则应对该 line 签发『May Proceed』。」
  > 「若产品看似不合规，你有两个选项：1. 请求现场工作；2. 向 Compliance Branch 建议扣留。」
- **判定步骤**：
  1. 自动筛查（PREDICT）→ 若已发 May Proceed 则本轮终止；未发则强制人工审查。
  2. 决策前必须先审阅并考虑 PREDICT 风险分与 rule flags；分析风险、调查 Import Alert / DWPE、检索企业产品数据库、核对单据。
  3. 落入有限动作集：① 确认全部合规且无需扣留/现场 → **May Proceed**（终局性放行，可 rescind）；② 请求现场工作 LEX/FEX/SAM（须先更正数据、设 work type 与 PAF、非例行工作须在 Instruction Text 给清晰指令）；③ 向 Compliance Branch 提交扣留建议 DER/DTR（审查员不自行作出终局扣留）；④ OGA/OGI/OGC referral：他机关已拒绝/扣押时上传其处置证明后关闭 line（不作 FDA 可采性判定）；⑤ 撤消已误发的 May Proceed。
  4. 与 PREDICT 相悖的放行、请求扣留、请求现场工作三类决定，均须在 Remarks 写**具体理由**，禁止 "May Proceed" / "N/A" 等空泛备注。
- **判停条件**：May Proceed 发出即本轮审查终止（但可被撤消，且依 §304(d) 入境后仍可执法）；扣留建议提交 CB 后审查员动作终止，由 CB 作可采性终局决定；OGA referral 以「他机关处置证明已上传」为关闭前提。
- **跨章节佐证线索**（供 1.5 V1 跨域验证）：6.2.3.3 [p.20]（单据审查后二选一：DTR 或 work request；3 工作日未收到单据自动发 "Second and Final Request" DR2）；6.3.10.7 [p.32]（Next Steps 按 Exam Class 分流的同构决策门）；6.4.3 [p.35]（无法取样/查验→标注 May Proceed）；6.1.4.6.1 [p.8–9]（IFE：缺 IUC/A of C 或支持文件→更新+rescreen 或请求扣留；文件齐备→可发 May Proceed）；6.2.2.2.6 [p.19]（OGA referral 关闭 line）；6.1.6.2 [p.13]（Notice of FDA Action 按 entry line 状态逐次签发）；6.9.56 / 6.9.57（May Proceed、NOA 定义含听证权告知）。
- **〔推导·非原书主张〕企业侧映射**：申报数据（A of C、IUC、产品代码、制造商、数量）须在进入审查前自洽，任何更正都应留痕并可重新筛查；对 PREDICT 命中项预先备齐可采性证据，可缩短人工审查与现场工作概率。

---

## f02 — DER vs DTR 扣留建议的触发依据分流

- **类型**：framework / 触发依据分流（routing）
- **出处**：IOM 6.2.5、6.2.5.1、6.2.5.2、6.2.5.3、6.2.5.4；[p.21–22]
- **原文引用**：
  > "As an entry reviewer, you will use one of two work types to recommend detention: DER or DTR. DER (Detention without Physical Examination): Use DER when a product is subject to Detention without Physical Examination (DWPE). DTR (All Other Detentions): Use DTR for all other situations where a product appears to be violative." — 6.2.5.1 [p.21]

  **中译**：
  > 「作为入境审查员，你会用两种 work type 之一来建议扣留：DER 或 DTR。DER（无需实物查验扣留）：当产品受 DWPE 约束时使用。DTR（其他一切扣留）：用于产品看似违规的其他所有情形。」
- **判定步骤**：
  1. 疑似不合规 → 判断触发依据是「受 DWPE / Import Alert 约束」还是「其他疑似违规」。
  2. 受 DWPE → **DER**：仅当三条件全满足（电子数据与 IA 标准匹配、IA 不要求特定单据、无需额外信息）才可免单据直接提交；IA 要求特定文书（如 IA 28-02 印度黑胡椒须证书）时**必须**先索取并审阅单据再提交。
  3. 其他疑似违规 → **DTR**：先审阅全部可用信息（电子申报、内部数据库、filer 提交单据）；仍不足可再请求 FEX/SAM；匹配 IA 但信息不足时先取单据、更正数据并 rescreen，命中则按 IA 指引，不命中则继续初审并用 feedback 说明未适用性。
  4. 提交前须：查 Import Program 页产品特定说明、检索全部相关中心数据库、**全部研究写入 Remarks**、多违规须列全 IA 与 PAF；提交给 Compliance Branch。
  5. Pending Addition to DWPE：OII 有 direct reference authority 且电子申报与既往违规 entry 完全一致 → DER（Instruction Text 记既往发现、CMS/entry 号、IA 引用、证据）；无 direct reference authority → entry 独立成立，与主管及 CB 商议走单据或现场工作。
- **判停条件**：扣留建议提交 CB 即审查员动作终止；DER/DTR 不是严重度分级，而是**触发依据**的分流（BOOK_OVERVIEW 术语表亦如此定义）；不得仅凭「数据查询失败或 A of C 缺失」建议扣留（6.2.5.5），须尽职核实。
- **跨章节佐证线索**：6.2.5.3 [p.21–22]（DER-IA 免单据三条件 + IA 28-02 证书例 + 提交 3 步）；6.2.5.4.2 / .4.2.1 / .4.2.2 [p.22]（Pending DWPE 的 authority 分流）；6.2.5.5 [p.23]（注册/列名/批准不可核实时的建议扣留与「合理努力」义务）；6.3.10.5 [p.31]（Class 3 → 记录 Class 3 FEX/LEX 并提交 DTR + PAF）；6.9.20 / 6.9.21 / 6.9.22（DTR、Detention、DWPE 定义）；6.1.3 [p.6]（FDA 判定可否经重整达合规并授权）。
- **〔推导·非原书主张〕企业侧映射**：被列入 Import Alert / DWPE 时，举证重点是「本批与警报标准的差异证据」（品牌、剂型、制造商豁免等），对应 6.2.2.2 的 Clear Remarks 示例；未被列入但数据无法核实注册/列名/批准时，应预置 NDA/510(k)/PMA、注册列名等可核验证明。

---

## f03 — 数据完整性闭环：更正 → 指派责任方 → 保存 → rescreen

- **类型**：framework / 不变量门禁循环（gating loop）
- **出处**：IOM 6.2.1；[p.14]（并在 6.2 / 6.3 / 6.4 多处重复出现）
- **原文引用**：
  > "Correct any inaccurate data (manufacturer, shipper, product code, quantity, etc.) that could affect PREDICT screening. Assign fault to the responsible party. Save and rescreen the entry/line after making corrections." — 6.2.1 [p.14]

  **中译**：
  > 「更正任何可能影响 PREDICT 筛查的不准确数据（制造商、发货人、产品代码、数量等）。把责任指派给责任方。更正后保存并重新筛查该 entry/line。」
- **判定步骤**：发现影响 PREDICT 的数据错误 → ① 更正字段 → ② 记录更正原因 → ③ assign fault（指派责任方）→ ④ 保存 → ⑤ rescreen → ⑥ 观察 flags / 筛查命中是否变化 → 若变化，按新结果重新进入 f01 决策门。
- **判停条件**：rescreen 后无新增命中且 Line Details 字段齐备即停；此后所有判定必须建立在**更正后**数据之上，否则「后续所有判定建立在脏数据上」（BOOK_OVERVIEW 核心命题 2）。
- **跨章节佐证线索**（「同一结构跨章反复引用」的最强证据，供 V1）：6.2.2.2.3 第 1 步 [p.17]（请求现场工作前先更正+记录原因+保存+rescreen）；6.2.5.2 [p.21]（"All information in 'Line Details' must be accurate. Inaccurate data will affect PREDICT screening."）；6.2.5.3 第 1 步 [p.22]（DER 前更正并 rescreen）；6.2.5.4.1 [p.22]（匹配 IA 前先更正并 rescreen）；6.3.10 [p.30]（完成查验结果前 Review Line Details，改动须备注+指派+rescreen）；6.4.6 [p.35]（完成 SCR 前同一流程）；6.1.4.6.1 [p.8]（IFE 缺 IUC/A of C → 更新、记录原因、保存、rescreen）；6.4.7 [p.38]（SCR 更正一次、改 Quantity/Units/DescText 须重发 NOA）。
- **〔推导·非原书主张〕企业侧映射**：申报数据的每次更正都应能回答「改了什么 / 为什么改 / 谁的责任」，并预期更正会触发重新风险评分；企业侧自建申报数据的版本留痕，是迎检时复现 FDA 判定依据的前提。

---

## f04 — 条件放行期判停窗口（30 天，三事件先到者）

- **类型**：framework / 时限判停条件（time-bound stop condition）
- **出处**：IOM 6.2.4；[p.20]
- **原文引用**：
  > "CBP may conditionally release a product while it awaits an FDA admissibility decision. You must make this decision before the conditional release period ends. This period typically lasts for 30 days. It ends as soon as one of these things happens first: The FDA issues a 'May Proceed' notice. The FDA issues a notice of refusal. The 30-day period expires." — 6.2.4 [p.20]
  >
  > "The following actions do not extend the conditional release period: Requesting Documents (DRQ), Detention Requests (DTR or DER), Deficient Entry (DEF), Requesting Information (INF)." — 6.2.4 [p.20]

  **中译**：
  > 「CBP 可在等待 FDA 可采性决定期间对产品作条件放行。你必须在该条件放行期结束前作出决定。该期通常为 30 天。以下三者中最先发生者即令其结束：FDA 签发 May Proceed 通知；FDA 签发拒绝通知；30 天期满。」
  > 「以下动作不延长条件放行期：索取单据（DRQ）、扣留请求（DTR 或 DER）、缺陷申报（DEF）、索取信息（INF）。」
- **判定步骤**：CBP 条件放行（货交进口商控制但仍受 FDA 管辖、须保持可召回）→ 启动 30 天窗口 → FDA 必须在窗口内作出可采性决定 → 需延长则须在**首个 30 天内书面**通知进口商，且通知书须声明 FDA 将查验、取样或扣留该货 → 注意 DRQ/DTR/DER/DEF/INF **均不**产生延期效力。
- **判停条件**：May Proceed / Refusal / 30 天到期三者**任一先发生**即窗口永久关闭；且 May Proceed 或 IB Release 一旦发出，条件放行期**永久结束**，即便撤消也不重开（6.2.2.2.2、6.3.11）。
- **跨章节佐证线索**：6.9.13 / 6.9.41 [p.51 / p.55]（Conditional Release 定义：Entry/Immediate Delivery 须抵达后 15 日历日内申报；货物可移动但 CBP 可在 30 天内要求 redelivery；期间以 May Proceed 或拒绝结束）；6.2.2.2.2 [p.17]（撤消 May Proceed 后期间不重开）；6.3.11 [p.32]（IB Release 后期间结束、撤消不重开）；6.4.3 [p.35]（May Proceed 定义）；6.5.2.8 [p.41]（Refusal 后 90 天出口/销毁，与 30 天 redelivery 区分）；6.9.12 [p.51]（Consumption Entry 15 天缴税安排）；6.9.66 [p.57]（redelivery bond 为货值 3 倍）。
- **〔推导·非原书主张〕企业侧映射**：条件放行不等于「已合格」，企业在窗口内须保持货物 intact、可召回、账实可追；把 30 天当作内部可采性举证倒计时，而非等待期。

---

## f05 — May Proceed / IB Release 撤消程序（24 小时 + 30 天 redelivery 窗口）

- **类型**：framework / 可逆处置链（reversal SOP）
- **出处**：IOM 6.2.2.2.2、6.3.11；[p.17–18]、[p.32–33]
- **原文引用**：
  > "You should only rescind a 'May Proceed' in rare cases, such as when a product requires a compliance action. You must act immediately, as this action is not for routine examinations. Once you issue a 'May Proceed,' the conditional release period for that entry ends permanently. Even if you rescind the notice, the period does not reopen." — 6.2.2.2.2 [p.17]
  >
  > "Send an updated 'Notice of FDA Action' to the filer, importer, and consignee within 24 hours. Request a bond hold from CBP within 24 hours… Instruct CBP to demand redelivery if the shipment has already been distributed. Act quickly, as CBP has a 30-day window to issue this demand." — 6.2.2.2.2 [p.18]

  **中译**：
  > 「仅在罕见情形下（如产品需合规行动）才应撤消 May Proceed。必须立即行动，因为此动作不用于例行查验。一旦签发 May Proceed，该 entry 的条件放行期即永久结束；即便撤消通知，该期也不重开。」
  > 「在 24 小时内向 filer、进口商和收货人发送更新后的 Notice of FDA Action；在 24 小时内请求 CBP 作 bond hold……若货物已被分销，指示 CBP 要求 redelivery。行动要快，因为 CBP 发出该要求只有 30 天窗口。」
- **判定步骤**（6.2.2.2.2 七步）：① 取得主管批准 → ② 立即通知 filer 已撤消并重新作可采性决定 → ③ 24 小时内向 filer/importer/consignee 发更新 NOA → ④ 24 小时内请求 CBP bond hold 以防拒绝时的财务损失 → ⑤ 确认系统向 filer 发出「勿分销」ABI 码 → ⑥ 已分销则请求 CBP redelivery（30 天窗口）→ ⑦ 全程动作与沟通在 FDA Import System 留痕。6.3.11 的 IB Release 撤消为同构七步（24h NOA、24h 请求 CBP Unset/Hold bond 防止清算、ABI 码 "PGA Decision Rescinded-Do Not Distribute Product"、30 天从 IB Release 签发日起算、Entry Remarks/Misc Info 留痕）。
- **判停条件**：撤消仅限「需合规行动 / 误放行 / 新信息需重审」，明确**不得**用于例行或工作计划性查验取样；完成后该 line 回到新的可采性决定；条件放行期不重开；CBP 30 天窗口一过，FDA 即无法要求 redelivery（"Any delays compromise FDA's ability"）。
- **跨章节佐证线索**：6.3.11 [p.32–33]（Rescinding an IB Release，几乎逐条同构，含 30 天起算点差异）；6.2.4 [p.20]（期间结束）；6.9.13 [p.51]（redelivery 30 天）；6.4.3 [p.35]（May Proceed 定义）；6.5.2.11 [p.42]（Bond Action：放行前分销且无法 redelivery 即触发）；6.2.2.2.1 [p.17]（允许入境后仍可依 §304(d) 执法）。
- **〔推导·非原书主张〕企业侧映射**：收到撤消类 NOA / ABI「勿分销」码后应立即冻结分销并保全货物与单据；24 小时与 30 天是双方共同的时间压力点，企业内部应预置「放行后回溯」应急流程。

---

## f06 — 违规发现后的法定时限处置主链（Detained → 听证 → 重整 → 放行/拒绝 → 90 天出口销毁 → Bond Action）

- **类型**：framework / 法定时限处置主链（time-bound disposition chain）
- **出处**：IOM 6.5.1、6.5.2、6.5.2.1、6.5.2.2、6.5.2.7、6.5.2.8、6.5.2.9、6.5.2.10、6.5.2.11；[p.39–42]
- **原文引用**：
  > "If examination of the sample or other evidence indicates the article appears to be in violation and detention is the course of action chosen by the Division, the filer, owner, and consignee… are advised… by 'Notice of FDA Action - Detained.' … Ordinarily, the respondents are allowed 10 working days to appear. However, if for some compelling reason the Division determines ten (10) working days are insufficient, this time period may be extended." — 6.5.2.1 [p.39]
  >
  > "The 'Notice of FDA Action - Refusal of Admission' provides for the exportation or destruction of the shipment, under CBP supervision, within 90 days of the date of the notice… The FDA file remains open until the division receives notification indicating that the goods were either destroyed or exported." — 6.5.2.8 [p.41]

  **中译**：
  > 「若样品或其他证据的检验表明该物品看似违规，且 Division 选择扣留为处置方式，则以『Notice of FDA Action - Detained』告知 filer、所有人与收货人……通常允许应答方 10 个工作日到场。但若 Division 因某种令人信服的理由认定 10 个工作日不足，可延长该期限。」
  > 「『Notice of FDA Action - Refusal of Admission』规定货物须在 CBP 监督下、自通知日起 90 天内出口或销毁……在 Division 收到表明货物已被销毁或出口的通知之前，FDA 档案保持开放。」
- **判定步骤**（不可逆时间链，每步产物是下一步输入）：
  1. 查验/取样后**无违规** → Notice of Release，货物可准入（6.5.1）。
  2. **有违规**且 Division 选扣留 → Notice of FDA Action - Detained：列明 charge、指定听证地点，听证为与 Division 的非正式会议，**通常 10 个工作日**内到场（NOA 上 "Respond By"；有 compelling reason 可延长）。
  3. 应答（6.5.2.2）：亲自/代表/邮寄；可提交可采性证据、请求拒绝入境、提出有效重整方法或使产品脱离 FD&C Act 管辖的方法。
  4. 听证后放行（6.5.2.7）→ Notice of Release，标注 "LINES RELEASED AFTER DETENTION" 并说明改判理由；或拒绝（6.5.2.8）→ Notice of FDA Action - Refusal of Admission（charge 须与原 Detained 通知**逐字一致**），抄送 CBP。
  5. 拒绝后：**90 天内**在 CBP 监督下出口或销毁；沟通 CBP 签发 CBP 4647（Notice to Mark/Redeliver），上传 4647 至 entry/line；未收到处置通知则主动核查状态；监管费用走 FDA 790（6.5.2.9，含监督人时、分析人时、差旅、行政支持等 6 项，向 CBP 收取、FDA 分部不得收款）。
  6. Bond Action（6.5.2.11）：放行前分销且无法 redelivery，或已扣留拒绝却未依法销毁/出口 → 立即联系 CBP、调查、出具进口商在 redelivery bond 下的责任明细；CBP 一般不在 FDA 不完全同意时减免违约金（21 CFR 1.97(b)）。
- **判停条件**：链条**不在发出 Refusal 时结束**——FDA 档案直到收到销毁/出口证明才关闭；FDA 对公众健康的责任延续到违规品被销毁或出口为止（6.5.2.8 末句："until the violative article is either destroyed or exported"）。
- **跨章节佐证线索**：6.9.23 [p.52–53]（Detention and Hearing Process：举证须在听证期内提交，形式可为邮件/电话到正式会议）；6.9.44 [p.55]（Import Refusal：90 天内销毁或出口）；6.9.21 [p.52]（Detention：可经合规化释放，否则拒绝入境或扣押）；6.9.57 [p.56]（NOA 告知听证权与 charge）；6.9.75 [p.58]（Testimony 交 NOA 所列 compliance officer）；6.2.4 [p.20]（Refusal 结束条件放行期）；6.6.2 [p.42]（调查证据转 CBP 制裁 / OCI 刑事调查）；6.5.2.3–6.5.2.6 [p.40]（重整子链，见 f07）；6.5.2.9/6.5.2.10/6.5.2.11 [p.41–42]（费用、出口销毁核验、保证金）。
- **〔推导·非原书主张〕企业侧映射**：把「10 个工作日听证」当作举证硬截止，预先准备可采性证据包与重整预案；Refusal 后内部闭环应延续到销毁/出口证明归档，而非收到通知即结案。

---

## f07 — 改标/重整（Form FDA 766）条件满足与否的成败分流

- **类型**：framework / 合规条件门（compliance-gate）+ 文书举证
- **出处**：IOM 6.5.2.3、6.5.2.4、6.5.2.5、6.5.2.6；[p.40]
- **原文引用**：
  > "The FDA may authorize relabeling or other remedial action upon the timely submission of an 'Application for Authorization to Relabel or To Recondition Non-Compliant Articles,' (Form FDA 766)… After review of the application, FDA will notify the importer of its approval or disapproval. If approved the original application will be returned outlining the conditions to be fulfilled and the time limit within which to fulfill them will be noted." — 6.5.2.3 [p.40]
  >
  > "If the initial attempt at reconditioning is unsuccessful, a second attempt should not be considered unless a revised method of reconditioning shows a reasonable assurance of success." — 6.5.2.6 [p.40]

  **中译**：
  > 「FDA 可在及时提交『不合格品改标或重整授权申请』（Form FDA 766）后授权改标或其他补救行动……审阅申请后，FDA 将通知进口商批准或不批准。若批准，将退回原申请并列出须满足的条件及完成这些条件的时限。」
  > 「若首次重整尝试不成功，不应考虑第二次尝试，除非修订后的重整方法能合理保证成功。」
- **判定步骤**：及时提交 FDA 766（或函件 + 充分 bond；已备案的 redelivery bond 适用，**无需新 bond**）→ FDA 批准/不批准；批准则列明**条件 + 完成时限** → 完成后提交 Importer's Certificate（766 第 2 页）或告知完成 → FDA 可复核查验/取样（可由 FDA 或 CBP 依协议）或仅接受进口商声明；拍照 as warranted；Report of Investigator/Inspector 转相关 FDA 办公室。
  - **条件满足**（6.5.2.5）→ Notice of Release（"Released after Reconditioning"）；不合格部分（rejects）**仍须**在 FDA/CBP 监督下销毁或再出口，并**单独**出具 Refusal of Admission；FDA 可在批准中规定 rejects 只销毁不出口。
  - **条件未满足**（6.5.2.6）→ Notice of Refusal of Admission 发进口商/收货人/filer，抄送 CBP；第二次机会判据为「修订方法合理保证成功」。
- **判停条件**：初次重整失败即原则上终止第二次尝试；合格部分放行时不合格部分仍须单独处置并单独拒绝；**未经批准的自行整改不产生放行效力**（BOOK_OVERVIEW 术语表 Reconditioning 定义，属术语口径推导）；重整授权与监督是 FDA/CBP 职权，非企业自行返工。
- **跨章节佐证线索**：6.9.65 [p.57]（Reconditioning 定义）、6.9.68 [p.57]（Relabeling 是重整的一种）、6.9.75 [p.58]（Testimony：企业提交以支持放行）；6.1.3 [p.6]（FDA 判定可否经重整达合规并授权重整，监督由 FDA 或 CBP 按就近/远程约定，拒绝后出口销毁由 CBP 指挥）；6.5.2.9 [p.41]（FDA 790 监督费用）；6.5.2.4 [p.40]（复核可 FDA 或 CBP）；6.6.4.1 [p.43]（Failure to Hold 可在 "verification of a reconditioning" 环节发现）；6.9.66 [p.57]（redelivery bond 适用于改标/重整）。Exhibit 6-2（FDA 766 原件，无文本层，字段需查原件）。
- **〔推导·非原书主张〕企业侧映射**：整改方案应在首次提交时即论证「合理保证成功」并写明方法、时限与 rejects 处置；把 Importer's Certificate 与复核记录作为放行举证链的一环归档。

---

## f08 — Prior Notice 适用性机械判定（2/4/8 小时 + 15/30 天 + 豁免 + inadequate 后果）

- **类型**：framework / 适用性 + 硬时限门（eligibility / hard-time gate）
- **出处**：IOM 6.1.5、6.1.5.1、6.1.5.2、6.1.5.3、6.1.5.4、6.1.5.5、6.1.5.6；[p.9–12]
- **原文引用**：
  > "Prior notice for food articles subject to the rule must be received and confirmed electronically by the FDA no more than 15 calendar days before the anticipated date of arrival for submission made through the PNSI, and no more than 30 calendar days before the anticipated date of arrival for submission made through ABI/ACE, and, dependent on the mode of transportation below, no fewer than: Two hours before arrival by land by road; Four hours before arrival by air or by land by rail; Eight hours before arrival by water." — 6.1.5.1 [p.9]
  >
  > "Food that is imported or offered for import with inadequate prior notice is subject to refusal and holding at the port or in a secure storage facility." — 6.1.5.5 [p.11]

  **中译**：
  > 「受规则约束的食品的事先通知，须由 FDA 以电子方式接收并确认：经 PNSI 提交的，不得早于预计抵达日前 15 个日历日；经 ABI/ACE 提交的，不得早于预计抵达日前 30 个日历日；且依下列运输方式，不得晚于：公路陆运抵达前 2 小时；空运或铁路陆运抵达前 4 小时；水运抵达前 8 小时。」
  > 「事先通知不充分而进口或申报进口的食品，将被拒绝并在港口或安全储存设施扣留。」
- **判定步骤**：
  1. 判定是否为 §201(f)「food」（人/动物食用、含口香糖及成分）→ 查 6.1.5.2 须通报清单（膳食补充剂、婴儿配方、饮料、果蔬、水产、乳蛋、生鲜农产品、罐藏冷冻、烘焙零食糖果、活食用动物、动物饲料/宠物食品）。
  2. 查豁免清单（6.1.5.3）：个人抵达随带自用、抵达港内不离港即出口、USDA 专属管辖的肉/禽/蛋制品、个人住宅自制作为个人礼物寄送、维也纳外交关系公约第 27.3 条外交邮袋。
  3. 按提交渠道定**上限**（PNSI 15 天 / ABI-ACE 30 天），按运输方式定**下限**（公路 2h / 空运·铁路 4h / 水运 8h）；国际邮件须在寄出前收到并确认，包裹须附 FDA 接收确认。
  4. 15 项字段齐备（21 CFR 1.281：提交人/传送人、entry type、产品代码与品名数量、制造商/种植者、生产国、发货人、起运国、预计抵达、进口商/货主/最终收货人、承运人与运输方式、装运信息、曾被拒入境国家、邮寄信息等）。
  5. 流程（6.1.5.6）：自动电子筛查 → 必要时 DTA（24/7）人工复核 → 识别可能严重危害公共卫生的产品 → 结果传 CBP、DTA 可在口岸启动查验 → 合规者再进入 §801(a) 可采性审查（Import Systems 筛查是否需进一步评估，如 Import Alert）。
  6. inadequate → refusal + hold（港口/安全设施）。
- **判停条件**：以「FDA 电子**接收并确认**（received and confirmed）」且落在上下限窗口内为本前置义务完成点；inadequate 触发 refusal/hold，但**不限制** FDA 依 FD&C Act 采取其他行动（含食品安全检查）、也**不影响** CBP 依 19 USC 1595a(b) 评估处罚或其他执法。
- **跨章节佐证线索**：6.1.4.5 [p.8]（人工/纸面 entry 的 human food / animal food-feed 仍须事先通知，可经 PNSI）；6.1.6.1 [p.12]（FD3 / FD4 PGA flag 判定是否须 PN；FD3 可用 A of C 码 "PND" 申明豁免；FD1 可 Disclaim）；6.1.5.6 [p.11]（PN 流程与 §801(a) 衔接）；6.9.62 [p.57]（Prior Notice 定义）；6.9.13 / 6.9.41 [p.51 / p.55]（Entry/Immediate Delivery 15 日历日）；6.9.66 [p.57]（redelivery bond 3 倍货值）；6.1.7 [p.13]（VQIP 快速放行，仅 for cause 查验）。
- **〔推导·非原书主张〕企业侧映射**：把 2/4/8 小时与 15/30 天做成订舱/发货节点的硬校验，并保留 FDA 确认回执；PN 是独立于报关单的法定前置义务，不能用报关数据替代。

---

## f09 — 现场查验 Exam Class 三级分流 + 受限 Next Steps（含结果字段）

- **类型**：framework / 分类门（classification gate）+ 字段级记录
- **出处**：IOM 6.3.10、6.3.10.1–6.3.10.7、6.3.1；[p.30–32]、[p.23–24]
- **原文引用**：
  > "Class 1 – No Adverse Findings within Problem Area… Class 2 – Other Findings: Class 2 is intended to be used only for those situations that do not meet the definitions of Class 1 or Class 3… Class 3 – Adverse Findings within Problem Area: The product appears to be in violation… Further action must be taken under the specified problem area, i.e., sampled or referred to the compliance branch for final admissibility determination." — 6.3.10.5 [p.31]
  >
  > "If the exam was classified as Class 1, you will have the option to IB Release or Add Work. If the exam was classified as Class 2, you will have the option to IB Release, Refer to CB, or Add Work. If the exam was classified as Class 3, you will have the option to Refer to CB or Add Work." — 6.3.10.7 [p.32]

  **中译**：
  > 「Class 1 — 该问题领域内无不良发现……Class 2 — 其他发现：仅用于不符合 Class 1 或 Class 3 定义的情形……Class 3 — 该问题领域内有不良发现：产品看似违规……须在该指定问题领域采取进一步行动，即取样，或转 Compliance Branch 作最终可采性判定。」
  > 「若查验归为 Class 1，可选 IB Release 或 Add Work；Class 2 可选 IB Release、Refer to CB 或 Add Work；Class 3 可选 Refer to CB 或 Add Work。」
- **判定步骤**：物理查验（最少 5 个容器或依 CP 排程，容器须标识 FDA/分部缩写/日期/主检查员缩写）→ 比对 filer 单据、实物、电子申报 → 先 Review Line Details（产品代码、制造商、原产国、数量、价值、批号、货物位置，改动须备注+指派+rescreen）→ 填写结果字段：Date Completed / Location of Goods / Remarks / Summary / **Exam Class** / Record Time / Next Steps → 三级分流 → 按 Class 进入**受限**的 Next Steps 集合 → 若 FEX/LEX 发现违规，记录为 Class 3 FEX/LEX 并以 DTR + 相应 PAF 提交 compliance（如标签宣称需上市许可则 DTR/AAP）。
- **判停条件**：Class 1 在该 problem area 内不再采取进一步行动（可 IB Release、就**不同**问题领域取样或转 CB、或加 work type）；Class 3 必须在该 problem area 进一步动作；**不得对未实际物理查验的 line 报告查验结果**（6.3.10.5 注："it is inappropriate to record a field examination if no physical examination occurred"，应用 "Same Action As" 挂起待其他 line 分析结果）；LEX 固定记为 LEX、其余 FEX 须附 PAF，remarks 与 exam class 会被 compliance 用于可采性判定。
- **跨章节佐证线索**：6.3.1 [p.23–24]（LEX/FEX 记录规则、监管笔记字段、现场验收标准须严于 formal guideline、Class 2/3 须拍照）；6.2.2.2.3 [p.17]（审查员请求现场工作须设 work type/PAF、非例行须给 Instruction Text）；6.2.5.4 [p.22]（DTR 前可请求 FEX/SAM）；6.4.6 [p.35]（SCR 同样先 Review Line Details 并 rescreen）；6.2.1 [p.14]（备注须具体，禁 "May Proceed"/"N/A"）；6.1.8 [p.14]（Class 2/3 现场/标签查验须上传照片）；6.3.10.3/6.3.10.4 [p.30–31]（Remarks/Summary 不出现在 NOA 上）。
- **〔推导·非原书主张〕企业侧映射**：现场查验前的「单据—实物—电子申报三者一致」自检，可直接对位 6.3.1 与 6.3.2 的差异清单（over-labeling、制造商不符、无英文强制标签、批号/效期改动、数量差异、原产国标记），用于迎检预演。

---

## f10 — 进口取样与证据链（SCR 字段 + 照片标识 + SDI 官方封条 + May Proceed / Release 定义分流）

- **类型**：framework / 字段级举证链（evidence-chain / field spec）
- **出处**：IOM 6.4.3、6.4.6、6.4.6.1–6.4.6.9、6.4.9、6.1.8、6.5 开头 SDI 续文；[p.35–38]、[p.13–14]、[p.39]
- **原文引用**：
  > "For every sample collected, a corresponding electronic collection report must be completed in FDA Import Systems… You are responsible for making sure all fields in the Line Details screen are complete and correct." — 6.4.6 [p.35]
  >
  > "May Proceed: 'Product may proceed without FDA examination. FDA has made no determination the product complies with all provisions…' (No compliance decision has been made.) Release: 'The product is released after FDA examination…' (A compliance decision has been made.)" — 6.4.3 [p.35]
  >
  > "All photographic evidence (including photographs of labeling) must be identified with the following required information: entry/line number, collection/examination date, investigator's initials, a brief description of the photo, and numbering that allows future reviewers to determine if any pages or photos are missing." — 6.1.8 [p.14]

  **中译**：
  > 「每采集一份样品，都必须在 FDA Import Systems 中完成对应的电子采集报告……你有责任确保 Line Details 屏幕的所有字段完整且正确。」
  > 「May Proceed：『产品可在未经 FDA 查验的情况下继续。FDA 未认定该产品符合所有条款……』（未作合规判定。）Release：『产品在 FDA 查验后被放行……』（已作合规判定。）」
  > 「所有照片证据（含标签照片）都必须以下列必备信息标识：entry/line 号、采集/查验日期、调查员姓名缩写、照片简要描述，以及能让后续审阅者判断是否有页或照片缺失的编号。」
- **判定步骤**：取样前确认货物位置已知、批次可得、申报描述与发票一致（6.4.4）→ 进口样品一般**不需** official seal 或 702(b) 保留份（除非拟采取扣押/禁令/起诉）→ 逐字段完成 SCR：Date Collected / Episode / Submitted To / Quantity Collected / Units / DescText（子样数、每份重量/体积、产品描述、容器类型、批次、取样方法）/ Hand Ship（保存、制备、运输方式、子样标识、chain of custody）/ Remarks（特殊处理、依据的 guidance、分析指令、controls/photos）/ Record Time（0.1 小时=6 分钟进制）→ 照片用**政务配发设备**拍摄并逐张标识（打印件须把标识永久固定在照片**上下方**、不得直接贴在照片上）→ ADS 须记在**同一 entry/line** 并在 Remarks 引用原样号 → SDI 额外：Remarks 记录标签描述、样品容器加官方封条 FDA 415a、封条上采集人 ID（以便检出违规时启用 FDA 国内管辖权；6.5 开头 p.39）→ 无法取样/查验 → 标注 "May Proceed"（**未作合规判定**），区别于 "Release"（查验后**已作**合规判定）。
- **判停条件**：样品在 FACTS 被置为 "In Progress" 后 SCR 不得再更正，且一份 CR **只允许更正一次**（6.4.7）；若 Quantity Collected / Units / DescText 变更须**重发 NOA**，仅 Hand Ship / Remarks 变更则不需；SDI 样品工作类型记录后不得再加 hold 类工作，line 一经放行即关闭，全 entry 各行关闭则 entry 关闭。
- **跨章节佐证线索**：6.1.8 [p.13–14]（照片：政务设备、须清晰覆盖包装各面/标签/批号/整批/不良状况，上传后可删本地，Class 2/3、取样、扣留请求、销毁、重整、拒绝核验须上传）；6.2.2.2.3 [p.17]（请求 SAM 须给清晰指令）；6.5 开头 [p.39]（SDI 记录规范、放行后 line 关闭、violative 由 import compliance branch 跟进）；6.4.2.4 [p.34]（未取样/待审 line 在 NOA 中标注 "May Proceed"）；6.4.7 [p.38]（更新 SCR）；6.4.8 [p.38]（ADS 三种适用情形）；6.9.2 / 6.9.24 / 6.9.70（Additional Sample、DI Sample、SAM 定义）；6.6.1 [p.42]（affidavit 可用于记录取样事实）；6.3.10.3 [p.30]（查验 Remarks 记录样品/照片）；6.9.3 [p.50]（Affidavit 定义）。
- **〔推导·非原书主张〕企业侧映射**：企业侧对留样、标签、批号、运输温控与 chain-of-custody 的记录粒度，建议对齐 SCR 九字段与照片标识规则，以便在抽样检测争议中复现证据链；"May Proceed" 不等于合规认定，不应作为对外合规声明。

---

## f11 — Failure to Hold 判定与 8 步固定调查清单（含健康危害 / DWPE 加重、30 vs 90 天）

- **类型**：framework / 固定调查清单 + 加重分流（investigation checklist）
- **出处**：IOM 6.6.4.1、6.6.4.2、6.6.4.3；[p.43–44]
- **原文引用**：
  > "Failure to hold means that the goods have been distributed by the importer/consignee without an FDA release from import status. *Please note that this is defined as distribution without a release, not merely moving the goods outside of the port area." — 6.6.4.1 [p.43]
  >
  > "Form 4647 can be issued for the purposes of examination/sampling, not merely because of an FDA refusal. In such circumstances, the deadline for redelivery is 30 days, instead of the 90 days post-refusal." — 6.6.4.1 第 7 步 [p.43]

  **中译**：
  > 「Failure to hold 指货物在未获 FDA 从进口状态放行的情况下，已被进口商/收货人分销。请注意：其定义是『无放行而分销』，而不只是把货物移出港区。」
  > 「CBP 4647 可为查验/取样之目的签发，并非仅因 FDA 拒绝才签发。在此类情形下，redelivery 的期限为 30 天，而非拒绝后的 90 天。」
- **判定步骤**（6.6.4.1 八步，适用于**所有** Failure to Hold 案件）：① 收集 entry 单据（CBP 3461/7501、发票、装箱单、BOL）→ ② 收集并分析分销记录，确定分销 → ③ 确定谁授权分销（可能不止一个责任方）→ ④ 确定进口商是否知悉产品健康危害 → ⑤ 取得授权人关于为何分销的说明（①–⑤ 须落入一份或多份 affidavit）→ ⑥ 经 ORADSS 等检索进口商历史并与主管/compliance 讨论 → ⑦ 协调 CBP 签发 4647 红交货（若因查验/取样而非拒绝，期限 **30 天**而非拒绝后 **90 天**）→ ⑧ 核定 bond 类型与金额。
  - **加重 A**（6.6.4.2，直接证据的重大健康危害，如即食食品检出 Salmonella）：八步之外追加与主管、compliance、分部 Recall and Emergency Coordinator 协商，处理收货人追回/通知及公共警告。
  - **加重 B**（6.6.4.3，仅达 §801(a)「外观违规」标准的健康危害 / DWPE，如因沙门氏菌史被 DWPE 扣留的即食食品）：八步之外追加「是否取样分析」协商，以及同样的召回/通知/公共警告协商。
- **判停条件**：八步为所有该类案件的必做下限；判定关键在**「分销」而非「位移」**——位置变化本身不构成该违规；发现点可分布于初查、取样、审计取样、健康危害复核、重整核验、拒绝核验（chain 多点）；30 天与 90 天 redelivery 期限由「4647 的签发依据」决定，不可混用。
- **跨章节佐证线索**：6.9.30 [p.53]（Failure to Hold 定义并指向 6.9.66 redelivery bond）；6.9.73 [p.58]（Substitution 可能用于掩盖 Failure to Hold 并规避 CBP bond action）；6.6.4.4 第 3 步 [p.44]（Substitution 在判定前「一律按实际货物无 FDA 放行而分销」处理，回指 6.6.4.1）；6.5.2.11 [p.42]（Bond Action 两类触发）；6.2.4 / 6.3.11 [p.20 / p.32]（30 天 redelivery 窗口）；6.6.3 [p.43]（调查备忘录时限，见 f12）；6.9.3 / 6.9.75 [p.50 / p.58]（Affidavit、Testimony）；6.9.66 [p.57]（redelivery bond 3 倍货值）。
- **〔推导·非原书主张〕企业侧映射**：在 FDA 放行前保持货物 intact 且**不进入分销**（含内部调拨），是避免该违规的核心控制点；分销记录、授权链、健康危害知悉情况应可随时举证。

---

## f12 — 四类违规模式识别 + 10+5 工作日调查备忘录 + filer 历史分流

- **类型**：framework / 模式→制裁路由（pattern→sanction routing）+ 报告时限
- **出处**：IOM 6.6.2、6.6.3、6.6.4、6.6.4.5、6.6.4.6、6.6.4.6.1；[p.42–45]
- **原文引用**：
  > "An investigational memo with supervisory endorsement should be generated for all instances described under IOM 6.6.4, Import Violation Patterns. The memo should normally be provided to supervisory staff for endorsement within ten business days of the last investigational activity and endorsed by supervisory staff within five business days." — 6.6.3 [p.43]
  >
  > "If the filer has no history of filing erroneous entries to FDA, divisions should consider further training and or placing the filer back to phase 1 filing status and withhold a request to assess a broker penalty… If the filer has a history… and the filer continues to disregard FDA's attempts to provide guidance, train, and document guidance provided… the FDA should contact (CBP) to request that a broker penalty be assessed against the filer." — 6.6.4.6.1 [p.45]

  **中译**：
  > 「对 IOM 6.6.4『进口违规模式』所述的所有情形，都应生成带主管背书的调查备忘录。备忘录通常应在末次调查活动后 10 个工作日内提交主管背书，并由主管在 5 个工作日内完成背书。」
  > 「若该 filer 无向 FDA 错报的历史，分部应考虑进一步培训、和/或将其退回 phase 1 申报状态，并暂不请求对该 filer 评估报关行罚款……若该 filer 有错报历史，且持续无视 FDA 提供指导、培训与留痕的努力，FDA 应联系 CBP 请求对该 filer 评估报关行罚款。」
- **判定步骤**：识别规避链条行为 → 归入四类模式之一（Failure to Hold / Substitution / Importer Misdeclaration / Filer Misdeclaration；**可重叠、清单非穷尽**）→ 按模式收集证据（关键区分：importer misdeclaration = 进口商给 filer 的信息本身错/缺；filer misdeclaration = 进口商给对、filer 报错；**filer 是进口商代理人，进口商负最终责任**）→ 反复 filer 错报走 5 步（记录 filer 当时可得信息 → 标签/照片取证 → 取得 filer affidavit → 必要时取得 importer affidavit → 开展 Filer Evaluation）→ 按**历史**分流（无历史→培训/退回 phase 1、暂不请求 broker penalty；有历史且漠视指导→联系 CBP 请求 broker penalty）→ 末次调查活动后 **10 工作日**出 memo 报主管、主管 **5 工作日**内背书 → 背书后通知 Compliance Branch 作后续法规考量；未出 memo 则须告知 importer/broker 并按分部政策留痕。
- **判停条件**：memo 经主管背书并通知 CB 后本调查动作终止，证据转为 CBP 制裁（行政扣押、民事罚款、取消条件放行特权、bond action 含违约金/提高保额/单笔 bond）或 OCI 刑事调查的输入（6.6.2）；10+5 工作日为硬时限；OCI 仅在货物经 FDA 拒绝程序并应销毁、或经 CBP 行政扣押没收程序后，才可为证据目的取得产品，且**不因此改变** FDA 对货物的处置标准与流程。
- **跨章节佐证线索**：6.6.2 [p.42–43]（证据转 CBP Title 19 制裁 / OCI 刑事调查，且刑事证据可能性不改变处置标准）；6.6.1 [p.42]（affidavit 可用于记录查验/取样/拒绝跟进事实，Exhibit 6-5）；6.7 / 6.7.1 [p.45–46]（周期性 Filer Evaluation 监控申报数据准确性，依 SOP-000217，可跨 division 抽取 filer 的 lines）；6.6.4.1 [p.43]（Failure to Hold 8 步，见 f11）；6.9.34 / 6.9.35 / 6.9.47 [p.54–55]（Filer Evaluation、Filer Misdeclaration、Importer Misdeclaration 定义）；6.9.75 [p.58]（Testimony / affidavit 提交给 NOA 所列 compliance officer）；6.8（FSVP 为并行的进口商合规轨）。
- **〔推导·非原书主张〕企业侧映射**：进口商对 filer 申报数据负最终责任，应建立「给 filer 的信息—filer 实际申报」双向核对与留痕；对反复错报，企业的整改与培训记录会影响是否被建议 broker penalty。

---

## f13 — FSVP 检查链：准备 → 记录审查 → 483a 观察项 → T-EIR/EIR（含危害分析比对、VSI 分流、15 工作日回应）

- **类型**：framework / 检查链 + 观察项签发门（inspection→observation gate）
- **出处**：IOM 6.8.1.1、6.8.1.2、6.8.1.3、6.8.1.4、6.8.1.4.1、6.8.2、6.8.2.1、6.8.2.1.1、6.8.2.1.2、6.8.3、6.8.3.1.1；[p.46–50]
- **原文引用**：
  > "Verify the firm or person identified at entry is the 'importer,' as defined in 21 CFR 1.500, and that the imported food is subject to the FSVP regulation… Determine if the importer of the food is a manufacturer/processor or re-packer, and if they should be inspected under any other specific human or animal programs…" — 6.8.1.1 [p.46]
  >
  > "Compare your preliminary assessment of potential hazards to the importer's hazard analysis. If there are discrepancies, discuss with the importer to determine their reasoning behind the discrepancy." — 6.8.1.4.1 [p.47]
  >
  > "The FDA 483a should only be issued at the conclusion of the inspection… inform the importer that they should respond to the FDA 483a within 15 business days after the end-date of the inspection and that their response may impact FDA's determination of the need for follow-up action." — 6.8.2.1 [p.48–49]

  **中译**：
  > 「核实 entry 上标识的企业或个人是否为 21 CFR 1.500 所定义的『importer』，以及该进口食品是否受 FSVP 规则约束……判断该食品进口商是否为制造商/加工商或再包装商，以及是否应依其他特定人类或动物食品计划（如 PC 规则）接受检查……」
  > 「将你对潜在危害的初步评估与进口商的危害分析作比对。若存在差异，与进口商讨论以确定其差异背后的理由。」
  > 「FDA 483a 只应在检查结束时签发……告知进口商应在检查结束日后 15 个工作日内对 FDA 483a 作出回应，且其回应可能影响 FDA 对是否需要后续行动的判定。」
- **判定步骤**：检查前联系（FSVP 预检邮件模板 → 未提供电话或未回复则致电）→ 7 项核实（表明身份；核实 importer 定义与 FSVP 适用性；核实联系方式；判定是否 PC for Human/Animal Food 规则覆盖；判定是否种植者→Produce Safety 规则；核实 FSVP 记录是否在场、off-site 则须取回；判定是否需翻译并给合理时间）→ 准备（查 FSVP 检查史/投诉/产品合规史/境外供应商、确保覆盖最高风险产品；列进口食品+对应境外供应商清单；做**潜在危害初步评估**；判定是否 VSI 并在 T-EIR 记录其是否选择 VSI Modified Requirements；熟悉 21 CFR Part 1 Subpart L；确认培训）→ 现场：找到最负责人、出示证件、说明目的、签发 FDA 482d（初始检查附 FSVP 教育材料）→ 记录审查：逐产品验证 importer 定义、**比对初步危害评估 vs 进口商危害分析**、差异追问理由、无 FSVP 时判断是否已有等效记录、公共卫生关切（如 Salmonela 阳性）则核查并取证纠正措施 → 483a 仅在结束会签发 → 15 工作日回应 → T-EIR/EIR 报告 + CARS 记录纠正措施。
- **判停条件**：483a **只在检查结束（closeout）时签发且只签已签名版**，检查期间不得向管理层展示任何草稿/未签版/屏幕电子稿；观察项须「显著且与被检查产品相关、按显著性排序、清晰具体、字迹清晰」，存疑重要性的观察项**不列入** 483a（当场讨论并记 T-EIR）；纠正措施**不写**在 483a 上而报在 T-EIR；若 importer 不满足定义，须在 T-EIR 说明并取得实际进口商信息；仅收集支持观察项的证据。
- **跨章节佐证线索**：6.8.1.2 [p.46–47]（准备含初步危害评估、VSI 判定）；6.8.3.1.1 [p.50]（EIR 须记录危害分析比对结果、importer 定义三种证明：owner/consignee 附订单等证明、U.S. agent/representative 附书面协议、不满足定义则说明并取实际进口商信息；纠正措施及预计完成日期记 CARS）；6.8.2.1.1 / .1.2 [p.49]（483a 逐字段抬头、签署政策）；6.8.1.3 [p.47]（记录审查权依 §805、21 CFR 1.510/1.512）；6.9.37 / 6.9.40 [p.54–55]（FSVP、FSVP/HACCP Importer 定义——与用户既有 HACCP/预防控制工作的衔接锚点）；6.9.23 [p.52]（听证举证，可作「举证时限」类比）；6.6 [p.42–45]（并行的进口调查轨）；6.2.4 [p.20]（货物准入与 FSVP 记录审查是不同轨，勿混同）。
- **〔推导·非原书主张〕企业侧映射**：FSVP importer 应预先备齐「importer 身份三类证明 + 逐食品 FSVP 计划 + 危害分析 + 境外供应商验证记录 + 纠正措施记录」；危害分析须能解释与监管方初步评估之间的任何差异；483a 的 15 工作日回应窗口应纳入内部 CAPA 时限。

---

## 覆盖自检（提交前）

- [x] 全量扫描 10 个分块：6.1 / 6.2 / 6.3 / 6.4 / 6.5 / 6.6 / 6.7 / 6.8 / 6.9 / Exhibits-6-1-to-6-4 均已逐块读取。
- [x] Exhibits 6-1~6-4 无文本层，仅记录事实并在 f06/f07 标注「表单字段需查原件」。
- [x] 共 13 条候选（f01–f13），每条均有小节号 + `[p.N]` 出处、英文引用 ≤100 词/段 + 中译、判定步骤、判停条件、跨章节佐证线索。
- [x] 每条均在原文中有依据；判定步骤/判停条件不虚构；企业侧内容全部冠以「〔推导·非原书主张〕」并声明其法律位阶限制。
- [x] 硬时限/硬数字全覆盖：2/4/8h、15/30 天（f08）、15/30 天条件放行（f04）、10 工作日听证（f06）、30 天 redelivery（f04/f05/f11）、90 天出口销毁（f06）、10+5 工作日 memo（f12）、24 小时撤消（f05）、15 工作日 483a（f13）、3 工作日 DR2（f01 佐证）。
- [x] 未提取纯叙述性文字、系统界面点击步骤、内部 Job Aid / SOP 编号清单、法条编号罗列。
- [x] 覆盖盲区说明：6.3.3–6.3.9 各产品类别查验要点为**并列列举性清单**，按 BOOK_OVERVIEW「不适合 skill 化」建议不独立成框架，仅作为 f09 的 example/佐证；6.9 术语定义主要由 glossary-extractor 承接，本文件仅取其为跨章节佐证；VQIP（6.1.7）为快速放行例外、非独立判定框架，并入 f08 佐证。
