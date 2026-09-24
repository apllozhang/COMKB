# mTLS 双向认证启用与版本限制（全员证书、SSL level、1024 位处置）

## R — 原文依据

> "If 'mTLS' is brought into service, certificate must be loaded in any IP deskphone, even those in clear mode • The first connection to OXE is always in secured mode"（p82）
> "Since Release R101.0 (N3), OXE provides the support of the latest OpenSSL version 3.0 … X509 certificates with RSA keys of less than 2048 bits or signed with the deprecated SHA1 algorithm are not accepted anymore."（p366）
> "2 (default value): which requires SHA2 signature and minimum key size of 2K • 1: … minimum key size of 1K … 0: restore support of deprecated algorithm SHA1 … and no minimum key size"（p366）
> "Enable Mutual TLS Authentication True"（p364）

出处：ENTPXTE421EN p81-83, p165-168, p354-379。

## I — 自述

服务器认证之上的安全强化：OXE 反向验证端点证书，代价与版本陷阱都要提前算：

1. **范围规则**（p82/p377）：

   | 对象 | 激活方式 | 生效动作 |
   |---|---|---|
   | DTLS 端点 | 系统参数 Enable Mutual TLS Authentication 全局一刀切 | 重签 lanpbx + 重启 OXE |
   | SIP TLS 扩展 | 系统参数 SIP TLS Mutual Authentication 全局一刀切 | 节点重启 |
   | SIP trunk | 按外部网关逐个（Transport type + True） | 重启 SIPMOTOR |

2. **连带义务**（p82/p359）：激活后所有 IP 话机/软话机（含明文模式用户）都必须装有证书；第一连接总是加密模式；认证失败则注册失败，EGW 触发含端点 IP/MAC 的事件
3. **身份比对**（p82）：证书身份与端点首个信令消息宣告的 MAC 地址比对——端点证书 CN=MAC 是 mTLS 的身份基础
4. **版本陷阱**（p83/p366，OpenSSL 3.0 断裂）：

   | SSL security level（netadmin 11.6.3） | 要求 | 适用 |
   |---|---|---|
   | 2（默认） | SHA2 + ≥2048 位 | 新 PKI 标准线 |
   | 1 | SHA2 + ≥1024 位 | ALE PKI v1 需要 |
   | 0 | 恢复 SHA1 + 无最小长度 | 遗留设备（风险管理员自担） |

   - R101.0(N3) 起 1024 位出厂证书设备（部分 NOE 话机、8378 IP-xBS、8328 SIP-DECT）默认建不起双向认证
   - 两条出路：外部 PKI 重签 ≥2048 位证书并部署；或 R101.1(N4) 起降 SSL level（2→1 或 0），改级后重启+copy to twin
5. **端点证书三线部署**（p356-375）：
   - IPMG 线：End Entity .pfx（GW.pfx，CN=板卡 MAC），omsconfig/mgconfig 先临时开 SSH，导入后核验、保存重启；SSH 白名单事后撤销并告知客户
   - IPDSP 线：安装目录放 softphone_cert.pem+softphone_pkey.pem，口令经 DTLS_PKEY_PASSWORD 或 DTLSPkeyPassphrase.exe /set 绑定
   - 话机线：手工 Get Certificate（参数已下发仍需手工一步）；只有 SCEP 是真自动
6. **主备特例**（p91）：主备 CS 间 DTLS 会话强制 mTLS，两 CS 共用同一密钥对与证书

## A1 — 书中案例

**mTLS 启用实验**（p354-365，c18 步骤 1-6）：

1. 前提核对：服务器认证已配（NE 参数、CA/CS 证书、端点 CTL 就位）
2. OMS 临时开 SSH（omsconfig 选项 6+9，按转移用 PC IP 限时开放）
3. omsconfig 的 Certificate management 导入 GW.pfx，输导入口令
4. Print certificates 核验后保存并重启 OMS，事后撤销 SSH 白名单 IP
5. IPDSP 安装目录放证书与私钥两个 pem，DTLSPkeyPassphrase.exe 绑定口令
6. XCA 根 CA 证书经 11.9.3.1 导入 OXE 端点 CTL
7. Enable Mutual TLS Authentication=True → lanpbxbuild 重签 → 重启 OXE
8. 验证：cryptview 显示 mTLS enabled；OMS/IPDSP 加密在服；跨节点加密通话

**版本限制处置**（p366-375，c18 步骤 7）：遇 1024 位出厂设备时，方案 1=外部 PKI 签 ≥2048 位证书经 V24 串口/SCEP 部署；方案 2=N4 起 11.6.3 降 SSL level（重启+copy to twin）。

## A2 — 未来触发

使用情境：要不要开双向认证；开了之后明文用户怎么办；升级 R101 后老话机连不上了；SSL security level 降几级；OMS/板卡证书怎么装；SIP 侧 mTLS 端口 6261。

语言信号：mTLS / Mutual TLS Authentication / 双向认证 / 6261 / SSL security level / OpenSSL 3.0 / 1024 位 / 2048 位 / GW.pfx / softphone_cert.pem / DTLSPkeyPassphrase / Endpoint CTL / SCEP。

与相邻能力区分：服务器认证基线（CS 证书+端点 CTL）归证书与信任链能力；做端点证书的 XCA 操作归 PKI 工坊（路由卡）；trunk 侧互认证端口成对规则归 SIP trunk 能力；验证命令归验证与维护能力。

## E — 可执行步骤

输入契约：服务器认证已就位、端点台账（型号/固件/出厂证书位数）、客户安全基线（能否接受降级）。台账缺失 → 判停先盘点 1024 位设备。

1. 台账核查：按 p366 线索盘 1024 位出厂证书设备（部分 NOE 话机、8378 IP-xBS、8328 SIP-DECT）。完成标准：受影响设备清单
2. 选路线：逐台换 ≥2048 位证书（推荐），或 N4 起降 SSL level 并书面确认风险自担。完成标准：路线决策签认
3. 铺证书：IPMG/IPDSP/话机三线按 I 段第 5 条部署；工厂证书话机免部署。完成标准：全员证书到位（含明文用户）
4. 导端点 CTL：新 CA 的根证书经 11.9.3.1 入 OXE 信任库并核验。完成标准：View 见新条目
5. 启用：DTLS 全局参数 True → 重签 lanpbx → 重启；SIP 侧按全局/逐网关口径分别启用。完成标准：参数与端口到位
6. 验证：cryptview 显示 mTLS enabled；明文用户注册不受阻；受影响老设备按所选路线处置后可注册。完成标准：全量注册正常

判停点：

- 台账没盘就启用 → 不要开：任何无证话机（含明文用户）都会注册失败（p359）
- 客户只肯降 SSL level 又不接受风险 → 判停，两条路线都走不通时升级决策
- 板卡开 SSH 传证书 → 告知客户开放时长，完成后立即撤销白名单 IP（p357）
- SIP 侧互认证配了不生效 → 查端口 0 覆盖陷阱与两侧端口成对（n15/n29，详见 SIP trunk 能力）

输出契约：mTLS 启用 + 全员证书台账 + SSL level 决策记录 + SSH 临时开放闭环记录。

## B — 边界

- 客户设备台账（1024 位清单）在客户侧，原书只给设备型号线索——启用前必须核查
- level 3 仅供 ALE 专家内部测试，不对外使用（p366）
- "By the end of 2025 新产板卡默认嵌 ALE 证书"为时效性承诺，落地前核对（nr-05）
- Windows 证书库法装 IPDSP 证书原书仅演示未测试（p362 自注），优先文件法
- 全部实验值（005056010113 等MAC、口令）为实验口径，生产按客户台账替换
