# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f38（主验证对象）；principle p01-p41 / case c01-c32 / counter-example n01-n43 作为各单元的证据素材归并；glossary g01-g60 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 821 页全文关键数字逐格回源抽查（15000/240、五天自检、14 位密码、62×16 通道、7000 信箱、Timer 76=80s、crystal 18/19、动态端口 10000-10499 等均与原文一致）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 36 | f01, f04-f38（除 f02/f03 外全部） |
| reference | 2 | f02（RLAB 实验平台拓扑）、f03（ITSP1 SIP 模拟器）——纯实验基础设施，仅作各能力卡 Boundary 的实验口径背景 |
| needs_review | 0（单元级） | 断言级 5 项转 needs-review.md（老化区间口径、原文笔误清单、培训约定覆盖、Statistic 标签、非故障现象判读） |
| rejected | 0 | 无编造断言；关键容量/计时器/密码数字与源文逐格一致 |

verified 明细：f01, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38

## 验证记录

```yaml
- id: f01
  title: 全书课程推进主线——准入链（登录/启停/网络/时间/库许可）+ 配置域（工具/硬件/用户）+ 业务域（呼叫处理/公网）+ 运维
  type: framework
  V1: {passed: true, reason: "p83 LESSON SUMMARY 与 p211 空库实验前置互证；模块排布与 29 项任务清单逐一对应"}
  V2: {passed: true, check_mode: walkthrough, input: "按什么顺序开局一台新 OXE", expected: "给出可执行的阶段顺序", observed: "准入链五连顺序即实验顺序（空库实验要求话务已停、OPS 恢复要求空库已建），跳章自检前置成立"}
  V3: {passed: true, expected_benefit: "全书组织轴与交付排期基线", evidence: "c02/c06/c07 验证依赖关系；n09 反证顺序不可乱"}
  decision: verified

- id: f02
  title: RLAB 实验平台两种 POD 拓扑（全虚拟/混合）与设备地址账目
  type: structure
  V1: {passed: true, reason: "p3-20 拓扑图与设备表完整，实验口径地址账号齐全"}
  V2: {passed: false, check_mode: n/a, input: "生产环境复现 RLAB 拓扑", expected: "不可", observed: "纯教学基础设施，IP/账号为教学约定值（n01），生产不可复用——按 reference 归档"}
  V3: {passed: true, expected_benefit: "实验口径 Boundary 的唯一依据；各卡 E 段实验值引用源", evidence: "p06 总表、n01"}
  decision: reference

- id: f03
  title: ITSP1 SIP 运营商模拟器拓扑与 POD 号码规则（pbxP/alcatel、DDI 41000↔31000）
  type: diagram
  V1: {passed: true, reason: "p21-26 模拟器拓扑、号码规则完整；p636 Warning 自证模拟器行为非生产口径"}
  V2: {passed: false, check_mode: n/a, input: "把 ITSP1 参数照抄到生产运营商", expected: "不可", observed: "模拟器特设口径（紧急显示、callback 规则），生产必须按 TC2005 与运营商文档重做（n29）——按 reference 归档"}
  V3: {passed: true, expected_benefit: "SIP 中继卡的实验口径锚点与生产化边界反例", evidence: "n29、c23/c24"}
  decision: reference

- id: f04
  title: OXE 系统组件全景——CS + MG + 终端 + 外部应用四层
  type: diagram
  V1: {passed: true, reason: "p30-31 组件定义与资源五类完整；中继类型谱系列全"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE 由什么组成、媒体资源在哪", expected: "CS 控制中心 + MG 承载语音指南/DTMF/会议/压缩器", observed: "p31 四层结构直接回答；与 p574 后章补 H323 无矛盾"}
  V3: {passed: true, expected_benefit: "系统观的架构底座，后续硬件/业务章的术语锚点", evidence: "g01-g03"}
  decision: verified

- id: f05
  title: 可靠性与拓扑两件套——CS Duplication / 单机集中式 / 网络式组网
  type: structure
  V1: {passed: true, reason: "p36-38 三形态与限额原文齐备（15000 用户/240 站点、100 节点/100000 分机）"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要双机热备怎么办", expected: "CS Duplication 主备同步", observed: "p36 主备持续更新机制明确；空间冗余/PCS 明示在 Advanced 课程（p131 注，n42）"}
  V3: {passed: true, expected_benefit: "售前组网边界的判定依据；数字经回源抽查一致", evidence: "p01、n42"}
  decision: verified

- id: f06
  title: 管理工具四件套矩阵——mgr / WBM / OmniVista 8770 / UMC
  type: structure
  V1: {passed: true, reason: "p45-47/p186/p224-243 四工具定位与操作口径完整"}
  V2: {passed: true, check_mode: walkthrough, input: "日常改用户用哪个工具、WBM 搜索能搜值吗", expected: "用户与业务走 WBM（免费内嵌），搜索只搜参数名不搜值", observed: "p45 免费内嵌 + p236 搜索口径原文一致；任务-工具对位关系与全书实验一致"}
  V3: {passed: true, expected_benefit: "一切业务配置的工具入口决策", evidence: "g07/g40、c15"}
  decision: verified

- id: f07
  title: 硬件承载四形态 + Common HW 机架板卡体系
  type: structure
  V1: {passed: true, reason: "p49-62 四承载形态与板卡族逐一定义；240 racks 上限回源一致"}
  V2: {passed: true, check_mode: walkthrough, input: "客户没有专用硬件怎么部署", expected: "虚拟机 OXE-V 或 GAS", observed: "p52 四形态并列；Crystal 退场背景与 p69-72/n38 一致"}
  V3: {passed: true, expected_benefit: "硬件选型与上架任务的承载面地图", evidence: "g14、n38"}
  decision: verified

- id: f08
  title: 虚拟化三线——OXE-V / OMS / GAS（含许可控制差异）
  type: structure
  V1: {passed: true, reason: "p63-68 三线定义、hypervisor 清单、编解码差异完整"}
  V2: {passed: true, check_mode: walkthrough, input: "要 OPUS/G722 高音质编解码选什么", expected: "只有 OMS 软件媒体网关支持 OPUS 与 G722", observed: "p65 'not available on hardware IPMG' 原文直接回答；与 n28 两级放行互证"}
  V3: {passed: true, expected_benefit: "虚拟化交付与编解码选型依据；证据归并 p16/p39", evidence: "g13/g12、n28"}
  decision: verified

- id: f09
  title: Crystal 退场与 XL 机架补位结构（384 FXS/奇数机位/240 racks 混装上限）
  type: structure
  V1: {passed: true, reason: "p69-80 退场原因与 XL 结构数字完整（12×FXS32-XL、-48Vdc）"}
  V2: {passed: true, check_mode: walkthrough, input: "高密度模拟口新项目选什么", expected: "XL 机架承接，Crystal 不再深入", observed: "p70 原文自注 + p75 384 FXS 结构直接回答；XL 参数占位（n38）已如实标注"}
  V3: {passed: true, expected_benefit: "存量 Crystal 与新项目的选型分流依据", evidence: "p17、n38"}
  decision: verified

- id: f10
  title: 系统访问三通道与四账户模型（root 仅本地/900 秒超时）
  type: structure
  V1: {passed: true, reason: "p84-90 通道、账户、root 限制原文齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "能通过 SSH 直接登 root 吗", expected: "不能——root 仅本地控制台直登，IP 侧必须 mtcl su", observed: "p90/p99 两处 Warning 一致；c01 实验验证"}
  V3: {passed: true, expected_benefit: "task-01 的准入骨架；证据归并 p02/n04", evidence: "p02、c01、n04"}
  decision: verified

- id: f11
  title: swinst 双菜单体系（Easy 10 项/Expert 9 项）与启停命令对照
  type: menu-path
  V1: {passed: true, reason: "p112-125 双菜单清单与启停命令原文逐项完整"}
  V2: {passed: true, check_mode: walkthrough, input: "有没有单独停话务的命令", expected: "没有——只能重启并在 5 秒窗口取消自启", observed: "p122 Notes 原文直接回答；Easy 7 连带取消 autostart（p124 Warning，n06）"}
  V3: {passed: true, expected_benefit: "task-02 的操作总入口；证据归并 c02/n05/n06", evidence: "c02、n05、n06"}
  decision: verified

- id: f12
  title: Call Server IP 双地址体系与 netadmin 配置流
  type: flow
  V1: {passed: true, reason: "p126-133/p145-149 双地址定义、netadmin 流程与强制重启原文齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "停话务后传备份文件用哪个地址", expected: "物理接口地址（Role 地址仅话务运行时生效）", observed: "p129/p733 两处一致（n08）；动态端口 10000-10499 回源一致"}
  V3: {passed: true, expected_benefit: "task-03 核心；恢复实验隐藏坑的解释源；证据归并 p07/p08/n07/n08", evidence: "c03、p07、n07、n08"}
  decision: verified

- id: f13
  title: OXE 内部防火墙（iptables）策略与可信主机管理结构
  type: structure
  V1: {passed: true, reason: "p134-144/p156-163 策略、菜单树、CSV 格式原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "新装机网络通不了先查什么", expected: "N3 起默认全关——先加可信主机白名单", observed: "p87/p135/p140 三处一致（n02）；c04 实验验证放行行为"}
  V3: {passed: true, expected_benefit: "task-04 核心；'连不上'类故障的第一分流；证据归并 p04/p05/n02/n03/n21", evidence: "c04、p04、p05、n02、n03、n21"}
  decision: verified

- id: f14
  title: NTP/chrony 双同步方法与命令面（两阶段同步法）
  type: flow
  V1: {passed: true, reason: "p164-183 六途径、chrony 参数、维护命令原文完整；chronyd 3.5 回源一致"}
  V2: {passed: true, check_mode: walkthrough, input: "时钟差了好几个月怎么校", expected: "先停 chronyd 做瞬时同步拨对，再 Start NTP 渐进维持", observed: "p172 'one shot' 口径原文一致；c05 实验验证（含 chronyc sources ^* 判据）"}
  V3: {passed: true, expected_benefit: "task-05 完整施工链；证据归并 p09/n12", evidence: "c05、p09、n12"}
  decision: verified

- id: f15
  title: MAO 数据库与空库创建流程（含抹许可连带效应）
  type: flow
  V1: {passed: true, reason: "p184-193 空库约束原文大写强调；顺序规则完整"}
  V2: {passed: true, check_mode: walkthrough, input: "把空库当'重置配置'随手执行行吗", expected: "不行——先备份 OPS，空库会连许可一起抹", observed: "p190/p192 两处 Warning 直接回答（n09）；c06 实验验证 FR 国家码与 99 条 Direct Link"}
  V3: {passed: true, expected_benefit: "task-06 的顺序红线；证据归并 p10/p38/n09", evidence: "c06、p10、p38、n09"}
  decision: verified

- id: f16
  title: OPS 许可体系——文件组/ID 体系/CAPEX-OPEX 双轨/降级模式三阶段
  type: structure
  V1: {passed: true, reason: "p194-209 OPS 四文件、四类许可 ID、锁值语义、降级节奏原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "换了 CS 主板许可会怎样", expected: "CPU-ID 不一致视为维护操作，30 天宽限后降级", observed: "p205 'every five days'/'postpones 30 days' 回源一致；c07 实验见 '30 remaining day(s)' 输出"}
  V3: {passed: true, expected_benefit: "task-07 的知识骨架与 PANIC 判读依据；证据归并 p11-p13/n10", evidence: "c07、p11、p12、p13、n10"}
  decision: verified

- id: f17
  title: GD4 硬件媒体网关上架流程（Shelf/Board/mgconfig/MAC/压缩器）
  type: flow
  V1: {passed: true, reason: "p245-258 五步流程、crystal 规则、维护命令原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "GD4 用 DHCP 地址后板子起不来查什么", expected: "勾 Ethernet Address checked by TFTP 并登记 MAC", observed: "p251/p252 原文一致（n13）；c08 实验验证 config/cplstat/rstcpl 链"}
  V3: {passed: true, expected_benefit: "task-08 施工主线；证据归并 p14/p15/p16/n13/n14/n15", evidence: "c08、p14、p15、p16、n13、n14、n15"}
  decision: verified

- id: f18
  title: OMS 虚拟媒体网关上架流程与强制字段
  type: flow
  V1: {passed: true, reason: "p259-268 四个 MANDATORY 字段与资源声明原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "往 OMS 机架里加接口板行吗", expected: "禁止——OMS 机架不得声明扩展架与板卡", observed: "p260-261 大写警告直接回答（n16）；c09 实验验证 omsconfig 与 spadmin #384/#385"}
  V3: {passed: true, expected_benefit: "task-09 施工主线；口令差异防混淆；证据归并 p14/n15/n16", evidence: "c09、p14、n15、n16"}
  decision: verified

- id: f19
  title: XL 机架上架流程与机位规划（奇数位/GA-XL 占 1/2 槽）
  type: flow
  V1: {passed: true, reason: "p757-772 机位规则、GA-XL 强制位置、动态 IP 的 MAC 要求原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "XL 架地址能随便挑吗", expected: "必须奇数位且 X/X+1 连续空闲", observed: "p758 原文一致；c29 实验验证（9/10 位、FXS32 放 3-6 槽口诀）"}
  V3: {passed: true, expected_benefit: "task-10 施工主线；证据归并 p17/n14/n38", evidence: "c29、p17、n14、n38"}
  decision: verified

- id: f20
  title: 用户开通三法与终端绑定标识（MAC/Phone Identifier/物理地址）
  type: structure
  V1: {passed: true, reason: "p290-296 三法绑定与分机唯一性原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "IP 话机换新机怎么处理", expected: "改绑 MAC（自动分配=清除后重新回收）", observed: "p294 'Must be removed when device replacement' 原文一致；c12/c13 实验验证"}
  V3: {passed: true, expected_benefit: "task-11/12/14 的绑定模型总纲；证据归并 p19", evidence: "c12、c13、p19"}
  decision: verified

- id: f21
  title: IP 话机两态开通操作链（静态 MMI / 动态 CS DHCP）
  type: flow
  V1: {passed: true, reason: "p320-329/p355-365 两态操作与 DHCP 规则原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "话机动态模式取不到地址查什么", expected: "CS 内部 DHCP 默认关闭（DHCP off）", observed: "p356 原文一致（p21/n20）；c12/c14 实验验证两态闭环与 dhcplog 四步"}
  V3: {passed: true, expected_benefit: "task-11/15 施工主线；证据归并 p20/p21/n19/n20", evidence: "c12、c14、p20、p21、n19、n20"}
  decision: verified

- id: f22
  title: 编号计划体系——Prefix/Suffix Plan 与 Timer 23 饱和对策
  type: structure
  V1: {passed: true, reason: "p366-388 前缀规则、Timer 23 默认值、规划分段建议原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "拨 31 等 3 秒才继续，是什么", expected: "31T 功能前缀与 31000 分机的 Timer 23 歧义消解（默认 3 秒）", observed: "p370 原文一致（p22）；c15 实验验证 ednump/listrad 巡检"}
  V3: {passed: true, expected_benefit: "task-16 的路由地基；证据归并 p22/n22", evidence: "c15、p22、n22"}
  decision: verified

- id: f23
  title: 双 COS 体系——Phone Features COS（256 类）与 Connection/Transfer COS 矩阵
  type: structure
  V1: {passed: true, reason: "p389-420 七分区、矩阵结构、Transfer 同 ID 独立矩阵原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "要禁止某用户打国际长途改哪套 COS", expected: "改 Public COS（外呼域），Phone Features COS 管功能不管外呼区域", observed: "p390 分区清单与 p659 Public COS 定义支撑该分流；c16/c17 实验验证行为闭环"}
  V3: {passed: true, expected_benefit: "task-17 的概念分流器；证据归并 p23", evidence: "c16、c17、p23"}
  decision: verified

- id: f24
  title: 静态语音指南与音乐保持体系（槽位/索引/MOH 激活/选择规则）
  type: structure
  V1: {passed: true, reason: "p425-448 载体容量、语言索引、MOH 激活二步、文件路径原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "保持音乐不生效查什么", expected: "MOH 激活=删 Tone 2 + 建 VG 2（p436 原文二步）", observed: "c18 实验验证 580 试听与 vgstat 槽位；16/120 并发回源一致"}
  V3: {passed: true, expected_benefit: "task-18 施工主线；证据归并 p24/p38/p41/n22", evidence: "c18、p24、p38、p41、n22"}
  decision: verified

- id: f25
  title: 话务台体系——Attendant group / Attendant set / 4059EE / BLF
  type: structure
  V1: {passed: true, reason: "p449-478 三层结构、限额（50 组/250 台）、呈现模式原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "只有一个话务员还要建组吗", expected: "要——话务台必须隶属一个组（p451 Note）", observed: "c19 实验验证建组/4059EE 关联/BLF/系统参数闭环"}
  V3: {passed: true, expected_benefit: "task-19 施工主线；证据归并 p25/n18/n23/n24", evidence: "c19、p25、n18、n23、n24"}
  decision: verified

- id: f26
  title: Entity 体系——逻辑分区/CDT 四状态/状态小时表/经理组
  type: structure
  V1: {passed: true, reason: "p496-513 Entity 0-1000、CDT 3+1 结构、经理组机制原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "夜间来话自动转手机之外的号码怎么配", expected: "实体 CDT 溢出号（夜转号，必须单线分机）", observed: "p500 原文一致；c20 实验验证经理组驱动 Day/Night 切换"}
  V3: {passed: true, expected_benefit: "task-20 与外呼闭锁的实体地基；证据归并 p26/n25", evidence: "c20、p26、n25"}
  decision: verified

- id: f27
  title: OmniMessage 4645 四种部署拓扑与容量口径
  type: structure
  V1: {passed: true, reason: "p526-546 拓扑、容量、编解码、组网原文完整；7000/30/500(600) 回源一致"}
  V2: {passed: true, check_mode: walkthrough, input: "一个节点能装两套语音邮件吗", expected: "不能——每 OXE 节点仅一个 VM 系统", observed: "p527 原文一致（n33）；c21 实验验证许可锁与信箱分配"}
  V3: {passed: true, expected_benefit: "task-21 部署决策与容量承诺依据；证据归并 p27/n33/n34", evidence: "c21、p27、n33、n34"}
  decision: verified

- id: f28
  title: UMC 云管理平台结构与边界（R1.1，Easy users/Easy SIP trunk/Expert Configuration）
  type: structure
  V1: {passed: true, reason: "p797-814 三大功能、前提（N3-MD3/SPS/PoD/FTR&RTR）、排除清单原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "UMC 能管话务台和 ACD 吗", expected: "不能——排除清单明确（Attendant/ACD/ALES 坐席等）", observed: "p802 排除清单直接回答（n39）；原书为纯讲义章无实验，结构判断成立"}
  V3: {passed: true, expected_benefit: "task-29 的能力边界与商务前提；证据归并 p37/n39/n40", evidence: "p37、n39、n40"}
  decision: verified

- id: f29
  title: 去话九步链路图（ARS 前缀/鉴别符/ARS 表/TG/NPD/DID/外部网关）
  type: diagram
  V1: {passed: true, reason: "p578-602/p659-666 九步链路与各对象定义原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "外呼通了但对方看到的号码不对查哪几步", expected: "NPD 号码格式、DID 翻译器 CLI 组装、回叫翻译器修饰", observed: "p582/p600-601 链路职责原文一致；c23 实验按此链路复测 CLI"}
  V3: {passed: true, expected_benefit: "task-22/23 的路由总图；证据归并 p29/n26/n27", evidence: "c23、p29、n26、n27"}
  decision: verified

- id: f30
  title: 来话链路与回叫翻译器（DID 落地/Caller Id 修饰）
  type: diagram
  V1: {passed: true, reason: "p586-603 来话三步与翻译器规则（A/B/DEF、255 个/20 条）原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "未接来电显示 +33… 回拨不通怎么办", expected: "配回叫翻译器规则（如 A33 去 3 位加 00）", observed: "p600-602 语法原文一致；c23 步骤 7 实验验证"}
  V3: {passed: true, expected_benefit: "task-22 来话侧闭环；证据归并 p29/n29", evidence: "c23、p29、n29"}
  decision: verified

- id: f31
  title: 紧急呼叫通知机制链（区域/Location ID/紧急组）
  type: flow
  V1: {passed: true, reason: "p682-699/p604-607 机制四要素、P-ANI 头、边界数值原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "组网（多节点）客户能用紧急通知吗", expected: "不能——仅 stand-alone 单节点（PCS 排除）", observed: "p683 原文一致（n31）；c26 实验验证 P-ANI 复测与紧急组动作"}
  V3: {passed: true, expected_benefit: "task-24 完整机制与合规边界；证据归并 p31/p32/n31/n32", evidence: "c26、p31、p32、n31、n32"}
  decision: verified

- id: f32
  title: 呼叫分配计时器图集（76/141/144/140/142/102/trunk COS/Entity 溢出）
  type: diagram
  V1: {passed: true, reason: "p700-708 计时器默认值与触发语义原文完整；76=800/144=150 回源一致"}
  V2: {passed: true, check_mode: walkthrough, input: "外线呼入用户不接等多久溢出", expected: "trunk COS 的 Overflow Timer（默认 300=30 秒），内线才是 144", observed: "p713 原文一致；c27 实验内外线分段验证"}
  V3: {passed: true, expected_benefit: "task-25 调参与排障依据；证据归并 p33/n23", evidence: "c27、p33、n23"}
  decision: verified

- id: f33
  title: 数据库备份/恢复体系（自动 5:45 + IMMED/OPS 分区 + Cloud/Rainbow 剥离选项）
  type: flow
  V1: {passed: true, reason: "p720-736 分区清单、恢复三选项、物理地址 Warning 原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "恢复时 SFTP 连不上 CS", expected: "话务已停，Role 地址失效——必须用 CS 物理地址", observed: "p733 大写 Warning 直接回答（n08/n37）；c28 实验验证恢复闭环"}
  V3: {passed: true, expected_benefit: "task-26 灾备底线与隐藏坑清单；证据归并 p34/n37", evidence: "c28、p34、n37"}
  decision: verified

- id: f34
  title: 维护排障工具箱八件套（oxetrace/ippstat/事件三件/securitystatustool/infocollect/tcpdump）
  type: structure
  V1: {passed: true, reason: "p737-756 八件套用途、账户要求、3GB 空间口径原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "ALE 支持要现场提供什么", expected: "infocollect 打包的 .tbz（root 运行）", observed: "p754 原文一致；c32 命令序列含 oxetrace 四子目录与解码"}
  V3: {passed: true, expected_benefit: "task-27 一线排障闭环；证据归并 p35/p41/n43", evidence: "c32、p35、p41、n43"}
  decision: verified

- id: f35
  title: T0/T2 中继组开通流程（传统 ISDN 线）
  type: flow
  V1: {passed: true, reason: "p773-796 参数组、节点号强制、信令变体、同步优先级原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "T0 的信令变体选 ISDN France 还是 all countries", expected: "按运营商：VN 用 France、ETSI 用 all countries", observed: "p784 原文一致；c30/c31 实验验证（教室口径已标注）"}
  V3: {passed: true, expected_benefit: "task-28 施工主线；证据归并 p36/n27/n29", evidence: "c30、c31、p36、n27、n29"}
  decision: verified

- id: f36
  title: 公共 SIP 中继开通主流程（系统参数/TG/网关/ARS/鉴别符/NPD-DID/回叫/国际紧急八段）
  type: flow
  V1: {passed: true, reason: "p609-640 八段流程与 Warning（ARS 强制/编解码两级）原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "SIP 中继能像 ISDN 一样 #010 直抓吗", expected: "不能——ARS 是 SIP 中继使用的强制前提", observed: "p616/p665 两处一致（n27）；c23 实验全链路验证含 484→DID 修复"}
  V3: {passed: true, expected_benefit: "task-22 全书中权重最高的实验链主线；证据归并 p28/p29/p30/n26-n29", evidence: "c23、p28、p29、p30、n26、n27、n28、n29"}
  decision: verified

- id: f37
  title: SIP 网关双机备份与负载均衡两案（ARS 第二路由 / SIP Pool）
  type: flow
  V1: {passed: true, reason: "p641-656 两案配置、故障注入测试法、Supervision timer 警告原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "主网关宕了切换很慢怎么治", expected: "Pool 场景把 Supervision timer 设短（例 5 秒）", observed: "p651 原文一致（n30）；c24 实验以 .bad FQDN 注入验证切换与复原"}
  V3: {passed: true, expected_benefit: "task-22 弹性设计；证据归并 p30/n30", evidence: "c24、p30、n30"}
  decision: verified

- id: f38
  title: 外呼闭锁操作链（真实鉴别符分区 + Public COS 放行 + Entity 影响）
  type: flow
  V1: {passed: true, reason: "p657-681 数值（8/256/64/32）、默认 Night 态、实体影响 Warning 原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Public COS 明明放行了还是打不出去", expected: "实体默认 Night 态——四状态列要按当前态放行", observed: "p674 大写原文一致（n25）；c25 实验三分区/放行/换实体验证"}
  V3: {passed: true, expected_benefit: "task-23 合规配置与防盗打；证据归并 p29/n25/n26", evidence: "c25、p29、n25、n26"}
  decision: verified
```

## 断言级裁决记录

1. **密码老化期区间口径**：原文 p93 为开区间 "10 < validity period for password in DAYS < 366"，BOOK_OVERVIEW 简写为"10-366 天"。按原文开区间记录（10 与 366 两个端点值本身不可用），详见 needs-review nr-01。
2. **话务台呈现模式标签 "Statistic"**：p451 原文如此，行为描述为"轮转呈现、最长待命优先"。标签疑为原文用词变体，保留照录、按行为转述，详见 nr-04。
3. **非故障现象判读（n43）**：BAD PCMS CODE、unknown rack type、484 Address Incomplete 三类"实验中看着像故障的正常现象"，其"实验环境占位/预期失败"的判断属谨慎解读（书中未逐条解释），已标推断口径——引用时注明。
4. **无 rejected 断言**：15000 用户/240 站点、240 racks、14 位密码九规则、3-5 次锁定、5 天自检/30 天宽限、62×16=992 通道、7000 信箱/30 端口、Timer 76/141/144/140/142/102/23/4 默认值、crystal 1-255（18/19 保留）、动态端口 10000-10499、同步优先级 0-199/200-254/255——全部回源抽查与原文逐格一致。
5. **单元级 needs_review 为 0**：两处 reference（f02/f03）为实验基础设施的定位性归档（书中自证其教学专用属性），属诚实边界；无需复核的矛盾未在单元级出现，笔误与口径问题全部下沉至断言级（needs-review.md）。
