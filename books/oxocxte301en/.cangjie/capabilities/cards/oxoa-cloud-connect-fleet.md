# Cloud Connect 舰队与远程维护（注册、Fleet Dashboard、软件更新、50443 远程接入）

## R — 原文依据

> "Both connections are initiated by the OXO Connect … No need to change the firewall rules … A VPN connection can be requested by a technician"（p264）
> "Registration of OXO Connect will take place automatically. By default, the Cloud Connect right is enabled. The service does not require licenses."（p287）
> "A delay of 24h is required to see the systems"（p289）
> "[D..] if Download indicator is RED: the Current SW version running in the call server is Older that the 'Recommended Version'. → Update is recommended"（p271）
> "User Privilege 'advanced' is needed for SW update action"（p272）
> "For remote access from Internet forwarded to the OXO Connect, the destination port on the OXO Connect must always be port 50443"（p303）

出处：OXOCXTE301EN p262-310。

## I — 自述

Cloud Connect（CCI）把舰队管理搬上云：OXO 主动发起永久 HTTPS（心跳/上报）+ 按需 VPN（技师请求后到远程服务中心），全程免改防火墙规则。注册自动、免 license、默认启用；Fleet 数据库一天刷新一次——注册后 24 小时才可见（n52）。

**门户三件套**（同一 Business Store 账号；域名书内两种写法见 nr-05，以登录页为准）：

| 门户 | 定位 | 核心功能 |
|---|---|---|
| Fleet Dashboard | 舰队级（OXE 与 OXO 通用） | 安装基础/SA 合同/Inventory（每日刷新，GDPR 匿名）/批量 SW 更新 |
| OXO Connectivity | 单系统（可 standalone） | VPN 配置、Watchdog/OMC 复位、硬件许可清单、DSP 统计、默认密码检出、会话日志、单台更新 |
| Business Store | 商务入口 | 合同与账号 |

**软件更新三步**：Connect（多台 Fleet/单台 Connectivity）→ Check（指示灯 [D..] 下载建议/[.S.] 切换建议/[..P] 进行中；D 或 S 红=建议动作）→ Update（下载后按 swap 时间自动切换）。单台与批量均需用户权限 "advanced"（n53）；服务免 license。

**远程维护四路径**（与云管理互补）：

| 路径 | 通道 | 关键口径 |
|---|---|---|
| 电话网 DDI | 保留公网 DDI 走 modem PPP | SIP-only 站点不可用（n51） |
| 本地 V24 | TC002_US 口径 | 现场串行 |
| 互联网 HTTPS | IAD 端口转发"公网任意端口→50443" | 目标端口永远 50443（专用访问控制）；公网 443 被占可换端口 |
| 管理 VPN | 专用管理 IP，仅 OMC 可配 | 激活/停用须 warm reset；每站点可用同一 IP |

**Rainbow 业务目录自助同步**（p307-310）：EC 管理员在 Rainbow 点 sync，公司下全部已连 OXO 集体目录先擦空再写入；姓名截断 16 字符、非 Unicode 忽略、短号首次随机分配后维持；Dial by Name 与主叫识别立即可用。

## A1 — 书中案例

**Cloud Connect 注册实验**（p286-289，厂商实验）：

1. 前提：系统接入客户网络并获得互联网访问（基线 IP 实验口径）。
2. 核对 OMC/Hardware and limits/LAN/IP Configuration。
3. 核验 OMC/Cloud/Cloud Connect 状态串为 "Connected with final credentials"。
4. Fleet 演示由讲师次日展示（数据库一天一刷新，需等 24 小时）。

**软件更新**（p269-273，讲义+演示）：

1. 多台走 Fleet Dashboard：筛选产品→Software→SW Minor Update（太旧版本标红）。
2. 单台走 OXO Connectivity：Switch/Download 状态（Recommended/OK/Has been requested）+动作按钮。
3. 指示灯 [D..]/[.S.]/[..P] 判读；advanced 权限执行。

**远程维护互联网接入**（p300-305，讲义）：

1. 固定公网 IP：IAD 转发公网 443 到 OXO 50443。
2. 公网 443 被占：转发公网任意端口到 50443。
3. OMC 直连填公网名/IP；经代理时 Options 配 proxy（默认密码 OMCAdmin，实验口径）。

## A2 — 未来触发

使用情境：系统上云注册与验收；舰队版本治理与批量升级；远程 VPN 调试；客户防火墙要不要开洞；远程维护走什么通道；Fleet 里看不到新注册系统；给客户推 Dial by Name 名录。

语言信号：Cloud Connect / Fleet Dashboard / OXO Connectivity / Inventory / 软件更新 / advanced 权限 / 远程维护 / 50443 / 端口转发 / 管理 VPN / Rainbow 目录。

与相邻能力区分：远程接入的访问控制开关与加固归安全加固能力；管理 VPN 的 warm reset 操作归维护工具能力；Rainbow 侧公司/成员管理属 starter bundle（Rainbow OXO Connect 入门）范畴，本卡只管目录同步到 OXO 这一段。

## E — 可执行步骤

输入契约：Business Store 账号与 SA 合同、门户账号权限（advanced）、站点互联网可达性、远程维护需求（通道/端口规划）。账号或权限缺失 → 判停先理顺商务与权限，不要现场绕过。

1. 注册核验：确认默认启用与互联网可达；OMC/Cloud 状态串 "Connected with final credentials"。完成标准：注册闭环
2. 舰队验收：等 24 小时数据库刷新后在 Fleet Dashboard 找到系统（当场看不到不算失败，n52）。完成标准：舰队可见
3. 版本治理：按指示灯判读（D/S 红即建议动作）；批量走 Fleet、单台走 Connectivity，advanced 权限执行。完成标准：更新策略成文
4. 远程通道选型：有 DDI 可走电话网；SIP-only 只能 IP；互联网路径端口转发一律指向 50443。完成标准：通道可用且安全口径留档
5. （更安全）管理 VPN：OMC 配专用管理 IP，warm reset 生效；配套收敛 Network IP Services。完成标准：管理面隔离
6. （Rainbow 目录）EC 管理员建共享联系人后点 sync；先导出备份 OXO 集体目录。完成标准：Dial by Name 可用
7. 验证：远程会话建立、更新后版本核对、同步后短号与识别抽查。完成标准：三场景闭环

判停点：

- Fleet 当天看不到系统 → 等 24 小时再判，不要重复注册
- 公网侧直接转发到 443 或其它内部端口 → 禁止：绕过 50443 专用访问控制（n50）
- SIP-only 站点承诺 modem 远程 → 停：物理上不可行（n51），投标前改口径
- 集体目录有手工维护数据 → 同步前必须导出备份（先擦空再写入，n49）；Max entries 原书留白（nr-08）

输出契约：注册与验收记录 + 舰队更新台账（版本/时间/执行人）+ 远程维护通道配置表 + 目录同步备份与结果。

## B — 边界

- 门户域名书内两种写法（nr-05）：文档不固化域名，以登录页实际跳转为准
- Inventory 数据每日刷新且 GDPR 匿名：实时性有限，不能当监控系统用
- 软件更新的版本兼容与应用/板卡矩阵查 OXO Connect Cross compatibility（MyPortal），书内不展开
- OMC 代理默认密码 OMCAdmin 为出厂值（实验口径）：生产必须改并纳入密码树管理
- Rainbow 目录同步要求 OXO 编号计划保留集体快速拨号段；未连 Rainbow 的 OXO 不同步，多站点短号可能不一致（n49）
