# 事先通知（Prior Notice）适用性硬时限判定（prior-notice-eligibility-gate）

*来源分层与定位：IOM 2026 Ch.6 是 FDA 内部操作指导（Investigations Operations Manual，OII 机构 SOP），不是法规，不创设企业义务；与 IOM Ch.4（取样全流程）、IOM Ch.5（检查员权限与 483）、CP 7303.878（FSVP 检查）、CP 7303.050（取样量）分层，不得混引。本卡只落在 IOM 6.1.5（Prior Notice 的适用性、硬时限、豁免与 inadequate 后果）及 6.1.4.5 / 6.1.6.1 / 6.1.5.6 / 6.1.7 / 6.9.62 / 6.9.13 / 6.9.41 的口径衔接。本卡判定对象是**运输方式 × 提交渠道的时限窗与豁免适用性**，产物是「合规 / inadequate → refusal + hold」；不判定产品是否可采（V01）、不判法律位阶与可主张性（V10）、不涉及危害分析、供应商批准或记录保存（包内既有 PCHF 类 CAP）。2/4/8 小时与 15/30 天是可机械判定的硬约束，与既有 CAP-01…28 几乎不重叠；但适用面限食品/动物饲料，故 importance 为 high 而非 critical。*

## R — 原文

> "Prior notice for food articles subject to the rule must be received and confirmed electronically by the FDA no more than 15 calendar days before the anticipated date of arrival for submission made through the PNSI, and no more than 30 calendar days before the anticipated date of arrival for submission made through ABI/ACE, and, dependent on the mode of transportation below, no fewer than: Two hours before arrival by land by road; Four hours before arrival by air or by land by rail; Eight hours before arrival by water."
> —— IOM 6.1.5.1 [p.9]
> "In addition, prior notice must be received and confirmed electronically by FDA before food is mailed by international mail. (The parcel must be accompanied by confirmation of FDA receipt of prior notice.)"
> —— IOM 6.1.5.1 [p.9]
> 中文自译：受规则约束的食品，其事先通知须由 FDA **以电子方式接收并确认**：经 PNSI 提交的，不得早于预计抵达日前 **15 个日历日**；经 ABI/ACE 提交的，不得早于 **30 个日历日**；且依运输方式**不得晚于**——公路陆运抵达前 2 小时、空运或铁路陆运 4 小时、水运 8 小时。此外，经国际邮件寄出的食品，须在**寄出前**由 FDA 电子接收并确认，且包裹须随附 FDA 接收确认回执。上限与下限构成双向窗口，早于上限提交同样不合规。

> "Food that is imported or offered for import with inadequate prior notice is subject to refusal and holding at the port or in a secure storage facility. The FDA provided guidance to its stakeholders and CBP staff on enforcing such prior notice requirements in its Compliance Policy Guide... This guidance, however, does not limit the FDA's ability to take actions that may be necessary, including conducting inspections for food safety and security concerns, or taking any other action under the FD&C Act. This policy will also not affect the ability of CBP to assess penalties under 19 U.S.C. 1595a(b) or to take enforcement action under any other authority."
> —— IOM 6.1.5.5 [p.11]
> 中文自译：事先通知不充分而进口或申报进口的食品，将被**拒绝并在港口或安全储存设施扣留**。FDA 曾在 Compliance Policy Guide 中就该要求的执行向利益相关方与 CBP 人员提供指导，但**该指导并不限制** FDA 采取必要行动的权力（含为食品安防顾虑实施检查、或依 FD&C Act 采取其他行动），也**不影响** CBP 依 19 U.S.C. 1595a(b) 评估罚款或依其他授权执法的权力——即指导文件不构成豁免。

> "Foods that are excluded from the prior notice requirement include: Food carried by, or otherwise accompanying, an individual arriving in the United States for that individual's personal use... Food that is exported without leaving the port of arrival until export. Meat products, poultry products, and egg products that are subject to the exclusive jurisdiction of the U.S. Department of Agriculture (USDA)... Food made by an individual in their personal residence and sent by that individual as a personal gift (that is, for non-business reasons) to an individual in the United States. Articles of food subject to Article 27.3 of the Vienna Convention on Diplomatic Relations (1961)."
> —— IOM 6.1.5.3 [p.10]
> 中文自译：豁免共 5 类：个人抵达时随身携带、供本人/家人/朋友食用且非销售分发的食品；抵达港内不离港即原状出口的食品；USDA 专属管辖的肉/禽/蛋制品；**个人在其住所自制、由该个人作为非商业性个人礼物**寄给美国境内个人的食品；《维也纳外交关系公约》（1961）第 27.3 条所涉物品（如外交邮袋）。「个人礼物」豁免的主体要件是「个人、住所自制、非商业」，企业规模化生产不适用。

> "Note: If the product being offered for manual entry is a human food or animal food/feed, prior notice filing is still required in advance of its arrival in the United States (IOM 6.1.5). For non-electronic entry filings, prior notice can be submitted through FDA's Prior Notice System Interface (PNSI)."
> —— IOM 6.1.4.5 [p.8]
> "FD3: Entries covered by an FD3 flag may be subject to prior notice under section 801 (m) of the FD&C Act and 21 CFR Part 1, subpart I... The filer may... specify the entry is not subject to prior notice and 'Disclaim' the entry. If the product is an FDA-regulated product, but not a food, the entry can be disclaimed from prior notice by using the affirmation of compliance code 'PND' in the entry." / "FD4: Entries covered by an FD4 flag may be 'food' for which prior notice is required... Entries covered by FD4 flag must include prior notice required information."
> —— IOM 6.1.6.1 [p.12]
> 中文自译：人工/纸面（non-ABI / manual）entry 的人用或动物用食品/饲料，**仍须**在抵达前提交事先通知（可经 PNSI）——PN 义务独立于报关方式。在申报数据层，「是否需 PN」落实为 CBP 的 PGA flag：FD3 可能须 PN、可用 A of C 码 **PND** 申明豁免/Disclaim；FD4 则必须包含 PN 所需信息。

> "Food that meets prior notice requirements will be subject to further review by FDA staff for admissibility determination under section 801(a) of the FD&C Act. The FDA Import Systems screening will determine if further evaluation of the article of food is necessary (for instance, subject to the guidance in an import alert)."
> —— IOM 6.1.5.6 [p.12]
> "The Voluntary Qualified Importer Program (VQIP) is a voluntary, fee-based program that provides expedited review and import entry of human and animal foods into the United States for participating importers who must meet eligibility criteria and pay a user fee... The FDA limits its examination and/or sampling of VQIP food entries to 'for cause' situations..."
> —— IOM 6.1.7 [p.13]
> "In the case of an article of food that is being imported or offered for import into the United States, a notice provided to the FDA prior to entry in the United States, with information about the article, manufacturer, shipper, grower, the country of origin, and anticipated port of entry. Prior notice must be submitted to the FDA electronically, via either the CBP Automated Commercial Environment (ACE) or the FDA Prior Notice System Interface (FDA PNSI)."
> —— IOM 6.9.62 [p.57]
> 中文自译：满足 PN 要求的食品**还要**再经 FDA 依 FD&C Act §801(a) 作可采性审查（Import Systems 筛查是否需进一步评估，例如是否受 Import Alert 指引）——两道门互不替代。VQIP 是**自愿、付费的加速审查**计划，须符合资格并缴费，FDA 仅保留 "for cause" 查验/取样，它不是合规认证、不是免检、也不豁免 PN。术语表把 PN 定义为**发给 FDA、先于入境**并经 ACE 或 PNSI 电子提交的通报。

> "For purposes of prior notice requirements, 'food' is defined by Section 201(f) of the FD&C Act [21 U.S.C 321(f)] as articles used for food or drink for man or other animals (including chewing gum) and articles used for components of any such articles."
> —— IOM 6.1.5.2 [p.9]
> "The prior notice must be submitted electronically and contain the following information, in accordance with 21 CFR 1.281: 1. Identification of the submitter... 4. The identification of the article of food, including complete FDA product code... 15. The anticipated date of mailing, and beginning October 1, 2026, the name of the mail service and the mail tracking number..."
> —— IOM 6.1.5.4 [p.10]
> "Entry/Immediate Delivery must be filed within 15 calendar days of arrival of goods in the United States." / "Entry/Immediate Delivery (CF 3461) must be filed within 15 calendar days of arrival of goods in the United States."
> —— IOM 6.9.13 [p.51]、IOM 6.9.41 [p.55]
> 中文自译：适用对象按 FD&C Act §201(f) 界定为「人或其他动物食用/饮用之物（含口香糖）及其成分」，清单另列膳食补充剂、婴儿配方、饮料、果蔬、水产、乳蛋、生鲜农产品、罐藏冷冻、烘焙零食糖果、活食用动物、动物饲料/宠物食品等。提交内容依 21 CFR 1.281 共 15 项（提交人/传送人识别、entry type、产品代码与品名数量、制造商/种植者、生产国、发货人、起运国、预计抵达、进口商/货主/最终收货人、承运人与运输方式、装运信息、曾被拒入境国家、邮寄信息等）。注意两个「15 天」同数异义：本卡 15 天是 **PN 提交上限**，6.9.13 / 6.9.41 的 15 天是 **CBP Entry/Immediate Delivery 申报义务**，不可混算。

**引文覆盖对照（verified.md V03 `source_evidence` 关键口径 → R 组）**

| source_evidence 关键口径 | 落点 |
|---|---|
| 6.1.5.1 [p.9] 15 天（PNSI）/ 30 天（ABI-ACE）上限、2h 公路 / 4h 空铁 / 8h 水运下限 | 组 1 |
| 6.1.5.1 [p.9] 国际邮件须寄出前 received and confirmed、包裹附 FDA 接收确认 | 组 1 |
| 6.1.5.5 [p.11] inadequate → refusal and holding；CPG 指导 does not limit FDA / will not affect CBP | 组 2 |
| 6.1.5.3 [p.10] 5 类豁免 | 组 3 |
| 6.1.4.5 [p.8] manual/paper entry 的人用或动物用食品仍须 PN（可经 PNSI） | 组 4 |
| 6.1.6.1 [p.12] FD3/FD4 PGA flag 判定是否须 PN；FD3 可用 A of C 码 PND 申明豁免 | 组 4 |
| 6.1.5.6 [p.12] PN 合规后仍须 §801(a) 可采性审查；6.1.7 [p.13] VQIP 不豁免 PN | 组 5 |
| 6.9.13 [p.51] / 6.9.41 [p.55] 两个「15 天」同数异义 | 组 6 |
| V1 跨域佐证：6.1.5.4 [p.10-11] 15 项要素 / 21 CFR 1.281；6.1.5.2 [p.9-10] §201(f) food 清单 | 组 6 / Step 3 |

**本卡反直觉口径清单（V3 机构特定校准，非聪明人常识）**
1. 完成点是「FDA 电子**接收并确认**（received and confirmed）」，不是「已提交」——缺确认回执即 inadequate。
2. 15/30 天是**上限**、2/4/8 小时是**下限**，双向窗口；早于上限提交同样不合规。
3. Prior Notice 是发给 FDA、独立于报关单的法定前置义务，不能用报关数据或 ACE 字段替代；纸质/manual entry 亦然。
4. 两个「15 天」同数异义：PN 上限 vs CBP Entry/Immediate Delivery 申报义务（6.9.13 [p.51] / 6.9.41 [p.55]）。
5. VQIP 是付费加速审查资格，不是合规认证、不是免检，不豁免 PN。
6. inadequate 不限制 FDA 其他行动、也不影响 CBP 处罚权——指导文件不构成豁免。
7. 国际邮件不走抵达前 2/4/8 小时，而是「寄出前确认 + 包裹附回执」——渠道一换，口径整体切换。
8. 豁免只是「不适用 PN 要求」，不等于免除 §801(a) 可采性审查；「个人礼物」豁免的主体要件是「个人、住所自制、非商业」，企业规模化生产不适用。

## I — 自述

这套方法判的是一道「前置闸」，不是产品能不能进。先问两件事：这东西是不是 FD&C Act §201(f) 意义上的 food（含动物饲料），以及是否落在 5 类豁免里；只有「是 food 且不豁免」才进入时限计算。

时限是**双向窗口**，不是「越早报越好」。上限由提交渠道决定（PNSI 15 个日历日 / ABI-ACE 30 个日历日），下限由运输方式决定（公路 2 小时、空运与铁路 4 小时、水运 8 小时）。早于上限提交与晚于下限提交同样不合规——「早点报总没错」在这里是错的。

完成点也不是「已提交」，而是「FDA 电子**接收并确认**（received and confirmed）」。缺确认回执即属 inadequate。国际邮件走的是另一套口径：不是抵达前 2/4/8 小时，而是**寄出前**须经 FDA 确认，且包裹必须随附确认回执。渠道一换，时限口径整体切换，这是最容易漏算的一处。

还有一层独立性：PN 是发给 FDA、有确认回执的**法定前置义务**，只是可以搭 ACE 通道传输，不等于报关单的一个字段；纸质/manual entry 的人用或动物用食品仍须提前通报（可经 PNSI）。在申报数据层，「是否需 PN」被落实为 FD3 / FD4 PGA flag，豁免可经 A of C 码 PND 申明——义务从法条落到字段，但字段判定不替代义务本身。

后果是刚性的：inadequate → rejection + 在口岸或安全设施 hold，且结论不是「补报即可」。企业援引 CPG 指导主张宽限无效，原文明确该指导 does not limit FDA 依 FD&C Act 采取行动的权力、也不影响 CBP 依 19 U.S.C. 1595a(b) 处罚。

最后要守住「两道门」：PN 合规只是过完第一道，食品仍须再走 §801(a) 可采性审查（V01 的决策门）。VQIP 是付费加速审查资格，不是合规认证、不是免检，也不豁免 PN。豁免清单也只是「不适用 PN」，不等于免除后续可采性审查。

## A1 — 书中用法

**情景一：企业经国际邮件寄送自家工厂生产的肉松烘焙零食，声称「个人礼物」主张豁免（IOM 6.1.5.3 [p.10]、IOM 6.1.5.1 [p.9]、IOM 6.1.5.5 [p.11]、IOM 6.1.5.6 [p.12]；V2 预测题）**
- 问题：能否按「个人礼物」豁免 PN；若不适用，时限是否按抵达前 2/4/8 小时算。
- 动作：核对豁免主体要件——6.1.5.3 的「个人礼物」要求「个人在**其住所自制**、作为非商业个人礼物寄送」，企业规模化生产不适用；且该豁免与「个人抵达随身携带」是两类，邮寄不自动落入。再按 6.1.5.1 切到国际邮件口径：须在**寄出前**由 FDA 电子接收并确认，包裹须随附确认回执。
- 判定/后果：两项主张都不成立。无确认回执 → inadequate → 拒绝并在口岸/安全设施扣留（6.1.5.5）；企业援引 CPG 指导主张宽限无效，因该指导不限制 FDA 依 FD&C Act 行动、也不影响 CBP 依 19 U.S.C. 1595a(b) 处罚。即便 PN 合规，该食品仍须再走 §801(a) 可采性审查（6.1.5.6）。结论不是「补报即可」，而是直接 refusal + hold。

**情景二：人工/纸面（manual / non-ABI）entry 的人用或动物用食品（IOM 6.1.4.5 [p.8]；case 交叉点）**
- 问题：不走 ACE 电子申报的食品，是否还要单独提交 Prior Notice。
- 动作：按 6.1.4.5 注确认「仍须在抵达前提交」，可经 FDA PNSI 提交；时限仍按 6.1.5.1 的渠道/运输方式窗口判定。
- 判定/后果：PN 义务**独立于报关方式**，不能因「纸质报关、没有 ACE 字段」而免除。这是最易被忽略的交叉点：把 PN 当成报关单附属项会漏掉整条前置义务。

**情景三：FD3 / FD4 flag 与 PND 码的申报判定（IOM 6.1.6.1 [p.12]）**
- 问题：系统里如何体现「这批是否需 PN」。
- 动作：FD3 flag 表示可能须 PN（如食品与非食品两用），filer 可依进口商提供的用途信息 Disclaim，或以 A of C 码 **PND** 申明「非食品、不适用 PN」；FD4 flag 表示可能是须 PN 的 food，**必须**包含 PN 所需信息。
- 判定/后果：「是否需 PN」从法定义务落到申报字段，但字段申明不替代义务本身；FD4 缺 PN 信息即 inadequate。本情景是 6.1 的申报判定，**不是 6.2 的审查动作**（见 A2 与 V01 的分流）。

**情景四：PN 提交后的自动筛查与 DTA 人工复核（IOM 6.1.5.6 [p.11-12]）**
- 问题：PN 提交后由谁审、结果怎么用、合规后是否结束。
- 动作：先经自动电子筛查，必要时由总部 Division of Targeting and Analysis（DTA，24/7）人工复核，识别可能严重危害公共卫生的产品；结果传 CBP，DTA 可在抵达口岸（铁路则在最近合适查验点）启动 FDA/CBP 查验，并负责与提交人沟通合规、因 PN 不足或未注册境外制造商而启动的拒绝/扣留、复核请求与流程完成。审查过程不受电子提交方式影响。
- 判定/后果：PN 合规者仍进入 §801(a) 可采性审查（Import Systems 筛查是否需进一步评估，如 Import Alert）——PN 门与可采性门是两道，互不替代；本卡只到第一道为止。DTA 的查验启动权属 FDA 侧作业，不构成对企业的新义务。

**情景五：VQIP 企业 / 把两个「15 天」混算（IOM 6.1.7 [p.13]、IOM 6.9.13 [p.51]、IOM 6.9.41 [p.55]）**
- 问题：已获批 VQIP 的食品能否跳过 PN；或把 PN 上限 15 天与 CBP 报关 15 天当同一时限。
- 动作：VQIP 是自愿、付费、须有 approved application 且 PREDICT 设识别规则的**加速审查**资格，FDA 仍保留 for cause 查验/取样、统计性微生物取样与审计 VQIP 有效性的权利；CBP 的 Entry/Immediate Delivery 15 天是货物抵达后申报报关单的义务，与「抵达前 PN 上限」方向相反、主体不同。
- 判定/后果：VQIP 不豁免 PN，也不是合规认证/免检；两个 15 天不可合并计算或相互抵扣，误用会使窗口判定整体错误。QAP（6.9.76 [p.58]）只是 VQIP 要求的书面政策与程序汇编，文件齐备 ≠ 已获批。

## A2 — 未来触发 ★

**触发场景（3–5 条）**
1. 判断某批食品/动物饲料是否须提交 Prior Notice、是否落在 5 类豁免清单内（尤其「个人礼物」「随身自用」的主体要件）。
2. 按运输方式与提交渠道计算合法时间窗：15/30 天上限、2/4/8 小时下限，或判断「提前 20 天经 PNSI 提交」是否合规。
3. 「已提交但没拿到 FDA 确认回执」是否算合规；或国际邮件、随行李携带、外交邮袋等特殊情形该套哪套口径。
4. inadequate prior notice 的后果，以及 CPG 指导、VQIP 资格是否构成宽限/豁免。
5. 判断 PN 合规之后是否还有下一道门（§801(a) 可采性审查），或区分 PN 的「15 天」与 CBP Entry/Immediate Delivery 的「15 天」。
6. 〔推导·非原书主张〕企业侧想把 2/4/8 小时与 15/30 天做成订舱/发货节点的硬校验、理解为何要保留 FDA 确认回执——这是从 FDA 判定动作反推的理解，非手册主张。

**语言信号（中英双写）**
- 中文：「要不要做事先通知」「提前多久报」「2/4/8 小时」「15 天还是 30 天」「早点报行不行」「已经提交了算不算」「没收到确认回执」「国际邮件怎么算」「个人礼物能不能免」「VQIP 能不能免」「食品/饲料」「inadequate 会怎样」「CPG 指导有没有宽限」「报关时一起填不行吗」
- English: "Prior Notice", "PNSI", "ABI/ACE", "received and confirmed electronically", "no more than 15 calendar days", "no more than 30 calendar days", "no fewer than 2 / 4 / 8 hours", "international mail", "confirmation of FDA receipt", "inadequate prior notice", "refusal and holding", "secure storage facility", "exemptions / excluded from prior notice", "section 201(f) food", "21 CFR 1.281", "FD3 / FD4 PGA flag", "A of C code PND", "VQIP", "section 801(a) admissibility", "Compliance Policy Guide does not limit"

**与相邻能力的区分（依 verified.md differentiator）**
- 本卡判定对象是**运输方式 × 提交渠道的时限窗与豁免适用性**，产物是「合规 / inadequate → refusal + hold」；不判定产品是否可采（V01）、不判法律位阶（V10）、不涉及危害分析或供应商验证（包内既有 PCHF 类 CAP）。
- 与包内既有【危害分析 / 供应商批准 / 记录保存】类 CAP：可能在「发运前置校验」上抢路由。本卡只管**发给 FDA 的法定前置通报是否落在时限窗内**，不管产品危害、供应商资质或企业记录体系。
- 与 **V10（效力层元规则）**：x13 以 6.1.5.5 为原文锚点，可能抢「指导文件是否构成豁免」路由。本卡只在**后果侧**引用「CPG 指导 does not limit」这一原文事实；「该结论的法律位阶与可主张性」由 V10 判定，本卡不下位阶结论。
- 与 **V01（入境审查决策门）**：6.1.6.1 的 FD3/FD4 flag 是 **6.1 申报字段判定**，不是 6.2 电子审查动作；PN 合规后进入的 §801(a) 可采性审查才归 V01。用户问「这条 line 放不放行」→ V01，问「要不要 PN / 时限多少」→ 本卡。
- 与 **CAP-17（CP 7303.050 取样量）/ CAP-28（IOM Ch.4 取样全流程）/ CAP-18（IOM Ch.5 检查员权限与 483）/ CAP-21（CP 7303.878 FSVP 检查）**：四者分别落在现场取样、取样执行、现场检查观察项、进口商记录审查，均不落在 6.1.5 的时限与豁免判定；不得因「食品/发运前置」字样混引。尤其 FSVP 是对进口商记录的独立合规轨，与 PN 的「发给 FDA 的抵达前通报」不是同一义务。
- 与 **V09（状态概念树）/ V04（时间窗）**：本卡的 15/30 天与 2/4/8 小时是**抵达前的 PN 窗口**，与条件放行期 30 天、CBP redelivery 30 天、拒绝后 90 天等窗口完全不同源，不可混算。

## E — 执行步骤

**E 段总览（输入 → 输出 → 交棒）**
- 输入：一批拟入境的食品/动物饲料 + 运输方式 + 提交渠道 + 预计抵达/寄出时间 + FDA 确认回执 + 15 项申报要素 + 豁免主张。
- 输出：适用性结论（food / 豁免）+ 双向窗口判定 + 完成点判定（received and confirmed）+ 「合规 / inadequate → refusal + hold」。
- 交棒：PN 合规后进入 §801(a) 可采性审查 → V01 决策门；法律位阶与可主张性 → V10；危害分析/供应商验证/记录保存 → 包内既有 PCHF 类 CAP。
- 全程硬约束：两个「15 天」分开登记；国际邮件切换独立口径；任何结论须回当前版本 21 CFR 1.281 与 IOM / RPM 复核；本卡不据 IOM 单独对企业下义务。

**Step 1 — 适用性判定（是不是 food、落不落豁免）**
- 动作：按 6.1.5.2 [p.9] 的 §201(f) 定义与 6.1.5.2 [p.9-10] 清单判是否为人用/动物用食品或饲料（含口香糖、膳食补充剂、婴儿配方、饮料、果蔬、水产、乳蛋、烘焙零食、活食用动物、宠物食品等）；再逐条比 6.1.5.3 [p.10] 的 5 类豁免，并严格核主体要件（「个人在其住所自制、作为非商业个人礼物」≠ 企业规模化生产；「个人抵达随身携带」≠ 邮寄）。
- 完成标准：能写出「food = 是/否」「豁免 = 命中第 N 类 / 不命中」，且豁免结论附主体要件核验（谁制作、在哪制作、是否商业、是否随抵达携带）。
- **判停点 A**：非 §201(f) food → **本卡不适用**，停止，不计算任何 PN 时限。
- **判停点 B**：命中豁免 → 本卡判定结束，但须写明「豁免仅指不适用 PN 要求，**不等于免除 §801(a) 可采性审查**」（6.1.5.6 [p.12]）。不得把豁免读成「整批免检」。

**Step 2 — 取双向窗口（渠道定上限、运输方式定下限）**
- 动作：按提交渠道取**上限**——PNSI 15 个日历日 / ABI-ACE 30 个日历日；按运输方式取**下限**——公路陆运 2 小时、空运或铁路陆运 4 小时、水运 8 小时（6.1.5.1 [p.9]）。计算「预计抵达日/时」与「FDA 接收确认时点」是否都落在窗口内。
- 完成标准：能写出窗口起止两个时间点，以及「上限未超、下限未晚」两项结论。
- **判停点**：**早于上限提交同样不合规**——「越早报越安全」不成立。若渠道是**国际邮件**，切换到独立口径：**寄出前**须由 FDA 电子接收并确认，且包裹须随附确认回执（6.1.5.1 [p.9]），**不再套用抵达前 2/4/8 小时**。若无法取得预计抵达/寄出时间，停在本步补齐信息，不得凭「已提交」推定合规。

**Step 3 — 核完成点与 15 项要素**
- 动作：确认状态是「FDA 电子**接收并确认**（received and confirmed）」而非「filer 已提交」；核对 6.1.5.4 [p.10-11] / 21 CFR 1.281 的 15 项要素（提交人与传送人识别、entry type 与 CBP 标识、完整 FDA 产品代码与品名数量、制造商/种植者、生产国、发货人、起运国、预计抵达或邮寄信息、进口商/货主/最终收货人、承运人与运输方式、装运信息、曾被拒入境国家等）；国际邮件另核「包裹随附确认回执」。
- 完成标准：有可核验的 FDA 确认回执，且 15 项要素齐备、与随货单据自洽。
- **判停点**：**已提交但无 FDA 确认回执 → 判定 inadequate**，直接进入 Step 4，不得按「补报即可」放行。纸面/manual entry 不豁免本步（6.1.4.5 [p.8]）；申报侧 FD4 缺 PN 信息 / FD3 未以 PND 正确申明同样落 inadequate（6.1.6.1 [p.12]）。

**Step 4 — inadequate 的后果与不可豁免性**
- 动作：判 inadequate → **refusal and holding at the port or in a secure storage facility**（6.1.5.5 [p.11]）；同时记录两条不限制：该 CPG 指导 **does not limit** FDA 依 FD&C Act 采取必要行动（含食品安全/安防检查），也 **will not affect** CBP 依 19 U.S.C. 1595a(b) 评估罚款或依其他授权执法。
- 完成标准：结论写为「拒绝 + 扣留」，并附「其他执法权不受影响」的说明；不写成「补交后自动合规」。
- **判停点**：**指导文件不构成豁免**——企业援引 CPG 宽限说明、VQIP 资格（6.1.7 [p.13]，仅付费加速审查）、或「已安排补报」主张免检/免罚，一律不成立。VQIP 不是合规认证、不是免检、不豁免 PN。

**Step 5 — 两道门不替代与本卡终点**
- 动作：PN 合规后，明确该食品**还要**进入 §801(a) 可采性审查，由 FDA Import Systems 筛查是否需进一步评估（如 Import Alert），必要时交 V01 决策门（6.1.5.6 [p.12]）；同时把本卡的「15 天」与 6.9.13 [p.51] / 6.9.41 [p.55] 的「CBP Entry/Immediate Delivery 15 天」显式分开登记，避免同数异义混算。
- 完成标准：案卷写明「PN 门已过 / §801(a) 门待走」，且两个 15 天各有独立标注。
- **判停点**：**本卡到此为止**——不代写正式法律文书、不出合规结论、不预测个案结果；不判定产品是否可采（V01）、不下法律位阶与可主张性结论（V10）、不展开危害分析/供应商验证（包内既有 PCHF 类 CAP）、不计算条件放行期或处置窗口（V04 / V05）。Exhibit 6-1~6-4 为扫描件，涉及任何表单字段一律「需查原件」。

**时限窗口速查（双向，且随渠道切换）**

| 维度 | 取值 | 性质 | 原文锚点 |
|---|---|---|---|
| 提交渠道 = PNSI | 不早于预计抵达前 **15 日历日** | 上限 | IOM 6.1.5.1 [p.9] |
| 提交渠道 = ABI/ACE | 不早于预计抵达前 **30 日历日** | 上限 | IOM 6.1.5.1 [p.9] |
| 公路陆运 | 抵达前 **2 小时** | 下限 | IOM 6.1.5.1 [p.9] |
| 空运 / 铁路陆运 | 抵达前 **4 小时** | 下限 | IOM 6.1.5.1 [p.9] |
| 水运 | 抵达前 **8 小时** | 下限 | IOM 6.1.5.1 [p.9] |
| 国际邮件 | **寄出前**由 FDA 接收并确认，包裹附确认回执 | 独立口径 | IOM 6.1.5.1 [p.9] |
| 完成点 | received and confirmed（非「已提交」） | 硬判据 | IOM 6.1.5.1 [p.9] |
| 不适用的后果 | inadequate → refusal + holding | 刚性 | IOM 6.1.5.5 [p.11] |
| 两个「15 天」 | PN 上限 ≠ CBP Entry/Immediate Delivery 申报义务 | 同数异义 | IOM 6.9.13 [p.51]、IOM 6.9.41 [p.55] |

**适用性判定速查（先于任何时限计算）**

| 判定项 | 结论 | 落点 |
|---|---|---|
| 非 §201(f) food（药品/器械/化妆品/烟草等） | 本卡不适用，停止 | Step 1 判停点 A |
| 命中 5 类豁免之一 | 不适用 PN，但仍须 §801(a) 审查 | Step 1 判停点 B |
| food 且不豁免 | 进入双向窗口 | Step 2 |
| 已提交但无 FDA 确认回执 | inadequate | Step 3 → Step 4 |
| PN 合规 | 第一道门过，交 §801(a) | Step 5 → V01 |
| 援引 CPG 指导 / VQIP / 已安排补报 | 不构成豁免 | Step 4 判停点 |

**〔推导·非原书主张〕** 企业侧（进口商 / 境外生产商）可据上述 FDA 判定动作反推的理解：把 2/4/8 小时与 15/30 天做成订舱/发货节点的硬校验，并保留 **FDA 确认回执**（而非「已提交」截图）；PN 是独立于报关单、发给 FDA 的法定前置义务，不能用报关数据或 ACE 字段替代，纸质/manual entry 亦然；逐项核对 15 项要素与境外制造商注册状态；不把 CPG 指导或 VQIP 资格当作可不合规的依据；PN 合规不等于可采，仍须准备 §801(a) 审查。**以上是从 FDA 适用性判定、完成点要求与 inadequate 后果反推出来的；IOM 是监管者视角的内部 SOP，不写企业侧义务，不构成原书主张，也不产生任何合规结论。**

## B — 边界

**反场景（不要用本卡）**
- 用户问的是「这条 line 放不放行 / PREDICT 高分怎么办」→ 路由 V01；问「指导文件能不能当豁免 / IOM 能不能对企业主张」→ V10；问条件放行期 30 天、redelivery 窗口 → V04；问拒绝后 90 天 → V05；问状态词能否分销 → V09。
- 非食品/饲料商品（药品、器械、化妆品、烟草等）不落 PN 时限门，按 Step 1 判停。
- 涉及危害分析、预防控制、供应商批准/验证、记录保存 → 包内既有 PCHF 类 CAP；现场取样、检查观察项、FSVP 记录审查 → CAP-28 / CAP-17 / CAP-18 / CAP-21。
- 需要出具正式法律文书、给出合规结论或预测个案结果时，本卡只提供时限与适用性口径，不能代写、不能下结论。

**作者警告的失败模式（counter-example x11 / x13；principle p08；case c01；glossary g18 / g23）**
- 把 Prior Notice 当成「报关单里顺带填的一项」，或以为「货到后补报即可」——PN 是发给 FDA、有确认回执的独立法定前置义务。
- 把「已提交」当成「已完成」——完成点是 **received and confirmed**，缺确认回执即 inadequate。
- 把 2/4/8 小时记成统一时限、记成「抵达后」，或忽略 15/30 天**上限**导致早报同样违规。
- 国际邮件仍套抵达前小时口径，漏掉「寄出前确认 + 包裹随附回执」这一独立切换。
- 误判豁免主体：把企业规模化生产当「个人在住所自制的个人礼物」、把邮寄当「个人抵达随身携带」；或把豁免读成免除 §801(a) 可采性审查。
- 以「CPG 里有宽限说明」「已加入 VQIP」「已安排补报」为由主张免检或免罚——指导 does not limit FDA 权力、will not affect CBP 罚款权；VQIP 只是付费加速审查。
- 漏报/错报 15 项要素、境外制造商未注册仍按一般食品申报；把 PN 的 15 天与 CBP Entry/Immediate Delivery 的 15 天混算。
- 把 `must be received and confirmed` 与 CPG 的 guidance 文字混同位阶，据指导文字主张豁免——见下方效力层。

**阶段 0 批判（BOOK_OVERVIEW §3，本卡 Boundary 来源）与法律位阶锚点**
- **IOM 非法规**：IOM 2026 Ch.6 是 FDA 内部操作指导（OII 机构 SOP），**不是法规，不创设企业义务，也不是可对外主张的法律依据**。PN 的真正义务来源在 **FD&C Act §801（含 §801(m)）、21 CFR Part 1 Subpart I（21 CFR 1.281 等）**，以及 19 U.S.C. 1595a(b) 等 CBP 处罚依据；保证金义务锚在 **19 CFR 113.62**。6.1.5.1 的 `must be received and confirmed` 是 FDA 侧作业口径，须回到上述法条与**当前版本 IOM / RPM** 复核，不可据 IOM 单独对企业下义务或主张权利。
- **should 与 as warranted 的裁量缺口**：本卡主体是硬数字，但章内仍密集使用 `should` / `as warranted` / `where appropriate`（如 DTA 是否启动查验、审查是否 impacted by submission method 之外的裁量），几乎不给判据，留给分部惯例。本卡**不补写判据**，只把硬时限与裁量区标明。
- **2026 版快照**：PNSI、ABI/ACE、ACE/ITDS、DTA、PREDICT、FD3/FD4 flag、A of C 码 PND，以及 6.1.5.4 第 15 项中「beginning October 1, 2026」的邮件服务名与追踪号要求，都随版本变化；本卡的窗口数字与字段清单是 2026 版快照，不是稳定规则。尤其 15 项要素须回**当前版本 21 CFR 1.281** 复核。
- **监管者视角与组织前提**：全篇写「FDA 如何接收、筛查与执行」，默认有 FDA 授权、系统权限、总部 DTA（7×24）与 CBP 协作通道；企业不具这些前提，照搬会把「检查清单」误当「合规义务清单」。本卡不写进口商/境外生产商如何举证或避免被扣（凡涉及一律见 E 段〔推导·非原书主张〕）。
- **系统绑定与跨章引用**：6.1.5 的细则靠 21 CFR Part 1、Compliance Policy Guide、RPM Chapter 9、FDA Supplemental Guide 与 ACE/ITDS 承载；6.1.5.6 明确把下一道门交给 §801(a) 可采性审查；单读本章会得到「有骨架、缺细则」的闭环幻觉。
- **不谈相对方权利与救济成本**：手册不提供进口商因 inadequate 被拒/扣留后的滞期、仓储与保证金风险权衡，也不提供复核请求的成本说明。
- **Exhibit 6-1~6-4 为扫描件、无文本层**（Notice of FDA Action / Form FDA 766 / Form FDA 790 / Form FDA 463a）；本卡涉及的 PN 确认回执、NOA 与任何表单**字段一律标「需查原件」**，不得据蒸馏文本推断字段内容。
- **同数异义与锚点复核提示**：6.1.5.1 的 15 天（PN 上限）与 6.9.13 [p.51] / 6.9.41 [p.55] 的 15 天（CBP Entry/Immediate Delivery）不是同一件事；6.1.5.5 的「guidance does not limit」同时是 V10 的 x13 原文锚点，主流程若把它路由到 V10 的「可主张性」问题，本卡只保留其**后果侧事实**（inadequate 仍拒绝+扣留、其他执法权不受影响）。

**复核锚点清单（交主流程 / 阶段 1.6 晋级门）**
- **同数异义**：6.1.5.1 的 15 天（PN 上限）与 6.9.13 [p.51] / 6.9.41 [p.55] 的 15 天（CBP Entry/Immediate Delivery）不是同一件事；30 天（PN ABI/ACE 上限）与条件放行期/redelivery 30 天（V04）亦不同源。
- **法条与字段**：PN 义务来源在 FD&C Act §801(m)、21 CFR Part 1 Subpart I（21 CFR 1.281），CBP 处罚依据 19 U.S.C. 1595a(b)，保证金义务锚 19 CFR 113.62；6.1.5.4 的 15 项要素须回**当前版本 21 CFR 1.281** 复核（含「beginning October 1, 2026」新增的邮件服务名与追踪号）。
- **口径锚点共享**：6.1.5.5 的 "guidance does not limit" 同时是 V10 的 x13 原文锚点；主流程若把「指导文件是否构成豁免」路由到 V10 的位阶问题，本卡只保留其**后果侧事实**（inadequate 仍 refusal + hold、其他执法权不受影响）。
- **系统编号**：PNSI、ABI/ACE、ACE/ITDS、DTA、FD3/FD4 flag、A of C 码 PND 为 2026 版快照。
- **裁量缺口**：DTA 是否启动查验、审查是否需人工复核等 `as warranted` 判据留给 FDA 侧，本卡不补写。
- **表单**：Exhibit 6-1~6-4 为扫描件，PN 确认回执、NOA 及任何表单字段「需查原件」。
- **企业侧**：E 段与 A2 触发场景第 6 条的〔推导·非原书主张〕内容是从 FDA 适用性判定与 inadequate 后果反推，非原书主张。

**相邻混淆**
- 与 V01 共享「食品入境」语境但层次不同：本卡是抵达前的**法定前置通报门**，V01 是 6.2 电子审查的**准入决定门**；6.1.6.1 的 FD3/FD4 flag 属申报字段，不是审查动作。两道门互不替代。
- 与 V10 共享 6.1.5.5：本卡用其「refusal + hold / 其他执法权不受影响」的后果事实，V10 用它判「指导≠法规」的位阶结论，不互相替代。
- 与包内 PCHF / FSVP 类 CAP：危害分析、供应商验证、记录保存是企业侧合规体系，与「发给 FDA 的抵达前通报」不是同一义务通道；不得因「发运前置校验」字样抢路由。
- 三个「15 天 / 30 天 / 90 天」家族：PN 上限 15/30 天、CBP Entry/Immediate Delivery 15 天、条件放行期与 redelivery 30 天、拒绝后出口销毁 90 天——同数异义，分属不同窗口，见 V04 / V05 / V09。
