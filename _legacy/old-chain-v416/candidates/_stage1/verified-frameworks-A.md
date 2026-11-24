# Verified Frameworks — A 池（chunk 1–3）

> 阶段 1.5 三重验证通过项。V1=跨域佐证，V2=预测力，V3=独特性。

```yaml
- id: fA-01
  title: 六列危害分析工作表法
  type: framework
  merged_from: [f1-01]
  group: 危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch2: 方法论核心（识别/评估/判定/理由/控制/落点六列强制解耦）
      - chunk3 Ch6: Cookie A/B、Soup A/B、Salsa A 全部示例厂以同一六列表呈现，Appendix 2 表单化
  V2_predictive_power:
    passed: true
    novel_question: "引入 AI 客服系统，如何做上线前的组织风险分析？"
    derived_answer: "按环节（训练数据/上线/人工接管/回滚）逐行填六列，任何一格空缺即分析不完整；'是否在本环节控制'独立成列，强制回答控制落点（如数据端而非客服端）而非直觉默认"
  V3_exclusivity:
    passed: true
    why_not_common: "通用 HACCP 判定树只处理 CCP；六列法把'未控危害'也强制留行留理由，且控制落点与发现点显式解耦——超出判定树的结构"
  → 进入阶段 2

- id: fA-02
  title: 书面 Yes/No 判定——解释 No 与解释 Yes 同等重要
  type: framework
  merged_from: [f1-02]
  group: 危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch2 Column 4: 原则出处（保守列示潜在危害再论证排除）
      - chunk3 Ch6/Ch11: Soup A 替代审查时限、Soup B 豁免检测、过敏原声明三选一——全部以书面论证承载"不做什么"
  V2_predictive_power:
    passed: true
    novel_question: "需求评审砍掉的功能，半年后老板问'为什么没做'怎么办？"
    derived_answer: "被砍项也编号入清单并写否决理由，使每个 No 成为'被考虑过的 No'；空白论证等于未考虑，写下才算辩护防线"
  V3_exclusivity:
    passed: true
    why_not_common: "常识说'记录决策'；此法方向相反——主动把排除项列入清单做保守列示，把'负向判定'本身变成交付物"
  → 进入阶段 2

- id: fA-09
  title: RTE 环境病原强制评估触发规则（if-then）
  type: framework
  merged_from: [f1-09]
  group: 危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch2 117.130(c)(1)(ii): 正面触发规则（RTE + 暴露 + 无后置致死 → 强制评估）
      - chunk3 Ch6 6.15.5/6.16.5: Soup B/Salsa A 以同一条件的否定式反推豁免（处理后不暴露 → 免环境监测）
  V2_predictive_power:
    passed: true
    novel_question: "离线笔记本带出办公网，数据需要安全审查吗？"
    derived_answer: "IF 数据离开受控环境 AND 归档前无脱敏/加密 THEN 强制评估——与'我觉得没风险'无关，两个客观条件相与即触发"
  V3_exclusivity:
    passed: true
    why_not_common: "把'是否需要评估'从主观判断题改为可观测条件核对题，主观自评无豁免权——立法式触发器设计，非通用质量管理内容"
  → 进入阶段 2

- id: fA-11
  title: 发现点 ≠ 控制点（列 6 逻辑）
  type: framework
  merged_from: [f1-11]
  group: 危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch2 Column 6: 独立 Yes/No 列承载"危害步骤 ≠ 控制步骤"
      - chunk3 Ch11 11.8: 供应链控制把控制前移到接收之前——危害在供应商、控制在收货方
  V2_predictive_power:
    passed: true
    novel_question: "客服端高频投诉'找不到入口'，在哪修？"
    derived_answer: "不按发现点（客服话术）处置，按杠杆最大点（产品文案/信息架构）处置；工作表式的独立列强制显式选位，防止'在哪发现在哪修'直觉"
  V3_exclusivity:
    passed: true
    why_not_common: "HACCP 常识把控制设在关键步骤；PCHF 明示可前移（供应链）/后移（成品检测），并给出'可控制性本身构成 Yes 理由'的决策结构"
  → 进入阶段 2

- id: fA-14
  title: 多组分界面微环境推理
  type: framework
  merged_from: [f1-14]
  group: 工艺危害与屏障
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch2 2.4.2.4: 十类评估因素指向多组分界面等典型失效模式
      - chunk1 Ch3 3.3.4.2.3: 泡芙夹心/鹰嘴豆泥顶料专节——整体 a_w/pH 安全 ≠ 界面安全
  V2_predictive_power:
    passed: true
    novel_question: "两个各自通过安全评审的微服务对接，最容易出什么事？"
    derived_answer: "故障高发点在交界（超时/编码/重试语义不匹配）而非任一服务内部；必须评估接口局部契约，不能只看两端各自参数"
  V3_exclusivity:
    passed: true
    why_not_common: "'整体性质安全≠处处安全，薄弱点在异质交界'是基于 pH/a_w 渗透的微环境推理，通用质量体系无此分析层"
  → 进入阶段 2

- id: fA-15
  title: 栅栏逻辑：屏障组合判定 + "先腐败后危害"
  type: framework
  merged_from: [f1-15, f2-31]
  group: 工艺危害与屏障
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch3 3.3.4.2.4: ROP 五屏障准入核对（弱屏障可组合成有效屏障）
      - chunk2 Ch4 4.3.3.1: 面包三重屏障叠加，设计追求"腐败先于危害"的感官警讯
  V2_predictive_power:
    passed: true
    novel_question: "客户端引入本地缓存技术前要核对什么？"
    derived_answer: "先列失效屏障清单（过期/并发/容量），单项弱屏障可组合达标再准入；并检查系统是否具备'先报错后损坏'的警讯属性——无警讯组合（如 ROP 先产毒后腐败）天然高危"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是单项达标才用；栅栏逻辑允许弱屏障组合，并把'警讯先于风险'当作显式设计目标——双重反直觉"
  → 进入阶段 2

- id: fA-17
  title: 目标菌选择法（情境→最耐药靶→削减倍数→残余分配）
  type: framework
  merged_from: [f1-17, f2-10, f3-08]
  group: 工艺危害与屏障
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch3 3.3.4.1: 孢子/营养细胞二分，按最抗性目标设计
      - chunk2 Ch4 4.3.1.1: 靶菌选定后 5D–7D/6D 强度档位跟随
      - chunk3 Ch6 6.15: Soup B 由包装（ROP）+储运（冷藏）情境推约束病原（非蛋白分解 C. botulinum）
  V2_predictive_power:
    passed: true
    novel_question: "面向弱网设备的性能基线怎么定？"
    derived_answer: "由部署情境推出约束用户画像→选最严苛者设基线→其余用户自动覆盖→残余风险显式分配给后置控制（降级/兜底），而非把所有用户堆进一个处理"
  V3_exclusivity:
    passed: true
    why_not_common: "通用说法是'考虑最坏情况'；此法给出'情境→约束对象→最耐靶→削减倍数→残余分配'的完整推导链，且对手是可枚举的具体病原"
  → 进入阶段 2

- id: fA-18
  title: Transient vs Resident 环境病原判定
  type: framework
  merged_from: [f1-18, f2-02]
  group: 环境病原控制战略
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch3 3.3.5.2: 定义与 niche 藏匿点机制
      - chunk2 Ch4 4.4: 清洁策略/卫生分区均以"阻断瞬时→定殖转化"为前提展开
  V2_predictive_power:
    passed: true
    novel_question: "线上偶发 500 错误，何时该放弃重试转做根除？"
    derived_answer: "判据是时间持续性+指纹一致性而非频次：同一 trace 特征反复出现=系统藏匿点（配置/连接池 niche），常规重启（=常规清洁）无效，必须升级为根除项目"
  V3_exclusivity:
    passed: true
    why_not_common: "'偶发 vs 系统性'看似常识，但'常规手段对定殖态无效、判据是株型一致性与持续性'是环境微生物学特定结论，处置路径完全分叉"
  → 进入阶段 2

- id: fA-20
  title: FSP 动态再分析触发器（周期 + 事件双轨）
  type: framework
  merged_from: [f1-20]
  group: 体系架构与动态维护
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch1 1.7: 双轨触发与"可限于相关部分"的增量许可
      - chunk2 Ch5 5.5.3: 纠正措施查历史记录→反复问题触发再分析
      - chunk3 Ch11 11.6.1.3: 设计失效（重复发现）→ 触发 FSP 再分析
  V2_predictive_power:
    passed: true
    novel_question: "个人知识库/团队运维手册如何防止与现实静默漂移？"
    derived_answer: "周期全量复审兜底 + 事件触发（新信息/意外事故/手段失效/变更）增量复审相关部分——全量与增量的成本权衡被显式写进规则而非靠自觉"
  V3_exclusivity:
    passed: true
    why_not_common: "常识只有'定期评审'；此法是周期兜底+事件驱动+允许部分更新的三件套设计，且事件类型学被明文枚举"
  → 进入阶段 2

- id: fA-22
  title: 屏障覆盖缺口检查（过程后添加配料）
  type: framework
  merged_from: [f1-22]
  group: 工艺危害与屏障
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch3 3.3.4.3: 杀菌后添加的配料走"无控制通道"，须单独评估
      - chunk3 Ch6 6.15.5: Soup B 以同一覆盖边界反面论证——处理后不暴露故免检测
  V2_predictive_power:
    passed: true
    novel_question: "每晚全量备份后录入的数据，在备份策略里处于什么位置？"
    derived_answer: "处于保护窗口之外——屏障只保护其覆盖期内的对象，之后进入的要素需重新评估并配独立控制（增量同步），'有备份'不等于'都在备份里'"
  V3_exclusivity:
    passed: true
    why_not_common: "直觉是'成品是熟的就安全'；此法要求逐项追问防护屏障的覆盖边界，之后进入者视为走无控制通道——显式缺口检查"
  → 进入阶段 2

- id: fA-23
  title: 冷却窗口与竞争菌群消失推理
  type: framework
  merged_from: [f1-23]
  group: 工艺危害与屏障
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch3 3.3.4.2.2: 杀灭步骤清场→幸存孢子在冷却窗口获得生态优势
      - chunk2 Ch4 4.3.2.1: 危险温区/迟滞期与冷却协议作为配套控制展开
  V2_predictive_power:
    passed: true
    novel_question: "抗生素疗程结束后，为什么反而要防特定菌定殖？"
    derived_answer: "干预清除了竞争菌群，幸存者获得生态位与资源优势——处理过的系统比未处理更怕后续滥用，需独立设计过渡期控制窗口"
  V3_exclusivity:
    passed: true
    why_not_common: "反直觉：杀伤步骤制造新风险窗口（工序交接处比工序内部更危险），通用'杀灭即安全'直觉正好相反"
  → 进入阶段 2

- id: fA-24
  title: 湿/干环境二分法（环境病原控制战略选择器）
  type: framework
  merged_from: [f2-01]
  group: 环境病原控制战略
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch3 3.3.5.3: 分类→头号病原映射（湿=李斯特菌，干=沙门氏菌）
      - chunk2 Ch4 4.4.1/4.4.2: 清洁策略三选一与卫生分区均以此二分法为决策锚点
  V2_predictive_power:
    passed: true
    novel_question: "数据中心冷通道/热通道，清洁与巡检策略要一样吗？"
    derived_answer: "不一样：先按'温度×介质'分类环境→识别各象限头号失效源→两个象限的最优策略可能完全相反（一个怕水一个更怕水），单一 SOP 必然在某一象限失效"
  V3_exclusivity:
    passed: true
    why_not_common: "'环境分类→对手识别→战略反转'的结构是 PCHF 特有的战略选择器——两类环境的核心对策（保持干燥 vs 严格控水）表面相同实质相反"
  → 进入阶段 2

- id: fA-25
  title: 化学危害按引入路径分流控制
  type: framework
  merged_from: [f2-03]
  group: 化学危害与供应链
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch3 3.4.1.3: 同一重金属按来源（土壤/设备浸出/配方）分流到不同控制类型
      - chunk3 Ch11 11.8: 过敏原危害按"接收前可控制与否"分流到供应链程序
  V2_predictive_power:
    passed: true
    novel_question: "发生数据泄露，先做什么？"
    derived_answer: "先问从哪条路径进来（员工/接口/第三方），再对路径开药——对'泄露'一词查表套通用控制无效，路径决定控制类型"
  V3_exclusivity:
    passed: true
    why_not_common: "通用表述是'对因下药'；此法给出具体的'路径→控制类型'映射（土壤→供应链、设备→CGMP、配方→工艺控制），分流是可操作的决策结构"
  → 进入阶段 2

- id: fA-32
  title: 工艺控制三步法（科学确立-投送-证明）+ 两步验证
  type: framework
  merged_from: [f2-11, f2-29, f3-03]
  group: 工艺控制与验证
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch4 4.3/Ch6 6.6: 三步框架与文献参数须按基质调整的降级规则
      - chunk3 Ch6 6.12/6.13: Cookie A（大学专家）、Cookie B（咨询）、Soup B、Salsa A 全走"文献定科学需求 × 厂内研究证可达"[本段重现]
  V2_predictive_power:
    passed: true
    novel_question: "采用行业基准定 SLO，为什么照抄不行？"
    derived_answer: "外部基准是'别人基质上的结论'——需按自家负载特征（基质）调整，且'科学要求什么'与'本机实际可达什么'分别取证后取交集，交集才是可承诺的限值"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'参考权威标准'；此法把外部证据降级为起点假设，强制本地化验证并取交集——证据结构而非条文照抄"
  → 进入阶段 2

- id: fA-33
  title: EPIPT 替代逻辑（用终点状态替代全程轨迹监控）
  type: framework
  merged_from: [f2-12, f3-06]
  group: 工艺控制与验证
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch4 4.3.1.1: 三前提（热分布/热穿透/其他关键因素）
      - chunk3 Ch6 6.14.2: Soup A 量化升降温免费致死量后采用 EPIPT，且 f3-10 以之为简化记录审查的论证前提
  V2_predictive_power:
    passed: true
    novel_question: "多层防护的系统里，能否用一次终态断言替代全程打点？"
    derived_answer: "当过程自然裕量（升降温段额外致死）经量化后远超要求时，可只监控终点状态——但简化的合法性来自一次性研究的完备性，未研究的关键因素不可省"
  V3_exclusivity:
    passed: true
    why_not_common: "'用前期研究购买日常监控简化'的交换模型非常识——简化不是拍脑袋省事，而是有明确的三前提审计链"
  → 进入阶段 2

- id: fA-34
  title: 代理参数转译法（不可测量→有函数关系的可测代理量）
  type: framework
  merged_from: [f2-13, f3-05, f3-07]
  group: 工艺控制与验证
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch4 4.3.1.1: 传导型大颗粒不可抽查→义务前移为验证关键因素
      - chunk3 Ch6 6.13/6.15: 批式→批时间、连续→泵速/保压管尺寸的参数映射
      - chunk3 Ch6 6.14/6.16: Soup A（13mm）/Salsa A（1.0cm）颗粒尺寸代理[本段重现]
  V2_predictive_power:
    passed: true
    novel_question: "'用户实际体验'不可实时测量，监控什么？"
    derived_answer: "找到与目标量有确定函数关系的可测代理（p99 延迟+错误率），并把代理成立的前提（客户端类型/网络分级）用实验确定、以 SOP 固化——前提成立时代理测量等价于直接测量"
  V3_exclusivity:
    passed: true
    why_not_common: "通用监控说'选可测指标'；此法要求代理量与目标的函数关系被研究确立、物理不可测时把前提本身固化为受控条件——转译是可审计的"
  → 进入阶段 2

- id: fA-38
  title: pH 4.6 分界线的双重角色（抑菌依据 + 管辖判据）
  type: framework
  merged_from: [f2-17]
  group: 工艺危害与屏障
  V1_cross_domain:
    passed: true
    evidence:
      - chunk1 Ch3 3.3.4.2.4: pH<4.6 作为 ROP 肉毒屏障之一
      - chunk2 Ch4 4.3.3.2: 同一数值被借用作 LACF/酸化食品法规管辖分界，且须防腐败菌产碱拉回 pH
  V2_predictive_power:
    passed: true
    novel_question: "往低酸配方里加酸酸化，除了口感还改变了什么？"
    derived_answer: "可能切换法规管辖体系（part 114 而非 PCHF），且酸化是大颗粒数天才能达到终平衡 pH 的过程、须同时控制腐败菌——改一个参数前先查它是否兼任管辖判据"
  V3_exclusivity:
    passed: true
    why_not_common: "'一个科学阈值承担抑菌依据+管辖权判据双重角色'及'腐败产碱使肉毒风险复活'的级联洞察，超出通用 HACCP 常识"
  → 进入阶段 2

- id: fA-42
  title: CGMP vs 预防控制身份判定与升格法
  type: framework
  merged_from: [f2-21, f3-15]
  group: 体系架构与动态维护
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch4 4.4: 同一清洁动作的身份由危害分析指派（卫生控制 vs CGMP）
      - chunk3 Ch11 11.4.1: 升格操作化——CGMP 措施 + 管理组件（监控/验证）即成预防控制
  V2_predictive_power:
    passed: true
    novel_question: "安全基线已全覆盖但预算有限，重点加固谁？"
    derived_answer: "同一实践可有两重身份：先全厂铺基线（不逐项监控），再由风险分析挑选最高风险项'升格'——最小操作是捆绑监控+记录，义务按需分配而非一刀切"
  V3_exclusivity:
    passed: true
    why_not_common: "'身份由危害分析指派而非由活动类型决定'违反'清洁就是清洁'的直觉；升格给出了基线→受管的最小增量路径"
  → 进入阶段 2

- id: fA-43
  title: 控制手段适用性矩阵 × 短板匹配法
  type: framework
  merged_from: [f2-22, f2-32]
  group: 工艺控制与验证
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch3 3.3.4.1/Ch5 Table 5-1: 热处理杀营养细胞不灭孢子不消除毒素；控制×危害适用性逐格标注
      - chunk2 Ch4 4.3.1.2: HPP 短板（孢子）×产品既有屏障（酸/冷藏）匹配推理
  V2_predictive_power:
    passed: true
    novel_question: "打算引入差分隐私，它能独立解决数据安全吗？"
    derived_answer: "先找它防不了的对手（内部恶意者/侧信道），再看产品既有屏障能否补上；补得上→可用，补不上→不可独立使用——技术选型是'能力边界×既有屏障'的匹配而非能力清单比对"
  V3_exclusivity:
    passed: true
    why_not_common: "常识看'控制能干什么'；此法先问'它对哪个靶明确失效'，再匹配产品属性补短板——且矩阵明示方向≠已验证"
  → 进入阶段 2

- id: fA-45
  title: 回溯暴露窗口假设（偏离即假定自上次合格点起失控）
  type: framework
  merged_from: [f2-24]
  group: 管理组件闭环
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch5 5.5.2/5.5.4: 默认推理规则与校准频次的风险含义
      - chunk3 Ch6 6.9/6.15: 偏差处置中"受影响产品=上次合格点以来全部产量"的评估逻辑实例化
  V2_predictive_power:
    passed: true
    novel_question: "监控/校准频次定多少才不是拍脑袋？"
    derived_answer: "频次是'暴露窗口宽度的旋钮'：间隔越长，一次偏离牵连的产品越多——频次决策=单次失效的最大损失×发生概率的风险定价，而非形式要求"
  V3_exclusivity:
    passed: true
    why_not_common: "常识把监控频次当合规参数；此法把它重释为风险定价变量，且给出失控起点的保守默认假设"
  → 进入阶段 2

- id: fA-46
  title: Correction vs Corrective Action 判定边界
  type: framework
  merged_from: [f2-25, f3-16, f4-23, fB-20]
  group: 管理组件闭环
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch5 5.5.3: 两判据（是否影响食品/孤立 vs 反复）与设备残渣示例
      - chunk3 Ch11 11.5.3/11.7.3: 标签'使用前 vs 使用后'同一错误走不同路径[本段重现]
      - chunk4 Ch11 11.13.3.3 + Ch12 12.10.2: Bakery B 以'生产是否已开始'、Manufacturer A 以'物料是否已投入生产'作时间代理边界[跨池重现]
  V2_predictive_power:
    passed: true
    novel_question: "发现数据误发给了错误收件人，算小事故还是大事故？"
    derived_answer: "不按错误自身严重度分级，按两个后验维度：拦截在发出前=correction（重发即可，甚至不必记录）；已送达=损害已发生，触发完整程序（评估/止损/防复发/阻断入市）"
  V3_exclusivity:
    passed: true
    why_not_common: "通用分级看错误严重度；此法用'损害是否已发生'+'是否成模式'两个后验维度定级，同一客观错误因发现时机不同走完全不同路径——反直觉的分诊结构"
  → 进入阶段 2

- id: fA-47
  title: 预授权决策预案（预定纠正措施 + 可/不可再加工清单）
  type: framework
  merged_from: [f2-26, f3-09]
  group: 管理组件闭环
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch5 5.5.3: 预定程序三优势（无压力时从容决策/免去临场重评）
      - chunk3 Ch6 6.15.4: Soup B 预写可/不可再加工清单，偏差时查表执行
  V2_predictive_power:
    passed: true
    novel_question: "事故响应预案写到什么粒度才算可用？"
    derived_answer: "按产品/情境穷举处置选项并书面预授权，紧急时刻降级为查表执行；专家判断仅保留'清单未覆盖的安全问题'一权——把决策质量与现场压力解耦"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'写个预案'；此法的关键是'预授权把紧急决策降级为查表，同时显式保留唯一例外判断权'的权限设计"
  → 进入阶段 2

- id: fA-49
  title: 例外记录模式（只记异常）
  type: framework
  merged_from: [f2-28, f3-25]
  group: 管理组件闭环
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch5 5.5.2: 法规允许连续监控场景下只建失控记录
      - chunk3 Ch11 11.5.6/11.7.5: 自动条码扫描/自动 CIP 记录的实例化
  V2_predictive_power:
    passed: true
    novel_question: "高频检查的记录负担能否合法削减？"
    derived_answer: "先给正常态找机器背书（连续扫描/自动记录），人工记录只留给异常——记录成本从 O(n) 降到 O(异常数)，且记录本身从合规负担反转为异常信号"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'凡事留痕'；此法反转：省的是正常态记录而非监控动作，前提是正常态有可靠背书——削减有明确的合法性条件"
  → 进入阶段 2

- id: fA-50
  title: 关键限值 vs 操作限双线设计
  type: framework
  merged_from: [f2-30, f3-04]
  group: 管理组件闭环
  V1_cross_domain:
    passed: true
    evidence:
      - chunk2 Ch6 6.5: 概念定义（红线 vs 内控线 vs adjustment）
      - chunk3 Ch6 6.12.2: Cookie B 烘焙 13 分钟关键限/15 分钟操作限实例化
  V2_predictive_power:
    passed: true
    novel_question: "SLO 和硬性红线要不要设成同一个值？"
    derived_answer: "不：给安全红线外配一条更严的内控线（error budget），让质量原因的波动在缓冲带被日常 adjustment 吸收，避免频繁触发高成本的产品处置程序——两类偏离分流"
  V3_exclusivity:
    passed: true
    why_not_common: "常识只有'红线'；双线设计让'碰内控线不算安全事件'，用缓冲带吸收波动的同时保住安全程序的严肃性——分级响应而非单一阈值"
  → 进入阶段 2

- id: fA-51
  title: 热处理偏差处置决策链（递进选项谱系）
  type: framework
  merged_from: [f3-01]
  group: 管理组件闭环
  V1_cross_domain:
    passed: true
    evidence:
      - chunk3 Ch6 6.9: 六级阶梯（补足→再加工→暂存评估→改用途→转饲料→销毁）
      - chunk3 Ch6 6.12–6.16: Cookie A/B、Soup A/B、Salsa A 五个示例的纠正措施全部套用此阶梯、仅选项组合不同[本段重现]
  V2_predictive_power:
    passed: true
    novel_question: "发现一批数据算错了，只能删库重跑吗？"
    derived_answer: "沿阶梯评估：补算（继续处理）→降级用途（改非关键场景）→销毁，每级都有'能否用证据证明该用途下问题不成立'的评估主体——先救回、再降级、最后销毁"
  V3_exclusivity:
    passed: true
    why_not_common: "直觉是'放行/销毁'二选一；阶梯给出谱系化处置+每级证据要求+指定评估主体（PCQI），是资产保全导向的偏差思维"
  → 进入阶段 2

- id: fA-52
  title: 验证活动五分类（证明方法有效 vs 证明执行有效）
  type: framework
  merged_from: [f3-02]
  group: 管理组件闭环
  V1_cross_domain:
    passed: true
    evidence:
      - chunk3 Ch6 6.10: validation/监控核查/纠偏核查/实施有效性/再分析五层
      - chunk2 Ch5 5.6: 四类控制免 validation 的义务差异——分类绑定义务
  V2_predictive_power:
    passed: true
    novel_question: "A/B 测试框架上线后，还需要做哪些'验证'？"
    derived_answer: "分开取证：'方法有效'（分流科学、指标合理，一次性/变更时）与'执行有效'（实际分流一致、数据完整，日常核查）不可互相替代——实验室报告不能代替校准记录"
  V3_exclusivity:
    passed: true
    why_not_common: "通用质量体系把'verification/validation'混用；此法拆成五层并指明两类证据不可互替、分类直接绑定义务清单"
  → 进入阶段 2

- id: fA-53
  title: 书面论证作为合规弹性出口（硬规则 + written determination 替代/豁免）
  type: framework
  merged_from: [f3-10, f3-12, f5-15, fB-31]
  group: 管理组件闭环
  V1_cross_domain:
    passed: true
    evidence:
      - chunk3 Ch6 6.14.5: Soup A 以'事实—推理—书面化'论证放行前审查替代 7 天默认审查
      - chunk3 Ch6 6.15.5/6.16.5: Soup B/Salsa A 以暴露剖面论证豁免产品检测与环境监测[本段重现]
      - chunk5 Ch15 15.11.2.2: SAHCODH 年度审核硬规则可经 PCQI 书面认定豁免[跨池重现]
      - chunk4 Ch11: 'may contain'咨询声明同样须 PCQI 书面论证才可用
  V2_predictive_power:
    passed: true
    novel_question: "合规要求的默认参数（频次/范围）不适合我，能改吗？"
    derived_answer: "能，但替代/豁免本身是一条需书面证据链的结论：陈述事实基础→说明为何同等或更优→书面化入 FSP；'风险不存在'的豁免也是结论而非省略"
  V3_exclusivity:
    passed: true
    why_not_common: "常识要么死守默认值要么随意放宽；此法给出合规弹性的第三条路——论证式偏离，且默认值被视为可挑战的假设"
  → 进入阶段 2

- id: fA-56
  title: 过敏原程序三支柱（CGMP 底座 + 双控制 + 供应链前移）
  type: framework
  merged_from: [f3-14]
  group: 体系架构与动态维护
  V1_cross_domain:
    passed: true
    evidence:
      - chunk3 Ch11 11.1: 三层结构定义（CGMP 七方面/交叉接触+标签双控制/供应链程序）
      - chunk2 Ch4 4.4 + chunk3 Ch11 11.4.1: CGMP 与预防控制身份分流是同构思想在卫生/过敏原两域的实例
  V2_predictive_power:
    passed: true
    novel_question: "数据安全治理体系该怎么分层？"
    derived_answer: "同一分层：基线实践（全员适用、不需逐项监控）—重点控制（防不该有的进 + 防该声明的不声明，各配管理组件）—外部前移（供应商/第三方数据处理协议），三层义务密度递增"
  V3_exclusivity:
    passed: true
    why_not_common: "'基线铺底/重点控制增强并管理/厂外环节前移'的分工结构是 PCHF 特定架构——不是简单的分级分类，而是义务密度沿层级递增"
  → 进入阶段 2

- id: fA-58
  title: 供应商咨询声明解码与三选一决定
  type: framework
  merged_from: [f3-18, f3-23]
  group: 化学危害与供应链
  V1_cross_domain:
    passed: true
    evidence:
      - chunk3 Ch11 11.8.3.1: 审批门槛——须查声明是否在替代 CGMP（解码成因）
      - chunk3 Ch11 11.9.3: 收货后三选一（不传递/传递/阈值论证）书面化；Table 11-4 高风险情境实例化
  V2_predictive_power:
    passed: true
    novel_question: "供应商 SaaS 附'不保证可用性'条款，采购流程怎么处理？"
    derived_answer: "先解码成因（真实技术限制 vs 管理惰性）再决定接受条件；传入下游时显式三选一：吸收（我的场景本就覆盖）/透传（同等管控）/量化豁免（残余风险可论证）——禁止默认忽略"
  V3_exclusivity:
    passed: true
    why_not_common: "常规供应商管理把免责声明透传或退回；此法要求'解码不透传'并把上游不确定性声明变成强制三岔决策——不确定性必须被显式处置"
  → 进入阶段 2

- id: fA-59
  title: 供应链风险分级 × 验证强度匹配谱系
  type: framework
  merged_from: [f3-19, f3-20]
  group: 化学危害与供应链
  V1_cross_domain:
    passed: true
    evidence:
      - chunk3 Ch11 11.8.2: 交叉接触潜力按空间/时间/管理/验证证据四维分级
      - chunk3 Ch11 11.8.3.2 Table 11-4: 八情境展示验证强度谱系（独立产线→问卷+年度声明；共线→年审+抽测；改用声明→多批检测）
  V2_predictive_power:
    passed: true
    novel_question: "对云供应商的审计强度该逐年一样吗？"
    derived_answer: "审计强度是因变量：自变量是数据敏感度（SAHCODH 类危害→首次使用前+每年现场审核）×供应商端隔离完备性；且检测因分布不均只能是其他验证活动的补充，不能是唯一手段"
  V3_exclusivity:
    passed: true
    why_not_common: "一刀切年审是常识；此法给出'风险梯度↔活动谱系'的滑动匹配，并把'检测天然有漏检风险、永远不能独立'作为硬约束写入"
  → 进入阶段 2
```
