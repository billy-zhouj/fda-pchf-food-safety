# 阶段 1 候选池 — 反例提取器（v4.10 / 第 15 类来源）

- **源文档**：`C:/Users/周至/AppData/Local/Temp/seafood_guide.md`（FDA《Fish and Fishery Products Hazards and Controls Guidance》June 2022 Edition，第 4 版导出全文，共 31,322 行；本文件所有行号均以此导出件为准）。
- **角色定位**：检索式取块提取（局部命中型）。仅做只读分析，产出 1 份候选池文件，供第 15 类来源蒸馏成 1 张能力卡的 **B（边界）段**取用。
- **检索策略**：以任务给定的 7 组行号为锚点逐段 `Read` 核对原文；并用 `Grep` 以 `should not / do not / does not / may not / not / however / Note that / except / cannot / unlikely / warning / new or emerging / substitution` 为一组，以 `does not … control / not adequate / cannot be relied upon / does not ensure / not intended / not designed to / not a substitute` 为补充组，在全篇定位 Ch.7 组胺、Ch.12 病原菌生长、Ch.13 肉毒章节中「某做法不足以控制」类明文警告；封面与页脚版本、Appendix 8 / Addendum 1 法规转录位置用 `June 2022`、`June 2021`、`Appendix 8`、`Addendum 1`、`PART 123` 定位。
- **阶段 0 批判结论的承接**：新卡须同时防两个方向的误读 —— ①「把指南当法规」（把 guidance 的 `should` 读成 `shall`、把示例数值当法定清单）；②「把 Part 123 法定义务当可选项」（把 `must` / `21 CFR 123.6` 的义务稀释成建议）。X-01 为双向防呆主锚点，X-02、X-03 强化 ①，X-01、X-07 强化 ②。
- **引用合规口径**：所有 `> ` 引用块只取散文段落、每段 ≤100 词、标行号；表格内容、页码 / 页眉 / 页脚、Appendix 3 残表一律不作逐字引用，只在字段文字中给行号并描述。
- **产出时间**：2026-11-06。
- **反例数量**：14 条（X-01 ~ X-14）。

---

## X-01 把 guidance 的 `should` 读成 `shall`；反向把 Part 123 的 `must` 稀释成「可选」

- **依据行号**：L100–108；L1447–1453；L178–179；L210–211；L1852–1854（引 21 CFR 123.6(c)(2)）；L185–189。
- **错误做法**：方向 ① —— 把指南里每一句 `should` 都当成强制法定义务，据此要求企业「必须」照做，或反过来宣称「FDA 指南规定了某关键限值」；方向 ② —— 因为「这只是 guidance、不具强制力」，就把指南中明文转述的法规义务（做危害分析、编制 HACCP 计划、每个显著危害至少一个 CCP、按 §123.7 / §123.8 保存记录、LACF 的强制控制）也一并当成「推荐、可酌情省略」。
- **为什么错 / 正确做法**：指南整体不设定法律上可强制执行的责任，`should` = suggested or recommended, but not required；但「unless specific regulatory or statutory requirements are cited」—— 一旦文本点名 21 CFR 123 / 113 等法规，那些 `must` / `require` / `shall` 是法定义务，其效力来自法规本身而非指南。正确读法：把「指南的建议层」与「被引法规的义务层」分开；`For every significant hazard, there must be at least one CCP` 属后者，不可选。
- **归属边界建议**：**效力层级** —— B 段「指南 ≠ 法规」与「法定义务不可选」双向防呆的主锚点，应置于 B 段开头。

> FDA's guidance documents, including this guidance, do not establish legally enforceable responsibilities. Instead, guidance describes the Agency's current thinking on a topic and should be viewed only as recommendations, unless specific regulatory or statutory requirements are cited. The use of the word "should" in Agency guidance means that something is suggested or recommended, but not required.
> 〔L100–108〕

> For every significant hazard, there must be at least one CCP where the hazard is controlled (21 CFR 123.6(c)(2)).
> 〔L1852–1854〕

---

## X-02 把控制策略示例的关键限值 / Appendix 5 数值当成合规清单或法定义务

- **依据行号**：L115–126（含 L121–126）；L27445–27462（Appendix 5 表头与「FDA and EPA Safety Levels」）；L27618；L6683–6686。
- **错误做法**：把 Ch.4–21「控制策略示例」里给出的关键限值（如冻结时温、盐度、水相盐、时间-温度）、或 Appendix 5「FDA and EPA Safety Levels in Regulations and Guidance」里的 tolerance / action level / guidance level，抄成「合规阈值清单」，认为达到即合法、未达到即违法，并直接把 guidance level 写进 HACCP 计划当控制措施。另一个反向错法：随意改用别的控制策略或自定关键限值，却不给科学论证。
- **为什么错 / 正确做法**：这些策略与数值是「recommendations … unless they are required by regulation or statute」，目标是「likely result in a HACCP plan that is acceptable to FDA」，不是法条本身。企业可选用其他控制策略，但须「comply with the requirements of the applicable food safety laws and regulations」且「should scientifically establish their adequacy」；guidance levels 明文「not intended to be identified in the HACCP plan as a control measure」。此外 L27445 明示：无论是否已有某个 established level，FDA 仍可依 FD&C Act 对掺假食品采取执法行动 —— 数值不是合规护身符。正确做法是把示例数值当「经论证的起点」，不是「法定终点」。
- **归属边界建议**：**效力层级** —— B 段「示例 / 数值 ≠ 法定义务」条，与 X-01 的 ① 同侧。

> The control strategies and practices provided in this guidance are recommendations to the fish and fishery products industry unless they are required by regulation or statute. This guidance provides information that would likely result in a HACCP plan that is acceptable to FDA. Processors may choose to use other control strategies, as long as they comply with the requirements of the applicable food safety laws and regulations. However, processors that chose to use other control strategies (e.g., critical limits) should scientifically establish their adequacy.
> 〔L115–126〕

> Guidance levels are not intended to be identified in the HACCP plan as a control measure.
> 〔L27618〕

---

## X-03 把指南当成危害分析的替代品（照抄表格即算完成 hazard analysis）

- **依据行号**：L137–144（含 L139–144 的 `new or emerging`）；L210–217；L172–181；L19770–19782。
- **错误做法**：不自行做危害分析，直接把 Ch.3 表的打勾结果或某章示例粘贴进 HACCP 计划，认为「指南已替我判过危害」；并据此认为指南之外的危害（新出现毒素、区域 / 厂房特有危害、非鱼配料带来的危害、进口商验证程序、HACCP 计划再评估）都不用管。
- **为什么错 / 正确做法**：指南明文「not a substitute for the performance of a hazard analysis by a processor … as required by FDA's regulations」—— 危害分析是 §123.6 施加给加工者的法定义务，主体不能转移给文档。指南还自陈「does not cover reassessment of the HACCP plan … as mandated by § 123.8」「does not provide specific guidance to importers」等范围缺口。正确做法：以指南为参考资料之一，由加工者结合产品、工艺、区域、新出现危害（new or emerging problems）独立完成危害分析并留痕。
- **归属边界建议**：**效力层级** —— B 段「指南是参考、不是危害分析本身」条，同时兜住「法定义务不可外包给文档」。

> The guidance is not a substitute for the performance of a hazard analysis by a processor of fish and fishery products, as required by FDA's regulations. Hazards not covered by this guidance may be relevant to certain products under certain circumstances. In particular, processors should be alert to new or emerging problems (e.g., the occurrence of natural toxins in fish not previously associated with that toxin).
> 〔L137–144〕

---

## X-04 单独用 Ch.3 表判定 `reasonably likely to occur`

- **依据行号**：L127–136；L2125–2134；L1761–1769（Step 9 要求查阅 Ch.4–21）。
- **错误做法**：只翻 Ch.3 的 Table 3-2 / 3-3 / 3-4，看某物种或成品类型有没有「√」，就直接填「该危害 reasonably likely to occur = Yes / No」，跳过后续章节。
- **为什么错 / 正确做法**：表只提供「determining which hazards are reasonably likely to occur」的 guidance，且明文「the tables should not be used separately for this purpose」；表列的是 **potential hazards**，必须「combined with the information in the subsequent chapters」以及「your own expertise or that of outside experts」才能定显著性并定控制方式。Ch.3 的 NOTES 与 Step 9 都把读者导向 Ch.4–21。正确做法：表 → 潜在危害清单 → 逐危害查对应控制章节 → 结合自身产品 / 工艺定显著性。
- **归属边界建议**：**判定逻辑** —— B 段「表是输入、不是判定结论」条。

> The information contained in the tables in Chapter 3 and in Chapters 4 through 21 provide guidance for determining which hazards are "reasonably likely to occur" in particular fish and fishery products under ordinary circumstances. However, the tables should not be used separately for this purpose. The tables list potential hazards for specific species and finished product types. This information should be combined with the information in the subsequent chapters to determine the likelihood of occurrence.
> 〔L127–136〕

> The tables provide lists of potential hazards. You should use the tables, together with the information provided in Chapters 4 through 21, and your own expertise or that of outside experts, to determine whether the hazard is significant for your particular product or process and, if so, how it should be controlled.
> 〔L2128–2134〕

---

## X-05 把 Ch.3 表当成「穷尽清单」，忽略表外 / 区域 / 厂房特有 / 新出现危害

- **依据行号**：L1709–1719；L1753–1760；L137–144；L2125–2134。
- **错误做法**：认为「表里没打勾 = 该物种 / 该工艺没有这个危害」，于是省略对表外危害的识别；不引入自身或外部专长，也不考虑本区域、本厂房、本设备、本工艺特有或新出现的危害。
- **为什么错 / 正确做法**：表只是「the best information currently available to FDA」，是「当前最佳」而非「穷尽」。指南两处都要求「use your own expertise, or that of outside experts … to identify any hazards that may not be included in the table」，并点名 `new or unique to your region` 与 `new or unique to your physical plant, equipment, or process`；L141–144 又要求警惕 `new or emerging problems`。正确做法：把表当基线，用专长做增量补全，并留痕说明为何判无。
- **归属边界建议**：**判定逻辑** —— B 段「表非穷尽、须专长补全」条，与 X-04 配对（一个防「单独用表」，一个防「迷信表全」）。

> Tables 3-2 and 3-3 include the best information currently available to FDA concerning hazards that are specific to each species of fish. You should use your own expertise, or that of outside experts, as necessary, to identify any hazards that may not be included in the table (e.g., those that may be new or unique to your region).
> 〔L1709–1715〕

> Table 3-4 includes the best information currently available to FDA concerning hazards that are related to specific processing techniques. You should use your own expertise, or that of outside experts as necessary, to identify any hazards that may not be included in the table (e.g., those that are new or unique to your physical plant, equipment, or process).
> 〔L1753–1760〕

---

## X-06 物种替换后按标签上的错误鱼种查表

- **依据行号**：L2157–2181（含 Table 3-1 的替换案例）；L2135–2143；L2125–2134。
- **错误做法**：拿到原料后只信包装 / 发票上的市场名，按该名字去 Table 3-2 / 3-3 查「species-related hazards」，据此填危害分析，未核实真实物种。
- **为什么错 / 正确做法**：指南专设 `Species substitution` 段，指出以次充好既可能是经济欺诈 / misbranding，更会「cause potential food safety hazards to be overlooked or misidentified by processors or end users」—— 按错鱼种查表得到的潜在危害集合是错的（表 3-1 的 Escolar→Sea Bass、Puffer Fish→Monkfish 等实际事故即为例）。正确做法：把物种身份核验（含供应链 / 标签一致性）前置为危害分析的输入前提；市场名的权威判定另见 `The Seafood List`，本指南不是该用途的官方来源（L2139–2140）。
- **引用说明**：L2159–L2163 之间被导出件插入了页脚 `3 - 1 (June 2021).`（L2160），下列引用已按散文原句重建、剔除该页脚，未逐字引用页码。
- **归属边界建议**：**判定逻辑**（兼 **范围**）—— B 段「输入身份错误则全表结论失效」条。

> Illicit substitution of one species for another may constitute economic fraud and/or misbranding violations of the Federal Food, Drug, and Cosmetic Act. Furthermore, species substitution may cause potential food safety hazards to be overlooked or misidentified by processors or end users, as shown in Table 3-1, "The Effect of Misbranding through Species Substitution on the Identification of Potential Species-Related Hazards." These examples are based on actual incidents of species substitution or misbranding.
> 〔L2158–2170，已剔除插入的页脚 L2160〕

---

## X-07 把「已有控制、从没出过事」当成「危害不显著」

- **依据行号**：L1715–1731；L172–181。
- **错误做法**：以「我们船上一直有时温控制、这款鱼从没发生过组胺 / 寄生虫问题」为由，把该危害判为 `not reasonably likely to occur`，在 Column 3 填 No，并把既有控制排除在 HACCP 计划之外。
- **为什么错 / 正确做法**：指南明文「The presence of such controls does not mean that the hazard is not significant. The likelihood of a hazard occurring should be judged in the absence of controls.」显著性须在「无控制」的假设下判断。文本给出两种情形：鱼本身不能产生组胺 → 才判 `not reasonably likely to occur`；之所以没出事是因为已有控制 → 仍判 `reasonably likely to occur`，且「the controls should be included in the HACCP plan」。把「没出事」当「不显著」是因果倒置，且会把法定义务要求的控制漏出 HACCP 计划。
- **归属边界建议**：**判定逻辑** —— B 段「显著性在『无控制』前提下判定」条，是判定逻辑类最核心的反例；同时兜住「法定义务不可被『没出过事』豁免」。

> You may already have effective controls in place for a number of these hazards as part of your routine or traditional handling practices. The presence of such controls does not mean that the hazard is not significant. The likelihood of a hazard occurring should be judged in the absence of controls.
> 〔L1715–1721〕

> In the first case, the hazard is not reasonably likely to occur. In the second case, the hazard is reasonably likely to occur, and the controls should be included in the HACCP plan.
> 〔L1728–1731〕

---

## X-08 「某步显著 = 必须在该步控制」以及「填 No 就不写理由」

- **依据行号**：L1813–1827；L1828–1836（Step 11 判定树）；L1837–1851。
- **错误做法**：其一，在 Column 3 判「Yes」的每一个加工步骤都就地设一个 CCP / 控制措施；其二，Column 3 填「No」时把 Column 4 留空，认为「不显著就无需解释」。
- **为什么错 / 正确做法**：关于其一，指南明文「identifying a hazard as significant at a processing step does not mean that it must be controlled at that processing step」，CCP 位置由 Step 11 的判定树决定，且同一危害的不同控制策略示例常对应不同 CCP。关于其二，「You should record the reason for your 'Yes' or 'No' answer in Column 4」—— Yes / No 都要写理由；填 No 只豁免 Step 11–18，不豁免理由记录（记录义务另见 §123.7 / §123.8）。
- **归属边界建议**：**判定逻辑** —— B 段「显著性判定 ≠ CCP 定位」与「No 也须留痕」两条并列。

> If you determine that a potential hazard is significant at a processing step, you should answer "Yes" in Column 3 of the Hazard Analysis Worksheet. If you determine that a potential hazard is not significant at a processing step, you should answer "No" in that column. You should record the reason for your "Yes" or "No" answer in Column 4.
> 〔L1813–1820〕

> It is important to note that identifying a hazard as significant at a processing step does not mean that it must be controlled at that processing step. Step 11 will help you determine where in the process the critical control point is located.
> 〔L1823–1827〕

---

## X-09 用盐渍 / 醋渍 / 酸渍（含柠檬汁腌鱼）当作能杀寄生虫的控制

- **依据行号**：L4692–4697；L4698–4702；L4645–4652。
- **错误做法**：把 brining、pickling，以及据此类推的柠檬汁 / 酸渍生鱼（ceviche、drunken crab 等）当作「足以消除寄生虫」的 CCP 控制，认为腌过即可生食、无需冻结或加热验证。
- **为什么错 / 正确做法**：指南明文盐渍与醋渍「may reduce the parasite hazard … but they do not eliminate it, nor do they minimize it to an acceptable level」，并给硬证据：线虫幼虫在 80° salinometer（21% 盐 by weight）盐水中存活 28 天。既然连 21% 盐水 28 天都不灭活，把它外推到低浓度、短时的酸 / 柠檬汁腌渍是更站不住的（属于「从文本可严格推出的高误读风险」）。正确做法：寄生虫控制须用经论证有效的手段（冻结 / 充分加热），腌渍至多作为减量辅助，不能单独使危害降到可接受水平。
- **归属边界建议**：**控制有效性** —— B 段「减量 ≠ 消除 / ≠ 降到可接受水平」条。

> Brining and pickling may reduce the parasite hazard in a fish, but they do not eliminate it, nor do they minimize it to an acceptable level. Nematode larvae have been shown to survive 28 days in an 80° salinometer brine (21% salt by weight).
> 〔L4692–4697〕

---

## X-10 把修剪腹肉 / 灯检当「可控到可接受水平」；把标准冻结参数无条件套用于厚鱼

- **依据行号**：L4703–4708；L4681–4691；L4668–4679；L4698–4702。
- **错误做法**：其一，把「修剪腹肉 + 灯检物理挑虫」列为单独 CCP，认为挑完即达标；其二，把 L4681–4688 的三组冻结时温参数（-20°C/7 天、-35°C/15 小时、-35°C 至实心后 -20°C/24 小时）不加验证地套到特别大的鱼（厚于 6 英寸）身上。
- **为什么错 / 正确做法**：修剪与灯检「are effective methods for reducing the numbers of parasites. However, they do not completely eliminate the hazard, nor do they minimize it to an acceptable level」—— 只是减量，与 X-09 同属「不能单独达标」。冻结有效性取决于温度、冻结所需时长、保持时长、鱼种与来源、寄生虫种类（L4668–4679），且明文 `Note that these conditions may not be suitable for freezing particularly large fish (e.g., thicker than 6 inches)`。正确做法：对大鱼 / 厚切须单独验证冻结曲线与保持时间，不能照抄表格参数。
- **归属边界建议**：**控制有效性** —— B 段「物理减量不达标」与「标准参数有适用边界，须验证」两条并列。

> Trimming away the belly flaps of fish or candling and physically removing parasites are effective methods for reducing the numbers of parasites. However, they do not completely eliminate the hazard, nor do they minimize it to an acceptable level.
> 〔L4703–4708〕

> Note that these conditions may not be suitable for freezing particularly large fish (e.g., thicker than 6 inches).
> 〔L4689–4691；`these conditions` 指 L4681–4688 的三组冻结时温参数〕

---

## X-11 以为「加热工艺足以杀寄生虫」就等于本指南涵盖 retorting / LACF 热杀菌

- **依据行号**：L4654–4667；L182–189；L4660；L19770–19798。
- **错误做法**：读到「加热到足以杀细菌病原体也足以杀寄生虫」后，把本指南的烹饪 / 巴氏杀菌建议直接用于低酸罐头 retorting，或据此认为指南已覆盖 21 CFR 113 的强制热杀菌工艺、可以只按指南设计而不引 LACF 法规。
- **为什么错 / 正确做法**：该句的真实作用域是 Ch.13（热熏）与 Ch.16（烹饪 / 巴氏杀菌）针对细菌病原体的工艺；指南随即把 retorting 的法规要求指向 21 CFR 113（LACF Regulation），并明确「This guidance does not provide further information on retorting」，Ch.1 又重申本指南「does not cover」LACF / 货架稳定酸化食品中的 *C. botulinum*，其「Mandatory controls」在 21 CFR 113。正确做法：把「足以杀寄生虫」这一伴随效应与「retorting 的法定工艺设计」分开，后者须回引官方法规，不可由指南代劳。
- **归属边界建议**：**控制有效性**（兼 **范围**）—— B 段「伴随效应 ≠ 工艺被本指南覆盖」条。

> The process of heating raw fish sufficiently to kill bacterial pathogens is also sufficient to kill parasites. Guidance concerning cooking and pasteurizing to kill bacterial pathogens is provided in Chapters 13 (hot smoking) and 16 (cooking and pasteurization). Regulatory requirements for retorting (i.e., thermal processing of low acid canned foods) are contained in the Thermally Processed Low-Acid Foods Packaged in Hermetically Sealed Containers regulation, 21 CFR 113 (hereinafter, the Low-Acid Canned Foods (LACF) Regulation). This guidance does not provide further information on retorting.
> 〔L4654–4667〕

---

## X-12 把本指南用于它明确不覆盖 / 非权威的对象：消费者与零售端、可接受市场名称、濒危物种限制、法规转录法源

- **依据行号**：L89–99（含 L92–95）；L2135–2143（含 L2139–2140）；L2144–2156；L1379–1387、L1422–1429、L1451–1457（L1457「codified portion … included in Appendix 8」）；L28210–28218；L29626–29641（Addendum 1 内 `PART 123` / `§ 123.6` 转录）；L27450–27462。
- **错误做法**：① 用本指南去规定 / 判定消费者或零售企业的安全操作；② 用本指南判定鱼类「可接受市场名称」（acceptable names）；③ 用本指南处理濒危物种 / ESA 限制；④ 把附录里转录的 21 CFR 123 全文（Appendix 8 → Addendum 1）或 Appendix 5 的法规数值，当成可独立引用的法源，直接以「本指南附录第 X 条」作为合规依据。
- **为什么错 / 正确做法**：① 指南「does not specifically address safe handling practices by consumers or by retail establishments」，只面向加工者并供监管者评估 HACCP 计划；② 明文「This Guide is not the official resource for determination of acceptable names」，权威来源是 `The Seafood List`；③ 濒危物种信息指向 NOAA「ESA Threatened & Endangered」list 与 U.S. Fish & Wildlife Services，指南只是转指，不是判定依据（L2144–2156 为带链接的 NOTE，按口径不逐字引用）；④ 指南自陈「The codified portion of the regulations is included in Appendix 8」，但改动记录又说明因结构调整，该附录内容「has been permanently relocated to Addendum 1」—— 这本身证明附录内只是法规的**转录副本**，且位置在版本间变动，法源应回引 CFR 官方文本（21 CFR 123 / 113 / 1240.60），不可把指南转录当独立法源。注意 L1457（正文仍称 Appendix 8）与 L28215（已迁 Addendum 1）的内部不一致，也说明不能凭指南内部位置引用。
- **归属边界建议**：**范围** —— B 段「适用对象 / 权威来源 / 法源层级」四条并列，是范围类的总纲。

> The guidance does not specifically address safe handling practices by consumers or by retail establishments, although many of the concepts contained in this guidance are applicable to both.
> 〔L92–95〕

> This Guide is not the official resource for determination of acceptable names.
> 〔L2139–2140〕

> Due to the updated structure of the Fish and Fishery Products Hazards and Controls Guidance document and to ensure ease of access, the information from this Appendix has been permanently relocated to Addendum 1: Regulations - Fish and Fishery Products (Part 123) and Control of Communicable Diseases (Part 1240.60).
> 〔L28212–28216〕

---

## X-13 忽视版本与导出文本陷阱：封面 June 2022 / 章节页脚 June 2021、Appendix 3 残表、表格列头连写

- **依据行号**：L1–23、L52、L77、L147（封面 / 前言页脚「June 2022 Edition」）；L2160、L25886、L27452、L28218（章节 / 附录页脚「June 2021」）；L1379–1382、L1390、L1397、L1405、L1412、L1418、L1425（各附录「as of June 2021 / August 2019」修改记录）；L25884–25904（Appendix 3 CCP 判定树）；L25888–25902（残表）；L2172–2181（Table 3-1）、L2185–2213（Table 3-2 列头与字符丢失）；L2159–2163（页脚插入正文句子）；L27608–27620（Appendix 5 脚注混入）。
- **错误做法**：① 把导出件当成「整份文档统一为 June 2022」，忽略多章 / 多附录页脚仍是 June 2021，从而在引用时误标版本或误判某章的修订时点；② 据 L25888–25902 的 Q1 / Q2 / Q3 与错位表格，逐字复原 Appendix 3 的 CCP 判定树并当作可引用决策工具；③ 把 L2185–2205 连写的列头（如 `Parasite3HazardsCHP5`、`MARKETNAMES`、`AMBERJACKAMBERJACKAMBERJACK`、`ANCHOVY.12…`、字符丢失 `PuferfshPoisoning` / `mystcetus`）当成规范字段值或物种名照抄。
- **为什么错 / 正确做法**：本导出件是 PDF 转 Markdown 的产物，存在三类结构性缺陷：**版本标识分层**（封面 / 前言为 June 2022，章节与附录页脚多为 June 2021，附录修改记录又标 June 2021 / August 2019）；**图形塌陷**（Appendix 3 的 CCP 判定树在导出件里退化为 `Q1 / Q2 / Q3` 加残表，文字与「YES NO Modify this step」错位，已非可逐字复原的原图）；**表格字符损坏**（列头连写、重复词、斜体标记残留、拼写丢失）。正确做法：引用版本时区分「文档版次（June 2022 第 4 版）」与「章节页脚日期」；Appendix 3 判定树与 Ch.3 表格只作结构参考，须回原版 PDF 核对，不据导出文本逐字复原；把页脚 / 残表 / 连写列头视为「不可引用区」。
- **引用说明**：页码、页眉、残表、表格一律不作逐字引用，仅在上列行号中定位并描述；下列两块只引用散文段落用于锚定「版次」与「 June 2021 修改记录」的对照。
- **归属边界建议**：**版本文本** —— B 段「导出件不是权威版式 / 不可逐字复原」条，提醒能力卡不要以本导出件的表格与判定树为逐字依据。

> This is the fourth edition of the Food and Drug Administration's (FDA's) "Fish and Fishery Products Hazards and Controls Guidance."
> 〔L1444–1446〕

> Appendix 8: "Procedures for Safe and Sanitary Processing and Importing of Fish and Fishery Products" has been modified with the following recommendations as of June 2021.
> 〔L1379–1382〕

---

## X-14 把 Ch.7 / Ch.12 / Ch.13 里「某做法不足以控制」的明文警告读反

- **依据行号**：L6679–6694（Ch.7 组胺：`Once this enzyme is formed, control of the hazard is unlikely`、`may not effectively control`）；L16975–17002、L17014–17023（Ch.13 肉毒：`not adequate to weaken the spores`、`adequate salt levels are not usually achieved`、`not adequate to prevent toxin formation`）；L21106–21117（`refrigeration alone cannot be relied upon`）；L16625–16642（`does not ensure the maintenance of these temperatures`）；L19786–19798（干燥 `is not designed to result in … 0.85 or below`）；L27618。
- **错误做法**：① 认为「上了船冷藏 / 时温控制」就能逆转已形成的组胺，或把这些参数当成也能控制腐败菌 / 分解；② 认为冷熏的热处理足以削弱 *C. botulinum* 芽孢、盐渍通常就达到足够水相盐、或熏制 / 烟熏鱼自带的抑菌组合足以防止 A 型及蛋白水解 B / F 型产毒；③ 认为「全程冷藏」本身即可作为 *C. botulinum* 的唯一屏障；④ 认为熏鱼的干燥工序能把水分活度降到 0.85 以下。
- **为什么错 / 正确做法**：这些都是章节里明文的否定式警告 —— 组胺一旦形成「control of the hazard is unlikely」，船上冷藏参数只针对 scombrotoxin formation、对其他腐败菌「may not effectively control」；冷熏「the heat applied … is not adequate to weaken the *C. botulinum* spores」，且「adequate salt levels are not usually achieved during brining」，熏制抑菌组合「are not adequate to prevent toxin formation」；零售 / 家用冰箱温度常高于 38°F(3.3°C)，故「refrigeration alone cannot be relied upon」；分销体系「does not ensure the maintenance of these temperatures」。正确做法：把「冷藏 / 盐 / 烟熏 / 干燥」当作须与其他屏障（严格 ≤40°F 冷藏、水相盐、TTI、冷冻标签、验证过的热处理等）组合的**条件性措施**，并在 HACCP 中按章节给出的充分条件逐项论证，不能单凭一项就宣称控制到位。
- **归属边界建议**：**控制有效性** —— B 段「单一屏障不足以控制」条，作为 Ch.7 / 12 / 13 具体危害章节的补充反例合集。

> The controls listed above for onboard chilling will prevent the rapid formation of the enzyme histidine decarboxylase. Once this enzyme is formed, control of the hazard is unlikely.
> 〔L6679–6683（Ch.7）〕

> This inhibition is important in cold-smoked fish because the heat applied during this process is not adequate to weaken the *C. botulinum* spores. Control of the temperature during the cold-smoking process to ensure survival of the spoilage organisms is, therefore, critical to the safety of the finished product.
> 〔L16979–16986（Ch.13）〕

> Surveys of retail display cases and home refrigerators indicate that temperatures above the minimum growth temperature of *C. botulinum* type E and non-proteolytic types B and F (38°F (3.3°C)) are not uncommon. Therefore, refrigeration alone cannot be relied upon for control of the *C. botulinum* hazard.
> 〔L21106–21112〕

---

## 覆盖率自查

**1）按任务 7 类逐项对照**

| 任务类别 | 给定行号 / 线索 | 承接反例 | 覆盖 |
| --- | --- | --- | --- |
| ① 控制手段无效类 | L4692–4697、L4703–4707、L4689–4691、L4654–4667 | X-09、X-10（冻结+修剪合并）、X-11 | 全覆盖 |
| ② 表格误用类 | L127–136、L2128–2134、L1709–1719、L1753–1760、L2157–2181 | X-04、X-05、X-06 | 全覆盖 |
| ③ 判定逻辑类 | L1718–1731、L1823–1827、L1813–1822、L1852–1854 | X-07、X-08、X-01（吸收 CCP 义务） | 全覆盖 |
| ④ 效力层级类 | L100–108、L115–126、L137–139、L121–126 | X-01、X-02、X-03 | 全覆盖 |
| ⑤ 范围类 | L92–95、L2139–2140、L2144–2156、Appendix 8 / Additional Document 法规转录 | X-12 | 全覆盖（4 子项合并 1 条） |
| ⑥ 版本与文本陷阱 | L2160、L25886、L27452、L25888–25902、L2185–2205、封面 June 2022 | X-13 | 全覆盖（3 子项合并 1 条） |
| ⑦ Ch.7 / Ch.12 / Ch.13 补充警告 | 章节内「某做法不足以控制」 | X-14 | 已补，给出 L6679–6694 / L16975–17023 / L21106–21117 / L16625–16642 / L19786–19798 行号 |

**2）阶段 0 两个防误读方向**
- 防「把指南当法规」：X-01（should≠shall）、X-02（示例 / Appendix 5 数值非法定）、X-03（指南非危害分析替代）、X-12（附录法规转录非独立法源）。
- 防「把 Part 123 法定义务当可选项」：X-01（must / 21 CFR 123.6(c)(2)、§123.7 / §123.8 记录义务、§123.6 控制必须入计划）、X-07（不得因「没出过事」把控制漏出 HACCP）、X-08（No 也须写理由）。

**3）合并与取舍说明**
- 第 1 类 4 条 → 3 条（冻结参数与修剪 / 灯检同属「减量 / 有适用边界」合并为 X-10）。
- 第 3 类 4 条 → X-07 + X-08 + X-01（「显著危害至少一个 CCP」并入 X-01 作为法定义务例证，避免与效力层级重复立条）。
- 第 4 类 L115–126 与 L121–126 同段，拆为「不可死守清单」（X-02）与「替代须科学论证」（X-02 同条内反向说明），不另立条。
- 第 5 类 4 项、第 6 类 3 项、第 7 类多项各合并为 1 条合集反例，以子项并列 + 多行号方式保留全部线索。
- 合计 14 条，落在目标 10–14 区间上限，未超。

**4）引用合规自查**
- 全部 `> ` 引用块均为散文段落，每段 ≤100 词，块内标行号（含章节点标注）。
- **未作逐字引用**的对象：Table 3-1（L2172–2181）、Table 3-2 连写列头与损坏字符（L2185–2213）、Appendix 3 CCP 判定树残表（L25888–25902）、各页脚页码（L2160、L25886、L27452、L28218、L2181、L2211）、封面 / 页眉标题行（L1–23）、Appendix 5 表格（L27454–27462）。这些仅在「依据行号」与字段文字中定位、描述。
- 特殊处理：L2160 页脚 `3 - 1 (June 2021).` 插入了 L2159–L2163 的正文句子，X-06 的引用按散文原句重建并显式注明「已剔除插入的页脚 L2160」；该现象同时作为版本文本证据登记在 X-13。
- 未改动包内其它任何文件；本文件为唯一产出。
