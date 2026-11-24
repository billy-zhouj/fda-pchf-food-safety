# 蓄意掺假防护：食品防护脆弱性评估方法学（FDA 修订草案 2019-03，Part 1）（intentional-adulteration-draft-2019）

*来源分层：本卡取用**一份 FDA 草案指南**——FDA, Center for Food Safety and Applied Nutrition, 《Mitigation Strategies to Protect Food Against Intentional Adulteration: Guidance for Industry — Revised Draft Guidance》，**March 2019**，Docket `FDA-2018-D-1398`，159 页；页眉逐页标注 `Contains Nonbinding Recommendations` / `Draft-Not for Implementation`，封面写明 "This guidance is being distributed for comment purposes only."。它是**草案建议层**——比 CAP-36 的 2017-08 SECG（最终指南）还低半级：连 FDA 当前最终观点都不是，不得当作现行合规依据或 FDA 定论；`should` 只是建议，不创设义务。**但它解释的 21 CFR Part 121 规则本身有法律约束力**，法条一律回指 CAP-32〔§ 121.xxx〕。凡引自本件的方法/示例，出处写 `Revised Draft Guidance 章.节 [pdf-page N]`；凡属法定义务，仍写〔§ 121.xxx〕，**两种标识不可互换**。*

*⚠ **版本与文件名错位（最高频坑）**：用户补传的源文件名为 `2016-436 IA Guidance Part 1 061418.pdf`，`2016`／`061418` 均**不是**封面日期；本地研究目录曾名 `ia-2018-part1`，同样不是封面日期。封面与正文标记一致指向 **March 2019 / Revised Draft Guidance / 第二分册**：Ch.5／6／7／9 与 App.2／3 在本册标 `(coming soon)`，由 **2020-02 Supplemental Draft Guidance（CAP-38）** 补齐。本件新增内容以 `[New March 2019]`（Ch.2 F/G/H、Ch.8、App.4）与 `[Updated March 2019]`（App.1 D、缩写表）标记，**不得把新增标记当作「2019 年新规」**。三个 docket 不可混：本件 `FDA-2018-D-1398`、CAP-36 SECG `FDA-2013-N-1425`、2016 最终规则 `81 FR 34166`。*

*⚠ **效力层与全包口径**：本卡是 v4.24 为本包新增的**第二十九来源**、FDA 指南层**第 8 类**（草案子类第 1 份）。与 CAP-32（法条正文）是「法条—方法学」配对，与 CAP-36（2017-08 SECG 白话问答）是「最终指南问答—草案方法细节」配对，三者冲突时**以 CAP-32 法条为准、其次 CAP-36 最终指南、本卡最末**。本卡不覆盖纠正措施／验证／再分析／记录的操作细则（→ CAP-38），不覆盖 CARVER + Shock 与 Food Defense Plan Builder 操作、食品防护专项检查程序、经济利益驱动掺假（EMA → CAP-06）。全包现为**三十类来源不可混引**，其中法规正文仍为**十二套编号**（本件不新增编号）。*

*⚠ **页码与不可逐字引用区**：`[pdf-page N]` 采用**本件提取件 0-based 标记**（封面 0、目录 1–4、正文自 6 起），不是 PDF 阅读器页码，也不是 CAP-32／CAP-36 的页码基准。大量评分表、工作表（App.1 1-C～1-F）、场景表（表 3-1～3-4）、监控记录表（表 4-5～4-8）与流程图（Figure 2a-1／2b／2c 系列）为多栏错行或纯图形，**只能转述、不可逐字引**；页眉页脚不得作引文。评分表内的数字是 FDA 可选工具，不是法规阈值。*

---

## R — 原文

**① 草案效力：征求意见稿、120 日评议、非约束性、`should` 只是建议**：

> "This guidance is being distributed for comment purposes only."
> —— Revised Draft Guidance 封面 [pdf-page 0]；草案定位的第一句；后面所有方法都是「征求意见」中的建议。

> "All comments should be identified with the docket number FDA-2018-D-1398 listed in the notice of availability that publishes in the Federal Register."
> —— Revised Draft Guidance 封面 [pdf-page 0]；docket 锁定为 FDA-2018-D-1398，与 CAP-36 的 FDA-2013-N-1425 不同。

> "This draft guidance, when finalized, will represent the current thinking of the Food and Drug Administration (FDA or we) on this topic. It does not establish any rights for any person and is not binding on FDA or the public."
> —— Revised Draft Guidance I 引言 [pdf-page 6]；`when finalized` 是条件式——本件尚未成为 FDA 当前观点。

> "FDA's guidance documents, including this guidance, do not establish legally enforceable responsibilities."
> —— Revised Draft Guidance II Purpose [pdf-page 8]；指南不创设法律责任；只有回指具体法规时才产生义务。

> "The use of the word should in FDA guidances means that something is suggested or recommended, but not required."
> —— Revised Draft Guidance II Purpose [pdf-page 8]；`should` ≠ `shall`；本卡里的评分、频次、场景全是建议。


**② 豁免入口：豁免自动生效、举证式极小企业、液体储罐例外（法条在〔§ 121.5〕）**：

> "If a facility satisfies the requirements for an exemption under 21 CFR 121.5, then it receives the exemption; no application is necessary but some documentation may be required."
> —— Revised Draft Guidance IV Exemptions [pdf-page 15]；豁免无需申请，但部分情形须应要求举证。

> "The only IA rule requirement for a very small business (defined in 21 CFR 121.3) is that it must, upon request, provide for official review documentation sufficient to show that the facility meets the criteria for the exemption; such documentation must be retained for 2 years."
> —— Revised Draft Guidance IV.A Very Small Business [pdf-page 15]；极小企业是**举证式豁免**，支撑材料保存 2 年。

> "The IA rule requirements do not apply to the holding of food, except the holding of food in liquid storage tanks."
> —— Revised Draft Guidance IV.B Holding of Food [pdf-page 15]；holding 普遍豁免，但**液体储罐储存除外**——与 KATs 第一类直接咬合。


**③ KATs：四类关键活动类型（不是七类），落入即为 APStep**：

> "Key Activity Types (KAT): The four activity types identified by FDA through an analysis of the results of over 50 vulnerability assessments as the activities consistently ranked as the most vulnerable, regardless of the food commodity assessed."
> —— Revised Draft Guidance III.B Glossary — Key Activity Types [pdf-page 13]；**four**、over 50 次评估，来源为 FDA 与政府/行业伙伴的既有评估。

> "The four KATs are: bulk liquid receiving and loading, liquid storage and handling, secondary ingredient handling, and mixing and similar activities."
> —— Revised Draft Guidance III.B Glossary [pdf-page 13]；四类封闭枚举：散装液体收发货／液体储存与处理／次级配料处理／混合及类似活动。

> "Secondary ingredient handling includes any point, step, or procedure where dry or liquid secondary ingredients (e.g., inclusions, minor ingredients, processing aids, and food additives) are manipulated by human contact prior to or during addition to the product stream."
> —— Revised Draft Guidance Ch.2.D.3 Secondary Ingredient Handling [pdf-page 26]；第三类含 staging／preparation／addition／rework 四种人手接触形态。

> "Process steps that fit within one or more of the KATs are actionable process steps. Process steps that do not fit within any of the KATs are not actionable process steps and do not require mitigation strategies."
> —— Revised Draft Guidance Ch.2.E [pdf-page 27]；用 KATs 时，落入即 APStep、不落入即非 APStep 且无需策略；但「无 KAT」结论仍须书面留痕。


**④ 三要素评估：法规要求 vs 草案工具、内部人员、固有特征**：

> "The IA rule requires that your vulnerability assessment include consideration of the following three fundamental elements at each point, step, or procedure you evaluate (21 CFR 121.130(a)):"
> —— Revised Draft Guidance Ch.2.F [pdf-page 35]；`[New March 2019]` 新增章节；三要素的法定出处是〔§ 121.130(a)〕。

> "Note that if you are using KATs to conduct a VA, you do not need to separately consider the three fundamental elements because they are already incorporated into the KAT approach."
> —— Revised Draft Guidance Ch.2.F [pdf-page 35]；**KATs 已内含三要素**，不可叠加成「先 KAT 再逐点打分」的双重评估（除非走 hybrid）。

> "When you evaluate each of the fundamental elements, you must consider the possibility of an inside attacker."
> —— Revised Draft Guidance Ch.2.F.1.a [pdf-page 36]；内部人员是每要素的强制考量，不是单独一栏。

> "Failing to consider the possibility of an inside attacker likely would lead to artificially low scores for each of the fundamental elements and adversely affect identification of significant vulnerabilities."
> —— Revised Draft Guidance Ch.2.F.1.a [pdf-page 36]；漏评 insider 的直接后果是三要素分数整体偏低。

> "Inherent characteristics are conditions, activities, practices, or characteristics that are integral to the operation of a point, step, or procedure; the point, step, or procedure could not properly operate without these inherent characteristics in place."
> —— Revised Draft Guidance Ch.2.F.1.b [pdf-page 38]；固有特征参与 VA 打分；与之相对的 existing measures 不参与，留到选策略时再评（Ch.3.E）。

> "The IA rule does not require you to use a specific method to estimate potential public health impact, but the estimate should include potential acute illnesses, deaths, or both (or proxies such as servings at risk)"
> —— Revised Draft Guidance Ch.2.F.2 Element 1 [pdf-page 39]；法规不指定估算方法，但建议用急性疾病／死亡或 servings at risk 代理量。


**⑤ 评分与合成：一票否决、灰区、非统一阈值（均为 FDA 建议，不是法规）**：

> "A high score for one element does not automatically result in identification of a significant vulnerability at an actionable process step."
> —— Revised Draft Guidance Ch.2.G [pdf-page 58]；单一要素极高不等于显著脆弱性，避免「某要素 10 分就判 APStep」。

> "if one of the elements is assigned a score of 1, then the step does not have a significant vulnerability and is not an actionable process step"
> —— Revised Draft Guidance Ch.2.G.1 [pdf-page 58]；任一要素 = 1 即一票否决，无需再算总分。

> "this grouping of the highest scoring process steps includes approximately the top 20-25% of the scores for the rank ordered process steps"
> —— Revised Draft Guidance Ch.2.G.1 [pdf-page 58]；高分组经验上约为前 20–25%，是观察不是阈值。

> "We expect significant vulnerabilities will exist when each of the elements are highly scored, i.e., when a process step sum score is greater than or equal to 26"
> —— Revised Draft Guidance Ch.2.G.1 [pdf-page 59]；≥26 为 FDA 预期「存在显著脆弱性」，**不是法规数字**。

> "When a process step sum score is within 14-25, whether significant vulnerabilities are present depends on the nature of the vulnerability at the process step under evaluation and the contribution of each of the three elements in each case."
> —— Revised Draft Guidance Ch.2.G.1 [pdf-page 59]；14–25 灰区须逐案逐要素解释，也是最容易写空的区间。

> "Your vulnerability assessment must include a written explanation as to why each point, step, or procedure either was or was not identified as an actionable process step."
> —— Revised Draft Guidance Ch.2.G.2 [pdf-page 63]；逐点**双向**书面解释，法条在〔§ 121.130(c)〕；`was or was not` 两边都要写。


**⑥ Hybrid Approach：KATs 快筛 + 三要素深挖（可能识别出更少的 APStep）**：

> "In the hybrid approach, a facility first assesses each point, step, or procedure to identify steps that fit within any of the four key activity types. Then, rather than concluding the VA with those steps identified as the actionable process steps, the facility uses the three elements to conduct a more in-depth evaluation of some of the steps."
> —— Revised Draft Guidance Ch.2.H [pdf-page 64]；`[New March 2019]`；先 KATs 筛查，再对需进一步判断的步骤用三要素深挖，不是两套结果取并集。


**⑦ 缓解策略：两条路径、全厂措施、既有措施、上锁后仍是 APStep**：

> "Mitigation strategies are practices or conditions that are not inherent to the operation of a process step."
> —— Revised Draft Guidance Ch.3.A [pdf-page 66]；策略须**非固有**：固有特征是工艺本身，不能被当作策略。

> "minimize the accessibility of the product to an inside attacker (e.g., physically reducing access to the product, such as by locking storage tanks)"
> —— Revised Draft Guidance Ch.3.B [pdf-page 68]；路径一：降低产品可及性（加锁、限制进入）。

> "reduce the opportunity for an inside attacker to contaminate the product (e.g., increasing observation of the area through supervision or use of the buddy system)"
> —— Revised Draft Guidance Ch.3.B [pdf-page 68]；路径二：降低污染机会（加强监督、buddy system）；两条可叠加。

> "Facility-wide security measures do not require a VA to inform their identification and implementation."
> —— Revised Draft Guidance Ch.3.D [pdf-page 75]；围栏、外门上锁、全厂 ID 徽章属全厂安保，不需要 VA，规则也不要求；只对特定 APStep 定向时才升级为策略。

> "Generally, such measures are not, by nature, inherent characteristics of the process step's operation and the VA should not consider these practices when identifying whether the process step is an actionable process step."
> —— Revised Draft Guidance Ch.3.E [pdf-page 76]；既有质量/工安措施在 VA 阶段**不纳入**，留到策略阶段评估；放错阶段会重复计分。

> "Actionable process steps identified through a VA do not cease to become actionable process steps just because they are protected with mitigation strategies."
> —— Revised Draft Guidance Ch.3.E [pdf-page 78]；上了锁仍是 APStep，不能从计划里摘掉。

> "your food defense plan must identify your mitigation strategies, and each mitigation strategy must include an explanation of how the facility expects the mitigation strategy(ies) to significantly minimize or prevent the significant vulnerabilities associated with the actionable process step."
> —— Revised Draft Guidance Ch.3.F [pdf-page 78]；每条策略都须附「如何充分最小化/预防」的书面说明，法条在〔§ 121.135(a)〕。


**⑧ 监控：四问、频次弹性、同步记录、例外记录的适用限制**：

> "Your food defense monitoring procedures should answer four questions: (1) What will be monitored? (2) How will monitoring be done? (3) How often will monitoring be done (frequency)? and (4) Who will do the monitoring?"
> —— Revised Draft Guidance Ch.4.A [pdf-page 88]；监控程序四问，写进 FDP 的骨架。

> "You have the flexibility to determine the frequency of monitoring needed so long as the frequency is adequate to provide assurances that the mitigation strategies are consistently performed."
> —— Revised Draft Guidance Ch.4.D.1 [pdf-page 91]；频次由企业自定，标准是「足以保证持续执行」；FDA 不给数字。

> "All food defense monitoring information must be recorded at the time the observation is made."
> —— Revised Draft Guidance Ch.4.E [pdf-page 92]；监控信息须在观察当时记录，法条在〔§ 121.305(d)〕。

> "In some cases, you can document monitoring of a mitigation strategy with a record of when the mitigation strategy is not functioning, or operating, as intended."
> —— Revised Draft Guidance Ch.4.F [pdf-page 93]；例外记录只适用「部分情形」：静态锁具等必须肯定记录，自动化持续监控才可用例外记录。


**⑨ 培训：qualified individual、意识培训、无强制复训周期**：

> "A "qualified individual" is a person who has the education, training, or experience (or a combination of these) necessary to perform an activity required under subpart C, as it relates to their assigned duties."
> —— Revised Draft Guidance Ch.8.A [pdf-page 105]；`[New March 2019]`；定义来自〔§ 121.4〕，按职责匹配。

> "an individual assigned to an actionable process step must receive training in food defense awareness."
> —— Revised Draft Guidance Ch.8.B [pdf-page 106]；意识培训只强制给 APStep 岗位人员（及其主管），**不是全员**。

> "The IA rule does not include specific retraining frequency requirements; however, in most cases, individuals conducting activities with associated requirements for education, training, and experience should repeat training periodically and as necessary to ensure that they are qualified to perform their duties."
> —— Revised Draft Guidance Ch.8.E [pdf-page 108]；无固定再培训周期，但上岗前完成、职责变化/表现不正确时按需复训。


## I — 自述

本卡回答的不是「法条怎么定」，而是「按 FDA 自己的方法，脆弱性评估**怎么一步步做出来**」。2017-08 SECG（CAP-36）只说「FDA 不指定方法论」，2019-03 草案则把 FDA 自己设计的三条可选路径写透：KATs 快筛、三要素打分、两者混合。它把 CAP-32 的〔§ 121.130〕从「必须评三要素」推进到「怎么评、评完怎么判、怎么解释」。

| 环节 | 本卡给的方法口径 | 出处 | 与法条/SECG 的分工 |
|---|---|---|---|
| ① 先定方法 | KATs / 三要素 / Hybrid 三选一，FDA 不指定；用 KATs 不必再单独打三要素分 | Revised Draft Guidance Ch.2.E/F/H | 义务在〔§ 121.130〕；SECG 只说「方法自选」 |
| ② KATs 快筛 | **四类**关键活动类型，来自 50 余次 VA；落入即 APStep，不落入即非 APStep | Ch.2.D/E | 方法层，不是法定清单 |
| ③ 三要素打分 | 每点考虑内部人员 + 固有特征；1/3/5/8/10 五档为 FDA 可选工具 | Ch.2.F | 三要素本身是〔§ 121.130(a)〕法定；分值是建议 |
| ④ 判定合成 | 任一要素=1 一票否决；≥26 / ≤13 两端预期，14–25 灰区逐案解释 | Ch.2.G | 阈值全部是 FDA 预期，**不在法规里** |
| ⑤ 书面解释 | 逐点对「是/不是 APStep」双向说明；灰区解释最详细 | Ch.2.G.2 | 法条在〔§ 121.130(c)〕 |
| ⑥ 策略设计 | 两条路径（降可及性／降污染机会）+ 既有措施与全厂安保的正确落位 | Ch.3.B/D/E/F | 法条在〔§ 121.135〕 |
| ⑦ 监控与培训 | 四问、频次弹性、同步记录、例外记录边界；四类人员资格与意识培训 | Ch.4 / Ch.8 | 法条在〔§ 121.140〕〔§ 121.4〕 |

**四组最容易反直觉的口径：**

1. **KATs 是四类，不是七类。** 七类来自 FSMA 基础规则数或把 App.2 的 FDMSD 七大类误搬过来；本件 glossary 与 Ch.2.D 明写 `The four KATs`。FDMSD 的七大类（Conveyance／Material Handling／Packaging／Processing／Storage／Transportation-Distribution／KAT）是 CAP-38 Appendix 2 的分类表，与本件的四类 KATs 不是一回事。
2. **分数不是法规。** 1/3/5/8/10、≥26、≤13、14–25、前 20–25%、250 mg／85 kg／50% mortality 全是草案表格里的 FDA 工具与示例；Part 121 只要求评三要素和内部人员，**没有给任何分数阈值**。把阈值写成「法规要求」是本卡最严重的误用。
3. **固有特征与既有措施方向相反。** 固有特征（封闭设备、高速输送、多人互检）参与 VA 打分；既有措施（因质量/工安而设的资深员工定点、特殊工服、铅封）在 VA 阶段**根本不纳入**，留到 Ch.3 决定是否升为缓解策略。倒置会重复计算或漏评。
4. **本册不是完整指南。** Ch.5 纠正措施、Ch.6 验证、Ch.7 再分析、Ch.9 记录、App.2／3 在本册均 `(coming soon)`；要补这些必须读 CAP-38（2020-02 Supplemental Draft Guidance），不得用 SECG 或别家模板代替。

**与本包其他卡的接口：**

| 接口 | 方向 |
|---|---|
| CAP-32 `intentional-adulteration-defense` | **上游法条**；本卡所有方法最终服务于〔§ 121.130〕〔§ 121.135〕〔§ 121.140〕，冲突以法条为准 |
| CAP-36 `intentional-adulteration-secg` | 2017-08 **最终指南**问答层；本卡是草案方法层，效力低于它，两者不互引页码 |
| CAP-38 `intentional-adulteration-draft-2020` | **同 docket 下册**；补齐 Ch.5/6/7/9 与 App.2/3，两册合起来才是完整 IA 指南草案 |
| CAP-06（食品欺诈 EMA） | 牟利性掺杂无「大规模公共卫生伤害意图」，不进本卡 |
| CAP-16 `inspection-readiness` | 检查员取证程序不创设企业义务；本卡不写检查问卷 |

## A1 — 判定场景

| 场景 | 回答要点 |
|---|---|
| 评估方法选哪种 | KATs（快）/ 三要素（深）/ Hybrid（先快后深）三选一；FDA 不指定，也不要求都用 |
| 用 KATs 还用不用逐点打分 | 不必——三要素已内含于 KATs；除非该点落入 KAT 但有固有特征需进一步判断，才走 Hybrid |
| 四类 KAT 具体是哪四类 | 散装液体收发货、液体储存与处理、次级配料处理、混合及类似活动 |
| 密封桶/罐装的液体也算散装收发货吗 | 不算——密封 jug/drum/jar/tote 排除，无论总量多大 |
| 已开封并接泵计量的 drum 算什么 | 落入「液体储存与处理」KAT；与「次级配料处理」的开口容器情形分开判 |
| 返工品投料算不算次级配料处理 | 落入该 KAT；staging／preparation／addition／rework 四种形态都要看 |
| 带桨叶的烘烤机不是专门混合设备，算混合吗 | 可能算——混合是过程结果，不要求设备专为均匀混合设计 |
| 工艺一个 KAT 都不落入 | 判为非 APStep、无需策略，但仍要在 FDP 书面记录「无 KAT 适用」并按〔§ 121.157〕再分析 |
| 某点三要素分别 10/10/1 | 非 APStep——任一要素 = 1 即一票否决，不算总分 |
| 三要素加起来 20 分 | 灰区（14–25），须逐案写明各要素贡献与脆弱性性质，不能只写「低于 26」 |
| 三要素加起来 27 分 | FDA 预期存在显著脆弱性；仍须写逐点解释，不是自动成立 |
| 分数能直接抄到别家工厂吗 | 不能——APStep 随设施和工艺而变；分值本身也只是 FDA 可选工具 |
| 内部人员要不要单独列一栏 | 每个要素都要考虑 insider 可能性；漏评会整体压低分数 |
| 全厂装了围栏和门禁，算不算缓解策略 | 默认不算——全厂安保不需要 VA；只有针对某 APStep 的显著脆弱性时才升级为策略 |
| 依赖老员工的经验把关，评估时能加分吗 | 不能——这是既有措施不是固有特征，VA 阶段不纳入；若依赖它降低脆弱性，须在策略阶段识别并配管理组件 |
| 储罐口加了锁，还能从 APStep 名单删掉吗 | 不能——上了锁仍是 APStep，策略只是降低脆弱性 |
| 策略说明要写多长 | FDA 预期「相对简短直接」，一句话说清如何充分最小化/预防即可；允许缩写和脚注 |
| 监控多久查一次 | 自定「足以保证持续执行」的频次；FDA 示例（48 小时清洗周期两端各查、每周至少一次）不是强制值 |
| 能用例外记录只记异常吗 | 自动化持续监控/人员持续看守可以；静态锁具等须肯定记录 |
| 食品安全检查记录能不能当监控记录 | 可以合并（Scenario 3 的清洗后目视检查改为投料前并留签核），但须在 FDP 中说明 |
| 谁要做 qualified individual | 执行 Subpart C 活动者、APStep 岗位人员及其主管；编制计划/评估/识别策略/再分析者另需标准化课程等效或工作经验等效 |
| 要不要全员做意识培训 | 规则只强制 APStep 岗位人员及其主管；FDA 鼓励全员但不强制 |
| 每年固定复训一次吗 | 规则无再培训频率；上岗前完成，职责变化/表现不正确时按需复训 |

## A2 — 未来触发

- 问「谁做过 VA、用了什么方法」→ 本卡给三条可选路径；具体方法（CARVER + Shock、Plan Builder）标「转引未收」。
- 问「KATs 到底几类、FDMSD 几类」→ 本卡四类 KATs；FDMSD 七大类归 CAP-38 App.2，两者不可混答。
- 问「分数阈值是不是法规定的」→ 明确不是；阈值出自草案表格，法规只有三要素 + 内部人员。
- 问「纠正措施/验证/再分析/记录怎么做」→ 本册 `(coming soon)`，转 CAP-38。
- 问「FDA 认可的标准化课程有哪些、哪里报名」→ 本卡只说「equivalent to a standardized curriculum recognized by FDA」，课程目录标「转引未收」。
- 问「现场检查会怎么判我们的评分」→ 检查员侧转 CAP-16；本卡不给检查结论。
- 问「这份指南现在生效了吗」→ 它是 2019-03 草案（Draft—Not for Implementation），不是生效文件；现行义务回 CAP-32 法条与官方公告。
- 问「经济利益驱动的掺假按本卡评吗」→ 不属 food defense；走 CAP-06。

## 硬数字速查

| 数字 | 含义 | 出处 | 陷阱 |
|---|---|---|---|
| **4 类** | KATs 数量：bulk liquid receiving and loading / liquid storage and handling / secondary ingredient handling / mixing and similar activities | Revised Draft Guidance III.B / Ch.2.D | 不是七类；FDMSD 七大类归 CAP-38 |
| **over 50** | FDA 推导 KATs 所分析的 VA 次数 | Ch.2.D | 经验来源，不是法定样本量 |
| **3 要素** | 公共卫生影响 / 物理可及度 / 成功污染能力 | Ch.2.F，〔§ 121.130(a)〕 | 三要素是法定，评分表不是 |
| **1 / 3 / 5 / 8 / 10** | 三张评分表的共同五档尺度 | Ch.2.F.2，表 1/2/3 | FDA 可选工具；法规无分值 |
| **任一 = 1** | 一票否决该点，不再算总分 | Ch.2.G.1 | 高总分不能救回 |
| **≥ 26 / ≤ 13** | FDA 预期「存在 / 不存在显著脆弱性」的 sum 分界 | Ch.2.G.1 | 不是法规阈值 |
| **14–25** | 灰区，须逐案结合要素性质判断 | Ch.2.G.1 | 解释最详细的区间，不能一句带过 |
| **top 20–25%** | 高分组经验占比 | Ch.2.G.1 | 观察值，步骤少时不适用 |
| **40 mg/serving / 85 kg / 50% mortality** | representative contaminant 的估算参数 | Ch.2.F.2 Element 1 | FDA 提供值，可自行研究替换；非法规 |
| **120 days** | 草案评议期 | 封面 | 草案特有，不是合规期限 |
| **500 FTE / < $10,000,000** | small / very small business 定义 | IV.A，〔§ 121.3〕 | 法规定义，与评分体系无关 |
| **2 年** | 极小企业豁免证明材料保存 | IV.A，〔§ 121.5(a)〕 | 不是记录通用保存期的同一对象 |
| **4 问** | 监控程序 what / how / frequency / who | Ch.4.A | 写进 FDP 的骨架 |
| **无强制复训周期** | 规则不规定再培训频率 | Ch.8.E | 不等于不用复训 |

## E — 执行要点

**Step 1 — 先确认效力层再动笔。** 凡「必须/不得」回 CAP-32〔§ 121.xxx〕；本卡的方法、分数、场景全部标 `Revised Draft Guidance 章.节 [pdf-page N]` 并注明是未定稿草案；冲突时法条 > CAP-36 最终指南 > 本卡。

**Step 2 — 过豁免闸门再谈方法。** 先判〔§ 121.5〕豁免；液体储罐储存不豁免，且正好是 KATs 第一类，不要把豁免与方法混为一谈。

**Step 3 — 三选一确定评估路径。** KATs 快筛 / 三要素深评 / Hybrid。用 KATs 不另打三要素分；Hybrid 只对落入 KAT 且需进一步判断的步骤深挖。

**Step 4 — 按四类 KAT 逐点归类。** 散装液体收发货、液体储存与处理、次级配料处理、混合及类似活动；落入多类要把每一类都写进解释，便于日后 reanalysis。

**Step 5 — 打分时先查内部人员与固有特征。** 每要素都考虑 insider；固有特征参与评分，既有措施不参与；任一要素 = 1 即判非 APStep。

**Step 6 — 灰区逐案解释。** ≥26 / ≤13 可用简式，14–25 必须逐要素说明性质与贡献；所有点（含非 APStep）都要双向书面解释〔§ 121.130(c)〕。

**Step 7 — 策略按两条路径设计并配解释。** 降低可及性 / 降低污染机会；全厂安保默认不算策略；依赖既有措施就把它升为策略并配管理组件；每条策略写「如何充分最小化/预防」。

**Step 8 — 监控程序写四问。** what/how/frequency/who 齐备，频次自定但说明足以保证持续执行；同步记录；例外记录只用于适合的策略类型。

**Step 9 — 培训按职责分档。** Subpart C 执行人、APStep 岗位人员及主管、四项特定活动责任人分别匹配 qualified individual / 意识培训 / 标准化课程等效或工作经验等效；记录日期、类型、受训人。

**Step 10 — 收尾声明。** 本册未覆盖纠正/验证/再分析/记录（→ CAP-38）；CARVER + Shock、Plan Builder、专项 CP、EMA 一律「转引未收」。全包现为**三十类来源不可混引**、十二套法规编号；本卡不新增编号，只新增 FDA 指南第 8 类（草案子类第 1 份）。

## B — 边界

**B1 — 草案不是最终指南，更不是法条。** 封面明写 `Draft—Not for Implementation` 与 `when finalized, will represent the current thinking`；本卡所有方法都是征求意见中的建议，不得当 FDA 现行定论，不得据此断言「合规」或「不合规」。法定义务只回 CAP-32。

**B2 — 文件名年份错位。** 源文件名 `2016-436 IA Guidance Part 1 061418.pdf` 与研究目录名 `ia-2018-part1` 都不是封面日期；以 March 2019 / Revised Draft Guidance 为准。不得据文件名把它写成 2016 或 2018 版指南。

**B3 — KATs 四类是封闭枚举。** `The four KATs` 出自本件 glossary；不得把 FDMSD 的七大类（CAP-38 App.2）或 FSMA 七部基础规则搬来当 KATs。

**B4 — 分数与阈值不是法规。** 1/3/5/8/10、≥26、≤13、14–25、top 20–25%、示例中的 mg/kg 参数全部出自草案表格与 FDA 示例；〔§ 121.130〕只给三要素和内部人员，没有任何数字阈值。写成「FDA 规定 26 分以上算显著脆弱性」是实质错误。

**B5 — 方法三选一，不叠加。** KATs 已内含三要素；用 KATs 再逐点打分是重复劳动。只有 Hybrid 才对部分步骤深挖，且 Hybrid **可能比纯 KAT 识别出更少的 APStep**。

**B6 — 固有特征与既有措施不可倒置。** 固有特征参与 VA 评分；既有措施（质量/工安动机的资深员工定点、特殊工服、铅封等）在 VA 阶段不纳入，留到策略阶段评估。依赖其降低脆弱性就须识别为策略并配齐管理组件。

**B7 — 全厂安保 ≠ 缓解策略。** 围栏、外门上锁、全厂 ID 徽章不需要 VA、规则也不要求；仅当专门针对某 APStep 的显著脆弱性时才成为策略，管理组件也只在该点配置。

**B8 — 上锁不改变 APStep 身份。** 被缓解后的步骤仍是 actionable process step；「无 KAT」结论也须书面留痕并按〔§ 121.157〕再分析。

**B9 — 本册是未完成的第二分册。** Ch.5／6／7／9 与 App.2／3 标 `(coming soon)`；纠正措施、验证、再分析、记录与业务规模计算一律转 CAP-38，不得从本册的只言片语反推。

**B10 — 不可逐字引用区。** 全部评分表（表 1/2/3）、工作表 1-C～1-F、场景表 3-1～3-4、监控记录表 4-5～4-8、Figure 2a-1／2b／2c 系列流程图均为多栏错行或纯图形；只可转述结构与数值对应关系。页眉页脚不是正文引文。

**B11 — 培训不是全员强制，也没有固定复训周期。** 意识培训只强制 APStep 岗位人员及其主管；四项特定活动责任人需标准化课程等效或工作经验等效；qualified individual 可以是外部人员；规则不设具体再培训频率。

**B12 — 引用规范（全包统一，三十类不可混引）。** 法规正文仍为十二套编号〔§ 1 / 101 / 108 / 113 / 114 / 117 / 120 / 121 / 123 / 172.xxx〕+〔§ 1.13xx/1.14xx〕+〔§ 1.9xx〕；FDA 最终指南为 should 建议层（CAP-36 第 7 类），**本件为草案建议层（第 8 类，最低）**，CPGM／CP／IOM 为检查员视角、不创设企业义务。**Part 1 三套 subpart（L / O / S）引用必须带 subpart 归属**，不得只说「part 1」。

*本卡落地于 v4.24；全包现为三十类不可混引，共 38 张能力卡（另 20 张子卡）。*
