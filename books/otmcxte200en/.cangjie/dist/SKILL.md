---
name: ot-message-center
description: |
  OpenTouch Message Center（OTMC，OXE 专用语音邮件服务器）Starter 级交付与运维支持：装机与 13 步站点配置、FlexLM 许可、8770 双向声明与同步、OXE 侧 SIP 对接、Connection 用户与语音邮箱交付、profile 批控与问候语、SMTP/SMS 通知、备份恢复与语音信箱统计，以及自助门户、IMAP 访问、企业广播三块增值能力。适用于 OTMC 的安装、纳管、对接、开箱到业务与日常运维问答；HA、UM 落地、硬件规格与容量规划不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.ot-message-center
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# OpenTouch Message Center Starter (Participant's Guide, Issue 08) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- HA 高可用配置（原书仅留指针，属后续课程；启用前置为副服务器 + 两台同时跑向导）
- 硬件/软件规格与产品上限、容量规划工具用法（feature list / product limits / OpenTouch Capacity Planning Tool）
- UM（Exchange/Lotus Domino/Gmail）落地与三方 VM 互通（VPIM）配置细节（原书仅支持性声明）
- AA 自动话务员配置、OXE 侧 DHCP 管理、Teams/SIP 话机生态对接

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. OTMC 是 OXE 专属外挂信箱：单服务器独立部署，消息存本地（LS）或统一消息（UM），访问通道三条——任意话机 TUI、8xx8/8088 话机 GUI、IMAP 邮件客户端
2. 配置管理唯一大脑是 OmniVista 8770：OXE/OTMC 双向声明并同步后一切经 8770；OTMC 自身 WBM 只做辅助（改密、问候语、IMAP 前端参数）
3. 上线顺序刚性：OS → core → 13 步向导 → 8770 双向声明同步 → OXE SIP 对接（单 trunk、端口 5040）→ 用户与信箱；信箱创建必须挂 profile
4. 外部设施依赖明确：许可走 flex-lm（.ice + ALUID/dongle，向导 OK 不校验有效性）；通知走外部 SMTP（无认证无 TLS、经 VPIM 路由）；DNS 必须前向+反向解析七类 FQDN
5. 实验口径纪律：教材密码/账号/网段仅限实验；15000/5000 为标注口径，生产规格以 feature list / product limits 为准

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 安装 OTMC 服务器；post-installation wizard 配置；站点 DNS 与账户规则；OTMC 虚机创建；install OTMC server；OTMC site installation wizard | references/capabilities/otmsg-install-site-setup.md | references/capabilities/otmsg-license-management.md |
| 安装或更换 OTMC 许可；FlexLM 服务器部署；许可核验；dongle 绑定；install OTMC license file；verify flexlm license | references/capabilities/otmsg-license-management.md | references/capabilities/otmsg-install-site-setup.md |
| 声明 OXE 进 OmniVista 8770；声明 OTMC 节点；OTMC 拓扑声明 OXE；执行配置同步；declare OTMC in 8770；OTMC synchronization | references/capabilities/otmsg-declaration-sync.md | references/capabilities/otmsg-install-site-setup.md |
| 配置 OXE 与 OTMC 的 SIP 对接；建 SIP trunk group；声明 SIP external gateway；信箱呼叫通道排障；configure SIP trunk to OTMC | references/capabilities/otmsg-sip-trunk-provisioning.md | references/capabilities/otmsg-declaration-sync.md |
| 创建 Connection 用户并开通话机；话机许可核查；创建 OTMC 账户与语音邮箱；信箱业务验证；create voice mailbox；provision OTMC user | references/capabilities/otmsg-user-mailbox-provisioning.md | references/capabilities/otmsg-declaration-sync.md、references/capabilities/otmsg-mailbox-profiles.md |
| 定制语音邮箱 profile；信箱容量与保留期批控；管理用户问候语；zero-out 与 Answer only 配置；create voice mail profile；greetings management | references/capabilities/otmsg-mailbox-profiles.md | references/capabilities/otmsg-user-mailbox-provisioning.md |
| 配置 SMTP 邮件通知；配置 SMS 短信通知；通知排障；定制通知模板；configure voicemail notification；SMTP notification troubleshooting | references/capabilities/otmsg-notification-smtp-sms.md | references/capabilities/otmsg-user-mailbox-provisioning.md |
| 执行 OpenTouch 备份；执行恢复演练；启用语音信箱统计；统计文件排障；backup restore OTMC；voicemail statistics | references/capabilities/otmsg-backup-statistics.md | references/capabilities/otmsg-declaration-sync.md |
| OTMC 产品定位咨询；部署形态选型；组网边界评估；规模口径解释；OTMC deployment options | references/capabilities/otmsg-product-positioning.md | references/capabilities/otmsg-install-site-setup.md |
| 指导用户使用自助门户；网页收听语音留言；用户自助改设置；My Profile portal；MyMessaging playback | references/capabilities/otmsg-web-portal.md | references/capabilities/otmsg-user-mailbox-provisioning.md |
| 配置 IMAP 客户端收语音留言；IMAP4 Front End 安全匹配；IMAP 连接排障；configure IMAP voicemail access | references/capabilities/otmsg-imap-access.md | references/capabilities/otmsg-user-mailbox-provisioning.md、references/capabilities/otmsg-notification-smtp-sms.md |
| 部署企业广播；录制或更换公告；公告需求边界评估；general announcement setup | references/capabilities/otmsg-general-announcement.md | references/capabilities/otmsg-user-mailbox-provisioning.md |

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

- 需要生产网络规格或产品上限数值 → 指向 feature list / product limits 与 MyPortal 安装手册（otmc2.6.1），不以实验口径搪塞
- 空间冗余 SIP 网关或 8770 上 NFS 部署 → 指向 TC1652 / TC2024，不在本书找步骤
- 书内口径漂移类提问（OTMC 节点号 98/99、defaultVmLS 拼写、GA wav 路径、151/155 网段）→ 按 needs-review 双口径如实说明
- 问 AA 配置或 HA 部署 → 明确超出 Starter 范围，转对应课程/文档
