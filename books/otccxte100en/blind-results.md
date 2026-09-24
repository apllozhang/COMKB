# 盲判结果 · otccxte100en

判定依据：仅 blind-input.json 中的 capability_catalog（13 项能力）。逐条凭第一判断锁定，未参考答案。

```
should-matrix-01 | otcc-ccd-matrix-foundation | 从零搭呼叫中心建 pilot/队列/处理组的顺序即基础矩阵创建流程
should-matrix-02 | otcc-ccd-matrix-foundation | acdsup 的 A/F/V/CLO/OPN 判读是矩阵验证能力的明确内容
should-ccs-01 | otcc-ccs-installation | 班长台安装决策链与 node1 直连后必须重启解释连不上的原因
should-ccs-02 | otcc-ccs-installation | 两台 CCS 打架对应 ccs.ini 的 id_terminal 0..127 唯一性
should-rules-01 | otcc-routing-distribution-rules | 对象连好后仍不通，典型原因是分配规则默认停用须 OXE 激活、方向默认关闭
should-rules-02 | otcc-routing-distribution-rules | 常态与饱和的路由方向、优先级 0-9 平局规则正是路由分配规则能力
should-agent-01 | otcc-agent-supervisor-onboarding | 固定/移动座席形态区分与班长创建是座席班长开通过程
should-agent-02 | otcc-agent-supervisor-onboarding | 前缀登出没反应对应 ACD 前缀动作表与 COS 放行问题
should-tune-01 | otcc-object-tuning | 话后自动休息时间即 wrap-up 参数，挂 pilot/PG 两种口径
should-tune-02 | otcc-object-tuning | 服务水平 85%/15s 与 smiley 三色 0.8 阈值正是对象调优内容
should-sup-01 | otcc-supervisor-features | 旁听与三方介入即监听三态 Listen/Restrictive/Intrusion
should-sup-02 | otcc-supervisor-features | 业务号定时切换到手机即通用转发的日历/按规则激活方式
should-vg-01 | otcc-voice-guides | 专业 wav 入库需 A-Law/8000Hz 转换与 SFTP 导入，属语音指南能力
should-vg-02 | otcc-voice-guides | 座席个性化问候即 538 欢迎指南 4500 消息池每座席 5 条机制
should-mon-01 | otcc-monitoring-statistics | 大屏实时排队与座席状态即 Navigator 3 秒快照监控
should-mon-02 | otcc-monitoring-statistics | 月底接话量/弃呼/分账报表即 Excel 报表统计能力
should-mlcal-01 | otcc-multilanguage-calendar | 不同号码听不同语言提示即 Multi-language 指南一号多语言
should-mlcal-02 | otcc-multilanguage-calendar | 周末节假日自动闭门即日历 50 特殊日覆盖与切换点机制
should-queue-01 | otcc-queue-experience | 您前面还有 N 位播报即 518 位次播报能力
should-queue-02 | otcc-queue-experience | 按预计等待播不同话术即 EWT 表 6 阈值挂 parking level
should-dc-01 | otcc-direct-calls-emergency | 直拨座席工号纳入统计与话后处理即 direct call pilot 机制
should-dc-02 | otcc-direct-calls-emergency | 一键关停所有业务号并播提示即紧急关闭功能
should-sp-01 | otcc-statistic-pilot | VIP 来电显示 GOLD 标签即 Call Tag ≤32 字符振铃期显示
should-sp-02 | otcc-statistic-pilot | 多业务线各自欢迎语与统计、一套座席即统计型 pilot 先问候再转路由 pilot
should-lab-01 | otcc-lab-connectivity | MicroSIP 打公网号核对 SIP 网关 pbxN 与 DID 翻译即实验环境链路内容
should-lab-02 | otcc-lab-connectivity | ABC-F 双 access 建链与 hybvisu/rsthyb 验证即实验链路能力
bait-rules-01 | otcc-object-tuning | 队列饱和改道是队列参数 Queuing overflow，属对象调优而非新建路由规则
bait-tune-01 | otcc-agent-supervisor-onboarding | 登出键没反应根因在前缀动作/COS 放行，计时器参数是误导方向
bait-vg-01 | otcc-queue-experience | 排队位置报数属 518 位次播报体系，应激活排队体验能力而非普通语音指南
bait-mon-01 | otcc-object-tuning | 服务水平阈值取值与三色判定是对象调优参数，不是监控搭建问题
bait-dc-01 | otcc-supervisor-features | 业务号临时切手机是通用转发的 CCS 激活，与 direct call pilot 无关
bait-sp-01 | otcc-direct-calls-emergency | 直线打到座席并计统计正是 direct call pilot 的呼叫性质判定场景
bait-matrix-01 | otcc-queue-experience | IAA 树层与选项上限（5 层 4 选项 8 树）属排队体验能力而非矩阵基础
bait-out-01 | none | ACR 技能档按语言路由不在 13 项能力目录内，超范围
bait-out-02 | none | 按话务量算队列数与招聘坐席属话务规划，超出教材能力目录
bait-out-03 | none | CCS 多站点集中管理部署超出安装能力目录（仅 Full/Monosite 决策链），超范围
edge-lang-01 | otcc-multilanguage-calendar | 英文放语言槽 1 还是 2 需按目标库核对，正是多语言能力的口径边界
edge-pwd-01 | otcc-lab-connectivity | WebAdmin 密码以哪个为准属实验环境口径，应查实验环境约定
edge-cmd-01 | otcc-ccd-matrix-foundation | acdsup 与 acdsetup 之争属矩阵验证命令口径，归属矩阵基础能力
edge-abc-01 | otcc-lab-connectivity | ABC-F 链路版本基线与是否自建属实验链路口径问题
```
