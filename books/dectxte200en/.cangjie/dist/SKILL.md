---
name: dect-solutions
description: |
  OmniPCX Enterprise 的 DECT 无绳移动交付与运营支持：三条产品线（8379 IBS / 8378 IP-xBS / 8328 SIP-DECT）选型、PARI/PLI/PARK 标识体系与 multi-PARI 适配、IP-xBS 部署、空中同步/外部同步与多站点组网、手机注册与自动重注册、固件双轨升级、混合模式迁移、日常维护排障。适用于 OXE DECT 的配置、选型、组网与排障问答；无线工程设计方法论与生产安全基线不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.dect-solutions
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# DECT Solutions (Participant's Guide, Edition 12) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 无线覆盖设计方法论（传播模型、天线选型、勘测判定流程）——原书外置到《DECT and IP-DECT Engineering Rules》8AL90874USAA
- 深度排障（PCAP 分析方法、日志深读）——外置到 8378 IP-xBS Troubleshooting Guide 8AL91443ENAA
- 生产安全基线（WBM/AC 密钥治理策略、证书管理）与 DHCP/初始配置通用细节——书内只有字段名，细节在 8AL91047ENAD
- RLAB 培训环境搭建、话务建模（Erlang）、OXE 系统级非 DECT 配置（SIP 中继、编号计划、板卡硬件规则）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 选型先于配置：IBS（TDM、1 PARI/256 台/无加密）、IP-xBS（全 IP、8 PARI/2032 台、每站 11 通话+11 IP 中继）、SIP-DECT（SIP 语义、20 手机/站、区间无切换）三条线能力边界决定方案
2. 一切标识围绕 PARI 体系：PARI+RPN=RFPI、PARK=PLI+PARI 注册时写入手机、IPUI 认机；multi-PARI 靠降 PLI 做缩位匹配（混合模式必须适配 PLI，p227 WARNING）
3. 同步是 handover 的生命线：站间 RSSI≥-80dBm、同步树最深 24 级、外部同步 Sync Master 禁载通信且 Backup 强制、>2 PARI 需 Sync Highway；handover 只发生在同 Site 且同一 Data Sync Primary 之下
4. 开通路径标准化：全局参数（PARI/PLI/AC/安全级别）→ DHCP（vendor class alcatel.ipxbs.0）→ 注册（全网单节点开关）→ dectview 核验；换故障基站走手动注册保 RPN
5. 实验环境口径：教材网段、密码、AC、PARI 值仅限实验；引用容量与门槛数字必须带前提（-70/-60/-80dBm、11 通话+11 中继、254 台每 PARI/2032 台每节点）

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 规划 DECT PARI 和 PLI；算 PARK 号码；混合模式 PLI 怎么取值；手机锁定不上哪个系统；PARI PLI PARK 规划；multi PARI configuration | references/capabilities/dect-pari-identifier.md | references/capabilities/dect-mixed-mode.md、references/capabilities/dect-auto-reregistration.md |
| 选择 DECT 产品线；对比 IBS 和 IP-xBS；SIP-DECT 适不适合；DECT 拓扑怎么选；DECT product selection；DECT topology | references/capabilities/dect-product-selection.md | references/capabilities/dect-ipxbs-deployment.md、references/capabilities/dect-sip-dect.md |
| 部署 IP-xBS 基站；基站注册不上；更换故障基站；IP-xBS DHCP 配置；deploy 8378 IP-xBS；replace base station | references/capabilities/dect-ipxbs-deployment.md | references/capabilities/dect-pari-identifier.md、references/capabilities/dect-firmware-management.md |
| 配置空中同步；配置外部同步链路；Sync Master 坏了怎么办；多站点 Site 划分；DECT synchronization；external handover | references/capabilities/dect-xbs-sync-topology.md | references/capabilities/dect-mixed-mode.md |
| 创建 DECT 用户；注册 DECT 手机；注销更换手机；GAP 和 GAP+ 区别；register DECT handset；dectinston | references/capabilities/dect-handset-registration.md | references/capabilities/dect-auto-reregistration.md |
| 部署混合 DECT；IBS 加 xBS 同站；混合模式手机漫游失败；Mixed 模式配置；mixed DECT infrastructure | references/capabilities/dect-mixed-mode.md | references/capabilities/dect-pari-identifier.md、references/capabilities/dect-xbs-sync-topology.md |
| 批量迁移 DECT 手机；PARI 变更手机怎么办；dectinston -update 用法；重注册失败清单；automatic re-registration；forceUpdate | references/capabilities/dect-auto-reregistration.md | — |
| 升级基站固件；手机固件空中升级；downstat 命令用法；固件升级窗口规划；firmware upgrade；downstat m | references/capabilities/dect-firmware-management.md | references/capabilities/dect-ipxbs-deployment.md |
| 查看基站状态；收集基站日志；DECT 排障初判；抓包取证；DECT troubleshooting；dectview | references/capabilities/dect-maintenance-troubleshooting.md | references/capabilities/dect-ipxbs-deployment.md |
| 做覆盖勘测；RSSI 门槛是多少；开手机勘测模式；覆盖验收标准；site survey；RSSI | references/capabilities/dect-radio-survey.md | references/capabilities/dect-product-selection.md |
| 部署 IBS 基站；UA 板卡怎么选；IBS 布线距离；IBS 状态判读；deploy 8379 IBS | references/capabilities/dect-ibs-deployment.md | references/capabilities/dect-mixed-mode.md |
| 部署 8328 SIP-DECT；8328 拿不到 IP；双小区谁是主站；8328 手机注册；SIP-DECT deployment；dual cell | references/capabilities/dect-sip-dect.md | references/capabilities/dect-handset-registration.md |

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

- 用户要"设计 DECT 无线网络"（布点/天线/容量建模）→ 明确指向 8AL90874USAA，不以教材页数代替工程规则
- 遗留机型（8212/8232/8242）维修、ATEX 部署细节、8328 双小区合计容量 → 书内无依据，如实声明书外（推断口径需标注）
- 引用容量数字被追问话务前提 → 按"11 通话+切换余量"口径说明，不做 Erlang 承诺
- 版本恰在边界（OXE R12.2、基站固件 v73b0003、重注册机型版本表 p252）→ 按书中版本表如实回答并建议先升固件
