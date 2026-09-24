---
name: omnivista-8770-nms
description: |
  OmniVista 8770 网络管理平台的安装与日常运维闭环：Windows 服务器/客户端安装、 OXE 与 OXO Connect 节点注册同步、 用户开通（Profile/Meta profile/批量/WBM）、告警接入与出口（邮件/脚本/SNMP Proxy）、权限与审计、报表任务与自动维护、 8770/OXE 两层备份恢复、许可管理。适用于 8770 R5.2 单机交付与运维问答；高可用设计、生产安全基线与容量规划工具不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.omnivista-8770-nms
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
# OmniVista 8770 — Setup & Network Management (Participant's Guide, Edition 47) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 8770 高可用/双机/多 8770 分级设计（书内仅许可 Redundancy 字段一笔带过，生产引 High Availability 文档）
- 生产安全基线（实验明文密码替换、Defender 排除与 IE ESC 关闭的客户审批、POODLE/TLS 全网元摸底方法）
- RLAB 实验平台搭建、hypervisor 侧 SNMP 规则、Capacity Planning 工具用法
- OXE 侧系统命令完整语法（siteid/netadmin/swinst 只教 8770 视角）与话务分析深水区（仅 OXE 且未展开）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 8770 是装在专用 Windows 服务器上的套件集合体（MariaDB + LDAP + Apache/Wildfly + 应用套件），安装参数（公司名/成本中心/端口/目录管理器登录）装后大多不可改，唯一后悔药是 RestoreContext.ini + 备份恢复/rehosting
2. 节点接入的钥匙是号对号：声明节点号 = 网络号×100 + 节点号，与 OXE siteid 一致才能同步；OXO Connect 同理换算（如 1x100+80=180），备份目录按声明节点落盘
3. 同步是数据流起点：Complete/Partial × Separate/Global 四语义按需选；OXE 改动经实时事件回传，但 profile、键 profile、空闲号码段必须主动同步才可见
4. 告警集中在 Alarms：相关/非相关决定自动/手动清除；出口三条——人工签名、邮件（server:port 语法）、脚本（%1/%2 变量），对外走 SNMP Proxy（trap 162，hypervisor 只填 IP）
5. 安全三层：8770 账户/组（多组取最高）> OXE Access Profile（11 档全体 OXE 共用，改后删本地 MIB）> OXE 侧访问白名单（Secure access 前提）
6. 兜底双铁律：备份与版本强绑定（nmcVersion）且备份期网管不可用、OXE 恢复须停电话；许可超限进受限模式（仅 Directory+Configuration，服务器不停机）

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 安装 OmniVista 8770 服务器；安装 8770 客户端；安装补丁；首次连接 8770；install OmniVista 8770 server | references/capabilities/ovnms-platform-installation.md | references/capabilities/ovnms-node-onboarding.md |
| 注册 OXE 节点；同步 OXE 数据；配置 OXE SSH；纳管 OXO Connect；OXE node registration synchronization | references/capabilities/ovnms-node-onboarding.md | references/capabilities/ovnms-user-provisioning.md、references/capabilities/ovnms-alarm-management.md |
| 创建 OXE 用户；配置 Meta profile 自动取号；批量开通用户；WBM 用户管理；mass provisioning OmniVista | references/capabilities/ovnms-user-provisioning.md | references/capabilities/ovnms-node-onboarding.md |
| 配置 OXE 告警上送；定制告警通知；部署 SNMP Proxy；处置告警；OmniVista alarm management | references/capabilities/ovnms-alarm-management.md | references/capabilities/ovnms-node-onboarding.md、references/capabilities/ovnms-topology-views.md |
| 配置密码策略；管理管理员与组；解锁锁定账户；配置 OXE 访问控制；OmniVista security administration | references/capabilities/ovnms-security-administration.md | references/capabilities/ovnms-audit-compliance.md |
| 启用 Audit 审计；检索管理操作记录；导出审计数据；生成审计报告；OmniVista audit | references/capabilities/ovnms-audit-compliance.md | references/capabilities/ovnms-security-administration.md、references/capabilities/ovnms-reports-scheduling.md |
| 备份恢复 8770 数据库；rehosting 换机改址；备份恢复 OXE 数据；swinst 恢复；OmniVista backup restore rehosting | references/capabilities/ovnms-backup-restore.md | references/capabilities/ovnms-network-drive.md、references/capabilities/ovnms-license-management.md |
| 查询 8770 许可；更新许可文件；处理许可超限；规划许可包型；OmniVista license nmc.license | references/capabilities/ovnms-license-management.md | references/capabilities/ovnms-platform-installation.md |
| 生成与分发报告；计划报告任务；编排 Scheduler 任务；配置自动维护清除 | references/capabilities/ovnms-reports-scheduling.md | — |
| 采集诊断信息；直查 LDAP 与 SQL 数据；管理 NMC 服务；查看与跟踪日志 | references/capabilities/ovnms-maintenance-operations.md | references/capabilities/ovnms-platform-installation.md |
| 配置 Topology 标准视图；构建自定义视图；告警重定向 | references/capabilities/ovnms-topology-views.md | — |
| OXE 配置界面检索与视图操作；配置导出导入 | references/capabilities/ovnms-oxe-ui-efficiency.md | — |
| 映射网络驱动器；配置服务账号写网络盘 | references/capabilities/ovnms-network-drive.md | — |

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

- 用户要求生产环境照抄本书实验密码/IP/账号 → 拒绝并引用 B 边界（实验口径，见 needs-review nr-06）
- 要求跨版本恢复 8770 备份或 OXE 恢复不接受停电话窗口 → 判停说明前提，不提供"热恢复"方案
- 需要 8770 集群/容灾/多级网管方案 → 超出单机闭环，转 High Availability 产品文档
- OXO 章法语残句影响理解 → 按 needs-review nr-02 语义转述，不逐字引用
