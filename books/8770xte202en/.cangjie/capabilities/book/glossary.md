# GLOSSARY — OmniVista 8770 目录管理术语表

> 阶段 3 产出（源：candidates/glossary.md，52 条，六类；此处为门户精选版，全量以 candidates 为准）。
> 口径：定义只采信本书正文；STAP/DDI/COS/WBM/NMC/AHV 等缩写书中未给全称，如实标注不编造；p95/p120/p330 三处为书内排版勘误（见 needs-review）。

# OmniVista 8770 Directory Administration (8770XTE202EN Ed40) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（565 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Company Directory | 公司目录 | LDAP v3 目录：按地理/部门/员工存组织数据，与通信服务器同步；根为 o=directoryroot | p32, p62 |
| Directory entry | 目录条目 | 两类：Organization（Country/City/Company/Department）与 Termination（Person/Group/Room）；地址簿是独立组织条目 | p63 |
| UID (User Identifier) | 用户标识 | 人员唯一业务 key，默认"名+姓"；可按 PCX 配置为"名+姓+分机号"防同名（只对自动创建生效） | p66, p74 |
| DN (Distinguished Name) | 可分辨名称 | 条目在树中的唯一位置路径；目录侧落 o=directoryroot，配置侧落 o=nmc，两套模板 | p67, p436 |
| Primary link | 主链接 | 人员↔OXE 用户一对一绑定（姓名+名字+成本中心一致），每条目仅一条；姓名修改必须经公司目录 | p69, p79 |
| Secondary link | 副链接 | 手工建的一人多机（典型 DECT）：异名同成本中心；建链瞬间 CC 继承主链接 | p70, p130 |
| Fax link | 传真链接 | n:n（传真机可多人共享），成本中心互不影响，传真号从 PCX 取回 | p70 |
| Multi-device link | 多设备链接 | 1 entry→n users，OXE 同步后自动建，多话机共用一条目；也可经 Users 应用 Add a secondary set | p69 |
| Additional resources link | 附加资源链接 | 与主链接同性质但可多条；4760 迁移"一人多主链"专用 | p71 |
| Automatic creation | 自动创建 | PCX 建用户事件到达后在 Location 指定路径自动建人员并建主链接；受三层开关控制 | p74-76, p105-107 |
| Confidentiality level | 保密级别 | 挂在人员条目上的四级标记（Green 默认/Orange/Red/Administration 8770） | p209 |
| Personal data | 个人数据 | 五种：家庭电话/家庭住址/驾照/工号/密码；其余为非个人数据 | p210 |
| Access levels | 应用访问级别 | Company Directory 五档 + Web Directory 五档，Security 应用按应用授予 | p214-215 |
| Cost Center | 成本中心 | PCX 侧定义（ID+名字）的组织/计费归属；目录侧可改但 PCX 必须已存在同名 CC | p80, p110 |
| Domain for management | 管理域 | 域=名字+一组公司目录 DN 级别+本地管理员名单；可嵌套可多父 | p429, p437-438 |
| Customized view | 定制视图 | 用户开户界面的字段显示模板，按管理员账户绑定，简化本地管理员开户 | p446-448 |
| Strict view | 严格视图参数 | 域内人员 Web 目录检索范围：关=本域+父域（默认）；开=严格本域 | p454 |

## 二、Click to Call 与号码域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| DDI translator | DDI 号码翻译器 | PCX 侧定义的 DDI↔内线映射（首外部号/首内部号/范围大小），同步取回 | p257, p268 |
| ISDN number | ISDN 号 | 8770 自动构造的外部号码=前缀+实体安装号+话机号；DDI 话机话机号被 DDI 号替换 | p258 |
| STAP | 自动呼叫权限（书中未展开全称） | 用户级三态 Off hook/Authorized/Forbidden；SIP 话机不支持 | p272 |
| Prefix rule | 前缀规则 | 三类：None/外部呼叫规则（匹配头+删+加）/网间呼叫规则；建在 Network/Subnetwork/PCX 层 | p261-263 |
| Associated station | 关联话机 | Web 客户端 Define associated station（分机号+密码）绑定 Click to Call 主叫话机 | p180, p283 |

## 三、定制域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| LdapAttributes.dict | 目录属性词典 | 默认翻译词典；打开定制工具必选 C:\8770\Client\dict 下该文件（How-To 口径） | p287, p309 |
| dict_user.zip | 客户端词典包 | 保存时重打包；客户端连接时校验版本并自动下载（被占用时保存失败） | p302, p310 |
| Dictionary version number | 词典版本号 | 默认空，每保存自增；Set All to Default 回退也自增 | p297, p309 |
| Theme | 主题 | Web 客户端皮肤，仅两套（theme1=8770WBM/theme2=Custom，CSS）；用户选择存 cookie | p313-314, p346 |

## 四、MSAD/Azure 域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| MSAD | Microsoft Active Directory | 本地 AD：8770 经专用账号做"一条映射+N 条规则"的双向属性同步 | p353, p369 |
| Attribute mapping | 属性映射 | 全 8770 只能建一条；sn 只能 AD→8770 不可删；电话只 8770→AD；abObjectGUID 隐藏保唯一 | p355-356, p380 |
| Synchronization rule | 同步规则 | 定义 8770 位置↔MSAD OU、Filter（objectclass=user 且 cn 非空）、Flat/Tree 模式 | p385-387 |
| Flat / Tree | 平铺/镜像同步 | Flat 只同步人不建分支（分支手工建）；Tree 按 AD 层级镜像建分支+人 | p386 |
| Automatic deletion of 8770 users | 自动删除二态 | False（默认）标记删除待人工；True 连 OT/OXE/8770 永久删 | p377 |
| Azure AD (Microsoft Entra ID) | 云目录同步 | Azure AD 恒为主节点，经 Microsoft Graph API 拉取，不 provision OXE 用户；tree 需 Directory 许可 | p360-361 |
| Meta profile | 元模板 | Users 应用的开户模板（OXE 节点+空闲号段+话机类型+profile）；Directory number 留空自动取首个空闲号 | p363-364 |
| MSAD8770Admin | 插件专用管理员 | 8770 侧为插件专建；改密后必须重启 NMC Java Service Definition 服务 | p404-405 |
| MSADadmin | AD 侧同步账号 | AD 服务器上为 8770 同步专建，须入 Domain Admins 组 | p369, p373 |

## 五、复制与运维域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Master replica | 主副本 | 读写数据库，复制供体；ID 手工 1-65534 | p505, p510 |
| Consumer replica | 消费者副本 | 只读数据库，ID 固定 65535；写请求经 referral 转主但复制后本地改动消失 | p505-507 |
| Referral | 写重定向 | Consumer 写操作转交 Master 执行的机制；管理上强烈建议只在 Master 改 | p505-507 |
| Replication Agreement | 复制协议 | 主服务器上的参数集（副本配置/属性集/从机 Host:Port/管理器密码/初始化与调度） | p506 |
| Attribute set | 属性集 | 可复制属性组；建协议后不可改，要改删协议重建或改后 Initialize | p512, p529 |
| Initialize | 初始化 | 先清空 Consumer suffix 全部数据，再从 Master 全量拷贝 | p531 |
| LDIF | LDAP 数据交换格式 | 导入只增改不删除；属性空值不导出；配套六件套命令行工具（8770\bin） | p85, p540-542 |
| PurgeLdap | 按过滤器删除工具 | 配合 misc10 时间戳标记实现"外部目录删了 8770 跟删" | p547, p557 |
| misc10 | 删除跟随标记 | da.conf 写入的时间戳类值；purgefilter 过滤"不等于本次标记"的条目 | p547, p557 |
| toolsOmniVista.exe | 服务器维护工具 | 停服务/改 directory manager 与复制管理器密码（选项 6） | p521 |
| dirmanag.exe | 目录根管理工具 | LDIF 管道坏结构后的救援通道（删 ABS 根） | p555 |
| NMC Java Service Definition | 8770 服务 | MSAD8770Admin 改密后必须重启才认新密码 | p404-405 |

## 六、许可与产品域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Directory license | 目录许可 | 公司目录功能许可；复制双机都要、Azure tree 模式也要；MCS 版默认自带 | p458, p514, p360 |
| Domain Management license | 域管理许可 | 管理域功能许可；MCS 版也不自带，永远单独持有 | p435, p458 |
| Unified Management license | 统一管理许可 | WBM Users 应用（用户供给+目录层级管理）所需 | p35 |
| Active Directory integration license | AD 集成许可 | MSAD 同步与 Azure AD 共用总许可 | p351, p360 |
| OmniPCX Enterprise (OXE) | 企业级 PBX | 目录的数据源与链接对端；实验实例 csa/csm，siteid/netadmin 做前置检查 | p9, p89 |
| OmniVista 4760 | 上一代网管 | 其"一人多主链"人员模型经 Additional resources link 迁移 | p71 |
| AdminNmc | 8770 超级管理员 | 出厂全局管理员账户（实验口令 Superuser01*，实验口径）；DN 见六件套参数 | p93, p544 |
