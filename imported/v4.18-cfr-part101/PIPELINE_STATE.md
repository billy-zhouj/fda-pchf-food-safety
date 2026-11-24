# PIPELINE_STATE — cfr-part101-2026

> cangjie-skill RIA-TV++ v2.5 流水线状态。断点续跑时先读本文件。

## 任务定位

- **类型**：`update/repair`（沿用原输出模式，**不新建独立技能**）
- **目标技能**：用户级 `C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety`
- **基线版本**：v4.17（29 张主卡 + 10 张 imports 子卡 / 21 类来源 / 六套法规编号 / `single` 变体）
- **目标版本**：**v4.18**（30 张主卡 + 10 张 imports 子卡 + **5 张 labeling 子卡** / **22 类来源** / **七套法规编号**〔§ 101.xxx〕）
- **用户确认（2026-11-09）**：① 全量 50 条款；② 1 入口 CAP-30 + 5 子卡形态

## 来源

| 项 | 值 |
|---|---|
| 输入 PDF | `G:/下载/21 CFR Part 101 (up to date as of 11-05-2026).pdf` |
| 规模 | 352 页 / 70 书签 / 50 条款 / 7 Subpart / 4 Appendix / 3.5 MB |
| 转换产物 | `source-cfr-part101-2026.md`（1,121,933 字节 / 17,498 行） |
| 转换器 | `.cangjie/convert_part101.py` |
| 自检报告 | `.cangjie/part101-convert-report.json` |
| 分块 | `.cangjie/chunks/chunk-01..09.md` + `index.json` |

## 阶段进度

| 阶段 | 状态 | 产物 / 备注 |
|---|---|---|
| 0 整书理解 | ✅ 完成（用户已确认） | `BOOK_OVERVIEW.md`；骨架 7 层、12 术语、4 组批判、接口清单 6 行 |
| 1 五路并行提取 | ✅ 完成 | 182 个方法类候选 + 44 术语；556 个英文引用段逐字核验全命中、0 漏检；50/50 条款全覆盖 |
| 1.5 三重验证 | ✅ 完成 | `verified.md`（V1 跨域 / V2 预测力 / V3 独特性 5/5 通过）+ `rejected/merged-duplicates.md` |
| 1.6 晋级门 | ✅ 完成 | `.cangjie/capabilities/destinations.json`（5 单元全部判 router；1 入口服务 5 单元） |
| 2 RIA++ 能力卡 | ✅ 完成 | `.cangjie/capabilities/cards/*.md`（5 张）+ 入口卡 + `.cangjie/capabilities/verified.yaml`；**93 个引用块 93/93 PASS** |
| 3 Zettelkasten | ✅ 完成 | `GLOSSARY.md`（t234–t277）+ 子卡 also_read 互链 + 术语接入安装目录词典 |
| 4 压力测试 | ✅ 完成 | `test-results/phase4-cases.json` 10 条（5 should_trigger / 2 edge_case / 2 router_reachable / 1 should_not_trigger 互斥负例） |
| 5 编译与安装 | ✅ 完成 | 增量升级安装目录：v4.17 → **v4.18**；备份 45 文件；`.cangjie/apply_v4_18.py` + `.cangjie/validate_v4_18.py` 全绿（0 fail / 0 warn） |

## 关键约定（全程锁定）

1. **法规正文层**：〔§ 101.xxx〕是**第七套独立编号**，与〔§ 108/113/114/117/120/123.xxx〕并列，不是上下位、不是新旧替代。
2. **效力栈**：法规正文（七套）＞ FDA 指南（should 建议层）＞ CPGM／CP／IOM 检查程序（检查员视角、不创设企业义务）。
3. **二十二类不可混引**：既有 21 类 + 21 CFR Part 101。
4. **接口红线**：Part 117〔§ 117.135(c)(2)〕管「标签控制怎么管」，Part 101 管「标签内容是什么」；**标签合规 ≠ 安全合规**，两者不得互引条款号替代。
5. **不可逐字引用区**：§101.12 Table 1/2（113 页流式列值）、Appendix B/C/D 图形、9 个纯图形页（44/45/51/239/240/344/347/348/351）。
6. **引用纪律**：英文引用块 ≤100 词/段，须标〔§ 101.xxx〕+ pdf-page，逐字核验脚本待写。
7. **不重编 dist**：主流水线 `assemble_bundle.py` 停在 v4.16（28 卡），缺 v4.17 的 CAP-29 与 imports 子卡；本次**直接对已安装目录做增量升级**（v4.17 同款做法），先备份再改，不重跑会丢内容的旧编译器。

## 变更日志

- 2026-11-09 15:0x — 建立目录、探测 PDF、加载 cangjie-skill 方法论
- 2026-11-09 15:1x — 阶段 0 转换：发现并修复 Prince 浮动标题错位（改用 block 坐标重排）、标题跨行合并、Subpart F 截断、Appendix 双破折号；自检 50/50 条款、0 噪声残留
- 2026-11-09 15:2x — `BOOK_OVERVIEW.md` 落盘；向用户展示骨架并确认范围与形态
- 2026-11-09 15:3x — 分块 chunk-01..09（按条款边界，§101.12 表单独成块）；启动 5 路 extractor 并行提取
- 2026-11-09 16:0x — 5 路提取完毕：framework 88 / principles 48 / cases 26 / counter-examples 20 / glossary 44；引用逐字核验全命中
- 2026-11-09 16:1x — 落 `verify_part101_quotes.py` 校验器；阶段 2 并行构造 5 张 RIA++ 子卡（V01–V05）+ CAP-30 入口卡；93 个引用块 93/93 PASS
- 2026-11-09 16:2x — 写 `verified.yaml` / `destinations.json` / `verified.md`；备份 v4.17 安装目录（45 文件）
- 2026-11-09 16:4x — `apply_v4_18.py` 干跑通过（修正 1 处路由锚点措辞：进口准入**与**处置链）；`--apply` 写入 10 文件：SKILL.md / capability-index / cheatsheet / overview / glossary（t01–t277）/ test-prompts（191 用例，version 4.18）+ 审计件
- 2026-11-09 16:4x — `validate_v4_18.py` 全包静态校验：12 必需文件、前 30 卡普查（30 主卡 + 10 imports + 5 labeling）、277 术语唯一、191 用例、路径完整性、子卡六段结构——**0 fail / 0 warn**；安装版 5 张子卡引用复核 93/93 PASS

## 最终交付状态（v4.18）

- **规模**：30 张主卡 + 10 张 imports 子卡 + 5 张 labeling 子卡 / 277 条术语（t01–t277）/ 191 条测试用例 / **二十二类来源 / 七套法规编号**
- **新增**：第二十二来源 21 CFR Part 101（eCFR 2026-11-05 快照）→ **CAP-30 `food-labeling-requirements`** 入口 + 5 张子卡
- **安装目录**：`C:\Users\HG\.workbuddy\skills\fda-pchf-food-safety`（51 文件）
- **备份**：`backups/fda-pchf-food-safety-v4.17-20261109-161215`（45 文件）
- **校验**：9 项静态检查全绿 + 93/93 引用逐字核验 PASS
