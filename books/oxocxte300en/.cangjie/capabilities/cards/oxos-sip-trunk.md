# 公共 SIP 中继（网关配置 / Profile 导入 / 注册验收）

## R — 原文依据

> "OMC/External Lines/SIP/SIP Gateway/ • Create a new one • These infos are given to the client by the public provider"（p208）
> "The following setting can only be configured after filling in the DNS tab!"（p233）
> "Put the bandwidth at 5 minimum calls in order to allow external calls"（p234）
> "OMC/History and Anomalies/History Table Message displayed: SIP registration success"（p240）
> "For a complete list, refer to the technical communication: TC1284 Public SIP Trunking Interoperability and Technical Support procedure"（p199）

出处：OXOCXTE300EN p197-242（SIP 拓扑讲义、网关配置讲义与 20 页实验、Profile/Easy Connect）。

## I — 自述

公共 SIP 中继是局外通话主通道，配置分周边四项+网关本体：

- 周边四项：默认网关指向 CE（OMC/Hardware and Limits/LAN/IP Configuration）、安装号（OMC/Numbering/Installation Numbers，SIP 默认规范格式 +国际码+城际码+安装号+DID）、DDI 段（Public Dialing Plan）、VoIP 接入与中继组（List of Accesses/List of Trunk Groups，Public 属性+通道数+链路类别）
- 网关九页签（OMC/External Lines/SIP/SIP Gateway）：General（索引/名称/号码格式）、DNS（DNS A）、Domain Proxy（Target/Local 域、Realm、Outbound Proxy——填 DNS 后 IP 类型自动 dynamic）、Registration、Media（RTP Direct、带宽=并发数）、Identity（RFC3325）、Protocol、Topology（NAT、ETH0/ETH1）、Security（SIP 流加密）
- 顺序依赖两条：DNS 页签先于 Outbound Proxy（n13）；网关建好后必须回填 VoIP 接入的 Gateway index，漏回填=不注册不呼出（n42）
- 并发口径：IPBox 120、PowerCPU EE+Armada64 至 76（默认 16）；Media 带宽低于并发需求会拒呼（n14）
- 提速路径：过 TSS 认证的运营商可用 Profile 导入（TC1994）；Cloud Connected 系统可用 Easy Connect 网页选 Profile 少量参数完成全套
- ARS 补充：按国家补短号与紧急号码（法国典型四行：0 开头/紧急 emerg/3 开头/1 开头）——实验刻意跳过，照抄实验配置上生产会漏紧急呼叫路由（n12，合规级风险）

## A1 — 书中案例

**SIP 网关配置实验**（p223-242，ITSP1 模拟器，实验口径）：

1. 前置核对：LAN IP、DNS、DHCP 池（改后 Reset OXO）
2. 编号计划：DDI 41100-41199、话务员 41000、安装号 210P41000
3. VoIP 接入：建 8 通道 Public 接入，Gateway index 暂空
4. 中继组：VoIP 接入加进主中继组，Link-Cat. 调整允许外呼
5. 网关 General：Index 1、ITSP1G1、号码格式 canonical、拨号结束表
6. DNS 页签：DNS A=192.168.1.250
7. Domain Proxy：域与 Realm=sip.itsp1.fr、Outbound Proxy=gateway1.itsp1.com
8. Registration：勾 Registration requested、Registrar=sip.itsp1.fr
9. Media：勾 RTP Direct、带宽至少 5 通话
10. Identity 启用 RFC3325；Topology 选 ETH0；Security 不加密（OCE 默认）
11. SIP 账户：Login/密码/注册用户名=pbxP、关联网关 ITSP1G1
12. 回填：List of Accesses 把网关联到 VoIP 接入
13. 验收：History Table 显示 SIP registration success；拨 DDI 与公共号双向可通
14. 抓包：Webdiag → TCP Dump 选 SIP，停止后自动生成文件，Wireshark 分析可交技术支持

## A2 — 未来触发

使用情境：新站点接运营商 SIP；注册成功但打不出/打不进；换运营商迁移配置；客户要求免手工配置；生产补紧急呼叫路由。

语言信号：SIP 中继 / SIP 网关 / SIP Gateway / Outbound Proxy / Registrar / RTP / 带宽 / 注册 / SIP registration / Profile / Easy Connect / ARS / 紧急号码 / DDI / 安装号。

与相邻能力区分：出局权限（谁能拨什么）→ 呼入分发与闭锁能力；Rainbow 路由的 ARS 行 → Rainbow 集成能力。本能力到"注册成功+双向拨测通过"为止。

## E — 可执行步骤

输入契约：运营商参数表（域/代理/Registrar/账号/号码格式/通道数）、网段规划、许可通道数。生产运营商未过 TC1284 兼容清单 → 判停先与 ALE 确认支持口径。

1. 周边配置：LAN 网关/安装号/DDI/VoIP 接入与中继组。完成标准：接入已建且 Link-Cat. 允许外呼
2. 建网关 General+DNS。完成标准：DNS A 保存成功
3. Domain Proxy：域/Realm/Outbound Proxy（必须在 DNS 之后）。完成标准：IP 类型 dynamic
4. Registration/Media/Identity/Protocol/Topology/Security 逐页签按运营商参数填。完成标准：带宽≥并发需求
5. SIP 账户：三元组+关联网关索引。完成标准：账户挂上网关
6. 回填 Gateway index 到 VoIP 接入。完成标准：接入-网关-账户三点成链
7. 验收：History Table 出现 SIP registration success，双向拨测。完成标准：注册+呼出+呼入三项通过
8. （生产）按国家补 ARS 短号与紧急号，编辑 Emergency Numbers 清单。完成标准：紧急拨测按当地规范执行
9. （可选提速）Profile 导入或 Easy Connect，后续修改仍走 OMC

判停点：

- 注册失败 → 按 DNS、Outbound Proxy、账户、Gateway index 回填的顺序排查，不要乱改页签
- 外呼被拒 → 查 Media 带宽、中继组 Link-Cat.、闭锁三层（转闭锁卡）
- 运营商参数与书内实验不同属正常——实验表仅教学约定，生产以运营商 TC 为准
- 客户要 TLS/SIPS 加密 → 书内只有不加密实验口径，按运营商与 TC1284 核对（n15，推断性结论）

输出契约：注册成功的 SIP 中继（参数表归档）+ 拨测与抓包记录。

## B — 边界

- 全部实验值（ITSP1/账号/号码/密码 alcatel）为教学约定，生产严禁沿用（n44）
- 运营商选型、兼容性与支持流程以 TC1284 为准；Profile 机制以 TC1994 为准
- SIP 流加密生产要求在 Security 页签之外（书外核对，n15）
- 短号与紧急号码的实验跳过是合规级边界——上生产必须补 ARS（n12）
- Media 带宽同时受许可通道与 DSP 通道上限约束（p05/p201）
