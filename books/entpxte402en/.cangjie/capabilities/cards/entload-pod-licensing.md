# OPEX / Purple on Demand：订阅许可、LMS 同步、panic 时间线与 C2P 转换

## R — 原文依据

> "In OPEX subscription mode, licenses of elements in OXE system ... are managed through a License Manager Server in the cloud • This new feature is also called "Purple on Demand" (PoD)"（p351）
> "A new lock, 431: 1 means new OPEX mode (0 for CAPEX mode) • Previous CAPEX locks are no more taken in account • Except lock Beta tests 87 and lock Release 165"（p354）
> "Warning CORRECT "SWK" FILE IS MANDATORY, WITH: CCSID (CLOUD CONNECT SUITE ID) LOCK 431: OPEX MODE SET TO "1""（p388）
> "OXE checks every 4 hours that licenses are synchronized ... If can't update the LMS licenses because the max of licenses is reached, the OXE switches in panic mode ... The incident 652 is sent"（p371）
> "To be able to download and implement the POD license files, the Project status must be seen Active"（p384）

出处：ENTPXTE402EN p350-408。

## I — 自述

OPEX/PoD 把许可从"装在机器上的文件"变成"云上池子的消耗额度"：硬件仍 CAPEX，用户/话务员/话务台/录音等订阅由云端 LMS 按项目池管理；OXE 侧只剩 lmsagent（无状态 HTTPS 桥，跑主/备/PCS 全部 CS、备机只读）与 spadmin 视图。

三种订阅消耗类型：

| 消耗类型 | 触发点 | 适用订阅 |
|---|---|---|
| Unitary | 实例创建即耗；LMS 无余量拒建 | Softphone、API Telephony、VNA、VNA Broadcast |
| On activation | 激活（OPEX activation=Yes）才耗；停用释放且保留配置 | 仅 Voice Enterprise 与 Room |
| By threshold | 加阈值才向 LMS 要许可（WBM Opex Licences 菜单维护） | Attendant Console（4059 上限 0-1000）、Voice Agent（ACD 0-2800）、API Recording Cnx（DR-Link 0-15000）、VAA（端口侧声明）、OPR 三档 |

许可映射规则（建用户前先对）：

- tandem/multi-device 无软话机=1 份 Voice Enterprise；带软话机（SIP/IP）=Voice Enterprise+ALE Softphone 双份
- DSU/DSS 办公共享=两份 Voice Enterprise（双方 flag 都开）；客房=1 份 Room（按客人管理时房间与客人双开、各占一份）
- 4059 关联设备占 1 份 Voice Enterprise；副机挂为 tandem 时 flag 强制归 0 并释放许可
- ACD 站的 flag 不可启用、登录时耗 Voice Agent(CCD)

同步与 panic 数值律：

- 每 4 小时对账：LMS 满员更新失败即 panic+事件 652；LMS 不可达发 654，连续 30 天不可达 panic+652；panic 后同步恢复自动解除
- 启动期无条件按本地旧消耗值起业务，但一切要向 LMS 要许可的管理动作（建用户、开 activation）被拒
- 超订时间线：15 天后随机停用空闲用户/话务员的 activation、下调话务台上限、拒 CC 新登录与 DR-Link 新录音（Softphone 超订始终不自动处置）；45 天后全部停用、话务台清零
- LMS 失联超 30 天则 15 天后即执行最狠档

目录与转换口径：

- 24 个商用订阅（对照约 500 个 CAPEX 软件项；OV8770 由约 60 项并为 1），UMC 免费无订阅，No PRS，不含 ISDN/模拟中继
- C2P 转换五步：准备、校验、导出 JSON 到 MyPortal、调量、购物车（下单即定局）；C2P 件号 3EYxxxxxMA（PoD 为 3EYxxxxxAA）
- C2P 排除 OPR、ALE Connect、Selfcare、VNA、API Management；OT-SBC 例外只需 C2P 维护订阅

## A1 — 书中案例

**PoD 许可下载与 LMS 同步核查**（p381-408，How-To）：

1. MyPortal 顶栏 Installed Base 进 Asset & service manager
2. Explore Purple Assets 点 Search，左侧选客户项目
3. 项目状态必须 Active，按产品点 CPU ID 图标下载 .swk
4. 装 swk（须含 CCSID 与 LOCK 431=1）并重启 OXE
5. spadmin 1 核 OPEX Flag=1、PANIC Flag=0；2 核 431 Opex Mode=1
6. 前提收口：FTR Registered、RTR Enabled=Yes、swinst 配好 NTP
7. spadmin 11 读四列计数（lms/oxe 两列必须一致，否则 panic）
8. 10 Force LMS synchronization 至 "Synchonization done…"
9. 实测：建话机开 activation 复核计数 +1；设 DR-Link 阈值 5 复核 "0 | 5/5 | 25"

## A2 — 未来触发

使用情境：客户要从 CAPEX 转 OPEX；装了许可系统还是 CAPEX 行为；LMS 断了能不能开户；话机报 No license available / 402 Payment required；订阅买多少怎么算；C2P 流程怎么走。

语言信号：OPEX / PoD / Purple on Demand / LMS / lmsagent / lock 431 / OPEX activation / spadmin / Voice Enterprise / Room / 4059 / panic mode / C2P / 3EY / MyPortal / Active。

与相邻能力区分：

- FTR/RTR 链路问题 → 云连接卡与 RTR 卡
- 云端 Dashboard 服务 → 机队服务卡（路由）
- 计费商务谈判 → 本卡 Boundary

## E — 可执行步骤

输入契约：LMS 侧项目与许可池已建（项目状态 Active）、swk 含 CCSID 与 lock 431=1、FTR/RTR 已通、NTP 已配。LMS 侧没建项目 → 判停先推商务/交付链路。

1. 下载许可：MyPortal Asset & service manager 逐产品下载 .swk。完成标准：项目 Active 且文件到手
2. 装许可：swk 入 OXE 后重启。完成标准：重启完成
3. 开关核对：spadmin 核 OPEX Flag=1、PANIC Flag=0、431 Opex Mode=1。完成标准：三处一致
4. 前提收口：incvisu 见 6201 CCagent 与 6250 LmsAgent started；登录横幅 Panic LMS Check=0。完成标准：双 agent 在跑
5. 对账：spadmin 11 读四列（中间 lms/oxe 必须相等），10 强制同步。完成标准：Synchonization done 且两列一致
6. 实测消耗：建/删用户与软话机、设阈值，逐项复核计数增减。完成标准：计数与配置联动正确
7. 排障：NOE 屏显 No license available 或 SIP 402（事件 5816、sipalarm.log）→ 查许可链。完成标准：根因定位

判停点：

- 装了许可系统仍按 CAPEX 行为 → 按"swk 含 CCSID、lock 431=1、确实重启过"三件套顺序排查
- LMS 不可达时想建带许可的用户 → 停，设备不会创建；删除/停用可做、同步延后
- 收到 654 事件 → 按剩余天数倒排修复窗口：失联 30 天后 15 天即执行最狠降级
- C2P 转换中想加 add-on → 停，转换期不允许；范围外扩容走常规 PoD 无折扣
- 引用 spadmin 计数示例 → p404 例子有排版错误（nr-02），判据以"lms/oxe 一致"为准

输出契约：OPEX 生效基线（Flag/计数/同步记录）+ 订阅消耗台账（阈值与映射核对）+ panic 应急预案。

## B — 边界

- CAPEX 模式下 OPEX activation 旗标"显示但不生效"——判断系统模式以 lock 431/spadmin 的 OPEX Flag 为准（p399）
- 订阅目录 24 项与件号是 Ed12 时点快照，商务目录动态变化；仅显示申请人所在国家授权的条目
- OPEX 收窄两点：ACD 不再分 CCD/RSI、DR-Link 不再分 IP/TDM，各自合并为单一阈值（p405）
- OV8770 订阅四个缩水点：30 客户端、5 万管理用户、不能管 CAPEX OXE、不能管 OXO/OpenTouch（p363）
- 其他应用的 LMS 校验周期与失联后果（8770 每夜/VAA 午夜/O2G 12h/OPR 24h；30 天宽限后各自失效）按 p375 口径
- VAA/VNA 无原生负载均衡高可用；VNA 的 911 并发由 SIP 中继承载（p364）
- 实验口径：NTP 192.168.1.252、许可池 "15 | 0/0 | 18" 为演示值
