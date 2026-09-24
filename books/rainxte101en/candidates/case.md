# 案例/实验/操作序列候选 — Rainbow Hub (RAINXTE101EN Sprint 170 Ed16)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（账号、密码、号段、POD 号）标注"实验口径"。
> 条目说明: 全书 11 个 How-To 实验章 → 12 条（成员章拆 2）+ 1 条讲义级 Generic SIP 配置操作序列（c13，非 How-To 章但属操作序列），共 13 条。

```yaml
- id: c01
  title: 创建 Rainbow Hub 客户公司（建司、补公司信息、开订阅）
  type: lab
  source_pages: p71-75
  source_chapter: Create a Rainbow Hub company — "1 Company creation (1.1 Customer company creation / 1.2 Company information / 1.3 Subscriptions management)"
  source_quote: |
    "Using BP administrator account: bpX.rv1@ale-training.com Create a new customer companies with
    following settings: - Names: Client-PX (X: POD number) - Country: France - Visibility: Closed - Define
    the customer administrator: aliceX.rv1@ale-training.com" (p72)；
    "Warning It is MANDATORY to define the time zone of the company because the voicemail and the
    calendars of the welcome services are based on it." (p73)；
    "Warning IN ORDER TO BE ABLE TO DECLARE A CLOUD PBX FOR THE COMPANY, AT LEAST ONE VOICE SUBSCRIPTION
    IS REQUIRED (VOICE BUSINESS OR VOICE ENTERPRISE)." (p75)
  steps: |
    1. 打开 https://web.openrainbow.com，用 BP 管理员账号 bpX.rv1@ale-training.com 登录（实验口径，X=POD 号，密码问讲师）。
    2. 进入 Administration/My Customers/Customer companies → 点 "Create" 按钮。
    3. 填必填项：Company name = Client-PX；Country = France；Visibility = Closed；Customer reference（选填）；Additional reference（选填）；Support e-mail address（默认取当前账号地址）。
    4. 指定客户管理员：aliceX.rv1@ale-training.com（Name: AndersonX，First name: Alice）。该用户会收到含激活链接的邮件（Notes，p73）。
    5. 补公司信息：Administration/My Customers/Customer companies/<新公司> → "Information" 区 → 填 Size、Activity、Web site、Time zone（实验口径 Europe/Paris，强制项）。
    6. 开订阅：同公司 "Subscriptions" 区 → Subscription 菜单 → "Add a new subscription" → Offer type 选 "Voice Enterprise" → 选 Monthly → 数量 4 → Subscribe（实验口径：禁止 YEAR PREPAID）。
  verification: |
    书中隐含验收：客户公司出现在 End customer companies 列表且可见性 Closed；alice 收到激活邮件；
    Subscriptions 区显示 4 条 Voice Enterprise Monthly（p72-75）。
  conditions: 需 BP/Reseller 管理员账号（建司与开订阅为 BP 专属）；alice 需完成邮箱激活。
  tags: [lab, company, subscription, voice-enterprise, bp]

- id: c02
  title: 声明并配置 Cloud PBX（Comm. Servers 声明、Call settings、公网号码段）
  type: lab
  source_pages: p99-104
  source_chapter: Create and manage the Cloud PBX — "1 Manage the Cloud PBX management (1.1 'Cloud PBX' declaration / 1.2 Public numbers management)"
  source_quote: |
    "Manage the settings: ­ Voice guide language: Select your language ­ Outbound prefix: 0 or 9 (country
    dependent) ­ SIP Trunk Group: ALE Training Carrier ­ Internal numbering plan: range 1: 100 to 199
    range 2: 200 to 299 ­ Barring: No restriction" (p100)；
    "Only one Cloud PBX can be declared per customer company." (p100)；
    "Manage the ranges of DDI numbers assigned to companies (ask confirmation to the trainer): - Client-PX:
    02982967X0-02982967X9 - Range size: 10" (p103)
  steps: |
    1. 前提：c01 已完成（公司已有 Voice Enterprise 订阅）。
    2. 声明：Administration/My Customers/Customer companies/<新公司> → "Communication" 区 → "Comm. Servers" 页签 → 点 "Create"。
    3. 填字段：Server name（PBX 名）；Server type = Cloud PBX；Voice prompts 选语言（例 French）；Dialing information：External trunk = ALE Training Carrier（实验口径，仅能选一个 trunk group）；Public number = 公司主号（默认在下一步建号段时自动定）；编号计划：Outbound prefix = 0 或 9（国家相关）、Prefixes = 成员号首位（例 1）、Number of digits = 3（默认）、可混多段拨号计划（1xx/3xx/4xxxx/6xxxxx）。
    4. 创建后编辑 Cloud PBX：勾 "Optimized phone dialing" 让话机成员免拨出局前缀（国家相关，需与 ALE 确认，p81/p101）。
    5. Call settings：Administration/…/Comm. Servers/<Cloud PBX> → "Call settings" 区，逐项核对默认规则——忙/无应答溢出到留言（超时秒数或默认）、留言邮件通知档（默认 No email notification）、外呼闭锁允许档与屏蔽档、主叫 ID 策略（用户公网号/公司号）与是否允许成员自选、软话机紧急呼叫（默认勾选）、呼转外部目的地（默认停用）、内部呼叫经外部 trunk（默认停用）、成员单/多线（默认多线）、录音提示音档（默认 None）、转移类型（协商转/盲转）。
    6. 公网号码：同公司 "Communication" 区 → "Public numbers" 页签 → Create → Public number = 02982967X0（段首，实验口径）→ 勾 "Set as company phone number" 定公司主号 → 勾 "Create a range of public numbers" → Range size = 10 → 创建（得 02982967X0-X9）。
    7. 核对：回看 Cloud PBX 设置确认主号已被自动指定为首段首号（如需改主号可用"自动改主号"选项，p104）。
  verification: |
    书中验收点：Comm. Servers 页签出现所声明的 Cloud PBX；Public numbers 页签显示 02982967X0-02982967X9
    段且主号已设置（p103-104）。
  conditions: BP 权限；公司至少一条 Voice Business/Enterprise 订阅（p75 Warning）；一公司仅一个 Cloud PBX、一 PBX 仅一条 trunk（p100-101）。
  tags: [lab, cloud-pbx, numbering-plan, call-settings, public-numbers]

- id: c03
  title: 声明话机设备：手工创建与 CSV 批量导入
  type: lab
  source_pages: p156-159
  source_chapter: Create the devices — "1 Devices creation (1.1 Manual creation / 1.2 Import in bulk)"
  source_quote: |
    "Declare phone devices with the mandatory information: ­ Type ­ MAC address" (p157)；
    "­ Download devices file template ­ Update the file providing mac addresses and device types ­ Upload
    the modified file ... Delete some of your existing devices to perform this exercise." (p158)；
    "action Action to realize for this device : create, delete, modify,.. . Here create — macAddress
    define the mac addresses — deviceType define devices type. E.g. Myriad M7 …" (p159)
  steps: |
    1. 手工建：Companies/Customer companies/<company to manage> → "Communication" 页签 → "Devices" 页签 → 点 "Create"。
    2. 填：Device type（选设备）；Mac address（终端 MAC）；Phone type（与实物对应）；Description（选填）。Notes：Member 页签可直接把设备指给成员——本实验成员未建，留到后续步骤分配。
    3. 批量建（先删几台已有设备做练习）：同页签点 "Import" → 点 "Download Sample File" 下载模板。
    4. 改 CSV：action=create、macAddress=设备 MAC、deviceType=设备类型（例 Myriad M7），保存（可另命名）。
    5. 上传修改后的文件（Import 按钮，p159 步骤 1-2-3）。
  verification: |
    书中隐含验收：Devices 页签出现新导入的设备；导入生成的设备随后续步骤关联到成员（p158-159）。
  conditions: 终端声明（含 MAC）为 BP 专属动作（p49/p58）；虚拟课堂无实物设备，可创建练习用条目（实验口径）。
  tags: [lab, devices, mac, bulk-import, csv]

- id: c04
  title: 建 DECT 8328 基站并注册分配 8214 手持机
  type: lab
  source_pages: p160-164
  source_chapter: Create a DECT base station 8328 and assign a DECT handset
  source_quote: |
    "Create a DECT 8328 base station by providing the following information: ­ Name (Important naming in
    the case of multiple 8368 base stations) ­ Type ­ MAC address ­ Cellular mode: mono (single base
    station)" (p161)；
    "Create a DECT handset 8214 — Pair it with Alice Anderson — Start registration from the DECT handset
    installation menu ... The handset is seen 'Running'" (p163-164)
  steps: |
    1. 建主站：Companies/Customer companies/<company to manage> → "Communication" 页签 → "Devices" 页签 → "DECT base stations" 页签 → 点 "Create primary base"。
    2. 填：Name（起有意义的名字——多 8368 站时命名很重要）；MAC address；Type = 8328（或 8368）；DECT cell mode = Mono 或 Dual（8328 最多 2 站、8368 最多 254 站）。虚拟课堂无基站，可建练习用（实验口径）。
    3. 查状态：点开基站编辑——Debug session 可登录基站（登录名/密码自动生成，用完记得登出）；"Restart the DECT base station" 可在故障时远端重启（p162）。
    4. 建手持机：同 Devices 页签 → 选设备类型（8214 DECT Handset）→ 填 IPEI 号与描述。
    5. 分配成员：把 8214 指给 Alice Anderson（p163 Assign a member）。
    6. 分配基站：把该手持机挂到步骤 1 建的基站上。
    7. 从 8214 手持机安装菜单启动注册（Start registration from the DECT handset installation menu）。
  verification: |
    手持机在列表中显示 "Running"（p164）。
  conditions: 终端按 IPEI 注册且必须选精确型号（不用 Generic SIP，p152）；被分配用户此前不得已有物理终端（p152）。
  tags: [lab, dect, 8328, 8214, ipei, zero-touch]

- id: c05
  title: 成员创建三法：邀请建 Bob、直接建 Carol（含电话设置）
  type: lab
  source_pages: p190-196
  source_chapter: Manage company members — "1.1 New member by invitation / 1.2 Direct creation of a new member / 1.2.1 Telephony settings"
  source_quote: |
    "Invite a new user to create his own account: ­ bobP.rv1@ale-training.com ... ­ Password: Superuser-P*
    ­ Subscription: Voice enterprise" (p191)；
    "Warning THE USER WILL APPEAR IN THE MEMBER LIST ONLY IF HE CREATES HIS ACCOUNT." (p191)；
    "Warning A MEMBER MUST HAVE A VOICE SUBSCRIPTION (VOICE BUSINESS, VOICE ENTERPRISE OR VOICE ATTENDANT)
    TO ASSIGN A PHONE NUMBER." (p194)；
    "THE EMAIL COMING FROM RAINBOW PLATEFORM COULD BE CONSIDERED AS SPAM" (p192)
  steps: |
    1. 邀请法：Companies/Customer companies/<company to manage> → "Members" 区 → "Invitation" 页签 → 点 "Invite" → 输入 bobP.rv1@ale-training.com → Continue。
    2. 用户侧：登录培训邮箱 https://mail44.lwspanel.com/（登录=邮箱、密码 PasswordP*，实验口径）→ 找邀请邮件（注意 SPAM）→ 点链接建户：First name Bob、Name BarkleyP、Password Superuser-P*（实验口径；≥12 字符含大写/数字/特殊字符）。
    3. 管理员补配：Members → 选 Bob → 补订阅 Voice Enterprise 等（邀请户建完后管理员 finalize）。
    4. 直建法：Members 区 → "Members" 页签 → 点 "Create" → 填 Login = carolP.rv1@ale-training.com、Password = Superuser-P*、Sign-in method 默认、Visibility = Same as company、Last name ConnorP、First name Carol、语言/国家/时区、Subscription = Voice enterprise、Site（多站点用）、勾选 Send enrollment email → Create。
    5. 电话设置（给 Alice/Bob/Carol 配号）：Members/<用户> → "Phone" 页签 → Equipment = Cloud PBX → Extension number 选分机（Alice 101 / Bob 102 / Carol 103，实验口径）→ Public number 从公司号池选（02982967P1/P2/P3）→ Device 有实体话机才选 → 核对该页其余项：Rainbow number（只读）、Call forwarding 三档（无条件/忙/无应答：留言/内线/公网号）、单/多线、Personal routines（默认 At work）、留言溢出与邮件通知档、外呼闭锁档、主叫 ID 策略与自选权限、录音档、Custom SIP Headers → Apply。
  verification: |
    Members 列表出现 Bob（完成建户后）与 Carol；电话页签显示内线/公网号已分配；alice 收到 enrollment 邮件
    （p193-196）。Notes：成员没有物理话机也可以配号码——纯软话机用户（p194）。
  conditions: c01 已完成（订阅已开）；分配号码前成员必须有 Voice 订阅（p194 Warning）。
  tags: [lab, members, invitation, direct-creation, telephony-settings]

- id: c06
  title: 成员批量导入（CSV）与标签/档案/可编程键/个人例行程序配置
  type: lab
  source_pages: p197-206
  source_chapter: Manage company members — "2 Import users in bulk / 3 Tags configuration / 4 Profiles configuration / 5 Programmable keys configuration / 6 Manage Personal routine"
  source_quote: |
    "Create a new member using bulk import: ­ Download the template file for users ­ Copy / paste an
    example user and modify only the necessary parameters ­ daveP.rv1@ale-training.com ... ­ Numéro: 104
    ­ Public number: 02982967P4" (p197)；
    "A pop-up is displays possible errors before import ... Click on 'Send enrollment email to new users'
    ... A report is generated each time you use the bulk import function" (p199)；
    "Warning WHEN VALIDATING A NEW PROFILE, THE SYSTEM WILL ASK IF THIS ONE MUST BECOME THE NEW DEFAULT
    PROFILE FOR THE COMPANY" (p201)
  steps: |
    1. 批量导入 Dave：Members 区 → "Members" 页签 → 点 "Import" → 选 CSV 图标 → "Download the sample file" → 复制示例行改参：Upsert（创建）、Login = daveP.rv1@ale-training.com、Password = Superuser-P*、Firstname DavidsonP/Lastname Dave、Internal number 104、DID 02982967P4、Subscription Voice Enterprise、设备 MAC（如有）→ 保存上传。
    2. 导入前看错误弹窗 → 勾 "Send enrollment email to new users" → 看导入报告（绿/红图标点开看明细）。
    3. 标签：Members 区 → "Tags" 页签 → Create → 建 "HR" 指派给 Alice；建 "Building A" 指派给 Alice 和 Bob → 回 Members 页签按 tag 过滤搜索验证。
    4. 档案：Members 区 → "Profiles" 页签 → 下拉 "+ Create a profile" → 建 "Restricted collaboration"（去勾 Use animated GIFs in conversations、Access and use Rainbow personal storage space）→ 验证时注意系统询问是否设为公司默认档案 → Members/Carol/Permission 页签选该档案 → Apply。
    5. 应用直呼键：Members/Alice/"Prog keys" 页签 → 选 "Speed dial" → Create → Label=Carol、Key=103 → Create。
    6. 话机可编程键：Members/Alice/"Prog keys" 页签 → 选 "Device" 选一个键 → 类型选 speed dial → 目的地选 Carol（Type: Speed dial or supervision；Type de destination: Member or group）。
    7. 个人例行程序：以 Alice 登录 → 头像 → Personal routines → Configure → 把 "Do Not Disturb" 改为来话转 Bob Barkley。
  verification: |
    导入报告无红行、Dave 出现在成员列表；tag 搜索能按 HR/Building A 过滤；Carol 的 Permission 显示受限档
    案；Alice 应用左栏出现 Carol 直呼键；DND 档生效后呼叫 Alice 转到 Bob（p199-206）。
  conditions: c05 已完成（成员与号码已配）；批量导入由 BP 或客户管理员执行（p169）。
  tags: [lab, members, bulk-import, tags, profiles, prog-keys, routines]

- id: c07
  title: 建 Hunt Group（含溢出）与 Manager/Assistant 组
  type: lab
  source_pages: p233-237
  source_chapter: Create members groups — "1 Hunting group / 2 Manager/Assistant group"
  source_quote: |
    "Create the following hunting group: ­ Directory number 100 ­ Public number: Assign a public number ­
    Distribution: serial ­ Members: 101 and 102 ­ Lock the last member in the group" (p234)；
    "Tips Edit the group again if you want to activate call overflow" (p235)；
    "Manage the manager/assistant group: ­ The group number is: 106 ­ Assign a public number, the public
    number is assigned to the group, not to Dave. ­ Manager : Dave ­ Assistant : Carol" (p236)
  steps: |
    1. 建 hunt group：Companies/Customer companies/<company to manage> → "Communication" 区 → "Groups" 页签 → 点 "Create"。
    2. 填：Name；Type = Hunt group（或 hunt group with waiting queue）；Subtype = Regular；Distribution = serial（实验口径；parallel/circular 可选）；Send call to next member 定时器（仅 serial/circular，默认 10 秒）；Internal number = 100；Public number = 从号池选。
    3. 第二页：Emergency group 标记（本组不勾）；Lock the last member（no empty group）= Yes；Allow the group manager to modify the DDI = Yes/No → 选成员（按姓名或邮箱搜，选 101、102）→ Apply。
    4. 配溢出：Groups 页签编辑该组 → Call recording 选 all/external/internal/none → 激活 busy 与 no answer 溢出 → Destination type（voice prompt/member/group/internal number/public number/voicemail/welcome service/automated attendant）→ 选具体目的地/成员。
    5. 建 manager/assistant 组：Groups 页签 → Create → Name；Type = Hunt Group；Subtype = Manager/Assistant；Internal number = 106；Public number（注意号码配给组而非 Dave 个人）；Lock the last… → Next → 选 Manager = Dave、Assistant = Carol → Apply。
  verification: |
    书中隐含验收：Groups 页签两个组可见、成员在列；溢出配置保存（p234-237）。组创建后自动生成对应
    bubble（含组留言与通话记录管理，p217 讲义口径）。
  conditions: 创建后可增删成员（Notes，p235）；多助理/助理跨多组按 Notes（p237）扩展。
  tags: [lab, hunt-group, overflow, manager-assistant, groups]

- id: c08
  title: 紧急号码查询、紧急组创建（两法）与激活
  type: lab
  source_pages: p238-242
  source_chapter: Emergency numbers and emergency group — "1.1 Emergency number consultation / 1.2.1 Emergency group creation / 1.2.2 Emergency group activation"
  source_quote: |
    "Consult the emergency numbers — Companies/Customer companies/ <company to manage> 'Communication'
    section / 'Traffic control' tab / Emergency numbers — Emergency numbers are automatically configured
    according to the country and the trunk group" (p239)；
    "Warning BY DEFAULT, USING WITH WAY, 'EMERGENCY GROUP' IS NOT VALIDATED BY DEFAUT. DON'T FORGET TO DO
    IT." (p241)；
    "Activate the emergency group just created. ... Click on 'Activate'" (p242)
  steps: |
    1. 查号码：Communication 区 → "Traffic control" 页签 → Emergency numbers——号码按公司国家+trunk 组自动配置（实验环境显示法国表）。
    2. 建紧急组方法 1（推荐，标记默认勾选）：同页点 "Create emergency group" → 按建 hunt group 填：Name = WFA、Distribution = parallel、Internal number = 110、成员 Alice 和 Carol（Emergency group 标记默认已勾）→ 加成员。
    3. 建紧急组方法 2：Communication 区 → "Groups" 页签 → Create → 填同上信息 → 手动勾选 Emergency group 框 → 加成员（此路默认不勾该框，勿忘）。
    4. 激活：Traffic control/Emergency numbers → 点 "Activate"；或 Administration/…/Comm. Servers/<Cloud PBX> → "Call settings" 区 → 勾 "Activate emergency group"。
  verification: |
    紧急组显示已激活；行为口径（讲义）：激活后免前缀紧急呼叫路由到组而非外线；组员转公共紧急号须加前缀
    （例 0112）（p227-228）。
  conditions: 一公司仅一个紧急组（p228）；紧急号码保留不可改、不可占作内线号（p227）。
  tags: [lab, emergency, emergency-group, activation, compliance]

- id: c09
  title: 欢迎服务实验：建日历、建欢迎服务、导提示音、测试、自定义 MoH
  type: lab
  source_pages: p277-283
  source_chapter: Welcome service & Music on hold — "1 Create calendars / 2 Welcome service creation / 3 Import of customized voice prompts – Open/close / 4 Make a Test / 5 Customize the Music on hold"
  source_quote: |
    "Create a calendar with opening/closing hours that will be associated with a company welcome service:
    ­ Open from Monday to Friday ­ Open from 8 am to 6 pm ­ Manage Christmas as a bank holiday" (p278)；
    "Warning: Associate the voice prompts with the right Calendar!" (p281)；
    "Tips Modify the open and closed hours of the company in order to check the voice prompts" (p282)
  steps: |
    1. 建日历：Companies/Customer companies/<company to manage> → "Communication" 区 → "Welcome services" 页签 → Calendar 菜单 → Create → 起名。
    2. 编辑日历：按周一至周五、8:00-18:00 配各天时段；"Specific days" 页签 → Add date → 加圣诞为闭店日（红=closed）→ Apply。日历时区=公司时区（Note，p279）。
    3. 建欢迎服务：Welcome services 页签 → Welcome 区 → Create → 填：Service=Welcome；Name=Company Welcome；Calendar=Main company Calendar（先建日历再建服务）；Public number 从空闲号池选；Open hours – Destination type = member/group/AA/group with waiting queue 并选目的地（实验选 Hunt group）；Closed hours – Destination type = closing voice prompt（voice prompt/external number/AA/member/group/welcome service 可选）→ Apply。
    4. 导提示音：Communication 区 → "Voice prompts" 页签 → Welcome 区 → 过滤器选刚建的欢迎服务 → Add → 选文件 welcome service.mp3（欢迎）→ 定义 Usage（Welcome/closed hours）→ 填描述 → Upload；同法导 Closinghours.mp3（闭店提示）。注意提示音要挂在正确的日历上（Warning）。
    5. 测试：拨打欢迎服务公网号，核对开/闭时段提示音播对（Tips：临时改公司开闭时段来验证）。
    6. 自定义 MoH：Voice prompts 页签 → General 区 → 核对过滤器 General → Add → 选 New_MOH.wav → Usage = Music on hold → Upload。列表刷新后 MoH 已上传并激活。
  verification: |
    拨测开/闭时段各自提示音正确播报（p282）；Voice prompts 列表绿色标显示自定义提示（p282）；MoH 生效
    （p283）。
  conditions: 音频文件 ≤4MB、问候 ≤120 秒（p263）；日历法定假日不预填须手工加（p256）；实验音频文件由讲师提供（实验口径）。
  tags: [lab, welcome-service, calendar, voice-prompts, moh]

- id: c10
  title: 话务台实验：订 Voice Attendant、建监督组、开控制台、建 attendant group
  type: lab
  source_pages: p284-289
  source_chapter: Attendant console, supervision group and attendant group
  source_quote: |
    "Subscribe to the service 'VOICE ATTENDANT' ... Companies/Customer companies/ <company to manage>
    'Subscriptions' section ... Choose an offer — Use monthly for this lab" (p285)；
    "Create a supervision group ­ Supervisor: for example, Elliot Evans (with the subscription VOICE
    ATTENDANT) ­ Members to supervise: Carol Connor and Bob Barkley" (p287)；
    "web.openrainbow.com or application — Click on [icon] to access Attendant console" (p288)
  steps: |
    1. 订阅：Subscriptions 区 → "Add a new subscription" → 选 VOICE ATTENDANT → 选 Monthly（实验口径：lab 用月付）→ 定许可数 → Subscribe（p285-286）。
    2. 分配：Members 区 → 编辑用户（例 elliotX.rv1@ale-training.com，实验口径）→ "Services" 页签 → 选 "Voice Attendant Monthly"。
    3. 建监督组：Communication 区 → "Supervision" 页签 → Create → 填 Name/Description → 选持 VOICE ATTENDANT 的监督员（Elliot Evans）→ 勾被监督成员（Carol Connor、Bob Barkley）→ Create。
    4. 开控制台：以 Elliot 登录 web.openrainbow.com 或客户端 → 点话务台图标进入 Attendant console（监督页签、BLF 区、呼叫队列）。
    5. 建 attendant group：Administration/Customer companies → "Communication" → "Groups" → Create → Type=Hunt Group、Subtype=Attendant → 配内线与 DDI → 成员选持 VOICE ATTENDANT 的用户（例 Elliot）→ Perform the test（p289）。
  verification: |
    控制台可打开并显示监督成员状态（p288）；attendant group 建成后按讲义口径可分配话务（Attendant 组全员
    须 Voice Attendant 订阅，p249）；话务台三档显示 Normal/small/condensed（p246）。
  conditions: Voice Attendant 用户不能用手机端话务台、不能用话机——激活话务台后话机关联被删（p246 Warning）；
    监督员 5 组/组 30 人规格（p224）。
  tags: [lab, attendant-console, supervision-group, voice-attendant, attendant-group]

- id: c11
  title: 自动话务员 IVR 实验：建 AA、挂公网号、建菜单树、配两级语音提示
  type: lab
  source_pages: p290-300
  source_chapter: Automated attendant — "1.1 Creation / 1.1.2 Assign the public number / 1.2 Menus Creation / 1.3 Voice prompts configuration"
  source_quote: |
    "Create a new automated attendant ­ Name: company AA ­ Choose a free public number in the list
    assigned to your pod: i.e. 02982967P8 (done in 2 steps) ­ Choose unique voice prompts for main and
    submenus: Menus with single voice prompts" (p291)；
    "Manage the following choices: ­ 1 -> Transfer to Alice ­ 2 -> Transfer to Bob ­ 3 -> Transfer to
    Marketing dpt" (p296)；
    "Usage Menu welcome or Exit" (p298)
  steps: |
    1. 建 AA：Communication 区 → "Welcome services" 页签 → Automated attendant 页签 → Create → Name = company AA；勾 "Menus with single voice prompts"（每菜单唯一提示，建后不可改）；Call overflow 目的地类型（internal number/IVR/welcome service/group/voice prompt/member）备用。
    2. 挂公网号：编辑该 AA → Service Information → Public number = 02982967P8（实验口径，从 POD 空闲号选，两步完成）。
    3. 建菜单：进入 AA → 把默认 Menu 1 改名 "Main menu" → Apply；点 "Create menu" → Name = Marketing → Create（此时未挂到主菜单）。
    4. 配主菜单树：<AA>/<Main menu> → Manage choices → 1=Transfer to Alice、2=Transfer to Bob、3=Transfer to Marketing 菜单 → 得预期树。
    5. 配 Marketing 菜单：下拉选 Marketing → 1=Transfer to Carol、2=Transfer to Dave。
    6. 主菜单提示音：<Main menu> → "Menu voice prompts"（不离开 AA 直达提示音页）→ 核对选中正确的 AA 与 Main menu → Add → Browse 选 AA_ALEMainmenu.wav（实验口径，问讲师取）→ Usage = Menu welcome 或 Exit → 描述 → Upload。
    7. Marketing 提示音："Communication"/"Voice prompts" 页签路径进入 <AA>/<Marketing Menu> → 同法传 AA_ALEMarketingmainmenu.wav。
  verification: |
    菜单树两页 "Result expected" 与配置一致（p296-297）；提示音列表更新；拨 AA 公网号按提示选键路由到对应
    成员/菜单（讲义口径 p271 三级示例）。
  conditions: IVR 最多 3 级、根菜单 10 项 0-9（p266）；唯一提示模式建后不可改（p270）；保密：来话显示默认名
    而非欢迎服务技术号（p269）。
  tags: [lab, aa, ivr, menus, voice-prompts]

- id: c12
  title: 多站点实验：建站点、分布用户、挂服务、定站点主号、配站点 MoH
  type: lab
  source_pages: p307-316
  source_chapter: Create multiple sites for a company — "1 Sites creation / 2 Distribution of users / 3 Distribution of other services and definition of the main number for each site / 4 Customization of music on hold"
  source_quote: |
    "The company has already been set up. We are going to create two sites, Brest and Rennes ... Public
    numbers will be linked to each site. Each site will also have its own hold music." (p308)；
    "Distribute members to sites according to their place of work ­ Alice and Bob work in Brest ­ Carol
    and Dave work in Rennes" (p309)；
    "Select « set as site phone number »" (p314)；
    "Customer company/ Communications/ 'voice prompts' tab/ 'Site' tab ... Select the site: Brest ... The
    hold music is customized." (p315-316)
  steps: |
    1. 建站点：以 BP 管理员登录 web.openrainbow.com → Customer company → Informations → "Sites" 页签 → Create → 建 Brest 与 Rennes。
    2. 分配用户：Members 菜单 → 编辑成员 → Information 处选站点——Alice、Bob → Brest；Carol、Dave → Rennes（成员编辑页的 Sites 字段，p171）。
    3. 核对/编辑站点：Informations/"Sites" 页签按成员或按公网号两种入口查看（跳转到带站点过滤器的 Members / Public Numbers 页，p311-312）。
    4. 服务挂站点：Communications → "Public numbers" 页签 → 编辑服务/组/成员（实验：编辑一个 AA）→ "Informations" 页签 → Site 选 Rennes → 可勾 "set as site phone number" 把该 AA 的公网号定为站点主号。
    5. 站点 MoH：Customer company → Communications → "Voice prompts" 页签 → "Site" 区 → 选站点 Brest → Add → 选本地文件 Upload → 同法配 Rennes。
  verification: |
    Sites 页签显示两站点及其成员/号码；AA 挂到 Rennes 且其号码成为站点主号（p314-315）；两站点 MoH 各自
    生效（p315-316）。不变量口径（讲义）：内呼互通、组跨站、欢迎服务/AA 与目录全公司共用（p304）。
  conditions: 实验用 SIP 模拟器无 Rennes 区号（0299…），号码沿用培训号段（实验口径 Note，p311）；一公司仍只有
    一个 Cloud PBX（p92）。
  tags: [lab, multi-site, sites, moh, site-number]

- id: c13
  title: Generic SIP 设备配置操作序列（手工/批量 + 证书链下载，讲义级）
  type: howto
  source_pages: p124-131
  source_chapter: GENERIC SIP DEVICES / Manual configuration & Bulk import
  source_quote: |
    "Create the device • Select the device type • Choose: « Generic SIP » • Settings Management • MAC
    address • SIP domain • SIP password • Certificates • Configure the SIP device" (p125)；
    "Edit the device — Download the CA certificates chain" (p127)；
    "Select the file and click Import — The devices have been created and must be linked to Rainbow
    accounts" (p131)
  steps: |
    1. 手工线：Communication/Devices → Create → Device type 选 "Generic SIP"。
    2. 管理设置：录入 MAC 地址、SIP domain、SIP username、SIP password；编辑该设备 → 下载 CA 证书链（Rainbow 服务器证书链，供终端侧认证）。
    3. 终端侧：按支持文章"Setting up Rainbow Hub to interconnect third-party SIP extensions"在设备上配网络与 SIP（TLS 1.2+ / SRTP，推荐 G711，p118）。
    4. 批量线：Devices 页签 → Import → 下载模板 → 填 action（create/update/delete）、MAC、设备类型、SIP 密码（仅 Generic SIP 需要）→ Import → 看报告。
    5. 回连账号：导入生成的设备须再手工（或批量）关联到 Rainbow 账号（p131）。
    6. 部署前后检查清单（p119）：先测互操作/编解码/证书；装时开 TLS/SRTP、记录配置、核固件；装后盯 SIP 注册、音质、收日志。
  verification: |
    书中本章无独立测试问题；验收按部署后清单（SIP 注册正常、音质合格）执行（p119）；批量导入后设备出现在
    Devices 列表（p131）。
  conditions: Generic SIP 无 RCC/无统一在场/无固件自动更新；ALE 不为大规模第三方话机部署兜底（p120）；8 款
    参考设备指南见 p122。
  tags: [howto, generic-sip, certificates, bulk-import, interop]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 24 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 网络前提与 Pilot | 无实验。概念章（p36-45），Pilot 为外部工具介绍页，书中无分步实验。 |
| task-02 公司体系创建 | 有 → c01（建司+公司信息+订阅三合一 How-To）。SSO/TOTP 为概念页（p54），无实验。 |
| task-03 管理员权责、目录/频道 | 无独立实验章。p57-62 为概念讲义（目录/频道仅截图级步骤）。 |
| task-04 订阅开通与分配 | 分散覆盖：c01 步骤 6（开 4 条 Voice Enterprise Monthly）、c10 步骤 1-2（订并分 Voice Attendant）。 |
| task-05 Cloud PBX 声明与配置 | 有 → c02 |
| task-06 号码分配与主叫策略 | 有 → c02（内含 Public numbers 段创建与主号设定；成员级主叫策略在 c05 步骤 5） |
| task-07 流量控制与闭锁 | 无独立实验。p85-87 概念页；Call settings 的闭锁档位在 c02 步骤 5 核对。 |
| task-08 trunk 商务与带宽 | 无实验。p88-90 概念页（trunk 由讲师预配 ALE Training Carrier，见 c02）。 |
| task-09 多站点规划（概念侧） | 概念页 p91-93 并入 c12 前置；无独立实验。 |
| task-10 成员管理 | 有 → c05（邀请+直建+电话设置）、c06（批量导入+标签/档案/按键/例行程序） |
| task-11 设备部署 | 有 → c03（手工+批量声明）。zero-touch 上线行为（p136-139）为讲义口径，无现场实验（虚拟课堂无设备）。 |
| task-12 设备维护日志 | 无独立实验。p141-145 概念页（debug/pcap/webadmin 报告步骤仅截图级）。 |
| task-13 Generic SIP 接入 | 有 → c13（讲义级操作序列，非 How-To 章） |
| task-14 DECT 部署 | 有 → c04 |
| task-15 Hunt Group 与队列 | 有 → c07（含溢出配置；队列参数为建组 Type 选项） |
| task-16 Manager/Assistant | 有 → c07（第 5 步） |
| task-17 话务台与监督组 | 有 → c10 |
| task-18 紧急号码与紧急组 | 有 → c08 |
| task-19 录音与归档 | 无独立实验。p230-231 概念页；组级录音开关在 c07 步骤 4。 |
| task-20 欢迎服务全家桶 | 有 → c09 |
| task-21 IVR 配置 | 有 → c11 |
| task-22 多站点配置 | 有 → c12 |
| task-23 分析体系 | 无实验。p317-328 概念页（仪表盘/CDR/报表仅截图级）。 |
| task-24 维护支持体系 | 无独立 How-To 实验。p330-343 概念页；设备日志相关步骤见 c13 前置与 p 系条目。 |

**统计**：13 条（lab 12 条 + howto 1 条）；24 项任务中 12 项有案例类条目直接覆盖（task-02/04/05/06/10/11/13/14/15/16/17/18/20/21/22 中取 12 章口径），其余为概念章或查表内容无实验（task-01/03/07/08/09/12/19/23/24）；订阅分配（task-04）以实验口径分散在 c01/c10。
