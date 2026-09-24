# 原则/清单/规则/公式/数值口径候选 — OmniPCX Enterprise Advanced (ENTPXTE401EN Ed13, R101.1 MD4)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号、号码）均标注"实验口径"，生产化需替换。版本号按原文保留完整位数（R101.1、N3、R100.0、N1、R9 等）。

```yaml
- id: p01
  title: SSHv2 公钥认证自 N3 起为默认；host-based 认证因 CIS 合规被移除
  type: rule
  source_pages: p57
  source_chapter: SSH Key Distribution / Overview
  source_quote: |
    "From N3 onwards, for security reasons SSHv2 is enabled by default with public key authentication.
    • OXE administrator accounts like mtcl, swinst and root will have unique SSH keys for each OXE CS.
    • Host based authentication is no longer supported, thanks to CIS compliance requirements."
  summary: |
    三条基线：从 N3 版本起 SSHv2 + 公钥认证默认启用；mtcl/swinst/root 三个管理员账户在每台 OXE CS 上各
    持独立密钥对；基于主机的认证（host-based）已因 CIS 安全合规要求不再支持。mastercopy、pcscopy、audit、
    broadcast 都依赖免密，密钥未分发这些功能必失败。
  conditions: 适用于所有协同机制部署前
  tags: [rule, ssh, security, version]

- id: p02
  title: oxe-ssh-auth 使用规则：root 权限、先查后同步、双向生效、口令可复用
  type: checklist
  source_pages: p59-60, p101, p124, p203, p447
  source_chapter: SSH KEY DISTRIBUTION / 各 How-To
  source_quote: |
    "This tool must be run from an OXE in N3 for synchronizing the SSH keys between two OXE CS. ...
    The tool requires the root privileges • Some inputs are required ... Remote CS IP address, local and
    remote accounts (mtcl, swinst, root) passwords" (p59-60)
    "Before starting the synchronization, the tool checks if passwordless connectivity already exists
    ... and starts synchronizing the keys only if it does not exist already." (p60)
    "Do you want to apply the same password to all accounts(mtcl, swinst, root) in local & remote nodes
    ? (y/n) default(y): y" (p101)
  summary: |
    操作清单：以 root 登录执行 `oxe-ssh-auth -c <远端CS IP>`；工具先检查双向免密是否已存在，已同步则跳
    过；需输入远端 mtcl 密码，并可选"同一密码套用本地与远端全部三账户"（默认 y，否则逐账户输入）；完成后
    输出 All Done OK!!!，验证方法是 more /usr2/mtcl/.ssh/authorized_keys 应同时含本地与远端公钥。该工具
    只处理"一对"OXE。
  conditions: N3+；两 CS 防火墙互信
  tags: [checklist, ssh, oxe-ssh-auth]

- id: p03
  title: oxe-nw-sshkey-sync 使用规则：CSV 五段格式、每节点各跑一次、结束自动清理
  type: rule
  source_pages: p62-66, p203, p206
  source_chapter: SSH KEY DISTRIBUTION / PCS How-To
  source_quote: |
    "Usage: oxe-nw-sshkey-sync –f <.csv file> ... <Main CS IP Address, Node X>,<mtcl password>,<swinst
    password>,<root password>,<log file>" (p64)
    "it is enough if the administrator runs the 'oxe-nw-sshkeys-sync' tool just once from each node of
    the network" (p63)
    "Password CSV file ssh_multi.csv, Config(/tmpd/config) folders are cleared ! Done !!!" (p206)
  summary: |
    CSV 每行五段逗号分隔：<IP 地址,节点名>,<mtcl 密码>,<swinst 密码>,<root 密码>,<日志文件>，覆盖主 CS/
    物理 CSA/CSB/PCS 1..240/4645；从主 CS 运行时自动按 MAO 数据推导 twin、PCS、网络节点、网络节点 twin、
    4645 清单，先同步主 CS 再同步 twin CS；全网每节点各跑一次即可。日志写 /tmpd/logs/oxenwsync.log；运行
    结束自动删除 csv 与 config（凭证不留盘），归档打包为 /tmpd/oxenwsynclogs.zip（root 解压后查日志）。
  conditions: root 权限；节点间防火墙互信
  tags: [rule, ssh, csv, oxe-nw-sshkey-sync]

- id: p04
  title: SSH 密钥存储路径表（mtcl/swinst/root 三账户）
  type: metric
  source_pages: p67
  source_chapter: SSH KEY DISTRIBUTION / Storage
  source_quote: |
    "Keys for « mtcl » account • Public key: /usr2/mtcl/.ssh/id_rsa.pub • Private key:
    /usr2/mtcl/.ssh/id_rsa • Keys for « swinst » account • Public key: /usr2/soft_install/bin/.ssh/
    id_rsa.pub ... • Keys for « root » account • Public key: /root/.ssh/id_rsa.pub • Private key:
    /root/.ssh/id_rsa" (p67)
  summary: |
    逐格路径：mtcl——公钥 /usr2/mtcl/.ssh/id_rsa.pub、私钥 /usr2/mtcl/.ssh/id_rsa，授权表
    /usr2/mtcl/.ssh/authorized_keys；swinst——/usr2/soft_install/bin/.ssh/id_rsa(.pub)；root——
    /root/.ssh/id_rsa(.pub)。核验同步结果的标准动作：more /usr2/mtcl/.ssh/authorized_keys（三机全网场景
    应各有 9 条 = 3 节点 × 3 账户；两机为 6 条）。
  conditions: 授权表文件名 authorized_keys
  tags: [metric, ssh, storage, paths]

- id: p05
  title: 冗余对两条铁律 + 切换语义（已建立保持、建立中丢失）+ 实时复制走 scp
  type: rule
  source_pages: p70-71, p94, p117
  source_chapter: CS DUPLICATION / How-To Warning
  source_quote: |
    "The 2 Call Servers must have the same type, and the same software release" (p70)
    "If the Main call server fails, the system switches to the standby one (which becomes Main):
    • Calls already established are maintained • Calls being connected during switch-over are lost" (p71)
    "The standby Call Server database is updated in real time ... Updates must be done with a 'secured
    copy protocol' (scp)" (p71)
    "CALL SERVERS MUST HAVE THE SAME SOFTWARE VERSION AND BE IMPLEMENTED ON IDENTICAL PLATFORMS" (p94, p117)
  summary: |
    规则组：①同软件版本 + 同类平台（CS 板卡/GAS/VM 同型）是 How-To 全大写警告；②主库实时复制到备机，传
    输用 scp；③切换时已建立通话保持、正在建立的通话丢失；④SSH 公钥必须先在主备间分发（库复制授权前提）。
  conditions: 主备间需 IP 链路
  tags: [rule, duplication, switchover, scp]

- id: p06
  title: 冗余 IP 链路承载清单 + netadmin Linux 数据不复制（Copy to Twin 例外）
  type: checklist
  source_pages: p74
  source_chapter: IMPLEMENTATION
  source_quote: |
    "It handles: The 'keep alive' messages exchange ... MAO (telephonic database) • Traffic observation
    • Accounting records • CCD data • LINUX data managed by 'swinst' • Note: LINUX data managed by
    netadmin are not duplicated (manual update is required: 'Copy to Twin' option) • Information from
    neighboring nodes (via the broadcast mechanism) • ACTIS files" (p74)
  summary: |
    IP 链路承载 8 类：keep-alive、MAO 电话库、话务观察、话单、CCD 数据、swinst 管的 Linux 数据、邻居节点
    信息（广播机制）、ACTIS 文件；另加参考 MG 声明（见 p07）。关键例外：netadmin 维护的 Linux 数据（如内
    部防火墙）不随库复制——要么 netadmin→Copy setup→Copy to twin CPU，要么 mastercopy 时勾 LINUX DATA。
    教材实验即用后法把 csa 防火墙带到 csb（p108/p132 Note）。
  conditions: Copy to Twin 在 netadmin 菜单 10 'Copy setup'
  tags: [checklist, duplication, ip-link, netadmin]

- id: p07
  title: 参考 MG 裁决规则：断链时连它的一侧保留管理权，恢复后另一侧重启
  type: rule
  source_pages: p74, p76-77
  source_chapter: IMPLEMENTATION / SWITCH OVER MECHANISM
  source_quote: |
    "When the IP link between the CPUs goes down, the main call server connected to the reference Media
    Gateway continues to authorize management (and broadcast) • When the IP link between the CPUs is
    restored, the call server that is not connected to the reference Media Gateway is rebooted." (p74)
    "The 'Reference Media Gateway' is used in this case to determine the Real Main on which will be
    activated the MAO (management)" (p76)
  summary: |
    double main 场景的裁决规则：参考 MG 是预先声明的一台媒体网关（实验口径为离 CS 最近的 OMS，MG #4，
    /Shelf/ → Reference YES）；两 CS 都失联时，连接参考 MG 的一侧成为 Real Main（MAO 开），另一侧为
    Pseudo Main（MAO 关）；链路恢复后未连参考 MG 的 CS 自动重启并回到 standby。
  conditions: 每 CS 必须配至少一台参考 MG；恢复后需检查是否需 mastercopy
  tags: [rule, redundancy, reference-mg, double-main]

- id: p08
  title: 角色初始化次序：MAO preferred CS IP 优先，未配置则 IP 高者成 main
  type: rule
  source_pages: p75, p104-105
  source_chapter: CALL SERVER ROLE INITIALIZATION / How-To
  source_quote: |
    "Preferred CS IP @: used to define which of the two Call Servers fulfils the Main role when they
    appear together on the network ... If the 'Call server role' is not correctly defined, the CS with
    the highest IP address starts in Main role" (p75)
    "If this parameter is not configured, the Com Server with the highest IP address becomes main." (p105)
  summary: |
    角色确定次序：两 CS 同时上线时，先按 MAO /IP/ 的 Preferred CS IP @（redundancy）参数定 main；该参数
    未配置时，IP 地址较高的 CS 自动成为 main（防御性行为）。实验口径：csa=192.168.1.1 为主。
  conditions: 参数路径 /IP/ Preferred CS @IP (redundancy)
  tags: [rule, redundancy, role, ip]

- id: p09
  title: 主备失联容忍窗口：默认 120 分钟（可配 0-120），超时触发 440 事件必须 mastercopy
  type: metric
  source_pages: p79
  source_chapter: DATABASE CONSISTENCY
  source_quote: |
    "Limited time: 120 minutes by default • /IP/Duplication Parameters/Updates storage time limit
    (0 to 120 minutes) ... After storage time limit: history of MAO commands is deleted and incident
    « 440 » is triggered. A database cloning operation, also called 'Mastercopy', is then necessary !"
  summary: |
    数值口径：备机不可达时主库保存 MAO 命令历史的时间上限默认 120 分钟，参数路径 /IP/Duplication
    Parameters/Updates storage time limit，取值 0-120 分钟；超时后历史删除并触发 440 事件，唯一修复手段
    是 mastercopy 克隆。运维含义：备机宕机修复要赶在窗口内。
  conditions: mastercopy 前须停备机电话应用、已分发 SSH 密钥
  tags: [metric, duplication, incident-440, mastercopy]

- id: p10
  title: double main 模式的服务缺失清单
  type: limitation
  source_pages: p82
  source_chapter: MISCELLANEOUS
  source_quote: |
    "Services not provided in Double Main mode: • Accounting (tickets generated on the Pseudo Main can
    not be reported on the other call server) • Traffic observation (same thing) • One part of the
    network has no Voice Mail"
  summary: |
    double main 期间三件事不可用：话单（Pseudo Main 产生的票据不会汇总到另一 CS）、话务观察（同上）、部分
    网络无语音邮箱。空间冗余（两 CS 分不同子网）是受支持特性，但 double main 本质是故障态，要靠参考 MG 与
    链路恢复机制尽快收敛。
  conditions: IP 链路中断期间
  tags: [limitation, double-main, accounting]

- id: p11
  title: 不停机升级 11 步序列（备机先行、克隆库、bascul 轮换）
  type: checklist
  source_pages: p83
  source_chapter: UPGRADING WITH A STATIC OR DYNAMIC PATCH WITHOUT INTERRUPTING SERVICE
  source_quote: |
    "1. Stop the telephone application on the standby Com Server • 2. Load the new software version
    onto this CS. ... 4. Update the databases (swinst tool: Cloning databases) • 5. Restart the
    telephone on this CS • 6. Switch over the CS (bascule command) • 7. Stop the phone on the second CS
    ... 11. Restart the telephone on this CS"
  summary: |
    11 步：①备机停话音→②装新版本（系统提示两机版本不同）→③无话音重启→④swinst 克隆数据库→⑤重启话音
    →⑥bascul 切换（原备机变 main）→⑦原主机停话音→⑧装新版本→⑨无话音重启→⑩克隆数据库→⑪重启话音。全程
    业务由当前 main 承载，无服务中断窗口。
  conditions: 依赖冗余已就绪（twin 全 READY）；步骤顺序不可颠倒
  tags: [checklist, upgrade, bascul, swinst]

- id: p12
  title: 空间冗余 DNS/DHCP/TFTP 适配规则（内部 DNS 仅主应答、委派、双 TFTP、活动 CS 应答 DHCP）
  type: rule
  source_pages: p88-90, p136
  source_chapter: SPATIAL REDUNDANCY（概念与 How-To）
  source_quote: |
    "The CS has an internal DNS server that answers to a 'node name' request with its own main IP
    address • Only the active main CS answers to the DNS requests ... Ensure that this information is
    not cached" (p88)
    "A DNS delegation is required. e.g. : oxe.company.com => 192.168.1.3 & 192.168.2.3" (p89)
    "Only the active CS answers to the DHCP requests and fills in the tftp server field with its own
    main role IP address • In case of external DHCP server, this one must be able to send two tftp
    addresses" (p90)
  summary: |
    四条规则：①OXE 内部 DNS 只由活动主 CS 应答节点名请求；无网内 DNS 时把两台主地址配成 SIP 设备的主/备
    DNS 并确保不缓存；②有客户 DNS 时必须做 DNS 委派，把节点名指向两个主地址（例 oxe.company.com →
    192.168.1.3 & 192.168.2.3），且 OXE 内部 DNS 解析器必须启用（netadmin）以回应客户 DNS 的查询（p136）；
    ③IP 话机/GD/GA/INTIP/8770 可填两个主角色地址（TFTP #1/#2、CPU role / CPU redundancy role 地址）；④
    DHCP 由活动 CS 应答并填自己的主地址；外部 DHCP 服务器必须能下发两个 tftp 地址。
  conditions: SIP 应用必须用节点名 FQDN（如 sip:31000@oxe.company.com）
  tags: [rule, spatial-redundancy, dns, dhcp, tftp]

- id: p13
  title: 编解码选择链：高带宽 OPUS SWB>WB>G722>G711>OPUS NB>G729；低带宽 OPUS NB>G729；跨域取低档；G722/OPUS 媒体需 OMS
  type: rule
  source_pages: p147-148, p156
  source_chapter: VOICE & SIGNALLING / CODECS SELECTION
  source_quote: |
    "High bandwidth: OPUS SWB (Super Wide Band) > OPUS WB (Wide Band)> G722 > G711 > OPUS NB (Narrow
    Band) > G729 ; Low bandwidth: OPUS NB > G729" (p147)
    "The lowest capability (of the 2 domains) is selected" (p147)
    "An OMS is required in order to provide media services (e.g., transcoding, conferencing) with OPUS
    or G.722 codecs" (p147)
  summary: |
    规则组：①系统按"设备能力 + 域带宽档"从选择链取最优：高带宽链 OPUS SWB > OPUS WB > G722 > G711 >
    OPUS NB > G729；低带宽链仅 OPUS NB 与 G729；②跨域呼叫取两域中较低的档位（例：域 1 高、域 2 低 → 走
    低带宽算法）；③G722/OPUS 的使用由系统参数决定（Network and local / Local only / Not available，取最
    严格者）；④用 OPUS/G722 提供转码、会议等媒体服务必须配 OMS；⑤OPUS 动态 payload 默认 125，对接异构
    SIP 中继时可改（OPUS dynamic payload type 参数）。
  conditions: 验证命令 compvisu eqt all（实验输出 LIOE_IP-G722 (83) / LIOE_IP-G729 (43)）
  tags: [rule, codec, opus, g722, domain]

- id: p14
  title: IP 域硬规则：CS 必须域 0、其他域范围不得覆盖 CS 地址、1000 域、掩码一致、设备复位才落域
  type: rule
  source_pages: p143, p152, p156, p158
  source_chapter: PRINCIPLE / MISCELLANEOUS / How-To Warning
  source_quote: |
    "If there is no entry, the default IP Domain ('0') is allocated to the equipment" (p143)
    "1000 domains are manageable per system" (p152)
    "THE CALL SERVER(S) MUST BELONG TO DOMAIN 0 • THIS ENTAILS THAT THE IP ADDRESS RANGES CONFIGURED FOR
    THE OTHER DOMAINS MUST NOT ENCOMPASS THE PHYSICAL AND ROLE IP ADDRESSES OF THE COM SERVER(S)" (p152)
    "THE SUBNET MASK MUST BE THE SAME AS IN THE EQUIPMENT! • DEVICES AND BOARDS MUST BE RESETED IN ORDER
    TO BE ASSIGNED TO THE RIGHT IP DOMAIN" (p158)
  summary: |
    五条硬规则：①域按设备 IP 在初始化阶段分配，查不到表项就落默认域 0；②每系统可管 1000 个域（编号 1-999
    自定义 + 0）；③CS 必须在域 0——其他域的地址段（含单主机条目）不得覆盖 CS 的物理与角色地址；④域地址
    条目的掩码必须与设备实际掩码一致；⑤设备与板卡必须复位后才会被划入（新）域——CS 在设备初始化结束时落
    域。单地址条目的技巧：IP Address Low 与 High 填同一地址（p158 Tips）。
  conditions: 域管理不参与广播（broadcast 不覆盖 IP 域）
  tags: [rule, ip-domain, domain-0, metric]

- id: p15
  title: CAC 参数口径：Domain Max Voice Connection（-1 不限）；域内通话不受控；cnx dom 读计数
  type: metric
  source_pages: p144, p156, p162
  source_chapter: IP DOMAIN FEATURES / How-To
  source_quote: |
    "'Domain Max Voice Connection' parameter in the IP domain ('-1' means unlimited)" (p144)
    "There is no control on voice communications number for calls between 2 parties belonging to the
    same IP domain (intra-domain communications)" (p144)
    "| allowed | ffff | 1 | 1 | ... Cac over Overrun CAC communication attempts" (p162)
  summary: |
    数值口径：每域的 Domain Max Voice Connection 限定"从/到该域"的并发通话数，-1 表示不限；实验里先设 1
    验证第二通被拒、再改回 -1。域内（intra-domain）通话数永不受控。维护命令 cnx dom 读表：allowed=允许数
    （hex，ffff 不限）、used=当前通话、cac over=CAC 超限尝试计数、comp alw/use/fre/out/ovr=压缩机总数/占
    用/空闲/退服/超限占用、UseOthCC/ProvidCC=会议电路跨域借/供开关。
  conditions: CAC 溢出退路依赖 Local Private to Public Overflow
  tags: [metric, cac, ip-domain, formula]

- id: p16
  title: 4645 VM 仅支持 G711；跨域访问需压缩机且 VoIP 板与 4645 同域
  type: rule
  source_pages: p151
  source_chapter: RESOURCES ALLOCATION
  source_quote: |
    "4645 Voice Mail supports only G711 algorithm • ALE IP devices can switch automatically in G711 when
    direct RTP is possible with the voice mail ... If G711 algorithm can not be used directly • G729->
    G711 conversion, performed by a local board (GDx/GAx or INTIPx), is required • As the communication
    between the VoIP board providing the compressors and the 4645 VMS is established in G.711, the VoIP
    board and the 4645 VMS must belong to the same IP domain"
  summary: |
    规则：4645 语音邮箱只支持 G711。设备可与邮箱直连 RTP 时自动切 G711（无需压缩机）；不能直连时需本地板
    卡（GDx/GAx/INTIPx）做 G729→G711 转换，且因板卡与 4645 之间走 G711，两者必须同域——跨域访问一次要吃
    两个压缩机。
  conditions: 被域隔离/PCS 接管时被救话机打不了 4645 VM（另见 p183 限制）
  tags: [rule, 4645, voice-mail, codec]

- id: p17
  title: PCS 三前提：许可锁 332>0、PCS 版本不低于 CS、RAM 不少于 CS
  type: rule
  source_pages: p167, p187-188
  source_chapter: REQUIREMENTS / How-To
  source_quote: |
    "PCS must have a memory configuration (RAM) equal to or greater than a CS • The software version of
    the PCS is the same, or more recent than the associated Call Server • Lock 332 is greater than 0 in
    the license file in the Communication Server" (p167)
    "332 M PCS max. number = 0/ 3" (p188, spadmin 输出)
  summary: |
    硬前提三条：①CS 许可文件中锁 332（PCS max. number）>0（实验环境 0/3，即可声明 3 台）；②PCS 软件版本
    相同或更新（mtcl 欢迎信息比对 Active version，实验值 R101.1-n4.523-0-fr-c0s1）；③PCS 内存配置 ≥ 一台
    CS。PCS 可承载于 CS 虚拟机、Common Hardware CS 板卡或 GAS。
  conditions: 版本核验法：登录 mtcl 看欢迎信息
  tags: [rule, pcs, licensing, version]

- id: p18
  title: PCS 容量与配对规则：240 台/系统；一域仅一 PCS；一 PCS 可救多域（至多 1000）；无 MG 域的 SIP 设备救不了
  type: metric
  source_pages: p168-169
  source_chapter: TOPOLOGY – CASE #1 / CASE #2
  source_quote: |
    "One IP domain can be rescued by only one PCS • 240 PCS max per system • Each PCS must be configured
    to rescue at least one Media Gateway" (p168)
    "Possible rescue of several domains, including domains with no Media Gateway • In that case, at
    least one of the domains must include a Media Gateway • One PCS can secure several IP domains • Up
    to 1000 ... SIP PHONES AND SIP EXTERNAL GATEWAYS SITUATED IN A DOMAIN WITH NO MEDIA GATEWAY CANNOT
    BE RESCUED" (p169)
  summary: |
    数值组：每系统最多 240 台 PCS；一个 IP 域只能被一台 PCS 救援；一台 PCS 可救多个域（书内标注 Up to
    1000）；每台 PCS 至少要绑定一台 MG；多域共救时至少一个域含 MG——完全没有 MG 的域里，SIP 话机与 SIP 外
    部网关无法被救。
  conditions: PCS 必须留在域 0（p199 警告）
  tags: [metric, pcs, capacity, topology]

- id: p19
  title: PCS 四状态判读（pcsview）：Active/Inactive*/Undef 才能保设备；冗余切换时现 Undef
  type: rule
  source_pages: p170, p210-216
  source_chapter: PCS STATES / How-To
  source_quote: |
    "The PCS can secure a device only if its status is 'Active', 'Inactive*' or 'Undef'" (p170)
    "(Inactive) means that pcs is not running and IP connection with the CS is up ... (Inactive*) means
    that PCS has recovered connection with CS and some equipment are connected to PCS. The PCS reboot at
    expiration time" (p210)
    "If a CS switching occurs while a PCS is in ACTIVE mode, this PCS will be seen in undefined state
    (UNDEF) by the CS which has switched to main role." (p170)
  summary: |
    状态判读：Inactive=随 CS 正常（设备归 CS）；Active=断链接管中；Inactive*=链路已恢复但设备仍挂在 PCS
    上，等回切计时器；Undef=冗余系统 CS 切换后 PCS 尚未与新主重建连接，或从未建立过连接。pcsview 在 CS
    与 PCS 两侧均可执行（PCS 侧还能看被救 MG/话机清单与 "Number of Domain connect on PCS: x/y"）。
  conditions: 演练验证顺序：INACTIVE→(断链) ACTIVE→(恢复链路) INACTIVE*→(重启 PCS) INACTIVE
  tags: [rule, pcs, states, pcsview]

- id: p20
  title: PCS 回切计时器三模式：默认 30 秒 / 定点 Hour / 定时值（0=不自动重启，人工控制）
  type: metric
  source_pages: p173, p197-198
  source_chapter: SWITCH BACK / How-To 参数
  source_quote: |
    "By default: the reset is launched 30 seconds after the IP link recovery • Hour: the reset will be
    launched at the hour fixed in configuration ... • Value of a timer: the reset will be made at the
    end of a timer • Specific case: if the value equals to 0 -> No reset." (p173)
    "Timeout: ... Delay in seconds (from 1 to 65535 seconds). Note that the '0' value means that the
    Passive Communication Server does not reset." (p197)
  summary: |
    数值口径：链路恢复后 PCS 与其设备统一重启的时机三选一——默认（恢复后 30 秒）、Hour（配置的定点时刻，
    一般选非工作时间）、Timeout（1-65535 秒延迟）；取 0 表示永不自动重启，由管理员手动执行（实验口径即用
    0，演练 shutdown -r now 手动重启）。多 PCS 时可逐台自定义 update 与 reset 类型。
  conditions: 参数在 WBM \Passive Com. Server\ 全局与单 PCS 两级
  tags: [metric, pcs, timer, reset]

- id: p21
  title: PCS 与 SIP 生存性规则：双 proxy、503 切换、spatial 必须 FQDN+DNS；外部网关注册计时器 ≠0
  type: rule
  source_pages: p175-177, p202
  source_chapter: PCS & SIP / PCS & EXTERNAL SIP GATEWAYS / How-To
  source_quote: |
    "The SIP terminals and SIP External Gateways can be rescued by a PCS if they are able to handle two
    proxies ... Primary Server will be the CS ... Secondary Server will be the PCS • A 'keep Alive'
    mechanism must be used" (p175)
    "If the Primary Server does not respond or provides a '503 error message' then SIP terminal tries
    to register with the Secondary SIP server" (p176)
    "The PCS IP address must be specified, and the registration timer must be different from 0,
    otherwise the backup of the external SIP gateway will not work properly." (p202)
  summary: |
    规则组：①SIP 终端/外部网关须支持双 proxy（主=CS、备=PCS），并启用 keep alive；②注册续期无响应或收
    503 即切换方向（主→备、备→主）；③空间冗余下主必须用 OXE FQDN 且强制使用 DNS；④外部 SIP 网关要被救
    必须填 PCS IP 地址且注册计时器 ≠0；⑤网关的 PCS 参数取法必须全网一致——要么全部用全局地址
    255.255.255.255，要么全部用真实 PCS 地址，不可混用（p178）。
  conditions: 全局 PCS 地址 255.255.255.255 语义=随任一 CS/PCS 在服
  tags: [rule, pcs, sip, failover]

- id: p22
  title: PCS 数据库单向同步 + 手工参数八项清单 + 修改即丢
  type: checklist
  source_pages: p179-180, p209
  source_chapter: PCS DATABASE / PARAMETERS TO BE MANAGED ON THE PCS
  source_quote: |
    "BE AWARE THAT 'DATABASE SYNCHRONIZATION' IS UNIDIRECTIONAL: ONLY FROM CS TOWARD PCS" (p179)
    "Some parameters, mainly the one configured either via 'swinst' or 'netadmin', are not sent to the
    PCS during the update, such as: • Internal Firewall • ... Date, Time & Timezone • NTP configuration
    • SSH configuration • Syslog Server • Hosts file • SNMP configuration • Radius users" (p180)
    "ANY MODIFICATIONS WILL BE LOST AT THE NEXT DATABASE UPDATE BETWEEN THE CS AND PCS" (p179)
  summary: |
    清单：①库同步仅 CS→PCS 单向，无实时更新，刷新手段=手动 pcscopy 或定时（每日/每周）；同步还带密码文
    件、PCS 证书与私钥、Radius 文件、CCD 统计；②八类参数不随库走，须逐台手工配：内部防火墙 IPTABLES（漏
    配则设备救不回来）、日期/时间/时区、NTP、SSH、Syslog、hosts 文件、SNMP、Radius 用户；③PCS 上做的任
    何数据库修改会在下次更新时被覆盖丢失；④pcsscopy 前提：CS 侧把 PCS 加为 trusted host，PCS 侧把
    csa/csb/csm 加为 trusted host 且 /etc/hosts 含对方地址（p192：hosts 缺条目 pcscopy 直接不工作）。
  conditions: 话单不在更新时复制；PCS 激活期话单需 OmniVista 8770 取回（p181）
  tags: [checklist, pcs, pcscopy, database]

- id: p23
  title: PCS 30 天激活上限与事件组（428/427 断链、431 倒计时、432 违约态）
  type: metric
  source_pages: p182
  source_chapter: MISCELLANEOUS
  source_quote: |
    "The PCS can be active for 30 days max • After 30 days, it switches in 'Software protection
    violation' position • Incidents are generated in the CS (N°428) and in the PCS (427) ... Another
    incident (N°431) is generated in the PCS, specifying how much longer it can remain in active mode •
    Incident (N° 432) can also be reported on the PCS"
  summary: |
    数值口径：PCS 最长连续激活 30 天，超时进入"软件保护违约"态。事件编号：428（CS 侧报告信令链路丢失）、
    427（PCS 侧同报）、431（PCS 报剩余可激活时间）、432（PCS 已进入违约态）。运维含义：PCS 是临时生存手
    段，30 天内必须恢复中心侧。
  conditions: PCS 不可被冗余（不能给 PCS 再配 twin）
  tags: [metric, pcs, incidents, 30-days]

- id: p24
  title: PCS 能力边界：不救 4645/SIP 传真/SIP VM；无 TFTP/DHCP/ABC-F 服务
  type: limitation
  source_pages: p183
  source_chapter: RESTRICTIONS
  source_quote: |
    "Terminals of an IP domain rescued by a PCS can not reach the 4645 Voice Mail • Any modification
    realized on the PCS database will be lost at the next database update • SIP fax servers & SIP Voice
    Mails cannot be rescued by PCS • No TFTP service (no binaries download) • No DHCP service • No ABC-F
    service"
  summary: |
    五条边界：被救域话机打不了 4645 语音邮箱；PCS 库修改下次更新即丢；SIP 传真服务器与 SIP 语音邮箱不能被
    救；PCS 不提供 TFTP（话机无法下 binaries）与 DHCP 服务；不提供 ABC-F 服务。跨域通话在被救场景需
    Local Private to Public Overflow 兜底（p182/p211 Notes：跨站点呼叫仅在配置该特性后才可能）。
  conditions: 断链演练验证口径（p211-213）
  tags: [limitation, pcs, restrictions]

- id: p25
  title: 溢出双层权利：phone feature COS（busy/OoS/两者）+ 被叫外号闭锁；话务台恒放行；本地溢出不适用 SIP 扩展
  type: rule
  source_pages: p223, p226, p506
  source_chapter: ACCESS TO THE SERVICE / MISCELLANEOUS（两溢出章）
  source_quote: |
    "Two levels of rights • Access right to the service • The 'phone feature COS' authorizes or forbids
    the overflow • In case of busy state ... In case of 'out of order' state ... • Barring rules linked
    to the called external number" (p223)
    "Attendant set • The service is always available (no call barring)" (p223)
    "Doesn't work for call to SIP extensions or to SIP devices" (p226)
  summary: |
    权利模型：第一层 phone feature COS 的 Busy private to public overflow 与 O/S private to public
    overflow 两个开关（1 允许/0 禁止）分别控制拥塞态与断链态；第二层被叫翻译出的外部号还要过闭锁规则；两
    层都通过才建立呼叫。例外：话务台发起的溢出永远可用（无闭锁）。被叫显示为其公网 ID；block mode 拨号时
    主叫需确认或等位间计时器。边界：本地私到公溢出对呼叫 SIP 扩展/SIP 设备无效。
  conditions: 溢出产生话单，字段 26 描述设施类型（BasicCall PrivateOverflowToPublic ARSService）
  tags: [rule, overflow, cos, barring]

- id: p26
  title: Thin sector 规则：非 DID 段映射唯一外号（段首号）；外号不得与既有 DID 段重叠；溢出场景 Install No Last Part 留空
  type: rule
  source_pages: p224, p230-231
  source_chapter: DID TRANSLATOR / How-To
  source_quote: |
    "A cleverness, called 'thin sector' allows to assign a DID number to a range of none DID users ...
    This number corresponds to the first external number of this range." (p224)
    "'Installation No Last Part': IN CASE OF 'LOCAL PRIVATE TO PUBLIC OVERFLOW', THIS FIELD HAS TO BE
    EMPTY. THE 'THIN SECTOR' WILL BE USED TO PROVIDE A DEFAULT NUMBER" (p230)
    "THIS FIRST EXTERNAL NUMBER MUST NOT OVERLAP A PREDEFINED DID SECTOR OF THE 'NODE ACCESS PREFIX'" (p231)
  summary: |
    规则组：①thin sector 把一段非 DID 内部号（如 31020-31029，段长 10）映射到唯一外部号（该段首外号，如
    33210141010），公网先打到这个"第三方"号再转接；②该唯一外号不得与 Node Access Prefix 已定义的 DID 段
    重叠；③本地私到公溢出场景下 Node Access Prefix 的 Installation No Last Part 字段必须留空，由 thin
    sector 提供缺省号。DID 容量：每 Node Access Prefix 至多 2000 条 DID 段。
  conditions: DID 段可绑定到 IP 域或 MG（用本地资源优先）
  tags: [rule, did, thin-sector, overflow]

- id: p27
  title: OoS 溢出系统参数：Overflow on OoS Extension=True 才能在 PCS 接管时溢出；配完记得 pcscopy
  type: rule
  source_pages: p225, p232
  source_chapter: OVERFLOW ON OUT OF SERVICE EXTENSION / How-To
  source_quote: |
    "When a PCS is 'Active', all the remote devices are seen as 'out of service' • In order to activate
    the 'local private to public overflow', a system parameter allows to overflow even if the initial
    called party is seen as 'OoS'" (p225)
    "System/Other System Param./System Parameters ... Overflow on OoS Extension True ... Don't forget
    to perform a 'pcscopy'" (p232)
  summary: |
    规则：PCS 激活后被救域设备在中心 CS 眼里全部是 out of service，默认不会触发溢出；必须把系统参数
    Overflow on OoS Extension 设为 True 才允许"被叫 OoS 仍溢出"。配置后要执行 pcscopy 把参数同步到 PCS
    （否则 PCS 侧行为不一致）。
  conditions: 与 COS 的 O/S private to public overflow 开关叠加生效
  tags: [rule, overflow, pcs, system-parameter]

- id: p28
  title: 速拨容量口径：总表 32500（默认仅 4000 可配）；400 范围；每实体 32 区；直接段不得与范围段重叠
  type: metric
  source_pages: p236-238, p244, p247
  source_chapter: SPEED DIALING（概念） / How-To limit
  source_quote: |
    "Numbers by range are distributed over one or more numbered ranges (up to 400) ... Each entity can
    offer access to one or more ranges (up to 32)" (p236)
    "This table can contain up to 32500 numbers, indexed from 0 to 32499 ... The Direct Speed Dialing
    Range CANNOT overlap a range of speed dial numbers by range" (p238)
    "the limit in terms of speed dialing numbers that can be created in the OXE database is 32500. But,
    by default, only the first 4000 indexes are configurable." (p247)
  summary: |
    数值组：总索引表 0-32499（32500 条）；出厂仅前 4000 个索引可配置，扩容方法=mtcl 进 /usr3/mao 目录执行
    cfgUpdate→选 Abbreviated Numbers 参数→输新上限（如 32500）→重启 OXE；分范围式至多 400 个范围（范围
    间可重叠）；每实体至多开放 32 个范围区；直接式段与任何范围段不得重叠（范围段之间可以重叠）。
  conditions: 扩容须重启生效
  tags: [metric, speed-dialing, capacity]

- id: p29
  title: 速拨行为规则：默认不受闭锁、勾选才受控；溢出缩位号；开放缩位号+定时溢出；入局按目录名显示
  type: rule
  source_pages: p239-243
  source_chapter: SPEED DIALING（概念）
  source_quote: |
    "A speed dial number is subject to barring tables for access to the public network only when
    declared as barred" (p236)
    "If the outgoing trunk group of a speed dial number cannot be used, the number can be automatically
    sent to an overflow speed dial number." (p241)
    "If the 'Calling ID' (SIP message) corresponds to a speed dial number, the corresponding 'display
    name' is shown on the called set" (p239)
  summary: |
    规则组：①缩位号默认绕过闭锁，勾选 Call Restriction-Barring 后才按用户 COS 受闭锁管控（可用于简化闭锁
    配置）；②溢出缩位号——原号中继不可用时自动改发备用缩位号；③开放缩位号允许不完整号（用户补拨尾部数
    位），配合定时转发缩位号（须完整号）在计时器超时后自动补发；④每号可配目录名/名：呼出便于 call by
    name，入局时 SIP Calling ID 命中缩位号即在话机显示该名。
  conditions: 定时溢出依赖系统计时器 #3（p243）
  tags: [rule, speed-dialing, barring, overflow]

- id: p30
  title: Multiline 基线：默认全部单线（SIP 扩展除外）；Multi-MCDU 键数无限制；监督者必须 multiline
  type: rule
  source_pages: p257-259, p262, p265
  source_chapter: MULTILINE DEFINITION / MULTI-DIRECTORY NUMBER / SUPERVISION KEYS
  source_quote: |
    "By default, all sets are mono-line • Except SIP extensions" (p257)
    "*No limitation about the number of Multiline keys on a set" (p259)
    "Supervision is only available on Multiline extensions • At least one multi-line key with the main
    number" (p262)
  summary: |
    基线规则：①出厂全部话机单线，SIP 扩展除外；线数取决于话机可用键数；②Multi-keys=一号多键（多路并发、
    一线忙来话落下一空闲键）；Multi-MCDU=多号一机（主号至少一键 + 附加号键，附加号可为 DID，键数无上限）；
    ③一切监督（话机/邮箱/经理助理）都要求监督方为 multiline 且至少有一把主号多线键。
  conditions: multiline 是 f14-f18 各特性的公共前置
  tags: [rule, multiline, supervision]

- id: p31
  title: 监督键上限四条：20 监督者/话机、100（网络 20）/邮箱、15000 键/系统、一号一机一键；话务台与寻线组不可被监督
  type: metric
  source_pages: p262, p265
  source_chapter: SUPERVISION KEYS / LIMITS
  source_quote: |
    "RESTRICTION: AN ATTENDANT OR A HUNTING GROUP CAN'T BE SUPERVISED" (p262)
    "A set can be supervised by 20 sets maximum • The maximum number of supervisors for a same voice
    mailbox is 100 (20 in a network configuration) • The supervisors must be declared as multiline • The
    total number of supervision keys in the system is 15000 • Only one key with the same directory number
    can be created on a set" (p265)
  summary: |
    数值组：一台话机至多被 20 台话机监督；同一语音邮箱至多 100 个监督者（组网配置 20）；监督者必须 multiline；
    全系统监督键总量 15000；同一话机上同一目录号只能建一把键；话务台与寻线组不能作为被监督对象。可监督对
    象：话机、传真、他人语音邮箱（新留言通知、凭密码代听）。
  conditions: 监督键五档铃型（No ring/Short/Long/Short without Overring/Long without Overring）；No Call=YES 时键只监督不可呼
  tags: [metric, supervision-keys, limits]

- id: p32
  title: 经理/助理数字与互斥规则：1000 过滤表×16 参数；screening/unscreening 互斥；Selective Filtering 只转主线
  type: rule
  source_pages: p277-280
  source_chapter: FILTERING CALLS / FILTERING TABLES / SELECTIVE FILTERING
  source_quote: |
    "1000 tables usable with screening or unscreening keys • 16 parameters in each table" (p278)
    "It is not possible to activate a screening and an unscreening key at the same time • When a
    screening keys is activated, if you press an unscreening key, you disable the screening key(s) (and
    vice versa)" (p279)
    "Only the main lines of the manager are routed to the assistant" (p280)
  summary: |
    规则组：①过滤表 1000 张、每表 16 个参数，可混装内部号/中继组/缩位号/话务台号/T2 号等；②同一话机可配
    多把 screening/unscreening 键（分对多个助理），但 screening 与 unscreening 互斥——按下一类键会关掉另
    一类；③Selective Filtering 勾选后只把经理主号来话转助理，副号来话仍进经理；④unscreening 表为空时全部
    来话都转助理；⑤Routing Assistant（溢出助理）每经理仅一名、可服务多经理、且不得已是该经理的助理
    （p283）；Assistant Away 键每助理仅一把（p282）。
  conditions: 建经理/助理键前双方必须已有至少一把 multiline 键（p288 Notes）
  tags: [rule, manager-assistant, filtering]

- id: p33
  title: 寻线组规则：COS 随进出（公网 COS=255 保留自己）、camp-on 百分比公式、溢出号、末位退组开关
  type: rule
  source_pages: p303-305
  source_chapter: CLASSES OF SERVICE / EXIT/ENTER / OVERFLOW DIRECTORY NUMBER
  source_quote: |
    "As soon as a user: Is part of a Hunting group: Takes the Hunting group's properties (Connection
    COS, Public Network COS, Entity) ... If you don't specify a public Network COS (leave 255 in the
    field), the user will use its own COS" (p303)
    "% authorized camp on calls = Max. Number of camp on calls authorized / number of active stations in
    the hunt group x 100" (p305)
  summary: |
    规则组：①成员入组即用组的 Connection COS/公网 COS/实体，退组即还原；公网 COS 字段留 255 表示保留成员
    自己的；②进出组前缀默认 480（entry）/481（exit），可配置禁止末位成员退组（允许退光则来话转溢出号或忙
    音）；③溢出触发两条件：组空（无人）或排队百分比到限（公式=最大允许 camp-on 数/组内活动站数×100）；
    溢出目标可为本地/网络话机、另一寻线组或话务台；④组有自己的 greeting guide（内部主叫听导引替代回铃，
    留空则回铃）。
  conditions: 一台话机只能属于一个寻线组（p318 警告）
  tags: [rule, hunting-group, cos, formula]

- id: p34
  title: 寻线组 multiline 行为参数：No Multi-line call in PCX（0/1/2 三分支）；仅循环/顺序组可含 multiline
  type: metric
  source_pages: p308
  source_chapter: MULTILINE SETS
  source_quote: |
    "The multiline sets are authorized only in cyclical or sequential Hunting groups • Three different
    modes of call distribution are manageable in the system • Parameter: No Multi-line call in PCX •
    Default value is 1"
  summary: |
    三分支口径：值 0——组来话即使该 multiline 话机一线忙，仍落到其空闲 multiline 键；值 1（默认）——忙机
    不落键、直接溢出到组内下一台，全组忙时才落回该机 multiline 键；值 2——忙机完全不落键（即使全组忙也不
    落）。只有 cyclical 与 sequential 组接受 multiline 成员（parallel 组不行）。
  conditions: 与"Authorized camp on calls %"配合决定排队与溢出次序
  tags: [metric, hunting-group, multiline, parameter]

- id: p35
  title: 代接默认前缀与权利：组代接 56、直接代接 55；需 COS 授权且被叫未受保护；zdpost 查 pickup_id
  type: metric
  source_pages: p314, p324-326
  source_chapter: CALL PICK-UP GROUP / How-To
  source_quote: |
    "Group call pick-up ... simply dial the group call pick-up prefix ... Direct call pick-up ... the
    Direct call pickup prefix must be dialed and followed by the directory number" (p314)
    "The two prefixes are created by default with the numbers 55 for the 'Group call pickup' prefix and
    56 for the 'Direct call pickup' prefix." (p325)
    "zdpost d 31001 |grep -i pickup_id → pickup_id = 0 ... pickup_id = -1" (p326)
  summary: |
    数值口径：默认前缀组代接=56（注意 p325 Note 原文 55/56 表述与截图互换，见 counter-example）、直接代接
    =55；直接代接可拨组号或振铃话机号。使用前提：代接方 Phone Features COS 的 Group/Direct call pickup=1，
    且被叫话机未受 pick-up 保护。核验：zdpost d <分机> |grep -i pickup_id，返回组索引（0 起）或 -1（不在
    组）。
  conditions: Pickup 组没有独立建组菜单——在用户属性填 PickupGroup Name 即自动成组（p323）
  tags: [metric, pickup, prefix, zdpost]

- id: p36
  title: 办公桌共享数值：虚拟 MAC aa:bb:分机号、自动登出 -1/0-23、忙时重置事件 6004、即时登录限定条件
  type: metric
  source_pages: p333, p334-336, p346-347
  source_chapter: REGISTRATION OF IP STATIONS / SYSTEM OPTIONS / How-To
  source_quote: |
    "'aa:bb:xx:xx:xx:xx' → xx:xx:xx:xx is replaced by the directory number of the DSU • Example for the
    DSU user 31000 : 'aa:bb:00:03:10:00'" (p333)
    "DSU Auto Log-off Time -1 : (default value) the feature is not activated • 0 to 23: time when the
    automatic log off is activated" (p346)
    "Allow Reset of Busy DSU True: ... An incident '6004' is generated." (p346)
  summary: |
    数值组：①DSU 虚拟 MAC=aa:bb:+分机号（如 31000→aa:bb:00:03:10:00），物理帧仍用真 MAC；②登出免密默认
    False；③全员自动登出时间 -1（默认关）/0-23 点；④Allow Reset of Busy DSU 默认 True（忙时 DSU 被登出
    并释放通话，产生 6004 事件；False 则保通话、异机登录显示 Unauthorized）；⑤首次登录强制改密默认 False；
    ⑥免重启即时登录默认 True，仅限 NOE3GEE/IP Essential/Enterprise 且 DSS/DSU 同族、同节点、无 AOM，不适
    用于 IPDSP；⑦ippstat 判读：DSU 登出态虚拟 INTIP 显示 255/255，登录态显示真实 19/1 并可由 MAC 反查所
    在 DSS；⑧话机侧清除：按 I+# → IP parameters → Free seating。
  conditions: domstat 的 DS 列 S=DSS、U=DSU；domstat/ippstat 支持 -noname 隐去用户名
  tags: [metric, desk-sharing, dsu, incident-6004]

- id: p37
  title: 多设备结构数值：主站+至多 4 副站（WBM 逐个添加）、DECT/REX 各限 1、禁用机型清单
  type: metric
  source_pages: p353-354, p367
  source_chapter: MULTI DEVICE OVERVIEW / PHONE SET CHARACTERISTICS / How-To
  source_quote: |
    "The number of sets can be extended up to 4 in a multi device user configuration" (p353)
    "*Only one DECT per multi device user • Only one Remote Extension per multi devices user" (p354)
    "They can not be: Analog type • S0 type • Attendant sets • Distribution agent sets (ACD, CCD) • Sets
    of a PABX hunt group • Sets declared as night forwarding • Sets declared as room or booth ..." (p354)
    "Tandem Directory Number Enter the directory number of the first secondary set (310x1) ... Attached
    multi device Add up to 3 secondary devices" (p367)
  summary: |
    数值口径：多设备=主站+至多 4 个副站（twinset 为 2 台的旧称/特例）；WBM 操作上 Tandem Directory Number
    填第 1 副站、Attached multi device 再加至多 3 台（合计 4 副）。主站类型：NOE IP/NOE TDM/IPDSP/SIP
    (SEPLOS)/desk sharing(DSU)；副站另加 DECT、MIPT、REX；每多设备仅 1 台 DECT、1 个 REX。禁用：模拟、
    S0、话务台、ACD/CCD 分配坐席、寻线组成员、夜转话机、客房/包厢。主副站都必须 multiline。
  conditions: 主站号即多设备号；呼叫副号只响副站
  tags: [metric, multi-device, twinset, limits]

- id: p38
  title: 多设备状态规则：忙=主站全线忙；Partial busy 与 Specific supervision 语义；主站退服三参数联动
  type: rule
  source_pages: p356-362, p369-370
  source_chapter: CALL HANDLING / PARTIAL BUSY / SPECIFIC SUPERVISION / MAIN SET IS OUT OF SERVICE / How-To
  source_quote: |
    "The multi device user is busy when all the lines of the main set are busy" (p356)
    "Partial busy • False: (by default) the status of the tandem reflects the occupation status of the
    main set • True: the tandem is seen as busy as soon as one of the sets ... is busy" (p357)
    "'MAIN BUSY' if only the main device is busy • 'SECONDARY BUSY' ... • 'TOTAL BUSY' ..." (p358)
    "This value is taken in account if the 2 following other data are set: • Forward if set is out of
    service = 1 • Overflw to sec tandem if main oos = 1" (p370)
  summary: |
    规则组：①忙态默认只看主站全线；Partial busy=True 则任一话机忙即算忙；②Specific supervision=True 时
    监督降级为状态监督（按键不呼叫、显示 MAIN/SECONDARY/TOTAL BUSY）；③主站退服三参数——Forward if set
    OOS（COS，1=来话转关联副站）、Overflow to sec tandem if main OOS（系统参数，True=溢出到副站 tandem）、
    Ring all its secondar. if main oos（COS，True=所有副站同响），第三项生效依赖前两项配置；④这些参数修改
    在主站退服期间不生效，要等主站恢复服务后再次退服才按新值走（p370 Tips）；⑤Ring Secondary REX in
    Parallel 控制主为 IPDSP 时副 REX 是否同响（默认 True）；REX 振铃停用/激活前缀 651（p360）。
  conditions: 建关联会清空话机全部数据且复制数据不可改（p366 警告）
  tags: [rule, multi-device, partial-busy, oos]

- id: p39
  title: Direct IP Link 容量口径：100 节点、24 接入×62 通道=1488 路/链、约 10000 呼/时/链、全网 ≥R100.0
  type: metric
  source_pages: p385, p395
  source_chapter: OVERVIEW / LIMIT /PROVISIONING LEVEL
  source_quote: |
    "All nodes of the subnetwork have to be in release OXE Purple R100.0 minimum" (p385)
    "Number of nodes is limited to 100 • ... Up to 24 accesses can be configured • 1 access with IP
    signalling • Other accesses without signalling • 62 channels per access • As a consequence, 1488
    simultaneous calls maximum on a direct call ... approximately 10000 calls per Direct IP link (with 8
    accesses) per hour" (p395)
  summary: |
    数值组：全网节点 ≤100；每链至多 24 接入（接入 1 必须 IP 信令，2-24 无信令）×每接入 62 通道 = 1488 路并
    发；性能约每链 10000 呼/小时（8 接入口径）；链路级可另设"Maximum number of IP calls"限带宽；节点级还
    有含 Direct IP Link/SIP trunk/ABCF-IP trunk 的全局呼叫上限（范围 -1..32767，超限 6005 事件）；要求全
    网版本 ≥ OXE Purple R100.0（直链首个支持版本为 N1）。
  conditions: 迁移场景另需全网 ≥N1（p388）
  tags: [metric, direct-ip-link, capacity]

- id: p40
  title: Direct IP Link 系统选项不可逆三态：Disabled→Migrating（必须重启）→Enabled；回退只能靠库恢复
  type: rule
  source_pages: p402-403
  source_chapter: 'Direct IP Link" system option'
  source_quote: |
    "Direct IP Link Enabled, means that 'Direct IP Links' can be configured in the OXE Database (no more
    Hybrid link + VPN overflow). This is an irreversible value : once in 'Enabled', it is not possible to
    change system option anymore. If reverting the process is mandatory, only restoration of database can
    handle this." (p403)
    "First, switch the system option value from 'Disabled' to 'Migrating' and REBOOT the OXE ... OXE
    REBOOT IS REQUIRED ('SHUTDOWN -R NOW') TO TAKE INTO ACCOUNT THIS PARAMETER • Then, switch the system
    option value from 'Migrating' to 'Enabled' (no reboot)" (p403)
  summary: |
    规则：系统选项三态——Disabled（只能建老一代 ABC 链路）、Migrating（中间态，切到该值必须 shutdown -r
    now 重启生效）、Enabled（允许建直链，不可逆，回退唯一手段是恢复数据库备份）。启用路径两条：空库创建时
    直接选 Direct Link Network: Y；或存量库按 Disabled→Migrating→重启→Enabled 三步走。
  conditions: 参数路径 System/Other System Param./Network Parameters/
  tags: [rule, direct-ip-link, system-option, irreversible]

- id: p41
  title: Direct IP Link 接入规则：接入 1 必须 IP 信令、2-24 无信令、增删前先停 Direct Link synchro、两端接入数必须一致
  type: rule
  source_pages: p405, p407-409
  source_chapter: Direct IP Link accesses creation
  source_quote: |
    "First, declare the 1st access, which uses 'IP' as 'signaling type'. Then, before adding the 2nd
    access, make sure that the 'Direct Link synchro' is disabled." (p407)
    "Only one access can be declared on this link with 'IP Signaling type' • Any supplementary access is
    'Without signaling' • There cannot be more than 24 accesses declared on one link" (p408)
    "IP BANDWIDTH RATE, ENCRYPTION AND NUMBER OF ACCESSES MUST HAVE THE SAME VALUE ON BOTH ENDS OF THE
    LINK. IF THEY ARE CHANGE IN AN ASYMMETRIC MANNER WHILE LINK IS ESTABLISHED, BEHAVIOUR MIGHT BE
    ERRATIC. IF THEY ARE DIFFERENT AT STARTUP, THEY WON'T ESTABLISH, AND INCIDENT 2879 IS RAISED" (p405)
  summary: |
    规则组：①接入 1 用 IP 信令（填对端 CS 主地址；空间冗余可在 Other 页签填第二主地址），接入 2-24 必须
    Without signaling 且 Sig Provider=接入 1；②增删接入前必须在任一接入上 Disable Direct Link 同步（此时
    整链断开），完成后重新 Enable（两端接入数不一致则建不起来）；③带宽档（High/Low）、加密、接入数必须两
    端一致——运行中改不对称行为异常、启动时不一致直接 2879 事件拒建；④链路名固定 Link_xx（xx=对端节点
    号），不可改名、全网同名以保证广播可用；⑤空链路 99 条自动生成、无接入的链路在管理界面默认不显示，
    hybvisu/trkvisu 用选项 dl 才能看全。
  conditions: 管理路径 Inter-Nodes Links / Logical Links (ABC-F) / <Link> / Hybrid or Direct Link Access
  tags: [rule, direct-ip-link, accesses, incident-2879]

- id: p42
  title: Audit 前提与对象行为：防火墙含全部物理+角色+第二主地址；specific 收集、shared 以参考节点为准、trunk groups 不审计
  type: checklist
  source_pages: p427-428, p436-437, p449
  source_chapter: AUDIT（概念）/ How-To prerequisites
  source_quote: |
    "Before processing an audit, it is mandatory to configure the internal firewall of each node in order
    to allow the connection to all the remote OXEs CS: • Physical IP address of each remote Call Server
    • Physical IP address of each remote twin Call Server (if exists) • Main IP address of each remote
    Call Server (role address) • Second main IP address of each remote Call Server (in case of spatial
    redundancy)" (p436)
    "The audit behaviour follows the broadcast objects configuration • Trunk Groups are not broadcast ...
    Trunk Groups are not audited" (p428)
  summary: |
    前提清单：每节点防火墙互信对方全部地址（物理 + twin 物理 + 主角色 + 第二主地址）+ SSH 公钥全网分发。
    对象行为：specific 对象（编号计划/电话簿/DDI/寻线组等）全网收集合并进参考库；shared 对象（各类 COS/
    资费/音色/定时器等）只取参考节点的值全网替换；不审计对象（ARS 表、中继组前缀、IP 域等）须逐节点本地
    配置；审计对象范围跟随 broadcast 对象配置（trunk groups 不广播因此也不审计，选对象时手动勾）。传输为
    ASCII 压缩 + sftp，客户端/服务器模型，动作全记录进 MAO 历史与 LOG。
  conditions: 参考节点默认=运行 audit 的本地节点（提问直接回车即本地）
  tags: [checklist, audit, firewall, objects]

- id: p43
  title: Audit 安全阀：必须先模拟（工作在表副本）；强烈建议全网备份；链式对象需跑两遍
  type: rule
  source_pages: p435, p442, p449
  source_chapter: ENCOUNTERED PROBLEMS / PRECAUTION
  source_quote: |
    "1- Do a partial audit for dialling plan, entities, attendant, attendant groups, call distribution
    Followed by a general audit • 2- Do a global audit twice" (p435)
    "IT IS HIGHLY RECOMMENDED TO SAVE THE DATABASE OF ALL NODES BEFORE STARTING THE AUDIT" (p442)
    "To limit the risks, it's mandatory to use simulation mode • In this mode, audit works on a copy of
    tables and doesn't modify the database" (p442)
  summary: |
    三条安全阀：①audit 直改数据库表、旧数据不留——模拟模式（菜单选项 4/5：Simulation Immediate/Delayed）
    是强制动作，模拟通过后再跑真实运行（选项 1/2）；②跑之前强烈建议备份全网所有节点数据库（原文全大写警
    告）；③话务台/实体/呼叫分配等链式对象首跑会因互相缺引用被拒（如先有 310 前缀又有 31000 用户），解法
    二选一：先做"编号计划+实体+话务台+话务台组+呼叫分配"的部分审计再全局审计，或全局审计直接跑两遍。
  conditions: 新增节点场景参考库构建只选单节点（见 c14/p421）
  tags: [rule, audit, simulation, backup]

- id: p44
  title: Broadcast 数值口径：buffer 默认 10 分钟、LOG 上限 127 个、广播域 -1..127（128 个）、区域文件名 A.Z.N.S
  type: metric
  source_pages: p474-475, p481, p483, p490
  source_chapter: THE BUFFER FILE / LOG FILES / BROADCAST AREAS / How-To 全局配置
  source_quote: |
    "The content of the buffer file is emptied and stred every 10 min into a LOG file (the timer can be
    modified)" (p474)
    "Enter the maximum number of LOG files that will be saved on the disk (maximum value: 127)." (p490)
    "128 broadcast areas can be used ... Area numbers are from –1 (no area) to 127" (p481, p483)
  summary: |
    数值组：buffer 文件（cm_cb.sav / area_cm_cb.sav，位于 /usr4/mao）默认每 10 分钟落一个 LOG（可调，步进
    1 分钟）；LOG 命名 LOG.节点号.序号，配广播域后为 A.Z.N.S（域号.节点号.序号）；磁盘保存 LOG 上限 127
    个（断网时文件囤积、恢复后续传）；广播域号 -1（不属域）至 127 共 128 个；文件在全网确认后删除、仅留每
    节点最新一条；远端写失败产生 RLOG。
  conditions: Broadcast Poll Timer 控制各节点互查 lupd.dat 的周期
  tags: [metric, broadcast, log, areas]

- id: p45
  title: Broadcast 对象行为矩阵：出向三态（不广播/域内/全网）×入向三态（不收/仅本域/全网），全局或逐对象
  type: rule
  source_pages: p481-482, p490-491, p485
  source_chapter: BROADCAST AREAS / OBJECTS BEHAVIOUR / RESTRICTIONS
  source_quote: |
    "Outgoing behaviour • No broadcast • Broadcast over the network • Broadcast in area • Incoming
    behaviour • Not included • Always included • Only from area" (p481)
    "List of objects not broadcasted: • Trunk groups prefixes and ARS tables • IP domains • Content of
    embedded DHCP server • Speed dialling • ... Local range: no broadcast • Network range: broadcast of
    the ranges and numbers" (p485)
  summary: |
    行为矩阵：每个对象可配出向（No broadcast / Broadcast in the area / Broadcast over the network，默认全
    网）与入向（Coming from the network 默认 / Only from the area / Not taken into account）；Update all
    Behaviors=Yes 时全局行为覆盖逐对象配置。明确不广播对象：trunk group 前缀与 ARS 表、IP 域、嵌入式
    DHCP 内容、本地范围缩拨号（网络范围缩拨号会广播范围与号码）。激活三法：cleanbroad -all（重置序号+删
    文件+全网重启）、WBM System/Broadcast（Operational YES）、mao +br（mao -br 关闭，mao -a 看状态）。
  conditions: broadcast 行为同时决定 audit 的对象范围（见 p42）
  tags: [rule, broadcast, objects, matrix]

- id: p46
  title: 组网私到公溢出的广播属性差异：Number to add 不广播；Install N° last part 与 Node DID Translation 广播
  type: rule
  source_pages: p505
  source_chapter: NODE ACCESS PREFIX
  source_quote: |
    "Node access prefix is declared toward the remote node number (e.g.: 2) • Define a local prefix
    (preferably ARS) • Parameter: 'number to add' • Not broadcasted • Specify a remote node third-party
    DID directory number ... • Parameter: 'Install. No Last Part' • Broadcasted • Assign the remote node
    DID translator ... • 'Node DID Translation' sub menu • Broadcasted"
  summary: |
    属性差异：Node Access Prefix 指向远端节点号；其中 Number to add（本地 ARS/中继前缀）不参与广播——各节
    点本地各配各的；Install. No Last Part（非 DID 被叫的远端第三方号）与 Node DID Translation（远端 DID 段
    翻译）参与广播。含义：新建/重装节点后，"本地方向"参数必须手工补配，广播不会替你带过来。
  conditions: 子网间场景对应 Network Access Prefix / Network DID Translation（p507）
  tags: [rule, overflow, broadcast, node-access-prefix]

- id: p47
  title: 公到私重路由规则：ARS 强制、Trunk Group=-1 每表仅一条且须首位、非 DID 不适用、需第二公网路由兜底
  type: rule
  source_pages: p519-522, p527-529
  source_chapter: PUBLIC TO PRIVATE REROUTING（概念） / How-To
  source_quote: |
    "Use of ARS is mandatory to force calls rerouting from public to private network" (p519)
    "Value '-1' on trunk group forces the OXE to check the meaning of the called number, modified by the
    ARS route ... Only one ARS route with this value per table • This route must be in first position in
    the table • In case of problems with the ABC-F link, a second public route (e.g.: public SIP carrier)
    can be used" (p522)
    "None DID sets are not taken into account by this feature" (p522)
  summary: |
    规则组：①重路由必须用 ARS：Real Discriminator 按呼叫号（尽量精确到远端 DID 段前缀）挂 ARS 表；②路由 1
    的 Trunk Group=-1 表示不占中继、改号后交回 OXE 重分析（去 6 位加 3 位还原内号后匹配网络号走直链）；-1
    路由每表仅一条且必须在首位；③路由 2 为公网兜底（实验口径：TG1/2 + Dialing Command Table 1/2，去 1 位
    加 33）；④Time-based Route List 定义 1→2 的降级顺序；⑤非 DID 被叫不适用该特性。
  conditions: 前提：闭锁规则已配（starter）、SIP 中继正常、直链可用、远端用户已是本地网络号（audit/broadcast 完成）
  tags: [rule, rerouting, ars, discriminator]

- id: p48
  title: 实验口径参数表（一）：集中式 Pod 的 SIP 网关与 DID 翻译给定值
  type: metric
  source_pages: p53-54, p381-382
  source_chapter: Pod Configuration（两套 How-To）
  source_quote: |
    "Registration ID: pbxN (where N is your POD Number) e.g.: for POD 3, pbx3 • Outgoing username= pbxN" (p53)
    "First external number 33210N41000 (where N is your POD Number) ... First internal number 31000 •
    Range Size 500" (p54)
    "For NODE 2: Registration ID: remoteN ... For NODE 2: First external number: 33110N41500 ... First
    internal number: 31500 • Range size 500" (p381-382)
  summary: |
    实验口径（RLAB，生产替换）：外部 SIP 网关注册参数 Registration ID=pbxN、Outgoing username=pbxN（组网
    Pod 的 Node 2 用 remoteN）；DID 翻译——Node 1：First external 33210N41000、First internal 31000、
    Range 500（即外号 41000-41499 ↔ 内号 31000-31499）；Node 2：33110N41500、31500、500。路径：SIP/SIP
    Ext. Gateway 与 Translator/External Numbering Plan/Default DID num. translator。
  conditions: 所有 N=两位 POD 号（如 POD 3 → 33210341000）
  tags: [metric, lab, did, sip-gateway]

- id: p49
  title: 维护事件编号对照表（本书出现的 incident 号）
  type: metric
  source_pages: p79, p182, p346, p348, p395, p405, p417
  source_chapter: 各章 MISCELLANEOUS / Maintenance
  source_quote: |
    "incident « 440 » is triggered. A database cloning operation ... is then necessary !" (p79)
    "Incidents are generated in the CS (N°428) and in the PCS (427) ... (N°431) ... (N° 432)" (p182)
    "An incident 6005 is edited : 'Further calls not possible on trunk %d'" (p395)
  summary: |
    事件对照：440=主备失联超时、需 mastercopy；427=PCS 侧信令链路丢失；428=CS 侧信令链路丢失；431=PCS 剩
    余可激活时间；432=PCS 进入软件保护违约态；6004=忙时 DSU 被登出/通话被释放（办公桌共享）；6005=节点级
    全局呼叫上限到达（Further calls not possible on trunk）；2879=Direct IP Link 两端带宽/加密/接入数不一致
    拒建；2880=ABCF_IP 信令链路建立中；2881=ABCF_IP 信令链路已建立；2882=信令链路释放；2884=ABCF_IP 信令
    链路已禁用；2832=节点 X 不可达；2846=节点 X 可达。查询命令 incvisu / incinfo GEA。
  conditions: 事件号以 R101.1 为口径
  tags: [metric, incidents, troubleshooting]

- id: p50
  title: 许可与版本锚点（本书出现）：锁 185/186/332/329/330、CAPEX 模式、SSHv2 自 N3、直链自 R100.0/N1
  type: metric
  source_pages: p94, p167, p187-188, p385, p388, p397
  source_chapter: spadmin 输出 / REQUIREMENTS / DIRECT IP LINK
  source_quote: |
    "184 Integrated Gatekeeper = 99999 • 185 SIP Gateway = 2 • 186 E-CS redundancy = 1 • 187 H323 (G711)
    network link = 20 • 188 SIP network links = 20" (p94)
    "329 M IP-Softphone Agents = 0/ 20 • 330 M Advanced Mobile IP-Touch Users = 0/ 10 • 332 M PCS max.
    number = 0/ 3" (p188)
    "CAPEX mode ... Panic flag status : PANIC flag : 0" (p188)
  summary: |
    锚点：冗余许可看锁 186 E-CS redundancy ≥1（实验值 1）；PCS 看锁 332（实验值上限 3）；SIP 网关锁 185
    （实验值 2）；另有 329 IP-Softphone Agents（0/20）、330 Advanced Mobile IP-Touch Users（0/10）。版本
    锚点：SSHv2 公钥认证自 N3 强制；Direct IP Link 首个支持版本 N1、要求全网 ≥ OXE Purple R100.0；混合网
    中其他节点最低 R9。spadmin 还显示 CAPEX 模式与 PANIC flag 状态（实验值 0）。
  conditions: 许可文件核验命令 spadmin → 选项 2 Display active file；FlexLM 服务器 192.168.1.80（实验口径）
  tags: [metric, licensing, version, spadmin]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 21 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 集中式 IP Pod 配置 | 有 | p48 | SIP 网关注册参数与 DID 翻译给定值（实验口径） |
| task-02 | SSH 免密体系 | 有 | p01, p02, p03, p04 | N3 基线、两工具使用规则、密钥路径表 |
| task-03 | 本地冗余部署 | 有 | p05, p06, p08, p09, p11 | 同版本铁律、链路承载、角色次序、120 分钟窗口、升级序列 |
| task-04 | 空间冗余部署 | 有 | p12 | DNS/DHCP/TFTP 四条适配规则 |
| task-05 | 冗余维护与切换演练 | 有 | p05, p07, p09, p10 | 切换语义、参考 MG 裁决、double main 服务缺失 |
| task-06 | 不停机升级 | 有 | p11 | 11 步清单 |
| task-07 | IP 域规划与配置 | 有 | p13, p14 | 编解码选择链、域 0 硬规则 |
| task-08 | IP 域验证排障 | 有 | p15, p16 | CAC 参数口径与 cnx dom 计数、4645 G711 规则 |
| task-09 | PCS 部署 | 有 | p17, p18, p22, p27 | 三前提、容量配对、单向同步与八项手工清单、OoS 溢出参数 |
| task-10 | PCS 救援与回切演练 | 有 | p19, p20, p23 | 四状态判读、计时器三模式、30 天与事件组 |
| task-11 | 本地私到公溢出 | 有 | p25, p26, p27 | 双层权利、thin sector、OoS 系统参数 |
| task-12 | 速拨体系 | 有 | p28, p29 | 容量口径与行为规则 |
| task-13 | 多线与监督键 | 有 | p30, p31 | multiline 基线与四条上限 |
| task-14 | 经理/助理组 | 有 | p32 | 过滤表数字与互斥规则 |
| task-15 | 寻线/代接组 | 有 | p33, p34, p35 | COS 随组、camp-on 公式、multiline 三分支、代接前缀 |
| task-16 | 办公桌共享 | 有 | p36 | 虚拟 MAC/登出/6004/即时登录数值组 |
| task-17 | 多设备用户 | 有 | p37, p38 | 结构数值与状态/退服规则 |
| task-18 | Direct IP Link 组网 | 有 | p39, p40, p41, p50 | 容量、不可逆三态、接入规则、许可锚点 |
| task-19 | Audit | 有 | p42, p43 | 前提清单与三安全阀 |
| task-20 | Broadcast | 有 | p44, p45 | 数值口径与行为矩阵 |
| task-21 | 组网双向溢出 | 有 | p25, p46, p47 | 权利模型、广播属性差异、ARS 规则 |
| （横切） | 事件与许可对照 | 有 | p49, p50 | 事件编号表、锁号/版本锚点 |

**覆盖结论**：21/21 全部有对应条目；另加两条横切对照表（p49 事件号、p50 许可与版本锚点）。
两点口径说明：
1. 实验给定值（IP/密码/POD 号码）只保留结构必需的最小集合并标注"实验口径"（p48），完整设置表不在此展开。
2. p35 代接默认前缀的 55/56 在原文 Note 与截图间互换，本表按截图口径（56=组代接、55=直接代接）记录并在 counter-example 中立条说明。
