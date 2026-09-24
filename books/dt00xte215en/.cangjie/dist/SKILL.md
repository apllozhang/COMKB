---
name: omniswitch-lan-access
description: |
  OmniSwitch R8 接入/汇聚交换机的交付与运维支持：AAA 登录与管理面加固、Lightning Config 快速开局、配置保存/认证/回滚生命周期、 Virtual Chassis 堆叠、VLAN/802.1Q 与 VLAN 间路由、链路聚合/STP/DHL 冗余、三层服务（DHCP/Loopback0/静态路由）与 VRRP 网关冗余、 QoS/ACL 统一策略、Access Guardian 准入、诊断八件套、LLDP-MED 语音与 PoE、软件升级与 Auto-Fabric 零触开局、Fleet/OST 工具面。 适用于 OmniSwitch LAN Access R8 的配置、组网、排障与方案落地问答；型号相关规格数值、升级操作步骤、RADIUS 服务器侧配置不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.omniswitch-lan-access
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
# OmniSwitch LAN Access Switching (Participant's Guide, Edition 23) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 型号相关规格数值（镜像会话数全矩阵、PoE 预算、每型号 VC 上限细节）——原书外置到 Specification Guide/datasheet
- 软件升级操作步骤与前置固件顺序——原书 p533 明示按 AOS Release Notes 执行
- RADIUS/LDAP 服务器侧部署（用户库、证书、TLS 开启）与 vcboot.cfg 模板设计——书外依赖
- 动态路由协议（OSPF/BGP）与组播协议的完整配置——本书仅触及 Auto-Routing 与 Loopback0 通告口径
- R-Lab 远程实验环境搭建与产品选型（datasheet 域）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 配置可靠性模型是三目录：running(RAM) 经 write memory 到启动目录、经 copy running certified / flash-synchro 固化认证基线；重启按内容异同回 certified 或 running，reload all 无条件回 certified
2. 一切管理入口是 AAA：七类服务各自认证链（本地库或 RADIUS/LDAP，exit-on-fail 语义），管理面收缩靠 ASA 限源、禁服务、会话参数与 SSH 强加密
3. 组网自下而上：VLAN 三入口（静态/UNP 分类/802.1Q）> 一个 IP 接口即激活路由 > 冗余四件套（LACP/STP/DHL/VRRP）按场景二选一，DHL 与 STP 不能混用于同一链路
4. QoS/ACL/PBR/镜像共用一个 policy 引擎：condition+action+rule 且 qos apply 才生效；默认 disposition 为 accept（不匹配即放行）
5. Access Guardian=UNP+RADIUS：Filter-Id 回传档案名决定 VLAN 与策略；服务器不可达走 auth-server-down 降级，无 MAC 登记一律 Block
6. 堆叠即一台交换机：ISIS-VC 选举（优先级>运行时长>最小 ID>最小 MAC），分裂防护靠 EMP 带外 RCD 与带内 VCSP，升级走 ISSU 滚动
7. 实验环境口径：教材地址/账号/实验数值仅限实验；型号规格（镜像会话数、PoE 预算、VC 上限全矩阵）以 Specification Guide/datasheet 为准

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 配置交换机登录认证；加固交换机管理面；管理本地用户与密码策略；WebView 或 SSH 登不上；switch management access | references/capabilities/swl2-aaa-hardening.md | references/capabilities/swl2-lightning-config.md |
| 新交换机快速开局；Lightning Config 向导；导入开局模板；lightning config onboarding | references/capabilities/swl2-lightning-config.md | references/capabilities/swl2-config-lifecycle.md |
| 保存交换机配置；配置回滚；配置备份恢复；show running-directory 判读；write memory certified | references/capabilities/swl2-config-lifecycle.md | references/capabilities/swl2-virtual-chassis.md |
| 组建 Virtual Chassis 堆叠；堆叠主备与选举；堆叠分裂防护；ISSU 滚动升级；virtual chassis vfl | references/capabilities/swl2-virtual-chassis.md | references/capabilities/swl2-config-lifecycle.md、references/capabilities/swl2-upgrade-autofabric.md |
| 创建 VLAN 与挂端口；802.1Q 打标互联；配置 VLAN 间路由与网关；UNP 动态 VLAN 分类；vlan trunk tagging | references/capabilities/swl2-vlan-routing.md | references/capabilities/swl2-access-guardian.md |
| 配置链路聚合；聚合负载分担与 hash；配置 STP 与根桥；1x1 负载分担；DHL 双活上行；link aggregation lacp stp | references/capabilities/swl2-link-redundancy.md | references/capabilities/swl2-vlan-routing.md |
| 配置 DHCP 中继；配置 Loopback0 与服务源地址；静态路由与主备默认路由；配置 VRRP 网关冗余；dhcp relay vrrp | references/capabilities/swl2-l3-services.md | references/capabilities/swl2-vlan-routing.md、references/capabilities/swl2-link-redundancy.md |
| 配置 QoS 策略与限速；auto-QoS 话机优先级；配置 ACL 过滤；用户口安全与防欺骗；qos acl policy rule | references/capabilities/swl2-qos-acl-policy.md | references/capabilities/swl2-access-guardian.md |
| 部署 802.1x 接入认证；MAC 认证与哑设备准入；认证后动态下发 VLAN 策略；RADIUS 降级预案；access guardian unp radius | references/capabilities/swl2-access-guardian.md | — |
| 查看交换机日志；端口镜像与抓包；CPU 内存健康查看；审计配置变更记录；switch diagnostics troubleshooting | references/capabilities/swl2-diagnostics.md | — |
| 配置 LLDP 与邻居发现；IP 话机自动入语音 VLAN；PoE 预算与优先级管理；Fast PoE 与延迟供电；lldp med voice vlan poe | references/capabilities/swl2-lldp-poe.md | — |
| 选择升级版本与通道；U-boot 与底层固件风险；Auto-Fabric 零触开局；首启提示与 RCL；software upgrade zero touch | references/capabilities/swl2-upgrade-autofabric.md | — |
| 资产与维保合规报表；Fleet Supervision 开通；安装使用 OST 2.0；PoE 设备一键修复；fleet supervision ost tooling | references/capabilities/swl2-fleet-tools.md | — |

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

- 需要型号相关规格数值或全量命令参数 → 明确指向 Specification Guide / CLI Reference，不以实验口径或记忆值搪塞
- 需要升级操作步骤 → 指向 AOS Release Notes；U-boot/ONIE/FPGA/CPLD 升级提示失败即 RMA 的风险边界
- 涉及 RADIUS 服务器侧建设或割接治理流程（变更窗口/审批）→ 声明超出原书范围，不给编造步骤
- 版本敏感参数（镜像会话数 2 vs 4、LLDP-MED 标记值、console 速率）→ 按 needs-review nr-01/02/04 双口径如实说明，以规格指南与实测为准
