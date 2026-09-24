# Book Overview（参考区）— Rainbow OXO Connect

> 供能力卡引用的背景参考；源自 references.md 落位。

## 公司搭建六步主线（交付组织轴）

创建公司 → 开订阅 → 创建并连接 PBX → 搭建 WebRTC 网关 → 创建成员（登录名/号码/订阅）→ 补充管理（监督组/话务台等）（p50）。付费订阅开通与 PBX 创建为 BP 专属。

## 实验环境（RLAB，仅 Boundary 背景）

- POD 池相互独立、配置相同；每 POD 一台 Windows 11 客户端虚机（OXOC_PC_CLIENT）+ 一台 OXO Connect Evolution（p11-16）。
- 实验网段 192.168.1.x：Client PC 192.168.1.10、OXO 192.168.1.246、网关 192.168.1.254、DNS1 192.168.1.250、DNS2 10.20.30.250、话机 DHCP 池 .30-.39（p12, p18-19, p80-82）。
- SIP 运营商模拟器 ITSP1：网关 gateway1.itsp1.com（10.20.30.51）+ 公网网关 public.itsp1.com（10.20.30.50）；账号 pbxP/alcatel；号码规则 33<区域>1PN12345（PN=POD 号两位）；紧急 112/15/17/18；DDI 段 41100-41199、安装号 3321PN41000（p21-26）。
- 客户端预装 4 个 MicroSIP（100-103）+ 2 个公网模拟；主软话机 IPDSP 用 104（p16）。
- 实验账号口径：cCpP.admin@ale-training.com / Superuser-P*（C=班号 P=POD 号）；实验邮箱 mail44.lwspanel.com（PasswordP*）；OMC 出厂首连 192.168.92.246 + pbxk1064；OCE-FE FTR 地址 192.168.94.246、首连密码示例 Alcatel1；Twinset 副站 130/131/135、Anydevice 132/133。
- 培训订阅口径：只用 Voice/Attendant MONTHLY，禁用预付（p66, p176）。

## 平台速览（方案沟通素材）

- Rainbow 定位：UCaaS（协作/云话音/会议）+ CPaaS（开放 API/SDK，developers.openrainbow.com）；混合云集成 OXO/OXE/第三方 PBX（p29-31）。
- 订阅 8 种：Essential（免费无 SLA 无电话）/ Business / Enterprise / Attendant / Enterprise Conference / Conference / Connect（CRM）/ Room（p33）；电话服务必须 Business/Enterprise/Attendant（p65）。
- WebRTC 网关价值：来话按路由档案同振话机与 Rainbow 客户端；去话从 Rainbow 达任意分机或出 PSTN（p119）。
- 容量上限：外部 GW 50 通话；OCE 集成与 FE 20 通话；Rainbow VoIP 用户上限 150（p147）。
- 传输安全：网关到 Rainbow 全程 HTTPS+SRTP（p126）。

## 教材口径声明

- 全部实验密码/账号/网段仅限实验环境；生产必须替换并做安全加固（原书明文密码遍布正文，引用时一律标"实验口径"）。
- 生产化边界三文档：Rainbow Network Requirements PDF（网络数值）、TC2479/TC2462（网关与话务台配置）、Rainbow WebRTC cookbook（OCE-FE 开局场景）——均为原书指定权威来源。
- 版本敏感点：自动配置 R4.0.020.002（p121 "from" / p150 "greater than" 双口径，见 needs-review nr-01）；Anydevice 副站语义 R5.2/R6.0 分界；FE 双端 ≥R4.0 MD。
