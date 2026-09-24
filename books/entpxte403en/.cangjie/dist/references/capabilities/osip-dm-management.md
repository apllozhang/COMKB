# SIP 设备管理选型与 profile 体系（OXE DM vs 8770、配置文件、二进制）

## R — 原文依据

> "Since OXE N1, the SIP device management can also be done directly on OXE ('SIP DM on OXE' feature) for local and remote SIP equipment's."（p146）
> "This option is not taken into account for ALES clients, which are only supported on OXE DM"（p148）
> "A SIP DM profile is assigned to each SIP user. The DM profile will adapt to the sub type of device to generate a compatible configuration file of settings ... By default, profile 0 is configured. Possibility to have up to 100 profiles"（p152）
> "There is no backup of configuration files. After database restoration, the manager must generate all configurations files manually"（p166）

出处：ENTPXTE403EN p144-167。

## I — 自述

DM 是终端批量管理的中枢，选型错误代价高：

| 维度 | OXE DM | 8770 DM |
|---|---|---|
| 支持终端 | 仅 8008、ALES、ALE-2/3/30/x00 | 另支持 8088 酒店/Huddle Room 与停产机型（8001/8018/8028s 等） |
| 优势 | 客户级证书更安全、按节点 DM profile、随 CS 冗余更韧、二进制自动更新+配置即时通知 | 集中化：跨节点/跨网、用户与设备模板、即插即用 |
| 开关 | 系统参数 "Device Management in 8770"：勾=8770 管，取消=OXE 管（ALES 不受此参数影响，恒归 OXE） | 同左 |

- DM profile 体系：默认 profile 0、上限 100；ALE-S 与 8008 本地/远程共用一份，ALE-x 系要两份（本地无 SBC、远程配 SBC）；改 profile 即为该 profile 全部设备重生成配置并发 SIP NOTIFY；profile 必须先建后配用户
- 配置文件命名：话机 config.<mac>.xml（/DHS3data/mao/DM/dmictouch）；ALES conf_<login 十六进制>.xml（dmsoftphone 目录，邮箱登录按域分目录）
- 二进制：随 OXE 版本交付存 /DHS3bin/downbin；设备比对版本头后才全量下载；升级按轮询（每天固定时刻或重启时）；ALES 无 binaries 托管
- 运维暗坑：配置文件无备份，数据库恢复后须手工 generate all configuration files；"Activate the Web Server" 系统选项须为 true

## A1 — 书中案例

**DM 激活与 profile 3**（c05 步骤 2/4，p174-180）：

1. WBM System/Other System Param. 取消勾选 "Device Management In 8770"（Warning：关 8770 会删其配置文件，存量话机 reset flash 预案）。
2. SIP device management/DM profile → Create：Profile number=3、LDAP、DNS/SNTP、DTMF、话务特性、admin 密码与 SSH。
3. 用户 31033 挂 profile 3 后入网，/usr3/mao/DM/dmictouch/ 下生成 config.3c28a608010d.xml。

## A2 — 未来触发

使用情境：新装站点选 DM 架构；存量 8770 迁移 OXE DM；规划 profile 数量与远程/本地分治；数据库恢复后终端全部拿不到配置。

语言信号：Device Management / DM / 8770 / OXE DM / DM profile / profile 0 / 100 个 / config.<mac>.xml / dmictouch / dmsoftphone / downbin / 二进制 / 轮询 / 生成全部配置文件 / generate all。

与相邻能力区分：证书与 mTLS 认证找证书管理；话机按 profile 开通找话机开通；远程 profile 双地址参数找远程办公。

## E — 可执行步骤

输入契约：终端家族清单（有无 8088/停产机型）、是否已用 8770、冗余模式、迁移窗口。存量 8088/停产机型在册 → 判停混合拓扑。

1. 选架构：有 8088 酒店/停产机型 → 混合（话机留 8770，ALES 归 OXE）；纯 ALE 家族 → OXE DM。完成标准：架构决策成文
2. 激活与迁移：关 "Device Management in 8770" 前排维护窗口与 reset flash 预案。完成标准：迁移方案过审
3. 规划 profile：按子型与本地/远程分治（ALE-x 两份、ALE-S/8008 一份）；profile 先建后配用户。完成标准：profile 清单就绪
4. 验证下发：话机入网后核 dmictouch/dmsoftphone 目录文件与 nginx access.log；二进制看 downbin 轮询。完成标准：配置与升级链路通

判停点：

- 直接关 8770 DM 而无窗口预案 → 停，全站配置即删（n08）
- 先配用户后建 profile → 停，引用悬空（n49）
- 灾备演练只恢复数据库 → 停，补 generate all configuration files 步骤（n43）

输出契约：DM 架构决策 + profile 规划表 + 配置文件/二进制下发验证记录。

## B — 边界

- 8770 存量迁移细节（模板搬运/批量导）书内只给拓扑原则，操作细节以 8770 文档为准
- 配置文件命名示例（MAC/login 十六进制）为 p156 原文口径；CTL 目录异写见 nr-03
- mTLS 下载认证与证书内容归证书管理卡，本卡只划体系边界
- profile 上限 100、默认 0 为 Ed12 口径
