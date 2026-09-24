# Book Overview（参考区）— OmniPCX Enterprise Starter

> 供能力卡引用的背景参考；源自 references.md 落位。

## 课程主线（交付组织轴）

一台 OXE 从"能登录"到"能打电话"，课程主线分四段（p1-821）：

1. 准入链五连：登录加固、系统启停、CS IP 与防火墙、NTP 对时、空库与 OPS 许可
2. 配置域：管理工具 + 三类媒体网关上架 + 用户终端开通
3. 业务域：内部呼叫处理（语音指南/话务台/Entity）；外部互通（公共 SIP 中继/闭锁/紧急）
4. 运维收尾：备份恢复/维护工具/T0T2/UMC

任务-工具对位：库/许可/网络/时间走 swinst+netadmin+CLI，业务走 WBM/mgr，排障走专用命令。

## 实验环境（RLAB，仅 Boundary 背景）

- 每 POD 一台 OXE（ENTP_OXE_EMPTY：物理地址 csa=192.168.1.1、Role 地址 csm=192.168.1.3）+ OMS（192.168.1.13）+ FlexLM（192.168.1.80，端口 27000）+ IT Server（NTP/邮件 192.168.1.252）+ 4 台 PC Client
- 混合模式另有课堂 GD4（192.168.1.12）、话机与 4059EE（p3-20）
- 网络锚点：内部 DNS 192.168.1.250、外部 DNS 10.20.30.250、网关 192.168.1.254、话机静态示例 192.168.1.141、DHCP 池 192.168.1.145-149、动态端口区 10000-10499（p9, p18, p149）。
- ITSP1 SIP 模拟器：网关 gateway1/gateway2.itsp1.com（10.20.30.51/52）+ 公网网关 public.itsp1.com（10.20.30.50）；注册账号 pbxP/alcatel、域 sip.itsp1.fr
- 安装号 3321PN（PN=两位 POD 号）、DDI 段 41000 ↔ 内部 31000、紧急 112/15/17/18（p21-26）
- 实验账号口径：mtcl=Administrator5689!、root/swinst/client=Superuser2580*、FlexLM root=letacla1、GD4 admin/root=letacla1/mg4.ale、OMS 均 letacla1（另有 kb/kb）、GDXL root=mgxl.ale
- 实验账号口径（续）：IT Server=training/superuser、话机初始码 0000、话机 SFTP=admin/*tx8000#（p9, p98, p248, p262, p759）
- 培训约定：空库国家码统一 FR、ISDN 用 ISDN France 变体、抓取前缀 #010/#012、许可文件由讲师发放（TJ00302A 示例）——现场必须按真实环境替换（p190, p784）。

## 系统速览（方案沟通素材）

- OXE 定位：基于 Linux 的软件 PABX；承载四形态=Common HW 机架、虚拟机 OXE-V（VMware/KVM/Hyper-V/Nutanix/AWS）、GAS（Rocky Linux+KVM 一体机）、Crystal（退场中，XL 机架补高密度模拟口）；混装上限每节点 240 racks（p52-80）。
- 容量与限额：单 CS 集中式 15000 用户/240 站点；网络式 100 节点/100000 分机；话务组 ≤50/节点、话务台 ≤250/节点；Entity 0-1000
- 容量与限额（续）：SIP TG 32 接入成对（标准型 62 通道/对，满配 992 并发；Mini 4 通道/对）；4645 7000 信箱/30 端口/500(600) 小时（p37-38, p459, p499, p576, p541）
- 管理工具：WBM（内嵌免费，主力）、mgr（CS 内置文本）、OmniVista 8770（集中管理）、UMC（云侧 R1.1，N3-MD3 起）（p45-47, p226-243, p797-814）。
- 传输安全：原生加密=SRTP（语音）+DTLS（信令），零硬件足迹；OMS 独有 OPUS/G722 编解码（p42, p65）。

## 教材口径声明

- 全部实验密码/账号/网段/号段仅限实验环境；生产必须替换并按客户安全基线加固（原书明文密码遍布正文，引用一律标"实验口径"）。
- 生产化边界文档：TC2005（SIP 运营商参数）、SA0046/TC1774（4645 安全加固）、TC3009（ALE-120/AOM）、ENTPXTE402（Cloud Connect）、Advanced/CPU Loading 课程（组网与 FlexLM）——均为原书指定权威来源。
- 版本敏感点：防火墙 N3 起默认全关（完整 iptables 自 R101.0）；chrony 自 R101；MR3 机架 150W 自 R100.0；OPEX（Purple on Demand）自 R100.1；UMC 自 N3-MD3 且多处 NEXT DELIVERY。
- 实验输出中的"非故障现象"（unknown rack type/BAD PCMS CODE/484 Address Incomplete）判读口径见 needs-review nr-06 与 n43。
