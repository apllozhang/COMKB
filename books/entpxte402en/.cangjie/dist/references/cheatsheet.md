# 决策规则速查 — OmniPCX Enterprise — 系统装载 (Participant's Guide, Edition 12)

| 能力 | 一句话规则 |
|---|---|
| S.O.T. 部署工具的安装、初始化、更新与 Template Factory | ISO 内含 OVA、Standalone 加物理机 Hosted 加虚机；首连强制改密设口令短语；更新仅限同主版本；Template Factory 可降级启用 |
| OXE 呼叫服务器单版本全加载与加载后初始化 | 网络引导（BOOTP/DHCP）经 TFTP 与 FTP 完成安装；空盘才自动装、已装盘须 grubboot ETHER；加载后密码九条规则与角色寻址/许可是独立后置清单 |
| OXE 多版本加载、分区切换与静态/动态补丁管理 | 双分区装第二版本不打断话音、切换才重启；静态补丁停话音或装 inactive、动态补丁必须排在静态之后；补丁累积包含全部此前修正 |
| OXE-V 虚拟化：平台选型、许可路径与 OXE/OMS 虚机交付 | 平台矩阵决定许可路径（FlexLM 仅 ESXi/KVM，其余强制 Cloud Connect 且与 RTR 互斥）；OXE 规格模板四档；OMS 每台 120 通道、每 OXE 240 台 |
| GAS 通用设备服务器：硬件前置、软件加载与后安装向导 | BP 自备硬件按前置表（360GB/硬件 RAID/50 并发 WebRTC 上限）；BootDVD+GAS iso 经 SOT 加载；后安装向导六段含 FlexLM 与 WebRTC GW 参数 |
| Cloud Connect 云连接：网络前提、FTR 首次注册与 PIN 恢复 | 出站 443 XMPP/WSS+80 SOCKS5 连 connect2.opentouch.com；FTR 用 swk 里的 CCSID 换永久凭证；备机禁做；panic 后 6 位 PIN（5 天有效）是唯一出路 |
| RTR 许可开关：资格期状态机、事件监控与 FlexLM 互斥 | 每日应答 OK 加 0.5 天/NOK 减 1 天、30 天归零进 panic；Dashboard 四级状态加 Duplicated 双扣；FlexLM 与 RTR 互斥 |
| OPEX / Purple on Demand：订阅许可、LMS 同步、panic 时间线与 C2P 转换 | lock 431 开 OPEX、24 项订阅按 Unitary/On activation/By threshold 消耗；OXE 每 4 小时与 LMS 对账，失联 30 天或超订会进 panic；C2P 下单即定局 |
| Easy Installation 分发器模式：无 SOT 环境的本地加载 | iso/zip 传到 /tmpd，OXE 用 swinst 9-10 自己当分发器解包安装；全版本/静态补丁强制 inactive；Rload 解包物要 9-7 手动清理 |
| SOT 媒体传输与加载项目配置（公共动作） | 媒体三库（Windows/NFS/本地）、FTP 或 SFTP 2222 传文件、Refresh 后 Declare；Easy 向导与 Expert 独立管理两种项目模式 |
| GAS 日常运维：版本、备份、host 升级与 UPS | gasversion 查五层版本、gasbackup 出 tar.gz+PostInstall.cfg、全新安装加备份等于免后安装；host 升级是全系统停机窗口；UPS 默认 30% 关机 |
| Fleet Dashboard 云端机队服务：Inventory、Offer、远程控制台与软件更新 | 五服务（Inventory/Get offer/Push offer/远程控制台/软件更新）；控制台单会话 1 分钟超时且入 shell.log 审计；更新只管传输、切换归 BP |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
