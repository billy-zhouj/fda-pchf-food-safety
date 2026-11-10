# 输出评测机械断言判分 — fda-pchf-food-safety

## si-out-01

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/5 | ✗regex:2023|11/01/2023|11/1/202; ✗regex:更正|Correction date|09/30; ✓regex:生成日|creationDate|2025092; ✓regex:CPGM|Transmittal|2025-CP; ✓regex:IMPLEMENTATION DATE|09/3 |
| v411_skill | 5/5 | ✓regex:2023|11/01/2023|11/1/202; ✓regex:更正|Correction date|09/30; ✓regex:生成日|creationDate|2025092; ✓regex:CPGM|Transmittal|2025-CP; ✓regex:IMPLEMENTATION DATE|09/3 |

## si-out-02

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 5/5 | ✓regex:合并|combination|single; ✓regex:7303\.844; ✓regex:03844|03842; ✓regex:PAC|码表|取样|分析; ✓regex:03842H|同名不同义|两套码表|取样/分析  |
| v411_skill | 5/5 | ✓regex:合并|combination|single; ✓regex:7303\.844; ✓regex:03844|03842; ✓regex:PAC|码表|取样|分析; ✓regex:03842H|同名不同义|两套码表|取样/分析  |

## si-out-03

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v411_skill | 5/5 | ✓regex:Table\s*1|表\s*1; ✓regex:Table\s*2|表\s*2; ✓regex:work planning|工作计划|合规史|排; ✓regex:90|10|100 entry|不对调|不可对调; ✓regex:HIGHER RISK|not all incl |
| without_skill | 1/5 | ✗regex:Table\s*1|表\s*1; ✗regex:Table\s*2|表\s*2; ✓regex:work planning|工作计划|合规史|排; ✗regex:90|10|100 entry|不对调|不可对调; ✗regex:HIGHER RISK|not all incl |

## si-out-04

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/5 | ✗regex:六类|6\s*类|Processor|Impor; ✓regex:Vessels|加工船|靠港; ✓regex:NSSP|贝类|93-01; ✗regex:HACCP Program Evaluation; ✗regex:Foreign Establishment|IS |
| v411_skill | 5/5 | ✓regex:六类|6\s*类|Processor|Impor; ✓regex:Vessels|加工船|靠港; ✓regex:NSSP|贝类|93-01; ✓regex:HACCP Program Evaluation; ✓regex:Foreign Establishment|IS |

## si-out-05

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/5 | ✗regex:for cause|for-cause|因由|仅; ✓regex:ATTACHMENT A|附件 A; ✗regex:surveillance|audit|监督; ✗regex:reconditioning|DWPE|不得|不; ✓regex:702\(b\)|Domestic HACCP  |
| v411_skill | 5/5 | ✓regex:for cause|for-cause|因由|仅; ✓regex:ATTACHMENT A|附件 A; ✓regex:surveillance|audit|监督; ✓regex:reconditioning|DWPE|不得|不; ✓regex:702\(b\)|Domestic HACCP  |

## si-out-06

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/5 | ✓regex:03842; ✓regex:03842H|H\s*结尾; ✓regex:documentary|证明文件|书面; ✓regex:Workplan|workplan|不计入|同名; ✗regex:HACCP Verification|报告表|取 |
| v411_skill | 5/5 | ✓regex:03842; ✓regex:03842H|H\s*结尾; ✓regex:documentary|证明文件|书面; ✓regex:Workplan|workplan|不计入|同名; ✓regex:HACCP Verification|报告表|取 |

## si-out-07

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/5 | ✓regex:500|50|35; ✗regex:触发|追加分析|check analysis|检; ✓regex:不是.{0,12}(法规|法定|限量|放行)|不; ✗regex:540\.525|CPG|转引未收; ✗regex:PART IV|6 subs|初始|CAP-22 |
| v411_skill | 5/5 | ✓regex:500|50|35; ✓regex:触发|追加分析|check analysis|检; ✓regex:不是.{0,12}(法规|法定|限量|放行)|不; ✓regex:540\.525|CPG|转引未收; ✓regex:PART IV|6 subs|初始|CAP-22 |

## si-out-08

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/5 | ✓regex:Table\s*4|表\s*4; ✗regex:case.by.case|逐案|个案; ✓regex:123\.6|significant hazar; ✓regex:concurrence|HFP|自动|不得; ✗regex:Significance must be det |
| v411_skill | 5/5 | ✓regex:Table\s*4|表\s*4; ✓regex:case.by.case|逐案|个案; ✓regex:123\.6|significant hazar; ✓regex:concurrence|HFP|自动|不得; ✓regex:Significance must be det |

## si-out-09

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v411_skill | 5/5 | ✓regex:FSVP|7303\.878; ✓regex:123\.12|进口商; ✓regex:03844H|Surveillance|监督取样; ✓regex:两套|不得|不能|不适用|法源; ✓regex:part 1 subpart L|§805|80 |
| without_skill | 5/5 | ✓regex:FSVP|7303\.878; ✓regex:123\.12|进口商; ✓regex:03844H|Surveillance|监督取样; ✓regex:两套|不得|不能|不适用|法源; ✓regex:part 1 subpart L|§805|80 |

## si-out-10

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 5/5 | ✓regex:超出|不适用|不覆盖|不(提供|代写)|无法(提; ✓regex:GB 2733|欧盟|FDA|本包; ✓not_contains:卫生证书编号：; ✓not_contains:组胺限量为; ✓regex:out_of_scope|stop_condit |
| v411_skill | 5/5 | ✓regex:超出|不适用|不覆盖|不(提供|代写)|无法(提; ✓regex:GB 2733|欧盟|FDA|本包; ✓not_contains:卫生证书编号：; ✓not_contains:组胺限量为; ✓regex:out_of_scope|stop_condit |

## 汇总（全部断言通过的 case 比例）

- v411_skill: 10/10
- without_skill: 3/10

> 机械断言先于 LLM judge；A/B 盲评与分歧样本人工复核另行进行，此处不自动宣布非劣。
