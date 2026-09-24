# ALE 设备 zero-touch 部署与 DECT 移动（话机/基站/手持机）

## R — 原文依据

> "Designed for Zero-Touch deployment. Centrally configured and managed via Rainbow administration interface. Only one physical SIP device per user account"（p134）
> "If the device receives a specific management URL in option 43, 66 or 67, Rainbow Hub's 'zero touch' mechanism will be broken, as the DHCP option will take precedence."（p136）
> "A Myriad device cannot start up in Cloud mode if a PBX is present on the LAN where the device is connected: TFTP will be given priority."（p137）
> "8328 SIP-DECT Single base station ... 8368 SIP-DECT Multi cell base station"（p148）

出处：RAINXTE101EN p105-113, p133-139, p147-164。

## I — 自述

端侧供给分三等：ALE 原生（Myriad/ALE-2 话机 + DECT，zero-touch、集中管理、官方支持）、入门 ALE-2、第三方 Generic SIP（另一能力卡）。zero-touch 机制链路四段：

1. **注册**：管理员按 MAC 声明设备（建设备时或建成员时；手工或 CSV 批量）
2. **关联**：每台设备必须关联到成员——每用户账号仅一台物理 SIP 设备（DECT 手持机同受此约束）
3. **取配**：设备上电经 DHCP 取 IPv4 参数后连云自动取配置与固件（出厂版本不同，多次重启共约 5-10 分钟）
4. **验收**：屏上已注册用户名前出现绿点即为注册成功

zero-touch 三条技术红线（p136-137）：

1. DHCP option 43/66/67 会以更高优先级覆盖 zero-touch 指向——必须在 DHCP 服务器禁用；禁不掉则下发的管理 URL 必须是 https://rdd.openrainbow.com
2. LAN 内有 PBX 做 TFTP 时会抢先，设备起不了 Cloud 模式
3. 除静态 IP 等极特殊需求外，禁止用设备自带 web 管理页配按键等——正确运行只由 zero-touch 保证；未分配用户的设备取不到配置（初始化报 Config Failed）

设备网络端口表（p136，防火墙放行依据）：

| 协议/端口 | 用途 | 源 | 目的 |
|---|---|---|---|
| TCP 5061 | SIP over TLS | SIP 设备 | *.openrainbow.com |
| TCP 443 | 配置与 API | SIP 设备 | *.openrainbow.com |
| UDP 30000-44999 | SRTP 媒体 | SIP 设备、Rainbow 软话机 | *.openrainbow.com |
| UDP 53 | DNS | SIP 设备 | DNS 服务器 |
| UDP 123 | NTP | SIP 设备 | pool.ntp.org |
| TCP 22 | SSH（若启用，原文 si activé） | SIP 设备 | — |

DECT 两档方案对照（p148-150）：

| 维度 | 8328（单/双站） | 8368（多站） |
|---|---|---|
| 基站数/站点 | 1-2 站 | 最多 254 站 |
| 手持机容量 | 最多 20 台 | 40 台/站，全系统 1000 台 |
| 并发呼叫 | 10 路 | 10 路/站 |
| 尺寸 | 95×93×24 mm | 室内 144×140×35 mm / 室外 365×210×65 mm IP55 |
| 覆盖半径 | 50-300 m，站间无缝切换 | 同左 |

补充口径：

1. 基站按 MAC 声明：8328 选 mono/dual，8368 选 multi 且必须录主站 IP——副站靠它找主站；上线基站可远端重启
2. 手持机按 IPEI 注册且必须选精确型号 8214/8262；只能关联到尚无物理终端的用户
3. 8214 办公型、8262（PTI）恶劣环境/独行工人型；两档都经 CAT-iq 对接本地告警服务器（已验证 F24、Newvoice，Tamat 进行中）

## A1 — 书中案例

**声明话机设备（手工+批量）**（p156-159，How-To）：

1. Communication 页签 → Devices 页签 → 点 Create。
2. 填 Device type、Mac address、Phone type（虚拟课堂无实物可建练习条目）。
3. 批量练习：先删几台已有设备 → 同页签点 Import → 下载模板。
4. 改 CSV：action=create、macAddress、deviceType（例 Myriad M7）。
5. 上传文件 → 设备出现在 Devices 列表，留待关联成员。

**建 DECT 基站并注册 8214 手持机**（p160-164，How-To）：

1. Devices 页签 → DECT base stations → Create primary base。
2. 填 Name（多站命名要有意义）、MAC、Type=8328、Cell mode=Mono。
3. 编辑基站可开 Debug session、故障时可远端重启。
4. Devices 页签选 8214 DECT Handset → 填 IPEI 号与描述。
5. 把手持机分配给 Alice Anderson（其此前无物理终端）。
6. 把手持机挂到步骤 1 建的基站上。
7. 从 8214 手持机安装菜单启动注册 → 手持机显示 Running 即验收通过。

## A2 — 未来触发

使用情境：新话机开箱即用怎么实现；话机报 Config Failed/No Service；功能键不下发；批量导入 50 台话机；门店/车间要移动分机；DECT 选 8328 还是 8368；手持机注册不上。

语言信号：zero-touch / 零接触 / MAC 地址 / IPEI / Myriad / M7 / M5 / M3 / ALE-2 / DECT / 8328 / 8368 / 8214 / 8262 / 基站 / base station / 手持机 / handset / Config Failed / DHCP option / 绿点 / EM200。

与相邻能力区分：第三方话机与日志排障归设备维护与 Generic SIP 能力；设备声明是 BP 专属动作（p49）归公司订阅能力的权责段；端口全集与带宽归网络就绪能力（路由卡）。

## E — 可执行步骤

输入契约：设备清单（型号/MAC/IPEI）、成员名单与站点、网络现状（DHCP option 43/66/67、LAN 内有无旧 PBX TFTP、防火墙端口表）。设备声明为 BP 专属动作。

1. 排雷网络：核对端口表放行；DHCP option 43/66/67 禁用或改指 rdd.openrainbow.com；确认 LAN 内无 TFTP 抢先。完成标准：三项核查记录在案
2. 声明设备：手工逐台或 CSV 批量（action/MAC/deviceType）。完成标准：设备出现在 Devices 列表
3. 关联成员：每设备绑一名尚无物理终端的用户。完成标准：绑定关系在列
4. 上电验收：设备自动取配（约 5-10 分钟、可能多次重启）→ 屏上用户名前绿点。完成标准：绿点验收通过
5. DECT 线：建基站（8368 录主站 IP）/ 按 IPEI 注册手持机（选精确型号）/ 挂基站 → 手持机显示 Running。完成标准：手持机 Running 且可呼入呼出
6. 静态 IP 特例（如需）：菜单 Advanced settings → Network → IPv4 settings；已配过 Hub 的设备先长按 conf 键恢复出厂。完成标准：静态地址生效且改掉出厂密码

判停点：

- 设备报 Config Failed/No Service → 停，先查 MAC 有没有录、有没有关联成员（未分配设备取不到配置与 Hub 固件）
- 现场想直接登话机 web 页改按键 → 停，这是高频坏习惯（n22），配置一律经 Rainbow 管理端下发
- 用户要"一人两台物理话机" → 停，每用户仅一台物理 SIP 设备（p134）；第二台只能换形态（纯软话机）或换人
- 手持机注册按了 Generic SIP 类型 → 停，zero-touch 手持机必须按精确型号 8214/8262（n28）

输出契约：注册成功的终端清单（绿点/Running 验收记录）+ 设备-成员绑定表 + 网络排雷记录。

## B — 边界

- 话机参数外链（aledevice.com）官方自注"不一定适用于 Rainbow Hub 语境"（p107，n17）——采购口径以产品目录与 Features List 为准
- Myriad 参数锚点：M7/M5/M3 彩屏 3.5/2.8/1.6 英寸、超宽频仅免提模式、M7 独有 BT4.1、EM200 扩展最多 10 页×20 LED 键、M 系 PoE class 2（p107，p30）
- DECT 8214 仅欧洲与亚洲供货（p9/p107）；无线勘测（站址/overlap 设计）在书外
- 虚拟课堂无实物设备，实验以练习条目代替（实验口径，needs-review nr-06）
- 出厂密码 123456（web 页 admin/123456）是安全暴露面，现场必须改掉（p138，n23）
