# DECT 日常维护与排障（命令族/syslog 日志收集/WBM）

## R — 原文依据

> "The following tools are adapted to work for xBS in the same way as for IBS: dectview / dectinston / dectinfo / dectarea / dectobs / obstraf / ippstat / downstat / Domstat / tftp_check"（p137）
> "P = data sync Primary xbs (the one which collects data) M = Master configured (for DECT synchronization) B = Backup configured (for DECT synchronization)"（p116）
> "SYSLOG IP address < Enter the IP address of the syslog server > ... SYSLOG port 514"（p160）
> "Debug: Used for troubleshooting. Must not be enabled during normal operation."（p160）

出处：DECTXTE200EN p116, p137-139, p153-161, p230-234。

## I — 自述

售后日常的三套抓手（命令均在 mtcl 下，xBS 与 IBS 通用）：

1. **命令族清单**（mtcl 下，xBS 与 IBS 通用）：

   - 状态查询：dectview xbs/ibs/com（基站表/通话表）、dectinfo（全局）、dectarea（位置区）
   - 同步树：xbssynchro（从 Data Sync Primary 取树，文本输出 RPN+RSSI）
   - 事件与链路：incvisu | grep xBS（或事件码 60/78）、listerm <mg> <cpl>（UA 链路）、listibs p <mg> <cpl> 0 <equip>（IBS 详情）
   - 复位与抓包：outserv/inserv；tcdump -s 0 -w /tmp/*.cap（root）或 xBS WBM 内 PCAP
   - 辅助：tftp_check / Domstat / obstraf
2. **dectview xbs 标志判读**：OK 在服 / NOK 停服 / OOS 已 outserv；P = Data Sync Primary（收集数据的站）、M = Master configured、B = Backup configured、+ = Master free running——P/M/B 是同步与切换健康度的第一读数。
3. **日志收集（syslog）**：OXE 侧 PWT/DECT System / xBS system 配 SYSLOG IP+端口（默认 514），按基站设四级：

   - off：不记录
   - Normal operation：呼叫、注册、定位、拥塞丢话、严重错误
   - System Analyze：漫游、手机固件状态（含 Normal 全部）
   - Debug：排障专用，禁常开

建议全部 xBS 日志落同一文件便于关联；WBM Syslog 菜单核验下发结果。

WBM 是排障入口之一（PCAP/同步树/统计/IP 设置），但其修改可被 PBX 下发覆盖——临时改动要记录，长期变更回 OXE 数据库做（p77）。

## A1 — 书中案例

**日志收集实验**（p155-161）：

1. 客户端 PC 装 Visual Syslog server（安装包在 NAS，实验口径映射 \\12.0.0.2\RLAB\ENTP）
2. PWT/DECT System / xBS system → Modify → SYSLOG IP address=192.168.1.9（实验口径）、SYSLOG port=514
3. xBS base station → 选基站 → Syslog level=Debug（排障档）
4. 基站侧核验：xBS WBM → Syslog 菜单核对 IP/port/级别已下发
5. 服务器侧核验：Visual Syslog 界面收到该基站日志

**状态判读**（p116/p147）：dectview xbs 输出表尾图例逐字对照 P/M/B/+/OOS 标志，再据标志分流（同步问题找 M/B、切换问题找 P）。

## A2 — 未来触发

使用情境：用户报断话/掉注册先看什么；要收基站日志给二线；基站状态灯异常；切换失败初判；排障完收尾。

语言信号：dectview / dectinfo / xbssynchro / incvisu / tcdump / listerm / listibs / outserv / inserv / 日志 / syslog / Syslog level / Debug / 514 / PCAP / LED / 排障 / troubleshooting / P 标志 / M 标志。

与相邻能力区分：同步拓扑怎么配见同步拓扑能力；固件下载失败的重试操作见固件管理能力；基站部署入库见 IP-xBS 部署能力；本卡只管判读、日志与取证分流。

## E — 可执行步骤

输入契约：故障现象（断话/掉注册/切换失败/状态异常）、受影响基站/手机清单、syslog 服务器（可用性）。

1. 初判：dectview xbs/ibs 拉状态表，对照 P/M/B/OK/NOK/OOS 标志。完成标准：异常站与标志定位
2. 分流：同步问题用 xbssynchro 看树，事件用 incvisu | grep xBS，UA 链路用 listerm，IBS 详情用 listibs。完成标准：问题域收窄
3. 取证：按需开 Debug 级别收 syslog（端口 514），或 WBM/tcdump 抓 PCAP。完成标准：日志/包可交付
4. 恢复动作：复位 outserv/inserv 或重启基站，记录前后状态。完成标准：服务恢复或升级二线
5. 收尾：Debug 回落 Normal operation，工单闭环注明。完成标准：无调试残留

判停点：

- PCAP/日志深读超出判读表 → 转二线依据 8AL91443ENAA 排障指南（p138 指针），不要现场猜包
- 排障结束忘了降日志级别 → Debug 禁常开（p160），影响程度书内未量化，一律回落
- WBM 改动"自己变回去" → PBX 下发覆盖（p77），临时改动要记录、长期变更回 OXE 做
- 命令无输出/报未知命令 → 核对是否在 mtcl 与对应节点（注册节点/安装节点）

输出契约：排障记录（现象/标志判读/处置）+ 日志或 PCAP 存档 + 级别还原确认。

## B — 边界

- LED 亮灯语义书内仅图示（p31/p139/p157-159/p221），无文字判读表——LED 细节不构成本卡内容
- Debug 常开的性能影响程度未量化（推断标注，needs-review nr-06）；四级之外无更细级别
- tcdump 需 root；深度过滤与分析方法在 8AL91443ENAA（书外）
- 实验 syslog 地址 192.168.1.9 与 NAS 凭据为实验口径；生产指向客户日志服务器
- 本卡不覆盖基站硬件维修与返修流程（书内无）
