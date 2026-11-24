# CAP-21 / CAP-22 路由命中 — 确定性静态核对（v4.8 / v4.9 历史补测）

- PASS | verified.yaml 共 23 张卡 | 实得 23
- PASS | verified.yaml CAP-21 capability_id 正确 | CAP-21
- PASS | CAP-21 status=active 且 also_read 非空 | status=active also_read=8
- PASS | verified.yaml CAP-22 capability_id 正确 | CAP-22
- PASS | CAP-22 status=active 且 also_read 非空 | status=active also_read=10
- PASS | destinations.json 共 23 个去向 | 实得 23
- PASS | destinations.json CAP-21 → fda-pchf-food-safety
- PASS | destinations.json CAP-22 → fda-pchf-food-safety
- PASS | capability-index.md 含唯一 CAP-21 行 | 命中 1 行
- PASS | capability-index 的 CAP-21 行指向正确卡片
- PASS | cheatsheet.md 含 CAP-21 一句话规则行 | 命中 1 行
- PASS | SKILL.md 路由表含唯一 CAP-21 主行（第 2 列） | 命中 1 行
- PASS | CAP-21 卡片在 dist-v14 与已安装目录均存在
- PASS | 两份 CAP-21 卡片内容一致
- PASS | CAP-21 卡片开头按当前口径标「十五类不可混引」
- PASS | capability-index.md 含唯一 CAP-22 行 | 命中 1 行
- PASS | capability-index 的 CAP-22 行指向正确卡片
- PASS | cheatsheet.md 含 CAP-22 一句话规则行 | 命中 1 行
- PASS | SKILL.md 路由表含唯一 CAP-22 主行（第 2 列） | 命中 1 行
- PASS | CAP-22 卡片在 dist-v14 与已安装目录均存在
- PASS | 两份 CAP-22 卡片内容一致
- PASS | CAP-22 卡片开头按当前口径标「十五类不可混引」
- PASS | dist-v14 与已安装目录逐文件 hash 一致 | files=28 diff=0

## 词面代理 top-1（弱证据，仅作诊断）

| case | 期望 | 词面 top-1 | 是否命中 |
|---|---|---|---|
| fsvp-01 | `fsvp-inspection-program` | `fsvp-inspection-program` | ✓ |
| fsvp-02 | `fsvp-inspection-program` | `inspection-sampling` | ✗ |
| fsvp-03 | `fsvp-inspection-program` | `fsvp-inspection-program` | ✓ |
| fsvp-04 | `fsvp-inspection-program` | `supply-chain-verification` | ✗ |
| fsvp-05 | `fsvp-inspection-program` | `fsvp-inspection-program` | ✓ |
| fsvp-06 | `fsvp-inspection-program` | `investigator-authority-procedure` | ✗ |
| fsvp-07 | `fsvp-inspection-program` | `supply-chain-verification` | ✗ |
| fsvp-08 | `fsvp-inspection-program` | `inspection-sampling` | ✗ |
| fsvp-09 | `fsvp-inspection-program` | `inspection-sampling` | ✗ |
| fsvp-10 | `fsvp-inspection-program` | `fsvp-inspection-program` | ✓ |
| seafood-01 | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` | ✓ |
| seafood-02 | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` | ✓ |
| seafood-03 | `seafood-haccp-statutory-requirements` | `regulatory-boundaries` | ✗ |
| seafood-04 | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` | ✓ |
| seafood-05 | `seafood-haccp-statutory-requirements` | `supply-chain-verification` | ✗ |
| seafood-06 | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` | ✓ |
| seafood-07 | `seafood-haccp-statutory-requirements` | `seafood-hazards-controls-guide` | ✗ |
| seafood-08 | `seafood-haccp-statutory-requirements` | `management-components` | ✗ |
| seafood-09 | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` | ✓ |
| seafood-10 | `seafood-haccp-statutory-requirements` | `seafood-hazards-controls-guide` | ✗ |

- 词面代理 top-1 总体：9/20
- 其中 CAP-21（fsvp-*）：4/10；CAP-22（seafood-*）：5/10
- 说明：中文口语化 prompt 与英文 keyword 表错位，且 CAP-21 / CAP-22 / CAP-23 在 hazard analysis / importer / HACCP 等词上重叠；本层只证明登记完整，准确率结论以干净 sub-agent 语义盲判为准。

## 结论

- 登记完整性：全部 PASS
- 词面代理结果见上表，不用于宣布路由准确率。

