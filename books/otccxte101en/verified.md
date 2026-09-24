# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f34（主验证对象）；principle p01-p33 / case c01-c15 / counter-example n01-n42 作为各单元的证据素材归并；glossary g01-g56 转 GLOSSARY（见 references.md）
> 验证人: 验证阶段执行者（2026-09-23），基于 597 页全文定位抽查 + 提取器页码证据交叉核对（p77 容量表、p186 ISM 手算、p513-514 中继数学、p557-558 接入容量等关键数字已回 source_fulltext.txt 逐格复核）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 31 | f01, f05-f34（f02/f03/f04 除外，详见下表） |
| reference | 3 | f02（RLAB POD 拓扑）、f03（软话机布局与双接入通道）、f04（ITSP1 SIP 模拟器）——教学专用基础设施，仅作 Boundary 背景与测试口径 |
| needs_review | 0（单元级） | 断言级 5 项转 needs-review.md（p558 "29 or 120"、p236 统计 Pilot 号、LAST_CALL_ 命名混用、p364 坐席称号、21 次双口径） |
| rejected | 0 | 无编造断言；ACR/SPM 两张容量表与 ISM 算例逐格核对一致 |

verified 明细：f01, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34

## 验证记录

```yaml
- id: f01
  title: 全书课程推进主线——环境基线 → ACR 高级路由主线 → 网络互助 → 增值工具域
  type: framework
  V1: {passed: true, reason: "p1-2 目录 + 15 个 How-To 章与讲义章严格成对（p39/p48/p130/p182/p204/p209/p235/p260/p338/p396/p455/p491/p516/p544/p580 开篇核验）"}
  V2: {passed: true, check_mode: walkthrough, input: "Advanced 级现场按什么顺序交付", expected: "环境与基线在前、ACR 主线居中、网络与增值域收尾", observed: "四段主线与 c01→c02→c03→c06→c07→c08→c09 实验依赖链一致，顺序无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线与依赖检查单"}
  decision: verified

- id: f02
  title: RLAB 实验 POD 拓扑与实例账号表——OXE 双节点 + Windows 族
  type: diagram
  V1: {passed: true, reason: "p7/p9 拓扑与实例表完整；全部为实验给定值"}
  V2: {passed: true, check_mode: walkthrough, input: "远程节点 CCS 填哪个 IP", expected: "主 CPU 地址 192.168.1.103", observed: "p9 表与 f07 声明步骤一致"}
  V3: {passed: true, expected_benefit: "实验环境背景与测试口径；不进生产"}
  decision: reference

- id: f03
  title: 客户端软话机布局与双接入通道——MicroSIP/IPDSP 分工 + Console/RDP
  type: structure
  V1: {passed: true, reason: "p10-13/p60-62 布局与通道定义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "坐席软话机没声音先查什么", expected: "RDP 通道音频设置", observed: "p61-62 与 n42 一致（播放/录音指向本机）"}
  V3: {passed: true, expected_benefit: "实验操作背景；教学专用布局不套生产"}
  decision: reference

- id: f04
  title: ITSP1 公共 SIP 运营商模拟器——拓扑、账号与号码变换规则
  type: diagram
  V1: {passed: true, reason: "p16-17 账号与号码表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "POD6 的 DID 首外号是什么", expected: "33210641000", observed: "p57 明确给出 POD6 示例，与 p17 号码规则同源（p19）"}
  V3: {passed: true, expected_benefit: "呼入测试口径；教学专用号码不套生产"}
  decision: reference

- id: f05
  title: CCD 预配置基线总览——矩阵、双 Pilot、坐席体系与本地 ABC-F 链路
  type: structure
  V1: {passed: true, reason: "p19-38 预配置五节齐备（p20 目录页核验）"}
  V2: {passed: true, check_mode: walkthrough, input: "Advanced 实验的起点是什么状态", expected: "Pilot1/Pilot2、坐席、班长、ABC-F 链路就绪", observed: "p20 检查单与 p50 预配置清单互证；31xxx 号段为实验口径"}
  V3: {passed: true, expected_benefit: "认知起点：所有实验跑在预配置之上，不从零建矩阵"}
  decision: verified

- id: f06
  title: CCsupervision（CCS）软件安装流程——从 NAS 解包到装后重启
  type: flow
  V1: {passed: true, reason: "p39-43 八步向导逐步可循；p349-352 同流程重复出现可作 SOP 互证"}
  V2: {passed: true, check_mode: walkthrough, input: "本章要不要装 ASM Script Editor 组件", expected: "选 No，独立安装章另有专用 msi", observed: "p42-43 明确 No；与 n03 专用 asm-se_setup.msi 口径一致"}
  V3: {passed: true, expected_benefit: "CCS 部署标准 SOP；证据归并 c01/p22/n01"}
  decision: verified

- id: f07
  title: CCS 声明 OXE 与 Navigator 连通验证——ccs.ini 写入后必须重启
  type: flow
  V1: {passed: true, reason: "p44-47 声明路径与重启要求原文明确"}
  V2: {passed: true, check_mode: walkthrough, input: "改完 Call Server IP 连不上", expected: "漏了重启 CCS", observed: "p45 原文 'must restart the CCS'；n02 同口径"}
  V3: {passed: true, expected_benefit: "CCS 类排障第一检查点；证据归并 c01/n02"}
  decision: verified

- id: f08
  title: POD 定稿四件套——SIP 扩展用户、外部 SIP 网关注册、DID 翻译、呼入验证
  type: flow
  V1: {passed: true, reason: "p51-59 六步序列与参数完整（p56/p57/p58 逐项核验）"}
  V2: {passed: true, check_mode: walkthrough, input: "呼入 Pilot1 拨什么号", expected: "0210X41600（X=POD 号）", observed: "p58 与 p17 号码规则一致；验证点含自动 wrap-up"}
  V3: {passed: true, expected_benefit: "一切实验的基线验收；证据归并 c02/p19/n42"}
  decision: verified

- id: f09
  title: ASM 架构——AFE、ASM 服务器、脚本编辑器三角色
  type: diagram
  V1: {passed: true, reason: "p68-70 架构与职责逐条给出"}
  V2: {passed: true, check_mode: walkthrough, input: "坐席列表由谁算、脚本由谁存", expected: "ASM 服务器计算，脚本存 /usr3/afe（alb 进程）", observed: "p69-70 与 p198 存储路径一致；g02/g08 互证"}
  V3: {passed: true, expected_benefit: "ACR 排障的角色分工底图；证据归并 g02/g08/p08"}
  decision: verified

- id: f10
  title: ACR 呼叫分发三步——特征化 → 生成动态组 → 等待室分配
  type: diagram
  V1: {passed: true, reason: "p71-75 三步模型与特征化信息源齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "等待室和等待队列能同时开吗", expected: "同一规则内互斥", observed: "p71-72 原文 CANNOT be open at the same time；f12 互证"}
  V3: {passed: true, expected_benefit: "ACR 运行模型主轴；证据归并 g11/g12/g14/n18"}
  decision: verified

- id: f11
  title: ACR 容量上限表（Provisioning Level）
  type: structure
  V1: {passed: true, reason: "p77 十二项上限一页齐备；本次抽查 source_fulltext 逐格一致"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要 25 个技能域行不行", expected: "不行，域上限 20", observed: "p77 Domains: 20 直接回答；超限指针 Feature List"}
  V3: {passed: true, expected_benefit: "容量合规红线表；与 p394 SPM 限制（p26）配对；证据归并 p05/n39"}
  decision: verified

- id: f12
  title: ACR Pilot 路由规则与等待室行为矩阵——互斥、饱和、同优先级、门限
  type: diagram
  V1: {passed: true, reason: "p81-92 五条行为规则与参数定义齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "同优先级方向怎么选", expected: "比 EWT 取最小", observed: "p86-87 原文明确；与 p17 MWT/TSP 定义构成同一机制两面"}
  V3: {passed: true, expected_benefit: "路由行为排障的判据集；证据归并 p17/n34/n36"}
  decision: verified

- id: f13
  title: CCS 侧 ACR 集成——权限、技能矩阵、统计与实时视图分区
  type: structure
  V1: {passed: true, reason: "p96-114 五个分区（安装/权限/技能/统计/实时）逐区有页面证据"}
  V2: {passed: true, check_mode: walkthrough, input: "班长看不到 ACR 菜单", expected: "未授 Advanced Call Routing 与 /ACR Data 权限", observed: "p99-101 权限项明确"}
  V3: {passed: true, expected_benefit: "CCS 侧 ACR 管理的操作地图；证据归并 p06/g25"}
  decision: verified

- id: f14
  title: ACR 对象菜单路径全集——OXE WBM 与 CCS 双侧
  type: menu
  V1: {passed: true, reason: "p119-126/p134-158 路径与示例值齐备；讲义示例号与实验号并存已注明"}
  V2: {passed: true, check_mode: walkthrough, input: "统计 Pilot 在哪建", expected: "Applications > CCD > Statistic pilot", observed: "p123 路径明确；实验值 31660/31661（p135-136）与讲义示例 31650（p123）并存已登记（nr-02）"}
  V3: {passed: true, expected_benefit: "双侧配置的路径字典；证据归并 c03/n13"}
  decision: verified

- id: f15
  title: agacd 与 adm_acd 命令树——OXE 侧 ACD 数据维护入口
  type: menu
  V1: {passed: true, reason: "p127-128 命令树 + p176/p257 -salb 分支齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "查 ASM 记忆里某个主叫的记录", expected: "adm_acd <ASM IP> -salb option 28 输 CLID", observed: "p257 明确；* 列全部"}
  V3: {passed: true, expected_benefit: "售后排障命令箱主干；证据归并 g54/c08/c15"}
  decision: verified

- id: f16
  title: ACR Management 实验对象创建序列——编号方案与操作顺序
  type: flow
  V1: {passed: true, reason: "p130-159 七步序列含全部实验编号（31803/31704/31603/31660/31661）"}
  V2: {passed: true, check_mode: walkthrough, input: "技能没赋给坐席时等待室什么状态", expected: "阻塞（红）", observed: "p148 'If the Agent does not have any skill, the Waiting Room is blocked!'；p154 赋技能后打开，n19 同口径"}
  V3: {passed: true, expected_benefit: "ACR 矩阵从零到验收的施工序列；证据归并 c03/n19"}
  decision: verified

- id: f17
  title: Navigator 定制视图——Tab 页与对象显隐
  type: menu
  V1: {passed: true, reason: "p147-148 定制流程 + p237 实时参数设置齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "只想看 ACR 相关对象怎么设", expected: "定制 Tab8 隐藏无关 Pilot/队列/PG", observed: "p148 步骤完整（Record 保存）"}
  V3: {passed: true, expected_benefit: "实时观察与验收的视图抓手；证据归并 g56/c03/c07"}
  decision: verified

- id: f18
  title: 呼叫档案/坐席档案数据模型——域、技能、等级、权重的四层结构
  type: structure
  V1: {passed: true, reason: "p163-166 四层模型与区间定义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "坐席最多配几个技能", expected: "50", observed: "p102 与 p77 Characteristics per Agent 50 互证"}
  V3: {passed: true, expected_benefit: "ISM 的数据底座；证据归并 p06/g16/n17"}
  decision: verified

- id: f19
  title: ISM 子列表降级算法——从满配匹配到全不匹配的 N 级漏斗
  type: flow
  V1: {passed: true, reason: "p168-172 算法三规则与列表长度参数齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "坐席强制属性等级不够进第一子列表吗", expected: "不进（坐席等级须 ≥ 呼叫等级）", observed: "p169 + p185 Agent5 案例一致"}
  V3: {passed: true, expected_benefit: "解释分配次序的核心模型；证据归并 p01/p02/p07/p10"}
  decision: verified

- id: f20
  title: ASM Script Editor 入口、工具栏与积木块清单
  type: menu
  V1: {passed: true, reason: "p189-196 入口/两模式/积木块四组齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "脚本能不能留悬空的入口出口", expected: "不能", observed: "p195/p212 原文 not allowed；n05 同口径"}
  V3: {passed: true, expected_benefit: "脚本能力的工具地图；证据归并 c05/n03/n05"}
  decision: verified

- id: f21
  title: 脚本生命周期——在线/离线创建 → 编译 → 激活绑定 Pilot
  type: flow
  V1: {passed: true, reason: "p197-202/p210-213 五步生命周期与产物规则齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "换脚本要不要重新激活", expected: "要，一 Pilot 一脚本", observed: "p199/p213/p217 三处同口径（p09/n06）"}
  V3: {passed: true, expected_benefit: "脚本交付的标准动作序列；证据归并 p08/p09/c06"}
  decision: verified

- id: f22
  title: 脚本调试器三窗格与四种过滤器——跟踪路由全流程
  type: structure
  V1: {passed: true, reason: "p221-233 三窗格与过滤器/Make call 规则齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "Make call 的发起分机能用坐席号吗", expected: "不能，必须普通用户", observed: "p225 全大写警告（n10）"}
  V3: {passed: true, expected_benefit: "路由排障的差异化能力；证据归并 c07/n10-n12"}
  decision: verified

- id: f23
  title: LCA 记忆模型与维护命令——ASM 为谁记什么、清到哪里
  type: structure
  V1: {passed: true, reason: "p248-258 记忆内容/7 状态码/维护命令齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "重启 MAIN_AFE 能清 LCA 记忆吗", expected: "不能，必须 kill alb", observed: "p252 原文 no effect；p272 清理三步（n15/p14 同口径）"}
  V3: {passed: true, expected_benefit: "回头客路由能力的记忆底座；证据归并 p12-p14/n15/n16/c08"}
  decision: verified

- id: f24
  title: 网络互助双模型与拒收回退表——Blind vs Intelligent mutual aid
  type: diagram
  V1: {passed: true, reason: "p293-315 两模型定义、ABC-F 条件与五类回退表齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "远端拒收后呼叫去哪", expected: "按远端 Pilot 地址类型回退本地（重路由组/GFWD/闭锁/排队溢出/振铃溢出五类）", observed: "p312 回退表逐项核对一致"}
  V3: {passed: true, expected_benefit: "多站点互助的决策与排障依据；证据归并 g20/n35"}
  decision: verified

- id: f25
  title: Remote PG 分布式互助三对象与管理路径——本地/远端分工
  type: structure
  V1: {passed: true, reason: "p316-336 三对象定义、传输信息与管理路径齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "Remote PG 有呼叫选择优先级吗", expected: "没有，只有资源选择优先级+分布门限", observed: "p319 原文明确；p15/p16 行为验证一致"}
  V3: {passed: true, expected_benefit: "分布式互助的施工与验收骨架；证据归并 c09/g21/p15/p16"}
  decision: verified

- id: f26
  title: ABC-F 直连链路诊断——compvisu sys 与 hybvisu 输出解读
  type: menu
  V1: {passed: true, reason: "p341-342 两命令输出字段与四态/两档定义齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "链路健康状态长什么样", expected: "UP(Enabled/DATA_TRANS)", observed: "p341 实验输出与 p342 四态定义一致（p20）"}
  V3: {passed: true, expected_benefit: "互助故障注入与链路体检的判读表；证据归并 c09/p20/g44"}
  decision: verified

- id: f27
  title: Soft Panel Manager 架构与安装三件套流程
  type: flow
  V1: {passed: true, reason: "p371-395 架构与限制 + p396-411 安装 How-To 齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "CCS 和 RTI Connector 同机时能手工开 CCS 吗", expected: "不能，CCS 必须专用于 RTI Connector", observed: "p405 全大写警告（n21）"}
  V3: {passed: true, expected_benefit: "墙板数据链的部署 SOP；证据归并 c10/g37/g38/n21/p25"}
  decision: verified

- id: f28
  title: SPM 基础设置与日统计链路——Settings 四区 + afe.properties
  type: menu
  V1: {passed: true, reason: "p412-417 四区设置与日统计参数逐项有页面证据"}
  V2: {passed: true, check_mode: walkthrough, input: "日统计能不能 5 分钟取一次", expected: "不能，15 分钟且不可更快（OXE 侧编译周期决定）", observed: "p417 原文 can't be reduced；取数在每刻后 2 分钟（p29）"}
  V3: {passed: true, expected_benefit: "日报对账与性能治理的口径；证据归并 c10/p29/p30"}
  decision: verified

- id: f29
  title: Soft Panel 对象模型——背景 → 视图 → 面板 → 挂件四层与显示 URL
  type: structure
  V1: {passed: true, reason: "p420-447/p457-474 四层模型、挂件全集与 URL 齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "视图定制能用 Chrome 吗", expected: "不能，仅 Firefox", observed: "p421 原文 other web browsers are not allowed（n25）"}
  V3: {passed: true, expected_benefit: "上墙交付的完整对象地图；证据归并 c11/p31/n25-n27"}
  decision: verified

- id: f30
  title: SPM 告警机制——阈值条件、两种动作与告警视图
  type: flow
  V1: {passed: true, reason: "p450-453/p478-479 告警参数与两动作齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "告警想重复发怎么设", expected: "Notification interval 非 0 按周期重复；0 只发一次", observed: "p478 原文明确；对象类型五选（含原文拼写 WaintingQueue，nr-07）"}
  V3: {passed: true, expected_benefit: "阈值运营场景的落地方案；证据归并 c11/p30"}
  decision: verified

- id: f31
  title: CCTA 票据分析器双工具链——Importation 与 Ticket Tracer
  type: flow
  V1: {passed: true, reason: "p480-497 票据类型/双工具/导入与导出全链齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "坐席挂机的结束原因是几", expected: "26（样例码之一，全表在工具文档）", observed: "p488 原文 0/1/26 样例（p33）"}
  V3: {passed: true, expected_benefit: "故障复盘与质量分析的数据抓手；证据归并 c12/p33/g40"}
  decision: verified

- id: f32
  title: 特殊功能菜单路径汇总表——Pilot/PG/中继/前缀四类开关
  type: menu
  V1: {passed: true, reason: "p498-515/p516-530 讲义与 How-To 双侧路径齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "队列满时主叫听什么", expected: "默认 2 号间隔引导音，开 Redirection busy tone on DID 才是忙音", observed: "p500/p521 与 n29 一致"}
  V3: {passed: true, expected_benefit: "交付验收高频开关的路径字典；证据归并 c13/p21/n28/n29"}
  decision: verified

- id: f33
  title: Excel 报表模板体系与定制原理——General/Custom 双工作表链接
  type: structure
  V1: {passed: true, reason: "p531-543 模板清单/定制原理/粒度陷阱齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "½ 小时粒度单表能覆盖全天吗", expected: "不能，只到 16:00，需第二张表", observed: "p542 原文 NO!（n30）"}
  V3: {passed: true, expected_benefit: "客户化日报的施工原理与陷阱；证据归并 c14/n30-n32"}
  decision: verified

- id: f34
  title: CCS Server 内/外部架构与客户端接入切换
  type: structure
  V1: {passed: true, reason: "p555-590 三形态/容量/强制条件/切换流程齐备；本次抽查 source_fulltext 逐格一致"}
  V2: {passed: true, check_mode: walkthrough, input: "外部 Server 连不上 AFE 先查什么", expected: "内部 serv_ccs 进程是否真停", observed: "p575 拒接机制 + p583-585 停进程步骤一致（n33）"}
  V3: {passed: true, expected_benefit: "多监督员客户的集中接入方案；证据归并 c15/p32/n33/n37"}
  decision: verified
```

## 断言级裁决记录

1. **counter-example n37 "p558 29 or 120"**：成立并如实记录。原文 "From a physical limit point of view, 29 or 120 CCs max can be connected to the AFE" 与同页图示（Internal 15 / External 120、14+1 connection）及其他章口径（p557、p567）不符；（推断）"29" 为笔误，规划以 15/120 与 ">9 须上 Server" 为准。详见 needs-review nr-01。
2. **counter-example n13 "p236 统计 Pilot 31650 vs 实验正文 31660"**：成立。p236 Notes 沿用了讲义章示例号 31650（p123），实验实际配置为 31660（p155）；照书操作以现场配置为准，详见 needs-review nr-02。
3. **counter-example n16 关键字命名混用**：成立。讲义定义 LAST_CALLED_ELAPSED_TIME/LAST_CALLED_STATE（p253），脚本范式与 How-To 用 LAST_CALL_ELAPSED_TIME/LAST_CALL_STATE（p254/p264）；以编辑器下拉可选值为准，详见 needs-review nr-03。
4. **principle p10 "21 次"双口径**：成立并并存记录——p214/p245 写"脚本执行/使用 21 次"，p220 写"alb 发 21 次请求（脚本执行 20 次）"；两处均按原文收录，不强行归一。
5. **无 rejected 断言**：p77 ACR 容量十二项、p394 SPM 三限、p186 ISM 手算（Cman 14/14、Copt 31/3、Sub-List1=Agent4/Agent1）、p513-514 中继数学（62→50→15、30%）、p557 接入容量（15/120）等关键数字经本次 source_fulltext 抽查与提取器页码双重核对一致；p364 "Agent2 (32500)" 坐席称号与分机不符一项转 needs-review nr-04。
