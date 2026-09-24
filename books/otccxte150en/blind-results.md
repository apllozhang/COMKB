# otccxte150en 盲判结果（仅依据能力目录，未读答案）

case-id | slug或none | 理由一句
should-script-01 | acr-script-editor-fundamentals | 第一条脚本从编写到保存传输、Pilot 激活闭环是编辑器能力核心
should-script-02 | acr-script-editor-fundamentals | LIT 是 asm_ag_free_duration 三值之一，排查走编辑器调试链
should-matrix-01 | acr-ccd-matrix-foundation | 普通链路与 ACR 链路双链路建对象正是 CCD 矩阵地基
should-matrix-02 | acr-ccd-matrix-foundation | hybvisu 混合链路校验是地基能力的验收手段
should-redirect-01 | acr-redirect-redistribution | 全忙转语音提示属重定向队列接 Voice Guide
should-redirect-02 | acr-redirect-redistribution | 空列表触发再分发及其次数后果是该能力触发规则
should-direct-01 | acr-direct-call-dica | 直拨忙等原人不换人要靠 ACR 直拨融合（无 ACR 则立即溢出换人）
should-direct-02 | acr-direct-call-dica | 临时禁止直拨对应 DICA 自动技能停用即完全不可直拨
should-intdb-01 | acr-internal-database-routing | 200 个 VIP 按主叫号查专属档案正是内部库三键路由（4000 条内）
should-intdb-02 | acr-internal-database-routing | Call Tag 键查名单正是内部数据库路由能力之一
should-combo-01 | acr-rule-combination-advanced | 名单加 ISM 失效对应多 APPLY 第一个失效的组合规则
should-combo-02 | acr-rule-combination-advanced | 混跑插队问题对应混跑选呼三序与 ISM 成本三档
should-asm-01 | acr-asm-deployment | ASM 迁独立 Windows 服务器割接与连不上 AFE 属部署能力
should-asm-02 | acr-asm-deployment | 主备双机脚本自动复制是 Main/Stand-By 机制
should-sql-01 | acr-database-query-routing | 外部 SQL 按主叫号查 VIP 与专属坐席正是 SQL 六构件
should-sql-02 | acr-database-query-routing | ASM 重启丢数据用 updateCalling 落库抗重启是该能力方案
should-list-01 | acr-list-rules | 圈定少数坐席接听用授权名单规则
should-list-02 | acr-list-rules | 按时段换名单仍是名单规则五式的应用
should-lang-02 | acr-multilanguage-voiceguide | 播报语言取档案偏好 1-7、偏好 1 优先正是该能力规则
should-calltag-01 | acr-call-tag-transfer | IVR 会员号传标签对应 CCivr TransferCall 前置 GetPilotInfo 的 Correlator data
should-calltag-02 | acr-call-tag-transfer | 转发后标签变 1500 对应转移链最后一个标签覆盖之前的规则
should-lang-01 | acr-multilanguage-voiceguide | 多语言欢迎语与按语言分配坐席正是该能力
should-filter-01 | acr-filter-statistics | 分业务线统计与合计口径对应过滤器 AND 与 Super/Hyper-Filter OR
should-filter-02 | acr-filter-statistics | 报表为空对应数据从创建起算的口径差异
should-script-03 | acr-script-editor-fundamentals | 屏显去前缀属字符串关键字与 DISPLAY_AGENT 脚本处理
should-combo-03 | acr-rule-combination-advanced | 等待阶段播不同内容涉及 IQUEUE 级别与脚本控制的组合运用
bait-script-01 | acr-ccd-matrix-foundation | 每 Pilot 规则条数与优先级数值是路由规则地基知识，非脚本编辑器
bait-script-02 | acr-list-rules | 授权名单容量（100 列表每表 30 坐席）属名单规则能力
bait-matrix-01 | acr-script-editor-fundamentals | 保存传输不生效且 Debugger 看不到新逻辑属编辑器调试链
bait-redirect-01 | acr-list-rules | 临时排除坐席用名单规则，非重定向
bait-direct-01 | acr-ccd-matrix-foundation | 普通 Pilot 全忙行为属基础矩阵普通链路知识
bait-intdb-01 | acr-internal-database-routing | 5 万条超内部库 4000 条上限，先查该能力容量约束再议外部库
bait-sql-01 | none | SQL Server 安装配置（Mixed Mode/sa 密码/重启）超出目录内各能力范围
bait-asm-01 | acr-database-query-routing | 脚本连不上外部库先查 32 位 ODBC 等查询约束，非 ASM 部署问题
bait-lang-01 | none | 录制提示音与录音代码属 CCivr 录音域，目录内多语言能力只管映射与偏好分发
bait-filter-01 | acr-rule-combination-advanced | VIP 排最前靠 IQUEUE 优先级；过滤器不影响分发，建过滤器不解决问题
edge-combo-01 | acr-rule-combination-advanced | IDLE 与 COM 互斥正是该能力组合约束
edge-calltag-01 | acr-call-tag-transfer | IAA 编码叶仅外部呼入，内部分机打不进是该能力明示边界
edge-retry-01 | acr-redirect-redistribution | 空列表再分发次数属该能力触发规则，精确次数需回书核对（边界）
edge-security-01 | acr-database-query-routing | 脚本内数据库连接串属外部查询能力，教材账号不可直接用于生产（边界）
edge-typo-01 | acr-database-query-routing | DNS=acr 连接串涉 32 位 ODBC 数据源；STRING_LENGHT 拼写需回书核对（边界）
