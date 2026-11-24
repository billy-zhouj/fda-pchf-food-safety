# PIPELINE_STATE — IOM 2026 Chapter 6: Imports

- **book_slug**: `iom-2026-ch6-imports`
- **工作根目录**: `E:/WeChatData/2026-11-09-08-58-24/books/iom-2026-ch6-imports/`
- **源文件**: `G:\下载\2026 IOM Chapter 6.pdf`
- **创建时间**: 2026-11-09
- **当前阶段**: ✅ 全部完成（阶段 0–5），已增量升级 `fda-pchf-food-safety` 至 **v4.17**
- **断点续跑**: 无；如需重跑，`.cangjie/apply_v4.17.py` 带幂等保护，备份在 `E:/WeChatData/2026-11-09-08-58-24/.pchf-backup-v4.16/`

## 阶段进度

| 阶段 | 状态 | 产出 / 备注 |
|---|---|---|
| 0 整章理解 | ✅ 完成（用户已确认骨架） | `BOOK_OVERVIEW.md`；全文 + TOC + 10 个分块索引 |
| 1 并行提取（5 extractors） | ✅ 完成 | `candidates/{framework,principle,case,counter-example,glossary}.md` 共 82 条 |
| 1.5 三重验证 | ✅ 完成 | 82 → 去重 20 → 通过 10、淘汰 10；`verified.md` + `rejected/R01–R10.md` + `verified-summary.txt` |
| 1.6 晋级门 | ✅ 完成 | 10 个单元全部 `router`，由 **CAP-29** 单一来源入口服务；`destinations.json`（可发现入口 = 1） |
| 2 RIA++ 能力卡 | ✅ 完成 | `.cangjie/capabilities/cards/*.md` × 10（2,528 行）+ `verified.yaml`（10 能力 / 14 条 also_read） |
| 3 Zettelkasten 链接 | ✅ 完成 | `GLOSSARY.md`（28 条）+ `book/{overview,glossary}.md` |
| 4 压力测试 | ✅ 完成 | 13 条评测（5 正面 / 3 兄弟诱饵 / 3 edge / 2 router）；首轮 96.7%，失败 1 条已定点修 A2；**独立复测 4/4 全对** |
| 5 编译与交付 | ✅ 完成 | `DIGEST.md`（7,967 汉字）+ CAP-29 入口卡 + 10 子卡；已写入 PCHF 包 v4.17（SKILL.md / capability-index / overview / glossary / cheatsheet / test-prompts），18 项校验通过 |

## 已建立的资产

- `source/iom-ch6-full.txt` — 全文，含 `[PAGE n]` 标记（239,840 字符）
- `source/toc.txt` — 235 条书签，含页码
- `.cangjie/index/*.txt` — 按 6.1…6.9 + Exhibits 切分的 10 个块，含 `[p.N]` 标记，页眉页脚已清理
- `.cangjie/index/MANIFEST.md` — 块清单与页码范围
- `BOOK_OVERVIEW.md` — 阶段 0 产出

## 关键约束（供续跑时读取）

1. 物理 PDF 页 = 印刷页码，引用一律用 `[p.N]`。
2. Exhibit 6-1~6-4（p.59–70）为扫描图像，文本层仅 588 字符，表单字段须标注"需查原件"。
3. 本文件是 FDA 内部操作手册，非法规；所有能力卡的 Boundary 必须写明法律位阶与版本时效。
4. 原文引用 ≤150 字/段（英文 ≤100 词/段）。
5. 用户视角偏好：见下方「用户确认记录」。

## 用户确认记录

- 阶段 0 骨架确认：✅ 2026-11-09 用户确认（三个 AskUserQuestion 回答均为「升级到 pchf 技能包中」）
- 输出模式选择：**增量升级既有技能包** `fda-pchf-food-safety`（非 cangjie 标准 single/pack 发布）；产物形态 = 1 个新增 CAP 入口 + 10 张子卡
- 安装位置：✅ 已安装到用户级 `C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety/`；工作区保留完整审计轨迹
- 视角偏好：原书 FDA 判定逻辑为准（R/I），A2 应用层给出企业迎检镜像并统一标注〔推导·非原书主张〕

## v4.17 写入清单（apply_v4.17.py）

1. `references/capabilities/iom-imports-procedure.md`（CAP-29 入口卡，29 KB）
2. `references/capabilities/imports/*.md` × 10
3. `SKILL.md`：frontmatter capability-count 28→29、description 追加、路由表插入 CAP-29 行、11 处精确更新 + 3 条新边界规则
4. `references/capability-index.md`：追加 CAP-29 行
5. `references/overview.md` / `glossary.md` / `cheatsheet.md`：v4.17 增量
6. `test-prompts.json`：version 4.16→4.17，168→181 条（+13）
7. 全包口径：二十类 → **二十一类不可混引**，28 → **29 张能力卡**，IOM Chapter 6 由「仍未收」改为「已收（CAP-29）」
