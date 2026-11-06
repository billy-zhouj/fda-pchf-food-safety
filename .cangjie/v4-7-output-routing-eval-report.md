# v4.7 补充质量评测报告 — 触发增强 / 输出质量 / 能力卡路由

- **触发原因**：v4.7 触发盲测（`.cangjie/v4-7-trigger-eval-report.md`，F1 1.000）有 6 条解读限制：每例仅 1 次、无 sibling 用例、负例仅 5 条、未评测能力卡路由正确性、judge 只看浓缩技能目录、不作统计非劣声明。用户选择「补跑输出与路由评测」以补齐其中可补的部分。
- **范围**：只做评测，**不改动正式 `test-prompts.json`、不改动已安装 v4.7 技能包、不发新版本**。所有套件、任务包、结果、报告均在 `.cangjie/v4-7-output-routing-eval/` 独立目录。
- **评测前基线复核**：安装目录官方 `validate_skill_pack.py` = `0 errors, 0 warnings`；20 卡 / 152 术语 / 85 用例 / CAP-20 present / 「十类不可混引」残留 0；5 份 glossary 副本 sha256 全同。

---

## 一、增强触发评测（官方 `run_trigger_evals.py`）

**套件** `trigger-suite-v2.json`：85 条原用例（沿用 v4.7 的 `edge_case → should_trigger` 映射）+ **8 条 sibling**（对应本机真实已安装的 `pdf2md-pro` / `brand-ip` / `cangjie-skill` / `officecli1098`，每个 2 条）+ **10 条新增负例**（上证指数、快排、21 CFR 210/211 药品 cGMP、9 CFR 416/417 肉类、GB 2763、EC 852/2004、ISO 22716、采购合同、天气、日译）= **103 条，全部 `runs: 3`**。split 62/41（seed 42），`prepare --set all` 生成 103 个盲测包。

**执行**：3 个互相独立的干净 sub-agent，各把 103 条完整判一遍，分别写 `results-trigger/run1|2|3.jsonl`，即构成每例 3 次独立重复；合并为 309 行 `results.jsonl`。三轮覆盖完整（各 103 行 / 103 唯一 case_id / 无 missing / 无 extra），**跨轮分歧 0 例**。

**官方 score 主结果**

| 指标 | 值 |
|---|---|
| runs | 309 |
| TP / FP / FN / TN | 237 / 0 / 3 / 69 |
| precision / recall / **F1** | 1.000 / 0.988 / **0.994** |
| **兄弟混淆率** | **0.000（0/24）** ← v4.7 原报告的 `0/0` 空值已补齐 |

8 条 sibling 在 3 轮中全部命中各自 `sibling_target`，无一条误选 `fda-pchf-food-safety`；15 条负例（5 原有 + 10 新增）全部判 `none`。

**唯一失败项 `secg-edge-02`（3 个 FN 全来自这一条）**

- prompt：`帮我按中国 GB 14881 出一份可直接签发的食品厂 cGMP 内审检查表，顺便把药品 21 CFR 211 的偏差调查要求也写进去。`
- 正式套件把它标为 `edge_case`，`expected_behavior` 原文是「**应明确告知超出本包覆盖，不硬套**……本卡与全包只提供 FDA 口径；中国 GB 14881 功能上大致对应 Subpart B 但条款体系与法定口径不同……药品 cGMP 是 21 CFR Parts 210/211，与人类食品 Part 117 不是同一体系」。
- 3 个 judge 判 `none` 的理由高度一致：「中国国标与药品 cGMP」「GB14881 与药品 211」「中外标准文档生成」。
- 已核对已安装 `SKILL.md` 的「不适用」段落**明确列有**「中国 GB 14881 等非美国法规的直接合规判定（本技能只提供 FDA 方法论与条款，跨体系映射需人工判断）」。因此判 `none` 与技能包自身停用条件一致，**不是技能漏触发**，而是把「应告知越界」类边界用例一律映射为 `should_trigger` 的评测口径错配。
- **口径敏感性分析**（`trigger-suite-v2-alt.json`：仅把该条按正式套件原始语义改为 `should_not_trigger`，其余不动）：TP 237 / FP 0 / FN 0 / TN 72，**F1 1.000**。此结果只用于展示口径影响，**主结果仍以 0.994 为准**，不用来粉饰。

---

## 二、输出质量评测（官方 `run_output_evals.py` 确定性机械断言）

**套件** `output-suite.json`：10 条 output case，共 27 条机械断言（`regex` / `contains` / `not_contains`），其中 out-01..07 针对 v4.7 新增或纠错的条款级知识（§113.100(g)(h) 的 1+2 年 + part 11、§114.100(e) 整段 3 年、Part 110 未移除、§117.1(c)/§117.5(d) 并行与条件豁免、§113.3 的 4.6/0.85、scheduled process、十二类不可混引），out-08..10 为三变体都应能过的难度基线（六列工作表、过敏原 Ed.5、迎检记录）。

**三变体**：`v47_skill`（读已安装 v4.7）、`v46_skill`（读 `backups/fda-pchf-food-safety-v4.6-20261106-132910`，19 卡）、`without_skill`（指令要求不读取任何本地技能文件，仅凭自身知识）。官方 `prepare` 生成 30 个匿名任务包（`vA/vB/vC` 随机映射 + `mapping.json` 单独存放），按 label 分给 3 个干净 sub-agent，各写 10 份 `.md`；同一 case 的 3 个变体来自不同 agent。30 份输出全部存在且非空（2,976–7,485 字节）。

**官方 score 结果（全部断言通过的 case 比例）**

| 变体 | 通过 | 失败项 |
|---|---|---|
| **v47_skill** | **10/10** | 无 |
| v46_skill | 8/10 | `out-02` 未写出 `114.100(e)`；`out-07` 仍写「十类不可混引」 |
| without_skill | 8/10 | `out-03` 缺 2018 撤回指令；`out-07` 明确拒答「当前共有 N 类来源」 |

**人工抽查确认断言失败确实对应版本差**：

- `out-02` 的 v46 输出写「21 CFR part 113 / 114 的法规正文未纳入本体系，涉及这两 part 具体记录条款只能标注『转引未收』，不得从检查员作业文件（CP 7303.070）反推条文」——正是 v4.6 的真实边界；v47 输出则逐字给出〔§ 114.100(e)〕原文并说明「没有 1+2 分段、没有 (h) 款、Part 114 全文无 electronic / part 11 字样」。
- `out-07` 的 v46 输出标题为「当前共十类来源（"十类不可混引"）」；v47 输出为「共 12 类，统一执行『十二类不可混引』」并列出三套法规正文编号；without 输出写「一个具体文档把来源分成几类是该文档内部编排约定……仅凭公开的 FDA 法规知识不能断言当前共有 N 类」，可佐证 `without_skill` 条件被遵守（至少该例）。
- **结论**：v4.7 在两处「本版新增知识点」上独占通过；未发现 v4.7 输出错误。

---

## 三、能力卡路由正确性评测（官方无此评测器，自建确定性判分）

**套件** `routing-suite.json`：20 条用例，覆盖 **20 张能力卡各 1 条**，每条给 `expected_capability`；候选清单来自已安装 `references/capability-index.md`（卡 id / 标题 / 重要度 / 意图 / 关键词 / 卡路径）。`packets-routing/route-01..20.json` 只给 prompt + 候选清单，隐藏 expected。

**执行**：2 个干净 sub-agent 各完整判 20 条，写 `results-routing/batch1|2.jsonl`；`.cangjie/score_routing_eval.py` 判分。

| 指标 | 值 |
|---|---|
| 判分记录 | 40（20 用例 × 2 次，来自不同 agent） |
| **top-1 命中** | **40/40 = 1.000** |
| 重复判断一致 | 20/20 |
| 非法 slug | 0 |
| 混淆对 | 无 |

包括最易混的 CAP-19（CP 7303.070 检查分流）与 CAP-20（Part 113/114 法规正文义务）两轮均正确命中。

---

## 四、发现与建议（不改变当前结论）

1. **技能包无需修复、无需发版**：输出评测未发现 v4.7 事实性错误，路由评测 20 卡全中，安装目录官方校验仍 `0 errors / 0 warnings`。本次为质量增强，不是缺陷修复。
2. **评测套件设计建议（非技能包缺陷）**：v4.7 适配器把 `edge_case` 一律映射为 `should_trigger`，会与「应明确告知超出覆盖」这类停用条件用例冲突。建议未来把边界用例拆成两类：`edge_scope_out`（按停用条件，不触发）与 `edge_reroute`（触发但需换卡/辅读），避免再出现 `secg-edge-02` 这类口径错配。
3. 触发描述本身可考虑补一条「跨体系/跨行业边界咨询（GB 14881、21 CFR 210/211 等）也会激活本技能并给出越界告知」——但这是产品取舍，需用户确认后才改 `SKILL.md` 并发版，本次未动。

---

## 五、方法与局限（必须连同数字一起读）

- **触发**：3 次重复来自 3 个独立 sub-agent，但均为同一底座模型，跨轮 0 分歧既说明判断确定、也可能反映模型同质化；judge 拿到的是 5 个技能的浓缩职责说明 + 判断原则，不是完整 `SKILL.md` frontmatter；未作统计非劣声明（仍需预注册界值 + McNemar / 配对 Bootstrap）。
- **输出**：本次只跑官方脚本的**确定性机械断言**环节；官方注释明确「A/B 盲评与分歧样本人工复核另行进行」，故**未做** A/B 偏好盲评、未做人工复核、不宣布非劣。变体条件是任务包内的 `condition_hint` 指令级约束，未做工具调用审计，无法 100% 排除越界读取。7/10 用例三变体全通过，说明多数断言对模型先验知识不敏感，不能据此夸大「有技能 vs 无技能」的差距；`without_skill` 仅 8/10 也说明基线本身不弱。
- **路由**：用例按各卡「意图 / 关键词」反向编写，属原型化、对号入座式 prompt，难度偏低；judge 预先读到完整 `capability-index.md` 浓缩索引，且指令中提示了 CAP-19/CAP-20 的区分规则；因此 1.000 **不代表真实用户口语化、模糊或复合意图下的路由准确率**。未测 also_read 辅读链是否正确、未测答案内容质量。
- **三块评测的共同边界**：都是技能层/卡层的离线代理评测，不是真实宿主环境的端到端激活日志；正式 `test-prompts.json` 与已安装 v4.7 均未改动。

---

## 六、产物清单（均在 `.cangjie/v4-7-output-routing-eval/`）

| 文件 | 内容 |
|---|---|
| `trigger-suite-v2.json` / `.split.json` / `trigger-suite-v2-alt.json` | 103 条增强触发套件、切分、口径敏感性套件 |
| `output-suite.json` / `routing-suite.json` | 10 条输出套件、20 条路由套件 |
| `packets-trigger/`（103）、`packets-output/`（30 包 + 30 份 `.md` + `mapping.json`）、`packets-routing/`（20） | 官方 prepare 生成的盲测任务包与输出 |
| `results-trigger/run1..3.jsonl` + `results.jsonl`（309 行）；`results-routing/batch1..2.jsonl`（40 行） | 干净 sub-agent 原始盲判结果 |
| `trigger-eval-report-v2.md` / `trigger-eval-report-v2-alt.md` | 官方触发判分（主 / 敏感性） |
| `output-eval-report.md` | 官方机械断言判分 |
| `routing-eval-report.md` | 自建路由判分（逐例 / 混淆对 / 被误选次数） |
| 本报告 | 汇总 |

生成与判分脚本：`.cangjie/build_v4_7_eval_suites.py`、`.cangjie/finalize_eval_packets.py`、`.cangjie/score_routing_eval.py`。
