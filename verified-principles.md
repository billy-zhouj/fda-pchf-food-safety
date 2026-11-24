# 验证通过的原则 — 三重验证产出（阶段 1.5）

> 输入：candidates/_stage1/principles-merged.md（93 个合并单元，来源 285 条原始候选）
> 验证基准：V1 跨域（≥2 独立语境，不同章节+不同对象）；V2 预测力（书外新场景可外推）；V3 独特性（超越通用食品安全常识的 FDA 特定规则/数值/判定逻辑）
> 结果：**74 / 93 通过**（80%）。通过率偏高的解释：本源文本为法规实操手册而非散文，分块提取器已自带操作规则过滤，且合并阶段吸收了大部分跨块重复。
> group 字段对应 10 个主题组（G1 危害分析方法 / G2 数值界限与工艺控制 / G3 管理组件 / G4 环境病原与卫生 / G5 过敏原 / G6 供应链 / G7 化学危害 / G8 召回 / G9 双法规管辖 / G10 附录工具纪律）

---

## G1 危害分析方法与书面判定纪律

```yaml
- id: pV-01
  title: 书面判定纪律——"No"与"Yes"同等重要
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch2 §2.3.2（六列工作表：第 4 列写 No 理由 + 保守列入）
      - Ch5 §5.1 / 117.130(a)(2)（无发现也必须书面记录判定）
      - Ch12 §12.8.1（化学危害"不需要控制"的依据须可供官方查阅复制）
      - 附录 1 A1.8.2（X 标记危害的 No 判定同样须解释理由）
  V2_predictive_power:
    passed: true
    novel_question: "检查员问'为什么你的花生酱厂没把 E. coli 列为需控危害'，没有书面理由会怎样？"
    derived_answer: "空白即漏洞——没有书面 No 理由等于没有做过该评估，危害分析整体可信度崩塌；书面理由把排除决定从'遗漏嫌疑'转为'已评估证据'"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'记录重要'；FDA 特定规则是：否定性判定承担与肯定性判定同等的书面举证义务，且争议项应保守列入再论证排除——这是对抗检查的程序设计而非文档习惯"
- id: pV-02
  title: FSP 动态文件：3 年再分析 + 四类事件触发
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch1 §1.7（117.170 法定要求与触发器总述）
      - Ch11 §11.5.5（过敏原各节再分析义务的总纲重述）
      - Ch12 §12.10（示例厂以季度检测数据支撑再分析）
  V2_predictive_power:
    passed: true
    novel_question: "公司换了新包装材料供应商，FSP 需要全部重写吗？"
    derived_answer: "不需要：重大变更触发的是'局部再分析'，可限于受影响部分；但若变更引入新危害可能则必须覆盖相应部分——双轨制（周期轨+事件轨）决定重写范围"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'定期复审'；FDA 特定的是 3 年硬周期 + 4 类明确触发事件 + '可限于相关部分'的裁剪规则——把动态维护法条化了"
- id: pV-03
  title: 偏差反复出现 = 程序无效 = 触发再分析
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch5 §5.5.3（关键限偏差频发→工艺与 FSP 再分析）
      - Ch11 §11.6.1.2/§11.7.4（清洁面反复检出残留、标签控制反复出问题→再分析）
      - Ch11 §11.8.6（供应商持续不合规→再分析供应链程序）
  V2_predictive_power:
    passed: true
    novel_question: "同一台封口机今年第 4 次校准超标，每次都重新校准了，还需要做什么？"
    derived_answer: "逐次 correction 已经失效：反复模式证明监控/校准程序本身无效，必须回溯历史纠正记录识别模式并对 FSP 相应部分再分析——继续逐次修机器是合规假象"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'别再犯'；FDA 判定逻辑是：重复本身就改变处理等级（correction→corrective action→再分析），孤立即与反复适用不同程序"
- id: pV-04
  title: 条件性升格——危害分析是状态机而非静态结论
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch12 §12.12（Miller C：常态 DON 走 CGMP，触发信息出现即升格为预防控制）
      - Ch12 §12.13（Baker D：同样的条件性结论 + 采购协议触发条款）
      - Ch12 §12.14（Sandwich F：链条下游凭逐级审查获得条件性保证）
  V2_predictive_power:
    passed: true
    novel_question: "采购的辣椒粉今年产区大旱，原本走 CGMP 的霉菌毒素危害要升级吗？"
    derived_answer: "是——按 DON 模式：异常环境信息=升格触发器，原有清洗/分选程序立即按预防控制运行（配监控/验证/纠正/记录），信息恢复后再降格。危害分析结论带触发条件写入 FSP"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'情况变了再改'；FDA 特定的是把'何种信息触发升格'预先写成危害分析结论的一部分（新粮首检/产区周报/检出率），控制状态随信息流自动切换"
- id: pV-05
  title: hazard 的法定边界——质量问题不进 FSP
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch1 §1.2（虫害、毛发、污物、腐败不属 hazard）
      - Ch2 §2.4（危害分析只处理致病致伤因子）
      - Ch4 §4.4.2（为控霉变等质量原因做的分区不算 PCHF 卫生控制）
  V2_predictive_power:
    passed: true
    novel_question: "客户投诉零食里有头发，这要在 FSP 里加预防控制吗？"
    derived_answer: "不进 FSP：头发不致病致伤，属 CGMP/质量管理范畴——把它塞进 FSP 会稀释监控与验证资源；反之把真正的安全危害当质量问题处理则漏控"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'食品里不能有头发'；FDA 特定的是法定三分边界（hazard/potential hazard/需控危害）决定文件边界与资源配置，混同即体系失焦"
- id: pV-06
  title: FSP 与 HACCP 的结构差异——控制为中心而非 CCP 为中心
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch1 §1.4.1/§1.4.2（供应商/过敏原/卫生控制升格为正式预防控制；监控按角色酌情）
      - Ch2 §2.5（CCP 划入标准收窄至工艺控制）
      - Ch11 §11.5（过敏原控制全套管理组件但不套 CCP 关键限模式）
  V2_predictive_power:
    passed: true
    novel_question: "存量 HACCP 企业把供应商审核放在前置程序里，升级到 FSP 时要改吗？"
    derived_answer: "要重新归类：FSP 下供应链控制是正式预防控制，须配纠正/记录审查/再分析组件（但免 validation、无监控组件）——不是补 CCP 而是换管理框架"
  V3_exclusivity:
    passed: true
    why_not_common: "HACCP 常识是'一切围绕 CCP'；FDA 特定的是五类控制并行、非 CCP 控制可不被监控、控制类型决定管理组件组合——照搬 HACCP 会漏配组件"
- id: pV-07
  title: X 标记只是建议评估的起点（三层漏斗）
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 1 A1.3/A1.8.1（hazard→potential hazard→需控危害三层术语体系）
      - 附录 1 A1.8.3 及 1A–1P 各表头（表中不标识任何需控危害，判定责任在设施）
      - Ch2 §2.4.1（Ch3/附录 1 非穷尽清单，表外危害责任在自己）
  V2_predictive_power:
    passed: true
    novel_question: "附录 1 表里我的产品没打 X 的危害，可以直接写'No'吗？"
    derived_answer: "不能直接抄：X 只是起点，表上没 X 也可能因产地、用途、工艺而存在于你的产线；同样 X 打了也可能不适用——每个危害都要过自己的评估，不是查表"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'有表照表做'；FDA 特定的是表格自我声明'不含任何需控危害判定'+三层漏斗——照表抄会过度控制，不看表会违规，责任不可外包"
- id: pV-08
  title: 逐设施独立评估——禁止照抄
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch2 §2.4.2.2（同一产品在不同设施危害谱不同，玻璃瓶 vs 塑料瓶例）
      - Introduction §II（指南是通用参考，必须做指南→自身操作的映射）
      - Ch4 §4.3（借用外部热处理数据须按自家产品脂肪/水分/糖调整）
  V2_predictive_power:
    passed: true
    novel_question: "同行 опубликов了完整的 FSP 模板且产品几乎一样，能直接用吗？"
    derived_answer: "设备、气流、原料产地、人流物流不同则危害谱不同——可作格式参考，但每个危害判定须用自己的设施证据支撑，否则检查时无法自证"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'参考行业实践'；FDA 特定的是把'逐设施独立'写成评估义务：转移结论需要可审查的适配性论证，而非行业惯例默认"
- id: pV-09
  title: 法定评估框架——双维度 + 十类因素
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch2 §2.4.2（117.130(c)(1) 严重性×概率 + (c)(2) 十类因素）
      - Ch2 §2.4.2.3（RTE 环境病原强制评估项嵌入同一框架）
      - Ch12 §12.3.4（化学危害四因素盘查是同一框架的化学分册）
  V2_predictive_power:
    passed: true
    novel_question: "评估一个新原料时如何保证没漏掉维度？"
    derived_answer: "用十类因素做查漏清单：配方/设施设备/原辅料/运输/加工/包装标签/储运/预期用途/卫生员工健康/其他——评估记录中每类留痕即构成完备性证据"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'评估风险大小'；FDA 特定的是法定强制清单（must consider）+ 严重性三因子/概率六因子的具体分解——把判断 structured 成可检查的清单"
- id: pV-10
  title: 发现地 ≠ 控制地——控制位置决定机制
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch2 §2.3.2 Column 6 / §2.4.2.4（识别步骤不必是控制步骤，按最有效处控制）
      - Ch2 §2.4.2.2.4（"Yes"三充分条件之一：别处识别、本步可控）
      - Ch15 §15.6.1（自厂控制该危害则无须供应链程序——控制位置决定程序类型）
  V2_predictive_power:
    passed: true
    novel_question: "面粉在接收时检出沙门氏菌风险，一定要在接收步骤加控制吗？"
    derived_answer: "不必：可在下游热处理步骤控制（更有效），危害分析第 6 列指向热处理；若选择在接收前由供应商控制，则走供应链程序——位置选择是设计决策不是默认"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'在哪发现在哪解决'；FDA 特定的是"控制最有效处"原则 + 位置选择决定适用哪套程序（工艺控制/供应链控制）的制度后果"
- id: pV-11
  title: 控制覆盖逻辑——一控多害
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch2 §2.5（一个控制措施可覆盖多个危害，烹饪例）
      - 附录 1 A1.6.1.2.2（控 Salmonella/致病性 E. coli 即覆盖 Shigella，故不单列）
      - 附录 1 A1.6.1.1（生可可豆只列 Salmonella，控制它即覆盖 L. mono/E. coli）
  V2_predictive_power:
    passed: true
    novel_question: "热处理验证只针对 Salmonella 做 6D，需要再为 E. coli O157:H7 单独设计工艺吗？"
    derived_answer: "若该病原的耐热性低于目标病原且污染途径相同，无需独立工艺——验证主病原控制的技术覆盖范围即可；覆盖不成立时才需要第二个控制"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'一个危害一个措施'；FDA 特定的是"控制覆盖即豁免单列"的判定逻辑——先找主病原再验证覆盖面，避免重复设计"
- id: pV-12
  title: PCQI 责任制
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch1 §1.3（FSP 须由 PCQI 编制或监督，不必是本厂员工）
      - Ch6/Ch11/Ch12 各示例（PCQI 审查记录、判安全、做书面认定贯穿全部示例厂）
      - Ch15 §15.11.2.2（SAHCODH 年审豁免须 PCQI 书面认定）
  V2_predictive_power:
    passed: true
    novel_question: "小厂没有全职质量人员，能把 FSP 全部外包给顾问吗？"
    derived_answer: "可以：PCQI 允许外聘，编制/监督、记录审查、安全判定可由外部 PCQI 承担；但签署与实施责任仍在 owner——外包的是能力不是责任"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'要有专人负责质量'；FDA 特定的是 PCQI 是法定角色（FSPCA 课程或经验认定）+ 其书面认定是一系列豁免与裁剪的唯一合法通道"
- id: pV-13
  title: 资格与培训体系——全员底线 + 记录留痕
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Introduction §V（117.4：合规责任明确分配给具名主管；按角色培训地图）
      - Ch11 §11.10（临时工季节工也不例外；培训记录必须建立保存）
      - Ch11 Table 11-5（采购/收货/维修/清洁/主管差异化主题）
  V2_predictive_power:
    passed: true
    novel_question: "旺季雇的 3 周临时工要培训吗？培训没记录会怎样？"
    derived_answer: "要——117.4 明确覆盖临时工；无记录=无法向检查官证明培训发生过=视同未培训。且采购岗与维修岗的培训内容不同（供应链控制 vs 工具带过敏原）"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'要培训员工'；FDA 特定的是资格人人有份（含临时工）+ 培训记录为法定保存项 + 责任须'明确分配'而非'人人有责'的制度设计"
- id: pV-14
  title: FSP 格式自由、内容不自由
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch1 §1.6（无标准化/强制格式）
      - 附录 2 Introduction（自定义格式须提供全部法定要素信息）
      - Ch11 §11.5（过敏原控制可用叙述式而非表单，前提信息齐全）
  V2_predictive_power:
    passed: true
    novel_question: "能用思维导图或 wiki 代替 FSPCA 表单吗？"
    derived_answer: "可以——只要 117.126/117.305/117.310 要求的每个组件信息都在；判定标准是内容完备性而非排版。用叙述式反而能更清楚展示危害分析的推理过程"
  V3_exclusivity:
    passed: true
    why_not_common: "多数监管体系规定申报格式；FDA 特定的是'格式完全放开 + 内容逐项法定'的组合——合规审查对象是信息完备性而非文档形态"
- id: pV-15
  title: should/must 阅读规则
  type: principle
  group: G1-危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Introduction §II（"should"=建议不强制）
      - Ch6 §6.15.5（示例用"PCQI 书面论证"把 should 级要求合法裁剪）
      - Ch16（must+条款号的硬要求与 should 建议混合排版，须分层）
  V2_predictive_power:
    passed: true
    novel_question: "指南说企业'should'每年审核供应商，不做违法吗？"
    derived_answer: "不违法——除非该建议被 117.430 那样以'must+条款号'引用（SAHCODH 场景即被引成硬要求）。读指南先分层：条款引用=硬约束，纯 should=可裁剪但裁剪宜书面化"
  V3_exclusivity:
    passed: true
    why_not_common: "这是解读 FDA 指南文本的解密规则：非约束性建议 vs 法定引用的双层结构，外部人极易把建议当强制而过度合规"
```

## G2 数值界限与工艺控制

```yaml
- id: pV-16
  title: 孢子局限与屏障接力
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.3.1–3.3.2（孢子耐性远超营养细胞，kill step 后需 pH/a_w/温度接力）
      - Ch5 Table 5-1（a_w≤0.92 抑制孢子萌发的双界限）
      - 附录 3 Table 3-E 引言（非蛋白分解 C. bot 在冷藏温度可生长→长货架期冷藏食品的强制考量）
  V2_predictive_power:
    passed: true
    novel_question: "HPP 处理过的即食餐冷藏 30 天，还需要额外屏障吗？"
    derived_answer: "需要：孢子是最耐压形态，HPP 后幸存孢子还获得无菌竞争优势；若货架期足以让非蛋白分解 C. bot 萌发，须叠加 a_w≤0.92、pH 或冷藏温度设计——杀菌步骤不终结孢子问题"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'高温灭菌=安全'；FDA 特定的是 kill step 后幸存孢子反而处于竞争真空、数值界限 0.92 与 3.3°C 的接力规则"
- id: pV-17
  title: 已形成毒素不可逆——控制必须赶在产毒之前
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.3.4.2.1（蛋奶派温度滥用产 S. aureus 毒素，后续热处理不破坏）
      - Ch4 §4.3.2.2（冷冻控产毒有效、对已形成毒素无效）
      - Ch4 §4.3.3.1（a_w 0.85 之下毒素问题的表述）+ Ch5 Table 5-1（配方控制对已形成毒素无效）
  V2_predictive_power:
    passed: true
    novel_question: "面糊室温放了 8 小时，烤透还能救回来吗？"
    derived_answer: "不能：S. aureus 产毒在烘烤前已发生且热稳定——'反正后面会烤'不能豁免前段时间温度控制；产毒前时序控制是独立于最终 kill step 的必要控制"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'煮熟就安全'；FDA 明确否定热处理万能论：毒素不可逆 + 杀前生长抬高基数使固定 6D 失效，是时序性的工艺设计规则"
- id: pV-18
  title: 目标病原选择规则——最耐热 × 能在该产品环境生长
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.3.4.1（按最 resistant 病原设计，糖/油屏蔽热效应）
      - Ch6 §6.15.1（Soup B：热灌装 ROP+冷藏→非蛋白分解 C. bot B 型为目标菌）
      - Ch6 §6.16.1（Salsa A：pH 4.1 文献依据→只针对营养细胞）
      - Ch12 Table 12-2 脚注（坚果漂烫去皮不算杀灭步骤）
  V2_predictive_power:
    passed: true
    novel_question: "新做真空包装的意式肉酱冷藏销售，热处理该按什么菌设计？"
    derived_answer: "厌氧环境×冷藏×货架期→目标菌=非蛋白分解 C. botulinum（最耐热的可生长者），按 90°C/10min 级 6D 设计；按惯例抄同行的'杀沙门氏菌'工艺会漏掉肉毒"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'杀菌就行'；FDA 特定的是包装氧环境×储运温度×耐热性三因素共同决定目标菌 + pH 文献值决定是否只需控营养细胞"
- id: pV-19
  title: 热处理验证三步——发表研究 + 热分布 + 热穿透
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.3.4.1（冷点未达最低致死工艺则病原存活）
      - Ch6 §6.12.2/§6.13.2（Cookie A/B：Lathrop 研究+满载热分布+热穿透）
      - Ch6 §6.14.2（Soup A：热穿透覆盖最慢加热产品最坏工况）
  V2_predictive_power:
    passed: true
    novel_question: "买了台新烤箱做同款饼干，能直接沿用旧关键限 350°F/13min 吗？"
    derived_answer: "不能直接沿用：发表研究只证明原理可行，厂内热分布/热穿透研究证明'我的设备做得到'——新设备的冷点位置不同，须重做厂内研究（配方变更同理）"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'按文献温度烤'；FDA 特定的是两层验证结构（原理层+设备层）+ 满载最坏工况要求 + 配方变更触发重评估"
- id: pV-20
  title: EPIPT——终点温度替代全程监控的三前提
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch4 §4.3.1.1 + Ch6 §6.6（热分布+热穿透+关键因素三前提）
      - Ch6 §6.14.2（Soup A：升降温附加致死量使 6D 仅需 3 秒→只监控 180°F 终点）
      - Ch6 §6.8.3（EPIPT 每批必测的监控频次）
  V2_predictive_power:
    passed: true
    novel_question: "能否把高风险低酸汤的'保温 30 分钟'监控省掉只测温？"
    derived_answer: "按致死需求判断：若到达终点温度时升降温冗余已覆盖全部致死需求（如 6D 仅需数秒）→可以 EPIPT；冗余不足→不可。监控简化由科学结论决定，非管理偏好"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'多记多保险'；FDA 特定的是 EPIPT 制度：三前提研究完成后时间维度从监控中消失，只测终点——把致死量算进升降温曲线是独有的判定逻辑"
- id: pV-21
  title: 粒径关键限与隐藏前提链
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch4 §4.3.1.1（大颗粒不能靠抽检粒子温度，须科学验证）
      - Ch6 §6.14.2（Soup A：颗粒≤½英寸 + 冷藏不冻结前提）
      - Ch6 §6.16.2（Salsa A：≤1.0cm + 冷藏 SOP 为前提，同一模式）
  V2_predictive_power:
    passed: true
    novel_question: "冷冻蔬菜直接投锅熬汤，原来按冷藏颗粒验证的工艺还有效吗？"
    derived_answer: "失效——热穿透以'颗粒初始冷藏状态'为前提，冻结改变了升温曲线；粒径 CL 背后藏着的温度史前提被破坏，须重做热穿透或把解冻/初始温度写成关键因素"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'控制汤温就行'；FDA 特定的是看得见的粒径参数背后有看不见的前提（原料温度史），SOP 本身成为关键限成立的条件链"
- id: pV-22
  title: 冷却三重威胁——孢子时窗 + 两段式协议 + 再污染通道
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.3.4.2.2（140°F 以下幸存孢子开始发芽）
      - Ch4 §4.3.2.1（两段式冷却 135→70°F/2h、70→41°F/4h；FSIS 等效替代）
      - Ch4 §4.3.2.1（冷却期再污染：手接触/冷凝水/交叉接触）
  V2_predictive_power:
    passed: true
    novel_question: "大桶熬好的汤自然放凉过夜行不行？"
    derived_answer: "不行：大体积冷却可长达 36 小时，孢子在危险温区停留过久萌发产毒；且冷却是最脆弱窗口（竞争菌已灭、再污染三通道敞开）——须 blast freezer/换热器等加速并防再污染"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'放凉就行'；FDA 特定的是数值化两段协议（2h/4h 分段）+ 把冷却识别为孢子萌发时窗与再污染窗口的双重陷阱工序"
- id: pV-23
  title: 危险温区与累计暴露时间表（禁线性内插）
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch4 §4.3.2（41–135°F 危险温区定义与 4 小时经验法则）
      - 附录 3 Table 3-B/3-C（生/熟 RTE 分档累计暴露限；累计=多次求和）
      - 附录 3 Table 3-C 引言（对数生长→禁止线性内插）
  V2_predictive_power:
    passed: true
    novel_question: "熟 RTE 半成品出库后在 25°C 装卸 40 分钟、又在 15°C 待了 2 小时，还能用吗？"
    derived_answer: "按分档累计：>80°F(26.7°C) 未触发；21.1–26.7°C 限 2 小时（已用 40min）；10–21.1°C 限 5 小时（用 2h）→仍未超。累计是分档求和而非单次判断，且不同温度档不可线性折算"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'别放太久'；FDA 特定的是分病原/分熟制/分温度档的累计暴露数值表 + 禁止内插（取更严档）的数值纪律"
- id: pV-24
  title: 配方屏障数值界限体系（a_w 0.85/0.92、pH 4.6）
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch4 §4.3.3.1（a_w 0.85=S. aureus 最低生长 a_w，三分类）
      - Ch5 Table 5-1（0.92 抑制孢子萌发的双防线）
      - Ch4 §4.3.3.2 / Ch16 §16.3（pH 4.6 肉毒萌发线与 LACF/酸化双法规分界）
      - 附录 3 Table 3-A（L. mono -0.4°C、S. aureus a_w 0.83 等极端值）
  V2_predictive_power:
    passed: true
    novel_question: "把果酱 a_w 做到 0.88，能常温卖吗？"
    derived_answer: "营养细胞被抑制（<0.85 才完全安全，0.88 已挡多数病原），但孢子萌发线在 0.92 之上——0.88 对孢子无屏障；若糖酸体系另行控制孢子（pH<4.6）则可，单看 a_w 不构成充分屏障"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'糖多防腐'；FDA 特定的是双界限数值体系（0.85 控营养细胞 / 0.92 控孢子萌发）+ pH 4.6 兼作法规管辖分界——每个数字都有判例与法规后果"
- id: pV-25
  title: 多组分界面微环境陷阱
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch2 §2.4.2.4（十类评估因素中的配方界面警示：派、分层面包）
      - Ch3 §3.3.4.2.3（界面 pH/a_w 重新分布可形成生长微环境）
  V2_predictive_power:
    passed: true
    novel_question: "酥皮（低 a_w）包奶油馅（低 pH），两组分各自'安全'，组合安全吗？"
    derived_answer: "不一定：界面处水分与酸重新分布，恰好可能落入病原生长窗口——多组分产品的危害评估必须测成品界面均衡 pH/a_w 与组分间梯度，单组分合格不外推"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'组分安全=产品安全'；FDA 点名的界面陷阱直接否定组分加总的直觉，是配方评估中可操作的判定项"
- id: pV-26
  title: 抑制 vs 杀灭——配方控制的效力边界
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.3.4.2.3（pH/a_w/防腐剂/氧协同构成抑制生态）
      - Ch5 Table 5-1（加酸能阻止生长但不能消灭营养细胞；防腐剂对孢子只能阻萌发）
  V2_predictive_power:
    passed: true
    novel_question: "酸化到 pH 3.8 的饮料还需要热处理吗？"
    derived_answer: "取决于目标：酸已可靠阻止病原生长（生长控制），若原料带入活菌且产品货架期/品质要求无菌，则抑制不等于杀灭——需致死处理或以'只抑不杀'明确设计货架期"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'酸了就安全'；FDA 特定的是把控制措施二分为生长控制/杀灭控制并规定各自能承诺什么——工艺逻辑需要'消灭'时配方控制不合法"
- id: pV-27
  title: ROP 准入规则——五屏障与先产毒后腐败
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.3.4.2.4（五屏障：a_w<0.93/pH<4.6/盐>10%/终容器热处理/冷冻储运）
      - Ch3 §3.3.4.2.4（3.33°C 以下才抑全部肉毒株→冷藏不得为唯一屏障）
      - Ch3 §3.3.4.2.4（低氧选择厌氧病原、清除腐败警讯→先产毒后腐败）
  V2_predictive_power:
    passed: true
    novel_question: "真空包装的卤味冷藏卖 14 天，安全吗？"
    derived_answer: "ROP 使腐败警讯消失（可能先产毒后腐败），冷藏温度通常高于 3.33°C 不构成屏障——须五屏障居其一（如终容器热处理）或组合屏障，'卖前闻着没问题'不是判据"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'真空+冷藏=保鲜'；FDA 特定的是屏障清单与'感官警讯被技术性消除'的机制解释——腐败不再是安全信号是反直觉核心"
- id: pV-28
  title: 致死度数值体系——5D–7D / 6D 与表值优化
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch4 §4.3.1.1（烹饪 5D–7D；孢子目标 6D=90°C/10min）
      - 附录 3 Table 3-D/3-E（L. mono 70°C/2.0min；表值为保守通值，可用 TTD 研究缩短或按初始水平调 D 值）
      - Ch6 §6.15.2/§6.16.2（Soup B 205°F×2.5min 等效换算；Salsa A pH≤4.1 下 5D）
  V2_predictive_power:
    passed: true
    novel_question: "自家产品初始菌量常年 <100 CFU/g，能低于 6D 吗？"
    derived_answer: "可以：以自身初始水平研究为据可降低杀灭度，或以热致死时间研究缩短表值时间——表值是保守下限起点，工艺优化方向由自身微生物数据决定"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'高温长时间最保险'；FDA 特定的是 D/z/6D 的量化语言 + 查表锚点（70°C/2min、90°C/10min）+ 双向优化路径（初始水平低可降、高须升）"
- id: pV-29
  title: 酸化屏障维持——腐败菌抬酸反扑
  type: principle
  group: G2-数值界限与工艺控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch4 §4.3.3.2（腐败菌代谢抬高 pH 使肉毒孢子萌发→须热处理杀营养细胞或用防腐剂）
      - Ch6 §6.16.1（Salsa A：先定 pH 屏障 4.1 再定热处理目标，防 pH 反升）
      - Ch16 §16.3/§16.9（酸化食品肉毒风险的完整机理重述）
  V2_predictive_power:
    passed: true
    novel_question: "pH 4.0 的莎莎酱 shelf-stable，开封前就绝对安全吗？"
    derived_answer: "若腐败菌（酵母/霉菌）在储运中生长把 pH 抬回 4.6 以上，肉毒防线即被击穿——屏障不是静态属性，须配套杀灭腐败菌的营养细胞或抑制其繁殖的定值工艺"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'pH 低就安全'；FDA 特定的是屏障可被非病原微生物代谢攻破的动态视角 + '先屏障后目标菌'的互补设计顺序"
```

## G3 管理组件闭环

```yaml
- id: pV-30
  title: 监控设计——四问框架 + 频次基线 + 校准底线
  type: principle
  group: G3-管理组件
  V1_cross_domain:
    passed: true
    evidence:
      - Ch5 §5.5.2（监控四问 What/How/How often/Who）
      - Ch6 §6.8.3（连续记录每批一次、连续设备每日一次、泵速每班两次）
      - Ch6 §6.12.5 等（示例厂统一"至少每年校准"+日常准确性核查）
  V2_predictive_power:
    passed: true
    novel_question: "新上了自动温度记录仪，人工巡检可以取消吗？"
    derived_answer: "不能全取消：连续记录仍须至少每批（批式）或每日（连续）人工目视核查偏离——自动化改变的是记录方式，不取消人工核查义务"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'装了传感器就不用人看'；FDA 特定的是四问框架 + 具体频次数值基线 + 自动化/人工手段兑换监控频率的规则"
- id: pV-31
  title: 受影响范围回溯推定——自上次合格点起
  type: principle
  group: G3-管理组件
  V1_cross_domain:
    passed: true
    evidence:
      - Ch5 §5.5.2（偏差假定自上次合格检查起未受控；校准失效同理回溯）
      - Ch11 §11.6.1.2（过敏原受影响批次 = cleanup to cleanup，举证负担在缩小方）
  V2_predictive_power:
    passed: true
    novel_question: "今天 15 点发现杀菌锅温度偏低 2 小时了，只需隔离这 2 小时的产品吗？"
    derived_answer: "不是：默认推定自上次合格检查起的全部产品未受控——监控间隔直接决定风险敞口。要缩小范围须自证中间时点合格，而非等待发现时点"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'发现多少处理多少'；FDA 特定的是举证方向反转：受影响边界由上次合格事件定义而非发现时点——这使得监控频次成为风险管理变量"
- id: pV-32
  title: correction 与 corrective action 的判定边界
  type: principle
  group: G3-管理组件
  V1_cross_domain:
    passed: true
    evidence:
      - Ch1 §1.4.3 / Ch5 §5.5.3（轻微孤立未影响产品→correction，如开工前残留重清洁）
      - Ch11 §11.5.3 / §11.13.3.3（过敏原：投产前发现错器具=correction 不记录；开工后=CA+评估产品）
      - Ch11 §11.7.3（错标已用于生产=依法错标，须 CA 并召回已入市品）
      - 附录 2 Form 2-D（卫生控制多数走 correction，但应预列升级触发情形）
  V2_predictive_power:
    passed: true
    novel_question: "贴标机下午贴错了 200 个盖子，下午 4 点才发现，怎么定性？"
    derived_answer: "生产已开始且产品可能受影响→corrective action（非 correction）：记录、查明原因、防复发、评估受影响食品、阻止入市；若盖子无过敏原信息则按 misbrand relevance 降级处理"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'错了就改'；FDA 特定的是双轴判定（是否触及产品 × 孤立 vs 反复）+ 时间分界（生产前/后）改变处理等级与记录义务的法定结构"
- id: pV-33
  title: 纠正措施四目标 + 预定程序三重价值
  type: principle
  group: G3-管理组件
  V1_cross_domain:
    passed: true
    evidence:
      - Ch6 §6.9（117.150(a) 四目标逐字）+ Ch11 §11.5.3（过敏原章重述）
      - Ch5 §5.5.3（预定纠正程序三价值：操作指引/从容制定/免于每次触发再评估）
  V2_predictive_power:
    passed: true
    novel_question: "写好预定纠正程序后，每次偏离还要重新评估 FSP 吗？"
    derived_answer: "不需要：预定程序的第三重价值正是豁免逐次再评估义务——把偏离处置前置为规则适用，而非每次临场判断是否动摇体系"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'出事再商量'；FDA 特定的是四目标为法定闭环（纠正/防复发/评估食品/阻止入市）+ 预定程序与再分析义务的豁免关系"
- id: pV-34
  title: 偏差处置阶梯
  type: principle
  group: G3-管理组件
  V1_cross_domain:
    passed: true
    evidence:
      - Ch6 §6.9（热处理偏差七选项：补足/延长/重加工/留评估/改用途/转饲料/销毁）
      - Ch12 §12.6.5（化学危害共用同一阶梯：根因→评估→改用途/转饲料/销毁）
  V2_predictive_power:
    passed: true
    novel_question: "杀菌不足的一批 RTE 汤一定要销毁吗？"
    derived_answer: "不必：按阶梯处置——补足加热、延长热循环、重加工均可恢复安全；RTE 降级为非 RTE（转非即食用途）是常被忽略的合法选项，只有无法确保安全才销毁"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'不合格=扔'；FDA 特定的是处置阶梯按'能否恢复安全'排序 + RTE→非 RTE 降级用途的制度通道"
- id: pV-35
  title: 操作限/关键限双层设计
  type: principle
  group: G3-管理组件
  V1_cross_domain:
    passed: true
    evidence:
      - Ch6 §6.5/§6.9（偏离操作限只 adjustment 与质量评估，不触发纠正措施）
      - Ch6 §6.12.2（Cookie 350°F/13min 关键限 vs 352°F/15min 操作限的实例）
      - Ch6 §6.16.2（Salsa A：货架期操作限视同关键限——失效后果触及安全即从严）
      - Ch6 §6.12.7（调整记录虽非强制但用于趋势分析）
  V2_predictive_power:
    passed: true
    novel_question: "投料量偶尔压线 27.5g（限 28g），要写纠正措施报告吗？"
    derived_answer: "不用：27.5g 在关键限内、超操作限 27g——只做 adjustment 并（建议）记录；但若调整记录显示频度上升，即是设备劣化趋势信号，应触发程序复审"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'超标就是超标'；FDA 特定的是双层限值制度：内控线的偏离有独立通道（adjustment），且分层依据是失效后果是否最终触及安全而非参数名义用途"
- id: pV-36
  title: 15 批强化监测规则
  type: principle
  group: G3-管理组件
  V1_cross_domain:
    passed: true
    evidence:
      - Ch6 §6.14.4（Soup A：颗粒尺寸失控后逐批 15 批）
      - Ch6 §6.16.4（Salsa A：同一数值协议）
  V2_predictive_power:
    passed: true
    novel_question: "抽样监控一次失察后，什么时候能恢复原抽样频率？"
    derived_answer: "数值化：立即升为逐批，连续 15 批全部合格才恢复'每 3 批抽 1'——一次失察=信任破产，降频资格须用连续合格记录重新赢回，消除'何时放松'的主观性"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'改了就好'；FDA 示例给出具体的升级/降级数值协议（15 批连续合格），是可照抄的频次治理规则"
- id: pV-37
  title: 验证体系两层——五类活动 + 日常四件套
  type: principle
  group: G3-管理组件
  V1_cross_domain:
    passed: true
    evidence:
      - Ch6 §6.10（117.155 五类验证活动逐字）+ Ch11 §11.5.2.2（过敏原章重述）
      - Ch6 §6.10（117.165(a) 日常四件套：校准/检测/环境监测/记录审查）
      - Ch6 §6.15.5（Soup B 不做检测与环境监测——验证强度与暴露史匹配，裁剪须书面化）
  V2_predictive_power:
    passed: true
    novel_question: "热灌装后不暴露环境的产品要做环境监测吗？"
    derived_answer: "不需要：暴露史决定验证活动取舍——产品经验证致死处理且热灌装后无环境暴露，则病原检测与环境监测均可省；但省略须 PCQI 书面认定并记录"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'验证越多越好'；FDA 特定的是验证=五类法定活动的封闭清单 + 按暴露史裁剪但每项裁剪都要书面依据的弹性结构"
- id: pV-38
  title: validation 豁免清单
  type: principle
  group: G3-管理组件
  V1_cross_domain:
    passed: true
    evidence:
      - Ch1 §1.4.5（卫生控制等可不需 validation）
      - Ch4 §4.2（法定四类豁免 + 其他控制豁免须 PCQI 书面论证）
      - Ch11 §11.5.2.2 脚注（过敏原控制豁免的立法理由：有效性证据尚不成熟）
  V2_predictive_power:
    passed: true
    novel_question: "公司的过敏原清洁程序需要做科学挑战试验吗？"
    derived_answer: "不需要 validation（法定豁免），但不豁免管理组件——监控/纠正/verification/记录照常；想做也不被禁止，且现有验证程序稍加修改可构成 validation 研究"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'控制措施都要科学验证'；FDA 特定的是封闭豁免清单（四类）+ '豁免 validation ≠ 豁免 verification'的组件分层——过度工程与偷工减料两头都被制度封住"
- id: pV-39
  title: 记录体系——双轨留痕 + PCQI 审查时限 + exception record
  type: principle
  group: G3-管理组件
  V1_cross_domain:
    passed: true
    evidence:
      - Ch1 §1.2（FSP 本身是记录 + 实施证明记录双轨）
      - Ch6 §6.11（监控/纠正/验证三类组件记录必须留痕）
      - Ch6 §6.12.5（PCQI 7 天审查惯例）+ Ch15 §15.13（供应链记录同等义务 + 18 项清单）
      - Ch11 §11.5.6（exception record：只记失控，条码扫描器例）
  V2_predictive_power:
    passed: true
    novel_question: "条码扫描器 7×24 在线核对标签，还用每个班次填记录吗？"
    derived_answer: "可以用 exception record：连续自动化监控下仅失控（检出错标）时生成记录——把记录负担与监控可靠性绑定，但前提是监控手段本身连续可信"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'凡事留痕'；FDA 特定的是'没有记录=没有做'的法定地位 + 审查时限数值（7 天惯例可论证放宽）+ 只记异常的例外记录制度"
- id: pV-40
  title: 偏差三角色分工
  type: principle
  group: G3-管理组件
  V1_cross_domain:
    passed: true
    evidence:
      - Ch6 §6.12.4（Cookie A 模式：PCQI 判安全/经理查根因/培训操作工）
      - Ch6 §6.15.4、§6.16.4（Soup B、Salsa A 同一模式——5 个示例厂全部采用）
  V2_predictive_power:
    passed: true
    novel_question: "偏差发生后生产经理能不能直接判定产品'应该没事'放行？"
    derived_answer: "不能：安全判定权归 PCQI（技术判断），根因调查与整改归管理线（管理权）——角色不可互换，放行决定须有 PCQI 的评估书面依据"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'领导拍板'；FDA 示例把技术判定权（PCQI）与管理整改权（经理）制度性分离，5 厂一致，是可迁移的职责矩阵"
```

## G4 环境病原与卫生控制

```yaml
- id: pV-41
  title: 湿区防李斯特——保持干燥 + 禁扩散性清洁
  type: principle
  group: G4-环境病原与卫生
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.3.5.3.1（湿区最有效策略是尽量干燥；高压水枪气溶胶扩散 L. mono）
      - Ch4 §4.4.1（消毒剂按 EPA 注册标签；清洁先于消毒）
      - 附录 11-1.D（干残留禁压缩空气/喷砂——同一扩散机理用于过敏原）
  V2_predictive_power:
    passed: true
    novel_question: "为了'更干净'每班用高压水枪冲洗车间地面，对吗？"
    derived_answer: "反效果：气溶胶把李斯特菌从地面溅到接触面——湿区控菌的第一杠杆是减少漫水与高压冲洗、按需用水、湿清洁后彻底干燥，而不是增加冲洗频次"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'冲得越勤越干净'；FDA 特定的是水是传播载体而非清洁介质本身、气溶胶扩散机制、以及清洁与消毒的两步定义"
- id: pV-42
  title: 干区防沙门——严格控水与干涸粉尘陷阱
  type: principle
  group: G4-环境病原与卫生
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.3.5.3.2（主沙门控制区始终保持干燥；积水与干涸斑点双危险）
      - Ch3 §3.3.5.3.2（干涸积水形成含菌粉尘经空气传播的附加风险）
      - Ch4 §4.4（湿清洁后必须彻底干燥方可使用；117.35(d)(1) 低水分食品接触面干燥要求）
  V2_predictive_power:
    passed: true
    novel_question: "干粉车间漏了次雨，水渍干了还需要处理吗？"
    derived_answer: "要：干涸水渍是潜在藏匿点，含菌粉尘会经空气扩散污染产品——'水干了就没事'是错误认知；须按受控湿清洁+彻底干燥处理并评估该区域"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'水干了就安全'；FDA 特定的是干区两种水状态（积水/干涸）各自不同的危害机制与处置要求 + 极少量断续水分即可支撑沙门氏菌"
- id: pV-43
  title: 卫生分区的范围判定
  type: principle
  group: G4-环境病原与卫生
  V1_cross_domain:
    passed: true
    evidence:
      - Ch4 §4.4.2（分区必要性按设施/产品/危害分析判定，非一刀切）
      - Ch3 §3.3.5.3.2（主沙门控制卫生区的定义本身取决于 RTE 暴露范围）
  V2_predictive_power:
    passed: true
    novel_question: "同一条线上既有生粉处理又有 RTE 包装，分区要画到什么程度？"
    derived_answer: "按人流物流、气流、生熟界面与 RTE 暴露点划定敏感区边界（生 vs 在制品、湿 vs 干、压差方向）；且只为控霉变等质量目的做的分区不计入 PCHF 卫生控制"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'脏区净区分开'；FDA 特定的是分区范围由危害分析输出决定 + 质量性分区不享有法定卫生控制地位——范围与定性都需论证"
- id: pV-44
  title: transient vs resident 二分与定殖根除
  type: principle
  group: G4-环境病原与卫生
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.3.5.2（定殖菌藏匿 niche 数月至数年，常规清洁无效须强化程序）
      - Ch3 §3.3.5.3（transient→常规 CGMP；resident→强化卫生+根除调查）
      - Ch3 §3.3.5（CGMP+HACCP 也不能保证环境再污染不发生→卫生控制+环境监测法定化）
  V2_predictive_power:
    passed: true
    novel_question: "环境监测连续三周在同一设备底座检出同型李斯特菌，常规 SSOP 加密有效吗？"
    derived_answer: "无效：同点位反复检出同型菌株=resident 定殖信号——常规清洁对 niche 内定殖菌无效，须启动强化卫生程序（拆机、深入 niche、根除调查），目标是防 transient 变 resident"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'加强清洁就行'；FDA 特定的是两态模型：定殖状态下常规清洁在微生物学上无效，且该模型是环境监测法定义务的论证根基"
```

## G5 过敏原程序

```yaml
- id: pV-45
  title: 咨询声明的定位——只能是被证明的控制极限之出口
  type: principle
  group: G5-过敏原
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 §11.1/§11.4.3/§11.8.3.1/§11.9.1（不能替代 CGMP 或交叉接触控制，四处重申）
      - Ch11 §11.6.1.3/§11.8.6（再分析可能反向得出"此时声明才合适"）
      - Ch11 §11.3（FDA 未设免声明阈值，阈值论证责任在企业）
  V2_predictive_power:
    passed: true
    novel_question: "共用产线清洁后偶有微量残留，能不能直接贴 'may contain peanuts' 免去清洁验证？"
    derived_answer: "不能：声明是控制极限被证明后的出口而非入口——须先用尽 CGMP 与预防控制，再分析证明无法避免交叉接触，PCQI 书面论证后才可使用；用声明换控制等于自认控制失效"
  V3_exclusivity:
    passed: true
    why_not_common: "行业常见做法是贴声明了事；FDA 的规则方向相反：声明是最后手段，其正当性来源于再分析结论而非风险规避意图"
- id: pV-46
  title: 供应商咨询声明三选一书面决定
  type: principle
  group: G5-过敏原
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 §11.8.4/§11.9.3（不传递/传递/阈值论证三选项）
      - Ch11 §11.8.3.1（批准出具声明的供应商前先讨论原因）
      - Ch11 §11.13.5.3 脚注（Bakery B 把"索取声明理由"写入供应链程序）
  V2_predictive_power:
    passed: true
    novel_question: "供应商的杏仁粉标了 may contain milk，我司产品不含乳——需要处理吗？"
    derived_answer: "沉默不是选项：PCQI 须书面三选一——①不传递（论证对自身产品无影响）②传递到自己的标签并按含乳原料管理 ③以科学有效阈值评估证明残留无害；且先要求供应商说明声明原因"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'供应商标了他的事'；FDA 特定的是把上游声明转化为接收方必须书面处置的三选一决策，且供应商的声明行为本身是风险评估输入信号"
- id: pV-47
  title: 过敏原排产与返工规则
  type: principle
  group: G5-过敏原
  V1_cross_domain:
    passed: true
    evidence:
      - Ch4 §4.5 / Ch5 Table 5-4（无过敏原先做/独特过敏原最后；like into like 返工）
      - Ch11 §11.12.2.1 + 附录 11-1.F.2（Dessert A 递增排产；过敏原晚加下游）
      - Ch11 §11.12.3.1（序列内通用清洁够用、回起点须专项清洁的 PCQI 判定）
      - Ch11 §11.13.2.2（花生严重性→器具/服装/人员流动加控）
  V2_predictive_power:
    passed: true
    novel_question: "排产完杏仁曲奇后接无坚果燕麦曲奇，普通清洁够吗？"
    derived_answer: "不够：燕麦曲奇的过敏原谱不包含杏仁——回到序列起点必须专项过敏原清洁；若接的是含杏仁谱内的产品则通用清洁即可。清洁等级由相邻产品过敏原谱的包含关系决定"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'换产就大清洗'；FDA 特定的是按过敏原谱包含关系决定清洁等级（省换产成本）+ 排产方向（少→多）+ 返工 exact into exact 的组合规则"
- id: pV-48
  title: 标签内容控制全生命周期
  type: principle
  group: G5-过敏原
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 §11.7.1（内容四阶段：开发/订购/生产/接收 + 管理三阶段）
      - Ch11 §11.7.2.3（接收时/放行前/投产前至少其一核对）
      - Ch11 §11.12.4.1.1（Dessert A：mock-up 审核 + 分托板发运条款）
  V2_predictive_power:
    passed: true
    novel_question: "印刷厂把新旧两版标签混发货了，防线应该设在哪？"
    derived_answer: "多道：订购文件写明过敏原标签规格文本、打样（mock-up）审核后才授权印刷、接收时/放行前/投产前至少一处对照规格核对——时点越早损失越小（避免停产等待）"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'出厂前检查标签'；FDA 特定的是全生命周期布防（含供应商打样与运输分托板）+ 核对时点的制度弹性——投产前核对是底线而非唯一时点"
- id: pV-49
  title: 标签管理控制的 misbrand relevance 边界
  type: principle
  group: G5-过敏原
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 §11.11（防错标比归类更重要；同一活动可兼两类控制）
      - Ch11 §11.12.4.1.1 脚注（盖子无过敏原信息→色环用错不构成标签管理控制）
      - Ch11 §11.7.2.3.2（连续扫描=连续监控；人工扫描按 1/2/4 小时间隔）
  V2_predictive_power:
    passed: true
    novel_question: "桶身色环贴错产品但盖子没印任何过敏原信息，算过敏原控制失效吗？"
    derived_answer: "不算标签管理控制失效：判定标准是'出错是否导致 403(w) 错标'——盖子无过敏原相关信息则色环与错标无关；手段自动化水平同时决定监控频率"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'贴错就是事故'；FDA 特定的是以法定错标后果（403(w)）为归类边界——控制项的成立与否由出错的法律后果反推"
- id: pV-50
  title: 过敏原供应链快筛豁免
  type: principle
  group: G5-过敏原
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 §11.8.2（供应商不做任何过敏原 / 只做你要的那一种→免评估）
      - Ch11 §11.12.2.3/§11.13.2.3（两个示例厂对乳/蛋/面粉供应商重复此判定，≥5 处）
      - Ch11 §11.13.2.3（高度精炼大豆油依法豁免标示→同样免评估）
  V2_predictive_power:
    passed: true
    novel_question: "供应商同时做花生酱和杏仁酱，采购杏仁粉需要评估其厂内交叉接触吗？"
    derived_answer: "需要——供应商处理多种过敏原，快筛不适用；反之若只向单一坚果商买杏仁（其不处理其他过敏原），供应链程序可免。规则本质：控制对象是供应商厂内的过敏原多样性"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'所有原料都审供应商'；FDA 给出法定快筛边界：交叉接触风险不存在时（单一过敏原/法定豁免原料）评估义务本身消失"
```

## G6 供应链控制

```yaml
- id: pV-51
  title: SAHCODH 供应链硬规则——首次使用前 + 每年现场审核
  type: principle
  group: G6-供应链
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 §11.8.1/§11.8.3.2（过敏原危害通常即 SAHCODH→年审）
      - Ch15 §15.11.2.1（现场审核唯一适当活动 + 13–14 个月宽限）
      - Ch15 §15.11.2.2（豁免唯一通道：PCQI 书面认定；集团外建议仍保留 2–3 年审核）
  V2_predictive_power:
    passed: true
    novel_question: "供应商提供了第三方认证证书，SAHCODH 危害还需要自己安排现场审核吗？"
    derived_answer: "默认需要：SAHCODH 场景法定适当活动=现场审核（使用前+每年一次，间隔 13–14 个月内视为达标）；第三方证书不能替代，唯一出口是 PCQI 书面认定替代方案充分"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'有认证就行'；FDA 特定的是按危害严重性分档的审核刚性（SAHCODH→年审）+ 具体宽限数值 + 书面认定作为唯一豁免通道"
- id: pV-52
  title: 检测频次信任曲线
  type: principle
  group: G6-供应链
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 §11.8.3.2（供应商控制好→年检；不做验证测试→月检/季检）
      - Ch12 §12.10.2 脚注（Manufacturer A：逐批检测直至建立信心后降为季度）
      - Ch15 §15.7.2.2（先高频如月检，良好历史后降为季检）
  V2_predictive_power:
    passed: true
    novel_question: "新供应商的 COA 看着很好，能直接按季度抽检吗？"
    derived_answer: "不能：信任曲线从批准前多批实测起步→逐批验证供应商控制与 COA 真实性→建立信心后才降频；检测成本按供应商控制水平定价，控制差者月检/季检"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'定期抽检'；FDA 特定的是频次与信任度/供应商控制水平联动的定价机制 + 先密后疏的默认路径"
- id: pV-53
  title: 经纪商不是供应商——批准对象穿透至制造者
  type: principle
  group: G6-供应链
  V1_cross_domain:
    passed: true
    evidence:
      - Ch15 §15.3.2（经纪商/集散商/分销商/冷藏库既非供应商也非收货设施）
      - Ch15 §15.8.1（须经其信息批准实际制造者；零售渠道可用标签定位实体）
  V2_predictive_power:
    passed: true
    novel_question: "从大型分销商买面粉，审核分销商的仓库够吗？"
    derived_answer: "不够：法定供应商是制造者/种植者——应要求分销商提供足以批准制粉厂的信息；'批准对象永远是做食品的人，不是卖食品的人'"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'谁卖货审谁'；FDA 的定义把审核对象从交易对手切换为风险制造者——采购中间商不改变批准义务的指向"
- id: pV-54
  title: 供应商验证四活动 + 批准四因素
  type: principle
  group: G6-供应链
  V1_cross_domain:
    passed: true
    evidence:
      - Ch15 §15.7.2（四类法定验证活动）+ §15.7.4（批准四因素：危害分析/控制实体/表现/储运）
      - Ch15 §15.7.4.3.2（警示函/进口警报不一票否决，看整改行动）
      - Ch15 §15.6.4（控制者非供应商本人时：自行验证或审查第三方文档）
      - Ch11 §11.13.5.3（Bakery B 四件套实例：问卷+FDA 检索+第三方审核+批次检测）
  V2_predictive_power:
    passed: true
    novel_question: "供应商有进口警报记录，直接拉黑吗？"
    derived_answer: "不一票否决：纳入四因素中的'表现'评估——重点考察事后整改行动及其对验证活动类型与频次的影响；同时确定控制实体是谁以指向验证对象"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'有问题就换'；FDA 特定的是封闭的四活动/四因素框架 + 执法史的权重规则（历史是验证强度输入而非资格判据）"
- id: pV-55
  title: 验证独立性——禁止自审自证 + 报酬隔离
  type: principle
  group: G6-供应链
  V1_cross_domain:
    passed: true
    evidence:
      - Ch15 §15.8.3（供应商四项自验证活动一律不可接受）
      - Ch15 §15.11.6（报酬不得与验证结果挂钩：不得按'合规'加薪、不得因发现不符合减薪罚款；供应商亦不得支付）
  V2_predictive_power:
    passed: true
    novel_question: "供应商说'我们内部审过自己，报告给你们'，能采信吗？"
    derived_answer: "不能：四项自审自证活动零效力；供应商只能提供自测数据（COA）或第三方对其的审核——独立第三方是底线，且你的审核员报酬结构不得使其有动机放水"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'信任但核实'；FDA 特定的是自我验证在合规体系中零效力的法定列举 + 用报酬结构（而非职业操守）保障审核独立性"
- id: pV-56
  title: 接收控制与临时供应商过渡期
  type: principle
  group: G6-供应链
  V1_cross_domain:
    passed: true
    evidence:
      - Ch15 §15.9.2（只从批准供应商收货的书面程序 + 临时通道须用前充分验证）
      - Ch15 §15.9.2（临时限于数周至数月；多供应商冗余减少临时通道使用）
  V2_predictive_power:
    passed: true
    novel_question: "独家供应商突然停产，临时换一家没审过的厂应急行吗？"
    derived_answer: "可走临时通道：用前完成最低限度验证（查 FDA 执法库+按危害做逐批检测），数周至数月内完成正式批准；若预计长期使用必须立即走完整程序——并以此教训建立多供应商冗余"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'应急先用了再说'；FDA 特定的是临时通道的前置验证义务 + 过渡期数值上限 + 冗余预防设计，让'例外'也受程序约束"
- id: pV-57
  title: 供应商不合规处置梯度
  type: principle
  group: G6-供应链
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 §11.8.5（correction vs corrective action 的供应商版判定）
      - Ch11 §11.13.5.4（Bakery B：暂停使用→评估产品→必要时召回评估→批准新供应商）
      - Ch12 §12.10.2（两示例厂：供应商不响应纠正即终止合作）
      - Ch15 §15.7.5（及时行动并记录：停用/通知/协助整改/修订程序/联合召回）
  V2_predictive_power:
    passed: true
    novel_question: "供应商原料检出问题但解释合理，还能继续用吗？"
    derived_answer: "取决于影响是否触及你的产品与供应商响应速度：执行性问题且未及产品→correction；影响或可能影响产品安全→corrective action+扣留评估；对纠正不响应→直接停用，响应速度本身就是风险指标"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'出问题换供应商'；FDA 特定的是与产品影响联动的三级梯度 + '无响应即终止'的闭环条件 + 联合召回的制度选项"
- id: pV-58
  title: 小供应商替代验证三轨
  type: principle
  group: G6-供应链
  V1_cross_domain:
    passed: true
    evidence:
      - Ch15 §15.7.4.5（三类小供应商表现审查简化为只查合规史）
      - Ch15 §15.11.3/§15.11.4/§15.11.5（qualified facility / 非覆盖农场 / 小蛋鸡场的年度+两年书面保证）
  V2_predictive_power:
    passed: true
    novel_question: "从年销售额 40 万美元的小酱料厂进货，还要做现场审核吗？"
    derived_answer: "若其为 qualified facility（前 3 年年均 <50 万美元）：可用书面保证替代验证活动——每年 12 月 31 日前索取身份保证 + 每 2 年合规保证；供应商自判身份、采购方负责索取"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'小厂风险大更要审'；FDA 反向设计：按法定类别（销售额/蛋鸡数门槛）减负小供应商义务，替代物是两份周期不同的书面保证"
```

## G7 化学危害

```yaml
- id: pV-59
  title: 化学危害归途分流
  type: principle
  group: G7-化学危害
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.4.3（设施相关化学危害走 CGMP：清洁剂残留、重金属浸出、灯具玻璃）
      - Ch12 §12.3.13（FDA 明确不知有任何需升格为预防控制的情形）
      - Ch12 §12.7 / Ch3 §3.4.1（原料相关走供应链、工艺相关走工艺控制的分流）
  V2_predictive_power:
    passed: true
    novel_question: "设备润滑油可能接触食品，要立预防控制吗？"
    derived_answer: "按引入途径分流：设施/环境的系统性问题归 CGMP（食品级润滑油、设备维护程序），FDA 明确此类通常不需预防控制；但若来自原料或特定工艺步骤，则走供应链或工艺控制——路径由危害来源决定"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'所有化学品都要严控'；FDA 给出官方背书的分流表：把'判定为 No'的依据体系化（CGMP 覆盖即可），避免全体系过度控制"
- id: pV-60
  title: 农产品化学危害按供应链管理 + 违禁史证据
  type: principle
  group: G7-化学危害
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.4.1.1（进口农产品农药残留→供应链控制；真菌毒素/重金属同理）
      - Ch12 §12.3.7（违禁史与 4 个进口警报作为概率证据）
      - Ch12 §12.3.8（兽药耐受量与禁用清单：蜂用氯霉素等零容忍）
  V2_predictive_power:
    passed: true
    novel_question: "美国本土和进口的菠菜，农药残留危害分析要区别对待吗？"
    derived_answer: "要：本土产品通常默认符合 EPA 限量（仍可被违禁史推翻），进口产品则把残留视为需预防控制的化学危害走供应链程序；有进口警报（如 99-14 全国扣留）的商品概率上调、验证加严"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'都检测一下'；FDA 特定的是按管辖来源分流的默认结论 + 违禁史/进口警报作为量化概率输入的评估方法 + 禁用药物零容忍清单"
- id: pV-61
  title: EMA 判定与强化响应
  type: principle
  group: G7-化学危害
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.4.1.6（聚焦历史掺杂模式，即使与具体供应商无关：三聚氰胺例）
      - Ch12 §12.3.11（香料加铅盐增重模式 + 2023 肉桂苹果酱铅铬酸盐事件）
      - Ch12 §12.10.2（疑似人为掺杂→停产/隔离/通知/立即断供/复测库存的五步升级）
  V2_predictive_power:
    passed: true
    novel_question: "新到肉桂铅含量是常规值的 50 倍但没超标法规限量，怎么处理？"
    derived_answer: "数值异常+已知掺杂模式（铅铬酸盐增重）=疑似 EMA→立即触发强化响应：暂停相关生产、隔离已产品、通知并立即断供该供应商、复测现有库存——不等法规限量、不依赖供应商解释"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'超标才处理'；FDA 特定的是 EMA 的模式化判定（跨供应商跨产品假设故意）+ 疑似掺杂时'无缓冲断供'的响应等级与常规超标处置完全不同"
- id: pV-62
  title: 真菌毒素双手段 + 商品-毒素对应
  type: principle
  group: G7-化学危害
  V1_cross_domain:
    passed: true
    evidence:
      - Ch4 §4.3.6/§4.3.7（储藏水分控制 + 物理分选去个别污染籽粒）
      - Ch12 §12.3.6.1（USDA 营销令与分级体系作为前置防线）
      - 附录 1 A1.6.2.6（黄曲霉毒素→花生/玉米/树坚果；DON→小麦大麦；棒曲霉素→苹果）
  V2_predictive_power:
    passed: true
    novel_question: "采购的花生已有 USDA 营销令黄曲霉毒素阴性证明，还需要自己的供应链程序吗？"
    derived_answer: "营销令是第一道防线而非替代：把它作为供应商表现证据纳入批准因素，但毒素已形成不可消除——验证设计仍按自家危害分析（如到货分选+周期检测），对应表锁定验证对象为黄曲霉毒素"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'发霉的挑掉'；FDA 特定的是毒素不可逆前提下的两个技术杠杆（储藏水分/分选）+ 毒素与商品的固定对应表直接锁定供应链验证对象"
- id: pV-63
  title: 婴幼儿毒元素分层控制
  type: principle
  group: G7-化学危害
  V1_cross_domain:
    passed: true
    evidence:
      - Ch12 §12.3.5（婴幼儿食品毒元素一律按供应链预防控制）
      - Ch12 §12.10/§12.11（Manufacturers A/B：未升格元素仍设采购规格+年审；季度成品检测；超标三步响应）
      - Ch12 §12.11.1（本厂检测史把砷/铅升格为需控危害——自家数据比文献更有分量）
      - 附录 1 A1.6.1.5（婴儿配方粉 106.55(e) 强制微生物标准）
  V2_predictive_power:
    passed: true
    novel_question: "镉没有判定为需预防控制，采购合同里就不用管它吗？"
    derived_answer: "要管：分层控制——判为预防控制的（铅/砷）走供应链程序，未升格的镉仍在采购协议中设规格、要求供应商周期检测并年审提交；检测数据同时作为再分析的体系有效性体温计"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'有标准照标准'；FDA 特定的是按人群脆弱性整体升格（不给 CGMP 选项）+ 判定外的分层规格 + 用自身检测史作为发生概率直接证据的判定方法"
- id: pV-64
  title: 毒元素动态标准跟踪
  type: principle
  group: G7-化学危害
  V1_cross_domain:
    passed: true
    evidence:
      - Ch12 §12.10.2/§12.11.2（两示例厂 PCQI 半年复核 Closer to Zero）
      - 附录 1 A1.6.2.5（行动水平散布于 CPG/GFI 且持续迭代，附录不设快照值）
  V2_predictive_power:
    passed: true
    novel_question: "去年定的果汁铅内控规格今年还有效吗？"
    derived_answer: "不确定：婴幼儿相关行动水平随时可能被 Closer to Zero 迭代调整——任何单一快照都不是永久标准，须建立周期复核机制（如半年）+ FDA 来函即查，必要时同步调整采购规格与危害分析"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'标准变了再改'；FDA 特定的是把'标准本身在动'制度化为复核义务（数值化频率+触发事件），标准跟踪成为危害分析维护的一部分"
- id: pV-65
  title: 监管终点限值 → 自建原料内部规格（DON 链）
  type: principle
  group: G7-化学危害
  V1_cross_domain:
    passed: true
    evidence:
      - Ch12 §12.12 脚注（FDA 只对成品设 DON 咨询水平，原料须自建内部规格反推）
      - Ch12 §12.12（检测频次四类触发：新粮首批/产区周报/地堆储存/检出率上升）
      - Ch12 §12.13/§12.14（签约前审查供应商程序或自测数批；逐级保证传递至隔级下游）
  V2_predictive_power:
    passed: true
    novel_question: "FDA 没有给燕麦原料设霉菌毒素限值，采购就不用设指标吗？"
    derived_answer: "监管限值缺位 ≠ 无需限值：以成品限值为反推目标，由 PCQI 基于自身工艺建立原料内部规格；检测频次由信息流（新粮/产区报告/检出率）驱动而非固定日历；隔级采购则审查直接供应商的评估程序"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'没标准就没义务'；FDA 案例链演示了反向转化模式：终点限值→过程规格、日历检测→信息驱动、直接审核→逐级程序传递，三级通用化"
- id: pV-66
  title: 偶带物质双判据（硫化剂 10 ppm）
  type: principle
  group: G7-化学危害
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.4.2.2（<10 ppm 且无技术作用才为 incidental；超最大使用水平即化学危害）
      - 附录 1 A1.6.2.2（标签声明义务的同一判据）+ A1.7.2（误配料构成工艺相关化学危害）
  V2_predictive_power:
    passed: true
    novel_question: "共线生产含亚硫酸盐果干和不含的坚果，标签义务怎么判？"
    derived_answer: "若无意把亚硫酸盐带入坚果产品且 >10 ppm 或有技术作用→既构成标签违规也构成工艺相关化学危害（误配料）；控制策略是配方管理+共线隔离，10 ppm 是豁免与危害的分界线"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'添加剂要标'；FDA 特定的是双判据豁免线（含量+技术作用）+ 该数值同时是标签义务与危害判定的分界点"
```

## G8 召回响应

```yaml
- id: pV-67
  title: 召回执行三机制——公众警告/有效性核查/决策人事先指定
  type: principle
  group: G8-召回
  V1_cross_domain:
    passed: true
    evidence:
      - Ch14 §14.5.2（公众警告：紧迫+其他手段不足；Enforcement Report 列出≠公众警告）
      - Ch14 §14.5.3（有效性核查=验证已送达+已行动，非"发通知"本身）
      - Ch14 §14.6（团队+替任+四项信息+明确召回决策人）
  V2_predictive_power:
    passed: true
    novel_question: "召回启动后要不要立刻发社交媒体声明？"
    derived_answer: "按事先书面化标准判定：公众警告仅用于紧迫且其他阻止使用手段不足的情形；且 FDA 执法报告公示不等于须公开警告——判定标准应预写在召回计划里而非临场拍板"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'出事就广而告之'；FDA 特定的是公众警告为最后手段 + 通知必须配'回执验证'环节 + 决策权与通讯录事先书面化的危机设计"
- id: pV-68
  title: 召回时序——FDA 先行 + RFR 24 小时
  type: principle
  group: G8-召回
  V1_cross_domain:
    passed: true
    evidence:
      - Ch14 §14.7.2（决定召回后立即通知 FDA 协调员，先于媒体与客户）
      - Ch14 §14.7.1（可报告食品确定后 24 小时内电子报告 RFR）
      - Ch15 §15.11.2.1（含 SAHCODH 危害的食品即可报告食品——两章衔接）
  V2_predictive_power:
    passed: true
    novel_question: "想先安抚大客户再向 FDA 报告，可以吗？"
    derived_answer: "顺序反了：监管沟通在对外沟通之前——先 FDA 协调员（及 RFR 24 小时限时），再媒体与客户；顺序错误会同时放大法律与声誉风险，且 24 小时是硬时限"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'先控制舆情'；FDA 规定通知次序的刚性（监管优先）+ RFR 24 小时数值时限——时序本身是合规要求而非公关策略"
```

## G9 双法规与管辖边界

```yaml
- id: pV-69
  title: 双法规并集原则——可借用、不可免除
  type: principle
  group: G9-双法规与管辖
  V1_cross_domain:
    passed: true
    evidence:
      - Ch16 §16.2.3（双向借用只能部分满足）
      - Ch16 §16.12/§16.13/§16.10.1（3 年记录、容器编码、Form 2541e 三大专项缺口）
      - Ch16 表 16-3/16-4（BPCS 专项培训与 PCQI 资质互不替代）+ 表 16-6（召回计划补"通知 FDA"）
  V2_predictive_power:
    passed: true
    novel_question: "酸化食品企业把 PCHF 的 FSP 做全了，还要单独做什么？"
    derived_answer: "找两套要求中互相缺位的项并补齐：3 年记录保存、容器编码、Form 2541e 提交、BPCS 专项培训、召回计划加'通知 FDA'程序——合规=义务并集，借用只减少重复工作量不减少义务总量"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'满足更严的那个就行'；FDA 特定的是并集逻辑：两套法规是叠加关系，各专项超出部分逐项独立存在——'取严'是错误策略"
- id: pV-70
  title: 管辖边界——LACF/FSIS 分割与表格解耦
  type: principle
  group: G9-双法规与管辖
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 1 A1.5.5（LACF 生物危害豁免 PCHF 但化学物理仍适用；多表脚注重申）
      - 附录 1 A1.6.1.4（FSIS 管辖产品作配料仍须自己做危害分析）
      - 附录 1 A1.6.1.6（表格列出与控制主体解耦——无论自控还是供应商控）
  V2_predictive_power:
    passed: true
    novel_question: "供应商的蛋液已过 USDA 检查并巴氏杀菌，还要在危害分析里列沙门氏菌吗？"
    derived_answer: "列（识别端不筛选）：表格列出的是潜在危害，与控制主体无关；USDA 检查不能替代收货方自己的判定——分析后可得出'由供应商巴氏杀菌控制'的结论，但识别与评估不可省略"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'有别的机构管就不用管'；FDA 特定的是管辖按危害类型切割（LACF 只豁生物）、供应商检查不转移判定责任、识别与控制解耦的三重结构"
```

## G10 附录工具使用纪律

```yaml
- id: pV-71
  title: 速查数据使用纪律——极端值警示 + 模型须验证
  type: principle
  group: G10-附录工具纪律
  V1_cross_domain:
    passed: true
    evidence:
      - Ch3 §3.3.1/§3.3.2（Table 3-A 数值为文献极端值且多来自实验室培养基）
      - 附录 3 Table 3-A 引言（食品基质影响生长：竞争菌群/营养/抑菌剂）
      - 附录 3 Table 3-C 后（PMP/ComBase 预测与实测可显著偏差——模型输出须验证后才可作关键限值依据）
  V2_predictive_power:
    passed: true
    novel_question: "ComBase 预测我的酱料在 25°C 下 48 小时内沙门氏菌不生长，能直接写成关键限吗？"
    derived_answer: "不能：模型输出是假设不是关键限——FDA 明确不背书且警告迟滞期等显著偏差；由模型导出的时间温度限值必须经自身产品验证后才可写入 FSP；速查表数值同理只作筛选与方向判断"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'有数据就能用'；FDA 特定的是对自家工具的一致性警示：极端值+培养基来源+基质效应三重失真警告 + '模型→验证→限值'的强制顺序"
- id: pV-72
  title: 危害的用途依赖性——状态与用途决定危害集
  type: principle
  group: G10-附录工具纪律
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 1 Table 1J/1N/1O/1F/1H/1E 脚注（干配料水合到允许生长的 a_w 才考虑芽孢菌，6+ 处）
      - 附录 1 Table 1P（蜂蜜 C. botulinum 仅婴儿用途）+ Table 1L（未酸化浸泡油才考虑肉毒）
      - 附录 1 A1.5.4/A1.6.1.1（多组分按原料+工艺评估；奶粉用于婴儿配方粉须考虑 Cronobacter）
  V2_predictive_power:
    passed: true
    novel_question: "同一批干辣椒粉，卖给干拌料厂和卖给蘸酱厂，危害分析一样吗？"
    derived_answer: "不一样：干混用途下芽孢菌不是潜在危害；进入水合高水分产品（蘸酱）则 B. cereus 等进入危害分析——接收时的危害评估要写明'取决于下游用途'，原料表+用途+工艺三者共同决定危害集"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'原料危害是固定属性'；FDA 特定的是危害随水合状态/最终用途/婴儿暴露切换——同一原料对不同买家是不同的危害对象"
- id: pV-73
  title: 附录空白 ≠ 无危害
  type: principle
  group: G10-附录工具纪律
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 1 A1.6.2.2–A1.6.2.4（过敏原/辐射/二噁英/未批准添加剂刻意不在化学表中）
      - 附录 1 A1.7（工艺设施相关危害 2016 版起删除表格，须每厂自建）
      - 附录 1 Table 1A 脚注等（夹杂物须叠加查其自身表，6 处）+ A1.4（非穷尽、截至 2022）
  V2_predictive_power:
    passed: true
    novel_question: "做植物基新蛋白饮料，附录 1 查不到该原料怎么办？"
    derived_answer: "表格空白≠无危害：特殊配料（海藻/植物蛋白/发酵蛋白）本就不在表内——用供应商 TDS、Food Chemicals Codex、FDA 规格、GRAS 回复补齐；产品含夹杂物还要叠加夹杂物自身表；产地依赖危害按三检验过滤"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'权威表格覆盖一切'；FDA 明示工具的边界（五类排除+工艺危害无表+夹杂物叠加+2022 数据截止）——把'什么时候不能信表'写成了使用说明"
- id: pV-74
  title: 极强致死工艺——产品属性即"No"的依据
  type: principle
  group: G10-附录工具纪律
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 1 A1.6.1.3 / A1.8.3 脚注（焦糖 240°F 煮沸、果酱熬煮、咸饼干 250°C×4.5min——工艺致死性与产品质地绑定，SME 未标潜在危害）
  V2_predictive_power:
    passed: true
    novel_question: "传统熬制在高热下数小时的糖果，还需要为生物危害设计控制吗？"
    derived_answer: "可判定'No'：若工艺的产品属性要求（质地/稠度）本身绑定极强致死条件（不充分加热就做不出合格产品），工艺参数即构成"No"的科学依据——判定仍须书面化并引用工艺证据"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'食品都要控菌'；FDA 特定的是承认一类结构性安全：产品可销性要求与致死性绑定的工艺自带屏障，可作为无需控制的合法科学依据"
```

---

## 汇总统计

| 主题组 | 通过数 |
|---|---|
| G1 危害分析方法 | 15 |
| G2 数值界限与工艺控制 | 14 |
| G3 管理组件 | 11 |
| G4 环境病原与卫生 | 4 |
| G5 过敏原 | 6 |
| G6 供应链 | 8 |
| G7 化学危害 | 8 |
| G8 召回 | 2 |
| G9 双法规与管辖 | 2 |
| G10 附录工具纪律 | 4 |
| **用户捞回** | 2 |
| **合计** | **76** |

---

## 用户捞回条目（阶段 1.5 轻确认时由用户决定捞回，人工补录验证记录）

- id: pV-75
  title: 危害分析支点思维（分析做错则整个 FSP 无效）
  type: principle
  group: G1-危害分析方法
  salvaged_from: rV-04（原淘汰理由 V3"近似 GIGO 常识"）/ 另见 fA-21
  V1_cross_domain:
    passed: true
    evidence:
      - Ch2 2.2: 危害分析做错/漏识别则整个 FSP 无效——"无论工厂执行得多好"
      - Ch1 1.4: FSP 与 HACCP 对比中危害分析被列为第一差异要素（化学含放射、EMA 纳入）
      - Ch5 5.1: 即使判定无需预防控制，判定本身也必须写入书面危害分析（117.130(a)(2)）
  V2_predictive_power:
    passed: true
    novel_question: "检查前发现某使用三年的设备从未出现在工艺流程图上，该先做什么？"
    derived_answer: "优先补危害分析而非先加控制措施：支点效应意味着任何'额外控制'的充分性都无法在缺失节点下证明——先核实流程图、对涉及该设备的所有步骤重做识别与评估、书面记录再分析依据"
  V3_exclusivity:
    passed: true
    why_not_common: "GIGO 是通用常识，但 FDA 的特定制度化形态是'无控危害也要书面+签署+PCQI+3 年再分析'——支点被做成了有签名、有时限、可检查的法定文件，而非口头原则"
  → 进入阶段 1.6（用户捞回）

- id: pV-76
  title: 政府检查书面结果可有条件替代现场审核（1 年内 + 适当性判定）
  type: principle
  group: G6-供应链
  salvaged_from: rV-16（原淘汰理由 V1 单语境；用户决定捞回）
  V1_cross_domain:
    passed: true
    evidence:
      - Ch15 15.12.3: FDA/USDA/州等机构 1 年内的"适当"检查书面结果可替代现场审核；USDA 有机认证检查不可替代；外国政府 HACCP 证书不能直接替代
      - Ch15 15.12.4: 仅满足 subpart G 的审核不必遵守第三方认证法规——同一活动在不同法规语境下效力不同，"替代"须判语境
  V2_predictive_power:
    passed: true
    novel_question: "供应商刚通过某国际认证机构的 GFSI 审核，能免掉今年的现场审核吗？"
    derived_answer: "GFSI 审核不是政府检查，不满足'适当检查书面结果'的替代条件；但可作为 PCQI 书面认定免年审的证据链一部分——先分清'法定替代'与'论证性豁免'两条不同通道"
  V3_exclusivity:
    passed: true
    why_not_common: "'有官方检查就不必再审'背后藏着一组 FDA 特定判定：时效（1 年内）、适当性（与危害相关、含书面计划审查）、可替代性排序（政府检查 > 第三方审核 > HACCP 证书 > 有机认证）——这是等效性判定而非证书收集"
  → 进入阶段 1.6（用户捞回）

