#!/usr/bin/env python3
"""v4.8 内容扩展：术语 t153–t162、评测用例 fsvp-01..10、状态文档同步。"""
from __future__ import annotations

import json
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
GLOSS = BOOK / "candidates/glossary.md"
GLOSS_ROOT = BOOK / "GLOSSARY.md"
TP = BOOK / "test-prompts.json"

# ---------------------------------------------------------------- 1. 术语表
t = GLOSS.read_text(encoding="utf-8")
print("glossary 十二类 -> 十三类:", t.count("十二类"))
t = t.replace("十二类", "十三类")
t = t.replace("全包自 v4.6 的十类扩为 **十三类不可混引**",
              "全包口径为 v4.6 十类 → v4.7 十二类 → **v4.8 十三类不可混引**")
anchor = "\n```\n\n## 自检记录"
assert t.count(anchor) == 1, f"glossary fenced-block anchor count {t.count(anchor)}"

NEW_TERMS = """
- id: t153
  title: FSVPI（§1.500 importer）与美国货主/收货人定义
  type: term
  source_chapter: CP 7303.878 PART I.1 / 21 CFR part 1 subpart L §1.500（转引未收）
  summary: FSVP 语境下的 importer 指入境时该食品的美国货主或收货人；若入境时没有美国货主/收货人，则为经签署同意书确认、代表境外货主/收货人的美国代理或代表，可缩写 FSVPI。不要把「进口商」泛化成报关行、货代或境外出口商；CP 7303.878 自己写明 `the term importer hereinafter means importer as defined in 21 CFR 1.500`。
  tags: [FSVP, FSVPI, 1.500, 进口商定义, CP 7303.878, v4.8]

- id: t154
  title: FSVP 与 Part 117 Subpart G 供应链程序是两套法源、两类主体
  type: term
  source_chapter: CP 7303.878 PART II.3.A / 21 CFR part 117 Subpart G〔§ 117.135〕
  summary: FSVP 由 FSMA §301 增订的 FD&C Act §805 授权，法规为 21 CFR part 1 subpart L（§§1.500–1.514），义务主体是进口商 FSVPI；Supply-Chain Program 由 FD&C Act §418 授权、法规为 21 CFR part 117 Subpart G，义务主体是接收设施 receiving facility。二者常被混为「供应商验证」，但法条编号、记录要求与检查 program 都不同。本包未收 part 1 subpart L 正文，一律标「转引未收」。
  tags: [FSVP, 供应链程序, 双法源, 805, 418, 1.500, 117.135, v4.8]

- id: t155
  title: deemed compliance 与 §1.509 例外
  type: term
  source_chapter: CP 7303.878 PART II.3.A / CPGM 7303.040 PART III
  summary: 进口商同时是 manufacturer/processor 且被认定符合 21 CFR part 117（或 507）供应链要求时，视为对其进口食品符合 FSVP 要求；但原文括号 `except they must comply with section 1.509 of the FSVP regulation` 把入境标识义务单独留下。反向口径同样重要：不是 receiving facility 的进口商 `must comply with the FSVP requirements for that food`，没有该通道；仅受 Subpart B CGMP 或 §117.206 / §507.51 约束的仓储设施也可能单独接受 FSVP 检查。
  tags: [deemed compliance, 1.509, receiving facility, 117.206, 507.51, v4.8]

- id: t156
  title: §1.509 每一 entry line 的 UFI / DUNS 申报
  type: term
  source_chapter: CP 7303.878 PART I.1 / PART V.1.A
  summary: FSVPI 须确保在向 CBP 报关时，对**每一条 entry line** 以电子方式提供其名称、电子邮箱与 FDA 认可的唯一设施标识 UFI；FDA 认可的是 DUNS 号码。不是「每年报一次」或「每家企业报一次」。PART V.1.A 把未确保这些信息电子申报列为较轻一档观察，PART III.1.A 把相关 handout 列为检查员应提供的资源。
  tags: [1.509, UFI, DUNS, CBP, entry line, FSVP, v4.8]

- id: t157
  title: §1.501 八类 FSVP 豁免与 modified requirements 分节
  type: term
  source_chapter: CP 7303.878 PART I.1 / PART I.2
  summary: 豁免见 §1.501(b)–(h)：符合 part 120 / 123 的果汁与水产及其原料、研究评估用、个人消费、酒精饮料相关、转运过境、进口加工后复出口且不在美销售、美国出口后未再境外加工而退回、进口时受 USDA 管辖的特定肉禽蛋制品。FSVP 条款又分 standard（§1.502/503/504/505/506/508/509/510）与 modified（§1.507 危害进口后受控、§1.511 膳食补充剂、§1.512 VSI 或小境外供应商、§1.513 SRA）；原文明确符合 modified 条件者**可以选择**走 standard。part 120 / 123 正文本包未收。
  tags: [1.501, 豁免, standard requirements, modified requirements, 1.512, 1.513, v4.8]

- id: t158
  title: FSVP 检查不取样、PART IV 全空
  type: term
  source_chapter: CP 7303.878 PART III.1.C / PART IV
  summary: 原文 `Samples will not be collected as part of an FSVP inspection.`，PART IV – ANALYTICAL 四节全部 `Intentionally Left Blank`。FSVP 检查是记录审评型：查按食品建立的 FSVP、书面危害分析、供应商批准评价与验证活动记录、§1.509 记录、纠正措施。不得把 CP 7303.050 的 subs 样品量、环境拭子、WGS / PAF 代码套过来；检查可 on-site 或 remote（RRA 的法定地位另见 CAP-19）。
  tags: [不取样, PART IV, 记录审评, 7303.050, RRA, 483a, v4.8]

- id: t159
  title: FSVP 483a 观察分级、NAI/VAI/OAI 与执法裁量因素
  type: term
  source_chapter: CP 7303.878 PART V.1
  summary: 最重大观察包括未 develop/maintain/follow FSVP、无书面危害分析或未记录对他方危害分析的审阅（尤其 SAHCODHA 危害）、无供应商批准评价、无验证活动、未履行 modified requirement 活动、以及 FDA 书面索取后未及时提供 FSVP 记录；较轻一档含未记录批准、未建书面程序、未记录 FSVP 变更、未确保 §1.509 信息。分类为 NAI / VAI / OAI。PART V.1.C 要求权衡违法史、SAHCODHA 风险、进口量、是否首次检查（`Initial FSVP violations should be prioritized ... only when there are known food safety risks`）、偏差范围、自愿合规与渐进改善、是否换商号继续进口。
  tags: [483a, NAI, VAI, OAI, SAHCODHA, 执法裁量, v4.8]

- id: t160
  title: §801(a)(3) 拒绝入境、§301(zz) 禁止行为与 direct reference authority
  type: term
  source_chapter: CP 7303.878 PART V.2 / PART V.3
  summary: FSVPI 不符合 FSVP 即违反 §805；FDA 可依 §801(a)(3) / §1.514(a) 拒绝该食品入境，官方指控措辞见 CAP-21 R 段；无合规 FSVP 而进口另构成 §301(zz)（21 U.S.C. 331(zz)）/ §1.514(b) 禁止行为，并可引出 §302 禁令、§303 刑事与 §306 debarment。但 WL / Untitled Letter / Import Alert 99-41 的 direct reference authority **只在有限情形授予**（HFP Enforcement Bulletin #13），其余须经 CMS 送 HFP OCE OE Imports Enforcement Branch（动物食品 CVM OSC DFC）并取得分类一致。
  tags: [801(a)(3), 301(zz), 1.514, direct reference, CMS, 拒绝入境, v4.8]

- id: t161
  title: Import Alert 99-41 Red List 与 99-37/99-38 不得混引
  type: term
  source_chapter: CP 7303.878 PART V.3.C / CP 7303.070 PART V.2
  summary: 99-41 针对 FSVP 不合规进口商，按「具体食品 + 具体境外供应商」组合或全部食品列入 Red List；未列组合在不受其他掺假/误标 Alert 约束时仍可继续进口，移除须按 99-41 指示向原发函 Division 提交证据、经 CMS 建议并咨询 Center，且应先申请移除再进口。99-37 / 99-38 属 CP 7303.070 的 LACF/AF 备案与过程控制轨道，且该卡另有「不得仅因未注册/未备案建议 DWPE」的反直觉限制。两者触发条件、列名对象与法律 hook 都不同。
  tags: [99-41, Red List, 99-37, 99-38, DWPE, 移除流程, v4.8]

- id: t162
  title: CP 7303.878 版本口径、CP 7303.819 状态与十三类不可混引
  type: term
  source_chapter: CP 7303.878 首页 / Change History p4 / 全包引用规范
  summary: 本件是 Transmittal 2023-CPM-CFSAN-003、Implementation Date 09/27/2023 的 2023 版程序，Date of Issuance 08/28/2025 对应 Change History 的 Corrections（仅重组后 POC 与机构名称缩写更新），不是 2025 新 program；与 7303.050（2022/2025-09-10 更正）、7303.070（2024/2025-09-26 更正）同型。CP 7303.819 是 2006 FY06/07/08 旧程序、已过 COMPLETION DATE 9/30/08 而非现行，准确说法不是「法规意义上废止」。全包自 v4.8 起为**十三类不可混引**：三套法规正文〔§ 117/113/114.xxx〕＋ PCHF 指南 / L.mono 指南 / SECG / Ed.5 / Handbook 五类参考指南层 ＋ CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / CP 7303.878 五类检查员作业层；检查员作业指导不创设企业义务。
  tags: [7303.878, 版本陷阱, 7303.819, 十三类不可混引, 收录边界, v4.8]
"""
t = t.replace(anchor, "\n" + NEW_TERMS + anchor, 1)

# 自检记录：条数 + 新增来源行
t = t.replace("全包 v4.6 时为十类、**v4.7 起十二类不可混引**，全库 **152 条**",
              "全包口径 v4.6 十类 → v4.7 十二类 → **v4.8 十三类不可混引**，全库 **162 条**")
t = t.replace("全包 v4.6 时为十类、**v4.7 起十三类不可混引**，全库 **152 条**",
              "全包口径 v4.6 十类 → v4.7 十二类 → **v4.8 十三类不可混引**，全库 **162 条**")
t += ("\n- [x] 第十三来源 FDA CP 7303.878（Transmittal 2023-CPM-CFSAN-003，2023-09-27 版 / 2025-08-28 更正，33 页 / 20 书签）"
      "术语 t153–t162 共 10 条已并入（FSVPI 定义、FSVP 与 Part 117 Subpart G 双法源、deemed compliance 与 §1.509 例外、"
      "每一 entry line 的 UFI/DUNS、§1.501 豁免与 standard/modified 分节、FSVP 检查不取样、483a 观察分级与 NAI/VAI/OAI、"
      "§801(a)(3)/§301(zz) 与 direct reference、Import Alert 99-41 与 99-37/99-38 区分、版本口径与十三类不可混引）；"
      "原文标「CP 7303.878 PART x」，21 CFR part 1 subpart L 正文一律标『转引未收』。全库 162 条，v4.8。\n")
GLOSS.write_text(t, encoding="utf-8")
GLOSS_ROOT.write_text(t, encoding="utf-8")
print(f"glossary ids: {t.count('- id: t')} (expect 162)")

# ---------------------------------------------------------------- 2. 评测用例
d = json.loads(TP.read_text(encoding="utf-8"))
assert d["version"] == "4.7" and len(d["test_cases"]) == 85
d["version"] = "4.8"

raw = TP.read_text(encoding="utf-8")
print("test-prompts 十二类 -> 十三类:", raw.count("十二类"))
for c in d["test_cases"]:
    c["expected_behavior"] = c["expected_behavior"].replace("十二类", "十三类")
    c["notes"] = c["notes"].replace("十二类", "十三类")

CASES = [
    dict(id="fsvp-01", type="should_trigger",
         prompt="我们公司既做进口也是加工厂，已经按 21 CFR Part 117 做了完整的供应链验证，是不是就不用单独建 FSVP 了？",
         expected_behavior="应激活本技能并加载 fsvp-inspection-program 卡（辅读 supply-chain-verification）：① 先按 §1.500 判 FSVPI 身份，再区分 FSVP（FD&C Act §805 / 21 CFR part 1 subpart L）与 Part 117 Subpart G 供应链程序（FD&C Act §418）是两套法源、两类主体；② 引用 CP 7303.878 PART II.3.A 与 CPGM 7303.040 PART III 的 deemed compliance 原文，说明制造商/加工商符合 part 117（或 507）供应链要求时视为符合 FSVP；③ **必须点出括号例外** `except they must comply with section 1.509`，即每一 entry line 的 UFI/DUNS 电子申报不免除；④ 补反向口径：不是 receiving facility 的进口商仍须完整 FSVP；⑤ 21 CFR part 1 subpart L 正文转引未收，全包十三类不可混引。",
         notes="v4.8：deemed compliance 与 §1.509 例外"),
    dict(id="fsvp-02", type="should_trigger",
         prompt="FDA 通知下周来做 FSVP 检查，我们要按 CP 7303.050 准备多少 subs 样品、环境拭子怎么布点？",
         expected_behavior="应激活本技能并加载 fsvp-inspection-program 卡（辅读 inspection-sampling）：① 明确纠正串轨——CP 7303.878 PART III.1.C 原文 `Samples will not be collected as part of an FSVP inspection.`，PART IV – ANALYTICAL 四节全部 `Intentionally Left Blank`；② CP 7303.050 的 subs 数、环境拭子 50/100、Zone 1–3、WGS/GenomeTrakr、PAF 代码属于另一个 program，不得套用；③ 给 FSVP 检查真正要备的六组记录（按食品建立的 FSVP、书面危害分析与他方分析审阅、供应商批准评价、验证活动、§1.509 入境标识、纠正措施与 483a 回复）；④ 检查可 on-site 或 remote，纠正措施记 EIR 与 CAR；⑤ 全包十三类不可混引。",
         notes="v4.8：FSVP 检查不取样，反串轨纠偏"),
    dict(id="fsvp-03", type="edge_case",
         prompt="报关时那个 UFI 到底填什么？是每家企业报一次还是每次进口都要报？",
         expected_behavior="应激活本技能并加载 fsvp-inspection-program 卡：① §1.509 要求 FSVPI 对**每一条 entry line** 在向 CBP 报关时电子提供名称、电子邮箱与 FDA 认可的 UFI；② FDA 认可的 UFI 是 **DUNS 号码**（CP 7303.878 PART I.1）；③ 不是每企业一次或每年一次；PART V.1.A 把未确保该信息电子申报列为较轻一档观察；④ §1.509 是 deemed compliance 的明文例外，即使被视为符合 FSVP 也不能免；⑤ 21 CFR part 1 subpart L 正文转引未收，不得从 CP 反推条文。",
         notes="v4.8：UFI/DUNS 每 entry line"),
    dict(id="fsvp-04", type="should_trigger",
         prompt="我们进口果汁、水产品、酒精饮料，还有一批只过境转运的货，哪些可以不做 FSVP？",
         expected_behavior="应激活本技能并加载 fsvp-inspection-program 卡：① 引 CP 7303.878 PART I.2 的 §1.501(b)–(h) 八类豁免；② 果汁与水产/水产品的豁免是**有条件的**——供应商须符合 21 CFR part 120 / 123，用于制造这些产品的原料则要求 FSVPI 自身符合 part 120 / 123；③ 其余：研究或评估用 (c)、个人消费 (d)、酒精饮料及相关特定食品 (e)、转运过境 (f)(1) 与进口加工后复出口且不在美销售 (f)(2)、美国生产出口后未再境外加工而退回 (g)、进口时受 USDA 管辖的特定肉禽蛋制品 (h)；④ part 120 / 123 正文本包未收，标转引未收；⑤ 不要漏掉 §1.509 的 UFI 义务与 FSVP 检查不取样的口径提示。",
         notes="v4.8：§1.501 八类豁免与条件性豁免"),
    dict(id="fsvp-05", type="edge_case",
         prompt="我们符合极小进口商 VSI 的条件，是不是就必须走 modified requirements？standard 那套还能选吗？",
         expected_behavior="应激活本技能并加载 fsvp-inspection-program 卡：① 分列 standard（§1.502/503/504/505/506/508/509/510）与 modified（§1.507 危害进口后受控、§1.511 膳食补充剂、§1.512 VSI 或小境外供应商、§1.513 SRA）；② 引 PART I.1 原文 `FSVPIs who meet the criteria for modified requirements may choose to follow standard requirements`——modified 是**可选路径**不是强制降级；③ PART III.1.A.ii 的取证口径：检查员须独立在 EIR 写明适用哪套要求，企业说「No FSVP」不约束该判定；无任何 modified 记录（含资格证明）可引「No FSVP」under §1.502(a)，有任一 §1.512 记录即按 modified 检查；④ §1.511(c) 须先排除 (a)/(b) 并考虑转 OP13；⑤ 21 CFR part 1 subpart L 正文转引未收。",
         notes="v4.8：standard / modified 可选关系与 VSI 取证"),
    dict(id="fsvp-06", type="should_trigger",
         prompt="刚收到 FSVP 检查的 Form FDA 483a，哪些观察项算最严重、会怎么升级？",
         expected_behavior="应激活本技能并加载 fsvp-inspection-program 卡（辅读 investigator-authority-procedure）：① PART V.1.A 六类最重大观察——未 develop/maintain/follow FSVP、无书面危害分析或未记录对他方危害分析的审阅（尤其 SAHCODHA 危害）、无供应商批准评价、无验证活动记录、未履行 modified requirement 的 FSVP 活动、**FDA 书面索取后未及时以电子或其他方式提供记录**；② 较轻一档四项（未记录批准、未建书面程序、未记录 FSVP 变更、未确保 §1.509 信息）；③ PART V.1.B/C 的鼓励自愿纠正、八项裁量因素与 NAI/VAI/OAI 分类；④ 升级路径：regulatory meeting → Warning Letter / Untitled Letter → Import Alert 99-41 → §801(a)(3) 拒绝入境，但须说明 direct reference authority 仅在有限情形授予、其余经 CMS 送 Center；⑤ 全包十三类不可混引，483a 措辞纪律转 CAP-18。",
         notes="v4.8：483a 观察分级与执法阶梯"),
    dict(id="fsvp-07", type="edge_case",
         prompt="第一次 FSVP 检查被开了缺陷，是不是马上会收到警告信、货也会被扣？",
         expected_behavior="应激活本技能并加载 fsvp-inspection-program 卡：① 引 PART V.1.C `Initial FSVP violations should be prioritized for regulatory action only when there are known food safety risks associated with the food or foreign supplier`——首次违法**不默认优先执法**；② 列其余裁量因素（违法史、RTE/宠物食品/已知 SAHCODHA 风险的农产品与暴发召回掺假过敏原误标的关联、进口量、偏差局限还是持续扩大、自愿合规与渐进改善、是否与另一被执法 FSVPI 共用责任人或换新商号）；③ PART V 的策略是 `to obtain industry compliance`，Division 应先鼓励 voluntary corrective actions；④ 说明 WL → 99-41 Red List 的触发前提（WL 后未纠正、无回复或回复不足）与 §801(a)(3) 拒绝入境的法律 hook，不得写成必然后果；⑤ 检查员作业指导不创设企业义务，全包十三类不可混引。",
         notes="v4.8：首次违法不默认优先执法"),
    dict(id="fsvp-08", type="should_trigger",
         prompt="公司被列进 Import Alert 99-41 了，是不是所有进口食品都进不来？要怎么才能移除？",
         expected_behavior="应激活本技能并加载 fsvp-inspection-program 卡：① PART V.3.C.i 的列名粒度是「具体食品 + 具体境外供应商」组合或全部食品；② 反直觉限制——`An FSVPI that is not listed on the Red List of FSVP Import Alert 99-41 may continue to import the same food and other food from a listed foreign supplier`，前提是不受其他掺假/误标 Import Alert 约束；③ 移除流程按 99-41 指示向原发函 Division 提交证据 → Division 经 CMS 建议 OIO/DIO → 咨询 HFP OCE OE 或 CVM OSC DFC，必要时做 FSVP 检查核实；④ `Divisions should encourage FSVPIs to request removal ... prior to attempting to import`——先申请移除再进口；⑤ 提醒 99-41 与 99-37/99-38 不是同一个 Alert，Import Alert 全文转引未收。",
         notes="v4.8：99-41 Red List 粒度、反直觉限制与移除流程"),
    dict(id="fsvp-09", type="edge_case",
         prompt="Import Alert 99-41 和做低酸罐头时说的 99-37/99-38 是一回事吗？没备案是不是就自动 DWPE？",
         expected_behavior="应激活本技能并加载 fsvp-inspection-program 卡（辅读 lacf-inspection-program）：① 99-41 属 CP 7303.878，针对 FSVP 不合规的进口商，依 §801(a)(3) 对食品作 DWPE；99-37（无 filed scheduled process）与 99-38（过程控制不足）属 CP 7303.070，针对 LACF/AF 轨道；② 列名对象不同：99-41 是 FSVPI / 食品 / 境外供应商组合，99-37/99-38 是企业与产品；③ **不得仅因未注册/未备案建议 DWPE** 是 CP 7303.070 PART V.2 的原文限制，须先查 FURLS / Center Views 的 FCE 与 SID；④ 两者法律 hook 与触发条件不同，不得混引；⑤ Import Alert 全文、part 108 正文均转引未收，全包十三类不可混引。",
         notes="v4.8：99-41 vs 99-37/99-38，反 DWPE 陷阱"),
    dict(id="fsvp-10", type="edge_case",
         prompt="CP 7303.878 首页写着 2025 年签发，是新规吧？顺便把 21 CFR 1.505 原文、Import Alert 99-41 全文和 FSVP Guidance Q&A G.8 列出来。",
         expected_behavior="必须区分「本包可答」与「转引未收」：① 版本陷阱——Change History 为 2021-10-20 首发 → 2023-09-27 Update → 2024-08-20 Pen/Ink → **2025-08-28 Corrections（仅 POC 与机构名称缩写更新）**，故为 Transmittal 2023-CPM-CFSAN-003 的 2023 版程序之更正版，不是 2025 新 program，与 7303.050 / 7303.070 同型，也不同于 CPGM 7303.040 的 2025-CPM-HFP-001；② **21 CFR part 1 subpart L（§§1.500–1.514）法规正文本包未收**，§1.505 原文、Import Alert 99-41 全文、FSVP Guidance Q&A G.8、FSVP Implementation Work Instructions、IP guidance tabs、HFP Enforcement Bulletin #13/#6、RPM 4-1-8 一律标「转引未收」，不得从 CP 反推条文或代填；③ 可给的是 CP 内的程序性口径与出处；④ 顺带可纠正 CP 7303.819 是 2006 FY06-08 旧程序、已过 completion date 而非现行；⑤ 全包十三类不可混引。",
         notes="v4.8：版本陷阱与转引未收边界"),
]
d["test_cases"].extend(CASES)
d["notes"] += (" | v4.8 追加 10 条 fsvp-* 用例（deemed compliance 与 §1.509、FSVP 检查不取样、UFI/DUNS、"
               "§1.501 豁免、standard/modified 可选关系、483a 观察分级、首次违法裁量、99-41 Red List 与移除、"
               "99-41 vs 99-37/99-38、版本陷阱与转引未收）；新增第 21 张卡 fsvp-inspection-program，"
               "第十三来源为 FDA CP 7303.878（2023 版 / 2025-08-28 更正），全包十三类不可混引。"
               "v4.7 的触发盲测与补充质量评测结果见 .cangjie/v4-7-output-routing-eval-report.md，本版未重跑评测。")
TP.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"test-prompts version {d['version']} cases {len(d['test_cases'])}")
print("remaining 十二类 in test-prompts:", TP.read_text(encoding="utf-8").count("十二类"))
