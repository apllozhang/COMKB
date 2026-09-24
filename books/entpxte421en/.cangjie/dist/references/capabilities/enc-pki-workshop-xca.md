# XCA 外部 CA 工坊（根 CA、实体证书、CSR 签发、格式转换）

## R — 原文依据

> "'XCA' is a tool for certificate and key management."（p335）
> "Take Care, 'Common Name' for 'OMS' end entity must match it's MAC address"（p344）
> "openssl crl2pkcs7 -nocrl -certfile RootCA.crt -out ca.p7"（p390）
> "Warning PKCS 12 IS NOT THE EASIEST WAY … PRIVATE KEY IS GENERATED ON THE CA AND MUST BE TRANSFERRED … CSR IS DONE MANUALLY ON THE CA"（p397）

出处：ENTPXTE421EN p333-353, p380-403。

## I — 自述

教学替身 CA 的操作工坊：客户没有现成 CA 时用它走通签发侧全流程（生产优先用客户自己的 CA）：

1. **准备工作**（p335-337/p381-385）：hohnstaedt.de/xca 下载 setup.exe 安装 → File/New DataBase 建口令保护库（实验口径 Alcatel）；客户已有 CA 就用客户的（p381 Warning）
2. **根 CA 制作**（p338-341/p386）：New key（4096）→ New certificate（自签、SHA 256、Type=Certification Authority、有效期）→ 导出 PEM（.crt）或 .p7b
3. **两条签发路线**（p391/p397）：
   - PKCS#7（推荐）：OXE 上 netadmin 11.9.1.2 生成 CSR（私钥不出机、SAN 自动），XCA 导入 CSR 后 Sign（选根 CA、End Entity），核验 subject/SAN 与 CSR 一致，导出 .p7b
   - PKCS#12（端点场景）：CA 侧 New key、New certificate（CN 按规则：CS/PCS=OXE FQDN，板卡/话机/IPDSP=MAC）、手工编辑 SAN，导出 PKCS12 设口令
4. **命名约定**（p344/p346/p351-352）：OMS/板卡实体 GW.pfx（CN=MAC）；IPDSP 两个文件 softphone_cert.pem + softphone_pkey.pem（加密导出）——部署端按文件名读取，严格匹配
5. **格式转换**（p389-390）：.p7b 用 conv-proper-p7-format.pl 转 ca.p7；.crt 用 openssl crl2pkcs7 转——OXE 导入菜单按格式要求收文件
6. **内嵌 CA 对照**（p310-312）：无外部 CA 时 netadmin 11.9.1.1 输 CC-suite-ID 一键自签（7300 天），XCA 仅在"外部 CA"路线上需要

## A1 — 书中案例

**端点实体制作**（p342-352，c17 步骤 3-4）：

1. New key 4096 位；New certificate 的签名证书选根 CA
2. OMS 实体：CN 填 OMS 的 MAC（005056010113，实验口径），Type=End Entity
3. 导出 PKCS12 且必须命名 GW.pfx，设导出口令
4. IPDSP 实体：CN 填其 MAC（设置 Network 页 phone identifier 查看）
5. 导出证书为 .pem 并命名 softphone_cert.pem
6. Private Keys 页导出私钥为 .pem encrypted 并命名 softphone_pkey.pem

**CS/PCS 签发**（p391-402，c19 步骤 2-4）：

1. 根 CA 导出 .p7b 传 OXE /tmpd，转格式为 ca.p7
2. PKCS#7 线：导入 OXE 的 CSR，Sign 后核验 SAN/CN，导出 .p7b
3. PKCS#12 线：CA 侧造钥造证，SAN 手工填（内嵌 EGW 填角色/物理 IP；外部 EGW+NSP 再加 EEGW 与 NSP FQDN）
4. 导出 PKCS12 设口令，交部署端

## A2 — 未来触发

使用情境：没有企业 CA 时怎么给 OXE 签证书；XCA 怎么建根 CA；端点证书的 CN 和文件名；CSR 拿来怎么签；.p7b 转格式；PKCS#12 什么时候才用。

语言信号：XCA / 根 CA / root CA / 自签 / End Entity / CSR 签发 / Sign / GW.pfx / softphone_cert / PKCS#12 / PKCS#7 / conv-proper-p7-format / crl2pkcs7 / 证书库。

与相邻能力区分：OXE 侧的 CSR 生成与导入 → 证书与信任链能力；证书部署到端点与 mTLS 启用 → mTLS 能力；本卡只是签发侧工坊（CA 角色视角）。

## E — 可执行步骤

输入契约：客户 CA 归属（无 CA 或教学场景用 XCA）、实体清单（CN=MAC 或 FQDN 的对照表）。客户有自己的 CA → 判停优先用客户的（p381）。

1. 建库与根 CA：XCA 建库 → 造 4096 位根密钥 → 自签 CA 证书（SHA 256、CA 型）。完成标准：根 CA 导出成功
2. CSR 线签发：收 OXE 的 CSR，Import、Sign、核验 subject/SAN 与请求一致后导出 .p7b。完成标准：证书可回交 OXE 导入
3. 端点实体：按台账逐台造钥造证（CN=MAC/FQDN、手工 SAN）→ 按命名约定导出。完成标准：GW.pfx/softphone 两个 pem 齐备
4. 格式转换：按 OXE 导入要求把根证书转 ca.p7（两种转换路径二选一）。完成标准：格式可被 11.9.1.4 接受
5. 交付：证书文件+口令走安全通道交部署端；台账记录序列号与有效期。完成标准：交付单闭环

判停点：

- 端点证书的 SAN/CN 手工填错 → PKCS#12 线的风险本体（p397 Warning）：交付前用 XCA 核验面板逐字段对照台账
- 客户 CA 有审批流程 → 签发排队在书外，按客户 CA 规程排期，不要按实验"秒签"节奏承诺
- XCA 软件安装本身的问题 → 通用 PC 操作，查其 Help（F1）与官网，不属于本卡

输出契约：根 CA 与实体证书文件（按命名约定）+ 台账（CN/SAN/有效期/序列号）。

## B — 边界

- XCA 是教学替身：客户生产 CA 的结构（层级、策略、CRL/OCSP）与 XCA 不同构，输出物以客户 CA 规程为准
- PKCS#12 线私钥在 CA 生成后搬运——仅用于端点证书等 CSR 不可行场景，能走 PKCS#7 就不走 P12（n30）
- XCA 软件安装与数据库创建属通用 PC 操作（p335-337/p381-385），本卡不展开
- 实验库口令与 MAC 值为实验口径，生产全部替换并纳入客户密钥管理
