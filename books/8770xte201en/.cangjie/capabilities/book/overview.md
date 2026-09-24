# Book Overview（参考区）— OmniVista 8770 计费与性能管理

> 供能力卡引用的背景参考；源自 references.md 落位。

## 交付主线（组织轴）

1. OXE 侧开计费出票
2. 8770 纳管与增量回收票据入库
3. 配运营商资费算成本
4. 用组织树/掩码/可见域管住"谁能看多少钱"
5. 用报表引擎出账
6. 用 VoIP 性能/流量分析/Tracking/Web Performance 四件套监控质量
7. 归档延长数据寿命（p3-650）

组织树定型放在开闸取票之前（建树期用 Organization update 方法，树建好切 Detailed，p101）。

## 实验环境（RLAB，仅 Boundary 背景）

- POD 池相互独立、配置相同；每 POD 含 OXE（csa 192.168.1.1/csm 192.168.1.3）、OMS（192.168.1.13）、FlexLM（192.168.1.80）、Client PC（192.168.1.10）、OmniVista 8770 服务器（nms 192.168.1.70）；网关 192.168.1.254、DNS 192.168.1.250/10.20.30.250（p47）。
- SIP 运营商模拟器 ITSP1（公共区）：gateway1.itsp1.com 10.20.30.51、public.itsp1.com 10.20.30.50、SIP 域 sip.itsp1.fr、注册账号 pbxP/alcatel；号码含两位 POD 号 PN：公网主号 3321PN12345、安装号 3321PN41000、DID 首外线 33210N41000（p53-58, p84）。
- 实验账号口径：8770 登录 AdminNmc/Superuser01*；OXE root/mtcl/Superuser2580*；FTP 用户 adfexc；cn=directory manager 口令 superuser；教学邮箱 alban.podX@company.com。
- 教学数据：ACCOUNTING_2025.txt 测试票（≥168 张）；税率 US VAT 10%/欧洲 TVA 20%；汇率 1€=1.21$ 或 1$=0.82€（报表实现章用 1.3，书内双口径见 needs-review nr-01）；加载性能实验口径 52 tic/sec（p114）。

## 平台速览（方案沟通素材）

- 8770 定位集中网管：thick client 五套件（Setup/Network/Reporting/Directory/PCX 管理）+ WBM 四应用（Users/Configuration/Performance/Manage My Phone）；审计与流量分析仅 OXE（p10-39, p25/p29）。
- 虚拟化：VMware ESXi 6.x/7.0/8.0、Hyper-V 2016/2019/2022、Nutanix AHV 20220304、AWS；虚拟化不占 8770 许可；选型用 Capacity Planning tool V3.0（p8，Ed45 口径）。
- 兼容矩阵按 8770 版本查列：OXE R12.2-R12.4 全兼容；Purple R101.x 仅 R5.2；OXO Connect R5.2-R6.2 需 R5.1+（p9）。
- 资费模型=Region×Direction→Tariff，成本在加载时算好；费率可精确复算（p117-137）。
- 归档生命周期：31 天归档+94 天清理=最长 125 天，按记录日期清理（p523/p529）。

## 教材口径声明

- 全部实验密码/账号/网段仅限实验环境；生产必须替换并做安全加固（原书明文密码遍布正文，引用时一律标"实验口径"）。
- 生产化边界四块外部输入：真实运营商价目数据工程、MariaDB 容量与备份、SNMPv3/口令生产治理、话务数据法定留存合规——原书只有指针或缺失。
- 书内已知笔误四处（汇率 1.21/1.3、report #4 题面 Telecom 7/0、31011 姓名颠倒、Telecom 2 方向表残留）见 needs-review nr-01~nr-04；成本中心名 MKT 在部分章节写作 Marketing（nr-05）。
