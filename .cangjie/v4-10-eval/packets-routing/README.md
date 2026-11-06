# 盲判说明（v4.10 补测）

- 触发：`packets-trigger/*.json` 共 28 条，3 个干净 sub-agent 各完整判一遍，分别写 results-run1/2/3.jsonl，构成每例 3 次重复。
- 输出：`packets-output/<case_id>/task-<label>.json` 共 20 个，按包内 output_file 写出 <label>.md；mapping.json 不得交给评审 sub-agent。
- 路由：本目录 route-*.json / cap2*.json 共 33 条，3 个干净 sub-agent 分批盲判。
- 所有 judge 只看 prompt + 候选索引，**不得**看到 suite 中的 expected / expected_capability。
