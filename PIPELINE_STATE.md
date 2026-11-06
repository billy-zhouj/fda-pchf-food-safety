# PIPELINE_STATE — fda-pchf-human-food-guidance

- **书名**: Draft Guidance for Industry: Hazard Analysis and Risk-Based Preventive Controls for Human Food (Full Guidance)
- **作者**: U.S. FDA, Center for Food Safety and Applied Nutrition (Office of Food Safety)
- **主来源**: books/fda-pchf-human-food-guidance/source.md (1.66MB, 19461 行)
- **第二来源**: books/_inbox/21-CFR-Part-117-2025.md（21 CFR Part 117 法规正文，2025）
- **第三来源**: books/fda-pchf-human-food-guidance/source-lmono.md（FDA《Control of Listeria monocytogenes in Ready-To-Eat Foods》Draft, 2017-01，212KB / 3128 行，21 章 + 5 附录）
- **第四来源**: books/fda-pchf-human-food-guidance/source-secg.md（FDA《What You Need to Know About the FDA Regulation: 21 CFR Part 117 — Small Entity Compliance Guide》, **October 2016**, Docket FDA-2011-N-0920；由 WorkBuddy 资料库文档转换，15 章 / 107KB）
- **第五来源**: books/fda-pchf-human-food-guidance/source-allergen-ed5.md（FDA 食品过敏原标签问答 Ed.5，2025-01 修订终版；27 页 / 68 书签）
- **第六来源**: books/fda-pchf-human-food-guidance/source-defect-levels-handbook.md（FDA《Food Defect Levels Handbook》网页正文，页面标注 Content current as of 09/07/2018；由用户提供 MHTML 转出，111 个产品 / 173 条行动水平）
- **第七来源**: books/fda-pchf-human-food-guidance/source-cpgm-7303-040-2025.md（FDA CPGM 7303.040 现行版 `2025-CPM-HFP-001`，签发 08/29/2025，IMPLEMENTATION DATE 05/23/2024，50 页 / 91 书签；用户提供 508-Compliant PDF 经 `pdf2md-pro` 转换）。已废止的 `2020-CPGM-CFSAN-003`（47 页）留作历史对照：source-cpgm-7303-040-2020.md
- **第八来源**: books/fda-pchf-human-food-guidance/source-cp-7303-050-2025.md（FDA CP 7303.050《Sampling for Foodborne Biological Hazards and Filth – Domestic and Import》，**Date of Issuance 06/03/2022 / IMPLEMENTATION DATE 06/03/2022 / Correction date 09/10/2025**，62 页 / 75 书签；用户提供的 508-Compliant PDF 经 `pdf2md-pro` 转换。是 2022 版程序的 2025 更正本，不是 2025 新 program）
- **第九来源**: books/fda-pchf-human-food-guidance/source-iom-ch5-2026.md（FDA《Investigations Operations Manual 2026》**Chapter 5 – Inspections 单章**，221 页 / 410 书签 / 450 标题；用户提供的官方 PDF 经 `pdf2md-pro` 转换。IOM 其余章节未收）
- **第十来源**: books/fda-pchf-human-food-guidance/source-cp-7303-070-2024.md（FDA CP 7303.070《Acidified and Low-Acid Canned Foods Program – Import & Domestic》，**Date of Issuance 09/26/2024 / IMPLEMENTATION DATE 9/26/2024 / Correction Date 9/26/2025**，61 页 / 40 书签；用户提供的 508-Compliant PDF 经 `pdf2md-pro` 转换。文件名 `20250929` 只是生成日，是 2024 版程序的 2025 更正本，不是 2025 新 program；其依据的 21 CFR part 113 / 114 法规正文自 v4.7 起已收；part 108 / 110 / 120 正文仍未收、part 123 自 v4.9 起已收，见 CAP-22）
- **第十一来源**: books/fda-pchf-human-food-guidance/source-cfr-part113-2025.md（**21 CFR Part 113 — Thermally Processed Low-Acid Foods Packaged in Hermetically Sealed Containers，4-1-25 Edition**，GPO/eCFR 双栏印刷版 36 页 / 10 条款；经本包专用 `.cangjie/convert_cfr_part.py` 按「页→左栏→右栏」重排转出。首次纳入 Part 117 之外的法规正文，标〔§ 113.xxx〕）
- **第十二来源**: books/fda-pchf-human-food-guidance/source-cfr-part114-2025.md（**21 CFR Part 114 — Acidified Foods，4-1-25 Edition**，7 页 / 8 条款；同一双栏脚本转出，标〔§ 114.xxx〕。文件头锁死「parts 110 and 117 不是过时引用、Part 110 至今有效」的纠错）
- **第十三来源**: books/fda-pchf-human-food-guidance/source-cp-7303-878-2023.md（FDA CP 7303.878《Foreign Supplier Verification Programs Inspections》，**Transmittal 2023-CPM-CFSAN-003 / Implementation Date 09/27/2023 / Date of Issuance 08/28/2025 更正**，33 页 / 20 书签；用户提供的 508-Compliant PDF 经 `pdf2md-pro` 转换。是 2023 版程序的 2025 更正本，不是 2025 新 program；其依据的 **21 CFR part 1, subpart L（§§1.500–1.514）法规正文仍未收**，一律标「转引未收」，见 CAP-21 `fsvp-inspection-program`）
- **输出模式**: single（用户已确认，全书均衡提取；十四次来源合并均沿用 single，未改变产物形态）
- **当前版本**: v4.11 ✅ 编译校验并安装完成，10 条新用例与 CAP-24 路由已补测（24 张卡 / 192 术语 / 125 用例 / 十六类来源 / dist-v15）
- **开始时间**: 2026-11-04；最后更新 2026-11-06

## 阶段进度

| 阶段 | 状态 | 产出 |
|---|---|---|
| 0 整书理解 | done | BOOK_OVERVIEW.md + candidates/_stage0/notes-1..6.md（已补 v3.0 来源说明） |
| 1 并行提取 | done | 框架 147 / 原则 285 / 案例 41 / 反例 38 / 术语 84 = 595 条候选 |
| 1.5 三重验证 | done | 框架 54（跨池去重后）+ 原则 76（含 2 条用户捞回）= 130 条通过；78 条淘汰留痕于 rejected/ |
| 1.6 晋级门 | done | 10 个能力聚合（CAP-01..10），single 模式全部经唯一入口路由（destinations.json） |
| 2 RIA 能力卡 | done | 14 张卡（六段完整）+ 14 份 _meta yaml + verified.yaml |
| 3 Zettelkasten | done | also_read 链接（14 卡互联）+ GLOSSARY.md（106 术语）+ book/overview.md |
| 4 压力测试 | done | test-prompts.json v4.0（28 正例 + 5 负例诱饵 + 12 边界用例 = 45 条，darwin 兼容；盲测待补跑） |
| 5 编译交付 | done | DIGEST.md + dist-v4/fda-pchf-food-safety（validate 0 errors / 0 warnings） |

> ⚠ 上表是 **v4.0 阶段快照**（14 卡 / 106 术语 / 45 用例 / dist-v4），保留作阶段轨迹，不代表当前状态。当前为 **v4.11：24 张卡 / 192 术语 / 125 用例 / 十六类来源 / dist-v15**，见本文件顶部与末尾 v4.9 节；v4.8 的 21 卡 / 162 术语 / 95 用例 / 十三类来源 / dist-v12、v4.7 的 20 卡 / 152 术语 / 85 用例 / 十二类来源 / dist-v11、v4.6 的 19 卡 / 142 术语 / 75 用例 / 十类来源 / dist-v10 与 v4.5 的 18 卡 / 134 术语 / 67 用例 / 九类来源 / dist-v9 均已成历史记录。

## 第二至第四来源合并记录

### 第二来源：21 CFR Part 117（2025）
- 增量：57 条新知识、28 条近重复、7 处需修正的指南措辞
- 新建 `exemption-withdrawal-procedure` 卡（CAP-11）：15 日申辩 / 15 日上诉 / 120 日合规 / 10 日裁决及逾期自动撤销
- 修正：§117.136 为五情形、召回计划整体免管理组件、qualified facility 仅免 Subparts C/G、24 小时仅适用异地记录、SAHCODH 年审非默认权利、检测可作为适当验证活动但指南不鼓励其成为唯一手段
- 术语统一：全库「过程控制」→「工艺控制」（133 处），法条语境保留 process control 英文锚点；glossary 新增 t27

### 第三来源：L. mono RTE 指南（Draft 2017-01）
- chunks：294 PCHF + 92 CFR + 203 L.mono = 589；change-set `+203/-0/~386`
- 三个并行提取代理产出：101 条新知识（nA 37 / nB 29 / nC 35）、29 条近重复、14 条矛盾、15 条术语建议
- 候选文件：candidates/_update-lmono/lmono-{A,B,C}-*.md
- **新增 2 张能力卡**（满足晋级门五判据：独立意图/独立契约/独立运行/独立复用；single 模式仍走统一路由，可发现入口仍为 1，未冲击 budget 8）：
  - `environmental-engineering-controls`（CAP-12）：nB-09..nB-28 共 20 条，厂房分区/气流压差/空气过滤/排水冷凝/设备卫生设计/预防性维护/附录 1、2 清单
  - `personnel-hygiene-controls`（CAP-13）：nB-04..nB-08 + nA-08 人员换装部分，手套/鞋履/工服/动线/维修与废弃物接触人员
- 其余 77 条织入 11 张既有卡的对应 Step 与 B 段；9 条 kC-* 矛盾逐条处理
- **四条合并纪律（已落实）**：
  1. 两套 pH/aw 基准并列：4.6 / 0.85（Part 117 酸化管辖与安全水分水平，法定）vs pH ≤4.4 / aw ≤0.92（L. mono 抑制型配方，指南建议层）；同一 0.92 在芽孢萌发视角与李斯特营养细胞视角含义不同
  2. 抑制 ≠ 杀灭：listeristatic <1 log 增幅 vs listericidal <0.04 CFU/g 不可检出（且须绑定方法检出灵敏度）
  3. 工艺闭环之外还有环境闭环：listericidal 后仍可再污染，须与工程/卫生/监测/人员控制成对设计
  4. Draft 效力层：L.mono 正文一律 we recommend（建议层），出现 must 均为引述 Part 117；不得把 5+5 点位、Zone 频次等建议层数值升格为法定义务
- glossary 85 → 100 条（t86–t100）；t64 与 t98 为 COA/COC 通用定义与专项精确定义双轨，已互链
- 测试用例 24 → 36 条（v3.0），新增 lmono-trigger-01..06 与 lmono-edge-01..06

### 第四来源：Small Entity Compliance Guide（SECG, 2016-10）
- 触发：用户把资料库文档 `FDA-SECG-21CFR117-Small-Entity-Compliance-Guide`（node `774yGiPHqcv4yL8lcsHxmb`）交给本包，回应上一轮「cGMP 合规有没有指南」的缺口
- 落地：`.cangjie/convert_secg.py` 把在线文档的 block/mark 标记剥离并合并换行，生成 `source-secg.md`（15 章 / 107KB）；保留两处已知排版错位说明（XIII 章首的项目符号实为 XII 章尾部；XIII.H 正文落在 XIV 标题后），引用以章节标题与条款号为准
- **新增 1 张能力卡**（CAP-14 `cgmp-compliance-guide`）：关闭「cGMP 此前只作法定义务锚点、缺合规判定层」的缺口；六段完整，含四层效力栈、Subpart B 九条「条款—法规结果义务—现场观察点」三列索引、5 个案例、8 步执行要点、9 条边界
- **四层效力栈**：Part 117 法规正文（唯一判定基准）＞ SECG（白话转述、不创设义务、允许替代方案）＞ 专项行业指南（草案建议层）＞ CPG / Compliance Programs（检查视角，非企业义务清单）
- **三处事实口径统一**：SECG 为 **October 2016** 而非 2016-11；80 FR 55907（发布通知首页）与 80 FR 56145（条文部分首页）属同一份 2015-09-17 最终规则；Table 4 合规日期为 2016 过渡安排、现已全部生效
- **沿用既有纪律**：adequate 的〔§ 117.3〕结果义务、豁免切上层不切底层、两条执法钩子（adulterated / prohibited act）、两套 pH/aw 基准不得互替、指南 should 不得写成 must、草案不得当现行法定义务

### v4.1：SECG 逐章通读后回补的三处简化
- 触发：用户要求「把 SECG 逐章讲一遍」。通读 15 章时用法规正文逐条对照，核出 SECG 因面向中小企业而**选择性不展开**的三处，原卡未覆盖
- **简化 1（供应链）**：SECG IX.A 把四类供应商验证活动并列成可选项，未提〔§ 117.430(b)(1)〕的强制现场审核升级（危害暴露后有可能致严重后果/死亡时，唯一适当活动是现场审核，首次使用前做、至少每年一次）、〔§ 117.430(b)(2)〕的 written determination 降级出口、〔§ 117.430(c)(d)(e)〕三类特殊供应商豁免
- **简化 2（qualified facility）**：SECG XI.D 只写「由是变非」一个方向，未写〔§ 117.201(c)(2)(i)(C)〕「由非变是」须当年 7-31 前首次申报；另 Table 2 写 `at least half`，而〔§ 117.3〕与 SECG 自身 XI.A 均为 `exceeded`（超过），以 `exceeded` 为准
- **简化 3（撤销豁免）**：SECG XI.E 止于 15 个日历日答复窗口，未展开〔§ 117.254〕批准层级、〔§ 117.257〕令件内容、〔§ 117.260〕遵守或上诉、〔§ 117.267/117.270〕非正式听证、〔§ 117.277〕决定时限
- **另补一处漏条**：〔§ 117.5(k)(1)〕五类情形**连 subpart B 都不适用**（farm、不受注册要求的渔船、仅存放/运输初级农产品的场所、farm mixed-type 设施中属 farm 定义的活动、仅做坚果去壳干燥包装存放而不烘烤的场所），SECG 仅在 Table 4 脚注 2 一行带过。这是全流程唯一能免掉 CGMP 本身的关口，已写入 Step 1 第②关
- **计数口径修正**：Subpart B 是**九条**，SECG XIII 章只覆盖**八条**（A–H）；第九条 § 117.95 被排在 XIV 章。原卡 I 段「Subpart B 九条按 XIII.A–H 重排」的表述已改为区分两者
- 卡片 29KB → 37.7KB；新增 R 段④三处法规对照引文、A1 案例 6/7、A2 触发 9–12、Step 1 第②关、B10 边界
- glossary 106 → 110 条（t107 强制现场审核升级 / t108 状态双向通知 / t109 撤销豁免程序 / t110 § 117.5(k) 五类不适用）；测试用例 45 → 49 条（v4.1，4 条定向验证三处简化与 § 117.5(k)）
- 引文核对：14 个英文引用块，13 个逐字命中；1 处（〔§ 117.201(c)(2)(i)(C)〕）因本地 CFR 文件中该处引号被 PDF 导入成连写单引号，已加转录说明，措辞与数值未改动
- 条款可回溯：28 个引用条款号全部在 CFR 正文中可查；卡内法规标注 79 处
- 编译产物 `dist-v5`（`dist-v4` 因预览面板占用无法覆盖，改用新目录）；官方校验 **0 errors / 0 warnings**；旧版备份 `backups/fda-pchf-food-safety-v4.0-20261105-114712`
- 组装脚本：SLUGS 13 → 14、ALSO_READ 双向指针、additional_sources 登记第四来源、入口描述与 core_principles / stop_conditions 同步；新增 `source_label` 字段以避免把非原书来源误标成「成员单元 0 个」
- glossary 100 → 106 条（t101–t106：SECG / adequate / current thinking / alternative approach / 80 FR 双页码 / 两条执法钩子）；test-prompts 36 → 45 条（v4.0，6 正例 + 2 边界 + 1 反例）
- 新卡引文核对：10 个英文引用块全部逐字命中来源；18 个条款号全部可在 CFR 正文回溯；40 处〔§ 117.xxx〕标注

## 最终校验（v3.0，历史记录）
- 官方 validate_skill_pack.py：**0 errors / 0 warnings**
- 六段结构：13/13 完整；SKILL.md 路由覆盖 13/13
- 法规条款：328 处〔§ 117.xxx〕标注，引用的 56 个条款号全部可在 CFR 正文回溯
- 英文引文：新增 L.mono 引文关键词 14/14 在 source-lmono.md 命中（严格逐字比对差异来自换行/斜体/引号排版，非实质改写）
- 术语：100 条无重复 id；「过程控制」残留 0
- 旧版本备份：backups/fda-pchf-food-safety-v2.1-20261105-080717
- 安装路径：C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety

## 最终校验（v4.0）
- 官方 validate_skill_pack.py（安装目录）：**0 errors / 0 warnings**；dist-v4 编译期仅 1 条「目录名 ≠ 技能名」warning，安装后消失
- 六段结构：14/14 完整；SKILL.md 路由覆盖 14/14；capability-index 与 cheatsheet 均含 CAP-14
- 新增卡引文：10 个英文引用块逐字命中（SECG 6 / CFR 4，其中 2 块在两份来源均命中）；18 个条款号全部可在 CFR 正文回溯；40 处〔§ 117.xxx〕标注
- 全包元数据：14 份 yaml 的 keywords / intents / also_read / member_units 字段全部为字符串（修复了新卡 `117.10` 等被 YAML 解析成 float 导致编译 TypeError 的问题）
- glossary 106 条无重复 id；test-prompts 45 条（28 正例 / 5 反例 / 12 边界）；「过程控制」残留 0；「13 张」旧表述残留 0
- 编译 run：run-20261105-103309-76dc3a；旧版本备份：backups/fda-pchf-food-safety-v3.0-20261105-103233
- 安装路径：C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety

## 已知边界（未关闭）
- **v4.8 评测状态**：本版**未重跑**触发 / 输出 / 路由评测；v4.7 的 F1 1.000（首次盲测）、F1 0.994（增强触发 103×3）、输出 10/10、路由 40/40 均属**上一版本**结论，不得当作 v4.8 结果。（当时）新增 10 条 `fsvp-*` 用例与 CAP-21 的路由正确性待后续补测 —— **11-06 晚已在 v4.10 产物上补测完成**：10 条 `fsvp-*` 触发 30/30、输出 10/10（严格套件仍 10/10）、CAP-21 路由 33/33，详见 「v4.8 / v4.9 历史用例补测」小节 与 `.cangjie/v4-8-v4-9-legacy-eval-report.md`。
- **评测状态（v4.7 全部补跑完成）**：① 首次触发盲测 85 条适配器用例 → F1 1.000，见 `.cangjie/v4-7-trigger-eval-report.md`；② **补充质量评测**（用户选项「补跑输出与路由评测」）已完成，见 `.cangjie/v4-7-output-routing-eval-report.md`：增强触发套件 103 条 × 3 次重复 = 309 判，官方 score **F1 0.994**（TP 237 / FP 0 / FN 3 / TN 69）、**兄弟混淆率 0.000（0/24，不再是空值）**，新增 8 条 sibling 与 10 条负例；输出质量评测 10 条 × 3 变体（v47 / v46 / 无技能）官方机械断言 **v47 10/10、v46 8/10、无技能 8/10**；能力卡路由评测 20 卡 × 2 轮 **top-1 40/40 = 1.000**。③ 唯一 3 个 FN 全来自 `secg-edge-02`（GB 14881 + 21 CFR 211 跨体系边界），SKILL.md「不适用」已明确排除该场景，属 `edge_case → should_trigger` 映射口径错配而非技能漏触发；按正式套件原始语义计 F1 1.000（仅作敏感性说明，主结果仍 0.994）。④ 仍未关闭：未作统计非劣声明、未做 A/B 偏好盲评与人工复核、未测 also_read 辅读链、路由用例为原型化 prompt、judge 为同一底座模型；正式 `test-prompts.json` 与已安装 v4.7 均未改动
- PCHF 指南 Ch7/8/9/10/13/17 仍未发布；L.mono 指南附录 4/5/6 的表格模板正文未纳入本次蒸馏，需回原始 PDF 取
- L.mono 指南为 2017 年 Draft – Not for Implementation，其建议层内容不得当作现行法定义务引用
- SECG 为 2016-10 的 Guidance for Industry：不创设义务、不是认证、不是可直接签发的逐条内审清单；其 Table 4 合规日期为过渡安排、现已全部生效，不得用作当前时限依据
- IOM **2026 Chapter 5 正文已作为第九来源纳入**（CAP-18），给的是检查员权限、表单、483 措辞纪律与证据固定规则，**不是抽样方法或实验室方法**；**IOM 其余章节仍未收**，尤其 Chapter 4（Sampling，含 702(b) 分割留样、4.2.5 FDA 484、4.3.6.6 环境/产品取样、4.6 报告、4.7 运输）、Ch.3（3.2 权限）、Ch.6（6.4 进口取样 / 6.8.1.4 FSVP）、Ch.7/8/9/10
- **CP 7303.050 正文已作为第八来源纳入**（CAP-17），给的是抽样量、环境拭子、WGS 与逐案执法阶梯，**不是检验方法正文**；eBAM / BAM / AOAC OMA / MPM / Macroanalytical Procedures Manual 方法正文、SOP-001052（原 Field Bulletin 30）、SOP-000529 / FMD-147、CPG Sec. 527.300 与 CPG Ch.5 全套、CPG Sec. 130.100、RPM Ch.6/9/10-4、FMD-86、其他 Compliance Programs（**7303.878 FSVP 正文自 v4.8 起已收（CAP-21），但其依据的 21 CFR part 1 subpart L 与 Import Alert 99-41 全文仍未收** / 7303.080 Produce Safety / 7304.019 / 7303.842 海产品 / 7371.000 动物食品 / 7321.006 婴儿配方等）、Import Alerts / Import Bulletins 与 Import Alert 99-37/99-38 正文、21 CFR 2.10 / 133 / 1240.61 正文、FDA 483/484/1551 数据库、Inspections Database、21 CFR part 117 citations table、SOFO job aid、Human Food By-Products GFI #239 全文、eNSpect / CAR / CMS 内部系统仍未纳入
- **CP 7303.070 正文已作为第十来源纳入**（CAP-19），给的是 LACF/AF 管辖分流、酸化判定、FCE/SID 与 Process Authority 取证、pH/aw 实验室判读与 Import 升级，**不是法规正文**：它依据的 **21 CFR part 113 / 114 两套法规正文自 v4.7 起已收（CAP-20，第十一/十二来源，按〔§ 113.xxx〕〔§ 114.xxx〕引用）**；**仍未收的是 part 108（FCE/SID/Emergency Permit/§108.35）、part 110（至今有效但正文未收）、part 120（part 123 自 v4.9 起已收，见 CAP-22）、BAM Ch.13B/14/17/21A/22A–22D、CPG Sec. 520.200 / 520.300、IOM Ch.4 Sample Schedule Chart 2、SOP-001642、RPM Ch.4/9、Form 2541e 细则**，相关内容一律标「转引未收」；F0/D/z 计算、温度分布与热穿透研究设计、卷边解剖判读、商业无菌验证不在本包内
- 因此**制样与显微判读、检验方法检出限、702(b) 分割留样规则、杀菌工艺计算、证据充分性标准、警告信判定阈值、进口扣留应诉、检查结果预测**仍须另行复核
- **境外无预告检查 / RRA 政策**：IOM 5.2.7 正文口径已收（`the Agency usually announces foreign inspections in advance`、食品企业一般不预告由 program division 裁量、国内预告不少于 5 个日历日、预告不是预约）；**CP 7303.070 PART II.2.B(2) 另给出 RRA 的官方程序性定义**（自愿、全程远程、`RRAs are not considered inspections`、不满足 510(h)/503B(b) 等 FD&C Act 704 条法定检查场景），可作条款级引用；但 2025 年 FDA 扩大境外无预告检查、RRA 适用范围与 FD&C Act 704(a)(4) 检查前索取记录的**政策公告原文仍未收**，只作准备原则提示，不得据 CP 反推政策
- `source-secg.md` 由资料库在线文档转换，存在两处 PDF 分页导入错位与个别连字残留（见文件头与卡片 B7）；引用以章节标题与条款号为准，可疑英文回法规正文核对


## v4.2：过敏原 Q&A Ed.5（2025-01）落为第五来源

- **触发**：此前「已知边界」记为「过敏原 Q&A Ed.5 未纳入」；用户提供官方 PDF `FDA-Guidance-Jan2025-AllergenLabelingQA-12292024.pdf`（27 页 / 68 书签），用 `pdf2md-pro` 转换为 `source-allergen-ed5.md` 后逐字核对，回补进过敏原卡。
- **文件性质**：January 2025 修订终版（revised final guidance），Docket FDA-2022-D-0099，发布公告 90 FR 1133（2025-01-07），合并替代 2022-11-30 同时发布的 Ed.5 草案与终版两份文件。属 FD&C Act § 201(qq)/§ 403(w) 标签解释、guidance 建议层，**不是 21 CFR Part 117 预防控制义务**，禁止标成〔§ 117.xxx〕。
- **核出的四处实质口径**：① 树坚果收成 Table 1 的 12 种封闭清单，未列表者不得进 "Contains" 但仍按通用名进配料表（C.7/C.8）；② milk 扩至牛/山羊/绵羊及其他反刍动物、eggs 扩至鸡/鸭/鹅/鹌鹑及其他禽类，并给出带动物来源的标注写法（C.1–C.4）；③ D.13/D.14：free-from 声明不得与同一过敏原的 advisory 声明同现，已声明者也不得再叠 advisory；做 free-from 即预期连交叉接触残留都不存在；④ D.12 与 Ch11 一致：advisory 不能替代 CGMP 与过敏原预防控制。
- **一处重要纠错**：官方 Ed.5 全文 **`coconut` 出现 0 次**。「椰子不再是主要食物过敏原」是从「仅 Table 1 所列」推出的行业解读（FDA Law Blog、Ohio Dept. of Agriculture、HLC 等二手来源均如此表述），不能说成 FDA 原文；Ed.4（2006）确实曾把椰子列入树坚果清单，旧资料须回 Table 1 复核。
- **对既有卡片的影响**：Big 9 类别（含 sesame）未被推翻，原 B4 仍成立；但类别内物种口径、标签声明互斥、两套法源分界是新增内容。已在 R 段补 3 组英文逐字引文、Step 3/Step 5 补核对点、B 段补边界 7/8/9。
- **改动清单**：`assemble_bundle.py` 登记第五来源 `src-fda-allergen-qa-ed5-2025` 并同步 entry.description / core_principles（+2）/ stop_conditions（+1）；`allergen-program.md` 五处补写；`_meta-allergen-program.yaml` 加 Ed.5 / Table 1 / allergen-free 三个路由关键词；glossary 110 → 113 条（t111–t113）；test-prompts 49 → 52 条（v4.2，3 条定向用例）。
- **转换自检**：68/68 书签命中、表格 27 行、残留独立页码 0、残留 `- Page N` 0；已知局限（个别问答书签标题与正文分离、图片占位、Table 1 跨行 `<br>`）已写入 `source-allergen-ed5.md` 文件头，检索以问答编号为准。


## v4.3：Food Defect Levels Handbook 落为第六来源

- **触发**：此前「已知边界」记为「Food Defect Levels Handbook 正文未纳入」，CAP-14 索引表也注明「本包未收其正文」。用户提供 FDA 官网页面存档 `Food Defect Levels Handbook _ FDA.mhtml`（1.26 MB，Blink 单页 MHTML，快照时间 2026-11-05 08:50 GMT），用新建的 `.cangjie/convert_defect_levels.py` 转为 `source-defect-levels-handbook.md`。
- **文件性质**：这是 FDA 汇编的 **defect action levels 一览与术语表**，属**执法裁量参考**（§ 117.3 定义用 `may regard ... adulterated`），不是法规、不是 Guidance for Industry 的 should 建议层、也不是检查员抽样作业指导；页面标注 Content current as of **09/07/2018**，正文 May 1995 / Rev. 1997-03、1998-05 / 2005-02 两处方法来源更正。
- **核出的关键落差（本次最有价值的发现）**：网页 INTRODUCTION 首句仍写 **`21 CFR Part 110.110`**，但 Part 110 依 2015-09-17 PCHF 最终规则（80 FR 56144）于 **2018-09-17 移除**；现行对应〔§ 117.110〕（Part 117 Subpart B，**仅 (a)(b) 两款**）＋〔§ 117.3〕定义＋〔§ 117.80(b)(3)(4)〕原料要求。手册 "Poor manufacturing practices may result in enforcement action without regard to the action level" 是旧 110.110(c) 的意译，**不得标成〔§ 117.110(c)〕**。另：手册写混合「at or above the current defect action level」不合法，法规写「at levels that render that food adulterated」，以法规为准。
- **其余实质口径**：① action level 不是合规上限、不是平均值、不是内控目标（手册三句原文），真义务是〔§ 117.110(a)〕`must ... lowest level currently feasible`；② 表内无产品或缺陷不契合判据时由 FDA 专家**逐案评估**，不是「无标准即合格」；③ `SIGNIFICANCE` 多为 `Aesthetic`，但 Allspice Whole / Capsicum Pods / Ground Paprika / Cocoa Beans / Coffee Beans Green / Figs / Ginger Whole / Nutmeg Whole 等标 `Potential health hazard - may contain mycotoxin producing fungi`，须联动〔§ 117.80(b)(3)〕与化学危害分析；④ FDA 立场：农药不是预防食品缺陷的替代手段；⑤ 修订以 Federal Register Notices 发布，引用数值前须核对现行版本。
- **改动清单**：新增第 15 张卡 `defect-action-levels`（六段完整，R 段 6 组英文逐字引文）与 `_meta-defect-action-levels.yaml`；`assemble_bundle.py` SLUGS 14→15、登记第六来源 `src-fda-defect-levels-handbook`、also_read 双向补 5 张卡、entry.description +1、core_principles +2、stop_conditions 改写 2 条、引用规范改为「六类不可混引」（当时口径；v4.4 起为七类）、out_of_scope 微调；`cgmp-compliance-guide` 回补 9 处（含「本包未收其正文」→「正文已收」、来源分层四→五类、B8 四者→六类、新增 B11 引用陷阱）；`reference-tools-discipline` / `regulatory-boundaries` 各加 1 条边界；glossary 113→117（t114–t117）；test-prompts 52→55（v4.3，3 条定向用例）。
- **转换自检**：主商品表 293 行 / 111 个产品 / 173 条行动水平 / 111 条 DEFECT SOURCE-SIGNIFICANCE；GLOSSARY 27 词条；2 张表格（主表 + 嵌套的树坚果容许百分比表，后者拆为独立小节）；残留版面 `<br>` 垃圾行 0（仅文件头说明中保留 1 处字面量）；已知局限（rowspan 展开、说明行移列、嵌套表拆出、链接只留锚文本、脚注星号转义）已写入文件头。


## v4.4：CPGM 7303.040 落为第七来源 + 迎检能力卡（检查员视角部分关闭）

- **触发**：此前「应对 FDA 现场检查还缺什么」的结论是「本包是建体系包、不是迎检包」，15 张卡里 `现场检查` / `IOM` / `7303.040` / `Form FDA 482` / `OAI` 全部 0 命中。用户先提供 47 页的 `2020-CPGM-CFSAN-003`，随后提供官方现行版 `CP 7303.040 ... 508-Compliant.pdf`（702 KB / 50 页 / 91 书签），遂把现行版落为第七来源、旧版标为**已废止的历史对照**。
- **版本判定（本次关键纠错）**：现行版首页为 **Transmittal `2025-CPM-HFP-001`、Date of Issuance `08/29/2025`、IMPLEMENTATION DATE `05/23/2024`**；旧版为 `2020-CPGM-CFSAN-003`、10/15/2020、47 页。此前从 FDA 网页 Food Compliance Programs 列表读到的 `5/7/2025` 一类日期与 PDF 首页不一致，属页面字段/更新时间——**以 PDF 首页三项为准**，已写入来源文件头、技能卡与停用条件。FDA 媒体节点 `media/131744` 曾返回 404，最终由用户提供的本地 PDF 解决。
- **逐字核出的 8 处实质变化**：① 观察项分级整体改写（单条观察项 eNSpect 只有 major/minor；整次检查才分 critical/major/minor 且 `investigators do not make this categorization`；再加 OAI/VAI/NAI 分类＝三层）；② `03040U` 从 `PCHF FOLLOW-UP` 改为 `FOCUSED PCHF`，PART III.1.A(6) 同步改写并扩为四类触发；③ 新增 `03040A` / `03S040A`；④ CFSAN/ORA → HFP/OII，新增 HFP OCE、OCIC、DCC、CMS、Compliance Intake and Consultation Form、SOFO job aid、eNSpect IP、CAR、trending OAI；⑤ 483 回复 15 个工作日 + 境外专用邮箱 `FDA483responseinternational@fda.hhs.gov` + 回复影响跟进决定；⑥ 明确 HFP 尚未授予 Direct Reference Authority，所有 advisory actions 须 HFP OCE 会签；⑦ Program Interactions 重排为 17 项现行 program；⑧ OAI 6 个月国内跟进 / OAI 重分类 VAI 1 年复检 / NAI-VAI 按 FSMA 频率。另：PART V.1 明确 OCIC/DCC 流程**暂不适用于境外检查案件路由**；ATTACHMENT A 的卫生运输属 21 CFR 1 Subpart O，与主 PART V 同名章节不同口径；PART III.1.A(4) 有 `quality facility` 笔误。
- **改动清单**：新增第 16 张卡 `inspection-readiness`（六段完整，R 段 20 个英文引用块；含 8 类 PAC 检查类型表、12 行记录举证矩阵、检查当天流程、483 回复骨架、OAI/VAI/NAI 后续、无预告检查准备、B1–B12 边界）与 `_meta-inspection-readiness.yaml`；`assemble_bundle.py` SLUGS 15→16、登记 `src-fda-cpgm-7303-040-2025`、ALSO_READ 双向补 7 张卡、entry.description +1、core_principles +2、out_of_scope 改写、stop_conditions 改写 3 条 +1 条、引用规范改「七类不可混引」；回补 `cgmp-compliance-guide`（7 处，含「检查视角未收全文」→ 已部分补入、六类→七类、新增 B12）、`defect-action-levels` B4/B8、`reference-tools-discipline` 新增第 9 条、`regulatory-boundaries` 新增第 8 条；glossary 117→122（t118–t122）；test-prompts 55→59（v4.4，4 条 `inspection-*` 定向用例）。
- **校验**：20 个英文引用块 / 20 个片段用**滑窗 65 字符 / 步长 50 覆盖整句**逐字命中源文（比此前只验前 60 字符更严）；1 处 PDF 跨行连字符转录丢失（`domestic follow-up` → `domestic followup`）按源文逐字保留并加注，来源文件头也记入转换局限。
- **仍未收**：IOM、RPM、FMD-86、CPG 全套、其他 Compliance Programs、Import Alerts、AOAC / MPM 方法正文、Form FDA 483 数据库、Inspections Database、21 CFR part 117 citations table、SOFO job aid、eNSpect / CAR / CMS 内部系统，以及 FDA 境外无预告检查与 RRA 政策原文。故本次关闭的是「检查类型、分级口径、记录举证路径」，**不是**抽样逻辑、制样判读、证据充分性或警告信/扣留应诉。（此段为 v4.4 当时的边界记录，v4.5 已部分关闭，见下节）


## v4.5：CP 7303.050 + IOM 2026 Ch.5 → 第八/第九来源，迎检链补齐（18 张卡）

- **触发**：11-06 回答「应对 FDA 现场检查还缺什么」时，v4.4 的「仍未收」清单第一项就是 IOM 与其他 Compliance Programs（点名 7303.050）；用户随后一次性提供 `20250915_7303.050_...508-Compliant.pdf`（62 页）与 `2026 IOM Chapter 5.pdf`（221 页）。两份用 `pdf2md-pro`（Python 3.12 `fitz` 回退）分别转出 `source-cp-7303-050-2025.md`、`source-iom-ch5-2026.md`，并各自写了含版本/效力/关键口径/转换局限的文件头。
- **转换自检**：CP 62 页 / 75 书签全命中 / 136 标题 / 253 表格行 / 残留独立页码 0；IOM 221 页 / 410 书签命中 409（丢弃 1 个首页锚点）/ 450 标题 / 259 表格行 / 残留独立页码 0。两份运行时各有一次 Windows 子进程 stdout 的 `UnicodeDecodeError` 警告（pymupdf4llm 内部线程读控制台），不影响输出。IOM 前 11 页为 Word 点线目录，转 GFM 后压成 9 条约 9 KB 单行文本，已在文件头注明「检索以 `5.x.x` 小节号为准，不得以目录行做逐字引证」；CP 首页封面表与 Contents 同样有点线/合并单元格瑕疵。
- **版本判定（本次关键纠错）**：CP 7303.050 首页为 `Date of Issuance 06/03/2022`、`IMPLEMENTATION DATE 06/03/2022`、`Correction date 09/10/2025`（PDF 元数据 creationDate 2025-09-10，作者 HFP/OCE）——**是 2022 版程序的 2025 年更正本**，文件名 `20250915` 不是新签发日期；与 CPGM 7303.040 的 `2025-CPM-HFP-001`（新 Transmittal）不是同一种版本形态。IOM 是 **2026 版 Chapter 5 单章**，不是全书。
- **核出的实质口径（两份合计）**：① CP 7303.050 `Inspections are not planned under this compliance program`——它是抽样 program 不是检查 program，抽样发生在 7303.040 等检查中；② 样品量以 subs 计且 `does not include 702(b) portions`，易腐/进口状态不取 702(b)，多分析物按最大 subs 数取足；③ ATTACHMENT A 环境拭子 **Listeria ≥50（理想 100）/ Salmonella ≥100（理想 300）**、Listeria 主要 Zone 1–3 / Salmonella 主要 Zone 2–3、湿干区目标菌、UPS 24 h / 周一至周四 / 48 ± 2 h 分析窗口、`No enumeration will be performed on environmental swab/sponge samples`；④ 确认阳性一律 WGS + GenomeTrakr，Zone 1/2/3 分离株须与历史/临床株比对；⑤ ATTACHMENT A Part V.1 三档 Findings + `HFP has not given Direct Reference Authority`；PART V 表 7/8 两次声明非穷尽、逐案判断；⑥ **IOM 5.5.10 / 5.5.11.3 的 483 措辞纪律是全包效力分层的制度性反证**：不得引法规原文/纳入标准/引 policy 或 guidance 偏离/写 opinions 或 violative，仅偏离 guidance 的属 Category 3 non-reportable observation；⑦ IOM 5.2.7 预告三层（食品企业一般不预告、境外通常提前告知、国内 ≥5 个日历日、预告不是预约）纠正了 v4.4 只写「无预告政策原文未收」的单向表述；⑧ IOM 5.5.12.3 是 15 个工作日的通用程序出处（与 CPGM PART III.1 双出处，均非法定时限）；⑨ IOM 5.5.12.5 / 5.6.4 / 5.6.5.1 / 5.6.6.1 / 5.6.7 给 FDA 484、样品合格不阻碍 cGMP 指控、唯一副本、电子记录与照片证据规则；⑩ IOM 5.5.2.3 非法定信息拒绝不构成 refusal，境外另有 FD&C Act 807(b) 拒绝入境。
- **改动清单**：新增第 17 张卡 `inspection-sampling`（六段完整，R 段 16 个英文引用块）与第 18 张卡 `investigator-authority-procedure`（六段完整，R 段 27 个英文引用块）及两份 `_meta-*.yaml`；`assemble_bundle.py` SLUGS 16→18、登记 `src-fda-cp-7303-050-2025` 与 `src-fda-iom-2026-ch5`、ALSO_READ 双向补 12 处、entry.description +2 段、core_principles +4、out_of_scope 改写、stop_conditions 改写 3 条 +2 条（七类→**九类不可混引**、16→18 张卡）；回补 `inspection-readiness`（12 处：来源分层、I 段第 7 条、A2 #6/#13、Step 3/6、B4/B5/B6/B9/B10/B12）、`cgmp-compliance-guide`（7 处含新增 B13）、`defect-action-levels`（B4/B8）、`reference-tools-discipline`（新增第 11 条）、`regulatory-boundaries`（新增第 9 条）；glossary 122→**134**（t123–t134）；test-prompts 55→**67**（v4.5，3 条 `sampling-*` + 5 条 `iom-*`）。
- **校验**：43 个英文引用块用「去除空白/Markdown/标点后逐字包含」全量核对，**43/43 命中**（修正 1 处 `When you issue` → `When issuing`）；18 份 meta yaml 的 keywords/intents/member_units 全为字符串；glossary 新增段单独解析 YAML 合法（全库 fenced yaml 块自 v1 起有历史遗留的 t03 解析错误，作为 markdown 交付不参与校验）；67 条用例 id 无重复。
- **编译产物**：`dist-v9`（run `run-20261106-112136-89eead`，single / 18 卡 / 23 个发布文件）；暂存目录校验 0 errors + 1 warning（`name-dir`：`dist-v9` 与 `SKILL.md` 的 `name` 不同，属产物目录名固有提示）；安装后官方 `validate_skill_pack.py` **0 errors / 0 warnings**；旧版备份 `backups/fda-pchf-food-safety-v4.4-20261106-112234`；已安装到 `C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety`（`.cangjie/install_v6.py`），产物与安装目录逐文件 sha256 一致，18 卡 / 134 术语 / 67 用例。完整记录见 `.cangjie/v4-5-sources-qa-report.json`。
- **仍未收**：见上节「已知边界（v4.5 重写，v4.6 再更新）」。本次关闭的是「抽样量与环境拭子、阳性升级阶梯、检查员权限与表单、483 措辞纪律、证据固定规则、预告口径」，**不是** IOM Ch.4 的 702(b)/制样、实验室方法检出限、CPG/RPM/Import Alert 正文或警告信判定阈值。


## v4.6：CP 7303.070 落为第十来源 + LACF/AF 管辖分流卡（专属体系迎检补位）

- **触发**：上一轮 v4.5 的「仍未收」清单点名 `7303.070 低酸/酸化`；用户提供 `G:/下载/20250929_CP 7303.070 Acidified and Low-Acid Canned Foods Program 508-Compliant.pdf`（652 KB / 61 页 / 40 书签）。用 `pdf2md-pro` + Python 3.12 转出 `source-cp-7303-070-2024.md`（133 KB / 1130 行 / 96 标题 / 162 表格行 / 40 书签全命中 / 残留独立页码 0），并写了含版本、效力、关键口径与转换局限的文件头。转换运行时出现过一次 Windows 子进程 stdout 的 `UnicodeDecodeError` 告警，不影响产物。
- **版本判定（又一次纠错）**：首页 `Date of Issuance 09/26/2024` / `IMPLEMENTATION DATE 9/26/2024` / `Correction Date 9/26/2025`；PDF title 也写 `(Implementation Date: 09/26/2024)`，creationDate 2025-09-29。文件名 `20250929` **只是生成日**，本件是 **2024 版程序的 2025 更正本**，与 CP 7303.050（2022 签发 / 2025-09-10 更正）同形态，不同于 CPGM 7303.040 的 `2025-CPM-HFP-001` 新 Transmittal。
- **本轮最有价值的发现：PART II.2.C 是 FDA 官方写明的 program 分工与 §117.5(d)(2) 检查员解释**。① LACF 受 Part 117 约束，但 Subparts C/G 不适用于 part 113 覆盖活动，且〔§ 117.5(d)(2)〕限定**仅豁免 part 113 管辖的微生物危害**；未被热处理控制且需 PC 的危害（`S. aureus` 生长产毒、化学、物理）仍归 C/G。② **酸化食品不在该豁免内**：`Acidified foods are subject to the CGMP & PCHF rule`，PCHF 覆盖转 7303.040，检查重点仍在 part 108/114（不论规模）。③ ⚠〔§ 117.201〕是 **qualified facility 的 modified requirements**，不是 LACF 条款——曾一度误判为 LACF 接口，核对 CFR 正文后纠正，并写入停用条件「LACF/AF 管辖判定三禁」。④ `Keep Refrigerated` 免 113/114 → 7303.050；brites 中央仓 → `PAC 03040`。⑤ **PART II.2.B(2) 给 RRA 官方程序性定义**：自愿、远程、`RRAs are not considered inspections`、不满足 510(h)/503B(b) 等 704 条法定检查场景——补上了此前「RRA 政策原文未收」的一半，但仍不等于 FDA 政策公告原文。
- **其余核出的实质口径**：法源三角 part 108（FCE 注册 / SID 备案 / Emergency Permit）、113、114 正文**未收**；酸化判定三步（酸成分+水 → 加低酸成分研磨测 `Maximum Equilibrium pH` → 送 HFP 邮箱判 significant difference，ROP 阈值 OTR <10,000 cc/m²/24h at 24°C，企业自判至少 6 单元）；AF / LACF / Aseptic LACF 三类检查目标与六组取证记录；pH 分析 ≤795 g 取 24 罐、其余 12 罐；**4.40 / 4.65 双分析师触发线与 `Never average the two analysts' results together`**、异常罐 >1% 与 pH >4.75 肉毒毒素/PCR、14 天 progressive decomp、C. botulinum 仅 for-cause（PAF `MIC`）；**Import Alert 99-37/99-38 与「不得仅因未注册/未备案建议 DWPE」的反直觉限制**、FCE/SID 在 FURLS / Center Views 核验与 DTR；检查优先级 3/6/12 个月与 24 小时通电；PAC 03070A/B/C/F/G/J 与 71070、PAF ACD/MIC。
- **改动清单**：新增第 19 张卡 `lacf-inspection-program`（六段完整，R 段 **25 个英文引用块全部逐字命中正文**）与 `_meta-lacf-inspection-program.yaml`；`assemble_bundle.py` SLUGS 18→19、登记 `src-fda-cp-7303-070-2024`、ALSO_READ 双向补 9 处、entry.description +1 段、core_principles +3、out_of_scope 改写 2 条、stop_conditions 改写 4 条 +2 条（**九类→十类不可混引**、18→19 卡）；回补 8 张既有卡共 **31 处**（`inspection-readiness` 11、`investigator-authority-procedure` 5、`cgmp-compliance-guide` 4、`defect-action-levels` 4、`inspection-sampling` 3、`regulatory-boundaries` 2 含新增 B10、`reference-tools-discipline` 新增第 12 条、`process-control-validation` 两套基准框加第三套数字），脚本 `.cangjie/apply_v4_6_revisions.py` 带唯一性断言；glossary 134→**142**（t135–t142）；test-prompts 67→**75**（v4.6，8 条 `lacf-*`，并同步 1 处旧「九类」口径）。
- **关键纪律（后续维护必须保持）**：① 三套 pH/aw 数字不可互替（4.6/0.85 法定；4.40/4.65/4.75/0.90/0.93/1%/24 罐检查员作业；≤4.4/≤0.92 L.mono 建议层）；② 21 CFR part 108/113/114 及 IOM Ch.4、BAM、CPG、Import Alert 全文一律标「转引未收」，不得从 CP 反推法条或把检查动作写成企业义务；③ 酸化食品是否属 AF 由 HFP 判定，本包不替企业下法定身份结论；④ RRA 的程序性定义可引，FDA 政策公告原文仍不可引；⑤ v4.6 当时为十类不可混引（**v4.7 起十二类，见下节**），CP 7303.070 用「CP 7303.070 PART x / ATTACHMENT x」。
- **编译产物**：`dist-v10`（run `run-20261106-115659-0e1060`，single / 19 卡 / 24 个 .md）；暂存目录校验 0 errors + 1 warning（`name-dir`：`dist-v10` 与 `SKILL.md` 的 `name` 不同，属产物目录名固有提示）；安装后官方 `validate_skill_pack.py` **0 errors / 0 warnings**；旧版备份 `backups/fda-pchf-food-safety-v4.5-20261106-115728`；已安装到 `C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety`（`.cangjie/install_v7.py`），19 卡 / 142 术语 / 75 用例。完整记录见 `.cangjie/v4-6-sources-qa-report.json`。
- **仍未收**：见「已知边界（未关闭）」v4.6 更新版。本次关闭的是「LACF/AF 的 program 与 Part 117 管辖分流、酸化判定、专属取证清单、pH/aw 实验室触发线、Import Alert 升级、RRA 法定地位」，**不是** 108/113/114 法条、杀菌工艺计算、实验室方法、制样判读或警告信阈值。


## v4.7：21 CFR Part 113 / 114 法规正文 → 第十一/第十二来源 + CAP-20 法条卡（20 张卡）

- **触发与范围**：v4.6 收尾后检查 `G:/下载` 发现 8 份未纳入资料（Part 113/114/120/123 四份 CFR，及 7303.878 / 7303.842 / 7303.847 / 7303.819 四份 Compliance Programs）。经选项确认，用户选择 **只补 Part 113 / 114**，并要求「纳入后一起跑」触发盲测；其余 6 份本版不纳入。
- **转换**：两份 GPO/eCFR 双栏印刷版 PDF 用 `pdf2md-pro` 会把同一 y 坐标左右栏文字串成一行（已在 `.cangjie/_probe/cfr114.md` 留证），故新建专用 `.cangjie/convert_cfr_part.py` 按「页 → 左栏 → 右栏」裁剪重排、裁掉首尾相邻 part 残段、按 § 编号渲染 H2。三处修复：跨 part 引用误提升 H2（`start_patterns(part)` 只认目标 part 条款号）、`0.85` / `4.6` 开头续行误判段落（收紧为 `^\d{3}\.\d+\s+[A-Z]`）、相邻 part 残段裁剪。自检：Part 113 **10/10 条款**、Part 114 **8/8 条款**，页眉与独立页码残留 0；保留印刷断词连字符（933 / 210 处），逐字引证按 NFKC 归一化核对。
- **版本口径**：`4–1–25 Edition` 是 CFR **年度编纂版次**（修订至 2025-04-01），不是 2025 新规；条文末尾 FR citation 才是修订出处。
- **本轮最有价值的发现（两处实质性纠错）**：
  1. **Part 110 至今有效**。2015-09-17 PCHF 最终规则的 **amendatory instruction 13**（80 FR 56144）本拟于 2018-09-17 `remove and reserve part 110`；FDA **2018-09-12 最终规则（FR Doc. 2018-19855）撤回该指令**（`amendatory instruction 13 in the third column on page 56144 is withdrawn`），因合规日期延长会造成 4–16 个月 CGMP 空档。eCFR 现行版 Part 110 仍列 11 个 sections（含 §110.110），§114.5 并列 `parts 110 and 117` 也是**现行文本、不是笔误**。v4.3「110.110 是过时引用 / Part 110 已移除」结论作废，改为「现行仍有效、正文本包未收 → 转引未收」；手册那句是 §110.110(c) 意译，**仍不得标成〔§ 117.110(c)〕**，但理由从「part 110 已删」更正为「那是 part 110 的 (c) 款」。2018-19855 正文属外部核实、本包未收。
  2. **两 part 记录保存口径不同**。〔§ 113.100(g)〕是厂内 ≥1 年 + 加工厂或其他合理可及地点再 2 年（合计 3 年，季节包停产可提前转移），〔§ 113.100(h)〕允许符合 **part 11** 的电子记录；〔§ 114.100(e)〕只要求 (b)(c)(d) 副本在加工厂或其他合理可及地点自生产日起**整段 3 年**，**无 1+2 分段、无 (h) 款、Part 114 全文无 electronic / part 11 字样**。CAP-20 草稿曾把两 part 合并写成「都是 1+2 年且可用 part 11 电子记录」，已按 CFR 正文更正到卡片 A2 #13、E 段义务并集矩阵、术语 t149、测试用例 stat-05 与 `source-cfr-part114-2025.md` 条款地图。
- **法条接口**：〔§ 117.1(c)〕并行；〔§ 117.5(d)(1)〕`required to comply with` **且** `in compliance with` 双条件；〔§ 117.5(d)(2)〕仅限 part 113 管辖的微生物危害；**§117.5 豁免清单无 part 114**，〔§ 114.5〕反向把 parts 110 and 117 拉进掺假判定。三套法规正文〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕独立编号，全包扩为 **十二类不可混引**。
- **改动清单**：新增第 20 张卡 `lacf-statutory-requirements`（六段完整，R 段 **26 个英文引用块 26/26 逐字命中**）与 `_meta-lacf-statutory-requirements.yaml`；`assemble_bundle.py` SLUGS 19→20、登记 `src-fda-cfr-part113-2025` / `src-fda-cfr-part114-2025`、ALSO_READ 双向补 6 处、entry.description +1 段、core_principles 改写 3 条 +3 条、out_of_scope 改写 2 条、stop_conditions 改写 5 条 +2 条（十类→十二类、19→20 卡）；`.cangjie/apply_v4_7_revisions.py` 带唯一性断言回补 **9 个文件 32 处**旧口径（含 CAP-19 B2、四张迎检卡、Part 110 纠错）；`_meta-lacf-inspection-program.yaml` source_label 同步；`source-cp-7303-070-2024.md` 文件头「十类来源」→「十二类来源」；glossary 142→**152**（t143–t152）并改写 t116 / t142；test-prompts 75→**85**（v4.7，10 条 `stat-*`，改写 `defect-level-02` / `lacf-08` 两处旧结论，5 处「十类」同步）；`BOOK_OVERVIEW.md` / `DIGEST.md` 同步版本与 v4.3 纠错。
- **校验**：20 份 meta YAML 类型检查 `problems 0`；CAP-20 R 段 26/26 引文逐字命中；glossary 152 条 id 无重复；85 条用例 id 无重复；`assemble_bundle.py` / `apply_v4_7_revisions.py` py_compile 通过。
- **编译产物**：`dist-v11`，安装后官方 `validate_skill_pack.py` **0 errors / 0 warnings**；旧版备份 `backups/fda-pchf-food-safety-v4.6-*`；已安装到 `C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety`。完整记录见 `.cangjie/v4-7-sources-qa-report.json`。
- **仍未收**：21 CFR part 108 / 110 / 120 / 123 正文、IOM 其余章节（尤其 Ch.4）、BAM / AOAC / MPM 方法正文、CPG 全套、Import Alerts 正文、其余 Compliance Programs（7303.878 / 7303.842 / 7303.847 等）、F0/D/z 计算与温度分布/热穿透研究设计、卷边解剖判读、商业无菌验证方案审批、Form 2541e 细则。本次关闭的是「LACF/AF 的条款级法定义务与 Part 117 并行接口」，**不是**杀菌工艺计算、备案流程或实验室方法。

## v4.7 补充质量评测（触发增强 / 输出 / 路由；未改正式套件、未发新版）

- **触发原因**：v4.7 首次触发盲测 F1 1.000 但带 6 条解读限制（每例 1 次、无 sibling、负例仅 5 条、未测卡路由、judge 只看浓缩目录、不作非劣声明）。用户选项确认「补跑输出与路由评测」。
- **范围纪律**：只做评测，**正式 `test-prompts.json`、`SKILL.md`、`dist-v11`、已安装 v4.7 一律未改动**；全部产物落在 `.cangjie/v4-7-output-routing-eval/`。评测前复核安装目录官方校验仍 `0 errors / 0 warnings`、20 卡 / 152 术语 / 85 用例、5 份 glossary 副本 sha256 全同。
- **增强触发评测**：`trigger-suite-v2.json` = 85 原用例（`edge_case → should_trigger` 沿用 v4.7 适配器）+ 8 条 sibling（`pdf2md-pro` / `brand-ip` / `cangjie-skill` / `officecli1098` 各 2 条）+ 10 条新增负例 = 103 条，全部 `runs: 3`；split 62/41。3 个干净 sub-agent 各完整判 103 条构成 3 次独立重复，合并 309 行，覆盖完整、跨轮分歧 0。官方 score：**TP 237 / FP 0 / FN 3 / TN 69，precision 1.000 / recall 0.988 / F1 0.994，兄弟混淆率 0.000（0/24）**。8 条 sibling 全中各自兄弟技能、15 条负例全判 none。
- **唯一失败项口径分析**：3 个 FN 全来自 `secg-edge-02`（「按中国 GB 14881 出内审检查表 + 药品 21 CFR 211 偏差调查」）。正式套件标 `edge_case`，`expected_behavior` 是「应明确告知超出本包覆盖，不硬套」；已安装 `SKILL.md` 的「不适用」明确列有「中国 GB 14881 等非美国法规的直接合规判定」。故 judge 判 none 与技能自身停用条件一致，**不是漏触发**，而是 `edge_case` 一律映射 `should_trigger` 的评测口径错配。仅把该条按原始语义改为 `should_not_trigger` 的敏感性套件得 F1 1.000，主结果仍以 0.994 为准。建议未来把边界用例拆为 `edge_scope_out`（按停用条件不触发）与 `edge_reroute`（触发但需换卡/辅读）。
- **输出质量评测**：官方 `run_output_evals.py` 确定性机械断言。10 条 output case / 27 条断言，锚定 v4.7 新增知识点（§113.100(g)(h) 的 1+2 年 + part 11、§114.100(e) 整段 3 年、Part 110 未移除、§117.1(c)/§117.5(d)、§113.3 的 4.6/0.85、scheduled process、十二类不可混引）+ 3 条难度基线。三变体 `v47_skill` / `v46_skill`（备份 `backups/fda-pchf-food-safety-v4.6-20261106-132910`）/ `without_skill`，官方 prepare 生成 30 个匿名包，3 个 agent 按 label 各写 10 份 `.md`。**v47 10/10、v46 8/10、无技能 8/10**。v46 失败于 `out-02`（明确写「part 113/114 正文未纳入本体系，转引未收」，未给出 §114.100(e)）与 `out-07`（仍写「十类不可混引」）；无技能失败于 `out-03`（缺 2018 撤回指令）与 `out-07`（拒答「当前共有 N 类来源」）。v4.7 在两处本版新增知识点上独占通过，未发现 v4.7 输出错误。
- **能力卡路由评测**：官方无此评测器，自建 `.cangjie/score_routing_eval.py`。`routing-suite.json` 覆盖 **20 张能力卡各 1 条**，候选清单取已安装 `references/capability-index.md`；2 个干净 sub-agent 各判 20 条。**top-1 命中 40/40 = 1.000、重复一致 20/20、非法 slug 0、混淆对 0**，含最易混的 CAP-19 / CAP-20 两轮全中。
- **局限（随数字一起读）**：触发仅跑确定性判分，未作统计非劣声明；输出只跑机械断言，A/B 偏好盲评与人工复核按官方设计留待后续，变体条件是指令级约束、未做工具调用审计，7/10 用例三变体全过说明多数断言对模型先验不敏感；路由用例按各卡意图反向编写、属原型化 prompt，judge 预读浓缩索引且被提示 CAP-19/20 区分，1.000 不代表真实口语化/复合意图下的准确率；三块均为离线代理评测，不是宿主端到端激活日志。
- **结论**：技能包无需修复、无需发版；本次为质量增强。产物与脚本见 `.cangjie/v4-7-output-routing-eval-report.md` 第六节。


## v4.8：CP 7303.878 落为第十三来源 + FSVP 进口商检查分流卡（21 张卡）

- **触发与范围**：v4.7 收尾时 `G:/下载` 仍有 6 份暂缓资料，本轮用户提供 `CP7303.878 Foreign Supplier Verification Programs Inspections 508-Compliant.pdf`（33 页 / 20 书签）。按既有模式纳入为**第十三来源**并发布 v4.8；其余 5 份（Part 120 / 123、7303.842 / 7303.847 / 7303.819）本版仍不纳入。
- **转换**：`pdf2md-pro` 转出原始 75893 chars / 510 行 / 50 headings / 93 表格行 / 20 书签全命中 / 0 丢弃 / 残留独立页码 0；`.cangjie/finalize_cp_7303_878_source.py` 再删除 62 行重复页眉（`**Date of Issuance**`、`**Transmittal Number**`、机构名/项目名），写文件头后为 `source-cp-7303-878-2023.md`（82178 chars / 487 行 / 92 个 `<u>` 标签）。自检见 `.cangjie/cp-7303-878-convert-report.json`。
- **版本口径（第三次同类纠错）**：首页 `PROGRAM 7303.878` / `Transmittal Number: 2023-CPM-CFSAN-003` / `Implementation Date: 09/27/2023` / `Date of Issuance: 08/28/2025`。Change History 为 Initial Issuance 10/20/2021 → Update 09/27/2023（改名 FSVP Inspections、不把一般进口 operations 内容并入本 CP、补 Part II 程序交互与 Part V 执法流程）→ Pen/Ink 08/20/2024（FSPCA 链接、部分案件 direct reference authority、POC）→ **Corrections 08/28/2025（仅 CFSAN 重组后 POC 与机构名称/缩写）**。故本件是 **2023-09-27 版程序的 2025-08-28 更正版**，与 CP 7303.050 / 7303.070 同型，不同于 CPGM 7303.040 的 `2025-CPM-HFP-001` 新 Transmittal。另更正 `CP 7303.819`：是 2006 FY06-08 旧程序、已过 COMPLETION DATE 9/30/08 而非现行，准确说法不是「法规意义上废止」；本包仍未收其正文。
- **法源与主体分流（本轮核心）**：FSMA §301 增订 FD&C Act §805 → 2015-11 FSVP regulation `21 CFR part 1, subpart L（§§1.500–1.514）`，**正文本包未收，一律标「转引未收」**；它与 FD&C Act §418 / Part 117 Subpart G 是**两套法源、两类主体**：前者管进口商 **FSVPI**（§1.500 定义的美国货主/收货人，无美国货主时由签署同意书的美国代理/代表承担），后者管 receiving facility。CP PART II.3.A 的 deemed compliance 只覆盖同时为 manufacturer/processor 且符合 Part 117 / 507 供应链要求者，且原文 `except they must comply with section 1.509` 把每一 entry line 的 UFI/DUNS 电子申报义务单独留下。
- **其余核出的实质口径**：§1.502(a) 对每一种食品 develop, maintain, and follow FSVP；standard requirements §1.502/1.503/1.504/1.505/1.506/1.508/1.509/1.510 与 modified requirements §1.507/1.511/1.512/1.513（满足 modified 条件者**可选择** standard）；§1.501(b)–(h) 八类豁免；**`Samples will not be collected as part of an FSVP inspection.`** 且 PART IV 四节 Intentionally Left Blank——不得套 CP 7303.050 的样品量与环境拭子；483a 观察分级 → NAI/VAI/OAI → Warning Letter / Import Alert 99-41 / §801(a)(3) 拒绝入境，§301(zz) 为禁止行为；**Import Alert 99-41 与 CP 7303.070 的 99-37/99-38 不是同一个 Alert**，99-41 按「具体食品 + 具体境外供应商组合」列 Red List，未上 Red List 不等于自动禁运，移除须先提交证据；§1.507 disclosure 不能替代 §801(b)/§1.95 reconditioning proposal 资料；direct reference authority 仅在有限情形授予，首次违法不默认优先执法。
- **设计决策**：新增 **CAP-21 `fsvp-inspection-program`**，不并入 CAP-07 `supply-chain-verification`——两者法源、主体不同，且 CAP-21 还承载进口商检查、483a 分级、99-41 加/删名单与拒绝入境阶梯。CAP-21 六段完整，R 段 **46 个英文引用块 46/46 逐字命中**（`.cangjie/verify_fsvp_quotes.py`；初版 `strip_markup()` 只剥 `</?u>` 导致 Change History 表格 `<br>` 残留而 46 MISS，改为 `re.sub(r"<[^>]+>", "", s)` 后全中），B1–B12 边界齐备；meta 数字形 keyword（`"1.500"` / `"03878"`）全加引号，`yaml.safe_load` 类型检查 problems 0。
- **改动清单**：`assemble_bundle.py` docstring 20→21 张、SLUGS +`fsvp-inspection-program`、ALSO_READ 正向 7 条 + 反向 6 张卡、登记 `src-fda-cp-7303-878-2023`、entry.description +FSVP 段、core_principles 37→40（+3）、out_of_scope 6→7、stop_conditions 14→16、全局「十二类→十三类」「20 张→21 张」；`.cangjie/apply_v4_8_revisions.py` 带唯一性断言回补 **8 张既有卡 + 3 个来源文件头**（第一次因非唯一锚点失败，从 `.cangjie/backup-v4-8-pre-revisions/` 回滚 12 个文件后修复重跑成功）；`.cangjie/append_v4_8.py` 写 glossary t153–t162（**162 条**）与 `fsvp-01..10`（**95 条**用例，v4.8）；`PIPELINE_STATE.md` / `BOOK_OVERVIEW.md` / `DIGEST.md` 由本脚本同步。
- **QA 附带修复（基线问题，非 v4.8 回归）**：glossary fenced YAML 块长期有 7 行 `summary` 因「整段双引号包裹 + 内部未转义 ASCII 双引号」而无法 `yaml.safe_load`（v4.7 备份复核确认）；`.cangjie/fix_glossary_yaml.py` 把这 7 行改写为内容逐字保留的 `|-` 块标量后，全块严格解析通过、**162 条 id 唯一**、t153–t162 齐备。该 fenced 块是 markdown 交付物，编译/官方校验本就不解析它，故不影响此前各版 0 errors 的结论。
- **口径残留判定**：`test-prompts.json` 顶层 notes 中 2 处「十二类」是**描述 v4.7 当时状态**的历史记录，保留不改；v4.8 段已写明「全包十三类不可混引」。`build_v4_7_eval_suites.py` 中 1 处「十二类」是 v4.7 输出评测的断言字符串，属历史评测套件，不随版本改写。
- **仍未收**：21 CFR part 1 subpart L（§§1.500–1.514）正文、Import Alert 99-41 全文、FSVP Guidance for Industry、IP guidance tabs / Implementation Work Instructions、HFP Enforcement Bulletin #13/#6、RPM 4-1-8、CP 7303.819 / 7303.842 / 7303.847 正文、21 CFR part 108 / 110 / 120 / 123 / 507 正文、IOM Ch.4、BAM / CPG 全套、F0/D/z 计算与卷边解剖判读。本次关闭的是「FSVP 轨道与 Part 117 供应链程序分流、进口商检查取证清单、483a 分级与 99-41 阶梯」，**不是** FSVP 法规条文级义务。
- **评测状态**：本版**未重跑**触发 / 输出 / 路由评测；v4.7 的 F1 1.000（首次盲测）、F1 0.994（增强触发 103×3）、输出 10/10、路由 40/40 均为上一版本结论。（当时）10 条 `fsvp-*` 用例与 CAP-21 的路由正确性待后续补测 —— **11-06 晚已补测完成**，详见 「v4.8 / v4.9 历史用例补测」小节。
- **编译产物**：`dist-v12`（run `run-20261106-151203-02dd78`，single / 21 卡 / 27 个发布文件 / 26 个 .md）；暂存目录校验 `0 errors + 1 warning`（`name-dir`，产物目录名固有提示）；安装后官方 `validate_skill_pack.py` **0 errors / 0 warnings**；旧版备份 `backups/fda-pchf-food-safety-v4.7-20261106-151259`；已安装到 `C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety`（`.cangjie/install_v9.py`），产物与安装目录逐文件 sha256 差异 **0**，5 份 glossary 副本 hash 全同（1b455fd004919712…），安装目录 `21 卡 / 162 术语 / 95 用例 / 十三类`。完整记录见 `.cangjie/v4-8-sources-qa-report.json`。

## GitHub 同步
- 私有仓库：`https://github.com/billy-zhouj/fda-pchf-food-safety`（默认分支 `main`，首次提交 `ec7b0f4`）。
- 工作目录已 `git init`，仓库级身份 `billy-zhouj <billy-zhouj@users.noreply.github.com>`，`.gitignore` 排除编译产物/备份/缓存、保留 `dist-v12` 与全部源码。
- 后续更新：改文件后 `git add -A && git commit -m "..." && git push`；本仓库因企业代理 MITM 设了 `http.sslVerify=false`（仅本仓库生效）。


## v4.9 — 海产品 HACCP 法条层（21 CFR Part 123）与 Part 117 条件性豁免接口

- **新增来源（第十四类）**：`source-cfr-part123-2025.md` — 21 CFR Part 123《Fish and Fishery Products》，**4–1–25 Edition**（修订至 2025-04-01，书页 456–464，9 页 / **13 条款**）。用户提供的 `CFR-2025-title21-vol2-part123.pdf`（170 KB）经 `.cangjie/convert_cfr_part.py` 双栏重排转出。自检：13/13 条款命中（123.3 / .5 / .6 / .7 / .8 / .9 / .10 / .11 / .12 / .15 / .16 / .20 / .28）、页眉与独立页码残留 0、卷首 Sec. 目录区裁 34 行（13 条目录条目）、尾部 Part 124 残段裁 19 段、串栏 0、最终 41,669 chars。
- **转换脚本两处缺陷与修复（本轮工程发现）**：
  1. **假 H2**：§123.8(b) 正文里的跨条引用 `§ 123.7 whenever any verification procedure ... reveals the need` 被 `start_patterns` 误判为条款标题，产出多余 H2。修法：§ 起点要求条号后同行接**大写起首**标题词，或**条号独占一行**（GPO 印刷版常见「§ 123.3 / Definitions.」两行式）。Part 113 / 114 回归测试条款数仍为 10 / 8，无回归。
  2. **卷首目录并段**：`Sec.` 后的目录条目不是段起点，被 `^\d{3}\.\d+\s+[A-Z]` 与 Subpart 规则反复拼接，产出 `### Subpart B—… 123.15 General. 123.16 Process controls.` 残行。新增 `drop_toc()` 整体裁掉 PART 行到 AUTHORITY/SOURCE 之间的目录区。
- **版本口径**：`4–1–25 Edition` 是 CFR **年度编纂版次**，**不是** 2025 新规则；SOURCE `60 FR 65197, Dec. 18, 1995`，§123.5 与 §123.11 经 `80 FR 56167 (2015-09-17)` 修订（PCHF conforming amendment）。本件**不是** CP 7303.842。
- **核心法条接口（双向锁定，逐字核对）**：
  - 〔§ 123.5(a)〕`Except as provided by § 117.5(b), parts 110 and 117 of this chapter apply in determining whether ...` —— Part 110/117 **默认适用**，§117.5(b) 是**唯一**例外出口。
  - 〔§ 117.5(b)〕`Subparts C and G of this part do not apply with respect to activities that are subject to part 123 ... if you are required to comply with, and are in compliance with, part 123 of this chapter with respect to such activities.` —— 与 part 113〔§ 117.5(d)(1)〕**同构**的条件性豁免。
  - ⚠ **关键差异**：part 113 有〔§ 117.5(d)(2)〕把豁免限缩到「part 113 管辖的微生物危害」；**§117.5(b) 没有对应限缩款**。故两向误读都会错：搬 part 113 口径 → 低估豁免；因无限缩就推成整厂免检 → 高估豁免（边界是受 part 123 管辖的 **activities**，〔§ 123.3(k)(2)〕三项排除不在内，且豁免不含 Part 117 **Subpart B** 的 CGMP）。
- **其它已钉死的口径**：〔§ 123.15〕〔§ 123.20〕`augments subpart A` 是**叠加非替代**；〔§ 123.16〕的 `except those subject to part 113 or 114` **只排该条**、Subpart A 全套仍适用（与〔§ 123.20〕整体不适用 Subpart C 的处理不同）；〔§ 123.6(c)(1)〕危害考虑清单为 **(i)–(ix) 九项**且措辞是 `Consideration should be given`（非强制穷举，但漏考虑属危害分析缺陷）；〔§ 123.7(c)(1)〕**先隔离扣留**再评审；〔§ 123.8(a)(3)(i)(ii)〕CCP 与纠正措施记录**1 周内**复审、(a)(1) 变更时及**至少每年**复审且不足时须立即改；〔§ 123.9(b)(1)〕记录期**冷藏 1 年 / 冷冻-保藏-货架稳定 2 年**；〔§ 123.11(a)〕SSOP 用 `should` 而 (b)(c) 监测记录用 `shall`（原文措辞，非转换错误）；〔§ 123.12〕进口商二选一 + affirmative steps (A)–(F)，competent third party 可代写程序，无等效保证即视为掺假并**拒绝入境**；〔§ 123.28〕贝类须来自 approved growing waters、shellstock 须附 tag 五要素、shucked 标签须符合 §1240.60(c)。
- **与 FSVP 的分工（易混点）**：§123.12 法源为 Part 123 + FD&C Act，FSVP 法源为 FD&C Act §805 + 21 CFR part 1 subpart L；两套可共用证据但**互不替代**；FSVP 的 deemed compliance 明文只免 FSVP 且保留 §1.509，**不覆盖 §123.12**。
- **新增能力卡 CAP-22**：`seafood-haccp-statutory-requirements`，importance `extended`，also_read 9 条，B1–B12 边界，A2 25 条触发。R 段 **33 个英文引用块全部逐字命中**（32 条 Part 123 + 1 条 §117.5(b)）。
- **引文核对脚本的自我验证缺陷（本轮重要发现）**：`verify_seafood_quotes.py` 初版直接对整份源文件做归一化匹配，而**文件头里我自己转述了 §117.5(b) 原文**，导致该条引文在「自己的文件头」里命中，形成自我验证循环。修法：`body_only()` 只取第一个 `## § ` 之后的正文区。修后第 2 条正确标为 `Part117`，其余 32 条 `Part123`，33/33 全中。同步核查了 `verify_fsvp_quotes.py`：它以第二个 H1 定位正文区，且 CP 878 文件头不含被核对引文，历史结论不受影响。
- **规模变化**：21 → **22 张卡**；162 → **172 条术语**（t163–t172）；95 → **105 条用例**（v4.9，`seafood-01..10`）；十三类 → **十四类来源**；core_principles 40 → **42**；out_of_scope 7 条（原「海产品 part 123 专项要求」条目已改为「CP 7303.842 正文 / NSSP Guide / part 120」）；stop_conditions 16 → **18**。
- **仍未收**：CP 7303.842 海产品检查程序正文、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、NSSP Guide、FDA《Fish and Fishery Products Hazards and Controls Guidance》4th ed.、Import Alert 16-xx 系列、BAM 海产品章节、组胺/河豚毒素/雪卡毒素限值。
- **评测状态**：本版**未重跑**触发 / 输出 / 路由评测；v4.7 的 F1 1.000 / 0.994、输出 10/10、路由 40/40 均为历史版本结论，**不得冒用**；（当时）10 条 `seafood-*` 用例与 CAP-22 路由待补测 —— **11-06 晚已补测完成**：触发 30/30、输出 10/10（严格套件仍 10/10）、CAP-22 路由 33/33，详见 「v4.8 / v4.9 历史用例补测」小节。
- **口径回补（4 个脚本，全部带唯一性断言 + 内存暂存 + 末尾一次性落盘）**：`apply_v4_9_revisions.py`（SLUGS / ALSO_READ / 索引与描述）、`apply_v4_9_residue.py`、`apply_v4_9_residue2.py`、`apply_v4_9_residue3.py`、`apply_v4_9_bundle_arrays.py`、`apply_v4_9_docs.py`。范围：**8 张既有卡 + 3 份 meta yaml + 2 份 overview + 3 份 glossary + 3 个来源文件头 + `assemble_bundle.py` + 三份状态文档**。回补前快照 `.cangjie/backup-v4-9-pre-revisions/`（29 文件）与 `.cangjie/backup-v4-9-pre-residue/`（52 文件）。
- **本轮发现的两类真实缺陷（不是措辞问题）**：
  1. **v4.8 的批量替换污染了 v4.7 的历史陈述**：v4.8 用全局 `十二类→十三类` 回补时，把 t152 里「v4.7 起十二类不可混引：三套法规正文 + 九类＝12」也改成了「十三类」，出现「十三类：列 12 项」的自相矛盾。v4.9 按版本复原为十二类并补完整阶梯（十→十二→十三→十四）。
  2. **Part 123 已收但全包仍在说「未收」**：除 `lacf-*` 三卡外，`cgmp-compliance-guide` / `defect-action-levels` / `inspection-sampling` / `reference-tools-discipline` / `regulatory-boundaries` / `inspection-readiness` / `fsvp-inspection-program` 与 3 份 meta、overview、glossary、`test-prompts.json` 共约 40 处仍写「part 108 / 110 / 120 / 123 未收」或「part 120 / 123 正文本包未收」。已逐处改为「part 120 未收、part 123 自 v4.9 起已收（见 CAP-22）」，并把「三套独立编号」统一为四套。
- **教训：`verified.yaml` 是 `assemble_bundle.py` 的生成物，不是手改对象。**本轮先手改了 `verified.yaml` 的 7 处来源注记，重跑组装后被脚本内硬编码文本覆盖回旧值；正确做法是改 `assemble_bundle.py` 里的 `additional_sources` / `entry` 文本，再重新组装。已据此修 10 处（含核心原则第 37 条「三套→四套」与引用纪律段的 part 123 括注位置）。
- **编译产物**：`dist-v13`（`compile_single.py --bundle .cangjie/capabilities --out dist-v13 --variant single`，Bundle 原生确定性编译，无 run id；27 个文件 / 26 个 .md / 22 张卡）；暂存目录校验 `0 errors + 1 warning`（`name-dir`：`dist-v13` 与 `SKILL.md` 的 `name` 不一致，属产物目录名固有提示）。
- **安装**：旧版备份 `backups/fda-pchf-food-safety-v4.8-20261106-161843`；已安装到 `C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety`（`.cangjie/install_v10.py`）；安装后官方 `validate_skill_pack.py` **0 errors / 0 warnings**；产物与安装目录逐文件 sha256 差异 **0**；5 份 glossary 副本 hash 全同（`9e366adcb39daa2e…`，172 条严格 `yaml.safe_load` 通过）；安装目录 `22 卡 / 172 术语 / 105 用例 / 十四类来源`。完整记录见 `.cangjie/v4-9-sources-qa-report.json`。
- **产物残留自查**：`dist-v13` 全量扫描，`SKILL.md` 内「十三类」= 0、「四套法规正文」= 2；`glossary.md` 6 处「十三类」全部是版本阶梯或 v4.7/v4.8 changelog（属历史记录，按 v4.8 同类口径保留）；「part 120 / 123 + 未收」的 2 处命中均为「供应商符合 part 120 / 123」这类**法规原文引用**，不是未收声明。


## v4.10 — 海产品危害分析判定链（FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版，June 2022）

- **新增来源（第十五类）**：`source-seafood-hazards-guide-2022.md` — FDA《Fish and Fishery Products Hazards and Controls Guidance》**第 4 版 June 2022**（SGR 129）。来源为 WorkBuddy 资料库节点 `XMsRyrFL0wM1hesg8X6K9u`，因内联读取报「大载荷不走内联代理」而改走 `export/export_node.py` 导出通道取得全文（1,709,446 字节 / 31,321 行）。落地文件含导入说明：非约束性定位、与 Part 123 法条层的分工、分章滚动修订的版本口径、以及导出件转换质量红线。**封面 June 2022，但 Ch.3 页脚 `3 - 1 (June 2021)`、Appendix 3 为 `A3-1 (June 2021)`、Appendix 5 为 `A5-1 (June 2021)`、Ch.19 书目 August 2019** —— 是分章滚动修订，不是 2022 新规。
- **本件填补的缺口**：v4.9 段「仍未收」清单里点名的 `FDA Fish and Fishery Products Hazards and Controls Guidance 4th ed.`。已收的 Part 123（CAP-22）是**法条义务层**，本件是配套的**技术指南层**（how to 判定），两者配对而非合并。核对确认：本地 `source.md` 是另一份（PCHF 行业指南草案 October 2026），与本件无重复。
- **cangjie 流水线（阶段 0–5，沿用 single 模式，不另起技能包）**：阶段 0 产出 `BOOK_OVERVIEW-seafood-hazards-guide-2022.md`（与既有第一来源 BOOK_OVERVIEW.md 并列，不覆盖），含 Adler 四步、7 条关键术语、4 组批判、转换质量红线；阶段 1 并行 5 路提取，审计轨迹留在 `candidates/v4-10-{framework,principles,cases,counter-examples,glossary}.md`（框架 8 / 原则 10 / 案例 11 / 反例 14 / 术语 15 条）；阶段 1.5 全部通过三重验证；阶段 1.6 **不晋级独立 Skill**，全部经唯一入口路由（与 v4.9 一致）；阶段 2–4 产出能力卡、also_read、术语与评测用例；阶段 5 编译交付。
- **新增能力卡 CAP-23**：`seafood-hazards-controls-guide`，importance `extended`，also_read 9 条（与 CAP-22 / hazard-analysis-method / chemical-hazard-controls / process-control-validation / allergen-program / regulatory-boundaries / inspection-sampling / cgmp-compliance-guide / reference-tools-discipline 双向链）。用户明确要求「**完整危害分析判定链**」，主干为：产品描述与流程图 → Ch.3 三表识别品种相关（Table 3-2/3-3）与工艺相关（Table 3-4）潜在危害 → Ch.4–21 理解危害 → 在**无控制条件下**按 `reasonably likely to occur` 逐步判显著性 → 第 3/4 栏 Yes/No 都写理由 → Step 11 判定树定 CCP → 选控制策略示例 → 定关键限值与监控四问 → 纠正/记录/验证。A2 32 条触发、B1–B12 边界、E 段 Step 1–8 含六栏工作表 ↔ 十栏计划表映射。
- **引文核对（独立复核，非自证）**：`.cangjie/verify_v4_10_quotes.py` 用 `body_only()` 只取源文件「## 正文（导出原文，未改写）」之后的文本，避免文件头自我验证循环（v4.9 `verify_seafood_quotes.py` 的教训）。R 段 **37 个英文引用块 37/37 逐字命中**，0 超 100 词，0 表格/页眉/残表引用。表格列头连写（`MARKETNAMES`）、词条粘连（`ALFONSINOALFONSINO`）、字符丢失（`fsh` / `Pufer`）、页码混入单元格、Appendix 3 的 CCP 判定树塌陷成残表，均已写入源文件导入说明与本卡 B 段红线。
- **关键口径（三处最易误读）**：① `should` 仅为建议、指南不设可执行责任、可另选控制策略与关键限值但须科学论证其充分性；② Ch.3 表**不得单独使用**、指南不替代〔§ 123.6〕危害分析、须警觉新出现危害与物种替换；③ **双向防误读**——既不把指南/Appendix 5 数值（组胺 50/500 ppm 回指 CPG Sec. 540.525，属转引未收）当合规清单或法定限值，也不因指南非强制就把 Part 123 的 `shall` 义务稀释成可选。Appendix 5 的限值是外部法源快照，不是 FDA 在本指南新设的限值。
- **规模变化**：22 → **23 张卡**；172 → **182 条术语**（t173–t182，围绕判定链排布）；105 → **115 条用例**（`seafood-hazards-01..10`，9 正/边界 + 1 跨法域 should_not_trigger）；十四类 → **十五类来源**；core_principles 42 → **45**；stop_conditions 18 → **20**；dist-v13 → **dist-v14**。
- **工程修复**：`.cangjie/assemble_bundle.py` 的 `BASE` 原硬编码原开发机路径 `E:/WeChatData/...`，本机无法运行；改为 `Path(__file__).resolve().parents[1]` 相对推导，任何机器可跑。`verified.yaml` / `destinations.json` / `book/` 仍是脚本生成物，未手改。
- **口径回补的两轮策略（沿用 v4.9 教训）**：第一轮 `apply_v4_10_revisions.py` 用精确替换 + 「整行含版本标记则跳过」保护历史陈述（**「第十四类」含「十四类」子串、历史编译记录里的「22 张」若全局替换会被污染**）；第二轮 `apply_v4_10_residue.py` 补掉一批行尾带 `v4.9` 注记的当前口径长行（各卡 B 段引用规范、Step 收尾、开头来源分层）。版本阶梯陈述（v4.6 十类 → v4.7 十二类 → v4.8 十三类 → v4.9 十四类 → v4.10 十五类）全部保留不改。
- **仍未收**：CP 7303.842 海产品检查程序正文、NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、Import Alert 16-xx 系列、BAM 海产品章节、CPG Sec. 540.525 / 555.300 / 575.100、21 CFR 556 系列、40 CFR 180 系列、Import Tolerance、组胺/河豚毒素/雪卡毒素检测方法。
- **评测状态（11-06 已补跑完成）**：10 条 `seafood-hazards-*` 用例与 CAP-23 路由正确性**已补测**，详见下方「v4.10 补充质量评测」小节与 `.cangjie/v4-10-eval-report.md`。触发 F1 1.000（84 判）、输出 `v410_skill 6/10 / without_skill 2/10`、路由 top-1 **99/99**（CAP-23 定向 **24/24**、CAP-22 定向 12/12、交叉混淆 0/0）、静态登记 14/14 PASS。v4.7 的 F1 1.000 / 0.994、输出 10/10、路由 40/40 仍属历史版本结论，未冒用；（当时）v4.8 的 10 条 `fsvp-*` 与 v4.9 的 10 条 `seafood-*`（CAP-22）用例仍未补测 —— **该项已于 11-06 晚补测关闭**，详见 「v4.8 / v4.9 历史用例补测」小节 与 `.cangjie/v4-8-v4-9-legacy-eval-report.md`。
- **编译产物**：`dist-v14`（`compile_single.py --bundle .cangjie/capabilities --out dist-v14 --variant single`，Bundle 原生确定性编译，无 run id；**28 个文件 / 28 个 .md / 23 张卡**）；官方 `validate_skill_pack.py` **0 errors + 1 warning**（`name-dir`：`dist-v14` 与 SKILL.md 的 `name` 不一致，属产物目录名固有提示）。SKILL.md 前 150 字符已含 PCHF / 21 CFR 117 / FSMA / 危害分析等核心触发词；description 共 4235 字符（v4.9 为 3857），超过 WorkBuddy 内置技能展示长度，按既有口径未擅自改动产物。
- **安装**：旧版备份 `../../.workbuddy/skills/backups/fda-pchf-food-safety-v4.9-20261106-201144`；已安装到工作区级 `.workbuddy/skills/fda-pchf-food-safety/`（`.cangjie/install_v10.py` 硬编码原开发机路径，仍采用等价的直接复制 + 逐文件 hash 校验）；产物与安装目录逐文件 sha256 差异 **0**；**5 份 glossary 副本 hash 全同**（`18eabcd564e9…`，182 条严格 `yaml.safe_load` 通过）；路由表 23 张卡全部命中且无孤立卡；`destinations.json` 23 个去向；全库「该指南仍未收」残留 **0**。完整审计见 `.cangjie/v4-10-sources-qa-report.json`。


## v4.10 补充质量评测（10 条用例 + CAP-23 路由；只做评测，未发新版）

- **触发原因**：v4.10 发布时写明「10 条 `seafood-hazards-*` 用例与 CAP-23 路由正确性待后续补测」；用户 11-06 要求补跑。
- **范围纪律**：只做评测，正式 `test-prompts.json`、`SKILL.md`、`dist-v14`、已安装 v4.10 一律未改动；评测后复核产物与安装目录仍 **28 文件、逐文件 sha256 差异 0**。全部产物落在 `.cangjie/v4-10-eval/`，新增 3 个脚本；v4.7 / v4.8 / v4.9 的历史评测结论原样保留，不改写、不冒用。
- **方法与口径**：完全沿用 v4.7 补充质量评测 —— 官方 `run_trigger_evals.py` / `run_output_evals.py` 判分，能力卡路由用与 `score_routing_eval.py` 同型的 `score_v4_10_routing.py`；干净 sub-agent 盲判；`edge_case → should_trigger` 沿用 v4.7 适配器口径（本次 08/09 的 expected_behavior 确实要求激活，语义正确，非 v4.7 `secg-edge-02` 那类错配）。
- **① 确定性静态核对**（`.cangjie/check_v4_10_routing.py`，不依赖 LLM）：**14/14 PASS** —— `verified.yaml` 23 卡且 CAP-23 为 `extended`/`active`、also_read 9 条；`destinations.json` 23 去向；`capability-index.md` / `cheatsheet.md` / `SKILL.md` 路由表主行 1 行 + 9 行辅读；两份卡片一致；产物与安装目录 hash 差异 0。首次运行曾误报 2 处 FAIL，核实为**检查判据写窄**（cheatsheet 用卡片标题而非 `CAP-23` 编号登记；主行子串匹配把 8 个辅读行误算为主行），改为按标题/按列判定后全 PASS，产物无缺陷。**词面代理（IDF 加权关键词）只判对 11/22、CAP-23 相关 8/18**，多被 `hazard-analysis-method` 抢走 —— CAP-01/22/23 在 `hazard analysis`/`CCP`/`critical limit`/`reasonably likely to occur` 上大量重叠，词面无法表达「问法定义务还是问判定方法」，故该层只证明登记完整，准确率以语义盲判为准。
- **② 触发评测**：28 条（10 新用例 + v4.7 原样复用的 8 sibling + 10 负例）× 3 轮 = **84 判**，官方 score 得 **TP 27 / FP 0 / FN 0 / TN 57，precision 1.000 / recall 1.000 / F1 1.000，兄弟混淆率 0.000（0/24）**；10 条新用例单独 **30/30**（9 正/边界 ×3 全 TP，1 条跨法域负例 ×3 全 TN）。
- **③ 输出质量评测**：10 条 × 2 变体 = 20 份答案、40 条机械断言（逐点抽取自 `expected_behavior`，比 v4.7 多数 case 的 2–3 条更严，**不可与 v4.7 的 10/10 直接比较**）：**`v410_skill 6/10` / `without_skill 2/10`**，逐例 7 胜 2 平 1 负。4 条未全过：`sh-out-05` 是断言 `Table 3-4` 未收合法简写「3-4」的**措辞缺陷**（另存 `output-suite-corrected.json` 敏感性套件得 **7/10 / 2/10、7 胜 3 平 0 负**，主结果仍以 6/10 为准）；`sh-out-02`（第 4 栏理由）、`sh-out-04`（六栏↔十栏映射）、`sh-out-07`（Ch.4–21 四段式）为**单次作答取舍**，已回查 CAP-23 卡片内 Column 4 理由 6 处、L226 映射表、L218 四段式、`Table 3-4` 6 处，**知识点齐备，不是卡片缺陷**。
- **④ 能力卡路由评测**：33 条（23 卡各 1 条 + CAP-23 定向 7 条 + CAP-22 定向 3 条）× 3 轮 = **99 判**，**top-1 99/99 = 1.000**、重复一致 33/33、非法 slug 0、无混淆对；**CAP-23 定向 24/24、CAP-22 定向 12/12、两卡交叉混淆 0/0**，23 张卡基础用例每卡均 3/3。**结论：CAP-23 已稳定承接「怎么判/怎么填表/怎么定 CCP」，且未吃掉 CAP-22 的「法定义务/条款号」问题。**
- **局限（随数字一起读）**：judge 为同一底座模型的干净 sub-agent，非宿主端到端激活日志；路由 `instruction` 已提示 CAP-22（法条层）/ CAP-23（指南判定链）分工（与 v4.7 提示 CAP-19/20 的做法一致，为可比性保留），会高估真实口语化/复合意图准确率，词面代理 8/18 正说明无提示时的难度；路由用例为原型化 prompt、judge 只看能力索引；5-skill catalog 沿用 v4.7（本机实际用户级 skills 仅 `cangjie-skill` / `officecli1098`，工作区级 `fda-pchf-food-safety`，`brand-ip` / `pdf2md-pro` 属评测设定，其 sibling 命中不代表宿主真实可激活）；输出只跑机械断言，未做 A/B 偏好盲评、人工复核与工具调用审计；触发未作统计非劣声明；未测 also_read 辅读链。
- **历史欠账已关闭**：v4.8 的 10 条 `fsvp-*` 与 v4.9 的 10 条 `seafood-*`（CAP-22）用例曾列为「仍未补测」，**11-06 晚已在 v4.10 产物上补测完成**（20 条触发 60/60、输出 20/20、路由 138/138，CAP-21 33/33 / CAP-22 33/33），详见 「v4.8 / v4.9 历史用例补测」小节 与 `.cangjie/v4-8-v4-9-legacy-eval-report.md`。**以下仍未关闭**：输出 6/10 说明单次作答对 expected_behavior 的逐点覆盖仍有取舍，若要提升需改 CAP-23 卡片 E 段输出清单或出卡模板（本版未改产物）；统计非劣、A/B 盲评、人工复核、端到端激活日志均未做。完整报告与复现命令见 `.cangjie/v4-10-eval-report.md`。


## v4.8 / v4.9 历史用例补测（只做评测，未发新版）

- **触发原因**：v4.8 / v4.9 发布时各自写明「10 条用例与 CAP-21 / CAP-22 路由待补测」，v4.10 补测报告又把它列为「仍未关闭」；用户 11-06 晚要求「顺手把那 20 条历史用例也用同一框架跑掉」。
- **范围纪律**：只做评测，正式 `test-prompts.json`、`SKILL.md`、`dist-v14`、已安装 v4.10 一律未改动；评测后复核产物与安装目录仍 **28 文件、逐文件 sha256 差异 0**。全部产物落在 `.cangjie/v4-8-v4-9-legacy-eval/`（新增 4 个脚本）；三版历史评测结论原样保留、不改写、不冒用。
- **两处历史文本差异**：① v4.9 的 10 条 `seafood-*` **只有 `notes`、没有 `expected_behavior`**，输出断言改由 `notes` + 已安装 CAP-22 卡片正文锚定，未臆造 expected_behavior；② v4.8 的 `fsvp-06/07/10` 仍写「全包十四类不可混引」（当时口径），当前已升十五类，断言写成 `十[四五]类`，**正式用例原文一字未改**。
- **① 确定性静态核对**（`.cangjie/check_legacy_routing.py`，不依赖 LLM）：**23/23 PASS** —— `verified.yaml` 23 卡且 CAP-21 / CAP-22 均 `active`（also_read 8 / 10 条）、`destinations.json` 23 去向、能力索引 / cheatsheet / SKILL.md 路由表主行各 1 行、两卡副本一致、两卡均按当前口径标「十五类不可混引」、产物与安装目录 hash 差异 0。**词面代理只判对 9/20**（CAP-21 4/10、CAP-22 5/10），说明纯关键词不区分「法定义务 / 进口商检查程序 / 技术判定链」，准确率以语义盲判为准。
- **② 触发评测**：38 条（20 历史用例 + v4.7 原样复用 8 sibling + 10 负例）× 3 轮 = **114 判**，官方 score 得 **TP 60 / FP 0 / FN 0 / TN 54，F1 1.000，兄弟混淆率 0.000（0/24）**；**20 条历史用例单独 60/60**（10 条 `fsvp-*` 与 10 条 `seafood-*` 各 30/30）。
- **③ 输出质量评测**：20 条 × 2 变体 = 40 份答案、81 条机械断言，**`v410_skill 20/20` / `without_skill 11/20`**，断言级 81/81 vs 71/81，逐例 9 胜 11 平 0 负。**该 20/20 有解释边界**：历史用例描述粒度不均（v4.9 只有一句 notes），71/81 断言两变体都通过、11 例为平局，明显比 v4.10 按 expected_behavior 逐点抽取的 6/10 更基础，**两者不可横向比较**。抽查技能答案确认非空过（`except they must comply with section 1.509`、`§123.9(b)(1)` 逐字原文、`§123.3(q)` 的 should 定义）。**严格化敏感性套件**（`score_legacy_output_strict.py`，每条追加 1 条卡片独占锚点断言，共 101 条，只加不减）：**`v410_skill 20/20`（101/101 全过）/ `without_skill 7/20`**，独占锚点命中 skill 20/20 vs baseline 8/20、逐例 13 胜 7 平 0 负 —— 既验证含金量，也量化主套件断言偏基础的虚高幅度。**主结果仍以 81 条断言的 20/20 为准**。
- **④ 能力卡路由评测**：46 条（23 卡各 1 条 + 20 条历史 prompt 直接作定向题 + 3 条 CAP-23 对照）× 3 轮 = **138 判**，**top-1 138/138 = 1.000**、重复一致 46/46、非法 slug 0；**CAP-21 33/33、CAP-22 33/33、CAP-23 12/12、三卡交叉错判 0**。`seafood-10` 的 notes 明说分流 CAP-22 与 CAP-20、top-1 本无唯一解，已单独披露 3 轮选卡分布并给出**不含该条的稳健数字 135/135**。结论：CAP-21（FSVP 检查程序层）与 CAP-22（Part 123 法条层）均稳定命中，互不吞噬，也未被 CAP-23 抢走。
- **局限（随数字一起读）**：judge 为同一底座模型的干净 sub-agent，非宿主端到端激活日志；路由 `instruction` 已点名 CAP-21/22/23 三层分工（沿用 v4.7 / v4.10 做法，为可比性保留），会高估真实口语场景；词面代理 9/20 即反证；用例为原型化 prompt、judge 只看能力索引；5-skill catalog 沿用 v4.7 评测设定（`brand-ip` / `pdf2md-pro` 本机未安装）；输出只跑机械断言，无 A/B 偏好盲评、人工复核、工具调用审计；触发未作统计非劣声明；未测 also_read 辅读链。
- **历史欠账结论：已关闭。** 完整报告与复现命令见 `.cangjie/v4-8-v4-9-legacy-eval-report.md`。

## v4.11 — CP 7303.842 落为第十六来源 + 海产品检查判定链（24 张卡）

- **触发与范围**：用户先安装用户级技能 `pdf2md-pro`，随后提供官方 508-Compliant PDF `20250929_CP 7303.842 Seafood Processor, Products, And Importer Inspection Program 508-Compliant.pdf`。该件是 `PIPELINE_STATE.md` v4.10 段「仍未收」清单的**第一项**，且 v4.6 / v4.7 / v4.8 三次明确暂缓未纳入。经选项确认，用户选择「纳入为第十六来源 + 1 张卡」，继续 single 输出、不另起技能包。
- **版本判定（第四次同型纠错）**：封面 `IMPLEMENTATION DATE 11/01/2023`、`Correction date: 09/30/2025`、`Date of Issuance: 09/30/025`（PDF 文本层残缺），正文页脚 `11/1/2023`，PDF creationDate `2025-09-29` → 文件名 `20250929` **只是生成日**，本件是 **2023-11-01 版程序的 2025-09-30 更正本**，与 CP 7303.050 / 7303.070 / 7303.878 同形态，不同于 CPGM 7303.040 的 `2025-CPM-HFP-001`。首页 NOTE 与 PART I 另写明 **CP 7303.842 与 CP 7303.844 已合并为单一程序**，但 PAC 仍分进口 `03844x` / 国产 `03842x`。
- **转换**：为跑技能第 0 步，在 `python3`（3.13.14）安装 `pymupdf4llm 2.1` / `pymupdf 2.1`；`PYTHONUTF8=1` 下转出 179,812 字节 / 1,334 行 / 203 表格行 / 148 书签全命中 / 0 残留页码。正式来源 `source-cp-7303-842-2023.md`（194,080 字节 / 1,373 行）= 文件头（版本、效力层级、与既有来源接口、关键口径、转换局限、十六类引用规范）+ `## 正文（转换原文，未改写）` + 原文。已知局限与 `source-cp-7303-878-2023.md` 同型：书签标题与 `# **…**` 伪标题并存导致 PART 各出现两次、H1 虚高 133，检索以 PART / 小节 / 表号为准；`UnicodeDecodeError` 与 RapidOCR 提示不影响文本层输出。
- **阶段 0–5**：并行产出 `candidates/v4-11-framework.md`（整书理解 / 完整检查判定链 / 阈值清单）、`v4-11-quotes.md`（36 段逐字引用候选）、`v4-11-counter-examples.md`（14 条反例 + 9 张卡 also_read 建议）；阶段 1.6 决定只新增 1 张卡、不晋级独立 Skill。
- **CAP-24 `seafood-inspection-program`**（33,921 字节 / 294 行 / 36 个引用块 + 44 intents / 182 keywords）：主题是**完整检查判定链**——Table 1 产品/工艺风险 + Table 2 work planning → 六类检查分流 → HACCP Program Evaluations → Sampling 三类与 PAC/PAF → PART IV A–G 与 CPG 判据出口 → PART V Table 4 ranking（case-by-case）→ FIELD REPORTING 收口；并给出三层配对（CAP-22 法条层 / CAP-23 指南层 / 本卡检查程序层）、双向误读防护、PAC 双码表与 `03842H` 同名不同义、阈值性质、ATTACHMENT A 适用域、十六类不可混引与转换质量红线。
- **引文核验**：`.cangjie/verify_v4_11_quotes.py` 用 `body_only()` 只取正文分界之后、先 `strip_md()` 剥离 `**`、`<u>`、`<br>`、`#`、行首 `o` / `•` 等转换标记再归一化比对，避免文件头自我验证循环。结果 **36/36 逐字命中正文区**，0 超 100 词、0 表格管道引用 → `RESULT: PASS`。
- **规模变化**：23 → **24 张卡**；182 → **192 条术语**（t183–t192）；115 → **125 条用例**（`seafood-inspection-01..10`）；十五类 → **十六类来源**；core_principles 45 → **48**；stop_conditions 20 → **22**；additional_sources +1；`verified.yaml` / `destinations.json` / `book/` 由 `.cangjie/assemble_bundle.py` 重生成，未手改生成物。
- **两轮口径回补策略**：`apply_v4_11_revisions.py`（21 文件 / 50 动作）用 `rep_once()` 唯一性断言 + 内存暂存 + 备份 + 末尾一次性落盘；**禁止「十五类 → 十六类」全局替换**（「第十五类」含该子串），`notes` 演进行、术语自检行与带 `v4.10` 版本注记的历史陈述整行跳过，只改确定性当前口径短语与明确点名的当前版本行，并补写 `test-prompts.json` 的 v4.11 演进句。第二轮 `apply_v4_11_cp842_residue.py`（6 文件 / 19 处）专清既有卡片中约 20 处把 CP 7303.842 写成「正文本包未收 / 请提供后纳入 / 转引未收」的**当前断言**（含 CAP-22 B1「本卡最大缺口」整段改写、CAP-23 开头仍未收清单、LACF / FSVP / 迎检卡的相邻 program 已收清单），统一改成「自 v4.11 起已收（CAP-24，检查程序作业层）+ 双向误读防护」；明确带「在 v4.8 及以前」「本包此前」的历史陈述原样保留。全库复扫只剩这 2 处历史句含「未收」。
- **评测状态**：（当时）本版**未重跑**触发 / 输出 / 路由评测，10 条 `seafood-inspection-*` 用例与 CAP-24 路由正确性待后续补测，v4.7 / v4.10 / 历史补测的既有结论不得冒用 —— **11-07 已补测完成**：静态登记 20/20 PASS、触发 F1 0.964（84 判，2 个 FP 全来自一条跨法域边界题）、输出 `v411_skill 10/10 / without_skill 4/10`（严格套件 3/10）、路由 top-1 **111/111**（CAP-24 定向 **24/24**、三层交叉错判 0），详见下方「v4.11 补充质量评测」小节与 `.cangjie/v4-11-eval-report.md`。
- **仍未收**：CPG Sec. 540.525 / 540.370 / 555.600 / 562.300 / 540.250 / 540.590 全文、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、NSSP Guide 与 Model Ordinance、BAM / AOAC / LIB / MPM 方法全文、Import Alert 16-74 / 16-20 / 99-41 全文、21 CFR part 1 subpart L、IOM Chapter 4、FDA 3501 / 3502 表单全文、Seafood List、eNSpect / CMS / FACTS / MARCS-CMS 内部系统、FDA–NMFS MOU / FMD#-029。
- **编译与安装（已完成）**：`assemble_bundle.py` 重生成事实源 → `compile_single.py --bundle .cangjie/capabilities --out dist-v15 --variant single` 产出 **29 个 .md / 24 张卡**（SKILL.md description 4827 字符）；`validate_skill_pack.py dist-v15` **0 errors + 1 warning**（`name-dir` 产物目录名固有提示）；`.cangjie/install_v11.py` 覆盖安装到工作区级 `.workbuddy/skills/fda-pchf-food-safety/`，旧版备份 `backups/fda-pchf-food-safety-v4.10-20261107-005244`；安装后官方校验 **0 errors / 0 warnings**，产物与安装目录 **29/29 文件、逐文件 sha256 差异 0**，glossary 5 份副本 hash 全同（`e468e517717c9c6f…`）、严格 `yaml.safe_load` 192 条 id 唯一。完整审计见 `.cangjie/v4-11-sources-qa-report.json`。

## v4.11 补充质量评测（10 条用例 + CAP-24 路由；只做评测，未改正式套件 / 产物 / 安装）

- **触发与范围**：v4.11 发布时写明「10 条 `seafood-inspection-*` 用例与 CAP-24 路由待补测」，按 v4.10 / 历史补测的同一框架补跑。只做评测：正式 `test-prompts.json`、`SKILL.md`、`dist-v15`、已安装技能一律未改动，评测后复核产物与安装目录仍 29 文件、hash 差异 0。全部产物隔离在 `.cangjie/v4-11-eval/`（新增脚本 `build_v4_11_eval_suites.py` / `check_v4_11_routing.py` / `score_v4_11_routing.py`）。
- **方法与口径**：官方 `run_trigger_evals.py` / `run_output_evals.py` 判分 + 自建 `score_v4_11_routing.py`；3 个干净 sub-agent 独立盲判；5-skill catalog、`edge_case → should_trigger`、v4.7 的 8 sibling + 10 负例原文不改写；新增 1 份「只加不减」的严格化输出套件（每条追加 1 条卡片独占锚点）。
- **① 静态登记核对**（`.cangjie/check_v4_11_routing.py`）：**20/20 PASS** —— 24 卡 / CAP-24 `active`·`extended`·also_read 9 条、48 principles / 22 stops、15 个 additional_sources 且末条为 `src-fda-cp-7303-842-2023`、24 去向、能力索引 / cheatsheet / 路由表主行各 1 行、双向辅读 10 行、SKILL.md 无「十五类」残留、两份卡片一致且含 36 个引用块、产物与安装目录 hash 差异 0。**词面代理只判对 12/26**（CAP-24 定向 8/18），反证语义盲判必要。
- **② 触发评测**：28 条（10 新 + 8 sibling + 10 负例）× 3 轮 = **84 判**，官方 score **TP 27 / FP 2 / FN 0 / TN 55，precision 0.931 / recall 1.000 / F1 0.964，兄弟混淆率 0.000（0/24）**；9 条 should_trigger 新用例 27/27 全中。**2 个 FP 全部来自 `seafood-inspection-10`**（跨法域负例里夹了「FDA 检查应对承诺函」，3 位判官 2:1 分歧），主结果按 0.964 如实保留，不改 prompt 或放宽判据；剔除该边界题的敏感性数字为 81 判 F1 1.000，与 v4.7 `secg-edge-02` 同属跨法域边界的 should_not_trigger 语义分歧。
- **③ 输出质量评测**：10 条 × 2 变体 = 20 份答案，主套件 40 条机械断言 → **`v411_skill 10/10（40/40）` / `without_skill 4/10（27/40）`**，逐例 4 平 6 胜 0 负；严格套件 50 条断言 → **`v411_skill 10/10（50/50）` / `without_skill 3/10（32/50）`**，3 平 7 胜 0 负。卡片独占锚点覆盖 `IMPLEMENTATION DATE`、`03842H 同名不同义`、`HIGHER RISK`、`ISSC / 483 / HFP`、`702(b)`、`Not applicable`、`PART IV · 6 subs`、`Significance must be determined / CMS`、`part 1 subpart L / §805`、`out_of_scope`。**防泄漏复核**：首次技能组答题指令过细、疑似镜像断言，已用中性指令（只读参考材料 + 完整回答子问）重跑覆盖 10 份答案，重判结果完全一致，排除提示词泄漏导致的虚高。仍有 4 条（严格 3 条）两变体都过，属描述性断言，区分度主要由技能独占通过的 6 / 7 条提供；10/10 不与 v4.10 的 6/10、历史补测的 20/20 横比。
- **④ 能力卡路由评测**：37 条（24 卡各 1 + CAP-24 定向 7 + CAP-23 定向 3 + CAP-22 定向 3）× 3 轮 = **111 判**，**top-1 111/111 = 1.000**、重复一致 37/37、非法 slug 0；**CAP-24 定向/基础 24/24**、CAP-23 12/12、CAP-22 12/12；**三层配对交叉错判全 0**（CAP-24↔CAP-23、CAP-24↔CAP-22、CAP-23↔CAP-22 六个方向均为 0）。
- **局限（随数字一起读）**：judge 为同一底座模型的干净 sub-agent，非宿主端到端激活日志；路由 `instruction` 已点名 CAP-22/23/24 三层分工（沿用 v4.7 / v4.10 为可比性保留），会高估真实口语场景；5-skill catalog 是评测设定而非本机实际安装清单；用例为原型化 prompt、judge 只看能力索引；输出只有机械断言，无 A/B 偏好盲评、分歧样本人工复核、工具调用审计，未测 `also_read` 辅读链；触发未作统计非劣声明；2 个 FP 集中在 1 条边界题，样本小，不推断总体误触发率。
- **结论：v4.11 评测欠账已关闭。** 完整报告与复现命令见 `.cangjie/v4-11-eval-report.md`。
