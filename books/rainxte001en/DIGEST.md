# DIGEST — Rainbow OXO Connect 集成精华长文

> 源：RAINXTE001EN Edition 13（251 页）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 Rainbow 混合云集成的全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

Rainbow 是 ALE 的云协作平台（UCaaS 协作/云话音 + CPaaS 开放 API），与 OXO Connect 是**混合云关系**：PBX 保留呼叫控制和现场话音，Rainbow 提供聊天、会议、移动端和云服务，中间靠一条 WebRTC 网关打通音频。

整本教材就是一条交付主线：**云侧开户 → PBX 接入 → 分机关联（RCC）→ 网关解锁完整音频 → 话务台/Teams 等增值场景**。

三个数字先记住：

| 数字 | 含义 |
|---|---|
| Business / Enterprise / Attendant | 电话服务必须付费订阅，免费 Essential 不行 |
| BP 专属 | 建 PBX 和开付费订阅只有经销商能做 |
| 50 / 20 / 150 | 网关通话上限：外部拓扑 50、OCE 集成与 Front End 20、用户上限 150 |

## 二、云侧三件套：公司、订阅、成员

- **公司（Company）**：一切功能的挂靠单元。BP 建客户公司，客户管理员管日常。可见性四级拿不准就 CLOSED（教材原话"建司即设"）；ISOLATED 别乱用——用户会无法被外部会议邀请。
- **认证**：两条路——SSO（Azure AD-SAML/OIDC、ADFS-SAML，管理员须 Enterprise 级）或本地密码（≥12 位含大写/数字/特殊字符）+ TOTP（推荐管理员）。
- **订阅**：先由 BP 开给公司（月付或预付 1/3/5 年），再分给成员。八种订阅按场景选：话音看 Business/Enterprise，话务台必须 Attendant，会议室是 Room，CRM 集成是 Connect。
- **成员**：邮箱即身份，一人不能属两家公司。开户四法（手动/邀请/CSV 批量/Azure AD 同步）。
- **删除与安全**：删除进 10 天宽限——恢复后回落免费版要重配订阅和电话线，宽限期内邮箱不能复用。管理员改密会立即踢掉在线会话（防盗号特性，批量改密避开工作时间）。

## 三、接入主线：从 RCC 到完整音频

1. **OMC 首连**：Expert 模式 + 服务器认证，证书装进受信任的根（一劳永逸消除告警），密码逐客户必改——pbxk1064 只是出厂一次性密码。
2. **接入 Rainbow**：PBXID + 激活码（经销商给，或客户管理员在 My company/Communication 自取），填入 OMC/Cloud/Rainbow，域名保持 openrainbow.com 不动。验证判据：Webdiag 显示 **connected with final password**；排障日志 ccrbagent.log。
3. **分机关联（RCC）**：Telephony 页签把 OXO 分机绑到 Rainbow 账号。此时 Rainbow 只能**监督**话机（接/挂/转），音频全在话机——这是无网关时的正常形态，不是故障。用户问"为什么耳机没声音"，答案就在这。
4. **WebRTC 网关解锁音频**：只建音频媒体关系，呼叫控制始终在 PBX。R4.0.020.002 起 Reseller 管理员在 Rainbow 管理端一键自动配置（网关/SIP 账号/中继组/ARS 全自动），但**连 PBX、建终端、编号计划与闭锁仍是安装员的活**。

## 四、网关选型一张表

| 拓扑 | 承载 | 版本前提 | 通话上限 | 许可特点 |
|---|---|---|---|---|
| OCE 集成 | OCE（IPBox）内置 | R3.2+ | 20 | 免 SIP trunk 许可（bypass）；Power CPU EE 不支持 |
| OCE Front End | 独立 IPBox 前置 | 双端 ≥R4.0 MD | 20 | 许可免费 FTR 自给；无 PBX 能力；仅配 Power CPU EE |
| 外部 VM/NUC | ESXi 或迷你 PC | — | 50 | 通用扩容路径 |

容量查表（用户数 → 推荐通道数，p147）：

| 用户数 | 外部拓扑 | 集成/FE 拓扑 |
|---|---|---|
| 5 | 5 | 5 |
| 10 | 7 | 7 |
| 20 | 11 | 11 |
| 30 | 15 | 15 |
| 50 | 20 | 20 |
| 70 | 27 | NA |
| 100 | 36 | NA |
| 150 | 50（打满） | NA |

150 用户上限的前提是极低话务——引用这个数字必须带前提。FE 改配置后必须 warm reset；双机 PBXID 必须一致；SIP 网关端口核对 5059；FTR 出厂占位凭证 FleetRef-Installref 正式接入前必须替换。

终端形态决定许可：

| 用户形态 | 终端结构 | 许可 |
|---|---|---|
| 有话机 | Multiset：物理主站 + **Free Rainbow in Twinset** 虚拟副站（R6.0 起） | 1 UTL（副站不额外占） |
| 纯软话机 | Anydevice 单终端 | 1 UTL |

R5.2 及以前副站位置用 Anydevice——升级过的系统按旧语义建副站会白占许可。

## 五、两个增值场景

- **话务台（Attendant）**：Attendant 订阅解锁，仅 Web/Desktop（手机上没有）。队列 OXE 10 路 / OXO 8 路；监督组每监督员 ≤5 组、每组 ≤30 人。互助组支持一键进出、临时纳排成员、锁定成员；代接**仅限同 PBX 的话机呼叫**——纯软话机用户和跨 PBX 都不在覆盖内，需求评审先泼这盆冷水。
- **Teams 集成**：工作台级（每台 PC 装配），不是租户一键生效。Teams 里的 Rainbow App 管电话面（拨号盘/历史/留言），Rainbow Desktop 管点击外呼和呼叫控制且**必须常驻运行**；权限收敛成 Telephony-only（协作归 Teams）；订阅 Business/Enterprise；在场同步默认关，要手动激活 O365 共享；SSO 不是前提。

## 六、交付红线与维护抓手

三条红线：

1. 教材全部密码/账号/网段是实验值，上生产必须换
2. 端口/带宽/TURN/防火墙等网络数值在书外（以官方《Rainbow Network Requirements》PDF 为准）
3. 编号计划与闭锁全书不教（TC2479 + 客户拨号规范）

维护八抓手：

| 抓手 | 用途 |
|---|---|
| 用户日志 | About Rainbow → Open logs |
| 用户问题上报 | 集成商能看到与客户同一份上报 |
| status.openrainbow.com | 云故障状态页 + 告警订阅 |
| 维护预告 | 管理门户内按地域/架构过滤的计划维护 |
| 音频告警 | 设阈值通知音质劣化与无音频 |
| 操作历史 | 审计谁在什么时候改了配置 |
| HelpDesk 指南 | help.openrainbow.com 排障入口 |
| MyPortal 开 SR | 注意：只有 Rainbow 认证伙伴的工单才会被建，项目启动先理顺认证 |

## 七、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 建 Rainbow 公司/开订阅 | rbx-company-subscription |
| 装 OMC/首连/改 IP | rbx-omc-onboarding |
| PBX 接入 Rainbow/接入排障 | rbx-pbx-onboarding |
| 开户/销户/批量导入 | rbx-member-lifecycle |
| 网关选型/容量计算 | rbx-gateway-planning |
| 网关部署/建终端 | rbx-gateway-deployment |
| 话务台/监督组/互助代接 | rbx-attendant-supervision |
| Teams 集成全流程 | rbx-teams-integration |
| 分机关联/RCC/日志/SR/网络核查 | 路由入口（rainbow-oxo-connect-router） |

## 版权

- 本精华长文为 ALE Training Services《Rainbow OXO Connect》（RAINXTE001EN Edition 13）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
