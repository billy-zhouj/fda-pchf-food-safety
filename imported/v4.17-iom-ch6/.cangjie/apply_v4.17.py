# -*- coding: utf-8 -*-
"""把 IOM 2026 Chapter 6 蒸馏产物增量写入 fda-pchf-food-safety v4.17。

幂等性：脚本会检查是否已打过 v4.17 标记，已打则拒绝重跑（避免重复插入）。
每处 SKILL.md 替换都断言命中次数，未命中即抛错。
"""
import json
import pathlib
import shutil
import sys

ROOT = pathlib.Path(r"E:/WeChatData/2026-11-09-08-58-24")
BOOK = ROOT / "books/iom-2026-ch6-imports"
DIST = BOOK / "dist"
PKG = pathlib.Path(r"C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety")
CAP = PKG / "references/capabilities"

report = []


def note(msg):
    report.append(msg)
    print(msg)


# ---------------------------------------------------------------- 0. 幂等检查
skill = (PKG / "SKILL.md").read_text(encoding="utf-8")
if "v4.17 新增第二十一来源" in skill:
    sys.exit("ABORT: SKILL.md 已含 v4.17 标记，拒绝重复写入。")
assert "cangjie.capability-count: 28" in skill, "前置版本不是 v4.16（capability-count 28）"

# ---------------------------------------------------------------- 1. 修 483a 触发歧义
entry_src = (DIST / "capabilities/iom-imports-procedure.md").read_text(encoding="utf-8")
anchor = "本卡对象是 entry line 的货物准入与事后追责，产物是 FDA 内部的决定、文书与时间窗，不是进口商的合规义务清单。*"
assert anchor in entry_src, "入口卡定位段锚点未命中"
trigger_fix = (
    "**⚠ 触发判别（避免 483 / 483a 字形吸附）**：凡问 `483a` / FSVP Observations / "
    "closeout 唯一签发时点 / 检查期间能否展示草稿 / 15 工作日 FSVP 回应 / importer 定义三类证明 / "
    "T-EIR·CARS 分流 → **本卡 V08**；凡问 `FDA 483` 现场检查观察项措辞纪律 / 483 回复骨架 / "
    "Ch.5 检查员权限与 482·484 → **转 CAP-18，不进本卡**。同一串数字加一个字母 a，归属两套完全不同的文书序列，"
    "不得因字形相近合并路由。本卡对象是 entry line 的货物准入与事后追责，产物是 FDA 内部的决定、文书与时间窗，"
    "不是进口商的合规义务清单。*"
)
entry_src = entry_src.replace(anchor, trigger_fix, 1)
v08_old = "| V08 | FSVP 检查链与 FDA 483a 签发门 |"
assert v08_old in entry_src
entry_src = entry_src.replace(v08_old, "| V08 ★ | FSVP 检查链与 FDA 483a 签发门（⚠ 483a≠483，不转 CAP-18） |", 1)
(DIST / "capabilities/iom-imports-procedure.md").write_text(entry_src, encoding="utf-8")
note("[1] 入口卡已定点修 A2：加入 483/483a 触发判别句 + V08 路由行硬标记")

# ---------------------------------------------------------------- 2. 复制能力卡
shutil.copy2(DIST / "capabilities/iom-imports-procedure.md", CAP / "iom-imports-procedure.md")
subdir = CAP / "imports"
subdir.mkdir(exist_ok=True)
subcards = sorted((DIST / "capabilities/imports").glob("*.md"))
assert len(subcards) == 10, f"子卡数量应为 10，实际 {len(subcards)}"
for f in subcards:
    shutil.copy2(f, subdir / f.name)
note(f"[2] 已复制 CAP-29 入口卡 1 张 + 子卡 {len(subcards)} 张 → references/capabilities/")

# ---------------------------------------------------------------- 3. capability-index.md 追加 CAP-29
idx_path = PKG / "references/capability-index.md"
idx = idx_path.read_text(encoding="utf-8")
assert "| CAP-29 |" not in idx
intents_29 = (
    "判断 FDA 进口准入与处置链（IOM 2026 Chapter 6）：entry line 该发 May Proceed / 请求现场工作 / "
    "提交扣留建议 / OGA Referral 关闭；与 PREDICT 相悖的放行须写可核验理由且禁止空泛备注；"
    "DER 与 DTR 按触发依据分流、DWPE「不检查就扣住」、Import Alert 命中能否免索单据、"
    "查不到注册/510(k)/A of C 不得直接建议扣留；Prior Notice 适用性与 2/4/8 小时、15/30 天双向窗、"
    "inadequate 后 refusal+hold；条件放行期 30 天不延长不重开、撤消放行后 24 小时动作、"
    "三个 30 天与一个 90 天窗口分野；Detained→10 工作日听证→FDA 766 改标重整授权门→放行/拒绝→"
    "90 天出口销毁→Bond Action 的环节—文书—时限矩阵（拒绝不是终点）；Failure to Hold 是"
    "「无放行而分销」而非「移出港区」与 8 步取证下限、健康危害/DWPE 加重；"
    "FSVP 检查执行 SOP 与 FDA 483a 只在 closeout 签发且只签已签名版（⚠ 483a≠483，CAP-18 管 483）、"
    "importer 定义三类证明、15 工作日回应；进口状态概念区分树（四种放行 / Conditional Release / "
    "Detention / DWPE / Refusal）；IOM 效力层判读（must·shall 约束 FDA 内部作业、should·as warranted·may 属裁量、"
    "IOM 非法规、2026 版快照、企业侧内容须冠〔推导·非原书主张〕）；"
    "判断哪些问题超出本卡（取样量与环境拭子转 CAP-17/28、FDA 483 现场检查观察项转 CAP-18、"
    "FSVP 合规程序与 §1.5xx 主体判定转 CAP-21、21 CFR part 1 subpart L 正文与 RPM/CPG/Import Alert 全文转引未收）"
)
keywords_29 = (
    "IOM 2026 Chapter 6、Imports、进口准入、entry line、May Proceed、PREDICT、DER、DTR、DWPE、"
    "Import Alert、Prior Notice、2/4/8 hours、15/30 calendar days、Conditional Release、rescind、"
    "redelivery、CBP 4647、Detained、10 working days、Form FDA 766、Reconditioning、Relabeling、"
    "Refusal of Admission、90 days、Bond Action、Failure to Hold、affidavit、Substitution、"
    "FSVP、FDA 483a、closeout、T-EIR、CARS、Importer of Record、Release with Comment、"
    "IB Release、VQIP、ITACS、OGA Referral、Notice of FDA Action、FDA 790、"
    "FD&C Act §801、21 CFR Part 1、19 CFR 113.62、二十一类不可混引"
)
row = (
    f"| CAP-29 | FDA 进口准入判定与处置链（IOM 2026 Chapter 6） | extended | {intents_29} | "
    f"{keywords_29} | capabilities/iom-imports-procedure.md |\n"
)
if not idx.endswith("\n"):
    idx += "\n"
idx_path.write_text(idx + row, encoding="utf-8")
note("[3] capability-index.md 追加 CAP-29 索引行")

# ---------------------------------------------------------------- 4. SKILL.md 精确更新
def rep(text, old, new, count=1, label=""):
    n = text.count(old)
    assert n >= count, f"未命中替换锚点 [{label}] (found {n}): {old[:80]!r}"
    return text.replace(old, new, count)

s = skill
s = rep(s, "cangjie.capability-count: 28", "cangjie.capability-count: 29", 1, "capability-count")

# 4a. frontmatter description 追加一段（插在 metadata: 之前，缩进与 block scalar 一致）
desc_add = (
    "  另覆盖 FDA 进口准入判定与处置链（IOM 2026 Chapter 6，v4.17 新增 CAP-29 `iom-imports-procedure`）："
    "entry line 的有限动作集与可辩护判定留痕、May Proceed 撤消、DER/DTR 按触发依据分流与 DWPE「不检查就扣住」、"
    "Prior Notice 的 2/4/8 小时与 15/30 天双向窗、条件放行期 30 天不延长不重开与三套窗口分野、"
    "Detained→听证→Form FDA 766 改标重整→Refusal→90 天出口销毁→Bond Action 的环节—文书—时限矩阵、"
    "Failure to Hold「无放行而分销」与 8 步取证、FSVP 检查 FDA 483a 的 closeout 唯一签发门（⚠ 483a≠483）、"
    "进口状态概念区分树与 IOM 效力层判读（must/shall 约束 FDA 内部作业、should/as warranted 属裁量、IOM 非法规）。"
    "不处理取样量与环境拭子（转 CAP-17/28）、FDA 483 现场检查观察项（转 CAP-18）、FSVP 合规程序与豁免（转 CAP-21）。\n"
)
s = rep(s, "metadata:\n", desc_add + "metadata:\n", 1, "description 追加")

# 4b. 不适用条目：进口扣留应诉文书（判定链已收，仍不代写）
s = rep(
    s,
    "FDA 483 回复/警告信答复/进口扣留应诉文书、检查结果预测与保证",
    "FDA 483 回复/警告信答复/进口扣留应诉文书代写（判定与举证口径自 v4.17 起转 CAP-29，本条仅指不代写文书）、检查结果预测与保证",
    1, "不适用条目",
)

# 4c. 第二十一来源
s = rep(
    s,
    "v4.16 新增第二十来源 IOM 2026 Ch.4）",
    "v4.16 新增第二十来源 IOM 2026 Ch.4、v4.17 新增第二十一来源 IOM 2026 Ch.6）",
    1, "来源计数",
)

# 4d. 能力路由表插入 CAP-29 行（在 CAP-28 那一行之后）
lines = s.split("\n")
cap28_i = next(
    i for i, ln in enumerate(lines)
    if ln.startswith("| 判定一份样品是否构成 21 CFR 2.10 意义上的 official sample")
)
route_intent = intents_29.replace("判断哪些问题超出本卡（", "判断哪些问题超出本卡（")  # 保持完整意图列
route_row = (
    f"| {route_intent} | references/capabilities/iom-imports-procedure.md | "
    "references/capabilities/imports/*.md（10 张子卡，按入口卡路由表加载 1 张）、"
    "references/capabilities/iom-sampling-procedure.md、"
    "references/capabilities/investigator-authority-procedure.md、"
    "references/capabilities/fsvp-inspection-program.md、"
    "references/capabilities/inspection-sampling.md |"
)
lines.insert(cap28_i + 1, route_row)
s = "\n".join(lines)
note("[4d] SKILL.md 能力路由表已插入 CAP-29 行（紧随 CAP-28）")

# 4e. 条款引用规则：IOM Ch.6 引用格式 + 二十一类 + 未收清单移除 Ch.6
s = rep(
    s,
    "Chapter 5 用「IOM 5.x.x / IOM Exhibit 5-x」，CP 7303.070",
    "Chapter 5 用「IOM 5.x.x / IOM Exhibit 5-x」、Chapter 6 用「IOM 6.x.x [p.N] / IOM Exhibit 6-x」"
    "（p.N 为 PDF 印刷页码，6.2.5.5 的 reasonable effort 条款正文跨页落在 p.23 与 6.3 起始页重叠，"
    "引用按小节号而非分块文件名），CP 7303.070",
    1, "IOM 引用格式",
)
s = rep(
    s,
    "IOM 其余各章（2/3/6/7/8/9/10）、BAM、CPG、Import Alert 等未收正文一律标「转引未收」；**二十类不可混引**",
    "IOM 其余各章（2/3/7/8/9/10）、BAM、CPG、Import Alert 等未收正文一律标「转引未收」；"
    "**二十一类不可混引**（IOM 2026 Ch.6 自 v4.17 起已收，见 CAP-29）",
    1, "二十一类不可混引",
)

# 4f. 29 张能力卡 + CAP-29 转介
s = rep(
    s,
    "用户任务超出 28 张能力卡路由范围时，明确告知超出本包覆盖，不要硬套；",
    "用户任务超出 29 张能力卡路由范围时，明确告知超出本包覆盖，不要硬套；"
    "进口准入判定与处置链转 CAP-29（先读入口卡再按意图加载 1 张子卡），",
    1, "能力卡数量",
)

# 4g. 仍未收清单移除 Chapter 6
s = rep(
    s,
    "仍未收：IOM Chapter 2/3/6/7/8/9/10、RPM、FMD-86",
    "仍未收：IOM Chapter 2/3/7/8/9/10（**IOM Chapter 6 自 v4.17 起已收，转 CAP-29**）、RPM、FMD-86",
    1, "仍未收清单 A",
)
s = rep(
    s,
    "**仍未收的是 IOM Chapter 2 / 3 / 6 / 7 / 8 / 9 / 10 全本**（尤其 Ch.3 的 3.2 法定权限、Ch.6 的 6.4 进口取样、Ch.8 的投诉与食源性疾病调查）",
    "**仍未收的是 IOM Chapter 2 / 3 / 7 / 8 / 9 / 10 全本**（尤其 Ch.3 的 3.2 法定权限、Ch.8 的投诉与食源性疾病调查）；"
    "**Chapter 6 自 v4.17 起已收（第二十一来源，CAP-29）**，其 6.4 进口取样给出的是进口取样政策与 SCR 字段规范，"
    "取样作为证据的类别判定与 702(b) 分割留样仍转 CAP-28",
    1, "仍未收清单 B",
)
s = rep(
    s,
    "全包自 v4.16 起**二十类不可混引**，当前为 28 张能力卡",
    "全包自 v4.17 起**二十一类不可混引**，当前为 29 张能力卡",
    1, "当前口径",
)

# 4h. 边界区追加 CAP-29 专用规则
boundary_add = "\n".join([
    "- IOM Chapter 6 正文自 v4.17 起已收（第二十一来源，CAP-29 `iom-imports-procedure`），引用写「IOM 6.x.x [p.N]」"
    "（Exhibit 6-1~6-4 为扫描件，字段一律标「需查原件」），**不得写成〔§ 117.xxx〕式法规引用，也不得与 IOM 4.x.x / 5.x.x 串章号**。"
    "它是 FDA 给入境审查员/调查员的内部作业手册，非法规、不创设企业义务；`must`/`shall` 约束 FDA 内部作业，"
    "`should`/`as warranted`/`may` 属机构裁量（注意 `should only` / `should not` / `should … on all cases` 三类非机械映射）。"
    "凡本章与法规正文冲突以法规正文为准，企业不得以「IOM 没写」主张免责。2026 版是快照，"
    "PREDICT / OASIS / ITACS / eNSpect / ACE 与 WI-000618 / SOP-000217 等编号随改版失效，结论须回当前版本 IOM/RPM 与"
    "FD&C Act §801、21 CFR Part 1、19 CFR 113.62 复核。",
    "- 回答进口类问题时不得把 IOM Ch.6 的审查员动作、DER/DTR work type、30 天/90 天作业窗口写成企业法定义务或产品放行标准；"
    "不得把 `May Proceed` 读成「已判定合规」（系统定义是 No compliance decision has been made）、把 `Conditional Release` 读成"
    "「可分销」、把 `DWPE` 读成「不检查就放过」、把 `Refusal of Admission` 读成流程终点（档案到销毁/出口证明才关闭）。"
    "企业侧迎检举证内容一律冠〔推导·非原书主张〕，不代写 Notice / 766 / 483 回复等正式法律文书，不出合规结论，不预测个案结果。",
    "- **483 / 483a 分流硬规则**：`FDA 483a`（FSVP Observations，IOM 6.8，只在 closeout 签发、只签已签名版、检查期间不得展示草稿）"
    "归 **CAP-29 / V08**；`FDA 483`（现场检查观察项，IOM Ch.5，措辞纪律与 15 工作日回复骨架）归 **CAP-18**。"
    "二者数值同为 15 工作日但章节、文书、对象均不同，不得互套；FSVP 合规程序层（§1.500 FSVPI 主体、§1.5xx 条款、"
    "Import Alert 99-41 / Red List）另归 **CAP-21**；取样量、环境拭子、702(b) 分割留样归 **CAP-17 / CAP-28**。",
])
if not s.endswith("\n"):
    s += "\n"
s += boundary_add + "\n"
(PKG / "SKILL.md").write_text(s, encoding="utf-8")
note("[4] SKILL.md 完成 11 处精确更新（frontmatter / description / 路由表 / 边界）")

# ---------------------------------------------------------------- 5. test-prompts.json
tp_path = PKG / "test-prompts.json"
tp = json.loads(tp_path.read_text(encoding="utf-8"))
inc = json.loads((DIST / "test-prompts-increment.json").read_text(encoding="utf-8"))
assert tp["version"] == "4.16"
existing_ids = {c["id"] for c in tp["test_cases"]}
new_cases = [c for c in inc["test_cases"] if c["id"] not in existing_ids]
assert len(new_cases) == 13, f"新增用例应为 13 条，实际 {len(new_cases)}"
tp["version"] = "4.17"
tp["source_book"] += " + IOM 2026 Chapter 6: Imports（FDA 内部 SOP，v4.17 增量，CAP-29）"
tp["test_cases"].extend(new_cases)
if isinstance(tp.get("notes"), str):
    tp["notes"] += "；v4.17 追加 IOM Ch.6 进口判定链 13 条评测（含 3 条兄弟诱饵 + 2 条 router 可达用例），盲测见 books/iom-2026-ch6-imports/dist/test-results.md。"
tp_path.write_text(json.dumps(tp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
note(f"[5] test-prompts.json: version 4.17, cases {len(tp['test_cases'])} (+{len(new_cases)})")

# ---------------------------------------------------------------- 6. overview / glossary / cheatsheet 增量
ov_path = PKG / "references/overview.md"
ov = ov_path.read_text(encoding="utf-8")
ov += "\n\n---\n\n## v4.17 增量（2026-11-09）：第二十一来源 IOM 2026 Chapter 6 — Imports\n\n"
ov += "\n".join([
    "- **新增能力卡 CAP-29 `iom-imports-procedure`**（来源路由入口）+ `references/capabilities/imports/` 下 **10 张 RIA++ 子卡**。"
    "输入为 FDA《Investigations Operations Manual 2026》Chapter 6（70 页 / 235 书签 / 约 24 万字符），"
    "按 cangjie-skill RIA-TV++ 流水线蒸馏：5 个 extractor 并行得 82 条候选 → 去重 20 单元 → 三重验证通过 10 → "
    "晋级门全部判 router（1 个可发现入口服务 10 个能力单元）→ 压力测试 13 条盲测 96.7%。",
    "- **覆盖的 10 个能力单元**：入境审查决策门与可辩护留痕（V01）、DER/DTR 触发依据分流与 DWPE（V02）、"
    "Prior Notice 硬时限（V03）、条件放行/撤消/redelivery 时间窗（V04）、违规处置主链与文书矩阵（V05）、"
    "Form FDA 766 改标重整授权门（V06）、Failure to Hold 8 步调查（V07）、FSVP 检查链与 483a 签发门（V08）、"
    "进口状态概念区分树（V09）、IOM 效力层判读元规则（V10）。",
    "- **六类实质纠偏**：① `May Proceed` 是终局放行但「未作合规判定」，可被撤消且撤消不重开条件放行期；"
    "② `DWPE` 是「不检查就扣住」，DER/DTR 按触发依据而非严重度分流，查不到注册/510(k)/A of C 禁止直接建议扣留；"
    "③ `Failure to Hold` 是「无放行而分销」而非「移出港区」，货物 may be moved 合法；"
    "④ 三个「30 天」与一个「90 天」同数异义，DRQ/DTR/DER/DEF/INF 都不延长条件放行期；"
    "⑤ `Refusal of Admission` 不是终点，档案到销毁/出口证明才关闭；"
    "⑥ `FDA 483a`（FSVP 观察项，只在 closeout 签发）≠ `FDA 483`（Ch.5 现场检查观察项）。",
    "- **二十一类不可混引（v4.17 口径；v4.16 时为二十类）**：在二十类之外增加 **IOM 2026 Chapter 6**。"
    "引用写「IOM 6.x.x [p.N]」，与 IOM 4.x.x / 5.x.x 并列但章号不得串用；不得写成〔§ 117.xxx〕式法规引用。",
    "- **效力层**：IOM 是 FDA 内部操作指导、不是法规、不创设企业义务；`must`/`shall` 约束 FDA 内部作业，"
    "`should`/`as warranted`/`may` 属机构裁量；企业义务回 FD&C Act §801、21 CFR Part 1、19 CFR 113.62。"
    "全篇是监管者视角，企业侧迎检举证内容一律标〔推导·非原书主张〕。",
    "- **仍未收**：IOM Chapter 2 / 3 / 7 / 8 / 9 / 10 全本、RPM Chapter 9、CPG 全套、Import Alert / Import Bulletin 全文、"
    "21 CFR part 1 subpart L 正文、Exhibit 6-1~6-4 表单字段（扫描件，需查原件）。",
    "- **审计轨迹**：`E:/WeChatData/2026-11-09-08-58-24/books/iom-2026-ch6-imports/`（BOOK_OVERVIEW / candidates / "
    "verified / rejected / verified.yaml / destinations.json / GLOSSARY / DIGEST / test-results）。",
])
ov_path.write_text(ov, encoding="utf-8")
note("[6a] overview.md 追加 v4.17 增量段")

gl_path = PKG / "references/glossary.md"
gl = gl_path.read_text(encoding="utf-8")
gl += "\n\n---\n\n## v4.17 增量术语 — IOM 2026 Chapter 6: Imports（t234 起）\n\n"
gl += "\n".join([
    "> 完整词典见 `books/iom-2026-ch6-imports/GLOSSARY.md`（28 条）；此处收最易造成判定错误的高价值词条。",
    "",
    "| 术语 | IOM 定义（浓缩） | 出处 | 与常识的差异 / 混淆后果 |",
    "|---|---|---|---|",
    "| May Proceed | 电子审查后允许货物进入流通的放行决定 | IOM 6.9.56 [p.56]、6.4.3 [p.35] | 字面像「准许继续办理」，实为终局放行；且系统定义明写「未作合规判定」，误当已合规会免除后续责任 |",
    "| Conditional Release | 货物先交进口商控制但仍处 FDA 管辖、须保持可召回 | IOM 6.9.13 [p.51]、6.2.4 [p.20] | 不是「有条件合格」；货 may be moved 但不可分销，误判即 Failure to Hold |",
    "| Failure to Hold | 未获 FDA 放行即已分销货物 | IOM 6.6.4.1 [p.43]、6.9.30 [p.53] | 原文特意加 `*Please note` 强调「不是移出港区」；按位置判断违规会答错 |",
    "| DWPE | Detention Without Physical Examination，凭违规史/Import Alert 免实物查验即扣 | IOM 6.9.22 [p.52] | 「不检查」不是放过，恰是不检查就扣住；解除须至少一份 FDA 自采 audit sample，企业送检报告无效 |",
    "| DER / DTR | 审查员提交扣留建议的两种 work type：DER 用于受 DWPE 约束，DTR 用于其他 | IOM 6.2.5.1 [p.21] | 按**触发依据**分流，不是严重度分级；误当轻重档会走错通道 |",
    "| Detention / Refusal | Detention 是临时行政措施（基于 appear not to be），Refusal 是终局决定 | IOM 6.9.21 [p.52]、6.9.44 [p.55] | Refusal 仍非流程终点：档案到销毁/出口证明才关闭 |",
    "| Release with Comment | 已明确认定存在违规（无公共健康风险）仍放行，并预告后续同类 entry 可能被拒 | IOM 6.9.69 [p.57] | 与 May Proceed / Release / IB Release 是四种法律含义不同的放行，不可统一映射成「放行＝合规」 |",
    "| Prior Notice | 食品/饲料抵达前须经 FDA 电子**接收并确认**的独立法定前置义务 | IOM 6.1.5.1 [p.9]、6.1.5.5 [p.11] | 提交≠完成；15/30 天是上限、2/4/8 小时是下限，早报同样不合规；不能用报关单替代 |",
    "| Reconditioning / Relabeling | 在 FDA 批准并监督下使不合格品达可采状态（Form FDA 766） | IOM 6.5.2.3 [p.40]、6.9.65/6.9.68 [p.57] | 改标 ⊂ 重整；企业未经批准自行返工**不产生放行效力**；申请主体是 importer of record |",
    "| FDA 483a | FSVP Observations，只在检查结束 closeout 签发且只签已签名版 | IOM 6.8.2.1 [p.48-49] | **≠ FDA 483**（IOM Ch.5 现场检查观察项，CAP-18）；检查期间展示草稿被明文禁止 |",
    "| FSVP Importer / Importer of Record | 前者是 FSMA 供应商验证主体（须在美国境内），后者是 CBP 报关/bond 主体 | IOM 6.9.40 [p.55]、6.9.43 [p.55] | 两套法律身份，常非同一人；混淆会导致 766 申请主体与 bond 判断出错 |",
    "| IB | 同形异义：Import Bulletin（指示请求现场工作）vs Investigations Branch（IB Release 签发主体） | IOM 6.3.10.7 / 6.3.11 [p.32] | 误读会把现场放行当成进口公告 |",
    "",
    "> **源层瑕疵（如实标注）**：6.9 术语表共 78 条，末条编号 `6-9.78` 与前 77 条 `6.9.x` 不一致；"
    "6.9 未收 DER、IUC、Import Bulletin、SDI、VQIP 本体、IB Release，须回 6.1–6.8 取定义。"
    "另 `6.2.5.5` 的 reasonable effort 条款正文跨页落在 p.23（与 6.3 起始页重叠），引用按小节号而非分块文件名。",
])
gl_path.write_text(gl, encoding="utf-8")
note("[6b] glossary.md 追加 12 条 IOM Ch.6 高价值术语")

cs_path = PKG / "references/cheatsheet.md"
cs = cs_path.read_text(encoding="utf-8")
cs_row = (
    "| FDA 进口准入判定与处置链（IOM 2026 Chapter 6） | 先定状态词（Conditional Release 可移动**不可分销**、"
    "May Proceed 未作合规判定），再把 line 判入有限动作集；扣留建议按**触发依据**分 DER/DTR 而非严重度；"
    "一切倒计时先分清三个 30 天与一个 90 天；Detained→766→Refusal 后档案仍不关闭；"
    "Failure to Hold 看「有没有放行、有没有分销」而不是「货动没动」；⚠ 483a（FSVP）≠ 483（Ch.5）|\n"
)
marker = "\n> 速查只给结论"
assert marker in cs
cs = cs.replace(marker, "\n" + cs_row + marker, 1)
cs_path.write_text(cs, encoding="utf-8")
note("[6c] cheatsheet.md 追加 CAP-29 速查行")

# ---------------------------------------------------------------- 7. 校验
checks = []
checks.append(("SKILL.md capability-count", "cangjie.capability-count: 29" in (PKG / "SKILL.md").read_text(encoding="utf-8")))
s_final = (PKG / "SKILL.md").read_text(encoding="utf-8")
checks.append(("SKILL.md CAP-29 路由行", "| references/capabilities/iom-imports-procedure.md |" in s_final))
checks.append(("SKILL.md 二十一类", "**二十一类不可混引**" in s_final))
checks.append(("capability-index CAP-29", "| CAP-29 |" in (PKG / "references/capability-index.md").read_text(encoding="utf-8")))
checks.append(("入口卡存在", (CAP / "iom-imports-procedure.md").exists()))
checks.append(("10 张子卡存在", len(list((CAP / "imports").glob("*.md"))) == 10))
tp2 = json.loads((PKG / "test-prompts.json").read_text(encoding="utf-8"))
checks.append(("test-prompts v4.17 / 181 cases", tp2["version"] == "4.17" and len(tp2["test_cases"]) == 181))
# 相对引用可达性（路由表与索引中的 capabilities/ 路径）
for rel in ["references/capabilities/iom-imports-procedure.md"] + [
    f"references/capabilities/imports/{f.name}" for f in subcards
]:
    checks.append((f"路径可达 {rel.split('/')[-1]}", (PKG / rel).exists()))
failed = [n for n, ok in checks if not ok]
for n, ok in checks:
    print(("  OK  " if ok else " FAIL ") + n)
if failed:
    sys.exit("ABORT: 校验失败 -> " + ", ".join(failed))

note("[7] 全部校验通过：" + str(len(checks)) + " 项")
(ROOT / "books/iom-2026-ch6-imports/.cangjie/apply_v4.17_report.txt").write_text("\n".join(report), encoding="utf-8")
