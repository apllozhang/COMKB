# MSAD 与 Azure AD 同步管道（服务器声明、属性映射、同步规则、云端拉取）

## R — 原文依据

> "Persons creation from MSAD to 8770 directory • Update of directory attributes in both ways ... Requires a dedicated login on MSAD to update the directory attributes • LDAP or LDAPS connection"（p353）
> "sn (Last name) only from AD to 8770, mandatory to create person in 8770. Can't be deleted"（p356）
> "Only one Attribute Mapping entry can be created."（p380）
> "Complete synchronization All the entries (which satisfy the specified filter) are (re)synchronized ... Need to be done after the creation of the synchronization rule or any modification"（p388）
> "Azure AD is considered as the master node ... Microsoft Graph API, instead of LDAPS for MSAD ... No OXE users provisioning from Azure AD"（p360）

出处：8770XTE202EN p351-361, p368-393。

## I — 自述

企业身份数据管道两条平行通道：MSAD（本地 AD，双向属性同步）与 Azure AD/Entra ID（云侧，8770 拉取）。

**MSAD 三层结构**：

- **Access info 服务器声明**（可声明多台 AD）：Name/Host/Port（389，LDAPS 为 636）/Username/Password/Is LDAPS/Automatic deletion of 8770 users/Scope。保存即发 LDAP bind，绑定成功才能建条目；AD 侧需专用管理员账号（入 Domain Admins 组）
- **Attribute mapping（全 8770 只能建一条）+ Synchronization rule（可多条）**：规则定义 8770 CD 位置与 MSAD OU 位置、Filter（默认 objectclass=user 且 cn 非空）、Flat/Tree 模式，经 Scheduler 调度
- **映射硬规则五条**：sn 只能 AD 到 8770 且不可删；隐藏映射 abObjectGUID 来自 objectGUID 保唯一；电话/ISDN 号只能 8770 到 AD；uid 只能 AD 到 8770（更新走改名）；附加属性可加且方向可调、空值可给默认值

**调度与边界**：

- 规则新建或映射/规则修改后必须跑一次 Complete；日常用 Partial（按上次同步日期增量）
- AD 删人二态：Automatic deletion=False（默认）只标记删除待人工确认；True 连 OT/OXE/8770 一起永久删
- AD 侧姓/名全空的用户不同步；8770 侧新建/删除人员不回写 AD（仅修改人员回写）

**MSAD 与 Azure AD 差异**：

| 维度 | MSAD | Azure AD |
|---|---|---|
| 主节点 | 对等双向属性同步 | Azure AD 恒为主节点 |
| 认证 | LDAP 389 / LDAPS 636（需 AD CS） | Microsoft Graph API（应用机密+权限） |
| OXE 用户供给 | 可经插件 provision | 不 provision OXE 用户 |
| 模式 | Flat/Tree | Flat/Tree（tree 需 Directory 许可） |
| 配置骨架 | 声明+映射+规则 | Azure 准备、租户信息、规则、映射四步 |

## A1 — 书中案例

**MSAD 声明与同步实验**（p368-393）：

1. AD 服务器（Ecosystem 实例）建用户 MSADadmin，密码按实验口径设不可改永不过期
2. MSADadmin 加入 Domain Admins 组，Member Of 核验
3. Administration 应用 MSAD Management 建 Access info 八字段，Scope 选公司目录根
4. Apply 后 LDAP bind 通过、条目建成
5. AD 侧建 OU 树（勾防误删保护）与两个测试用户，一人设 Employee Number
6. 建 Attribute mapping：保持默认，附加 Mobile（8770 到 MSAD）与 Employee number（MSAD 到 8770）
7. 建 Synchronization rule：位置两侧各选，模式 Tree，Filter 保持默认
8. 右键规则跑 Complete：8770 目录出现 AD 分支镜像与两人
9. 两侧各改 Mobile 再跑 Partial：以 8770 侧值为准双向一致
10. False 态删 AD 用户跑 Complete：目录中标为已删除
11. Access info 改 True 态再删另一 AD 用户跑 Complete：目录条目消失
12. 重建测试用户供后续实验使用

## A2 — 未来触发

使用情境：对接客户 Active Directory；同步规则建了但人没进来；改了映射数据没变化；AD 删人后 8770 还挂着；客户用 Entra ID/Azure AD；想做"电话号码以 AD 为准"的方案。

语言信号：MSAD / Active Directory / LDAPS / Access info / attribute mapping / objectGUID / synchronization rule / Flat / Tree / Complete / Automatic deletion / Azure AD / Entra ID / Graph API。

与相邻能力区分：

- AD 里右键手动开户（不经同步周期）→ MSAD 插件能力
- 目录树/位置语法基础 → 自动创建能力
- 批量 LDIF 文件管道 → LDIF 工具能力

## E — 可执行步骤

输入契约：AD 服务器版本（2016/2019/2022 口径）、专用管理员账号（Domain Admins）、Active Directory integration 许可、LDAPS 需 AD CS。许可或账号缺失 → 判停。

1. AD 侧建专用管理员并入 Domain Admins，密码策略按客户安全要求。完成标准：账号可绑定
2. 声明 Access info：八字段齐、Scope 对准目标根、Port/LDAPS 按加密方案。完成标准：bind 成功条目建成
3. 建 Attribute mapping（唯一一条）：默认映射+按需附加属性与方向/默认值。完成标准：sn 方向未动
4. 建 Synchronization rule：两侧位置、Filter、Flat 或 Tree。完成标准：规则保存
5. 跑 Complete 全量并核验镜像结构与人。完成标准：首量一致
6. 变更管理：任何映射/规则修改后重跑 Complete；日常排 Partial 周期。完成标准：变更后数据一致
7. 删除策略：先 False 观察标记删除，评估后决定是否切 True。完成标准：策略成文并告知客户

判停点：

- 想做"电话以 AD 为准" → 与映射硬规则冲突（电话只能 8770 到 AD），改方案或向客户对齐（n21）
- 改了映射但同步结果没变 → Partial 不感知结构性变更，必须 Complete（n25）
- AD 用户同步不进来 → 先查姓/名是否为空（空则不同步），再查 Filter 条件
- 删除需求是"连 OXE 话机一起删" → 这会切 True 永久删除三系统，先书面确认影响面（n23）
- 客户要求 LDAPS → AD 侧先装 AD CS 发证书，否则 Is LDAPS 勾了也连不通（p377）

输出契约：已声明的 AD 管道（映射+规则）+ 首量与增量验证记录 + 删除二态策略说明。

## B — 边界

- 映射全 8770 只能建一条：多部门多 AD 靠多规则/多 Access info，不靠多映射（p380）
- "双向"不对称（n22）：8770 新建/删除不回写 AD；AD 姓名全空不同步
- LDAPS 仅 MSAD 声明支持且需 AD CS；复制通道不支持 LDAPS（复制能力卡 Boundary 另述）
- Azure AD tree 模式另需 Directory 许可（p360）；本书该章无配套实验，属讲义口径
- Windows Server 支持清单止于 2022（Ed40 印刷口径）：更新版本以官方兼容文档为准
