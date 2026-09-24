# OTFC Profile 策略与电话簿（默认两档、限制组、呼号限制、通知 Profile、LDAP 电话簿）

## R — 原文依据

> "By default, the Basic and No Faxing Rights profiles are available: • The Basic profile allows the user to fax at a normal fax priority. • The No Faxing Rights profile does not allow the transmission of faxes."（p118）
> "A barring table could be linked to one/several user profile(s) • E.g. National only: International numbers are forbidden"（p121）
> "'Exchange integration' has to be checked with 'Message body format: Text'. Format used for email notification, not for web access!"（p126）
> "There are two types of Phone Books: • Public (corporate): assigned to users through their profile • Personal (private): accessible and manageable only by each user"（p135）

出处：OTFCXTE200EN p117-139。

## I — 自述

Profile 是策略中枢，六块属性五种挂接：

1. **六块属性**：Profile information（名称/组织/电话信息）、Cover Sheets（默认与允许封页）、Billing Codes（三类计费码）、Fax Options（优先级/重试/分辨率等）、Security（选项/覆盖策略/号码限制）、Notification 设置
2. **默认两档**：Basic（正常优先级可发）与 No Faxing Rights（禁发）；一个 Profile 可服务多个用户
3. **出方向闭锁**：Restriction group（barring table）挂一个/多个 Profile，如"仅国内：禁国际号"——与 OXE 语音侧闭锁是两套体系
4. **入方向拒收**：站点级 Calling Number Restriction（Sites ➤ General Settings ➤ Calling Number restrictions），来话在呼叫建立阶段直接拒接
5. **邮件通知 Profile**：每语言一份，经用户 Profile 关联才生效；Exchange 场景勾 "Exchange integration" + 正文 Text（只影响邮件通知不影响 Web 访问）
6. **电话簿两类**：Public（企业级，经 Profile 下发、仅管理员管、Webadmin 可建多本可分组、CSV 导入）；Personal（仅用户本人）；电话簿可经 LDAP 访问——主机级 Fax Archive 属性勾 Enable LDAP Access、站点级 General Settings 设认证、LDAP Attribute Mapping 匹配属性

封页与公共电话簿同规则：仅管理员管理、经 Profile 下发。

## A1 — 书中案例

**禁国际号码策略**（p120-121，讲义口径）：

1. 建 Restriction group（barring table），条目口径"National only：禁国际号码"
2. 路径 Sites ➤ Site ➤ Configuration ➤ Profile 打开目标 Profile
3. 把拦截表关联到该 Profile（可挂多个 Profile）
4. 套用用户外发国际号即被拦截

**LDAP 电话簿访问**（p138-139）：

1. System Configuration ➤ Fax Archive 属性勾 Enable LDAP Access（主机级开关）
2. Configuration ➤ General Settings 属性里设 LDAP 认证（站点级）
3. LDAP Attribute Mapping 匹配 OTFC 与 LDAP 服务器属性

## A2 — 未来触发

使用情境：给部门分等级传真策略；禁发国际号/高价号；某些来传真的号码直接拉黑；Exchange 用户通知格式乱码或带图异常；企业共享联系人库；多语言组织通知模板。

语言信号：Profile / Basic / No Faxing Rights / 限制组 / restriction group / barring / 仅国内 / national only / 呼号限制 / calling number / 计费码 / billing code。

语言信号（续）：优先级 / 重试 / resolution / 通知 / notification / Exchange integration / Text / 电话簿 / phone book / Public / Personal / LDAP。

与相邻能力区分：账号本身的开户删户归用户管理能力；外发号码在电话系统侧的变换归目录与路由能力（Modification Table）；封页编辑与导入动作归客户端与封页能力（经路由）。

## E — 可执行步骤

输入契约：站点与用户已就位、企业策略（谁能发/发哪里/通知格式）、企业联系人清单或 LDAP 目录信息。

1. 定 Profile 框架：默认两档起步，按部门/合规需求增补（一份可服务多用户）。完成标准：Profile 清单与覆盖人群表
2. 配 Fax Options 与 Billing Codes：优先级/重试/分辨率按成本与时效定，计费码按财务口径。完成标准：策略参数表入档
3. 出方向闭锁：建 Restriction group 并挂目标 Profile。完成标准：测试号（如国际号）被拦截
4. 入方向拒收：站点级 Calling Number restrictions 加黑名单。完成标准：黑名单来话呼叫建立即拒
5. 通知 Profile：按语言核对每语言一份的模板，Exchange 场景勾 Exchange integration + Text。完成标准：测试通知格式正确
6. 电话簿：Public 电话簿 Webadmin 建本/分组/CSV 导入，经 Profile 下发。完成标准：用户端可见企业电话簿
7. LDAP 电话簿（如需）：勾 Enable LDAP Access、站点认证、属性映射三处配置。完成标准：LDAP 侧联系人可检索

判停点：

- 客户要求"禁国际"却要留给特殊审批 → 停，书内拦截表无审批流概念，按黑白名单口径管理预期或另想流程
- 通知里看不到传真图像 → 先分清邮件通知与 Web 访问两条线（Exchange integration + Text 只管前者），不要改错地方
- LDAP 属性映射对不上 → 停，按客户目录实勘字段重配映射，不猜属性名
- 把 Restriction group 当语音侧闭锁 → 停，两套体系独立，涉及 OXE 侧闭锁转语音侧方案

输出契约：Profile 体系表（属性/挂接/覆盖人群）+ 限制组与黑名单清单 + 通知 Profile 配置记录 + 电话簿（含 LDAP 访问）就绪说明。

## B — 边界

- 出方向 Restriction group 与入方向 Calling Number Restriction 方向相反、层级不同（Profile 级 vs 站点级），混用是常见错误源
- 邮件通知格式的 "Exchange integration + Text" 只影响邮件通知，Web Client 显示无关——排障先分两条线
- 私人电话簿不在系统备份覆盖内（Users\<username>\AppData\Roaming\Fax\PhoneBook，p219）；敏感组织建议引导常用联系人进 Public 电话簿（整理建议，原文只给路径）
- 具体合规条款（GDPR/HIPAA 类）解读在书外；Profile 里的安全选项细节以现场版本界面为准
- 封面的编辑器操作（.cse 五步）在客户端与封页能力（经路由）；本卡只管"经 Profile 下发"这半边
