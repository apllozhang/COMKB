# Fleet Dashboard 云端机队服务：Inventory、Offer、远程控制台与软件更新

## R — 原文依据

> "SERVICES GLOSSARY DC Data Collector DOD Data On-Demand FTR First Time Registration POD Push On-Demand RTR Right To Run SU Software Update"（p340）
> "Only one console can be opened at the same time • Console is disconnected after 1 minute of inactivity ... Each connection is logged by the Call Server (shell.log)"（p343）
> "Provide to the OXE a temporary URL for the AWS repository • Request the concerned OXE to download the version (HTTPS) ... Transfer only: switch on the new version remains under BP's responsibility"（p347）

出处：ENTPXTE402EN p310、p338-348。

## I — 自述

Fleet Dashboard 是 CCI 上的机队管理应用：FTR 注册后即可用（FTR 与许可控制必需，新装机默认启用），OV8770 或 OXE WBM 控制。五个可开关服务：

| 服务 | 用途 | 硬约束 |
|---|---|---|
| Inventory | 资产盘点：许可/订阅/终端/中继/板卡 | 终端含硬件参考/软件版本/MAC/IP 域；中继含 TLS 加密状态 |
| Get offer files | 从运行中的 OXE 取实时 OPS 文件供 Actis 报价 | 默认启用、可关 |
| Push offer | 从 eBuy 拉许可+offers server 拉 Actis offer 推到 OXE | 经 POD/XMPP IBB；切换新文件归 BP |
| Remote management | 远程控制台（等价 SSH） | 单会话、1 分钟无操作断开、OXE 凭证再认证、记 shell.log（可经 OmniVista 8770 审计） |
| Software update | 给 AWS 仓库临时 URL，OXE HTTPS 下载官方 ISO | 有效 SPS 合同+technical advanced 特权；信任主机须含 cdn-oxe-sw-update.al-enterprise.com |

行为细节：

- 远程控制台不能从 Dashboard 主页分离，支持复制粘贴
- 软件更新只管传输——切换新版本仍是 BP 责任（可用远程控制台安装）
- 告警展示由 DC 每日取回；低于推荐版本（ALE Technical Support 每版指定）的条目橙色高亮、每日计算

动作状态字段三段读法：第一段 D（需下载）/-；第二段 I（手动安装）/A（自动）/S（手动切分区）/-；第三段 P（下载中）/O（完成）/K（失败）/F（OXE 侧禁用软件更新）/-。

## A1 — 书中案例

**服务状态与推荐版本判读**（p338-348，讲义）：

1. RTR 状态列按剩余资格期分四级显示（判读细则在 RTR 卡）
2. Inventory 拉取终端与中继资产清单
3. Get offer 取 OPS 文件，供 Actis 报价比对
4. Push offer 推许可，动作列读 D 与 I/A/S 状态
5. 软件更新下发后盯 P/O/K/F：F 表示 OXE 侧禁用，先查开关
6. 每次远程控制台登录在 shell.log 留痕，8770 审计可查

## A2 — 未来触发

使用情境：想在云端盘点客户资产；远程进客户 OXE 排障；云端下发新版本；许可推送到设备；控制台总掉线。

语言信号：Fleet Dashboard / Inventory / offer / Push offer / Get offer / remote console / 远程控制台 / shell.log / Software update / cdn-oxe-sw-update / SPS 合同 / technical advanced / DOD / POD / DC。

与相邻能力区分：

- RTR 状态与资格期数值 → RTR 卡
- FTR 注册与连通性 → 云连接卡
- OXE 本体加载与切换 → 加载类卡（云端更新只管传输）

## E — 可执行步骤

输入契约：FTR 已注册、Fleet Dashboard 账号（OV8770 或 OXE WBM 控制开关）、远程操作需 OXE 凭证、软件更新需 SPS 合同与 technical advanced 特权。无 SPS 合同 → 判停先补商务前提，别硬试更新。

1. 开关核对：OV8770/WBM 确认各服务启用状态与 KeepAlive。完成标准：服务清单确认
2. 资产盘点：Inventory 拉许可/终端/中继清单。完成标准：资产表导出
3. Offer 推取：Get offer 取 OPS；Push offer 推许可并读动作状态列。完成标准：状态 P 到 O 收敛
4. 远程排障：单会话控制台，OXE 凭证再认证，1 分钟内保持操作。完成标准：操作完成且退出
5. 软件更新：确认 SPS 与特权，核对信任主机含 cdn 域名后下发。完成标准：下载完成、切换计划移交 BP

判停点：

- 想开着控制台跑长脚本 → 停，1 分钟无操作即断，长任务改本地或分段
- 更新状态卡 F → 停，F=OXE 侧禁用软件更新，先查 OXE 开关
- 客户以为云端更新会自动切换版本 → 停，传输归云端、切换归 BP，提前对齐预期
- 信任主机站点下载失败 → 停，核对 cdn-oxe-sw-update.al-enterprise.com 是否在白名单

输出契约：机队资产清单 + 推送/更新动作记录（状态字段留档）+ BP 侧切换责任交接说明。

## B — 边界

- 远程管理与软件更新均要求有效 SPS 合同与 technical advanced 特权（无专属角色）；远程管理需 OXE 电话应用已启动
- VAD 可把子机队委托给 IR（p305，书中仅此一处，无操作细节）
- 推荐版本由 ALE Technical Support 指定；升不升级由 BP 决策
- 审计数据（shell.log：Dashboard 账号名+公司名）经 OmniVista 8770 查询
