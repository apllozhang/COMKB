# Access Guardian 接入认证（UNP 档案、802.1x/MAC、RADIUS 降级）

## R — 原文依据

> "Role Based Access Control with UNP (Universal Network Profile) • Auto-sensing, multi-client authentication on a port"（p456）
> "Authentication Method • MAC-based (non-supplicant) or • 802.1x-based (supplicant) ... RADIUS Access-Accept + UNP name"（p457）
> "Users are moved to a specific profile when RADIUS server is not available. ... Auth Server Down Profile1 = ag_SrvDownPrf, Auth Server Down Timeout = 60"（p474）
> "Parameters Default ... retries 3 ... seconds 2 ... auth_port 1812 ... acct_port 1813 ... ssl | no ssl No ssl"（p472）

出处：DT00XTE215EN p454-485。

## I — 自述

基于 UNP 的角色接入控制：认证成功后 RADIUS 以 Filter-Id 属性回传 UNP 名，用户按档案进 VLAN 并吃策略（VLAN+ACL/QoS 策略列表+位置+时段）。

1. **决策流**（p457-458）：802.1x 开且终端支持走 supplicant 认证；否则 MAC 认证开则以源 MAC 作账号密码
2. **结果分支**：Pass 按 Filter-Id 入 UNP；Fail 进 Default UNP（注册/隔离）；服务器不可达迁 auth-server-down 档案（默认 60 秒重试重认证）；无匹配 Block 或 pass-alternate 备用档案
3. **配置五层**（p461-474）：unp port port-type bridge + 802.1x/mac 认证；validity-location/period 位置时段；policy list type unp 挂规则
4. **档案与 AAA**：unp profile（map vlan + qos-policy-list + 位置/时段策略）；AAA profile（device-authentication + accounting + 服务器）
5. **RADIUS 默认参数**（p472）：retries 3、timeout 2 秒、认证 1812、计费 1813、SSL 默认关（建议启用 TLS，服务器侧先开）；MAC 会话计时器默认 12 小时
6. **降级三口径**（p466/p474/p478）：Filter-Id 缺失走 pass-alternate（802.1x 与 MAC 各自可配）；服务器不可达全体迁 auth-server-down 档案；MAC 无登记一律 Block
7. **监控**：show unp user / status / details（Profile From Auth Server、Role、Source=Radius）

## A1 — 书中案例

**Access Guardian 实验**（p476-485，How-To）：

1. 声明 RADIUS：aaa radius-server my_radius host 192.168.100.102 key（实验口径），device-authentication 802.1x 与 mac，accounting，ip service source-ip Loopback0 radius
2. qos flush/apply 清掉全局 ACL 规则，重建 deny_ftp 与 deny_http 规则（改为按用户档案生效）
3. policy list type unp enable 挂规则：deny_employees（禁 FTP）、deny_contractors（禁 HTTP）
4. unp profile UNP-employee/UNP-contractor：qos-policy-list + map vlan 20/30
5. 用户口 unp port 1/1/1 port-type bridge + 802.1x-authentication + mac-authentication
6. aaa test-radius-server 验证：user employee 返回 Filter-ID=UNP-employee
7. 客户端开 802.1X（PEAP+免 CA+MSCHAPv2），flush 端口后重连：show unp user 显示 VLAN 20/UNP-employee/Active
8. 换 contractor 凭据重连：落入 VLAN 30 与 deny_contractors 角色
9. 关闭 802.1x 走 MAC 认证：服务器无该 MAC 登记，show unp user 显示 Profile=-、Status=Block
10. 清理：no unp port 后 write memory flash-synchro

## A2 — 未来触发

使用情境：员工/承包商分区准入；认证后动态下 VLAN 与策略；打印机/摄像头等哑设备接入口；RADIUS 挂了用户怎么办；认证上不了网排查。

语言信号：Access Guardian / UNP / 802.1x / MAC 认证 / RADIUS / Filter-Id / pass-alternate / auth-server-down / Block / supplicant / PEAP / device-authentication / unp profile / 动态 VLAN 准入。

与相邻能力区分：

- 非认证的 MAC/IP 分类入 VLAN：VLAN 与路由能力卡（UNP 简单分类）
- 全局 ACL 策略写法：QoS 与 ACL 策略能力卡
- RADIUS 服务器上怎么建用户库：书外（本卡只管交换机侧）

## E — 可执行步骤

输入契约：用户角色矩阵（角色/认证方式/VLAN/策略）、RADIUS 服务器地址与密钥、哑设备清单与放行策略。RADIUS 服务器侧用户库未就绪 → 判停先补书外前提。

1. 声明服务器：aaa radius-server（建议 TLS）+ aaa device-authentication 802.1x/mac + accounting。完成标准：test-radius-server 返回预期 Filter-ID
2. 策略改挂档案：全局规则清场，重建规则并 policy list type unp enable。完成标准：列表 enable 且规则挂接
3. 建 UNP 档案：unp profile map vlan + qos-policy-list（+ 位置/时段按需）。完成标准：show unp profile 与矩阵一致
4. 端口准入：unp port port-type bridge + 802.1x/mac 认证（+ pass-alternate 备用档案）。完成标准：端口进入认证态
5. 用户验证：客户端 802.1X 重连，show unp user/details 确认 VLAN、Role、Source=Radius。完成标准：各角色落位正确
6. 降级验证：服务器不可达演练 auth-server-down 档案；哑设备验证 Block 或放行路径。完成标准：降级行为符合设计
7. 固化：write memory flash-synchro。完成标准：配置已保存

判停点：

- 认证通过但进错 VLAN → 查 RADIUS Filter-Id 是否回传（test-radius-server 可单独验证），缺了走 pass-alternate 而不是反复改交换机
- 哑设备上线即断网 → 服务器无 MAC 登记时 Block 属设计行为；要么登记 MAC，要么走分类规则/默认档案放行
- RADIUS 服务器侧配置缺失 → 停，用户库/证书在书外，先补齐再回到交换机侧
- 802.1x 客户端配置问题（PEAP/证书） → 按 p481 客户端口径核对（免 CA + MSCHAPv2），属客户端域

输出契约：角色化准入生效（各角色 VLAN/策略落位）+ 降级路径验证记录 + 哑设备处理方案。

## B — 边界

- RADIUS 服务器侧（用户库、证书、TLS 开启）全书不教，实验直接用现成 AAA Training Server 192.168.100.102（实验口径）
- "UNP 全称书中两写"（User/Universal Network Profile）见 needs-review nr-03，同一概念
- 同端口 802.1x 与 MAC 认证并存时，非 supplicant 设备自动走 MAC 认证（auto-sensing multi-client）
- Captive Portal 挂钩在属性清单中点到（p467），本书不展开部署
- employee/contractor 用户名密码、VLAN 编号均为实验口径（p446/p478）
- MAC 会话 12 小时为默认口径（p472）；改超时属生产化调参，以 CLI Reference 为准
