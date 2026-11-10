# v4.8 / v4.9 历史用例补测 — 10 条 `fsvp-*` + 10 条 `seafood-*`（CAP-21 / CAP-22 路由）

- 执行日期：2026-11-06
- 触发：用户要求「顺手把那 20 条历史用例也用同一框架跑掉」，关闭 `PIPELINE_STATE.md` 中 v4.8 / v4.9 遗留、且被 v4.10 补测报告列为「仍未关闭」的评测欠账
- 方法：**完全沿用 v4.10 补充质量评测的框架** —— 官方 `run_trigger_evals.py` / `run_output_evals.py` 判分，能力卡路由用与 `.cangjie/score_routing_eval.py` 同型的自建判分器；干净 sub-agent 盲判；`edge_case → should_trigger` 沿用 v4.7 适配器口径；5-skill catalog 与 v4.7 / v4.10 一致；输出变体沿用 `v410_skill` / `without_skill`（跑的是当前已安装的 v4.10 产物）
- 产物目录：`.cangjie/v4-8-v4-9-legacy-eval/`

## 0. 范围纪律与两处历史文本差异

- **只做评测**：正式 `test-prompts.json`、`SKILL.md`、`dist-v14/`、已安装 `.workbuddy/skills/fda-pchf-food-safety/` 一律未改动；评测后复核产物与安装目录仍 **28 文件、逐文件 sha256 差异 0**。v4.7 / v4.8 / v4.9 / v4.10 的历史版本陈述原样保留，v4.7 的 F1 1.000 / 0.994、输出 10/10、路由 40/40 未被改写或冒用。
- **差异 1（v4.9）**：10 条 `seafood-*` 只有 `notes`、**没有 `expected_behavior`**；其输出断言改由 `notes` + 已安装 CAP-22 卡片正文的知识点锚定，不臆造一份 expected_behavior 出来。10 条 `fsvp-*` 则有完整的逐点 `expected_behavior`。
- **差异 2（v4.8 旧口径）**：`fsvp-06/07/10` 的 `expected_behavior` 仍写「全包十四类不可混引」（v4.8 当时口径），当前 v4.10 已升为**十五类**。断言写成 `十[四五]类`，**正式用例原文一字未改**，避免把历史文本改写成当前口径。
- 新增 4 个脚本 + 评测目录；文档侧仅回补 `PIPELINE_STATE.md` 的三处历史「待补测」行与两处「仍未关闭」表述，并在 v4.10 报告末尾追加回指注记。

## 1. 四层证据

### 1.1 确定性静态核对（不依赖 LLM，可重复复现）

`check_legacy_routing.py` → `v4-8-v4-9-legacy-eval/static-routing-check.md`，**23/23 PASS**：

`verified.yaml` 23 卡，CAP-21 / CAP-22 均 `status=active` 且 also_read 非空（8 / 10 条）；`destinations.json` 23 去向且两卡均 → `fda-pchf-food-safety`；`capability-index.md` / `cheatsheet.md` / `SKILL.md` 路由表主行各有且仅有 1 行；两卡在 `dist-v14` 与安装目录的副本各自内容一致；两卡开头均按当前口径标「十五类不可混引」；产物与安装目录 28 文件 hash 差异 0。

- **词面代理（IDF 加权关键词）只判对 9/20**（CAP-21 定向 4/10、CAP-22 定向 5/10）。中文口语化 prompt 与英文 keyword 表错位、且 CAP-21 / CAP-22 / CAP-23 在 `hazard analysis` / `importer` / `HACCP` 上重叠，纯词面无法表达「问法定义务 / 进口商检查程序 / 技术判定链」的差别。该层只证明登记完整，**准确率结论一律以语义盲判为准**。

### 1.2 触发评测（官方 `run_trigger_evals.py score`）

套件 38 条 = **20 条历史用例** + v4.7 原样复用的 8 条 sibling + 10 条负例；每条 `runs: 3`，3 个干净 sub-agent 各完整判一遍 = **114 判**。

```
runs: 114（TP 60 / FP 0 / FN 0 / TN 54）
precision 1.000 / recall 1.000 / F1 1.000
兄弟混淆率 0.000（0/24）
```

**20 条历史用例单独 60/60**：10 条 `fsvp-*` + 10 条 `seafood-*`（含 `edge_case` 的 `seafood-10`）每轮全判 `fda-pchf-food-safety`；8 条 sibling 各 3 次全中各自兄弟技能，10 条负例全判 `none`。20 条历史的 `notes` / `expected_behavior` 都明确要求激活技能，故 `edge_case → should_trigger` 映射语义正确。

### 1.3 输出质量评测（官方 `run_output_evals.py score` 机械断言）

20 条 output case、2 变体 = **40 份答案**，主套件 **81 条断言**（`fsvp-out-01` 为 5 条，其余 4 条）：

```
v410_skill:     20/20
without_skill:  11/20
断言级：skill 81/81，baseline 71/81
逐例：skill 胜 9/20、平 11/20、负 0/20
```

**这个 20/20 必须带解释读，不能直接当成「技能在 20 个 case 上全面胜出」**：

- 历史用例本身描述粒度不均。v4.9 的 10 条只有一句话 `notes`，断言多为「条款号 + 常见结论」，baseline 凭自身知识即可命中；**71/81 条断言两变体都通过（零区分度）**，逐例有 11 例是平局。
- v4.10 补测的 6/10 是按 `expected_behavior` **逐点抽取**、覆盖次要要点（第 4 栏理由、六栏↔十栏映射、Ch.4–21 四段式）；本套断言明显更基础，**20/20 与 6/10 不可横向比较**。
- 抽查 `v410_skill` 答案确认不是空过：`fsvp-out-01` 逐字给出 `except they must comply with section 1.509` 与 `An importer that is not a receiving facility`；`sf-out-04` 逐字给出 `§123.9(b)(1)` 冷藏 1 年 / 冷冻 2 年原文及 (b)(2) 起算点；`sf-out-09` 逐字给出 `§123.3(q)` 对 should 的定义与 `§123.11(b)(c)` 的 shall。

**严格化敏感性分析**（`score_legacy_output_strict.py`，只加不减、不放宽）：给每条 case 追加 1 条「卡片独占锚点」断言（CAP-21 / CAP-22 卡片正文里的精确原文或精确款号，共 **101 条断言**）：

```
v410_skill:     20/20（101/101 断言全过）
without_skill:   7/20
卡片独占锚点：  skill 20/20，baseline 8/20
逐例：skill 胜 13/20、平 7/20、负 0/20
```

即：**在要求写出卡片独占精确口径后，技能加持答案仍全过，无技能对照从 11/20 掉到 7/20**。这既验证了 20/20 的含金量，也量化了主套件断言偏基础造成的虚高幅度。主结果仍以 81 条断言的 20/20 为准。

### 1.4 能力卡路由评测（`score_legacy_routing.py`）

套件 46 条 = **23 张卡各 1 条基础** + **20 条历史用例 prompt 直接作为定向题** + 3 条 CAP-23 对照；3 个干净 sub-agent = **138 判**：

```
top-1 命中            138/138 = 1.000
排除开放边界题后       135/135 = 1.000
重复判断一致          46/46
非法 slug              0
CAP-21 定向/基础       11 条 ×3 = 33 判，命中 33/33
CAP-22 定向/基础       11 条 ×3 = 33 判，命中 33/33
CAP-23 对照/基础        4 条 ×3 = 12 判，命中 12/12
三卡交叉错判           0
```

20 条历史 prompt 中，v4.8 的 10 条 `expected_behavior` 均明写主卡 `fsvp-inspection-program`；v4.9 的 9 条 `notes` 均考 Part 123 法条层 → `seafood-haccp-statutory-requirements`。`seafood-10` 的 notes 明说「分流 CAP-22 与 CAP-20」，**top-1 本无唯一解**，按 notes 主卡记 CAP-22 并在报告中单独披露（3 轮选卡分布全为 CAP-22），另给不含该条的稳健数字 135/135。**结论：CAP-21（FSVP 检查程序层）与 CAP-22（Part 123 法条层）都稳定命中，既没有互相吃掉，也没被 CAP-23 技术指南层抢走。**

## 2. 历史欠账结论

**已关闭。** `PIPELINE_STATE.md` v4.8 的「10 条 `fsvp-*` 用例与 CAP-21 路由正确性待后续补测」、v4.9 的「10 条 `seafood-*` 用例与 CAP-22 路由待补测」，以及 v4.10 报告「仍未关闭」中的同一项，均已在当前 v4.10 产物上完成补测：静态登记 23/23 PASS、触发 60/60、输出主套件 20/20（严格套件仍 20/20）、路由 138/138 且 CAP-21 33/33 / CAP-22 33/33。三版历史评测结论原样保留，未冒用。

## 3. 局限（随数字一起读）

- judge 为同一底座模型的干净 sub-agent，**不是宿主端到端激活日志**；触发与路由均为盲判，非真实运行时的技能激活记录。
- 路由 `instruction` **已点名** CAP-21 / CAP-22 / CAP-23 三层分工（沿用 v4.7 提示 CAP-19/20、v4.10 提示 CAP-22/23 的做法，为可比性保留），会高估真实口语化 / 复合意图下的准确率；词面代理 9/20 正说明无提示时的难度。
- 路由用例为原型化 prompt，judge 看的是能力索引而非完整卡片正文；`seafood-10` 是显式多解边界题。
- 5-skill catalog 沿用 v4.7 评测设定；本机实际用户级 skills 仅 `cangjie-skill` / `officecli1098`、工作区级 `fda-pchf-food-safety` —— `brand-ip` / `pdf2md-pro` 的 sibling 命中**不代表宿主真实可激活**。
- 输出只跑机械断言；**主套件 71/81 断言零区分度**，20/20 的解释边界见 1.3。严格套件虽补了卡片独占锚点，仍不是 A/B 偏好盲评或人工复核。
- 触发为确定性判分，**未作统计非劣声明**；`edge_case → should_trigger` 是口径选择。未测 `also_read` 辅读链、工具调用审计。
- 输出变体的「条件」为指令级约束，`without_skill` 是否严格遵守「不读文件」未做工具调用审计。

## 4. 仍未关闭

- A/B 偏好盲评、分歧样本人工复核、统计非劣声明、端到端激活日志、`also_read` 辅读链评测，两轮补测均未做。
- v4.10 输出 6/10（敏感性 7/10）反映的「单次作答对 `expected_behavior` 逐点覆盖有取舍」问题依旧存在；本次严格套件证明卡片知识点能被读出，但**没有改动任何产物**（CAP-23 卡片 E 段输出清单 / 出卡模板均未调整）。
- 只做本地 commit，**未 push**；技能目录如要在当前会话触发仍需新开对话或重启。

## 5. 产物清单与复现

| 文件 | 内容 |
|---|---|
| `.cangjie/build_legacy_eval_suites.py` | 只读正式/历史套件，生成 3 个套件 + 盲判包（含 `output-case-map.json` / `routing-legacy-meta.json` 追溯表） |
| `.cangjie/check_legacy_routing.py` | CAP-21 / CAP-22 静态登记核对 → `static-routing-check.md` |
| `.cangjie/score_legacy_routing.py` | 路由判分 → `routing-eval-report.md`（含开放边界题单独统计） |
| `.cangjie/score_legacy_output_strict.py` | 严格化敏感性套件 → `output-suite-strict.json` / `output-eval-report-strict.md` |
| `v4-8-v4-9-legacy-eval/trigger-suite.json` / `packets-trigger/` / `results-trigger/` | 38 条触发套件、盲判包、3×38 判 |
| `v4-8-v4-9-legacy-eval/output-suite.json` / `packets-output/` | 20 条输出套件、40 个匿名任务与答案 |
| `v4-8-v4-9-legacy-eval/routing-suite.json` / `packets-routing/` / `results-routing/` | 46 条路由套件、盲判包、3×46 判 |
| `v4-8-v4-9-legacy-eval/{trigger,output,routing}-eval-report.md` | 三份官方 / 自建判分报告 |

复现：

```bash
python3 .cangjie/build_legacy_eval_suites.py
python3 .cangjie/check_legacy_routing.py
# 3 个干净 sub-agent 各判 packets-trigger/*.json → results-trigger/run{1,2,3}.jsonl
# 3 个干净 sub-agent 各判 packets-routing/*.json → results-routing/run{1,2,3}.jsonl
# 4 个干净 sub-agent 按 packets-output/*/task-*.json 写 <label>.md
cat results-trigger/run{1,2,3}.jsonl > results-trigger/results.jsonl
python3 <cangjie-skill>/scripts/run_trigger_evals.py score trigger-suite.json \
  --results results-trigger/results.jsonl --out trigger-eval-report.md
python3 <cangjie-skill>/scripts/run_output_evals.py score output-suite.json \
  --outputs packets-output --mapping packets-output/mapping.json --out output-eval-report.md
python3 .cangjie/score_legacy_routing.py
python3 .cangjie/score_legacy_output_strict.py
```
