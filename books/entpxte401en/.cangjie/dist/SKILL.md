---
name: oxe-advanced
description: |
  OmniPCX Enterprise 高级部署与运维支持：SSH 免密地基、CS 冗余（本地/空间）与不停机升级、IP 域与 CAC、PCS 域级生存性、公私网双向溢出与重路由、 Direct IP Link 全 IP 组网、Audit/Broadcast 数据一致性，以及多线监督、经理助理、寻线代接、速拨、办公桌共享、多设备等话机级业务。适用于 OXE 企业级机制的配置、演练、 排障与行为解释问答；冗余拓扑/域规划等设计决策的话务输入、生产安全基线与 Starter 级前置不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.oxe-advanced
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# OmniPCX Enterprise - Advanced (Participant's Guide, Edition 13) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- Starter 级内容：装机、barring、ARS 基础、GD/OMS SSH 方法、swinst/netadmin 入门（原书多处 REFER TO STARTER TRAINING）
- 话务模型（Erlang）与带宽计算方法论；15000/100000/1488/10000 呼时等均为标称口径
- 生产安全基线（证书轮换、口令治理、PKI 管理）与 OmniVista 8770/4645 VM/DECT/SIP 终端装机操作
- RLAB/SIP 模拟器教学基础设施搭建与培训评估流程

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 高可用分层各管一段：CS 冗余保呼叫控制（已建立通话跨切换存活）、IP 域+PCS 保远程域断链自治、公私网溢出保电话网退路——三层不可互替
2. SSHv2 公钥免密自 N3 起是协同地基：mastercopy/pcscopy/audit/broadcast 全依赖；oxe-ssh-auth 管一对、oxe-nw-sshkey-sync 以 CSV 管全网
3. 冗余对铁律同版本同类平台；备机失联窗口默认 120 分钟（0-120 可配），超时触发 440 事件只能 mastercopy 整库克隆
4. IP 域按设备初始化时 IP 归属落域且 CS/PCS 必须域 0；CAC 只闸跨域通话数（-1 不限）；PCS 是域级生存性而非热备（30 天上限、库单向同步）
5. Direct IP Link 启用是一次性决策：Disabled→Migrating（必须重启）→Enabled 不可逆；两端带宽/加密/接入数不一致即 2879 拒建
6. Audit 直改表须先模拟+强烈建议备份全网库；Broadcast 默认 10 分钟周期非即时；trunk 组前缀/ARS 表/IP 域等本地对象不广播不审计
7. 实验口径纪律：书中 IP/账号/密码/号码仅限 RLAB；生产化依据指向 My Portal 技术文档与 Starter 教材，容量数字须带标称上限前提

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 分发 SSH 免密密钥；mastercopy 或 pcscopy 认证失败；oxe-ssh-auth 用法；oxe-nw-sshkey-sync CSV 格式；ssh passwordless between OXE | references/capabilities/entadv-ssh-trust-foundation.md | references/capabilities/entadv-cs-redundancy.md、references/capabilities/entadv-audit-broadcast.md |
| 部署本地/空间冗余 CS 对；执行冗余切换或不停机升级；处理 double main 或 440 事件；mastercopy 克隆数据库；CS duplication bascul switchover | references/capabilities/entadv-cs-redundancy.md | references/capabilities/entadv-ssh-trust-foundation.md、references/capabilities/entadv-ip-domain-pcs.md |
| 规划配置 IP 域与 CAC；部署 PCS；断链救援与回切演练；处理设备不落域或跨域拒呼；PCS survivability pcsview | references/capabilities/entadv-ip-domain-pcs.md | references/capabilities/entadv-overflow-rerouting.md |
| 配置私到公溢出（本地/组网）；配置公到私重路由；规划 thin sector 或 DID 翻译；处理来电显示变成外部号类问题；overflow rerouting ARS | references/capabilities/entadv-overflow-rerouting.md | references/capabilities/entadv-ip-domain-pcs.md、references/capabilities/entadv-direct-ip-link.md |
| 建立或迁移 Direct IP Link 组网；处理 2879 或链路建不起来；加删组网节点；评估直链容量与监控方式；direct ip link ABC-F2 | references/capabilities/entadv-direct-ip-link.md | references/capabilities/entadv-audit-broadcast.md |
| 执行全网 Audit 对账；启用或巡检 Broadcast；新节点并入全网导数据；处理 RLOG 或数据分叉；audit broadcast OXE database | references/capabilities/entadv-audit-broadcast.md | references/capabilities/entadv-ssh-trust-foundation.md、references/capabilities/entadv-direct-ip-link.md |
| 配置多线与监督键；建经理/助理组与过滤表；设计助理顶班（away/溢出助理）；核算监督容量上限；multiline supervision manager assistant | references/capabilities/entadv-multiline-supervision.md | references/capabilities/entadv-hunting-pickup-speeddial.md |
| 建寻线组与溢出策略；配代接组；管理速拨编号体系；处理缩位号闭锁合规；hunting group pickup speed dial | references/capabilities/entadv-hunting-pickup-speeddial.md | references/capabilities/entadv-multiline-supervision.md |
| 配置办公桌共享；解释 DSU 忙时被顶或 6004；规划共享工位机型；desk sharing DSS DSU | references/capabilities/entadv-desk-sharing.md | references/capabilities/entadv-multi-device.md |
| 配置多设备用户或 Twinset；执行快速移机；规划主站退服兜底；multi device twinset tandem | references/capabilities/entadv-multi-device.md | references/capabilities/entadv-desk-sharing.md、references/capabilities/entadv-multiline-supervision.md |
| 搭建教材同构实验环境；换算 POD 号码规则；处理实验 IP 冲突或 ping 不通；RLAB pod ITSP1 numbering | references/capabilities/entadv-lab-pod-baseline.md | — |
| 查状态该用什么命令；解释事件号含义；核验许可锁；maintenance commands incident codes | references/capabilities/entadv-cli-toolbox.md | — |

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

- 需要冗余拓扑选择、域与编号规划、PCS 布点等设计输入 → 标注书外，指向客户网络设计与 My Portal 技术文档，不以实验口径搪塞
- Direct IP Link 已 Enabled 想改回 → 如实说明不可逆（只能恢复数据库备份），引导走变更/回滚流程而非尝试改系统选项
- 引用容量数字做承诺 → 强制带前提（每链/每节点/每系统+标称口径），缺话务模型时明确说明
- 客户期望 PCS 长期顶班或给无 MG 纯 SIP 域配 PCS → 按 30 天上限与救援边界如实纠偏
