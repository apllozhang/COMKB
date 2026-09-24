# WebRTC 网关部署与升级（OVF 虚机、mp 命令族、BP 激活、远程/手动升级）

## R — 原文依据

> "A software component located in a customer's premises that runs on a virtual machine. Use of the WebRTC Gateway requires a BUSINESS or ENTERPRISE subscription for a member"（p133）
> "Require OXE release 12.1 MD4, 12.2 or later … The virtual machine (OVF) is delivered by ALE • The Operating System is based on a Debian"（p135）
> "In Rainbow Administration, the WebRTC gateway option in PBX settings must be activated by the BP administrator."（p161）
> "Update your WebRTC gateway with the REMOTE UPGRADE METHOD via Rainbow, if available. Otherwise, perform the update manually."（p173）

出处：RAINXTE003EN p131-136, p153-176。

## I — 自述

网关负责 Rainbow 客户端与 OXE 分机/资源的语音互通；呼叫控制始终在 PBX，网关只管音频媒体（p133）。

部署三重前提（p133/p135/p154）：

| 前提 | 口径 | 出处 |
|---|---|---|
| 成员订阅 | Business 或 Enterprise | p133 |
| OXE 版本 | 12.1 MD4、12.2 或更高 | p135 |
| 顺序前提 | PBX 已接 Rainbow 且用户已做分机关联 | p154 |

部署流程五步（p153-161）：

- MyPortal 下载 OVF（OXE/OXO 目录同一软件）
- VM console 改键盘（模板默认 QWERTY）
- mpnetwork 配网络
- mpconfig 填 PBX 域名与 PBXID
- mpshow/mpcheck 核验后由 BP 管理员在 Rainbow 侧勾 Activate WebRTC gateway

mp 命令族（p156-166）：

| 命令 | 用途 |
|---|---|
| mpnetwork | 配 IP/掩码/网关/DNS/主机名/NTP，确认 y 后重启生效 |
| mpconfig | 填 PBX_DOMAIN 与 PBXID；默认输出含 TURN_SERVER=GEOIP、WRTRANGE/SIPRANGE 端口段 |
| mpshow | 看版本与全量配置 |
| mpcheck | 八段连通性自检（网络/Rainbow 设置/DNS/Rainbow connect/TLS/STUN-TURN/PBX 域/SIP OPTIONS） |
| mpssh | 开关 SSH（供 WinSCP 传文件或粘贴 PBXID） |
| mpupgrade | 手动升级（-now 立即或 -delay 延迟） |

升级两法（p163-176）：远程升级优先——BP 管理员在 Rainbow Web 端操作，适用 1.73.x+ 且仅 35 国（清单在在线文章）；手动升级兜底——MyPortal 下载 iso 与校验文件，WinSCP 传到网关 Upgrade 目录后 mpupgrade，适用 1.67.6-121 起。升级失败按官方文章处理。

## A1 — 书中案例

**部署实验**（p153-162）：

1. 下载四份文档备用：安装指南、命令清单、升级指南、TC2462
2. 从 MyPortal Taxonomy 下载网关 OVF（选 OXE 或 OXO 目录皆可，同一软件）
3. 首次启动用 VM console 以专用小账号登录改键盘（模板默认 QWERTY）
4. mpnetwork 配 IP/掩码/网关/DNS/主机名/NTP，确认 y 后重启
5. mpconfig 填 PBX_DOMAIN（OXE 地址）与 PBXID（从 Rainbow 端复制）
6. 核对输出中 RAINBOW_DOMAIN、TURN_SERVER、WRTRANGE、SIPRANGE 四个默认值后重启
7. mpshow 看版本与全量配置；mpcheck 逐段核验八段输出
8. BP 管理员登录 Rainbow，在该 OXE 的 PBX 设置勾 Activate WebRTC gateway（客户管理员无此权限）

**升级实验**（p172-176）：

1. 优先远程法：BP 账户在 PBX 列表看新版本，按在线文章上传并确认 Upgrade
2. 手动法兜底：MyPortal 下载新版，解压得 iso 与 iso.md5；mpssh on 开 SSH
3. WinSCP（SFTP）把两个文件传到网关 Upgrade 文件夹
4. mpupgrade 确认执行（可 -now 或 -delay），完成后 mpcheck 验证配置恢复且已连云

## A2 — 未来触发

使用情境：部署 Rainbow 语音网关；mpcheck 某段报错；网关激活按钮点不到；升级网关版本；升级后起不来。

语言信号：WebRTC Gateway / OVF / 虚机 / mpnetwork / mpconfig / mpshow / mpcheck / mpssh / mpupgrade / WinSCP / 升级 / upgrade / GEOIP / STUN / TURN / 激活 / BP 管理员。

与相邻能力区分：

- OXE 侧 SIP/ARS/回调配套 → OXE 侧网关配置能力
- 多 OXE 共用与容量 → 共享池与容量能力
- 接入层连接问题 → OXE 接入能力

## E — 可执行步骤

输入契约：三重前提核查表、虚机资源（独立 ESXi 或与 OXE 同服务器）、BP 管理员账号（激活/远程升级）、MyPortal 访问权。前提缺一 → 判停先补前提。

1. 核前提：订阅档位、OXE 版本、PBX 已接入且分机已关联。完成标准：三项全部满足
2. 部署 VM：载入 OVF、改键盘、mpnetwork 配网并重启。完成标准：网关 IP 可达
3. 配 PBX 参数：mpconfig 填域名与 PBXID，核对默认输出后重启。完成标准：mpshow 值正确
4. 核验：mpcheck 八段逐段看。完成标准：主干段全部 OK（GEOIP 段例外见边界）
5. 激活：BP 管理员在 Rainbow 端勾 Activate WebRTC gateway。完成标准：网关状态启用
6. 升级规划：按版本与地域选远程或手动法。完成标准：升级路径与回退方案成文
7. 升级执行：远程上传确认或手动传输后 mpupgrade。完成标准：mpcheck 正常且版本号更新

判停点：

- OXE 版本低于 12.1 MD4/12.2 → 停，先升级 OXE，不硬配网关
- PBX 未接入或用户未关联 → 停，回接入/分机关联能力补顺序前提
- mpcheck 的 STUN/TURN 段 FAILED 但 Rainbow connect 段 OK → 多为 GEOIP 文件缺失，非部署失败（n17）
- 无显示器键盘的独立 PC → 排除远程升级，走手动 mpupgrade（n18）
- 升级后仍是旧版 → 按官方失败处理文章操作，不反复重刷

输出契约：网关运行且已激活的双侧证据 + mpcheck 基线记录 + 升级路径与版本台账。

## B — 边界

- TURN 生产位置选择与防火墙白名单在书外（TURN_SERVER=GEOIP 仅为默认口径，p158/p160）；以 Network Requirements PDF 与 VoIP calling Troubleshooting guide 为准
- 远程升级的版本门槛（1.73.x+）与 35 国清单随版本演进，执行前取支持网站最新文章（n18）
- 上传前必须接受出口管制条款；下载被代理拦截用 Abort 重试（p168）
- 网关软件样例版本（1.78.11-470）、三服务名与实验账号见 book/overview 环境区，均为实验口径
- 本卡只覆盖网关 VM 侧；OXE 侧九件套与 VoIP 测试在 OXE 侧网关配置能力
