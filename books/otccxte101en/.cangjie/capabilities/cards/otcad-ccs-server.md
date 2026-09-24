# CCS Server 集中接入（内部 serv_ccs、外部 Windows 服务、客户端切换）

## R — 原文依据

> "Internal CCs server: • The process "serv_ccs" is started on the OmniPCX • 15 CCsupervision Clients simultaneously connected • External CCs server: • "server CCs" service is started on the PC • 120 CCsupervision Client simultaneously connected"（p557）
> "The CCs server is mandatory for these releases when the CCs connections numbers to the PCX is greater than 9 (whatever the CCs type, mono-site or multi-site)"（p567）
> "The AFE server can receive only one CCs server. • If the service (external CCs server) is started and the process (internal CCs server) isn't stopped, the connection of the external CCs server is rejected by the AFE server."（p575）

出处：OTCCXTE101EN p555-590。

## I — 自述

CCS 客户端接入的三种形态：

| 形态 | 承载 | 容量 | 要点 |
|---|---|---|---|
| 直连 AFE | CCS 直接连 OXE 的 CCD 程序 | AFE 物理上限 15 连接 | 每客户端占 1 连接；Ping-pong 周期默认 30 秒 |
| 内部 CCS Server | OXE 上 serv_ccs 进程（serv_ccs_on_dhs=1） | 15 个 CCS 客户端 | 自身占 AFE 一条连接，客户端实得 14 |
| 外部 CCS Server | Windows Server 2019/2022 服务（serv_ccs.msi） | 120 个 CCS 客户端 | 需先停 OXE 内部进程（置 0 并重启 MAIN_AFE） |

强制条件：CCd R3.1 + CCs 4.3.46.1 起，连接数 >9（不分单/多站点）必须用 CCS Server；一个 AFE 只能接一个 CCS Server——内部进程未停时外部服务会被 AFE 拒接（n33）。

客户端切换：Window > Customise > Network 把 Direct connexion 改为经 CCS Server（填服务器 IP），提示后重启 CCS。

维护锚点四件：CCS Real Time > Licenses 看锁占用（AFE 1 连接+Server 1 连接+monosite 令牌）；adm_acd option 11 看 *SERV_CCS* 终端；
adm_acd <Server IP> -servccs option 10 看经服务器接入的客户端（自报 maxCli=150、maxConnected=120）；日志 servccsYYMMDD.log。

## A1 — 书中案例

**从内部到外部的切换**（p580-590，外部 Server 装在实验 Windows Server 192.168.1.70）：

1. 摸底直连：CCS 核对直连参数（Ping-pong 30 秒、Memorise connections），Real time > Licences 记录当前锁
2. 查内部 Server：OXE console（mtcl）ps -edf|grep serv_ccs；adm_acd option 11 见 *SERV_CCS* 终端与 SALB
3. 停内部进程：nano /usr3/afe/parameters.cfg 把 serv_ccs_on_dhs 由 1 改 0，dhs3_init -R MAIN_AFE，ps 复核进程消失
4. 装外部服务：serv_ccs.msi 安装（Setup Type 选 Alcatel-Lucent CCS Server，填主 CPU IP），再用 Ccs Server Installation 工具建服务并启动
5. 验服务：CCS Server Status 应用 Connect 后双绿灯（Server 绿+CCD 绿）
6. 客户端改接：Network 页填 CCS Server IP，重启 CCS 后 Licences 复核
7. 终验：adm_acd 192.168.1.70 -servccs option 10，核对 "CCS Server release 8.0 cnx= 1, afe= 1" 与客户端在列

## A2 — 未来触发

使用情境：监督员超过 15 人连不上；客户要求集中接入/多客户端共享；从直连或内部 Server 迁移到外部 Server；外部服务连不上 AFE。

语言信号：CCS Server / serv_ccs / serv_ccs_on_dhs / 外部服务器 / 内部服务器 / 15 客户端 / 120 客户端 / AFE 连接 / maxCli / maxConnected / 拒接 / -servccs / Server Status / 集中接入。

与相邻能力区分：CCS 首次安装与 OXE 声明转 CCS 安装与实验环境卡（路由卡）；实时锁与许可语义归本卡维护锚点；CCS 客户端日常排障转 ACD 维护命令箱卡（路由卡）。

## E — 可执行步骤

输入契约：OXE 管理权（mtcl）、一台 Windows Server 2019/2022（外部形态）、客户端数量与接入规划。宿主 OS 不满足 → 停，先换/升 OS（p567）。

1. 摸底：数清当前 CCS 连接数，>9 即必须上 CCS Server；记录现有许可锁。完成标准：接入形态决策有据
2. 选形态：≤15 客户端可留内部 Server；>15 或要独立承载时走外部 Server。完成标准：形态确定
3. 内部转外部：先停 OXE 内部进程（serv_ccs_on_dhs=0 + 重启 MAIN_AFE + ps 复核）。完成标准：进程消失
4. 装外部服务并用 Status 工具验证双绿灯。完成标准：Server 与 CCD 均 Green
5. 客户端逐台改接 Network 指向 Server IP 并重启 CCS。完成标准：Licenses 显示经服务器接入
6. 终验：adm_acd <Server IP> -servccs option 10 核对 cnx/afe/nbCli 与 maxConnected。完成标准：与设计一致

判停点：

- 外部服务启动后被 AFE 拒接 → 停，第一查内部 serv_ccs 是否真停（ps 应无输出），这是 n33 场景，不是网络故障
- 规划依据出现 "29 or 120" → 停，按 nr-01 双口径处理：以 15/120 与 ">9 强制"为准，标注原文如此
- 客户端规模要超 120 → 停，超出本书与 CCS Server 口径，转产品文档评估分域接入

输出契约：接入形态决策记录 + 内/外部切换操作记录 + 客户端接入清单与许可锁快照。

## B — 边界

- p558 "29 or 120 CCs max" 与同页图示 15/120 矛盾（nr-01，推断为笔误）；规划一律按 15/120 与 >9 强制口径
- 外部 Server 仅支持 Windows Server 2019/2022（p567）；maxCli=150 是服务自报上限，有效客户端上限按 120 口径
- 一个 AFE 只能接一个 CCS Server（p575/p590 原文 "Only 1 CCS Server can connect to the PABX!"），双 Server 方案不存在
- adm_acd option 编号以 R10.15 为准（f15 conditions）；跨版本先核对命令树
- 内部 Server 占 AFE 一条连接、客户端实得 14 的口径来自 p558 图示（14 connections max + 1 connection）
