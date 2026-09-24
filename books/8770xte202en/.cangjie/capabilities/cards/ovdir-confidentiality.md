# 目录保密级别与访问级别（四级保密、两应用十档、Web 目录两级访问）

## R — 原文依据

> "4 levels of confidentiality available • Entries with the confidentiality level 'Green' (default value) • ... 'Orange' • ... 'Red' • Administration 8770 is the most confidential level"（p209）
> "Personal data • Home Telephone • Home Address • Car License • Employee Number • Password"（p210）
> "Anonymous access • Only green records displayed • With only non-personal data"（p211）
> "Authenticated access with a company directory person • Only green records displayed • With personal data included for the authenticated person"（p212）
> "When you consult the web directory with a person account, only the persons with confidentiality level green are displayed and the authenticated person."（p243）

出处：8770XTE202EN p209-215, p217-251。

## I — 自述

保密是"条目级"，管理端权限是"账户级"，两套机制正交——出问题时先分清是哪套挡住了。

- **条目保密四级**：Green（默认）/ Orange / Red / Administration 8770（最高）；挂在人员条目上
- **属性两类**：个人数据五种（家庭电话/家庭住址/驾照/工号/密码），其余为非个人数据；Password 指人员 UID 密码
- **Web 目录两级访问**：匿名=只读且只见 Green 条目的非个人数据；UID+密码认证=可改本人记录、管个人地址簿，本人 personal data 可见。注意：本人级别是 Orange/Red 并不扩大对他人条目的可见性
- **管理端访问级别**（Security 应用按应用分别授予）：

| 应用 | 五档（低到高） |
|---|---|
| Company Directory | No Access / Partial Read / Total Read / Partial Modification / All |
| Web Directory | Partial View Orange List / Partial View Red List / Total View Red List / Partial Modification / All |

- **授予入口**：Security 应用 nmc > 8770Applications > Company Directory 或 WebDirectory，加账户选级别；AdminNmc 默认 All
- **行为矩阵速记**（实测口径，c06 七类会话验证）：匿名 2 绿非个人；Green 人员 2 绿+本人；Orange/Red/Admin8770 人员同前；web 管理员按档扩面；AdminNmc 八人全见全改

## A1 — 书中案例

**保密级别矩阵验证实验**（p217-251）：

1. Directory 应用 Ale 根下建 RH 部门
2. RH 下建八人：green/green2/orange/orange2/red/red2/admin8770/admin8770_2
3. 每人设 Password、Confidentiality 级别与家庭电话/住址（实验口径）
4. Security 应用建五个管理员账户（partial_read/total_read/partial_orange_web/partial_red_web/total_red_web）
5. Company Directory 应用下授 partial_read 与 total_read 两档
6. WebDirectory 应用下授三档查看级别
7. 匿名会话搜 RH：仅 green/green2，且只有非个人数据
8. Green 人员登录：green/green2+本人，本人 personal data 可见
9. Orange/Red/Admin8770 人员分别登录：结果与 Green 相同（只多看本人）
10. partial_orange_web 登录：四条目非个人属性
11. partial_red_web/total_red_web 登录：六条目，后者含个人属性
12. AdminNmc 登录：八人全见全属性，可建删改

## A2 — 未来触发

使用情境：HR/领导层号码要对普通员工隐藏；员工能不能看到同事家庭电话；匿名访问能看到什么；给前台开目录账号该给哪档；Orange 的人为什么查不到别人；员工想自己改手机号。

语言信号：保密 / confidentiality / Green / Orange / Red / Administration 8770 / personal data / 个人数据 / 匿名 / anonymous / 访问级别 / access level / Security / 地址簿。

与相邻能力区分：

- 按部门切割管理员可见范围 → 管理域与委派能力
- Web 客户端界面/字段定制 → 客户端与词典定制能力
- 人员属性批量维护 → LDIF 工具能力

## E — 可执行步骤

输入契约：保密对象名单与级别映射、需要的管理员账户清单、Web 目录匿名是否开放的业务决定。

1. 定级：按名单给人员条目设 Confidentiality（默认 Green 不动）。完成标准：级别台账成文
2. 建账户：Security 应用建管理员并按应用授 Company Directory/Web Directory 级别。完成标准：账户-级别对照表就绪
3. 员工侧：给需自助维护的人员设 UID 密码并告知认证入口。完成标准：认证可用
4. 匿名验证：无会话搜保密部门，应只见 Green 非个人数据。完成标准：泄漏面为零
5. 人员验证：抽 Orange 人员登录核对"2 绿+本人"边界。完成标准：本人可见性正确
6. 管理员验证：逐档登录核对可见条目数与属性范围。完成标准：与矩阵一致

判停点：

- 客户以为"给 Orange 的人授了权就能看 Orange 同事" → 正交机制讲清：条目保密与账户权限是两套，本人级别不放大他人可见性
- 需要按部门切管理员可见范围 → 那是管理域能力（Domain Management），不是保密级别能做的
- 匿名入口被要求彻底关闭 → 检查 GlobalParameters 认证图标与入口策略（客户端定制能力域）
- 误把 UID 密码当登录账号密码 → Password 属性只用于 Web 目录认证（g13），与 8770 管理员账户无关

输出契约：保密级别台账 + 管理员账户授权表 + 七类会话抽验记录。

## B — 边界

- admin8770 级别条目只有持相应权限的管理员账户经 Web Directory 才可见（p211/p243 口径）
- 保密级别不加密数据：LDAP 层与 LDIF 导出仍可触达，安全方案要另算
- Password 属性（人员 UID 密码）属于个人数据、认证本人可见（p212/p243），保密设计时不得遗漏
- 个人地址簿（500 条上限，默认值）属用户私有数据，与保密级别无关（p328）
- c06 实验口令与人数为实验口径，生产按客户名单执行
