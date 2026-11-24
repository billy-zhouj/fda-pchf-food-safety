# PIPELINE_STATE — 21 CFR Part 172 → CAP-31 增量升级（v4.18 → v4.19）

## 目标

把 eCFR 2026-11-05 现行版 **21 CFR Part 172《Food Additives Permitted for Direct Addition to Food for Human Consumption》**（178 页 / 198 书签 / 154 条款 / 9 Subpart）蒸馏为可执行能力，增量升级用户级技能 `C:\Users\HG\.workbuddy\skills\fda-pchf-food-safety`。

## 用户已确认的决策

| 决策点 | 结论 |
|---|---|
| 蒸馏范围 | **全量 154 条款 + 分层主次**：通用效力层与高风险重点类逐条展开；长尾物质（§172.510/§172.515 名录等）只做「查表导航 + 定位规则」 |
| 编号与形态 | **新增第八套法规编号〔§ 172.xxx〕**，新增 **CAP-31 `direct-food-additives` 入口 + 5 张子卡**；口径升级为**二十三类不可混引 / 八套编号**；版本 v4.18 → **v4.19** |
| 子卡拆分 | V01 许可判定链与限制五形态（横切）/ V02 防腐剂与抗菌剂 / V03 甜味剂与脂肪替代物 / V04 品质功能类与长尾名录导航 / V05 效力层与 IBR 边界（横切） |

## 关键事实（阶段 0 实测）

- 转换：`.cangjie/convert_part172.py`，**154/154 条款命中**、9 Subpart、**16 张表格**按词级坐标重建、0 噪声残留、6,575 行 / 390 KB。
- 限制形态分布：**ppm 数值 80 / 仅 GMP 34 / 仅限特定食品 8 / 功能限定 11 / 无明显限制 21**。
- 模板语法覆盖率：量化限制 66% / 身份定义 44% / 纯度规格 40% / IBR 引用 **27%** / 「To assure safe use」25%。
- 体量集中：§172.515（834 行）、§172.510（366 行）、§172.886（310 行）、§172.864（199 行）四条约占全文 26%。

## 目录

| 内容 | 路径 |
|---|---|
| 整书理解 | `BOOK_OVERVIEW.md` |
| 转换件 | `source-cfr-part172-2026.md` |
| 分块 | `.cangjie/chunks/chunk-01..04.md` + `index.json` |
| 候选池 | `candidates/framework.md` / `principles.md` / `cases.md` / `counter-examples.md` / `glossary.md` |
| 验证 | `verified.md` / `rejected/` |
| 能力卡 | `.cangjie/capabilities/cards/*.md` + `verified.yaml` + `destinations.json` |
| 安装备份 | `backups/` |

## 阶段进度

| 阶段 | 状态 | 备注 |
|---|---|---|
| 0 整书理解 | ✅ 完成（用户已确认） | 骨架 9 Subpart、限制五形态、模板四段、接口 4 条、批判 4 条 |
| 1 五路并行提取 | ✅ 完成 | framework 16 / principles 15 / cases 15 / counter-examples 19 / glossary 41；引用 **142/142** 逐字命中 |
| 1.5 三重验证 | ✅ 完成 | 65 方法候选 → 5 单元，通过 5 / 淘汰 0；`verified.md` + `rejected/merged-duplicates.md` |
| 1.6 晋级门 | ✅ 完成 | 5/5 判 router；`destinations.json` + `verified.yaml`；1 入口服务 5 单元 |
| 2 RIA++ 能力卡 | ✅ 完成 | 5 张子卡（V01–V05）+ CAP-31 入口卡，六段齐全 |
| 3 Zettelkasten | ✅ 完成 | `GLOSSARY.md`（41 条）；术语 t278–t318 并入安装包 glossary（318 条）；also_read 关系 12 条 |
| 4 压力测试 | ✅ 完成 | 13 条用例（should_trigger 7 / edge_case 2 / router_reachable 2 / should_not_trigger 2），含四类兄弟诱饵 |
| 5 编译与安装 | ✅ 完成 | 备份 v4.18 → 增量改安装目录 → 静态校验 **0 FAIL / 0 WARN** |

---

## v4.19 交付状态（2026-11-10）

- **技能包**：`fda-pchf-food-safety` v4.18 → **v4.19**（新增第二十三来源 CAP-31 `direct-food-additives`）
- **安装包普查**：**57 文件 / 31 张主卡 + 10 imports + 5 labeling + 5 additives 子卡 / 318 条术语（t01–t318）/ 204 条测试用例**
- **本来源规模**：154 条款 / 9 Subpart / 178 页；限制五形态（数值上限 80 / 仅 GMP 34 / 仅限食品 8 / 功能限定 11 / 无限制语 21）= 154/154
- **转换件**：`source-cfr-part172-2026.md`（6,575 行 / ~390 KB；154/154 条款、16 张表重建、0 噪声残留、174/178 页）
- **校验**：`.cangjie/verify_part172_quotes.py` → 候选池+6 卡 **142/142**、术语 **41/41**；`.cangjie/validate_v4_19.py` → **0 FAIL / 0 WARN**
- **备份**：`backups/fda-pchf-food-safety-v4.18-20261110-104537`

## 关键约定（全程锁定）

1. **法规正文层**：〔§ 172.xxx〕是**第八套独立编号**，与〔§ 101/108/113/114/117/120/123.xxx〕并列。
2. **效力栈**：法规正文（八套）＞ FDA 指南（should）＞ CPGM／CP／IOM 检查程序。
3. **二十三类不可混引**：既有 22 类 + 21 CFR Part 172。
4. **三条分工红线**：Part 172 许可 ≠ Part 101 标签写法 ≠ Part 117 过程控制；§172.5(b) 明文不免除其他义务。
5. **五形态纪律**：有条款 ≠ 有 ppm 上限；有 ppm ≠ 全食品适用。
6. **IBR 纪律**：43 条（27%）纯度规格整体引用到 FCC / 厂商方法 / AOAC，**只可引「须符合某文件」，不可转述数值**。
7. **不可逐字引用区**：16 张重建表格数值、§172.510/§172.515 名录、全部 IBR 外部文件。
8. **不重编 dist**：直接对已安装目录增量升级，先备份。

## 变更日志

- 2026-11-10 08:1x — 探测 PDF（178 页 / 198 书签 / 154 条款 / 9 Subpart）；确认同为 Prince 16.2 生成，浮动标题缺陷必然复现
- 2026-11-10 08:2x — 写 Part 172 专用转换器：因本件主体是表格，改用**词级坐标重建行 + 水平空隙 >20pt 切单元格**（Part 101 用的 block 级方法会丢列结构）；修 1 处死循环（prose 分支漏 `i += 1`）
- 2026-11-10 08:3x — 转换器打磨：表头堆叠还原（`Food` / `Limitations ... parts per million`）、折行续接（`mixes`）、脚注不并入数据行、单双行「表格」降级为文本行；最终 154/154 条款、16 表、0 噪声
- 2026-11-10 08:4x — `BOOK_OVERVIEW.md` 落盘；统计限制五形态与模板覆盖率；向用户确认范围与子卡拆分；切 4 块；启动五路提取- 2026-11-10 09:xx–11:xx — 阶段 1 五路提取（因上游限流改为主代理顺序执行）：framework 16 / principles 15 / cases 15 / counter-examples 19 / glossary 41；`verify_part172_quotes.py` 首轮 13/15 → 修 §172.730(a)(2) 与 §172.831(b) 两处引用措辞后 142/142 PASS。
- 2026-11-10 11:xx — 阶段 1.5/1.6：65 候选 → 5 单元（PASS 5 / 淘汰 0）；5/5 判 router；落 `verified.md`、`rejected/merged-duplicates.md`、`.cangjie/capabilities/{destinations.json,verified.yaml}`。
- 2026-11-10 11:xx–12:xx — 阶段 2：写 5 张 RIA++ 子卡 + CAP-31 入口卡；三处引用 MISS（入口卡两处说明行、V05 一处省略号）修复后候选池+6 卡 142/142 PASS。
- 2026-11-10 12:xx — 阶段 3：`GLOSSARY.md`（41 条）；t278–t318 并入安装包 glossary YAML 块（318 条连续）；追加 v4.19 增量表。
- 2026-11-10 12:xx — 阶段 4：`test-results/phase4-cases.json` 13 条；合并进 `test-prompts.json`（191 → 204，version 4.19）。
- 2026-11-10 12:xx — 阶段 5：备份 v4.18 → 增量改 SKILL.md（frontmatter 31 / 描述段 / 原则 #37 八套二十三类 / 新原则 #58 / 路由行 / 纪律段）+ capability-index + cheatsheet + overview + glossary + test-prompts；`validate_v4_19.py` **0 FAIL / 0 WARN**。
