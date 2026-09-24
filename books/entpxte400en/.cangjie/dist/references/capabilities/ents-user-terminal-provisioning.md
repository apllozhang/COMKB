# 用户与终端开通（IP 话机/IPDSP/TDM/User Profile/内部 DHCP）

## R — 原文依据

> "Each user has a directory number • This number is unique in the system and has a length of 8 digits maximum"（p291）
> "The association between the Directory number and the device is done via the MAC Address … Must be removed when device replacement"（p294）
> "The secret code by default for all the users is: '0000'"（p325）
> "Configuration: 'DHCP off' by default. … Alcatel terminals only: Yes"（p356）

出处：ENTPXTE400EN p287-365。

## I — 自述

用户=唯一分机号（≤8 位），开通三法按终端形态分绑定标识：

1. **IP 话机绑 MAC**：自动分配=话机插线后输分机+初始密码（统一 0000）由系统回收 MAC；手工=建户时填写，换机必须先清除旧 MAC
2. **IPDSP 绑 Phone Identifier**：PC 需有音频设备否则不入服；TFTP 拉 lanpbx.cfg 注册
3. **TDM 绑物理地址**：机架/板/端口三地址；自动分配时设备号位留空（255）
4. **静态开通线**：话机启动期进 MMI（#* 同按或触屏）配 IP 与 TFTP #1=CS Main 地址，注册后自动重启入服
5. **动态开通线（CS 内部 DHCP）**：默认关闭；可设 Alcatel terminals only；改配置必须 Apply 重启 dhcpd；/etc/dhcpd.conf 由 MAO 再生、禁止手改；DHCP 池自动入防火墙且 netadmin 不可改
6. **User Profile 批量建户**：建 Set Function=Profile 的模板用户（Profile 名必须大写、DN 用字母开头），再 Users by profile 按模板建户
7. **维护抓手**：termstat/eqstat（d/n/p 三语法）、换机改 MAC、tnet d 上话机、getlogs+ippstat 15 取日志、outserv/inserv 摘挂服

| 终端 | 绑定标识 | 网络 | 开通方式 |
|---|---|---|---|
| IP 话机 | MAC 地址 | 静态或 DHCP | 插线输分机+0000 |
| IPDSP | Phone Identifier | TFTP/HTTPS 拉配置 | 装软件输分机+0000 |
| TDM 数字/模拟 | 机架/板/端口 | 无 IP | 插线注册或手工三地址 |
| Profile 模板 | 同上（继承） | 同上 | Users by profile 派生 |

## A1 — 书中案例

**IP 话机静态开通实验**（p320-329，How-To）：

1. WBM 建户 31011，Set type=ALE-300
2. 重启话机，无屏按 #+* 或触屏进 Config. MMI
3. IP Parameters 里 IPv4 改 Static，填 IP/掩码/路由（实验口径 192.168.1.141）
4. System Settings 里 TFTP #1 填 CS Main 地址 192.168.1.3
5. 话机上拨自己分机 31011，输密码 0000 注册
6. WBM 核对 TSC IP user 页 MAC 已自动回填
7. 换机演练：删旧 MAC 填新 MAC 后话机恢复在服
8. 日志演练：ippstat 开 SSH 后 getlogs，SFTP 取回日志包

## A2 — 未来触发

使用情境：新员工开通话机；话机换新；软话机装不上/不入服；TDM 话机供电异常（事件 3757）；批量建户；客户没有 DHCP 时用 CS 内部 DHCP；话机日志收集。

语言信号：建户 / 开通 / commissioning / MAC / Phone Identifier / ALE-300 / IPDSP / ALE-30h / ANALOG / User Profile / DHCP / dhcpd / 0000 / termstat / 换机 / getlogs。

与相邻能力区分：板子不在服导致话机不起见网关上架能力；号码规则设计见编号计划与 COS 能力；CS 网络/防火墙不通见 CS 网络与防火墙能力。

## E — 可执行步骤

输入契约：用户清单（姓名/分机号/终端类型/位置）、客户 DHCP 现状、话机密码规范。分机号规划冲突先回编号计划能力核对。

1. 建户：WBM Users 建 DN+姓名+Set type；IPDSP 场景再开 IP-Softphone emulation。完成标准：用户对象在库
2. 终端上线：IP 话机插线输分机+0000（首登后按客户规范改密）；TDM 按自动/手工分配。完成标准：termstat 显示 IN_SERV
3. 静态/动态选线：客户有 DHCP 走动态；无则 CS 内部 DHCP（默认关，开 Alcatel-only 评估）。完成标准：话机获址并注册
4. CS DHCP 配置（如走此线）：WBM DHCP 配置池与全局参数，Apply 重启 dhcpd。完成标准：话机从池内获址，dhcplog 四步完整
5. 批量场景：建大写 Profile 模板，Users by profile 派生建户。完成标准：新户继承模板参数
6. 巡检与维护：termstat/eqstat 核状态；换机改 MAC；故障机 tnet+getlogs 取日志。完成标准：台账与在服清单一致

判停点：

- IPDSP 不入服 → 先查 PC 音频设备与 PC 防火墙端口（n19），再查 OXE 侧
- TDM 话机报事件 3757 → 供电不足禁入服（n17），按 110W/150W MR3 规则处理而不是反复重启
- 话机改了 IP 参数不生效 → IP 参数仅启动期可改，重启话机再进 MMI
- dhcpd.conf 被手改后丢失 → 该文件按 MAO 再生（n20），改配置回 WBM 而不是改文件

输出契约：在服用户与终端清单（绑定标识齐全）+ DHCP 配置记录（如启用）。

## B — 边界

- 实验分机号 31000-31043、地址池 192.168.1.145-149、密码 0000/*tx8000# 均为实验口径；生产必须替换并收紧初始密码
- TDM 功耗规则仅约束 3U 机架（110W MR3 预留 4/3 槽+MG Reserved 虚板）；1U/Crystal/本地电源不受限（n17）
- ALE-3 不支持远程办公场景；4059EE 关联分机禁 multiline（n18，话务台场景在呼叫处理能力展开）
- 话机硬件规格目录（屏幕/音频/接口参数）归产品目录不入册；IPDSP 端口基线（UDP 10000-10499/32512-33023/28000-39999、TCP 2535）见 p314 附录
- DECT/WLAN 终端开通不在本书实验链内
