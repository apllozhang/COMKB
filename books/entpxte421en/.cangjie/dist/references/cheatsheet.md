# 决策规则速查 — OmniPCX Enterprise — Native Encryption (Participant's Guide, Edition 05)

| 能力 | 一句话规则 |
|---|---|
| 证书与信任链全生命周期 | PKI 三模式选 PKCS#7 主线（私钥不出机）、CSR 五步闭环、CTL 经 lanpbx/TOFU 或手工预置、CA 更新有连锁义务 |
| 加密解决方案开通与 lanpbx.cfg | NE 参数三件套+用户级部分加密+lanpbxbuild 签名（DTLS 端口 32643）；AES-256 有压缩器降额与 GD3 禁用红线 |
| DTLS 验证、排障与维护闭环 | cryptview/ippstat/twin 命令族+事件 5991-5995 处置+证书备份+Wireshark 抓包（加密=噪音） |
| SIP TLS 扩展加密 | sipmotor 承载 TLS 1.2（端口 5061）；SEPLOS 设备专用，参数三件套+motortrace 验证 X-ALE-CALL-ENCRYPTED |
| SIP trunk 的 TLS 与 SRTP | OTSBC 与 OXE 两侧成对配置；媒体加密=系统 NE×网关 RTP/SRTP 参数；端口 5061/6261 四组合与 0 覆盖陷阱；四步安全停用 |
| EEGW/NSP 大容量部署 | 超 1500 会话强制 EEGW VM（每 CS 一台、上限 15000）；声明/改名都触发证书重生成+重启；冗余必须用 NSP FQDN |
| ABC-F 网络加密 | 节点间 IPSec（500/2579）+SRTP 经加密链路分发；链路参数两端同值且须 DOWN 才能改；任一环缺失即明文 |
| mTLS 双向认证与版本限制 | 激活后全员（含明文用户）必须有证书、首连总是加密；1024 位设备两条出路——换 ≥2048 位证书或 N4 起降 SSL level |
| PCS 加密接管 | 端点必须连过 CS 才能被救援；PCS 与主 CS 共用 lanpbx；证书同 CA 异证书且导入前先打 tar；断网演练要预备操作路径 |
| XCA 外部 CA 工坊 | XCA 建库造根 CA、CSR 导入签发（P7 推荐）、端点实体 PKCS#12（CN=MAC、命名严格匹配）、根证书格式转换 |
| 应用生态加密与安全下载 | 4645 自动受保护、录音换钥、VAA 加密 120→60 端口、DC 不受影响、Rainbow WG 信令恒加密；HTTPS 替代 TFTP 有前提 |
| 实验环境底座（RLAB） | 两套拓扑（stand-alone 双 CS / ABC-F 双节点）、Pod 五步初始配置、NTP 与信任库约束、VM 同 IP 禁忌 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
