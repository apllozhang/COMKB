# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f37（主验证对象）；principle p01-p44 / case c01-c18 / counter-example n01-n55 作为各单元的证据素材归并；glossary g01-g60 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 587 页全文候选与提取器页码证据交叉核对

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 34 | f01, f05-f37（f02/f03/f04 除外，详见下表） |
| reference | 3 | f02（R-Lab 平台结构）、f03（Linux/无线客户端操作）、f04（产品组合与文档指针） |
| needs_review | 0（单元级） | 断言级 4 项转 needs-review.md（镜像会话新旧口径、LLDP-MED 两页数值、UNP 全称两写、console 速率两处口径） |
| rejected | 0 | 无编造断言；会话上限表、PoE 功率表、路径成本表、hash 默认表、VC 规模矩阵均与原文逐格核对一致 |

verified 明细：f01, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37

reference 说明：f02/f03 为 R-Lab 教学基础设施（账号/POD/客户端操作，实验口径），仅作 Boundary 背景与 book/overview 环境区素材；f04 为产品组合营销页与文档指针（选型查 datasheet），其文档五册指针已并入 references.md 与各卡 Boundary。

## 验证记录

```yaml
- id: f01
  title: 三日课程推进主线——管理接入 → 配置生命周期 → 堆叠 → 二层 → 三层 → 策略 → 运维
  type: framework
  V1: {passed: true, reason: "p6-8 三日议程逐日列出；p580 课程收尾；附加模块页码区间明确"}
  V2: {passed: true, check_mode: walkthrough, input: "新工程师按什么顺序学 OmniSwitch 交付", expected: "接入→生命周期→组网→策略→运维的顺序", observed: "议程与 17 个 How-To 章分布互证，讲义→实验闭环成立"}
  V3: {passed: true, expected_benefit: "交付排期与学习路径的顺序基线"}
  decision: verified

- id: f05
  title: AAA 认证框架——服务类型 × 认证链 × fail-through 语义
  type: framework
  V1: {passed: true, reason: "p67-69 概览图与命令语法完整；p95 ASA 定义句"}
  V2: {passed: true, check_mode: walkthrough, input: "SSH 登录被拒怎么恢复", expected: "查认证链是否 denied 并显式声明 local", observed: "p95 Tips 与 c01 步骤 2 一致（aaa authentication ssh local）"}
  V3: {passed: true, expected_benefit: "一切配置的入口机制；证据归并 p01/p03/n38"}
  decision: verified

- id: f06
  title: 用户数据库与外部服务器结构——userTable/64 用户/密码策略/命令日志
  type: framework
  V1: {passed: true, reason: "p70-74 逐段给出；p74 IEC62443 版本线明确"}
  V2: {passed: true, check_mode: walkthrough, input: "账号合规治理要做哪些项", expected: "复杂度+生命周期+强制刷新+外部服务器四层", observed: "p02/p03/p04 与原文逐条对上，密码策略默认值书中未给（如实标注）"}
  V3: {passed: true, expected_benefit: "安全底线的账号治理清单；证据归并 p01/p02/p03/p04/n01"}
  decision: verified

- id: f07
  title: 管理面接入方式全景——console/EMP/WebView/SNMP/会话数表
  type: framework
  V1: {passed: true, reason: "p75-87 五通道逐段；p80 会话表逐格"}
  V2: {passed: true, check_mode: walkthrough, input: "各协议并发会话上限是多少", expected: "Telnet 6/FTP 4/SSH 8/HTTP 4/总 20/SNMP 50", observed: "p07 与 p80 表逐格一致"}
  V3: {passed: true, expected_benefit: "接入规划与加固基线；证据归并 p05/p06/p07/p08/p09/n02/n38/n39"}
  decision: verified

- id: f08
  title: WebView 七大配置组与操作动线
  type: framework
  V1: {passed: true, reason: "p98 七组原文列举；p98-101 动线截图级"}
  V2: {passed: true, check_mode: walkthrough, input: "WebView 里改会话参数走哪里", expected: "Security > ASA > Session > Configuration", observed: "p98 路径明确；c01 步骤 6 实测一致"}
  V3: {passed: true, expected_benefit: "远程排障入口的操作锚点；证据归并 c01"}
  decision: verified

- id: f09
  title: Lightning Config 开局七步流
  type: framework
  V1: {passed: true, reason: "p104-121 步骤与禁令齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "新交换机怎么最快开局", expected: "DHCP 接端口 1 → https 192.168.0.1 → Defaults → 改密 → 保存", observed: "七步流与 c17 操作序列、p10 数值口径完全对应"}
  V3: {passed: true, expected_benefit: "小网络交付主路径；证据归并 p10/c17/n03-n07"}
  decision: verified

- id: f10
  title: 示例网络拓扑两型——纯二层中型网与 Mesh/三层中型网
  type: framework
  V1: {passed: true, reason: "p122-125 两张拓扑图与警告框"}
  V2: {passed: true, check_mode: walkthrough, input: "照示例拓扑接线可以直接施工吗", expected: "不行——必须先确认环路避免技术", observed: "p125 STOP 警告原文明确；n06 归并一致"}
  V3: {passed: true, expected_benefit: "组网沟通素材与防环红线；证据归并 n06"}
  decision: verified

- id: f11
  title: 闪存目录三层模型与启动序列
  type: framework
  V1: {passed: true, reason: "p129-131 目录/引导链/启动命令齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "设备从哪个目录启动", expected: "按内容异同判 certified/running；reload all 强制 certified", observed: "p142 启动规则与 p11 逐条一致；c02 实测验证"}
  V3: {passed: true, expected_benefit: "配置可靠性的模型底座；证据归并 p11/p12/c02/n08-n10"}
  decision: verified

- id: f12
  title: 配置保存/认证/回滚状态机
  type: framework
  V1: {passed: true, reason: "p132-135 三命令语义与约束完整"}
  V2: {passed: true, check_mode: walkthrough, input: "write memory 后重启配置还会丢吗", expected: "CERTIFY NEEDED 态重启回 certified，working 里文件可取回", observed: "p144 Warning 与 c02 步骤 5-6 行为一致"}
  V3: {passed: true, expected_benefit: "防配置丢失的核心操作语义；证据归并 p11-p13/c02/n09/n10/n11"}
  decision: verified

- id: f13
  title: 配置备份恢复与 USB 备份结构
  type: framework
  V1: {passed: true, reason: "p136-137/p148-149 两线口径齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "配置备份包里有什么、存哪里", expected: "横幅+userTable+vcboot.cfg 打 tar 存 /flash/config-backup-recovery（上限 10）", observed: "p13 与 p136 逐格一致"}
  V3: {passed: true, expected_benefit: "备份恢复 SOP 依据；证据归并 p13/n12"}
  decision: verified

- id: f14
  title: Virtual Chassis 每型号规模与 VFL 端口矩阵
  type: framework
  V1: {passed: true, reason: "p152-154/p159 矩阵逐格"}
  V2: {passed: true, check_mode: walkthrough, input: "6360 最多堆几台、VFL 用哪些口", expected: "24/48 口 4 台（10 口机型 8 台）；P24 用 27/28", observed: "p153 矩阵与 c03 步骤 1 实验口径一致"}
  V3: {passed: true, expected_benefit: "堆叠规划查表依据；证据归并 g31/p16/c03"}
  decision: verified

- id: f15
  title: VC 选举与接管规则
  type: framework
  V1: {passed: true, reason: "p155-157 四级序与 MAC retention 原文明确"}
  V2: {passed: true, check_mode: walkthrough, input: "主备怎么选、原主恢复会抢回吗", expected: "优先级→运行时长(>10 分钟)→ID→MAC；原主不抢回", observed: "p15 与 p156-157 逐条一致；p167 优先级 0-255 互证"}
  V3: {passed: true, expected_benefit: "堆叠高可用的行为模型；证据归并 p15/p16/c03/n14"}
  decision: verified

- id: f16
  title: VC 分裂防护双机制——带外 EMP RCD 与带内 VCSP helper
  type: framework
  V1: {passed: true, reason: "p160-161 两机制与行为完整"}
  V2: {passed: true, check_mode: walkthrough, input: "VFL 断了怎么防双主", expected: "RCD 经 EMP 带外侦测或 VCSP 经 helper 带内防护", observed: "p17 与原文行为（关用户口/Split-Topology/恢复重启回归）一致；平台限制已标注"}
  V3: {passed: true, expected_benefit: "堆叠分裂风险的设计对策；证据归并 p17"}
  decision: verified

- id: f17
  title: ISSU 滚动升级流程与 ssh-chassis 远程访问
  type: framework
  V1: {passed: true, reason: "p162-163/p181 步骤与命令齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "堆叠升级怎么减少中断", expected: "issu_dir 独立目录，slave 按 ID 从低到高滚动", observed: "p162 四步与 p17 口径一致"}
  V3: {passed: true, expected_benefit: "堆叠升级路径与跨成员运维入口；证据归并 c03"}
  decision: verified

- id: f18
  title: VC 配置五步与 VC 内同步语义
  type: framework
  V1: {passed: true, reason: "p164-171/p175-176 步骤与 Notes 齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "VC 下 write memory 够了吗", expected: "不够——certified 级同步需 flash-synchro/copy running certified", observed: "p170-171 与 c03 步骤 6（Synchronizing chassis 2）一致"}
  V3: {passed: true, expected_benefit: "堆叠施工序列；证据归并 c03/n13/n14"}
  decision: verified

- id: f19
  title: VLAN 三入口结构——静态成员 / UNP 动态分类 / 802.1Q 打标
  type: framework
  V1: {passed: true, reason: "p185-200 三通道与 802.1Q 数值齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "端口进 VLAN 有几种方式", expected: "静态/UNP 动态/802.1Q 三通道", observed: "p185 原文三通道；c04/c07 实验分别验证"}
  V3: {passed: true, expected_benefit: "二层基本盘的结构模型；证据归并 p37/p38/p42/c04/c07/n15"}
  decision: verified

- id: f20
  title: UNP 分类规则优先级体系
  type: framework
  V1: {passed: true, reason: "p189-192 九规则与优先序原文明确"}
  V2: {passed: true, check_mode: walkthrough, input: "多条分类规则同时命中听谁的", expected: "Extended > Binding > Simple；简单规则按编号", observed: "p192 优先序原文；c04 按 MAC 分类实验一致"}
  V3: {passed: true, expected_benefit: "动态 VLAN 与准入的规则设计依据；证据归并 p38/c04/f27"}
  decision: verified

- id: f21
  title: VLAN 间路由与 IP 接口绑定模型
  type: framework
  V1: {passed: true, reason: "p194-196/p348 模型句与命令齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "开了 IP 接口就自动路由了吗", expected: "是——≥1 个 IP 接口即激活路由；无成员 VLAN 接口 DOWN", observed: "p195/p39 与 c04 步骤 5（int_50 DOWN 思考题）一致"}
  V3: {passed: true, expected_benefit: "三层可达的启用条件；证据归并 p39/p42/c04/n16"}
  decision: verified

- id: f22
  title: OST 工具两代架构
  type: framework
  V1: {passed: true, reason: "p215-230 功能/架构/获取口径齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "OST 2.0 什么前提能装", expected: "MyPortal 免费+有效 OmniSwitch 支持合同", observed: "p33 与 p229-230 逐条一致"}
  V3: {passed: true, expected_benefit: "一线装机效率工具的引入决策；证据归并 p33/n47/c18"}
  decision: verified

- id: f23
  title: 诊断工具箱八件套结构
  type: framework
  V1: {passed: true, reason: "p232-259 八件逐段"}
  V2: {passed: true, check_mode: walkthrough, input: "排障取证有哪些抓手", expected: "swlog/事件日志/命令日志/镜像/抓包/RMON/health/sFlow", observed: "八件与 c05 实验一一对应；p34/p35/p44 数值互证"}
  V3: {passed: true, expected_benefit: "售后日常排障的工具地图；证据归并 p34/p35/p44/c05/n40-n42/n55"}
  decision: verified

- id: f24
  title: 链路聚合结构——静态 vs LACP + hash 控制矩阵
  type: framework
  V1: {passed: true, reason: "p270-281 两型与 hash 默认表齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "6360 出厂 hash 是哪种", expected: "brief", observed: "p36 与 p280 逐型号表一致；c06 实验冗余验证"}
  V3: {passed: true, expected_benefit: "上行带宽与可靠性的基础方案；证据归并 p36/c06/n23/n44-n46"}
  decision: verified

- id: f25
  title: STP 体系——两种模式 × 三种协议 + 路径成本与保护特性
  type: framework
  V1: {passed: true, reason: "p300-311 模式/协议/成本/保护齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "默认生成树行为是什么", expected: "per-VLAN（1x1）模式；默认桥优先级 32768", observed: "p18/p19 与 p300/307/315-316 逐格一致；c08 实验验证"}
  V3: {passed: true, expected_benefit: "环路避免标配的行为模型；证据归并 p18/p19/c08/n18-n20/n54"}
  decision: verified

- id: f26
  title: DHL Active-Active 机制结构
  type: framework
  V1: {passed: true, reason: "p326-334/p341/p344 结构与约束齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "DHL 和 STP 能同链路混用吗", expected: "不能——DHL 端口自动禁 STP", observed: "p21/n21 与 p327-328/p341 一致；c09 实验验证"}
  V3: {passed: true, expected_benefit: "双上行方案的选型与约束；证据归并 p20/c09/n21/n22"}
  decision: verified

- id: f27
  title: Access Guardian/UNP 认证决策流与配置五层
  type: framework
  V1: {passed: true, reason: "p456-474 决策流与五层配置齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "认证成功后用户怎么拿到 VLAN 和策略", expected: "RADIUS Filter-Id 回传 UNP 名，档案含 VLAN+策略列表", observed: "p27 与 p457/p477-480 一致；c15 实验验证（Filter-ID=UNP-employee）"}
  V3: {passed: true, expected_benefit: "准入+动态策略一体的部署依据；证据归并 p27/p14/c15/n29"}
  decision: verified

- id: f28
  title: LLDP/LLDP-MED 信息模型与 IP 电话自动语音 VLAN 流
  type: framework
  V1: {passed: true, reason: "p488-499 TLV 模型与语音流齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "话机怎么自动进语音 VLAN", expected: "lldp network-policy + mobile tag + 分类规则", observed: "p496 命令链与 c16/p28 一致；两页示例数值差异已转 nr-02"}
  V3: {passed: true, expected_benefit: "IP 电话场景刚需的落地路径；证据归并 p28/c16/n30/n31"}
  decision: verified

- id: f29
  title: PoE 管理体系——供电等级表/优先级/特殊特性
  type: framework
  V1: {passed: true, reason: "p508-520 等级表与管理参数齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "802.3bt Type4 能给 PD 多少瓦", expected: "PD 71W / PSE 100W", observed: "p29 与 p513 表逐格一致；p30 型号线与 p510-511 一致"}
  V3: {passed: true, expected_benefit: "AP/话机/摄像头供电规划依据；证据归并 p29/p30/n32/n33/n48"}
  decision: verified

- id: f30
  title: 软件升级三通道与安全版本线
  type: framework
  V1: {passed: true, reason: "p529-535 通道与版本线齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "日常升级选什么版本", expected: "最新 GA/MR；合规场景查 FIPS/JITC/CC 认证清单", observed: "p31 与 p531-533 一致；升级步骤书外（Release Notes）如实标注"}
  V3: {passed: true, expected_benefit: "版本策略与安全合规底线；证据归并 p31/n34/n35/n55"}
  decision: verified

- id: f31
  title: Auto-Fabric 零触开局七步链与 LBD 环路检测
  type: framework
  V1: {passed: true, reason: "p536-553 七步/LBD/默认值齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "首启提示 Y/N 怎么答才是启用自动配置", expected: "N 或不答=启用，Y=禁用（语义相反）", observed: "p32/n36 与 p539 原文一致；RCL 6 次与 SPB 默认值互证"}
  V3: {passed: true, expected_benefit: "规模化部署的零触路径；证据归并 p32/n36/n37"}
  decision: verified

- id: f32
  title: Fleet Supervision 与 Services Kiosk 结构
  type: framework
  V1: {passed: true, reason: "p555-568 四块能力与开通三路齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "没有 OmniVista 能用 Fleet Supervision 吗", expected: "能——CSV/XLSX 模板导入设备清单", observed: "p563 原文支持；免费只读边界（p556-558）一致"}
  V3: {passed: true, expected_benefit: "资产合规看板的开通依据；证据归并 g20/g57"}
  decision: verified

- id: f33
  title: OST 2.0 安装组件与依赖链
  type: framework
  V1: {passed: true, reason: "p572-580 组件与步骤齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "OST 2.0 装机顺序是什么", expected: "Postgres 先装 → Server → Config Tool 初始化 → Client", observed: "c18 与 p573-580 逐步一致；测试版本 18.1 明确"}
  V3: {passed: true, expected_benefit: "2.0 新架构落地施工链；证据归并 c18/p33"}
  decision: verified

- id: f34
  title: QoS 端口队列模型——QSet/QSI/QSP 与策略引擎接入
  type: framework
  V1: {passed: true, reason: "p393-409 队列模型与策略三件套齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "QoS 策略配完怎么才生效", expected: "qos apply 下发硬件；全局开关类立即生效", observed: "p24/n26 与 p396/404/423-425 一致；c12 实验验证"}
  V3: {passed: true, expected_benefit: "语音/关键业务保障的机制底座；证据归并 p24/p25/p43/c12/n25-n27"}
  decision: verified

- id: f35
  title: VRRP 结构——虚拟路由器/优先级/抢占/跟踪策略
  type: framework
  V1: {passed: true, reason: "p374-381/p387/p390 结构与数值齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "改 VRRP 优先级直接改行吗", expected: "不行——必须先 disable 实例", observed: "p23/n24 与 p390 Warning 一致；c11 实验验证"}
  V3: {passed: true, expected_benefit: "网关高可用的设计与操作约束；证据归并 p23/c11/n24"}
  decision: verified

- id: f36
  title: ACL 条件关键字分层与保留安全组
  type: framework
  V1: {passed: true, reason: "p431-443 条件分箱与保留组齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "UserPorts 组要写进策略条件才生效吗", expected: "不用——组内端口自动生效，但仅作用于路由流量", observed: "p26/n28 与 p440/p453 一致；c14 实验验证"}
  V3: {passed: true, expected_benefit: "安全边界的过滤设计依据；证据归并 p26/c14/n27/n28/n53"}
  decision: verified

- id: f37
  title: IP 服务基础件——DHCP Client/Relay/UDP Relay/Loopback0/静态路由
  type: framework
  V1: {passed: true, reason: "p349-365 五基础件齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "Loopback0 的路由通告行为是什么", expected: "RIP/OSPF 自动通告，BGP 不会", observed: "p40 与 p360 原文一致；p22/p21 DHCP 口径互证"}
  V3: {passed: true, expected_benefit: "跨网段取址与管理地址的标准件；证据归并 p21/p22/p39/p40/c10/c13/n43"}
  decision: verified
```

## 断言级裁决记录

1. **提取器登记“镜像会话数 2→4 新旧口径矛盾”**：成立。p249 讲义（已从 2 提高到 4，另有 4 个 MTP 索引限制）与 p265 实验注释（"limited to two"）矛盾；按较新规格口径取 4，实验页为旧口径残留。转 needs-review nr-01，卡 Boundary 要求以 Specification Guide 与 show 实测为准。
2. **提取器登记“LLDP-MED 两页数值不一致”**：成立。p496（l2-priority 5 / dscp 46）与 p499（l2-priority 7 / dscp 14）同命令不同值，属教材示例差异；不编造统一值，转 needs-review nr-02。
3. **提取器登记“UNP 全称两写”**：成立。p393 "User Network Profile" 与 p456/p477 "Universal Network Profile" 并存，同一概念；glossary g13 如实并列，转 needs-review nr-03。
4. **验证新发现“console 默认速率两处口径”**：p76 幻灯标 "Speed (baud): 115200" 并注明新一代不同；p523-527 分代表表则多数机型 9600、6900/6870/6860N 按 115200。两处以“分代表查表”为准确口径，转 needs-review nr-04。
5. **无 rejected 断言**：会话上限（6/4/8/4/20/50）、PoE 四档功率（12.95/15.4 等）、路径成本两套（100/19/4/2 与 200 万/20 万/2 万/2000）、hash 默认逐型号、VC 选举四级序、STP 收敛（50s/<1s/<1s）、RADIUS 默认参数（3 次/2 秒/1812/1813）均与原文逐格一致。
