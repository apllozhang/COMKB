# 决策规则速查 — OmniPCX Enterprise - SIP (Participant's Guide, Edition 12)

| 能力 | 一句话规则 |
|---|---|
| SIP 协议机理与 OXE SIP 架构 | SIP 只管信令（六组件协作、消息码表、注册时序）；域名必须改默认值，空间冗余靠节点名+DNS 委托只让 Main 应答 |
| SIP 用户形态选型与容量核算 | SEPLOS=内部话机级、SIP Device=远端子网设备级（五不带）；软件锁 177/345/430，容量 15000 用户/20000 设备；终端家族四档加软终端 |
| SIP Device 用户开通与维护 | 私网+私有 SIP 中继组+本地网关三件套先行（2 接入=62 通道），建户后 sipregister/trkstat 收口；改虚拟接入数必须重启 |
| ALE 话机 SIP 开通与 NOE↔SIP 切换 | DM 激活 → profile → 建户 → DHCP 类（ALE-2X/aledevice 或 SIP80x8s/ictouch.0）→ MAC 绑定或 auto-discovery；ALE-x00 双分区 Force Download 决定切换快慢 |
| ALES 软终端开通与认证 | login 必须预建且匹配 LDAP uid；Framework 3s/50 条防隔离；移动端 Keep Alive=NO 与轮询 ≥21600s 是推送硬前提；一号多机同型互斥可 force |
| OXE DM 证书定制与安全级 | 默认证书只适配 WBM；内部 PKI 生成根 CA+CS 证书（SAN 含 FQDN/通配/IP）并出 CTL；OpenSSL 三级 2/1/0 改后必须重启；mTLS 8443 为 R101.1 起 |
| 经 SBC 的 SIP 运营商接入与 OTSBC 部署 | OXE 侧七件事（信任主机/中继组/外部网关/ARS/DID/NPD/回拨）+ OTSBC 向导八屏与排障三连（编解码放行/消息域改写/Contact User） |
| 远程办公方案与落地 | 两条路——SBC/RP（≤500 用 OTSBC 内嵌反代，更多 NGINX PLUS）与 VPN（仅 ALE-2/3 内嵌 OpenVPN）；EDS 零touch 四限制；证书五方信任链缺一断一跳 |
| 编解码协商与验证 | 系统→域→DM→终端→链路/网关五层放行后按优先级选最高质量；系统总闸压过一切；compvisu 定格实际算法 |
| SIP 跟踪采集与维护排障 | 状态四查（sipregister/sipdict/sipgateway/trkstat）→ motortrace 轻量信令 → oxetrace 打包 zip → mtracer/sipdump 深挖；恢复首选 dhs3_init -R SIPMOTOR |
| SIP 设备管理选型与 profile 体系 | OXE DM（N1 起）只管 8008/ALES/ALE-x，8770 另管 8088 酒店与停产机型；profile 默认 0 上限 100，ALE-x 本地/远程两份；配置文件无备份 |
| ALE SIP 业务特性配置 | 监督（SUBSCRIBE/NOTIFY、30000/40 键、事件 510-513）、寻线组三型（并行组禁混装）、多终端（1 主 4 副）、可编程键（#3-#122）、RCC 三档、按名呼叫（48 条/16 并发） |
| POD 实验环境与运营商模拟器 | RLAB 按 POD 划分（OXE 192.168.1.1/1.3、SBC .105、ITServer .252）；POD 准备四段收尾外线基线；ITSP1 直连与 ITSP2 经 SBC 双腿号码规则 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
