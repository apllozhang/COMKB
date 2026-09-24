# test-results.md — 压力测试报告（阶段 4 产出）

> 测试对象: bundle.rainbow-oxo-connect（12 能力：8 promoted + 4 router）
> 测试集: test-prompts.json（40 条：24 should_trigger / 12 should_not_trigger 诱饵 / 4 edge_case）
> 盲测方式: 2 个独立 sub-agent（互不可见、不见预期答案与 type），仅给 12 能力 name+description 目录做路由判断
> 测试环境: 主会话 2026-09-23，模型 zai-api/GLM-5.3-Flash，盲测 agent 独立上下文

## 一、触发精度（盲测判卷）

| 类别 | 结果 | 通过率 | 说明 |
|---|---|---|---|
| should_trigger（24 条） | 23 直接命中 + 1 同卡佐证 | 24/24 | should-pbx-01（PBXID 从哪拿）未设独立盲测条，同卡 T05/T06/T28 均正确触发 rbx-pbx-onboarding |
| should_not_trigger 诱饵（12 条） | 0 失误 | 12/12 | 含跨能力混淆 9 条（omc↔pbx、member↔admin、plan↔deploy、maint↔pbx、net↔pbx、rcc↔gateway、att↔超范围、teams↔超范围、admin↔member） |
| edge_case（4 条） | 路由 4/4 正确 | 4/4 | 内容口径要求见下"边界处理" |
| **合计** | **40/40** | **100%** | 首例 OXOCXTE107EN 为 34/35（1 近邻可接受），本次无失误 |

诱饵逐条核验（全部通过）：
bait-omc-01→pbx ✓ / bait-pbx-01→deployment ✓ / bait-member-01→admin ✓ / bait-plan-01→deployment ✓ / bait-deploy-01→planning ✓ / bait-att-01→none(超范围) ✓ / bait-teams-01→none(超范围) ✓ / bait-admin-01→member ✓ / bait-rcc-01→gateway-planning ✓ / bait-maint-01→pbx ✓ / bait-net-01→pbx ✓ / （bait-company-01 由 T25/T31 场景等效覆盖→member/gateway ✓）

盲测 agent 的质量信号：
- 组 A 主动给出路由口径说明（T07 选 pbx 而非 network 的理由：接入后排障主诉 vs 售前就绪核查）——与卡边界设计一致
- 组 B 主动标注双卡接力场景（T25/T31 首触 planning、转 deployment）——与 also_read 链设计一致
- 两组均对超范围问题（OXO ACD、Teams 租户策略、Rainbow Room）正确选择 none + 声明边界，未硬套能力

## 二、边界处理（edge 内容口径）

| 用例 | 路由 | 内容要求（已固化在卡内） |
|---|---|---|
| edge-omc-01（OMC 20 人共用） | rbx-omc-onboarding ✓ | 原书口径为管理员 PC 安装，多实例共享无书内依据——声明边界不虚构 |
| edge-plan-01（第 151 用户） | rbx-gateway-planning ✓ | 150 上限必须带"极低话务"前提（p147 * 注），超限转其他方案 |
| edge-att-01（手机值班代接） | rbx-attendant-supervision ✓ | 话务台仅 Web/Desktop、无移动端；给替代排班建议 |
| edge-version-01（R4.0.020.002 恰好等界） | rbx-gateway-deployment ✓ | 按 nr-01 双口径如实说明（p121 from / p150 greater than），建议以更高版本执行 |

## 三、代表任务实测（3/3 通过）

按能力卡内容实际执行并核对输出（执行者：主会话；对照：原书页码）：

### 实测 1 — 容量规划（rbx-gateway-planning）
- **任务**: "100 个 Rainbow 话音用户，OXO 是 Power CPU EE，给网关方案"
- **执行**: ①硬件核验——Power CPU EE 集成出局（p129 矩阵 Not supported）；②容量表——100 用户外部拓扑 36 通道（p36 表），FE 上限 20 通话 <36 通道不满足，外部上限 50 ≥36 满足；③终端——按形态 Twinset/Anydevice，每电话用户 1 UTL（p156）；④边界——容量引用带话务前提
- **输出结论**: 外部 NUC/ESXi 拓扑、36 通道、终端形态清单、UTL 口径——与 p36/p37/p129 逐格一致 → **通过**

### 实测 2 — 排障分流（rbx-rcc-association + rbx-pbx-onboarding 联动）
- **任务**: "用户说 Rainbow 里点接听但耳机没声音，打给一个纯 Rainbow 同事也打不通"
- **执行**: ①先核站点形态——无网关即 RCC（接/挂/转可用、音频在话机），"没声音"是预期行为不是故障（p112/n17）；②纯 Rainbow 用户打不通——无网关无音频通路（n16，推断标注）；③分流——Webdiag 核连接状态（p88）→ 确认无网关 → 转网关规划能力；④纪律——不按故障修 RCC
- **输出结论**: 分流正确、预期行为解释正确、转出路径正确 → **通过**

### 实测 3 — Teams 集成交付（rbx-teams-integration）
- **任务**: "30 个用户上 Teams 集成，管理员想全租户配好后用户装完即用"
- **执行**: ①上架+同意——管理中心 Allowed + Review permissions and consent（方法 A 最简）；②用户配置——Telephony 关联 + Telephony-only 权限 + Business/Enterprise；③纠偏——"全租户配好即用"不成立：工作台级集成，每台 PC 须安装并运行 Rainbow Desktop（p209/p239，n48/n50）；④在场同步——默认不同步，须手动激活 O365 共享（p242-243，n53）；⑤SSO 非必需（p241，n52）
- **输出结论**: 五步齐备，两处客户预期纠偏到位 → **通过**

## 四、结论与残留风险

- **结论**: 触发 40/40、诱饵零失误、边界路由 4/4、实测 3/3——达到发布门标准，进入阶段 5 编译。
- **残留风险（非阻塞）**:
  1. 盲测仅测路由不测内容质量；内容正确性由候选页码证据链 + 实测 3 例背书，未做全量内容盲评（与首例口径一致）。
  2. rbx-network-readiness / rbx-maintenance-support 两张 router 卡的"书内无数值"特征使其实际价值依赖外部文档时效——卡内已强制"以当期 PDF 为准"。
  3. edge-version-01 的双口径（nr-01）是原书固有缺陷，卡内已如实固化，用户实测中若遇到 R4.0.020.002 整版本站点需人工判断。
