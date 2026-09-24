# 决策规则速查 — OmniSwitch LAN Access Switching (Participant's Guide, Edition 23)

| 能力 | 一句话规则 |
|---|---|
| 交换机登录接入与 AAA 管理面加固 | 七类服务各自认证链（本地库或 RADIUS/LDAP）+ 账号密码治理 + ASA 限源/禁服务/会话参数/SSH 强加密四清单 |
| Lightning Config 快速开局 | 笔记本 DHCP 接端口 1、浏览器 https://192.168.0.1、Defaults 必做、admin 密码必改（避开 ! 与 $）、保存固化 |
| 配置生命周期（保存/认证/回滚/备份） | write memory 到启动目录、copy running certified/flash-synchro 固化基线；冷启动按内容异同回滚，reload all 无条件回 certified |
| Virtual Chassis 堆叠 | 多台合成一台（ISIS-VC）；选举按优先级>运行时长>最小 ID>最小 MAC；分裂防护 RCD/VCSP 双机制；升级走 ISSU 滚动 |
| VLAN 与 VLAN 间路由 | VLAN 三入口（静态/UNP 分类/802.1Q，VLAN 1 不可删）；一个 IP 接口即激活路由，VLAN 无成员则接口 DOWN |
| 链路与生成树冗余（LAG/STP/DHL） | 静态聚合仅 ALE 间、接服务器用 LACP；STP 默认 per-VLAN/32768、显式指定根桥；DHL 双活分流（1 会话 2 链路、默认 30 秒抢占） |
| 三层服务与网关冗余（DHCP/Loopback0/静态路由/VRRP） | DHCP Relay 全局/接口互斥、Loopback0 永活作管理源、静态路由默认优于动态；VRRP 虚拟 IP/MAC 冗余、改优先级必须先 disable |
| QoS 与 ACL 策略 | 统一 policy 引擎（condition+action+rule，qos apply 生效）；默认不匹配即放行；UserPorts/DropServices 保留组做用户口安全 |
| Access Guardian 接入认证 | UNP+RADIUS：Filter-Id 回传档案定 VLAN 与策略；pass-alternate 降级、auth-server-down 60 秒重试、无 MAC 登记 Block |
| 诊断工具箱八件套 | swlog/事件日志/命令日志/镜像/抓包/RMON/health/sFlow；抓包只存前 64 字节，完整报文用镜像+外部抓包器 |
| LLDP/LLDP-MED 与 PoE 管理 | LLDP 默认双开（30 秒/TTL×4、不支持 linkagg 级）；network-policy 下发语音 VLAN 与标记；PoE 四档供电、优先级与 FPoE/PPoE |
| 软件升级与 Auto-Fabric 零触开局 | 版本取最新 GA/MR（8.10R4 起签名镜像）；三通道升级；Auto-Fabric 七步链（Y=禁用/N=启用）+ LBD 防环 |
| 资产与装机工具（Fleet Supervision/OST） | Fleet Supervision 免费只读看资产合规（三路声明/模板导入）；OST 2.0 装机排障（Postgres 先装、需支持合同、100 交换机/5 并发） |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
