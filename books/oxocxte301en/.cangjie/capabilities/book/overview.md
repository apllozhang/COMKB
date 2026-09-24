# Book Overview（参考区）— OXO Connect Advanced

> 供能力卡引用的背景参考；源自 references.md 落位。

## 全书十段主线（交付组织轴）

实验环境（RLAB+ITSP1）→ OMC 基础 → 公网 SIP 网关 → 酒店与计费垂直 → 终端生态 → 呼叫处理增强（ARS/私网/Internal ARS/多实体/VM/AA/MLAA/SCR/游牧）→ Cloud Connect 云管理 → 安全与证书 → DECT 移动 → Webdiag/noteworthy/LoLa 维护收尾。隐含主线：OMC/Webdiag 双工具 × 编号计划/中继组/ARS 三件套贯穿所有功能（p3-601）。

## 实验环境（RLAB，仅 Boundary 背景）

- POD 池相互独立、配置相同；每 POD 一台 Windows 11 客户端虚机（OXOC_PC_CLIENT）+ 一台 OXO Connect Evolution（p5-13）。
- 实验网段 192.168.1.x：Client PC 192.168.1.10、OXO 192.168.1.246、网关 192.168.1.254、DNS1 192.168.1.250、DNS2 10.20.30.250、话机 DHCP 池 .30-.39（p34 口径；p40 检查清单写 .10-.39，见 nr-02）。
- SIP 运营商模拟器 ITSP1：gateway1.itsp1.com（10.20.30.51）+ public.itsp1.com（10.20.30.50），SIP 域 sip.itsp1.fr；账号 pbxP/alcatel（P=POD 号）；号码规则含 POD 号 PN：安装号 210P41000、DDI 41100-41199、话务台 41000、公网 33{1-5}1PN12345、紧急 112/15/17/18（p16-22）。
- 客户端预装 4 个 MicroSIP（100-103）+2 个公网模拟；主软话机 IPDSP 用 104，安装前必须改 IP 并完成 NTP 时间同步（否则 lanpbx 加载错误，p14）。
- 出厂/实验口令（全部实验口径，生产必改）：OMC 首连 192.168.92.246 + pbxk1064（仅首连）；Webdiag installer 教室例 Alcatel1；OMC 代理参数 OMCAdmin；xBS 网页 admin/00!；实验远程接入码 780911/615243；8088 管理菜单 *tx8000#；DECT 服务菜单 *7378423*。
- 私网组网实验按 POD 号取 N（192.168.N.246），勿与其它 lab 产生 IP 冲突（p208）；多实体链路类别实验值 1/2（讲义示例 3/4，nr-06）；DECT 实验 ARI 示例 110004360P0。

## 平台速览（方案沟通素材）

- 组网三件套：编号计划触发、ARS 表匹配变换、中继组列表按序选路；网关 Media 带宽最少 5 通话是外呼放行闸门（p48/p215）。
- 呼叫处理三层递进：AA（一套树两级）→ MLAA（按 DID/CLI 最多 5 棵 3 级，消息总量 12000 秒）→ SCR（客户码+时间，10000 条规则）。
- 安全生产基线：强制改默认密码 + AutoPwdChk（4 周默认）+ Network IP Services 收敛 + VMU 锁定翻倍封顶 1440 分钟 + 加固清单（总纲 TC1143）。
- 证书与加密：WebDIAG 为证书管理主接口；R6.2 起 OpenSSL V3 + 4K，回滚前必须先经 WebDIAG 切回 2K（p357）；DTLS 只保话机信令不保语音（p353）。
- 云与远程：Cloud Connect 注册自动免 license、Fleet 数据一天一刷新（24h 延迟）；互联网远程入站目标端口永远 50443（p303）。
- 无线：IP 轨 80 xBS/200 手柄（每 xBS 11 并发）、TDM 轨 60 IBS（每 IBS 6 并发）；切换仅同集群内；勘测以 -72 dBm 划语音质量区（p494-495, p533）。

## 教材口径声明

- 全部实验密码/账号/网段/号码仅限实验环境；生产必须替换并做安全加固（原书明文密码遍布正文，引用时一律标"实验口径"）。
- 生产化边界文档：TC1143（安全）、TC1398（noteworthy 清单）、TC2249（密码审计）、TC002_US（V24）、TC2349（WinPDM）、8AL90874USAA（SSK 勘测）、OXO Connect Global Limits、hospitality ecosystem PDF（PMS 清单）、OXO Connect Cross compatibility——均为原书指定权威来源。
- 版本敏感点：4K 证书回滚先切回 2K（R6.2）；8214 仅 R6.0 MD1（R5.2 兼容为 2023 底计划）；8158s/8168s 仅 NOE 模式；DECT 频率页与部分讲义页为 OXE 素材残留（nr-04）。
- 原书内部矛盾：Internal ARS 时段（nr-01）、DHCP 池（nr-02）、门户域名（nr-05）、伪多公司链路类别取值（nr-06）——按 needs-review.md 双口径如实呈现。
