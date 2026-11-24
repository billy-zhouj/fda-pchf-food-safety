#!/usr/bin/env python3
"""v4.18 incremental upgrade of the installed fda-pchf-food-safety skill.

Adds the 22nd source (21 CFR Part 101, eCFR 2026-11-05) as CAP-30:
  * 1 router entry card + 5 RIA++ sub-cards (written separately)
  * SKILL.md / capability-index / cheatsheet / glossary / overview / test-prompts
  * audit artifacts: GLOSSARY.md, DIGEST.md, rejected/, verify report

Every single-shot replacement is guarded by assert count == 1.
Run with --apply to write; default is a dry run that prints all checks.
"""
from __future__ import annotations

import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path(r"C:\Users\HG\.workbuddy\skills\fda-pchf-food-safety")
APPLY = "--apply" in sys.argv

NEW_DESC_LINE = (
    "  另覆盖 21 CFR Part 101 食品标签法规正文（eCFR 2026-11-05 现行快照，v4.18 新增 CAP-30 "
    "`food-labeling-requirements`）：PDP 主展示面与信息面板的法定面积与方位、配料表按重量降序与通用名、"
    "显著性字号与 misbranding 定性；§101.9 营养标签普遍义务与 (j) 豁免、§101.12 RACC 份量基准、"
    "§101.11 连锁菜单与 §101.36 Supplement Facts；§101.13/14 声称三层闸门（express/implied、SSA、"
    "disqualifying level）与 Subpart D/E/F 逐词授权、gluten-free 20 ppm；§101.17 各款强制警示"
    "（含未巴氏果汁 (g) 与 Part 120〔§ 120.24〕5-log 的三层接口）、§101.30 果汁百分比声明、§101.8 自动售货机；"
    "§101.100/101.108/101.9(j) 与 Part 117 主体豁免的四套对象切分、七套法规编号与二十二类不可混引。"
    "不处理过敏原厂内交叉接触控制与 Big 9 / Contains / advisory 声明（转 CAP-05 + Ed.5 guidance 层）、"
    "果汁 5-log 工艺设计与 HACCP 计划（转 CAP-26）、检查员取证与 PAC（转 CAP-27/17/28）、"
    "Part 117 qualified facility 主体豁免（转 CAP-09）。\n"
)

CORE_57 = (
    "57. **v4.18 新增第七套法规编号〔§ 101.xxx〕**：21 CFR Part 101 是**法规正文层**（具法律约束力），"
    "与〔§ 108/113/114/117/120/123.xxx〕并列共**七套独立编号**，合计**二十二类不可混引**。"
    "Part 101 管标签**内容**，Part 117〔§ 117.135(c)(2)〕管标签**控制**——两套法源互不减免；"
    "**标签合规 ≠ 食品安全合规**（403 misbranding 错标 / 402 adulteration 掺假是两条独立执法钩子，"
    "一张合规的 Nutrition Facts 不能替代危害分析与预防控制）。四套豁免对象不可互替："
    "〔§ 101.100〕免配料表 403(i)(2)、〔§ 101.9(j)〕免营养标签、〔§ 101.108〕是 FDA 书面提案获批的临时标签实验、"
    "Part 117〔§ 117.5〕是主体/活动豁免。〔§ 101.17(g)〕未巴氏果汁警示不替代〔§ 120.24〕5-log，"
    "做了 5-log 也不自动免 §101.30 等其他标签义务；§101.12 RACC 表（约 113 页）与 Appendix B/C/D "
    "图形为不可逐字引用区，数值须回原表核对\n"
)

ROUTE_ROW = (
    "| 判定 21 CFR Part 101 食品标签法定义务：PDP/信息面板/配料表/显著性/misbranding；"
    "要不要 Nutrition Facts 与 §101.9(j) 豁免、serving size 与 §101.12 RACC；"
    "某句话是不是 claim（含暗示/品牌名/符号）、SSA 与 disqualifying level、Subpart D/E/F 逐词授权、"
    "gluten-free 20 ppm；§101.17 各款警示（含未巴氏果汁 (g)）、§101.30 果汁百分比声明、§101.8 自动售货机；"
    "§101.100 / §101.108 / §101.9(j) 四套豁免对象切分、七套编号与二十二类不可混引；"
    "Part 101 标签内容义务与 Part 117〔§ 117.135(c)(2)〕标签控制的分工 | "
    "references/capabilities/food-labeling-requirements.md | "
    "references/capabilities/labeling/*.md（5 张子卡，按入口卡路由表加载 1 张）、"
    "references/capabilities/allergen-program.md、references/capabilities/juice-haccp.md、"
    "references/capabilities/juice-inspection-program.md、references/capabilities/regulatory-boundaries.md、"
    "references/capabilities/cgmp-compliance-guide.md |\n"
)

BOUNDARY_LINE = (
    "- **21 CFR Part 101 法规正文自 v4.18 起已收**（第二十二来源，CAP-30 `food-labeling-requirements`）："
    "引用写〔§ 101.xxx〕[pdf-page N]，**不得写成〔§ 117.xxx〕，也不得与 Ed.5 guidance 的 Big 9 / "
    "advisory 声明规则互引**。它是法规正文层（具法律约束力），与 Part 117〔§ 117.135(c)(2)〕的"
    "「标签控制」这一预防控制分工：前者管标签内容该是什么，后者管如何确保标签内容与用法正确；两套互不减免。"
    "⚠ **标签合规 ≠ 食品安全合规**：403 misbranding 与 402 adulteration 是两条独立执法钩子，"
    "不得以一张合规 Nutrition Facts 替代危害分析与预防控制。四套豁免对象不可互替"
    "（§101.100 配料表 / §101.9(j) 营养标签 / §101.108 临时实验 / §117.5 主体豁免）；"
    "〔§ 101.17(g)〕未巴氏果汁警示不替代〔§ 120.24〕5-log，反向亦不成立。"
    "eCFR 2026-11-05 是快照且自述 authoritative but unofficial，RACC / DV / 阈值须复核 FR citation；"
    "§101.12 Table 1/2、Appendix B/C/D 图形与 9 个纯图形页为不可逐字引用区；"
    "FD&C Act 全文、21 CFR part 102 / 130 / 105.66、§104.20、1 CFR part 51 并入材料、AOAC 方法等一律标「转引未收」。"
    "先读入口卡再按意图加载 1 张子卡；V05 是横切口径层，不单独抢路由。\n"
)

INDEX_ROW = (
    "| CAP-30 | 21 CFR Part 101 食品标签法定义务与判定链 | core | "
    "判定 PDP/信息面板/配料表/显著性/misbranding；要不要 Nutrition Facts 与 §101.9(j) 豁免、serving size 与 §101.12 RACC；"
    "某句话是不是 claim（含暗示/品牌名/符号）、SSA 与 disqualifying level、Subpart D/E/F 逐词授权、gluten-free 20 ppm；"
    "§101.17 各款警示（含未巴氏果汁 (g)）、§101.30 果汁百分比声明、§101.8 自动售货机；"
    "§101.100/101.108/101.9(j) 四套豁免对象切分、七套编号与二十二类不可混引；"
    "Part 101 标签内容义务与 Part 117 标签控制的分工 | "
    "21 CFR Part 101、食品标签、PDP、principal display panel、information panel、配料表、§ 101.4、§ 101.9、"
    "Nutrition Facts、serving size、RACC、§ 101.12、nutrient content claim、health claim、SSA、disqualifying level、"
    "gluten-free、20 ppm、§ 101.17、未巴氏果汁警示、§ 101.30、百分比果汁声明、§ 101.100、incidental additives、"
    "亚硫酸盐 10 ppm、§ 101.108、标签豁免、misbranding、403、adulteration、402、七套编号、二十二类不可混引 | "
    "capabilities/food-labeling-requirements.md（+ labeling/ 下 5 张子卡） |\n"
)

CHEAT_ROW = (
    "| 21 CFR Part 101 食品标签法定义务与判定链 | "
    "先分层再引用：〔§ 101.xxx〕是**第七套法规编号**；Part 101 管标签内容、Part 117〔§ 117.135(c)(2)〕管标签控制，"
    "两套互不减免，**标签合规 ≠ 食品安全合规**（403 错标 / 402 掺假两条钩子）。"
    "四套豁免对象不可互替（§101.100 配料表 / §101.9(j) 营养标签 / §101.108 临时实验 / §117.5 主体豁免）；"
    "serving size 由 §101.12 RACC 推导且是所有声称阈值共同分母；暗示、品牌名、heart 符号都算 claim，"
    "健康声称须 SSA + 不超 disqualifying level；gluten-free 是 <20 ppm 定量定义；"
    "〔§ 101.17(g)〕未巴氏果汁警示不替代〔§ 120.24〕5-log、反向亦不成立；"
    "§101.12 表值与 Appendix 图形不可逐字引用。 |\n"
)

OVERVIEW_SECTION = """

## v4.18 追加：第二十二来源 21 CFR Part 101（食品标签法规正文）

> 本节是 v4.18 增量记录；上文各节的 v4.x 规模、「二十一类不可混引」与各版「仍未收」均为**历史口径**，保留不改。

- **v4.18 规模**：**30 张主卡 + 10 张 imports 子卡 + 5 张 labeling 子卡 / 277 条术语（YAML 块 t01–t277）/ 191 条测试用例 / 二十二类来源 / 七套法规编号**。
- **第二十二来源**：**21 CFR Part 101《Food Labeling》**（eCFR 导出 PDF，Prince 16.2，352 页 / 70 书签 / 50 条款 / 7 Subpart / 4 Appendix，页脚 `up to date as of 11/05/2026`，自述 `authoritative but unofficial`），`books/cfr-part101-2026/source-cfr-part101-2026.md`。属**法规正文层**，为全包**第七套独立编号**〔§ 101.xxx〕。⚠ `2026-11-05` 是 eCFR 现行快照日期，**不是修订生效日、不是新规发布日**；条文末尾 FR citation 才是修订出处。与 4-1-25 Edition 年度编纂版不同，不得混称。
- **新增 CAP-30 `food-labeling-requirements`**（来源路由入口）+ `references/capabilities/labeling/` 下 **5 张 RIA++ 子卡**：V01 标签载体与强制信息架构、V02 营养标签与份量基准体系、V03 声称三层闸门与逐词授权、V04 特定品类与强制警示声明、V05 标签豁免体系与效力层元规则（横切层，不单独抢路由）。输入按 cangjie-skill RIA-TV++ 蒸馏：5 个 extractor 并行得 182 个方法类候选 + 44 条术语 → 去重合并 5 单元 → 三重验证 5/5 通过 → 晋级门全部判 router → 93 个英文引用块逐字核验 **93/93 PASS**。
- **补齐的是「标签内容」的法条层空白**：既有包对标签的表述全在 **guidance / Part 117 层**——过敏原 Ed.5（FD&C Act §201(qq)/§403(w)）、〔§ 117.135(c)(2)〕标签控制、CAP-29 的 misbranding 扣留作业。此前从未收录 Part 101 正文。两者分工为「厂内控制怎么管 ↔ 标签内容是什么」，条款号不得互引替代。
- **六类实质纠偏**：① **四套豁免对象不可互替**——〔§ 101.100〕免的是 FD&C Act **403(i)(2) 配料表**要求，营养标签豁免在〔§ 101.9(j)〕，〔§ 101.108〕是 FDA 书面提案获批的临时实验，Part 117〔§ 117.5〕是**主体/活动**豁免；② **标签合规 ≠ 食品安全合规**——403 misbranding 与 402 adulteration 是两条独立执法钩子；③ **暗示也算 claim**——§101.13(b)(2) / §101.14(a)(1) 明列品牌名、heart 符号、vignette、第三方引用；健康声称须 SSA 且不超 disqualifying level；④ **〔§ 101.17(g)〕未巴氏果汁警示 ↔ 〔§ 120.24〕5-log ↔ CP 7303.847 是三层接口**，双向互推都会造成实质病原控制漏洞；⑤ **serving size 由 §101.12 RACC 推导**，是监管比较基准而非厂商建议食用量，也是所有声称阈值的共同分母；⑥ **20 ppm（gluten-free，§101.91）与 10 ppm（亚硫酸盐可检出，§101.100(a)(4)）是不同条款不同判据**，不可混算。
- **二十二类不可混引（v4.18 口径）**：在二十一类之外增加 **21 CFR Part 101 法规正文**。层次仍为：法规正文（**七套编号**〔§ 101 / 108 / 113 / 114 / 117 / 120 / 123.xxx〕）＞ FDA 指南（should 建议层）＞ CPGM／CP／IOM 检查程序（检查员视角、不创设企业义务）。
- **转换与自检**：`.cangjie/convert_part101.py` 按 block 坐标 (y0,x0) 重排，修 Prince 浮动标题错位（默认 `get_text()` 会把 §101.2 标题提前到 §101.1 的 (a)(b)(c) 之前）；书签全标题合并 7 处跨行标题；Subpart F 续行与 Appendix A [Reserved] 补回；清 1,747 行页眉页脚、0 残留；**50/50 条款命中**、7 Subpart、4 Appendix。**9 个纯图形页**（44/45/51/239/240/344/347/348/351）在文本层无字，系 Nutrition Facts 图形示例，已标注不可引。
- **不可逐字引用区**：§101.12 Table 1 / Table 2（约 113 页流式列值、表头脚注逐页重复、列可能错列）、Appendix B 图形增强 / C 生鲜果蔬 / D 熟鱼 Nutrition Facts 图形、§101.9 sample label 图形页。只可引「产品类别 → RACC → label statement」对应关系，数值与版式回原表核对。
- **仍未收**：FD&C Act 全文、FALCPA 法定过敏原定义本体（§201(qq)/§403(w)）、21 CFR part 1 subpart L / 102 / 130 / 105.66 / 110、§104.20 强化政策、1 CFR part 51 并入材料、AOAC / 检测方法正文、请愿表格栏目、营养数据库与消费调查原始文献、IOM Chapter 2/3/7/8/9/10、CPG 全套、Import Alert 全文、BAM 方法全文。涉及这些法源一律标「转引未收」。
- **审计轨迹**：`E:/WeChatData/2026-11-09-15-05-22/books/cfr-part101-2026/`（BOOK_OVERVIEW / PIPELINE_STATE / verified / rejected / candidates / verified.yaml / destinations.json / GLOSSARY / DIGEST / cards / test-results / backups）。
"""

GLOSSARY_TAIL = """

## v4.18 — 21 CFR Part 101 术语增量（t234–t277，44 条）

> 全部回 `source-cfr-part101-2026.md` 原文逐字核验；`clause` 统一为〔§ 101.xxx〕，属**法规正文层**，与 Part 117 预防控制层、Ed.5 guidance 层不同源。

| 术语 | 条款 | 浓缩释义 | 常见误读 |
|---|---|---|---|
| principal display panel (PDP) | 〔§ 101.1〕 | 最可能在零售陈列条件下被展示的标签部分；面积按矩形高×宽 / 圆柱 40% 高×周长 / 其他形状 40% 总表面 | 当成可自由指定的「正面」；圆柱强制信息必须落在那 40% 内 |
| information panel | 〔§ 101.2〕 | 紧邻 PDP 右侧的法定相对方位（有例外） | 以为任意空白面都能放营养标签与配料表 |
| serving / serving size | 〔§ 101.9(b)〕 | 由 §101.12(b) RACC 推导的 customary consumption 量 | 当成厂商建议食用量或营养建议 |
| RACC | 〔§ 101.12〕 | 按产品类别给出的参考量，是所有声称阈值与 Daily Value 的共同分母 | 抄表值当企业内控规格；表值为不可逐字引用区 |
| nutrient content claim | 〔§ 101.13(b)〕 | 明示或暗示表征 §101.9/§101.36 要求标示的营养素水平 | 以为「暗示」「品牌名」不算 claim |
| health claim | 〔§ 101.14(a)(1)〕 | 明示或暗示表征某物质与疾病/健康相关状况的关系，含 heart 符号、vignette、第三方引用 | 以为「有研究支持」即可；须 SSA + 不超 disqualifying level |
| significant scientific agreement | 〔§ 101.14(b)〕 | 合格科学专家间的显著科学一致，健康声称获授权的法规级证据门槛 | 与「有论文/有专家背书」混同 |
| disqualifying level | 〔§ 101.14(a)(4)〕 | 食品中特定营养素超过阈值即**丧失**健康声称资格 | 只查正面条件、漏查负面资格门槛 |
| gluten-free | 〔§ 101.91(a)(3)〕 | 不可避免的麸质存在须 **below 20 ppm**，是定量定义 | 当成「无添加」营销词；与亚硫酸盐 10 ppm 混算 |
| incidental additive | 〔§ 101.100(a)(3)〕 | 量不显著且在该食品中无技术或功能效果，可免配料表申报 | 以为一律免申报；亚硫酸盐 ≥10 ppm 是反向例外 |
| 标签义务豁免 | 〔§ 101.100〕/〔§ 101.9(j)〕/〔§ 101.108〕 | 免的分别是配料表 403(i)(2) / 营养标签 / 经 FDA 批准的临时实验 | 把 §101.100 当营养标签豁免；把主体豁免混进来 |
| misbranding | 〔§ 101.18〕/ FD&C Act §403 | 标签或 labeling 中虚假或误导性陈述使食品错标 | 与 402(a) adulteration（掺假）混为一条执法钩子 |

> 完整 44 条见 `books/cfr-part101-2026/GLOSSARY.md`；YAML 块内 t234–t277 已并入上方词典。
"""

TEST_CASES = [
    {
        "id": "part101-01", "type": "should_trigger",
        "prompt": "我们要给一款圆柱罐装饮料设计标签，主展示面该怎么算面积？营养成分表和配料表能放背面吗？字号有没有法定要求？",
        "expected_behavior": "应激活 CAP-30 入口卡并路由到 V01 `labeling-architecture`：〔§ 101.1〕PDP 面积按 (a) 矩形高×宽 / (b) 圆柱或近圆柱 40% 高×周长 / (c) 其他形状 40% 总表面，圆柱容器强制信息须落在这 40% 内；〔§ 101.2〕信息面板是紧邻 PDP 右侧的法定相对方位而非任意空白面；〔§ 101.4(a)(1)〕配料按重量降序以通用名列出；〔§ 101.15〕显著性与字号本身即义务。须提示这是法规正文层〔§ 101.xxx〕，不是〔§ 117.xxx〕，且标签合规不等于食品安全合规。",
        "notes": "V01 正面场景：PDP 面积公式 + 信息面板方位 + 显著性"
    },
    {
        "id": "part101-02", "type": "should_trigger",
        "prompt": "一款小包装零食要不要做 Nutrition Facts？serving size 是我们建议消费者一次吃的量吗？RACC 表里的数值能直接抄进内控规格吗？",
        "expected_behavior": "路由到 V02 `nutrition-labeling-serving-size`：〔§ 101.9(a)〕默认一律提供营养信息，豁免须落在 (j) 列举款；serving size 由〔§ 101.9(b)〕+〔§ 101.12(b)〕RACC 推导，是监管比较基准而非厂商建议量，也是所有声称阈值的共同分母。§101.12 Table 1/2（约 113 页流式列值）与 Appendix B/C/D 图形为不可逐字引用区，只可引「产品类别 → RACC → label statement」对应关系并回原表核对；须核对 eCFR 2026-11-05 快照与 FR citation。",
        "notes": "V02 正面场景：豁免对象 + serving size 推导 + 表值引用纪律"
    },
    {
        "id": "part101-03", "type": "should_trigger",
        "prompt": "包装上印了个心形符号，品牌名里带 heart，写「high in oat bran」算不算需要授权的声称？我们有几篇论文支持，能做健康声称吗？",
        "expected_behavior": "路由到 V03 `claims-authorization-gates`：〔§ 101.14(a)(1)〕health claim 含品牌名、heart 符号、vignette、第三方引用；〔§ 101.13(b)(2)〕implied nutrient content claim 同样受管。健康声称须〔§ 101.14(b)〕significant scientific agreement（法规级证据门槛，不是「有论文支持」）+ 不超 disqualifying level + 落在 §101.72–83 已授权模型或经 §101.70 请愿。须提示 gluten-free〔§ 101.91〕below 20 ppm 与亚硫酸盐〔§ 101.100(a)(4)〕10 ppm 是不同条款不同判据。",
        "notes": "V03 正面场景：暗示/符号构成 claim + SSA 门槛"
    },
    {
        "id": "part101-04", "type": "should_trigger",
        "prompt": "我们做未巴氏杀菌的苹果汁，已经按 Part 120 做完 5-log 验证了，是不是就不用贴 WARNING 了？反过来贴了警示是不是可以不做 5-log？果汁百分比声明怎么写？",
        "expected_behavior": "路由到 V04 `specific-foods-warning-statements`：〔§ 101.17(g)〕未经 (g)(7) 所述工艺处理的果汁须带逐字 WARNING 声明；〔§ 101.30(b)〕百分比声明格式为 `Contains __ percent (or %) ______ juice`，<1% 用 `less than 1 percent juice`。两层义务不可互推：贴了警示不等于做过〔§ 120.24〕5-log（工艺义务转 CAP-26），做了 5-log 也只是让 (g) 警示不适用、不自动免 §101.30 等其他标签义务；检查员取证转 CAP-27 / CP 7303.847。",
        "notes": "V04 ★ 三层接口：5-log ↔ 警示双向互推纠偏"
    },
    {
        "id": "part101-05", "type": "should_trigger",
        "prompt": "我们产品属于 §101.100 的豁免范围，是不是不用做 Nutrition Facts 了？另外配料里亚硫酸盐很少，按 incidental additive 免申报可以吗？",
        "expected_behavior": "路由到 V05 `labeling-exemptions-effect-level`（横切层，须依附 V01/V02 使用）：〔§ 101.100(a)〕免的是 FD&C Act **403(i)(2) 配料表**要求，营养标签豁免在〔§ 101.9(j)〕，两者不可互替；〔§ 101.108〕是 FDA 书面提案获批的临时标签实验，Part 117〔§ 117.5〕是主体/活动豁免，四套对象切分。〔§ 101.100(a)(3)〕incidental additive 须「量不显著且无技术或功能效果」，(a)(4) 明定亚硫酸盐成品 ≥**10 ppm** 即不得免申报（反向例外）。须提示 403 misbranding 与 402 adulteration 是两条独立执法钩子。",
        "notes": "V05 正面场景：四套豁免对象 + 10 ppm 反向例外"
    },
    {
        "id": "part101-06", "type": "edge_case",
        "prompt": "我们是 qualified facility，FSP 记录简化了；那标签是不是也可以整体免标？还有 FDA 那份过敏原问答 Ed.5 说未列入 Table 1 的树坚果不得进 Contains 声明，这条是不是 21 CFR 101 的规定？",
        "expected_behavior": "应识别为跨层混淆。Part 117〔§ 117.5〕/〔§ 117.201〕的 qualified facility 是**主体/活动**豁免，只减 Subparts C/G 负担，不触及 Part 101 标签义务（转 CAP-09 + V05）。Ed.5（2025-01）解释的是 FD&C Act §201(qq)/§403(w)，属 **guidance 建议层**，Big 9 / Table 1 树坚果封闭清单 / allergen-free 与 advisory 声明互斥**不得标成〔§ 101.xxx〕**（转 CAP-05）。须明确七套法规编号与二十二类不可混引，且标签合规不替代危害分析。",
        "notes": "兄弟诱饵①：主体豁免 + Ed.5 guidance 层不得混入 Part 101 法条层"
    },
    {
        "id": "part101-router-01", "type": "router_reachable",
        "prompt": "我们想在包装上写「低脂」「高纤」，还想用 20 ppm 的 gluten-free 声明；另外包装正面有个心形图案，这些分别该按什么规则审？",
        "expected_behavior": "CAP-30 入口卡路由表应把该意图指向 V03 `claims-authorization-gates`（`references/capabilities/labeling/claims-authorization-gates.md`），而非 V01（载体位置）、V02（份量基准）、V04（强制警示）或 V05（豁免/效力层）。V03 内再分：低脂/高纤是 §101.13 + Subpart D〔§ 101.62〕等营养素含量声称；gluten-free 是 Subpart F〔§ 101.91〕定量定义；心形图案按 §101.14(a)(1) 属健康声称暗示。serving size / RACC 分母不足时补读 V02。",
        "notes": "router_reachable①：V03 与 V01/V02/V04 的近邻区分"
    },
    {
        "id": "part101-router-02", "type": "router_reachable",
        "prompt": "未巴氏果汁的 WARNING 声明字号位置、随货单据披露、以及 100% juice 的百分比措辞，该看哪张卡？",
        "expected_behavior": "CAP-30 入口卡应指向 V04 `specific-foods-warning-statements`（`references/capabilities/labeling/specific-foods-warning-statements.md`），而非 V01（PDP/显著性虽相关但不是警示措辞本体）、V03（声称授权）或 V05（豁免）。关键依据：〔§ 101.17〕各款是独立立法，措辞/位置/例外不得互借；〔§ 101.17(g)〕散装非零售或异地加工可免但随货单据须披露未处理；〔§ 101.30〕给百分比声明格式。5-log 工艺问题须另转 CAP-26〔§ 120.24〕，不得在本卡内回答。",
        "notes": "router_reachable②：V04 与 V01/V03 的近邻区分 + CAP-26 外转"
    },
    {
        "id": "part101-07", "type": "edge_case",
        "prompt": "我们的 Nutrition Facts 完全合规、标签也都贴对了，是不是就可以不做危害分析和预防控制了？另外进口时被 FDA 以 misbranding 扣留，IOM Chapter 6 的 Form FDA 766 改标重整是不是我们的标签义务？",
        "expected_behavior": "两个都要否定并分层。**标签合规 ≠ 食品安全合规**：〔§ 101.18〕/FD&C Act §403 misbranding 与 §402 adulteration 是两条独立执法钩子，一张合规 Nutrition Facts 不能替代 Part 117 的危害分析与预防控制（转 CAP-01）。IOM 2026 Ch.6（CAP-29）是 FDA 给入境审查员/调查员的**内部作业手册**，非法规、不创设企业义务，`must/shall` 约束 FDA 内部作业；Form FDA 766 改标重整是扣留后的处置程序，不是企业的标签内容义务。错标的实体判定依据部分回到 Part 101，但 IOM 时限与文书不得写成企业义务。",
        "notes": "兄弟诱饵②：标签合规不能替代危害分析 + IOM 作业层不创设义务"
    },
    {
        "id": "part101-08", "type": "should_not_trigger",
        "prompt": "帮我们设计一条坚果共线产线的过敏原换产清洁验证方案，并制定 may contain 咨询声明的传递规则；另外给果汁巴杀工艺定 5-log 的关键限值和热穿透验证方案。",
        "expected_behavior": "**不应**加载 CAP-30 / labeling 子卡。过敏原交叉接触控制、换产清洁验证、may contain / advisory 声明三选一属 `allergen-program` CAP-05（Part 117〔§ 117.135(c)(2)〕+ Ed.5 guidance 层）；果汁 5-log 工艺设计、关键限值与热穿透验证属 `juice-haccp` CAP-26〔§ 120.24〕与 `process-control-validation` CAP-03。CAP-30 只管标签内容与形式的法定义务，不设计工艺、不做厂内控制；仅当追问「那 §101.17(g) 警示要不要贴」时才转 CAP-30 V04。",
        "notes": "互斥负例：厂内过敏原控制 + 5-log 工艺设计不得吸附到 CAP-30"
    },
]


def load_candidates() -> list[dict]:
    txt = (ROOT / "candidates" / "glossary.md").read_text(encoding="utf-8")
    body = txt[txt.find("- id: t101-01"):]
    data = yaml.safe_load(body)
    assert isinstance(data, list) and len(data) == 44, f"candidate glossary parse: {type(data)}"
    return data


def build_yaml_entries(data: list[dict]) -> str:
    out = ["\n# ============ v4.18 增量：21 CFR Part 101 食品标签法规正文（t234–t277，44 条） ============\n"]
    for i, e in enumerate(data, start=234):
        entry = {
            "id": f"t{i}",
            "title": str(e["title"]),
            "type": "term",
            "source_chapter": f"21 CFR Part 101 {e['clause']}（eCFR 2026-11-05 快照，法规正文层）",
            "source_quote": f'"{e["quote"]}"',
            "summary": str(e["summary"]),
            "tags": list(e.get("tags") or []) + ["v4.18", "Part 101", "法规正文层"],
        }
        block = yaml.safe_dump([entry], allow_unicode=True, sort_keys=False,
                              default_flow_style=False, width=10 ** 6)
        out.append(block.rstrip() + "\n")
    return "\n".join(out)


def glossary_markdown(data: list[dict]) -> str:
    lines = [
        "# 21 CFR Part 101（eCFR 2026-11-05）— 关键概念词典（阶段 3 产出）",
        "",
        "> 44 条术语，全部回 `source-cfr-part101-2026.md` 原文逐字核验（英文引用 ≤100 词）。",
        "> 本件属**法规正文层 / 第七套编号**〔§ 101.xxx〕，与 Part 117 预防控制层、Ed.5 guidance 层不同源，不得混引。",
        "> 已并入 `fda-pchf-food-safety/references/glossary.md` 的 YAML 块，编号 t234–t277。",
        "",
        "| # | 术语 | 条款 | 中文释义（浓缩） | tags |",
        "|---|---|---|---|---|",
    ]
    for i, e in enumerate(data, start=234):
        s = str(e["summary"]).replace("|", "｜").replace("\n", " ")
        if len(s) > 150:
            s = s[:147] + "…"
        tags = ", ".join(str(x) for x in (e.get("tags") or []))
        lines.append(f"| t{i} | {str(e['title']).replace('|', '｜')} | {e['clause']} | {s} | {tags} |")
    lines += ["", "## 引用纪律", "",
              "- §101.12 Table 1/2（约 113 页流式列值）、Appendix B/C/D 图形、9 个纯图形页为不可逐字引用区。",
              "- eCFR 2026-11-05 是快照且自述 `authoritative but unofficial`；RACC / DV / 阈值须复核 FR citation。",
              "- FD&C Act 全文、21 CFR part 102 / 130 / 105.66 / 110、§104.20、AOAC 方法等一律标「转引未收」。",
              ""]
    return "\n".join(lines)


def digest_md() -> str:
    return """# DIGEST — 21 CFR Part 101 食品标签法规正文，蒸馏为可执行能力

> 面向读者：本技能包的使用者（食品合规 / 法规事务 / 工厂质量）。本次把 eCFR 2026-11-05 现行版 21 CFR Part 101（352 页 / 50 条款）蒸馏成 **CAP-30 一个入口 + 5 张 RIA++ 子卡**，并入已迭代到 v4.17 的 `fda-pchf-food-safety` 技能包（升级为 v4.18）。

## 一句话

**Part 101 管「标签上必须写什么、只能怎么说」，Part 117 管「生产过程怎么控制危害」——两套法源并行、互不减免，而「标签合规」永远不能替代危害分析。**

## 为什么这次升级重要

既有包对「标签」的所有表述都在 **guidance / Part 117 层**：过敏原 Ed.5 问答解释 FD&C Act §403(w)，〔§ 117.135(c)(2)〕把「标签控制」列为一类过敏原预防控制，CAP-29 处理进口扣留的 misbranding 作业。**但没有一处收录 Part 101 法规正文本体**。结果是：用户问「配料表怎么写」「圆柱罐 PDP 面积怎么算」「低脂能不能写」时，包里只能靠指南旁推，给不出条款级依据。本次补上的正是这一层。

## 五个可执行能力

1. **标签载体与强制信息架构（V01）**：先定哪些信息强制，再定放主展示面还是信息面板。PDP 不是视觉正面——〔§ 101.1〕给的是面积公式，圆柱容器是「高 × 周长的 40%」，且强制信息必须落在这 40% 内；信息面板是 PDP 右侧的法定相对方位；配料表按重量降序、用通用名；字号与显著性本身就是可开观察项的义务。
2. **营养标签与份量基准（V02）**：〔§ 101.9(a)〕默认一律提供营养信息，豁免须落在 (j) 列举款。serving size 不是厂商建议食用量，而是由〔§ 101.12〕RACC 推导的监管比较基准，并且是所有声称阈值的共同分母。§101.12 那 113 页表值在文本层失真，只能引「产品类别 → RACC → label statement」的对应关系并回原表核对。
3. **声称三层闸门（V03）**：先判是不是 claim——**暗示、品牌名、heart 符号、vignette、第三方引用都算**；再分营养素含量声称 / 健康声称 / 描述性声称；再过负面门槛（disqualifying level、婴幼儿禁用）；再过正面授权（SSA + Subpart D 逐词定义或 Subpart E 已授权模型）。gluten-free 是 **below 20 ppm** 的定量定义，不是「无添加」营销词。
4. **特定品类与强制警示（V04）**：〔§ 101.17〕各款是独立立法，措辞、位置、例外不得互相借用。本次最有价值的接口是 **〔§ 101.17(g)〕未巴氏果汁 WARNING ↔ 〔§ 120.24〕5-log ↔ CP 7303.847 检查取证**三层：**贴了警示不等于做过 5-log，做了 5-log 也不自动免 §101.30 等其他标签义务**。
5. **豁免体系与效力层（V05，横切）**：四套豁免对象不可互替——〔§ 101.100〕免的是 **403(i)(2) 配料表**、〔§ 101.9(j)〕免营养标签、〔§ 101.108〕是 FDA 书面提案获批的临时实验、Part 117〔§ 117.5〕是主体/活动豁免。403 misbranding 与 402 adulteration 是两条独立执法钩子。

## 六条最该记住的纠偏

| 常见说法 | 正确判定 |
|---|---|
| 「我们属于 §101.100 豁免，不用做 Nutrition Facts」 | §101.100 免的是配料表 403(i)(2)；营养标签豁免在 §101.9(j) |
| 「标签都合规了，危害分析可以省」 | 403 错标 / 402 掺假两条独立钩子；标签合规 ≠ 食品安全合规 |
| 「包装上只是个心形图案，不算声称」 | §101.14(a)(1) 明列符号、品牌名、vignette、第三方引用 |
| 「有几篇论文支持就能作健康声称」 | 须 significant scientific agreement + 不超 disqualifying level + 落在已授权模型 |
| 「做了 5-log 就不用贴果汁警示」 | 工艺义务、标签义务、检查取证三层不可互推 |
| 「20 ppm 和 10 ppm 是同一类阈值」 | 前者是 gluten-free〔§ 101.91〕，后者是亚硫酸盐可检出〔§ 101.100(a)(4)〕，对象与后果都不同 |

## 边界

- 本件是 **eCFR 2026-11-05 快照**，页脚自述 `authoritative but unofficial`；不是 GPO 正式文本、不是新规发布日，具体数值须复核条文末尾 FR citation。
- §101.12 Table 1/2、Appendix B/C/D 图形、9 个纯图形页为**不可逐字引用区**。
- FD&C Act 全文、FALCPA 法定过敏原定义本体、21 CFR part 102/130/105.66/110、§104.20、AOAC 方法等一律「转引未收」。
- 与既有 21 类来源合计 **二十二类不可混引**；法规正文（七套编号）＞ FDA 指南（should）＞ CPGM/CP/IOM 检查程序（检查员视角、不创设企业义务）。

## 审计

阶段 0 `BOOK_OVERVIEW.md` → 阶段 1 五路并行（182 方法类候选 + 44 术语 / 556 个英文引用段全命中）→ 阶段 1.5 三重验证 5/5 → 阶段 1.6 晋级门全部 router → 阶段 2 五张 RIA++ 卡（93 个引用块 93/93 PASS）→ 阶段 3 Zettelkasten 11 条 also_read → 阶段 4 触发/路由用例 10 条 → 阶段 5 增量安装与静态登记校验。完整轨迹见 `PIPELINE_STATE.md` 与 `.cangjie/`。
"""


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    assert n == 1, f"{label}: expected exactly 1 occurrence, got {n}"
    print(f"  [OK] {label}")
    return text.replace(old, new, 1)


def main() -> int:
    data = load_candidates()
    print(f"candidate glossary: {len(data)} entries")
    report: dict = {}

    # ---------- 1. glossary.md ----------
    gp = SKILL / "references" / "glossary.md"
    g = gp.read_text(encoding="utf-8")
    fence = g.find("\n```", g.find("```yaml") + 7)
    assert fence > 0, "glossary yaml closing fence not found"
    entries = build_yaml_entries(data)
    g_new = g[:fence] + "\n" + entries.rstrip() + "\n\n" + g[fence:]
    g_new = g_new.rstrip() + "\n" + GLOSSARY_TAIL
    # strict YAML check on the fenced block
    block = g_new.split("```yaml", 1)[1].split("\n```", 1)[0]
    parsed = yaml.safe_load(block)
    assert isinstance(parsed, list), "glossary yaml did not parse to list"
    ids = [x["id"] for x in parsed]
    assert len(ids) == len(set(ids)), "duplicate glossary ids"
    assert ids[-1] == "t277" and len(ids) == 277, f"glossary id count/last: {len(ids)} / {ids[-1]}"
    print(f"  [OK] glossary: {len(parsed)} entries, first {ids[0]}, last {ids[-1]}, unique ids")
    report["glossary_entries"] = len(parsed)

    # ---------- 2. SKILL.md ----------
    sp = SKILL / "SKILL.md"
    s = sp.read_text(encoding="utf-8")
    s = replace_once(s, "  cangjie.capability-count: 29\n", "  cangjie.capability-count: 30\n",
                     "frontmatter capability-count 29 → 30")

    lines = s.splitlines(keepends=True)
    desc_idx = next(i for i, l in enumerate(lines)
                    if l.startswith("  另覆盖 FDA 进口准入判定与处置链（IOM 2026 Chapter 6"))
    lines.insert(desc_idx + 1, NEW_DESC_LINE)
    s = "".join(lines)
    print("  [OK] SKILL.md frontmatter description: appended v4.18 paragraph")

    anchor = "## 能力路由（先读本表，按意图加载 1 张能力卡）"
    s = replace_once(s, anchor, CORE_57 + "\n" + anchor, "core principle #57 inserted")

    route_anchor = "| 判断 FDA 进口准入与处置链（IOM 2026 Chapter 6）"
    ri = s.find(route_anchor)
    assert ri >= 0, "CAP-29 route row not found"
    eol = s.find("\n", ri)
    s = s[:eol + 1] + ROUTE_ROW + s[eol + 1:]
    print("  [OK] SKILL.md route table: CAP-30 row inserted after CAP-29")

    route_idx_anchor = "| CAP-29 |"
    # (capability-index handled separately below)

    for old, new, label in [
        ("37. 六套法规正文〔§ 108.xxx〕", "37. 七套法规正文〔§ 101.xxx〕〔§ 108.xxx〕", "core #37 seven numbering sets"),
        ("合计**二十类不可混引**（v4.8 新增", "合计**二十二类不可混引**（v4.8 新增", "core #37 count"),
        ("v4.17 新增第二十一来源 IOM 2026 Ch.6）",
         "v4.17 新增第二十一来源 IOM 2026 Ch.6、v4.18 新增第二十二来源 21 CFR Part 101）",
         "core #37 v4.18 source"),
        ("- 条款引用必须核对原文：六套法规正文分别以〔§ 108.xxx〕",
         "- 条款引用必须核对原文：七套法规正文分别以〔§ 101.xxx〕〔§ 108.xxx〕",
         "citation discipline seven sets"),
        ("**二十一类不可混引**（IOM 2026 Ch.6 自 v4.17 起已收，见 CAP-29）",
         "**二十二类不可混引**（IOM 2026 Ch.6 自 v4.17 起已收，见 CAP-29；21 CFR Part 101 自 v4.18 起已收，见 CAP-30）",
         "citation discipline 22 sources"),
        ("- 用户任务超出 29 张能力卡路由范围时",
         "- 用户任务超出 30 张能力卡路由范围时", "out-of-scope guard"),
        ("全包自 v4.17 起**二十一类不可混引**，当前为 29 张能力卡",
         "全包自 v4.18 起**二十二类不可混引**，当前为 30 张能力卡", "seafood boundary count"),
    ]:
        s = replace_once(s, old, new, label)

    # Append the Part 101 boundary bullet at the end of the boundary list.
    s = s.rstrip() + "\n" + BOUNDARY_LINE
    print("  [OK] SKILL.md boundary: v4.18 Part 101 bullet appended")

    # Global current-state wording sweeps (historical "第二十一来源" statements are preserved).
    for old, new in [
        ("二十一类不可混引", "二十二类不可混引"),
        ("29 张能力卡", "30 张能力卡"),
        ("六套法规正文", "七套法规正文"),
    ]:
        n = s.count(old)
        if n:
            s = s.replace(old, new)
        print(f"  [SWEEP] {old} -> {new}: {n} occurrence(s)")

    # ---------- 3. capability-index.md ----------
    ip = SKILL / "references" / "capability-index.md"
    idx = ip.read_text(encoding="utf-8")
    ci = idx.find("| CAP-29 |")
    assert ci >= 0, "CAP-29 index row not found"
    eol = idx.find("\n", ci)
    idx_new = idx[:eol + 1] + INDEX_ROW + idx[eol + 1:]
    assert idx_new.count("| CAP-30 |") == 1
    print("  [OK] capability-index: CAP-30 row inserted")

    # ---------- 4. cheatsheet.md ----------
    cp = SKILL / "references" / "cheatsheet.md"
    c = cp.read_text(encoding="utf-8")
    marker = "\n> 速查只给结论"
    assert marker in c
    c_new = c.replace(marker, "\n" + CHEAT_ROW + marker, 1)
    assert c_new.count("21 CFR Part 101 食品标签法定义务与判定链") == 1
    print("  [OK] cheatsheet: CAP-30 row inserted")

    # ---------- 5. overview.md ----------
    op = SKILL / "references" / "overview.md"
    o = op.read_text(encoding="utf-8")
    o_new = o.rstrip() + "\n" + OVERVIEW_SECTION
    print("  [OK] overview: v4.18 section appended")

    # ---------- 6. test-prompts.json ----------
    tp = SKILL / "test-prompts.json"
    t = json.loads(tp.read_text(encoding="utf-8"))
    existing = {x["id"] for x in t["test_cases"]}
    assert not (existing & {x["id"] for x in TEST_CASES}), "duplicate test ids"
    t["test_cases"].extend(TEST_CASES)
    t["version"] = "4.18"
    t["notes"] = (str(t.get("notes", "")) +
                  " v4.18 新增 10 条 part101-* 用例（5 should_trigger / 3 edge_case 含 2 条 router_reachable / 1 条 should_not_trigger 互斥负例），"
                  "覆盖 CAP-30 五个能力单元与『主体豁免 / Ed.5 guidance / 5-log 工艺 / IOM 作业层』四类兄弟诱饵。").strip()
    t_json = json.dumps(t, ensure_ascii=False, indent=2) + "\n"
    report["test_cases"] = len(t["test_cases"])
    print(f"  [OK] test-prompts: {len(t['test_cases'])} cases, version {t['version']}")

    # ---------- 7. audit artifacts ----------
    audit = {
        "GLOSSARY.md": glossary_markdown(data),
        "DIGEST.md": digest_md(),
        "rejected/merged-duplicates.md": (
            "# 阶段 1.5 候选级去重记录（无单元级淘汰）\n\n"
            "5 路提取器共产出 182 个方法类候选（framework 88 / principles 48 / cases 26 / "
            "counter-examples 20）与 44 条术语。经三重验证后合并为 **5 个能力单元**，"
            "**0 个单元被淘汰**。\n\n"
            "## 去重规则\n\n"
            "- 同一条法规规则在 framework 与 principles 中重复出现 → 合并为同一单元的一条「方法论陈述」，"
            "另一个候选的条款出处并入「跨域佐证」（V1 证据）。\n"
            "- counter-examples 的 20 条误读全部并入各单元 E 段，不单设「误读卡」——"
            "误读不是独立能力，而是能力边界。\n"
            "- cases 的 26 条实例全部并入各单元 A1 段情景，不单设「案例卡」。\n"
            "- glossary 的 44 条术语全部并入 `GLOSSARY.md` 与安装目录术语表（t234–t277）。\n"
            "- §101.12 Table 1/2 数值、Appendix B/C/D 图形、9 个纯图形页因「不可逐字引用」"
            "不构成候选单元，但作为「回原表核对」纪律写入 5 张子卡 B 段。\n\n"
            "## 覆盖率硬门\n\n"
            "检索式 extractor（案例 / 反例 / 术语）相对全量扫描基线漏检数 **0**："
            "框架与原则提取器均报告 50/50 条款全覆盖，检索式未覆盖条款由其兜底。\n"
        ),
        "test-results/phase4-cases.json": json.dumps(TEST_CASES, ensure_ascii=False, indent=2) + "\n",
    }

    # ---------- write ----------
    files = {
        gp: g_new, sp: s, ip: idx_new, cp: c_new, op: o_new, tp: t_json,
    }
    for rel, content in audit.items():
        files[ROOT / rel] = content

    if APPLY:
        for p, content in files.items():
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
        (ROOT / ".cangjie" / "apply_v4_18_report.json").write_text(
            json.dumps({"applied_at": datetime.now().isoformat(), **report},
                       ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nAPPLIED: {len(files)} files written")
    else:
        print("\nDRY RUN complete — pass --apply to write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
