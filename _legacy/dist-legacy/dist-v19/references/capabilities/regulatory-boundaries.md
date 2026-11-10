# 双法规与豁免边界（regulatory-boundaries）

*来源分层：本卡融合两类权威——FDA 行业指南（草案，方法论解释）与 21 CFR Part 117 法规正文（最终规则，法定义务）。标注〔§ 117.xxx〕的内容出自法规正文；其余出自指南。*

## R — 原文

> "LACF 食品的生物危害归 part 113（PCHF 不适用），但化学/物理危害 PCHF 仍适用（查附录 1 表 2H）。" ——附录 1 §A1.5.5 及多张表脚注

并集原则（第 16 章 §16.2.3）：酸化食品法规（108.25/part 114）与 PCHF 可**双向借用**程序与记录来满足对应要求，但借用只能部分满足——3 年记录保存、容器编码、Form 2541e 提交等专项超出部分不可免除。专项 CGMP 与 Part 117 并行不互斥的法定出处〔§ 117.1(c)〕："Food covered by specific current good manufacturing practice regulations also is subject to the requirements of those regulations"——受专项 CGMP 法规管辖的食品同时受 Part 117 要求约束。

中文大意：一个产品"受哪套法规管"不是产品级的单选题。法规适用性是"对象×危害类别"的二维矩阵：同一罐酸化莎莎酱，肉毒风险归 part 114/113，化学物理危害归 PCHF，两套义务取并集。

**关于 FDA 专项指南的效力读法**（本卡的第二类边界：不是"哪条法规管我"，而是"指南里那句话约束谁"）：

> "Because some persons who are subject to the CGMP requirements in subpart B are exempt from the PCHF requirements in subparts C and G, this guidance: Is written as a set of recommendations even though in some cases part 117 includes an explicit requirement. ... If you are a facility subject to the PCHF requirements of part 117, you must comply with 21 CFR 117.160(a) even though this guidance “recommends” validation of process controls such as listeristatic and listericidal control measures."
> —— L.mono 指南 III（How to Apply This Guidance…）

> "Uses general terms such as “control” and “control measure” even though in some cases the control or control measure is a preventive control."
> —— L.mono 指南 III

中文大意：这份指南把自己写成一套"建议"，但同一句话对不同主体不是同一件事——只受 CGMP 约束的人读到的是建议；受 PCHF 约束的人，只要 Part 117 有明文要求，"recommends" 背后的 must 就是法定义务（典型如验证〔§ 117.160(a)〕）。另外指南在术语层做了合并：它通篇用泛称 control / control measure，其中许多实为 preventive control。

## I — 自述

这一卡处理 PCHF 全书的边界条件层："哪些规则对我适用"与规则本身同等重要。三类结构化判定：

1. **按危害类别拆分法规适用性**——LACF（低酸罐装食品）的生物危害由 part 113 专门体系管，〔§ 117.5(d)(1)(2)〕据此免其 Subparts C/G 且**仅限 part 113 管辖的微生物危害**；但同一产品的化学/物理危害、以及未被热处理控制的金葡生长产毒 PCHF 仍适用（CP 7303.070 PART II.2.C(1) 逐字确认，见 B10）。酸化食品同理：两套法规按程序逐条划分适用范围，超出部分单独兜底。适用性没有"全有全无"，逐格判定才是合法路径。
2. **豁免与例外体系**——qualified facility 豁免、极强致死工艺豁免、USDA FSIS 管辖、研究用途食品等。其中极强致死工艺是最优雅的一条："做对产品"与"控住危害"可以是同一个动作——工艺的产品属性要求（糖食必须煮沸、咸饼干必须 250°C 烘烤）本身绑定致死条件，工程约束转化为合规论据。法规正文另有三条指南未展开的法定豁免通道〔§ 117.5〕：农场混合型设施低风险"活动×食品"组合清单豁免〔§ 117.5(g)(3) 23 项包装/存放组合 + § 117.5(h)(3) 27 项加工组合〕、酒精设施豁免（非酒精食品须预包装且 ≤5% 总销售额〔§ 117.5(i)〕）、仅贮存未拆封包装食品者 C/G 不适用（需温控的走 § 117.206〔§ 117.7〕）。豁免结构须精确到条款：各通道均只免 Subparts C 和 G，不免 B/F；按 Part 123/120 合规的活动豁免〔§ 117.5(b)(c)〕；Part 113 豁免仅限其管辖的微生物危害〔§ 117.5(d)(2)〕；膳食补充剂合规者（part 111 + 761）与农产品安全规则（FD&C Act 419 条）覆盖的活动分别另列豁免通道〔§ 117.5(e)(f)〕。
3. **管辖不转移判定责任**——供应商的产品过了 USDA 检查，你仍须自己做危害分析；表格列出潜在危害与由谁控制解耦。
4. **不合规的法律定性**（法规独有，指南从不讲"不做的后果"）——应遵守而未遵守 FD&C Act 418 条或 Part 117 C–G 分部的设施运营本身构成 prohibited act〔§ 117.1(a)(1), (b)→FD&C Act § 301(uu)〕；CGMP 失守则直接对应 § 402(a)(3)/(4) 的 adulterated 认定（"unfit for food"/"insanitary conditions"）。豁免判定与义务裁剪的意义不仅是省工作量，更是脱离这条执法钩子的法定出口。
5. **117.136 法定出口实为五情形**（法规视角，细节归 supply-chain-verification 卡）——除指南常讲的情形外，(a)(5) 另开"自主分销链控制体系"通道：自行建立、文件化并运行一套确保在后续分销环节控制危害的体系即可不实施 PC，无需客户书面保证；(a)(2)–(4) 三条客户依赖通道共用法定披露措辞 "not processed to control [identified hazard]" 并须每年取得书面保证，(a)(4) 还要求客户的下游链式传递保证（cascade）〔§ 117.136(a)(1)–(5)、(b)〕。
6. **指南的"建议"与法规的"必须"要逐句分层，且分层取决于主体身份**（读 FDA 专项指南时的元规则）——一份指南把全文写成 "we recommend that you…"，不等于它对所有读者都只是建议：只受 CGMP（subpart B）约束、因某些豁免而免 subpart C 与 G 的主体，读到的整份指南都是建议；受 PCHF 约束的主体则不然——指南写"recommends"而 Part 117 有明文要求的部分就是 must，典型如验证〔§ 117.160(a)〕。所以"这句话我能不能不做"必须先问主体身份。
7. **指南的排除情形只影响"这套建议怎么读"**——指南声明自己不适用于某类加工者（最终包装内施加致死措施者、不受 Part 117 约束的农场），这是"我该读哪部分建议"的边界，不是"我是否受 Part 117 约束"的边界；两套适用性各自独立判定（见 E 段 Step 1）。

## A1 — 书中案例

**案例 1：Salsa Processor A 的双法规叠加（第 6 章 §6.16）**
直接酸化莎莎酱（pH 4.1）同时受两套法规约束：pH 4.1 屏障控肉毒与腐败芽孢菌（part 114 管辖），热处理 158°F/1.5 min 对营养细胞病原 5D（PCHF 工艺控制）；作为酸化食品还须向 FDA 提交 Form 2541e 定时工艺备案——这是 PCHF 借用不到的专项义务。演示"义务并集、逐项清点"的实际形态。

**案例 2：极强致死工艺的 No 判定（附录 1 §A1.6.1.3/§A1.8.3）**
焦糖在约 240°F 煮沸、果酱熬煮、咸饼干 250°C×4.5 min——这些工艺的产品属性要求（质地/稠度）与致死性绑定：不充分加热就做不出合格产品，因此 SME 对这类食品甚至不标记潜在生物危害。工厂可凭极强致死把汤酱等弱案例的 X 标记判为"不需控制"，理由须书面化并引用工艺证据。

**案例 3：FSIS 管辖配料的判定责任（附录 1 §A1.6.1.4）**
供应商的蛋液已过 USDA 检查并巴氏杀菌，收货方仍须在危害分析里列沙门氏菌（识别端不筛选）；分析后可得出"由供应商巴氏杀菌控制"的结论——USDA 检查不能替代收货方自己的判定，表格列出与控制主体解耦。

## A2 — 未来触发

**用户情境：**
1. 产品属于低酸罐装/酸化食品，问要不要做 FSP、哪些义务重叠、哪些必须单做。
2. 问"我的产品能不能豁免 PCHF"（qualified facility、极强致死工艺、研究用途）。
3. 供应商产品归 USDA/其他机构管辖，问自己还要不要做危害分析。
4. 多法规交叉产品（自热火锅类：食品+危险品）问适用性怎么切。
5. 存量 HACCP 或酸化食品体系企业问升级/并行时的义务清单。
6. 拿到一份 FDA 专项指南（草案），问"这条建议我算不算必须做"、"我厂在不在它的适用范围内"。

**语言信号**："豁免/exempt"、"qualified facility"、"低酸罐装/LACF"、"酸化食品/acidified/part 114/108.25"、"part 113"、"USDA/FSIS 管辖"、"双法规"、"Form 2541e"、"极强致死"；英文：exemption, qualified facility, LACF, acidified food, dual regulation, jurisdiction。

**与相邻卡的区分**：与《危害分析方法》（hazard-analysis-method）区分——"No"判定的通用书面纪律在那张卡；本卡只讲有法定依据的特定 No 路径（极强致死、管辖豁免、双法规拆分）。与《召回计划》（recall-plan）区分——酸化食品召回计划需补"通知 FDA"程序属于本卡的并集缺口清单，召回执行本身在那张卡。与《权威参考表与数据使用纪律》（reference-tools-discipline）区分——附录 1 表的使用纪律在那张卡；本卡讲的是法规适用性矩阵，不是查表方法。

## E — 执行要点

**Step 1 产品定性（先问管辖再问危害）**
- 走三问：是否 LACF（pH>4.6 且 a_w>0.85 的罐装）？是否酸化食品（加酸降 pH 至 4.6 以下）？是否落入其他管辖（USDA FSIS 肉禽蛋、研究用途、qualified facility）？
- 完成标准：产品在"对象×危害类别"矩阵上逐格标注管辖归属。
- **再问一层：手上这份专项指南适用于本设施吗**（以 FDA《Control of Listeria monocytogenes in Ready-To-Eat Foods: Guidance for Industry（Draft，2017 年 1 月）》为例）。指南自述的两类不适用情形须在定性阶段就排除，否则后面整套建议都读错了对象：
  > "This guidance is not directed to processors of RTE foods that receive a listericidal control measure applied to the food in the final package, or applied to the food just prior to packaging in a system that adequately shields the product and food contact surfaces of the packaging from contamination from the food processing environment."
  > —— L.mono 指南 I（Introduction）

  > "This guidance also is not intended for food establishments that are not subject to part 117, such as farms."
  > —— L.mono 指南 I（Introduction）

  读法：①**致死措施的位置**决定是否落入指南范围——在最终包装内施加、或在紧邻包装前施加且该系统能充分屏蔽产品与包装的食品接触面不受环境污染，这两类加工者不在指南的适用对象内；②**不受 Part 117 约束的场所**（如农场）不在指南对象内。这与法规侧的适用性是两个问题：指南的排除情形只影响"这套建议怎么读"，不影响 Part 117 本身对产品的适用性。危害分析里的分流动作见 `hazard-analysis-method` 卡。
- **指南本身也不设法律责任**——这一点决定了"照着指南做"能到什么程度：
  > "FDA’s guidance documents, including this guidance, do not establish legally enforceable responsibilities. Instead, guidance describes the Agency's current thinking on a topic and should ... be viewed only as recommendations, unless specific regulatory or statutory requirements are cited."
  > —— L.mono 指南 I（Introduction）
  同章给出 "should" 的官方口径："The use of the word *should* in Agency guidance means that something is suggested or recommended, but not required."〔L.mono 指南 I〕故本卡分层标注：〔§ 117.xxx〕是法定义务，L.mono 指南条款一律为建议层。
- **指南与专项指南互补而不取代**——同一产品可能同时落在多份指南的适用范围内：
  > "In general, the recommendations in this guidance complement, but do not supersede, recommendations that we have issued in other guidance documents."
  > —— L.mono 指南 III
  指南自举例：处理供寿司用的海鲜时，仍应遵循 part 123 的鱼类 HACCP 指南（Ref. 49）。

**Step 2 矩阵逐格切分**
- LACF：生物危害→part 113 专项体系；化学/物理危害→PCHF 仍适用（照常查附录 1 表 2H 评估）。
- 酸化食品：108.25/part 114 与 PCHF 双向借用程序与记录；逐项清点专项缺口——3 年记录保存、容器编码、Form 2541e 提交、BPCS 专项培训、召回计划补"通知 FDA"程序。
- 完成标准：义务并集清单，禁止"取更严的那个就够"策略。

**Step 3 豁免判定（每条都要书面）**
- 极强致死路径：证明"工艺的产品属性要求本身绑定致死条件"（如焦糖必须煮沸）→生物危害判 No；豁免以工艺稳定受控为前提，参数漂移则豁免自动失效，须书面引用工艺证据。
- qualified facility 精确门槛（两段式测试，非单看销售额）〔§ 117.3〕——两条独立通道：(1) very small business（3 年年均食品销售额 <$100 万，含未销售货物的市场价值；small business 口径为 <500 名全职当量员工 FTE，FTE=总工时÷2,080 向下取整〔§ 117.3〕）；或 (2) 两段式测试：直销 qualified end-users 的年均货值须**超过**卖给其他购买者的年均货值（占比过半是第一要件，常被漏检），且年均总销售额 <$50 万（通胀调整）。qualified end-user 有地理约束：与设施同州，或距设施 ≤275 英里（直接卖给消费者的零售商等）〔§ 117.3〕。门槛计算须合并计入所有 affiliate（含母/子公司）的销售额〔§ 117.3〕。
- 豁免的实质是"减配"不是"消失"〔§ 117.201〕：qualified facility 仅免 Subparts C 和 G〔§ 117.5(a)〕，Subpart B（CGMP）与 F（记录）照常，且须履行替代义务——向 FDA 提交**双份保证书**：身份保证（含资格判定，通胀调整以 **2011 年为基线年**）+ 二选一的业务保证：(i) 已识别潜在危害、正实施预防控制、在监控其性能；或 (ii) 符合州/地方/部落/外国等非联邦食品安全法（可凭执照、检查报告、证书佐证）〔§ 117.201(a)〕。注意 (a)(2)(i) 意味着豁免企业仍须实际识别危害+实施 PC+监控，只是免写全套 FSP。邮寄用 Form FDA 3942a〔§ 117.201(a)〕。
- 选 (ii) 非联邦法轨道的隐性对价〔§ 117.201(e)〕：未提交 (a)(2)(i) 保证书的合格设施必须向消费者披露制造/加工设施的名称与完整地址——有标签的在标签显著处，无标签的在购买点标签/海报/标牌/随附文件，网络销售用电子通知。豁免判定 Step 3 的必填分支。
- 合格设施合规日历〔§ 117.201(c)(d)〕：每年 7 月 1 日前完成并记录资格判定；保证书自 2020 年起每 2 年在 10 月 1 日–12 月 31 日窗口提交；丧失资格须 7 月 31 日前用 Form 3942a 通知 FDA，并于当年 12 月 31 日前满足 Subparts C+G 全套合规——"unless otherwise agreed to by FDA"，宽限期可双边协商〔§ 117.201(d)〕。
- 农场混合型设施第四豁免通道〔§ 117.5(g)(3)(h)(3)〕：small 或 very small business 在 farm mixed-type facility 上只做低风险"活动×食品"组合清单内项目（23 项包装/存放 + 27 项加工）时整体豁免 C/G，very small business 连 § 117.201 简化义务也免。查表须"活动×食品"双维，注意清单细节：裹糖衣/蘸焦糖苹果明确**不属**低风险；切酸果（cranberry）仅限 pH<4.2；调味坚果制品须调味料已经消毒害处理（"provided that the seasonings have been treated to significantly minimize pathogens"）。
- 酒精设施与非酒精食品〔§ 117.5(i)〕：同时满足 TTB 许可与"制造酒精饮料"注册条件的设施，其非酒精食品豁免前提为预包装 + ≤5% 设施总销售额。仅贮存未拆封包装食品者 C/G 不适用〔§ 117.7〕，但需时间/温度控制以防病原增殖或**产毒**的走 § 117.206。仅做坚果脱壳/去壳/干燥/包装/存放（无烘焙等附加加工）的设施连 Subpart B 都豁免〔§ 117.5(k)(1)(v)〕；离农 RAC 包装存放的 Subpart B 义务可用 Part 112（农产品灌溉水质规则）相应要求替代履行〔§ 117.8〕。
- 纯贮存设施裁剪义务包〔§ 117.206〕：仅贮存未拆封包装食品者不做全套 FSP；但贮存需时间/温度控制的冷藏包装食品须做五项——温度控制、温度监控、失控纠正措施、验证（时钟校准+监控/纠正记录审查沿用 7 工作日规则+PCQI 书面论证）、记录（肯定记录或例外记录均可）。
- 管辖转移：供应商受 USDA 检查≠免自己的危害分析；识别端不筛选，评估后可把控制指给供应商。
- 副产品转饲料管辖衔接〔§ 117.95〕：人食工厂副产品（酒糟、豆渣类）转作动物食品时，存放期间须准确标识；分销时须附以通用/常用名标识的标签；运输容器与散装车辆使用前须检查（义务按是否自行运输或安排运输限定）——与 21 CFR 507.12 动物食品规则衔接，指南基本不讲此路径。
- 完成标准：每条豁免/No 结论有书面依据并可向检查官出示。

**Step 4 复核触发**
- 法规版本、产品配方（pH/水分活度变化可能切换管辖）、工艺参数三者任一变更→重新走 Step 1。
- 复核时可用指南自带的条款对照索引定位责任条款：它把"指南讨论的内容"与"Part 117 条款"一一挂上，是判定某句话到底是建议还是义务的导航表。表 1 是 CGMP 侧（§ 117.10 Personnel、117.20 Plant and grounds、117.35 Sanitary operations、117.37 Sanitary facilities and controls、117.40 Equipment and utensils、117.80 Processes and controls、117.93 Warehousing and distribution），表 2 是 PCHF 侧（§ 117.126/130/135/139/140/145/150/155/160/165/170/190）〔L.mono 指南 II.A 表 1 / 表 2〕。
  用法：读到一条指南建议时先在表里找对应条款号——对上的按法规口径处理，表里没有的即为纯建议层。两张表按 CGMP/PCHF 两条线分列，正好对应本卡"义务并集"的判定结构。

## B — 边界

1. **豁免不是零义务**：qualified facility 免的仅是 Subparts C 和 G〔§ 117.5(a)〕，Subpart B（CGMP）与 F（记录）照常适用，且须履行 § 117.201 替代义务（双份保证书，见 E Step 3）——"豁免"实为"减配"；极强致死豁免只覆盖其致死性确实绑定的危害类别，化学物理危害不受影响。
2. **文件为草案且滚动发布**：本卡引用的章节划分（Ch16 已发布）与专项清单可能随定稿调整；执行前核对现行法规原文，不要把指南建议（should）当强制（must）。
3. **双法规借鉴有硬边界**：借用只减少重复工作量，不减少义务总量——"满足更严的法规就行"是 FDA 明确否定的错误策略。
4. **美国中心**：全部建立在 FD&C Act/21 CFR 体系上；中国读者映射到 GB 体系时只有"适用性逐格判定"的方法结构可迁移，具体豁免门槛、Form 2541e 类备案义务不可类推。
5. **不要用豁免逻辑反向逃避**：极强致死工艺的 No 是科学结论不是省事出口——若工艺实际无法稳定达到宣称参数，继续引用该豁免等于带着漏洞运行。
6. **执法裁量参考不是义务来源**：FDA《Food Defect Levels Handbook》给的是 defect action level（§ 117.3 定义为 FDA `may regard ... adulterated` 的水平），与「企业必须做什么」分属两层。法定义务在〔§ 117.110(a)〕的 `must ... reduce ... to the lowest level currently feasible`、〔§ 117.110(b)〕掺混禁令与〔§ 117.80(b)(3)(4)〕原料要求；低于行动水平仍可因 FD&C Act 402(a)(4) 不卫生条件被判掺假。⚠ **v4.7 纠错**：网页首句的 `21 CFR 110.110` **不是过时引用**——FDA 2018-09-12 撤回了 2015 规则拟删除 part 110 的 amendatory instruction 13，Part 110 至今有效、eCFR 仍列 11 个 sections；但 **part 110 正文本包未收**，须标「转引未收」，Part 117 侧义务仍回〔§ 117.110〕核对，且手册那句 'Poor manufacturing practices...' 是 §110.110(c) 的意译、**不得标成〔§ 117.110(c)〕**（§117.110 只有 (a)(b) 两款）。另注意过敏原标签问答 Ed.5 与缺陷行动水平虽然都是「FDA 给的数值」，法源分别是 FD&C Act 403(w) 与 402(a)(3)，与 Part 117 预防控制互不减免。详见 `defect-action-levels` B2 与 CAP-20 B2。
7. **指南的章节交叉引用自身就不可靠，引用前须核对原始 PDF 目录**：指南正文里存在指向错误章节的交叉引用（例如把书面预防性维护程序的建议指向 IV.C，而 IV.C 实为 Clothing；另有条目把 "section V.A.1" 用作人员控制的前置引用）。所以**照抄章节号会把读者带到错误段落**——本卡引用的每个 L.mono 指南小节号都须回原始目录核对；出现矛盾时先怀疑标注，再怀疑内容。
8. **检查员作业指导不是义务来源，也不是效力栈的一层**：FDA CPGM 7303.040（现行版 `2025-CPM-HFP-001`）规范的是 Divisions / HFP OCE 如何检查、分级、上报与建议执法，属内部作业指导；它与《Food Defect Levels Handbook》的执法裁量参考、Guidance for Industry 的建议层、21 CFR Part 117 的法定义务是四种不同性质的文件，不可互相替代。企业义务与合规结论只能回〔§ 117.xxx〕；CPGM 的 15 个工作日 483 回复期望、6 个月跟进检查、Direct Reference 会签流程都不是企业法定时限。检查类型、记录举证与三层分级见 `inspection-readiness` 卡。
9. **v4.5 再补两份检查员侧文件，性质相同但分工不同**：CP 7303.050（2022 签发 / 2025-09-10 更正，非 2025 新签发 program）是**抽样 program**，`Inspections are not planned under this compliance program`——样品量（Table 2/3）、环境拭子（ATTACHMENT A，Listeria ≥50 / Salmonella ≥100）、WGS 与 PART V 逐案执法阶梯都是 FDA 内部取证与建议口径，**不是企业义务、不是放行标准**；IOM 2026 Chapter 5 是**调查员作业手册**（仅本包收 Ch.5 单章），给 FD&C Act 704(a)(1) 下的进场、482/483/484 表单、483 措辞纪律、807(b) 拒绝入境后果与证据规则。特别记住 IOM 5.5.10.7 / 5.5.11.3：`Do not cite deviations from policy or guidance documents on the FDA 483`——**检查员自己都不能拿 guidance 偏离开观察项**，这从制度上印证了本卡第 2、6、8 条的效力分层；但不得误读成「指南可以不做」，事实若同时违反〔§ 117.xxx〕仍是观察项。引用分别用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」与「IOM 5.x.x」，全包十九类不可混引。详见 CAP-17 / CAP-18 / CAP-19。
10. **v4.6 补入 CP 7303.070，把本卡第 1 条的双法规并集落到检查员侧**：CP PART II.2.C(1) 与法规正文一致地写明，LACF 产品受 Part 117 约束，但〔§ 117.5(d)(1)〕豁免 Subparts C/G **仅限 part 113 覆盖的活动**、且须 `required to comply with, and are in compliance with` part 113，〔§ 117.5(d)(2)〕进一步限定**仅限 part 113 管辖的微生物危害**；未被热处理控制且需预防控制的危害（`Staphylococcus aureus` 生长产毒、化学、物理）仍归 Subparts C/G。⚠ **酸化食品不在该豁免内**：CP 原文 `Acidified foods are subject to the CGMP & PCHF rule`，PCHF 覆盖转 7303.040，检查重点仍在 21 CFR part 108/114；**〔§ 117.201〕是 qualified facility 的 modified requirements，不是 LACF 条款**。CP PART II.2.C(2) 另给 `Keep Refrigerated` 免 113/114 → 7303.050、brites 中央仓 → `PAC 03040` 两条路由。**v4.7 更新**：21 CFR Part 113 / 114 法规正文已收（CAP-20），自此「法规正文层」含 Part 117 / 113 / 114 三套独立编号（**v4.9 增为四套：加 Part 123，见 CAP-22**），本卡第 1 条「Part 117 是唯一法定义务判定基准」须理解为「判定 **Part 117 义务**的唯一基准」；〔§ 114.5〕还明文并列 `parts 110 and 117` 用于酸化食品掺假判定（Part 110 至今有效，正文未收）。**仍未收**：21 CFR part 108 / 110 / 120 正文（part 123 自 v4.9 起已收），CP 内相关表述一律标「转引未收」。完整判定见 CAP-19（检查员侧）与 CAP-20（法条侧）。

---
