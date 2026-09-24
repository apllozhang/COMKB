# OXE/OTMC 双向声明进 8770 与同步（bics.conf 对账、节点编号、同步矩阵）

## R — 原文依据

> "Subnetwork – Node number: Enter a numeric value equal to the ABC network*100 + OmniPCX Enterprise node number."（p87）
> "OTMC server must be declared in the same sub-network than the OXE call server."（p94）
> "Partial and complete synchronization are identical for OTMC node."（p100）
> "OTMC information can be found in the file bics.conf on the OTMC server"（p92）

出处：OTMCXTE200EN p83-101（c03/c04、f12/f13、p08、n09/n17 归并）。

## I — 自述

纳管闭环四段：

1. **OXE 侧准备**：netadmin -m 核 IP 与角色地址、配节点名（改完必须 20.'APPLY MODIFICATION'，否则丢弃）、核节点/网络号（siteid 或提示符括号）、开目录实时同步（47xx directory – 4400 Synchro = True，8770 目录自动增改的前提）
2. **8770 声明 OXE**：三层树 Network（自由编号）→ Subnetwork（编号必须等于 OXE 的 ABC 网络号）→ Node；OXE 节点号 = ABC×100 + 节点号
3. **声明 OTMC**：bics.conf（/var/data/bics/bics.conf）是站点账本——HOST_NAME/HOST_DOMAIN + ICE 三账户（otAdmin=8770 配置、otProfile=模板管理、otuser=维护/SSH），声明时逐项对账；OTMC 节点号自由但不得与任何 OXE 节点号重复，且必须与 OXE 呼叫服务器同子网
4. **OTMC 拓扑对称声明 OXE**：System services/Topology/OXE CS 下建 network/subnetwork/OXE CS（名称编号沿用 8770 侧定义；Port 2570、SIP Port 5060、FTP adfexc）

同步矩阵：

| 发起节点 | 类型+目标 | 效果 |
|---|---|---|
| OXE | Partial + Separate | 仅该 OXE 增量（用户/目录/数据终端/缩位拨号/远端用户） |
| OXE | Partial + Global | OXE 增量 + OpenTouch 全量 |
| OXE | Complete + Separate | OXE 全量 |
| OTMC | Partial 或 Complete + Separate | OTMC 全量（对 OTMC 节点两者等价） |
| OTMC | 任意 + Global | OTMC 全量 + 连带全量同步关联 OXE |

## A1 — 书中案例

**双向声明与同步实验**（c03+c04，网段/口令等环境值见 book/overview）：

1. OXE 侧核 IP：netadmin -m 进 Local Ethernet interface 核对（实验口径见 book/overview）
2. 配角色地址：netadmin -m 的 Role addressing 下 Add main 角色
3. 配节点名：Node Setup 下 Update；离开菜单前必须执行 20.'APPLY MODIFICATION'
4. 核节点/网络号：siteid 或命令行提示符括号确认 OXE 为目标节点号（ABC×100+节点号，实验为 101）
5. 开实时同步：47xx directory – 4400 Synchro 置 True
6. 8770 建网络与子网：Configuration 应用右键 Create；子网号等于 OXE 的 ABC 网络号
7. 8770 声明 OXE：Subnetwork-Node number=101、IP=main 地址、FTP adfexc、勾 Process configuration 与 Process directory
8. 同步 OXE：右键 Synchronization，Complete+Separate，刷新任务日志至无错、OXE 分支生成
9. OTMC 对账：more /var/data/bics/bics.conf 记下主机名/域与 ICE 三账户；DNS 正反双向 nslookup 核验（示例网段漂移见 nr-02）
10. 8770 声明 OTMC：Create 选 OTMC；OT 页签填自由节点号（实验用 98、模板例 99，见 nr-01）、FQDN、otAdmin 凭据；Connectivity 页签填 otProfile；Maintenance 页签填 otuser
11. OTMC 拓扑声明 OXE：Topology/OXE CS 下建 network/subnetwork/OXE CS（Port 2570、SIP Port 5060、FTP adfexc、Node Identifier 与 8770 侧一致）
12. 同步 OTMC：右键 Synchronization 目标 Global；确认 OXE 节点挂到 OTMC 的 Topology 分支下

## A2 — 未来触发

使用情境：新站点纳管；声明后同步报错；OXE 改动"没生效"；OTMC 账户密码丢失；同步只想要增量还是全量；OXE 节点没出现在 OTMC 拓扑下。

语言信号：声明 / declaration / 8770 / Nmc / 节点号 / node number / bics.conf / otAdmin / otProfile / otuser / 同步 / synchronization / Complete / Partial / Global / Separate / 4400 Synchro / APPLY MODIFICATION。

与相邻能力区分：前置的站点配置 → otmsg-install-site-setup；后续的话路对接 → otmsg-sip-trunk-provisioning；OXE 侧基础命令属 OXE 课程（本书直接使用）。

## E — 可执行步骤

输入契约：OXE 可管理（netadmin/mgr）、8770 已装可达、DNS 正反解析就绪、post-install 完成且 bics.conf 可读。账户密码丢失先走重置（见 B 与判停）。

1. 准备 OXE：IP/角色地址/节点名/节点号四项设置并 APPLY；开 4400 Synchro。完成标准：siteid 显示目标节点号
2. 声明 OXE 进 8770：三层树建节点（编号=ABC×100+节点号）并同步。完成标准：同步日志无错、OXE 分支生成
3. 对账 bics.conf：主机名/域/ICE 三账户逐项核对；DNS 正反 nslookup 双向核验。完成标准：声明参数与账本一致
4. 声明 OTMC 进 8770：节点号自由但唯一、与 OXE 呼叫服务器同子网、填三账户。完成标准：OTMC 节点创建成功
5. OTMC 拓扑声明 OXE：network/subnetwork/OXE CS 逐层建（2570/5060/adfexc）。完成标准：拓扑层与 8770 侧定义一致
6. 双向同步验收：OTMC 发起 Global 同步。完成标准：OXE 出现在 OTMC Topology 分支下

判停点：

- bics.conf 与声明参数对不上 → 停，回 post-install 记录核对，不硬猜账户（p92）
- OXE 改动没生效 → 先查 netadmin 是否漏了 20.'APPLY MODIFICATION'（n09），再查别处
- 同步后 OXE 不在 OTMC 拓扑下 → 查 DNS 正反解析、节点号唯一性、同子网约束
- 密码丢失：otAdmin/otProfile 走 WBM 重置，otuser 走 root 执行 /usr/bin/musett.sh（p93-94）

输出契约：8770 中 OXE/OTMC 双节点就位、拓扑互挂、同步基线完成 + bics.conf 对账记录。

## B — 边界

- OTMC 节点号示例双口径：p94 实施写 98、p95 模板举例 99（规则一致：自由号、不撞 OXE 节点号）——引用注明 nr-01
- 声明章示例网段 155.1.1.x 与拓扑章 151.1.1.x 并存、p94 反查 .50 返回 .60、p84 掩码 /16 与 /24 不符——示例仅示意（nr-02/nr-03）
- OXE 节点可由 WBM 首登自动创建（p96）；未用 WBM 时才手工声明
- OXE 基础命令（netadmin/mgr/siteid/ednump）属 OXE 课程内容，本书直接使用不解释
- 实验网段、otAdmin/otuser 口令、csa/csm 地址等环境值集中见 book/overview
