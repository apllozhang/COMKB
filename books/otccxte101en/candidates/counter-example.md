# 反例/限制/边界/易错点候选 — OmniTouch Contact Center Standard · Advanced (OTCCXTE101EN Ed07)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 明文实验口令贯穿全书——生产安全基线零覆盖
  type: limitation
  source_pages: p9, p46, p52, p272, p404, p493
  source_chapter: POD INSTANCES MANAGEMENT / CCS 安装 / SPM 安装 / CCTA 导入（各处凭据）
  source_quote: |
    p9: "mtcl … Superuser2580* … root … Superuser2580* … FLEXLM SERVER … root letacla1"
    p52: "The SIP password set up for both SIP extension users is 123456."
    p46: "Password Enter the default password (i.e. alcatel)"
    p404: "Log in the Soft Panel Manager administration using the following username/password: admin/admin"
  summary: |
    教材为教学便利使用统一弱口令（mtcl/Superuser2580*、root/Superuser2580*、administrator/alcatel、admin/admin、
    FlexLM letacla1、SIP 分机 123456、ITSP alcatel），且无任何生产安全章节（密码策略、证书、加固）。交付时必须把
    这些当作"实验口径"整体替换，并回到产品安全指南补齐基线。
  conditions: 所有实验环境操作
  tags: [limitation, security, credentials, lab]

- id: n02
  title: CCS 改完 OXE 声明必须重启应用——ccs.ini 不重启不生效
  type: limitation
  source_pages: p45
  source_chapter: CCS software installation and set up / OXE declaration
  source_quote: |
    "The CCS application needs to write the updated values in the file ccs.ini file (call server IP address). So you
    must restart the CCS to consider this and the connection to the server call is established."
  summary: |
    Window > Customise > Network 改完点 OK 后会弹两次确认（修改确认 Yes、重启提示 OK），必须关闭 CCS 再启动，新
    Call Server IP 才生效。"改了连不上"先查是否漏了重启这一步。
  conditions: 修改 OXE 声明、切换直连/服务器连接时
  tags: [limitation, ccs, ccs-ini]

- id: n03
  title: ASM Script Editor 不能用 CCS 安装包补装——必须专用 msi
  type: version-trap
  source_pages: p204, p206
  source_chapter: ASM Script Editor software installation
  source_quote: |
    "If the CCsupervision application is already installed, you can't reuse the executable CCsupervision setup file to
    add the ASM Script Editor package. You must use the dedicated executable setup file (asm-se_setup.msi) dedicated
    to the ASM Script Editor application."
    "ASM Script Editor software application can be also installed during CCsupervision application installation
    process." (p205)
  summary: |
    两条安装路径互斥：装 CCS 时勾 ASM Script Editor 组件一步到位；CCS 已装后再补装，重跑 CCS 安装包无效（也不建
    议），必须单独跑 asm-se_setup.msi。漏装组件的表现是 CCS 里看不到 ASM Script Editor 菜单。
  conditions: CCS 已部署环境追加脚本能力时
  tags: [version-trap, installation, asm-script-editor]

- id: n04
  title: ASM 编辑器起不来先补 JRE——版本可高于书示
  type: version-trap
  source_pages: p207
  source_chapter: JRE software installation
  source_quote: |
    "Sometimes, Azul Zulu JRE software package need to be installed if you can't run ASM Script Editor application.
    The software version of the Azul Zulu JRE software package can be different from the one described on the
    installation process."
    "Select the zulu8.72.0.17-ca-jre8.0.382-win_i686.msi file."
  summary: |
    书示 JRE 为 Azul Zulu 8.72.0.17（8u382，32 位），但明确说明版本可不同——卡在"编辑器无法启动"时按"装 JRE"处理，
    不必拘泥书示版本号。它是 JRE 8 系列（书示文件名含 jre8）。
  conditions: ASM Script Editor 启动失败时
  tags: [version-trap, jre, installation]

- id: n05
  title: 脚本积木块的入口/出口不允许悬空——不闭合不能保存生效
  type: warning
  source_pages: p195, p212
  source_chapter: GRAPHIC EDITOR / ASM script creation Notes
  source_quote: |
    "To link 2 blocks, click on the red square and move to join the yellow one. … To remove a link, right click on the
    red square and choose remove." (p195)
    "It is not allowed to have an \"Entry\" or an \"Exit\" of a building block open." (p212)
  summary: |
    图形编辑器连线规则：红方块（出口）拖到黄方块（入口）；删线右键红方块 remove。任何积木块的 Entry/Exit 悬空即非法，
    编译前必须把 Start→…→Stop 全链闭合。脚本"保存了但不生效"先检查是否有未连线块。
  conditions: ASM 脚本图形编排全程
  tags: [warning, script, building-blocks]

- id: n06
  title: 一 Pilot 一脚本——换脚本必须重新激活
  type: limitation
  source_pages: p199, p213, p217
  source_chapter: ACTIVATION（含两处 How-To Notes 同文）
  source_quote: |
    "Only one script per pilot, or one common script for all pilots!"
  summary: |
    一个 ACR Pilot 同一时刻只挂一个脚本（或全 Pilot 公共脚本）。做 LCA_1→LCA_2→LCA_3 迭代时每次都要重新 Activate 到
    31603，否则跑的还是旧脚本——实验现象"脚本改了行为没变"九成是这个原因。
  conditions: 脚本迭代、A/B 验证场景
  tags: [limitation, script, activation]

- id: n07
  title: 直拨 ACR Pilot 无档案即空列表——21 次后播 Blocked Voice Guide
  type: limitation
  source_pages: p214
  source_chapter: ACR Script & ISM Rule / 2.3 Notes
  source_quote: |
    "There are no characteristics attached to the ACR Pilot, so no agent can be in the List. The script is used 21
    times and the call goes then to the ACR Pilot blocked address if no address is managed the \"Blocked Voice Guide\"
    will be played!"
  summary: |
    呼叫特征挂在统计 Pilot 上：直接拨 ACR 路由 Pilot（31603）没有呼叫档案，ASM 算出空列表，脚本跑满 21 次后走闭锁
    地址，未配地址就播闭锁语音引导。业务呼叫必须引导客户拨统计 Pilot 号，直拨路由 Pilot 的"死循环等待"是设计行为。
  conditions: ACR 业务号码规划与用户引导
  tags: [limitation, acr, pilot, blocked]

- id: n08
  title: LIT 受 5 分钟统计刷新限制——低话务时同坐席每 5 分钟被叫一次
  type: limitation
  source_pages: p175, p215
  source_chapter: ALGORITHM ISM Notes & ACR Script & ISM Rule / 3.1 Notes
  source_quote: |
    "LIT is not realy working. By default, the agent statistics are refreshed only every 5 min. Which means that with
    a low traffic, the same agent will be rung every 5 min."
    "Same order during the statistic period (5 min by default)" (p175)
  summary: |
    切了 asm_ag_free_duration=1 不等于呼叫级公平：坐席统计默认 5 分钟刷新，低话务量下 LIT 排序退化为"同一坐席每 5
    分钟一轮"。向客户承诺公平分配前必须讲清这个粒度，或另行评估统计周期调整（书外操作）。
  conditions: 低话务站点、公平性验收测试
  tags: [limitation, lit, statistics]

- id: n09
  title: 空列表两级回落——先路由管理方向，最后才是 Pilot 闭锁
  type: limitation
  source_pages: p220, p159
  source_chapter: Skill management by agent Notes（另见 ACR Management 尾注）
  source_quote: |
    "When you call the Statistic Pilot 31651 (Call_Profile_2: English & Home), the alb process makes 21 requests
    (script is executed 20 times) and in case of empty agent list, the call follows the routing management. If no
    other direction (Int. Overflow, …) is available, as last destination the call uses the ACR Pilot blockage mode."
    "As no script is attached to the ACR Pilot, the Waiting Room is not used; the System will try to use another
    Waiting Queue, if possible. As last resort, the ACR Pilot blockage data (Address or Voice Guide) will be used." (p159)
  summary: |
    空列表不等于直接挂断：呼叫先按路由管理找其他方向（内部溢出等），全部不可用才落到 ACR Pilot 闭锁模式。排障"客户
    电话没人接但没挂断"时，按"脚本空列表→其他方向→闭锁数据"三级链路逐级查。另注意 21 次请求=脚本执行 20 次的表
    述与 n07"脚本用 21 次"并存，两处均按原文记录。
  conditions: 呼叫无人接续的排障
  tags: [limitation, routing, fallback]

- id: n10
  title: 调试器 Make call 的发起分机必须是普通用户——坐席/班长都不行
  type: warning
  source_pages: p225
  source_chapter: SCRIPT EDITOR DEBUGGER / FILTER
  source_quote: |
    "THIS EXTENSION MUST BE A NORMAL USER, NEITHER AGENT NOR SUPERVISOR."
  summary: |
    调试器命令窗模拟呼叫时，Phone number（发起分机）不能是坐席或班长，必须是普通用户——否则轨迹不符合真实坐席话务
    路径。实验里用 MicroSIP 内部分机做发起方。全大写为原书警告样式，属硬约束。
  conditions: 调试器模拟呼叫、轨迹复现
  tags: [warning, debugger, make-call]

- id: n11
  title: CALLING 过滤的主叫号必须与运营商送来的完全一致
  type: limitation
  source_pages: p226
  source_chapter: SCRIPT EDITOR DEBUGGER / FILTER
  source_quote: |
    "The calling number must be exactly the number received from the public operator"
  summary: |
    用 CALLING 过滤器跟踪特定主叫时，输入格式必须与公网侧实际送达的号码逐位一致（含 +33 前缀形态），否则过滤不到任
    何轨迹。不确定时先用"无过滤"跑一通，从轨迹里抄真实 CLID 再设过滤。
  conditions: 调试器按主叫过滤
  tags: [limitation, debugger, clid]

- id: n12
  title: 调试器改不了脚本结构——新增积木块必须回编辑器
  type: limitation
  source_pages: p224, p232
  source_chapter: SCRIPT EDITOR DEBUGGER / SCRIPT MODIFICATION & SAVE THE TRACE
  source_quote: |
    "Part1: Script graphic mode window • Provide view of the script • Objects can't be deleted or modified" (p224)
    "Modify the script using the console part • Save the script modifications • New building blocks can't be added
    from the debugger!!" (p232)
  summary: |
    调试器三窗格的图形窗是只读的；控制台可双击改脚本属性并保存，但不能新增积木块。要改脚本结构必须回 ASM Script
    Editor 正式编辑、编译、重新激活。调试轨迹可保存留档（Save the trace）。
  conditions: 调试期脚本迭代
  tags: [limitation, debugger]

- id: n13
  title: 教材内部编号不一致——Car_Profile 挂靠 Pilot 写成 31650（正文实验为 31660）
  type: limitation
  source_pages: p236, p155, p123
  source_chapter: ISM rule and reselection / Car skill update Notes
  source_quote: |
    "Don't modify the Car_Profile, which is attached to the statistic Pilot 31650 - Language: English / Level 5 /
    Mandatory - Insurance: Car / Level 8 / Mandatory" (p236)
    "Call profile called Car_Profile assigned to Car Insurance statistic pilot (31660)" (p155)
    "Pilot Stat. Directory Number: 31650 • Directory Name: Car insurance" (p123 讲义示例)
  summary: |
    p236 的 Note 写 Car_Profile 挂在统计 Pilot 31650，但实验正文（p155）明确配到 31660；31650 是讲义章（p123）的示
    例号。操作时以本实验实际配置（31660）为准，（推断）此处为教材笔误沿用讲义示例号。同类问题：p123 讲义统计
    Pilot 号 31650 与实验号 31660 并存，照抄页码前先核对现场配置。
  conditions: 照书操作前的编号核对
  tags: [limitation, inconsistency, pilot]

- id: n14
  title: RESELECTION_TIMEOUT 是"重跑脚本"的节拍器——离线脚本同样可用
  type: limitation
  source_pages: p242
  source_chapter: ISM rule and reselection / 2.2 Notes
  source_quote: |
    "The propose of the RESELECTION_TIMEOUT Building Block is to execute the script again after the timeout (example
    10sec.). If the Agents of the 1st sub-list are busy, the 2nd sub-list will be created, after 10 sec. the 3rd
    sub-list and so on. Script can also be created \"offline\" and then transferred to the ASM Server."
  summary: |
    两个易错点：①RESELECTION_TIMEOUT 不是"呼叫最多等多久"，而是脚本重执行的间隔——第 1 子列表全忙时，10 秒后才生成
    第 2 子列表，依此类推；主叫实际等待=若干个 timeout 叠加，最长可到 21 次重选的总量。②脚本可离线创建再传 ASM 服
    务器，但必须导入并激活才生效。
  conditions: 重选参数设计与等待体验评估
  tags: [limitation, reselection, timeout]

- id: n15
  title: ASM 记忆清理必须 kill alb——重启 MAIN_AFE 不清记忆
  type: warning
  source_pages: p252, p272
  source_chapter: FUNCTIONING (next) & ASM memory clean up
  source_quote: |
    "The ASM memory is emptied when the ASM process is re-started. • MAIN_AFE re-starting has no effect on the ASM
    memory." (p252)
    "To clean up the ASM Memory, you must stop the alb process … su – … kill -9 5596" (p272)
  summary: |
    反直觉点：改 parameters.cfg 后习惯性 dhs3_init -R MAIN_AFE，但 LCA 记忆在 alb 进程里，MAIN_AFE 重启不清。要做干
    净的 LCA 测试必须 ps 找 PID → su - → kill -9 <alb>，再用 adm_acd -salb option 28* 复核为空。kill 的是 alb 主进
    程，PID 每台不同（5596 为实验口径）。
  conditions: LCA 测试前、记忆数据污染后
  tags: [warning, lca, asm-memory, maintenance]

- id: n16
  title: 教材关键字命名不一致——LAST_CALLED_ 与 LAST_CALL_ 混用
  type: limitation
  source_pages: p253, p254, p264
  source_chapter: MEMORY CALL STATUS RETRIEVING vs MANAGEMENT vs LCA_1 步骤
  source_quote: |
    "LAST_CALLED_ELAPSED_TIME • The duration between the last call time and actually time" (p253)
    "IF ((LAST_CALLED_AGENT<>NULL) AND (LAST_CALL_ELAPSED_TIME < 1DY))" (p254)
    "Define a condition Select the condition to be checked (i.e. LAST_CALL_ELAPSED_TIME)" (p264)
  summary: |
    讲义定义用 LAST_CALLED_ELAPSED_TIME，脚本范式与 How-To 操作全用 LAST_CALL_ELAPSED_TIME（LAST_CALL_STATE 同理，
    定义页写 LAST_CALLED_STATE）。编辑器里实际以下拉可选值为准（How-To 的选择路径是可执行的），抄讲义伪代码手敲时
    注意两套拼写不要混写。
  conditions: 手写/检查脚本条件时
  tags: [limitation, inconsistency, lca]

- id: n17
  title: 域与技能在 ABC 网络中全网广播——改名删技能影响面是全网络
  type: warning
  source_pages: p150
  source_chapter: ACR Management / 6.2 Skills creation Notes
  source_quote: |
    "In an ABC Network the Domain and the Skills will be broadcasted."
  summary: |
    组网环境下域与技能对象会向所有节点广播：在任一节点改技能名/删技能，全网坐席技能引用与呼叫档案同步受影响。多站点
    环境做技能体系重构前先全网评审引用关系，避免远端呼叫档案悬空。
  conditions: ABC 网络技能体系维护
  tags: [warning, skills, network]

- id: n18
  title: 无档案坐席只服务等待队列，有档案坐席才服务等待室
  type: limitation
  source_pages: p89
  source_chapter: CALL FLOW / Waiting room：call selection
  source_quote: |
    "Agent without profile I can only serve the waiting queues … Agent with profile! I serve the waiting queues And
    waiting rooms"
  summary: |
    坐席技能与分配的关系：没有呼叫档案相关技能的坐席只被普通队列分配；只有具备档案技能（且激活）的坐席才会从等待室
    拿呼叫。"等室有人等、坐席却闲着"先查坐席技能是否漏配/被停用。
  conditions: ACR 分配异常排障
  tags: [limitation, waiting-room, skills]

- id: n19
  title: 阻塞传导链——坐席无技能 → 等待室阻塞 → ACR Pilot 阻塞
  type: warning
  source_pages: p84, p148, p154
  source_chapter: CALL FLOW & ACR Management（两处 Notes 同义）
  source_quote: |
    "If no agent with skills is logged on, the waiting room is blocked, and the ACR pilot could be blocked!!!" (p84)
    "The ACR Pilot is blocked. If the Agent does not have any skill, the Waiting Room is blocked !" (p148)
    "As soon as a logged Agent has an active Skill, the Waiting Room will be open" (p154)
  summary: |
    等待室打开的前提是有"带激活技能的坐席在线"：全下线或全无技能时 WR 阻塞，ACR Pilot 随之可能整体阻塞。新配置完
    ACR 后第一通电话没人接，先看 Navigator 里 WR 是否红色/阻塞，再查坐席登录与技能激活状态，而不是先怀疑脚本。
  conditions: ACR 上线验证与早高峰排障
  tags: [warning, waiting-room, blocked]

- id: n20
  title: 建 CCD 矩阵对象前必须先建 ACD 前缀
  type: limitation
  source_pages: p346
  source_chapter: Remote Processing Group (How to) / ACD prefix creation Notes
  source_quote: |
    "The ACD prefix is mandatory prior to create the CCD matrix objects."
  summary: |
    顺序硬约束：任何 CCD 矩阵对象（Pilot/队列/处理组…）创建前，节点上必须已有 ACD 前缀。新节点或重建环境时报"无法
    建 CCD 对象"，先查 Translator > Prefix plan 里有没有 ACD Prefix。
  conditions: 新节点初始化、CCD 对象创建报错时
  tags: [limitation, acd-prefix, ccd]

- id: n21
  title: 同机共存硬约束——CCS 必须专用于 RTI Connector，RTI 运行期禁手工启 CCS
  type: warning
  source_pages: p405
  source_chapter: Soft Panel Manager Installation / RTI Connector 安装 Warning
  source_quote: |
    "WHEN CCS AND RTI CONNECTOR ARE INSTALLED ON THE SAME PHYSICAL SERVER, THE CCS MUST BE DEDICATED TO THE RTI
    CONNECTOR. YOU MUST NOT START THE CCS MANUALLY IF THE RTI CONNECTOR IS RUNNING."
  summary: |
    CCS 与 RTI Connector 同机时，CCS 实例只供 RTI Connector 用：排障时手工双击启动 CCS 抢占连接，会与 RTI Connector
    冲突导致统计断流。要人工看实时数据，另开一台 CCS 客户端或停 RTI 服务再启 CCS，二选一。
  conditions: SPM 与 CCS 同主机部署
  tags: [warning, rti-connector, ccs]

- id: n22
  title: 统计按需订阅——新挂件数值最多等 1 分钟才开始更新
  type: limitation
  source_pages: p407, p408
  source_chapter: RTI Connector Notes & Warning
  source_quote: |
    "Statistics are updated only when they are used in a view, calculated data, alarms, etc…."
    "WHEN A STATISTIC IS CHOSEN IN A WIDGET OR IN AN ALARM, IT TAKES AT MOST 1 MINUTE TO BE SUBSCRIBED AND THEN TO BE
    UPDATED"
  summary: |
    两个验收误区：①以为 SPM 上"全量实时"——实际上只有被视图/计算数据/告警引用的统计才会更新；②新配挂件第一分钟数
    值不动是正常订阅延迟，不是故障。验收面板时先制造话务再等满 1 分钟。
  conditions: 面板/告警功能验收
  tags: [limitation, rti-connector, subscription]

- id: n23
  title: 许可失效的处罚是"统计冻结"——界面常驻告警横幅
  type: warning
  source_pages: p411
  source_chapter: Soft Panel Manager Installation / FlexLM Notes
  source_quote: |
    "The license is constantly verified during the life-time of the application. If no license is found or if a
    license is found but not valid: ­ A message is permanently displayed in the administration and display mode. ­ The
    statistics updates are blocked."
  summary: |
    FlexLM 许可是全程在线校验：丢许可/许可无效时管理与显示端出现常驻告警，且统计更新被冻结——墙板数值停在最后一刻。
    "墙板不动+界面有横幅"先查许可服务器（LMTOOLS 状态、Administration > Monitoring > Check license），不要重启
    RTI Connector。
  conditions: SPM 运行期许可异常
  tags: [warning, licensing, spm]

- id: n24
  title: 已被使用的统计过滤器撤不掉——必须先删光引用对象
  type: warning
  source_pages: p415
  source_chapter: CCD filters settings Warning
  source_quote: |
    "WHEN A STATISTIC IS USED IN A WIDGET, WALLBOARD OR AN ALARM, THE CORRESPONDING FILTER CANNOT BE UNCHECKED. IF YOU
    WANT TO UNCHECK THE FILTER, YOU HAVE TO REMOVE ALL THE OBJECTS USING THE STATISTIC CORRESPONDING TO IT"
  summary: |
    收敛过滤器（Keep used filters only 提性能）时若某统计仍被挂件/墙板/告警引用，其勾选去不掉。正确顺序：先删引用对
    象 → 再撤过滤器 → 最后 Save。反过来操作会一直报"未生效"。
  conditions: 过滤器治理、性能优化
  tags: [warning, spm, filters]

- id: n25
  title: 视图定制仅限 Firefox——其他浏览器不允许
  type: limitation
  source_pages: p421
  source_chapter: STARTING WITH THE SOFT PANEL
  source_quote: |
    "The views are: • Created and initialized from the Soft Panel Manager management tool • Customized from the view
    itself using Firefox • other web browsers are not allowed for views customization"
  summary: |
    管理台可走 Chrome/Edge，但进入视图定制页（拖挂件、调布局）只支持 Firefox。用 Edge/Chrome 打开定制页的兼容问题
    （拖拽失效、参数面板异常）属不支持场景。另注意浏览器版本基线 120 起（p387）。
  conditions: 视图/挂件定制
  tags: [limitation, spm, firefox]

- id: n26
  title: HTML 挂件只认 http://——https 页面嵌不进
  type: limitation
  source_pages: p468
  source_chapter: HTML widget Notes
  source_quote: |
    "Only web sites which URL starts with \"http://\" are authorized. Nowadays, most websites use URL which starts
    with \"https://\" which make difficult to use this widget. Anyway, this one can be used if the website you want to
    reach is internal."
  summary: |
    HTML 挂件（iframe 嵌页）仅支持 http:// 开头的地址；公网 https 站点基本嵌不了，实际可用场景是内网 http 页面（如
    内部看板）。另外部分站点本身禁止 iframe，要用 Test URL 先试。客户要求"上墙外部网站"时先做可行性验证。
  conditions: HTML 挂件选型
  tags: [limitation, spm, html-widget]

- id: n27
  title: 折线图历史数据双顶——2000 个值或 24 小时
  type: limitation
  source_pages: p429, p471
  source_chapter: Global parameters – Data history & Chart widget Notes
  source_quote: |
    "historySize: number of counter updates you want to retrieve from Soft Panel Manager and to keep in memory. •
    historyTimer: the number of milliseconds to update the history line chart." (p429)
    "The Soft Panel Manager server will keep in memory a maximum number of 2000 values. If there are less than 2000
    values, the server will keep a maximum of 24 hours of statistics." (p471)
  summary: |
    折线图（历史视图）数据保留取双上限较小者：最多 2000 个采样点，不足 2000 时最多回看 24 小时。想要更长历史不能只
    调 historySize——服务器端同口径封顶，长周期趋势要落到日报（Excel/日统计）而不是实时面板。
  conditions: 历史曲线需求评估
  tags: [limitation, spm, history]

- id: n28
  title: 转接到劝恼状态 Pilot 的两种提示语——参数 true/false 行为相反
  type: limitation
  source_pages: p520
  source_chapter: Special features / Transfer to pilot in redirection Notes
  source_quote: |
    "If the parameter is set to false, when the call is transferred to the pilot and the waiting queue is saturated,
    the extension, which called the pilot for the transfer, receives the following message \"the transfer is not
    allowed\". If the parameter is set to true, transferred callers hears the guide of dissuasion and the extension
    that transfer the call receives the following message \"you can hang up to transfer the call\"."
  summary: |
    Transfer to pilot in redirection=false 时内线转接饱和 Pilot 会直接收到"不允许转接"提示；=true 时被转客户听劝恼
    引导、转接人听到"可以挂机完成转接"。验收时按参数两态分别打一通，别只测一遍就下结论。
  conditions: 转接类功能验收
  tags: [limitation, transfer, dissuasion]

- id: n29
  title: 队列满时的默认表现是 2 号间隔引导音，不是忙音
  type: limitation
  source_pages: p500, p521
  source_chapter: SPECIAL FEATURES / SENDING AN INTER-GUIDE TONE & Redirection busy tone Notes
  source_quote: |
    "Listen to the inter-guide tone if the queue is congested • instead of parking guides … Inter-guide tone Number:
    2" (p500)
    "During a call to the pilot, when the queue is full, by default the caller receives the tone inter-guide (tone n°
    2). To play the busy tone (to encourage the caller to hang up), you must validate the parameter \"Redirection Busy
    Tone on DDI\" in pilot 31601." (p521)
  summary: |
    默认行为链：劝恼不可用+队列饱和 → 主叫听 2 号间隔引导音（不是忙音、不是劝恼引导）；想让主叫听忙音促挂机，必须另
    开 Pilot 的 Redirection Busy Tone on DID。客户报"排队时是嘟嘟声/提示音怪"先对这组参数。
  conditions: 饱和行为客户体验调优
  tags: [limitation, busy-tone, congestion]

- id: n30
  title: Excel 粒度陷阱——½ 小时粒度单表只覆盖 0:00 到 16:00
  type: warning
  source_pages: p542, p537
  source_chapter: CUSTOMIZATION OF EXCEL COUNTERS / CAUTION
  source_quote: |
    "NO!, because only 1 table form has been created, so with the granularity of ½ an hour, you will retrieve only the
    transition from 0:00 to 16:00. • You must create, in \"custom\", a second table form linked to the value contained
    in the \"General\" second table form." (p542)
    "More than 24 lines to edit statistics over a day split per hour." (p537)
  summary: |
    General 表结构约 24 行（按小时一天），½ 小时粒度下一天需要 48 行——单张 Custom 表只能链到第一张表单，覆盖到
    16:00 为止。要全天 ½ 小时报表必须在 Custom 再建第二张表并链接 General 的第二表单。定制报表"下午没数据"先想到这
    一条。
  conditions: 报表粒度高于 1 小时的定制
  tags: [warning, excel, granularity]

- id: n31
  title: 改模板前先备份原件——FormPil_old.xlsm 纪律
  type: limitation
  source_pages: p545
  source_chapter: Customized Excel reports / 1.1
  source_quote: |
    "Rename the Excel file in FormPil_old.xlsm. Open the FormPil_old.xlsm file and rename it Formpil.xlsm."
  summary: |
    官方流程本身就要求"先改名留底、再另存出同名新件"——模板损坏/定制失败时用它一步回滚。跳过备份直接改 FormPil.xlsm
    一旦改坏，恢复只能重装 CCS 或找同版本拷贝。
  conditions: 任何 Excel 模板修改
  tags: [limitation, excel, backup]

- id: n32
  title: 模板改完必须关并重开 CCSupervision 才生效
  type: limitation
  source_pages: p552
  source_chapter: Customized Excel reports / 1.2.5
  source_quote: |
    "To enable the template FormPil.xlsm previously updated. ­ Close the template FormPil.xlsm. ­ Close the
    CCSupervision application and open it again to consider the new FormPil.xlsm template."
  summary: |
    模板在 CCS 启动时加载：改完 Excel 不重开 CCS，出报表还是旧结构（看不到 Custom 页签）。与 n02 的 ccs.ini 同属
    "改配置必须重启应用"家族。
  conditions: Excel 模板热更新预期
  tags: [limitation, excel, ccs]

- id: n33
  title: 一个 AFE 只接一个 CCS Server——内部进程没停，外部服务会被拒接
  type: warning
  source_pages: p575, p590
  source_chapter: EXTERNAL CCS SERVER / Maintenance
  source_quote: |
    "The AFE server can receive only one CCs server. • If the service (external CCs server) is started and the process
    (internal CCs server) isn't stopped, the connection of the external CCs server is rejected by the AFE server."
    "Only 1 CCS Server can connect to the PABX!" (p590)
  summary: |
    切换到外部 CCS Server 时若忘了把 OXE 的 serv_ccs_on_dhs 置 0 并重启 MAIN_AFE，外部服务启动后会被 AFE 拒绝（可
    用 adm_acd 观察拒接）。"外部服务装好了连不上 AFE"第一查内部进程是否真停了（ps -edf|grep serv_ccs 应无输出）。
  conditions: 内部→外部 CCS Server 迁移
  tags: [warning, ccs-server, migration]

- id: n34
  title: 两套"优先级"语义别混——分配方向 0-9 数字 vs 同优先级 LIT vs 方向间 EWT
  type: misconception
  source_pages: p363, p86-87
  source_chapter: Remote PG Notes & ACR CALL FLOW
  source_quote: |
    "It starts from 0 (highest) to 9 (lowest). The lowest is the number, the highest is the priority. … If all
    processing groups have the same priority, it's the longest idle time (LIT) that will be applied." (p363)
    "Directions with same priority • Lowest expected waiting time" (p87)
  summary: |
    三个"同分裁决"各管一层：队列内多个处理组之间比资源选择优先级数字（0 高 9 低），同级比 LIT；ACR Pilot 的多个方向
    之间同优先级比 EWT（最小预期等待）。把 LIT 当成方向选择规则、或把 0-9 数字理解为"0 最低"，都会得出相反结论。
  conditions: 分配/路由策略设计与排障
  tags: [misconception, priority, lit, ewt]

- id: n35
  title: 队列饱和+远端不可达时，溢出呼叫落到 Voice_guide_PG 播引导后释放
  type: limitation
  source_pages: p368, p370
  source_chapter: Remote Processing Group / 4.2 与 4.3 测试
  source_quote: |
    "The second call is distributed to the Voice_guide_PG processing group because the Normal_WQ is saturated and the
    Remote_PG processing group is unreachable. … The voice guide #685 \"There is no agent to answer you right now\" is
    broadcast twice and the call is released."
  summary: |
    远端 Pilot 闭锁或 ABC-F 断链时，Remote_PG 方向不可用；Normal_WQ 再饱和，第二通呼叫流向 Voice_guide_PG——播 685
    "现在没有坐席接听"两遍后释放。这是有意的兜底链（本地饱和→语音劝阻→释放），不是故障；但它意味着断链期间溢出话务
    直接流失，生产要有告警与回拨策略。
  conditions: 网络互助故障场景的话务流失评估
  tags: [limitation, mutual-aid, failure]

- id: n36
  title: Maximum waiting time=0 的特殊语义——无等待队列、直接改道
  type: limitation
  source_pages: p365
  source_chapter: Remote Processing Group / 4.2.1 Notes
  source_quote: |
    "Use \"Maximum waiting time\"=0 to configure a queue without waiting time. A call switched to this queue will be
    redirected toward another queue if no resource is available downstream, and will be distributed directly without
    waiting otherwise."
  summary: |
    MWT 取值 0-3276 秒，0 不是"无限等待"而是"零等待队列"：下游无资源立即改道其他队列，有资源则直接分配。把 0 当
    "不设限"配置会导致呼叫瞬间溢出，队列形同虚设。
  conditions: 队列参数配置评审
  tags: [limitation, mwt, queue]

- id: n37
  title: 教材数字自相矛盾——"29 or 120 CCs max"与图示 15/120
  type: limitation
  source_pages: p558
  source_chapter: CCS SERVER / OVERVIEW Physical limits
  source_quote: |
    "The maximum # of connections to the AFE is 15 • The maximum # of connections to the CCs server is 120 • From a
    physical limit point of view, 29 or 120 CCs max can be connected to the AFE."
  summary: |
    正文写"29 or 120 CCs max 可接 AFE"，同页图示为"15 connections (Internal CCs server) / 120 connections (External
    CCs server)；14 connections max + 1 connection"。按图示与其他章口径（内部 Server 15 客户端、AFE 15 连接且
    Server 自占 1 条）理解，（推断）"29"为笔误。规划 CCS 客户端数以 15/120 与 ">9 必须上 Server"（p567）为准。
  conditions: CCS 客户端规模规划
  tags: [limitation, inconsistency, ccs-server]

- id: n38
  title: 实验正文坐席称号混淆——"Agent2 (32500)"实为 Agent3
  type: limitation
  source_pages: p364
  source_chapter: Remote Processing Group / threshold 测试
  source_quote: |
    "While Agent1 (31500) is busy, call again Pilot1 (31600) and check that the call is transferred to Agent2 (32500)
    after 15 seconds."
  summary: |
    本实验中 32500 是 Agent3（远端新坐席），Agent2 是 31501（本地）。照抄验证记录会张冠李戴。读实验步骤时以括号内
    分机号为准，称号仅作辅助。
  conditions: 照书执行 Remote PG 实验
  tags: [limitation, inconsistency, lab]

- id: n39
  title: ACR/SPM 容量只给"上限清单"——话务建模与 sizing 全在书外
  type: out-of-scope
  source_pages: p77, p386, p394
  source_chapter: ACR LIMITS & SPM REQUIREMENTS & LIMITATIONS
  source_quote: |
    "For more Information check the Feature List" (p77)
    "OXE 11.1 is supported but with the same limits of previous OXE releases in terms of CCD objects." (p394)
  summary: |
    书内只有对象数与订阅数上限（ACR 12 项、SPM 500/150/200），没有 Erlang 话务模型、坐席数估算、中继数规划方法；
    超限场景一律指向 Feature List。做生产 sizing 必须回到产品文档与话务历史数据，教材数值只作合规红线。
  conditions: 生产环境容量规划
  tags: [out-of-scope, capacity, sizing]

- id: n40
  title: 安全与合规零覆盖——监听、录音、密码策略只有"开关"没有"边界"
  type: out-of-scope
  source_pages: p508, p511-512, p528
  source_chapter: VOICE MAIL（录音） & SECRET LISTENING / INTRUSION & Supervisor listening 实验
  source_quote: |
    "The supervisor may listen to the agent conversation • Agent does not ear the supervisor" (p511)
    "You see on the display of the station agent: \"supervisor listening\"." (p528)
  summary: |
    秘密监听（坐席听不到班长）、会话录音（Record 动态键 + Conversation Recording 前缀）都只教配置与操作，法律告知
    义务、隐私合规、录音留存策略完全未提。生产部署这些功能前必须补合规评审，教材不能作为合规依据。
  conditions: 监听/录音功能上线
  tags: [out-of-scope, compliance, privacy]

- id: n41
  title: 技能体系"怎么设计"缺位——只教配域配技能，不教划分方法
  type: out-of-scope
  source_pages: p120-124, p148-158
  source_chapter: SKILLS & CALL PROFILE（讲义与实验）
  source_quote: |
    "2 steps for the skills management • Definition of the skill domains • Definition of the skills (components)" (p120)
  summary: |
    教材给出域/技能/等级/权重的配置路径与算例，但"业务怎么映射到域、权重怎么定、等级标准怎么定、坐席技能怎么评定"没
    有一页。直接照实验建 Language/Insurance 两域上生产，大概率得到失真的技能路由——设计方法论要另行补充。
  conditions: 技能路由方案设计
  tags: [out-of-scope, skills, methodology]

- id: n42
  title: 嵌套 RDP 的音频设置不可省——否则坐席软话机无声
  type: warning
  source_pages: p61-62
  source_chapter: Finalizing the pod configuration / Remote Desktop Connection
  source_quote: |
    "Remote audio playback Select the option \"Play on this computer\". Remote audio recording Select the option
    \"Record from this computer\". Tick the option called \"Don't ask me again for connections to this computer\"."
  summary: |
    从 PC10 的 RDP 会话里再开 PC11 会话时，必须在 Local Resources > Remote audio 里把播放/录音都指向本机，否则嵌套
    会话里的 IPDSP 软话机没有音频，坐席实验全数失败。实验室"坐席接了没声音"第一查这里。
  conditions: 嵌套 RDP 实验布局
  tags: [warning, rdp, audio, lab]
```

---

## 任务覆盖自检（task ↔ id 映射）

- 逐页扫描口径：p39-590 的 How-To Notes/Warnings 与 p63-579 讲义 Notes 已全量过一遍，Warning 类原文（全大写警告：p225、p405、p408、p415、p84 的 !!!、p232 的 !!、p575/p590 的 Only 1）全部收录（n10/n21/n22/n24/n12/n19/n33）。
- task-01/03（环境）→ n42、n01
- task-02（CCS）→ n02
- task-04/05/06（ACR 对象与技能）→ n17、n18、n19、n20、n13
- task-08/09/10（脚本/LIT/调试）→ n03、n04、n05、n06、n07、n08、n09、n11、n12、n14、n16、n34
- task-11（LCA）→ n15
- task-12（网络互助）→ n20、n35、n36、n38
- task-13/14（SPM）→ n21、n22、n23、n24、n25、n26、n27
- task-15（CCTA）→ n01（凭据）
- task-16（特殊功能）→ n28、n29
- task-17（Excel）→ n30、n31、n32
- task-18（CCS Server）→ n33、n37
- task-20（容量/边界）→ n39、n40、n41
- 覆盖自检：42 条编号计划收敛为 42 条 id（n01-n42）连续无缺号；推断性结论（n13 的笔误判断、n37 的 29 笔误判断）均已标"（推断）"；YAML 以 ``` 闭合。
