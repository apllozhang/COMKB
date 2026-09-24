# DIGEST — OmniVista 8770 目录管理精华长文

> 源：8770XTE202EN Edition 40（565 页，OmniVista 8770 R5.2 口径）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 8770 目录（Company Directory）交付的全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

OmniVista 8770 是 ALE 的网管平台，目录套件里的"公司目录"是一个 **LDAP v3 目录服务器**：按地理/部门/员工存组织数据，与通信服务器（OXE/OXO/OpenTouch）双向同步，配 MariaDB 做系统存储。配置目录（o=nmc，给系统用）和公司目录（o=directoryroot，给人看）是两棵树，靠六类"链接"缝合。

整本教材是一条交付主线：

1. 接 OXE（节点注册与同步）
2. 建树与自动供给
3. 绑人机链接
4. 保密与查询
5. 拨号出口（Click to Call）
6. 定制
7. 对接企业 AD
8. 分域运营与目录冗余

先记住三组数字：

| 数字 | 含义 |
|---|---|
| 6 类 | 人员-用户链接（主/多设备/副/传真/杂项/附加资源），主链接是根 |
| 4 级 × 5 档 × 2 | 条目保密四级；管理端 Company/Web Directory 各五档访问级别 |
| 1 主 4 从 / 7 天 | 复制拓扑上限；从机断联超 7 天主侧新增数据丢失 |

## 二、地基：树、标识、供给

- **树**：组织条目（Country/City/Company/Department）作枝干，终止条目（Person/Group/Room）作叶子；人可挂任意层级。DN 是位置路径（目录侧 uid=…落 o=directoryroot；配置侧 TelephoneNumber=…落 o=nmc）。
- **UID**：人员业务 key，默认"名+姓"，目录内唯一。同名撞车时自动创建拒建并告警——解法是把该 PCX 的 UID construction 改为 Extension（名+姓+分机号），注意三点：按 PCX 分别设、只对自动创建生效、试点完要改回。
- **三条供给通道**：PCX 事件自动创建（实时，受全局三开关+节点 Location+两前提控制，任一缺失静默失效）、OXE 同步、LDIF 批量管道。

## 三、人机绑定：六类链接与改名

| 链接 | 基数 | 成本中心 |
|---|---|---|
| Primary 主链接 | 1:1（每条目唯一） | 双向 |
| Multi-device 多设备链 | 1 entry→n users（同步后自动建） | 随主链接 |
| Secondary 副链 | 手工，异名同 CC（DECT） | 建链瞬间继承主链接 |
| Fax 传真链 | n:n（可共享） | 不动 |
| Miscellaneous 杂项链 | 异名同 CC（数据终端/Modem） | 双向 |
| Additional resources 附加资源链 | 同主链接可多条（4760 迁移） | 同主链接 |

改名入口决定后果：**Users 应用/WBM 是钦定最佳入口**（链接与 CC 全保留、Name 同步更新）；目录应用改要手工同步 User id；从 Configuration 界面改姓名会**断链生成新人**——修复流程是删新人、旧人 Primary link 重挂分机。

目录侧改 CC 前必须先在 PCX 建 CC，否则拒绝并告警回滚。核验口诀：Configuration Users 文件夹关开刷新再看值。

## 四、保密与账户：两套正交机制

- **条目保密**：Green（默认）/Orange/Red/Administration 8770 四级 + 个人数据五种（家庭电话/住址/驾照/工号/密码）。行为矩阵：匿名只见 Green 非个人数据；认证本人多看自己的个人数据；**本人是 Orange/Red 也不会多看到别人的条目**。
- **账户权限**：Company Directory 五档 + Web Directory 五档，Security 应用按应用分别授予；AdminNmc 默认全开。排障第一步永远是分清"哪套机制挡住了"。
- 管理域是第三把刀：按 DN 级别切管理员的可见范围与权限（Domain Management+Directory 双许可、默认关闭）；本地管理员永远建不了域，Delegation 才能下放建户权。

## 五、拨号出口：Click to Call 五环链

Click to Call 五环链：

1. DDI 翻译器（PCX 侧映射，8770 同步取回）
2. ISDN 号构造（前缀+实体安装号+话机号；缺安装号、翻译器未纳管且无补充号都不构造；改 PCX 数据必须重同步）
3. 前缀规则（外部呼叫规则/网间规则，Prefix to delete 是"匹配头+删除"双重语义）
4. 属性关联（默认 Extension/ISDN/Mobile 三项，Misc 1-5 手工加）
5. STAP 权限放行+关联话机（分机+密码）

硬边界：**OXE SIP 话机全线不支持** STAP 与 Click to Call——交付前先盘点话机类型。

## 六、数据管道：LDIF 与企业 AD

- **LDIF**：导入只增改不删除（第一性约束）；备份用 Branch 范围；服务器导出走 Scheduler 落 C:\8770\Client\data\import。命令行六件套在 8770\bin：标准管道是 CSV 转换导入后用 LinkDn 建关系链、PurgeLdap 做"外部删我也删"（misc10 时间戳标记+过滤器）。全书最重警告：**p.conf 的 o=abs 根名忘改就跑 go.bat 会造坏结构，改回重跑无效，须 dirmanag.exe 删根重来**。
- **MSAD**：一条映射（sn 只进不出且不可删、电话只出不进、abObjectGUID 隐藏保唯一）+ N 条规则（Flat 不同步分支/Tree 镜像结构）；规则或映射改完必须跑 Complete；AD 删人默认只标记（True 才连删三系统）。"双向"不对称：8770 侧新建/删除人员不回写 AD。
- **Azure AD/Entra ID**：Azure 恒为主节点，走 Graph API（不用 LDAPS、无需管理员账号），不 provision OXE 用户；tree 模式另需 Directory 许可。
- **MSAD 插件**：AD 服务器上装插件，右键用户按 Meta profile 一键开户（目录+Users+OXE）；前置三件——MSAD8770Admin 改密后重启 NMC Java Service、空闲号段建完必须同步、Meta profile。更新仅 CC 与称谓可改；**IE 强依赖是版本风险项**。

## 七、规模化：定制与冗余

- **词典定制**：改属性显示名=改翻译，保存三动作且版本号自增（回退也自增）；客户端重连自动下载新 dict_user.zip；服务器本机开着客户端时保存失败。
- **客户端定制**：默认参数（管理员定基线）/用户参数（认证用户个人覆盖）/主题（存 cookie）三层；没有一键还原——动手前先导 DirectoryClient 分支 LDIF+备份 Themes 文件夹。
- **目录复制**：Slave 建 Consumer（ID 65535）→ Master 建副本（ID 1-65534）+协议+属性集 → Initialize+调度（实验每日 5:00AM）。纪律三条：只在 Master 改数据（Consumer 改动复制后消失）、属性集建协议后锁死、断联超 7 天走 LDIF 六步人工恢复。**它只冗余目录数据，不冗余 8770 服务器，且不支持 LDAPS**。

## 八、交付红线

| 红线 | 说明 |
|---|---|
| 实验口径 | 教材所有 IP/密码/号码（Superuser01* 族、DDI 段等）是教学约定值，生产必须全量替换 |
| 书内勘误 | p95 节点号示例、p120 UID 描述、p330 字段说明三处排版勘误，操作以字段与实测为准 |
| 生产化指针 | 安装/管理细节以 8770 官方 Installation/Administration Guide 为准（整理侧建议） |

## 九、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 接 OXE/同步/节点号 | ovdir-oxe-sync-ldap |
| 建树/自动创建/同名 | ovdir-auto-creation |
| 链接/改 CC/改名/断链 | ovdir-links-rename |
| 接 AD/Azure AD 同步 | ovdir-msad-azure-pipelines |
| 点击外呼/STAP/DDI | ovdir-click-to-call |
| 保密/访问级别/匿名 | ovdir-confidentiality |
| 目录复制/7 天恢复 | ovdir-replication |
| 分域/委派/定制视图 | ovdir-domains-delegation |
| AD 右键开户/LDIF 管道/词典与界面定制/平台背景 | 路由入口（omnivista-directory-router） |

## 版权

- 本精华长文为 ALE Training Services《OmniVista 8770 — Directory Administration》（8770XTE202EN Edition 40）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
