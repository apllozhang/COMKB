# QoS 与 ACL 策略（统一 policy 引擎、队列模型、auto-QoS、用户口安全）

## R — 原文依据

> "A policy (or a policy rule) is made up of: 1. a condition 2. an action"（p400）
> "By default, the port default values for 802.1p and ToS/DSCP are 0. ... By default, switched ports are untrusted"（p423）
> "the global setting is active immediately; however, modifying a port configuration requires qos apply to activate the change"（p424）
> "* By default, flows that do not match any policies are accepted on the switch"（p434）
> "This port group does not need to be used in a condition or rule to be effective on flows and only applies to routed traffic."（p453）

出处：DT00XTE215EN p391-453。

## I — 自述

QoS/ACL/PBR/策略镜像共用同一个 policy 引擎：condition（L1-L4 条件）+ action（accept/drop/deny、优先级、标记、限速、PBR 网关、镜像、port-disable）+ rule（precedence/validity-period/log/count），qos apply 才下发硬件（p400-407）。

1. **队列模型**：每端口 8 个队列（QSI）；队列集档案 QSP 定义调度——QSP 1=8×严格优先级、QSP 2=1×EF+7×SP 等；可按端口改 QSI 的 QSP 或改系统默认（p397-398）
2. **默认口径五条**（p396/404/423/424/434）：QoS 默认启用；不匹配任何策略的流默认接受；端口默认 802.1p 与 ToS/DSCP 为 0；交换端口默认不信任；全局设置立即生效、端口与策略改动必须 qos apply
3. **auto-QoS**（p410）：qos phones 按四个 ALE 话机 MAC 段识别流量自动给优先级 5，信任与非信任端口都生效，默认启用
4. **ACL**：disposition 为 drop/deny 的 policy；条件按 L2/L3/L4/组播分箱；兜底规则惯例用 precedence 65535 放最后
5. **保留安全组**：UserPorts 端口组反 IP 欺骗（源 IP 与端口子网不符即丢，仅作用路由流量，无需被条件引用）
6. **用户口协议防护**：qos user-port filter/shutdown 处理协议清单（spoof/bgp/bpdu/rip/ospf/vrrp/pim 等）；DropServices 服务组丢弃指定 TCP/UDP 服务
7. **port-disable 规则**：命中即管理性关闭端口，配 violation-recovery-time 自动恢复与 recovery-trap

**auto-QoS 话机 MAC 段**（p410）：

| MAC 段（前 3 字节） | 设备 |
|---|---|
| 00:80:9F | Enterprise IP Phones |
| 78:81:02 | Communications IP Phones |
| 00:13:FA | Lifesize IP Phones |
| 48-7A-55 | ALE 8008 IP Phone |

## A1 — 书中案例

**QoS 实验**（p421-428）：

1. 清场：qos flush、qos apply、show qos config 核对默认（Trust=no、Phones=trusted）
2. 端口默认标记：qos port 1/1/1 default 802.1p 7，理解不信任口对 tagged 流量也改写
3. 信任口：qos port 1/1/1 trusted 后 apply，Trust 列变 Yes
4. 标记策略：policy condition source vlan 20 + action 802.1p 5 + rule，qos apply 后 show active policy rule 才出现
5. 限速验证：action 加 maximum bandwidth 100k，大包 ping 触发 Tri-Color 的 Red 计数（实验值 148，实验口径）
6. 调试技巧：规则开 log 后 show qos log 查看

**ACL 实验**（p447-453）：

1. 取客户端 MAC：show mac-learning port 记录 Client 5/9 地址
2. L2 过滤：condition source mac + action disposition deny，apply 后 ping 断；flush/reset 恢复默认放行
3. FTP 过滤：condition source vlan 20 destination ip-port 20-21 ip-protocol 6，rule 用 precedence 65535 兜底
4. HTTP 过滤：建 5 个 policy service（80/8080/8000/443/4343）+ service group，对 VLAN 30 整组 deny
5. 用户口安全：policy port group Userports 划口防 IP 欺骗；qos user-port shutdown bpdu 防私接交换机成环

## A2 — 未来触发

使用情境：语音流量优先级保障；按部门限速；禁某网段 FTP/HTTP；防 IP 欺骗；用户口收到 BPDU 就关；策略配了没生效；标记被改写排查。

语言信号：QoS / policy / condition / action / rule / precedence / qos apply / 802.1p / DSCP / 限速 / Tri-Color / auto-QoS / qos phones / ACL / UserPorts / DropServices / BPDU shutdown。

与相邻能力区分：

- 认证成功后按用户下发策略：Access Guardian 能力卡（UNP policy list，非全局策略）
- 话机拿到语音 VLAN 与 LLDP 标记：LLDP 与 PoE 能力卡
- 网关侧过滤与路由：三层服务能力卡

## E — 可执行步骤

输入契约：流量矩阵（谁到谁、什么协议/端口）、优先级与带宽目标、端口角色（用户口/上联口/话机口）、实验或生产口径。默认拒绝语义需明确设计。

1. 清场基线：qos flush + qos apply + show qos config 确认默认（尤其复用环境）。完成标准：无残留 pending 规则
2. 端口队列与信任：接终端口保持不信任；接上游/话机口 trusted；需要时调 QSP。完成标准：信任边界与设计一致
3. 写策略三件套：condition（按层选关键字）+ action（标记/限速/deny）+ rule（precedence，兜底 65535）。完成标准：show policy 三查齐全
4. 下发验证：qos apply 后 show active policy rule 确认命中计数增长；"配了没效果"先查是否 apply。完成标准：规则激活且有计数
5. 限速与标记验证：大包 ping 触发 Red 计数；抓优先级位验证标记。完成标准：行为与目标一致
6. 用户口安全（按需）：UserPorts 划口、qos user-port shutdown bpdu、DropServices 按需。完成标准：欺骗与环路防护生效
7. 固化与收尾：write memory；实验场景 flush/reset 恢复默认，不留全局 deny 规则。完成标准：状态可交接

判停点：

- 策略规则看不到效果 → 先查 qos apply 与 show active policy rule，再查条件方向（source/destination）
- 需要"默认拒绝" → 默认语义是接受，须自行设计 accept 白名单+兜底 deny，评估漏配影响后再上
- 用户口被 shutdown 后恢复 → 需人工恢复或配 violation-recovery-time；排障先问有没有私接小交换机
- UserPorts 想拦二层桥接流量 → 只作用路由流量（p453），二层防护改用 BPDU shutdown 等手段
- 规则要开 count → 仅 6860(E)/6865/6900-X72 支持（p407），其他型号判停换验证手段

输出契约：生效的 QoS/ACL 策略清单（apply 后计数佐证）+ 信任边界与用户口安全配置 + 收尾状态说明。

## B — 边界

- 不信任口把 tagged 流量的 802.1p 也改写为端口默认值（原始标记丢失）；接上游口要 trusted（p423）
- 默认 accept 语义：写一条 deny 只拦命中项，其余照通——"配了 ACL 就安全了"是错觉（p434）
- 条件组合全表在 Network Configuration Guide（p422 指针），本卡只覆盖教材出现的条件
- PBR（permanent gateway）与策略镜像复用同引擎，细节按需查 Network Configuration Guide
- 实验 QoS 数值（802.1p 7、100k 限速、Red 148）为实验口径，生产按业务目标定
- qos reset（回默认）/revert（删 pending）/flush（清配置）三者语义不同，清场前分清（p422/p449）
