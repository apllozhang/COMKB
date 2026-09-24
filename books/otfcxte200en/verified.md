# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f33（主验证对象）；principle p01-p43 / case c01-c08 / counter-example n01-n32 作为各单元的证据素材归并；glossary g01-g57 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 233 页全文通读 + 提取器页码证据交叉核对 + 关键数值逐格 grep 复核

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 32 | f01-f33 中除 f04 外全部（明细见下表） |
| reference | 1 | f04（收发示意三张图，与 p8-10 讲义矩阵信息重复，作 f03 的背景佐证） |
| needs_review | 0（单元级） | 断言级 4 项转 needs-review.md（首用户邮箱不一致、Outlook 2022 笔误、缩写全称推断、停止命令行笔误） |
| rejected | 0 | 无编造断言；15000/30、QOS 0/0/240、5360/25/389、2 通道/100 用户/10 站点、20MB/15 天逐格 grep 复核一致 |

verified 明细：f01, f02, f03, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——认知地基 → 安装闭环 → 管理面 → 两大外部集成 → 运维纵深
  type: framework
  V1: {passed: true, reason: "p3-233 章节排布完整；p44 Lesson summary 给出四步交付顺序"}
  V2: {passed: true, check_mode: walkthrough, input: "新项目按什么顺序交付 OTFC", expected: "给出可执行的阶段顺序", observed: "概览→概念→架构→安装→管理→集成→运维十段与 p46 安装四步主线互证，顺序无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免先配 Profile 后装服务器的倒置"}
  decision: verified

- id: f02
  title: OTFC 能力全景——定位/传输/合规三张清单
  type: framework
  V1: {passed: true, reason: "p4-12 基础能力/传输安全/可服务性三段完整"}
  V2: {passed: true, check_mode: walkthrough, input: "向客户解释 OTFC 的合规卖点", expected: "GDPR/HIPAA/FERPA/SOX 语境 + 零保留 + 审计日志", observed: "p6 原文逐条对应；细节边界见 n32（TLS 未展开）"}
  V3: {passed: true, expected_benefit: "售前选型与方案沟通的素材底座；证据归并 g01/n03"}
  decision: verified

- id: f03
  title: 发送/接收入口矩阵与入局路由四法
  type: framework
  V1: {passed: true, reason: "p8-10 四类发送入口与四类接收去向逐条列出；p9 路由四法原文"}
  V2: {passed: true, check_mode: walkthrough, input: "用户都能从哪里发传真、收到哪去", expected: "邮件/Web/虚拟打印机/SendFAX 与邮箱/Web/打印机/文件夹", observed: "p8/p9 原文支持；DNIS/CSID/ANI/DTMF 四法在 p31 高级路由章得到展开"}
  V3: {passed: true, expected_benefit: "方案入口设计与需求评审的核对矩阵；证据归并 p03/g49-g51"}
  decision: verified

- id: f05
  title: 组件流程链——入局路由图 + 外发/内收流水线
  type: framework
  V1: {passed: true, reason: "p19 路由图与 p26-27 外发七步/内收四步原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "传真从提交到入库经过哪些组件", expected: "Gateway→FaxManager→Rasterizer→FaxDriver→SMTP Gateway/FaxArchive 闭环", observed: "p26/p27 两链逐组件一致；'Gateway 取决于提交方客户端'的口径明确"}
  V3: {passed: true, expected_benefit: "排障分段（转换/发送/通知/归档）的概念依据；证据归并 g19/p05"}
  decision: verified

- id: f06
  title: System/Site/User/Profile 概念模型与属性联动
  type: framework
  V1: {passed: true, reason: "p22-24 四级定义逐条原文；'One fax belongs to one and only one site' 单处明示"}
  V2: {passed: true, check_mode: walkthrough, input: "多部门客户怎么切分租户", expected: "按 Site 切、用户挂 Site+Profile、身份是 SMTP 地址", observed: "p22-24 原文支持；n18 补充外部用户必须被 Lookup 归类才能用"}
  V3: {passed: true, expected_benefit: "全书配置界面的组织轴（Sites ➤ Site ➤ … 全按此展开）；证据归并 g02-g06"}
  decision: verified

- id: f07
  title: Queue & History 三视图结构（用户看自己、管理员看全部）
  type: framework
  V1: {passed: true, reason: "p25 三视图与状态清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "用户问传真卡住了怎么解释", expected: "按外发队列六状态对号（Preprocessing/Delayed/Ready to Send/Sending/Waiting/Sent）", observed: "p04 状态口径逐格一致；Sent/Failed 与 Received/Failed to receive 两历史态齐备"}
  V3: {passed: true, expected_benefit: "用户沟通与排障分流的第一入口；证据归并 p04/g10-g11"}
  decision: verified

- id: f08
  title: 全局架构生态图——OTFC 与 OXE/邮件/客户端的协议关系
  type: framework
  V1: {passed: true, reason: "p32-34 生态图协议清单完整（T.30/SIP/T.37/T.38/G711/CSGD/SMTP/XML/HTTP(S)）"}
  V2: {passed: true, check_mode: walkthrough, input: "传真流量和邮件流量走一条路吗", expected: "分两路：话路 SIP/T.38 经 OXE，邮件 SMTP 经邮件服务器", observed: "p34 图与 p157-160 SMTP 拓扑互证；CSGD 缩写未展开（如实记录）"}
  V3: {passed: true, expected_benefit: "架构沟通与防火墙规划的底图；证据归并 g27/g39-g46"}
  decision: verified

- id: f09
  title: 多网关多站点拓扑与双 SIP 网关号码分段路由
  type: framework
  V1: {passed: true, reason: "p35-37 三张拓扑图与示例号段原文"}
  V2: {passed: true, check_mode: walkthrough, input: "多台 OXE 怎么接一台 OTFC", expected: "Fax Center 配多 SIP 网关，OXE 侧建 SIP private trunk，按号码段分流", observed: "p36 GW1/GW2 号段示例（1200-1500/3300-3800，实验口径）；p37 两种出呼路由场景齐备"}
  V3: {passed: true, expected_benefit: "多站点多 PBX 交付的拓扑选型依据；证据归并 g27/n29"}
  decision: verified

- id: f10
  title: 部署形态与支持软件矩阵结构
  type: framework
  V1: {passed: true, reason: "p32/p38-41 四块矩阵（OS/虚拟化/软件/客户端）原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户环境 Server 2019 + ESXi 7 + Exchange 2016 能不能装", expected: "三者在支持矩阵内", observed: "p05/p06/p07 逐格核对一致；Outlook 2022 笔误与 p38/p42 空指针已如实标注（nr-02/nr-05）"}
  V3: {passed: true, expected_benefit: "勘测阶段的快速核对表；全部版本以 Features List 为准的边界诚实"}
  decision: verified

- id: f11
  title: 安装四步主线——准备服务器 → 软件安装 → FTW → 客户端安装/初始设置
  type: framework
  V1: {passed: true, reason: "p46 四步主线原文；p45 实验生态图全套锚点"}
  V2: {passed: true, check_mode: walkthrough, input: "按四步走一遍裸机交付", expected: "每步有 How-To 支撑", observed: "步1→c01，步2→c02，步3→c03，步4→c05，全覆盖无断链"}
  V3: {passed: true, expected_benefit: "从裸机到能收发的交付主线骨架；证据归并 c01-c03/p08"}
  decision: verified

- id: f12
  title: 服务器准备检查结构——网络/DNS 正反解、防火墙、IIS 角色服务、服务账号
  type: framework
  V1: {passed: true, reason: "p47-48 两组清单原文逐条"}
  V2: {passed: true, check_mode: walkthrough, input: "安装前服务器要核什么", expected: "DNS 正反解 + IIS 四角色服务 + 服务账号六权限", observed: "p09/p10/p11 三条目与原文一致；关防火墙为实验口径（n01）"}
  V3: {passed: true, expected_benefit: "安装失败第一大来源的前置拦截；证据归并 p09/p10/p11/c01/n01"}
  decision: verified

- id: f13
  title: 软件安装流程——Setup.exe 向导到 FTW 启动 + 禁用 MS SMTP
  type: framework
  V1: {passed: true, reason: "p49 九步要点 + p59-65 How-To 逐屏"}
  V2: {passed: true, check_mode: walkthrough, input: "装完传真后邮件入口收不到任务", expected: "先查 25 端口被 MS SMTP 占用，先停禁再启 XMSMTPGateway", observed: "p49/p65/p183 三处口径一致（n02）；服务名两种写法见 nr-04"}
  V3: {passed: true, expected_benefit: "安装施工的标准序列与最大坑位；证据归并 c02/p12/p15/n02/n05"}
  decision: verified

- id: f14
  title: First Time Setup Wizard 十二项动作结构
  type: framework
  V1: {passed: true, reason: "p67 十二项逐条原文；p16 清单逐格一致"}
  V2: {passed: true, check_mode: walkthrough, input: "不走向导手工配要配哪些", expected: "对照 12 项逐条手工配置或跑 FirstTimeSetup.exe", observed: "p67/p17 原文支持；QOS 0/0/240 与 CSID=站点名为向导固定动作"}
  V3: {passed: true, expected_benefit: "最小可用系统的构成定义（12 项即验收清单）；证据归并 p16/p17/c03/g14"}
  decision: verified

- id: f15
  title: 管理双入口与认证体系——MMC Snap-in + Web admin，System/Site 两级管理员
  type: framework
  V1: {passed: true, reason: "p74-77 双入口路径与两级管理员原文"}
  V2: {passed: true, check_mode: walkthrough, input: "客户网管只给浏览器权限怎么管系统", expected: "Web 管理页 http(s)://<服务器>/faxadmin 全功能", observed: "p74/p14 口径一致；CSV 导入导出仅 Webadmin（n09）反证 Web 端功能覆盖更全"}
  V3: {passed: true, expected_benefit: "管理权责与入口规划依据；证据归并 p14/p22/g33-g34"}
  decision: verified

- id: f16
  title: Web Client 界面分区与访问口径
  type: framework
  V1: {passed: true, reason: "p79-81 六区界面与访问 URL 原文"}
  V2: {passed: true, check_mode: walkthrough, input: "用户免安装用什么发传真", expected: "浏览器访问 /fax，六区界面", observed: "p80/p14 口径一致；508/e-inclusion 合规口径齐备（p18）"}
  V3: {passed: true, expected_benefit: "用户侧入口的最低门槛方案；证据归并 p18/g35"}
  decision: verified

- id: f17
  title: Windows 客户端四件套与部署方式
  type: framework
  V1: {passed: true, reason: "p83-90 四件套功能与部署口径原文"}
  V2: {passed: true, check_mode: walkthrough, input: "500 台工作站怎么批量装客户端", expected: "静默安装 + GPO，或直接发 ClientRedistribution 精简包", observed: "p19 三条规则与原文一致；SendFAX Outlook 模式依赖 FAX 地址空间（n13）"}
  V3: {passed: true, expected_benefit: "客户端批量交付方案依据；证据归并 p19/g29-g31/c05/n11/n13"}
  decision: verified

- id: f18
  title: 封面页定制五步流程（Editor → 下载 → 另存 → 导入 → Profile 关联）
  type: framework
  V1: {passed: true, reason: "p91-96 五步闭环原文连贯"}
  V2: {passed: true, check_mode: walkthrough, input: "企业自有封页怎么生效", expected: "编辑 .cse、Web 管理导入、挂 Profile", observed: "p93/p95-96 路径完整；.cse 专有格式、一个 Profile 可挂多张封页口径明确"}
  V3: {passed: true, expected_benefit: "品牌化交付的标准动作；证据归并 g20/g32/n05"}
  decision: verified

- id: f19
  title: 用户双源模型与建户路径（Internal/AD 共存 + CSV）
  type: framework
  V1: {passed: true, reason: "p100-105 双源定义与建户/CSV 路径原文"}
  V2: {passed: true, check_mode: walkthrough, input: "客户有 AD 还要建内部用户吗", expected: "两源可共存，按群体混用", observed: "p100 'can co-exist' 原文明示（n08 误解纠正）；CSV 仅 Webadmin（p21/n09）"}
  V3: {passed: true, expected_benefit: "用户开通方案选型与批量路径；证据归并 p20/p21/g04/n08/n09"}
  decision: verified

- id: f20
  title: 管理员两级结构与账号生命周期（建 System/Site 管理员、改密、登录界面区分）
  type: framework
  V1: {passed: true, reason: "p106-113 两级定义与三组操作步骤"}
  V2: {passed: true, check_mode: walkthrough, input: "管理员密码丢了怎么办", expected: "提前建备份管理员对冲", observed: "p110 'recommended to create a backup administrator' 原文；n10 锁死风险齐备"}
  V3: {passed: true, expected_benefit: "权责切分与防锁死交付检查项；证据归并 p22/g21-g22/n10"}
  decision: verified

- id: f21
  title: Profile 属性块与五种关联机制（限制组/呼号限制/邮件通知/电话簿/封页）
  type: framework
  V1: {passed: true, reason: "p118-129 六块属性与五种挂接原文"}
  V2: {passed: true, check_mode: walkthrough, input: "禁发国际传真的策略怎么做", expected: "Restriction group 挂 Profile（National only）", observed: "p121 原文支持；出方向挂 Profile 与入方向站点级 Calling Number Restriction 方向相反口径清楚"}
  V3: {passed: true, expected_benefit: "合规与成本控制策略的核心机制；证据归并 p23/g05/g15-g16/n12"}
  decision: verified

- id: f22
  title: 电话簿体系与 LDAP 访问链（Public/Personal、CSV、属性映射）
  type: framework
  V1: {passed: true, reason: "p134-139 两类电话簿与 LDAP 三处配置原文"}
  V2: {passed: true, check_mode: walkthrough, input: "企业电话簿怎么让用户经 Outlook 式目录访问", expected: "Fax Archive 属性勾 Enable LDAP Access + 站点认证 + 属性映射", observed: "p42 三处开关与原文一致；私人电话本不在系统备份内（n22）"}
  V3: {passed: true, expected_benefit: "联系人库规划与目录对接；证据归并 p42/g48/n22"}
  decision: verified

- id: f23
  title: OTFC 侧 SIP 配置与 OXE 声明路径（含空间冗余双呼叫服务器）
  type: menu-path
  V1: {passed: true, reason: "p141-146 SIP 配置/声明/dial plan/Peer List 原文"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE 空间冗余时 OTFC 侧怎么配", expected: "Peer List 声明 2 台呼叫服务器 + Dial Plan 排优先级", observed: "p145-146 原文支持；UDP 5360 与单 PBX (*) 路由口径明确（p29）"}
  V3: {passed: true, expected_benefit: "话路互通的 OTFC 半边施工与冗余设计；证据归并 p29/g40/n32"}
  decision: verified

- id: f24
  title: OXE 侧 SIP 网关 MGR 菜单七步序列
  type: menu-path
  V1: {passed: true, reason: "p151-155 How-To 七步菜单截图与文字"}
  V2: {passed: true, check_mode: walkthrough, input: "照七步做完话路一定通吗", expected: "不一定——参数细节在 TC3048", observed: "p141/p147 官方明示 refer to TC3048（n29 边界诚实）；mtcl 默认账号、#31600-31699 号段实验口径"}
  V3: {passed: true, expected_benefit: "OXE 半边的施工骨架与书外边界；证据归并 c06/p30/n06/n29"}
  decision: verified

- id: f25
  title: OXE 侧传真故障抓包三法（CHtrace/motortrace/tcpdump→Wireshark）
  type: flow
  V1: {passed: true, reason: "p148-150 三组命令逐字原文"}
  V2: {passed: true, check_mode: walkthrough, input: "传真时通时断怎么取证", expected: "OXE 侧抓 CHtrace/SIP trace/网络包三选组合", observed: "p31 命令逐格一致；p148 停止命令行混入 'traced' 字样（killall mtracer 本身正确，nr-06）"}
  V3: {passed: true, expected_benefit: "互通排障的硬技能抓手；证据归并 p31/g40"}
  decision: verified

- id: f26
  title: SMTP 网关收发事务与中继拓扑结构
  type: structure
  V1: {passed: true, reason: "p157-163 模块职责/部署拓扑/寻址原文"}
  V2: {passed: true, check_mode: walkthrough, input: "邮件直连网关行不行", expected: "可行但官方强烈建议前置真实邮件服务器", observed: "p157/p160 原文支持；n30 四类缺失能力齐备"}
  V3: {passed: true, expected_benefit: "邮件拓扑设计与告警回收（NDR）依据；证据归并 p32/g47/n30"}
  decision: verified

- id: f27
  title: Exchange 'FAX' 地址空间集成与连接器流程
  type: flow
  V1: {passed: true, reason: "p164-170 四段流程与命令逐字原文"}
  V2: {passed: true, check_mode: walkthrough, input: "Exchange 用户怎么发传真", expected: "建 fax:* Send Connector 指向网关智能主机", observed: "p33 命令与示例逐格一致；通知被拦调 Receive Connector（n16）、SMTP connector 为许可特性（n14）"}
  V3: {passed: true, expected_benefit: "主入口场景的施工与排障全链；证据归并 p33/c07/g13/g25/g37/n13-n16"}
  decision: verified

- id: f28
  title: 服务架构三层模型与 Stateful/Stateless 分类
  type: structure
  V1: {passed: true, reason: "p177-185 模块/服务/组件与 9 服务分类原文"}
  V2: {passed: true, check_mode: walkthrough, input: "哪几个服务挂了会丢数据", expected: "有状态 5 个（复制）持有配置/事务/历史", observed: "p179 分类清单逐格一致；XMFaultTolerance 仅组件介绍无部署教学（n28 诚实边界）"}
  V3: {passed: true, expected_benefit: "运维动作（复制/负载均衡）的理论依据；证据归并 g36/n28"}
  decision: verified

- id: f29
  title: 服务管理三通道与日志体系
  type: structure
  V1: {passed: true, reason: "p186-191 状态/启停/命令行与日志原文"}
  V2: {passed: true, check_mode: walkthrough, input: "改完配置怎么整体重启", expected: "xmsc -ra（或 -oa/-aa）", observed: "p34 命令与路径逐格一致；日志 20MB/15 天、Trace 目录、SIP 日志激活入口齐备（p35）"}
  V3: {passed: true, expected_benefit: "售后日常运维的标准动作集；证据归并 p34/p35/g52-g53/n31"}
  decision: verified

- id: f30
  title: 目录集成机制链——LDAP 声明 → Lookup 表 → NT Account 免密 → IIS 自动登录
  type: flow
  V1: {passed: true, reason: "p194-204 四段机制原文连贯"}
  V2: {passed: true, check_mode: walkthrough, input: "AD 用户查得到但用不了传真", expected: "先查 Site/Profile Lookup 规则命中，别只盯目录连接", observed: "p198 原文明示无 Site+Profile 即拒用（n18）；LDAP 参数/过滤器/IIS 开关逐格一致（p24/p25/n19）"}
  V3: {passed: true, expected_benefit: "大客户目录场景的完整施工与排障链；证据归并 p24/p25/g06-g07/g17-g18/n18/n19/n31"}
  decision: verified

- id: f31
  title: 入局路由三层与号码规整机制（Incoming Routing/DTMF/Modification/Accounting）
  type: structure
  V1: {passed: true, reason: "p205-213 四机制原文"}
  V2: {passed: true, check_mode: walkthrough, input: "国际格式联系人发传真多拨了 33 怎么办", expected: "Modification Table 把 33 前缀换 00", observed: "p28 规则与示例逐格一致；Default 规则恒最后（n20）、$did:?????$ 匹配、DTMF P 语法、8770 计费默认映射传真号齐备（p26-p28/p40）"}
  V3: {passed: true, expected_benefit: "复杂编号场景的四个调节旋钮；证据归并 p03/p26-p28/p40/p41/g49-g51/n20"}
  decision: verified

- id: f32
  title: 备份/恢复/升级流程骨架（三数据域、五步升级法）
  type: flow
  V1: {passed: true, reason: "p216-222 备份三域/恢复四前提/五步法原文"}
  V2: {passed: true, check_mode: walkthrough, input: "备份脚本能不能 taskkill 强杀服务", expected: "不能——备份要求停止不可 kill，恢复才可 kill", observed: "p37/n21 语义差原文逐字；数据库不在升级自动备份内（n23）"}
  V3: {passed: true, expected_benefit: "灾难底线动作与升级窗口的执行顺序；证据归并 p36-p38/c08/g19/g36/g57/n21-n23"}
  decision: verified

- id: f33
  title: 报表与监控体系（31 报表 + BIRT + SNMP V2 + 删除策略）
  type: structure
  V1: {passed: true, reason: "p223-229 删除策略/报表/监控原文"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要求零保留合规怎么配", expected: "传真记录与传真文档分开/一起删", observed: "p43 原文支持；31 报表、BIRT 装在 3rd\\birt、SNMP V2 trap 清单逐格一致（p39/g38/g56）"}
  V3: {passed: true, expected_benefit: "合规保留策略与主动运维的抓手；证据归并 p39/p43/g19/g38/g56"}
  decision: verified
```

## 断言级裁决记录

1. **case 提取器"首用户邮箱两页不一致"**：成立。p50 讲义页写 barkley@company.com、p70 实验页写 baker@company.com（原文 grep 双向确认，两账号在 p45 生态图中均真实存在：barkley=31600 用户、baker=传真管理员）。实践口径按实验页 baker 执行；详见 needs-review nr-01。
2. **principle 提取器"Outlook 2022 为原文笔误"**：成立。p41 原文 "Microsoft Outlook 2022 / 2019 / 2016"，桌面 Office 无 2022 版本（版本常识推断，已标注）；引用矩阵时以 Features List 为准（nr-02）。
3. **glossary 提取器"缩写全称未展开的如实记录"**：成立。DNIS/CSID/ANI/DDI/ARS/MLE/SMB/CSGD/MMC/BIRT/UTL 等书内未给全称，候选中的括注全部保留"（推断）"标注，不升格为原文事实（nr-03）。
4. **新增断言（验证中发现的 p148 停止命令行表述混用）**：CHtrace 页停止说明写 'kill the process "traced" with the command: "killall mtracer"'——进程启动命令是 mtracer，killall mtracer 正确，但 "traced" 字样系与 p149 SIP trace 页混排的笔误；按原文记录（nr-06）。
5. **无 rejected 断言**：容量 15000/30、QOS 0/0/240、SIP UDP 5360、SMTP 25、LDAP 389、评估许可 2 通道/100 用户/10 站点/每页水印、日志 20MB/15 天、45 格式、31 报表、号段 #31600-31699、GW1/GW2 号段 1200-1500/3300-3800——全部与原文逐格一致；第一本出现过的"公式矛盾"类误报本书未复现。
