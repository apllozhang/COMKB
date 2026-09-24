# 终端生态：PIMphony、SIP 话机与软话机接入（含媒体三处理）

## R — 原文依据

> "The OXO Connect is a Registrar for its SIP client … The OXO Connect is a B2BUA Back-to-Back User Agent for the SIP calls"（p140-141）
> "A voice communication is processed in one of these 3 ways: • Through DSP channels … • RTP proxy: … packets are only routed by OXO … • Direct RTP: … the most optimal solution"（p148）
> "SIP username: Directory number of the subscriber … Registrar and Proxy SIP: OXO IP@:5059 … Registration timer: >=120 seconds … Transport protocol: Prefer UDP"（p153）
> "SIP Phones do not support nomadic mode"（p147）
> "By default, the service is deactivated. Internet connection is required to update PIMphony."（p127）

出处：OXOCXTE301EN p119-165, p166-172。

## I — 自述

终端接入三条线：

**SIP 话机/软话机接入基线**（p149-153）：

- 注册/代理地址 OXO IP:5059；SIP 用户名=分机号，注册密码在订阅户 IP/SIP 参数里读
- 注册计时器 ≥120 秒；传输优先 UDP；SNTP 由 OXO 提供
- Basic 与 Open SIP 话机都在订阅户列表建（IP Subscriber 改类型），均需虚拟 MAC+注册密码
- Open 型多一项 Conference Bridge Allowed（SIP Enhanced 5 方会议，系统最多 3 路）

**媒体三处理取舍**（p144-148）：

| 路径 | 机制 | 取舍 |
|---|---|---|
| DSP 通道 | 压缩解压 | 非最优，耗 DSP |
| RTP proxy | 两腿同编解码同 framing 时仅路由不压缩 | 省 DSP/降 CPU，路径仍经 OXO |
| Direct RTP | 端点直连 | 最优；TLS/SRTP 场景不可用 |

编解码透传开关（话机侧 OMC/VoIP parameter/SIP Phone 与中继侧 External lines/SIP/Media 各自独立）：关=仅 OXO 六编解码（G.711/G.723/G.729/G722/G722.2/OPUS）；开=按终端能力全量音视频。SIP 话机不支持游牧模式（p147）。

**PIMphony**（p119-138）：

- profile 阶梯 Basic（免费）、Pro（弹窗+VM 管理）、Team（监督与工作组）、Attendant（PC 话务台）逐级递进
- 在线更新默认停用且需互联网，全局（Central Services）与每用户（Serv.Cent/PIMphony tab）两级策略
- 基于 license，可与任何设备关联（SIP 话机除外）；8088 安卓话机仅 v2+ 受支持（p105）

## A1 — 书中案例

**Zoiper 软话机实验**（p155-165，厂商实验）：

1. OMC 订阅户列表 Add 新用户为 IP Terminal（如 105），类型改 Open Sip Phone。
2. Details 的 IP/SIP 按钮读该终端 SIP 密码；勿改既有 MicroSIP（100-103）。
3. PC 装 Zoiper（管理员运行），Continue as a Free user，不更新。
4. 登录填 105@192.168.1.246 与 SIP 密码（实验口径）。
5. Settings 的 SIP Accounts 给 Domain 补端口 192.168.1.246:5059，离开菜单记得保存 Yes。
6. 从另一台话机呼叫 105 验证注册与通话（p165）。

**SIP 话机维护**（p166-172，讲义+操作）：

1. Webdiag 的 VoIP information 看 IP/SIP/DSP 状态与 SIP sets 列表。
2. Traces→Network Capture 对话机抓包。
3. IP 设备远程 trace：NOE 话机自动解锁；SIP 话机手动解锁且用完必须手动锁回（n19）。

## A2 — 未来触发

使用情境：第三方话机/软话机注册不上；通话单向没声或音质差；要不要开编解码透传；PIMphony 装哪版 profile；在线更新策略；8088 能不能上 OXO；SIP 话机抓包排障。

语言信号：SIP 话机 / SIP phone / Open SIP / Basic SIP / Zoiper / 软话机 / 5059 / 注册密码 / 编解码 / codec / 透传 / pass-through / RTP proxy / Direct RTP / DSP / PIMphony / profile / 在线更新 / 8088 / ALE-2 / ALE-3。

与相邻能力区分：注册排障的底层（History Table/抓包）与中继归 SIP 组网能力；会话计时器 sipphone_sess_tim 等 noteworthy 归维护工具能力；话机共享（Hot Desking/Multiset）归共享终端能力。

## E — 可执行步骤

输入契约：话机型号与白名单状态（DSPP）、分机号与命名、媒体路径偏好、PIMphony 的 license 与用户清单。非白名单第三方话机 → 按 RFC 符合度 best effort（p143）提前声明。

1. 声明终端：订阅户列表建 IP Subscriber、改类型（Basic/Open SIP）、虚拟 MAC、读注册密码。完成标准：账号就绪
2. 话机侧：注册/代理填 OXO IP:5059、用户名=分机号、计时器 ≥120 秒、UDP 优先。完成标准：注册成功
3. 媒体定策：ALE IP 话机优先 Direct RTP；需省 DSP 用 RTP proxy；核对透传开关两侧独立。完成标准：媒体路径成文
4. （PIMphony）全局开更新、用户预配 profile、装客户端、向导关联（或建 PC Multimedia 终端）。完成标准：软话机可用
5. 排障：Webdiag 看 SIP sets 状态与注册拒绝消息；抓包比对 SIP 信令。完成标准：问题定位

判停点：

- 注册不上且参数无误 → 查 Domain 是否漏 :5059 端口（n18）、计时器是否 <120 秒
- SIP 话机用户要游牧/移动 → 不支持（p147），改方案并声明边界
- 通话异常先分层 → 注册层（History Table）与媒体层（三处理/透传）分开查
- SIP 话机远程 SSH 用完不锁回 → 禁止：留暴露面（n19）；NOE 话机自动、SIP 话机手动

输出契约：终端接入清单（型号/分机/媒体路径）+ PIMphony profile 与更新策略表 + 排障记录。

## B — 边界

- 白名单清单在 DSPP（p143）；8088 仅 v2+（p105），Private Store 默认禁装应用且 GPS/Wi-Fi 类 APK 装不上（p107）
- PIMphony 是 Windows 专用软话机（时代产物）：新项目优先评估 Rainbow/桌面话机路线，PIMphony 按存量维护口径对待
- PIMphony 实验虚拟课堂不可实操（p129）；更新与注册均需互联网，封闭内网站点先确认策略（n15）
- TDM 系列话机耗 1 个 VoIP 资源（p147）；SIP Enhanced 会议 5 方、系统最多 3 路（p151）
- 实验账号/分机号（105、100-103 MicroSIP）为实验口径
