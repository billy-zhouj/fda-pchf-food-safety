# FDA PCHF 指南 — 案例提取（case extractor 产出）

> 提取原则：只收指南正文亲自推演/引用的具体实例（示例工厂、暴发史、供应链情境），每条均回 source.md 原文核验并摘录原句。
> 共 41 条。章节号按指南原文编号。

```yaml
# ============ ① 五个热处理示例厂（Ch6，每种组合演示一种验证模式）============

- id: c01
  title: Cookie Processor A — 批式烤箱曲奇的 Salmonella 热处理验证
  type: case
  source_chapter: 第 6 章 6.12（Ch6 示例 1/5，批式×固体）
  source_quote: |
    "Cookie Processor A's PCQI identified Salmonella as the hazard associated with the
    ingredients (e.g., flour, eggs, peanut butter)... The extension specialist provided
    Cookie Processor A's PCQI with a published study by Lathrop et al., (2014)... Cookies
    baked for 13 minutes showed at least a 5.2 log reduction in Salmonella."
  summary: |
    批式曲奇厂走完"文献+现场试验"两步验证全流程：PCQI 先请大学推广专家从已发表研究
    （Lathrop 2014，花生酱曲奇 350°F/15 min 无检出、13 min 达 5.2 log 减少）取得科学依据，
    再对本厂烤箱做热分布+热穿透试验（满载、28 g 挤料），确认最冷点 13 min 后 >230°F。
    据此定三条关键限值（炉温≥350°F、时间≥13 min、面团≤28 g）和更严的三条操作限
    （352°F/15 min/27 g），并按操作限生产。监控覆盖温度记录仪、批次时间、每 2 小时查
    挤料设定、每班 2 次称重。演示模式：借用公开文献+第三方专家+厂内验证试验确定关键限值。
  bound_to:
    - "热处理（致死步骤）设计与验证三步法"
    - "关键限值 vs 操作限"
  tags: [case, example-facility, heat-treatment, salmonella, validation, batch-process]

- id: c02
  title: Cookie Processor B — 连续带式烤箱的时间-转速控制
  type: case
  source_chapter: 第 6 章 6.13（Ch6 示例 2/5，连续×固体）
  source_quote: |
    "The in-house heat penetration studies for the baking process used thermocouples with
    the sensors placed in the geometric center of the cookie dough portions (in 16 cookie
    dough portions... in each of 3 trials conducted over 3 days)... all 28 g cookie dough
    portions achieved a minimum internal temperature of 231°F at the end of a 13.0-minute
    baking time."
  summary: |
    与 Cookie A 同样的 Salmonella 危害，但设备换成连续带式烤箱，演示连续工艺的验证差异：
    烘烤时间不再逐批记录，而是由网带速度（转速计 RPM）控制——专家同时标定 13 min（最差
    情形）与 15 min（操作限）对应的 RPM 读数。热穿透试验用 16 支热电偶分布带宽、跨 3 天
    3 次试验，证明最坏点达 231°F。偏差处置走 QC hold + PCQI 处置（曲奇碎做原料或转动物
    饲料），验证增加 QC 每班两次查图表。演示模式：连续工艺中"时间"参数的代理监控（RPM）。
  bound_to:
    - "连续热处理的关键参数替代监控"
    - "热穿透试验设计"
  tags: [case, example-facility, heat-treatment, continuous-process, thermocouple]

- id: c03
  title: Soup Processor A — EPIPT 终点温度替代全程监控（冷冻汤）
  type: case
  source_chapter: 第 6 章 6.14（Ch6 示例 3/5，批式×液体×冷冻）
  source_quote: |
    "Using Table 3-D in Appendix 3 of this guidance, Soup Processor A's PCQI determined
    that 0.05 minutes (3 seconds) at 180°F achieves an acceptable 6-log... reduction...
    Because of the additional lethality during the heating time... Soup Processor A's PCQI
    decided to use an EPIPT and cook the soups until the temperature reaches 180°F."
  summary: |
    RTE 冷冻蔬菜汤（150 加仑夹层锅批煮）以 L. monocytogenes 为目标菌，直接查指南附录 3
    Table 3-D 得 180°F/3 秒即 6D，利用升温降温途中的额外致死量，采用 EPIPT——只监控
    "终点内部温度达到 180°F"，免除全程温度记录。第二条关键限值是蔬菜颗粒 ≤½ 英寸
    （厂内研究证明颗粒≤½ inch 时颗粒与液体同步达温，前提是来料冷藏 33-40°F 储存，
    因而颗粒温度无需单设关键限值、由 SOP 保证）。监控：测锅内最冷的上层 1 英寸、
    每 10 分钟一次直至达温；每 3 批来料用数字卡尺抽测颗粒。演示模式：查表定限值+
    EPIPT 三前提（热分布/热穿透/其他关键因素）落地。
  bound_to:
    - "EPIPT 替代全程时间-温度监控"
    - "6D 目标查表（Table 3-D）"
  tags: [case, example-facility, EPIPT, listeria, batch-kettle]

- id: c04
  title: Soup Processor B — 连续换热器以肉毒梭菌非蛋白分解 B 型为目标菌
  type: case
  source_chapter: 第 6 章 6.15（Ch6 示例 4/5，连续×液体×冷藏 ROP）
  source_quote: |
    "Because hot-filling into 5-gallon bags would result in reduced oxygen packaging, and
    because the soups will be distributed refrigerated, Soup Processor B's PCQI/food
    processing expert determined that C. botulinum non-proteolytic type B is an appropriate
    target organism for the soup heat treatment."
  summary: |
    连续刮板换热器+5 加仑袋热灌装+冷藏分销的组合触发最严苛的目标菌选择逻辑：减氧包装
    使 C. botulinum 成为必须考虑的病原，冷藏使耐冷的非蛋白分解 B 型（而非蛋白分解型）
    成为目标——据此查 Table 3-E 选 205°F/2.5 min（等效 90°C/10 min）6D 工艺，185°F
    热灌装防再污染。五条关键限值（IT 40-45°F、计量泵 RPM、持留管 2.5 min、出口 205°F、
    暂存罐 185°F）覆盖连续系统每个关键因素，持留管与配方一一对应编号。脚注特别提醒：
    此类工艺设计者需专门经验（虽不强制为 process authority）。纠正措施区分了可/不可
    再加工的汤品清单。演示模式：目标菌=最耐热+包装与分销条件决定的选择推理。
  bound_to:
    - "目标菌选择（包装/分销条件驱动）"
    - "ROP 减氧包装与肉毒屏障"
  tags: [case, example-facility, continuous-heat-exchanger, botulinum, ROP]

- id: c05
  title: Salsa Processor A — 酸化食品"双限值"工艺（安全+货架期）
  type: case
  source_chapter: 第 6 章 6.16（Ch6 示例 5/5，酸化食品×玻璃罐热灌装）
  source_quote: |
    "Salsa Processor A's PCQI/process authority selected a process (158°F (70°C) for 1.5
    minutes) that will deliver a 5D process for Salmonella, E. coli O157:H7, and Listeria
    monocytogenes at a product pH of no higher than 4.1 (Breidt et al., 2010)... a process
    that delivers 200°F (93°C) for 2 minutes is adequate to destroy any other sporeformers
    that could survive the process and potentially spoil the product."
  summary: |
    直接酸化莎莎酱（pH 4.1）演示了 pH 与热处理如何分工：pH 4.1 控制肉毒梭菌及腐败
    芽孢菌萌发（文献：sporeformers 在 pH≤4.2 不生长），热处理 158°F/1.5 min 只需对
    营养细胞病原（Salmonella/E. coli O157:H7/L. mono）达 5D（Breidt 2010）；但为货架期
    另加 200°F/2 min 杀灭可致腐败产酸升高 pH 的非致病芽孢菌——安全限与腐败限并存。
    颗粒 ≤1.0 cm 保证颗粒同步达温（前提冷藏储存）。作为 part 114 酸化食品还需向 FDA
    提交 Form 2541e 定时工艺备案。演示模式：酸化+低热组合、双法规（PCHF+part 114）叠加。
  bound_to:
    - "酸化食品双法规对照（108.25/part 114 ↔ PCHF）"
    - "配方（pH）作为工艺控制"
  tags: [case, example-facility, acidified-food, 5D-process, part-114]

# ============ ② 过敏原示例厂（Ch11）============

- id: c06
  title: Dessert Manufacturer A — 同线四种冷冻甜点的排产+色码+标签控制
  type: case
  source_chapter: 第 11 章 11.12（过敏原示例厂 1）
  source_quote: |
    "Scheduling: Dessert Manufacturer A produces the frozen products in a sequence whereby
    the product with no allergens (i.e., raspberry sorbet) is produced first and the product
    with the most allergens (i.e., vanilla frozen custard with almonds) is produced last...
    Processing: Dessert Manufacturer A adds the almonds at the end of the production process."
  summary: |
    同一条生产线轮产雪葩（无过敏原）→香草冰淇淋（奶）→香草蛋奶冻（奶+蛋）→杏仁蛋奶冻
    （奶+蛋+杏仁），演示过敏原交叉接触控制的全套组合拳：排产按过敏原递增排序（"like into
    like"）、称量区一次只称一种过敏原并即清洁、色码容器与专用工具、杏仁在灌装末端才加入
    以减少接触设备、每批产后即配新清洁液。清洁验证四层：检查单+ATP/蛋白拭子+投料前目视
    +季度过敏原特异性检测（PCQI 周审）。标签控制含 tub/lid 四色色码与 UPC 扫码核对。
    供应链评估结论：奶/蛋供应商不处理其他过敏原、杏仁处理商不碰其他树坚果，故无需评估
    其交叉接触。演示模式：危害分析→CGMP 措施+交叉接触控制+标签控制三层落位。
  bound_to:
    - "过敏原程序三支柱（CGMP→交叉接触+标签→供应链）"
    - "排产与 like-into-like 规则"
  tags: [case, example-facility, allergen, cross-contact, scheduling, color-coding]

- id: c07
  title: Bakery B — 为牛奶过敏消费者生产"无奶"饼干的物理隔离方案
  type: case
  source_chapter: 第 11 章 11.13（过敏原示例厂 2）
  source_quote: |
    "Bakery B produces three types of cookies, for milk allergic-consumers, that have no
    ingredients containing milk... One ingredient (i.e., vegan caramel chips) that does not
    contain a food allergen but has the potential to contain a food allergen (i.e., milk)
    as a result of allergen cross-contact by suppliers."
  summary: |
    产品定位本身就是风险管理：客户是牛奶过敏人群，产品配方不含奶，但 vegan 焦糖豆有
    供应商端交叉接触奶的潜在风险——于是"潜在过敏原"进入危害分析。花生线独立（Line B）、
    称量/staging 区墙门物理分隔、器具色码（花生=蓝）、人员按线固定；标签生产中即时电子
    打印贴附并采用 Contains 声明；大豆起酥油用高精炼豆油（豁免标注）。演示了 correction
    与 corrective action 的判定：花生品误入非花生区，若生产未开始只需 correction（可不
    记录），已开始则须完整 corrective action（评估面团、改做花生酱饼干或转动物饲料）。
  bound_to:
    - "物理隔离 vs 排产清洁的选择"
    - "correction vs corrective action 边界"
  tags: [case, example-facility, allergen, physical-segregation, consumer-safety]

- id: c08
  title: Caramel Chip Processor A vs B — 同一原料两种供应商风险画像
  type: case
  source_chapter: 第 11 章 11.13.5.2（Bakery B 供应商评估）
  source_quote: |
    "Caramel Chip Processor A uses dedicated processing lines... and does not provide an
    allergen advisory statement... Caramel Chip Processor B uses product scheduling,
    scraping, and push-through cleaning of a processing line used to produce caramel chips
    containing milk before using that processing line to produce caramel chips that do not
    contain milk."
  summary: |
    同一原料（vegan 焦糖豆）的两个候选供应商构成一组对照实验：A 用含奶/无奶专用双线
    （低风险→无咨询声明）；B 用共用线靠排产+刮扫+推过式清洁+推过料回用于含奶产品+
    常规 FCS 牛奶检测（中等风险→无咨询声明但依赖清洁验证）。Bakery B 对两者的批准与
    验证活动随之分级：A 每年要专用线 CoC、每三年一次审核；B 每年第三方审核+每季抽样
    检测牛奶。演示模式：验证强度=供应商工艺风险画像的函数，而非一刀切。
  bound_to:
    - "供应链验证活动选择（风险分级）"
    - "咨询声明与供应商清洁验证的关系"
  tags: [case, supplier-approval, allergen, risk-graded-verification]

- id: c09
  title: Table 11-4 — 八个供应商情境矩阵（从分建筑到同线+咨询声明）
  type: case
  source_chapter: 第 11 章（Table 11-4，11.8 供应商批准/验证示例）
  source_quote: |
    "Low, because the supplier uses different processing lines for vegan caramel chips and
    caramel (and other) chips that contain milk. Therefore, the supplier does not use
    allergen advisory statements. ... High. The supplier uses allergen advisory statements
    because it uses the same processing line... and its verification testing during
    development of the food safety plan demonstrates that its cleaning is not always able
    to protect the vegan caramel chips from allergen cross-contact."
  summary: |
    用 8 个系统化情境铺满"供应商交叉接触风险谱系"：vegan 焦糖豆×4（分线/同线+清洁有效/
    同线+逐批检测弃用阳性批/同线+清洁无效改用咨询声明）、杏仁饮料×豆（同线液体+检测
    阴性）、干烤杏仁×花生（分建筑/同建筑分室色码/同室+时空分离）、干烤杏仁×腰果（分室/
    同室+清洁无效→咨询声明）。每行给出匹配的批准活动（问卷+FDA 资源检索+现场审核+
    多批检测）与持续验证频次（CoC 年检/审核 1-3 年/抽检季度）。演示模式：把"批准什么、
    验证什么、多久一次"变成可查表的决策逻辑，同时示范咨询声明="清洁无法保证"的兜底信号。
  bound_to:
    - "供应链验证决策框架（风险×活动×频次）"
    - "咨询声明三选一决定"
  tags: [case, decision-table, supplier-verification, advisory-statement]

- id: c10
  title: 同厂含奶饮料与含豆饮料互染 — 过敏原控制为何必要（11.3 动机示例）
  type: case
  source_chapter: 第 11 章 11.3（含杏仁巧克力糖、乳清蛋白粉粉尘）
  source_quote: |
    "If one beverage that you produce contains milk-derived ingredients, and a different
    beverage that you produce in that same establishment contains soy-derived ingredients...
    Otherwise, the milk beverage could have unintended soy protein, and the soy beverage
    could have unintended milk protein."
  summary: |
    指南用三个递进的日常场景论证过敏原程序的必要性：①同一工厂的含奶饮料与含豆饮料
    互染（双向污染）；②含杏仁与不含杏仁的巧克力糖互染；③乳清蛋白粉这类粉状配料以
    粉尘形式扩散到无奶食品。第三个场景点出"配料形态"维度——粉末的物理扩散性使交叉
    接触控制不能只靠清洁，还要控制空气与人员/设备流动。随后指出过敏原危害与配料占比
    无关：香料混合物里作为微量组分的奶同样算数。
  bound_to:
    - "交叉接触的物理机制（粉尘扩散）"
    - "过敏原危害与配料主次无关"
  tags: [case, motivation-example, cross-contact, powder-dust]

- id: c11
  title: 咨询声明传递两情境 — vegan 脆片用于含奶 vs 不含奶产品
  type: case
  source_chapter: 第 11 章 11.8.4
  source_quote: |
    "If your supplier provides an allergen advisory statement for vegan caramel chips... and
    you will use the vegan caramel chips in a food product that contains an ingredient that
    is (or contains) milk (such as milk powder), your product label would already declare
    the food source 'milk,' and there would be no need for an additional allergen advisory
    statement."
  summary: |
    供应商带"may contain milk"声明的 vegan 焦糖豆，买方是否要把它传递到自己产品标签上？
    指南给出分叉：产品本已含奶配料（标签已声明 milk）→无需传递；产品不含奶→二选一：
    传递声明（并在收料 Label Content Procedures 中把该配料视同主过敏原管理），或由 PCQI
    做科学有效的阈值论证（依据 Remington 2020、FAO/WHO 2021/2022 人群阈值剂量数据）
    证明可能存在的奶量不足以引起多数过敏者反应。演示模式：上游声明不能自动免除下游
    判定责任——三选一（传递/不传递/阈值论证）必须书面化。
  bound_to:
    - "咨询声明三选一决定"
    - "过敏原阈值论证"
  tags: [case, advisory-statement, label-control, threshold-determination]

- id: c12
  title: 供应商因 unintended soy 召回奶粉 — 买方的 corrective action 清单
  type: case
  source_chapter: 第 11 章 11.8.5
  source_quote: |
    "For example, if your supplier recalls a powdered milk product due to unintended soy
    presence, and you had purchased that powdered milk product, you would follow the
    supplier's instructions regarding powdered milk that you have not already used. However,
    the problem that led to the recall... could directly impact the safety of food that you
    manufactured/processed before becoming aware of the recall."
  summary: |
    供应商召回含意外大豆的奶粉时，买方动作分两层：未使用的库存按供应商指令处理即可
    （correction 层）；但召回前已用该奶粉生产的产品可能已受影响——必须走完整 corrective
    action 四步：查明供应商过敏原程序为何失效、纠正并防复发（换供应商或整改）、评估
    全部受影响食品安全性、确保含意外过敏原的食品不进入流通（已出货则召回）。演示模式：
    供应商非合规如何沿链条向上游买方传导处置义务。
  bound_to:
    - "correction vs corrective action 边界"
    - "供应商非合规处置"
  tags: [case, recall, supplier-nonconformance, corrective-action]

# ============ ③ 化学危害示例厂与 DON 案例链（Ch12）============

- id: c13
  title: Manufacturer A — 婴儿果泥/菜泥的铅供应链控制（含肉桂 EMA 论证）
  type: case
  source_chapter: 第 12 章 12.10（毒元素示例厂 1）
  source_quote: |
    "Manufacturer A makes shelf-stable baby food – i.e., puréed apples (i.e., applesauce),
    carrots, sweet potatoes... The toxic element lead is a chemical hazard requiring a
    preventive control in the baby food products due to the potential contamination of
    growing areas with lead and the intended consumer of the products (i.e., babies and
    young children)."
  summary: |
    货架稳定婴儿食品厂演示化学危害的"归途判定"：危害分析逐元素×逐配料判定——铅在胡萝卜/
    甜薯（附录 1 标记）且消费者是婴幼儿→判为需预防控制，走供应链程序（审供应商土壤/水
    检测程序、FDA 警告信/进口警报记录、先测数批、季度来料检测且结果未出前不使用）；砷/镉
    未达需控级→降级为 CGMP 质量控制操作（采购规格+年检）。肉桂因 2017 年文献记载的铅盐
    掺假模式（增重增色）+2023 苹果酱事件→铅判为需控。每半年跟踪 Closer to Zero 行动水平
    更新、季度成品检测铅砷镉作为再分析输入。演示模式：同一化学危害在不同配料/消费者
    组合下落到不同控制层级。
  bound_to:
    - "化学危害归途判定（CGMP vs 预防控制四因素）"
    - "婴幼儿食品毒元素供应链控制"
  tags: [case, example-facility, toxic-elements, lead, baby-food, EMA]

- id: c14
  title: Manufacturer B — 干状婴儿米粉的无机砷/镉双源控制
  type: case
  source_chapter: 第 12 章 12.11（毒元素示例厂 2）
  source_quote: |
    "Manufacturer B makes dry infant rice cereal... Purchase agreements with suppliers of
    rice and suppliers of vitamin and mineral premixes include specifications for three
    toxic elements (i.e., arsenic, cadmium, and lead) in these ingredients."
  summary: |
    与 Manufacturer A 对照的第二个毒元素示例：产品换成干状米粉，工艺为米→浆→加维生素
    矿物质预混→干燥磨片。危害来源随之变成两条供应链：大米控无机砷与镉（水稻富集特性），
    预混料控砷与铅（矿物质来源风险）——同一产品、不同配料、不同元素组合。同样执行半年度
    Closer to Zero 跟踪、首单前审检测、季度来料与季度成品检测（砷镉铅）；对未检测批次
    可通过向供应商索取额外检测信息评估风险。检测超标时走根本原因调查（米粉 vs 预混料）、
    评估供应链计划、决定产品处置。演示模式：毒元素控制随作物/配料矩阵而变。
  bound_to:
    - "婴幼儿食品毒元素供应链控制"
    - "检测作为再分析数据源"
  tags: [case, example-facility, arsenic, cadmium, rice-cereal]

- id: c15
  title: Miller C — 磨粉厂 DON 条件性升格（CGMP→预防控制的动态切换）
  type: case
  source_chapter: 第 12 章 12.12（DON 案例链 1/3）
  source_quote: |
    "The outcome of Miller C's hazard analysis is that the hazard of DON in wheat RACs is
    not a hazard requiring a preventive control unless the available information (such as
    the test results... associated with 'new crop' wheat or USDA's weekly reports) indicate
    the potential for higher levels of DON than expected."
  summary: |
    磨粉厂的全套 DON 防线平时以 CGMP 运行：要求供应链供 U.S. No. 1 等级小麦（损伤粒
    上限最低）、自动取样装置/轨道取样器代表性采样、筒仓风机控温控湿、筛分-风选-碟式分离-
    打麦-去石物理清理+昆虫歼灭机、润麦<24 小时、参加第三方年度能力验证的技术人员定期
    检测。判定结论是"DON 不是需预防控制的危害——除非信息显示可能超标"。当新麦上市、
    USDA 周报或检测显示高风险时，同一套物理清理立即升格为预防控制（工艺控制），色选机
    用到最大、成品加严检测作为验证，超标产品转动物饲料/工业用途/销毁并记录。FDA 的 DON
    advisory level 只管成品不管小麦 RAC，故厂内规格由企业自行反推建立。演示模式：
    危害分析的"条件性升格"——季节性信息恶化触发控制层级切换。
  bound_to:
    - "条件性升格逻辑（危害分析动态维护）"
    - "物理清理与色选作为工艺控制"
  tags: [case, DON, mycotoxin, wheat-milling, conditional-escalation]

- id: c16
  title: Baker D — 面包师用采购协议条款差异化管控两家磨粉厂
  type: case
  source_chapter: 第 12 章 12.13（DON 案例链 2/3）
  source_quote: |
    "The outcome of Baker D's hazard analysis is that the hazard of DON in wheat RACs is
    not a hazard requiring a preventive control. When the potential for higher than expected
    levels of DON is indicated during a growing season, Baker D uses the conditions specified
    in its purchase agreements (e.g., requesting a COA from Miller C for each shipment...)"
  summary: |
    面包师 D 从 Miller C 与 Miller E 两家进面粉，对两家写进采购协议的条款不同：C（小型
    企业，有自己的 DON 程序）→高风险时逐批索取 COA；E（微小企业，无定期检测程序）→
    验收以 DON 检测结果为条件（检测由 E 或 D 任一方进行）。危害分析结论同样是"无需预防
    控制"，但高风险生长季到来时靠协议条款完成验证。演示模式：把上游控制要求写进合同
    （COA/附条件验收）是供应链控制之外的轻量替代，且条款强度随供应商能力而异。
  bound_to:
    - "采购协议作为供应链控制载体"
    - "条件性升格逻辑"
  tags: [case, DON, purchase-agreement, COA]

- id: c17
  title: Sandwich Maker F — 三明治厂对面包 DON 的"信任传导"分析
  type: case
  source_chapter: 第 12 章 12.14（DON 案例链 3/3）
  source_quote: |
    "Sandwich Maker F concludes that the procedures, practices, and processes that it
    includes in its purchase agreements are adequate to provide assurance that DON is
    unlikely to be present at levels that could cause illness or injury. The outcome of
    Sandwich Maker F's hazard analysis is that the hazard of DON in pre-sliced bread is not
    a hazard requiring a preventive control."
  summary: |
    链条第四环：三明治厂 F 收 Baker D 的预切片面包，其危害分析不重复 D 的功课，而是
    审查"D 如何评估磨粉厂 DON 程序、以及高风险期磨粉厂如何调整程序"，据此认定预切片
    面包中 DON 无需预防控制。Miller C→Baker D→Sandwich F 三级 demonstrates 危害分析
    责任沿供应链的分层传导：每一级只需保证向上一级的控制评估充分，而非从头控制。与
    c13-c14 的"供应链程序"形成对照——并非所有原料危害都终局于供应链程序，判定可以
    是"无需控制"，理由与"Yes"同等重要。
  bound_to:
    - "危害分析责任的供应链传导"
    - "'No' 判定的书面论证"
  tags: [case, DON, sandwich-maker, tiered-analysis]

# ============ ④ 供应链情境（Ch15 + Ch11）============

- id: c18
  title: 黑胡椒蒸汽处理链（Figure 1）— 向直接供应商索取上游记录
  type: case
  source_chapter: 第 15 章 15.7.2.3（Figure 1）
  source_quote: |
    "Figure 1 shows an example of using relevant food safety records when the hazard
    requiring a supply-chain-applied control is Salmonella that could contaminate black
    pepper and your supplier (Supplier A) provides you with a spice mix containing black
    pepper that has been steam-treated by Establishment B (earlier in the supply chain)."
  summary: |
    控制沙门氏菌的蒸汽处理发生在链条上游 Establishment B，而非直接供应商 A——收货设施
    的验证对象必须前移：可向 A 索取其对 B 的现场审核记录（审核程序、日期、结论、纠正
    措施）及 A 的定期检测记录；想看某批次蒸汽处理参数时，可直接向 B 或经 A 索取。脚注
    补充另一路径：A 可要求 B 做第三方审核，由 B 直接向你提供审核记录。演示模式：
    "supplier 不能自审自证"原则在上游延伸——谁实施控制，验证就指向谁，但索取通道
    可以经过中间商。
  bound_to:
    - "供应商验证记录的传递链"
    - "relevant food safety records 验证活动"
  tags: [case, supply-chain, spice, steam-treatment, records-review]

- id: c19
  title: 调味混合料 Supplier X / Establishment Y / Z（Figure 2）— 控制者与供应商不重合
  type: case
  source_chapter: 第 15 章 15.7.4.2（Figure 2）
  source_quote: |
    "You identify Salmonella as a hazard in the seasoning mix, and you learn from Supplier X
    (your direct supplier) that it does not apply a control for Salmonella in its blending
    operation. Instead, Establishment Y applies a process control for Salmonella in the milk
    powder and Establishment Z applies a process control for Salmonella in the spice blend."
  summary: |
    比黑胡椒链更复杂的拓扑：X 混合 Y 的奶粉与 Z 的香料制成调味混合料，沙门氏菌工艺控制
    由 Y、Z 分别实施，X 的混合工序本身无致死步骤。收货设施的三条路径：依赖 X 提供的其
    自身对 Y/Z 的验证文档（117.415(a)(3)）、自行对 Y/Z 开展验证、或两者混合——同时仍须
    为 X 本身（作为一个制造设施）确定单独的验证活动。决策时建议评估 X 的供应商批准流程
    与验证活动的稳健性。演示模式：一票原料、多个控制实施者时的验证分配。
  bound_to:
    - "供应链控制实施者识别"
    - "依赖供应商验证文档的合规路径"
  tags: [case, supply-chain, seasoning-blend, multi-tier]

- id: c20
  title: SAHCODH 危害=年度现场审核硬规则 — 危害分析如何决定审核频次
  type: case
  source_chapter: 第 15 章 15.7.4.1
  source_quote: |
    "For example, when the hazard is one for which there is a reasonable probability that
    exposure to the hazard will cause serious adverse health consequences or death, in
    general you must conduct an annual onsite audit before using the raw material or other
    ingredient from the supplier and at least annually thereafter."
  summary: |
    供应商验证三要素的第一要素是危害分析：危害严重性直接决定验证强度档位——SAHCODH
    （暴露后有合理概率导致严重健康后果或死亡）危害触发"首次使用前+此后每年"的现场审核
    硬要求；非 SAHCODH 危害按风险比例选择活动与频次。这一规则与 Table 11-4（c09）的
    过敏原情境、c21 的例外路径共同构成"严谨度随风险升降"的完整谱系。演示模式：
    把抽象的"风险为本"翻译成可执行的审核日历。
  bound_to:
    - "SAHCODH 年审规则"
    - "供应链验证三要素（危害分析/控制实施者/供应商表现）"
  tags: [case, SAHCODH, onsite-audit, risk-based]

- id: c21
  title: 集团子公司烤花生 — 免于年审的书面认定
  type: case
  source_chapter: 第 15 章 15.11.2.2
  source_quote: |
    "consider the situation in which you are part of a larger corporation, are making trail
    mix, and obtain roasted peanuts from a supplier that is a subsidiary of the corporation
    and is operating under the same food safety system as you. You could determine that the
    food safety requirements established by the parent company and applied at the subsidiary
    provide the needed assurance."
  summary: |
    SAHCODH 年审规则的唯一例外路径示范：同一母公司体系内的子公司供应商，可由 PCQI 书面
    认定"母公司食品安全要求+集团对子公司的核查"已提供足够保证，从而免于年度现场审核；
    书面认定须记录供应商程序与集团核查活动。指南同时建议：对非集团体系的长期稳定供应商，
    若以多年合规历史（检测、审核发现汇总）替代年审，现场审核频次仍宜保持每 2-3 年一次、
    间隔年加季度抽检。演示模式：例外须书面化且有支撑证据，不是默认豁免。
  bound_to:
    - "SAHCODH 年审规则的书面替代"
    - "PCQI 书面认定"
  tags: [case, corporate-supplier, written-determination, salmonella]

- id: c22
  title: 蜂蜜烤山核桃 qualified facility 供应商 — 替代验证活动
  type: case
  source_chapter: 第 15 章 15.11.3
  source_quote: |
    "For example, a qualified facility that supplies honey-roasted pecans could include a
    brief written description of its preventive controls to control Salmonella on the pecans
    (e.g., roasting the pecans at a specified temperature for a specified time period);
    alternatively, a qualified facility... could provide a statement that it complies with
    the food safety laws of the state in which it is located."
  summary: |
    微小企业（qualified facility）供应商不适用 PCHF 供应链程序，收货设施的替代验证是
    两份书面保证：①状态证明（首次批准前+每年 12 月 31 日前，可用 Form FDA 3942a 副本）；
    ②每两年一次的合规保证——或简述其控制危害的预防控制（如"在规定温度烤规定时间"），
    或声明符合所在州/地食品安法律。指南刻意留出灵活性：企业与供应商可协商每年通知状态
    的具体日期。演示模式：对豁免企业的验证降档不等于零验证——书面保证+双年声明兜底。
  bound_to:
    - "qualified facility 替代验证"
    - "书面保证机制"
  tags: [case, qualified-facility, small-supplier, written-assurance]

- id: c23
  title: 香料供应商的亚硫酸盐前科 — 供应商食品安全史的跨危害迁移
  type: case
  source_chapter: 第 15 章 15.7.4.3.3
  source_quote: |
    "if you are obtaining a product from a supplier that is controlling a microbial hazard
    (e.g., Salmonella in a spice blend) and food from this supplier has been associated with
    a chemical hazard (e.g., excess sulfites in another spice blend it produces), you should
    consider whether you should implement verification activities related to control of
    sulfites."
  summary: |
    供应商表现评估第三要素（food safety history）的扩展示范：你的采购合同只针对沙门氏菌
    控制，但该供应商的另一产品线曾查出亚硫酸盐超标——虽然危害类型不同，仍应考虑临时增加
    对硫化物的验证活动，持续到确认问题已解决。要义：供应商表现是"跨危害"的整体信号，
    一条产品线的失控模式提示其体系的系统性弱点。演示模式：验证范围可被供应商历史动态
    扩张，而非锁定在合同危害清单内。
  bound_to: 
    - "供应商表现评估（food safety history）"
    - "验证活动的动态扩展"
  tags: [case, supplier-history, sulfites, spice]

- id: c24
  title: 紧急情况临时启用未批准供应商 — 黑胡椒逐批检测
  type: case
  source_chapter: 第 15 章 15.9.2
  source_quote: |
    "if you are receiving a raw material or ingredient such as black pepper and your supplier
    controls Salmonella, you could sample and test each shipment of food from the supplier
    for Salmonella using a statistically-based sampling plan. Alternatively, you could obtain
    and review records of the process that the temporary supplier uses to kill Salmonella in
    the black pepper."
  summary: |
    地震/龙卷风/干旱/洪涝、独家供应商设备故障、供应商爆发污染或突然停业等紧急情形下，
    可临时从未批准供应商采购，但原料须在验收前接受充分验证：黑胡椒（供应商控沙门氏菌）
    可按统计抽样方案逐批检测，或审查其杀菌工艺记录；事前先查 FDA 网站有无警告信/进口
    警报。临时使用期为数周至数月，同时推进正式批准或修复原供应商。另有配套收货控制：
    计算机系统锁定仅接受批准供应商的到货。演示模式：供应链弹性的合规通道——应急不豁免
    验证，只压缩形式。
  bound_to:
    - "临时供应商的应急验证"
    - "批准供应商系统的弹性设计"
  tags: [case, emergency, temporary-supplier, black-pepper]

# ============ ⑤ 暴发/掺假案例（危害真实性论证素材，Ch3/Ch5）============

- id: c25
  title: Table 3-3 — 环境病原暴发史：巧克力、花生酱、白胡椒、甜瓜、软奶酪
  type: case
  source_chapter: 第 3 章 Table 3-3（3.3.5）
  source_quote: |
    "Table 3-3. Examples of Pathogens Identified from Outbreaks Attributed to Contamination
    with Environmental Pathogens | Chocolate | S. Napoli | Possibly contaminated water used
    in double-walled pipes, tanks and other equipment | ... | Peanut butter | S. Tennessee |
    From processing environment | FDA (2007a, 2007b) |"
  summary: |
    十起设施相关病原暴发构成"环境病原是真危害"的实证链：巧克力（S. Napoli 疑因双层管/
    罐的污染水；S. Eastbourne 来自加工环境）、巴氏奶油黄油（L. mono，芬兰）、花生酱
    （S. Tennessee、Salmonella spp.、S. Bredeney 三起）、白胡椒（S. Rissen）、甜瓜
    （L. mono，Jensen Farms 2012）、巴氏乳软奶酪（L. mono，2013/2014 两起）。共同点：
    原料经热处理、病原来自工厂环境——直接支撑"RTE 食品暴露于环境且包装后无致死处理时，
    环境病原评估为强制项"（117.130(c)(1)(ii)）与环境卫生控制的立法逻辑。
  bound_to:
    - "环境病原控制战略的实证基础"
    - "湿/干环境二分法（危害真实性）"
  tags: [case, outbreak, environmental-pathogen, salmonella, listeria]

- id: c26
  title: 三聚氰胺掺入稀释乳制品 — EMA 造成 29 万婴儿患病 6 死亡
  type: case
  source_chapter: 第 3 章 3.4.1.6 / Table 3-8
  source_quote: |
    "some milk firms in one country added melamine, a nitrogen-rich industrial by-product,
    to diluted dairy products to increase the apparent protein content (FDA, 2008). This
    adulteration resulted in significant public health consequences, with more than 290,000
    ill infants and 6 deaths in that country."
  summary: |
    经济动机掺假（EMA）的标志性案例：奶企向掺水乳制品加三聚氰胺虚增表观蛋白含量，
    29 万余婴儿患病、6 例死亡。指南由此给出判定规则：当使用来自有掺假史国家的乳制品时，
    危害分析应纳入三聚氰胺并据判定结果决定是否写入 FSP；使用本国或无掺假史国家的乳品
    则不必。与 Table 3-8 其他 EMA 情境（姜黄+铬酸铅、红椒粉+氧化铅、辣椒粉+Sudan I）
    共同构成"按历史掺假模式扫描原料"的方法示范，并推荐 USP 免费食品欺诈数据库等资源。
  bound_to:
    - "EMA 危害判定（国别+供应商历史扫描）"
    - "化学危害真实性论证"
  tags: [case, outbreak, EMA, melamine, milk]

- id: c27
  title: 二噁英事件 — 2008 爱尔兰猪肉与 1999 比利时禽蛋（饲料源头污染）
  type: case
  source_chapter: 第 3 章 3.4.1.4
  source_quote: |
    "In 2008, pork meat and pork products were recalled in Ireland when up to 200 times the
    safe limit of dioxins were detected in samples of pork... The contamination was traced
    back to contaminated feed. In 1999, high levels of dioxins were found in poultry and
    eggs from Belgium... traced to animal feed contaminated with illegally disposed
    PCB-based waste industrial oil."
  summary: |
    两起环境污染物事件的共同结构：污染源在饲料，沿"饲料→食品动物→脂肪富集→人"传递。
    爱尔兰 2008 年猪肉二噁英超标至安全限 200 倍（风险评佔虽示无公共卫生担忧仍全数召回）；
    比利时 1999 年非法倾倒的 PCB 基工业废油污染饲料波及多国禽蛋。因为二噁英在脂肪中
    累积，动物源食品是人类暴露主途径。指南用它论证：环境污染物需要的控制类型取决于
    进入食物的途径——此处是"原料（动物产品）相关危害"，控制落点在供应商与原料验收。
  bound_to:
    - "环境污染物危害的源头追溯"
    - "ingredient-related vs process-related 化学危害分类"
  tags: [case, outbreak, dioxin, feed-contamination, environmental-contaminant]

- id: c28
  title: 2023 肉桂苹果酱铅铬事件 — Manufacturer A 危害分析的直接触发案例
  type: case
  source_chapter: 第 12 章 12.10（引 CDC 2024 / FDA 2024a）
  source_quote: |
    "Beginning in 2023, CDC reported on elevated blood lead levels in individuals with
    exposure to certain applesauce products that contained cinnamon with very high levels
    of lead and chromium from lead chromate (CDC, 2024). In 2024, FDA announced its leading
    hypothesis that this was likely an act of economically motivated adulteration (FDA,
    2024a)."
  summary: |
    在 c13 的婴儿食品厂危害分析中，肉桂铅被列为需预防控制的理由之一正是这起真实事件：
    2023 年起 CDC 报告食用含高铅铬肉桂的苹果酱袋装产品的儿童血铅升高，2024 年 FDA 认定
    很可能是铅铬酸盐掺入肉桂（增重增色）的经济动机掺假。案例同时暴露体系盲点（阶段 0
    批判已指出）：该事件靠临床血铅异常发现，而非任何设施的再分析捕捉——提示依赖供应链
    检测与文献扫描的局限。作为"危害真实性论证"素材，它把 EMA 从历史模式（2017 Cowell
    文献）连接到当代现实。
  bound_to:
    - "EMA 危害真实性论证"
    - "婴幼儿食品毒元素危害分析输入"
  tags: [case, outbreak, lead, cinnamon, EMA, baby-food]

- id: c29
  title: 香料掺假模式表 — 姜黄铬酸铅、红椒粉氧化铅、辣椒粉 Sudan I
  type: case
  source_chapter: 第 3 章 Table 3-8
  source_quote: |
    "| Turmeric | Lead chromate | A chemical with a vibrant yellow color that has been used
    as an adulterant in turmeric to change the color of the spice to suggest that it is of
    a higher quality | ... | Chili powder | Sudan I | An orange-red powder that had been
    added to chili powder as a coloring agent, but is now banned in many countries..."
  summary: |
    Table 3-8 与三聚氰胺并列的三个香料 EMA 情境：姜黄掺铬酸铅（鲜黄色冒充优质）、红椒粉
    掺氧化铅（红色增色）、辣椒粉掺 Sudan I（IARC 3 类致癌物，多国禁用）。判定建议同时
    考虑配料的原产国与具体供应商——历史掺假模式提示潜在风险，即使过往事件与当前供应商
    无关。危害分析据此决定是否将 EMA 危害写入 FSP 并通过供应链程序控制。演示模式：
    用"掺假模式速查表"驱动原料级危害扫描。
  bound_to:
    - "EMA 危害判定"
    - "香料供应链危害扫描"
  tags: [case, EMA, spice, lead, sudan-i]

- id: c30
  title: Ackee（西非荔枝果）hypoglycin A — 天然毒素与成熟度工艺
  type: case
  source_chapter: 第 3 章 3.4.1.5 / Table 12-2（CPG 550.050）
  source_quote: |
    "An example of a natural toxin produced by a plant is hypoglycin A, a heat stable toxin
    found in the tropical fruit ackee. The level of hypoglycin A in the edible portion of
    the ackee fruit decreases as the fruit ripens. Only properly ripened and processed ackee
    products with hypoglycin A at negligible levels are safe for consumption."
  summary: |
    天然植物毒素案例：hypoglycin A 热稳定、随果实成熟而降低；未熟 ackee 食后可致呕吐到
    严重低血糖、昏迷甚至死亡，虽有人食用无恙但风险不可预测。控制要点是选熟果与正确加工
    （Ch12 配套 CPG 550.050：罐装/冷冻 ackee 成品 hypoglycin A >100 ppm 视为加工不当）。
    因为毒素热稳定，热处理不能消除——唯一控制点是原料成熟度筛选与工艺规范。演示模式：
    "热处理非万能"的天然毒素样本，控制前移到原料选择。
  bound_to:
    - "天然毒素控制（热稳定性决定控制点位）"
    - "CPG 阈值与工艺规范"
  tags: [case, natural-toxin, ackee, hypoglycin-a]

- id: c31
  title: 学校午餐鸡柳氨中毒 — 制冷剂泄漏的工业化学品危害
  type: case
  source_chapter: 第 3 章 3.4（引 Dworkin et al. 2004）
  source_quote: |
    "Ammonia in food contaminated by a refrigerant leak has caused gastrointestinal illness
    (stomachache and nausea) and headaches (Dworkin, et al. 2004)."
  summary: |
    工业化学品危害的即时效应案例：制冷剂氨泄漏污染食品（学校午餐鸡柳）导致胃痛、恶心与
    头痛。与苛性清洁剂灼伤口腔食道同列"立即效应"类化学危害；与铅的儿童认知损害（糖果中
    低剂量慢性暴露）、黄曲霉毒素致肝癌（慢性暴露）形成急/慢性效应对照。这类设施相关
    化学危害的控制落在设施维护（制冷系统）与化学物管理，而非原料或工艺参数——补齐
    "危害来源四分类"（原料/工艺/设施/人员）中的设施维度实例。
  bound_to:
    - "设施相关化学危害（制冷剂）"
    - "急/慢性化学效应分类"
  tags: [case, ammonia, facility-related, chemical-hazard, school-lunch]

- id: c32
  title: 冷冻树莓蛋糕 Cyclospora 暴发 — 寄生虫耐冷冻的例外证据
  type: case
  source_chapter: 第 5 章 Table 5-1（Freezing 行）
  source_quote: |
    "Cyclospora is known to be at least somewhat resistant to freezing because an outbreak
    occurred attributed to raspberries in cake that was previously frozen at about 26°F
    (–3.3°C)."
  summary: |
    Table 5-1 用一行脚注立起一个反直觉案例：普遍认为冷冻能阻止病原生长，但环孢子虫
    （Cyclospora cayetanensis）对冷冻至少有一定耐受——曾致蛋糕中约 -3.3°C 冷冻过的树莓
    引发暴发。该案例在指南中的功能是打断"冷冻=安全"的默认假设，提示寄生虫（诺如、甲肝
    同类）对常规致死/抑菌手段的抗性需单独评估；莓果类（及石榴籽、鲜香草）在附录 1 中
    因此带病毒/寄生虫标记。演示模式：用单点暴发证据修正通用控制常识。
  bound_to:
    - "冷冻控制的边界（寄生虫耐受）"
    - "莓果类病原标记依据"
  tags: [case, outbreak, cyclospora, raspberries, freezing]

- id: c33
  title: 脂溶性兽药残留浓缩于全脂奶酪 + 蜂蜜氟喹诺酮
  type: case
  source_chapter: 第 3 章 3.4.1.2
  source_quote: |
    "if a fat-soluble, heat-stable drug residue is present in raw milk, the drug can get
    concentrated when the milk is converted to full fat cheese... An example of an unapproved
    drug residue that has adulterated food is fluoroquinolone, which is an antibiotic that
    has not been approved for use on honey bees in the United States and has been detected
    in honey products from certain regions outside the United States."
  summary: |
    两个动物药物残留情境：①原料奶中的脂溶性热稳定药物（如伊维菌素类）在加工成全脂奶酪
    时被浓缩——加工过程非但不稀释危害反而放大它；②美国未批准用于蜜蜂的氟喹诺酮在部分
    境外地区蜂蜜产品中检出——国别差异决定危害判定。判定规则：无该药物-食品组合的 tolerance
    或超出 tolerance 即为危害。演示模式：加工放大效应与境外农业投入品差异，二者都是
    "为何原料验收需要药物残留维度"的论证素材。
  bound_to:
    - "兽药残留危害（加工浓缩效应）"
    - "国别差异危害判定"
  tags: [case, drug-residue, cheese, honey, concentration-effect]

# ============ ⑥ 工艺危害陷阱与判定素材（Ch2/3/4）============

- id: c34
  title: 面包的"惊喜" — 瓤 a_w 0.95 却无需冷藏的多重屏障
  type: case
  source_chapter: 第 4 章 4.3.3.1（Table 4-11/4-12 注）
  source_quote: |
    "The big surprise here is probably the bread. Most of us tend to think it is a dry,
    shelf-stable product. Actually, the 'crumb' (interior) has a relatively high water
    activity. It is safe because of the multiple barriers of pH, water activity (the crust
    has a low water activity), and preferential growth by mold rather than pathogens. In
    other words, the bread spoils before it becomes hazardous."
  summary: |
    打破"干制即低水分"直觉的教科书案例：面包瓤 a_w 高达 0.95（与牛奶同级的"湿食品"），
    却不需要冷藏控病原——因为三重屏障叠加：pH、外壳低 a_w、以及霉菌比病原菌优先生长。
    结论凝练为"面包在变得危险之前先变质（spoils before it becomes hazardous）"。与酱油
    （a_w 0.80，看似高水分实为中间水分食品，因盐糖结合水分）配对，演示 a_w 单一数值
    不能判定安全性，必须看多 hurdles 组合。方法迁移：任何"看似该冷藏却常温卖"的产品，
    都应能说出它的屏障清单。
  bound_to:
    - "水分活度控制（多屏障逻辑）"
    - "中间水分食品判定"
  tags: [case, formulation, water-activity, bread, multiple-barriers]

- id: c35
  title: 酱油 — 盐糖结合水使高水分外观产品落入中间水分类别
  type: case
  source_chapter: 第 4 章 4.3.3.1（Table 4-13）
  source_quote: |
    "Some unique products like soy sauce appear to be a high moisture product, but actually
    are in the intermediate-moisture category because salt, sugars or other ingredients bind
    the moisture."
  summary: |
    与 c34 配对的 a_w 案例的另一面：酱油含水量高得像湿食品，但盐、糖等溶质结合了自由水，
    实际 a_w 0.80 落入中间水分区（0.60-0.85），无需冷藏控病原，仅因酵母霉菌腐败有货架期
    限制。对照组：果酱果冻 a_w 支持酵母霉生长，故包装前需轻度热处理防腐；RTE 熟食沙拉
    单靠蛋黄酱/醋酸化不足，常需山梨酸钾+丙酸补充。演示模式：a_w 分类的实质是"可被病原
    利用的水"，而非总含水量——配料表可以改变水的生物学意义。
  bound_to:
    - "水分活度分类判定"
    - "配方作为工艺控制"
  tags: [case, water-activity, soy-sauce, intermediate-moisture]

- id: c36
  title: 奶油泡芙界面与鹰嘴豆泥顶饰 — 多组分界面的微环境陷阱
  type: case
  source_chapter: 第 3 章 3.3.4.2.3
  source_quote: |
    "A simple example is an éclair filled with a cream filling. The pH and a_w at the
    interface of the pastry and the filling will be affected by the difference between the
    higher pH and lower a_w of the pastry... A good example is hummus... If a topping of
    pine nuts, or oil, or diced red peppers is added to the top in the container as
    'decoration' then those additions could then significantly change the microenvironment
    at the interface and may require a control (such as acidification)."
  summary: |
    配方控制的两类界面陷阱：①泡芙皮与奶油馅交界处，皮的较高 pH/较低 a_w 与馅的较低 pH/
    较高水分相互作用，可在界面形成适合微生物生长的微环境——单组分检测合格不代表界面
    合格；②鹰嘴豆泥（鹰嘴豆+酸化剂+油+香料均质后整体平衡 pH 本就不同于原料）顶部加
    松子/油/红椒丁"装饰"后，界面微环境被改变，可能需要额外酸化控制。演示模式：
    均相产品的平衡 pH/a_w 判定不能外推到非均相产品的组分界面。
  bound_to:
    - "多组分界面微环境"
    - "平衡 pH/a_w 与单组分差异"
  tags: [case, formulation, interface, eclair, hummus]

- id: c37
  title: 水浴冷却真空吸入污染水 — 热处理后包装完整性陷阱
  type: case
  source_chapter: 第 3 章 3.3.4.4
  source_quote: |
    "The primary causes of recontamination of foods after a process control step and
    packaging are defective container closures and contaminated cooling water... as the
    product cools, a vacuum is drawn in the container. Contaminated cooling water can enter
    through the container closure, especially if the closure is defective."
  summary: |
    热处理后再污染的两大主因：容器封口缺陷与冷却水污染。机理示范：水浴冷却时产品降温
    在容器内形成真空，污染的冷却水可经封口（尤其缺陷封口）被吸入。这类"工艺合法完成
    却在最后一步失守"的场景，与暴发史（c25 的设施相关病原）共同论证热处理不能是唯一
    防线——封口完整性、冷却水水质（如加氯）构成后续屏障。演示模式：致死步骤之后的
    风险惯性，控制设计须覆盖工艺链条末端。
  bound_to:
    - "热处理后再污染路径"
    - "封口完整性控制"
  tags: [case, post-process-contamination, cooling-water, container-closure]

- id: c38
  title: 老旧切片/滚压设备 niche 与鲜软奶酪厂冷湿环境 — 设备设计如何孵化李斯特菌
  type: case
  source_chapter: 第 2 章 2.4.2.4
  source_quote: |
    "older equipment (e.g., older slicing, rolling and conveying equipment) may be more
    difficult to clean (e.g., because of close fitting components or hollow parts) and, thus,
    provide more opportunities for pathogens to become established in a niche environment...
    A facility that manufactures... an RTE product such as fresh soft cheese may have cold,
    moist conditions that are conducive to the development of a niche where the pathogen
    L. monocytogenes can become established."
  summary: |
    设施条件维度的三个嵌套示例：①老旧切片/滚压/输送设备因密合部件或中空结构难清洁，
    成为病原 niche——此时需强化卫生控制；②金属-金属接触设计会产生金属屑，配金属探测器
    作预防控制；③鲜软奶酪厂的冷湿环境天然利于 L. mono 定殖（resident strain），常规
    SSOP 无效需强化卫生程序。与 transient/resident 菌概念呼应：niche 里的菌是"定殖"
    状态，这正是环境监测法定化的原因。演示模式：设备设计与产品类别共同决定卫生控制强度。
  bound_to:
    - "病原 niche 与 resident 菌概念"
    - "设施/设备相关危害识别"
  tags: [case, equipment-design, niche, listeria, soft-cheese]

- id: c39
  title: "巧克力冰淇淋"包装装错含杏仁产品 — 错贴标签即化学危害
  type: case
  source_chapter: 第 3 章 3.4.2.1.3
  source_quote: |
    "If you apply the wrong label to a food, or use the wrong packaging (e.g., using
    packaging for 'chocolate ice cream' rather than for 'chocolate ice cream with almonds'),
    consumers who have a food allergy could purchase a food that would cause an allergic
    reaction. An undeclared food allergen due to applying the incorrect food label to a
    product, or using the wrong packaging, is a chemical hazard."
  summary: |
    过敏原三大失控路径之一的最小案例：包装用错（用普通巧克力冰淇淋的包装装杏仁巧克力
    冰淇淋）即构成未声明过敏原——按 117.130(b)(1)(ii) 属化学危害。与标签设计错误
    （FALCPA 要求遗漏）、交叉接触（c06/c10）并列为过敏原失控三源。该案例在指南中的
    作用是把"标签控制"从文书工作升格为食品安全控制：包装/标签的收货核验、开机核对
    与换线管理都是实质性的预防控制（对照 c06 Dessert A 的 UPC 扫码监控设计）。
  bound_to:
    - "标签控制的三种失控路径"
    - "未声明过敏原=化学危害"
  tags: [case, mislabeling, allergen, packaging]

- id: c40
  title: 金属碎片 7-25 mm 监管线 — 物理危害的量化边界
  type: case
  source_chapter: 第 3 章 3.5
  source_quote: |
    "FDA's Health Hazard Evaluation Board (FDA, 2005e; Olsen, 1998) has supported regulatory
    action against products with metal fragments of 0.3 inches (7 mm) to 1.0 inches (25 mm)
    in length. Such fragments have been shown to be a hazard to [the consumer]."
  summary: |
    物理危害的定量判定基准：FDA 健康危害评估委员会支持对含 7-25 mm 金属碎片的产品采取
    监管行动——小于此区间或大于此区间的碎片另有判定逻辑（过小无创伤意义、过大易被发现
    或难吞咽）。配合指南其他物理危害素材（机械采收农产品带入异物、金属-金属接触产生
    碎屑→金属探测器作预防控制），给出物理危害"不是所有异物都是危害"的边界意识：
    危害定义以致病/致伤为准，尺寸-后果关系是判定核心。Ch13（物理危害控制专章）未发布，
    本条是现有正文中最明确的物理危害量化锚点。
  bound_to:
    - "物理危害量化判定（7-25mm 规则）"
    - "金属探测器作为预防控制"
  tags: [case, physical-hazard, metal-fragments, regulatory-threshold]

- id: c41
  title: 加州杏仁营销令 — 4-log 沙门氏菌降低的法定工艺验证
  type: case
  source_chapter: 第 4 章 4.3.1.4
  source_quote: |
    "In California, treatment processes for almonds must use technologies that have been
    determined to achieve a minimum 4-log reduction of Salmonella in almonds (see 7 CFR part
    981, Almonds Grown in California). The Almond Board of California (ABC) has processes in
    place to review treatment processes for scientific adequacy."
  summary: |
    行业营销令与 PCHF 叠加的实例：7 CFR part 981 要求加州杏仁的处理工艺达到至少 4-log
    沙门氏菌降低，杏仁委员会（ABC）负责审查处理工艺的科学充分性，其资助的研究证明
    环氧丙烷（PPO）熏蒸是达标方法（ABC 2008 验证指南）。对加工者的意义：热处理/熏蒸
    工艺的验证可能有法定行业渠道可依（对照 c01/c02 需自请推广专家或顾问）。演示模式：
    当行业已有"验证过的工艺库"时，企业 validation 负担可部分卸载到行业组织——
    但仍需厂内热分布/热穿透确认（衔接 Ch6 示例的验证结构）。
  bound_to:
    - "致死工艺验证的行业资源"
    - "4-log 法定降低要求"
  tags: [case, almonds, PPO, 4-log, industry-marketing-order]
```
