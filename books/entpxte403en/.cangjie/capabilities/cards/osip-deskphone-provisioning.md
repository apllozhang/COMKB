# ALE 话机 SIP 开通与 NOE↔SIP 切换（ALE-2/3、ALE-x00 双分区）

## R — 原文依据

> "1 DHCP request. SIP Phone retrieves the device management application address 2 SIP Phone downloads its configuration file ... 3 SIP Deskphone downloads its binaries ... 4 SIP signaling establishment"（p71）
> "BE AWARE THAT DISABLING THE DM IN THE OMNIVISTA 8770 WILL CAUSE THE REMOVAL OF THE DEVICE CONFIGURATION FILES FROM THE 8770 SERVER ... A RESET FLASH WILL BE MANDATORY ON ALL DEVICES"（p174）
> "From the binary version R200, out-of-the-box Deskphones include both binaries (NOE and SIP) ... 'Download' message means that ... downloading the SIP binaries in background mode (it can take up to 30 minutes the first time)"（p188, p200）
> "ALE-2/ALE-3 devices belong to a DHCP class, named 'ALE-2X' and use a Vendor Class ID (VCI) called 'aledevice'"（p181）

出处：ENTPXTE403EN p71, p172-216。

## I — 自述

SEPLOS 话机入网四步链：DHCP 拿 DM 地址、HTTPS 拉 DM 配置文件（按 MAC）、拉二进制、SIP 注册。两类话机两条施工线：

| 维度 | ALE-2/ALE-3 | ALE-30/ALE-x00 |
|---|---|---|
| DHCP 类/VCI | ALE-2X / aledevice | SIP80x8s / ictouch.0 |
| TFTP URL（无/本地冗余） | https://<OXE Main IP>/dmictouch | 同左 |
| TFTP URL（空间冗余） | 必须 https://<OXE FQDN>/dmictouch | 同左（DNS 可解） |
| 双分区 | 无 | 有（NOE/SIP 各一） |
| NOE↔SIP 切换 | 不适用 | WBM 按钮 / DHCP 批切 / 话机 MMI |
| 远程搬迁 | 不能动态 LAN↔WAN（先换专用 DM profile） | 双栈可即插即迁 |

- 开通六段（两系通用）：①DM 激活（关 "Device Management in 8770" 参数）②SIP Phone COS ③DM profile ④建户（Set Type=SIP Extension + 子型 + DM profile）⑤DHCP（启用 dhcpd、建范围、配类 TFTP URL、Apply Modifications）⑥注册（MAC 手工绑定或 auto-discovery）
- 双分区切换状态图：Force Download NOE/SIP=YES 时对侧二进制后台预载（首次下载可达 30 分钟），切换即快切；=NO 时切换现场下载、明显变慢；R200 起出厂双分区但版本未必最新
- auto-discovery 口令三件（别混）：auto-discovery 认证=分机号+用户密码码（默认 0000）；话机高级菜单=123456；DM profile 下发 admin 密码（实验 2580）

## A1 — 书中案例

**ALE-2/3 开通（31033）**（p172-186，How-To）：

1. WBM 取消勾选 "Device Management In 8770" 激活 OXE DM（存量的先做 reset flash 预案）。
2. 建 DM profile 3：LDAP（ldap://192.168.1.252:389 实验口径）、DNS/SNTP、DTMF、SBC=No、admin 密码与 SSH。
3. 建户：DN=31033、Set type=SIP Extension、Sub type=ALE-2/ALE-3、DM profile=3、Phone COS=0。
4. DHCP：启用 dhcpd、建范围 192.168.1.161-164（实验口径）、ALE-2X 类 TFTP URL=https://<OXE Main IP 或 FQDN>/dmictouch、Apply Modifications。
5. 话机置 DHCP 模式（高级菜单口令 123456）；注册走 MAC 手工绑定或 auto-discovery（31033/0000）。
6. 验证：sipregister 见 31033；nginx access.log 出现 404→401 认证序列与 config.<mac>.xml。

**ALE-300 存量切 SIP（31011）**（p196-216，How-To）：

1. 先给 Phone COS 0 设 Force download NOE/SIP=Yes，话机后台预载 SIP 二进制（Download 约 30 分钟 → Upgrade 数分钟 → 自动重启）。
2. WBM 选 31011 点 "Change NOE to SIP" → OK → 核对子型自动带出、补 DM profile=3。
3. 验证：话机 MMI 显示双版本；access.log 见 PHONE_MODEL=ALE-300 ST=200 与 downbin 请求。

## A2 — 未来触发

使用情境：新站点批量部署 ALE 话机；存量 NOE 话机转 SIP；切换太慢要提速；话机注册不上/拿到旧配置；空间冗余站点配 DHCP 类。

语言信号：ALE-2 / ALE-3 / ALE-300 / ALE-500 / 双分区 / dual partition / Force Download / Change NOE to SIP / sipconfig.txt / aledevice / ictouch.0 / auto-discovery / dmictouch / Apply Modifications。

与相邻能力区分：证书与 SSL 安全级前提找证书管理；DM 选型与 profile 体系找 SIP 设备管理；切到 SIP 后配业务键找 SIP 业务特性；话机搬到员工家找远程办公。

## E — 可执行步骤

输入契约：话机型号清单（是否双栈）、MAC 或 auto-discovery 策略、DHCP 现状（OXE 内部/外部）、冗余模式。老话机证书不达标 → 判停先处理 SSL 级。

1. 核前提：FQDN 已建、证书已生成、CTL 在 /usr3/mao/DM/VHE8082/。完成标准：三件齐
2. 激活 OXE DM：关 "Device Management in 8770"；存量 8770 话机按 reset flash 预案排窗口。完成标准：DM 在 OXE
3. 建 DM profile 与 SIP Phone COS：LDAP/DNS/SNTP/DTMF/话务特性/admin 密码。完成标准：profile 先于用户存在
4. 建户：SIP Extension + 子型 + DM profile + Phone COS；登记防火墙信任主机。完成标准：用户就绪
5. 配 DHCP：启用 dhcpd、建范围、按型号配类（ALE-2X/aledevice 或 SIP80x8s/ictouch.0）与 TFTP URL；空间冗余必须 FQDN。完成标准：Apply Modifications 已点
6. 注册入网：话机 DHCP 模式 → MAC 手工绑定或 auto-discovery（分机号+0000）。完成标准：sipregister 见注册
7. （ALE-x00 切换）预载：COS 设 Force Download=Yes 等后台 Download/Upgrade 完成再切；批量用 DHCP 类挂 sipconfig.txt（前提无其他 NOE 设备，外部 DHCP 加 option 67）。完成标准：切换后 SIP 版本生效

判停点：

- 空间冗余却配了 IP 型 URL → 停，改 FQDN（n10）
- 改了 DHCP 不点 Apply Modifications → 停，进程不读新配置（n11）
- NOE↔SIP 切换对象是远程用户/8770 DM/带 manager-assistant 键/desk sharing/ubiquity/自动话务员/user profile/ACD → 停，六类禁止（n13）
- Force Download=NO 且要白天批量切 → 停，先预载或改夜间窗口（n14）

输出契约：入网注册成功的话机清单 + DHCP 类与 profile 配置台账 + 切换窗口记录。

## B — 边界

- 关 8770 DM 即删其配置文件，全站 SIP 话机丢配置必须 reset flash——迁移是"全站重开"级操作（n08）
- OpenSSL 安全级 2 拒收 RSA<2048 位或 SHA-1 证书，老话机入网前先查证书；降级到 1/0 必须重启且是权宜之计（n09）
- 三个默认口令（0000/123456/2580）全部实验/默认口径，生产必须替换（n12/n50）
- DHCP 批量切 SIP 仅限系统无其他 NOE 设备或外部 DHCP 可设专用类，混存站点用 WBM 逐台（n15）
- ALE-2/3 不能 LAN↔WAN 动态搬迁，必须先挂目标位置专用 DM profile（n38，远程场景详见远程办公卡）
