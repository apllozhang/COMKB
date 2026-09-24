# DIGEST — OmniSwitch LAN Access Switching 精华长文

> 源：DT00XTE215EN Edition 23（587 页）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OmniSwitch R8 接入交换机交付与运维的全局认知；操作细节按需查 13 张能力卡。

## 一、这套东西是什么

OmniSwitch 是 ALE 的企业交换机产品线（Core 的 OS9900/6900、汇聚的 OS6870/6860N、接入的 OS6560/6360 等），本教材讲它们运行 AOS R8 时"从开箱到生产就绪"的全套技能。

整本书是一条交付主线：**登录并加固管理面、快速开局、配置保存/认证/回滚、堆叠与二三层组网、策略与准入、运维周边**。三日议程（p6-8）就是这个顺序：Day1 管理与 VLAN，Day2 冗余与三层，Day3 QoS/ACL/准入/LLDP/PoE；升级、Auto-Fabric、Fleet、OST 为附加模块。

三组数字先记住：

| 数字 | 含义 |
|---|---|
| admin / switch | 出厂默认账号口令；8.10R4 强制改、8.10R04 强制首登改密——存量升级先查这个 |
| working / certified | 配置两目录：write memory 只到启动目录，copy running certified（或 flash-synchro）才固化基线 |
| reload all | 无条件从 certified 启动（强制回滚）；普通重启按"内容相同回 running、不同回 certified"判定 |

## 二、管理接入与开局

- **AAA**：七类服务（console/Telnet/FTP/HTTP/SSH/SNMP/default）各自一条认证链，本地库（admin/default 两用户、上限 64）或 RADIUS/LDAP；exit-on-fail 决定只查第一个还是逐个查。
- **加固四清单**：ASA 限源（≤64 地址）、ip service 禁不安全端口、会话参数（login-attempt/timeout/session-limit）、SSH 强加密（strong-ciphers/strong-hmacs/enforce-pubkey-auth）。禁用 console 前想清楚：全部通道同失即 RMA。
- **会话并发上限**（p80）：Telnet 6、FTP 4、SSH+SFTP 8、HTTP 4、五类总 20、SNMP 50。
- **Lightning Config 开局**：笔记本 DHCP 接端口 1（唯一连线），浏览器 https://192.168.0.1（笔记本会被分到 192.168.0.200/24），RECOMMENDED DEFAULTS 不可跳过，admin 新密码至少 8 位含四类字符且避开 ! 与 $，保存要等绿色提示。六条禁令：不预接线、不连其他交换机、不先接外设、不接 DHCP 服务器、笔记本就绪再上电、不懂 IP 编址就停。

## 三、配置生命周期（防丢配置的核心）

| 动作 | 命令 | 效果 |
|---|---|---|
| 存到启动目录 | write memory | RAM 改动同步 working；状态变 CERTIFY NEEDED |
| 固化回滚基线 | copy running certified | working 覆盖 certified；状态回 CERTIFIED |
| 两步合一 | write memory flash-synchro | VC 下还同步全体成员 |
| 指定目录重启 | reload from <目录> | 从 working/用户目录取回配置 |
| 强制回滚 | reload all | 无论内容是否相同一律回 certified |

排障三问用 show running-directory 一条命令回答：从哪启动（字段一）、是否已认证（CERTIFY NEEDED）、是否已保存（NOT SYNCHRONIZED）。CERTIFY NEEDED 态断电：回 certified 启动，但 working 里的文件还在、可取回。

备份三件套（会话横幅+userTable+vcboot.cfg）打成 tar（上限 10 个）；USB 备份启用后写内存自动同步 /uflash，拔盘前必须 usb disable。

## 四、组网：堆叠、VLAN、冗余、三层

- **Virtual Chassis**：多台经 VFL 合成一台（ISIS-VC 私有协议、免许可、成员间无需 STP/VRRP）。选举四级序=最高优先级（0-255）> 运行时长差 >10 分钟 > 最小 chassis ID > 最小 MAC；MAC retention 恒开，原主恢复不抢回。分裂防护两套：带外 RCD（经 EMP）与带内 VCSP（需 helper）。优先级与 ID 改完必须 reload 生效。
- **VLAN 三入口**：静态成员（VLAN 1 不可删只可禁）、UNP 动态分类（九条规则按编号即优先级，Extended > Binding > Simple）、802.1Q 打标（4096 tag；物理口恒有一个默认 VLAN 未打标桥接）。一个 IP 接口绑定 VLAN 即激活路由；VLAN 无活动成员则网关接口 DOWN、不回 PING、不进路由通告——新建网段后接口 DOWN 首查这个。
- **冗余四件套**：

| 方案 | 一句话 | 关键约束 |
|---|---|---|
| LACP 聚合 | 多链路带宽+成员冗余 | 静态聚合仅 ALE 间；组播默认只走主端口（non-ucast 可改） |
| STP | 防环，默认 per-VLAN | 默认优先级 32768；显式指定根桥；每链路只有一侧 BLK 属正常 |
| DHL | 双上行 VLAN 分流双活 | 1 会话 2 链路；自动禁 STP；恢复默认等 30 秒抢占 |
| VRRP | 网关冗余 | 虚拟 MAC 00-00-5E-00-01-{VRID}、组播 224.0.0.18；改优先级必须先 disable 实例 |

hash 分担出厂默认逐型号不同（9900/6870/6860/6865/6560=extended；6900/6465/6360=brief）——接入层 6360 默认 brief，虚机同源同目的流量会挤一个口。

三层侧：DHCP Relay 全局/接口两型互斥（max hops 16）；Loopback0 永活作管理/协议源（RIP/OSPF 自动通告、BGP 不会）；静态路由默认优于动态，用 metric 做主备默认路由。

## 五、策略、准入与运维

- **策略引擎**：QoS/ACL/PBR/镜像共用 condition+action+rule，qos apply 才下发硬件；不匹配默认放行（accept）。端口默认不信任（tagged 流量的 802.1p 也会被改写为端口默认值），接上游口要 trusted。auto-QoS 按 ALE 话机四个 MAC 段自动给优先级 5。UserPorts 保留组反 IP 欺骗（仅作用路由流量）；qos user-port shutdown bpdu 防私接交换机成环。
- **Access Guardian**：UNP 档案（VLAN+策略列表+位置+时段）由 RADIUS Filter-Id 回传触发；服务器不可达迁 auth-server-down 档案（默认 60 秒重试）；打印机等哑设备无 MAC 登记一律 Block——要么登记、要么走分类规则放行。
- **LLDP-MED 与 PoE**：LLDP 默认双开（30 秒、TTL×4、不支持 linkagg 级配置）；network-policy 下发语音 VLAN 与标记，配 mobile-tag 动态入网。PoE 四档（PD 12.95/25.5/51/71W）；优先级 low/high/critical 定断电顺序；Fast/Perpetual PoE 需型号线且 OS6360-P10A 例外；delayed-start 120-600 秒与 FPoE/PPoE 互斥。
- **运维周边**：诊断八件套（swlog/事件日志/命令日志/镜像/抓包/RMON/health/sFlow）——抓包只存前 64 字节，要完整报文用镜像+外部抓包器；升级取最新 GA/MR（8.10R4 起签名镜像，步骤按 Release Notes），U-boot 密码丢失无恢复、底层固件升级失败即 RMA；Auto-Fabric 七步零触开局（首启提示 Y 才是禁用、N 或不答是启用——语义相反）；Fleet Supervision 免费只读看资产合规；OST 2.0 装机排障（Postgres 18.1 先装、需有效支持合同）。

## 六、三条红线与速查卡

红线：

1. 教材全部实验地址/账号/数值仅限实验，上生产必须换
2. 型号规格（镜像会话数、PoE 预算、VC 上限全矩阵）以 Specification Guide/datasheet 为准，不以记忆值或实验值承诺
3. 升级步骤按 AOS Release Notes；U-boot/底层固件升级失败即 RMA

速查卡：

| 要做的事 | 去哪张能力卡 |
|---|---|
| 登录/加固/账号策略 | swl2-aaa-hardening |
| 新机快速开局 | swl2-lightning-config |
| 保存/回滚/备份 | swl2-config-lifecycle |
| 组堆叠/分裂防护/ISSU | swl2-virtual-chassis |
| VLAN/打标/网关接口 | swl2-vlan-routing |
| 聚合/STP/DHL | swl2-link-redundancy |
| DHCP/Loopback0/VRRP | swl2-l3-services |
| QoS/ACL/防欺骗 | swl2-qos-acl-policy |
| 准入认证/日志/LLDP 与 PoE/升级与零触/资产工具 | 路由入口（omniswitch-lan-access-router） |

## 版权

- 本精华长文为 ALE Training Services《OmniSwitch LAN Access Switching》（DT00XTE215EN Edition 23）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
