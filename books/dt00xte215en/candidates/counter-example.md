# 反例/限制/边界/易错点候选 — OmniSwitch LAN Access Switching (DT00XTE215EN Ed23)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 出厂默认口令 admin/switch 与强制改密版本线——存量升级最易漏
  type: version-trap
  source_pages: p70, p71
  source_chapter: SWITCH USER ACCOUNT / PASSWORD FOR ADMIN
  source_quote: |
    p70: "** Default login name and password Login : admin Password : switch ... * Up to 64 users can be configured in the local switch database"
    p71: "From 8.10R03 a warning message will be displayed urging for the default password to be changed ... In 8.10R4 changing the default password is mandatory. • From 8.10R04 it is mandatory to change the password at first login"
  summary: |
    出厂默认登录 admin/switch，本地库仅两用户（admin/default）、上限 64 个。版本线三段：8.10R03 只警告、8.10R4 强制改默认密码、8.10R04 强制首登改密。
    升级存量设备（尤其低于 8.10R3 的）后不要以为系统会替你堵住默认口令——升级不等于改密，必须逐一核查。
  conditions: 所有 OmniSwitch 登录治理场景
  tags: [version-trap, users, security]

- id: n02
  title: 禁用 console 前想清楚——全部管理通道同失即 RMA
  type: warning
  source_pages: p77
  source_chapter: SECURING CONSOLE PORT ACCESS
  source_quote: |
    "In case you disable console access, and you lose all other means of management access (SSH, HTTPS, SNMP …), you won't be able to manage anymore your switch ! (RMA necessary in this case)"
  summary: |
    aaa session console disable 会整体关闭 console 登录。若同时丢失 SSH/HTTPS/SNMP 等全部远程通道，设备只能返厂（RMA）。
    收紧管理面前先确认至少两条独立可用通道；ASA 限源地址表要包含运维网段。
  conditions: 管理面加固变更前
  tags: [warning, console, hardening]

- id: n03
  title: Lightning Config 六条禁令——禁止预接线、先接外设、接 DHCP 服务器
  type: warning
  source_pages: p108
  source_chapter: LIGHTNING CONFIG: PREPARE FOR INSTALL (READ THIS FIRST)
  source_quote: |
    "• Do not pre-cable the ALE switch to the network. • Do not connect the ALE switch to any other switch. • Do not connect cameras or other devices to the switch before setup. • Wait to power up the ALE switch until the laptop is ready. • Do not connect the ALE switch to a DHCP server."
    "• If you don't understand IP addressing, Subnet Masks, and/or Default Gateways please stop and contact the solution architect that designed the network"
  summary: |
    开局前硬禁令：不预接线进网、不与其他交换机互联、不上电前接外设、不接 DHCP 服务器；上电前笔记本就绪；不懂 IP 编址就停下来找方案架构师。
    违反任意一条都可能让开局向导走偏（端口 1 DHCP 冲突、误入生产网络）。
  conditions: Lightning Config 开局全流程
  tags: [warning, lightning-config]

- id: n04
  title: Lightning Config 必做项——Recommended Defaults 不可跳过、IP 必须全网唯一
  type: warning
  source_pages: p115
  source_chapter: LIGHTNING CONFIG: MINIMUM VIABLE CONFIGURATION
  source_quote: |
    "1.Click on RECOMMENDED DEFAULTS 2.Click on LIGHTNING CONFIG • Do NOT skip the Recommended Defaults! ... • Every IP Address must be unique on the same network! • Get help if you are unsure about IP, Subnet, or Gateway settings"
  summary: |
    两点纪律：Recommended Defaults 步骤不可跳过（含基线安全与服务配置）；所有 IP 地址必须全网唯一。
    抄模板或复制他台配置时最容易把 IP 一起复制，产生地址冲突。
  conditions: Lightning Config 配置页
  tags: [warning, lightning-config]

- id: n05
  title: Lightning Config 改密规则——不得留默认密码，特殊字符避开 ! 与 $
  type: warning
  source_pages: p116
  source_chapter: LIGHTNING CONFIG: CHANGE THE ADMIN PASSWORD
  source_quote: |
    "• Do not leave the default password in place. It is not secure • The new password must meet the following requirements: • At least 8 characters • 1 uppercase letter • 1 lowercase letter • 1 digit • 1 special character (but avoid using ! or $)."
  summary: |
    开局必须改 admin 密码；密码规则为至少 8 字符含大写/小写/数字/特殊字符，且明确建议避开 ! 和 $（疑与界面解析/自动化脚本冲突，原文未解释原因——按原文执行）。
    生成密码时注意与 CLI 侧 user password-policy 的规则并行不悖。
  conditions: Lightning Config 改密页
  tags: [warning, lightning-config, password]

- id: n06
  title: 出箱交换机禁止未开局互联——"Never connect an out-of-box ALE switch"
  type: warning
  source_pages: p117, p125
  source_chapter: LIGHTNING CONFIG: SAVE ALL CHANGES / LOOP AVOIDANCE
  source_quote: |
    "• Connect edge devices. • Connect other preconfigured ALE switches. • Never connect an out-of-box ALE switch to another without running Lightning Config first."
    "If you have been given instructions to interconnect switches in a manner similar to those listed in the preceding templates, please STOP and consult with the solution architect to ensure they have implemented loop avoidance network technologies"
  summary: |
    两条互联禁令：保存配置后只能连接边缘设备与其他已配置的 ALE 交换机，未做 Lightning Config 的出箱交换机严禁先互联；示例拓扑本身含物理环路，照图接线前必须确认环路避免技术（STP/DHL 等）已实施，否则停下来找架构师。
    两条都指向同一后果：无防护环路会拖垮全网。
  conditions: 新交换机组网与拓扑施工
  tags: [warning, lightning-config, loop]

- id: n07
  title: Lightning Config 纪律——每次改动必须 Write Memory、正确退出 Certified Mode
  type: warning
  source_pages: p118
  source_chapter: LIGHTNING CONFIG: DISCOVER THE HOME PAGE
  source_quote: |
    "Important Reminders: • ALWAYS Write Memory after making any changes—this step is critical to avoid losing unsaved configurations. • Learn to Exit Certified Mode properly to avoid issues caused by unsaved changes."
  summary: |
    图形界面改完不等于保存：必须 Write Memory，否则丢失未保存配置；退出 Certified Mode 也要按正确流程（有未保存改动时退出会引发问题）。
    该纪律与 CLI 侧 write memory 语义一致，只是 Lightning Config 界面更让人误以为"点点就保存了"。
  conditions: Lightning Config 日常使用
  tags: [warning, lightning-config, write-memory]

- id: n08
  title: reload all 永远从 certified 启动——"回滚按钮"也会吃掉 working 里的新配置
  type: warning
  source_pages: p142
  source_chapter: Booting behavior in Release 8
  source_quote: |
    "IF THE OMNISWITCH IS REBOOTED WITH THE 'RELOAD ALL' COMMAND, IT WILL REBOOT FROM THE CERTIFIED DIRECTORY, NO MATTER WHAT THE CONTENT OF THE RUNNING DIRECTORY IS (SAME/DIFFERENT THAN THE CERTIFIED DIRECTORY CONTENT)"
  summary: |
    reload all 是无条件回 certified 的强制回滚：即使 working 与 certified 内容相同也回 certified 启动。
    把 reload all 当普通重启用，会在无意间触发回滚行为；普通重启（冷启动）才按"内容相同回 running"规则。
  conditions: 重启/回滚操作
  tags: [warning, rollback, reload]

- id: n09
  title: 未保存改动重启即丢——NOT SYNCHRONIZED 状态是红色警报
  type: warning
  source_pages: p143, p144
  source_chapter: Synchronizing RAM and Running Directory / Saving the Running Configuration
  source_quote: |
    "IF THE OMNISWITCH IS REBOOTED NOW ... ALL THE CHANGES IN THE RUNNING CONFIGURATION WILL BE OVERWRITTEN ... IN OUR CASE, VLAN 2, 3 AND 99 WILL BE LOST, AS THEY ARE NOW STORED IN THE RUNNING CONFIGURATION." (p143)
    "IF THE OMNISWITCH IS REBOOTED NOW (VIA A COMMAND RELOAD ALL OR IF POWER TO THE OMNISWITCH IS INTERRUPTED), THE OMNISWITCH WILL BOOT FROM THE CERTIFIED DIRECTORY ... HOWEVER, SINCE THE CONFIGURATION FILE WAS SAVED TO THE WORKING DIRECTORY, THAT FILE IS STILL IN THE WORKING DIRECTORY AND CAN BE RETRIEVED." (p144)
  summary: |
    两段实验警示：①write memory 前（NOT SYNCHRONIZED）断电/重启，RAM 改动（实验中的 VLAN 2/3/99）全部丢失；②write memory 后但未认证（CERTIFY NEEDED）时断电，会从 certified 启动，但 working 里的配置文件仍在、可经 reload from working 取回。
    排障"重启后配置没了"先看 show running-directory 三字段：是没保存、还是保存了没认证。
  conditions: 配置变更与重启生命周期
  tags: [warning, rollback, write-memory]

- id: n10
  title: certified 模式只读——write memory 直接报错
  type: limitation
  source_pages: p135, p142, p145
  source_chapter: AOS MANAGING FILES/DIRECTORIES / How-To
  source_quote: |
    p135: "When the switch boots from the CERTIFIED directory, changes made to the switch cannot be saved and files cannot be moved between directories."
    p145: "ERROR: Write memory is not permitted when switch is running in certified mode"
  summary: |
    从 certified 目录运行时：配置改动只在 RAM 生效、无法保存到任何目录、也不能在目录间移动文件（write memory 报错）。
    见到该报错先 show running-directory 确认启动目录，再 reload from working 取回正确目录。
  conditions: 误从 certified 启动后
  tags: [limitation, certified, rollback]

- id: n11
  title: cp 复制目录时 boot.md5 报 permission denied——可忽略；copy running certified 前必须验证
  type: limitation
  source_pages: p146
  source_chapter: Creating a User-Defined Directory
  source_quote: |
    "sw3 (6560-A) -> cp working/*.* lab ... cp: can't open 'working/boot.md5': Permission denied ... Tips The lab directory may have been already created, ignore error and proceed on. During the copy; it tries to copy the boot.md5 file but a 'permission denied' message is displayed. This file is auto generated so ignore this error and proceed"
    "Notes The copy running certified command should only be done if the running configuration has been verified."
  summary: |
    两个易慌点：①用户目录复制时报 boot.md5 permission denied 属正常（该文件自动生成），lab 目录已存在同理忽略；②copy running certified 会把当前运行配置固化为全网回滚基线——执行前必须确认配置验证无误，否则错误的配置一旦 certified，回滚点就被污染。
  conditions: 用户目录操作与认证动作
  tags: [limitation, directories, certified]

- id: n12
  title: USB 拔出前必须 usb disable
  type: warning
  source_pages: p148
  source_chapter: Annex: USB Backup & Restore
  source_quote: |
    "+++ CAUTION: Do usb disable before removing usb WARNING: CAUTION: Do usb disable before removing usb"
  summary: |
    直插 U 盘（usb enable 挂载 /uflash）后拔出前必须先 usb disable 卸载，否则可能损坏文件系统或丢备份。
    注意 R-Lab 的 USB 口被 USB-to-Eth dongle 占用，USB 备份实验无法在远端实验室演示（p148）。
  conditions: USB 备份/恢复操作
  tags: [warning, usb, backup]

- id: n13
  title: VC 中改 chassis-id 后 write memory 会警告清除"缺失 chassis"配置
  type: warning
  source_pages: p176
  source_chapter: Virtual Chassis-6360 (How-To)
  source_quote: |
    "sw6 (6360-B) -> write memory ... WARNING - Virtual chassis topology change detected. Chassis 1 missing! Configuration associated with missing chassis will be erased permanently! Confirm to continue  (Y/N) : y ... The command write memory is protected by issuing a warning to prevent or warn purging the configuration of the elements that are missing."
  summary: |
    在单机改 chassis-id 后保存，VC 管理器把"原 chassis 1"视为缺失成员并警告将永久清除其关联配置，需确认 y 继续。
    这是设计行为而非故障：改 ID 即拓扑变化。但盲目确认会清掉 VC 成员配置，组网中途要清楚自己确认的是什么。
  conditions: VC 成员 ID 变更时的保存动作
  tags: [warning, virtual-chassis]

- id: n14
  title: VC 优先级与 chassis-id 改动必须 reload 才生效
  type: limitation
  source_pages: p175, p176
  source_chapter: Virtual Chassis-6360 (How-To)
  source_quote: |
    "Notes A reload is mandatory to consider the chassis priority" (p175)
    "Notes A reload is mandatory to take into account the new chassis-id" (p176)
  summary: |
    configured-chassis-priority 与 configured-chassis-id 都要在 reload 后才生效（书中两处 Notes 重复强调）。
    配置完 show 输出仍是旧值属预期，别当成命令失败；排产时要算上每次约 4-5 分钟的重启窗口（实验口径）。
  conditions: VC 选举参数变更
  tags: [limitation, virtual-chassis, reload]

- id: n15
  title: VLAN 1 不可删除，只能禁用（三处口径一致）
  type: limitation
  source_pages: p185, p205, p213
  source_chapter: VLAN MANAGEMENT / VLANs (How-To)
  source_quote: |
    p205: "In its untagged configuration, the switch has only one VLAN, the VLAN 1. This is the default VLAN and all ports are initially associated with it. This VLAN CANNOT be deleted, but it can be disabled if desired."
    p213: "VLAN 1 cannot be deleted. It is only possible to deactivate."
    p185: "Ports become members of VLANs by • Static Configuration • Mobility/with or without Authentication * • 802.1q"
  summary: |
    默认 VLAN 1 无法删除，只能 admin-state disable；no vlan 1 会失败。
    出于安全要弃用 VLAN 1 的做法是禁用 + 把聚合/上行的默认 VLAN 换成业务 VLAN（实验用 VLAN 57/58），而非删除。
  conditions: 一切 VLAN 规划
  tags: [limitation, vlan]

- id: n16
  title: VLAN 无活动成员则 IP 接口 DOWN 且不进路由——"接口 DOWN"三连问
  type: limitation
  source_pages: p207, p209, p293
  source_chapter: VLANs (How-To) / 802.1q (How-To)
  source_quote: |
    p207: "If Status = DOWN, it indicates no active ports or devices have been associated with the VLAN ... If an IP interface is DOWN, it cannot be connected to, will not reply to PING requests nor will it be advertised in any router updates. This will not affect the Layer 2 broadcast domain, however."
    p209: "Why the status of the IP interface int_50 is DOWN?"
    p293: "The IP interfaces status is DOWN. Why? ... if there are no members of a VLAN the IP interface is not only down but will not be advertised to the Layer 3."
  summary: |
    三处重复出现同一坑：IP 接口 DOWN 的首要原因是 VLAN 没有活动成员端口（inactive）。此时接口不回 PING、不被路由协议通告，但二层广播域不受影响。
    新建 VLAN + 网关后必须 enable 至少一个成员口（或确认对端已连接），网关才会 UP。
  conditions: VLAN/网关新建后验证
  tags: [limitation, vlan, routing]

- id: n17
  title: 物理端口永远保留一个默认 VLAN 做二层桥接——802.1Q 不是"纯 trunk"
  type: rule
  source_pages: p292, p295
  source_chapter: 802.1q (How-To)
  source_quote: |
    "In an IEEE 802.1Q environment, the Default VLAN for the port is bridged, and all the other VLANs will have the IEEE 802.1Q tag inserted for proper VLAN association at the remote side." (p292)
    "A PHYSICAL PORT ALWAYS HAS 1 VLAN (THE DEFAULT VLAN FOR THE PORT) THAT BRIDGES TRAFFIC (LEVEL 2)" (p295)
  summary: |
    OmniSwitch 口径：交换机间链路上，端口默认 VLAN 以未打标方式桥接，其余 VLAN 打 802.1Q tag 共链承载——不存在"全部打标"的模式（与某些厂商 trunk 口径不同）。
    安全上要避免默认 VLAN 1 过 trunk，就用业务 VLAN（如 VLAN 57/58）作为链路默认 VLAN（实验正是这么做的）。
  conditions: 交换机互联链路设计
  tags: [rule, 8021q, vlan]

- id: n18
  title: STP 端口状态取决于根桥选举——实验结果"每 POD 不同"
  type: limitation
  source_pages: p294, p316
  source_chapter: 802.1q / STP (How-To)
  source_quote: |
    p294: "Notes The ports status available in the tables below depend on the STP root bridge election. Could be different on your pod."
    p316: "By default, the bridge priority is 32768 (0x8000). Since all priorities are identical by default, the switch with the lowest MAC address is selected as the root bridge (in this example, the 6870-A has the lowest MAC address)."
  summary: |
    教材明示：show vlan members 里 tagged 口显示 forwarding 还是 blocking，随 STP 根桥选举而异，"你的 POD 可能不同"。
    网络里默认根桥由最小 MAC 决定——这是"谁的交换机最旧/最小 MAC 谁当根"的经典事故源，生产必须显式指定根桥优先级。
  conditions: STP 观察与排障
  tags: [limitation, stp, root-bridge]

- id: n19
  title: 同一链路只有一侧 blocking——对称双 blocking 是异常
  type: rule
  source_pages: p317
  source_chapter: STP (How-To)
  source_quote: |
    "Also, notice that only one side of the link(s) has a port or link aggregation with the status BLK (blocking). This ensures the neighbor(s) are still able to initiate a topology change in the event of a failure."
  summary: |
    正常 STP 状态：每条互联链路只有一侧端口为 BLK（ALT），对侧保持 forwarding——这样邻居才能在故障时发起拓扑变更。
    排障口径：看到两侧同时 blocking 属异常；检查根桥与路径成本配置。
  conditions: STP 状态核查
  tags: [rule, stp]

- id: n20
  title: 任何物理变更都触发 STP 重收敛
  type: limitation
  source_pages: p319
  source_chapter: STP (How-To)
  source_quote: |
    "Tips Remember that anytime there is a physical change, the STP will make the network infrastructure re-converge."
  summary: |
    插拔线、关开局口、聚合成员变化都会引发全网 STP 重收敛（Topology Changes 计数上涨、Age 重置）。
    生产变更窗口要预估收敛期流量抖动；RSTP 收敛 <1 秒但 Topology Change 仍会泛洪刷新 MAC 表。
  conditions: STP 网络变更
  tags: [limitation, stp, change-management]

- id: n21
  title: DHL 端口自动禁用 STP——DHL 与 STP 不能混用于同一链路
  type: limitation
  source_pages: p341
  source_chapter: Dual Home Link Active-Active (How-To)
  source_quote: |
    "Notes Spanning Tree is disabled on all the DHL enabled ports"
  summary: |
    DHL 会话启用后，linkA/linkB 端口上的 STP 被自动关闭——DHL 自己防环。
    两种方案混搭（同一接入口一部分 VLAN 走 STP 一部分走 DHL）不受支持；DHL 端口也不支持 mobile/802.1x/GVRP/UNI 口（p327），接终端的口别配 DHL。
  conditions: DHL 与 STP 方案边界
  tags: [limitation, dhl, stp]

- id: n22
  title: DHL 链路恢复后默认等 30 秒才收回 VLAN（pre-emption）
  type: limitation
  source_pages: p344
  source_chapter: Dual Home Link Active-Active (How-To)
  source_quote: |
    "It can takes a few seconds for the VLAN 20 to be forwarded back on the link aggregation 8: when the failed link comes back up, DHL waits a configurable amount of time (default: 30 secs) before the link resumes forwarding of its assigned VLAN traffic."
  summary: |
    故障链路恢复后 DHL 并不立即回切：默认 pre-emption 时间 30 秒（可配 0-600 秒）内 VLAN 仍留在存活链路。
    验收测试别把"恢复后立即回切"写进标准；频繁闪断场景调大该值可防来回摆动。
  conditions: DHL 故障恢复测试
  tags: [limitation, dhl, timer]

- id: n23
  title: 端口加入聚合前必须清掉 VLAN/其他配置——"Port cannot be added to Linkagg"
  type: limitation
  source_pages: p338
  source_chapter: Dual Home Link Active-Active (How-To) 前置
  source_quote: |
    "sw5 (6360-A) -> linkagg lacp port 2/1/3 actor admin-key 8 ... ERROR: Port cannot be added to Linkagg, please remove other configuration on this port ... Untag the vlan on this port to be able to add it to the linkagg ... no vlan 58 members port 2/1/3 ... no vlan 20 members port 2/1/3 ..."
  summary: |
    已有 VLAN 成员关系（tagged/untagged）或其它配置的端口不能直接加入聚合，须先逐一 no 掉。
    旧实验遗留的 802.1Q 打标正是本次报错来源——复用实验环境时先 show vlan members port 核对残留。
  conditions: 聚合成员端口改造
  tags: [limitation, linkagg]

- id: n24
  title: VRRP 改优先级必须先 disable 实例
  type: warning
  source_pages: p390
  source_chapter: VRRP (How-To)
  source_quote: |
    "Warning THE VRRP INSTANCE MUST BE DISABLED BEFORE CHANGING THE PRIORITY ... ip vrrp 1 interface int_20 admin-state disable ... priority 150 ... admin-state enable"
  summary: |
    运行中的 VRRP 实例直接改 priority 不被接受/不生效——必须 admin-state disable → priority → enable 三步。
    主备切换演练时注意 disable 本身即触发该实例上的主备切换，安排在窗口内做。
  conditions: VRRP 优先级调整
  tags: [warning, vrrp]

- id: n25
  title: QoS 端口信任语义——不信任口把 tagged 流量也改写为默认值
  type: limitation
  source_pages: p423
  source_chapter: Quality of Service (QoS) (How-To)
  source_quote: |
    "Any untagged traffic (traffic without any 802.1p settings) arriving on port 1/1/1 will be tagged with an 802.1p value of 7 (highest priority). ­ If the port is configured to be untrusted, any tagged traffic will be tagged with an 802.1p value of 7. ­ If the port is configured to be trusted, any tagged traffic will preserve the 802.1p value in the flow. By default, switched ports are untrusted"
  summary: |
    端口默认值配成 7 后：不信任口上 untagged 流量被打成 7，且已带 802.1p 的 tagged 流量也被改写为 7（原始标记丢失）；信任口才保留原值。
    接终端的口不信任（防用户伪造高优先级）是对的；接上游/话机交换机的口要 trusted，否则跨网段优先级被洗掉。
  conditions: QoS 边界端口设计
  tags: [limitation, qos, trust]

- id: n26
  title: qos apply 才生效——全局立即、端口与策略不立即
  type: limitation
  source_pages: p424, p425
  source_chapter: Quality of Service (QoS) (How-To)
  source_quote: |
    "the global setting is active immediately; however, modifying a port configuration requires qos apply to activate the change" (p424)
    "The rule is not active on the switch until it has been applied: ... show active policy rule（apply 前无 rule1）" (p425)
  summary: |
    QoS 的两段生效模型：全局开关类立即生效；端口配置与策略规则要 qos apply 才下发硬件，apply 前 show active policy rule 看不到。
    "配了策略没效果"第一反应查有没有 apply；配套排查命令 show qos config 的 Pending changes 字段。
  conditions: QoS/ACL 配置全程
  tags: [limitation, qos, acl]

- id: n27
  title: ACL 兜底语义——不匹配即放行（默认 accept），先写 deny 规则须想清楚默认面
  type: limitation
  source_pages: p434, p449
  source_chapter: ACL (How-To 讲义) / ACLs (How-To)
  source_quote: |
    "* By default, flows that do not match any policies are accepted on the switch" (p434)
    "sw5 (6360-A) -> policy condition cond1 source mac <Client 5 MAC address> ... policy action DenyTraffic disposition deny ... qos apply ­ Is the ping still working?" (p449)
  summary: |
    策略引擎默认放行所有不匹配流量：写一条 deny 规则只拦命中项，其余照通——这既是便利（精确打击）也是风险（以为"配了 ACL 就安全了"）。
    若要默认拒绝语义，须自行用 accept 规则 + 低 precedence 兜底 deny 组合；实验后记得 qos flush/reset 恢复，别把 deny 规则留在全网。
  conditions: ACL 设计与实验收尾
  tags: [limitation, acl]

- id: n28
  title: UserPorts 组只作用于路由流量；shutdown bpdu 防用户口环路
  type: limitation
  source_pages: p453, p440
  source_chapter: Configuring User ports Security
  source_quote: |
    "This port group does not need to be used in a condition or rule to be effective on flows and only applies to routed traffic. Ports added to the UserPorts group will block spoofed traffic while still allowing normal traffic on the port" (p453)
    "-> qos user-port shutdown bpdu ... any user access port used will be blocked if a Spanning Tree frame is received" (p453)
  summary: |
    两个边界：①UserPorts 反 IP 欺骗仅对路由（三层）流量生效，纯二层桥接流量不受其检查；②qos user-port shutdown bpdu 会让收到 STP 帧的用户口直接关闭（防私接交换机成环）——端口被关后需人工恢复，给用户排障时要先问有没有私接小交换机。
  conditions: 接入口安全
  tags: [limitation, userports, security]

- id: n29
  title: RADIUS 无 MAC 登记则 MAC 认证一律 Block
  type: limitation
  source_pages: p478, p485
  source_chapter: Access Guardian (How-To)
  source_quote: |
    p478: "Notes: @MAC Auth: as there are no MAC addresses configured on the RADIUS server, the user will be blocked from accessing the network via a MAC address authentication."
    p485: "As there are not any MAC addresses configured on the RADIUS server, then the user is blocked from accessing the network. ... 1/1/1 00:50:56:90:22:3c ... Profile - ... Status Block"
  summary: |
    端口同时启用 802.1x 与 mac-authentication 时，非客户端设备走 MAC 认证；RADIUS 没登记该 MAC 的结果是 Status=Block（Profile 为空）。
    接打印机/摄像头等哑设备的口，要么在 RADIUS 登记 MAC，要么单独放行（分类规则/默认档案），否则上线即被断网。
  conditions: Access Guardian 端口准入
  tags: [limitation, access-guardian, mac-auth]

- id: n30
  title: LLDP 不支持 linkagg 级配置；相关端口要在物理口上逐个配
  type: limitation
  source_pages: p502
  source_chapter: Link Layer Discovery Protocol (How-To)
  source_quote: |
    "Tips LLDP is configured at port level (or NI or chassis), but not at linkagg level."
  summary: |
    LLDP（含 notification、TLV、MED 策略）只能配在物理端口/槽/机箱上，配到 linkagg 上不生效。
    聚合成员口的 LLDP 属性要逐口配置——脚本化时按物理口清单遍历。
  conditions: LLDP 配置
  tags: [limitation, lldp, linkagg]

- id: n31
  title: LLDP-MED 两页示例数值不一致（l2-priority/dscp）
  type: limitation
  source_pages: p496, p499
  source_chapter: LLDP NETWORK POLICY TLV/MOBILE TAG（两页示例）
  source_quote: |
    p496: "(OS6860-A) -> lldp network-policy 1 application voice vlan 151 l2-priority 5 dscp 46"
    p499: "(OS6860-A) -> lldp network-policy 1 application voice vlan 151 l2-priority 7 dscp 14"
  summary: |
    同一命令在两页示例中数值不同（p496: l2-priority 5 / dscp 46；p499: l2-priority 7 / dscp 14）。两页均称语音流被打上相应标记，属教材示例不一致（推断为不同版本截图残留）。
    生产取值应按企业 QoS 规划（常见语音 EF=DSCP 46）而非照抄本教材，逐台核查 show lldp config 实配。
  conditions: LLDP-MED 语音策略配置
  tags: [limitation, lldp-med, voice]

- id: n32
  title: Fast/Perpetual PoE 的型号线与前提——OS6360-P10A 不支持、需 FPGA/CPLD 升级
  type: version-trap
  source_pages: p510, p511
  source_chapter: POE POWER MANAGEMENT
  source_quote: |
    "Fast PoE : 2X60, 6360, 6860E, 6860N, 6865, 6870 • Note: OS6360 – P10A does not support FPoE ... • Fast PoE requires an upgraded FPGA/CPLD, refer to the release note." (p510)
    "Perpetual PoE : 2X60, 6360, 6860E, 6860N, 6865, 6870 • Note: OS6360 – P10A does not support PPoE." (p511)
  summary: |
    FPoE（上电即供）与 PPoE（重启不断电）支持 2X60/6360/6860E/6860N/6865/6870，但 OS6360-P10A 两个都不支持，且两类特性都要求先升级 FPGA/CPLD（按 release note）。
    售前承诺"重启不断电"前先核对型号与固件，P10A 与未升 FPGA 的设备都会翻车。
  conditions: PoE 特性选型
  tags: [version-trap, poe]

- id: n33
  title: delayed-start 与 FPoE/PPoE 互斥、必须 write memory、先启动 lanpower 服务
  type: limitation
  source_pages: p520
  source_chapter: POE POWER MANAGEMENT (delayed-feature)
  source_quote: |
    "• Start the lanpower service before enabling the delay start feature. • It is mandatory to do write memory to reflect this command on bootup. • Lanpower service starts after the delay timer expiry ... • Fpoe and Ppoe is not supported on enabling this feature. ... <num> - specific delay value in seconds in multiples of 5. Value should be within 120 to 600 seconds"
  summary: |
    PoE 延迟启动三前提一互斥：先启动 lanpower 服务才能启用；必须 write memory 否则重启后不生效；延迟期内可 lanpower service stop 强制提前结束；启用期间与 Fast/Perpetual PoE 互斥。取值 120-600 秒、5 的倍数。
    想用"延迟供电"的机柜就不能同时要"上电即供"，两者二选一。
  conditions: PoE 启动策略设计
  tags: [limitation, poe]

- id: n34
  title: U-boot 密码一旦丢失无法恢复——启用即单点
  type: warning
  source_pages: p531
  source_chapter: UPGRADING SOFTWARE IMAGE
  source_quote: |
    "U-boot password protection is available since 8.7R3 – be careful when enabling it (no AOS recovery possible in case you lose this password)"
  summary: |
    U-boot 密码保护自 8.7R3 起可用，但密码丢失后 AOS 层面无任何恢复手段（设备报废级后果）。
    启用前把密码入库存档、双人可见；不要为了"防拆"在没有运维流程保障的站点开。
  conditions: 设备物理安全加固
  tags: [warning, upgrade, security]

- id: n35
  title: U-boot/ONIE/FPGA/CPLD 升级失败即 RMA
  type: warning
  source_pages: p533
  source_chapter: UPGRADING SOFTWARE IMAGE
  source_quote: |
    "For U-boot / ONIE and or FPGA / CPLD upgrade, it is usually done through CLI. Be careful as a failure during U-boot / ONIE or FPGA/CPLD upgrade will lead to RMA."
  summary: |
    引导层与硬件逻辑层升级（U-boot/ONIE/FPGA/CPLD）失败没有软恢复路径，直接返厂。
    这类升级必须：稳电网+按 release note 核对前置固件、逐台分批、避开业务窗口。
  conditions: 底层固件升级
  tags: [warning, upgrade, rma]

- id: n36
  title: Auto-Fabric 首启 Y/N 语义相反——Y 才是禁用
  type: misconception
  source_pages: p539
  source_chapter: AUTO-FABRIC - START UP
  source_quote: |
    "Do you want to disable auto-configurations on this switch [Y/N]? N ... N If no response or input is [N], then it is assumed to be false. Meaning to use auto-VC, RCL and auto-fabric Y If input is [Y] then auto-VC, RCL and auto-fabric are disabled"
  summary: |
    出箱首启提示"Do you want to disable auto-configurations?"：回答 N 或超时不答都会启用自动配置（Auto-VC/RCL/Auto-Fabric），只有明确输 Y 才禁用。
    与直觉相反——键盘上随手敲 Y 想跳过提示的人会把自动配置关掉，敲 N 想确认的人会让交换机自动入网。批量开局前先统一操作口径。
  conditions: 新机首次上电
  tags: [misconception, auto-fabric]

- id: n37
  title: RCL 自动拉取配置会重置设备、只有 6 次机会——错过的指令文件不会再来
  type: limitation
  source_pages: p543
  source_chapter: AUTOMATIC REMOTE CONFIGURATION (RCL)
  source_quote: |
    "RCL is run after Auto VC, and before the rest of Auto Fabric ... • RCL tries 6 times, 3 each on VLAN 1 and 127 to get DHCP and download instruction file • To cancel RCL, run command 'auto-config-abort' • At the end of RCL, if a vcboot.cfg is downloaded, the box will be reset"
  summary: |
    RCL（远程自动配置）在 VLAN 1 与 127 上各试 3 次（共 6 次）取 DHCP 与指令文件；一旦下载到 vcboot.cfg 设备会重置加载；中途不想继续要 auto-config-abort 主动取消。
    现场没准备好 DHCP/指令文件时别让新机空跑 RCL（白等 6 轮还可能被旧模板重置），先 abort 或断网。
  conditions: 零触开局现场准备
  tags: [limitation, auto-fabric, rcl]

- id: n38
  title: WebView 默认 enabled 但不允许认证——"打得开登录页"不等于"登得进去"
  type: misconception
  source_pages: p97, p181
  source_chapter: Remote Switch Access (How-To) / Virtual Chassis (How-To)
  source_quote: |
    "By default, the WebView is enabled on the OmniSwitch, but you are not allowed to authenticate. On the Remote-Lab, the WebView access has already been enabled. It is possible to disable it with the command: no aaa authentication http" (p97)
    "If it is not, enable it via the command: aaa authentication http local" (p181)
  summary: |
    WebView 服务出厂 enabled，但 HTTP 认证未授权时登录必失败；需要 aaa authentication http local 显式开启。
    两处重复出现同一坑——排障时先 show aaa authentication 看 Http 服务类型，再怀疑账号密码。
  conditions: WebView 首次启用
  tags: [misconception, webview, aaa]

- id: n39
  title: R8 强制 SSL——明文 HTTP 连不上属预期
  type: limitation
  source_pages: p97
  source_chapter: Setting up the HTTP Session
  source_quote: |
    "SSL is forced by default in Release 8. It means that you can't connect with plain HTTP on R8 OmniSwitches, you will be automatically redirected to an HTTPS connection."
  summary: |
    R8 起 WebView 强制 SSL：http:// 访问会被重定向到 https://，自签名证书浏览器会告警（点 Advanced 继续）。
    老脚本/书签用 http:// 打不开不是故障；证书告警是自签名证书的预期行为（p113 引导步骤明示）。
  conditions: WebView 访问
  tags: [limitation, webview, ssl]

- id: n40
  title: 镜像会话数两处口径不一——规格 4、实验注释 2
  type: version-trap
  source_pages: p249, p265
  source_chapter: PORT MIRRORING / 诊断 How-To
  source_quote: |
    p249: "The same destination port can be used in different port mirroring session and the maximum port-mirroring sessions has been increased from 2 to 4. • There is a limit of 4 Mirror-to-port (MTP) indexes. • Bi-directional counts as two MTP indexes"
    p265: "The maximum number of mirroring sessions is limited to two."
  summary: |
    讲义页说镜像会话上限已从 2 提升到 4（另有 4 个 MTP 索引限制、双向计 2），How-To 实验页仍写"limited to two"。
    按较新规格口径取 4 执行，但现场以 show port-mirroring 实测与 Specification Guide 为准；老版本设备按 2 规划。
  conditions: 镜像容量规划
  tags: [version-trap, mirroring]

- id: n41
  title: 镜像与抓包互斥于同一端口；抓包默认只存前 64 字节
  type: limitation
  source_pages: p251
  source_chapter: PORT MONITORING
  source_quote: |
    "Captures first 64-bytes of frame • Session supported per switch or stack: 1 • Default file size: R8: 64 KB (max = 2 MB) • Round-Robin or stop capture when max storage reached • Cannot use port monitoring and mirroring on same port"
  summary: |
    三条边界：同一端口不能同时配 port-mirroring 与 port-monitoring；抓包每交换机/堆叠仅 1 会话、默认文件 64KB（上限 2MB，写满轮转或停止）；只捕获每帧前 64 字节——够看头部（MAC/IP/端口），看不了应用层内容。
    要完整报文得用镜像 + 外部抓包器，抓包功能只做快速定性。
  conditions: 流量取证方案
  tags: [limitation, monitoring, mirroring]

- id: n42
  title: command.log 启用期间不可删除；最多存 100 条
  type: limitation
  source_pages: p245
  source_chapter: COMMAND LOGGING
  source_quote: |
    "Creates command.log file in /flash directory ... Deleting command.log deletes log history • Cannot be deleted while command logging is enabled • Stores 100 most recent commands • Must be enabled"
  summary: |
    命令日志（command.log，/flash 下）滚动保留最近 100 条；command logging 启用期间文件不可删除（删除会连带丢历史）。
    审计场景保持启用；清盘前先 disable 再处理文件。
  conditions: 审计与日志管理
  tags: [limitation, logging, audit]

- id: n43
  title: DHCP Relay 全局与接口模式互斥
  type: limitation
  source_pages: p353
  source_chapter: DHCP RELAY
  source_quote: |
    "Two types of DHCP relay agents: global and per-interface. ... They are mutually exclusive"
  summary: |
    全局中继（ip dhcp relay destination）与接口中继（per-interface-mode + interface destination）二者只能取其一——从全局切接口模式（或反向）要先清另一侧配置。
    多 DHCP 服务器分网段服务时才需要接口模式；单一服务器用全局即可（实验 Tips 同口径，p371）。
  conditions: DHCP 中继模式选择
  tags: [limitation, dhcp-relay]

- id: n44
  title: 静态链路聚合只能在 ALE 交换机之间用；组内端口必须同速率
  type: limitation
  source_pages: p273
  source_chapter: STATIC VS. DYNAMIC
  source_quote: |
    "Static • Port parameters MUST be exactly the same at both ends and within the group • same speed (e.g., all 10 Mbps, all 100 Mbps, all 1 Gigabit, or all 10 Gigabit) • Only works between Alcatel-Lucent OmniSwitches • Dynamic • IEEE 802.3ad LACP ... It also works between two different devices such as switches, servers and storage systems."
  summary: |
    静态聚合两限制：两端与组内端口参数必须完全一致（同速率），且仅 ALE OmniSwitch 互联可用——接服务器/存储/他厂设备必须用 LACP 动态聚合。
    向服务器团队交付上行时默认按 LACP 设计，别按静态配置文档对接。
  conditions: 聚合对接选型
  tags: [limitation, linkagg, lacp]

- id: n45
  title: 聚合 hash 默认值逐型号不同——6900/6465/6360 是 brief
  type: version-trap
  source_pages: p280
  source_chapter: HASHING CONTROL ALGORITHM
  source_quote: |
    "Switch Default Hashing Mode 9900 extended 6900 brief 6870 extended 6860 extended 6865 extended 6560 extended 6465 brief 6360 brief"
  summary: |
    出厂 hash 默认：9900/6870/6860/6865/6560 = extended（含 UDP/TCP 端口），6900/6465/6360 = brief（仅源/目的 IP）。
    接入层（6360）默认 brief，虚机多网卡同源同目的 IP 的流量会挤在同一成员口——上行不均时先查 hash 模式再骂链路聚合。
  conditions: 聚合负载分担优化
  tags: [version-trap, linkagg, hashing]

- id: n46
  title: 组播默认只走聚合主端口——不开 non-ucast 就不分担
  type: limitation
  source_pages: p281
  source_chapter: LOAD BALANCING MULTICAST ON LINK AGGREGATION GROUPS
  source_quote: |
    "Multicast traffic is by default forwarded through the primary port of the Link Aggregation Group • User has the option to enable hashing for non-unicast traffic ... • If non-ucast option is not specified, link aggregation will only load balance unicast packets"
  summary: |
    默认非单播（组播/广播）不参与聚合分担，全部走主端口——视频/组播大流量会打满单口。
    组播重的站点显式启用 non-ucast hash，或规划时按"组播不分担"算带宽。
  conditions: 组播流量规划
  tags: [limitation, linkagg, multicast]

- id: n47
  title: OST 1.0 已停更；OST 2.0 下载免费但需有效支持合同
  type: limitation
  source_pages: p229, p230
  source_chapter: ALE OMNIVISTASMART TOOL (OST1.0 / OST2.0)
  source_quote: |
    "OST 2.0 is a Windows-based application available for download free of charge via ALE MyPortal. • The tool is available to customers with a valid OmniSwitch support contract. • The OmniSwitch Smart Tool is available for all Business Partners with a valid distributor agreement" (p229)
    "OST 1.0 will remain in Github as a community available version but no further development will be done by ALE." (p230)
  summary: |
    版本边界：OST 1.0（GitHub/Spacewalkers 社区版）ALE 不再开发；2.0 经 MyPortal 免费下载，但客户需持有效 OmniSwitch 支持合同（BP 需分销协议）。
    现场没合同装不了 2.0、用 1.0 又无新特性修复——支持合同状态是装机前的第一道核查。
  conditions: 工具引入与合规
  tags: [limitation, ost, licensing]

- id: n48
  title: EEE 仅铜口 100/1000M 有效，U 型光纤口不支持
  type: limitation
  source_pages: p512
  source_chapter: ENERGY EFFICIENT ETHERNET (EEE)
  source_quote: |
    "Protocol to allow chipset to go to a low power mode state when idle (i.e. no traffic sent) • Compatibles with OmniSwitches models except 'U' models (optical fiber models). • EEE is only applicable to OmniSwitch copper ports operating at 100/1000 Mbps speed"
  summary: |
    EEE（802.3az）节能只在铜口 100M/1000M 生效；U 后缀（光口）机型不支持。
    节能核算别把光纤上行与 10G 口算进去；链路两端 EEE 能力不一致时的行为以 Specification Guide 为准。
  conditions: 节能与端口选型
  tags: [limitation, poe, eee]

- id: n49
  title: 实验 SSH 凭据与交换机登录凭据不同（admin-netadv/Superuser01! vs admin/Superuser=1）
  type: limitation
  source_pages: p15, p38
  source_chapter: REMOTE LABS
  source_quote: |
    p15: "OmniSwitch credentials: login: admin password: Superuser=1"
    p38: "On terminal window, indicate : ssh admin-netadv@10.4.X.Y ... Enter the passphrase: Superuser01!"
  summary: |
    实验口径两套凭据并存：从 Linux 客户端 SSH 到交换机用 admin-netadv/口令 Superuser01!；直连交换机控制台用 admin/Superuser=1。
    这是 R-Lab 特有配置（admin-netadv 为实验账号），生产环境不存在——把实验凭据记成"产品默认"会在现场抓瞎（实验口径）。
  conditions: 仅 RLAB 培训环境
  tags: [limitation, lab, credentials]

- id: n50
  title: 实验交换机是"最小化配置"不是空配置——预置静态路由与预建聚合
  type: limitation
  source_pages: p92, p284, p286
  source_chapter: Remote Switch Access (How-To) / Link Aggregation (How-To)
  source_quote: |
    p92: "The OmniSwitches have been reinitialized with a minimum Network configuration. Please note this is not an empty configuration. ­ A static route is configured to reach the administration network 10.0.0.0"
    p286: "On the 6870-A, 3 link aggregations are available: the new one you created (linkagg 7), plus 2 other link aggregations (17 and 78) used to connect the switch to the 6900 and 6860-B ... These two other aggregations have already been created on a previous lab or via a configuration download at the beginning of the course"
  summary: |
    R-Lab 交换机预置了到管理网的静态路由、部分聚合（17/78）与 WebView 授权等——实验里"凭空出现"的配置都来自预置或前序实验（实验口径）。
    把实验环境当出厂基线复刻到生产会带上看不见的预置路由；生产开局永远从确认后的模板开始。
  conditions: 仅 RLAB 培训环境
  tags: [limitation, lab]

- id: n51
  title: 无线客户端严禁断开 Ethernet——一断即失联
  type: warning
  source_pages: p43
  source_chapter: DISCONNECT FROM A SSID
  source_quote: |
    "3. Warning: NEVER Disconnect the Ethernet Network > you will lose access to the Wireless Client"
  summary: |
    无线客户端同时有线+无线连接：断有线网络即失去对该客户端的远程访问（远控走有线）。
    实验 802.1X 切换时只操作 Wi-Fi 连接，别手滑断了 Ethernet（WLAN 章节实验依赖该客户端）。
  conditions: RLAB 无线客户端操作（实验口径）
  tags: [warning, lab]

- id: n52
  title: 浏览器口径——推荐 Chrome/Edge，Firefox 有复制粘贴兼容问题
  type: limitation
  source_pages: p14
  source_chapter: CONNECT TO THE REMOTE LAB
  source_quote: |
    "Recommended web browsers: • Chrome • Edge ... Notes: We recommend to use Google Chrome or Firefox. Other web browser may have some issue with copy/paste from a lab guide to the remote terminal session. Known workaround for Firefox: https://sudoedit.com/firefox-async-clipboard/"
  summary: |
    R-Lab 入口推荐 Chrome/Edge；Firefox 从实验指导复制粘贴到远程终端可能异常（需 async-clipboard workaround）。（注：标题行与 Notes 行推荐浏览器表述不一致——标题写 Chrome/Edge、注释写 Chrome/Firefox，以"避免 Firefox 复制粘贴问题"的实际意图为准。）
    培训前统一浏览器减少环境噪音。
  conditions: RLAB 接入（实验口径）
  tags: [limitation, lab]

- id: n53
  title: 握手类安全特性默认面——早期 ARP 丢弃默认开、DHCP 中继 Opt82 默认关、PXE 默认关
  type: rule
  source_pages: p443, p354
  source_chapter: ADVANCED ACL SECURITY FEATURES / DHCP RELAY
  source_quote: |
    "Early ARP discard • Limitation of number of ARP packets sent to CPU • ARP packets not destined for switch are not processed • Enabled by default • ARPs intended for use by a local subnet, AVLAN, VRRP, and Local Proxy ARP are not discarded" (p443)
    "-> ip directed-broadcast disable ... IP datagram sent to broadcast address of subnet the user is not on • Generates large number of responses to a spoofed host" (p443)
    "Relay Agent Information = Disabled, Relay Agent Information Policy = Drop, ... PXE support = Disabled" (p354)
  summary: |
    默认面三项：①早期 ARP 丢弃默认启用（非本机 ARP 不送 CPU；本地子网/AVLAN/VRRP/Local Proxy ARP 不受影响）；②定向广播默认可关（ip directed-broadcast disable 防反射放大）；③DHCP 中继的 Option 82 插入与 PXE 支持默认关闭（需要 Option 82 的接入认证/PXE 网络要显式打开）。
    依赖这些默认值做设计前先 show 核对实况。
  conditions: 安全与 PXE/认证设计
  tags: [rule, security, dhcp]

- id: n54
  title: 生成树阻塞口选择由"路径成本与端口 ID"决定——教材留白不给答案
  type: limitation
  source_pages: p317, p296, p318
  source_chapter: STP / 802.1q (How-To 思考题)
  source_quote: |
    "What determines which side of the link is blocking? ____" (p317)
    "How are the Clients VM exchange between each other (Layer 2 or Layer 3)? ____" (p296)
    "Has our Topology age changed? / Has the Root port changed? ____" (p319)
  summary: |
    教材多处实验以开放式提问收尾（阻塞侧判定、二层还是三层、Topology age/Root port 是否变化），不提供标准答案——依赖学员从 show spantree 输出反推。
    用本教材做自动化题库或考核时，这些空缺需自行补齐答案（阻塞侧=根路径成本→发送者桥 ID→端口 ID 逐级比较；Client 间流量走三层——不同 VLAN 网关路由）。（推断：由 STP 标准机制与实验拓扑推出，教材原文未给。）
  conditions: 教学考核与知识转移
  tags: [limitation, stp, teaching]

- id: n55
  title: 微码 show 输出按目录区分——working/certified/loaded 三个口径别混
  type: limitation
  source_pages: p141
  source_chapter: Displaying the microcode version
  source_quote: |
    "sw3 (6560-A) -> show microcode working |or| show microcode certified |or| show microcode loaded ... Notes 'Loaded'? ­ Loaded displays the currently active microcode versions. ­ Entering the command show microcode also displays the currently active microcode version."
  summary: |
    微码三口径：show microcode working/certified 看两目录里装的版本；show microcode loaded（或无参 show microcode）看当前实际加载版本。
    升级验证必须看 loaded 而不是 working——镜像拷进目录不等于已经运行。
  conditions: 升级验证
  tags: [limitation, upgrade]
```

---

## 收尾自检 — 对照 BOOK_OVERVIEW.md 26 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | 远程实验室接入 | 有 → n49（双凭据）、n50（非空配置）、n51（勿断 Ethernet）、n52（浏览器口径） |
| task-02 | 多方式登录 | 有 → n38（WebView 认证默认关）、n39（强制 SSL） |
| task-03 | 用户与认证服务器 | 有 → n01（默认口令版本线） |
| task-04 | 加固管理面 | 有 → n02（禁 console 即 RMA） |
| task-05 | WebView 管理 | 有 → n38、n39 |
| task-06 | Lightning Config | 有 → n03（六禁令）、n04（Defaults/IP 唯一）、n05（密码避 ! $）、n06（出箱禁互联）、n07（必 Write Memory） |
| task-07 | 配置生命周期 | 有 → n08（reload all）、n09（未保存重启即丢）、n10（certified 只读）、n11（boot.md5/certify 前验证）、n12（usb disable） |
| task-08 | Virtual Chassis | 有 → n13（write memory 清配置警告）、n14（reload 才生效） |
| task-09 | VLAN 与 802.1Q | 有 → n15（VLAN1 不可删）、n16（无成员接口 DOWN）、n17（默认 VLAN 恒桥接） |
| task-10 | VLAN 间路由与 IP 接口 | 有 → n16、n43（DHCP Relay 互斥）、n53（Opt82 默认关） |
| task-11 | OST 使用 | 有 → n47（1.0 停更/2.0 合同门槛） |
| task-12 | 诊断八件套 | 有 → n40（镜像 2 vs 4）、n41（镜像抓包互斥/64 字节）、n42（command.log）、n55（微码三口径） |
| task-13 | 链路聚合 | 有 → n23（先清口）、n44（静态仅 ALE）、n45（hash 逐型号）、n46（组播主端口） |
| task-14 | STP | 有 → n18（状态随根桥）、n19（单侧 blocking）、n20（物理变更收敛）、n54（思考题留白） |
| task-15 | DHL | 有 → n21（STP 自动禁）、n22（30 秒回切） |
| task-16 | DHCP | 有 → n43、n53 |
| task-17 | VRRP | 有 → n24（先 disable 再改优先级） |
| task-18 | QoS | 有 → n25（不信任口改写标记）、n26（qos apply）、n27（默认 accept） |
| task-19 | ACL 与用户口 | 有 → n26、n27、n28（UserPorts 仅路由流量） |
| task-20 | Access Guardian | 有 → n29（无 MAC 登记 Block） |
| task-21 | LLDP | 有 → n30（不支持 linkagg 级）、n31（两页数值不一致） |
| task-22 | PoE | 有 → n32（P10A/FPGA）、n33（delayed-start 互斥）、n48（EEE 限制） |
| task-23 | 软件升级 | 有 → n34（U-boot 密码无恢复）、n35（底层升级失败 RMA） |
| task-24 | Auto-Fabric | 有 → n36（Y/N 反直觉）、n37（RCL 6 次与重置） |
| task-25 | Fleet Supervision | 无独立边界条目（p555-569 无 Warning/Note 框；限制已在 BOOK_OVERVIEW 术语差异列注明"只看不管"） |
| task-26 | OST 2.0 安装 | 有 → n47 |

**25/26 全部有边界类条目覆盖**（task-25 原文无警示框，如实留白）。扫描完整性说明：

### Warning/Note/Tips 标记框逐页核对
- 已入册的 Warning 框：p43（勿断 Ethernet）、p77（console RMA）、p108（Lightning 六禁令）、p115（Defaults/IP 唯一）、p116（密码规则）、p117（出箱禁互联）、p118（Write Memory）、p125（环路 STOP）、p142（reload all）、p143/p144（重启丢失两段）、p146（certify 前验证）、p148（usb disable）、p176（VC write memory 警告）、p319（物理变更收敛）、p390（VRRP disable）、p531（U-boot 无恢复）、p533（底层升级 RMA）。
- 已入册的 Notes/Tips/ERROR：p95 Tips（ssh 认证 denied 恢复，并入 c01）、p97（WebView 认证与 SSL）、p141（loaded 口径）、p146（boot.md5 忽略）、p175/176（reload 才生效）、p249（镜像 2→4）、p265（旧口径 two）、p294（状态随根桥）、p317（单侧 blocking）、p338（端口先清配）、p341（DHL 禁 STP）、p344（30 秒回切）、p423（信任语义）、p424/425（qos apply）、p434（默认 accept）、p453（UserPorts 路由流量）、p478/485（MAC Block）、p502（LLDP 层级）、p510/511（P10A/FPGA）、p520（delayed-start）、p539（Y/N 语义）、p543（RCL 6 次）。
- 复核后排除的纯操作提示（非边界，不构成候选）：p26（Linux 客户端步骤注）、p96 Notes（write memory 输出解释）、p175 Notes（等待重启完成）、p285/286 Notes（actor admin key 本地意义）、p293 Notes（路由核查）、p371 Tips（按 VLAN 中继）、p388 Tips（MAC 表为空造流量）、p422 Notes（实验范围声明）、p428 Tips（log 建议）、p448（MAC 示例说明）、p472 完整命令行参数表、p480 Notes（Filter-Id 机制，已入 principle p27/p29 语义）、p502 Notes（LLDP 默认双开）、p504 Tips（前后对比）、p514（预算查规格）。
- 推断性结论已标"（推断）"：n31（LLDP-MED 数值不一致为截图残留的推断）、n36（Y/N 反直觉的场景化描述）、n54（STP 阻塞侧判定与题库补齐，教材原文留白）。
- 版本号均按原文保留完整位数：8.7R3、8.9R3、8.9R4、8.10R03、8.10R4、8.10R04、18.1。
