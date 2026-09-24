# OXE 侧 WebRTC 网关配置九件套（SIP TG/可信 IP/Rainbow type 网关/ARS/判别器/回调）

## R — 原文依据

> "AN IP DOMAIN WITHOUT COMPRESSION BUT WITH COMPRESSION RESOURCES (GD/OMS) IS REQUIRED ON THE SYSTEM FOR A CORRECT WORKING MODE OF THE WEBRTC GATEWAY."（p180）
> "Gateway type Rainbow type … Trusted From header Checked (true) … Support G711 YES"（p181）
> "Call Number 1 … Area Number 1 … Schedule number -1 … Number of Digits 17 (length of numbers managed by the Rainbow agent)"（p185）
> "Basic Number DEF • No. Digits To Be Removed 0 • Digits to Add BBB"（p187）

出处：RAINXTE003EN p177-197。

## I — 自述

网关装好只是第一步，OXE 侧要配齐九件套才通（p177-190）：

| 件 | 配置项 | 关键口径 |
|---|---|---|
| 1 | 国家码 | System 参数 SG Country Code 按站点填 |
| 2 | SIP trunk group | T2 类型、T2 Specification=SIP、Q931 取 ISDN all countries |
| 3 | 可信 IP | 把网关 IP 加入 SIP Trusted IP Addresses |
| 4 | SIP 外部网关 | Gateway type=Rainbow type、端口 5060/UDP、监督定时器 380、DTMF 动态载荷 101、仅 G711 |
| 5 | IP 域 | 必须无压缩（High bandwidth）且系统带压缩资源（GD/OMS），Warning 级前提 |
| 6 | CDT | 编号命令表挂外部 SIP 网关——ARS 用 SIP TG 的前提 |
| 7 | ARS 路由 | Route List 挂 TG 与 CDT，Time-based Route List 指向默认表 |
| 8 | BBB 前缀与判别器 | 前缀 BBB、判别器规则 Call Number 1 / Area 1 / route list / schedule -1 / 位数 17 |
| 9 | 回调三件套 | CSTA 开关 Yes + 外部回调翻译表（DEF 变 BBB、删 0 位）+ 专用实体挂网关 TG |

判别器五元组固定语义（p185）：前缀 BBB 与判别器号可按站点调整，但位数 17 与 schedule -1（用默认时段路由表）语义固定——17 位即 Rainbow agent 管理的号码长度。

CPaaS 补充（公司含纯 Rainbow 用户时）：用户 COS 勾 Calling name display（主叫名显示）；Remote Extension Parameters 选 CLI Format（Standard 送外部号/Private 送内部号）；系统参数配 NPD for external forward。

维护命令族（p191-195）：sipextgw -l 看外部 SIP 网关在服状态；lookars i 交互验 ARS 解析；motortrace 配 traced 抓 SIP 信令（killall traced 停）；multidevice/zdpost/remotesets 验 tandem 与 REX 的 BBB 号。

## A1 — 书中案例

**九件套配置实验**（p177-195）：

1. 系统参数填国家码（实验口径取法国 33）
2. 建 SIP trunk group：TG IP 5、Type T2、名 WebRTC、T2 Specification 选 SIP
3. 核 IP 域：域 0 的 Intra/Extra bandwidth 均设 High bandwidth（无压缩）
4. 可信 IP 添加网关地址（实验口径 192.168.1.15，见 book/overview）
5. 建 SIP 外部网关：Rainbow type、5060/UDP、监督 380、DTMF 101、仅 G711、Trusted From header 勾选
6. 建 CDT：表 5 的 Command I 挂外部 SIP 网关 5
7. 建 ARS Route List 5 挂 TG 5 与 CDT 5，Time-based Route List 1 指向它
8. Prefix Plan 建前缀 BBB 挂逻辑判别器；实判别器 5 号按五元组建规则
9. 用户与 Ghost Z 所在实体的 Discriminator Selector 关联判别器
10. 回调：CSTA 开关 Yes、翻译表规则 DEF 变 BBB、建专用实体挂网关 TG
11. lookars i 输入 BBB 加分机验证解析链；remotesets 核对 REX 的 17 位号
12. VoIP 四项测试：computer 路由呼出、来话计算机接听、呼纯 Rainbow 用户、纯 Rainbow 用户呼入

## A2 — 未来触发

使用情境：网关装好了但 VoIP 不通；ARS/判别器怎么配；话机想用通话记录回拨 Rainbow 分机；主叫名显示不对。

语言信号：SIP trunk / T2 / 可信 IP / trusted IP / Rainbow type / G711 / IP 域 / 压缩 / CDT / ARS / BBB / 判别器 / discriminator / 回调 / callback / lookars / sipextgw / 主叫名 / CLI。

与相邻能力区分：

- 网关 VM 与升级 → 网关部署能力
- REX/tandem 与 Ghost Z → 远程延伸路由能力
- 话务台与监督 → 两套话务台能力（路由卡）

## E — 可执行步骤

输入契约：网关已部署激活（部署能力交付）、站点编号计划、是否含纯 Rainbow（CPaaS）用户、回调翻译表现状。判别器/表号规划与存量冲突 → 停，先出编号方案。

1. 核 IP 域：确认网关流量所经域无压缩且系统有压缩资源。完成标准：Warning 前提成立（p180）
2. 建 TG 与可信 IP：T2/SIP 类型、网关 IP 入可信清单。完成标准：TG 在册
3. 建 Rainbow type 网关：逐字段按取值表填（端口/定时器/DTMF/编解码）。完成标准：字段与表一致
4. 建 CDT 与 ARS：命令表、Route List、Time-based 表三层挂接。完成标准：ARS 链完整
5. 配 BBB 前缀与判别器：五元组建规则并做实体关联。完成标准：lookars i 解析直达 Route List
6. 配回调三件套：CSTA 开关、翻译表、专用实体。完成标准：话机通话记录可回拨 Rainbow 号
7. CPaaS 补充（如需）：主叫名 COS、CLI Format、NPD 参数。完成标准：纯 Rainbow 用户互叫主叫身份正确
8. 验收：四项 VoIP 测试逐项记录。完成标准：来去话与主叫身份全部符合预期

判停点：

- VoIP 不通且域配过压缩 → 先查件 5（隐性前提，表象常是单通/媒体异常，n19）
- lookars 解析不达 Route List → 逐层查前缀、逻辑判别器、实体关联，不乱改 ARS 表
- 生产站点要改编解码 → 先与网关侧能力核对（书内仅 G711 为实验口径，p181）
- 存量回调翻译表冲突 → 必须走专用实体隔离，不与现有表混挂（p187）

输出契约：OXE 侧九件套配置清单 + lookars/remotesets 验证输出 + 四项 VoIP 测试记录。

## B — 边界

- SIP 外部网关仅 G711、实验 IP/表号/实体号均为实验口径；生产按站点重规划并核对网关能力（p181）
- 维护命令各管一段：深排障在 VoIP calling Troubleshooting guide 与 TC2462（p194，n28）
- 池化场景的溢出参数与 406 语义在共享池与容量能力展开
- 回测技巧：把 REX 里的 BBB 号设成缩位拨号可从 OXE 话机直拨验证到 Rainbow 客户端（p188 Tips）
