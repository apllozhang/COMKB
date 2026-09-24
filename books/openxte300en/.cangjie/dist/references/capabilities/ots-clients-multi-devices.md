# OTC PC 客户端交付与多终端（Desktop 许可、软电话、Multi-devices）

## R — 原文依据

> "Two different working modes possible for Connection users: OTC PC: full mode for Connection users with « Desktop » right (license) • OTC PC One : Freemium mode"（p433）
> "MAKE SURE THAT THE DESKTOP LICENSE IS ENABLED FOR THIS USER DON'T GRANT "NOMADIC SIP" RIGHT TO THIS TYPE OF USER"（p474）
> "Up to 5 devices with following rules: Main device can be: NOE IP, NOE TDM, IPDSP, SIP(SEPLOS), desk sharing (DSU), an OTC PC ... Only one remote extension Only one DECT"（p439）
> "« MICROSOFT VISUAL STUDIO C++ 2010 TOOLS FOR OFFICE » MUST BE ALREADY INSTALLED ON THE PC TO DEPLOY SUCCEFULLY "OUTLLOK ADD-IN""（p462，OUTLLOK 为原文笔误）

出处：OPENXTE300EN p430-493。

## I — 自述

客户端是"许可驱动形态"：OTC PC 与 OTC PC One 是同一安装包，Desktop 许可决定运行模式。

| 形态 | 触发条件 | 能力面 |
|---|---|---|
| OTC PC 全量 | 档案/用户勾 Desktop 许可 | RCC+VoIP+IM/共享/会议/Outlook 集成 |
| OTC PC One 免费 | 无 Desktop 许可 | 话机伴侣：单线、盲通话只能挂断、无 VoIP、无监督、共享仅 viewer |

安装与前置：安装包从 OT 服务器的固定 URL 分发（OpenTouchConversation.msi）；前置 .NET Framework 4.5 与 VS C++ 2010 Tools for Office（缺后者 Outlook 加载项装不上）；必填内部 FQDN 与远程 FQDN；首次启动把 IM 默认应用答 Yes 才有 Outlook 在场与操作。

软电话两路线：

- **Multi-devices（本卡主线）**：给用户挂 SIP 分机为第二设备并关联 OTC PC 设备（设备标识为"分机号@OT FQDN"，类型 Softphone）；SIP 配置由设备管理服务器（DM，实验由 8770 充当）下发；许可组合必须 Desktop 勾、Nomadic SIP 不勾（两权互斥）。
- **Nomadic 池**：旧软电话路线，另一培训讲，本卡仅作判停指针。

多终端规则与前置：

- 一名用户最多 5 台设备；主设备白名单（NOE IP/TDM、IPDSP、SIP、DSU、OTC PC）；副设备另可 DECT、MIPT、REX、OTC 手机
- 远端分机与 DECT 各限 1；OTC PC 走 VoIP 不冻结话机
- 前置：用户 Phone features COS 开"主站故障时副站同振"；建 Twinset get call 与 No ringing 两前缀并在 COS 授权

## A1 — 书中案例

**客户端安装与模式对照**（p460-483）：

1. 从 OT 服务器 URL 下载 OpenTouchConversation.msi 并安装。
2. 部署类型选 Standard（自动带 Outlook 扩展）。
3. 填内部 FQDN 与远程 FQDN 完成向导。
4. 8770 侧给用户勾 Desktop 许可与协作共享权。
5. 登录客户端：服务器填内部 FQDN，首次 IM 默认应用答 Yes。
6. 功能验证：在场、收藏、呼出接听转接、IM 与共享、呼叫历史。
7. One 模式对照：不勾 Desktop 的用户登录即落免费模式。
8. One 下验证：呼出可用、来话不能接只能挂、共享仅可看。

**软电话与多终端实验**（p471-493）：

1. 建 SIP extension 类型设备（SIP 口令留空则自动生成）。
2. 设备右键 Associate SIP device 关联 OTC PC（分机@OT FQDN）。
3. OT 配置设备页 SIP extension type 选 Softphone。
4. 许可组合核对：Desktop 勾、Nomadic SIP 不勾。
5. 多终端前置：COS 开主站故障副站同振。
6. 建 Twinset get call 与 No ringing 两前缀并授权。
7. 副站加 NOE 话机或 SIP extension（各受上限约束）。
8. 两侧核验 Tandem 号与 Softphone Directory Numbers。
9. 行为测试：切换设备呼出接听、副站静音主站、路由档案切换。

## A2 — 未来触发

使用情境：客户端装了电话功能都用不了；耳机没声音；想用电脑接听；要给一部手机也接来话；Outlook 里没有 OT 按钮。

语言信号：OTC PC / OTC PC One / Desktop 许可 / freemium / RCC / VoIP / 软电话 / softphone / SIP 分机 / Multi-devices / 多终端 / 副站 / secondary set / Twinset / No ringing / Outlook 加载项 / .msi。

与相邻能力区分：监督组（建组/代接/进出组）转监督组路由卡；SIP 配置文件没下发查 8770 的 DM 声明（节点声明与 SIP 能力）；用户开通与档案属用户供给能力；Nomadic 模式在书外培训。

## E — 可执行步骤

输入契约：用户画像（有话机/纯软话机/移动需求）；Desktop 许可池余量；客户端 PC 前置件核查；内部与远程 FQDN。

1. 装前置件并安装客户端（Standard 类型）。完成标准：安装完成且无加载项报错
2. 按画像发 Desktop 许可（全量）或不发（One）。完成标准：运行模式与设计一致
3. 软电话用户建 SIP 分机副站并关联客户端。完成标准：SIP 配置文件生成且可注册
4. 许可组合核对：Desktop 勾、Nomadic SIP 不勾。完成标准：无互斥组合
5. 多终端按 5 设备规则加副站并配两前缀。完成标准：设备切换与静音行为正确
6. Outlook 集成验证：从邮件与联系人卡发起 IM 与呼叫。完成标准：加载项可用

判停点：

- 用户报"客户端坏了"电话功能全无 → 先查 Desktop 许可勾选，别急着重装
- 软电话行为怪 → 查 Desktop 与 Nomadic SIP 是否被同时授权（互斥）
- SIP 配置文件没生成 → 查 8770 是否已声明为 DM、端口与下发目录
- 副站加不上 → 超 5 台或远端分机/DECT 已各占 1
- Outlook 加载项装不上 → 缺 VS C++ 2010 Tools for Office 前置件

输出契约：可交付客户端清单（模式/设备/许可组合）+ 行为验证记录。

## B — 边界

- 实验口径（生产按现场计划替换）：分机 31000/31002/31009、软电话 SIP 口令 98765、Twinset 前缀 506/507、副站号 2131000/2131002。
- OTC for MAC 无桌面共享/桌面集成/VDI（p443 对比表）；OTC PC One 的 IM 不能加参与者、不能发起共享。
- 远程安全接入走 SBC+反向代理（端口 443/8016，正文 413 为笔误见 nr-02），证书见证书路由卡；VPN 非必需（p444）。
- OTC Mobile 仅提及不展开；Nomadic 模式在另一培训（n39）。
- 可编程键、路由档案属用户自助配置面，本卡给交付验证口径，不做终端个性化定制。
