# 原则/清单/规则/公式/数值口径候选 — OpenTouch Suite for MLE (OPENXTE300EN Ed10, R2.6.1)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: 容量口径：OTMS 与 OTMS-v 均上限 5000 用户；物理服务器由 BP/客户提供
  type: metric
  source_pages: p5, p9
  source_chapter: Solution Overview / Introduction / OTMS delivery modes
  source_quote: |
    "OTMS 5000 users max" (p5)
    "OTMS up to 5000 users • Physical server provided by Business Partner or customer ... OTMS-V up
    to 5000 users" (p9)
  summary: |
    两种交付形态（物理一体机 OTMS、虚拟化 OTMS-V）的用户容量口径一致：均 5000 用户上限。
    硬件平台不由 ALE 提供，由 BP 或客户自备，兼容性用 OTCP 工具核对。
  conditions: 平台兼容性核对工具 OTCP（p9 标注 (*)）
  tags: [metric, capacity, sizing]

- id: p02
  title: 虚拟化与 OS 支持矩阵：ESXi 6.5/7.0.x、Hyper-V 2016/2019、SLES 12 SP5
  type: metric
  source_pages: p9
  source_chapter: OTMS delivery modes
  source_quote: |
    "Virtualization platform cross-compatibility VMware ESXi (6.5 and 7.0.x) Microsoft Hyper-V (2016
    & 2019) ... Operating system Suse Linux Enterprise Server 12 SP 5" (p9)
  summary: |
    虚拟化平台仅支持 VMware ESXi 6.5 与 7.0.x、Microsoft Hyper-V 2016 与 2019；OTMS 软件包操作系统为
    SUSE Linux Enterprise Server 12 SP5。做兼容性核查与升级规划时的版本基线。
  conditions: Ed10/R2.6.1 时代口径
  tags: [metric, virtualization, version]

- id: p03
  title: SOT 宿主要求：standalone 需 VirtualBox ≥5.2.24 / VMware WS ≥14；hosted 需 ESXi ≥6.0；Template Factory 需 8CPU/16GB/500GB
  type: metric
  source_pages: p55, p56, p59
  source_chapter: S.O.T. / Stand-alone / Hosted / Template Factory
  source_quote: |
    "Installed on technician laptop thanks to Virtual Box client (version 5.2.24 minimum) or VMware
    workstation (version 14 minimum)" (p55)
    "Deployed in a vSphere ecosystem : ESXI server version 6.0 minimum" (p56)
    "Pre-requisites for the S.O.T. VM 8 CPUs / 16Go memory size / 500Go for the second disk • Vmx flag
    (or Virtual machine capability) activated on the CPU specification • USB controller available" (p59)
  summary: |
    SOT 虚机宿主底线：standalone 模式 VirtualBox ≥5.2.24 或 VMware Workstation ≥14；hosted 模式 ESXi ≥6.0。
    Template Factory 配置加码：8 CPU / 16 GB 内存 / 第二块盘 500 GB，CPU 开 VMX 标志，必须带 USB 控制器；
    启动自检不过时可用 templateFactory 命令列出缺失项。
  conditions: 虚机规格详见 SOT Delivery note
  tags: [metric, sot, requirements]

- id: p04
  title: Post-install 账户口令硬规则：全部 ≥8 字符且无报错弹窗；管理员/模板口令需大写+数字+特殊字符；用户名不得用系统保留名
  type: rule
  source_pages: p95, p96
  source_chapter: OTMS Post-installation wizard / OpenTouch Core Settings
  source_quote: |
    "THE ACCOUNT USERNAME MUST ALL BE DIFFERENT AND MUST NOT BE "ADMIN", "ADMINNMC", "HTUSER" OR ANY
    OTHER EXISTING ACCOUNT. ALL PASSWORDS ON THIS PAGE MUST CONTAIN AT LEAST 8 CHARACTERS. THERE IS NO
    ERROR POP-UP IN CASE YOU USE LESS THAN 8 CHARACTERS BUT YOU WILL FACE PROBLEMS AFTERWARDS." (p95)
    "Administrator Password Enter the administrator password (8 characters minimum, one upper case,
    one figure, one specific character)" (p96)
    "IT IS RECOMMENDED TO NOTE THE DIFFERENT USERNAMES AND PASSWORDS BECAUSE YOU WILL NEED THEM TO
    DECLARE OPEN TOUCH NODE IN OMNIVISTA 8770 SERVER." (p96)
  summary: |
    四条硬规则：(1) 本页所有账户用户名必须互不相同，且不得使用 admin/adminnmc/htuser 等既有账户名；
    (2) 本页全部口令至少 8 字符——少于此长度不会弹任何报错，但后续必出问题；(3) otAdmin/otProfile 的
    口令另需大写字母+数字+特殊字符；(4) 全部用户名口令要记录存档——8770 声明 OT 节点时逐项要用。
  conditions: 实验值：root=superuser、otuser=maintenanceuser、otAdmin=Admin-8770、otProfile=Admin-T1、SNMP=adminsnmp（实验口径）
  tags: [rule, security, post-installation, checklist]

- id: p05
  title: DNS 正反向解析清单：OT/8770/邮件/LDAP/OXE 呼叫服务器 FQDN 全部要能正反向解析
  type: checklist
  source_pages: p93
  source_chapter: OTMS Post-installation wizard / Network settings
  source_quote: |
    "THE DNS MUST BE CONFIGURED TO RESOLVE (FORWARD AND REVERSE RESOLUTION): • OPENTOUCH SERVER FQDN
    • OMNIVISTA 8770 SERVER FDQN • MAIL SERVER FDQN • LDAP SERVER FDQN • ALCATEL-LUCENT OMNIPCX
    ENTERPRISE COMMUNICATION SERVER CALL SERVER: • NO REDUNDANCY: CALL SERVER FQDN • LOCAL
    REDUNDANCY: CALL SERVER MAIN ROLE FQDN • SPATIAL REDUNDANCY: EACH CALL SERVER FQDN" (p93)
  summary: |
    向导网络页的 DNS 核查清单：OT 服务器、OmniVista 8770、邮件服务器、LDAP 服务器、OXE 呼叫服务器的
    FQDN 全部要配正向+反向解析；OXE 侧按冗余形态分别核（无冗余核呼叫服务器 FQDN，本地冗余核主角色
    FQDN，spatial 冗余逐台核）。另注：本地 DNS 服务器仅在 OXE 未做 duplication 时可用（p93 Notes）；
    NTP 建议确认防火墙放行，事后可用 ot-config.sh --ntp 修改。
  conditions: 声明 OT/OXE 前先 nslookup 双向验证
  tags: [checklist, dns, network]

- id: p06
  title: HA 对新装机已不再支持——向导中必须保持 Disable
  type: rule
  source_pages: p94
  source_chapter: OTMS Post-installation wizard / High availability
  source_quote: |
    "HIGH AVAILABILITY IS NOT MORE SUPPORTED FOR A NEW INSTALLATION DON'T ENABLE IT. KEEP DISABLE.
    IT IS ONLY AVAILABLE IN CASE OF MIGRATION OF A SYSTEM FROM RELEASE 2.2.X WITH HA ALREADY DEPLOYED." (p94)
  summary: |
    高可用仅限"从 R2.2.x 带着已部署 HA 迁移上来"的系统继续存在；全新安装一律保持 Disable。
    现场若客户提出 HA 需求，本版本口径下没有可启用的路径（替代方案在书外）。
  conditions: Post-installation wizard HA 页
  tags: [rule, ha, version]

- id: p07
  title: 许可机制原则：FlexLM 校验锚定物；物理机=ALUID、虚拟机=加密狗；OXE 容量仍以本地 .swk 为准
  type: principle
  source_pages: p130-132, p158-159, p162, p165
  source_chapter: Licensing / Licenses files checking
  source_quote: |
    "For a non virtualized deployment, the ice license file is linked to the physical server thank to
    the ALUID controlled by the flex-lm server ... For virtualized deployment, the ice license file is
    linked to a hardware dongle (Aladdin) plugged on the server" (p131)
    "IN OPENTOUCH,ALUID IS THE ELEMENT USED IN CASE OF PHYSICAL SERVER DEPLOYMENT (OTMS, OTMC) TO
    CONTROL THE LICENSE. USB DONGLE IS USED ONLY IN CASE OF VIRTUALIZATION." (p162)
    ""Use Flex license" is not used. In this case, the FlexLM server only validates the Product ID,
    then the CS uses the licenses (total amount of users, trunk groups …) of its ".swk" file stored
    locally." (p159)
  summary: |
    原则三条：(1) 许可校验一律 FlexLM（端口 27000），锚定物按部署形态二选一——物理机用 ALUID（128 位
    硬件标识，getaluid 读取），虚拟化一律 USB 加密狗（lmutil lmhostid -flexid 读 Dongle-ID）；(2) OXE 的
    FlexLM 字段口径：FlexLM Licensing Enabled=Yes、Flex Server Port=27000、ProductID discovery=Yes（虚
    拟产品 ID 场景）、Use Flex License=No——FlexLM 只验 Product ID，用户数/中继组等容量仍以 OXE 本地 .swk
    为准；(3) 8770 的 .sw8770 由 8770 服务器自行控制。
  conditions: OXE 亦可改用 Cloud Connect 控制许可（p130/132 反复标注）
  tags: [principle, licensing, flexlm, aluid, dongle]

- id: p08
  title: 许可文件路径与命名规则：$LICENSES_HOME → final_licenses（含 /oxes），final 文件名按锚定物生成
  type: rule
  source_pages: p144-149, p162, p165
  source_chapter: Licenses files installation / Final licenses file / Licenses files edition
  source_quote: |
    "The licence file is in a first step copied by the post-installation Wizard in: $LICENSES_HOME
    (/var/data/licenses) During Flexlm service startup, the file is copied (and renamed) in:
    $LICENSES_HOME/final_licenses" (p144)
    "ALUID_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_licenses.ice FLEXID_x-xxxxxxxx_license.ice
    SERVERMACADDRESS_<interface1>_license.ice SERVERMACADDRESS_ANY_license.ice" (p148)
    "For internal Flexlm server: $LICENSE_HOME=/var/data/licenses For external Flexlm server:
    $LICENSE_HOME=/opt/Alcatel-Lucent/data/licenses" (p162)
  summary: |
    路径规则：SOT 指定的许可落在 /opt/sot/licenses；向导装入 $LICENSES_HOME（内嵌 FlexLM=/var/data/
    licenses，外部 FlexLM 的服务器侧=/opt/Alcatel-Lucent/data/licenses）；Flexlm 服务启动时复制改名进
    final_licenses（命名含锚定物：ALUID_xxx / FLEXID_x-xxx / SERVERMACADDRESS_<接口> / ANY），OXE 的 .ice
    另进 final_licenses/oxes；手动换许可后必须 service flexlmd stop/start 重启才生效并生成 alchostid.cfg。
    检查命令：service flexlmd status/restart；许可内容用 more 查看并抄录 OTID/Dongle ID/OXE product ID。
  conditions: 新文件须复制进 $LICENSES_HOME 并重启 FlexLM 服务
  tags: [rule, licensing, paths, flexlm]

- id: p09
  title: OXE 许可健康判据：spadmin 三个 PANIC 计数全 0；改 FlexLM 字段后必须重启
  type: rule
  source_pages: p159
  source_chapter: Licenses files checking / Checking the status of the licensing
  source_quote: |
    ""PANIC flag" value must be "0" otherwise it means that the licenses are locked "Panic Flex"
    value must be "0" otherwise it means that the FlexLM server is unreachable "Panic SWK check" means
    that the FlexLM is reachable but the product ID has not been validated" (p159)
    "Warning A REBOOT IS REQUIRED AFTER MODIFICATION." (p159)
  summary: |
    判据：mtcl 登录 OXE 跑 spadmin 选 1（Display current counters）——PANIC Flag=0（否则许可被锁）、
    Panic Flex=0（否则 FlexLM 不可达）、Panic SWK Check=0（否则 FlexLM 可达但 Product ID 未过验）。
    选 2（Display active file）读 Product-Id 与 Handle 4760；Product ID 对应 .ice 文件中的 FEATURE 行。
    在 OXE Webadmin/mgr 的 System/Licenses 改 FlexLM 字段后必须重启 OXE。
  conditions: Flex Server 可填两台（内嵌 192.168.1.50 + 外部 192.168.1.80，实验口径）
  tags: [rule, licensing, troubleshooting, spadmin]

- id: p10
  title: lmutil 命令集与 $FLEXLM_HOME 路径（内嵌/外部两套）
  type: checklist
  source_pages: p162-164, p178-180
  source_chapter: Licenses files checking / External FlexLM deployment / Tools & logs
  source_quote: |
    "For internal Flexlm server: $FLEXLM_HOME=/opt/Alcatel-Lucent/platform/flexlm For external Flexlm
    server: $FLEXLM_HOME=/opt/Alcatel-Lucent/flexlm_standalone" (p162)
    "lmutil lmstat ... lmutil lmstat -a ... lmutil lmhostid ... lmutil lmhostid -flexid" (p162-164)
    "Logs are available in the "/opt/Alcatel-Lucent/logs/flexlm/" directory ... Details on license
    checkout are logged in the file: "/opt/Alcatel-Lucent/logs/flexlm/flexlm_lmlog.log"" (p180)
  summary: |
    工具清单：lmstat（服务是否 UP）、lmstat -a（各 FEATURE 已发/在用量，如 Users of ECCSTART: Total of
    50 issued; 4 in use）、lmstat -a | grep K<产品ID>（OXE 是否占用许可）、lmhostid（FlexLM 服务器 MAC）、
    lmhostid -flexid（加密狗 Dongle-ID）、lmstat 输出的 License server status 端口 27000@主机。路径：内嵌
    FlexLM 的工具在 /opt/Alcatel-Lucent/platform/flexlm，外部 FlexLM 在 /opt/Alcatel-Lucent/
    flexlm_standalone（其下 flexlm/ 目录）；外部 FlexLM 日志在 /opt/Alcatel-Lucent/logs/flexlm/（含
    flexlm_lmlog.log 记录 OXE checkout——一份许可被一台 OXE 占用后其他 OXE 不能再用）。
  conditions: lmutil 兼容Macrovision/Flexera 各版本输出
  tags: [checklist, licensing, lmutil, troubleshooting]

- id: p11
  title: checkLicensing.sh 工具口径：OT 与 Flex 两侧各跑一遍，输出主机信息/许可清单/活动测试/问题计数并打 zip 包
  type: checklist
  source_pages: p178-179
  source_chapter: External FlexLM deployment / Tools & logs
  source_quote: |
    ""checkLicensing.sh" tool can be used to check the license on the OpenTouch and FlexLM servers. It
    will warn you from potential issues." (p178)
    "============= Potential issue(s): 0 ============ ... = /logs/checkLicensing/checkLicensing-
    opentouch-20160307-134033.zip (1002K) can now be downloaded =" (p178)
  summary: |
    排障工具用法：OT 侧与 FlexLM 侧分别执行 checkLicensing.sh；输出四段——Server details（Type/Version/
    Hardware/Flex 指向/HostID/DongleID/ALUID/HA）、Installed licenses（逐文件验 HostID 匹配、到期天数、
    NULL 字符等，逐项 [OK]）、Running deployment and active tests（主机名不同、OT2.0 外部 flex 许可须同时
    部署在 OT 上、FQDN ping、Flex 服务与 ALCFIRM 守护进程等）、Potential issue(s) 计数与日志归档 zip
    （/logs/checkLicensing/）。问题计数 >0 时逐条回看。
  conditions: 归档 zip 可直接提给支持
  tags: [checklist, licensing, troubleshooting]

- id: p12
  title: 外部 FlexLM 部署规则：许可证须含 Dongle ID+OT ID+OXE 产品 ID；仅可 SFTP/SCP 传输；落地后必须移出 /root
  type: rule
  source_pages: p173, p177
  source_chapter: External FlexLM server deployment / Aladdin declaration / License files installation
  source_quote: |
    "License files hosted on external FlexLM server ESXI virtual machine must contain following
    information: Dongle ID OT ID OXE product ID" (p177)
    "For security reasons, the standard FTP protocol cannot be used for the license server. Copy the
    license file with SFTP (Secure FTP), or SCP" (p177)
    "AFTER SFTP TRANSFER THE LICENSE FILES ARE IN "/ROOT" FOLDER. THEY MUST BE COPIED/MOVED TO THE
    DEDICATED LICENSE DIRECTORY." (p177)
  summary: |
    三条规则：(1) 外部 FlexLM 上的许可文件必须包含 Dongle ID、OT ID、OXE product ID 三要素（R-Lab 例外：
    许可锚 MAC 地址，无需加密狗声明）；(2) 传输禁用标准 FTP，只走 SFTP/SCP（root/自定义口令）；(3) SFTP
    落地在 /root，必须再复制/移动到许可目录（/opt/Alcatel-Lucent/data/licenses，如 OTMS.ice/OXE.ice）并
    重启 flexlmd，随后许可进入 final_licenses。虚拟化时先给 FlexLM 虚机挂 USB Device（内嵌 FlexLM 还要先
    挂 USB Controller）；ALE 交付的外部 FlexLM 虚机已默认带 USB 控制器。
  conditions: FlexLM 虚机 OVF 从 My Portal 下载；系统语言保持 CentOS 默认
  tags: [rule, licensing, flexlm, sftp]

- id: p13
  title: 内部→外部 FlexLM 切换：ot-config.sh --external_flex 一条命令，约 5 分钟，随后核服务
  type: rule
  source_pages: p181-185
  source_chapter: Switch from internal to external FlexLM server (How-To)
  source_quote: |
    "You need first to install the external FlexLM server, connect the USB dongle on the external
    FlexLM server and then do the switch." (p182)
    "Enter the command: ot-config.sh --external_flex ... The operation takes about 5 minutes. Verify
    the OpenTouch is running. Start the OpenTouch services if needed checkAll.sh service opentouchd
    restart" (p184-185)
  summary: |
    切换次序：先装好外部 FlexLM 并把加密狗从 OT 虚机解绑、绑到外部 FlexLM 虚机（R-Lab 锚 MAC 时跳过
    加密狗操作）→ OT 上以 root 跑 ot-config.sh --external_flex → 向导填外部 FlexLM 参数（实验口径
    192.168.1.80）→ Finish，约 5 分钟 → 验证：checkAll.sh、必要时 service opentouchd restart。
  conditions: 切换后许可锚定物从 ALUID/MAC 变为 Dongle-ID（见 p42 rehosting 许可条）
  tags: [rule, licensing, flexlm, switch]

- id: p14
  title: OXE 声明前置参数口径：角色地址 csm、节点号=ABC 网络×100+节点号、47xx 同步开、离开 netadmin 必须 APPLY
  type: rule
  source_pages: p186-190
  source_chapter: OmniPCX Enterprise declaration (How-To)
  source_quote: |
    "Name used when the CPU role is main: csm Address used when the CPU role is main: 192.168.1.3" (p187)
    "Subnetwork – Node number Enter a numeric value equal to the ABC network*100 + OmniPCX Enterprise
    node number. Example: With an ABC network number = 1 and node number = 1, you must enter 101" (p190)
    "Validate the directory real-time synchronization (events sending) in order to have automatic
    creation/modification in OmniVista 8770 directory and Users applications. ... 47xx directory –
    4400 Synchro. True" (p188)
    "Warning DON'T FORGET TO APPLY THE MODIFICATION BEFORE TO LEAVE: 20. 'APPLY MOFIFICATION'" (p187)
  summary: |
    四条口径：(1) OXE 双地址——物理名 csa/物理 IP 与主角色名 csm/主 IP（实验 192.168.1.1/192.168.1.3），
    8770 声明填主 IP；(2) 8770 节点号公式：Subnetwork-Node number = ABC 网络号×100 + OXE 节点号（例 101），
    子网号必须等于 OXE 网络号；(3) 打开 47xx directory – 4400 Synchro=True 后 OXE 目录/用户变化实时推
    8770（OXE profile 类变化走实时事件，OT profile 需手动同步）；(4) netadmin -m 修改后必须选 20 APPLY
    MODIFICATION（原文拼错为 MOFIFICATION）再退出。节点/网络号可用 siteid 命令或提示符前缀核验。
  conditions: FTP 凭证 adfexc（口令默认 adfexc）；告警接收模式 Permanent IP connectivity
  tags: [rule, oxe, declaration, netadmin, nmc]

- id: p15
  title: 同步类型矩阵：Complete/Partial × Separate/Global × 从 OXE 或 OT 发起，行为各不相同
  type: metric
  source_pages: p192, p202
  source_chapter: OmniPCX Enterprise declaration / OpenTouch server declaration / Synchronizing
  source_quote: |
    "Partial synchronization includes changes performed since the date of last synchronization for
    entries of the following types: Users, Directory, Data terminals, Speed dial numbers, Remote users." (p191)
    "Partial and complete synchronization are identical for OpenTouch node. (Partial and complete
    synchronization are different for OXE node)" (p202)
    "Global: the selected OXE and associated OpenTouch are synchronized." (p191)
  summary: |
    矩阵口径：从 OXE 发起——Complete/Separate=完整同步所选 OXE；Complete/Global=完整同步 OXE+关联 OT；
    Partial/Separate=部分同步所选 OXE（仅 Users/Directory/Data terminals/Speed dial/Remote users 的增量）；
    Partial/Global=部分同步 OXE + 完整同步 OT。从 OT 发起——Partial 与 Complete 对 OT 本身等价（都是完整）；
    Global 时额外完整同步关联 OXE（若从 OT 发起 Partial+Global 则 OXE 只做部分同步）。实操：声明后先做
    Complete → Separate；OT 档案建完后必须发起同步才能在 8770 Users 应用可见。
  conditions: 上次同步时间在节点 Configuration/Data Collection 的 Date of last modification 查看
  tags: [metric, synchronization, nmc]

- id: p16
  title: OT 节点声明口径：bics.conf 四参数一一对应；节点号用 99 等自由号且不得与 OXE 节点号冲突；必须与 OXE 同子网
  type: rule
  source_pages: p194-197
  source_chapter: OpenTouch server declaration (How-To)
  source_quote: |
    "ICE_USERNAME="otAdmin" Used by 8770 Configuration application to configure the OpenTouch server.
    ICE_TEMPLATEUSERNAME="otProfile" Used by 8770 server to retrieve and manage user profiles on
    OpenTouch ICE_MAINTENANCEUSERNAME="otuser" Used by 8770 Maintenance application for OpenTouch
    backup and restore operations. Also used to access the OpenTouch via SSH." (p194)
    "Node number is a free number. This node number must be different than OXE node numbers existing
    in the OXE network. (Use 99 for example)." (p196)
    "OpenTouch server must be declared in the same sub-network than the OXE call server." (p196)
  summary: |
    对应关系：FQDN=HOST_NAME.HOST_DOMAIN；配置账号=ICE_USERNAME(otAdmin)；Connectivity 页模板账号=
    ICE_TEMPLATEUSERNAME(otProfile)；Maintenance 页=ICE_MAINTENANCEUSERNAME/PASSWORD(otuser，兼 SSH 与
    备份恢复)。节点号取自由号（示例 99），不得撞 OXE 节点号；声明位置必须与 OXE 呼叫服务器同一子网。
    密码找回：otAdmin/otProfile 可经 WBM（System services/Security/Administrator）互相改 GUI 口令；
    otuser 是 Linux 账号，用 passwd otuser 重置。
  conditions: DNS 正反向解析前置核查（见 p05）
  tags: [rule, ot-declaration, bics-conf, accounts]

- id: p17
  title: OT 侧挂 OXE 的固定参数：PRS 端口 2570、FTP adfexc、Codec 必须与呼叫服务器一致
  type: rule
  source_pages: p199-201
  source_chapter: OpenTouch server declaration / Declaring the OXE in the OpenTouch topology
  source_quote: |
    "Port 2570 (OXE PRS port number) FTP User name adfexc FTP password adfexc Enable notification
    Selected HTTP Mode Default ... PRS Select "Presentation Service – opentouch"" (p201)
    "Codec Select the compression algorithm used for inter domain calls: This parameter must be the
    same as the one declared on the Call Server: System > Others System Param. > Compression
    Parameters" (p201)
  summary: |
    OT 拓扑里 OXE CS 对象的固定口径：端口 2570（OXE PRS）、FTP 账号 adfexc/adfexc、启用通知、HTTP Mode
    默认、Node Identifier=OXE 节点号、PRS 选 Presentation Service – opentouch；CAC IP link 页的 Codec
    （实验 G729）必须与 OXE 呼叫服务器的压缩参数一致——两边不一致会造成跨域呼叫编协商问题。
  conditions: 网络/子网命名沿用 8770 侧定义（Logical-network=1、ABC-subnetwork=1，实验口径）
  tags: [rule, topology, codec, prs]

- id: p18
  title: SNMP 告警对接数值：agent 161 / server 162、v3+SHA+AES128+Inform、trap 过滤三档、ams 由 omp 控制
  type: metric
  source_pages: p205-209
  source_chapter: Alarms - OpenTouch (How-To)
  source_quote: |
    "SNMP Agent port 161. The SNMP agent receives requests on UDP port 161." (p205)
    "Port 162 The SNMP server receives notification (Inform request) on port 162. Trap transmission
    filter ... NO_FILTER sends all alarms MAJOR ALARMS ... CRITICAL ALARMS" (p207)
    "SNMP authentication protocol SHA SNMP encryption protocol AES 128 SNMP security level V3
    authentication: privacy" (p208)
  summary: |
    数值口径：OT SNMP agent 收请求 UDP 161；8770 SNMP server 收 Inform 162；SNMP v3 认证 SHA、加密
    AES 128、安全级 auth-privacy；trap 过滤 NO_FILTER（全发）/MAJOR（≥major）/CRITICAL（≥critical）；
    通知类型 Inform。OT 侧用户/认证口令/加密口令均 ≥8 字符（实验 AdminSNMP/adminsnmp）。引擎 ID = 系统
    Engine ID + Custom data engine ID（默认节点名）自动拼接。8770 侧配置落盘
    c:\\8770\\data\\config\\netsnmp\\snmptrapd.conf。改 SNMP 配置后 OT 侧 service ompd stop/start（含 ams）。
  conditions: MIB 首次下载不全需手动重载（删 C:\\8770\\data\\config\\ICE → 重启 NMC Alarm Server → 重启 ompd）
  tags: [metric, snmp, alarms, ports]

- id: p19
  title: 编解码兼容矩阵：OXE 呼叫服务器 G711/G723/G729；ESS 不支持 G723；OT-OXE 间 Codec 两端一致
  type: rule
  source_pages: p218, p201, p233
  source_chapter: System prior management / Compression algorithm / OXE SIP configuration
  source_quote: |
    "OXE call server is compatible with the following algorithms: G711, G723, G729 Enterprise SIP
    Server (ESS) is compatible with the following algorithms: G711, G722, G722.2, G729 Not compatible
    with G723" (p218)
    "Compression type G 729 Multi. Algorithms for Compression False" (p233)
  summary: |
    矩阵：OXE 呼叫服务器支持 G711/G723/G729；ESS（OT 的 SIP 服务器）支持 G711/G722/G722.2/G729、明确
    不兼容 G723——跨 OT/OXE 的呼叫编解码要避开 G723。OXE 侧落地：System/Other System Param./Compression
    Parameters 设 Compression type=G729、Multi. Algorithms=False；OT 侧 OXE CS 对象的 Codec 必须与呼叫
    服务器同值（G729）。
  conditions: AMS 支持语音 G711/G729/G722、视频 H264（p7），是媒体面另一层
  tags: [rule, codec, sip]

- id: p20
  title: 号码段规则：31000-31499 整段在 OT 侧声明归属 OXE；范围建在 OXE 声明级 Ranges 页签
  type: rule
  source_pages: p216-217, p237
  source_chapter: System prior management / Numbers range / Prior management / Ranges of numbers
  source_quote: |
    "Range of numbers from 31000 to 31499 (including users, voice mail, attendants, …) are declared
    belonging to OXE. Numbers from 31000 to 31499 are declared on OXE as users, voice mail,
    attendants …" (p216)
    "On the OpenTouch SIP Server (ESS), a range defines dialing numbers which are processed in the
    OmniPCX Enterprise server. Ranges include: All OmniPCX Enterprise server user numbers ... Direct
    abbreviated numbers Attendant numbers" (p237)
    "OpenTouch users can be included in a range Several ranges can be declared" (p237)
  summary: |
    规则：OT 侧的号段决定"这些号去 OXE 处理"——须覆盖 OXE 全部用户号、留言号（UM/本地）、缩位号、话务台
    号等；入口在 OT 配置 System services/Topology/OXE CS/…/<OXE> 的 Ranges 页签（Number min/max，右键
    Add）。OT 自己的用户号也可放进某号段；可声明多个号段。实验口径 31000-31499（DDI 翻译：首外线
    33210N41000、首内线 31000、跨度 500，N=POD 号）。
  conditions: 外部语音邮件 31200→GW2(5040)、会议 31250/31260→GW1(5260) 的指向另见 f15
  tags: [rule, numbering, ranges]

- id: p21
  title: 前缀服务口径：转发/溢出/话务台前缀两侧同值；法国默认 51/52/53/54/41/9；OT R2.1 后话务台前缀必配并重启 wireald
  type: rule
  source_pages: p238-239
  source_chapter: Prior management / Prefix services
  source_quote: |
    "On SIP Server, the forwarding application, as the attendant call, works with prefixes. These
    prefixes must be configured. On OmniPCX Enterprise server, prefixes with the same purpose exist.
    It is recommended to enter the same values on both servers." (p238)
    "Example: Immediate forward (for routing management): 51 Forward on busy activation: 52 Forward
    on no answer activation: 53 Forward on busy or no answer activation: 54 Cancel forwarding: 41
    Attendant prefix: 9 These default values are for a French OXE, please check your current OXE
    configuration" (p238)
    "AFTER OT R2.1, CONFIGURATION OF THE ATENDANT PREFIX IS MANDATORY FOR THE START UP OF THE
    EXTENSIBLE SERVICES. IF NOT YET CONFIGURED, ACCESS THE OPENTOUCH CONFIGURATION TOOL TO DECLARE THE
    ATTENDANT PREFIX THEN RESTART THE EXTENSIBLE SERVICES BY USING THE FOLLOWING COMMAND (USING ROOT
    LOGIN): > SERVICE WIREALD RESTART" (p238)
  summary: |
    口径：OT 的 Telephone Prefixes 页（System Services/Applications/Telephony/Telephone Prefixes）要配
    溢出忙/无应答/无应答或忙/取消、路由管理（立即前转，同 OXE 立即前转值）、Join or leave group（监督组
    进出前缀）、CLIR、话务台前缀（只能呼 OXE 侧话务台，可多条）；推荐与 OXE 同名前缀同值。硬规则：OT R2.1
    之后话务台前缀必须配置，否则可扩展服务起不来——配置后以 root 执行 service wireald restart。
  conditions: 法国默认值仅为示例，须核对现场 OXE 前缀表
  tags: [rule, prefixes, telephony]

- id: p22
  title: 拨号规则行为：按名呼打全客户端自动加外呼前缀；按号呼打仅 OTC PC/Mobile；话机与视频终端须手拨；最小长度=拨号计划+1
  type: rule
  source_pages: p220-222, p242
  source_chapter: System prior management / Dialing rule / Prior management / Dialing Rules
  source_quote: |
    "« call by name » feature In that case, dialing rule is involved, whatever the client performing
    the outgoing call (external prefix is added automatically) OTC PC, OTC Mobile, Deskphones" (p221)
    "« call by number » feature In that case, dialing rule is involved only for the following clients
    (no need to dial the external prefix) OTC Mobile, OTC PC Specific file (containing dialing rule
    configuration) is downloaded at client level Calls through Deskphones and video equipments must be
    performed by dialing the external prefix manually" (p221)
    "Minimum length The dialing external prefix will only be added to numbers which length is upper or
    equal to the specified value Enter your dialing plan length +1" (p242)
  summary: |
    规则：OT 的 Dialing Rule（System services/Applications/Telephony settings/Dialing rule/dialingRule 1）
    自动给外呼加前缀。行为分层：按姓名呼打——所有客户端（OTC PC/Mobile/话机）都自动加；按号码呼打——仅
    OTC PC 与 OTC Mobile（客户端侧下载规则文件），话机与视频设备必须手拨前缀；会议呼叫走 DAS Rules（p221
    注）。参数：外呼前缀 0 或 9（按国家）、Minimum length=拨号计划长度+1、Exception length=不加前缀的号码
    长度。
  conditions: 实验示例 Minimum length 7 / Exception 0（p220 图示口径）
  tags: [rule, dialing-rules, routing]

- id: p23
  title: UDAS 同步硬规则：同步日期/时间/周期必须设置；周期 ≥1（1=每天），绝不能为 0；检索只打同步库
  type: rule
  source_pages: p223-224, p243-245
  source_chapter: System prior management / UDAS synchronization / Prior management / UDAS directories Synchronization
  source_quote: |
    "All the search are made in the synchronized database (synchronized directories) and not directly
    in the declared directories storages" (p223)
    "SYNCHRONIZATION DATE, TIME AND PERIOD MUST BE SET. SYNCHRONIZATION PERIOD MUST BE EQUAL OR UPPER
    TO 1. 1 MEANS SYNCHRONIZATION EVERY DAY AT DECLARED TIME 2 MEANS EVERY 2 DAYS ETC … NEVER SET
    PERIOD TO "0"" (p243)
  summary: |
    机制：UDAS 把三路数据源——OTS（OXE 话簿）、内部目录（ESS 用户）、外部 LDAP（8770 等）——单向倾倒进
    OT 上 PostgreSQL 的同步库（LDAP sync / Internaldir sync / Phonebookdir 表），客户端检索只查同步库。
    配置硬规则：internalDir 与 phonebookDir 两目录的同步页签必须设日期（yyyy-mm-dd）、时间（hh:mm:ss）、
    周期（天数，≥1，0 禁止）；"done by merge" 勾选后按合并周期自动先同步；Force synchronization 为手动
    立即同步。
  conditions: 默认两目录 internalDir=OT 目录、phonebookDir=OXE 话簿
  tags: [rule, udas, directory, sync]

- id: p24
  title: 会议桥号码口径：TUI application 每语言一条（实验 31250 英/31260 法）；OXE 侧对应 External Voice Mail 走网关 10；SIP proxy 用户自动生成
  type: rule
  source_pages: p246-248, p252
  source_chapter: Prior management / ACS Configuration
  source_quote: |
    "It is possible to create several "conferencing" number (1 number per language) To create another
    number for conference bridge (associated to a different language), it is required to create a new
    "TUI application"" (p247)
    "All SIP Proxies settings are filled in automatically after the post installation wizard. You will
    only have to check that all values are correctly set up." (p252)
  summary: |
    口径：OT 侧 System services/Applications/Telephony settings/Vocal applications/TUI application 建
    Conferencing 类型号码（实验 31250 英/31260 法），字段含 Collaboration organization（默认 DEFAULT）、
    语言、邮件邀请开关与标签、Dial in number（外部 DDI）；OXE 侧 Applications/External Voice Mail 按同号建
    两条走外部网关 10（到 OT SIP server 5260）。会议服务器管理台（WBM otAdmin → Users and devices/
    Conference server）核 System options（国际 00/国内 0/国码 33/Smart mail relay host）与 SIP Proxies
    （默认出站代理=OT IP:5260，realm=OT FQDN，用户 31700/31710 为 TUI 会议号自动生成）。
  conditions: OXE 侧第二条会议桥（另一语言）需再建一条 External Voice Mail
  tags: [rule, conference, acs, tui]

- id: p25
  title: DAS rules 强制且按国家定制；法国口径十条；声明顺序重要、多条可同时命中
  type: rule
  source_pages: p253
  source_chapter: Prior management / DAS rules configuration
  source_quote: |
    "The call routing rules, called DAS rules, are applied to the user's dialed digits Note that the
    dialing rules are linked to a domain DAS rules are mandatory and are country dependant. The
    configuration proposed will be for France." (p253)
    "WARNING THE DECLARATION ORDER IS IMPORTANT. SEVERAL RULES CAN BE APLLIED AT A TIME (EXAMPLE :
    RULE 1 AND 2, 4 AND 6 …)" (p253)
  summary: |
    十条法国口径（会议服务器 Advanced settings/Edit DAS Rules，Default 域）：R1 s/^\\+(\\d{3,6})$/+x\\1/
    （内部号缺 x 补 x）；R2 s/^\\+x//（放行内部呼叫）；R3 s/^\\+00/+/；R4 s/^\\+0/+33/；R5 s/^\\+330/00/；
    R6 s/^\\+33/00/（放行国内）；R7 s/^\\+N/N/（nomadic）；R8 s/^\\+M/M/（手机/OTC PC/外部号）；R9 s/^\\+V/V/
    （视频）；R10 s/^\\+/000/（放行国际）。规则与域名绑定；顺序敏感；多条可同时生效（如 1+2、4+6）。
  conditions: 各国需按本国拨号计划改写
  tags: [rule, das, conference, regex]

- id: p26
  title: 电话号码格式化规则：Extension Pattern 正则须与拨号计划位数匹配（5 位计划 /^\s*\+*[xX]?(\d{3,5})\s*$/）
  type: rule
  source_pages: p254
  source_chapter: Prior management / Configure phone formatting rules
  source_quote: |
    "Extension Pattern /^\\s*\\+*[xX]?(\\d{3,5})\\s*$/ for a 5 digits length dialing plan (second digit
    in the regular expression)" (p254)
    "These settings are intended to allow extension dialing and customize the formatting of phone
    numbers. It is also used for creation of the device(s) with auto-provisioning on Conference server
    side." (p254)
  summary: |
    规则：会议服务器 Phone Formatting Rules 的 Extension Pattern 正则（分机位数的第二处数字）必须与现场
    拨号计划一致；它同时用于分机拨号识别与会议服务器侧自动开通设备时的号码格式判定。改拨号计划位数时
    同步改正则。
  conditions: 位于会议服务器管理台 Advanced Settings
  tags: [rule, formatting, regex, conference]

- id: p27
  title: 档案权限边界：Users 应用只能改档案；建/删必须回 OXE 或 OT 配置工具；OXE 档案实时同步、OT 档案要手动同步
  type: rule
  source_pages: p265-266, p275-278, p297
  source_chapter: Users application / User profiles creation / Web Provisioning Client
  source_quote: |
    "Created thanks to OmniPCX Enterprise configuration tool It's a user with the "Set function"
    parameter set to "Profile" Useful to give a directory number starting with A,B,C or D (e.g. A1000)" (p265)
    "Only profile modification is allowed via Users application. Creation and deletion must be done
    via OXE or OpenTouch configuration application" (p278)
    "If some OXE profiles need to be created, they will be automatically displayed on Users
    application. After OpenTouch profiles creation, a complete synchronization is required to make them
    displayed on Users application." (p297)
  summary: |
    规则：(1) OXE 档案=Set function=Profile 的特殊用户，目录号可用 A0000 式字母占号省号段，Profile Name
    必须大写；前置开启 Use profile with auto. recognition；(2) OT 档案在 Users and devices/User/Profile
    建，Category 必须选 ACU-OXE；(3) 同步行为不对称——OXE 档案靠实时事件直达 8770，OT 档案建完必须做一次
    完整同步才在 Users 应用出现；(4) Users 应用只开放"修改"，新建/删除必须回两侧配置工具。
  conditions: 档案可继承的默认属性清单见 p274（Cost Center、各类 COS、话机特性等）
  tags: [rule, profiles, users, sync]

- id: p28
  title: 用户口令策略：GUI 字母数字；TUI 6 位纯数字且拒绝顺序数列；SIP 口令仅 SIP 分机需要——实验放宽属例外
  type: rule
  source_pages: p281, p284, p286
  source_chapter: Users creation (How-To)
  source_quote: |
    "GUI Password ... Available characters are letters of the alphabet or digits" (p285)
    "TUI password ... Available characters are digits (6 digits minimum). Passwords composed of a
    logical series of digits (for example: 12345, 65432 or 13579) are refused by default." (p286)
    ""PASSWORD MINIMUM LENGTH": 5 (DEFAULT: 6 CHARACTERS) "ALLOW TRIVIAL TUI PASSWORD": CHECKED
    (DEFAULT: UNCHECKED) ... THESE MODIFICATIONS ARE DONE HERE FOR A LAB CONTEXT AND ARE NOT RECOMMANDED
    AT ALL ON SITE." (p284, p281)
  summary: |
    默认策略：GUI 口令字母/数字；TUI 口令至少 6 位纯数字，12345/65432/13579 之类顺序数列默认被拒；SIP 口令
    只在 Device type=SIP extension 时需要。实验放宽口径（System services/Security/Password management）：
    密码最小长度 5（默认 6）、允许 trivial GUI/TUI/SIP 口令——教材两处强调仅限 LAB，现场绝不建议。
  conditions: OT 侧 SIP 口令留空则自动生成（软电话场景 p471）
  tags: [rule, security, passwords, users]

- id: p29
  title: Web Provisioning Client 约束：8770 3.2.8+ 且 Unified management 许可；仅 Chrome ≥54；不能建 Conversation 用户；一台设备
  type: rule
  source_pages: p290, p292-294
  source_chapter: Web Provisioning Client (讲义)
  source_quote: |
    "Available from OmniVista 8770 3.2.8 with Unified management license Web client: 0 footprint" (p290)
    "Only support of Chrome versions from 54 Restrictions: Management of profiles from OXE/OT
    Configuration • No creation of new OpenTouch Conversation users • Association of one device" (p292)
  summary: |
    约束清单：版本门槛 OmniVista 8770 3.2.8 + Unified management 许可；浏览器只支持 Chrome 54+；能力=同质
    模式下 OXE/OTCt 用户的 MACD、最小参数集+档案、多 OXE/OT 实例、按角色控权；限制=档案仍回 OXE/OT 配置
    工具管、不能新建 OpenTouch Conversation 用户、只关联一台设备。入口 URL：https://<8770 FQDN>（或
    /nmclient、:8443/nmclient 直达登录页）。
  conditions: 对 OT 用户称呼字段强制（Salutation mandatory for a user with OpenTouch rights）
  tags: [rule, wpc, provisioning, constraints]

- id: p30
  title: 语音邮箱档案默认面：LS 三档案（Advanced/Classic/Simplified）+ UM Standard；四页签逐项口径
  type: checklist
  source_pages: p338-343
  source_chapter: Voice mailbox profiles (How-To)
  source_quote: |
    "Profiles called "Advanced", "Classic" and "Simplified", dedicated to Local Storage. "Standard"
    profile is dedicated to Unified Messaging." (p339)
    "Answer only • Yes: callers cannot leave messages ... • Manageable by users (default value): users
    can authorize or forbid callers from leaving messages" (p340)
    "TUI password management Select the appropriate option: TUI password change allowed / TUI password
    change allowed but forbidden when expired / TUI password change forbidden" (p341)
  summary: |
    配置清单（Advanced 为例）：Configuration 1——Answer only 三态（默认 Manageable by users）、Check quota、
    Announce time received、Skip memo、Direct callback（直按 2 回呼）、Callback voice prompt、Limited
    access（防恶意问候录音）、Extended absence 阻止留言、Record invitation、Keep call in system、Callback
    sender allowed、Propose options after message deposit、录音提示音、Attendant call enabled（零出）；
    Configuration 2——最大问候/留言/现场录音秒数、TUI 口令管理三档；Configuration 3——每箱 MB 配额（需 Check
    quota 启用）、新留言/已听留言保留天数、口令到期预警、可网络化、可 IMAP。
  conditions: 新建 LS 型档案可完全自定（实验 my_profile：10MB/5s/15s/15s/15 天/7 天）
  tags: [checklist, voice-mail-profile]

- id: p31
  title: IMAP 数值口径：内嵌服务器 1000 并发封顶、1001-20000 需专用服务器；留言 G711 编码；默认 IMAPS+TLS
  type: metric
  source_pages: p313, p351
  source_chapter: Voice mail / IMAP4 / IMAP How-To
  source_quote: |
    "Up to 1 000 simultaneous sessions (with embedded IMAP server) For 1 001 up to 20 000 simultaneous
    sessions, a dedicated server is required" (p313)
    "Messages are encoded in G.711 Compatible with any IMAP client" (p313)
    "BY DEFAULT, IMAPS IS ENABLED ON OPENTOUCH SIDE WITH "TLS" SECURITY. ... IF YOU WANT TO ENABLE IMAP
    PROTOCOL WITH "SSL" SECURITY OR IMAP PROCOTOL WITHOUT ANY SECURITY, YOU WILL HAVE TO MODIFY THE
    PORT NUMBER ON OPENTOUCH SIDE ... DON'T FORGET TO RESTART THE IMAP FRONT-END SERVICE: service
    imap4fed restart" (p351)
  summary: |
    数值：内嵌 IMAP 前端最多 1000 并发会话；1001-20000 会话须专用服务器；消息 G711 编码兼容任意 IMAP
    客户端；IMAP 访问权由档案（Accessible via IMAP）与管理员授予；安全支持 IMAP over TLS/SSL；OT 侧默认
    IMAPS+TLS，改 SSL/明文须同步改端口并 service imap4fed restart。
  conditions: 消息未压缩 wav 存储（p304），IMAP 侧编码 G711
  tags: [metric, imap, capacity, security]

- id: p32
  title: SMTP 通知约束：OT 无内置 SMTP；外部服务器须无认证无 TLS；发件账号必须真实存在；失败告警仅覆盖"未达 SMTP"
  type: rule
  source_pages: p358-360, p370
  source_chapter: SMTP/SMS notification (讲义) / How-To
  source_quote: |
    "Notifications are sent through an external SMTP server. There is no SMTP server in the OpenTouch
    solution. This server must be used without authentication and without TLS." (p360)
    "The "notification sender mail address" should be valid on SMTP server (existing account)" (p370)
    "An SMTP notification of non delivery is delivered in the mailbox of the valid e-mail account and
    there is no other notification of sending failure An OpenTouch alarm is generated only when the
    operation of sending mail failed before reaching the SMTP server." (p360)
  summary: |
    规则：通知一律走外部 SMTP（OT 不内置）；该服务器必须无认证、无 TLS；发件人地址必须是 SMTP 上真实存在
    的账号；投递失败（NDN）只落在发件账号邮箱，OT 侧仅在"邮件根本没到 SMTP"时产告警（并转 SNMP trap）。
    全局参数：发件名/地址、SMS 网关地址、附件上限（实验 2MB，线性 PCM 8bits 口径）、近满阈值（默认 80%）、
    音频格式（AAC/PCM16/PCM8/G711 wav）；SMTP 路由经 VPIM 会话声明（域、FQDN/IP、端口 25）。
  conditions: wav 附件/箱满通知/My Messaging 链接/回呼仅 Local Storage（p366 表）
  tags: [rule, smtp, notification]

- id: p33
  title: SMS 通知口径：仅一个 SMTP-SMS 网关；地址格式 SMS$号码$@域名；模板按 GUI 语言
  type: rule
  source_pages: p362-364, p368, p370
  source_chapter: SMS notification (讲义) / How-To
  source_quote: |
    "An SMS gateway is required for SMS notifications. ... Only one SMS Gateway can be configured in
    the system" (p363)
    "SMS gateway address Enter the SMS gateway address, e.g. SMS$xxxxx$@company.com where "xxxxx" will
    be the phone number where to notifiy the user" (p370)
    "Default bodies for the SMS are defined in different languages in template files available in the
    directory: "/var/data/panda"" (p364)
  summary: |
    口径：SMS 通知=OT 发邮件给 SMTP-SMS 网关（负责格式化并下发）；系统只能配一个网关；全局地址格式
    SMS$<手机号>$@company.com；通知内容模板在 /var/data/panda/notification4（NotifTemplate_xx.properties），
    语言跟用户 GUI 语言；用户侧可选手机型（工作机/个人机/自由号码）。升级不覆盖已存在的模板文件（见 n 条目）。
  conditions: SMS 通知 Local Storage 与 UM 均可用（p366 表）
  tags: [rule, sms, notification]

- id: p34
  title: 通用公告硬限制：一次仅一条、新录覆盖、最长 5 分钟、wav 格式 CCITT A-law 8kHz 单声道、固定文件名
  type: metric
  source_pages: p392, p396
  source_chapter: General announcement / Conclusion / WAV file
  source_quote: |
    "Only one general announcement can be recorded at a time. Any new recording will overwrite the
    previous one. Max duration: 5 minutes" (p392)
    "If a wav file is used, it is stored under: /var/data/general_announcement The name must be
    "general_announcement.wav" Format: CCITT A-law 8bits 8kHz mono" (p392)
    "Suse console /var/ data/ ics-group/general_announcement" (p396)
  summary: |
    硬限制四条：同时只能存在一条通用公告；再次录音/上传即覆盖；最长 5 分钟；wav 文件格式固定 CCITT A-law
    8bits 8kHz mono、文件名必须 general_announcement.wav。存放路径两处表述：讲义 /var/data/general_
    announcement，How-To 实操 /var/data/ics-group/general_announcement（生产以实测系统目录为准）。wav 就位
    即启用；停用=删文件或 TUI 菜单停用。
  conditions: 功能仅对使用 wav 文件的语言可用
  tags: [metric, general-announcement, limits]

- id: p35
  title: 问候语规则：标准/个人/延长缺席/备选（最多 2 条且需管理员授权）；管理员可批量上传专业 wav
  type: rule
  source_pages: p308-311, p333, p335
  source_chapter: Voice mail System services / Voice mailbox configuration
  source_quote: |
    "Available types of greetings: Standard greeting Subscriber name or extension number Personal
    greeting ... Absence greeting ... Alternative personal greetings (2 max)" (p308)
    "A user can activate a maximum of 2 alternative greetings, only when the administrator has granted
    you the rights to use them." (p333)
    "Number of greeting managers is not limited" (p334)
  summary: |
    规则：问候类型=标准（姓名或分机号）、个人（内外线可不同）、延长缺席（长期外出，可禁留言）、备选个人
    （最多 2 条，需管理员在档案/邮箱侧授权，用于会议/午休等场景快速切换）。录制：用户 TUI/GUI 或管理员
    上传专业 wav；激活：用户 TUI/GUI/My Profile 或管理员 Web 界面。问候语管理器（WBM → Voice mail
    greetings management）数量无上限，可按用户上传/激活/下载/删除。OTC 客户端支持面：OTC PC 与 OTC Android
    可管问候、OTC PC One/OTC iPhone 不可（p310 表）。
  conditions: 问候细节另见 Quick Reference Guide（p333 引用）
  tags: [rule, greetings, voice-mail]

- id: p36
  title: 多终端规则：最多 5 设备；主/副设备类型白名单；远端分机仅 1、DECT 仅 1；VoIP 不冻结话机
  type: rule
  source_pages: p438-439, p485-486
  source_chapter: OTC PC / Multi-devices (讲义+How-To)
  source_quote: |
    "Up to 5 devices with following rules: Main device can be: NOE IP, NOE TDM, IPDSP, SIP(SEPLOS),
    desk sharing (DSU), an OTC PC (PC/Mac) (on SEPLOS) Secondary devices can be: NOE IP, NOE TDM, DECT,
    MIPT, IPDSP, SIP (SEPLOS), REX, an OTC PC (PC/Mac) (on SEPLOS), an OTC Smartphone ... Only one
    remote extension Only one DECT" (p439)
    "Voice over IP on OTC PC is available without freezing the desk phone device (main set) Note:
    Former solution based on Nomadic also supported" (p439)
    "Manage the ringing on secondary devices parameter. ... Ring all Secondary if Main Out of Service
    Yes" (p485)
  summary: |
    规则：一名 Connection 用户最多 5 台设备；主设备白名单 NOE IP/TDM、IPDSP、SIP(SEPLOS)、DSU 话机共享、
    OTC PC（SEPLOS）；副设备另可 DECT、MIPT、REX、OTC 手机；远端分机（REX 类）与 DECT 各限一台；OTC PC 与
    OTC 手机可共存于一套多终端；OTC PC 走 VoIP 不再冻结话机（旧 Nomadic 方式仍支持）；任意设备拨出/接听/
    移会话。前置配置：用户 Phone features COS 勾 Ring all Secondary if Main Out of Service=Yes；建 Twinset
    get call 与 No ringing 两前缀（实验 506/507）并在 COS 授权。
  conditions: 软电话第二设备方案禁授 Nomadic SIP 权（p474/p492：Nomadic SIP 不勾、Desktop 勾）
  tags: [rule, multi-devices, devices, licensing]

- id: p37
  title: OTC PC One（免费模式）能力边界：无 VoIP、单线盲通话、无监督、共享仅 viewer、三个静态路由档
  type: metric
  source_pages: p448-458
  source_chapter: OTC PC One (讲义)
  source_quote: |
    "OTC PC starts in a "freemium mode" Without universal client option: Desktop right unchecked
    Reduced level of service Used for test, "try and buy"" (p448)
    "Blank call: no call monitoring No conversation card (i.e. no window session) The only possible
    action during an active call is to release the call ... No possibility to launch a second call if
    there is already an established call on the main device (application is mono-line)" (p455)
    "Three static routing profiles: Deskphone Home phone Other number (Nomadic GSM) Immediate forward
    on voicemail" (p453)
  summary: |
    边界清单：同一二进制、无 Desktop 许可即落 One；仅垂直单列显示；Settings 去掉 Audio/Video/Overflow 页与
    QR 码；号码簿仅 business+mobile；路由=三个静态档（话机/家庭电话/其他号码）+立即转留言；可视留言不可用
    但有未听数图标（点击进 TUI）；状态短语不显示；联系人卡仅 Start IM 与 Make audio call；RCC 盲通话（无会
    话卡、只能挂断、单线、不能二次外呼）；来话不能接只能挂；无监督；IM 不能加参与者、不能发起共享（可
    viewer 看共享）、无多媒体联动；预约会议持 Conferencing 选项可管理但入会不带全媒体。按许可解锁扩展：
    Outlook 会议插件（+Conferencing）、Office 集成/Skype 集成（+Universal client）；升级只需加 Universal
    许可（带桌面集成再重跑 setup 部署扩展）。
  conditions: 免费模式面向全员画像（Profiles: Entire staff），全量版面向 Power users
  tags: [metric, otc-pc-one, licensing, limits]

- id: p38
  title: 监督组规格：500 组上限、40 人/组、监督链 4000（500-1500 用户系统）/6000（3000-5000 用户系统）；一人一组、同 OT 节点
  type: metric
  source_pages: p497, p500, p507
  source_chapter: Supervision groups (讲义)
  source_quote: |
    "Up to 500 supervision groups Up to 40 supervised users per group OTC PC can display up to 40
    Supervised users on the screen Supervision links * With a server capacity between 500 and 1500
    users : up to 4000 supervision links With a server capacity between 3000 and 5000 users : up to
    6000 supervision links" (p507)
    "40 members maximum per group" (p497)
    "An user can only be declared in one group Group members may be declared on different OXE nodes
    but must be attached to the same OT node (no multi OT)" (p500)
  summary: |
    硬规格：每组 2-40 名同类型成员（监督员+被监督合计）；每用户只能属于一个组；组成员可跨 OXE 节点但必须
    挂同一 OT 节点（不支持多 OT）；系统级 500 组上限；监督链上限按服务器容量档——500-1500 用户系统 4000
    条、3000-5000 用户系统 6000 条（更细 provisioning 见 Features list & Product limits）；OTC PC 一屏最多
    40 人。功能本身无专用许可（p498）。
  conditions: 与 OXE 话机监督键是两套机制、无同步（p501）；OTC PC One 不支持监督
  tags: [metric, supervision, capacity, limits]

- id: p39
  title: 备份机制数值：自动备份每日 00:01（周日全量/其余增量）；/var/backup/daily 命名 fqdn.yyyy-mm-dd-hh-mm.zip；OT-V 必须 NFS
  type: metric
  source_pages: p535-546, p552, p555-556
  source_chapter: Backup and Restore (讲义 + How-To)
  source_quote: |
    "Automatic backup done every day at 00:01 Full backup on Sunday Incremental backup on other days
    Saved in "/var/backup/daily" folder and named "fqdn.yyyy-mm-dd-hh-mm.zip"" (p541)
    "In case of OT-v, the complete "/var/backup" working folder itself is not created locally and has
    to be mounted on external NFS server." (p555)
    "IT DOESN'T MAKE SENSE TO USE USB OPTION IN CASE OF VIRTUALIZATION." (p556)
  summary: |
    数值与结构：OT 数据库备份覆盖 ICAS（库+语音消息）、SIP SRV、ACS 三组件；自动备份每日 00:01，周日全量、
    其余增量，落 /var/backup/daily（名 fqdn.yyyy-mm-dd-hh-mm.zip）；手动用 otbr.sh backup|restore host|moh
    （OTMS 中 appliall 等价 host），产物走 /var/backup/bics；/var/backup 子目录 acs_tar/ACSBackup/Bics/
    daily/on_demand/tmp。前置 ot-config.sh --storage 选本地/USB/NFS（USB 须 FAT32/NTFS/EXT3 并用
    prepareUsbdisk -f 格式化）；OT-V 场景 /var/backup 整体挂 NFS（bics 最终目录可单独挂点）、USB 无意义；
    若本地无 /var/backup 且未挂 NFS，8770 发起的 OT 备份不工作。
  conditions: OXE 用 swinst（/DHS3dyn/BACKUP/IMMED：mao-dat 配置/mao-acc 计费），恢复前先停话务、恢复后 RUNTEL；8770 用 8770 Maintenance（C:\\8770_ARC）
  tags: [metric, backup, otbr, nfs]

- id: p40
  title: rehosting 命令族与硬约束：ot-config.sh --rehost（隐藏 --suspend 换子网）；约 25 分钟；死锁不可回退；inactive 分区被清
  type: rule
  source_pages: p560-566, p569-572, p586
  source_chapter: Re-hosting (讲义) / OTMS rehosting (How-To) / TC2149
  source_quote: |
    "Performing the re-hosting process with the wrong configuration (hostnames not declared, IP
    address already used etc...) will result in a deadlock situation. As the machines cannot be
    reached, the re-hosting cannot be played afterwards. Therefore, it is not possible to fall back to
    the previous configuration." (p565)
    "Performing the re-hosting process makes the current inactive partition incompatible ... Therefore,
    the content of the inactive partition will be suppressed and deleted Rollback or update to the
    inactive partition will NOT be allowed." (p566)
    "After around 25 minutes (with the lab configuration), rehosting is completed" (p572)
    "--rehost –suspend (1) rehost the system and suspend operation in order to move the servers in
    another place (ex subnet modification)" (p586)
  summary: |
    规则：rehosting 用 ot-config.sh --rehost（与 post-install 同款向导，改 OT 的 IP/主机名/FQDN/DNS/
    License server；TC2149 另载 --ntp、--external_flex 等兄弟选项；--suspend 为隐藏选项：先在旧环境挂起、
    断电搬迁后上电续跑，适用换子网）；实验口径约 25 分钟完成。硬约束：参数配错即死锁且无回退——动手前
    必须确认全部参数正确、基础设施一致、有可用备份（OT 备份 + 整盘镜像 Clonezilla（TC1625）/VMware 快照）；
    rehost 后 inactive 分区内容被清除，不能回滚/升级到旧分区（后续可平滑升级或全新安装）。改动不会触达
    OXE/8770/OMS 与生态，必须按 TC2149 矩阵补齐（OXE trusted IP、外部网关 Remote domain、8770 OT 节点
    FQDN、DNS/DHCP/SSO/SNMP/防火墙等）。
  conditions: 证书变更后 OTMS 需重启（TC2149 2.4）；换 FlexLM 形态需核许可锚定物（见 p41）
  tags: [rule, rehosting, tc2149, risk]

- id: p41
  title: rehosting 的许可联动：内嵌 Flex 可锚 MAC/ALUID/加密狗，外部虚拟化 Flex 必须加密狗；换形态要走 eBP 工单
  type: rule
  source_pages: p587
  source_chapter: TC2149 / Operation detail for OTMS/OTMC / License
  source_quote: |
    "When changing license FLEX server configuration from internal to external, the license controlled
    elements must be verified. Internal flex can use @MAC (physical server only), ALUID (physical
    server only) or a DONGLE External virtualized FLEX LM server requires the use of a DONGLE. A
    license adaptation may be required in such a case. Refer to license request for rehosting on eBP
    (Siebel ticket to open)" (p587)
  summary: |
    规则：rehosting 若涉及 FlexLM 内部→外部切换，锚定物必须复核——内嵌 Flex 可用 @MAC（仅物理机）、ALUID
    （仅物理机）或加密狗；外部虚拟化 FlexLM 只支持加密狗；不匹配时需要重做许可（经 eBP 开 Siebel 工单）。
    交付排期要把这条商务流程算进去。
  conditions: 证书在主机名/域名变更后也要重签重部署（TC2149 2.4）
  tags: [rule, rehosting, licensing, flexlm]

- id: p42
  title: 维护工具端口与入口：Maintenance Portal :4448；tsa_maintenance 端口 3595；隐藏菜单口令 2998；dla.sh 选项 1 须 root
  type: metric
  source_pages: p520-521, p479-480, p531
  source_chapter: Maintenance (讲义) / OTC PC Maintenance / Maintenance tools How-To
  source_quote: |
    "Through a specific URL https://<OpenTouch server FQDN>:4448" (p521)
    "Trying connect: opentouch.company.com 3595 Connection with opentouch.company.com , port 3595 is OK" (p479)
    "100 -------------------- MENU PROTECTED by secret code ... (2998 is the secret code value). So,
    choose the "ACAPI control" by entering "106 2998"" (p480)
    "MUST BE LOGGED AS ROOT TO BE ABLE TO EXECUTE OPTION 1 TO LAUNCH "DLA.SH"" (p531)
  summary: |
    端口/权限口径：Maintenance Portal 走 https://<OT FQDN>:4448（或 WebAdmin Monitoring 区进入）；
    tsa_maintenance（/opt/Alcatel-Lucent/infra_services/ots/）连本机 3595 端口，菜单 47 dump 全部号码、
    菜单 100 起为口令保护（口令 2998，经 106 2998 进 ACAPI control，选 7 重载全部 Acapi 对象可强同步）；
    dla.sh 日志收集的菜单选项 1 必须 root 执行（otconsole 1-5-1 路径同样受限）。listtool.sh 可按
    Maintenance/Troubleshoot/Information/Log/Misc 五类列全部脚本。
  conditions: 客户端侧日志另可经 OTC PC Settings → Support → Activate logging → Save logs 生成 zip
  tags: [metric, maintenance, ports, tools]

- id: p43
  title: 实验口径账号口令总表（RLAB）：root/letacla 系、superuser、Superuser01*、mtcl、adfexc、admin/letacla(SOT)
  type: metric
  source_pages: p16, p24, p69, p111, p298
  source_chapter: POD Settings / SOT How-To / Connections / WPC
  source_quote: |
    "OPENTOUCH OPEN_OTMS_STARTER opentouch 192.168.1.50 ... root superuser ... 8770 OPEN_8770_STARTER
    nms 192.168.1.70 ... adminnmc superuser Superuser01*" (p16, 实验口径)
    "Login admin Password letacla" (p69, SOT 默认口令)
    "Esxi server root ... superuser / OpenTouch root ... superuser otuser ... maintenanceuser /
    OmniPCX Enterprise mtcl mtcl swinst SoftInst adfexc adfexc" (p111)
  summary: |
    实验口径（RLAB，不可用于生产）：SOT 首次登录 admin/letacla（强改密+安全问题）；OT root=superuser、
    otuser=maintenanceuser（SOT 预置默认 root/letacla1，p101/p106 tips）；8770 adminnmc/Superuser01*；
    8770 Windows Administrator/superuser；OXE mtcl/mtcl、swinst/SoftInst、adfexc/adfexc；FlexLM VM root/
    letacla 首登强改；ESXi root 课堂改 superuser。IP：OT 192.168.1.50、8770 192.168.1.70、FlexLM
    192.168.1.80、SOT 192.168.1.230、OXE csa/csm 192.168.1.1/.3、DNS/NTP 192.168.1.254。
  conditions: 全部为实验口径；生产必须替换并纳入口令管理
  tags: [metric, lab, credentials, lab-口径]

- id: p44
  title: OXE 侧 SIP 数值口径：trunk 10/T2、外部网关 10→5260、11→5040、Subscribe Min Duration 600、Supervision timer 380
  type: metric
  source_pages: p227-233
  source_chapter: OmniPCX Enterprise SIP configuration (How-To)
  source_quote: |
    "Number of SIP Accesses 2 by default. Can be modified to specify the number of SIP accesses needed
    between OXE & OpenTouch" (p228)
    "SIP Subscribe Min Duration Enter 600" (p229)
    "Port number 5260 Transport type TCP ... Supervision timer 380 ... Outbound Calls 100 REL Supported
    Incoming Calls 100 REL Not requested Gateway type ICE type" (p231)
    "Port number 5040 ... Outbound calls only True" (p232)
  summary: |
    数值口径（实验示例值）：SIP trunk group ID=10、类型 T2、Q931=ABC-F、T2 Specification=SIP、SIP 接入数
    默认 2；本地网关端口 5060、Subscribe Min Duration=600、Registrar Min expiry=600；外部网关 10（To_OT→
    OT SIP server）：Remote domain=OT FQDN、端口 5260、TCP、Supervision timer=380、认证 None、Gateway type=
    ICE type、100 REL 出向支持/入向不请求、CSTA User-to-User=Yes；外部网关 11（TO_VM→Mule）：端口 5040、
    Outbound calls only=True；Proxy 认证 Digest+仅认证来话；trusted addresses 加 OT IP；codec G729、
    Routing Optimisation=Yes。
  conditions: Belonging domain 与 Contact with IP address 在 spatial redundancy 下的取值不同（TC1652）
  tags: [metric, sip, oxe, ports]

- id: p45
  title: 版本-功能时间线：otconsole.sh/SHA-2 自 R2.2；话务台前缀强制自 OT R2.1；License_release 10=R2.4、11=R2.5；SOT 补丁自 SOT 3.0
  type: metric
  source_pages: p65, p154, p238, p426, p519
  source_chapter: 分散于全书
  source_quote: |
    "Since SOT version 3.0, SOT VM can be updated by installing patches (".zip" file + ".MD5" file)" (p65)
    "License_release Examples: 10 for OpenTouchR2.4 11 for OpenTouchR2.5" (p154)
    "AFTER OT R2.1, CONFIGURATION OF THE ATENDANT PREFIX IS MANDATORY ..." (p238)
    "Since R2.2, SHA-2 (SHA-256) is available on OpenTouch because SHA-1 is deprecated." (p426)
    ""otconsole.sh" Available since R2.2" (p519)
  summary: |
    版本时间线四条：OT R2.1 起话务台前缀必配（否则重启 wireald）；R2.2 起 otconsole.sh 可用、SHA-2 可用且
    SHA-1 弃用；许可文件 License_release 值 10 对应 R2.4、11 对应 R2.5（R2.6.1 时代应核对更新值）；SOT 工具
    自身 3.0 起支持 zip+MD5 补丁升级（限同主版本）。做跨版本升级/比对旧文档时的基线参照。
  conditions: R2.6.1 具体命令横幅：Product OpenTouch™ Multimedia Services 2.6.1、Version 18.0.100.003（p115）
  tags: [metric, version, timeline]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 18 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | POD 搭建 | 有 | p43 | 实验 IP/账号口径；模拟器号码规则在 f05 |
| task-02 | SOT 部署 | 有 | p03, p45 | 宿主要求、SOT 补丁版本线 |
| task-03 | OVF 导入 | 部分 | — | 纯操作序列（thin provisioning 等）归 case；无独立数值 |
| task-04 | Post-installation wizard | 有 | p04, p05, p06 | 口令规则、DNS 清单、HA 禁用 |
| task-05 | 系统连接 | 有 | p43 | 账号口径；通道结构在 f10 |
| task-06 | 许可安装 | 有 | p07, p08 | 机制原则与路径命名规则 |
| task-07 | 许可核查 | 有 | p09, p10, p11 | spadmin 判据、lmutil、checkLicensing |
| task-08 | 外部 FlexLM | 有 | p12, p13 | 部署规则与切换规则 |
| task-09 | 声明 OXE | 有 | p14, p15 | 前置口径 + 同步矩阵 |
| task-10 | 声明 OT | 有 | p16, p17 | bics.conf 对应 + PRS/Codec 规则 |
| task-11 | OXE SIP | 有 | p19, p44 | codec 矩阵 + SIP 数值 |
| task-12 | prior management | 有 | p20-p26 | 号码段/前缀/拨号/UDAS/会议/DAS/格式化 |
| task-13 | 告警对接 | 有 | p18 | SNMP 数值口径 |
| task-14 | 档案与用户 | 有 | p27, p28, p29 | 档案边界、口令策略、WPC 约束 |
| task-15 | 语音邮箱体系 | 有 | p30-p35 | 档案面、IMAP、SMTP、SMS、公告、问候 |
| task-16 | 证书 | 部分 | p45 | SHA-1 弃用线；流程细节归 framework f25 与 case |
| task-17 | 客户端交付 | 有 | p36, p37, p38 | 多终端规则、OTC PC One 边界、监督规格 |
| task-18 | 运维 | 有 | p39, p40, p41, p42 | 备份数值、rehosting 规则、许可联动、工具端口 |

**覆盖结论**：18/18 中 17 项有直接条目，task-03（OVF 导入）与 task-16（证书）以操作序列为主，数值/规则部分并入相邻条目（p45、f25），无知识丢失。两点口径说明：
1. p44 的 SIP 参数、p43 的账号表均为"实验口径"示例值，已在条目内显式标注，生产化须按现场设计替换。
2. 原书的法国制式默认值（前缀 51-54/41/9、国码 33、DAS 十条）均忠实转写并标注"示例，须核对本国制式"。
