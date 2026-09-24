# 反例/限制/边界/易错点候选 — OmniPCX Enterprise Advanced (ENTPXTE401EN Ed13, R101.1 MD4)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: RLAB 启动顺序约束——CSB 与 PCS REMOTE 必须延后启动避免 IP 冲突
  type: limitation
  source_pages: p47-48, p375
  source_chapter: Pod Configuration（两套 How-To）
  source_quote: |
    p47: "OXE CSB (ENTP_OXE_CSB) and PCS REMOTE (ENTP_PCS_REMOTE) will be started later to avoid IP
    address conflict."
    p375: "Due to RLAB infrastructure and technology, 2 VMs (even if not started) can't have the same IP
    address."
  summary: |
    RLAB 平台不允许两台 VM（哪怕没开机）持有相同 IP：集中式 Pod 里 ENTP_OXE_CSA 与 ENTP_OXE_CSB/PCS
    REMOTE 的地址安排要求按清单顺序启动；组网 Pod 更需先做网卡迁移（ENTP_OXE_CSA 摘除 192.168.1.1、
    ENTP_OXE_NODE_1 重建该地址）。这是纯教学基础设施约束，照搬到生产没有意义，但实验卡在"ping 不通"时
    先查启动顺序与网卡归属。
  conditions: RLAB 环境实验准备阶段
  tags: [limitation, rlab, ip-conflict]

- id: n02
  title: host-based SSH 认证已被 CIS 合规移除——老脚本/老习惯失效
  type: version-trap
  source_pages: p57
  source_chapter: SSH Key Distribution / Overview
  source_quote: |
    "From N3 onwards, for security reasons SSHv2 is enabled by default with public key authentication. ...
    Host based authentication is no longer supported, thanks to CIS compliance requirements."
  summary: |
    N3 起 SSHv2+公钥认证为默认且 host-based 认证不再支持。凡是按旧版本习惯依赖 host-based 免密的脚本、
    手册或运维直觉（mastercopy/pcscopy/audit/broadcast 的前置）都会在 N3+ 系统上失败；正确路径是三账户
    （mtcl/swinst/root）密钥分发。
  conditions: N3 及以后版本的所有免密场景
  tags: [version-trap, ssh, security, cis]

- id: n03
  title: 角色 MAO 未定义时的防御行为——IP 高者自动成 main
  type: warning
  source_pages: p75, p104-105
  source_chapter: CALL SERVER ROLE INITIALIZATION / How-To
  source_quote: |
    "Defense: If the 'Call server role' is not correctly defined, the CS with the highest IP address
    starts in Main role"
    "If this parameter is not configured, the Com Server with the highest IP address becomes main."
  summary: |
    Preferred CS IP @（redundancy）没配时，两 CS 同时上线由"IP 地址最高者"当 main——这是防御性行为而非设
    计意图。实验口径里 csa(1.1) < csb(1.2)，不配 preferred 会导致 csb 抢主；现场规划网按时要把这个隐含规
    则纳入，或显式配置 preferred。
  conditions: 双 CS 同时上线/同时出现的场景
  tags: [warning, redundancy, role, ip]

- id: n04
  title: 冗余对硬约束——同版本 + 同平台，netadmin 后必须关机重启
  type: warning
  source_pages: p70, p94, p97, p99, p117, p120, p122
  source_chapter: CS DUPLICATION / 两套冗余 How-To 的 Warning 框
  source_quote: |
    "The 2 Call Servers must have the same type, and the same software release" (p70)
    "CALL SERVERS MUST HAVE THE SAME SOFTWARE VERSION AND BE IMPLEMENTED ON IDENTICAL PLATFORMS" (p94, p117)
    "A SHUTDOWN OF THE CS IS MANDATORY AFTER THE NETADMIN MANAGEMENT" (p97, p99, p120, p122)
  summary: |
    两类全大写警告：①冗余对必须同软件版本且部署在同类平台（CS 板卡/GAS/VM 混搭不成立）；②每次 netadmin
    改完 IP/防火墙后必须关机重启 CS 才生效。漏掉重启是"配了但行为不对"的第一嫌疑。
  conditions: 冗余部署与 IP 维护
  tags: [warning, redundancy, netadmin, reboot]

- id: n05
  title: mastercopy 三前提——SSH 密钥先行、只能在备机上做、备机话音必须先停
  type: warning
  source_pages: p71, p100, p107, p131
  source_chapter: INTRODUCTION / How-To Database cloning
  source_quote: |
    "SSH Public/private keys must be distributed between Main Call Server and the Stand-by CS, to
    authorize the DB copy • Updates must be done with a 'secured copy protocol' (scp)" (p71)
    "You must be logged on the call server where you want to copy the database. In this case, call server
    B ... Telephone application must be stopped on 'csb' to permit the 'mastercopy'" (p107)
  summary: |
    mastercopy 失败三主因：密钥没分发（scp 无授权）、登错了机器（必须在"要被覆盖"的备机上执行）、备机话
    音应用没停。另外要有心理预期：克隆过程分钟级（书内 Warning "BE PATIENT!"，实验输出等待约 3 分钟）。
  conditions: 数据库克隆/冗余初始化
  tags: [warning, mastercopy, duplication, ssh]

- id: n06
  title: netadmin 管的 Linux 数据不随电话库复制——防火墙会"丢"
  type: limitation
  source_pages: p74, p94, p108, p132
  source_chapter: IMPLEMENTATION / How-To mastercopy Notes
  source_quote: |
    "LINUX data managed by netadmin are not duplicated (manual update is required: 'Copy to Twin'
    option)" (p74)
    "'Linux data' contains information entered by netadmin command. So, for example, the content of the
    internal firewall of 'csa' will be copied in 'csb'." (p108)
  summary: |
    冗余链路只复制 swinst 管的 Linux 数据；netadmin 维护的部分（最典型=内部防火墙 iptables）不实时复制。
    补齐两条路：mastercopy 时勾选 LINUX DATA=y（实验采用），或 netadmin→Copy setup→Copy to twin CPU。
    只配了 csa 防火墙、没做任一同步的 csb，在接管后防火墙是空的。
  conditions: 冗余/防火墙维护
  tags: [limitation, netadmin, firewall, duplication]

- id: n07
  title: 双 main 期间话单与话务观察不合并、部分网络无语音邮箱
  type: limitation
  source_pages: p82
  source_chapter: MISCELLANEOUS
  source_quote: |
    "Services not provided in Double Main mode: • Accounting (tickets generated on the Pseudo Main can
    not be reported on the other call server) • Traffic observation (same thing) • One part of the
    network has no Voice Mail"
  summary: |
    IP 链路中断形成 real/pseudo double main 期间：Pseudo Main 上的话单不会汇总（计费对账会缺数）、话务观
    察同样、部分网络没有语音邮箱。链路恢复并按参考 MG 收敛后才会复原——期间的话务/计费缺口要有预期。
  conditions: IP 链路中断期间
  tags: [limitation, double-main, accounting]

- id: n08
  title: 主备失联窗口 120 分钟——超时触发 440 后只能 mastercopy
  type: limitation
  source_pages: p79
  source_chapter: DATABASE CONSISTENCY
  source_quote: |
    "Limited time: 120 minutes by default ... After storage time limit: history of MAO commands is
    deleted and incident « 440 » is triggered. A database cloning operation, also called 'Mastercopy',
    is then necessary !"
  summary: |
    备机不可达时主库只保存 120 分钟（0-120 可配）的 MAO 命令历史；超时历史删除并触发 440，此后备机即使回
    来也无法增量补齐，必须整库克隆。运维排班要把"备机故障必须在窗口内修复"当成硬时限。
  conditions: 冗余系统备机宕机
  tags: [limitation, duplication, incident-440, sla]

- id: n09
  title: 空间冗余的 DNS 陷阱——必须委派节点名到两个主地址且不缓存
  type: warning
  source_pages: p88-89, p136
  source_chapter: EXTERNAL APPLICATIONS（内部/外部 DNS） / How-To SIP terminals
  source_quote: |
    "Ensure that this information is not cached (and reused after a switchover between the two CS)" (p88)
    "It is necessary to explain to the LAN manager that the DNS requests concerning the node name must be
    rerouted towards the DNS servers of the two CS (main IP addresses). A DNS delegation is required." (p89)
    "Moreover, INTERNAL DNS RESOLVER activation is mandatory in the OXE (done with 'netadmin' tool)." (p136)
  summary: |
    三个易漏点：①SIP 设备直填两个主地址当 DNS 时，必须确保结果不被缓存（否则切换后连旧主）；②客户有 DNS
    时必须做委派（oxe.company.com → 两个主地址），要提前与客户 LAN 管理员交底；③OXE 内部 DNS 解析器必须
    在 netadmin 启用，否则无法应答客户 DNS 的回查。漏任何一条，spatial 冗余下 SIP 应用在切换后失联。
  conditions: 空间冗余 + SIP 终端/应用
  tags: [warning, spatial-redundancy, dns, sip]

- id: n10
  title: IP 域地址范围不得覆盖 CS 地址；CS 必须域 0
  type: limitation
  source_pages: p152, p199
  source_chapter: MISCELLANEOUS（IP DOMAINS）/ PCS How-To
  source_quote: |
    "THE CALL SERVER(S) MUST BELONG TO DOMAIN 0 • THIS ENTAILS THAT THE IP ADDRESS RANGES CONFIGURED FOR
    THE OTHER DOMAINS MUST NOT ENCOMPASS THE PHYSICAL AND ROLE IP ADDRESSES OF THE COM SERVER(S)" (p152)
    "THE PCS MUST REMAIN IN IP DOMAIN 0!" (p199)
  summary: |
    两条"必须域 0"硬规则：呼叫服务器物理与角色地址不得被任何自定义域的地址段（含单主机条目）覆盖；PCS 也
    必须留在域 0。把 CS/PCS 的网段整段划进业务域是常见的规划事故——CAC、生存性、资源分配全部会错乱。
  conditions: IP 域规划与 PCS 部署
  tags: [limitation, ip-domain, domain-0, pcs]

- id: n11
  title: 域掩码必须与设备一致；设备/板卡不复位不落域
  type: warning
  source_pages: p158
  source_chapter: IP domains How-To（Warning 框）
  source_quote: |
    "THE SUBNET MASK MUST BE THE SAME AS IN THE EQUIPMENT! DEVICES AND BOARDS MUST BE RESETED IN ORDER TO
    BE ASSIGNED TO THE RIGHT IP DOMAIN • THE CS PLACES THE VOIP EQUIPMENT IN THEIR IP DOMAIN AT THE END OF
    THEIR INITIALIZATION PHASE"
  summary: |
    域地址条目的掩码照抄设备实际掩码（不是想当然的 /24）；域配置改完，话机与板卡必须复位才会被划入新域
    （CS 在设备初始化结束时落域）。"建了域但设备还在域 0"十有八九是没复位或掩码不匹配。
  conditions: IP 域地址分配后
  tags: [warning, ip-domain, reset, mask]

- id: n12
  title: 无 MG 的域里 SIP 话机与 SIP 外部网关救不了
  type: limitation
  source_pages: p169
  source_chapter: TOPOLOGY – CASE #2
  source_quote: |
    "SIP PHONES AND SIP EXTERNAL GATEWAYS SITUATED IN A DOMAIN WITH NO MEDIA GATEWAY CANNOT BE RESCUED"
  summary: |
    PCS 可以一台救多个域，但若某域完全没有媒体网关，该域内的 SIP 话机与 SIP 外部网关无法被救援（多域共救
    时至少一个域须含 MG；且每台 PCS 至少绑定一台 MG）。纯 SIP 远程站点要做生存性，得先给域里放一台 MG 或
    改用其他方案。
  conditions: PCS 拓扑设计
  tags: [limitation, pcs, sip, media-gateway]

- id: n13
  title: PCS 出厂 IP 与实验网不兼容——首配必须 console 模式
  type: limitation
  source_pages: p187, p189
  source_chapter: PCS How-To Requirements / IP configuration
  source_quote: |
    "the PCS VM uses a default IP configuration (10.253.253.1/26), which is not compatible with the IP
    configuration of the PC (192.168.x.1x/24). So, as not ethernet access is possible in a first step,
    you must use the 'console mode'"
  summary: |
    PCS VM 出厂网络是 10.253.253.1/26，与常规 192.168.x 网段不互通——第一次配置改不了 IP 就连不上，必须走
    Rlab console。现场部署 PCS 也要预留带外/控制台通道，别假设"上架即可 SSH"。
  conditions: PCS 首次配置
  tags: [limitation, pcs, console, ip]

- id: n14
  title: pcscopy 前提：双向 trusted hosts + hosts 文件条目，缺一不可
  type: limitation
  source_pages: p190-192, p193-195
  source_chapter: PCS How-To IP configuration / CS firewall
  source_quote: |
    "Add trusted hosts (csa, csb and csm): this is mandatory for the 'pcscopy' operation" (p190)
    "The 'pcscopy' command does not work if the IP addresses are not present in the hosts files. Without
    this management, the update of the database of the PCS will be impossible." (p192)
    "In case of duplication, please perform a 'copy to twin' to synchronize the changes with the twin CS" (p195)
  summary: |
    pcscopy 失败排查顺序：①PCS 侧防火墙是否已把 csa/csb/csm 加为 trusted hosts（/etc/hosts 自动更新，可用
    more /etc/hosts 核对）；②CS 侧是否已把 pcs 加为 trusted host；③冗余系统里 CS 侧改动是否 Copy to twin
    同步到了另一台。hosts 文件缺条目时库更新直接不可能。
  conditions: PCS 数据库同步
  tags: [limitation, pcs, pcscopy, hosts, firewall]

- id: n15
  title: PCS 库单向同步——PCS 上的修改下次更新即丢；八类参数必须逐台手工配
  type: limitation
  source_pages: p179-180
  source_chapter: PCS DATABASE / PARAMETERS TO BE MANAGED ON THE PCS
  source_quote: |
    "BE AWARE THAT 'DATABASE SYNCHRONIZATION' IS UNIDIRECTIONAL: ONLY FROM CS TOWARD PCS ... THOSE
    MODIFICATIONS WILL BE LOST AT THE NEXT DATABASE UPDATE BETWEEN THE CS AND PCS" (p179)
    "Some parameters ... are not sent to the PCS during the update, such as: Internal Firewall • Date,
    Time & Timezone • NTP configuration • SSH configuration • Syslog Server • Hosts file • SNMP
    configuration • Radius users" (p180)
  summary: |
    两条数据纪律：①库同步只从 CS 到 PCS——在 PCS 上直接做的数据库修改是临时的，下次更新被覆盖；②防火墙/
    时间/NTP/SSH/Syslog/hosts/SNMP/Radius 八类参数不随库走，每台 PCS 都要手工配。特别是防火墙漏配时，设
    备救援过来也连不上 PCS。
  conditions: PCS 日常运维
  tags: [limitation, pcs, database, manual-params]

- id: n16
  title: PCS 最多连续激活 30 天——超时进入软件保护违约态
  type: limitation
  source_pages: p182
  source_chapter: MISCELLANEOUS
  source_quote: |
    "The PCS can be active for 30 days max • After 30 days, it switches in 'Software protection violation'
    position"
  summary: |
    PCS 是临时生存手段：最长连续激活 30 天（431 事件报剩余时间），超时进入违约态（432 事件）。把 PCS 当
    "长期分支局方案"卖是错误设计——它的定位是争取中心侧修复时间；30 天内必须恢复 CS 链路。
  conditions: PCS 激活期管理
  tags: [limitation, pcs, 30-days, licensing]

- id: n17
  title: PCS 能力边界——4645 VM/SIP 传真/SIP VM 救不了；无 TFTP/DHCP/ABC-F；话单需 8770 取回
  type: limitation
  source_pages: p181, p183
  source_chapter: ACCOUNTING / RESTRICTIONS
  source_quote: |
    "The tickets generated by the PCS (during its Active mode period) are not retrieved by the Call
    Server. However, with the OmniVista 8770 it is possible to retrieve those tickets" (p181)
    "Terminals of an IP domain rescued by a PCS can not reach the 4645 Voice Mail ... SIP fax servers &
    SIP Voice Mails cannot be rescued by PCS • No TFTP service (no binaries download) • No DHCP service •
    No ABC-F service" (p183)
  summary: |
    五条边界：被救话机打不了 4645 语音邮箱；SIP 传真服务器与 SIP 语音邮箱不能被救；PCS 不提供 TFTP（话机
    无法下 binaries）与 DHCP；不提供 ABC-F；PCS 激活期产生的话单 CS 不会自动收回，要靠 OmniVista 8770 日
    同步或手动。客户问"分部断了还能不能用留言信箱"——答案是不能。
  conditions: PCS 接管期间
  tags: [limitation, pcs, voice-mail, accounting]

- id: n18
  title: 外部 SIP 网关被救前提：PCS IP 必填 + 注册计时器 ≠0 + 全网取法一致（不可混用全局地址与真实地址）
  type: warning
  source_pages: p177-178, p202
  source_chapter: PCS & EXTERNAL SIP GATEWAYS / How-To
  source_quote: |
    "WARNING: If several SIP external gateways are created, all of them need to be managed in the same
    way (regarding the 'PCS IP Address' parameter): Either with the global IP Address OR with a real PCS
    address. It's not possible to mix both types among the gateways." (p178)
    "The PCS IP address must be specified, and the registration timer must be different from 0, otherwise
    the backup of the external SIP gateway will not work properly." (p202)
  summary: |
    三个坑：①网关要被救必须填 PCS IP 地址且注册计时器不为 0；②多台网关的 PCS 参数取法必须统一——要么全用
    全局地址 255.255.255.255，要么全用真实 PCS 地址，混用即故障；③好消息是"单网关 + 单中继组"即可覆盖多
    PCS 场景，入局由 SIP 运营商按 503 重路由，ARS 也更简单。
  conditions: SIP 中继生存性设计
  tags: [warning, pcs, sip-gateway, config]

- id: n19
  title: 断链演练期间主站全部 VM 不可 IP 访问——测试只能用远端 PC
  type: warning
  source_pages: p212
  source_chapter: PCS How-To Network breakdown simulation
  source_quote: |
    "AT THIS STAGE, AS SUBNET 1 HAS BEEN DISCONNECTED, YOU DON'T HAVE ACCESS ANYMORE TO VIRTUAL MACHINES
    OF THE MAIN SITE (CS, OMS, PC...) THROUGH IP. SO, FOR THE TEST, USE PC VM BELONGING TO REMOTE SITE
    (SUBNET 2: 192.168.2.X)"
  summary: |
    Rlab 断开 Subnet 1 模拟断网后，主站的 CS/OMS/PC 全部失去 IP 可达性——包括你正远程着的那台。演练前要
    把操作路径切到 Subnet 2 的 PC VM，否则会把自己锁在门外；生产演练同理要准备带外通道。
  conditions: PCS 断网演练
  tags: [warning, pcs, drill, access]

- id: n20
  title: 本地私到公溢出不适用 SIP 扩展/SIP 设备；话务台却恒放行
  type: limitation
  source_pages: p223, p226
  source_chapter: ACCESS TO THE SERVICE / MISCELLANEOUS
  source_quote: |
    "Attendant set • The service is always available (no call barring)" (p223)
    "Doesn't work for call to SIP extensions or to SIP devices" (p226)
  summary: |
    两个方向的不对称：本地私到公溢出对"呼叫 SIP 扩展或 SIP 设备"无效——纯 SIP 远端在断链场景没有公网退
    路；而话务台发起的溢出永远可用、不受闭锁约束（计费上要留意话务台这条"后门"）。设计与计费沟通都要把
    这两点讲清。
  conditions: 溢出方案设计与计费说明
  tags: [limitation, overflow, sip, attendant]

- id: n21
  title: 本地私到公溢出实验在 RLAB 不可执行——仅作现场参考规程
  type: limitation
  source_pages: p229
  source_chapter: Local Private to Public Overflow How-To
  source_quote: |
    "PLEASE, NOTE THAT THIS LAB CANNOT BE PERFORMED WITH THE CURRENT RLAB ENVIRONMENT. THIS MANAGEMENT
    PROCEDURE IS PROVIDED ONLY AS INFORMATION, FOR CONFIGURATION PURPOSE ON CUSTOMER SITE."
  summary: |
    全书唯一明示"课堂上做不了"的实验：该章配置步骤只在客户现场可验。培训学员对这章没有手感，交付前应组
    织现场演练或沙盘；同时 ARS 管理是其强前置且属 Starter 内容（p229 Warning）。
  conditions: 本地溢出配置交付
  tags: [limitation, overflow, lab, starter]

- id: n22
  title: 溢出配置的字段陷阱——Install No Last Part 必须留空、thin sector 外号不得与 DID 段重叠、配完 pcscopy
  type: warning
  source_pages: p230-232
  source_chapter: Local Private to Public Overflow How-To
  source_quote: |
    "'Installation No Last Part': IN CASE OF 'LOCAL PRIVATE TO PUBLIC OVERFLOW', THIS FIELD HAS TO BE
    EMPTY. THE 'THIN SECTOR' WILL BE USED TO PROVIDE A DEFAULT NUMBER" (p230)
    "THIS FIRST EXTERNAL NUMBER MUST NOT OVERLAP A PREDEFINED DID SECTOR OF THE 'NODE ACCESS PREFIX'" (p231)
    "Don't forget to perform a 'pcscopy'" (p232)
  summary: |
    三个易错点：①Node Access Prefix 的 Install No Last Part 在本地溢出场景必须留空（由 thin sector 兜非
    DID），填了会与 thin sector 打架；②thin sector 使用的唯一外号不得与该前缀已定义的 DID 段重叠；③改完
    系统参数（Overflow on OoS Extension）要 pcscopy 同步到 PCS，否则断链时 PCS 侧行为不一致。
  conditions: 本地溢出配置
  tags: [warning, overflow, thin-sector, pcscopy]

- id: n23
  title: 速拨闭锁默认关闭——缩位号默认绕过闭锁表；上限默认只有 4000
  type: limitation
  source_pages: p236, p247
  source_chapter: SPEED DIALING（概念）/ How-To limit
  source_quote: |
    "A speed dial number is subject to barring tables for access to the public network only when declared
    as barred" (p236)
    "But, by default, only the first 4000 indexes are configurable." (p247)
  summary: |
    两个默认值陷阱：①缩位号默认不受公网闭锁管控——不做闭锁设计就上缩位号，等于给用户开了绕过拨号权限的
    侧门（要逐号勾 Call Restriction-Barring）；②数据库标称 32500 条，出厂只有前 4000 个索引可配，扩容要
    cfgUpdate + 重启。
  conditions: 速拨体系上线
  tags: [limitation, speed-dialing, barring, capacity]

- id: n24
  title: 多目录号键必须选编号计划内空闲号
  type: warning
  source_pages: p269
  source_chapter: Multi-Line & Supervision Keys How-To
  source_quote: |
    "IN CASE OF MULTI DIRECTORY NUMBERS, BE SURE TO SELECT A FREE DIRECTORY NUMBER FROM THE NUMBERING PLAN"
  summary: |
    给话机加附加目录号（Multi-MCDU）时必须从编号计划里挑空闲号——占用已分配号码会造成双绑与呼叫异常。扩
    展键位前先查编号计划余量。
  conditions: 多目录号配置
  tags: [warning, multiline, numbering]

- id: n25
  title: 监督体系四条硬上限 + 两类不可监督对象
  type: limitation
  source_pages: p262, p265
  source_chapter: SUPERVISION KEYS / LIMITS
  source_quote: |
    "RESTRICTION: AN ATTENDANT OR A HUNTING GROUP CAN'T BE SUPERVISED" (p262)
    "A set can be supervised by 20 sets maximum • The maximum number of supervisors for a same voice
    mailbox is 100 (20 in a network configuration) ... The total number of supervision keys in the system
    is 15000 • Only one key with the same directory number can be created on a set" (p265)
  summary: |
    上限组：一台话机至多 20 个监督者；同一邮箱至多 100（组网 20）个监督者；全网 15000 把监督键；一话机上
    同号只能一把键。两类对象不可被监督：话务台与寻线组。给客户承诺"全员互监"前先对这组数字。
  conditions: 监督方案设计
  tags: [limitation, supervision-keys, capacity]

- id: n26
  title: 经理/助理前置与互斥——先有多线键、screening/unscreening 不能同时、溢出助理不得已是该经理助理
  type: limitation
  source_pages: p279, p283, p288
  source_chapter: SCREENING/UNSCREENING KEYS / ROUTING ASSISTANT / How-To Notes
  source_quote: |
    "It is not possible to activate a screening and an unscreening key at the same time" (p279)
    "This extension must not already be declared 'assistant' for this manager" (p283)
    "Before to create the Assistant/Manager keys, it is mandatory to create one multi-line key minimum." (p288)
  summary: |
    三条约束：①经理/助理键创建前双方至少各有一把 multiline 键；②screening 与 unscreening 键互斥激活（按
    一类关另一类），但同类多键可并存；③溢出助理（Routing Assistant）每经理仅一名、可服务多经理、但不得已
    是该经理的助理。设计"助理+溢出助理"矩阵时按这三条画表。
  conditions: 经理/助理方案
  tags: [limitation, manager-assistant, screening]

- id: n27
  title: 寻线组一台话机只能属一个组；末位成员退组受开关约束
  type: limitation
  source_pages: p304, p318
  source_chapter: EXIT/ENTER / How-To Warning
  source_quote: |
    "NO (default position): if stations are authorized to be removed from the group the last station
    remaining loose this right (in order to keep the service functioning)." (p304)
    "A SET CAN BELONG TO ONLY ONE HUNTING GROUP" (p318)
  summary: |
    两条结构性约束：①一台话机只能属于一个寻线组（跨组需求用并行组或溢出号拼）；②默认配置下最后一留在组
    内的成员无权退组（保服务）；若把"允许末位退组"打开，来话将转溢出号或忙音——这是有意的服务降级开关，
    不是 bug。
  conditions: 寻线组设计
  tags: [limitation, hunting-group, membership]

- id: n28
  title: 代接前缀默认值的文档自相矛盾（55/56 与 480/481 的 Note 与截图互换）
  type: misconception
  source_pages: p304, p314, p320, p324-325
  source_chapter: EXIT/ENTER / CALL PICK-UP / How-To
  source_quote: |
    p304 图: "480 Group entry • 481 Group exit"（概念章口径）
    p320 Note: "The two prefixes are created by default with the numbers 480 for the 'Sta. Group Entry'
    prefix and 481 for the 'Sta. Group Exit' prefix."（Note 口径，但其上方截图 480 标 Sta. Group exit、481
    标 Sta. Group Entry）
    p325 Note: "The two prefixes are created by default with the numbers 55 for the 'Group call pickup'
    prefix and 56 for the 'Direct call pickup' prefix."（Note 口径，但其上截图 56=Group call pick-up、
    55=Direct call pick-up，且 p314 图为 55+号码=直接代接）
  summary: |
    教材排版事故：进出组（480/481）与代接（55/56）的默认前缀，在 Note 文本与截图/概念图之间存在互换。按
    截图与概念章口径应为：480=组进入、481=组退出；56=组代接、55=直接代接（p314 图 55+31000 为直接代接）。
    现场以 Prefix Plan 实际查询为准（Translator/Prefix Plan 按含义过滤），不要背教材 Note。
  conditions: 进出组/代接配置与排障
  tags: [misconception, prefix, erratum]

- id: n29
  title: 办公桌共享忙时重置默认开启——DSU 会被打断通话并产生 6004
  type: warning
  source_pages: p334, p346, p348
  source_chapter: SYSTEM OPTIONS / How-To
  source_quote: |
    "Allow Reset of Busy DSU True: if a DSU is busy (on line), the call is released and it can be log off
    ... An incident '6004' is generated. • False: ... the conversation is maintained. In case of log on
    from another DSS, a message 'Unauthorized' is displayed." (p346)
    "25/03/22 ... =4:6004=Communication End due to 31000 ... Communication End due to AutoLogoff" (p348)
  summary: |
    Allow Reset of Busy DSU 默认 True：忙线上的 DSU 会被登出并释放通话（6004 事件），另一人即可登录该工
    位——共享效率优先。若客户要求"通话中不许被顶"，要改为 False（代价：忙时无法异机登录、自动登出也会跳
    过）。两个方向的服务承诺要先和客户对齐。
  conditions: 办公桌共享参数设计
  tags: [warning, desk-sharing, incident-6004]

- id: n30
  title: 办公桌共享即时登录的适用面限制——仅 NOE3GEE/Essential/Enterprise 同族同节点无 AOM，IPDSP 不适用
  type: limitation
  source_pages: p336
  source_chapter: SYSTEM OPTIONS（免重启即时登录）
  source_quote: |
    "Restrictions for the 'Instant DS login/logoff' feature • Applicable only for NOE3GEE sets & IP
    Essential/Enterprise Business Deskphones • Not for IP DSP • When both DSS and DSU belong to same NOE
    family • When both DSS and DSU are in same node • When AOM is not configured in DSU/DSS"
  summary: |
    "登录/登出免重启"是个有前提的甜点：只覆盖 NOE3GEE 与 IP Essential/Enterprise 话机，IPDSP 明确排除；
    且要求 DSS/DSU 同 NOE 族、同节点、都未配 AOM。条件不满足时回落为重启式切换（体验是登录要等一轮重启）。
    混合机型办公区要按机型分别承诺体验。
  conditions: 办公桌共享体验设计
  tags: [limitation, desk-sharing, instant-login]

- id: n31
  title: 建多设备关联会清空话机全部数据，且复制到副站的数据不可再改
  type: warning
  source_pages: p366
  source_chapter: Multi devices user How-To Prerequisites
  source_quote: |
    "ON CREATION OF THE MULTI DEVICE ASSOCIATION, ALL DATA (CALL FORWARDINGS, CALLBACKS, MESSAGE DEPOSITS,
    ETC.) ARE CANCELLED ON THE SETS. ... The data copied into the secondary set cannot be modified."
  summary: |
    主副关联是破坏性操作：两台话机上的呼转、回叫、留言等全部清空，然后主站的一组数据（关联号/显示名/各类
    COS/邮箱/实体/成本中心/密码等）复制进副站且此后不可在副站修改。改造存量用户（如从办公桌共享转多设备）
    前先导出/记录话机配置。
  conditions: 多设备/双机改造
  tags: [warning, multi-device, destructive]

- id: n32
  title: 主站退服参数的生效时机——退服期间修改不生效，要等主站恢复后再次退服
  type: limitation
  source_pages: p362, p370
  source_chapter: MAIN SET IS OUT OF SERVICE / How-To Tips
  source_quote: |
    "If you modify the values for these options, they are considered after the next main set status
    change (from in service to out of service)" (p362)
    "When 'forward if set is oos' or 'Overflow to sec tandem if main oos' parameters are modified when the
    Main is OOS, this is NOT taken into account until the Main set returns to service" (p370 Tips)
  summary: |
    三个退服相关参数（Forward if set OOS / Overflow to sec tandem if main OOS / Ring all its secondar.）
    的取值在主站退服状态下被"冻结"：正在退服时改参数不生效，要等主站回到服务、再次退服才按新值走。故障
    现场热改参数救急时别误以为没保存。
  conditions: 多设备主站退服场景
  tags: [limitation, multi-device, oos, timing]

- id: n33
  title: 多设备的监督降级——Specific supervision=True 后监督键不再振铃提示
  type: limitation
  source_pages: p358
  source_chapter: CONFIGURING THE SPECIFIC SUPERVISION
  source_quote: |
    "The supervision of the multi-equipment set becomes a state supervision, that means that the
    supervisor only sees if the set is occupied or if it is free (no longer sees the ringing and partial
    occupancy states)."
  summary: |
    多设备用户打开 Specific supervision 后，监督方只看到占用状态（按键显示 MAIN/SECONDARY/TOTAL BUSY），
    不再看到振铃与部分占用状态，按键也不再呼叫而是显示占用。对秘书/老板场景这是行为变化，要在配置前讲清
    楚（它是为 tandem 关联特化的监督语义，不是故障）。
  conditions: 多设备 + 监督组合
  tags: [limitation, multi-device, supervision]

- id: n34
  title: Direct IP Link 系统选项不可逆——Enabled 后只能靠库恢复回退；Migrating 态必须重启
  type: version-trap
  source_pages: p403
  source_chapter: '"Direct IP Link" system option'
  source_quote: |
    "This is an irreversible value : once in 'Enabled', it is not possible to change system option
    anymore. If reverting the process is mandatory, only restoration of database can handle this."
    "OXE REBOOT IS REQUIRED ('SHUTDOWN -R NOW') TO TAKE INTO ACCOUNT THIS PARAMETER"
  summary: |
    启用直链是一次性决策：Disabled→Migrating 必须重启一次，再切 Enabled（免重启）；Enabled 后系统选项不
    可改回，唯一回退是恢复数据库备份。上线直链前把回退预案（库备份+回滚窗口）写进变更单。
  conditions: Direct IP Link 启用变更
  tags: [version-trap, direct-ip-link, irreversible]

- id: n35
  title: 直链两端一致性硬约束——带宽/加密/接入数不对称即 2879 拒建或行为异常
  type: warning
  source_pages: p405, p409
  source_chapter: Logical Links Consult / 接入 Notes
  source_quote: |
    "IP BANDWIDTH RATE, ENCRYPTION AND NUMBER OF ACCESSES MUST HAVE THE SAME VALUE ON BOTH ENDS OF THE
    LINK. IF THEY ARE CHANGE IN AN ASYMMETRIC MANNER WHILE LINK IS ESTABLISHED, BEHAVIOUR MIGHT BE
    ERRATIC. IF THEY ARE DIFFERENT AT STARTUP, THEY WON'T ESTABLISH, AND INCIDENT 2879 IS RAISED" (p405)
    "Before enabling the link again, one must ensure that the number of accesses declared for this link
    on the adjacent node is the same. If it is not the case, the link will not be established." (p409)
  summary: |
    两端对称三条：带宽档（High/Low）、加密、接入数。启动时不一致 → 链路起不来并抛 2879；运行中改成不对称
    → 行为异常（ERRATIC）。增删接入的正确姿势：任一接入上先 Disable Direct Link synchro（整链断开）→改
    两端→重新 Enable；只改一端就 Enable 必然失败。
  conditions: 直链接入维护
  tags: [warning, direct-ip-link, incident-2879, symmetry]

- id: n36
  title: 直链无中继无透明溢出——IP 断链时话务层不绕行，靠网络设计兜底
  type: limitation
  source_pages: p386
  source_chapter: OVERVIEW（失败语义）
  source_quote: |
    "No overflow is handled at telephonic application level, in case IP connectivity between two nodes is
    lost • Routing is always direct • OXE does not select another route to reach the destination ... No
    concept of transit node • Only private to public trunk overflow may be used, when it is managed"
  summary: |
    直链是"直连语义"：节点间没有中转节点概念，某节点 IP 故障即孤立（不产生 ABCF 话务，也没有 IP/SIP 话
    务），其他节点间照常互打；话务层不做绕行——唯一的退路是配置了私到公溢出时的公网绕行。这把"IP 网络本
    身要按单点故障不影响全互联来设计"变成了直链方案的前置假设，方案评审必须核这条。
  conditions: 直链组网设计
  tags: [limitation, direct-ip-link, overflow, network-design]

- id: n37
  title: 直链迁移前提清单——全网 ≥N1、子网内无 TDM ABC-F、hybrid 仅限 IP 信令/无信令、无备份信令；homogeneous 开关差异
  type: limitation
  source_pages: p385, p388, p391-392
  source_chapter: OVERVIEW / TOPOLOGY BEFORE MIGRATION / NETWORKING
  source_quote: |
    "All nodes of the subnetwork are updated to release N1 or higher • There must be no more TDM ABC-F
    links within the subnetwork ... • Only hybrid links with IP signalling (only 1 access) or without
    signalling ... can be configured • No Standby signalling must be configured for hybrid links." (p388)
    "'Homogeneous network for Direct RTP' is ENABLED (in IP Trunk Group)" (p391)
  summary: |
    迁移门槛四条：全网 ≥N1；子网内清光 TDM ABC-F（过渡期可用 hybrid+VPN hop 顶替）；hybrid 链只允许"仅 IP
    信令（1 接入）"或"无信令"两种，且不得配备份信令；直链子网禁止再建 hybrid/TDM 链（本地 hybrid 链保留
    不迁移）。跨子网互通还有开关差异：全同构/部分迁移网要开 IP Trunk Group 的 Homogeneous network for
    Direct RTP，异构网（含 TDM/低版本）关掉并接受压缩机接续。
  conditions: hybrid+VPN 向直链迁移项目
  tags: [limitation, direct-ip-link, migration, prerequisite]

- id: n38
  title: 直链配套限制——免许可但禁 IP Premium Security、不能 SNMP 监管、链名 Link_xx 不可管理
  type: limitation
  source_pages: p397, p404
  source_chapter: MISCELLANEOUS / Fully meshed network
  source_quote: |
    "IP Premium Security not allowed in a 'Direct IP Link' based ABC-F network • ABC-F Direct IP Links
    cannot be supervised via SNMP" (p397)
    "The names of previously existing links are changed. When direct link is enabled, all links (except
    local hybrid) are named Link_xx ... They are no more manageable" (p397)
  summary: |
    三条能力收缩：直链网络里不能用 IP Premium Security；直链不支持 SNMP 监管（网管平台要换 hybvisu/trkvisu
    或事件采集）；启用直链后全部链路改名 Link_xx（对端节点号）且不再可管理（含改名/手调）。运维监控与安
    全方案的调整要前置。
  conditions: 直链网络运维
  tags: [limitation, direct-ip-link, snmp, security]

- id: n39
  title: Audit 直改数据库——必须先模拟、强烈建议全网备份；链式对象要跑两遍
  type: warning
  source_pages: p435, p442
  source_chapter: ENCOUNTERED PROBLEMS / PRECAUTION
  source_quote: |
    "Audit modifies directly database tables • In case of error, old data doesn't exist anymore • To limit
    the risks, it's mandatory to use simulation mode" (p442)
    "IT IS HIGHLY RECOMMENDED TO SAVE THE DATABASE OF ALL NODES BEFORE STARTING THE AUDIT" (p442)
    "the system will refuse the creation of an attendant ... To deal with this problem ... 1- Do a partial
    audit ... 2- Do a global audit twice" (p435)
  summary: |
    audit 不是"只读检查"：它直接改表、旧数据不留。安全阀三件套——模拟模式（工作在表副本）先行、全网库备份
    再跑、链式对象（话务台/实体/呼叫分配/编号计划互相引用）首跑报错属已知问题，按"部分审计（编号计划+实体
    +话务台+组+分配）→全局审计"或"全局审计跑两遍"处理。
  conditions: 全网 audit 执行
  tags: [warning, audit, destructive, backup]

- id: n40
  title: Audit 前提按地址逐条配——物理+twin 物理+主角色+第二主地址，漏一类即断
  type: warning
  source_pages: p436, p447
  source_chapter: AUDIT PREREQUISITES / How-To
  source_quote: |
    "it is mandatory to configure the internal firewall of each node in order to allow the connection to
    all the remote OXEs CS: • Physical IP address ... • Physical IP address of each remote twin Call
    Server (if exists) • Main IP address (role address) • Second main IP address ... (in case of spatial
    redundancy)" (p436)
    "DON'T FORGET TO DO THE CONFIGURATION ON NODE 2" (p447)
  summary: |
    audit/broadcast 的防火墙前提是"四类地址全放行"：对端物理地址、对端 twin 物理地址、主角色地址、空间冗
    余第二主地址——只放物理地址是典型漏配；且配置是双向的（NODE2 也要配，教材专给 Warning）。排障顺序：先
    核对两侧 trusted hosts 与 /etc/hosts，再查 SSH 密钥。
  conditions: audit/broadcast 准备
  tags: [warning, audit, firewall, bidirectional]

- id: n41
  title: Broadcast 不是即时同步——默认 10 分钟 buffer 周期，急事要手动 Immediate Broadcast
  type: limitation
  source_pages: p474, p484, p492
  source_chapter: THE BUFFER FILE / IMMEDIATE BROADCAST / How-To
  source_quote: |
    "The content of the buffer file is emptied and stred every 10 min into a LOG file (the timer can be
    modified)" (p474)
    "For some reasons, it is necessary to force the broadcast by applying an 'immediate broadcast'" (p484)
  summary: |
    修改先落在 buffer 文件，默认每 10 分钟才落成 LOG 并广播——两个节点先后改数据，另一侧要等周期。验收测
    试或割接时用 WBM 的 Immediate Broadcast 按钮立刻冲刷。以为"配完即全网生效"会产生大量假故障工单。
  conditions: broadcast 日常运维与验收
  tags: [limitation, broadcast, timing]

- id: n42
  title: Broadcast 的对象盲区——trunk group 前缀/ARS 表/IP 域/DHCP 内容/本地范围缩拨号不广播
  type: limitation
  source_pages: p485, p505
  source_chapter: RESTRICTIONS / NODE ACCESS PREFIX
  source_quote: |
    "List of objects not broadcasted: • Trunk groups prefixes and ARS tables • IP domains • Content of
    embedded DHCP server • Speed dialling • ... Local range: no broadcast • Network range: broadcast of
    the ranges and numbers" (p485)
    "'number to add' • Not broadcasted" (p505)
  summary: |
    广播不覆盖的对象要逐节点手工配：trunk group 前缀与 ARS 表、IP 域、嵌入式 DHCP 内容、本地范围缩拨号（网
    络范围缩拨号会广播）；溢出方向上 Node Access Prefix 的 Number to add（本地 ARS 前缀）也不广播。新建或
    重装节点后，这些"本地对象"漏配是全网业务不通的高频根因。
  conditions: 节点新增/重装与 audit/broadcast 后核验
  tags: [limitation, broadcast, out-of-band, checklist]

- id: n43
  title: 广播失败的痕迹是 RLOG——重复号码等远端写失败要主动排查
  type: limitation
  source_pages: p477, p495
  source_chapter: '"LUPD.DAT" FILE / How-To LOG and RLOG'
  source_quote: |
    "One 'RLOG' file is generated whenever a modification cannot be made on a distant node • Duplicate in
    mao for example" (p477)
  summary: |
    远端节点应用 LOG 失败（典型如对端已有同号用户）时不弹告警到眼前，而是生成 RLOG 文件等人工处理——广播
    表面"完成"、数据实际分叉。巡检动作：/usr4/mao 下查 RLOG*、prog_diff 菜单 1 读错误文件、菜单 2 核对远
    端序号。
  conditions: broadcast 巡检
  tags: [limitation, broadcast, rlog, silent-failure]

- id: n44
  title: 私到公溢出的"被叫显示"变化——对方看到的是公网 ID；block mode 下主叫要等确认
  type: limitation
  source_pages: p223, p506, p514
  source_chapter: ACCESS TO THE SERVICE / How-To Test
  source_quote: |
    "The display of the called party corresponds to the 'public id' of the called party. (if 'block mode'
    is used to set up this kind of call, the caller has to validate the call establishment or wait for the
    'end dialing' timer)" (p223)
    "As soon as the internal called number (31500) is entered, if the Direct IP link is not usable, the
    corresponding translated external DID number is displayed on the caller (31000) screen" (p514)
  summary: |
    溢出呼叫的两点体验差异：①被叫侧看到的是主叫的公网 ID 而非内部分机名（反之主叫拨的还是内号，屏显却变
    成翻译后的外号）——用户报"来电显示不对"先想溢出路径；②block mode 拨号时主叫需确认或等位间计时器，呼
    叫建立比内网慢。客户体验说明要写进割接通知。
  conditions: 溢出呼叫体验
  tags: [limitation, overflow, display, user-experience]

- id: n45
  title: 公到私重路由仅覆盖 DID 被叫；-1 路由每表一条且必须首位
  type: limitation
  source_pages: p522
  source_chapter: RESTRICTIONS
  source_quote: |
    "None DID sets are not taken into account by this feature ... Only one ARS route with this value per
    table • This route must be in first position in the table"
  summary: |
    两条硬边界：①非 DID 被叫不参与公到私重路由（外拨其第三方号不会折回专线）；②Trunk Group=-1 的重分析路
    由每张 ARS 表只能有一条且必须放首位——排在后面不生效。ARS 表设计时把"直链还原路由"钉在第一位，公网
    兜底路由排其后。
  conditions: 公到私重路由配置
  tags: [limitation, rerouting, ars, did]

- id: n46
  title: 教材实验值版本漂移——同一台 PCS 在两章显示不同软件版本
  type: limitation
  source_pages: p187, p212
  source_chapter: PCS How-To Requirements / Network breakdown
  source_quote: |
    p187: "Active version : R101.1-n4.523-0-fr-c0s1"
    p212: "Active version : R101.1-n4.205-19-fr-c0s1 ... Inactive version : R101.1-n4.205-3-fr-c0s1"
  summary: |
    同一实验环境的 PCS VM，在部署章与断链章的 mtcl 欢迎信息里分别显示 n4.523 与 n4.205 批次——教材截图来
    自不同时期的环境。引用本书输出做版本比对基线时，以现场实际欢迎信息为准，勿把书中具体 build 号当标准。
  conditions: 版本核对与排障引用
  tags: [limitation, version-drift, evidence]

- id: n47
  title: RLAB 防火墙为"部分配置"教学口径——生产防火墙基线书内未给
  type: out-of-scope
  source_pages: p49, p94, p378
  source_chapter: OXE Preconfiguration / How-To firewall
  source_quote: |
    "OXE CS firewall is partially configured (all PCs, all OMS, the GD4, NTP server, the gateway, the
    DHCP ranges)" (p49)
  summary: |
    实验环境的防火墙只放行了教学所需对象（PC/OMS/GD4/NTP/网关/DHCP 段），bulk 文件也是实验口径。生产系统
    的防火墙基线（放行清单、最小权限、证书管理）不在本书范围——交付时按安全技术文档另行设计，别把"能跑通
    实验"当成"安全达标"。
  conditions: 安全基线设计
  tags: [out-of-scope, security, firewall, lab]

- id: n48
  title: Starter 内容外置——ARS、闭锁、装机、GD/OMS SSH 方法均为书外前置
  type: out-of-scope
  source_pages: p110, p134, p229, p525
  source_chapter: 各 How-To 的 Warning/Note
  source_quote: |
    "REFER TO STARTER TRAINING TO KNOW THE PROCEDURE TO SET UP A SSH CONNECTION TO THE GD BOARD" (p110)
    "ARS MANAGEMENT ... IS NOT DETAILLED IN THIS PROCEDURE (ALREADY EXPLAINED IN THE STARTER TRAINING)" (p229)
    "you need to master the 'call barring' topic (explained in the starter training)" (p525)
  summary: |
    本书的四个高频书外依赖：GD/OMS 的 SSH 连接方法（冗余/PCS 章反复引用）、ARS 基础（溢出/重路由强前置）、
    闭锁规则（重路由前置）、swinst/netadmin/空库/autostart 基本操作（PCS 初始化引用）。学员或交付者缺
    Starter 功底时，本书一半实验无法独立完成。
  conditions: 学习路径与交付准备
  tags: [out-of-scope, starter, prerequisite]

- id: n49
  title: 直链容量数字是"每链/每节点"口径，不可当全网容量承诺
  type: misconception
  source_pages: p395, p406
  source_chapter: LIMIT/PROVISIONING LEVEL / How-To 全局上限
  source_quote: |
    "1488 simultaneous calls maximum on a direct call ... approximately 10000 calls per Direct IP link
    (with 8 accesses) per hour" (p395)
    "Maximum number of IP calls Default Value: -1 (range: -1 .. 32767) ... overall on all direct IP link,
    SIP trunk and ABCF-IP trunk on this node. When maximum is reached ... An incident 6005 is edited" (p406)
  summary: |
    三层数字别混：1488=单链并发上限（24 接入×62 通道）；10000 呼/时=单链话务能力（8 接入口径的工程值）；
    节点级还有一个覆盖 direct+ SIP trunk + ABCF-IP trunk 的全局呼叫上限（默认 -1 不限，超限 6005）。售前
    若把 1488 当"节点容量"或忽略节点级全局上限，都会算错规模。
  conditions: 组网容量测算
  tags: [misconception, direct-ip-link, capacity, formula]

- id: n50
  title: 话机型号边界散落在特性章——监督/多设备/办公桌共享各有支持面
  type: limitation
  source_pages: p329, p354, p359, p336
  source_chapter: DESK SHARING / MULTI DEVICE / 振铃控制
  source_quote: |
    "Feature available for • 8 series IP Touch EE devices • IP Premium Deskphones • IP Essential Business
    Deskphones • IP Enterprise Business Deskphones • IP Desktop Softphones" (p329)
    "SUPPORTED ONLY FOR IP/TDM NOE SETS • NOT FOR DECT SETS, SIP EXTENSIONS OR REMOTE EXTENSIONS" (p359)
  summary: |
    特性×机型矩阵要在售前对表：办公桌共享覆盖 8 系列 EE/IP Premium/Essential/Enterprise/IPDSP；多设备副
    站的静音振铃仅 IP/TDM NOE（DECT/SIP/REX 不适用，REX 走 651 前缀）；即时登录仅 NOE3GEE/Essential/
    Enterprise（IPDSP 除外）。混机型项目按"最弱机型"定体验承诺。
  conditions: 特性选型
  tags: [limitation, handset-matrix, desk-sharing, multi-device]
```

---

## 收尾自检 — 对照 BOOK_OVERVIEW.md 21 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | 集中式 IP Pod 配置 | 有 → n01（启动顺序/IP 冲突）、n47（防火墙教学口径） |
| task-02 | SSH 免密体系 | 有 → n02（host-based 移除） |
| task-03 | 本地冗余部署 | 有 → n04（同版本/重启）、n05（mastercopy 三前提）、n06（Linux 数据不复制） |
| task-04 | 空间冗余部署 | 有 → n09（DNS 三坑）、n40（四类地址放行） |
| task-05 | 冗余维护与切换演练 | 有 → n03（IP 高者成 main）、n07（double main 服务缺失）、n08（120 分钟/440） |
| task-06 | 不停机升级 | 有 → n08（升级失败的兜底即 mastercopy）、n05 |
| task-07/08 | IP 域配置与验证 | 有 → n10（域 0 硬规则）、n11（掩码/复位）、n16 相邻（PCS 域 0 同规则） |
| task-09 | PCS 部署 | 有 → n12（无 MG 域）、n13（console 首配）、n14（pcscopy 前提）、n15（单向/手工参数） |
| task-10 | PCS 救援与回切演练 | 有 → n16（30 天）、n17（能力边界）、n19（断链锁门） |
| task-11 | 本地私到公溢出 | 有 → n20（SIP 不适用/话务台恒放）、n21（RLAB 不可做）、n22（字段三坑）、n44（显示体验） |
| task-12 | 速拨体系 | 有 → n23（闭锁默认关/4000 上限） |
| task-13 | 多线与监督键 | 有 → n24（空闲号）、n25（上限与不可监督对象） |
| task-14 | 经理/助理组 | 有 → n26（三约束） |
| task-15 | 寻线/代接组 | 有 → n27（一组一台/末位退组）、n28（前缀 erratum） |
| task-16 | 办公桌共享 | 有 → n29（忙时重置 6004）、n30（即时登录适用面）、n50（机型矩阵） |
| task-17 | 多设备用户 | 有 → n31（破坏性关联）、n32（参数冻结时机）、n33（监督降级）、n50 |
| task-18 | Direct IP Link 组网 | 有 → n34（不可逆）、n35（2879 对称）、n36（无中继语义）、n37（迁移前提）、n38（配套限制）、n49（容量口径） |
| task-19 | Audit | 有 → n39（直改表/跑两遍）、n40（四类地址） |
| task-20 | Broadcast | 有 → n41（10 分钟周期）、n42（对象盲区）、n43（RLOG 静默失败） |
| task-21 | 组网双向溢出 | 有 → n44（显示/计时）、n45（DID 与 -1 路由）、n42（Number to add 不广播） |
| 横切 | 版本与证据 | 有 → n46（截图版本漂移）、n47/n48（安全与 starter 外置） |

**21/21 全部有边界类条目覆盖，另加两条横切条目。**

### 扫描完整性说明（Warning/Note/Tips 框逐页核对）

- 已入册的全大写 Warning 框：p47/p375（IP 冲突）、p94/p117（同版本同平台）、p97/p99/p120/p122（netadmin 后关机）、p108/p132（BE PATIENT）、p152（域 0）、p158（掩码/复位）、p169（无 MG 域）、p179（单向同步）、p180（手工参数）、p199（PCS 域 0）、p203（oxe-ssh-auth pair 需跑两遍）、p212（断链锁门）、p229（RLAB 不可做）、p230（Install No Last Part 留空）、p231（外号不重叠）、p262（话务台/寻线组不可监督）、p269（空闲号）、p318（一组一台）、p366（关联清数据）、p403（Migrating 重启/不可逆）、p405（两端一致 2879）、p420-422（audit 参考节点选择与第二阶段必要性）、p442（模拟+备份）、p488（broadcast 前提）。
- 已入册的 Note/Important/Tips：p75/p105（IP 高者防御）、p79（440）、p82（double main 服务缺失）、p88-90（DNS/DHCP）、p133（spatial DHCP）、p136（内部解析器强制）、p178（PCS 地址不可混用）、p182（30 天）、p183（限制清单）、p190-192（pcscopy hosts）、p195（copy to twin）、p225-226（OoS 溢出/SIP 不适用）、p236/247（闭锁默认/4000）、p279/283/288（助理三约束）、p304（末位退组）、p320/325（Note 与截图互换，n28 立条）、p334-336（办公桌共享选项）、p346（6004）、p362/370（退服参数冻结）、p385-388/391-392（直链迁移前提与开关）、p386（无中继语义）、p397（直链三限制）、p404（99 链/显示过滤）、p409（接入数一致）、p417（事件组）、p435（跑两遍）、p436/447（四类地址+NODE2）、p474-477（buffer/RLOG）、p485（不广播对象）、p505（Number to add 不广播）、p522（-1 路由规则）、p370 Tips（参数时机）。
- 排除的纯操作提示（非边界类）：p11/p16/p26/p31（ENTP NAS 网络盘说明）、p51/p52（IPDSP TFTP 设置教学图）、p100-103/p123-126（authorized_keys 全文粘贴，属实验输出非边界）、p299-302（搜索类型原理图说明）、p395（性能口径已并入 n49/p39）、p538-543（培训评估流程，BOOK_OVERVIEW 已列为不入册）。
- 推断性结论已在条目内标注"（推断）"：本次无推断性结论条目——n28 的"以截图与概念章口径为准"是对教材内部矛盾的直接文本比对，非推断。
- 版本号按原文保留完整位数：R101.1（MD4）、N3、R100.0（Purple）、N1、R9、R101.1-n4.523/n4.205（实验 build）。
