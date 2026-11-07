# 21 CFR Part 113 — Thermally Processed Low-Acid Foods Packaged in Hermetically Sealed Containers (4-1-25 Edition)

> **来源**：用户提供的 `CFR-2025-title21-vol2-part113.pdf`（1.20 MB，36 页），GPO/eCFR 印刷版 **21 CFR Ch. I (4–1–25 Edition)**，书页 344–379；PDF 元数据 creationDate `D:20250806205405Z`、modDate `D:20250806170140-04'00'`。经本包专用脚本 `.cangjie/convert_cfr_part.py` 按「页 → 左栏 → 右栏」重排转出——**没有**用 `pdf2md-pro`，后者会把双栏同一 y 坐标的左右栏文字并成一行（见「转换局限」）。自检：10/10 条款命中、页眉与独立页码残留 0、裁掉首部 Part 112 残段 2 段与尾部相邻 part 残段 20 段。
> ⚠ **版本口径**：`4–1–25 Edition` 是 CFR **年度编纂版次**（修订至 2025-04-01），**不是**「2025 年新规则」；条文末尾的 FR citation 才是修订出处（如 §113.100 `[44 FR 16215, Mar. 16, 1979, as amended at 76 FR 11923, Mar. 3, 2011]`）。引用写「21 CFR part 113（4-1-25 Edition）」，不得写成「2025 新规」。

## 效力层级与使用边界（导入说明，非原文）

- 本件是 **联邦法规正文**，具法律约束力，与已收的 21 CFR Part 117 同级。这是本包**首次纳入 Part 117 之外的法规正文**；自此「法规正文层」含〔§ 117.xxx〕〔§ 113.xxx〕〔§ 114.xxx〕三套**独立编号体系**，`regulatory-boundaries` 里「Part 117 是唯一法定义务判定基准」须理解为「判定 **Part 117 义务**的唯一基准」，不再能解释为「全包唯一法条」。
- **与 Part 117 的接口（三处，逐字核对 `books/_inbox/21-CFR-Part-117-2025.md`——该文件自 v4.14 起随仓库分发，160,825 字节 / 3,577 行）**：
  - 〔§ 117.1(c)〕`Food covered by specific current good manufacturing practice regulations also is subject to the requirements of those regulations.` —— 受专项 CGMP 管辖的食品**同时**受 Part 117 约束，是并行而非替代。
  - 〔§ 117.5(d)(1)〕Subparts C/G 对 part 113 覆盖的活动不适用，**但条件是** `if you are required to comply with, and are in compliance with, part 113 of this chapter with respect to such activities` —— 这是**条件性豁免**，企业未遵守 part 113 时豁免不成立；不得写成「LACF 自动豁免 PCHF」。
  - 〔§ 117.5(d)(2)〕`The exemption in paragraph (d)(1) of this section is applicable only with respect to the microbiological hazards that are regulated under part 113 of this chapter.` —— 仅限 part 113 管辖的微生物危害；其余需预防控制的危害仍归 Subparts C/G。
  - 对照：〔§ 117.5(b)〕part 123（水产品）、〔§ 117.5(c)〕part 120（果汁）有同类条件性豁免；**part 114（酸化食品）不在 § 117.5 豁免清单内**，酸化食品全程受 Subparts C/G 约束。
- ⚠ **21 CFR part 108 正文仍未收**：FCE（Food Canning Establishment）注册、SID / scheduled process 备案、Emergency Permit Control、§108.35 的 Better Process Control School 认可均出自 part 108；本包只有 CP 7303.070 的转引。凡涉及注册 / 备案 / 许可证的法条级结论须标「**转引未收**」，不得从本件或 CP 反推。
- **与 CP 7303.070 的分工**：本件给**企业法定义务**（shall / must），CP 7303.070 给**检查员取证口径**（抽样量、pH 4.40/4.65 双分析师、异常罐 >1%、Import Alert 升级），后者不是企业放行标准；pH 4.6 / aw 0.85 是本件与 §114.3 的法定身份边界，CP 里的 4.40/4.65/4.75/0.90/0.93 是实验室触发线，三套数字不可互替。
- 引用规范：本件标〔§ 113.xxx〕，酸化食品标〔§ 114.xxx〕，Part 117 标〔§ 117.xxx〕；CP 7303.070 的检查动作标「CP 7303.070 PART x」。全包自 v4.7 起十二类、v4.8 起「**十四类不可混引**」。

## 条款地图（逐字核对，勿沿用二手摘要）

| 条款 | 要点 |
|---|---|
| §113.3 | 定义：`commercial sterility` (e)(1)(2)、`critical factor` (f)、`hermetically sealed container` (j)、**`low-acid foods` (n) = finished equilibrium pH > 4.6 且 aw > 0.85**，番茄及番茄制品 pH < 4.7 不算低酸；`scheduled process` (r)、`water activity` (w) |
| §113.5 | CGMP 判据：`The criteria in §§ 113.10, 113.40, 113.60, 113.81, 113.83, 113.87, 113.89, and 113.100 shall apply in determining whether ... are operated or administered in a manner adequate to protect the public health.` |
| §113.10 | 人员：杀菌釜 / 无菌系统 / 配方系统操作与封口检验员须由**完成 FDA 认可学校课程**者监督，且 `This person shall supervise only in those areas for which a school approved by the Commissioner identifies the person as having satisfactorily completed training.` |
| §113.40 | 设备与程序（本件最长，约 400 行）：静置/搅动杀菌釜、无菌系统、火焰杀菌等；温度指示装置须 **NIST 或其他国家计量院可溯源**、安装时及**每年至少一次**校准、带标签封识并有准确性记录 |
| §113.60 | 容器：卷边 / 封口完整性、检查频次与记录、冷却水卫生 |
| §113.81 | 产品制备；(e) 以 pH > 4.6 的 normally low-acid food 的 pH 作为 scheduled process 依据时，须按 **§114.90** 方法测；(f) aw 作为关键因子时的控制 |
| §113.83 | Scheduled process：由具备热加工专业知识且有 adequate facilities 的 qualified persons 确立；须覆盖季节/品种/供应商/返工/混合等 variations；critical factors 须写入 scheduled process；可用 thermal death time / heat penetration / inoculated packs；incubation tests 应含 **4 个以上实际商业生产批次**；确立过程记录**永久保存** |
| §113.87 | 杀菌室：每产品/罐型的操作与排气规程须张贴或 readily available；`Scheduled processes must be made readily available to the supervisor and any duly authorized employee of the Food and Drug Administration.`；须有 heat-sensitive indicator 防止未杀菌品绕过 |
| §113.89 | 偏差：低于 scheduled process 或关键因子失控 → 全批返工 / 由 competent processing authority 评价 / 销毁；所有偏差须单独建档 |
| §113.100 | 记录：`Processing and production information shall be entered at the time it is observed`；厂内保存 ≥1 年 + 其他可及地点再 2 年（合计 3 年）；(h) 电子记录须符合 part 11 |

## 转换局限

- **双栏重排**：栏边界左 x≈132–303、右 x≈310–483，页眉 y≈159、页码 y≈718 已被 clip 排除；`pdf2md-pro` 直接转会把左右栏同一行并成一串（例如 §114.3(b) 的 `''pickled erages, jams, jellies ...''`），本件已修复。
- **印刷版断词连字符按原样保留**（如 `cab- bage`、`proc- esses`、`stan- dardized`），共 933 处；不做 dehyphenate，以免把 `low-acid foods` 这类真实复合词误并。逐字引文核对采用 NFKC + 去除所有非字母数字的归一化，天然消除换行、空格与断词连字符；**检索以 § 编号为准**，不要以 Markdown 行边界做引证。
- **连续页截取**：PDF 首页含 Part 112（农产品 qualified exemption）尾段、末页含相邻 part 开头，已按 `PART 113` / `PART ...` 边界裁掉并在转换报告记录；目录 `Sec.` 行保留但不作为引证依据。
- 跨 part 引用（如 §113.81(e) 的 `§ 114.90 of this chapter should be used.`）已作为续行拼回正文，不会被误提升为条款标题。

---

## PART 113—THERMALLY PROCESSED LOW-ACID FOODS PACKAGED IN HERMETICALLY SEALED CON- TAINERS

### Subpart A—General Provisions

Sec. 113.3 Definitions. 113.5 Current good manufacturing practice. 113.10 Personnel.

### Subpart B [Reserved]

### Subpart C—Equipment 113.40 Equipment and procedures.

### Subpart D—Control of Components, Food Product Containers, Closures, and In- Process Material 113.60 Containers.

### Subpart E—Production and Process Controls 113.81 Product preparation. 113.83 Establishing scheduled processes. 113.87 Operations in the thermal processing room. 113.89 Deviations in processing, venting, or control of critical factors.

### Subpart F—Records and Reports 113.100 Processing and production records.

AUTHORITY: 21 U.S.C. 342, 371, 374; 42 U.S.C. 264.

SOURCE: 44 FR 16215, Mar. 16, 1979, unless otherwise noted.

### Subpart A—General Provisions

## § 113.3 Definitions.
For the purposes of this part, the fol- lowing definitions apply:

(a) Aseptic processing and packaging means the filling of a commercially sterilized cooled product into presterilized containers, followed by aseptic hermetical sealing, with a presterilized closure, in an atmosphere free of microorganisms.

(b) Bleeders means openings used to remove air that enters with steam from retorts and steam chambers and to promote circulation of steam in such retorts and steam chambers. Bleeders may serve as a means of re- moving condensate.

(c) Come-up-time means the time which elapses between the introduction of steam into the closed retort and the time when the retort reaches the re- quired processing temperature.

(d) Commercial processor includes any person engaged in commercial, custom, or institutional (church, school, penal, or other organization) processing of food, including pet food. Persons en- gaged in the production of foods that are to be used in market or consumer tests are also included.

(e) Commercial sterility: (1) ‘‘Commer- cial sterility’’ of thermally processed food means the condition achieved—

(i) By the application of heat which renders the food free of—

(a) Microorganisms capable of repro- ducing in the food under normal non- refrigerated conditions of storage and distribution; and

(b) Viable microorganisms (including spores) of public health significance; or

(ii) By the control of water activity and the application of heat, which ren- ders the food free of microorganisms capable of reproducing in the food under normal nonrefrigerated condi- tions of storage and distribution.

(2) ‘‘Commercial sterility’’ of equip- ment and containers used for aseptic processing and packaging of food means the condition achieved by appli- cation of heat, chemical sterilant(s), or other appropriate treatment that ren- ders the equipment and containers free of viable microorganisms having public health significance, as well as micro- organisms of nonhealth significance, capable of reproducing in the food under normal nonrefrigerated condi- tions of storage and distribution.

(f) Critical factor means any property, characteristic, condition, aspect, or other parameter, variation of which may affect the scheduled process and the attainment of commercial ste- rility.

(g) Flame sterilizer means an appa- ratus in which hermetically sealed con- tainers are agitated at atmospheric pressure, by either continuous, dis- continuous, or reciprocating move- ment, with impinging gas flames to achieve sterilization temperatures. A holding period in a heated section may follow the initial heating period.

(h) Headspace, gross is the vertical distance between the level of the prod- uct (generally the liquid surface) in an upright rigid container and the top edge of the container (the top of the double seam of a can or the top edge of a glass jar).

(i) Headspace, net of a container is the vertical distance between the level of the product (generally the liquid sur- face) in the upright rigid container and the inside surface of the lid.

(j) Hermetically sealed container means a container that is designed and in- tended to be secure against the entry of microorganisms and thereby to maintain the commercial sterility of its contents after processing.

(k) Incubation means the holding of a sample(s) at a specified temperature for a specified period of time for the purpose of permitting or stimulating the growth of microorganisms.

(l) Initial temperature means the aver- age temperature of the contents of the coldest container to be processed at the time the thermal processing cycle be- gins, as determined after thorough stir- ring or shaking of the filled and sealed container.

(m) Lot means that amount of a prod- uct produced during a period of time indicated by a specific code.

(n) Low-acid foods means any foods, other than alcoholic beverages, with a finished equilibrium pH greater than 4.6 and a water activity (aw) greater than 0.85. Tomatoes and tomato prod- ucts having a finished equilibrium pH less than 4.7 are not classed as low-acid foods.

(o) Minimum thermal process means the application of heat to food, either before or after sealing in a hermeti- cally sealed container, for a period of time and at a temperature scientif- ically determined to be adequate to en- sure destruction of microorganisms of public health significance.

(p) Operating process means the proc- ess selected by the processor that equals or exceeds the minimum re- quirements set forth in the scheduled process.

(q) Retort means any closed vessel or other equipment used for the thermal processing of foods.

(r) Scheduled process means the proc- ess selected by the processor as ade- quate under the conditions of manufac- ture for a given product to achieve commercial sterility. This process may be in excess of that necessary to ensure destruction of microorganisms of pub- lic health significance, and shall be at least equivalent to the process estab- lished by a competent processing au- thority to achieve commercial ste- rility.

(s) Shall is used to state mandatory requirements.

(t) Should is used to state rec- ommended or advisory procedures or to identify recommended equipment.

(u) Vacuum-packed products means those products that are sealed in a con- tainer under the vacuum specified in the scheduled process, the maintenance of which vacuum is critical to the ade- quacy of the scheduled process.

(v) Vents means openings through the retort shell, controlled by gate, plug cock, or other adequate valves used for the elimination of air during the vent- ing period.

(w) Water activity (aw) is a measure of the free moisture in a product and is the quotient of the water vapor pres- sure of the substance divided by the vapor pressure of pure water at the same temperature.

## § 113.5 Current good manufacturing practice.
The criteria in §§ 113.10, 113.40, 113.60, 113.81, 113.83, 113.87, 113.89, and 113.100 shall apply in determining whether the facilities, methods, practices, and con- trols used by the commercial processor in the manufacture, processing, or packing of low-acid foods in hermeti- cally sealed containers are operated or administered in a manner adequate to protect the public health.

## § 113.10 Personnel.
The operators of processing systems, retorts, aseptic processing and pack- aging systems and product formulating systems (including systems wherein water activity is used in conjunction with thermal processing) and container closure inspectors shall be under the operating supervision of a person who has attended a school approved by the Commissioner for giving instruction appropriate to the preservation tech- nology involved and who has been iden- tified by that school as having satisfac- torily completed the prescribed course of instruction. This person shall super- vise only in those areas for which a school approved by the Commissioner identifies the person as having satisfac- torily completed training.

### Subpart B [Reserved]

### Subpart C—Equipment

## § 113.40 Equipment and procedures.

(a) Equipment and procedures for pres- sure processing in steam in still retorts—

(1) Temperature-indicating device. Each retort shall be equipped with at least one temperature-indicating device that accurately indicates the temperature during processing. Each temperature- indicating device shall have a sensor and a display. Each temperature-indi- cating device and each reference device that is maintained by the processor shall be tested for accuracy against a reference device for which the accuracy is traceable to a National Institute of Standards and Technology (NIST), or other national metrology institute, standard reference device by appro- priate standard procedures, upon in- stallation and at least once a year thereafter, or more frequently if nec- essary, to ensure accuracy during proc- essing. Each temperature-indicating device and each reference device that is maintained by the processor shall have a tag, seal, or other means of identity.

(i) The design of the temperature-in- dicating device shall ensure that the accuracy of the device is not affected by electromagnetic interference and environmental conditions.

(ii) Records of the accuracy of the temperature-indicating device and of a reference device that is maintained by the processor shall be established and maintained in accordance with

§ 113.100(c) and (d).

(iii) A temperature-indicating device that is defective or cannot be adjusted to the accurate calibrated reference de- vice shall be repaired before further use or replaced.

(iv) A temperature-indicating device shall be accurate to 1 °F (0.5 °C). The temperature range of a mercury-in- glass thermometer shall not exceed 17 °F per inch (4 °C per centimeter) of graduated scale. A mercury-in-glass thermometer that has a divided mer- cury column shall be considered defec- tive.

(v) Each temperature-indicating de- vice shall be installed where it can be accurately and easily read. The tem- perature-indicating device sensor shall be installed either within the retort shell or in external wells attached to the retort. External wells or pipes shall be connected to the retort through at least a 3⁄4-inch (2 centimeters) diameter opening and equipped with a 1⁄16-inch (1.5 millimeters) or larger bleeder open- ing so located as to provide a full flow of steam past the length of the tem- perature-indicating device sensor. The bleeders for external wells shall emit steam continuously during the entire processing period. The temperature-in- dicating device—not the temperature recording device—shall be the ref- erence instrument for indicating the processing temperature.

(2) Temperature-recording device. Each retort shall have an accurate tempera- ture-recording device. Each tempera- ture-recording device shall have a sen- sor and a mechanism for recording temperatures to a permanent record, such as a temperature-recording chart. The temperature-recording device sen- sor shall be installed either within the retort shell or in a well attached to the shell. Each temperature-recording de- vice sensor well shall have a 1⁄16-inch (1.5 millimeters) or larger bleeder that emits steam continuously during the processing period.

(i) Analog or graphical recordings. Temperature-recording devices that create analog or graphical recordings may be used. Temperature-recording devices that record to charts shall be used only with the appropriate chart. Each chart shall have a working scale of not more than 55 °F per inch (12 °C per centimeter) within a range of 20 °F (10 °C) of the process temperature. Chart graduations shall not exceed 2 °F (1 °C) within a range of 10 °F (5 °C) of the process temperature. Temperature- recording devices that create multipoint plottings of temperature readings shall record the temperature at intervals that will assure that the parameters of the process time and process temperature have been met.

(ii) Digital recordings. Temperature- recording devices, such as data loggers, that record numbers or create other digital records may be used. Such a de- vice shall record the temperature at in- tervals that will assure that the pa- rameters of the process time and proc- ess temperature have been met.

(iii) Adjustments. The temperature-re- cording device shall be adjusted with sufficient frequency to ensure agree- ment as nearly as possible with, but to be in no event higher than, the tem- perature-indicating device during proc- essing. A means of preventing unau- thorized changes in adjustment shall be provided. A lock or a notice from management posted at or near the tem- perature-recording device that provides a warning that only authorized persons are permitted to make adjustments is a satisfactory means of preventing unau- thorized changes.

(iv) Temperature controller. The tem- perature-recording device may be com- bined with the steam controller and may be a recorder-controller.

(3) Pressure gages. Each retort should be equipped with a pressure gage that is accurate to 2 pounds per square inch (13.8 kilopascals) or less.

(4) Steam controller. Each retort shall be equipped with an automatic steam controller to maintain the retort tem- perature. This may be a recorder-con- troller when combined with a tempera- ture-recording device. The steam con- troller may be air-operated and actu- ated by a temperature sensor posi- tioned near the temperature-indicating device in the retort. Air-operated tem- perature controllers should have ade- quate filter systems to ensure a supply of clean, dry air. A steam controller ac- tivated by the steam pressure of the re- tort is acceptable if it is carefully maintained mechanically so that it op- erates satisfactorily.

(5) Steam inlet. The steam inlet to each still retort shall be large enough to provide sufficient steam for proper operation of the retort. Steam may enter either the top portion or the bot- tom portion of the retort but, in any case, shall enter the portion of the re- tort opposite the vent; for example, steam inlet in bottom portion and vent in top portion.

(6) Crate supports. A bottom crate support shall be used in vertical still retorts. Baffle plates shall not be used in the bottom of still retorts.

(7) Steam spreaders. Steam spreaders are continuations of the steam inlet line inside the retort. Horizontal still retorts shall be equipped with steam spreaders that extend the length of the retort. For steam spreaders along the bottom of the retort, the perforations should be along the top 90° of the pipe, that is, within 45° on either side of the top center. Horizontal still retorts over 30 feet (9.1 meters) long should have two steam inlets connected to the spreader. In vertical still retorts, the steam spreaders, if used, should be per- forated along the center line of the pipe facing the interior of the retort or along the sides of the pipe. The number of perforations should be such that the total cross-sectional area of the per- forations is equal to 1.5 to 2 times the cross-sectional area of the smallest re- striction in the steam inlet line.

(8) Bleeders. Bleeders, except those for temperature-indicating device wells, shall be 1/8-inch (3 millimeters) or larg- er and shall be wide open during the entire process, including the come-up time. For horizontal still retorts, bleeders shall be located within ap- proximately 1 foot (30.5 centimeters) of the outermost locations of containers at each end along the top of the retort. Additional bleeders shall be located not more than 8 feet (2.4 meters) apart along the top. Bleeders may be in- stalled at positions other than those specified in this paragraph, as long as there is evidence in the form of heat distribution data that they accomplish adequate removal of air and circula- tion of steam within the retort. Vertical retorts shall have at least one bleeder opening located in that portion of the retort opposite the steam inlet. In retorts having top steam inlet and bottom venting, a bleeder shall be in- stalled in the bottom of the retort to remove condensate. All bleeders shall be arranged so that the operator can observe that they are functioning prop- erly.

(9) Stacking equipment and position of containers. Crates, trays, gondolas, etc., for holding containers shall be made of strap iron, adequately perforated sheet metal, or other suitable material. When perforated sheet metal is used for the bottoms, the perforations should be approximately the equivalent of 1-inch (2.5 centimeters) holes on 2-inch (5.1 centimeters) centers. If dividers are used between the layers of containers, they should be perforated as stated in this paragraph. The positioning of con- tainers in the retort, when specified in the scheduled process, shall be in ac- cordance with that process.

(10) Air valves. Retorts using air for pressure cooling shall be equipped with a suitable valve to prevent air leakage into the retort during processing.

(11) Water valves. Retorts using water for cooling shall be equipped with a suitable valve to prevent leakage of water into the retort during proc- essing.

(12) Vents. Vents shall be installed in such a way that air is removed from the retort before timing of the process is started. Vents shall be controlled by gate, plug cock, or other adequate type valves which shall be fully open to per- mit rapid discharge of air from the re- tort during the venting period. Vents shall not be connected directly to a closed drain system. If the overflow is used as a vent, there shall be an atmos- pheric break in the line before it con- nects to a closed drain. The vent shall be located in that portion of the retort opposite the steam inlet; for example, steam inlet in bottom portion and vent in top portion. Where a retort manifold connects several vent pipes from a sin- gle still retort, it shall be controlled by a gate, plug cock, or other adequate type of valve. The retort manifold shall be of a size that the cross-sectional area of the pipe is larger than the total cross-sectional area of all connecting vents. The discharge shall not be di- rectly connected to a closed drain without an atmospheric break in the line. A manifold header connecting vents or manifolds from several still retorts shall lead to the atmosphere. The manifold header shall not be con- trolled by a valve and shall be of a size that the cross-sectional area is at least equal to the total cross-sectional area of all connecting retort manifold pipes from all retorts venting simulta- neously. Timing of the process shall not begin until the retort has been properly vented and the processing temperature has been reached. Some typical installations and operating pro- cedures reflecting the requirements of this section for venting still retorts without divider plates are given in paragraphs (a)(12)(i)(A) through (a)(12)(i)(D) and (a)(12)(ii)(A) and (a)(12)(ii)(B) of this section.

(i) Venting horizontal retorts. (A) Vent- ing through multiple 1-inch (2.5 centi- meters) vents discharging directly to atmosphere.

(1) Specifications. One 1-inch (2.5 cen- timeters) vent for every 5 feet (1.5 me- ters) of retort length equipped with a gate or plug cock valve and discharging to atmosphere; end vents not more than 2.5 feet (76 centimeters) from ends of retort.

(1) Specifications. One 1-inch (2.5 cen- timeters) vent for every 5 feet (1.5 me- ters) of retort length; and vents not over 2.5 feet (76 centimeters) from ends of retort. Size of manifold—for retorts less than 15 feet (4.6 meters) in length, (2) Venting method. Vent valves should be wide open for at least 5 min- utes and to at least 225 °F (107 °C), or at least 7 minutes and to at least 220 °F (104.5 °C).

(B) Venting through multiple 1-inch (2.5 centimeters) vents discharging through a manifold to atmosphere. 2.5 inches (6.4 centimeters); for retorts 15 feet (4.6 meters) and over in length, 3 inches (7.6 centimeters).

(2) Venting method. Manifold vent gate or plug cock valve should be wide open for at least 6 minutes and to at least 225 °F (107 °C), or for at least 8 minutes and to at least 220 °F (104.5 °C).

(1) Size of vent and vent valve. For re- torts less than 15 feet (4.6 meters) in length, 2 inches (5.1 centimeters); for retorts 15 feet (4.6 meters) and over in length, 2.5 inches (6.4 centimeters).

(2) Size of water spreader. For retorts less than 15 feet (4.6 meters) in length, 1.5 inches (3.8 centimeters); for retorts 15 feet (4.6 meters) and over in length, 2 inches (5.1 centimeters). The number of holes should be such that their total cross-sectional area is approximately

(C) Venting through water spreaders. equal to the cross-sectional area of the vent pipe inlet.

(3) Venting method. Water spreader vent gate or plug cock valve should be wide open for at least 5 minutes and to at least 225 °F (107 °C), or for at least 7 minutes and to at least 220 °F (104.5 °C).

(D) Venting through a single 2.5-inch (6.4 centimeters) top vent (for retorts not exceeding 15 feet (4.6 meters) in length).

(1) Specifications. A 2.5-inch (6.4 centi- meters) vent equipped with a 2.5-inch (6.4 centimeters) gate or plug cock valve and located within 2 feet (61 cen- timeters) of the center of the retort.

(2) Venting method. Vent gate or plug cock valve should be wide open for at least 4 minutes and to at least 220 °F (104.5 °C).

(ii) Venting vertical retorts. (A) Vent- ing through a 1.5-inch (3.8 centimeters) overflow.

(1) Specifications. A 1.5-inch (3.8 centi- meters) overflow pipe equipped with a 1.5-inch (3.8 centimeters) gate or plug cock valve and with not more than 6 feet (1.8 meters) of 1.5-inch (3.8 centi- meters) pipe beyond the valve before break to the atmosphere or to a mani- fold header.

(2) Venting method. Vent gate or plug cock valve should be wide open for at least 4 minutes and to at least 218 °F (103.5 °C), or for at least 5 minutes and to at least 215 °F (102 °C).

(B) Venting through a single 1-inch (2.5 centimeters) side or top vent.

(1) Specifications. A 1-inch (2.5 centi- meters) vent in lid or top side, equipped with a 1-inch (2.5 centimeters) gate or plug cock valve and discharging directly into the atmosphere or to a manifold header.

(2) Venting method. Vent gate or plug cock valve should be wide open for at least 5 minutes and to at least 230 °F (110 °C), or for at least 7 minutes and to at least 220 °F (104.5 °C).

(iii) Other procedures. Other installa- tions and operating procedures that de- viate from the requirements in para- graph (a)(12) of this section may be used if there is evidence in the form of heat distribution data, which shall be kept on file, that they accomplish ade- quate venting of air.

(13) Critical factors. Critical factors specified in the scheduled process shall be measured and recorded on the proc- essing record at intervals of sufficient frequency to ensure that the factors are within the limits specified in the scheduled process.

(i) When maximum fill-in or drained weight is specified in the scheduled process, it shall be measured and re- corded at intervals of sufficient fre- quency to ensure that the weight of the product does not exceed the maximum for the given container size specified in the scheduled process.

(ii) Closing machine vacuum in vacu- um-packed products shall be observed and recorded at intervals of sufficient frequency to ensure that the vacuum is as specified in the scheduled process.

(iii) Such measurements and record- ings should be made at intervals not to exceed 15 minutes.

(iv) When the product style results in stratification or layering of the pri- mary product in the containers, the po- sitioning of containers in the retort shall be according to the scheduled process.

(b) Equipment and procedures for pres- sure processing in water in still retorts—

(1) Temperature-indicating device. Each retort shall be equipped with at least one temperature-indicating device that accurately indicates the temperature during processing. Each temperature- indicating device shall have a sensor and a display. Each temperature-indi- cating device and each reference device that is maintained by the processor shall be tested for accuracy against a reference device for which the accuracy is traceable to a National Institute of Standards and Technology (NIST), or other national metrology institute, standard reference device by appro- priate standard procedures, upon in- stallation and at least once a year thereafter, or more frequently if nec- essary, to ensure accuracy during proc- essing. Each temperature-indicating device and each reference device that is maintained by the processor shall have a tag, seal, or other means of identity.

(i) The design of the temperature-in- dicating device shall ensure that the accuracy of the device is not affected by electromagnetic interference and environmental conditions.

(ii) Records of the accuracy of the temperature-indicating device and of a reference device that is maintained by the processor shall be established and maintained in accordance with

§ 113.100(c) and (d).

(iii) A temperature-indicating device that is defective or cannot be adjusted to the accurate calibrated reference de- vice shall be repaired before further use or replaced.

(iv) A temperature-indicating device shall be accurate to 1 °F (0.5 °C). The temperature range of a mercury-in- glass thermometer shall not exceed 17 °F per inch (4 °C per centimeter) of graduated scale. A mercury-in-glass thermometer that has a divided mer- cury column shall be considered defec- tive.

(v) Each temperature-indicating de- vice shall be installed where it can be accurately and easily read. In both hor- izontal and vertical retorts, the tem- perature-indicating device sensor shall be inserted directly into the retort shell or in a separate well or sleeve at- tached to the retort. The temperature- indicating device sensor shall be lo- cated so that it is beneath the surface of the water throughout the process and where there is adequate circulation to ensure accurate temperature meas- urement. On horizontal retorts, the temperature-indicating device sensor should be located in the side at the center of the retort. The temperature- indicating device—not the tempera- ture-recording device—shall be the ref- erence instrument for indicating the processing temperature.

(2) Temperature-recording device. Each retort shall have an accurate tempera- ture-recording device. Each tempera- ture-recording device shall have a sen- sor and a mechanism for recording temperatures to a permanent record, such as a temperature-recording chart.

(i) Analog or graphical recordings. Temperature-recording devices that create analog or graphical recordings may be used. Temperature-recording devices that record to charts shall be used only with the appropriate chart. Each chart shall have a working scale of not more than 55 °F per inch (12 °C per centimeter) within a range of 20 °F (10 °C) of the process temperature. Chart graduations shall not exceed 2 °F (1 °C) within a range of 10 °F (5 °C) of the process temperature. Temperature- recording devices that create multipoint plottings of temperature readings shall record the temperature at intervals that will assure that the parameters of the process time and process temperature have been met.

(ii) Digital recordings. Temperature- recording devices, such as data loggers, that record numbers or create other digital records may be used. Such a de- vice shall record the temperature at in- tervals that will assure that the pa- rameters of the process time and proc- ess temperature have been met.

(iii) Adjustments. The temperature-re- cording device shall be adjusted with sufficient frequency to ensure agree- ment as nearly as possible with, but to be in no event higher than, the tem- perature-indicating device during proc- essing. A means of preventing unau- thorized changes in adjustment shall be provided. A lock or a notice from management posted at or near the tem- perature-recording device that provides a warning that only authorized persons are permitted to make adjustments is a satisfactory means of preventing unau- thorized changes.

(iv) Temperature controller. The tem- perature-recording device may be com- bined with the steam controller and may be a combination recorder-con- troller. For a vertical retort equipped with a combination recorder-con- troller, the temperature recorder-con- troller sensor shall be located at the bottom of the retort below the lowest crate rest in such a position that the steam does not strike it directly. For a horizontal retort equipped with a com- bination recorder-controller, the tem- perature recorder-controller sensor shall be located between the water sur- face and the horizontal plane passing through the center of the retort so that there is no opportunity for direct steam impingement on the sensor. For all still retort systems that pressure process in water and are equipped with combination recorder-controllers, the temperature recorder-controller sen- sors shall be located where the re- corded temperature is an accurate measurement of the scheduled process temperature and is not affected by the heating media.

(3) Pressure gages. (i) Each retort should be equipped with a pressure gage that is accurate to 2 pounds per square inch (13.8 kilopascals) or less.

(ii) Each retort should have an ad- justable pressure relief or control valve of a capacity sufficient to prevent an undesired increase in retort pressure when the water valve is wide open and should be installed in the overflow line.

(4) Steam controller. Each retort shall be equipped with an automatic steam controller to maintain the retort tem- perature. The steam controller may be combined with a temperature-record- ing device and, thus, may be a com- bination recorder-controller. Air-oper- ated temperature controllers should have adequate filter systems to ensure a supply of clean, dry air.

(5) Steam introduction. Steam shall be distributed in the bottom of the retort in a manner adequate to provide uni- form heat distribution throughout the retort. In vertical retorts, uniform steam distribution can be achieved by any of several methods. In horizontal retorts, the steam distributor shall run the length of the bottom of the retort with perforations distributed uni- formly along the upper part of the pipe.

(6) Crate supports. A bottom crate support shall be used in vertical still retorts. Baffle plates shall not be used in the bottom of the retort. Centering guides should be installed so as to en- sure that there is about a 1.5-inch (3.8 centimeters) clearance between the side wall of the crate and the retort wall.

(7) Stacking equipment and position of containers. Crates, trays, gondolas, etc., for holding containers shall be made of strap iron, adequately perforated sheet metal, or other suitable material. When perforated sheet metal is used for the bottoms, the perforations should be approximately the equivalent of 1-inch (2.5 centimeters) holes on 2-inch (5.1 centimeters) centers. If divider plates are used between the layers of con- tainers, they should be perforated as stated in this paragraph. The posi- tioning of containers in the retort, when specified in the scheduled proc- ess, shall be in accordance with that process. Dividers, racks, trays, or other means of positioning of flexible con- tainers shall be designed and employed to ensure even circulation of heating medium around all containers in the retort.

(8) Drain valve. A nonclogging, water- tight valve shall be used. A screen shall be installed or other suitable means shall be used on all drain openings to prevent clogging.

(9) Air supply and controls. In both horizontal and vertical still retorts for pressure processing in water, a means shall be provided for introducing com- pressed air at the proper pressure and rate. The proper pressure shall be con- trolled by an automatic pressure con- trol unit. A check valve shall be pro- vided in the air supply line to prevent water from entering the system. Air or water circulation shall be maintained continuously during the come-up time and during processing and cooling peri- ods. The adequacy of the air or water circulation for uniform heat distribu- tion within the retort shall be estab- lished in accordance with procedures recognized by a competent processing authority and records shall be kept on file. If air is used to promote circula- tion, it shall be introduced into the steam line at a point between the re- tort and the steam control valve at the bottom of the retort.

(10) Water level indicator. There shall be a means of determining the water level in the retort during operation, e.g., by using a sensor, gage, water glass, or petcock(s). Water shall cover the top layer of containers during the entire come-up time and processing pe- riods and should cover the top layer of containers during the cooling periods. The operator shall check and record the water level at intervals sufficient to ensure its adequacy.

(11) Water circulation. When a water circulating system is used for heat dis- tribution, it shall be installed in such a manner that water will be drawn from the bottom of the retort through a suc- tion manifold and discharged through a spreader which extends the length of the top of the retort. The holes in the water spreader shall be uniformly dis- tributed and should have an aggregate area not greater than the cross-sec- tional area of the outlet line from the pump. The suction outlets shall be pro- tected with nonclogging screens or other suitable means shall be used to keep debris from entering the circu- lating system. The pump shall be de- signed to provide proper flow on start- up and during operation, such as with a bleeder or other suitable means to re- move air during startup and with an appropriate device or design to prevent pump cavitation during operation. The pump shall be equipped with a sig- naling device to warn the operator when it is not running. Alternative methods for circulation of water in the retort may be used when established by a competent authority as adequate for even heat distribution.

(12) Cooling water supply. In vertical retorts, the cooling water should be in- troduced at the top of the retort be- tween the water and container levels. In horizontal retorts the cooling water should be introduced into the suction side of the pump. A check valve should be included in the cooling water line.

(13) Retort headspace. The headspace necessary to control the air pressure should be maintained between the water level and the top of the retort shell.

(14) Vertical and horizontal still retorts. Vertical and horizontal still retorts should follow the arrangements in the diagrams in this paragraph. Other in- stallation and operating procedures that deviate from these arrangements may be used, as long as there is evi- dence in the form of heat distribution data or other suitable information, which shall be kept on file, which dem- onstrates that the heat distribution is adequate. LEGEND FOR VERTICAL AND HORIZONTAL STILL RETORTS A—Water line. B—Steam line. C—Temperature control. D—Overflow line. E1—Drain line. E2—Screens. F—Check valves. G—Line from hot water storage. H—Suction line and manifold. I—Circulating pump. J—Petcocks. K—Recirculating line. L—Steam distributor. M—Temperature-controller sensor. N—Temperature-indicating device sensor. O—Water spreader. P—Safety valve. Q—Vent valve for steam processing. R—Pressure gage. S—Inlet air control. T—Pressure control. U—Air line. V—To pressure control instrument. W—To temperature control instrument. X—Wing nuts. Y1—Crate support. Y2—Crate guides. Z—Constant flow orifice valve. Z1—Constant flow orifice valve used during come-up. Z2—Constant flow orifice valve used during cook.

(15) Critical factors. Critical factors specified in the scheduled process shall be measured and recorded on the proc- essing record at intervals of sufficient frequency to ensure that the factors are within the limits specified in the scheduled process.

(i) When maximum fill-in or drained weight is specified in the scheduled process, it shall be measured and re- corded at intervals of sufficient fre- quency to ensure that the weight of the product does not exceed the maximum for the given container size specified in the scheduled process.

(ii) Closing machine vacuum in vacu- um-packed products shall be observed and recorded at intervals of sufficient frequency to ensure that the vacuum is as specified in the scheduled process.

(iii) Such measurements and record- ings should be made at intervals not to exceed 15 minutes.

(iv) When the product style results in stratification or layering of the pri- mary product in the containers, the po- sitioning of containers in the retort shall be according to the scheduled process.

(c) Equipment and procedures for pres- sure processing in steam in continuous agitating retorts—(1) Temperature-indi- cating device. Each retort shall be equipped with at least one tempera- ture-indicating device that accurately indicates the temperature during proc- essing. Each temperature-indicating device shall have a sensor and a dis- play. Each temperature-indicating de- vice and each reference device that is maintained by the processor shall be tested for accuracy against a reference device for which the accuracy is trace- able to a National Institute of Stand- ards and Technology (NIST), or other national metrology institute, standard reference device by appropriate stand- ard procedures, upon installation and at least once a year thereafter, or more frequently if necessary, to ensure accu- racy during processing. Each tempera- ture-indicating device and each ref- erence device that is maintained by the processor shall have a tag, seal, or other means of identity.

(i) The design of the temperature-in- dicating device shall ensure that the accuracy of the device is not affected by electromagnetic interference and environmental conditions.

(ii) Records of the accuracy of the temperature-indicating device and of a reference device that is maintained by the processor shall be established and maintained in accordance with

§ 113.100(c) and (d).

(iii) A temperature-indicating device that is defective or cannot be adjusted to the accurate calibrated reference de- vice shall be repaired before further use or replaced.

(iv) A temperature-indicating device shall be accurate to 1 °F (0.5 °C). The temperature range of a mercury-in- glass thermometer shall not exceed 17 °F per inch (4 °C per centimeter) of graduated scale. A mercury-in-glass thermometer that has a divided mer- cury column shall be considered defec- tive.

(v) Each temperature-indicating de- vice shall be installed where it can be accurately and easily read. The tem- perature-indicating device sensor shall be installed either within the retort shell or in external wells attached to the retort. External wells or pipes shall be connected to the retort through at least a 3⁄4-inch (2 centimeters) diameter opening and equipped with a 1⁄16-inch (1.5 millimeters) or larger bleeder open- ing so located as to provide a full flow of steam past the length of the tem- perature-indicating device sensor. The bleeders for external wells shall emit steam continuously during the entire processing period. The temperature-in- dicating device—not the temperature- recording device—shall be the ref- erence instrument for indicating the processing temperature.

(2) Temperature-recording device. Each retort shall have an accurate tempera- ture-recording device. Each tempera- ture-recording device shall have a sen- sor and a mechanism for recording temperatures to a permanent record, such as a temperature-recording chart. The temperature-recording device sen- sor shall be installed either within the retort shell or in a well attached to the shell. Each temperature-recording de- vice sensor well shall have a 1⁄16-inch (1.5 millimeters) or larger bleeder that emits steam continuously during the processing period.

(i) Analog or graphical recordings. Temperature-recording devices that create analog or graphical recordings may be used. Temperature-recording devices that record to charts shall be used only with the appropriate chart. Each chart shall have a working scale of not more than 55 °F per inch (12 °C per centimeter) within a range of 20 °F (10 °C) of the process temperature. Chart graduations shall not exceed 2 °F (1 °C) within a range of 10 °F (5 °C) of the process temperature. Temperature- recording devices that create multipoint plottings of temperature readings shall record the temperature at intervals that will assure that the parameters of the process time and process temperature have been met.

(ii) Digital recordings. Temperature- recording devices, such as data loggers, that record numbers or create other digital records may be used. Such a de- vice shall record the temperature at in- tervals that will assure that the pa- rameters of the process time and proc- ess temperature have been met.

(iii) Adjustments. The temperature-re- cording device shall be adjusted with sufficient frequency to ensure agree- ment as nearly as possible with, but to be in no event higher than, the tem- perature-indicating device during proc- essing. A means of preventing unau- thorized changes in adjustment shall be provided. A lock or a notice from management posted at or near the tem- perature-recording device that provides a warning that only authorized persons are permitted to make adjustments is a satisfactory means of preventing unau- thorized changes.

(iv) Temperature controller. The tem- perature-recording device may be com- bined with the steam controller and may be a recorder-controller.

(3) Pressure gages. Each retort should be equipped with a pressure gage that is accurate to 2 pounds per square inch (13.8 kilopascals) or less.

(4) Steam controller. Each retort shall be equipped with an automatic steam controller to maintain the retort tem- perature. This may be a recorder-con- troller when combined with a tempera- ture-recording device. A steam con- troller activated by the steam pressure of the retort is acceptable if it is care- fully maintained mechanically so that it operates satisfactorily. Air-operated temperature controllers should have adequate filter systems to ensure a supply of clean, dry air.

(5) Bleeders. Bleeders, except those for temperature-indicating device wells, shall be 1⁄8-inch (3 millimeters) or larg- er and shall be wide open during the entire process, including the come-up time. Bleeders shall be located within approximately 1 foot (30.5 centimeters) of the outermost location of containers at each end along the top of the retort. Additional bleeders shall be located not more than 8 feet (2.4 meters) apart along the top of the retort. All bleeders shall be arranged so that the operator can observe that they are functioning properly. The condensate bleeder shall be checked with sufficient frequency to ensure adequate removal of condensate or shall be equipped with an automatic alarm system(s) that would serve as a continuous monitor of condensate- bleeder functioning. Visual checks should be done at intervals of not more than 15 minutes. A record of such checks should be kept to show that the bleeder is functioning properly.

(6) Venting and condensate removal. Vents shall be located in that portion of the retort opposite the steam inlet. Air shall be removed before processing is started. Heat distribution data or documentary proof from the manufac- turer or from a competent processing authority, demonstrating that ade- quate venting is achieved, shall be kept on file. At the time steam is turned on, the drain should be opened for a time sufficient to remove steam condensate from the retort, and provision shall be made for continuing drainage of con- densate during the retort operation. The condensate bleeder in the bottom of the shell serves as an indicator of continuous condensate removal.

(7) Retort speed timing. The rotational speed of the retort shall be specified in the scheduled process. The speed shall be adjusted and recorded when the re- tort is started, at any time a speed change is made, and at intervals of suf- ficient frequency to ensure that the re- tort speed is maintained as specified in the scheduled process. These adjust- ments and recordings should be made every 4 hours or less. Alternatively, a recording tachometer may be used to provide a continuous record of the speed. A means of preventing unau- thorized speed changes on retorts shall be provided. A lock or a notice from management posted at or near the speed adjustment device that provides a warning that only authorized persons are permitted to make adjustments is a satisfactory means of preventing unau- thorized changes.

(8) Emergency stops. If a retort jams or breaks down during processing oper- ations, necessitating cooling the retort for repairs, the retort shall be operated in such a way that ensures that the product is commercially sterile, or the retort is to be cooled promptly and all containers either reprocessed, repacked and reprocessed, or discarded. When op- erated as a still retort, all containers shall be given a full still retort process before the retort is cooled. If, in such an emergency, a scheduled still process or another process established to en- sure commercial sterility is to be used, it shall be made readily available to the retort operator.

(i) Any containers in the retort in- take valve or in transfer valves be- tween cooker shells of a continuous re- tort at the time of breakdown shall ei- ther be reprocessed, repacked and re- processed, or discarded.

(ii) Both the time at which the reel stopped and the time the retort was used for a still retort process, if so used, shall be indicated on the tem- perature-recording device record and entered on the other production records required in this chapter. If the alternative procedure of prompt cool- ing is followed, the subsequent han- dling methods used for the containers in the retort at the time of stopping and cooling shall be entered on the pro- duction records.

(9) Temperature drop. If the tempera- ture of the continuous retort drops below the temperature specified in the scheduled process while containers are in the retort, the retort reel shall be stopped promptly. An automatic device should be used to stop the reel when the temperature drops below the speci- fied process temperature. Before the reel is restarted, all containers in the retort shall be given a complete sched- uled still retort process if the tempera- ture drop was 10 °F (5 °C) or more below the specified temperature, or alter- natively, container entry to the retort shall be stopped and the reel restarted to empty the retort. The discharged containers shall be either reprocessed, repacked and reprocessed, or discarded. Both the time at which the reel stopped and the time the retort was used for a still retort process, if so used, shall be indicated on the tem- perature-recording device record and entered on the other production records required in this chapter. If the alternative procedure of emptying the retort is followed, the subsequent han- dling methods used for the containers in the retort at the time of the tem- perature drop shall be entered on the production records. If the temperature drop was less than 10 °F (5 °C), a sched- uled authorized emergency still process approved by a qualified person(s) hav- ing expert knowledge of thermal proc- essing requirements may be used before restarting the retort reel. Alter- natively, container entry to the retort shall be stopped and an authorized emergency agitating process may be used before container entry to the re- tort is restarted. When emergency pro- cedures are used, no containers may enter the retort and the process and procedures used shall be noted on the production records.

(10) Critical factors. Critical factors specified in the scheduled process shall be measured and recorded on the proc- essing record at intervals of sufficient frequency to ensure that the factors are within the limits specified in the scheduled process. The minimum headspace of containers, if specified in the scheduled process, shall be meas- ured and recorded at intervals of suffi- cient frequency to ensure that the headspace is as specified in the sched- uled process. The headspace of solder- tipped, lapseam (vent hole) cans may be measured by net weight determina- tions. The headspace of double seamed cans may also be measured by net weight determinations for homogenous liquids, taking into account the spe- cific can end profile and other factors which affect the headspace, if proof of the accuracy of such measurements is maintained and the procedure and re- sultant headspace is in accordance with the scheduled process. When the product consistency is specified in the scheduled process, the consistency of the product shall be determined by ob- jective measurements on the product taken from the filler before processing and recorded at intervals of sufficient frequency to ensure that the consist- ency is as specified in the scheduled process. Minimum closing machine vacuum in vacuum-packed products, maximum fill-in or drained weight, minimum net weight, and percent sol- ids shall be as specified in the sched- uled process for all products when devi- ations from such specifications may af- fect the scheduled process. All meas- urements and recordings of critical fac- tors should be made at intervals not to exceed 15 minutes.

(d) Equipment and procedures for pres- sure processing in steam in discontinuous agitating retorts—(1) Temperature-indi- cating device. Each retort shall be equipped with at least one tempera- ture-indicating device that accurately indicates the temperature during proc- essing. Each temperature-indicating device shall have a sensor and a dis- play. Each temperature-indicating de- vice and each reference device that is maintained by the processor shall be tested for accuracy against a reference device for which the accuracy is trace- able to a National Institute of Stand- ards and Technology (NIST), or other national metrology institute, standard reference device by appropriate stand- ard procedures, upon installation and at least once a year thereafter, or more frequently if necessary, to ensure accu- racy during processing. Each tempera- ture-indicating device and each ref- erence device that is maintained by the processor shall have a tag, seal, or other means of identity.

(i) The design of the temperature-in- dicating device shall ensure that the accuracy of the device is not affected by electromagnetic interference and environmental conditions.

(ii) Records of the accuracy of the temperature-indicating device and of a reference device that is maintained by the processor shall be established and maintained in accordance with

§ 113.100(c) and (d).

(iii) A temperature-indicating device that is defective or cannot be adjusted to the accurate calibrated reference de- vice shall be repaired before further use or replaced.

(iv) A temperature-indicating device shall be accurate to 1 °F (0.5 °C). The temperature range of a mercury-in- glass thermometer shall not exceed 17 °F per inch (4 °C per centimeter) of graduated scale. A mercury-in-glass thermometer that has a divided mer- cury column shall be considered defec- tive.

(v) Each temperature-indicating de- vice shall be installed where it can be accurately and easily read. The tem- perature-indicating device sensor shall be installed either within the retort shell or in external wells attached to the retort. External wells or pipes shall be connected to the retort through at least a 3⁄4-inch (2 centimeters) diameter opening and equipped with a 1⁄16-inch (1.5 millimeters) or larger bleeder open- ing so located as to provide a full flow of steam past the length of the tem- perature-indicating device sensor. The bleeders for external wells shall emit steam continuously during the entire processing period. The temperature-in- dicating device—not the temperature- recording device—shall be the ref- erence instrument for indicating the processing temperature.

(2) Temperature-recording device. Each retort shall have an accurate tempera- ture-recording device. Each tempera- ture-recording device shall have a sen- sor and a mechanism for recording temperatures to a permanent record, such as a temperature-recording chart. The temperature-recording device sen- sor shall be installed either within the retort shell or in a well attached to the shell. Each temperature-recording de- vice sensor well shall have a 1⁄16-inch (1.5 millimeters) or larger bleeder that emits steam continuously during the processing period.

(i) Analog or graphical recordings. Temperature-recording devices that create analog or graphical recordings may be used. Temperature-recording devices that record to charts shall be used only with the appropriate chart. Each chart shall have a working scale of not more than 55 °F per inch (12 °C per centimeter) within a range of 20 °F (10 °C) of the process temperature. Chart graduations shall not exceed 2 °F (1 °C) within a range of 10 °F (5 °C) of the process temperature. Temperature- recording devices that create multipoint plottings of temperature readings shall record the temperature at intervals that will assure that the parameters of the process time and process temperature have been met.

(ii) Digital recordings. Temperature- recording devices, such as data loggers, that record numbers or create other digital records may be used. Such a de- vice shall record the temperature at in- tervals that will assure that the pa- rameters of the process time and proc- ess temperature have been met.

(iii) Adjustments. The temperature-re- cording device shall be adjusted with sufficient frequency to ensure agree- ment as nearly as possible with, but to be in no event higher than, the tem- perature-indicating device during proc- essing. A means of preventing unau- thorized changes in adjustment shall be provided. A lock or a notice from management posted at or near the tem- perature-recording device that provides a warning that only authorized persons are permitted to make adjustments is a satisfactory means of preventing unau- thorized changes.

(iv) Temperature controller. The tem- perature-recording device may be com- bined with the steam controller and may be a recorder-controller.

(3) Pressure gages. Each retort should be equipped with a pressure gage that is accurate to 2 pounds per square inch (13.8 kilopascals) or less.

(4) Steam controller. Each retort shall be equipped with an automatic steam controller to maintain the retort tem- perature. This may be a recorder-con- troller when combined with a tempera- ture-recording device. A steam con- troller activated by the steam pressure of the retort is acceptable if it is me- chanically maintained so that it oper- ates satisfactorily. Air-operated tem- perature controllers should have ade- quate filter systems to ensure a supply of clean, dry air.

(5) Bleeders. Bleeders, except those for temperature-indicating device wells, shall be 1⁄8-inch (3 millimeters) or larg- er and shall be wide open during the entire process, including the come-up time. Bleeders shall be located within approximately 1 foot (30.5 centimeters) of the outermost location of con- tainers, at each end along the top of the retort; additional bleeders shall be located not more than 8 feet (2.4 me- ters) apart along the top. Bleeders may be installed at positions other than those specified in this paragraph, as long as there is evidence in the form of heat distribution data that they ac- complish adequate removal of air and circulation of heat within the retort. In retorts having top steam inlet and bottom venting, a bleeder shall be in- stalled in the bottom of the retort to remove condensate. All bleeders shall be arranged in a way that enables the operator to observe that they are func- tioning properly.

(6) Venting and condensate removal. The air in each retort shall be removed before processing is started. Heat dis- tribution data or documentary proof from the manufacturer or from a com- petent processing authority, dem- onstrating that adequate venting is achieved, shall be kept on file. At the time steam is turned on, the drain should be opened for a time sufficient to remove steam condensate from the retort and provision should be made for continuing drainage of condensate dur- ing the retort operation.

(7) Retort speed timing. The rotational speed of the retort shall be specified in the scheduled process. The speed shall be adjusted, as necessary, to ensure that the speed is as specified in the scheduled process. The rotational speed as well as the process time shall be re- corded for each retort load processed. Alternatively, a recording tachometer may be used to provide a continuous record of the speed. A means of pre- venting unauthorized speed changes on retorts shall be provided. A lock or a notice from management posted at or near the speed-adjustment device that provides a warning that only author- ized persons are permitted to make ad- justments is a satisfactory means of preventing unauthorized changes.

(8) Critical factors. Critical factors specified in the scheduled process shall be measured and recorded on the proc- essing record at intervals of sufficient frequency to ensure that the factors are within the limits specified in the scheduled process. The minimum headspace of containers in each retort load to be processed, if specified in the scheduled process, shall be measured and recorded at intervals of sufficient frequency to ensure that the headspace is as specified in the scheduled process. The headspace of solder-tipped, lap seam (vent hole) cans may be measured by net weight determinations. When the product consistency is specified in the scheduled process, the consistency of the product shall be determined by objective measurements on the product taken from the filler before processing and recorded at intervals of sufficient frequency to ensure that the consist- ency is as specified in the scheduled process. Minimum closing machine vacuum in vacuum-packed products, maximum fill-in or drained weight, minimum net weight, and percent sol- ids shall be as specified in the sched- uled process for all products for which deviations from such specifications may affect the scheduled process. All measurements and recordings of crit- ical factors should be made at intervals not to exceed 15 minutes.

(e) Equipment and procedures for pres- sure processing in water in discontinuous agitating retorts—(1) Temperature-indi- cating device. Each retort shall be equipped with at least one tempera- ture-indicating device that accurately indicates the temperature during proc- essing. Each temperature-indicating device shall have a sensor and a dis- play. Each temperature-indicating de- vice and each reference device that is maintained by the processor shall be tested for accuracy against a reference device for which the accuracy is trace- able to a National Institute of Stand- ards and Technology (NIST), or other national metrology institute, standard reference device by appropriate stand- ard procedures, upon installation and at least once a year thereafter, or more frequently if necessary, to ensure accu- racy during processing. Each tempera- ture-indicating device and each ref- erence device that is maintained by the processor shall have a tag, seal, or other means of identity.

(i) The design of the temperature-in- dicating device shall ensure that the accuracy of the device is not affected by electromagnetic interference and environmental conditions.

(ii) Records of the accuracy of the temperature-indicating device and of a reference device that is maintained by the processor shall be established and maintained in accordance with

§ 113.100(c) and (d).

(iii) A temperature-indicating device that is defective or cannot be adjusted to the accurate calibrated reference de- vice shall be repaired before further use or replaced.

(iv) A temperature-indicating device shall be accurate to 1 °F (0.5 °C). The temperature range of a mercury-in- glass thermometer shall not exceed 17 °F per inch (4 °C per centimeter) of graduated scale. A mercury-in-glass thermometer that has a divided mer- cury column shall be considered defec- tive.

(v) Each temperature-indicating de- vice shall be installed where it can be accurately and easily read. In both hor- izontal and vertical retorts, the tem- perature-indicating device sensor shall be inserted directly into the retort shell or in a separate well or sleeve at- tached to the retort. The temperature- indicating device sensor shall be lo- cated so that it is beneath the surface of the water throughout the process and where there is adequate circulation to ensure accurate temperature meas- urement. On horizontal retorts, the temperature-indicating device sensor should be located in the side at the center of the retort. The temperature- indicating device—not the tempera- ture-recording device—shall be the ref- erence instrument for indicating the processing temperature.

(2) Temperature-recording device. Each retort shall have an accurate tempera- ture-recording device. Each tempera- ture-recording device shall have a sen- sor and a mechanism for recording temperatures to a permanent record, such as a temperature-recording chart. The temperature-recording device sen- sor shall be installed either within the retort shell or in a well attached to the shell.

(i) Analog or graphical recordings. Temperature-recording devices that create analog or graphical recordings may be used. Temperature-recording devices that record to charts shall be used only with the appropriate chart. Each chart shall have a working scale of not more than 55 °F per inch (12 °C per centimeter) within a range of 20 °F (10 °C) of the process temperature. Chart graduations shall not exceed 2 °F (1 °C) within a range of 10 °F (5 °C) of the process temperature. Temperature- recording devices that create multipoint plottings of temperature readings shall record the temperature at intervals that will assure that the parameters of the process time and process temperature have been met.

(ii) Digital recordings. Temperature- recording devices, such as data loggers, that record numbers or create other digital records may be used. Such a de- vice shall record the temperature at in- tervals that will assure that the pa- rameters of the process time and proc- ess temperature have been met.

(iii) Adjustments. The temperature-re- cording device shall be adjusted with sufficient frequency to ensure agree- ment as nearly as possible with, but to be in no event higher than, the tem- perature-indicating device during proc- essing. A means of preventing unau- thorized changes in adjustment shall be provided. A lock or a notice from management posted at or near the tem- perature-recording device that provides a warning that only authorized persons are permitted to make adjustments is a satisfactory means of preventing unau- thorized changes.

(iv) Temperature controller. The tem- perature-recording device may be com- bined with the steam controller and may be a recorder-controller. Air-oper- ated temperature controllers should have adequate filter systems to ensure a supply of clean, dry air.

(3) Pressure gages. Each retort should be equipped with a pressure gage that is accurate to 2 pounds per square inch (13.8 kilopascals) or less.

(4) Steam controller. Each retort shall be equipped with an automatic steam controller to maintain the retort tem- perature. This may be a recorder-con- troller when combined with a tempera- ture-recording device. Air-operated temperature controllers should have adequate filter systems to ensure a supply of clean, dry air.

(5) Retort speed timing. The rotational speed of the retort shall be specified in the scheduled process. The speed shall be adjusted, as necessary, to ensure that the speed is as specified in the scheduled process. The rotational speed as well as the process time shall be re- corded for each retort load processed. Alternatively, a recording tachometer may be used to provide a continuous record of the speed. A means of pre- venting unauthorized speed changes shall be provided. A lock or a notice from management posted at or near the speed adjustment device that pro- vides a warning that only authorized persons are permitted to make adjust- ment is a satisfactory means of pre- venting unauthorized changes.

(6) Air supply and controls. When air is used to provide overpressure:

(i) A means shall be provided for in- troducing compressed air at the proper pressure and rate. The proper pressure shall be controlled by an automatic pressure control unit. A check valve shall be provided in the air supply line to prevent water from entering the sys- tem.

(ii) A water level indicator, e.g., sen- sor, gage, water glass, or petcock(s), shall be used for determining the water level in the retort during operation. Water shall cover the top layer of con- tainers during the entire come-up time and processing periods and should also cover the top layer of containers dur- ing the cooling periods. The operator shall check and record the water level at intervals sufficient to ensure its adequacy.

(7) Water circulation. When a water circulating system is used for heat dis- tribution, it shall be installed in such a manner that water will be drawn from the bottom of the retort through a suc- tion manifold and discharged through a spreader which extends the length of the top of the retort. The holes in the water spreader shall be uniformly dis- tributed and should have an aggregate area not greater than the cross-sec- tional area of the outlet line from the pump. The suction outlets shall be pro- tected with nonclogging screens or other suitable means shall be used to keep debris from entering the circu- lating system. The pump shall be de- signed to provide proper flow on start- up and during operation, such as with a bleeder or other suitable means to re- move air during startup and with an appropriate device or design to prevent pump cavitation during operation. The pump shall be equipped with a sig- naling device to warn the operator when it is not running. Alternative methods for circulation of water in the retort may be used when established by a competent authority as adequate for even heat distribution.

(8) Drain valve. A nonclogging, water- tight valve shall be used. A screen shall be installed or other suitable means shall be used on all drain openings to prevent clogging.

(9) Critical factors. Critical factors specified in the scheduled process shall be measured and recorded on the proc- essing record at intervals of sufficient frequency to ensure that the factors are within the limits specified in the scheduled process. The minimum headspace of containers, if specified in the scheduled process, shall be meas- ured and recorded at intervals of suffi- cient frequency to ensure that the headspace is as specified in the sched- uled process. The headspace of solder- tipped, lap seam (vent hole) cans may be measured by net weight determina- tions. When the product consistency is specified in the scheduled process, the consistency of the product shall be de- termined by objective measurements on the product taken from the filler be- fore processing and recorded at inter- vals of sufficient frequency to ensure that the consistency is as specified in the scheduled process. Minimum clos- ing machine vacuum in vacuum-packed products, maximum fill-in or drained weight, minimum net weight, and per- cent solids shall be as specified in the scheduled process for all products when deviations from such specifications may affect the scheduled process. All measurements and recordings of crit- ical factors should be made at intervals not to exceed 15 minutes.

(f) Equipment and procedures for pres- sure processing in steam in hydrostatic re- torts—(1) Temperature-indicating device. Each retort shall be equipped with at least one temperature-indicating de- vice that accurately indicates the tem- perature during processing. Each tem- perature-indicating device shall have a sensor and a display. Each tempera- ture-indicating device and each ref- erence device that is maintained by the processor shall be tested for accuracy against a reference device for which the accuracy is traceable to a National Institute of Standards and Technology (NIST), or other national metrology in- stitute, standard reference device by appropriate standard procedures, upon installation and at least once a year thereafter, or more frequently if nec- essary, to ensure accuracy during proc- essing. Each temperature-indicating device and each reference device that is maintained by the processor shall have a tag, seal, or other means of identity.

(i) The design of the temperature-in- dicating device shall ensure that the accuracy of the device is not affected by electromagnetic interference and environmental conditions.

(ii) Records of the accuracy of the temperature-indicating device and of a reference device that is maintained by the processor shall be established and maintained in accordance with

§ 113.100(c) and (d).

(iii) A temperature-indicating device that is defective or cannot be adjusted to the accurate calibrated reference de- vice shall be repaired before further use or replaced.

(iv) A temperature-indicating device shall be accurate to 1 °F (0.5 °C). The temperature range of a mercury-in- glass thermometer shall not exceed 17 °F per inch (4 °C per centimeter) of graduated scale. A mercury-in-glass thermometer that has a divided mer- cury column shall be considered defec- tive.

(v) Each temperature-indicating de- vice shall be installed where it can be accurately and easily read. The tem- perature-indicating device sensor shall be located in the steam dome near the steam-water interface. When the sched- uled process specifies maintenance of particular temperatures in the hydro- static water legs, a temperature-indi- cating device sensor shall be located in each hydrostatic water leg in a posi- tion near the bottom temperature-re- cording device sensor. The tempera- ture-indicating device—not the tem- perature-recording device—shall be the reference instrument for indicating the processing temperature.

(2) Temperature-recording device. Each retort shall have an accurate tempera- ture-recording device. Each tempera- ture-recording device shall have a sen- sor and a mechanism for recording temperatures to a permanent record, such as a temperature-recording chart. The temperature-recording device sen- sor shall be installed either within the steam dome or in a well attached to the dome. Each temperature-recording device sensor well shall have a 1⁄16-inch (1.5 millimeters) or larger bleeder that emits steam continuously during the processing period. Additional tempera- ture-recording device sensors shall be installed in the hydrostatic water legs in situations where the scheduled proc- ess specifies maintenance of particular temperatures in the hydrostatic water legs.

(i) Analog or graphical recordings. Temperature-recording devices that create analog or graphical recordings may be used. Temperature-recording devices that record to charts shall be used only with the appropriate chart. Each chart shall have a working scale of not more than 55 °F per inch (12 °C per centimeter) within a range of 20 °F (10 °C) of the process temperature. Chart graduations shall not exceed 2 °F (1 °C) within a range of 10 °F (5 °C) of the process temperature. Temperature- recording devices that create multipoint plottings of temperature readings shall record the temperature at intervals that will assure that the parameters of the process time and process temperature have been met.

(ii) Digital recordings. Temperature- recording devices, such as data loggers, that record numbers or create other digital recordings may be used. Such a device shall record the temperature at intervals that will assure that the pa- rameters of the process time and proc- ess temperature have been met.

(iii) Adjustments. The temperature-re- cording device shall be adjusted with sufficient frequency to ensure agree- ment as nearly as possible with, but to be in no event higher than, the tem- perature-indicating device during proc- essing. A means of preventing unau- thorized changes in adjustment shall be provided. A lock or a notice from management posted at or near the tem- perature-recording device that provides a warning that only authorized persons are permitted to make adjustments is a satisfactory means of preventing unau- thorized changes.

(iv) Temperature controller. The tem- perature-recording device may be com- bined with the steam controller and may be a recorder-controller.

(3) Pressure gages. Each retort should be equipped with a pressure gage that is accurate to 2 pounds per square inch (13.8 kilopascals) or less.

(4) Recording of temperatures. Tem- peratures indicated by the tempera- ture-indicating device or devices shall be entered on a suitable form during processing operations. Temperatures shall be recorded by an accurate tem- perature-recording device or devices at the following points:

(i) In the steam chamber between the steam-water interface and the lowest container position.

(ii) Near the top and the bottom of each hydrostatic water leg if the sched- uled process specifies maintenance of particular temperatures in the legs.

(5) Steam controller. Each retort shall be equipped with an automatic steam controller to maintain the retort tem- perature. This may be a recorder-con- troller when combined with a tempera- ture-recording device. A steam con- troller activated by the steam pressure of the retort is acceptable if it is care- fully mechanically maintained so that it operates satisfactorily. Air-operated temperature controllers should have adequate filter systems to ensure a supply of clean, dry air.

(6) Venting. Before the start of proc- essing operations, the retort steam chamber or chambers shall be vented to ensure removal of air.

(7) Bleeders. Bleeder openings 1⁄4-inch (6 millimeters) or larger shall be lo- cated at the top of the steam chamber or chambers opposite the point of steam entry. Bleeders shall be wide open and shall emit steam continu- ously during the entire process, includ- ing the come-up time. All bleeders shall be arranged in such a way that the operator can observe that they are functioning properly.

(8) Retort speed. The speed of the con- tainer-conveyor chain shall be speci- fied in the scheduled process and shall be determined and recorded at the start of processing and at intervals of sufficient frequency to ensure that the retort speed is maintained as specified. The speed should be determined and re- corded every 4 hours. An automatic de- vice should be used to stop the chain when the temperature drops below that specified in the scheduled process. A means of preventing unauthorized speed changes shall be provided. A lock or a notice from management posted at or near the speed-adjusting device that provides a warning that only author- ized persons are permitted to make ad- justments is a satisfactory means of preventing unauthorized changes.

(9) Critical factors. Critical factors specified in the scheduled process shall be measured and recorded on the proc- essing record at intervals of sufficient frequency to ensure that the factors are within the limits specified in the scheduled process.

(i) When maximum fill-in or drained weight is specified in the scheduled process, it shall be measured and re- corded at intervals of sufficient fre- quency to ensure that the weight of the product does not exceed the maximum for the given container size specified in the scheduled process.

(ii) Closing machine vacuum in vacu- um-packed products shall be observed and recorded at intervals of sufficient frequency to ensure that the vacuum is as specified in the scheduled process.

(iii) Such measurements and record- ings should be made at intervals not to exceed 15 minutes.

(g) Aseptic processing and packaging systems—(1) Product sterilizer—(i) Equip- ment—(A) Temperature-indicating device. Each product sterilizer shall be equipped with at least one tempera- ture-indicating device that accurately indicates the temperature during proc- essing. Each temperature-indicating device shall have a sensor and a dis- play. Each temperature-indicating de- vice and each reference device that is maintained by the processor shall be tested for accuracy against a reference device for which the accuracy is trace- able to a National Institute of Stand- ards and Technology (NIST), or other national metrology institute, standard reference device by appropriate stand- ard procedures, upon installation and at least once a year thereafter, or more frequently if necessary, to ensure accu- racy during processing. Each tempera- ture-indicating device and each ref- erence device that is maintained by the processor shall have a tag, seal, or other means of identity.

(1) The design of the temperature-in- dicating device shall ensure that the accuracy of the device is not affected by electromagnetic interference and environmental conditions.

(2) Records of the accuracy of the temperature-indicating device and of a reference device that is maintained by the processor shall be established and maintained in accordance with

§ 113.100(c) and (d).

(3) A temperature-indicating device that is defective or cannot be adjusted to the accurate calibrated reference de- vice shall be repaired before further use or replaced.

(4) A temperature-indicating device shall be accurate to 1 °F (0.5 °C). The temperature range of a mercury-in- glass thermometer shall not exceed 17 °F per inch (4 °C per centimeter) of graduated scale. A mercury-in-glass thermometer that has a divided mer- cury column shall be considered defec- tive.

(5) Each temperature-indicating de- vice shall be installed where it can be accurately and easily read. The tem- perature-indicating device—not the temperature-recording device—shall be the reference instrument for indicating the processing temperature.

(B) Temperature-recording device. Each product sterilizer shall have an accu- rate temperature-recording device. Each temperature-recording device shall have a sensor and a mechanism for recording temperatures to a perma- nent record, such as a temperature-re- cording chart. A temperature-recording device sensor shall be installed in the product at the holding-tube outlet be- tween the holding tube and the inlet to the cooler. Additional temperature-re- cording device sensors shall be located at each point where temperature is specified as a critical factor in the scheduled process.

(1) Analog or graphical recordings. Temperature-recording devices that create analog or graphical recordings may be used. Temperature-recording devices that record to charts shall be used only with the appropriate chart. Each chart shall have a working scale of not more than 55 °F per inch (12 °C per centimeter) within a range of 20 °F (10 °C) of the desired product steriliza- tion temperature. Chart graduations shall not exceed 2 °F (1 °C) within a range of 10 °F (5 °C) of the process tem- perature. Temperature-recording de- vices that create multipoint plottings of temperature readings shall record the temperature at intervals that will assure that the parameters of the proc- ess time and process temperature have been met.

(2) Digital recordings. Temperature-re- cording devices, such as data loggers, that record numbers or create other digital recordings may be used. Such a device shall record the temperature at intervals that will assure that the pa- rameters of the process time and proc- ess temperature have been met.

(3) Adjustments. The temperature-re- cording device shall be adjusted with sufficient frequency to ensure agree- ment as nearly as possible with, but to be in no event higher than, the tem- perature-indicating device during proc- essing. A means of preventing unau- thorized changes in adjustment shall be provided. A lock or a notice from management posted at or near the tem- perature-recording device that provides a warning that only authorized persons are permitted to make adjustments is a satisfactory means of preventing unau- thorized changes.

(C) Temperature controller. An accu- rate temperature controller shall be in- stalled and capable of ensuring that the desired product sterilization tem- perature is maintained. Air-operated temperature controllers should have adequate filter systems to ensure a supply of clean, dry air. (D) Product-to-product regenerators. When a product-to-product regenerator is used to heat the cold unsterilized product entering the sterilizer by means of a heat exchange system, it shall be designed, operated, and con- trolled so that the pressure of the sterilized product in the regenerator is greater than the pressure of any unsterilized product in the regenerator to ensure that any leakage in the re- generator is from the sterilized product into the unsterilized product.

(E) Differential pressure recorder-con- troller. When a product-to-product re- generator is used, it shall be equipped with an accurate differential pressure recorder-controller. The differential pressure recorder-controller shall be accurate to within 2 pounds per square inch (13.8 kilopascals). One pressure sensor shall be installed at the steri- lized product regenerator outlet and the other pressure sensor shall be in- stalled at the unsterilized product re- generator inlet. The sensor and re- corder of the differential pressure re- corder-controller shall be tested for ac- curacy against an accurate reference device upon installation and at least once every 3 months of operation thereafter, or more frequently if nec- essary, to ensure its accuracy.

(1) Analog or graphical recordings. Dif- ferential pressure recorder-controllers that create analog or graphical record- ings may be used. Differential pressure recorder-controllers that record to charts shall be used only with the ap- propriate chart. The scale divisions of the chart shall not exceed 2 pounds per square inch (13.8 kilopascals) on a working scale of not more than 20 pounds per square inch per inch of scale (55 kilopascals per centimeter). (2) Digital recordings. Differential pressure recorder-controllers, such as data loggers, that record numbers or create other digital recordings may be used. Such differential pressure re- corder-controllers shall record the dif- ferential pressure at intervals that will assure that the minimum differential pressure is maintained.

(F) Flow control. A flow control de- vice shall be located upstream from the holding tube and shall be operated to maintain the required rate of product flow. A means of preventing unauthor- ized flow adjustments shall be pro- vided. A lock or a notice from manage- ment posted at or near the flow con- trolling device that provides a warning that only authorized persons are per- mitted to make adjustments is a satis- factory means of preventing unauthor- ized changes.

(G) Product holding tube. The product- sterilizing holding tube shall be de- signed to give continuous holding of every particle of food for at least the minimum holding time specified in the scheduled process. The holding tube shall be designed so that no portion of the tube between the product inlet and the product outlet can be heated, and it must be sloped upward at least 1⁄4- inch per foot (2.1 centimeters per meter).

(H) Flow-diversion systems. If a proc- essor elects to install a flow-diversion system, it should be installed in the product piping located between the product cooler and the product filler or aseptic surge tank and should be de- signed to divert flow away from the filler or aseptic surge tank automati- cally. Controls and/or warning systems should be designed and installed with necessary sensors and actuators to op- erate whenever the sterilizing tempera- ture in the holding tube or pressure dif- ferential in the product regenerator drops below specified limits. Flow-di- version systems should be designed and operated in accordance with rec- ommendations of an aseptic processing and packaging authority.

(I) Equipment downstream from the holding tube. Product coolers, aseptic surge tanks, or any other equipment downstream from the holding tube, with rotating or reciprocating shafts, valve stems, instrument connections, or other such points, are subject to po- tential entry of microorganisms into the product. Such locations in the sys- tem should be equipped with steam seals or other effective barriers at the potential access points. Appropriate means should be provided to permit the operator to monitor the performance of the seals or barriers during operations.

(ii) Operation—(A) Startup. Before the start of aseptic processing operations the product sterilizer and all product- contact surfaces downstream shall be brought to a condition of commercial sterility.

(B) Temperature drop in product-steri- lizing holding tube. When product tem- perature in the holding tube drops below the temperature specified in the scheduled process, product flow should be diverted away from the filler or aseptic surge tank by means of a flow- diversion system. If for any reason product subjected to a temperature drop below the scheduled process is filled into containers, the product shall be segregated from product that re- ceived the scheduled process. The proc- essing deviation shall be handled in ac- cordance with § 113.89. The product holding tube and any further system portions affected shall be returned to a condition of commercial sterility be- fore product flow is resumed to the filler or to the aseptic surge tank.

(C) Loss of proper pressures in the re- generator. When a regenerator is used, the product may lose sterility when- ever the pressure of sterilized product in the regenerator is less than 1 pound per square inch (6.9 kilopascals) greater than the pressure of unsterilized prod- uct in the regenerator. In this case, product flow should be diverted away from the filler or aseptic surge tank by means of the flow-diversion system. If for any reason the product is filled into containers, the product shall be seg- regated from product that received the scheduled process. The processing devi- ation shall be handled in accordance with § 113.89. Product flow to the filler or to the aseptic surge tank shall not be resumed until the cause of the im- proper pressure relationships in the re- generator has been corrected and the affected system(s) has been returned to a condition of commercial sterility.

(D) Loss of sterile air pressure or other protection level in the aseptic surge tank. When an aseptic surge tank is used, conditions of commercial sterility may be lost when the sterile air over- pressure or other means of protection drops below the scheduled process value. Product flow to and/or from the aseptic surge tank shall not be re- sumed until the potentially contami- nated product in the tank is removed, and the aseptic surge tank has been re- turned to a condition of commercial sterility.

(E) Records. Readings at the following points shall be observed and recorded at the start of aseptic packaging oper- ations and at intervals of sufficient fre- quency to ensure that these values are as specified in the scheduled process: Temperature-indicating device in hold- ing tube outlet; temperature-recording device in holding tube outlet; differen- tial pressure recorder-controller, if a product-to-product regenerator is used; product flow rate as established by the flow control device or as determined by filling and closing rates and, if an asep- tic surge tank is used, sterile air pres- sure or other protection means; and proper performance of steam seals or other similar devices. The measure- ments and recordings should be made at intervals not to exceed 1 hour.

(2) Container sterilizing, filling, and closing operation—(i) Equipment—(A) Re- cording device. The container and clo- sure sterilization system and product filling and closing system shall be in- strumented to demonstrate that the re- quired sterilization is being accom- plished continuously. Recording de- vices shall be used to record, when ap- plicable, the sterilization media flow rates, temperature, concentration, or other factors. When a batch system is used for container sterilization, the sterilization conditions shall be re- corded.

(B) Timing method(s). A method(s) shall be used either to give the reten- tion time of containers, and closures if applicable, in the sterilizing environ- ment specified in the scheduled proc- ess, or to control the sterilization cycle at the rate specified in the scheduled process. A means of preventing unau- thorized speed changes must be pro- vided. A lock or a notice from manage- ment posted at or near the speed ad- justing device that provides a warning that only authorized persons are per- mitted to make adjustments is a satis- factory means of preventing unauthor- ized changes.

(ii) Operation—(A) Startup. Before the start of packaging operations, both the container and closure sterilizing sys- tem and the product filling and closing system shall be brought to a condition of commercial sterility.

(B) Loss of sterility. A system shall be provided to stop packaging operations, or alternatively to ensure segregation of any product packaged when the packaging conditions fall below sched- uled processes. Compliance with this requirement may be accomplished by diverting product away from the filler, by preventing containers from entering the filler, or by other suitable means. In the event product is packaged under conditions below those specified in the scheduled process, all such product shall be segregated from product that received the scheduled process. The processing deviation shall be handled in accordance with § 113.89. In the event of loss of sterility, the system(s) shall be returned to a condition of commer- cial sterility before resuming pack- aging operations.

(C) Records. Observations and meas- urements of operating conditions shall be made and recorded at intervals of sufficient frequency to ensure that commercial sterility of the food prod- uct is being achieved; such measure- ments shall include the sterilization media flow rates, temperatures, the container and closure rates (if applica- ble) through the sterilizing system, and the sterilization conditions if a batch system is used for container steriliza- tion. The measurements and recordings should be made at intervals not to ex- ceed 1 hour. (3) Incubation. Incubation tests should be conducted on a representa- tive sample of containers of product from each code; records of the test re- sults should be maintained.

(4) Critical factors. Critical factors specified in the scheduled process shall be measured and recorded on the proc- essing record at intervals of sufficient frequency to ensure that the factors are within the limits specified in the scheduled process. Such measurements and recordings should be done at inter- vals not to exceed 15 minutes.

(h) Equipment and procedures for flame sterilizers. The container conveyor speed shall be specified in the sched- uled process. The container conveyor speed shall be measured and recorded at the start of operations and at inter- vals of sufficient frequency to ensure that the conveyor speed is as specified in the scheduled process. Such meas- urements and recordings should be done at 1-hour intervals. Alternatively, a recording tachometer may be used to provide a continuous record of the speed. A means of preventing changes in flame intensity and unauthorized speed changes on the conveyor shall be provided. A lock or a notice from man- agement posted at or near the speed adjusting device that provides a warn- ing that only authorized persons are permitted to make adjustments is a satisfactory means of preventing unau- thorized changes. The surface tempera- ture of at least one container from each conveyor channel shall be meas- ured and recorded at the entry and at the end of the holding period at inter- vals of sufficient frequency to ensure that the temperatures specified in the scheduled process are maintained. Such measurements and recordings should be done at intervals not to exceed 15 minutes.

(1) Process interruption. In the event of process interruption wherein the temperature of the product may have dropped, an authorized, scheduled emergency plan approved by a qualified person having expert knowledge of the process requirements may be used.

(2) Critical factors. Critical factors specified in the scheduled process shall be measured and recorded on the proc- essing record at intervals of sufficient frequency to ensure that the factors are within the limits specified in the scheduled process.

(i) Equipment and procedures for ther- mal processing of foods wherein critical factors such as water activity are used in conjunction with thermal processing. The methods and controls used for the man- ufacture, processing, and packing of such foods shall be as established in the scheduled process and shall be op- erated or administered in a manner adequate to ensure that the product is safe. The time and temperature of processing and other critical factors specified in the scheduled process shall be measured with instruments having the accuracy and dependability ade- quate to ensure that the requirements of the scheduled process are met. All measurements shall be made and re- corded at intervals of sufficient fre- quency to ensure that the critical fac- tors are within the limits specified in the scheduled process.

(j) Other systems. All systems, wheth- er or not specifically mentioned in this part, for the thermal processing of low- acid foods in hermetically sealed con- tainers shall conform to the applicable requirements of this part and the methods and controls used for the man- ufacture, processing, and packing of these foods shall be as established in the scheduled process. These systems shall be operated or administered in a manner adequate to ensure that com- mercial sterility is achieved. Critical factors specified in the scheduled proc- ess shall be measured and recorded at intervals of sufficient frequency to en- sure that the critical factors are within the limits specified in the scheduled process.

[76 FR 11906, Mar. 3, 2011; 76 FR 81363, Dec. 28, 2011]

### Subpart D—Control of Compo- nents, Food Product Con- tainers, Closures, and In-Proc- ess Materials

## § 113.60 Containers.

(a) Closures. Regular observations shall be maintained during production runs for gross closure defects. Any such defects shall be recorded and corrective action taken and recorded. At intervals of sufficient frequency to ensure proper closure, the operator, closure super- visor, or other qualified container clo- sure inspection person shall visually examine either the top seam of a can randomly selected from each seaming head or the closure of any other type of container being used and shall record the observations made. For double- seam cans, each can should be exam- ined for cutover or sharpness, skidding or deadheading, false seam, droop at the crossover or lap, and condition of inside of countersink wall for evidence of broken chuck. Such measurements and recordings should be made at inter- vals not to exceed 30 minutes. Addi- tional visual closure inspections shall be made immediately following a jam in a closing machine, after closing ma- chine adjustment, or after startup of a machine following a prolonged shut- down. All pertinent observations shall be recorded. When irregularities are found, the corrective action shall be re- corded.

(1) Teardown examinations for dou- ble-seam cans shall be performed by a qualified individual and the results therefrom shall be recorded at inter- vals of sufficient frequency on enough containers from each seaming station to ensure maintenance of seam integ- rity. Such examinations and recordings should be made at intervals not to ex- ceed 4 hours. The results of the tear- down examinations shall be recorded and the corrective action taken, if any, shall be noted.

(i) Required and optional can seam measurements:

(a) Micrometer measurement system: Required Optional Cover hook Overlap (by calculation). Body hook Countersink. Width (length, height) Tightness (observation for wrinkle) Thickness

(b) Seam scope or projector: Required Optional Body hook Width (length, height). Overlap Cover hook. Tightness (observation for wrinkle) Countersink. Thickness by micrometer

(c) Can double seam terminology:

(1) ‘‘Crossover’’: The portion of a dou- ble seam at the lap.

(2) ‘‘Cutover’’: A fracture, sharp bend, or break in the metal at the top of the inside portion of the double seam.

(3) ‘‘Deadhead’’: A seam which is in- complete due to chuck spinning in the countersink.

(4) ‘‘Droop’’: Smooth projection of double seam below bottom of normal seam.

(5) ‘‘False seam’’: A small seam breakdown where the cover hook and the body hook are not overlapped.

(6) ‘‘Lap’’: Two thicknesses of mate- rial bonded together.

(ii) Two measurements at different locations, excluding the side seam, shall be made for each double seam characteristic if a seam scope or seam projector is used. When a micrometer is used, three measurements shall be made at points approximately 120° apart, excluding the side seam.

(iii) Overlap length can be calculated by the following formula: The theoretical overlap length = CH + BH + T ¥ W, where CH = cover hook BH = body hook T = cover thickness, and W = seam width (height, length)

(2) For glass containers with vacuum closures, capper efficiency must be checked by a measurement of the cold water vacuum. This shall be done be- fore actual filling operations, and the results shall be recorded.

(3) For closures other than double seams and glass containers, appro- priate detailed inspections and tests shall be conducted by qualified per- sonnel at intervals of sufficient fre- quency to ensure proper closing ma- chine performance and consistently re- liable hermetic seal production. Records of such tests shall be main- tained.

(b) Cooling water. Container cooling water shall be chlorinated or otherwise sanitized as necessary for cooling ca- nals and for recirculated water sup- plies. There should be a measurable re- sidual of the sanitizer employed at the water discharge point of the container cooler.

(c) Coding. Each hermetically sealed container of low-acid processed food shall be marked with an identifying code that shall be permanently visible to the naked eye. When the container does not permit the code to be em- bossed or inked, the label may be leg- ibly perforated or otherwise marked, if the label is securely affixed to the product container. The required identi- fication shall identify in code the es- tablishment where packed, the product contained therein, the year packed, the day packed, and the period during which packed. The packing period code shall be changed with sufficient fre- quency to enable ready identification of lots during their sale and distribu- tion. Codes may be changed on the basis of one of the following: intervals of 4 to 5 hours; personnel shift changes; or batches, as long as the containers that constitute the batch do not extend over a period of more than one per- sonnel shift.

(d) Postprocess handling. Container handling equipment used in handling filled containers shall be designed, con- structed, and operated to preserve the can seam or other container closure in- tegrity. Container handling equipment, including automated and non-auto- mated equipment, shall be checked with sufficient frequency and repaired or replaced as necessary to prevent damage to containers and container closures. When cans are handled on belt conveyors, the conveyors should be constructed to minimize contact by the belt with the double seam, i.e., cans should not be rolled on the double seam. All worn and frayed belting, can retarders, cushions, etc. should be re- placed with new nonporous material. All tracks and belts that come into contact with the can seams should be thoroughly scrubbed and sanitized at intervals of sufficient frequency to avoid product contamination.

[44 FR 16215, Mar. 16, 1979, as amended at 76 FR 11922, Mar. 3, 2011]

### Subpart E—Production and Process Controls

## § 113.81 Product preparation.

(a) Before using raw materials and ingredients susceptible to micro- biological contamination, the proc- essor shall ensure that those materials and ingredients are suitable for use in processing low-acid food. Compliance with this requirement may be accom- plished by receiving the raw materials and ingredients under a supplier’s guarantee that they are suitable for use, by examining them for their microbiological condition, or by other acceptable means.

(b) Blanching by heat, when required in the preparation of food for canning, should be effected by heating the food to the required temperature, holding it at this temperature for the required time, and then either rapidly cooling the food or passing it to subsequent processing without delay. Thermophilic growth and contamina- tion in blanchers should be minimized by the use of adequate operating tem- peratures and by cleaning. If the blanched food product is washed before filling, potable water should be used.

(c) The filling of containers, either mechanically or by hand, shall be con- trolled so as to ensure that the filling requirements specified in the scheduled process are met.

(d) The exhausting of containers for the removal of air shall be controlled so as to meet the conditions for which the process was designed. Compliance with the requirement may be accom- plished by heat exhausting, mechanical exhausting, hot brining, or steam in- jection.

(e) When the maintenance of pH (above 4.6) of a normally low-acid food is a basis for a scheduled process, there shall be careful supervision to ensure that the equilibrium pH of the finished product meets that of the scheduled process. The methodology described in § 114.90 of this chapter should be used.

(f) When the scheduled process sets forth critical factors to prevent the growth of microorganisms not de- stroyed by the thermal process, the factors shall be carefully controlled to ensure that the limits established in the scheduled process are not exceeded. When normally low-acid foods require sufficient solute to permit safe proc- essing at low temperatures, such as in boiling water, there shall be careful su- pervision to ensure that the equi- librium water activity (aw) of the fin- ished product meets that of the sched- uled process. The scheduled thermal processes for foods having an aw great- er than 0.85 and less than the aw that would allow the growth of spores of microorganisms of public health sig- nificance shall be sufficient to render the food free of microorganisms capa- ble of reproducing in the food under normal nonrefrigerated conditions of storage and distribution.

## § 113.83 Establishing scheduled proc- esses.
Scheduled processes for low-acid foods shall be established by qualified persons having expert knowledge of thermal processing requirements for low-acid foods in hermetically sealed containers and having adequate facili- ties for making such determinations. The type, range, and combination of variations encountered in commercial production shall be adequately pro- vided for in establishing the scheduled process. Variations include those that occur due to seasonal or growing fluc- tuations, variety differences, supplier processes, reprocessing, and mixing a batch of processed product with the same unprocessed product before it is processed. Critical factors, e.g., min- imum headspace, consistency, max- imum fill-in or drained weight, aw, etc., that may affect the scheduled process, shall be specified in the scheduled proc- ess. Acceptable scientific methods of establishing heat sterilization proc- esses shall include, when necessary, but shall not be limited to, the use of microbial thermal death time data, process calculations based on product heat penetration data, and inoculated packs. Calculation shall be performed according to procedures recognized by competent processing authorities. If in- cubation tests are necessary for proc- ess confirmation, they shall include containers from test trials and from actual commercial production runs during the period of instituting the process. The incubation tests for con- firmation of the scheduled processes should include the containers from the test trials and a number of containers from each of four or more actual com- mercial production runs. The number of containers from actual commercial production runs should be determined on the basis of recognized scientific methods to be of a size sufficient to en- sure the adequacy of the process. Com- plete records covering all aspects of the establishment of the process and associated incubation tests shall be prepared and shall be permanently re- tained by the person or organization making the determination.

[76 FR 11922, Mar. 3, 2011]

## § 113.87 Operations in the thermal processing room.

(a) Operating processes and retort venting procedures to be used for each product and container size being packed shall either be posted in a con- spicuous place near the processing equipment or be made readily available to the retort or processing system op- erator and any duly authorized em- ployee of the Food and Drug Adminis- tration. Scheduled processes must be made readily available to the super- visor and any duly authorized em- ployee of the Food and Drug Adminis- tration.

(b) A system for product traffic con- trol in the retort room shall be estab- lished to prevent unretorted product from bypassing the retort process. Each retort basket, truck, car, or crate used to hold containers in a retort, or one or more containers therein, shall, if it contains any retorted food prod- uct, be plainly and conspicuously marked with a heat-sensitive indicator, or by other effective means that will indicate visually, to thermal proc- essing personnel, those units that have been retorted. A visual check shall be performed to determine whether or not the appropriate change has occurred in the heat-sensitive indicator as a result of retorting for all retort baskets, trucks, cars, or crates, to ensure that each unit of product has been retorted. A record of these checks should be made.

(c) The initial temperature of the contents of the containers to be proc- essed shall be accurately determined and recorded with sufficient frequency to ensure that the temperature of the product is no lower than the minimum initial temperature specified in the scheduled process. For those operations that use water during the filling of the retort or during processing, provision shall be made to ensure that the water will not, before the start of each ther- mal process, lower the initial tempera- ture of the product below that specified in the scheduled process. The tempera- ture-indicating device used to deter- mine the initial temperature shall be tested for accuracy against a reference device for which the accuracy is trace- able to a National Institute of Stand- ards and Technology (NIST), or other national metrology institute, standard reference device, by appropriate stand- ard procedures, with sufficient fre- quency to ensure that initial tempera- ture measurements are accurate. Records of the accuracy of the tem- perature-indicating device and of a ref- erence device that is maintained by the processor shall be established and maintained in accordance with

§ 113.100(c) and (d).

(d) Timing devices used in recording thermal process time information shall be accurate to the extent needed to en- sure that the processing time and vent- ing time specified in the scheduled process are achieved. Pocket or wrist watches are not considered satisfactory for timing purposes. Digital clocks may be used if the operating process and the venting schedule have a 1- minute or greater safety factor over the scheduled process.

(e) Clock times on temperature-re- cording device records shall reasonably correspond to the time of day on the processing records to provide correla- tion of these records.

(f) The steam supply to the thermal processing system shall be adequate to the extent needed to ensure that suffi- cient steam pressure is maintained during thermal processing, regardless of other demands of steam by the plant.

(g) If mufflers are used on bleeders or vent systems, evidence that the bleed- ers or vents are operated in a manner that does not significantly impede the removal of air shall be kept on file. This evidence may be in the form of heat distribution data or other satis- factory evidence such as a letter from the manufacturer, the designer, or a competent processing authority.

[44 FR 16215, Mar. 16, 1979, as amended at 76 FR 11923, Mar. 3, 2011]

## § 113.89 Deviations in processing, vent- ing, or control of critical factors.
Whenever any process is less than the scheduled process or when critical fac- tors are out of control for any low-acid food or container system as disclosed from records by processor check or oth- erwise, the commercial processor of that low-acid food shall either fully re- process that portion of the production involved, keeping full records of the re- processing conditions or, alternatively, must set aside that portion of the prod- uct involved for further evaluation as to any potential public health signifi- cance. Such evaluation shall be made by a competent processing authority and shall be in accordance with proce- dures recognized by competent proc- essing authorities as being adequate to detect any potential hazard to public health. Unless this evaluation dem- onstrates that the product had been given a thermal process that rendered it free of microorganisms of potential public health significance, the product set aside shall be either fully reproc- essed to render it commercially sterile or destroyed. A record shall be made of the evaluation procedures used and the results. Either upon completion of full reprocessing and the attainment of commercial sterility or after the deter- mination that no significant potential for public health hazard exists, that portion of the product involved may be shipped in normal distribution. Other- wise, the portion of the product in- volved shall be destroyed. All process deviations involving a failure to satisfy the minimum requirements of the scheduled process, including emer- gencies arising from a jam or break- down of a continuous agitating retort necessitating cooling the retort for re- pairs, shall be recorded and made the subject of a separate file (or a log iden- tifying the appropriate data) detailing those deviations and the actions taken.

### Subpart F—Records and Reports

## § 113.100 Processing and production records.

(a) Processing and production infor- mation shall be entered at the time it is observed by the retort or processing system operator, or other designated person, on forms that include the prod- uct, the code number, the date, the re- tort or processing system number, the size of container, the approximate number of containers per coding inter- val, the initial temperature, the actual processing time, the temperature-indi- cating device and temperature-record- ing device readings, and other appro- priate processing data. Closing ma- chine vacuum in vacuum-packed prod- ucts, maximum fill-in or drained weight, or other critical factors speci- fied in the scheduled process shall also be recorded. In addition, the following records shall be maintained:

(1) Still retorts. Time steam on; time temperature up to processing tempera- ture; time steam off; venting time and temperature to which vented.

(2) Agitating retorts. Functioning of condensate bleeder; retort speed; and, when specified in the scheduled proc- ess, headspace, consistency, maximum drained weight, minimum net weight, and percent solids.

(3) Hydrostatic retorts. The tempera- ture in the steam chamber between the steam-water interface and the lowest container position; speed of the con- tainer conveyor chain; and, when the scheduled process specifies mainte- nance of particular temperatures in the hydrostatic water legs, the tempera- tures near the top and the bottom of each hydrostatic water leg.

(4) Aseptic processing and packaging systems. Product temperature in the holding tube outlet as indicated by the temperature-indicating device and the temperature-recording device; differen- tial pressure as indicated by the dif- ferential pressure recorder-controller, if a product-to-product regenerator is used; product flow rate, as determined by the flow controlling device or by filling and closing rates; sterilization media flow rate or temperature or both; retention time of containers, and closures when applicable, in the steri- lizing environment; and, when a batch system is used for container and/or clo- sure sterilization, sterilization cycle times and temperatures.

(5) Flame sterilizers. Container con- veyor speed; surface temperature at the beginning and at the end of the holding period; nature of container.

(6) Food preservation methods wherein critical factors such as water activity are used in conjunction with thermal proc- essing. Product formulation and sched- uled processes used, including the ther- mal process, its associated critical fac- tors, as well as other critical factors, and results of aw determinations.

(7) Other systems. Critical factors specified in the formulation of the product or in the scheduled process. (b) Temperature-recording device records shall be identified by date, re- tort number, and other data as nec- essary, so they can be correlated with the record of lots processed. Each entry on the processing and production records shall be made by the retort or processing system operator, or other designated person, at the time the spe- cific retort or processing system condi- tion or operation occurs, and this re- tort or processing system operator or other designated person shall sign or initial each record form. Not later than 1 working day after the actual process, and before shipment or release for dis- tribution, a representative of plant management who is qualified by suit- able training or experience shall review all processing and production records for completeness and to ensure that the product received the scheduled process. The records, including tem- perature-recording device records, shall be signed or initialed and dated by the reviewer.

(c) Records of the accuracy of a tem- perature-indicating device shall in- clude:

(1) A reference to the tag, seal, or other means of identity used by the processor to identify the temperature- indicating device;

(2) The name of the manufacturer of the temperature-indicating device;

(3) The identity of the reference de- vice, equipment, and procedures used for the accuracy test and to adjust the temperature-indicating device or, if an outside facility is used to conduct the accuracy test for the temperature-indi- cating device, a guarantee, certificate of accuracy, certificate of calibration, or other document from the facility that includes a statement or other doc- umentation regarding the traceability of the accuracy to a National Institute of Standards and Technology (NIST) or other national metrology institute standard;

(4) The identity of the person or facil- ity that performed the accuracy test and adjusted or calibrated the tempera- ture-indicating device;

(5) The date and results of each accu- racy test, including the amount of cali- bration adjustment; and

(6) The date on or before which the next accuracy test must be performed.

(d) Records of the accuracy of a ref- erence device maintained by the proc- essor shall include:

(1) A reference to the tag, seal, or other means of identity used by the processor to identify the reference de- vice;

(2) The name of the manufacturer of the reference device;

(3) The identity of the equipment and reference to procedures used for the ac- curacy test and to adjust or calibrate the reference device or, if an outside facility is used to conduct the accuracy test for the reference device, a guar- antee, certificate of accuracy, certifi- cate of calibration, or other document from the facility that includes a state- ment or other documentation regard- ing the traceability of the accuracy to a NIST or other national metrology in- stitute standard;

(4) The identity of the person or facil- ity that performed the accuracy test and adjusted or calibrated the ref- erence device;

(5) The date and results of each accu- racy test, including the amount of cali- bration adjustment; and

(6) The date on or before which the next accuracy test must be performed.

(e) Records of all container closure examinations shall specify the product code, the date and time of container closure inspections, the measurements obtained, and all corrective actions taken. Records shall be signed or ini- tialed by the container closure inspec- tor and reviewed by management with sufficient frequency to ensure that the containers are hermetically sealed. The records shall be signed or initialed and dated by the reviewer.

(f) Records shall be maintained to identify the initial distribution of the finished product to facilitate, when necessary, the segregation of specific food lots that may have become con- taminated or otherwise rendered unfit for their intended use.

(g) Copies of all records provided for in this part, except those required under § 113.83 establishing scheduled processes, shall be retained at the proc- essing plant for a period of not less than 1 year from the date of manufac- ture, and at the processing plant or other reasonably accessible location for an additional 2 years. If, during the first year of the 3-year record-retention period, the processing plant is closed for a prolonged period between sea- sonal packs, the records may be trans- ferred to some other reasonably acces- sible location at the end of the sea- sonal pack.

(h) Records of this part may be main- tained electronically, provided they are in compliance with part 11 of this chapter.

[44 FR 16215, Mar. 16, 1979, as amended at 76 FR 11923, Mar. 3, 2011]
