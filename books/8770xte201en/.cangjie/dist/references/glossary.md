# GLOSSARY — OmniVista 8770 计费与性能管理术语表

> 阶段 3 产出（源：candidates/glossary.md，69 条全量，此处收录主干约 45 条）。
> 口径：定义只采信本书正文；WBM/NMC/OMC/MOS/RTCP-XR/NDDI/ABC-F/PWT/DECT/RBS/IBS/CAC/GD 等缩写书中未给全称，如实标注；实验值（密码/账号/号码/税率/汇率）一律标"实验口径"。

# OmniVista 8770 R5.2 (8770XTE201EN Ed45) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（650 页），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、计费票据与管道域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Accounting record / ticket | 计费票据 | OXE 呼叫结束时生成的话务票据（ED5.2 版式最长 47 字段），先入内存缓冲（≤500 条）再落盘——全书计费链的原子数据 | p61-62, p66 |
| Memory buffer / tax.tmp | 内存缓冲/过渡文件 | 缓冲满时旧票进 tax.tmp，再满时合并出新 DAT；90 分钟无新票定时落盘；account compress 强制落盘 | p62-64, p93 |
| TAX*****.DAT / ACCOUNT.LIS | 票据文件与索引 | 压缩票据文件（序号 AAAAA-ZZZZZ 递增）与文件清单索引；8770 靠对比 ACCOUNT.LIS 做增量取回 | p62, p98 |
| Accounting methods | 五种计费方法 | 每台 PCX 各选一：No accounting/Detailed（默认推荐）/Organization update without retrieval/Global per node 两种（实体键=网络号×1000000+节点号） | p99-102 |
| Loading filter | 加载过滤 | 五道闸：Duration/Cost 阈值、Communication Type、Call type、Charged party node；被过滤票不入库不可恢复 | p110-111 |
| Ticket collector | 票据收集器 | 把 PCX 票据原样供给外部计费应用，仅需 Ticket collector 许可；文件落 C:\8770\data\collector | p103 |
| PCS | 被动通信服务器 | 经呼叫服务器同步透明发现；文件带 PCS ID（IP 的十六进制，如 AC199E64=172.25.158.100）后缀 | p104-106 |
| adfexc | OXE FTP 取数账号 | 8770 PCX 页签必填且用户名禁改（许可校验），密码须与 OXE 一致 | p77, p109 |
| NMCLD_1.log | 票据加载日志 | TicketsRead/BadLines/处理速度/被过滤数（实验口径 9 张票 52 tic/sec） | p114 |
| NMC Loader / Service Manager | 加载服务与管理器 | 停/启 NMC Loader 即触发 loader 目录文件入库（手工灌测试票的标准手法） | p142 |

## 二、运营商与资费域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Carrier | 运营商 | 8770 里的资费容器（不代表真实合同）；Name/Symbol（≤5 字母）全局唯一；分直连与 pulse 两类建法 | p117, p152, p218 |
| Period | 资费有效期 | 新周期建立时旧周期自动封口；同一运营商可并存多周期（价目演进正规做法） | p152, p244 |
| Calling / Called region | 主叫/被叫区域 | 主叫区=PCX 或 PCX+中继组；被叫区=前缀集合按最优（最长）匹配归属；同一前缀不能跨区；一区可兼两角 | p118, p154-156, p181 |
| Direction | 方向 | 主叫区×被叫区配对，唯一绑定通信资费（可选服务资费/调整/时延）；未匹配落 unspecified 兜底 | p118, p172 |
| Tariff（exact / round / pulse / PCX given） | 资费四种计算模式 | exact 线性可叠加 initial cost/initial duration/minimum cost/segments；round 按阶段；pulse 用票据 Charge units；PCX given 不换汇 | p128-136 |
| Service tariff（C+S） | 服务费双资费 | 特服号总票价=通信费 C+服务费 S；必须建两个资费并在 Direction 成对绑定；法国 SVA 由 ARCEP 监管 | p137, p162-163 |
| Adjustment | 调整系数 | 线性 Ax+b 或百分比 x+A%x，可挂资费/方向/段/运营商（Brest→Paris 打 9 折=A=-10） | p138 |
| Reference / Additional currency | 参考/附加币种 | 参考币种安装时定死唯一不可删；附加币种带有效期汇率（无结束日=永久） | p145-146 |
| Compute cost | 成本计算/重算 | 成本在加载时计算；配置改动涉及存量必须 Force 重算；错误看 NMCLD_CostCalculation 与重算日志 | p117, p176-180 |
| No first carrier found | 成本日志典型错误 | 两类根因：前缀漏配无匹配运营商；号码落在多运营商被叫区无法抉择而放弃计价 | p180 |
| Code book | 运营商配置文件集 | .inf/.rgn/.trf/.dir/.cal/.ccn/.adj/.fct/.itl/.trg 十文件；@表头/Tab 分隔/%注释；.itl 的 Node 须匹配目标机声明名 | p228-233 |

## 三、组织与成本归属域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Organization tree | 计费组织树 | 财务组织图形树（level/cost center/chargeable entry），呈现过去与现在；随 OXE 同步/事件与公司目录自动更新 | p253-256 |
| Cost center | 成本中心 | OXE 侧记账单位（编号即槽位，默认已建只配名字）；cc=255 未指定落组织根；修改只能经 OXE 配置或公司目录 | p89, p256 |
| Default cost center | 默认成本中心 | Data collection 页签配置的兜底：中继组/话务台组/语音信箱等无成本中心对象统一落此 | p257, p271 |
| Inactive entry（灰色条目） | 非活动历史条目 | 改名/换成本中心/复制后旧位置留下的带记录影子；ToolsOmniVista 全局更新前承担记录归属 | p258, p284, p287 |
| Cut & paste / Copy & paste | 剪贴/复制语义 | 剪贴=无历史搬移；复制=带历史另立（原件转 inactive 转灰，粘贴件 active） | p261-262 |
| Assign earlier creation date | 回溯创建日期 | 把非活动条目记录按身份（PCX ID/分机号）重挂到活动设备——只能选设备；level/成本中心/人不可回溯 | p263, p290 |
| ToolsOmniVista.exe | 服务器端运维工具 | 组织更新强制停 8770 服务、删除全部非活动实体并把票据与 Ptp 计数器重挂（不可逆，先归档） | p266, p293 |
| Cost profile / Invoiced cost | 成本档案/发票价 | 对总成本（直连+ISDN+间接）做线性 Ax+B 或百分比调整；+10% 即 A=1.1 或百分比 A=10 | p323-325, p333 |
| Subscription record | 订阅票 | 每次同步后生成的纯订阅费记录（日/周日/月一、时间戳 00:00:00）；月订阅次月 1 日起计；计算永不处理当天 | p327 |

## 四、机密控制域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Mask profile | 掩码档案 | 按呼叫类别控制被叫/主叫/PIN/成本/地名/时长/日期的显示与遮蔽位数；随组织树继承；Default 档案不可改名删除 | p298-302 |
| Masked / Unmasked group | 汇总报表专用类别 | 只存在于 Default 档案：grouped 报表无视组织树档案，一律按这两个类别遮蔽 | p300, p310 |
| Mask data access | 解密组 | 默认禁止无掩码报表；账号入组后生成 w/o mask 索要组员口令；改组须关闭并重开 Reports 应用 | p314-316 |
| Accounting domain | 计费可见域 | 挂组织树节点的域名；管理员配域后只见域内；未配域只见根；域按父继承；群组域无效只认用户级 | p343-346, p351-355 |
| AdminNmc | 主管理员账号 | 实验口径口令 Superuser01*；可见域机制下配根域（Alcatel）即全域可见 | p47, p343, p352 |

## 五、报表域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Report definition / Generated / Unmasked | 定义/实例/解密版 | 报表树三类节点；预定义报表必须 Copy/Paste 到个人目录才能生成 | p361 |
| Detailed / Grouped report | 详细/汇总报表 | Detailed 逐条不汇总（25 次呼叫 25 行）；Grouped 聚合（1 行）；Hit-list 限量仅 grouped | p385, p393 |
| Querytool / Designer | 选数/排版双页签 | Querytool 管字段/Operation/公式/Sort/Filter/hit-list；Designer 管区域/前后缀/小数位/图表 | p387-399 |
| View（同区域规则） | 视图区域 | 图表与公式只能取同一视图区域表头；嵌套汇总须把上层区域 View 切到下层 | p396 |
| Hit-list Report | 限量报表 | grouped 定义专用：只显前 N 名（如时长最长前 10 台话机、呼出最多前 3 台分机） | p393, p634 |
| Total counters | 累计计数器数据源 | 基于夜间算好的累计计数器，报表生成显著更快；实例为空先手工 Total calculation | p380-381, p385 |

## 六、性能监控域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| IP ticket / segment | VoIP 话单/通话段 | 每段 IP 通话结束出票（跨节点多段、双向各一票）；含压缩算法/丢包/时延表/BFI 密度 | p408-409 |
| KPI 阈值（Delay/Loss/BFI Burst） | 质量三阈值 | 默认时延>150ms、丢包>3%、BFI Burst>5%；BFI 是补造帧，通信 BFI>3% 才统计 burst（10 秒段占比） | p414, p422 |
| pmm 文件 | 话务观察计数器 | OXE 每半小时生成（/usr4/pmm，C<周><日><半小时><序号>，XX 占位）；流量分析专属（仅 OXE） | p433, p431 |
| PtpType ALL | 观察对象开关 | Daily/Weekly Job 计数任务默认只算话务台/组/中继组；改 ALL 才算被叫号与终端（两处都要改） | p446-447 |
| Tracking profile | 跟踪档案 | 阈值集合（Tracking value+Period+Threshold+Call Type+Action）；按实体类型挂默认或单条目指定；Reset Profile 全量强制 | p457, p478 |
| Variation rate | 变化率 | 100×(当前值−前 x 期均值)÷前 x 期均值；移动平均默认日 30/月 3/年 1 期；Max alarms 默认 50 | p462-463, p476 |
| CDR / RTCP-XR | 话终话单格式 | Web Performance 数据腿一：IP 设备专有格式、SIP 设备 RTCP-XR；经同步与小时轮询取回 | p492 |
| A4400-RTM-MIB / UC-DAVIS | SNMP 双 MIB | 数据腿二：专有（中继/压缩器/CAC/SIP 注册）+标准（CPU/磁盘健康）；SNMPv3 authPriv（SHA+AES） | p492, p510-512 |
| archZ | 归档文件 | zip 格式每天每节点一档；Archive delay 31（不带 D）+Clean-up delay 94D=最长 125 天，按记录日期清理 | p521, p523, p529 |
| Record origin | 记录来源标签 | Loaded=无标签进树与原始票不可区分；Archived=打标、树中不可见、报告可见、可 Only restored 单独清除 | p537, p548 |

## 七、产品与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniVista 8770 | 集中网管服务器 | ALE 集中网管：IP 连通纳管 OXE/OXO Connect/OpenTouch；thick client 五套件+WBM 四应用 | p5-11 |
| OmniPCX Enterprise（OXE） | 企业级 PBX | 计费数据源（CPU 双地址 csa 物理/csm 主）；实验机 R101.1-n4；计费/流量分析/审计仅 OXE 全量支持 | p5, p71, p25 |
| Thick client / WBM | 厚客户端/Web 门户 | 五套件全功能入口 / :8443 经 NETWORK MANAGEMENT 登录的轻客户端（Users 需 Unified Management 许可） | p10-39 |
| MariaDB / LDAP | 内部数据库与目录 | 计费票据与累计计数器存 MariaDB；目录 LDAP v3（LDIF/AD 同步为附加选项） | p7, p460 |
| RLAB / POD | 培训远程实验室 | 按 POD 划分的同构实验单元（网段 192.168.1.x）；公共区提供 NAS/SIP 模拟器/邮件服务器（实验口径） | p41-51 |
| ITSP1 | SIP 运营商模拟器 | 培训专用（gateway1.itsp1.com/public.itsp1.com，注册 pbxP/alcatel）；号码含两位 POD 号 PN（实验口径） | p53-58 |
| C:\8770 目录族 | 8770 数据与日志 | data\loader（回收）、data\collector（收集器）、log 五件套（同步/加载/成本两份/实时性能）、bin（ToolsOmniVista） | p80-114, p179, p517 |
| /usr4/account 与 /usr4/pmm | OXE 侧数据目录 | 计费与 VoIP 票据文件（TAX/IP/SIP DAT 与 LIS）/流量半小时计数器文件——排障第一站 | p65, p94, p433 |
| C:\8770_ARC\Accounting\tickets | 归档默认目录 | archZ 按天+节点存放；恢复对话框默认从此取 | p529 |
