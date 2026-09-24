# 目录词典与 Web 客户端定制（属性改名、三层参数、主题、备份回退）

## R — 原文依据

> "Default translations are stored in the dictionaries LdapAttributes.dict ... CustomDict tool used to generate a second dictionary"（p287）
> "Save button used to #1: Save the new translations in the folder C:\8770\dict\user. #2: Automatically generate files ... #3: update the archive 8770\Client\bin\dict_user.zip"（p302）
> "Paul didn't customize the tab Results: The default configuration is used ... Default configuration of the tab used in case of anonymous access"（p322）
> "Do an LDIF export to save the configuration of the web directory client • Do a backup of the folder c:\8770\client\themes"（p326）
> "The theme selected by a user is saved in a cookie ... The Edit option ... is reserved to the Directory administrator."（p346）

出处：8770XTE202EN p287-310, p311-348。

## I — 自述

定制分两块：目录词典（属性显示名）与 Web 目录客户端（界面行为与外观）。

**词典定制**（属性"改名"=改翻译）：

- 文件族：源词典 LdapAttributes.dict（打开定制工具必选 C:\8770\Client\dict 下该文件）；用户词典只存被改属性；客户端分发包 dict_user.zip
- 保存一次做三件事：写用户目录、生成 Locales 文件、重打包 dict_user.zip；每次保存 Dictionary version number 自增（Administration 应用 OmniVista 8770 页签查看），Set All to Default 回退也自增
- 客户端连接时校验版本并自动下载新 zip
- 同名属性按 Context information 选行：人员信息 Misc1/Misc2 选上下文为空的行；PCX 条目页签名/属性名各选对应上下文行——选错行会改错界面文案
- 硬约束：服务器本机开着 8770 客户端时保存失败（dict_user.zip 被占用）

**Web 客户端定制三层模型**：

| 层 | 谁配 | 生效范围 | 存储 |
|---|---|---|---|
| 默认参数（GlobalParameters/SearchClasses/Grid/Detail/Edit） | 目录管理员 | 全体用户基线；匿名与未定制者都用它 | Administration 应用（LDAP 属性名） |
| 用户参数 | 认证用户自配 | 仅本人已定制页签 | 用户配置 |
| 主题 | 用户可选；Edit 定制仅管理员 | 个人（存 cookie） | C:\8770\Client\Themes 两套 CSS |

- **定制前置**：先导出 DirectoryClient 分支 LDIF + 备份 Themes 文件夹——没有内置一键还原，回退全靠这两步备份（参数 Import > Modify only，主题整目录替换）
- GlobalParameters 常用默认值：地址簿 500 条上限、建条目允许、认证/关联话机/Browse 等图标默认显示

## A1 — 书中案例

**词典与客户端定制实验**（p295-348）：

1. 记录当前词典版本号（默认空）
2. 关闭服务器上运行中的 8770 客户端（防 zip 占用）
3. 打开 Dictionary customization 选 LdapAttributes.dict 与语言
4. 选上下文为空的 Misc.1/Misc.2 改译名（Passport number/Sport），Save
5. 核验版本号自增、Directory/计费/Web 客户端三处显示新名
6. 再改 PCX 条目上下文的 Miscellaneous 与 Misc.1/Misc.2 行并保存
7. Edit > Set All to Default 回退，核验回默认且版本号仍自增
8. 客户端定制前备份：导 DirectoryClient 分支 LDIF + 拷贝 Themes 文件夹
9. GlobalParameters 改地址簿上限 500 到 10、隐藏关联话机图标
10. 配搜索过滤器、网格（行数 6+五列）、详情页三区、编辑页属性
11. 换两套主题 Logo/背景色；jean dupont 配用户参数（行数 5）验证个人视图
12. 回退：Import > Modify only 导入备份 LDIF，Themes 目录替换后核验全默认

## A2 — 未来触发

使用情境：客户要改目录字段显示名；界面要贴合企业 VI；员工说个性化设置丢了；搜索/列表列/详情页要调整；改了词典不生效；定制改坏了怎么回退。

语言信号：词典 / dictionary / CustomDict / dict_user.zip / 属性改名 / Context information / 客户端定制 / Customize / GlobalParameters / Grid / Detail / theme / 主题 / cookie / 默认参数 / 回退。

与相邻能力区分：

- 谁能改这些配置（权限档）→ 保密能力的访问级别与域的组档
- 属性值本身的数据维护 → LDIF 工具能力
- LDIF 的 Modify only 回退用法 → LDIF 工具能力

## E — 可执行步骤

输入契约：定制需求清单（字段名/界面/主题）、目录管理员账户、维护窗口（词典保存需关服务器端客户端）。

1. 备份先行：导 DirectoryClient 分支 LDIF + 整拷 Themes 文件夹。完成标准：双回退点在手
2. 词典定制：关服务器端客户端 > 选源词典 > 按上下文选行改译名 > Save。完成标准：版本号自增
3. 三处核验：Directory 应用、计费应用、Web 客户端显示新译名。完成标准：三处一致
4. 全局参数：GlobalParameters 按业务调整（地址簿上限/图标开关）。完成标准：匿名会话可见变化
5. 界面定制：搜索过滤器/网格/详情/编辑按对象类型逐层配（LDAP 属性名）。完成标准：各页签生效
6. 用户参数与主题：认证用户自配个人视图；主题 Edit 仅管理员。完成标准：个人视图隔离生效
7. 回退演练：Import > Modify only + Themes 替换，核验全默认。完成标准：回退闭环

判停点：

- 保存词典失败 → 服务器本机 8770 客户端没关（zip 占用，n16），关掉再存
- 改了 A 属性 B 变了 → 同名属性上下文选错行（n15），重选正确 Context information 行
- 客户验收要求"用户个性化永久保存" → 讲清回落规则：主题存 cookie、未定制者用默认（n20），改验收口径
- 定制出错要回退 → 只能用事先备份；没做第 1 步就没有安全回退点（n18），只能手工逐项改回
- 字段说明与实际不符 → p330 存在串行勘误（nr-03）：以字段名与实测为准

输出契约：词典与客户端定制基线 + 备份回退点（LDIF+Themes）+ 版本号与三处核验记录。

## B — 边界

- 词典路径书内双口径（nr-04）：操作统一按 How-To 的 C:\8770\Client\dict，讲义 C:\8770\dict 仅背景
- 版本号只增不减：它不代表"改了几处"，不能当变更审计账本
- 主题仅两套（theme1/theme2，CSS 构成）：深度 UI 改造属前端工程，超出词典/参数定制域
- GlobalParameters 数值（500 条地址簿等）为默认值口径（p328），实验改 10 为教学要求（实验口径）
- 属性必须写 LDAP 名（如 sn/givenname），写界面译文无效（p331）
