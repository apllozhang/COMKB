# 维护工具箱：Webdiag 排障、Noteworthy 调参与 LoLa 系统加载

## R — 原文依据

> "Login: installer … Operator and Manufacturer sessions are also available"（p560）
> "Writing a value to the wrong address can result in a deterioration in the operation of the system … Noteworthy addresses return to their default values following a cold reset"（p575）
> "Find on MyPortal, the technical communication listing all the Noteworthy addresses • TC1398 OXO Connect Noteworthy addresses"（p578）
> "Lola allows the complete loading of a PowerCPU or OCE • Loading of the call handling software • Loading of the application packages VoIP and ACD • Loading of the main and CTI software licenses"（p583）
> "The phones configuration and the voice prompts must be saved by OMC"（p583）

出处：OXOCXTE301EN p553-591。

## I — 自述

售后进阶三件工具，各管一层：

**Webdiag**（p559-570）：https://OXO@IP/services/webapp/ 或 OMC/Tools 进入；三会话分工——installer（全功能调试/证书/抓包/DECT）、operator（每实体 MoH 上传、Hot Desking 监督注销、解锁用户账户）、manufacturer（技术支持专用）。信息树七块：

- Start（启动/数据保存恢复/串口）
- Information（版本/机柜拓扑/Config Check）
- System（日志/Dump 摘要/复位 warm、cold 与出厂）
- VoIP（Traces/状态/Debug/Telnet Control）
- DECT（集群同步/已注册手柄/基站统计）
- Certificates（证书管理主接口）
- Services（ACD/IM/Hot desking/用户账户/Cloud Connect/Rainbow status）

CPU 启动监视走 V24（115200 8 N 1）。

**Noteworthy 地址**（p574-581）：内存读写调服务器全局参数，四类——Timer Labels、Debug Labels、Other Labels、Numeric Addresses（十六进制）。清单以 TC1398 为准；写错可致系统恶化；cold reset 全部回默认。书内实例：

- PerAssAlwd、DivRemCust、AATypTrf、MLTSETRING、TmpMenLTim、NotiAppTim
- AutoPwdChk、VMUMaxTry、MLAA_MSG、sipphone_sess_tim、Auto_Reset

**LoLa**（p582-591）：完整加载 PowerCPU/OCE（呼叫处理软件、应用包、license），三类流程 Installation / Migration Mono CPU / Install-Restore。

- 数据分工：LoLa 管话机数据（留言/NMC 工单），话机配置与语音提示必须 OMC 先存后恢复（p49）
- installer 密码遗失且 Console 重置被禁时的现场兜底（p325）

## A1 — 书中案例

**Webdiag 排障五连查实验**（p571-573，厂商实验）：

1. OMC/Tools/Webdiag，login: installer + installer 密码（教室例 Alcatel1，实验口径）。
2. Start/System Start 查机架板型。
3. Information/General Information 查软件版本。
4. Information/Cabinet Topology 查 MAC 与序列号。
5. System/Dump System 出系统摘要（可作报障附件）。

**Noteworthy 修改两例实验**（p579-581，厂商实验）：

1. 自动重启：Memory Read/Write/Debug Labels 选 Auto_Reset，Offset 填 "01 05 03 1E"（周五 3:30）→Modify→Write。
2. 铃音节奏：Other labels 记 Ringing 基址（例 0242D978，随软件版本变化）。
3. 从 TC 附录 B 查内部 UA 铃偏移 9AH，与基址求和得 Numeric 地址 0242DA12。
4. Numeric Addresses 读出（长度 14）后写入新节奏（响 2s=C8、静 1s=64），warm reset 生效。
5. 验证：周五 3:30 自动重启触发；内呼铃声呈 2 秒响 1 秒静（周期必须 <4 秒）。

**LoLa 迁移**（p584-591，讲义）：

1. OCE 进 LoLa 模式：按住电源键至 LED 快闪绿；PowerCPU 用交叉网线+Dip switch。
2. Step 1 定位交付文件（C:\Releasexxx）、语言、国家、license 文件（.csl/.msl）、应用包。
3. Step 2 选类型（新装/抹数据安装/Mono CPU 迁移/Install-Restore）。
4. Mono 迁移序：OMC Backup、旧 CPU 备份话机数据、新 CPU 下载恢复、重启、OMC 恢复。

## A2 — 未来触发

使用情境：系统状态/版本/序列号怎么查；报障要收集什么；抓包与日志从哪出；解锁被锁账户；改系统默认振铃/定时器；installer 密码丢了；换 CPU 迁移；退役设备净化。

语言信号：Webdiag / installer / Dump / 抓包 / TCP Dump / 解锁 / noteworthy / Memory Read Write / label / AutoPwdChk / VMUMaxTry / TC1398 / 铃音 / LoLa / 迁移 / cold reset / warm reset。

与相邻能力区分：各能力域的"验证动作"（注册判定、指示灯、LED）分散在对应卡内，本卡管工具本身与系统级调参；证书管理界面归证书套件能力；Console 口重置开关的安全口径归安全加固能力。

## E — 可执行步骤

输入契约：问题现象、访问权限（installer/operator）、TC1398 与对应 TC 附录、交付文件与 license 文件（LoLa）。无 TC1398 或地址依据 → 判停：不猜地址、不抄书例基址。

1. 排障五连查：板型、版本、MAC/序列号、Dump 摘要（p572-573）。完成标准：报障材料齐
2. 按域定位：VoIP 抓包/状态、DECT 块、Services 解锁与监督、System 日志与复位。完成标准：信息到手
3. （noteworthy）TC1398 查地址，选类型、Details 改字节、Modify、Write，然后 warm reset。完成标准：参数生效
4. （Numeric 类）基址（随版本变化）加 TC 附录偏移求和，按长度 Read 后写入，warm reset。完成标准：算法留痕
5. （LoLa）确认 OMC 已存话机配置与语音提示→进 LoLa 模式→按类型走三步向导。完成标准：系统加载完成
6. （退役净化）清 MLAA/ACD 语音资产→ACD/SCR 出厂→三档冷复位（p593）。完成标准：数据清空

判停点：

- 写错 noteworthy 可致系统恶化 → 改前备份、改后测试；cold reset 会把全部调优打回默认（n38）
- Ringing 基址照抄书例 → 禁止：0242D978 随软件版本变化（n39），必须现算
- 铃音节奏周期 ≥4 秒 → 不合法（p581），重新设计节奏
- installer 密码遗失且 Console 重置被禁 → 只能现场 LoLa，ALE 无远程重置（n48）：接手老站点先查开关再报价
- PhD-relay 调试 trace → 用完必须擦除（n37）

输出契约：排障材料包（Dump/日志/抓包）+ noteworthy 变更台账（地址/旧值/新值/依据）+ LoLa 加载或迁移记录 + 净化确认单。

## B — 边界

- Webdiag 三会话权限分明：operator 只能 MoH/Hot Desking 监督/解锁，证书与调试归 installer；manufacturer 是 ALE 支持专用
- Noteworthy 是"地下层"配置：本卡只给流程与已知实例语义，地址全量清单与算法偏移一律以 TC1398 及附录为准
- LoLa 的版本建议查最新 TC、应用/板兼容查 OXO Connect Cross compatibility（MyPortal）；话机配置与语音提示必须 OMC 单独保存（p49）
- 冷复位不擦自签证书（n40，推断：净化设备需另行处理证书）
- Webdiag 登录密码为客户环境值（教室例 Alcatel1 仅为实验口径）；生产纳入密码树管理
