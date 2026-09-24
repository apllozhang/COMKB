# Cloud Connect 云连接：网络前提、FTR 首次注册与 PIN 恢复

## R — 原文依据

> "Establish a permanent XMPP channel to CCO infra over Web Socket Secure to port 443/tcp ... The remote FQDN used by OXE agent is connect2.opentouch.com"（p290）
> "The main goal of the FTR (First Time Registration) is to allow the OXE to automatically retrieve the password corresponding to the CC-Product-ID"（p293）
> "Never perform a First Time Registration (FTR) on a stand-by Call Server ... The final credentials received from CCI are automatically synchronized with the TWIN Stand-by CS"（p297）
> "A new temporary activation account will be created with a 6 digits (0-9) PIN code and will be provided by helpdesk."（p299）

出处：ENTPXTE402EN p283-301、p310-321、p322-331。

## I — 自述

FTR 是一切云服务的门禁；设计原则是"零改动入云"——OXE 出站主动发起，不改客户防火墙策略。

网络前提清单：

- 可出 Internet；DNS 解析 53/udp；常驻 XMPP over WSS 到 443/tcp；按需 SOCKS5 到 80/tcp（Inventory/Offer 取数）；两者均可经 HTTP 代理（可选）
- 目标 FQDN 固定 connect2.opentouch.com；TLS v1.2（CCI 证书由 ALE 责任下的 CA 签发，OXE 专用信任库存该 CA）
- DNS/代理配置（netadmin 14/15 菜单）仅服务于 Rainbow 与 Cloud Connect 两个代理；备用 DNS 无值也必须填 127.0.0.1 占位
- 验证入口 checkCloudConfig.sh：依次测 DNS 解析、代理参数、443（openssl 出 ALE-CLOUDCONNECT-ROOT 证书链）、SOCKS5 80——后两项打印 "Success !!" 为过关

身份体系：CC-SUITE-ID 是 23 字符串（20 个十六进制大写字符 5 个一组以"-"分隔），订单链生成、写在 .swk 里、产品终身不变；CC-PRODUCT-ID=CC-SUITE-ID+"-"+产品类型；主备 CPU 共用一个 SUITE-ID。

FTR 行为规则：

- 新装机自动执行：每 4 小时重试，失败发事件 6214、成功由 6207 清除；等不及可 CCTool 手动立即做
- 备机严禁做 FTR（永久凭证经克隆机制自动同步 twin）；PCS 不跑云服务
- FTR 只能在线路应用已启动时执行

FTR with PIN 恢复（panic 唯一出路）：触发条件为 RTR Panic Flag、无效 FTR 数据、Fleet Dashboard 显示 Duplicated。流程与边界：

- 向 helpdesk 申请 6 位数字 PIN（5 天有效）；helpdesk 同时删除其他激活账户并断开同 ID 全部产品
- CCTool 以"CC-SUITE-ID+PIN"重做 FTR：PIN 只交给 ccprocess、不落任何文件
- 操作在系统在线状态下完全重置 Cloud Connect 配置；前提是 RTR 与 ccagent 进程已在跑

## A1 — 书中案例

**云连接前提配置与 FTR 执行**（p316-331，How-To）：

1. netadmin 14 菜单配 DNS（主用 192.168.1.250、备用 127.0.0.1 占位）
2. 按需在 15 菜单配 HTTP 代理（地址/端口/账号）
3. mtcl 跑 checkCloudConfig.sh，443 与 SOCKS5 80 两项 Success
4. 装 .swk（含 CCSID）到 /usr4/BACKUP/OPS 并 swinst 恢复
5. spadmin 2 查 Suite Id（带 CCSID: 前缀；RTR 未启用时不显示）
6. WBM 核对 Cloud Connect enable=YES（新装机默认开）
7. CCTool 1 Perform FTR，接受条款后 "FTR done!!"
8. 复核三态：FTR status=Registered、operation=Success、XMPP_CONNECTED

**panic 恢复**（p330）：CCTool 1-2 输 helpdesk 的 6 位 PIN 重做 FTR，系统在线重置全部云配置并重注册。

## A2 — 未来触发

使用情境：新装机连不上云；FTR 一直失败；checkCloudConfig 不过；备机上要不要做 FTR；系统进 panic 怎么救；防火墙要放行什么。

语言信号：Cloud Connect / CCI / FTR / CC-SUITE-ID / CCSID / checkCloudConfig / XMPP / WSS / SOCKS5 / connect2.opentouch.com / PIN code / panic / helpdesk / XMPP_CONNECTED。

与相邻能力区分：

- RTR 状态与资格期监控 → RTR 卡
- Fleet Dashboard 云端操作 → 机队服务卡（路由）
- OPEX 与 LMS 订阅 → 订阅许可卡

## E — 可执行步骤

输入契约：.swk 许可文件（含 CCSID）、客户网络出站策略（443/80/53）、DNS/代理参数、MyPortal/BP 支持通道（申请 PIN 用）。电话应用未启动 → 判停先起应用再 FTR。

1. 网络配置：netadmin 14 配 DNS（备用 127.0.0.1 占位），按需 15 配代理。完成标准：配置保存
2. 连通性验证：checkCloudConfig.sh 逐项跑，443 与 80 均 "Success !!"。完成标准：全绿
3. 许可就位：.swk 恢复进 OXE（文件名过长可改名 license.swk）。完成标准：spadmin 可见 CCSID
4. 开关核对：WBM Cloud Connect enable=YES；虚机另核 FlexLM Enabled=No。完成标准：开关正确
5. 执行 FTR：CCTool 1 Perform FTR，接受 Terms & Conditions。完成标准："FTR done!!" 且三态 Registered/Success/XMPP_CONNECTED
6. panic 恢复（按需）：向 helpdesk 申请 6 位 PIN（5 天内用掉），CCTool 1-2 重做。完成标准：重注册成功退出 panic
7. 排障（失败时）：ccprocess.log + CCTool 状态页两入口，先分清连不上（6205/6209）还是注册被拒（6214）。完成标准：根因定位

判停点：

- checkCloudConfig 不过 → 停，先解决 DNS/代理/出站放行，别反复点 FTR
- 手里有备机想"FTR 顺手也做了" → 停，备机严禁 FTR，凭证靠克隆同步
- RTR 或 ccagent 进程没起就想做 PIN FTR → 停，两进程在跑是硬前提
- spadmin 找不到 Suite Id → 停，先查 RTR Enabled 开关（未启用时不显示），再疑许可文件

输出契约：FTR Registered + XMPP_CONNECTED 的注册凭证记录（Jid、时间、版本）+ 网络前提核查单。

## B — 边界

- 客户防火墙掐空闲会话时调 KeepAlive（默认 90 秒，MAO/WBM 改值动态生效），表现为 6204/6207 反复交替（p311）
- 自动 FTR 每 4 小时才试一次——网络一通就手动 CCTool 立即做，别干等（p296）
- "云服务不跑备机/PCS"与"lmsagent 跑全部 CS（备机只读）"是两条规则，排障先分域（nr-06）
- 云连接只覆盖注册与连通；RTR 许可状态监控在 RTR 卡；LMS 订阅对账在订阅许可卡
- 实验口径：DNS 192.168.1.250、代理示例 192.168.1.253:3128、PC 信任主机 192.168.1.9
