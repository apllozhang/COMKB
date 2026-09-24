---
name: ot-mobility-remote-worker
description: |
  OpenTouch MLE 移动化与远程工作者交付支持：DMZ 双边缘架构（反代+OTSBC）与 DNS/端口规划、证书策略与自建 CA 签发、OpenTouch 服务器侧远程访问申报（RP/OTSBC/DAS/ACS）、 OTSBC 部署与向导配置、反向代理两路线（内嵌 RP 与 Nginx）、OTC PC 两模式（multi-devices 与 Nomadic SIP）、OTC 智能手机开通（自动对象与 DISA/ARS 联动）、iPhone+ APNS 推送专项。 适用于把 OpenTouch 通信服务安全开放到互联网的部署、选型与排障问答；生产容量数值、iPhone 完整手工配置与正式 PKI 流程不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.ot-mobility-remote-worker
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# OpenTouch — 移动与远程办公 (Participant's Guide) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 容量与体验数值（CAC 阈值、并发用户规模、带宽、游牧池算例）——指向 TC2639、8AL90065USAG 或 ALE sizing 工具
- iPhone 完整手工配置（书内两处明示 not part of this lab，查 TC2639）与 APNS 证书 2022 后的续期机制
- 正式 PKI 流程、通配符证书合规性、生产安全基线（口令台账/SBC 加固/防火墙整站策略）
- 非 OpenTouch 平台与 OTES 旧代方案（OTES 自 OT 2.2 起不再是方案一部分）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 远程接入骨架是 DMZ 双边缘：反代管 HTTPS/Web 服务通道，OTSBC 管 SIP 信令与 RTP/SRTP 媒体；VPN 只是官方标注的技术替代方案
2. 证书是硬前提：远程访问必须 CA 签发，预载"通用证书"（security off）被官方明确反对；会议服务 FQDN 必须进反代与 OT 服务器证书的 SAN
3. DNS 内外分离：同一批 FQDN 内部解析到私网、公共 DNS 解析到反代/SBC 公网 IP；EVS 通知 URL 必须带 8016 端口
4. 客户端侧两步法：接入配置（公共 URL+凭证）加路由档案（从哪拨/路由到哪）；手机发起拨打永远本机发话，dial from 不影响
5. 版本分界：OTSBC 7.2 起可内嵌反代；OT 2.2 起 Nginx 必须 remoteworker.conf 与 conference.conf 同改；R2.6 起远程分机可做用户唯一设备
6. 实验环境口径：教材域名/公网/口令/号码仅限实验，生产全量替换；容量数值（CAC/并发/带宽）全书缺位

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 规划远程接入拓扑；远程用户要哪些边缘组件；反向代理和 SBC 怎么分工；DNS 内外怎么解析；plan remote access topology | references/capabilities/otm-dmz-security-channels.md | references/capabilities/otm-certificate-pki.md |
| 远程访问证书怎么选；签发服务器证书；自建 CA；证书导入与部署；generate certificate CA | references/capabilities/otm-certificate-pki.md | references/capabilities/otm-ot-server-settings.md |
| 申报反向代理；申报 OTSBC；配置 DAS 规则；会议服务 FQDN 与 rehost；declare reverse proxy OpenTouch | references/capabilities/otm-ot-server-settings.md | references/capabilities/otm-certificate-pki.md、references/capabilities/otm-reverse-proxy.md |
| 部署 OTSBC；配置 OTSBC 向导；OTSBC 许可与证书；SIP 接口 TLS 上下文；deploy OTSBC | references/capabilities/otm-otsbc-deployment.md | references/capabilities/otm-certificate-pki.md、references/capabilities/otm-reverse-proxy.md |
| 部署内嵌反向代理；部署 Nginx 反向代理；反代路线选型；反代 LDAP 认证；nginx reverse proxy OpenTouch | references/capabilities/otm-reverse-proxy.md | references/capabilities/otm-otsbc-deployment.md |
| 配置 multi-devices 副设备；配置 Nomadic SIP；游牧池规划；OTC PC 远程办公；OTC PC secondary device | references/capabilities/otm-otc-pc-modes.md | references/capabilities/otm-client-access-profiles.md、references/capabilities/otm-lab-dialtest.md |
| 配置 OTC 智能手机；关联手机到用户；自动对象核验；远程分机 RE 配置；smartphone dual mode | references/capabilities/otm-smartphone-provisioning.md | references/capabilities/otm-iphone-apns.md、references/capabilities/otm-smartphone-modes.md |
| iPhone 收不到来话；APNS 防火墙端口；kamailio-wasp 维护；iPhone+ SBC 端口；iPhone push notification | references/capabilities/otm-iphone-apns.md | references/capabilities/otm-smartphone-provisioning.md |
| 客户端怎么接入；路由档案配置；OTC Web 怎么进会议；dial from 不生效；remote access profile | references/capabilities/otm-client-access-profiles.md | references/capabilities/otm-otc-pc-modes.md |
| 手机没流量怎么办；WiFi 和 4G 下什么功能可用；Android 无 SIM；回落模式；smartphone connectivity modes | references/capabilities/otm-smartphone-modes.md | references/capabilities/otm-smartphone-provisioning.md |
| 部署 OVF 虚机；vSphere 还是 web client；ESXi 导入 OVA；deploy OVF VMware | references/capabilities/otm-vmware-ovf.md | references/capabilities/otm-otsbc-deployment.md |
| 实验环境是什么；拨测号码怎么变换；主叫显示是什么；SIP 模拟器；dial test numbering | references/capabilities/otm-lab-dialtest.md | references/capabilities/otm-otc-pc-modes.md |

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

- 需要生产容量数值或 sizing 结论 → 明确指向 TC2639/8AL90065USAG/sizing 工具，不以实验口径搪塞
- 需要 iPhone 手工配置清单 → 指向 TC2639（TC2341en 辅助），不虚构书内步骤
- 涉及 VPN 隧道/加密算法等替代方案细节 → 声明书内仅标"技术替代"，转客户网络规范
- 版本分界判定（OTSBC 7.2、OT 2.2、R2.6）→ 按系统实际版本区分配法，不把新配法套到老系统
