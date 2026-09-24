---
name: oxo-connect-call-center
description: |
  OXO Connect 呼叫中心（ACD）交付与运营支持：从 OMC 安装、基础 ACD 搭建、 呼入场景排障、特征化路由、队列与搜索模式调优，到坐席签入签出、多秘书方案、 Supervisor/Agent/Statistics 三件套部署与语音定制。适用于 OXO Connect R6.x 时代的 配置、排障与方案落地问答；生产化安全加固与话务容量规划不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.oxo-connect-call-center
  cangjie.capability-count: 15
  cangjie.entrypoint-count: 1
---
# OXO Connect 呼叫中心 (Participant's Guide, Edition 07) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 生产环境安全加固、SBC/真实中继对接、防火墙策略（原书仅 RLAB 模拟器口径）
- 话务量分析与坐席/端口容量规划方法论（原书仅给许可包与上限）
- 非 OXO Connect 平台的呼叫中心（OmniPCX Enterprise ACD、OpenTouch Contact Center 等另属其他教材）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 一切呼入行为先归入六场景之一（空闲/全忙/队满/端口忙/全员登出/组关闭），再谈配置与排障
2. 配置分两层：ACD Setup 向导一次成型，ACD Services 菜单精细调整；改完向导必须重启 ACD 引擎才生效
3. 呼叫特征化按 CLI(左→右)+DDI(右→左) 三级优先匹配，路由表从最特殊填到最一般
4. 队列长度 = ceil(On duty 坐席数 × 话务因子 K)，上限 16；坐席状态与登录状态是两类独立排障维度
5. 实验环境口径：教材密码（pbxk1064/Acdc1064）与网段仅限实验，生产必须替换并做安全加固

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 从零搭建 OXO ACD；新建呼叫中心组；ACD 初始配置；configure ACD on OXO Connect | references/capabilities/oxo-acd-basic-setup.md | references/capabilities/oxo-acd-call-scenarios.md、references/capabilities/oxo-acd-routing.md、references/capabilities/oxo-acd-login-status.md |
| 来电被挂断/排队/没铃声；ACD 呼入行为异常；caller behavior troubleshooting；为什么电话直接被劝退 | references/capabilities/oxo-acd-call-scenarios.md | references/capabilities/oxo-acd-queue.md、references/capabilities/oxo-acd-login-status.md、references/capabilities/oxo-acd-schedule-calendar.md |
| 按客户/国家分流来电；配置 Smart Call Routing；大客户专线分组；call routing by CLI DDI | references/capabilities/oxo-acd-routing.md | references/capabilities/oxo-acd-call-scenarios.md |
| 队列长度怎么设；排队等待时间播报；queue length；estimated waiting time；队满了还来电 | references/capabilities/oxo-acd-queue.md | references/capabilities/oxo-acd-login-status.md、references/capabilities/oxo-acd-search-noanswer.md、references/capabilities/oxo-acd-call-scenarios.md |
| 话务怎么在坐席间分配；坐席被自动签出；ringing duration；无应答自动移除；search mode 选哪种 | references/capabilities/oxo-acd-search-noanswer.md | references/capabilities/oxo-acd-login-status.md、references/capabilities/oxo-acd-queue.md |
| 坐席怎么登录/签出；登录了却不接电话；话机显示 1:01；ACD tab；free seating；agent login logout | references/capabilities/oxo-acd-login-status.md | references/capabilities/oxo-supervisor-app.md、references/capabilities/oxo-acd-call-scenarios.md |
| 多经理共享秘书；秘书台显示老板名字；multi secretary；领导秘书分机方案 | references/capabilities/oxo-multi-secretary.md | references/capabilities/oxo-acd-basic-setup.md、references/capabilities/oxo-acd-routing.md、references/capabilities/oxo-acd-schedule-calendar.md、references/capabilities/oxo-acd-voice-prompts.md |
| 装 OMC；连不上 OXO；安全告警反复弹；OMC installation；pbxk1064 | references/capabilities/oxo-omc-first-connect.md | references/capabilities/oxo-ip-replan.md、references/capabilities/oxo-acd-basic-setup.md |
| 改 OXO IP；换网段；DHCP 地址池；change IP settings | references/capabilities/oxo-ip-replan.md | references/capabilities/oxo-omc-first-connect.md |
| 设置营业时间；节假日关闭；exceptional days；opening hours | references/capabilities/oxo-acd-schedule-calendar.md | references/capabilities/oxo-acd-call-scenarios.md |
| 装班长监控台；实时看坐席状态；坐席显示忙却不接；supervisor application；activity rate | references/capabilities/oxo-supervisor-app.md | references/capabilities/oxo-acd-login-status.md、references/capabilities/oxo-statistics-app.md、references/capabilities/oxo-agent-app.md |
| 装坐席软件；来电弹屏；通话分类打标；agent application；screen popup | references/capabilities/oxo-agent-app.md | references/capabilities/oxo-dtmf-client-popup.md、references/capabilities/oxo-statistics-app.md、references/capabilities/oxo-supervisor-app.md |
| 看来话量报表；坐席统计；导出统计；statistics application；S1 S2 threshold | references/capabilities/oxo-statistics-app.md | references/capabilities/oxo-supervisor-app.md |
| 客户来电弹资料；输码识别客户；DTMF client code；customer code popup | references/capabilities/oxo-dtmf-client-popup.md | references/capabilities/oxo-agent-app.md、references/capabilities/oxo-acd-voice-prompts.md |
| 定制欢迎语；换提示音；voice prompts；101.wav；录音上传 | references/capabilities/oxo-acd-voice-prompts.md | references/capabilities/oxo-acd-call-scenarios.md、references/capabilities/oxo-acd-queue.md、references/capabilities/oxo-dtmf-client-popup.md |

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

- 需求超出 OXO Connect 平台范围（如 32 坐席以上、跨站点容灾）→ 转对应产品线教材或 ALE 预销售支持
- 涉及 RLAB/SIP 模拟器环境搭建细节 → 参考 book/overview 环境区，不虚构配置步骤
- 用户问的是生产安全/加固 → 明确声明超出原书范围，避免以实验口径误导
