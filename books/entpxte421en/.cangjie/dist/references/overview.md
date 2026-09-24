# Book Overview（参考区）— OmniPCX Enterprise 加密解决方案

> 供能力卡引用的背景参考；源自 references.md 落位。

## 交付主线（课程组织轴）

交付主线分八段（p4, p111-403）：先证书后开关、先单机后网络，就是实际交付项目的推荐顺序。

1. 密码学/证书基础
2. 证书就位（PKI 模式、CSR、签发、导入、twin）
3. 系统参数与 lanpbx.cfg
4. DTLS/SIP TLS 端点加密
5. 验证排障
6. SIP trunk 中继
7. EEGW/NSP 扩容
8. ABC-F 网络与 mTLS 强化

## 实验环境（RLAB，仅 Boundary 背景）

- 全虚拟化 POD 池相互独立同构；每 POD 两套拓扑：stand-alone（双 CS+OMS+EEGW×2+SBC+远端 PCS）与 ABC-F 网络（NODE1/NODE2+直连链路）（p29-40）。
- stand-alone 网段（实验口径）：CSA 192.168.1.1（角色 .3）、CSB .2、OMS .13、EEGW .7/.8、SBC .105/.205、PCS 192.168.2.5、NTP .252、FlexLM .80、内部 DNS .250、外部 DNS 10.20.30.250；网络线 NODE2 192.168.1.101（角色 .103）（p32-39）。
- 实验口令（生产禁用）：mtcl/swinst/root=Superuser2580*、SBC=Admin/Admin、ALES=alcatel、FlexLM/EEGW 初始=letacla1、话机 tnet 默认 *tx8000#（p34, p135, p279）。
- 号码（实验口径，PN=POD 号）：安装号 3392PN、DID 首外线 33920N31000/首内线 31000/范围 500、SBC NAT=12.班级.POD.105、S.O.T. VM https://192.168.1.194（p43-46, p54-56, p276）。
- 许可实验值：#424=75、#359=30（p129 spadmin 输出）；内嵌 CA 自动生成有效期 7300 天、Root CA CN=CC-suite-ID（p311-312）。

## 方案速览（售前/交付沟通素材）

- 定位：FSNE 纯软件零硬件，加密由 Call Server 强制执行；从大客户可选件转为全体客户原生基线；与 IP Premium Security 不互通（p61-65）。
- 容量分界：内嵌 EGW <1500 并发 DTLS/TLS 会话；EEGW（每 CS 一台 VM）1500-15000；会话公式=受保护端点报价数+3×(GD4/GD-XL/GD3/INTIP3B/OXE-MS)+3×外部 SIP 网关+3×节点数（p63, p77, p109）。
- 协议矩阵：DTLS 1.2（NOE 侧，端口 32643）、TLS 1.2（SIP 侧，5061/6261）、IPSec（ABC-F 节点间，500/2579）、SRTP（媒体，AES-128/256 二选一）（p67-72）。
- 证书体系：全系统一个 CA；端点实体 CN=MAC、CS/PCS CN=FQDN；SAN 按拓扑装配（EEGW 五字段）；工厂证书仅新代板卡/话机/IP-xBS（p78, p85, p206, p344）。
- AES-256 代价：GD4/GD-XL 压缩器 60→45、INTIP3 60→30、GD3 禁用；AES-128-only 设备通话回落明文（p70-72）。

## 教材口径声明

- 全部实验密码/账号/网段/号码仅限实验环境；生产必须替换并做安全加固（原书明文口令遍布正文，引用时一律标"实验口径"）。
- 生产化边界：企业 PKI 运营治理（原书只有概念页）、EEGW VM 规格与压测（Sizing 仅"最大用户数"）、trunk/EEGW 侧抓包位置与 SIP TLS 解密、客户 1024 位设备台账——均以 OXE 安装/维护文档与客户安全策略为准。
- 版本敏感点：R101.0（N3，OpenSSL 3.0 拒收 <2048 位/SHA1）、R101.1（N4，SSL level 可调；INTIP3 AES-256 MD4 起）、R101.2（IP-xBS AES-256 MD2 起）、OXE N5（无 IP SAN，IP-xBS 与 NOE 模式 80x8s 不兼容）。
- 原书笔误备查："Diffie-Helmman"（p7）、"11520-8-N-1"（p367，疑脱漏 0）、"ENCRYTPION"（p247）、ITSP1/2 标签混用（p43-46）——引用按 needs-review.md 标注。
