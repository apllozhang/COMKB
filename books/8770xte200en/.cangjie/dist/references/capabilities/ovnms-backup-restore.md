# OmniVista 8770 备份恢复（8770 数据库 rehosting + OXE swinst 全链）

## R — 原文依据

> "LDAP data ... / MariaDB database (Accounting, VoIP, Traffic, alarms, audit data and reports) / Others data (Customized dictionaries, scheduled task, loader data, license file) / RestoreContext.ini file"（p507）
> "A backup is dedicated to a version. It cannot be restored on a server running another version."（p510）
> "Comparison of RestoreContext.ini files ... will exclude the hostname svNMCName and domain svDomain entries."（p512）
> "You must stop the telephone application of OXE to be able to restore a database. But by stopping such process, you disable the role address facility."（p589）

出处：8770XTE200EN p503-521（8770 Maintenance）、p568-593（OXE backup & restore）。

## I — 自述

两层灾备：先保 8770 自己（网管大脑），再保 OXE（通话系统）。两条铁律贯穿：版本绑定、恢复窗口。

**8770 数据库备份恢复**

- 备份四块内容：LDAP 数据（系统配置+目录库）、MariaDB 数据（计费/VoIP/话务/告警/审计与报告）、其他（自定义字典/计划任务/loader 数据/许可文件）、RestoreContext.ini
- 铁律：备份与版本强绑定（RestoreContext.ini 的 nmcVersion 决定可还原的版本）；备份期间 8770 不可用（话务不受影响）
- 维护设置：8770 Maintenance > Preferences > Maintenance > Configuration 定备份位置（默认 C:\8770_ARC\8770Backup）、双阈值告警（磁盘空间或容量）、记录寿命（由 Scheduler 日检删除）
- 立即备份：双击 Databases - Immediate backup > 确认位置 > 执行；备份目录名 YYYYMMDDHHMMSS
- 恢复前提：先删 Configuration 中全部节点 + 删全部告警；确认备份的 nmcVersion 与目标服务器一致
- rehosting 三场景：改 IP=备份 > 改 IP > Restore databases with rehosting（脚本更新配置）；改 FQDN 同机=卸载 > 改 FQDN > 同参数重装（密码/目录树/路径不变）；换机（含 FQDN）=新机同参数安装 > rehosting 恢复（比对 RestoreContext 时排除 svNMCName/svDomain）

**OXE 备份恢复（bck + swinst）**

- 备份选项：Maintenance > Preferences > Maintenance > OXE Configuration 定位置（默认 c:\8770_ARC\OXEBackup）+ 勾 Enable PCX automatic backup
- OXE 侧参数：Data Collection 勾 Automatic database save；Software download 填 mtcl；Connectivity 填 swinst 密码
- 立即/计划备份：Maintenance 双击 PCX - Backup > 选数据类型（mao/语音导引/OPS）> Simple job，Start Date=Now 或 As scheduled + Repeat Daily
- 机制：8770 经 Telnet/SSH（mtcl）让 OXE 跑 bck 命令（swinst 密码授权），OXE 生成 /usr4/BACKUP/IMMED 与 /usr4/BACKUP/OPS 文件，8770 经 FTP/SFTP（adfexc）取回，存 OXEBackup\<网络>\<子网>\<节点>\<时间戳>
- 恢复链（七步）：PCX - Restore 选 MAO 备份 > swinst 会话 Easy 菜单 7 停电话（y）> 重进 swinst > Expert 2 > 4 Backup & restore > 3 Restore operations > 1 from cpu disk > 1 IMMEDIATE > 2 Restore mao data（securing 填 n）> Expert 6 > 2 Autostart management > 1 Set autostart > Easy 菜单 8 起电话 > 核对被删用户已还原

**恢复窗口管理**

- OXE 停电话期间业务中断，且 role address 设施失效——原用角色 IP 的会话全断，重连必须用物理 CPU IP
- 凭据代际：N2 及以前有默认密码（mtcl/adfexc/SoftInst），N3 起必须已自定义

## A1 — 书中案例

**8770 备份恢复实验**（p514-521）：

1. 维护设置确认备份位置与阈值、寿命
2. 双击 Databases - Immediate backup，默认目录下生成时间戳目录
3. 目录内含 LDAP/MariaDB/其他数据与 RestoreContext.ini
4. 删节点与告警后走 Restore - databases，Search 选备份目录执行恢复
5. 恢复完成后被删节点与告警重建

**OXE 备份恢复实验**（p579-593）：

1. 配 OXE Configuration 备份位置并启用自动备份
2. 立即备份走 Simple job=Now，OXE 侧 ll /usr4/BACKUP/IMMED 与 OPS 核对，8770 侧目录落盘
3. 计划备份 As scheduled + Repeat Daily，Scheduler 中 Execute Now 核验
4. OXE 删部分用户后 PCX - Restore 传回备份
5. swinst 七步链完成恢复，被删用户还原、Autostart 设回、电话重启

## A2 — 未来触发

使用情境：灾备预案编写；机房搬迁换机；改 IP/改 FQDN；升级前快照；OXE 数据回滚；"备份怎么还原到新版本"。

语言信号：Immediate backup / Restore - databases / rehosting / RestoreContext.ini / nmcVersion / svNMCName / 8770Backup / PCX - Backup / bck / /usr4/BACKUP / swinst / 停电话 / role address / Autostart。

与相邻能力区分：备份落到网络盘（网络驱动器能力）；许可文件内容与更新（许可管理能力）；本能力管备份恢复执行与预案。

## E — 可执行步骤

输入契约：备份窗口（8770 不可用/OXE 停电话）获批、版本匹配确认、OXE 侧 mtcl/swinst 凭据、目标位置（本地或网络盘已映射）。

8770 线

1. 维护设置：位置+双阈值+寿命。完成标准：设置保存且阈值告警可触发
2. 立即备份并核对时间戳目录四块内容。完成标准：RestoreContext.ini 在内
3. 恢复演练：删节点+删告警 > 核对 nmcVersion > Restore - databases。完成标准：节点与告警重建

rehosting 线

4. 改 IP：备份 > 改 IP > Restore databases with rehosting。完成标准：新 IP 可登录、配置完整
5. 换机：新机同参数安装（含 FQDN）> rehosting 恢复。完成标准：服务与数据迁移完成，客户端按新地址接入

OXE 线

6. 备份参数三件套 + 立即/计划备份。完成标准：OXE 与 8770 两侧目录出现备份文件
7. 恢复七步链按序执行（securing 填 n）。完成标准：被删用户还原、Autostart 设回、电话重启
8. 预案归档：窗口、凭据、物理 IP、目录路径写入预案文档。完成标准：演练记录可复查

判停点：

- 跨版本恢复请求（nmcVersion 不一致）→ 判停：先装同版本或重装同版本再恢复，不存在跨版本还原
- OXE 恢复不能接受停电话窗口 → 判停改期，不做"热恢复"尝试
- 停电话后会话断开 → 用 OXE 物理 CPU IP 重连（role address 已失效），不要判"设备故障"
- 网络盘位置不可见 → 先查网络驱动器映射与服务账号（网络驱动器卡），不要改成本地路径了事

输出契约：备份目录与四块内容清单 + 恢复/演练记录 + rehosting 前后参数表 + OXE 恢复窗口报告。

## B — 边界

- 备份期间 8770 网管不可用（话务不受影响）；OXE 停电话期间业务中断——两窗口都要提前报备
- 高可用/双机热备不在本书范围：许可文件 Redundancy 字段是唯一痕迹，容灾设计引 High Availability 产品文档
- OXE 侧 bck/swinst 命令完整语法属 OXE 系统文档；本卡只覆盖 8770 视角的编排
- 8770 侧默认/实验凭据（目录管理器密码、swinst 密码等）见 book/overview；生产必须替换
- 网络盘备份依赖 ExecdEx/SaveRestore 服务账号配置正确，见网络驱动器卡
