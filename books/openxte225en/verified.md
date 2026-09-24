# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f18（主验证对象）；principle p01-p32 / case c01-c10 / counter-example n01-n35 作为各单元的证据素材归并；glossary g01-g62 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 287 页全文通读 + 提取器页码证据交叉核对

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 16 | f01, f04-f18 |
| reference | 2 | f02（RLAB 平台结构）、f03（POD 虚机清单与账号总表，教学专用基础设施） |
| needs_review | 0（单元级） | 断言级 4 项转 needs-review.md（原文笔误 n29、矩阵转写风险、工程引申、容量缺位归纳） |
| rejected | 0 | 无编造断言；端口矩阵、DAS 条数、游牧公式、APNS 端口逐格核对一致 |

verified 明细：f01, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18

## 验证记录

```yaml
- id: f01
  title: 全书章节推进逻辑——讲义/How-To 成对，先边缘后客户端
  type: flow
  V1: {passed: true, reason: "p1-287 十四个知识域区间逐段核对，与 BOOK_OVERVIEW 骨架一致"}
  V2: {passed: true, check_mode: walkthrough, input: "新项目按什么顺序交付远程接入", expected: "证书→服务器申报→OTSBC→反代→客户端的顺序", observed: "p47-144 部署链章序与 p145-217 客户端章序支持该顺序，无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免先配客户端后建边缘的倒置"}
  decision: verified

- id: f02
  title: RLAB 远程实验平台——POD 池 + 三种学员接入拓扑
  type: structure
  V1: {passed: true, reason: "p4-10 拓扑三选一与 POD 结构完整"}
  V2: {passed: true, check_mode: walkthrough, input: "实验环境怎么接入", expected: "教室 RAP/RAP 话机/HTTPS 直连三选一", observed: "p4-8 三拓扑与 POD 独立性一致"}
  V3: {passed: true, expected_benefit: "仅培训环境认知；生产不复用，作 Boundary 背景与 book/overview 素材"}
  decision: reference

- id: f03
  title: 每 POD 虚机清单、Eco-system 角色与 DNS 域（实验口径）
  type: structure
  V1: {passed: true, reason: "p11-22 虚机地址表逐行核对；p30 账号口令总表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Eco-system 承担哪些角色", expected: "DNS/Exchange/AD/LDAP/手机 DHCP/CA 六角色", observed: "p19 原文六角色一致；域名 company.com（p21）一致"}
  V3: {passed: true, expected_benefit: "实验跟做与排障对照基准；凭据值仅进 book/overview 与 Boundary，不进能力卡正文"}
  decision: reference

- id: f04
  title: 设备 DHCP 池、用户编号计划与 SIP 模拟器号码变换规则
  type: diagram
  V1: {passed: true, reason: "p23-29 编号三层逐条核对；p27/p29 变换示例原文一致"}
  V2: {passed: true, check_mode: drill, input: "拨 0678931001 落到哪、主叫显示什么", expected: "分机 31001、主叫 0298131000", observed: "与 p27 原文示例逐格一致；国际格式 0044123431001、主叫 33298131000 与 p29 一致"}
  V3: {passed: true, expected_benefit: "task-14 拨测的预期结果表；证据归并 p09/p10/n29/n31"}
  decision: verified

- id: f05
  title: 远程接入需求三分类与总拓扑——DMZ 双边缘 + VPN 备选
  type: diagram
  V1: {passed: true, reason: "p33-36 三类需求与拓扑图完整；p35 脚注双标注原文一致"}
  V2: {passed: true, check_mode: walkthrough, input: "外部客户要进会议走什么通道", expected: "经 DMZ Edge Servers（RP+OTSBC）", observed: "p35-36 拓扑与脚注支持；VPN 仅标 technological alternative 不展开"}
  V3: {passed: true, expected_benefit: "方案沟通的架构底座；证据归并 p01"}
  decision: verified

- id: f06
  title: RP 与 OTSBC 职责分工——Web 服务通道 vs SIP/媒体通道
  type: diagram
  V1: {passed: true, reason: "p37-39/p81/p121-123 特性清单三处互证一致"}
  V2: {passed: true, check_mode: walkthrough, input: "桌面共享流量和 SIP 信令各走谁", expected: "协作/Web 服务走 RP，SIP/RTP 走 OTSBC", observed: "p37 职责句 + p81 ToIP 特性清单支持；兼任时认证需另配服务器（p37/p140）"}
  V3: {passed: true, expected_benefit: "组件选型与排障分流的概念依据；证据归并 p02/n24"}
  decision: verified

- id: f07
  title: 客户端×边缘组件用例矩阵（含 N.U./N.A. 语义）
  type: structure
  V1: {passed: true, reason: "p40-42/p82/p122 三张矩阵口径一致，符号定义 p82 原文"}
  V2: {passed: true, check_mode: drill, input: "OTC PC One 要不要配 SBC", expected: "N.U.——无 VoIP 可代理，仅需 RP", observed: "p82 N.U 定义原文一致；与 n24 语义澄清互证"}
  V3: {passed: true, expected_benefit: "给某类用户报边缘组件清单的查表依据；证据归并 n24"}
  decision: verified

- id: f08
  title: DNS 双侧解析结构与 conference FQDN 特例
  type: diagram
  V1: {passed: true, reason: "p43/p85/p124-125 双 DNS 布局三处一致"}
  V2: {passed: true, check_mode: walkthrough, input: "同一个 OT FQDN 内外各解析到哪", expected: "内部到私网 IP、公共到 RP 公网 IP；OTSBC WAN 侧仅公共 DNS 申报", observed: "p43/p85 原文一致；conference FQDN 内部解析到会议簇 IP 一致"}
  V3: {passed: true, expected_benefit: "DNS/NAT 规划输入；证据归并 p07/n03/n32"}
  decision: verified

- id: f09
  title: 证书体系——三来源、两封装、远程访问两案例
  type: structure
  V1: {passed: true, reason: "p44-61 证书讲义完整；p50/p58-59 结构原文一致"}
  V2: {passed: true, check_mode: walkthrough, input: "自签证书能不能用于远程访问", expected: "不能——远程访问必须 CA 签发", observed: "p53 Required for remote accesses + p61 官方反对预载通用证书（p03/n01）"}
  V3: {passed: true, expected_benefit: "证书策略红线与布局选型；证据归并 p03/p04/p05/p16/n01/n04/n05"}
  decision: verified

- id: f10
  title: OpenTouch 服务器侧远程访问设置三段流程
  type: flow
  V1: {passed: true, reason: "p62-77 How-To 完整；p63/p67 关键句原文一致"}
  V2: {passed: true, check_mode: walkthrough, input: "客户端从公网回连的 URL 从哪来", expected: "RP 申报的四个公共 URL 写入配置", observed: "p63 API/EVS(:8016)/ACS/DMS 四 URL 一致；OTSBC 申报 5261/8061（p64-66）一致"}
  V3: {passed: true, expected_benefit: "服务器侧闭环的施工顺序；证据归并 p06/p07/c01/n02/n03"}
  decision: verified

- id: f11
  title: OTSBC 配置结构总览（IPG/Media Realm/端口矩阵）与部署主步骤
  type: structure
  V1: {passed: true, reason: "p86-88 配置结构逐格核对；端口与网段为实验口径已标注"}
  V2: {passed: true, check_mode: walkthrough, input: "向导能生成什么、还缺什么", expected: "IPG/Media Realm/接口模板全生成；OXE 侧 TCP 与 iPhone 对象要手工", observed: "p86 结构 + p105/p117 手工警告一致（p13/p14）"}
  V3: {passed: true, expected_benefit: "OTSBC 部署清单骨架；证据归并 p11-p15/c02/n06-n08"}
  decision: verified

- id: f12
  title: 反向代理两条部署路线——OTSBC 内嵌（7.2+）与独立 Nginx VM
  type: structure
  V1: {passed: true, reason: "p128-130 两路线对象清单原文一致；模板文件名与可选性核对无误"}
  V2: {passed: true, check_mode: walkthrough, input: "已有 OTSBC 且许可允许，反代怎么选", expected: "内嵌省一台机器；需独立扩展或 LDAP 认证专用机时选 Nginx", observed: "p128 内嵌前提 + p129 独立路线 + p140 认证专用机警告支持"}
  V3: {passed: true, expected_benefit: "反代选型与两条施工入口；证据归并 p17-p20/c03/c08/n09/n10/n25/n26/n28/n35"}
  decision: verified

- id: f13
  title: 客户端远程接入两步法——接入配置 + 路由档案
  type: flow
  V1: {passed: true, reason: "p147-150 两步法定义与特例规则原文一致（p147/p150 两处重复强调）"}
  V2: {passed: true, check_mode: walkthrough, input: "手机上点联系人为什么还是手机出话", expected: "手机发起拨打永远本机发话，dial from 不影响", observed: "p147 原文一致；与 n11 误解澄清互证"}
  V3: {passed: true, expected_benefit: "用户侧第一步与高频误解排障；证据归并 p21/n11"}
  decision: verified

- id: f14
  title: OTC PC 远程工作者两模式对比——multi-devices 副设备 vs Nomadic SIP 池
  type: structure
  V1: {passed: true, reason: "p151-157/p204 两模式定义与前提原文一致"}
  V2: {passed: true, check_mode: walkthrough, input: "在家用 PC 接听、主话机保留，选哪条路", expected: "multi-devices 副设备；要求 COS 与两前缀前提", observed: "p152 定义 + p152-153 前提清单一致；Nomadic 走池化冻结（p157）对照"}
  V3: {passed: true, expected_benefit: "PC 远程形态选型与容量规划；证据归并 p22/p23/c04/c05/n12-n15"}
  decision: verified

- id: f15
  title: 智能手机连接模式矩阵——WiFi/3G4G/DTMF 回落 × Android/iPhone
  type: structure
  V1: {passed: true, reason: "p166-177 场景五分与汇总表核对；汇总表部分格转写风险转 needs-review（nr-05）"}
  V2: {passed: true, check_mode: drill, input: "手机没有数据连接还能干什么", expected: "DTMF 回落：打/挂电话、留言、有限路由", observed: "p175-176 回落能力清单原文一致；Android 无 SIM 代价三项（p176/n23）一致"}
  V3: {passed: true, expected_benefit: "移动方案能力边界沟通；证据归并 n23"}
  decision: verified

- id: f16
  title: 智能手机自动配置对象流——关联一次，OXE 自动建对象（按模式增减）
  type: flow
  V1: {passed: true, reason: "p178-181/p196-198/p207-211 流程与矩阵原文一致"}
  V2: {passed: true, check_mode: walkthrough, input: "关联手机后还要手工做什么", expected: "Entity 判别器关联 + 公网接入 COS 区域授权两项", observed: "p212 两处 Warning 一致；自动对象矩阵 p181 逐格核对（p26）"}
  V3: {passed: true, expected_benefit: "智能手机开通核验清单；证据归并 p24-p29/p32/c06/n19-n22/n34"}
  decision: verified

- id: f17
  title: iPhone APNS 推送来话流程与 VoIP everywhere 组件
  type: diagram
  V1: {passed: true, reason: "p183-188 机制链与组件原文一致；p184 端口表逐格核对"}
  V2: {passed: true, check_mode: walkthrough, input: "iPhone 后台收不到来话查什么", expected: "APNS 证书/hotfix、四端口放行、kamailio-wasp 状态", observed: "p183-184 证书年更机制 + p186 UDP/TCP 约束 + p187 组件职责一致"}
  V3: {passed: true, expected_benefit: "iPhone 场景必答题与运维抓手；证据归并 p30/c07/n06/n17/n18"}
  decision: verified

- id: f18
  title: Nginx RP 文件/组件结构——三份 conf + snippets + LDAP 认证模块
  type: structure
  V1: {passed: true, reason: "p251-259 文件清单与行号核对；OT 2.2 双 conf 规则原文一致"}
  V2: {passed: true, check_mode: walkthrough, input: "OT 2.2 后只改 remoteworker.conf 行吗", expected: "不行——conference.conf 必须同改", observed: "p253 原文一致；LDAP 模块 Python 2 only（p257）一致"}
  V3: {passed: true, expected_benefit: "Nginx 施工清单与版本陷阱；证据归并 p19/p20/n25/n26/n28/n29/n35"}
  decision: verified
```

## 断言级裁决记录

1. **counter-example 提取器 n29 四处笔误**：成立并集中登记——p229 网关两处不一致、p250/p254 /etc/inid.d/、p156 otsbx-podx、p214 https// 缺冒号；详见 needs-review nr-01~nr-04。
2. **f15 附带条件"iPhone 汇总表部分格未打勾"**：成立，属表格截图转写风险，引用以原表为准；转 needs-review nr-05。
3. **n13/n18 含轻度工程引申**（池空后果"无法游牧"、漏接排查指向）：机制与依据均出自原文，引申部分引用时带标注；转 needs-review nr-06。
4. **n30 容量缺位**：为全书级归纳性结论（CAC 无阈值、游牧池无算例、带宽无口径），非编造，引用标"书外/以 sizing 工具为准"；转 needs-review nr-07。
5. **数字复核一致**：端口规划（公网 443/8016、OTSBC 5261/8061/5265、RTP/SRTP 7000-7499）、DAS 规则（游牧新增 4 条 + 会议域 10 条示例）、游牧公式（1 并发 = 1 SIP 设备 + 1 Ghost Z）、APNS 四端口（TCP 5223/2195/2196/443）、速拨号范围约束（不为 0 不满）、版本坐标（R2.0/R2.2/R2.3.1/R2.5/R2.6、OTSBC 7.2、Mediant 7.2、ESXi 6.0/6.5、Ubuntu 16.04.3 LTS）——全部与 candidates 原文逐格一致。
6. **glossary 候选 g01-g62 不进 verified**：按口径直接转 GLOSSARY（六域分组），落位说明见 references.md。
