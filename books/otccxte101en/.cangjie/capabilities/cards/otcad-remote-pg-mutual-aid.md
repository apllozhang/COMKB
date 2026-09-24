# Remote PG 分布式互助与 ABC-F 链路（虚拟队列、专用 Pilot、故障注入）

## R — 原文依据

> "Remote PG • Processing Group of the local node • Has a minimum waiting time threshold (distribution threshold) and a resource selection priority but no call selection priority. • Virtual Queue • … the image of the head of the normal queue • Dedicated Pilot • Remote Pilot is dedicated to one Virtual Queue."（p319）
> "Information transferred: • Information on the originating pilot (number, name) • Status of the remote pilot • Voice Guides heard on the local node • Real Waiting Time"（p325）
> "Direct link 2002 to node 2:UP(Enabled/DATA_TRANS) High Bandwidth"（p341）

出处：OTCCXTE101EN p293-370。

## I — 自述

跨站点互助分两种：盲互助（无 ABC-F，远端当新呼叫处理）与智能互助（经 ABC-F 按远端状态路由）。Remote PG 是智能互助的分布式形态，三对象分工：

| 对象 | 所在节点 | 关键属性 |
|---|---|---|
| Remote PG | 本地 | Type=Remote，指向远端专用 Pilot；有分布门限+资源选择优先级，无呼叫选择优先级 |
| 虚拟队列 | 远端 | Type=Virtual，只映射本地队列队头呼叫的特征 |
| 专用 Pilot | 远端 | 一个虚拟队列专属，可被多个 Remote PG 调用 |

经 ABC-F 传输：源 Pilot 号/名、远端 Pilot 状态、本地已听语音引导、真实等待时间。远端拒收时按远端 Pilot 地址类型五类回退本地（重路由组/全局转发/闭锁/排队溢出/振铃溢出，p312）。

三级水位控制（排障与规划的主轴）：

| 参数 | 取值 | 语义 |
|---|---|---|
| 资源选择优先级 | 0-9 | 0 最高 9 最低；同优先级处理组之间按 LIT |
| 分布门限 thresho. | 秒（实验 15） | 呼叫在本地队列等满 N 秒才允许流向远端 |
| Maximum waiting time | 0-3276 秒 | 计算等待达阈值即把队列降为最低优先级；0=零等待队列（无资源立即改道） |
| Traffic Sampling Period | 2-15 分钟 | 平均等待时间滚动窗口；等待室不可用 |

链路体检两命令：compvisu sys（Direct Link 管理状态/H323/RTP Direct）；hybvisu -f all（四态 IDLE/SYN_REQ/SYN_ACK/DATA_TRANS，健康=DATA_TRANS；带宽 High=全编解码/Low=G729；接入数 1-24）。

## A1 — 书中案例

**Remote PG 部署与四类测试**（p338-370，编号为实验口径）：

1. 链路体检：compvisu sys 与 hybvisu -f all，确认链路 2002 UP/DATA_TRANS
2. 本地 WBM 建网络前缀：Translator > Prefix plan，Number=32602、Prefix Meaning=Network No.、Type=Pilot
3. 本地建 Remote_PG：Applications > CCD > Processing Group，DN=31851、Type=Remote、语音/数据 DN=32602
4. 本地 CCS：Normal_WQ 加 Remote_PG 并在 Resource selection 勾通方向
5. 远端 WBM：建 ACD 前缀、专用 Pilot 32602、虚拟队列 32703（Type=Virtual）、坐席 PG 32800、分配规则
6. 远端坐席 32500 登录后，测试一（优先级）：Agent_PG=0、Remote_PG=1，本地坐席优先
7. 测试二（门限）：thresho.=15 秒，本地忙时第二通等 15 秒转远端
8. 测试三（远端闭锁+本地饱和）：MWT=10 秒，溢出呼叫落 Voice_guide_PG 播 685 两遍后释放
9. 测试四（断链注入）：mgr 菜单临时 Disable 链路，Remote_PG blocked 而专用 Pilot 仍 open

## A2 — 未来触发

使用情境：多站点客户要互备坐席；远端坐席纳不进本地队列；溢出呼叫总被远端拒收；断链时话务流失评估；链路状态判读。

语言信号：Remote PG / 虚拟队列 / Virtual Queue / 专用 Pilot / Dedicated Pilot / 互助 / mutual aid / ABC-F / Direct IP Link / hybvisu / compvisu / 分布门限 / thresho / 资源选择优先级 / 拒收 / reject / 溢出。

与相邻能力区分：队列参数语义的告警与忙音行为转特殊功能卡；维护命令全表转 ACD 维护命令箱卡（路由卡）；链路的新建与组网规划在书外（OXE 组网文档）。

## E — 可执行步骤

输入契约：本地/远端两节点管理权、ABC-F 直连链路已建立、远端坐席与 PG 已规划。链路未建 → 停，先走 OXE 组网流程（书外）。

1. 体检链路：mtcl 下 compvisu sys + hybvisu -f all。完成标准：目标链路 UP(Enabled/DATA_TRANS)
2. 远端：建 ACD 前缀（必须先建，n20）> 虚拟队列（Type=Virtual）> 专用 Pilot > 坐席 PG 与分配规则。完成标准：远端矩阵就绪
3. 本地：建网络前缀（Network No.+节点号+Type=Pilot）> Remote PG（Type=Remote，指向专用 Pilot）。完成标准：pildstctx/pgctx 可查到对象
4. 双侧 CCS：接路由方向、勾通资源选择方向、设优先级与门限。完成标准：Navigator 两端状态正常
5. 行为验证三连：优先级（本地优先）、门限（等满 N 秒才溢出）、故障注入（断链/置忙后回退本地）。完成标准：三级水位行为与设计一致

判停点：

- Remote_PG 常驻 blocked → 停，按"远端 Pilot GFWD/闭锁、下游全闭锁、链路无时隙"三条件排查，不盲目重建对象
- 断链期间溢出话务直接播引导释放（n35） → 停，这是兜底设计；生产要另配告警与回拨策略，不是故障修复
- 客户要溢出话务建模/坐席数估算 → 停，书外能力，指向 Feature List 与话务数据

输出契约：可用的跨站点互助链路 + 三级水位参数记录 + 故障注入验证报告（含拒收回退路径）。

## B — 边界

- 全部实验编号（32602/31851/32703/32800）为实验口径；p364 "Agent2 (32500)" 称号系原文笔误，实为 Agent3（nr-04）
- 盲互助/智能互助的组网话务建模在书外（n39）；hybvisu 的 High/Low 带宽结论是实验口径，生产链路按带宽规划
- Maximum waiting time=0 是"零等待队列"语义，会立即改道，别当"不设限"配（n36）
- 两套"优先级"语义勿混：处理组之间 0-9 数字比大小（0 高），ACR Pilot 方向之间同优先级比 EWT（n34）
- 资源选择优先级同分时按 LIT——该 LIT 同样受坐席统计 5 分钟刷新约束（p04）
