# v4.11 补充质量评测 — 10 条 `seafood-inspection-*` 用例 + CAP-24 路由

- **对象**：v4.11 / `dist-v15` / 工作区级已安装技能（24 张卡 / 192 术语 / 125 用例 / 十六类来源）。
- **范围纪律**：只做评测，正式 `test-prompts.json`、`SKILL.md`、`dist-v15`、已安装技能一律未改动；全部产物隔离在 `.cangjie/v4-11-eval/`。评测后复核 `dist-v15` 与安装目录仍 **29 文件、逐文件 sha256 差异 0**。
- **框架**：完全沿用 v4.7 / v4.10 / 历史补测——官方 `run_trigger_evals.py` / `run_output_evals.py` 判分，自建 `score_v4_11_routing.py`（同 `score_routing_eval.py` / `score_v4_10_routing.py` 口径），3 个干净 sub-agent 独立盲判；5-skill catalog、`edge_case → should_trigger`、v4.7 的 8 sibling + 10 负例原文均不改写，保证与前三版可比。
- **新增脚本**：`build_v4_11_eval_suites.py`（套件与盲判包）、`check_v4_11_routing.py`（静态登记）、`score_v4_11_routing.py`（路由判分）。

## ① 确定性静态核对（不依赖 LLM）

`check_v4_11_routing.py` → **20/20 PASS**：`verified.yaml` 24 卡且 CAP-24 `active` / `extended` / also_read 9 条；`book.additional_sources` 15 条（+主来源＝十六类），末条 `src-fda-cp-7303-842-2023`；`core_principles 48` / `stop_conditions 22`；`destinations.json` 24 去向；能力索引 / cheatsheet / SKILL.md 路由表主行各 1 行；CAP-24 双向辅读链 10 行；SKILL.md 已无「十五类」当前口径、含「24 张能力卡 / 十六类不可混引」；两份卡片内容一致且含 36 个逐字引用块；`dist-v15` 与安装目录 hash 差异 0。

**词面代理 top-1 只判对 12/26**（其中 CAP-24 定向/新用例 8/18）：CAP-22 法条层、CAP-23 指南判定链、CAP-24 检查程序层的关键词高度重叠（hazard analysis / CCP / histamine / 500 ppm / §123.6 等），纯词面无法表达「问的是法定义务、危害判定方法，还是 FDA 检查作业」的语义差别——这是仍需语义盲判的反证。

## ② 触发评测

28 条（10 条 v4.11 新用例 + v4.7 原样复用 8 sibling + 10 负例）× 3 轮 = **84 判**，官方 `score`：**TP 27 / FP 2 / FN 0 / TN 55，precision 0.931 / recall 1.000 / F1 0.964，兄弟混淆率 0.000（0/24）**。10 条新用例中 9 条 `should_trigger` 全部 27/27 命中；**2 个 FP 全部来自 `seafood-inspection-10`**：该跨法域负例的 prompt 同时写了「按中国 GB 2733 判定组胺」「欧盟法规卫生证书」与「**FDA 检查应对承诺函**」，3 位判官 2:1 分歧（2 人认为该激活技能以说明边界、1 人判 none）。

- **主结果以 0.964 为准，不通过改 prompt 或放宽判据把数字做漂亮。**
- 敏感性（仅作说明）：剔除该边界题后 81 判为 TP 27 / FP 0 / FN 0、F1 1.000；与 v4.7 `secg-edge-02` 的 3 个 FN 同属「跨法域边界题在 should_not_trigger 口径下的语义分歧」，不是漏触发。
- v4.10 的 F1 1.000 是上一版结论，不冒用；本版 0.964 也**不与** v4.7 / 历史补测直接横比（suite 组成不同）。

## ③ 输出质量评测

10 条 × 2 变体（技能加持 / 无技能基线）= 20 份答案，机械断言 `contains` / `not_contains` / `regex` 共 **40 条**：

| 套件 | 断言 | `v411_skill` | `without_skill` | 逐例（平 / 技能胜 / 基线胜） |
|---|---|---|---|---|
| 主套件 | 40 | **10/10（40/40）** | 4/10（27/40） | 4 平 / 6 胜 / 0 负 |
| 严格化敏感性（每条只**加** 1 条卡片独占锚点，只加不减） | 50 | **10/10（50/50）** | 3/10（32/50） | 3 平 / 7 胜 / 0 负 |

- 卡片独占锚点覆盖：`IMPLEMENTATION DATE` / `03842H 同名不同义` / `HIGHER RISK · not all inclusive` / `ISSC · 483 · HFP` / `702(b) · Domestic HACCP Verification` / `HACCP Verification · Not applicable` / `PART IV · 6 subs · 分解指示` / `Significance must be determined · CMS` / `part 1 subpart L · §805` / `out_of_scope · 法域`。严格套件把基线从 4/10 压到 3/10，技能保持 10/10，**量化了主套件偏基础的虚高幅度**。
- **防泄漏复核**：首次生成技能组答案时给的写作指令过细，疑似镜像断言；已用**中性指令**（只要求「按 condition_hint 读参考材料、完整回答所有子问」）重跑并覆盖 10 份技能答案，重新判分结果**完全一致**（主 10/10 vs 4/10、严格 10/10 vs 3/10），排除提示词泄漏导致的虚高。
- 仍有 4 条（严格套件 3 条）两变体都通过，属描述性断言（`FSVP` / `123.12` / `03842` / 跨法域拒绝），不能单独证明技能加持；区分度主要来自 6 条（严格 7 条）技能独占通过。

## ④ 能力卡路由评测

37 条（24 张卡各 1 条 + CAP-24 定向 7 条 + CAP-23 定向 3 条 + CAP-22 定向 3 条）× 3 轮 = **111 判**：

- **top-1 111/111 = 1.000**；重复判断一致 37/37；非法 slug 0。
- **CAP-24 定向/基础 24/24**（用户此前明确要求的「确认新卡路由命中」在 v4.11 的对应项）；CAP-23 12/12、CAP-22 12/12。
- **三层配对交叉错判全 0**：CAP-24→CAP-23 0、CAP-24→CAP-22 0、CAP-23→CAP-24 0、CAP-22→CAP-24 0、CAP-23→CAP-22 0、CAP-22→CAP-23 0。CAP-24 稳定承接「检查优先级 / Table 1·2 / PAC 码表 / 取样 / PART IV 触发值 / Table 4 / FIELD REPORTING」，既不吞掉法条层与指南层，也不被它们抢走。

## ⑤ 局限（随数字一起读）

- judge 均为同一底座模型的干净 sub-agent，非宿主端到端激活日志；路由 `instruction` 已点名 CAP-22 / 23 / 24 三层分工（沿用 v4.7 / v4.10 为可比性保留），会高估真实口语场景；词面代理 12/26 即反证。
- 5-skill catalog 沿用 v4.7 评测设定，不是本机实际安装清单；用例为原型化 prompt，judge 只看能力索引、不看完整卡片正文。
- 输出只跑机械断言：无 A/B 偏好盲评、无分歧样本人工复核、无工具调用审计、未测 `also_read` 辅读链；触发未作统计非劣声明（需预注册界值 + McNemar / 配对 Bootstrap）。
- 触发 0.964 的 2 个 FP 集中在 1 条跨法域边界题，样本量小，不推断总体误触发率。
- 输出 10/10 不可与 v4.10 的 6/10、历史补测的 20/20 横比：断言粒度、用例描述粒度、答题 agent 指令均不同；**主结果以本版 40 条断言的 10/10 为准**，严格套件只作区分度敏感性。
- **评测后的唯一产物改动**：补测完成后，仅把 `BOOK_OVERVIEW.md` 中两处带「当前」的 v4.10 规模说明改成明确历史措辞（「v4.10 当时为…」「v4.10 当时规模…」），重跑 `assemble_bundle.py` + `compile_single.py` 并同步安装目录 `references/overview.md`。未触及任何能力卡、路由表、术语、正式用例或断言；二次编译逐文件 hash 差异 0（编译器确定性已验证），`dist-v15` 与安装目录 29/29 文件 hash 差异 0、静态核对 20/20 PASS、安装目录官方校验 0 errors / 0 warnings。**评测结论不受影响**。

## ⑥ 产物与复现

- 套件：`trigger-suite.json`（28）、`output-suite.json`（10）、`output-suite-strict.json`（10）、`routing-suite.json`（37）
- 盲判包：`packets-trigger/`（28）、`packets-output/`（20 task + 20 答案）、`packets-routing/`（37）
- 结果：`results-trigger/run1-3.jsonl` + `results.jsonl`（84 行）、`results-routing/run1-3.jsonl`（111 行）
- 报告：`static-routing-check.md`、`trigger-eval-report.md`、`output-eval-report.md`、`output-eval-report-strict.md`、`routing-eval-report.md`
- 判分命令（工作目录为仓库根）：
  ```
  python3 .cangjie/build_v4_11_eval_suites.py
  python3 .cangjie/check_v4_11_routing.py
  python3 <cangjie-skill>/scripts/run_trigger_evals.py score .cangjie/v4-11-eval/trigger-suite.json --results .cangjie/v4-11-eval/results-trigger/results.jsonl --out .cangjie/v4-11-eval/trigger-eval-report.md
  python3 <cangjie-skill>/scripts/run_output_evals.py score .cangjie/v4-11-eval/output-suite.json --outputs .cangjie/v4-11-eval/packets-output --mapping .cangjie/v4-11-eval/packets-output/mapping.json --out .cangjie/v4-11-eval/output-eval-report.md
  python3 .cangjie/score_v4_11_routing.py
  ```

**结论**：v4.11 的 10 条 `seafood-inspection-*` 用例与 CAP-24 路由均已补测，CAP-24 路由 24/24 稳定命中、三层配对交叉错判 0；触发 F1 0.964（2 个 FP 全为一条跨法域边界题，如实保留）；输出技能加持 10/10 vs 基线 4/10（严格 3/10）。**本版评测欠账已关闭。**
