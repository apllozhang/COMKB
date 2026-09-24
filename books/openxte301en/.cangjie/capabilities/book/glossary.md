# GLOSSARY — OpenTouch Advanced 术语表

> 阶段 3 产出（源：candidates/glossary.md，58 条，五大域；本门户版精选约 30 条高频术语）。
> 口径：定义只采信本书正文；MLE/OMS/OTMS/DISA/DDI/REX/DTMF/NOE 等缩写书中未给全称，如实标注；p108 "APLLIED"、p371 "Windows 2010" 等为原文笔误。

# OpenTouch Advanced (OPENXTE301EN Ed08) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（468 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Connection user | 绑话机型 OT 用户 | 可享 Deskphone control/Nomadic/Softphone 三模式；nomadic 专属；视频仅限预约会议 | p34, p44, p274 |
| Conversation user | 纯软 OT 用户 | 拥有点对点视频与 ad-hoc 视频能力（Connection 没有）；协作特性全开 | p79, p274, p291 |
| Nomadic mode | 移动模式 | 激活后办公话机冻结，音频改道到家庭/手机号（蜂窝经 Ghost Z）或 PC（VoIP 经 Ghost Z+SIP 设备） | p34-35, p44, p46 |
| Ghost Z set | 虚拟 Z 设备池资源 | 每路蜂窝连接占 1 个、VoIP 占 1 个；连接期间保持 busy 直至关闭 nomadic；按池管理、并发数=池规模 | p39, p46-47, p51 |
| Remote Extension (RE) | 远程扩展 | OTC 智能手机在 OXE 的落地形态，配速拨号实现 DISA 自动替换；R2.6 起可直接作主设备 | p92-94, p134, p137 |
| DISA | 远程扩展公网呼入机制（全称未展开） | DISA 前缀（实验 31280）经 DDI 翻译落地；速拨触发免码自动替换；系统级+中继组级两级授权 | p92, p121-123 |
| Tandem (twinset) | 主话机与远程扩展的绑定结构 | 系统自动创建；两端必须多线设备（至少 L1/L2）；Tandem 目录号=RE 号 | p92, p139 |
| Desksharing (DSU/DSS) | 共享工位 | DSU 无绑定设备（虚拟 MAC=aa:bb+号码 hex）凭 600/601 加密码用任意 DSS（真实 MAC） | p59-61, p64-68 |
| DAS rules | ACS 呼叫路由规则 | 最多 20 条 Unix 正则，按序串行处理所拨号码（输出接输入）；按 Domain 配置、按国家定制 | p108, p299, p317 |
| UDAS | 通用目录访问服务 | 把 OXE 电话簿/OT 内部目录/外部 LDAP 单向同步进 PostgreSQL 同步库；一切搜索查同步库 | p220-223 |
| Single Business Card (SBC) | 目录合并机制 | 按 Synchronization Order 权重合并多目录，Merge keys（至少姓+名）识别同一人；与 OTSBC 缩写撞车 | p226, p252 |
| Impersonation / Delegation | Exchange 代持/委托 | R2.3 起 OT 用 Impersonation（服务账号扮演邮箱所有者）替代 Delegation（逐邮箱委托） | p189-190 |
| Downstream / Upstream | 外部认证两方向 | Downstream=OT 验证用户（LDAP/RADIUS 插件）；Upstream=外部先验、OT 验票据（Kerberos/NTLM V2） | p418, p427 |
| DTA / External login | 内部认证库与外部身份字段 | DTA=默认认证源（外认失败时 Web 客户端级联回落）；External login 与外部唯一 ID 匹配且全局唯一 | p417, p424, p433, p454 |
| Calendar presence / synchro | 日历在场/同步 | presence=日历状态作在场旁注文本（不改颜色码）；synchro=OT 与 Exchange 会议双向同步（OTC 建的周期会议不回推） | p386-392 |

## 二、许可/权限域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Desktop (license) | 桌面客户端许可 | nomadic 激活、Desksharing 远程释放（配 Flex Office）、协作/会议（配 Conferencing）的共同前提 | p46, p49, p54, p72, p340 |
| Nomadic GSM / Nomadic SIP | nomadic 两模式专用权限 | GSM 开蜂窝、SIP 开 VoIP；均须与 Desktop 并用；VoIP 以蜂窝配置为前提 | p47, p49, p51, p54 |
| Off site mobility | 场外移动权限 | OTC 智能手机用户的专用许可；设备关联后必须手动勾选，漏勾手机侧不可用 | p133, p136 |
| Conferencing / Voice mail / Flex Office / OT Applications | 其余功能许可组 | 建会通话/留言功能/远程释放配对/OT 库未知用户兜底 | p72, p204-206, p340 |
| Connection user license 组 | Extended Mobility 成本口径 | Connection 用户许可+universal connection client 许可+REX 资源（GhostZ/IP/DTMF） | p161 |

## 三、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OpenTouch (OTMS) | 协作服务器 | 承载 ACS 协作会议、ICAS 消息、移动性组件、UDAS 与 UM；呼叫控制仍在 OXE（实验实例 192.168.1.50） | p8, p79, p170, p220 |
| OXE (OmniPCX Enterprise) | 企业通信服务器 | 本书宿主 PBX：呼叫控制、话机生态与编号计划（实验实例 OPEN_OXE_ADVANCED，csa/csm） | p8, p29, p38 |
| OmniVista 8770 | 网管/配置平台 | 全书配置操作统一入口（OpenTouch/OXE 配置窗口、Users 应用、WBM 跳转；实验 nms 192.168.1.70） | p8, p105, p123, p313 |
| OTSBC | OT 会话边界控制器 | 远程 OTC 的 SIP 注册（5261）与 WebRTC（8061）入口，媒体段 7000-7499；iPhone+ 另有 5265 专用声明 | p102, p105-107, p332 |
| Reverse Proxy | 反向代理 | DMZ 数据面 https 入口，四个公共 URL（API/EVS:8016/ACS/DMS）在 OT 拓扑声明 | p38, p104-105, p332 |
| ACS | 高级通信服务器（会议服务器） | 会议桥、DAS 规则、电话格式规则、SIP 代理（5060 监听/5260 互连）与管理台所在 | p109, p296, p299, p313-316 |
| AMS | ALE 媒体服务器（内置 MCU） | 多方视频混流点，仅 Active talker 切换（无 continuous presence）；Radvision/LifeSize 已淘汰 | p273, p296 |
| DCS | 文档转换服务器 | 会议 Office 文档演示必需（Basic 只支持 pdf/图片）；内部 KVM 或外部 VM/物理机两形态 | p344, p365-368 |
| Wireal / MASC | UM/日历守护进程 | Wireal 管理与 Exchange 交互（日历同步经 EWS）、MASC 邮件访问组件；service mascd/wireald restart | p215, p391 |
| kamailio-wasp / wspcfg | iPhone VoIP everywhere 组件 | kamailio-wasp=SBC 与 OXE 间 SIP 代理（缓冲 TCP INVITE）、wspcfg=给 kamailio 提供配置 | p101, p147 |
| ICEaccess | Exchange 特权账号 | OT 访问邮箱的 AD 账号（配邮箱、密码永不过期）；授权走 Impersonation（新）或 Delegation（旧） | p180, p184-185, p196 |
| ice_kerb / wbm_admin | Kerberos 账号组 | ice_kerb=OT 专用服务账号（keytab 一致、SPN 两条）；wbm_admin=Kerberos 启用后预留的 WBM 管理 AD 账号 | p436, p448, p452-454 |
| PRS | 呈现服务器 | NOE 终端 Web 应用的强制接入点；话机 Home 页与 Communicate by name 的前提 | p232, p258 |

## 四、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| EWS | Exchange Web Services | UM 邮件存取、日历同步（Wireal）、O365 通知（/ExchangeNotificationService）都基于 EWS over HTTPS 443 | p174, p196, p391 |
| APNS | 苹果推送通知服务 | OT 到 iPhone 通知必经苹果云（TCP 5223/2195/2196/443）；证书一年有效、每年 hotfix | p97-98 |
| Kerberos (KDC/TGT/SPN/keytab) | 上游 SSO 协议族 | Windows 会话凭据换票据、OT 用 keytab 验票；ice_kerb 注册两条 SPN（HTTP/短名与 FQDN） | p427-429, p448, p451 |
| LDAP/LDAPS / RADIUS | 下游认证协议 | LDAP 389（user.uid.attribute 匹配 External login）；RADIUS 1812/1813、pap、shared_secret | p418, p425, p459-460 |
| ARS / Discriminator | 呼出路由选择与识别码 | 智能手机自动生成每用户 ARS 表（Route 1=SIP 设备、Route 2=公网拨手机）；识别码逻辑映射物理 | p92, p128, p140-141 |
| DDI / DID | 外线直拨映射（缩写未展开） | 外线号段映射内线（实验 33210N41000 对 31000，范围 500）；DISA 前缀必须能被 DDI 翻译 | p23, p30, p122 |
| SIP URI (Dial by URI) | 会议 SIP 拨叫入口 | LAN 内任意 H.264 SIP 设备拨 sip:31250@opentouch.company.com 入会；ACS 代理监听 5060 | p279, p295-296 |
| SIP TLS / SRTP | 信令与媒体加密 | 外密内明：远程路径 SIPS/SRTP，OTSBC 为加解密边界 | p38, p332 |
| OAuth 2.0 | Gmail 后端认证协议 | Google Developer Console 一次性建 Client ID/私钥/服务账号；Gmail 上限 500 用户 | p176, p181 |
| DTMF | 双音多频（缩写未展开） | 三处使用：移动 fallback 控制通道、RE 参数序列、会议角色控制码（##1/##3/##4/##91/##92/##93） | p80, p123, p271 |
| NOE / IP-NOE | 话机应用协议族（缩写未展开） | NOE XML 语法的应用开放性；PRS 面向 NOE 兼容终端交付 Web 应用 | p232-233 |

## 五、站点与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| TC2341/TC2391/TC2258/TC2558/TC1623 | 五份 ALE 技术通报 | 智能手机 VoIP 部署/UM 实现/日历在场同步/本地存储邮箱日历/Kerberos 深入——生产化权威依据 | p147, p190, p395, p400, p436 |
| RLAB / POD | 培训远程实验室/实验单元 | POD 池独立同构、共享 NAS 与 SIP 模拟器；全虚拟化与混合课堂两种形态 | p3-18 |
| ITSP1 | SIP 运营商模拟器 | gateway1.itsp1.com+public.itsp1.com（pbxP/alcatel）；号码规则含两位 POD 号 PN | p19-23 |
| ot-podX / conf-podX / otsbc-podX | 实验域名模板 | ot-podX=OT/OTSBC 公共 FQDN；conf-podX=会议专用（须入证书 SAN、内网指 ACS 虚拟 IP） | p104-111 |
| tsa_maintenance | nomadic/Ghost 维护脚本 | OT 服务器 /opt/Alcatel-Lucent/infra_services/ots/ 下；选项 20 dump Nomadic、100/2998 进保护菜单 | p55-57 |
| ALE NFC Extended Mobility | NFC 写卡工具与标签生态 | Google 市场工具（Android R4.2+）；推荐 ALE 标签 Ref 3BA27856AA，自购须 NFC Type 2 且 BP 验证 | p159-160 |
| FreeRADIUS.net 1.0.5 | 实验用 Windows 版 RADIUS | radiusd.conf（UDP 1812）/users/clients.conf 三文件；纯实验工具 | p462-467 |
| My Profile / My Messaging | OT 用户自助 Web 应用 | 改邮箱行为与问候语（须先用话机录）；/MyMessaging 听转留言 | p210-211 |
