# DIGEST — OmniPCX Enterprise Starter 开局精华长文

> 源：ENTPXTE400EN Edition 12（821 页）· 文档整理入库 · 2026-09-23
> 定位：15 分钟建立"一台 OXE 从能登录到能打电话"的全局认知；操作细节按需查 14 张能力卡。

## 一、这套东西是什么

OmniPCX Enterprise（OXE）是 ALE 的企业通信服务器：一台**基于 Linux 的软件 PABX**，跑在 IP 数据网上。承载形态四种并存——Common HW 机架、虚拟机 OXE-V（五种 hypervisor）、GAS 一体机（Rocky Linux+KVM）、Crystal CPU（退场中，由 XL 机架补高密度模拟口）。

整本教材是一条**准入闭环**主线，九段推进：安全登录、系统启停、IP 与防火墙、时间同步、空库与许可、网关上架与用户开通、内部呼叫处理、公共 SIP 中继、备份排障。

五个数字先记住：

| 数字 | 含义 |
|---|---|
| 14 位 | 系统密码最小长度（九规则治理，失败 3-5 次锁 15 分钟） |
| N3 / R101.0 | 防火墙默认全关的版本起点（完整 iptables 自 R101.0） |
| 5 天 / 30 天 | 许可自查周期 / CPU-ID 不一致的宽限期 |
| 1-255 | crystal number 取值范围（18/19 保留） |
| 992 并发 | 标准 SIP 中继满配（32 接入成对，每对 62 通道） |

## 二、准入链五连（顺序即依赖）

1. **登录加固**：三通道（V24/SSHv2/控制台）、四账户（mtcl/swinst/root/client）。root 只能本地直登，IP 侧必须 mtcl su；root/mtcl 固定 900 秒超时。密码 ≥14 位、失败锁定、老化期 10-366 天范围内取值（RADIUS 场景必须关老化）。
2. **系统启停**：全走 swinst（Easy/Expert）。起话务=Easy 8 或 RUNTEL；停话务=Easy 7（连带取消 autostart，且没有独立 CLI 命令）；判状态用 role，提示符 (E) 不实时刷新。
3. **IP 与防火墙**：双地址体系——物理地址永远可达（停话务后唯一可用），Role MAIN 地址仅话务运行时生效，设备统一指向它。netadmin 改动必须 Apply+重启；默认域名 oxedomain.com 会致证书错误。N3 起防火墙默认全关，互通全靠可信主机白名单；"Allow SSH for all" 是开局便门，配完必须 Deny 收口。
4. **时间同步**：chrony（R101 起）做渐进同步（client/server、UDP 123）；首次装机先停 chronyd 瞬时拨钟再开启渐进；时区改动必须重启。
5. **空库与许可**：MAO 存配置、OPS 存许可。空库只能在话务停止时建，且**连 OPS 一起抹掉**——"停话务、建库（真实国家码）、恢复 OPS、起话务"顺序不可乱。软件每 5 天自查许可；CPU-ID 不一致给 30 天宽限，之后进降级三阶段（告警、4 小时后禁内呼、8 小时循环）。

## 三、配置域：网关与用户

**媒体网关上架三线一个套路**（WBM 声明 + 板侧 mgconfig/omsconfig + crystal/MAC 联动）：

| 网关 | 形态 | 关键约束 | 压缩器 |
|---|---|---|---|
| GD4 | 硬件机架 1U/3U | 板侧口令 root=mg4.ale；crystal=Shelf 地址 | 30（+ARMADA=60） |
| OMS | 虚拟软件网关 | 四强制字段；禁止加扩展架与板卡；口令均 letacla1 | 上限 120，独有 OPUS/G722 |
| XL | 高密度模拟机架 | 奇数机位创建；GA-XL 只能占 1/2 槽；-48Vdc 供电 | 每 GD-XL 30（+ARMADA=60） |

crystal number 取值 1-255（18/19 保留）；crystal 自动分配或 DHCP 寻址时必须勾 "Ethernet Address checked by TFTP" 并登记板 MAC，换板必更新，否则 CS 不下发 binom。rstcpl 打在 GD4/GDXL 上=整个机架重启，避开话务高峰。

**用户开通三法**：分机号全系统唯一、≤8 位、初始密码统一 0000。IP 话机绑 MAC（换机必改），IPDSP 绑 Phone Identifier（PC 无音频设备不入服），TDM 绑机架/板/端口。TDM 功耗注意：110W MR3 上要预留 4/3 槽并配 MG Reserved 虚板，供电不足报事件 3757。

批量建户走 User Profile（模板名必须大写）。客户没有 DHCP 时用 CS 内部 DHCP（默认关闭；dhcpd.conf 按 MAO 再生禁止手改；DHCP 池自动进防火墙白名单）。

## 四、业务域：路由与外线

**编号计划是路由地基**：每个前缀唯一对应一个功能（≤8 位）；31T 功能前缀与 31000 分机的歧义靠 Timer 23（默认 3 秒）消解；改前缀必须同步换语音指南，否则指南播旧号码。两套 COS 分管两摊：Phone Features COS（256 类）管功能开关，Connection/Transfer 矩阵管连转；外呼区域是第三套 Public COS。

**内部呼叫处理**：MOH 激活固定二步=删 Tone 2+建 VG 2；指南槽位 GD4/GA4 为 4 静态+1 动态（16 并发），OMS 120 并发，试听拨 580+指南号。话务台必须隶属组（每节点 ≤50 组），4059EE 只管操作不管语音（须关联单线话机/IPDSP），话务员 80 秒无应答自动转 Absent。

Entity/CDT：四状态各 3 个顺次路由+公共溢出号（夜转号必须单线分机），实体默认 Night 态。

**公共 SIP 中继九步流水线**，按序走完：ARS 前缀（逻辑鉴别符）；实体鉴别符选择器；真实鉴别符规则（Area+ARS 表）；ARS 路由（去位/加位）；中继组；NPD；DID 翻译器（CLI 组装）；外部网关。

三条红线：SIP 不支持 # 直抓（ARS 强制）；真实鉴别符必须先建才能在实体映射；G722/OPUS 要系统级与网关级两级放行（且仅 OMS 支持）。来话靠 DID 翻译器落地（未配时回 484），显示修饰靠回叫翻译器。弹性两案：ARS 第二路由备份、SIP Pool 负载均衡+互备（Supervision timer 设短如 5 秒，否则切换慢）。

**闭锁与紧急**：外呼权限=Area × Public COS × 实体状态三交点（32 类 COS、64 Area）；"明明放行了还打不出去"先查实体默认 Night 态。紧急通知仅 stand-alone 单节点（组 ≤10 台商务设备，Tone 34+弹窗，日志 ≤100 条 FIFO）；Location ID（P-ANI 头，RFC 7913）外发必须启用 Direct IP Link。

## 五、运维收尾

- **备份恢复**：自动备份每日 5:45；分区 DAY/WEEK/MONTH/IMMED/OPS/FACTORY。两个隐藏坑：停话务后 SFTP 必须用 CS 物理地址（Role 地址已失效）；传输必须 Binary。恢复选项里 "restore Cloud and Rainbow services" 实验室选 n 剥离客户云凭据。
- **排障八件套**：oxetrace（三路抓包打包 zip）、ippstat（IP 话机）、incvisu/incinfo（事件与释义）、syslog（UDP 514 外发）、securitystatustool（安全全景）、infocollect（root，交支持标配 .tbz）、tcpdump（pcap）。实验输出里的 unknown rack type、BAD PCMS CODE、484 大多是"非故障现象"，用 incinfo 与业务结果定性。
- **传统中继与 UMC**：T0（BRA，2B+D）/T2（PRA，30 通道）信令变体按运营商选（VN=ISDN France、ETSI=all countries）；同步优先级 IP 架 200-254；节点号必须=本系统 ID。UMC（N3-MD3 起）三功能：Easy users（15 参数）、Easy SIP trunk（约 120 架构 Profile，不支持 Mini SIP）、Expert Configuration（云 WBM）；前提=SPS 合同或 PoD 订阅+云连接就绪；排除话务台/ACD/多实体/酒店等场景。

## 六、交付红线

| 红线 | 说明 |
|---|---|
| 教材密码不上生产 | Administrator5689! / Superuser2580* / letacla1 等全部是实验值，首连即改密 |
| 空库即抹许可 | 建空库前先备份 OPS，顺序不可乱 |
| SIP 实验值不外带 | ITSP1 号段/账号/紧急显示规则是模拟器口径，生产按 TC2005 与运营商文档 |
| 4645 安全另补 | 防盗打加固按 SA0046 与 TC1774 执行 |
| 深度主题有边界 | 空间冗余/组网=Advanced；FlexLM=CPU Loading；Cloud Connect=ENTPXTE402 |

## 七、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 登录/改密/密码策略 | ents-first-login-hardening |
| 配 IP/防火墙/白名单 | ents-cs-network-firewall |
| 建空库/恢复许可/FlexLM | ents-db-license |
| 上架 GD4/OMS/XL | ents-media-gateway-deployment |
| 开户/话机/软话机/DHCP | ents-user-terminal-provisioning |
| 编号计划/COS | ents-numbering-cos |
| 语音指南/话务台/Entity/计时器 | ents-call-processing |
| SIP 中继/ARS/网关互备 | ents-sip-trunk |
| 启停/对时/4645/闭锁紧急/备份排障/T0T2/UMC | 路由入口（oxe-starter-router） |

## 版权

- 本精华长文为 ALE Training Services《OmniPCX Enterprise - Starter》（ENTPXTE400EN Edition 12）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
