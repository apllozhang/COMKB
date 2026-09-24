# 8770xte201en 盲判结果（仅依据能力目录，锁定后不改）

case-id | slug或none | 理由一句
should-node-01 | ovbill-node-onboarding | 新 OXE 接入计费的第一步核查与节点三级声明正是纳管能力核心
should-node-02 | ovbill-node-onboarding | 同步验证与日志排查、信任主机范围属纳管侧核查
should-pipe-01 | ovbill-ticket-pipeline | 打了电话看不到话单，按采集-过滤-加载的票据管道顺序排查
should-pipe-02 | ovbill-ticket-pipeline | OXE 外部计费参数与 0 计费呼出也有记录属票据生成侧
should-tariff-01 | ovbill-tariff-costing | 时段价目加接通费属资费公式族建模
should-tariff-02 | ovbill-tariff-costing | 存量话单按新价目重算即 Compute cost (Force)
should-codebook-01 | ovbill-codebook-migration | 导入报错方向建不出来指向二次导出才完整等迁移规则
should-codebook-02 | ovbill-codebook-migration | 新旧费率按日期并存即 EFFECT_DATE 改期导入等于新增 Period
should-org-01 | ovbill-org-costing | 分机拖不动因搬移权限二分，只能经 OXE 配置改
should-org-02 | ovbill-org-costing | 用户更替后记录归属靠组织树与回溯对象处理
should-conf-01 | ovbill-confidentiality | 按人掩码与经理看全号即掩码档案继承与解密组口令
should-conf-02 | ovbill-confidentiality | 可见域开启须重启且未配域只见根，不是数据丢失
should-cost-01 | ovbill-cost-profile | 加管理费加每通手续费即发票价 C+S 双资费，按月收话机费即月订阅
should-report-01 | ovbill-reporting | 报表导出 PDF 邮件与 Schedule 定时属报表生成能力
should-report-02 | ovbill-traffic-tracking | Daily Station Traffic 属 pmm 话务观察对象报表，空表先查话务数据源
should-design-01 | ovbill-report-design | 嵌套汇总切 View 加双币种表达式属 Querytool/Designer 定制
should-design-02 | ovbill-report-design | 前 10 排行即 Hit-list 且仅 grouped 支持
should-voip-01 | ovbill-voip-monitoring | 时延丢包等 KPI 与质量报告属 VoIP 监控
should-voip-02 | ovbill-voip-monitoring | 质量报告空表排障，话务须走被监控承载段
should-traffic-01 | ovbill-traffic-tracking | 中继话务量与被叫号码维度即 pmm 六类观察对象
should-traffic-02 | ovbill-traffic-tracking | 话费超阈值发邮件即 Tracking 阈值档案与告警邮件
should-web-01 | ovbill-web-performance | 实时健康大屏与轮询周期属 Web Performance 仪表盘
should-web-02 | ovbill-web-performance | SNMPv3 口令变更断数据腿且配置不一致即告警停用监控
should-archive-01 | ovbill-archiving | 旧话单归档且可查回即 archZ 与恢复
should-archive-02 | ovbill-archiving | 31 不带 D 与 94D 必带 D 是归档参数规则
bait-pipe-vs-node-01 | ovbill-ticket-pipeline | 同步成功且 loader 有文件说明纳管正常，看不到新话单应查加载过滤等管道下游
bait-tariff-vs-cost-01 | ovbill-cost-profile | 成本加成 15% 卖内部是发票价百分比调整，题面猜的运营商资费参数正是诱饵
bait-report-01 | ovbill-report-design | 现成模板不满足要从零定义嵌套汇总报表属 Designer 定制而非用报表库
bait-conf-vs-report-01 | ovbill-confidentiality | grouped 报表只认 Default 档案，无需逐成本中心改档案
bait-voip-vs-traffic-01 | ovbill-traffic-tracking | 呼叫数量与占用率是话务量指标，VoIP 质量报告不含话务量
bait-outofscope-01 | none | 法国 08 特服官方监管费率表属外部信息源问题，教材能力只覆盖建模不提供现价数据
bait-outofscope-02 | none | MariaDB 磁盘扩容与备份策略规划属基础设施容量设计，超出目录全部能力
bait-org-vs-archive-01 | ovbill-org-costing | 灰色条目来自复制留灰、ToolsOmniVista 全局更新停服务不可逆均属组织树能力
edge-lab-01 | none | 教材实验口令能否上生产属安全边界声明，目录无对应计费能力
edge-voip-02 | ovbill-voip-monitoring | MOS 与 KPI 归 VoIP 监控，具体公式教材未必给出需声明边界
edge-tariff-02 | ovbill-tariff-costing | 练习里汇率取值属币种与资费建模参数问题
edge-multi-01 | ovbill-ticket-pipeline | 5 台 OXE 加 2 台 PCS 的生产化差异集中在回收收集器架构，不能照搬单节点实验
edge-report-03 | ovbill-reporting | 100000 行库扫描上限属报表六项尺寸上限
