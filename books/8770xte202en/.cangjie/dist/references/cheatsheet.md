# 决策规则速查 — OmniVista 8770 — Directory Administration (Participant's Guide, Edition 40)

| 能力 | 一句话规则 |
|---|---|
| OXE 节点注册与同步 | 前置三查（siteid/netadmin/信任列表）→ Network/Subnetwork/OXE 三级声明 → Complete-Separate 同步 → 日志与时间戳核验 |
| 目录树搭建与 PCX 自动创建 | 建树 + 全局三开关 + 节点 Location + 两前提；UID 撞名改 Extension 构造（按 PCX、只对自动创建生效） |
| 六类链接与改名语义 | 主链接是根（1:1、姓名+CC），副链继承 CC、传真链不动；改名首选 Users/WBM 入口，配置入口断链走"删新人+重挂"修复 |
| MSAD 与 Azure AD 同步管道 | 一条映射+N 条规则（sn 不可删、电话只从 8770 写回）；Complete 增量规则、删除二态；Azure AD 走 Graph API 不 provision OXE 用户 |
| Click to Call 交付 | 五环链交付：DDI 翻译器 → ISDN 构造 → 前缀规则 → 属性关联 → STAP 放行；SIP 话机全线出局 |
| 目录保密级别与访问级别 | 条目保密四级 × 个人数据五种定 Web 目录可见性；账户两应用各五档在 Security 授予；本人级别不放大他人可见性 |
| 目录复制主从部署 | Slave 建 Consumer → Master 建副本+协议 → Initialize+调度；Master-only 写入、断联超 7 天须 LDIF 人工恢复 |
| 管理域与委派 | 域=DN 级别集合×管理员组（双许可、默认关）；三预定义组定权限档；Delegation 下放建户权，定制视图简化开户 |
| MSAD 插件开户（AD 右键一键开通） | properties 生成+AD 装插件+Meta profile 一键开户；前置三件（改密重启/号段同步/Meta profile）缺一即失败 |
| LDIF 导入导出与管理工具管道 | GUI 三范围备份恢复 + CLI 六件套管道（CSV 转换/导入/建链/删除跟随）；导入永不删除，p.conf 根名第一步改 |
| 目录词典与 Web 客户端定制 | 词典改属性显示名（版本号自增+客户端自动下载）+ 客户端三层定制（默认参数/用户参数/主题）；备份先行否则没有回退点 |
| 8770 平台基础（套件/拓扑/兼容/虚拟化） | 四套件 15 应用+WBM 四应用分工；MariaDB+LDAP 双存储；p9 版本兼容矩阵与虚拟化平台清单 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
