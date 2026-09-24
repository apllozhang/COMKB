---
name: oxe-native-encryption
description: |
  OXE 加密解决方案（FSNE）的交付与运维支持：证书与信任链全生命周期（PKI 三模式、PKCS#7 五步闭环、CTL/TOFU）、系统参数与 lanpbx.cfg 开通、DTLS/SIP TLS 验证排障与维护闭环、 SIP TLS 扩展与中继（OTSBC+OXE 双侧）、EEGW/NSP 大容量部署、ABC-F 网络加密、mTLS 双向认证与版本限制处置。适用于 OXE R101.x 信令（DTLS/TLS 1.2/IPSec）与媒体（SRTP） 加密的配置、选型、排障与验收问答；企业 PKI 运营治理、EEGW VM 规格等生产化数值不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.oxe-native-encryption
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# OmniPCX Enterprise — Native Encryption (Participant's Guide, Edition 05) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 企业 PKI 运营治理（CA 私钥保管、CRL/OCSP 基础设施、审批流程）——原书只有概念页，签发环节在客户 CA 规程
- EEGW VM 的 CPU/内存规格与压测口径（S.O.T. 仅按最大用户数 Sizing）；trunk/EEGW 侧抓包位置与 SIP TLS 解密
- 真实运营商 TLS 对接参数与 SBC 型号差异（实验用 ITSP2 模拟器与 OTSBC）；SIP TLS with SSM 与 IPv6 场景（不兼容）
- 课程评估/RLAB 平台运营等教学基础设施操作细节

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 加密由 Call Server 强制执行：NE 开启后 IPMG 与 PCS 一律加密，端点按用户选项逐台加密，trunk/ABC-F 链路两端能力不匹配即退出服务
2. 信任锚是 CTL：端点用 CTL 验证 CS 身份；获取走 lanpbx.cfg 自动推送（首连 TOFU）或手工预置；CA 更新必须立即重生成 lanpbx+重启+重做 PCS 证书
3. 私钥尽量不出端点：PKCS#7 路线（CSR 在实体上生成、外部 CA 只回签证书）是推荐主线；PKCS#12 私钥搬家且 SAN 手工易错，仅端点证书场景
4. 容量分界 1500/15000：内嵌 EGW 承载 1500 并发 DTLS/TLS 会话以内，超出强制 EEGW（每 CS 一台 VM，连带 CS 重启风险）
5. 媒体加密=信令加密×参数叠加：SIP TLS 只管信令，SRTP 要求系统 NE 与网关 RTP/SRTP 参数同时开启；端到端任何一环缺失即明文
6. 实验环境口径：教材密码、账号、网段、许可值仅限实验；所有菜单路径为 netadmin/lanpbxbuild/WBM 导航坐标

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 选择 PKI 模式与证书格式；生成 CSR 并导入签发证书；规划 CTL 分发与 TOFU；证书备份与 CA 更新；generate CSR import certificate OXE | references/capabilities/enc-certificate-trust-chain.md | references/capabilities/enc-native-encryption-bringup.md、references/capabilities/enc-mtls-endpoint-authentication.md |
| 启用加密解决方案系统参数；按用户开启加密；生成维护 lanpbx.cfg；选择 SRTP cipher suite；enable native encryption OXE | references/capabilities/enc-native-encryption-bringup.md | references/capabilities/enc-certificate-trust-chain.md、references/capabilities/enc-dtls-verification-maintenance.md |
| 验证加密是否生效；处置加密解决方案事件；备份证书；抓包证明媒体加密；cryptview ippstat troubleshooting | references/capabilities/enc-dtls-verification-maintenance.md | references/capabilities/enc-native-encryption-bringup.md |
| 启用 SIP 扩展 TLS 加密；排查 SIP TLS 注册失败；验证 SIP 媒体加密；sipmotor TLS 5061 SEPLOS | references/capabilities/enc-sip-tls-endpoints.md | references/capabilities/enc-native-encryption-bringup.md、references/capabilities/enc-eegw-deployment.md |
| 配置加密 SIP 中继；配置 OTSBC TLS context；验证中继 SRTP；安全停用加密解决方案；OTSBC SIP TLS SRTP trunk | references/capabilities/enc-sip-trunk-tls.md | references/capabilities/enc-sip-tls-endpoints.md、references/capabilities/enc-eegw-deployment.md |
| 部署外部加密网关 EEGW；声明 SIP Translator NSP；用 S.O.T. 生成 EEGW VM；迁移内嵌 EGW 到 EEGW；EEGW NSP deployment capacity | references/capabilities/enc-eegw-deployment.md | references/capabilities/enc-certificate-trust-chain.md、references/capabilities/enc-sip-trunk-tls.md |
| 启用节点间链路加密；部署内部 PKI 双节点；规划 hybrid/direct 拓扑；验证跨节点加密；ABC-F IPsec link encryption | references/capabilities/enc-abcf-network-encryption.md | references/capabilities/enc-certificate-trust-chain.md |
| 启用双向认证 mTLS；部署端点证书；处置 1024 位证书设备；调整 SSL security level；mutual TLS authentication endpoint certificate | references/capabilities/enc-mtls-endpoint-authentication.md | references/capabilities/enc-pki-workshop-xca.md |
| 部署 PCS 加密救援；做 PCS 断网演练；PCS certificate pcscopy | references/capabilities/enc-pcs-failover.md | — |
| 用 XCA 制作根 CA；签发 CSR 与端点实体；转换证书格式；XCA sign CSR root CA | references/capabilities/enc-pki-workshop-xca.md | — |
| 加密语音信箱与录音；评估 VAA/DC 加密代价；启用 HTTPS 安全下载；4645 VAA recording encryption | references/capabilities/enc-application-encryption.md | — |
| 搭建加密实验 POD；切换网络实验室拓扑；RLAB pod ITSP2 setup | references/capabilities/enc-lab-environment.md | — |

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

- 需要企业 PKI 运营或真实 CA 签发排期 → 明确指向客户 CA 规程，不以实验"秒签"口径搪塞
- 站点要求 SIP TLS with SSM、IPv6 或第三方 SIP 话机加密 → 原书明确不兼容，声明边界不硬配
- EEGW VM 规格与容量规划超出"最大用户数"口径 → 指向 OXE 安装文档与压测依据
- 证书吊销（CRL/OCSP）执行、集中监控/SIEM 集成 → 原书无操作实验，转客户安全方案
