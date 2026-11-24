# 阶段 1.5 三重验证 — 通过单元（verified.md）

> 来源：IOM 2026 Chapter 6: Imports（FDA 内部 SOP，非方法论书籍）
> 上下文：`BOOK_OVERVIEW.md`（阶段 0）；验证规范：`03-stage1.5-triple-verify.md`
> 原文核验：`.cangjie/index/6.1…6.9-*.txt`（含 `[p.N]` 页标记），关键口径已逐条回原文确认
> 下游用途：**增量升级 `fda-pchf-food-safety` 技能包（当前 v4.16 / CAP-01…28 / 二十类不可混引）**

## 0. 本轮口径与统计

| 项 | 数值 |
|---|---|
| 原始候选 | **82** 条（framework 13 + principle 15 + case 12 + counter-example 14 + glossary 28） |
| 去重后单元 | **20** 个 |
| 通过（独立成能力卡） | **10** 个（本文件） |
| 淘汰 / 降级 | **10** 个（`rejected/R01–R10.md`） |

**去重与降级口径（严格执行）**
- 同一方法论被多个 extractor 提取的合并为 1 个单元，`merged_from` 列出全部来源 id；**每条原始候选有且仅有一个主归属单元**（82 条全覆盖，完整映射见 `rejected/SUMMARY.md`）。
- 跨单元复用仅作 V1 佐证（`source_evidence` / `V1_cross_domain.independent_contexts`），不重复计入 `merged_from`。
- `case` / `counter-example` 的具体实例作为**佐证材料并入**框架单元，不各自独立成能力（唯一例外是 x14 术语误读，并入 V09 概念区分树）。
- `glossary` 术语一般作为共享 GLOSSARY 与单元内口径说明，不独立成能力；**仅「扣留 / 放行 / 条件放行」这组本身构成判定框架的术语升格为 V09**。

**V3 判定口径（本轮最关键）**：独特性 = **反直觉的机构特定口径**（DWPE「不检查就扣住」、Failure to Hold「无放行即分销」而非「移出港区」、DER/DTR 按触发依据而非严重度分流、May Proceed 是终局放行、与 PREDICT 相悖的放行须写明理由、30 天 vs 90 天窗口的区分、放行可撤消但条件放行期不重开、拒绝不是终点、483a 只在 closeout 签发），**不是措辞文雅**。「要留记录 / 要及时沟通 / 数据要准确」这类聪明人常识一律判不通过。

**既有技能包锚点（每单元必填 `overlap_risk` / `differentiator`）**
- CAP-17：CP 7303.050 取样量
- CAP-18：IOM Ch.5 检查员权限与 483
- CAP-21：CP 7303.878 FSVP 检查
- CAP-28：IOM Ch.4 取样全流程
- 「二十类不可混引」：包内既有主题卡不得交叉引用，V09（口径层）与 V10（效力层）专门服务该约束，供阶段 1.6 晋级门与阶段 4 负例设计使用。

---

## V01 · 入境审查决策门与可辩护判定留痕

```yaml
id: V01
slug: entry-review-admissibility-decision-gate
title: 入境审查决策门与可辩护判定留痕
type: framework
importance: critical
importance_reason: |
  BOOK_OVERVIEW 优先级 1「最高频的判定动作、预测力最强」。6.2 是整条进口链的决策中枢，
  其动作集与「决定须可被听证复核」是后续所有处置的输入；一旦动作选错，下游全链不可逆。
one_liner: "先审 PREDICT 风险分与 rule flags，再把每条 line 判入有限动作集；凡与 PREDICT 相悖的放行、请求扣留、请求现场工作，必须写出可核验的具体事实理由，不能只写动作码。"
intents:
  - "判断某条 entry line 应发 May Proceed、请求现场工作、提交扣留建议，还是以 OGA referral 关闭"
  - "审查员想在 Priority Review flag 下仍放行时，判断备注写到什么程度才合格"
  - "判断与 PREDICT 筛查结果相悖的决定该如何留痕才可在听证/复核中站得住"
  - "他机关已扣押/拒绝同一批货时，判断 FDA 是否还应作出可采性判定"
  - "企业侧〔推导〕理解 FDA 电子审查阶段会看哪些输入、为何申报数据要自洽"
keywords: ["May Proceed", "PREDICT", "入境审查", "entry reviewer", "Remarks", "空泛备注", "Priority Review flag", "OGA Referral", "Compliance Branch", "可采性判定", "rule flags", "decision gate", "admissibility"]
merged_from: [f01, p02, c07, x06, g19, g22, g24]
source_evidence:
  - "IOM 6.2.2.2 [p.16]：自动筛查未发 May Proceed 即强制人工审查；带 Priority Review flag 的放行须在 Remarks 写 clear reason"
  - "IOM 6.2.2.2.1 [p.17]：能用电子单据确认全部合规且无需扣留/现场 → 签发 May Proceed"
  - "IOM 6.2.5 [p.21]：产品看似不合规只有两个选项——请求现场工作，或向 Compliance Branch 建议扣留"
  - "IOM 6.2.1 [p.14]：三类决定须 clear remarks；Avoid vague remarks like 'May Proceed' or 'N/A'"
  - "IOM 6.2.2.2.6 [p.19]：OGI/OGC work type 在他机关处理该票时关闭 line，FDA 不作可采性判定；关闭前须上传他机关处置证明"
  - "IOM 6.9.57 / 6.1.6.2 [p.56]/[p.13]：Notice of FDA Action 按每个 entry line 逐项、随状态变化反复出具"
V1_cross_domain:
  passed: true
  independent_contexts:
    - context: "6.2.2.2 / 6.2.5 [p.16,p.21]（对象：电子申报的 entry line）"
      conclusion: "未自动放行即人工审查，落入五分支有限动作集；疑似违规只能请求现场工作或向 CB 建议扣留，审查员不自行终局扣留"
    - context: "6.3.10.7 [p.32]（对象：已完成物理查验的 line，属不同 6.x 节）"
      conclusion: "同构决策门按 Exam Class 收窄 Next Steps（Class 1 可 IB Release/Add Work；Class 3 只能 Refer to CB/Add Work）——同一「有限动作集」思想，但对象与结论都不同"
    - context: "6.1.4.6.1 [p.8-9]（对象：Import for Export 入境类型）"
      conclusion: "缺 IUC/A of C 或支持文件 → 更新+rescreen 或请求扣留；文件齐备 → 可发 May Proceed——决策门在上游入境类型判定中的复用"
    - context: "6.5.2.7 [p.40]（对象：听证后改判，属处置链）"
      conclusion: "放行改变须 explain the reason for the change of action——「决定须可辩护」跨到 6.5 仍成立"
  reasoning: "四个语境分属 6.1 / 6.2 / 6.3 / 6.5，对象分别是 IFE 申报、电子审查 line、现场查验结果、听证改判，结论分别是「文件齐备可放行」「落入动作集」「按 Class 收窄动作」「改判须写理由」——不是同一规则换个说法。"
V2_predictive_power:
  passed: true
  novel_question: "某 line 被 PREDICT 标为高风险，但 CBP 已以走私为由扣押该批货并把扣押证明上传；审查员该继续走扣留建议，还是签 May Proceed？"
  derived_answer: |
    两者都不对。按 6.2.2.2.6，另一政府机关已在处理该票时应走 OGA Referral（OGI/OGC）
    关闭该 line，FDA **不作可采性判定**；且关闭的硬前提是「他机关处置证明已上传」，
    本案已满足。签发 May Proceed 等于 FDA 自己作出了可采性决定（与「不作判定」相冲突），
    提交扣留建议则与已扣押状态重复、且审查员本就无权终局扣留。若反而要对该 line 作
    May Proceed，还须因与 PREDICT 高风险相悖而在 Remarks 写出可核验的具体理由。
  why_nontrivial: "直觉会认为两个机关各自都要出决定、或「已被扣押=不用管了」；实际是「FDA 主动放弃判定并关闭 line」，且关闭带文书前提。"
V3_exclusivity:
  passed: true
  institution_specific_calibration:
    - "'May Proceed' 字面像『准许继续办理』，实为终局性放行动作（货物可进入流通），且可被 rescind"
    - "把放行动作名 'May Proceed' 写进 Remarks 当理由，是被手册点名的头号错误——放行动作不等于判定依据"
    - "合格备注的判据是『可核验的具体差异事实』（品牌不在 DWPE 名单、粉剂非液剂、单据证明不含肝素），不是字数、不是结论复述"
    - "OGA Referral 的法律后果是『FDA 不作可采性判定就关闭 line』，而非『转交协查、FDA 仍出决定』"
    - "PREDICT 是输入不是判决；与筛查结果相悖的放行必须写明理由"
  why_not_common: "常识是『做决定要写清楚』；本单元的反直觉在于——放行动作本身被禁止当作理由、高风险评分不构成自动判决、以及存在一条『主动放弃判定并关闭』的合法分支。三者都是 FDA 内部判定口径，外行说不出。"
overlap_risk:
  - "CAP-18（IOM Ch.5 检查员权限与 483）：可能抢『检查员作出书面动作/观察项』路由"
  - "CAP-28（IOM Ch.4 取样全流程）：可能抢『请求现场工作/取样』路由"
  - "V02（DER/DTR 分流）：同属 6.2，可能抢『扣留』路由"
differentiator: "本卡只管 6.2 **电子审查阶段的准入决策门**与判定理由的可辩护性，产物是 May Proceed / 现场工作请求 / 扣留建议 / OGA 关闭 / 撤消，不产出 483 观察项、不执行取样、不决定扣留建议走哪个 work type。CAP-18 是 Ch.5 现场检查权限与 483，CAP-28 是 Ch.4 取样执行流程，阶段与产物均不同；V02 只接本卡『请求扣留』这一支的下游分流。"
supporting_refs: [f09, c04, p07, c02, R07]
```

---

## V02 · DER/DTR 按触发依据分流与 DWPE「不检查就扣住」

```yaml
id: V02
slug: der-dtr-detention-routing
title: DER/DTR 按触发依据分流与 DWPE「不检查就扣住」
type: framework
importance: critical
importance_reason: |
  BOOK_OVERVIEW 优先级 1 的另一半、核心命题 5。DER/DTR 是用户点名的反直觉口径，
  且 Import Alert / DWPE 判定直接决定货物是否免查验即扣，是全章预测力最强的分流点。
one_liner: "扣留建议先问『触发依据是不是 DWPE/Import Alert』——是则 DER，其余一切疑似违规走 DTR；这是触发依据分流，不是严重程度分级，且查不到数据不等于违规。"
intents:
  - "判断某条疑似违规的 line 该用 DER 还是 DTR 提交扣留建议"
  - "命中 Import Alert 时判断可否免索单据直接 DER、何时必须先索取证书"
  - "数据库查不到注册/510(k)/PMA 或 A of C 缺失时，判断能否直接建议扣留"
  - "判断企业自行送检合格报告是否足以解除 DWPE"
  - "区分 Import Alert（别再请求现场工作、走 DER）与 Import Bulletin（指示去请求现场工作）"
  - "判断命中多个 Import Alert 时扣留建议要列哪些内容"
keywords: ["DER", "DTR", "DWPE", "Import Alert", "Import Bulletin", "扣留建议", "Compliance Branch", "IA 28-02", "audit sample", "reasonable effort", "PAF", "触发依据", "detention recommendation"]
merged_from: [f02, p13, c06, g06, g07, g16, g17]
source_evidence:
  - "IOM 6.2.5.1 [p.21]：Use DER when a product is subject to DWPE；Use DTR for all other situations where a product appears to be violative"
  - "IOM 6.2.5.3 [p.21-22]：DER 免单据三条件（电子数据匹配 IA / IA 不要求特定文书 / 无需额外信息）；IA 28-02 印度黑胡椒须先索取证书"
  - "IOM 6.2.5.5 [p.23]：You must make a reasonable effort to verify compliance… Do not recommend detention based solely on a failed data lookup or missing A of C"
  - "IOM 6.2.5.2 [p.21]：多重违规须列全 applicable alerts 与 PAF"
  - "IOM 6.3.10.5 [p.31]：Class 3 FEX/LEX 发现违规 → 记录并提交 DTR + 相应 PAF"
  - "IOM 6.9.22 [p.52] / 6.9.6 [p.51]：DWPE 凭违规史/Import Alert 免实物查验扣留；移除 DWPE 至少须一份 FDA audit sample"
  - "IOM 6.2.2.2.x [p.17]：Import Alerts: Do not routinely request work for a line that is already subject to an Import Alert"
V1_cross_domain:
  passed: true
  independent_contexts:
    - context: "6.2.5.1 / 6.2.5.5 [p.21,p.23]（对象：电子审查阶段的扣留建议）"
      conclusion: "按触发依据分 DER/DTR；查不到注册/列名/批准不得直接建议扣留，须先合理努力核实"
    - context: "6.3.10.5 [p.31]（对象：现场查验 Class 3 结果，属不同 6.x 节）"
      conclusion: "FEX/LEX 发现违规时以 DTR + PAF 提交 compliance——分流规则从电子审查延伸到现场查验"
    - context: "6.6.4.3 / 6.2.2.2 [p.44]/[p.16]（对象：事后调查与风险标记，属不同 6.x 节）"
      conclusion: "因 DWPE 历史被扣的即食食品仍属高优先级加重情形；PREDICT Priority Review flag 明确包含 DWPE 产品——DWPE 是加重信号而非减轻信号"
    - context: "6.9.6 / 6.9.22 [p.51,p.52]（对象：术语与证据门槛）"
      conclusion: "解除 DWPE 须至少一份 FDA 自采 audit sample，企业私人实验室报告不构成移除证据"
  reasoning: "四个语境分属 6.2 / 6.3 / 6.6 / 6.9，对象分别是扣留建议、现场查验结果、调查加重分级、术语证据门槛，结论互不重复。"
V2_predictive_power:
  passed: true
  novel_question: "某企业出口的产品在 FDA 数据库查不到 510(k) 与注册记录，filer 的 A of C 也缺失；审查员想据此直接建议扣留并走 DER 快速通道，可以吗？"
  derived_answer: |
    两步都错。① 6.2.5.5 明令「不得仅凭 failed data lookup 或 missing A of C 建议扣留」，
    须先用手上信息作合理努力核实（电子申报 + 内部数据库 + filer 单据，必要时请求
    DRQ/FEX/SAM），查不到只是核实起点而非违规结论。② 即便核实后确需扣留，触发依据
    是「无法确认可采性」而非「受 DWPE 约束」，应走 **DTR**（6.9.20 正是以注册、
    scheduled process filing、510(k)、PMA 无法核实为 DTR 示例），不是 DER；DER 只在
    受 Import Alert/DWPE 约束时使用。③ 若检索后确认不匹配任何 IA，还须用系统
    feedback 写明为何该 IA 不适用，并把全部研究写进 Remarks。
  why_nontrivial: "直觉会把「查无记录」当成违规证据、把 DER 当成更严重的档位；实际恰好相反，且还牵出一条『核实义务 + 不命中也要写理由』的隐藏动作。"
V3_exclusivity:
  passed: true
  institution_specific_calibration:
    - "DER/DTR 是**按触发依据**分流，不是按严重程度分级——直觉上极易当成轻重档"
    - "DWPE = 『不检查就扣住』（凭历史/Import Alert 免实物查验即扣），字面『不检查』极易被读成『不检查就放过』"
    - "'查不到 ≠ 违规'：数据库查询失败、A of C 缺失都只是核实起点，直接建议扣留被明文禁止"
    - "Import Alert 与 Import Bulletin 方向几乎相反：Alert → 别再请求现场工作、走 DER；Bulletin → 指示去请求现场工作、不触发 DWPE"
    - "审查员提交的是 recommendation/request，不是终局扣留决定，须交 Compliance Branch"
    - "解除 DWPE 的证据门槛是『至少一份 FDA 自采 audit sample』，企业送检合格报告无效"
  why_not_common: "任何聪明人都会说『违规就扣、严重的走快通道』；本单元反着来——快通道由『是否列名 Import Alert』触发，与严重度无关，而且『查无记录』被禁止当作扣留依据。"
overlap_risk:
  - "V01（决策门）：同属 6.2，抢『请求扣留』这一支的路由"
  - "V09（状态概念区分树）：抢 DWPE / Detention 术语口径"
  - "CAP-18（IOM Ch.5 检查员权限与 483）：可能误把扣留建议当成检查观察项"
  - "包内既有【Import Alert / 进口警报】相关 CAP（若存在）：抢『警报命中后怎么处置』路由"
differentiator: "本卡只输出**向 Compliance Branch 提交的 work type（DER 或 DTR）及其提交前核实义务**，不管决策门选哪个动作（V01）、不管状态词定义（V09）、不产出 483 观察项（CAP-18 是 Ch.5 现场检查观察项，与 6.2 扣留建议是不同文书）、不执行取样（CAP-28）。"
supporting_refs: [x02, x14, c07, R01, R06]
```

---

## V03 · 事先通知（Prior Notice）适用性硬时限判定

```yaml
id: V03
slug: prior-notice-eligibility-gate
title: 事先通知（Prior Notice）适用性硬时限判定
type: framework
importance: high
importance_reason: |
  BOOK_OVERVIEW 优先级 5。2/4/8 小时与 15/30 天是可机械判定的硬约束，且与既有
  CAP-01…28（PCHF/取样/检查）几乎不重叠，是增量价值最干净的一张卡；但适用面限食品/饲料，
  故不列 critical。
one_liner: "先判是否 §201(f) food 且不在免列，再按提交渠道取上限（PNSI 15 天 / ABI-ACE 30 天）、按运输方式取下限（2/4/8 小时），以『FDA 电子接收并确认』为完成点；不满足即 refusal + hold，且指导文件不构成豁免。"
intents:
  - "判断某批食品是否须提交 Prior Notice、是否落在豁免清单内"
  - "按运输方式与提交渠道计算事前通知的合法时间窗"
  - "判断『已提交但无 FDA 确认回执』是否算合规"
  - "判断国际邮件/随行李携带/外交邮袋等特殊情形的口径"
  - "理解 inadequate prior notice 的后果及其他执法权是否受影响"
keywords: ["Prior Notice", "事先通知", "PNSI", "ABI/ACE", "2/4/8 hours", "15/30 calendar days", "received and confirmed", "inadequate", "refusal and holding", "豁免清单", "21 CFR 1.281", "DTA", "FD3/FD4"]
merged_from: [f08, p08, c01, x11, g18, g23]
source_evidence:
  - "IOM 6.1.5.1 [p.9]：no more than 15 calendar days (PNSI) / 30 calendar days (ABI/ACE)；no fewer than 2h 公路 / 4h 空运铁路 / 8h 水运"
  - "IOM 6.1.5.1 [p.9]：国际邮件须在寄出前 received and confirmed，包裹须附 FDA 接收确认"
  - "IOM 6.1.5.5 [p.11]：inadequate prior notice → refusal and holding at the port or in a secure storage facility；CPG 指导 does not limit FDA / will not affect CBP 罚款权"
  - "IOM 6.1.5.3 [p.10]：5 类豁免（个人随身自用、港内不离港即出口、USDA 专属管辖肉禽蛋、个人住所自制作为个人礼物、维也纳公约 27.3 外交邮袋）"
  - "IOM 6.1.4.5 [p.8]：manual/paper entry 的人用或动物用食品仍须事先通知（可经 PNSI）"
  - "IOM 6.1.6.1 [p.12]：FD3/FD4 PGA flag 判定是否须 PN；FD3 可用 A of C 码 PND 申明豁免"
V1_cross_domain:
  passed: true
  independent_contexts:
    - context: "6.1.5.1 / 6.1.5.3 / 6.1.5.5 [p.9-11]（对象：一般进口食品）"
      conclusion: "时限—豁免—后果闭环；完成点是 FDA 电子接收并确认，inadequate 直接 refusal + hold"
    - context: "6.1.4.5 [p.8]（对象：人工/纸面 entry 的食品，属不同入境类型）"
      conclusion: "PN 义务独立于报关方式，纸质/手工申报仍须提前通报——这是最易被忽略的交叉点"
    - context: "6.1.6.1 [p.12]（对象：申报数据字段 FD3/FD4 / A of C 码 PND）"
      conclusion: "『是否需 PN』落实为申报判定字段，豁免可经 PND 代码申明——从义务落到数据层"
    - context: "6.1.7 / 6.1.5.6 [p.13]/[p.11-12]（对象：VQIP 与 §801(a) 后续审查）"
      conclusion: "VQIP 只是加速审查、不豁免 PN；满足 PN 的食品还要再走 §801(a) 可采性审查，两道门互不替代"
  reasoning: "四个语境对象分别是一般食品、纸面 entry 食品、申报字段、VQIP/后续审查，结论分别是时限后果、义务不随报关方式免除、字段化落实、两道门不替代——不是同节换个说法。"
V2_predictive_power:
  passed: true
  novel_question: "某境外食品企业经国际邮件向美国个人寄送一批自家工厂生产的肉松烘焙零食，声称是『个人礼物』并主张豁免 Prior Notice；若不适用豁免，时限该按 2/4/8 小时算吗？"
  derived_answer: |
    两项主张都不成立。① 6.1.5.3 的『个人礼物』豁免要求「个人在其**住所自制**、作为
    非商业个人礼物寄送」，企业规模化生产不适用；且该豁免与『个人抵达随身携带』是两类，
    邮寄不自动落入。② 国际邮件不走抵达前 2/4/8 小时口径，而是「**寄出前**须由 FDA
    电子接收并确认」，且包裹须随附 FDA 接收确认回执（6.1.5.1）。③ 若未取得确认回执，
    属 inadequate → 拒绝并在口岸/安全设施扣留（6.1.5.5）；企业援引 CPG 指导主张宽限
    无效，因原文明确该指导 does not limit FDA 依 FD&C Act 采取行动、也不影响 CBP 依
    19 USC 1595a(b) 处罚。④ 即便 PN 合规，该食品仍须再走 §801(a) 可采性审查。
  why_nontrivial: "同时踩中『豁免主体误判』与『时限口径随渠道切换』两个隐藏点，且结论不是『补报即可』而是直接拒绝+扣留。"
V3_exclusivity:
  passed: true
  institution_specific_calibration:
    - "完成点是『FDA 电子**接收并确认**（received and confirmed）』，不是『已提交』——缺确认回执即 inadequate"
    - "15/30 天是**上限**、2/4/8 小时是**下限**，双向窗口；早于上限提交同样不合规"
    - "Prior Notice 是发给 FDA、独立于报关单的法定前置义务，不能用报关数据替代"
    - "两个『15 天』同数异义：PN 上限（6.1.5.1）vs CBP Entry/Immediate Delivery 申报义务（6.9.13/6.9.41）"
    - "VQIP 是付费加速审查资格，不是合规认证、不是免检，不豁免 PN"
    - "inadequate 不限制 FDA 其他行动、也不影响 CBP 处罚权——指导文件不构成豁免"
  why_not_common: "常识是『报关前通知一下、早点报总没错』；本单元反直觉在于早报同样违规、提交不等于完成、以及存在一个与报关单完全平行的独立义务通道。"
overlap_risk:
  - "包内既有【危害分析 / 供应商批准 / 记录保存】类 CAP：可能在『发运前置校验』上抢路由"
  - "V10（效力层元规则）：x13 以 6.1.5.5 为原文锚点，可能抢『指导文件是否构成豁免』路由"
  - "V01（决策门）：6.1.6.1 的 FD3/FD4 flag 可能被当成 6.2 审查动作"
differentiator: "本卡判定对象是**运输方式 × 提交渠道的时限窗与豁免适用性**，产物是『合规 / inadequate → refusal+hold』，不判定产品是否可采（V01）、不判法律位阶（V10 只借 x13 作 Boundary 锚点）、不涉及危害分析或供应商验证（包内既有 PCHF 类 CAP）。"
supporting_refs: [R05, R06, x13, g23]
```

---

## V04 · 条件放行 / 撤消 / redelivery 时间窗体系

```yaml
id: V04
slug: conditional-release-rescission-windows
title: 条件放行 / 撤消 / redelivery 时间窗体系
type: framework
importance: critical
importance_reason: |
  BOOK_OVERVIEW 优先级 2/3、核心命题 4。30 天窗口、撤消不重开、24 小时硬动作
  一旦错过即不可逆（货物无法召回、只能追偿 liquidated damages），是后果最不可挽回的一张卡。
one_liner: "条件放行期通常 30 天，以 May Proceed / Refusal / 30 天届满三者最先发生者永久结束；DRQ/DTR/DER/DEF/INF 都不延期，撤消放行也不重开，CBP 的 30 天 redelivery 反而从放行日起算。"
intents:
  - "计算某批条件放行货物还剩多少可采性决定时间"
  - "判断哪些动作会/不会延长条件放行期"
  - "误发 May Proceed 或 IB Release 后，判断 24 小时/30 天内必须完成哪些动作"
  - "判断撤消放行后条件放行期能否重新计时"
  - "区分 30 天 redelivery 窗口与拒绝后的 90 天出口/销毁窗口"
keywords: ["Conditional Release", "条件放行期", "30 days", "May Proceed rescind", "IB Release", "redelivery", "24 hours", "bond hold", "ABI Do Not Distribute", "DRQ/DTR/DER/DEF/INF", "90 days", "irreversible"]
merged_from: [f04, f05, p03, c05, x07, g03]
source_evidence:
  - "IOM 6.2.4 [p.20]：条件放行期典型 30 天，以 May Proceed / 拒绝通知 / 30 天届满三者最先发生者结束；DRQ/DTR/DER/DEF/INF 均不延长"
  - "IOM 6.2.4 [p.20]：延长只有一条路——首个 30 天内书面通知进口商，且须声明 FDA 将查验、取样或扣留"
  - "IOM 6.2.2.2.2 [p.17]：Once you issue a 'May Proceed,' the conditional release period … ends permanently. Even if you rescind the notice, the period does not reopen."
  - "IOM 6.2.2.2.2 [p.18]：24 小时内发更新 NOA、24 小时内请求 CBP bond hold、确认 ABI『勿分销』码、已分销则请求 redelivery（CBP 30 天窗口）"
  - "IOM 6.3.11 [p.32-33]：Rescinding an IB Release 同构七步；30 天从 IB Release 签发日起算，任何延误损害 FDA 请求 redelivery 的能力"
  - "IOM 6.9.13 / 6.9.41 [p.51,p.55]：货物 may be moved，但 CBP 可 30 天内要求 redelivery；期间以 May Proceed 或拒绝结束"
  - "IOM 6.5.2.11 [p.42]：放行前已分销且无法 redelivery → Bond Action"
V1_cross_domain:
  passed: true
  independent_contexts:
    - context: "6.2.4 [p.20]（对象：等待可采性决定的条件放行货物）"
      conclusion: "30 天三事件先到者结束；四类请求动作均不产生延期效力"
    - context: "6.2.2.2.2 [p.17-18]（对象：误发的 May Proceed，属电子审查动作）"
      conclusion: "撤消仅限罕见情形且须立即完成 24h 硬动作；发出放行即永久终结期间，撤消不重开"
    - context: "6.3.11 [p.32-33]（对象：现场查验后的 IB Release，属不同 6.x 节）"
      conclusion: "同一撤消程序第二次完整书写，但 30 天起算点改为 IB Release 签发日——同构而非同一"
    - context: "6.6.4.1 第 7 步 / 6.5.2.8 [p.43]/[p.41]（对象：调查与拒绝处置）"
      conclusion: "因查验/取样签发的 4647 是 30 天 redelivery；拒绝后出口/销毁是 90 天——两套窗口不可混用"
  reasoning: "四个语境分属 6.2 / 6.3 / 6.5 / 6.6，对象分别是等待判定货物、误发电子放行、现场放行、调查/拒绝处置，结论分别是窗口终止规则、撤消不可逆、起算点差异、30 与 90 天分野。"
V2_predictive_power:
  passed: true
  novel_question: "进口商认为『已向 FDA 提交 DTR 扣留请求 = 审查时钟暂停』，于是拖到第 35 天才追问为何条件放行期已过、FDA 还没出决定；这个理解错在哪，后果是什么？"
  derived_answer: |
    错在把请求动作当成延期。6.2.4 明确列出 DRQ、DTR/DER、DEF、INF **都不延长**
    条件放行期，唯一延长路径是在首个 30 天内**书面**通知进口商且声明 FDA 将查验、
    取样或扣留。第 35 天时窗口已因届满永久关闭，FDA 事实上已丧失在该期内作可采性
    决定的程序基础。更反直觉的是：若此前曾误发 May Proceed，期间同样已永久结束，
    即便撤消也不重开，而 CBP 要求 redelivery 的 **30 天反而从放行日起算**——
    拖延会同时吃掉这个窗口，货物一旦分销即无法召回，只能转入 Bond Action /
    liquidated damages（6.5.2.11）。
  why_nontrivial: "直觉是『案子还在审、时钟该停』；实际是四类请求一个都不延期，且撤消放行非但不重置时钟、反而启动另一个更短的倒计时。"
V3_exclusivity:
  passed: true
  institution_specific_calibration:
    - "放行**不是终局且可撤消**，但撤消**不重启**条件放行期——「可逆」与「不可逆」同时成立"
    - "DRQ/DTR/DER/DEF/INF 明确不延长条件放行期；唯一延长路径必须书面且声明将查验/取样/扣留"
    - "'May Proceed' 明确表示『未作合规判定』，不产生『已合格』豁免；放行后仍可依 §304(d) 执法"
    - "30 天（条件放行期 / redelivery 窗口）与 90 天（拒绝后出口销毁）是三套独立窗口，同数异义、不可混用"
    - "CBP 的 30 天 redelivery 窗口从放行日（而非发现误放行日）起算，任何延误损害 FDA 追货能力"
    - "撤消仅限『需合规行动 / 误放行 / 新信息』，明确不得用于例行或工作计划性查验"
  why_not_common: "常识是『发现错了就撤回来重来』；本单元说撤回不等于回退、发出即永久结束、而且请求动作不暂停时钟——这是一套不可逆的时间法，外行不会这么设计。"
overlap_risk:
  - "V07（Failure to Hold）：抢『条件放行 / 30 天』路由，且用户示例『条件放行后未收 May Proceed 即发货』同时命中两卡"
  - "V09（状态概念区分树）：抢 Conditional Release 状态词定义"
  - "V05（处置主链）：抢 Refusal 后 90 天窗口"
  - "CAP-28（IOM Ch.4 取样全流程）：含取样期间货物状态，可能被误当条件放行期"
differentiator: "本卡只管**时间窗的起算、终止、不延长、不重开以及撤消后 24h/30d 补救动作序列**，不认定是否构成违规（V07）、不定义状态词（V09）、不展开 Refusal 后处置链（V05）。用户示例『货已条件放行但未收 May Proceed 就发经销商』应路由到 V07（分销即 FTH），本卡只提供其 30 天窗口背景。"
supporting_refs: [g02, g11, x08, f06, R09]
```

---

## V05 · 违规处置主链与文书矩阵（拒绝不是终点）

```yaml
id: V05
slug: violation-disposition-chain
title: 违规处置主链与文书矩阵（拒绝不是终点）
type: framework
importance: critical
importance_reason: |
  BOOK_OVERVIEW 优先级 2、核心命题 8/10。不可逆时间链（听证 10 工作日 → 766 →
  放行/拒绝 → 90 天出口销毁 → Bond Action），文书与时限一旦错后果不可逆；
  「拒绝不是终点」是用户点名的反直觉口径。
one_liner: "扣留后走听证→举证→重整→复核→放行或拒绝；拒绝通知发出后档案不关闭，须在 90 天内于 CBP 监督下出口或销毁并回传证明，否则转 Bond Action——发通知不等于结案。"
intents:
  - "判断某批被扣货物下一步该出哪张通知/文书、由谁签字"
  - "计算听证期、90 天出口/销毁期等硬时限"
  - "判断收到 Refusal Notice 后企业内部能否结案"
  - "理解 Detention（临时可回转）与 Refusal（终局）的分界"
  - "判断拒绝后未按期处置会触发什么经济后果"
  - "核对 Refusal 通知上的 charge 是否合法"
keywords: ["Notice of FDA Action", "Detained", "Refusal of Admission", "10 working days", "90 days", "CBP 4647", "FDA 790", "Bond Action", "file remains open", "export or destroy", "charge 逐字一致", "liquidated damages", "听证"]
merged_from: [f06, p15, c09, c11, x08, g05, g08, g10, g25, g26]
source_evidence:
  - "IOM 6.5.2.1 [p.39]：Notice of FDA Action - Detained，通常允许 10 working days 到场（有 compelling reason 可延长）"
  - "IOM 6.5.2.8 [p.41]：Refusal 后 90 天内 CBP 监督下出口或销毁；The FDA file remains open until… destroyed or exported；FDA 责任延续到违规品被销毁或出口"
  - "IOM 6.5.2.8 [p.41]：Refusal 版 charge 须与原 Detained 通知逐字一致，副本送 CBP"
  - "IOM 6.5.2.10 [p.41-42]：合理期限未收到处置通知须调查状态、核实货物 intact / 再出口确已发生"
  - "IOM 6.5.2.11 [p.42]：Bond Action 两类触发；CBP 一般不在 FDA 不完全同意时减免违约金（21 CFR 1.97(b)）"
  - "IOM 6.9.21 [p.52]：Detention 是 temporary administrative action，基于『appear not to be』违规"
  - "IOM 6.9.44 [p.55]：Refusal 是 final decision，90 天内销毁或出口"
  - "IOM 6.6.2 [p.42-43]：证据转 CBP Title 19 制裁 / OCI 刑事调查，且刑事取证不改变 FDA 处置顺序"
V1_cross_domain:
  passed: true
  independent_contexts:
    - context: "6.5.2.1 / 6.5.2.8 [p.39,p.41]（对象：被扣 / 被拒的货物）"
      conclusion: "听证 10 工作日 → 拒绝 → 90 天出口销毁；档案到销毁/出口证明才关闭"
    - context: "6.5.2.3 / 6.5.2.9 / 6.5.2.11 [p.40-42]（对象：重整、监管费用、保证金）"
      conclusion: "每步产物绑定固定文书（FDA 766 / 790）与经济后果（Bond Action），构成环节—文书—签字矩阵"
    - context: "6.6.2 [p.42-43]（对象：进口调查与刑事取证，属不同 6.x 节）"
      conclusion: "个案证据转成 CBP 制裁或 OCI 刑事调查输入，且取证可能性不改变 FDA 对货物的处置标准与顺序"
    - context: "6.9.21 / 6.9.44 / 6.9.23 [p.52,p.55,p.52-53]（对象：术语与听证举证）"
      conclusion: "Detention 临时可回转、Refusal 终局；举证须在听证期内提交，形式可为一串邮件/电话到正式会议"
  reasoning: "四个语境分属 6.5 / 6.6 / 6.9，对象分别是货物处置、文书费用、调查制裁、术语举证，结论分别是时间链、文书矩阵、证据外溢、临局分界。"
V2_predictive_power:
  passed: true
  novel_question: "某批货收到 Refusal Notice 后第 80 天进口商才安排出口，出口证明预计第 100 天才能回传；为减少滞期损失，进口商想把货物先转内销。可以吗，FDA 档案此时是否已关闭？"
  derived_answer: |
    都不行。① 90 天约束的是「**出口或销毁完成**」，不是「已安排出口」；第 100 天才
    拿到证明已逾期。② FDA 档案在分部收到销毁/出口证明**之前保持开放**，发通知 ≠ 结案，
    FDA 对公众健康的责任延续到违规品实物灭失为止（6.5.2.8）。③ 合理期限未收到处置
    通知，分部还须主动调查状态、核实货物是否 intact 待处置 / 再出口是否确已发生
    （6.5.2.10）。④ 转内销既属「已扣留并拒绝却未依法销毁/出口」，又属放行前分销，
    直接触发 **Bond Action**（6.5.2.11）——主体是 CBP，追缴 liquidated damages，且
    涉及 FDA 货物时 CBP 通常须 FDA 完全同意才减免（21 CFR 1.97(b)）。⑤ 若发现
    CBP 4647 未签发，还须联系 compliance officer 并通知 CBP CTAC。
  why_nontrivial: "直觉把『收到拒绝通知』当终点、把『已安排出口』当履约；实际责任延续到实物灭失，且『安排』与『完成并取证』之间的差距正是 Bond Action 的触发点。"
V3_exclusivity:
  passed: true
  institution_specific_calibration:
    - "Refusal of Admission **不是流程终点**：之后还有 4647 redelivery、出口/销毁核验、Bond Action，档案才关闭"
    - "『发出通知』与『责任解除』被解耦；FDA 公共健康责任延续到违规品被销毁或出口"
    - "Detention 是 temporary / administrative / 基于『appear not to be』的外观标准，Refusal 才是 final decision"
    - "Refusal 通知的 charge 须与原 Detained 通知**逐字一致**，否则程序瑕疵"
    - "90 天（拒绝后出口销毁）与 30 天（放行/条件放行期结束后的 redelivery）是两套窗口"
    - "OCI 刑事取证不得改变 FDA 处置顺序——不能『因为可能成为证据就另走一套标准』"
    - "Bond Action 主体是 CBP 而非 FDA；减免通常须 FDA 完全同意"
  why_not_common: "常识是『判了、发了通知就结案』；本单元说法律责任延续到货物物理灭失、通知只是中间文书，且刑事取证不能插队——这是一套监管者视角的责任延续口径。"
overlap_risk:
  - "V06（FDA 766 授权门）：抢『重整』子链路由"
  - "V04（时间窗）：抢 90 天 / 30 天窗口"
  - "V07（FTH）：抢『放行前分销 → Bond Action』触发条件"
  - "CAP-18（IOM Ch.5 检查员权限与 483）：483 在上游检查阶段，可能被误当处置链文书"
  - "CAP-28（IOM Ch.4 取样全流程）：取样在扣留之前，可能抢『证据』路由"
differentiator: "本卡管 **6.5 下游处置链的全貌与文书/时限矩阵**（Detained→听证→766→放行/拒绝→90 天→Bond），不放行 766 授权门的内部判据（V06）、不算条件放行期（V04）、不认定 FTH 违规（V07）。483 是 CAP-18 的 Ch.5 现场检查观察项，与本卡的 Notice of FDA Action 是完全不同的文书序列。"
supporting_refs: [f07, c08, c10, R08, g24, g28]
```

---

## V06 · 改标 / 重整 Form FDA 766 授权门

```yaml
id: V06
slug: fda-766-reconditioning-authorization
title: 改标 / 重整 Form FDA 766 授权门
type: framework
importance: high
importance_reason: |
  BOOK_OVERVIEW 优先级 2 子链、核心命题 9。「未经批准的自行整改不产生放行效力」与
  「第二次机会的举证对象是方法而非态度」都是强反直觉口径，直接命中用户给的
  『进口商收到 Detained 通知后想自行改标再申报』场景。
one_liner: "重整效力来自『importer of record 申请 → FDA 766 批准并载明条件与时限 → 复核』三段，企业自行返工无效；首次失败后第二次机会的门槛是修订后的方法能合理保证成功，且 rejects 仍须单独拒绝销毁。"
intents:
  - "收到 Detained 通知后判断能否自行改标/返工再申报"
  - "判断重整申请应由谁提交、需不需要新 bond"
  - "首次重整失败后判断是否还能再试一次、要举证什么"
  - "合格部分放行后判断 rejects 该如何处置"
  - "理解 FDA 766 / Importer's Certificate / FDA 790 在链条中的位置"
keywords: ["Form FDA 766", "Reconditioning", "Relabeling", "importer of record", "Released after Reconditioning", "rejects", "revised method", "reasonable assurance of success", "redelivery bond", "自行整改无效", "Importer's Certificate"]
merged_from: [f07, p14, c08, x09, g09]
source_evidence:
  - "IOM 6.5.2.3 [p.40]：FDA may authorize relabeling… upon timely submission of Form FDA 766；批准后退回原件列明 conditions 与 time limit；已备案 redelivery bond 适用，无须新 bond"
  - "IOM 6.5.2.4 [p.40]：完成后提交 Importer's Certificate（766 第 2 页）或告知完成，FDA 可复核查验/取样或仅接受声明"
  - "IOM 6.5.2.5 [p.40]：条件满足 → Notice of Release『Released after Reconditioning』；rejects 仍须销毁或再出口并单独出具 Refusal"
  - "IOM 6.5.2.6 [p.40]：a second attempt should not be considered unless a revised method of reconditioning shows a reasonable assurance of success"
  - "IOM 6.1.3 [p.6]：FDA 才有权判定物品能否经重整带入合规并授权重整，监督由 FDA 或 CBP 按就近/远程约定"
  - "IOM 6.9.65 / 6.9.68 [p.57]：申请主体是 importer of record；Relabeling is considered a form of reconditioning"
V1_cross_domain:
  passed: true
  independent_contexts:
    - context: "6.5.2.3 / 6.5.2.5 [p.40]（对象：被扣货物的改标/重整申请）"
      conclusion: "效力三段 = 申请 + 批准（条件与时限）+ 复核；条件满足才放行，rejects 单独拒绝"
    - context: "6.5.2.6 [p.40]（对象：首次重整失败的申请）"
      conclusion: "第二次机会门槛落在『修订后的方法能否合理保证成功』，不是企业愿不愿意再试"
    - context: "6.1.3 [p.6]（对象：法定授权层，属不同 6.x 节）"
      conclusion: "只有 FDA 有权判定可否经重整达合规并授权，监督由 FDA 或 CBP 按就近/远程约定——授权来源与 6.5 的执行层不同"
    - context: "6.9.65 / 6.9.68 / 6.5.2.9 [p.57]/[p.41]（对象：术语与费用）"
      conclusion: "申请主体是 importer of record、改标 ⊂ 重整；监管费用走 FDA 790 向 CBP 收取，FDA 分部不得收款"
  reasoning: "四个语境分属 6.1 / 6.5 / 6.9，对象分别是申请流程、失败重试、法定授权、术语与费用，结论分别是三段效力、方法门槛、授权主体、主体/费用口径。"
V2_predictive_power:
  passed: true
  novel_question: "进口商收到 Detained 通知后，不等 FDA 回复就自行撕标重贴、分选返工，随后按原申报重新提交一次，认为『整改完自然获得放行』；首次被拒后又原样再试一次。这套做法为什么不产生放行效力？"
  derived_answer: |
    ① 重整的法律效力来自『**FDA 授权 + 按批准条件执行 + FDA/CBP 复核**』三段，
    不是企业单方返工（6.1.3、6.5.2.3）：须由 **importer of record** 及时提交 Form FDA 766
    （或函件 + 足额 bond；已备案 redelivery bond 适用、无须新 bond），FDA 批准并载明
    条件与完成时限，完成后提交 Importer's Certificate（766 第 2 页）或告知完成，
    再由 FDA 复核查验/取样或接受声明，满足条件才发『Released after Reconditioning』。
    手册用 `may authorize` / `approval or disapproval` 明示这是**机构裁量**而非企业权利。
    ② 自行整改不产生放行效力，货物仍按违规处理 → Refusal + 90 天出口销毁 + Bond Action。
    ③ 首次失败后第二次机会的举证对象是『**修订后的方法本身能合理保证成功**』，
    原样再试（只改执行日期）不构成修订方法，原则上不予考虑（6.5.2.6）。
    ④ 即便条件满足放行，rejects 仍须在 FDA/CBP 监督下销毁或再出口并**单独**出具
    Refusal，FDA 还可限定只销毁不出口。
  why_nontrivial: "直觉把返工当内部质量动作、把第二次机会当『态度问题』；实际举证对象是方法、效力来源是对岸授权、且部分放行不等于整批结案。"
V3_exclusivity:
  passed: true
  institution_specific_calibration:
    - "未经批准的**自行整改不产生放行效力**——返工不是企业内部质量动作，是须 FDA 授权并监督的法定程序"
    - "申请主体是 **importer of record**（不是 FSVP Importer、不是境外生产商）；改标 ⊂ 重整，不是并列动作"
    - "第二次机会门槛落在『修订后的方法能合理保证成功』，举证对象是方法而非意愿"
    - "合格部分放行 ≠ 整批结案：rejects 仍须单独 Refusal + 监督销毁/再出口，FDA 可限定只销毁不出口"
    - "已备案的 redelivery bond 适用于获批改标，**无须另立新 bond**"
    - "监管费用付给 CBP（FDA 790），任何 FDA 分部办公室不得代收监督费"
  why_not_common: "常识是『东西修好了就该放行、多试一次总有诚意』；本单元说整改本身没有法律效力、第二次机会看方法不看态度、且放行一部分还要为不合格部分单独走拒绝链。"
overlap_risk:
  - "V05（处置主链）：本卡是其 766 子链，路由高度相邻"
  - "V09（概念区分树）：抢 Reconditioning / Relabeling 术语"
  - "V10（效力层元规则）：`may authorize` 属机构裁量，可能被当成企业权利"
  - "包内既有【过敏原控制 / 排产 / 返工】类 CAP：企业侧『返工』概念可能抢路由"
differentiator: "本卡只管 **FDA 766 授权门及其内部判据**（申请主体、批准条件与时限、第二次机会门槛、rejects 单独处置），不展开听证→拒绝→90 天→Bond 的全链（V05）、不定义术语（V09）、不下法律位阶结论（V10）。企业侧『返工』在本卡中被明确标注为不产生放行效力，与包内生产返工类 CAP 的语境不同。"
supporting_refs: [f06, c10, x13, g14]
```

---

## V07 · Failure to Hold 判定与 8 步调查清单

```yaml
id: V07
slug: failure-to-hold-investigation
title: Failure to Hold 判定与 8 步调查清单
type: framework
importance: critical
importance_reason: |
  BOOK_OVERVIEW 优先级 3、核心命题 11，用户点名的头号反直觉口径。定义要件
  『无放行而分销 ≠ 移出港区』直接决定企业是否构成违规，且与条件放行概念强绑定；
  8 步清单 + 健康危害/DWPE 加重是可直接执行的调查下限。
one_liner: "Failure to Hold 的判定要件是『未获 FDA 放行即已分销』，不是『货物被移出港区』；所有该类案件统一走 8 步取证，健康危害/DWPE 情形再追加召回与公共警告协调，30 天与 90 天按 4647 签发依据区分。"
intents:
  - "判断某批条件放行货物是否已构成 Failure to Hold"
  - "区分『移库/位移』与『分销』在违规认定上的差别"
  - "列出所有 FTH 案件必做的 8 步取证与 affidavit 要求"
  - "判断健康危害 / DWPE 情形是否须追加召回、收货人通知、公共警告"
  - "判断 CBP 4647 的 redelivery 期限该用 30 天还是 90 天"
  - "企业侧〔推导〕理解放行前须保持货物 intact 且不进入分销"
keywords: ["Failure to Hold", "无放行而分销", "distribution not movement", "8 steps", "affidavit", "CBP 4647", "30 days vs 90 days", "Salmonella", "RTE food", "DWPE 加重", "Recall and Emergency Coordinator", "Bond Action", "Substitution"]
merged_from: [f11, p09, p10, c12, x01, x02, g11]
source_evidence:
  - "IOM 6.6.4.1 [p.43]：Failure to hold means… distributed… without an FDA release… *Please note that this is defined as distribution without a release, not merely moving the goods outside of the port area."
  - "IOM 6.6.4.1 [p.43]：8 步清单（单据→分销记录→授权人→健康危害知悉→授权人说明+affidavit→ORADSS 历史→CBP 4647→bond 核定）；第 7 步 deadline for redelivery is 30 days, instead of the 90 days post-refusal"
  - "IOM 6.6.4.2 [p.43-44]：直接证据的重大健康危害（RTE 食品检出 Salmonella）= highest priority，追加召回/通知/公共警告协调"
  - "IOM 6.6.4.3 [p.44]：仅达 §801(a) 外观违规标准的 DWPE 情形仍为 high priority，追加是否取样 + 同样召回协调"
  - "IOM 6.9.30 [p.53]：术语表逐字复述定义并指向 redelivery bond"
  - "IOM 6.9.13 [p.51]：The goods may be moved but CBP can request redelivery within 30 days"
  - "IOM 6.6.4.4 [p.44]：Substitution 在查明前一律按『实际货物无 FDA 放行而分销』处理，回指 6.6.4.1"
V1_cross_domain:
  passed: true
  independent_contexts:
    - context: "6.6.4.1 [p.43]（对象：被分销货物的定义与调查）"
      conclusion: "要件是『无放行而分销』而非位移；8 步为所有该类案件必做下限，①–⑤ 须作成 affidavit"
    - context: "6.6.4.2 / 6.6.4.3 [p.43-44]（对象：含健康危害 / DWPE 历史的 RTE 食品，属不同结论）"
      conclusion: "按证据强度分最高优先级 / 高优先级两档，均在 8 步外追加召回、收货人通知、公共警告协调"
    - context: "6.6.4.4 [p.44]（对象：Substitution 调包案）"
      conclusion: "查明前一律按 FTH 处理并回指 8 步，且须查验整批以封堵『未查验部分未被顶替』抗辩"
    - context: "6.9.13 / 6.9.30 / 6.5.2.11 [p.51,p.53,p.42]（对象：术语与 bond 后果，属不同 6.x 节）"
      conclusion: "货物 may be moved（位移合法）；只有『放行前已分销且无法 redelivery』才触发 Bond Action"
  reasoning: "四个语境分属 6.5 / 6.6 / 6.9，对象分别是 FTH 定义、健康危害分级、调包案、术语与 bond，结论分别是要件与取证下限、加重分支、推定规则、责任后果。"
V2_predictive_power:
  passed: true
  novel_question: "某企业出口冷冻罗非鱼片到美国，货已条件放行但尚未收到 FDA May Proceed，就把货发给了经销商；企业辩称『货一直在保税仓/港区内、只是移库，不算违规』。用本单元判定？"
  derived_answer: |
    辩解不成立，且恰好踩中手册特意加 `*Please note` 纠偏的误读。① 判定要件是
    『**未获 FDA release from import status 即已分销**』，位置变化本身**不构成**该违规
    （6.6.4.1 / 6.9.13 明说 goods may be moved）——所以『还在港区』不是抗辩理由；
    反过来，『发往经销商』已构成 distribution，即便货物物理上仍在港区内也成立。
    ② 一旦成立，8 步清单对**所有**该类案件必做：取单据、分析分销记录、确定授权人
    （可能不止一个责任方）、判断是否知悉健康危害、取授权人说明并作成 affidavit、
    ORADSS 检索历史、协调 CBP 签发 4647、核定 bond。③ 4647 若因查验/取样签发，
    redelivery 期限是 **30 天**而非拒绝后的 90 天（6.6.4.1 第 7 步），且 4647
    可为查验/取样而发、不必先有 FDA 拒绝。④ 若该批命中 Import Alert/DWPE 或涉
    Salmonella 等健康危害，即便证据仅达『外观违规』标准仍属高优先级，须在 8 步外
    追加召回、收货人通知、公共警告协调。⑤ 已发经销商导致无法召回 → Bond Action。
  why_nontrivial: "直觉按『位置/位移』判断违规，手册按『放行状态 + 分销动作』判断；且『发经销商』与『仍在港区』可以同时为真却仍构成违规，这是外行第一眼一定会答错的点。"
V3_exclusivity:
  passed: true
  institution_specific_calibration:
    - "Failure to Hold = 『无放行而分销』，**不是**『货物被移出港区』；原文用 `*Please note` 显式纠偏，说明作者预期读者会弄错"
    - "条件放行期内货物『may be moved』——位移合法，法律状态未变，位置与法律状态被刻意解耦"
    - "8 步清单用 `should` 却写 `on all … cases`，是准硬性下限；①–⑤ 须固化成 **affidavit（宣誓书）**而非普通访谈记录"
    - "Form 4647 可仅为查验/取样而签发，不必先有 FDA 拒绝；此时 30 天而非拒绝后 90 天"
    - "Substitution 在查明前一律按 FTH 处理（举证责任倒置式推定），且须查验整批"
    - "DWPE 是『不检查就扣住』，其违规史本身即风险信号；命中后即便仅达外观违规标准仍属高优先级，绝非低风险放过"
  why_not_common: "常识按『货动没动、出没出港区』判断违规；本单元按『有没有放行、有没有分销』判断，且把『不检查』读成加重信号——两处都是反直觉的机构口径。"
overlap_risk:
  - "V04（时间窗）：抢『条件放行 / 30 天』路由；用户示例同时命中两卡"
  - "V09（概念区分树）：抢 Conditional Release / FTH 术语"
  - "R05（四类违规模式，已淘汰并入本卡）：Substitution / misdeclaration 可能仍抢路由"
  - "包内既有【放行 / 分销控制】类 CAP：企业侧 WMS 发货闸门可能抢路由"
differentiator: "本卡只认定 **FTH 违规要件并给出 8 步取证下限与加重分支**，不算条件放行期倒计时（V04）、不定义状态词（V09）、不展开 importer/filer 责任分流（已并入本卡作佐证，见 R05）。用户示例『条件放行后未收 May Proceed 即发经销商』应路由到本卡，V04 只提供 30 天窗口背景。"
supporting_refs: [f12, x03, x08, g12, g13, R05]
```

---

## V08 · FSVP 检查链与 FDA 483a 签发门

```yaml
id: V08
slug: fsvp-inspection-483a-gate
title: FSVP 检查链与 FDA 483a 签发门
type: framework
importance: high
importance_reason: |
  BOOK_OVERVIEW 优先级 4，与用户既有 HACCP / 预防控制工作直接衔接；但既有技能包
  已有 **CAP-21（CP 7303.878 FSVP 检查）**，重叠风险最高，须靠 differentiator 严格区分，
  故列 high 而非 critical。
one_liner: "FSVP 检查对象是进口商的记录（非货物）；须先把自己的潜在危害初步评估与进口商危害分析比对并追问差异理由；FDA 483a 只在检查结束（closeout）时签发且只签已签名版，检查期间不得展示任何草稿/未签版/电子稿。"
intents:
  - "判断 FSVP 检查对象与 Importer of Record 的区别"
  - "现场检查期间能否向企业展示 483a 草稿"
  - "判断观察项该写进 483a、T-EIR 还是 CARS"
  - "理解危害分析比对与差异追问的检查动作"
  - "计算 FDA 483a 的 15 工作日回应窗口"
  - "判断 importer 不满足定义时 EIR 该怎么处理"
keywords: ["FSVP", "FDA 483a", "T-EIR", "EIR", "closeout", "已签名版", "hazard analysis 比对", "importer 定义", "U.S. agent", "Very Small Importer", "15 business days", "CARS", "FDA 482d", "21 CFR 1.500"]
merged_from: [f13, g14]
source_evidence:
  - "IOM 6.8.1.1 [p.46]：核实 entry 上标识者是否为 21 CFR 1.500 定义的 importer、食品是否受 FSVP 约束；判定是否 PC/HACCP/Produce Safety 覆盖"
  - "IOM 6.8.1.4.1 [p.47]：Compare your preliminary assessment of potential hazards to the importer's hazard analysis. If there are discrepancies, discuss… to determine their reasoning"
  - "IOM 6.8.2.1 [p.48-49]：The FDA 483a should only be issued at the conclusion of the inspection… respond within 15 business days after the end-date"
  - "IOM 6.8.2.1 [p.48]：Use care, during the inspection, to not show or reveal to the firm's management any draft, unsigned copy… or electronic copy"
  - "IOM 6.8.3.1.1 [p.50]：EIR 须记录危害分析比对结果、importer 定义三类证明；纠正措施及预计完成日期记 CARS"
  - "IOM 6.9.40 / 6.9.43 [p.55]：FSVP Importer 须位于美国境内；Importer of Record 是 CBP 报关/bond 主体，二者常非同一人"
  - "IOM 6.8.1.3 [p.47]：记录审查权依 §805、21 CFR 1.510/1.512"
V1_cross_domain:
  passed: true
  independent_contexts:
    - context: "6.8.1.1 / 6.8.1.4.1 [p.46-47]（对象：检查前准备与现场记录审查）"
      conclusion: "先核实 importer 定义与 FSVP 适用性，再把监管方初步危害评估与进口商危害分析比对、追问差异理由"
    - context: "6.8.2.1 / 6.8.2.1.1 [p.48-49]（对象：观察项文书，属不同判定环节）"
      conclusion: "483a 只在 closeout 签发且只签已签名版；存疑重要性的观察项不列入 483a，纠正措施不写在 483a 而报 T-EIR"
    - context: "6.8.3.1.1 [p.50]（对象：EIR / CARS 报告）"
      conclusion: "报告须记录危害分析比对结果、importer 定义三类证明（owner/consignee 附订单、U.S. agent 附书面协议、不满足定义则说明并取实际进口商信息）"
    - context: "6.9.40 / 6.9.43 / 6.1.6.2 [p.55]/[p.13]（对象：术语身份层，属不同 6.x 节）"
      conclusion: "FSVP Importer（FSMA 供应商验证，须在美国境内）与 Importer of Record（CBP 报关/bond）是两套法律身份，常非同一人"
  reasoning: "四个语境分属 6.1 / 6.8 / 6.9，对象分别是检查准备、观察项签发、报告、身份术语，结论分别是比对动作、签发门、记录字段、身份分野。"
V2_predictive_power:
  passed: true
  novel_question: "调查员在 FSVP 检查第 2 天发现进口商危害分析漏了某过敏原危害，当场打印一份未签名的 483a 草稿交给管理层『先看着准备』，并把企业承诺的整改措施写进了这份草稿。这样做错在哪？"
  derived_answer: |
    至少四处违规。① 6.8.2.1 明确 483a **只在检查结束（closeout）时签发且只签已签名版**，
    检查期间不得向管理层展示任何 draft / unsigned copy / 屏幕电子稿。② 检查动作顺序
    反了：应先把监管方自己的『潜在危害初步评估』与进口商危害分析**比对**，若有差异
    先与进口商讨论、确定其差异背后的**理由**（6.8.1.4.1），而不是直接下『漏了危害』
    的结论。③ 存疑重要性的观察项**不列入** 483a（当场讨论并记 T-EIR）；观察项须
    『显著且与被检查产品相关、按显著性排序、清晰具体』。④ **纠正措施不写在 483a 上**，
    须报在 T-EIR 并把纠正措施及预计完成日期记入 CARS（6.8.3.1.1）。⑤ 483a 发出后
    应告知进口商在检查结束日后 **15 个工作日**内回应，且其回应可能影响 FDA 是否
    采取后续行动的判定。
  why_nontrivial: "直觉是『发现问题早点告知、帮企业准备整改』；实际手册禁止检查期间展示草稿、要求先比对追问理由、且把纠正措施与观察项分到两套文书——外行几乎必然反着做。"
V3_exclusivity:
  passed: true
  institution_specific_calibration:
    - "483a **只在 closeout 签发且只签已签名版**；检查期间展示草稿/未签版/电子稿被明文禁止"
    - "存疑重要性的观察项不列入 483a（当场讨论、记 T-EIR）；纠正措施不写在 483a 而报 T-EIR / CARS"
    - "检查动作是『把自己的潜在危害初步评估 vs 进口商危害分析』比对并追问差异理由，不是直接判定漏项"
    - "FSVP 检查对象是**进口商的记录**，与货物查验是并行的独立合规轨（6.2.4 货物准入勿混同）"
    - "FSVP Importer ≠ Importer of Record：前者须位于美国境内、属 FSMA；后者属 CBP 报关/bond，二者常非同一人"
    - "483a（FSVP 观察项）与 CAP-18 的 483（Ch.5 现场检查观察项）是不同文书"
  why_not_common: "常识是『检查发现问题就出观察项、让企业整改』；本单元说观察项有唯一签发时点、草稿不得示人、纠正措施另走报告，且检查对象根本不是货而是记录。"
overlap_risk:
  - "**CAP-21（CP 7303.878 FSVP 检查）：重叠风险最高**——同主题，可能直接抢路由"
  - "**CAP-18（IOM Ch.5 检查员权限与 483）**：483 与 483a 名称相近，极易混引"
  - "包内既有【危害分析 / HACCP / 预防控制】类 CAP：『危害分析比对』可能抢路由"
  - "V10（效力层元规则）：`should only be issued` 属 `should` 承载唯一时点，可能抢 Boundary 路由"
differentiator: "CAP-21 是 FSVP **合规程序 / 检查依据（CP 7303.878）**；本卡是 **IOM 6.8 的检查执行 SOP**：483a 的 closeout 唯一签发门与签署政策、监管方初步危害评估 vs 进口商危害分析的比对追问、importer 定义三类证明、15 工作日回应、T-EIR/EIR/CARS 分流。**483a ≠ 483**：CAP-18 的 483 是 IOM Ch.5 现场检查观察项，与本卡的 FSVP 观察项分属不同章节与文书序列，正对应『二十类不可混引』。阶段 4 应专门设计『483 / 483a 混用』负例。"
supporting_refs: [c10, g25, p12, R09]
```

---

## V09 · 进口状态概念区分树（放行 / 扣留 / 条件放行）

```yaml
id: V09
slug: admission-status-concept-tree
title: 进口状态概念区分树（放行 / 扣留 / 条件放行）
type: glossary-framework
importance: high
importance_reason: |
  本轮**唯一**允许 glossary 独立成能力卡的例外：这组术语本身构成判定框架
  （用户明确点名「扣留/放行/条件放行」概念区分树）。它是消除「二十类不可混引」
  的口径前置层，直接决定企业能否把某状态理解为「可分销」。
one_liner: "先把状态词归位：Conditional Release 是等待判定的状态（可移动不可分销、附 3 倍货值 bond），May Proceed / Release / IB Release / Release with Comment 是四种法律含义不同的放行，Detention 临时可回转，Refusal 终局但非终点；三个『30 天』与一个『90 天』分属不同窗口。"
intents:
  - "判断某个 FDA 状态词到底意味着『能不能分销』"
  - "区分 May Proceed / Release / IB Release / Release with Comment 四种放行"
  - "区分 Conditional Release 与 May Proceed（等待状态 vs 结束该状态的决定）"
  - "区分 Detention（临时）与 Refusal（终局但非终点）"
  - "区分三个 30 天与一个 90 天窗口"
  - "判断『货可以移动』是否等于『货可以销售』"
keywords: ["May Proceed", "Release", "IB Release", "Release with Comment", "Conditional Release", "Detention", "Refusal of Admission", "No compliance decision has been made", "可移动不可分销", "三个30天", "90 days", "AGR", "Re-export", "概念区分树", "同形异义 IB"]
merged_from: [g01, g02, g04, g27, g28, x14]
source_evidence:
  - "IOM 6.4.3 [p.35]：May Proceed =『未经 FDA 查验、No compliance decision has been made』；Release =『查验后放行、A compliance decision has been made』"
  - "IOM 6.9.56 [p.56]：May Proceed 是放行、产品可进入美国流通，但 does not preclude future FDA action"
  - "IOM 6.9.13 / 6.9.41 [p.51,p.55]：Conditional Release 期间 goods may be moved 但 CBP 可 30 天内要求 redelivery；以 May Proceed 或拒绝结束"
  - "IOM 6.9.21 [p.52]：Detention = temporary administrative action，基于 appear not to be"
  - "IOM 6.9.44 / 6.5.2.8 [p.55]/[p.41]：Refusal = final decision，但档案到销毁/出口证明才关闭"
  - "IOM 6.3.10.7 / 6.3.11 [p.32]：IB Release 的 IB 指 Investigations Branch（非 Import Bulletin），Class 2 有不良发现仍可裁量放行但须详述理由"
  - "IOM 6.9.69 [p.57]：Release with Comment = 已明确认定存在违规（无公共健康风险）仍放行，并预告后续同类 entry 可能被拒"
  - "IOM 6.9.1 / 6.9.67 [p.50]/[p.57]：AGR 美国货退回视为进口（§801(d)(1)）；Re-export 不适用 §801(e)"
  - "IOM 6.9.25 / 6.9.28 [p.53]：Entry 是报关行为、Line 是可单独判定的最小单元"
V1_cross_domain:
  passed: true
  independent_contexts:
    - context: "6.4.3 / 6.9.56 [p.35]/[p.56]（对象：系统两条放行消息）"
      conclusion: "May Proceed 未作合规判定、Release 已作合规判定，二者不可互换；放行不排除后续 §304(d) 执法"
    - context: "6.9.13 / 6.2.4 [p.51-52]/[p.20]（对象：条件放行状态）"
      conclusion: "是等待判定期间的状态（可移动不可分销），与『结束该状态的决定』May Proceed 是不同范畴"
    - context: "6.3.10.7 / 6.9.69 [p.32]/[p.57]（对象：现场放行与附意见放行，属不同 6.x 节）"
      conclusion: "IB Release 由调查分部在查验后作出、Release with Comment 是已认定违规仍放行并预告后续拒绝——放行动作有四种且法律含义不同"
    - context: "6.9.1 / 6.9.67 / 6.9.44 [p.50,p.57,p.55]（对象：法定例外与窗口）"
      conclusion: "AGR 视为进口、Re-export 不受 §801(e) 约束；90 天（Refusal 后）与三个 30 天分属不同窗口，误用即期限全错"
  reasoning: "四个语境分属 6.2 / 6.3 / 6.4 / 6.9，对象分别是放行消息、状态、放行种类、法定例外与窗口，结论分别是合规判定有无、状态与决定的范畴差、四种放行不可统一映射、窗口不可混用。"
V2_predictive_power:
  passed: true
  novel_question: "某企业把内部 WMS 状态机里的四种 FDA 文书（May Proceed、Release、IB Release、Release with Comment）统一映射成『放行 = 可销售 + 已合规、此批结案』，并把 CBP 的 immediate delivery 回执也归到同一状态。这个状态机会导致哪些具体误判？"
  derived_answer: |
    至少四处。① **May Proceed** 按 6.4.3 是『未经查验、No compliance decision has been
    made』——可分销但**不是合规背书**，且可被 rescind、日后发现违规仍可依 §304(d) 执法；
    把它当『已合规』会让企业误以为免除后续责任、并错过撤消窗口。② **Release with Comment**
    是已明确认定存在违规（只是无公共健康风险）仍放行，且**预告后续同类 entry 可能被拒**，
    它会进入合规历史影响 PREDICT / DWPE / Import Alert 判定——当『没问题』会使企业不整改、
    后续被拒时毫无准备。③ **IB Release** 的 IB 指 Investigations Branch（不是 Import
    Bulletin），且 Class 2 有不良发现时属裁量放行、须在 Summary 详述理由；与 May Proceed
    所处阶段、主体、是否经查验均不同。④ **CBP immediate delivery / Conditional Release
    根本不是放行**：货仍处 FDA 管辖、可移动但不可分销、附 3 倍货值 redelivery bond，
    以它安排上架销售直接构成 Failure to Hold（V07）+ Bond Action。⑤ 若再叠加把
    三个 30 天（条件放行期长度 / CBP 请求 redelivery 窗口 / FTH 下 4647 期限）与
    一个 90 天（Refusal 后出口销毁）混用，所有倒计时计算全错。
  why_nontrivial: "直觉把『放行』当单一终态；区分树推导出四种放行 + 一个非放行状态各自不同的可分销性、合规判定、后续风险与窗口，且其中一个（Release with Comment）反而预示下一批会被拒。"
V3_exclusivity:
  passed: true
  institution_specific_calibration:
    - "May Proceed 字面像『准许继续办理』，实为终局放行动作；且系统定义明确『未作合规判定』"
    - "DWPE 字面『不检查』实为『不检查就扣住』；Conditional Release 字面『有条件地合格』实为『仍在 FDA 管辖、须保持可召回』"
    - "三种术语误读方向一致：**都高估自身合规状态**——这是全书最系统的一组反直觉"
    - "放行有四种（May Proceed / Release / IB Release / Release with Comment）且法律含义不同，不可统一映射"
    - "三个『30 天』与一个『90 天』同数异义：条件放行期长度 / CBP redelivery 窗口 / FTH 4647 期限 / Refusal 后出口销毁"
    - "『IB』同形异义：Import Bulletin vs Investigations Branch；『货可以移动』≠『货可以分销』"
    - "AGR（美国货退回）视为进口 §801(d)(1)；Re-export（外国货进出）不适用 §801(e)——方向相反的两条例外"
  why_not_common: "常识是『放行就是合格、扣留就是不合格』；本单元是一整套把字面语义整体反转的机构口径树，且错位方向一致（都让人误以为自己更合规），外行不可能自行推出。"
overlap_risk:
  - "**与 V01 / V04 / V05 / V07 全部抢路由**（状态词贯穿全链），是阶段 1.6 晋级门重点审视对象"
  - "V02（DER/DTR）：抢 DWPE / Detention 术语口径"
  - "包内既有【放行 / 状态判定】类 CAP：『可分销』闸门可能抢路由"
  - "『二十类不可混引』：本卡是防混引的口径前置层，本身也最易被误当成业务判定卡"
differentiator: "本卡是**口径判定层**——只回答『这个状态词意味着什么、能不能分销、属于哪个窗口』，**不产出动作**（V01）、**不算时限倒计时**（V04）、**不展开处置链**（V05）、**不认定违规**（V07）。阶段 4 应设计『把 Conditional Release 当放行』『把 Release with Comment 当无记录』『把 30 天与 90 天混用』三组负例。"
supporting_refs: [g03, g05, g08, g11, g26, g22, f04, f06, R06]
```

---

## V10 · IOM 效力层判读元规则（法律位阶与情态分层）

```yaml
id: V10
slug: iom-effect-level-modality
title: IOM 效力层判读元规则（法律位阶与情态分层）
type: meta
importance: critical
importance_reason: |
  BOOK_OVERVIEW §3「最强反对意见」+ 全部能力卡的 Boundary (B) 字段来源，也是 p12
  元规则与 x13 反例的落点。若不单独成卡，下游 9 张卡会系统性把 IOM 当法规、
  把 should 当 shall，直接违反『二十类不可混引』的法律位阶约束。
one_liner: "IOM 是内部操作指导、不是法规；must/shall/祈使 = 审查员硬性作业动作，should/as warranted/may = 机构裁量且几乎不给判据；任何结论须回到 FD&C Act §801、21 CFR Part 1、19 CFR 113.62 与当前版本 IOM/RPM 复核。"
intents:
  - "判断某条 IOM 表述能否对企业主张为法定义务或权利"
  - "把 should / as warranted / may 与 must / shall 分开读"
  - "识别 `should only` / `should not` 这类『用裁量词承载禁止/唯一时点』的反向陷阱"
  - "判断指导文件（CPG / IOM）是否构成豁免或宽限"
  - "理解 IOM 是 2026 版快照、系统编号会随改版失效"
  - "为企业侧迎检推导内容标注『推导·非原书主张』"
keywords: ["IOM 不是法规", "must vs should", "as warranted", "机构裁量", "FD&C Act §801", "21 CFR Part 1", "19 CFR 113.62", "legal hierarchy", "guidance does not limit", "版本快照", "Boundary", "should only", "should on all cases", "复核锚点"]
merged_from: [p12, x13]
source_evidence:
  - "BOOK_OVERVIEW §3 最强反对意见：IOM 是内部操作指导，不是法规，也不是可对外主张的法律依据；真义务来自 FD&C Act §801、21 CFR Part 1、19 CFR 113.62"
  - "IOM 6.1.5.5 [p.11]：This guidance… does not limit the FDA's ability… will not affect the ability of CBP to assess penalties under 19 U.S.C. 1595a(b)"
  - "IOM 6.2.2.2.2 [p.17]：You should only rescind a 'May Proceed' in rare cases… You **must** act immediately（同句 should 与 must 并存）"
  - "IOM 6.5.2.3 [p.40]：The FDA **may** authorize relabeling…（机构裁量而非企业权利）"
  - "IOM 6.6.4.1 [p.43]：The following steps **should** be taken on **all** Failure to Hold cases（裁量词覆盖全部个案）"
  - "IOM 6.8.2.1 [p.48]：The FDA 483a **should only** be issued at the conclusion of the inspection（should 承载唯一时点）"
  - "IOM 6.5.2.9 [p.41]：The expenses **shall** be computed… / Payment of supervisory charges **should not** be accepted by any FDA division offices"
  - "IOM 6.5.2.11 [p.42]：Under… FD&C Act §801(b) and 19 CFR 113.62, a bond is required（原文把义务锚回法条）"
V1_cross_domain:
  passed: true
  independent_contexts:
    - context: "6.1.5.5 [p.11]（对象：CPG 指导文件的效力）"
      conclusion: "guidance / policy 明确 does not limit FDA 权力、will not affect CBP 处罚权——指导不构成豁免"
    - context: "6.2.2.2.2 / 6.5.2.3 / 6.6.4.1 [p.17,p.40,p.43]（对象：情态动词分布，跨 3 个 6.x 节）"
      conclusion: "同一句可硬软并存；`should only` 承载禁止、`should … on all cases` 覆盖全部个案——映射不是纯机械的"
    - context: "6.5.2.11 / 6.1.4.6.1 / 6.9.47 [p.42,p.9,p.55]（对象：法条引用）"
      conclusion: "原文自身把义务锚回 §801(b) / §801(d)(3) / 21 CFR，说明 IOM 不是义务来源"
    - context: "6.5.2.9 / 6.8.2.1 [p.41,p.48]（对象：费用与观察项）"
      conclusion: "`shall` 是硬性计算、'should not be accepted' 是禁止、'should only be issued' 是唯一时点——三者形式不同但都不可省略"
  reasoning: "四个语境分属 6.1 / 6.2 / 6.5 / 6.6 / 6.8 / 6.9，对象分别是指导文件效力、情态动词、法条锚点、具体禁止，结论分别是『指导≠豁免』『should 不可一律译建议』『义务在法条』『形式_soft 语义_hard』。"
V2_predictive_power:
  passed: true
  novel_question: "某企业法务引用 IOM 6.2.4『You must make this decision before the conditional release period ends』，主张『FDA 逾期未作可采性决定即丧失扣留权，企业可自行分销』；并援引 CPG 指导里的宽限说明主张免检。这个主张成立吗？"
  derived_answer: |
    不成立，且是典型的效力层误读。① IOM 是**内部操作指导、不是法规，也不是可对外
    主张的法律依据**；真正义务来自 FD&C Act §801、21 CFR Part 1（Prior Notice / FSVP）、
    19 CFR 113.62 等。6.2.4 的 `must` 约束的是 **FDA 审查员的内部作业时限**，
    不产生企业的可诉权利；FDA 在个案中偏离 IOM 通常也不产生可诉权利。② 即便 FDA
    逾期，条件放行期届满也不等于『已放行』——按 6.2.4 窗口只是关闭，货物法律状态
    并未变成可分销；企业自行分销反而构成 Failure to Hold（V07）并触发 Bond Action。
    ③ CPG / IOM 的指导文字**不构成豁免**：6.1.5.5 原文明确该指导 does not limit FDA
    依 FD&C Act 采取必要行动的权力，也不影响 CBP 依 19 USC 1595a(b) 处罚。
    ④ 还须注意 IOM 是 **2026 版快照**，PREDICT / ITACS / ACE / WI-000618 /
    SOP-000217 等系统与 SOP 编号会随改版失效；任何结论须回到法条与当前版本
    IOM/RPM 复核。⑤ 全篇是**监管者视角**且默认 FDA 授权、系统权限、Compliance
    Branch / OCI / CBP 协作通道，企业不具这些前提，照搬会把『检查清单』误当
    『合规义务清单』。
  why_nontrivial: "直觉会认为『手册写了 must、对方没做到，我就获得权利』；本单元说该 must 约束的是对方内部作业、不产生企业权利，且『指导里的宽限』反而不限制对方执法——两层都反直觉。"
V3_exclusivity:
  passed: true
  institution_specific_calibration:
    - "IOM 是内部操作指导、**不是法规**、不是可对外主张的法律依据；把本章蒸馏成『合规规则引擎』会系统性高估法律位阶"
    - "`should` 与 `as warranted` 属机构裁量且章内几乎不给判据（留给分部惯例），不构成企业法定义务"
    - "**映射不是纯机械的**：`should only` / `should not` 形式软、语义却是禁止或唯一时点；反向 `should … on all cases` 用裁量词覆盖全部个案"
    - "同一句内可硬软并存（should only rescind / You must act immediately）"
    - "判据缺失本身是作者假设（请求扣留 vs 现场工作的选择标准、adverse conditions 阈值、照片 warranted 情形），应作为 Boundary 复核锚点，不应补写成规则"
    - "2026 版是快照；组织前提（FDA 授权 / 系统权限 / CB / OCI / CBP 通道）企业不具备"
  why_not_common: "常识是『官方手册写的就是规定、must 就是必须、should 就是建议』；本单元说手册本身不产生企业义务、`must` 只约束对方、`should` 有时反而是禁止——这是一套关于『如何读这份文件』的元规则，外行不可能自行推出。"
overlap_risk:
  - "**与全部 9 张业务卡抢 Boundary 路由**（它本就是共享边界层），阶段 1.6 晋级门须确认它不替代任何业务判定"
  - "V06（766 授权门）：`may authorize` 的裁量性质可能抢路由"
  - "V08（FSVP 483a）：`should only be issued` 的唯一时点可能抢路由"
  - "V03（Prior Notice）：x13 以 6.1.5.5 为锚点，可能抢『指导是否构成豁免』路由"
differentiator: "本卡**唯一的输出是『该结论的法律位阶与可主张性』**——回答『能不能据此主张义务/权利、该回到哪条法条复核、哪些词是裁量』，**不回答任何业务判定**（不放行、不扣留、不算时限、不认定违规）。它是全部卡的 Boundary (B) 字段来源，以及 x13/x14 与所有『企业侧迎检推导』内容必须冠以〔推导·非原书主张〕的约束来源，直接服务『二十类不可混引』与阶段 4 负例设计。"
supporting_refs: [x14, g19, g21, g23, R09, BOOK_OVERVIEW-§3]
```

---

## 附：通过单元索引（供阶段 1.6 晋级门）

| id | slug | title | type | importance | overlap_risk 最高项 |
|---|---|---|---|---|---|
| V01 | entry-review-admissibility-decision-gate | 入境审查决策门与可辩护判定留痕 | framework | critical | CAP-18 / CAP-28 |
| V02 | der-dtr-detention-routing | DER/DTR 按触发依据分流与 DWPE「不检查就扣住」 | framework | critical | V01 / CAP-18 |
| V03 | prior-notice-eligibility-gate | 事先通知（Prior Notice）适用性硬时限判定 | framework | high | V10（仅锚点） |
| V04 | conditional-release-rescission-windows | 条件放行 / 撤消 / redelivery 时间窗体系 | framework | critical | V07 / V09 |
| V05 | violation-disposition-chain | 违规处置主链与文书矩阵（拒绝不是终点） | framework | critical | V06 / V04 |
| V06 | fda-766-reconditioning-authorization | 改标 / 重整 Form FDA 766 授权门 | framework | high | V05 / V10 |
| V07 | failure-to-hold-investigation | Failure to Hold 判定与 8 步调查清单 | framework | critical | V04 / V09 |
| V08 | fsvp-inspection-483a-gate | FSVP 检查链与 FDA 483a 签发门 | framework | high | **CAP-21 / CAP-18（483≠483a）** |
| V09 | admission-status-concept-tree | 进口状态概念区分树（放行 / 扣留 / 条件放行） | glossary-framework | high | V01/V04/V05/V07 全部 |
| V10 | iom-effect-level-modality | IOM 效力层判读元规则（法律位阶与情态分层） | meta | critical | 全部卡的 Boundary |

**给阶段 1.6 / 阶段 4 的三点提示**
1. **V08 vs CAP-21 / CAP-18** 是最需要 differentiator 的一组：483a（IOM 6.8 FSVP 观察项）≠ 483（IOM Ch.5 现场检查观察项），建议专门设计混引负例。
2. **V09（口径层）与 V10（效力层）都不产出业务判定**，晋级门须确认它们作为「前置/边界层」而非独立路由，否则会与 V01/V04/V05/V07 抢路由。
3. **用户示例的路由**：『条件放行后未收 May Proceed 即发经销商』→ **V07**（FTH），V04 只提供 30 天窗口背景；『收到 Detained 后想自行改标再申报』→ **V06**（766 授权门），V05 提供其上下游链。
