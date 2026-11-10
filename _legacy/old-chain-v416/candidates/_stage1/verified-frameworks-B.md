# Verified Frameworks — B 池（chunk 4–6）

> 阶段 1.5 三重验证通过项。V1=跨域佐证，V2=预测力，V3=独特性。

```yaml
- id: fB-01
  title: 过敏原排产序列与清洁触发判定
  type: framework
  merged_from: [f4-01, f4-03]
  group: 过敏原控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 Dessert A: 排产序列实例化（sorbet→vanilla 系→almond 收尾）
      - Ch11 11.12.3.1: 序列末尾回无过敏原产品触发专项清洁
      - 附录 11-1.F.2 + 附录 2 Form 2-G: 通用化推荐与表单化（2-G 驱动排产决策）
  V2_predictive_power:
    passed: true
    novel_question: "共用烘焙线上临时插单一批含杏仁产品，排产怎么办？"
    derived_answer: "插单插到同谱系批次槽位即可（集合包含成立，通用清洁够用）；若插到无过敏原产品之后，则集合包含判定失败，必须升级专项清洁——插单成本不是清洁时间，而是谱系位次"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'脏了就清洗'；本框架把清洁决策变成'前序过敏原集合⊆后序过敏原集合？'的可推导判定，用顺序设计替代清洁投入——逆向的排序"
  → 进入阶段 2

- id: fB-03
  title: 标签内容控制 vs 标签管理控制的生命周期二分
  type: framework
  merged_from: [f4-04]
  group: 过敏原控制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 Dessert A（预印包装）: 色码带+条码扫描实现管理控制
      - Ch11 Bakery B（电子打印标签）: 电子文件核对+在线打印核对实现同一控制
      - Ch11 11.11: 明言分类本身不改变监管后果，先有控制、分类可灵活
  V2_predictive_power:
    passed: true
    novel_question: "SaaS 多租户产品，如何防止给 A 客户发 B 客户的配置？"
    derived_answer: "同一二分：'内容控制'管配置文件里写了什么（开发期评审）与'管理控制'管对的配置部署到对的环境（staging/发布/回滚），两段失手点不同，控制手段也不同"
  V3_exclusivity:
    passed: true
    why_not_common: "常识只说'标签别贴错'；本框架把防错沿生命周期切成'写什么'与'用在哪'两个独立失控面，且指出分类学争议不影响后果——防的是两种不同性质的错误"
  → 进入阶段 2

- id: fB-06
  title: 风险比例原则（严重性驱动控制/隔离/验证强度）
  type: framework
  merged_from: [f4-07, f5-10]
  group: 通用风险决策
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 11.13: Bakery B 因花生严重性从时间分隔升格为空间物理分隔+人员管控
      - Ch15 15.7.4.1: SAHCODH 危害锁定"首用前+每年现场审核"硬底线，其余危害按风险自选强度与频次
      - 附录 11-1.C: 空间分隔设计菜单（专用车间/封闭设备/气流/缓冲间）按等级展开
  V2_predictive_power:
    passed: true
    novel_question: "小厂同时做常规巧克力与花生酱，有限的改造预算先投哪里？"
    derived_answer: "先投花生线的空间隔离（严重性端点决定隔离档位），巧克力线的验证频次优化放后——因为严重性是离散跳档的（SAHCODH/非 SAHCODH），概率只是连续微调"
  V3_exclusivity:
    passed: true
    why_not_common: "'风险越大管得越严'是空话；本框架给出严重性→隔离方式的非连续阶梯（时间分隔→空间分隔→人员锁定）和 SAHCODH 硬底线——强度是跳档的，不是均匀可调的旋钮"
  → 进入阶段 2

- id: fB-07
  title: 按供应商控制方式差异化验证配置
  type: framework
  merged_from: [f4-08, f5-03]
  group: 供应链管理
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 11.13.5: Bakery B 对专线供应商（低验证：年度 COA+三年一审）与共线供应商（高验证：年审+季抽检）差异配置
      - Ch12 12.13: Baker D 对有检测程序的 Miller C 审其数据、对无检测的 Miller E 签约前自测+合同预埋验收条件
  V2_predictive_power:
    passed: true
    novel_question: "两家云厂商，一家有 SOC2 全套控制，一家靠运维手工流程，审计条款怎么谈？"
    derived_answer: "对前者验证其控制的存在性（年度证书+偶尔复核），对后者把验证写成合同里的条件触发权利（每次交付附证据+保留抽测权）——缺什么补什么，而不是一刀切加价"
  V3_exclusivity:
    passed: true
    why_not_common: "通用说法是'按风险分级管理供应商'；本框架的判别器是供应商控制的结构性程度（物理隔离=结构性 vs 清洁验证=操作性）——结构越强买方验证越轻，这是反向的、可操作的换算"
  → 进入阶段 2

- id: fB-09
  title: 化学危害公共判定器+类别杀手问题路由
  type: framework
  merged_from: [f4-10, f4-11]
  group: 化学危害与食品欺诈
  V1_cross_domain:
    passed: true
    evidence:
      - Ch2: 严重性×概率+117.130(c)(2) 十类因素是全类别危害的公共评估底座
      - Ch12 12.3.5–12.3.13: 九类化学危害逐类套用同一四因素+各类专属杀手问题（违规残留史/官方检测体系/掺假模式库等）
  V2_predictive_power:
    passed: true
    novel_question: "瓶装茶里发现微塑料，书里九类都没列，怎么判？"
    derived_answer: "先走公共四因素（信息/工艺来源/无控概率/严重性），再补杀手问题'它从供应链还是从过程设备来'→主要来自包装迁移→归过程+包装材料控制而非原料供应链控制，路由结果与九类中的'过程污染物'同格"
  V3_exclusivity:
    passed: true
    why_not_common: "HACCP 传统聚焦生物危害；'公共判定器+每类一个杀手问题'的路由结构，以及化学危害主要走供应链控制的 FDA 特定分流，是超出通用质量常识的判定工程"
  → 进入阶段 2

- id: fB-10
  title: 易感人群锚定的控制升降级与降级处置
  type: framework
  merged_from: [f4-12, f4-14]
  group: 化学危害与食品欺诈
  V1_cross_domain:
    passed: true
    evidence:
      - Ch12 12.3.5/12.10: 婴幼儿食品毒元素强制升格为供应链预防控制
      - Ch12 12.6.5: 超标产品降级转作成人餐食/动物食品（远离易感人群）
      - Ch11 11.13.3.3: 误触花生蛋白的面团重加工为花生酱饼干（跨谱系降级）
  V2_predictive_power:
    passed: true
    novel_question: "一批铅略超婴幼儿行动水平的根茎菜泥，直接销毁吗？"
    derived_answer: "不必：控制等级是消费人群的函数——转作普通成人食品在安全边界内合法且保值；但若法律限值对全人群统一（非易感人群阈值），降级阶梯就到动物食品为止，'换市场'不是万能出口"
  V3_exclusivity:
    passed: true
    why_not_common: "'孩子吃的要更小心'是常识；反直觉的是对称操作成立：控制可随目标人群降级，超标品的合法出路之一是'换个不那么脆弱的市场'——把人群脆弱性当作可匹配的设计变量"
  → 进入阶段 2

- id: fB-11
  title: 条件性升格+外部信息保鲜双触发
  type: framework
  merged_from: [f4-13, f5-01]
  group: 动态维护与再分析
  V1_cross_domain:
    passed: true
    evidence:
      - Ch12 12.12: DON 案例链——新收获季信息恶化时 CGMP 级清洁升格为预防控制（Miller C→Baker D→Sandwich F 逐级联动）
      - Ch12 12.10.2/12.11.2: 两个示例厂均设"每半年+FDA 来函即查"双触发查新机制，结果喂入再分析
  V2_predictive_power:
    passed: true
    novel_question: "欧盟明年下调某污染物限值，我的出口产品线和合同要提前做什么？"
    derived_answer: "危害分析结论应写成'默认态+触发条件+升格动作'三段式：限值修订是预设触发器→规格复评→供应链合同里预埋'监管变更触发规格重谈与按批索证'条款，而不是等限值生效后再逐家改合同"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'定期复审'；本框架的反直觉点是危害分析结论允许带条件（不是/除非信息恶化→是），且升格要在供应链上预埋联动条款——把'活的文档'落到合同层"
  → 进入阶段 2

- id: fB-14
  title: 供应商不符合双路径处置阶梯
  type: framework
  merged_from: [f4-17, f5-26]
  group: 供应链管理
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 11.13.5.4: Bakery B 疑虑未证实→暂停用货等答复；证实交叉接触→评估成品+召回
      - Ch12 12.10.2/12.11.2: Manufacturer A 以"物料是否已投入生产"为判定维度分流
      - Ch15 15.7.5: 处置阶梯法条化（停用→通知→协助→修订计划→联合召回）
  V2_predictive_power:
    passed: true
    novel_question: "供应商年报显示其体系有缺陷，但三年抽检全合格，停供吗？"
    derived_answer: "不停：证据确定性低且无受影响物料→走 correction 路径（暂停增量+限期答复）；但立即启用第二供应商的批量爬坡作为退出备份——处置力度跟'证据确定性×物料已用与否'走，不跟情绪走"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'发现问题就拉黑'或'视而不见'；本框架把处置写成二维分流（确定性×影响范围）+由轻到重阶梯（止损/沟通/赋能/自省/共同善后），且永远保留双供应商冗余作为退出通道"
  → 进入阶段 2

- id: fB-15
  title: 经济掺假签名触发的升级处置
  type: framework
  merged_from: [f4-18]
  group: 化学危害与食品欺诈
  V1_cross_domain:
    passed: true
    evidence:
      - Ch12 12.10.2: 肉桂铅超标形态指向铅盐掺假→停产/隔离/终止合作/全库存复检
      - Ch12 12.3.11: 掺假模式库（肉桂/姜黄铅盐、三聚氰胺、苏丹红Ⅰ）作为分诊依据；2023 肉桂苹果酱事件为实例
  V2_predictive_power:
    passed: true
    novel_question: "进口辣椒粉检出苏丹红 0.5ppm，远低于急性中毒剂量，放行吗？"
    derived_answer: "不放行、且按欺诈事件而非质量问题处置：超标幅度虽小，但'工业染料'是掺假签名，意味着供应商诚信失效+未知批次污染——立即断供并复检全部库存，不给整改机会；0.5ppm 这个数字本身不重要"
  V3_exclusivity:
    passed: true
    why_not_common: "常识把检测超标当成一个连续刻度上的'高/低'；本框架引入离散分诊维度：异常是否符合已知欺诈模式——签名一旦匹配，处置逻辑整体从'质量纠正'切换为'欺诈应对'"
  → 进入阶段 2

- id: fB-17
  title: CGMP 基线+免控判定双层
  type: framework
  merged_from: [f4-20, f6-09]
  group: 体系架构
  V1_cross_domain:
    passed: true
    evidence:
      - Ch11 附录 11-1.A: 先盘 CGMP 八大类措施，预防控制只做查漏+加强（过敏原）
      - Ch12 12.3.4: 化学危害同样先问 CGMP/前提程序能否覆盖，再决定是否升格
      - 附录 1 A1.8.3: X 标记适用的危害仍可经三条路径判"不需控制"（极强致死/CGMP 有效/消费前制备）
  V2_predictive_power:
    passed: true
    novel_question: "CI 流水线已有 lint+单测+评审，安全扫描还要不要单独立卡？"
    derived_answer: "先做覆盖判定：若基线工具对某类漏洞系统性有效（如评审能拦注入类），该类免设专门控制；残余风险点（如依赖投毒）才升格为带监控/纠正/验证的独立关卡——免控可以，但须书面论证，不许静默跳过"
  V3_exclusivity:
    passed: true
    why_not_common: "常识要么全部叠加控制（过度）要么凭感觉跳过（违规）；本框架给出'已覆盖即免控'的合法路径与三条免控依据，且把论证义务显式化——免控是结论不是省略"
  → 进入阶段 2

- id: fB-20
  title: 【已跨池合并至 fA-46（Correction vs Corrective Action 判定边界）】
  merged_from: [f4-23]
  status: merged-into-fA-46
  → 不重复进入阶段 2

- id: fB-21
  title: 跨层级验证传递（验证验证者）
  type: framework
  merged_from: [f5-02]
  group: 供应链管理
  V1_cross_domain:
    passed: true
    evidence:
      - Ch12 12.14: Sandwich F 审 Baker D"如何评估 miller 程序"，不直接验证 miller
      - Ch15 15.7.4.2: 当控制由上游实体实施时，可通过审查直接供应商对上游的评估来履行义务
  V2_predictive_power:
    passed: true
    novel_question: "外包开发团队又把模块分包给第三方，我该审计谁？"
    derived_answer: "审计外包团队的分包含理机制（它如何评估与监督第三方：准入标准、抽查频次、不合格处置），而非逐层穿透到第三方——每层只看上一环，保证链条的每一节都有一个被验证过的验证者"
  V3_exclusivity:
    passed: true
    why_not_common: "常识要么逐层穿透审计（成本爆炸）要么只看直接供应商（断层）；'验证供应商的验证体系'是第三条路，把多层 assurance 压缩为单层结构化审查——PCHF 把它写成了法定实现路径"
  → 进入阶段 2

- id: fB-26
  title: SAHCODH 三重联动判定
  type: framework
  merged_from: [f5-08]
  group: 分类与联动机制
  V1_cross_domain:
    passed: true
    evidence:
      - Ch14 14.2.1: SAHCODH 锚定召回分级 Class I 与报告性食品（RFR）义务
      - Ch15 15.11.2.1: 同一判定锚定供应链"首用前+每年现场审核"硬要求
  V2_predictive_power:
    passed: true
    novel_question: "检出未申报亚硫酸盐且浓度偏高，一旦定性为 SAHCODH 会连坐什么？"
    derived_answer: "一次定性三处自动生效：召回按 Class I 摆布、24 小时内 RFR 报告义务启动、对该配料供应商的年度现场审核义务立即触发——不需要三次独立评估，一个分类裁决驱动全部下游制度"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是对每项义务分别评估、分别争议；本框架揭示监管体系的'单点判定、多点联动'架构——找到贯穿性严重度定义并复用它，是企业内控同样可以复制的设计模式"
  → 进入阶段 2

- id: fB-29
  title: 控制主体定位（验证追着控制者走）
  type: framework
  merged_from: [f5-13]
  group: 供应链管理
  V1_cross_domain:
    passed: true
    evidence:
      - Ch15 15.7.4.2: 调味料商只做混合，杀菌在上游奶粉厂/香料厂→验证指向真正控制者，三条实现路径
      - Ch15 15.6.4: 控制由供应商定义之外的第三方（独立采收/包装商）实施时，收货设施须自行验证或审查其文件
  V2_predictive_power:
    passed: true
    novel_question: "从代理商买的进口原料，出了安全问题找谁验证？"
    derived_answer: "代理商不是'approved supplier'——必须定位实际制造者并对其验证（或审查代理商对制造者的验证并自己记录评估）；验证对象跟着控制行为走，文件流跟着责任走，中间商层级不豁免任何一环"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'谁卖给我审谁'；本框架要求先做控制主体映射再定验证对象，且只有收货设施能批准供应商、禁止验证对象的自我指派——责任-控制-文件三点一线是可操作的映射规则"
  → 进入阶段 2

- id: fB-31
  title: 【已跨池合并至 fA-53（书面论证作为合规弹性出口）】
  merged_from: [f5-15]
  status: merged-into-fA-53
  → 不重复进入阶段 2

- id: fB-38
  title: 集团化集中管理（责任/执行分离+记录可及）
  type: framework
  merged_from: [f5-23]
  group: 治理与合规设计
  V1_cross_domain:
    passed: true
    evidence:
      - Ch15 15.6.2: 集团母公司可代行供应商批准/验证/记录全套职能并建集团级计划
      - Ch15 15.11.2.2 + Ch1: 集团内供应商豁免年审、PCQI 无须是本厂员工——分离的合法性根基
      - 记录异地存放合法但须 24 小时内可取回现场（电子可及即视为现场）
  V2_predictive_power:
    passed: true
    novel_question: "初创请外部顾问当 PCQI，体系文件放谁那里？"
    derived_answer: "义务主体仍是工厂，执行可外置，但记录可及性必须兜底：顾问可持有文件，前提是检查要求后 24 小时内可取回（含电子远程可及）——分离本身合法，没有可及性兜底的分离是违规"
  V3_exclusivity:
    passed: true
    why_not_common: "常识把'谁负责'与'谁干活'绑死；本框架显式允许二者分离，代价是可及性约束（24h 取回）——这是集团化/外包治理中反直觉但可复制的制度安排"
  → 进入阶段 2

- id: fB-40
  title: 二阶危害链推理（间接危害的正名）
  type: framework
  merged_from: [f5-25]
  group: 危害识别思维
  V1_cross_domain:
    passed: true
    evidence:
      - Ch16 16.3: 腐败菌（非健康危害）生长抬高 pH→肉毒孢子萌发产毒→被正名为需预防控制的生物危害
      - Ch16 16.9: 容器密封渗漏→二次污染，同款二阶链推理
      - Ch4 ROP: "可能先产毒后腐败"——无感官警讯的因果链同构
  V2_predictive_power:
    passed: true
    novel_question: "酸化酱汁里添加'安全'的益生菌发酵剂，需要按危害控制吗？"
    derived_answer: "要：益生菌本身不是危害，但任何持续耗酸/产碱的微生物都会抬 pH、瓦解肉毒屏障——判定不看添加物的直接致病性，看它是否是通向真正危害的必要一环；二阶链适用于一切'无害物改变屏障参数'的场景"
  V3_exclusivity:
    passed: true
    why_not_common: "常识按'X 本身是否致病'判定危害；本框架要求沿因果链看二阶后果——'本身无害的东西可能因后果链成为危害'是反直觉的识别原则，且被指南制度化为法定判定"
  → 进入阶段 2

- id: fB-41
  title: 分层危害分析三层级漏斗
  type: framework
  merged_from: [f6-01]
  group: 危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - Ch2: 危害识别（收窄到 potential）与危害评估（收窄到需预防控制）是两道独立闸门
      - 附录 1 A1.3/A1.8.1: universe→potential→requiring preventive control 的正式三层级表述
  V2_predictive_power:
    passed: true
    novel_question: "线上事故复盘时把 200 个候选原因全列出来整改，对吗？"
    derived_answer: "不对：应走同一漏斗——全集只用于穷尽（防遗漏），第二层按本系统相关性收窄，第三层经严重性×概率评估才进入行动集；漏斗各层用不同操作，把'列举'和'决策'混在一层就会过度整改"
  V3_exclusivity:
    passed: true
    why_not_common: "常识把风险清单当决策清单；本框架的核心是中间层'potential hazard'作为法定过渡态——明确'建议评估的起点'与'需要行动的子集'是两个集合，防止跳步也防止照单全收"
  → 进入阶段 2

- id: fB-43
  title: 组合物分解评估法（部件表×组装方式）
  type: framework
  merged_from: [f6-04, f6-12]
  group: 危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 1 A1.5.4: 多组分食品=Σ（各原料危害）+（加工方式引入危害），含 inclusions 脚注路由
      - 附录 1 A1.11: 4 个食品组干脆不建化学危害表，只留"含巧克力查 2D、含蛋查 2G"路由规则
  V2_predictive_power:
    passed: true
    novel_question: "新品'冻干草莓酸奶块'查不到现成危害表怎么办？"
    derived_answer: "按部件求解：草莓查果蔬表（农药/毒元素，且注意干态→复水状态切换）、酸奶查乳品表、冻干工艺查物理危害与水分活度屏障变化——组合物风险=部件风险向量×组装算子，缺总表不是免评估理由"
  V3_exclusivity:
    passed: true
    why_not_common: "常识要么穷举组合建总表（组合爆炸）要么放弃查表；本框架给出第三条路：部件表×组装方式的二维分解——化学危害按供应链可控行改用成分级路由表，是 FDA 特定的工程取舍"
  → 进入阶段 2

- id: fB-44
  title: 用途条件化危害判定（配料×下游场景）
  type: framework
  merged_from: [f6-05]
  group: 危害识别思维
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 1 Table 1F/1H/1J/1N/1O 脚注: 干谷物/香料/脱水蔬菜/奶粉的芽孢菌危害仅在"复水或用于高水分食品"时适用（5+ 张表反复）
      - 附录 1 A1.5.4: 同一配料在不同用途下危害不同（干配料水合条目）
  V2_predictive_power:
    passed: true
    novel_question: "同一批奶粉，卖给做烘焙的工厂和卖给做冲饮的工厂，评估一样吗？"
    derived_answer: "不一样：烘焙场景终产品经高温且低水分，芽孢菌可判'potential 不适用'；冲饮场景水合后 a_w 支持生长，必须评估——危害不是配料的固有属性，是'配料×下游状态轨迹'的函数，评估要顺产品一生往下看"
  V3_exclusivity:
    passed: true
    why_not_common: "常识把危害当成原料的静态标签（查表打钩）；本框架要求把使用场景作为判定变量——X 标记会随下游状态切换而失效，这是把危害分析从'查物料'升级为'查物料的一生'"
  → 进入阶段 2

- id: fB-45
  title: 极强致死工艺豁免逻辑
  type: framework
  merged_from: [f6-06]
  group: 危害分析方法
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 1 A1.6.1.3: 糖食/饼干等因工艺极端致死，SME 不标任何潜在生物危害
      - 附录 1 多张表脚注: 汤酱等弱案例仍标 X，但工厂可凭极强致死判"不需控制"（与 A1.8.3 路径一衔接）
      - Ch6/Ch14: 极强致死工艺作为例外体系的组成部分反复出现
  V2_predictive_power:
    passed: true
    novel_question: "230°C 油炸 4 分钟的脆片，原料带沙门氏菌要紧吗？"
    derived_answer: "可走豁免：工艺致死性与产品可行性重合（炸不透产品本身做不成），沙门氏菌可判不需控制——但豁免以工艺稳定受控为前提，且理由须书面化；一旦工艺参数漂移，豁免自动失效"
  V3_exclusivity:
    passed: true
    why_not_common: "常识认为原料带病原就该控制；反直觉点是'做对产品'与'控住危害'可以是同一个动作——工艺的物理必要性本身就是控制证据，这是把工程约束转化为合规论据的特定推理"
  → 进入阶段 2

- id: fB-46
  title: 控主亦控次（支配性危害覆盖推理）
  type: framework
  merged_from: [f6-07]
  group: 危害识别思维
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 1 A1.6.1.1/A1.6.1.2.2: 志贺氏菌从全部 16 张表删除——控制沙门氏菌/致病性大肠杆菌的措施一般也控制它
      - Ch6/附录 3: 6D 工艺按最耐热目标菌（非蛋白分解肉毒）设计，顺带覆盖更敏感的病原
  V2_predictive_power:
    passed: true
    novel_question: "测试矩阵里有 5 种病原各设一条工艺，能精简吗？"
    derived_answer: "能：找出最严苛目标（最长 D 值/最难灭活的病原）按它设计，其余敏感病原被同工艺顺带覆盖——精简不靠加权平均，靠 minimax 识别；但前提是验证'覆盖推理'在该工艺下确实成立"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是逐项危害逐项控制；本框架反向操作：在并列风险中识别支配性目标，控制它即精简清单——'控制最难者、删除被覆盖者'是反直觉的清单瘦身术"
  → 进入阶段 2

- id: fB-48
  title: 按危害类别拆分法规适用性（矩阵切分）
  type: framework
  merged_from: [f6-11]
  group: 治理与合规设计
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 1 A1.5.5: LACF 食品的生物危害归 part 113（PCHF 不适用），但化学/物理危害 PCHF 仍适用（查 2H）
      - Ch16: 酸化食品与 PCHF 双法规按程序逐条划分适用，超出部分单独兜底
  V2_predictive_power:
    passed: true
    novel_question: "自热火锅产品同时受食品与危险品（发热包）监管，要不要整体二选一？"
    derived_answer: "按'对象×危害类别'逐格判定：食品部分走食品法规、发热包走危险品法规、但食品部分中的化学危害（发热包泄漏迁移）两类法规交叉处单独评估——适用性没有'全有全无'，矩阵逐格才是合法路径"
  V3_exclusivity:
    passed: true
    why_not_common: "常识把'产品受哪个法规管'当成产品级单选题；本框架揭示适用性是'对象×危害类别'二维矩阵的逐格判定——同一产品可被两套体系按类别分治，这是 FDA 例外体系的结构性洞察"
  → 进入阶段 2

- id: fB-51
  title: D/z 值参数化与 6D 查表边界
  type: framework
  merged_from: [f6-15, f6-16]
  group: 工艺控制与热处理
  V1_cross_domain:
    passed: true
    evidence:
      - Ch6: 5 个热处理完整示例全用 D/z 换算与 6D 目标定关键限值
      - 附录 3 Table 3-D/3-E: 保守默认值+双向边界（可放宽须本地数据、初始负荷高须收紧）
  V2_predictive_power:
    passed: true
    novel_question: "65°C 下要杀李斯特菌多久（表里只给 70°C/2min）？"
    derived_answer: "用 z 值把 lethal rate 换算到 65°C，得出与 70°C/2min 等效的更长时间——两个系数把未测温度的外推变成乘法；但外推只允许在参数有效域内做，跨食品基质要重新验证"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'高温杀菌、越久越好'；本框架把耐热性参数化为两个可换算系数（D=对数递减时间，z=温度敏感度），并给出保守默认值与个体化调整的交易规则——默认安全，个性须付费（本地数据）"
  → 进入阶段 2

- id: fB-52
  title: 权威参考表使用纪律（起点非终点+三问检验+禁插值）
  type: framework
  merged_from: [f6-03, f6-08, f6-17]
  group: 工具与方法论
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 1 A1.5/A1.10: X 表只是 SME 建议评估的起点，判定责任在工厂（含本厂历史危害）
      - 附录 1 A1.8.2: X 适用性三问（产品覆盖/产地条件/状态改变）
      - 附录 3 Table 3-A: 极端值≠设计值+对数过程禁线性插值+基质修正
  V2_predictive_power:
    passed: true
    novel_question: "拿行业基准延迟百分位（p99=200ms）给我的服务定 SLO 行吗？"
    derived_answer: "按三问检验：该基准覆盖我的流量形态吗？数据来自与我相同的部署条件吗？我的链路改变了数据形态吗（如加了缓存）？三问任一为否则只能当先验起点——且对数类指标不许在数据点间线性插值"
  V3_exclusivity:
    passed: true
    why_not_common: "常识把权威表格当答案抄；本框架给出系统性使用纪律：表=先验起点、个体判定不可外包、三问适用性检验、极端值/插值/基质三条修正——'照表抄会过度、不看表会违规'的双错框架是 FDA 特定工程"
  → 进入阶段 2

- id: fB-53
  title: 预测模型须验证原则（模型输出是假设不是结论）
  type: framework
  merged_from: [f6-18]
  group: 工具与方法论
  V1_cross_domain:
    passed: true
    evidence:
      - 附录 3: PMP/ComBase 预测的生长曲线（尤其迟滞期）与实测可能显著偏离，用作关键限值前必须实测验证
      - Ch6/Ch9: 过程验证（validation）体系同样要求用科学/技术证据确认控制有效——模型不得自证
  V2_predictive_power:
    passed: true
    novel_question: "用仿真器跑出来的压测上限能直接写成容量红线吗？"
    derived_answer: "不能直接写：仿真输出是生成假设的工具，对初始条件敏感的量（类似迟滞期——冷启动/缓存预热）偏差最大；红线必须先用真实系统验证，模型的价值是把验证范围从全空间压缩到边界附近"
  V3_exclusivity:
    passed: true
    why_not_common: "常识是'有模型就信模型'或'模型不可靠就不用'；本框架给出中间态定位：模型=假设生成器，凡进入受控参数的输出必须付费验证——且点名最易失真的量（迟滞期）提醒验证重点"
  → 进入阶段 2
```
