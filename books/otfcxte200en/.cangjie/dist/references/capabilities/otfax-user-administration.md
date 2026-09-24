# OTFC 用户与管理员管理（双用户源、CSV 批量、两级管理员、认证方式）

## R — 原文依据

> "In OpenTouch Fax Center, a user is always identified by an SMTP Address."（p23）
> "Internal Users: … Active Directory integration: … Note: The two type of user's directory can co-exist"（p100）
> "Users can be imported by the Webadmin interface only • .csv file format … The list of users could be exported by the Webadmin interface only"（p104-105）
> "There are two types of administrators: SYSTEM Administrators ; SITE Administrators … It is recommended to create a backup administrator"（p107, p110）

出处：OTFCXTE200EN p97-116（含 How-To 实验 4 的建户与建管理员步骤）。

## I — 自述

用户是运营主体，三条主线：

1. **身份与绑定**：用户恒以 SMTP 地址（邮箱）为身份；必须同时属于一个 Site、有一个 faxing Profile 才能用系统；时区写入传真报头并影响封页/报头/邮件通知三处时间戳
2. **双源可共存**：内部用户（OTFC 内建，手工建或静态导入，可导出 CSV）与 AD 集成（经域管理，Windows 账号登录用 NT Account 属性反查 SMTP 地址）不是二选一，按群体混用；CSV 批量导入/导出仅 Webadmin 界面有，MMC 没有
3. **两级管理员**：System administrator 管整个系统（可多名，认证基于内部服务器/AD/SAML）；Site administrator 只管自己的站点；官方推荐建备份管理员防锁死；登录认证可用 SMTP 地址或 Windows 认证（SSO 与 SAML）

建户要素：邮箱地址、Profile、密码（首登必改）、个人信息、电话号码、传真号；时区可在 Profile 级管理。

## A1 — 书中案例

**建备份管理员与两个测试用户**（p114-116，实验 4，实验口径）：

1. 启动 OpenTouch Fax Center 应用，用 Administrator 登录 MMC，按提示改密为 Alcatel1!@123
2. 浏览器打开 http://fax/faxadmin 发现 Web 管理界面
3. System Configurations ➤ Administrators 选 add，建 backupadmin（认证选传真服务器，密码 Alcatel1!@123）后 Create
4. 用新账号登录 MMC 验证，按提示改密并记录
5. 在 Sites ➤ Site ➤ Configuration ➤ Internal Users 建 allen@company.com（传真号 31604）与 barkley@company.com（传真号 31600）
6. 两用户登录 Web Client（http://localhost/fax）互发传真，检查 inbound/outbound/queue 三菜单
7. 从管理界面监控传真交换

## A2 — 未来触发

使用情境：批量开传真账号；删错用户怎么补；管理员密码丢了；客户问 AD 账号能不能直接用；MMC 里找不到导入用户按钮；跨时区用户通知时间不对。

语言信号：用户 / user / Internal Users / Active Directory / NT Account / CSV / 批量导入 / 导出 / SMTP 地址 / Profile 分配 / 管理员 / administrator / backupadmin / SSO / SAML / 时区 / time zone / 传真号。

与相邻能力区分：Profile 里的策略（限制组/通知格式/封页）归 Profile 策略能力；外部用户自动归类（Lookup 表）归目录与路由能力；登录问题里目录侧的排查归目录与路由能力的 NT Account 段。

## E — 可执行步骤

输入契约：站点已建（Site 就绪）、Profile 体系已规划（见 Profile 策略能力）、用户清单（邮箱/传真号/时区）、AD 域环境（如走 AD 源）。

1. 定用户源：主体用户走 AD、少量外部/临时走内部库（两源可共存）。完成标准：各群体归属明确
2. 内部建户：Web 管理界面 Sites ➤ Site ➤ Configuration ➤ Internal Users ➤ Create，填邮箱/Profile/密码/个人信息/传真号/时区。完成标准：用户出现在列表且绑定 Site+Profile
3. 批量导入：Webadmin 的 Import users，.csv 格式，第 3 步选套用 Profile。完成标准：导入报告无报错、用户可登录
4. AD 源准备：确认域内 NT Account 属性可反查 SMTP 地址（Lookup 链见目录与路由能力）。完成标准：AD 用户可经 Windows 账号登录
5. 建管理员：System 级按 p110 三步（认证可选内部服务器/AD/SAML）；Site 级按 p111 四步。完成标准：两类账号各就位
6. 建备份管理员：与主管理员不同认证路径，密码入交付文档。完成标准：backupadmin 可独立登录
7. 行为验证：建两个测试用户互发传真，核对 inbound/outbound/queue 与管理端监控。完成标准：双向传真与监控记录齐全

判停点：

- MMC 里翻不到 Import/Export users → 停，这是功能边界（仅 Webadmin），切 Web 管理界面操作
- 用户建了但登录被拒 → 先核对是否绑定了 Site 与 Profile（缺一即拒用），再查密码首登强制改密
- 客户只有一名 System 管理员且用 SSO 登录 → 停，锁死风险高，先落备份管理员再上线
- 时区没按用户所在地设置 → 交付前逐用户核对，否则封页/报头/通知三处时间戳全错

输出契约：用户清单（源/站点/Profile/传真号/时区）+ 管理员账号表（级别/认证方式）+ 备份管理员交接记录 + 测试互发验证结果。

## B — 边界

- 评估许可下用户数上限 100（p52）：批量开号前先核许可余量
- CSV 导入导出仅 Webadmin；MMC 无此功能——功能分布差异以原书口径为准
- 教材账号密码（Alcatel1!@123、123456）是实验口径，生产必须替换并纳入交付检查表
- NT Account Lookup 的两条实现路径与 IIS 免密登录配置在目录与路由能力展开；本卡只覆盖账号管理面
- Site 管理员的建号步骤（p111）书内为讲义级四步，无独立实验章
