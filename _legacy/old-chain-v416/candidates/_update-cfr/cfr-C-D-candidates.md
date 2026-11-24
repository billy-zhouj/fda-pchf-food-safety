# CFR Subpart C+D 增量候选（来源标注 chunk id）

读取范围：cfr-chunks.md 第 1725–2617 行（Subpart C 全部 + Subpart D 全部）。
核对卡：hazard-analysis-method / management-components / process-control-validation / recall-plan / supply-chain-verification / regulatory-boundaries（另抽查 allergen-program、environmental-pathogen-sanitation、chemical-hazard-controls、reference-tools-discipline）。

---

## 一、新知识候选（指南没有或法规措辞构成法定例外/门槛）

### nC-D-01 危害分析的法定证据来源与"无论结论都要书面"义务
- 条文出处: § 117.130(a)(1)(2)；chunk: ck-cfdeac63f142
- 原文关键句: "You must conduct a hazard analysis to identify and evaluate, based on experience, illness data, scientific reports, and other information… The hazard analysis must be written regardless of its outcome."
- 中文大意：危害分析必须基于"经验、疾病数据、科学报告及其他信息"作出；且无论分析结果如何都必须书面成文。
- 类型: rule
- 建议归属: hazard-analysis-method
- 为什么是指南缺口: 指南泛称"历史暴发、科学数据"，法规把四类信息源写成法定基准（illness data 是明示类别，指南未单列）；"regardless of its outcome" 是 must 级措辞，指南 Step 4 只说"全部为 No 时 FSP 可只含书面危害分析"，未把"零危害也必须书面"上升为法定义务。

### nC-D-02 概率评估的法定参照系："无预防控制时"
- 条文出处: § 117.130(c)(1)(i)；chunk: ck-cfdeac63f142
- 原文关键句: "…assess the severity of the illness or injury if the hazard were to occur and the probability that the hazard will occur in the absence of preventive controls."
- 中文大意：评估概率必须在"假设不存在任何预防控制"的反事实条件下进行，而不是在当前有措施运行的条件下。
- 类型: rule
- 建议归属: hazard-analysis-method
- 为什么是指南缺口: 指南卡 Step 3 写"严重性（致病/致伤程度）× 概率（历史暴发、配方、工艺、设施、消费者）"，未点明概率的条件概率框架"in the absence of preventive controls"——这是决定"现有 CGMP 算不算控制"的方法学分水岭，法规措辞直接锁定"不得用现有措施压低概率再判 No"。

### nC-D-03 十因素清单的法定收口：面向"预期消费者的成品安全"+ 时间性/气象性因素
- 条文出处: § 117.130(c)(2) chapeau 及 (c)(2)(x)；chunk: ck-cfdeac63f142
- 原文关键句: "The hazard evaluation must consider the effect of the following on the safety of the finished food for the intended consumer… (x) Any other relevant factors, such as the temporal (e.g., weather-related) nature of some hazards (e.g., levels of some natural toxins)."
- 中文大意：十因素的评估视角是"对预期消费者的成品安全性"；兜底因素明确举例——某些危害具有时间性（如天气相关），例：某些天然毒素的水平随季节变化。
- 类型: fact / threshold
- 建议归属: hazard-analysis-method
- 为什么是指南缺口: 指南转述十类因素时第 (x) 类只写"其他"，丢掉了法规自带的"temporal/weather-related + 天然毒素"实例（这正是 DON、组胺、贝类毒素季节性评估的法定锚点）；"for the intended consumer" 的评估视角限定也是法规独有措辞。

### nC-D-04 CCP 是可选而非强制："if there are any CCPs"
- 条文出处: § 117.135(a)(2)；chunk: ck-81c43a31140b
- 原文关键句: "Preventive controls required by paragraph (a)(1)… include: (i) Controls at critical control points (CCPs), if there are any CCPs; and (ii) Controls, other than those at CCPs, that are also appropriate for food safety."
- 中文大意：预防控制包括 CCP 处的控制——但仅"若存在 CCP"；没有 CCP 完全不违法，非 CCP 控制同样合格。
- 类型: legal-exception
- 建议归属: hazard-analysis-method（或 management-components）
- 为什么是指南缺口: 指南讲 HACCP 升级到 FSP 时的 CCP 映射，但未把"法规不强制设 CCP"写成明确结论；存量 HACCP 企业常误以为必须保留 CCP 概念，此条是法定的"可以没有"。

### nC-D-05 不实施预防控制的法定情形是五类而非四类：(a)(5) 自主分销链控制体系
- 条文出处: § 117.136(a)(1)–(5)、(b)；chunk: ck-597db08ced38、ck-4a84da3f5f9c
- 原文关键句: "(5) You have established, documented, and implemented a system that ensures control, at a subsequent distribution step, of the hazards in the food you distribute and you document the implementation of that system."
- 中文大意：第五种情形不依赖客户书面保证——企业自行建立、文件化并运行一套"确保在后续分销环节控制危害"的体系即可豁免实施 PC，但体系及其运行都要留记录。(a)(2)–(4) 三条客户依赖通道共用法定披露措辞 "not processed to control [identified hazard]" + 每年取得书面保证；(a)(4) 还要求客户的下游传递保证链（cascade）。
- 类型: rule / legal-exception
- 建议归属: supply-chain-verification、regulatory-boundaries
- 为什么是指南缺口: 指南蒸馏的"合法 No 三通道"（极强致死/CGMP 覆盖/消费前制备）与 117.136 不是同一层（见矛盾 cC-D-01）；法规的 (a)(5) 自主体系通道指南几乎未讲，(a)(4) 的链式保证传递（客户须书面承诺继续披露+约束其买方）在指南中无对应细节。另注：任务背景说"四种情形"，法规原文实为 (a)(1)–(a)(5) 五种。

### nC-D-06 出具保证书一方的对向义务：照做并记录
- 条文出处: § 117.137；chunk: ck-43570a81de36
- 原文关键句: "A facility that provides a written assurance under § 117.136(a)(2), (3), or (4) must act consistently with the assurance and document its actions taken to satisfy the written assurance."
- 中文大意：给别人出具 117.136 书面保证的设施，自身必须行为与保证一致，并记录为履行保证采取的行动。
- 类型: rule
- 建议归属: supply-chain-verification
- 为什么是指南缺口: 指南全部站在"收货方索取保证"视角；117.137 是给"上游出具保证的卖方"独立设定义务的对向条款——用户企业作为客户供应链上游被索要保证时的义务来源，指南完全空白。

### nC-D-07 管理组件映射的法定不对称：供应链程序只有三件、召回计划整体豁免
- 条文出处: § 117.140(a)(b)(c)；chunk: ck-40000ec5bd3c
- 原文关键句: "(b) The supply-chain program… is subject to… (1) Corrective actions… (2) Review of records in accordance with § 117.165(a)(4); and (3) Reanalysis… (c) The recall plan established in § 117.139 is not subject to the requirements of paragraph (a)."
- 中文大意：供应链程序只挂纠正措施、记录审查、再分析三件（无监控、无验证确认）；召回计划则整体不受监控/纠正/验证三类管理组件约束。
- 类型: legal-exception
- 建议归属: management-components
- 为什么是指南缺口: 指南只说这四类控制免 validation，并警告"豁免不等于豁免管理组件"；法规实际规定召回计划连监控/纠正/验证都豁免（117.140(c)），供应链程序也仅三件——指南把"减配"说成"不减"，方向性偏差。

### nC-D-08 correction 的两条法定通道：过敏原/卫生"条件与实践"通道不带"孤立"限定
- 条文出处: § 117.150(c)(1)(2)；chunk: ck-25e4d2767a47
- 原文关键句: "You do not need to comply with… (a) and (b)… if: (1) You take action, in a timely manner, to identify and correct conditions and practices that are not consistent with the food allergen controls in § 117.135(c)(2)(i) or the sanitation controls in § 117.135(c)(3)(i) or (ii); or (2) You take action, in a timely manner, to identify and correct a minor and isolated problem that does not directly impact product safety."
- 中文大意：走 correction 而免完整纠正措施有两条独立通道：(1) 及时纠正与过敏原控制（仅 (c)(2)(i) 防交叉接触部分）或卫生控制不一致的条件和实践——不要求"孤立"；(2) 及时纠正不影响产品安全的轻微且孤立问题。
- 类型: rule / legal-exception
- 建议归属: management-components
- 为什么是指南缺口: 指南把 correction 判定合并成"未影响食品 AND 孤立"一个二维规则；法规拆成两条并列通道，且通道 (1) 无"minor and isolated"限定——同一清洁偏差按指南要升级 CA，按法规 (c)(1) 及时纠正即可。另注意 (c)(1) 引用的是 117.135(c)(2)(i)（交叉接触），不含 (ii) 标签控制——贴错标签走不了这条捷径，指南未区分。

### nC-D-09 validation 时段的法定弹性窗：投产前，或投产后 90 个日历日内，或 PCQI 书面论证更长
- 条文出处: § 117.160(b)(1)(i)(A)(B)、(b)(2)；chunk: ck-88cf79796874
- 原文关键句: "(A) Prior to implementation of the food safety plan; or (B)… (1) Within 90 calendar days after production of the applicable food first begins; or (2) Within a reasonable timeframe, provided that the [PCQI] prepares… a written justification for a timeframe that exceeds 90 calendar days…"
- 中文大意：validation 由 PCQI 执行或监督，须在 FSP 实施前完成；或（为证控制措施可按设计实施）在首批投产后 90 个日历日内；超过 90 天须 PCQI 书面论证。另 (b)(2)：以获取并评估科学技术证据为主，证据不可得或不充分时才自行开展研究。
- 类型: threshold / rule
- 建议归属: management-components、process-control-validation
- 为什么是指南缺口: 指南只说"validation 一次性/变更时做"，完全没有 90 日历日窗口和"书面论证可超 90 天"的法定时限；(b)(2) 的"文献证据优先、自做研究是证据缺位时的补充"的法定顺序也是指南未明文的成本规则。

### nC-D-10 validation 豁免第五通道：PCQI 书面论证"validation 不适用"
- 条文出处: § 117.160(c)(1)–(5)；chunk: ck-88cf79796874
- 原文关键句: "(5) Other preventive controls, if the preventive controls qualified individual prepares… a written justification that validation is not applicable based on factors such as the nature of the hazard, and the nature of the preventive control and its role in the facility's food safety system."
- 中文大意：除过敏原、卫生、召回、供应链四类法定豁免外，任何其他预防控制都可经 PCQI 书面论证豁免 validation，论证因素为"危害性质+控制性质及其在体系中的角色"。
- 类型: legal-exception
- 建议归属: management-components
- 为什么是指南缺口: 指南明确写"法定豁免四类"，漏掉 (c)(5) 这条开放式第五通道——它是 process-control-validation 卡"裁剪须书面论证"直觉的法定出处，豁免数量口径需从"四"改为"四+一兜底"。

### nC-D-11 产品检测与环境监测书面程序的法定七要素清单
- 条文出处: § 117.165(b)(2)、(b)(3)；chunk: ck-5f371fce170b
- 原文关键句: "Procedures for product testing must: (i) Be scientifically valid; (ii) Identify the test microorganism(s) or other analyte(s); (iii) Specify the procedures for identifying samples, including their relationship to specific lots…; (iv) Include the procedures for sampling, including the number of samples and the sampling frequency; (v) Identify the test(s) conducted…; (vi) Identify the laboratory…; (vii) Include the corrective action procedures required by § 117.150(a)(1)."
- 中文大意：产品检测程序法定七要素（科学有效/目标菌或分析物/样品与批次对应/抽样数与频次/方法与检测实验室/含 117.150(a)(1) 纠正程序）；环境监测程序结构相同，另强制"采样点位数量与位置、取样时机与频次必须足以判定预防控制有效"。
- 类型: rule
- 建议归属: management-components（或 environmental-pathogen-sanitation）
- 为什么是指南缺口: 指南分散提及检测方案要素，从未给出"七要素均为 must"的完备清单；环境监测"点位与频次的充分性标准"（must be adequate to determine whether preventive controls are effective）是法规独有判准，指南用 should 级语言。

### nC-D-12 再分析的完成时限与"无修订结论也要书面"义务
- 条文出处: § 117.170(c)(d)；chunk: ck-fa4b17bf2670
- 原文关键句: "(c)… Before any change in activities… is operative; or (2)… Within 90 calendar days after production of the applicable food first begins… (d) You must revise the written food safety plan if a significant change… creates a reasonable potential for a new hazard… or document the basis for the conclusion that no revisions are needed."
- 中文大意：事件触发的再分析+新增控制的 validation 须在变更生效前完成，或（同 90 日逻辑）投产后 90 日历日内/PCQI 书面论证更长；再分析后要么修订 FSP，要么书面记录"无需修订"的结论依据。
- 类型: threshold / rule
- 建议归属: management-components
- 为什么是指南缺口: 指南讲"变更触发再分析"但无任何完成时限（90 日历日窗是法规新信息）；(d) 的"不改也要留结论记录"是指南"结论是状态机不是句号"直觉的法定版，指南未升格为 must。

### nC-D-13 FDA 指令型再分析：第五类触发器
- 条文出处: § 117.170(f)；chunk: ck-fa4b17bf2670
- 原文关键句: "You must conduct a reanalysis of the food safety plan when FDA determines it is necessary to respond to new hazards and developments in scientific understanding."
- 中文大意：FDA 认定因新危害或科学认知进展需要时，可责令再分析——企业自己的触发器清单之外多出一条监管方发起的强制通道。
- 类型: rule
- 建议归属: management-components、regulatory-boundaries
- 为什么是指南缺口: 指南的触发器清单为"3 年周期 + 变更/新信息/意外/无效"四类事件，完全没有 FDA 单方发起再分析（117.170(f)）这一类——监管互动场景下指南会漏列义务。

### nC-D-14 PCQI 八项法定专属职能清单（含两项"书面论证"职能）
- 条文出处: § 117.180(a)(1)–(8)、(c)(1)、(d)；chunk: ck-190d18736f5a
- 原文关键句: "One or more preventive controls qualified individuals must do or oversee the following: (1) Preparation of the food safety plan… (3) Written justification for validation… exceeds the first 90 calendar days… (4) Determination that validation is not required… (6) Written justification for review of records… exceeds 7 working days… (8) Determination that reanalysis can be completed… in a timeframe that exceeds the first 90 calendar days…"
- 中文大意：八项必须由 PCQI 执行或监督的职能封闭清单，其中包括三项"写书面论证/豁免认定"（超 90 天 validation、免 validation、超 7 工作日记录审查、超 90 天再分析完成）；PCQI 可为非雇员（标准化课程培训或同等工作经验）；培训记录须含日期、类型、受训人。
- 类型: rule / fact
- 建议归属: management-components（PCQI 职能）；training 记录部分→hazard-analysis-method Step 1
- 为什么是指南缺口: 指南散落式提到 PCQI 判安全、审记录；法规给出封闭的八项清单——尤其"书面论证本身也是 PCQI 专属职能"（企业不能把放宽时限的论证委托给 QA 经理签字）指南未讲；"not required to be an employee"给外部 PCQI 模式以法定明文。

### nC-D-15 qualified facility 的替代义务实质：双轨保证书 + 通胀基线 2011
- 条文出处: § 117.201(a)；chunk: ck-a151bd77492a
- 原文关键句: "…(2)(i) An attestation that you have identified the potential hazards…, are implementing preventive controls…, and are monitoring the performance…; or (ii) An attestation that the facility is in compliance with State, local, county, tribal, or other applicable non-Federal food safety law…"
- 中文大意：合格设施须向 FDA 提交两份保证书：身份保证（含"以 2011 年为通胀调整基线年"判定资格）+ 二选一的业务保证：(i) 已识别危害、已实施 PC、在监控其性能；或 (ii) 符合州/地方/部落/外国等非联邦食品安全法（可凭执照、检查报告、证书等）。邮寄用 Form FDA 3942a。
- 类型: fact / rule
- 建议归属: regulatory-boundaries
- 为什么是指南缺口: 指南只把 qualified facility 当"豁免身份"一句带过；法规实际是"保证书替代 FSP"的替代合规体系——(a)(2)(i) 意味着即便豁免也要真的识别危害+实施 PC+监控（只是不写全套 FSP），"豁免"实为"减配"，指南的"义务换成简化要求"表述可被此条精确锚定。

### nC-D-16 合格设施合规日历与身份翻转的过渡期
- 条文出处: § 117.201(c)(d)；chunk: ck-a151bd77492a、ck-13645e4ad4e6
- 原文关键句: "(1) A facility must determine and document its status as a qualified facility on an annual basis no later than July 1…; (2)(ii) Beginning in 2020, submitted… every 2 years during the period beginning on October 1 and ending on December 31… (d)… must comply with subparts C and G… no later than December 31 of the applicable calendar year unless otherwise agreed to by FDA and the facility."
- 中文大意：每年 7 月 1 日前完成并记录资格判定；保证书自 2020 年起每 2 年在 10 月 1 日–12 月 31 日窗口提交；丧失资格须 7 月 31 日前用 Form 3942a 通知 FDA，并于当年 12 月 31 日前满足 Subpart C+G——除非 FDA 与设施另行商定。
- 类型: threshold / rule
- 建议归属: regulatory-boundaries
- 为什么是指南缺口: 指南无任何合格设施时限；此条给出全年四个法定节点+"unless otherwise agreed to by FDA" 这一罕见的双边宽免通道（宽限期可谈，指南不知道可谈）。

### nC-D-17 走"非联邦法合规"轨道的合格设施须向消费者披露厂名厂址
- 条文出处: § 117.201(e)；chunk: ck-13645e4ad4e6
- 原文关键句: "A qualified facility that does not submit attestations under paragraph (a)(2)(i) of this section must provide notification to consumers as to the name and complete business address of the facility where the food was manufactured or processed…"
- 中文大意：未提交 (a)(2)(i) 保证书（即选 (ii) 非联邦法轨道）的合格设施，必须在标签显著处（有标签时）或购买点标签/海报/标牌/随附文件/网络销售的电子通知中，向消费者披露制造/加工设施名称与完整地址。
- 类型: rule
- 建议归属: regulatory-boundaries
- 为什么是指南缺口: 指南完全没讲这条"豁免的隐性对价"——选择非联邦法轨道=换取标签/购买点披露义务，是豁免判定 Step 3 的必填分支。

### nC-D-18 纯贮存设施（未拆封包装食品）的裁剪义务包
- 条文出处: § 117.206；chunk: ck-36885ae60c52
- 原文关键句: "…stores any such refrigerated packaged food that requires time/temperature control… the facility must conduct… (1) Establish and implement temperature controls…; (2) Monitor…; (3)… take appropriate corrective actions…; (4) Verify… Calibrating… Reviewing records of monitoring and corrective actions… within 7 working days…"
- 中文大意：仅从事贮存未拆封包装食品的设施不做全套 FSP；但若贮存需时间/温度控制（防病原增殖/产毒）的冷藏包装食品，须做五项：温度控制、监控、失控纠正措施、验证（校准时钟+记录审查沿用 7 工作日+PCQI 书面论证规则）、记录（肯定记录或例外记录均可）。
- 类型: legal-exception / rule
- 建议归属: regulatory-boundaries（贮存条款）；其记录审查机制引用 management-components
- 为什么是指南缺口: 指南以加工/制造设施为叙述主体，纯仓储的替代要求整章空白；冷藏库客户问"要不要做 FSP"时，现有卡只能答"看豁免"，此条给出法定裁剪清单。

### nC-D-19 FSP 法定七部件封闭清单 + FSP 本身即 Subpart F 记录
- 条文出处: § 117.126(a)(2)(b)(1)–(7)(c)；chunk: ck-33f07aee6243
- 原文关键句: "The written food safety plan must include: (1) The written hazard analysis…; (2) The written preventive controls…; (3) The written supply-chain program…; (4) The written recall plan…; (5)… monitoring…; (6)… corrective action procedures…; (7)… verification procedures… The food safety plan… is a record that is subject to the requirements of subpart F."
- 中文大意：FSP 必须包含且由 PCQI 编制/监督编制的书面件共七项（危害分析、预防控制、供应链程序、召回计划、监控程序、纠正程序、验证程序）；FSP 整体按 Subpart F 记录规则管理。
- 类型: fact / rule
- 建议归属: hazard-analysis-method（FSP 结构层）
- 为什么是指南缺口: 指南从不给出"七部件"法定清单（且注意：验证程序引用的是 117.165(b) 的书面程序而非 validation 报告；确认/validation 结果不在此清单，走记录体系）；"FSP 即记录"决定其保存/可及义务，指南未升格明示。

---

## 二、近重复（指南已覆盖，法规条款号可作权威出处强化）

- rC-D-01: 召回计划四动作（直接通知收货人含退回/处置方式、适时通知公众危害、有效性核查、妥善处置——再加工/重工/转安全用途/销毁）+ 每步指派责任人 ↔ 现有卡 recall-plan（E 段 Step 1/4 全覆盖；可补条款号 § 117.139(a)(b)(1)–(4)，并把适用前提"仅限有需预防控制危害的食品"补精确，§ 117.139 chapeau；chunk: ck-4bbff62701f1）
- rC-D-02: RTE 食品包装前暴露于环境且包装后无致死处理/配方抑制 → 必须评估环境病原 ↔ 现有卡 hazard-analysis-method Step 3"强制触发器"、environmental-pathogen-sanitation（两卡均已引 117.130(c)(1)(ii)；chunk: ck-cfdeac63f142，法规措辞含"otherwise include a control measure (such as a formulation lethal to the pathogen)"可补全触发器的第二个排除条件）
- rC-D-03: 验证活动五类封闭清单（validation、监控执行情况核查、纠正决定适当性核查、实施与有效性验证、再分析）↔ 现有卡 management-components Step 4（卡已写"五类法定验证活动（117.155）是封闭清单"，出处直接坐实 § 117.155(a)(1)–(5)；chunk: ck-837069edce76）
- rC-D-04: 监控与纠正记录须在记录产生后 7 个**工作日**内审查（或由 PCQI 监督），超期须 PCQI 书面论证；校准/检测/供应链验证记录"合理时间内"审查 ↔ 现有卡 management-components Step 4/5（卡写"7 天"，应精确为"7 working days"；"合理时间"双轨是法规明文；chunk: ck-5f371fce170b § 117.165(a)(4)(i)(ii)）
- rC-D-05: 例外记录合法性：需时间/温度控制食品的冷藏温度监控记录可为"肯定记录或例外记录"，且例外记录在其他情形"may be adequate" ↔ 现有卡 management-components Step 5 记录减负（法规明文给出冷藏 TCS 这一典型场景+一般性许可句，§ 117.145(c)(2)(i)(ii)；chunk: ck-74f833261f39）
- rC-D-06: 危害识别三分类法定枚举：生物（含寄生虫、环境病原）、化学（含放射学危害、农兽药残、天然毒素、**腐败分解**、未批食用/色素添加剂、过敏原）、物理（石块/玻璃/金属）+ 来源三渠道（天然存在/无意引入/为经济利益故意引入）↔ 现有卡 hazard-analysis-method Step 2、chemical-hazard-controls（经济掺假；"腐败/分解 decomposition"作为法定化学危害值得补进卡的分类枚举——指南卡把它归质量缺陷的表述需与本条并读，§ 117.130(b)；chunk: ck-cfdeac63f142）
- rC-D-07: 工艺控制必须含"危害控制相关参数"+"须控制的生物/化学/物理参数的最大值/最小值或其组合" ↔ 现有卡 process-control-validation Step 4 关键限值（法定"max/min value or combination of values"即关键限值的法规定义，§ 117.135(c)(1)(i)(ii)；chunk: ck-81c43a31140b）
- rC-D-08: corrective action 四步（识别并纠正、降低复发可能、评估全部受影响食品、不能保证不变质/不错标则阻止入市）+ 未预期食品安全问题三情形（PC 失当且无预案/控制或 FSP 整体无效/记录审查发现记录不完备、活动未按 FSP 执行或纠正决定不当）↔ 现有卡 management-components Step 3（卡的四步与三角色分工完全对应 § 117.150(a)(2)(i)–(iv)、(b)(1)(i)–(iii)、(b)(2)；chunk: ck-25e4d2767a47；"阻止入市"的法定条件是"cannot ensure not adulterated or misbranded"，卡表述可加条款号）
- rC-D-09: 再分析双轨：整体至少每 3 年一次 + 四类事件触发（重大变更/新危害信息/117.150(b) 意外问题/控制无效），事件触发可限于"适用部分" ↔ 现有卡 management-components Step 6、hazard-analysis-method Step 6（核对结论：法规原文 117.170(a) 确为 "as a whole at least once every 3 years"，3 年时钟只约束"整体"再分析，事件触发允许局部——与卡一致，补条款号 § 117.170(a)(b)(1)–(4)；chunk: ck-fa4b17bf2670）
- rC-D-10: "其他控制"法定示例=卫生培训及其他 CGMP——CGMP 措施可升格为预防控制 ↔ 现有卡 management-components Step 6 升格最小操作（法规明文背书，§ 117.135(c)(6)；chunk: ck-81c43a31140b）
- rC-D-11: 环境监测的适用前提（RTE 食品受环境病原污染属需预防控制的危害时才强制采样检测）+ 训练记录三要素（日期、类型、受训人）↔ 现有卡 environmental-pathogen-sanitation（条件句式坐实"不触发则可不做"，§ 117.165(a)(3)、§ 117.180(d)；chunk: ck-5f371fce170b、ck-190d18736f5a）

---

## 三、潜在矛盾（指南建议 vs 法规要求不一致）

- **cC-D-01｜"合法 No 三通道"与 117.136 是两层不同的事，卡有混层风险**。hazard-analysis-method Step 4 把"①极强致死工艺②CGMP/前提程序已覆盖③消费前制备消除"称为"合法 No 的三条通道"。法规中：117.136 的适用前提是"你已识别出**需预防控制的危害**"（"when you identify a hazard requiring a preventive control (identified hazard)"），其五情形是"不实施 PC"的出口，其中并无"CGMP 已覆盖"通道；(a)(1)"could not be consumed without application of an appropriate control"的法定示例是 RAC（可可豆、咖啡豆、谷物）——比指南"消费前制备消除危害"窄且条件不同；"极强致死"通道在 117.136 中找不到对应条文（它实为 117.130(c) 评估阶段"不构成需 PC 危害"的结论，或援引 (a)(1) 需个案论证）。建议卡把"判 No（无需 PC 的危害）"与"判 Yes 但不实施 PC（117.136 五情形+117.136(b) 记录）"拆成两节。出处：hazard-analysis-method E/Step 4 vs § 117.136(a)(1)–(5)（ck-597db08ced38）。
- **cC-D-02｜"豁免不等于豁免管理组件"对召回计划不成立**。management-components Step 4 写四类免 validation 控制"豁免不等于豁免管理组件"；但 117.140(c) 明文"召回计划**不受 (a) 款（监控/纠正/验证）约束**"——召回计划是整体减配而非仅免 validation；供应链程序也只挂 (b) 款三件，无监控。指南的警示语方向正确但覆盖面错误，按法规应改写分级表述。出处：management-components Step 4 vs § 117.140(b)(c)（ck-40000ec5bd3c）。
- **cC-D-03｜"决定召回后立即通知 FDA 协调员"在 117.139 中无对应条文**。recall-plan Step 3 将其列为时序硬规则；本节法规原文（117.139 全文）只要求通知直接收货人与"适时通知公众"，无 FDA 通知义务——该义务出自 Subpart J（1.361 强制召回报告）等非本节条文/指南建议。卡应把出处从"117.139"降级标注为"跨 Subpart 义务"，避免以本节条文为据引用时举证失败。出处：recall-plan E/Step 3 vs § 117.139（ck-4bbff62701f1）。
- **cC-D-04｜任务背景所称"117.126(d) 签署"在本 chunk 中不存在**。ck-33f07aee6243 的 § 117.126 文本止于 (c) Records，无 (d) PCQI 签署/日期条款——要么分块时截断，要么该句在其他 chunk。签署义务**不应**据本节文本入库，待后续核对全文再补。

---

### 附：核对用户指定问题
- "3 年再分析"：法规原文在 **117.170(a)**（非 (b)）："as a whole at least once every 3 years"——3 年时钟仅约束整体再分析；事件触发（(b)(1)–(4)）允许针对"applicable portion"局部再分析。指南卡两处（hazard-analysis-method Step 6、management-components Step 6）与法规一致，无需改数，仅补条款号。
- "validation 豁免情形"：法定为 117.160(c)(1)–(4) 四类列举 + (c)(5) PCQI 书面论证兜底，指南"四类"口径缺兜底通道（见 nC-D-10）。
- "合法 No 三通道"：与法规层级不符（见 cC-D-01）；117.136 实为五情形。
- "117.155(b) 每年审查记录"：原文 117.155(b) 仅为"所有验证活动须记录"文档义务，**无"每年审查"语句**——记录审查时限规则在 117.165(a)(4)（7 工作日/合理时间双轨）；"每年"字样本节法规中只出现在 117.136(a)(2)(ii)(3)(ii)(4)(ii) 的"年度书面保证"与 Subpart G 审核（不在本节）。指南若有"年审记录"表述属转述失真，引用时改挂 117.165(a)(4)。
