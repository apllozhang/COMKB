# OTFC 与 OXE 的 SIP 通道集成（OTFC 侧声明、OXE 侧 MGR 七步、传真抓包）

## R — 原文依据

> "SIP configuration • Local SIP UDP port: 5360 • Activate SIP message in log files (for maintenance) • SIP authentication"（p142）
> "In Driver/Peer List • Declare the 2 call servers: IP addresses or FQDN (if managed in DNS server) … In Driver/Dial Plan • For the number pattern concerned, specify the 2 call servers declared previously with a priority order"（p145-146）
> "Use MGR or Omnivista 8770 to manage. mtcl is the default login & password … Select mgr / Trunk groups/ Create"（p152）
> "To manage SIP connexion between the OTFC & OmniPCX Enterprise, you have to refer to the Technical Communication: • TC3048"（p141）

出处：OTFCXTE200EN p140-155（含 How-To 实验 6）、p148-150（Maintenance 抓包）。

## I — 自述

传真话路是收发传真的命脉，两侧都要配，缺一边就不通：

1. **OTFC 侧**：SIP 基础配置——本地 SIP UDP 端口 5360（防火墙放行与排障核对点）、SIP 认证、维护时可激活 SIP 消息日志；OXE 声明可增改；Dial Plan 单 PBX 默认所有号码（*）路由到该 PBX
2. **OXE 侧（MGR 七步）**：Trunk groups/Creat、SIP gateway、Proxy、Trusted IP addresses/Creat、SIP Ext gateway/Creat、Translator/Network Routing Table、Prefix plan/Creat——菜单序列骨架，参数细节一律参照 TC3048
3. **空间冗余**：Driver/Peer List 声明 2 台呼叫服务器（IP 或 FQDN），Driver/Dial Plan 对相关号码模式排优先级
4. **抓包三法**（OXE 呼叫服务器 mtcl 账号）：CHtrace（tuner/actdbg/mtracer 滚动日志）、SIP trace（motortrace/traced）、网络包（tcpdump -s 2000 -w，FTP bin 模式取回 Wireshark 分析）

多网关多站点：Fax Center 可配多个 SIP 网关按号码段分流（如 GW1 对 1200-1500、GW2 对 3300-3800，实验口径示例）；OXE 侧必须建 SIP private trunk。

## A1 — 书中案例

**OXE 侧 SIP 网关配置**（p151-155，实验 6）：

1. 终端登录 OXE 呼叫服务器：mtcl/mtcl（默认口径），进入 csa 后执行 mgr
2. mgr / Trunk groups / Create 建 SIP 中继组
3. mgr / SIP / SIP gateway 配网关参数（细节照书内截图与 TC3048）
4. mgr / SIP / Proxy 配代理
5. mgr / SIP / Trusted IP addresses / Create 把传真服务器列入信任
6. mgr / SIP / SIP Ext gateway / Create 配外部网关
7. mgr / Translator / Network Routing Table / 5 配路由表
8. mgr / Translator / Prefix plan / Create 把目录号 #31600-31699 指向传真网关（实验口径号段）

**CHtrace 抓包**（p148）：tuner km、tuner clear-traces、tuner +cpu +cpl +at hybrid=on、actdbg all=off sip=on abcf=on、mtracer -ag -d -1 /DHS3dyn/tmp/CHtrace -s 1000000 -f 90，停止 Control C 或 killall mtracer。

## A2 — 未来触发

使用情境：OTFC 装好了发不出/收不到传真；OXE 和 OTFC 之间 SIP 不通；OXE 有两台呼叫服务器要做冗余；多台 OXE 接一台 OTFC；传真时通时断要取证；SIP 信令要看日志。

语言信号：SIP / T.38 / G.711 / 5360 / trunk / 中继组 / MGR / mtcl / Trusted IP / Prefix plan / 前缀计划 / dial plan / 拨号计划 / Peer List / 空间冗余 / 抓包 / CHtrace / motortrace / tcpdump / Wireshark / TC3048。

与相邻能力区分：装系统与许可归首次交付能力；邮件入口不通归邮件与 Exchange 集成能力；来传真路由到人归目录与路由能力；服务日志归服务运维能力。

## E — 可执行步骤

输入契约：OTFC 已安装且 XMSMTPGateway 等服务正常（见首次交付能力）、OXE 的 mtcl/mgr 访问权限、两侧 IP/号段规划、TC3048 文档在手。没有 TC3048 不开工。

1. OTFC 侧 SIP：确认本地 UDP 5360、SIP 认证口径，维护场景激活 SIP 消息日志。完成标准：SIP 配置页参数落定
2. OTFC 侧声明 OXE：核对安装时声明的 PBX，多 PBX 场景逐台声明。完成标准：每台 OXE 在声明列表内
3. Dial Plan：单 PBX 保持默认（* 全路由）；多 PBX 按号码模式分派。完成标准：出呼号码模式全覆盖
4. 空间冗余（如适用）：Peer List 声明 2 台呼叫服务器，Dial Plan 排优先级。完成标准：两服务器均在列表且优先级明确
5. OXE 侧 MGR 七步：Trunk groups、SIP gateway、Proxy、Trusted IP、SIP Ext gateway、Network Routing Table、Prefix plan。完成标准：七步全部落配置，参数以 TC3048 核对
6. 联通验证：两端互发测试传真（书内口径以 p116 两用户互发 + 管理端监控为准）。完成标准：测试传真双向可达
7. 故障取证（如不通）：按 mtcl 账号抓 CHtrace / SIP trace / tcpdump，FTP bin 取回 Wireshark 按 SIP 过滤分析。完成标准：拿到可分析的 trace 文件

判停点：

- 手头没有 TC3048 → 停，向 ALE 渠道索要后再上站；本书只有菜单骨架，照抄参数大概率回工
- 抓包发现 SIP 请求根本没到对端 → 先查防火墙/路由（5360 放行），再查 Trusted IP 列表，不要急着改两侧配置
- 客户要求加密话路（SIP/TLS）→ 停，概览页提到 SIP/TLS 能力但本书无启用路径，按 Features List 与产品安全文档答复
- 涉及 XMFaultTolerance 高可用部署 → 停，本书只介绍该组件不教部署，转产品文档/专业服务

输出契约：两侧 SIP 配置清单（OTFC 侧 5360/声明/Dial Plan + OXE 侧七步结果）+ 双向测试传真记录（或 trace 文件与初步分析）。

## B — 边界

- OXE 侧七步是菜单序列骨架，网关/中继具体参数（编码、号码变换、中继属性）原书未给，权威口径在 TC3048
- mtcl/mtcl 是 OXE 出厂默认账号，生产必须改；#31600-31699 与 GW1/GW2 号段均为实验口径示例
- SIP/TLS 在 p7 概览作为能力出现，配置章只有 UDP 5360，加密信令的证书与启用路径书内为零
- 高可用停留在虚拟化平台层（vMotion/HA）；XMFaultTolerance 只作组件介绍，failover 部署与演练全书未教
- 生态图中的 CSGD 缩写（p34）书内未定义；引用架构图时如实标注，不臆测含义
