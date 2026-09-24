# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f30（主验证对象）；principle p01-p38 / case c01-c17 / counter-example n01-n59 作为各单元的证据素材归并；glossary g01-g62 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 415 页全文提取件 + 提取器页码证据交叉核对

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 29 | f01, f03-f30（f02 除外，全部通过三重验证） |
| reference | 1 | f02（RLAB 实验平台结构与节点访问表——仅作 Boundary 背景，不进能力卡正文） |
| needs_review | 0（单元级） | 断言级 6 项转 needs-review.md（RTR 重试双口径、p404 排版错误、媒体通道表述、TC0000 占位件号、实验凭证纪律、lmsagent 范围辨析） |
| rejected | 0 | 无编造断言；GAS 硬件前置表、RTR 状态阈值、PoD 目录件号、订阅消耗归属等数字口径逐格核对一致 |

verified 明细：f01, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——环境 → SOT 工具 → 三条加载路径 → 两种承载形态 → 云连接 → 订阅许可
  type: framework
  V1: {passed: true, reason: "p22/p133/p352 三处章节锚点句；八段结构与目录页吻合"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE 软件交付按什么顺序推进", expected: "环境→工具→加载→承载→云→订阅的可执行顺序", observed: "八段推进与各 How-To 依赖链（FTR 依赖 swk+连通性）互证，顺序无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免先装云客户端后装基座系统的倒置"}
  decision: verified

- id: f02
  title: RLAB 全虚拟化实验平台——POD 结构与五类节点访问表
  type: structure
  V1: {passed: true, reason: "p1-20 节点表逐台给出（IP/账号/密码）；p3 明示 RLAB ONLY"}
  V2: {passed: true, check_mode: walkthrough, input: "培训环境各节点怎么访问", expected: "五类节点 IP/账号/密码总表", observed: "p10-p19 表与各 How-To 引用值一致（如 SOT .130、GAS .45）"}
  V3: {passed: true, expected_benefit: "仅作实验口径 Boundary 背景：所有 IP/密码为培训值，生产必换"}
  decision: reference

- id: f03
  title: SOT 形态与模式矩阵——ISO/OVA 交付 × Standalone/Hosted × default/Template Factory
  type: structure
  V1: {passed: true, reason: "p22-29 三维矩阵每格有原文；一次一个部署任务（p22 Notes）"}
  V2: {passed: true, check_mode: walkthrough, input: "加载物理 CS 与加载虚机分别用哪种 SOT 形态", expected: "Standalone 主打物理裸机、Hosted 主打虚机", observed: "p24/p25 用途句与 c01/c09/c10 实验对应一致"}
  V3: {passed: true, expected_benefit: "交付前选形态的决策底座；证据归并 p02/n01/n02"}
  decision: verified

- id: f04
  title: Template Factory 降级模式五步流程（低资源机器）
  type: flow
  V1: {passed: true, reason: "p29 五步顺序句 + p155-165 How-To 全步骤"}
  V2: {passed: true, check_mode: walkthrough, input: "低配笔记本能不能建 OVA 模板", expected: "标准 ova + 50GB 盘 + templateFactory 命令绕过", observed: "p164 'Enter Y to bypass resource control' 与 c06 验证点一致"}
  V3: {passed: true, expected_benefit: "无高配服务器时的官方绕过路径；证据归并 p02/n03"}
  decision: verified

- id: f05
  title: SOT Web 界面分区与两种工作模式（Easy/Expert）
  type: menu-path
  V1: {passed: true, reason: "p30-32 四主页面与 Settings 区逐项列出"}
  V2: {passed: true, check_mode: walkthrough, input: "Easy 和 Expert 模式差别是什么", expected: "Easy=向导；Expert=媒体与项目独立管理、媒体先声明", observed: "p31 原文两句直接回答；c03/c04 Expert 操作流印证"}
  V3: {passed: true, expected_benefit: "所有 SOT 操作的界面地图；证据归并 n06"}
  decision: verified

- id: f06
  title: SOT 媒体库三类型与支持格式清单
  type: structure
  V1: {passed: true, reason: "p33 三库与格式清单原文；p86 传输通道与账号"}
  V2: {passed: true, check_mode: walkthrough, input: "补丁 zip 和版本 iso 怎么传给 SOT", expected: "FTP/SFTP(2222) upload 账号上传→Refresh→Declare", observed: "p86/p95 与 c02/c03 步骤一致；通道表述差异见 needs-review nr-03"}
  V3: {passed: true, expected_benefit: "一切加载场景的公共前置动作；证据归并 p38/n01"}
  decision: verified

- id: f07
  title: SOT 版本命名与更新规则（ISO A.B.XXX.000 / zip A.B.XXX.YYY）
  type: flow
  V1: {passed: true, reason: "p47 命名与三规则原文；p197-198 hosted 章同口径"}
  V2: {passed: true, check_mode: walkthrough, input: "SOT 能从 3.1 zip 更新到 3.2 吗", expected: "不能——仅同主版本内可更新，跨主版本禁", observed: "p47 'update will be forbidden' 原文直接回答；n04 同口径"}
  V3: {passed: true, expected_benefit: "SOT 维护与补丁管理的版本判断依据；证据归并 p03/n04"}
  decision: verified

- id: f08
  title: 单版本全加载端到端时序——BOOTP/DHCP→TFTP→Linux RAM→FTP 安装
  type: diagram
  V1: {passed: true, reason: "p52/p56-60 时序与协议分工原文；p56 SOT=DHCP+FTP 虚机定义"}
  V2: {passed: true, check_mode: walkthrough, input: "CS 网络引导后 SOT 交付什么", expected: "IP 配置+引导文件（CS=startup.txt）→TFTP 清单与 Linux RAM→FTP 安装", observed: "p60 分机型引导文件表与 c02 实验现象一致"}
  V3: {passed: true, expected_benefit: "加载失败定位的时序底图；证据归并 n07/g48"}
  decision: verified

- id: f09
  title: CS 启动相位链与可中断/可失效点
  type: diagram
  V1: {passed: true, reason: "p58 六相位原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "已装系统的机器怎么强制走网络引导", expected: "BIOS 相位选设备或 grubboot ETHER（GRUB 相位失效）", observed: "p57-58/p89 与 c02 步骤 8 一致；RUNTEL 手动起话音应用同页"}
  V3: {passed: true, expected_benefit: "'SOT 一直等目标机'类卡点的一线排查图；证据归并 n07/g28"}
  decision: verified

- id: f10
  title: 硬盘双分区目录结构图（active/inactive/公共区）
  type: diagram
  V1: {passed: true, reason: "p54-55 目录挂链逐条原文"}
  V2: {passed: true, check_mode: walkthrough, input: "inactive 分区在哪些目录", expected: "/root2_d、/usr5(/DHS3bin2)、/usr6(/DHS3data2)、/var2", observed: "p55 原文与 swinst 8-2 的 0/1 分区查询语义吻合"}
  V3: {passed: true, expected_benefit: "多版本/复制/切换机制的结构依据；证据归并 g06"}
  decision: verified

- id: f11
  title: 多版本加载两分支流程——复制+补丁 vs 完整加载+数据复制
  type: flow
  V1: {passed: true, reason: "p71-77 两分支判据与参数原文（Duplicate OXE/Linux Data、Switch partition/time/back）"}
  V2: {passed: true, check_mode: walkthrough, input: "同基础版本与跨 Linux 版本各走哪条分支", expected: "同版本=复制+补丁；跨 Linux=完整加载+数据复制", observed: "p73 两例（N4.205.19→36a / N3.521.12→36a）直接回答"}
  V3: {passed: true, expected_benefit: "升级不停机的核心流程；证据归并 p07/g05/c03/n11"}
  decision: verified

- id: f12
  title: swinst 菜单树全景（Main/Expert/Cloning/Identity/Remote download）
  type: menu-path
  V1: {passed: true, reason: "p98-99/p114/p117-130 多处菜单原文互证"}
  V2: {passed: true, check_mode: walkthrough, input: "手工复制分区与切换在哪个菜单", expected: "2-3-2（Partitions duplication）与 2-3-3（Switch on inactive）", observed: "p98 原文路径与 c03 附录、c04 步骤 4 逐级吻合"}
  V3: {passed: true, expected_benefit: "全书 OXE 侧 CLI 操作的菜单地图；证据归并 g21"}
  decision: verified

- id: f13
  title: 补丁安装双场景操作流——active 分区（停话音）与 inactive 分区（先复制）
  type: flow
  V1: {passed: true, reason: "p100-110 双场景 Warning 与步骤原文（p104 静态停话音、p106 Duplicate all）"}
  V2: {passed: true, check_mode: walkthrough, input: "给 active 分区装静态补丁会发生什么", expected: "停话音+系统自动重启，须排维护窗口", observed: "p104 Warning 原文直接回答；c04 场景 A 印证（实验 0→19→36）"}
  V3: {passed: true, expected_benefit: "日常维护最高频动作的完整操作与窗口口径；证据归并 p06/n09/n15"}
  decision: verified

- id: f14
  title: Easy Installation 分发器流程与文件落点图（/tmpd → Rload）
  type: flow
  V1: {passed: true, reason: "p111-130 流程/落点/清理原文（p113 传 /tmpd、p129 Rload 三目录）"}
  V2: {passed: true, check_mode: walkthrough, input: "分发器加载后磁盘会越占越满吗", expected: "Rload 解包物不自动删，须 swinst 9-7 清理；/tmpd 源文件自动删", observed: "p129-130 原文与 n16 一致，方向易错点成立"}
  V3: {passed: true, expected_benefit: "客户现场不让架 SOT 时的唯一替代路径；证据归并 n14/n15/n16/c05"}
  decision: verified

- id: f15
  title: OXE-V 虚拟化技术矩阵与许可控制路径图
  type: structure
  V1: {passed: true, reason: "p133-136 平台版本矩阵与许可规则原文（含脚注 gen1/gen2）"}
  V2: {passed: true, check_mode: walkthrough, input: "客户定了 Hyper-V 还能报 FlexLM+加密狗吗", expected: "不能——无 USB 重定向且无 FlexLM 虚机，必须 Cloud Connect", observed: "p136 原文直接回答；n17 同口径"}
  V3: {passed: true, expected_benefit: "全书代价最高的架构决策依据；证据归并 p10/p11/n17/n18"}
  decision: verified

- id: f16
  title: OXE-V 六种拓扑图组与 PCS 接管行为
  type: diagram
  V1: {passed: true, reason: "p142-148 六拓扑图组 + p147 PCS 软/硬复位原文"}
  V2: {passed: true, check_mode: walkthrough, input: "PCS 接管后虚机会重启吗", expected: "CS→PCS 软复位（释放话音、虚机不重启）；PCS→CS 硬复位（重启）", observed: "p147 原文两句直接回答；n39/g11 范围辨析一致"}
  V3: {passed: true, expected_benefit: "OXE-V 方案沟通与冗余预期管理素材"}
  decision: verified

- id: f17
  title: OMS 软媒体网关定位与能力结构
  type: structure
  V1: {passed: true, reason: "p138-140 定义/能力/许可三段原文（120 通道、240 台、Lock 384/385）"}
  V2: {passed: true, check_mode: walkthrough, input: "OMS 许可怎么算、要不要停机装", expected: "Lock 384 台数 + Lock 385 通道总数，均可不停机安装", observed: "p140 原文直接回答；p09 逐格一致"}
  V3: {passed: true, expected_benefit: "虚化交付媒体容量规划依据；证据归并 p09/g10/n19"}
  decision: verified

- id: f18
  title: GAS 架构与部署模式对比图（ALE 平台/虚拟化/AS/GAS 四象限）
  type: diagram
  V1: {passed: true, reason: "p221-224 四形态与 GAS 组件栈原文"}
  V2: {passed: true, check_mode: walkthrough, input: "GAS 和传统 Appliance Server 差在哪", expected: "GAS=BP 自备硬件+ALE 软件包（Rocky+KVM），解决 AS 硬件寿命短问题", observed: "p221 动机句与 p228 legacy 退出（n21）互证"}
  V3: {passed: true, expected_benefit: "一体机形态交付的结构认知底座；证据归并 p12/n19/n20/g12"}
  decision: verified

- id: f19
  title: GAS 许可控制两拓扑（ALU-ID 本地 vs CC-PRODUCT-ID 云端）
  type: diagram
  V1: {passed: true, reason: "p231-234 两拓扑原文（各自 ALU-ID vs 共用 CC-PRODUCT-ID）"}
  V2: {passed: true, check_mode: walkthrough, input: "GAS 冗余时许可标识怎么分布", expected: "ALU-ID 模式各 CS 独立；CC 模式两 CS 共用同一 CC-PRODUCT-ID", observed: "p231/p233 冗余句逐字一致；p11 互斥规则兜底"}
  V3: {passed: true, expected_benefit: "GAS 开局许可方案二选一的判据；证据归并 p36/n27"}
  decision: verified

- id: f20
  title: Cloud Connect 连接架构图——XMPP over WSS 443 常驻 + SOCKS5 80 按需
  type: diagram
  V1: {passed: true, reason: "p286-290 架构/端口/安全原文；p340 服务总览图"}
  V2: {passed: true, check_mode: walkthrough, input: "入云要客户防火墙改什么", expected: "出站 443(XMPP/WSS)+80(SOCKS5)+53(DNS) 至 connect2.opentouch.com，OXE 主动发起", observed: "p290 清单与 p17/n36 一致；c14 checkCloudConfig 实测印证"}
  V3: {passed: true, expected_benefit: "零改动入云的设计原则与网络前提清单；证据归并 p17/g14/g46/g47"}
  decision: verified

- id: f21
  title: FTR 原理时序——订单链 → CC-SUITE-ID 激活账户 → 永久凭证
  type: diagram
  V1: {passed: true, reason: "p291-295 ID 语法与十步时序原文"}
  V2: {passed: true, check_mode: walkthrough, input: "FTR 换来的是什么", expected: "以激活账户换永久凭证（CC-Product-ID+密码），隐藏存库并克隆 twin", observed: "p293 目标句 + p297 冗余句互证；p18/p19 一致"}
  V3: {passed: true, expected_benefit: "一切云服务的门禁认知；证据归并 p18/p19/n29/n32/g15"}
  decision: verified

- id: f22
  title: FTR with PIN 恢复流程（helpdesk → 6 位 PIN → 重注册）
  type: flow
  V1: {passed: true, reason: "p298-301/p330 触发条件、PIN 属性、进程前提原文"}
  V2: {passed: true, check_mode: walkthrough, input: "RTR panic 后怎么恢复", expected: "helpdesk 申请 6 位 PIN（5 天有效）→ CCTool 重做 FTR → 在线重置全部云配置", observed: "p299-300/p330 原文逐条回答；n30 四边界齐备"}
  V3: {passed: true, expected_benefit: "panic 唯一出路的标准流程；证据归并 p20/n30/n31/g16"}
  decision: verified

- id: f23
  title: RTR 状态机——Qualifying Period 数轴与 Fleet Dashboard 六状态
  type: structure
  V1: {passed: true, reason: "p303-308 数值律（30 天起/OK +0.5/NOK -1）与状态映射原文"}
  V2: {passed: true, check_mode: walkthrough, input: "Fleet Dashboard 显示 Soon Blocked 意味着什么", expected: "剩余资格期 9-1 天且超 24h 无连接，每日收邮件，需立即恢复连通", observed: "p306 阈值原文直接回答；p21/p23 逐格一致"}
  V3: {passed: true, expected_benefit: "dongle-less 许可运维的状态判读表；重试双口径差异转 nr-01；证据归并 p21/p22/p23/n31/n35"}
  decision: verified

- id: f24
  title: Fleet Dashboard 服务全景与六缩写体系（FTR/RTR/DC/POD/DOD/SU）
  type: structure
  V1: {passed: true, reason: "p310/p338-348 五服务与缩写表原文"}
  V2: {passed: true, check_mode: walkthrough, input: "远程控制台能开着跑长脚本吗", expected: "不能——单会话、1 分钟无操作断开、全程 shell.log 审计", observed: "p343 原文直接回答；n37/n38 边界齐备"}
  V3: {passed: true, expected_benefit: "云端远程运维的产品化边界认知；证据归并 p26/n37/n38/g19"}
  decision: verified

- id: f25
  title: CCTool 菜单结构与 CC 进程/日志布局
  type: menu-path
  V1: {passed: true, reason: "p312/p328-337 四菜单与进程/日志路径原文"}
  V2: {passed: true, check_mode: walkthrough, input: "FTR 失败先看哪两个入口", expected: "/tmpd/Cloud_cnx/logs 的 ccprocess.log + CCTool 1 状态页", observed: "p329 Tips 原文直接回答；p24/p25/n33 一致"}
  V3: {passed: true, expected_benefit: "云连接排障的工具抓手地图；证据归并 p24/p25/n33/g20"}
  decision: verified

- id: f26
  title: OPEX/PoD 总体架构图——LMS/lmsagent 与周边系统
  type: diagram
  V1: {passed: true, reason: "p351-353 架构/定义/lmsagent 原文"}
  V2: {passed: true, check_mode: walkthrough, input: "备机上 lmsagent 跑不跑", expected: "跑（主/备/PCS 全部 CS），备机只读；与'云服务不跑备机/PCS'是两回事", observed: "p353 原文直接回答；n39 辨析成立"}
  V3: {passed: true, expected_benefit: "OPEX 冗余排障的范围判据；证据归并 p31 注/n39/g22/g23"}
  decision: verified

- id: f27
  title: 三种订阅消耗类型图——Unitary / On activation / By threshold
  type: diagram
  V1: {passed: true, reason: "p367-369 三类定义与适用清单原文"}
  V2: {passed: true, check_mode: walkthrough, input: "酒店场景 Room 和 Voice Enterprise 怎么耗许可", expected: "两者都是 On activation——开 OPEX activation 才耗、停用腾挪", observed: "p368 原文限定 Voice Enterprise 与 Room；p30/p31 映射一致"}
  V3: {passed: true, expected_benefit: "建用户前先对消耗规则的业务映射底表；证据归并 p30/p31/n46/g25"}
  decision: verified

- id: f28
  title: OXE-LMS 同步决策流程图（4 小时对账 → panic 判定树）
  type: flow
  V1: {passed: true, reason: "p371-373 运行期/启动期两决策树原文（652/654、30 天）"}
  V2: {passed: true, check_mode: walkthrough, input: "LMS 断了 OXE 重启还能起业务吗", expected: "能——按本地旧消耗值启动，但要许可的管理动作被拒", observed: "p373 原文直接回答；p32/n48 一致"}
  V3: {passed: true, expected_benefit: "OPEX 运维最核心的对账与降级认知；证据归并 p32/p33/n47/n48/n49"}
  decision: verified

- id: f29
  title: C2P 转换五步流程与范围边界
  type: flow
  V1: {passed: true, reason: "p376-378 五步/排除清单/件号规则原文"}
  V2: {passed: true, check_mode: walkthrough, input: "C2P 下单后还能调数量吗", expected: "不能——下单即定局，调整必须发生在购物车前", observed: "p376 'Transformation is definitive once ordered' 原文；n51 一致"}
  V3: {passed: true, expected_benefit: "存量转 OPEX 的商务流程与红线；证据归并 p35/n51/n52/g24"}
  decision: verified

- id: f30
  title: MyPortal PoD 许可下载路径与项目状态判据
  type: menu-path
  V1: {passed: true, reason: "p381-385 路径与 Active 判据原文"}
  V2: {passed: true, check_mode: walkthrough, input: "MyPortal 里项目显示 Pending 能下载许可吗", expected: "不能——必须 Active；Pending=项目未激活（交付问题），先推商务链路", observed: "p384-385 原文直接回答；n53 一致"}
  V3: {passed: true, expected_benefit: "OPEX 交付起点与卡单分流依据；证据归并 n53/c16"}
  decision: verified
```

## 断言级裁决记录

1. **principle 提取器"RTR 重试双口径"**：成立。p308（讲义）写"4 小时窗口内每 10 分钟重试、4 小时后仍不通才减 1 天"；p332（How-To Notes）写"当天不再重试直到次日每日请求，出问题时减 1 天"。两处描述不一致，不强行统一——监控按保守口径（当日即可能扣减）设计，详见 needs-review nr-01。
2. **counter-example 提取器"p404 排版错误"**：成立。p404 Voice Agent(CCD) 计数示例 "13 | 2/2 | 18" 下方的解释文字误用了 5/5/25，属复制粘贴级编辑错误；判据本身以"lms/oxe 两列消耗一致"为准（p397 原文），示例数值不照抄。详见 nr-02。
3. **"SOT 媒体传输通道两章表述差异"**：成立并如实记录。p86（Standalone 章）明确"FTP or SFTP (port 2222), upload 账号"；hosted/ESXi 各章仅写"FTP"。功能等价（同为向 SOT 传媒体），表述粒度不一。详见 nr-03。
4. **"GAS 迁移文档件号为占位编号"**：成立。p230 引用 "TC0000_GAS_migration_FR_ed04.docx"，TC0000 为未定编号占位（原文如此），转述时保留并标注。详见 nr-04。
5. **实验凭证纪律**：全书正文遍布 Superuser2580*、letacla/letacla1、rainbow/Rainbow123 等培训口令与 192.168.1.x 网段——全部标注"实验口径"，只进 Boundary 段与 book/overview 环境区，不进能力卡操作正文。详见 nr-05。
6. **"lmsagent 范围与云服务范围"辨析**：非矛盾，但两规则并存极易误读——CC 云服务（FTR/RTR）不跑备机与 PCS（p297），lmsagent 跑全部 CS 且备机只读（p353）。已按双规则分别入册（f21/f26），能力卡引用时成对出现。详见 nr-06。
7. **无 rejected 断言**：GAS 硬件前置表（p226 四行逐格）、RTR 状态阈值（29-28/27-10/9-1/0）、PoD 目录 24 项与件号、订阅消耗归属、补丁累积规则、swinst/CCTool 菜单树等关键数字与结构与原文逐格一致；p22（一次一个部署）、p46/p196（网卡一致性）等 Warning 无一漏记。
