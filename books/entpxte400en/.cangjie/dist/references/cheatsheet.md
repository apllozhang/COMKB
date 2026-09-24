# 决策规则速查 — OmniPCX Enterprise - Starter (Participant's Guide, Edition 12)

| 能力 | 一句话规则 |
|---|---|
| OXE 首登加固（四账户与密码治理） | 三通道登录四账户分工；密码 ≥14 位九规则；失败 3-5 次锁 15 分钟；老化 10-366 天（开区间）且与 RADIUS 互斥 |
| OXE 系统启停与 autostart 管理 | 起话务 Easy 8/RUNTEL，停话务只有 Easy 7（连带取消 autostart）；无独立停话务命令；role 与 (E) 提示符判状态 |
| Call Server IP 寻址与内部防火墙 | 物理地址永远可达、Role MAIN 地址仅话务运行时生效；netadmin 改动必须 Apply+重启；iptables 默认 DROP，互通靠可信主机白名单 |
| OXE 时间同步（NTP/chrony） | chrony 渐进同步（client/server、UDP 123）+ 停 chronyd 才能瞬时拨钟；时区改动必须重启；chronyc sources 见 ^* 为判据 |
| 空数据库创建与 OPS 许可管理 | 空库只能在话务停止时建且连 OPS 一起抹；"停话务 → 建库 → 恢复 OPS → 起话务"顺序固定；5 天自检/30 天宽限/降级三阶段；spadmin+FlexLM 巡检 |
| 媒体网关上架（GD4/OMS/XL） | OPS 自动建架 + WBM 声明 + mgconfig/omsconfig 板侧配置；crystal 1-255（18/19 保留）；自动 crystal 或 DHCP 必须登记 MAC；rstcpl 打在 GD 上=整架重启 |
| 用户与终端开通（IP 话机/IPDSP/TDM/Profile/DHCP） | 分机号全系统唯一 ≤8 位；IP 话机绑 MAC、IPDSP 绑 Phone Identifier、TDM 绑物理地址；初始密码 0000；CS 内部 DHCP 默认关闭 |
| 编号计划与 COS 管理 | 前缀唯一对应功能 ≤8 位；Timer 23（3 秒）消解 31T/31000 歧义；Phone Features COS 256 类管功能开关；Connection/Transfer 矩阵管连转 |
| 呼叫处理业务域（语音指南/话务台/Entity/计时器） | 指南四槽+1 动态（GD4/GA4 16 并发、OMS 120）；MOH 激活=删 Tone 2+建 VG 2；话务台必须属组且 4059EE 只管操作；CDT 四状态 3+1 路由；计时器 76/144/trunk COS 300 |
| OmniMessage 4645 语音邮件与邮件通知 | 一节点仅一套留言系统；7000 信箱/30 端口/500(600) 小时；通知三档 None 默认/Basic/Advanced（附件）；SMTP 经 netadmin 声明+防火墙加白 |
| 公共 SIP 中继开通与弹性 | 去话九步流水线（ARS/鉴别符/ARS 表/TG/NPD/DID/网关）；SIP 禁直抓必须走 ARS；标准 TG 32 接入成对 62 通道；双网关走 ARS 第二路由或 SIP Pool |
| 外呼闭锁与紧急呼叫通知 | 闭锁=Area × Public COS（四状态列）× 实体状态（默认 Night）；8 逻辑/256 真实鉴别符/64 Area/32 COS；紧急组 ≤10 台仅 stand-alone；P-ANI 位置头依赖 Direct IP Link |
| 数据库备份恢复与维护排障工具箱 | 自动备份每日 5:45（DAY..MONTH/OPS/IMMED 分区）；恢复时停话务必须用 CS 物理地址；oxetrace 三路抓包、incinfo 释义、infocollect 交支持 |
| 传统中继（T0/T2）与 UMC 云管理 | T0=BRA 2B+D、T2=PRA 30 通道，信令按运营商（VN=France/ETSI=all countries），同步 IP 架 200-254；UMC 三功能前提 N3-MD3+SPS/PoD+云连接 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
