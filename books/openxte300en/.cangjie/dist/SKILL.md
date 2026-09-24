---
name: opentouch-starter
description: |
  OpenTouch Suite for MLE（OTMS/OTMS-v，含 OXE + OpenTouch + OmniVista 8770）的全流程交付与运维支持：SOT 自动化装机、Post-installation wizard 初始化、FlexLM 许可落地与核查、 8770 双向节点声明与 OXE SIP 打通、prior management 号码路由、档案与用户供给（含 WPC 批量）、本地存储语音邮箱与 IMAP/通知/公告、证书部署、OTC PC 客户端与多终端、监督组，以及维护、备份与 rehosting（TC2149 矩阵）。 适用于 OpenTouch Starter 站点的安装、配置、集成、排障与交付问答；容量与话务设计、OXE spatial redundancy 操作、SBC 安装、UM/Nomadic/OTBE 不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.opentouch-starter
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# OpenTouch — OpenTouch Suite for MLE — Solution Overview / Starter (Participant's Guide) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 容量与话务建模、虚机规格 sizing（原书外置到 Delivery note / Features list / Product limits）
- OXE spatial redundancy 的 SIP 与外部语音邮件网关操作（TC1652）
- SBC 与反向代理安装（TC2257/TC2639）与 UM 语音邮件、Nomadic、OTBE、VPN-less 会议地址（另见专项培训/另一手册）
- Teams/Skype for Business 深度集成与 OTC Mobile 移动端（原书仅一笔带过）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 交付主线层层递进：装机 → 向导初始化 → 许可闸门 → 双向集成声明 → 号码路由 → 业务供给 → 安全与客户端 → 运维闭环（p50-51 主步骤链）
2. 许可自成一体：FlexLM 校验锚定物（物理机 ALUID、虚拟机加密狗）；OXE 容量仍以本地 .swk 为准；向导许可页 OK 只代表文件在，不代表内容有效（p130-132, p159, p101）
3. 三台服务器靠互挂成网：先 OXE 前置，再 8770 建树，然后声明 OT（bics.conf 三账号），最后 OT 侧挂 OXE；DNS 正反向解析是硬前提（p186-203, p93）
4. 客户端是许可驱动形态：OTC PC 与 OTC PC One 同一二进制，Desktop 许可决定模式；软电话路线 Desktop 勾、Nomadic SIP 不勾（p433, p474）
5. 实验环境口径：教材密码、账号、IP 与号码仅限实验（公开教学值）；rehosting 配错即死锁无回退，一切以 TC2149 矩阵为准（p16, p565-567, p579-602）

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 完成 OTMS 初始化向导；从备份恢复重装 OTMS；向导口令与 DNS 有什么要求；post-installation wizard | references/capabilities/ots-post-installation-wizard.md | references/capabilities/ots-license-flexlm.md、references/capabilities/ots-node-declaration-sip.md |
| 安装许可文件；许可核查与排障；部署外部 FlexLM；内部切外部 FlexLM | references/capabilities/ots-license-flexlm.md | references/capabilities/ots-post-installation-wizard.md、references/capabilities/ots-maintenance-rehosting.md |
| 在 8770 声明 OXE；在 8770 声明 OpenTouch；配置 OXE SIP 打通；OT 告警对接 8770 | references/capabilities/ots-node-declaration-sip.md | references/capabilities/ots-prior-management.md、references/capabilities/ots-post-installation-wizard.md |
| 配置号码段与归属；配置前缀与拨号规则；修复目录检索陈旧；配置会议桥与 DAS 规则 | references/capabilities/ots-prior-management.md | references/capabilities/ots-node-declaration-sip.md |
| 创建 Connection 用户；创建 OXE/OT 档案；批量供给用户（WPC）；用户口令策略 | references/capabilities/ots-users-profiles.md | references/capabilities/ots-voice-mail.md、references/capabilities/ots-node-declaration-sip.md |
| 创建语音邮箱；配置语音邮箱档案；配置 IMAP 收取语音留言；配置 SMTP/SMS 通知与公告 | references/capabilities/ots-voice-mail.md | references/capabilities/ots-users-profiles.md |
| 安装交付 OTC PC；排查 OTC PC One 免费模式；配置电脑软电话；配置多终端副站 | references/capabilities/ots-clients-multi-devices.md | references/capabilities/ots-users-profiles.md、references/capabilities/ots-supervision-groups.md |
| 收集日志与系统核查；配置备份与恢复；执行 rehosting 改 IP 主机名；rehosting 后收尾三件套 | references/capabilities/ots-maintenance-rehosting.md | references/capabilities/ots-license-flexlm.md |
| 用 SOT 部署 OTMS；SOT 媒体与项目管理；手动安装 OTMS；OVF/OVA 导入 ESXi | references/capabilities/ots-sot-installation.md | — |
| 切换自签证书；用 Windows CA 签发证书；评估 security off 风险；排查证书不生效 | references/capabilities/ots-certificates.md | — |
| 创建监督组；配置进出组前缀；配置监督代接；评估监督覆盖边界 | references/capabilities/ots-supervision-groups.md | — |
| 搭建实验 POD；连接 OT/OXE/8770；SUSE 图形界面操作；验证模拟外呼 | references/capabilities/ots-lab-connections.md | — |

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

- 需容量与话务设计或虚机规格 → 明确指向 Delivery note / Features list / Product limits，不以 5000 用户一条数字搪塞
- OXE 为 spatial redundancy 站点 → SIP 字段与外部语音邮件网关转 TC1652，不照抄单机实验步骤
- rehosting 前置不满足（参数未全对齐或无备份）→ 判停拒绝执行：配错即死锁且无回退（p565）
- 涉及 RLAB/ITSP1 实验环境搭建 → 参考 book/overview 实验环境区背景，实验值不虚构为生产配置
- UM 语音邮件、Nomadic、OTBE、Teams 深度集成 → 声明属书外专项培训/手册，不硬答
