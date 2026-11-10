# 输出评测机械断言判分 — fda-pchf-food-safety

## out-01

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/3 | ✓regex:113\.100\(g\); ✓regex:113\.100\(h\)|part\s*11; ✓regex:1\s*年 |
| v47_skill | 3/3 | ✓regex:113\.100\(g\); ✓regex:113\.100\(h\)|part\s*11; ✓regex:1\s*年 |
| v46_skill | 3/3 | ✓regex:113\.100\(g\); ✓regex:113\.100\(h\)|part\s*11; ✓regex:1\s*年 |

## out-02

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v46_skill | 3/4 | ✗regex:114\.100\(e\); ✓regex:3\s*年; ✓not_contains:§ 114.100(h); ✓not_contains:两 part 都是 1+2 年 |
| without_skill | 4/4 | ✓regex:114\.100\(e\); ✓regex:3\s*年; ✓not_contains:§ 114.100(h); ✓not_contains:两 part 都是 1+2 年 |
| v47_skill | 4/4 | ✓regex:114\.100\(e\); ✓regex:3\s*年; ✓not_contains:§ 114.100(h); ✓not_contains:两 part 都是 1+2 年 |

## out-03

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v46_skill | 3/3 | ✓regex:110\s*and\s*117; ✓regex:2018|撤回|withdraw; ✓not_contains:Part 110 已移除 |
| v47_skill | 3/3 | ✓regex:110\s*and\s*117; ✓regex:2018|撤回|withdraw; ✓not_contains:Part 110 已移除 |
| without_skill | 2/3 | ✓regex:110\s*and\s*117; ✗regex:2018|撤回|withdraw; ✓not_contains:Part 110 已移除 |

## out-04

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v46_skill | 3/3 | ✓regex:117\.1\(c\); ✓regex:117\.5\(d\); ✓regex:条件|豁免|并行 |
| v47_skill | 3/3 | ✓regex:117\.1\(c\); ✓regex:117\.5\(d\); ✓regex:条件|豁免|并行 |
| without_skill | 3/3 | ✓regex:117\.1\(c\); ✓regex:117\.5\(d\); ✓regex:条件|豁免|并行 |

## out-05

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/3 | ✓regex:113\.3; ✓regex:4\.6; ✓regex:0\.85 |
| v47_skill | 3/3 | ✓regex:113\.3; ✓regex:4\.6; ✓regex:0\.85 |
| v46_skill | 3/3 | ✓regex:113\.3; ✓regex:4\.6; ✓regex:0\.85 |

## out-06

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v47_skill | 2/2 | ✓regex:(?i)scheduled process; ✓regex:113\.|114\. |
| without_skill | 2/2 | ✓regex:(?i)scheduled process; ✓regex:113\.|114\. |
| v46_skill | 2/2 | ✓regex:(?i)scheduled process; ✓regex:113\.|114\. |

## out-07

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v46_skill | 1/3 | ✗contains:十二类; ✓regex:〔§\s*(117|113|114)\.; ✗not_contains:十类不可混引 |
| v47_skill | 3/3 | ✓contains:十二类; ✓regex:〔§\s*(117|113|114)\.; ✓not_contains:十类不可混引 |
| without_skill | 2/3 | ✗contains:十二类; ✓regex:〔§\s*(117|113|114)\.; ✓not_contains:十类不可混引 |

## out-08

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v46_skill | 2/2 | ✓contains:危害分析; ✓regex:117\.130|六列 |
| v47_skill | 2/2 | ✓contains:危害分析; ✓regex:117\.130|六列 |
| without_skill | 2/2 | ✓contains:危害分析; ✓regex:117\.130|六列 |

## out-09

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v46_skill | 2/2 | ✓contains:过敏原; ✓regex:Ed\.5|第五版|2025 |
| v47_skill | 2/2 | ✓contains:过敏原; ✓regex:Ed\.5|第五版|2025 |
| without_skill | 2/2 | ✓contains:过敏原; ✓regex:Ed\.5|第五版|2025 |

## out-10

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓contains:记录; ✓regex:FDA|检查 |
| v47_skill | 2/2 | ✓contains:记录; ✓regex:FDA|检查 |
| v46_skill | 2/2 | ✓contains:记录; ✓regex:FDA|检查 |

## 汇总（全部断言通过的 case 比例）

- v46_skill: 8/10
- v47_skill: 10/10
- without_skill: 8/10

> 机械断言先于 LLM judge；A/B 盲评与分歧样本人工复核另行进行，此处不自动宣布非劣。
