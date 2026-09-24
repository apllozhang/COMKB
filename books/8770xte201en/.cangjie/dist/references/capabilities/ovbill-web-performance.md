# Web Performance 实时仪表盘（SNMPv3 双侧配置、CDR 采集、widget 与轮询调优）

## R — 原文依据

> "CDR stands for Call Detail Record: set of data emitted at the end of a call by the Call Server for billing purposes • Proprietary format for IP devices, IPMG, 4645 and IP-xBS… RTCP-XR format for SIP devices"（p492）
> "Automatic retrieval via a fixed 30 minutes polling timer (R5.0 GA) and a manageable one with 5 minutes minimum (R5.0 MD1)"（p492）
> "A maximum of 6 elements can be selected — For trunks, disk, IP domains and entities"（p503）
> "In case of misconfiguration the 8770 raise an alarm and disable the SNMP monitoring."（p511）

出处：8770XTE201EN p489-517。

## I — 自述

Web Performance 是 WBM 侧的实时性能仪表盘，两条数据腿：

- VoIP CDR（话终话单）：IP 设备用 ALE 专有格式、SIP 设备用 RTCP-XR 格式；经同步与小时轮询经 SSH/FTP 取回，可按类型/时间/IP 过滤
- OXE SNMP MIB：SNMPv3（authPriv，SHA 认证+AES 加密）轮询两棵 MIB——专有 A4400-RTM-MIB（中继监督/压缩器/CAC/SIP 注册）+ 标准 UC-DAVIS（CPU/磁盘平台健康）
- 轮询口径：R5.0 GA 固定 30 分钟；R5.0 MD1 起可管理、最低 5 分钟（经 ToolsOmniVista 的 SNMP 菜单）；数据 widget 刷新默认 30 分钟、可缩至 5 分钟
- 仪表盘五大主题：IP domains（压缩器/会议电路/CAC）、OXE health（CPU/IO/磁盘）、VoIP quality（MOS/超限票/记录分布）、Trunk groups（状态/累计 OOS 与超限）、Devices（NOE 设备出入服/SIP 注册）
- 两类仪表盘：节点仪表盘（过去 24 小时、固定 5 widget）与详细仪表盘（一天到一年、可增删预定义 widget、加阈值线）；原始数据（逐轮询粒度）只在周期=最后一天时可见；widget 单参数最多选 6 个元素
- 一致性自检：8770 周期校验双侧 SNMP 配置（协议/community/V3 用户）与代理状态，发现不一致时不做重试，直接出告警并停用 SNMP 监控，须人工重新启用
- 数据源限制：Hybrid link、直连链路、远端中继组不支持；承载仅 ISDN（T0/T1/T2）、SIP、NDDI、ABC-F

## A1 — 书中案例

**SNMPv3 双侧配置与验证**（p509-517，实验口径）：

1. OXE 配置 SNMP Configuration > 1 > SNMP Global Configuration：版本选 V3，先 Disable 再配置后 Enable
2. Agent SNMPv3 Users 建 agentV3：口令 superuser、加密短语 pwdagentV3
3. OXE SSH 会话用 snmpget 验证：snmpget -v 3 -l authPriv -u agentV3 -a SHA -A superuser -x AES -X pwdagentV3 -E 8000027D046F786531 localhost .1.3.6.1.4.1.637.64.4400.1.7.0，返回在服话机数=5
4. 8770 节点 Connectivity 页签：SNMP port 161、security level v3、V3 user agentV3、认证 SHA/superuser、加密 AES128/pwdagentV3
5. PCX 页签勾 SNMP performance monitoring
6. WBM 登录（https://服务器:8443 选 NETWORK MANAGEMENT）打开 Performance 仪表盘查看五大主题 widget
7. 调优：R5.0 MD1 起经 ToolsOmniVista 把 SNMP 轮询从 30 分钟缩到 5 分钟；widget 内按需选元素（≤6）与阈值线

## A2 — 未来触发

使用情境：给管理层搭实时大屏；OXE 健康与中继状态可视化；SNMP 仪表盘没数据；改了 OXE 的 V3 口令后仪表盘断粮；轮询能不能更快；widget 想看更多元素。

语言信号：Web Performance / WBM / 仪表盘 / dashboard / widget / SNMPv3 / agentV3 / SHA / AES / A4400-RTM-MIB / UC-DAVIS / CDR / RTCP-XR / 轮询 / polling / 30 分钟 / 5 分钟 / 原始数据 / raw data / MOS。

与相邻能力区分：厚客户端 VoIP 报表面 → VoIP 性能能力；Tracking 告警 → 流量与 Tracking 能力；本卡只管实时采集与可视化。

## E — 可执行步骤

输入契约：OXE 与 8770 IP 连通；WBM 可访问；SNMP 凭证已与客户约定治理口径。凭证无治理约定 → 判停先约定归属与轮换，再落配置。

1. OXE 侧建 SNMPv3 用户（版本 V3、先 Disable 配置再 Enable）。完成标准：用户与口令落盘
2. OXE 侧 snmpget 验证 OID 可读。完成标准：返回值合理（如在服话机数）
3. 8770 节点 Connectivity 页签按同口径配 v3（端口/用户/认证/加密）并勾性能监控。完成标准：双侧参数逐项一致
4. WBM 登录 Performance 查看五大主题 widget。完成标准：数据非空
5. 需要更快刷新时（R5.0 MD1+）经 ToolsOmniVista 调轮询至最低 5 分钟。完成标准：widget 刷新周期符合预期
6. 详细仪表盘按需增删 widget、加阈值线、选元素（≤6）。完成标准：版面可读

判停点：

- 仪表盘整体断粮且有告警 → 双侧 SNMP 配置不一致触发了"停用监控"，两侧改完后人工重新启用，不当故障反复重启
- OXE 侧改了 V3 口令 → 把 8770 侧同改当成同一次变更窗口的两步做
- 中继类型不在支持列表（非 ISDN/SIP/NDDI/ABC-F、Hybrid/直连/远端中继组）→ widget 无数据是设计边界，售前按中继类型核对
- 想看更早的逐轮询数据 → 原始数据仅限"最后一天"周期，更早只有聚合值

输出契约：双侧 SNMP 参数对照表 + snmpget 验证记录 + 仪表盘配置（主题/widget/轮询周期）。

## B — 边界

- 全部 SNMP 口令（agentV3/superuser/pwdagentV3）与 WBM 账号为实验口径；生产凭证治理（持有/轮换/留痕）在书外（n45/n38）
- OID 业务含义须查 ALE 技术文档（p512 Notes 明示）；本卡不解读未列出的 OID
- 版本分界 R5.0 GA / R5.0 MD1 决定轮询可调性；升级前按 8770 版本核对
- 仪表盘覆盖 ISDN（T0/T1/T2）、SIP、NDDI、ABC-F 中继；Hybrid link/直连/远端中继组不支持（p493）
- CDR 与计费票据同源不同消费面：本卡消费话终质量数据；话费计算属资费建模能力
