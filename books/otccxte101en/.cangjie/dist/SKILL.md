---
name: otcc-standard-advanced
description: |
  OmniTouch Contact Center Standard 高级能力交付与运营支持：网络互助（盲/智能互助、Remote PG 三对象、ABC-F 链路诊断）、 Soft Panel Manager 实时墙板 （部署三件套与可视化配置）、 CCTA 票据分析、特殊功能开关、 Excel 报表定制、 CCS Server 集中接入，以及 ACR 对象/技能体系与 ISM 匹配排序口径。适用于 OTCC Standard 高级功能的配置、排障、容量核对与验收问答；ASM 脚本编写深度与 LCA 脚本族由姊妹技能 otcc-standard-advanced-call-routing 承接（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.otcc-standard-advanced
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# OmniTouch Contact Center Standard Edition - Advanced (Participant's Guide, Edition 07) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- ASM 脚本积木块级开发、LCA_1/2/3 渐进脚本族与调试器完整实操（姊妹技能 otcc-standard-advanced-call-routing 承接）
- 技能体系设计方法论（域怎么划、权重怎么定、坐席技能怎么评定，原书只教配置）
- 话务建模与 sizing（Erlang、坐席/中继估算）、监听与录音的法律合规边界（原书零覆盖）
- RLAB 虚机平台细节与培训评估流程（教学专用基础设施）
- OXE 组网与 Direct IP Link 的新建规划（书内只给状态诊断与互助行为）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. ACR 呼叫三步走：特征化（CLID/被叫号/呼叫标签/呼叫档案）> ASM 按脚本算坐席列表（动态组）> 呼叫带列表进等待室分配；等待室非 FIFO 且与等待队列同规则互斥
2. ISM 匹配是三级漏斗：强制属性全满足进第 1 子列表 > 重选定时不中逐级降级 > 同级按 Cman 最小、同分比 Copt（缺技能按 9 代入）、再同分按 PLTR/LIT
3. 网络互助的关键是"知道对方状态"：智能互助经 ABC-F 交换 Pilot 状态与真实等待时间；Remote PG 有分布门限+资源选择优先级而无呼叫选择优先级；三级水位=优先级 0-9 > 门限秒数 > MWT 饱和
4. Soft Panel Manager 是独立数据链：RTI Connector 从 CCS 取数推 SPM（Tomcat 9060），统计按需订阅（选用后最多 1 分钟生效），日统计 15 分钟节拍不可更快
5. 运维有完整命令箱：adm_acd（含 -salb/-servccs）、agacd、hybvisu/compvisu、pildstctx/pgctx、acdsup、spadmin，配合 Navigator 与调试器全栈排障
6. 实验环境口径：教材密码、账号、号码、编号仅限实验；容量数字（21 次重选、5 分钟统计刷新、15 秒门限）均为实验观察口径而非调优建议

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 解释坐席分配次序；开启最久空闲优先；手算 ISM 坐席列表；ACR 容量核对；ISM skill matching；longest idle time | references/capabilities/otcad-ism-skill-matching.md | references/capabilities/otcad-acr-objects.md、references/capabilities/otcad-asm-script-advanced.md |
| 部署跨站点互助；排查 Remote PG blocked；判读 ABC-F 链路状态；mutual aid overflow | references/capabilities/otcad-remote-pg-mutual-aid.md | references/capabilities/otcad-acd-maintenance.md、references/capabilities/otcad-special-features.md |
| 安装 Soft Panel Manager；排查墙板没数据；配置日统计；SPM deployment | references/capabilities/otcad-spm-deployment.md | references/capabilities/otcad-soft-panel-manager.md |
| 配置实时看板；配置告警视图与邮件；选择挂件类型；wallboard configuration | references/capabilities/otcad-soft-panel-manager.md | references/capabilities/otcad-spm-deployment.md |
| 分析话务票据；导出呼叫明细；排查放弃率；ticket analysis | references/capabilities/otcad-ccta-ticket-analysis.md | references/capabilities/otcad-excel-report-customization.md |
| 配置优先转接；配置代接前缀；配置监督监听与永恒整理；中继预留计算；special features setup | references/capabilities/otcad-special-features.md | references/capabilities/otcad-remote-pg-mutual-aid.md |
| 定制报表模板；报表加图表；排查粒度缺数据；Excel report template | references/capabilities/otcad-excel-report-customization.md | references/capabilities/otcad-ccta-ticket-analysis.md |
| 部署 CCS Server；内部转外部切换；排查外部服务拒接；CCS server migration | references/capabilities/otcad-ccs-server.md | references/capabilities/otcad-ccs-onboarding.md、references/capabilities/otcad-acd-maintenance.md |
| 部署 ACR 矩阵对象；配置技能与呼叫档案；排查等待室阻塞；ACR waiting room setup | references/capabilities/otcad-acr-objects.md | references/capabilities/otcad-ism-skill-matching.md、references/capabilities/otcad-asm-script-advanced.md |
| 安装 ASM Script Editor；激活脚本到 Pilot；调试器抓路由轨迹；清空 ASM 记忆；ASM script debugger | references/capabilities/otcad-asm-script-advanced.md | references/capabilities/otcad-acr-objects.md |
| 安装 CCsupervision；声明 OXE；坐席软话机登录；配置 DID 翻译；CCS installation | references/capabilities/otcad-ccs-onboarding.md | references/capabilities/otcad-acr-objects.md |
| 查询 ACD 对象清单；判读链路状态；核查 ASM 记忆；核对许可包；ACD maintenance commands | references/capabilities/otcad-acd-maintenance.md | references/capabilities/otcad-remote-pg-mutual-aid.md |

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

- 需要 ACR 脚本级深度开发或复杂 LCA 策略 > 明确转姊妹技能 otcc-standard-advanced-call-routing，不在本 bundle 内展开
- 需要生产容量承诺或话务建模 > 声明书中数值为实验口径与合规红线，指向当期 Feature List 与话务数据
- 涉及监听/录音上线 > 先过法律合规评审，本 bundle 只覆盖技术开关与行为验证
- 版本相关判定（CCS Server 15/120、p558 "29 or 120"）> 按 needs-review nr-01 双口径如实说明，以 15/120 与 ">9 强制" 为规划口径
