# SIP 协议机理与 OXE SIP 架构（协议栈、六组件、域名与空间冗余）

## R — 原文依据

> "SIP: Session Initiation Protocol • Protocol TCP/IP • TCP or UDP • IPv4 or IPv6 • IETF Standard: RFC 3261 • Application layer ... Establish, maintain, modify and terminate multimedia sessions"（p45）
> "SIP Gateway The SIP gateway acts as an interface between the Call Handling and SIP proxy server • SIP Dictionary Provides translation between PCX directory number and SIP URLs • External SIP gateway Declaration of a remote proxy/gateway of an external SIP system"（p57）
> "Two different IP addresses are used for the role addressing • The 'node name' should be used to reach the SIP server ... Only the main Communication Server replies to DNS requests by sending its main IP address"（p58-59）
> "!! IMPORTANT WARNING !! OXE is still having default domain name. Please configure a legitimate registered domain name, to prevent certificate errors."（p62）

出处：ENTPXTE403EN p44-63, p329。

## I — 自述

SIP 只管信令不管媒体搬运：会话的建立/维持/修改/终止归它，媒体协商靠 SDP、传输靠 RTP，信令可加 TLS。OXE 的 SIP 体系是六组件协作（同栖 sipmotor 进程域）：

| 组件 | 职责 |
|---|---|
| SIP Gateway（本地） | Call Handling 与 SIP 代理之间的接口 |
| SIP Dictionary | 分机号 ↔ SIP URL 翻译 |
| Proxy Server | 网内消息路由、权限控制、消息改写 |
| Registrar Server | 收终端注册并送位置服务器（租期钳制在 1800-86400s） |
| Location Server | URL → IP（注册库，sipregister 转储） |
| External SIP Gateway | 外部 SIP 系统的远端代理/网关声明（挂中继组） |

- 消息码表：请求十种（INVITE/ACK/PRACK/BYE/CANCEL/SUBSCRIBE/NOTIFY/REGISTER/REFER/INFO/UPDATE）；响应六类（1xx 临时 100/180、2xx 成功 200、3xx 重定向、4xx 客户端失败 400/403/404/406/488、5xx 服务器失败 500/502/503、6xx 全局失败 600/603）
- 呼叫时序（经代理）：INVITE（A 的 SDP）、100 Trying、180 Ringing（无 SDP）、200 OK（B 的 SDP）、ACK、RTP 双向、BYE 收尾
- 空间冗余接入：每台 CS 有物理 IP 与角色 IP，客户端一律用节点名（FQDN=节点名+域名）；客户 DNS 把 OXE FQDN 委托给 OXE 内部域名解析器，仅 Main 以主用角色 IP 应答
- 注册即服务：注册后才 in service；注销或超时后 IP 置 0.0.0.0、终端 out of service

## A1 — 书中案例

**OXE 域名定制**（p61-63，How-To）：

1. CS 上以 mtcl 登录，执行 netadmin -m；默认域名时先弹 IMPORTANT WARNING（防证书错误）。
2. 选 19/1/1 'View' 查看：显示 OXE DOMAIN=oxedomain.com、OXE FQDN=oxe.oxedomain.com（实验初始态）。
3. 选 19/1/2 'Create/Update' 输入新域名 company.com（实验口径）并应用。
4. 复核：管理工具 SIP/SIP Gateway → Edit/Consult 中 DNS local domain name 应变为 company.com。

**NOE 话机呼 SIP 话机**（p80-81）：

1. NOE 话机拨号，请求送本地 SIP 网关。
2. SIP 网关查 SIP 字典把号码换成 URL。
3. INVITE 发给 SIP 代理。
4. 代理查位置服务器拿已注册 IP。
5. 已注册则转发，终端振铃；注销或超时的终端 IP 置 0.0.0.0 并 out of service。

## A2 — 未来触发

使用情境：新站点 SIP 化前定域名；读 trace 定位 403/488/404；双机冗余下终端该连哪个地址；解释 SIP 和 RTP 的分工。

语言信号：RFC 3261 / SIP 消息 / 响应码 / 403 / 488 / REGISTER / INVITE / 六组件 / sipmotor / SIP 字典 / 位置服务器 / 空间冗余 / 节点名 / FQDN / oxedomain.com / 内部域名解析器。

与相邻能力区分：按这份地基去开通用户 → SIP 用户形态选型、SIP Device 开通；域名判定影响外线来话 → SBC 运营商接入。

## E — 可执行步骤

输入契约：站点域名（客户合法注册域名）、是否空间冗余、客户 DNS 管理权。域名未注册 → 判停先补域名。

1. 定域名：确认客户拥有正式注册域名；默认 oxedomain.com 必须改（证书错误源头）。完成标准：域名成文
2. 查现状：netadmin -m → 19/1/1 View，记录当前 OXE DOMAIN 与 FQDN。完成标准：现状有底
3. 改域名：19/1/2 Create/Update 输入新域名应用；管理工具只读核对 DNS local domain name。完成标准：两处一致
4. 冗余规划（如适用）：客户 DNS 把 OXE FQDN 委托给内部域名解析器；终端接入一律用节点名 FQDN。完成标准：解析链验证通过
5. 建立码表直觉：排障前先对响应码分类（4xx 客户端侧/5xx 服务器侧），再进信令采集。完成标准：能读基本时序

判停点：

- 客户 DNS 不能配委托 → 空间冗余解析不可用，先解决 DNS 管理权再谈冗余接入
- 域名仍是 oxedomain.com 就要装证书/开 SIP → 停，先改域名（n01）
- 需要逐字段讲 INVITE 报文 → 属协议基础课，声明边界不给报文课

输出契约：合法 OXE 域名与 FQDN + 冗余解析方案 + 后续开通动作的协议底座说明。

## B — 边界

- 默认域名 oxedomain.com 会引发证书错误，且域名参数只能 netadmin 改、管理工具只读（n01）
- 空间冗余下 DM URL 必须用 FQDN（DNS 可解），抄 IP 型 URL 会让备机接管后终端失联（n10）
- 来话归属判定靠 Request URI 域与本地网关三参数（OXE_Address/Machine Name/拼接）匹配，改域名后须同步网关参数（n47，机制性推断）
- 报文逐字段教学与 Wireshark 深度分析属协议基础课，本卡只给 OXE 语境下的读法
- p45-54 报文样例混合 R100.0/R101.0/R101.1 多版本截图（nr-07），跨版本参数以现场版本为准
