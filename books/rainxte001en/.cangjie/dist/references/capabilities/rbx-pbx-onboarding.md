# OXO 接入 Rainbow（PBXID+激活码）与接入排障

## R — 原文依据

> "You will find here: • PBXID • Activation code"（p85）
> "Domain name Leave the default value: openrainbow.com"（p86）
> "OMC /Tools /Webdiag /Services /Rainbow Status — Control the connection status: « connected with final password »"（p88）
> "The rainbow agent log file name is: ccrbagent.log"（p88）

出处：RAINXTE001EN p83-89。

## I — 自述

PBX-Rainbow 连接是混合闭环的第一关口，三段：

1. **取凭证**（两条路）：
   - 向经销商索取（PBX 由其创建）
   - 自取：客户管理员登录 web.openrainbow.com → 公司管理图标 → My company → Communication → 点该 OXO → 复制 PBXID 与 Activation code
2. **接入**（OMC/Cloud/Rainbow）：
   - 填 Rainbow PBX-ID → 填 Activation code → 勾 Rainbow enabled → Apply
   - Domain name 保持默认 `openrainbow.com` 不改
3. **验证与排障**（三个抓手）：
   - 状态：OMC/Tools/Webdiag（installer 登录）→ Services → Rainbow Status 应显示 `connected with final password`
   - 系统日志：Webdiag → System 页签 → System Files → Log files → 取 `ccrbagent.log`
   - 用户侧日志：Rainbow 界面 → User Settings → About Rainbow → Open logs

## A1 — 书中案例

**接入实验**（p83-89，厂商实验）：

1. 公司/PBX 已由讲师（BP）在云侧建好
2. 客户管理员账号取凭证（实验口径 cCpP.admin@ale-training.com）
3. OMC/Cloud/Rainbow 填入启用，域名保持默认
4. Webdiag 核验状态为 connected with final password
5. 演练取 ccrbagent.log 与用户侧 Open logs 两个排障入口

## A2 — 未来触发

使用情境：PBX 连 Rainbow；连接状态异常；PBXID 在哪找；PBXID 是不是序列号；域名要不要改；接入后怎么查日志。

语言信号：接入 Rainbow / PBXID / PABX-ID / activation code / 激活码 / openrainbow.com / Webdiag / Rainbow Status / connected with final password / ccrbagent.log / rainbow agent。

与相邻能力区分：接入之后的分机关联 → RCC 关联（路由卡）；网关部署前提检查用本卡的状态判据；凭证与 FTR 占位符（FleetRef-Installref）相关场景见网关部署能力。

## E — 可执行步骤

输入契约：客户管理员或经销商提供的凭证来源、可用的 OMC。两者都缺 → 判停找 BP/经销商。

1. 取凭证：经销商索取，或 web.openrainbow.com → My company → Communication → 点 OXO → 复制 PBXID + Activation code。完成标准：两串凭证在手
2. 填入启用：OMC/Cloud/Rainbow → 填双凭证 → 勾 Rainbow enabled → Apply；域名字段不动。完成标准：页面显示连接信息
3. 状态核验：Webdiag（installer 登录）→ Services → Rainbow Status。完成标准：`connected with final password`
4. 异常排查：在 Webdiag 的 System 页签下取 System Files / Log files 里的 ccrbagent.log 分析；若仍显示默认密码态，回查账户密码是否已改（首连改密是前置）

判停点：

- PBXID/激活码不明 → 找经销商或 BP，**PBXID 不是设备序列号**，铭牌上找不到，不要猜（n34）
- FTR 场景看到 `FleetRef-Installref` → 那是出厂占位凭证（设备连的是占位租户），正式接入必须替换为平台生成的真实凭证
- 状态长时间不达 `connected with final password` 且日志无明确报错 → 核对网络出口（443/HTTPS 到 openrainbow.com），网络前提属网络就绪能力（路由卡），不要盲改 PBX 配置

输出契约：Webdiag 状态达标的 PBX-Rainbow 连接 + 排障日志路径记录。

## B — 边界

- 域名固定 openrainbow.com：原书明示不改；私有化/区域域名部署不在原书范围
- "connected with final password" 判据的含义：仍停在临时/默认口令态说明改密流程未完成——改密是首连能力的责任段
- 防火墙/端口/代理等网络前提原书外置到《Rainbow Network Requirements》PDF（p36-40 指针），本卡不覆盖具体端口清单
- OCE-FE 拓扑的双机 PBXID 一致性问题属网关部署能力（p134），本卡只管单机接入
