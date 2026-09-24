# Rainbow 管理员工具（权责分工、企业目录、信息频道）

## R — 原文依据

> "The 'Roles' tab is used to assign administrative rights to the client company. • It is possible to have several administrators to manage the company."（p59）
> "By default, a customer administrator can manage the directory. You can delegate the management to other Rainbow users, who are not necessarily administrators"（p60）
> "Only users with an 'Enterprise' service level can create Information Channels."（p61）

出处：RAINXTE001EN p56-62。

## I — 自述

管理面三件事：

1. **权责分配**：Roles 页签授管理权；BP 管理员与 EC 管理员权责分工（BP 专属：建 PBX/开付费订阅）；可设多名管理员；完整角色矩阵查 help.openrainbow.com Features List/Administration
2. **企业目录**（Business Directory）：存外部联系人及号码（提升来电识别）；默认客户管理员管理、可委托非管理员；手工创建或 CSV 批量导入（样例文件 + 导入报告）
3. **信息频道**（Information Channels）：先在 Roles 授权 → 仅 Enterprise 服务级可创建；可设"全员自动订阅且不可退订"的强制频道，或跨公司开放

## A1 — 书中案例

**配置序列**（p60-61，讲义截图级）：目录两步——开权限 → 手工/CSV 导入（出报告）；频道两步——Roles 授权 → 创建（选全员强制订阅或自选成员强制订阅）。

## A2 — 未来触发

使用情境：加管理员；外部联系人号码进 Rainbow；来电显示公司名；发公司通告频道；频道成员退不了订。

语言信号：管理员权限 / roles / 企业目录 / business directory / CSV 导入联系人 / 信息频道 / information channel / 通告 / 委托管理。

与相邻能力区分：成员账户本身的管理 → 成员生命周期能力；公司创建与订阅 → 公司与订阅能力。

## E — 可执行步骤

输入契约：管理员账号、委托对象及其服务级别、外部联系人清单（CSV）。频道创建者非 Enterprise 级 → 判停先调级。

1. 授权：Roles 页签给委托对象开对应权限。完成标准：对方可见对应管理面
2. 企业目录：开目录管理权 → 手工建或 CSV 导入 → 核对导入报告。完成标准：外部联系人可被检索与识别
3. 信息频道：确认创建者 Enterprise 级 → 创建 → 选择订阅范围（强制订阅须谨慎）。完成标准：频道上线

判停点：

- 强制订阅频道的内容无长期维护承诺 → 停，先与内容负责人确认（成员不可退订）
- 需要的权限入口缺失 → 对照服务级别门槛（SSO=Enterprise、AAD 导入=Voice Enterprise、频道=Enterprise），缺级先升级

输出契约：管理权分配表 + 目录导入报告 + 频道清单（含订阅范围）。

## B — 边界

- 服务级别三门槛（p53/p92/p61）：操作前核级别，避免白折腾
- 目录之外的联系人与 AAD 的关系：AAD 通讯录搜索是成员/同事域，Business Directory 只存外部联系人（p60）
- 管理操作全量入操作历史（p189）：多管理员并行时可审计谁做了什么
