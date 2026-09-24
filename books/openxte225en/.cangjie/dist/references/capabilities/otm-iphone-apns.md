# iPhone+ APNS 推送专项（来话机制、防火墙端口、5265 声明、kamailio-wasp 维护）

## R — 原文依据

> "All notifications from OpenTouch server to OTC iPhone are sent through Apple Push Notification Server (APNS); APNS is an Apple Cloud service: firewall configuration is impacted"（p183）
> "Several SIP invites may be required … UDP is mandatory to allow the several SIP Invites during incoming calls … Behind the SBC, over Internet, TCP is mandatory: OpenTouch server will act as a SIP proxy 'buffering' the SIP invite message over TCP"（p186）
> "kamailio-wasp: SIP proxy between SBC and OXE; wspcfg: service to provide configuration for kamailio"（p187）
> "APNS's certificate is shipped with OpenTouch server: Valid one year; A dedicated hotfix will be delivered every year to keep the certificate up to date"（p184）

出处：OPENXTE225EN p183-188, p197, p217。

## I — 自述

R2.3.1 起 iPhone 的 OpenTouch 通知全走 APNS（Apple 云推送服务），它是 VoIP 来话的"第二振铃路径"：应用在后台时首个 SIP invite 被忽略，要先推送唤醒、再收一次 invite——所以"多次 SIP invite"是设计行为，不是故障。

承载约束与组件：

- 场内（仅 UDP 拓扑）：UDP 承载多次 invite，无额外动作
- 场外经 SBC 走互联网强制 TCP：由 OpenTouch 侧 kamailio-wasp（SBC 与 OXE 之间的 SIP 代理）+ wspcfg（给 kamailio 提供配置的服务）做 invite 缓冲
- iPhone+ 专用 SBC 声明：FQDN 与通用 SBC 相同、端口 5265；OT SBC 增配 5265 的 SIP 接口

防火墙四端口（p184）：

| 端口 | 用途 |
|---|---|
| TCP/5223 | 与 APNs 通信 |
| TCP/2195 | 向 APNs 发通知 |
| TCP/2196 | APNs 反馈服务 |
| TCP/443 | 设备激活；WiFi 上 5223 不可达时的回落 |

证书机制：APNS 证书随 OT 出厂、有效期一年、每年由专门 hotfix 更新；Geotrust 根证书出厂自带、有效期至 2022 年；连接 APNS 时两证同时校验。运维含义：每年跟 OpenTouch 的 APNS hotfix，跨 2022 的续期机制在书外。

书内边界：OTSBC 向导不覆盖 iPhone 所需对象，完整手工配置书内两处 Warning 明示"not part of this lab, consult TC2639"——本卡只覆盖书内可做的三件事（5265 声明、5265 SIP 接口、组件维护）。

## A1 — 书中案例

iPhone+ 配置与维护动作（p188/p197/p217，实验口径值见 book/overview）：

1. Eco system/IT Server 右键 Create，建 iPhone 用 SBC 声明：FQDN 同通用 SBC、Network type=WAN、Port 5265
2. OT SBC 侧增配端口 5265 的 SIP 接口
3. 防火墙放行 TCP 5223/2195/2196/443 四端口
4. 查 kamailio-wasp 状态：service kamailio-wasp status（start/stop/restart 同式）
5. 查 kamailio 日志：/var/log/localmessages
6. 调日志级别：/usr/kamailio-wasp/loglevel.sh（3=DBG、2=INFO、1=NOTICE、0=WARN、-1=ERR）
7. 查 wspcfg 服务：service wspcfgd status，日志 /logs/wspcfg/wspcfg.log
8. 调 wspcfg 级别：loglevel.sh component=wspcfg logger=* level=debug
9. 取全量日志用 Logzipper 打包（含 kamailio 与 wspcfg 日志）

## A2 — 未来触发

使用情境：iPhone 后台收不到来话或来话慢；iPhone+ 上线评估；防火墙评审要报端口；跨年维护证书；场外 iPhone 通话承载排障。

语言信号：iPhone / iPhone+ / APNS / 推送 / push / 5265 / 5223 / 2195 / 2196 / kamailio-wasp / wspcfg / invite / TCP / UDP / hotfix / Geotrust / VoIP everywhere。

与相邻能力区分：

- 手机的开通与自动对象 → 智能手机配置能力
- 手机在无数据时的行为 → 智能手机模式能力
- SBC 本体部署 → OTSBC 部署能力

## E — 可执行步骤

输入契约：OpenTouch 版本（R2.3.1+）、iPhone+ 应用清单、防火墙策略变更通道、SBC 管理权限。

1. 确认版本与组件：R2.3.1 起推送全走 APNS；盘点 kamailio-wasp/wspcfg 所在服务器。完成标准：组件清单与版本记录
2. 建 iPhone+ 专用 SBC 声明（同 FQDN、端口 5265）。完成标准：IT Server 列表出现该声明
3. OT SBC 增配 5265 SIP 接口。完成标准：SIP Interfaces 出现 5265 条目
4. 防火墙放行四端口：TCP 5223/2195/2196/443。完成标准：策略变更单与端口表一致
5. 记录证书台账：APNS 证书一年一换（跟年度 hotfix）；核对当前 hotfix 状态。完成标准：维护日历含年度动作
6. 排障抓手就位：会查两个服务的状态/日志/级别与 Logzipper 打包。完成标准：A1 步骤 4-9 命令可执行

判停点：

- 客户要求书内给出 iPhone 完整手工配置 → 停，书内明示查 TC2639（n06），如实外置
- 现在已过 2022 年 → 停，Geotrust 根证书续期机制在书外（n17），查当期 ALE 维护公告
- "iPhone 突然收不到来话" → 按链路查：两张证书与 hotfix 状态、四端口、kamailio-wasp 状态（n17/n18）

输出契约：iPhone+ 推送链路就绪记录（5265 声明与接口、四端口放行、证书台账）+ 组件维护命令清单。

## B — 边界

- iPhone 部署的完整手工配置强制但书外（TC2639）；按"跑完向导就完事"交付必翻车（n06）
- APNS 证书一年一换靠专门 hotfix；Geotrust 根证书 2022 年到期后的机制超出本书（n17）
- 多次 SIP invite/UDP 强制/场外 TCP 代理缓冲为机制约束（n18）；"漏接先查链路"含工程引申（needs-review nr-06）
- 具体环境值（服务器地址等）见 book/overview 环境区；端口为协议规划口径可复用
- 本卡以 R2.6/Issue 10 时代坐标为限；后续 iOS/APNS 演进不在书内
