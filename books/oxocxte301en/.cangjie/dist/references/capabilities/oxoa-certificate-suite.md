# 证书与加密传输（数字证书四类、DTLS、SIP 中继 TLS/SRTP）

## R — 原文依据

> "Server Certificate … HTTPS (OMC, WebDIAG APIs) • SIP trunk with SIP-TLS … 2048 (d) 4096 … Public Server certificate … Issuer External PKI … DTLS OXO certificate … Port 7780"（p346, p351-353）
> "Roll back to previous release after a migration to R6.2 … switch again to 2K certificates (Via WebDIAG) and then roll back."（p357）
> "DTLS (TLS 1.2) secures the signaling. Voice packet are in clear mode (Not SRTP)"（p353）
> "Up to 300 DTLS connections • License free … Available only with platform OXO Connect Evolution"（p360）
> "TLS Authentication model: Server Provided Certificate Authentication or Mutual Authentication • Cryptographic suites: AES Counter Mode [128 and HMAC SHA1 80] [256 and HMAC SHA1 80] …"（p367）
> "WebRTC GW alone 20 calls max. NA … SIP PROXY alone NA 20 calls max. … WebRTC GW + SIP PROXY 20 calls max. 20 calls max."（p375）

出处：OXOCXTE301EN p339-378。

## I — 自述

证书与加密分三层：证书体系（身份）、DTLS（话机信令）、TLS/SRTP（中继）。

**证书四类 + 端口矩阵**（p346-356，WebDIAG 为管理主接口）：

| 证书 | 身份/用途 | 端口 | 签发 | 密钥 |
|---|---|---|---|---|
| Server Certificate | LAN 私有身份（HTTPS + SIP-TLS） | 443、30443 | 自签默认或外部 PKI | 2048 默认/4096 可配 |
| Public Server certificate | WAN 公共身份（SIP-TLS + HTTPS） | 50443 | 仅外部 PKI（默认未定义） | 2048/4096 |
| DTLS OXO certificate | NOE 话机 DTLS | 7780 | 自签 4096 不可配或外部 PKI | 4096 |
| Generic / OXO HAN | ALE SIP 话机简易部署 / Wi-Fi AP | 10443 / 11443 | 自签（Generic 2048 不可配） | HAN R6.2 起 4096 |

**升级路径**：

- 自签 2 步：CA 再生成，然后服务器证书再生成（两者密钥长度必须一致；重启仅 OCE）
- 外部 PKI 4 步：CA 再生成、CSR（PKCS#10）生成下载、外部 CA 签、导入安装；Public Server 3 步；DTLS 自签 1 步/外部 3 步
- R6.2 起 OpenSSL V3 + 4K 支持；4K 存储格式不同——回滚旧版本前必须先经 WebDIAG 切回 2K，否则 OMC 报错（n41）

**DTLS**（p359-364）：

- 只加密 ALE VoIP 话机信令（TLS 1.2），语音包仍明文（非 SRTP）；300 连接、免 license、仅 OCE、默认激活
- 两模式：Generic（零接触，跨 OCE 免清除移动）/ Specific（锁定端点）
- 跨系统移动（OXO↔OXE）必须清 TrustList：部分清除（OMC）/完全清除（WebDiag recovery token）/专用 token（ALE 支持）

**SIP 中继 TLS/SRTP**（p365-378）两实现：

| 实现 | 平台 | 容量 | 要点 |
|---|---|---|---|
| OCE 原生 | OCE | 免 license | 网关 Security tab + Topology（静态 NAT）+ SIP Trunk 信令端口 5061；四套 AES-CTR 套件 |
| OCE-FE SIP PROXY | OCO 等无原生平台 | GW 与 PROXY 各 20 通话 | 认证/DNS/套件/静态 NAT 四项全局共享；SIPS URI 不支持；ETH1 不走 SIP |

## A1 — 书中案例

**证书章为讲义形态（无实验），关键行为口径**（p339-378）：

1. 改接入路由器外部地址或 LAN IP 会重建自签证书，已信任客户端要重新信任（p327）。
2. 冷复位与 LoLa 不清证书（p327）——净化转售设备需另行处理（n40，推断）。
3. 双向认证从旧版本迁移启用时证书必须再生成（p373 note）。
4. TLS/SRTP 模式下 Direct RTP 不可用，媒体在 OCE GW 侧终结（p368）。
5. 私网两 OCE 互联：一端自动做 TLS Server、另一端做 Client；对端仅 TLS client 时须停用双向认证（p369）。

## A2 — 未来触发

使用情境：运营商要求加密中继；话机要 DTLS；证书快过期或要换企业 PKI；升级 4K 后想回滚版本；话机跨系统搬过去注册不上；OCO 老平台怎么接加密中继；双向认证握手失败。

语言信号：证书 / certificate / PKI / CSR / 自签 / 4096 / 4K / 2048 / 2K / 回滚 / DTLS / TrustList / TLS / SRTP / 5061 / 加密中继 / OCE-FE / SIP PROXY / 双向认证 / mutual authentication。

与相邻能力区分：系统密码与加固归安全加固能力；SIP 中继本身的注册与路由归 SIP 组网能力；WebDIAG 操作界面归维护工具能力。

## E — 可执行步骤

输入契约：平台形态（OCE/OCO/PowerCPU EE）、软件版本（是否 R6.2+）、PKI 流程（有无企业 CA）、运营商加密参数（认证模型/套件/端口）。企业 PKI 流程未定 → 判停先对齐客户 PKI 管理方。

1. 盘点证书：WebDIAG/Certificates 核当前四类证书的密钥长度与签发者。完成标准：证书台账
2. 签发路径：自签走 2 步（CA 与证书，长度一致）；外部走 4 步（CA、CSR、外部签、导入）。完成标准：证书就位
3. 重启核验：OCE 重启后在 WebDIAG 看 current certificate。完成标准：新证书生效
4. （DTLS）系统级 OMC/Security/DTLS Encryption + 每用户 IP-SIP parameters；话机确认钥匙图标。完成标准：信令加密上线
5. （TLS/SRTP）网关 Security tab 启用并选认证模型与套件；Topology 配静态 NAT；信令端口 5061。完成标准：加密中继注册通
6. （OCO 平台）改走 OCE-FE SIP PROXY：WebDIAG Settings 配接口/DNS/拓扑/认证/套件，ALE CC 注册后可用。完成标准：代理转发通
7. 回滚预案：升 4K 的站点把"WebDIAG 先切回 2K 再回滚"写进回滚手册（n41）。完成标准：预案成文
8. 移动场景：跨系统搬话机前按三法之一清 TrustList。完成标准：话机在新系统注册

判停点：

- 运营商要求 SIPS URI → OCE-FE 不支持（n43），换方案或协商
- 对端仅 TLS client 且客户不接受停用双向认证 → 安全等级下降需书面确认（n44）
- 4K 升级后直接回滚 → 禁止：先切 2K，否则 OMC 报错（n41）
- OCO 平台想原生开 TLS → 平台无此能力，只有 OCE-FE 代理一条路（p375）

输出契约：证书台账与签发记录 + DTLS/TLS 部署清单 + 容量口径（FE 各 20 通话）+ 回滚预案。

## B — 边界

- DTLS 只保信令不保语音（n62）：合规对话中"话机加密"与"语音机密性"必须分开表述，语音机密走中继 SRTP
- OCE-FE 四项配置全局共享：不同网关要不同套件做不到；OCE FE 无 PBX 能力、license 免费但需硬件（p375-378）
- 企业 PKI 的申请审批流、证书生命周期管理在书外（原书只给系统侧操作）
- Generic 证书覆盖 8001/8008CE/8008G/8028 等清单见 p356；NOE 话机 DTLS 支持清单见 p353
- 运营商 TLS 参数（套件/端口/认证）在书外，按运营商合同取值；实验口径不适用生产
