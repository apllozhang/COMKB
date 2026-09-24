---
name: rainbow-oxo-connect
description: |
  Rainbow 与 OXO Connect 混合云集成交付与运营支持：云侧公司/订阅/成员体系、 OXO 接入（PBXID+激活码）与接入排障、WebRTC 网关三拓扑选型与部署、 虚拟终端与 UTL 口径、话务台与监督组、Rainbow/Teams 集成、维护支持体系。适用于 Rainbow Hybrid on OXO Connect 的配置、选型、排障与方案落地问答； 生产化网络数值、编号计划与 Teams 租户策略不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.rainbow-oxo-connect
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# Rainbow OXO Connect (Participant's Guide, Edition 13) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 端口/带宽/防火墙/TURN 具体数值（原书外置到 Rainbow Network Requirements PDF 与安装指南）
- 编号计划与闭锁配置、话务建模方法论（原书明示安装员自做且不教）
- OCE-FE 多场景开局细节（必须按 MyPortal 最新版 Rainbow WebRTC cookbook）
- Teams 租户侧策略（应用权限策略、紧急呼叫、Direct Routing 共存）与非 OXO 平台（OXE 详节见 TC2462）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 混合云分工：PBX 保留呼叫控制，Rainbow 提供协作/移动/云服务；WebRTC 网关只建音频媒体关系（排障先分媒体面与呼控面）
2. 云侧一切挂在 Company 体系下：BP 专属建 PBX 与开付费订阅，成员须持 Business/Enterprise/Attendant 才有电话服务
3. 接入闭环按序推进：建公司开订阅 → OMC 首连 → PBXID 接入 → 分机关联（RCC）→ 网关解锁完整音频
4. 网关三拓扑功能等价：集成（R3.2+/20 通话/免 SIP trunk 许可）、OCE-FE（双端 ≥R4.0 MD/20）、外部 VM/NUC（50）；自动配置 R4.0.020.002 起且仅 Reseller 管理员可激活，终端/编号计划/闭锁仍归安装员
5. 实验环境口径：教材密码、账号与网段仅限实验；引用容量数字必须带话务前提（150 用户上限仅极低话务成立）

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 创建 Rainbow 公司；开通 Rainbow 订阅；选择公司可见性；配置 SSO/TOTP 认证；create Rainbow company；Rainbow subscription plans | references/capabilities/rbx-company-subscription.md | references/capabilities/rbx-member-lifecycle.md、references/capabilities/rbx-pbx-onboarding.md |
| 安装 OMC；OMC 连不上 OXO；修改 OXO IP 规划；install OMC first connection | references/capabilities/rbx-omc-onboarding.md | references/capabilities/rbx-pbx-onboarding.md |
| OXO 接入 Rainbow；PBXID 在哪找；Rainbow 连接状态异常；connect OXO to Rainbow | references/capabilities/rbx-pbx-onboarding.md | references/capabilities/rbx-rcc-association.md |
| 批量创建 Rainbow 用户；删除恢复用户；成员设置；Rainbow user management | references/capabilities/rbx-member-lifecycle.md | references/capabilities/rbx-rcc-association.md |
| 选择 WebRTC 网关拓扑；网关容量规划；网关通道数；WebRTC gateway dimensioning | references/capabilities/rbx-gateway-planning.md | references/capabilities/rbx-gateway-deployment.md、references/capabilities/rbx-network-readiness.md |
| 部署 WebRTC 网关；自动配置网关；配置 Twinset/Anydevice 终端；deploy WebRTC gateway | references/capabilities/rbx-gateway-deployment.md | references/capabilities/rbx-gateway-planning.md |
| 部署 Rainbow 话务台；建监督组；互助值班方案；attendant console setup | references/capabilities/rbx-attendant-supervision.md | references/capabilities/rbx-company-subscription.md |
| Rainbow 集成 Teams；Teams 应用上架与权限同意；Teams 在场同步；Rainbow for Teams integration | references/capabilities/rbx-teams-integration.md | references/capabilities/rbx-gateway-deployment.md、references/capabilities/rbx-rcc-association.md |
| 分配管理员权限；企业目录导入；信息频道创建 | references/capabilities/rbx-admin-tools.md | — |
| 关联 OXO 分机到 Rainbow；RCC 模式验证；Rainbow number | references/capabilities/rbx-rcc-association.md | — |
| 查 Rainbow 日志；开 Rainbow 服务请求；云状态与维护预告 | references/capabilities/rbx-maintenance-support.md | — |
| Rainbow 网络要求；连通性评估；端口放行 | references/capabilities/rbx-network-readiness.md | — |

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

- 用户数超 150 或需跨站点容灾 → 超出 OXO Rainbow VoIP 范围，转其他产品线方案
- 需要生产网络数值或 FE 开局操作步骤 → 明确指向外部权威文档（Network Requirements PDF / cookbook / TC2479），不以实验口径搪塞
- 涉及 RLAB/SIP 模拟器环境搭建 → 参考 book/overview 环境区背景，不虚构生产配置
- 版本恰为 R4.0.020.002 的自动配置判定 → 按 needs-review nr-01 双口径如实说明，建议以更高版本执行
