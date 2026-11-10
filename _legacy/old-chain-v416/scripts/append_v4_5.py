#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""append_v4_5.py — 把 CP 7303.050 与 IOM 2026 Ch.5 的术语/用例并入 glossary 与 test-prompts。"""
import json
from pathlib import Path

BASE = Path("E:/WeChatData/2026-11-04-09-51-05/books/fda-pchf-human-food-guidance")
GLOSS = BASE / "candidates/glossary.md"
TESTS = BASE / "test-prompts.json"

TERMS = """- id: t123
  title: CP 7303.050 的版本形态（2022 签发 / 2025-09-10 更正，非 2025 新 program）
  type: term
  source_chapter: FDA CP 7303.050 首页（p1）；文件名 20250915_...
  source_quote: |
    "Date of Issuance: 06/03/2022" / "IMPLEMENTATION DATE 06/03/2022" / "Correction date: 09/10/2025"
  summary: 用户提供的 62 页 508-Compliant PDF 首页为 **Date of Issuance 06/03/2022、IMPLEMENTATION DATE 06/03/2022、Correction date 09/10/2025**；PDF 元数据 creationDate 2025-09-10、作者 HFP/OCE。文件名里的 `20250915` 指**2022 版程序的 2025 年更正本**，不是 2025 年新签发的 program；与 CPGM 7303.040 的 `2025-CPM-HFP-001`（新 Transmittal、08/29/2025 签发）不是同一种版本形态，不得互相套用。⚠ 本 program `Inspections are not planned under this compliance program`——它是**抽样 program**，检查由 7303.040 等 interacting programs 承担，只在其中视情形采 for-cause 产品/环境样；「7303.050 检查」「7303.050 分级」都是错误说法。引用用「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」。
  tags: [CP 7303.050, 版本陷阱, 抽样 program, 非检查 program, 高频误读]

- id: t124
  title: subs（份样）与 702(b) 部分（FDA 取证量，非企业放行标准）
  type: term
  source_chapter: FDA CP 7303.050 PART III.1.C / Sample Size；Table 2、Table 3；FD&C Act 702(b)；21 CFR 2.10(b)(3)
  source_quote: |
    "The sample size does not include 702(b) portions. See IOM Chapters 4 and 6 for additional information on 702(b) portion. Do not collect 702(b) sample portions for perishable products (see  21 CFR 2.10(b)(3)) or for samples collected in import status (unless otherwise requested)." / "In the absence of specific instruction, randomly collect ten (10), 2 lb. subsamples."
  summary: CP 7303.050 的样品量以 **subs（份样）** 计：Table 2 给 Salmonella（如叶菜 30 subs × 100 g、番茄 10 subs × 454 g、RTE 三明治 30 subs × 100 g、散装奶酪按重量分 10/2/1 subs），Table 3 给其他分析物（如 L. mono 10 subs × 200 g、EHEC/STEC 10 × 50 g、Cyclospora 5 × 50 g、甲肝/诺如 3 × 150 g）。三条硬规则：① **样品量不含 702(b) 部分**；② 多分析物按最大 subs 数取足且每 sub 同时满足各分析物用量；③ **易腐产品与进口状态样品不取 702(b) 部分**（21 CFR 2.10(b)(3)）。ATTACHMENT B 的污秽/霉变样在无专门指令时为随机 10 个 2 lb subs，奶酪制样取 6 个 227 g 且不得合并。⚠ 这些是 **FDA 检查员的取证量**，不是企业批放行抽样计划、不是内控规格；企业抽样须依自身危害分析与验证另定。702(b) 分割留样细则在 IOM Chapter 4，本包未收。
  tags: [CP 7303.050, 抽样量, 702(b), subs, 非放行标准, 高频误读]

- id: t125
  title: 环境拭子 50/100 与 Zone 分区（CP 7303.050 ATTACHMENT A）
  type: term
  source_chapter: FDA CP 7303.050 ATTACHMENT A Part III.C / Sample Size / Table 1 Sampling Framework
  source_quote: |
    "A minimum of 50 subsamples (ideally 100 subs) should be collected for _Listeria_ analysis and a minimum of 100 subs (ideally 300 subs) should be collected for _Salmonella_ analysis." / "Investigators may determine whether to swab for _Listeria_ or for _Salmonella_ based on the food being manufactured during the inspection and the environment in which the food is exposed."
  summary: 资格前提两项：① 生产**包装前暴露于环境**的 RTE 食品且无后续致死处理/无抑制型配方控制；② 检查期间**正在加工** RTE 食品。数量：**Listeria 最少 50 subs（理想 100）、Salmonella 最少 100 subs（理想 300）**；点位不足须在检查结束前联系 program monitor。Table 1 的 Collection Zones 为 Listeria 主要 zones 1-3、Salmonella 主要 zones 2-3（逐字原文见本条 source_quote 与卡片 R 段）；湿区偏 L. monocytogenes、偶发受潮的干区偏 Salmonella；历史环境阳性厂在原阳性 Zone 及邻近加密。⚠ 这是**检查员选点与取证量**，不是企业环境监测频次标准（后者见 L.mono 2017 Draft 建议层与 environmental-pathogen-sanitation 卡）。运输须 UPS Next Day Air Early A.M.、24 h 到室、周一至周四发运、周五不发、冷藏不冷冻；Salmonella 分析须在采集后 48 ± 2 h 内启动，超时样品无效。
  tags: [CP 7303.050, 环境取样, Zone 1, Zone 2, 50 subs, 100 subs, 湿干二分]

- id: t126
  title: WGS / GenomeTrakr 与环境拭子不计数
  type: term
  source_chapter: FDA CP 7303.050 PART IV.5.a、ATTACHMENT A Part IV.3.A / 3.C / Part IV.4
  source_quote: |
    "All positive samples for the following pathogens must send an isolate to WGS for analysis, unless otherwise specified or requested." / "WGS must be performed immediately on all confirmed _Listeria monocytogenes_ or _Salmonella_ positives and the results must be submitted to GenomeTrakr database, the national sub-typing network for foodborne disease surveillance." / "No enumeration will be performed on environmental swab/sponge samples."
  summary: 确认阳性的 **Salmonella / L. monocytogenes / E. coli O157:H7 或其他 STEC** 分离株一律做全基因组测序并上传 GenomeTrakr；环境拭子若分离出 L. mono 或 Salmonella（Zone 1/2/3），须联系 HFP/OCE 请求与**同厂历史分离株及 CDC 临床株**比对（非致病 Listeria spp. 不请求），可能翻出多年定殖史。产品 L. mono 阳性有剩余样品时按 eBAM Ch.10 计数（常规 composite、CORE/死亡相关按单个 sub），但**环境拭子不做计数**——拭子的判读维度是阳性点位与数量、WGS 关联和现场条件，不是菌数。实验室确认结果后 24 小时内先通报分部 Compliance Branch 再向企业发 FDA Form 1551；CRO（Cannot Rule Out）结果也须通报。⚠ WGS/GenomeTrakr 是 FDA 实验室动作，不是企业法定义务；企业侧对应义务是〔§ 117.170〕再分析触发与〔§ 117.190(a)〕实施记录。
  tags: [CP 7303.050, WGS, GenomeTrakr, 环境拭子, 不计数, 阳性升级]

- id: t127
  title: ATTACHMENT A Part V.1 三档 Findings 与 Direct Reference Authority
  type: term
  source_chapter: FDA CP 7303.050 ATTACHMENT A Part V.1 Findings / Part V.3.B Compliance Activities；PART V 表 7、表 8
  source_quote: |
    "Consideration for enforcement depends on several factors including the firm’s compliance history, the significance and severity of inspection observations, the prevalence and location of pathogens in the environment, the possible route of contamination, and the adequacy and timeliness of the firm’s corrective actions." / "HFP has not given Direct Reference Authority for any compliance actions related to violations resulting from environmental sampling results at this time." / "The table is not inclusive of all FDA enforcement strategies."
  summary: 环境取样结果的三档：① **无需行动**＝无显著条件且未检出环境病原；② **视厂方响应决定是否行动**＝显著 cGMP/卫生失控，或 Zones 2–3 阳性但无法建立到食品/食品接触面的直接污染路径（此档整改速度与证据权重最大，纠正须在检查结束前验证留证）；③ **预期采取监管行动**＝显著 cGMP/卫生失控、**Zone 1 阳性**、或 Zones 2/3 阳性且观察到直接交叉污染。执法判断逐案看合规史、观察项严重度、病原流行率与位置、污染路径、**整改充分性与及时性**。⚠ HFP **尚未**就环境取样结果授予 Direct Reference Authority，所有行政/法律行动须会签并与州伙伴讨论。PART V 表 7/8 列 voluntary corrective action、召回、warning letter、行政扣留、扣押、禁令、注册暂停、Import Alert / DWPE 等（domestic / foreign 分栏；指控 402(a)(1)/(3)/(4)、801(a)(3)），原文两次声明**非穷尽、逐案判断**，不是「检出 X 必定导致 Y」的对照表。
  tags: [CP 7303.050, Zone 1, 三档 Findings, Direct Reference Authority, 逐案判断, 非穷尽]

- id: t128
  title: IOM 483 措辞纪律与 Category 3 non-reportable observation（效力分层的制度性反证）
  type: term
  source_chapter: FDA IOM 2026 Chapter 5, §§ 5.5.10、5.5.10.7、5.5.11、5.5.11.3
  source_quote: |
    "However, do not quote regulations or incorporate standards (e.g.ISO 13485:2016) when reporting your observations." / "Do not cite deviations from policy or guidance documents on the FDA 483, FDA 483a, or FDA 4056." / "However, do not report opinions, conclusions, or characterize conditions as "violative." The determination of whether any condition is “violative” is an agency decision made after considering all circumstances, facts, and evidence." / "Observations, based on your judgement, that deviate from official published guidance, but do not deviate from regulations, and warrant discussion with management."
  summary: FDA 483 只写**事实性、显著**的观察项（clear / specific / significant / 不重复 / 按显著性排序），用 Who/What/When/Where/Why/How Much/How Often 写清并给总体比例（如 `Two out of 50 records examined`）、以 `So What?` 自验；**不引法规原文、不纳入标准、不引 policy/guidance 偏离、不写 opinions 或 violative**——是否违法是 FDA 事后综合全部事实证据的 agency decision。IOM 5.5.11.3 把 non-reportable observations 分三类，其中 **Category 3＝仅偏离官方 guidance 而未违反法规**，只能口头讨论并写入 EIR 的 `General Discussion with Management`，且 eNSpect 无对应 cite。这从检查员侧制度性印证本包分层：**Guidance / SECG / Handbook / CPGM / CP 7303.050 都不是可直接开观察项的法定义务**；⚠ 但不得反过来读成「指南可以不做」——同一事实若同时构成〔§ 117.xxx〕失守（如 adequate、〔§ 117.110(a)〕），仍会被写成事实性观察项。
  tags: [IOM 2026 Ch.5, FDA 483, 措辞纪律, non-reportable observation, 效力分层, 高频误读]

- id: t129
  title: FDA 检查表单地图（482 / 482c / 482d / 483 / 483a / 4056 / 484）
  type: term
  source_chapter: FDA IOM 2026 Chapter 5, §§ 5.1.4.2.1、5.5.1、5.5.10、5.5.12.5、5.8.1.3；Exhibit 5-1/5-5/5-10/5-17/5-18
  source_quote: |
    "After showing your credentials, issue the original, properly executed, and signed FDA 482, Notice of Inspection, to the most responsible individual at the firm." / "A Notice of Inspection is not required to be issued during foreign inspections (refer to 5.5.8); however, credentials should still be presented to the most responsible individual at the firm." / "You must issue a Form 484, Receipt for Samples, if you collect any physical sample during an inspection."
  summary: 发给 **owner / operator / agent-in-charge（OOAC）**，且 IOM 5.8.1.3 要求用 OOAC 与企业的**法定名称**（不得用 alias / DBA）：**FDA 482** Notice of Inspection＝国内到场、检查开始前（纸质签名或电子签名 PDF 须确认送达；团队检查所有成员签字）；**境外一般不发 482**（除非美国军方设施）但仍须出示证件；**482d**＝FSVP 记录索取；**482c**＝检查前索取记录（Exhibit 5-10）；**FDA 483**＝检查结束、离厂前的收尾会签发**已签署**版本（IOM 5.5.10.3 禁止展示未签署草稿）；**483a**＝FSVP Observations；**4056**＝Produce Farm Inspection Observations；**FDA 484** Receipt for Samples＝采集**任何实体样品**时必发，一般在检查结束时签发（提前签发视为结束检查，须另发 482 才能继续）。另：证件可查看并记录姓名/号码但**不得复印、不得按指纹**（18 U.S.C. 701）。
  tags: [IOM 2026 Ch.5, FDA 482, FDA 483, FDA 484, OOAC, 表单地图, 境外检查]

- id: t130
  title: IOM 5.2.7 预告三层口径（食品企业一般不预告、境外通常提前告知、预告不是预约）
  type: term
  source_chapter: FDA IOM 2026 Chapter 5, §§ 5.2.7、5.2.7.1、5.2.7.2；§§ 5.1.4.2.1、5.5.8
  source_quote: |
    "Pre-announcements are mandatory for all medical device surveillance inspections—and some Bioresearch Monitoring (BIMO) inspections—in accordance with the criteria and instructions below. Routine produce farm inspections should be pre-announced, unless otherwise directed." / "In general, though, it may be inappropriate to pre-announce inspections of food establishments, blood banks, source plasma establishments, and some BIMO inspections, but this is subject to program division discretion." / "In general, the Agency usually announces foreign inspections in advance, partly due to logistics such as arranging travel and access to facilities, securing visas, and partly because of the high costs of conducting foreign inspections." / "The pre-announcement of domestic inspections should generally be no less than five calendar days in advance of the inspection." / "ORA's primary purpose for pre-announcing is to ensure that the appropriate records and personnel will be available so that we may execute an effective inspection. It is _not_ to make an appointment for the inspection."
  summary: 三层必须一起读：① 医疗器械 surveillance 与部分 BIMO **强制预告**，常规 produce farm 检查应预告；② **食品企业检查** `may be inappropriate to pre-announce`，由 program division 裁量；③ **境外检查通常提前告知**（签证、差旅、成本）。国内预告一般**不少于 5 个日历日**，改期由 investigator/team 决定且新日期不得晚于原日期 +5 天，企业要求时可早于 5 天；预告目的是确保**人员与记录在场**，不是预约，不得称 `appointment to inspect`；届时人员/记录不到位会被记入 EIR。⚠ 此前 inspection-readiness 卡把「2025 扩大境外无预告检查」记为政策层、原文未收——补入 IOM 后须区分：**「通常提前告知」是常态，「无预告」是政策变化**，两者不是同一件事；不得写成「FDA 从不预告」或「境外一律无预告」。
  tags: [IOM 2026 Ch.5, Pre-Announcement, 5 个日历日, 境外检查, 无预告检查, 高频误读]

- id: t131
  title: 拒绝检查的边界（301(e)/(f)、非法定信息与 FD&C Act 807(b)）
  type: term
  source_chapter: FDA IOM 2026 Chapter 5, §§ 5.5.2、5.5.2.1、5.5.2.3、5.5.3；FD&C Act 301(e)/(f)、704、807(b) [21 U.S.C. 384c(b)]
  source_quote: |
    "A refusal of inspection is refusal to permit entry or other action that prohibits you from obtaining records and information to which the FDA is entitled under the law." / "It is not an inspection "refusal" when management refuses to provide information (for example, formulations, lists of shipments and manufacturing codes, etc.) not specifically required by law or regulation." / "For international food inspections, section 807(b) of the FD&C Act (21 U.S.C. 384c(b)), authorizes the FDA to refuse admission of a food ..."
  summary: 拒绝**入场**援引 `301(f)` + `704`；拒绝提供或复制**依法有权取得**的记录援引 `301(e)`；检查员须能证明检查在 reasonable time / manner / limits 内进行、已出示证件并（国内）签发 482（CPG Sec. 130.100 口径，正文未收）。⚠ **拒绝提供法规未强制要求的信息**（IOM 明确举例配方、发货清单、生产编码）**不构成 inspection refusal**；企业可依 IOM 5.1.5 提出商业秘密保护诉求。但〔§ 117.320〕要求法定记录口头/书面请求即 promptly 提供并可供复制、〔§ 117.315(c)〕FSP 必须在现场，不能拿「保密」一刀切拒绝。**境外食品检查**拒绝的后果更重：FD&C Act **807(b)** 授权 FDA 对该外国工厂的食品拒绝入境，并可能 Import Alert、注销食品设施注册；IOM 5.5.2.1 要求以 Operation 15 – Foreign Investigation 备忘录上报，不得记为 Washout。⚠ 药品/器械的 `501(j)`「拒绝即掺假」规则**不得套到食品**。
  tags: [IOM 2026 Ch.5, 拒绝检查, 301(e), 301(f), 807(b), 商业秘密, 境外检查]

- id: t132
  title: 样品合格不阻碍 cGMP 指控，以及记录/电子记录/照片的证据固定
  type: term
  source_chapter: FDA IOM 2026 Chapter 5, §§ 5.6.4、5.6.5.1、5.6.6.1、5.6.7；§§ 5.5.12.1、5.5.12.3
  source_quote: |
    "Lack of a violative physical sample is not a bar to pursuing regulatory and/or administrative action providing the cGMP deficiencies have been well documented. Likewise, physical samples found in compliance are not a bar to pursuing action under cGMP charges." / "Do not remove the firm's only copy of records. If duplicates are not available, whenever possible, scan, photograph, or photocopy." / "Of note: Do not personally access a firm’s system to review electronic records, databases, or source data during the course of an inspection" / "Photos taken during inspections are not investigational samples. They are exhibits. Only use FDA-issued equipment, such as a government-issued camera, to take photographs"
  summary: ① **没有阳性实体样**不阻碍依充分记录的 cGMP 缺陷采取监管/行政行动，**样品合格也不阻碍 cGMP 指控**——cGMP 是〔§ 117.3〕`adequate` 的观察型结果义务，与检测结果无关。② 记录作 exhibit：**不得取走企业唯一副本**，应扫描/拍照/复印并核对可读性、保全证据链、不得通过外部邮件接收 exhibit（远程 FSVP 例外）。③ 电子记录：**检查员不得亲自登录企业系统**，应由企业人员操作、检查员旁视提问（仅 BIMO 5.14.2.1 与生物制品 5.13.2.5.1 例外）。④ 检查照片是 **exhibit 不是样品**，只能用 FDA 配发设备（个人设备可能被保全并进入 discovery）。⑤ 检查员至少**每日一次**与管理层沟通可能形成 483 的发现（5.5.12.1），且不得提供咨询建议；**15 个工作日**内的充分 483 回复 `may impact FDA's determination of the need for subsequent action`（5.5.12.3）——与 CPGM 7303.040 PART III.1 双出处，均非法定时限。
  tags: [IOM 2026 Ch.5, 证据链, 样品合格, cGMP 指控, 电子记录, FDA 484, 15 business days]

- id: t133
  title: 九类不可混引与 IOM 收录范围（v4.5 引用纪律）
  type: term
  source_chapter: 全包引用规范；source-cp-7303-050-2025.md / source-iom-ch5-2026.md 文件头
  source_quote: |
    "Do not cite deviations from policy or guidance documents on the FDA 483, FDA 483a, or FDA 4056." —— IOM 5.5.10.7
  summary: v4.5 起全包**九类来源不可混引**：① 21 CFR Part 117 法规正文〔§ 117.xxx〕；② FDA PCHF 行业指南（Ch/小节号）；③ L.mono RTE 指南（其章节号，Draft 建议层）；④ SECG（SECG 章号）；⑤ 过敏原 Ed.5（问答编号如 C.8 / D.13，FD&C Act 标签解释）；⑥ Food Defect Levels Handbook（「Handbook 章名 + 产品名」，执法裁量参考）；⑦ CPGM 7303.040（「CPGM 7303.040 PART x」，附件带 ATTACHMENT A 前缀）；⑧ **CP 7303.050（「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」，其 ATTACHMENT A Part V 与主文 PART V 同名不同口径）**；⑨ **IOM 2026（「IOM 5.x.x / IOM Exhibit 5-x」，Exhibit 编号与小节号不同层，勿把 Exhibit 5-5 写成 IOM 5.5.5）**。⚠ 本包**只收 IOM 2026 Chapter 5 单章**；IOM Ch.3（3.2 权限）、Ch.4（Sampling / 702(b) / 4.3.6.6 / 4.6 / 4.7）、Ch.6（Imports / 6.4 / 6.8.1.4）、Ch.7、Ch.8、Ch.9、Ch.10，以及 RPM、CPG 全套、Import Alerts、eBAM/AOAC/MPM 方法正文、SOP-001052、FMD-147 均未收；遇 IOM 正文的跨章引用只标「转引未收」，不得代填。
  tags: [引用规范, 九类不可混引, IOM 2026 Ch.5, CP 7303.050, 收录边界, v4.5]

- id: t134
  title: PAC / PAF 与抽样报告系统（FACTS / SERIO / OASIS / CMS）
  type: term
  source_chapter: FDA CP 7303.050 首页 PRODUCT/ASSIGNMENT CODES、PART III.2 Table 4、PART IV.6 Table 6、ATTACHMENT A Part III Table 2
  source_quote: |
    "Report domestic sample collections and all analytical results into the Field Accomplishment and Compliance Tracking System (FACTS). Import sample collections should be reported in the System for Entry Review and Imports Operations (SERIO) and/or the Operational & Administrative System for Import Support (OASIS), as appropriate."
  summary: CP 7303.050 首页列 **FDA PAC**：`03037D` 国内/进口奶酪及奶酪制品微生物样、`03803D` 国内人类食品微生物样、`03819C` 进口人类食品微生物样、`03050B` 国内/进口人类食品污秽样、`03050E` 国内/进口人类食品设施 exhibit 样、`03050N` 国内人类食品环境样；**州合同码** `03S050N`。PART III.2 Table 4 给采集报样的 PAC/PAF 组合（MIC / PAR / VIR / CCD / FDF / FIL / NAR），PART IV.6 Table 6 给分析结果报样的组合（`*NAR` 仅用于 FACTS 未预设的特殊微生物检测）；ATTACHMENT A Table 2 给环境采样工时 PAC。**国内**样品与全部分析结果报 FACTS，**进口**报 SERIO / OASIS，执法建议经 CMS 提交 HFP/OCE 并关联样品；进口另按 IOM Ch.6 6.4 与 RPM Ch.9 的 Import Alerts / Import Bulletins 处理（正文未收），与被抽行 same or similar 的 entry lines 须转 compliance branch 待结果，一般不再抽已在 DWPE 清单上的产品（除非另有分析物关切）。⚠ PAC/PAF 是 FDA 内部作业码，不是企业要填的合规编号，也不是检查类型码（后者见 CPGM 7303.040 的 03040 系列）。
  tags: [CP 7303.050, PAC, PAF, FACTS, SERIO, OASIS, CMS, 进口抽样, 内部作业码]

"""

CASES = [
    {
        "id": "sampling-01",
        "type": "should_trigger",
        "prompt": "FDA 检查员今天来我们 RTE 沙拉厂取样，说要抽 Salmonella 和 L. monocytogenes，我们要准备多少个 subs、每份多少克？702(b) 那份能不能也给我们留一份？",
        "expected_behavior": "应激活 inspection-sampling 卡：先说明 CP 7303.050 是抽样 program 且 Inspections are not planned under this compliance program（抽样发生在 7303.040 等检查中），并看 Collection Report 的 PAC。产品样品量按 Table 2 / Table 3：Salmonella 多为 30 subs × 100 g、L. mono 10 subs × 200 g；多分析物按最大 subs 数取足且每 sub 同时满足两者用量。明确 The sample size does not include 702(b) portions，且易腐产品与进口状态样品不取 702(b) 部分（21 CFR 2.10(b)(3)）；702(b) 分割留样细则在 IOM Chapter 4，本包未收，只能给出索取 Form FDA 484 并做内部平行留样的准备原则。必须强调这些 subs 数是 FDA 检查员取证量，不是企业批放行抽样标准",
        "notes": "v4.5 第八来源：样品量 / 702(b) / 取证量非放行标准"
    },
    {
        "id": "sampling-02",
        "type": "edge_case",
        "prompt": "FDA 在我们厂做了环境擦拭，Zone 1 检出 L. monocytogenes，但同期成品抽检全部阴性，是不是就不用整改了？另外让实验室数一下拭子的 CFU 看严不严重。",
        "expected_behavior": "应分三层纠正。① 样品合格不构成安全港：IOM 5.6.4 原文 physical samples found in compliance are not a bar to pursuing action under cGMP charges；cGMP 是〔§ 117.3〕adequate 的观察型结果义务，与检测结果无关。② 升级：CP 7303.050 ATTACHMENT A Part V.1 把 Zone 1 阳性列入 Level at which regulatory action is expected；所有确认的 L. mono / Salmonella 阳性须 WGS 并上传 GenomeTrakr，且 Zone 1/2/3 的环境分离株须联系 HFP/OCE 请求与同厂历史株及 CDC 临床株比对；HFP 尚未授予环境取样相关的 Direct Reference Authority，所有行动须会签、逐案看合规史与整改及时性。③ 环境拭子不计数：ATTACHMENT A Part IV.3.A 明写 No enumeration will be performed on environmental swab/sponge samples；产品 L. mono 阳性才按 eBAM Ch.10 计数（常规 composite、CORE/死亡相关按单个 sub）。应联动 environmental-pathogen-sanitation 卡的阳性升级决策树与〔§ 117.170〕再分析触发",
        "notes": "v4.5 第八/第九来源：Zone 1 阳性 + 样品合格不阻碍 cGMP + 拭子不计数"
    },
    {
        "id": "sampling-03",
        "type": "edge_case",
        "prompt": "我手上这份文件名叫 20250915_7303.050，是不是 2025 年新版的抽样检查计划？里面 PART V 表 7 写了检出 Salmonella 就会 seizure 和注册暂停，我们是不是一检出就要停厂？",
        "expected_behavior": "应做版本判定与效力分层两处纠错。① PDF 首页是 Date of Issuance 06/03/2022、IMPLEMENTATION DATE 06/03/2022、Correction date 09/10/2025（62 页），即 2022 版程序的 2025 年更正本，不是 2025 新签发 program；不得套用 CPGM 7303.040 的 2025-CPM-HFP-001 Transmittal 格式。且 CP 7303.050 是抽样 program 不是检查 program。② PART V 表 7/8 的 Possible FDA Response 是给分部的、逐案且非穷尽的建议清单（原文 The table is not inclusive of all FDA enforcement strategies / This list is not meant to be all encompassing），判断因素含合规史、观察项严重度、病原位置与污染路径、整改充分性与及时性；不是法定后果表，不能推出『一检出即停厂』。合规结论仍回〔§ 117.xxx〕与 FD&C Act 402(a)(1)/(4)、801(a)(3)。应提示 CPG Sec. 527.300 / RPM Ch.9 / Import Alerts 正文未收",
        "notes": "v4.5 第八来源：版本陷阱 + 7303.050 非检查 program + PART V 表非穷尽"
    },
    {
        "id": "iom-01",
        "type": "should_trigger",
        "prompt": "收到的 FDA 483 上写『未遵循 FDA 行业指南的建议』，还直接引了 21 CFR 117 的条款并说这条 violative。我们能不能据此主张整条观察项无效？另外我们只是没按 SECG 做，会不会被开 483？",
        "expected_behavior": "应激活 investigator-authority-procedure 卡并分层回答。① IOM 5.5.10 明令 do not quote regulations or incorporate standards when reporting your observations，5.5.10.7 明令 Do not cite deviations from policy or guidance documents on the FDA 483，5.5.11 明令 do not report opinions, conclusions, or characterize conditions as violative（是否违法是 agency 事后决定）；483 只写事实性、显著观察项并用 Who/What/When/Where/Why/How Much/How Often 与 So What? 自验。可在收尾会或书面回复中请求澄清其对应的法规事实，但不得据此主张整条观察项自动无效——同一事实若同时构成〔§ 117.xxx〕失守仍是观察项。② 只偏离官方 guidance（含 SECG）而未违反法规的，属 IOM 5.5.11.3 Category 3 non-reportable observation，不得写进 483，只能口头讨论并进入 EIR 的 General Discussion with Management；这从检查员侧印证全包效力分层。⚠ 但不得读成『指南可以不做』：adequate〔§ 117.3〕、〔§ 117.110(a)〕等法规结果义务仍须履行",
        "notes": "v4.5 第九来源：483 措辞纪律 + non-reportable observation + 效力分层反证"
    },
    {
        "id": "iom-02",
        "type": "edge_case",
        "prompt": "FDA 从来不预告检查吧？境外工厂应该都是突击检查、也不发 482。这次提前 5 天通知我们，能不能跟检查员约个更方便的时间？",
        "expected_behavior": "应逐条纠偏并引 IOM 5.2.7 / 5.1.4.2.1 / 5.5.8。① 预告不是一律：医疗器械 surveillance 与部分 BIMO 强制预告、常规 produce farm 检查应预告、食品企业检查 it may be inappropriate to pre-announce（由 program division 裁量）、而 the Agency usually announces foreign inspections in advance（签证与成本原因）。2025 扩大境外无预告检查属政策层且 FDA 公告原文未收，‘通常提前告知’是常态，两者不是同一件事。② 国内预告一般不少于 5 个日历日，改期由 investigator/team 决定且新日期不得晚于原日期 +5 天；ORA's primary purpose ... It is not to make an appointment for the inspection，不得称 appointment to inspect；企业该做的是确保人员与记录在场。③ 境外一般不签发 FDA 482（5.1.4.2.1 / 5.5.8，除非美国军方设施），但仍须出示 credentials；不能拿『没收到 482』当拒绝理由",
        "notes": "v4.5 第九来源：预告三层口径 + 5 个日历日 + 境外 482"
    },
    {
        "id": "iom-03",
        "type": "edge_case",
        "prompt": "检查员要我们的配方和发货清单，还说想直接登录 MES 查电子记录、把唯一一份原始记录带走；我们拒绝了算不算拒绝检查？另外取了样只给了一张 484，这是什么？",
        "expected_behavior": "应分四层回答。① IOM 5.5.2.3 明写 It is not an inspection 'refusal' when management refuses to provide information (for example, formulations, lists of shipments and manufacturing codes, etc.) not specifically required by law or regulation——拒绝非法定信息不构成 refusal；但〔§ 117.320〕法定记录口头/书面请求即须 promptly 提供并可供复制、〔§ 117.315(c)〕FSP 必须在现场，不能一刀切拒绝，商业秘密按 IOM 5.1.5 提出保护诉求。② 电子记录：IOM 5.6.6.1 Do not personally access a firm's system，应由企业人员操作、检查员旁视提问（仅 BIMO / 生物制品例外）。③ IOM 5.6.5.1 Do not remove the firm's only copy of records，应扫描/拍照/复印并保全证据链、核对可读性。④ FDA 484 = Receipt for Samples，IOM 5.5.12.5 规定采集任何实体样品必发、一般在检查结束时签发（提前签发视为结束检查须另发 482）；它不是放行依据，702(b) 分割留样规则在 IOM Ch.4 未收。境外拒绝检查另提示 FD&C Act 807(b) 拒绝入境风险",
        "notes": "v4.5 第九来源：拒绝边界 + 电子记录/唯一副本 + FDA 484 + 807(b)"
    },
    {
        "id": "iom-04",
        "type": "should_trigger",
        "prompt": "FDA 483 回复的 15 个工作日到底是哪里规定的？CPGM 里有，IOM 里有没有？482、483、484、4056 分别什么时候给谁？",
        "expected_behavior": "应给出双出处与表单地图。① 15 个工作日：CPGM 7303.040 PART III.1 写 FDA expects to receive a facility's FDA 483 response within 15 business days of the end date of the inspection（境外另有 FDA483responseinternational@fda.hhs.gov）；IOM 5.5.12.3 是通用程序出处——15 个工作日内的充分回复 may impact FDA's determination of the need for subsequent action。两者都是 FDA 期望/程序口径，不是法定时限，不得与〔§ 117.145〕7 个工作日记录审核、豁免撤销 15/90/120 日窗口混算，也不得说逾期即违法。② 表单：482 国内到场检查前发 OOAC（境外一般不发）、482d FSVP 记录索取、482c 检查前索取记录、483 收尾会签发已签署版本（不得展示草稿）、483a FSVP、4056 农场、484 取任何实体样必发且一般在结束时；须用 OOAC 与企业法定名称。③ 引用分别用「CPGM 7303.040 PART x」与「IOM 5.x.x」，全包九类不可混引",
        "notes": "v4.5 第九来源：15 工作日双出处 + 表单地图"
    },
    {
        "id": "iom-05",
        "type": "edge_case",
        "prompt": "检查员拿自己的手机拍了车间，我们能不能要求删掉？另外 IOM 里提到的 Chapter 4 取样细则、702(b) 和 RPM Chapter 10-4 记录索取权，帮我们按条款解释一下。",
        "expected_behavior": "应分两半。① IOM 5.6.7：照片是 exhibit 不是样品，只能用 FDA 配发设备（Only use FDA-issued equipment），个人设备可能因后续诉讼被保全并进入 discovery；企业不宜自行抢拍或要求删除，但可在陪同记录里注明设备、时间、点位并同步留存自己的对照照片。可补充 IOM 5.6.4 样品合格不阻碍 cGMP 指控、5.5.12.1 至少每日一次管理层沟通。② 明确收录边界：本包只收 IOM 2026 Chapter 5 单章；IOM Chapter 4（Sampling、702(b)、4.2.5、4.3.6.6、4.6、4.7）、IOM Ch.3/6/7/8/9/10、RPM Chapter 10-4（FD&C Act 414(a) / 704(a) 的记录索取权）、CPG Sec. 130.100 等正文均未收，遇 IOM 正文跨章引用只标『转引未收』，不得凭常识代填或编造条款细节；可给出向具资质合规顾问复核的建议",
        "notes": "v4.5 第九来源：照片证据地位 + IOM 只收 Ch.5 的收录边界"
    },
]


def main():
    # 1) glossary
    text = GLOSS.read_text(encoding="utf-8")
    fence = text.rfind("\n```\n")
    assert fence > 0, "glossary closing fence not found"
    assert "- id: t123" not in text, "already appended"
    text = text[:fence] + "\n" + TERMS + text[fence:]
    text = text.replace(
        "- [x] 第七来源 FDA CPGM 7303.040 现行版（`2025-CPM-HFP-001`）术语 t118–t122 已并入（三层分级、Focused PCHF / 03040U 改义、official review 记录举证、483 回复 15 工作日、Limited Scope 取证边界）；CPGM 原文标「CPGM 7303.040 PART x」，法规标〔§ 117.xxx〕，检查员作业指导不升格为企业义务；2020 版旧口径单列为版本陷阱；全库 122 条",
        "- [x] 第七来源 FDA CPGM 7303.040 现行版（`2025-CPM-HFP-001`）术语 t118–t122 已并入（三层分级、Focused PCHF / 03040U 改义、official review 记录举证、483 回复 15 工作日、Limited Scope 取证边界）；CPGM 原文标「CPGM 7303.040 PART x」，法规标〔§ 117.xxx〕，检查员作业指导不升格为企业义务；2020 版旧口径单列为版本陷阱\n"
        "- [x] 第八来源 FDA CP 7303.050（2022 签发 / 2025-09-10 更正）术语 t123–t127 已并入（版本形态与『非检查 program』、subs 与 702(b)、环境拭子 50/100 与 Zone、WGS/GenomeTrakr 与拭子不计数、三档 Findings 与 Direct Reference）；原文标「CP 7303.050 PART x / ATTACHMENT A Part x / Table x」，subs 数一律注明为 FDA 取证量而非放行标准\n"
        "- [x] 第九来源 FDA IOM 2026 Chapter 5 术语 t128–t133 已并入（483 措辞纪律与 Category 3 non-reportable observation、表单地图、预告三层、拒绝边界与 807(b)、样品合格不阻碍 cGMP 指控与证据固定、九类不可混引与 IOM 收录范围）；原文标「IOM 5.x.x / IOM Exhibit 5-x」，遇跨章引用标『转引未收』；全库 **134 条**",
    )
    GLOSS.write_text(text, encoding="utf-8")
    print("glossary: appended t123–t134 (total 134)")

    # 2) test prompts
    data = json.loads(TESTS.read_text(encoding="utf-8"))
    assert data["version"] == "4.4", data["version"]
    existing = {c["id"] for c in data["test_cases"]}
    for c in CASES:
        assert c["id"] not in existing, c["id"]
    data["version"] = "4.5"
    data["test_cases"].extend(CASES)
    data["notes"] += (
        " | v4.5 追加 8 条用例（3 条 sampling-* + 5 条 iom-*）：CP 7303.050 样品量与 702(b)、Zone 1 阳性与样品合格不阻碍 cGMP、2025 文件名版本陷阱与 PART V 表非穷尽、"
        "IOM 483 措辞纪律与 non-reportable observation、预告三层与境外 482、拒绝边界与电子记录/484/807(b)、15 工作日双出处与表单地图、照片证据地位与 IOM 只收 Ch.5；"
        "新增第 17 张卡 inspection-sampling（第八来源 CP 7303.050，2022 签发 / 2025-09-10 更正）与第 18 张卡 investigator-authority-procedure（第九来源 IOM 2026 Chapter 5），全包九类不可混引。"
    )
    TESTS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"test-prompts: v4.5, {len(data['test_cases'])} cases")


if __name__ == "__main__":
    main()
