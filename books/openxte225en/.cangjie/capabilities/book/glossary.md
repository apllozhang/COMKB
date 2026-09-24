# GLOSSARY — OpenTouch 移动与远程办公 术语表

> 阶段 3 产出（源：candidates/glossary.md，62 条，六大域）。
> 口径：定义只采信本书正文；DISA/CTL/CAC/DAS/OTES/SEPLOS/OTMS/OMS/EVS/ACS/DMS/IPG 等缩写书中未给全称，如实标注不补外部知识；CSR/SAN/APNS 以书中展开为准；原文笔误（网关两值、inid.d、otsbx-、https// 缺冒号）见 needs-review nr-01~nr-04。

# OpenTouch 移动与远程办公 (OPENXTE225EN R2.6 Issue 10) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（287 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OpenTouch Suite for MLE | OpenTouch 中大型企业通信套件 | OTMS 管理服务器 + OXE 呼叫服务器 + OmniVista 8770 的组合；本书为其加"远程工作者与移动接入"能力（R2.6/Issue 10） | p1, p3, p31, p33 |
| Remote worker / Remote access | 远程工作者/远程接入 | 员工从互联网全功能接入、外部来宾限会议/Web 协作；客户端侧落地为"接入配置+路由档案"两步 | p33-34, p147 |
| Conversation user | Conversation 用户 | 同一 OTC PC 客户端的两种身份之一：SIP 通信走 OpenTouch SIP 服务器（OTSBC 向导对应 OTCV 组） | p114, p177 |
| Connection user | Connection 用户 | 另一种身份：SIP 通信走 OXE SIP 服务器；智能手机移动化 How-To 全部按此展开（对应 OTCT 组） | p114, p189 |
| Multi-devices | 多设备（副设备） | OTC PC 远程办公新法：把 SIP 分机（实验口径 213100x）绑为副设备，主话机保留 | p151-152, p156 |
| Nomadic / Nomadic SIP | 游牧/SIP 游牧 | 老法仍在：话机从 Deskphone 切到 Personal Computer 后主设备冻结、SIP 软话机顶替；每并发占 1 SIP 设备+1 Ghost Z | p151-152, p157-158 |
| Ghost Z set | 虚拟 Z 设备 | Set Type=Analog+Ghost Z 特性（Nomadic 或 Remote Extension），把打给内部设备的呼叫重定向出去；编号可用 B<数字> | p158-159, p194-195 |
| Remote Extension (RE/REX) | 远程分机 | 经 DISA 公共号码把呼叫引到手机；与主话机构成 tandem；R2.6 起可做用户唯一设备 | p178-182, p192, p204 |
| DISA | 远程分机公共接入机制（全称未展开） | DISA 前缀（实验口径 31280）+公共 DISA 号码+中继组允许+DDI 翻译表落地 | p178, p192-193, p198 |
| Automatic substitution | 自动替代 | 远程分机呼入时用直连速拨号（A<RE 号>）替换主叫呈现；系统级授权 Without code | p192, p195, p208 |
| Tandem (twinset) | 并联结构 | 主话机与远程分机的同组并铃（双方多线 L1/L2）；与呼转是两种机制 | p178, p209 |
| Direct Speed Dialing number | 直连速拨号 | 自动替代占用的速拨号（A<RE 号>）；号段不能为 0、不能满 | p178, p195, p201, p208 |
| DAS rule | 会议接入号码变换规则（全称未展开） | 会议服务器管理台的 s/^ 正则；强制、国家相关、顺序重要、多条可同中 | p67 |
| Fallback mode (DTMF) | DTMF 回落模式 | 无数据连接时靠话音流 DTMF 指令支撑打/挂电话、留言与有限路由 | p166, p175-176 |

## 二、用户角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Corporate user | 公司内部用户 | 有 OpenTouch 账号的员工：远程接入走边缘双件套（RP+OTSBC）或 VPN（技术替代） | p35-36, p40-41 |
| External guest user | 外部来宾 | 伙伴/客户从互联网进会议与 Web 协作（OTC Web/WebRTC）；用例矩阵中该行多为 N.A | p33-35, p42 |

## 三、许可与权利域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Nomadic SIP right | SIP 游牧权利 | 用户级许可：SIP 游牧必须与 Desktop 同时启用 | p161 |
| Desktop license | Desktop 许可 | 用户级许可项：游牧 SIP 场景与 Nomadic SIP 同开（完整能力范围书外） | p161 |
| Off-site mobility right | 场外移动权利 | 使用与 OpenTouch 服务绑定手机的权力；智能手机两种配法都必须勾选 | p178, p198, p203, p206 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OTSBC | OpenTouch 会话边界控制器 | 管理并保护 SIP 会话与 RTP/SRTP 媒体（DoS/拓扑隐藏/TLS/SRTP/CAC/NAT 穿越/紧急路由）；AudioCodes Mediant 承载；7.2 起可内嵌反代 | p35-39, p78-88, p89-117 |
| Reverse Proxy (RP) | 反向代理 | 管理远程客户端到话音 Web 服务的 HTTPS 会话；拓扑隐藏/认证/URL 改写封禁/SSL 卸载；第三方产品，OTSBC 7.2+ 可兼任（认证需另配服务器） | p35-38, p118-130, p131-144 |
| Nginx | Nginx（engine-x） | 独立反代承载：Ubuntu 上三份 conf+snippets；OT 2.2 起 remoteworker.conf 与 conference.conf 必须同改 | p129, p218-259 |
| OTMS | OpenTouch 管理服务器（全称未展开） | 实验"OpenTouch server"的承载虚机（opentouch.company.com，实验口径）；RP 模板的 ot.private-ip 指向它 | p9, p12, p21 |
| OmniVista 8770 | 网管与配置工具 | 全部 OXE/OT 侧申报与 Users 应用、Profiles 的载体；兼任设备管理服务器 DM | p9, p13, p63-77, p151-212 |
| OXE (OmniPCX Enterprise) | 企业呼叫服务器 | 承载编号计划、Ghost Z/SIP 设备/远程分机/tandem/ARS/判别器；智能手机自动对象全部落在 OXE | p9, p14, p152-161, p191-212 |
| Eco-system server | 实验生态服务器 | Windows Server 2016：DNS/Exchange/AD/LDAP/手机 DHCP/证书颁发机构六角色（实验口径） | p9, p19-21, p72 |
| SIP carrier simulator | SIP 运营商模拟器 | 基于 OXE 的出局中继与主叫显示变换（教学专用，行为与真实运营商有差异） | p9, p17, p26-29 |
| OTC PC | PC 全功能软话机 | 含 VoIP/视频；远程接入需 RP+OTSBC；multi-devices 里作 SIP 副设备 | p40, p49, p148, p151-161 |
| OTC PC One | 无 VoIP 的 PC 客户端 | 仅协作：远程接入只需 RP，矩阵中标 N.U.（SBC 用不上，非不支持） | p40, p82, p122 |
| OTC Web / OTC WebRTC | 浏览器两种形态 | OTC Web 协作（仅需 RP）与 OTC WebRTC 音视频（RP+OTSBC）；用邮件里的会议公共 URL 进入 | p40, p42, p149 |
| OTC smartphone (Android/iPhone) | 智能手机客户端家族 | Connection 用户按双模式/单设备配置；关联后自动建 OXE 对象；App 装自 Google Play/App Store | p164-188, p189-217 |
| OpenTouch Conversation Plus (OTC Plus/iPhone+) | iPhone+ 专用应用 | App Store 名 OpenTouch Conversation Plus；VoIP everywhere：SBC 5265、防火墙四端口、APNS 证书年更 | p188, p215-217 |
| APNS | Apple 推送通知服务 | R2.3.1 起 iPhone 的 OT 通知全走它；防火墙放行 TCP 5223/2195/2196/443；证书一年一换（专门 hotfix） | p183-186 |
| kamailio-wasp / wspcfg | iPhone VoIP everywhere 专用组件 | SBC 与 OXE 之间的 SIP 代理+给 kamailio 提供配置的服务；场外 TCP 场景缓冲多 SIP invite | p187, p217 |
| OTES | 旧代远程接入服务器（全称未展开） | OT 2.2 起"不再是方案的一部分"，职能由反代+OTSBC 接管 | p46, p253, p267 |
| WebAdmin | OpenTouch Web 管理界面 | 证书 CSR 生成/导入/部署（System services/Security/Certificate）与 SAN 核验入口 | p49, p54, p71-77 |
| Device Management server (DM) | 设备管理服务器 | OTC PC 软话机从它取 SIP 文件；本书即把 OmniVista 8770 声明为 DM（端口 8080） | p154 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SIP | 场外话音信令协议 | 客户端经 OTSBC 公共 FQDN 注册（TLS 5261/8061/5263 等）；OXE 侧 UDP/TCP 5060 均可（向导只配 UDP，建议补 TCP） | p36-37, p81-86, p104-117 |
| RTP / SRTP / TLS | 媒体与加密口径 | 信令 TLS、媒体 RTP/SRTP；OTSBC Media Realm 划端口段（WAN 侧 SRTP 7000-7499 等，实验口径） | p36, p39, p81, p86 |
| DTMF | 双音多频（全称未展开） | 回落模式的带内控制通道；RE Parameters 可改 DTMF 序列 | p166, p175, p193 |
| LDAP | 目录认证协议 | RP 层认证可接 LDAP/RADIUS；Nginx 路线用 nginx-ldap-auth 模块（Python 2、daemon 8888） | p19, p37-38, p140, p257-259 |
| PKCS7 / PKCS12 | 两种证书封装 | CSR 在本机生成用 PKCS7（只含证书链）；密钥对在 CA 生成用 PKCS12（含私钥带 passphrase） | p54, p56-57, p76, p263 |
| CSR | 证书签名请求 | WebAdmin/OTSBC TLS Context/OpenSSL 生成，同时产生密钥对；生成位置决定封装 | p54-55, p71, p250 |
| SAN | 主题备用名 | 会议 FQDN 必须进 RP 与 OT 证书 SAN；核验入口为证书 Details 页签 | p68-69, p77, p127, p136-137 |
| CTL | 话机侧信任列表（全称未展开） | 预装"通用证书"方案里由通用设备签名；服务器证书变更后必须重新生成（另一培训规程） | p50-51, p268 |
| NAT | 公私网地址映射 | RP/SBC 各一组公私 IP 对+端口与 RTP 段映射；OTSBC 向导以 NAT Public IP 字段录入 | p10, p43, p63-66, p102 |

## 六、站点与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Business Portal | ALE 商务门户 | TC/8AL 文档族、OTSBC OVF 与配置向导软件的下载入口 | p46, p90, p101, p107 |
| TC2639 | 远程工作者/移动化配置更新（第一权威外链） | iPhone 手工配置、RP 模板链接更新、LDAP 细节的生产化必读 | p46, p105, p117, p220 |
| TC2257 / TC1990 | 两代"从零到远程工作者"部署文档 | TC2257 为 OTES 替代版；OTSBC 手工配置补充 | p46, p117 |
| TC2341en | OTC 智能手机 VoIP 部署指南 | businessportal2.alcatel-lucent.com/TC2341en 直达链接 | p217 |
| 8AL90062USAG / 8AL90065USAG | OTSBC 发布说明与配置指南 | OTSBC 手工参数与容量口径的权威外链 | p46, p117 |
| al-mydemo.com | 实验演示公网域 | ot-podx/conf-podx/otsbc-podx 三个公共 FQDN 后缀；对应公网段 195.128.146.10x（实验口径） | p63-77, p90, p220 |
| company.com | 实验内网 DNS 域 | 全部内网主机名后缀与通配符证书 *.company.com 的域（实验口径） | p11, p19-21, p262 |
| eco.company.com/CertSrv | 实验 Windows CA 申请入口 | OT/OTSBC/RP 的 CSR 提交处（advanced、base-64、Web Server 模板） | p72, p98, p137 |
| nginx-ldap-auth | Nginx LDAP 认证开源项目 | github.com/nginxinc/nginx-ldap-auth：Python 2 脚本+init 脚本，daemon 监听 8888 | p257-259 |
| nas.alcatel-support.com（模板下载） | 反代配置模板下载地址 | 书内快照链接；官方明示以 TC2639 最新版链接为准 | p220 |
| RLAB / POD | 培训远程实验室/实验单元 | POD 间独立同构；三种学员接入拓扑；完整虚机与账号表见 book/overview | p4-22 |
