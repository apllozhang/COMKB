# 案例/实验/操作序列候选 — OmniTouch Contact Center Standard (OTCCXTE100EN Ed09)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号、公网号码）标注"实验口径"。
> 条目说明: 全书 20 个 How-To 实验章 → 20 条（c01-c20），一一对应，不拆分不合并。页码按 PDF 页标记（===== PAGE N =====）。

```yaml
- id: c01
  title: 创建基础 CCD 矩阵（ACD 前缀 + 3 个处理组 + 3 个队列 + 2 个 Pilot + acdsup 验证）
  type: lab
  source_pages: p63-77
  source_chapter: Basic CCD matrix creation (How-To)
  source_quote: |
    "Select Translator> Prefix Plan> … Number Enter the ACD prefix number (i.e. 12). … The ACD prefix
    is mandatory prior to create the CCD matrix objects." (p66)
    "Select Applications> CCD> Processing Group> … Directory Number Enter the directory number of the
    processing group (i.e. 31800) … Type Enter the type of processing group (i.e. Agent)" (p67)
    "From an OXE SSH session, check the CCD matrix configuration. … Enter the command acdsetup …
    A=agent group F=Forward group V=Voice guide processing group CLO= pilot closed" (p76-77)
  steps: |
    1. OXE Web Admin（https://192.168.1.3，mtcl/Superuser2580*，实验口径）。
    2. 建 ACD 前缀：Translator> Prefix Plan> Create——Number=12、Prefix Meaning=Local Features、
       Local Features=ACD Prefixes → Save。
    3. 建座席组：Applications> CCD> Processing Group> Create——DN=31800、Name=Agent_PG、Type=Agent → Save。
    4. 前置：Client PC 10 上把 MicroSIP-31010、MicroSIP-31011 拉起并确认 Online 状态。
    5. 建前转组：Applications> CCD> Processing Group> Create——DN=31801、Name=Forwarding_PG、
       Type=Forwarding、Manual closure=False、Forwarding directory number=31010 → Save。
    6. 建语音指南组：Applications> CCD> Processing Group> Create——DN=31802、
       Name=Voice_guide_PG、Type=Voice guide → Save（指南号后改）。
    7. 建队列：Applications> CCD> Queue> Create——Normal_WQ（31700，Type=Normal）、
       Overflow_WQ（31701，Type=Intelligent Overflow）、Redirection_WQ（31702，Type=Redirection）。
       注意：原书三步表格字段值均误写 31701/Overflow_WQ（见 n12），实际 DN/名称按本步骤。
    8. 建 Pilot：Applications> CCD> Pilot> Create——Pilot1（DN=31600）、Pilot2（DN=31601）→ Save。
    9. 验证：Client PC 10 运行 PuTTY（会话 OXE-SSH，Window>Colours 勾 Use system colours，
       Window>Translation 远程字符集选 ISO-8859-1:1998 并勾 Use Unicode line drawing code points，
       Save 后 Open，首连 Accept），mtcl 登录后执行 acdsetup/acdsup 查矩阵。
  verification: |
    acdsup 输出中可见：A=agent group、F=Forward group、V=Voice guide processing group、CLO=pilot
    closed（此时无座席登录、规则未建，pilot 为关闭态）。
  conditions: OXE VM 已预配置（许可恢复、FlexLM 192.168.1.80、机架/板卡已建、公共 SIP 中继组已建）。
  tags: [lab, ccd-matrix, web-admin, acdsup]

- id: c02
  title: CCS 软件安装与 OXE 声明（安装向导 + node1 直连 + Navigator 首登改密）
  type: lab
  source_pages: p89-97
  source_chapter: CCS software installation and set up (How-To)
  source_quote: |
    "Right click on CCS.msi and select Open. … On Feature level window, select Full … On Feature level
    license window, select Monosite." (p91-92)
    "From Network menu, select node1 and click on Modify … Master PABX name Enter the IP address of
    the Call Server (i.e. 192.168.1.3)" (p94-95)
    "User name Enter the login user name (i.e. administrator) … Password Enter the default password
    (i.e. alcatel) … You will be asked to change the password" (p96)
  steps: |
    1. Client10 PC：从 OTCC_NAS 网络盘把 CCS 软件拷到 Documents，右键 Open → More info → Run anyway
       → 默认路径 Extract。
    2. 运行 CCS.msi：EULA 接受 → 默认安装路径 → （自动装 VC++ 2017 x86）→ Feature level=Full →
       许可=Monosite → Excel=Yes（高级统计报表）→ Excel 文件默认位置 → 语言保留 English+French、
       界面 English → Setup type=Windows standalone → 用户文件默认路径 → Station ID 核对 →
       Real Time Information when logged-off=Yes → ASM Script Editor=No → Install → ccs.ini 合并提示
       OK → Finish。
    3. 启动 CCsupervision → Window > Customise… → Network 菜单选 node1 → Modify → Direct access：
       勾 Connected at start up、连接方式 Direct connection、Master PABX name=192.168.1.3 → OK →
       确认修改 Yes → 提示重启 CCS 的 OK → 关闭 CCS。
    4. 重启 CCS（重启原因：ccs.ini 要写入呼叫服务器 IP，p95 Notes）。
    5. 登录：administrator/alcatel（默认，实验口径）→ 强制改密为 Superuser01*（实验口径，须符合
       安全规则）→ 用新密码重登。
    6. Real time > Navigator 查看矩阵。
  verification: |
    Navigator 中能看到 OXE CCD 阵列。书中注明：此时矩阵尚未连通（pilot-队列-处理组之间无连线），
    下一实验补齐。
  conditions: CCS 站与 OXE 网络可达；重启 CCS 是 IP 声明生效的必要动作。
  tags: [lab, ccs, installation, navigator]

- id: c03
  title: 创建路由规则与分配规则（pilot rule + 方向 + 优先级 + 分配规则激活 + Navigator 矩阵）
  type: lab
  source_pages: p98-120
  source_chapter: Creation of the rules (How-To)
  source_quote: |
    "From the main menu, select Call Flow mgt > Call Routing … From Pilot rule area, click on Create
    … Rule Name Enter the rule name (i.e. Rule_0)" (p99-100)
    "Select Applications> CCD> Distribution Rule> 0-Rule_0 … Active Rule Tick the option to activate
    the distribution rule." (p113)
    "Warning … BY DEFAULT, ALL DIRECTION RULES ARE CLOSED" (p117)
  steps: |
    1. 业务目标（p99）：Pilot1(31600) 常态走 Normal_WQ→Agent_PG，饱和走 Overflow_WQ→语音指南组；
       Pilot2(31601) 常态走 Normal_WQ→Agent_PG，饱和走 Redirection_WQ→前转（31010）。
    2. 建 pilot 规则：CCS Call Flow mgt > Call Routing → 选 Pilot1 → Pilot rule 区 Create → Rule_0 →
       OK → Yes → Apply → Yes；Pilot2 同样操作。
    3. 核验：OXE Web Admin Applications> CCD> Pilot> 31600-Pilot1> Pilot Rule Guide 确认 Rule_0
       已应用（31601 同）。
    4. 建路由方向：CCS Configurations> Pilot → 选 31600 → Call Routing 区依次加 Normal_WQ、
       Overflow_WQ 到 Possible queues → OK；31601 加 Normal_WQ、Redirection_WQ → OK。
    5. 核验方向：Navigator 看连接点；OXE 侧 Pilot Rule Direction 查 routing direction 0/1 上队列号。
    6. 激活路由：Call Flow mgt > Call Routing → 选 Pilot1 → Normal mode 页签 → 对 Normal_WQ 与
       Overflow_WQ 启用 Normal → Save 并确认；Pilot2 同样。
    7. 改方向优先级：同页签把 Normal_WQ 设 0、Overflow_WQ（Pilot1）/Redirection_WQ（Pilot2）设 9 →
       Save（数字越小优先级越高，默认 Normal 队列已高于其它）。
    8. 建分配规则：Call Flow mgt > Call Distribution → Create → Rule_0 → OK → Yes。
    9. 激活分配规则：OXE Web Admin Applications> CCD> Distribution Rule> 0-Rule_0 → 勾 Active Rule →
       SAVE（默认停用，必须 OXE 侧激活；也可经 CCS 日历激活）。
    10. 建分配方向点：CCS Configuration> Queue and Waiting Room → Normal_WQ 加 Agent_PG、
        Overflow_WQ 加 Forwarding_PG、Redirection_WQ 加 Voice_guide_PG → OK；Navigator 中连接点
        黄色=已建未激活。
    11. 激活方向：Navigator 中点连接点进 Call Distribution 界面 → 对三个队列分别选 Rule_0 →
        Resource selection 页签勾 Direction → Save（连接点变红/绿）。
  verification: |
    Navigator：队列-PG 连接点红/绿色（已激活）；Agent_PG 因无座席登录仍为红色。OXE mtcl 会话执行
    acdsup：OPN=Open（pilot 正常态，p120）。
  conditions: c01/c02 已完成；分配规则激活必须回 OXE 侧。
  tags: [lab, routing-rule, distribution-rule, priority, activation]

- id: c04
  title: 创建 ACD 话机、座席与班长并完成登入验证
  type: lab
  source_pages: p121-149
  source_chapter: Creation of the ACD-authorized sets, agents and supervisor (How-To)
  source_quote: |
    "Directory Number Enter the directory number (i.e. 31000) … Set Type Enter the set type (i.e.
    IPTouch 8068s) … ACD station Select the ACD function of the set (i.e. ACD authorised phone set)" (p124-125)
    "Self-assigning means that the agent can log himself in any desired processing group." (p137)
    "To directly call the agent without listening to the pilot presentation guide, you must delete
    tone number 70." (p147)
  steps: |
    1. OXE Web Admin：Users>Create 建 3 台 ACD 话机——31000/PRO1、31001/PRO2、31002/PRO3，
       Set Type=IPTouch 8068s，Miscellaneous 页签 ACD station=ACD authorised phone set → Save。
    2. IP 软话机仿真：Users>31000>TSC IP User>31000 – IPTouch 8068s → IP-Softphone Emulation=YES →
       Save（31001/31002 同）。
    3. 建座席：Users>Create——31500/Agent1、31501/Agent2（IPTouch 8068s，ACD station=Agent）。
    4. 建班长：Users>Create——31502/Supervisor（IPTouch 8068s，ACD station=Supervisor）。
    5. 放行 ACD 前缀：Users>31500>Rights 查 Phone Feature COS=0（默认全员 0）；Classe of Service>
       Phone Features COS> 0 → PCX SERVICES 区启用 ACD Prefixes=1 → Save。
    6. 座席规则（CCS Configurations> Agents）：Agent1——Password at log-on 禁用、Self-Assigning
       Agent 启用、Associated set no.=31000（固定在 31000）；Agent2——密码禁用、Self-Assigning 禁用、
       不选话机（移动座席）。OXE 侧 Applications> CCD> CCD Users> CCD Operations data management>
       31500 查 AGENT FEATURES 核验。
    7. 挂组（CCS Configurations> Agents）：Agent1>Add>Agent_PG→OK（自指派，登录时自选组）；
       Agent2>Add>Agent_PG→OK 且 Preferred GT Agents=Agent_PG（非自指派必须设优选组）；
       Supervisor>Add>Agent_PG→OK、Password at log-on 禁用（班长自动自指派、无优选组）。
    8. 登入 Agent1：Client PC 10 启动 IPDSP → 按键注册（分机 31000 + 个人码 0000，实验口径）→
       Menu 页签下翻 → LogOn →（自指派）点 List 选 Agent_PG → 登入成功。
    9. 登入 Agent2：Client PC 11 的 IPDSP 注册 31001/0000 → LogOn → Identification 输 31501 →
       （优选组 Agent_PG 自动生效）登入。
    10. 关欢迎指南：CCS Call Flow mgt> Call Routing → Pilot1/Pilot2 → Additional 页签 → Normal Table
        双击 Presentation Guide → 删除指南号 70（免听欢迎语直振座席）。
  verification: |
    Real time> Navigator：登入前 Agent_PG 因无座席为 blocked；Agent1 登入后 Agent_PG 变 open、
    所有 pilot 激活（p144-145）。真实呼叫验证留待下一实验。
  conditions: c03 已完成；IPDSP 注册码 0000 为实验口径。
  tags: [lab, agents, supervisor, logon, self-assigning]

- id: c05
  title: 收尾 POD 配置（公网软话机、SIP 网关 POD 参数、DID 翻译、外呼 Pilot 实测、RDP 音频）
  type: lab
  source_pages: p150-158
  source_chapter: Finalizing the pod configuration - OTCCXTE100EN (How-To)
  source_quote: |
    "configure 2 parameters in your external SIP gateway: • Registration ID: pbxN (where N is your
    POD Number) … • Outgoing username= pbxN" (p153)
    "First external number 33210N41000 (where N is your POD Number) … First internal number 31000
    … Range Size 1000" (p154)
    "Remote audio playback Select the option 'Play on this computer'. Remote audio recording Select
    the option 'Record from this computer'." (p157)
  steps: |
    1. RLAB 面板确认五台 VM 已启动（OXE/OMS/FlexLM/Client10/Client11）。
    2. 机架核验（OXE 侧）：MAIN 站 Software Rack 3U (OMS)，Rack n°4，Virtual GD4 slot 0，
       IP 192.168.1.13/24，MAC 00:50:56:01:01:13（实验口径）。
    3. 公网软话机：Client PC 10 启动 MicroSIP – Public → 选 Public POD X profile（X=POD 号）→
       确认 Online。
    4. SIP 网关参数化：OXE WebAdmin（本章登录口径 mtcl/mtcl，实验口径，见 n11）→ SIP> SIP Ext.
       Gateway → 选外部网关 → Registration ID=pbxN、Outgoing username=pbxN（N=POD 号，如 POD6
       填 pbx6）→ 保存。
    5. DID 翻译：Translator> External Numbering Plan> Default DID num. translator> Create——
       First external number=33210N41000、First internal number=31000、Range Size=1000。
    6. 外呼实测：MicroSIP – Public 拨 0210X41600 打 Pilot1 → Agent1 应答；挂机后座席自动 wrap-up；
       再拨 0210X41601 打 Pilot2 同样验证（X=POD 号）。
    7. RDP 串联：按 RLAB 学员指南建到 Client PC 10 的 RDP；再从 PC10 的 Guacamole 会话内开到
       PC11（192.168.1.11）的远程桌面，Local Resources>Remote audio Settings：播放与录音均选
       "…this computer"；勾"不再询问"→ Yes；把 PC11 窗口最小化并对齐 IPDSP，单屏容纳全部软话机。
  verification: |
    两个 pilot 外呼均可接通到 Agent1 且挂机后进入 wrap-up（p154-155）；PC11 音频在 PC10 会话可用。
  conditions: OXE 预置库含公共 SIP 中继组与语音指南；本章 WebAdmin 密码 mtcl 与其余章节
    Superuser2580* 不一致（书内矛盾，见 n11）。
  tags: [lab, pod, sip-gateway, did, rdp]

- id: c06
  title: 开通本地 ABC-F 混合链路（内呼 Pilot 31600 的前提）
  type: lab
  source_pages: p159-165
  source_chapter: Local hybrid ABC-F link (How-To)
  source_quote: |
    "Warning … ABC-F LINK MUST BE DELARED ON THE SAME NODE, BUT IN A DIFFERENT NETWORK" (p162)
    "Select Inter-Nodes Links> Logical Links (ABC-F)> Loop-Hybrid … Multi access hybrid link Check
    that feature is enabled (i.e. YES). At least two acesses must be created." (p163)
    "Type hybvisu -f all … The two accesses must be 'UP'. … In the event of congestion, use the rsthyb
    command to restart the ABC-F link." (p165)
  steps: |
    1. 试内呼：MicroSIP 拨 31600；不通则需建/改本地混合链路。
    2. 前置检查：OXE Web Admin System 页查 Node 号与 Network 号（链路必须同 Node、不同 Network）。
    3. 查 pilot 放行：Applications> CCD> Pilot> 31600-Pilot1> 末尾 Routing Direction 区确认
       ABC Local Call Allowed 已启用（法国目标默认启用；31601 同）。
    4. 查链路：Inter-Nodes Links> Logical Links (ABC-F)> Loop-Hybrid → Multi access hybrid link=YES
       （OXE R100 起默认已建；若无则改为创建）。
    5. 建 access 1：Inter-Nodes Links> Logical Links (ABC-F)> Hybrid or Direct Link Access> Create →
       Access number=1、Signalling type=B Channel → Save。
    6. 建 access 2：同路径 Create → Access number=2、Signalling type=B Channel → Save
       （链路默认存在但 access 必须自建）。
    7. 控制验证：OXE 控制台/SSH mtcl 会话执行 hybvisu -f all；两 access 须 UP；拥塞时 rsthyb 重启链路。
  verification: |
    hybvisu -f all 显示两条 access 均 UP；内部拨 31600 可通。
  conditions: 同 Node 不同 Network 是硬约束； France 目标库 ABC Local Call Allowed 默认开。
  tags: [lab, abc-f, hybrid-link, internal-calls]

- id: c07
  title: 用 CCS 调优 CCD 对象（wrap-up/pause/服务水平 + PG 八选项逐项测试 + 队列参数）
  type: lab
  source_pages: p166-193
  source_chapter: Setting up the CCD objects with the CCS (How-To)
  source_quote: |
    "Set up Pilot1 (31600): • Change the wrap up time (10 s) • Modify the pause time (5 sec). • Change
    the level of service. 85% of calls must be answered in less than 15 sec." (p167)
    "Last agent withdrawal authorized … Disable the option. If disabled, the last available agent
    loses this right to preserve the service." (p173)
    "Maximum waiting time Enter the maximum waiting time in seconds (i.e. 45) … Address Enter a
    destination extension number (i.e. 31010) Delay Enter a time-out in seconds (i.e. 60)" (p192-193)
  steps: |
    1. Pilot 参数：CCS System> Pilot → 选 Pilot1 → Pause between two calls=5、Wrap Up duration=10 →
       OK；服务水平目标=85% / 15 秒（影响 smiley，SOP 默认 15 分钟）。
    2. 实测 wrap-up/pause：MicroSIP-Public 拨 0210X41600 → Agent1 应答 → 挂机 → Real time>
       Processing Group> PG Agents/IVR/Team（中图标+文本数据显示）核对 10 秒 wrap-up 与 5 秒 pause。
    3. PG 选项逐项（Configurations> Processing Group> PG Agents> Agent_PG）：
       a. Last agent withdrawal authorized——先开测"末座席可退出"，再关测"被拒"，测完恢复开启。
       b. Withdrawal after logon——开启后登出再登入，状态应为 unavailable（退出态）；测完关闭。
       c. Call release by agent forbidden——开启后座席挂机呼叫保持（等主叫挂），主叫挂后 wrap-up→
          pause；测完关闭。
       d. Eternal Wrap-Up——先把 pilot wrap-up 提到 30 秒；不开时座席 wrap-up 中外呼 31010 即取消
          wrap-up；开启后操作结束回到 wrap-up 直至时长耗尽；测完关闭并恢复 10 秒。
       e. Wrap Up duration in Idle/Pause——设 idle=12s、pause=8s：空闲按 Wrap-Up 键 12 秒回闲；
          通话挂机进 pause 后按 Wrap-Up 键 8 秒回闲；测完恢复默认 600 秒。
       f. Ring rotation time-out——用默认 15 秒：两座席登入，来话不接，15 秒后转到另一座席
          （Real Time 界面看振铃座席变绿轮转）。
       g. Type of search——Cyclic：连续两通由两座席轮流接；Sequential：Agent1（序号 1）一直接，
          其退出后 Agent2 接；MIT：让 Agent2 先登、Agent1 后登，Agent2 空闲更久先振铃；
          测完恢复 Cyclic。
    4. 队列参数：System> Queue and Waiting Room → Normal_WQ → Maximum waiting time=45（超过则按
       规则走下一方向）；Queuing overflow：Address=31010、Delay=60（排队超 60 秒改址 31010）。
  verification: |
    每项均有行为验证点（退出允许/拒绝、登入即退出、挂机保持、wrap-up 保持/取消、12s/8s 计时、
    15 秒轮转、三种选座席方式、45 秒饱和与 60 秒溢出配置落位）。溢出行为留待后续实验复核（p193 Notes）。
  conditions: c04 两座席已登入；每个选项测试后须恢复默认，否则影响后续实验。
  tags: [lab, ccs, wrap-up, pg-options, queue]

- id: c08
  title: 话机录制动态语音指南并排入 CCD 矩阵（After-Sales pilot 683/684/685）
  type: lab
  source_pages: p194-236
  source_chapter: Voice Guides（讲义）+ Voice guides management by the set (How-To)
  source_quote: |
    "Dial the prefix 401 to start recording process … Enter the voice message (i.e. 1683, 1684 or
    1685) … File name: welcome … Enter a memo: vg1683" (p219)
    "Selecting the file means that it is downloaded into the GD3 board and can thus be played by the
    system. The command vgstat (vgstat 4 0) allows you to check that the file was uploaded on the GD3." (p220)
    "# diff. Value from 1 to 32767.To repeat the broadcast (i.e. 2) Duration 0.1 to 3276 seconds." (p232)
  steps: |
    1. 建指南：OXE System> Voice Guides> Create——683（演示）、684（排队等待）、685（阻塞）；
       Function=Single-message Voice Guide、Voice Guide Start=YES、Backup Tone=56、
       Language1 消息=1683、Language2 消息=2683（684/685 同法：1684/2684、1685/2685）。
    2. 分配板卡：前置 mtcl 会话 config 4 确认 OMS 在服、vgstat 4 0 看静态指南；System> Dynamic
       Voice Guides> Assignment> Create——VG Sub-message No.=1683、ACT-Board=4-0 → Save
       （2683/1684/2684/1685/2685 同；实验只做英文语言 1）。
    3. 放行录音：Translator> Prefix plan> 401（Recordable Voice Guides）、580（Tone test）确认存在；
       Users>31000>Rights 查 COS=0、Set Characteristics 查键盘已启用；Classe of Service> Phone
       Features COS> 0 → PCX SERVICES 启用 Recordable Voice Guides=1（法语库默认关）。
    4. 话机录音：IPDSP 31000 拨 401 → Record → 输消息号 1683 → Start recording 录"Welcome to
       after-sales services" → Stop → 试听 → Apply → 文件名 welcome → memo vg1683 → Apply
       （落 /usr7/vg/dhs）→ 按提示选文件（装入 GD 板）；1684（"Please hold on, an agent will
       answer you"）、1685（"There is no agent to answer you right now"）同法；vgstat 4 0 复核。
    5. 试听：拨 580 + 0683/0684/0685。
    6. 排入矩阵（pilot 改名 After-Sales，语言 English）：Call Flow mgt> Call Routing → After-Sales →
       Additional 页签 Normal Table——Pres.Guide=683（1 次扩散；cut auth 灰显属正常）；Level[1]=指南 2
       （音乐保持，5.0 秒）；Level[2]=684（1 次）；Level[3]/[4]/[5] 删默认；Level[6]=指南 2。
    7. 阻塞态两种配法：
       a. 按规则（with rule）：Normal mode 页签对 Redirection_WQ 关 Main Direction（即勾 Blocked）；
          Call Routing>Configuration… 勾 Blockage；Additional 页签 Blocked Table 删 Pres.Guide；
          Configurations> Processing Group> PG Other → Voice_guide_PG 设指南 685（1 次）。
       b. 不按规则（without rule）：Normal mode 页签取消 Blocked；Configuration… 的 Blockage closure
          addresses——Rule 不勾、Voice guide #=685、# diff=2、Duration 空（0.1-3276 秒域）。
    8. 行为测试：①开态+座席闲：拨 0210X41600，只播 683 一次即转座席；②开态+座席 wrap-up：播 683 →
       5 秒音乐 → 684 → 第 6 级音乐；③规则阻塞：来话由 Voice_guide_PG 播 685 一次；④无规则阻塞：
       先播演示指南再播 685。
  verification: |
    vgstat 4 0 列出已装载指南；四场景听感与上述脚本一致（p233-236）。
  conditions: c05 已打通外呼；401/580/编号 683-685 为实验口径；不录音时播备份音 56。
  tags: [lab, voice-guides, recording, parking-levels, blocking]

- id: c09
  title: .wav 文件导入语音指南（转换 → SFTP 传输 → 选中 → Offer pilot 矩阵）
  type: lab
  source_pages: p237-264
  source_chapter: Voice guides management by downloading .wav files (How-To)
  source_quote: |
    "From OTCC_NAS instance, copy 688_Offer_services_EN and 690_New_MOH wav files … A-Law, 8000Hz,
    64 Kbps, mono" (p240-241)
    "Configurations> Voice Guide Management> Audio File Conversion … Voice Message Number Enter the
    voice message number of the converted file (i.e. 1688)" (p241-242)
    "SFTP Enable the SFTP connection (mandatory from OXE N3)" (p245)
  steps: |
    1. 建指南：System> Voice Guides> Create——688（Offer 演示，消息 1688/2688）、690（新音乐保持，
       消息 1690/2690），参数同 c08（Single-message、Start=YES、备份音 56）。
    2. 分配板卡：System> Dynamic Voice Guides> Assignment> Create——1688 → ACT-Board 4-0（1690 同）。
    3. 取文件：从 OTCC_NAS 拷 688_Offer_services_EN.wav 与 690_New_MOH.wav 到 Client10 的
       Music/CCD Training（属性 A-Law/8000Hz/64kbps/mono）。
    4. 转换：CCS Configurations> Voice Guide Management> Audio File Conversion——源文件、目标目录
       /CCD Training/Converted files/1688、消息号 1688、名称 welcome → Convert；690 → 目录 …/1690、
       消息号 2690 → Convert（产物 1688_welcome、1690_onhold）。
    5. 传输：Configurations> Voice Guide Management> Audio File Update——文件路径、mtcl/
       Superuser2580*、勾 SFTP（OXE N3 起强制）→ Update；1690 同。
    6. 选中：Configurations> Voice Guide Management> Dynamic Voice Messages Configuration——输
       1688 → Select Message → 选中行点 Selected → OK（装入 GD 板）；1690 同；vgstat 4 0 复核。
    7. 试听：580 + 0688/0690。
    8. 矩阵（pilot2 改名 Offer，语言 English）：Pres.Guide=688（1 次）；Level[1]=690（5.0 秒）；
       Level[2]=684（1 次）；Level[3]-[5] 删；Level[6]=690。
    9. 阻塞态配法：a. 按规则——Normal mode 页签对 Overflow_WQ 关 Main Direction；Configuration…
       勾 Blockage；Blocked Table 设 Pres.Guide=684（1 次）；PG Other> Forwarding_PG 前转地址=31010。
       b. 不按规则——取消 Blocked、恢复 Overflow_WQ Main Direction；Blockage closure addresses——
       Rule 不勾、Voice guide #=685、# diff=2。
    10. 行为测试（0210X41601）：①开态+闲：688 一次后转座席；②开态+wrap-up：688 → 690 五秒 →
        684 → 690；③规则阻塞：684 一次后经 Forwarding_PG 前转 31010；④无规则阻塞：685 播两次后
        释放。
  verification: |
    转换/传输/选中三步均有成功提示；四场景听感与脚本一致（p261-264）。
  conditions: c08 已建 684/685；SFTP 选项在 OXE N3 及以后必须勾选。
  tags: [lab, wav, conversion, sftp, offer-pilot]

- id: c10
  title: 座席与班长特性配置（退出类型、监听与强插、通用转发四种激活、PG 关闭、多线、事务码）
  type: lab
  source_pages: p304-347
  source_chapter: Agent and supervisor features (How-To)
  source_quote: |
    "Unavailable type Enter the number of unavailable types you want to enable (i.e. 2) … Display
    Unavailable type 1 Enter the name of a type of unavailability you want to specify (i.e. Tea)" (p307)
    "Function Enter the ACD function (i.e. ACD Listening) … Mnemo … (i.e. Help Agent)" (p313)
    "Set up the transaction code parameters … (the unit is 100ms). The minimum value allowed is 10." (p343)
  steps: |
    1. 退出类型：OXE Applications> CCD> Processing Group> 31800> UNAVAILABLE TYPE PARAMETERS——
       Unavailable type=2、类型 1=Tea、类型 2=Lunch → 保存；IPDSP 按 Unavailable 键可见 Tea/Lunch
       两选项。
    2. wrap-up/pause 复测（同 c07 第 1-2 步：10s/5s）。
    3. 监听与强插：Users>31502>Progr.Keys>2 设 Function=ACD Listening、Mnemo=Help Agent；两台软话机
       分别登入 Agent1（31000）与 Supervisor（31501 话机登 31502）；MicroSIP-Public 打 0210X41600，
       Agent1 应答后按 Help 键——班长侧收到请求，可选 Listen（旁听，座席侧提示受 Show Supervisor
       Listening 参数控制，法国/德国默认 False）、Restrictive（restrictive intrusion，仅座席听到班长）、
       Intrusion（三方强插会议）；班长另可主动永久监控：Help Agent 键 → 输 31500 → 选 Permanent，
       此后座席状态变化（退出/忙）班长可见，来话时自动具备旁听/强插入口。
    4. 通用转发（四种激活）：a. 话机键——Users>31502>Progr.Keys>3 设 Function=General Forwarding of
       Pilot、DN=31600、Mnemo=Gen. Fwd 31600；Configurations> Pilot> After-Sales> Closure addresses>
       Standard General forwarding 地址=31010；按键+密码 0000 激活/取消（弹窗 General forwarding
       registered / Cancel gen. forward. Regist.；Navigator 显示 GF 态；来话转 31010）。
       b. CCS 界面——Call Flow mgt> Call Routing> After-Sales → Set to FWD / Bring into service。
       c. 日历——Calendar per Pilot 页签：周一 09:00 Rule0 Nor、17:00 Rule0 Fwd，复制到周二至周五；
       周六/周日 00:00 Fwd；勾 Active Time Slices；测试把 Fwd 时间改成"当前+5 分钟"观察自动切换；
       测完取消勾选。
       d. 按规则——Configurations> Pilot> After-Sales> Closure addresses 勾 Standard General
       forwarding（by rule）；Call Routing 的 FWD 页签勾 Redirection_WQ；Additional 页签 General
       Forward Table 删指南 70；Bring into service 后 Navigator：Normal_WQ 方向关、Redirection_WQ 开，
       来话经 Voice_guide_PG 听 685。
    5. PG 关闭：Users>31502>Progr.Keys>4 设 Function=Closing PG、DN=31800、Mnemo=Closing PG 31800
       （DN 留空则按键时手选组）；按键+密码 0000 → PG closure registered；Navigator：Normal_WQ 方向
       关、Overflow_WQ/Redirection_WQ 开（Offer 走 Forwarding_PG、After-Sales 走 Voice_guide_PG）。
    6. 多线座席：先登出班长（CC 页签 LogOff）才能改键；Progr.Keys>1 设 Function=Multi-line、DN=31502、
       Mnemo=ML_31502（再加一条 ACD line 键）；重新登入后 Perso 页签可见多线键与 ACD 线键；测试：
       Agent1 置 Lunch，31010 直呼 31502 为私人本地通话；再来 0210X41600 ACD 呼叫——ACD 优先接入、
       私人通话被保持，ACD 挂机经 wrap-up/pause 后保持通话回呼。
    7. 事务码：OXE Applications> CCD> Pilot> 31600> TRANSACTION CODE DIALING——Timer=100（=10 秒，
       单位 100ms）、位数=3、Business Code=Yes；测试：0210X41600 通话挂机后座席被要求摘码，输 123 →
       Apply → Code registered。
  verification: |
    各步均有座席话机显示或 CCS Real time 状态佐证（p306-345）；仅 Business 码进 Excel 统计（p345）。
  conditions: 密码 0000 为实验口径；Show Supervisor Listening 法国/德国默认 False（p315）。
  tags: [lab, supervisor, monitoring, general-forwarding, transaction-code]

- id: c11
  title: 预期等待时间（EWT）表配置与三阈值播报验证
  type: lab
  source_pages: p358-373
  source_chapter: Expected Waiting Time (How-To)
  source_quote: |
    "Voice guide 720:'Your estimated waiting time is less than 10 seconds' … 721:'… between 20
    seconds' … 722:'Your estimated waiting time is more than 1 minute'" (p359-360)
    "Expected Waiting Time Enter the first threshold in seconds (i.e. 10). … Guide number Enter the
    guide number (i.e. 720). … Cut Auth To be enabled. Voice guide automatically stopped as soon as
    an agent is available." (p365)
    "Pay attention, the tests depend on the TSP (Traffic Sampling Period) of the waiting queue. So,
    expect some lag while testing." (p373)
  steps: |
    1. 建指南：System> Voice Guides> Create——720（消息 1720/2720）、721（1721/2721）、722
       （1722/2722）；本章分配消息 2720/2721/2722 到 OMS 板（"Only language #2 must be set up"，
       实验口径）。
    2. 话机录音（401）：2720="Your waiting time is about 10 seconds"（文件名 twenty、memo vg2720）、
       2721="…about 20 seconds"、2722="…more than 1 minute"（文件名 minute、memo vg2722）；选文件
       装 GD 板；vgstat 4 0 复核。
    3. 建 EWT 表：CCS Configurations> EWT Tables → Table>Create（自动编号 Table[0]）→ 双击进入 6 个
       阈值：Threshold[1]——EWT=10、Guide=720、1 次扩散、时长 10.0、Cut Auth 勾；Threshold[2]——
       EWT=20、Guide=721；Threshold[3]——EWT=60、Guide=722。
    4. 挂表：Call Flow mgt> Call Routing> Offer> Additional 页签 Normal Table → Level[1] 双击 →
       EWT Table=0。
    5. 实时呈现：Real time> Navigator → 定制图标 → Real Time Info → Normal Queue 选 Expected
       Waiting Time → Record（Normal_WQ 对象旁显示 EWT，悬停看明细）。
    6. 行为测试：PG Agents 把 idle 态手动 wrap-up 拉到 300 秒；Agent1 置 wrap-up 占线；连打多通
       0210X41601 排队；解除 wrap-up 让 Agent1 逐通消化以拉长队列等待；Navigator 观察 EWT 值——
       <10s 播队列级指南（688），>10s/20s/60s 分别切到 EWT 表播 720/721/722。
  verification: |
    Navigator EWT 计数与所听指南对应（四段场景，p373）；注意测试受队列 TSP 影响有滞后。
  conditions: c09 已完成 Offer pilot；语言索引本章用 #2（与 c08 的 #1 并存，见 n16）。
  tags: [lab, ewt, thresholds, navigator]

- id: c12
  title: 排队位置语音指南 518（语言顺序、固定/变量段录音、分级编排、两 Calling 位次测试）
  type: lab
  source_pages: p385-400
  source_chapter: Waiting queue position voice guide (How-To)
  source_quote: |
    "Select System> Voice Guides> 518> VG Dynamic Feature> … Language Number Enter the language
    number for message broadcasting (i.e. 2 for English)" (p390)
    "Max position Enter a max position (i.e. 2 fo the test). … the variables messages are #3318
    (position 1) and #3319 (position 2)." (p390)
    "For the 3rd call, the caller hears inter-guide tone of the pilot After-Sales (31600) because the
    Max position in the dynamic guide '518' was handled at 2." (p400)
  steps: |
    1. 基线听感：查 After-Sales 现有分级（L1=2、L2=684、L3-L5 无、L6=2）；PG idle wrap-up 临时改
       60 秒；Agent1 wrap-up、Agent2 登出后拨 0210X41600，依次听 683 → 音乐 2 → 684 → 音乐 2；
       60 秒后座席回闲接听。
    2. 查 518：OXE System> Voice Guides> 翻页找 518（CCD waiting queue position 功能）——不改动参数。
    3. 设语言与顺序：System> Voice Guides> 518> VG Dynamic Feature> Language Number=2（本章口径
       2=English）→ 消息顺序选 Fix1 + Variable + Fix2 → Max position=2 → Apply。
    4. 变量段：System> Dynamic Voice Guides> Assignment> Create——3318 → 4-0（3319 同）；话机 401 录
       3318="one"（文件 one、memo vg3318）、3319="two"（two/vg3319）；选中装板；vgstat 4 0。
    5. 固定段：分配 3228（Fix1）、3229（Fix2）到 4-0；录 3228="You are in position"（youare/vg3228）、
       3229="On the waiting queue"（waiting/vg3229）；选中装板；vgstat 4 0。
    6. 分级编排：Call Flow mgt> Call Routing> After-Sales> Additional——L1=2（5 秒）、L2=518
       （1 次）、L3=2（5 秒）、L4=684（1 次）、L5 无、L6=2 → 保存 pilot 规则（书中强调 Don't forget
       to save）。
    7. 测试：①位置 1——Agent1 wrap-up，拨 0210X41600，排华中听到"You are in position 1 in the
       queue"；②位置 2——再从本地 MicroSIP 拨 00210X41600，听"position 2"；③第 3 通——因 Max
       position=2，只播 pilot 的 inter-guide 音。
  verification: |
    三个位次场景听感符合（p400）；文件选中以 /usr7/vg/dhs 的 ^ 标记与 vgstat 输出佐证。
  conditions: c08 已完成 After-Sales；518/3226-4217 为系统预置号不可自造。
  tags: [lab, position-guide, 518, recording]

- id: c13
  title: 实时信息与告警（Navigator 页签、实时对象、中继 CSTA 监控、S.L.、事件窗）
  type: lab
  source_pages: p430-448
  source_chapter: Real time information and alerts (How-To)
  source_quote: |
    "Display on tab #5 of the Navigator application, pilot 31600 with all connected objects. … Rename
    the Name tab field by the pilot number. (i.e. 31600)" (p431-432)
    "Select Trunk Groups> 1-T2-SIP PUBLIC> Trunk Group> … CSTA Monitored Enable the option (i.e. YES)." (p438)
    "Busy rate alarm threshold Default value is set to 80 % … Enter a new value (i.e. 1)." (p439)
  steps: |
    1. 页签管理：Real time> Navigator → Tab5 → 右键定制 → 选 After-Sales(31600) 及全部关联对象、
       页签名改 31600 → Record；Tab6 同法配 Offer（31601）。
    2. 实时对象：定制图标 → Real Time Info——Pilots=Calls in progress、Normal Queue=# Calls queued、
       PG Agent=# of agents in ACD call、PG Other=# of ACD call → Record；F1 查帮助。
    3. 行为核验：Agent1 wrap-up 后连打 0210X41600（公）与 00210X41600（本地），看对象计数变化。
    4. 座席状态分布：Real Time Info 勾 Breakdown of agent's states in PG；Advanced Options 为各话机
       状态配色 → Record；依次观察 logon/wrap-up/振铃/通话四态。
    5. 中继组实时：OXE Trunk Groups> 1-T2-SIP PUBLIC> Trunk Group> 勾 CSTA-Monitored=YES → SAVE；
       CCS Real time> Trunk group → 选 SIP PUBLIC → 配置图标 → Busy rate alarm threshold 临时改 1 →
       打一通 ACD 呼叫 → Busy/Total % 字段变色并出告警（点 Alert 图标看明细）→ 阈值改回默认 80。
    6. Pilot S.L.：Configurations> Pilot> After-Sales 查服务质量与效率参数；连打数通后看
       Real time> Pilots S.L. 与 Real time> Pilots（MSP 15 分钟统计）。
    7. 队列/PG/座席实时：Real time> Queue and Waiting Room、Processing Group> PG Agents/IVR/Team
       （图标切换、文本数据；饼图默认 30 秒刷新）。
    8. 事件窗：Real time> Incidents（配置与连接问题消息）；Real time> Alarms（Alarms 例=pilot 被关、
       Alerts 例=阈值检出、Indications 例=配置规则更新）。
    9. 阈值入口总览：Configurations> Trunk group / Pilot / Queue and Waiting Room / PG Agent 四页。
  verification: |
    页签、计数器、状态分布、中继告警、S.L. 演化均与操作对应（p431-448）。
  conditions: c05 中继组可用；CSTA-Monitored 不开则中继组实时无值（p414）。
  tags: [lab, navigator, real-time, alarms, csta]

- id: c14
  title: CCD 直接呼叫（direct call pilot 31603、私人号码、五场景呼叫性质验证）
  type: lab
  source_pages: p460-476
  source_chapter: CCD direct calls (How-To)
  source_quote: |
    "Select Applications> CCD> Processing Group> 31800> … Pilot Direct Call Enter the processing
    number for pilot direct call (i.e. 31603)." (p467)
    "Select Applications> CCD> CCD Users> 31500-Agent> … Private agent No. Enter a directory number
    ( i.e. 31000)" (p468)
    "Warning … THE LOCAL HYBRID LINK CANNOT BE USED FOR THE DIRECT CALL FACILITY." (p469)
  steps: |
    1. 建 pilot：OXE Applications> CCD> Pilot> Create——31603 / Direct call → Save（Navigator 可见；
       也可复用既有 pilot；该 pilot 专用于统计，不强制建规则）。
    2. 规则与方向（CCS）：Call Flow mgt> Call Routing> Direct call → 建 Rule_0 → Apply；
       Configurations> Pilot> 31603 → Call Routing 区加 Normal_WQ → OK。
    3. Pilot 计时：Configurations> Pilot> 31603 → Pause between two calls=5、Wrap Up duration=10、
       Language=English → OK。
    4. 激活路由：Call Flow mgt> Call Routing> Direct call> Normal mode 页签 → 勾 Normal_WQ 的
       Normal → Save 确认。
    5. PG 侧：OXE Applications> CCD> Processing Group> 31800> Pilot Direct Call=31603 → SAVE；
       同页 Outgoing ACD Call 启用 → SAVE（座席去话算 CCD、吃 wrap-up/pause 并进统计）。
    6. 私人号：OXE Applications> CCD> CCD Users> 31500-Agent> Private agent No.=31000 → SAVE。
    7. 五场景（Warning：本地 ABC-F 链路不能用于 direct call）：
       a. 打私人号 0210X41000——私人呼叫，无 wrap-up/pause；
       b. 打座席号 0210X41500——CCD 呼叫，话机显示 31603（Direct call），挂机走 31603 的
          wrap-up/pause（私人号查法：Info 页）；
       c. 座席登下去话 0+0210X12345（登入态）——CCD 呼叫+计时；
       d. 座席退出去话——私人呼叫，无计时；不可用态打 0210X41500——pilot 31603 blocked（默认播
          指南 #75 后释放），改为播 685：Configurations> Pilot> 31603> Blockage=685、# diff=1 →
          再测听"There is no agent to answer you right now"。
       e. 部分退出：OXE PG 31800> Partial Unavailable 启用 → 座席切部分退出去话与来话——均按 CCD
          呼叫处理，挂机 wrap-up→pause→回部分退出态。
  verification: |
    各场景呼叫性质（话机显示 Direct call/pilot 名）、计时有无与 p469-476 描述一致。
  conditions: c04/c06 已完成；私人号自动前转随登入登出启停（p454）。
  tags: [lab, direct-calls, private-number, partial-unavailable]

- id: c15
  title: Excel 统计（对象数放宽、Pilot/弃呼/事务码报表、预编译日报与重启动）
  type: lab
  source_pages: p517-526
  source_chapter: Excel statistic (How-To)
  source_quote: |
    "From the main menu, select Window> Customise … Select Statistics … Statistics Pilots Enter the
    number of statistics pilots (i.e. 5). … The max value is 50. You must restart CCS application to
    apply modifications previously made." (p518)
    "From the main menu, select Statistics> Excel> Pilot … Activation mode: Select the Activation
    mode Excel Display." (p519)
    "From the main menu, select Statistics> Excel> Automatic edition restart … Files are stored in
    the default folder. C:\ProgramData\Alcatel\CCSupervisor\Excel\DAILY or WEEKLY or MONTHLY." (p526)
  steps: |
    1. 放宽对象数：Window> Customise → Statistics——Statistics Pilots=5、Pilots=5、Filters=1、
       PG Agents/IVR=5、Agents=5 → 重启 CCS（默认 1，最大 50）。
    2. Pilot 报表：Statistics> Excel> Pilot → 选 After-Sales、Offer → 模板加 General、
       Detailed_graph、Detailed_report、Summary_graph、Summary_report → Excel Display → Daily、
       粒度 ¼h → Validate；General 页第二对象从 132 行起（¼h 一天 96 行）；改 Over several days
       of the month 再生成一次对比行号。
    3. 弃呼报表：Statistics> Excel> Abandoned Calls → 选两 pilot → 模板 General → Excel Display →
       Validate；结果页可经 CCA 对弃呼号码 click-to-call 回拨（CCA 10.7.8.0 起超链接自动回呼）。
    4. 事务码报表：Statistics> Excel> Transaction Code → 选 After-Sales → General → Excel Display →
       Validate（应看到 c10 录入的码记录）。
    5. 预编译日报：Configurations> Precompiled statistics> Daily edition → 选 After-Sales → 模板
       General → Save → 粒度改 1 小时（输出时刻、Run macro(ACDMacro)、Lists of Pilots(≤50)、
       Keep Excel links 为可选项）。
    6. 手动重启自动报表：Statistics> Excel> Automatic edition restart；产物在
       C:\ProgramData\Alcatel\CCSupervisor\Excel\DAILY（或 WEEKLY/MONTHLY）。
  verification: |
    各报表打开可见数据（132 行偏移、弃呼清单含超链接、码记录两条）；预编译文件落默认目录。
  conditions: 启动 CCsupervisor 后 Precompiled statistics 窗口延迟打开属正常（p524 Notes）。
  tags: [lab, excel, statistics, templates, precompiled]

- id: c16
  title: 紧急关闭（Emergency0 列表、指南 640、激活/停用/历史）
  type: lab
  source_pages: p531-542
  source_chapter: Emergency closure (How-To)
  source_quote: |
    "From the main menu, select Call Flow mgt> Emergency closure. … Name of the new list Select the
    default name (i.e. Emergency0) … The name of the list supports a maximum of 16 characters." (p532)
    "Voice guide number Enter a voice guide number (i.e. 640). … Message language 1 Enter the voice
    message number (i.e. 1640)." (p533-534)
    "You MUST be a CCS ADMINISTRATOR to be able to select the pilot in the emergency closure pilot
    list." (p542)
  steps: |
    1. 建列表：CCS Call Flow mgt> Emergency closure → Create → 名称 Emergency0 → 把 31600、31601、
       31603 全部选入（箭头）→ OK。
    2. 建指南：OXE System> Voice Guides> Create——640（消息 1640/2640，Single-message，备份音 56）；
       分配 2640 → ACT-Board 4-0。
    3. 话机录音（401）：2640="The pilot is closed. Please, call us later."（文件 closure、memo
       vg2640）→ 选中装板；vgstat 4 0 复核。
    4. 挂指南：CCS Configurations> Pilot → After-Sales → Closure addresses → Emergency closure：
       Voice guide #=640、# diff=1；Offer 同。
    5. 激活：Call Flow mgt> Emergency closure → 选 Emergency0 → Activate（Navigator 查看状态）。
    6. 测试：0210X41600 与 0210X41601 均应听到关闭消息。
    7. 停用→再激活→History…→Update 查操作历史；测完 Deactivate 复位（书中提醒勿忘）。
  verification: |
    激活后两 pilot 来话播 640；History 窗口列出激活/停用记录（p541-542）。
  conditions: 选 pilot 进列表须 CCS ADMINISTRATOR 权限；统计上计入"通用转发态来话"（p529）。
  tags: [lab, emergency-closure, voice-guide, history]

- id: c17
  title: 统计型 pilot（Stat.Pil Gold 31650、Call Tag GOLD、问候指南 701、Excel 报表）
  type: lab
  source_pages: p553-565
  source_chapter: Statistics Pilots (How-To)
  source_quote: |
    "Pilot Stat. Directory Number Enter the directory number (i.e. 31650) … Routing pilot Enter the
    pilot to be associated with (i.e. 31600)" (p555)
    "Call Tag Enter a call tag name (i.e. GOLD) Up to 32 characters to display during the ringing
    phase on the agent display." (p557)
    "Display on agent screen Select the Display on agent screen option (i.e. Call tag or pilot
    characteristics)" (p558)
  steps: |
    1. 建统计 pilot：OXE Applications> CCD> Statistic Pilot> Create——31650 / Stat.Pil Gold →
       下滚 Routing pilot=31600。
    2. CCS 侧可见性：Real time> Navigator → 开统计 pilot 显示，把鼠标悬停 pilot 打开
       Stat.Pil Gold 查看设置。
    3. Call Tag：CCS Configurations> Statistics Pilot → Call Tag=GOLD（≤32 字符，振铃期显示）；
       OXE 侧同页核对。
    4. PG 显示：OXE Applications> CCD> Processing Group> 31800> Display on agent screen 选
       Call tag or pilot characteristics；Call Tag Display Timer（0=仅振铃期，>0=振铃+接通后秒数）。
    5. 问候指南：System> Voice Guides> Create——701（消息 1701/2701）；分配 2701 → 4-0；话机 401 录
       2701="Welcome to our gold members"（gold/vg2701）→ 选中装板。
    6. 挂指南：CCS Configurations> Statistics Pilot → Presentation guides> Normal：Guide n°=2701、
       # diff=1（注意此处填消息号口径，原书如此）。
    7. 测试：0210X41650 → 先听 Gold 问候 → Agent1 应答，话机显示 GOLD。
    8. Excel：Statistics> Excel> Statistics Pilot → 选 Stat.Pil Gold → General → Excel Display →
       粒度 1 小时 → Validate。
  verification: |
    问候播报与 GOLD 显示（p563）；统计 pilot 的 General 报表产出（p565）。
  conditions: c04/c05 已完成；统计 pilot 只能溢出到一个本地路由 pilot（p546）。
  tags: [lab, statistics-pilot, call-tag, excel]

- id: c18
  title: 座席欢迎指南（538 机制、4500 消息、早晚双版本录制与切换激活）
  type: lab
  source_pages: p572-582
  source_chapter: Agent welcome guide (How-To)
  source_quote: |
    "The voice guide #538 puts into service the agent welcome guide feature on the OmniPCX
    Enterprise. It's not necessary neither to create nor to modify (in database France)." (p574)
    "Pres. Message Number Enter the voice guide number dedicated for agent presentation (i.e. 4500).
    Nb of Presentation Mess. File Enter the number of message(s) the agent wants te record (i.e. 2).
    Agent can record a maximum of 5 prompts." (p575)
    "Silent Connection on Agent: Value to 0 (default): the caller and the agent will hear the guide.
    Value to 1: only the caller will hear the guide." (p576)
  steps: |
    1. 查机制指南：System> Voice Guides> Page 2 → 538（法国库预置，不建不改）。
    2. 分配消息：System> Dynamic Voice Guides> Assignment> Create——4500 → ACT-Board 4-0。
    3. 座席指派：CCS Configurations> Agent> Agent1——Pres. Message Number=4500、Nb of Presentation
       Mess. File=2（最多 5 条）；OXE CCD Users> CCD Operations data management> 31500 核对。
    4. COS 检查：Classe of Service> Phone Features COS> 0 → RIGHTS 区 Silent Connection on Agent：
       0=主叫和座席都听，1=仅主叫听（实验保持 0）。
    5. 录音（IPDSP 31000 已登入 31500，CC 页签下翻 → Welcome guide → Record → Apply → Start）：
       晨版"Good morning, I'm Mister Dupont"（文件 morning、memo 4500 morning）；再 New file 录
       晚版"Good evening, I'm Mister Dupont"（evening/4500 evening）；OXE 上 cd /usr7/vg/dhs && ll
       确认两文件。
    6. 选择版本：Welcome guide → Download → 选 morning → 确认（OXE 上 ^ 标记选中之文件）。
    7. 激活三法：话机 Welcome guide → Apply；CCS Configurations> Agent> Agent1 → 勾 Presentation
       Message Activation；OXE CCD Operations data management> 31500 → Presentation mess. activation
       启用。
    8. 测试：0210X41600 来话，座席摘机时先播欢迎指南（主叫与座席都听），随后转接。
  verification: |
    ll 输出 ^ 指示选中；来话场景座席先闻欢迎语（p582）；欢迎指南不在 CCD direct calls 上播放（p567）。
  conditions: 欢迎指南存 RAM（GPA2/GD3/GA3）；登出座席可用 ACD 前缀+92+座席号+密码录音（p568）。
  tags: [lab, welcome-guide, 538, agent]

- id: c19
  title: 多语言语音指南（After-Sales EN/FR 双 pilot、Multi-language 指南 702/703、双语实测）
  type: lab
  source_pages: p588-606
  source_chapter: Multi language voice guide (How-To)
  source_quote: |
    "Create the pilot 31602 with the following items. Pilot name: After-Sales FR Language number:
    French" (p591)
    "Function Select the guide function (i.e. Multi-language message). … Language Number Select the
    language number (i.e. French) Message number Enter the message number for the french voice
    guide(i.e. 1702)." (p596-597)
    "The caller should ear first: 'Bienvenu au service après-vente'. The caller should ear after:
    'Ne quittez pas, un agent va vous répondre'." (p606)
  steps: |
    1. 改名：CCS Configurations> Pilot> 31600 → Pilot Name=After-Sales EN。
    2. 建 FR pilot：OXE Applications> CCD> Pilot> Create——31602 / After-Sales FR；下滚 Language
       Number=French → SAVE。
    3. FR pilot 规则（CCS）：Call Flow mgt> Call Routing> After-Sales FR → 建 Rule_0 → Apply；
       Configurations> Pilot> 31602 → 加 Normal_WQ、Redirection_WQ → OK；Normal mode 页签勾两队列
       Normal、Normal_WQ 优先级 0 → Save；Navigator 核对连接点。
    4. 建多语言指南：OXE System> Voice Guides> Create——702：Function=Multi-language message、
       Start=YES、备份音 56 → Add an element（Language=French、Message=1702）→ 再 Add（English、
       2702）→ SAVE；703（1703 FR / 2703 EN）同法。
    5. 分配板卡：System> Dynamic Voice Guides> Assignment——1702、2702、1703、2703 → 各建一条
       4-0。
    6. 话机录音（401）：1702="Bienvenu au service après-vente"（bienvenu/vg1702）、2702="Welcome
       again to after-sales services"（welcome/vg2702）、1703="Ne quittez pas, un agent va vous
       répondre"（repond/vg1703）、2703="Please hold on, an agent will answer you"（holdon/vg2703）；
       逐一选中装板；vgstat 4 0。
    7. 分级（两 pilot 相同）：Pres.Guide=702（1 次）；L1=2（5.0 秒）；L2=703（1 次）；L3-L5 删；
       L6=2（5 秒）。
    8. 测试：①0210X41600（EN pilot）：先"Welcome again…"后"Please hold on…"；②0210X41602
       （FR pilot）：先"Bienvenu…"后"Ne quittez pas…"；过程中解除 wrap-up 让 Agent1 接听。
  verification: |
    同一指南号 702/703 在两个 pilot 上按各自语言播报（p605-606）。
  conditions: c08 已建基础矩阵；指南 Function 必须选 Multi-language message 才能挂多语言消息。
  tags: [lab, multilanguage, pilots, voice-guides]

- id: c20
  title: 日历（Closed_rule 双规则、路由/分配日历、特殊日、时间片激活与开闭日验证）
  type: lab
  source_pages: p617-642
  source_chapter: Calendar (How-To)
  source_quote: |
    "Rule Name Enter the rule name (i.e. Closed_rule)" (p620)
    "Select Applications > CCD> Distribution rule> 1.Closed_rule.false … Click on Active Rule … The
    Call distribution rule is activated" (p627)
    "Tick the option Activate Time Slices" (p639)
  steps: |
    1. 目标（p619）：开日（工作日时段）矩阵照旧；闭日（午休/夜间/周末/特殊日）播提示消息。
    2. 新 pilot 规则：Call Flow mgt> Call Routing> Offer> Create 规则 Closed_rule → OK/Yes。
    3. 规则方向：选 Closed_rule → Normal mode 页签 → 关 Normal_WQ 的 Main Direction、开
       Redirection_WQ 的 Normal → Save；Additional 页签 Normal Table> Pres.Guide=683（1 次）→ Save。
    4. 新分配规则：Call Flow mgt> Call Distribution → Create → Closed_rule → OK/Yes；Resource
       selection：Normal_WQ→勾 Agent_PG、Overflow_WQ→勾 Forwarding_PG、Redirection_WQ→勾
       Voice_guide_PG（各 Save）。
    5. 激活规则：pilot 规则——Call Routing 选 Closed_rule → Apply；分配规则——OXE Applications>
       CCD> Distribution rule> 1.Closed_rule.false → Active Rule。
    6. 查矩阵：Navigator 定制 Tab8 → 选 Offer + Normal_WQ/Redirection_WQ + Agent_PG/
       Voice_guide_PG → Record；此时 Redirection_WQ 路由激活、Normal_WQ 未激活；拨 Offer 听
       "There is no agent to answer you right now"。
    7. 路由日历：Call Routing> Offer> Calendar per Pilot——周一 08:00 Rule0 Nor、12:00 Rule1、
       13:30 Rule0、19:00 Rule1（Add Time Step 逐条）；复制到周二至周五；周六/周日 00:00 Rule1；
       Special Days… 建 1 月 1 日、5 月 1 日、7 月 14 日、12 月 25 日并各配 00:00 Rule1。
    8. 分配日历：Call Distribution> Overflow_WQ> Calendar 页签——同一时间片骨架，切换分配规则 ID
       （0/1）；周六日与特殊日 00:00 Rule1；复制跨日。
    9. 激活：Call Routing> Offer> Calendar per Pilot → 勾 Activate Time Slices（p639）。
    10. 验证：开日——Navigator 双队列可用、Rule_0 Active、当前时间片绿色且 ID 吻合；闭日——仅
        Redirection_WQ 可达、Closed_rule Active；注意活动时间片上的修改要到下一切换点才生效
        （p638，测试提前几分钟改）。
  verification: |
    Navigator Tab8 在开/闭两种时间下矩阵方向与激活规则 ID 均与日历一致（p640-642）。
  conditions: c09 已完成 Offer；特殊日最多 50 个、pilot 日历 10 切换/日、分配日历 20 切换/日。
  tags: [lab, calendar, rules, special-days]
```

---

## 收尾自检：How-To 实验章 ↔ case 条目映射（task 覆盖）

| How-To 章（PDF 页） | case id | 对应 BOOK_OVERVIEW task |
|---|---|---|
| Basic CCD matrix creation（p63-77） | c01 | task-03 |
| CCS software installation and set up（p89-97） | c02 | task-04 |
| Creation of the rules（p98-120） | c03 | task-05 |
| Creation of the ACD-authorized sets, agents and supervisor（p121-149） | c04 | task-06 |
| Finalizing the pod configuration（p150-158） | c05 | task-07 |
| Local hybrid ABC-F link（p159-165） | c06 | task-08 |
| Setting up the CCD objects with the CCS（p166-193） | c07 | task-09 |
| Voice guides management by the set（p211-236） | c08 | task-10 |
| Voice guides management by downloading .wav files（p237-264） | c09 | task-11 |
| Agent and supervisor features（p304-347） | c10 | task-13 |
| Expected Waiting Time（p358-373） | c11 | task-14 |
| Waiting queue position voice guide（p385-400） | c12 | task-15 |
| Real time information and alerts（p430-448） | c13 | task-16 |
| CCD direct calls（p460-476） | c14 | task-17 |
| Excel statistic（p517-526） | c15 | task-18 |
| Emergency closure（p531-542） | c16 | task-19 |
| Statistics Pilots（p553-565） | c17 | task-20 |
| Agent welcome guide（p572-582） | c18 | task-21 |
| Multi language voice guide（p588-606） | c19 | task-22 |
| Calendar（p617-642） | c20 | task-22 |

说明：
- 全书 20 个 How-To 章全部入册，一一对应，无遗漏无合并；task-01/02/12 为环境准备与讲义理解类任务，由 framework.md（f01-f03）与 BOOK_OVERVIEW 承载，不设独立 case。
- 所有实验值（IP、密码、分机、公网号码、板位 4-0）均为实验口径；验证（verification）均取自书中明确的验收截图说明或 Notes。
