# 输出评测机械断言判分 — fda-pchf-food-safety

## fsvp-out-01

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/5 | ✓regex:deemed|视为符合|视为已符合; ✗regex:1\.509|section 1\.509; ✓regex:DUNS|UFI|entry line|每一条|; ✓regex:Part 117|part 117|117\.1; ✓regex:805|subpart L|两套|不同.{0,8 |
| v410_skill | 5/5 | ✓regex:deemed|视为符合|视为已符合; ✓regex:1\.509|section 1\.509; ✓regex:DUNS|UFI|entry line|每一条|; ✓regex:Part 117|part 117|117\.1; ✓regex:805|subpart L|两套|不同.{0,8 |

## fsvp-out-02

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/4 | ✗regex:不取样|不(会|应|能).{0,6}取(样|集); ✓regex:7303\.050|subs|环境拭子|Zone; ✓regex:危害分析|供应商(批准|评价)|验证活动|纠正措; ✓regex:on-site|remote|现场|远程|EIR |
| v410_skill | 4/4 | ✓regex:不取样|不(会|应|能).{0,6}取(样|集); ✓regex:7303\.050|subs|环境拭子|Zone; ✓regex:危害分析|供应商(批准|评价)|验证活动|纠正措; ✓regex:on-site|remote|现场|远程|EIR |

## fsvp-out-03

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v410_skill | 4/4 | ✓regex:entry line|每一条|每一(次)?(报关; ✓regex:DUNS|UFI; ✓regex:1\.509|CBP|电子|electronic; ✓regex:deemed|例外|不免|不能免|仍(然|须|要 |
| without_skill | 4/4 | ✓regex:entry line|每一条|每一(次)?(报关; ✓regex:DUNS|UFI; ✓regex:1\.509|CBP|电子|electronic; ✓regex:deemed|例外|不免|不能免|仍(然|须|要 |

## fsvp-out-04

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/4 | ✓regex:1\.501|八类|豁免; ✓regex:part 120|120|果汁|水产|part ; ✓regex:转运|过境|酒精|研究|个人消费|USDA|复出; ✗regex:十[四五]类|不可混引|转引未收|1\.509| |
| v410_skill | 4/4 | ✓regex:1\.501|八类|豁免; ✓regex:part 120|120|果汁|水产|part ; ✓regex:转运|过境|酒精|研究|个人消费|USDA|复出; ✓regex:十[四五]类|不可混引|转引未收|1\.509| |

## fsvp-out-05

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/4 | ✓regex:standard|标准.{0,4}要求; ✓regex:modified|1\.507|1\.511|1; ✓regex:可以(选择|选)|may choose|可选|不; ✓regex:EIR|独立|No FSVP|资格证明|PART |
| v410_skill | 4/4 | ✓regex:standard|标准.{0,4}要求; ✓regex:modified|1\.507|1\.511|1; ✓regex:可以(选择|选)|may choose|可选|不; ✓regex:EIR|独立|No FSVP|资格证明|PART |

## fsvp-out-06

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/4 | ✓regex:PART V|483a|观察|重大; ✓regex:危害分析|供应商(批准|评价)|验证活动|书面索; ✓regex:Warning Letter|警告信|99-41; ✓regex:direct reference|有限情形|CM |
| v410_skill | 4/4 | ✓regex:PART V|483a|观察|重大; ✓regex:危害分析|供应商(批准|评价)|验证活动|书面索; ✓regex:Warning Letter|警告信|99-41; ✓regex:direct reference|有限情形|CM |

## fsvp-out-07

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/4 | ✓regex:首次|initial|Initial; ✓regex:不默认|不(一定|必然)|only when|仅; ✓regex:voluntary|自愿|纠正|complian; ✗regex:十[四五]类|不创设|作业指导|不得|不是必然| |
| v410_skill | 4/4 | ✓regex:首次|initial|Initial; ✓regex:不默认|不(一定|必然)|only when|仅; ✓regex:voluntary|自愿|纠正|complian; ✓regex:十[四五]类|不创设|作业指导|不得|不是必然| |

## fsvp-out-08

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/4 | ✓regex:99-41|Red List; ✓regex:具体食品|食品.{0,8}供应商|组合|或全部食; ✓regex:未(被)?列(入|名)|不在|may conti; ✓regex:移除|removal|Division|CMS| |
| v410_skill | 4/4 | ✓regex:99-41|Red List; ✓regex:具体食品|食品.{0,8}供应商|组合|或全部食; ✓regex:未(被)?列(入|名)|不在|may conti; ✓regex:移除|removal|Division|CMS| |

## fsvp-out-09

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v410_skill | 4/4 | ✓regex:99-37|99-38; ✓regex:7303\.070|LACF|低酸|酸化|sch; ✓regex:不得仅因|不能仅|未注册|未备案|DWPE|FU; ✓regex:801\(a\)\(3\)|法律 hook|触发 |
| without_skill | 4/4 | ✓regex:99-37|99-38; ✓regex:7303\.070|LACF|低酸|酸化|sch; ✓regex:不得仅因|不能仅|未注册|未备案|DWPE|FU; ✓regex:801\(a\)\(3\)|法律 hook|触发 |

## fsvp-out-10

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/4 | ✗regex:不是.{0,10}(新规|新程序|新 ?prog; ✓regex:Corrections|更正|POC|机构名称|; ✗regex:转引未收|未收|不得(从|反推); ✓regex:1\.505|Import Alert 99-4 |
| v410_skill | 4/4 | ✓regex:不是.{0,10}(新规|新程序|新 ?prog; ✓regex:Corrections|更正|POC|机构名称|; ✓regex:转引未收|未收|不得(从|反推); ✓regex:1\.505|Import Alert 99-4 |

## sf-out-01

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/4 | ✓regex:123\.16; ✓regex:part 113|part 114|113|11; ✓regex:只(是|排|排除|限于)|例外|不(是|代表|等; ✓regex:HACCP 计划|危害分析|货架期|123\.6 |
| v410_skill | 4/4 | ✓regex:123\.16; ✓regex:part 113|part 114|113|11; ✓regex:只(是|排|排除|限于)|例外|不(是|代表|等; ✓regex:HACCP 计划|危害分析|货架期|123\.6 |

## sf-out-02

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/4 | ✓regex:123\.5\(a\)|默认|Except as; ✓regex:117\.5\(b\)|两个|双条件|requi; ✓regex:Subparts? C|Subpart G|C/; ✓regex:activities|活动|按活动|不是整厂|受 |
| v410_skill | 4/4 | ✓regex:123\.5\(a\)|默认|Except as; ✓regex:117\.5\(b\)|两个|双条件|requi; ✓regex:Subparts? C|Subpart G|C/; ✓regex:activities|活动|按活动|不是整厂|受 |

## sf-out-03

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/4 | ✓regex:117\.5\(b\); ✓regex:117\.5\(d\)\(2\)|part 11; ✓regex:没有.{0,10}(限缩|对应)|不限缩|无限缩; ✓regex:两个方向|两头都错|高估|低估|不是整厂|不能. |
| v410_skill | 4/4 | ✓regex:117\.5\(b\); ✓regex:117\.5\(d\)\(2\)|part 11; ✓regex:没有.{0,10}(限缩|对应)|不限缩|无限缩; ✓regex:两个方向|两头都错|高估|低估|不是整厂|不能. |

## sf-out-04

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/4 | ✓regex:123\.9; ✓regex:冷藏|refrigerated; ✓regex:1\s*年|一年; ✓regex:2\s*年|两年|冷冻|保藏|货架稳定|Part |
| v410_skill | 4/4 | ✓regex:123\.9; ✓regex:冷藏|refrigerated; ✓regex:1\s*年|一年; ✓regex:2\s*年|两年|冷冻|保藏|货架稳定|Part |

## sf-out-05

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/4 | ✓regex:123\.12; ✓regex:FSVP|805|subpart L|part ; ✓regex:两套|双轨|互不替代|不(等于|自动)|不能.{; ✓regex:deemed|1\.509|拒绝入境|123\. |
| v410_skill | 4/4 | ✓regex:123\.12; ✓regex:FSVP|805|subpart L|part ; ✓regex:两套|双轨|互不替代|不(等于|自动)|不能.{; ✓regex:deemed|1\.509|拒绝入境|123\. |

## sf-out-06

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 4/4 | ✓regex:123\.28|shellstock|tag|标; ✓regex:五(项|个|要素)|采捕|harvester|d; ✓regex:123\.9\(e\)|不受|除非|例外|保存|; ✓regex:1240\.60|NSSP|转引未收|未收|不得 |
| v410_skill | 4/4 | ✓regex:123\.28|shellstock|tag|标; ✓regex:五(项|个|要素)|采捕|harvester|d; ✓regex:123\.9\(e\)|不受|除非|例外|保存|; ✓regex:1240\.60|NSSP|转引未收|未收|不得 |

## sf-out-07

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v410_skill | 4/4 | ✓regex:123\.8; ✓regex:1\s*周|一周|7\s*天|within 1 ; ✓regex:每年|至少每年|annual|至少.{0,4}一; ✓regex:监控记录|CCP|纠正措施记录|123\.8\( |
| without_skill | 3/4 | ✗regex:123\.8; ✓regex:1\s*周|一周|7\s*天|within 1 ; ✓regex:每年|至少每年|annual|至少.{0,4}一; ✓regex:监控记录|CCP|纠正措施记录|123\.8\( |

## sf-out-08

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/4 | ✗regex:123\.7; ✓regex:隔离|扣留|segregate|hold|不得放; ✓regex:关键限值|偏离|critical limit|d; ✓regex:商业|commerce|不合格品|不得使|123 |
| v410_skill | 4/4 | ✓regex:123\.7; ✓regex:隔离|扣留|segregate|hold|不得放; ✓regex:关键限值|偏离|critical limit|d; ✓regex:商业|commerce|不合格品|不得使|123 |

## sf-out-09

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v410_skill | 4/4 | ✓regex:123\.11; ✓regex:should; ✓regex:shall; ✓regex:不(得|能).{0,10}(升格|当成|说成)| |
| without_skill | 3/4 | ✗regex:123\.11; ✓regex:should; ✓regex:shall; ✓regex:不(得|能).{0,10}(升格|当成|说成)| |

## sf-out-10

| 变体 | 断言通过 | 明细 |
|---|---|---|
| v410_skill | 4/4 | ✓regex:123\.16; ✓regex:part 113|113|LACF|低酸罐头|密; ✓regex:只(排|排除|是)|例外|Subpart A|仍; ✓regex:两套|分(两套|开)|分别|分流|CAP-20| |
| without_skill | 3/4 | ✗regex:123\.16; ✓regex:part 113|113|LACF|低酸罐头|密; ✓regex:只(排|排除|是)|例外|Subpart A|仍; ✓regex:两套|分(两套|开)|分别|分流|CAP-20| |

## 汇总（全部断言通过的 case 比例）

- v410_skill: 20/20
- without_skill: 11/20

> 机械断言先于 LLM judge；A/B 盲评与分歧样本人工复核另行进行，此处不自动宣布非劣。
