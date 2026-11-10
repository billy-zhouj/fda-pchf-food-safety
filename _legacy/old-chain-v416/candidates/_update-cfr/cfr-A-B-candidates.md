# CFR Subpart A+B 增量候选（来源标注 chunk id）

扫描范围：cfr-chunks.md 第 1–1724 行（§117.1–§117.110）。对照现有 10 卡（重点：regulatory-boundaries / hazard-analysis-method / management-components / reference-tools-discipline）。

## 一、新知识候选（指南没有、法规独有的）

### nA-B-01 不合规不是"缺陷"而是法定 prohibited act——执法后果钩子
- 条文出处: § 117.1(a)(1), (b)；chunk: ck-31931dd3d7ec
- 原文关键句: "The operation of a facility ... if the owner, operator, or agent in charge ... is required to comply with, and is not in compliance with, section 418 ... or subpart C, D, E, F, or G of this part is a prohibited act under section 301(uu)." 中文大意：应遵守而未遵守 418 条/C-G 分部的运营本身构成 FD&C Act §301(uu) 禁止行为；CGMP 失守直接对应 §402(a)(3)/(4) 的 adulterated 认定（"unfit for food" / "insanitary conditions"）。
- 类型: rule
- 建议归属: regulatory-boundaries
- 为什么是指南缺口: 指南全篇讲"怎么做"，从不讲"不做的法律定性"。"CGMP 违规会导致什么后果"这类问题指南回答不了——禁制行为/ adulterated 双钩子是纯法条信息。

### nA-B-02 豁免身份体系的精确数字门槛（qualified facility 两段式测试）
- 条文出处: § 117.3 (qualified facility / qualified end-user / small business / very small business / full-time equivalent employee)；chunk: ck-d4321842b5a9, ck-5fafd7ac6a65, ck-5b32c149c7eb, ck-c163f4b37467
- 原文关键句: "the average annual monetary value of the food ... sold directly to qualified end-users ... exceeded the average annual monetary value of the food sold by such facility to all other purchasers; and ... was less than $500,000, adjusted for inflation"；qualified end-user 距离条件 "In the same State ... or ... Not more than 275 miles from such facility"；FTE = 总工时 ÷ 2,080、向下取整，small business <500 FTE，very small business 3 年年均 <$1,000,000（含无销售货物的市场价值）。门槛计算须合并计入所有 affiliates 与 subsidiaries 的销售额。中文大意：qualified facility 有两条独立通道——(1) very small business，或 (2) "直销 qualified end-users 占比过半 + 年均总销售额 <$50 万"两段式测试；end-user 有同州/275 英里地理约束。
- 类型: threshold
- 建议归属: regulatory-boundaries
- 为什么是指南缺口: 该卡 Step 3 只写"前 3 年年均销售额（食品销售<$50 万等门槛）"——漏掉了"直销占比须过半"这个第一要件、275 英里/同州距离、2,080 小时 FTE 算法、affiliate 合并计算。"我的销售额 60 万但全卖给散客算不算 qualified facility"这类具体判定指南给不出。

### nA-B-03 "环境病原"的法定外延：明确排除产芽孢病原菌
- 条文出处: § 117.3 (Environmental pathogen)；chunk: ck-74dc4628c862
- 原文关键句: "Examples of environmental pathogens for the purposes of this part include Listeria monocytogenes and Salmonella spp. but do not include the spores of pathogenic sporeforming bacteria." 中文大意：法规意义上的环境病原指能在环境中存活定殖、不经处理即食可致病的病原，列举李斯特菌与沙门氏菌，但把产芽孢致病菌的芽孢排除在外。
- 类型: fact
- 建议归属: environmental-pathogen-sanitation
- 为什么是指南缺口: 该卡讲了湿区防李斯特/干区防沙门的战略，但从未给出"环境病原"这个法定概念的边界——"肉毒梭菌芽孢、蜡样芽孢杆菌算不算触发 117.130(c)(3) 强制评估的环境病原"只能靠法条定义回答。

### nA-B-04 "significantly minimize" 的法定含义：降到可接受水平，含彻底消除
- 条文出处: § 117.3 (Significantly minimize)；chunk: ck-d4321842b5a9
- 原文关键句: "Significantly minimize means to reduce to an acceptable level, including to eliminate." 中文大意：显著最小化=降低到可接受水平（可以不是零），必要时才到消除——这是所有预防控制法定目标的统一标尺。
- 类型: fact
- 建议归属: hazard-analysis-method（PC 判定语言）兼 process-control-validation（削减目标设定）
- 为什么是指南缺口: 指南通篇使用该术语但未定义；"控制是否必须做到零检出/是否允许残留风险水平"这一常见问题，法定答案（可接受水平≠零，消除只是特例）只在 117.3。

### nA-B-05 预防控制的法定动态标准：与"分析当时"的科学认知一致
- 条文出处: § 117.3 (Preventive controls)；chunk: ck-5fafd7ac6a65
- 原文关键句: "...consistent with the current scientific understanding of safe food manufacturing, processing, packing, or holding at the time of the analysis." 中文大意：预防控制的适格性锚定在危害分析作出之时的科学认知水平——科学进展本身构成法定再评估理由，无需等其他触发事件。
- 类型: rule
- 建议归属: management-components（Step 6 动态维护）
- 为什么是指南缺口: 卡的再分析触发器是"变更/新信息/意外/失效"四类事件型；"科学认知演进导致原控制不再适格"这一法定时间锚点指南没展开——"科学文献更新但我的工艺没变，要重审吗"答不了。

### nA-B-06 PCQI 资格的双通道与 qualified auditor 的两类法定适格主体
- 条文出处: § 117.3 (Preventive controls qualified individual / Qualified auditor，交叉引用 § 117.180(c)(2))；chunk: ck-5fafd7ac6a65
- 原文关键句: "successfully completed training ... at least equivalent to that received under a standardized curriculum recognized as adequate by FDA or is otherwise qualified through job experience"；auditor 例子："A government employee, including a foreign government employee; and ... An audit agent of a certification body that is accredited in accordance with regulations in part 1, subpart M." 中文大意：PCQI 可经"等效 FSET 培训"或"纯粹工作经验"两条通道取得资格；法定适格审核人例子包括政府雇员（含外国政府）与按 21 CFR Part 1 Subpart M 认可的认证机构审核代理。
- 类型: rule / fact
- 建议归属: supply-chain-verification（审核人适格）+ management-components（PCQI）
- 为什么是指南缺口: 卡只标"PCQI=具名资质个人"；"没上过 FSET 但 15 年厂内经验能不能当 PCQI"（能，须书面论证经验等效）与"外国政府检查员能不能算 qualified auditor"是法规定义的精确答案，指南没落到这个粒度。

### nA-B-07 全体人员（含临时/季节工）的法定资质义务 + 培训记录义务
- 条文出处: § 117.4(a)(b)(c)(d) + § 117.9；chunk: ck-2e62b0f0a35a, ck-c49b9d7bb0bd
- 原文关键句: "Each individual engaged in manufacturing, processing, packing, or holding food (including temporary and seasonal personnel) ... must ... Be a qualified individual ... and Receive training in the principles of food hygiene and food safety"；"Records that document training required by paragraph (b)(2) ... must be established and maintained"（并受 Subpart F 约束）。管理层（management）对 B/F 分部范围人员资质负确保责任，对 C-G 分部范围由 owner/operator/agent 负责；监督职责须明确指派给具资质人员。
- 类型: rule
- 建议归属: 建议新能力（人员资质与记录），或暂并入 regulatory-boundaries 记录层
- 为什么是指南缺口: 指南聚焦 PCQI 一层的人员要求；"季节性临时工算不算、谁对全员资质负法定确保责任、培训记录是受 Subpart F 约束的法定记录"三个硬义务在现有卡中无落点。

### nA-B-08 农场混合型设施低风险"活动×食品"组合豁免清单
- 条文出处: § 117.5(g)(3) 23 项包装/存放组合 + § 117.5(h)(3) 27 项加工组合（食品类别定义在 (g)(2)）；chunk: ck-abd378c5f00d, ck-11dbc26c658c, ck-4948e6e61285, ck-1cc8a6a27a4b
- 原文关键句: "Subparts C and G of this part do not apply to on-farm packing or holding of food by a small or very small business, and § 117.201 does not apply ... by a very small business, if the only packing and holding activities ... are the following low-risk packing or holding activity/food combinations"。含条件性细节：调味花生/坚果制品"provided that the seasonings have been treated to significantly minimize pathogens"；裹糖衣苹果蘸焦糖明确**不**属低风险；切酸果仅限 pH<4.2。中文大意：small 或 very small business 在 farm mixed-type facility 上只做清单内低风险组合时整体豁免 C/G；very small business 连 117.201 简化义务也免。
- 类型: rule
- 建议归属: regulatory-boundaries
- 为什么是指南缺口: 卡的豁免体系只有 qualified facility/极强致死/管辖豁免三条，完全没有这条法定第四通道；"农场里烘焙饼干再打包要不要做 FSP"须按清单+企业规模双维查表回答。

### nA-B-09 酒精设施豁免（≤5% 门槛）、RAC 存储豁免与 Part 112 替代合规路线
- 条文出处: § 117.5(i)(j)(k)、§ 117.7、§ 117.8；chunk: ck-1cc8a6a27a4b, ck-175ef16773a9, ck-2a4ef391e822
- 原文关键句: 酒精设施须同时满足 TTB 许可条件与"engaged in manufacturing ... one or more alcoholic beverages"注册条件；该设施内的非酒精食品豁免前提 "Is in prepackaged form ... and Constitutes not more than 5 percent of the overall sales of the facility"；§117.7 仅存储 unexposed packaged food 者 C/G 不适用，但需时间温度控制以"minimize or prevent the growth of, or toxin production by, pathogens"的走 §117.206；§117.5(k)(1)(v) 仅做坚果脱壳/去壳/干燥/包装/存放的设施连 Subpart B 都豁免（无烘焙等附加加工）；§117.8 离农 RAC 包装存放的 Subpart B 义务可用 Part 112 相应要求替代履行。
- 类型: rule / threshold
- 建议归属: regulatory-boundaries
- 为什么是指南缺口: 酒精设施 5% 预包装门槛、坚果初加工设施连 CGMP 都免、"Part 112 可替代 Subpart B"的二选一合规路线、117.7 里"毒素产生"（如组胺）作为简化义务触发词——都是指南未覆盖的具体适用判定。

### nA-B-10 Defect action levels 的法律地位与"掺混稀释无效"禁止规则
- 条文出处: § 117.110(a)(b) + § 117.3 (Defect action level)；chunk: ck-309a98e30249, ck-74dc4628c862
- 原文关键句: "must at all times utilize quality control operations that reduce natural or unavoidable defects to the lowest level currently feasible"；"The mixing of a food containing defects at levels that render that food adulterated with another lot of food is not permitted and renders the final food adulterated, regardless of the defect level of the final food." Defect action level 定义：非危害性、天然不可避免缺陷达到 FDA 可据 §402(a)(3) 执法的界限。中文大意：质量缺陷控制是持续法定义务（lowest level currently feasible 是动态标准）；把超标批次掺混稀释到限值以下仍违法——终产品不豁免。Defect Levels Handbook 被法条直接引用。
- 类型: rule / threshold
- 建议归属: hazard-analysis-method（B1 质量/安全分界）+ chemical-hazard-controls（天然毒素/缺陷分线）
- 为什么是指南缺口: 卡只说"质量缺陷不进危害分析"；"用合格料稀释问题批次能不能救回"这一常见实务操作的法定答案（不能，掺混即 adulterated）只有 117.110(b) 给出；"lowest level currently feasible"随行业整体水平移动的动态法律标准也未见于指南。

### nA-B-11 清洁剂/消毒剂自身的法定验证义务与毒物四类目允许清单
- 条文出处: § 117.35(b)(1)(2)；chunk: ck-cb52341c6e48
- 原文关键句: "Cleaning compounds and sanitizing agents ... must be free from undesirable microorganisms and must be safe and adequate under the conditions of use. Compliance with this requirement must be verified by any effective means, including purchase of these substances under a letter of guarantee or certification or examination of these substances for contamination." 仅四类毒物允许在食品加工/暴露区使用或存放：卫生维护、实验室检测、厂屋设备维护运转、生产运转之所需。中文大意：化学品危害控制的最上游——清洁剂本身须验证不含不良微生物，验证手段法定列举（担保函/证书/自行检测）；车间内存放毒物封闭四类目。
- 类型: rule
- 建议归属: chemical-hazard-controls
- 为什么是指南缺口: 卡的归途判定讲"设施相关化学危害走 CGMP 即可"，但没说 CGMP 里对清洁剂本身有法定验证要求、以及毒物存放是"允许清单"模式（法无授权即禁止）——"车间能不能存放未列明的消杀药剂"这类问题指南无解。

### nA-B-12 干/湿加工食品接触面清洁的法定分界（干区湿洗须彻底干燥）
- 条文出处: § 117.35(d)(1)(2)(3)；chunk: ck-cb52341c6e48, ck-c0d679e0ce44
- 原文关键句: 低水分食品："Food-contact surfaces ... must be in a clean, dry, sanitary condition before use. When the surfaces are wet-cleaned, they must, when necessary, be sanitized and thoroughly dried before subsequent use." 湿加工："all food-contact surfaces must be cleaned and sanitized before use and after any interruption during which the food-contact surfaces may have become contaminated." 中文大意：干区设备若做了湿式清洁，法定要求"必要时消毒+彻底干燥后方可再用"；湿加工中断后必须重新清洁消毒——"中断即重清"是 cleanup-to-cleanup 回溯逻辑的法定锚点。
- 类型: rule
- 建议归属: environmental-pathogen-sanitation
- 为什么是指南缺口: 卡的"干区防沙门须控水"战略与法条直接衔接（湿洗后彻底干燥是义务不是建议），但卡没引用这条；"湿洗过的干区设备能不能自然晾干/算不算合规"要靠 117.35(d)(1) 回答。

### nA-B-13 再调理（reconditioning）的法定下限：方法须经证明有效，或处理后复检
- 条文出处: § 117.80(c)(9)；chunk: ck-076eafd6e350（引文起于 ck-f07d7b4d9efe 末行）
- 原文关键句: "If the adulterated food is capable of being reconditioned, it must be: (A) Reconditioned (if appropriate) using a method that has been proven to be effective; or (B) Reconditioned (if appropriate) and reexamined and subsequently found not to be adulterated ... before being incorporated into other food." 中文大意：受污染食品的救回只有两条合法路径——用已被证明有效的方法再处理，或再处理后复检确认不再 adulterated 才能并入其他食品；"经验上应该没问题"不是法定出口。
- 类型: rule
- 建议归属: management-components（处置阶梯"再加工"级的法定条件）
- 为什么是指南缺口: 卡的处置阶梯列了"再加工"但没给它法定门槛；"这批受潮香料重新过筛/重烘干合法吗"取决于方法是否有有效性证据——指南只给惯例，法条给证明义务。

### nA-B-14 屏障维持的法定义务：平衡 pH≤4.6 须"监测并维持"、水分依赖须达安全水分活度
- 条文出处: § 117.3 (Acid foods / Safe-moisture level / Water activity) + § 117.80(c)(14)(15)；chunk: ck-74dc4628c862, ck-d4321842b5a9, ck-c163f4b37467, ck-076eafd6e350
- 原文关键句: "Acid foods or acidified foods means foods that have an equilibrium pH of 4.6 or below"；"Food, such as acid and acidified food, that relies principally on the control of pH ... must be monitored and maintained at a pH of 4.6 or below."；依赖 aw 的食品 "must be processed to and maintained at a safe moisture level"，safe moisture level 定义为有充分数据证明该 aw 下不良微生物不增殖的水平。中文大意：pH 4.6 法定基准指"平衡 pH"（非初始/表观 pH）；屏障食品有法定"监测+维持"双义务；安全水分水平须有数据支撑。
- 类型: threshold / rule
- 建议归属: process-control-validation + reference-tools-discipline
- 为什么是指南缺口: "刚酸化完测 4.5、货架期回升怎么办"——equilibrium pH 与 monitored and maintained 直接给出法定答案：屏障是持续监测义务且以平衡值为准；a_w 数据支撑要求把卡内"模型/表值须经验证"纪律升格为法定标准。

### nA-B-15 人食副产品转饲料的法定标识、标签与容器检查义务
- 条文出处: § 117.95(a)(b)(c)；chunk: ck-7b0b045595ce
- 原文关键句: "During holding, human food by-products for use as animal food must be accurately identified"; "Labeling that identifies the by-product by the common or usual name must be affixed to or accompany human food by-products ... when distributed"; 运输容器与散装车辆 "must be examined prior to use"。中文大意：人食工厂副产品（酒糟、豆渣类）转作动物食品时，存放期间须准确标识、分销时须附通用名标签、发货容器使用前须检查——义务按"是否自行运输或安排运输"限定。
- 类型: rule
- 建议归属: 建议并入 regulatory-boundaries（管辖衔接：117.95 与 21 CFR 507.12 动物食品条款衔接）或新能力
- 为什么是指南缺口: 指南基本不讲副产品转饲料路径；"卖酒糟要不要贴通用名标签"是指南完全回答不了、而 117.95(b) 给确定答案的具体问题。

## 二、近重复（指南已覆盖，法规措辞可作强化引用）

- rA-B-01: Hazard 法定定义"any biological, chemical (including radiological), or physical agent that has the potential to cause illness or injury"（§ 117.3；ck-5b32c149c7eb）↔ 现有卡 hazard-analysis-method B 第 1 条（质量缺陷不是 hazard）——可补 §117.3 作权威出处，卡中"按法定定义"的模糊指代可落地。
- rA-B-02: Known or reasonably foreseeable hazard + Hazard requiring a preventive control 定义（严重性×概率、概率须"in the absence of preventive controls"评估）（§ 117.3；ck-5b32c149c7eb）↔ hazard-analysis-method E Step 3 评估框架——法定措辞可强化"十类因素"上游的评估义务来源（§117.130 交叉）。
- rA-B-03: Validation / Verification / Correction / Monitor 四个法定定义（§ 117.3；ck-c163f4b37467, ck-d4321842b5a9, ck-74dc4628c862, ck-5fafd7ac6a65）↔ management-components I 第 2/3 条与 E Step 1/Step 3——"两类证据不可互替""correction 与 corrective action 分诊"均有法条原文可引；注意法定 Correction 定义以"不附带防复发/评估受影响食品/阻止入市等动作"作排除式描述，与卡的分诊逻辑完全一致。
- rA-B-04: RTE food 定义（"reasonably foreseeable that the food will be eaten without further processing that would significantly minimize biological hazards"）（§ 117.3；ck-d4321842b5a9）↔ hazard-analysis-method E Step 3 强制触发器、environmental-pathogen-sanitation 的 RTE 前提——RTE 法定判定基准（消费前无显著最小化生物危害的处理）可作卡内"消费前制备"No 通道的反向锚。
- rA-B-05: § 117.5(a)–(f) 豁免结构：合格设施仅免 C/G、Part 123/120 合规活动豁免、(d)(2) 明确 Part 113 豁免仅限其管辖的微生物危害、(e) 膳食补充剂（111+761 合规）、(f) 农产品安全规则（419 条）活动（ck-aaf66c571fa6, ck-5fb917e59e14）↔ regulatory-boundaries R 段与 E Step 2"按危害类别拆分"——卡的核心主张被 (d)(2) 原文逐字印证，可补全条号出处；(e)(f) 两条豁免通道卡内未点名。
- rA-B-06: § 117.1(c) "Food covered by specific current good manufacturing practice regulations also is subject to the requirements of those regulations"（ck-31931dd3d7ec）↔ regulatory-boundaries 并集原则——"专项 CGMP 与 Part 117 并行不互斥"的法定出处。
- rA-B-07: Supplier 法定定义（"without further manufacturing/processing by another establishment, except ... solely ... addition of labeling or similar activity of a de minimis nature"）（§ 117.3；ck-d4321842b5a9）↔ supply-chain-verification I 第 1 条"经纪商/分销商不是供应商"——de minimis 再加工例外措辞可补作原文引用。
- rA-B-08: Subpart B 通篇把 "protect against allergen cross-contact" 织入 CGMP 义务，§ 117.20(b)(2) 给出法定分离手段清单（location, time, partition, air flow systems, dust control systems, enclosed systems）（ck-d31a61c1d36a, ck-cb52341c6e48 等）↔ allergen-program 支柱 1 CGMP 基线与排产/分区手段清单——法定手段清单比指南更封闭，可作权威出处。
- rA-B-09: § 117.40(f) 控制性仪器法定适格要求（"measuring, regulating, or recording temperatures, pH, acidity, water activity ... must be accurate and precise and adequately maintained, and adequate in number"）（ck-82424ebf2dbb）↔ management-components E Step 1 校准基线——校准义务的 CGMP 层法定出处（卡内只有指南惯例值）。

## 三、潜在矛盾（指南说法 vs 法规措辞不一致）

- cA-B-01（低严重度，措辞不精确）: regulatory-boundaries B 第 1 条称"qualified facility 免的是**全套 PCHF**，但 CGMP 与注册等基本义务仍在"——前半句与法条不符：§ 117.5(a) 明确豁免范围仅为 **Subparts C 和 G**，且 qualified facility 仍须履行 § 117.201 简化要求（Subpart B/F 照常适用）。同卡 Step 3"义务换成简化要求而非消失"的说法与法条一致，属卡内部表述不一致。建议以 § 117.5(a) 措辞统一修正（本任务不改卡，仅记录）。出处：§ 117.5(a)（ck-aaf66c571fa6）↔ regulatory-boundaries B1。
- 其余未发现 Subpart A+B 与现有卡的实质矛盾——卡内"should/must 分层阅读"的纪律（regulatory-boundaries B2、management-components B6）与法规并入后的读法兼容。

---
统计：新知识 15 条（nA-B-01…15）；近重复 9 条（rA-B-01…09）；矛盾 1 条（cA-B-01）。
