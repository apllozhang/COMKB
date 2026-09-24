# OTSBC 部署与向导配置（OVF 上电、CLI 初始化、许可、证书、Remote Users 模板、手工补配）

## R — 原文依据

> "Start the OTSBC virtual machine and logon. … Login and password are 'Admin'."（p91）
> "Application: Remote Users (IP-PBX with remote Users); Template: Alcatel-Lucent Remote Users"（p102）
> "Warning: FOR IPHONE DEPLOYMENT, ADDITIONNAL MANUAL CONFIGURATION OF SEVERAL OBJECTS IS MANDATORY. IT IS NOT PART OF THIS LAB. CONSULT THE TC2639 FOR CONFIGURATION INFORMATION."（p105）
> "OXE can use UDP as well TCP for SIP. But wizard configures only UDP. It is why it is better to configure also TCP port in OTSBC. … TCP port 5060"（p117）

出处：OPENXTE225EN p78-88, p89-117。

## I — 自述

OTSBC 是 ALE OEM 的 AudioCodes Mediant 平台，部署高度向导化，主步骤四件：OVF 上传、IP 设置、Web 界面向导、附加配置。

部署链按序：

1. **OVF 部署**：Business Portal 下载 OVF（向导软件同站），ESXi 导入并开机
2. **CLI 初始化**：初始账号 Admin/Admin（出厂默认，生产首登即改）；配管理网口 IP 后 write + reload now 生效
3. **许可**：webadmin 的 Setup/Administration/Maintenance 更新 License key，改完用 Maintenance Actions 的 RESET（Save to FLASH=Yes）保存重启
4. **证书**：TLS Contexts 导入 CA 根证书，新建上下文，Generate Private key 后走 CSR 签发并加载（联动证书能力）
5. **向导**：Configuration Wizard 选 Application=Remote Users (IP-PBX with remote Users)、Template=Alcatel-Lucent Remote Users，按参数分组走完
6. **收尾手工**：给每个 SIP 接口把 TLS Context Name 换成自签发的证书上下文；补两项手工（见下）

向导参数分组（p101-105/p110-115）：

| 分组 | 关键项 |
|---|---|
| General | End Customer/Country/Integrator/Installer |
| Topology | Application=Remote Users、Template=Alcatel-Lucent Remote Users、Network Setup 按端口拓扑 |
| System | Web 界面 HTTP/HTTPS、CLI Telnet/SSH、时区、NTP |
| IP | 物理口 Group 1、IP/掩码/网关、NAT Public IP、内部 DNS、OAM 接口=WAN |
| OpenTouch SIP | 内部 IP/FQDN/传输（web 向导 UDP，thick 向导 TCP） |
| OXE SIP | 主 IP/FQDN |
| SBC SIP | OTCV、OTCT、OTCV Web 三组开关与域 |

配置结构总览（p86，实验口径端口）：6 个 IP Profile/IP Group（OT、OXE、OTCv、OTC WebRTC、OTCt、SIP carrier）+ 4 个 Media Realm（RTP/SRTP 端口段，WAN 侧 RTP 7000-7499 等）；OTSBC 申报分"IT 服务器级"与"设备级"两层（p88）。

两项必做手工（书内明示）：给 OXE 的 SIP 接口补 TCP 5060——向导只配 UDP，而 iPhone 场外场景强制 TCP；iPhone 部署的其余手工对象不在向导与本书实验范围，查 TC2639。

## A1 — 书中案例

OTSBC 部署实验主线（p89-117，实验口径 IP/口令见 book/overview）：

1. 核对 NAT 规划：公私 IP 对、5261/8061 端口、RTP/SRTP 7000-7499 段
2. ESXi 部署 OTSBC OVF 并开机（OVF 通用步骤见虚机部署卡）
3. CLI 用 Admin/Admin 登录，enable 后 configure voip，interface network-if 0 配 IP/掩码/网关
4. 两级 exit 后 write，reload now 重启生效
5. webadmin 更新 License key，RESET（Save to FLASH=Yes）保存重启
6. TLS Contexts 先 Import CA 根证书，再新建上下文并走 CSR 签发加载证书链
7. Configuration Wizard 更新模板后按七组参数走完，Apply & Reset
8. SIP Interfaces 里逐个把 TLS Context Name 改为新证书上下文
9. 手工补：OXE 的 SIP interface 2 增配 TCP 5060（Edit 后 Apply）

## A2 — 未来触发

使用情境：新站点部署远程话音边缘；OTSBC 装完注册不上；向导跑完发现缺承载；iPhone 场景准备；申报侧需要 SBC 的 FQDN 与端口。

语言信号：OTSBC / SBC / Mediant / OVF / 向导 / wizard / Remote Users / 许可 / license / TLS Context / SIP 接口 / IPG / Media Realm / 5261 / 8061 / 5263 / TCP 5060 / NAT Public IP。

与相邻能力区分：

- 先签证书 → 证书与 PKI 能力
- 申报 SBC 到 OT 侧 → OT 服务器侧设置能力
- SBC 内嵌反代 → 反向代理能力
- iPhone 5265 与推送链路 → iPhone APNS 能力

## E — 可执行步骤

输入契约：公私 IP 对与 NAT 规则、证书（CA 根 + 签发通道）、License key、OT 与 OXE 的内部地址、客户端端口规划（5261/8061）。

1. 下载 OVF 与向导软件（Business Portal），ESXi 导入上电。完成标准：虚机控制台可登录
2. CLI 初始化管理网口并 write+reload。完成标准：webadmin 可用新 IP 访问
3. 更新许可并 RESET 保存。完成标准：License Key 页许可生效
4. 导入 CA 根证书，新建 TLS 上下文完成 CSR 签发加载。完成标准：上下文持有可信证书链
5. 跑向导：Application/Template 选 Remote Users 与 Alcatel-Lucent Remote Users，七组参数按规划填。完成标准：Apply & Reset 成功
6. 逐个 SIP 接口替换 TLS Context Name。完成标准：SIP Interfaces 页 Result 核对通过
7. 手工补 OXE 侧 SIP 接口 TCP 5060。完成标准：interface 2 同时有 UDP 与 TCP 端口
8. iPhone 场景另建 SBC 声明（同 FQDN、端口 5265）并在 OT SBC 增配 5265 SIP 接口（转 iPhone APNS 能力）

判停点：

- 客户问通道数/CAC 阈值等容量口径 → 停，书内无数值（n30），指向 8AL90065USAG 或 sizing 工具
- iPhone 场景以为向导能全覆盖 → 停，书内两处 Warning 明示必须手工补配且查 TC2639（n06）
- SIP 注册失败 → 先核对 Conversation/Connection 两种身份的 OTCV/OTCT 域配置（n08），再查口令与证书

输出契约：可用的会话边界控制器（许可/证书/向导配置落地）+ SIP 接口证书核验记录 + 手工补配清单（TCP 5060、iPhone 待办移交 TC2639）。

## B — 边界

- 初始凭据 Admin/Admin 为出厂默认（实验口径），生产首登即改并纳入口令台账（n33）；本卡正文不含环境值，见 book/overview
- iPhone 部署强制手工配置、不在本书实验范围，权威依据 TC2639（p105/p117/n06）
- 向导只配 UDP；OXE 建议 TCP 5060 补配，深入信息查 TC1990 或 8AL90065USAG（p117）
- 端口矩阵与 Media Realm 网段为实验口径；容量（并发/带宽/CAC 阈值）书内缺位（n30）
- thick wizard 版本口径 Mediant Software (SE/VE) 7.2；向导软件从 Business Portal 下载
