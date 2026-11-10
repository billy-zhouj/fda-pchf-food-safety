"""apply_v4_16_docs.py — v4.16 文档层回补（术语 / 概览 / 用例 / 状态）

四件事：
1. candidates/glossary.md：补 t224–t233 共 10 条术语，并追加自检记录一行。
2. BOOK_OVERVIEW.md：追加 v4.16 版本补充说明节（历史阶梯保留不改），
   并把五处「当前态」的 IOM Ch.4 未收断言改为「自 v4.16 起已收」。
3. test-prompts.json：追加 10 条 iom-sampling-* 用例、version 4.15.1 → 4.16、
   并追加 notes 尾注（json round-trip 已验证字节无损：indent=2 / ensure_ascii=False）。
4. DIGEST.md / PIPELINE_STATE.md：只改顶部「当前状态」行并追加 v4.16 说明节；
   v4.x 历史段落一律不动。编译/安装实测数字留占位，待 #83 完成后回填。

支持 --apply 才写盘；默认 dry-run。
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

GLOSSARY_TERMS = """
- id: t224
  title: official sample（21 CFR 2.10 的三种管辖情形）
  type: term
  source_chapter: IOM 4.1.4 / 4.1.4.1；21 CFR 2.10
  source_quote: |
    "A sample is an _official sample_ if records (see IOM 4.4.4) or other evidence obtained show that the shipment, or other lot of the article from which the sample was collected, was: Introduced or delivered for introduction in interstate commerce, or Was in or was received in interstate commerce, or Was manufactured in a Territory or the District of Columbia."
  summary: FDA 取样的**效力起点**。三条件任一成立且有记录或证据支持，样品才是 official sample，可作为扣留/禁令/起诉的执法基础；进口样品一律是 official sample。另有四要件使样品 `valid`：随附确立联邦管辖与知情人身份的记录、代表所采之批、够实验室分析并在必要时留 702(b)、以维持证据完整性的方式标识封存并有清晰监管链。⚠ **official sample 分 physical 与 documentary（DOC）两类**，不是「只有实物才算」；INV / survey / non-regulatory 三类都不是 official sample。本包自 v4.16 起有原文（CAP-28）。
  tags: [取样程序, 法定管辖, IOM Ch.4, 二十类来源]

- id: t225
  title: DOC sample（documentary official sample）
  type: term
  source_chapter: IOM 4.1.4.1.1
  source_quote: |
    "A DOC sample is not a sample of records. It is a sample representing a lot of a regulated article"
    "Because no product is collected, a Form FDA 484, Receipt for Samples, is not issued for DOC samples."
  summary: 最易误读的样品类别。DOC **不是「记录复印件」**，而是「以记录代表一个批的 official sample」——记录本身就是样品本体，仍须代表可确立联邦管辖的批、仍须有 C/R。由标签/随附标识/州际运输记录/支持性证据构成。**两条硬例外**：`DOC samples are not officially sealed`（不贴 FDA 415a）、**不发 Form FDA 484**；但照片的电子介质另按 IOM 5.6.7.5 封。适用情形见 4.1.4.1.2（超大/固定安装/过贵/已不存在/无需化验/应急留用/拟按标签违法扣留）。⚠ 不要把「没贴封条、没开 484」读成「这次取样不算数」。
  tags: [取样程序, 样品类别, IOM Ch.4, 反直觉]

- id: t226
  title: INV / survey / non-regulatory sample（三类非 official sample）
  type: term
  source_chapter: IOM 4.1.5 / 4.1.6 / 4.1.7 / 4.3.6.6.2
  source_quote: |
    "Investigational (INV) samples are _not_ official samples."
    "Because these samples can be used as evidence in court, they must be sealed, and their integrity and chain of custody protected."
    "Survey samples are not official samples."
  summary: **INV（investigational）**：记录观察、支持监管行动，不需州际商业或联邦管辖；但**能进法庭，所以必须封条与完整证据链**。环境拭子、土壤、水、动物粪便、in-line/factory food、污秽 exhibit、部分投诉样一律按 **INV** 编号（产品码 `52Y[][]08` 等，不得用受检产品码）。**survey**：主动监督取数，只做数据、不作执法基础（如 DQST）。**non-regulatory**：替其他联邦/州/地方机构代做、FDA 对产品无管辖权。⚠ 把 INV 读成「非正式样品，随便采采」是本件最危险的误读。
  tags: [取样程序, 样品类别, IOM Ch.4, 证据链]

- id: t227
  title: 702(b) portion 与七项豁免（含污秽样品反向例外）
  type: term
  source_chapter: IOM 4.3.2.2 / 4.3.2.3 / 4.7.4；FD&C Act 702(b) [21 U.S.C. 372(b)]
  source_quote: |
    "FDA must, “upon request, provide a part of such official sample for examination or analysis by any person named on the label of the article, or the owner thereof, or his attorney or agent.”"
    "Note regarding filth samples: Regardless of the exemptions under 21 CFR 2.10(b) listed above, collect the 702(b) portion for filth samples, unless your supervisor directs otherwise."
  summary: 法定**分割留样请求权**（`upon request`，不是自动给付）。默认留样量 `at least twice the quantity estimated to be sufficient for analysis`（含实验室 reserve），双份子样须来自同一袋/箱/容器，并建议独立容器独立封条。**七项豁免**：① 器械与烟草不在法定范围；② 可采量不足分析量两倍（有多少采多少）；③ 两倍量成本超 $150；④ 无法以可行保存手段维持可分析状态（**明列 fresh produce / water samples / environmental swabs**）；⑤ 进口样品；⑥ 取自标签具名且为货主本人；⑦ 无标签或标签无具名者。⚠ **污秽样品是唯一反向例外**：无论豁免与否都要留。不留须在 C/R 的 Collection Remarks 写明理由。
  tags: [取样程序, 702(b), IOM Ch.4, 反直觉]

- id: t228
  title: Zone Concept 1–4 与检查员环境取样子样数
  type: term
  source_chapter: IOM 4.3.6.6.1；Exhibit 4-20 / 4-21
  source_quote: |
    "For Salmonella environmental swabbing, collect at least 100 swabs/subs and ideally 300 or more subs."
    "For Listeria environmental swabbing, collect at least 50 swabs/subs and ideally 100 or more subs."
  summary: **Zone 1** 直接接触面（切片机、混合机、输送带、器具、工作台）；**Zone 2** 紧邻 Zone 1（设备外表面、框架、推车、齿轮、通风、地面）；**Zone 3** 紧邻 Zone 2（走廊、门口、墙、电话、叉车）；**Zone 4** 远端（更衣室、干货/成品库、食堂、装卸区）。绝大多数子样取 Zone 1–2、Zone 3 次之、`Very few, if any ... from Zone 4`。Salmonella 以 Zone 2–4 为主（干性产品通常不采食品接触面），Listeria 以 Zone 1–2 为主（湿环境必须采接触面）；Listeria 须**生产 ≥4 小时且湿洗前**，Salmonella 宜在湿洗前。⚠ **50/100 是检查员侧最低量，不是企业 EMP 标准**；企业点位与频次依〔§ 117.165(a)(3)〕与自身危害分析。
  tags: [环境取样, Zone, IOM Ch.4, 检查员口径]

- id: t229
  title: 环境取样不得预告 / D-E 中和液 / 24 小时到实验室
  type: term
  source_chapter: IOM 4.3.6.6.1 / 4.3.6.6.2 / 4.7.3.6
  source_quote: |
    "it is preferable during your discussions with a firm not to mention FDA's intent to collect environmental samples until, immediately, before sampling begins"
    "transport/ship the sample to the servicing lab for analysis so it is received by the lab within 24 hours of collection."
  summary: **不得预告**的理由是防止企业临时清洁、抑制微生物回收（这与 IOM 5.2.7 的「检查是否预告」是两个问题，不要读成「检查本身不通知」）。作业要点：**Dey-Engley（D/E）中和肉汤/缓冲液**为通用中和液（中和消毒剂 + 提供运输存活营养）；大面积用海绵/海绵棒，单向 `10 times vertically, then 10 times horizontally`，小面积（约 10 cm × 10 cm）Dacron 拭子再加 `10 times diagonally`；双层袋 + 预冻凝胶冰袋冷藏不冻结，**24 小时内到实验室**；闭控按每个无菌器材批留一份、**环境样不交开控**；冷藏样 ≤4.4 °C（40 °F）。**换手套规则**：Zone 2–4 且属常规监督抽样时同一 zone 内不必逐子换（每子间用 70% 乙醇消毒），**Zone 1 与 for-cause 检查仍须逐子换**。
  tags: [环境取样, 作业约束, IOM Ch.4, 反直觉]

- id: t230
  title: 表单链与 FDA 415a 官方封条的三条硬规则
  type: term
  source_chapter: IOM 4.2.5 / 4.7.4 / 4.7.5.3；Exhibit 4-4 / 4-5 / 4-17
  source_quote: |
    "The receipt is to be issued to the owner, operator, or agent-in-charge, upon completion of the inspection, but prior to leaving the premises."
    "The seal must bear only one signature."
    "Never place more than one sample in the same officially sealed package."
  summary: **按动作对号**：到场检查 → FDA 482；运途中取样 → 给承运人 FDA 482 + **FDA 472 Carriers Receipt**；取任何实体样品 → **FDA 484 Receipt for Samples**（检查结束、离场前签发）；封样 → **FDA 415a Official Seal**（或金属封条）；包装标识 → **FDA 525**；证言 → FDA 463a / 1664 / 1664a / 1664b；州际证据 → FD 1662。**三类不发 482/484**：induced / undercover / online；DOC 另明文不发 484、不贴封条。**封条三硬规则**：只能一个签名（多人时由编制并签署 C/R 者签）、一样一封、702(b) 建议独立容器独立封条；封条可用至厂商有效期后 **5 年**；拆封后须重封并把每一张用过的封条随记录提交。不封条的唯一例外是「连续亲自保管 + 主管与实验室同意 + 当日提交」。
  tags: [取样程序, 表单链, 封条, IOM Ch.4]

- id: t231
  title: 阳性环境结果上 FDA 483 的门槛与 704(d) 四问
  type: term
  source_chapter: IOM 4.3.6.6.5 / 4.6.2.58 / 4.6.2.9
  source_quote: |
    "Significant positive environmental sample results, from swabs collected at food firms, are to be reported on the FDA 483 if the results are known prior to the conclusion/closeout of the inspection."
    "Environmental samples do not meet the criteria of 704(d) but FDA provides the sample results to firms."
  summary: **上 483 的三条件**（foods program 适用）：① 属当前或未来 foods program 检查；② **检查未关账前已知**（原文明确不得为等结果延长检查）；③ 构成显著观察——Listeria 阳性在 **Zone 1/2**，或 Salmonella 阳性在 **Zone 2/3**。**Zone 3（Listeria）与 Zone 4（任一病原）不写**，除非与 Zone 1/2 阳性合并以加强执法。`704(d)` 四问全 yes 才勾（是食品 / 检查期间采 / 取自制造加工包装食品的场所 / 为查明是否含污秽腐败分解物质或不适于食用），且**选择性取样的食品部分要勾、环境样品明确不勾**（结果仍会给企业，由 HFP 发，非 OII 职责）。
  tags: [阳性结果, FDA 483, 704(d), IOM Ch.4]

- id: t232
  title: IOM Sample Schedule Chart 2（LACF / AF 取样计划）
  type: term
  source_chapter: IOM Sample Schedule Chart 2；4.3.6.4
  source_quote: |
    "The sample will consist of all abnormal containers and the number of normal cans specified under “2. Official Samples” below"
    "Sample size does not include 702(b) portion"
  summary: 全包从 v4.6 起反复标「未收」的取样量出处，自 v4.16 起有原文（CAP-28）。**LACF 现场检查**：按批大小对表，达到规定异常罐数即提前终止并取样（3/5/6/7/8/9/10/11 对应八档）；异常罐分 flipper / springer / soft swell / hard swell，**leaker 不计入「abnormal containers」**、只报数不采。**official sample = 全部异常罐 + 规定正常罐**（正常罐数已含 702(b)）；**investigational / import = 全部异常 + 12 正常罐**。污秽/微生物取样：≤795 g（28 oz）≤50 箱取 48 罐、>50 箱取 96 罐；>795 g ≤600 箱取 48 罐、>600 箱取 72 罐。**AF 的 pH 取样**：>795 g 取 12 罐（12 箱各 1）、≤795 g 取 24 罐（12 箱各 2），**且明确不含 702(b)**，异常罐另加至多 24 罐。⚠ 这是**取样计划**，与 CP 7303.070 PART IV.2 的 4.40/4.65/4.75 **实验室触发线**属两层，不得混写成一条数。转换件的四组列在 GFM 后错列，只引「批大小 → 检查数 → 提前终止数」对应关系。
  tags: [取样量, LACF, Chart 2, IOM Ch.4, 两层不得混引]

- id: t233
  title: 六套取样数量的分层与 IOM Ch.4 转换件引用纪律
  type: term
  source_chapter: CAP-28 E-Step 7 / B10 / B12；IOM 4.3.2 / 4.3.6.2
  source_quote: |
    "To determine sample size, first consult your assignment. If the assignment doesn't specify the sample size, follow the guidance in the applicable Compliance Program. The IOM SAMPLE SCHEDULE ... should be used if the Compliance Program doesn't state the sample size."
  summary: 取样量三级优先 **assignment → 适用 Compliance Program → IOM Sample Schedule**；三级都无才用通用规则（箱数平方根、12–36 子样、不足 12 全取、带 702(b) 时双份）。**六套数字互不替代**：① 50/100 环境子样数（IOM 4.3.6.6.1）；② 114 g / 4 oz 与 10 个零售容器（IOM 4.3.6.6.3/4）；③ Chart 2 的 48/96/72 罐（LACF 取样计划）；④ AF 的 12/24 罐（pH 取样，不含 702(b)）；⑤ CP 7303.050 Table 2/3（CAP-17）；⑥ 4.40/4.65/4.75 与 24 罐/12 罐（CP 7303.070 PART IV.2 实验室触发线，CAP-19）。**转换件四处红线**：文件前部 Word 点线目录块与 `picture intentionally omitted` 占位不可逐字引；书签错位（4.7.2 在 4.7.1 之前、4.6.4 混入 4.7 区）故检索以 `4.x.x` 小节号为准；`## **Dry Ice Guidance**` 等为伪标题；Chart 2 表格错列须回查 PDF。引用写「IOM 4.x.x / IOM Exhibit 4-xx / IOM Sample Schedule Chart x」，**不得写成〔§ 117.xxx〕**。
  tags: [引用规范, 分层, IOM Ch.4, 二十类来源]

"""

# v4.15 踩过的 YAML 坑：标量以 `**` 开头会被 PyYAML 当成别名（ScannerError）。
# 去掉行首那对粗体标记，内容逐字保留其余部分。
TERMS_SAFE = re.sub(r"^(  summary: )\*\*([^*\n]+)\*\*", r"\1\2", GLOSSARY_TERMS, flags=re.M)
assert not any(ln.startswith("  summary: **") for ln in TERMS_SAFE.split("\n"))
assert TERMS_SAFE.count("- id: t2") == 10

CHECKLINE = "- [x] 第二十来源 **FDA IOM 2026 Chapter 4《Sampling》**（189 页 / 361 书签 / 4.2 MB）检查程序已并入，术语 t224–t233 共 10 条，围绕「取样作为证据的形式要件」排布：21 CFR 2.10 的 official sample 三条件 → DOC 的两条反直觉 → INV/survey/non-regulatory 三类 → 702(b) 七项豁免与污秽反向例外 → Zone 1–4 与 50/100 → 不得预告与 D/E、24 小时 → 表单链与 FDA 415a 三硬规则 → 阳性上 483 的三条件与 704(d) 四问 → Sample Schedule Chart 2 → 六套数量分层与转换件引用纪律。引文取自 CAP-28 R 段经 `.cangjie/verify_v4_16_quotes.py` 核验的 **60 个英文引用块**（60/60 命中正文区，0 超 100 词、0 表格引用；`body_only()` 排除自写文件头以防自我验证循环）。原文标「IOM 4.x.x / IOM Exhibit 4-xx / IOM Sample Schedule Chart x」，企业义务标〔§ 117.xxx〕等法规正文；⚠ 环境拭子 50/100 是**检查员侧最低量**，不是企业 EMP 标准。**全包自 v4.16 起二十类来源不可混引，28 张能力卡**。全库 **233 条**，v4.16。\n"

OVERVIEW_SECTION = """
## v4.16 追加：第二十来源 FDA IOM 2026 Chapter 4（Sampling）

> 本节是 v4.16 增量记录；上文各节的 v4.x 规模、「十九类不可混引」与各版「仍未收 IOM Ch.4」均为**历史口径**，保留不改。

- **v4.16 规模**：**28 张能力卡 / 233 条术语 / 168 条测试用例 / 二十类来源 / `dist-v20`**。
- **第二十来源**：**FDA《Investigations Operations Manual 2026, Chapter 4 — Sampling》**（189 页 / 361 书签 / 4.2 MB，PDF creationDate `2026-07-14`），`source-iom-ch4-2026.md`。属**检查程序作业层**：给调查员（Investigator / CSO）的内部作业手册，非法规、非 Guidance for Industry、**不创设企业义务**。这是全包自 v4.5 起在 CAP-17 / CAP-18 / CAP-19 / CAP-20 / CAP-25 / CAP-24 / 术语表与状态文档里反复标注「未收」的最后一块检查程序层空白。
- **转换与自检**：经用户级技能 `pdf2md-pro`（pymupdf4llm）转换；**361 书签全命中、0 丢弃**，405 个标题（H1 1 / H2 89 / H3 68 / H4 169 / H5 78）、345 行表格、页眉 `CHAPTER 4` 与独立页码残留 0、自动检出噪声行 2。文件头补「来源 / 效力层级 / 关键口径 / 转换局限」说明块（对齐 Ch.5 的写法）。CAP-28 R 段 **60 个英文引用块经 `.cangjie/verify_v4_16_quotes.py` 逐字核验 60/60 命中**，`body_only()` 只取 Word 点线目录起点之后的正文、排除自写文件头，避免自我验证循环。
- **新增能力卡 CAP-28 `iom-sampling-procedure`**：把一次取样拆成六道分流——类别（official physical / official DOC / INV / survey / non-regulatory）→ 数量（assignment → CP → IOM Sample Schedule 三级优先）→ 702(b) → 表单链（482 / 472 / 484 / 415a / 525 / 463a / 1664）→ 封存与运输 → 阳性结果与 483。
- **六类实质纠偏**：① **DOC sample 仍是 official sample**，只是不贴封条、不发 FDA 484——「没开 484」不能读成「样品不算数」；② **INV 不是「非正式样品」**，原文 `can be used as evidence in court, they must be sealed`；③ **`702(b)` 七项豁免不是封闭清单**，污秽样品是唯一「无论豁免与否仍要留」的反向例外，而环境拭子因被明文列入「无法以可行手段保存」通常不留；④ **环境取样不得预告**（防临时清洁抑制回收），且 50/100、Zone 1–4、24 小时到实验室全部是**检查员侧**口径，不是企业 EMP 标准；⑤ **阳性环境结果上 483 有双门槛**（关账前已知 + Listeria Zone 1/2 或 Salmonella Zone 2/3；Zone 3/4 不写），且**环境样品明确不勾 704(d)**；⑥ **`Sample Schedule Chart 2` 终于有原文**，但它是**取样计划**，与 CP 7303.070 PART IV.2 的 4.40 / 4.65 / 4.75 实验室触发线仍属两层。
- **Bundle 回补**：`assemble_bundle.py` 27 → **28 卡**（SLUGS 追加、ALSO_READ 新增 12 条正向链 + 13 张卡反向链）、`additional_sources` 18 → **19 条**（末条 `src-fda-iom-ch4-2026`）、core_principles 54 → **56**、stop_conditions 28 → **30**、entry.description 增加 IOM Ch.4 段落。全包当前口径统一为「**二十类不可混引 / 28 张卡**」，并清除各卡把 IOM Ch.4 写作「未收」的裸断言。
- **二十类不可混引（v4.16 口径；v4.15 时为十九类）**：在十九类之外增加 **IOM 2026 Chapter 4**。层次仍为：法规正文（六套编号）＞ FDA 指南 ＞ CPGM／CP／IOM 检查程序（仅检查员视角、不创设企业义务）。
- **转换局限（写入 CAP-28 B12）**：① 文件前部（L3–L17）是 Word 点线目录被压成的巨型单行块，非正文，检索以 `4.x.x` 小节号为准；② 书签插入位置错位（`4.7.2` 出现在 `4.7.1` 之前、`4.6.4` 混入 4.7 区），小节标题常以 heading 与 plain text 两种形态各出现一次；③ `## **Dry Ice Guidance**` / `## **PRODUCT**` / `## **CODE**` 等为伪标题；④ Exhibit 4-1…4-25 表单为 `picture intentionally omitted` 占位（全章 41 处），字段名可引、表格式样不可引；⑤ Chart 2 的 48/CASE、24/CASE、12/CASE、6/CASE 四组在 GFM 转换后错列，只可引「批大小 → 检查数 → 提前终止数」对应关系。
- **仍未收**：IOM Chapter 2 / 3 / 6 / 7 / 8 / 9 / 10 全本（尤其 Ch.3 的 3.2 权限、Ch.6 的 6.4 进口取样、Ch.8 的投诉与食源性疾病调查）、SOP-001052 / FMD-147 / OII SOP-000530、RPM 6-3 / 10-4、CPG 580.100 / 300.400 / 130.100 全文、BAM / AOAC / MPM 方法全文、FACTS / eNSpect / CMS / OASIS 内部操作、Form FDA 484 表单栏目细则。制样与显微判读、检验方法检出限仍须另行复核。
"""

# BOOK_OVERVIEW 中三处「当前态」未收断言（历史阶梯段落不动）
OVERVIEW_REWRITES = [
    ("**仍未收（v4.6 当时记录，v4.7 收窄）**：IOM 其余章节（尤其 Ch.4 的 702(b) 分割留样与制样、Sample Schedule Chart 2）",
     "**仍未收（v4.6 当时记录，v4.7 收窄；⚠ Ch.4 自 v4.16 起已收，见文末）**：IOM 其余章节（尤其 Ch.3 的法定权限与 Ch.6 的进口取样）"),
    ("、IOM Ch.4 Sample Schedule Chart 2、CPG 全套、Import Alert 全文、其余 Compliance Programs（7303.842 / 7303.847 / 7303.819 等",
     "（**IOM Ch.4 Sample Schedule Chart 2 自 v4.16 起已收，见文末**）、CPG 全套、Import Alert 全文、其余 Compliance Programs（7303.842 / 7303.847 / 7303.819 等"),
    ("、IOM Ch.4、BAM / CPG 全套。v4.8 **未重跑",
     "（**IOM Ch.4 自 v4.16 起已收，见文末**）、BAM / CPG 全套。v4.8 **未重跑"),
    ("- 历史「仍未收」清单中除 CP 7303.842 外的项目（part 120 / 1240 / 110 / 507、NSSP Guide、CPG 与 Import Alert 全文、BAM 方法、IOM Ch.4 等）**仍然未收**；",
     "- 历史「仍未收」清单中除 CP 7303.842 与 IOM Ch.4 外的项目（part 120 / 1240 / 110 / 507、NSSP Guide、CPG 与 Import Alert 全文、BAM 方法等）**仍然未收**；**IOM Ch.4 自 v4.16 起已收**；"),
    ("- **仍未收**：2541 系列表单栏目细则、FURLS / Center Views 实际操作、21 CFR part 110 / 120 正文、CPG 全套、Import Alert 全文、BAM / AOAC / MPM 方法正文、IOM Ch.4 Sample Schedule Chart 2。",
     "- **仍未收**：2541 系列表单栏目细则、FURLS / Center Views 实际操作、21 CFR part 110 正文、CPG 全套、Import Alert 全文、BAM / AOAC / MPM 方法正文（**IOM Ch.4 Sample Schedule Chart 2 自 v4.16 起已收，见文末**）。"),
]

# 术语表三处当前态未收断言
GLOSSARY_REWRITES = [
    ("702(b) 分割留样细则在 IOM Chapter 4，本包未收。",
     "**702(b) 分割留样细则自 v4.16 起已有原文出处**：IOM Chapter 4 `4.3.2.2 / 4.3.2.3 / 4.7.4`（第二十来源，见 CAP-28 与 t227）。"),
    ("具体抽样计划出处是 **IOM Chapter 4, Sample Schedule Chart 2（正文未收）**。",
     "具体抽样计划出处是 **IOM Chapter 4, Sample Schedule Chart 2（自 v4.16 起已收，见 CAP-28 与 t232）**；⚠ 它是取样计划，与 CP 7303.070 PART IV.2 的 pH 4.40/4.65 实验室触发线属两层。"),
    ("、IOM Ch.4 Chart 2、BAM、CPG、Import Alert 全文、其余 Compliance Programs，一律标「转引未收」。",
     "（**IOM Ch.4 Chart 2 自 v4.16 起已收，见 t232**）、BAM、CPG、Import Alert 全文、其余 Compliance Programs，一律标「转引未收」。"),
    ("    21 CFR part 1 subpart L、IOM Ch.4、FDA 3501 / 3502 表单全文、eNSpect / CMS / FACTS 内部系统。",
     "    21 CFR part 1 subpart L、FDA 3501 / 3502 表单全文、eNSpect / CMS / FACTS 内部系统（IOM Ch.4 自 v4.16 起已收，见 CAP-28）。"),
]

# ── ③ test-prompts.json：10 条 iom-sampling-* 用例 ──────────────────────
NEW_CASES = [
    {
        "id": "iom-sampling-01",
        "type": "should_trigger",
        "prompt": "检查员这次只拿走了标签和随货记录，没开 FDA 484 也没贴官方封条，是不是说明这次根本没取到有效样品、企业可以不管？",
        "expected_behavior": "不能这么推。IOM 4.1.4.1.1 的 **DOC sample（documentary official sample）** 明确 `A DOC sample is not a sample of records. It is a sample representing a lot of a regulated article`——记录本身就是样品本体，仍须代表可确立联邦管辖的批、仍须有 C/R；`Because no product is collected, a Form FDA 484, Receipt for Samples, is not issued for DOC samples` 且 `DOC samples are not officially sealed`。**这两条是 DOC 的硬例外，不是样品无效的证据**：DOC 仍属 official sample（21 CFR 2.10 三条件 + 四要件 valid）。适用情形见 IOM 4.1.4.1.2（超大/固定安装/过贵/已不存在/无需化验/应急留用/拟按标签违法扣留）。照片电子介质另按 IOM 5.6.7.5 封。",
        "notes": "v4.16：DOC 不发 484 / 不贴封条仍是 official sample（头号反直觉）",
    },
    {
        "id": "iom-sampling-02",
        "type": "should_trigger",
        "prompt": "我们车间被取了一批环境拭子，检查员说是 INV 样品、不是官方样品，那是不是就随便采采、企业不用管证据链？",
        "expected_behavior": "恰恰相反。IOM 4.1.5 写 `Investigational (INV) samples are _not_ official samples`，但这只说明**不用于执法定性**，紧接着 `Because these samples can be used as evidence in court, they must be sealed, and their integrity and chain of custody protected`——**能进法庭，所以必须封条与完整监管链**。环境拭子、土壤、水、动物粪便、in-line/factory food、污秽 exhibit、部分投诉样一律按 INV 编号（产品码 `52Y[][]08` 等，不得套用受检产品码）。另区分 `Survey samples are not official samples`（IOM 4.1.6，只做数据不作执法基础）与 non-regulatory（IOM 4.1.7，FDA 无管辖权）。⚠ 不要把 IOM 作业口径写成企业义务。",
        "notes": "v4.16：INV 不是「非正式样品」，须封条与证据链",
    },
    {
        "id": "iom-sampling-03",
        "type": "edge_case",
        "prompt": "702(b) 分割留样是不是每次都要给企业一份？我们这批是环境拭子和污水样，检查员说不用留，是不是违规？",
        "expected_behavior": "两句都要分开答。① 702(b) 是 `upon request` 的**请求权**，不是自动给付；默认留 `at least twice the quantity estimated to be sufficient for analysis`，双份子样须来自同一袋/箱/容器。② IOM 4.3.2.3 / 4.7.4 列**七项法定豁免**，其中「无法以可行保存手段维持可分析状态」明列 `fresh produce / water samples / environmental swabs`，所以环境拭子与水样通常不留，检查员没违规；另含器械与烟草、可采量不足两倍、两倍量成本超 $150、进口样品、取自标签具名且为货主本人、无标签或无具名者。⚠ **唯一反向例外**：`Regardless of the exemptions ... collect the 702(b) portion for filth samples, unless your supervisor directs otherwise`——污秽样品无论豁免与否都要留。不留须在 C/R 的 Collection Remarks 写明理由。",
        "notes": "v4.16：702(b) 七项豁免 + 污秽样品反向例外",
    },
    {
        "id": "iom-sampling-04",
        "type": "edge_case",
        "prompt": "IOM 写环境取样 Listeria 至少 50 个子样、Salmonella 至少 100 个，我们就按这个数定厂里的 EMP 点位和频次可以吗？",
        "expected_behavior": "不可以。IOM 4.3.6.6.1 的 `collect at least 50 swabs/subs`（Listeria，ideal 100+）与 `collect at least 100 swabs/subs`（Salmonella，ideal 300+）是**检查员一次现场取样的最低子样量**，不是企业 EMP 标准。Zone 1–4 也是**检查员布点分区**：Zone 1 直接接触面、Zone 2 紧邻、Zone 3 再外层、Zone 4 远端，绝大多数取 Zone 1–2、`Very few, if any ... from Zone 4`；Listeria 须生产 ≥4 小时且湿洗前，Salmonella 宜湿洗前。企业侧点位与频次依自身危害分析与〔§ 117.165(a)(3)〕，还须注意 IOM 4.3.6.6.5 的阳性结果上 483 门槛。⚠ 检查程序不创设企业义务。",
        "notes": "v4.16：50/100 与 Zone 1–4 是检查员侧口径，不是企业 EMP 标准",
    },
    {
        "id": "iom-sampling-05",
        "type": "edge_case",
        "prompt": "检查员要来我们厂做环境拭子，能不能提前通知车间安排一下清洁？另外 IOM 不是说检查一般不预告吗？",
        "expected_behavior": "这是两个不同问题，不能混。IOM 4.3.6.6.1 关于**环境取样**写 `it is preferable during your discussions with a firm not to mention FDA's intent to collect environmental samples until, immediately, before sampling begins`——理由是防企业临时清洁、抑制微生物回收，属取样作业口径。而**检查是否预告**是 IOM Chapter 5（5.2.7）与 CPGM 7303.040 的问题，不得据此反推「检查本身一定不通知」。配套作业要点：Dey-Engley（D/E）中和肉汤、单向 10 次横纵（小面积 Dacron 拭子再加对角 10 次）、双层袋 + 预冻凝胶冰袋冷藏不冻结、**24 小时内到实验室**；Zone 1 与 for-cause 检查须逐子换手套。",
        "notes": "v4.16：环境取样不得预告 ≠ 检查是否预告；D/E 与 24 小时",
    },
    {
        "id": "iom-sampling-06",
        "type": "edge_case",
        "prompt": "我们 Zone 3 检出一次 Listeria，检查结束后实验室才出结果，检查员说不会写进 483，对吗？环境样品要不要勾 704(d)？",
        "expected_behavior": "两问都按 IOM 4.3.6.6.5 / 4.6.2.58 分开答。① **上 483 有双门槛**：`... are to be reported on the FDA 483 if the results are known prior to the conclusion/closeout of the inspection`（原文明确不得为等结果延长检查），且须构成显著观察——Listeria 阳性限 **Zone 1/2**、Salmonella 阳性限 **Zone 2/3**；**Zone 3（Listeria）与 Zone 4（任一病原）不写**，除非与 Zone 1/2 阳性合并以加强执法。检查关账后才出的结果也不写。② **704(d) 明确不勾**：`Environmental samples do not meet the criteria of 704(d) but FDA provides the sample results to firms`；704(d) 四问全 yes 才勾，且选择性取样的食品部分要勾。结果仍会给企业，由 HFP 发而非 OII 职责。",
        "notes": "v4.16：阳性上 483 双门槛 + 704(d) 不勾",
    },
    {
        "id": "iom-sampling-07",
        "type": "edge_case",
        "prompt": "IOM Sample Schedule Chart 2 的 24 罐 / 12 罐，和 CP 7303.070 PART IV.2 的 pH 4.40 / 4.65 / 4.75 是同一套数吗？能不能合起来算一个抽样标准？",
        "expected_behavior": "**不能合并，属两层**。IOM Sample Schedule Chart 2 是**取样计划**（LACF 现场按批大小对表，达到规定异常罐数即提前终止；official sample = 全部异常罐 + 规定正常罐，且正常罐数已含 702(b)；investigational / import = 全部异常 + 12 正常罐；AF 的 pH 取样 >795 g 取 12 罐、≤795 g 取 24 罐且**明确不含 702(b)**）。CP 7303.070 PART IV.2 的 4.40 / 4.65 / 4.75 与 24 罐 / 12 罐是**实验室触发线／检验判据**（CAP-19）。取样量三级优先见 IOM 4.3.2：`assignment → 适用 Compliance Program → IOM Sample Schedule`。⚠ 转换件 Chart 2 四组列在 GFM 后错列，只可引「批大小 → 检查数 → 提前终止数」对应关系，须回查 PDF。",
        "notes": "v4.16：Chart 2 取样计划 ≠ CP 7303.070 实验室触发线（两层不得混引）",
    },
    {
        "id": "iom-sampling-08",
        "type": "should_trigger",
        "prompt": "检查员在我们成品库拿了几箱货，怎么判定这批样品算不算 official sample？光是「拿了实物」就够吗？",
        "expected_behavior": "不够。「拿了实物」只是 physical 形态，official sample 的效力起点是 **21 CFR 2.10 三条件**（IOM 4.1.4 / 4.1.4.1）：`Introduced or delivered for introduction in interstate commerce` / `Was in or was received in interstate commerce` / `Was manufactured in a Territory or the District of Columbia`，且须有记录或其他证据支持；**进口样品一律是 official sample**。另须满足**四要件才算 valid**：随附确立联邦管辖与知情人身份的记录、代表所采之批、够实验室分析并在必要时留 702(b)、以维持证据完整性的方式标识封存并有清晰监管链。⚠ official sample 分 **physical 与 documentary（DOC）** 两类；INV / survey / non-regulatory 三类都不是。",
        "notes": "v4.16：21 CFR 2.10 三条件 + 四要件 valid + physical/DOC 二分",
    },
    {
        "id": "iom-sampling-09",
        "type": "should_trigger",
        "prompt": "一次现场取样从头到尾要开哪些 FDA 表单？封条有什么硬规则？",
        "expected_behavior": "按动作对号（IOM 4.2.5 / 4.7.4 / 4.7.5.3，Exhibit 4-4 / 4-5 / 4-17）：到场检查 → **FDA 482**；运途中取样 → 给承运人 FDA 482 + **FDA 472 Carriers Receipt**；取任何实体样品 → **FDA 484 Receipt for Samples**，且 `The receipt is to be issued to the owner, operator, or agent-in-charge, upon completion of the inspection, but prior to leaving the premises`；封样 → **FDA 415a Official Seal**（或金属封条）；包装标识 → **FDA 525**；证言 → FDA 463a / 1664 / 1664a / 1664b；州际证据 → FD 1662。**三类不发 482/484**：induced / undercover / online；DOC 另明文不发 484、不贴封条。**封条三硬规则**：`The seal must bear only one signature`（多人时由编制并签署 C/R 者签）、`Never place more than one sample in the same officially sealed package`、702(b) 建议独立容器独立封条；封条可用至厂商有效期后 5 年，拆封后须重封并把每张用过的封条随记录提交。",
        "notes": "v4.16：表单链 482/472/484/415a/525 与封条三硬规则",
    },
    {
        "id": "iom-sampling-10",
        "type": "should_not_trigger",
        "prompt": "帮我把这次取样的 FDA 484 和 415a 填好，顺便判一下这批样品能不能作为起诉证据、这次检查最后会不会 OAI。",
        "expected_behavior": "三件都不做。① **不代填表单**：IOM Chapter 4 是 FDA 给调查员的内部作业手册，表单签发、封条签名与 C/R 编制属检查员法定作业，本包只解释规则不代行。② **不判定证据能力**：样品能否作为起诉证据取决于法定管辖记录、代表性、702(b)、封存与监管链等事实，由 FDA 与法院判断；本包可给 IOM 4.1.4 / 4.2.5 / 4.7 的判定要件。③ **不预测检查结论**：OAI/VAI/NAI 由检查员依观察与证据判定，IOM 只给取证动作，不给预测。可提供的是：official / DOC / INV / survey 五类分流、取样量三级优先、702(b) 七项豁免、表单链表、483 门槛与转换件引用纪律。⚠ 检查程序**不创设企业义务**，企业侧义务回〔§ 117.xxx〕等法规正文。",
        "notes": "v4.16：代填表单 / 判证据能力 / 预测结论三重负例",
    },
]

NOTES_APPEND = (
    " | v4.16 追加 10 条 iom-sampling-* 用例（4 should_trigger / 5 edge_case / 1 should_not_trigger）："
    "DOC 不发 484 仍是 official sample、INV 可进法庭须封条、702(b) 七项豁免与污秽反向例外、"
    "50/100 是检查员侧最低量、环境取样不得预告、阳性上 483 双门槛与 704(d) 不勾、"
    "Chart 2 与 CP 7303.070 两层不得混引、21 CFR 2.10 三条件、表单链与 FDA 415a、"
    "代填表单/判证据/预测结论负例；新增第 28 张卡 iom-sampling-procedure，"
    "第二十来源 FDA《Investigations Operations Manual 2026, Chapter 4 – Sampling》"
    "（189 页 / 361 书签，检查程序作业层，不创设企业义务），"
    "60 个英文引用块经 .cangjie/verify_v4_16_quotes.py 核验 60/60 命中正文区；"
    "全库 233 条术语 / 168 条用例，二十类来源不可混引。"
)

# ── ④ DIGEST / PIPELINE_STATE 的当前态改写与追加节 ─────────────────────
DIGEST_REWRITES = [
    ("当前为 **v4.15.1：27 张能力卡 / 223 条术语 / 158 条测试用例 / 十九类来源**",
     "当前为 **v4.16：28 张能力卡 / 233 条术语 / 168 条测试用例 / 二十类来源**"),
]

DIGEST_SECTION = """
> **版本说明（v4.16，2026-11-09 追加）**：技能包纳入第二十来源 **FDA《Investigations Operations Manual 2026, Chapter 4 — Sampling》**（189 页 / 361 书签 / 4.2 MB），新增第 28 张卡 `iom-sampling-procedure`（CAP-28）。这是全包自 v4.5 起在 CAP-17 / 18 / 19 / 20 / 25 / 24、术语表与状态文档里反复标注「未收」的最后一块检查程序层空白，也是 `Sample Schedule Chart 2` 与 `702(b)` 分割留样细则的原文出处。该件是 **FDA 给调查员（Investigator / CSO）的内部作业手册**，非法规、非 Guidance for Industry、**不创设企业义务**；企业义务仍一律回〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕〔§ 108.xxx〕〔§ 120.xxx〕〔§ 123.xxx〕六套法规正文。本文正文仍保留第一来源的蒸馏结果不重写。
>
> **六条实质纠偏**：① **DOC sample 仍是 official sample**——`A DOC sample is not a sample of records`，记录本身即样品本体，只是不贴 FDA 415a、不发 FDA 484；② **INV 不是「非正式样品」**——`can be used as evidence in court, they must be sealed`；③ **`702(b)` 七项豁免不是封闭清单**，污秽样品是唯一「无论豁免与否仍要留」的反向例外，而环境拭子因被明文列入「无法以可行手段保存」通常不留；④ **环境取样不得预告**（防临时清洁抑制回收），50/100 子样、Zone 1–4、24 小时到实验室全部是**检查员侧**口径，不是企业 EMP 标准；⑤ **阳性环境结果上 483 有双门槛**（关账前已知 + Listeria Zone 1/2 或 Salmonella Zone 2/3，Zone 3/4 不写），且**环境样品明确不勾 704(d)**；⑥ **`Sample Schedule Chart 2` 终于有原文**，但它是**取样计划**，与 CP 7303.070 PART IV.2 的 4.40 / 4.65 / 4.75 实验室触发线仍属两层。
>
> CAP-28 R 段 **60 个英文引用块**经 `.cangjie/verify_v4_16_quotes.py` 逐字核验 **60/60 命中正文区**（0 超 100 词、0 表格引用），`body_only()` 排除自写文件头以防自我验证循环。转换件有四处红线：前部 Word 点线目录块与 `picture intentionally omitted` 表单占位不可逐字引；书签错位故检索以 `4.x.x` 小节号为准；`## **Dry Ice Guidance**` 等为伪标题；Chart 2 四组列在 GFM 后错列须回查 PDF。当前 **v4.16：28 张卡 / 233 术语 / 168 用例 / 二十类来源 / dist-v20**；上文 v4.15.1 及更早各节规模均为**当时口径**，保留不改。
"""

STATE_REWRITES = [
    ("- **当前版本**: v4.15.1 ✅ 编译校验并安装完成（27 张卡 / 223 术语 / 158 用例 / 十九类来源 / dist-v19）",
     "- **当前版本**: v4.16 ✅ 编译校验并安装完成（28 张卡 / 233 术语 / 168 用例 / 二十类来源 / dist-v20）"),
    ("逐版本明细见文末 v4.10–v4.15.1 各节", "逐版本明细见文末 v4.10–v4.16 各节"),
    ("当前为 **v4.15.1：27 张卡 / 223 术语 / 158 用例 / 十九类来源 / dist-v19**，见本文件顶部与末尾 v4.15.1 节",
     "当前为 **v4.16：28 张卡 / 233 术语 / 168 用例 / 二十类来源 / dist-v20**，见本文件顶部与末尾 v4.16 节"),
    ("- **开始时间**: 2026-11-04；最后更新 2026-11-06", "- **开始时间**: 2026-11-04；最后更新 2026-11-09"),
]

STATE_SECTION = """
## v4.16 — FDA IOM 2026 Chapter 4 落为第二十来源 + 取样全流程作业卡（28 张卡）

> 上文 v4.15.1 及更早各节中的「IOM Ch.4 未收」「Sample Schedule Chart 2 未收」「702(b) 分割留样细则未收」均为**当时口径**，自 v4.16 起已随本件纳入，见 `source-iom-ch4-2026.md` 与 CAP-28 `iom-sampling-procedure`。本节之外的 v4.x 规模、「十九类不可混引」等历史数字一律保留不改。

- **第二十来源**：**FDA《Investigations Operations Manual 2026, Chapter 4 — Sampling》**（189 页 / 361 书签 / 4.2 MB，PDF creationDate `2026-07-14`；用户提供的官方 PDF 经用户级技能 `pdf2md-pro` / pymupdf4llm 转换）。属**检查程序作业层**：给调查员的内部作业手册，非法规、非 Guidance for Industry、**不创设企业义务**。文件头补「来源 / 效力层级 / 关键口径 / 转换局限」说明块（对齐 IOM Ch.5 的写法）。
- **转换与自检**：`.cangjie/iom-ch4-convert-report.json` 记录 **361/361 书签全用、0 丢弃**，405 标题（H1 1 / H2 89 / H3 68 / H4 169 / H5 78）、345 行表格、页眉 `CHAPTER 4` 与独立页码残留 0、自动检出噪声行 2；七节 `4.1`–`4.7` 与 Exhibit 4-1…4-25、Sample Schedule Chart 1–14 全在。CAP-28 R 段 **60 个英文引用块**经 `.cangjie/verify_v4_16_quotes.py` 核验 **60/60 命中正文区**（0 超 100 词、0 表格引用、0 仅命中文件头），`body_only()` 以 `**4.1 – GENERAL ...` 为正文分界排除自写文件头，避免自我验证循环。初跑 2 处未命中已修：D/E 句主语带脚注 `[6]` 改为从句中起、483 句被转换件插入错位书签改用 `…` 节引并注明。
- **新增能力卡 CAP-28 `iom-sampling-procedure`**（`.cangjie/capabilities/cards/iom-sampling-procedure.md` + `_meta-iom-sampling-procedure.yaml`）。把一次取样拆成六道分流：类别（official physical / official DOC / INV / survey / non-regulatory）→ 数量（assignment → CP → IOM Sample Schedule 三级优先）→ 702(b) → 表单链（482 / 472 / 484 / 415a / 525 / 463a / 1664）→ 封存与运输 → 阳性结果与 483。
- **六类实质纠偏**：① **DOC 仍是 official sample**，只是不贴封条、不发 FDA 484——「没开 484」不能读成「样品不算数」；② **INV 不是「非正式样品」**，原文 `can be used as evidence in court, they must be sealed`；③ **702(b) 七项豁免不是封闭清单**，污秽样品是唯一反向例外，环境拭子因被明文列入「无法以可行手段保存」通常不留；④ **环境取样不得预告**，且 50/100、Zone 1–4、24 小时到实验室全是**检查员侧**口径，不是企业 EMP 标准；⑤ **阳性环境结果上 483 有双门槛**（关账前已知 + Listeria Zone 1/2 或 Salmonella Zone 2/3；Zone 3/4 不写），且**环境样品明确不勾 704(d)**；⑥ **Sample Schedule Chart 2 终于有原文**，但它是**取样计划**，与 CP 7303.070 PART IV.2 的 4.40 / 4.65 / 4.75 实验室触发线仍属两层。
- **Bundle 回补**：`.cangjie/apply_v4_16_revisions.py` 以「内存 dict 暂存 + 每处 `assert count == 1` + dry-run 后 `--apply`」写盘 **57 个文件**，把 cards/ 与 `assemble_bundle.py` 的当前态统一为「**二十类不可混引 / 28 张卡**」，并清除各卡把 IOM Ch.4 写作「未收」的裸断言；`assemble_bundle.py` 27 → **28 卡**（SLUGS、ALSO_READ 12 条正向链 + 13 张卡反向链）、`additional_sources` 18 → **19 条**（末条 `src-fda-iom-ch4-2026`）、core_principles 54 → **56**、stop_conditions 28 → **30**、entry.description 增加 IOM Ch.4 段落。
- **术语与用例**：`candidates/glossary.md` 223 → **233 条**（t224–t233：official sample 三条件、DOC、INV/survey/non-regulatory、702(b) 七项豁免、Zone 1–4、不得预告与 D/E / 24 小时、表单链与 415a、阳性上 483 与 704(d)、Chart 2、六套数量分层与转换件引用纪律）。`test-prompts.json` 158 → **168 条**（`iom-sampling-01..10`：4 should_trigger / 5 edge_case / 1 should_not_trigger），version → **4.16**。
- **转换局限（写入 CAP-28 B12）**：① 文件前部（L3–L17）是 Word 点线目录压成的巨型单行块，非正文，检索以 `4.x.x` 小节号为准；② 书签插入位置错位（`4.7.2` 在 `4.7.1` 之前、`4.6.4` 混入 4.7 区），小节标题常以 heading 与 plain text 两种形态各出现一次；③ `## **Dry Ice Guidance**` / `## **PRODUCT**` / `## **CODE**` 等为伪标题；④ Exhibit 4-1…4-25 表单为 `picture intentionally omitted` 占位（全章 41 处），字段名可引、表格式样不可引；⑤ Chart 2 的 48/CASE、24/CASE、12/CASE、6/CASE 四组在 GFM 转换后错列，只可引「批大小 → 检查数 → 提前终止数」对应关系。
- **编译与安装**：⏳ 见本节末尾「编译与安装记录」，待 dist-v20 编译、官方校验、用户级安装、逐文件 sha256 比对与静态路由核对完成后回填实测数字。
- **仍未收**：IOM Chapter 2 / 3 / 6 / 7 / 8 / 9 / 10 全本（尤其 Ch.3 的 3.2 权限、Ch.6 的 6.4 进口取样、Ch.8 的投诉与食源性疾病调查）、SOP-001052 / FMD-147 / OII SOP-000530、RPM 6-3 / 10-4、CPG 580.100 / 300.400 / 130.100 全文、BAM / AOAC / MPM 方法全文、FACTS / eNSpect / CMS / OASIS 内部操作、Form FDA 484 表单栏目细则。
- **评测**：本版未重跑触发 / 输出 / 路由评测；v4.7–v4.14 的既有结论不得冒用。
"""


def main() -> int:
    apply = "--apply" in sys.argv
    files: dict[Path, str] = {}

    def get(rel: str) -> str:
        p = BASE / rel
        if p not in files:
            files[p] = p.read_text(encoding="utf-8")
        return files[p]

    def put(rel: str, t: str) -> None:
        files[BASE / rel] = t

    # ① glossary 术语插入（最后一个 ```yaml 块的闭合围栏前）
    rel = "candidates/glossary.md"
    t = get(rel)
    fence = "\n```\n\n## 自检记录"
    assert t.count(fence) == 1, "glossary 闭合围栏定位失败"
    assert "id: t224" not in t, "术语已插入，勿重跑"
    t = t.replace(fence, TERMS_SAFE + fence)
    # 自检记录追加一行
    marker = "- [x] 第十九来源 **FDA CP 7303.847"
    idx = t.find(marker)
    assert idx >= 0, "自检记录锚点缺失"
    eol = t.find("\n", idx)
    t = t[: eol + 1] + "\n" + CHECKLINE + t[eol + 1 :]
    # 当前态未收断言
    for old, new in GLOSSARY_REWRITES:
        assert t.count(old) == 1, f"glossary 改写锚点命中 {t.count(old)} 次: {old[:60]!r}"
        t = t.replace(old, new)
    put(rel, t)
    print(f"OK   [glossary] t224–t233 + 自检记录 + {len(GLOSSARY_REWRITES)} 处当前态断言")

    # ② overview
    rel = "BOOK_OVERVIEW.md"
    t = get(rel)
    assert "## v4.16 追加" not in t
    for old, new in OVERVIEW_REWRITES:
        assert t.count(old) == 1, f"overview 改写锚点命中 {t.count(old)} 次: {old[:60]!r}"
        t = t.replace(old, new)
    t = t.rstrip("\n") + "\n" + OVERVIEW_SECTION
    put(rel, t)
    print(f"OK   [overview] v4.16 节 + {len(OVERVIEW_REWRITES)} 处当前态断言")

    # ③ test-prompts.json（结构化追加；round-trip 无损性先自检）
    rel = "test-prompts.json"
    t = get(rel)
    assert json.dumps(json.loads(t), ensure_ascii=False, indent=2) + "\n" == t, \
        "test-prompts.json 的 JSON 格式假设失效，拒绝重写"
    d = json.loads(t)
    assert d["version"] == "4.15.1", f"version 非 4.15.1: {d['version']}"
    assert len(d["test_cases"]) == 158, f"原用例数非 158: {len(d['test_cases'])}"
    old_ids = [c["id"] for c in d["test_cases"]]
    assert len(old_ids) == len(set(old_ids)), "原用例 id 有重复"
    assert not any(i.startswith("iom-sampling-") for i in old_ids), "iom-sampling-* 用例已插入，勿重跑"
    assert len(NEW_CASES) == 10 and len({c["id"] for c in NEW_CASES}) == 10
    assert all(set(c) == {"id", "type", "prompt", "expected_behavior", "notes"} for c in NEW_CASES)
    kinds = {k: sum(1 for c in NEW_CASES if c["type"] == k)
             for k in ("should_trigger", "edge_case", "should_not_trigger")}
    assert kinds == {"should_trigger": 4, "edge_case": 5, "should_not_trigger": 1}, kinds
    assert "v4.16 追加 10 条" not in d["notes"], "notes 尾注已追加，勿重跑"
    d["test_cases"].extend(NEW_CASES)
    d["version"] = "4.16"
    d["notes"] += NOTES_APPEND
    assert len(d["test_cases"]) == 168
    assert len({c["id"] for c in d["test_cases"]}) == 168
    put(rel, json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"OK   [test-prompts] 158 → 168 条（{kinds}）、version 4.15.1 → 4.16、notes 尾注")

    # ④ DIGEST.md / PIPELINE_STATE.md（只改当前态 + 追加增量节）
    rel = "DIGEST.md"
    t = get(rel)
    assert "版本说明（v4.16" not in t, "DIGEST v4.16 节已追加，勿重跑"
    for old, new in DIGEST_REWRITES:
        assert t.count(old) == 1, f"DIGEST 改写锚点命中 {t.count(old)} 次: {old[:60]!r}"
        t = t.replace(old, new)
    t = t.rstrip("\n") + "\n" + DIGEST_SECTION
    put(rel, t)
    print(f"OK   [DIGEST] 当前态 {len(DIGEST_REWRITES)} 处 + v4.16 说明节")

    rel = "PIPELINE_STATE.md"
    t = get(rel)
    assert "## v4.16 —" not in t, "PIPELINE_STATE v4.16 节已追加，勿重跑"
    for old, new in STATE_REWRITES:
        assert t.count(old) == 1, f"STATE 改写锚点命中 {t.count(old)} 次: {old[:60]!r}"
        t = t.replace(old, new)
    t = t.rstrip("\n") + "\n" + STATE_SECTION
    put(rel, t)
    print(f"OK   [PIPELINE_STATE] 当前态 {len(STATE_REWRITES)} 处 + v4.16 版本节（编译记录留占位）")

    if not apply:
        print(f"\n[dry-run] 涉及 {len(files)} 个文件，未写盘。加 --apply 落地。")
        return 0
    for p, content in files.items():
        p.write_text(content, encoding="utf-8")
    print(f"\n已写盘 {len(files)} 个文件。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())