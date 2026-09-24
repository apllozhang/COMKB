# DIGEST — OmniPCX Enterprise 加密解决方案 集成精华长文

> 源：ENTPXTE421EN Edition 05（410 页）· 文档整理入库 · 2026-09-24
> 定位：10 分钟建立 OXE 加密解决方案（FSNE）的全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

OmniPCX Enterprise 的加密解决方案（Native Encryption，简称 FSNE）是 OXE 内置的信令与媒体加密能力：**纯软件、零硬件 footprint**，靠数据库配置+软件许可（#424/#359）激活，全称 Full Software Native Encryption。

信令走 DTLS 1.2（NOE 侧）、TLS 1.2（SIP 侧）、IPSec（ABC-F 节点间），媒体走 SRTP。

加密由 Call Server 强制执行：开启后 IPMG 与 PCS 一律加密，端点按用户选项逐台开启，trunk/ABC-F 链路两端能力不匹配就直接退出服务——系统不允许"半吊子"状态静默存在。

整本教材就是一条交付主线：**证书就位、参数与 lanpbx.cfg、DTLS/SIP TLS 端点、验证排障、中继与扩容、网络化与双向认证强化**。先证书后开关、先单机后网络。

## 二、证书是全书的钥匙

- **PKI 模式三选一**：内嵌 CA（一键自签，最快）、PKCS#12（私钥在 CA 生成后搬运，仅端点场景）、PKCS#7（CSR 在实体上生成、外部 CA 只回签证书——私钥不出机、SAN 自动，**推荐主线**）。
- **五步闭环**：netadmin 11.9.1.2 生成 CSR、外部 CA 签发、11.9.1.4 导入、11.9.1.8 核验、10.2 复制 twin，再执行 dhs3_init -R NGINX。
- **命名规则**：板卡/话机/软话机实体证书 CN=设备 MAC；CS/PCS 证书 CN=OXE FQDN；节点证书 CN 恒为节点 FQDN。
- **CTL 分发两条路**：打进 lanpbx.cfg 自动推送（首连走 TOFU），或客户拒绝 TOFU 时手工预置/SCEP/EST。CA 更新的连锁义务：立即重生成 lanpbx+重启+手工重做 PCS 证书。
- **续期自动化分工**：SCEP 管话机（老旧，HTTP+共享密钥）、EST 管 IPMG（RFC7030，自动续期，事件 5779/5780）、ACME 只管 WBM 证书且须本地 CA——Let's Encrypt 等公网 CA 因 HTTP-01 需公网可达而不可用。

## 三、容量与端口，五个先记住的数字

| 数字 | 含义 |
|---|---|
| 1500 / 15000 | 内嵌 EGW 承载 1500 并发 DTLS/TLS 会话以内；超出强制 EEGW VM（每 CS 一台，上限 15000） |
| 32643 | DTLS 默认端口（lanpbx.cfg 的 DTLS_PORT） |
| 5061 / 6261 | SIP TLS 服务器认证端口 / 双向认证端口（本地网关两参数，四组合） |
| 60→45、60→30 | AES-256 模式下 GD4/GD-XL 与 INTIP3 的压缩器降额；GD3 禁用 AES-256 必须换 GD4 |
| 7300 天 | 内嵌 CA 自动生成的证书/私钥有效期（约 20 年） |

会话计数公式：受保护端点报价数 + 3×(GD4/GD-XL/GD3/INTIP3B/OXE-MS) + 3×外部 SIP 网关 + 3×节点数。许可 #424 管系统 DTLS/TLS 会话总数、#359 管并发 SIP TLS 通信，两个维度分开算。

## 四、三条实验线的骨架

1. **DTLS 主线**（单机）：证书先行；Native Encryption 参数（IPDSP 站点锁定 SRTP Authenticated）；用户级部分加密；lanpbxbuild 签名（duplication 只能在 main 跑）；重启后用 cryptview/ippstat/twin 验证；事件 5991-5995 巡检；证书备份。
2. **SIP TLS 线**：SIP 参数三件套（TLS signaling/SRTP offer answer/Loose Route=False）、用户开加密、motortrace 看 X-ALE-CALL-ENCRYPTED。
3. **中继线**（加在 SIP TLS 之上）：SBC 侧配 TLS context（TLSv1.2/DH 2048）、证书、Proxy Set 5061/TLS、Media Security。验收总纲：**信令不等于媒体**，SRTP 要系统 NE 与网关 RTP/SRTP 参数同时开启。
4. **扩容与网络线**：EEGW 部署六步（声明、防火墙、证书、lanpbx 指向 EEGW、VM、下载证书）；S.O.T. 生成 VM（仅 Chrome/Firefox，首登 letacla1 立即改密）；ABC-F 链路参数两端同值且须链路 DOWN 才能改；mTLS 激活后全员（含明文用户）必须有证书。

## 五、排障与验收速查

| 症状/需求 | 第一抓手 |
|---|---|
| 系统整体加没加密 | cryptview（System is DTLS secured、EGW 内/外部、mTLS 状态） |
| 单话机加密状态 | ippstat <分机>（DTLS、SRTP 套件）；话机加密图标 |
| 主备之间是否明文 | twin 命令 + 事件 5993（P1=0 明文，修复后重启 CS） |
| 证书快到期 | 事件 5992（P1=剩余天数；P1=0 证书失效、全站 FSNE 端点重启） |
| 链路建不起来 | ABC-F 查两端 Encryption 是否同值；trunk 查两侧端口是否成对 |
| 媒体加没加密 | Wireshark 抓 RTP 播放（噪音=加密）+ 决定表核对网关 SRTP 参数 |
| 媒体明文误报 | AES-128-only 设备在 AES-256 系统上回落明文是产品行为，不是故障 |

维护底线：证书变更后系统化备份（netadmin 导出或随 swinst 备份）并转存介质；EEGW 的证书操作会连带 CS 重启，变更窗口按 CS 重启级申报。

## 六、六条边界红线

1. 教材全部密码/账号/网段/许可值是实验值，上生产必须换
2. 企业 PKI 运营（CA 治理、CRL/OCSP、审批）在书外——签发环节以客户 CA 规程为准
3. EEGW VM 规格、压测口径在书外（S.O.T. 只按最大用户数 Sizing）
4. 无 IP SAN 证书：IP-xBS 与 NOE 模式 80x8s 不支持，答 n 前先查终端 release notes
5. SIP TLS with SSM 与 NE 互斥；SIP 扩展加密仅 SEPLOS 设备、仅 IPv4、不支持 CCD agent
6. 升级 R101.0（N3）后 1024 位出厂证书设备（部分 NOE 话机、8378 IP-xBS、8328 SIP-DECT）建不起双向认证——换 ≥2048 位证书或 N4 起降 SSL level（风险自担）

## 七、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 选 PKI/做 CSR/导证书/配 CTL | enc-certificate-trust-chain |
| 开加密/配 lanpbx/选 cipher suite | enc-native-encryption-bringup |
| 验证/查事件/备份/抓包 | enc-dtls-verification-maintenance |
| ALES 等 SIP 话机加密 | enc-sip-tls-endpoints |
| 运营商中继 TLS/SRTP/停用 | enc-sip-trunk-tls |
| 上 EEGW/NSP/S.O.T. | enc-eegw-deployment |
| 多节点 ABC-F 加密 | enc-abcf-network-encryption |
| 开 mTLS/装端点证书/降 SSL level | enc-mtls-endpoint-authentication |
| PCS 救援/XCA 做证/应用加密/实验环境 | 路由入口（oxe-native-encryption-router） |

## 版权

- 本精华长文为 ALE Training Services《OmniPCX Enterprise — Native Encryption》（ENTPXTE421EN Edition 05）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
