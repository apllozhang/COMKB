# 办公桌共享（DSS/DSU、虚拟 MAC、系统选项）

## R — 原文依据

> "A shared terminal is called a Desk Sharing Set (DSS) … A roaming user using a DSS is called a Desk Sharing User (DSU)"（p330）
> "'aa:bb:xx:xx:xx:xx' → xx:xx:xx:xx is replaced by the directory number of the DSU • Example for the DSU user 31000 : 'aa:bb:00:03:10:00'"（p333）
> "Allow Reset of Busy DSU True: … the call is released … An incident '6004' is generated."（p346）

出处：ENTPXTE401EN p327-351。

## I — 自述

工位漫游：DSS=共享话机（真 MAC 注册，配 LogOn 键+Help Desk 键），DSU=漫游用户（自动获得虚拟 MAC aa:bb:分机号，配 OverLogOn/LogOff 键），登录即恢复键位/特性/邮箱。虚拟 MAC 是应用层标识，物理帧仍用真地址；前缀默认 62（OverLogOn）/63（LogOff），COS 放行。

五个系统选项：

1. 登出免密（默认 False）
2. 忙时 DSU 重置（默认 True：通话被释放并发 6004；False 则保通话但异机登录显示 Unauthorized）
3. 首次登录强制改密（默认 False）
4. 定时全员自动登出（-1 关闭；0-23 点）
5. 免重启即时登录（默认 True，仅 NOE3GEE/IP Essential/Enterprise 同族同节点且无 AOM，IPDSP 不适用）

## A1 — 书中案例

**配置与验证**（p338-351，实验口径号码）：

1. Prefix Plan 建 62/63 两前缀，COS 放行 Desk Sharing Over Logon/Logoff
2. 建 DSS：Users 建共享话机对象（Set Function=Desk Sharing Set）；IPDSP 需开 IP-Softphone emulation
3. 改 DSU：把漫游用户 Set Type 改话机型号、Set Function=Desk Sharing User；TSC IP user 自动出现虚拟 MAC
4. DSS 配键 1=62（LogOn）+键 2=Help Desk 号；DSU 配键 1=62（OverLogOn）+键 2=63（LogOff）
5. 系统参数五项按客户策略核对（默认值见 I 段）
6. 验证：登录/登出/忙时被顶（6004）/定时登出；dsstat 13 项、domstat DS 列（S=DSS/U=DSU）、ippstat 判读（登出态虚拟 INTIP 255/255）

## A2 — 未来触发

使用情境：共享工位/轮班坐席；"工位随便坐、配置跟着人走"；DSU 通话中被顶的客诉；混机型办公区的登录体验承诺。

语言信号：desk sharing / DSS / DSU / 办公桌共享 / 虚拟 MAC / aa:bb / LogOn / LogOff / OverLogOn / 62 / 63 / 6004 / dsstat / ippstat / free seating。

与相邻能力区分：一号多机（固定关联）→ multi-device（路由卡）；登录底层的注册与 TFTP 属装机域（Starter）。

## E — 可执行步骤

输入契约：机型清单（对照支持面）、前缀/COS、系统选项策略（忙时重置与自动登出先和客户对齐）。机型不在支持清单 → 判停。

1. 配前缀与 COS：62/63 建好并放行。完成标准：前缀可拨
2. 建 DSS 与 DSU：Set Function 角色化配置。完成标准：TSC IP user 见真/虚拟 MAC
3. 配键：DSS（LogOn+Help Desk）、DSU（OverLogOn+LogOff）。完成标准：四键可用
4. 定系统选项：忙时重置/自动登出/免密/即时登录按客户策略。完成标准：与书面承诺一致
5. 验证：登录恢复配置、登出清空、6004 行为符合所选策略。完成标准：dsstat/ippstat/doministat 证据齐

判停点：

- 客户要求"通话中绝不能被顶" → Allow Reset of Busy DSU=False，并告知代价（忙时无法异机登录、跳过自动登出）
- 客户要求 IPDSP 即时登录 → 不适用（明确排除），体验回落为重启式切换
- DSU 登录显示 Unauthorized → 查忙时重置是否被设为 False 且该 DSU 正忙

输出契约：可漫游的 DSS/DSU 池 + 系统选项策略记录 + 6004/自动登出的行为说明。

## B — 边界

- 适用机型：8 系列 IP Touch EE、IP Premium、IP Essential/Enterprise、IPDSP（p329）；即时登录仅 NOE3GEE/Essential/Enterprise 同族同节点无 AOM（p336）
- 虚拟 MAC 是应用层标识；ippstat 登出态显示虚拟 INTIP 255/255（p333/p350）
- 话机侧清除走 I+# → IP parameters → Free seating（实验口径菜单）
- 前缀 62/63 为书内建卡示例值，现场以 Prefix Plan 实查为准
