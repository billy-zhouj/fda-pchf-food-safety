# 能力卡路由正确性评测 — fda-pchf-food-safety v4.10

- 用例数 33（23 张卡各 1 条 + CAP-23 定向 7 条 + CAP-22 定向 3 条）
- 判分记录 99 条；每个用例重复 3 次（3 个干净 sub-agent）
- top-1 命中 99/99 = **1.000**
- 重复判断一致的用例 33/33
- 非法 slug（不在候选清单）: 0

## CAP-23 专项（用户明确要求确认的项）

- CAP-23 定向/基础用例 8 条 × 3 轮 = 24 判，命中 **24/24**
- CAP-22 定向/基础用例 4 条 × 3 轮 = 12 判，命中 **12/12**
- CAP-23 题误判为 CAP-22: 0；CAP-22 题误判为 CAP-23: 0

## 逐例结果

| case | cap | expected | selected (按 run) | 命中 |
|---|---|---|---|---|
| cap22-a | CAP-22 | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` / `seafood-haccp-statutory-requirements` / `seafood-haccp-statutory-requirements` | 3/3 |
| cap22-b | CAP-22 | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` / `seafood-haccp-statutory-requirements` / `seafood-haccp-statutory-requirements` | 3/3 |
| cap22-c | CAP-22 | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` / `seafood-haccp-statutory-requirements` / `seafood-haccp-statutory-requirements` | 3/3 |
| cap23-a | CAP-23 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` | 3/3 |
| cap23-b | CAP-23 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` | 3/3 |
| cap23-c | CAP-23 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` | 3/3 |
| cap23-d | CAP-23 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` | 3/3 |
| cap23-e | CAP-23 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` | 3/3 |
| cap23-f | CAP-23 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` | 3/3 |
| cap23-g | CAP-23 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` | 3/3 |
| route-01 | CAP-01 | `hazard-analysis-method` | `hazard-analysis-method` / `hazard-analysis-method` / `hazard-analysis-method` | 3/3 |
| route-02 | CAP-02 | `management-components` | `management-components` / `management-components` / `management-components` | 3/3 |
| route-03 | CAP-03 | `process-control-validation` | `process-control-validation` / `process-control-validation` / `process-control-validation` | 3/3 |
| route-04 | CAP-04 | `environmental-pathogen-sanitation` | `environmental-pathogen-sanitation` / `environmental-pathogen-sanitation` / `environmental-pathogen-sanitation` | 3/3 |
| route-05 | CAP-05 | `allergen-program` | `allergen-program` / `allergen-program` / `allergen-program` | 3/3 |
| route-06 | CAP-06 | `chemical-hazard-controls` | `chemical-hazard-controls` / `chemical-hazard-controls` / `chemical-hazard-controls` | 3/3 |
| route-07 | CAP-07 | `supply-chain-verification` | `supply-chain-verification` / `supply-chain-verification` / `supply-chain-verification` | 3/3 |
| route-08 | CAP-08 | `recall-plan` | `recall-plan` / `recall-plan` / `recall-plan` | 3/3 |
| route-09 | CAP-09 | `regulatory-boundaries` | `regulatory-boundaries` / `regulatory-boundaries` / `regulatory-boundaries` | 3/3 |
| route-10 | CAP-10 | `reference-tools-discipline` | `reference-tools-discipline` / `reference-tools-discipline` / `reference-tools-discipline` | 3/3 |
| route-11 | CAP-11 | `exemption-withdrawal-procedure` | `exemption-withdrawal-procedure` / `exemption-withdrawal-procedure` / `exemption-withdrawal-procedure` | 3/3 |
| route-12 | CAP-12 | `environmental-engineering-controls` | `environmental-engineering-controls` / `environmental-engineering-controls` / `environmental-engineering-controls` | 3/3 |
| route-13 | CAP-13 | `personnel-hygiene-controls` | `personnel-hygiene-controls` / `personnel-hygiene-controls` / `personnel-hygiene-controls` | 3/3 |
| route-14 | CAP-14 | `cgmp-compliance-guide` | `cgmp-compliance-guide` / `cgmp-compliance-guide` / `cgmp-compliance-guide` | 3/3 |
| route-15 | CAP-15 | `defect-action-levels` | `defect-action-levels` / `defect-action-levels` / `defect-action-levels` | 3/3 |
| route-16 | CAP-16 | `inspection-readiness` | `inspection-readiness` / `inspection-readiness` / `inspection-readiness` | 3/3 |
| route-17 | CAP-17 | `inspection-sampling` | `inspection-sampling` / `inspection-sampling` / `inspection-sampling` | 3/3 |
| route-18 | CAP-18 | `investigator-authority-procedure` | `investigator-authority-procedure` / `investigator-authority-procedure` / `investigator-authority-procedure` | 3/3 |
| route-19 | CAP-19 | `lacf-inspection-program` | `lacf-inspection-program` / `lacf-inspection-program` / `lacf-inspection-program` | 3/3 |
| route-20 | CAP-20 | `lacf-statutory-requirements` | `lacf-statutory-requirements` / `lacf-statutory-requirements` / `lacf-statutory-requirements` | 3/3 |
| route-21 | CAP-21 | `fsvp-inspection-program` | `fsvp-inspection-program` / `fsvp-inspection-program` / `fsvp-inspection-program` | 3/3 |
| route-22 | CAP-22 | `seafood-haccp-statutory-requirements` | `seafood-haccp-statutory-requirements` / `seafood-haccp-statutory-requirements` / `seafood-haccp-statutory-requirements` | 3/3 |
| route-23 | CAP-23 | `seafood-hazards-controls-guide` | `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` / `seafood-hazards-controls-guide` | 3/3 |

## 每卡命中（按 capability_id 聚合）

| cap | 命中/判数 |
|---|---|
| CAP-01 | 3/3 |
| CAP-02 | 3/3 |
| CAP-03 | 3/3 |
| CAP-04 | 3/3 |
| CAP-05 | 3/3 |
| CAP-06 | 3/3 |
| CAP-07 | 3/3 |
| CAP-08 | 3/3 |
| CAP-09 | 3/3 |
| CAP-10 | 3/3 |
| CAP-11 | 3/3 |
| CAP-12 | 3/3 |
| CAP-13 | 3/3 |
| CAP-14 | 3/3 |
| CAP-15 | 3/3 |
| CAP-16 | 3/3 |
| CAP-17 | 3/3 |
| CAP-18 | 3/3 |
| CAP-19 | 3/3 |
| CAP-20 | 3/3 |
| CAP-21 | 3/3 |
| CAP-22 | 12/12 |
| CAP-23 | 24/24 |

## 混淆对（expected → selected）

无错判。

## 被误选次数（按卡）

无。

> 本评测只测「给定 23 张卡候选时的 top-1 路由」，不测技能层是否触发、也不测答案内容质量（另见 output 评测报告）。judge 看到的是能力索引，不是完整卡片正文；且 instruction 中已提示 CAP-22（法条层）与 CAP-23（指南判定链）的分工，可能高估真实口语场景准确率。
