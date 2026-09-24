# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f20（主验证对象）；principle p01-p47 / case c01-c22 / counter-example n01-n50 作为各单元的证据素材归并；glossary g01-g58 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 468 页全文页码证据交叉核对（关键数字已对 source_fulltext.txt 逐格抽查）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 18 | f01, f04-f20（详见下表） |
| reference | 2 | f02（RLAB POD 拓扑，教学专用基础设施）、f03（ITSP1 模拟器，教学专用） |
| needs_review | 0（单元级） | 断言级 5 项转 needs-review.md（LDAP 上限双口径、tsa_maintenance 菜单缺项、RADIUS 章笔误、POD IP 排版、拼写印误） |
| rejected | 0 | 无编造断言；端口表、Ghost Z 定量、DAS 10 条、DTMF 码表等关键数字逐格核对一致 |

verified 明细：f01, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20

reference 处置理由：f02/f03 描述的是 RLAB 培训专用基础设施（POD 虚机表、SIP 模拟器号码规则），BOOK_OVERVIEW 已明确"仅作 Boundary 背景与实验口径引用，不入册"；由 ota-lab-pod 路由卡承接（证据 c01/p06/p07），不进入 promoted 知识域。

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——实验地基 → 移动性 → 消息/目录 → 协作 → 安全认证
  type: framework
  V1: {passed: true, reason: "p3-468 章节编排完整；11 主题域每章“讲义+How-To”配对可逐一指认"}
  V2: {passed: true, check_mode: walkthrough, input: "按什么顺序交付 OT 高级特性", expected: "先打通道再配终端再接企业系统", observed: "远程接入(p103)先于 nomadic/手机(p31-167)，邮件/目录(p168-263)与认证(p415-467)收尾，依赖链自洽（VoIP nomadic 以 cellular 为前提 p51、Kerberos 前置管理员 p452）"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免'先配手机后通远程接入'的倒置"}
  decision: verified

- id: f04
  title: Connection 用户三操作模式表与 Nomadic 双模式机制
  type: framework
  V1: {passed: true, reason: "p34 服务定义与冻结口径、p44 三模式总表、p46 双模式划分齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "远程员工怎么保留完整话机体验", expected: "nomadic 改道且办公话机冻结", observed: "p34 'frozen and disabled' 与 p44 Modes 表、p46 cellular/VoIP 两分法一致；激活入口 OTC PC routing 窗口明确"}
  V3: {passed: true, expected_benefit: "移动性主线的概念基座；证据归并 p01/p02/p03/g04/n01"}
  decision: verified

- id: f05
  title: Nomadic 资源池机制——Ghost Z 池与 SIP 设备池的定量关系
  type: framework
  V1: {passed: true, reason: "p47 蜂窝 1 Ghost Z/连接、p51 VoIP 1 Ghost Z + 1 SIP 设备/连接，两处口径一致"}
  V2: {passed: true, check_mode: walkthrough, input: "50 个并发 nomadic 用户要规划多少资源", expected: "蜂窝 50 个 Ghost Z；VoIP 50+50", observed: "p47 'quantity must equal the number of Ghost Z sets' 直接可答；占线至关闭 nomadic 的释放规则（p47/p51）支撑池规模=并发数"}
  V3: {passed: true, expected_benefit: "全书最核心的容量公式；证据归并 p01/n05/g05/c02-c04"}
  decision: verified

- id: f06
  title: Desksharing 机制——DSU/DSS 结构与 OTC PC 增强
  type: framework
  V1: {passed: true, reason: "p59 DSU/DSS 定义、p60 远程释放、p61 UA 替代三层齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "共享工位用户怎么用任意话机", expected: "DSU 凭 600/601+密码登录登出任意 DSS", observed: "p59 定义与 c05 前缀实验互证；nomadic 兼容路径（UA 软话机替代、不冻结话机 p61）与 c02 冻结口径区分清楚"}
  V3: {passed: true, expected_benefit: "共享工位场景的机制底座；证据归并 p04/p05/c05/c06/n04/n06/n07"}
  decision: verified

- id: f07
  title: OTC 智能手机配置原理——9 对象清单与自动创建边界
  type: framework
  V1: {passed: true, reason: "p92 复杂度定位、p94 自动创建清单、p95 按模式矩阵、p96 R2.6 单设备化完整"}
  V2: {passed: true, check_mode: walkthrough, input: "关联手机后管理员还要手工做什么", expected: "核验自动对象、补 Entity 识别码与公网 COS", observed: "p94 九对象与 p142 两处 Warning（识别码选择器/barring 放行）互补，c11 逐项核验步骤落地"}
  V3: {passed: true, expected_benefit: "智能手机交付复杂度的分解框架；证据归并 p09-p11/c09-c11/n12-n15/n43"}
  decision: verified

- id: f08
  title: iPhone/APNS 推送与 VoIP everywhere 架构（kamailio-wasp + wspcfg + 5265 SBC）
  type: framework
  V1: {passed: true, reason: "p97 推送链、p98 端口与证书、p99-100 协议口径、p101-102 组件与 5265 齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "iPhone 收不到推送先查什么", expected: "防火墙四端口 + APNS 证书有效期", observed: "p98 端口表（5223/2195/2196/443）与一年期 hotfix 口径直接可答；kamailio-wasp 服务与日志路径（p147）可执行"}
  V3: {passed: true, expected_benefit: "iPhone 特例全家桶的排查地图；证据归并 p12/p13/n50/g33/g34"}
  decision: verified

- id: f09
  title: OpenTouch 远程接入拓扑——反向代理 / OTSBC / NAT/DNS 三层结构
  type: framework
  V1: {passed: true, reason: "p104-107 四个公共 URL、NAT 端口表、DNS 条目逐项给出"}
  V2: {passed: true, check_mode: walkthrough, input: "远程 OTC 客户端从哪个通道进来", expected: "数据面走 RP 443/8016，SIP/媒体走 SBC 5261/8061/7000-7499", observed: "p104-107 与 p14 端口总表一致；URL/FQDN 写入客户端配置文件的闭环（p105/p106 Notes）成立"}
  V3: {passed: true, expected_benefit: "一切远程特性的通道底座；证据归并 p14/c07/g27/g28/g53"}
  decision: verified

- id: f10
  title: ACS 会议服务 FQDN 与证书生命周期（验证 → rehost → CSR → CA → 导入 → 部署）
  type: framework
  V1: {passed: true, reason: "p109 SAN 警告、p110-111 rehost、p112-117 CSR/CA/导入/部署六步连贯"}
  V2: {passed: true, check_mode: walkthrough, input: "会议邀请链接内网打得开外网打不开", expected: "查 conf FQDN 是否同时入 RP 与 OT 两张证书 SAN", observed: "p109 Warning 直接命中；rehost（p111）与内部 DNS 前置（p110/p111 Warning）链条完整；Deploy 断会话属正常（p117）防误判"}
  V3: {passed: true, expected_benefit: "证书与会议 FQDN 的全生命周期操作链；证据归并 p37/c08/n09-n11"}
  decision: verified

- id: f11
  title: UM 四种邮件后端架构与能力递减谱系
  type: framework
  V1: {passed: true, reason: "p170 单点存储 Wav、p175-177 四后端、p178 兼容表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户坚持用 Gmail 存语音留言行不行", expected: "行但限 500 用户，OAuth 2.0 接入", observed: "p176 上限与 p181 OAuth 三件套一致；IMAP4 砍 PPR/扩展/MWI/消息类别（p177）支撑选型递减谱系"}
  V3: {passed: true, expected_benefit: "UM 后端选型矩阵；证据归并 p30-p33/c13/c14/n18-n20/n23/n44"}
  decision: verified

- id: f12
  title: UDAS 同步与合并目录结构——同步库、联系人卡、照片优先级
  type: framework
  V1: {passed: true, reason: "p220 模块定位、p222 单向同步、p224 联系人卡结构、p226-230 合并与照片齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "搜不到人第一排查项是什么", expected: "同步参数（date/time/period≥1）与同步库状态", observed: "p222 'searches are made in the synchronized database' 与 p244 Tips 硬规则互证；照片三级优先（p230）可执行核验"}
  V3: {passed: true, expected_benefit: "目录域的数据流底座；证据归并 p20-p23/c15/n24/n25/g12/g13"}
  decision: verified

- id: f13
  title: 会议三类型与角色权限体系（ad-hoc / scheduled / reservationless）
  type: framework
  V1: {passed: true, reason: "p266 双访问码、p267-269 三类型、p270-271 角色权限与 DTMF、p330-331 矩阵完整"}
  V2: {passed: true, check_mode: walkthrough, input: "普通参会人能共享桌面吗", expected: "不能——参与者无演示/邀请/控制权", observed: "p270 'PARTICIPANTS CANNOT' 清单直接可答；7 位双码制（p266）与 c17 预约流程互证"}
  V3: {passed: true, expected_benefit: "协作主线的权限治理底座；证据归并 p15/p16/p40/n48/c16/c17"}
  decision: verified

- id: f14
  title: 视频会议架构——AMS 媒体服务器与 Dial by URI
  type: framework
  V1: {passed: true, reason: "p273 MCU 定位与 Active talker 限制、p274 用户类型分界、p295-296 URI 架构完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要多方同屏（continuous presence）", expected: "内置 AMS 做不到，需另寻方案", observed: "p273 'no continuous presence' 与 n26（Radvision/LifeSize 淘汰）一致；Connection 用户视频受限（p274）支撑需求分界"}
  V3: {passed: true, expected_benefit: "视频方案的边界清单；证据归并 n26/n27/g30/g46/p14"}
  decision: verified

- id: f15
  title: DAS 规则处理流程与法国 10 规则集
  type: framework
  V1: {passed: true, reason: "p299 规则定义（≤20 条串行）、p301 三段管线、p108/p317-318 法国 10 条、p303 元字符速查齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "拨 0041123456789 经 ACS 后变成什么", expected: "系统选项层先转 +41123456789，再走 DAS 规则链", observed: "p302 五类输入实例与 p317 规则链（③s/^\\+00/+/）逐段互证；顺序重要与多条同中（p108 Warning）确认"}
  V3: {passed: true, expected_benefit: "拨号格式排障的两层定位法；证据归并 p43/p44/n08/n45/c08/c16"}
  decision: verified

- id: f16
  title: OTC Web 定位、能力边界与 WebRTC 架构
  type: framework
  V1: {passed: true, reason: "p323-324 定位与匿名入会、p332 架构、p333-334 部署要求与限制清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "外部访客不装客户端能入会吗", expected: "能——浏览器匿名入会、凭访问码定角色", observed: "p323-324 与 p355 回呼链接互证；'No white board / poll / recording / video'（p334）界定期望"}
  V3: {passed: true, expected_benefit: "访客入会方案的验收边界；证据归并 n29/p29/c17"}
  decision: verified

- id: f17
  title: DCS 两模式与安装形态（Basic/Advanced × 内部 KVM/外部 VM 或 PC）
  type: framework
  V1: {passed: true, reason: "p365 Basic 边界、p367-368 两形态、p370-371 兼容矩阵、p373 ESXi 约束齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "Office 文档在会议里演示不了", expected: "Basic 模式只支持 pdf/图片，Office 需装 DCS", observed: "p365 与 p344 一致；'文档卡 queued'根因（p375 许可/更新）指向 Windows 侧而非 ACS 配置"}
  V3: {passed: true, expected_benefit: "会议文档能力的补全路径；证据归并 p34-p36/c18/n30/n31"}
  decision: verified

- id: f18
  title: Calendar presence / Calendar synchro 机制与状态优先级
  type: framework
  V1: {passed: true, reason: "p387 旁注文本定义、p389 五态优先级、p390-392 同步机制与周期会议限制齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "为什么在场颜色码没跟着日历变", expected: "presence 只加文本不改颜色", observed: "p387 原文直接回答；TC2258 补充四条预期差（自己看不到自己/FREE 仅名片/不改颜色/OOO 优先）闭环"}
  V3: {passed: true, expected_benefit: "日历增值特性与高频排障依据；证据归并 p18/p19/p46/c19/n32-n34/n46"}
  decision: verified

- id: f19
  title: 外部认证架构——Downstream/Upstream 双轨与插件级联
  type: framework
  V1: {passed: true, reason: "p417 DTA、p418 Downstream、p427 Upstream、p421-426 插件链与作用域完整"}
  V2: {passed: true, check_mode: walkthrough, input: "能不能只给 OTC PC 单独开 LDAP 认证", expected: "不能——外认对所有应用全局生效", observed: "p426 作用域原文直接回答（IP Touch/TUI 除外）；级联不对称（Web 回 DTA、厚客户端不级联）支撑维护窗口预告"}
  V3: {passed: true, expected_benefit: "安全集成的影响评估框架；证据归并 p25/p26/p29/n35-n40/n47/c20-c22"}
  decision: verified

- id: f20
  title: Kerberos SSO 流程与四件套配置（web.xml/krb5.conf/auth.config/keytab）
  type: framework
  V1: {passed: true, reason: "p429 票据流、p428/p445 web.xml 模板、p446-448 三件路径与 ktutil 命令、p450-454 AD 侧与 WBM 保护完整"}
  V2: {passed: true, check_mode: walkthrough, input: "启用 Kerberos 后 8770 客户端进不了 WBM", expected: "预留 External login 指向 AD 的 WBM 管理员", observed: "p430/p452/p454 三处一致（Application=WBM + Delegate authentication）；keytab 密码一致性（p450 Warning）与 SPN 两条命令（p451）可执行"}
  V3: {passed: true, expected_benefit: "高风险变更的保命流程；证据归并 p27/p28/n37-n40/c21/g40"}
  decision: verified
```

## 断言级裁决记录

1. **LDAP 溢出容量两处口径冲突**：成立并如实记录（讲义 p235 "20 LDAP servers maximum" vs 实验 p260 "Up to five LDAP servers / phone book index 1-5"）。实践口径按实验页 5 个做 OXE 侧上限、20 的适用语境存疑；详见 needs-review nr-01（候选 p24/n42）。
2. **tsa_maintenance "option 47" 在所列菜单中不存在**：成立。p57 原文提示用 option "47" dump all QMCDU 或 option "20" dump nomadic，但同页 ACAPI 子菜单仅列 0-20 且无 47，疑为原文笔误；核验动作按 option 20 执行（候选 p47/c04），详见 needs-review nr-02。
3. **RADIUS 章 Notes 复制粘贴错误**：成立。p459 Notes 写"连接 LDAP 目录所需参数"，页面实际内容为 plugin_radius.properties（RADIUS 参数）；以文件名与参数名为准（候选 p26/n47），详见 needs-review nr-03。
4. **POD 服务器 IP 排版异常**：成立。p9/p17 两处印作 "192.16.8.1.1 / 192.16.8.1.3"（同网段其余地址均为 192.168.1.x），疑为排版变体，原文如此照录、引用时标注（候选 p06），详见 needs-review nr-04。
5. **无 rejected 断言**：端口表（443/8016/5261/8061/5265/7000-7499/5060/5260）、Ghost Z 定量（1 与 1+1）、Desksharing 前缀（600/601）与 6004 事件、DISA 前缀 31280、秘密码 2998、Gmail 500 用户、DTMF 码表（##1/##3/##4/##91/##92/##93）、DAS 法国 10 条逐条、merge keys ≥2、照片三级优先、同步 period≥1/merge period≠0——均与原文逐格一致。
