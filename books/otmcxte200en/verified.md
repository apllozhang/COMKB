# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f24（主验证对象）；principle p01-p25 / case c01-c13 / counter-example n01-n30 作为各单元的证据素材归并；glossary g01-g46 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 259 页全文通读 + 提取器页码证据交叉核对 + 关键口径字符串回原文 grep 复核

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 23 | f01-f06, f08-f24（全部除 f07 外） |
| reference | 1 | f07（实验拓扑对照表——搭建操作在书外，仅作实验口径与 Boundary 背景） |
| needs_review | 0（单元级） | 断言级 7 项转 needs-review.md（节点号/网段/掩码口径、GA 路径、笔误群、VMS 拼写漂移、推断性结论） |
| rejected | 0 | 无编造断言；端口表/许可三族/my_profile 数值/统计默认值逐格核对一致 |

verified 明细：f01, f02, f03, f04, f05, f06, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——产品认知 → 装机站点配置 → 双向纳管 → SIP 对接 → 信箱业务 → 增值与运维
  type: flow
  V1: {passed: true, reason: "p3-258 章节编排完整；p70 向导自动启动与 p94 同子网声明等关键节点有原文"}
  V2: {passed: true, check_mode: walkthrough, input: "新站点按什么顺序交付 OTMC", expected: "装机→站点配置→纳管→对接→业务→增值运维", observed: "13 个 How-To 章的硬依赖链（向导产出 bics.conf → 声明用其账户 → SIP 对接接已声明 OTMC → 信箱业务依赖对接）与主线一致"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免声明先于向导、信箱先于 SIP 的倒置"}
  evidence: c01-c13 顺序依赖、BOOK_OVERVIEW 优先级排序
  decision: verified

- id: f02
  title: OTMC 产品定位与访问三通道图
  type: framework
  V1: {passed: true, reason: "p5 定义句、p6 三通道、p8 信封键直达逐条有原文"}
  V2: {passed: true, check_mode: walkthrough, input: "老话机用户能用可视化信箱吗", expected: "GUI 直达仅限 8xx8 系与 8088，其余走 TUI", observed: "p8 envelope key 条件与 conditions 一致，g07/g29 互证"}
  V3: {passed: true, expected_benefit: "售前定位与用户期望管理的话术底座"}
  evidence: g01/g07/g29
  decision: verified

- id: f03
  title: OTMC 软件架构组件图（SUSE + OpenTouch Framework + 语音消息应用）
  type: framework
  V1: {passed: true, reason: "p13 底座、p17 架构图组件齐全"}
  V2: {passed: true, check_mode: walkthrough, input: "通知发不出去先看哪个组件", expected: "Scorpio 负责通知，chameleon 管模板生效", observed: "p185 Scorpio 职责 + p192 服务与日志路径可落地排障"}
  V3: {passed: true, expected_benefit: "排障分流（组件/服务/日志）的概念依据；缩写未展开处如实标注"}
  evidence: g31、p19（模板）、n12
  decision: verified

- id: f04
  title: OXE-OTMC 连接架构图——单 SIP trunk + PRS 链路 + VPIM 组网
  type: framework
  V1: {passed: true, reason: "p18-20 三要素原文齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE 与 OTMC 之间能建多条 SIP trunk 吗", expected: "仅一条、指向 front node，Bypass 按全部端口", observed: "p18 原文直接回答；n27 Supra 限制互证"}
  V3: {passed: true, expected_benefit: "组网方案的硬约束清单；证据归并 p01/g33/g34/n27"}
  decision: verified

- id: f05
  title: 商业包装与虚拟化决策结构（非虚拟化 vs OTMC-V）
  type: framework
  V1: {passed: true, reason: "p14-16 商业包/虚拟化/许可三段完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要 vMotion 加全套 VMware HA 可以吗", expected: "仅 vMotion 与手动/半自动 DRS 在支持列表", observed: "p15 白名单原文 + n26 展开边界一致"}
  V3: {passed: true, expected_benefit: "形态决策与合同谈判的边界依据；许可绑定差异（ALUID/dongle）清楚"}
  evidence: g02/g27/g28、n26
  decision: verified

- id: f06
  title: flex-lm 许可机制结构图——.ice 文件、ALUID/OTID、FlexLM 内嵌或外部
  type: framework
  V1: {passed: true, reason: "p16/p35-45/p76-77/p82 四层结构跨章证据连贯"}
  V2: {passed: true, check_mode: walkthrough, input: "向导里许可显示 OK 算装好了吗", expected: "OK 只代表文件存在，有效性要 lmstat 复核", observed: "p77 Warning 与 p82 核验命令闭环；Skip 后不正常工作的 Tips 齐"}
  V3: {passed: true, expected_benefit: "无许可不工作的防线；证据归并 c02/p05/n06/n07/n08"}
  decision: verified

- id: f07
  title: 实验拓扑总图——ESXi 六虚机 + 客户端 PC + company.com DNS 域
  type: reference
  V1: {passed: true, reason: "p21-32 拓扑/域名/IP 表完整"}
  V2: {passed: false, check_mode: walkthrough, input: "照书搭一套实验环境", expected: "分步搭建步骤", observed: "书中无搭建 How-To（ESXi/虚机属课前准备，p58 明说 VMware 基础设施已装）——拓扑表仅作对照"}
  V3: {passed: true, expected_benefit: "全部实验口径值的唯一对照来源（IP/账号/DNS 域），供 Boundary 与 references.md 引用"}
  evidence: g24/g26/g27、n17（网段漂移）
  decision: reference

- id: f08
  title: 安装资料与介质两条制法（DVD 全刻 vs SUSE 单刻 + USB 硬盘）
  type: framework
  V1: {passed: true, reason: "p49-52 物料与制法逐条有原文"}
  V2: {passed: true, check_mode: walkthrough, input: "现场只带一块 USB 硬盘怎么装", expected: "只刻 SUSE 引导盘，其余 ISO 拷 USB 硬盘", observed: "p51 制法二原文直接回答；下载源 BPWS 注明（全称书内未展开）"}
  V3: {passed: true, expected_benefit: "装机物料清单与介质准备的执行入口"}
  evidence: c01、n25
  decision: verified

- id: f09
  title: SUSE 安装三种模式与语义（硬件 / 虚拟化 / 单分区平滑升级）
  type: framework
  V1: {passed: true, reason: "p62 三个安装项原文逐一定义"}
  V2: {passed: true, check_mode: walkthrough, input: "虚机环境选哪个安装项", expected: "OTMC for Virtualized Infrastructure", observed: "p62 定义 + c01 步骤实际选择一致；OTMC first 放弃平滑升级的语义清楚"}
  V3: {passed: true, expected_benefit: "装机第一选择点的防错（选错模式丢平滑升级能力）"}
  evidence: c01、p04、p25
  decision: verified

- id: f10
  title: OTMC 虚机创建参数与 BIOS/ESXi 调优清单
  type: framework
  V1: {passed: true, reason: "p58 规格清单 + p59 调优两项有原文"}
  V2: {passed: true, check_mode: walkthrough, input: "OTMC-V 虚机给多少资源", expected: "按 MyPortal 安装手册 6.2 章口径", observed: "p58 规格在册但 Note 明说 requirements specified only for lab purposes——生产以手册为准的边界诚实"}
  V3: {passed: true, expected_benefit: "装机底座的可执行清单与书外边界同时成立"}
  evidence: c01、g30
  decision: verified

- id: f11
  title: Post-installation wizard 13 步站点配置骨架
  type: framework
  V1: {passed: true, reason: "p69 目录 + p70 自动启动 + p71-81 各步页面证据完整"}
  V2: {passed: true, check_mode: walkthrough, input: "站点级配置在哪做", expected: "首启自动进向导，13 步顺序固定", observed: "目录顺序与 c02 实验步骤一一对应；DNS/账户/许可/证书/备份存储各步与 p02-p07 原则互证"}
  V3: {passed: true, expected_benefit: "站点配置唯一入口的操作骨架；证据归并 c02/p02-p07/n01-n05"}
  decision: verified

- id: f12
  title: 8770 网络层级与节点编号规则（Network → Subnetwork → Node）
  type: framework
  V1: {passed: true, reason: "p85-87/p94-98 层级与编号规则原文齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE 在 8770 里节点号怎么填", expected: "ABC 网络号×100 + OXE 节点号", observed: "p87 公式与 p85 siteid 核对法一致；OTMC 节点自由号规则清楚（98/99 双口径见 needs-review nr-01）"}
  V3: {passed: true, expected_benefit: "声明层级的防错公式；证据归并 c03/c04/p08/n09/n17"}
  decision: verified

- id: f13
  title: OXE/OTMC 双向同步矩阵（complete/partial × separate/global × 发起侧）
  type: framework
  V1: {passed: true, reason: "p88/p100 两处矩阵原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "只想同步几个新用户用哪种组合", expected: "OXE 节点发起 Partial+Separate（前提 4400 Synchro=True）", observed: "p88 Partial 类型定义 + p100 'OTMC 节点 Partial 与 Complete 等价'口径自洽"}
  V3: {passed: true, expected_benefit: "同步操作的选择表；证据归并 c03/c04"}
  decision: verified

- id: f14
  title: OXE 侧 SIP 对接参数结构（trunk group → external gateway → proxy/gateway/registrar/trusted → 全局）
  type: framework
  V1: {passed: true, reason: "p102-108 四段参数逐页有原文"}
  V2: {passed: true, check_mode: walkthrough, input: "信箱呼叫不通先查哪段", expected: "按 trunk/external gateway/trusted/全局四段排查", observed: "p103 trunk 三参数、p105 端口 5040/TCP/ICE type、p107 trusted、p108 编解码与前缀逐段对上"}
  V3: {passed: true, expected_benefit: "SIP 对接施工与排障的四段地图；证据归并 c05/p09/p10/n29"}
  decision: verified

- id: f15
  title: Connection 用户开通与话机寻址体系（两法建户 + resurrection/空闲地址/IP 静态 + 许可三族）
  type: framework
  V1: {passed: true, reason: "p109-118 建户/寻址/许可三段证据完整"}
  V2: {passed: true, check_mode: walkthrough, input: "数字话机没有物理地址怎么激活", expected: "resurrection：话机直拨分机号+默认密码 0000", observed: "p113 原文 + 移机 In/Out of Service 前缀口径；许可三族六类表 p117 逐格核对"}
  V3: {passed: true, expected_benefit: "宿主用户交付的三法选型与许可核查；证据归并 c06/p11/n24"}
  decision: verified

- id: f16
  title: 语音信箱对象模型——VMS → mailbox（必须挂 profile）→ user（Mailboxes/Licenses 页签）
  type: framework
  V1: {passed: true, reason: "p121-127/p134-141 三级对象逐页有原文"}
  V2: {passed: true, check_mode: walkthrough, input: "信箱建到保存时报错", expected: "Configuration 页签没挂 profile", observed: "p139 强制前置原文；p137 VMS 核验、p136 分机号挂钩闭环"}
  V3: {passed: true, expected_benefit: "信箱交付的防错模型；证据归并 c07/p12/p13"}
  decision: verified

- id: f17
  title: Voice mail profile 参数地图（General + Configuration 1/2/3 四页签）
  type: framework
  V1: {passed: true, reason: "p146-152 四页签参数与默认值原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "怎么批量限制信箱容量", expected: "profile Configuration 3 的 Max size per mailbox + Check quota", observed: "p150 'Check quota 关闭时不生效'原文；zero-out（p149）等行为参数逐项在册"}
  V3: {passed: true, expected_benefit: "批控模板的参数字典；证据归并 c08/p14/p15"}
  decision: verified

- id: f18
  title: 问候语（Greetings）管理体系——四类问候 + 管理员 Greeting Managers 网页
  type: framework
  V1: {passed: true, reason: "p128 网页职责、p131/142 四类问候有原文"}
  V2: {passed: true, check_mode: walkthrough, input: "要给指定用户换公司问候语", expected: "Greeting Managers 网页上传/激活", observed: "p128 动作集（激活/删除/下载/上传、数量不限）+ c07 步骤 12 实操路径一致"}
  V3: {passed: true, expected_benefit: "问候语集中管理的入口与权限模型；证据归并 c07/g19"}
  decision: verified

- id: f19
  title: 用户自助 Web 双应用——My Profile 与 MyMessaging 入口与功能区
  type: framework
  V1: {passed: true, reason: "p153-166 两应用 URL 与功能分区原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "用户想在网页上听留言", expected: "MyMessaging（FQDN/MyMessaging）或经 My Profile 进入", observed: "p156/p165 两个入口原文；功能分区与 p11 图一致"}
  V3: {passed: true, expected_benefit: "交付后用户自助的导览；证据归并 g13/p12/p24"}
  decision: verified

- id: f20
  title: SMTP/SMS 通知链路图——留言落箱 → Scorpio → 外部 SMTP → 邮件/短信
  type: framework
  V1: {passed: true, reason: "p169-185 链路与 p180-182 双矩阵原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "没收到邮件通知怎么排", expected: "查发件账户退信、SMTP 连通、scorpio 日志", observed: "p174 失败可见性两条（退信/未达才告警）+ p192 服务与日志路径闭环；LS/UM 矩阵 p180 逐格核对"}
  V3: {passed: true, expected_benefit: "感知最强增值功能的部署与排障地图；证据归并 c09/p16-p19/n11/n12/n15/n16/n21/n22"}
  decision: verified

- id: f21
  title: IMAP 访问链路——OTMC 即 IMAP 服务器（IMAPS/TLS 默认），邮件客户端直读留言
  type: framework
  V1: {passed: true, reason: "p193-201/p207-208 原理与 How-To 证据连贯"}
  V2: {passed: true, check_mode: walkthrough, input: "Outlook 测试有红叉算失败吗", expected: "发信测试失败属预期，IMAP 登录测试 Completed 才算", observed: "p207 判据原文 + p208 IMAPS/TLS 默认与改级规则一致"}
  V3: {passed: true, expected_benefit: "IMAP 对接的三处对齐点与验收判据；证据归并 c10/p20/n13/n14"}
  decision: verified

- id: f22
  title: General announcement 机制——三种播报场景 + 增强菜单与权限
  type: framework
  V1: {passed: true, reason: "p210-227 讲义与 How-To 证据完整"}
  V2: {passed: true, check_mode: walkthrough, input: "能不能给不同部门配不同公告", expected: "不能——单条、新录覆盖旧录", observed: "p223 硬限制原文 + p225 三选场景 + n19 AA 选项废弃互证"}
  V3: {passed: true, expected_benefit: "广播需求评估的边界表；证据归并 c11/p21/n18/n19/n20"}
  decision: verified

- id: f23
  title: OpenTouch 备份恢复机制——8770 发起，SSH/SFTP 两段式，恢复后手工起服务
  type: framework
  V1: {passed: true, reason: "p228-238/p240-245 链路与归档结构原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "恢复完服务没起来是失败吗", expected: "设计行为——起服务必须手工，<5 分钟", observed: "p245 原文 + p238 停服务命令 + p244 Force 选项 + n10 删用户入口警告闭环"}
  V3: {passed: true, expected_benefit: "运维底线动作的行为规则；证据归并 c12/p22/p25/n10"}
  decision: verified

- id: f24
  title: Voicemail statistics 机制——statistics.properties 参数结构 + 三格式输出
  type: framework
  V1: {passed: true, reason: "p247-258 参数与默认值原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "统计文件没生成先查什么", expected: "目录是否手工建/权限、mascd 是否重启", observed: "p258 Note 与操作链 + p256 默认值表闭环"}
  V3: {passed: true, expected_benefit: "统计启用的参数字典与哑坑清单；证据归并 c13/p23/n30"}
  decision: verified
```

## 断言级裁决记录

1. **principle 提取器"近满阈值默认 80%"**：成立。p184 原文 "Enter the percentage (by default 80%)"——默认口径为原文明示，已回原文逐格核对，不是提取器推断。
2. **counter-example 提取器 n17 四处示例漂移**：全部原文核验成立——OTMC 节点号 p94=98 与 p95=99；声明章网段 155.1.1.x 与拓扑章 151.1.1.x 并存；p94 反查 155.1.1.50 返回 otmc.company.com 155.1.1.60；p84 netadmin 示例掩码 255.255.0.0 与同页 /24 不符。转 needs-review nr-01/nr-02/nr-03。
3. **本轮新发现——VMS 默认名拼写漂移**：p137 写 "defaultVmLS"，p138/p188 写 "defaultVmsLS"，同一对象两种拼写并存（回原文 grep 复核）。转 needs-review nr-06。
4. **counter-example 提取器 n25 笔误群**：原文核验成立——p52 "Red Hat installation"、p53 "CheckSytemLinux.sh" 与 p66 "CheckSystemLinux.sh" 并存、p84 "APPLY MOFIFICATION"、p36 "Sytem"。转 needs-review nr-05。
5. **无 rejected 断言**：端口（5040/5060/2570）、规模（15000×3 模式/5000 GUI）、通知（2MB/80%/端口 25）、许可三族六类（173/174/176/177/316/317）、my_profile（10MB/5s/15s/15s/15 天/7 天）、统计默认值（enableStatistics=disabled 等）、时长（25 分钟/30 分钟/<5 分钟）全部与原文逐格一致。
