# 目录搜索与 Single Business Card（UDAS 同步、合并、照片同化）

## R — 原文依据

> "Directories synchronization is a one way directory synchronization ... all the searches are made in the synchronized database (synchronized directories) and not directly in the declared directories storages"（p222）
> "A contact card = 4 default attributes + [1 .. 5] dynamic attributes"（p224）
> "'Merge keys' are composed by several contact attributes (two minimum: firstname & lastname)"（p252）
> "Tips Synchronization Date, Time and period MUST BE SET. Synchronization period >= 1 (NEVER SET period to 0)"（p244）

出处：OPENXTE301EN p218-263。

## I — 自述

目录搜索永远查"同步库"，不查源目录——同步参数不设就是空库：

1. **数据流**：OXE 电话簿（phonebookdir）、OT 内部目录（internaldir）、外部 LDAP（ldapdir）单向同步进 PostgreSQL 同步库；客户端经 Chameleon Web Service 查询
2. **联系人卡**：4 个默认属性（sn/givenName/mail/telephoneNumber）恒可搜 + 最多 5 个可选属性参与搜索（预置 20+ 可选）；photo 只能 Displayable 不能 Searchable，且可选属性搜索非所有客户端支持
3. **Single Business Card 合并**：按 Synchronization Order 定权重（高覆盖低），Merge keys（至少姓+名，可加电话）识别同一人；每个键可配预处理（去前缀/去后缀/取前 n 字符，实验例 3 键各取 12 字符、first name 去 "_DECT" 后缀）
4. **照片同化三级**：Avatar（存 internaldir）> LDAP 照片 > 本地照片；删除 Avatar 后 LDAP 照片回显；机制仅在合并开启时有意义
5. **话机侧**：PRS 选 "Presentation server - opentouch" 后，80x8 话机经 Communicate by name（IP Touch 应用声明）走 UDAS 找人；OXE 用户还可配 LDAP 溢出（电话簿声明+Entity 挂索引+系统参数放行）
6. **高级搜索语法**：最多 5 个关键字、% 前缀通配、- 排除

## A1 — 书中案例

**目录域全流程实验**（p243-263）：

1. 内部目录与电话簿：勾激活并设同步 date/time/period（period≥1）
2. 声明 LDAP 服务器（eco.company.com:389，实验口径）
3. 新建 AD 目录：Root=cn=users,dc=company,dc=com、Access 账号 directory（实验口径）、Field names 四映射、Force synchronization
4. 可选属性：Photo 设 Displayable 并映射 LDAP 属性（searchable 不可用）
5. SBC 合并：勾 Merge activation、定 Merge Period（非 0）、browse 定 Synchronization Order（AD 最高）
6. 各目录配 Merge keys（姓+名必选，配预处理规则）
7. 维护：chameleond/udas 日志核查，照片在 /var/data/slides/d.DEFAULT/ 检查
8. 话机：PRS 选 opentouch、建 Communicate by name 应用（Registration URL 指向 /eccnoe/myphone）
9. LDAP 溢出：电话簿索引 1-5 声明、Entity 挂索引、系统参数勾选

## A2 — 未来触发

使用情境：来电识别与按名找人多目录方案；搜不到联系人排障；同名联系人合并成一张名片；联系人照片从哪来；话机键盘找人；OXE 用户溢出查 LDAP。

语言信号：目录 / directory / UDAS / 搜索 / search / 同步 / synchronization / Single Business Card / SBC 合并 / merge keys / 联系人卡 / contact card / 照片 / photo / Avatar / LDAP Phone Book / Communicate by name / PRS。

与相邻能力区分：LDAP 认证（登录验证）→ 外部认证能力（同为 LDAP 但机制不同，勿混）；实验环境 LDAP 服务器 → 实验 POD 能力（路由卡）。

## E — 可执行步骤

输入契约：目录清单（内部/电话簿/AD/LDAP）、账号与属性名、合并需求（权重与识别键）、话机型号。

1. 声明源目录并逐个设同步三参数（period≥1）。完成标准：Force synchronization 后同步库有数据
2. 属性映射：4 默认属性 + 按需选可选属性（≤5 参与搜索）。完成标准：搜索结果字段正确
3. 合并配置：Merge activation、权重排序、每目录 Merge keys 与预处理。完成标准：同名联系人合为一张名片
4. 照片同化核验：Avatar>LDAP>本地，缺图查照片目录并手动同步。完成标准：名片照片显示
5. 话机侧：PRS 绑定、Communicate by name 声明。完成标准：80x8 键盘可按名拨人
6. （按需）LDAP 溢出：电话簿 1-5、Entity 挂索引、系统参数放行。完成标准：OXE 用户可溢出查询

判停点：

- "搜不到人"第一排查项 → 同步参数三处（内部/电话簿/LDAP 目录）是否设置且 period≥1、Merge Period≠0
- 可选属性搜不到 → 三重边界逐项核：是否在 5 个限额内、该属性是否有 searchable 开关、客户端是否支持
- LDAP 溢出容量引用 → 按实验页 5 个做 OXE 上限；讲义 20 的语境存疑（nr-01），引用注明出处
- 合并后数据不对 → 查权重（高覆盖低）与 Merge keys 预处理（12 字符/去后缀规则）

输出契约：目录清单与同步参数记录 + 合并/照片核验结论 + 话机找人验证 + 溢出配置（如启用）。

## B — 边界

- 同步是单向快照：源目录变更要等下个周期或手动 Force synchronization
- 照片目录路径与同步库为服务端内部口径，排障用（/var/data/slides/d.DEFAULT/）
- merge keys 每个参与合并的目录都要单独配置，漏一个目录即合并不全
- LDAP 服务器声明（eco.company.com:389、directory 账号）为实验口径
- UDAS 不做目录写入/回写，一切以同步库为查询面（单向机制）
