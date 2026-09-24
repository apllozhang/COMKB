# 远程接入架构与 DMZ 双边缘（需求分类、组件分工、用例矩阵、DNS 双侧）

## R — 原文依据

> "Employees who benefit from an OTC client (PC/Mobile) must be able to connect remotely from the Internet to the OpenTouch system with full services"（p34）
> "* Reverse Proxy function can be delivered by OTSBC server; ** VPN access scenario that is a technological alternative"（p35）
> "Reverse Proxy … In charge of managing the HTTPs session to access the Telephony services … OTSBC: In charge of managing and securing the SIP session and the media streams (audio and video) based on RTP or SRTP"（p37）
> "N.U : Not Used (because no VoIP/video on this client); N.A : Not Applicable"（p82）

出处：OPENXTE225EN p33-46, p81-85, p121-127。

## I — 自述

三类远程接入需求决定方案边界：

1. 公司员工持 OTC 客户端从互联网全功能接入（话音/视频/IM/协作）
2. 全体员工（含无 OpenTouch 账号者）可远程使用 Web 协作
3. 外部伙伴/客户从互联网进会议与 Web 协作

总拓扑是 DMZ 双边缘：反向代理管 HTTPS/Web 服务（话音控制、目录、留言、协作/桌面共享），OTSBC 管 SIP 信令与 RTP/SRTP 媒体；VPN 在拓扑图上标为"技术替代方案"，全书不展开。五类过墙流量：话音 Web 服务、协作 Web 服务、SIP 信令、RTP 媒体、PSTN 话音流。

组件分工速记：

| 组件 | 职责 | 关键特性 |
|---|---|---|
| 反向代理（RP） | 远程客户端到话音 Web 服务的 HTTPS 会话 | 拓扑隐藏、认证（LDAP/RADIUS）、URL 改写/封禁、SSL 卸载；第三方产品 |
| OTSBC | SIP 会话与 RTP/SRTP 媒体的管理与保护 | DoS 防护、拓扑隐藏、TLS/SRTP 加密、QoS 与 CAC、NAT 穿越、紧急号码路由 |

客户端×边缘组件矩阵（查表依据，p40-42/p82）：

| 客户端 | 需 RP | 需 OTSBC | 说明 |
|---|---|---|---|
| OTC PC | 是 | 是 | 全功能（VoIP/视频/IM/桌面共享） |
| OTC PC One | 是 | N.U. | 无 VoIP/视频，SBC 用不上（非不支持） |
| OTC Web | 是 | — | 协作，仅需 RP |
| OTC WebRTC | 是 | 是 | 浏览器音视频 |
| OTC iPhone/Android | 是 | 是 | 带 * 仅音频无视频 |

DNS 内外分离：内部 DNS 把 OT/conference/SBC FQDN 解析到私网 IP（OTSBC 的 WAN 接入不需内部申报）；公共 DNS 把同一批 FQDN 解析到 RP/SBC 公网 IP；conference FQDN 内部解析到会议簇 IP。同一逻辑服务"内外两套名字+两套地址"。

## A1 — 书中案例

用例矩阵查表（p40-42/p82，讲义案例）：

1. 确定 user 类型：公司员工（OTC PC/One/智能手机）或外部来宾（OTC Web/WebRTC）
2. 查矩阵行：该客户端需要 RP 吗、需要 OTSBC 吗
3. 读符号：N.U.=该客户端无 VoIP 所以 SBC 用不上；N.A.=该组合不适用
4. 输出组件清单：如"OTC PC One 用户只需 RP，不占 SBC 资源"
5. 对照 DNS 布局（p43/p85）：内部用户走私网解析，场外用户走公共 DNS 到 RP/SBC 公网 IP

## A2 — 未来触发

使用情境：客户要开放远程办公；售前问"需要买/部署哪些边缘组件"；外部客户要进会议；规划 DNS/NAT；有人说"直接给每人发 VPN 就行"。

语言信号：远程接入 / remote access / DMZ / 边缘 / 双边缘 / 反向代理 / Reverse Proxy / OTSBC / SBC / VPN / 拓扑 / 用例矩阵 / 拓扑隐藏 / SSL 卸载 / 桌面共享 / DNS 解析。

与相邻能力区分：

- 动手签证书 → 证书与 PKI 能力
- 服务器侧申报动作 → OT 服务器侧设置能力
- 反代怎么装 → 反向代理部署能力

## E — 可执行步骤

输入契约：用户类型清单（员工/来宾、各端形态）、公网资源（可做 NAT 的公网 IP 与域名）、内外 DNS 控制权。

1. 按 p34-36 归类三类需求，确认是否含外部来宾（决定 conference 通道是否必选）。完成标准：需求清单带用户数与客户端形态
2. 查用例矩阵输出组件清单（RP 必须；有 VoIP 的端加 OTSBC）。完成标准：每类用户有明确的边缘组件行
3. 定反代路线倾向（内嵌 vs 独立）留待部署能力展开，此处只定"要不要兼任"。完成标准：拓扑图标注 RP 归属
4. 画 DNS 双侧表：每个公共 FQDN 两行（内部解析目标/公共解析目标）。完成标准：conference FQDN 在两列都有落点
5. 列端口与 NAT 规划口径：RP 侧公网 443 与 8016（EVS 通知）；OTSBC 侧 5261（OTC）、8061（WebRTC）、RTP/SRTP 7000-7499。完成标准：端口表带 NAT 公私 IP 对占位
6. VPN 诉求按"技术替代"口径说明：功能可行但非主推路线，书内不展开

判停点：

- 客户问 VPN 隧道/加密算法细节 → 停，书外内容，转客户网络规范
- 客户问并发容量/CAC 阈值 → 停，书内无数值（n30），指向 TC2639/8AL90065USAG 或 sizing 工具
- 公共 DNS 不在客户或自己控制下 → 停，先解决 DNS 归属再谈公共解析

输出契约：拓扑选型结论（双边缘组件清单）+ DNS 双侧解析表 + 端口/NAT 规划表。

## B — 边界

- VPN 全书仅标"技术替代方案"，无任何配置内容；不要把双边缘方案说成"唯一方案"，但按官方口径它是主路线（p35）
- 容量与体验数值全书缺位：CAC 只在 SBC 功能列表出现一次、无阈值；游牧池无算例；带宽无口径（n30，另见 needs-review nr-07）
- RP 是第三方产品（ALE 不提供）；OTSBC 为 ALE OEM（AudioCodes Mediant 平台）
- RP 由 OTSBC 兼任时，认证部分必须另配服务器（p37/p140，两处口径一致）
- 公共 DNS 归属（域名商/客户 IT）是原书未证明的假设；端口/IP 具体值均为实验口径（见 book/overview 环境区）
- 用例矩阵的 N.U. 与 N.A. 语义不可混用：OTC PC One 是"没有 VoIP 可保护"，别报成"不支持 SBC/加密"（n24）
