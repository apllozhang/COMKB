---
name: rainbow-hub
description: |
  Rainbow Hub 纯云话音交付与运营支持：公司/Voice 订阅云侧开户、Cloud PBX 声明与编号计划/号码/闭锁、成员五通道开户与话务配置、ALE 设备 zero-touch 与 DECT 部署、 设备维护与 Generic SIP 评估、呼叫组/话务台/欢迎服务与 IVR、多站点、分析与维护支持。适用于 Rainbow Hub（纯云，全托管 Cloud PBX）的开户、配置、排障与方案落地问答； 生产化网络数值、trunk 合同与 DID 紧急定位登记不在原书范围内（见 out_of_scope）。与混合云（RAINXTE001EN）的差异点：Voice 前缀订阅、Cloud PBX、BP 四项专属、zero-touch。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.rainbow-hub
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# Rainbow Hub (Participant's Guide, Edition 16) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 端口/带宽/防火墙全集与 TURN 数值（原书外置到 Network Requirements 文章与 PDF，书内仅两张局部摘录）
- trunk 合同、资费、号码携转、DID 地址登记（紧急定位）——BP/运营商侧
- 编号计划设计方法论、话务建模、提示音文案制作、DECT 无线勘测（原书不讲）
- Teams 集成、WebRTC 网关、OXO/OXE 接入（混合云产品线，属 RAINXTE001EN 语系）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 纯云架构：话务核心全托管云侧 Cloud PBX，客户侧无 PBX/SBC/VPN；一公司一 Cloud PBX、一 PBX 一条外部 SIP trunk
2. 云侧顺序硬约束：BP 建公司（时区强制）→ 至少一条 Voice Business/Enterprise 订阅 → 才能声明 Cloud PBX → 公网号码 → 终端 → 成员 → 功能
3. 权责切分：BP 独占 PBX 声明/付费订阅/终端声明/电话线四项；客户管理员做成员、组、欢迎服务等日常配置
4. 端侧三等供给：ALE 原生（zero-touch、集中管理）优先于入门档，第三方 Generic SIP 仅做补充（手工配置、无 RCC、ALE 不为大规模兜底）
5. 话务能力域参数化：组 50 人、队列溢出 10-900 秒、监督 5 页签/30 人、IVR 3 级无许可、录音存 2 个月——引用数字必须带口径
6. 实验环境口径：教材账号、密码、号段仅限实验；培训禁预付是实验规则，生产预付正常

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 创建 Rainbow Hub 公司；开通 Voice 订阅；选择公司可见性；配置 SSO/TOTP 认证；create Rainbow Hub company；Voice subscription plans | references/capabilities/hub-company-voice-subscription.md | references/capabilities/hub-member-telephony.md、references/capabilities/hub-cloud-pbx-provisioning.md |
| 声明 Cloud PBX；设计编号计划参数；分配公网号码与主号；配置呼叫闭锁；declare Cloud PBX；public numbers DDI | references/capabilities/hub-cloud-pbx-provisioning.md | references/capabilities/hub-company-voice-subscription.md |
| 批量创建成员；配置成员电话号码；管理个人例行程序；删除恢复成员；Rainbow user management | references/capabilities/hub-member-telephony.md | references/capabilities/hub-zero-touch-provisioning.md |
| 部署 Myriad 话机；批量导入设备；部署 DECT 基站与手持机；zero-touch provisioning | references/capabilities/hub-zero-touch-provisioning.md | references/capabilities/hub-device-maintenance.md、references/capabilities/hub-network-readiness.md |
| 采集话机日志；远程排障设备；评估接入第三方 SIP 话机；Generic SIP device onboarding | references/capabilities/hub-device-maintenance.md | references/capabilities/hub-maintenance-support.md |
| 创建呼叫组与等待队列；配置经理助理组；配置紧急号码与紧急组；管理通话录音；hunt group waiting queue | references/capabilities/hub-hunt-groups.md | references/capabilities/hub-attendant-supervision.md、references/capabilities/hub-welcome-service-ivr.md |
| 部署话务台；创建监督组；建 attendant group；attendant console setup | references/capabilities/hub-attendant-supervision.md | references/capabilities/hub-company-voice-subscription.md |
| 配置欢迎服务与营业时间路由；管理日历与语音提示；配置自动话务员菜单；custom music on hold | references/capabilities/hub-welcome-service-ivr.md | references/capabilities/hub-hunt-groups.md |
| 核查网络端口与防火墙；评估站点承载容量；估算话音带宽；Rainbow Pilot assessment | references/capabilities/hub-network-readiness.md | references/capabilities/hub-cloud-pbx-provisioning.md |
| 创建站点并分布用户；配置站点主号；配置站点音乐保持；multi-site configuration | references/capabilities/hub-multisite.md | references/capabilities/hub-cloud-pbx-provisioning.md |
| 获取月度话单 CDR；解读分析仪表盘；排查话音质量问题；CDR billing data | references/capabilities/hub-analytics.md | references/capabilities/hub-hunt-groups.md |
| 查平台状态与维护预告；收集用户日志与上报；开 Rainbow Hub 服务请求；Rainbow support SR | references/capabilities/hub-maintenance-support.md | references/capabilities/hub-device-maintenance.md |

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

- 客户要保留现有 PBX 接云（混合云形态）→ 转 Rainbow 混合云产品线（RAINXTE001EN 语系），不套用 Hub 开户流程
- 需要生产网络数值或 SR 流程细节 → 明确指向外部权威文档（Network Requirements / TBE099 / TBE127），不以实验口径搪塞
- 涉及 RLAB/MicroSIP 环境搭建 → 参考 book/overview 环境区背景，不虚构生产配置
- 成员配号订阅门槛出现 Voice Phone 争议 → 按 needs-review nr-01 双口径如实说明（p194 括注疑不完整，以 p66 四档口径为准）
- 紧急呼叫定位与合规诉求 → 声明责任链（BP 登记 DID 地址、运营商判 PSAP、Rainbow 不管），不替 BP/运营商承诺
