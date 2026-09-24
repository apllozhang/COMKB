# Book Overview（参考区）— OmniPCX Enterprise DECT Solutions

> 供能力卡引用的背景参考；源自 references.md 落位。

## 六步交付主线（教学与交付组织轴）

懂底座（频段/复用/帧/标识号码/安全三级）→ 备环境（实验 POD，教学专用）→ 部 8378 IP-xBS（全局参数/DHCP/注册）→ 通同步（内部树/外部同步/Site 组网）→ 交付用户（建户/注册/固件双轨）→ 补支线（混合模式/自动重注册/8328 SIP-DECT）。全书 14 个 How-To 实验按"讲义→实验→命令行输出验证"闭环穿插在这条轴上（p3-298 模块序）。

## 三条产品线速览（方案沟通素材）

| 产品线 | 定位 | 关键口径 |
|---|---|---|
| 8379 IBS | TDM 存量 | 1 PARI/256 台；1/2 条 UA 链路=3/6 通话；无加密；切换限同一网关 |
| 8378 IP-xBS | 全 IP 主线 | 8 PARI/2032 台；每站 11 通话+11 IP 中继；PoE Class 2；OXE R12.2 起 |
| 8328 SIP-DECT | 低成本小站 | 每站 20 只 8214；G.711 10 路/G.729 4 路；仅欧洲频段；双小区才有切换 |

硬数字口径：站间同步门槛 -80dBm；话音门槛 -70dBm（容易）/-60dBm（金属）；同步树最深 24 级；每 PARI 254 台 xBS；混合无法外部同步时区域间距 >1km；重注册 2-3s/机；手机 OTA 理论 6-8 小时/机；8328 双小区链路约 5 分钟。

## 实验环境（RLAB，仅 Boundary 背景）

- POD 池相互独立、配置相同；OXE CSA 物理 192.168.1.1/Main 192.168.1.3、OMS 192.168.1.13、IT SERVER/NTP 192.168.1.252、FlexLM 192.168.1.80、内部 DNS 192.168.1.250、课堂 PC 192.168.1.9（实验口径，p42/p44——p44 表 OXE 地址为点号错位笔误，以 p42 为准）。
- DHCP VLAN1 池 192.168.1.145-155（xBS vendor class alcatel.ipxbs.0）；公共区（10.20.30.x）放 NAS/SIP 模拟器/外部 DNS 10.20.30.250。
- 账号密码（实验口径）：mtcl/Superuser2580*、flex/letacla1、training/superuser、RLAB\Trainee/Superuser1234；xBS WBM engineer/Engineer00!、admin/Admin00!；8328 WBM admin/admin。
- DECT 实验值：AC System=1111；PARI 约定 IBS=100004101x0、xBS=100004101x4（x=POD 号）；分机 31015/31016（GAP+）、31017（GAP）、31040（SIP Extension）；Site 0=BREST、Site 1=BO；混合实验两站间距约 15 米。
- 重注册产物：DECT.txt 传 /tmpd，结果 ReinstallSuccessHandsetsList.txt / ReinstallNOKHandsetsList.txt；手机固件二进制 /usr2/downbin。
- 课堂硬件：IBS 与 xBS 各两台 + 手机（31015/8234、31016/8244、31017/8214、31020/ALE-30h 等，实验口径）。

## 教材口径声明

- 全部实验密码/账号/网段/AC/PARI 仅限实验环境；生产必须替换并做安全加固（原书明文密码遍布正文，引用一律标"实验口径"）。
- 生产化边界四文档：8AL90874USAA（工程规则+勘测手册）、8AL91443ENAA（xBS 排障指南）、8AL91047ENAD（初始配置）、《Getting started with the 8378 DECT IP-xBS solution on OXE》（BP 网站）——均为原书指定权威来源。
- 版本敏感点：OXE 最低 R12.2；基站固件最低 v73b0003；native 加密需 IP-xBS R200；重注册机型版本表（8262 v5580b0007/v5680b0005、8262 Ex v7381b0009、82x4 无最低版本）；IPv6 硬件就绪但暂不适用。
- 数值笔误备查：p44 OXE 地址点号错位（nr-01）；p281/p282 8328 NTP 双例（nr-02）；p182 "bone"笔误与参数名不全（nr-03）；频段双表口径（nr-04）。
