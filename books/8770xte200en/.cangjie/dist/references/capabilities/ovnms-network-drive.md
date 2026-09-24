# OmniVista 8770 网络驱动器映射（报表与备份落网络存储）

## R — 原文依据

> "Creation of the REPORTS_ECO et BACKUP_ECO folders on the ecosystem server ... Creation of a user account named ADM8770 with access rights on folders previously created"（p669）
> "ExecdEx service is linked to report generation facility. SaveRestore service is linked to backup & restore facility."（p669）
> "ADM8770 account must be member of Administrators group. ADM8770 account must be removed from Users group"（p680）
> "Assign the following rights to ADM8770 account: Access this computer from the network / Log on as a service / Act as part of the operating system / Adjust memory quotas for a process / Replace a process level token"（p684）
> "Username Enter account in uppercase preceded with the following characters .\ (i.e. .\ADM8770)"（p696）

出处：8770XTE200EN p668-698（Map network drive How-To）。

## I — 自述

让报表导出（ExecdEx）与备份恢复（SaveRestore）两个服务能写网络存储——核心是"同名同密账号 + 服务账号注入"。

**远程存储服务器侧（三步）**

1. 建 AD 账号 ADM8770（密码策略设为不可更改、永不过期——服务账号口径）
2. 建两个共享文件夹：报表导出用（如 REPORTS_ECO）与备份用（如 BACKUP_ECO）
3. 共享授权：ADM8770 读写；Advanced Sharing 限制并发用户数、移除 Everyone

**8770 服务器侧（四步）**

1. 建本地同名同密账号 ADM8770（服务访问凭据比对依赖同名同密）
2. 组调整：加入 Administrators 组、移出 Users 组
3. Local Security Policy > User Rights Assignment 赋五项权利：从网络访问此计算机 / 作为服务登录 / 作为操作系统一部分 / 调整进程内存配额 / 替换进程级令牌
4. 注销 Administrator、以 ADM8770 登录后映射网络驱动器（盘符自定，实验用 Y:/Z: 两共享）

**服务账号注入与验收**

- Administration 应用 nmc > OmniVista 8770 > nms > Service：给 ExecdEx（报表导出）与 SaveRestore（备份恢复）配 Nt account——用户名 .\ADM8770（大写、带 .\ 前缀）+ 密码
- 验收：8770 Maintenance 立即备份对话框 > 取消默认目录 > Search，列表出现网络共享位置即为通

## A1 — 书中案例

**网络盘实验**（p668-698）：

1. ecosystem 服务器建 ADM8770（实验密码见 book/overview；勾不可改密/永不过期）
2. C 盘根建 REPORTS_ECO 与 BACKUP_ECO 并共享授权（限并发、移 Everyone）
3. 8770 服务器建本地 ADM8770：入 Administrators、移出 Users
4. 逐项赋五项用户权利
5. 以 ADM8770 登录映射 Y:（REPORTS_ECO）与 Z:（BACKUP_ECO）
6. ExecdEx 与 SaveRestore 配 .\ADM8770 + 密码
7. 立即备份对话框 Search 见 BACKUP_ECO/REPORTS_ECO 网络位置，验收通过

## A2 — 未来触发

使用情境：生产部署把备份与报表落到客户 NAS/存储服务器；备份对话框看不到网络位置；服务账号密码轮换后备份失败。

语言信号：网络驱动器 / Map network drive / ADM8770 / REPORTS_ECO / BACKUP_ECO / ExecdEx / SaveRestore / Nt account / .\ADM8770 / 用户权利 / Log on as a service / 同名同密。

与相邻能力区分：备份恢复执行（备份恢复卡）；报表生成（报表任务卡）；本能力管"存储通路"，是两者的生产化前置。

## E — 可执行步骤

输入契约：客户存储服务器地址与共享规划、服务账号命名与密码策略口径、8770 服务器本地管理员权限。

1. 存储侧建账号与共享：ADM8770 + 两个文件夹读写授权。完成标准：并发受限且无 Everyone
2. 8770 侧建同名同密本地账号。完成标准：两台机器凭据一致
3. 组与权利：入 Administrators、移出 Users、赋五项权利。完成标准：逐项可在 Local Security Policy 复查
4. 映射驱动器：以 ADM8770 登录后映射共享。完成标准：资源管理器可见网络盘
5. 服务账号注入：ExecdEx 与 SaveRestore 配 .\ADM8770 + 密码。完成标准：保存无报错
6. 验收：立即备份对话框 Search 见网络位置。完成标准：备份可选网络目录

判停点：

- 立即备份对话框看不到网络位置 → 按序查映射（是否以 ADM8770 登录时映射）、服务账号、五项权利，不要改用本地盘凑合
- 密码被改导致备份失败 → 两台机器同步改并更新服务账号；密码策略（不可改/不过期）为服务账号口径，需客户安全侧确认
- 客户安全策略不接受五项权利全量 → 与客户裁剪组合并记录（原书 Notes 允许按策略裁剪）

输出契约：共享与授权清单 + 账号/权利配置记录 + 服务账号注入记录 + 备份网络位置验收截图。

## B — 边界

- 环境值（共享地址 151.1.1.100、盘符 Y:/Z:、账号密码 superuser 等）为实验口径，见 book/overview；生产按客户存储与命名规范替换
- ADM8770 是服务账号：密码不可改/不过期与客户密码策略可能冲突，须事前对齐
- ExecdEx/SaveRestore 服务身份变化后，旧任务（计划备份/报告分发）应重跑验证一次
- 该 How-To 为 Windows 环境专用；NAS 协议级备份（NFS/S3 等）在书外
