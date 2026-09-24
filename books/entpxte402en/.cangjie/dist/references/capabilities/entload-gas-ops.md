# GAS 日常运维：版本、备份、host 升级与 UPS

## R — 原文依据

> ""gasversion" command to get version of GAS, OXE, OXE-MS, Rainbow WebRTC gateway and Rocky Linux operating system"（p239）
> "Archive file is created by default in "/var/backup/" directory, in "<oxe_name>_YYMMDD.tar.gz" format • The archive file contains "mao-acc" and "Postinstall.cfg" files"（p240）
> "GAS package fresh installation + GAS backup = functional GAS system, without the need to perform the post-installation"（p241）
> "Automatic safe shutdown (server & VMs) if UPS battery power percentage reduces to configured value (Default: 30 %)"（p236）

出处：ENTPXTE402EN p236-241、p275-282。

## I — 自述

GAS 交付后的日常运维三件套加两条底线：

运维命令：

1. **gasversion**：查 GAS 包/OXE/OMS/WebRTC/Rocky 五层版本——交互菜单（1.GAS Package 2.OXE 3.OMS 4.WebRTC）或直接 gasversion all|package|oxe|oms|webrtc
2. **gasbackup**：整 GAS 备份（OXE 数据库、各组件网络配置、许可文件）

   - 交互模式问 OXE 账号/密码/路径（默认 /var/backup）；CLI 模式 gasbackup -u mtcl -p 口令 -d 路径 免确认
   - 产物 <oxe_name>_YYMMDD[_hhmmss].tar.gz + 同名 _PostInstall.cfg（后者仅静默恢复后安装用）
   - 归档含 *.ice、mao-acc、cho-dat、obstraf、acd、noe、PostInstall.cfg、hardware.mao 等
3. **uhwconf**：确认 "CPU Hosted On: GAS"（判断 OXE 宿主形态）

两条运维等式与前提：

- **全新安装 + 恢复备份 = 免后安装向导**即可用的 GAS 系统（恢复可在 GUI 或静默模式）
- 备份前提：OXE 许可控制已配置（.swk 入 /usr4/BACKUP/OPS、.ice 入 FlexLM 目录、OXE 指向 Flex 服务器）；gasbackup 经 SSH 连 OXE（swinst 账号）
- host 升级两条路：SOT 建 GAS 型 "Project for existing products" 选新 bootdvd iso；或挂载 BootDVD 后跑 gas-rocky-update.sh（升级前 OXE/OMS/WebRTC 三个 VM 优雅关机，Rocky 随后重启——全系统停机窗口）
- host 升级日志：/var/log/rocky-update.log 与 /var/log/gas-rocky-update.log
- UPS：USB 信号线监控，NUT 包（BootDVD 内置）实现；电量降至阈值（默认 30%）自动安全关机（服务器+VM）；状态轮询默认 5 秒；事件记 /var/log/gasups.log

## A1 — 书中案例

**运维命令实操**（p275-282，How-To 附录）：

1. gasversion all 一次读出五层版本
2. gasbackup 交互备份：填 OXE 账号密码与路径后确认
3. 核对 /var/backup 下 .tar.gz 与 _PostInstall.cfg 成对出现
4. uhwconf 确认 OXE 宿主为 GAS
5. FlexLM 例行核对：lmutil lmstat -a 查许可占用
6. host 升级演练：挂 BootDVD 跑 gas-rocky-update.sh 并盯两份日志

## A2 — 未来触发

使用情境：GAS 各组件版本怎么看；换机/灾备怎么恢复最快；宿主 Rocky 打补丁；UPS 接入与阈值；备份里有没有许可。

语言信号：gasversion / gasbackup / uhwconf / /var/backup / PostInstall.cfg / gas-rocky-update.sh / BootDVD / NUT / UPS / 30% / 优雅关机 / 静默恢复。

与相邻能力区分：

- GAS 初次加载与后安装 → GAS 交付卡
- OXE 本体的版本与补丁 → 补丁与多版本卡
- FlexLM 首次安装与 OXE 对接 → GAS 交付卡（本卡只管例行核对）

## E — 可执行步骤

输入契约：GAS 已交付在运、OXE swinst 账号与口令、备份存储位置、BootDVD 媒体（升级时）。许可控制未配置 → 判停先补许可，再谈备份。

1. 版本盘点：gasversion all 记录五层版本基线。完成标准：基线入档
2. 例行备份：gasbackup（或 CLI 带参数）执行并核对产物成对。完成标准：tar.gz+_PostInstall.cfg 在库
3. 恢复演练：确认"全新安装+备份=免后安装"路径可用。完成标准：演练记录在案
4. host 升级（按需）：排停机窗口，走 SOT 项目或 gas-rocky-update.sh。完成标准：Rocky 升级且 VM 全部拉起
5. UPS 核对：NUT 在跑、阈值 30%、轮询 5 秒、gasups.log 有事件。完成标准：断电预案成立

判停点：

- 宿主要升级但客户不知情 → 停，host 升级=全系统停机窗口，必须按停机维护排期
- 想用 GAS 型项目升级 OXE 版本 → 停，GAS 型项目无升级路径，OXE 升级用 OXE 型项目
- 备份文件缺 _PostInstall.cfg → 停，静默恢复会失效，重新备份
- 传文件用标准 FTP → 停，GAS 禁用 FTP，走 SFTP/SCP

输出契约：版本基线 + 备份/恢复演练记录 + host 升级与 UPS 应急预案。

## B — 边界

- 本卡只覆盖 GAS 宿主与打包层运维；OXE 数据库与应用配置不在本教材
- Eva-msg 缺失仅警告不阻塞备份（p15 口径）；备份跨机恢复需同版本 BootDVD
- 课件时长口径（加载约 60 分钟、后安装约 15-20 分钟）为培训环境值
- FlexLM 例行核对只读（lmstat）；改动配置与重启 OXE 的规则在 GAS 交付卡
