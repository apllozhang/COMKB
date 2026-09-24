# 寻线组、代接组与速拨编号体系（Hunting、Pick-up、Speed Dialing）

## R — 原文依据

> "Search types • Sequential • Cyclical • Parallel"（p299）
> "% authorized camp on calls = Max. Number of camp on calls authorized / number of active stations in the hunt group x 100"（p305）
> "A SET CAN BELONG TO ONLY ONE HUNTING GROUP"（p318）
> "This table can contain up to 32500 numbers, indexed from 0 to 32499 … by default, only the first 4000 indexes are configurable."（p238, p247）
> "A speed dial number is subject to barring tables for access to the public network only when declared as barred"（p236）

出处：ENTPXTE401EN p234-254, p296-326。

## I — 自述

团队话务三件套：寻线组管"谁来接"，代接管"别人帮着接"，速拨管"拨得快"。

1. **寻线组三搜索**：Sequential（固定队头顺序）、Cyclical（队头轮转均摊）、Parallel（并发同响先接）；溢出号在组空或 camp-on 百分比到限时启用（公式=最大允许 camp-on 数/组内活动站数×100），目标可为话机/另一寻线组/话务台
2. **COS 随进出组**：入组即用组的 Connection COS/公网 COS/实体（公网 COS 留 255 保留成员自己的）；进出组前缀默认 480 入/481 出（p304/p320 口径，见 B 段勘误）；默认禁末位成员退组（退光转溢出号或忙音）
3. **multiline 三分支**：仅 Cyclical/Sequential 组可含 multiline；系统参数 No Multi-line call in PCX（0/1/2，默认 1）决定忙机是否落空闲键
4. **代接两式**：组代接（拨前缀接同组振铃话机）与直接代接（前缀+号码）；需 COS 授权且被叫未受代接保护；Pickup 组无独立建组菜单——用户属性填 PickupGroup Name 即自动成组；zdpost 查 pickup_id（组索引/-1 不在组）
5. **速拨体系**：统一索引表 0-32499（默认仅前 4000 可配，cfgUpdate 扩容需重启）；直接式全网统一段（不可与范围段重叠）+范围式（至多 400 范围可互叠、每实体至多 32 区）；每号可带目录名（入局按 Calling ID 显示、支持 call by name）
6. **速拨行为**：默认绕过闭锁，逐号勾 Call Restriction-Barring 才受控；溢出缩位号（原中继不可用自动改发）；开放缩位号（不完整号补拨）+定时转发（超时自动补全）

## A1 — 书中案例

**寻线组与代接**（p316-326）：

1. 建组：Groups 里建 31300（Cyclical）并加成员；310x0 呼 31300 验证轮转，改 Sequential 复测
2. 进出组前缀核验：Prefix Plan 过滤 Set Features 的 Sta. Group entry/exit（默认 480/481，如缺则建）
3. COS 放行：Phone Features COS 的 Sta. group entry/exit=1，实测进出组
4. 维护：pbxstat -f d 31300（头成员/modcycle/组态/成员态）、supgpbx -le 全网组态
5. 代接：用户填 PickupGroup Name=Pickup Gr1 成组；COS 放行后同组拨组代接前缀、跨组拨直接代接前缀+号码
6. 核验：zdpost d 31001 显示 pickup_id=0（在组）、zdpost d 31000 显示 -1（不在组）

**速拨管理**（p246-254）：

1. 扩容：/usr3/mao 下运行 cfgUpdate，选 Abbreviated Numbers 输新上限，重启 OXE
2. 直接式：建紧急号 112（Call Number=0 112、Name=Emergency）与普通号 60（外呼屏显目录名）
3. 闭锁受控：系统闭锁禁外呼后，编辑 60 勾 Call Restrictions-Barring，用允许/禁止外呼用户对比测
4. 开放缩位号+定时溢出：前缀 2 不完整号补拨；640 完整号等计时器自动补发
5. 范围式：Range 0（Index=1000/Length=100/2 位）+ 实体映射（Area 0）+ 范围前缀 61，拨 61 00 测试
6. 查询：edabv -l GEA 按前缀/序号/号码检索（显示 60|1|00210141000 类记录）

## A2 — 未来触发

使用情境：客服/销售团队轮接；"电话在别桌响没人接"；挂短号拨常用客户；外呼管控（缩位号绕闭锁的合规风险）；组溢出到话务台的设计；忙机掉键行为调参。

语言信号：hunting group / 寻线组 / sequential / cyclical / parallel / 轮转 / camp-on / 溢出号 / 进组 / 出组 / pickup / 代接 / 组代接 / 直接代接 / speed dial / 缩位拨号 / 32500 / 4000 / edabv / cfgUpdate。

与相邻能力区分：multiline 键配置转多线监督能力；话务台排队属 Rainbow/其他域（本书仅寻线组溢出可指话务台）；组员监督键组合转多线监督能力。

## E — 可执行步骤

输入契约：组员名单与 COS、溢出策略（目标号/百分比）、速拨号段规划与闭锁策略。一台话机已在别的寻线组 → 判停（先出组或换号）。

1. 建寻线组：DN/名称/Search type/成员；multiline 成员确认组型支持。完成标准：pbxstat 组态与成员态正常
2. 配权利与溢出：COS 进出组放行、溢出号与 camp-on 百分比按公式核算。完成标准：组空/到限实测溢出
3. 建代接组：用户填 PickupGroup Name 成组 + COS 放行两式代接。完成标准：组代接与直接代接实测通过、zdpost pickup_id 正确
4. 速拨扩容：cfgUpdate 设新上限并重启（如需超 4000）。完成标准：可配置索引数达标
5. 建速拨号：直接式（紧急号+常用号）/范围式（区+前缀+实体映射）/开放与定时号。完成标准：拨测屏显与闭锁行为符合勾选
6. 巡检：edabv 查号、pbxstat/supgpbx 查组。完成标准：查询输出与配置一致

判停点：

- 用户要求"同时属于两个寻线组" → 硬限制不允许，用溢出号或并行组拼方案
- 闭锁合规审查发现缩位号绕行 → 逐号勾 Call Restriction-Barring 或收回号段
- 前缀拨了没反应 → 先到 Prefix Plan 实查实际值（55/56、480/481 存在教材勘误，nr-01），不背书
- parallel 组要放 multiline 话机 → 不支持，改 Cyclical/Sequential 或换非 multiline 机

输出契约：可用的组业务与代接（pbxstat/zdpost 证据）+ 速拨编号表（直接/范围/实体映射）+ 闭锁受控说明。

## B — 边界

- 一台话机只能属一个寻线组（p318 大写）；默认末位成员不可退组是服务保护开关（p304）
- 速拨总表 32500、默认 4000 可配、400 范围、每实体 32 区——扩容须重启（p236-p247）
- 代接与进出组默认前缀在教材 Note 与截图间存在互换（nr-01）——一律以现场 Prefix Plan 实查为准
- 问候导引（greeting guide）可向内部主叫替代回铃，留空则回铃（p305）
- ACD/CCD 分配坐席是另一体系，本书仅列为多设备禁用对象，不在本卡范围
