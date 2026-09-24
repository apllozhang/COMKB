---
name: rainbow-oxe-integration
description: |
  Rainbow 与 OmniPCX Enterprise 混合云集成交付与运营支持：云侧公司/订阅/成员体系、OXE 接入（DNS/代理 + PBXID/激活码）与接入排障、REX/Ghost Z/tandem 远程延伸路由、WebRTC 网关部署升级与 OXE 侧九件套配置、共享网关池与容量规划、4059EE 与 Rainbow 两套话务台、维护支持体系、Microsoft Teams 集成。适用于 Rainbow Hybrid on OXE 的配置、选型、排障与方案落地问答；生产化网络数值、TURN 部署与 Teams 租户策略不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.rainbow-oxe-integration
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
# Rainbow / OmniPCX Enterprise (Participant's Guide, Edition 12) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 端口/带宽/防火墙/TURN 具体数值（原书外置到 Rainbow Network Requirements PDF 与 VoIP calling Troubleshooting guide）
- 编号计划设计与话务建模方法论（TBE067 工具本体与流量模型假设在书外）
- RLAB 培训基础设施搭建细节（SIP 模拟器号码表等仅作背景，见 book/overview）
- Teams 租户侧策略（应用权限策略、紧急呼叫、Direct Routing 共存）与 CPaaS 开发（developers.openrainbow.com）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 混合云分工：OXE 保留呼叫控制与话音资源（trunk group/话务/留言/公号），Rainbow 提供协作、移动端与云服务；WebRTC 网关只建音频媒体关系，呼叫控制始终在 PBX
2. 云侧一切挂在 Company 体系下：BP 专属申报建 PBX 与开通付费订阅；成员一人不能属两家公司；电话服务必须 Business/Enterprise/Attendant 订阅
3. 接入与路由闭环按序推进：DNS/代理就绪（验证必须 nslookup/dig，URL ping 不算）→ PBXID+激活码接入 → 分机关联（RCC）→ REX/tandem 路由 → 网关解锁完整 VoIP；Essential 订阅只有 RCC 且不能改路由
4. REX/Ghost Z 是路由地基：每路 REX 并发呼叫占一个 Ghost Z，池大小即并发上限；Rainbow agent 按用户路由自动改写 REX——computer 路由写 BBB 前缀 17 位号走网关，mobile/home/other 走公共 trunk；tandem 两端必须 multi-line
5. 网关三重前提（成员 Business/Enterprise、OXE 12.1 MD4/12.2+、PBX 已接入且分机已关联）+ OXE 侧九件套（SIP TG/可信 IP/Rainbow type 网关/无压缩 IP 域/CDT/ARS/BBB 判别器/回调）缺一不通
6. 实验环境口径：教材密码、账号、网段与示例号码仅限实验；容量数字必须带口径（单网关 400 并发流，用户数与并发数是两个量纲）

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 创建 Rainbow 公司；开通 Rainbow 订阅；选择公司可见性与认证方式；管理员权责划分；create Rainbow company；Rainbow subscription plans | references/capabilities/rxe-company-subscription.md | references/capabilities/rxe-member-lifecycle.md |
| 配置 OXE DNS 与代理；OXE 接入 Rainbow；PBXID 在哪找；Rainbow 连接状态异常；connect OXE to Rainbow；rainbowagent troubleshooting | references/capabilities/rxe-agent-onboarding.md | references/capabilities/rxe-rcc-association.md |
| 创建 Rainbow 成员；邀请用户加入公司；删除恢复用户；批量导入成员；Rainbow user management | references/capabilities/rxe-member-lifecycle.md | references/capabilities/rxe-company-subscription.md |
| 选择 OXE 用户接入形态；配置远程延伸与 tandem；规划 Ghost Z 容量；排查路由振铃问题；remote extension configuration | references/capabilities/rxe-routing-rex.md | references/capabilities/rxe-webrtc-gateway-deployment.md、references/capabilities/rxe-oxe-gateway-config.md |
| 部署 WebRTC 网关；网关 VM 网络与 PBX 参数配置；网关配置核验与排障；升级 WebRTC 网关；deploy WebRTC gateway；mpcheck troubleshooting | references/capabilities/rxe-webrtc-gateway-deployment.md | references/capabilities/rxe-gateway-pool-sizing.md |
| 配置 OXE 侧网关配套；ARS 与判别器配置；回呼 Rainbow 分机；网关 VoIP 测试；OXE SIP configuration for WebRTC gateway | references/capabilities/rxe-oxe-gateway-config.md | references/capabilities/rxe-routing-rex.md |
| 选择网关池化架构；配置 ARS 溢出；估算网关容量与通道数；WebRTC gateway dimensioning | references/capabilities/rxe-gateway-pool-sizing.md | references/capabilities/rxe-webrtc-gateway-deployment.md、references/capabilities/rxe-network-readiness.md |
| Rainbow 集成 Teams；Teams 应用上架与权限同意；Teams 用户电话配置；Teams 在场同步；Rainbow for Teams integration | references/capabilities/rxe-teams-integration.md | references/capabilities/rxe-webrtc-gateway-deployment.md、references/capabilities/rxe-rcc-association.md |
| 关联 OXE 分机到 Rainbow；RCC 模式验证；Rainbow number | references/capabilities/rxe-rcc-association.md | references/capabilities/rxe-routing-rex.md |
| 交付 4059EE 话务台；部署 Rainbow 话务台；建监督组与互助组；attendant console setup | references/capabilities/rxe-attendant-consoles.md | references/capabilities/rxe-company-subscription.md |
| 查 Rainbow 日志；开 Rainbow 服务请求；云状态与维护预告 | references/capabilities/rxe-maintenance-support.md | references/capabilities/rxe-agent-onboarding.md |
| Rainbow 网络要求；连通性评估；端口放行 | references/capabilities/rxe-network-readiness.md | references/capabilities/rxe-agent-onboarding.md |
| 配置培训实验环境；核对 OXE Pod 基线；配置实验 DID 翻译 | references/capabilities/rxe-lab-pod-setup.md | references/capabilities/rxe-agent-onboarding.md |

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

- 需要生产网络数值或 TURN 部署位置选择 → 明确指向外部权威文档（Network Requirements PDF / VoIP calling Troubleshooting guide / TC2462），不以实验口径搪塞
- OXE 版本低于 12.1 MD4/12.2 → 网关功能不可部署，先升级再交付，不硬配
- 实验示例值（IP/账号/示例号码）与现场冲突 → 一律按现场重规划，实验值仅作格式参考
- 涉及 RLAB/SIP 模拟器环境复现 → 参考 book/overview 环境区背景，不虚构生产配置
