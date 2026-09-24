# 配置生命周期（闪存三目录、保存/认证/回滚、备份恢复）

## R — 原文依据

> "The certified directory contains files that have been certified by an authorized user as the default files for the switch. The working directory is a holding place for new files."（p141）
> "IF THE OMNISWITCH IS REBOOTED WITH THE 'RELOAD ALL' COMMAND, IT WILL REBOOT FROM THE CERTIFIED DIRECTORY, NO MATTER WHAT THE CONTENT OF THE RUNNING DIRECTORY IS"（p142）
> "write memory flash-synchro = write memory + copy running certified"（p133）
> "When the switch boots from the CERTIFIED directory, changes made to the switch cannot be saved and files cannot be moved between directories."（p135）

出处：DT00XTE215EN p127-149。

## I — 自述

OmniSwitch 的配置可靠性模型是"三目录 + 两条启动判定规则 + 三条保存命令"：

1. **三目录**：working=新文件试验场；certified=授权用户认证过的回滚基线；running=当前启动目录（RAM 中的运行配置由它加载、再叠加未保存改动）；另有用户自定义目录（同 working 语义，可存多套镜像）
2. **启动判定**（p142）：冷启动时 running 目录与 certified 内容相同则回 running、不同则回 certified；reload all 无条件回 certified（强制回滚语义）；reload from <目录> 指定启动
3. **保存三命令**（p132-133）：write memory=RAM 同步到启动目录；copy running certified=启动目录覆盖认证基线；write memory flash-synchro=两者合一（VC 下同步全体成员）
4. **状态判读**：show running-directory 三字段——Running configuration（启动目录名）、Certify/Restore Status（CERTIFIED 或 CERTIFY NEEDED）、Synchronization（SYNCHRONIZED 或 NOT SYNCHRONIZED）
5. **备份两条线**（p136-137/p148）：配置备份：把横幅+userTable+vcboot.cfg 打包为 configuration_backup.tar，存 /flash/config-backup-recovery（上限 10 个）；USB 备份启用后写内存动作自动同步到 /uflash/<型号>/ 目录，可设 key 加密

**排障三问**（p142-147）：从哪启动（字段一）？是否已认证（字段二）？是否已保存（字段三）？

## A1 — 书中案例

**闪存目录实验**（p140-149，How-To）：

1. show microcode working/certified/loaded 查各目录镜像（实验镜像 8.10.9.R04，实验口径）
2. show running-directory 基线：Running=WORKING、CERTIFIED、SYNCHRONIZED
3. 制造未保存改动：vlan 2、vlan 3、vlan 99，show running-directory 变 NOT SYNCHRONIZED
4. 此时 reload all：重启后 VLAN 2/3/99 全部丢失（回滚到 certified）
5. 重做改动并 write memory：状态变 CERTIFY NEEDED + SYNCHRONIZED
6. 再次 reload all：从 certified 启动，但 working 里的配置文件仍在，可取回
7. 从 working 重启：reload from working no rollback-timeout，VLAN 2/3/99 重现
8. 验证 certified 只读：从 certified 运行时 vlan 4 后 write memory 直接报错
9. 用户目录：mkdir lab 并 cp working/*.* lab（boot.md5 报 permission denied 属正常），reload from lab 验证
10. 认证用户目录：copy running certified 成功后 show running-directory 显示 lab + CERTIFIED
11. 清理：rm -Rf lab 并 reload from working；USB 备份步骤在 R-Lab 无法演示（USB 口被占用，实验口径）

## A2 — 未来触发

使用情境：改配置重启后丢失；写内存与认证的区别；回滚到之前版本；升级前的配置备份；从 U 盘恢复；COPY 命令报错 certified 只读。

语言信号：write memory / flash-synchro / copy running certified / working / certified / 回滚 / reload all / show running-directory / CERTIFY NEEDED / NOT SYNCHRONIZED / 备份 / usb backup / userTable。

与相邻能力区分：

- VC 成员间的同步语义：Virtual Chassis 能力卡（flash-synchro 的 chassis 同步面）
- 镜像文件版本管理：升级与 Auto-Fabric 能力卡
- 账号文件 userTable 的治理：AAA 加固能力卡

## E — 可执行步骤

输入契约：变更内容与验收状态、是否 VC、回滚点要求、备份介质。copy running certified 前必须确认配置验证无误。

1. 基线确认：show running-directory 记录启动目录与三字段状态。完成标准：当前状态明确
2. 保存：write memory（VC 环境直接用 write memory flash-synchro）。完成标准：SYNCHRONIZED 且 Certify 状态明确
3. 认证基线：配置验证无误后 copy running certified（或并步 flash-synchro）。完成标准：CERTIFIED 且内容为验收版本
4. 回滚操作：强制回基线用 reload all；取回 working 未认证版本用 reload from working no rollback-timeout。完成标准：启动目录与预期一致
5. 备份：配置备份生成 tar（上限 10 个）；USB 线启用 usb backup 后写内存自动同步 /uflash。完成标准：备份文件可列出
6. 恢复演练：restore 自动选取 tar 解出三件；usb auto-copy 从 U 盘目录复制。完成标准：配置回到设备

判停点：

- write memory 报 "not permitted in certified mode" → 先 show running-directory 确认误从 certified 启动，再 reload from working，不要反复重试
- 配置尚未验证 → 停，不要执行 copy running certified，否则回滚点被污染
- 拔 U 盘 → 先 usb disable 卸载，否则可能损坏文件系统
- 把 reload all 当普通重启用 → 停，它会无条件回滚 certified，普通重启才按内容判定

输出契约：受控的配置状态（保存/认证/备份三确认）+ 回滚路径说明。

## B — 边界

- reload all 永远回 certified，即使内容相同；把 reload all 当普通重启用会无意触发回滚（p142）
- CERTIFY NEEDED 态断电：会从 certified 启动，working 里配置文件仍在、可经 reload from working 取回（p144）
- cp 目录时 boot.md5 的 permission denied 属正常（自动生成文件），lab 目录已存在同理忽略（p146）
- R-Lab 的 USB 口被 USB-to-Eth dongle 占用，USB 备份仅讲义口径（p148）
- certify-on-reboot（p134）仅当次登录有效，需再固化，勿当持久状态
- 镜像文件名随产品代际不同（Nos/Wos/Uos 等）；升级版本管理属升级与零触能力卡
