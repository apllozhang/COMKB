# 双向节点声明与 SIP 打通（含告警对接）

## R — 原文依据

> "OpenTouch information can be found in the file bics.conf on the OpenTouch server: HOST_NAME="opentouch" ... ICE_USERNAME="otAdmin" ... ICE_TEMPLATEUSERNAME="otProfile" ICE_MAINTENANCEUSERNAME="otuser""（p194）
> "Node number is a free number. This node number must be different than OXE node numbers existing in the OXE network. (Use 99 for example)."（p196）
> "Port 2570 (OXE PRS port number) ... Codec Select the compression algorithm used for inter domain calls: This parameter must be the same as the one declared on the Call Server"（p199-201）
> "Gateway Number Enter the SIP external gateway number ("10" in our example) ... Port number 5260"（p231）
> "The SIP server of the Media Server (called "mule") has to be declared as an external SIP gateway. ... Port number 5040 ... Outbound calls only True"（p232）
> "The first time the MIB is downloaded from the OpenTouch to the OmniVista 8770 Server, it is not retrieved completely."（p209）

出处：OPENXTE300EN p186-234, p204-212。

## I — 自述

三台服务器靠"互挂"成网，顺序固定：先备 OXE，再在 8770 建 OXE 节点，然后在 8770 声明 OT 节点，最后在 OT 侧把 OXE 挂进自己的 Topology。四段要点：

- **OXE 前置**：netadmin -m 核对地址并建主角色名 csm；节点号=ABC 网络×100+节点号；开 47xx directory 4400 Synchro 实时同步；离开 netadmin 前必须选 20 APPLY MODIFICATION。
- **8770 建 OXE 节点**：Configuration 应用建 Network、Subnetwork、OmniPCX 4400 Enterprise 三级；FTP 凭证 adfexc；告警接收 Permanent IP connectivity。
- **8770 声明 OT 节点**：必须在 OXE 同子网；节点号用 99 等自由号且不得撞 OXE 节点号；凭证逐项取自 bics.conf（配置用 otAdmin、模板用 otProfile、维护用 otuser）。
- **OT 侧挂 OXE**：Topology 建同名网络与子网，OXE CS 对象填端口 2570（OXE PRS）、FTP adfexc、Codec 与呼叫服务器一致。

同步类型矩阵：

| 发起方 | 类型 | 行为 |
|---|---|---|
| OXE | Complete + Separate | 完整同步所选 OXE |
| OXE | Complete + Global | 完整同步 OXE + 关联 OT |
| OXE | Partial + Separate | 仅用户/目录/终端/缩位/远程用户增量 |
| OT | Complete 或 Partial | 对 OT 本身等价（均完整）；Global 时另同步关联 OXE |

OXE SIP 五段（承载层）：trunk group（T2/SIP）、本地网关与代理/注册器、两条外部网关（10 号到 OT SIP server 端口 5260；11 号到 Mule 语音邮件端口 5040，仅出话）、trusted addresses 加 OT 地址、全局压缩参数设 G729 并开 Routing Optimisation。

告警对接五段：

- OT 侧核 SNMP agent（161），建 SNMP server 对象（162、v3、SHA、AES 128、Inform、trap 过滤三档）并重启 ompd
- 8770 侧 OT 节点配 Alarm monitoring、V3 参数与 MIB 路径
- 首次 MIB 下载不全需重载：删 ICE 目录、重启 NMC Alarm Server、重启 ompd
- 停 lama 服务做告警闭环验证（产生 minor 告警，重启后自动恢复）

## A1 — 书中案例

**双向声明实验**（p186-203）：

1. OXE 侧 netadmin -m 核地址并建主角色名 csm。
2. 设 Node Number 与 Network Number，开 47xx directory 4400 Synchro。
3. 离开 netadmin 前选 20 APPLY MODIFICATION 提交改动。
4. 8770 Configuration 应用建 Network 与 Subnetwork。
5. 子网下建 OmniPCX 4400 Enterprise 节点并填主 IP 与 FTP 凭证。
6. 对 OXE 节点做 Complete + Separate 同步并查最近修改时间。
7. OT 上读 bics.conf 抄主机名、FQDN 与三账号。
8. 双向 nslookup 验 OT 与 OXE 的 FQDN 正反向解析。
9. 8770 在 OXE 同子网建 OpenTouch 节点（节点号 99、otAdmin）。
10. Connectivity 页填 otProfile，Maintenance 页填 otuser。
11. OT 配置工具 Topology 建网络与子网，再建 OXE CS 对象。
12. OXE CS 填端口 2570、Codec 与呼叫服务器一致后做 OT 节点同步。
13. 同步完成后 OXE 出现在 OT 的 Topology 分支下。

**SIP 与告警实验**（p204-234）：

1. 建 trunk group：ID 10、类型 T2、T2 Specification=SIP。
2. 配本地网关（端口 5060）与代理认证、注册器租期 600。
3. 建外部网关 10 指向 OT SIP server：端口 5260、TCP、类型 ICE type。
4. 建外部网关 11 指向 Mule：端口 5040、Outbound calls only=True。
5. Trusted addresses 加入 OT 服务器地址；压缩参数设 G729。
6. 告警：OT 建 SNMP server 对象（162、v3、Inform）并重启 ompd。
7. 8770 侧配 V3 用户与 MIB 路径；MIB 不全走三步重载。
8. 停 lama 服务产生 minor 告警，重启后自动恢复即闭环。

## A2 — 未来触发

使用情境：三件套互相看不见；同步后 OXE 不出现在 OT 拓扑；跨域呼叫单通或编解码异常；OT 告警进不了 8770；netadmin 改完参数"丢了"。

语言信号：bics.conf / otAdmin / otProfile / otuser / 节点声明 / declaration / Topology / PRS / 2570 / trunk group / 外部网关 / trusted / G729 / Mule / ESS / SNMP / Inform / MIB / 同步 / synchronization。

与相邻能力区分：号码段、前缀与拨号行为 → prior management 能力；向导账户口令遗忘 → 初始化向导能力；SIP 中继到运营商与本卡无关；OXE spatial redundancy 的字段差异全部外置 TC1652。

## E — 可执行步骤

输入契约：三台服务器管理权（OXE 的 netadmin/mgr、8770 的 nmc、OT 配置工具/WBM）；DNS 正反向解析就绪；OXE 节点号与网络号；编解码计划（默认 G729）。

1. 前置：DNS 双向解析全通、节点/网络号定案、bics.conf 三账号在手。完成标准：nslookup 全通
2. OXE 前置并 APPLY；8770 建网络、子网与 OXE 节点。完成标准：Complete+Separate 同步成功
3. 8770 声明 OT 节点（同子网、自由节点号、bics.conf 凭证）。完成标准：节点创建成功
4. OT 侧 Topology 挂 OXE（2570、Codec 一致）并同步。完成标准：OXE 入 OT 拓扑树
5. OXE SIP 五段配齐：trunk、本地网关、两条外部网关、trusted、全局压缩。完成标准：字段与设计一致
6. 告警五段走完并做停 lama 验证。完成标准：告警产生与自动恢复闭环

判停点：

- 声明失败或拓扑不显示 → 先查 DNS 反向解析（最高频根因）
- netadmin 修改"丢了" → 没选 20 APPLY，重做并提交
- 跨域呼叫编解码异常 → 两端 Codec 不一致；注意 ESS 不支持 G723
- 改了 SNMP 配置不生效 → OT 侧必须重启 ompd（含 ams）
- Alarms 树里没有 OT 图标 → 走 MIB 重载三步（删 ICE 目录、重启 NMC Alarm Server、重启 ompd）
- OXE 是 spatial redundancy → SIP 字段与语音邮件网关口径全变，转 TC1652，不照抄本卡

输出契约：互挂完成的三件套 + SIP 承载参数清单 + 告警闭环验证记录。

## B — 边界

- 实验口径（生产按现场设计替换）：OT 192.168.1.50、8770（nms）192.168.1.70、OXE csa/csm 192.168.1.1 与 192.168.1.3、trunk=10、外部网关 10/11、SIP DNS 192.168.1.254、SNMP 用户 AdminSNMP。
- OT 节点号示例 99 为自由号，不得与任何 OXE 节点号冲突；OT 必须与 OXE 同子网声明（p196）。
- DPNSS 前缀与 Routing Optimisation 属可选项，按现场中继计划定（p233-234）。
- SIP 部分要成套建完再呼叫（p226 Note）：trunk、网关、外部网关缺一项即不通。
- 告警口令至少 8 字符；8770 侧配置落盘 snmptrapd.conf（p208-209）。
- spatial redundancy 全面改口径（Belonging domain、Contact with IP address、外部语音邮件网关），完整操作在 TC1652（n17）。
