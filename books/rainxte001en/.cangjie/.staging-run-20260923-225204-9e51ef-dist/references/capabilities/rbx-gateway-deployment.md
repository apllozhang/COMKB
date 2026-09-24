# WebRTC 网关部署与虚拟终端配置（三拓扑施工、自动配置、Twinset/Anydevice）

## R — 原文依据

> "The automatic configuration of the internal / external WebRTC gateway is available from system version R4.0.020.002"（p121）
> "The following settings are still to be done by the installer ... • Connect PBX to Rainbow • Creation and association of the AnyDevice/Rainbow virtual terminals • Configuration of numbering plans and of the barring"（p121）
> "Rainbow PBXID must be the same in both OXO Connect, Front-End and call server ... Verify port numbers to 5059 in the SIP Gateway parameters"（p134）
> "OMC / Cloud / Rainbow — WebRTC Gateway is Connected and Enabled"（p154）
> "Deskphone + Free Rainbow virtual terminal = 1 UTL • Anydevice only = 1 UTL"（p156）

出处：RAINXTE001EN p121-122, p124-161。

## I — 自述

**通用前提**：PBX 已接入 Rainbow；用户持 Business/Enterprise 且账号已关联话机（p120/p142）。传输安全：网关到 Rainbow 全程 HTTPS + SRTP（p126）。

**自动配置边界**（R4.0.020.002+，发起人必须是 Reseller 管理员）：
- 自动建（内部）：网关激活（仅 OCE）、WebRTC SIP 网关、SIP 账号（用 PBXID）、VoIP 接入与中继组、ARS 路由表
- 自动建（外部）：SIP 网关/SIP 账号/中继组/ARS 四项（无激活项）
- 安装员保留：连 PBX、终端创建与关联、编号计划与闭锁；外部拓扑另加 VM/PC 安装与网关激活

**三拓扑施工要点**：
- OCE 集成：Rainbow 管理端激活即可，OXO 侧自动配置
- OCE Front End：FTR（ETH1 DHCP → 浏览器 192.168.94.246 → 设密码 → 产品类型 Frontend WebRTC）→ warm reset 生效 → Rainbow 侧选 "External on OCE Front End"（≤20 通道）→ OMC 核验私有 SIP 网关端口 5059 → 双机 PBXID 必须一致（FTR 占位 FleetRef-Installref 要替换）
- 外部 VM/NUC：MyPortal 下 OVF/ISO → ESXi 部署或 RUFUS 做 U 盘装 NUC → 配网络四参数 + OXO 地址 + PBXID + TURN（按站点位置）→ Rainbow 侧激活为外部网关

**虚拟终端两形态**（OMC/Subscribers list）：
- 有话机：建 Free Rainbow in Twinset 虚拟终端 → 挂为主分机副站（Multiset）
- 纯软话机：建 Anydevice 终端 → Rainbow 侧 Members → Telephony 页签绑定该号

## A1 — 书中案例

**内部网关自动配置实验**（p149-154）：Reseller 管理员登录 → Client Company/Communication → Manage connection → Information 页签勾 Activate WebRTC Gateway → Settings 页签选 Internal 设通道数 → OMC/Cloud/Rainbow 核验显示 Connected and Enabled。

**虚拟终端实验**（p155-161）：admin 建 Twinset 副站 130 挂主分机 100 副站（实验口径），user1 建 131；user2 建 Anydevice 132 并在 Rainbow 端绑定 → 配完验证路由切换测试清单（电脑↔电脑/话机↔电脑/三方会议/屏幕共享/视频）。

**OCE-FE 部署序列**（p128-135，讲义级）：FTR 全流程 + warm reset + Rainbow 激活 + OMC 双机核验，生产细节指向 cookbook。

## A2 — 未来触发

使用情境：部署网关；激活 WebRTC Gateway 按钮找不到；自动配置后建终端；FE 装完配置不生效；双机 PBXID；端口 5059；建 Twinset/Anydevice；核算 UTL。

语言信号：部署网关 / Activate WebRTC Gateway / 自动配置 / auto configuration / Reseller 管理员 / FTR / Frontend WebRTC / warm reset / FleetRef / 5059 / Twinset / Anydevice / secondary set / UTL / Subscribers list。

与相邻能力区分：选型与容量 → 网关规划能力；接入 Rainbow 本身 → PBX 接入能力；用户侧路由使用问题先确认终端已建。

## E — 可执行步骤

输入契约：拓扑结论（规划卡输出）、Reseller 管理员账号、PBXID/激活码、OMC 可用。无 Reseller 账号 → 判停（激活无法执行）。

1. 激活网关（Reseller）：Communication → Manage connection → 勾 Activate WebRTC Gateway → 选类型（Internal / External / External on OCE Front End）与通道数。完成标准：Settings 显示 enabled
2. 拓扑专项施工：
   - 集成：跳过（步骤 1 即完成 OXO 侧配置）
   - FE：FTR 建设备 → warm reset → 核对双机 PBXID 一致（替换占位符）→ OMC 核验端口 5059
   - 外部：装 VM/NUC → 配网络与 PBXID/TURN → 核对自动建项落地
3. OMC 核验：Cloud/Rainbow 显示 Connected and Enabled。完成标准：状态达标
4. 建虚拟终端：OMC/Subscribers list 按形态建 Twinset/Anydevice → Twinset 挂副站 / Anydevice 在 Rainbow 端绑定。完成标准：每个话音用户有终端且占 1 UTL
5. 行为验证：用户切路由（computer/office phone/other）→ 覆盖电脑↔话机互打、三方、共享、视频。完成标准：测试清单全通过

判停点：
- 客户管理员找不到激活入口 → 权限设计如此（仅 Reseller），转经销商操作，不要找绕路
- FE 修改后"没变化" → 先确认做过 warm reset，再往 Rainbow 侧查（p132）
- FTR 后设备连不上正式租户 → 查占位符 FleetRef-Installref 是否已替换、双机 PBXID 是否一致
- 自动配置完成但打不出电话 → 编号计划与闭锁是安装员保留项（原书不教），转 TC2479 + 客户拨号规范
- R4.0.020.002 恰好等界站点 → 两处原文口径不一（nr-01），保守按"需更高版本"处理或先升级

输出契约：Connected and Enabled 的网关 + 终端配置清单（形态/号码/UTL）+ 行为测试记录。

## B — 边界

- TURN 取值、防火墙白名单、VM/NUC 详细安装步骤：书外（安装指南，p140/p144 指针）——漏配白名单是外置网关不通的高频原因
- OCE-FE 多场景开局（新装/加装/版本低于 R4）：必须按 MyPortal 最新版 cookbook，不凭本卡记忆操作（p137）
- 编号计划与闭锁全书未教（n21）：本卡明确以此判停转出
- 实验号码 130-135 为 RLAB 口径；生产编号按客户拨号规范
- FE 无 PBX 能力：不得当备用 PBX 用（p129）
