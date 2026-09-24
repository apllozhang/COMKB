# 反例/限制/边界/易错点候选 — OmniPCX Enterprise Starter (ENTPXTE400EN Ed12)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 培训实验口径全景——明文教学密码遍布全书，生产必须全部替换
  type: warning
  source_pages: p9, p18, p98, p248, p262, p312, p329, p759
  source_chapter: RLAB SETTINGS / 各实验章
  source_quote: |
    p98: "mtcl (for the current training; password= Administrator5689!) • root … Superuser2580* • swinst … Superuser2580*"
    p248: "default passwords: admin [letacla1] and root [mg4.ale]]"
    p329: "User: admin Password: *tx8000# (default password)"
  summary: |
    实验密码族：Administrator5689!（mtcl）/ Superuser2580*（root、swinst、client）/ alcatel（SIP 运营商、Thunderbird）/ letacla1（FlexLM root、GD4 admin、OMS admin+root、GDXL admin）/ mg4.ale（GD4 root）/ mgxl.ale（GDXL root）/ 0000（用户初始码）/*tx8000#（话机 SFTP）。
    教材用途是教学记忆锚点；照抄进生产等于零防线。产出 skill 时必须整体标注"实验口径"，并把"首连即改密"写成强制步骤。
  conditions: 全书实验环境
  tags: [warning, lab, security, passwords]

- id: n02
  title: 防火墙默认全关——任何主机不可入站，互通靠白名单
  type: limitation
  source_pages: p87, p135, p138, p140
  source_chapter: Connection & login / OXE internal firewall
  source_quote: |
    p87: "By default, no host is allowed to communicate with OXE (inbound connections) • Outbound connections from OXE are not controlled"
    p140: "Chain INPUT (policy DROP …) … Chain FORWARD (policy DROP …) … Chain OUTPUT (policy ACCEPT …)"
  summary: |
    N3 起默认最高安全：入站/转发默认 DROP、出站 ACCEPT；回环与 ICMP 放行。"装完连不上"先查防火墙可信主机，而不是怀疑网络。配了 DNS 还必须把 DNS 服务器加为可信主机（p138）。
  conditions: OXE N3 及以后（R101.0 起为完整 iptables）
  tags: [limitation, firewall, security]

- id: n03
  title: "Allow SSH for all" 是临时便门——配完必须 Deny，否则白名单无意义
  type: warning
  source_pages: p142, p159
  source_chapter: OXE internal firewall / lab
  source_quote: |
    p142: "Useful facility for the administrators to allow quickly and temporarily the connection to OXE CS during fresh installation or migration to N3 (restore database). • Not very secured, must be done in accordance with the customer."
    p159: "If option 'Allow SSH for All' was enabled previously, don't forget to 'Deny SSH for All', otherwise the trusted hosts management has no meaning!"
  summary: |
    开局/迁移时允许全网 SSH 便于操作，但教材两处强调收口：可信主机配完必须 Deny SSH for all；Deny 不删除 iptables 规则、可信主机仍可 SSH。培训实验甚至建议可整体关防火墙——绝不可带入生产。
  conditions: 开局/迁移期
  tags: [warning, firewall, ssh]

- id: n04
  title: root 只能本地直登；IP 侧必须经 mtcl su；900 秒固定超时
  type: limitation
  source_pages: p90, p99
  source_chapter: System accounts & passwords
  source_quote: |
    p90: "Direct access (by login request) to the root account can only be performed on the console port. • Access via IP (SSHv2) can only be performed indirectly by using the 'su' command from the mtcl account."
    p99: "Warning IT IS POSSIBLE TO CONNECT DIRECTLY VIA THE ROOT ACCOUNT ONLY IF YOU USE A LOCAL ACCESS (SERIAL CONNECTION, KVM, …)"
  summary: |
    root 直登仅限串口/KVM 控制台；SSH 会话需先 mtcl 再 su -（要求 root 密码）。root/mtcl 无操作 900 秒强制登出且不可配置——长脚本操作要考虑会话保活。
  conditions: 全版本
  tags: [limitation, accounts, security]

- id: n05
  title: 提示符 (E) 不实时刷新——话务启动后旧会话状态失真
  type: limitation
  source_pages: p117, p123
  source_chapter: Start & Stop
  source_quote: |
    p117: "Note: the (E) information is not refreshed automatically, in real time, meaning that if you are logged on before the end of the OXE startup phase, you must logout and login again to display the real status"
    p123: "If the telephone was started after logon, the prompt will not change, and you must logout and login again to have new prompt (with number) displayed."
  summary: |
    (E)=话务（大概率）停止、(数字)=运行，但仅在登录时判定。启动完成前登录的会话会一直显示 (E)——判状态以 role 命令为准，或重登录刷新提示符。
  conditions: 系统启动/重启场景
  tags: [limitation, role, troubleshooting]

- id: n06
  title: swinst Easy 7 停话务会同时取消 autostart；停话务无独立命令
  type: warning
  source_pages: p116, p122, p124
  source_chapter: Start & Stop
  source_quote: |
    p124: "WHEN THE TELEPHONE APPLICATION IS STOPPED VIA THE SWINST MENU (1-EASY MENU > 7-STOP THE TELEPHONE), THE AUTOSTART IS AUTOMATICALLY DISABLED"
    p122: "There is no command to stop the telephone application. The whole system must be restarted and a telephone start-up cancelation must be performed"
  summary: |
    两个易错点：①Easy 7 停话务后 autostart 自动取消，下次重启话务不会自起——维护完要记得重新 Set autostart；②CLI 没有"停话务"命令，只能重启系统并在 5 秒窗口按回车取消自启。
  conditions: 系统维护
  tags: [warning, autostart, start-stop]

- id: n07
  title: netadmin 改动必须 Apply+重启；默认域名会致证书错误
  type: warning
  source_pages: p146, p148
  source_chapter: IP Addressing & Firewall lab
  source_quote: |
    p148: "TO TAKE THE MODIFICATION DONE VIA THE NETADMIN MENU INTO ACCOUNT, IT IS MANDATORY TO RESTART THE SYSTEM"
    p146: "WARNING: Default domain name is configured Please configure a legitimate registered domain name, to prevent certificate errors. Enter OXE Domain to be configured (default is oxedomain.com)"
  summary: |
    两条：①netadmin 一切修改要按 a 应用并重启系统才生效（Apply 时 NGINX 重启）——"改了没生效"先查这两步；②默认域名 oxedomain.com 会导致证书错误，开局应改成客户合法注册域名。
  conditions: 网络配置变更
  tags: [warning, netadmin, certificate]

- id: n08
  title: 话务停止后 Role 地址失效——备份恢复传文件必须用物理地址
  type: warning
  source_pages: p129, p733
  source_chapter: IP addressing / Database restore lab
  source_quote: |
    p733: "AS THE TELEPHONE APPLICATION IS ALREADY STOPPED, IT IS NOT POSSIBLE TO USE CS MAIN IP ADDRESS TO TRANSFER THE BACKUP FILE. CS PHYSICAL IP ADDRESS MUST BE USED FOR SFTP SESSION."
    p129: "This address can be used to access to the Call Server, whatever the Telephone Application status (started or stopped)"
  summary: |
    Role MAIN 地址只在话务运行时生效。恢复数据库流程先停话务，此时 SFTP 必须改用 CS 物理地址（实验 192.168.1.1）——按惯性用 Role 地址（192.168.1.3）会连不上，这是恢复实验最隐蔽的坑。
  conditions: 数据库/OPS 恢复等停话务场景
  tags: [warning, restore, ip-addressing]

- id: n09
  title: 空库创建必然连 OPS 许可一起抹掉，且只能在话务停止时做
  type: warning
  source_pages: p187, p190, p192
  source_chapter: Database management / Empty DB lab
  source_quote: |
    p190: "THIS OPERATION OVERWRITES THE EXISTING DATABASE AND THE SOFTWARE LICENSE FILES. IT CAN ONLY BE PERFORMED IF THE TELEPHONE APPLICATION IS STOPPED."
    p192: "After creating an empty database, it is mandatory to restore the software licenses (See next chapter)."
  summary: |
    "Database re-init/建空库"三连约束：话务必须停、现有库与许可文件同时被覆盖、完成后必须先恢复 OPS 再重启起话务。把建空库当"重置配置"随手执行会把许可一起洗掉。
  conditions: 空库/重建库场景
  tags: [warning, database, licensing]

- id: n10
  title: 许可不一致的处置节奏——5 天自检、CPU-ID 宽限 30 天、降级三阶段
  type: limitation
  source_pages: p205-206, p214, p220
  source_chapter: Software protection / OPS lab
  source_quote: |
    p205: "the Call Server checks its OPS files every five days … In case of 'CPU-Id' incoherency, the system suspects a maintenance operation … postpones the degraded mode procedure for 30 days"
    p214: "* 30 remaining day(s) to fix this issue"
    p206: "Action 2 (4 hours later): … Internal calls are not possible"
  summary: |
    修复窗口：不一致检出即记 PANIC（话务台告警+管理命令报错），4 小时后禁内呼+全屏提示，8 小时循环；CPU-ID 不一致视为换机维护，给 30 天宽限（恢复 OPS 输出 "30 remaining day(s)…" 即此口径）。收到宽限提示要在期限内换上与 CPU/Product/ALU-ID 匹配的正式许可。
  conditions: 许可更换/换机
  tags: [limitation, licensing, degraded-mode]

- id: n11
  title: 老化密码与 RADIUS 互斥——RADIUS 场景必须关闭 aging
  type: limitation
  source_pages: p93
  source_chapter: Password security
  source_quote: |
    "This facility must be deactivated, when 'RADIUS' authentication is enabled • Indeed, if 'aging passwords' is implemented, authentication can succeed on the 'RADIUS' server but the session establishment can be refused by the OXE because the password used is no longer valid"
  summary: |
    启用 RADIUS 认证时若保留本地密码老化，会出现"RADIUS 认证通过但 OXE 拒绝建会话"的诡异故障。两套密码治理机制不能叠加。
  conditions: RADIUS 认证环境
  tags: [limitation, security, radius]

- id: n12
  title: NTP 瞬时同步必须先停 chronyd；时区改动要重启
  type: limitation
  source_pages: p172, p176, p179
  source_chapter: NTP / Date & time lab
  source_quote: |
    p172: "Instant synchronization is possible only when 'NTP' process ('chronyd') is stopped"
    p176: "Warning YOU MUST REBOOT THE SYSTEM TO APPLY MODIFICATION!"（时区）
  summary: |
    两条操作约束：瞬时同步（一次性拨钟）在 chronyd 运行时不可用，须先 Stop NTP；时区修改必须重启系统才生效。渐进同步仅支持 client/server 模式，broadcast 不支持。
  conditions: 时间同步部署
  tags: [limitation, ntp, chrony]

- id: n13
  title: crystal number 取值排除 18/19；自动分配或 DHCP 时必须登记 MAC
  type: limitation
  source_pages: p250-252, p264, p764
  source_chapter: Hardware labs
  source_quote: |
    p250: "Enter new crystal number [1..255] (values 18 and 19 are not allowed): 2"
    p251: "This attribute must be checked in 2 situations: -When crystal number is not set manually (automatic mode) in the GD board configuration -When DHCP addressing is used for GD board(s)"
    p252: "…modified in case of board replacement, otherwise the CS does not send the binaries."
  summary: |
    三条：①crystal number 1-255 且 18/19 保留（虚架 0=CS、19=INTIP 信令）；②crystal 自动分配或 DHCP 寻址时必须勾 "Ethernet Address checked by TFTP" 并在 CS 库登记板 MAC；③换板必须更新 MAC，否则 CS 不下发 binom 文件、板永远起不来。
  conditions: GD4/OMS/GDXL 通用
  tags: [limitation, hardware, mac, crystal-number]

- id: n14
  title: rstcpl 用在 GD 板上=整架重启；压缩器/子板改动必须重启板
  type: warning
  source_pages: p253, p257, p266, p772
  source_chapter: Hardware labs
  source_quote: |
    p257: "IF YOU USE THIS COMMAND ON A GD4 BOARD, ALL BOARDS OF THE SHELF WILL BE RESTARTED!"
    p772: "IF YOU USE THIS COMMAND ON A GDXL BOARD, ALL BOARDS OF THE SHELF WILL BE RESTARTED!"
    p253: "It is required to reboot the GD4 board to take into account the daughter board (use 'rstcpl …')"
  summary: |
    rstcpl <架> <板> 作用于普通接口板=单板重启；作用于 GD4/GDXL=整个机架所有板重启（业务全断）。加 ARMADA 子板或改压缩器数后必须重启该板才生效——要按维护窗口规划，别在话务高峰随手 rstcpl GD。
  conditions: 硬件维护
  tags: [warning, hardware, rstcpl]

- id: n15
  title: GD4 与 OMS/GDXL 的默认口令不同——mg4.ale 只属于 GD4
  type: misconception
  source_pages: p248, p262, p759
  source_chapter: Hardware labs
  source_quote: |
    p248: "admin [letacla1] and root [mg4.ale]"
    p262: "admin [letacla1] and root [letacla1]"（OMS）
    p759: "admin [letacla1] and root [mgxl.ale]"（GDXL）
  summary: |
    三类网关默认口令易混：GD4 root=mg4.ale；OMS root 与 admin 均=letacla1；GDXL root=mgxl.ale。另外 SSH 侧三类都只暴露 admin（root 需 su）、且只能从 CS 发起。跨机型批量维护时按机型查表，不要凭记忆。
  conditions: 首次访问（首连强制改密）
  tags: [misconception, hardware, passwords]

- id: n16
  title: OMS Shelf 三个强制字段与"禁止加板"约束
  type: warning
  source_pages: p260-261
  source_chapter: OMS lab
  source_quote: |
    "Shelf Type 'Media Gateway Large'; this type is MANDATORY for OMS declaration … Shelf Role Main (Master); MANDATORY … OXE Media Server YES; MANDATORY … OF COURSE, DO NOT DECLARE NEITHER SECONDARY RACKS NOR BOARDS IN THIS SHELF!"
  summary: |
    OMS 虚拟机架必须同时满足：类型=Media Gateway Large、Role=Main(Master)、OXE Media Server=YES；且禁止声明扩展机架与任何板卡（虚 GD4 由系统自动落 0 槽）。手工"补全"字段或往里加板会直接破坏 OMS。
  conditions: OMS 声明
  tags: [warning, oms, hardware]

- id: n17
  title: TDM 混合话机功耗门槛——110W MR3 上的预留槽位规则与事件 3757
  type: limitation
  source_pages: p299-306
  source_chapter: TDM hybrid deskphone in MR3 rack
  source_quote: |
    p300: "Incident '3757' is added to indicate if the terminal is not allowed to come in service due to power supply"
    p304: "Minimum 4 slots to deploy such deskphones in the main rack of an IPMG … Minimum 3 slots … in an extension rack … 'MG Reserved' virtual boards must be managed in the MR3"
    p303: "the power restriction only applies to the 3U rack."
  summary: |
    ALE-20h/30h 在 110W MR3 上电不足即报 3757 "UA: Power Supply Anomaly" 不入服。解决路径：换 150W MR3（R100.0 起）/加本地电源适配器/升级电源套件（仅 ps=2 机架）/在 110W 架预留 ≥4（主架）或 ≥3（扩展架）空槽并用 'MG Reserved' 虚板占位；扩展架 150W 还需 PowerMEX2/EvolMEX。功耗限制只约束 3U 架——1U 架、Crystal、本地电源不受限。ps 参数只有 GD3/PowerMEX2/GD4/EvolMEX 能上报，老 PowerMEX 板报 0。
  conditions: TDM 话机部署；版本锚点 R100.0
  tags: [limitation, tdm, power, incident]

- id: n18
  title: ALE-3 不支持远程办公场景；4059EE 关联分机禁 multiline
  type: limitation
  source_pages: p282, p482
  source_chapter: Users / Call distribution lab
  source_quote: |
    p282: "The remote worker use case is currently not supported"（ALE-3）
    p482: "Warning: This extension must not be multi-line, as it will be associated to the 4059 IP attendant (multiline set is incompatible with 4059 IP attendant)"
  summary: |
    两条选型红线：ALE-3 SIP 话机当前不支持远程办公（VPN 客户端虽有但用例未支持），别按 ALE-300 的 VPN 口径承诺；4059EE 的关联语音分机（物理话机或 IPDSP）必须是单线，multiline 分机与 4059 IP 话务台不兼容。
  conditions: 终端选型与话务台部署
  tags: [limitation, phones, attendant]

- id: n19
  title: IPDSP 无音频设备不入服；PC 防火墙可能拦端口
  type: warning
  source_pages: p310
  source_chapter: IP Desktop Softphone lab
  source_quote: |
    "Warning: IPDSP will not come in service if there are no audio devices in the PC"
    "ACCORDING TO THE FIREWALL USED ON THE PC, THE MANUAL CONFIGURATION OF THIS LAST ONE CAN BE REQUIRED."
  summary: |
    两个软话机环境坑：PC 没有可用音频设备（麦克风/扬声器）时 IPDSP 无法入服；PC 防火墙可能拦 TFTP/信令/RTP 端口（10000-10499、32512-32515、32640-32643、32512-33023、28000-39999、TCP 2535），需按附录手工放行。"IPDSP 注册不上"先查这两条再查 OXE。
  conditions: IPDSP 部署
  tags: [warning, ipdsp, ports]

- id: n20
  title: 内部 DHCP 配置改后必须重启 dhcpd；配置文件禁止手改；DHCP 池地址 netadmin 不可动
  type: warning
  source_pages: p347, p358, p362, p364
  source_chapter: Internal DHCP server / lab
  source_quote: |
    p358: "THE DHCP PROCESS RESTARTS AND READ THE '/ETC/DHCPD.CONF' FILE … IT IS MANDATORY TO DO THIS IN ORDER TO TAKE INTO ACCOUT THE MODIFICATIONS"
    p362: "Do not modify anything in this file because the file is systematically erased and created with the MAO data after each restart of the DHCP process"
    p364: "WARNING : the following trusted hosts are DHCP addresses declared by MAO, they cannot be modified by netadmin."
  summary: |
    三条：①DHCP 改动必须 Apply（dhcpd 重启才读配置）；②/etc/dhcpd.conf 每次 dhcpd 重启都按 MAO 重新生成，手工编辑会被冲掉；③DHCP 池地址自动写入防火墙规则且来源标记为 MAO、netadmin 无法修改——要缩小池请回 WBM 改。
  conditions: 内部 DHCP
  tags: [warning, dhcp, firewall]

- id: n21
  title: 防火墙白名单与 DHCP/DNS 的隐式联动
  type: limitation
  source_pages: p138, p364
  source_chapter: Firewall / DHCP
  source_quote: |
    p138: "If DNS is configured through SOT (or manually in /etc/resolv.conf), then the DNS IP should be added as a trusted host"
    p364: "the following trusted hosts are DHCP addresses declared by MAO, they cannot be modified by netadmin"
  summary: |
    联动两条：配了 DNS 就必须把 DNS 服务器 IP 加白（否则解析类功能被防火墙拦）；DHCP 池自动入白名单。排障时 iptables 里"没配过的放行条目"多半是这两个来源，不是入侵。
  conditions: 防火墙排障
  tags: [limitation, firewall, dns, dhcp]

- id: n22
  title: 换编号计划会让静态语音指南"说错号码"
  type: warning
  source_pages: p431
  source_chapter: Static voice guides
  source_quote: |
    "Caution: • Once the numbering plan has been established, modifying phone feature prefixes/suffixes may result in a voice message providing users with incorrect information."
  summary: |
    静态指南的播报内容内嵌功能前缀（如"取消呼转请拨 41"）。计划定型后再改前缀/后缀，指南仍在播旧号码，用户按提示操作会失败。改计划必须同步核对并更换指南文件（Generic 指南自带 4x/7x/*x 三套计划口径）。
  conditions: 编号计划变更
  tags: [warning, numbering, voice-guides]

- id: n23
  title: 话务员无应答会转 Absent——测试后要手动恢复 Available
  type: limitation
  source_pages: p461, p712
  source_chapter: Attendant sets / Call distribution lab
  source_quote: |
    p712: "Note that when an attendant set does not answer to a call, the attendant switches in 'Absent' mode. So, don't forget to switch back to 'Available' mode, from the console."
    p461: "Absent: • When an attendant in the idle position does not answer calls for a certain time (system timer '76'; 80 s by default)"
  summary: |
    Timer 76（80 秒）内不应答，话务员自动进 Absent，组内呈现与计时器实验结果都会随之变化——溢出测试"没按预期响铃"先查话务员是不是已经 Absent；测试完在 4059 控制台恢复 Available。
  conditions: 话务台测试与值守
  tags: [limitation, attendant, timers]

- id: n24
  title: 4059EE 只管操作不管语音——必须关联话机/IPDSP；PCX 连接要先放防火墙
  type: warning
  source_pages: p484-485
  source_chapter: Call distribution lab
  source_quote: |
    p484: "The 4059 EE handles the specific functions of the attendant but not the voice. It is mandatory to associate a physical set (ALE series) or an IP Desktop Softphone."
    p485: "Before launching the application, be sure to have allowed the 4059 EE application in your firewall rules along with 'abcacom.exe'"
  summary: |
    两条部署前提：4059EE 是纯操作台，声音完全走 "Associated phone set" 指定的话机/IPDSP，漏配则话务台接不了电话；PC 侧防火墙要放行 4059EE 程序与 abcacom.exe，否则连不上 CS（培训环境直接关防火墙是权宜之计）。
  conditions: 4059EE 部署
  tags: [warning, attendant, 4059ee, firewall]

- id: n25
  title: 实体默认 Night 态——只开 Day 放行等于没放行
  type: warning
  source_pages: p674, p677
  source_chapter: Barring lab
  source_quote: |
    p674: "THE STATE (NIGHT, DAY, MODE 1, MODE 2) ARE THE ENTITY'S STATE. BY DEFAULT, AN ENTITY IS IN THE STATE NIGHT."
    p677: "Area 2 … Night 1 (to authorized) Reminder: By default, entity is in 'night' state"
  summary: |
    Public COS 的四状态列对应实体当前状态；实体默认处于 Night。给 Area 2/3 只开 Day、不开 Night，实体在默认态时外呼照样被拒——"明明放行了还打不出去"第一查实体状态，第二查 Public COS 四列。
  conditions: 外呼闭锁
  tags: [warning, barring, entity]

- id: n26
  title: 逻辑鉴别符只能映射到已存在的真实鉴别符
  type: warning
  source_pages: p619, p672, p680
  source_chapter: SIP carrier lab / Barring lab（三处重复 Warning）
  source_quote: |
    p619: "HERE, IT IS NOT AS FOR THE REAL DISCRIMINATOR CONFIGURATION WITH THE ARS TABLE NUMBER, IT IS NOT POSSIBLE TO ASSOCIATE TO A LOGICAL DISCRIMINATOR A REAL DISCRIMINATOR NUMBER IF THIS LAST ONE IS NOT ALREADY EXISITING."
  summary: |
    与真实鉴别符规则（可先引用未建的 ARS 表号）相反，实体鉴别符选择器里的逻辑→真实映射要求真实鉴别符已存在，否则保存不了。配置顺序：先建真实鉴别符规则，再去实体做映射。教材用三处 Warning 反复强调，是高频翻车点。
  conditions: ARS/闭锁配置
  tags: [warning, discriminator, ars]

- id: n27
  title: SIP 中继不支持直抓前缀，ARS 是强制路径
  type: limitation
  source_pages: p616, p665
  source_chapter: SIP carrier / Barring
  source_quote: |
    p616: "Warning ARS IS REQUIRED TO USE SIP TRUNK GROUP WITH AN EXTERNAL SIP GATEWAY"
    p665: "Note: Direct trunk group seizure is not available for SIP trunk groups"
  summary: |
    ISDN 中继可用 "#010" 直抓，SIP 中继不行——外呼必须走 ARS 前缀+鉴别符链路。给客户做拨号计划时 SIP 出局方案里必须保留 ARS 前缀，别按 ISDN 习惯配直抓。
  conditions: SIP 中继出局
  tags: [limitation, sip-trunk, ars]

- id: n28
  title: 系统级不放行 G722/OPUS，网关级开了也无效
  type: warning
  source_pages: p612
  source_chapter: SIP carrier lab
  source_quote: |
    "IF THE G722 AND OPUS ALGORITHMS ARE NOT ALLOWED HERE AT THE GENERAL LEVEL OF THE SYSTEM, EVEN IF IN THE EXTERNAL GATEWAY SETTINGS, G722 IS ALLOWED, IT WILL NOT BE USED AND THEREFORE THE SYSTEM WILL USE G711 INSTEAD."
  summary: |
    编解码开关是两级与逻辑：System/Compression parameters 的支持范围（Network and local / local only / not available）∩ 外部网关的 Support G722/OPUS。系统级不放行，协商会静默回落 G711——"明明开了 G722 还是 G711 音质"按此顺序排查。另注意 OPUS 与 G722 只有 OMS 软件媒体网关支持，硬件 IPMG 不支持。
  conditions: SIP 中继与编解码
  tags: [warning, codecs, sip-trunk]

- id: n29
  title: 紧急号码显示管理是模拟器特设口径，生产必须按运营商文档
  type: warning
  source_pages: p636, p611, p642
  source_chapter: SIP carrier labs
  source_quote: |
    p636: "THIS MANAGEMENT IS LINKED TO THE USE OF OUR SIP SIMULATOR CARRIER AND CAN BE DIFFERENT ACCORDING TO THE REAL CARRIER USED AND NUMBERS FORMAT USED BY THIS LAST ONE."
    p611: "THIS MANAGEMENT MUST BE DONE ACCORDING TO THE SIP PUBLIC PROVIDER REQUESTS! PLEASE CONSULT THE DOCUMENTS (TC 2005, AND ADDITIONAL ONE…)"
  summary: |
    回叫翻译器的紧急号规则（A15/A17/A18/A112 去 1 加 0）、登记账号（pbxP/alcatel）、域名（sip.itsp1.fr）全部是 ITSP1 模拟器口径；真实运营商的号码格式、CLIR、紧急显示要求各不相同，必须按 TC2005 与运营商技术通报重做，不能照抄实验配置。
  conditions: SIP 中继生产化
  tags: [warning, sip-trunk, lab, emergency]

- id: n30
  title: SIP Pool 互备依赖 Supervision timer——不配短探活切换就慢
  type: warning
  source_pages: p651-652
  source_chapter: SIP carrier backup lab
  source_quote: |
    "THE SUPERVISION TIMER IS IMPORTANT TO MONITOR THE GATEWAY, TO SWITCH ON THE OTHER ONE, IF THIS ONE IS OUT OF ORDER."（例值 5 秒）
  summary: |
    双网关 Pool 互备的切换速度由 Supervision timer（OPTIONS 探活周期）决定，默认值下感知故障很慢；实验配 5 秒。生产按运营商容忍度设短值，否则主网关宕机后用户会经历长时间呼叫失败。
  conditions: 网关备份/负载均衡
  tags: [warning, sip-gateway, backup]

- id: n31
  title: 紧急通知仅限 stand-alone 单节点、ARS 强制、组容量 10 台
  type: limitation
  source_pages: p683, p699
  source_chapter: Emergency calls notification
  source_quote: |
    p683: "Feature available only for stand-alone systems: single node, PCS excluded … Only one emergency group in the OXE system: • Maximum 10 devices in the system emergency group • Any NOE device with minimum 3 lines display … Only business mode"
    p699: "Warning ARS USE IS MANDATORY FOR EMERGENCY CALLS NOTIFICATION."
  summary: |
    边界四条：单节点（PCS/组网 excluded）；必须启用 ARS；全系统仅 1 个紧急组且 ≤10 台设备；设备限 ≥3 行显示的 NOE 商务话机/IPDSP、business 模式（客房/坐席/话务台/DSS 不行）。组网客户或超大站点要用位置服务须另选方案。
  conditions: 紧急通知
  tags: [limitation, emergency]

- id: n32
  title: Location ID 发送强依赖 Direct IP Link；仅 SIP 中继外呼支持
  type: limitation
  source_pages: p605, p693
  source_chapter: Caller geolocation / emergency lab
  source_quote: |
    p693: "THE USE OF DIRECT IP LINKS BY THE SYSTEM IS A MANDATORY PREREQUISITE FOR SENDING LOCATION ID."
    p605: "If caller and SIP trunk group are on different nodes, these nodes must be connected via 'Direct Link' (no hybrid link) • Not supported: OXE not in direct link mode, ABC-F network with hybrid links, inter ABC-F sub-networks calls • In case of heterogeneity in network (<= N2 version), this feature is discarded, but no call drop"
  summary: |
    P-ANI 位置头的前置与边界：系统必须启用 Direct IP Link；跨节点必须直连（混合链/跨 ABC-F 子网不支持）；仅 SIP 中继外呼携带；≤N2 异构网络自动弃用（不掉话）。"紧急呼叫不带位置"先核对这些再查 NPD/P-ANI 配置。
  conditions: Location ID / 紧急位置
  tags: [limitation, p-ani, location, network]

- id: n33
  title: 4645 一节点仅一个留言系统；VM 不冗余；仅 G711
  type: limitation
  source_pages: p527, p536, p538
  source_chapter: OmniMessage 4645
  source_quote: |
    p527: "Only one voice mail system (4645 or other) per OXE node"
    p536: "The voice mail is not duplicated … If the CS that embeds the voice mail fails, the voice mail also fails"
    p538: "4645 supports only G711 algorithm"
  summary: |
    三条硬边界：一节点只能有一套留言系统（4645 或其它）；嵌在主备之一的拓扑里 VM 不冗余——承载 CS 垮则留言垮（主 CS 负责保障 VM 运转）；仅支持 G711，非 G711 终端经本地板转码每路吃 2 个压缩器。容量承诺按 7000 箱/30 端口/500(600) 小时口径。
  conditions: 4645 部署
  tags: [limitation, 4645, voicemail]

- id: n34
  title: 4645 基础语音指南不能从话机录制；邮件通知默认关闭
  type: limitation
  source_pages: p528, p564
  source_chapter: OmniMessage 4645
  source_quote: |
    p528: "The basic voices guides can be recorded by the 'Alcatel Audio-Station' (no recording from sets)"
    p564: "E-mail notification None: no notification (default value)"
  summary: |
    两条：4645 的公司问候/自动话务员等基础指南只能用 Audio-Station 工具录制（与 OXE 静态指南可从话机录的规则不同）；邮件通知三档中 None 是默认值——"留了言没邮件"先查用户 4645 CoS 是不是还停在 None，再看 SMTP 声明与防火墙白名单。
  conditions: 4645 使用
  tags: [limitation, 4645, email]

- id: n35
  title: SMTP 发件域不符会被对方判垃圾邮件；端口按协议类型区分
  type: limitation
  source_pages: p560
  source_chapter: 4645 e-mail notification lab
  source_quote: |
    "Some SMTP servers process the mail, based on the from address domain. If the domain is not expected domain name, then it will be considered as SPAM mail. … If the field 'from address' is not configured, then default from address with OXE domain name is used in email. 'from address' must be in an email address format."
    "The default port number for all three protocol types: Plain – 25 • StartTLS – 587 • TLS – 465"
  summary: |
    4645 邮件通知被吞的两个常见根因：from address 域名与 SMTP 服务器期望不符（缺省用 OXE 域名）；端口没按协议选（Plain 25/StartTLS 587/TLS 465）。netadmin 的 SMTP 声明在双 CPU 系统要同步 twin、独立 4645 CPU 必须配在 4645 CPU 上而不是主备上。
  conditions: 4645 邮件通知
  tags: [limitation, smtp, email]

- id: n36
  title: 4645 声明必须用物理地址而非 Role 地址
  type: limitation
  source_pages: p549
  source_chapter: OmniMessage 4645 lab
  source_quote: |
    "Voice Mail CPU Name: Name or IP Address where is implemented The Alcatel-Lucent 4645 (warning: don't use role address)."
  summary: |
    WBM 里 4645 实例的 Voice Mail CPU Name 要填 4645 所在服务器的物理地址/主机名（实验 192.168.1.1），填 Role 地址会导致 VM 注册路径随话务主备切换漂移。
  conditions: 4645 声明
  tags: [limitation, 4645]

- id: n37
  title: 备份恢复的三个隐藏坑——物理地址 SFTP、Binary 传输、secure/archive 选项
  type: warning
  source_pages: p721, p726, p733, p736
  source_chapter: Database backup & restore
  source_quote: |
    p733: "CS PHYSICAL IP ADDRESS MUST BE USED FOR SFTP SESSION."
    p726: "Do you wish to secure the restoration (y/n): y … Do you wish to restore Cloud and Rainbow services (y/n): n"
  summary: |
    三个易踩点：①停话务后只能用 CS 物理地址 SFTP；②传输类型必须 Binary（文本模式会损坏备份）；③恢复时的 secure restoration（先存当前库为回退档案）与 "restore Cloud and Rainbow services"（实验室选 n 防止用客户云凭据连生产云）要按场景选，选错 either 白做或把生产凭据带进实验室。
  conditions: 备份恢复
  tags: [warning, backup, restore, cloud]

- id: n38
  title: Crystal 硬件已退场、书中不再深入——新项目按 Common/XL/虚拟化选型
  type: limitation
  source_pages: p70, p72
  source_chapter: Crystal hardware
  source_quote: |
    p70: "Note that crystal hardware is no more covered in details during the training session Please refer to the technical documentation if required."
    p72: "Reasons • Scarcity of components … • Market trend / significant sales decline • Offer evolution • Transition to common hardware or to a fully software/IP solution • New XL-rack introduction"
  summary: |
    Crystal（CPU8/ACT/M2/M3）因元器件稀缺退场，教材自注不深入；高密度模拟口新需求由 XL 机架承接。存量 Crystal 站点的扩容/迁移方案在技术文档与专门课程里，Starter 教材不给路径。XL 参数多处为占位（mgxl_XX.XX），实施前取最新文档。
  conditions: 硬件选型
  tags: [limitation, crystal, xl, version]

- id: n39
  title: UMC 是 R1.1 快速演进中的云功能——多处 NEXT DELIVERY，且有一串排除项
  type: version-trap
  source_pages: p797, p801-806, p813
  source_chapter: Unified Management Center
  source_quote: |
    p799: "Note: Functionality available from OXE N3-MD3"
    p802: "Not included in the UMC Easy user management • Attendant, ACD, ALE SoftPhone agent • SIP 3rd party (except VTECH SIP hotel) • DECT GAP basic 3rd party (but DECT GAP basic 8214 is taken into account) • Multi-entity configurations • Hotel room suites … • Hotel guest user • Multi-country management of callback number"
    p805: "Desk Sharing (NEXT DELIVERY)"
  summary: |
    UMC 边界：功能自 N3-MD3 起、容量 Mid-Market 500 用户 day one；Easy users 不覆盖话务台/ACD/ALES 坐席/第三方 SIP（除 VTECH 酒店）/第三方 DECT GAP（8214 除外）/多实体/酒店套房与宾客/多国回叫号；Easy SIP trunk 不支持 Mini SIP；Desk Sharing 等标注 NEXT DELIVERY。按 R1.1 截图做方案会在这些排除项上翻车。
  conditions: UMC 规划
  tags: [version-trap, umc, cloud]

- id: n40
  title: Easy SIP trunk 前缀冲突规则——非 ARS 前缀直接拒绝
  type: limitation
  source_pages: p808
  source_chapter: Unified Management Center
  source_quote: |
    "If the prefix number already exists in OmniPCX Enterprise and is not an ARS prefix, then the SIP trunk creation is refused by UMC. • If the prefix number already exists … and is an ARS prefix, or if it is not existing then: • If no discrimination already exists …, discrimination and SIP trunk are created by UMC • Else only the SIP trunk is created by UMC"
  summary: |
    UMC 建中继时的前缀三岔口：已存在且非 ARS 前缀→拒绝；已存在且是 ARS 前缀或不存在→继续，且仅在系统尚无鉴别符时连带创建鉴别符，否则只建中继、鉴别符留给手工。用 UMC 的站点要先理清存量前缀/鉴别符，否则"向导走完了还是打不出局"。
  conditions: UMC SIP 中继
  tags: [limitation, umc, sip-trunk]

- id: n41
  title: 安全文档只给指针——4645 防盗打与加固在 SA0046/TC1774
  type: out-of-scope
  source_pages: p544-545, p611
  source_chapter: OmniMessage 4645 security / SIP carrier
  source_quote: |
    p544: "The phreaking is a business run by organised crime … The victims can loose more than 20 K€ in one weekend"
    p545: "Apply the Voice mail configuration rules described into the following documents: • SA0046: Voicemail phreaking prevention and security measures • TC1774: Reinforce security on 46x5 voicemail systems"
    p611: "PLEASE CONSULT THE DOCUMENTS (TC 2005, AND ADDITIONAL ONE…) GIVEN BY ALE OR THE PUBLIC OPERATOR"
  summary: |
    Starter 只给安全意识（盗打=打客户钱包）与文档指针：语音邮件加固 SA0046/TC1774；SIP 运营商参数 TC2005。语音加密、SBC、防火墙深度策略都不在本书展开。生产交付必须补读这三份文档，Skill 的 Boundary 应显式引用。
  conditions: 安全与运营商接入
  tags: [out-of-scope, security, phreaking, documentation]

- id: n42
  title: 深度主题全部外置——Advanced/CPU Loading/ENTPXTE402 等课程边界
  type: out-of-scope
  source_pages: p131, p219, p297, p813
  source_chapter: 各章注记
  source_quote: |
    p131: "If the 2 CS (Main/Stand-by) are in 2 different IP subnets: spatial redundancy • Topic covered in 'Advanced' training"
    p219: "The Flexlm topic is covered in another training ('CPU Loading')"
    p813: "Refer to ENTPXTE402 ebook (Cloud Connect chapter)"
    p297: "For more details refer to documents on MyPortal website • 'Sales Companion' • 'OXE Feature list' • 'OXE product limits' …"
  summary: |
    书内明示的外置清单：空间冗余/组网→Advanced；FlexLM/CPU 装载→CPU Loading 课程；Cloud Connect→ENTPXTE402；产品限额/特性清单/话机手册→MyPortal 文档组。Starter 的 Boundary 是"一台系统的最小可用闭环"，跨边界需求要显式转引。
  conditions: 全书
  tags: [out-of-scope, training, documentation]

- id: n43
  title: 事件流里的"非故障"现象——BAD PCMS CODE/unknown rack type/484 Address Incomplete
  type: misconception
  source_pages: p214-215, p253, p623
  source_chapter: OPS lab / Hardware labs / SIP lab
  source_quote: |
    p214: "Warning rack 1-254: unknown rack type at line 101"（恢复 OPS 输出）
    p253: "| 2 | 0 | (GD4<cpu mode>) | IN SERVICE | BAD PCMS CODE |"
    p623: "SIP/2.0 484 Address Incomplete"（DID 未配时的预期来话失败）
  summary: |
    实验输出中的三类"看着像故障的正常现象"：恢复 OPS 时 unknown rack type 提示（实验室机架模型差异）、config 输出的 BAD PCMS CODE（实验环境的耦合器代码占位，板仍 IN SERVICE）、DID 翻译器未配时来话回 484（正是下一步配 DID 的动因）。初学者易把这些当事故上报；判读以 incinfo 释义与业务结果为准。
  conditions: 实验/开局初期
  tags: [misconception, troubleshooting, incidents]
```

---

## 收尾自检 — 对照 BOOK_OVERVIEW.md 29 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | 登录与账户密码治理 | 有 → n01（实验密码）、n04（root 限制） |
| task-02 | 系统启停 | 有 → n05（(E) 不刷新）、n06（Easy 7 取消 autostart） |
| task-03 | CS IP 双地址 | 有 → n07（netadmin 重启/域名）、n08（物理地址规则） |
| task-04 | 内部防火墙 | 有 → n02（默认全关）、n03（SSH 便门）、n21（DNS/DHCP 联动） |
| task-05 | NTP/chrony | 有 → n12（瞬时同步/重启） |
| task-06 | 空数据库 | 有 → n09（抹许可） |
| task-07 | OPS 与 FlexLM | 有 → n10（宽限节奏）、n38 相关；n43（unknown rack type） |
| task-08 | GD4 上架 | 有 → n13（crystal/MAC）、n14（rstcpl）、n15（口令差异） |
| task-09 | OMS 上架 | 有 → n15、n16（强制字段） |
| task-10 | XL 上架 | 有 → n14、n38（占位参数） |
| task-11 | IP 话机开通 | 有 → n43 相关（484 为 SIP 侧）；c12/c14 承接操作 |
| task-12 | IPDSP | 有 → n19（音频/防火墙） |
| task-13 | User Profile | 无独立边界（可选提效手段，无强制约束）；操作归 c11 |
| task-14 | 数字/模拟用户 | 有 → n17（TDM 功耗） |
| task-15 | 内部 DHCP | 有 → n20（三条）、n21 |
| task-16 | 编号计划 | 有 → n22（指南失真） |
| task-17 | 两级 COS | 有 → n23 相关（Absent 影响测试）；n25（实体状态） |
| task-18 | 语音指南与 MOH | 有 → n22 |
| task-19 | 话务台与 4059EE | 有 → n18（multiline）、n23（Absent）、n24（语音/防火墙） |
| task-20 | Entity 与 CDT | 有 → n25（Night 默认） |
| task-21 | 4645 与邮件通知 | 有 → n33（单实例/不冗余/G711）、n34（录制/默认关）、n35（SMTP）、n36（物理地址） |
| task-22 | 公共 SIP 中继 | 有 → n26（鉴别符顺序）、n27（禁直抓）、n28（编解码）、n29（模拟器口径）、n30（Supervision timer） |
| task-23 | 外呼闭锁 | 有 → n25、n26 |
| task-24 | 紧急通知 | 有 → n29（显示口径）、n31（边界）、n32（Location ID） |
| task-25 | 呼叫分配计时器 | 有 → n23 |
| task-26 | 备份恢复 | 有 → n37（三坑）、n08 |
| task-27 | 维护工具 | 有 → n43（非故障现象） |
| task-28 | T0/T2 中继组 | 有 → n27（直抓对比）、n29（信令变体口径） |
| task-29 | UMC | 有 → n39（排除项/版本）、n40（前缀规则） |

**29/29 中 28 项有边界类条目覆盖，无空缺（task-13 为无约束的可选操作，已注明）。**

### 扫描完整性说明（Warning/Note/Tips 标记逐条核对，全书共 118 处命中）

- 已全部入册的 Warning/Attention 框：p99/p102（root 本地直登、client 需话务）→n04/n02；p124（Easy7 取消 autostart）→n06；p139/p162（CSV 格式）→principle p05；p146/p148（netadmin 三警告+重启）→n07；p176（时区重启）→n12；p190/p191（空库抹许可）→n09；p219（FlexLM 重启）→principle p13；p246/p247/p261（OPS 自动建架/板位/OMS 禁加板）→n16；p257/p772（rstcpl 整架）→n14；p310（IPDSP 音频/防火墙）→n19；p358（dhcpd 重启）→n20；p364（DHCP 地址不可改）→n20/n21；p482/p484/p485（4059 三警告）→n18/n24；p611/p612/p616/p619/p629/p632/p636/p642/p647/p649/p651/p655（SIP 章九处）→n28/n26/n27/n29/n30；p672/p674/p680（Barring 三处）→n25/n26；p692/p693/p699（Location ID/紧急组）→n32/n31；p733（物理地址）→n37/n08；p764/p766（XL 动态/MAC、GA-XL 机位）→n13、principle p17；p784/p785/p792/p793（TG 节点号/重置板）→principle p36；p692 Attention（Location ID 用途不限紧急）→principle p32 口径。
- 已入册的 Note/Important 类：p70（Crystal 不再深入）→n38；p96/p98（虚化参照/提示符）→n05；p117（role 不刷新）→n05；p123（Tips：提示符语义）→n05；p152（SSH 便门口径）→n03；p157（Deny 后可信主机仍可 SSH）→n03；p190 Note1/2（FR 国家码）→principle p38；p214/215/253（unknown rack type/BAD PCMS）→n43；p248/p262 NOTE（GD4/OMS 访问通道）→n15；p310/316（IPDSP 警告/Profile 可选）→n19/c11；p440（CD-ROM 目录）→c18；p451（话务台必须属组）→principle p25；p482-485 Tips（管理员运行）→c19；p558/560/568（hosts 查看/SMTP 域名/回归外线）→n35；p568 Note（外线通知待 SIP 章）→c22 verification；p615/p644（G729 建议恒开）→principle p30；p638/642/647/649/653/655 Tips（SIPMOTOR 重启/改回配置）→c23/c24；p712（Absent 恢复）→n23；p741（trace 归档）→c32；p748（ippstat -noname GDPR）→c32；p759/763/766（XL 口令/DHCP 类/机位建议）→n15/principle p17；p799（N3-MD3）→n39；p816（评估必做）→不入册（培训流程，OVERVIEW 已列不适合）。
- 复核后排除的纯操作提示（非边界类）：p371/372（TIPS FOR NUMBERING PLAN 为章节标题）、p379/748/784/793（表格行首词误命中）、p545 末句（用户改密宣导，并入 n41 摘要）、p560（端口默认值）→principle p27、p650/652 Note（Pool 语义）→c24、p763 Note（TFTP 留空语义）→principle p21。
- 推断性结论已在对应条目标注"（推断）"：本文件无纯推断条目；n43 对 BAD PCMS CODE 的"实验环境占位"判断基于实验输出上下文，属谨慎解读。
- 版本号均按原文保留完整位数：N3、R101.0、R100.0、R100.1、N3-MD3、R101.1 MD4、Edition 12。
