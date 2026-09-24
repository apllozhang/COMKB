# CS 冗余部署与切换维护（本地/空间冗余、mastercopy、bascul、不停机升级）

## R — 原文依据

> "The 2 Call Servers must have the same type, and the same software release"（p70）
> "Calls already established are maintained • Calls being connected during switch-over are lost"（p71）
> "Limited time: 120 minutes by default … After storage time limit: history of MAO commands is deleted and incident « 440 » is triggered. A database cloning operation, also called 'Mastercopy', is then necessary !"（p79）
> "Defense: If the 'Call server role' is not correctly defined, the CS with the highest IP address starts in Main role"（p75）
> "When the IP link between the CPUs is restored, the call server that is not connected to the reference Media Gateway is rebooted."（p74）

出处：ENTPXTE401EN p69-138。

## I — 自述

高可用第一层：main+standby 软件平台复制，经 IP 链路实时 scp 同步 MAO/话务观察/话单/CCD/swinst 数据；切换时已建立通话保持、建立中丢失。

1. **两条铁律**：同软件版本+同类平台（全大写警告，p94/p117）；netadmin 改完配置必须关机重启 CS
2. **链路承载与例外**：8 类数据走 IP 链路；netadmin 管的 Linux 数据（典型=内部防火墙）不复制——要么 mastercopy 勾 LINUX DATA，要么 netadmin 的 Copy to Twin
3. **角色裁决**：两 CS 同时上线按 MAO 的 Preferred CS IP 定 main；未配置则 IP 高者上（防御行为，规划时要显式配置）
4. **失联窗口**：备机不可达时主库存 MAO 命令历史，默认 120 分钟（0-120 可配）；超时删历史、触发 440 事件，唯一出路 mastercopy
5. **double main 裁决**：链路断出现 Real Main（MAO 开）与 Pseudo Main（MAO 关）；连参考 MG 的一侧为真主，恢复后另一侧自动重启；期间话单/话务观察不合并、部分网络无语音邮箱
6. **空间冗余适配**：两 CS 分不同子网（各自 router/主角色地址 csma/csmb）；内部 DNS 只由活动主应答节点名；客户 DNS 须委派到两个主地址且内部解析器必须启用；DHCP 由活动 CS 应答（外部 DHCP 须能发两个 TFTP 地址）
7. **不停机升级**：备机先行（停话音、装版本、克隆库、起话音）→ bascul 切换 → 对原主机重复，共 11 步，全程业务在线

## A1 — 书中案例

**本地冗余部署**（p92-114，实验口径 IP）：

1. csa 上 spadmin 核验锁 186 E-CS redundancy=1
2. netadmin 双机配 IP：node=oxe、CPU csa/192.168.1.1 与 csb/192.168.1.2、main=csm/1.3、互为 twin、router 1.254；每台改完必须关机重启
3. 防火墙 Security 菜单 Bulk Import /tmpd/Firewall_Rules_multi.txt 后应用
4. root 执行 oxe-ssh-auth -c 对端 IP 建免密（authorized_keys 各 6 条）
5. MAO 参数：离 CS 最近的 MG（实验为 OMS MG #4）设 Reference=YES；Preferred CS @IP=192.168.1.1
6. csb（备机）swinst 停话音 → Expert 菜单 Cloning database 勾 DATABASE AND ACCOUNTING=y、LINUX DATA=y（带走 csa 防火墙）→ 等待克隆完成（分钟级）
7. csb 设 Autostart；GD/OMS mgconfig/omsconfig 的 CPU role address 填主地址 1.3
8. 验证：role -b 显示 MAIN(ACTIVE)/STAND-BY；twin 各项 READY；bascul 切换测试后切回

**空间冗余差异**（p115-138）：netadmin 参数改双子网（csma 1.3/csmb 2.3、双 router）；两台都激活内部 DNS；设备侧填两个 TFTP/主地址（TFTP #1=1.3、#2=2.3）；SIP 终端走 DNS 委派（oxe.company.com → 1.3 & 2.3）。

**不停机升级**（p83）：备机停话音、装新版本、无话音重启、swinst 克隆库、重启话音，bascul 切换后对原主机重复五步，全程业务在线。

## A2 — 未来触发

使用情境：部署冗余对；主备切换演练；不停机升级；备机宕机后恢复；double main 处置；防火墙在切换后"丢失"；空间冗余 SIP 切换失联。

语言信号：CS duplication / main standby / mastercopy / bascul / twin / 参考媒体网关 / Reference Media Gateway / double main / pseudo main / 440 事件 / 空间冗余 / spatial redundancy / preferred CS / 不停机升级。

与相邻能力区分：免密未建转 SSH 地基能力；域与 PCS 转 IP 域与 PCS 能力；命令用法速查转 cli-toolbox（路由卡）。

## E — 可执行步骤

输入契约：同版本同类平台的两套 CS（板卡/GAS/VM）、许可锁 186≥1、root 与 mtcl 密码、网络规划（同子网或双子网+DNS 条件）。版本或平台不一致 → 判停，先对齐再部署。

1. 许可核验：spadmin 确认锁 186≥1。完成标准：冗余许可就位
2. netadmin 双机配 IP/防火墙/DNS（空间冗余加内部解析器激活）。完成标准：两侧 trusted hosts 互含且配置一致；每台关机重启生效
3. 免密：oxe-ssh-auth 对机同步。完成标准：authorized_keys 条数正确
4. MAO 参数：参考 MG 声明 + Preferred CS IP 显式配置。完成标准：参数落库且不依赖 IP 高者防御行为
5. 克隆：备机停话音后 swinst Cloning database（勾 LINUX DATA 带防火墙）。完成标准：克隆完成、话音自动启动
6. 验证：role -b 主备态、twin 全 READY、主库建对象备库实时可见、bascul 切换演练。完成标准：切换后已建立通话保持且可切回
7. 设备指向：GD/OMS/话机填主角色地址（空间冗余加第二地址或 DNS 委派）。完成标准：设备注册走活动主

判停点：

- 备机失联超 120 分钟（440 事件）→ 放弃增量幻想，直接 mastercopy 整库克隆
- double main 已发生 → 以参考 MG 为准收敛；恢复后检查是否需要 mastercopy 补齐期间修改
- 空间冗余 SIP 切换后失联 → 依次查 DNS 委派、不缓存、内部解析器（netadmin）三处
- mastercopy 卡住或失败 → 核对三前提（免密、在备机上执行、备机话音已停）

输出契约：twin 全 READY 的冗余对 + 切换演练记录 + 升级/故障处置预案（窗口 120 分钟内）。

## B — 边界

- 冗余拓扑选择（本地 vs 空间）、话务影响评估属客户网络设计，本书只教机制与施工（BOOK_OVERVIEW 批判节）
- GD/OMS 的 SSH 连接方法 REFER TO STARTER TRAINING（p110/p134）
- 实验拓扑/IP 为 RLAB 口径；double main 是故障态而非目标态（话单与邮箱缺失期间要有预期，p82）
- PCS 是域级生存性手段，与本卡冗余不可互替——分部断链场景转 IP 域与 PCS 能力
