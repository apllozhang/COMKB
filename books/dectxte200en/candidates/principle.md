# 原则/清单/规则/公式/数值口径候选 — OmniPCX Enterprise DECT Solutions (DECTXTE200EN Ed12)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号、号码）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: DECT 频段按国家划分，共 4 段
  type: metric
  source_pages: p5, p8
  source_chapter: DECT overview / DECT characteristics – Frequency band
  source_quote: |
    "1880 MHz – 1900 MHz European / 1900 MHz – 1920 MHz China / 1910 MHz – 1930 MHz Latin America /
    1920 MHz – 1930 MHz North America" (p5)
    "Europe: 1.88 GHz – 1.90 GHz ... US: 1.92 GHz to 1.93 GHz ... South America: 1.91 GHz to 1.93 GHz
    Except Brazil: 1910 to 1920 MHz ... Asia: 1.90 GHz to 1.906 GHz" (p8)
  summary: |
    频段口径表：欧洲 1880-1900；中国 1900-1920；拉美 1910-1930；北美 1920-1930；巴西例外 1910-1920；亚洲 1900-1906。两个表口径略有交叉（p5 与 p8 各给一版），部署前按国家法规确认。关联硬规则：8328 SIP-DECT 仅支持欧洲频段（p272），基站配置里的 Station base type（如 DECT Europe）必须与所在频段一致（p144/p227）。
  conditions: 部署国家决定 Station base type 与天线/功率合规
  tags: [metric, frequency, regulatory]

- id: p02
  title: DECT 无线物理参数口径（功率/信道/载波/容量密度）
  type: metric
  source_pages: p5, p8, p13, p206
  source_chapter: DECT overview & characteristics / Radio coverage
  source_quote: |
    "High-density traffic (up to 10000 E/Km2)." (p5)
    "Radio power 250 mW ... Channel bandwidth 1,728 MHz ... Transmission carriers 10 ... Carrier
    spacing 2 MHz ... That is, 120 multiplexed radio channels" (p8)
    "The power of the transmitters is constant (around 250 mW) ... Cells may overlap partially or
    totally to increase traffic density ... Non-adjacent cells can use the same channel (frequency +
    timeslot)" (p13)
    "Radio power: 250 mW Pe= 23 dB" (p206)
  summary: |
    物理层口径：发射功率恒定 250mW（Pe=23dB）；信道带宽 1.728MHz；10 个载波（F0-F9）、载波间隔 2MHz；FDMA×TDMA×TDD 合计 120 个复用无线信道；话务密度上限 10000 Erlang/Km²。规划含义：功率恒定→小区大小由环境（墙体/金属/干扰）决定→容量靠小区重叠与非相邻小区频率复用（频率+时隙两级复用）。
  conditions: 环境决定实际覆盖，见 p14 RSSI 门槛
  tags: [metric, radio, planning]

- id: p03
  title: DECT 帧结构数字（10ms/24 时隙/Field A/B 速率）
  type: metric
  source_pages: p8, p11
  source_chapter: DECT characteristics – Time multiplexing / frame structure
  source_quote: |
    "Time multiplexing inside each carrier for IBSs • 6 TSs for reception ... 6 TSs for transmission
    ... for xBSs 12 TSs for reception ... 12 TSs for transmission" (p8)
    "Each DECT frame is 480 bits ... 24 time slots per frame ... Field A: command and signaling
    throughput 6.4 Kbit/s / Field B: voice throughput 32 Kbit/s" (p11)
  summary: |
    帧结构口径：10ms 一帧、480 bits、24 时隙（12 上行+12 下行）；IBS 用收发各 6 时隙（故 3/6 路通话），xBS 用收发各 12 时隙（故 11 路通话+同步保留）；Field A 信令 6.4Kbit/s、Field B 语音 32Kbit/s。理解点：IBS 与 xBS 的容量差异源头就在时隙占用方式。
  conditions: IBS 1/2 条 UA 链路对应 3/6 B 信道（见 p27 容量表与 p219）
  tags: [metric, frame, tdm]

- id: p04
  title: IBS 与 IP-xBS 系统能力对照表
  type: metric
  source_pages: p27
  source_chapter: DECT capacity
  source_quote: |
    "IBS: DECT calls per base station 3 or 6 / Number of PARI 1 / Base station per PARI 256 / Base
    stations supported by a system 256"
    "IP-xBS: DECT calls per base station 11 / Number of PARI 8 / Base station per PARI 254 / Base
    stations supported by a system 2032"
  summary: |
    选型硬表：每基站通话 IBS 3 或 6（1/2 条 UA 链路）vs xBS 11；PARI 数 1 vs 8；每 PARI 基站 256 vs 254；全网基站 256 vs 2032。加上 p195 的混合上限（2032 xBS + 256 IBS 同网），这是产品线选型与站点规模测算的第一张表。
  conditions: 8328 SIP-DECT 另计（20 手机/站，见 p21 相关条目体系之外，p272）
  tags: [metric, capacity, ibs, ip-xbs]

- id: p05
  title: PARI 规则——31 位、11 个八进制位、每类硬件一个 PARI、每节点最多 8 个
  type: rule
  source_pages: p14-15, p82
  source_chapter: Identification numbers / PARI management
  source_quote: |
    "PARI: Primary Access Right Identifier, identification of the PABX, made of 31 bits or 8 hexa
    decimal digits" (p14)
    "A different PARI is mandatory per type of DECT hardware deployed on an OXE • IBS • xBS" (p15)
    "The Call Server can manage several PARI • Up to 8 different PARI" (p82)
  summary: |
    三条 PARI 硬规则：①长度 31 位（8 个十六进制位或 11 个八进制位两种表示）；②同一台 OXE 上 IBS 与 xBS 必须用不同 PARI（混合模式因此至少 2 个 PARI）；③每 OXE 节点最多 8 个 PARI、每 PARI 254 台 xBS。规划动作：先按硬件类型分 PARI，再按规模决定是否一个类型拆多 PARI（>254 台才需要，p106）。
  conditions: 实验 PARI 约定 IBS=100004101x0、xBS=100004101x4（x=平台号，实验口径）
  tags: [rule, pari, planning]

- id: p06
  title: PARK 构成公式与算例
  type: formula
  source_pages: p17
  source_chapter: Identification numbers – PARK
  source_quote: |
    "The PARK is composed of 13 digits • PLI value (2 digits in decimal form) + PARI (11 digits in
    octal form) ... Example: PLI=31 and PARI=10000400100 → PARK=3110000400100"
  summary: |
    公式：PARK = PLI(2 位十进制) ‖ PARI(11 位八进制)，共 13 位。算例：PLI=31、PARI=10000400100 → PARK=3110000400100。PARI 与 PLI 信息在注册阶段由系统发给手机（写 PARK），此后手机用 PARK 与收到的 PARI 比对决定是否锁定。排障用途：由系统 PARI/PLI 可直接推算手机里应存的 PARK。
  conditions: 手机侧不手工输入 PARK；注册时输入的是 PIN 与 AC 码
  tags: [formula, park, pli]

- id: p07
  title: PLI 匹配规则——位数决定兼容 PARI 数，multi-PARI 靠降位
  type: rule
  source_pages: p18-20
  source_chapter: Identification numbers – PLI / Multi PARI
  source_quote: |
    "The PLI determines how many bits, of the PARI received from the base station, must be compared
    to the local PARK • If the PLI is decreased, the handset is compatible with more PARI • Used in
    a Multi PARI configuration" (p18)
    "29 Digits are taken into account" (p20，PLI=29 算例)
  summary: |
    规则：手机把空中收到的 PARI 与本地 PARK 做逻辑 AND，参与比较的位数=PLI。PLI=31 全比（单 PARI）；降到 29 则末 2 位"Don't care"，两个仅末位不同的 PARI（如 10000412340 与 10000412350）对同一手机等效。工程含义：混合部署/扩容时把 PLI 从 31 降到 30 或 29，旧手机无需重注册即可漫游到新 PARI 基站；PLI 选择要"新 PARI 尽量接近旧 PARI"（p254）。原书 WARNING：混合模式（多 PARI）必须适配 PLI（p227）。
  conditions: PLI 修改后已注册手机需重注册或用 -update 推送（见 case c12）
  tags: [rule, pli, multi-pari]

- id: p08
  title: 标识号码位数口径表（RPN/RFPI/IPUI/IPEI）
  type: metric
  source_pages: p14, p21-22
  source_chapter: Identification numbers
  source_quote: |
    "RPN: Radio Part Number: coded in two hexadecimal digits ... RFPI: Radio Fixed Part Identifier,
    identification of the Base station composed of the PARI and of the RPN" (p14)
    "IPUI: International Portable User Identity, identification of the handset international number
    written in the EPROM of the set composed by 14 octal digits" (p21)
  summary: |
    位数口径：RPN 2 个十六进制位（每 PARI 254 台的上限来源）；RFPI=PARI+RPN 由基站广播；IPUI 14 个八进制位、固化在手机 EPROM；IPEI 在 dectrm 输出中出现（如 1410309133756，p176），是手机识别的另一表示。注册核验点：webadmin 的 IPUI N/IPUI O 字段从空到有即为注册成功（p169）。
  conditions: IPEI 与 IPUI 的换算关系书内未给出，不编造
  tags: [metric, identification, ipui, rpn]

- id: p09
  title: 安全密钥规则——AC 注册时比对、UAK 128 位派生、DCK 64 位每呼叫一换
  type: rule
  source_pages: p36
  source_chapter: DECT security – How it works
  source_quote: |
    "This key (128 bits) is called UAK for User Authentication Key. For security reason, it can't be
    broadcasted. ... This value is called AC for Authentication Code. A registration phase isn't
    possible if the AC key used in the PBX is different from the AC key used in the handset" (p36)
    "a special random key (64 bits) is derived from UAK. This key is called DCK for Derived Cipher
    Key. A new DCK is computed at the beginning of each call and is maintained during the whole
    conversation, including conversations with handover(s)." (p36)
  summary: |
    密钥三层规则：AC（鉴权码）双侧共享、注册时手机侧输入比对，不一致则无法注册；UAK（128 位）由 AC 派生，存于手机与系统库，从不上空口/逻辑链路传输；DCK（64 位）每次呼叫开始由 UAK 派生、全程（含切换）保持、不广播不传输。工程含义：AC 码是唯一需要人工管理的秘密（系统 AC System 字段 + 手机注册时输入），改 AC 需重注册；认证级别下自动重注册不重算 UAK（p253）。
  conditions: 加密级别仅 IP-xBS 支持（p37，见 n01）
  tags: [rule, security, ac, uak, dck]

- id: p10
  title: IP-xBS 关键数值口径（11+11 / 12 信道 / 24 级 / 2032 台）
  type: metric
  source_pages: p58, p60, p75, p97
  source_chapter: IP-xBS Overview / Site management
  source_quote: |
    "12 radio channels - 11 simultaneous voice communications" (p58)
    "Up to 2032 Base Stations per OXE node ... 254 bases Stations per PARI ... 8 IP-xBS PARI per OXE
    node" (p60)
    "The maximum of levels in the synchronisation tree is 24" (p75)
    "IP-xBS Base Station supports simultaneoulsly 11 DECT radio communications + 11 IP Relays." (p97)
  summary: |
    容量四口径：每站 12 信道、11 路并发通话；每站同时 11 路 IP 中继（切换时双链路并存，瞬时占用可达 2 份）；同步树最深 24 级；系统级 8 PARI×254=2032 台。话务规划时以"11 通话+切换余量"估单站承载，多站重叠摊薄。
  conditions: 8244/8262 可预留 2 信道做告警（p58），进一步压缩话音容量
  tags: [metric, capacity, ip-xbs]

- id: p11
  title: 位置区（Location Area）数值口径——64 区/PARI、按 RPN 区间划分
  type: metric
  source_pages: p84-85
  source_chapter: Location area management
  source_quote: |
    "Location areas are identified according to base station RPN ... Inside a PARI, up to 64 location
    areas may be defined" (p84)
    "Area RPN: 0 → 1-63 / 1 → 64-127 / 2 → 128-191 / 3 → 192-254" (p85)
  summary: |
    数值口径：每 PARI 最多 64 个位置区；位置区按 RPN 区间映射（示例 4 区：0 区 RPN1-63、1 区 64-127、2 区 128-191、3 区 192-254）。管理员给基站配区号后，系统自动分配该区内的空闲 RPN。用途：高密度安装时按物理区域划分，优化 DECT 终端寻呼搜索范围（Area type 字段）。
  conditions: Area type 配置项 "1 area of 256 xBS" 为默认（p145）
  tags: [metric, location-area, rpn]

- id: p12
  title: Sync Cluster 规则——每 Site/PARI 最多 8 簇、默认 Cluster 0、单站可属 8 簇
  type: rule
  source_pages: p102-104
  source_chapter: Sync Cluster
  source_quote: |
    "Up to 8 Sync Clusters per couple Site/PARI • By default, all base stations belong to Sync
    Cluster 0 ... A base station may belong up to 8 Sync Clusters • Scope of a Sync Cluster is a
    group of base stations defined by the couple Site/PARI ... Only for Special cases when the radio
    coverage is tricky" (p102)
    "when internal synchronization between some bases may not be stable because of a changing radio
    environment" (p103)
  summary: |
    规则三条：①每 Site/PARI 对最多 8 个簇，全部基站默认属 Cluster 0；②单基站可同时属最多 8 个簇（跨簇重叠覆盖）；③簇拆分仅用于特殊场景——站内空中同步因无线环境多变而不稳定时（典型：电梯井分隔楼层，p119 示例）。配置位置：xBS base station 的 Cluster 0-7 复选（p146）。默认部署不动簇。
  conditions: 拆簇代价是簇间无同步→跨簇 handover 受限，谨慎使用
  tags: [rule, sync-cluster, radio]

- id: p13
  title: 外部同步规则——Backup 强制、就近放置、Sync Master 禁载通信
  type: rule
  source_pages: p106, p109
  source_chapter: Multi PARI synchronization / External synchronization
  source_quote: |
    "The selection of the base station used for external synchronization ('Master Sync' and 'External
    Synchronization RPN' is done manually ... The Sync master base station does not support any
    communications ... A backup Sync Master must also be setup and configured" (p106)
    "This Backup Sync Master needs to be placed near to the Sync Master, it must see the same
    External Sync BS ... if the Sync Master fails, the Backup Sync Master will not be able any more
    to support this traffic" (p109)
  summary: |
    外部同步四条硬规则：①Master Sync 与 External Sync RPN 手工指定（非自动选举）；②Sync Master 不承载任何通信（规划时留纯同步站）；③Backup Sync Master 强制配置且必须放 Sync Master 旁边、能看见同一个外部同步源基站；④Backup 可补承 Sync Master 不支持的话务，但主备切换后该话务即失——不能接受时在主备旁再加一台专载话务的 xBS。配置字段见 case c13（Sync Master RPN/Backup RPN 255/External Sync PARI/RPN）。
  conditions: 主备皆失的后果见 n07（无孤岛、无自动恢复）
  tags: [rule, external-synchronization, redundancy]

- id: p14
  title: RSSI 门槛口径——-70dBm 容易 / -60dBm 困难 / -80dBm 站间同步
  type: metric
  source_pages: p207-210
  source_chapter: Coverage and Speech Quality / Coverage and IP-xBS over the air synchronization
  source_quote: |
    "Rs is a distance corresponding to a RSSI level for satisfactory voice quality: -70 dBm (for easy
    coverage) - 60dBm (for tricky coverage)" (p207)
    "-70 dB Minimum RSSI level between and ALE DECT handset and a base station ... Site with no
    coverage problem(s) = Easy • Offices tertiary • Store rooms" (p208)
    "-60 dB ... Site with difficult coverage (Metallic environment) (=Tricky) • Production plant ...
    clean rooms" (p209)
    "-80 dB Zone of quality for DAP synchronization ... Minimum RSSI level between the base stations" (p210)
  summary: |
    三个 RSSI 门槛：手机-基站话音质量门槛——容易场景（写字楼/仓库）-70dBm，金属困难场景（厂房/洁净室）-60dBm；基站-基站空中同步门槛——-80dBm。勘测口径：survey mode 下以对应门槛画覆盖边界（case c09 的 -70dBm 实验）。这两组数字是覆盖验收与同步可行性的最低判据。
  conditions: Rl 距离还取决于手机 RF 灵敏度与环境（p207）；详细勘测方法在 8AL90874USAA
  tags: [metric, rssi, coverage, survey]

- id: p15
  title: xBS 的 DHCP 配置口径——vendor class alcatel.ipxbs.0 与地址池
  type: checklist
  source_pages: p127, p146, p51
  source_chapter: IP Configuration / DHCP Management
  source_quote: |
    "A new Vendor Class has been added in the internal DHCP to provide an ip settings to the xBS" (p127)
    "A range of IP addresses in the internal OXE DHCP server is already managed. ­ Range: 192.168.1.145
    to 192.168.1.155 ... A new Vendor Class for the xBS: Vendor id: alcatel.ipxbs.0" (p146)
  summary: |
    DHCP 清单：内部 DHCP 为 xBS 新增 vendor class，vendor id=alcatel.ipxbs.0；实验地址池 192.168.1.145-155（实验口径）；动态模式下发 IP/掩码/网关/TFTP/DNS，静态模式手工配 IP/掩码/网关/DNS（p126）。外部 DHCP 亦可（p128），但书内只给内部 DHCP 截图——外部 DHCP 需自行实现 vendor class 匹配。文档指针：oxe_p_101.1_sd_InitialConfig_8AL91047ENAD_2_en-1.pdf。
  conditions: 实验口径地址池；生产替换为客户网段
  tags: [checklist, dhcp, ip-xbs]

- id: p16
  title: xBS WBM 访问规则——默认放行、默认口令 Engineer00!/Admin00!、复位入口
  type: rule
  source_pages: p77-78, p145, p148, p161
  source_chapter: xBS base station web based management
  source_quote: |
    "At the first use of an xBS base station, this interface is unlocked by default ... Access
    authorization to web interface, as long as admin password is programmable by OXE management.
    Modifications of the settings of the base station through WBM can be then overwritten by the
    PBX." (p77)
    "xBS WBM engineer password (Default: Engineer00!) / xBS WBM admin password (Default: Admin00!)" (p145)
    "Press the Reset button between 6 seconds and 10 seconds • Browse: http://192.168.0.2" (p78)
  summary: |
    WBM 访问规则：首次使用默认解锁（便于静态组网），之后访问授权与管理口令由 OXE 下发管理；OXE 侧配置项 Allow xBS Web Based Management=YES + 两个默认口令（engineer/Engineer00!、admin/Admin00!，实验口径，生产必须改）；WBM 所做修改可被 PBX 下发覆盖（排障改动可能被冲掉）。无法取 IP 时：按 Reset 6-10 秒回出厂，用出厂地址 http://192.168.0.2 访问。WBM 功能清单：排障、IP 设置、软件更新、空中同步树显示、重启、证书、Syslog、统计、内部设置（p77）。
  conditions: WBM 非日常运维必需（"This interface is not required for normal operations"）
  tags: [rule, wbm, password]

- id: p17
  title: 基站固件升级清单——最低版本 v73b0003、downstat x 菜单、自动复位策略
  type: checklist
  source_pages: p130-132
  source_chapter: Firmware update (xBS)
  source_quote: |
    "Minimum firmware version: v73b0003" (p131)
    "1. Start download of new xBS firmware 2. Send Flash and Reset command to some xBS 3. Restore all
    xBS to legacy mode (no download in background at next startup) 4. Allow new download of xBS in
    DOWNLOAD_FAILED state 0. Exit" (p132)
    "Allow auto. Reset after update: YES → All xBS of a site/pari will automatically reset when
    background download has succeeded for them. NO → The reset will be managed thanks to 'downstat x'
    command" (p132)
  summary: |
    基站固件操作清单：①确认最低固件 v73b0003（downstat x 表头显示 system binary version，如 V0073B0014）；②菜单 1 启动后台下载（downstat x 表格盯 Download status：IN_PROGRESS/READY_TO_FLASH/UP TO DATE）；③全部 READY 后选项 2 下发 Flash and Reset（按 site/pari 选择并二次确认）；④自动复位策略二选一（YES=成功即自动重启；NO=手工控制窗口）；⑤DOWNLOAD_FAILED 用选项 4 重试；升级完成后选项 3 恢复 legacy 模式。
  conditions: 下载不中断业务（旧软件运行中下载到 RAM，p130）
  tags: [checklist, firmware, downstat-x]

- id: p18
  title: Syslog 配置清单——端口 514 与四级日志口径
  type: checklist
  source_pages: p153, p160
  source_chapter: Syslog Server / Collect IP-xBS logs
  source_quote: |
    "It is recommended that you configure the syslog server so that all the xBS logs will be logged
    in a same file. ... Default Syslog server port: 514" (p153)
    "Syslog off: No data is saved ... Normal operation: Normal operation events are logged, incoming
    call, outgoing calls, handset registration, DECT location, and call lost due to busy, critical
    system errors, general system information ... System Analyze: Handset roaming, handset firmware
    updates status ... Debug: Used for troubleshooting. Must not be enabled during normal operation." (p160)
  summary: |
    配置清单：①OXE 侧 PWT/DECT System / xBS system 配 SYSLOG IP+端口（默认 514，实验例 192.168.1.9）；②按基站设 Syslog level 四档：off / Normal operation（呼叫、注册、定位、拥塞丢话、严重错误）/ System Analyze（漫游、手机固件状态，含 Normal 全部）/ Debug（排障专用，禁止常开）；③xBS WBM Syslog 菜单核验下发结果；④服务器侧建议全部 xBS 落同一文件便于关联分析。
  conditions: 系统侧另有 CS embedded syslog 与外部 syslog 两路（p153）
  tags: [checklist, syslog, troubleshooting]

- id: p19
  title: 注册开关规则——全网仅一节点、Default PARI/Area 支持 auto(255)
  type: rule
  source_pages: p147, p247
  source_chapter: IP-xBS registration
  source_quote: |
    "Registration enabled YES ... Parameter used to allow/forbid the automatic registration of new
    IP-xBS. Can be set to True only in one node of a network. • Avoid installation of unwanted
    equipments • Allow installer to change following fields before installing new base stations" (p147)
    "Default PARI for registration ... If set to auto (255), the first PARI, where RPN values are
    available is affected ... If auto mode (255) is set, first free RPN is used. If auto is set for
    default PARI, then auto is also applied for this parameter." (p147)
  summary: |
    注册三条规则：①Registration enabled 全网只能在一个节点为 True（防误收编+允许安装员先改参数）；②Default PARI for registration 可设 auto=255（取第一个有空闲 RPN 的 PARI）；③Default location area 同理 auto=首个空闲 RPN，且 default PARI 为 auto 时本参数强制跟随 auto。安全含义：注册开关平时应关，装站时开——防未授权设备入网。
  conditions: 手动注册（直接录入 MAC@）不依赖该开关，见 p20
  tags: [rule, registration, security]

- id: p20
  title: 换基站用手动注册以保持 RPN（地理定位/告警依赖 RPN）
  type: rule
  source_pages: p150
  source_chapter: Replace an out of service IP-xBS
  source_quote: |
    "The manual registration is recommended when replacing a broken base station by a new one (with a
    new MAC@) When using the automatic registration, the first free RPN will be used and it can be
    different. This could be problematic if alarming and geo localization is used." (p150)
  summary: |
    规则：更换故障基站时走手动注册（删旧 MAC@ → 录新 MAC@ → 原位置名），保持原 RPN 不变；若走自动注册，系统按"首个空闲 RPN"分配，RPN 会漂移——依赖 RPN 的告警与地理定位随之失准。操作序列见 case c05。
  conditions: 先在 OXE DB 删除旧 MAC@（Un-register），再录新 MAC@
  tags: [rule, replacement, rpn, geo-location]

- id: p21
  title: 手机固件 OTA 运行规则——语音优先、充电座切换、6-8 小时、binaries 位置
  type: rule
  source_pages: p179, p181
  source_chapter: FIRMWARE UPGRADE OVER THE AIR
  source_quote: |
    "Only one communication channel can be opened at a time with a handset • The Audio communication
    is preferred over downloading. That means that a software download is stopped during an audio
    communication and will resume later ... The handsets switch on the new downloaded software
    version when they are put on a charger cradle" (p179)
    "The theoretical duration of a download is between 6-8 hours ... When switching on a standby CPU
    all downloads are stopped. The Download Server resumes the downloads but not necessary in the
    same order ... The handset firmware MUST support FWU protocol ... Handsets on visited node in
    case of roaming/campus are not downloaded" (p181)
  summary: |
    OTA 规则五条：①单手机同一时刻仅一条数据信道，语音优先（下载暂停续传）；②并行度由 DECT 应用按话务与在线基站数决定；③新版本在回充电座时才切换生效；④理论单机下载 6-8 小时（计划过夜窗口）；⑤限制——手机固件必须支持 FWU 协议（否则 USB 手动升）、漫游到访问节点的手机不下载、主备 CPU 切换会停止下载且恢复顺序不保证。二进制位置 /usr2/downbin（bin8212/bin8214/bin8232/bin8234_8254/bin8242/bin8244/bin8262/bin8262EX）。
  conditions: 特定机型指定版本用 downstat m b <binary> n <列表>
  tags: [rule, fwu, ota, handsets]

- id: p22
  title: downstat m 状态口径——A/X/M 模式与六态自动化状态机
  type: checklist
  source_pages: p186
  source_chapter: FIRMWARE UPGRADE OVER THE AIR – download status
  source_quote: |
    "A Automatic download: the set is in automatic mode. System automatically updates the set if it
    is not in the current pbx release. X This set is excluded from automatic mode. It will NOT be
    updated by the system. M The set was excluded from the automatic mode. A manual download was
    launched through 'downstat m' menu 4." (p186)
    "IDLE ... ERASE REQUESTED: system asked to the set to prepare the memory flash zone ... telling
    to put the set back on his cradle: 'charger required' ... WRITING ... PAUSED ... WAIT FOR
    FLASHING ... always needs a restart of the set on his cradle ... ERROR: the protocol failed in
    automatic mode & the set will be downloaded again later" (p186)
  summary: |
    状态判读清单：模式三值 A（自动）/X（排除自动）/M（手工经菜单 4 触发）；百分比=进度或 0.0%；状态六值 IDLE → ERASE REQUESTED（提示"charger required"）→ WRITING → PAUSED（暂不可用等待续传）→ WAIT FOR FLASHING（必须回充电座重启生效）→ ERROR（自动模式失败稍后重试）。排障入口：状态栏 QMCDU=分机号、Neqt=设备号、Note 列；手动下载前置条件=用户参数"Exclude from automatic FW update"=Yes（p188）。
  conditions: 全局与单机自动下载开关在 DECT 用户参数页（p182）
  tags: [checklist, downstat-m, firmware, status]

- id: p23
  title: 混合模式 PLI 适配规则——多 PARI 必须降 PLI（实验 30）
  type: rule
  source_pages: p227, p244-245, p265
  source_chapter: IBS deployment / Mixed DECT infrastructure / External synchronization link
  source_quote: |
    "Warning IN CASE OF MIXED MODE, SO WITH MULTI PARI NUMBERS, THE PLI MUST BE ADAPTED." (p227)
    "The PLI value will be 30. With that all DECT users will be able to connect on all DECT base
    stations (xBS & TDM)." (p244)
    "In multi PARI or in mixed mode, the PLI must be adapted" (p245, p265)
  summary: |
    规则：单 PARI 时 PLI=31；一旦混合 IBS+xBS（多 PARI），必须把 PLI 降到能让两个 PARI 在逻辑 AND 下等效的位数——实验口径取 30（IBS PARI 100004101x0 与 xBS PARI 100004101x4 仅末位不同），使全部 DECT 用户可在两类基站间漫游。配套动作：已注册手机用 dectinston -update 推新 PARI/PLI（case c12），或降位后老 PARK 自动兼容（PLI 缩位语义）。
  conditions: PLI 取值前提是新旧 PARI 高位相同；PARI 完全不同时用 -forceUpdate
  tags: [rule, pli, mixed-mode]

- id: p24
  title: 自动重注册性能与安全口径（2-3s/机、paging 1.3-6.5s、UAK 不重算）
  type: metric
  source_pages: p253
  source_chapter: DECT handset automatic re-registration – Performance/Security
  source_quote: |
    "Total duration of a batch of handsets update is proportional to the duration of one set (2 -3s)
    • Paging of the handsets: from 1,3s for a reachable handset to 6,5s for a handset that is out of
    coverage, with default paging configuration (5 paging retransmissions) • Duration of the
    procedure: about 800ms" (p253)
    "The handset remains registered with the same level of security as before applying the tool • In
    case of authentication/ciphering level, the UAK is not computed again. • Keys are never exchanged
    over the air" (p253)
  summary: |
    性能口径：单机全程 2-3 秒（其中 paging 1.3s 可达/6.5s 出覆盖，默认 5 次寻呼重传；过程本体约 800ms），批量时长≈单机×台数。安全口径：安全级别保持不变、UAK 不重算、密钥永不上空口。排产用途：按台数线性估算维护窗口。
  conditions: 出覆盖/关机/漫游到访问节点的手机更新不了（限制见 n11）
  tags: [metric, re-registration, performance]

- id: p25
  title: 自动重注册机型最低固件版本表
  type: metric
  source_pages: p252
  source_chapter: DECT handset automatic re-registration – Supported handsets
  source_quote: |
    "All 82x4 handsets are supported ... Available for IBS and xBS ... Handsets support automatic
    re-registration from version: • 8262 DECT v5580b0007, v5680b0005 • 8262 Ex DECT v7381b0009 •
    8214/8234/8244/8254 DECT No minimum version required" (p252)
  summary: |
    版本表：8214/8234/8244/8254 无最低版本要求；8262 需 v5580b0007 或 v5680b0005；8262 Ex 需 v7381b0009。老版本存量先用 OTA（FWU）或 UST+USB 手动升到位，再跑重注册。前提：手机已在本系统注册且在运行。
  conditions: 82x2 系列不在"all 82x4"口径内（p252 标题即 82x4）
  tags: [metric, version, re-registration]

- id: p26
  title: -update 与 -forceUpdate 决策规则
  type: rule
  source_pages: p254-255
  source_chapter: DECT handset automatic re-registration
  source_quote: |
    "New PARI as close as possible of the existing ones ... PARI and PLI are compatible with the
    existing system, the handset moves to new PARI immediately after ... Use the option '- update'" (p254)
    "When we can't have a new PARI as close as possible of the existing one, we need to change it ...
    automatic re-registration must be done before changing the system PARI. The handsets must be still
    reachable ... the handsets are no longer able to communicate with the system, as soon as they
    receive their new configuration ... The system configuration must be changed only once the maximum
    of handsets have been registered. Handsets for whom the procedure has failed will need manual
    reinstallation" (p255)
  summary: |
    决策规则：新 PARI 与旧 PARI 高位兼容→用 -update（手机立即迁移、业务不断）；PARI 彻底变化→用 -forceUpdate，且顺序铁律：先推新标识、后改系统 PARI（手机收到新配置后即无法与旧系统通信）；执行时手机必须可达；失败手机事后手工重装；批量用 -f 文件（/tmpd，结果落 ReinstallSuccess/NOKHandsetsList.txt，# 开头行为注释，p257）。
  conditions: 命令形态 dectinston -update <dn> -pari <octal> -pli <decimal>（p256）
  tags: [rule, re-registration, update, forceupdate]

- id: p27
  title: IBS 硬件口径——UA 链路=3B 信道、板卡密度表、线缆长度
  type: metric
  source_pages: p219-220, p230
  source_chapter: 8379 DECT IBS / IBS station management
  source_quote: |
    "1 UA link corresponds at 3 B channels available for voice communications • 2 UA link corresponds
    at 6 B channels ... Master link connected on an even port, slave link connected on the next odd
    port ... MIX4/4/8 → 2 ... UAI8, MIX4/8/4 → 4 ... UAI16-1 → 8" (p219)
    "Cable SYT 0.5 mm Max length: 800m ... Cable LY278 0.6 mm Max length: 1200m" (p220)
    "Line delay ... Short line (O-400M) • Medium line (400-800M) • Long line (800-1200M) ... Number
    of UA links Select 1 UA link (3 TS) or 2 UA links (6 TS). The next port address is reserved by
    the system if you select '2'." (p230)
  summary: |
    IBS 硬件口径：1 条 UA 链路=3 个 B 信道（3 路通话），2 条=6 路；主链路接偶数端口、从链路接下一奇数端口（选 2 条时系统自动预留下一端口）；板卡密度 MIX4/4/8=2 站、UAI8 与 MIX4/8/4=4 站、UAI16-1=8 站；线缆 SYT 0.5mm 最长 800m、LY278 0.6mm 最长 1200m，建站时 Line delay 按实际距离三档选（0-400/400-800/800-1200m）。全网仅 1 个 PARI、256 台上限。
  conditions: IBS 2G/1G 代际在建站时选择（p230）
  tags: [metric, ibs, ua-board, wiring]

- id: p28
  title: 8328 SIP-DECT 容量与媒体口径——20 手机/站、G.711 10 路、G.729 4 路
  type: metric
  source_pages: p272
  source_chapter: 8328 SIP-DECT Single Base Station
  source_quote: |
    "Supports up to 20 DECT handsets and, per Base Station with: 10 simultaneous communications using
    G.711 • 4 simultaneous communications using G.729" (p272)
    "8214 DECT handsets only, declared as SIP extension ... Only European DECT frequencies are
    supported (not US ones) ... Base Station powered via PoE ... Web-Based Management (HTTPS)" (p272)
  summary: |
    8328 容量口径：每站最多 20 只 8214 手机；并发通话 G.711 10 路、G.729 4 路（选 G.729 要拿容量换带宽）；仅欧洲频段；仅 PoE 供电；管理走 HTTPS WBM、可导入配置文件快配。定位：小区域、少话务的低成本方案，与 IP-xBS 的 11 路/站不同计量口径。
  conditions: 双小区时两站合计口径书内未单列，按单站×2 估算（推断）
  tags: [metric, sip-dect, capacity]

- id: p29
  title: 8328 部署规则——DHCP 须含非 ALE 设备、NTP mandatory、电话本不集成 OXE
  type: rule
  source_pages: p272-273, p280
  source_chapter: 8328 Topology/Configuration
  source_quote: |
    "Two cells topology: ... Stations located within the same IP subnet • NTP mandatory" (p272)
    "Company phone book can be: Embedded in the base station, as a 'csv' or 'xml' file • Accessible
    via an external LDAP server • No integration with OXE phone book" (p273)
    "Configuration 'DHCP Server' to be active ... Alcatel-Lucent terminals only NO (as the 8328 will
    not be recognized as an ALE device)" (p280)
  summary: |
    部署规则：①OXE DHCP 的"Alcatel-Lucent terminals only"必须设 NO——8328 不被识别为 ALE 设备，否则拿不到地址；②双小区必须同 IP 子网且 NTP 强制；③公司电话本与 OXE 电话本不集成：基站内置 csv/xml 文件或外接 LDAP，查询顺序先本地文件后 LDAP；④建议 DHCP 按 MAC 固定基站 IP 便于 WBM 访问（p280 Tips），或用手机 *47* 搜索基站功能查 IP（p281）。
  conditions: 多站点时每子网各配 DHCP 更简单，或单 DHCP+DHCP relay（p274）
  tags: [rule, sip-dect, dhcp, phonebook]

- id: p30
  title: DECT 维护命令族清单（OXE 通用口径）
  type: checklist
  source_pages: p116, p137-138, p165, p170, p176, p183, p230-234
  source_chapter: Maintenance Tools / 各 How-To 验证命令
  source_quote: |
    "The following tools are adapted to work for xBS in the same way as for IBS: dectview /
    dectinston / dectinfo / dectarea / dectobs / obstraf / ippstat / downstat / Domstat / tftp_check" (p137)
    "Oxe tool: xbssynchro ... Command: incvisu | grep xBS (or 60, 78)" (p116)
    "on CS with root account: tcdump • tcdump –s 0 –w /tmp/filename.cap" (p138)
  summary: |
    命令清单（均在 mtcl 下）：状态查询 dectview xbs/ibs/com（基站表/通话表，含 P/M/B/+/* 标志）、dectinfo（全局信息）、dectarea（位置区）；注册注销 dectinston <dn>|-g / dectrm <dn>；固件 downstat x（基站）/ downstat m（手机）；同步树 xbssynchro（从 Sync Primary 取树，文本输出 RPN+RSSI）；事件 incvisu | grep xBS（或事件码 60/78）；UA 链路 listerm <mg> <cpl>；IBS 详情 listibs p <mg> <cpl> 0 <equip>；重启 outserv/inserv；抓包 tcdump -s 0 -w /tmp/*.cap（root）或 xBS WBM 内 PCAP，导出 Wireshark 过滤 bootp.dhcp/tftp/UA-UDP；tftp_check/Domstat/obstraf/obstraf 辅助。
  conditions: 深度排障文档 im_8378_DECT_IP-xBS_Troubleshooting_Guide_8AL91443ENAA_1_en-1.pdf（p138）
  tags: [checklist, commands, maintenance]
```

## 任务覆盖自检

| BOOK_OVERVIEW task | 对应 principle 条目 |
|---|---|
| task-01 | p01, p02, p03, p05, p06, p07, p08, p09 |
| task-02 | p04, p28 |
| task-03 | 无（实验环境为 How-To 流程，见 case c01/f07） |
| task-04 | p10, p15, p16, p19 |
| task-05 | p20 |
| task-06 | p18 |
| task-07 | p09（AC 口径）|
| task-08 | p08（IPUI 核验口径）|
| task-09 | p17 |
| task-10 | p21, p22 |
| task-11 | p11（位置区）|
| task-12 | p14 |
| task-13 | p27 |
| task-14 | p23 |
| task-15 | p24, p25, p26 |
| task-16 | p13, p12 |
| task-17 | p29 |
| task-18 | p29（同子网+NTP 规则）|
| task-19 | p30 |
| task-20 | p09 |

20 项中 19 项有对应（task-03 为实验环境操作任务，数值口径落在 f07/f08 与 case c01，属预期分工）。
