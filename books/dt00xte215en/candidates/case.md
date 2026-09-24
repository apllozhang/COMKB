# 案例/实验/操作序列候选 — OmniSwitch LAN Access Switching (DT00XTE215EN Ed23)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、账号、POD 规则）标注"实验口径"。交换机统一凭据 admin/Superuser=1（实验口径，p15）。
> 条目说明: 全书 17 个 How-To 实验章 → 17 条 + Lightning Config 操作序列（讲义内嵌步骤，c17）共 18 条。

```yaml
- id: c01
  title: 远程接入实验——SSH 登录、改 Inactivity Timer、WebView 建/删 VLAN
  type: lab
  source_pages: p91-101
  source_chapter: Remote Switch Access — "Administrate the OmniSwitches remotely"
  source_quote: |
    "Example with switch 3 pod 21 type : ssh admin@10.4.21.3 ­ Then the password of the switch" (p95)；
    "sw3 (6560-A) -> session cli timeout 60 ... sw3 (6560-A) -> write memory ... File /flash/working/vcsetup.cfg replaced." (p96)；
    "Select Layer 2 > VLAN in the VLAN management column or in the left menu. ­ Click on the '+' icon to create a new VLAN ... Vlan : 59 Description : Student ­ Click on SUBMIT" (p100)
  steps: |
    1. 前置核查：实验交换机已预配到管理网 10.0.0.0 的静态路由（非空配置，p92）；按 p93 表核对 7 台交换机 EMP 地址（10.4.Pod#.{1,2,3,5,6,7,8}，实验口径），从 POD 桌面逐台 ping。
    2. SSH 前核查：登录 OS6560-A，show aaa authentication 确认各服务类型 1st authentication server = local；若 SSH 显示 Authentication = denied，执行 aaa authentication ssh local（p95 Tips）。
    3. 测试 SSH：桌面右键 Open Terminal Here → ssh admin@10.4.<pod>.3 → 输交换机密码。
    4. CLI 改会话参数：session cli timeout 60 → write memory → show session config 验证 Cli Inactivity Timer = 60（p96）。
    5. WebView 登录：浏览器开 https://10.4.Pod#.3（R8 强制 SSL），admin + 密码登录（p97-98）。
    6. WebView 改会话参数：Security > ASA > Session > Configuration，CLI 改 45、Webview 改 15 → Apply → 回 CLI show session config 验证（p98）。
    7. WebView 写内存：顶部图标栏第三个图标（write memory）→ Yes 保存到 running（p99）。
    8. 机框可视化：Physical > Chassis management > Chassis visualization，悬停端口看信息（p99）。
    9. WebView 建 VLAN：Layer 2 > VLAN → "+" → Vlan 59 / Description Student → SUBMIT → CLI show vlan 验证出现 VLAN 59 student（p100）。
    10. WebView 删 VLAN：Layer 2 > VLAN Mgmt → 勾选 VLAN 59 → 垃圾桶 → Yes → CLI show vlan 验证只剩 VLAN 1 与 4094 → write memory 固化（p101）。
  verification: |
    p96/p98 show session config 两次数值变化（60 → 45/15）；p100 show vlan 出现 59 student；p101 删除后 VLAN 59 消失且 write memory 成功替换 vcsetup.cfg/vcboot.cfg。
  conditions: 交换机已预配管理网静态路由（p92）；WebView 访问已启用（Remote-Lab 预配，p97）。
  tags: [lab, ssh, webview, session, vlan]

- id: c02
  title: 闪存目录实验——改动/保存/认证/回滚全流程与用户目录
  type: lab
  source_pages: p140-149
  source_chapter: OmniSwitches Directories Content (R8)
  source_quote: |
    "sw3 (6560-A) -> show microcode working ... Nos.img 8.10.9.R04 111683640 Alcatel-Lucent OS" (p141)；
    "IF THE OMNISWITCH IS REBOOTED NOW ... THE OMNISWITCH WILL ROLL BACK TO THE WORKING DIRECTORY ... IN OUR CASE, VLAN 2, 3 AND 99 WILL BE LOST" (p143)；
    "sw3 (6560-A) -> VLAN 4 ... -> write memory ... ERROR: Write memory is not permitted when switch is running in certified mode" (p145)
  steps: |
    1. 打开 OS6560-A 控制台（RustConn，admin + 密码登录）。
    2. 查看文件与微码：ls -l /flash/working（或 /flash/certified）；show microcode working|certified|loaded（实验镜像 8.10.9.R04，实验口径，p141）。
    3. 查启动目录：show running-directory → Running configuration: WORKING / Certify-Restore: CERTIFIED / Synchronized（p142）。
    4. 制造未保存改动：vlan 2、vlan 3、vlan 99 → show vlan 确认 → show running-directory 显示 NOT SYNCHRONIZED（p143）。
    5. 保存：write memory → show running-directory 显示 CERTIFY NEEDED + SYNCHRONIZED（p144）。
    6. 验证 reload all 回滚：reload all → 确认 y → 重启后 show running-directory 显示 Running=CERTIFIED、show vlan 中 VLAN 2/3/99 消失（p144）。
    7. 验证 certified 只读：vlan 4 → write memory → 报错 "Write memory is not permitted when switch is running in certified mode"（p145）。
    8. 从 working 重启取回配置：reload from working no rollback-timeout → y → VLAN 2/3/99 重现（p145）。
    9. 用户目录：mkdir lab → cp working/*.* lab（boot.md5 报 permission denied 可忽略）→ ls lab 核对 → reload from lab no rollback-timeout → show running-directory 显示 Running=lab（p146）。
    10. 认证用户目录：copy running certified → flashManager 日志 "Copy running to certified succeeded" → show running-directory 显示 lab + CERTIFIED（p146-147）；此后断电重启将从 lab 启动。
    11. 清理：rm -Rf lab → reload from working no rollback-timeout（p147）。
    12. 附件（R-Lab 无法做，USB 口被占）：usb enable → usb backup admin-state enable → write memory 观察 "saved to USB" 与 /uflash/6560/{certified,working} 内容（p148-149）。
  verification: |
    三次 show running-directory 状态迁移（CERTIFIED→CERTIFY NEEDED→certified 只读报错→lab CERTIFIED）；p143/144 Warning 框两段重启行为与实测一致。
  conditions: 实验口径：镜像 8.10.9.R04；lab 目录若已存在忽略报错继续（p146 Tips）。
  tags: [lab, directories, rollback, write-memory, usb]

- id: c03
  title: Virtual Chassis 实验——两台 OS6360 组 VC 并监控
  type: lab
  source_pages: p173-182
  source_chapter: Virtual Chassis-6360
  source_quote: |
    "sw5 (6360-A) -> virtual-chassis chassis-group 1 ... sw5 (6360-A) -> virtual-chassis chassis-id 1 configured-chassis-priority 200 ... Notes A reload is mandatory to consider the chassis priority" (p175)；
    "sw6 (6360-B) -> virtual-chassis chassis-id 1 configured-chassis-id 2 ... WARNING - Virtual chassis topology change detected. Chassis 1 missing! Configuration associated with missing chassis will be erased permanently! Confirm to continue (Y/N) : y" (p176)；
    "sw5 (6360-A) -> show virtual-chassis vf-link ... 1/0 Up 1/1/27 2 2 1 10G" (p180)
  steps: |
    1. 识别机型与 VFL 口：show chassis 看型号——OS6360-P10 用 VFL 1/1/11-12，OS6360-P24 用 1/1/27-28（实验 POD 有两种，p174）。
    2. 6360-A：show virtual-chassis topology（初始 Local Chassis 1/Pri 100/Group 0）→ virtual-chassis chassis-group 1 → virtual-chassis chassis-id 1 configured-chassis-priority 200 → write memory → reload from working no rollback-timeout（约 4 分钟，实验口径）→ 重启后 Pri=200（p175-176）。
    3. 6360-B：virtual-chassis chassis-id 1 configured-chassis-id 2 → virtual-chassis chassis-group 1 → write memory（出现"缺失 chassis 配置将被清除"警告，确认 y）→ reload from working（p176-177）。
    4. 配 VFL（A 与 B 同法，端口按机型）：virtual-chassis vf-link-mode auto → virtual-chassis auto-vf-link-port <port1> → <port2> → write memory；show configuration vcm-snapshot chassis-id N 核对（p177-178）。
    5. 启用接口：interfaces <vfl ports> admin-state enable；6360-B 侧 VFL 口自动 LINK UP 并重启（约 5 分钟，实验口径）；A 侧出现 isisVc 日志 "New Master: chassisId 1"（p178）。
    6. 监控：show virtual-chassis topology（Chassis 2 带 "+" 后缀表示未保存拓扑）→ write memory flash-synchro（日志 Synchronizing chassis 2）→ 后缀消失（p179）。
    7. VFL 详情：show virtual-chassis vf-link 与 vf-link member-port（Is Primary 字段区分主/备端口；P10 型号 1G，P24 型号 10G）（p180）。
    8. 一致性：show virtual-chassis consistency 核对 Type/Group/Hello(15)/Control Vlan(4094)/License(A)（p180）。
    9. 远程成员访问：ssh-chassis admin@2 → 看 Local Chassis=2 确认在 B 上 → logout 返回（p181）。
    10. 收尾：关闭未用接口（P24: 1/1/1-26 与 2/1/1-26；P10: 1/1/1-10 与 2/1/1-10）→ WebView https://10.4.pod#.5 打开 Chassis visualization 查看两机框（p181-182）。
  verification: |
    p179 topology 显示 Chassis 1 Master Pri 200 + Chassis 2 Slave Running（保存后无 +）；p180 vf-link 两链 Up、consistency 全 OK。
  conditions: 实验口径：VFL 端口 11-12 或 27-28 按 POD 机型；重启约 4-5 分钟。
  tags: [lab, virtual-chassis, vfl, vc]

- id: c04
  title: VLAN 实验——建 VLAN/绑 IP 接口/连通验证/UNP 动态 VLAN/删除
  type: lab
  source_pages: p204-214
  source_chapter: VLANs — "Manage VLANs on the OmniSwitches"
  source_quote: |
    "sw5 (6360-A) -> ip interface int_1 address 192.168.10.5/24 ... The Device status is unbound. It is because the IP interface has not been associated to a VLAN yet." (p206)；
    "sw5 (6360-A) -> unp profile employee ... -> unp classification mac-address 00:50:56:90:ee:0a profile1 employee ... -> unp user flush port 2/1/1" (p212-213)；
    "VLAN 1 cannot be deleted. It is only possible to deactivate." (p213)
  steps: |
    1. 查默认态：show vlan（仅 VLAN 1）、show vlan 1（Admin enabled/Oper disabled——无成员）、show vlan members（全部口 inactive）、show vlan members port 1/1/1（p205-206）。
    2. 建 IP 接口：ip interface int_1 address 192.168.10.5/24 → show ip interface 显示 Device=unbound → ip interface int_1 vlan 1 绑定（两步可合并为一条，p206 Notes）。
    3. 激活端口：interfaces 1/1/1 admin-state enable（所接为 Client 5）→ show vlan members port 1/1/1 变 forwarding → int_1 变 UP。
    4. Client 5 设 IP 192.168.10.105/24 网关 192.168.10.5 → ping 192.168.10.5 验证（p208）。
    5. 建 VLAN 50：vlan 50 → ip interface int_50 address 192.168.50.5/24 vlan 50 → 状态 DOWN（无成员，思考题）→ vlan 50 members port 1/1/2 untagged → interfaces 1/1/2 admin-state enable → int_50 UP（p209-210）。
    6. Client 9 设 192.168.50.105/24 网关 192.168.50.5 → show ip routes 出现两条 LOCAL 路由 → Client 9 ping Client 5 验证跨 VLAN 路由（p211）。
    7. 动态 VLAN（按 MAC）：vlan 40；Client 6 设静态 192.168.40.106/24 无网关 → 记录其 MAC（show mac-learning port 2/1/1）→ unp profile employee → unp profile employee map vlan 40 → unp classification mac-address <Client6 MAC> profile1 employee → unp port 2/1/1 port-type bridge → unp user flush port 2/1/1 → show unp user 显示 VLAN 40/employee/Active → show vlan members port 2/1/1 出现 40 unpUntag forwarding（p212-213）。
    8. 清理：no ip interface int_50 / no vlan 50 / no vlan 40 / no ip interface int_1；UNP 清理——sh configuration snapshot DA-UNP 查看残留 → no unp classification ... / no unp port 2/1/1 / no unp profile "employee" → 复查 snapshot 为空、端口回 VLAN 1 forwarding（p213-214）。
  verification: |
    p208 Client 5 ping 网关通；p211 Client 9 ping Client 5 通（路由验证）；p213 show unp user 显示 employee/Active/VLAN 40；p214 清理后恢复默认。
  conditions: 实验口径：Client IP 按 VLAN x.10N 规则；MAC 地址每 POD 不同须现场读取。
  tags: [lab, vlan, unp, routing, ip-interface]

- id: c05
  title: 诊断工具实验——swlog/事件日志/命令日志/镜像/抓包/health/RMON
  type: lab
  source_pages: p261-269
  source_chapter: Switch maintenance and Diagnostics tools
  source_quote: |
    "sw7 (6870-A) -> swlog disable ... Operational Status : Not Running ... -> swlog enable" (p262)；
    "sw7 (6870-A)-> port-mirroring 1 source port 1/1/1 destination port 1/1/10 ... port-mirroring 1 enable ... show port-mirroring status 1" (p265)；
    "sw7 (6870-A)-> port-monitoring 1 pause ... port-monitoring 1 resume ... WARNING: Monitored data is available in file /flash/pmonitor.enc" (p265-266)
  steps: |
    1. swlog：在 6870-A show swlog（Running、console flash、级别 info）→ show log swlog（Ctrl+C 停止；可 grep/timestamp 过滤）→ swlog disable → show swlog 变 Not Running → swlog enable（p262）。
    2. 可读事件日志：swlog appid all subapp all level event → show log events（时间戳 : CMM : 模块 : 描述格式）→ 与 show log swlog 输出对比（p263）。
    3. 命令日志：show command-log → command-log enable → vlan 4-5 与 no vlan 4-5 → show command-log 显示两条命令（用户/时间/来源 console/结果）→ command-log disable（p264）。
    4. 端口镜像：port-mirroring 1 source port 1/1/1 destination port 1/1/10 → port-mirroring 1 enable → show port-mirroring status 1（Mirror Direction bidirectional）→ no port-mirroring 1 删除（p265）。
    5. 端口抓包：interfaces 1/1/1 admin-state enable → port-monitoring 1 source port 1/1/1 enable → show port-monitoring status（64K/Brief//flash/pmonitor.enc）→ 从客户端 ping 造流量 → port-monitoring 1 pause → status（Oper OFF）→ resume → port-monitoring 1 disable（提示数据在 pmonitor.enc）→ ls -l 见 pmonitor.enc → show port-monitoring file 显示捕获帧 → no port-monitoring 1（p265-267）。
    6. health：show health（CMM CPU/内存当前/1 分/1 时/1 天）→ show health slot 1/1（含 Receive/Receive-Transmit）（p266-268）。
    7. RMON：interfaces 1/1/1 enable → show rmon probes（Ethernet 探针）→ show rmon probes history → show rmon probes stats → show rmon probes stats 1（Owner/时长/资源）→ 也可 probes history 1 / alarm 1（p268-269）。
  verification: |
    p265 镜像状态表 Config/Oper = Enable；p266 抓包 pause 后 Oper=OFF、resume 后 ON；p267 show port-monitoring file 输出捕获帧。
  conditions: 实验口径：交换机 6870-A，端口 1/1/1 接 Client；镜像与抓包不可同端口（p251）。
  tags: [lab, diagnostics, swlog, mirroring, monitoring, rmon]

- id: c06
  title: 链路聚合实验——6360 VC 与 6870-A 建 LACP 聚合并测冗余
  type: lab
  source_pages: p283-290
  source_chapter: Link Aggregation — "Create Dynamic Aggregation Links"
  source_quote: |
    "sw5 (OS6360-A) -> linkagg lacp agg 7 size 2 actor admin-key 7 ... Notes: Actor Admin Key ... the admin key has local significance only" (p285)；
    "sw7 (OS6870-A) -> linkagg lacp port 1/1/3-4 actor admin-key 7 ... show linkagg ... 7 Dynamic 40000007 2 ENABLED UP 2 2" (p286)；
    "sw7 (6870-A) -> interface 1/1/3 admin-state disable ... 1/1/3 Dynamic 1003 CONFIGURED NONE DOWN DOWN UNK ... 1/1/4 Dynamic 1004 ATTACHED 7 UP UP YES" (p290)
  steps: |
    1. 背景核对：聚合 78（VLAN 278）已存在于 6870-A 与 6860-B 之间；客户要求不使用默认 VLAN 1，聚合 7 的默认 VLAN 改为 VLAN 57（p284）。
    2. 6360 VC 侧：linkagg lacp agg 7 size 2 actor admin-key 7 → show linkagg（无端口，Oper DOWN）→ linkagg lacp port 1/1/3 actor admin-key 7 → linkagg lacp port 2/1/4 actor admin-key 7 → interfaces 1/1/3 与 2/1/4 enable（p285）。
    3. 6870-A 侧：linkagg lacp agg 7 size 2 actor admin-key 7 → linkagg lacp port 1/1/3-4 actor admin-key 7 → interfaces 1/1/3-4 enable → show linkagg（聚合 7 UP 2/2；另有预置聚合 17、78，p286）。
    4. 属性核对：两侧 show linkagg agg 7（SNMP Id 40000007、Actor/Partner Admin/Oper Key、Primary Port、Port Selection Hash）（p287-288）。
    5. 换默认 VLAN：两侧 vlan 57 → vlan 57 members linkagg 7 untagged → show vlan 57 members（端口 0/7 untagged forwarding）（p288）。
    6. 连通与冗余测试：两侧把 Client（5 与 7）口入 VLAN 57 并 enable；Client 5 设 192.168.57.105/24、Client 7 设 192.168.57.107/24 → Client 5 持续 ping 192.168.57.107 → 6870-A 上 interface 1/1/3 admin-state disable → show linkagg port 显示 1/1/3 CONFIGURED/DOWN、1/1/4 仍 ATTACHED UP → 恢复 interface 1/1/3 enable（p289-290）。
  verification: |
    p286 聚合 7 两端 UP 且 Selected/Attached = 2；p290 断一个成员口 ping 不断（LACP 冗余生效），恢复后回到 2/2。
  conditions: 实验口径：admin-key 与聚合号相同仅为习惯、非必须（p285 Notes）；Client IP 为实验口径。
  tags: [lab, linkagg, lacp, redundancy]

- id: c07
  title: 802.1Q 实验——三交换机间单链承载多 VLAN
  type: lab
  source_pages: p291-297
  source_chapter: 802.1q — "Apply 802.1q tagging on link aggregation and ports"
  source_quote: |
    "sw5 (6360-A) -> vlan 58 members port 2/1/3 untagged ... sw8 (6860-B) -> show vlan members port 1/1/3 ... 20 tagged blocking ... 58 untagged forwarding" (p292-295)；
    "Normally, to have Layer 2 connectivity between the two switches for all three VLANs, three physical links would be required. However, we will configure 802.1Q tagging to carry data from all VLANs over physical link." (p294)
  steps: |
    1. 直链段配置：6360 VC 的 2/1/3 与 6860-B 的 1/1/3 enable → 两侧 vlan 58 → vlan 58 members port <口> untagged（VLAN 58 作该链默认 VLAN）（p292）。
    2. 建业务 VLAN：三台交换机（6360 VC/6870-A/6860-B）各 vlan 20、vlan 30（p293）。
    3. 网关：VLAN 20 网关建在 6870-A（ip interface int_20 address 192.168.20.7/24 vlan 20），VLAN 30 网关建在 6860-B（int_30 192.168.30.8/24 vlan 30）→ show ip interface 显示 DOWN（无成员，思考题）（p293）。
    4. 打标：6360 VC——vlan 20/30 members linkagg 7 tagged 与 members port 2/1/3 tagged；6870-A——vlan 20/30 members linkagg 78 tagged 与 linkagg 7 tagged；6860-B——vlan 20/30 members linkagg 78 tagged 与 port 1/1/3 tagged（p294）。
    5. 核对：show vlan 20 members / show vlan 30 members / show vlan members port（实验注：端口状态取决于 STP 根桥选举，6860-B 的 1/1/3 可能 tagged blocking）（p294-295）。
    6. 终端验证：Client 5 口入 VLAN 20（vlan 20 members port 1/1/1 untagged），IP 192.168.20.105/24 网关 192.168.20.7；Client 6 口入 VLAN 30（2/1/1），IP 192.168.30.106/24 网关 192.168.30.8 → 各自 ping 网关 → 思考客户端间走二层还是三层（p296）。
    7. 收尾：三台 write memory flash-synchro（p297）。
  verification: |
    p295 端口视图同时显示 tagged（20/30）与 untagged（58）；p296 Client 各自 ping 通网关。
  conditions: 实验口径：VLAN 57 已由 c06 建好；STP 端口状态随根桥而异（p294 Notes）。
  tags: [lab, 8021q, vlan, tagging]

- id: c08
  title: STP 实验——指定根桥、识别端口角色、断链测收敛、1x1 负载分担
  type: lab
  source_pages: p313-323
  source_chapter: Spanning Tree Protocol (STP)
  source_quote: |
    "sw7 (6870-A) -> spantree vlan 20 priority 20000 ... spantree vlan 30 priority 20000" (p314)；
    "Only one side of the link(s) has a port or link aggregation with the status BLK (blocking). This ensures the neighbor(s) are still able to initiate a topology change in the event of a failure." (p317)；
    "sw5 (6360-A) -> linkagg lacp agg 7 admin-state disable ... notice how quickly Rapid STP recovers from a link failure" (p318)
  steps: |
    1. 指定根桥：6870-A 上 spantree vlan 20 priority 20000、spantree vlan 30 priority 20000 → show spantree 确认 VLAN 20/30 优先级 20000（0x4E20）（p314）。
    2. 识别端口状态：三台 show spantree vlan 20（看 Bridge ID 与 Designated Root 是否相同判根桥、Cost to Root、Topology Age/Changes）→ show spantree vlan 20 ports（角色 DESG/ROOT/ALT 与 FORW/BLK）→ show spantree ports blocking 汇总阻塞口（p315-317）。
    3. 思考题：哪一侧阻塞由什么决定？（根桥到各链路的路径成本与端口 ID 比较；同一链路仅一侧 BLK）（p317）。
    4. 冗余测试：Client 8 入 VLAN 20（6860-B port 1/1/1），IP 192.168.20.108/24 网关 192.168.20.7 → Client 8 持续 ping 192.168.20.105（Client 5）→ 6360-A 上 linkagg lacp agg 7 admin-state disable 模拟断链 → show spantree vlan 20（Topology Changes 增加、Age 重置）与三台端口状态（原 ALT 口转 FORW，无阻塞口剩余）→ 思考 Topology age/Root port 变化（p318-319）。
    5. 恢复与再收敛：linkagg lacp agg 7 admin-state enable → show spantree ports blocking 重新出现 VLAN 20/30 阻塞口（p320）。
    6. 1x1 负载分担：6870-A 恢复 VLAN 30 默认优先级 32768；6860-B 设 spantree vlan 30 priority 20000 → VLAN 20 根=6870-A（走 linkagg 7 方向），VLAN 30 根=6860-B（走 linkagg 8 方向）→ 三台 show spantree vlan 20 / vlan 30 / ports 核对两 VLAN 阻塞口互补（p320-323）。
  verification: |
    p316 根桥判定（Bridge ID = Designated Root）；p318-319 断链后 RSTP 快速恢复、阻塞口转移；p321-322 两 VLAN 的 ALT 阻塞口分别位于不同上行。
  conditions: 实验口径：优先级 20000；提示任何物理变更都会触发 STP 重收敛（p319 Tips）。
  tags: [lab, stp, rstp, load-balancing]

- id: c09
  title: DHL Active-Active 实验——建聚合 8、DHL 会话、VLAN 分流与故障切换
  type: lab
  source_pages: p336-344
  source_chapter: Dual Home Link Active-Active
  source_quote: |
    "sw5 (6360-A) -> linkagg lacp agg 8 size 2 actor admin-key 8 ... ERROR: Port cannot be added to Linkagg, please remove other configuration on this port ... no vlan 58 members port 2/1/3 ..." (p338)；
    "sw5 (6360-A) -> dhl 1 ... dhl 1 linka linkagg 7 linkb linkagg 8 ... Notes Spanning Tree is disabled on all the DHL enabled ports ... dhl 1 vlan-map linkb 30 ... dhl 1 admin-state enable" (p341)；
    "It can takes a few seconds for the VLAN 20 to be forwarded back on the link aggregation 8: when the failed link comes back up, DHL waits a configurable amount of time (default: 30 secs)" (p344)
  steps: |
    1. 前置：Client 5 口入 VLAN 20（p338）。
    2. 建 6360 VC ↔ 6860-B 聚合 8：6360-A linkagg lacp agg 8 size 2 actor admin-key 8 → 加端口 2/1/3 报错（口上有 VLAN 配置）→ 先清口（no vlan 58 members port 2/1/3、no vlan 20/30 members、no vlan 58）→ linkagg lacp port 1/1/4 与 2/1/3 actor admin-key 8 → enable 两口；6860-B 同法（清 1/1/3、建 agg 8、加 1/1/3-4）（p338-339）。
    3. VLAN 归位：两侧 vlan 57 members linkagg 8 untagged（换默认 VLAN）；vlan 20/30 members linkagg 8 tagged；6860-B vlan 57 members linkagg 78 tagged（p339-340）。
    4. 建 DHL：6360-A dhl 1 → dhl 1 linka linkagg 7 linkb linkagg 8 → dhl 1 vlan-map linkb 30（VLAN 30 归 LinkB，其余归 LinkA）→ dhl 1 admin-state enable（p341）。
    5. 监控：show dhl（会话 1 up/up、PE 30s、MAC Flushing none）→ show dhl 1（LinkA 0/7 Active Vlans 20 57；LinkB 0/8 Active Vlans 30；Protected Vlans 20 30 57）→ show dhl 1 linka / linkb → show vlan 20 members（0/7 forwarding、0/8 dhl-blocking）与 show vlan 30 members（互补）（p341-343）。
    6. 切换测试：Client 5（192.168.20.105/24 网关 192.168.20.7）持续 ping 192.168.20.7 → 启用 RAW 刷新（dhl 1 mac-flushing raw）→ linkagg lacp agg 7 admin-state disable → 观察丢包、show vlan 20 members 变 0/8 forwarding → 恢复 agg 7 enable → VLAN 20 回到 dhl-blocking 状态（等待约 30 秒抢占，默认值）（p343-344）。
    7. 收尾：write memory flash-synchro（p344）。
  verification: |
    p343 dhl-blocking/forwarding 互补；p343-344 断 agg 7 后 VLAN 20 立即走 agg 8、恢复后等 30 秒回切；show dhl 各字段与配置一致。
  conditions: 实验口径：LinkA=agg 7（→6870-A）、LinkB=agg 8（→6860-B）；DHL 端口自动禁 STP（p341 Notes）。
  tags: [lab, dhl, active-active, vlan-map]

- id: c10
  title: DHCP Relay 实验——核查路由、配置中继、客户端动态取址验证
  type: lab
  source_pages: p367-371
  source_chapter: DHCP Server & DHCP Relay — "Configure the DHCP Relay feature (aka IP Helper)"
  source_quote: |
    "sw7 (6870-A) -> ping 192.168.100.102 ... 64 bytes from 192.168.100.102: icmp_seq=1 ttl=127 time=2.08 ms" (p369)；
    "sw7 (6870-A) -> ip dhcp relay destination 192.168.100.102 ... ip dhcp relay admin-state enable ... Relay Mode = Global" (p370)；
    "Configure clients 5, 6, 9 and 10 in DHCP mode to obtain an IP address and DNS server address automatically." (p371)
  steps: |
    1. 核查路由：6870-A 与 6860-B 各 show ip routes 确认有到 192.168.100.0/24 的 OSPF 路由 → ping 192.168.100.102 通（p369）。
    2. 配中继：两台各 ip dhcp relay destination 192.168.100.102 → ip dhcp relay admin-state enable → show ip dhcp relay 核对（Enable/Max hops 16/Relay Mode Global/Opt82 Base MAC）（p370）。
    3. 核对客户端 VLAN：show vlan 20 members / show vlan 30 members（6360 VC 上 Client 口 1/1/1、2/1/1 与 1/1/2、2/1/2 归属正确；不正确按 vlan x members port y untagged 修正并 enable）（p370-371）。
    4. 客户端改 DHCP：Client 5/6/9/10 网卡改 Automatic (DHCP)（见远程实验室章操作）。
    5. 验证：show ip dhcp relay statistics——Reception From Client 与 Tx Server 计数增长（实验值 43/43 与 40/40，实验口径）；客户端拿到 192.168.20.x / 192.168.30.x 地址（p371）。
  verification: |
    p370 show ip dhcp relay Status=Enable 且 Relay Mode=Global；p371 统计计数非零、客户端获得对应网段地址。
  conditions: 实验口径：DHCP 服务器 192.168.100.102（同一台亦作 RADIUS/Web/FTP）；VLAN 间路由依赖此前实验配置。
  tags: [lab, dhcp-relay, dhcp]

- id: c11
  title: VRRP 实验——双 VRID 建虚拟网关、验证主备、改优先级指定主备
  type: lab
  source_pages: p383-390
  source_chapter: Virtual Router Redundancy Protocol (VRRP)
  source_quote: |
    "sw7 (6870-A) -> ip vrrp 1 interface int_20 ... ip vrrp 1 interface int_20 address 192.168.20.254 ... ip vrrp 1 interface int_20 admin-state enable ... Virtual router enabled IPv4 VRID=1" (p385)；
    "1 int_20 Master ... 2 int_30 Master（6870-A） ... 1 int_20 Backup ... 2 int_30 Backup（6860-B）" (p387-388)；
    "THE VRRP INSTANCE MUST BE DISABLED BEFORE CHANGING THE PRIORITY ... ip vrrp 1 interface int_20 admin-state disable ... priority 150 ... admin-state enable" (p390)
  steps: |
    1. 核对 VLAN 成员与 IP 接口（VLAN 20/30 各成员口归位；6870-A 需补 int_30：ip interface int_30 address 192.168.30.7/24 vlan 30；6860-B 需补 int_20：192.168.20.8/24 vlan 20）（p385-386）。
    2. 6870-A 建 VRID 1（int_20，VIP 192.168.20.254）与 VRID 2（int_30，VIP 192.168.30.254）；6860-B 同样建 VRID 1/2 指向相同 VIP（p385-386）。
    3. 查状态：两侧 show ip vrrp 1 / show ip vrrp 2（Version V2、Priority 100、Preempt Yes、Interval 100、Virtual MAC 00-00-5E-00-01-01/02）（p387）。
    4. 主备判定：两侧 show ip vrrp statistics——初始 6870-A 双 Master、6860-B 双 Backup（同优先级取最低 router ID）（p387-388）。
    5. 终端验证：Client 5（192.168.20.105，网关改 192.168.20.254）与 Client 9（192.168.30.109，网关 192.168.30.254）→ Client 5 ping Client 9 → Client 5 上 ip neigh show 看 192.168.20.254 对应 VRRP 虚拟 MAC → 持续 ping 192.168.20.254 → 6870-A write memory 后 reload from working → 6860-B show ip vrrp statistics 变双 Master（接管）（p388-389）。
    6. 指定主备与负载分担：6870-A disable VRID 1 → priority 150 → enable（VLAN 20 主）；6860-B disable VRID 2 → priority 150 → enable（VLAN 30 主）→ 两侧 show ip vrrp statistics 交叉确认 Master/Backup（p390）。
  verification: |
    p387 虚拟 MAC 出现在终端 ARP；p389 主机重启后 Backup 接管（Become Master 计数 1）；p390 优先级 150 的实例成为对应 VLAN Master。
  conditions: 实验口径：改优先级前必须 disable 实例（p390 Warning）；MAC 表为空时先从客户端 ping 网关造流量（p388 Tips）。
  tags: [lab, vrrp, gateway, redundancy]

- id: c12
  title: QoS 实验——端口默认标记、信任口、策略三件套、限速与 Tri-Color 验证
  type: lab
  source_pages: p421-428
  source_chapter: Quality of Service (QoS)
  source_quote: |
    "Before beginning, reset all the QoS parameters back to default (6360-A): qos flush ... qos apply ... show qos config ... Phones = trusted" (p422)；
    "sw5 (6360-A) -> qos port 1/1/1 default 802.1p 7 ... 1/1/1 Yes No 7/ 0 DSCP 1G" (p423)；
    "sw5 (6360-A) -> policy condition client_traffic source vlan 20 ... policy action priority_5 802.1p 5 ... policy rule rule1 condition client_traffic action priority_5 ... show active policy rule ... Green Packets = 6982" (p425-426)
  steps: |
    1. 清场：qos flush → qos apply → show qos config 核对默认（Trust ports=no、Phones=trusted 等）（p422）。
    2. 端口默认标记：show qos port 1/1/1（默认 0/0）→ qos port 1/1/1 default 802.1p 7 → show 核对 Default P/DSCP=7/0；理解不信任口对 untagged/tagged 流量的改写语义（p423）。
    3. 信任口：qos port 1/1/1 trusted → qos apply → show qos port 1/1/1（Trust 列 +Yes、DEI Map=Yes）（p424）。
    4. 802.1p 映射策略：policy condition Traffic 802.1p 4 → policy action SetBits 802.1p 7 → policy rule 802.1p_rule condition Traffic action SetBits → qos apply → show policy condition/action/rule 三查（p424）。
    5. VLAN 优先级策略：policy condition client_traffic source vlan 20 → policy action priority_5 802.1p 5 → policy rule rule1 condition client_traffic action priority_5 → show active policy rule（未 apply 前 rule1 不在）→ qos apply → show active policy rule 出现 rule1 且有 Packets/Bytes 计数（p425）。
    6. 限速与 Tri-Color：policy action priority_5 maximum bandwidth 100k → qos apply → Client 5（VLAN 20）小包 ping（正常，Green 计数涨）→ ping -s 65000 大包（Red Packets 出现，超带宽丢弃）→ policy action priority_5 no maximum bandwidth 恢复（p425-426）。
    7. 优先级与开关：policy rule rule1 precedence 1000 ...；policy rule rule1 disable → qos apply → show active policy rule 消失；全部清理 no policy rule/action/condition ×组 → qos apply → show policy rule "No pending rules"（p426-428）。
    8. 技巧：调试期对规则开 log（policy rule rule1 log）→ show qos log 查看（p428）。
  verification: |
    p423 端口默认值 7/0 生效；p425 qos apply 前后 active rule 差异；p426 大包 ping 出现 Red Packets=148（实验值，实验口径）。
  conditions: 实验口径：仅覆盖 QoS 概览，条件组合全表见 Network Configuration Guide（p422 Notes）。
  tags: [lab, qos, policy, marking, policing]

- id: c13
  title: ACL 前置配置实验——四台交换机与 Client 1 基线
  type: lab
  source_pages: p445-446
  source_chapter: Prior Configuration — "Set up a network topology"
  source_quote: |
    "sw5 (OS6360-A) -> ip interface Loopback0 address 192.168.254.5 ... ip interface int_57 address 192.168.57.5/24 vlan 57 ... ip static-route 0.0.0.0/0 gateway 192.168.57.7 metric 1 ... gateway 192.168.57.8 metric 2" (p446)；
    "sw7 (6870-A) -> ip route-map 'staticIntoOspf' sequence-number 10 action permit ... ip redist static into ospf route-map 'staticIntoOspf' admin-state enable" (p446)
  steps: |
    1. 6360-A：Loopback0 192.168.254.5、int_57 192.168.57.5/24 vlan 57、默认路由主备（网关 .7 metric 1 / .8 metric 2）。
    2. 6870-A：int_57 192.168.57.7/24 vlan 57；route-map localIntoOspf（match 192.168.57.0/24 permit）；静态路由 192.168.254.5/32 → 192.168.57.5；route-map staticIntoOspf permit + redist static into ospf 启用。
    3. 6860-B：int_57 192.168.57.8/24 vlan 57；route-map localIntoOspf（match 192.168.57.0/24）；静态路由 192.168.254.5/32 → 192.168.57.5。
    4. 6900-A：vlan 110 + port 1/1/1 untagged + enable；int_110 192.168.110.1/24 vlan 110；route-map localIntoOspf（match 192.168.110.0/24）。
    5. Client 1（下一实验用）：IP 192.168.110.51/24 网关 192.168.110.1 DNS 10.0.0.51。
  verification: |
    后续 ACL 实验依赖该拓扑：Client 5 → 数据库服务器 192.168.110.51 的 ICMP/HTTP/FTP 过滤均经此路由路径（p449-452）。
  conditions: 实验口径；route-map/redist 仅按教材给的最小配置。
  tags: [lab, prior-configuration, routing, ospf]

- id: c14
  title: ACL 实验——L2 过滤、ICMP 过滤、HTTP/FTP 分组过滤、UserPorts 与 BPDU 防护
  type: lab
  source_pages: p447-453
  source_chapter: Access Control Lists (ACLs)
  source_quote: |
    "sw5 (6360-A) -> qos reset ... qos flush ... qos apply ... policy condition cond1 source mac <Client 5 MAC address> ... policy action DenyTraffic disposition deny ... policy rule Filter1 ... qos apply ­ Is the ping still working?" (p449)；
    "policy condition ftpfromvlan20 source vlan 20 destination ip-port 20-21 ip-protocol 6 ... policy rule deny_ftp_employee condition ftpfromvlan20 action deny precedence 65535" (p450)；
    "policy service http1 destination ip-port 80 protocol 6 ... policy service group http from cli http1 http2 http3 http4 http5 ... policy condition httpfromvlan30 source vlan 30 destination ip any service group http" (p452)
  steps: |
    1. 取信息：show mac-learning port 1/1/1 与 1/1/2 记录 Client 5/9 的 MAC（每 POD 不同，p448）。
    2. L2 过滤：qos reset/flush/apply 清场 → Client 5 持续 ping 网关 192.168.20.254 → policy condition cond1 source mac <MAC> → action DenyTraffic disposition deny → rule Filter1 → qos apply → ping 断？→ qos flush/reset/apply 恢复默认放行（p449）。
    3. ICMP 过滤：Client 5 持续 ping 数据库服务器 192.168.110.51 → policy condition icmpCondition source mac <MAC> ip-protocol 1 destination ip 192.168.110.51 → action deny → rule icmpRule → qos apply → ping 断（p449）。
    4. FTP 过滤（员工禁 FTP）：先两客户端用 FileZilla 验证 FTP 192.168.100.102 可用 → policy condition ftpfromvlan20 source vlan 20 destination ip-port 20-21 ip-protocol 6 → action deny → rule deny_ftp_employee precedence 65535 → qos apply → Client 5 FTP 失败、Client 9 正常（p450-451）。
    5. HTTP 过滤（承包商禁 HTTP）：先浏览器验证两客户端可开 https://www.al-enterprise.com → 建 5 个 policy service（80/8080/8000/443/4343, protocol 6）→ policy service group http from cli 五者 → condition httpfromvlan30 source vlan 30 destination ip any service group http → action deny → rule deny_http_contractor precedence 65535 → qos apply → Client 9 失败、Client 5 正常（p452）。
    6. 用户口安全：policy port group Userports 1/1/1-2（防 IP 欺骗，仅路由流量生效）→ qos user-port shutdown bpdu（用户口收到 STP 帧即关口防环路）（p453）。
  verification: |
    p449 ping 断/恢复；p451 Client 5 FTP 失败 + Client 9 正常（截图）；p452 Client 9 HTTP 失败 + Client 5 正常。
  conditions: 实验口径：员工=VLAN 20、承包商=VLAN 30；precedence 65535 作兜底规则。
  tags: [lab, acl, filtering, userports]

- id: c15
  title: Access Guardian 实验——RADIUS 声明、UNP 档案、802.1x 认证与 MAC Block 验证
  type: lab
  source_pages: p476-485
  source_chapter: Access Guardian — "Configure the Access Guardian on OmniSwitch"
  source_quote: |
    "sw5 (6360-A) -> aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent ... aaa device-authentication 802.1x my_radius ... aaa accounting 802.1x my_radius ... ip service source-ip Loopback0 radius" (p479)；
    "sw5 (6360-A) -> policy list deny_employees type unp enable ... policy list deny_employees rules deny_ftp_employee ... unp profile UNP-employee qos-policy-list deny_employees ... unp profile UNP-employee map vlan 20" (p479-480)；
    "-> aaa test-radius-server my_radius type authentication user employee password password ... Filter-ID = UNP-employee" (p481)
  steps: |
    1. 声明 RADIUS：aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent → aaa device-authentication 802.1x/mac my_radius → aaa accounting 802.1x/mac my_radius → ip service source-ip Loopback0 radius（p479）。
    2. 重建策略（脱离全局生效、改为按用户档案生效）：qos flush/apply 清掉 ACL 实验的全局规则 → 重建 deny_ftp_employee（条件 NoFtp 目的 20-21/ip-protocol 6，动作 deny，no default-list）与 deny_http_contractor（目的 80/ip-protocol 6）→ qos apply（p479）。
    3. 建策略列表：policy list deny_employees type unp enable → rules deny_ftp_employee；deny_contractors → rules deny_http_contractor → qos apply（p479-480）。
    4. 建 UNP 档案：unp profile UNP-employee / UNP-contractor → 各自 qos-policy-list 与 map vlan（20/30）；show unp profile UNP-contractor 与 show unp profile map vlan 核对（p480）。
    5. 配用户口：unp port 1/1/1 port-type bridge → 802.1x-authentication → mac-authentication（p480）。
    6. 测 RADIUS：aaa test-radius-server my_radius type authentication user employee password password → 返回 Filter-ID=UNP-employee（p481）。
    7. employee 验证：Client 5 网卡开 802.1X（PEAP + 免 CA + MSCHAPv2，用户 employee/password）→ unp user flush port 1/1/1 → 客户端断连重连 → show unp user（VLAN 20/UNP-employee/Active）、show unp user status（Source=Radius/Authenticated）、show unp user details（Profile From Auth Server=UNP-employee、Role=deny_employees）（p481-482）。
    8. contractor 验证：改凭据 contractor/password → flush + 重连 → show unp user（VLAN 30/UNP-contractor/Active）（p483-484）。
    9. MAC Block 验证：Client 5 关闭 802.1x → flush + 重连 → show unp user 显示用户名=MAC、Profile=-、Status=Block（服务器无该 MAC 登记）（p485）。
    10. 清理：no unp port 1/1/1 → write memory flash-synchro（p485）。
  verification: |
    p481 RADIUS 测试返回 Filter-ID；p482/p484 两用户分别落入 VLAN 20/30 且 Role 生效；p485 无登记 MAC 被阻断。
  conditions: 实验口径：RADIUS 服务器即 AAA Training Server 192.168.100.102；employee/contractor 密码均 password。
  tags: [lab, access-guardian, unp, 8021x, radius]

- id: c16
  title: LLDP 实验——通知使能、TLV 管理、远端系统信息丰富化
  type: lab
  source_pages: p501-505
  source_chapter: Link Layer Discovery Protocol
  source_quote: |
    "sw5 (6360-A) -> lldp port 1/1/3 notification enable ...（三台交换机全部互联口）" (p502)；
    "Tips LLDP is configured at port level (or NI or chassis), but not at linkagg level." (p502)；
    "all -> lldp chassis tlv management system-name enable ... system-description enable ... system-capabilities enable ... management-address enable ... Management IP Address = 192.168.254.7" (p505)
  steps: |
    1. 使能通知：三台交换机对全部互联口 lldp port <口> notification enable（6360 VC 四口、6870-A 四口、6860-B 四口）（p502）。
    2. 使能管理 TLV：三台对各互联口 lldp port <口> tlv management port-description enable（p503）。
    3. 验证统计：6870-A show lldp statistics（各口 Tx/Rx 计数、零错误）（p503）。
    4. 查远端系统：6360-A show lldp remote-system（对端 Chassis/Port、Capabilities Bridge Router；此时 System Name 仍为 (null)）（p503-504）。
    5. 本机信息：6870-A show lldp local-system（系统名 Pod20sw7、版本、发送间隔 30 秒/TTL 倍乘 4 等参数、管理地址）（p504）。
    6. 丰富化：三台 lldp chassis tlv management system-name/system-description/system-capabilities/management-address enable → 再次 show lldp remote-system——System Name（Pod20sw7/sw8）、System Description（型号与版本）、Management IP Address 出现（p505）。
  verification: |
    p503 统计表 Tx/Rx 正常增长零错误；p505 前后对比：远端系统名/描述/管理 IP 由 null 变为实际值。
  conditions: 实验口径：LLDP 默认收发双开，无需显式开启（p502 Notes）。
  tags: [lab, lldp, discovery]

- id: c17
  title: Lightning Config 操作序列——笔记本 DHCP、登录、必配项、改密、保存认证、模板导入
  type: howto
  source_pages: p110-121
  source_chapter: Using OmniSwitch Lightning Configuration（讲义内嵌操作步骤）
  source_quote: |
    "For Windows: 1. Open the Control Panel. 2. Select Network and Sharing Center. ... Ensure Obtain an IP address automatically ... selected" (p112)；
    "• Power on the ALE switch • Wait for approximately 3 minutes ... • Enter https://192.168.0.1/ • You must use https • Click on Advanced" (p113)；
    "Click IMPORT • Select the template supplied to you by the solution architect • Templates end in .json ... Click Lightning Config • Complete the required information • Click SAVE CONFIGURATION" (p120-121)
  steps: |
    1. 准备（禁令清单，p108）：不要预接线到网络/其他交换机、不要先接摄像头等外设、不要接 DHCP 服务器、笔记本就绪再上电；笔记本设 DHCP 客户端（Windows: 控制面板 → 网络和共享中心 → 更改适配器设置 → 属性 → 自动获得 IP/DNS）（p112）。
    2. 连接：网线接交换机端口 1（唯一连线）→ 上电等约 3 分钟 → 核对两侧绿灯（p113）。
    3. 登录：Chrome 开 https://192.168.0.1/（必须 https）→ Advanced → Proceed to 192.168.0.1 (unsafe) 接受自签名证书 → admin/switch 登录（笔记本此时已被分到 192.168.0.200/24）（p113-114）。
    4. 最小配置：点 RECOMMENDED DEFAULTS → LIGHTNING CONFIG → 填必填项（IP/掩码/网关，全网唯一；不懂就停，p115）。
    5. 应用并改密：YES 应用 → 立即改 admin 密码（≥8 位，含大写/小写/数字/特殊字符，避开 ! 与 $）→ 保存（p116）。
    6. 保存认证：Yes（保留 working 开关开）→ 等待绿色成功提示（数分钟）→ 回主页（p117）。
    7. 主页巡检：Quick Links 常用配置、搜索功能、下方 PoE 信息（PoE Port Configuration 看 Power mW 列确认受电设备已启动）；纪律——任何改动后 ALWAYS Write Memory、正确退出 Certified Mode（p118-119）。
    8. 模板复用（可选）：IMPORT → 选架构师提供的 .json 模板 → Open → Lightning Config 补必填项（IP 全网唯一）→ SAVE CONFIGURATION → YES → 按常规流程走完（p120-121）。
  verification: |
    p117 保存完成后绿色成功消息；p119 PoE 端口 Power (mW) 列显示各受电设备功率；后续接边缘设备与其他已配置 ALE 交换机（p117）。
  conditions: 禁止连接未开局的出箱交换机到网络或其他交换机（p108/p117）；每台交换机逐一执行。
  tags: [howto, lightning-config, onboarding, template]

- id: c18
  title: OST 2.0 安装实验——Postgres、Server、Config Tool、Client 接入与添加交换机
  type: lab
  source_pages: p572-580
  source_chapter: OmniVista Smart Tool Installation Guide
  source_quote: |
    "Minimum version 10, 11 ... Version 18.1 is tested. ... Run the setup on your server: postgresql-18.1-2-windows-x64.exe" (p573)；
    "After installing Postgres database and OmniSwitch Smart Tool Server, the user MUST run the Server Configuration Tool to perform initial setup" (p576)；
    "Run OmniVistaSmartTool.ServerConfig.exe (C:\Program Files\Alcatel-Lucent Enterprise\Tools\Server Configuration Wizard) ... Provide the password previously defined during PostgresSQL installation ­ Test the connection with the PostgresSQL Database ... Define a password for OST admin" (p577-578)
  steps: |
    1. 前置：Windows 10/11；从 postgresql.org/download 取 Windows x86-64 版（测试版本 18.1）（p573）。
    2. 装 Postgres：运行 postgresql-18.1-2-windows-x64.exe → 设数据库访问密码、保留默认端口 → 取消 Stack Builder → Finish（p573-575）。
    3. 装 OST 2.0：Server（默认与 Client 同机，且必须装在 Postgres 所在服务器）+ Client（p576）。
    4. Server 初始化：运行 OmniVistaSmartTool.ServerConfig.exe（C:\Program Files\Alcatel-Lucent Enterprise\Tools\Server Configuration Wizard）→ 填 Postgres 密码 → Test the connection → 定义 OST admin 密码（p577-578）。
    5. Client 连接：启动 OmniVista Smart Tool Client 连接 Server（p578-579）。
    6. 添加交换机：Client 内 Add a switch（p579-580）。
  verification: |
    p577 数据库连接测试通过；p578 OST admin 密码设定完成；p579-580 Client 登录成功并出现交换机。
  conditions: Postgres 必须先于 OST Server 安装；Server 与 Postgres 同机（p573/p576）。
  tags: [lab, ost, installation, postgres]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 26 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 远程实验室接入 | 无独立 How-To 章（p12-51 为操作讲义），操作细节已并入 c01 前置与 BOOK_OVERVIEW 骨架 1，不入册为实验（教学基础设施）。 |
| task-02 多方式登录 | 有 → c01（SSH 测试 + WebView 登录；console/EMP 为讲义无实验）。 |
| task-03 用户与认证服务器 | 无独立实验章（p70-74 讲义；Access Guardian 实验复用 RADIUS 声明，见 c15 步骤 1）。 |
| task-04 加固管理面 | 无实验章（p77-89 纯讲义清单）。 |
| task-05 WebView 管理 | 有 → c01（步骤 5-10：会话参数/写内存/可视化/建删 VLAN）。 |
| task-06 Lightning Config | 有 → c17（讲义级操作序列，非独立 How-To 章）。 |
| task-07 配置生命周期 | 有 → c02 |
| task-08 Virtual Chassis | 有 → c03 |
| task-09 VLAN 与 802.1Q | 有 → c04（VLAN/UNP）、c07（802.1Q） |
| task-10 VLAN 间路由与 IP 接口 | 有 → c04 步骤 2-6（IP 接口与路由验证）、c10（DHCP Relay 核查路由）；静态路由/Loopback0 配置于 c13。 |
| task-11 OST 使用 | 无独立使用实验（p215-231 为功能讲义）；安装实验见 c18。 |
| task-12 诊断八件套 | 有 → c05 |
| task-13 链路聚合 | 有 → c06 |
| task-14 STP | 有 → c08 |
| task-15 DHL | 有 → c09 |
| task-16 DHCP Client/Relay | 有 → c10 |
| task-17 VRRP | 有 → c11 |
| task-18 QoS | 有 → c12 |
| task-19 ACL 与用户口 | 有 → c13（前置）、c14（ACL 主体） |
| task-20 Access Guardian | 有 → c15 |
| task-21 LLDP | 有 → c16 |
| task-22 PoE | 无实验章（p506-521 纯讲义；OST 的 PoE 向导属工具，见 c18 关联）。 |
| task-23 软件升级 | 无实验（p529-535 明言"不覆盖升级步骤"，指向 Release Notes）。 |
| task-24 Auto-Fabric | 无实验（p536-554 纯讲义）。 |
| task-25 Fleet Supervision | 无实验（p555-569 为控制台操作截图讲义）。 |
| task-26 OST 2.0 安装 | 有 → c18 |

**统计**：18 条（lab 16 条 + howto 1 条 + lab 型前置配置 1 条）；26 项任务中 15 项有案例类条目直接覆盖，11 项为纯讲义/环境/外部文档内容（task-01/03/04/11/22/23/24/25 及 task-06 的实验属性说明、task-08 已覆盖）。课程结构特点：Agenda 中的模块几乎全部配有 How-To 实验，仅 PoE、升级、Auto-Fabric、Fleet Supervision 四个附加模块纯讲义。
