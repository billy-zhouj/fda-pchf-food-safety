# 能力卡路由正确性评测 — fda-pchf-food-safety v4.7

- 用例数 20（覆盖 20 张能力卡，每卡 1 条）
- 判分记录 40 条；每个用例重复 2 次（不同干净 sub-agent）
- top-1 命中 40/40 = **1.000**
- 重复判断一致的用例 20/20
- 非法 slug（不在候选清单）: 0

## 逐例结果

| case | expected | selected (按 run) | 命中 |
|---|---|---|---|
| route-01 | `hazard-analysis-method` | `hazard-analysis-method` / `hazard-analysis-method` | 2/2 |
| route-02 | `management-components` | `management-components` / `management-components` | 2/2 |
| route-03 | `process-control-validation` | `process-control-validation` / `process-control-validation` | 2/2 |
| route-04 | `environmental-pathogen-sanitation` | `environmental-pathogen-sanitation` / `environmental-pathogen-sanitation` | 2/2 |
| route-05 | `allergen-program` | `allergen-program` / `allergen-program` | 2/2 |
| route-06 | `chemical-hazard-controls` | `chemical-hazard-controls` / `chemical-hazard-controls` | 2/2 |
| route-07 | `supply-chain-verification` | `supply-chain-verification` / `supply-chain-verification` | 2/2 |
| route-08 | `recall-plan` | `recall-plan` / `recall-plan` | 2/2 |
| route-09 | `regulatory-boundaries` | `regulatory-boundaries` / `regulatory-boundaries` | 2/2 |
| route-10 | `reference-tools-discipline` | `reference-tools-discipline` / `reference-tools-discipline` | 2/2 |
| route-11 | `exemption-withdrawal-procedure` | `exemption-withdrawal-procedure` / `exemption-withdrawal-procedure` | 2/2 |
| route-12 | `environmental-engineering-controls` | `environmental-engineering-controls` / `environmental-engineering-controls` | 2/2 |
| route-13 | `personnel-hygiene-controls` | `personnel-hygiene-controls` / `personnel-hygiene-controls` | 2/2 |
| route-14 | `cgmp-compliance-guide` | `cgmp-compliance-guide` / `cgmp-compliance-guide` | 2/2 |
| route-15 | `defect-action-levels` | `defect-action-levels` / `defect-action-levels` | 2/2 |
| route-16 | `inspection-readiness` | `inspection-readiness` / `inspection-readiness` | 2/2 |
| route-17 | `inspection-sampling` | `inspection-sampling` / `inspection-sampling` | 2/2 |
| route-18 | `investigator-authority-procedure` | `investigator-authority-procedure` / `investigator-authority-procedure` | 2/2 |
| route-19 | `lacf-inspection-program` | `lacf-inspection-program` / `lacf-inspection-program` | 2/2 |
| route-20 | `lacf-statutory-requirements` | `lacf-statutory-requirements` / `lacf-statutory-requirements` | 2/2 |

## 混淆对（expected → selected）

无错判。

## 被误选次数（按卡）

无。

> 本评测只测「给定 20 张卡候选时的 top-1 路由」，不测技能层是否触发，也不测答案内容质量（另见 output 评测报告）。judge 看到的是浓缩能力索引，不是完整卡片正文。
