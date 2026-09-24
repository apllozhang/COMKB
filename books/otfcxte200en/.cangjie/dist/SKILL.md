---
name: ot-fax-center
description: |
  OpenTouch Fax Center（OTFC）纯软件 FoIP 传真服务器的首次交付与长期运维支持：宿主准备与软件安装、 First Time Setup Wizard 最小可用系统、许可两级控制、 与 OXE 的 SIP 话路对接（含 OXE 侧 MGR 七步与传真抓包）、SMTP/Exchange 邮件集成、用户/管理员/Profile 策略体系、目录集成与来传真路由、服务架构运维、备份升级与删除策略。 适用于 OTFC 的配置、选型、排障与方案落地问答；生产化端口全表、OXE 侧网关参数与 HA 部署不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.ot-fax-center
  cangjie.capability-count: 11
  cangjie.entrypoint-count: 1
---
# OpenTouch Fax Center - R9.2 Starter (Participant's Guide, Edition 04) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 端口使用表全表、服务器资源推荐数值、45 种格式明细、浏览器支持清单（原书外置 OTFC Features List）
- OXE 侧 SIP 网关参数细节（编码/号码变换/中继属性，原书明示参照 TC3048，本书只给 MGR 菜单骨架）
- XMFaultTolerance 高可用部署与演练、SIP/TLS 加密信令启用路径（书内零实操）
- 许可商务流程细节、GDPR/HIPAA 类合规条款解读、OmniVista 8770 侧报表配置

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 四级模型：System 管 Site，Site 是隔离的虚拟传真服务器（一份传真只属一个站点），用户恒以 SMTP 地址标识且必须绑定 Site+Profile 才能用系统
2. 交付主线四步：准备服务器（DNS 正反解/IIS 四角色服务/服务账号/Office 预初始化）→ 装软件（禁用 MS SMTP 释放 25 端口）→ FTW 十二项搭最小可用系统 → 许可去水印解锁通道
3. 两大外部集成缺一不可：OXE 侧 SIP 话路（OTFC UDP 5360 + MGR 七步 + TC3048）与邮件通道（SMTP 网关独占 25 + Exchange FAX 地址空间连接器）
4. 运维闭环：9 服务分有状态（复制）/无状态（负载均衡），xmsc -ra/-oa/-aa 一键启停；备份冷备不可 kill、恢复可 kill；升级五步法且数据库不在自动备份内
5. 实验环境口径：教材密码、IP、账号、号段仅限实验；端口全表、45 格式、sizing 一律外置 OTFC Features List

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 安装 OpenTouch Fax Center；跑 First Time Setup Wizard；准备传真服务器宿主；处理 OTFC 许可与水印；install OTFC fax server；First Time Setup Wizard steps | references/capabilities/otfax-installation-ftw.md | references/capabilities/otfax-sip-channel-integration.md |
| 配置 OTFC 与 OXE 的 SIP 对接；OXE 侧配传真 SIP 网关；传真话路不通排障；OXE 空间冗余配置；configure SIP between OTFC and OXE | references/capabilities/otfax-sip-channel-integration.md | references/capabilities/otfax-installation-ftw.md、references/capabilities/otfax-services-operations.md |
| 集成邮件系统发传真；Exchange 建 FAX 地址空间连接器；传真通知邮件收不到；传真邮件寻址格式；configure Exchange send connector for fax | references/capabilities/otfax-mail-exchange-integration.md | references/capabilities/otfax-profile-policy.md、references/capabilities/otfax-services-operations.md |
| 创建管理 OTFC 用户；批量导入用户 CSV；建 System/Site 管理员；配置管理员认证方式；manage OTFC users and administrators | references/capabilities/otfax-user-administration.md | references/capabilities/otfax-profile-policy.md、references/capabilities/otfax-directory-routing.md |
| 设计 OTFC 用户 Profile；禁发国际传真号码；配置传真邮件通知格式；管理企业电话簿与 LDAP 访问；configure OTFC profile policy | references/capabilities/otfax-profile-policy.md | references/capabilities/otfax-user-administration.md、references/capabilities/otfax-client-coversheet.md |
| 集成 AD/LDAP 目录；配置 Site/Profile Lookup 自动归类；配置来传真路由表与 DTMF；规整外发传真号码；configure OTFC LDAP and inbound routing | references/capabilities/otfax-directory-routing.md | references/capabilities/otfax-user-administration.md、references/capabilities/otfax-sip-channel-integration.md |
| 查 OTFC 服务状态与重启；读 OTFC 组件日志排障；激活 SIP 日志；理解服务架构分类；OTFC service management | references/capabilities/otfax-services-operations.md | references/capabilities/otfax-backup-upgrade.md |
| 备份恢复 OTFC 系统；升级 OTFC 版本；配置传真删除策略零保留；迁移传真服务器；backup restore upgrade OTFC | references/capabilities/otfax-backup-upgrade.md | references/capabilities/otfax-services-operations.md |
| 部署 OTFC 客户端；批量安装传真客户端；定制企业封页；查询传真队列状态；deploy OTFC client coversheet | references/capabilities/otfax-client-coversheet.md | — |
| 评估 OTFC 方案容量与协议；规划传真服务器部署架构；核对支持软件矩阵；应答传真合规要求；OTFC capacity planning | references/capabilities/otfax-solution-planning.md | — |
| 出 OTFC 传真量报表；自定义报表模板；接入 SNMP 监控告警；查询站点传真统计；OTFC reports SNMP monitoring | references/capabilities/otfax-reports-monitoring.md | — |

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

- 需要生产端口白名单或 sizing 数值 → 指向 OTFC Features List（书内 p38/p42 为指针页），不以实验口径搪塞
- OXE 侧互通做不通或要配中继参数 → 先要 TC3048 再上站，本书菜单骨架不足以保证话路通
- 客户要 HA/Failover 部署或 TLS 加密话路 → 声明书内边界，转产品文档/专业服务，不虚构步骤
- 涉及实验环境复刻（192.168.1.x 网段、Alcatel1!@123、mtcl） → 参考 book/overview 环境区背景并标注实验口径，不进生产
