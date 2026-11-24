# CAP-24 路由命中 — 确定性静态核对（v4.11）

- PASS | verified.yaml 共 24 张卡 | 实得 24
- PASS | verified.yaml 含 CAP-24 且 capability_id 正确 | CAP-24
- PASS | CAP-24 importance / status | importance=extended status=active
- PASS | CAP-24 also_read 9 条 | 9
- PASS | book.additional_sources 15 条（+主来源 = 十六类） | 15
- PASS | 第十六来源 source_id 正确
- PASS | core_principles 48 / stop_conditions 22 | 48 / 22
- PASS | destinations.json 共 24 个去向 | 实得 24
- PASS | destinations.json CAP-24 → fda-pchf-food-safety
- PASS | 已安装 capability-index.md 含 CAP-24 行
- PASS | capability-index 的 CAP-24 行指向正确卡片
- PASS | cheatsheet.md 含 CAP-24 一句话规则行 | 命中 1 行
- PASS | SKILL.md 路由表含 CAP-24 主行（第 2 列为该卡） | 命中 1 行主行
- PASS | SKILL.md 中 CAP-24 被其它卡列为辅读（双向链） | 共 10 行含该 slug
- PASS | SKILL.md 已无「十五类」当前口径
- PASS | SKILL.md 含「24 张能力卡」与「十六类不可混引」
- PASS | CAP-24 卡片文件在 dist-v15 与已安装目录均存在
- PASS | 两份 CAP-24 卡片内容一致
- PASS | CAP-24 卡含 36 个逐字引用块
- PASS | dist-v15 与已安装目录逐文件 hash 一致 | files=29 diff=0

## 词面代理 top-1（弱证据，仅作诊断）

| case | 期望 | 词面 top-1 | 是否命中 | CAP-24 分 / top-1 分 |
|---|---|---|---|---|
| route-22 | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` | ✓ | 0.127 / 1.439 |
| route-23 | `seafood-hazards-controls-guide` | `hazard-analysis-method` | ✗ | 0.000 / 0.728 |
| route-24 | `seafood-inspection-program` | `seafood-inspection-program` | ✓ | 0.554 / 0.554 |
| cap24-a | `seafood-inspection-program` | `seafood-inspection-program` | ✓ | 0.584 / 0.584 |
| cap24-b | `seafood-inspection-program` | `seafood-inspection-program` | ✓ | 0.711 / 0.711 |
| cap24-c | `seafood-inspection-program` | `inspection-sampling` | ✗ | 0.165 / 0.597 |
| cap24-d | `seafood-inspection-program` | `seafood-inspection-program` | ✓ | 0.195 / 0.195 |
| cap24-e | `seafood-inspection-program` | `inspection-readiness` | ✗ | 0.165 / 0.801 |
| cap24-f | `seafood-inspection-program` | `seafood-haccp-statutory-requirements` | ✗ | 0.195 / 0.309 |
| cap24-g | `seafood-inspection-program` | `supply-chain-verification` | ✗ | 0.143 / 0.483 |
| cap23-a | `seafood-hazards-controls-guide` | `hazard-analysis-method` | ✗ | 0.000 / 0.728 |
| cap23-b | `seafood-hazards-controls-guide` | `hazard-analysis-method` | ✗ | 0.000 / 0.536 |
| cap23-c | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` | ✓ | 0.329 / 0.904 |
| cap22-a | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` | ✓ | 0.000 / 0.619 |
| cap22-b | `seafood-haccp-statutory-requirements` | `regulatory-boundaries` | ✗ | 0.000 / 0.702 |
| cap22-c | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` | ✓ | 0.000 / 1.074 |
| seafood-inspection-01 | `seafood-inspection-program` | `inspection-readiness` | ✗ | 0.389 / 0.739 |
| seafood-inspection-02 | `seafood-inspection-program` | `seafood-inspection-program` | ✓ | 0.516 / 0.516 |
| seafood-inspection-03 | `seafood-inspection-program` | `seafood-haccp-statutory-requirements` | ✗ | 0.000 / 0.619 |
| seafood-inspection-04 | `seafood-inspection-program` | `seafood-haccp-statutory-requirements` | ✗ | 0.195 / 0.309 |
| seafood-inspection-05 | `seafood-inspection-program` | `seafood-inspection-program` | ✓ | 0.359 / 0.359 |
| seafood-inspection-06 | `seafood-inspection-program` | `seafood-inspection-program` | ✓ | 0.516 / 0.516 |
| seafood-inspection-07 | `seafood-inspection-program` | `seafood-inspection-program` | ✓ | 0.718 / 0.718 |
| seafood-inspection-08 | `seafood-inspection-program` | `hazard-analysis-method` | ✗ | 0.291 / 0.728 |
| seafood-inspection-09 | `seafood-inspection-program` | `supply-chain-verification` | ✗ | 0.143 / 0.483 |
| seafood-inspection-10 | `seafood-inspection-program` | `seafood-haccp-statutory-requirements` | ✗ | 0.000 / 0.619 |

- 词面代理总体 top-1：12/26
- 其中 CAP-24 定向/新用例：8/18
- 说明：CAP-22（法条层）、CAP-23（指南判定链）、CAP-24（检查程序层）的关键词高度重叠（hazard analysis / CCP / histamine / 500 ppm / §123.6 等），纯词面无法表达「问的是法定义务、危害判定方法，还是 FDA 检查作业」这一语义差别；本层只证明登记完整，准确率结论以干净 sub-agent 盲判为准。

## 结论

- 登记完整性：全部 PASS
- 词面代理结果见上表，不用于宣布路由准确率。

