# 成员管理与话务配置（开户五通道、七分区、例行程序、宽限与安全）

## R — 原文依据

> "Members can be created: Manually • By invitation • By bulk import • From .CSV file (UTF-8) • Microsoft Azure Active Directory • LDAP"（p167）
> "Warning A MEMBER MUST HAVE A VOICE SUBSCRIPTION ... TO ASSIGN A PHONE NUMBER."（p194）
> "If you restore it, it will default to 'Essential' (free) mode, so you'll need to reallocate the appropriate license"（p176）
> "If the user is logged in at the time you make the password change, he/she will be logged out immediately."（p177）

出处：RAINXTE101EN p165-206。

## I — 自述

成员是云侧日常运营主体，五条开户通道与一组生命周期规则：

1. **开户五通道**：手动逐个（当场定全字段）、邮件邀请（用户自建后管理员补配）、CSV 批量、Azure AD、LDAP 连接器

   - CSV：UTF-8 模板，建/改/删、按 MAC 绑设备，SSO 时密码列留空
   - Azure AD：需先把 AAD 关联公司、限 Voice Enterprise 管理员，关联本身不触发自动供应
   - LDAP：免费装客户 Windows server，三功能自选（用户单向同步仅付费许可、AD 联系人进企业目录、Exchange 日历在场）
2. **成员编辑页七分区**：Information（含时区=留言时间戳依据、可见性、标签、Sites）、Permissions、Phone（设备=Cloud PBX、内线/公网号、可选物理设备）、Programmable keys、Services（Voice 四档）、Roles、Security
3. **横向项**：Tags（手工/批量打标优化搜索）、User Profiles（公司级功能限制档案；验证新档案时系统会问是否设为公司默认——看清弹窗）、个人例行程序（At Work/DND/On Break/Out of office 四预置；一键同时改在场/主叫 ID/呼叫设备/呼转/退组五类参数）
4. **电话服务门槛**：成员必须持 Voice 订阅才能配号码；无物理话机也可以是纯软话机用户；分到号码即自动配留言信箱，容量 30 分钟
5. **删除与安全**：删除进 10 天宽限（Suspended）——恢复后订阅已回收、回落 Essential 免费档，须重新分订阅并重挂电话线；宽限期内邮箱不可复用；管理员改密会立即踢掉该用户在线会话（防盗号特性）

## A1 — 书中案例

**邀请与直建成员并配电话**（p190-196，How-To）：

1. Members 区 / Invitation 页签 / Invite → 输入 bobP 邮箱 → Continue。
2. 用户登录培训邮箱点链接建户（邮件可能进 SPAM；密码 Superuser-P*，实验口径）。
3. 管理员在成员列表补配 Bob 的订阅 Voice Enterprise。
4. Members 页签 → Create 直建 Carol：登录/密码/订阅/时区/勾 Send enrollment email。
5. Phone 页签给成员配号：Equipment=Cloud PBX、内线 101/102/103、公网号从号池选。

**批量导入与横向配置**（p197-206，How-To）：

1. Members / Import / 下载 CSV 模板 → 复制示例行改 Dave 的登录/内线 104/DID/订阅。
2. 上传前看错误弹窗 → 勾 Send enrollment email → 看导入报告（绿/红行）。
3. Tags 页签建 HR、Building A 指派成员 → 按标签过滤搜索验证。
4. Profiles 页签建受限档案 → 系统询问是否设为公司默认 → 指派给 Carol。
5. Prog keys 给 Alice 配应用速拨键（Key=103）与话机 supervision 键。
6. 以 Alice 登录把 DND 例行程序改为来话转 Bob，拨测验证生效。

## A2 — 未来触发

使用情境：批量开户选通道；给成员配内线/公网号；设一键下班转手机；限制某类用户的协作功能；误删恢复；怀疑盗号踢下线；邀请邮件收不到。

语言信号：成员 / members / 邀请 / invitation / CSV / 批量导入 / Azure AD / LDAP / 订阅分配 / 内线 / 公网号 / 例行程序 / routines / DND / 标签 / tags / 档案 / profiles / 宽限期 / grace period / Essential / 改密。

与相邻能力区分：公司创建与订阅池归公司订阅能力；组与话务分配归呼叫组能力；按键组批量下发细节在本卡（f17），设备侧 zero-touch 归设备部署能力。

## E — 可执行步骤

输入契约：成员名单与身份信息、订阅池余量、号码资源（内线段/空闲 DDI）、目录设施现状（AAD/LDAP/Exchange）、设备 MAC（如有）。

1. 选通道：单人急用走直建；用户自配走邀请；批量走 CSV；目录驱动走 AAD/LDAP。完成标准：通道与前提匹配（AAD 需 Voice Enterprise 管理员）
2. 开户：按所选通道执行（CSV 记得 UTF-8、SSO 场景密码列留空、导入后看报告）。完成标准：成员出现在列表且订阅已挂
3. 配电话：Phone 页签 / Equipment=Cloud PBX / 内线 + 公网号 → 按需绑物理设备。完成标准：号码分配成功（前提是成员已有 Voice 订阅）
4. 配体验项：例行程序/标签/档案/按键组按需下发（档案弹窗看清再确认）。完成标准：功能拨测或按 tag 搜索验证通过
5. 生命周期管理：删除前确认 10 天宽限三重副作用；改密等敏感操作避开工作时间并提前告知。完成标准：工单时序含宽限与恢复成本

判停点：

- 配号字段点不动 → 停，查成员订阅（无 Voice 订阅不能配号，p194）；纯软话机用户同样要订阅
- "发了邀请却搜不到人" → 不是故障：用户接受邀请后才出现在列表，急用改直建或批量（n31）
- 邮箱建户报错被占用 → 查是否 10 天宽限期内被删账号（n29）；恢复账号要重配订阅与电话线
- "没收到邮件" → 先查 SPAM（n32）；生产建议把 openrainbow.com 发件域加白

输出契约：可用成员账户（订阅/号码/体验项就位）+ 批量导入报告 + 生命周期操作记录。

## B — 边界

- AAD/LDAP 依赖客户已有目录设施；AAD 关联不自动供应，建/改/删仍是管理员经 CSV 主动做（p170）；LDAP 的 Exchange 在场同步是 161 版前功能的等价回归（n55）
- 密码复杂度四处一致口径：≥12 字符 + 1 大写 + 1 数字 + 1 特殊字符（p54/p168/p169/p177；原文未单列小写要求）
- 实验成员密码 Superuser-P* 与培训邮箱 PasswordP* 均为实验口径（needs-review nr-06）
- JSON 来电卡片（屏幕弹卡定制）书中为成员话务特性一处提及（p198 区域），无独立 How-To——引用时按"特性存在、细节以支持站点为准"表述
- 管理员改密踢线的对象是该成员全部在线会话（p177）；批量改密要先公告，避免被当掉线故障上报
