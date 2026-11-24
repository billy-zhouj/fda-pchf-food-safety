# 输出评测机械断言判分 — fda-pchf-food-safety

## sh-out-01

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/4 | ✓regex:Table 3-2|三表|三张表; ✓regex:潜在危害|potential hazard|只列; ✓regex:无控制|absence of controls|; ✓regex:第\s*4\s*栏|Column 4|理由 |
| v410_skill | 4/4 | ✓regex:Table 3-2|三表|三张表; ✓regex:潜在危害|potential hazard|只列; ✓regex:无控制|absence of controls|; ✓regex:第\s*4\s*栏|Column 4|理由 |

## sh-out-02

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/4 | ✓regex:无控制|absence of controls; ✓regex:组胺|scombrotoxin|histamin; ✗regex:第\s*4\s*栏|Column 4|书面理由; ✗regex:转引未收|540\.525|CPG |
| v410_skill | 3/4 | ✓regex:无控制|absence of controls; ✓regex:组胺|scombrotoxin|histamin; ✗regex:第\s*4\s*栏|Column 4|书面理由; ✓regex:转引未收|540\.525|CPG |

## sh-out-03

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v410_skill | 4/4 | ✓regex:Step\s*11|STEP\s*11|判定树|; ✓regex:123\.6\(c\)\(2\)|至少一个|at; ✓regex:Appendix 3|残表|塌陷|逐字; ✓regex:控制策略|control strategy|漂移 |
| without_skill | 2/4 | ✓regex:Step\s*11|STEP\s*11|判定树|; ✗regex:123\.6\(c\)\(2\)|至少一个|at; ✗regex:Appendix 3|残表|塌陷|逐字; ✓regex:控制策略|control strategy|漂移 |

## sh-out-04

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/4 | ✓regex:第\s*4\s*栏|Column 4; ✓regex:跳过|Steps?\s*1[128]|剪枝; ✗regex:十栏|HACCP Plan Form|映射; ✗regex:十五类不可混引|123\.6|不得(把|将) |
| v410_skill | 3/4 | ✓regex:第\s*4\s*栏|Column 4; ✓regex:跳过|Steps?\s*1[128]|剪枝; ✗regex:十栏|HACCP Plan Form|映射; ✓regex:十五类不可混引|123\.6|不得(把|将) |

## sh-out-05

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/4 | ✓regex:Table 3-2|Table 3-3|三表; ✓regex:Table 3-4; ✓regex:Step\s*10|STEP\s*10|第\s*; ✓regex:What|How|Frequency|Who|监 |
| v410_skill | 3/4 | ✓regex:Table 3-2|Table 3-3|三表; ✗regex:Table 3-4; ✓regex:Step\s*10|STEP\s*10|第\s*; ✓regex:What|How|Frequency|Who|监 |

## sh-out-06

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/4 | ✓regex:非约束性|legally enforceable; ✗regex:540\.525|NSSP|40 CFR 180; ✓regex:-20|-35|7\s*天|6\s*英寸|盐渍|; ✓regex:CAP-22|123\.|科学|scientif |
| v410_skill | 4/4 | ✓regex:非约束性|legally enforceable; ✓regex:540\.525|NSSP|40 CFR 180; ✓regex:-20|-35|7\s*天|6\s*英寸|盐渍|; ✓regex:CAP-22|123\.|科学|scientif |

## sh-out-07

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/4 | ✓regex:control strategy|Control; ✓regex:CCP|Step\s*11|第\s*5\s*栏|; ✗regex:四段式|Understand|Determine; ✓regex:科学|scientifically|充分性 |
| v410_skill | 3/4 | ✓regex:control strategy|Control; ✓regex:CCP|Step\s*11|第\s*5\s*栏|; ✗regex:四段式|Understand|Determine; ✓regex:科学|scientifically|充分性 |

## sh-out-08

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/4 | ✗regex:123\.6; ✓regex:shall|法定义务|法条层; ✓regex:非约束性|should|legally enfo; ✗regex:十五类不可混引|CAP-22|反向误读 |
| v410_skill | 4/4 | ✓regex:123\.6; ✓regex:shall|法定义务|法条层; ✓regex:非约束性|should|legally enfo; ✓regex:十五类不可混引|CAP-22|反向误读 |

## sh-out-09

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v410_skill | 4/4 | ✓regex:June 2021|2021|滚动修订|分章; ✓regex:转引未收; ✓regex:Appendix 3|残表|塌陷|逐字|不得; ✓regex:June 2022|第\s*4\s*版|4th |
| without_skill | 3/4 | ✓regex:June 2021|2021|滚动修订|分章; ✗regex:转引未收; ✓regex:Appendix 3|残表|塌陷|逐字|不得; ✓regex:June 2022|第\s*4\s*版|4th |

## sh-out-10

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/4 | ✗regex:超出|不适用|不覆盖|不(提供|代写)|无法(提; ✓regex:GB 2733|欧盟|FDA|本包; ✓not_contains:卫生证书编号：; ✓not_contains:组胺限量为 |
| v410_skill | 4/4 | ✓regex:超出|不适用|不覆盖|不(提供|代写)|无法(提; ✓regex:GB 2733|欧盟|FDA|本包; ✓not_contains:卫生证书编号：; ✓not_contains:组胺限量为 |

## 汇总（全部断言通过的 case 比例）

- v410_skill: 6/10
- without_skill: 2/10

> 机械断言先于 LLM judge；A/B 盲评与分歧样本人工复核另行进行，此处不自动宣布非劣。
