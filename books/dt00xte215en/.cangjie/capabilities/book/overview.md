# Book Overview（参考区）— OmniSwitch LAN Access Switching

> 供能力卡引用的背景参考；源自 references.md 落位与 BOOK_OVERVIEW.md。

## 课程主线（三日议程 + 附加模块）

Day1：课程介绍与 R-Lab 接入、产品组合、交换机管理（登录/闪电配置/文件目录）、Virtual Chassis、VLAN（p6）。Day2：OST、诊断工具、链路聚合、STP、DHL、IP 接口（DHCP/静态路由）、VRRP（p7）。Day3：QoS、ACL、Access Guardian、LLDP、PoE（p8）。议程外附加模块：Console 连接（p522-528）、软件镜像升级（p529-535）、Auto-Fabric（p536-554）、Fleet Supervision（p555-569）、OST 2.0 安装指南（p572-580）。

教学推进主线：先接入后组网、先二层后三层、先底座后策略——这也是实际交付项目的推荐学习顺序。

## 实验环境（R-Lab，仅 Boundary 背景）

- 入口 rdp.al-mydemo.com，账号 LanpodXa/Xb（X=POD 号 1-32），密码每会话唯一由讲师发放（p14）；推荐 Chrome/Edge，Firefox 有复制粘贴兼容问题（p14，nr-06）。
- 交换机凭据：控制台 admin / Superuser=1（p15）；Linux 客户端 SSH 用 admin-netadv@10.4.X.Y、口令 Superuser01!（p38，双凭据并存，nr-07）。
- POD 拓扑：7 台交换机 EMP 地址 10.4.Pod#.{1,2,3,5,6,7,8} 对应 6900-A/6870-B/6560-A/6360-A/6360-B/6870-A/6860-B（p93）+ 10 个 Linux 客户端 + 无线客户端；RustConn 管控制台与桌面（支持分屏广播命令），Proxmox 仅开停虚机（p19）。
- 公共服务器：192.168.100.102 同机充当 DHCP/RADIUS/Web/FTP；pfSense 192.168.100.108；客户端 DNS 10.0.0.51（p17-18, p23）。
- 实验交换机为"最小化非空配置"：预置到管理网 10.0.0.0 的静态路由（p92）、预置聚合 17/78（p286）、WebView 已授权（p97）——实验里"凭空出现"的配置来自预置或前序实验。
- 实验镜像 8.10.9.R04（p141）；历史截图残留 8.7.98.R03（p504，nr-08）。
- 无线客户端严禁断开 Ethernet（远控走有线，p43）。

## 平台速览（方案沟通素材）

- 产品分层：Core=OS9900/OS6900（VRF/SPB/VXLAN/ISSU）；Aggregation=OS6870（200G VFL）/OS6860N；Edge=OS6560/6360/6370 等（p53-56）；选型参数查 datasheet。
- 配置可靠性：三目录模型 + reload all 强制回滚语义；VC 成员 flash-synchro 同步（p129-149, p170-171）。
- 堆叠：免许可、成员间无需 STP/VRRP；分裂防护 RCD/VCSP；ISSU 滚动升级（p150-182）。
- 策略：QoS/ACL/PBR/镜像共用一个 policy 引擎，默认 accept、qos apply 生效（p391-453）。
- 准入：Access Guardian=UNP+RADIUS（Filter-Id 下发档案）；无 MAC 登记 Block（p454-485）。
- 运维：诊断八件套；升级取最新 GA/MR（8.10R4 起签名镜像）；Auto-Fabric 零触七步链；Fleet 免费看资产、OST 2.0 装机排障（需支持合同）。

## 教材口径声明

- 全部实验地址/账号/实验数值仅限实验环境；生产必须替换并做安全加固（引用时一律标"实验口径"）。
- 生产化边界三文档：OmniSwitch AOS Release 8 Specifications Guide（型号规格数值）、CLI Reference/Network Configuration Guide（全量命令与条件组合）、AOS Release Notes（升级步骤）——原书反复回指，现场必须随手备查。
- 版本敏感点（needs-review）：镜像会话数 2 vs 4（nr-01）；LLDP-MED 两页标记值不一致（nr-02）；UNP 全称两写（nr-03）；console 速率分代表（nr-04）；实验镜像版本混杂（nr-08）。
- 生产割接流程（变更窗口/灰度/审批）原书不涉及，属治理域。
