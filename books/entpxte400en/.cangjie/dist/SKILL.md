---
name: oxe-starter
description: |
  OmniPCX Enterprise（OXE）基础开局与日常维护的准入闭环：安全登录与密码治理、系统启停、CS 双地址与内部防火墙、NTP/chrony 对时、空库与 OPS 许可、 三类媒体网关上架（GD4/OMS/XL）、用户终端开通（IP 话机/IPDSP/TDM/Profile/DHCP）、编号计划与 COS、呼叫处理业务域（语音指南/话务台/Entity/计时器）、 公共 SIP 中继全链路与弹性、外呼闭锁与紧急呼叫、备份恢复与维护排障、T0/T2 传统中继与 UMC 云管理。适用于单机（stand-alone）口径的开局、配置、 拨测与一线排障问答；高可用组网、Cloud Connect 深度、运营商生产参数不在原书范围（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.oxe-starter
  cangjie.capability-count: 14
  cangjie.entrypoint-count: 1
---
# OmniPCX Enterprise - Starter (Participant's Guide, Edition 12) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- CS Duplication 空间冗余、PCS、多节点组网（原书明示 Advanced 课程）
- Cloud Connect/RTR 深度与 FlexLM 服务器搭建（ENTPXTE402 与 CPU Loading 课程）
- SIP 运营商生产参数与紧急显示管理（TC2005 与运营商文档）；4645 防盗打加固（SA0046/TC1774）
- 话机硬件规格目录、Crystal 硬件细节、产品限额全集（MyPortal 文档组）；SBC/QoS/中继深调

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 准入链顺序即实验顺序：登录加固 → 启停 → IP/防火墙 → 时间 → 空库与许可，前一步是后一步的前提；跳章必须自检依赖
2. 双 IP 地址体系：物理接口地址永远可达（含话务停止），Role MAIN 地址仅话务运行时生效——设备与外部应用统一指向 Role 地址；停话务后传文件必须用物理地址
3. 安全基线 N3 起默认全关：iptables 默认 DROP 入站/转发，互通全靠可信主机白名单；"Allow SSH for all" 只是开局便门，配完必须 Deny 收口
4. 库与许可是一对：空库创建连 OPS 一起抹掉，"停话务 → 建库 → 恢复 OPS → 起话务"顺序不可乱；软件每 5 天自查许可，CPU-ID 不一致给 30 天宽限再进降级三阶段
5. 业务路由固定流水线：ARS 前缀 → 鉴别符 → ARS 表 → 中继组 → NPD → DID 翻译器 → 外部网关；闭锁 = Area × Public COS × 实体状态（默认 Night 态）的交点

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 登录 OXE；修改系统账户密码；配置密码策略与账户锁定；启用 client 账户；OXE SSH login | references/capabilities/ents-first-login-hardening.md | references/capabilities/ents-cs-network-firewall.md、references/capabilities/ents-system-start-stop.md |
| 启动或停止话务应用；重启或停机；管理 autostart；查系统运行状态 | references/capabilities/ents-system-start-stop.md | — |
| 配置 Call Server IP 地址；配置 Role 地址；配置内部防火墙与可信主机；OXE 连不上排查；netadmin firewall | references/capabilities/ents-cs-network-firewall.md | references/capabilities/ents-first-login-hardening.md |
| 部署 NTP 时间同步；瞬时校时；配置时区；chrony 巡检 | references/capabilities/ents-time-sync.md | references/capabilities/ents-cs-network-firewall.md |
| 创建空数据库；恢复或备份 OPS 许可；对接 FlexLM；处理降级模式告警；spadmin 巡检 | references/capabilities/ents-db-license.md | references/capabilities/ents-media-gateway-deployment.md、references/capabilities/ents-backup-maintenance.md |
| 上架 GD4 硬件网关；部署 OMS 虚拟媒体网关；上架 XL 机架；配置压缩器与子板；板卡不入服排查 | references/capabilities/ents-media-gateway-deployment.md | references/capabilities/ents-user-terminal-provisioning.md |
| 创建用户与开通话机；IP 话机静态或动态开通；部署 IPDSP 软话机；User Profile 批量建户；配置 CS 内部 DHCP；话机换机与日志收集 | references/capabilities/ents-user-terminal-provisioning.md | references/capabilities/ents-numbering-cos.md |
| 规划或维护编号计划；创建前缀与后缀；管理 Phone Features COS；配置 Connection/Transfer 矩阵 | references/capabilities/ents-numbering-cos.md | references/capabilities/ents-call-processing.md |
| 部署静态语音指南与 MOH；部署话务台与 4059EE；管理 Entity 与 CDT；调优呼叫分配计时器 | references/capabilities/ents-call-processing.md | references/capabilities/ents-voicemail-4645.md、references/capabilities/ents-barring-emergency.md |
| 部署 4645 语音邮件；分配与管理信箱；配置邮件通知；声明 SMTP 服务器 | references/capabilities/ents-voicemail-4645.md | — |
| 开通公共 SIP 中继；配置 ARS 与鉴别符；配置 NPD 与 DID 翻译器；配置回叫翻译器；SIP 网关备份与负载均衡 | references/capabilities/ents-sip-trunk.md | references/capabilities/ents-numbering-cos.md、references/capabilities/ents-barring-emergency.md |
| 配置外呼闭锁；管理 Area 与 Public COS；配置紧急呼叫通知；配置 Location ID 与 P-ANI | references/capabilities/ents-barring-emergency.md | references/capabilities/ents-sip-trunk.md |
| 备份数据库；恢复数据库；抓包与日志排障；事件查询与释义；生成支持材料 | references/capabilities/ents-backup-maintenance.md | references/capabilities/ents-db-license.md |
| 开通 T0 中继组；开通 T2 中继组；评估或使用 UMC 云管理；UMC 向导建 SIP 中继 | references/capabilities/ents-legacy-trunks-umc.md | references/capabilities/ents-sip-trunk.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 需要空间冗余、多节点组网或 PCS 方案 → 超出 Starter 单机口径，转 Advanced 课程口径并显式说明
- 需要具体运营商 SIP/ISDN 参数（号段/信令变体/CLIR/紧急显示）→ 指向 TC2005、SA0046/TC1774 与运营商文档，不照抄实验值
- 涉及 RLAB/ITSP1 实验环境值（密码/IP/账号/号段）→ 按 book/overview 实验口径声明处理，不当作生产配置
- 用户要求把教材密码照搬上生产 → 拒绝，给出首登加固的改密与策略收紧步骤
