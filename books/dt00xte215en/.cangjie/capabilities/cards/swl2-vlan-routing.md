# VLAN 与 VLAN 间路由（三入口、UNP 分类、802.1Q、IP 接口）

## R — 原文依据

> "Ports become members of VLANs by • Static Configuration • Mobility/with or without Authentication • 802.1q"（p185）
> "UNP Port classification rules 1. Port/Linkagg 2. Domain 3. MAC address 4. MAC-OUI 5. MAC address range 6. LLDP 7. Auth-type 8. IP address 9. VLAN tag"（p189）
> "IP interfaces are associated with VLANs • IP routing is active as soon as at least one IP interface is associated with a VLAN"（p195）
> "The first interface bound to a VLAN becomes the primary interface for that VLAN."（p348）

出处：DT00XTE215EN p183-214, p291-297, p345-348。

## I — 自述

端口进 VLAN 有三条通道，路由由 IP 接口绑定 VLAN 触发：

1. **静态**：vlan <id> 建、members port untagged/tagged 挂口、支持批量（vlan 10-15 100-105）；VLAN 1 不可删只可禁（p187/p205/p213）
2. **动态 UNP**：按流量特征把移动口分入 VLAN；九条简单规则按编号即优先级，绑定规则=多条件 AND，扩展规则=命名列表+precedence；生效序 Extended > Binding > Simple；UNP 口启用而认证关闭/失败时应用分类规则（p189-192）
3. **802.1Q**：一条链路承载多 VLAN——端口默认 VLAN 未打标桥接，其余 VLAN 打标共链；4096 个 tag、802.1p 三位 8 级优先级、硬件实现（p199/p292/p295）
4. **IP 接口与路由**：ip interface <name> address <ip/mask> vlan <id> 充当网段网关；≥1 个 IP 接口即激活 IP 路由；第一个绑定该 VLAN 的接口为主接口；VLAN 无活动成员则其 IP 接口 DOWN、不回 PING、不进路由通告（二层广播域不受影响）
5. **监控**：show vlan / show vlan members / show vlan members port；show ip interface / show ip routes（LOCAL 路由自动生成）

## A1 — 书中案例

**VLAN 与路由实验**（p204-214，How-To）：

1. 查默认态：show vlan 仅 VLAN 1，show vlan members 全部口 inactive
2. 建 IP 接口：ip interface int_1 address 192.168.10.5/24，show 显示 Device=unbound
3. 绑定 VLAN：ip interface int_1 vlan 1（可与建址一步合并）
4. 激活端口：interfaces 1/1/1 admin-state enable，端口变 forwarding、int_1 变 UP
5. Client 5 设 192.168.10.105/24 网关 192.168.10.5，ping 网关验证
6. 建 VLAN 50 并绑 int_50：未挂成员时接口 DOWN（实验思考题），挂口 enable 后 UP
7. Client 9 ping Client 5 验证跨 VLAN 路由，show ip routes 出现两条 LOCAL 路由
8. 动态 VLAN：vlan 40 + unp profile employee map vlan 40 + unp classification mac-address <Client6 MAC> + unp port 2/1/1 port-type bridge
9. unp user flush 后 show unp user 显示 VLAN 40/employee/Active，端口出现 40 unpUntag forwarding
10. 清理：逐条 no 掉 UNP 分类/端口/档案与 VLAN/IP 接口，复查 snapshot 为空、端口回 VLAN 1

## A2 — 未来触发

使用情境：按部门隔离二层；交换机间单链跑多 VLAN；新建网关接口 DOWN；按 MAC/位置把终端动态分 VLAN；跨 VLAN 不通；弃用 VLAN 1。

语言信号：VLAN / vlan members / untagged / tagged / 802.1Q / trunk / 默认 VLAN / UNP / 动态 VLAN / 分类规则 / mac-address 分类 / ip interface / 网关 / VLAN 间路由 / LOCAL 路由 / int DOWN。

与相邻能力区分：

- 网关冗余与 DHCP 取址：三层服务能力卡
- 端口收 BPDU 关闭等用户口安全：QoS 与 ACL 策略能力卡
- 认证驱动的动态入网：Access Guardian 能力卡

## E — 可执行步骤

输入契约：VLAN 规划表（编号/命名/成员口）、IP 编址（每 VLAN 网段与网关地址）、动态分类的匹配特征（MAC/IP/端口）。802.1Q 链路两端规划必须一致。

1. 建 VLAN：vlan <id>（可批量）+ name；规划弃用 VLAN 1 时改用业务 VLAN 作链路默认 VLAN。完成标准：show vlan 列表正确
2. 挂成员：静态口 members port untagged/tagged；互联口把业务 VLAN 置 tagged、默认 VLAN 保持桥接。完成标准：show vlan members 与规划一致
3. 绑网关：ip interface address vlan 一步完成；确认至少一个成员口 enable。完成标准：接口 UP 且 show ip routes 出现 LOCAL
4. 连通验证：终端 ping 网关，再跨 VLAN ping 验证路由。完成标准：三层可达
5. 动态入网（按需）：unp profile map vlan + unp classification 规则 + unp port port-type bridge，flush 后验证。完成标准：show unp user 命中档案
6. 固化：write memory（VC 用 flash-synchro）。完成标准：配置已保存

判停点：

- 新建 VLAN 网关接口 DOWN → 首查 VLAN 无活动成员口，enable 成员或确认对端连接后再排路由
- 想删除 VLAN 1 → 不可能，只能禁用；改用业务 VLAN 承载并调整链路默认 VLAN
- 互联口状态显示 tagged blocking → 端口状态取决于 STP 根桥选举，"每 POD 不同"属预期，先查生成树而非 VLAN 配置
- 认证场景要按 RADIUS 下发 VLAN → 转 Access Guardian 能力卡（Filter-Id 机制），不要用简单分类规则硬凑

输出契约：按规划生效的 VLAN 与网关（接口 UP、路由可达）+ 动态分类规则清单（如适用）。

## B — 边界

- 物理端口永远保留一个默认 VLAN 做二层桥接，不存在"全部打标"模式；防默认 VLAN 过 trunk 就换业务 VLAN（p295）
- UNP 简单规则九条的编号即优先级；扩展规则列表内设备须匹配全部规则（p189-192）
- UNP 的认证分支（Filter-Id 下发）在 Access Guardian 能力卡；本卡只覆盖非认证分类
- 802.1p 与 DSCP 的标记改写语义（信任口/非信任口）在 QoS 与 ACL 策略能力卡
- 实验 VLAN 编号与客户端 IP 规则（192.168.x.10N）为实验口径，生产按客户编址
- VLAN 数量上限 4096 为 802.1Q 标准口径；型号相关规格差异查 Specification Guide
