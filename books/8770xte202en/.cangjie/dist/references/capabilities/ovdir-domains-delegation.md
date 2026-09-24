# 管理域与委派（分域可见性、三预定义组、定制视图）

## R — 原文依据

> "Possibility to split organization in several parts and manage them independently ... Each local administrator sees/manages his own domain for Directory and Users applications"（p429）
> "Required licenses • Domain Management • Directory / Management Domain to be enabled • Feature disabled by default after fresh installation"（p435）
> "Delegation: right for local administrators to create and manage other local administrators within their domain"（p450）
> "Strict view parameter disabled (by default) • Person search can retrieve persons from domain D but also from parent domain(s) • Strict view parameter enabled • ... strictly from domain D"（p454）

出处：8770XTE202EN p429-454, p456-500。

## I — 自述

域是"可见性+管理权"的切割单位：域=名字+一组公司目录 DN 级别+本地管理员名单；可嵌套、可多父。支撑多站点/OXE 多租户/云端多公司三类用例。

- **许可与激活**：Domain Management+Directory 双许可缺一不可（MCS 版自带 Directory 但 Domain Management 仍要买）；功能默认关闭，Security 应用 8770DomainManagement 手工 Enable
- **三预定义组权限档**：

| 组 | 管理面 | 不含 |
|---|---|---|
| Users Configuration | 只管用户（Directory 仅 Partial modification） | 域内目录结构、定制视图 |
| Users & Directory Configuration | 用户+域内目录结构全管 | 定制视图 |
| Users & Customization Configuration | 再加定制视图与 Web Admin 的域/账户管理 | — |

- **本地管理员**：Security 应用建的账户默认是全局管理员（蓝色显示）；归入预定义组并关联域后降为 local，只能查看和管理本域；Domain configuration 菜单对其显示但 inactive
- **Delegation 委派**：Application rights 页签单开——本地管理员可在自己域内再建本地管理员与目录级别（经 WBM）
- **strict view 参数**：域内人员经 Web 目录检索，关（默认）可查本域+父域，开则严格本域；域场景下 Web 目录认证强制、匿名不可用
- **定制视图**：预设开户界面字段（预定义+自定义），按管理员账户绑定；目的是简化本地管理员开户——视图越精简开户越快（书中对比结论）
- **配套**：批量建管理员时实验把"首登强制改密"设 False 以免打断验证（生产保留强制更安全）

## A1 — 书中案例

**管理域搭建与委派实验**（p456-500）：

1. Directory 应用扩树：Portugal/Lisbon/Porto 及三个 Department
2. Help > About 核对 Directory 与 Domain Management 许可均已启用
3. Security 应用 8770DomainManagement 勾 Enable 并 Apply
4. 建六个管理员账户（AdminFrance/Brest/Colombes/Portugal/Lisbon/Porto，实验口径密码）
5. 归组：三人入 Users Configuration、一人入 Users & Directory、两人入 Users & Customization
6. 8770 Domain Management 下建六域，各选目录级别并加成员管理员
7. Password Policy 把首登强制改密设 False（实验口径）
8. AdminBrest 登录厚客户端与 WBM：只见 Brest、仅能管用户、域菜单不可用
9. AdminPorto 同法验证：可管域内目录结构
10. AdminFrance 开 Delegation，经 WBM 建 Nantes/Rennes 级别与两域
11. 建 RennesView 定制视图并绑 AdminRennes（Default view 绑 AdminNantes）
12. 两本地管理员各开户一人，对比开户步数并核验相互不可见

## A2 — 未来触发

使用情境：多站点/多分公司要分权管理；本地管理员该给哪组权限；让分公司自己开户且界面简化；域内的人查不到父域同事；本地管理员要能自己再建管理员；批量建完管理员首登全卡改密。

语言信号：管理域 / domain / Domain Management / 本地管理员 / local administrator / Delegation / 委派 / strict view / 定制视图 / customized view / 可见性 / 多租户。

与相邻能力区分：

- 条目对普通员工隐藏 → 保密能力
- 账户的应用级权限档 → 保密能力的 Security 部分
- WBM 客户端本身的定制 → 客户端与词典定制能力

## E — 可执行步骤

输入契约：组织分域设计（DN 级别边界）、管理员名单与组别、双许可已购。许可缺失 → 判停先补许可。

1. 核许可：Help > About 查 Domain Management+Directory。完成标准：双许可在列
2. 激活：Security 应用 8770DomainManagement 勾 Enable。完成标准：域节点可用
3. 建管理员：按名单建账户（默认全局），归入三预定义组。完成标准：组员对照表落地
4. 建域：选目录级别（o/c/l/ou 任意层）加成员管理员，需要时嵌套。完成标准：域边界成图
5. 委派（按需）：给有下放需求的组开 Delegation。完成标准：本地管理员可自建管理员
6. 定制视图：基于预定义视图关字段另存，按账户绑定。完成标准：开户流程精简可对比
7. 验证：逐管理员登录核可见范围与可管内容。完成标准：与组档一致

判停点：

- 本地管理员要建域/改域 → 不可能（菜单 inactive，n31）；给 Delegation 让其建"自己域内"的级别与账户
- 域内人员查不到人 → 先查 strict view（开=严格本域），再查其所在域与嵌套关系（n33）
- 批量建管理员被首登改密打断 → 实验 False 口径仅为验证顺畅；生产保留强制改密（n32），别搬实验值
- 客户只有 Directory 许可 → 域功能不可用，Security 里开了也建不出域（n30）
- 组权限与讲义表对不上 → p441 与 p463 表述有出入（nr-05），以现场实测为准并记录

输出契约：分域管理体系（域+组+账户）+ 委派与视图配置记录 + 各管理员可见性验证矩阵。

## B — 边界

- 域切割的是 Directory/Users 应用的可见性与管理权：Web 目录匿名在域场景被禁用（p453）
- 定制视图只简化"开户界面字段"，不改权限档；权限仍由组+应用级别决定
- WBM 侧三入口（Domain configuration/Customized views/Administrator configuration）中前者对本地管理员永远 inactive
- 密码策略是全局 Security 配置，不按域分设
- 实验六域与 Portugal 树为教学约定（实验口径），生产按客户组织设计
