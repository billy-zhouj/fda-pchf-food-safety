# 盲判说明（v4.8 / v4.9 历史用例补测）

- 触发：`packets-trigger/*.json` 共 38 条，3 个干净 sub-agent 各完整判一遍 → results-trigger/run{1,2,3}.jsonl。
- 输出：`packets-output/<case_id>/task-<label>.json` 共 40 个 → 按包内 output_file 写出 <label>.md；mapping.json 不得交给评审 sub-agent。
- 路由：本目录共 46 条，3 个干净 sub-agent 各完整判一遍 → results-routing/run{1,2,3}.jsonl。
- 所有 judge 只看 prompt + 候选索引，**不得**看到 suite 中的 expected / expected_capability。
