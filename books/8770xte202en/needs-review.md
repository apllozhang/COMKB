# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。nr-01~nr-03 为提取器登记的书内勘误（推断），nr-06~nr-08 为生产风险引用项。

## nr-01 p95 节点号公式示例与公式自相矛盾（erratum，推断）

- **位置**: p95 "Subnetwork – Node number Enter a numeric value equal to the OmniPCX Enterprise network*100 + OmniPCX Enterprise node number. Example: With a network number = 1 and node number = 2, you must enter 101"
- **差异**: 按公式 1*100+2 应得 102，书例写 101；实验实配网络 1/节点 1 亦得 101。
- **判断**: 合理读法为"百位=网络号、末两位=节点号"（推断为公式表述或示例之一有误）。
- **处置**: 能力卡按"百位=网络号、末两位=节点号"表述并标注推断；实配时以 siteid 输出的真实网络/节点号拼装并现场验证。

## nr-02 p120 同名实验第二个用户的 UID 描述与步骤不符（erratum，推断）

- **位置**: p120 Notes "it's UID is 'Thomas Anderson 31024'"。
- **差异**: 按实验逻辑第二个创建的用户是 31023，UID 应为 "Thomas Anderson 31023"，与前文 4.1.3 节自相矛盾。
- **处置**: 保留原文不改；能力卡引用 UID 结果时用 31023 口径并注明原书排版勘误。

## nr-03 p330 GlobalParameters 字段说明串行（erratum，推断）

- **位置**: p329-330 "Display Define associated station icon Disabled: the tab 'Browse' is hidden in the Web Directory client."
- **差异**: 按 p328 字段定义，隐藏 Browse 页签是 "Display browse tab" 的职责；本行应为 Define associated station 图标被隐藏。
- **处置**: 配置时以字段名为准、以实测为准；能力卡引用该字段表时标注"原文说明串行"。

## nr-04 词典文件路径两处口径并存

- **位置**: 讲义 p299 "The .dict files are stored in the folder C:\8770\dict." vs How-To p309 "you always must select the 'LdapAttributes.dict' file from C:\8770\Client\dict\."
- **判断**: 同一词典族在书内两处路径表述并存（实验口径差异），原文如此。
- **处置**: 操作步骤统一按 How-To 的 C:\8770\Client\dict 为准；讲义路径保留作背景。用户词典只存被改属性、Set All to Default 也自增版本号（n17）随此口径一并说明。

## nr-05 本地管理员组权限档讲义与实验表述出入

- **位置**: 讲义 p441 Users Configuration 组 "Access level/App: All/Users + ..." vs 实验 p463 同组写 "Write/Users"。
- **差异**: All/Users 与 Write/Users 语义不同，两页口径不一。
- **处置**: 能力卡以讲义 p441 三档为主口径并标注 p463 原文如此；交付时以现场实测权限为准。

## nr-06 MSAD 插件强依赖 Internet Explorer（生产风险，引用项）

- **位置**: p413-414 信任站点加 nms.company.com（否则界面缺字段）、允许"我的电脑"上的活动内容、IE9 另需 active scripting。
- **影响**: 现代浏览器/新 Windows 环境下该流程能否复现是版本风险点（BOOK_OVERVIEW 批判章亦点名）。
- **处置**: ovdir-msad-plugin 卡 Boundary 标记为交付前置核查风险项；界面缺字段先查这三项，不要重装插件。

## nr-07 目录复制不支持 LDAPS（生产风险，引用项）

- **位置**: p511 "Host: Port: ... (LDAPS is not supported by the replication)"；对照 p377 MSAD 声明支持 LDAPS（需 AD CS 角色）。
- **影响**: 复制流量明文——同一台 8770 上 MSAD 接入与目录复制两套 LDAP 加密能力不一致，安全方案要分开设计。
- **处置**: ovdir-replication 卡 Boundary 显式声明；客户有加密合规要求时给替代口径（网络隔离/IPSec 层面方案在书外）。

## nr-08 实验明文密码口径（生产风险，引用项）

- **位置**: 全书（例 p47 AdminNmc/Superuser01*、p90 Superuser2580*、p407 插件 properties 内加密密码原样印刷）。
- **影响**: 教学约定值不可迁移生产；插件配置文件含凭据需访问控制；复制管理器密码默认沿用 superuser，应经 toolsOmniVista.exe 单独设置。
- **处置**: 全部环境值只进 Boundary 与 book/overview；各能力卡 E 段不使用具体口令作默认值。

## nr-09 含推断成分的结论标注（引用需带标注）

- n44（节点号拼装读法）、n04（p120 UID 应为 31023）、n19（p330 串行指向）三条均含"推断"成分。
- **处置**: 三条已在对应能力卡保留推断标注，不升格为书中明示事实；复核时若拿到原版 PDF 勘误表以勘误表为准。
