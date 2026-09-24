# Book Overview（参考区）— OXO Connect Starter

> 供能力卡引用的背景参考；源自 references.md 落位。

## 交付主线（课程组织轴）

1. 实验环境
2. 产品与硬件
3. 售前数据采集与两种部署方案
4. 系统开通（FTR/OMC/IP/默认配置）
5. 终端开通（话机/IP-DECT）
6. 编号计划与组
7. 用户功能与语音信箱
8. 公共 SIP 中继与站点业务（消息/呼入/闭锁）
9. 维护与安全（备份/升级/复位/防盗打）
10. Rainbow 混合云集成（接入/RCC/网关/话务台）

（p3-426；p427 后为培训收尾与硬件/启动/向导附注。）

## 实验环境（RLAB，仅 Boundary 背景）

- POD 池相互独立、配置相同；每 POD 一台 Windows 11 客户端虚机（OXOC_PC_CLIENT）+ 一台 OXO Connect Evolution；公共区 10.20.30.x 放 NAS、SIP 模拟器（12.0.0.2）与外部 DNS（p5-13）。
- 实验网段 192.168.1.x：Client PC 192.168.1.10、OXO Eth0 192.168.1.246、OCE Eth1 192.168.94.246、网关 192.168.1.254、DNS1 192.168.1.250、DNS2 10.20.30.250、话机 DHCP 池 .10-.69（p12-13, p44）。
- SIP 运营商模拟器 ITSP1：gateway1.itsp1.com（10.20.30.51）/ public.itsp1.com（10.20.30.50）；SIP 域 sip.itsp1.fr；账号 pbxP/alcatel；号码规则含 POD 号 PN；DDI 41100-41199、话务员 41000、安装号 210P41000（尾段另有 41100 口径，见 needs-review nr-02）（p17-21）。
- 实验账户密码表（p45）：Attendant Letacla1 / Administrator Qwerty12 / Installer Alcatel1 / Download Oxopb123 / NMC Pbxnmc12 / ACD Acdc1064 / Users 142535；OMC 出厂首连 192.168.92.246 + pbxk1064；FTR 首连改密示例 Alcatel1；Webdiag 登录 installer。
- 实验编号：分机 100-104（IPDSP=104）、hunt 501（500 被 VM 占用）、Twinset 副站 130/135、Anydevice 133、广播组号 *2、ARI 11000436010-…60（POD1-6）、DECT PIN/AC 0000、8328 Web Admin admin/admin。
- Rainbow 实验账户：cCpP.admin@ale-training.com / Superuser-P*；培训邮箱 mail44.lwspanel.com（PasswordP*）；培训禁用 PREPAID 订阅（p421）。

## 平台速览（方案沟通素材）

- 产品定位：≤300 用户企业与酒店；OCE（IPBox 纯 IP）与 Compact/Small/Large（PowerCPU EE 混合）四平台；证书认证 RSA 2048/4096 位（p24-26）。
- 话音容量：DSP 通道无子板 16、+Armada32=48、+Armada64=60/76；SIP 并发 IPBox 120、PowerCPU EE+Armada64 76（p37, p201）。
- 交付双路线：Cloud Connect（FTR 自动注册+许可自动下载+Fleet Dashboard）与 Standard（OMC+.msl/.csl 双钥匙）（p51-55）。
- 出局三层：Traffic sharing（占组）→ Barring（表定位）→ 闭锁表（6 张、00 国际默认禁、默认 LC=12）（p271-286）。
- Rainbow 混合云：网关四拓扑——集成 20/OCE-FE 20/外部 50 通话，Rainbow VoIP 用户上限 150（方向性参考带话务前提）（p374, p392）。
- 维护底线：OCE SD 卡 AES 256 恢复仅同主版本；双版本+Swap 可回退；Warm/Cold/Factory 递进删除（p301-324）。

## 教材口径声明

- 全部实验密码/账号/网段仅限实验环境；生产必须替换并做安全加固（原书明文密码遍布正文，引用时一律标"实验口径"）。
- 生产化边界五文档：TC1143（安全加固）、TC1284（SIP 运营商兼容）、TC1994（SIP Profile）、TC2479（Rainbow WebRTC 网关）、Rainbow WebRTC cookbook（OCE-FE 开局，必须最新版）。
- 版本敏感点：WebRTC 自动配置 R4.0.020.002（p366 "from" / p395 "greater than" 双口径，见 needs-review nr-01）；OCE-FE 双端 ≥R4.0 MD；Twinset/Anydevice 副站语义 R5.2/R6.0 分界。
- 原书质量信号：法文残留（p88/p27）、LOLA 无定义（p58/p322）、话务员 DDI 两口径（nr-02）、Circular/Cyclic 并用（nr-03）——细节以最新版英文文档为准。
