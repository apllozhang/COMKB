---
name: oxo-connect-starter
description: |
  OXO Connect（OCE IPBox 与 PowerCPU EE 平台）从开箱到投产的端到端交付：交付前数据采集、FTR 上云与 OMC Standard 双路线开通、IP 规划、终端开通（IP 话机/DECT）、编号计划与组、用户功能与语音信箱、公共 SIP 中继、呼入分发与呼出闭锁、备份升级复位、安全基线，以及 Rainbow 混合云接入速览。 适用于 OXO 本体交付的配置、排障与方案问答；Rainbow 云侧运营深入内容与 OXO ACD 呼叫中心不在本 bundle（见 out_of_scope 与姊妹技能）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.oxo-connect-starter
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# OXO Connect Starter (Participant's Guide, Edition 16) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- Rainbow 云侧公司/订阅/成员运营、OCE-FE 多场景开局、Teams 集成、SR 支持体系（bundle.rainbow-oxo-connect 承载，本 bundle 仅速览）
- OXO ACD 呼叫中心排队坐席体系（bundle.oxo-connect-call-center 承载）
- 生产 SIP 运营商选型与加密要求（TC1284）、安全加固全文（TC1143）、TURN 与防火墙白名单（cookbook）
- RLAB 实验环境与 ITSP1 模拟器搭建（教学基础设施，仅 Boundary 背景）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 交付从数据采集开始：IP 规划、七账户密码表、三位编号计划（100-199/主中继组 0/hunt 500-525/DDI 41100-41199）先定稿后动配置
2. 开通两条路：Cloud Connect（FTR 自动注册、许可自动下载、Fleet Dashboard）与 Standard（OMC 连 192.168.92.246、导入 .msl+.csl 双钥匙）；pbxk1064 仅首连一次
3. 出局控制是矩阵不是清单：Traffic sharing 与 Barring 两类链路类别 × 6 张闭锁表 × digit counter，用户 COS × 中继组 COS 求交判定
4. 呼入靠话务台组+时段表+Normal/Restricted 双 DDI 计划；组恒并行；用户默认不跟随时段，要逐话机关 Inhibition Time-ranges
5. 维护三板斧语义分明：备份（OCE SD 卡 AES 256、恢复仅同主版本）、双版本+Swap 可回退、Warm/Cold/Factory 递进删除
6. 实验环境口径：教材全部密码、账号、网段仅限实验；生产化依据外置 TC1143/TC1284/TC1994/TC2479/cookbook 五份文档

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 做 OXO 交付前数据采集；定编号计划与 IP 规划；准备安装密码表；data collection checklist | references/capabilities/oxos-data-collection.md | references/capabilities/oxos-commissioning.md、references/capabilities/oxos-numbering-groups.md |
| OCE FTR 注册 Cloud Connect；安装 OMC 并首次连接；修改 OXO IP 规划；冷复位后重建基础配置；FTR first time registration | references/capabilities/oxos-commissioning.md | references/capabilities/oxos-terminals.md、references/capabilities/oxos-data-collection.md |
| 开通 IP 话机；话机拿不到地址；部署 IP-DECT 基站；注册 8328/8214 话机；put in service IP phone | references/capabilities/oxos-terminals.md | references/capabilities/oxos-commissioning.md |
| 配置编号计划；建新前缀段报冲突；建 hunt/代接/广播组；建经理秘书组；numbering plan configuration | references/capabilities/oxos-numbering-groups.md | references/capabilities/oxos-user-features.md |
| 配用户可编程键；配动态路由与前转；前转不生效排障；管理语音信箱；configure dynamic routing | references/capabilities/oxos-user-features.md | references/capabilities/oxos-numbering-groups.md |
| 配置公共 SIP 网关；SIP 注册失败排障；导入运营商 Profile；补短号与紧急号码路由；configure SIP trunk | references/capabilities/oxos-sip-trunk.md | references/capabilities/oxos-incoming-barring.md |
| 配置呼入日夜分发；配置时段表与预公告；控制用户出局权限；配置国际闭锁；call barring management | references/capabilities/oxos-incoming-barring.md | references/capabilities/oxos-sip-trunk.md |
| 建立备份制度；恢复数据库；执行软件升级与回退；选择复位方式；backup restore software download | references/capabilities/oxos-maintenance.md | references/capabilities/oxos-commissioning.md |
| 选硬件平台形态；估算话音并发容量；评估机柜扩展条件；OXO hardware family | references/capabilities/oxos-hardware-platform.md | — |
| 上传欢迎与预公告消息；配置保持音乐；音频格式转换核查；music on hold download | references/capabilities/oxos-audio-messages.md | — |
| 制定密码策略；清理默认口令；处置疑似盗打；phreaking security baseline | references/capabilities/oxos-security.md | — |
| 把 OXO 接入 Rainbow；Rainbow 连接排障；网关拓扑与容量速查；connect OXO to Rainbow | references/capabilities/oxos-rainbow-integration.md | references/capabilities/oxos-commissioning.md |

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

- 用户数超 300 或需机柜扩展以外的平台能力 → 超出 OXO 产品定位，转其他产品线方案
- 需要生产网络数值、TC 全文或 cookbook 操作步骤 → 明确指向外部权威文档，不以实验口径搪塞
- 涉及 Rainbow 云侧深度运营或 ACD 排队业务 → 转对应姊妹技能，不越界作答
- 版本恰为 R4.0.020.002 的自动配置判定 → 按 needs-review nr-01 双口径如实说明，建议以更高版本执行
