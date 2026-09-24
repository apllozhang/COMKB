# 经 SBC 的 SIP 运营商接入（OXE 侧七件事、OTSBC 部署、排障三连）

## R — 原文依据

> "THIS MANAGEMENT MUST BE DONE ACCORDING TO THE SIP PUBLIC PROVIDER REQUESTS! PLEASE CONSULT THE DOCUMENTS (TC 2005, AND ADDITIONAL ONE…) ... AS EACH OPERATOR HAS ITS OWN SPECIFIC PARAMETERS"（p349）
> "Warning ARS IS REQUIRED TO USE SIP TRUNK GROUP WITH AN EXTERNAL SIP GATEWAY"（p355）
> "By default, only 2 coders were configured by the wizard. G729 is not present."（p375）
> "Put the login expected (podX) by the ITSP gateway in the field 'Contact User'"（p382）

出处：ENTPXTE403EN p328-383。

## I — 自述

外线是站点生命线，两条腿施工：OXE 侧七件事 + OTSBC 侧部署调通，缺一不通（SBC 未配好前外部网关不工作）。

| 段 | 配置对象 | 关键口径 |
|---|---|---|
| 1 | 防火墙信任主机 | netadmin 11/1/3/2 加 SBC LAN IP；双机 Copy set up 同步；more /etc/hosts 核对 |
| 2 | 系统参数 | 法线随国家（欧 A/美 μ）；G722/OPUS 支持域是系统总闸，关了网关开了也没用 |
| 3 | SIP 中继组 | T2 + Q931 ISDN all countries + T2 Specification=SIP |
| 4 | 外部 SIP 网关 | Remote domain=SBC 地址、注册与凭据留空交 SBC；四编解码开关（OPUS/G722 开必须连带 G711）；公共中继组只许 Re-INVITE 直连 RTP |
| 5 | ARS | 前缀 0 与逻辑判别器、路由表（删位/加位）、时间路由清单；entity 上逻辑与实际判别器映射，实际判别器必须已存在 |
| 6 | DID/NPD | DID 翻译把外线号段映射回内线；NPD 定主被叫计划（NPI/TON 国际）与默认号；中继组 NPD 选择器绑定 |
| 7 | 回拨翻译 | DEFAULT 表 A33 → 删 3 位加 00（显示可回拨） |
| SBC | OTSBC 四段部署 | VM（OVF/ISO）、CLI 配 LAN 口、Web 与许可、向导八屏加补充配置；重启后 HTTPS 通用证书要手工接受 |

- 向导八屏：WELCOME（模板）、GENERAL（OXE+Generic SIP Trunk+两口）、SYSTEM（HTTPS/Syslog/NTP）、INTERFACES（LAN/WAN/NAT 公网）、IP-PBX、SIP TRUNK、SIP ACCOUNT（Registration 型）、NUMBER MANIPULATION，最后 SUMMARY
- 进出呼叫判定（p330-332）：入向先判 Request URI 域是否本机（OXE_Address/Machine Name/拼接三条件），再按 P-Asserted-ID → From → Via 定来源网关；出向 ARS 选网关后按 NPD 拼号、按网关声明构 INVITE

## A1 — 书中案例

**OXE 侧接入 ITSP2**（p347-363，How-To）：

1. root 进 netadmin 加信任主机 sbc=192.168.1.105（实验口径），Copy set up 同步双机。
2. 建中继组 TG 2（T2、ISDN all countries、Specification=SIP）；建外部网关 3（Remote domain=192.168.1.105、5060/UDP、注册留空、四编解码 Yes）。
3. ARS：前缀 0 → 判别器 0；TG 2 关联网关 3；路由表 9（去 1 位加 33）；0 公共判别器规则（位数 10）；entity 上挂判别器映射（实际判别器须先存在）。
4. DID 翻译（33920x31000 起、范围 1000，实验口径）；NPD 34（ISDN International）；TG 2 的 NPD 选择器=34；回拨 A33 → 删 3 加 00。
5. 验证：sipextgw -l 见网关 3 在服；trkstat -r 2 见 62 路；OTSBC 未配好前对外不可用。

**OTSBC 部署与三连排障**（p364-383，How-To）：

1. CLI 初始化：Admin/Admin 登录，network-if 0 设 LAN IP/网关，write 后 reload now。
2. 向导八屏按实验拓扑填（IP-PBX=OXE 地址、SIP TRUNK=gateway.itsp2.com、账号 podx/alcatel 实验口径），Apply & Reset；重启后接受通用 HTTPS 证书。
3. 排障一：呼出单通 G711——Syslog 见 SBC 只转发 2 coder；Allowed Audio Coders Groups 组 1 补 G729，Apply+Save。
4. 排障二：呼出被 ITSP 拒——From/Authorization 域是 OXE IP；Message Manipulations 改 from/to 的 url.host 为 itsp2.fr 并绑 ITSP IP 组。
5. 排障三：来话无声无息——SBC 未注册成功；Accounts 补 Contact User=podX，Action → Register，REGISTER 变 podX@itsp2.fr 后来话打通。

## A2 — 未来触发

使用情境：站点要接 SIP 运营商（直连或经 SBC）；外线打不出/打不进；音质突然降级；运营商说"你们没注册上"；改域名后外线全断。

语言信号：SIP trunk / SIP 中继组 / 外部 SIP 网关 / External SIP gateway / ARS / 判别器 / discriminator / DID 翻译 / NPD / 回拨翻译 / SBC / OTSBC / 向导 / Contact User / message manipulation / Remote domain / TC2005。

与相邻能力区分：SBC 同时是远程办公底座找远程办公；信令级定位找 SIP 跟踪排障；编解码总闸与协商找编解码卡；防火墙信任主机细则与 SIP Device 开通卡同源规则。

## E — 可执行步骤

输入契约：运营商参数表（TC2005 口径）、SBC 硬件/VM 与许可、号码计划（本局 DID 段）、拓扑（LAN/DMZ/NAT）。运营商参数未拿到 → 判停先要参数，不照书直配。

1. 加信任主机：SBC LAN IP 入 netadmin 防火墙，双机同步，/etc/hosts 核对。完成标准：hosts 有记录
2. 核系统参数：法线、G722/OPUS 支持域（系统总闸）。完成标准：总闸状态明确
3. 建中继组与外部网关：T2+SIP；网关指向 SBC、注册留空（SBC 代注册）、四编解码开关（OPUS/G722 连带 G711）。完成标准：sipextgw -l 在服
4. 配 ARS：前缀/判别器/路由表删加位/时间清单/entity 映射（先建实际判别器再挂映射）。完成标准：出局选路通
5. 配 DID/NPD/回拨：DID 翻译、NPD 计划与默认号、TG NPD 选择器、回拨翻译表。完成标准：来话可定位分机
6. 部署 OTSBC：CLI 初始化、Web 许可、向导八屏、重启接受证书。完成标准：SBC Web 可管
7. 端到端调通：按"编解码放行 → 消息域改写 → Contact User 注册"三连排障，每步以 Syslog 报文收口。完成标准：进出呼 ACK

判停点：

- 运营商参数与教材模拟器口径冲突 → 停，以 TC2005 与运营商文档为准（n28）
- 系统级 G722/OPUS 关着而纠结网关开关 → 停，先开总闸（n29）
- OXE 侧配完就验收 → 停，SBC 侧没好外部网关不工作（n33）
- entity 挂判别器映射时找不到实际判别器 → 停，先建判别器规则（n32）

输出契约：可用的 SIP 中继外线 + OXE/SBC 双侧配置台账 + Syslog 排障证据链。

## B — 边界

- 教材只在 ITSP 模拟器验证过，号码变换/账号/行为全部实验口径；真实运营商的 REGISTER 行为、SIPS 强制、号码格式差异书外（n28/n45）
- 公共中继组（ISDN all countries）只允许直连 RTP，不支持转移与溢出（n31）
- SBC 自身高可用与容量规划书外（AudioCodes 口径）；向导产物全部可手工改但模板时效短（版本提示随 AudioCodes 更新）
- 每个运营商参数不同——任何"照书直配"都要先过运营商参数核对（p349 Warning）
- 实验地址（192.168.1.105、12.C.P2.105、itsp2.fr、podX/alcatel）为实验口径，生产替换
