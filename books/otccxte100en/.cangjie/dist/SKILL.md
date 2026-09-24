---
name: otcc-standard-starter
description: |
  OXE 内置呼叫中心（OTCC Standard/CCD）的入门级交付闭环：CCD 五级矩阵（pilot/队列/处理组）、CCS 班长台安装、路由与分配规则、座席班长体系、 对象参数调优、语音指南三路径、实时监控与 Excel 统计、多语言与双日历；另含班长特性、排队体验（EWT/518）、直接呼叫与紧急关闭、统计 pilot、实验环境链路五张路由卡。 适用于单站点入门交付、配置、排障与行为口径问答；话务建模、CCIVR/ACR/CCA、多站点等进阶域不在原书范围（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.otcc-standard-starter
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
# OmniTouch Contact Center Standard Edition — Starter (Participant's Guide, Edition 09) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- CCIVR 外部语音服务器、ACR 高级路由（语言技能/呼叫档案）、CCA 座席桌面、Soft Panel、ALE Connect 全渠道（原书只点名，指向 OTCC901 进阶教材）
- 话务建模与容量规划方法（TSP 调参只有"逐步调整+观察告警"口径，无话务量→队列数→座席数规划）
- 多站点 Multisite CCS、Excel 宏（ACDMacro）、录音第四法（Audio Station/VGTransfer 工具链）
- 生产中继申请、编号计划与 COS 体系设计（原书假设 RLAB 预置库现成）
- Rainbow 平台与 WebRTC 网关部署（本书 Rainbow 仅作座席形态，只有架构图无落地步骤）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 五级矩阵：一切呼叫流服从 pilot → 路由 → 队列 → 分配 → 处理组；配置的本质是连方向、定优先级、给默认行为
2. 默认全关：分配规则默认停用（须 OXE 侧激活）、所有方向默认关闭、末座席退出可禁——"配好了不通"先查激活与方向
3. 优先级统一 0-9（0 最高 9 最低），平局规则三类各异：路由看 EWT、资源选择看 LIT、呼叫选择看真实等待时间
4. 双控制台分工：OXE Web Admin 建 CCD 底层对象，CCS 管规则/座席/实时/统计/紧急关闭；CCS 无权创建 CCD 对象（只能建班长与分配规则）
5. 座席状态时序是排障共同语言：wrap-up 自动挂 pilot、手动挂 PG；pause 可接私人电话；退出 9 类型供统计；Blocked 是"下游无资源"的自动态
6. 实验口径红线：教材密码/号码/前缀/板位为 RLAB 实验值（法国目标库），生产必须替换并按当版文档核对

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 创建 CCD 矩阵；建 pilot/队列/处理组；acdsup 输出判读；队列与处理组类型选型；create CCD matrix pilot queue | references/capabilities/otcc-ccd-matrix-foundation.md | references/capabilities/otcc-routing-distribution-rules.md、references/capabilities/otcc-agent-supervisor-onboarding.md |
| 安装 CCS；声明 OXE 呼叫服务器；ccs.ini 参数核对；CCS 连不上 OXE；install CCsupervision | references/capabilities/otcc-ccs-installation.md | references/capabilities/otcc-ccd-matrix-foundation.md |
| 创建路由规则；创建激活分配规则；设置方向优先级；呼叫不通排查；activate distribution rule | references/capabilities/otcc-routing-distribution-rules.md | references/capabilities/otcc-ccd-matrix-foundation.md |
| 创建 ACD 话机与座席；创建班长；座席登录登出；座席形态选型；ACD agent logon | references/capabilities/otcc-agent-supervisor-onboarding.md | references/capabilities/otcc-ccd-matrix-foundation.md、references/capabilities/otcc-supervisor-features.md |
| 调 wrap-up 与 pause；配服务水平目标；PG 选项行为测试；队列饱和溢出参数；wrap-up timer service level | references/capabilities/otcc-object-tuning.md | references/capabilities/otcc-supervisor-features.md |
| 配置班长监听强插；pilot 通用转发；关闭处理组；配置事务码业务码；supervisor listening barge-in | references/capabilities/otcc-supervisor-features.md | references/capabilities/otcc-agent-supervisor-onboarding.md、references/capabilities/otcc-object-tuning.md |
| 话机录制语音指南；导入 .wav 录音；配置座席欢迎指南；指南编号与装板；voice guide recording wav | references/capabilities/otcc-voice-guides.md | references/capabilities/otcc-queue-experience.md、references/capabilities/otcc-multilanguage-calendar.md |
| 搭建实时监控视图；配置告警阈值；生成 Excel 报表；配置预编译日报；navigator alarms excel report | references/capabilities/otcc-monitoring-statistics.md | references/capabilities/otcc-object-tuning.md |
| 部署多语言语音指南；按语言分流来话；配置 pilot 日历；配置分配日历与特殊日；multi-language calendar time slot | references/capabilities/otcc-multilanguage-calendar.md | references/capabilities/otcc-voice-guides.md |
| 按等待时长播报；配置 EWT 表；部署排队位置播报；排队听感设计；EWT queue position announcement | references/capabilities/otcc-queue-experience.md | — |
| 部署 CCD 直接呼叫；配置私人号码；判定 CCD 与私人呼叫；实施紧急关闭；direct call emergency closure | references/capabilities/otcc-direct-calls-emergency.md | — |
| 创建统计型 pilot；配置 Call Tag；分业务统计与问候；统计 pilot 排障；statistic pilot call tag | references/capabilities/otcc-statistic-pilot.md | — |
| 收尾实验 POD 配置；打通公网外呼；开通 ABC-F 内呼链路；RLAB 环境排障；lab pod abc-f hybrid link | references/capabilities/otcc-lab-connectivity.md | — |

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

- 用户问 CCIVR/ACR/CCA/Soft Panel/ALE Connect 细节 → 声明书外边界，指向 OTCC901 与 Feature list，不以本包内容猜测
- 用户要话务量→队列数→座席数的规划方法 → 给 EWT/TSP 公式口径但明确声明建模在书外
- 生产环境拟套用教材密码/号码/前缀 → 判停并要求替换（实验口径红线）
- 现场界面与 R10.16/CCS 10.5 时代不符 → 按当版 OXE/CCS 文档核对，不凭本包记忆操作
- 需要 Multisite 多站点 CCS 或 Excel 宏自动化 → 边界外，指向 OTCC901
