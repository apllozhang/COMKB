# ALES 软终端开通与认证（PC/Android、LDAP/本地、一号多机）

## R — 原文依据

> "Remember, the login information must match with 'uid' of a person managed in the LDAP directory."（p230）
> "14 characters minimum with - at least 2 characters (1 upper case mandatory) - at least 2 digits - at least 1 special character ... Must not contain 4 or more consecutive or identical characters"（p114）
> "Keep Alive NO. For ALES Mobile, this 'Keep Alive' option is mandatory to be set 'NO' to be compatible with the Push Notification mechanism"（p252）
> "a unique identifier (ALES-DUID) is sent by each ALES in any SIP request (RFC4122)"（p115）

出处：ENTPXTE403EN p106-121, p217-270。

## I — 自述

ALES 是 SIP+ 软终端（Windows/Android/iOS），只受 OXE DM 管理。开通七段：LDAP 认证、SIP 代理、Phone COS、DM profile、建户、装软件登录、维护。

| 主题 | 口径 |
|---|---|
| 认证三模式 | 外部 LDAP（swinst 配 uid/Bind DN）、OXE 本地、OpenID Connect（规划中）；外部与本地互斥，切换先关再开 |
| 密码策略（本地认证） | ≥14 位、至少 2 字母含 1 大写、2 数字、1 特殊字符、禁 4 连续/相同、不与前 5 次重复；密码加密存独立文件不入 MAO 库，双机同步随库备份 |
| 防隔离 | SIP Proxy Framework period=3s、Nb Message=50；不配好软终端会被 DoS 检测误隔离 30 分钟 |
| 移动端双强制 | Phone COS Keep Alive=NO（否则推送不工作）；DM profile 轮询 ≥21600s（低于则 Android 配置通知失效） |
| 一号多机 | 同型互斥（PC vs PC、手机 vs 手机）：403 + Warning 399 Multiple Logins，可 force 抢占，通话中禁抢；跨型（PC 与手机）并存互不影响 |
| 建户 | Set type=SIP extension、Sub type=ALES-desktop/ALES-mobile、Login=LDAP uid、外部认证密码留空 |
| 退出语义 | 关窗/隐藏只是后台化仍收来话；任务栏右键 Quit 才退出（此后不再收来话） |

## A1 — 书中案例

**ALES PC 开通（31030 eevans）**（p217-246，How-To）：

1. LDAPExplorerTool 先探目录，核对 eevans 的 uid/telephoneNumber（实验 192.168.1.252/389 口径）。
2. swinst 配 LDAP 认证：Expert / System management / User authentication / Configure LDAP，录 Realm、Port 389、Search Base DN、Login attribute=uid、Bind DN。
3. Enable LDAP 激活；退出菜单时 nginx 重配重启提示答 y。
4. SIP 代理配 SIP Digest + Framework 3s/50 条 + TCP 长消息。
5. 建 DM profile 1（LDAP 映射、DTMF、拨号规则 33/FR/0/;0/10 实验口径）。
6. 建户 31030：Sub type=ALES-Desktop、Login=eevans、Password 留空、勾 Dial by name。
7. 装 msi 填 CS 地址，登录 eevans/alcatel（实验口径），首连接受证书（可 GPO 预铺 ROOT CA）。
8. 验证：sipregister 见 31030；check_ales_ldap eevans 出 DN；寻线组/监督按键实验照做。

**ALES Android 开通（31035 eedison）**（p247-270，How-To）：

1. 认证与代理同 PC 线；Phone COS 设 Keep Alive=NO（推送强制）。
2. DM profile 加目录映射（givenname/sn/telephonenumber）与轮询 ≥21600s。
3. 建户 31035：Sub type=ALES-mobile、Login=eedison、密码留空。
4. Play Store 安装、连 Wi-Fi、登录后 sipregister 验证；csipsets -d 31035 可看配置文件路径。

## A2 — 未来触发

使用情境：给移动/居家员工配软终端；ALES 登录失败；来话不推送；"同一账号两台电脑打架"；从 LDAP 切回本地认证；软终端莫名 30 分钟连不上。

语言信号：ALES / ALE SoftPhone / softphone / LDAP / uid / swinst / 本地认证 / 密码策略 / Keep Alive / 推送 / 21600 / Framework / 隔离 / 一号多机 / DUID / 403 / Multiple Logins / ALES-desktop / ALES-mobile。

与相邻能力区分：装好后配按键/寻线组/监督找 SIP 业务特性；出门在外经 SBC 注册找远程办公；排查信令找 SIP 跟踪排障。

## E — 可执行步骤

输入契约：LDAP/AD 基础设施、用户清单（login 对应 uid）、终端平台（PC/Android/iOS）、认证模式选择。VDI/RDS 虚拟桌面 → 判停劝退。

1. 探目录：LDAPExplorerTool 核对每个 login 在 LDAP 的 uid 与号码属性。完成标准：login-uid 对照表成文
2. 配认证：swinst 走 LDAP（外部开着切本地必须先关，反之亦然）。完成标准：认证模式激活且 nginx 重配完成
3. 配代理与 COS：SIP Digest、Framework 3s/50 条、TCP 长消息；移动端 Keep Alive=NO。完成标准：参数落库
4. 建 DM profile：LDAP 映射、拨号规则、DTMF；Android 版轮询 ≥21600s。完成标准：profile 先于用户存在
5. 建户：Sub type 按平台、Login=uid、外部认证密码留空、勾 Dial by name。完成标准：sipdict 可见
6. 装软件并登录：msi 或应用商店；首连接受证书；登录验证通话。完成标准：sipregister 见注册
7. 维护核对：check_ales_ldap 验认证链、csipsets 看能力、切本地认证后按策略补密码并让用户首连改密。完成标准：维护命令全部通过

判停点：

- login 未预建就发软件给用户 → 停，ALES 无 auto-discovery，登录必失败（n16）
- 认证开关直接切 → 停，互斥先关再开，且切本地要给全量用户补密码（n18）
- 客户在 VDI/RDS 虚拟桌面推 ALES → 停，明确不支持，改物理机/瘦客户机直装（n20）
- 移动端来话不推送 → 查 Keep Alive=NO 与轮询 ≥21600s 两条强制（n17）

输出契约：注册在网的 ALES 用户清单 + 认证方案与密码基线 + 移动端推送参数记录。

## B — 边界

- 密码策略与全部口令值为书中口径（实验值如 alcatel/Superuser1245* 生产必须替换，n50）
- ALES 不支持酒店、话务员助理、MLA、VDI/RDS 部署（p121）；iPhone 无监督端
- 一号多机只互斥同型设备；403 399 是顶号不是盗号（n19）
- 视频通话在虚拟桌面（Guacamole）测不了，需物理摄像头与桌面（p241）
- OpenID Connect 当时为规划中（p163），不得当作已交付能力引用
