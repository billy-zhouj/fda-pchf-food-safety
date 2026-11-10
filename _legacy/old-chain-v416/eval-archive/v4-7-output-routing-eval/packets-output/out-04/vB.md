# 做 Part 113 的 scheduled process 是否就不用管 Part 117 Subparts C/G

## 结论

**不是。** Part 113 的 scheduled process 只解决「密封容器内低酸食品的商业无菌（微生物危害）」这一格；它既不能覆盖同一产品的化学/物理/金葡等危害，也不能覆盖你们那条普通即食食品（RTE）产线。正确做法是按「**对象 × 危害类别**」逐格切分，写成义务矩阵，而不是给「整厂免检 / 不免检」的二值结论。

## 条款层面

1. **并行不互斥**：〔§ 117.1(c)〕明文 `Food covered by specific current good manufacturing practice regulations also is subject to the requirements of those regulations` —— 受专项 CGMP（Part 113）管辖的食品**同时**受 Part 117 约束。「做了 part 113 就不归 Part 117 管」和「做了 PCHF 就不用管 part 113」两个方向都错。
2. **豁免是有条件的**：〔§ 117.5(d)(1)〕只免「受 part 113 管辖之活动」的 Subparts C/G，且须**同时**满足 `required to comply with, and are in compliance with, part 113` 两个并列条件。只要 Part 113 侧不合规（scheduled process 未按〔§ 113.83〕由 qualified person 确立、关键因子未写入、〔§ 113.87〕杀菌室规程未张贴或无 traffic control、〔§ 113.89〕偏差未按规定返工/评价/销毁），`in compliance with` 不成立，**整条豁免不成立**，Subparts C/G 全部回来。
3. **豁免只切一小块危害**：〔§ 117.5(d)(2)〕`The exemption in paragraph (d)(1) ... is applicable only with respect to the microbiological hazards that are regulated under part 113`。因此化学危害、物理危害，以及**未被热处理控制且需要预防控制的危害**（典型如 `Staphylococcus aureus` 在杀菌前配料/暂放阶段生长产毒——毒素耐热、热处理不可逆）仍归 Part 117 Subparts C/G。
4. **普通即食食品产线完全不在豁免内**：该线要做完整危害分析〔§ 117.130〕、书面 FSP 七部件〔§ 117.126(b)(1)–(7)〕、预防控制〔§ 117.135〕、监控〔§ 117.145〕、纠正措施〔§ 117.150〕、验证〔§ 117.155/160/165〕、再分析〔§ 117.170〕、实施记录〔§ 117.190(a)〕与召回计划〔§ 117.139〕。若 RTE 食品包装前暴露于环境且包装后无致死处理，还**强制**评估环境病原〔§ 117.130(c)(1)(ii)〕（李斯特菌/沙门氏菌）。
5. **别引错条款**：〔§ 117.201〕是 qualified facility 的 modified requirements，**不是** LACF 条款；〔§ 117.5〕的豁免清单是 part 123（(b)）、part 120（(c)）、part 113（(d)），**不含 part 114**——若你们还做酸化食品，酸化食品全程受 Subparts C/G 约束，且〔§ 114.5〕反向把 `parts 110 and 117` 拉进掺假判定。

## 落地矩阵（按危害逐行，不按整厂）

| 危害类别 | LACF 线 | 普通 RTE 线 | 依据 |
|---|---|---|---|
| 肉毒梭菌等密封容器微生物 | Part 113（scheduled process、§113.83/§113.87/§113.89） | 不适用 | §117.5(d)(1)(2) |
| 金葡产毒、化学（过敏原、农残、真菌毒素）、物理危害 | **仍须 Subparts C/G 危害分析与预防控制** | 须全套 Subparts C/G | §117.5(d)(2)、§117.130、§117.135 |
| 包装后环境再污染（李斯特菌/沙门氏菌） | 评估是否适用 | 强制评估 + 卫生/环境控制 | §117.130(c)(1)(ii)、§117.135(c)(3) |
| CGMP 底层（Subpart B）与记录（Subpart F） | 均适用，豁免只切 C/G | 均适用 | §117.1(c)、§117.5(a) |

## 执行动作

- 两条产线**分别**建 FSP；LACF 线在危害分析工作表里，对「part 113 管辖的微生物危害」写明依据 §117.5(d)(1)(2) 的豁免理由，其余每一类危害照常判 Yes/No 并给书面理由（判 No 也要书面，§117.130(a)）。
- 建立 Part 113 合规自检清单（scheduled process 与关键因子、杀菌室规程、偏差档案、记录 §113.100(g)(h)），作为豁免成立的前提证据，检查时可向 FDA 出示。
- 不要写成「本厂免 PCHF」或「本厂全免 Subparts C/G」——监管口径是按危害切分的义务并集，不是全有全无。
