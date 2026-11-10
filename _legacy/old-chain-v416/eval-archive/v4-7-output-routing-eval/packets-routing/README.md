# 盲判说明

- 触发：`packets-trigger/*.json` 共 103 条，3 个干净 sub-agent 各完整判一遍，分别写 results-run1/2/3.jsonl，即构成每例 3 次重复。
- 输出：`packets-output/<case_id>/task-<label>.json` 共 30 个，按包内 output_file 写出 <label>.md；映射表不得交给 sub-agent。
- 路由：本目录 route-*.json 共 20 条，2 个干净 sub-agent 分批盲判。
