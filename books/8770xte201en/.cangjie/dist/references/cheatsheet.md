# 决策规则速查 — OmniVista 8770 R5.2 Accounting and Performance Administration (Participant Guide, Edition 45)

| 能力 | 一句话规则 |
|---|---|
| OXE 纳管与 SIP 中继对接 | 先在 OXE 核 siteid/SSH/信任主机，再按 网络号×100+节点号 声明节点并同步验证；SIP 模拟器按 POD 配 pbxN 与 DID 翻译 |
| 计费票据管道（出票、回收、加载过滤） | OXE 缓冲 500 条或 90 分钟落盘成 TAX 与 ACCOUNT.LIS，8770 对比索引 FTP 增量取回、过五道加载闸入库；FTP 用户 adfexc 禁改 |
| 运营商资费建模与成本计算 | Period 下的 Calendar/Region/Tariff/Direction 五件套建模，exact/round/pulse 公式族算价；改配置必须 Compute cost（Force）重算存量 |
| Code Book 导出与导入 | 十种文本文件 @表头/Tab 分隔/%注释；导出两次才完整；.itl 的 Node 必须等于目标机声明名；改 EFFECT_DATE 导入等于新增周期 |
| 计费组织树与成本归属 | 成本中心从 OXE 同步（cc=255 落根）；分机改归属只能回 OXE 配置；剪贴无历史、复制留灰条目；回溯选设备不选用户 |
| 计费机密控制三道闸（掩码、解密、可见域） | 掩码档案按树继承遮显示、解密须 Mask data access 组口令且改组要关 Reports、可见域开启后未配域只见根且群组域无效 |
| 成本档案（发票价与订阅费） | 发票价=总成本线性或百分比调整（+10% 即 A=1.1 或 A=10）；订阅票日/周日/月一，月订阅次月 1 日起计 |
| 报表生成、导出与定时 | 预定义报表复制到个人目录才能生成；TXT 400 行/PDF 50 页/库 100000 行上限；累计报表空表先 Total calculation 补算 |
| 报表定制（Querytool 与 Designer） | Querytool 管字段/Operation/过滤/hit-list，Designer 管版面/公式/图表；图表公式只能取同一视图区域字段，嵌套汇总须切 View |
| VoIP 性能监控（IP ticket 与 KPI） | 每段 IP 通话出 IP ticket；KPI 默认时延大于 150ms、丢包大于 3%、BFI Burst 大于 5%；报告有数的前提是话务走被监控承载段 |
| 流量分析与 Tracking 告警 | pmm 半小时计数器作流量报表；默认只算话务台/中继组须改 PtpType ALL；Tracking 阈值档案挂实体类型，变化率按移动平均默认 30/3/1 期 |
| Web Performance 实时仪表盘 | VoIP CDR 与 OXE SNMP MIB 两条数据腿喂五大主题 widget；R5.0 MD1 起轮询可从 30 分钟缩到 5 分钟；配置不一致即告警停用 |
| 计费归档与恢复 | 31 天归档成 archZ、再 94 天清理（最长 125 天按记录日期）；恢复选 Loaded 与 Archived 标签决定可否区分与单独清除 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
