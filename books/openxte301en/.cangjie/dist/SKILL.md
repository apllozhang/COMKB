---
name: opentouch-advanced
description: |
  OpenTouch 与 OXE 高级特性的交付与排障支持：Nomadic 移动与 Ghost Z 资源池、Desksharing、OTC 智能手机（REX/DISA/APNS）、远程接入通道与证书、统一消息（Exchange/O365/Gmail/IMAP）、目录搜索与 Single Business Card、协作会议、日历在场与同步、外部认证（LDAP/RADIUS/Kerberos）。适用于 OpenTouch R2.6.x 时代的配置、选型、排障与方案问答； 容量算例、非法国号码计划与生产安全加固不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.opentouch-advanced
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
# OpenTouch - Advanced (Participant's Guide, Edition 08) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 容量规划算例（Ghost Z 池、会议端口、DCS 吞吐书内只有"按并发规划"一句话，无算例）
- 非法国号码计划方法论（DAS/ARS/DID 仅 +33/00/0 口径，他国需自行推导）
- 高可用、安全加固、企业 IAM 治理细节（ICEaccess 账号治理等仅一句话级提示）
- Teams/Skype for Business 集成细节、eSIM/5G/MDM、新版浏览器矩阵（2019 年生态，按最新文档重核）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 分工：OXE 保留呼叫控制与话机生态，OpenTouch 服务器承载协作、消息、移动性与目录；客户端统一从 OT 拿服务
2. Nomadic 的本质是资源池换轨：每路蜂窝连接占 1 个 Ghost Z、每路 VoIP 连接占 1 个 Ghost Z 加 1 个 SIP 设备，占住直到用户关闭 nomadic——并发数决定池规模
3. 远程接入三件套：数据面走反向代理（443/8016），SIP/媒体走 OTSBC（5261/8061/7000-7499），号码格式靠 DAS 正则串行处理——顺序错一条全盘错；会议 FQDN 必须进两张证书 SAN
4. 统一消息把语音留言变成邮件：四后端能力递减（Exchange 全功能、O365 桌面版、Gmail 限 500 用户、IMAP4 砍四项）；Exchange 侧钥匙是 ICEaccess 特权账号加 Impersonation 加 CA 证书
5. 目录搜索永远查同步库：UDAS 单向同步进 PostgreSQL，同步三参数不设就是空库；合并按权重、Merge keys 至少姓加名、照片 Avatar 优先
6. 外部认证是全局开关：downstream（LDAP/RADIUS 插件）与 upstream（Kerberos）两条路，启用前管理员必须先配好 External login，否则把自己锁在配置工具外面
7. 实验环境口径：教材密码、账号、号码与网段仅限实验；生产必须全部替换并对照最新 release note（版本碎片化 R2.0-R2.6）

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 配置 OpenTouch 远程接入；声明反向代理与 OTSBC；会议邀请链接打不开；证书签发与部署；DAS 规则配置；reverse proxy declaration | references/capabilities/ota-remote-access.md | references/capabilities/ota-smartphone-rex.md、references/capabilities/ota-nomadic-ghost-z.md |
| 配置 Nomadic 蜂窝模式；配置 Nomadic VoIP 模式；Ghost Z 资源池规划；nomadic 资源核查维护；activate nomadic mode | references/capabilities/ota-nomadic-ghost-z.md | references/capabilities/ota-remote-access.md、references/capabilities/ota-desksharing.md |
| 交付 OTC 智能手机；配置远程扩展与 DISA；核验自动创建对象；iPhone 推送排障；smartphone deployment | references/capabilities/ota-smartphone-rex.md | references/capabilities/ota-remote-access.md、references/capabilities/ota-extended-mobility.md |
| 部署统一消息；选择 UM 邮件后端；配置 Exchange Impersonation；语音邮箱档案与信箱；unified messaging setup | references/capabilities/ota-um-exchange-integration.md | references/capabilities/ota-calendar-sync.md |
| 配置会议服务器；建会议桥号；会议角色与密码管理；协作能力限制；conference server setup | references/capabilities/ota-conference-collaboration.md | references/capabilities/ota-dcs-documents.md、references/capabilities/ota-otc-web-guest.md |
| 实施 Calendar presence；实施 Calendar synchronization；日历在场排障；会议双向同步验证；calendar synchronization | references/capabilities/ota-calendar-sync.md | references/capabilities/ota-um-exchange-integration.md |
| 部署目录搜索；配置目录同步；启用 Single Business Card 合并；联系人照片与可选属性；UDAS directory search | references/capabilities/ota-directory-udas.md | references/capabilities/ota-enterprise-authentication.md |
| 配置 LDAP/RADIUS 外部认证；启用 Kerberos 单点登录；外部认证排障与级联；WBM 管理员保护；external authentication setup | references/capabilities/ota-enterprise-authentication.md | references/capabilities/ota-directory-udas.md |
| 配置共享工位；DSU 登录登出管理；OTC PC 远程释放；desksharing maintenance | references/capabilities/ota-desksharing.md | — |
| 部署 Extended Mobility 标签；QR 码与 NFC 标签制作；呼叫切换测试；extended mobility deployment | references/capabilities/ota-extended-mobility.md | — |
| 安装 DCS 文档转换服务器；Office 文档会议演示；DCS 排障；document conversion setup | references/capabilities/ota-dcs-documents.md | — |
| 访客浏览器入会；OTC Web 能力边界确认；WebRTC 音频接入；guest browser join | references/capabilities/ota-otc-web-guest.md | — |
| 搭建核对实验 POD；解读书中实验环境值；ITSP1 模拟器联调；rlab pod configuration | references/capabilities/ota-lab-pod.md | — |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 需要生产网络数值或最新兼容矩阵 → 指向 TC2341/TC2391/TC2258/TC2558/TC1623 与最新 release note，不以实验口径搪塞
- 版本敏感行为（R2.0/R2.2/R2.3.1/R2.6 分界）→ 按章内版本口径回答并提示跨版本核对（needs-review nr-07）
- LDAP 上限引用 → 按"OXE 侧 5 个"口径并注明 p235/p260 双口径冲突（nr-01），不二选一冒充原文
- 涉及 RLAB/SIP 模拟器环境搭建 → 参考 book/overview 环境区背景，不虚构生产配置
