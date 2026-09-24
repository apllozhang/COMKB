# 客户端远程接入两步法（接入配置与路由档案）

## R — 原文依据

> "Step 1: configuration of remote access: Public OpenTouch URL, Login and password; Step 2: routing configuration: Activation of required profile (Call from PC/Route to PC, …)"（p147）
> "When a smart phone is used to dial (dial by number, directory search, from history, from contacts, …), it is always used to make the call whatever the 'dial from' specified in the active profile"（p147）
> "PC: OTC Web: Conference public URL received by mail"（p149）

出处：OPENXTE225EN p145-150。

## I — 自述

任何客户端远程接入都是两步：

1. **接入配置**：填公共 OpenTouch URL（反代公共地址）+ 登录凭证
2. **路由档案**：激活"从哪拨/路由到哪"组合（PC/手机/家庭电话/其他号码的呼出与落地路由）

各客户端入口：

| 客户端 | 接入配置入口 | 说明 |
|---|---|---|
| OTC PC | 启动时或 Settings/Preferences 填反代 FQDN | 也可直接填 OTSBC 公共 FQDN 走 SIP |
| OTC 智能手机 | 首次启动填，后续 Settings/Connections 改 | Public hostname 填反代地址而非内网地址 |
| OTC Web | 用邮件收到的会议公共 URL 直接进 | 无需装客户端 |
| OTC PC One | 同 OTC PC | 无 VoIP，仅协作功能 |

手机拨打特例（p147/p150 两处强调）：只要是用智能手机发起拨打（按键、目录、历史、联系人），发话设备永远是手机本机，与档案里的 "dial from" 无关——该设置只对从 PC 等其他端发起的呼叫生效。

## A1 — 书中案例

客户端接入动作（散布于各 How-To，p148/p156/p214-216）：

1. OTC PC：Settings/Preferences 里填反代 FQDN，凭证用 OpenTouch 账号
2. OTC PC（软话机形态）：Security 页配 SBC——OTSBC 公共 FQDN、端口 5261、TLS、Encrypted only
3. Android：商店装 OpenTouch Conversation，首启填 Public hostname/URL 与 Private hostname/URL
4. iPhone：App Store 装 OpenTouch Conversation Plus，首启填 Public/Private Server Name 与凭证
5. OTC Web/来宾：点邮件里的会议公共 URL 进浏览器协作

## A2 — 未来触发

使用情境：远程员工第一次配客户端；"手机上打电话为什么走的手机"类疑问；来宾问怎么进会议；换反代地址后客户端批量改配置。

语言信号：接入配置 / 公共 URL / public URL / 路由档案 / routing profile / dial from / Call from PC / Route to PC / OTC Web / 会议链接 / Settings / Connections / 首次启动。

与相邻能力区分：

- 手机的开通过程 → 智能手机配置能力
- PC 两模式选型 → OTC PC 两模式能力
- URL 与端口规划 → DMZ 双边缘能力

## E — 可执行步骤

输入契约：反代公共 URL、用户凭证、路由档案需求（呼出/落地方向）、客户端类型清单。

1. 分发接入信息：公共 URL + 凭证 + 客户端下载渠道。完成标准：用户拿到可登录的接入包
2. 按客户端类型指引入口填 URL 与凭证（首启或 Settings）。完成标准：登录成功
3. 配路由档案：按用户场景选"从哪拨/路由到哪"组合并激活。完成标准：激活档案与需求一致
4. 讲清手机拨打特例：手机发起的呼叫永远本机发话。完成标准：用户知情（减少误报障）
5. 行为验证：从 PC 与手机各发起一通呼叫，核对发话设备与落地。完成标准：与档案预期一致

判停点：

- 用户报"路由档案没生效"但触发方式是手机上直接拨号 → 停，这是设计行为不是故障（n11）
- 手机首启填了内网地址 → 停，Public URL 必须填反代公网地址（n32）
- OTC Web 进不去 → 停，先核会议 FQDN 公共解析与证书 SAN（转 DMZ 双边缘与证书能力）

输出契约：可登录的远程客户端 + 已激活的路由档案 + 行为验证记录。

## B — 边界

- 手机拨打特例是排障高频误解点：dial from 不改变手机发话（p147/p150/n11）
- EVS 通知必须带 8016 端口，客户端 URL 细节错配的表现是"通知时好时坏"（n32）
- 客户端 VoIP 能力差异见 DMZ 双边缘能力的用例矩阵；OTC Web 仅协作、WebRTC 才有浏览器音视频
- 实验口径的示例 URL（原书 p214 缺冒号笔误）见 needs-review nr-04；本卡不含环境值
