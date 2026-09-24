# GLOSSARY — Visual Automated Attendant 术语表

> 阶段 3 产出（源：candidates/glossary.md，58 条，六大域）。
> 口径：定义只采信本书正文；PCS/OMS/IPDSP/ITSP/CMIP/DPNSS/TUI/VXML/COS/ANI/Q931/JDBC/SMTP/SNMP/FQDN/MAC/OPEX/CAPEX 等缩写书中未给全称，如实标注；GRUB 口令大小写不一致、URL 笔误见 needs-review nr-01/nr-02。

# Visual Automated Attendant (VSAAXTE001EN Ed20) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（351 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| VAA | Visual Automated Attendant | 跑在 SUSE 上的软件自动话务台/IVR：多租户、SIP 对接 OXE、7×24 呼叫路由与欢迎语，CIS-2 安全标准 | p1, p20-21, p42 |
| Tree | 树（呼叫处理脚本） | 与路由号码绑定的脚本，节点拖拽编排；节点命名进统计与呼叫日志 | p27, p144-145 |
| Node | 节点（积木块） | 原生 12 种 + IVR 选项 9 种（另购许可）；每个节点必须个性化命名 | p27, p144-162, p203 |
| Tenant / Company | 租户/公司 | 多租户配置边界：时区、DDI 段、留言前缀、目录辅助类型、分机位长 | p24-25, p50 |
| Routing number | 路由号码 | DID 与树的绑定条目（需激活）；双层路由缺一不可，推荐一号一树 | p28-29, p111 |
| Prompt | 提示音 | WAV 导入/电话录制/TTS 生成三来源；Announcement 另有 Server file 模式（不推荐） | p28, p34, p138 |
| TTS | 文本转语音 | 内置免费 PicoTTS（六语言，不建议生产）与付费 Google Cloud TTS（生产推荐） | p34, p36, p140-141 |
| ASR | 语音识别 | Google speech-to-text（需账号与 API key）；G729 与 ASR 互斥，要用必须 G711 | p37, p42, p154 |
| Directory / Dial by name | 按姓名拨号目录 | 手工创建或 OXE 电话簿同步（CMIP 链路）；同步是破坏性的 | p33, p42, p156 |
| Filter | 过滤器 | 按主叫号码过滤；CSV 导入清空全部条目；Unknown ANI 可纳入 | p32, p159 |
| Schedule | 日历与营业时间 | 闭假日历（可多日历用于同一树）与营业时间，Schedule 页签或树内节点维护 | p30-31, p135 |
| Master / Slave | 主/从双机 | 库 Master→Slave 复制，Slave 只读无统计；OXE ARS 完成切换 | p44, p47, p240 |
| Reference VAA | 基准机（N+1） | N+1 扩容结构的配置基准；故障期其余照跑但配置冻结 | p51 |
| PCS | 外围站点 VAA（全称未展开） | 中心库周期复制、断网本地接管；应急配置恢复即丢 | p49, p301-303 |
| S.O.T | 软件编排工具（software Orchestration tool） | 自动装系统/配网/改密/装许可/装 VAA；只能自签证书、incoming username 固定 vaa | p76-78, p110 |
| incoming username | 接入用户名 | 安装时定义、必须与 OXE 外部网关一致（无密码、认证 None）；S.O.T 固定 vaa | p81, p101, p109-110 |
| ARS | 自动路由选择（Automatic Route Selection） | OXE 侧路由表，VAA 高可用切换的实际执行者（首呼有判延） | p28, p44, p86, p265-271 |
| Discriminator | 编号识别符 | OXE 编号计划：放行主叫号码并挂 ARS route list（实验 11/VAA） | p262-263 |
| NPD | 编号计划描述（Numbering Plan Description） | 外部来话翻译与去话号码构造（实验 id 56/VAA），被 ARS Route 引用 | p264, p267 |
| Purple On Demand / OPEX / CAPEX | 按用量许可池模式 | 云化 OXE + 单订阅 + 端口分摊；许可每晚午夜校验；不支持空间冗余 | p46, p76, p305 |

## 二、角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Super administrator | 超级管理员 | 可创建公司（数量不限）；管理类角色含公司管理/全量路由/用户管理 | p22, p25-26 |
| Advanced user profile | 受限用户档案 | 只开放管理面局部功能（如问候语控制），可下放给非管理员 | p21, p145 |

## 三、许可体系域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| FlexLM license（.lic / .vaa） | FlexLM 许可文件 | 绑定 MAC 且须含正确 FQDN（换网卡/改主机名失效）；装 /etc/ale/aa-license-server | p95, p249, p274 |
| VAA_RELEASE / Release 11 | 许可版本项 | 4.8.006 强制 Release 11 新许可；排障以 vaa services 运行态为准 | p89, p253, p274 |
| AAIVR / AAPORTS / ECCSTART | FEATURE 许可项 | IVR 功能/端口数/启动项，各带到期日；对应 vaa services 三项输出 | p253, p274 |
| IVR Options | IVR 选项许可 | 解锁 9 种信息系统对接节点；High availability 也列在 Option 栏 | p21, p27, p203 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OXE | OmniPCX Enterprise | ALE 企业级 PBX（对接对象）：保留呼控，经 ABC/F SIP 中继把呼叫交给 VAA | p42-43, p85, p107 |
| OMS | OXE 管理服务器（全称未展开） | 实验拓扑虚机 VSAA_OMS（192.168.1.13） | p7, p9, p65 |
| aa-media-server | 媒体服务 | SIP 连 OXE + RTP 栈 + 跑 VAA 脚本；主日志与 softcmp (SIP) 日志所在 | p54, p277, p281 |
| aa-webapp | Web 应用服务 | Tomcat 承载 aa-management（管理界面）与 aa-engine（VXML server 取脚本）；JDBC 驱动装其 lib | p54, p277, p320 |
| aa-license-server | 许可服务 | FlexLM 许可加载校验；排障目录 /var/lib/ale/aa-license-server/ | p54, p277 |
| tts-hub | TTS/识别接入服务 | TTS 与语音识别服务统一接入；日志 /var/log/ale/tts-hub/ | p54, p132, p281 |
| Nginx | HTTP 反向代理 | 让管理 Web 应用可用；安装期证书放 /etc/nginx/certificate/ | p54, p277, p288 |
| PostgreSQL | PostgreSQL 16 数据库 | 存提示音、路由策略与统计；三级备份与 HA 复制的主体 | p54, p102, p277 |
| SUSE | SUSE Linux（系统底座） | ALE BootDVD 安装，物理机/虚机均可 | p52, p88 |
| XCA | 开源私有 CA 工具 | 实验证书生成（RootCA + VAA 证书，SAN 必填 IP 与 DNS） | p59-60, p123 |
| IPDSP | ALE IP 软话机（全称未展开） | 实验主用软话机（分机 31000） | p10, p66-67 |
| MicroSIP | 第三方 SIP 软话机 | 实验预装：4 内部 + 2 公网模拟 | p10, p67 |
| ITSP1 | SIP 运营商模拟器 | RLAB 公共区模拟运营商（gateway1.itsp1.com，pbxP 账号，号码规则含 POD 号） | p15-17 |
| MS SQL Express / SSMS | 微软免费数据库及管理工具 | 外部库实验用（2019 版）；三默认值陷阱与 ODBC 验证 | p326-329 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SIP trunk（ABC/F） | SIP 中继（ABC/F 型） | T2 中继组、Q931 变体 ABC-F、独立 remote network、直连 RTP 否 | p42, p107-108 |
| G711 / G729 / G723 | 语音编解码 | VAA 支持 G711（aLaw/µLaw）与 G729；G729 与 ASR 互斥；OXE N2 起默认 G729（G723 淘汰） | p42, p101, p113 |
| SIP TLS / SRTP / secureCall | 中继加密（可选） | 激活需双方有效证书；实验一律关闭；vaa full 备份覆盖其两本证书 | p42, p102, p289 |
| HTTPS / TLS 1.2 | 管理面加密 | 4.6.104 起界面仅 HTTPS；证书 PKCS12 与 PEM 两系，放 /tmp 自动识别 | p22, p42, p57 |
| CMIP | 电话簿同步链路（未展开） | VAA 与 OXE 电话簿同步的链路；同步破坏性 | p42 |
| DPNSS | DPNSS 前缀机制（未展开） | 599 前缀路由优化：删旧重建为 "PCX address in DPNSS" 并开 Routing optimization | p112 |
| DDI / DID | 直拨号码（两种拼写同义） | 公司 DID 段界定树号范围（可用内线号）；OXE DID 翻译表映射外线 | p17, p24, p28 |
| WAV（8KHz PCM 16-bits mono） | 提示音格式 | 三硬约束 + 名称无空格；多语言语言选择前提示必须双语同文件 | p34, p138, p187-188 |
| JSON | JSON 数据格式 | HTTP 节点返回载体；VAR(变量.对象.字段) 点语法取值 | p232-233 |
| JDBC / SQL | 数据库接入技术 | 默认内置 PostgreSQL/MariaDB 驱动；SQL 节点单字段、首条、空结果不算错 | p207-208, p320, p322 |
| SMTP / SNMP | 告警通道 | 邮件三类事件；SNMP trap 同类但默认不启用；SMTP 改后必重启 | p101, p130, p282 |
| PKCS12 / PEM / SAN / X.509 / PKI | 证书族术语 | 格式两系；SAN 必须含 VAA IP 与 DNS；CN 必填 | p57, p59-60 |

## 六、文档与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| MyPortal | ALE 客户服务门户 | VAA 文档/发行包/BootDVD 下载入口 | p76, p95 |
| RLAB / POD | 培训远程实验室/实验单元 | 纯虚拟化、POD 间独立同构、共享公共资源区（NAS/SIP 模拟器/SQL/Mail） | p5-13 |
| ALE BootDVD | ALE 系统安装介质 | 启动选 VAA 与版本自动装 SUSE；S.O.T 与手工安装的共同起点 | p76, p80, p88, p95 |
| TBE083 | OXE 多公司特性文档 | multi-company 集成权威文档 | p50 |
| OTEC-S VAA configuration Guide | VAA 配置指南 | multi-company 场景的配置细节所在 | p50 |
| VAA Installation Guide / Administration Guide | 安装指南/管理指南 | 完整安装（4.2）、公网证书（6.4）、系统管理（第 6 章）；路由表达式（4.3）、TTS（第 10 章） | p29, p53, p61, p78, p141, p277 |
| ALE Knowledge Hub | ALE 培训平台 | 在线评估与证书下载、课程目录（培训收尾专用） | p347, p351 |
