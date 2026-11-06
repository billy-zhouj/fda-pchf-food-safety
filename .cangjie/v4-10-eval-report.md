# v4.10 补充质量评测 — 10 条 `seafood-hazards-*` 用例 + CAP-23 路由命中

- 执行日期：2026-11-06
- 触发：用户要求「补跑那 10 条评测用例并确认 CAP-23 的路由命中」
- 方法：**完全沿用 v4.7 补充质量评测口径** —— 官方 `run_trigger_evals.py` / `run_output_evals.py` 判分，能力卡路由用与 `.cangjie/score_routing_eval.py` 同型的自建判分器；干净 sub-agent 盲判
- 产物目录：`.cangjie/v4-10-eval/`

## 0. 范围纪律

- **只做评测**：正式 `test-prompts.json`、`SKILL.md`、`dist-v14/`、已安装 `.workbuddy/skills/fda-pchf-food-safety/` 一律未改动。评测后复核 `dist-v14` 与安装目录仍 **28 文件、逐文件 sha256 差异 0**。
- 新增：3 个脚本（`build_v4_10_eval_suites.py`、`check_v4_10_routing.py`、`score_v4_10_routing.py`）+ `.cangjie/v4-10-eval/` 全部产物；文档侧仅回补 `PIPELINE_STATE.md` 的 v4.10「评测状态」行。
- 历史版本陈述原样保留：v4.7 的 F1 1.000 / 0.994、输出 10/10、路由 40/40 未改，也不冒用为 v4.10 结果。

## 1. 三层证据

### 1.1 确定性静态核对（不依赖 LLM，可重复复现）

`check_v4_10_routing.py` → `v4-10-eval/static-routing-check.md`，**14/14 PASS**：

`verified.yaml` 23 卡且 CAP-23 为 `extended` / `active`、also_read 9 条；`destinations.json` 23 去向且 CAP-23 → `fda-pchf-food-safety`；`capability-index.md` 有 CAP-23 行且指向正确卡片；`cheatsheet.md` 有 CAP-23 一句话规则行；`SKILL.md` 路由表有且仅有 1 行以 CAP-23 为主卡、另有 9 行把它列为辅读；两份 CAP-23 卡片内容一致；`dist-v14` 与安装目录 28 文件 hash 差异 0。

- 首次运行曾报 2 处 FAIL，核实为**检查判据写窄、非产物缺陷**：cheatsheet 用卡片标题而非 `CAP-23` 编号登记；SKILL.md 主行的子串匹配把 8 个「辅读列末尾是 CAP-23」的行误算为主行。改为按标题 / 按列判定后全 PASS。
- **词面代理（IDF 加权关键词打分）只判对 11/22、其中 CAP-23 相关 8/18**，多被 `hazard-analysis-method` 抢走。原因是 CAP-01 / CAP-22 / CAP-23 在 `hazard analysis` / `CCP` / `critical limit` / `reasonably likely to occur` 等词上大量重叠，词面无法表达「问的是法定义务还是判定方法」。该层只证明登记完整，**准确率结论一律以语义盲判为准**。

### 1.2 触发评测（官方 `run_trigger_evals.py score`）

套件 28 条 = 10 条 v4.10 新用例 + v4.7 原样复用的 8 条 sibling + 10 条负例；每条 `runs: 3`，3 个干净 sub-agent 各完整判一遍 = **84 判**。

映射沿用 v4.7 适配器：`edge_case → should_trigger`。本次 `seafood-hazards-08/09` 的 `expected_behavior` 明确要求激活技能（「必须同时纠正两个方向的误读」「必须分清可答与转引未收」），故该映射语义正确，不同于 v4.7 `secg-edge-02` 那类口径错配。

```
runs: 84（TP 27 / FP 0 / FN 0 / TN 57）
precision 1.000 / recall 1.000 / F1 1.000
兄弟混淆率 0.000（0/24）
```

其中 **10 条新用例单独 30/30**：9 条应触发 ×3 = 27 TP，1 条跨法域负例 `seafood-hazards-10` ×3 = 3 TN。8 条 sibling 各 3 次全中各自兄弟技能，10 条负例全判 `none`。

### 1.3 输出质量评测（官方 `run_output_evals.py score` 机械断言）

10 条 output case，每条 4 条断言（共 40 条，全部锚定 v4.10 新增知识点），2 变体 `v410_skill` / `without_skill` = 20 份答案：

```
v410_skill:     6/10
without_skill:  2/10
逐例：skill > baseline 7/10、持平 2/10、更差 1/10
```

- 本次断言按 `expected_behavior` **逐点抽取**（每 case 4 点），比 v4.7 多数 case 的 2–3 条更严，**6/10 不可与 v4.7 的 10/10 直接比较**。
- 4 条未全过的人工复核：
  - `sh-out-05`：断言 `Table 3-4` 未收合法简写「3-4」（技能答案写「Table 3-2/3-3 与 3-4」）→ **断言措辞缺陷**。另存 `output-suite-corrected.json` 敏感性套件（只改这 1 条正则，主套件不动），得 `v410_skill 7/10 / without_skill 2/10`、逐例 **7 胜 3 平 0 负**。**主结果仍以 6/10 为准**。
  - `sh-out-02`（第 4 栏理由）、`sh-out-04`（六栏↔十栏映射）、`sh-out-07`（Ch.4–21 四段式）：答案核心判定正确但未铺出该次要要点 → **单次作答取舍**。回查已安装 CAP-23 卡片：Column 4 理由 6 处、L226 六栏↔十栏映射表、L218 四段式、`Table 3-4` 6 处，**知识点在卡内齐备**，不是卡片缺陷。
- 无技能对照 2/10，技能加持在 9/10 个 case 上优于或持平对照。

### 1.4 能力卡路由评测（`score_v4_10_routing.py`）

套件 33 条 = **23 张卡各 1 条** + CAP-23 定向 7 条 + CAP-22 定向 3 条；3 个干净 sub-agent = **99 判**：

```
top-1 命中        99/99 = 1.000
重复判断一致      33/33
非法 slug          0
CAP-23 定向/基础   8 条 ×3 = 24 判，命中 24/24
CAP-22 定向/基础   4 条 ×3 = 12 判，命中 12/12
CAP-23 题→CAP-22   0 ；CAP-22 题→CAP-23  0
```

23 张卡的基础用例每卡均 3/3 命中，无混淆对、无被误选卡。完整逐例表见 `v4-10-eval/routing-eval-report.md`。

## 2. CAP-23 路由命中结论

**已确认。** 静态登记 14/14 PASS、语义盲判 CAP-23 **24/24**、与最易混的 CAP-22 交叉混淆 **0/0**、编译产物与安装副本 hash 一致。CAP-23 不是「编进去了但路由不到」的孤儿卡；且 CAP-22（法条层）没有被新卡吃掉。

## 3. 局限（随数字一起读）

- judge 为同一底座模型的干净 sub-agent，**不是宿主端到端激活日志**。
- 路由 `instruction` **已提示** CAP-22（法条层）/ CAP-23（指南判定链）的分工（与 v4.7 提示 CAP-19/20 的做法一致，为可比性保留），会高估真实口语化 / 复合意图下的准确率；词面代理 8/18 正说明无提示时的难度。
- 路由用例按各卡意图反向编写，属**原型化 prompt**；judge 看的是能力索引，不是完整卡片正文。
- 5-skill catalog 与 v4.7 完全一致以保证可比；本机实际用户级 skills 只有 `cangjie-skill` / `officecli1098`、工作区级有 `fda-pchf-food-safety` —— `brand-ip` / `pdf2md-pro` 属评测设定，其 sibling 命中**不代表宿主真实可激活**。
- 输出只跑机械断言，未做 A/B 偏好盲评、人工复核、工具调用审计；变体条件为指令级约束。
- 触发为确定性判分，**未作统计非劣声明**；`edge_case → should_trigger` 是口径选择。
- 未测 `also_read` 辅读链。

## 4. 仍未关闭

- **v4.8 的 10 条 `fsvp-*` 与 v4.9 的 10 条 `seafood-*`（CAP-22）用例仍未补测**。本次只跑用户指定的 v4.10 10 条 + CAP-23 路由；`PIPELINE_STATE.md` 中 v4.8 / v4.9 的「待后续补测」保持有效。
- 输出 6/10（敏感性 7/10）说明单次作答对 `expected_behavior` 的逐点覆盖仍有取舍。若要提升需调整 CAP-23 卡片 E 段的输出清单或出卡模板，**本版未改动任何产物**。
- 统计非劣、A/B 偏好盲评、分歧样本人工复核、端到端激活日志均未做。

## 5. 产物清单与复现

| 文件 | 内容 |
|---|---|
| `.cangjie/build_v4_10_eval_suites.py` | 只读正式/历史套件，生成 3 个套件 + 盲判包 |
| `.cangjie/check_v4_10_routing.py` | 确定性静态核对 → `v4-10-eval/static-routing-check.md` |
| `.cangjie/score_v4_10_routing.py` | 路由判分 → `v4-10-eval/routing-eval-report.md` |
| `v4-10-eval/trigger-suite.json` / `packets-trigger/` / `results-trigger/` | 28 条触发套件、盲判包、3×28 判 |
| `v4-10-eval/output-suite.json` / `packets-output/` | 10 条输出套件、20 个匿名任务与答案 |
| `v4-10-eval/routing-suite.json` / `packets-routing/` / `results-routing/` | 33 条路由套件、盲判包、3×33 判 |
| `v4-10-eval/{trigger,output,routing}-eval-report.md` | 三份官方/自建判分报告 |
| `v4-10-eval/output-suite-corrected.json` / `output-eval-report-corrected.md` | 仅修正 1 条断言措辞的敏感性套件与报告 |

复现：

```bash
python3 .cangjie/build_v4_10_eval_suites.py
python3 .cangjie/check_v4_10_routing.py
# 3 个干净 sub-agent 各判 packets-trigger/*.json → results-trigger/run{1,2,3}.jsonl
# 3 个干净 sub-agent 各判 packets-routing/*.json → results-routing/run{1,2,3}.jsonl
# 2 个干净 sub-agent 按 packets-output/*/task-*.json 写 <label>.md
cat results-trigger/run{1,2,3}.jsonl > results-trigger/results.jsonl
python3 <cangjie-skill>/scripts/run_trigger_evals.py score trigger-suite.json \
  --results results-trigger/results.jsonl --out trigger-eval-report.md
python3 <cangjie-skill>/scripts/run_output_evals.py score output-suite.json \
  --outputs packets-output --mapping packets-output/mapping.json --out output-eval-report.md
python3 .cangjie/score_v4_10_routing.py
```

## 6. 后续更新（2026-11-06 晚，回指注记）

本节第 4 节「仍未关闭」中「**v4.8 的 10 条 `fsvp-*` 与 v4.9 的 10 条 `seafood-*`（CAP-22）用例仍未补测**」是**本报告撰写当时**的状态，现已被后续补测关闭，故在此追加回指、不改写当时的结论：

- 用户随后要求「顺手把那 20 条历史用例也用同一框架跑掉」。已按本报告的同一框架（官方 `run_trigger_evals.py` / `run_output_evals.py` + 同型路由判分器、干净 sub-agent 盲判、5-skill catalog、`v410_skill` / `without_skill`）完成补测。
- 结果：静态登记 **23/23 PASS**；触发 38 条 ×3 = 114 判 **F1 1.000**（20 条历史用例 60/60）；输出主套件 **`v410_skill 20/20` / `without_skill 11/20`**（严格化敏感性套件 20/20 vs 7/20）；路由 46 条 ×3 = **138/138 = 1.000**，**CAP-21 33/33、CAP-22 33/33、CAP-23 12/12、三卡交叉错判 0**。
- 完整报告：`.cangjie/v4-8-v4-9-legacy-eval-report.md`；产物目录：`.cangjie/v4-8-v4-9-legacy-eval/`；`PIPELINE_STATE.md` 的 v4.8 / v4.9 状态行与「历史欠账」表述已同步回补。
- 本报告其余结论（尤其输出 **6/10** 及其不可与历史用例 20/20 横向比较的说明）依然有效；A/B 盲评、人工复核、端到端激活日志等仍未关闭。
