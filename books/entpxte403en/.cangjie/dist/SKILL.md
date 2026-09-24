---
name: oxe-sip
description: |
  OmniPCX Enterprise（OXE）SIP 化交付与运维支持：SIP 协议机理与六组件架构、SEPLOS/SIP Device 两形态选型与容量、SIP Device 与 ALE 话机与 ALES 软终端三条开通线、 OXE DM 证书体系、经 SBC 的运营商接入与 OTSBC 部署、远程办公（SBC/RP/EDS/VPN）、编解码与信令排障。适用于 OXE 站点 SIP 化的配置、选型、排障与方案问答； 真实运营商参数、外部 CA 流程、零touch 开户等生产化依据不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.oxe-sip
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
# OmniPCX Enterprise - SIP (Participant's Guide, Edition 12) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 真实运营商参数（REGISTER 行为、SIPS 强制、P-Asserted-Identity 策略、号码格式）——以 TC2005 与运营商文档为准（原书明示书外）
- 外部 CA 申请签发流程、企业 PKI 策略、安全加固制度（原书只给机制与内部 PKI 演示）
- EDS 账号开通操作与 NGINX PLUS 反代部署细节、VPN 网关兼容清单（指向 EDS user manual、Server deployment Guide for Remote workers）
- SBC 高可用与容量规划、话务建模与带宽估算方法论（原书无性能章节）
- SIP 协议报文逐字段教学与 Wireshark 深度分析（属协议基础课）；Teams/Rainbow 等外部生态集成细节

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. SIP 只做信令不做媒体搬运：会话建立/维持/修改/终止归 SIP，媒体协商靠 SDP、传输靠 RTP；OXE 六组件（本地网关/字典/代理/注册器/位置/外部网关）同栖 sipmotor
2. SIP 用户两形态决定服务等级：SEPLOS=内部话机级（前缀后缀/寻线组/CTI），SIP Device=远端子网设备级（五不带）；软件锁 177/345/430 与 15000 用户/20000 设备管规模
3. 终端入网四步链：DHCP 拿 DM 地址 → HTTPS 拉 DM 配置文件 → 拉二进制 → SIP 注册；注册即服务、超时即离服；一切发起请求的设备必须是 CS 防火墙信任主机
4. 证书是地基：默认证书只适配 WBM，须内部 PKI 定制（SAN 含 FQDN/通配/IP）并产出 CTL；R101.0 起 OpenSSL 安全级 2 拒收 RSA<2048 位或 SHA-1
5. 外线双腿施工：OXE 侧（信任主机/中继组/外部网关/ARS/DID/NPD/回拨）+ OTSBC 侧（向导+编解码放行/消息域改写/Contact User 注册），缺一不通
6. 远程办公两条路：SBC/RP（≤500 用 OTSBC 内嵌反代）与 VPN（仅 ALE-2/3 内嵌 OpenVPN）；EDS 零touch 四限制；远程加密放行是 N4 起语义
7. 实验环境口径：教材密码、账号、号码全部为 RLAB 实验值（模拟运营商与真实 ITSP 行为差异大）；生产以 TC2005/TC2957/Features List 等权威文档为准

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 理解 SIP 协议机理；OXE SIP 架构组件；修改 OXE 域名；空间冗余终端怎么接入；SIP response codes meaning | references/capabilities/osip-protocol-foundation.md | references/capabilities/osip-user-forms.md、references/capabilities/osip-sip-device-provisioning.md |
| 选 SEPLOS 还是 SIP Device；SIP 软件锁与容量；ALE 话机怎么选型；会议话机门禁接入方案；SIP user capacity limits | references/capabilities/osip-user-forms.md | references/capabilities/osip-sip-device-provisioning.md、references/capabilities/osip-deskphone-provisioning.md |
| 开通 SIP Device 用户；会议话机接入 OXE；SIP 中继组虚拟接入扩容；SIP device registration troubleshooting | references/capabilities/osip-sip-device-provisioning.md | references/capabilities/osip-sip-troubleshooting.md |
| 开通 ALE-2 ALE-3 话机；NOE 话机切换到 SIP；双分区 Force Download；auto-discovery 注册；DHCP class TFTP URL | references/capabilities/osip-deskphone-provisioning.md | references/capabilities/osip-certificate-management.md、references/capabilities/osip-dm-management.md |
| 开通 ALES 软终端；配置 LDAP 认证；ALES 推送不工作；一号多机 403；switch to local authentication | references/capabilities/osip-ales-provisioning.md | references/capabilities/osip-sip-features.md、references/capabilities/osip-remote-workers.md |
| OXE 证书报错；生成 CS 证书与 CTL；老话机证书被拒；OpenSSL 安全级别；mTLS DM authentication | references/capabilities/osip-certificate-management.md | references/capabilities/osip-deskphone-provisioning.md |
| 接入 SIP 运营商；配置 ARS 和 DID 翻译；部署 OTSBC；外线打不通；SBC registration Contact User | references/capabilities/osip-otsbc-carrier-interconnect.md | references/capabilities/osip-remote-workers.md、references/capabilities/osip-sip-troubleshooting.md |
| 员工居家办公打电话；远程办公方案选型；EDS 零touch 部署；OTSBC 反向代理配置；ALES Remote Worker | references/capabilities/osip-remote-workers.md | references/capabilities/osip-otsbc-carrier-interconnect.md |
| 音质差单通排查；编解码协商规则；488 法线不匹配；compvisu 看编解码 | references/capabilities/osip-codec-negotiation.md | references/capabilities/osip-sip-troubleshooting.md |
| 抓 SIP 信令；oxetrace 打包取证；sipdump 强拆呼叫；SIP 进程重启 | references/capabilities/osip-sip-troubleshooting.md | references/capabilities/osip-codec-negotiation.md |
| OXE DM 与 8770 怎么选；DM profile 规划；8770 迁移 OXE DM；数据库恢复后终端拿不到配置 | references/capabilities/osip-dm-management.md | — |
| 配置话机监督代接；建寻线组；多终端同振；配可编程键；前缀激活业务 | references/capabilities/osip-sip-features.md | references/capabilities/osip-ales-provisioning.md |
| 准备实验环境；POD 预配置核对；运营商模拟器号码规则；实验外线打通 | references/capabilities/osip-lab-environment.md | — |

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

- 话务台坐席/ACD/呼叫中心、酒店全量业务（8008 例外）在 SIP 侧缺席或受限 → 声明形态边界，回 NOE 或改方案，不硬配
- 客户要照书直配真实运营商 → 停，先拿 TC2005 与运营商参数表再动手
- 版本低于特性门槛（R101.1 的 8443 mTLS、N4 的远程加密放行、N3 的 SSH 强制）→ 先核对版本再谈功能
- 涉及 RLAB/ITSP 实验环境搭建 → 参考 book/overview 环境区背景并声明实验口径，不虚构生产配置
- 用户数/并发超出许可与容量口径（177/345/430 锁、15000 用户/20000 设备、RP ≤500）→ 走扩许可或换方案，不硬撑
