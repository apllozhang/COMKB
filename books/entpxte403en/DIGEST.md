# DIGEST — OmniPCX Enterprise SIP 集成长文

> 源：ENTPXTE403EN Edition 12（465 页，OXE R101.1 MD4）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OXE 站点 SIP 化的全局认知；操作细节按需查 13 张能力卡。

## 一、这套东西是什么

OmniPCX Enterprise（OXE）是 ALE 的企业级通信服务器，这本教材教的是把它做成一张"会讲 SIP 的电话系统"：开通三类 SIP 用户（SIP Device 设备、ALE 话机、ALES 软终端），管好设备管理与证书，再经 OTSBC 接通 SIP 运营商、把终端延伸到远程办公。
全程用 sipregister/trkstat/compvisu/oxetrace 等命令行工具闭环验证。

整本教材就是一条交付主线：**内核 SIP 化、终端、运维、出口（外线与远程）**。

四个数字先记住：

| 数字 | 含义 |
|---|---|
| 177 / 345 / 430 | SIP 软件锁三把：用户总数 / 仅 SEPLOS 分机 / 仅 ALE-S 软终端 |
| 15000 / 20000 | 用户上限（单设备或多终端主设备）/ 设备上限 |
| 62 / 992 | SIP 中继组 2 接入=62 路并发；单组上限 992 TS（32×31） |
| ≤500 | 远程用户用 OTSBC 内嵌反代的规模红线，更多转 NGINX PLUS |

## 二、SIP 底座：协议与六组件

- SIP 只管信令：会话的建立/维持/修改/终止，媒体协商靠 SDP、传输靠 RTP——"SIP 不搬语音"是全书反复强调的分界。
- OXE 六组件同栖 sipmotor 进程：本地 SIP 网关（Call Handling 的接口）、SIP 字典（号码↔URL）、代理（路由/权限/改写）、注册器（收注册）、位置服务器（URL→IP）、外部 SIP 网关（对外声明）。
- 注册即服务：注册后才 in service，注销或超时后 IP 置 0.0.0.0、终端 out of service；租期被钳制在 1800 秒到 86400 秒之间。
- 响应码直觉：403 多为认证/互斥拒绝，488 是媒体不可接受（常为法线不匹配），404 找不到用户——排障先分类再进信令。
- 域名是证书地基：默认域名 oxedomain.com 必须改成客户合法注册域名（只能 netadmin 改，管理工具只读）；空间冗余靠节点名 + 内部域名解析器 + DNS 委托，只有 Main 应答。

## 三、SIP 用户两形态与终端三条开通线

形态选错 = 服务等级全错：

| 维度 | SEPLOS（SIP Extension） | SIP Device |
|---|---|---|
| 视角 | 内部话机 | 远端子网设备 |
| 业务 | 前缀/后缀、寻线组、CTI、坐席（按机型） | 五不带：无前缀/后缀、无酒店、无 CTI、无坐席、不入组 |
| 对象 | ALE 话机、ALES 软终端 | 会议话机、门禁、视频设备 |
| 前提 | 子型 + DM profile | 私网 + 私有 SIP 中继组 + 本地网关 |

三条开通线共享"DHCP 拿 DM 地址、拉 DM 配置文件、拉二进制、SIP 注册"四步链：

1. **SIP Device**：基础设施先行（私网/中继组/本地网关），2 接入=62 通道，建户后 sipregister/trkstat 收口；改虚拟接入数必须重启。
2. **ALE 话机**：ALE-2/3 走 DHCP 类 ALE-2X（VCI aledevice），ALE-x00 走 SIP80x8s（ictouch.0）；空间冗余下 TFTP URL 必须用 FQDN；ALE-x00 双分区 Force Download=Yes 后台预载（首次下载可达 30 分钟）才能快切；NOE 转 SIP 有六类禁止场景。
3. **ALES 软终端**：login 必须管理员预建且匹配 LDAP uid（无 auto-discovery）；防隔离 Framework 3 秒/50 条；移动端 Keep Alive=NO 与轮询 ≥21600 秒是推送硬前提；一号多机同型互斥（403 + Warning 399，可 force 抢占，通话中禁抢）。

口令三件别混：auto-discovery 用分机号+用户密码码（默认 0000）；话机高级菜单 123456；DM 下发 admin 密码（实验 2580）。

## 四、设备管理与证书：全站终端的中枢与地基

- **DM 选型**：OXE 自 N1 起自带 SIP DM，只管 8008/ALES/ALE-2/3/30/x00；8770 另管 8088 酒店与停产机型（8001/8018/8028s）。开关是系统参数 "Device Management in 8770"；ALES 恒归 OXE。关 8770 即删其配置文件——迁移是"全站重开"级操作，必须排窗口并备 reset flash 预案。
- **DM profile**：默认 0、上限 100；ALE-S 与 8008 本地/远程一份通吃，ALE-x 系要两份；改 profile 即全量重生成并发 NOTIFY；profile 必须先建后配用户。
- **证书**：安装默认证书只适配 WBM，SIP 客户端必须内部 PKI（或外部 CA）定制——SAN 含 FQDN/通配/物理与角色 IP，密钥默认 4096 位，产物含 CTL（/usr3/mao/DM/VHE8082 下 ctl_VHE8082）。R101.0 起 OpenSSL 安全级 2 拒收 RSA<2048 位或 SHA-1 签名，老话机入网失败先查证书；降级到 1/0 是权宜且必须重启。R101.1 起 mTLS 8443 强下载认证（远程由已知 RP 注入 X-Real-Mac/X-Forward-For）。
- **防火墙信任主机**：一切主动向 CS 发请求的设备（话机/软终端/SBC）都要登记为信任主机，漏配的典型表现是完全无响应——先查 /etc/hosts。

## 五、编解码与排障

- 编解码五层决策链：系统总闸（法线与 G722/OPUS 支持域三档）、IP 域带宽（域内高/跨域低）、DM profile 与用户 SIP profile（最多 5 席，G729 与一份 G711 必选）、终端能力、链路/外部网关联动（OPUS/G722 开必须连带 G711）。系统总闸关了，下层全白开。
- 优先级（高带宽）：OPUS SWB > OPUS WB > G.722 > G.711 > OPUS NB > G.729；法线不匹配直接回 488。
- 排障四件套：状态四查（sipregister/sipdict/sipgateway/trkstat）、motortrace 轻量信令（级别 0-b 十二档）、oxetrace 问题导向采集（自动打包 zip 进 Wireshark）、mtracer/sipdump 深挖（强拆/过滤/许可读数）。恢复首选 dhs3_init -R SIPMOTOR，killall 是 root 级激进手段。

## 六、外线：经 SBC 接通 SIP 运营商

两条腿施工，缺一不通（SBC 没配好前 OXE 外部网关不工作）：

| 腿 | 内容 |
|---|---|
| OXE 侧七件事 | 信任主机（SBC LAN IP）、系统参数、SIP 中继组（T2+SIP）、外部网关（指向 SBC、注册交 SBC、四编解码开关）、ARS（硬前提：前缀/判别器/路由表删加位/时间清单/entity 映射）、DID 翻译与 NPD、回拨翻译 |
| OTSBC 侧 | CLI 初始化、Web 与许可、向导八屏（IP-PBX/SIP TRUNK/SIP ACCOUNT/号码操纵）、重启换 HTTPS 接受通用证书 |

排障三连（先故意失败再修的因果链）：音质降级查 SBC 默认只放行 2 个 coder（补 G729）；呼出被拒查消息域（from/to 的 url.host 改写为运营商域）；来话无声无息查注册（补 Contact User 后 Register，REGISTER 变 podX@域）。

真实运营商参数一切以 TC2005 与运营商文档为准——教材只在 ITSP 模拟器上验证过流程。

## 七、远程办公：两条路与零touch

| 终端 | SBC/RP 路 | VPN 路 |
|---|---|---|
| ALES | RP 拉 DM 配置（内含 SBC 地址 5261）→ 经 SBC 注册 | 第三方 VPN 客户端（ALE 不提供） |
| 话机 | SBC/RP/EDS：LAN↔WAN 搬迁、EDS 零touch | 仅 ALE-2/3（内嵌 OpenVPN，不支持 IPSec） |

- 规模红线：≤500 远程用户用 OTSBC 内嵌反代（TLS 5261 注册、媒体 6000-6399），更多用 NGINX PLUS。
- EDS 零touch：出厂话机联系 device.eds.al-enterprise.com 切 SIP 并取 RP 地址与根证书；四限制（无出向 HTTP 代理、无 802.1x、无 VLAN、暂无 Wi-Fi）售前必须问掉；ALE-2/3 不能动态搬迁，先挂目标位置专用 DM profile。
- 证书五方信任链：话机（Cloud Connect CA 默认在 + SBC/RP CA 经 CTL/EDS）、RP（ALE Terminals CA）、OT SBC（OXE 加密网关 CA）、EDS（还须导 RP CA）、OXE（导 SBC/RP CA 进 CTL）——缺一张断一跳。
- 原生加密：N4 起远程工人可开用户级加密，经 REGISTER Via 头识别、传输模式不一致也放行；SBC LAN IP 清单最多登记 10 个。
- 验收口径：sipregister 里远程用户 contact 指向 SBC LAN 地址，本地用户仍是直连 IP。

## 八、交付红线与速查卡

三条红线：

1. 教材全部密码/账号/号码是 RLAB 实验值（模拟运营商），上生产必须换并以 TC2005/TC2957/Features List 等权威文档为准
2. 版本门槛先核：SSH 自 N3、远程加密放行自 N4、mTLS 8443 自 R101.1、OpenSSL 级 2 自 R101.0、双栈出厂自 R200
3. SIP 侧没有话务台坐席/ACD、酒店仅 8008——需求评审先对齐形态与机型矩阵，别硬承诺

| 要做的事 | 去哪张能力卡 |
|---|---|
| 懂 SIP/改域名/规划冗余 | osip-protocol-foundation |
| 选形态/算容量/选话机 | osip-user-forms |
| 接会议话机/门禁 | osip-sip-device-provisioning |
| 装 ALE 话机/NOE 转 SIP | osip-deskphone-provisioning |
| 配 ALES 软终端/LDAP 认证 | osip-ales-provisioning |
| 配证书/CTL/安全级 | osip-certificate-management |
| 接运营商/部署 OTSBC | osip-otsbc-carrier-interconnect |
| 居家办公/零touch/反代 | osip-remote-workers |
| 编解码/抓包排障/DM/业务特性/实验环境 | 路由入口（oxe-sip-router） |

## 版权

- 本精华长文为 ALE Training Services《OmniPCX Enterprise - SIP》（ENTPXTE403EN Edition 12）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
