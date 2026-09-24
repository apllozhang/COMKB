# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f48（主验证对象）；principle p01-p50 / case c01-c14 / counter-example n01-n54 作为各单元的证据素材归并；glossary g01-g56 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 465 页全文理解 + 提取器页码证据交叉核对

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 46 | f01, f04-f48（除 f02/f03 外全部，详见下表） |
| reference | 2 | f02（RLAB 全虚拟化拓扑/账号表）、f03（混合模式课堂拓扑）——教学环境结构，能力卡仅作 Boundary 背景 |
| needs_review | 0（单元级） | 断言级 8 项转 needs-review.md（容量表归属、矩阵双列、CTL 路径异写、DID 双口径、笔误、推断、版本混布、清单交叉） |
| rejected | 0 | 无编造断言；软件锁 177/345/430、租期 1800/86400、优先级六级序等关键数字均逐格核对一致 |

verified 明细：f01, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39, f40, f41, f42, f43, f44, f45, f46, f47, f48

## 验证记录

```yaml
- id: f01
  title: 全书课程推进主线——环境地基 → 协议底座 → 终端侧 → 运维工具 → 出口（外线+远程）
  type: framework
  V1: {passed: true, reason: "p44/p65/p384 章节结构页齐备，九段推进与目录一致"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE 站点 SIP 化按什么顺序交付", expected: "环境→协议→终端→运维→出口", observed: "九段主线与 20 项任务映射互证，无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线；capability 体系组织轴"}
  decision: verified

- id: f04
  title: ITSP1 SIP 运营商模拟器——直连拓扑与号码变换规则
  type: framework
  V1: {passed: true, reason: "p22-27 网关地址/账号/号码规则逐格给出"}
  V2: {passed: true, check_mode: walkthrough, input: "实验里拨 0110312345 出局变成什么号", expected: "+33110312345", observed: "p24 呼出变换规则直接回答"}
  V3: {passed: true, expected_benefit: "lab-environment 能力卡的实体内容；证据归并 g53/n45"}
  decision: verified

- id: f05
  title: ITSP2 模拟器——经 SBC 的第二条运营商腿
  type: framework
  V1: {passed: true, reason: "p29-33 网关/账号/号码口径齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "SBC 实验对接的运营商地址和账号是什么", expected: "gateway.itsp2.com + podP/alcatel", observed: "p30 直接回答；与 c12 向导 SIP TRUNK/ACCOUNT 屏互证"}
  V3: {passed: true, expected_benefit: "SBC 接入实验的公共依赖；两套 DID 口径差异已转 needs-review nr-04"}
  decision: verified

- id: f06
  title: POD 准备 How-To 流程——虚机启动 → 预配置核对 → 终端开通 → 公网接入
  type: framework
  V1: {passed: true, reason: "p35-42 四段流程完整（启动清单/预配置/用户表/公网参数）"}
  V2: {passed: true, check_mode: walkthrough, input: "拿到 POD 后第一步做什么", expected: "启动虚机并核对预配置基线", observed: "p38 预配置清单（许可/SSH/防火墙/NTP/DHCP）可直接核对"}
  V3: {passed: true, expected_benefit: "task-01/03 执行主体；证据归并 c01/p26/p48"}
  decision: verified

- id: f07
  title: SIP 协议定位与协议栈结构——信令/媒体分层
  type: framework
  V1: {passed: true, reason: "p45-48 分层图与职责五要素完整"}
  V2: {passed: true, check_mode: walkthrough, input: "SIP 负责传语音吗", expected: "只协商不承载，媒体走 RTP、特征由 SDP 描述", observed: "p48 原文明确；与 p32 省资源设计互证"}
  V3: {passed: true, expected_benefit: "全书信令层通用语言；证据归并 p01/g01/g41"}
  decision: verified

- id: f08
  title: SIP 消息与响应码体系——请求十种 + 响应六类
  type: framework
  V1: {passed: true, reason: "p49-50 码表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "trace 里 403 和 488 各代表什么", expected: "403 拒绝（互斥/认证）、488 媒体不可接受", observed: "p50 码表 + p273 法线场景互证"}
  V3: {passed: true, expected_benefit: "读懂全书 trace 的码表；证据归并 p02/n30"}
  decision: verified

- id: f09
  title: SIP 实体角色图——注册/位置/代理/SBC/网关/B2BUA 八角色
  type: framework
  V1: {passed: true, reason: "p51 八角色逐一定义"}
  V2: {passed: true, check_mode: walkthrough, input: "运营商侧的 SBC 在信令里扮什么角色", expected: "安全/拓扑隐藏/NAT 穿越，常以 B2BUA 形态出现", observed: "p51 定义 + g23（ITSP2 报文 Call-ID 带 _b2b-1 踪迹）一致"}
  V3: {passed: true, expected_benefit: "排障定位'谁该回 403/488'的前提；证据归并 g23/g32"}
  decision: verified

- id: f10
  title: SIP 注册与呼叫建立时序——REGISTER 租期 + INVITE 五步
  type: framework
  V1: {passed: true, reason: "p52-54 时序图与全报文样例齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "注册租期默认能有多长", expected: "被注册器上下限钳制（1800-86400s，示例 3600 合法）", observed: "p52 示例与 p88 注册器参数互证"}
  V3: {passed: true, expected_benefit: "注册类排障的时序基线；证据归并 p08/p46/n44"}
  decision: verified

- id: f11
  title: OXE SIP 实现六组件架构——本地网关/字典/代理/注册器/位置/外部网关
  type: framework
  V1: {passed: true, reason: "p56-57 六组件定义完整，p329 外线章复用"}
  V2: {passed: true, check_mode: walkthrough, input: "分机号怎么变成对端 IP", expected: "字典（号码↔URL）+位置服务器（URL→IP）两级", observed: "p57 定义与 f16 互通流程一致"}
  V3: {passed: true, expected_benefit: "SIP Device 开通与外线判定的概念底座；证据归并 g04-g06"}
  decision: verified

- id: f12
  title: 空间冗余与内部域名解析机制——双 IP/节点名/DNS 委托
  type: framework
  V1: {passed: true, reason: "p58-59 机制图与规则原文齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "双机下终端为什么只会连到 Main", expected: "内部域名解析器只让 Main 应答 DNS", observed: "p59 原文明确；与 p181 空间冗余 DM URL 必须 FQDN 互证"}
  V3: {passed: true, expected_benefit: "冗余站点接入规划依据；证据归并 g07/n10"}
  decision: verified

- id: f13
  title: OXE 域名管理路径——netadmin 菜单 19（查询/定制）与管理工具只读
  type: framework
  V1: {passed: true, reason: "p61-63 How-To 完整（菜单号/告警/字段）"}
  V2: {passed: true, check_mode: walkthrough, input: "在 WebAdmin 里能改域名吗", expected: "不能——只能 netadmin 改，管理工具只读", observed: "p62 Warning 原文明确；c02 复核步骤一致"}
  V3: {passed: true, expected_benefit: "证书与冗余的共同地基动作；证据归并 c02/n01"}
  decision: verified

- id: f14
  title: SEPLOS(SIP Extension) vs SIP Device 两形态对比结构
  type: framework
  V1: {passed: true, reason: "p66-68/p75-78 两形态定义与限制齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "门禁设备要参与代接组行吗", expected: "不行——SIP Device 不能入组", observed: "p78 五不带清单直接回答；n02 同源"}
  V3: {passed: true, expected_benefit: "选型即服务等级决策；证据归并 p03/p09/p10/n02/n03"}
  decision: verified

- id: f15
  title: SEPLOS 终端部署四步图——DHCP → DM 配置文件 → 二进制 → SIP 信令
  type: framework
  V1: {passed: true, reason: "p71 四步图原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "话机入网先拿什么地址", expected: "DHCP 拿 DM 应用地址（option 66 或内部 DHCP 类）", observed: "p71 步骤 1 与 c05/c06 DHCP 实验一致"}
  V3: {passed: true, expected_benefit: "三个开通实验的共同骨架；证据归并 g08/g49"}
  decision: verified

- id: f16
  title: NOE↔SIP 终端互通流程——NOE 主叫 6 步 / SIP 主叫 7 步
  type: framework
  V1: {passed: true, reason: "p80-82 两条流程逐步给出"}
  V2: {passed: true, check_mode: walkthrough, input: "SIP 话机拨 NOE 话机信令怎么走", expected: "代理→域名判定→SIP 网关→Call Handling→振铃", observed: "p82 七步与 p330 外线判定条件互证"}
  V3: {passed: true, expected_benefit: "混网站点排障的路径图；证据归并 p46/n44/n47"}
  decision: verified

- id: f17
  title: SIP Device 开通主线九节——私网→中继组→网关→代理→注册器→字典→隔离/信任→建户→验证
  type: framework
  V1: {passed: true, reason: "p84-94 How-To 九节完整"}
  V2: {passed: true, check_mode: walkthrough, input: "新建 SIP Device 用户最小前置是什么", expected: "私网+私有 SIP 中继组+本地网关三件套", observed: "p67/p85/p89 三处一致；n03 同源"}
  V3: {passed: true, expected_benefit: "task-07 执行主体；证据归并 c03/p05-p08/n04/n07"}
  decision: verified

- id: f18
  title: SIP 用户维护命令族——sipgateway/trkstat/sipdict/sipregister/进程与隔离日志
  type: framework
  V1: {passed: true, reason: "p91-94/p236-238/p260-261 命令输出样例齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "31060 是 Device 还是 Extension 怎么查", expected: "sipdict -l，type 2=Device、type 3=Extension", observed: "p92 原文直接回答"}
  V3: {passed: true, expected_benefit: "排障第一步的抓手清单；证据归并 p34/n44/n52"}
  decision: verified

- id: f19
  title: ALE SIP 终端家族谱系——话机四档 + 软终端 + 8008 特例
  type: framework
  V1: {passed: true, reason: "p70 谱系图 + p97-106 各档功能矩阵"}
  V2: {passed: true, check_mode: walkthrough, input: "售前报酒店话机选什么", expected: "8008/8008G（Business+酒店）；8088 酒店只在 8770", observed: "p98 overview + p147 DM 分界互证（推断标注见 nr-06）"}
  V3: {passed: true, expected_benefit: "终端选型清单；证据归并 p11/p12/g27-g29/n26"}
  decision: verified

- id: f20
  title: ALES 界面分区与退出语义——九宫功能区 + 隐藏 vs 退出
  type: framework
  V1: {passed: true, reason: "p118-119 界面分区与两种退出行为原文齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "用户说 ALES 收不到电话，先问什么", expected: "是不是右键 Quit 了（隐藏/关窗仍收来话）", observed: "p119 语义对比直接回答"}
  V3: {passed: true, expected_benefit: "高频客诉的第一分流；证据归并 g26"}
  decision: verified

- id: f21
  title: 一号多机 ALES-DUID 互斥时序——注册记录/403 拒绝/force 抢占/通话中例外
  type: framework
  V1: {passed: true, reason: "p115-117 三分支时序与报文样例齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "同账号两台 PC 同时登录会怎样", expected: "403 + Warning 399 Multiple Logins，可 force 抢占", observed: "p116 报文对照直接回答；通话中禁抢（p117）"}
  V3: {passed: true, expected_benefit: "'账号打架'类工单解释依据；证据归并 p14/g10/n19"}
  decision: verified

- id: f22
  title: 监督与代接机制——SUBSCRIBE/NOTIFY 结构 + Keep Alive 事件码
  type: framework
  V1: {passed: true, reason: "p130-133 机制链与事件码完整"}
  V2: {passed: true, check_mode: walkthrough, input: "被监督人状态多久更新一次", expected: "状态变化以 NOTIFY 推送；Keep Alive 超时判离服", observed: "p132-133 与 p15 事件码（510-513）一致"}
  V3: {passed: true, expected_benefit: "监督方案容量与排障依据；证据归并 p15/g16/g22/n21"}
  decision: verified

- id: f23
  title: 多终端两种组网结构——纯 SEPLOS 主备与 NOE/DECT 混合
  type: framework
  V1: {passed: true, reason: "p134-137 两种组网规则与 RFC3326 佐证齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "REX 能不能顶多终端名额", expected: "不能——Virtual UA/REX/MIPT 不支持", observed: "p135 原文明确；n23 同源"}
  V3: {passed: true, expected_benefit: "多终端组网规划依据；证据归并 g15/n23"}
  decision: verified

- id: f24
  title: 寻线组三型与混装规则矩阵——circular/cyclical/parallel
  type: framework
  V1: {passed: true, reason: "p138-141 三型规则与禁令齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "并行组能 SIP/NOE 混装吗", expected: "不能——首个成员类型定调", observed: "p141 原文直接回答；n22 同源"}
  V3: {passed: true, expected_benefit: "建组需求评审依据；证据归并 p18/g17"}
  decision: verified

- id: f25
  title: RCC 能力分层——legacy basic / enhanced basic / advanced 三档
  type: framework
  V1: {passed: true, reason: "p142 三档条件与业务全集齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "Make call 想不占压缩资源怎么配", expected: "SIP 设备 Phone COS 开 Optimize resource 3PCC call", observed: "p142 原文直接回答"}
  V3: {passed: true, expected_benefit: "CTI 集成方案分层依据；证据归并 g18"}
  decision: verified

- id: f26
  title: SIP DM 选型结构——OXE DM vs 8770 DM 对比 + 三种部署拓扑
  type: framework
  V1: {passed: true, reason: "p146-150 对比清单与拓扑分支齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "ALES 用 8770 管理行吗", expected: "不行——ALES 只受 OXE DM 管理", observed: "p148 原文明确；p49 同源"}
  V3: {passed: true, expected_benefit: "DM 架构决策依据；证据归并 p49/g08/g36/n08/n26"}
  decision: verified

- id: f27
  title: DM profile 体系与六块特性——默认 0、上限 100、按子型适配
  type: framework
  V1: {passed: true, reason: "p152-153 体系规则与六块特性完整"}
  V2: {passed: true, check_mode: walkthrough, input: "改一个 profile 影响多少设备", expected: "该 profile 全部设备重生成配置并发 NOTIFY", observed: "p152 原文明确；p19 同源"}
  V3: {passed: true, expected_benefit: "profile 规划与变更评估依据；证据归并 p19/n49"}
  decision: verified

- id: f28
  title: 配置文件生成/存储/获取机制——MAC 与 login 双命名 + 401/mTLS 双认证
  type: framework
  V1: {passed: true, reason: "p156-160/p163-164 命名规则与认证通道齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "ALES 的配置文件叫什么名", expected: "conf_<login 十六进制>.xml，按 login 命名", observed: "p156 规则与 c08 csipsets -d 输出互证"}
  V3: {passed: true, expected_benefit: "DM 排障入口；证据归并 p21/p22/n42"}
  decision: verified

- id: f29
  title: 二进制管理机制——downbin 目录/版本比对/轮询升级
  type: framework
  V1: {passed: true, reason: "p165 五点机制原文齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "话机什么时候升级二进制", expected: "每天固定时刻或设备重启时（轮询）", observed: "p165 原文直接回答；c05/c06 access.log downbin 记录互证"}
  V3: {passed: true, expected_benefit: "升级窗口规划依据；证据归并 g08"}
  decision: verified

- id: f30
  title: OXE DM 证书定制流程（内部 PKI）——根 CA → CS 证书 → CTL 产物
  type: framework
  V1: {passed: true, reason: "p168-171 How-To 完整（菜单/参数/核验）"}
  V2: {passed: true, check_mode: walkthrough, input: "安装默认证书能给 SIP 话机用吗", expected: "不能——只适配 WBM/HTTPS", observed: "p169 原文明确；c04 核验步骤一致"}
  V3: {passed: true, expected_benefit: "安全地基施工链；证据归并 c04/p23/p24/n09"}
  decision: verified

- id: f31
  title: ALE-2/ALE-3 话机开通流程骨架——DM 激活 → 参数 → 建户 → DHCP → MAC
  type: framework
  V1: {passed: true, reason: "p172-186 六段 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "ALE-2 拿地址的方式是什么", expected: "DHCP 类 ALE-2X（VCI aledevice）下发 DM URL", observed: "p181 原文与 c05 步骤 7 一致"}
  V3: {passed: true, expected_benefit: "基础话机批量部署标准路径；证据归并 c05/p25/p26/n11/n12"}
  decision: verified

- id: f32
  title: ALE-x00 双分区切换状态图——Force Download 两态 × 切换时机
  type: framework
  V1: {passed: true, reason: "p188-194 状态图与 R200 分界齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "Force Download=NO 时切换会怎样", expected: "现场下载 SIP 二进制，切换明显变慢", observed: "p193-194 原文直接回答；n14 同源"}
  V3: {passed: true, expected_benefit: "批量切换窗口规划依据；证据归并 p27/g14/n14"}
  decision: verified

- id: f33
  title: ALE-x00 SIP 化两条开通路径 + 三种模式切换触发
  type: framework
  V1: {passed: true, reason: "p196-216 两路径三触发完整"}
  V2: {passed: true, check_mode: walkthrough, input: "200 台 NOE 话机批量切 SIP 用什么方法", expected: "DHCP 类挂 sipconfig.txt（前提无其他 NOE 设备）", observed: "p214 原文与 n15 边界一致"}
  V3: {passed: true, expected_benefit: "存量站点 SIP 化主力动作；证据归并 c06/p20/n13/n15"}
  decision: verified

- id: f34
  title: ALES 开通主线（PC/Android）——LDAP → 代理 → COS → DM profile → 建户 → 安装登录
  type: framework
  V1: {passed: true, reason: "p217-270 七段 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "ALES 登录用什么账号", expected: "login 须匹配 LDAP uid；外部认证密码留空", observed: "p230 原文直接回答；n16 同源"}
  V3: {passed: true, expected_benefit: "软终端交付主线；证据归并 c07/c08/p13/p28/n16/n17"}
  decision: verified

- id: f35
  title: swinst 认证管理菜单路径——LDAP/本地/OpenID 三入口与互斥切换
  type: framework
  V1: {passed: true, reason: "p225-226/p242-243 菜单路径逐级给出"}
  V2: {passed: true, check_mode: walkthrough, input: "从 LDAP 切回本地认证直接点开关行吗", expected: "不行——先停 LDAP 再启本地", observed: "p243 与 n18 三处 Warning 一致"}
  V3: {passed: true, expected_benefit: "认证方案切换的操作锚点；证据归并 c07 步骤 2/13/n18"}
  decision: verified

- id: f36
  title: 编解码协商决策链——系统 → 域 → DM → 终端 → 链路/网关 → 优先级排序
  type: framework
  V1: {passed: true, reason: "p272-281 五层决策链与优先级原文齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "系统关了 G722，外部网关开了有用吗", expected: "没用——系统级总闸压过一切", observed: "p281 与 n29（p274/p351）互证"}
  V3: {passed: true, expected_benefit: "音质/单向语音问题的根因层；证据归并 p30/p31/p47/n29/n30/n31/n46"}
  decision: verified

- id: f37
  title: SEPLOS 业务激活三型与 DTMF 三法——前缀/前缀+信息/后缀 + 183 开媒体
  type: framework
  V1: {passed: true, reason: "p304-310 三型示例与媒体机制齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "锁机前缀 45 拨完为什么会听到提示音", expected: "CS 以 183+SDP 开 RTP 放语音指南并收 DTMF", observed: "p305 原文直接回答；p32 同源"}
  V3: {passed: true, expected_benefit: "业务激活与 DTMF 排障依据；证据归并 p32/g48/g19"}
  decision: verified

- id: f38
  title: SIP 跟踪工具箱结构——motortrace/traced、oxetrace、mtracer、sipdump 四工具
  type: framework
  V1: {passed: true, reason: "p288/p312-327 四工具用法与菜单齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "给 ALE 支持提工单要带什么证据", expected: "oxetrace 自动打包 zip（三目录+pcap）", observed: "p315-316 与 c10 步骤 2-3 一致"}
  V3: {passed: true, expected_benefit: "升级工单的标配能力；证据归并 c10/p33/p34/n52"}
  decision: verified

- id: f39
  title: 外部网关进出呼叫判定流程——目的地三判 + 来源三判
  type: framework
  V1: {passed: true, reason: "p330-332 两步判定原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "改了域名后外线突然全断，查哪", expected: "ReqURI 域与 OXE_Address/Machine Name/域名拼接三条件", observed: "p330 与 n47 一致"}
  V3: {passed: true, expected_benefit: "外线判定与域名变更排障依据；证据归并 p35/n47"}
  decision: verified

- id: f40
  title: OTSBC 定位与部署主步骤——SBC 五职能 + 四段部署
  type: framework
  V1: {passed: true, reason: "p336-345 职能清单与部署四段齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "SBC 都帮我干什么", expected: "NAT 穿越/认证/消息适配/编解码转换/号码修改/加解密", observed: "p337 与 p341 用例动作一致"}
  V3: {passed: true, expected_benefit: "运营商接入与远程办公的公共底座；证据归并 g32/p39"}
  decision: verified

- id: f41
  title: OXE 侧 SBC 运营商接入配置主线——防火墙 → 系统参数 → TG → ExtGW → ARS → DID/NPD → 回拨
  type: framework
  V1: {passed: true, reason: "p347-363 七段 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "SIP 中继组不配 ARS 行吗", expected: "不行——ARS 是硬前提", observed: "p355 Warning 原文明确"}
  V3: {passed: true, expected_benefit: "外线交付的 OXE 侧全链；证据归并 c11/p35-p37/n28/n32/n33"}
  decision: verified

- id: f42
  title: OTSBC 向导步骤结构——八屏配置流 + 重启换 HTTPS
  type: framework
  V1: {passed: true, reason: "p368-373 八屏逐屏给出"}
  V2: {passed: true, check_mode: walkthrough, input: "向导跑完重启后进不了 Web 界面", expected: "换 HTTPS + 通用证书须手工接受", observed: "p373 Warning 原文明确；n34 同源"}
  V3: {passed: true, expected_benefit: "OTSBC 标准部署路径；证据归并 c12/p38/n34"}
  decision: verified

- id: f43
  title: OTSBC 排障修正三步——编解码放行 → 消息域改写 → 注册 Contact User
  type: framework
  V1: {passed: true, reason: "p374-383 三连排障叙事完整"}
  V2: {passed: true, check_mode: walkthrough, input: "来话一片空白没报错，查什么", expected: "SBC 未注册成功——补 Contact User 后 Register", observed: "p381-383 原文直接回答；n35 同源"}
  V3: {passed: true, expected_benefit: "SBC 调通的因果链教学；证据归并 c12/p38/n35/n36"}
  decision: verified

- id: f44
  title: 远程办公方案结构——ALES 两条路 + 话机两条路 + 原生加密
  type: framework
  V1: {passed: true, reason: "p384-420 方案矩阵与边界齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "500 个远程用户用内嵌反代行吗", expected: "行——≤500 用 OTSBC 内嵌 RP，更多用 NGINX PLUS", observed: "p387 原文明确；p40 同源"}
  V3: {passed: true, expected_benefit: "远程办公方案决策树；证据归并 p40-p45/n37-n42"}
  decision: verified

- id: f45
  title: 话机远程两用例时序——LAN→WAN 搬迁与 EDS 零touch
  type: framework
  V1: {passed: true, reason: "p400-406 两用例时序与限制齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "出厂话机寄到员工家怎么开通", expected: "EDS 零touch：联系 EDS 切 SIP 并取 RP 地址与根证书", observed: "p404-405 原文直接回答；p42/g34 同源"}
  V3: {passed: true, expected_benefit: "零touch 售前评估依据；证据归并 p42/g34/n37/n38"}
  decision: verified

- id: f46
  title: 远程办公证书四方信任链结构——话机/RP/SBC/OXE DM/EDS 五个信任库
  type: framework
  V1: {passed: true, reason: "p408-410 五库信任关系原文齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "远程话机握手失败怎么查", expected: "五方图逐库核对证书", observed: "p408-410 清单与 n41 一致"}
  V3: {passed: true, expected_benefit: "远程证书排障地图；证据归并 g09/g43/n41/n42"}
  decision: verified

- id: f47
  title: OTSBC 内嵌反代配置主线——TLS context → RP 三件套 → SBC 六对象 → 操纵与路由
  type: framework
  V1: {passed: true, reason: "p421-449 七段 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "RP 激活后配置不生效", expected: "必须重启 SBC", observed: "p431 原文明确；n34 同源"}
  V3: {passed: true, expected_benefit: "远程办公承载施工链；证据归并 c13/p39/p45/n34"}
  decision: verified

- id: f48
  title: ALES Remote Worker 配置与验证主线——DM profile(SBC) → 用户挂 profile → 异地登录
  type: framework
  V1: {passed: true, reason: "p450-458 四段 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "远程用户注册成功怎么看", expected: "sipregister 的 contact 指向 SBC LAN 地址", observed: "p458 输出样例直接回答；c14 步骤 7 一致"}
  V3: {passed: true, expected_benefit: "远程办公端到端验收；证据归并 c14/p41/n48/n49"}
  decision: verified
```

## 断言级裁决记录

1. **p04 容量表"Maximum 5000"归属不明**：成立。p68 原图中一处 "Maximum 5000" 标注在纯文本层无法确认归属对象，principle 提取器已照录并注明；引用容量数字时以六维上限与 15000 用户/20000 设备口径为准，不采信该孤立数值。详见 needs-review nr-01。
2. **p11 功能矩阵双列歧义**：成立。p99/p104 的"✓/空白"双列在纯文本层存在并列歧义（ALE-2 与 ALE-3 列分布、ALE-30 与 ALE-x00 视频列），条目内已注明以原文双列为准，不替原文补格子。详见 needs-review nr-02。
3. **CTL 目录两处写法**：成立。p171 写 /usr3/mao/DM/VHE8082，p166 写 /DHS3/data/mao/DM/VHE8082，判为同物异写（/DHS3/data 与 /usr3 为同一路径两种呈现）；能力卡统一用 p171 口径并注明。详见 needs-review nr-03。
4. **DID 翻译两套实验口径并存**：成立。ITSP1 腿（p41）33210N41000/范围 500 与 ITSP2 腿（p359）33920x31000/范围 1000 是两条运营商腿各自的口径，非矛盾；但极易混淆混配，转 needs-review nr-04 提示。
5. **原文笔误两处**：p358 "EXISITING"（应为 EXISTING）、p239 "Cicular"（应为 Circular），照录不改动，转述用正确拼写。详见 needs-review nr-05。
6. **无 rejected 断言**：软件锁 177/345/430（p67）、容量六维（p68）、中继组 62 通道/992 TS（p86/p363）、注册租期 1800/86400（p88）、密码策略六条（p114）、监督 30000/40 与事件码 510-513（p130/p133）、编解码六级优先序（p281）、RP 规模 ≤500（p387）、零touch 四限制（p404）、端口 5261/6000-6399（p439-440）等关键数字均与原文逐格一致。
