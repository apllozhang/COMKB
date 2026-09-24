# VAA 多租户与树设计（公司/日历/营业时间、原生节点、三级用例 UC1-UC3）

## R — 原文依据

> "It is IMPERATIVE to personalize the NAME of each block when configuring a tree! This name is used by statistics and will facilitate the analysis"（p145）
> "The calendar, schedules and the filter must be created before the creation of the tree"（p175）
> "The Welcome prompt must be recorded in both languages in the same WAV file, because the choice of languages is only made after its broadcast."（p187）
> "Independent time zones … DDI range … Directory assistance type … Extension length"（p24）

出处：VSAAXTE001EN p22-39, p133-201。

## I — 自述

多租户上下文与树脚本是 VAA 的核心交付面，五个知识块：

1. **公司（租户）四要素**：独立时区、DID 段（树号取值范围，可用内线号）、留言前缀（OXE 留言箱号）、分机位长；超管可建公司（数量不限），公司资源含用户/路由/提示音/计划/目录/过滤器/树编辑器/统计
2. **时间类路由依据**：营业时间（时区/星期/时段）与日历（闭假日，可多日历用于同一树），既可在 Schedule 页签集中维护，也可在树内节点自定义——但必须在建树之前建好（依赖物先行）
3. **树与节点**：树是与路由号码绑定的呼叫处理脚本，节点拖拽编排；原生 12 种节点覆盖绝大多数需求

   - Start、Select language、Announcement（四种模式，Server file 不推荐）、Business hours、Calendar
   - Menu（最多 12 选项 0-9#*，重试/超时/重复键/最大重复）、Transfer（监督/盲转、Wait time、Bypass forward）
   - Voicemail、Filter（含 Unknown ANI）、Go to tree（仅同租户）、Record prompt（需租户用户 ID+PIN）、Release（命名进报表），另有 Comment 画布注释
4. **三级用例递进**：UC1 简单转接（欢迎 + 监督转 + 忙/无应答分支）；UC2 日历+营业时间+VIP 过滤分流（VIP 盲转 31001、非 VIP 盲转 31002）；UC3 多语言菜单（双语同文件、语言选择菜单、四选项主菜单含播报/盲转/留言/跳树）
5. **路由绑定与纪律**：VAA 内 Routing 菜单把 DID 绑到树并点图标激活（Forbidden 图标切换）；推荐一号一树，通配符 ?/*/号段"可用但不推荐"（歧义规则在 Administration Guide 4.3）；每个节点必须个性化命名——名称直接进统计与呼叫日志

## A1 — 书中案例

**UC2 日历+过滤分流树**（p173-184，实验口径分机号）：

1. 前置：建日历 Calendar2（闭假日）、营业时间 Business hours company1（9-12、14-18）
2. 前置：建过滤器 VIP filter（内容 31000，多号码可逗号分隔）
3. File/New 建树，Start 命名 Customers services，选公司默认语言后保存
4. 加 Announcement 命名 Welcome customers，TTS 欢迎语，与 Start 连线
5. 加 Calendar 节点选 Calendar2：营业日走 Business hours 分支，闭日走闭馆提示
6. 加 Business hours 节点选前置营业时间：时段内走下一节点，非时段走闭馆提示
7. 闭馆提示 Announcement 接 Release 块，逐节点连线
8. 加 Filter 节点选 VIP filter：命中走 Filtered 连线，未命中走 Unfiltered
9. VIP 转接节点：目的地 31001、盲转，接 Filtered 连线
10. 非 VIP 转接节点：目的地 31002、盲转，接 Unfiltered 连线
11. 保存树；Routing 绑 31402 并点激活图标
12. 验收：31000 拨打走 VIP 路径，其他分机走非 VIP 路径，闭日播闭馆提示

## A2 — 未来触发

使用情境：给客户建租户；按营业时间/假日分流；VIP 客户识别；多语言 IVR；菜单重试与异常路径；树绑号与激活；节点命名与统计。

语言信号：公司/tenant / 时区 / DID 段 / 日历 / calendar / 营业时间 / business hours / 过滤器 / filter / VIP / 树 / tree / 菜单 / menu / 转接 / transfer / 多语言 / 双语 / 路由号码 / routing number / 节点命名。

与相邻能力区分：提示音与 TTS 引擎归语音资产能力；收号/HTTP/SQL 等增值节点归 IVR 选项节点能力；OXE 侧把呼叫送进 VAA 归安装对接能力。

## E — 可执行步骤

输入契约：客户业务需求（语言/时间规则/VIP 名单/菜单结构）、公司四要素参数、树号段（落在公司 DID 范围内）、提示音资产（依赖语音资产业务先行）。

1. 建公司：名称 + 时区 + DID 段 + 留言前缀 + 分机位长；点公司名左侧对勾进入其配置。完成标准：公司出现在租户列表且可选中
2. 建时间依据：Schedule 页签下营业时间（按时段/星期/时区）与日历（闭假日）。完成标准：可在树节点中被引用
3. 建过滤器（如需）：表达式或 CSV（注意 CSV 导入清空已有条目）。完成标准：Filter 节点可引用
4. 建提示音：全部先于建树完成（UC3 还要求双语同文件）。完成标准：节点可引用
5. 建树：File/New 起 Start 块，按用例模板拖节点，每建一个立即与前一个连线并个性化命名。完成标准：画布无未连线节点、无默认名
6. 路由绑定：Routing 菜单输号码选树，点激活图标；推荐一号一树。完成标准：状态为激活
7. 验收：按用例测试清单拨打（正常/忙/无应答/闭日/异常输入），对照预期行为逐项核对。完成标准：测试清单全过

判停点：

- 需求要"跨公司复用同一棵树" → 停，Go to tree 仅限同租户，多租户共享话术须各建一份
- 客户坚持通配符号段绑定 → 停，说明"可用但不推荐"与歧义风险，指向 Administration Guide 4.3
- 建树中才发现提示音没建 → 停，回步骤 4，不要用未命名默认资源硬凑
- 菜单要超过 12 个选项 → 停，原生 Menu 上限 12 键（0-9#*），需重新设计菜单层级

输出契约：可用的公司租户 + 激活状态的树 + 按测试清单通过记录 + 节点命名清单（供统计排障）。

## B — 边界

- 节点不命名 = 放弃统计排障能力，原书三处大写强调（n21）
- 双语树的欢迎语/语言选择语必须双语同文件（语言选择发生在播报之后，n22）
- 破坏性操作：过滤器 CSV 导入清空全部条目、目录 OXE 电话簿同步清空手工条目——同步/导入前先导出（n18）
- Record prompt 远程录音要求租户用户 ID+PIN，无匿名通道（n38）
- Announcement 的 Server file 模式原书标注 not recommended
- 多语言语音选择前的提示与 ASR 菜单档位的组合行为书内未展开实验，复杂场景需实测
- 通配符路由表达式的歧义消解规则在 Administration Guide 4.3，教材不负责解释（n17）
