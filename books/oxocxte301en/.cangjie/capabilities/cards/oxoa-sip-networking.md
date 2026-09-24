# SIP 组网：公网 SIP 网关与私网互联（九 tab、注册验证、双向溢出）

## R — 原文依据

> "Don't forget to now configure the Outbound Proxy: gateway1.itsp1.com in the Domain Proxy tab … The following setting can only be configured after filling in the DNS tab!"（p46-47）
> "The Gateway index must be filled in later when the SIP Gateway is created"（p44）
> "Put the bandwidth at 5 minimum calls in order to allow external calls"（p48）
> "OMC/History and Anomalies/History Table … Message displayed: SIP registration success"（p54）
> "Calls may overflow on the public network in the event of saturation of the private network … Public calls between the 2 sites will be redirected to the private network as a priority"（p208）
> "Set the bandwidth to a minimum of 5 calls in order to make calls to the outside … Validate direct RTP"（p215）

出处：OXOCXTE301EN p37-56, p206-224。

## I — 自述

公网与私网 SIP 网关共用同一套配置面（SIP 网关九 tab + 编号计划 + VoIP 接入 + 中继组），差异只在编号计划与路由目的。固定顺序九步：

1. **LAN IP/DNS 核查**：改后复位 OXO
2. **编号计划**：公网填 DDI/安装号（私网填 Private Numbering Plan）
3. **VoIP 接入**：定通道数与网络类型，网关索引暂空
4. **中继组**：接入入组，调 Link-Cat 放行
5. **SIP 网关九 tab**：General（索引/标签/canonical）、DNS、Domain Proxy、Registration、Media、Identity、Protocol、Topology、Security
6. **SIP 账号**：Login/Password 并指向网关
7. **回填网关索引**到 VoIP 外线
8. **验证注册**：History Table 看 "SIP registration success"
9. **抓包**：Webdiag TCP Dump 选 SIP，Wireshark 分析

两条硬顺序（跳序必卡）：DNS tab 先于 Domain Proxy tab（配 DNS 后 IP 类型才变 dynamic）；网关索引回填在网关建好之后。

**Media 隐藏闸门**：带宽最少 5 通话 + RTP Direct 打勾，公网（p48）与私网（p215）同规则——带宽语义是"该网关允许的并发通话资源"，不设就外呼不通。

**私网组网四步**（在公网九步之上叠加）：

| 步骤 | 内容 | 关键参数 |
|---|---|---|
| 私网编号计划 | Private Numbering Plan 加站点号段 | N100-N199 base 100（实验口径） |
| 私网网关 | Domain Proxy 填对端 IP；Protocol 选 SIP Option 监督 | Media 带宽 ≥5 + RTP Direct |
| 私→公溢出 | ARS 表私网行加溢出子线，列表 index 2 指向公网主组 | 私网满后自动走公网，显示字符 T |
| 公→私优先强制 | 主中继行 base 改 ARS，加公转私行 + 透明行 | DID 呼叫强制走私网，显示字符 P |

## A1 — 书中案例

**公网 SIP 网关实验**（p37-56，厂商实验）：

1. 核对 LAN IP 与 DNS（192.168.1.246 / DNS1 .250 / DNS2 10.20.30.250，实验口径），改后复位。
2. 公网编号计划填 DDI 段 41100-41199、话务台 41000；必要时复制到 Restricted 计划。
3. 安装号填 210P41000（实验口径）。
4. 建 VoIP 接入 8 通道放主中继组 0，网关索引暂空；中继组加入接入并调 Link-Cat。
5. 建网关 ITSP1G1：按九 tab 顺序填（DNS tab 先于 Domain Proxy tab）。
6. Media tab 验证 RTP Direct 并把带宽设为最少 5 通话。
7. SIP 账号 pbxP/alcatel（实验口径），Gateway Parameters Index 指到 ITSP1G1。
8. 回 VoIP 外线回填网关索引。
9. History Table 出现 "SIP registration success" 即注册成功（p54）。
10. Webdiag（installer/Alcatel1，实验口径）TCP Dump 选 SIP 抓包，Wireshark 分析。

**私网组网实验**（p206-224，两台 OXO）：

1. 拓扑按 POD 号取 N（192.168.N.246），勿与其它 lab 产生 IP 冲突（p208 Attention）。
2. 私网编号计划加 N100-N199 base 100；私网 VoIP 接入按带宽定通道数入副中继组。
3. 私网网关 Domain Proxy 填对端 IP，Media 带宽最少 5 通话，Protocol 选 SIP Option。
4. 无 ARS 测试：经中继组前缀 400 呼对端私网号（OXO1 打 (400) 21xx）。
5. 配 ARS：内部编号计划 Secondary Trunk Group 行 base=ARS、NMT=Keep、Private=Yes。
6. ARS 表加对端前缀行，中继组列表指向含 VoIP 接入的副中继组；直拨 21xx 测试。
7. 私→公溢出：私网行加子线，列表 index 2 指向公网主组 0；占满 2 通道后呼叫显示 T。
8. 公→私强制：主中继行 base 改 ARS 加公转私行；DID 呼叫被强制走私网显示 P（p224）。

## A2 — 未来触发

使用情境：对接 SIP 运营商；注册不上怎么排；Domain Proxy 找不到参数位；外呼不通查哪里；两站点用 SIP 互联；私网饱和怎么溢出到公网；DID 呼叫强制走专线。

语言信号：SIP 网关 / SIP gateway / ITSP / 运营商中继 / Domain Proxy / Outbound Proxy / 注册 / registration success / 中继组 / trunk group / 私网 / 组网 / 溢出 / overflow / 双向 / 站点互联 / 5059。

与相邻能力区分：路由选路与号码变换规则归 ARS 套件能力；中继加密（TLS/SRTP）归证书套件能力；本能力到"注册成功 + 双向溢出行为验证"为止。

## E — 可执行步骤

输入契约：运营商对接参数（或对端站点 IP/号段）、本站 IP 规划、并发话务量、中继组与链路类别规划。运营商参数不全 → 判停先收集，不要用实验值顶替。

1. 核查 LAN IP/DNS 并复位；确认 DHCP 池规划（p34 口径，注意 nr-02 两处不一致）。完成标准：网络可达
2. 编号计划：公网填 DDI 段与安装号（私网加 Private Numbering Plan 段）。完成标准：号码落表
3. 建 VoIP 接入（通道数按带宽勘测）入中继组，调 Link-Cat 放行。完成标准：接入入组
4. 按九 tab 建网关：DNS tab 先填，再配 Domain Proxy；Media 设带宽最少 5 通话 + RTP Direct。完成标准：九 tab 全填
5. 建 SIP 账号指向网关索引；回 VoIP 外线回填网关索引。完成标准：账号与外线关联
6. 验证：History Table 出现 "SIP registration success"；试呼本站 DDI 与外呼。完成标准：注册与呼叫双通
7. （私网）加 ARS 双向四步：私网行、溢出子线、公转私强制行、透明行。完成标准：P/T 字符验证通过
8. 排障分层：注册层查 History Table，信令层 Webdiag 抓包，分析层 Wireshark。完成标准：问题定位或升级支持

判停点：

- 运营商要求 TLS/SRTP 或 SIPS URI → 转证书套件能力（SIPS 在 OCE-FE 不支持要提前声明）
- 站点带宽未知 → 不承诺通道数，先勘测（通道数按"该网关允许的并发通话资源"定）
- 注册失败且账号/参数核对无误 → 查拓扑（ETH0）与安全 tab 明文默认，再抓包比对 SIP 消息
- 短号与紧急号码需求 → ADL 表管理在书外（n63），生产割接前必须补测紧急呼叫

输出契约：注册成功的 SIP 中继（公网或私网）+ 编号计划落表记录 + 抓包存档 + 溢出行为验证结论（P/T 字符）。

## B — 边界

- 全部实验参数（ITSP1、pbxP/alcatel、号段、N 值）为 RLAB 口径，生产按运营商与客户网段整体替换（n64）
- 默认 Security tab 为明文 SIP（n07）：生产要加密走 TLS/SRTP 章，不能默认当作已加密
- 公网编号计划配置必要时复制到 Restricted 计划（n04），漏配时受限时段 DDI 映射落空
- 生产运营商的注册超时、鉴权方式、号码变换规则在书外，需按运营商合同勘测
- 短号/紧急号码 ADL 管理书内未覆盖（n63）；Webdiag 登录 installer 密码为客户环境值（实验 Alcatel1 仅教室口径）
