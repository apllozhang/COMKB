---
name: oxo-connect-advanced
description: |
  OXO Connect（R6.3）进阶组网与垂直方案交付：公网/私网 SIP 组网与注册排障、ARS 路由套件（三表协作/多运营商/Internal ARS）、酒店与计费垂直方案、 系统安全加固、证书与加密传输（DTLS/TLS-SRTP）、语音导航（AA/MLAA/SCR）、语音邮箱与移动办公、Cloud Connect 舰队与远程维护。适用于已掌握 OXO 基础的交付/售后 工程师的进阶配置、选型、排障与方案落地问答；OMC 安装与云侧入门属 bundle.oxo-connect-starter，生产化数值与方案方法论不在原书范围（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.oxo-connect-advanced
  cangjie.capability-count: 14
  cangjie.entrypoint-count: 1
---
# OXO Connect - Advanced (Participant's Guide, Edition 18) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 生产运营商互联参数、eBuy license 资料、国家 DECT 频段许可等"讲师给值"位（原书全部为实验口径）
- 方案设计方法论：ARS 前缀规划、MLAA 菜单设计、DECT 布点勘测方法（SSK 手册 8AL90874USAA）、license 规划——书内只给机制与上限
- OMC 安装入门、Rainbow 云侧公司/订阅/成员体系（属 bundle.oxo-connect-starter）；OXE 平台详节
- 外部计费应用入账、企业 PKI 审批流、Teams/Rainbow 租户策略、ACD 呼叫中心完整运营

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 双工具贯穿全书：OMC 管配置对象树，Webdiag 管调试/证书/抓包；几乎所有 How-To 都以"行为验证"收口（History Table 消息、显示字符、LED、小票文件）
2. 组网三件套：编号计划触发、ARS 表匹配变换、中继组列表按序选路；Media 带宽最少 5 通话是公网与私网网关共同的外呼放行闸门
3. 垂直与增强按 license 分层：酒店/OHL、Call Accounting、安全加固、DTLS、TLS/SRTP、Cloud Connect 免 license；AA 定制、MLAA 树数、SCR、Hot Desking、IP-DECT 用户、多实体 MoH 需 license
4. 安全基线五支柱：强制改默认密码 + AutoPwdChk 自动检查 + Network IP Services 网络面收敛 + VMU 锁定翻倍（封顶 1440 分钟）+ 加固清单；总纲 TC1143
5. 实验环境口径：教材全部 IP/密码/账号/号码为 RLAB 教学值；生产必须替换并按 TC1143/TC1398/Global Limits 等书外权威文档校准

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 配置公网 SIP 网关；SIP 注册失败排查；两台 OXO 私网互联；私网饱和溢出公网；configure SIP gateway；SIP trunk registration | references/capabilities/oxoa-sip-networking.md | references/capabilities/oxoa-numbering-ars-suite.md、references/capabilities/oxoa-certificate-suite.md |
| 规划 ARS 选路；多运营商分流与溢出；一个 DDI 分时段路由；非营业时间播欢迎消息；ARS routing configuration | references/capabilities/oxoa-numbering-ars-suite.md | references/capabilities/oxoa-sip-networking.md、references/capabilities/oxoa-voicemail-mobility.md |
| 部署酒店模式；客房计费与预付切断；生成 XML 计费小票；账号码与内部替代；hotel solution setup | references/capabilities/oxoa-hotel-billing-vertical.md | references/capabilities/oxoa-sip-networking.md |
| 执行安全基线核查；密码策略与弱密码审计；收敛管理面与话务面；远程访问锁定处理；system security hardening | references/capabilities/oxoa-security-hardening.md | references/capabilities/oxoa-certificate-suite.md |
| 管理数字证书与 PKI 签发；部署 DTLS 话机信令加密；配置 SIP 中继 TLS/SRTP；4K 证书升级与回滚；certificate and TLS SRTP setup | references/capabilities/oxoa-certificate-suite.md | references/capabilities/oxoa-security-hardening.md、references/capabilities/oxoa-sip-networking.md |
| 配置自动话务员；多语言多树导航；按客户码分流来话；语音导航排障；auto attendant MLAA SCR | references/capabilities/oxoa-attendant-suite.md | references/capabilities/oxoa-voicemail-mobility.md、references/capabilities/oxoa-numbering-ars-suite.md |
| 配置语音邮箱远程接入；处理邮箱锁定与解锁；激活游牧模式；配置远程替代回环；voicemail nomadic remote substitution | references/capabilities/oxoa-voicemail-mobility.md | references/capabilities/oxoa-attendant-suite.md、references/capabilities/oxoa-numbering-ars-suite.md |
| 注册系统到 Cloud Connect；舰队软件更新；选型远程维护通道；同步 Rainbow 业务目录；cloud connect fleet management | references/capabilities/oxoa-cloud-connect-fleet.md | references/capabilities/oxoa-security-hardening.md |
| OMC 首次连接；修改 OXO IP 规划；IPDSP 安装报错处理 | references/capabilities/oxoa-foundation-ip.md | — |
| 接入 SIP 话机或软话机；选择媒体处理路径；部署 PIMphony；SIP 话机排障 | references/capabilities/oxoa-terminal-ecosystem.md | — |
| 配置站群监督；部署 Hot Desking；配置 Multiset/Twinset | references/capabilities/oxoa-shared-devices.md | — |
| 多实体隔离配置；两家公司共享系统分账 | references/capabilities/oxoa-multi-entity.md | — |
| 选型与部署 DECT；注册 DECT 话机；勘测验收覆盖；SUOTA 批量升级 | references/capabilities/oxoa-dect-deployment.md | — |
| Webdiag 排障与信息收集；noteworthy 地址修改；LoLa 系统加载与迁移；退役设备净化 | references/capabilities/oxoa-maintenance-toolkit.md | — |

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

- 涉及生产取值（运营商参数/端口带宽/ARI/密码策略）→ 明确指向书外权威来源（运营商合同/TC 文档/Global Limits），不以实验口径搪塞
- 用户数、公司数、树数等超出书内容量上限（4 实体、5 MLAA 树、10000 SCR 规则、80 xBS 等）→ 声明上限并转其它产品线或架构方案
- 版本敏感判定（4K 证书回滚、8214 兼容、8158s NOE 模式）→ 按书内注记如实说明并要求核对最新 TC
- 原书内部矛盾（Internal ARS 时段 nr-01、DHCP 池 nr-02、门户域名 nr-05）→ 双口径如实呈现，不给虚假唯一答案
