# DIGEST — OpenTouch Suite for MLE / Starter 精华长文

> 源：OPENXTE300EN Edition 10（603 页，OpenTouch R2.6.1 / Starter Edition 10）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OpenTouch Starter 交付的全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

OpenTouch Suite for MLE（OTMS）是 ALE 面向大市场的 OpenTouch 服务器套件，上限 5000 用户，物理一体机与虚拟化（OTMS-v）两种形态。一套三件：OXE 呼叫服务器（传统 PBX 侧）、OpenTouch 服务器（ICAS 协作 + ICM SIP 核心 + AMS 媒体）、OmniVista 8770 管理服务器。

整本教材是一条交付主线：**装机 → 初始化向导 → 许可闸门**，再到**双向声明与 SIP 打通、号码路由、用户与语音业务、安全与客户端**，最后是运维闭环。

三个数字先记住：

| 数字 | 含义 |
|---|---|
| 5000 用户 | OTMS 与 OTMS-v 同一口径的用户上限；容量与话务设计在书外（Delivery note/Product limits） |
| 2570 / 5260 / 5040 | 三个关键端口：OXE PRS、OT SIP 核心（ESS）、Mule 语音邮件——两条外部网关的来由 |
| TC2149 | rehosting 唯一完整依据（附录全文收录）；配错即死锁无回退 |

## 二、装机与初始化：向导是总闸

装机三选一：手动 DVD（易错）、手动 ISO（仍非静默）、**SOT 自动化**（生产首选：虚机内自动挂载全部 ISO、含 hotfix 静默安装、PXE 启动目标机，一次只部署一台）。

软件装完不等于能交付：OT 首次开机自动进入 Post-installation wizard——这就是站点安装的正式入口。from scratch 十节走完 OT 服务才启动；重装迁移走 restore from archive。

向导四条硬规则：

1. 全部口令至少 8 字符——短了**不弹任何报错**，事后才出问题；otAdmin/otProfile 另需大写+数字+特殊字符
2. DNS 必须五类 FQDN 正反向全通（OT、8770、邮件、LDAP、OXE 呼叫服务器）——漏反向解析是声明失败的最高频根因
3. HA 新装机一律保持 Disable——仅 R2.2.x 迁移场景保留，本书没有替代高可用方案
4. 许可页显示 OK 只代表"文件在"——内容有效性与 FlexLM 连接都不测，装完必须复核

## 三、许可一张表

| 文件族 | 产品 | 校验方式 |
|---|---|---|
| .ice | OTMS / OXE-v | FlexLM（端口 27000）：物理机锚 ALUID（getaluid 读取）、虚拟机锚加密狗 |
| .swk | OXE 物理机 | 专有加密、CPUID 验证；用户数等容量口径的真正载体 |
| .sw8770 | 8770 | 在 OT/Flex 服务器侧改名 nmc.license，8770 自查 handle |

核查三件套：spadmin（三个 PANIC 计数全 0 才健康）、lmutil（服务与 FEATURE 用量）、checkLicensing.sh（两侧各跑、问题计数与日志 zip）。FlexLM 可内嵌或外置；外置后许可必须含 Dongle ID+OT ID+OXE 产品 ID，传输只许 SFTP/SCP，落地 /root 后必须移进许可目录再重启服务。

## 四、集成与号码：三件套缝合

声明顺序固定，四步走完三件套互挂：

1. OXE 前置：netadmin 建角色地址，离开前必须选 20 APPLY。
2. 8770 三级建树声明 OXE，节点号=ABC 网络×100+节点号。
3. 8770 声明 OT：凭证取自 bics.conf（otAdmin/otProfile/otuser），节点号用 99 等自由号、必须同子网。
4. OT 侧 Topology 挂 OXE：端口 2570、Codec 与呼叫服务器一致。

SIP 承载五段：trunk group（T2/SIP）、本地网关、两条外部网关（10 号到 ESS 5260、11 号到 Mule 5040 仅出话）、trusted addresses、全局压缩 G729。ESS 不支持 G723。

| 业务号 | 用途 | 去向 |
|---|---|---|
| 31000-31499 | 用户/留言/话务台/缩位 | OT 侧声明归属 OXE |
| 31200 | 语音邮件 TUI | OXE 侧走外部网关 11 |
| 31250 / 31260 | 会议桥（英/法） | OXE 侧走外部网关 10 |

前缀两侧同值；话务台前缀 OT R2.1 起必配（否则重启 wireald）；按名呼打全客户端自动加外呼前缀、按号呼打仅 OTC PC/Mobile；UDAS 同步周期至少 1、禁 0（检索只打同步库，周期设 0 目录永远陈旧）；DAS 规则强制、按国家、顺序敏感。

## 五、业务供给：用户与语音

用户供给三件套：OXE 档案（Set function=Profile、A0000 式占号、实时同步）+ OT 档案（Category=ACU-OXE、勾权、**建完必须手动完整同步**）+ 语音邮箱档案。

Users 应用只能改档案，建删必须回两侧配置工具。批量走 Web Provisioning Client（8770 3.2.8+、Unified management 许可、仅 Chrome 54+；不建 Conversation 用户、一台设备）。

语音邮箱默认就绪：defaultVmsLS（Local Storage）出厂即建，留言未压缩 wav、IMAP 直收（内嵌 1000 并发封顶）；建箱必须先选档案；通知走外部 SMTP（**无认证无 TLS**、发件账号须真实存在、失败几乎无告警）与唯一一个 SMS 网关；通用公告一次仅一条、覆盖式、5 分钟封顶。

## 六、客户端与安全

| 形态 | 触发条件 | 能力面 |
|---|---|---|
| OTC PC 全量 | 勾 Desktop 许可 | RCC+VoIP+IM/共享/会议/Outlook 集成 |
| OTC PC One 免费 | 无 Desktop 许可 | 话机伴侣：单线、盲通话、无 VoIP、无监督 |

用户报"客户端坏了"，第一排查项是 Desktop 许可勾选，不是重装。软电话走 Multi-devices：Desktop 勾、**Nomadic SIP 绝不勾**（两权互斥）。多终端最多 5 设备、远端分机与 DECT 各限 1、VoIP 不冻结话机。监督组与 OXE 话机监督键是两套机制无联动，前转与溢出会让呼叫脱离监督。

证书三档位：security OFF（全球同款通用证书，官方点名不推荐——盗打风险）、自签 Internal SHA256（换证后必须用 808x 话机重签 CTL）、外部 CA（远程接入必需；PKCS7 或带口令 PKCS12；**导入与 Deploy 是两步**，Deploy 后断会话属正常）。

## 七、运维红线

rehosting（ot-config.sh --rehost）三条铁律：

1. 参数配错即死锁且无回退——动手前必须参数全对、有可用备份（OT 备份+Clonezilla 镜像或虚机快照）
2. inactive 分区内容被清除——回滚与升级到旧分区的通道关闭
3. --rehost 只改 OT 自己——OXE/8770/OMS 与生态（DNS/DHCP/SSO/SNMP/防火墙）按 TC2149 矩阵逐项收尾；换内外 FlexLM 形态要重做许可（eBP 工单，有商务周期）

备份：每日 00:01 自动（周日全量其余增量，/var/backup/daily）；手动 otbr.sh；OT-V 必须挂 NFS、USB 无意义。维护三通道同源：原始命令、otconsole.sh 菜单、Maintenance Portal（4448 端口）。

## 八、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 装软件（SOT/手动/导 OVF） | ots-sot-installation（路由） |
| 初始化向导/备份恢复重装 | ots-post-installation-wizard |
| 装许可/查许可/外部 FlexLM | ots-license-flexlm |
| 声明节点/SIP 打通/告警对接 | ots-node-declaration-sip |
| 号码段/前缀/拨号/UDAS/会议 | ots-prior-management |
| 建档案/建用户/WPC 批量 | ots-users-profiles |
| 语音邮箱/IMAP/通知/公告 | ots-voice-mail |
| OTC PC/软电话/多终端 | ots-clients-multi-devices |
| 维护/备份/rehosting | ots-maintenance-rehosting |
| 证书/SOT 装机/监督组/实验环境 | 路由入口（opentouch-starter-router） |

## 版权

- 本精华长文为 ALE Training Services《OpenTouch — OpenTouch Suite for MLE — Solution Overview / Starter》（OPENXTE300EN Edition 10）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
