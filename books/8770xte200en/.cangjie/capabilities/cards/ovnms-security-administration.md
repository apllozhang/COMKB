# OmniVista 8770 安全管理（密码策略 / 管理员与组 / 访问控制 / TLS）

## R — 原文依据

> "An administrator account can belong to several groups. For each application, the highest access level found is used"（p398）
> "11 Access Profiles are available ... 0 YES Gives access to all objects, all attributes, and all actions ... 10 YES Specially designed for attendant management"（p399）
> "The Secure access for system management option must be set up to enable OXE control access."（p408）
> "When configuring password aging, respect the rule (B) + (C) < (A)"（p385）
> "ALL THE NETWORK ELEMENTS IN THE INFRASTRUCTURE ... MUST BE TLS COMPATIBLE."（p414）

出处：8770XTE200EN p363-415（Security 应用讲义与 How-To、POODLE 附录）。

## I — 自述

安全模型三层，逐层收敛管理面：

**第一层：8770 账户与组（Security 应用）**

- 密码策略字段：质量规则、最小长度、历史、首登改密、失败锁定次数与锁定时长（0=仅管理员可解锁）、时效三参数 A（有效期）/B（提前警告天数）/C（最短改密间隔），必须满足 B+C<A
- 预定义账户：AdminNmc（全权主账户）、Alcatel4059（话务台专用）、MSAD8770Admin（AD 同步服务账户）、Thirdparty8770Admin（API 开通服务账户）
- 组与权限：预定义组按角色授权（Accountants/Network experts/Simplified Configuration 等），成员继承组权限；账户在多组按应用取最高访问级——临时拉进高权组后忘记移出即变相提权
- 单登录：勾 Limit user(s) to single login 后同账户第二会话被拒；AdminNmc 与 Normal Administrators 组豁免
- 管理域：OXE 对象按系统域分区授权，默认全域 0，最多 255 个

**锁定解锁四路径**

1. 普通管理员：Security 应用选中账户改密
2. 普通管理员（客户端进不去时）：ToolsOmniVista 选 1 Security > 1 Password Update > 5 Administrator password update
3. AdminNmc 专用：ToolsOmniVista 选 1 > 1 > 4（普通解锁流程对其不适用）
4. WBM 邮件重置：前提=邮件服务器已配 + 管理员账户在 Security 应用 Individual 页填了邮箱；WBM 登录页 Forgotten your password? 收重置码邮件后输码+新密

锁定时 Alarms 应用 NMC > nms > Password policy 下出 Locked user accounts 的 major 告警。

**第二层：OXE Access Profile（Configuration 界面）**

- 11 个 profile（0 全量 / 1 expert / 2 usual / 3 用户管理 / 4-9 自定义 / 10 话务台简化配置），每类对象四级权限 Nothing/Read/Read-Write/All + 属性显隐 + Actions 授权
- 全体 OXE 共用一套——改一个等于改所有；建议在最新版本 OXE 上编辑
- Security 应用给账户/组配 Configuration 访问时选 Access Level（No Access/Configure/All）+ OmniPCX 4400 Access Level（profile 号）
- 改完必须删客户端本地 MIB（Preferences > Configuration > Object Model Save > List > Delete）重载，否则"改了没变化"

**第三层：OXE 侧访问控制**

- Security and Access Control > 1 > User Access Control 建大写账号白名单（填 Security 应用中存在的账户名）；前提=OXE Connectivity 页勾 Secure access for system management
- 开启后需断开 8770 会话重连才生效；重置走 OXE telnet：mao off > multitool SECURITY_ACCESS 选 10 > mao on

**TLS 加固（POODLE 附录）**

- ToolsOmniVista > 1 Security > 2 Minimal SSL/TLS release 选 5（TLS 1.3），同时关闭 SSLv3 及更低
- 硬前提：全网元（OXE/OXO/OpenTouch/SIP 话机/AD/邮件服务器）均 TLS 兼容，否则不能关——该流程书中标注"仅供信息、勿执行"

## A1 — 书中案例

**安全配置实验**（p382-415）：

1. 放宽密码策略（实验口径：取消质量、长度 4、关历史、3 次失败锁定、关时效）
2. 建 user1/user2/Expert1/Expert2 四个管理员
3. user1 入 Accountants 组后以 user1 重开客户端，核对可见应用
4. 开单登录后 user1 第二会话被拒（AdminNmc 不受限）
5. user1 连错 3 次触发锁定告警，四路径分别验证解锁；AdminNmc 用 ToolsOmniVista 选项 4，WBM 邮件重置收码成功
6. 自建组配 Accounting=Read + Fault Management=All，多组取最高核验
7. Profile 9 设 Users=All、Trunk groups=Read，删本地 MIB 后 user2 配置界面只见授权对象
8. EXPERT1 加白名单可进、EXPERT2 未加被拒；TLS 1.3 输出确认（仅供信息演示）

## A2 — 未来触发

使用情境：等保/安审整改；管理员入职离职授权；"改了 Access Profile 没生效"；账户锁定所有人进不去；客户要求关 SSLv3。

语言信号：密码策略 / B+C<A / 锁定 / 解锁 / AdminNmc / ToolsOmniVista / 单登录 / 取最高 / Access Profile / Profile 9 / 本地 MIB / Object Model Save / User Access Control / Secure access / POODLE / TLS 1.3。

与相邻能力区分：用户开通与 COS（用户开通能力）；操作留痕审计（审计合规能力）；本能力管"谁能进、能看什么、密码怎么管"。

## E — 可执行步骤

输入契约：客户密码策略与角色矩阵、管理员清单与分组方案、（如做 OXE 收敛）Secure access 可开启的确认。

1. 密码策略：按客户策略录字段并验算 B+C<A。完成标准：策略保存且验算通过
2. 建管理员并入预定义组。完成标准：每人按角色可见应用，无超权
3. 开单登录并验证。完成标准：普通账户第二会话被拒、豁免账户不受限
4. 预演锁定解锁：连错触发告警后走四路径之一。完成标准：账户恢复且告警闭环
5. OXE Access Profile：在最新版本 OXE 上编辑目标 profile。完成标准：对象级四级权限与 Actions 符合矩阵
6. 删客户端本地 MIB 重载。完成标准：各客户端按新 profile 显示
7. OXE 侧白名单：勾 Secure access > 建大写账户清单 > 断开重连验证。完成标准：名单内可进、名单外被拒
8. TLS 加固（单独立项）：先全网元 TLS 摸底再动 ToolsOmniVista。完成标准：最低协议提升且老网元不失联

判停点：

- AdminNmc 被锁且 ToolsOmniVista 也不可用 → 判停升级，不要反复试错（有锁定告警观察窗口）
- 改 Access Profile 后"没变化" → 先问本地 MIB 删过没，不要回滚配置
- 任一网元不支持 TLS → 停止关 SSLv3，先改造网元
- ToolsOmniVista 改密不经策略校验 → 改完人工核对符合策略，且必须按 0 正常退出

输出契约：密码策略与时效验算记录 + 账户-组-profile 矩阵 + 解锁演练记录 + OXE 白名单清单 +（可选）TLS 摸底表。

## B — 边界

- 与客户 AD/Radius 的外部认证集成只列选项（Radius Server、MSAD 同步账户），完整配置在书外
- ToolsOmniVista 是救援工具：不校验密码策略、非正常退出（不按 0）会让 NMC 服务停在停止态
- 密码时效实验放宽口径（长度 4、关历史）仅教学用；生产按客户策略从严
- 实验账户（user1/Expert1 等）与实验密码见 book/overview；生产凭据一律替换并纳入轮换
- 全书默认单机管理口径，无 8770 集群安全设计
