---
name: visual-automated-attendant
description: |
  VAA（Visual Automated Attendant）软件话务台/IVR 的安装、配置与维护：SUSE 服务器安装（install.sh 参数契约）与 HTTPS 证书、OXE 侧 SIP 五段链对接与接通排障、多租户与三级树设计（UC1-UC3）、提示音与 TTS/ASR 资产、IVR 选项节点（变量/收号/显示名/HTTP/邮件）、 Master/Slave 高可用与 OXE ARS 切换、日常维护备份升级、外部数据库集成、统计报告。适用于 VAA 交付、配置、排障与方案落地问答；OXE 编号计划原理、生产网络端口与公网证书细节不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.visual-automated-attendant
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# Visual Automated Attendant — Installation, Configuration and Maintenance (Participant's Guide, Edition 20) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- OXE 编号计划原理与冗余工程实施（ABC-F 语义、呼叫服务器冗余设计；OXE 侧文档体系承载）
- 端口清单、完整安装步骤、公网证书配置细节（原书外置到 VAA Installation Guide 4.2/6.4 与第 6 章）
- multi-company 配置细节（TBE083 与 OTEC-S 配置指南）与 OPEX 超配处置行为
- 非 JDBC 关系库（如 NoSQL）接入、离线/国产化 TTS 替代方案、Teams 等第三方集成（原书未涉及）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 双层路由缺一不可：VAA 内 Routing 把 DID 绑到树，OXE 侧经 ABC/F 型 SIP 中继把呼叫送进 VAA；incoming username 双侧一致是接通契约
2. 一切配置在 Web 界面完成且必须 HTTPS（4.6.104 起）；树是拖出来的（12 种原生节点 + 9 种 IVR 选项节点另购许可），每个节点必须命名——名称直接进统计
3. 依赖物先行：日历/营业时间/过滤器/提示音必须在建树之前建好；多语言树的语言选择前提示必须双语同文件
4. 高可用是 VAA 侧复制 + OXE 侧切换：Slave 只读无统计、切换丢进行中呼叫、Master 恢复后必须手工 vaa ha resync
5. 实验环境口径：教材密码、账号与网段仅限实验；规格表与端口清单为示例口径，生产以官方文档为准

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 安装 VAA 服务器；OXE 对接 VAA；拨测试树不通；install.sh parameters；VAA SIP trunk | references/capabilities/vaa-install-sip-integration.md | references/capabilities/vaa-master-slave-ha.md |
| 创建 VAA 公司租户；设计 IVR 树；多语言菜单；business hours routing；VIP 过滤分流 | references/capabilities/vaa-multitenant-tree-design.md | references/capabilities/vaa-prompt-tts-asr.md、references/capabilities/vaa-ivr-option-nodes.md |
| 导入提示音；选 TTS 引擎；开语音识别；prompt management；TTS generation | references/capabilities/vaa-prompt-tts-asr.md | references/capabilities/vaa-multitenant-tree-design.md |
| 配置 IVR 变量与条件；收号采集；HTTP 节点集成；display name node；collect digits | references/capabilities/vaa-ivr-option-nodes.md | references/capabilities/vaa-db-integration.md |
| 部署 VAA 双机；主备切换测试；OXE ARS 双路由；vaa ha addslave；高可用行为 | references/capabilities/vaa-master-slave-ha.md | references/capabilities/vaa-install-sip-integration.md、references/capabilities/vaa-architecture-redundancy.md |
| VAA 日常巡检；备份恢复；升级 VAA 版本；vaa commands；密码策略 | references/capabilities/vaa-maintenance-backup.md | references/capabilities/vaa-install-sip-integration.md、references/capabilities/vaa-master-slave-ha.md |
| VAA 连接外部数据库；SQL 节点查库转接；安装 JDBC 驱动；MS SQL connectivity；Oracle JDBC URL | references/capabilities/vaa-db-integration.md | references/capabilities/vaa-ivr-option-nodes.md |
| 配置话务周报；逐节点排障；导出呼叫日志；VAA statistics；报表口径 | references/capabilities/vaa-statistics-reporting.md | references/capabilities/vaa-multitenant-tree-design.md |
| 添加 VAA 管理员；配置 SMTP 告警；查看 VAA 日志；webadmin setup；受限用户档案 | references/capabilities/vaa-webadmin-administration.md | — |
| 配置 PCS 同步；OPEX 模式评估；核查 VAA 许可；Purple On Demand；许可失效排查 | references/capabilities/vaa-pcs-opex-licensing.md | — |
| 选 VAA 服务器规格；核对虚拟化兼容；端口数上限；VAA hypervisor；sizing | references/capabilities/vaa-server-sizing-virtualization.md | — |
| 解释 VAA 架构；multi-company 集成；N+1 冗余；VAA call flow；冗余选型 | references/capabilities/vaa-architecture-redundancy.md | — |

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

- 端口数超 120 或需跨站点容灾 + OPEX 组合 → 超出书内范围（120 上限找中央售前；空间冗余与 Purple On Demand 互斥），如实声明
- 需要生产网络端口/证书细节或完整安装步骤 → 指向 VAA Installation Guide 对应章节，不以实验口径搪塞
- 涉及 RLAB/ITSP1 实验环境搭建 → 参考 book/overview 环境区背景，不虚构生产配置
- 4.8.006 升级诉求 → 按书内唯一路径回答（全新安装 + 数据库恢复 + Release 11 新许可），不提供原地升级方案
