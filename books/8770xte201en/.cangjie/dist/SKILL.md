---
name: omnivista-billing-performance
description: |
  OmniVista 8770 R5.2 计费与性能管理交付支持：OXE 纳管与票据回收管道、运营商资费建模与成本计算、Code Book 迁移、计费组织树与成本归属、机密控制 （掩码/解密/可见域）、成本档案、报表生成与定制、VoIP 性能、流量分析与 Tracking 告警、Web Performance 仪表盘、计费归档恢复。适用于 8770 计费与性能的配置、 排障与交付问答；真实运营商价目、数据库运维与安全凭证治理不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.omnivista-billing-performance
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
# OmniVista 8770 R5.2 Accounting and Performance Administration (Participant Guide, Edition 45) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 真实运营商价目数据工程与各国监管费率（书内全用教学数值，法国 SVA 仅示例 ARCEP 口径）
- MariaDB 容量规划、备份与恢复演练（书内仅 Maintenance 一句带过）
- SNMPv3 与系统口令的生产治理（书内明文密码均为实验口径）
- 话务数据法定留存期限与合规结论（125 天是机制上限，GDPR 类合规在书外）
- 8770 安装、虚机规格与防火墙端口（属安装文档与 Capacity Planning tool）；OXE 维护命令体系（属 OXE 技术文档）
- RLAB 实验平台搭建与报表练习题面的具体业务数值（教学专用，保留模式替换业务值）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 单向管道：OXE 内存缓冲（≤500 条，满或 90 分钟无新票落盘）经 TAX 文件与 ACCOUNT.LIS，由 8770 对比索引 FTP 增量取回、加载过滤后入库，断点按目录与日志逐段查
2. 成本在票据加载时算好：运营商配置为 Period 下的 Calendar/Region/Tariff/Direction；配置改动涉及存量必须 Compute cost（Force）重算，否则新旧成本混存
3. 费率可复算：exact 线性可叠加接通费/免费时长/保底/分段，round 按阶段计，脉冲按票据 Charge units 乘单价；服务费 C+S 须双资费成对绑方向
4. 组织树决定钱归谁：成本中心从 OXE 同步（cc=255 落根，无成本中心对象落默认成本中心）；分机改归属只能回 OXE 配置；剪贴无历史、复制留灰色条目
5. 机密三道闸：掩码档案按树继承遮显示（grouped 报表只认 Default 档案）、解密须 Mask data access 组口令、可见域按管理员裁剪；OXE 侧已遮号码 8770 无法还原
6. 质量与告警有量化口径：VoIP KPI 默认时延大于 150ms、丢包大于 3%、BFI Burst 大于 5%；流量分析仅 OXE 且默认只算三类对象（PtpType ALL 才看被叫与终端）；Tracking 由任务驱动非实时
7. 数据寿命：计费票 31 天归档成 archZ、再 94 天清理，最长 125 天且按记录日期清理；书内实验口径数值（税率/汇率/密码）一律不进生产

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 把 OXE 接入 8770；同步失败排查；信任主机核查；配置 SIP 运营商模拟器；register OXE node | references/capabilities/ovbill-node-onboarding.md | references/capabilities/ovbill-ticket-pipeline.md |
| 8770 收不到话单；开启 OXE 外部计费；选择计费方法；排查票据入库；accounting records retrieval | references/capabilities/ovbill-ticket-pipeline.md | references/capabilities/ovbill-node-onboarding.md、references/capabilities/ovbill-tariff-costing.md |
| 建运营商资费模型；配置费率公式；成本计算与重算；特服号服务费计费；carrier tariff configuration | references/capabilities/ovbill-tariff-costing.md | references/capabilities/ovbill-ticket-pipeline.md、references/capabilities/ovbill-cost-profile.md |
| 迁移运营商配置；修复 code book 导入报错；运营商配置备份；import export code book | references/capabilities/ovbill-codebook-migration.md | — |
| 搭建计费组织树；搬移成本中心；历史票据归属修正；ToolsOmniVista 组织更新；organization tree management | references/capabilities/ovbill-org-costing.md | references/capabilities/ovbill-confidentiality.md |
| 配置号码与成本遮蔽；开通解密报表权限；隔离管理员可见范围；mask profile and visibility domain | references/capabilities/ovbill-confidentiality.md | references/capabilities/ovbill-org-costing.md、references/capabilities/ovbill-reporting.md |
| 配置发票加价或折扣；配置设备订阅费；订阅计费口径解释；cost profile configuration | references/capabilities/ovbill-cost-profile.md | — |
| 生成与导出报表；报表邮件分发；配置定时报表；report generation and export | references/capabilities/ovbill-reporting.md | references/capabilities/ovbill-report-design.md |
| 从零创建报表定义；配置分组汇总与 hit-list；报表公式与图表；report customization | references/capabilities/ovbill-report-design.md | references/capabilities/ovbill-reporting.md |
| 配置 VoIP 质量监控；解读 VoIP 质量报告；排查 VoIP 报告空表；voip performance monitoring | references/capabilities/ovbill-voip-monitoring.md | references/capabilities/ovbill-web-performance.md |
| 配置话务量报表；开通被叫号与终端话务统计；配置阈值告警与邮件；tracking profile and alerts | references/capabilities/ovbill-traffic-tracking.md | references/capabilities/ovbill-ticket-pipeline.md |
| 部署 WBM 性能仪表盘；配置 SNMPv3 采集；调优轮询与 widget；web performance dashboard | references/capabilities/ovbill-web-performance.md | references/capabilities/ovbill-voip-monitoring.md |
| 配置计费归档；恢复历史票据；定向清除恢复票；accounting archiving and restore | references/capabilities/ovbill-archiving.md | references/capabilities/ovbill-org-costing.md |

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

- 用户要真实价目/税率/汇率的权威数值 → 指向运营商价目与监管文件（如法国 ARCEP），不以教学值搪塞
- 涉及生产口令、SNMP 凭证治理或留存合规 → 声明书内为实验口径，要求客户提供安全基线与合规口径
- 多节点组网、PCS 与 OpenTouch 关联同步的生产部署 → 书内只有概念图无实验，声明边界不虚构
- 数据库容量、备份与恢复演练需求 → 指向 8770 安装文档与数据库运维规范（书外）
- 版本漂移敏感问题（兼容矩阵/界面/预定义报表清单）→ 按 Ed45 与 R5.2 口径回答并提示重核最新文档
