# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指向的配套资源与权威依据（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| SIP Carrier Simulator 文档（RLAB 配套） | 外呼验证与模拟器号码规则的操作依据 | p268（c07 步 4 引用） |
| LDIF1.zip / LDIF2.zip 随书实验文件 | go.bat/link.bat/purge.bat/export.bat 与各 .conf 的实际载体；misc10 标记机制依赖其中数据 | p552-558（c17 步 1/9） |
| AD CS（Active Directory Certificate Services）服务器角色 | MSAD LDAPS 的证书前提——AD 侧安装与发证 | p377 |
| Microsoft Graph API 应用注册（Azure 门户） | Azure AD 同步的应用机密与 User.ReadWrite.All 权限授予 | p360-361 |
| 8770 Capacity Planning tool V3.0 | 虚拟机 sizing 工具（本书仅点名，不教用法） | p8 |
| OXE 侧命令生态（siteid / netadmin / netstat） | 节点注册前置检查的取数手段 | p89-92 |

> 说明：本书为培训教材，生产化的安装/管理细节原书未给正式文档指针；BOOK_OVERVIEW 批判章建议生产依据以 OmniVista 8770 官方 Installation/Administration Guide 为准——该指针属整理侧建议（推断），非原书引用，能力卡引用时保留此标注。

## 2. 原书内部资源区（服务器自带工具与文件，术语卡已收录）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| CustomDict / Dictionary customization | 词典定制工具（生成 LdapAttributes_user.dict） | p287, p295-310 |
| toolsOmniVista.exe | 停服务/改 directory manager 与复制管理器密码 | p511, p521 |
| dirmanag.exe | 目录根级管理（LDIF 管道坏结构后的救援通道） | p555 |
| MindTerm | OXE 声明 Connectivity 页签的 SSH 公钥建立 | p96 |
| NMC Java Service Definition 服务 | MSAD8770Admin 改密后必须重启的服务 | p404-405 |
| SHARING 文件夹 | 8770 与 AD 服务器双虚机间传安装文件的中转 | p408 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g52（52 条，六类）全部通过术语核验；STAP/DDI/COS/WBM/NMC/AHV 等缩写书中未给全称，如实省略不采信外部知识。
- 落位口径：GLOSSARY.md 全量收录（按 concept/role/subscription/product/protocol/resource 六类分组）；阶段 3 生成 `book/glossary.md` 门户版（精选高频条目，保持第一本版式）。
- g39（Company Directory license）书内仅一处提及、与 Directory license 的关系未说明——按"待确认"口径进 glossary 备查行，不作能力依据。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- RLAB POD（实验口径）：OXE csa 192.168.1.1 / csm 192.168.1.3；Client PC 192.168.1.10；Ecosystem（AD）192.168.1.100；OV8770 server nms 192.168.1.70；内部 DNS 192.168.1.250、网关 192.168.1.254；公共区 10.20.30.x（SIP 模拟器 12.0.0.2、外部 DNS 10.20.30.250）。
- 账户口令（实验口径）：AdminNmc/Superuser01*、adfexc 与 mtcl 均为 Superuser2580*、MSADadmin/MSAD8770Admin 用 Superuser01*、话机密码 0000、SIP 话机密码 123456、复制管理器默认 superuser。
- 号码口径（实验口径）：分机 31000-31005/31022-31024/31105；DDI 翻译器 33210N41000 起首外部号、首内部号 31000、范围 500（N=POD 号）；ITSP1 号码规则 3321PN12345 族。
- 全部"实验口径"值生产化必须替换；引用只允许出现在 Boundary 与 book/overview.md。
