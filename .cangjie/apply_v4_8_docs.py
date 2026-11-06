"""apply_v4_8_docs.py — v4.8 状态文档回补（带唯一性断言、可回滚）

覆盖 PIPELINE_STATE.md / BOOK_OVERVIEW.md / DIGEST.md：
  - 登记第十三来源 CP 7303.878 与 CAP-21
  - 当前规模 21 卡 / 162 术语 / 95 用例 / 十三类来源 / dist-v12
  - 把「7303.878 未收」的旧边界改写为「正文已收、但 part 1 subpart L 与 99-41 全文未收」
  - 明确 v4.8 未重跑评测（v4.7 评测结论不得冒用）
  - 追加 v4.8 版本节

历史口径（v4.6 十类 / v4.7 十二类、当时的规模数字）作为演进记录保留，
只改「陈述当前状态」的句子。每个替换断言 count == 1，失败即抛错不落盘。
备份沿用 .cangjie/backup-v4-8-pre-revisions/（apply_v4_8_revisions.py 已建）。
"""
from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
BACKUP = BASE / ".cangjie" / "backup-v4-8-pre-revisions"

V48_PIPELINE = """

## v4.8：CP 7303.878 落为第十三来源 + FSVP 进口商检查分流卡（21 张卡）

- **触发与范围**：v4.7 收尾时 `G:/下载` 仍有 6 份暂缓资料，本轮用户提供 `CP7303.878 Foreign Supplier Verification Programs Inspections 508-Compliant.pdf`（33 页 / 20 书签）。按既有模式纳入为**第十三来源**并发布 v4.8；其余 5 份（Part 120 / 123、7303.842 / 7303.847 / 7303.819）本版仍不纳入。
- **转换**：`pdf2md-pro` 转出原始 75893 chars / 510 行 / 50 headings / 93 表格行 / 20 书签全命中 / 0 丢弃 / 残留独立页码 0；`.cangjie/finalize_cp_7303_878_source.py` 再删除 62 行重复页眉（`**Date of Issuance**`、`**Transmittal Number**`、机构名/项目名），写文件头后为 `source-cp-7303-878-2023.md`（82178 chars / 487 行 / 92 个 `<u>` 标签）。自检见 `.cangjie/cp-7303-878-convert-report.json`。
- **版本口径（第三次同类纠错）**：首页 `PROGRAM 7303.878` / `Transmittal Number: 2023-CPM-CFSAN-003` / `Implementation Date: 09/27/2023` / `Date of Issuance: 08/28/2025`。Change History 为 Initial Issuance 10/20/2021 → Update 09/27/2023（改名 FSVP Inspections、不把一般进口 operations 内容并入本 CP、补 Part II 程序交互与 Part V 执法流程）→ Pen/Ink 08/20/2024（FSPCA 链接、部分案件 direct reference authority、POC）→ **Corrections 08/28/2025（仅 CFSAN 重组后 POC 与机构名称/缩写）**。故本件是 **2023-09-27 版程序的 2025-08-28 更正版**，与 CP 7303.050 / 7303.070 同型，不同于 CPGM 7303.040 的 `2025-CPM-HFP-001` 新 Transmittal。另更正 `CP 7303.819`：是 2006 FY06-08 旧程序、已过 COMPLETION DATE 9/30/08 而非现行，准确说法不是「法规意义上废止」；本包仍未收其正文。
- **法源与主体分流（本轮核心）**：FSMA §301 增订 FD&C Act §805 → 2015-11 FSVP regulation `21 CFR part 1, subpart L（§§1.500–1.514）`，**正文本包未收，一律标「转引未收」**；它与 FD&C Act §418 / Part 117 Subpart G 是**两套法源、两类主体**：前者管进口商 **FSVPI**（§1.500 定义的美国货主/收货人，无美国货主时由签署同意书的美国代理/代表承担），后者管 receiving facility。CP PART II.3.A 的 deemed compliance 只覆盖同时为 manufacturer/processor 且符合 Part 117 / 507 供应链要求者，且原文 `except they must comply with section 1.509` 把每一 entry line 的 UFI/DUNS 电子申报义务单独留下。
- **其余核出的实质口径**：§1.502(a) 对每一种食品 develop, maintain, and follow FSVP；standard requirements §1.502/1.503/1.504/1.505/1.506/1.508/1.509/1.510 与 modified requirements §1.507/1.511/1.512/1.513（满足 modified 条件者**可选择** standard）；§1.501(b)–(h) 八类豁免；**`Samples will not be collected as part of an FSVP inspection.`** 且 PART IV 四节 Intentionally Left Blank——不得套 CP 7303.050 的样品量与环境拭子；483a 观察分级 → NAI/VAI/OAI → Warning Letter / Import Alert 99-41 / §801(a)(3) 拒绝入境，§301(zz) 为禁止行为；**Import Alert 99-41 与 CP 7303.070 的 99-37/99-38 不是同一个 Alert**，99-41 按「具体食品 + 具体境外供应商组合」列 Red List，未上 Red List 不等于自动禁运，移除须先提交证据；§1.507 disclosure 不能替代 §801(b)/§1.95 reconditioning proposal 资料；direct reference authority 仅在有限情形授予，首次违法不默认优先执法。
- **设计决策**：新增 **CAP-21 `fsvp-inspection-program`**，不并入 CAP-07 `supply-chain-verification`——两者法源、主体不同，且 CAP-21 还承载进口商检查、483a 分级、99-41 加/删名单与拒绝入境阶梯。CAP-21 六段完整，R 段 **46 个英文引用块 46/46 逐字命中**（`.cangjie/verify_fsvp_quotes.py`；初版 `strip_markup()` 只剥 `</?u>` 导致 Change History 表格 `<br>` 残留而 46 MISS，改为 `re.sub(r"<[^>]+>", "", s)` 后全中），B1–B12 边界齐备；meta 数字形 keyword（`"1.500"` / `"03878"`）全加引号，`yaml.safe_load` 类型检查 problems 0。
- **改动清单**：`assemble_bundle.py` docstring 20→21 张、SLUGS +`fsvp-inspection-program`、ALSO_READ 正向 7 条 + 反向 6 张卡、登记 `src-fda-cp-7303-878-2023`、entry.description +FSVP 段、core_principles 37→40（+3）、out_of_scope 6→7、stop_conditions 14→16、全局「十二类→十三类」「20 张→21 张」；`.cangjie/apply_v4_8_revisions.py` 带唯一性断言回补 **8 张既有卡 + 3 个来源文件头**（第一次因非唯一锚点失败，从 `.cangjie/backup-v4-8-pre-revisions/` 回滚 12 个文件后修复重跑成功）；`.cangjie/append_v4_8.py` 写 glossary t153–t162（**162 条**）与 `fsvp-01..10`（**95 条**用例，v4.8）；`PIPELINE_STATE.md` / `BOOK_OVERVIEW.md` / `DIGEST.md` 由本脚本同步。
- **QA 附带修复（基线问题，非 v4.8 回归）**：glossary fenced YAML 块长期有 7 行 `summary` 因「整段双引号包裹 + 内部未转义 ASCII 双引号」而无法 `yaml.safe_load`（v4.7 备份复核确认）；`.cangjie/fix_glossary_yaml.py` 把这 7 行改写为内容逐字保留的 `|-` 块标量后，全块严格解析通过、**162 条 id 唯一**、t153–t162 齐备。该 fenced 块是 markdown 交付物，编译/官方校验本就不解析它，故不影响此前各版 0 errors 的结论。
- **口径残留判定**：`test-prompts.json` 顶层 notes 中 2 处「十二类」是**描述 v4.7 当时状态**的历史记录，保留不改；v4.8 段已写明「全包十三类不可混引」。`build_v4_7_eval_suites.py` 中 1 处「十二类」是 v4.7 输出评测的断言字符串，属历史评测套件，不随版本改写。
- **仍未收**：21 CFR part 1 subpart L（§§1.500–1.514）正文、Import Alert 99-41 全文、FSVP Guidance for Industry、IP guidance tabs / Implementation Work Instructions、HFP Enforcement Bulletin #13/#6、RPM 4-1-8、CP 7303.819 / 7303.842 / 7303.847 正文、21 CFR part 108 / 110 / 120 / 123 / 507 正文、IOM Ch.4、BAM / CPG 全套、F0/D/z 计算与卷边解剖判读。本次关闭的是「FSVP 轨道与 Part 117 供应链程序分流、进口商检查取证清单、483a 分级与 99-41 阶梯」，**不是** FSVP 法规条文级义务。
- **评测状态**：本版**未重跑**触发 / 输出 / 路由评测；v4.7 的 F1 1.000（首次盲测）、F1 0.994（增强触发 103×3）、输出 10/10、路由 40/40 均为上一版本结论，10 条 `fsvp-*` 用例与 CAP-21 的路由正确性待后续补测。
- **编译产物**：`dist-v12`，安装后官方 `validate_skill_pack.py` **0 errors / 0 warnings**；旧版备份 `backups/fda-pchf-food-safety-v4.7-*`；已安装到 `C:/Users/HG/.workbuddy/skills/fda-pchf-food-safety`。
"""

V48_OVERVIEW = """

## 版本补充说明（v4.8，第十三来源：CP 7303.878 FSVP 检查程序）

本版把 **FDA Compliance Program 7303.878《Foreign Supplier Verification Programs Inspections》** 纳入为第十三来源，全文见 `source-cp-7303-878-2023.md`，对应第 21 张能力卡 **`fsvp-inspection-program`（CAP-21）**。PDF 首页 `Transmittal Number: 2023-CPM-CFSAN-003` / `Implementation Date: 09/27/2023` / `Date of Issuance: 08/28/2025`；Change History 显示 2025 条目**只改 POC 与机构名称缩写**，故本件是 **2023-09-27 版程序的 2025-08-28 更正版**，不是 2025 新 program，也不是 CPGM 7303.040 那种新 Transmittal 形态。33 页 / 20 书签全命中，转换后清除 62 行重复页眉。

**它是什么、不是什么**：这是 FDA 给检查员、进口分区合规官与中心审评人员的**内部作业指导**（`provides instruction to field staff`），标注「CP 7303.878 PART x」，**不创设企业义务**。真正创设义务的是 FSMA §301 增订的 FD&C Act §805 与其下的 **21 CFR part 1, subpart L（§§1.500–1.514）FSVP 法规**——**该法规正文本包未收，一律标「转引未收」**，不得从 CP 的检查动作反推条文。引用时四层要分开：法规义务〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕｜FSVP 法规「21 CFR part 1 subpart L §1.5xx（转引未收）」｜CP 内容「CP 7303.878 PART x」｜其余 program 各自章号。

**与 Part 117 Subpart G 的分流（本卡价值所在）**：两套法源、两类主体——FD&C Act §805 / part 1 subpart L 管进口商 **FSVPI**（§1.500 定义：入境时的美国货主/收货人；无美国货主时由签署同意书的美国代理/代表承担），FD&C Act §418 / Part 117 Subpart G 管 **receiving facility**。CP PART II.3.A 的 **deemed compliance** 仅在进口商同时为 manufacturer/processor 且符合 Part 117 / 507 供应链要求时成立，且原文 `except they must comply with section 1.509` 把**每一 entry line 报关时电子提供名称、邮箱与 UFI（FDA 认可 DUNS）**的义务单独留下；纯贸易进口商没有该通道。回答「已做 Part 117 供应链验证，还要不要做 FSVP」必须先问主体身份，不能二值合并。

**检查口径与执法阶梯**：§1.502(a) 对每一种食品 develop, maintain, and follow FSVP；standard requirements（§1.502/1.503/1.504/1.505/1.506/1.508/1.509/1.510）与 modified requirements（§1.507/1.511/1.512/1.513）是**可选关系**（满足 modified 条件者仍可选择 standard），不是「少做一套」；§1.501(b)–(h) 八类豁免。CP PART III.1.C 明写 **`Samples will not be collected as part of an FSVP inspection.`**、PART IV 四节 Intentionally Left Blank——FSVP 检查查 FSVP、危害分析、供应商批准评价、验证活动、§1.509 与纠正措施**记录**，不得套 CP 7303.050 的 subs 样品量与环境拭子。PART V 给 483a 观察分级 → NAI/VAI/OAI → Warning Letter / **Import Alert 99-41** / FD&C Act §801(a)(3) 拒绝入境（§301(zz) 禁止行为）。⚠ **99-41 是 FSVP 不合规进口商名单，不是 CP 7303.070 的 99-37 / 99-38**（LACF/AF 备案与过程控制）；99-41 按「具体食品 + 具体境外供应商组合」列 Red List，未列组合在不受其他 Alert 约束时仍可进口，移除须按指示提交证据并先于再次进口；direct reference authority 仅在有限情形授予，首次违法不默认优先执法；§1.507 disclosure 不能替代 §801(b)/§1.95 整改提案资料。

**十三类不可混引**：21 CFR Part 117 / PCHF 行业指南 / L.mono Draft Guidance / SECG / 过敏原 Ed.5 / Food Defect Levels Handbook / CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / 21 CFR Part 113 / 21 CFR Part 114 / **CP 7303.878**。检查员作业指导一律不创设企业义务；shall/must 的法定义务只回法规正文。

**仍未收**：21 CFR part 1 subpart L 正文、Import Alert 99-41 全文、FSVP Guidance 与 IP guidance tabs、HFP Enforcement Bulletin #13/#6、RPM 4-1-8、CP 7303.819 / 7303.842 / 7303.847 正文、21 CFR part 108 / 110 / 120 / 123 / 507 正文、IOM Ch.4、BAM / CPG 全套。v4.8 **未重跑**触发 / 输出 / 路由评测，v4.7 的评测结论不得冒用。

**当前规模**：21 张能力卡 / 162 条术语 / 95 条测试用例 / 十三类来源（v4.8，dist-v12）。
"""


_STATE: dict[Path, str] = {}


def replace_one(path: Path, old: str, new: str, label: str) -> None:
    """先改内存副本；全部断言通过后由 flush() 一次性写盘，避免半改状态。"""
    t = _STATE.setdefault(path, path.read_text(encoding="utf-8"))
    n = t.count(old)
    assert n == 1, f"{path.name} [{label}]: expected 1 hit, got {n}: {old[:70]!r}"
    _STATE[path] = t.replace(old, new, 1)
    print(f"  {path.name:22s} {label}: ok")


def append_one(path: Path, text: str, label: str) -> None:
    t = _STATE.setdefault(path, path.read_text(encoding="utf-8"))
    _STATE[path] = t + text
    print(f"  {path.name:22s} {label}: ok")


def flush() -> None:
    for p, t in _STATE.items():
        p.write_text(t, encoding="utf-8")
    print(f"flushed {len(_STATE)} files")


def main() -> None:
    ps = BASE / "PIPELINE_STATE.md"
    bo = BASE / "BOOK_OVERVIEW.md"
    dg = BASE / "DIGEST.md"
    for p in (ps, bo, dg):
        assert p.exists(), p
    assert BACKUP.is_dir(), "缺 v4.8 前置备份目录"

    # 本次改前的当前态快照：任一唯一性断言失败时可整体回滚，避免半改状态
    import shutil
    snap = BASE / ".cangjie" / "backup-v4-8-pre-docs"
    snap.mkdir(parents=True, exist_ok=True)
    for p in (ps, bo, dg):
        shutil.copyfile(p, snap / p.name)
    print(f"pre-doc snapshot: {snap}")

    # ---- PIPELINE_STATE ----
    replace_one(
        ps,
        "- **输出模式**: single（用户已确认，全书均衡提取；十二次来源合并均沿用 single，未改变产物形态）",
        "- **第十三来源**: books/fda-pchf-human-food-guidance/source-cp-7303-878-2023.md（FDA CP 7303.878《Foreign Supplier Verification Programs Inspections》，**Transmittal 2023-CPM-CFSAN-003 / Implementation Date 09/27/2023 / Date of Issuance 08/28/2025 更正**，33 页 / 20 书签；用户提供的 508-Compliant PDF 经 `pdf2md-pro` 转换。是 2023 版程序的 2025 更正本，不是 2025 新 program；其依据的 **21 CFR part 1, subpart L（§§1.500–1.514）法规正文仍未收**，一律标「转引未收」，见 CAP-21 `fsvp-inspection-program`）\n"
        "- **输出模式**: single（用户已确认，全书均衡提取；十三次来源合并均沿用 single，未改变产物形态）",
        "登记第十三来源",
    )
    replace_one(
        ps,
        "- **当前版本**: v4.7 ✅ 全部完成，已安装到用户级技能目录（20 张卡 / 152 术语 / 85 用例 / 十二类来源）",
        "- **当前版本**: v4.8 ✅ 全部完成，已安装到用户级技能目录（21 张卡 / 162 术语 / 95 用例 / 十三类来源 / dist-v12）",
        "当前版本",
    )
    replace_one(
        ps,
        "当前为 **v4.7：20 张卡 / 152 术语 / 85 用例 / 十二类来源 / dist-v11**，见本文件顶部与末尾 v4.7 节；v4.6 的 19 卡",
        "当前为 **v4.8：21 张卡 / 162 术语 / 95 用例 / 十三类来源 / dist-v12**，见本文件顶部与末尾 v4.8 节；v4.7 的 20 卡 / 152 术语 / 85 用例 / 十二类来源 / dist-v11、v4.6 的 19 卡",
        "阶段快照注",
    )
    replace_one(
        ps,
        "## 已知边界（未关闭）\n- **评测状态（v4.7 全部补跑完成）**",
        "## 已知边界（未关闭）\n"
        "- **v4.8 评测状态**：本版**未重跑**触发 / 输出 / 路由评测；v4.7 的 F1 1.000（首次盲测）、F1 0.994（增强触发 103×3）、输出 10/10、路由 40/40 均属**上一版本**结论，不得当作 v4.8 结果。新增 10 条 `fsvp-*` 用例与 CAP-21 的路由正确性待后续补测。\n"
        "- **评测状态（v4.7 全部补跑完成）**",
        "已知边界评测状态",
    )
    replace_one(
        ps,
        "其他 Compliance Programs（7303.878 FSVP / 7303.080 Produce Safety / 7304.019 / 7303.842 海产品 / 7371.000 动物食品 / 7321.006 婴儿配方等）、Import Alerts",
        "其他 Compliance Programs（**7303.878 FSVP 正文自 v4.8 起已收（CAP-21），但其依据的 21 CFR part 1 subpart L 与 Import Alert 99-41 全文仍未收** / 7303.080 Produce Safety / 7304.019 / 7303.842 海产品 / 7371.000 动物食品 / 7321.006 婴儿配方等）、Import Alerts",
        "已知边界 7303.878 收窄",
    )
    append_one(ps, V48_PIPELINE, "追加 v4.8 版本节")

    # ---- BOOK_OVERVIEW ----
    replace_one(
        bo,
        "全包 v4.6 时为「十类不可混引」、**v4.7 起扩为「十二类不可混引」**（新增两套法规正文，见下节）；",
        "全包 v4.6 时为「十类不可混引」、v4.7 扩为「十二类不可混引」（新增两套法规正文）、**v4.8 起扩为「十三类不可混引」**（新增 CP 7303.878 检查程序，见文末节）；",
        "v4.6 节分层口径",
    )
    replace_one(
        bo,
        "**当前规模见下节 v4.7**。",
        "**当前规模见文末 v4.8 节**。",
        "v4.6 节当前规模指引",
    )
    replace_one(
        bo,
        "全包自 v4.7 起统一「**十二类不可混引**」；检查员作业指导（CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070）不创设企业义务",
        "全包 v4.7 时统一「十二类不可混引」、**v4.8 起统一「十三类不可混引」**；检查员作业指导（CPGM 7303.040 / CP 7303.050 / IOM 2026 Ch.5 / CP 7303.070 / CP 7303.878）不创设企业义务",
        "v4.7 节分层口径",
    )
    replace_one(
        bo,
        "其余 Compliance Programs（7303.878 / 7303.842 / 7303.847 等）、Form 2541e 细则。",
        "其余 Compliance Programs（7303.842 / 7303.847 / 7303.819 等；**7303.878 已由 v4.8 收入**）、Form 2541e 细则。",
        "v4.7 节仍未收清单",
    )
    replace_one(
        bo,
        "**当前规模**：20 张能力卡 / 152 条术语 / 85 条测试用例（v4.7）。",
        "**当时规模**：20 张能力卡 / 152 条术语 / 85 条测试用例（v4.7）；**当前规模见下节 v4.8**。",
        "v4.7 节规模",
    )
    append_one(bo, V48_OVERVIEW, "追加 v4.8 版本节")

    # ---- DIGEST ----
    replace_one(
        dg,
        "当前为 **v4.7：20 张能力卡 / 152 条术语 / 85 条测试用例 / 十二类来源**",
        "当前为 **v4.8：21 张能力卡 / 162 条术语 / 95 条测试用例 / 十三类来源**",
        "当前状态",
    )
    replace_one(
        dg,
        "迎检链与法条卡合起来才回答 LACF/AF 的完整合规与迎检问题。",
        "迎检链与法条卡合起来才回答 LACF/AF 的完整合规与迎检问题。\n\n"
        "**v4.8 再加第六张 `fsvp-inspection-program`（CAP-21）**：纳入第十三来源 FDA CP 7303.878《Foreign Supplier Verification Programs Inspections》（2023-09-27 版程序 / 2025-08-28 更正，不是 2025 新 program），把**进口轨道**从企业侧供应链验证中分出来。核心是两套法源、两类主体：FD&C Act §805 / `21 CFR part 1, subpart L（§§1.500–1.514）` 管进口商 **FSVPI**，FD&C Act §418 / Part 117 Subpart G 管 receiving facility；deemed compliance 只覆盖前者且 `except they must comply with section 1.509`（每一 entry line 的 UFI/DUNS 电子申报不豁免）。FSVP 检查**不取样**（PART IV 四节 Intentionally Left Blank），不得套 7303.050 的样品量与环境拭子；483a 观察分级 → NAI/VAI/OAI → Warning Letter / **Import Alert 99-41**（与 7303.070 的 99-37/99-38 不是同一个 Alert）/ §801(a)(3) 拒绝入境。**21 CFR part 1 subpart L 法规正文本包未收**，一律标「转引未收」，CP 是检查员内部作业指导、不创设企业义务。自此全包 **十三类不可混引 / 21 张卡 / 162 条术语 / 95 条用例**；v4.8 未重跑评测，v4.7 的 F1 与路由结论不得冒用。本版还修掉了 glossary fenced YAML 块自 v1 遗留的 7 行严格解析失败（内容逐字保留改为块标量，现 162 条可 `yaml.safe_load`）。",
        "追加 v4.8 段",
    )

    # ---- 收尾校验（内存态），全部通过后才一次性写盘 ----
    for p in (ps, bo, dg):
        t = _STATE[p]
        assert "v4.8" in t, f"{p.name} 未写入 v4.8"
    flush()
    print("\n三份状态文档 v4.8 回补完成")


if __name__ == "__main__":
    main()
