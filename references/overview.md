# Hazard Analysis and Risk-Based Preventive Controls for Human Food — 整书理解 (阶段 0 产出)

> 本文档是 cangjie-skill 流水线的阶段 0 产出, 后续所有 extractor 和 skill 都以此为全局上下文。

> **来源与版本说明（v3.0，2026-11-05 追加）**：本文是**第一来源**（PCHF 行业指南）的阶段 0 整书理解，保留原始分析不重写。本技能包此后追加了两份来源：① 21 CFR Part 117（2025）法规正文，提供法定义务、法定例外与时限（卡内以〔§ 117.xxx〕标注）；② FDA《Control of Listeria monocytogenes in Ready-To-Eat Foods: Guidance for Industry》(Draft, 2017-01)，补齐 RTE 即食食品李斯特菌专项的卫生程序、环境监测、厂房工程、人员卫生、抑制型/致死型配方、储运与术语。三份来源合并后能力卡由 10 张扩展为 **13 张**（新增 environmental-engineering-controls、personnel-hygiene-controls、exemption-withdrawal-procedure），glossary 扩展至 100 条。三者的效力层级为：**法规正文（must）> 指南（should / we recommend）**；L.mono 指南正文中出现的 must 均为其引述 Part 117 的法定义务。本文以下章节的所有结论仍以第一来源为准，涉及法定义务时须以法规正文与对应能力卡为准。

> **来源与版本说明（v4.0，2026-11-05 追加）**：本次再追加第四来源——FDA《What You Need to Know About the FDA Regulation: 21 CFR Part 117 — Small Entity Compliance Guide》(**October 2016**, Docket FDA-2011-N-0920)，本地 `source-secg.md`。它是依 SBREFA § 212 编制的**非约束性白话版规则说明**，自己声明「不约束 FDA 或公众」「允许满足法规的替代方案」，因此**不构成义务来源**。合并后能力卡由 13 张扩展为 **14 张**（新增 `cgmp-compliance-guide`，CAP-14），glossary 106 条，测试用例 45 条。效力栈为四层：**Part 117 法规正文（must，唯一判定基准）> SECG（白话转述）> 专项行业指南（草案建议层）> CPG / Compliance Programs（检查视角）**；SECG 章号与〔§ 117.xxx〕分列标注，不得混引。本文以下章节仍以第一来源为准，涉及 cGMP 合规判定与资料分层时以 `cgmp-compliance-guide` 卡为准。

## 基本信息

- **标题**: Hazard Analysis and Risk-Based Preventive Controls for Human Food: Guidance for Industry (Full Guidance, Draft)
- **作者**: U.S. FDA, CFSAN Office of Food Safety（美国食品药品监督管理局食品安全与应用营养中心）
- **出版/发布时间**: 正文封面 2024 年 1 月草案（滚动发布；源文件名标注 October 2026）；引用数据截至 2016–2022 年
- **内容类型**: 实操手册（法规实施指南，Draft – Not for Implementation，含非约束性建议）
- **版本来源**: books/fda-pchf-human-food-guidance/source.md（资料库导出，1.66MB / 19461 行）
- **处理时间**: 2026-11-04
- **章节状态**: 已发布 Ch1–6、11、12、14、15、16 + 附录 1–3；Ch7（时间/温度）、8（配方/干燥）、9（过程验证）、10（卫生程序）、13（物理危害控制）、17（RTE 分类）为 "Coming Soon" 占位

> **第二来源（2026-11-04 增量并入）**：21 CFR Part 117（2025 版）法规正文（Subparts A–G 全量条文，160KB / 3577 行，来源 books/_inbox/21-CFR-Part-117-2025.md）。它是本指南所解释的法规本体（**v4.14 起该文件已随仓库分发**；此前仅声明路径、仓库内无文件，故〔§ 117.xxx〕引文当时无法本地复核），**为最终规则、具法律约束力**，与指南草案的 should 级建议形成权威分层。本文档描述的骨架、术语、批判均以指南为对象；能力卡中标注〔§ 117.xxx〕的内容来自法规正文，负责提供法定义务、法定例外、硬时限与豁免门槛的权威出处。两者冲突时以法规为准。

---

## 1. 结构 (Structural)

### 类型
监管实操手册（regulatory guidance）——把 21 CFR Part 117（PCHF）的法律要求翻译成企业可执行的程序、决策表、工作表和完整示例。

### 一句话主旨
食品设施通过"书面危害分析 → 判定需预防控制的危害 → 对每个危害实施预防控制并配套监控/纠正/验证管理组件"的循环框架，建立、实施并持续再分析一份由 PCQI 负责的食品安全计划（FSP）。

### 骨架 (主要论点及其关系)

1. **法律底座**：PCHF 落实 FSMA 第 418 条，适用于需注册设施；FSP 必须书面、由 PCQI 编制、签署、至少每 3 年再分析；危害分析无论结论如何都必须书面。（Ch1 + Introduction）
2. **危害分析六列工作表方法**（全书的方法论核心）：前期步骤（小组/产品描述/现场核实的流程图）→ 识别（10 类 NACMCF 问题清单 + 潜在危害表）→ 评估（严重性 × 概率 + 117.130(c)(2) 十类因素 + RTE 环境病原强制项）→ 控制识别（每个"Yes"危害至少一个预防控制，可行时定 CCP；"No" 的理由与 "Yes" 同等重要）。（Ch2）
3. **危害知识库**：三类危害（生物/化学/物理）× 四类来源（原料/工艺/设施/人员）的识别矩阵 + 湿/干环境二分法（湿→李斯特菌，干→沙门氏菌）+ 附录 1 的 16 食品组分层危害表（X 标记 ≠ 需要控制）。（Ch3 + Appendix 1）
4. **五类预防控制**：工艺控制（process control，致死处理/时间温度/配方 a_w、pH/脱水/物理排除）、过敏原控制（防交叉接触 + 标签）、卫生控制（接触面清洁 + 卫生分区）、供应链控制（批准供应商 + 验证活动）、召回计划（四要素）。（Ch4–5、6、11、12、14、15、16）
5. **管理组件闭环**：监控四问（What/How/How often/Who）→ correction vs corrective action 的判定边界（问题是否已影响食品、孤立 vs 反复）→ 验证（validation 确认 + 日常 verification）→ 记录（可用 exception records）→ 再分析触发。（Ch5 贯穿全书）
6. **示例驱动的可复制性**：5 个热处理完整示例（批式/连续 × 固体/液体 × 酸化）、2 个过敏原程序完整示例、2 个婴儿食品毒元素示例、3 个 DON 条件性升格示例——每个都走完"危害→关键限值→监控→纠正→验证→记录→汇总表"全闭环。（Ch6、11、12）
7. **例外与豁免体系**：qualified facility、LACF/酸化食品双法规、USDA FSIS 管辖、极强致死工艺、研究用途食品、临时供应商——判断"哪些规则对我适用"与规则本身同等重要。

**论点之间的关系**: 递进 + 层层深入：1→2 是"要做什么"的法律与方法框架；3 为 2 提供识别素材；4 是 2 的输出端（怎么控）；5 是 4 的运行保障（怎么管）；6 把 2–5 串成可照抄的实例；7 是全书的边界条件层。

### 作者要解决的核心问题
如何让一家食品设施（尤其是没有 HACCP 深厚积累的中小设施）从零开始，做出一份经得起 FDA 检查的、科学有效且持续维护的食品安全计划——而不是一份"纸面合规"文件。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| hazard（危害） | 仅指能致人生病或受伤的生物/化学（含放射）/物理因子 | 虫害、毛发、腐败等质量缺陷**不是** hazard |
| potential hazard | "known or reasonably foreseeable hazard"的同义词，附录表中 X 标记者 | 只是"建议评估的起点"，绝不等于需要控制 |
| hazard requiring a preventive control | 知情者基于危害分析（严重性+概率）会建立预防控制来显著减小/预防的危害 | 三个层级的顶层，判定责任在每个工厂 |
| preventive control | 基于风险、与科学认知一致的程序/实践/过程；可应用于 CCP 也可应用于非 CCP | 比 HACCP 的"CCP 控制"宽：卫生、过敏原、供应商控制都算 |
| FSP (Food Safety Plan) | 书面危害分析+预防控制+管理组件+召回计划（如适用）的文档集 | 无标准化格式；可以是文档集合；未识别出需控危害时可以只有危害分析一份 |
| PCQI | 完成 FSPCA 标准课程或凭工作经验具备能力者；FSP 及验证等须由其编制/监督 | 无须是本厂员工；不等于 HACCP 时代的"质量经理" |
| critical limit vs operating limit | 关键限值=食品安全红线；操作限=更严格、基于非食品安全（质量）原因的内控线 | 偏离操作限只需 "adjustment"，偏离关键限才触发纠正措施 |
| correction vs corrective action | correction=及时纠正轻微、孤立、未影响产品安全的问题；corrective action=四步完整程序（纠正/防复发/评估受影响食品/阻止入市） | 以"问题是否已影响食品"和"孤立 vs 反复"为判定边界，correction 可不记录 |
| validation vs verification | validation=用科学/技术证据确认控制措施有效；verification=监控之外的核查（校准、记录审查、产品检测、环境监测） | 过敏原控制、卫生控制、召回计划、供应链计划**不需要** validation |
| environmental pathogen | 能在环境中存活并持续存在从而污染食品的病原（L. mono、Salmonella）；**不包括致病孢子形成菌的孢子** | 定义排除孢子影响环境监测义务的适用 |
| transient vs resident (strain) | 瞬时污染=常规清洁可控制；定殖(resident)=病原藏匿于 niche 持续数月至数年，需强化卫生程序根除 | 对 resident 菌，常规 SSOP 无效——这是环境监测法定化的原因 |
| SAHCODH hazard | 暴露后有合理可能性导致严重健康后果或死亡的危害（对应 Class I 召回） | 触发供应链"首次使用前+每年现场审核"的硬要求 |
| supply-chain-applied control | 在原料接收**之前**对该原料危害实施的预防控制 | 只有收货设施能批准供应商；供应商不能自审、自证 |
| approved supplier | 满足供应链计划标准、正在控制所识别危害并获批准的供应商 | 从经纪商/分销商采购时，供应商是实际制造者而非中间商 |
| lethality treatment vs non-lethality treatment | 前者杀灭/失活（营养细胞 kill、孢子 inactivate）；后者抑制生长（时间温度、配方、干燥） | 热处理只杀营养细胞不灭孢子；不能消除已形成的毒素 |
| EPIPT | 经研究确立后，用"终点内部产品温度"替代全程时间-温度监控 | 有三前提：热分布研究+热穿透研究+识别其他关键因素 |
| exception record | 仅在失控时才建立的监控记录 | 允许"只记异常"，大幅降低记录负担 |
| a_w / pH 4.6 / 0.85 | a_w≤0.85 病原不能生长（S. aureus 界限）；pH≤4.6 排除 C. botulinum；0.92 抑制孢子萌发 | 数值是判据不是玄学；多组分界面微环境可推翻单组分判断 |
| D value / z value / 6D | D=90% 递减时间；z=D 值降 10 倍所需温度；6D=百万倍减少（L. mono 70°C 2 分钟；非蛋白分解 C. botulinum 90°C 10 分钟） | 技术上不可能降到零 |
| ROP（减氧包装） | 抑制腐败延长货架期的包装；无 C. botulinum 屏障不得使用 | "可能先产毒后腐败"——无感官警讯 |

### 核心命题 (用自己的话)

1. 危害分析做错或漏识别，则整个 FSP 无效——无论工厂执行得多好。危害分析是全体系的阿基米德支点。
2. 危害必须书面判定"Yes/No"，且解释"No"与解释"Yes"同等重要——书面理由是对抗检查质疑的防线。
3. 控制措施可以放在识别出危害的步骤之外（列 6），关键是"在哪里控制最有效"而非"在哪里发现"。
4. 只要 RTE 食品在包装前暴露于环境且包装后无致死处理，环境病原评估就是强制项（117.130(c)(1)(ii)）——没有商量余地。
5. 控制程度存在技术上限：不可能降到零；热处理只杀营养细胞、不灭孢子、不消除已形成的毒素（S. aureus / B. cereus）。
6. 湿/干环境二分法决定环境病原控制战略：湿区防李斯特菌靠"保持干燥"，干区防沙门氏菌靠"严格控水"。
7. 监控只是记录并不能保证安全：发现偏差时应假定自上次合格检查起全部未受控；校准频次低会使更多产品面临风险。
8. correction 与 corrective action 的边界不是主观判断，而是"问题是否已影响食品"+"孤立还是反复"；反复出现=程序无效=触发再分析。
9. 检测只能作为其他供应商验证活动的补充，永远不能是唯一手段（分布不均匀性使抽样天然有漏检风险）。
10. 供应链控制的本质是"把控制前移到接收之前"，其严谨度与危害的 SAHCODH 属性挂钩：SAHCODH 危害=首次使用前+每年现场审核，除非 PCQI 书面认定替代方案。
11. FSP 是动态文件：至少每 3 年再分析；变更、新危害信息、意外问题、控制无效都会触发（可限于相关部分）。
12. 附录 1 的 X 标记只是 SME 建议评估的起点；判定责任永远在每个工厂——"照表抄控制"会过度，"不看表"会违规。
13. 危害分析结论不是一劳永逸：DON 案例链（Miller C→Baker D→Sandwich F）展示"条件性升格"——季节性信息恶化时，原本不是预防控制的操作要升格为预防控制并加大验证。
14. 双法规体系（酸化食品 108.25/part 114 与 PCHF）可双向借用程序与记录满足对应要求，但专项超出部分（3 年记录、容器编码、Form 2541e 提交）不可免除。
15. "May contain" 类咨询声明不能替代 CGMP 或预防控制；使用需 PCQI 书面论证，且供应商声明需做"传递/不传递/阈值论证"三选一决定。

### 论证链
法律条款（21 CFR 117）→ 指南把它拆解为可操作的程序与决策表（六列工作表、监控四问、纠正措施四要素、供应链 18 项记录）→ 用科学数据（D/z 值、6D 表、a_w/pH 界限、生长极限表）支撑关键限值 → 用 12+ 个完整示例厂（Cookie A/B、Soup A/B、Salsa A、Dessert A、Bakery B、Manufacturer A/B、Miller C、Baker D、Sandwich F）演示闭环 → 用暴发史（巧克力、花生酱、焦糖苹果、肉桂苹果酱等）证明危害的现实性 → 用例外体系（豁免、双法规、极强致死工艺）划定适用边界。证据类型：法规条文 + 定量微生物学数据 + 暴发/召回流行病学 + 示例推演。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- **滚动发布的"半成品"**：Ch7/8/9/10/13/17 仍是占位，全书对时间/温度控制、配方控制、验证方法学、卫生程序、物理危害控制只有概述级内容——按本指南无法完整建立这些控制的细节。
- **引用数据滞后**：辐照批准用途"截至 2016 年 4 月"、过敏原阈值数据 2021–2022、附录 1 数据截至 2022；Closer to Zero 行动水平仍在迭代；定稿章节内容还会变。
- **文件为草案**："Draft – Not for Implementation"，多处脚注自认定稿时会调整（如 2016 年 Ch2/3 定稿顺序调整、Table 5 拟纳入更多进口警报）。

### 作者的立场盲点
- **监管者视角**：默认企业能负担 PCQI、process authority、qualified auditor、第三方审核、实验室检测——对极小企业这些成本被轻描淡写（仅靠"qualified facility 替代验证"缓解）。
- **美国中心**：全部建立在 FD&C Act、21 CFR、USDA 体系之上；对中国读者需自行映射到 GB 14881、GB 31654 等体系，监管逻辑（以记录和书面判定为核心的检查式合规）与 HACCP 认证体系亦有差异。
- **以"致病/致伤"定义危害**：质量、欺诈（除 EMA 外）、可持续性等企业真实关切被排除在外；过敏原阈值决策依赖企业自证"科学有效确定"，监管不确定性由企业承担。

### 未被证明的假设
- 假设"书面判定"能忠实反映真实风险——但危害分析质量高度依赖 PCQI 个人水平，指南无法保证这一点。
- 假设环境监测、抽样检测等工具在统计上有效——指南自己也承认分布不均匀性、检测灵敏度、模型偏差（迟滞期）会击穿这些工具，却仍把它们作为体系支柱。
- 假设 3 年再分析周期足够捕捉新危害（如 2023 肉桂苹果酱铅事件是靠儿童血铅异常才发现的，不是靠任何设施的再分析）。
- Table 3-A 生长极限来自文献极端值与实验室培养基，FDA 自己承认"未必适用于具体食品"，但使用者常直接当设计依据。

### 最强反对意见
这套体系的合规成本与风险削减不成比例：它把巨量资源投在"写文件、做记录、应付检查"上，而历史上真正的暴发（花生酱、巧克力、焦糖苹果）恰恰发生在"文件齐全"的企业——书面体系创造了虚假安全感。同时，X 标记表 + 十类评估因素 + 十八项供应链记录的组合让中小设施实际上只能请顾问代写 FSP，合规变成付费门槛而非能力建设。FDA 用"非约束性建议"的措辞回避了这一点，但 PCQI 签名与检查现实使它事实上强制。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] **六列危害分析方法**（前期步骤→识别 10 类问题→评估两维度+强制项→控制识别 7 项考虑）——完整决策程序，Ch2 + Form 2-B
- [x] **"是否需要预防控制"的三条判定标准 + 117.130(c)(2) 十类评估因素**——可迁移的判定框架
- [x] **correction vs corrective action 判定**（四要素程序 + "是否影响食品/孤立 vs 反复"边界）——高频决策点
- [x] **热处理（致死步骤）设计与验证三步法** + EPIPT 三前提 + 6D 目标查表（Table 3-D/3-E）——工艺控制核心
- [x] **湿/干环境二分法与环境病原控制战略**（卫生分区、清洁策略三选择、环境监测触发）——Ch3/4 精华
- [x] **过敏原程序三支柱**（CGMP 措施→交叉接触控制+标签控制→供应链）+ 咨询声明三选一决定 + 排产/"like into like" 规则
- [x] **化学危害归途判定**（CGMP vs 预防控制四因素；供应链/工艺控制/配方管理/物理分选的分流）+ 婴幼儿食品毒元素供应链控制
- [x] **供应链验证活动选择**（四种活动、批准 4 因素、SAHCODH 年审规则、三类替代验证、供应商不符合处置）+ 18 项记录清单
- [x] **ROP 肉毒屏障判定**（五屏障）与**多组分界面/过程后添加配料/冷却陷阱**等工艺危害陷阱清单
- [x] **召回计划四程序 + 书面通讯 6 要素 + RFR 24 小时规则**
- [x] **附录 1 分层危害表使用法**（16 食品组→X 标记→三种适用性检验→判定路径）与附录 3 生长/灭活速查
- [x] **FSP 与 HACCP 的差异映射**（Table 1-1）——存量 HACCP 企业升级路径
- [x] **条件性升格逻辑**（DON 案例链）——危害分析的动态维护
- [x] **酸化食品双法规对照**（108.25/part 114 ↔ PCHF 双向借用 + 专项不可免清单）

### 不适合 skill 化的内容
- 病原体年病例数、暴发史细节（作为 skill 的 example 素材保留）
- FDA/USDA/Codex 资源表与参考文献（作为工具引用保留在能力卡 B/E 段）
- 法定术语的逐字定义（117.3 原文）——保留在术语词典
- 缩写表、表单填写格式的排版细节

### 预估 skill 数量
**约 6–9 个**（最终由阶段 1.5 三重验证决定）：危害分析方法 / 预防控制体系设计（含管理组件闭环）/ 热处理与过程验证 / 环境病原与卫生控制 / 过敏原程序 / 化学危害与供应链控制 / 召回计划 / 危害速查工具（附录 1+3）。

### 优先级排序 (按"最能赋能普通人"的角度)
1. 危害分析六列方法（一切的地基，独立价值最高）
2. 预防控制管理组件闭环（监控四问/纠正判定/验证/记录——跨行业可迁移）
3. 供应链验证决策（采购与供应商管理的通用框架）
4. 过敏原程序（跨境食品电商/代工厂高频踩坑区）
5. 热处理设计与验证（工艺研发场景）
6. 环境病原控制战略（湿/干二分法）
7. 召回计划（危机预案模板）
8. 危害速查（附录工具）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 3–7 个一级论点（7 个）
- [x] 关键术语词典 ≥5 条（18 条）
- [x] 批判阶段列出 ≥3 条作者局限（4 组共 11 条）
- [ ] 已向用户展示并得到确认

**用户确认时间**: （待确认）

---

### 附：分块阅读笔记索引（审计轨迹）

- candidates/_stage0/notes-1.md — Introduction/术语表/Ch1 FSP/Ch2 危害分析/Ch3 前半（第 1–3300 行）
- candidates/_stage0/notes-2.md — Ch3 后半/Ch4 预防控制/Ch5 管理组件/Ch6 前半（第 3301–6600 行）
- candidates/_stage0/notes-3.md — Ch6 后半+5 个热处理示例/Ch11 过敏原程序主体（第 6601–9900 行）
- candidates/_stage0/notes-4.md — Ch11 尾部+2 个过敏原示例/Ch12 化学危害控制（第 9901–13200 行）
- candidates/_stage0/notes-5.md — Ch12 尾部+DON 案例/Ch14 召回/Ch15 供应链/Ch16 酸化食品（第 13201–16500 行）
- candidates/_stage0/notes-6.md — 附录 1 危害表 1A–1P、2B–2P/附录 2 表单/附录 3 生长灭活数据（第 16501–19461 行）


## 版本补充说明（v4.2，第五来源）
本包另纳入 FDA《Questions and Answers Regarding Food Allergens ... (Edition 5): Guidance for Industry》**2025 年 1 月修订终版**（Docket FDA-2022-D-0099；90 FR 1133），全文见 `source-allergen-ed5.md`。该指南解释 FD&C Act § 201(qq)/§ 403(w) 的**过敏原标签**义务，与 21 CFR Part 117 的过敏原预防控制分属两套法源：Big 9 类别未变，但树坚果以 Table 1 的 12 种封闭清单为准，milk/eggs 的物种范围扩展，allergen-free 声明与 advisory 声明不得同现。引用须用 Ed.5 问答编号（C.1、C.8、D.13），不得标成〔§ 117.xxx〕；标签清单收窄不等于厂内危害分析可免控。


## 版本补充说明（v4.3，第六来源）
本包另纳入 FDA《Food Defect Levels Handbook》网页正文（页面标注 09/07/2018），全文见 `source-defect-levels-handbook.md`，对应能力卡 `defect-action-levels`。它给的是**缺陷行动水平阈值出处**（111 个产品、术语表、DEFECT SOURCE / SIGNIFICANCE），属 FDA 依 FD&C Act § 402(a)(3) 的执法裁量参考，**不是法规上限、不是平均值、不是放行标准**；法定义务在〔§ 117.110(a)〕`lowest level currently feasible`、〔§ 117.110(b)〕掺混稀释禁令与〔§ 117.80(b)(3)(4)〕。⚠ **v4.7 纠错**：本段当时写「`21 CFR 110.110` 已过时、Part 110 于 2018-09-17 移除」，**该结论不成立**。2015-09-17 PCHF 最终规则的 amendatory instruction 13 原拟于 2018-09-17 删除 part 110，但 FDA 2018-09-12 最终规则（FR Doc. 2018-19855）已撤回该指令，eCFR 现行版 Part 110 仍列 11 个 sections（含 §110.110），§114.5 并列 `parts 110 and 117` 也是现行文本。正确处理是「**现行仍有效、但正文本包未收 → 转引未收**」；手册那句是 §110.110(c) 意译，**仍不得标成〔§ 117.110(c)〕**（Part 117 的 §117.110 只有 (a)(b) 两款），但理由是「那是 part 110 的 (c) 款」而非「part 110 已删」。Part 117 侧法定义务仍回〔§ 117.110〕，并以「Handbook 章名 + 产品名」标注手册原文，不与〔§ 117.xxx〕混引。完整事实链见 `source-cfr-part114-2025.md` 文件头与 CAP-20 B2。


## 版本补充说明（v4.4，第七来源）
本包另纳入 FDA **CPGM 7303.040《Preventive Controls and Sanitary Human Food Operations》现行版**（`2025-CPM-HFP-001`，签发 08/29/2025，IMPLEMENTATION DATE 05/23/2024，50 页 / 91 书签），全文见 `source-cpgm-7303-040-2025.md`；2020-10-15 的 `2020-CPGM-CFSAN-003` 另存为 `source-cpgm-7303-040-2020.md`，**已废止、仅供版本对照**。CPGM 是 FDA 给检查员/分部的**内部作业指导**，非法规、非 Guidance for Industry、不创设企业义务；引用用「CPGM 7303.040 PART x」，合规结论仍回〔§ 117.xxx〕。对应能力卡 `inspection-readiness`：8 类检查与 PAC 码、Limited Scope / Full Scope / Focused PCHF 取证深度与转换、〔§ 117.320〕official review 与〔§ 117.315(c)〕FSP 现场 / 24 小时记录举证矩阵、483 回复 15 个工作日骨架、eNSpect 观察项与 OAI/VAI/NAI 三层分级、OAI 后 6 个月跟进检查。注意现行版把 critical/major/minor 挂在**整次检查**上（单条观察项只有 major/minor），`03040U` 已改为 Focused PCHF；FDA 网页列表日期与 PDF 首页 IMPLEMENTATION DATE 不一致，以 PDF 首页为准。IOM / RPM / CPG 全套 / 其他 Compliance Programs / AOAC-MPM 方法正文仍未纳入。


## 版本补充说明（v4.5，第八与第九来源：迎检链补齐）
本包再纳入两份**检查员侧内部文件**，与 v4.4 的 CPGM 7303.040 共同构成完整的迎检链。两份都是 FDA 给检查员/调查员/分部/实验室的**内部作业指导**，非法规、非 Guidance for Industry、不创设企业义务；合规结论仍回〔§ 117.xxx〕与 FD&C Act。

**第八来源 — FDA CP 7303.050《Sampling for Foodborne Biological Hazards and Filth – Domestic and Import》**（62 页 / 75 书签，官方 508-Compliant PDF 经 `pdf2md-pro` 转换，全文见 `source-cp-7303-050-2025.md`）：PDF 首页 `Date of Issuance 06/03/2022`、`IMPLEMENTATION DATE 06/03/2022`、`Correction date 09/10/2025`——⚠ 这是**2022 版程序的 2025 年更正本**，文件名 `20250915` 不是新签发日期，不得套用 7303.040 的 `2025-CPM-HFP-001` Transmittal 格式。原文 `Inspections are not planned under this compliance program`：它是**抽样 program**，检查由 7303.040 等承担，只在其中采 for-cause 产品/环境样。PART III.1.C / Table 2、3 给产品样品 subs 数（**不含 702(b) 部分**；易腐与进口状态不取 702(b)）；ATTACHMENT A 给环境拭子 **Listeria ≥50（理想 100）/ Salmonella ≥100（理想 300）**、Zone 1–3 / 2–3、湿干区目标菌、WGS + GenomeTrakr、Part V.1 三档 Findings 与未授予 Direct Reference；ATTACHMENT B 给污秽/霉变抽样；PART V 表 7/8 是**逐案、非穷尽**的可能 FDA 响应清单。对应能力卡 **`inspection-sampling`（CAP-17）**。引用用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」。

**第九来源 — FDA IOM 2026《Chapter 5 – Inspections》**（221 页 / 410 书签 / 450 标题，官方 PDF 经 `pdf2md-pro` 转换，全文见 `source-iom-ch5-2026.md`）：⚠ **仅 Chapter 5 单章**（含 5.1–5.16 与 Exhibit 5-1…5-23），IOM Ch.3/4/6/7/8/9/10 未收。法定基础 FD&C Act 704(a)(1)；国内到场出示 credentials 并签 **FDA 482**、**境外一般不发 482**；IOM 5.2.7 预告三层口径（医疗器械与部分 BIMO 强制、常规 produce farm 应预告、食品企业一般不预告由 program division 裁量、**境外通常提前告知**、国内不少于 5 个日历日且改期不晚于原日期 +5 天、预告不是预约）；**5.5.10 / 5.5.11.3 的 483 措辞纪律是全包效力分层的制度性反证**——不得引用法规原文、不得纳入标准、`Do not cite deviations from policy or guidance documents on the FDA 483`、不得写 opinions/violative，仅偏离 guidance 未违反法规的属 **Category 3 non-reportable observation**（只口头讨论并入 EIR）；5.5.12.3 给 15 个工作日的通用程序出处；5.5.12.5 给 Form FDA 484；5.6 给记录/电子记录/照片证据规则与「样品合格不阻碍 cGMP 指控」；5.5.2 给 301(e)/(f) 与境外 807(b)。对应能力卡 **`investigator-authority-procedure`（CAP-18）**。引用用「IOM 5.x.x / IOM Exhibit 5-x」。

**分工（v4.5 当时口径）**：CPGM 7303.040（CAP-16）＝检查类型/分级/记录举证/483 回复；CP 7303.050（CAP-17）＝取样量/环境拭子/阳性升级；IOM Ch.5（CAP-18）＝权限/表单/483 措辞/证据链。三卡合起来才回答「FDA 来检查怎么办」；**不要拿其中一份的数字或规则去替代另一份**。全包自 v4.5 起统一「九类不可混引」——**v4.6 起再加 CAP-19 与 CP 7303.070，改为四卡 /「十类不可混引」，见下节**。

**仍未收（v4.5 当时记录）**：IOM 其余章节（尤其 Ch.4 的 702(b) 分割留样与制样）、eBAM / BAM / AOAC / MPM 方法正文、SOP-001052 / SOP-000529 FMD-147、CPG 全套（含 Sec. 130.100 / 527.300）、RPM、Import Alerts / Import Bulletins 正文、其他 Compliance Programs（7303.878 / 7303.080 / 7303.070 / 7304.019）、21 CFR 2.10 / 133 / 1240.61 正文、FDA 483/484/1551 数据库、21 CFR part 117 citations table、SOFO job aid 与 eNSpect / CAR / CMS 内部系统；以及 FDA 境外无预告检查与 RRA 的政策公告原文。

## 版本补充说明（v4.6，第十来源：低酸罐头与酸化食品 program）

本包再纳入 FDA **CP 7303.070《Acidified and Low-Acid Canned Foods Program – Import & Domestic》**（`20250929_CP 7303.070 ... 508-Compliant.pdf`，61 页 / 40 书签，官方 PDF 经 `pdf2md-pro` 转换，全文见 `source-cp-7303-070-2024.md`）。⚠ 首页 `Date of Issuance 09/26/2024` / `IMPLEMENTATION DATE 9/26/2024` / `Correction Date 9/26/2025`——文件名 `20250929` 只是 PDF 生成日，本件是 **2024 版程序的 2025 更正本**，与 CP 7303.050 同形态，不同于 CPGM 7303.040 的 `2025-CPM-HFP-001` 新 Transmittal。它同样是 FDA 给检查员、实验室分析员与合规官的**内部作业指导**，非法规、非 Guidance for Industry、不创设企业义务。对应能力卡 **`lacf-inspection-program`（CAP-19）**。

**最重要的贡献是把本包 Part 117 管辖分流落到检查员侧**（`PART II.2.C(1)`，与 CFR 正文〔§ 117.5(d)(1)(2)〕一致）：LACF 产品受 CGMP & PCHF 约束，但 Subparts C/G 不适用于 part 113 覆盖的活动，且该豁免**仅限 part 113 管辖的微生物危害**；未被热处理控制且需预防控制的危害（`Staphylococcus aureus` 生长与产毒、化学危害、物理危害）仍归 Subparts C/G。⚠ **酸化食品不在 § 117.5(d) 的豁免内**——`Acidified foods are subject to the CGMP & PCHF rule`，其 PCHF 覆盖转 CP 7303.040，但不论企业规模，AF 检查重点仍在 21 CFR part 108 / 114。**〔§ 117.201〕是 qualified facility 的 modified requirements，不是 LACF 条款**。〔§ 117.1(c)〕另定受专项 CGMP 管辖的食品同时受 Part 117 约束。

**与已收三卡的官方分工**：`Products labeled "Keep Refrigerated" are exempt from 21 CFR 113/114. These products should be covered under Compliance Program 7303.050.`；未贴标 AF/LACF「brites」运至中央仓贴标装箱的检查报 `PAC 03040`；CGMP & PCHF 覆盖工时按 7303.040 的 PART II.2.C(3) 报 PAC；动物食品 `71070` 联动 7371.000 /〔21 CFR 507.5(b)〕、海产品并做 7303.842 HACCP。`PART II.2.B(2)` 明确 **RRA 自愿、全程远程、`RRAs are not considered inspections`、不满足 FD&C Act 704 条要求现场 inspection 的法定场景（510(h) / 503B(b)）**——这是程序性定义，不是 FDA 扩大 RRA / 境外无预告检查的政策公告原文（后者仍未收），也不改变 IOM 5.2.7 的预告三层口径。

**其余口径**：判定合规的法源三角为 **21 CFR part 108（FCE 注册 / SID 定时工艺备案 / Emergency Permit）、part 113、part 114**，⚠ **v4.7 更正**：其中 **part 113 / 114 两套法规正文已收**（第十一/十二来源，CAP-20，按〔§ 113.xxx〕〔§ 114.xxx〕引用）；**仍未收的是 part 108**（FCE 注册 / SID 定时工艺备案 / Emergency Permit / §108.35），以及 part 110（至今有效但正文未收）、part 120（**part 123 自 v4.9 起已收，见 CAP-22**）。以下 CP 内涉及 113/114 法条义务的表述已可回法条核对，其余一律标「转引未收」；`PART III.1.A` 给酸化判定三步（酸成分+水 → 加低酸成分研磨测 `Maximum Equilibrium pH` → 送 HFP 邮箱判 significant difference；ROP 阈值 OTR <10,000 cc/m²/24h at 24°C；企业自判至少 6 个成品单元；**法定身份由 HFP 判定**）、AF / LACF / Aseptic LACF 三类检查目标与六组取证记录；`PART IV.2` 给 ≤795 g 取 24 罐 / 其余 12 罐、pH **4.40 / 4.65** 双分析师触发线与 `Never average the two analysts' results together`、异常罐 **>1%** 与 pH **>4.75** 肉毒毒素/PCR、14 天 progressive decomp、C. botulinum 仅 for-cause（PAF `MIC`）；`PART V.2` 给 Import Alert 99-37 / 99-38 与 `Do not recommend firm/products for an Import Alert/DWPE solely based on firm/product not registered and/or filed processes with FDA` 的**反直觉限制**、FCE/SID 在 FURLS / Center Views 核验与 DTR；`PART II.2.B(1)` 给 Emergency Permit / OAI 3 个月与 6 个月、VAI 12 个月、NAI 按 FSMA 频率、24 小时通电。引用用「CP 7303.070 PART x / ATTACHMENT x」。

**⚠ 三套 pH/aw 数字不可互替**：4.6 / 0.85 是〔§ 117.3〕〔§ 117.80(c)(14)(15)〕的**法定**平衡 pH 边界与持续维持义务；4.40 / 4.65 / 4.75 / 0.90 / 0.93 / 异常罐 1% / 24 罐是 CP 的**检查员与实验室触发线**；≤4.4 / ≤0.92 是 L.mono 草案**建议层**的抑制型配方基准。CP 的取样量与触发线**不是企业放行标准**。全包 v4.6 时为「十类不可混引」、v4.7 扩为「十二类不可混引」（新增两套法规正文）、v4.8 扩为「十三类不可混引」（新增 CP 7303.878 检查程序）、**v4.9 起扩为「十四类不可混引」**（新增 21 CFR Part 123 法规正文，见文末节）；21 CFR part 108 / 110 / 120、IOM Ch.4 Sample Schedule Chart 2、BAM Ch.13B/14/17/21A/22A–22D、CPG Sec. 520.200/520.300、Import Alert 全文、SOP-001642、RPM Ch.4/9 等未收正文一律标「转引未收」。

**仍未收（v4.6 当时记录，v4.7 收窄；⚠ Ch.4 自 v4.16 起已收，见文末）**：IOM 其余章节（尤其 Ch.3 的法定权限与 Ch.6 的进口取样）、21 CFR part 108 / 110 / 120（**part 113 / 114 正文自 v4.7 起已收、part 123 自 v4.9 起已收**）与 21 CFR 2.10 / 133 / 1240.61 / 507 正文、eBAM / BAM / AOAC / MPM 方法正文、FMD-86 / FMD-147 / SOP-001052 / SOP-000529 / SOP-001642、CPG 全套（含 Sec. 130.100 / 527.300 / 520.200 / 520.300）、RPM、Import Alerts / Import Bulletins 与 Import Alert 99-37/99-38 正文、其他 Compliance Programs（7303.878 / 7303.080 / 7303.842 / 7371.000 / 7321.006 / 7304.019 / 7304.004A / 7309.006）、FDA 483/484/1551 数据库、21 CFR part 117 citations table、SOFO job aid 与 eNSpect / CAR / CMS 内部系统；以及 FDA 境外无预告检查、RRA 适用范围与 FD&C Act 704(a)(4) 检查前索取记录的政策公告原文。

**当时规模**：19 张能力卡 / 142 条术语 / 75 条测试用例（v4.6）；**当前规模见文末 v4.8 节**。


## 版本补充说明（v4.7，第十一与第十二来源：低酸/酸化食品法规正文）

本版把 **21 CFR Part 113（Thermally Processed Low-Acid Foods Packaged in Hermetically Sealed Containers）** 与 **21 CFR Part 114（Acidified Foods）** 两套 **联邦法规正文**（均为 4-1-25 Edition，GPO/eCFR 双栏印刷版；Part 113 共 36 页 / 10 条款，Part 114 共 7 页 / 8 条款）纳入，全文见 `source-cfr-part113-2025.md` 与 `source-cfr-part114-2025.md`，对应第 20 张能力卡 **`lacf-statutory-requirements`（CAP-20）**。这是本包**首次纳入 Part 117 之外的法规正文**：自此法规正文层含〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕**三套独立编号**，并行、不是上下位、也不是新旧替代关系。⚠ `4–1–25 Edition` 是 CFR 年度编纂版次（修订至 2025-04-01），不是 2025 年新规；条文末尾 FR citation 才是修订出处。两份 PDF 会串栏，故用专用 `.cangjie/convert_cfr_part.py` 按「页→左栏→右栏」重排，条款号全部命中，保留印刷断词连字符。

**接口（本卡的核心）**：〔§ 117.1(c)〕`Food covered by specific current good manufacturing practice regulations also is subject to the requirements of those regulations` 给并行依据；〔§ 117.5(d)(1)〕的 Subparts C/G 豁免须同时满足 `required to comply with` **且** `in compliance with` part 113（**条件性**，企业 part 113 不合规时不成立），〔§ 117.5(d)(2)〕把它限定在 **part 113 管辖的微生物危害**；**§117.5 豁免清单列的是 part 123 (b)、part 120 (c)、part 113 (d)，没有 part 114**——酸化食品全程受 Part 117 Subparts B/C/G 约束，〔§ 114.5〕又反向把 `parts 110 and 117` 与本 part 五个 § 一并列为掺假判据。

**企业义务清单（条款级）**：Part 113 的 §113.3(n) 定义（4.6 / 0.85、番茄 pH <4.7 例外）、§113.5 八个判据条款、§113.10 BPCS、§113.40 设备与 NIST 溯源校准、§113.60 容器、§113.81 产品制备、§113.83 scheduled process 与 critical factors、§113.87 杀菌室规程 / product traffic control / **FDA 调阅权**、§113.89 偏差、§113.100 记录；Part 114 的 §114.3 定义与排除项、§114.5 掺假判据、§114.10 BPCS（课程含 pH controls and critical factors in acidification）、§114.80 成品 pH ≤4.6 按时达到并维持 + **酸化不等于免除热处理**（杀 vegetative cells）+ **pH >4.0 须用电位法**、§114.83 scheduled process、§114.89 **三条偏差路径**（含按 part 113 作低酸食品热处理）、§114.90 方法、§114.100 记录。

**两处必须记住的纠错**：① **Part 110 至今有效**——FDA 2018-09-12 最终规则（FR Doc. 2018-19855）撤回了 2015 规则拟于 2018-09-17 删除 part 110 的 amendatory instruction 13，§114.5 的 `parts 110 and 117` 与 Handbook 的 `21 CFR 110.110` 都不是过时引用，只是**正文本包未收**，须标「转引未收」；手册那句是 §110.110(c) 意译，仍不得标成〔§ 117.110(c)〕。② **两 part 记录保存口径不同**：〔§ 113.100(g)〕1 年厂内 + 另 2 年（合计 3 年）、(h) 允许符合 part 11 的电子记录；〔§ 114.100(e)〕只有整段 3 年，无分段、无 part 11 条款。

**三套数字仍不可互替**：4.6 / 0.85 / 4.0（法条层）｜4.40 / 4.65 / 4.75 / 0.90 / 0.93 / 1% / 24 罐（CP 7303.070 检查员实验室触发线）｜≤4.4 / ≤0.92（L.mono 草案建议层）。全包 v4.7 时统一「十二类不可混引」、**v4.8 起统一「十三类不可混引」**；检查员作业指导（CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / CP 7303.878）不创设企业义务，与 CAP-19 分工为「本卡＝法条义务层，CAP-19＝检查员作业层」。

**仍未收**：21 CFR part 108 / 110 / 120 正文（part 123 自 v4.9 起已收，见 CAP-22）、F0/D/z 计算与温度分布/热穿透研究设计、卷边解剖判读、商业无菌验证方案审批、BAM / AOAC / MPM 方法正文（**IOM Ch.4 Sample Schedule Chart 2 自 v4.16 起已收，见文末**）、CPG 全套、Import Alert 全文、其余 Compliance Programs（7303.842 / 7303.847 / 7303.819 等；**7303.878 已由 v4.8 收入**）、Form 2541e 细则。

**当时规模**：20 张能力卡 / 152 条术语 / 85 条测试用例（v4.7）；**当前规模见下节 v4.8**。


## 版本补充说明（v4.8，第十三来源：CP 7303.878 FSVP 检查程序）

本版把 **FDA Compliance Program 7303.878《Foreign Supplier Verification Programs Inspections》** 纳入为第十三来源，全文见 `source-cp-7303-878-2023.md`，对应第 21 张能力卡 **`fsvp-inspection-program`（CAP-21）**。PDF 首页 `Transmittal Number: 2023-CPM-CFSAN-003` / `Implementation Date: 09/27/2023` / `Date of Issuance: 08/28/2025`；Change History 显示 2025 条目**只改 POC 与机构名称缩写**，故本件是 **2023-09-27 版程序的 2025-08-28 更正版**，不是 2025 新 program，也不是 CPGM 7303.040 那种新 Transmittal 形态。33 页 / 20 书签全命中，转换后清除 62 行重复页眉。

**它是什么、不是什么**：这是 FDA 给检查员、进口分区合规官与中心审评人员的**内部作业指导**（`provides instruction to field staff`），标注「CP 7303.878 PART x」，**不创设企业义务**。真正创设义务的是 FSMA §301 增订的 FD&C Act §805 与其下的 **21 CFR part 1, subpart L（§§1.500–1.514）FSVP 法规**——**该法规正文本包未收，一律标「转引未收」**，不得从 CP 的检查动作反推条文。引用时四层要分开：法规义务〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕｜FSVP 法规「21 CFR part 1 subpart L §1.5xx（转引未收）」｜CP 内容「CP 7303.878 PART x」｜其余 program 各自章号。

**与 Part 117 Subpart G 的分流（本卡价值所在）**：两套法源、两类主体——FD&C Act §805 / part 1 subpart L 管进口商 **FSVPI**（§1.500 定义：入境时的美国货主/收货人；无美国货主时由签署同意书的美国代理/代表承担），FD&C Act §418 / Part 117 Subpart G 管 **receiving facility**。CP PART II.3.A 的 **deemed compliance** 仅在进口商同时为 manufacturer/processor 且符合 Part 117 / 507 供应链要求时成立，且原文 `except they must comply with section 1.509` 把**每一 entry line 报关时电子提供名称、邮箱与 UFI（FDA 认可 DUNS）**的义务单独留下；纯贸易进口商没有该通道。回答「已做 Part 117 供应链验证，还要不要做 FSVP」必须先问主体身份，不能二值合并。

**检查口径与执法阶梯**：§1.502(a) 对每一种食品 develop, maintain, and follow FSVP；standard requirements（§1.502/1.503/1.504/1.505/1.506/1.508/1.509/1.510）与 modified requirements（§1.507/1.511/1.512/1.513）是**可选关系**（满足 modified 条件者仍可选择 standard），不是「少做一套」；§1.501(b)–(h) 八类豁免。CP PART III.1.C 明写 **`Samples will not be collected as part of an FSVP inspection.`**、PART IV 四节 Intentionally Left Blank——FSVP 检查查 FSVP、危害分析、供应商批准评价、验证活动、§1.509 与纠正措施**记录**，不得套 CP 7303.050 的 subs 样品量与环境拭子。PART V 给 483a 观察分级 → NAI/VAI/OAI → Warning Letter / **Import Alert 99-41** / FD&C Act §801(a)(3) 拒绝入境（§301(zz) 禁止行为）。⚠ **99-41 是 FSVP 不合规进口商名单，不是 CP 7303.070 的 99-37 / 99-38**（LACF/AF 备案与过程控制）；99-41 按「具体食品 + 具体境外供应商组合」列 Red List，未列组合在不受其他 Alert 约束时仍可进口，移除须按指示提交证据并先于再次进口；direct reference authority 仅在有限情形授予，首次违法不默认优先执法；§1.507 disclosure 不能替代 §801(b)/§1.95 整改提案资料。

**十四类不可混引（v4.9 口径；v4.8 时为十三类）**：21 CFR Part 117 / PCHF 行业指南 / L.mono Draft Guidance / SECG / 过敏原 Ed.5 / Food Defect Levels Handbook / CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / 21 CFR Part 113 / 21 CFR Part 114 / CP 7303.878 / **21 CFR Part 123**。检查员作业指导一律不创设企业义务；shall/must 的法定义务只回法规正文。

**仍未收**：21 CFR part 1 subpart L 正文、Import Alert 99-41 全文、FSVP Guidance 与 IP guidance tabs、HFP Enforcement Bulletin #13/#6、RPM 4-1-8、CP 7303.819 / 7303.842 / 7303.847 正文、21 CFR part 108 / 110 / 120 / 507 正文（part 123 自 v4.9 起已收）（**IOM Ch.4 自 v4.16 起已收，见文末**）、BAM / CPG 全套。v4.8 **未重跑**触发 / 输出 / 路由评测，v4.7 的评测结论不得冒用。

**当时规模**：21 张能力卡 / 162 条术语 / 95 条测试用例 / 十三类来源（v4.8）；**当前规模见文末 v4.9 节**。


## v4.9 — 海产品 HACCP 法条层（21 CFR Part 123）

**第十四来源**：`source-cfr-part123-2025.md` — 21 CFR Part 123《Fish and Fishery Products》，4-1-25 Edition（9 页 / 13 条款）。用户提供的 `CFR-2025-title21-vol2-part123.pdf` 经 `.cangjie/convert_cfr_part.py` 双栏重排转出；13/13 条款命中、页眉页码残留 0、卷首目录区裁 34 行、串栏 0。

**新增 CAP-22 `seafood-haccp-statutory-requirements`**：把水产品企业义务从「只能靠 CP 7303.842 反推」升级为条款级法定义务。B1–B12 边界、A2 25 条触发、R 段 33 个引用块逐字核验（32 条 Part 123 + 1 条 §117.5(b)）。

**五处高频误读已钉死**：
1. **默认适用，例外只有一扇门**：〔§ 123.5(a)〕`Except as provided by § 117.5(b), parts 110 and 117 ... apply`；不是「做水产品就只按 part 123 管」。
2. **§117.5(b) 无限缩款**：part 113 有〔§ 117.5(d)(2)〕把豁免限缩到微生物危害，**part 123 没有**。搬前者口径会低估豁免；因「没限缩」推成整厂免检会高估。边界是受 part 123 管辖的 activities（〔§ 123.3(k)(2)〕三项排除不在内），且豁免不含 Part 117 Subpart B 的 CGMP。
3. **Subpart B/C 是 augments 叠加**：〔§ 123.15〕〔§ 123.20〕原文 `augments subpart A`，漏 Subpart A 即漏项。
4. **§123.16 例外只排一条**：`except those subject to part 113 or 114` 只排除该条；Subpart A 全套仍适用（与〔§ 123.20〕整体不适用 Subpart C 不同）。
5. **记录期三套口径不可串**：〔§ 123.9(b)(1)〕冷藏 1 年 / 冷冻-保藏-货架稳定 2 年；Part 113〔§ 113.100(g)〕1+2 分段；Part 114〔§ 114.100(e)〕整段 3 年。

**另钉两处**：〔§ 123.11(a)〕SSOP 是 `should`、(b)(c) 监测记录是 `shall`（原文措辞，不得升格也不得说可以不做）；〔§ 123.12〕进口商验证与 FSVP 是**两套法源**，deemed compliance 不覆盖 §123.12。

**规模（v4.9 历史快照）**：22 张能力卡 / 172 条术语 / 105 条测试用例 / **十四类来源**（v4.9）。**v4.10 当时为 23 张能力卡 / 182 条术语 / 115 条测试用例 / 十五类来源 / dist-v14**；当前 v4.11 规模见文末 v4.11 节。

**本版未重跑评测**：v4.7 的 F1 1.000 / 0.994、输出 10/10、路由 40/40 均为历史结论，不得冒用；10 条 `seafood-*` 与新卡路由待测。


## v4.10 追加：第十五来源与第 23 张卡

> 本节是 v4.10 增量记录；上文各节的 v4.x 规模与「十四类不可混引」为**历史口径**，保留不改。

- **v4.10 当时规模**：23 张能力卡 / 182 条术语 / 115 条测试用例 / **十五类来源** / `dist-v14`。（v4.11 时为 24 张 / 192 条 / 125 条 / 十六类 / `dist-v15`；v4.12 时为 25 张 / 202 条 / 135 条 / 十七类 / `dist-v16`；**v4.13 现为 26 张 / 212 条 / 145 条 / 十八类 / `dist-v17`**，见文末 v4.13 节。）
- **第十五来源**：FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版 June 2022（SGR 129），`source-seafood-hazards-guide-2022.md`。它是**非约束性技术指南层**，与第十四来源 21 CFR Part 123（法条义务层，CAP-22）配对而非合并：前者给「怎么判定」，后者给「必须做什么」。
- **新增能力卡 CAP-23 `seafood-hazards-controls-guide`**：完整危害分析判定链（Ch.3 三表识别 → Ch.4–21 理解危害 → 无控制条件下判 `reasonably likely to occur` → 六栏工作表 Yes/No 理由 → Step 11 判定树定 CCP → 控制策略示例 → 关键限值与监控四问）。R 段 37 个英文引用块经 `.cangjie/verify_v4_10_quotes.py` 逐字核验 37/37 命中。
- **十五类不可混引（v4.10 口径；v4.9 时为十四类）**：在上文十四类清单之外，增加 **FDA 海产品危害与控制指南第 4 版**。层次仍为：法规正文 ＞ FDA 指南 ＞ CPGM／CP／IOM 检查程序（仅检查员视角）。指南内引用写「Seafood Hazards Guide 第 4 版 Ch.x / Appendix x / L####」，法条写〔§ 123.xxx〕，不可互换。
- **仍未收**：CP 7303.842、NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、Import Alert 16-xx、BAM 海产品章节，以及 Appendix 5 回指的 CPG / 21 CFR 556 / 40 CFR 180 / Import Tolerance 等外部法源。涉及具体数值的条款级结论一律标「转引未收」。
- 阶段 0 整书理解见 `BOOK_OVERVIEW-seafood-hazards-guide-2022.md`；阶段 1 五路候选见 `candidates/v4-10-*.md`；完整变更与校验记录见 `PIPELINE_STATE.md` v4.10 段。

## v4.11 追加：第十六来源 CP 7303.842（海产品检查程序）

- 上表与各节「仍未收 CP 7303.842」为 **v4.10 及以前**的当时口径，自 v4.11 起该件已纳入为**第十六来源**，见 `source-cp-7303-842-2023.md` 与 CAP-24 `seafood-inspection-program`。v4.11 时为 **十六类来源不可混引**、24 张能力卡 / 192 术语 / 125 用例 / `dist-v15`（v4.12 时为十七类 / 25 张 / 202 条 / 135 条 / `dist-v16`；**v4.13 现为十八类 / 26 张 / 212 条 / 145 条 / `dist-v17`**，见文末 v4.13 节）。
- 该件是 **2023-11-01 版程序的 2025-09-30 更正本**（文件名 `20250929` 只是 PDF 生成日），CP 7303.842 与 CP 7303.844 已合并但 PAC 仍分进口/国产。层次为**检查程序作业层**：法规正文〔§ 123.xxx〕（CAP-22）＞ 技术指南（CAP-23）＞ 本 CP 的 field staff 指令（CAP-24）；CP 不创设企业义务，其 PART IV 触发值也不是法规限值。
- 历史「仍未收」清单中除 CP 7303.842 与 IOM Ch.4 外的项目（part 120 / 1240 / 110 / 507、NSSP Guide、CPG 与 Import Alert 全文、BAM 方法等）**仍然未收**；**IOM Ch.4 自 v4.16 起已收**；**21 CFR part 108 自 v4.12 起已收**（第十七来源，CAP-25），不再属未收项。

## v4.12 追加：第十七来源 21 CFR Part 108（紧急许可控制）

> 本节是 v4.12 增量记录；上文各节的 v4.x 规模与「十六类不可混引」为**历史口径**，保留不改。

- **v4.12 当时规模**：**25 张能力卡 / 202 条术语 / 135 条测试用例 / 十七类来源 / `dist-v16`**。
- **第十七来源**：**21 CFR Part 108《Emergency Permit Control》**（4-1-25 Edition，11 页 / 9 条款，书页 248–257），`source-cfr-part108-2025.md`。它是 **FD&C Act §404 的实施细则**（AUTHORITY `21 U.S.C. 342, 344, 371`），属**法规正文层**，与已收的 Part 113 / 114 / 117 / 123 并列而成**第五套独立编号体系**〔§ 108.xxx〕。
- **新增能力卡 CAP-25 `emergency-permit-control`**：这是全包被点名最久的一处缺口——CAP-20 的 B1 曾明写「21 CFR part 108 正文仍未收，这是本卡最大缺口」。卡内把「**手续层**」与「**实体层**」切开：Subpart A（108.3/.5/.6/.7/.10/.12/.19）给许可裁定、撤销、签发、中止与恢复、无证生产的产品放行闸门、许可豁免；Subpart B（108.25 酸化食品 / 108.35 LACF）给注册（Form FDA 2541）、工艺备案（2541e / 2541d / 2541f / 2541g）、停业通知、腐败与偏差报告、召回程序文件、BPCS 受训主管与记录保存。R 段 27 个英文引用块经 `.cangjie/verify_v4_12_quotes.py` 逐字核验 **27/27 命中正文区，0 超 100 词、0 表格引用**。
- **核心纠偏（本版最重要的一条）**：**紧急许可不是 LACF／酸化食品企业的常态义务**。108.25(a) / 108.35(a) 用的都是 `may be required whenever the Commissioner finds, after investigation, that the commercial processor has failed to fulfill all the requirements of this section`，未履行义务只构成 `prima facie basis`（初步依据），仍须走 Subpart A 的裁定—通知—异议—听证—裁定链条；108.6(a) 另限定 `A permit shall be required only during such temporary period as is necessary to protect the public health.` 因此「LACF 企业必须持紧急许可证」是错误陈述。
- **其余四处高频误读**：① Subpart A 全是 **working days**（3/5/10/20），Subpart B 全是**日历天**（10/30/60/90），不可互换；② 记录保存**四套口径**（108.25(g) 整段 3 年｜108.35(h) 1+2 年｜113.100(g) 1+2 年且可用 part 11 电子记录｜114.100(e) 整段 3 年无 part 11 条款）不得合并成「3 年」；③ 国内企业走紧急许可、**外国加工者走 §801 拒绝入境**（108.25(j) / 108.35(k)），两条路方向相反；④ 108.35 独有的 FSIS 连续检验豁免 (i)、加州视为合规 (j)(2)、FOIA 豁免 (l) 不得套到酸化食品。
- **十七类不可混引（v4.12 口径；v4.11 时为十六类）**：在十六类之外增加 **21 CFR Part 108 法规正文**。层次仍为：法规正文（五套编号）＞ FDA 指南 ＞ CPGM／CP／IOM 检查程序。Part 108 引用写〔§ 108.xxx〕，且 `§§ 114.10, 114.80(a) (1) and (2), and (b), 114.83, 114.89, and 114.100 (b), (c), and (d)` 这类交叉引用清单不得简写。
- **仍未收**：2541 系列表单栏目细则、FURLS / Center Views 实际操作、21 CFR part 110 正文、CPG 全套、Import Alert 全文、BAM / AOAC / MPM 方法正文（**IOM Ch.4 Sample Schedule Chart 2 自 v4.16 起已收，见文末**）。
- 转换链路：`.cangjie/convert_cfr_part.py`（页 → 左栏 → 右栏重排）→ `.cangjie/fix_part108_reflow.py`（定点修 **6 处**重排缺陷：1 处正文句被误升为条款标题、4 处句中断段、1 处两编号项并段，逐条断言）。自检：9/9 条款命中、页眉与独立页码残留 0、裁掉首部 Part 107 残段 9 段与尾部 Part 109 残段 14 段、串栏 0。完整变更与校验记录见 `PIPELINE_STATE.md` v4.12 段。

## v4.13 追加：第十八来源 21 CFR Part 120（果汁 HACCP）

> 本节是 v4.13 增量记录；上文各节的 v4.x 规模与「十七类不可混引」为**历史口径**，保留不改。

- **v4.13 当时规模**：**26 张能力卡 / 212 条术语 / 145 条测试用例 / 十八类来源 / `dist-v17`**。
- **第十八来源**：**21 CFR Part 120《Hazard Analysis and Critical Control Point (HACCP) Systems》**（4-1-25 Edition，10 页 / 15 条款，书页 439–448），`source-cfr-part120-2025.md`。它是**独立的果汁 HACCP 体系法规**——不是「果汁版的 Part 117」，也不是 Part 117 的子集——属法规正文层，为全包**第六套独立编号体系**〔§ 120.xxx〕。
- **新增能力卡 CAP-26 `juice-haccp`**：补上全包最后一处「成熟法规但只有转引」的缺口。此前六处（CAP-20 B10、CAP-22 A2-22、CAP-23 头注、CAP-25 B10、CAP-15 未收清单、`reference-tools-discipline` 第 12 条）一律把 part 120 正文标「转引未收」，只能靠〔§ 117.5(c)〕倒推「果汁有同类豁免」。R 段 26 个英文引用块经 `.cangjie/verify_v4_13_quotes.py` 逐字核验 **26/26 命中正文区，0 超 100 词、0 表格引用**。
- **五处实质纠偏**：
  1. **5-log 是法定要求**——〔§ 120.24(a)〕`shall ... consistently produce, at a minimum, a 5 log (i.e., 10⁵) reduction`，须**持续**、覆盖**货架期**、在**正常与中度滥用条件**下成立；目标菌是 `pertinent microorganism`（最耐热＋具公共卫生意义＋可能出现于该果汁），不是沙门氏菌或 O157。
  2. **§120.25 只适用于果面处理者**——`relies on treatments that do not come into direct contact with all parts of the juice`；靠热力杀菌的厂，成品检验在〔§ 120.11(a)(1)(iii)〕下是 `At the option of the processor`。
  3. **两处豁免对象不同**——〔§ 120.24(a)(1)(2)〕免 **5-log 指标**；〔§ 120.7(e)〕免「part 113/114 已控制的微生物与微生物毒素」**危害的计划处理**。混成「受 113/114 管辖就不用做果汁 HACCP」是双重错误。
  4. **记录复审是 7 日历天**——〔§ 120.11(a)(1)(iv)(A)(B)〕`within 1 week (7 days)`，与 Part 117 的工作日口径不同；同部法规内〔§ 120.25(a)〕又用 `working days`，两种日并存。
  5. **记录期是第六套口径**——易腐/冷藏 ≥1 年、冷冻/保藏/货架稳定 2 年或货架期孰长，起算点**产品制备日**；异地存放须监测后 6 个月 + 24 小时内到现场。
- **接口逐字锁定**：〔§ 120.5〕`Except as provided by § 117.5(c), parts 110 and 117 of this chapter apply ...`——Part 117 **默认适用**，〔§ 117.5(c)〕是唯一且**条件性**的出口。⚠ 但 **§ 117.5(c) 的逐字文本不在本包**，凡需引用其措辞一律标「转引未收」，不得据 §120.5 反推、也不得套用 §117.5(b)/(d) 的写法。
- **十八类不可混引（v4.13 口径；v4.12 时为十七类）**：在十七类之外增加 **21 CFR Part 120 法规正文**。层次仍为：法规正文（六套编号）＞ FDA 指南 ＞ CPGM／CP／IOM 检查程序。
- **转换器本轮修了两处缺陷（已回写 `.cangjie/convert_cfr_part.py`）**：① 多行 part 标题的续行落在目录裁剪区内被整段吞掉（Part 120 的 `CRITICAL CONTROL POINT (HACCP) SYSTEMS` 曾丢失；Part 108 的标题也因此缺 `CONTROL`，但那份已定稿不回改）；② NOISE 的 `^\d{2,4}$` 把独占一行的数字当页码（§120.25(c)(4)(i) 的 `90 mL` 曾丢成 `mL`），现改为 `--keep-standalone-numbers` 按需启用。另 `.cangjie/fix_part120_reflow.py` 修 11 处段界缺陷（1 处句中断段 + 10 处编号项并段），脚本幂等。
- **文本层缺陷**：`5 log (i.e., 105)` 的 `105` 是上标 10⁵ 在 PDF 文本层丢失，引用须还原并注明。
- **仍未收**：〔§ 117.5(c)〕逐字文本、21 CFR part 110 正文、CP 7303.047 果汁 program、CPG 与 Import Alert 全文、BAM / AOAC 方法全文。

## v4.15 追加：第十九来源 FDA CP 7303.847（果汁 HACCP 检查程序）

> 本节是 v4.15 增量记录；上文各节的 v4.x 规模与「十八类不可混引」为**历史口径**，保留不改。

- **v4.15 当时规模**：**27 张能力卡 / 223 条术语 / 157 条测试用例 / 十九类来源 / `dist-v19`**。
- **第十九来源**：**FDA Compliance Program Guidance Manual, PROGRAM 7303.847《Juice HACCP Inspection Program (Processor and Importer Inspections)》**（Chapter 03，**2010-11-02 版 / 2025-09-18 更正**，26 页 / 35 书签），`source-cp-7303-847-2025.md`。属**检查程序作业层**：非法规、非 Guidance for Industry、**不创设企业义务**。
- **新增能力卡 CAP-27 `juice-inspection-program`**：与 CAP-26（Part 120 法条层）配对，补齐 LACF（CAP-20/CAP-19）与海产品（CAP-22/23/24）之外的最后一条「法条层 + 检查程序层」链路。R 段 29 个英文引用块经 `.cangjie/verify_v4_15_quotes.py` **29/29 命中**（含 33 字符短句 `No samples are to be collected.`，核验阈值已由 40 降至 20）。
- **四类实质纠偏**：① **「没取样」不能反推「没问题」**——进口商检查根本不取样、验证样品只在预期 NAI/VAI 时取、且原文写「多数法规缺陷不需实物样品」；② **PAC 分流是硬错高发区**——`847H` 只服务实物验证样品、文档性样品只报 `03847` 且不计工作计划、进口商报 `03847H` 且 Establishment Type 用 A；③ **铅的 10/20 ppb 是 2022-04 草案拟议行动水平**，非法规限值；④ **CPGM 不创设企业义务**，检查动作不得写成企业义务。
- **⚠ 订正 v4.13 的一处硬错**：果汁检查程序号是 **CP 7303.847**，v4.13 在 CAP-26 与 meta 里误写为 `7303.047`（7 处）。本版全部订正，并在正文保留勘误说明。
- **转换方式变更**：本件**未用 pdf2md-pro**——其书签注入把 7 个书签标题插进段落中间、并把大纲块前置乱序（H2 虚高到 60）。改用 `.cangjie/convert_cp847.py` 按「固定 3 行页眉 + `— Page N` 页标记 + 全加粗标题 + 字号 ≥11」重建，行距 >1.55×行高断段；7 个 PART / 66 个小节 / 605 行。两处标题在文本层无字（PART II `1. Objective`、PART VI `1. References`/`2. Attachments`），已用书签补回，卡内注明**不可当逐字原文引**。
- **十九类不可混引（v4.15 口径；v4.14 时为十八类）**。
- **仍未收**：CPG 510.150 / 555.425 全文、CP 7307.001 / 7304.019 / 7309.006 / 7321.005 全文、BAM / AOAC 方法全文、Import Alert 全文、FACTS / eNSpect / CMS 内部操作、21 CFR part 110 正文。

## v4.16 追加：第二十来源 FDA IOM 2026 Chapter 4（Sampling）

> 本节是 v4.16 增量记录；上文各节的 v4.x 规模、「十九类不可混引」与各版「仍未收 IOM Ch.4」均为**历史口径**，保留不改。

- **v4.16 规模**：**28 张能力卡 / 233 条术语 / 168 条测试用例 / 二十类来源 / `dist-v20`**。
- **第二十来源**：**FDA《Investigations Operations Manual 2026, Chapter 4 — Sampling》**（189 页 / 361 书签 / 4.2 MB，PDF creationDate `2026-07-14`），`source-iom-ch4-2026.md`。属**检查程序作业层**：给调查员（Investigator / CSO）的内部作业手册，非法规、非 Guidance for Industry、**不创设企业义务**。这是全包自 v4.5 起在 CAP-17 / CAP-18 / CAP-19 / CAP-20 / CAP-25 / CAP-24 / 术语表与状态文档里反复标注「未收」的最后一块检查程序层空白。
- **转换与自检**：经用户级技能 `pdf2md-pro`（pymupdf4llm）转换；**361 书签全命中、0 丢弃**，405 个标题（H1 1 / H2 89 / H3 68 / H4 169 / H5 78）、345 行表格、页眉 `CHAPTER 4` 与独立页码残留 0、自动检出噪声行 2。文件头补「来源 / 效力层级 / 关键口径 / 转换局限」说明块（对齐 Ch.5 的写法）。CAP-28 R 段 **60 个英文引用块经 `.cangjie/verify_v4_16_quotes.py` 逐字核验 60/60 命中**，`body_only()` 只取 Word 点线目录起点之后的正文、排除自写文件头，避免自我验证循环。
- **新增能力卡 CAP-28 `iom-sampling-procedure`**：把一次取样拆成六道分流——类别（official physical / official DOC / INV / survey / non-regulatory）→ 数量（assignment → CP → IOM Sample Schedule 三级优先）→ 702(b) → 表单链（482 / 472 / 484 / 415a / 525 / 463a / 1664）→ 封存与运输 → 阳性结果与 483。
- **六类实质纠偏**：① **DOC sample 仍是 official sample**，只是不贴封条、不发 FDA 484——「没开 484」不能读成「样品不算数」；② **INV 不是「非正式样品」**，原文 `can be used as evidence in court, they must be sealed`；③ **`702(b)` 七项豁免不是封闭清单**，污秽样品是唯一「无论豁免与否仍要留」的反向例外，而环境拭子因被明文列入「无法以可行手段保存」通常不留；④ **环境取样不得预告**（防临时清洁抑制回收），且 50/100、Zone 1–4、24 小时到实验室全部是**检查员侧**口径，不是企业 EMP 标准；⑤ **阳性环境结果上 483 有双门槛**（关账前已知 + Listeria Zone 1/2 或 Salmonella Zone 2/3；Zone 3/4 不写），且**环境样品明确不勾 704(d)**；⑥ **`Sample Schedule Chart 2` 终于有原文**，但它是**取样计划**，与 CP 7303.070 PART IV.2 的 4.40 / 4.65 / 4.75 实验室触发线仍属两层。
- **Bundle 回补**：`assemble_bundle.py` 27 → **28 卡**（SLUGS 追加、ALSO_READ 新增 12 条正向链 + 13 张卡反向链）、`additional_sources` 18 → **19 条**（末条 `src-fda-iom-ch4-2026`）、core_principles 54 → **56**、stop_conditions 28 → **30**、entry.description 增加 IOM Ch.4 段落。全包当前口径统一为「**二十类不可混引 / 28 张卡**」，并清除各卡把 IOM Ch.4 写作「未收」的裸断言。
- **二十类不可混引（v4.16 口径；v4.15 时为十九类）**：在十九类之外增加 **IOM 2026 Chapter 4**。层次仍为：法规正文（六套编号）＞ FDA 指南 ＞ CPGM／CP／IOM 检查程序（仅检查员视角、不创设企业义务）。
- **转换局限（写入 CAP-28 B12）**：① 文件前部（L3–L17）是 Word 点线目录被压成的巨型单行块，非正文，检索以 `4.x.x` 小节号为准；② 书签插入位置错位（`4.7.2` 出现在 `4.7.1` 之前、`4.6.4` 混入 4.7 区），小节标题常以 heading 与 plain text 两种形态各出现一次；③ `## **Dry Ice Guidance**` / `## **PRODUCT**` / `## **CODE**` 等为伪标题；④ Exhibit 4-1…4-25 表单为 `picture intentionally omitted` 占位（全章 41 处），字段名可引、表格式样不可引；⑤ Chart 2 的 48/CASE、24/CASE、12/CASE、6/CASE 四组在 GFM 转换后错列，只可引「批大小 → 检查数 → 提前终止数」对应关系。
- **仍未收**：IOM Chapter 2 / 3 / 6 / 7 / 8 / 9 / 10 全本（尤其 Ch.3 的 3.2 权限、Ch.6 的 6.4 进口取样、Ch.8 的投诉与食源性疾病调查）、SOP-001052 / FMD-147 / OII SOP-000530、RPM 6-3 / 10-4、CPG 580.100 / 300.400 / 130.100 全文、BAM / AOAC / MPM 方法全文、FACTS / eNSpect / CMS / OASIS 内部操作、Form FDA 484 表单栏目细则。制样与显微判读、检验方法检出限仍须另行复核。


---

## v4.17 增量（2026-11-09）：第二十一来源 IOM 2026 Chapter 6 — Imports

- **新增能力卡 CAP-29 `iom-imports-procedure`**（来源路由入口）+ `references/capabilities/imports/` 下 **10 张 RIA++ 子卡**。输入为 FDA《Investigations Operations Manual 2026》Chapter 6（70 页 / 235 书签 / 约 24 万字符），按 cangjie-skill RIA-TV++ 流水线蒸馏：5 个 extractor 并行得 82 条候选 → 去重 20 单元 → 三重验证通过 10 → 晋级门全部判 router（1 个可发现入口服务 10 个能力单元）→ 压力测试 13 条盲测 96.7%。
- **覆盖的 10 个能力单元**：入境审查决策门与可辩护留痕（V01）、DER/DTR 触发依据分流与 DWPE（V02）、Prior Notice 硬时限（V03）、条件放行/撤消/redelivery 时间窗（V04）、违规处置主链与文书矩阵（V05）、Form FDA 766 改标重整授权门（V06）、Failure to Hold 8 步调查（V07）、FSVP 检查链与 483a 签发门（V08）、进口状态概念区分树（V09）、IOM 效力层判读元规则（V10）。
- **六类实质纠偏**：① `May Proceed` 是终局放行但「未作合规判定」，可被撤消且撤消不重开条件放行期；② `DWPE` 是「不检查就扣住」，DER/DTR 按触发依据而非严重度分流，查不到注册/510(k)/A of C 禁止直接建议扣留；③ `Failure to Hold` 是「无放行而分销」而非「移出港区」，货物 may be moved 合法；④ 三个「30 天」与一个「90 天」同数异义，DRQ/DTR/DER/DEF/INF 都不延长条件放行期；⑤ `Refusal of Admission` 不是终点，档案到销毁/出口证明才关闭；⑥ `FDA 483a`（FSVP 观察项，只在 closeout 签发）≠ `FDA 483`（Ch.5 现场检查观察项）。
- **二十一类不可混引（v4.17 口径；v4.16 时为二十类）**：在二十类之外增加 **IOM 2026 Chapter 6**。引用写「IOM 6.x.x [p.N]」，与 IOM 4.x.x / 5.x.x 并列但章号不得串用；不得写成〔§ 117.xxx〕式法规引用。
- **效力层**：IOM 是 FDA 内部操作指导、不是法规、不创设企业义务；`must`/`shall` 约束 FDA 内部作业，`should`/`as warranted`/`may` 属机构裁量；企业义务回 FD&C Act §801、21 CFR Part 1、19 CFR 113.62。全篇是监管者视角，企业侧迎检举证内容一律标〔推导·非原书主张〕。
- **仍未收**：IOM Chapter 2 / 3 / 7 / 8 / 9 / 10 全本、RPM Chapter 9、CPG 全套、Import Alert / Import Bulletin 全文、21 CFR part 1 subpart L 正文、Exhibit 6-1~6-4 表单字段（扫描件，需查原件）。
- **审计轨迹**：`E:/WeChatData/2026-11-09-08-58-24/books/iom-2026-ch6-imports/`（BOOK_OVERVIEW / candidates / verified / rejected / verified.yaml / destinations.json / GLOSSARY / DIGEST / test-results）。


## v4.18 追加：第二十二来源 21 CFR Part 101（食品标签法规正文）

> 本节是 v4.18 增量记录；上文各节的 v4.x 规模、「二十一类不可混引」与各版「仍未收」均为**历史口径**，保留不改。

- **v4.18 规模**：**30 张主卡 + 10 张 imports 子卡 + 5 张 labeling 子卡 / 277 条术语（YAML 块 t01–t277）/ 191 条测试用例 / 二十二类来源 / 七套法规编号**。
- **第二十二来源**：**21 CFR Part 101《Food Labeling》**（eCFR 导出 PDF，Prince 16.2，352 页 / 70 书签 / 50 条款 / 7 Subpart / 4 Appendix，页脚 `up to date as of 11/05/2026`，自述 `authoritative but unofficial`），`books/cfr-part101-2026/source-cfr-part101-2026.md`。属**法规正文层**，为全包**第七套独立编号**〔§ 101.xxx〕。⚠ `2026-11-05` 是 eCFR 现行快照日期，**不是修订生效日、不是新规发布日**；条文末尾 FR citation 才是修订出处。与 4-1-25 Edition 年度编纂版不同，不得混称。
- **新增 CAP-30 `food-labeling-requirements`**（来源路由入口）+ `references/capabilities/labeling/` 下 **5 张 RIA++ 子卡**：V01 标签载体与强制信息架构、V02 营养标签与份量基准体系、V03 声称三层闸门与逐词授权、V04 特定品类与强制警示声明、V05 标签豁免体系与效力层元规则（横切层，不单独抢路由）。输入按 cangjie-skill RIA-TV++ 蒸馏：5 个 extractor 并行得 182 个方法类候选 + 44 条术语 → 去重合并 5 单元 → 三重验证 5/5 通过 → 晋级门全部判 router → 93 个英文引用块逐字核验 **93/93 PASS**。
- **补齐的是「标签内容」的法条层空白**：既有包对标签的表述全在 **guidance / Part 117 层**——过敏原 Ed.5（FD&C Act §201(qq)/§403(w)）、〔§ 117.135(c)(2)〕标签控制、CAP-29 的 misbranding 扣留作业。此前从未收录 Part 101 正文。两者分工为「厂内控制怎么管 ↔ 标签内容是什么」，条款号不得互引替代。
- **六类实质纠偏**：① **四套豁免对象不可互替**——〔§ 101.100〕免的是 FD&C Act **403(i)(2) 配料表**要求，营养标签豁免在〔§ 101.9(j)〕，〔§ 101.108〕是 FDA 书面提案获批的临时实验，Part 117〔§ 117.5〕是**主体/活动**豁免；② **标签合规 ≠ 食品安全合规**——403 misbranding 与 402 adulteration 是两条独立执法钩子；③ **暗示也算 claim**——§101.13(b)(2) / §101.14(a)(1) 明列品牌名、heart 符号、vignette、第三方引用；健康声称须 SSA 且不超 disqualifying level；④ **〔§ 101.17(g)〕未巴氏果汁警示 ↔ 〔§ 120.24〕5-log ↔ CP 7303.847 是三层接口**，双向互推都会造成实质病原控制漏洞；⑤ **serving size 由 §101.12 RACC 推导**，是监管比较基准而非厂商建议食用量，也是所有声称阈值的共同分母；⑥ **20 ppm（gluten-free，§101.91）与 10 ppm（亚硫酸盐可检出，§101.100(a)(4)）是不同条款不同判据**，不可混算。
- **二十二类不可混引（v4.18 口径）**：在二十一类之外增加 **21 CFR Part 101 法规正文**。层次仍为：法规正文（**七套编号**〔§ 101 / 108 / 113 / 114 / 117 / 120 / 123.xxx〕）＞ FDA 指南（should 建议层）＞ CPGM／CP／IOM 检查程序（检查员视角、不创设企业义务）。
- **转换与自检**：`.cangjie/convert_part101.py` 按 block 坐标 (y0,x0) 重排，修 Prince 浮动标题错位（默认 `get_text()` 会把 §101.2 标题提前到 §101.1 的 (a)(b)(c) 之前）；书签全标题合并 7 处跨行标题；Subpart F 续行与 Appendix A [Reserved] 补回；清 1,747 行页眉页脚、0 残留；**50/50 条款命中**、7 Subpart、4 Appendix。**9 个纯图形页**（44/45/51/239/240/344/347/348/351）在文本层无字，系 Nutrition Facts 图形示例，已标注不可引。
- **不可逐字引用区**：§101.12 Table 1 / Table 2（约 113 页流式列值、表头脚注逐页重复、列可能错列）、Appendix B 图形增强 / C 生鲜果蔬 / D 熟鱼 Nutrition Facts 图形、§101.9 sample label 图形页。只可引「产品类别 → RACC → label statement」对应关系，数值与版式回原表核对。
- **仍未收**：FD&C Act 全文、FALCPA 法定过敏原定义本体（§201(qq)/§403(w)）、21 CFR part 1 subpart L / 102 / 130 / 105.66 / 110、§104.20 强化政策、1 CFR part 51 并入材料、AOAC / 检测方法正文、请愿表格栏目、营养数据库与消费调查原始文献、IOM Chapter 2/3/7/8/9/10、CPG 全套、Import Alert 全文、BAM 方法全文。涉及这些法源一律标「转引未收」。
- **审计轨迹**：`E:/WeChatData/2026-11-09-15-05-22/books/cfr-part101-2026/`（BOOK_OVERVIEW / PIPELINE_STATE / verified / rejected / candidates / verified.yaml / destinations.json / GLOSSARY / DIGEST / cards / test-results / backups）。

---

## v4.19 追加：第二十三来源 21 CFR Part 172（直接食品添加剂法规正文）

> 本节是 v4.19 增量记录；上文各节的 v4.x 规模、「二十二类不可混引」与各版「仍未收」均为**历史口径**，保留不改。

- **v4.19 规模**：**31 张主卡 + 10 张 imports 子卡 + 5 张 labeling 子卡 + 5 张 additives 子卡 / 318 条术语（YAML 块 t01–t318）/ 204 条测试用例 / 二十三类来源 / 八套法规编号**。
- **第二十三来源**：**21 CFR Part 172《Food Additives Permitted for Direct Addition to Food for Human Consumption》**（eCFR 导出 PDF，Prince 16.2，178 页 / 198 书签 / **154 条款** / 9 Subpart，页脚 `up to date as of 11/05/2026`，自述 `authoritative but unofficial`）。
- **新增 CAP-31 `direct-food-additives`**（来源路由入口）+ `references/capabilities/additives/` 下 **5 张 RIA++ 子卡**：V01 许可判定链与限制五形态、V02 防腐剂与抗菌剂、V03 甜味剂与脂肪替代物、V04 品质功能类与长尾名录导航、V05 效力层与 IBR 边界（V05 为横切口径层，不单独抢路由）。
- **补齐的是「某物质是否被许可、上限多少」这一法条层空白**：既有包对添加剂的表述全在**危害/控制层**——化学危害识别（CAP-06）、CGMP（CAP-14）、工艺控制（CAP-03）、标签内容（CAP-30 / 21 CFR Part 101）。此前用户问「我们这个防腐剂能不能用在焙烤食品里、上限多少」时，包里只能讲控制原则，给不出许可依据。
- **本件的方法层核心**：Part 172 不是原则型法规，而是**逐物质许可清单（per-substance positive list）**。154 条几乎按同一模板展开（Identity → Specifications → Use/Limitations → To assure safe use），因此可用**一条判定链覆盖全部条款**：① 定位条款；② 判食品是否落在用途范围（`specified foods` 封闭清单）；③ 判**限制五形态**（数值上限 **80** / 仅 GMP **34** / 仅限食品 **8** / 功能限定 **11** / 无限制语 **21**）；④ 判用量是否在限值内（无数字则受 §172.5(a)(1) 合理需要量约束）；⑤ 判纯度是否满足规格（含 IBR 引用）。
- **六类实质纠偏**：① **有条款 ≠ 有剂量上限**——仅 52% 条款给 ppm/百分比，其余靠 GMP/食品范围/功能/总则兜底，无数字时不得凭空编造上限；② **有 ppm ≠ 全食品适用**——数值上限与食品范围是两条独立闸门；③ **限值作用点不固定**——可能测中间品（麦芽 75 ppm 溴酸盐）、成品（啤酒 25 ppm 溴化物）或法定取样部位（`as measured in the loin muscle`），同物质多来源须累计（`total BHA and BHT`、`in combination`、§172.730(a)(2) 他源同类残留）；④ **用途锁定靠逐字法定标签措辞**（§172.730(c) `Brewer's Malt—To be used in the production of fermented malt beverages only`），自拟无效；⑤ **IBR 只可引「须符合某文件某版某页」**——43 条（27%）规格整体外转，转述其内部数值即编造法规（FCC 7th ed.=2010 / 9th ed.=2014）；⑥ **添加剂被许可 ≠ 产品安全合规**——§172.5(b) 许可是许可层的合规、§172.5(c) 营养物质许可不是有用性认定。
- **二十三类不可混引（v4.19 口径）**：在二十二类之外增加 **21 CFR Part 172 法规正文**。层次仍为：法规正文（**八套编号**〔§ 101 / 108 / 113 / 114 / 117 / 120 / 123 / 172.xxx〕）＞ FDA 指南（should 建议层）＞ CPGM / CP / IOM 检查程序（检查员视角、不创设企业义务）。
- **转换与自检**：`.cangjie/convert_part172.py` 按**词级坐标**（word coordinates）重建表格——Part 172 的价值集中在表格（`食品 → 限量 ppm`、`Component → Limitations`），逐行文字块会把表格行压成一整块，故改用 `get_text("words")` 按 y 容差聚行、再按水平空隙 > 20 pt 切格（实测列间空档 44–327 pt，词内空隙 < 10 pt）。成果：**154/154 条款命中、16 张表格重建、0 噪声残留、174/178 页保留**。校验器 `.cangjie/verify_part172_quotes.py`：候选池 + 6 张卡 **142/142** 逐字命中、术语 41/41 命中。
- **不可逐字引用区**：16 张重建表格的数值（词级坐标启发式重建，跨页续表与 `Do.` 行有归属歧义）、§172.510（366 行）/ §172.515（834 行）名录内部行、全部 IBR 引用的外部规格文件内容（FCC 页码、厂商方法、ATCC 菌株资料）。
- **仍未收**：FD&C Act 全文、21 CFR Part 170（添加剂请愿程序）/ 171 / 175–178（间接添加剂）/ 180（临时许可）/ 182 / 184 / 186（GRAS）/ 102（通用名）/ 105（特殊膳食）、1 CFR part 51、FCC 各版正文、9 CFR 430.1、40 CFR 725.421(d)、AOAC / 厂商检测方法正文、ATCC 菌株资料。
- **审计轨迹**：`E:/WeChatData/2026-11-09-15-05-22/books/cfr-part172-2026/`（BOOK_OVERVIEW / PIPELINE_STATE / source-cfr-part172-2026.md / candidates / verified.md / rejected / .cangjie/capabilities/{destinations.json,verified.yaml,cards} / GLOSSARY.md / test-results/phase4-cases.json），备份 `backups/fda-pchf-food-safety-v4.18-20261110-104537`。

---

## v4.20 追加：第二十四来源 21 CFR Part 121（蓄意掺假防护法规正文）

> 本节是 v4.20 增量记录；上文各节的 v4.x 规模、「二十三类不可混引」与各版「仍未收」均为**历史口径**，保留不改。

- **v4.20 规模**：**32 张主卡 + 10 张 imports 子卡 + 5 张 labeling 子卡 + 5 张 additives 子卡 / 327 条术语（YAML 块 t01–t327）/ 212 条测试用例 / 二十四类来源 / 九套法规编号**。
- **第二十四来源**：**21 CFR Part 121《Mitigation Strategies to Protect Food Against Intentional Adulteration》**（eCFR 导出 PDF，`up to date as of 11/20/2026`，11 页 / **20 条款** / 5 Subpart（Subpart B 为 Reserved），页脚自述 `authoritative but unofficial`；SOURCE `81 FR 34219, May 27, 2016, unless otherwise noted`；Authority `21 U.S.C. 331, 342, 350g, 350(i), 371, 374`）。上位授权为 FD&C Act **§420**（FSMA §106 增订）。
- **新增 CAP-32 `intentional-adulteration-defense`**（**单卡，不拆子卡**：20 条款体量远小于 Part 172 的 154 条，判定链单一，拆子卡只会分散路由）。
- **补齐的是「整块法规缺席且未声明」的缺口**：v4.19 及以前全包对 Part 121 的命中为 **0**——`Part 121`、`intentional adulteration`、`mitigation strateg`、`脆弱性`、`vulnerability`、`insider`、`actionable process step`、`食品防护`、`蓄意` 均无任何出现，且边界段也**未登记为「转引未收」**。这比「声明未收」更危险：技能会硬答而不说超出范围。
- **本件的方法层核心**：Part 121 与 Part 117 **条款编号结构同构、判定对象相反**（121.126↔117.126 计划、121.130↔117.130 评估、121.135↔117.135 控制、121.138↔117.135(c)/140 管理组件、121.140↔117.145 监控、121.145↔117.150 纠正、121.150↔117.165 验证、121.157↔117.170 再分析、121.301–330↔117.3xx 记录、121.401↔117.1 合规）。正因编号相近，最危险的错误是**按编号类推**；本卡的处理是强制按判据差异记忆：117 问「危害是否显著」，121 问「**脆弱性**是否显著」。
- **六类实质纠偏**：① **食品防护 ≠ 食品欺诈（EMA）**——EMA 以牟利为目的、不要求造成大规模公共卫生危害，归 CAP-06，条款号绝不可互引；② **〔§ 121.5(b)〕holding 豁免不含液体储罐**——只做储存的罐区仍受管辖，最高频误答；③ **〔§ 121.130(c)〕`Regardless of the outcome`**——每个点/步骤/程序都要双向书面说明，判 No 留空等于未评估；④ **〔§ 121.305(g)〕part 11 是豁免不是禁止**，且只覆盖「为满足本 part 而建立」的记录，同时受其他法源要求者仍适用；⑤ **两个 2 年、两个 3 年对象不同**（记录 2 年 vs 计划停用后 2 年；再分析 3 年 vs 极小企业销售窗口 3 年）；⑥ **〔§ 121.401〕两个钩子按原文形态引用**——(a) 引 §418/§301(uu)、(b) 引 §420/§301(ww)，本卡不推断是否笔误，执法申辩场景引用前须回 eCFR 与 FD&C Act 核对。
- **二十四类不可混引（v4.20 口径）**：在二十三类之外增加 21 CFR Part 121 法规正文。层次仍为：法规正文（**九套编号**〔§ 101 / 108 / 113 / 114 / 117 / 120 / 121 / 123 / 172.xxx〕）＞ FDA 指南（should 建议层）＞ CPGM / CP / IOM 检查程序（检查员视角、不创设企业义务）。
- **抽取与自检**：源件为用户提供的 eCFR 导出 PDF（`G://下载//21 CFR Part 121 (up to date as of 11-20-2026).pdf`，131 KB / 11 页），用 pdf-inspector v1.27.0 提取（`TextBased`，confidence 1.00，`pagesNeedingOcr` 为空），按「去页眉页脚 `page N of 11` + 去 `<u>` 标记 + 压空白」归一化后核验：卡片 **20 段引文块 / 24 个可核片段，24/24 逐字命中，0 未命中**（4 段过短片段跳过）；条款覆盖 **20/20**（121.1、121.3、121.4、121.5、121.126、121.130、121.135、121.138、121.140、121.145、121.150、121.157、121.301、121.305、121.310、121.315、121.320、121.325、121.330、121.401）。
- **不可逐字引用区**：本件无表格、无 IBR 外部文件；唯一需谨慎处是 §121.401 的交叉引用形态（见纠偏⑥）。
- **仍未收**：FDA Food Defense Plan Builder 工具、Mitigation Strategies 相关指南文件、CARVER + Shock 等方法学、DHS 风险评估内容、食品防护专项检查程序（CP）、21 CFR 1 subpart H（注册）与 FD&C Act §420/§301(ww) 正文、CPG 全套、Import Alert 全文、IOM Chapter 2/3/7/8/9/10、BAM 方法全文、part 110、part 1 subpart L。
- **测试**：新增 8 条用例（4 `should_trigger` / 2 `edge_case` / 2 `should_not_trigger`），钉住液体储罐例外、三要素与内部人员、APStep≠CCP、计划须留现场与 24 小时、极小企业三要素口径、EMA 分流，以及两条负例（专项 CP 未收、Part 117 义务不得记为 121）。
- **审计轨迹**：源件 `G://下载//21 CFR Part 121 (up to date as of 11-20-2026).pdf`；提取件 `E:/WeChatData/2026-11-04-09-51-05/.tmp-research/part121/part121.md`（232 行）；核验脚本口径见上条。

---

## v4.21 追加：第二十五来源 21 CFR Part 1 Subpart L（FSVP 法规正文）

> 本节是 v4.21 增量记录；上文各节的 v4.x 规模、「二十四类不可混引」与各版「仍未收」均为**历史口径**，保留不改。

- **v4.21 规模**：**33 张主卡 + 10 张 imports 子卡 + 5 张 labeling 子卡 + 5 张 additives 子卡 / 336 条术语（YAML 块 t01–t336）/ 221 条测试用例 / 二十五类来源 / 十套法规编号**。
- **第二十五来源**：**21 CFR Part 1, Subpart L《Foreign Supplier Verification Programs for Food Importers》**（§§ 1.500–1.514，共 **15 条**，eCFR 导出 PDF `up to date as of 11/20/2026`，**25 页**，页脚自述 `authoritative but unofficial`；Subpart L 的 SOURCE 为 `80 FR 74340, Nov. 27, 2015, as amended at 81 FR 25327, Apr. 28, 2016`）。上位授权为 FD&C Act **§805**（FSMA §301 增订）。
- **新增 CAP-33 `fsvp-statutory-requirements`**（单卡，不拆子卡：15 条、义务链单线、无表格与 IBR）。
- **补齐的是全包被点名最多的一条悬空引用**：v4.20 及以前有 **13 个文件**把「21 CFR part 1 subpart L 正文」标为「转引未收」，而 CAP-21 只有 **CP 7303.878**（检查员侧内部作业指导，明写 `provides instruction to field staff`，不创设企业义务）。结果是：能回答「检查员会索要哪六组记录」，却回答不了「这些记录本来由哪条法规要求、要求到什么程度」。本轮把 6 张卡（CAP-21 及 labeling / imports / inspection-readiness / seafood-inspection 相关段）与 glossary 的相关声明全部翻转为正向引用〔§ 1.5xx〕。
- **本件的方法层核心**：FSVP 的义务链是**六环节单向推进**——判主体〔§ 1.500〕→ 判适用〔§ 1.501〕→ 判标准〔§ 1.502〕→ 做评估〔§ 1.504–1.505〕→ 做验证〔§ 1.506–1.507〕→ 留证据〔§ 1.509–1.510〕。任一环节判错，后面的活动再完备也不成立；尤其**「一份 FSVP 对应一份 food，不是一家供应商」**（〔§ 1.502(a)〕`for each food you import`）。
- **六类实质纠偏**：① **〔§ 1.502(c)〕deemed compliance 明确排除〔§ 1.509〕**——接收设施仍须每一 entry line 报 UFI/DUNS；② **〔§ 1.501(b)〕juice/seafood 的豁免是「换轨」**到〔§ 120.14〕/〔§ 123.12〕，说成「不用做任何事」即实质错误；③ **〔§ 1.506(e)(2)(ii)〕不得依赖供应商本身**执行验证活动（仅抽样检测例外），供应商自检报告不构成验证；④ **极小进口商是双金额制**（人食 <100 万、动物食品 <250 万）、且须计入「未销售部分的美国市场价值」、含关联企业；⑤ **五组「2 年/3 年」对象各不相同**（记录 2 年、程序类停用后 2 年、极小进口商证明 3 年、供应商重评 3 年、保证每 2 年），压成一个数字即错；⑥ **〔§ 1.227〕（farm 定义）不属本 subpart**，是外部锚点。
- **二十五类不可混引（v4.21 口径）**：在二十四类之外增加 21 CFR Part 1 subpart L 法规正文。层次仍为：法规正文（**十套编号**〔§ 1 / 101 / 108 / 113 / 114 / 117 / 120 / 121 / 123 / 172.xxx〕）＞ FDA 指南（should 建议层）＞ CPGM / CP / IOM 检查程序（检查员视角、不创设企业义务）。注意 FSVP 的编号写法是〔§ 1.5xx〕，**不是〔§ 1.xxx〕全段**——subpart L 只到 §1.500–1.514。
- **抽取与自检**：源件 `G://下载//21 CFR Part 1 Subpart L (up to date as of 11-20-2026).pdf`（266 KB / 25 页），pdf-inspector v1.27.0 提取（`TextBased`，confidence 1.00，`pagesNeedingOcr` 为空），去页眉 `page N of 25`、去 `<u>` 标记、压空白后核验：卡片 **25 段引文块 / 26 个可核片段，26/26 逐字命中**；术语 t328–t336 **9/9 逐字命中**；条款覆盖 **15/15**。
- **不可逐字引用区**：本件无表格、无 IBR 外部文件。唯一需注意处：§1.500 的金额门槛是**通胀调整项**，卡片给的 $1M/$2.5M 是条文基数，不等于当年生效数。
- **仍未收**：Import Alert 99-41 全文、FSVP Guidance for Industry、FSVP Implementation Work Instructions / Inspection Protocol guidance tabs、HFP Enforcement Bulletin #13/#6、RPM 4-1-8、21 CFR part 111 / 112 / 507 正文、DUNS 申请与 CBP entry 系统操作、SRA 国别清单内容。
- **测试**：新增 9 条用例（5 `should_trigger` / 2 `edge_case` / 2 `should_not_trigger`），钉住 deemed compliance 的 §1.509 例外、juice/seafood 换轨、供应商自证无效、极小进口商双金额、五组年限不可互换，以及两条负例（检查员侧走 CAP-21、Part 117 Subpart G 走 CAP-07）。
- **审计轨迹**：源件 `G://下载//21 CFR Part 1 Subpart L (up to date as of 11-20-2026).pdf`；提取件 `E:/WeChatData/2026-11-04-09-51-05/.tmp-research/fsvp/fsvp.md`（511 行）；核验口径同上。

---

## v4.22 追加：第二十六、二十七来源 21 CFR Part 1 Subpart S 与 Subpart O

> 本节是 v4.22 增量记录；上文各节的 v4.x 规模、「二十五类不可混引」与各版「仍未收」均为**历史口径**，保留不改。

- **v4.22 规模**：**35 张主卡 + 10 张 imports 子卡 + 5 张 labeling 子卡 + 5 张 additives 子卡 / 356 条术语（YAML 块 t01–t356）/ 二十七类来源 / 十二套法规编号**。
- **第二十六来源**：**21 CFR Part 1, Subpart S《Additional Traceability Records for Certain Foods》**（§§ 1.1300–1.1465，共 **33 条**，eCFR 导出 PDF `up to date as of 11/20/2026`，**26 页**；SOURCE `87 FR 71077, Nov. 21, 2022, as amended at 88 FR 65815, Sept. 26, 2023`）。上位授权为 FD&C Act **§204(d)**（FSMA 增订），执法钩子为 **§301(e)** 与 **§301(hh)**，拒绝入境走 **§801(a)(4)**（本 subpart）——不是 FSVP 的 §801(a)(3)。
- **第二十七来源**：**21 CFR Part 1, Subpart O《Sanitary Transportation of Human and Animal Food》**（§§ 1.900–1.934，共 **21 条**，同批 PDF，**10 页**；SOURCE `81 FR 20166, Apr. 6, 2016`）。掺假定性走 FD&C Act **§402(i)**——这是 Subpart O 独有的钩子，**不要求证明食品实际不安全**，仅需 `may render` 的条件成立。
- **新增 CAP-34 `food-traceability-records`**（单卡，33 条、义务链按六个 CTE 分支、无 IBR）与 **CAP-35 `sanitary-transportation`**（单卡，21 条、四类主体、无 IBR）。
- **补齐的是同一部 Part 1 下最后两块空缺**：v4.21 收到 Subpart L 后，Part 1 在包内只剩 Subpart S / O 两处「转引未收」。二者与 Subpart L **同属 21 CFR Part 1、分属三个不同 Subpart、编号连续且互不覆盖**（L = §1.500–1.514、O = §1.900–1.934、S = §1.1300–1.1465，中间隔着 M–R），因此全包口径由「十套法规编号 / 二十五类」升为**十二套 / 二十七类**，且新增第 11、12 两套编号〔§ 1.13xx/1.14xx〕〔§ 1.9xx〕。
- **本件的方法层核心（Subpart S）**：义务链是**清单驱动 + 事件驱动**——先判食品是否在 FTL 上〔§ 1.1300〕→ 再逐款排 18 项豁免〔§ 1.1305〕→ 再判本主体是不是 FTRI / initial packer〔§ 1.1300〕→ 再判事件属七类 CTE 的哪一类〔§ 1.1325–1.1350〕→ 再定赋号规则〔§ 1.1320〕→ 最后落到记录留存与可得性〔§ 1.1455〕。任一环节判错，后面的记录再全也不成立。
- **本件的方法层核心（Subpart O）**：义务链是**主体 × 合同 × 容器形态**三轴——先判是 shipper / loader / carrier / receiver 中的哪几类〔§ 1.904〕→ 再判是否 non-covered business 而整条不适用 → 再判是否构成完全封闭容器排除（五项回拉先过一遍）→ 最后判 carrier 组义务是否因**与 shipper 的书面合同**而被激活〔§ 1.908(e)〕。
- **七类实质纠偏（Subpart S）**：① **FTL 清单封闭**，不在清单即不受本 subpart 约束，但「不受 CTE 约束」≠「不受本 subpart 约束」；② **18 款豁免（a–r）**而非 21 款，且 (d) 加工后免六款全挂条件；③ **KDE 条数 8/7/7/8/8/9**，另有 initial packing 一般情形 16 项、芽苗菜 +7 项；④ 赋号是**双向规则**（正向三处必须新赋 / 反向禁止新赋 / 收无管辖上家货时补赋），不是「有批号就赋」；⑤ 记录期限有五套（2 年 / 旧计划 2 年 / 部分豁免 2 年 / 协议 3 年续签 / **180 天**）；⑥ **§301(e) 有 `except ... by a farm` 农场例外**，与 §301(hh) 不得混；⑦ **运输商在本 subpart 完全豁免**〔§ 1.1305(n)〕。
- **七类实质纠偏（Subpart O）**：① 管辖覆盖 `whether or not ... enters interstate commerce`；② **non-covered business（<$500,000，revenues、2011 基年）判「管不管」，small business（<500 FTE / 纯 motor carrier <$27,500,000）只是规模分类**；③ 完全封闭容器排除有**五项回拉**；④ **carrier 全部实体义务以书面合同为前提**；⑤ 402(i) 掺假不要求证明食品实际不安全；⑥ 清洁程序是**一份、含三项内容**、且须留现场，(e)(6)(i) 的「现场」要求常被漏；⑦ `promptly` 与 24 小时只适用于**异地取回**，六处「12 个月 beyond」起算点各异。
- **最强的跨卡反向陷阱**：**运输商（transporter / carrier）在 Subpart S 完全豁免〔§ 1.1305(n)〕，在 Subpart O 却是四大义务主体之一**。同一部 Part 1、两个相邻 subpart，方向相反，任何互推都是实质错误。第二处是 **§801(a)(4)**（追溯，本 subpart）≠ **§801(a)(3)**（FSVP，CAP-33）。
- **二十七类不可混引（v4.22 口径）**：在二十五类之外增加 21 CFR Part 1 subpart S 与 subpart O 法规正文。层次仍为：法规正文（**十二套编号**〔§ 1 / 101 / 108 / 113 / 114 / 117 / 120 / 121 / 123 / 172.xxx〕+〔§ 1.13xx/1.14xx〕+〔§ 1.9xx〕）＞ FDA 指南（should 建议层）＞ CPGM / CP / IOM 检查程序（检查员视角、不创设企业义务）。**Part 1 三套编号必须带 subpart 归属**，不得只说「part 1」。
- **抽取与自检**：Subpart S 源件 `G://下载//21 CFR Part 1 Subpart S (up to date as of 11-20-2026).pdf`（26 页）→ 提取件 591 行；卡片 **46 段引文块 46/46 逐字命中且页码一致**；条款覆盖 33/33；术语 t337–t346 **10/10 命中**。Subpart O 源件 `G://下载//21 CFR Part 1 Subpart O (up to date as of 11-20-2026).pdf`（10 页）→ 提取件 244 行；卡片 **35 段引文块 35/35 命中且页码一致**；条款覆盖 21/21；术语 t347–t356 **10/10 命中**。核验口径同 v4.21（`norm()` 归一去 `<u>`/`**`/智能引号/连字符换行 + 折叠空白 + 全线小写）。
- **不可逐字引用区**：两份 PDF 均含目录页（S 第 1 页、O 第 1 页）；S 另有 11 页多栏排版（1/4/7/8/9/11/12/13/15/21/22），O 有 4 页（1/3/7/10），跨栏处不可按视觉行序引。两份来源均无 IBR 外部文件。
- **仍未收**：FDA 网站公布的 Food Traceability List 现行清单内容（清单本身不在法规正文里，只能引「须在清单上」的判定规则，不得编造清单条目）；FTL 增补/删除的 FR 公告；Subpart S/O 的 Small Entity Compliance Guide；CPGM 与 PAC `03040T` 的卫生运输取证问卷内容（检查员侧口径归 CAP-16）；21 CFR part 1 subparts A–K/M–R 其余各 subpart 正文。
- **测试**：新增 18 条用例（10 `should_trigger` / 4 `edge_case` / 4 `should_not_trigger`），钉住 FTL 清单封闭性、18 款豁免数、KDE 条数不可混、赋号双向规则、180 天期限、运输商反向制度、non-covered vs small business、五项回拉、carrier 合同闸门、402(i) 的 `may render` 口径，以及四条负例（检查员侧走 CAP-16、召回走 CAP-08、FSVP 走 CAP-33、Subpart S 运输豁免不得推到 Subpart O）。
- **审计轨迹**：源件如上；提取件 `E:/WeChatData/2026-11-04-09-51-05/.tmp-research/subpartS/subpartS.md`（591 行）与 `.../subpartO/subpartO.md`（244 行）；核验脚本 `checkcard.py` 直接消费能力卡文件，把每个引文块与出处行的 `pdf-page N` 比对。
