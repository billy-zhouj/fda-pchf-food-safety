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

> **第二来源（2026-11-04 增量并入）**：21 CFR Part 117（2025 版）法规正文（Subparts A–G 全量条文，160KB / 3577 行，来源 books/_inbox/21-CFR-Part-117-2025.md）。它是本指南所解释的法规本体，**为最终规则、具法律约束力**，与指南草案的 should 级建议形成权威分层。本文档描述的骨架、术语、批判均以指南为对象；能力卡中标注〔§ 117.xxx〕的内容来自法规正文，负责提供法定义务、法定例外、硬时限与豁免门槛的权威出处。两者冲突时以法规为准。

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

**仍未收（v4.6 当时记录，v4.7 收窄）**：IOM 其余章节（尤其 Ch.4 的 702(b) 分割留样与制样、Sample Schedule Chart 2）、21 CFR part 108 / 110 / 120（**part 113 / 114 正文自 v4.7 起已收、part 123 自 v4.9 起已收**）与 21 CFR 2.10 / 133 / 1240.61 / 507 正文、eBAM / BAM / AOAC / MPM 方法正文、FMD-86 / FMD-147 / SOP-001052 / SOP-000529 / SOP-001642、CPG 全套（含 Sec. 130.100 / 527.300 / 520.200 / 520.300）、RPM、Import Alerts / Import Bulletins 与 Import Alert 99-37/99-38 正文、其他 Compliance Programs（7303.878 / 7303.080 / 7303.842 / 7371.000 / 7321.006 / 7304.019 / 7304.004A / 7309.006）、FDA 483/484/1551 数据库、21 CFR part 117 citations table、SOFO job aid 与 eNSpect / CAR / CMS 内部系统；以及 FDA 境外无预告检查、RRA 适用范围与 FD&C Act 704(a)(4) 检查前索取记录的政策公告原文。

**当时规模**：19 张能力卡 / 142 条术语 / 75 条测试用例（v4.6）；**当前规模见文末 v4.8 节**。


## 版本补充说明（v4.7，第十一与第十二来源：低酸/酸化食品法规正文）

本版把 **21 CFR Part 113（Thermally Processed Low-Acid Foods Packaged in Hermetically Sealed Containers）** 与 **21 CFR Part 114（Acidified Foods）** 两套 **联邦法规正文**（均为 4-1-25 Edition，GPO/eCFR 双栏印刷版；Part 113 共 36 页 / 10 条款，Part 114 共 7 页 / 8 条款）纳入，全文见 `source-cfr-part113-2025.md` 与 `source-cfr-part114-2025.md`，对应第 20 张能力卡 **`lacf-statutory-requirements`（CAP-20）**。这是本包**首次纳入 Part 117 之外的法规正文**：自此法规正文层含〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕**三套独立编号**，并行、不是上下位、也不是新旧替代关系。⚠ `4–1–25 Edition` 是 CFR 年度编纂版次（修订至 2025-04-01），不是 2025 年新规；条文末尾 FR citation 才是修订出处。两份 PDF 会串栏，故用专用 `.cangjie/convert_cfr_part.py` 按「页→左栏→右栏」重排，条款号全部命中，保留印刷断词连字符。

**接口（本卡的核心）**：〔§ 117.1(c)〕`Food covered by specific current good manufacturing practice regulations also is subject to the requirements of those regulations` 给并行依据；〔§ 117.5(d)(1)〕的 Subparts C/G 豁免须同时满足 `required to comply with` **且** `in compliance with` part 113（**条件性**，企业 part 113 不合规时不成立），〔§ 117.5(d)(2)〕把它限定在 **part 113 管辖的微生物危害**；**§117.5 豁免清单列的是 part 123 (b)、part 120 (c)、part 113 (d)，没有 part 114**——酸化食品全程受 Part 117 Subparts B/C/G 约束，〔§ 114.5〕又反向把 `parts 110 and 117` 与本 part 五个 § 一并列为掺假判据。

**企业义务清单（条款级）**：Part 113 的 §113.3(n) 定义（4.6 / 0.85、番茄 pH <4.7 例外）、§113.5 八个判据条款、§113.10 BPCS、§113.40 设备与 NIST 溯源校准、§113.60 容器、§113.81 产品制备、§113.83 scheduled process 与 critical factors、§113.87 杀菌室规程 / product traffic control / **FDA 调阅权**、§113.89 偏差、§113.100 记录；Part 114 的 §114.3 定义与排除项、§114.5 掺假判据、§114.10 BPCS（课程含 pH controls and critical factors in acidification）、§114.80 成品 pH ≤4.6 按时达到并维持 + **酸化不等于免除热处理**（杀 vegetative cells）+ **pH >4.0 须用电位法**、§114.83 scheduled process、§114.89 **三条偏差路径**（含按 part 113 作低酸食品热处理）、§114.90 方法、§114.100 记录。

**两处必须记住的纠错**：① **Part 110 至今有效**——FDA 2018-09-12 最终规则（FR Doc. 2018-19855）撤回了 2015 规则拟于 2018-09-17 删除 part 110 的 amendatory instruction 13，§114.5 的 `parts 110 and 117` 与 Handbook 的 `21 CFR 110.110` 都不是过时引用，只是**正文本包未收**，须标「转引未收」；手册那句是 §110.110(c) 意译，仍不得标成〔§ 117.110(c)〕。② **两 part 记录保存口径不同**：〔§ 113.100(g)〕1 年厂内 + 另 2 年（合计 3 年）、(h) 允许符合 part 11 的电子记录；〔§ 114.100(e)〕只有整段 3 年，无分段、无 part 11 条款。

**三套数字仍不可互替**：4.6 / 0.85 / 4.0（法条层）｜4.40 / 4.65 / 4.75 / 0.90 / 0.93 / 1% / 24 罐（CP 7303.070 检查员实验室触发线）｜≤4.4 / ≤0.92（L.mono 草案建议层）。全包 v4.7 时统一「十二类不可混引」、**v4.8 起统一「十三类不可混引」**；检查员作业指导（CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / CP 7303.878）不创设企业义务，与 CAP-19 分工为「本卡＝法条义务层，CAP-19＝检查员作业层」。

**仍未收**：21 CFR part 108 / 110 / 120 正文（part 123 自 v4.9 起已收，见 CAP-22）、F0/D/z 计算与温度分布/热穿透研究设计、卷边解剖判读、商业无菌验证方案审批、BAM / AOAC / MPM 方法正文、IOM Ch.4 Sample Schedule Chart 2、CPG 全套、Import Alert 全文、其余 Compliance Programs（7303.842 / 7303.847 / 7303.819 等；**7303.878 已由 v4.8 收入**）、Form 2541e 细则。

**当时规模**：20 张能力卡 / 152 条术语 / 85 条测试用例（v4.7）；**当前规模见下节 v4.8**。


## 版本补充说明（v4.8，第十三来源：CP 7303.878 FSVP 检查程序）

本版把 **FDA Compliance Program 7303.878《Foreign Supplier Verification Programs Inspections》** 纳入为第十三来源，全文见 `source-cp-7303-878-2023.md`，对应第 21 张能力卡 **`fsvp-inspection-program`（CAP-21）**。PDF 首页 `Transmittal Number: 2023-CPM-CFSAN-003` / `Implementation Date: 09/27/2023` / `Date of Issuance: 08/28/2025`；Change History 显示 2025 条目**只改 POC 与机构名称缩写**，故本件是 **2023-09-27 版程序的 2025-08-28 更正版**，不是 2025 新 program，也不是 CPGM 7303.040 那种新 Transmittal 形态。33 页 / 20 书签全命中，转换后清除 62 行重复页眉。

**它是什么、不是什么**：这是 FDA 给检查员、进口分区合规官与中心审评人员的**内部作业指导**（`provides instruction to field staff`），标注「CP 7303.878 PART x」，**不创设企业义务**。真正创设义务的是 FSMA §301 增订的 FD&C Act §805 与其下的 **21 CFR part 1, subpart L（§§1.500–1.514）FSVP 法规**——**该法规正文本包未收，一律标「转引未收」**，不得从 CP 的检查动作反推条文。引用时四层要分开：法规义务〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕｜FSVP 法规「21 CFR part 1 subpart L §1.5xx（转引未收）」｜CP 内容「CP 7303.878 PART x」｜其余 program 各自章号。

**与 Part 117 Subpart G 的分流（本卡价值所在）**：两套法源、两类主体——FD&C Act §805 / part 1 subpart L 管进口商 **FSVPI**（§1.500 定义：入境时的美国货主/收货人；无美国货主时由签署同意书的美国代理/代表承担），FD&C Act §418 / Part 117 Subpart G 管 **receiving facility**。CP PART II.3.A 的 **deemed compliance** 仅在进口商同时为 manufacturer/processor 且符合 Part 117 / 507 供应链要求时成立，且原文 `except they must comply with section 1.509` 把**每一 entry line 报关时电子提供名称、邮箱与 UFI（FDA 认可 DUNS）**的义务单独留下；纯贸易进口商没有该通道。回答「已做 Part 117 供应链验证，还要不要做 FSVP」必须先问主体身份，不能二值合并。

**检查口径与执法阶梯**：§1.502(a) 对每一种食品 develop, maintain, and follow FSVP；standard requirements（§1.502/1.503/1.504/1.505/1.506/1.508/1.509/1.510）与 modified requirements（§1.507/1.511/1.512/1.513）是**可选关系**（满足 modified 条件者仍可选择 standard），不是「少做一套」；§1.501(b)–(h) 八类豁免。CP PART III.1.C 明写 **`Samples will not be collected as part of an FSVP inspection.`**、PART IV 四节 Intentionally Left Blank——FSVP 检查查 FSVP、危害分析、供应商批准评价、验证活动、§1.509 与纠正措施**记录**，不得套 CP 7303.050 的 subs 样品量与环境拭子。PART V 给 483a 观察分级 → NAI/VAI/OAI → Warning Letter / **Import Alert 99-41** / FD&C Act §801(a)(3) 拒绝入境（§301(zz) 禁止行为）。⚠ **99-41 是 FSVP 不合规进口商名单，不是 CP 7303.070 的 99-37 / 99-38**（LACF/AF 备案与过程控制）；99-41 按「具体食品 + 具体境外供应商组合」列 Red List，未列组合在不受其他 Alert 约束时仍可进口，移除须按指示提交证据并先于再次进口；direct reference authority 仅在有限情形授予，首次违法不默认优先执法；§1.507 disclosure 不能替代 §801(b)/§1.95 整改提案资料。

**十四类不可混引（v4.9 口径；v4.8 时为十三类）**：21 CFR Part 117 / PCHF 行业指南 / L.mono Draft Guidance / SECG / 过敏原 Ed.5 / Food Defect Levels Handbook / CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / 21 CFR Part 113 / 21 CFR Part 114 / CP 7303.878 / **21 CFR Part 123**。检查员作业指导一律不创设企业义务；shall/must 的法定义务只回法规正文。

**仍未收**：21 CFR part 1 subpart L 正文、Import Alert 99-41 全文、FSVP Guidance 与 IP guidance tabs、HFP Enforcement Bulletin #13/#6、RPM 4-1-8、CP 7303.819 / 7303.842 / 7303.847 正文、21 CFR part 108 / 110 / 120 / 507 正文（part 123 自 v4.9 起已收）、IOM Ch.4、BAM / CPG 全套。v4.8 **未重跑**触发 / 输出 / 路由评测，v4.7 的评测结论不得冒用。

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

**规模（v4.9 历史快照）**：22 张能力卡 / 172 条术语 / 105 条测试用例 / **十四类来源**（v4.9）。**当前 v4.10 为 23 张能力卡 / 182 条术语 / 115 条测试用例 / 十五类来源 / dist-v14**，见文末 v4.10 节。

**本版未重跑评测**：v4.7 的 F1 1.000 / 0.994、输出 10/10、路由 40/40 均为历史结论，不得冒用；10 条 `seafood-*` 与新卡路由待测。


## v4.10 追加：第十五来源与第 23 张卡

> 本节是 v4.10 增量记录；上文各节的 v4.x 规模与「十四类不可混引」为**历史口径**，保留不改。

- **当前规模**：23 张能力卡 / 182 条术语 / 115 条测试用例 / **十五类来源** / `dist-v14`。
- **第十五来源**：FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版 June 2022（SGR 129），`source-seafood-hazards-guide-2022.md`。它是**非约束性技术指南层**，与第十四来源 21 CFR Part 123（法条义务层，CAP-22）配对而非合并：前者给「怎么判定」，后者给「必须做什么」。
- **新增能力卡 CAP-23 `seafood-hazards-controls-guide`**：完整危害分析判定链（Ch.3 三表识别 → Ch.4–21 理解危害 → 无控制条件下判 `reasonably likely to occur` → 六栏工作表 Yes/No 理由 → Step 11 判定树定 CCP → 控制策略示例 → 关键限值与监控四问）。R 段 37 个英文引用块经 `.cangjie/verify_v4_10_quotes.py` 逐字核验 37/37 命中。
- **十五类不可混引（v4.10 口径；v4.9 时为十四类）**：在上文十四类清单之外，增加 **FDA 海产品危害与控制指南第 4 版**。层次仍为：法规正文 ＞ FDA 指南 ＞ CPGM／CP／IOM 检查程序（仅检查员视角）。指南内引用写「Seafood Hazards Guide 第 4 版 Ch.x / Appendix x / L####」，法条写〔§ 123.xxx〕，不可互换。
- **仍未收**：CP 7303.842、NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、Import Alert 16-xx、BAM 海产品章节，以及 Appendix 5 回指的 CPG / 21 CFR 556 / 40 CFR 180 / Import Tolerance 等外部法源。涉及具体数值的条款级结论一律标「转引未收」。
- 阶段 0 整书理解见 `BOOK_OVERVIEW-seafood-hazards-guide-2022.md`；阶段 1 五路候选见 `candidates/v4-10-*.md`；完整变更与校验记录见 `PIPELINE_STATE.md` v4.10 段。
