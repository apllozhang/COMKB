# IP 域与 PCS 域级生存性（CAC、编解码、PCS 部署、救援与回切）

## R — 原文依据

> "THE CALL SERVER(S) MUST BELONG TO DOMAIN 0 • THIS ENTAILS THAT THE IP ADDRESS RANGES CONFIGURED FOR THE OTHER DOMAINS MUST NOT ENCOMPASS THE PHYSICAL AND ROLE IP ADDRESSES OF THE COM SERVER(S)"（p152）
> "'Domain Max Voice Connection' parameter in the IP domain ('-1' means unlimited)"（p144）
> "High bandwidth: OPUS SWB > OPUS WB > G722 > G711 > OPUS NB > G729 ; Low bandwidth: OPUS NB > G729 … The lowest capability (of the 2 domains) is selected"（p147）
> "BE AWARE THAT 'DATABASE SYNCHRONIZATION' IS UNIDIRECTIONAL: ONLY FROM CS TOWARD PCS"（p179）
> "The PCS can be active for 30 days max • After 30 days, it switches in 'Software protection violation' position"（p182）

出处：ENTPXTE401EN p139-233。

## I — 自述

高可用第二层：IP 域划分设备归属，PCS 在断链时接管远程域——域是底座，PCS 是域级生存性，两者都不是热备 CS。

1. **IP 域五条硬规则**：按设备 IP 在初始化时落域（未匹配进默认域 0）；每系统 1000 域；CS/PCS 必须域 0 且其他域地址段不得覆盖 CS 物理/角色地址；域条目掩码须与设备一致；设备复位后才落新域
2. **CAC 只闸跨域**：Domain Max Voice Connection 限"从/到该域"通话数（-1 不限），域内不控；超限退路靠溢出特性
3. **编解码选择链**：按设备能力+域带宽档取交集，跨域取两域较低档；G722/OPUS 的转码/会议等媒体服务须 OMS；OPUS 动态 payload 默认 125（p159）
4. **PCS 三前提**：许可锁 332>0、版本≥CS、RAM≥CS；容量 240 台/系统、一域一 PCS、一 PCS 可救多域（至多 1000）但每台至少绑一台 MG——无 MG 域里的 SIP 话机/网关救不了
5. **四状态**（pcsview）：Inactive（随 CS）/ Active（接管中）/ Inactive*（链路恢复等回切计时器）/ Undef（CS 切换后未重建连接）
6. **救援与回切**：GD/OMS 软复位改连救援地址；话机重启用 CS 下发的 TFTP Backup IP@（p172，藏于话机 flash，排障用 tnet d 的 ipconfig survi 查看）；回切计时器三模式——默认 30 秒、定点 Hour、Timeout 值 1-65535 秒（0=不自动重启人工控制）
7. **数据纪律**：库单向同步（CS→PCS），PCS 上改的下次更新即丢；防火墙/时间/NTP/SSH/Syslog/hosts/SNMP/Radius 八类参数逐台手工配；最长连续激活 30 天（431 报剩余、432 违约态、427/428 报断链）；不提供 TFTP/DHCP/ABC-F，被救域打不了 4645 VM

## A1 — 书中案例

**建域与 CAC 测试**（p154-163）：

1. WBM IP 域 Create：域 1（Intra=Large/Extra=Low）、域 2 同法；Domain Max Voice Connection 先设 1
2. IP Domain Address 分配地址段（掩码照抄设备；单主机条目 Low=High）
3. 复位设备与板卡后落域；domstat 看域参数/条目/设备，cnx dom 看 allowed/used 计数
4. CAC 验证：域 1 呼域 2 第一通成功、第二通被拒；两域改回 -1 后全通
5. compvisu eqt all 验证编解码（域内 G722(83)、跨域 G729(43)）

**PCS 部署与断链演练**（p185-216，实验口径）：

1. PCS VM 版本核验（欢迎信息 ≥CS）+ spadmin 确认锁 332=0/3
2. console 模式改 IP（出厂 10.253.253.1/26 不兼容实验网）+ 防火墙互信 + hosts 核对
3. WBM 声明 PCS 地址/FQDN；域 2 的 Backup IP address 指向 PCS；OMS omsconfig 填 Passive CS address
4. oxe-nw-sshkey-sync 全网免密 → PCS 初始化（空库/autostart/日期）→ pcscopy 到 End OK
5. 断链：Rlab 断开主站子网 → pcsview 显示 ACTIVE、被救话机数 2、域 1/1
6. 恢复链路 → INACTIVE*（Timeout=0 实验口径人工重启）→ 重启后回 INACTIVE、设备归 CS

## A2 — 未来触发

使用情境：跨域通话被拒；设备"不落域"；建 PCS；断链演练；"分部断了还能不能用"；PCS 激活超 30 天；回切时机设计；4645 留言打不通。

语言信号：IP domain / domain 0 / CAC / call admission control / Domain Max Voice Connection / 带宽档 / OPUS / G722 /
  PCS / passive communication server / pcsview / pcscopy / TFTP Backup IP@ / 30 天 / 427 / 428 / 431 / 432。

与相邻能力区分：断链后的公网退路转溢出能力；库刷新失败先查免密（SSH 地基能力）；冗余对本身转 CS 冗余能力。

## E — 可执行步骤

输入契约：网络规划（域划分/地址段/掩码）、PCS 资源（许可锁 332、VM/板卡/GAS）、断链演练窗口。无 MG 的纯 SIP 域要 PCS → 判停，先补 MG 或改方案。

1. 建域与地址分配：WBM 建域 → 配带宽档/CAC/本地化 → 配地址段（掩码与设备一致）。完成标准：domstat 可见域与条目
2. 复位落域：复位相关设备与板卡。完成标准：domstat 菜单 8/10 设备进入正确域
3. CAC 设定：按话务设 Domain Max Voice Connection（不确定先 -1）。完成标准：cnx dom allowed 值与设计一致
4. PCS 前提核验：锁 332>0、版本≥CS、RAM≥CS、PCS 留域 0。完成标准：三项全过
5. PCS 部署：console 改 IP、防火墙/hosts 互信、WBM 声明与全局参数、域绑定 Backup IP、OMS/板卡声明、全网免密、pcscopy。完成标准：pcsview 显示 PCS 且域关联正确
6. 演练：断链看 ACTIVE 接管 → 恢复链路看过渡态 → 按回切策略复位。完成标准：四状态迁移链全程可验、设备归 CS

判停点：

- 其他域地址段覆盖了 CS/PCS 地址 → 停，重新规划（域 0 硬规则，CAC/生存性全会错乱）
- 建了域设备还在域 0 → 先查是否复位、掩码是否一致，不盲目重建
- pcsview 长期 Undef → 查冗余切换后 PCS 与新主的连接重建
- 客户期望"PCS 长期顶班"→ 停，30 天上限+单向同步，转中心侧修复方案

输出契约：生效的域划分与 CAC 口径 + 可验证的 PCS 生存性（演练记录）+ 手工参数八项核对清单。

## B — 边界

- 域与编号规划、PCS 布点设计需客户网络/话务输入，本书只教机制与施工
- PCS 救不了 4645 VM、SIP 传真、SIP VM；无 TFTP/DHCP/ABC-F（p183）——客户体验预期要提前讲
- PCS 激活期话单 CS 不自动收回，要 OmniVista 8770 同步或手动取回（p181，书外操作）
- 断链演练期间主站全部 VM 失去 IP 可达——生产演练先备带外通道（p212）
- 空 swinst 库/autostart 等 PCS 初始化操作属 Starter 内容（p185-210 引用）
