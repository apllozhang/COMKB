# DIGEST — OpenTouch Message Center Starter 精华长文

> 源：OTMCXTE200EN Issue 08（259 页，OTMC R2.6 / 2.6.1 时代）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OTMC 交付全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

OpenTouch Message Center（OTMC）是 ALE 的**OXE 专用外挂语音邮件服务器**：单台服务器独立部署（SUSE Linux Enterprise 底座），专门服务 OmniPCX Enterprise 的 Connection 用户，取代 46xx/8440 旧方案。消息存 OTMC 本地（Local Storage）或统一消息后端（UM）。

访问通道三条——任意话机按 TUI、8xx8/8088 话机信封键直达可视化信箱（GUI）、任意 IMAP 邮件客户端。配置管理只有一个大脑：**OmniVista 8770**（OTMC 是其中的新节点类型）；OTMC 自己的网页管理只做辅助（改密码、问候语管理、IMAP 前端参数）。

三个数字先记住：

| 数字 | 含义 |
|---|---|
| 15000 users | 三个 SUSE 安装模式的标注口径（生产规格看 product limits） |
| 5000 用户 | 话机 GUI（可视化信箱）并发显示上限，经 PRS 链路，限 8 系/80x8/8088 |
| 5040/TCP | OXE 侧把 OTMC 声明为 SIP external gateway 的端口——配错即无信箱业务 |

## 二、交付主线（顺序不可颠倒）

1. **装机**：三张 DVD（或 SUSE 单刻 + USB 硬盘装其余 ISO）；虚机按 MyPortal 安装手册 6.2 章建（实验口径 4 核/4GB/E1000/250GB 精简置备）；BIOS 关超线程、ESXi 电源 High performance；SUSE 三种安装模式——硬件 GUI 版、**虚拟化基础设施版**（虚机选这个）、OTMC first（单分区、放弃平滑升级）。
2. **core 安装**：CheckSystemLinux.sh 查前置 → setup.bin 部署约 30 分钟 → 重启自动进 post-installation wizard。
3. **13 步向导**（站点配置唯一入口）：类型/主机/网络/HA/五账户/许可服务器/许可文件/证书/备份存储/摘要/更新。硬规则如下：

   - 主机名小写；DNS 前向+反向解析七类 FQDN（OTMC、8770、邮件、LDAP、OXE 呼叫服务器按冗余模式、H.323 网关）
   - 账户密码 ≥8 字符且**界面不报错**；虚拟环境备份必须外置 NFS
   - 课堂"网络安全 OFF"生产禁止照搬；全部设置落盘 bics.conf

4. **双向声明与同步**，顺序五步：

   - OXE 侧 netadmin 备好（改完必须 APPLY MODIFICATION、开 4400 实时同步）
   - 8770 三层树声明 OXE（节点号 = ABC 网络号×100 + OXE 节点号）
   - 对账 bics.conf（otAdmin/otProfile/otuser 三账户）声明 OTMC（节点号自由、不撞 OXE、与呼叫服务器同子网）
   - OTMC 拓扑对称声明 OXE（端口 2570/5060、FTP adfexc）
   - 按同步矩阵选对组合执行（见下表）
5. **SIP 对接**：trunk group（T2/ABC-F/SIP）；OTMC 声明为 external gateway（5040/TCP/ICE type）；trusted 地址加 OTMC IP；全局 G.729 + DPNSS 前缀 + Routing Optimisation=Yes。
6. **业务交付**：OXE 建 Connection 用户（寻址三法：resurrection 拨分机+0000、空闲地址表、IP 话机静态注册）；核话机许可三族六类；OTMC 建账户（分机号对齐）；建信箱（**必须挂 profile 才能保存**）；挂信箱、开 Voice mail 权。
7. **增值与运维**：通知（外部 SMTP，无认证无 TLS，经 VPIM 路由）、IMAP 客户端（默认 IMAPS+TLS）、企业广播（单条/覆盖/≤5 分钟）、备份恢复（8770 发起，恢复后**手工**起服务）、语音信箱统计。

## 三、关键表

**话机许可三族六类**（OXE 侧，核查走 spadmin 左=已用/右=可用）：

| 族 | License | 名称 | 话机 |
|---|---|---|---|
| TDM | 174 | Analog users | Z 设备模拟话机 |
| TDM | 173 | Advanced reflexes users | 8029/8039 |
| TDM | 316 | Connection reflexes users | 4019 |
| IP | 176 | Advanced IP users | 8028/8038/8068 |
| IP | 317 | Connection IP users | 4008/4018 |
| SIP | 177 | SIP users | SEPLOS/SIP 设备 |

**同步矩阵**（选型速查）：

| 发起节点 | 类型+目标 | 效果 |
|---|---|---|
| OXE | Partial + Separate | 仅 OXE 增量 |
| OXE | Partial + Global | OXE 增量 + OpenTouch 全量 |
| OTMC | 任意类型 | Partial 与 Complete 等价（全量） |
| OTMC | + Global | OTMC 全量并连带全量同步关联 OXE |

**通知功能可用性**（LS = Local Storage / UM = 统一消息）：

| 功能 | LS | UM |
|---|---|---|
| 邮件/短信通知 | 有 | 有 |
| wav 附件 | 有 | 无 |
| My Messaging 链接 | 有 | 无 |
| 回呼留言主 | 有 | 无 |
| 满箱/近满提醒 | 有 | 无 |

**端口与时长速记**：

| 口径 | 数值 |
|---|---|
| OTMC external gateway | 5040/TCP（ICE type） |
| OXE SIP / PRS 端口 | 5060 / 2570 |
| SUSE 安装 / core 部署 | 约 25 分钟 / 约 30 分钟 |
| 恢复后服务重启 | <5 分钟（手工 service opentouchd start） |
| 近满告警阈值 | 默认 80%（原文 by default 80%） |

## 四、高频坑位（现场返工排行）

1. **许可假 OK**：向导显示 OK 只代表文件在本地，有效性不校验——必须 ./lmutil lmstat –a 复核；拷入新 .ice 后不重启 flexlmd 等于白拷。
2. **DNS 漏解析**：七类 FQDN 少一条正反解析，声明/通知/对接到处报错。
3. **信箱保存报错**：Configuration 页签没挂 profile（强制前置）。
4. **"有信箱不能留言"**：用户 Licenses 页签 Voice mail 权没开。
5. **恢复完服务没起**：设计行为——起服务必须管理员手工做，别提前判失败；恢复测试删用户只能走 OT Configuration 窗口（从 Users 应用删会连带删 OXE 虚拟 SIP 设备）。
6. **通知静默失败**：SMTP 送达失败基本无告警——先查发件账户退信；UM 用户没有附件/满箱提醒（LS 专属），界面照样显示但配了无效。
7. **升级后通知文案没变**：模板保护机制，删旧模板 + 重启 chameleon 才拿新版。
8. **统计文件不生成**：输出目录要手工建并注意读写权限，改完必须重启 mascd。

## 五、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 装 OTMC/跑向导/配 DNS 账户 | otmsg-install-site-setup |
| 装许可/换许可/lmstat 核验 | otmsg-license-management |
| 声明节点/同步/密码重置 | otmsg-declaration-sync |
| SIP 对接/通道排障 | otmsg-sip-trunk-provisioning |
| 建用户/开信箱/许可核查 | otmsg-user-mailbox-provisioning |
| profile 批控/问候语 | otmsg-mailbox-profiles |
| 邮件/短信通知 | otmsg-notification-smtp-sms |
| 备份恢复/用量统计 | otmsg-backup-statistics |
| 产品选型/形态/上限口径 | 路由入口（ot-message-center-router） |
| 自助门户/IMAP/企业广播 | 路由入口（ot-message-center-router） |

## 六、交付红线

1. 教材全部密码/账号/网段是实验值（letacla1/OtmcV01*/letacla1234/Admin-8770、151.1.1.x 等），上生产必须换并做加固；话机默认密码 0000 是"谁拿到话机谁认领分机"的口子。
2. 硬件规格、产品上限、容量规划工具用法、HA、UM 落地全部在书外——分别指向 feature list / product limits、Capacity Planning Tool、后续课程与 UM 文档；空间冗余 SIP 看 TC1652，8770 上 NFS 看 TC2024。
3. 书内口径漂移如实引用：OTMC 节点号 98/99 两例、声明章网段 151/155 混用、GA wav 路径两处、defaultVmLS 拼写两样——示例仅示意，现场以实际系统为准。

## 版权

- 本精华长文为 ALE Training Services《OpenTouch Message Center · Starter》（OTMCXTE200EN Issue 08）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
