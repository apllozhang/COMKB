# 案例/实验/操作序列候选 — OmniTouch Contact Center Standard · Advanced (OTCCXTE101EN Ed07)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号）标注"实验口径"。
> 条目说明: 全书 15 个 How-To 实验章 → 15 条，一章一条（章内多脚本/多功能作为同条步骤组）。

```yaml
- id: c01
  title: CCS 软件安装、声明 OXE 与 Navigator 连通验证
  type: lab
  source_pages: p39-47
  source_chapter: CCS software installation and set up — "Install and set up the CCS software"
  source_quote: |
    "On Feature level window, select Full for a full CCS version installation. … On Feature level license window,
    select Monosite." (p42)
    "The CCS application needs to write the updated values in the file ccs.ini file (call server IP address). So you
    must restart the CCS" (p45)
    "From the CCS main menu, select Real time > Navigator. You now view the OXE CCD array with the CCS application." (p47)
  steps: |
    1. Client10 PC（实验口径 192.168.1.10）：从 OTCC_NAS 网络盘把 CCS 软件拷到 Documents 目录，右键 Open。
    2. 解压：More info → Run anyway → 保持默认路径 → Extract。
    3. 进入解压目录，右键 CCS.msi → Open → Setup 向导 Next。
    4. End-User License Agreement 勾选接受 → Next；Destination Folder 保持默认 → Next（期间自动装 Microsoft Visual
       C++ 2017 Redistributable x86）。
    5. Feature level=Full → Next；Feature level license=Monosite → Next；Excel=Yes（高级统计报表）→ Next；Excel 报
       表位置=默认 → Next；语言第一页保持 English+French → Next；界面语言 English → Next。
    6. Setup type=Windows standalone → Next；User's Files Folder 默认 → Next；Station ID 核对计算机名 → Next；登出
       后实时信息=Yes → Next；ASM Script Editor=No（本章不装）→ Next；复查 → Install；ccs.ini 合并提示 OK → Finish。
    7. 声明 OXE：启动 CCsupervision → Window > Customise… → Network 菜单选 node1 → Modify → Direct access：勾
       Connected at start up、Direct connection，Master PABX name=192.168.1.3（实验口径）→ OK → 确认 Yes → 提示重启
       OK → 关闭 CCS。
    8. 重新启动 CCS：登录 administrator/alcatel（实验口径）→ 强制改密（Old=alcatel，New/Confirm=Superuser01*，实验
       口径，须满足安全规则）→ Yes/OK → 用新密码再登录。
    9. 验证：主菜单 Real time > Navigator 打开 CCD 矩阵全景。
  verification: |
    书中验收点：Real time > Navigator 显示 "You now view the OXE CCD array with the CCS application"（p47）。
    隐含验收：改密后能用新密码登录。
  conditions: POD 已启动（OXE/Client10 虚机在运行）；NAS 网络盘可用。
  tags: [lab, ccs, installation, navigator]

- id: c02
  title: POD 定稿——软话机上线、坐席登录、外部 SIP 网关注册、DID 翻译与呼入测试
  type: lab
  source_pages: p48-62
  source_chapter: Finalizing the pod configuration — "Configure the Pod for OTCC labs"
  source_quote: |
    "Registration ID pbxN (where N is your POD number) … Outgoing username pbxN" (p56)
    "First external number 33210N41000 … First internal number 31000 … Range Size 1000" (p57)
    "Call Pilot1 from Public user by dialing 0210X41600. … When Agent1 hangs up, automatic wrap-up status is applied
    to the agent." (p58)
  steps: |
    1. 核对虚机已启动（OXE 双节点、OMS、FlexLM、Client10/11、Windows Server）。
    2. 机架核对：OXE WBM（https://192.168.1.3，mtcl/Superuser2580*，实验口径）——主站 Software Rack 3U Rack4，GD4
       192.168.1.13；远端 Rack3，GD4 192.168.1.113；在役状态确认。
    3. 用户核对：WBM Users 下 31010/31011（Local SIP SIP extension，Main 站，装于 Client10）；注意两 SIP 用户密码均
       为 123456（实验口径）。
    4. Client10 上启动 MicroSIP-31010/31011，确认 Online（不在线则查改密码）；启动 MicroSIP-Public，选 Public POD X
       profile（X=POD 号），确认 Online。
    5. 坐席登录：Client10 启动 IPDSP → 按任意键注册 → 输分机 31000 + 个人码 0000（实验口径）→ Menu 页下滑点 LogOn →
       31500 为自助型，点 List 选 Agent_PG；Client11 同法注册 31001，31501 非自助型，直接输坐席号 31501 登录偏好组
       Agent_PG。
    6. 外部 SIP 网关：WBM SIP > SIP Ext. Gateway → 选外部网关 → Registration ID=pbxN、Outgoing username=pbxN（N=
       POD 号）→ 保存。
    7. DID 翻译：WBM Translator > External Numbering Plan > Default DID num. translator → Create → First external
       number=33210N41000、First internal number=31000、Range Size=1000。
    8. 外呼入测试：MicroSIP-Public 拨 0210X41600（Pilot1）、0210X41601（Pilot2），坐席应答，挂机后自动 wrap-up。
    9. 内呼入测试：MicroSIP-31010 拨 31600、31601，验证本地混合 ABC-F 链路，行为同上。
    10. 嵌套 RDP：从 Client10 的 Guacamole 会话开远程桌面连 192.168.1.11 → Local Resources 页远程音频设"在本机播
        放/录音" → 勾"不再询问" → Yes；把 PC11 会话窗口缩放对齐到其 IPDSP。
  verification: |
    书中验收点：外/内呼 Pilot1、Pilot2 均能接通到 Agent1，"When Agent1 hangs up, automatic wrap-up status is applied
    to the agent"（p58-59）；两 MicroSIP 与 Public profile 均 Online（p52-53）。
  conditions: c01 已完成；NAS 与 SIP 模拟器可用；POD 号代入所有 N/X。
  tags: [lab, pod-setup, sip-gateway, did, agent-logon]

- id: c03
  title: ACR 基础对象部署——附加 PG、等待室、ACR Pilot、统计 Pilot、路由/分配规则与坐席附加
  type: lab
  source_pages: p130-159
  source_chapter: ACR Management — "Manage ACR"
  source_quote: |
    "Create the pilot ACR Pilot (31603)." (p135)
    "The ACR Pilot is blocked. If the Agent does not have any skill, the Waiting Room is blocked !" (p148)
    "As no script is attached to the ACR Pilot, the Waiting Room is not used; the System will try to use another
    Waiting Queue, if possible." (p159)
  steps: |
    1. 建附加处理组：WBM（https://192.168.1.3，mtcl）Applications > Processing Group > Create → DN=31803、Name=
       Agent2_PG、Type=Agent（实验口径）。
    2. 建等待室：Applications > CCD > Queue > Create → DN=31704、Name=WaitingRoom、Type=Waiting room。
    3. 建 ACR Pilot：Applications > CCD > Pilot > Create → Pilot DN=31603、Name=ACR Pilot。
    4. 建统计 Pilot：Applications > CCD > Statistic pilot > Create → 31660 Car Insurance、Routing pilot=31603；同法
       31661 Home Insurance、Routing pilot=31603。
    5. 建 Pilot 规则：CCS → Call Flow mgt > Call Routing → 选 ACR Pilot → Pilot rule 区 Create → 规则名 Rule_0（可
       用默认）→ OK → Yes → Apply → Yes，规则生效。
    6. 接路由方向：CCS Configurations > Pilot → 选 31603 → Call Routing 区选 WaitingRoom 加入可能队列 → OK。
    7. 激活路由：Call Flow mgt > Call Routing → 选 ACR Pilot → Normal mode 页 → WaitingRoom 启用 Normal → Save → 确
       认。
    8. 配分配：Configurations > Queue and Waiting Room → 选 31704 → 依次加 Agent_PG、Agent2_PG → OK；Call Flow mgt >
       Call Distribution → 选 31704 → Resource selection 页勾通两个方向 → Save。
    9. 坐席附加 PG：Configurations > Agent → Agent1 → Add → 选 Agent2_PG → OK（31500 变双组）；Agent2 同法；Agent2
       的 Preferred GT Agents=Agent2_PG。
    10. 重新登录：两坐席先从 Agent_PG 登出，再登录到 Agent2_PG（31500 走 List 自选，31501 直接输号）。
    11. 矩阵总览：Real time > Navigator——Tab1 看全景；点定制图标建 Tab8（隐藏 Pilot1/2、三个普通队列、Forwarding_PG
        与 Voice_guide_PG）后切 Tab8 看 ACR 专用视图。
    12. 技能三连（后续小节）：Configurations > Advanced Call Routing > Skill 建域 Insurance（权重 1，ID 自动）与技能
        Car/Home；ACR Data 页建 Car_Profile（English L5 强制 + Insurance Car L8 强制）与 Home_Profile（English L5 +
        Home L8）；Configurations > Statistics Pilot 把 Car_Profile 配 31660、Home_Profile 配 31661；Configurations >
        Agent 给 31500 加 English L9 + Car L9、给 31501 加 English L9 + Home L9（默认激活）。
    13. 验证呼叫：Navigator 确认等待室 Open 且绿色；打统计 Pilot 观察。
  verification: |
    三阶段验收：①技能赋予前 ACR Pilot 阻塞（"If the Agent does not have any skill, the Waiting Room is blocked!"，
    p148）；②坐席带激活技能登录后等待室 Open 且绿色（p159）；③未挂脚本时呼叫不进等待室，落其他队列或 Pilot 闭锁数据
    （p159 Notes）。
  conditions: c01/c02 已完成；全部 DN 为实验口径。
  tags: [lab, acr, waiting-room, pilot, skills]

- id: c04
  title: ISM 坐席清单手算——四域五坐席的强制/可选成本全算例
  type: lab
  source_pages: p182-186
  source_chapter: ISM agent list — "Find the agents list created by ASM"
  source_quote: |
    "Mandatory attributes are: ­ Car Insurance (L4), ­ French (L3), ­ Paris (L1) … Only Agent 1, Agent 4 and Agent 5
    have all mandatory attributes." (p185)
    "Mandatory cost calculation for agent 1 … Cman = (French (9 -3)*1) + (Car in. (4-4)*4) + (Paris (5-1)*2) … = 14"
    (p185)
    "So the list returned by ASM is the following list: Sub-List1: Agent 4, Agent 1 Sub-List2: Agent 5" (p186)
  steps: |
    1. 场景设定（纸面演算）：主叫打 Car Insurance（31660）统计 Pilot；4 个域——Language(权重 1：English/French/
       German)、Geographic market(权重 2：Paris/France/UK/German)、Privilege(权重 3：Client/VIP)、Product(权重 4：
       Car/Home/Life insurance/Financial consultant)。
    2. 呼叫档案 Car_Call_Profile：Product Car L4 强制、Language French L3 强制、Geographic market Paris L1 强制、
       Product Life insurance L1 可选、Privilege Client L1 可选。
    3. 五个坐席技能表逐项抄录（p183-184）。
    4. 强制属性筛选：Agent2 无 Product Car insurance 出局；Agent3 无 Language French 出局；Agent1/4/5 齐备；Agent5
       的 Car 等级低于要求只能进后续子列表。
    5. 算 Cman：Agent1=(法语 9-3)×1+(车险 4-4)×4+(巴黎 5-1)×2=6+0+8=14；Agent4=(5-3)×1+(5-4)×4+(5-1)×2=2+4+8=14。
    6. 同分算 Copt（可选属性）：可选=Life insurance L1、Client L1；Agent1=(寿险 2-1)×4+(客户 9)×3=4+27=31（无
       Client 技能按 9 代入）；Agent4=(1-1)×4+(2-1)×3=0+3=3。
    7. 结论排序：Sub-List1=Agent4、Agent1（Copt 3<31）；Sub-List2=Agent5。
  verification: |
    书中给出完整结果作为验收："Sub-List1: Agent 4, Agent 1 Sub-List2: Agent 5"（p186）；两坐席 Cman 同为 14 时按
    Notes 触发可选成本计算（p185）。
  conditions: 纸面演算章，无需环境；公式与等级/权重定义见 principle p01/p06。
  tags: [lab, ism, calculation, algorithm]

- id: c05
  title: ASM Script Editor 独立安装与首次启动（含 JRE）
  type: lab
  source_pages: p204-208
  source_chapter: ASM Script Editor software installation — "Install the ASM Script editor software application"
  source_quote: |
    "If the CCsupervision application is already installed, you can't reuse the executable CCsupervision setup file to
    add the ASM Script Editor package. You must use the dedicated executable setup file (asm-se_setup.msi)" (p206)
    "Select the zulu8.72.0.17-ca-jre8.0.382-win_i686.msi file." (p207)
    "From the main menu, select Configurations> System> Advanced Call Routing> ASM Script Editor … Click on Allow
    access for private network." (p208)
  steps: |
    1. Client10：NAS 上进入 CCS 软件目录的 ASM Script Editor 子目录，右键 asm-se_setup.msi → Install。
    2. 向导五步：Welcome Next → License 接受 Next → Destination Folder 默认 Next → Start Copying Next → Ready 点
       Install → Finish。
    3. （备选路径）装 CCS 时勾 ASM Script Editor 组件一步到位；已装 CCS 的机器禁止用 CCS 安装包补装，必须用专用
       asm-se_setup.msi。
    4. 装 JRE：NAS 的 JRE 目录，右键 zulu8.72.0.17-ca-jre8.0.382-win_i686.msi（Azul Zulu JRE 8.72.0.17 32 位）→
       Next → Custom Setup 保持默认 → Install → Finish（编辑器起不来时先装它；版本可高于书示）。
    5. 启动：CCS 主菜单 Configurations > System > Advanced Call Routing > ASM Script Editor。
    6. Windows Defender 防火墙弹窗 → Allow access（专用网络）。
  verification: |
    书中验收点："ASM Script Editor application is started."（p208）。
  conditions: c01 已装 CCS；NAS 可达。
  tags: [lab, asm-script-editor, installation, jre]

- id: c06
  title: ISM 脚本创建激活与 LIT 切换——从 ISM.scr 到 ISM_IDLE 与 parameters.cfg
  type: lab
  source_pages: p209-220
  source_chapter: ACR Script & ISM Rule — "Create an ACR script with the ISM Rule"
  source_quote: |
    "Enter the remote ASM IP address (i.e. 192.168.1.3) … check that connection to ASM is enabled." (p210)
    "There are no characteristics attached to the ACR Pilot, so no agent can be in the List. The script is used 21
    times and the call goes then to the ACR Pilot blocked address" (p214)
    "nano /usr3/afe/parameters.cfg … Modify the value from 0 to 1. … Enter the following command to restart the AFE
    process: dhs3_init -R MAIN_AFE … Now the agent will be used one after the other based on LIT." (p218-219)
  steps: |
    1. 连 ASM：CCS Configurations > Advanced Call Routing > ASM Script Editor → ASM > Connection… → 填 Call Server
       IP 192.168.1.3（实验口径）→ OK → 等连接成功。
    2. 建脚本：右键远程 ASM > Add new… → 名 ISM → 选位置 → Graphic mode。
    3. 编排：Rules 页点 ISM rule 图标 → 落在 Start/Stop 之间 → 属性选 CHARACTERISTICS_LIST → OK；连线（Start 红→
       ISM 黄，ISM 黄→Stop 红）；积木块入口/出口不得悬空；关图形编辑器保存。
    4. 激活：右键 ISM.scr > Activate… → 左侧选 Pilot 31603 → OK。
    5. 三路呼叫测试（MicroSIP-Public）：拨 0210X41660 → Agent 31500（English/Car）振铃；拨 0210X41661 → 31501
       （English/Home）振铃；直拨 0210X41603（ACR Pilot）→ 无坐席，脚本跑满 21 次后走闭锁地址/Blocked Voice Guide。
    6. LIT 预演：给 31501 加 Car L9 技能（Configurations > Agent > Agent2 > Skills Add，域 Insurance/Car，等级 9，激
       活）→ 再打 31660 仍 31500 先振（PLTR 默认）。
    7. 建 ISM_IDLE：Add new → 名 ISM_IDLE → Graphic mode → 拖 RULE_ISM（属性 CHARACTERISTICS_LIST）+ RULE_IDLE_TIME
       （无属性）→ 连线 → 保存；右键 Activate… 到 31603。
    8. 改参数：OXE console（mtcl）→ nano /usr3/afe/parameters.cfg → Ctrl+W 搜 asm_ag → 值 0 改 1 → Ctrl+X → Y →
       Enter → dhs3_init -R MAIN_AFE 重启 AFE。
    9. 坐席侧技能开关：Configurations > Agent → Agent2 勾"Can set his skills"；Client11 IPDSP 的 CC 页 > ACR manage
       > View → 关 Home 技能；CCS 里复核该技能已禁用；Skills Matrix 图标 > options 设 Displayed skills=Used skills、
       两种表头模式全开。
  verification: |
    书中验收点：0210X41660 → "Agent 31500 is ringing"（p214）；0210X41661 → "Agent 31501 is ringing"；直拨 31603 →
    脚本 21 次后播 Blocked Voice Guide；改参后"Now the agent will be used one after the other based on LIT"
    （p219）；关 Home 技能后打 31651（Call_Profile_2：English & Home），alb 发 21 次请求（脚本执行 20 次）空列表，
    呼叫回归路由管理（p220）。
  conditions: c03/c05 已完成；LIT 粒度受 5 分钟统计刷新限制（principle p04）。
  tags: [lab, ism, script, lit, parameters-cfg]

- id: c07
  title: 重选机制与调试器——Reselect 脚本、10 秒节拍与双子列表轨迹
  type: lab
  source_pages: p221-245
  source_chapter: Script Editor Debugger（讲义）+ ISM rule and reselection — "Use ISM rule & to generate several agent sub-lists"
  source_quote: |
    "THIS EXTENSION MUST BE A NORMAL USER, NEITHER AGENT NOR SUPERVISOR." (p225)
    "Select the parameter CHARACTERISTICS_LIST … On Variable field, select the RESELECTION_TIMEOUT … Enter an integer
    of 10 (seconds)" (p241)
    "The caller waits for 10 sec in the waiting room. After 10 sec, the ASM will re-execute the script to build the
    next sub-list … Sub-List 2 with Agent2 (31501) … The maximum number of script execution is 21 times." (p245)
  steps: |
    1. 技能改版（Skills Matrix）：Configurations > Agent > Skills Matrix 图标 → Agent2(31501) 的 Car 从 9 改 4；保持
       31500=English L9/Car L9。不要改 Car_Profile（English L5 强制 + Car L8 强制）。
    2. 案例一：保持 ISM_IDLE 激活，Public 拨 0210X41660 → 仅 31500 振铃（31501 Car 等级低于档案要求）。
    3. 案例二：让 31500 忙（接一通不放），另一软话机再拨（Local 用户拨 00210X41660）→ Navigator 定制 Real Time Info
       参数 #Calls queued 后观察等待室 Active，呼叫泊入等待室（仅生成第 1 子列表）。
    4. 案例三：31500 登出后再拨 → 31501 振铃（ASM 自动生成第 2 子列表；找不到人则脚本重选至 21 次）。
    5. 建 Reselect 脚本：ASM > Connection 连 192.168.1.3 → 右键远程 ASM > Add new → 名 Reselect → Graphic mode → 拖
       RULE_ISM（CHARACTERISTICS_LIST）→ Statement 页 Set a call context variable → Variable=RESELECTION_TIMEOUT、
       Value=10 → OK → 连线 → 保存 → Activate 到 31603。
    6. 起调试器：右键 Reselect.scr > Debugger → OK 确认 → 激活窗口选 31603 → OK → 调试器选 Calls without any filter
       → Commit。
    7. 第一通：Public 拨 0210X41660（31500 空闲）→ 轨迹显示 SEQUENCE=1、Sub-List 1=Agent1；接听后挂机，让 31500 进
       wrap-up。
    8. 第二通：再拨 → SEQUENCE=2，主叫在等待室等 10 秒 → ASM 重执行脚本 → Sub-List 2=Agent2。
  verification: |
    书中验收点：调试器第一序列=1 出 Sub-List 1（Agent 31500），第二序列=2 等待 10 秒后出 Sub-List 2（Agent 31501），
    "The maximum number of script execution is 21 times"（p245）；调试器约束——Make call 的发起分机必须是普通用户
    （非坐席非班长，p225），CALLING 过滤的主叫号必须与运营商送来的号码完全一致（p226）。
  conditions: c06 已完成；调试器图形窗只读、新增积木块须回编辑器（p232）。
  tags: [lab, reselection, debugger, sublist]

- id: c08
  title: LCA 脚本族——LCA_1/2/3 渐进编写、记忆清理与调试器验证
  type: lab
  source_pages: p246-292
  source_chapter: Last Called Agent rule — "Write some ASM scripts using the \"Last Called Agent\" rule"
  source_quote: |
    "Create a script named LCA_1 … If an agent has answered to the caller this day, the system applies a Priority
    (Call Selection Priority) of 2, a Reselection Timeout of 10s and the \"Last Called Agent Rule\" process." (p262)
    "To clean up the ASM Memory, you must stop the alb process … [root@cs1 ~]# kill -9 5596 … ASM memory is empty" (p272)
    "(LAST_CALLED_AGENT<>NULL) AND (LAST_CALL_ELAPSED_TIME<1DY) -> TRUE So the rule LAST_CALLED_AGENT is used" (p277)
  steps: |
    1. 建 LCA_1：连 ASM → Add new → 名 LCA_1 → Graphic mode。
    2. 第一层 IF：Statement > IF → 条件 SEQUENCE=1 → Add condition。
    3. TRUE 支路第二层 IF：条件 LAST_CALLED_AGENT <> NULL → Add；点 AND → 条件 LAST_CALL_ELAPSED_TIME < 1DY →
       Add（每条语句要加括号）。
    4. TRUE 支路动作：Set a call context variable → PRIORITY=2；再设 RESELECTION_TIMEOUT=10；Rules 页拖 Last Called
       Agent 图标。
    5. FALSE 支路：PRIORITY=8、RESELECTION_TIMEOUT=20、拖 ISM 规则（CHARACTERISTICS_LIST）。
    6. SEQUENCE>1 支路：PRIORITY=2 + ISM 规则。全部连线闭合 → 保存 → Activate 到 31603。
    7. 清记忆：OXE console（mtcl）→ adm_acd 192.168.1.3 -salb → option 28*（列记忆）→ Ctrl+C 退出 → ps -edf|grep alb
       → su -（Superuser2580*，实验口径）→ kill -9 <alb 主进程 PID> → adm_acd … 28* 复核记忆为空。
    8. LCA_1 测试（调试器挂 31603，无过滤 Commit）：第一通 0210X41660 → 轨迹 SEQUENCE=1 TRUE、LCA 条件 FALSE → 走
       ISM；查 28* 记忆新增 A33210612345 条目（含应答坐席 31500）；第二通 → 条件 TRUE → 走 LAST_CALLED_AGENT 规则。
    9. 升级 LCA_2：复制 LCA_1 → 粘贴 → 改名 LCA_2 → 打开图形编辑 → 双击 IF → AND 加条件 LAST_CALLED_PILOT =
       PILOT_NUMBER（同服务才回头）→ 保存激活 → 清记忆 → 调试器验证两通（FALSE→ISM / TRUE→LCA）。
    10. 升级 LCA_3：复制 LCA_2 改名 → IF 再加 AND (LAST_CALL_STATE = DROP_OUT_WAITING)、OR (LAST_CALL_STATE =
        DROP_OUT_RINGING)（两组括号）→ SET PRIORITY 改 0（放弃重呼最高优先）→ 保存激活 → 清记忆 → 两通验证。
  verification: |
    书中验收点：LCA_1 第二通轨迹"(LAST_CALLED_AGENT<>NULL) AND (LAST_CALL_ELAPSED_TIME<1DY)-> TRUE So the rule
    LAST_CALLED_AGENT is used"（p277）；LCA_2 需同 Pilot 才 TRUE（p284）；LCA_3 放弃重呼场景 TRUE 且 PRIORITY=0
    （p292）；每次验证前记忆为空（28* 显示 empty，p273/281/287）。
  conditions: c07 已完成；记忆清理的 kill PID 以现场 ps 输出为准（5596 为实验口径）。
  tags: [lab, lca, script, asm-memory]

- id: c09
  title: Remote PG 分布式互助部署与三类故障注入验证
  type: lab
  source_pages: p338-370
  source_chapter: Remote Processing Group — "Test the distributed mutual-aid and the remote processing group"
  source_quote: |
    "hybvisu -f all … Direct link 2002 to node 2:UP(Enabled/DATA_TRANS) High Bandwidth" (p341)
    "Agent_PG Enter a number as a resource selection priority (i.e. 0) Remote_PG Enter a number as a resource
    selection priority (i.e. 1)" (p363)
    "The second call is distributed to the Voice_guide_PG processing group because the Normal_WQ is saturated and the
    Remote_PG processing group is unreachable." (p368)
  steps: |
    1. 链路体检：OXE console（mtcl）→ compvisu sys（Direct Link ENABLED、H323 yes）；hybvisu -f all 与 hybvisu -f 2
       （链路 2002 UP/DATA_TRANS、High Bandwidth）。
    2. 本地节点 WBM（https://192.168.1.3）：Translator > Prefix plan > Create → Number=32602、Prefix meaning=Network
       No.、Network number=1、Node number/ABC-F Trunk Group=2、Type=Pilot。
    3. 本地建 Remote PG：Applications > CCD > Processing Group > Create → DN=31851、Name=Remote_PG、Type=Remote、
       Voice directory number=32602、Data directory number=32602。
    4. 本地 CCS：Configurations > Queue or Waiting Room → Normal_WQ 加 Remote_PG；Call Flow mgt > Call Distribution >
       Normal_WQ > Resource selection 勾通 Remote_PG 方向。
    5. 远端节点 WBM（https://192.168.1.103）：建 ACD 前缀（Translator > Prefix plan：Number=12、Local Features=ACD
       Prefix）；建专用 Pilot（Applications > CCD > Pilot：32602 Dedicated）；建虚拟队列（Queue：32703 Virtual_WQ，
       Type=Virtual）；建坐席 PG（Processing Group：32800 Remote_Agent_PG，Type=Agent）；建分配规则（Distribution
       Rule：Rule_0，Active=True）。
    6. 远端 CCS（Client11 新装 CCS，Master PABX=192.168.1.103）：Pilot 规则 Rule_0 并 Apply；Configurations > Pilot
       连 Dedicated → Virtual_WQ；Call Routing Normal 页启用；分配侧确认 Rule_0 活跃、Virtual_WQ 加 Remote_Agent_PG、
       Resource selection 勾通方向。
    7. 远端坐席：WBM 建 32000（PRO4，IPTouch 8068s，ACD station=ACD authorised phone set，TSC IP user 开 IP-Softphone
       Emulation）；建 32500（Agent3，ACD station=Agent，同开仿真）；Phone Features COS 类别 0 开 ACD Prefixes=1；
       CCS Configurations > Agent 给 Agent3 挂 Remote_Agent_PG 并启用 Self-Assigning；Client11 IPDSP 注册 32000/0000，
       LogOn 输 32500 → List 选 Remote_Agent_PG；Navigator 看远端矩阵。
    8. 测试一（优先级）：Call Distribution > Normal_WQ > Resource selection 设 Agent_PG=0、Remote_PG=1 → 打
       0210X41600 → Agent1 接；Agent1 置 wrap-up 再打 → Agent3 接。
    9. 测试二（门限）：Call Distribution 选 Remote_PG > Call Selection 页 thresho.=15 → Agent1 接第一通；Agent1 忙
       时第二通等 15 秒后转远端坐席。
    10. 测试三（远端闭锁）：Normal_WQ 设 Maximum waiting time=10 秒、Traffic sampling period=2 分钟；Voice_guide_PG
        （Configurations > Processing Group > PG Other）设语音引导 685、扩散 2 次；Agent3 置 Unavailable → 两侧
        Navigator 显示 Dedicated pilot 与 Remote_PG 均 blocked；Agent1 手动 wrap-up → Public 打第一通入队等待饱和 →
        Local 打第二通 → 分配到 Voice_guide_PG，播 685"There is no agent to answer you right now"两遍后释放。
    11. 测试四（断链）：OXE console mgr → Inter-Nodes Links > Logical Links (ABC-F) > Link_2 Direct IP Link > Hybrid
        or Direct Link Access → 选 1 → X25/Direct Link Synchronization → Disable → Remote_PG 显示 blocked、Dedicated
        pilot 仍 open → 重复饱和测试，第二通同样落 Voice_guide_PG。
  verification: |
    书中验收点：链路 DATA_TRANS（p341）；优先级/门限行为（p363-364 Notes）；饱和+远端不可达时"播 685 两遍后释放"
    （p368）；断链后"Remote_PG blocked、Dedicated pilot open"（p369）。
  conditions: c02 已完成（ABC-F 链路就绪）；全部 DN 为实验口径。
  tags: [lab, remote-pg, mutual-aid, fault-injection]

- id: c10
  title: Soft Panel Manager 三件套安装与基础设置
  type: lab
  source_pages: p396-417
  source_chapter: Soft Panel Manager Installation — "Install the Soft Panel Manager for OTCC Standard Edition"
  source_quote: |
    "(Default connection port: 9060) … http://localhost:9060/wbm Username: admin Password: admin" (p402-404)
    "WHEN CCS AND RTI CONNECTOR ARE INSTALLED ON THE SAME PHYSICAL SERVER, THE CCS MUST BE DEDICATED TO THE RTI
    CONNECTOR. YOU MUST NOT START THE CCS MANUALLY IF THE RTI CONNECTOR IS RUNNING." (p405)
    "afe.sites OXE main CPU address (hostname or IP address). (i.e. 192.168.1.3) … afe.pilots A list of pilots names
    to monitor" (p416)
  steps: |
    1. 前置：Client11 的 CCS 改指本地节点——Window > Customise > Network → Master PABX IP 192.168.1.103 → Modify →
       Master PABX name=192.168.1.3 → OK/Yes/OK → 重新登录（默认密码流程同 c01）→ 核对已连本地节点 → 关闭 CCS。
    2. 装 SPM 服务器：NAS 拷 ccdSoftpanel_setup.6.x.x.x.exe 到 Documents 运行 → License I Agree → 全局安装欢迎 Next →
       Destination Folder 默认 C:\SoftPanelServer → 开始菜单默认 Alcatel-Lucent\Soft Panel Server → Server
       configuration 端口 9060 → Install → 双层 Finish。
    3. 验服务：Start > Control Panel > Services 查 SoftPanelServer 运行中且自动启动；Chrome 开
       http://localhost:9060/wbm，admin/admin 登录。
    4. 核许可：mtcl 会话 adm_acd → option 15（或 spadmin）确认 OXE 有 103 号包（WBI Licence）。
    5. 装 RTI Connector：运行 RTIConnector_2.x.x.x_installer.exe → Next → License I Agree → 组件按需 → 目录默认
       C:\Program Files (x86)\Alcatel-Lucent\RTIConnector → SoftPanel Server 配置填 192.168.1.11 → Install（如弹
       Visual Basic 6.0 运行库则 Yes 并 OK）→ Finish；服务里核 RTIConnector 自动启动。
    6. 装 FlexLM：NAS 拷 softpanel.lic 到自建目录（目标 C:\FLEXlmServer\License）→ 运行 ALE-FLEXlmServer-x.x.exe →
       Yes → 浏览选许可文件 → 保持 Launch LM tool 勾选 → Finish。
    7. LMTOOLS 验证：Service/License File 选 Alcatel-Lucent FlexLM Server → Start/Stop/Reread 点 Start Server →
       Server Status 点 Perform Status Enquiry；服务列表核 FlexLM 自动启动；Web 端 Administration > Monitoring 可
       Check license。
    8. 基础设置（Administration > Settings）：General 核服务器 IP（Tomcat 端口不可改）；License Server 默认
       localhost:27000；Mail Configuration 填 SMTP 与发件人（可勾 Test the configuration 发测试件）；CCD Filters 两页
       全勾 → Save。
    9. 日统计：编辑 C:\SoftPanelServer\tomcat\webapps\wbm\WEB-INF\classes\afe.properties → afe.sites=192.168.1.3、
       afe.pilots 留空（全部）→ Real Time Data > Statistics > Ccd Consolidated 核对 S(pilot 名)_daily_* 统计生成。
  verification: |
    书中验收点：三个 Windows 服务（SoftPanelServer/RTIConnector/FlexLM）运行且自动启动（p404/407/411）；wbm 登录成
    功；LMTOOLS 状态查询正常（p411）；日统计出现在 Ccd Consolidated（p417）。
  conditions: 装在 Client11（192.168.1.11，实验口径）；许可文件由讲师提供。
  tags: [lab, spm, rti-connector, flexlm, settings]

- id: c11
  title: Soft Panel 可视化配置——背景/视图/面板/挂件/消息/告警全流程
  type: lab
  source_pages: p455-479
  source_chapter: Soft Panel Manager Configuration — "Configure and customize the Soft Panel Manager to display data on LCD screen"
  source_quote: |
    "Name Enter the name of the view (i.e. MyView) Background Browse the backgroung ans select it (i.e. sunset.jpg)" (p460)
    "Name Enter the name of the Soft Panel (i.e. MySoftPanel). Authentication Select the default option for
    authentication (i.e. No)." (p461)
    "Display time … Display date … Duration … Repeat everyday If you enable, the display date is not used." (p477)
    "Condition -<: lower >: greater … Validity timer … Notification interval If 0, the alarm will be sent only once" (p478)
  steps: |
    1. 登录：Chrome 开 http://localhost:9060/wbm（admin/admin，实验口径）。
    2. 背景：Soft Panels > Backgrounds > Add a background → Choose File 选 NAS 的 sunset.jpg → Upload background。
    3. 视图：Soft Panels > Views > New View → Name=MyView、Background=sunset.jpg → Save → 自动进入视图定制页（工具
       栏：回管理/插挂件/换背景）。
    4. 面板：回管理台 → Soft Panel > Soft Panel > New Soft Panel → Name=MySoftPanel、Authentication=No、Assigned
       views=MyView → Add → Save。
    5. 挂件操作通用：视图页工具栏 Add Widget（默认 Gauge）；单击挂件出边框——红叉删除（确认）、拖边框顶移动、拉角缩
       放、黄方块置顶/置底、下箭头改类型。
    6. 按实验配挂件集：HorizontalGauge（选计数器如 Agent1__45_ServiceState，设 Min/Max/Th1/Th2）；Chart（加统计定
       色，选折线/条/饼/3D）；Simple（计数器如 Pilot1_NbOfWaitingCalls）；Table（设行列后逐格点选文本/计数器/表头/
       对齐）；Time（日期模板）；AgentWidget（选坐席，开状态时长/电话状态/撤出状态显示）。
    7. 消息：Messages > Messages > New Message → Name=MsgWelcome、Color=red、Flash mode=Yes、Message="Welcome to ALE
       International" → Save → 点该消息 → 选 MySoftPanel → 设 Display time/Display date/Duration/Repeat everyday →
       面板端核对显示并把消息区拖到屏幕底部。
    8. 告警视图：先建专用视图并定制；Alarms > New Alarm → 引用名/描述/Enabled → Counter reference 选对象类型与统计
       （如 Sales Pilot 低效率阈值）→ 条件/值/Validity timer/Notification interval → Send an email 填收件人（分号分
       隔）/主题/正文 → Display a view 选 MySoftPanel+视图名+显示秒数（可加音频文件）→ Save。
  verification: |
    书中验收点：背景入列（p459）；视图默认内容=背景+Logo+左侧消息区（p460）；面板 MySoftPanel 可用（p462）；消息按
    时显示在面板（p477"Check the result from the soft panel"）；告警触发时指定面板在设定秒数内切换告警视图（p453/
    p479）。
  conditions: 视图定制仅 Firefox（p421）；统计须已在 CCD Filters 勾选。
  tags: [lab, spm, widgets, message, alarm]

- id: c12
  title: CCTA 话务票据分析——安装、导入 .Z、过滤出 ASCII 报表
  type: lab
  source_pages: p491-497
  source_chapter: Contact Center Ticket Analyzer tool — "Set up and use the CCTA tool"
  source_quote: |
    "PABX Enter the IP address of the Call Server (i.e. 192.168.1.3) User Enter the mtcl login (i.e. mtcl) Password
    Enter the mtcl password (i.e. mtcl) … Tickets type Select the types of tickets to be retrieved (i.e. both)" (p493)
    "The files will be dropped in C:/Program Data /Alcatel /Ticket Analyzer/ (name or IP address of the pcx)." (p494)
    "From the main menu, select Functions> File ASCII" (p497)
  steps: |
    1. 安装：Client10 从 NAS 运行 ccta_setup.msi → Welcome Next → License 接受 → 目录默认 → Start Copying Next →
       Install → Finish。
    2. 导入：启动 Importation 工具（C:/Program Files (x86)/Alcatel/Ticket Analyzer）→ 首连声明站点：PABX=192.168.1.3、
       User=mtcl、Password=mtcl（书示示例，实验口径）、Use SSH 不勾、Tickets type=both → Test 连接确认 → 导入。
    3. 核文件：C:/ProgramData/Alcatel/Ticket Analyzer/192.168.1.3 下出现 .Z 文件。
    4. 分析：运行 Ticket Analyzer → 选语言 → File > Open → Tickets on PC → PABX 填 192.168.1.3（自动拼路径）→
       Type=Communication → 起止日期 → Validate。
    5. 过滤：过滤器窗口选 Long Ticket、全部对象、ID Mao、Column → Validate 生成报表。
    6. 导出：Functions > File ASCII → 定路径命名 → Save → 打开文本核对内容。
  verification: |
    书中验收点："Import process is successful."（p494）；报表生成后能导出 ASCII 并读出结束原因/呼叫类型等字段
    （p488 口径：40 种结束原因、10 种呼叫类型）。
  conditions: OXE 侧票据机制在产话务；离线分析不占 CCS 连接。
  tags: [lab, ccta, tickets, reporting]

- id: c13
  title: 特殊功能八连配——优先转接到中继预留的配置与逐项测试
  type: lab
  source_pages: p516-530
  source_chapter: Special features — "Set up special features"
  source_quote: |
    "When agent2 becomes vacant, the second call is taken by the agent and the first call remains in the queue." (p519)
    "Agent2 (31501) who belongs to the same processing group (31800), dials the \"#013\" prefix to pick up the call." (p523)
    "Agent1 (31500) remains in the status wrap up for eternal time to wrap up automatic remaining because the
    parameter \"eternal wrap up\" has been validated in the GT agent" (p527)
  steps: |
    1. 优先转接：WBM（mtcl）Applications > CCD > Pilot > 31601 Offer > 开 Transfer with priority → Save。测试：仅
       31501 在岗——31010 打 31601 占住坐席；31011 打 31601 排队 31700；Public 拨 31000 的 DID 并把该呼叫转 31601 →
       31501 一空，优先处理转接呼叫，普通呼叫仍在队。
    2. 转接到劝恼：Pilot > 31600 After Sales > 开 Transfer to pilot in redirection。测试：调低 Normal_WQ 最大等待时
       间快速饱和 → Public 拨 31000 的 DID 转 31601，分别在参数 true/false 下对比（true=被转方听劝恼引导、转接方听
       "you can hang up"；false=转接方收"the transfer is not allowed"）。
    3. DID 忙音：Pilot > 31601 Offer 核对 Redirection Busy Tone on DID 开。测试：规则里禁用劝恼队列 → 队列满时呼叫
       默认听间隔引导音（2 号音），开启参数后改播忙音促挂机。
    4. 组内代接：Translator > Prefix plan 删除 # Local Features Speed call to associated set 前缀 → Create #013、
       General Features=Agent processing group call pickup → Categories > Phone Features COS 类别 0 开 Processing
       group call pick up。测试：Public 打 31601，31500 振铃不接，同组 31501 拨 #013 截call。
    5. 直接代接：建 #014、General Features=Direct call pickup；COS 核对 Direct call pick up 已开。测试：两坐席不同
       组（另建一组）时 31501 拨 #014+31500 截call。
    6. 监督转接：Pilot > 31601 Offer > 开 Pilot Supervised Transfer。测试：参数 No 时 31002 转后听"You can hang up to
       transfer the call"；Yes 时呼叫立即分配到空闲坐席。
    7. 永恒整理：CCS Configurations > Processing Group > PG Agent 勾 Eternal Wrap up；Configurations > Pilot 核
       Wrap Up duration=200 秒（3 分 20 秒，实验口径）。测试：31500 接 31601 后挂机 → 整理期内拨 31010 通话 10 秒挂
       机 → 坐席回到剩余整理状态直至满额。
    8. 监督监听：WBM Applications > CCD > Processing group > 31800 Agent_PG > 开 Show Supervisor Listening。测试：
       31500 通话中，班长 31502 按软键"listen ACD"+坐席号 31500 → 动态键选 listen → 坐机屏显"supervisor listening"。
    9. 中继预留：WBM Trunk Groups > 1 T2 SIP_Pub_N1 > Trunk Group > Max. % of trunks out CCD=20；Applications > CCD
       > Pilot > 31601 Offer > Trunk limitation > Create → Trunk Group ID=1、Max.% of trunk=30。
  verification: |
    书中验收点：各步"feature is enabled"回显 + 行为测试结论（优先转接次序 p519、代接截call p523-524、永恒整理 p527、
    监听显示 p528、预留数学 62→50→15 p530）。
  conditions: c02/c03 已完成；代接前缀实验先删后建避免冲突。
  tags: [lab, special-features, pilot, prefix, trunk]

- id: c14
  title: Excel 报表模板定制——FormPil 备份、Custom 工作表、图表与报表生成
  type: lab
  source_pages: p544-554
  source_chapter: Customized Excel reports — "Create a new template based on FormPil model"
  source_quote: |
    "Rename this file FormPil_old.xlsm. Open the FormPil_old.xlsm file. Save the file and rename it FormPil.xlsm." (p545)
    "Copy the links: From General tab, select the data from C7 up to D43, write click and select Copy … Paste Link (N)." (p549)
    "Select a Daily type of edit. Select an output granularity of 1/2 hour. Select Excel Display and Keep Excel links
    on Activation mode settings." (p553)
  steps: |
    1. 备份：C:\ProgramData\Alcatel\CCSupervisor\Excel\Formats 下把 FormPil.xlsm 改名 FormPil_old.xlsm → 打开 → 另存
       回 FormPil.xlsm（留回滚件）。
    2. 启宏：打开 FormPil.xlsm → Enable Content。
    3. 加工作表：右键 General 页签 > Insert > Worksheet → 把 Sheet1 改名 Custom。
    4. 拷结构：General 选 B7:D48 复制 → Custom 的 B7 粘贴。
    5. 拷链接：General 选 B7:B39 复制 → Custom B7 粘贴链接（Paste Link）；再 General C7:D43 → Custom C7:D43 粘贴链
       接。
    6. 插图表：Custom 选 C7:D43 → 插入二维柱形图 → 标题改"Total received calls" → 图例移右（Chart Elements > Legend
       > Right）→ Chart Filter 改系列名："Calls received in open state"、"Calls received in blocked state"。
    7. 生效：关模板 → 关并重开 CCSupervision。
    8. 出报表：Statistics > Excel > Pilot → 选 Pilot 31600 → 模板全选（含 Custom）→ Daily → 粒度 1/2 小时 → 激活方
       式选 Excel Display + Keep Excel links → 起止日期 → Validate。
  verification: |
    书中验收点：报表在 Custom 页按新图表呈现（"Here is an example of a statistics report displayed on Custom tab"，
    p554）；½ 小时粒度下单表只覆盖 0:00-16:00 的陷阱已在讲义声明（p542）。
  conditions: 讲义粒度陷阱——需要全天 ½ 小时数据时在 Custom 再建第二张表链到 General 第二表。
  tags: [lab, excel, reporting, template]

- id: c15
  title: CCS Server 切换——从内部 serv_ccs 到外部 Windows 服务与客户端改接
  type: lab
  source_pages: p580-590
  source_chapter: CCs Server — "switch to an internal CCS Server and to install an external CCS Server"
  source_quote: |
    "ps -edf |grep serv_ccs … /DHS3bin/afe/serv_ccs" (p583)
    "nano /usr3/afe/parameters.cfg … Modify the value from 1 to 0. … dhs3_init -R MAIN_AFE" (p584-585)
    "adm_acd 192.168.1.70 -servccs … CCS Server release 8.0 cnx= 1, afe= 1 … nbCli= 1, maxCli= 150, maxConnected= 120" (p590)
  steps: |
    1. 摸底直连：CCS（Client10）Window > Customise > Network → Modify：核对直连参数（Ping-pong 周期默认 30 秒、
       Memorise connections）；Site edition 页记 Master PABX=CPU A、Backup=CPU B；Real time > Licences 看当前锁。
    2. 查内部 Server：OXE console（mtcl）ps -edf|grep serv_ccs（列 /DHS3bin/afe/serv_ccs 进程）；adm_acd → option 11
       → 见 *SERV_CCS*4400（192.168.1.1，CPU A 静态地址）与 SALB 终端；maxConnected=15。
    3. 停内部 Server：nano /usr3/afe/parameters.cfg → Ctrl+W 搜 serv_ccs → serv_ccs_on_dhs 由 1 改 0 → Ctrl+X → Y →
       Enter → dhs3_init -R MAIN_AFE → ps 复核进程消失。
    4. 装外部 Server：WINDOWS_SRV（192.168.1.70）从 NAS 运行 serv_ccs.msi → Next → 目录 Next → Setup Type 选
       Alcatel-Lucent CCS Server → 填主 CPU IP 192.168.1.3 → Apply → Next → Install → Finish。
    5. 装服务：开始菜单开 Ccs Server Installation 工具 → Install → 核参数 OK → 服务建成 → 启动；Server Manager >
       Tools > Services 核 ccs server 自动启动。
    6. 验服务：CCS Server Status 应用 → Connect → CCS Server 绿、CCD Status 绿（已连 OXE 主 CPU）。
    7. 客户端改接：CCS Window > Customise > Network → 填 CCS Server IP（192.168.1.70）→ 提示重启 CCS → Realtime >
       Licences 复核锁；Status 工具看客户端经服务器接入。
    8. 终验：OXE console adm_acd 192.168.1.70 -servccs → option 10 → CCS Server release 8.0、cnx=1、afe=1、
       nbCli=1、maxCli=150、maxConnected=120，CLIENT10（CCS Mono）在列。
  verification: |
    书中验收点：内部进程消失（p585）；服务双绿灯（p587）；adm_acd -servccs 输出"CCS Server release 8.0 cnx= 1,
    afe= 1"且 CLIENT10 经服务器接入（p590）；日志 C:\Program Files(x86)\Alcatel\A4400 CCS Server\log。
  conditions: 一个 AFE 只能接一个 CCS Server（p575/590）；Windows Server 2019/2022 才可装外部 Server。
  tags: [lab, ccs-server, serv-ccs, migration]
```

---

## 任务覆盖自检（task ↔ id 映射）

- task-02（CCS 安装声明）→ c01
- task-01/03（POD 搭建与定稿）→ c02
- task-04/05（ACR 对象与技能）→ c03
- task-06（ISM 手算）→ c04
- task-07（ASM 编辑器安装）→ c05
- task-08/09（ISM 脚本与 LIT）→ c06
- task-10（调试器与重选）→ c07
- task-11（LCA 脚本族）→ c08
- task-12（Remote PG 网络互助）→ c09
- task-13（SPM 部署）→ c10
- task-14（SPM 显示配置）→ c11
- task-15（CCTA）→ c12
- task-16（特殊功能）→ c13
- task-17（Excel 报表）→ c14
- task-18（CCS Server）→ c15
- 覆盖自检：15 条 id（c01-c15）与全书 15 个 How-To 实验章一一对应，无缺号；每条含编号步骤（保留精确菜单路径）与 verification；YAML 以 ``` 闭合；实验值均标"实验口径"。
