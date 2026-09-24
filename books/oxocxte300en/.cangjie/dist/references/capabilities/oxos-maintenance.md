# 备份恢复、软件升级与系统复位（运维三板斧）

## R — 原文依据

> "OMC \ Data Saving & Swapping \Date & Time Data Saving • Program the date of the first back-up, the periodicity of the next ones"（p296）
> "Restore of a recovery point is only supported in the same major release … Supported file system is EXT2"（p304）
> "2 versions simultaneously available on a system An active version A replacement version"（p316）
> "When Cold reset is triggered without selecting any sub options • The following settings are not deleted: • Installer passwords • Network settings • Management services access flags • Cloud Connect parameters"（p323）

出处：OXOCXTE300EN p292-324（数据保存讲义+备份实验、软件下载讲义、系统复位讲义）。

## I — 自述

**备份四线**：

- 基础自动备份：OMC/Data Saving & Swapping/Date & Time Data Saving 定首次日期与周期；PowerCPU EE 存 eMMC/MSDB、OCE 存文件系统
- OMC 手动备份恢复：Read all from PCX → Save As → Backup/Store 到外部介质（.cdb）；恢复走 Auto-Connect for Restore（installer 密码）
- OCE SD 卡：关机插卡、AES 256 加密、多恢复点（最旧自动滚动删除）；卡 2-32GB、SD/SDHC 支持 SDXC 不支持、仅 OMC 格式化、EXT2；恢复仅限同主版本
- DBAdapter：跨版本打开旧库自动透明转换（MyPortal 装 DBAdapterSetup.msi）

**软件升级**：系统同时保留 active+replacement 双版本；MyPortal 下载三件套（PBX 软件 zip+配套 OMC zip+配套技术通函）；下载流程=传输、Data saving、Swap（排程在 SW-downloading）、restore；回退用 switchover 切回前版本。

**三种复位**：

- Warm：重启不丢库，解锁硬件故障（手动关机再开=Warm）
- Cold：回默认配置；不勾子选项时保留 installer 密码、网络设置、管理服务接入旗标、Cloud Connect 参数
- Factory：Cold 全删之外再删系统日志，状态接近 Lola 安装态（LOLA 书内无定义，见 needs-review nr-04）

## A1 — 书中案例

**备份恢复实验**（p307-314）：

1. OMC → Comm → Read all from PCX（主对象默认勾选），传输完成
2. File → Save As 命名保存（默认 Documents\OMC）
3. 导出外部介质：先 Comm → Disconnect，再 Backup/Store 到 USB/网络盘
4. 导入：断开状态下 Backup → Restore → 选介质上的库
5. 在线恢复：Auto-Connect for Restore，输 installer 密码，选 Classic data → OK
6. 传输完成提示重启 → Yes；系统自动 warm reset 后重连
7. 验收：OMC 在线且配置与备份一致；部分更新在重启后生效

**讲义口径操作**（p315-324，无独立实验——见 needs-review nr-05）：

1. 升级三件套从 MyPortal 下载并解压到管理 PC
2. OMC/Tools/Software download → 下载密码 → 会话生效
3. Swap 排程：OMC/Data saving and swapping/SW-downloading
4. 回退：switchover 切回 active 前版本
5. 复位入口：话机 MMC 话务员会话 Menu/Operator/Expert/System reset 或 OMC Expert/System Miscellaneous/System Reset

## A2 — 未来触发

使用情境：交付收尾建备份制度；升级前快照；升级失败要回退；系统故障选哪种复位；设备转手要清干净；换 CPU 板。

语言信号：备份 / backup / 恢复 / restore / SD 卡 / DBAdapter / .cdb / 软件下载 / software download / Swap / switchover / 版本 / 升级 / warm reset / cold reset / factory reset / 复位。

与相邻能力区分：复位后重建配置 → 开通能力（初始安装向导）；升级前的密码与安全核对 → 安全基线卡。本能力到"可恢复的备份体系+受控版本"为止。

## E — 可执行步骤

输入契约：当前库状态、目标版本三件套、介质（USB/网络盘/SD 卡）、installer 密码。Cold/Factory 前无有效备份 → 判停先补备份。

1. 建制度：设自动备份首次日期与周期。完成标准：备份计划成文并生效
2. 手动快照：Read all from PCX → Save As → 导出外部介质。完成标准：介质上有可导入的 .cdb
3. （OCE）SD 卡线：关机插卡 → OMC 格式化 → 启用计划备份。完成标准：恢复点生成
4. 升级：核版本配套、下载三件套、先备份 → Software download → Swap 排程。完成标准：新版本 active、业务拨测通过
5. 回退：switchover 切回前版本。完成标准：业务恢复且原因记录
6. 故障复位：按损失最小原则选 Warm → Cold（带选项）→ Factory。完成标准：复位后按预案重建
7. 跨版本读旧库：装 DBAdapter 后透明转换。完成标准：旧 .cdb 可在最新 OMC 打开

判停点：

- SD 卡想跨主版本恢复 → 不支持（n21），回滚走 switchover 而不是恢复点
- 换 CPU 后服务起不来 → 软件钥匙与主 CPU 序列号绑定，必须重新生成 license（n22）
- "Cold=全清"是误解——转手/回收要勾全子选项或用 Factory（n23）
- Factory 后系统接近 Lola 态且删除系统日志——排障证据在复位前先导出

输出契约：备份制度（周期/介质/恢复点）+ 版本台账（active/replacement）+ 复位操作记录。

## B — 边界

- 软件下载与 Swap、复位均为讲义口径，无书内实验验收步骤（needs-review nr-05）
- eMMC 复用需重新生成许可；SD 卡为 ALE 不提供的选件
- MyPortal 下载权限在客户/伙伴账户侧，书外流程
- 下载密码（系统启动时定制）纳入密码管理清单，与七账户密码表同域
