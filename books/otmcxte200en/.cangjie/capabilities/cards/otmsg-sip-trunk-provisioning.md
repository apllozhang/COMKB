# OXE 侧 SIP 对接 OTMC（trunk group/external gateway/trusted/编解码）

## R — 原文依据

> "Trunk Group Type: Select 'T2' type … Q931 Signal variant: Select ABC-F … T2 Specification: Select SIP"（p103）
> "Port number: 5040 • Transport type: TCP … Gateway type: ICE type"（p105）
> "The OTMC server IP address must be declared as trusted IP address."（p107）
> "Compression type: G 729 … Routing Optimisation: Yes"（p108）

出处：OTMCXTE200EN p102-108（c05、f14、p09/p10、n29 归并）。

## I — 自述

OXE 与 OTMC 的话路对接是四段参数结构（8770 或 OXE mgr 均可配）：

1. **SIP trunk group**：ID 全网唯一、类型 T2、T2 Specification=SIP、Q931 变体 ABC-F、远端网络号空闲且异于 OXE 网络号、节点号取 post-install 定义的值；本地参数 Dialing end to end=No、DTMF end to end=No（默认即对）；SIP 虚拟接入数默认 2（可改）
2. **SIP external gateway**：OTMC 必须声明为外部 SIP 网关（Connection 用户由此访问 OTMC 的 SIP 服务）。参数清单：

   - Remote domain=OTMC FQDN、端口 5040、传输 TCP、Gateway type=ICE type
   - 勾 Ignore inactive/black hole 与 Contact with IP address
   - 100 REL：出向 Supported、入向 Not requested
3. **Proxy/Gateway/Registrar/Trusted**：Proxy 认证 None；SIP Gateway 的 Subscribe Min Duration=600、本地 DNS 域；Registrar 最小/最大有效期按需；Trusted IP Addresses 必须含 OTMC 服务器 IP
4. **全局**：编解码 G.729、多算法 False；DPNSS 前缀（Translator/Prefix plan 建条目）用于优化经中继组的转接，必须把 Routing Optimisation 设为 Yes 才生效

端口对照表：

| 端口 | 用途 |
|---|---|
| 5040/TCP | OTMC 声明为 SIP external gateway 的 SIP 端口 |
| 5060 | OXE 侧 SIP 端口（OTMC 拓扑声明 OXE 时填） |
| 2570 | OXE PRS 端口（话机 GUI 显示链路） |

## A1 — 书中案例

**SIP 对接实验**（c05，OTMC FQDN/IP 等环境值见 book/overview）：

1. 建 SIP trunk group：Trunk Groups 右键 Create，录 ID、类型 T2、名称 SIP、Q931 ABC-F、T2 Specification=SIP
2. 核对 trunk 本地参数：Dialing end to end=No、DTMF end to end signal=No
3. 核对 SIP 虚拟接入数（默认 2，按 OXE 与 OTMC 互联需要调整）
4. 声明 OTMC 为 SIP external gateway：Remote domain 填 OTMC FQDN、Port 5040、TCP、Gateway type=ICE type，勾 Ignore inactive/black hole、Contact with IP address，100 REL 按口径
5. 核对 SIP Proxy：Minimal authentication method=None
6. 核对 SIP Gateway：远端网络号与 trunk 组号带出、SIP Subscribe Min Duration=600、本地 DNS 域
7. 核对 SIP Registrar 最小/最大有效期；Trusted IP Addresses 建条目填 OTMC 服务器 IP
8. 全局编解码：Compression type=G 729、Multi. Algorithms=False
9. 建 DPNSS 前缀条目（实验示例 D1234，实验口径）并把 Routing Optimisation 设为 Yes

## A2 — 未来触发

使用情境：信箱呼叫不通的通道侧排查；新 OXE 接既有 OTMC；空间冗余站点对接；运营商 trunk 与 OTMC trunk 混淆；DPNSS 前缀要不要配。

语言信号：SIP trunk / trunk group / T2 / ABC-F / external gateway / 5040 / trusted IP / G.729 / DPNSS 前缀 / Routing Optimisation / ICE type / 话路对接。

与相邻能力区分：声明与拓扑（端口 2570/5060 在哪填）→ otmsg-declaration-sync；对接完成后建用户验证业务 → otmsg-user-mailbox-provisioning。

## E — 可执行步骤

输入契约：声明同步完成（otmsg-declaration-sync）、OTMC FQDN 可解析、8770 或 OXE mgr 配置入口可用。

1. 建 trunk group：按四段清单第一段录全参数。完成标准：trunk 创建、远端网络号合法
2. 声明 external gateway：OTMC FQDN + 5040/TCP + ICE type。完成标准：网关在册
3. 配 trusted 地址：加入 OTMC 服务器 IP。完成标准：OTMC IP 受信任
4. 核对 Proxy/Gateway/Registrar：认证 None、Subscribe 600、DNS 域就位。完成标准：三处一致
5. 全局优化：G.729 单算法、DPNSS 前缀、Routing Optimisation=Yes。完成标准：转接优化生效
6. 联动验证：建用户后走信箱业务端到端测试（转 otmsg-user-mailbox-provisioning）。完成标准：呼叫通道打通

判停点：

- 信箱呼叫不通 → 按四段顺序排查：trunk 类型/变体、gateway 5040/TCP/ICE type、trusted 缺 OTMC IP、编解码两侧一致
- OXE 是空间冗余（spatial redundancy）站点 → 停，须按 TC1652 另行声明外置信箱 SIP 网关，书内零步骤（n29）
- 与出局运营商 SIP trunk 混淆 → 停，这是 PBX 与信箱服务器的内部对接中继，仅一条、指向 front node

输出契约：OXE 侧 SIP 对接参数就位（trunk/gateway/trusted/全局四段）+ 呼叫通道验证记录。

## B — 边界

- SIP Registrar 有效期书中为"按需记录"口径，未给具体数值——不编造
- DPNSS 前缀实验示例 D1234（实验口径），生产按客户编号计划；DPNSS 缩写书中未展开全称
- 空间冗余场景唯一出处是 TC1652（p105 Warning），本书不含操作步骤
- 8770 与 OXE mgr 两侧界面均可配，书中以 8770 界面为主
- 实验 FQDN/网段等环境值见 book/overview
