# 多站点配置（Sites、站点主号、站点 MoH）

## R — 原文依据

> "Note: here there is only one Rainbow company, and therefore only one Cloud PBX."（p92）
> "Select whether the user will be able to present the company number (set to 'Not allowed' for users outside the main site)."（p93）
> "Regardless of the multi-site configuration, the following functions remain unchanged within the company: • Internal calls are available between company members at different sites."（p304）

出处：RAINXTE101EN p91-93, p301-316。

## I — 自述

多站点是一公司一 Cloud PBX 下的逻辑分区，不是分 PBX：

1. **站点挂什么**：成员（成员编辑页 Information 的 Sites 字段）、公网号与可配号服务（组/欢迎服务/AA 经公网号归属站点）
2. **站点级配置**：站点默认公网号（未配个人号的站点成员外呼，被叫看到的是站点号）；站点级音乐保持（覆盖公司级）；站点独立问候语
3. **跨站点不变量**（p304）：内呼互通、组成员可跨站、欢迎服务/AA 全公司共用（可经号码标识归属）、企业目录全站共用、一个号码可同时充当公司主号与站点主号、不强制所有号码/成员都挂站点
4. **参数红线**（p92-93）：每站内部分机号段分段只是便于管理的建议，非强制；全部 DDI 仍归公司号码池；副站点用户"允许改外呼号"与"呈现公司号"两项建议显式设 Not allowed（默认可改）

实施四步（p305）：建站点 / 分配用户 / 号码与服务关联 / 站点 MoH。

## A1 — 书中案例

**两地站点配置**（p307-316，How-To）：

1. 以 BP 管理员登录 / Customer company / Informations / Sites 页签 → Create。
2. 建两个站点：Brest 与 Rennes（实验口径）。
3. Members 菜单编辑成员：Alice、Bob 挂 Brest；Carol、Dave 挂 Rennes。
4. Sites 页签按成员或按公网号两种入口核对分布。
5. 编辑一个 AA 的 Informations → Site 选 Rennes → 勾 set as site phone number。
6. Voice prompts 页签 / Site 区 → 选 Brest 上传站点 MoH → 同法配 Rennes。

验收口径：Sites 页签显示两站点及其成员/号码；AA 挂 Rennes 且其号码成为站点主号；两站点 MoH 各自生效。

## A2 — 未来触发

使用情境：客户两地/多址办公；分支机构外呼要显示本地号码；各分店要自己的等待音乐；"要不要给分部再买一台 PBX"；副站点成员乱改主叫号。

语言信号：多站点 / multi-site / 站点 / site / Sites / 站点主号 / site phone number / 站点音乐 / MoH / Brest / Rennes（实验）/ 号码池 / DDI / 内线分段。

与相邻能力区分：PBX 声明与号码池归 Cloud PBX 能力；成员 Sites 字段操作入口归成员管理能力；DID 地址登记（紧急定位）归呼叫组能力边界与网络就绪口径。

## E — 可执行步骤

输入契约：站点清单与人员分布、号码资源分布（各地 DDI）、是否需要站点主号/站点 MoH、主叫权限管理要求。

1. 建站点：Informations → Sites → Create（一公司仍只有一个 Cloud PBX）。完成标准：站点在列
2. 分配用户：编辑成员 → Information → Sites 字段选站。完成标准：成员分布与实际办公地一致
3. 关联号码与服务：编辑公网号/服务（组、欢迎服务、AA）→ Site 选站 → 按需勾 set as site phone number。完成标准：站点主号确定
4. 配站点 MoH：Voice prompts → Site 区 → 选站点上传。完成标准：站点等待音乐生效
5. 收紧主叫权限：副站点成员 Telephony 页签"改外呼号/呈现公司号"设 Not allowed。完成标准：抽拨验证主叫显示符合预期

判停点：

- 客户预期"每站点一台 PBX/每地一条中继" → 停，纠正：站点是单 PBX 逻辑分区，PBX 数量不随站点走（n11/n15）
- 副站点成员可改任一公司 DDI 作主叫 → 停，这是默认行为漏收紧（n16），按步骤 5 显式 Not allowed
- 紧急定位要按分部地址 → 停，DID 地址登记在 BP/运营商侧（p229，n41），购号清单按站点单列
- 想按站点隔离目录或内呼 → 停，目录与内呼全公司共用是设计行为（p304），隔离诉求超出站点机制

输出契约：站点分布表（成员/号码/服务/主号/MoH）+ 主叫权限收紧记录。

## B — 边界

- 站点内线分段是建议不是机制（p92）；不分段也能跑，但目录与话务可读性差
- 实验"Rennes 无本地区号、号码沿用培训号段"为实验口径（p311，needs-review nr-06）
- 多站点常量清单（p304）为 Sprint 170 口径，版本演进以 Features List 为准
- 站点 MoH 覆盖公司级 MoH；两级 MoH 的优先级关系在拨测时确认
- 跨站点欢迎服务归属靠号码标识——服务挂站操作在号码/服务编辑页，不在站点页
