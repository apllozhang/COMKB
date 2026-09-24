# OXE 首登加固（四账户、密码策略、失败锁定与老化）

## R — 原文依据

> "4 accounts can be used on the OXE: • mtcl: maintenance account … • swinst: 'Facilities' account … • root: Administrator account, expert maintenance … • client: Account with basic access • Disabled by default"（p88）
> "Direct access (by login request) to the root account can only be performed on the console port."（p90）
> "Password string must have a minimum of 14 characters … Possible values of unsuccessful attempt before locking an account • 3 <= Number of unsuccessful attempts <= 5 • Default value is '3'"（p89, p92）

出处：ENTPXTE400EN p82-107。

## I — 自述

登录准入是"碰机器"的第一道门，三条通道、四个账户、一套密码治理：

1. **通道**：物理 CS 走 V24 串口或 SSHv2（Putty/Teraterm）；虚拟 CS 走各 hypervisor 控制台或 SSHv2；GAS 走 VGA+键鼠或 SSHv2。V24 下可用 ifconfig -a 或 netadmin 找回 IP
2. **四账户**：mtcl=日常维护与 su 跳板；swinst=设施菜单（启停/备份恢复/日期/账户）；root=专家维护（安全管理），仅本地控制台直登；client=基础访问，默认禁用、经 swinst 启用且需话务运行
3. **密码九规则**：≥14 字符；≥2 字母（必含 1 大写）；≥2 数字；≥1 特殊字符；不含账户名；无 4 连同字符；无 4 连顺序字符；无字典词；与最近 24 个历史密码不同
4. **失败锁定**：连续失败 3-5 次（默认 3）锁 15 分钟，swinst 可调
5. **密码老化**：有效期在 10-366 天范围内取值（原文为开区间，见 needs-review nr-01；0=不老化），到期强制改密；RADIUS 场景必须关闭老化

会话与横幅：root/mtcl 固定 900 秒无操作登出且不可配置；登录横幅含版本、Role、SSH/iptables 状态、PANIC 旗标。

## A1 — 书中案例

**账户与密码实验**（p95-107，How-To）：

1. 物理机接串口，虚拟机经 vSphere 控制台进入 OXE
2. mtcl 登录（实验口令 Administrator5689!），横幅显示版本与安全状态
3. root 登录验证"仅本地"限制；或从 mtcl 执行 su -（需 root 密码）
4. swinst 建 client 账户并登录，验证仅基础四项菜单
5. 同菜单改 mtcl 密码，按九规则设新密码
6. 失败锁定实验：次数设 4，连错验证锁定 15 分钟，再恢复默认 3
7. 老化实验：mtcl 设 21 天，把系统月份 +1 后重登录验证强制改密
8. 验证：四账户均可登录，锁定与强制改密行为符合配置

## A2 — 未来触发

使用情境：新 OXE 开局首次登录；SSH 连不上 root；要改密码/设锁定/设老化；启用 client 账户；900 秒掉线疑问；RADIUS 用户登录被拒。

语言信号：登录 / login / mtcl / swinst / root / client / V24 / SSHv2 / 密码策略 / 14 位 / 锁定 / 老化 / aging / RADIUS / 900 秒。

与相邻能力区分：IP 地址与防火墙配置 → CS 网络与防火墙能力；登录后的启停操作 → 系统启停能力（路由卡）。

## E — 可执行步骤

输入契约：物理访问方式（串口/KVM/虚拟机控制台）或网络可达性、客户密码规范。没有本地访问且网络又不通时，先解决带外通道再继续。

1. 选通道登录：本地串口 115200 或 SSHv2 到可达地址，用 mtcl 登录。完成标准：横幅显示版本与 Role
2. 核对账户基线：确认 client 状态与各账户密码是否符合客户规范。完成标准：账户清单与责任人对齐
3. 收紧密码策略：swinst 系统管理菜单设失败锁定次数（3-5）与老化期（10-366 天范围内）。完成标准：策略值与客户安全基线一致
4. 逐账户改密：按九规则（≥14 字符+大小写/数字/特殊字符组合）改掉全部默认密码。完成标准：无默认密码残留（可用 securitystatustool 复核）
5. client 按需启用：确认话务运行中再经 swinst 启用并设强密码。完成标准：如启用则登录可用，如不用则保持禁用
6. 记录并移交：账户责任人、策略值、变更时间写入交付记录。完成标准：交接单齐全

判停点：

- 客户用 RADIUS 认证却要求开密码老化 → 停，两机制互斥（n11），必须关老化并说明原因
- 远程现场要求"开放 root SSH 直登" → 停，架构仅允许本地直登；给 mtcl+su 流程替代方案
- 密码不满足九规则被拒 → 停，不要降级存储弱密码；按规则重设
- 900 秒超时影响长脚本 → 停，说明不可配置（p90），改用脚本内保活或分段执行

输出契约：可登录且策略收紧的系统访问基线 + 账户/策略台账。

## B — 边界

- 教材全部口令（Administrator5689! / Superuser2580* / letacla1 等）为实验口径（n01），照抄进生产等于零防线；首连即改密是强制动作
- root 直登仅限本地（串口/KVM）；SSH 侧必须 mtcl 登录后 su -（p90/p99 双 Warning）
- 900 秒无操作超时不可配置；client 账户菜单仅基础项且需话务运行（p88/p102）
- 老化期 10-366 天为开区间口径（nr-01）；"0=不老化"与 RADIUS 互斥规则并存（n11）
- 主动防御类扩展（旁路认证/双因子）不在本书范围，生产加固按客户安全规范与 ALE 安全公告执行
