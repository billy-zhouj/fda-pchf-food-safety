#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""append_v4_1.py — 为 cgmp-compliance-guide 卡的三处 SECG 简化补充术语（t107–t110）与测试用例（v4.1）"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------- 1. 术语 t107–t110 ----------------
NEW_TERMS = """
- id: t107
  title: 强制现场审核升级（supplier onsite audit escalation）
  type: term
  source_chapter: 21 CFR 117.430(b)(1)(2)；对照 SECG IX.A（未展开）
  source_quote: |
    "when a hazard in a raw material or other ingredient will be controlled by the supplier and is
    one for which there is a reasonable probability that exposure to the hazard will result in
    serious adverse health consequences or death to humans: (i) The appropriate supplier
    verification activity is an onsite audit of the supplier; and (ii) The audit must be conducted
    before using the raw material or other ingredient from the supplier and at least annually thereafter."
  summary: 供应商验证活动的四类（现场审核／抽样检测／审阅记录／其他适当活动）并非自由选择。**若该原料危害由供应商控制，且暴露后有可能导致严重健康后果或死亡**，〔§ 117.430(b)(1)〕规定当时唯一适当的验证活动是**现场审核**，且须在首次使用前完成、之后至少每年一次。唯一合法降级出口是〔§ 117.430(b)(2)〕的 **written determination**（书面判定其他活动或更低频审核能提供足够保证）。SECG IX.A 只并列四类活动、未提这条升级，据 SECG 应答「能不能只靠 COA」会答错。
  tags: [供应链, 供应商验证, 强制条款, SECG 简化, 高频误读]

- id: t108
  title: qualified facility 状态双向通知（status change notification）
  type: term
  source_chapter: 21 CFR 117.201(c)(2)(i)(C)、(c)(3)、(d)；SECG XI.D（只写单向）
  source_quote: |
    "(C) By July 31 of the applicable calendar year, when the status of a facility changes from
    'not a qualified facility' to 'qualified facility' based on the annual determination required by
    paragraph (c)(1) of this section." / "When the status of a facility changes from 'qualified
    facility' to 'not a qualified facility' ... the facility must notify FDA of that change in status
    using Form 3942a by July 31 of the applicable calendar year."
  summary: 状态变更是**双向义务**，且时限都在 7 月 31 日。① **由非变是**：当年 **7 月 31 日**前完成首次申报〔(c)(2)(i)(C)〕——SECG XI.D 未写这一方向。② **由是变非**：当年 **7 月 31 日**前用 Form 3942a 通知 FDA〔(c)(3)〕，并在当年 **12 月 31 日**前符合危害分析与预防控制要求〔(d)〕。此外每年 **7 月 1 日**前须完成并记录资格判定〔(c)(1)〕；2020 年起每两年一次，在 10-01 至 12-31 窗口内提交〔(c)(2)(ii)〕。判定门槛用 `exceeded`（超过），不是「至少一半」。
  tags: [qualified facility, 申报时限, 双向义务, SECG 简化]

- id: t109
  title: qualified facility 豁免撤销程序（withdrawal of exemption）
  type: term
  source_chapter: 21 CFR 117.251、117.254、117.257、117.260、117.264、117.267、117.270、117.277；SECG XI.E（止于 15 日答复）
  source_quote: |
    "FDA may withdraw a qualified facility exemption — In the event of an active investigation of a
    foodborne illness outbreak that is directly linked to the qualified facility; or If FDA determines
    that it is necessary to protect the public health ..." / "provide an opportunity ... to respond in
    writing, within 15 calendar days of the date of receipt of the notification"
  summary: 触发情形两项〔§ 117.251(a)〕：与该设施直接相关的食源性疾病暴发**在行调查**；或 FDA 为保护公众健康判定必要。程序完整链条：书面意向通知 + **15 个日历日**书面答复窗口〔§ 117.251(b)(2)〕→ 撤销令须经分区主任（境外为 CFSAN 合规办公室主任）或其上级**批准**〔§ 117.254(a)〕→ 令件须载明法定内容〔§ 117.257〕→ 收到令后可选择**遵守或上诉**〔§ 117.260〕，可申请**非正式听证**〔§ 117.267、§ 117.270〕，决定时限见〔§ 117.277〕。**SECG XI.E 只写到 15 日答复**，据其判断「没有后续救济」是错的。
  tags: [qualified facility, 撤销豁免, 行政程序, SECG 简化]

- id: t110
  title: subpart B 的五类不适用情形（§ 117.5(k)）
  type: term
  source_chapter: 21 CFR 117.5(k)(1)(2)；SECG VI. Table 4 脚注 2（一行带过）
  source_quote: |
    "(k)(1) Except as provided by paragraph (k)(2) of this section, subpart B of this part does not
    apply to any of the following: (i) 'Farms' (as defined in § 1.227 of this chapter); (ii) Fishing
    vessels that are not subject to the registration requirements ...; (iii) Establishments solely
    engaged in the holding and/or transportation of one or more raw agricultural commodities;
    (iv) Activities of 'farm mixed-type facilities' ... that fall within the definition of 'farm'; or
    (v) Establishments solely engaged in hulling, shelling, drying, packing, and/or holding nuts
    (without additional manufacturing/processing, such as roasting nuts)."
  summary: 这是**唯一能把 CGMP 本身也免掉**的条款，与只免 Subparts C/G 的豁免不同层级。五类：farm、不受注册要求的渔船、**仅从事初级农产品存放和/或运输的场所**、farm mixed-type 设施中属 farm 定义的活动、**仅做坚果去壳/脱壳/干燥/包装/存放而不烘烤**的场所。回拉条款〔(k)(2)〕：farm 或 farm mixed-type 设施若干燥/脱水 covered produce 以形成 distinct commodity，则 subpart B 适用于该干燥品的包装、打包与存放（可通过符合 part 112 相应要求达标）。判定顺序上这是 Step 1 的第②关，SECG 仅在 Table 4 脚注 2 提一句。
  tags: [适用性边界, subpart B, farm, SECG 简化, 高频误读]
"""

gl = ROOT / "candidates" / "glossary.md"
text = gl.read_text(encoding="utf-8")
anchor = "\n## 自检记录"
assert anchor in text, "未找到自检记录节"
# 插到 yaml 围栏结束前
fence_idx = text.rindex("```", 0, text.index(anchor))
text = text[:fence_idx] + NEW_TERMS.strip("\n") + "\n\n" + text[fence_idx:]
# 更新自检记录条目
old_line = "106 条（原始 84 条 + 21 CFR Part 117 增量 1 条 + L.mono 指南 XIX Glossary 增量 15 条 + SECG 增量 6 条；"
new_line = "110 条（原始 84 条 + 21 CFR Part 117 增量 1 条 + L.mono 指南 XIX Glossary 增量 15 条 + SECG 增量 10 条；"
if old_line in text:
    text = text.replace(old_line, new_line)
text = text.replace(
    "- [x] 高频误读类术语（potential hazard",
    "- [x] SECG 三处已知简化（供应商强制现场审核、qualified facility 双向通知、撤销豁免完整程序）与 § 117.5(k) 五类不适用情形已补为 t107–t110，均标注 SECG 未展开之处\n- [x] 高频误读类术语（potential hazard",
)
gl.write_text(text, encoding="utf-8")
print("术语写入完成，当前条数:", text.count("- id: t"))

# ---------------- 2. 测试用例 ----------------
tp = ROOT / "test-prompts.json"
d = json.loads(tp.read_text(encoding="utf-8"))

new_cases = [
    {
        "id": "secg-audit-01",
        "type": "should_trigger",
        "prompt": "我们买一款即食原料，致病菌危害是供应商控制的，能不能每批拿个 COA、每年看一次供应商记录就够了，不做现场审核？",
        "expected_behavior": "应先问该危害的严重性档位，而不是直接答『可以，SECG 列了四类活动任选』。若属『暴露后有可能导致严重健康后果或死亡』档，则〔§ 117.430(b)(1)〕规定唯一适当的验证活动是现场审核，须首次使用前做、之后至少每年一次；要降级必须出具〔§ 117.430(b)(2)〕的 written determination。同时提示三类特殊供应商豁免〔§ 117.430(c)(d)(e)〕：qualified facility 供应商、不受 part 112 约束的农场、少于 3000 只蛋鸡的带壳蛋生产商。指出 SECG IX.A 未展开此升级，不可据其作答",
        "notes": "针对 SECG 简化 1：四类验证活动被读成自由选择",
    },
    {
        "id": "secg-qf-01",
        "type": "should_trigger",
        "prompt": "我们厂去年销售额降到 45 万美元，超过一半卖给本地餐馆，今年变成 qualified facility 了，需要通知 FDA 吗？什么时候？",
        "expected_behavior": "应指出这是『由非变是』方向，须在当年 7 月 31 日前完成首次申报（〔§ 117.201(c)(2)(i)(C)〕），并提示 SECG XI.D 只写了反方向所以容易漏；同时给出配套时限：每年 7 月 1 日前完成并记录资格判定、2020 年起每两年在 10-01 至 12-31 窗口提交、若日后由是变非须在 7 月 31 日前用 Form 3942a 通知并在 12 月 31 日前符合 PCHF；并提示判定门槛是 `exceeded`（超过）而非『至少一半』，且须按三年均值、含无销售持有的市场价值、通胀调整基准年 2011",
        "notes": "针对 SECG 简化 2：状态变更只写单向；兼验 exceeded vs at least half",
    },
    {
        "id": "secg-withdraw-01",
        "type": "should_trigger",
        "prompt": "FDA 给我们发了撤销 qualified facility 豁免的意向通知，我们 15 天内答复了，之后还能做什么？",
        "expected_behavior": "应说明 15 日书面答复只是撤销**之前**的陈述机会（〔§ 117.251(b)(2)〕），不是全部救济。后续链条：撤销令须经分区主任（境外为 CFSAN 合规办公室主任）或其上级批准〔§ 117.254(a)〕；令件载明法定内容〔§ 117.257〕；收到令后可选择遵守或上诉〔§ 117.260〕，可申请非正式听证〔§ 117.267、§ 117.270〕，决定时限见〔§ 117.277〕。并指出 SECG XI.E 讲到 15 日即止，不能据其判断没有后续程序",
        "notes": "针对 SECG 简化 3：撤销程序讲到一半就停",
    },
    {
        "id": "secg-1175k-01",
        "type": "edge_case",
        "prompt": "我们只做坚果的去壳、干燥和包装，不做烘烤，也不做其他加工。CGMP 我们是不是也要全做？",
        "expected_behavior": "应指出这是〔§ 117.5(k)(1)(v)〕的情形——仅从事坚果去壳/脱壳/干燥/包装和/或存放而不做烘烤等进一步加工的场所，**subpart B 也不适用**，这是唯一能把 CGMP 本身免掉的条款，与只免 Subparts C/G 的豁免不同层级。同时提示：一旦增加烘烤等进一步加工即落入 subpart B；〔§ 117.5(k)(2)〕对 farm 系干燥 covered produce 的回拉条款不适用于本情形但应一并说明以免误用；并指出 SECG 仅在 Table 4 脚注 2 提一句，判定须回法规正文",
        "notes": "边界场景：唯一能免 CGMP 本身的条款，验证 B10 与 Step 1 的第②关",
    },
]

existing = {c["id"] for c in d["test_cases"]}
added = 0
for c in new_cases:
    if c["id"] not in existing:
        d["test_cases"].append(c)
        added += 1

d["version"] = "4.1"
tp.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

from collections import Counter
print(f"用例新增 {added} 条，当前 version={d['version']} 共 {len(d['test_cases'])} 条")
print("类型分布:", dict(Counter(c["type"] for c in d["test_cases"])))