# 交换机登录接入与 AAA 管理面加固（认证链、账号治理、五通道、收缩清单）

## R — 原文依据

> "Authenticated Switch Access (ASA) provides the ability to restrict which users can configure the switch remotely. ... ASA applies to Telnet, FTP, SNMP, SSH, HTTP, and the console and modem ports."（p95）
> "By default : 2 users 'admin and default' ... Up to 64 users can be configured in the local switch database"（p70）
> "From 8.10R03 a warning message will be displayed ... From 8.10R04 it is mandatory to change the password at first login"（p71）
> "In case you disable console access, and you lose all other means of management access ... (RMA necessary in this case)"（p77）

出处：DT00XTE215EN p65-101。

## I — 自述

一切配置的入口是 AAA：按服务类型逐条声明认证链，再叠加管理面收缩。四层结构：

1. **认证链**：default/console/telnet/ftp/http/snmp/ssh 七条链各自独立，命令 aaa authentication <service> server1 [server2...] [local]；可挂多服务器 fail-through，exit-on-fail enabled=只用第一个可用服务器，disabled=逐个查完（p69）
2. **账号治理**：本地库存于 flash/system 的 userTable，出厂 admin/default 两用户、上限 64；密码策略四层——复杂度（禁含用户名/禁连续字符/大小写数字非字母最少个数）、生命周期（min/expiration/history/min-age）、强制刷新 password-refresh、创建时 sha+des 加密（p70-74）
3. **五通道参数**：console（速率分代、可限 admin-only 或禁用）、EMP（旁路 NI 直连 CMM，无口机型 8.9.R1 起 USB-Ethernet dongle 等效）、WebView（R8 强制 SSL）、SSH/Telnet/FTP、SNMP
4. **收缩清单**：ASA 限源（上限 64 地址）、ip service 禁不安全端口、会话参数（login-attempt/login-timeout/session-limit）、SSH 强加密（strong-ciphers/strong-hmacs/enforce-pubkey-auth）、session banner

**管理会话并发上限**（p80）：

| 协议 | 上限 |
|---|---|
| Telnet（V4/V6） | 6 |
| FTP（V4/V6） | 4 |
| SSH + SFTP | 8 |
| HTTP | 4 |
| 五类总会话（含 console） | 20 |
| SNMP | 50 |

**版本线**（p70-71）：8.10R03 登录警告 → 8.10R4 强制改默认密码 → 8.10R04 强制首登改密。

## A1 — 书中案例

**远程接入实验**（p91-101，How-To）：

1. 前置核查：实验交换机已预配到管理网的静态路由（实验口径，非空配置）
2. 按地址表核对 7 台交换机 EMP 地址（10.4.Pod#.{1,2,3,5,6,7,8}），从 POD 桌面逐台 ping
3. show aaa authentication 确认各服务 1st authentication server = local；SSH 为 denied 则 aaa authentication ssh local
4. SSH 测试：ssh admin@10.4.<pod>.3 输入交换机密码登录
5. CLI 改会话参数：session cli timeout 60，write memory 后 show session config 验证
6. WebView 登录 https://10.4.Pod#.3（R8 强制 SSL），Security > ASA > Session > Configuration 改参数
7. WebView 写内存：顶部图标栏第三个图标，Yes 保存
8. WebView 建 VLAN 59（Layer 2 > VLAN > "+"），CLI show vlan 验证；再经 VLAN Mgmt 删除并 write memory

## A2 — 未来触发

使用情境：新交换机开通管理接入；升级后 admin 默认密码问题；限制管理来源网段；关 Telnet/HTTP 等不安全服务；SSH 加固；WebView 登不上；账号密码策略合规。

语言信号：AAA / ASA / 登录认证 / SSH 加固 / 管理面 / console / EMP / WebView / SNMP / 密码策略 / password-policy / admin/switch / 限源 / session timeout / 64 用户。

与相邻能力区分：

- 开局向导一体化的初始化：Lightning Config 能力
- 改完配置怎么保存：配置生命周期能力
- userTable 备份细节：配置生命周期能力（备份线）

## E — 可执行步骤

输入契约：交换机版本（决定强制改密行为）、运维网段、认证基础设施（本地库或 RADIUS/LDAP）、合规要求。全部通道未确认前不收紧。

1. 基线核查：show aaa authentication 看七条认证链；确认 admin 密码已改（8.10R04 起强制）。完成标准：各服务认证链明确
2. 声明认证链：外部服务器先 aaa radius-server 声明（建议 TLS），再逐服务 aaa authentication 挂链，保留 local 兜底与 exit-on-fail 取舍。完成标准：show 显示新链
3. 账号治理：按密码策略四层设定复杂度/生命周期/刷新；权限按命令域最小化授予。完成标准：策略命令生效且新用户可登录
4. 管理面收缩：先 aaa switch-access management stations 限源（≤64 地址，含运维网段），再 ip service 禁不安全端口，然后会话参数、SSH 强加密与 session banner。完成标准：仅保留授权通道
5. 验证后固化：从另一条独立通道重登验证未被锁死，write memory 保存。完成标准：新旧双通道均可用

判停点：

- 计划禁用 console → 停，先确认至少两条独立远程通道可用，否则全部丢失即 RMA
- WebView 登录失败 → 先 show aaa authentication 查 Http 服务类型（默认服务开但认证未授权），再怀疑账号
- http:// 访问被重定向 → R8 强制 SSL 属预期，改用 https 并接受自签名证书
- 需要多因子认证细节 → 超出本书，指向 MFA Application Note（书外）

输出契约：可用的管理接入清单（通道/认证链/账号策略）+ 已生效的收缩配置 + 保存确认。

## B — 边界

- 出厂默认 admin/switch、本地库 64 用户上限；升级存量设备后必须逐一核查默认口令是否已换（升级不等于改密）
- console 速率按型号查分代表（多数 9600；6900 部分 V72/C32 系、6860N/6870 为 115200），勿沿用单一默认值（nr-04）
- EMP 相关命令适用于 dongle 等效口；VC 场景所有成员都要插 dongle 才有完整 VC EMP
- 实验环境双凭据（admin/Superuser=1 与 admin-netadv/Superuser01!）为 R-Lab 特有，见 book/overview 环境区
- RADIUS/LDAP 服务器侧的部署（用户库、证书）在书外；本书只给交换机侧声明与默认参数（retries 3/timeout 2 秒/1812/1813）
