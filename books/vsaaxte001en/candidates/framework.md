# 框架/流程/结构候选 — Visual Automated Attendant (VSAAXTE001EN Ed20, R4.8.006)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径/命令、组件关系图示、界面分区。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书推进逻辑——概念底座 → 交付闭环 → 树设计核心 → HA 加强 → 运维与集成
  type: flow
  source_pages: p4, p19, p41, p63, p143, p239, p272, p319
  source_chapter: OVERVIEW / ARCHITECTURE / How-To 章节编排（全部分区页）
  source_quote: |
    "OVERVIEW" (p4) / "ARCHITECTURE" (p41) / "Pod Configuration - How to - Configure the Pod for VAA labs" (p63)
    "TREE EDITOR - NATIVE FEATURES" (p143) / "HIGH AVAILABILITY OVERVIEW" (p239) / "MAINTENANCE" (p272)
  summary: |
    全书十段推进：①实验环境（RLAB POD + SIP 模拟器，p3-18）；②VAA 概览（定位/功能/管理面，p19-40）；③架构（组件/呼叫流/HA 冗余/规格/证书，p41-62）；④交付基础实验（Pod 配置→装 VAA→OXE SIP 对接→证书→WebAdmin，p63-132）；⑤业务配置（公司/日历、提示音 TTS，p133-142）；⑥树设计（原生节点讲义 + 用例 1-3 + IVR 选项节点 + 五个节点专项实验，p143-238）；⑦高可用（讲义 + VAA 侧 + OXE 侧两段实验，p239-271）；⑧运维（维护/PCS/OPEX/升级/统计，p272-318）；⑨外部数据库（SQL 节点 + MS SQL Express，p319-344）；⑩培训收尾（p345-351）。讲义与实验交替，实验均带验收测试。
  conditions: 无版本前提；④⑦⑨的 How-To 依赖①的实验环境
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB POD 结构——五虚机 + 公共资源区拓扑
  type: diagram
  source_pages: p5-13
  source_chapter: TRAINING LAB ENVIRONMENT / Introduction / Training platform / Settings
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data center." (p5)
    "Common resources - Subnet 0 - 10.20.30.x - External DNS 10.20.30.250 - NAS: softs, licenses, … - SIP Simulator - SQL/Mail server 12.0.0.2 … Subnet 192.168.1.x - VAA Master - VAA Slave" (p7)
  summary: |
    POD 内五台虚机（实验口径）：OXE（VSAA_OXE，csa/csm，192.168.1.1 与 192.168.1.3）、OMS（VSAA_OMS，192.168.1.13）、FlexLM Server（VSAA_FLEXLM，192.168.1.80，root/letacla1）、VAA Master（VSAA_VAA_MASTER，vaa1，192.168.1.55）、VAA Slave（VSAA_VAA_SLAVE，vaa2，192.168.1.56）、PC CLIENT（VSAA_PC_CLIENT，CLIENT-PC，192.168.1.10，装 IPDSP + MicroSIP）。网关 192.168.1.254，内部 DNS 192.168.1.250；公共区（10.20.30.x）放 NAS/软件许可、SIP 模拟器（12.0.0.2）与外部 DNS。RLAB 纯虚拟化；课堂模式同拓扑、可经 RAP 接物理话机（p13）。
  conditions: 仅培训环境；POD 间相互独立、配置相同、共享公共资源
  tags: [structure, lab, rlab, topology]

- id: f03
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: diagram
  source_pages: p15-17
  source_chapter: SIP CARRIER SIMULATOR / Overview / External calls
  source_quote: |
    "ITSP1 SIP Gateway 1 - gateway1.itsp1.com - 10.20.30.51 … Id: pbxP - password: alcatel … SIP domain: sip.itsp1.fr" (p16)
    "PBX installation nb 3321PN … DDI table - First external nb 41000 … DDI table – First internal nb 31000 … Number sent by the PBX: +33210341002" (p17)
  summary: |
    模拟器在 RLAB 公共区扮演出局运营商：SIP 网关 gateway1.itsp1.com（10.20.30.51，PBX 注册账号 pbxP/alcatel，SIP 域 sip.itsp1.fr）与公网网关 public.itsp1.com（10.20.30.50）。号码规则（PN=两位 POD 号）：安装号 3321PN；DDI 外线首号 41000；内线首号 31000（用户 31000-31004）。外呼循环示例：POD 3 拨 0210341002 或 33210341002，PBX 送出 +33210341002 并收回同一号码（外呼回环）。OXE 侧只需在外部 SIP 网关填 Registration ID 与 Outgoing username = pbxP。
  conditions: 实验口径（RLAB 专用）；账号/号码/地址为教学约定值，不可套用到生产
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f04
  title: VAA 产品定位与四类功能清单
  type: structure
  source_pages: p20-21
  source_chapter: OVERVIEW / Features list
  source_quote: |
    "AUTOMATED 24/7 CALL ROUTING AND GREETING … Scalable software solution for small to extra-large businesses, multi-tenants and uses the SIP protocol … Security - compliance with CIS-2 Security Standards" (p20)
    "Generic … Administration … Features … Option" (p21 四栏功能清单)
  summary: |
    定位：专业客户迎宾/7×24 呼叫路由，可接数据库或呼叫中心方案，图形化界面，从中小企业到超大型、多租户、SIP 协议，符合 CIS-2 安全标准。功能四栏：Generic（HTTPS Web 管理、证书、WAV 导入/电话录制/TTS 提示音、PCS 支持）；Administration（受限用户档案、整系统导入导出、多租户、高级报表、计划备份、NFS 备份存储、邮件告警——中继断/端口占用、统计日志报表）；Features（层级树、多语言、直拨、营业时间与日历路由、子树挂接、按主叫/被叫过滤、菜单节点可定制（定时器/重试）、转固定号或留言箱、监督与盲转按节点、按姓名拨号、异常事件问候、TTS、ASR）；Option（IVR：呼叫定性、数据库读写、HTTP 请求、SQL 读写、收号、语音识别、条件测试、自定义显示名、邮件）。p145 重复此清单。
  conditions: Option 列需 IVR 许可（p27 "IVR options (Additional licenses)"）
  tags: [structure, features, product-scope]

- id: f05
  title: VAA 软件组件族与六服务视图
  type: structure
  source_pages: p54, p277
  source_chapter: ARCHITECTURE / VAA components & MAINTENANCE / Main VAA services
  source_quote: |
    "aa-license-server Manage licenses / aa-media-server Manage the SIP connection with the OXE, and the RTP stack / aa-cli VAA Command Line Interface / aa-webapp A tomcat java web application server, that host two web app. aa-management … aa-engine … / Postgresql A postgresql 16 database … / Nginx Configured as an HTTP reverse proxy to the web app / tts-hub Service to access TTS and Speech Recognition service" (p54)
  summary: |
    组件七件：aa-license-server（FlexLM 许可）、aa-media-server（与 OXE 的 SIP 连接 + RTP 栈）、aa-cli（命令行）、aa-webapp（Tomcat，承载 aa-management 管理界面与 aa-engine 引擎——引擎与 media-server 协作从库中取脚本）、PostgreSQL 16（提示音/路由策略/统计）、Nginx（HTTP 反向代理）、tts-hub（TTS 与语音识别服务接入）。p277 服务表同口径：nginx 使管理 webapp 在 80 端口可用；日志目录见 p281。
  conditions: 无；组件名是 vaa services 输出与日志目录的命名基础
  tags: [structure, components, architecture]

- id: f06
  title: 高层软件架构与四步典型呼叫流
  type: diagram
  source_pages: p42-43
  source_chapter: ARCHITECTURE / High level software architecture / Typical call management
  source_quote: |
    "VAA is connected to the OmniPCX Enterprise using a SIP trunk of ABC/F Type … Management application access is secured using https over TLS 1.2 … The SIP Trunk between Visual Automated Attendant and OmniPCX Enterprise can be encrypted. Visual Automated Attendant supports G711 (aLaw/µLaw), and G729. Note: G729 can't be used with Automatic Speech Recognition feature … The CMIP link allow to synchronize the Visual Automated Attendant with the OXE Phone book." (p42)
    "1 The calling party calls the company welcome number through the public network 2 OmniPCX Enterprise routes the call to the Visual Automated Attendant via a SIP trunk 3 The Visual Automated Attendant runs the script associated to the called number, plays the announcement voice guides, collects digits, … 4 The Visual Automated Attendant routes the call to the destination through the OmniPCX Enterprise in blind transfer." (p43)
  summary: |
    架构五要素：VAA（Media Server/Engine/Management）— FlexLM 许可服务器 — PostgreSQL — HTTPS 管理（TLS 1.2）— OXE（SIP/ABC-F 中继，可加密 SIP/TLS；CMIP 链路同步 OXE 电话簿）。编解码 G711 aLaw/µLaw 与 G729（G729 与 ASR 互斥）。呼叫四步：公网呼入公司欢迎号 → OXE 经 SIP 中继送 VAA → VAA 执行被叫号绑定的脚本（放音/收号）→ VAA 经 OXE 盲转/监督转落地（分机/留言箱/话务员）。
  conditions: SIP trunk 加密为可选（SIP TLS/SRTP，需两侧有效证书，见 p102）
  tags: [diagram, architecture, call-flow, sip-trunk]

- id: f07
  title: Master/Slave 高可用机制图（OXE ARS 切换 + 数据库复制）
  type: diagram
  source_pages: p44, p240
  source_chapter: ARCHITECTURE & HIGH AVAILABILITY OVERVIEW / High availability - Redundancy
  source_quote: |
    "High availability is made of one Master VAA and one slave VAA … The routing is performed by OmniPCX Enterprise based on an ARS routing table … When Master VAA goes down, ARS mechanism routes calls through SIP Trunk 2 on the Slave VAA … The VAA database is replicated from master to slave … The slave VAA database is in ReadOnly mode. Therefore, no statistics will be recorded for a call handled during the failure period on the PCS side." (p44)
  summary: |
    HA 结构：两台 VAA 各建一条 SIP 中继（trunk group 1→Master、trunk group 2→Slave），OXE 用 ARS 路由表选路；数据库 Master→Slave 定期复制。行为口径：Slave 库只读，故障期间被处理呼叫不产生统计。该图在 p240（HA OVERVIEW 章）原样重复，是 OXE 侧 HA 实验（c17）的设计蓝图。
  conditions: 切换由 OXE ARS 完成，VAA 自身不做漂移
  tags: [diagram, ha, redundancy, ars]

- id: f08
  title: OXE 冗余三用例矩阵——呼叫服务器丢失 / 主 VAA 丢失 / WAN 断
  type: structure
  source_pages: p45-48
  source_chapter: ARCHITECTURE / OXE local & spatial redundancy – 3 use cases
  source_quote: |
    "In case of switch over of the call server, the SIP trunk is re-established on the standby call server. Existing ongoing calls are lost when switch over occurs" (p45)
    "In case of failure of master VAA, the SIP trunk is established between the main call server and the slave VAA. … No database synchronisation will be performed when master VAA will be recovered. Web client must reconnect (to Slave VAA)." (p47)
    "Spatial redundancy is not supported in Purple On Demand solution" (p46)
  summary: |
    三用例：①OXE 呼叫服务器切换（本地/空间冗余）——中继在新主呼叫服务器上重建，进行中呼叫丢失；②主 VAA 丢失——中继切到主呼叫服务器↔Slave VAA，Slave 只读（不能改配置、无统计），Master 恢复后不自动回同步，Web 客户端需重连 Slave；③WAN 断——中继切到伪主呼叫服务器↔Slave VAA，复制停止。空间冗余（地理双中心）要求在第二数据中心部署 Slave VAA；Purple On Demand 不支持空间冗余。
  conditions: 三用例均为讲义级，无实验
  tags: [structure, ha, redundancy, use-cases]

- id: f09
  title: PCS 支撑架构——中心 VAA + 外围 PCS VAA
  type: diagram
  source_pages: p49, p300-303
  source_chapter: ARCHITECTURE & PCS SUPPORT / PCS support reminder & databases synchronization
  source_quote: |
    "Main VAA manages the peripheral areas. SIP Trunk is established with the call server. Configuration of the central VAA connected to CS is copied toward all the VAA-PCS databases in a regular basis. On network failure, PCS becomes active. PCS VAA establishes the SIP Trunk with the PCS and manages local calls." (p49)
    "sudo vaa conf pcs [IP@] … sudo vaa db sendBackup [IP@] … Daily automatic backup defined with standard name Backup4PCS.sql.gz … First cron task set at 01:00 AM. Second cron task set at 01:00 + 1 minute …" (p303)
  summary: |
    PCS 架构：中心 VAA 与呼叫服务器建中继；配置周期性复制到各外围 PCS VAA（DB Import/Export）；断网时 PCS VAA 激活、与 PCS 建中继管本地呼叫，可临时配本地应急但网络恢复后丢失。同步实现：vaa conf pcs [IP@] 配置自动同步（建 SSH key、默认备份名 Backup4PCS.sql.gz），vaa db sendBackup [IP@] 发备份并远端恢复；定时任务每天 01:00 起，第二/三个任务各延 1 分钟。
  conditions: PCS 为可选支撑能力（features list Generic 列 "PCS support"）
  tags: [diagram, pcs, synchronization]

- id: f10
  title: OXE multi-company 集成与 N+1 冗余结构
  type: structure
  source_pages: p50-51
  source_chapter: ARCHITECTURE / Integration with OXE multi-company & Multiple VAA in N+1 redundancy
  source_quote: |
    "VAA supports OmniPCX Enterprise multi-company features • For details, refer to the document TBE083 … The Visual Automated Attendant Media Server is shared by all companies • It's not possible to reserve ports for a given company" (p50)
    "N+1 redundancy is made of a 'reference VAA' and several other VAAs. The 'reference VAA' serves as configuration basis for all VAAs … When one VAA becomes unavailable, ARS mechanism routes the calls to other VAAs (N+1 principle) … If 'reference VAA' becomes unavailable, the other VAAs continue to operate but any configuration changes is impossible" (p51)
  summary: |
    multi-company：VAA 支持 OXE 多公司功能（细节见 TBE083），媒体服务器被各公司共享（公司 A 号 861 → VAA 号 8613999，公司 B 号 862 → 8623999，SIP 中继属公共公司），不能为单一公司预留端口；配置细节指向 OTEC-S: Visual Automated Attendant configuration Guide。N+1：一台 reference VAA 作配置基准（脚本/提示音/日历等复制到其他 VAA，各自统计除外），ARS 按 N+1 原则把呼叫分给可用 VAA；故障期间总容量下降，reference 挂了其余可跑但不能改配置。
  conditions: N+1 面向扩容（同 OXE 多 VAA），Master/Slave 面向冗余
  tags: [structure, multi-company, n+1, capacity]

- id: f11
  title: 服务器规格三档表与端口上限
  type: structure
  source_pages: p52, p55
  source_chapter: ARCHITECTURE / Server prerequisites & TCP/UDP port usages
  source_quote: |
    "The maximum number of VAA ports supported is 120 • To go above this limit, please contact the central presales team … up to 8 ports / up to 50 ports / up to 120 ports — Processor Dual-core 2.4 GHz / Quad-core 2.4 GHz / Octo-core 2.4 GHz — Memory 8 GB / 16 GB / 32 GB — Network 100 Mb/s / 1 Gb/s / 1 Gb/s — Hard Disk 80 GB / 80 GB min 320 GB" (p52)
    "The remote SSH access for the ROOT account is forbidden. You must use the admin account with the function 'sudo'." (p55)
  summary: |
    规格三档（示例口径，原文两处强调"Given as an example! Always consult the official documentation!"）：≤8 端口——双核 2.4GHz/8GB/100Mb/s/80GB；≤50——四核 2.4GHz/16GB/1Gb/s/80GB；≤120——八核 2.4GHz/32GB/1Gb/s/≥320GB；超 120 端口找中央售前。p55 为端口清单页（正文仅一句安全规则：root 禁止 SSH 远程登录，须 admin + sudo）。
  conditions: 规格表为示例；端口清单细节在官方文档
  tags: [structure, sizing, prerequisites]

- id: f12
  title: 虚拟化环境兼容表
  type: structure
  source_pages: p53
  source_chapter: ARCHITECTURE / Virtualized environment
  source_quote: |
    "VMware ESXi 8.0 • Network adapter for the VM must be VMXNet3 • VMWare Tools must be installed / Microsoft Hyper-V 2022 • VM type recommended is Generation 2 / KVM hypervisor Proxmox 8.2 • Network adapter for the VM must be VMXNet3 … (1) KVM hypervisor Proxmox supported from VAA 4.6.1" (p53)
  summary: |
    三种 Hypervisor（同样标注示例口径）：VMware ESXi 8.0——网卡必须 VMXNet3、须装 VMware Tools；Microsoft Hyper-V 2022——推荐 Generation 2 虚机；KVM（Proxmox 8.2）——VAA 4.6.1 起支持、网卡须 VMXNet3。部署细节指向 VAA Installation Manual。
  conditions: 版本随时代演进，选型前对官方兼容表
  tags: [structure, virtualization, hypervisor]

- id: f13
  title: HTTPS 切换与证书体系（版本前提 + 证书格式 + 三种来源）
  type: flow
  source_pages: p56-62
  source_chapter: ARCHITECTURE / Switching VAA to HTTPS / Certificate installation / generation with XCA / public certificate
  source_quote: |
    "From version 4.6.104, the VAA web interface is only accessible via HTTPS … PKCS12 certificates (.pfx and .p12 extensions) • PEM certificates (.pem, .crt and .cer extensions for the certificate and .key for the certificate key) … If no certificate has been provided, the installation process will generate a self-signed certificate and its associated key" (p57)
    "The certificate and its associated key can be updated with the following command: vaa conf https … HTTPS configuration status … vaa diag https" (p58)
    "The Subject Alternative Name (SAN) … must be completed by added the VAA IP address and DNS name … Mandatory, the commonName: vaa1.company.com" (p60)
  summary: |
    证书体系四块：①版本前提——4.6.104 起仅 HTTPS；全新安装自动配 HTTPS，升级时已有配置保留、无配置可选切换（切换会擦除原配置）或保持 HTTP；②格式——PKCS12（.pfx/.p12）与 PEM（.pem/.crt/.cer + .key）；约定上传 /tmp 让安装进程自动识别；无证书则自签（S.O.T 安装只能自签）；③管理命令——vaa conf https 更新、vaa diag https 查状态；④证书生成——实验用 XCA 建 RootCA（SHA-256、RSA 4096、填签发者信息）+ VAA 证书（SAN 必须含 VAA IP 与 DNS 名、CN 必填 vaa1.company.com，导出 vaa1.pfx）；RootCA 导入 PC 信任库。暴露公网须向 CA 购买真证书，步骤（上传/配 Nginx/重启）见安装手册 6.4。
  conditions: XCA 参数（Hash/密钥长度/信息）须按客户环境调整
  tags: [flow, https, certificate, xca, security]

- id: f14
  title: WebAdmin 管理面分区（登录/About/公司/角色/编辑器/路由/日历/过滤/目录/提示音/公司设置/管理员菜单）
  type: structure
  source_pages: p22-39
  source_chapter: OVERVIEW / WEBADMIN … ADMINISTRATOR MENU
  source_quote: |
    "Login: admin - Password: admin … The password for the admin account must be changed on 1st connection. … http://<hostname> … Enter the VAA URL or @IP" (p22)
    "It displays general system information about the server … Settings management SNMP, SMTP, PBX and security … Supervision, stop & restart services (Use a SSH connection) … Server logs to facilitate support … Content and usage of the currently loaded license file" (p39)
  summary: |
    管理面地图：登录（默认 admin/admin 首连必改，URL http://<hostname> 或 IP，实验 https://192.168.1.55）；About（版本/许可端口数/服务器信息）；Companies（多公司：每公司时区/DDI 段/目录辅助类型/分机位长，创建公司入口）；Administrators & user profiles（超管建公司、公司资源=用户/路由/提示音/计划/目录/过滤器/树编辑器/统计；角色分管理类与功能类——Routing/Prompts/Directory/Filters/Calendar 等）；Tree editor（p27 命令与 IVR 选项清单）；Routing numbers（DID↔树，含激活）；Calendars & Schedule；Filters（CSV 或表达式建主叫过滤）；Directory（手工/OXE 同步）；Prompts（WAV/录制/TTS/ASR）；Company settings（时区/DID 段/留言前缀/目录/TTS/ASR/外部库/变量）；Administrator menu（Server info/Settings(SNMP,SMTP,PBX,security)/Supervision/Logs/License）。
  conditions: 界面随版本演进；实验全在 https://192.168.1.55
  tags: [structure, webadmin, ui-map]

- id: f15
  title: 树编辑器原生节点全集（12 种）与画布命令
  type: structure
  source_pages: p27, p144-162
  source_chapter: OVERVIEW / TREE STRUCTURE EDITOR & TREE EDITOR NATIVE FEATURES
  source_quote: |
    "Tree design associated commands • Set default language • Play prompt • Business hours • Calendar • Menu • Transfer • Transfer to voicemail • Filter call • Jump to sub tree • Record prompt via TUI • Release call • Comments" (p27)
    "Menu with up to 12 choices (0-9, #, *)" (p144)
  summary: |
    原生节点 12 种：Start（树默认语言）、Select language（呼叫者选语言）、Announcement（放提示音，四种模式：Prompt/TTS/Global Prompt/Server file——最后者不推荐；可勾 DTMF 打断）、Business hours（营业时间分支，自定义或引用 Schedule）、Calendar（闭假日分支）、Menu（最多 12 选项 0-9#*；重试次数/超时/重复键/最大重复；直拨、盲转或监督转、保持音、过滤、多过滤模式与反向过滤、ASR 菜单选择两种档位）、Transfer（目的地=号码或目录辅助；监督/盲转；过滤；ASR 读名；保持音；Wait time；Bypass forward）、Voicemail（转留言箱，箱号须在公司设置管理）、Filter（主叫过滤分支 + Unknown ANI 入列）、Go to tree（跳子树，仅同租户）、Record prompt（季节性提示音远程录制，需租户用户 ID+PIN）、Release（挂断，命名进报表）与 Comment（画布注释）。画布命令含 Import/export/Save 等。
  conditions: 节点命名必须个性化（统计依赖，p145/p165）；IVR 选项节点另见 f16
  tags: [structure, tree-editor, nodes, ivr]

- id: f16
  title: IVR 选项节点全集（9 种，另购许可）
  type: structure
  source_pages: p27, p203-213
  source_chapter: TREE EDITOR / IVR OPTIONS & 各节点页
  source_quote: |
    "Custom display name … Collect digit … Speech recognition … SQL request … Correlator Data … Condition … HTTP request … Mail Service … Set variable" (p203)
    "Options subject to licenses allowing the VAA server to be connected to an information system" (p203)
  summary: |
    九种 IVR 选项节点：Custom display name（监督转接振铃期在目标话机屏显名称）；Collect digit（收号存变量：位数上下限、# 结束、超时/重复）；Speech recognition（外部引擎识别结果存变量）；SQL request（对外部库执行 SELECT/INSERT，单字段返回，多行多列模式最多 200 行）；Correlator data（在 SIP 帧注入 User-to-User 相关数据，Magic ID 0xC015 使 OXE 在振铃期显示呼叫标签，ASCII 最长 27 字节 + XOR 校验）；Condition（变量比较路由：Is empty/Contains/Equals/Starts with/End with/length 等，可比较另一变量）；HTTP request（GET/POST/DELETE/PUT，可配头与出站代理）；Mail（脚本内发邮件，SMTP/SMTPs，plain/SSL/TLS 认证，正文可 HTML）；Set variable（声明/赋值变量）。
  conditions: 全部需要 IVR 许可；SQL/HTTP 节点安全与性能边界见 principle 条目
  tags: [structure, ivr-options, nodes, licensing]

- id: f17
  title: Pod 配置操作流（OXE 底座准备）
  type: flow
  source_pages: p63-74
  source_chapter: How-To / Pod Configuration
  source_quote: |
    "Check that the following virtual machines have started. Don't start the 'VAA slave' instance." (p64)
    "According to your POD number, configure 2 parameters in your external SIP gateway: ­ Registration ID: pbxP … ­ Outgoing username= pbxP" (p69)
    "Add the VAA master (IP @= 192.168.1.55) and VAA slave servers (IP @= 192.168.1.56) as a trusted host. via netadmin -m" (p70)
  summary: |
    七步：①核对虚机已启动（不启 VAA Slave）；②OXE 预配置核对（许可恢复、FlexLM 192.168.1.80 已声明、机架/板卡在服——Software Rack 3U OMS/Rack 4/Virtual GD4 slot0 192.168.1.13/24 MAC 00:50:56:01:01:13；DHCP 192.168.1.145-149）；③开通用户——IPDSP 31000（Brad Barkley，密码 0000）与 MicroSIP 31001-31004（Online 状态）；④外部 SIP 网关填 pbxP（Registration ID 与 Outgoing username）；⑤DID 翻译（Translator/External Numbering Plan/Default DID num. translator：首外线 33210P41000、首内线 31000、范围 500）；⑥外呼测试（对照 SIP Carrier Simulator 文档）；⑦防火墙信任主机——OXE 上 root 登录 netadmin -m → 11 Security → 1 Firewall(iptables) → 3 Restricted Access → 2 逐个加 vaamaster 192.168.1.55 与 vaaslave 192.168.1.56 → 23 Apply modifications；附：p74 Thunderbird 按 POD 选档案收培训邮件。
  conditions: 全部为实验口径；netadmin 菜单号以书中为准
  tags: [flow, pod, oxo-oxe, firewall, menu-path]

- id: f18
  title: VAA 安装三方式与手工安装/发行包装配流程
  type: flow
  source_pages: p76-83, p88-104
  source_chapter: VAA INSTALLATION STEPS（讲义）& How-To / Install the VAA application
  source_quote: |
    "VAA can be installed in different ways: • MANUALLY (Used in this training) • AUTOMATICALLY With S.O.T (software Orchestration tool) … • Via Purple on demand" (p76)
    "sudo ./install.sh • Enter OXE IP@ & standby • Define an incoming username which will also be entered in the external SIP gateway • Choose codecs • Enable email notifications • Barring • Configure VAA database auto backup • Activate SIP TLS/SRTP if needed • PostgreSQL user password • Specify if a remote Syslog server is used • Add the license file" (p81)
    "Important information to read carefully before installing VAA 4.8.006: • Only a fresh installation followed by a database restoration is supported. • A new license (Release 11) is required." (p89)
  summary: |
    三方式：手工（本书实验）、S.O.T 自动（装系统/配网/改默认密码/装许可/装 VAA，物理或虚机，填写项见 p78：admin 与 root 密码须 20 位含大写/数字/特殊字符、键盘、国家、主机名、MAC、IP）、Purple on Demand。手工流（p88-104）：①系统准备——ALE BootDVD 选 VAA（4.8）装 SUSE（实验跳过，预装虚机起步）；root 首登 letacla1 改 InternationalSuperuser1234*（≥20 位），admin letacla1 改 Superuser1234*（≥12 位），GRUB 口令（≥14 位，实验 Generalconfig1!）；②配网——IP 192.168.1.55、FQDN vaa1.company.com、掩码 255.255.255.0、网关 192.168.1.254、DNS 192.168.1.250；③传文件——FileZilla SFTP：发行包 zip → /home/admin（二进制），license1.vaa → /tmp（二进制）；④装——sudo su → unzip Visual_Automated_Attendant-4.8.006.zip → cd aa-distribution-4.8.006 → sudo ./install.sh 交互应答（本地 IP 确认 y；证书选"稍后提供"→自签；OXE 主/备 IP 192.168.1.3；incoming username vaa1 无密码；编解码 G711a+G729；代理 N；邮件 y（SMTP 10.20.30.11:25 plain，发件 vaa.podX@company.com，收件 administrator.podX@company.com）；禁拨前缀空（实验）；自动备份 y（vaa.tar，Daily 午夜）；SIP TLS N；postgres 密码 Superuser1234*；远程 syslog N；许可 y（/tmp 自动识别 license1.vaa））；⑤验收——vaa status 全 Running，浏览器 https://192.168.1.55。HA 场景：slave 同法安装（vaa2/192.168.1.56/license2.vaa），配置一律从 Master 发起（p82-83）。
  conditions: 全部实验口径；生产须提前准备证书与真实 SMTP/许可
  tags: [flow, installation, install-sh, sot, menu-path]

- id: f19
  title: OXE 侧 SIP 对接配置链（trunk group → 外部网关 → 信任 IP → 路由 → 全局参数）
  type: flow
  source_pages: p85-86, p105-113
  source_chapter: VAA INSTALLATION STEPS / MAIN CONFIGURATION STEPS & How-To / SIP configuration in OXE
  source_quote: |
    "The VAA's on-board server SIP must be declared as an external SIP gateway … Set the VAA server IP as a trusted IP address … Manage the routing numbers … Dedicated OXE SIP Gateway for VAA + VAA type • incoming username field must be defined • SIP TLS/SRTP supported" (p85)
    "The SIP configuration must be done manually in the OXE, which means that you must create the SIP trunk group, the external gateways, manage the local SIP gateway, the proxy..." (p107)
  summary: |
    五段链：①SIP trunk group（/Trunk groups/ Create：ID 10、名 SIPVAA1、类型 T2、Node 1、Q931 变体 ABC-F、Remote network 10（未占用且异于 OXE 网络号）、T2 specificity=SIP、直连 RTP 否；局部设置：端到端拨号 Yes-自动话音频率切换、DTMF 端到端 Yes、QoS Always VoIP；SIP virtual access 默认 2）；②本地 SIP 网关联动（/SIP/SIP Gateway：SIP 子网 10 + trunk group 10，初始化 SIPMOTOR）；③外部网关（/SIP/SIP Ext Gateways Create：ID 2、名 VAA1、远端域=VAA IP 192.168.1.55、端口 5060、UDP、监督定时器 60、trunk group 10、incoming username=vaa1（与安装一致）、密码空、最小认证 None、网关类型 VAA）；④信任 IP（/SIP/Trusted IP Addresses：192.168.1.55）与网络路由表（Translator/Network Routing Table/<network 10>→关联外部网关 2）；⑤路由号码（Translator/Prefix Plan：前缀 314→网络 10、trunk group 10、5 位）。HA 场景另建第二套（trunk group 11/SIPVAA2、外部网关 3/VAA2/192.168.1.56/信任 IP，p86、p256-267）+ ARS。全局参数：DPNSS 前缀 599 路由优化（/System Routing optimization Yes，p112）、编解码 G729 两侧匹配（OXE N2 起默认，p113）、外部回叫翻译去 "0B"（Basic number B 删 1 位，p113）。
  conditions: 客户现场已有参数不要改（p109 SIPMOTOR 注）；OXE 侧配置全书手工
  tags: [flow, oxe, sip, trunk-group, menu-path]

- id: f20
  title: OXE-VAA 接通性验证与四层排障抓手
  type: flow
  source_pages: p114-121
  source_chapter: How-To / SIP configuration in OXE / Testing the connection & Maintenance
  source_quote: |
    "Manage a basic tree simply playing a guide so that you can easily test the connection with the VAA server. ­ Guide to play: Welcome ­ Number to call to reach the tree: 31400" (p114)
    "Command trkstat -r 10 … On the CS : login as 'mtcl' Command sipextgw –g 2 … Command motortrace 3 Command traced … mtracer" (p119-120)
    "Select the 'Logs' tab. Specify the type of logs you want to consult. Here 'softcmp (SIP)'" (p121)
  summary: |
    验证四步：①WebAdmin 首登（admin/admin→改 Superuser1234*）建测试公司 TEST；②Editor 建最简树（Start→Announcement(Welcome)→Hang up 节点）存为 TEST；③Routing 绑 31400 并激活；④软话机拨 31400——应听到欢迎语后自动挂断。排障四层：①OXE 中继状态 trkstat -r 10（mtcl 登录，看 62 路 Free/Busy）；②外部网关状态 sipextgw –g 2（State: IN SERVICE、远端域/端口/代理核对）；③OXE SIP 抓包——motortrace 1/2/3（信息量递增，量大用 2、需细节用 3）+ traced，或 mtracer 全套（tuner km/clear-traces/+cpl+cpu+at、actdbg csip=on、mtracer –a）；④VAA 侧日志——WebAdmin 头像 → Administrator Menu → Logs → 选 softcmp (SIP)，默认 200 行可调，Refresh 查看。
  conditions: 建树细节在 c08 展开；此处只做最小验证树
  tags: [flow, testing, troubleshooting, motortrace, menu-path]

- id: f21
  title: 公司创建与业务时间/日历管理流
  type: flow
  source_pages: p24, p30-31, p133-136
  source_chapter: OVERVIEW / MULTI-COMPANIES … CALENDARS & How-To / Create a new company
  source_quote: |
    "Select the company to display its settings - Create a company" (p24)
    "Define the Business hours name 'Open hours' with following settings: ­ Business hours from 9am to 12 and from 2pm to 6pm ­ Closed during the Weekend ­ Time zone: Europe/Paris (UTC+02:00)" (p135)
  summary: |
    公司四要素（p24）：独立时区、DID 段（树的号码范围，可用内线号）、目录辅助类型（按姓名拨号/留言箱——OXE 留言号）、分机位长。创建流（p133-136）：登录 https://192.168.1.55（admin/Superuser1234*）→ 输名称点 "+" → 设时区（实验 Europe/Paris UTC+02:00）、DID 段（实验 31400-31415，内线号口径）、留言前缀（31499）、分机 5 位 → 点公司名左侧对勾进入其配置。业务时间：Schedule 页签 → Business Hours 输名称（Open hours）→ "+" → 按周填时段（9-12、14-18，周末关闭）。日历：Calendars 页签 → 输名称（Calendar1）→ "+" → 勾闭假日（1/1、4/14、7/14、11/11）并管理来年假日。日历/营业时间既可在 Schedule 页签维护也可在树内节点自定义（p30-31）。
  conditions: 树绑定 DID 段须落在公司 DID 范围内
  tags: [flow, company, schedule, calendar, menu-path]

- id: f22
  title: 提示音与 TTS/ASR 管理流
  type: flow
  source_pages: p33-37, p137-142
  source_chapter: OVERVIEW / PROMPTS MANAGEMENT … & How-To / Manage Prompts and Text-to-Speech
  source_quote: |
    "Import of wav files •Format: 8KHz PCM 16-bits mono … Text To Speech •Free TTS engine embedded - PicoTTS (DE, GB, US, FR, ES, IT) •Paid (Licenses not provided by ALE) based on the number of characters •Google Cloud TTS … Speech Recognition •Google ASR" (p34)
    "Define a name: TTS Pico - Choose the TTS engine: PICO - SAVE - Make a test ­ Language Pico English/French…etc ­ Click on Generate to create a WAV file" (p140)
  summary: |
    提示音三来源：WAV 导入（8KHz PCM 16-bit 单声道；NAS 提供样例；名称不能含空格；按语言分别导入）、电话录制（拨专属 "-Prompt Recording-" 树号码，或树编辑器/Prompts 页发起；User ID+密码，Prompt ID 见 Prompts 菜单，p28）、TTS 生成（Prompts 页或树节点内）。TTS 激活：Tenant/Settings → Text to speech 页签 → 定义引擎（名 TTS Pico、类型 PICO）→ Save → 测试生成。引擎选型：Pico 免费离线（六语言 DE/GB/US/FR/ES/IT，不建议生产）；Google Cloud TTS 付费（按字符计费，非 ALE 提供）；ASR 用 Google speech-to-text（需 Google Cloud 账号 + API key），在公司设置配置识别。语音一致性建议：TTS 树把存量 WAV 统一转 TTS（p138）。多语言提示：语言选择前的提示要在同一 WAV 内双语串联（p188，用例 3 关键约束）。
  conditions: 云引擎价格信息可能过时（p141 自注）
  tags: [flow, prompts, tts, asr, menu-path]

- id: f23
  title: 树设计三级用例递进链（UC1 简单转接 → UC2 日历+过滤 → UC3 多语言菜单）
  type: flow
  source_pages: p164-201
  source_chapter: How-To / Manage a VAA script (tree) – Use case 1/2/3
  source_quote: |
    "Use a Transfer node to transfer calls to the number entered: 31000. The transfer will be supervised, this will make it possible to manage behavior on busy and no response" (p168)
    "Callers will be filtered : ­ 31000 (IPDSP) is a VIP. It will receive a personalized answer and will be transferred to the number: 31001 ­ All other callers (Non VIP) will be transferred to the extension number 31002." (p175)
    "This tree will use 2 languages: French & English. According the caller choice, the tree will be played in French or English." (p187)
  summary: |
    三级递进（先建依赖物再建树是共同铁律）：UC1 Training 树——Start→Announcement(TTS 欢迎语)→Transfer（监督转到 31000、Wait 15s、Bypass forward、保持音）→No answer/Busy 两个 Announcement 分支→Release；绑 31401。UC2 Customers services 树——前置建 Calendar2、Business Hours company1、Filter(VIP=31000)；树内 Calendar 节点（营业日→Business hours 节点；闭日→Closing prompt）→Filter 节点（命中=VIP→盲转 31001；未命中→盲转 31002）；绑 31402。UC3 Welcome employees 树——前置建双语提示（MainMenuChoices/PromptInformationEmployees，欢迎语双语串一个 WAV）；树内 Languages choice 菜单（1 法 2 英，超时挂断）→Select language 双节点→Main menu（4 选项：信息播报/盲转 helpdesk 31002/留言箱 31000/跳 Training 树；重试 2、超时 4s、重复键 *、最大重复 2；无输入异常→转话务员 31000）；绑 31403。每树完成后 Routing 激活并按测试清单拨打验证。
  conditions: 每个节点必须命名（统计依赖）；连接线逐节点建立
  tags: [flow, tree-design, use-cases, menu-path]

- id: f24
  title: 变量体系与动态脚本流（Set variable/Condition 闭环）
  type: flow
  source_pages: p215-220
  source_chapter: How-To / IVR node - Variables
  source_quote: |
    "Variables could be: ­ Local … ­ Global … ­ Contextual: a context variable is a variable linked to the current call. These variables are predefined and cannot be modified." (p216)
    "In the following example, we will analyze the caller ID and determine if it is internal or external. The conditions to be tested will be: ­ Internal numbers start with 31 ­ The external calling number +33210P12345 (P: pod number) is a VIP" (p218)
  summary: |
    变量三类：Local（脚本启动时创建，仅本 VAA 线可见）、Global（公司级，全树共享——适合做免改脚本的通用参数）、Contextual（呼叫上下文预定义只读，清单在管理指南）。实验树：Start → Set variable（复制 callingNumber 上下文变量）→ Welcome 播报 → Condition（以 31 开头=内部 → TTS "Internal Call"）→ Condition（等于 +33210P12345=VIP → "VIP call"，否则 "Other calls"）→ Release；绑 31404。测试：内部呼叫、公网用户呼入、内部用户打公网回环。进阶：三迭代循环并用 TTS 报告每轮。
  conditions: 变量是 SQL/HTTP/收号/TTS 四节点的必需品（p216）
  tags: [flow, variables, condition, menu-path]

- id: f25
  title: HA 安装五步流（slave 侧安装 + master 侧 addslave + 双侧验证）
  type: flow
  source_pages: p240-246, p247-255
  source_chapter: HIGH AVAILABILITY OVERVIEW & How-To / Install the high availability for VAA
  source_quote: |
    "HA configuration is performed from the master server … Run the command: vaa ha addslave [IP@ of the slave] ssh keys are generated to allow sync to the slave server and to copy a snapshot of the current database to the slave server" (p82)
    "Warning ANY CONFIGURATION THAT HAD BEEN DONE ON THE SLAVE WILL BE ERASED, AS THE DATABASE WILL BE REPLACED BY A COPY OF THE MASTER'S DATABASE." (p252)
  summary: |
    五步：①slave 系统准备（同 master：BootDVD/改密/GRUB；FQDN vaa2.company.com、IP 192.168.1.56——FQDN 用于许可文件，问题查 /var/lib/ale/aa-license-server/）；②slave 装 VAA（同法 install.sh：incoming username vaa2、license2.vaa、其余同 master 参数）；③核对互通——Web 可达、双机互 ping；④master 侧配置——SSH 192.168.1.55（admin/Superuser1234*）→ sudo su → vaa ha role（应 Classic）→ vaa ha addslave 192.168.1.56（输 slave admin 密码，建 SSH key + 复制库快照，slave 原配置被清）；⑤验证——slave：sudo vaa restart → vaa ha role（Slave）；master：vaa services 全 Running、vaa ha role（Master）、vaa ha listslave（192.168.1.56）；slave：vaa services、vaa ha whoismaster（192.168.1.55）、登录 slave Web 确认只读告警且配置与 master 一致（公司/路由/脚本）。
  conditions: addslave 在 master 执行；slave 库会被 master 快照覆盖
  tags: [flow, ha, addslave, vaa-commands, menu-path]

- id: f26
  title: OXE 侧 HA 附加配置链（第二中继/网关/识别符/NPD/ARS 双路由/时间路由/测试号）
  type: flow
  source_pages: p242, p256-271
  source_chapter: How-To / OXE Additional configuration in case of High availability
  source_quote: |
    "Create a discriminator for routing allowed numbers to VAA1 or VAA2 … Discriminator No. 11 - name VAA" (p262)
    "Create two routes, route 1 pointing to the SIP trunk group of the master server and route 2 pointing to the SIP trunk group of the slave server." (p266)
    "Simulate master server failure - Run the command sudo vaa stop or shut down the machine. Call a VAA routing number (ex: 3140X) ­ A short delay may occur on the first call, as OXE will need to determine that the SIP trunk on the master server has been interrupted." (p271)
  summary: |
    九段链：①第二 trunk group 11（SIPVAA2，remote network 11，ABC-F/T2 SIP，直连 RTP 否 + 局部设置与 virtual access 同 f19）；②第二外部网关 3（VAA2：192.168.1.56、5060 UDP、proxy=自身 IP、监督 60、tg 11、incoming username vaa2、None、VAA 类型）；③信任 IP 192.168.1.56；④识别符（Translator/External numbering plan/Numbering discriminator：11/VAA）+ 识别规则（放行 314 开头 5 位号、Zone 1、挂 ARS route list 11）；⑤Entity 挂接——entity 1（分机）与 entity 0（中继）的 discriminator selector 条目 05 填识别符 11；⑥NPD（Numbering Plan Description id 56 名 VAA，NPI/TON ISDN Unknown）；⑦编号命令表——表 10（命令 I=Insert、外部网关 2）与表 11（命令 I、外部网关 3）；⑧ARS——Route list 11（名 VAA）下建 Route 1（名 VAA1：tg 10、NCT 10、NPD 56、quality speech）与 Route 2（名 VAA2：tg 11、NCT 11、NPD 56），Time Based Route List 1（Route 1→VAA1，第二路由 VAA2，成本/等待限 -1）；⑨测试号——ARS 前缀 21（ARS Prof.Trk Grp Seiz.with overlap、识别符 5），Speed dialing 长度 30，直连速拨 31401→呼叫号 2131401（前缀+树号）。测试：master 上 sudo vaa stop（或关机）→拨 3140X——首呼有短暂延迟，随后脚本应从 slave 读出；测完 sudo vaa start。
  conditions: 前提是 OXE 侧 SIP（f19）已通；识别符/ARS/NPD 均为 OXE 侧概念
  tags: [flow, oxe, ha, ars, discriminator, menu-path]

- id: f27
  title: VAA 命令族与维护操作地图
  type: structure
  source_pages: p273-294, p296-299
  source_chapter: MAINTENANCE / CHECK LICENSES … DATABASE AUTOMATIC BACKUP & HIGH AVAILABILITY 命令页
  source_quote: |
    "vaa stop Stop all VAA services except postgresql & nginx / vaa fullstop Stop all VAA services, and also postgresql & nginx / vaa start … vaa restart … vaa status Get status for all VAA services / vaa services … vaa version Get VAA version. Use –d to get details on each component." (p278)
    "sudo vaa ha role … sudo vaa ha ismaster … sudo vaa ha whoismaster … sudo vaa ha listslave … sudo vaa ha addslave @IP … sudo vaa ha removeslave <secondary @IP> … sudo vaa ha resync … sudo vaa ha free" (p243-245, p297-299)
  summary: |
    维护地图七块：①许可——.lic/.vaa 绑 MAC/FQDN，装在 /etc/ale/aa-license-server，问题查 /var/lib/ale/aa-license-server/（FEATURE 项：AAIVR/AAPORTS/ECCSTART/VAA_RELEASE，实验 5 端口 Release 11）；②密码策略（见 principle）；③服务/命令族——vaa stop（留 postgresql+nginx）/fullstop/start/restart/status/services/version(-d)、vaa -h 求助；④日志——Web 界面 Admin/Logs 五类 + 文件系统路径（/logs/aa-media-server/aa-media-server.log、aa-softcmp.log SIP 库、/var/log/ale/tts-hub/ 等，p281）；呼叫日志 CSV 导出（字段 id/caller/tenant/tree/duration/cause/correlatorDataInput/Output/transferredTo 等，p280）；⑤告警——邮件（中继断/恢复、端口到限、许可问题）；SNMP trap 同三类但默认不启用（p282-283）；⑥备份/恢复——Admin 菜单导出（全局 zip 含 wav / 按租户 zip 或 CSV；树可 CSV 导出）+ SSH 命令（vaa db backup/restore、vaa cert backup/restore（nginx 证书目录+nginx.conf+conf.d）、vaa full backup/restore（vaa.conf + secureCall 证书两件））；其他：vaa db reset/purgestats/userreset（超管重置 admin/admin）/sendBackup；⑦自动备份——vaa conf backup 或 Admin/Settings/Backup（名称默认 vaa.tar；Daily 午夜/Weekly 周日/Monthly 首日/自定义 cron；可推 NFS；启用后不可关、无容量监控、6 个月备 20GB 起）。HA 命令族单列（role/ismaster/whoismaster/listslave/addslave/removeslave/resync/free，删 master 角色文件 /var/lib/ale/.master）。
  conditions: 命令需 root 权限（sudo）；细节以安装手册第 6 章 VAA system management 为准
  tags: [structure, maintenance, vaa-commands, backup, logs]

- id: f28
  title: PCS 同步与 OPEX（Purple On Demand）运行模式
  type: flow
  source_pages: p300-305
  source_chapter: PCS SUPPORT & SUPPORT OF OPEX MODE
  source_quote: |
    "sudo vaa conf pcs [IP@] • Main command to configure automatic synchronization of database from primary VAA to VAA PCS … sudo vaa db sendBackup [IP@] • Command … to send automatic backup file to configured target and restore it on remote server" (p303)
    "OPEX oriented license management mechanism based on Purple On Demand offer … OPEX mode uses a pool of licenses for different applications … License items values will be checked every night at midnight, whatever the working mode, CAPEX or OPEX" (p305)
  summary: |
    PCS 同步：vaa conf pcs [IP@] 配置主 VAA→PCS VAA 自动同步（核连接、建 SSH key、未设自动备份时定义每日备份名 Backup4PCS.sql.gz）；vaa db sendBackup [IP@] 发备份到目标并远端恢复（前提：自动备份已设、备份文件已生成、SSH key 已布）；cron 任务每天 01:00 起、第二个 +1 分钟、第三个 +2 分钟依次执行。OPEX：基于 Purple On Demand 的 OPEX 许可管理——VAA 须连云化 OXE 且只关联一个订阅；端口在项目内多应用分摊，须在服务器上声明可用 VAA 端口数；CAPEX/OPEX 两种模式每晚午夜校验许可项。
  conditions: 空间冗余在 Purple On Demand 下不支持（p46）
  tags: [flow, pcs, opex, licensing]

- id: f29
  title: 版本升级流程（手工 + HA 重同步 + S.O.T 自动）
  type: flow
  source_pages: p307-310
  source_chapter: UPDATE VAA VERSION
  source_quote: |
    "First perform a backup of the configuration • /etc/ale/vaa.conf • vaa db backup file.tar or file.sql.gz … Run the script •./install.sh … Warning: VAA 4.8.006: Only a fresh installation followed by a database restoration is supported" (p308)
    "Newer version of the VAA may add new required parameters in the file, so just replacing it by the backup is not advised." (p308)
  summary: |
    手工升级七步：①备份配置（/etc/ale/vaa.conf + vaa db backup）；②下载新发行包与新许可并传服务器；③解压；④./install.sh 重跑；⑤核对 /etc/ale/vaa.conf——新版可能新增参数，不能拿旧备份直接覆盖，逐值比对、改过则 vaa restart；⑥HA 场景所有服务器同法升级后在 master 跑 vaa ha resync 重同步；⑦（可选）S.O.T 自动升级——在项目更新菜单选目标 Boot DVD 与 VAA 版本、提供 admin 密码，核连接后启动。
  conditions: 4.8.006 的升级路径即"全新安装 + 数据库恢复"
  tags: [flow, upgrade, update]

- id: f30
  title: 统计与报告体系（全局/按公司/呼叫日志/邮件周报）
  type: structure
  source_pages: p312-317
  source_chapter: STATISTICS
  source_quote: |
    "The number of calls received • The number of treated calls • The calls released by the caller • The calls lost due to insufficient VAA license port … VAA ports usage (Number of calls being treated/ports being used) • A pie chart: Number of calls transferred, number of 'released by vaa', number of 'released by caller', number of 'insufficient licenses'" (p314)
    "if the administrator selects 'Monday', he will receive the Tuesday at the time defined, the report of the previous day, i.e. Monday." (p317)
  summary: |
    四层：①全局统计（主菜单）与按公司统计（选中公司后）；②报表四指标——收到呼叫数、已处理数、主叫挂断数、许可端口不足丢失数 + 两图（端口占用；饼图：转出/VAA 挂断/主叫挂断/许可不足）；③呼叫日志（Call Logs）逐呼叫明细，点开可见所用节点及各节点时长（排障利器），CSV 字段见 p280；④租户活动邮件报告——xlsx 给管理员（覆盖服务器上全部租户：处理呼叫与逐小时来话图）；开启条件：/etc/ale/vaa.conf 两开关 autogenerateTenantActivityReport 与 autogenerateExcelTenantReport（默认 true），管理员须有 "received activity reports" 权限与有效邮箱，可定发送时间与星期（选 Monday=周二收周一报）。
  conditions: 统计依赖节点命名纪律（p145）；slave 故障期间无统计（p44）
  tags: [structure, statistics, reports]

- id: f31
  title: 外部数据库集成链（JDBC 驱动 → 库连接 → SQL 节点树）
  type: flow
  source_pages: p319-325
  source_chapter: How-To / IVR node - Connect an external SQL database
  source_quote: |
    "By default, only the org.postgresql.Driver and org.mariadb.jdbc.Driver drivers are available and integrated with the VAA. Specific jdbc drivers (MS SQL, Oracle ...) must be downloaded or provided by customer's SGBD administrators." (p320)
    "sudo mv /home/admin/mssql-jdbc-9.4.1.jre8.jar /opt/ale/aa-webapp/lib … It is not possible to make a sftp directly in the directory /opt/ale/aa-webapp/lib … Note: in HA mode, the driver must also be on the slave VAA." (p320)
  summary: |
    三段：①装驱动——默认仅 PostgreSQL/MariaDB 内置；MS SQL（mssql-jdbc-9.4.1.jre8.jar）/Oracle（ojdbc6.jar，jre8 兼容）经 SFTP 传 /home/admin 后 sudo mv 到 /opt/ale/aa-webapp/lib（该目录不能直接 SFTP），sudo systemctl restart aa-webapp 生效；HA 模式两台都要装。②建连接——Tenant/Settings → External Databases 页签 → 加库名 + JDBC URL（MS SQL：jdbc:sqlserver://10.20.30.11:1433;Database=DB_VAA；驱动名 com.microsoft.sqlserver.jdbc.SQLServerDriver；凭证实验 vaa/vaa）→ 连接测试；Oracle 两种连接串（thin:@host:1521:TNS 服务名 vs (description=...service_name=...)）不等价，可能只有一个可用，驱动 oracle.jdbc.driver.OracleDriver。③建树——Start→Welcome→SQL request 节点（SELECT transfertNumber FROM customers WHERE callingNumber='VAR(callingNumber)'，红色输出管 SQL 失败）→ Condition（结果非空才转；空结果不报错）→ Transfer（监督转到库中号码）→ 失败播报→Release；绑 31410 测试。
  conditions: 安全建议库连接定义在公司设置而非节点手工配置（p207）
  tags: [flow, sql, jdbc, integration, menu-path]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-22）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | Pod/OXE 基础准备 | 有 | f02, f03, f17 | POD 拓扑、SIP 模拟器、七步操作流 |
| task-02 | 安装 VAA 应用 | 有 | f18 | 三方式 + 手工装配全流程（含 HA 场景） |
| task-03 | OXE 侧 SIP 对接与验证 | 有 | f19, f20 | 五段配置链 + 测试树四步 + 四层排障 |
| task-04 | 安装 Web 证书 | 有 | f13 | HTTPS/证书体系与 XCA 生成流 |
| task-05 | WebAdmin 初始管理 | 有 | f14 | 管理面分区地图 |
| task-06 | 公司与业务时间/日历 | 有 | f21 | 公司四要素与创建流 |
| task-07 | 提示音与 TTS/ASR | 有 | f22 | 三来源 + 引擎激活流 |
| task-08/09/10 | 三级树设计用例 | 有 | f15, f23 | 原生节点全集 + 三用例递进链 |
| task-11 | 变量与条件 | 有 | f24 | 三类变量 + 实验树流 |
| task-12/13/14/15 | 收号/显示名/HTTP/邮件 | 有 | f16 | IVR 选项节点全集（参数细节在 principle/case） |
| task-16 | VAA HA 部署 | 有 | f25 | 五步流 + HA 命令 |
| task-17 | OXE 侧 HA 配置 | 有 | f07, f08, f26 | HA 机制图 + 冗余用例 + 九段配置链 |
| task-18 | 日常维护 | 有 | f27 | 维护地图七块 |
| task-19 | PCS/OPEX | 有 | f09, f28 | PCS 架构与同步流 + OPEX 模式 |
| task-20 | 升级 | 有 | f29 | 七步升级流 |
| task-21 | 统计报告 | 有 | f30 | 四层统计体系 |
| task-22 | 外部数据库集成 | 有 | f31 | JDBC→连接→SQL 树三段链 |

补充说明：
- f01（全书推进逻辑）、f04（产品定位）、f05（组件族）、f06（架构与呼叫流）、f10（multi-company/N+1）、f11/f12（规格与虚拟化）不直接对应单一 task，属 BOOK_OVERVIEW 骨架 2-3 的概念底座。
- 全部 22 项 task 均有框架类条目覆盖，无空缺；数值类细节（规格表逐格、密码策略、端口/超时值）留待 principle 提取器，本文件只保留结构锚点、菜单路径与命令。
- 生产化边界提示（来自 BOOK_OVERVIEW 批判节）：端口清单与安装细节指向 VAA Installation Guide（4.2/6 章）；multi-company 指向 TBE083 与 OTEC-S 配置指南；路由表达式细节指向 Administration Guide 4.3。
