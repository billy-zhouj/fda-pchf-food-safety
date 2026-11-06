# Fish and Fishery Products Hazards and Controls Guidance (4th ed., June 2022) — 整书理解（阶段 0 产出）

> 本文档是 cangjie-skill 流水线**阶段 0** 对**第 15 类来源**的产出，是后续 extractor 与能力卡的全局上下文。
> 与包内既有 `BOOK_OVERVIEW.md`（第一来源：PCHF 行业指南）**并列**，不覆盖、不合并。
> 本来源属于 update/repair 增量补源：按仓颉惯例沿用既有 **single** 输出模式，产物仍落进 `.cangjie/capabilities`，不另起技能包。

## 基本信息

- **标题**：Fish and Fishery Products Hazards and Controls Guidance, June 2022 Edition（第 4 版，SGR 129）
- **作者**：U.S. FDA / HHS / PHS / CFSAN / Office of Food Safety, Division of Seafood Safety
- **出版时间**：June 2022（第 4 版）；正文部分章节页脚仍为 `June 2021`，附录 3 为 `A3-1 (June 2021)`，属**滚动更新、分章修订**
- **内容类型**：监管机构技术指南（实操手册 + 危害对照表 + 控制策略范例）
- **版本来源**：资料库节点 `XMsRyrFL0wM1hesg8X6K9u` 导出 `SeafoodHazardsGuide-CompleteDocument-June2022.md`；1,709,446 字节 / 31,321 行
- **处理时间**：2026-11-06

---

## 1. 结构（Structural）

### 类型

**监管技术指南 / 决策程序手册**。不是法规本身，也不是教学教材；它是 21 CFR Part 123（Seafood HACCP Regulation）与 21 CFR Part 1240 的**配套实施文件**，同时被 FDA 用作**检查员评估企业 HACCP 计划的工具**（L96–99）。

### 一句话主旨

> 把「某个具体鱼种 + 某种具体加工/包装/储运方式」映射到一组可能危害，用 18 步流程判定其中哪些「在无控制条件下合理可能发生」，再从多条可选控制策略中定出 CCP 与关键限值，最终形成一份可被 FDA 接受的 HACCP 计划——而这份指南本身不构成法定义务。

### 骨架（3–7 个一级论点及关系）

1. **合法性边界**：指南不设可强制执行的责任，`should` 只是建议；企业可另选控制策略，但须科学论证其充分性（L100–126）。
2. **危害识别起点**：Ch.3 的三张表（脊椎动物 Table 3-2 / 无脊椎动物 Table 3-3 / 工艺相关 Table 3-4）列出**潜在**危害；表**不得单独使用**，必须结合 Ch.4–21 与自身/外部专家判断（L127–136、L2128–2134）。
3. **显著性判定**：以 `reasonably likely to occur` 为唯一闸门，且必须在**无控制条件下**判断；逐步独立评估，Yes/No **都要**在工作表第 4 栏书面写理由（L1720–1731、L1774–1822）。
4. **控制策略与 CCP**：每个显著危害至少一个 CCP；同一危害常有多条控制策略示例，其 CCP 位置互不相同，用 Appendix 3 判定树定位（L1828–1870、L25884–25902）。
5. **分危害技术层**：Ch.4–21 每章固定四段式（Understand the Potential Hazard → Determine Whether Significant → Identify CCPs → Develop a Control Strategy），覆盖养殖区病原、寄生虫、天然毒素、组胺、环境化学污染物、甲基汞、水产药物、病原菌生长、肉毒毒素、干燥不足、金葡菌毒素、加热/巴氏存活、杀菌后引入、过敏原、金属、玻璃。
6. **事实查表层**：Appendix 1–12 提供工作表/计划表、流程图示例、CCP 判定树、病原菌生长与灭活参数、FDA/EPA 安全水平、生食鱼类俗名、Part 123 法规全文、过敏原交叉接触与清洁、批准/未批准水产药物。
7. **法规正文附带**：Additional Document 1（21 CFR Part 123 与 1240 全文）、Additional Document 2（21 CFR Part 117 Subpart B）——导出件把这些一起收进来了。

**论点关系**：层层递进 + 一处关键对比。1 是统领全书的「非强制」框架；2→3→4 是**判定链**（识别 → 显著性 → CCP）；5 是判定链在各危害上的**并列展开**；6 是支撑 5 的**事实底座**；7 是法源锚点。最需要与既有能力卡区分的对比是：**指南的"建议"层 vs Part 123 的"法定义务"层**。

### 作者要解决的核心问题

在 1995 年 Seafood HACCP Regulation（60 FR 65096，1997-12-18 生效，L149–157）只规定义务、不提供具体危害清单与判定方法的空白下，给加工者和检查员一套**可操作、可辩护、可复核**的共同语言：怎样证明「我考虑过这个危害，并且有理由把它纳入/不纳入 HACCP 计划」。

---

## 2. 解释（Interpretive）

### 关键术语（作者本人的用法）

| 术语 | 作者的定义（含出处） | 和常识用法的差异 |
|---|---|---|
| `reasonably likely to occur` | 〔21 CFR 123.6(a) 转引，L1780–1789〕`one for which a prudent processor would establish controls because experience, illness data, scientific reports, or other information provide a basis to conclude that there is a reasonable possibility that it will occur in the particular type of fish or fishery product being processed in the absence of those controls.` | 不是统计概率，是**规范性拟制**（谨慎加工者标准），且明确要求**在缺少控制措施的条件下**评估 |
| `significant hazard` | L1774–1779：把潜在危害收窄为 `significant or, in other words, "reasonably likely to occur"` | 与 PCHF 语境的 SAHCODH 不是同一个判定体系，不得互套 |
| `species-related hazard` / `process-related hazard` | L2107–2124：前者由**鱼种**决定（Table 3-2/3-3），后者由**成品形态 + 包装类型 + 储运方式**决定（Table 3-4） | 常识会把"工艺危害"理解成加工步骤本身；本指南指成品/包装/储运属性的组合 |
| `should` | L105–108：`The use of the word "should" in Agency guidance means that something is suggested or recommended, but not required.` | **术语级**的强制程度标记，读错就等于把指南当法规 |
| `control strategy example` | L1843–1847：`there are often more ways than one to control a hazard. CCP(s) for one control strategy example often differ from those of another example for the same hazard.` | 不是"标准答案模板"；换一条控制策略，CCP 位置就变 |
| `hazard analysis` vs `HACCP plan` | L1503–1506：有显著危害时**必须**有 HACCP 计划；L1534–1540：法规**不要求**危害分析书面化，但 FDA 期望书面化以便复核与再评估 | 法定义务强度不同，"没写危害分析"不等于违规，"没写 HACCP 计划"才违规 |
| `prudent processor` | L1782：判定 `reasonably likely to occur` 的拟人化基准 | 不是可测量的操作判据，是留给检查员与企业博弈的解释空间 |

### 核心命题（用自己的话）

1. 危害清单只是**起点**，不是判定结论；表 3-2/3-3/3-4 必须与 Ch.4–21 合用（L127–136、L2128–2134）。
2. 判断危害是否显著，要**先假设所有现有控制都不存在**；已有控制之所以有效，恰恰证明该危害"合理可能发生"，应纳入 HACCP 计划（L1720–1731）。
3. 显著性要**按每一个加工步骤分别**判；三种情形任一成立即为显著：该步引入至不安全水平 / 该步增长至不安全水平 / 他步显著但可在当前步预防消除降低（L1796–1808）。
4. 工作表第 3 栏的 `Yes`/`No` **都必须在第 4 栏写出理由**；填 `No` 的步骤可跳过 Steps 11–18，但理由本身就是检查时的抗辩材料（L1813–1822）。
5. 「某步显著」≠「必须在该步控制」；CCP 定位是独立的 Step 11，用判定树决定（L1823–1836）。
6. 每个显著危害**至少一个 CCP**，同一危害可有多个 CCP，同一步骤可同时是多个危害的 CCP（L1852–1859）。
7. 18 步流程（L1492–1615）从「描述食品/分销/预期用途/流程图」到「监控 What-How-Frequency-Who / 纠正措施 / 记录 / 验证」，把 HACCP 七大原理落成可填表格。
8. 关键限值可用其他值替代，但替代者须**科学论证其充分性**（L121–126）——这是指南给企业留的最大裁量口，也是最容易失控处。
9. 控制参数随危害而异且**不可互换**：寄生虫靠冻结（-20°C 7 天 / -35°C 15 小时 / -35°C 冻实后 -20°C 24 小时，L4681–4689），组胺靠时间-温度链，肉毒靠包装/盐相盐度/aw 屏障。
10. 盐渍、醋渍、柠檬汁腌渍**不能**消除寄生虫（L4692–4697：线虫幼虫在 21% 盐水中可存活 28 天）；修剪腹肉、灯检挑虫只能降低数量不能彻底去除（L4703–4707）。
11. 冻结参数对**特别大的鱼（厚于 6 英寸）可能不适用**（L4689–4691）。
12. 安全水平有**来源分层**：Appendix 5 的组胺 `≥ 500 ppm - toxic` / `≥ 50 ppm - decomposed` 引自 CPG Sec. 540.525（L27547），兽药残留引自 21 CFR 556 系列或 Import Tolerance，农药引自 40 CFR 180 系列，贝类弧菌引自 NSSP Guide（L27460–27549）——**不是 FDA 在本指南里新设的限值**。
13. 新出现/新出现的毒素关联、物种替换（species substitution）会造成危害被漏识别，指南明文要求加工者自行警觉（L137–144、L2157–2170）。
14. 指南同时服务监管评估：标准化表格虽非强制，但用它会**加快监管审查**（L1506–1510、L1528–1540）。

### 论证链

法规（21 CFR 123.6 要求危害分析 + HACCP 计划）→ 法规未给危害清单 → 用 Ch.3 表按鱼种/成品形态枚举**潜在**危害 → 用 Ch.4–21 的"理解危害"段给出发生条件与科学证据 → 用"判定显著性"段按无控制条件逐步筛选 → 用 CCP 判定树定位控制点 → 用"控制策略示例"给出关键限值与监控四问 → 用 Appendix 5 把限值回指到真正的法规/CPG/NSSP 出处 → 全书首尾用「非强制」声明把上述全部降级为**建议**。证据类型混合：流行病学数据、监管检查经验、微生物学文献（Appendix 4 的生长/灭活参数）、以及 FDA 既有合规政策指南。

---

## 3. 批判（Critical）★

### 作者的时代局限

- **版本标识与实际内容不同步**：封面为 `June 2022 Edition`，但 Ch.3 页脚是 `3 - 1 (June 2021)`（L2160）、Appendix 3 是 `A3-1 (June 2021)`（L25886）、Appendix 5 是 `A5-1 (June 2021)`（L27452）、Ch.19 书目为 `Bibliography_August 2019`（L24718）。这是**分章滚动修订**的产物，引用时必须写"第 4 版 June 2022，某章页脚仍为 June 2021"，不能笼统称"2022 年新规"。
- **附录 3 的判定树在导出件里已塌陷**：L25891–25902 的 Q1/Q2/Q3 与流程框被转成了语义不完整的 markdown 表格（`IscontrolatthisstepnecessaryforSafety?`）。**不可据此逐字复原判定树问答**，需回查 PDF 原版。
- 限值表是**外部文件快照**：CPG Sec. 540.525 / 555.300 / 575.100、21 CFR 556、40 CFR 180、NSSP Guide 都可能在 2022 之后被修订；指南自身也把"新出现危害"列为未覆盖项（L140–144）。
- 附录 8 与 Additional Document 1 收录的 Part 123 全文，与包内已收的 `source-cfr-part123-2025.md`（4–1–25 Edition）**版本口径不同**，引用法条时必须以包内已核的 CFR 正文为准，指南内的转录只作对照。

### 作者的立场盲点

- **主体限定为加工者与监管者**：L92–95 明言 `does not specifically address safe handling practices by consumers or by retail establishments`。零售/餐饮/消费者端不适用。
- **不管命名合规**：L2139–2140 `This Guide is not the official resource for determination of acceptable names`，指向 FDA Seafood List；濒危物种与 NOAA/USFWS 限制也外链（L2144–2156）。
- **不管低酸罐头杀菌**：L4666–4667 `This guidance does not provide further information on retorting`，转引 21 CFR 113（包内已有 `lacf-*`、`source-cfr-part113-2025.md` 负责）。
- **不管经济欺诈本身**：物种替换只在"会导致危害被漏识别"的意义上被提及（L2157–2170），不处理掺假/错误标签的法律定性。
- 作为监管方文件，它天然**以"能否被 FDA 接受"为成功标准**（L119–120），而非以企业成本、可操作性或中小微企业能力为标准。

### 未被证明的假设

- 假定加工者「有自己的专长或能找到外部专家」补表外危害（L1711–1714、L1756–1760、L2128–2134）——对小微企业是实质性门槛，但指南未论证其可得性。
- 假定 `prudent processor` 是一个可共享的判断基准（L1782），实际把自由裁量留给了检查员与企业的事后博弈；书面理由（Column 4）是唯一可审计的落点。
- 假定表格 + 章节足以覆盖具体厂区/设备/工艺（L1759–1760 又自我否认了这一点）。
- 假定「科学论证替代关键限值的充分性」（L124–126）在企业侧可执行，但未给论证的形式标准。

### 最强反对意见

> 既然指南自己承认不具强制力、允许任何替代控制策略、且明文「不替代危害分析」（L137–139），那么把 Ch.3 的勾选表、Appendix 5 的限值、控制策略示例里的关键限值**当成合规清单或法定义务**，恰恰是对 21 CFR 123.6 的危害分析义务的背离：企业照抄表而不做本厂判定，检查员照抄限值而不接受等效论证，双方都把"建议"误当成"要求"。

这条反对意见直接决定下游能力卡的 **Boundary (B)** 段：新卡必须同时防「把指南当法规」和「把法规义务当可选项」两个方向的误读。

---

## 4. 应用潜力（Applicability）

### 可 skill 化的内容

- [x] **18 步 HACCP 计划开发流程**（Ch.2 + Appendix 1）——决策程序
- [x] **`reasonably likely to occur` / 无控制条件下显著性三步判定**——决策框架，且是全书最反直觉、最易与 PCHF 危害分析混淆之处
- [x] **Ch.3 表 + Ch.4–21 联动的危害识别分流**（品种相关 vs 工艺相关，表不可单独用）——清单/框架
- [x] **CCP 判定树与多控制策略并存**（同一危害不同策略 CCP 不同）——决策程序
- [x] **「指南建议 / 法规强制 / 外部 CPG 限值」三层来源分野**——原则，直接对应既有卡的引用纪律
- [x] **具体控制参数链**：寄生虫冻结三条件与 6 英寸例外、盐渍无效；组胺 50/500 ppm；Appendix 4 病原菌生长/灭活参数；Appendix 5 安全水平回指链
- [x] **过敏原与金属/玻璃**（Ch.19–21、Appendix 9–10）——与包内 `allergen-program` 有接口但主体不同

### 不适合 skill 化的内容

- 附录 6 生食鱼类日/夏威夷俗名对照、附录 11/12 批准与未批准水产药物逐项清单、Appendix 5 数百行农药/兽药残留数值——**事实查表**，可作为卡的引用数据或 R 段证据，不独立成卡
- 各章 Bibliography、法规全文转录（附录 8 / Additional Document 1–2）——与包内已收来源重复
- 物种替换案例表 3-1 的具体逸闻——保留为 example

### 预估 skill 数量

**1 张**（最终由阶段 1.5 三重验证决定）。沿用包内 v4.9 每来源 1 卡的惯例，建议 `CAP-23 seafood-hazards-controls-guide`，importance 取 `extended`，与既有 `CAP-22 seafood-haccp-statutory-requirements`（法条层）构成**指南层 / 法条层**配对而非合并。

### 优先级排序（按"最能赋能使用者"）

1. 显著性判定的「无控制条件」口径 + Yes/No 都要写理由（与 PCHF `hazard-analysis-method` 的误混风险最高）
2. 指南非强制 vs Part 123 强制的边界，以及替代关键限值须科学论证
3. Ch.3 表不可单独用、须结合 Ch.4–21 与自身专长
4. 具体控制参数（寄生虫冻结、组胺、肉毒、Appendix 4/5）及其外部法源回指
5. CCP 判定树与多控制策略下的 CCP 位置漂移

---

## 5. 转换质量风险（影响逐字引文核对，必须记入审计）

导出件是 PDF/网页转 Markdown，**不是可信的逐字文本**：

- 表格列头连写：`MARKETNAMES`/`LATINNAMES`/`Parasite3HazardsCHP5`（L2187）、`iPotentalSpecies-RelatedHazards...`（L2174）
- 词条重复粘连：`ALFONSINOALFONSINO`、`AMBERJACKAMBERJACKAMBERJACK`、`ANCHOVY.12**ANCHOVY.12**`（L2191–2203）
- 字符丢失/替换：`fsh`→fish、`fnfsh`→finfish、`Pufer Fish`、`Tetrodotoxin (PuferfshPoisoning)`（L2177）、`Specifcations`、`Fluoroquinilones`（L27462）；开头有控制字符 `\x03`（L2 `Hazards \x03and Controls`）
- 页码与页眉混入正文：`3 - 2 (June 2021).` 被塞进表格单元格（L2181）、`A5 - 2 (June 2021)` 混入 TABLE A-5（L27468）
- 图形塌陷：Appendix 3 的 CCP 判定树（L25888–25902）Q1/Q2/Q3 与分支框变成不完整表格
- 章节标题层级错乱：`### Table 1-1`（L13199，应为 Table 11-2）、`### Ch11 - CS\_6`（L13637）、`### ° The adequacy of ice surrounding the`（L18513）被误判为 H2/H3

**结论**：新卡的 R 段英文引用块只能取自**散文段落**（如 L100–144、L1720–1731、L1780–1789、L4681–4697、L27547），且必须以包内 `verify_*_quotes.py` 的 `body_only()` 方式对源文件逐字校验；**表格、页码、页眉、CCP 判定树不得作为逐字引用来源**。建议落地源文件时保留原始导出件不改写，另建 QA 报告记录上述缺陷。

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 7 个一级论点
- [x] 关键术语词典 7 条（≥5）
- [x] 批判阶段列出 4 组局限（≥3）
- [ ] 已向用户展示并得到确认 ← **等待本轮确认，确认后才进入阶段 1（5 路并行提取）**

**用户确认时间**：待填
