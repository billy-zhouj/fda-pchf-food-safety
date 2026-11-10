# CAP-23 路由命中 — 确定性静态核对（v4.10）

- PASS | verified.yaml 共 23 张卡 | 实得 23
- PASS | verified.yaml 含 CAP-23 且 capability_id 正确 | CAP-23
- PASS | CAP-23 importance / status | importance=extended status=active
- PASS | CAP-23 also_read 9 条 | 9
- PASS | destinations.json 共 23 个去向 | 实得 23
- PASS | destinations.json CAP-23 → fda-pchf-food-safety
- PASS | 已安装 capability-index.md 含 CAP-23 行
- PASS | capability-index 的 CAP-23 行指向正确卡片
- PASS | cheatsheet.md 含 CAP-23 一句话规则行 | 命中 1 行
- PASS | SKILL.md 路由表含 CAP-23 主行（第 2 列为该卡） | 命中 1 行主行
- PASS | SKILL.md 中 CAP-23 被其它卡列为辅读（双向链） | 共 9 行含该 slug
- PASS | CAP-23 卡片文件在 dist-v14 与已安装目录均存在
- PASS | 两份 CAP-23 卡片内容一致
- PASS | dist-v14 与已安装目录逐文件 hash 一致 | files=28 diff=0

## 词面代理 top-1（弱证据，仅作诊断）

| case | 期望 | 词面 top-1 | 是否命中 | CAP-23 分 / top-1 分 |
|---|---|---|---|---|
| route-22 | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` | ✓ | 0.176 / 1.441 |
| route-23 | `seafood-hazards-controls-guide` | `hazard-analysis-method` | ✗ | 0.482 / 0.717 |
| cap23-a | `seafood-hazards-controls-guide` | `hazard-analysis-method` | ✗ | 0.241 / 0.717 |
| cap23-b | `seafood-hazards-controls-guide` | `inspection-sampling` | ✗ | 0.241 / 0.318 |
| cap23-c | `seafood-hazards-controls-guide` | `hazard-analysis-method` | ✗ | 0.417 / 0.525 |
| cap23-d | `seafood-hazards-controls-guide` | `supply-chain-verification` | ✗ | 0.000 / 0.000 |
| cap23-e | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` | ✓ | 0.723 / 0.723 |
| cap23-f | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` | ✓ | 0.964 / 0.964 |
| cap23-g | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` | ✓ | 0.482 / 0.482 |
| cap22-a | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` | ✓ | 0.241 / 0.609 |
| cap22-b | `seafood-haccp-statutory-requirements` | `regulatory-boundaries` | ✗ | 0.000 / 0.691 |
| cap22-c | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` | ✓ | 0.353 / 1.055 |
| seafood-hazards-01 | `seafood-hazards-controls-guide` | `hazard-analysis-method` | ✗ | 0.482 / 0.717 |
| seafood-hazards-02 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` | ✓ | 0.241 / 0.241 |
| seafood-hazards-03 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` | ✓ | 0.241 / 0.241 |
| seafood-hazards-04 | `seafood-hazards-controls-guide` | `hazard-analysis-method` | ✗ | 0.000 / 1.434 |
| seafood-hazards-05 | `seafood-hazards-controls-guide` | `hazard-analysis-method` | ✗ | 0.241 / 0.717 |
| seafood-hazards-06 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` | ✓ | 0.964 / 0.964 |
| seafood-hazards-07 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` | ✓ | 0.723 / 0.723 |
| seafood-hazards-08 | `seafood-hazards-controls-guide` | `hazard-analysis-method` | ✗ | 0.241 / 0.717 |
| seafood-hazards-09 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` | ✓ | 0.482 / 0.482 |
| seafood-hazards-10 | `seafood-hazards-controls-guide` | `seafood-haccp-statutory-requirements` | ✗ | 0.000 / 0.305 |

- 词面代理总体 top-1：11/22
- 其中 CAP-23 定向/新用例：8/18
- 说明：关键词表在 CAP-22（法条层）与 CAP-23（指南判定链）之间大量重叠（hazard analysis / CCP / critical limit / reasonably likely to occur 等），纯词面无法表达「问的是法定义务还是判定方法」这一语义差别；本层只证明登记完整，准确率结论以干净 sub-agent 盲判为准。

## 结论

- 登记完整性：全部 PASS
- 词面代理结果见上表，不用于宣布路由准确率。

