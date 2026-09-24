# OpenTouch 备份恢复与语音信箱统计（8770 备份/opentouchd/statistics.properties）

## R — 原文依据

> "The OmniVista 8770 Server establishes an SSH connection to the OpenTouch for running the backup command. … The 8770 server retrieves the backup archive from the OpenTouch server via SFTP."（p231）
> "Enter the command service opentouchd start in order to restart the OpenTouch services"（p245）
> "DON'T DELETE THE USER … FROM THE USERS APPLICATION! IF YOU DO SO, THE VIRTUAL SIP DEVICE WILL BE DELETED FROM THE OXE!"（p243）
> "Once the 'statistics.properties' file has been modified, don't forget to stop and start the masc service."（p258）

出处：OTMCXTE200EN p228-258（c12/c13、f23/f24、p22/p23/p25、n10/n30 归并）。

## I — 自述

**备份恢复（8770 发起两段式）**，链路五步：

1. 8770 经 SSH 执行备份命令
2. OTMC 生成归档（$BACKUP8770_HOME 下按 8770 FQDN/时间戳存放，含 filelist.txt、ngvm3、.zip、.zip.md5、version.txt）
3. 8770 经 SFTP 取回归档，OTMC 侧临时目录删除
4. 恢复方向相反：SFTP 传回备份、service iced stop 停服务、执行恢复、清临时文件
5. 管理员手工 service opentouchd start（重启 <5 分钟）

备份内容为 OpenTouch 数据库（ESS/ICS/ACS/FAX/MOH）+ 特定数据（IP 配置/许可/证书/设备部署数据）。

**配置面**：8770 侧默认备份目录（默认 C:\8770_ARC\OTBackup）、阈值（两级=次要/主要告警）、Record Life（超期备份由 Scheduler 每日清理）；OT 节点 Maintenance 页签维护账号（备份/恢复与 SSH 凭据）。跨版本恢复（旧版备份 → 高版本系统）必须勾 Force。

**语音信箱统计**：配置文件 /var/data/ics-group/vms/ngvm3/statistics.properties，按频率输出 XML/HTML/CSV：

| 参数 | 默认值 | 说明 |
|---|---|---|
| enableStatistics | disabled | 总开关 |
| enableStatisticsGeneration | enabled | 生成开关 |
| fileLocation | <streamRepository>/statistics | 输出目录，须手工创建并注意读写权限 |
| frequencyGeneration | day | month / week / day |
| timeGeneration | 22:00:00 | 生成时刻 |
| historicSize | 10 | 保留份数，超限滚动删旧，0 永不删 |
| freshness | P10DT0H0M0S | 删除数据保鲜期（ISO 8601 周期） |
| frequencyGC | after generation | 清理节奏（含 dayGC/timeGC） |

统计项按用户：登录名、电话号码、信箱 ID、信箱状态、留言总数/新留言/已听/已归档/已删。改完配置必须 service mascd stop/start。

## A1 — 书中案例

**备份恢复演练 + 统计启用**（c12+c13，维护账号等环境值见 book/overview）：

1. 配备份目录与阈值：Maintenance 应用 → Preferences → Maintenance >OT Configuration（目录/阈值/Record Life）
2. 配备份参数：Configuration 应用选 OpenTouch → Maintenance 页签：勾 Automatic database save、填维护账号
3. 执行备份：Operations 双击 OT 节点 – Backup，选 All OT data，Simple job 选 Now
4. 恢复验证准备：从 OT Configuration 窗口删测试用户（绝不能从 Users 应用删——会连带删 OXE 侧虚拟 SIP 设备，n10）
5. 执行恢复：Operations 双击 OT 节点 – Restore → 选备份目录（时间戳目录名口径）；跨版本勾 Force
6. 核对测试用户已恢复；SSH 维护账号登录 → su - 到 root → service opentouchd start（<5 分钟）
7. 统计配置：编辑 /var/data/ics-group/vms/ngvm3/statistics.properties（实验口径：启用、频率 day、指定星期与时刻、输出到自建目录）
8. 手工创建输出目录并确认读写权限；service mascd stop → service mascd start
9. 到生成时刻核对输出目录中的 XML/HTML/CSV 文件与统计项完整性

## A2 — 未来触发

使用情境：上线前定备份策略；恢复演练与 RTO 验证；系统迁移/版本升级前备份；客户要信箱用量报表；"统计文件一直不生成"。

语言信号：备份 / backup / 恢复 / restore / opentouchd / iced / SFTP / Record Life / Force / 统计 / statistics / statistics.properties / mascd / XML / CSV / 报表。

与相邻能力区分：备份的前提（OTMC 已纳管、有数据）→ otmsg-declaration-sync；统计反映的信箱策略 → otmsg-mailbox-profiles。

## E — 可执行步骤

输入契约：8770 可用、维护账号就位；虚拟环境须已有外置 NFS（NFS server 部署按 TC2024，书外）。统计需求：客户要的频率/格式/保留策略。

1. 备份基线：配目录/阈值/保留期，手动跑一次全量备份。完成标准：归档在 8770 侧可查
2. 恢复演练：删测试对象、执行恢复、核对数据、手工起服务。完成标准：RTO 实测成文（<5 分钟口径）
3. 统计启用：改 properties、建目录、重启 mascd。完成标准：文件按频率产出
4. 交付归档：备份策略/恢复步骤/统计样例写入运维手册。完成标准：客户可自运维

判停点：

- 恢复完服务没起 → 设计行为：起服务必须管理员手工做（service opentouchd start，<5 分钟），不要提前判失败（p245）
- 恢复测试要删用户 → 只能走 OT Configuration 窗口；从 Users 应用删会连带删 OXE 虚拟 SIP 设备（n10）
- 统计文件不生成 → 先查目录是否手工创建/读写权限、mascd 是否重启（n30），再看配置
- 虚拟环境备份目录配在本地 → 停，违反"必须外置 NFS"硬规则（n05）

输出契约：可运转的备份恢复闭环（含恢复后起服务步骤）+ 按频率产出的统计文件与样例报告。

## B — 边界

- NFS server 部署在 8770 上按 TC2024（Business Portal 可取），本书零步骤（n29）
- 归档时间戳格式 YYYY-MM-DD-hh-mm、恢复目录示例为 YYYYMMDDhhmmss 口径（p233/p244）
- HA 场景的备份差异不在本书（HA 本身书外，n23）
- 实验维护账号（otuser/maintenanceuser、root/superuser）、实验统计参数值见 book/overview
- masc 服务名以原文口径记录（service mascd stop/start，p258）
