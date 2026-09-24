# OXE DM 证书定制与安全级（内部 PKI、CTL、mTLS、OpenSSL）

## R — 原文依据

> "By default, a certificate is generated at OXE installation for the HTTPs server for the usage of the WBM feature. However, it is not suitable for the SIP clients."（p169）
> "With OXE R101.0 and the upgrade of OpenSSL component to v3.0, the SSL security level has been increased to '2', that implies that any certificate with a RSA key length lower than 2048 bits or with a SHA-1 signing algorithm is no longer accepted"（p161）
> "2 : any certificates with a RSA key length lower than 2048 bits or signed with an older algorithm than SHA2 are refused. • 1 : any certificates with a RSA key length lower than 1024 bits ... • 0 : no restriction. • A reboot of the system is required after security level modification."（p162）
> "netadmin -m ... 11 : Security 9 : PKI Management 1 : CS Certificates And choice 1 : Create/Update CS certificates (Auto generated)"（p169）

出处：ENTPXTE403EN p156-171。

## I — 自述

证书是 SIP 化的地基：安装默认证书只适配 WBM/HTTPS，SIP 话机必须用定制证书 + CTL。三条主线：

| 主题 | 口径 |
|---|---|
| 内部 PKI 生成 | root 登录后进 netadmin 11/9/1 选 Create/Update (Auto generated)：录 CC-suite-ID（默认取自许可文件）、通配 DNS *.company.com（默认 y）、物理与角色 IP 入 SAN（默认 y）、密钥 2048-4096（默认 4096）；产出根 CA + CS 密钥对 + CSR + CS 证书 |
| 证书内容 | CS 证书 CN=oxe.company.com，SAN 含 FQDN/通配/物理与角色 IP；示例有效期 20 年；生成后必须重启 OXE |
| CTL 产物 | 话机侧信任列表落在 /usr3/mao/DM/VHE8082/（ctl_VHE8082、ict8000ctl.pem；p166 另写 /DHS3/data/mao/DM/VHE8082，同物异写） |
| 下载认证双通道 | ①传统 401 挑战：分机号+密码+MAC+机型 认证（auto-discovery 依赖）；②R101.1 起 mTLS：443 收请求后 302 到专设 8443 实例强双向证书（MAC↔证书 CN），远程场景由 RP 注入 X-Real-Mac/X-Forward-For，仅已知 RP 可带这些头 |
| OpenSSL 三级 | 2（R101.0 起默认）=拒 RSA<2048 位或 SHA-1 签名；1=拒 RSA<1024 位；0=不限制；3 仅 ALE 内部测试；改后必须重启 |
| 证书核查 | SSH 上 certificate info；话机 MMI：Enterprise/Essential/8008 走 Security > Certificate，ALE-2/3 走 Advanced Settings > View Certificate |

## A1 — 书中案例

**内部 PKI 定制证书**（p168-171，How-To）：

1. mtcl 登录后 su 切 root，执行 netadmin -m。
2. 依次进 11 Security / 9 PKI Management / 1 CS Certificates，选 1 Create/Update (Auto generated)。
3. 逐项应答：CC-suite-ID（实验 11111-11111-11111-11111）、通配 y、IP SAN y、附加 SAN n、密钥 4096、国家/组织（实验口径）→ 确认 y。
4. 系统生成四件（Root CA/私钥/CSR/CS 证书），提示 successfully generated。
5. 11/9/1/8 View 核验：CA CN=CC-suite-ID、CS CN=oxe.company.com、SAN 含 FQDN/通配/IP、有效期约 20 年。
6. 重启 OXE；cd /usr3/mao/DM/VHE8082/ 核验 ctl_VHE8082 与 ict8000ctl.pem 存在。

**老话机证书排查**（p179/p206-207）：

1. 话机入网失败先 SSH 执行 certificate info 或话机 MMI 查证书位数与签名算法。
2. 确为 1K RSA/SHA-1 则评估降级：netadmin（root）进 11 Security / 6 SSL configuration / 3 SSL security level。
3. 降级后必须重启 OXE；安全敏感站点应换证书而非降级。

## A2 — 未来触发

使用情境：话机批量报证书错误；上 SIP 前的证书规划；R101.0 升级后老话机掉线；要启用 8443 mTLS 下载认证；远程话机经反代拉配置失败。

语言信号：证书 / certificate / 内部 PKI / 根 CA / CS 证书 / CSR / SAN / CN / CTL / ctl_VHE8082 / OpenSSL / security level / 安全级 / RSA 2048 / SHA-1 / mTLS / 8443 / X-Real-Mac / 401 认证。

与相邻能力区分：证书做好了去开话机找话机开通；远程场景的 RP/EDS/SBC 证书五方链找远程办公；DM 体系本体的选型找 SIP 设备管理。

## E — 可执行步骤

输入契约：客户域名与 FQDN、是否外部 CA、存量话机年龄清单（证书代次）、维护窗口（要重启）。域名未定 → 判停回域名定制。

1. 核对前提：OXE 域名已改正式注册域名（默认域名必致证书错误）。完成标准：FQDN 落定
2. 生成证书：root 进 netadmin 11/9/1，按 CC-suite-ID/通配/IP SAN/密钥长度逐项应答。完成标准：四件生成
3. 核验：11/9/1/8 View 检查 CN/SAN/有效期；重启 OXE。完成标准：核验通过且重启完成
4. 验 CTL：/usr3/mao/DM/VHE8082/ 下见 ctl_VHE8082 与 ict8000ctl.pem。完成标准：CTL 就位
5. 核存量话机：SSH certificate info 或 MMI 查证书代次；R101.0+ 站点对 1K RSA/SHA-1 老机先出方案。完成标准：话机分桶（可直接入网/需换证书/需降级）
6. （按需）调安全级：11/6/3 改级别 → 必须重启；排重启窗口。完成标准：级别变更生效
7. （按需）启用 mTLS：swinst "DM auth. with client cert"（默认 Enabled）；远程场景确认 RP 已知且注入 X-Real-Mac/X-Forward-For。完成标准：下载认证链路通过

判停点：

- 域名还是 oxedomain.com → 停，先改域名再谈证书（n01）
- 安全敏感客户要求降级到 0 → 停，给换证书方案，降级只作过渡并留回退计划（n09）
- 远程话机 mTLS 失败且 RP 非客户自选第三方 → 查 RP 是否 CS 已知、头注入是否合规（n42）

输出契约：可用的证书链与 CTL + 存量话机证书分桶表 + 安全级别决策记录。

## B — 边界

- 外部 CA 亦可替代内部 PKI，但外部 CA 申请/签发流程书外（p169 只演示内部 PKI）
- 密钥/有效期示例（4096 位、20 年）与 CC-suite-ID 为实验/示例口径（n50）
- mTLS 8443 为 R101.1 起特性，低版本站点无此能力（nr-07）
- 远程办公五方信任链（话机/RP/SBC/OXE/EDS）详见远程办公卡，本卡只管 OXE 侧
- p166 与 p171 的 CTL 目录为同物异写（nr-03），引用时注明
