---
name: oxe-loading
description: |
  OmniPCX Enterprise（OXE）软件加载与云许可交付支持：用 S.O.T. 部署工具完成 CS 从物理板卡、虚机到 GAS 一体机的全形态软件加载与补丁/多版本管理，OXE-V 虚拟化选型与虚机交付，GAS 加载与后安装，Cloud Connect 云连接（FTR/RTR），OPEX/Purple on Demand 订阅许可与 LMS 同步。 适用于 OXE 软件交付、云注册与订阅许可的配置、排障与验收问答；OXE 数据库业务配置（用户/路由/编号计划）不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.oxe-loading
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# OmniPCX Enterprise — 系统装载 (Participant's Guide, Edition 12) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- OXE 数据库业务配置（用户创建、编号计划、路由、话机开通）——原书指向 Starter 课程
- 虚拟化设计权威细节（TBE043）、AWS 部署（TC3142en-Ed01）、GAS 安装权威步骤（TC3138）
- N3 以下版本迁移的执行细节（TC3104en-Ed08 指南）
- 生产安全基线加固与容量规划方法论（原书仅引用 CIS 条目一次，不展开）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 一切软件交付围绕 S.O.T.：一台自带 DHCP/FTP 服务的虚机，Standalone 加载物理机、Hosted 加载虚机；一次只允许一个部署任务
2. 双分区是升级安全模型：第二版本不停话音装好、切换才重启；静态补丁停话音或装 inactive，动态补丁可热装但必须在静态之后；补丁累积包含此前全部修正
3. 虚拟化平台决定许可路径：FlexLM+加密狗仅 ESXi/KVM；Hyper-V/Nutanix/AWS 必须 Cloud Connect；FlexLM 与 RTR 两种模式互斥
4. FTR 是云服务门禁：swk 含 CCSID、电话应用已启动、连通性全绿才能注册；备机禁做 FTR；panic 后 PIN 是唯一出路
5. RTR 与 LMS 都靠对账维持许可：RTR 资格期 30 天起、OK 加 0.5 天/NOK 减 1 天；OXE 每 4 小时与 LMS 对账，失联或超订会进 panic 逐渐锁死系统
6. 实验环境口径：教材密码、账号与网段仅限实验；加载 completed 之后角色寻址、许可恢复、业务配置是独立的后置清单

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 部署 SOT 虚拟机；更新 SOT 版本；启用 Template Factory；SOT 首连初始化；deploy SOT virtual machine | references/capabilities/entload-sot-installation.md | references/capabilities/entload-sot-media.md |
| 全新安装 OXE 呼叫服务器；加载卡在等待目标机；加载后初始化清单；设 OXE 账户密码；load full release on OXE | references/capabilities/entload-cs-loading.md | references/capabilities/entload-sot-media.md |
| 多版本加载与分区切换；安装静态/动态补丁；升级回退预案；补丁维护窗口评估；install patch on OXE | references/capabilities/entload-patch-management.md | references/capabilities/entload-cs-loading.md |
| 选择虚拟化平台与许可路径；生成并加载 OXE 虚机；加载 OMS 媒体网关虚机；OMS 容量与许可计算；deploy OXE-V virtual machine | references/capabilities/entload-oxe-v-deployment.md | references/capabilities/entload-sot-installation.md、references/capabilities/entload-patch-management.md |
| 加载 GAS 服务器；执行 GAS 后安装向导；配置 FlexLM 许可；配置 WebRTC 网关参数；install Generic Appliance Server | references/capabilities/entload-gas-delivery.md | references/capabilities/entload-gas-ops.md、references/capabilities/entload-sot-media.md |
| 配置 DNS 代理并验证云连通性；执行 FTR 首次注册；FTR 失败排障；PIN 恢复 panic；perform First Time Registration | references/capabilities/entload-cloud-connect.md | references/capabilities/entload-rtr-licensing.md、references/capabilities/entload-pod-licensing.md |
| 启用 RTR 许可；解读资格期与 Dashboard 状态；处置 Duplicated 告警；RTR 事件排障；monitor Right To Run status | references/capabilities/entload-rtr-licensing.md | references/capabilities/entload-cloud-connect.md、references/capabilities/entload-fleet-dashboard.md |
| 下载并安装 PoD 许可；核查 OXE 与 LMS 许可同步；配置订阅消耗与阈值；评估 C2P 转换；configure Purple on Demand licensing | references/capabilities/entload-pod-licensing.md | references/capabilities/entload-cloud-connect.md |
| 无 SOT 环境加载版本；分发器模式装补丁；清理 Rload 目录；local load as distributor | references/capabilities/entload-distributor-loading.md | references/capabilities/entload-patch-management.md、references/capabilities/entload-cs-loading.md |
| 向 SOT 传输软件媒体；声明媒体与许可文件；创建加载项目；declare media in SOT | references/capabilities/entload-sot-media.md | — |
| 查 GAS 组件版本；备份恢复 GAS；升级 GAS 宿主系统；配置 UPS 监控；backup and upgrade GAS | references/capabilities/entload-gas-ops.md | references/capabilities/entload-gas-delivery.md |
| 云端盘点 OXE 资产；推取许可与 offer 文件；使用远程控制台；云端下发软件更新；Fleet Dashboard services | references/capabilities/entload-fleet-dashboard.md | references/capabilities/entload-rtr-licensing.md |

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

- 需要建用户/配路由/做编号计划 → 明确超出本书范围，指向 Starter 课程，不以加载口径搪塞
- 虚拟化平台版本不在 Ed12 矩阵内 → 以 TBE043 最新版复核，不按教材矩阵硬答
- RTR 失败扣减口径争议 → 按 needs-review nr-01 双口径如实说明，监控按保守口径设计
- 涉及 RLAB 实验环境搭建与节点口令 → 参考 book/overview 环境区背景并标注实验口径，不虚构生产配置
