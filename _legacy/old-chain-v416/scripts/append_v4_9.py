"""append_v4_9.py — v4.9 内容扩展：glossary t163–t172 + test-prompts seafood-01..10。

术语写法要点（与 v4.8 教训一致）：summary 若含 ASCII 双引号会破坏 YAML，
统一用 `|-` 块标量 + 不含 ASCII 双引号的正文，且缩进与既有条目一致。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

NEW_TERMS = """- id: t163
  title: fish 与 fishery product 的法定范围（§123.3(d)(e)）
  summary: >-
    〔§ 123.3(d)〕fish 含淡水与海水真骨鱼、甲壳类、其他水生动物（明列鳄鱼、蛙、水龟、水母、海参、海胆及其卵），
    明确不含鸟与哺乳动物，且包含全部软体动物，前提是供人食用；〔§ 123.3(e)〕fishery product 指以鱼为特征配料的
    任何人类食品。边界意义：鳄鱼、蛙腿、水龟等边缘物种属 part 123 管辖而非普通食品；但 birds 与 mammals
    （如养殖兔、鳄梨除外）不属 fish。判定顺序是先看物种是否落入 (d)、再看成品是否以鱼为特征配料。

- id: t164
  title: processing 的三项法定排除（§123.3(k)(2)）
  summary: >-
    〔§ 123.3(k)〕把 processing 定义为 handling、storing、preparing、heading、eviscerating、shucking、freezing、
    改变市场形态、manufacturing、preserving、packing、labeling、码头卸货与 holding 等；(k)(2) 明列三项不适用本 part：
    (i) 不从事其他加工的捕捞或运输、(ii) 仅为在捕捞船上暂存而进行的去头、去内脏或冷冻、(iii) 零售经营。
    这三项同时也是 §117.5(b) 豁免的边界之外——不在 processing 内的活动不属 part 123 管辖，因而不能主张
    「受 part 123 管辖所以免 Subparts C/G」，须回到 Part 117 自行判定。

- id: t165
  title: §123.5(a) 默认适用与 §117.5(b) 双向锁定
  summary: >-
    两处法条构成双向锁定：〔§ 123.5(a)〕原文 Except as provided by § 117.5(b), parts 110 and 117 of this chapter
    apply，即 Part 110 / 117 是默认适用、§117.5(b) 是唯一例外出口；〔§ 117.5(b)〕则规定 Subparts C and G 对受
    part 123 管辖的 activities 不适用，条件是 required to comply with 且 in compliance with part 123。
    推论：做水产品不等于只按 part 123 管；也不能因为「我们做 HACCP」就认为 PCHF 整体不适用。

- id: t166
  title: §117.5(b) 无限缩款——不得套用 part 113 的微生物限制
  summary: >-
    part 113 的豁免有〔§ 117.5(d)(2)〕追加限制：仅适用于 part 113 管辖的微生物危害。part 123 的〔§ 117.5(b)〕
    没有对应条款。因此两个方向都错：把 part 113 的「仅限微生物危害」搬过来会低估豁免范围（误以为化学、物理危害
    仍须 PCHF）；因为「没限缩」就推成整厂免检会高估豁免范围（忽略 activities 限定与 Subpart B 不在豁免内）。
    正确口径是「受 part 123 管辖的 activities 范围内的 Subparts C/G」。

- id: t167
  title: Subpart B / C 的 augments 语义与 §123.16 的例外只排一条
  summary: >-
    〔§ 123.15〕与〔§ 123.20〕都用 This subpart augments subpart A of this part 表述，即熏制熏味水产品与
    新鲜冷冻双壳软体动物的专项要求是叠加在 Subpart A 之上，不是另一套替代体系；漏 Subpart A 的 HACCP 计划、
    纠正措施、验证、记录、培训即为漏项。另需区分两种例外范围：〔§ 123.16〕的 except those subject to part 113 or 114
    只排除该条自身，Subpart A 全套义务仍适用；〔§ 123.20〕则是对「含足以杀灭公众健康意义微生物繁殖体处理的加工」
    整体不适用 Subpart C。

- id: t168
  title: HACCP 计划的九项危害考虑清单（§123.6(c)(1)）
  summary: >-
    〔§ 123.6(c)(1)〕要求列出按 (a) 识别的、须对每种水产品控制的 RTL 危害，并以 Consideration should be given to
    whether any food safety hazards are reasonably likely to occur as a result of the following 引出 (i)–(ix) 共 9 项：
    自然毒素、微生物污染、化学污染、农药、兽药残留、鲭鱼毒素种或其他种的分解、寄生虫、未经批准的直接或间接食品
    或着色添加剂使用、物理危害。措辞是 should be given 的考虑清单而非强制穷举，但漏考虑属危害分析缺陷；
    寄生虫项有三个触发条件（已知或应知将不经足以灭虫的工艺食用、声称、标示或意图如此食用）。

- id: t169
  title: 纠正措施三条路径与隔离扣留顺序（§123.7）
  summary: >-
    〔§ 123.7(a)〕给两个入口：(1) 按预先制定的纠正措施计划，或 (2) 按 (c) 程序。〔§ 123.7(b)〕的纠正措施计划
    须确保 No product enters commerce that is either injurious to health or is otherwise adulterated as a result of
    the deviation，并纠正偏差原因。〔§ 123.7(c)〕的顺序是：先按 (c)(1) Segregate and hold 隔离扣留 → (c)(2) 由
    具备适当培训或经验者评审可接受性（该培训 may or may not include §123.10 培训）→ (c)(3)(4) 必要时纠正产品与
    原因 → (c)(5) 由按 §123.10 培训者及时复审并必要时修改 HACCP 计划。跳过隔离直接放行是最常见的违规形态。

- id: t170
  title: 验证的两个时间硬指标——1 周复审与至少每年复审（§123.8）
  summary: >-
    〔§ 123.8(a)(3)(i)〕要求 CCP 监控记录的复审须在记录形成后 1 周内完成（This review shall occur within 1 week
    of the day that the records are made），(a)(3)(ii) 对纠正措施记录给同一时限；两项复审均须由按 §123.10 培训者
    签名并注明日期。(a)(1) 另要求 HACCP 计划在可能影响危害分析或改动计划的变更发生时及至少每年一次复审，
    且复审显示计划不再满足 §123.6(c) 时须立即修改。1 周是法条明文，不是内部 SOP 自定的建议值。

- id: t171
  title: 三套记录保存口径不可串用（§123.9 / §113.100 / §114.100）
  summary: >-
    part 123 按产品类型分档：〔§ 123.9(b)(1)〕冷藏产品自记录形成日起至少 1 年、冷冻保藏或货架稳定产品至少 2 年，
    存于加工场所或进口商美国营业地；(b)(2) 设备或工艺总体适宜性记录（含科学研究与评价结果）至少 2 年，起算点
    是从其对该产品的适用性；(b)(3) 季节性停产或船上偏远加工点存储受限时可在季末转移至其他合理可及地点，
    但须应要求立即归还；(f) 电子记录可接受但须有适当控制确保数据与签名完整性。对照：Part 113〔§ 113.100(g)〕
    是厂内至少 1 年加另存 2 年（1+2 分段）且 (h) 引 part 11；Part 114〔§ 114.100(e)〕是自生产日起整段 3 年、
    无分段、无 part 11 条款。三套写法互推即错，不得统一写成「法规要求 3 年」。

- id: t172
  title: §123.12 进口商验证与 FSVP 是双轨，及 Part 123 版本口径
  summary: >-
    〔§ 123.12〕是 part 123 自带的进口商义务：二选一为 (a)(1) 从与 FDA 有现行有效 MOU 的国家采购（须覆盖该产品、
    证明检查体系等效、准确反映现状、整体可执行）或 (a)(2) 建立并实施书面验证程序，程序至少列产品规格与
    (a)(2)(ii)(A)–(F) 中至少一项 affirmative step；(b) 可聘 competent third party 协助或代为执行、包括代写程序；
    (c) 保存英文记录；(d) 无等效保证即视为掺假并拒绝入境。该轨与 FSVP（21 CFR part 1 subpart L，法源 FD&C Act §805）
    是两套法源两套结构，可共用证据但互不替代；FSVP 的 deemed compliance 明文只免 FSVP 且保留 §1.509 义务，
    不覆盖 §123.12。版本口径：4-1-25 Edition 是 CFR 年度编纂版次而非 2025 新规，SOURCE 为 60 FR 65197 (1995-12-18)；
    CP 7303.842 海产品检查程序与 part 120、1240、108、110 正文仍未收，一律标转引未收；
    全包口径由 v4.8 十三类升为 v4.9 十四类不可混引。
"""

CASES = [
    dict(id="seafood-01", type="should_trigger",
         prompt="我们做烟熏三文鱼，厂长说按 21 CFR 123.16 控制肉毒就够，不用做完整 HACCP。这样对吗？",
         notes="考 §123.16 只是 Subpart A 之上的增量要求，且例外只排 part 113/114"),
    dict(id="seafood-02", type="should_trigger",
         prompt="水产品厂是不是只要符合 part 123 就免了 PCHF 的 Subparts C 和 G？",
         notes="考 §123.5(a) 默认适用 + §117.5(b) 双条件 + activities 限定"),
    dict(id="seafood-03", type="should_trigger",
         prompt="part 113 的豁免只限微生物危害，那水产品的 117.5(b) 是不是也只限微生物危害？",
         notes="考 §117.5(b) 无限缩款，两个方向误读都要纠正"),
    dict(id="seafood-04", type="should_trigger",
         prompt="21 CFR 123.9 的 HACCP 记录要保存几年？冷藏和冷冻一样吗？",
         notes="考 §123.9(b)(1) 冷藏 1 年 / 冷冻-保藏-货架稳定 2 年，及与 Part 113/114 三套口径的区别"),
    dict(id="seafood-05", type="should_trigger",
         prompt="进口冷冻虾，我们拿到了境外厂的 HACCP 计划副本，是不是 123.12 和 FSVP 都算满足了？",
         notes="考 §123.12 与 FSVP 双轨互不替代，deemed compliance 不覆盖 §123.12"),
    dict(id="seafood-06", type="should_trigger",
         prompt="生食牡蛎的 shellstock 容器上那个 tag 要写哪些内容？要不要保存记录？",
         notes="考 §123.28(c) tag 五要素 + §123.9(e) Tag 例外"),
    dict(id="seafood-07", type="should_trigger",
         prompt="CCP 监控记录最晚多久要有人复核签字？",
         notes="考 §123.8(a)(3)(i) 1 周内，以及计划至少每年复审"),
    dict(id="seafood-08", type="should_trigger",
         prompt="烟熏鱼偏离了关键限值，我们组长直接把产品放行了，说反正后面还要检。合规吗？",
         notes="考 §123.7(c)(1) 隔离扣留优先，及 (b)(1) 不得使不合格品进入商业"),
    dict(id="seafood-09", type="should_trigger",
         prompt="21 CFR 123 里 SSOP 写的是 should，是不是可以不建立？",
         notes="考 §123.11(a) should 与 (b)(c) shall 的措辞差异，不得升格也不得说可以不做"),
    dict(id="seafood-10", type="edge_case",
         prompt="我们厂既做烟熏鱼又做低酸罐头，HACCP 计划要不要分两套？肉毒控制按哪个法条？",
         notes="边界用例：part 123 与 part 113 交叉，§123.16 例外只排一条；应激活并分流到 CAP-22 与 CAP-20"),
]


def append_glossary(path: Path) -> int:
    t = path.read_text(encoding="utf-8")
    m = re.search(r"```ya?ml\n(.*?)\n```", t, re.S)
    assert m, "找不到 fenced yaml 块"
    body = m.group(1)
    assert "id: t163" not in body, "t163 已存在，勿重复追加"
    new_body = body.rstrip("\n") + "\n\n" + NEW_TERMS.rstrip("\n")
    t2 = t[:m.start(1)] + new_body + t[m.end(1):]
    path.write_text(t2, encoding="utf-8")
    return len(re.findall(r"^- id: t\d+", new_body, re.M))


def append_notes(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    anchor = "全库 162 条，v4.8。"
    assert t.count(anchor) == 1, t.count(anchor)
    add = (anchor + "\n\n- [x] 第十四来源 **21 CFR Part 123**（Fish and Fishery Products，4-1-25 Edition，9 页 / 13 条款）"
           "法规正文已并入，术语 t163–t172 共 10 条（fish 与 fishery product 范围、processing 三项排除、"
           "§123.5(a) 默认适用与 §117.5(b) 双向锁定、§117.5(b) 无限缩款、augments 语义与 §123.16 例外范围、"
           "九项危害考虑清单、纠正措施三条路径与隔离扣留顺序、1 周复审与每年复审、"
           "三套记录期口径不可串用、§123.12 与 FSVP 双轨及版本口径）；引文取自 CAP-22 R 段已逐字核验的 33 个英文引用块"
           "（32 条 Part 123 + 1 条 §117.5(b)）。原文标〔§ 123.xxx〕，CP 7303.842 与 part 120/1240/108/110 一律标"
           "『转引未收』。全库 **172 条**，v4.9。")
    path.write_text(t.replace(anchor, add, 1), encoding="utf-8")


def append_cases(path: Path) -> tuple[int, str]:
    d = json.loads(path.read_text(encoding="utf-8"))
    existing = {c["id"] for c in d["test_cases"]}
    for c in CASES:
        assert c["id"] not in existing, f"{c['id']} 已存在"
    d["test_cases"].extend(CASES)
    d["version"] = "4.9"
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return len(d["test_cases"]), d["version"]


def main() -> None:
    added = 0
    for gp in (BASE / "candidates/glossary.md", BASE / "GLOSSARY.md"):
        before = len(re.findall(r"^- id: t\d+", gp.read_text(encoding="utf-8"), re.M))
        assert before == 162, f"{gp.name}: 预期 162 条，实际 {before}"
        added = append_glossary(gp)
        after = len(re.findall(r"^- id: t\d+", gp.read_text(encoding="utf-8"), re.M))
        print(f"{gp.name}: {before} → {after} (+{added})")

    append_notes(BASE / "GLOSSARY.md")
    append_notes(BASE / "candidates/glossary.md")
    print("glossary 自检记录已追加 v4.9 段")

    n, ver = append_cases(BASE / "test-prompts.json")
    print(f"test-prompts.json: version={ver} cases={n}")


if __name__ == "__main__":
    main()