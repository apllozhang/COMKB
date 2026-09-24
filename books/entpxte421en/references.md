# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| 客户企业 PKI / CA 运营规程 | 真实 CA 的签发排队、策略审批、CRL/OCSP 基础设施、CA 私钥保管——原书只有 CSR/CRL 概念页，签发环节在书外 | p12, p16-p18 |
| OXE 产品特性清单与各终端 release notes | 无 IP SAN 证书的固件支持核查（IP-xBS、NOE 模式 80x8s 不兼容）；"终端可能永远无法投入服务"的前置核查 | p85, p113, p248 |
| OXE 安装/维护文档与客户安全策略 | EEGW VM 规格、口令治理、SSH 收口、防火墙最小化等生产化基线（原书只有零散 Warning） | p52, p239, p357 |
| 支持 ACME 的本地第三方 CA 文档 | WBM 证书自动续期的服务器侧部署（公网 CA 因 HTTP-01 不可用） | p84 |
| XCA 官网（hohnstaedt.de/xca）与 Help（F1） | 教学用 CA 工具的下载与用法；客户已有 CA 时优先用客户的 | p335, p353, p381, p403 |
| ALE Knowledge Hub（enterprise-education.csod.com） | 课程评估与培训证书下载（课程运营，非技术知识） | p404-410 |

## 2. 官方工具与入口（书内出现的管理面）

| 工具 | 用途 | 书内位置 |
|---|---|---|
| netadmin -m | OXE 证书全生命周期主操作面（11.9.1 CS 证书/11.9.2 PCS/11.9.3 端点 CTL/11.1.3 防火墙/11.6.3 SSL level/17 内部 DNS/19 域名/20 EGW/10 copy to twin） | p101, p104 |
| lanpbxbuild | lanpbx.cfg 生成/维护（-auto、4→j/k/l/n、6 Apply changes 重签） | p121-125 |
| omsconfig / mgconfig / ostconfig | OMS VM / GD 板卡（V24 串口）/ EEGW VM 三类网元的配置与证书管理 | p147, p235-238, p288-289, p356-369 |
| WBM / OmniVista 8770 / mgr | 数据库参数配置面（Native Encryption/SIP Parameters/Voice Mail Parameters） | p101, p119, p140 |
| S.O.T. | EEGW VM 生成与加载（仅 Chrome/Firefox） | p272-282 |
| 验证命令族 | ippstat/twin/cryptview/sipregister/csipsets/sipextgw/config ost/pcsview/hybvisu/motortrace | p129-131, p143, p192-193, p242, p290 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g52（52 条，六类：concept 12 / role 4 / subscription 2 / product 18 / protocol 11 / resource 5）全部通过术语核验（BOOK_OVERVIEW 18 行候选术语逐条映射无遗漏，详见 glossary.md 收尾自检）。
- 落位口径：GLOSSARY.md 全量收录（按六类分组）；阶段 3 生成 `book/glossary.md` 门户版（精选高频 30 条左右，保持第一本版式）。
- 仅 passing 提及未单列的词（CC-suite-ID、DDI/DID、NPD、MD5、ECC/Diffie-Hellman、OpenSwan、OpenSSL、libsrtp、Nginx、Rocky Linux、pfSense、*tx8000#、VLAN/DHCP option 66、8135s/8378/8328、ALE-120/EM-200 等）已在 glossary.md 收尾自检备查，不进主表。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- stand-alone 拓扑（Subnet1 192.168.1.x / Subnet2 192.168.2.x / 公共区 10.20.30.x）：CSA 192.168.1.1（角色 .3）、CSB .2、OMS .13、EEGW .7/.8、SBC .105/.205、PCS 192.168.2.5、PC10/20/21 .10/2.10/2.11、NTP .252、FlexLM .80、内部 DNS .250、外部 DNS 10.20.30.250、NAS Z:\\12.0.0.2\rlab、CA_MAIL Y:\\10.20.30.200。
- 网络拓扑：NODE1 192.168.1.1（角色 .3）/NODE2 .101（角色 .103）、OMS Node2 .113、用户 31000（Node1）/31500（Node2）。
- 口令（实验口径，生产禁用）：mtcl/swinst/root=Superuser2580*、SBC=Admin/Admin、ALES（eevans/eeastwood）=alcatel、FlexLM/EEGW 初始=letacla1、SIP 模拟器=podP/alcatel、话机 tnet 默认 *tx8000#、XCA 库=Alcatel。
- 号码（实验口径，PN=POD 号两位）：安装号 3392PN、DID 首外线 33920N31000/首内线 31000/范围 500、SBC NAT=12.班级.POD.105、S.O.T. VM https://192.168.1.194。
- 许可实验值：#424=75、#359=30（p129 spadmin 输出）；内嵌 CA 自动生成有效期 7300 天、Root CA CN=CC-suite-ID（11111-11111-11111-11111 实验口径）。
