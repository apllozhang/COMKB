# SIP Device 用户开通（私网、中继组、本地网关、代理、注册器、建户、验证）

## R — 原文依据

> "Remember that a call from/to a 'SIP device' user requires the OXE local SIP gateway. So, in a first step, it is mandatory to configure the private SIP Trunk Group, the local SIP gateway, the SIP proxy…"（p85）
> "SIP Access number: up to 992 TS per SIP TG (maximum 32 virtual accesses * 31 TS) They must be allocated by pair (2, 4, …..) 2 accesses = 62 communications"（p86）
> "Warning IN CASE OF MODIFICATION OF THE NUMBER OF VIRTUAL ACCESSES FOR SIP, A RESTART OF THE SYSTEM IT'S NECESSARY"（p86）
> "THE SIP DEVICE MUST BE DECLARED AS TRUSTED HOST IN THE CS INTERNAL FIREWALL (NETADMIN -M / SECURITY)."（p89-90）

出处：ENTPXTE403EN p84-94。

## I — 自述

SIP Device 是"远端子网设备"（会议话机/门禁/视频），开通是九节主线，基础设施先行：

| 节 | 配置对象 | 关键值（标准口径） |
|---|---|---|
| 1 | 私网 | Translator/Network Routing Table，选空闲号（勿占 ABC/VPN 号），协议 ABC-F |
| 2 | 私有 SIP 中继组 | T2 型 + T2 Specification=SIP，远端网络=私网号；2 接入=62 路并发，上限 992 TS（32×31），接入成对分配 |
| 3 | 本地 SIP 网关 | 关联子网/中继组/角色 IP/主机名；代理端口 5060、TLS 5061、MTLS 6261；订阅 1800/86400s；会话计时器 1800（最小 900，方法 UPDATE）；SDP in 18x=True；DTMF payload 101 |
| 4 | SIP 代理 | 认证 SIP Digest、realm=OXE；防隔离 Framework 3s/50 条、隔离期 1800s；TCP 长消息勾选 |
| 5 | 注册器 | 租期 Min 1800s / Max 86400s |
| 6 | SIP 字典 | 重名用户加 alias 区分 |
| 7 | 隔离/信任 IP | 高频设备加 Trusted IP 白名单；自动隔离看 /usr4/tmp/sipalarm.log（f003） |
| 8 | 建户 | Set Type=SIP device + SIP 密码 + 防火墙信任主机（/etc/hosts 核对） |
| 9 | 验证 | sipregister/sipdict -l（type 2=Device）/trkstat/内外呼测试 |

- 中继组 TS 是信令占位：SEPLOS 呼叫不占 TS，SIP Device 呼叫占 TS
- 参数纪律：端口 5060 等标准值仅在客户端非标时改；initial time-out/T2/TLS timer 只在支持或研发建议下改；Recursive search 暂未使用

## A1 — 书中案例

**31060 会议话机开通**（p84-94，How-To）：

1. 私网：Network Routing Table 建 Network Number=10、Protocol=ABC-F、Associated Ext SIP gateway=-1。
2. 中继组：Trunk Groups Create：ID=10、T2、Q931=ABC-F、Remote Network=10、T2 Specification=SIP。
3. 虚拟接入：Number of SIP Accesses=2（默认）；Warning：改接入数必须重启系统，TRKSTAT 显示 Free 不代表生效。
4. 本地网关：SIP Subnetwork=10、SIP Trunk Group=10、IP=192.168.1.3（实验口径）、Proxy Port=5060、SDP in 18x=True。
5. 代理：Minimal authentication=SIP Digest、Framework Period=3、Nb Message By Period=50、Quarantine Period=1800。
6. 注册器：Min/Max Expiration=1800/86400。
7. 建户 31060（Set Type=+SIP device、SIP Passwd=12345 实验口径）并加防火墙信任主机。
8. 终端 MicroSIP 填 SIP 密码注册；验证 sipregister 见 31060、trkstat 10 显示 62 路 TS、31060 进出呼成功。

## A2 — 未来触发

使用情境：客户买来会议话机/门禁对讲/视频设备要接入 OXE；SIP Device 注册不上；中继组扩容；设备被隔离 30 分钟。

语言信号：SIP device / 会议话机 / 门禁 / 视频设备 / 私网 / private SIP trunk group / 虚拟接入 / 62 通道 / 992 TS / 本地 SIP 网关 / 5060 / 信任主机 / sipregister / trkstat / 隔离 / quarantine。

与相邻能力区分：先决定该不该用 Device 形态找用户形态选型；注册不上要抓信令找 SIP 跟踪排障；这台设备要走话机业务属形态上限问题回选型。

## E — 可执行步骤

输入契约：设备型号与 SIP 能力、可用私网号、并发路数需求、设备 IP（可达 CS）。设备不支持 SIP → 判停换形态。

1. 规划私网：选空闲网络号（勿占 ABC/VPN），协议 ABC-F。完成标准：私网号登记
2. 建私有 SIP 中继组：T2 + Specification=SIP + 远端网络=私网号；每系统仅一个 ABC 型私有中继组。完成标准：trkstat 可见
3. 配虚拟接入：成对分配（2 起）；若改动接入数 → 排重启窗口，改完必须重启。完成标准：62 路/2 接入口径确认
4. 建本地 SIP 网关：挂子网与中继组、角色 IP、端口 5060、SDP in 18x、会话计时器；标准值不动。完成标准：sipgateway 输出正常
5. 配代理与注册器：SIP Digest 认证；Framework 3s/50 条防隔离；租期 1800/86400。完成标准：参数落库
6. 建户并加信任主机：Set Type=SIP device、设 SIP 密码；netadmin 登记设备 IP 为信任主机并核 /etc/hosts。完成标准：sipregister 见该分机
7. 终端注册与验证：终端填注册服务器与密码；trkstat 看占用、sipdict -l 看 type=2；做进出呼。完成标准：双向通话

判停点：

- 私网号与 ABC/VPN 冲突 → 停，换号，不强行复用
- 改了虚拟接入但没重启 → 停，TS 显示 Free 也未生效（n04），先排重启
- 终端完全无响应 → 先查信任主机 /etc/hosts（n07），不急着抓包
- 客户要求 Device 参与 CTI/坐席/入组 → 停，形态上限（n02），回选型卡

输出契约：可注册可通话的 SIP Device 用户 + 私网/中继组/网关参数台账 + 验证记录。

## B — 边界

- 修改虚拟接入数必须重启系统，TRKSTAT 空闲不算数（n04）
- 端口与计时器默认值别乱动；Recursive search 配了也没效果（n05）
- 一切主动向 CS 发请求的设备都要登记信任主机，漏配的典型表现是完全无响应（n07）
- 3 秒超 50 条消息会被自动隔离 30 分钟，高频设备提前配 Framework 或 Trusted IP（n06）
- 数值口径：62 通道/992 TS/端口/租期等为标准值；实验 IP/密码（192.168.1.3、12345）为实验口径，生产替换
