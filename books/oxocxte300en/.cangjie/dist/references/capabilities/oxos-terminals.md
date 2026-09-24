# 终端开通（IP 话机 / IP-DECT / SIP-DECT）

## R — 原文依据

> "Enable « auto provision » in the Subscribers/Base stations list to allow IP devices to register onto the OXO Connect"（p107）
> "There are 2 modes for Dynamic: Dynamic and Dynamic Alcatel."（p116）
> "Enter the ARI number (11 digits in octal) … 11000436010 for POD 1"（p119，实验口径）
> "The factory IP configuration of an 8328 base station is a dynamic IP configuration. Therefore, a DHCP server must be present"（p455）

出处：OXOCXTE300EN p106-122（IP 话机与 IP-DECT 实验），p453-465（8328+8214 实验）。

## I — 自述

终端开通三条线，共用一个前置开关：

- **前置**：OMC/Subscribers BaseStations list 启用 Auto-Provision（可临时启用）+ DHCP 池就绪——教材三处 IMPORTANT 反复强调"别忘开"，终端不上线先查它（n05）
- **IP 话机静态**：话机启动 2/5 或 3/5 阶段按 * 和 # 进配置，IPv4 Static 填地址、填 NOE 管理密码，TFTP1 指向 OXO 地址 → 重启后系统自动分配目录号
- **IP 话机动态**：话机选 Dynamic（任意 DHCP 服务器）或 Dynamic Alcatel（只接受 OXO 分配）——两者语义不同，客户网已有 DHCP 时选错会拿不到地址（n06）
- **IP-DECT xBS（8378）**：OXO 侧输 ARI（11 位八进制，IBS 与 IP-DECT 通用，唯一值取自 eBuy）绑定系统；基站 PoE 上电看 LED 六步（红三步、橙三步、绿 1s 亮 1s 灭=存活）；建话机后 GAP 注册（IPUI 出现后 Assign）
- **SIP-DECT（8328+8214）**：8328 出厂动态 IP，Web Admin（admin/admin）把 OXO 声明为 SIP 服务器；OXO 侧建 Open SIP Phone 分机并置旗标 no_pack_support_for_siphone=true；话机 Auto Install 注册（PIN/AC 默认 0000）后做分机声明
- **模拟设备**：经 MEDIA5 FXS 网关接入 OCE，每模拟口耗 1 UTL+1 Open SIP 许可（f46）

## A1 — 书中案例

**IP 话机动态模式实验**（p106-116）：

1. OMC/Hardware and limits/LAN/IP Configuration/DHCP：池 192.168.1.10-39（实验口径）
2. Subscribers BaseStations list：启用 Auto-Provision
3. 话机断电重上电，启动 2/5 阶段同时按 * 和 #
4. IPv4 wired → Network Settings，选 Dynamic 后校验退出
5. 验收：话机重启后 OXO 自动分配目录号码，"The deskphone is now in service"

**IP-DECT xBS 实验**（p117-122）：

1. 内置 DHCP 启用（池 .10-.30），确认配置并做 warm reset
2. 别忘了激活 Autoprovision（p118 原文为法文 IMPORTANT）
3. OMC/Dect/DECT-PWT ARI-GAP/ARI：输入 11 位八进制 ARI（实验口径 POD1=11000436010）
4. 8378 基站接 PoE，LED 红三步→橙三步→绿 1s 亮 1s 灭=存活
5. Subscribers/Base stations list 基站上线 → Add/IBS-xBS sets 建话机
6. GAP registration → IPUI 出现 → Assign；话机侧注册 PIN 0000（实验口径）
7. 验收：终端类型自动显示，互打测试通过

**8328+8214 实验**（p453-465）：

1. DHCP 池 .10-.69 + Auto-Provisioning 先行
2. 8328 接网线，绿闪=拿到 IP；不知 IP 用 8214 拨 menu+*47* 搜基站
3. Web Admin：Country/NTP、核验 DNS、Servers 区填 Registrar=192.168.1.246、注册周期 3600s、Sipping 19=Disabled → Save
4. OXO 侧建分机 120（Open SIP Phone），记录 SIP 密码；VoIP 高级旗标 no_pack_support_for_siphone=true
5. 话机注册：Auto Install 选 SIP，输 PIN 0000 与 AC 0000，提示 Registration success!
6. 注意：注册成功后主页暂显"无 SIP 注册"属正常中间态，再做分机声明（n40）
7. 验收：Web Admin 表中 IPEI 非默认 FFFFFFFFFF、分机关联出现、互打通过

## A2 — 未来触发

使用情境：新装/批量开通话机；话机拿不到地址；终端不上线；DECT 基站部署与手柄注册；传真等模拟设备接入。

语言信号：IP 话机 / static / dynamic / Dynamic Alcatel / Auto-Provision / TFTP / NOE 密码 / xBS / ARI / GAP / IPUI / 8328 / 8214 / *47* / FXS / Open SIP。

与相邻能力区分：系统还没开通 → 开通能力；话机要建组与按键 → 编号计划与组能力。本能力到"终端在役、号码已分配"为止。

## E — 可执行步骤

输入契约：终端型号清单、DHCP 规划、NOE 管理密码、（DECT）ARI 值与 PoE 交换机。物理基站/话机不在现场 → 该实验只做配置不验收（n09 同类限制）。

1. 前置：DHCP 池就绪 + Auto-Provision 启用。完成标准：池内有空闲地址
2. IP 话机（静态）：话机侧填 IP/掩码/网关+NOE 密码+TFTP1=OXO 地址。完成标准：重启后自动分配目录号
3. IP 话机（动态）：选 Dynamic 或 Dynamic Alcatel（按客户网环境）。完成标准：同上
4. IP-DECT：ARI 绑定、warm reset，基站上线后建话机 → GAP 注册 Assign。完成标准：LED 绿 1s 亮 1s 灭、互打通
5. SIP-DECT：DHCP+旗标就绪，Web Admin 声明 SIP 服务器，话机注册后做分机声明。完成标准：Registration success 且关联出现
6. 模拟设备：FXS 网关接入，核许可（每口 1 UTL+1 Open SIP）。完成标准：OMC 显示 Open SIP 终端在役

判停点：

- 终端不上线 → 先查 Auto-Provision 与 DHCP 池，再查话机侧配置，不要先重灌系统
- 客户网已有 DHCP 却选 Dynamic Alcatel → 拿不到地址，改模式而不是改网络
- 8214 注册成功但主页"无 SIP 注册" → 属正常中间态，继续做分机声明（n40）
- ARI 丢失 → 唯一值从 eBuy 重新获取，不要猜号

输出契约：在役终端清单（型号/号码/模式）+ 待验收物理测试项（虚课未测项）。

## B — 边界

- 全部地址/ARI/PIN/AC/admin 密码为实验口径，生产替换并纳入安全基线（n44）
- 8328 Web Admin 默认 admin/admin——部署完必须改（推断，结合防打基线；n38）
- 短号与紧急号相关话机行为不在本卡（出局路由属 SIP 中继与 ARS 域）
- LED 六步、ARI 位数等设备口径以当期 System Guide 为准（原书指向 8328 System Guide）
- 生产无线部署的勘测与覆盖设计在书外
