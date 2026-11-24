#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""append_v4_6.py — 把 CP 7303.070（第十来源 / CAP-19）的术语与用例并入 glossary 与 test-prompts。"""
import json
from pathlib import Path

BASE = Path("E:/WeChatData/2026-11-04-09-51-05/books/fda-pchf-human-food-guidance")
GLOSS = BASE / "candidates/glossary.md"
TESTS = BASE / "test-prompts.json"

TERMS = """- id: t135
  title: CP 7303.070 的版本形态（2024 签发 / 2025-09-26 更正，文件名 20250929 只是生成日）
  type: term
  source_chapter: FDA CP 7303.070 首页（p1）；PDF 元数据 title / creationDate
  source_quote: |
    "Date of Issuance: 09/26/2024" / "IMPLEMENTATION DATE: 9/26/2024" / "Correction Date: 9/26/2025"
  summary: 用户提供的 61 页 508-Compliant PDF 首页为 **Date of Issuance 09/26/2024、IMPLEMENTATION DATE 9/26/2024、Correction Date 9/26/2025**；PDF title 亦写 `(Implementation Date 09/26/2024)`，creationDate 2025-09-29。文件名 `20250929` 是 **PDF 生成日，不是签发日**；本件是 **2024 版程序的 2025 更正本**，与 CP 7303.050（2022 签发 / 2025-09-10 更正）同属更正本形态，不同于 CPGM 7303.040 的 `2025-CPM-HFP-001`（新 Transmittal、08/29/2025 签发）。引用写「CP 7303.070（2024 签发 / 2025-09-26 更正）」，不要写成「2025 版 7303.070」。首页 PAC `03070A/B/C`（境内 AF / LACF / 无菌 LACF）、`03070F/G/J`（进口）、`71070`（动物食品）；PAF `ACD`（常规）、`MIC`（仅 C. botulinum for-cause）；Problem Codes `AFD / ACF / LAF`。
  tags: [CP 7303.070, 版本陷阱, 更正本, PAC, PAF, 十类不可混引]

- id: t136
  title: §117.5(d)(1)(2) 的 LACF 管辖分流与 AF 不豁免（CP 7303.070 官方细化）
  type: term
  source_chapter: CP 7303.070 PART II.2.C(1)；21 CFR 117.5(d)(1)(2)、117.1(c)
  source_quote: |
    "LACF products are subject to the CGMP and PCHF rule (21 CFR part 117). However, subparts C and G do not apply to activities covered by 21 CFR part 113" / "The exemption in paragraph (d)(1) of this section is applicable only with respect to the microbiological hazards that are regulated under part 113 of this chapter." / "Acidified foods are subject to the CGMP & PCHF rule."
  summary: 本包最容易被误用的一处。**①** LACF 受 Part 117 约束，〔§ 117.5(d)(1)〕只免 **part 113 覆盖活动**的 Subparts C/G；**②**〔§ 117.5(d)(2)〕再限定该豁免**仅限 part 113 管辖的微生物危害**；CP 逐字给出残余危害：`Staphylococcus aureus` 生长与产毒、化学危害、物理危害仍归 Subparts C/G。**③**〔§ 117.1(c)〕明定受专项 CGMP 法规管辖的食品同时受 Part 117 约束，Subpart B/F 不因该豁免消失。**④** **酸化食品不在 § 117.5(d) 内**：`Acidified foods are subject to the CGMP & PCHF rule`，其 PCHF 覆盖转 CP 7303.040，检查重点仍在 21 CFR part 108/114（不论规模）。**⑤** ⚠〔§ 117.201〕是 **qualified facility 的 modified requirements**（attestation、双份保证书、7 月 31 日），**不是 LACF 条款，不得误引**。CP 原文标「CP 7303.070 PART II.2.C(1)」，法规标〔§ 117.5(d)(1)(2)〕，两者不可混引。
  tags: [管辖分流, 117.5(d), 117.1(c), 117.201, 酸化食品, 双法规并集, 高频误读]

- id: t137
  title: 法源三角 21 CFR part 108 / 113 / 114（CP 7303.070 转引未收）
  type: term
  source_chapter: CP 7303.070 PART I、PART II.1 Objectives、PART VII.2；21 CFR 117.1(c)
  source_quote: |
    "In addition, 21 CFR part 108 “Emergency Permit Control” requires manufacturers of AF or LACF to register their processing plants, file their scheduled processes with FDA and to adhere to the mandatory requirements expressed in the GMPs."
  summary: CP 7303.070 据以判定合规的法源是 **part 108（Emergency Permit Control：FCE 加工厂注册、SID 定时工艺备案）、part 113（密封容器热加工低酸食品）、part 114（酸化食品）**，三套正文**本包均未收**。CP 内出现的 FCE、SID、SUP-SID、filed scheduled process、Process Authority、商业无菌、Emergency Permit、BPCS（Better Process Control School）、Form 2541e 等都属**转引**，只能标「转引未收」，**不得从 CP 反推法条**，也不得把 CP 的检查动作（观察运行中 retort、审核温度分布/热穿透、卷边完整性、冷却水消毒残留、异常罐处置、投诉档案）写成 Part 117 的企业义务。PART VII.2 把 LACF Registration and Process Files 归 HFP；FURLS 的 AF/LACF 注册备案系统可判 LACF / AF / aseptic / aw-controlled 及容器尺寸、加工方式、关键因子。完整判定见 CAP-19 `lacf-inspection-program`。
  tags: [21 CFR part 108, 21 CFR part 113, 21 CFR part 114, FCE, SID, Process Authority, 转引未收]

- id: t138
  title: 酸化食品判定三步与 Maximum Equilibrium pH
  type: term
  source_chapter: CP 7303.070 PART III.1.A Acidified Food Determination（STEP 1–3）
  source_quote: |
    "This value is called the “Maximum Equilibrium pH”." / "Submit the information to HFP-OCE-OE-LACF-AND-ACIDIFIEDFOODS@fda.hhs.gov for review to determine if there is a significant difference between the pH of the finished product and the predominant acid(s) or acid food(s)."
  summary: 检查员遇「疑似酸化食品」时收集配方与包装信息交 HFP 判定。**STEP 1**：合并全部 pH ≤4.6 的酸成分 + 全部配方用水，测该混合物 pH；**STEP 2**：加入全部 pH >4.6 的低酸成分，固体研磨/匀浆成与成品同比例的平滑混合物，测得值称 **"Maximum Equilibrium pH"**；**STEP 3**：送 HFP 官方邮箱由 HFP 判断成品 pH 与主导酸/酸性食品之间是否存在 significant difference。所有配料须与成品同品种同比例。包装判 ROP 的阈值是最终包装氧透过率 `< 10,000 cc/m²/24 hours at 24°C`（源文 `10,000 cc/ m[2] /24 hours at 24ºC` 为 PDF 上标转录）。企业自判产品身份时成品**至少测 6 个单元**；⚠ **最终法定身份由 HFP 判定，本包不得替企业下结论**。注意平衡 pH 4.6 的法定定义与持续维持义务在〔§ 117.3〕〔§ 117.80(c)(14)〕，不是 CP 创设。
  tags: [酸化食品判定, Maximum Equilibrium pH, ROP, 平衡 pH, HFP 判定, CP 7303.070]

- id: t139
  title: 三套 pH / aw 数字（法定边界 / 检查员触发线 / L.mono 建议层）
  type: term
  source_chapter: 〔§ 117.3〕〔§ 117.80(c)(14)(15)〕；CP 7303.070 PART IV.2；L.mono 指南 IX
  source_quote: |
    "If one or more containers have pH values equal to or greater than 4.40, or if the mean pH plus 2 standard deviations is equal to or greater than 4.40, a second analyst must promptly (same day) re-determine the pH values" / "Never average the two analysts' results together."
  summary: 三套数字互不替代。**第一套（法定）**：pH **4.6**（平衡 pH，〔§ 117.3〕定义、〔§ 117.80(c)(14)〕须监测并维持）、aw **0.85**（LACF 管辖/安全水分，〔§ 117.80(c)(15)〕须加工至并维持安全水分水平）。**第二套（CP 7303.070 检查员/实验室作业）**：pH **4.40** 触发第二分析师同日换 pH 计复测、**4.65** 触发两分析师各测余下半数、**4.75**（异常罐 + 活的嗜温革兰阳性厌氧芽孢菌）触发 botulinum neurotoxin 与 `C. botulinum` PCR；aw **0.90 / 0.93** 触发换仪器在同 3 罐复测；`Never average the two analysts' results together`——original analysis 与 check analysis 分别判定。**第三套（L.mono 草案建议层）**：pH ≤**4.4**、aw ≤**0.92** 是 listeristatic 配方设计基准。⚠ 三者用途不同、不得互替：pH 4.5 勉强满足酸化管辖、会触发 CP 复测、却不满足 L.mono 抑制目标；4.40/4.65/1%/24 罐也不是企业放行标准。
  tags: [pH 4.6, pH 4.40, pH 4.65, pH 4.75, aw 0.85, aw 0.90, aw 0.92, 三套数字, 高频误读]

- id: t140
  title: 异常罐 1%、795 g / 24 罐与 14 天 progressive decomp（FDA 取证口径）
  type: term
  source_chapter: CP 7303.070 PART III.1.A Inspectional Considerations、PART III.1.B、PART IV.2、PART V.1
  source_quote: |
    "Visual observation of warehoused product that shows a significant number of abnormal containers (greater than 1%) where the firm has not conducted a spoilage diagnosis" / "The total sample size for containers 795 grams (i.e., 28 oz.) net weight or smaller is 24 containers.  The total sample size for all others is 12 containers."
  summary: 检查员取证口径。**异常容器 >1% 且企业未做 spoilage diagnosis**（判定腐败原因与批次能否放行）是检查员侧的显著观察项；PART V.1 把「异常容器 ≥1% 批确认掺假或进行性腐败」列为通知 Center 的触发之一；进口侧异常率 1% 以上须另提 DTR。pH 分析取样：**≤795 g（28 oz）取 24 罐，其余 12 罐**；具体抽样计划出处是 **IOM Chapter 4, Sample Schedule Chart 2（正文未收）**。实验室对正常容器做 **14 天 progressive decomp** 培养，异常罐另做气体/气味/外观、净重与沥干重、漏罐测试、卷边解剖与内壁状态检查；`C. botulinum` 分析**仅 for-cause**（PAF `MIC`），涉病走 BAM Ch.17、不涉病走 BAM Ch.21A，典型分离株做 WGS 送 HFP/OLOAS 做毒素基因评价。⚠ 这些都是 FDA 取证与执法建议口径，不是企业内控抽样或放行标准。
  tags: [异常罐, 1%, 795 克, 24 罐, progressive decomp, BAM, 非放行标准]

- id: t141
  title: Import Alert 99-37 / 99-38 与「未备案不自动 DWPE」陷阱
  type: term
  source_chapter: CP 7303.070 PART III.2 Import Entry Review、PART V.2 (f)
  source_quote: |
    "Do not recommend firm/products for an Import Alert/DWPE solely based on firm/product not registered and/or filed processes with FDA since all LACF and acidified foods should be checked for registration and  process filing."
  summary: 两个 Import Alert 与一条反直觉限制。**#99-37** 针对「被判为 LACF/AF 且无 filed scheduled process」的 **DWPE（Detention Without Physical Examination）**；**#99-38** 针对「已提交 scheduled process 但过程控制不足」。⚠ 反直觉陷阱：CP 原文明确**不得仅因企业/产品未注册或未备案就建议列入 Import Alert/DWPE**——所有 LACF/AF 产品都须先查验注册与备案，且 #99-37 的适用以 `when FDA determines such action is necessary for efficient and effective protection of the public health` 为前提（例如检查显示潜在公共卫生风险、屡次规避备案）。进口审核：FDA import systems 用 AofC 交叉核验 **FCE 与 SID** 与 LACF/AF 数据库，系统查询失败须人工核验（Center Views 的 HFP tab）；地址无法核实或不符 → **DTR（detention recommendation）**；SID 与容器尺寸、品名、备案状态不符 → 现场查验或 DTR。加入 Red List 的建议经 CMS 报 DIO，非 direct reference 范围须附 Center concurrence。⚠ Import Alert 全文、CPG Sec. 520.200/520.300、RPM Ch.9 本包未收。
  tags: [Import Alert 99-37, Import Alert 99-38, DWPE, FCE, SID, DTR, 反直觉陷阱]

- id: t142
  title: RRA 程序性定义、Keep Refrigerated / brites 路由与十类不可混引
  type: term
  source_chapter: CP 7303.070 PART II.2.B(2)、PART II.2.C(1)(2)；FD&C Act 704(a)(1)
  source_quote: |
    "RRAs are not considered inspections, conducted pursuant to section 704(a)(1) of the FD&C Act" / "Products labeled “Keep Refrigerated” are exempt from 21 CFR 113/114. These products should be covered under Compliance Program 7303.050."
  summary: 程序定义与两条路由。**RRA（Remote Regulatory Assessment）**：FDA 可对 AF/LACF 企业开展**自愿、全程远程**的记录/设施评估；CP 明确 `RRAs are not considered inspections`，不满足 FD&C Act 704 条要求现场 inspection 的法定场景（如 510(h)、503B(b)）。这是 **CP 内的程序性定义**，可据此回答「RRA 算不算检查」，但 **FDA 扩大 RRA 适用范围 / 境外无预告检查的政策公告原文仍未收**，不得据此推导政策，也不能替换 IOM 5.2.7 的预告三层口径。**两条路由**：`Keep Refrigerated` 产品免 21 CFR 113/114 → 归 **CP 7303.050（CAP-17）**；未贴标 AF/LACF「brites」运至中央仓贴标装箱的检查报 **`PAC 03040`（CAP-16）**。另：动物食品 LACF 用 `71070` 并联动 7371.000 / 21 CFR 507.5(b)；海产品 LACF 并做 7303.842 HACCP。**收录边界**：第十来源 CP 7303.070 已收（CAP-19），全包自 v4.6 起 **十类不可混引**；但 21 CFR part 108/113/114 正文、IOM Ch.4 Chart 2、BAM、CPG、Import Alert 全文、其余 Compliance Programs 仍未收，一律标「转引未收」。
  tags: [RRA, Keep Refrigerated, brites, 7303.050, 7303.040, 十类不可混引, 收录边界, v4.6]
"""

CASES = [
    {
        "id": "lacf-01",
        "type": "should_trigger",
        "prompt": "我们是做酸化莎莎酱的（pH 4.1），听说低酸罐头企业可以免 PCHF 的 Subparts C 和 G，那我们是不是也不用做危害分析、FSP 和预防控制了？",
        "expected_behavior": "必须明确否定并给出条款级分流。①〔§ 117.5(d)(1)〕的豁免字面只写「受 21 CFR part 113 管辖且合规的活动」，〔§ 117.5(d)(2)〕进一步限定**仅限 part 113 管辖的微生物危害**；CP 7303.070 PART II.2.C(1) 逐字给出残余危害（Staphylococcus aureus 生长产毒、化学、物理）仍归 Part 117 Subparts C/G。② **酸化食品不在该豁免内**：CP 原文 `Acidified foods are subject to the CGMP & PCHF rule. Refer to the PCHF Compliance Program for PCHF coverage of acidified foods.`——PCHF 覆盖转 7303.040（CAP-16），但 `Regardless of the size of the operation`，AF 检查重点仍在 21 CFR part 108/114。③〔§ 117.1(c)〕另定受专项 CGMP 管辖食品同时受 Part 117 约束，Subpart B/F 不消失。④ ⚠ 不得把〔§ 117.201〕（qualified facility 的 modified requirements）当 LACF 条款。⑤ 21 CFR part 108/113/114 正文未收，相关表述标「转引未收」；引用分别用〔§ 117.xxx〕与「CP 7303.070 PART II.2.C(1)」，十类不可混引",
        "notes": "v4.6 第十来源：头号误读——AF 不免 Subparts C/G"
    },
    {
        "id": "lacf-02",
        "type": "should_trigger",
        "prompt": "我们是低酸罐头厂，肉毒风险由杀菌工艺控制；那化学危害（比如罐头内壁涂层迁移）和物理危害（金属碎屑）还要不要进 PCHF 的危害分析和预防控制？另外 §117.201 是不是就是 LACF 的修改要求？",
        "expected_behavior": "① 要。CP 7303.070 PART II.2.C(1) 与〔§ 117.5(d)(2)〕一致：豁免仅限 part 113 管辖的**微生物危害**，`Hazards that are not controlled by thermal processing requirements in 21 CFR part 113 and that require a preventive control are covered by 21 CFR part 117 subparts C and G (e.g., Staphylococcus aureus growth and toxin formation, chemical hazards and physical hazards)`。按危害类别逐格判定，不做全有全无（呼应 regulatory-boundaries 并集矩阵）。② 明确纠错：**〔§ 117.201〕是 qualified facility 的 modified requirements**（attestation、双份保证书、7 月 31 日通知等），与 LACF 无关；LACF 与 Part 117 的接口只有〔§ 117.5(d)(1)(2)〕与〔§ 117.1(c)〕。③ Subpart B（cGMP）与 F（记录）照常适用。④ part 113 正文未收，涉及具体杀菌与备案义务标「转引未收」",
        "notes": "v4.6 第十来源：残余危害归 C/G + §117.201 误引纠正"
    },
    {
        "id": "lacf-03",
        "type": "edge_case",
        "prompt": "我们有一款冷藏销售的酸化素食酱标签写了 Keep Refrigerated，还有一批没贴标的 brite 罐要运到中央仓贴标。FDA 来查会按 7303.070 吗？",
        "expected_behavior": "按 CP 7303.070 PART II.2.C 的官方分工路由，不要一律说「按 7303.070 查」。① `Products labeled “Keep Refrigerated” are exempt from 21 CFR 113/114. These products should be covered under Compliance Program 7303.050.` → 转 CAP-17 `inspection-sampling`（产品/环境样品量、for-cause 抽样）。② `Report inspections of central distribution warehouses where unlabeled AF or LACF containers (“brites”) are shipped for labeling and casing against PAC 03040.` → 转 CAP-16 `inspection-readiness`（7303.040 检查类型与记录举证）。③ 常规常温密封 LACF/AF 才走 7303.070（CAP-19）。④ 补充动物食品 `71070` / 7371.000、海产品 7303.842 HACCP 并行仅作分流提示，正文未收。⑤ 引用用「CP 7303.070 PART II.2.C(1)(2)」，十类不可混引",
        "notes": "v4.6 第十来源：Keep Refrigerated / brites 两条 program 路由"
    },
    {
        "id": "lacf-04",
        "type": "should_trigger",
        "prompt": "我们往低酸蔬菜里加了少量酸味配料，成品测 pH 4.3，这算酸性食品还是酸化食品？我们自己定就行吧，检查员要配方和包装信息合理吗？",
        "expected_behavior": "① 给 CP 7303.070 PART III.1.A 的判定三步：STEP 1 合并所有 pH ≤4.6 的酸成分 + 全部配方用水测 pH；STEP 2 加入全部 pH >4.6 的低酸成分、固体研磨成与成品同比例匀浆，测得 **\"Maximum Equilibrium pH\"**；STEP 3 送 `HFP-OCE-OE-LACF-AND-ACIDIFIEDFOODS@fda.hhs.gov` 由 **HFP 判断**成品 pH 与主导酸/酸性食品是否有 significant difference。企业自判时成品至少测 6 个单元；也可现场观察企业自判过程。② 包装信息合理：需判断是否形成厌氧环境，ROP 判据为最终包装氧透过率 `< 10,000 cc/m²/24h at 24°C`（源文 `10,000 cc/ m[2] /24 hours at 24ºC` 为 PDF 上标转录）。③ ⚠ **法定身份由 HFP 判定，本包不得替企业下结论**；配方与包装信息由检查员收集后交 HFP，不是检查员单方定性。④ 法定平衡 pH 4.6 定义与持续维持义务在〔§ 117.3〕〔§ 117.80(c)(14)〕，不是 CP 创设；part 114 正文未收，标「转引未收」",
        "notes": "v4.6 第十来源：酸化判定三步 + HFP 判定权 + ROP 阈值"
    },
    {
        "id": "lacf-05",
        "type": "edge_case",
        "prompt": "我们成品 pH 做到 4.5，是不是就合规了？检查员说还要第二个人用另一台 pH 计重测，两家结果能不能取平均？他们抽了 24 罐，我们内控是不是也照 24 罐抽？",
        "expected_behavior": "拆三套数字并否定取平均。① 法定：平衡 pH ≤4.6 是〔§ 117.3〕定义与〔§ 117.80(c)(14)〕持续维持义务，4.5 勉强满足酸化管辖一侧（且是平衡值，不是出锅一次测量）。② CP 7303.070 PART IV.2 实验室触发线：任一罐 pH ≥**4.40** 或均值 + 2SD ≥4.40 → 第二分析师**同日**用另一台 pH 计复测同批容器；>4.65 或均值 + 2SD >4.65 → 两分析师各用各自仪器测余下半数；`Never average the two analysts' results together`——original analysis 与 check analysis 分别判定。③ 取样量：≤795 g（28 oz）**24 罐**、其余 **12 罐**是 FDA 的 pH 分析样品量，具体抽样计划出处 IOM Ch.4 Sample Schedule Chart 2 未收；**不是企业内控或放行标准**。④ 三套数字还包括 L.mono 草案抑制型配方 pH ≤4.4 / aw ≤0.92（建议层）——pH 4.5 不满足抑制目标；aw 0.85 法定 vs 0.90/0.93 CP 复测触发也须区分。⑤ 引用分别用〔§ 117.xxx〕与「CP 7303.070 PART IV.2」，十类不可混引",
        "notes": "v4.6 第十来源：三套 pH/aw 数字 + Never average + 取样量非放行标准"
    },
    {
        "id": "lacf-06",
        "type": "edge_case",
        "prompt": "我们进口的一批酸化食品被查出没做 process filing，是不是马上会被列进 Import Alert 99-37 自动扣留？FCE 和 SID 到底怎么核？",
        "expected_behavior": "纠正简化说法。① CP 7303.070 PART V.2 原文 `Do not recommend firm/products for an Import Alert/DWPE solely based on firm/product not registered and/or filed processes with FDA since all LACF and acidified foods should be checked for registration and  process filing.`——**未注册/未备案本身不构成建议 DWPE 的充分理由**；#99-37 针对「被判为 LACF/AF 且无 filed scheduled process」，且以 FDA 认定 `necessary for efficient and effective protection of the public health` 为前提；#99-38 才是「已备案但过程控制不足」。② FCE/SID 查验：FDA import systems 用 AofC 与 LACF/AF 数据库交叉核验；查询失败人工核验（Center Views 的 HFP tab）；地址无法核实或不符 → DTR；SID 与容器尺寸/品名/备案状态不符 → 现场查验或 DTR；Red List 建议经 CMS 报 DIO 并附 Center concurrence。③ 明确边界：Import Alert 99-37/99-38 全文、CPG Sec. 520.200/520.300、RPM Ch.9、part 108 正文未收，标「转引未收」；不代写 DTR 应诉或预测扣留结果",
        "notes": "v4.6 第十来源：Import Alert 反直觉限制 + FCE/SID 核验与 DTR"
    },
    {
        "id": "lacf-07",
        "type": "should_trigger",
        "prompt": "FDA 通知要对我们做 RRA（远程监管评估），这是不是就等于检查完了？我们是不是可以不给记录？2025 年不是扩大无预告检查了吗，帮我们把政策依据列一下。",
        "expected_behavior": "分层回答，不编造政策条文。① CP 7303.070 PART II.2.B(2) 给**程序性定义**：RRA 自愿、全程远程，用于常规境内外监督无法开展或远程更合适时；`RRAs are not considered inspections, conducted pursuant to section 704(a)(1) of the FD&C Act`，且 `RRAs do not satisfy statutory requirements that specify inspection under section 704 of the FD&C Act (e.g., section 510(h) or 503B(b))`。**可以替代监督动作，不能替代法定检查**；因此「等于检查完了」不成立。② 记录义务不因远程而消失：〔§ 117.320〕口头或书面请求即须 promptly 提供并可供复制、〔§ 117.315(c)〕FSP 在现场/异地记录 24 小时内取回现场（记录举证矩阵见 CAP-16）。③ 预告口径仍以 IOM 5.2.7 为准：食品企业一般不预告（program division 裁量）、境外通常提前告知、国内预告一般不少于 5 个日历日、预告不是预约；**2025 年境外无预告检查扩张、RRA 适用范围与 704(a)(4) 检查前索取记录属 FDA 政策公告层，本包未收原文**，只作准备原则，不得写成条款级结论或编造公告编号。④ 引用用「CP 7303.070 PART II.2.B(2)」与「IOM 5.2.7」，十类不可混引",
        "notes": "v4.6 第十来源：RRA 程序性定义 + 预告口径不被替换 + 政策原文未收"
    },
    {
        "id": "lacf-08",
        "type": "should_trigger",
        "prompt": "这份 20250929 的 7303.070 是 2025 年新规吧？顺便帮我把 21 CFR part 113 里关于杀菌釜记录保存年限、Form 2541e 提交时限和 BAM Ch.21A 的培养步骤逐条列出来。",
        "expected_behavior": "① 版本纠错：文件名 `20250929` 只是 PDF 生成日；首页 `Date of Issuance 09/26/2024`、`IMPLEMENTATION DATE 9/26/2024`、`Correction Date 9/26/2025` 表明这是 **2024 版程序的 2025 更正本**，不是 2025 年新签发 program，不得套用 CPGM 7303.040 的 `2025-CPM-HFP-001` Transmittal 格式；与 CP 7303.050（2022 签发 / 2025-09-10 更正）同属更正本形态。② 明确**超出本包**：21 CFR part 108/113/114 正文、BAM Ch.13B/14/17/21A/22A-22D、IOM Ch.4 Sample Schedule Chart 2、CPG Sec. 520.200/520.300、Form 2541e 细则、SOP-001642、RPM Ch.4/9 **均未收**；CP 7303.070 里出现的相关内容一律标「转引未收」，**不得从 CP 反推法条或代填培养步骤/时限**。③ 可给到的：CP 里的检查员取证口径（filed scheduled process、Process Authority 参与温度分布/热穿透、运行中 retort 观察、卷边完整性、冷却水消毒残留、异常罐与投诉档案、BPCS 培训）与三类检查目标。④ 建议由具备资质的 Process Authority / PCQI 与法规正文核对；引用用「CP 7303.070 PART x」，十类不可混引",
        "notes": "v4.6 第十来源：版本陷阱 + 法源三角转引未收 + 不编造条款"
    },
]


def main():
    # 1) glossary
    text = GLOSS.read_text(encoding="utf-8")
    fence = text.rfind("\n```\n")
    assert fence > 0, "glossary closing fence not found"
    assert "- id: t135" not in text, "already appended"
    text = text[:fence] + "\n" + TERMS + text[fence:]
    lines = text.split("\n")
    idx = next(
        (i for i, l in enumerate(lines)
         if l.startswith("- [x] 第九来源 FDA IOM 2026 Chapter 5")),
        None,
    )
    assert idx is not None, "glossary checklist anchor missing"
    assert "全库 **134 条**" in lines[idx], "glossary count anchor missing"
    lines[idx] = lines[idx].replace("；全库 **134 条**", "")
    lines.insert(
        idx + 1,
        "- [x] 第十来源 FDA CP 7303.070（2024 签发 / 2025-09-26 更正）术语 t135–t142 已并入"
        "（版本形态、§117.5(d)(1)(2) 管辖分流与 AF 不豁免、法源三角转引未收、"
        "酸化判定三步与 Maximum Equilibrium pH、三套 pH/aw 数字、异常罐 1% 与 24 罐/12 罐、"
        "Import Alert 99-37/99-38 与 DWPE 陷阱、RRA 程序性定义与 Keep Refrigerated / brites 路由）；"
        "原文标「CP 7303.070 PART x / ATTACHMENT x」，21 CFR part 108/113/114 等未收正文一律标『转引未收』；"
        "全包自 v4.6 起**十类不可混引**，全库 **142 条**",
    )
    text = "\n".join(lines)
    GLOSS.write_text(text, encoding="utf-8")
    print("glossary: appended t135–t142 (total 142)")

    # 2) test prompts
    data = json.loads(TESTS.read_text(encoding="utf-8"))
    assert data["version"] == "4.5", data["version"]
    existing = {c["id"] for c in data["test_cases"]}
    for c in CASES:
        assert c["id"] not in existing, c["id"]
    # 旧用例里的「九类不可混引」口径同步为十类
    fixed = 0
    for c in data["test_cases"]:
        for k in ("expected_behavior", "notes", "prompt"):
            if k in c and "九类不可混引" in c[k]:
                c[k] = c[k].replace("九类不可混引", "十类不可混引")
                fixed += 1
    data["version"] = "4.6"
    data["test_cases"].extend(CASES)
    data["notes"] += (
        " | v4.6 追加 8 条用例（lacf-01..08）：酸化食品不免 Subparts C/G 的头号误读、残余危害与 §117.201 误引纠正、"
        "Keep Refrigerated / brites 路由、酸化判定三步与 HFP 判定权、三套 pH/aw 数字与 Never average、"
        "Import Alert 99-37 反直觉限制与 FCE/SID 核验、RRA 程序性定义与政策原文未收、版本陷阱与 108/113/114 转引未收；"
        "新增第 19 张卡 lacf-inspection-program（第十来源 CP 7303.070，2024 签发 / 2025-09-26 更正），全包十类不可混引；"
        f"并把既有 {fixed} 处「九类不可混引」同步为十类。"
    )
    TESTS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"test-prompts: v4.6, {len(data['test_cases'])} cases, {fixed} legacy strings fixed")


if __name__ == "__main__":
    main()
