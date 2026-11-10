#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""apply_v4_10_residue.py — v4.10 第二轮口径回补 + 状态文档落盘。

首轮按「整行含版本标记则跳过」保护了历史陈述，但也漏掉了一批**当前口径长行**
（B 段引用规范、Step 收尾声明、卡开头来源分层），因其行尾带 v4.9 注记。
本轮做更细粒度的替换，只改「十四类不可混引」这一固定短语，并保留/补写版本注记。
"""
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CARDS = BASE / ".cangjie/capabilities/cards"
pending = {}
log = []


def stage(p, t):
    pending[p] = t


def rep_exact(p, old, new, label, count=1):
    t = pending.get(p) or p.read_text(encoding="utf-8")
    n = t.count(old)
    assert n == count, f"[{label}] 期望 {count} 处，实得 {n}：{old[:80]!r}"
    stage(p, t.replace(old, new))
    log.append((p.name, label))


# ---------------------------------------------------- 1. 能力卡逐行细粒度替换
HARD_SKIP = ("升为", "→", "初版", "快照", "当时", "v4.9 口径；", "（v4.9 口径",
             "十三类升为", "第十四类", "第十三类")
for p in sorted(CARDS.glob("*.md")):
    if p.name == "seafood-hazards-controls-guide.md":
        continue  # 新卡已是十五类
    t = p.read_text(encoding="utf-8")
    lines = t.splitlines(keepends=True)
    n = 0
    for i, line in enumerate(lines):
        if "十四类不可混引" not in line or any(k in line for k in HARD_SKIP):
            continue
        new = line
        if "十四类不可混引，v4.9" in new:
            new = new.replace("十四类不可混引，v4.9", "十五类不可混引，v4.9 时为十四类")
        elif "十四类不可混引，v4.8" in new:
            new = new.replace("十四类不可混引，v4.8", "十五类不可混引，v4.8 时为十三类")
        else:
            new = new.replace("十四类不可混引", "十五类不可混引")
        lines[i] = new
        n += 1
    if n:
        stage(p, "".join(lines))
        log.append((p.name, f"行级替换 {n} 处"))

# cgmp 卡开头的「v4.8 起全包统一「十四类不可混引」」是 v4.9 遗留的错误版本陈述，单独修
cg = CARDS / "cgmp-compliance-guide.md"
rep_exact(cg,
          "v4.8 起全包统一「十四类不可混引」",
          "v4.10 起全包统一「十五类不可混引」（v4.8 时为十三类）",
          "cgmp 开头来源分层版本陈述")

# FSVP 卡 B11 的来源清单补第十五来源
fs = CARDS / "fsvp-inspection-program.md"
rep_exact(fs,
          "CP 7303.878。检查员作业指导一律不创设企业义务",
          "CP 7303.878 / **FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版 June 2022（第十五来源，CAP-23）**。检查员作业指导一律不创设企业义务",
          "FSVP B11 补第十五来源")

# ---------------------------------------------------- 2. 当前版本行
PS = BASE / "PIPELINE_STATE.md"
rep_exact(PS,
          "- **当前版本**: v4.9 ✅ 编译校验并安装完成（22 张卡 / 172 术语 / 105 用例 / 十四类来源 / dist-v13）",
          "- **当前版本**: v4.10 ✅ 编译校验并安装完成（23 张卡 / 182 术语 / 115 用例 / 十五类来源 / dist-v14）",
          "PIPELINE_STATE 当前版本")
rep_exact(PS,
          "当前为 **v4.9：22 张卡 / 172 术语 / 105 用例 / 十四类来源 / dist-v13**",
          "当前为 **v4.10：23 张卡 / 182 术语 / 115 用例 / 十五类来源 / dist-v14**",
          "PIPELINE_STATE 快照说明")

BO = BASE / "BOOK_OVERVIEW.md"
rep_exact(BO,
          "**规模**：22 张能力卡 / 172 条术语 / 105 条测试用例 / **十四类来源**（v4.9）。",
          "**规模（v4.9 历史快照）**：22 张能力卡 / 172 条术语 / 105 条测试用例 / **十四类来源**（v4.9）。**当前 v4.10 为 23 张能力卡 / 182 条术语 / 115 条测试用例 / 十五类来源 / dist-v14**，见文末 v4.10 节。",
          "BOOK_OVERVIEW 规模行")

DG = BASE / "DIGEST.md"
rep_exact(DG,
          "当前为 **v4.9：22 张能力卡 / 172 条术语 / 105 条测试用例 / 十四类来源**",
          "当前为 **v4.10：23 张能力卡 / 182 条术语 / 115 条测试用例 / 十五类来源**",
          "DIGEST 当前版本行")

# ---------------------------------------------------- 3. 状态文档追加 v4.10 段
V410_PS = """

## v4.10 — 海产品危害分析判定链（FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版，June 2022）

- **新增来源（第十五类）**：`source-seafood-hazards-guide-2022.md` — FDA《Fish and Fishery Products Hazards and Controls Guidance》**第 4 版 June 2022**（SGR 129）。来源为 WorkBuddy 资料库节点 `XMsRyrFL0wM1hesg8X6K9u`，因内联读取报「大载荷不走内联代理」而改走 `export/export_node.py` 导出通道取得全文（1,709,446 字节 / 31,321 行）。落地文件含导入说明：非约束性定位、与 Part 123 法条层的分工、分章滚动修订的版本口径、以及导出件转换质量红线。**封面 June 2022，但 Ch.3 页脚 `3 - 1 (June 2021)`、Appendix 3 为 `A3-1 (June 2021)`、Appendix 5 为 `A5-1 (June 2021)`、Ch.19 书目 August 2019** —— 是分章滚动修订，不是 2022 新规。
- **本件填补的缺口**：v4.9 段「仍未收」清单里点名的 `FDA Fish and Fishery Products Hazards and Controls Guidance 4th ed.`。已收的 Part 123（CAP-22）是**法条义务层**，本件是配套的**技术指南层**（how to 判定），两者配对而非合并。核对确认：本地 `source.md` 是另一份（PCHF 行业指南草案 October 2026），与本件无重复。
- **cangjie 流水线（阶段 0–5，沿用 single 模式，不另起技能包）**：阶段 0 产出 `BOOK_OVERVIEW-seafood-hazards-guide-2022.md`（与既有第一来源 BOOK_OVERVIEW.md 并列，不覆盖），含 Adler 四步、7 条关键术语、4 组批判、转换质量红线；阶段 1 并行 5 路提取，审计轨迹留在 `candidates/v4-10-{framework,principles,cases,counter-examples,glossary}.md`（框架 8 / 原则 10 / 案例 11 / 反例 14 / 术语 15 条）；阶段 1.5 全部通过三重验证；阶段 1.6 **不晋级独立 Skill**，全部经唯一入口路由（与 v4.9 一致）；阶段 2–4 产出能力卡、also_read、术语与评测用例；阶段 5 编译交付。
- **新增能力卡 CAP-23**：`seafood-hazards-controls-guide`，importance `extended`，also_read 9 条（与 CAP-22 / hazard-analysis-method / chemical-hazard-controls / process-control-validation / allergen-program / regulatory-boundaries / inspection-sampling / cgmp-compliance-guide / reference-tools-discipline 双向链）。用户明确要求「**完整危害分析判定链**」，主干为：产品描述与流程图 → Ch.3 三表识别品种相关（Table 3-2/3-3）与工艺相关（Table 3-4）潜在危害 → Ch.4–21 理解危害 → 在**无控制条件下**按 `reasonably likely to occur` 逐步判显著性 → 第 3/4 栏 Yes/No 都写理由 → Step 11 判定树定 CCP → 选控制策略示例 → 定关键限值与监控四问 → 纠正/记录/验证。A2 32 条触发、B1–B12 边界、E 段 Step 1–8 含六栏工作表 ↔ 十栏计划表映射。
- **引文核对（独立复核，非自证）**：`.cangjie/verify_v4_10_quotes.py` 用 `body_only()` 只取源文件「## 正文（导出原文，未改写）」之后的文本，避免文件头自我验证循环（v4.9 `verify_seafood_quotes.py` 的教训）。R 段 **37 个英文引用块 37/37 逐字命中**，0 超 100 词，0 表格/页眉/残表引用。表格列头连写（`MARKETNAMES`）、词条粘连（`ALFONSINOALFONSINO`）、字符丢失（`fsh` / `Pufer`）、页码混入单元格、Appendix 3 的 CCP 判定树塌陷成残表，均已写入源文件导入说明与本卡 B 段红线。
- **关键口径（三处最易误读）**：① `should` 仅为建议、指南不设可执行责任、可另选控制策略与关键限值但须科学论证其充分性；② Ch.3 表**不得单独使用**、指南不替代〔§ 123.6〕危害分析、须警觉新出现危害与物种替换；③ **双向防误读**——既不把指南/Appendix 5 数值（组胺 50/500 ppm 回指 CPG Sec. 540.525，属转引未收）当合规清单或法定限值，也不因指南非强制就把 Part 123 的 `shall` 义务稀释成可选。Appendix 5 的限值是外部法源快照，不是 FDA 在本指南新设的限值。
- **规模变化**：22 → **23 张卡**；172 → **182 条术语**（t173–t182，围绕判定链排布）；105 → **115 条用例**（`seafood-hazards-01..10`，9 正/边界 + 1 跨法域 should_not_trigger）；十四类 → **十五类来源**；core_principles 42 → **45**；stop_conditions 18 → **20**；dist-v13 → **dist-v14**。
- **工程修复**：`.cangjie/assemble_bundle.py` 的 `BASE` 原硬编码原开发机路径 `E:/WeChatData/...`，本机无法运行；改为 `Path(__file__).resolve().parents[1]` 相对推导，任何机器可跑。`verified.yaml` / `destinations.json` / `book/` 仍是脚本生成物，未手改。
- **口径回补的两轮策略（沿用 v4.9 教训）**：第一轮 `apply_v4_10_revisions.py` 用精确替换 + 「整行含版本标记则跳过」保护历史陈述（**「第十四类」含「十四类」子串、历史编译记录里的「22 张」若全局替换会被污染**）；第二轮 `apply_v4_10_residue.py` 补掉一批行尾带 `v4.9` 注记的当前口径长行（各卡 B 段引用规范、Step 收尾、开头来源分层）。版本阶梯陈述（v4.6 十类 → v4.7 十二类 → v4.8 十三类 → v4.9 十四类 → v4.10 十五类）全部保留不改。
- **仍未收**：CP 7303.842 海产品检查程序正文、NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、Import Alert 16-xx 系列、BAM 海产品章节、CPG Sec. 540.525 / 555.300 / 575.100、21 CFR 556 系列、40 CFR 180 系列、Import Tolerance、组胺/河豚毒素/雪卡毒素检测方法。
- **评测状态**：本版**未重跑**触发 / 输出 / 路由评测；v4.7 的 F1 1.000 / 0.994、输出 10/10、路由 40/40 均为历史版本结论，**不得冒用**；10 条 `seafood-hazards-*` 用例与 CAP-23 路由正确性待后续补测。
- **编译产物**：`dist-v14`（`compile_single.py --bundle .cangjie/capabilities --out dist-v14 --variant single`，Bundle 原生确定性编译，无 run id；**28 个文件 / 28 个 .md / 23 张卡**）；官方 `validate_skill_pack.py` **0 errors + 1 warning**（`name-dir`：`dist-v14` 与 SKILL.md 的 `name` 不一致，属产物目录名固有提示）。SKILL.md 前 150 字符已含 PCHF / 21 CFR 117 / FSMA / 危害分析等核心触发词；description 共 4235 字符（v4.9 为 3857），超过 WorkBuddy 内置技能展示长度，按既有口径未擅自改动产物。
- **安装**：旧版备份 `../../.workbuddy/skills/backups/fda-pchf-food-safety-v4.9-20261106-201144`；已安装到工作区级 `.workbuddy/skills/fda-pchf-food-safety/`（`.cangjie/install_v10.py` 硬编码原开发机路径，仍采用等价的直接复制 + 逐文件 hash 校验）；产物与安装目录逐文件 sha256 差异 **0**；**5 份 glossary 副本 hash 全同**（`18eabcd564e9…`，182 条严格 `yaml.safe_load` 通过）；路由表 23 张卡全部命中且无孤立卡；`destinations.json` 23 个去向；全库「该指南仍未收」残留 **0**。完整审计见 `.cangjie/v4-10-sources-qa-report.json`。
"""
ps = pending.get(PS) or PS.read_text(encoding="utf-8")
assert "## v4.10 — 海产品危害分析判定链" not in ps
stage(PS, ps.rstrip("\n") + "\n" + V410_PS)

V410_BO = """

## v4.10 追加：第十五来源与第 23 张卡

> 本节是 v4.10 增量记录；上文各节的 v4.x 规模与「十四类不可混引」为**历史口径**，保留不改。

- **当前规模**：23 张能力卡 / 182 条术语 / 115 条测试用例 / **十五类来源** / `dist-v14`。
- **第十五来源**：FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版 June 2022（SGR 129），`source-seafood-hazards-guide-2022.md`。它是**非约束性技术指南层**，与第十四来源 21 CFR Part 123（法条义务层，CAP-22）配对而非合并：前者给「怎么判定」，后者给「必须做什么」。
- **新增能力卡 CAP-23 `seafood-hazards-controls-guide`**：完整危害分析判定链（Ch.3 三表识别 → Ch.4–21 理解危害 → 无控制条件下判 `reasonably likely to occur` → 六栏工作表 Yes/No 理由 → Step 11 判定树定 CCP → 控制策略示例 → 关键限值与监控四问）。R 段 37 个英文引用块经 `.cangjie/verify_v4_10_quotes.py` 逐字核验 37/37 命中。
- **十五类不可混引（v4.10 口径；v4.9 时为十四类）**：在上文十四类清单之外，增加 **FDA 海产品危害与控制指南第 4 版**。层次仍为：法规正文 ＞ FDA 指南 ＞ CPGM／CP／IOM 检查程序（仅检查员视角）。指南内引用写「Seafood Hazards Guide 第 4 版 Ch.x / Appendix x / L####」，法条写〔§ 123.xxx〕，不可互换。
- **仍未收**：CP 7303.842、NSSP Guide、21 CFR part 120 / 1240 / 108 / 110 / 507 正文、Import Alert 16-xx、BAM 海产品章节，以及 Appendix 5 回指的 CPG / 21 CFR 556 / 40 CFR 180 / Import Tolerance 等外部法源。涉及具体数值的条款级结论一律标「转引未收」。
- 阶段 0 整书理解见 `BOOK_OVERVIEW-seafood-hazards-guide-2022.md`；阶段 1 五路候选见 `candidates/v4-10-*.md`；完整变更与校验记录见 `PIPELINE_STATE.md` v4.10 段。
"""
bo = pending.get(BO) or BO.read_text(encoding="utf-8")
assert "## v4.10 追加：第十五来源" not in bo
stage(BO, bo.rstrip("\n") + "\n" + V410_BO)

V410_DG = """

> **版本说明（v4.10，2026-11-06 追加）**：技能包再合并第十五来源 FDA《Fish and Fishery Products Hazards and Controls Guidance》第 4 版 June 2022（SGR 129），新增第 23 张卡 `seafood-hazards-controls-guide`，专门承载**海产品完整危害分析判定链**。该指南是**非约束性**的配套技术指南层，与第十四来源 21 CFR Part 123 的**法条义务层**（CAP-22）配对而非合并：本文正文关于 PCHF / Part 117 的六列危害分析工作表、预防控制与管理组件属于**另一套框架**，不得套到海产品 HACCP 的 CCP / 关键限值体系上。当前规模 23 张卡 / 182 术语 / 115 用例 / **十五类来源不可混引** / dist-v14。本文正文仍保留第一来源的蒸馏结果不重写。
"""
dg = pending.get(DG) or DG.read_text(encoding="utf-8")
assert "版本说明（v4.10" not in dg
stage(DG, dg.rstrip("\n") + "\n" + V410_DG)

# ---------------------------------------------------- 落盘
for p, t in pending.items():
    p.write_text(t, encoding="utf-8")

print(f"touched files: {len(pending)}")
for name, label in log:
    print(f"  {name:<58} {label}")
print("APPLY_V4_10_RESIDUE_OK")
