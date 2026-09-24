# 盲判结果 entpxte421en（阶段一锁定，不回改）

should-cert-01 | enc-certificate-trust-chain | 内嵌 CA 还是企业 CA 的模式选择与证书格式归属 PKI 三模式主线
should-cert-02 | enc-certificate-trust-chain | 导入签发证书并让 twin 备机生效属 CSR 闭环与备份同步义务
should-bringup-01 | enc-native-encryption-bringup | 开原生加密与用户级部分加密正是 NE 参数块开通能力
should-bringup-02 | enc-native-encryption-bringup | AES-256 与 GD3 板卡硬件代价属 SRTP cipher suite 评估
should-verify-01 | enc-dtls-verification-maintenance | 向客户证明媒体加密用 cryptview/ippstat 验证命令族
should-verify-02 | enc-dtls-verification-maintenance | 5992 事件与 P1 倒计时处置属事件族维护闭环
should-sipext-01 | enc-sip-tls-endpoints | ALES 加密注册的参数三件套属 SIP 端点扩展加密
should-sipext-02 | enc-sip-tls-endpoints | 端点加密后 488 拒绝属 SIP TLS 端点配置错误范畴
should-trunk-01 | enc-sip-trunk-tls | OTSBC 与 OXE 成对配 TLS/SRTP 正是中继加密能力
should-trunk-02 | enc-sip-trunk-tls | 信令 TLS 后媒体是否加密查信令/媒体决定表
should-eegw-01 | enc-eegw-deployment | 2000 路超内嵌 1500 分界，扩容归 EEGW 容量公式与部署
should-eegw-02 | enc-eegw-deployment | EEGW 上操作连带 CS 重启属其五条硬规则
should-abcf-01 | enc-abcf-network-encryption | 节点间链路 Encryption 参数两端同值且须 DOWN
should-abcf-02 | enc-abcf-network-encryption | 跨节点明文段排查属端到端短木桶拓扑分析
should-mtls-01 | enc-mtls-endpoint-authentication | mTLS 对存量明文话机的影响属范围规则与全员证书义务
should-mtls-02 | enc-mtls-endpoint-authentication | R101 后老话机注册失败指向 OpenSSL 3.0 对 1024 位证书的断裂
should-pcs-01 | enc-pcs-failover | 加密环境下 PCS 救援部署正是该能力
should-xca-01 | enc-pki-workshop-xca | 没有企业 CA 自建签发工具即 XCA 工坊
should-app-01 | enc-application-encryption | 留言信箱与录音在加密站点的处理属应用生态加密
should-app-02 | enc-application-encryption | VAA 加密后端口 120→60 正是该能力条目
should-lab-01 | enc-lab-environment | RLAB Pod 初始配置五步属实验底座能力
should-bringup-03 | enc-native-encryption-bringup | lanpbx.cfg 的 DTLS 地址与端口 32643 属开通参数块
bait-cert-01 | enc-native-encryption-bringup | 证书装好仍明文的下一步是开 NE 加密参数而非再动证书
bait-bringup-01 | enc-dtls-verification-maintenance | 参数已开后验证注册与通话加密用 cryptview 命令族
bait-verify-01 | enc-native-encryption-bringup | SRTP 参数改后不生效疑与 lanpbxbuild 签名重建规则有关
bait-sipext-01 | enc-sip-trunk-tls | SBC 上建 TLS context 属中继 TLS 的 OTSBC 侧步骤
bait-eegw-01 | enc-eegw-deployment | 500 路是否要上 EEGW 取决于 1500 容量分界与许可公式
bait-abcf-01 | enc-sip-trunk-tls | 对接运营商网关的加密是中继 TLS，与节点间 ABC-F 无关
bait-mtls-01 | enc-pki-workshop-xca | 用 XCA 造板卡端点证书并导出 GW.pfx 正是工坊能力
bait-pcs-01 | enc-dtls-verification-maintenance | 5993 事件处置归事件族能力，不因提到 PCS 就跳接管
bait-xca-01 | enc-certificate-trust-chain | 客户已有企业 CA 走 PKI 三模式主线而非 XCA 工坊
bait-app-01 | enc-application-encryption | HTTPS 替代 TFTP 的前提（NE+DHCP option 66）正是该能力条目
bait-lab-01 | enc-lab-environment | 192.168.1.x 与 Superuser2580* 是 RLAB 实验口径，识别其不得用于生产属该能力边界
bait-trunk-01 | enc-sip-tls-endpoints | ALES 话机音频走向与加密能力限制属端点扩展加密范畴
edge-san-01 | enc-certificate-trust-chain | CSR 的 SAN 与 CN=MAC/FQDN 命名规则归证书生命周期
edge-acme-01 | enc-certificate-trust-chain | WBM 证书自动续期问题归证书全生命周期（ACME 未必在教材内，需声明边界）
edge-port-01 | enc-sip-trunk-tls | 端口填 0 的覆盖陷阱正是 5061/6261 四组合条目
edge-aes-01 | enc-abcf-network-encryption | direct link 两端参数同值要求与不一致后果属 ABC-F 链路加密
edge-version-01 | enc-mtls-endpoint-authentication | SSL level 2/1/0 降级兼容老话机正是该能力语义
