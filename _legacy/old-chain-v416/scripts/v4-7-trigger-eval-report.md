# 触发评测判分 — fda-pchf-food-safety

- runs: 85（TP 80 / FP 0 / FN 0 / TN 5）
- precision 1.000 / recall 1.000 / **F1 1.000**
- 兄弟混淆率: 0.000（0/0）

| case | expected | selected | 判定 |
|---|---|---|---|
| should-trigger-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| should-trigger-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| should-trigger-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| should-trigger-04#r1 | should_trigger | fda-pchf-food-safety | TP |
| should-trigger-05#r1 | should_trigger | fda-pchf-food-safety | TP |
| should-trigger-06#r1 | should_trigger | fda-pchf-food-safety | TP |
| should-trigger-07#r1 | should_trigger | fda-pchf-food-safety | TP |
| should-trigger-08#r1 | should_trigger | fda-pchf-food-safety | TP |
| should-trigger-09#r1 | should_trigger | fda-pchf-food-safety | TP |
| should-trigger-10#r1 | should_trigger | fda-pchf-food-safety | TP |
| should-not-trigger-01#r1 | should_not_trigger | none | TN |
| should-not-trigger-02#r1 | should_not_trigger | none | TN |
| should-not-trigger-03#r1 | should_not_trigger | none | TN |
| should-not-trigger-04#r1 | should_not_trigger | none | TN |
| edge-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| edge-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| cfr-trigger-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| cfr-trigger-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| cfr-trigger-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| cfr-trigger-04#r1 | should_trigger | fda-pchf-food-safety | TP |
| cfr-trigger-05#r1 | should_trigger | fda-pchf-food-safety | TP |
| cfr-edge-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| cfr-edge-04#r1 | should_trigger | fda-pchf-food-safety | TP |
| term-rename-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-trigger-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-trigger-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-trigger-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-trigger-04#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-edge-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-edge-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-edge-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-edge-04#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-edge-05#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-edge-06#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-trigger-05#r1 | should_trigger | fda-pchf-food-safety | TP |
| lmono-trigger-06#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-trigger-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-trigger-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-trigger-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-trigger-04#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-trigger-05#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-trigger-06#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-edge-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-edge-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-negative-01#r1 | should_not_trigger | none | TN |
| secg-audit-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-qf-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-withdraw-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| secg-1175k-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| ed5-tree-nut-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| ed5-milk-eggs-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| ed5-freefrom-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| defect-level-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| defect-level-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| defect-level-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| inspection-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| inspection-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| inspection-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| inspection-04#r1 | should_trigger | fda-pchf-food-safety | TP |
| sampling-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| sampling-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| sampling-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| iom-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| iom-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| iom-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| iom-04#r1 | should_trigger | fda-pchf-food-safety | TP |
| iom-05#r1 | should_trigger | fda-pchf-food-safety | TP |
| lacf-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| lacf-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| lacf-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| lacf-04#r1 | should_trigger | fda-pchf-food-safety | TP |
| lacf-05#r1 | should_trigger | fda-pchf-food-safety | TP |
| lacf-06#r1 | should_trigger | fda-pchf-food-safety | TP |
| lacf-07#r1 | should_trigger | fda-pchf-food-safety | TP |
| lacf-08#r1 | should_trigger | fda-pchf-food-safety | TP |
| stat-01#r1 | should_trigger | fda-pchf-food-safety | TP |
| stat-02#r1 | should_trigger | fda-pchf-food-safety | TP |
| stat-03#r1 | should_trigger | fda-pchf-food-safety | TP |
| stat-04#r1 | should_trigger | fda-pchf-food-safety | TP |
| stat-05#r1 | should_trigger | fda-pchf-food-safety | TP |
| stat-06#r1 | should_trigger | fda-pchf-food-safety | TP |
| stat-07#r1 | should_trigger | fda-pchf-food-safety | TP |
| stat-08#r1 | should_trigger | fda-pchf-food-safety | TP |
| stat-09#r1 | should_trigger | fda-pchf-food-safety | TP |
| stat-10#r1 | should_trigger | fda-pchf-food-safety | TP |

> 本报告只给原始配对计数与比率；统计非劣需预注册界值 + McNemar/配对 Bootstrap（§10.3），不在此自动宣布。


---

## 方法与局限（v4.7 补跑说明）

- **执行时间**：v4.7 安装（`dist-v11` → `C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety`）之后，按用户选项「纳入后一起跑」补跑。
- **套件**：`test-prompts.json` v4.7 共 **85 条**（49 `should_trigger`、31 `edge_case`、5 `should_not_trigger`）。官方 `run_trigger_evals.py` 要求 `trigger_cases` / `suite_id` / `target` 结构，且把 `edge_case` 判为不应触发；本包是 **single 模式**，`edge_case` 仍应激活本技能（只是要路由到正确能力卡），故建适配器 `.cangjie/v4-7-trigger-eval/trigger-suite.json`，把 `edge_case` 映射为 `should_trigger`，其余原样映射；**未改动正式套件**。
- **切分**：`split` 固定种子 42、train_ratio 0.6 → train 51 / validation 34；`prepare --set all` 生成 85 个盲测包，评分覆盖全 85 条。
- **盲测执行**：候选技能为实际安装的 5 个（`fda-pchf-food-safety` / `brand-ip` / `cangjie-skill` / `officecli1098` / `pdf2md-pro`）。3 个**未参与蒸馏的干净 sub-agent** 分 3 批（29/29/27）独立判断，每批只允许读取该批 `batch-N.jsonl`（仅含 `case_id` + `prompt`），并明确禁止读取 `test-prompts.json`、`verified.yaml`、任何 `SKILL.md`/能力卡/`packets/` 或使用网络搜索；judge 只看到 prompt 文本与 5 个技能的浓缩描述目录。`results-batch-*.jsonl` 合并为 `results.jsonl` 后用官方 `score` 判分。
- **结果**：TP 80 / FP 0 / FN 0 / TN 5，precision 1.000 / recall 1.000 / **F1 1.000**；5 条 `should_not_trigger`（`should-not-trigger-01..04`、`secg-negative-01`）全部判为 `none`；新增 10 条 `stat-01..10` 全部正确激活；零误判。
- **⚠ 解读限制（不得当作统计非劣声明）**：① 每例只跑 **1 次**（官方默认 3 次），未做重复运行一致性检验；② 适配器无 `sibling` 类用例，故报告的「兄弟混淆率 0.000」是 **0/0 的空值**，不表示兄弟技能不混淆；③ 只有 5 条负例，negative 覆盖偏薄；④ `edge_case` 在技能层按「应触发」计分，**未评测能力卡路由正确性**（那需要另一套 output eval）；⑤ judge 看到的是浓缩技能目录，不是完整的 5 份 `SKILL.md` frontmatter；⑥ 本结果只给原始配对计数与比率，按官方脚本说明，统计非劣需预注册界值 + McNemar / 配对 Bootstrap，不在此宣布。
- **产物**：`.cangjie/v4-7-trigger-eval/`（适配器套件、split、85 个盲测包、3 份分批结果、合并 `results.jsonl`）、本报告。
