# 档案与用户供给（三类用户、双侧档案、WPC 批量）

## R — 原文依据

> "This is a directory user - Without any node properties (no device and no applications) ... User has one or more OXE devices - Can have access to OpenTouch applications"（p258）
> "Only profile modification is allowed via Users application. Creation and deletion must be done via OXE or OpenTouch configuration application"（p278）
> "If some OXE profiles need to be created, they will be automatically displayed on Users application. After OpenTouch profiles creation, a complete synchronization is required to make them displayed"（p297）
> "Available from OmniVista 8770 3.2.8 with Unified management license ... Only support of Chrome versions from 54"（p290, p292）
> "TUI password ... Available characters are digits (6 digits minimum). Passwords composed of a logical series of digits (for example: 12345, 65432 or 13579) are refused by default."（p286）

出处：OPENXTE300EN p255-301。

## I — 自述

用户供给三件套：OXE 档案、OT 档案、语音邮箱档案，三者合成一个 Connection user（ACU，Advanced Communication User）。三类用户对照：

| 用户类型 | 界面取值 | 设备与应用 |
|---|---|---|
| Directory user | type=None | 无设备无应用，仅进公司目录 |
| OXE 用户（无 OT 权） | type=OXE，Applications=None | 有话机，无 OT 应用 |
| Connection user | type=OXE，Applications=OT | 话机 + OT 应用 + 可有邮箱（ACU） |

双侧档案与同步不对称：

- **OXE 档案**：OXE 配置工具建，Set function=Profile，目录号用 A0000 式字母占号省号段，Profile Name 必须大写；建完经实时事件直达 8770，无需同步。
- **OT 档案**：OT 配置工具 Users and devices/User/Profile 建，Category 必须选 ACU-OXE，Licenses 页勾 Desktop/Voice mail/Conferencing 等权；建完必须做一次完整同步才在 Users 应用可见。
- **权限边界**：Users 应用只能修改档案；新建与删除必须回 OXE/OT 配置工具。

Web Provisioning Client（WPC）：版本门槛 OmniVista 8770 3.2.8 且须 Unified management 许可；浏览器仅 Chrome 54 及以上；三条限制——档案的建删仍回配置工具、不能新建 OpenTouch Conversation 用户、每用户只关联一台设备。

口令策略：GUI 口令字母数字；TUI 口令至少 6 位纯数字且默认拒绝顺序数列；SIP 口令仅 SIP 分机设备需要。实验放宽（最小长度 5、允许 trivial）仅限 LAB，现场绝不建议。

## A1 — 书中案例

**档案与用户实验**（p272-288）：

1. 前置：OXE 开 Use profile with auto. recognition。
2. 建 OXE 档案：Set function=Profile、A0000 式占号、名称全大写。
3. 建 OT 档案：Category=ACU-OXE，Licenses 页勾所需权项。
4. OT 档案建完对 OT 发起一次完整同步。
5. Directory 应用建部门树，把目标层级建出来。
6. Users 应用右键 Create user 逐个建三类用户。
7. Connection 用户填登录名、GUI/TUI 口令、OT 模板与站点。
8. Connection 用户再填语音邮箱服务器与邮箱档案。
9. 存量用户加 OT：补邮箱地址、Applications=OT、模板与站点。
10. 收尾三侧核验：目录有其人、OXE 有分机、OT 有用户与邮箱档案。

**WPC 批量实验**（p295-301）：

1. 前置四查：OXE 档案在机、空闲号段、OT 档案、Users 应用档案齐全。
2. Chrome 打开 8770 的 WPC 地址并用 nmc 管理员登录。
3. 左树选部门后新建用户，Users 页签填类型与姓名邮箱。
4. OXE Rights 页签选 OXE、分机、话机型号与 OXE 档案。
5. Application 页签填 OT 登录、口令、站点、OT 档案与邮箱。
6. Devices 页签核对话机，启用手机权时另配移动四参。
7. Save 后在部门树核验新用户。

## A2 — 未来触发

使用情境：建了用户登不上 OT；档案在 Users 应用里看不到；几十上百人批量开户；用户改不了自己的 TUI 密码；WPC 打不开或选项缺失。

语言信号：档案 / profile / ACU-OXE / Connection 用户 / ACU / Set function / 占号 / Directory user / WPC / Web Provisioning / Chrome / TUI 口令 / GUI 口令 / 批量 / MACD / 移动加删改。

与相邻能力区分：邮箱档案参数与留言行为归语音邮箱能力；Desktop 许可与客户端形态归客户端能力；8770 声明与同步机制见节点声明与 SIP 能力。

## E — 可执行步骤

输入契约：拨号计划内空闲号；OXE/OT 档案设计（权限矩阵）；口令策略决策；WPC 版本前提（8770 3.2.8+ 与 Unified management 许可）。

1. 建档案三件套并完成 OT 侧完整同步。完成标准：Users 应用可见全部档案
2. 目录树规划并落地到 Directory 应用。完成标准：目标层级存在
3. 逐个建用户，三类分清（Directory/无 OT 权/Connection）。完成标准：三侧可查且符号正确
4. 存量加 OT 或用 WPC 批量（按量级与版本前提选择）。完成标准：登录测试通过
5. 交付核对：OT 模板、邮箱服务器、Licenses 勾权与设计单一致。完成标准：逐项核对无偏差

判停点：

- 用户建了但登不上 OT → 查 Applications 是否=OT、模板与站点是否填全
- OT 档案不在 Users 应用 → 没做完整同步（OXE 档案才走实时事件）
- 想在 Users 应用新建或删除档案 → 设计不允许，回 OXE/OT 配置工具
- TUI 口令被拒 → 6 位纯数字且拒绝顺序数列；实验放宽不可带生产
- 一台用户要绑多台设备 → WPC 只支持一台，多终端走客户端能力

输出契约：可登录用户清单（档案/权限/终端/邮箱挂钩）+ 口令交付记录 + WPC 批量结果报告。

## B — 边界

- 实验口径（生产必须替换）：用户口令 12345/54321、登录名 adams/barkley/backman、档案名 BASIC/EXECUTIVE 与 Basic-Connection/Executive-Connection、占号 A0000/A0001、目录层级 France\Brest\Training。
- 口令放宽（最小长度 5、允许 trivial）原书两处强调仅限 LAB（p281/p284）。
- WPC 不能建 OpenTouch Conversation 用户；OT 用户的称呼字段（Salutation）强制（p292）。
- Conversation user 在本书无正式定义，仅零星提及，按备查处理（术语落位见 references）。
- 档案可继承的默认属性清单见 p274（Cost Center、各类 COS、话机特性等），改属性前先核继承面。
- 建用户时 OT 密码策略放宽属实验动作，生产按口令基线（n09）。
