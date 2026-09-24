# DIGEST — Rainbow / OmniPCX Enterprise 集成精华长文

> 源：RAINXTE003EN Edition 12（314 页，Rainbow R101.1 N4 MD4/SP161 + OXE Ed12）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OXE+Rainbow 混合集成的全局认知；操作细节按需查 13 张能力卡。

## 一、这套东西是什么

Rainbow 是 ALE 的云协作平台（UCaaS 协作/云话音 + CPaaS 开放 API），与 OmniPCX Enterprise 是**混合云关系**：OXE 保留呼叫控制和话音资源（中继组、话务、留言、公号），Rainbow 提供聊天、会议、移动端和云服务。

中间有两层机制：先靠 OXE 内置的 Rainbow Agent（PBXID+激活码）把 PBX 挂上云；再靠远程延伸（REX）与 WebRTC 网关把音频路径打通。

整本教材是一条交付主线，五步递进：云侧开户、OXE 接入、分机关联（RCC）、REX/tandem 路由、网关解锁完整 VoIP，最后进入话务台/维护/Teams 三个增值域。

三个数字先记住：

| 关键 | 含义 |
|---|---|
| Business / Enterprise / Attendant | 电话服务必须付费订阅，免费 Essential 只有 RCC 且不能改路由 |
| BP 专属 | 申报建 PBX、开付费订阅、激活网关、远程升级——客户管理员做不了是权限设计非故障 |
| 400 并发流 | 单网关硬上限（TBE067 估算通道数）；用户数与并发数是两个量纲 |

## 二、云侧三件套：公司、订阅、成员

- **公司（Company）**：BP 建 EC 公司（先查重），客户管理员管日常。可见性四级拿不准就 CLOSED（教材原话"建司即设"）；ISOLATED 别乱用——用户无法被外部会议邀请。SSO（Azure AD-SAML/OIDC、ADFS-SAML）配置管理员须 Enterprise 级；否则本地密码（至少 12 位含大写/数字/特殊字符）+ TOTP。
- **订阅**：先由 BP 开给公司（月付或预付 1/3/5 年），再分给成员。八种订阅按场景选：话音看 Business/Enterprise，Rainbow 话务台必须 Attendant（与 4059EE 无关），会议室是 Room，CRM 集成是 Connect。
- **成员**：邮箱即身份，一人不能属两家公司。实验主线两法：手动创建与邮件邀请（坑：邀请邮件可能进 SPAM；必须点邮件底部的 JOIN 按钮）。CSV/Azure AD 批量为讲义级，AAD 导入要 Voice Enterprise 级管理员。
- **删除与安全**：删除进 10 天宽限——恢复后回落免费版要重配订阅和电话线；宽限期内同邮箱不能重建新号。管理员改密会立即踢掉在线会话（防盗号特性，批量改密避开工作时间）。

## 三、接入与路由主线：从 RCC 到完整音频

1. **网络前提**：netadmin 菜单 14/15 配 DNS/代理，只服务 Rainbow 与 Cloud Connect agent。验证 DNS 必须用 nslookup/dig（URL ping 不算数）；HTTPS 测试只能用 IP 地址，curl 报证书错误属预期（ALE 专有证书）。
2. **接入 Rainbow**：Rainbow 端取 PBXID+激活码，webadmin Rainbow 菜单启用 agent。健康判据看 incvisu 五链路（4503/4505/4509/4507/4511）全部 in service。

   - 维护四抓手：incvisu、dhs3_init -R RAINBOWAGENT、checkCloudConfig.sh -rainbow、rainbowagent.log。
3. **分机关联（RCC）**：Telephony 页签把 OXE 分机绑到 Rainbow 账号，出现 BBB 开头的 17 位 Rainbow number。此时 Rainbow 只能监督话机（接/挂/转），音频全在话机——无网关时的正常形态。
4. **REX/tandem 解锁路由**：Business/Enterprise 用户把话机与 REX 组成 tandem（两端必须 multi-line，配置只做主站）。每路 REX 并发呼叫占一个 Ghost Z，池大小即并发上限。用户切路由时 agent 自动改写 REX：computer 路由写 BBB 号走网关，手机/家庭/其他号走公网 trunk。记住"路由不是转发"。
5. **网关解锁完整 VoIP**：网关只建音频媒体关系，呼叫控制始终在 PBX。三重前提（订阅/版本 12.1 MD4 或 12.2+/接入与关联顺序）缺一不可。

## 四、网关一张图：部署、OXE 侧配套、池化

部署是标准 VM 流程（p153-161）：

- MyPortal 下载 OVF（OXE/OXO 目录同一软件）
- mpnetwork 配网、mpconfig 填 PBX 域名与 PBXID
- mpshow/mpcheck 核验
- BP 管理员勾 Activate WebRTC gateway；升级远程法优先（BP 账户，1.73.x+ 且 35 国），手动法兜底（WinSCP 传 iso 后 mpupgrade，1.67.6-121 起）；无显示器键盘的独立 PC 不适用远程升级。

OXE 侧九件套（配错即不通，全书最重的 21 页实验）：

| 件 | 配置项 | 关键口径 |
|---|---|---|
| 1 | 国家码 | SG Country Code 按站点 |
| 2 | SIP trunk group | T2/SIP |
| 3 | 可信 IP | 网关地址入清单 |
| 4 | SIP 外部网关 | Rainbow type、5060/UDP、监督 380、DTMF 101、仅 G711（实验口径） |
| 5 | IP 域 | 无压缩但系统带压缩资源（GD/OMS）——Warning 级隐性前提 |
| 6 | CDT | ARS 用 SIP TG 的前提 |
| 7 | ARS 路由 | Route List 挂 TG 与 CDT |
| 8 | BBB 前缀与判别器 | Call Number 1 / Area 1 / route list / schedule -1 / 位数 17 |
| 9 | 回调三件套 | CSTA 开关 + 翻译表（DEF 变 BBB）+ 专用实体 |

路由四案例（选 Office phone 路由时，p116）：

| 用户档案手机号 | REX 内容 | 振铃终端 |
|---|---|---|
| 无手机号 | 空 | 仅话机 |
| 配专业手机 | 专业手机 | 话机+专业手机同响 |
| 配个人手机 | 个人手机 | 话机+个人手机同响 |
| 两个都配 | 专业手机（优先） | 话机+专业手机同响 |

池化与容量：默认选共享网关池（多 OXE 共用，按集群推进），每 OXE 每网关一条 SIP trunk；每 OXE 网关复制仅超高流量（书中示例每 OXE 达 5000 用户）才划算。满载时网关回 SIP 406 Not Acceptable，OXE 溢出到 ARS 下一条路由；溢出参数留空则退化为 SIP trunk 限制（弹性失效，核查必查）。

## 五、两个增值场景

- **话务台两套**：4059EE 走 OXE 传统话务——只管话务不管话音，关联话机禁 multi-line（与 tandem 要求正好相反），不用 Attendant 订阅；Rainbow Attendant Console 走订阅——队列 OXE 10 路/OXO 8 路，仅 Web/Desktop。监督组每监督员最多 5 组、每组最多 30 人；互助组一键进出、临时纳排成员、同时最多监督 4 路。代接**仅限同 PBX 的话机呼叫**——纯软话机用户和跨 PBX 都不覆盖，需求评审先泼这盆冷水。Rainbow 在场与电话状态是两个独立信息（书中专门设计双测试验证）。
- **Teams 集成**：工作站级（逐台 PC），不是租户一键生效。Teams 里的 Rainbow App 管电话面（拨号盘/历史/留言），Rainbow Desktop 管点击外呼和呼叫控制且**必须常驻运行**（缺它应用显示感叹号）；权限收敛成 Telephony-only（协作归 Teams）；订阅 Business/Enterprise；在场同步默认关，要手动激活与 Office 365 共享信息；SSO 不是前提。

## 六、交付红线与维护抓手

三条红线：

1. 教材全部密码/账号/网段/示例号码是实验值，上生产必须换
2. 端口/带宽/TURN/防火墙等网络数值在书外（以官方《Rainbow Network Requirements》PDF 为准）
3. 生产级配置依据：TC2462（OXE 集成）、TBE067（容量）、VoIP calling Troubleshooting guide（深排障）

维护五入口：

| 入口 | 用途 |
|---|---|
| Help Desk 指南 | help.openrainbow.com 排障/日志/报障流程 |
| 用户日志与问题上报 | 集成商与客户同视角；Web 端不采日期，取证要趁早 |
| status.openrainbow.com | 云故障状态页 + 告警订阅（按主题/地域过滤） |
| 操作历史 | 审计谁在何时改了配置（多管理员场景） |
| MyPortal 开 SR | 只有 Rainbow 认证伙伴的工单才会被建，项目启动先理顺认证 |

## 七、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 建 Rainbow 公司/开订阅/目录频道 | rxe-company-subscription |
| OXE 配 DNS/代理/接入/接入排障 | rxe-agent-onboarding |
| 开户/销户/批量导入/密码策略 | rxe-member-lifecycle |
| 用户形态/REX/tandem/振铃问题 | rxe-routing-rex |
| 网关部署/升级/mpcheck | rxe-webrtc-gateway-deployment |
| OXE 侧九件套/ARS/回调/VoIP 测试 | rxe-oxe-gateway-config |
| 共享池/406 溢出/容量估算 | rxe-gateway-pool-sizing |
| Teams 集成全流程 | rxe-teams-integration |
| 分机关联/RCC/两套话务台/云侧维护/网络核查/实验环境 | 路由入口（rainbow-oxe-integration-router） |

## 版权

- 本精华长文为 ALE Training Services《Rainbow / OmniPCX Enterprise (Participant's Guide)》（RAINXTE003EN Edition 12）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
