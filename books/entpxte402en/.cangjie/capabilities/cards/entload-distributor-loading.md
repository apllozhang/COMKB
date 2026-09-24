# Easy Installation 分发器模式：无 SOT 环境的本地加载

## R — 原文依据

> "The BP must transfer, through FTP, the "ISO image" and/or "ZIP files" to the "/tmpd" directory of the Call Server"（p113）
> "In case of full software version or static patch, the installation must be performed on OXE inactive partition • For a dynamic patch, the choice is offered: active or inactive partition"（p113）
> "2.Expert menu/9.Remote download/10. 'Local load as distributor of ISO image/ZIP file and installation'"（p114）
> "REMOVES ONLY THE EXTRACTED FILES (FROM ISO & ZIP) STORED IN "/USR4/FTP/RLOAD" DIRECTORY. THE SOURCES FILES ... ARE AUTOMATICCALY DELETED AT THE END OF INSTALLATION"（p129-130）

出处：ENTPXTE402EN p111-130。

## I — 自述

客户环境不允许临时部署 SOT（外部 BP PC/虚机被拒）时的官方替代路径：OXE 自己当分发器，加载工具从"另一台服务器"变成"被加载的机器本身"。

前置与流程：

1. PC IP 加入 OXE 信任主机（netadmin 的 Security 菜单，Firewall(iptables) 下 Restricted Access 里 Add a trusted host）
2. Filezilla 把版本 iso / 补丁 zip 传到 CS 的 /tmpd 目录
3. swinst 账号登录，进 2 Expert 菜单的 9 Remote download，选 10 Local load as distributor，输入文件名确认（REMOTE LOAD OPERATION，Client CPU type DISTRI）
4. 分区规则：全版本与静态补丁强制装 inactive 分区；动态补丁可选（安装器询问 1 ACTIVE / 2 INACTIVE）
5. 复核：swinst 8-2 按分区查版本与补丁号（0=active、1=inactive）
6. 收尾：按需复制 Linux 数据与数据库（2-3 菜单）并切换分区（2-3-3）

文件落点与清理（方向别搞反）：

- 解包物落 /usr4/ftp/Rload/{version,patch,dynpatch}，不会自动删除、会累积吃满硬盘，用菜单 9-7 Cleaning operation 清理（只清 Rload）
- 手工传进 /tmpd 的 iso/zip 源文件在安装结束时自动删除，无需人工处理

## A1 — 书中案例

**分发器加载版本与补丁**（p116-130，How-To）：

1. 把 PC（192.168.1.9，实验口径）加入 OXE 信任主机并应用
2. Filezilla 传版本 iso 到 /tmpd
3. swinst 2-9-10 输入文件名，确认本地加载（inactive 分区）
4. swinst 8-2 按 1 复核 inactive 分区为新版本
5. 2-3-2 复制 Linux 数据，再 4 Duplicate database 复制数据库
6. 2-3-3 Switch on inactive version 切换重启
7. 静态补丁 zip 传 /tmpd，同 9-10 菜单装入 inactive
8. 动态补丁装入后按提示 downstat d/i/t 检查需下载对象
9. 收尾用 9-7 Cleaning operation 清空 Rload 解包物

## A2 — 未来触发

使用情境：客户现场不允许架 SOT；只能用 OXE 自身加载版本或补丁；/tmpd 传完文件装不上；磁盘被 Rload 占满。

语言信号：Easy Installation / Distributor / 分发器 / /tmpd / Rload / swinst 9-10 / Local load / REMOTE LOAD OPERATION / Cleaning operation / downstat。

与相邻能力区分：有 SOT 的常规加载 → CS 加载卡与补丁卡；补丁顺序律与切换细节 → 补丁与多版本卡（本卡流程与它共用分区语义）。

## E — 可执行步骤

输入契约：OXE 可登录（mtcl/swinst/root）、PC 与 OXE 网络可达、iso/zip 媒体在手、无重新分区需求。目标机磁盘要重排 → 停，本路径的前提是无重新分区。

1. 信任主机：PC IP 加入 OXE iptables 白名单并应用。完成标准：FTP 可连
2. 传输：iso/zip 传到 /tmpd。完成标准：文件就位
3. 加载：swinst 2-9-10 输文件名确认；全版本/静态补丁进 inactive。完成标准：OPERATION ENDED CORRECTLY
4. 复核：8-2 查目标分区版本/补丁号。完成标准：版本按预期推进
5. 数据复制与切换（按需）：2-3-2 复制、2-3-3 切换，首进 swinst 输国家码。完成标准：新版本生效
6. 清理：9-7 Cleaning operation 清 Rload（选本机 CPU，逐项确认）。完成标准：Rload 目录为空

判停点：

- 想"直接把新版本怼在 active 上" → 停，分发器路径全版本/静态补丁强制 inactive
- 动态补丁装完就交机 → 停，先 downstat d/i/t 跟完终端下载，否则部分话机行为不变
- 磁盘满了才想起清理 → 停，每次加载后主动 9-7 清理；/tmpd 源文件会自动删、Rload 不会

输出契约：无 SOT 环境下加载成功的版本/补丁记录 + Rload 已清理确认。

## B — 边界

- 本路径是"无需重新分区"前提下的替代方案；迁移类需求走完整加载与迁移指南
- 信任主机管理（netadmin Security 菜单）是本路径与许可恢复、gasbackup 共用的前置技能
- 动态补丁装完的 downstat 收尾属于补丁管理域，本卡引用其判据
- 实验口径：PC 192.168.1.9、文件名 nYYYY.iso 示例——现场以实际媒体命名
