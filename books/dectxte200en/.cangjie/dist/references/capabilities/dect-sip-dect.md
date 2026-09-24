# 8328 SIP-DECT 部署（DHCP 固定 IP/四步注册/双小区）

## R — 原文依据

> "1) Create SIP extension user on OXE for each corresponding DECT handset ... 4) Then, SIP-DECT Base Station makes 'SIP register' on OXE for the Handset ... 'Contact' = 'DECT handset phone Number' @ 'Base Station IP address'"（p278）
> "Configuration 'DHCP Server' to be active ... Alcatel-Lucent terminals only NO (as the 8328 will not be recognized as an ALE device)"（p280）
> "THE PRIMARY STATION WILL BE THE STATION WITH ALREADY AT LEAST ONE EXTENSION DECLARED."（p288）
> "No roaming, between 2 DECT areas • No handover between 2 DECT areas"（p275）

出处：DECTXTE200EN p271-291, p7, p275。

## I — 自述

8328 是低成本单站方案，走 SIP 语义（PARI/PLI 体系不适用，p7 脚注）。注册闭环四步：

1. **OXE 建 SIP Extension 用户**：每台 DECT 手机 1 个 SIP 许可（Set type=SIP Extension、SIP password）。
2. **基站 WBM 建扩展**：Servers 区声明 OXE（Server Alias + Registrar FQDN）、Country、Time server=NTP；Extensions/Handset 加手机并 Register。
3. **手机空中注册到基站**：选 SIP → 设备 PIN（默认 0000）→ AC 码（基站侧可见可改，默认 0000）；注册成功后 IPEI 不再是通用值 FFFFFFFFFF。
4. **基站代发 SIP register**：Registrar 记录 contact=号码@基站 IP；随后 Extensions 关联扩展与手机（IPEI-分机号），手机屏显扩展名。

双小区（dual cell）：第二台 8328 只配 DHCP 后入网，自动发现主站并拉取全部配置；**主站=先声明 Extension 的那台**（与 IP 地址无关，仅声明 Extension 即可确立身份）；区内有 handover/roaming，两小区间没有；链路建立约 5 分钟，起不来在两站 reset the chain。

部署前提：双小区必须同 IP 子网 + NTP 强制；OXE 的 DHCP "Alcatel-Lucent terminals only" 必须设 NO（8328 不被识别为 ALE 设备）；建议 DHCP 按 MAC 固定基站 IP。

## A1 — 书中案例

**8328 部署实验**（p279-291）：

1. DHCP 固定 IP：Static IP Address 建 192.168.1.150 + MAC（实验口径）；"Alcatel-Lucent terminals only"=NO → Apply
2. 不知 IP 时的技巧：手机空闲按菜单键拨 *47* 搜基站
3. 基站 WBM（https://基站 IP，admin/admin 默认）：Country、Time server=NTP、Servers 区 Server Alias=OXE、Registrar=oxe.company.com
4. OXE 建用户 31040：Set type=SIP Extension、SIP password=31040（实验口径）
5. 基站侧 Add Handset → Register Handset(s)；手机选 SIP、PIN 0000、AC 0000（默认，实验口径）
6. Extensions 页 Add extension（31040 + 认证账号密码 + Server=OXE），勾选已注册手机后 Save；核验 IPEI-31040 关联与双向通话
7. 双小区：第二台仅配 DHCP（192.168.1.151）入网 → 约 5 分钟后主站 Dual Cell 区显示副站

## A2 — 未来触发

使用情境：小门店低成本 DECT；8328 拿不到 IP；手机注册后显示无 SIP 注册；两台 8328 谁是主站；8328 能不能组大网。

语言信号：8328 / SIP-DECT / 8214 / SIP Extension / SIP register / dual cell / 双小区 / 主站 / primary / 副站 / secondary / reset the chain / *47* / FFFFFFFFFF / Alcatel-Lucent terminals only。

与相邻能力区分：GAP 手机的 PARI 体系注册 → 手机注册能力（语义不同，勿混）；选型比较 → 产品选型能力；SIP 用户许可与编号计划属 OXE 侧通用配置（书内仅用到）。

## E — 可执行步骤

输入契约：OXE 的 SIP 许可余量、Registrar FQDN、基站 MAC 清单、NTP 服务器、手机型号（仅 8214）。非欧洲频段站点 → 停（产品边界）。

1. 规地址：DHCP 按 MAC 固定基站 IP；"Alcatel-Lucent terminals only"=NO。完成标准：取址路径打通
2. 配基站：WBM 进 Country/NTP/Servers（Alias+Registrar）。完成标准：基站认识 OXE
3. 建用户：OXE 建 SIP Extension（目录号+SIP password）。完成标准：用户与许可就位
4. 注册手机：基站侧 Add+Register，手机侧 SIP/PIN/AC。完成标准：IPEI 变真实值
5. 关联扩展：Extensions 建扩展并勾手机 → Save。完成标准：IPEI-分机关联、手机屏显扩展名
6. 通话验证：手机呼系统内用户并反向呼入。完成标准：双向通话成功
7. （双小区）副站仅配 DHCP 入网，等约 5 分钟核主站状态页。完成标准：Dual Cell 区显示副站

判停点：

- 手机注册成功但主页显示"无 SIP 注册" → 正常中间态（SIP register 由基站在关联扩展后代做，p285），不要反复重注册手机
- 两台全新站同时入网角色不定 → 先把主站配完（至少声明一个 Extension）再上副站（p288 WARNING）
- 链路 2 分钟没起来就判失败 → 时间预期不足，等满 5 分钟；仍不起在两站 reset the chain（p291）
- 想用 8328 堆叠做大覆盖 → 区间无切换/漫游（p275），转产品选型能力上 IP-xBS

输出契约：8328 部署记录（IP/MAC/扩展关联）+ 双小区主副站状态 + 边界告知单（WAN 断全断/无电话本集成）。

## B — 边界

- 三个硬边界（p272-273）：仅欧洲频段、仅 8214 手机（GAP，无 A-GAP）、电话本不集成 OXE（基站 csv/xml 或外接 LDAP，改名换号两处维护属推断标注）
- WAN 断则该站 DECT 用户全断、无 SIP 备份机制（p274）——分支办公选型必须前置告知
- 双小区合计容量书内未单列，按单站×2 估算属推断口径
- 实验 IP（192.168.1.150/151）、PIN/AC 默认 0000、admin/admin 均为实验口径，生产必须改
- 多台 8328 的 PARI 由系统自动分配（p275 语境），不可手工规划
