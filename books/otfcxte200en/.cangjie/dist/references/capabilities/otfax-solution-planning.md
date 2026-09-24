# OTFC 方案评估与部署规划（容量协议合规、架构拓扑、支持矩阵、入口设计）

## R — 原文依据

> "Dedicated server • Up to 15000 users • 30 ports ; Fully software-based • Fax over IP • SIP/TCP and SIP/TLS • T38 / SIP connection to OmniPCX Enterprise ; Fax transmission protocol: • T.38 … speed of up to 14.4kbps • G.711 • Speed of up to 33.8kbps"（p7）
> "Inbound routing methods •DNIS, CSID, ANI, DTMF"（p9）
> "Fax deletion options allow the system to be configured for zero retention if desired"（p6）
> "2 SIP gateways are configured on Fax Center • Sip private Trunks on OXE are necessary to support fax connection"（p36）

出处：OTFCXTE200EN p3-42。

## I — 自述

售前/规划阶段的三张底牌：

1. **容量与传输**：单专用服务器（物理或虚机）上限 15000 用户、30 端口；全软件实现（Fax over IP），SIP/TCP 与 SIP/TLS，经 T.38/SIP 连 OXE；T.38（含 Group 3）最高 14.4kbps，G.711 透传最高 33.8kbps
2. **收发接口与合规**：发送入口（邮件/Web/虚拟打印机打印/SendFAX 及 T.37 MFP）+ 全入口定时发送 + 按 Profile 闭锁；接收去向（邮箱 HTML/文本 + PDF/TIFF 附件、Web 界面、打印机、本地/共享文件夹）；入局路由四法（DNIS/CSID/ANI/DTMF）；合规卖点 GDPR/HIPAA/FERPA/SOX 语境、零保留、事件日志审计
3. **部署形态**：OTFC 可物理可虚拟（OTFC-V：虚拟化 + Windows Server）；与 OXE 共存但独立部署，传真流量与邮件流量分两路；多台 OXE 经 WAN 互联时 Fax Center 配多 SIP 网关按号码段分流，OXE 侧必须建 SIP private trunk
4. **支持矩阵**：Windows 64 位 Server 2022/2019/2016（含 IIS 10.0）；Hyper-V 三版 / VMware ESXi 6.5-8.0（vSphere、v-Motion、HA）；Exchange 2019/2016/2013、O365、SMTP 兼容

5. **客户端与光栅化**：Rasterizer 需本机 Office 2021/2019/2016（64/32 位）；工作站 Windows 11/10、终端服务器 2022/2019；Outlook "2022" 为原文笔误（以 Features List 为准）

## A1 — 书中案例

**双 SIP 网关号段分段**（p36，示例口径）：

1. Fax Center 配置 2 个 SIP 网关（Sip GW 1 / Sip GW 2）
2. GW1 对 OXE 1 的 IP 地址 1，承载传真号 1200-1500
3. GW2 对 OXE 1 的 IP 地址 2，承载传真号 3300-3800
4. OXE 侧为此建 SIP private trunk 支撑传真连接

**出呼路由两场景**（p37）：所有出呼走同一网关（如 GW1），或按收件人号码分流到对应网关；入呼按被叫号码分给对应用户。

## A2 — 未来触发

使用情境：客户问传真服务器能撑多少人；传真走什么协议速率多少；怎么和现有 OXE 对接；多分支多 PBX 怎么规划；合规投标要写零保留；现有邮件环境兼容吗。

语言信号：选型 / 容量 / 多少用户 / 多少端口 / T.38 / G.711 / 14.4k / 33.8k / FoIP / 合规 / GDPR / HIPAA / 零保留 / 拓扑 / 多网关 / 多站点 / SIP trunk / 虚拟化 / ESXi / Hyper-V / 支持矩阵 / Exchange 2016 / 入口 / DNIS。

与相邻能力区分：落地施工 → 首次交付与 SIP 通道集成能力；防火墙端口数值 → Features List（本卡只给已知三处：SIP UDP 5360、SMTP 25、LDAP 389）。

## E — 可执行步骤

输入契约：用户数与话务画像、现有 PBX（OXE 版本/冗余形态）、邮件环境（Exchange 版本或 SMTP）、虚拟化平台、合规要求清单。

1. 容量对答：单服务器上限 15000 用户/30 端口口径，结合话务画像评估端口余量。完成标准：容量结论含前提
2. 协议路径：默认 T.38/SIP；网络质量差场景对照 G.711 透传速率。完成标准：传输路径选型说明
3. 入口矩阵：按用户群体配四类发送入口与四类接收去向，确认定时发送与闭锁诉求。完成标准：入口清单获客户确认
4. 拓扑设计：单/多网关、多站点切分（Site 按公司/分支/部门）、号码段分流方案。完成标准：拓扑图与号段表
5. 支持矩阵核对：OS/虚拟化/邮件/客户端逐项对客户环境。完成标准：兼容性核对表
6. 合规条款映射：零保留、敏感文档路由、审计日志逐条对应客户要求。完成标准：合规应答表
7. 外置项清单：端口全表、45 格式明细、浏览器支持、服务器资源——全部标注"查 Features List"。完成标准：边界清单交付

判停点：

- 客户要逐项端口白名单 → 停，书内 p42 无数值，按 Features List 出数，只确认已知三处
- 客户环境不在支持矩阵内（如 Server 2012） → 停，查最新 Features List 与产品线现状，不按书内矩阵下硬结论
- 客户要求传真加密信令落地 → 停，SIP/TLS 仅为概览能力项，启用路径在书外，转产品安全文档
- 话务模型复杂（广播高频/大附件） → 停，书内无话务建模方法，sizing 转 ALE 售前工具与 Features List

输出契约：选型结论（容量/协议/入口/合规四段）+ 拓扑与号段规划表 + 兼容性核对表 + 外置文档清单（Features List/TC3048）。

## B — 边界

- 15000 用户/30 端口是单服务器上限口径；话务建模与性能调优书内缺席，引用数字必须带前提
- 服务器资源推荐表与端口使用表书内无数值（p38/p42 指针页），生产数值一律查 Features List
- "Outlook 2022" 为原文笔误（nr-02）；45 种文件格式与浏览器清单外置
- CSGD 缩写（生态图）书内未定义；DNIS/CSID/ANI 全称括注为推断
- 合规法规为原文列举语境，具体条款解读与认证口径在书外
