# OmniVista 8770 节点接入（OXE 注册同步 + SSH 安全 + OXO Connect 纳管）

## R — 原文依据

> "Use the siteid command to display network and node number."（p119）
> "Subnetwork – Node number: Enter a numeric value equal to the OmniPCX Enterprise network*100 + OmniPCX Enterprise node number. Example: With a network number = 1 and node number = 2, you must enter 101"（p123）
> "Partial synchronization: Retrieve data changed since the last synchronization for the following entries: Users, Directory, Data terminals, Speed dial numbers, Remote users."（p114）
> "If the real-time synchronization doesn't work, perform the following actions: Restart NMC Alarm server service"（p128）
> "the OmniVista 8770 server converts it in a declaration node applying the following rule: (Subnetwork number X 100) + OXO Connect node number."（p658）

出处：8770XTE200EN p109-136（OXE）、p640-667（OXO Connect）。

## I — 自述

被管设备接入的钥匙是"号对号"，三条线：

**线一：OXE 节点注册（五段）**

1. 前置核查：SSH 到 Call Server 用 siteid 核对网络号/节点号；netadmin -m 选项 5（Role addressing）核对主用 IP；su - 提权后操作
2. 三级声明：Configuration 应用右键 nmc 建 Network（网络号为自由号）> 建 Subnetwork（子网号必须等于 OXE 网络号）> 建 OmniPCX 4400/Enterprise
3. 节点关键页：PCX 页（节点号=网络号×100+节点号、IP=OXE 主用地址、FTP 账号 adfexc、勾 Process configuration、告警接收模式 Permanent IP connectivity）；Software download 页填 mtcl 维护账号；Connectivity 页勾 SSH 并填唯一主机名
4. 同步：右键 OXE 选 Complete/Partial × Separate/Global 四种组合；Scheduler 窗口按 of the task > Status > Apply > Refresh 四步看日志
5. 实时核验与排障：OXE 侧建测试用户，Alarms 应用 Event 页应收到事件、Configuration 树 TelephonicDevices 出现该用户；失效时经 Service Manager 重启 NMC Alarm server（自动重启）后重测

**同步语义速查**

| 维度 | 取值 | 语义 |
|---|---|---|
| 范围 | Complete / Partial | 全量取回；或仅五类条目（Users/Directory/Data terminals/Speed dial/Remote users）按增量、其余全取 |
| 伴随 | Separate / Global | 只同步所选 OXE；连带关联 OpenTouch 一起同步 |

- 日志：同步 NMCSyncLdapPbx_1.log、事件 NMCFaultManager_1.log（C:\8770\log）
- OXE 侧改动经事件实时回传；但 profile、键 profile、空闲号码段必须主动同步才可见

**线二：OXE SSH 安全链路**

- 核查：netadmin -m 选项 2 确认 "Security with SSH: yes"；netstat 过滤 :22 应 LISTEN、:23 应无输出（telnet 关闭）
- 可信主机：netadmin -m > 11 Security > 1 Firewall > 3 Restricted Access > 1 View / 2 Add；加完回主菜单选 22 Apply modifications
- 8770 侧：Connectivity 页勾 SSH connection + 唯一主机名（字母开头）；树中右键 OXE > Connect 建 MindTerm 会话（首次接受许可、生成公钥存 MindTerm\hostkeys）；Plugins 可开 SFTP
- 代际：OXE N2 及以前默认 telnet 开/SSH 关；N3 起 SSH 默认开且可信主机管理强制

**线三：OXO Connect 纳管（五段）**

1. 布线与 IP 核查：Premium 话机 Menu > Operator > Expert > Netw.config > IP@CPU 核对 MAIN@ 地址
2. 装 OMC（8770 服务器与每个客户端都要装，首装需 .NET Framework）；Expert 会话经 Communication > Connect 输 CPU IP，装证书到受信任根，按提示改全部会话密码（OXO R10 起强制），首连必填客户信息
3. 声明：Configuration 应用建 OmniPCX Office 节点（节点号直接填 OXO 号，系统按 子网号×100+节点号 换算成声明节点）；FTP password 填 OXO 的 NMC 账号（取计费票用）；Connectivity 页填 Omc config password（installer 密码）
4. 共享目录与同步：Preferences > Configuration > OXO Preferences 配 Secure Shared Directory（填 8770 服务器 Windows 会话账号，供 \\nms\OXO-databases 备份访问）；右键 OXO Connect > Synchronization 完整同步并核对版本号
5. 运维会话：右键 Configure > Online mode 直连 OMC Expert；Offline mode 打开本地数据库副本离线编辑

- 备份目录按声明节点落盘：C:\8770_ARC\OXO\data\<网络>\<子网>\<声明节点>（如 1x100+80=180）

## A1 — 书中案例

**OXE 注册实验**（p118-128）：

1. siteid 核对节点号 1 / 网络号 1，netadmin 选项 5 核对主用地址（实验口径参数见 book/overview）
2. 建 Network（ale/1）与 Subnetwork（abc1/1，子网号=网络号）
3. 建 OmniPCX Enterprise 节点 101（1×100+1）、填主用 IP 与 adfexc 账号、勾 Process configuration 与 Permanent IP connectivity
4. 右键 Synchronization > Partial > Global，四步操作至成功消息
5. OXE 侧建用户 31234：Event 页收到事件、TelephonicDevices 出现 31234、日志记录创建消息

**OXE SSH 实验**（p129-136）：netstat 确认 22 监听 23 关闭；8770 内右键 Connect 建 MindTerm 会话；telnet 连接验证被拒。

**OXO Connect 纳管实验**（p640-667）：声明节点号 80 换算为 180；同步成功后 Configuration 显示 OXO 版本号；备份目录随之落 1\1\180。

## A2 — 未来触发

使用情境：新 OXE/OXO 上线接入；同步失败或实时不联动；OXE 升 N3 后 telnet 连不上；告警收不到但同步正常；OXO 备份目录找不到。

语言信号：节点注册 / siteid / 子网号 / 节点号 101 / Complete Partial / Separate Global / 实时同步 / NMC Alarm server / trusted hosts / MindTerm / OMC / OmniPCX Office / 声明节点 180 / OXO-databases。

与相邻能力区分：接入后建用户 → 用户开通能力；让告警上屏 → 告警管理能力；本能力到"同步成功 + 实时核验通过"为止。

## E — 可执行步骤

输入契约：OXE/OXO 侧维护账号（adfexc/mtcl/installer，现场应已自定义）、网络可达、8770 管理员会话。

1. 前置：siteid 与 netadmin -m 核对网络号/节点号/主用 IP。完成标准：三个值与规划表一致
2. 三级声明：Network > Subnetwork > PCX 逐级建。完成标准：节点号=网络号×100+节点号，IP 为主用地址
3. 填 Software download（mtcl）与 Connectivity（SSH + 主机名）。完成标准：账号密码与现场档案一致
4. 同步：右键 > Synchronization 选组合，Scheduler 窗口四步看日志。完成标准：成功消息 + OXE 下生成分支
5. 实时核验：OXE 侧建测试用户。完成标准：Event 页收事件 + 树中见用户
6. 排障（如失效）：Service Manager 重启 NMC Alarm server 后重测。完成标准：新事件恢复上送
7. SSH 链路：核查 22/23 状态、加可信主机并 Apply。完成标准：8770 内 SSH 会话可建、telnet 被拒
8. OXO 纳管：装 OMC > 首连改密 > 声明 OmniPCX Office > 配共享目录 > 完整同步。完成标准：版本号显示 + 备份目录按声明节点生成

判停点：

- 节点号与 siteid 对不上 → 先改声明值对齐 OXE 侧，不要反复同步
- #1125 类事件在 incident filter 下拉中找不到 → 先 Create 事件再设 Network incident（属告警卡边界，此处不硬调）
- OXO 共享目录参数填错 → 必须重启 8770 服务器才能再改，先确认凭据再动手

输出契约：已同步节点清单 + 同步/事件日志路径 + SSH 可信主机表 +（OXO）声明节点号与备份目录。

## B — 边界

- OXE 侧账号默认密码（mtcl/adfexc/SoftInst，N2 及以前）与实验口径 Superuser2580* 只作背景，N3 起必须已自定义；生产凭据按客户密码策略管理
- OXO 的配置本体在 OMC 完成，8770 只做纳管与代理；OMC 许可与 OXO 账号由客户侧自备
- 8770 与 OXE 的协议分工（配置 CMISE、数据提取 FTP/SSH、告警 CMISE/Corba）是排障前置认知，协议层报文排障在书外
- OXO 章存在未翻译法语残句（nr-02），按语义转述；声明节点换算与备份目录规则（p658）为全书一致口径
