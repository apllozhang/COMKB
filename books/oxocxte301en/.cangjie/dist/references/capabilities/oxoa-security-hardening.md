# 系统安全加固（密码体系、自动检查、网络面收敛、锁定公式、加固清单）

## R — 原文依据

> "It is mandatory for Installer to change all the default passwords in order to proceed further"（p315）
> "Enabled by default, with default periodicity of 4 weeks … every xx weeks (allowed values 01 to 52 weeks, 00 function is disabled) • Systematically after warm reset"（p316）
> "Password rules have been implemented and requires now a minimum of one uppercase letter, one lowercase letter, and one numeric character (fixed length of 8 characters)"（p319）
> "The lockout time is doubled for each denial (24 hours max value, 1440 minutes)"（p384）
> "Limit the use of the ETH1 port exclusively to the SIP gateway by explicitly prohibiting any connection to the OCE management services … Default value = enabled"（p312）
> "Not used ports (21, 1721, 5061, 8729, 8888, 17069, 23400) are definitively closed"（p337）

出处：OXOCXTE301EN p311-338。

## I — 自述

安全生产基线五支柱（全部免 license，总纲指向 TC1143）：

| 支柱 | 内容 | 入口/参数 |
|---|---|---|
| 密码树 | 管理密码（一窗全显、固定 8 位含大小写数字）、SIP 话机管理密码（Expert 级读/重置/设）、订阅户密码（弱密码检出+批量重置）、Remote Access Code | OMC/Security/Passwords |
| 自动密码检查 | 默认启用、周期 4 周（01-52 可配，00 禁用）；激活立即查一次 + warm reset 后必查；弱密码生成 urgent alarm 可邮件通知 | noteworthy AutoPwdChk；审计工具 TC2249 |
| 网络面收敛 | Network IP Services 三开关（WAN 管理服务/WAN 用户应用/LAN 用户应用）；ETH1 限制（disabled 时仅 SIP trunk 保留，OMC/WebDiag/OSC 全封） | OMC/Security/Network IP Services |
| 远程接入锁定 | 认证连续失败锁时翻倍：10→20→40 分钟，封顶 1440 分钟（24 小时）；本地与远程共享失败计数；LAN 本地访问不受锁 | noteworthy VMUMaxTry |
| 加固清单 | OpenSSL v3、SIP DoS 测试、ARP 欺骗检测、移除 WSDL、内核补丁、未用端口永久关闭、紧急号码表（上限 100 条）、LDAPS/StartTLS | OMC/Emergency；LDAP 证书校验 Mandatory 默认 |

两级开关"与"关系：系统级 WAN 用户应用禁用时，每用户 WAN API Access 开了也无效（p334）。Console 口重置 installer 密码的开关默认启用，也允许禁用；禁用后遗失密码的唯一出路是现场 LoLa，ALE 不提供远程重置（p325）。

## A1 — 书中案例

**安全章为讲义形态（无实验），关键行为口径**（p311-338）：

1. 首登强制改全部默认密码才能继续操作（p315）。
2. 自动检查发现默认/弱密码即生成 urgent alarm 历史事件（p316-321）。
3. 邮件通知经 Central Services 配置；SMTP 带 TLS 的认证暂不支持（p331）。
4. ETH1 限制置 disabled 后 SIP trunk 独占该口（p312 矩阵）。
5. 锁定测试：连续错密码后语音邮箱锁 10 分钟，History Table 可见（p402，VM 章实测）。

## A2 — 未来触发

使用情境：上线前安全基线；默认密码要不要改、怎么审；弱密码扫描；远程访问被锁怎么办；ETH1 要不要专口专用；该关哪些端口；紧急号码表怎么配；LDAP 目录连接要不要加密。

语言信号：安全 / security / 密码 / password / 默认密码 / 弱密码 / AutoPwdChk / 自动检查 / 锁定 / lockout / VMUMaxTry / ETH1 / Network IP Services / 加固 / hardening / TC1143 / 紧急号码 / LDAPS / StartTLS / 端口关闭。

与相邻能力区分：证书与传输加密（DTLS/TLS-SRTP）归证书套件能力；远程维护接入的端口转发归 Cloud Connect 与远程维护能力；语音邮箱锁定/解锁操作归语音邮箱与移动能力。

## E — 可执行步骤

输入契约：客户安全策略（密码周期/复杂度）、网络分区规划（管理面/话务面）、LDAP 服务器信息、所在国紧急号码表。安全策略未定 → 判停按 TC1143 默认基线执行并留档。

1. 改密：首登改全部默认密码（管理 8 位含大小写数字；每客户唯一）。完成标准：无默认密码残留
2. 自动检查：确认 AutoPwdChk 启用与周期（默认 4 周）；按需配邮件通知。完成标准：审计可跑
3. 网络面：Network IP Services 三开关按分区收敛；OCE 站点评估 ETH1 限制（SIP 专用则 disabled）。完成标准：管理面与话务面分离
4. 锁定策略：核对 VMUMaxTry 与翻倍封顶口径；远程接入码按需启用。完成标准：暴力破解有界
5. 加固清单：核未用端口关闭（21/1721/5061/8729/8888/17069/23400，启用 SIP-TLS 前先核对版本行为，nr-07）。完成标准：清单过一遍
6. 紧急号码：按所在国配 Emergency Numbers（上限 100 条）。完成标准：紧急呼叫可达
7. LDAP：LDAPS 636 或 StartTLS 389（推荐默认），证书校验 Mandatory；证书经 WebDiag Trust Store 导入。完成标准：Test 通过
8. 验证：跑 TC2249 审计工具；试错密码确认锁定与告警。完成标准：基线可复验

判停点：

- Console 口重置开关已被前供应商禁用且密码遗失 → 只能现场 LoLa（n48），报价前先查该开关状态
- 邮件服务器强制 STARTTLS 认证 → 告警邮件发不出（n46，推断：改用内网中继或开放 25 的服务器）
- 远程应用连不上 → 两级开关都要开（系统级 + 每用户 WAN API Access，n47）
- 客户要求绕过密码策略或关闭自动检查 → 停，书面留风险，不执行

输出契约：安全基线核查表（五支柱逐项）+ 密码审计报告 + 网络面开关矩阵 + 遗留风险清单。

## B — 边界

- 本卡是"机制与开关"清单，不提供威胁模型：什么场景开 ETH1 限制、何时关远程维护，需工程师按客户环境判断（BOOK_OVERVIEW 批判）
- 5061 同时出现在关闭清单与 SIP-TLS 端口，两者关系原书未展开（nr-07，推断性保留）
- 管理密码固定 8 位是 OXO 管理面口径，与 Rainbow 侧 ≥12 位策略不同体系，勿混用
- 安全生产的完整策略（密码审计流程、审计周期）以 TC1143 + TC2249 为准；书内只给机制
- 实验接入码 780911/615243 等全部为实验口径，生产禁用
