# OXE 时间同步（NTP/chrony 部署与巡检）

## R — 原文依据

> "Since OXE R101, the 'chrony' tool is implemented in the OXE O.S. … 'chrony' is a versatile implementation of the Network Time Protocol (NTP)"（p167）
> "Instant synchronization is possible only when 'NTP' process ('chronyd') is stopped … This is a 'one shot' method"（p172）
> "The NTP protocol uses the port 123 (UDP/TCP) … The NTP packets have a size of 90 bytes on the Ethernet level (76 bytes on the IP level)"（p170）

出处：ENTPXTE400EN p164-183。

## I — 自述

系统时间影响计费、留言时间戳与排障日志，时间同步分"粗调"与"细调"两层：

1. **对时六途径**：date 命令 / swinst / MAO / 话务台 / T0T2 线上取时 / NTP——前几种为直接跳变的粗调，话机自动跟随；多站点可按 IP 域配时区
2. **chrony（R101 起）**：承担渐进同步——client/server 模式（不支持 broadcast），UDP 123，OXE 可同时作客户端与服务器，支持对称密钥认证；stratum 分层（0=参考钟、1=主服务器、n+1=次级）
3. **两阶段同步法**：首次装机或时差大时先停 chronyd 做"瞬时同步"（一次性拨钟），再 Start NTP 进入渐进维持
4. **服务器选项**：burst/iburst（可达/不可达时 8 连发）/prefer（优先）
5. **维护命令**：chronyc sources/clients/ntpdata、systemctl status|start|stop|restart chronyd、lsof -i:123、more /etc/chrony.conf

| 维护动作 | 命令/入口 | 判据 |
|---|---|---|
| 查同步源 | chronyc sources | ^* 标记=已选中源 |
| 查服务状态 | systemctl status chronyd | active (running) |
| 查端口占用 | lsof -i:123（root） | chronyd 进程在听 |
| 瞬时同步 | swinst NTP 菜单 4 | 须先 Stop NTP |
| 渐进同步 | swinst NTP 菜单 1 Start NTP | NTP is running |

## A1 — 书中案例

**NTP/chrony 实验**（p175-183，How-To）：

1. swinst 系统管理设时区，按 Warning 重启系统生效
2. NTP 管理菜单加服务器 192.168.1.252（实验口径），key 0、无 burst/iburst/prefer
3. 人为把系统日期改偏 1 个月制造时差
4. 确认 NTP is stopped 后执行 Instant synchronisation，时钟立即回正
5. Start NTP 启动 chronyd 进入渐进同步
6. 巡检：chronyc sources 显示 ^* ntp1，systemctl 显示 active (running)
7. 验证系统时间与 NTP 服务器一致，实验收尾

## A2 — 未来触发

使用情境：新装机对时；时区配错；话机/话务台时间不对；计费或留言时间戳异常；NTP 服务器换地址；chronyd 起不来排查。

语言信号：时间 / NTP / chrony / chronyd / 对时 / 时区 / timezone / 瞬时同步 / instant / 渐进 / UDP 123 / stratum / iburst。

与相邻能力区分：时间不对导致的话机显示问题先查本卡，再查话机自身 → 用户终端开通能力（路由卡）；系统时间相关的日志分析 → 备份维护能力（路由卡）。

## E — 可执行步骤

输入契约：上级 NTP 服务器地址（客户内网或运营商提供）、时区与夏令时要求。没有 NTP 源时先与客户网络组确认，临时用粗调要在交付记录注明。

1. 配时区：swinst 系统管理 → Date & Time → Set timezone，确认后重启系统。完成标准：date 输出时区正确
2. 加 NTP 服务器：NTP 管理菜单 5 Modify configuration → 2 Add/Modify server，按需带 iburst/prefer。完成标准：View 里服务器在列
3. 校大偏差（首装/漂移大时）：确认 NTP is stopped，执行 Instant synchronisation 拨正。完成标准：时钟与源一致
4. 启动渐进同步：Start NTP（chronyd）。完成标准：NTP is running
5. 巡检闭环：chronyc sources 见 ^* 选中源；systemctl 状态 active；端口 123 在听。完成标准：三项判据全过
6. 留档：NTP 源、时区、认证方式写入交付记录。完成标准：时间域台账完整

判停点：

- 瞬时同步选项点不动 → chronyd 在运行，先 Stop NTP 再做（n12），做完记得重新启动
- 改了时区"没生效" → 时区改动必须重启系统（p176 Warning），排入维护窗口
- chronyc sources 无 ^* 选中源 → 查网络可达性与防火墙（UDP 123 需在 OXE 与上级源两侧放行）
- RADIUS/认证类时钟强校验场景 → 渐进同步需数分钟属正常（p172），不要反复重启 chronyd

输出契约：时钟受控的系统（时区+同步源+巡检判据）+ 时间域配置台账。

## B — 边界

- 上级 NTP 源为书外前提；实验源 192.168.1.252 为实验口径（IT Server）
- 渐进同步仅 client/server 模式，broadcast 不支持；对称密钥认证在 chrony.conf keyfile 层面，书中只点名
- 时钟漂移根因分析（VM 工具同步冲突等）属虚拟化平台议题，不在本书范围
- 多站点按时区/夏令时的集中策略在组网课程（Advanced）展开
