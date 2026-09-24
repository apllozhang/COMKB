# POLISH-NOTES — rainxte001en 中文化润色记录（2026-09-24）

范围：.cangjie/capabilities/cards/*.md（12 卡）+ .cangjie/capabilities/book/{overview,glossary}.md + 根 DIGEST.md（扫描覆盖到的文件）。
原则：只改表达，不动任何数字、版本、页码、IP、端口、菜单路径、命令、参数、文件名、R 段英文原文、专有名词、yaml。

## 一、总体判断

全书为人工精写的紧凑工程文体，未发现"被配置为 / 允许……到…… / 使用……来进行……"等机器翻译腔（已用模式扫描核验，零命中）。本次仅修两类问题：①"与相邻能力区分"等散文名里的映射式箭头串；②个别生硬措辞。35 条箭头链告警中改写 11 处，保留 24 处合法菜单路径/纯流程链（逐条见第三节）。

## 二、逐处修改记录（11 处箭头链改写 + 2 处措辞）

1. cards/rbx-attendant-supervision.md · A2「与相邻能力区分」
   - 原：`Attendant 订阅的购买与分配 → 公司与订阅能力；被监督成员的话机关联 → 分机关联（路由卡）；OXO 侧 ACD 呼叫中心 → 第一本书能力域（另一 bundle）。`
   - 改：`Attendant 订阅的购买与分配归公司与订阅能力；被监督成员的话机关联见分机关联（路由卡）；OXO 侧 ACD 呼叫中心属第一本书能力域（另一 bundle）。`
   - 理由：箭头当"归属/指向某卡"的映射符号用，属散文塞逻辑，改动词表述。
2. cards/rbx-attendant-supervision.md · I「互助监督组」
   - 原：`与普通组同法创建` → 改：`创建方法与普通组相同`
   - 理由："同法"生硬文言腔。
3. cards/rbx-company-subscription.md · A2「与相邻能力区分」
   - 原：`建户之后的人员管理 → 成员生命周期；公司级目录与频道 → 管理员工具（路由卡）；PBX 接入 → PBX 接入能力。`
   - 改：`建户之后的人员管理归成员生命周期；公司级目录与频道见管理员工具（路由卡）；PBX 接入属 PBX 接入能力。`
   - 理由：同第 1 条，映射式箭头串。
4. cards/rbx-member-lifecycle.md · I 开户路径 2
   - 原：`**邮件邀请**：Invitations 页签 → Invite（可批量地址）→ 用户收 noreply@openrainbow 邮件自助完成 → 管理员回补号码/订阅等设置`
   - 改：`**邮件邀请**：Invitations 页签点 Invite（可批量填地址），用户收到 noreply@openrainbow 邮件后自助完成开户，管理员再回补号码/订阅等设置`
   - 理由：一段里塞了菜单+三方动作的箭头串，改自然叙述。
5. cards/rbx-member-lifecycle.md · A2「与相邻能力区分」
   - 原：`给成员配电话（设备/分机）→ 分机关联（路由卡）；订阅开通在公司侧 → 公司与订阅能力；成员在 Teams 场景的收敛配置 → Teams 集成能力。`
   - 改：`给成员配电话（设备/分机）见分机关联（路由卡）；订阅开通在公司侧归公司与订阅能力；成员在 Teams 场景的收敛配置属 Teams 集成能力。`
   - 理由：同第 1 条。
6. cards/rbx-member-lifecycle.md · E 步骤 2「邀请」子项
   - 原：`邀请：Invitations → Invite → 用户自助 → 管理员回补 Telephony/Services。`
   - 改：`邀请：Invitations → Invite，用户自助完成开户，管理员回补 Telephony/Services。`
   - 理由：保留菜单箭头（2 个），后半段多角色动作改行文。
7. cards/rbx-pbx-onboarding.md · E 步骤 4
   - 原：`异常排查：Webdiag → System → System Files → Log files → 取 ccrbagent.log 分析；仍显示默认密码态 → 回查账户密码是否已改（首连改密是前置）`
   - 改：`异常排查：在 Webdiag 的 System 页签下取 System Files / Log files 里的 ccrbagent.log 分析；若仍显示默认密码态，回查账户密码是否已改（首连改密是前置）`
   - 理由：菜单路径后混入条件分支箭头；菜单改斜杠分隔（本卡他处同款写法），分支改正文。
8. cards/rbx-rcc-association.md · A2「与相邻能力区分」
   - 原：`部署网关解锁音频 → 网关部署能力；Teams 场景的关联 → Teams 集成能力（同一路径的应用）；账户与订阅问题 → 成员生命周期。`
   - 改：`部署网关解锁音频见网关部署能力；Teams 场景的关联属 Teams 集成能力（同一路径的应用）；账户与订阅问题归成员生命周期。`
   - 理由：同第 1 条。
9. cards/rbx-teams-integration.md · I「四条呼叫路径」
   - 原：`内呼走 MakeCall API → CSTA 到 PBX（p202）；外呼走 MakeCall → WebRTC 网关 → PSTN（p203）；…`
   - 改：`内呼走 MakeCall API，经 CSTA 到 PBX（p202）；外呼走 MakeCall，经 WebRTC 网关出 PSTN（p203）；…`
   - 理由：信令流向用"经/到"更自然，页面引用原样保留。
10. cards/rbx-teams-integration.md · A2「与相邻能力区分」
    - 原：`分机关联的通用做法 → 分机关联（路由卡）；网关部署 → 网关部署能力；订阅开通 → 公司与订阅能力。`
    - 改：`分机关联的通用做法见分机关联（路由卡）；网关部署属网关部署能力；订阅开通归公司与订阅能力。`
    - 理由：同第 1 条。
11. cards/rbx-teams-integration.md · E 步骤 1「上架」
    - 原：`admin.teams.microsoft.com → Teams apps → Manage apps → 搜 Rainbow；有 → 状态置 Allowed；无 → Upload new app 传 zip（上传后默认 Allowed）。`
    - 改：`admin.teams.microsoft.com → Teams apps → Manage apps 搜 Rainbow；搜到就把状态置为 Allowed，搜不到就 Upload new app 传 zip（上传后默认 Allowed）。`
    - 理由：菜单后混入"有/无"分支箭头，分支改正文，保留 2 个菜单箭头。
12. cards/rbx-teams-integration.md · E 步骤 5「在场同步」
    - 原：`先做基线测试（改 Teams 状态 Rainbow 不动）→ App 设置图标 → 勾选与 Office 365 共享信息 → 选账户 → 复测同步生效。`
    - 改：`先做基线测试（改 Teams 状态，Rainbow 应不动）；再进 App 设置图标，勾选与 Office 365 共享信息并选账户，复测同步生效。`
    - 理由：测试→菜单→复测混一条箭头串，按语义分段。
13. cards/rbx-network-readiness.md · I 步骤 1
    - 原：`并挂两份 PDF` → 改：`并附两份 PDF`
    - 理由："挂"口语省字，"附"为工程文档规范用词。

## 三、保留的箭头链（24 处，均为合法菜单路径或纯流程链）

1. rbx-attendant-supervision:64 建组操作流：Communication → Supervision → Create → 填名称 → 选监督员 → 勾被监督成员——菜单后同一表单内的线性操作，无分支。
2. rbx-company-subscription:38 菜单/表单流：Members → 选成员 → Services 页签 → 勾 Enterprise → Apply。
3. rbx-company-subscription:39 合法菜单路径：Companies → Subscriptions → ATTENDANT → Attendant Monthly。
4. rbx-company-subscription:58 合法菜单/表单流：Companies → Subscriptions → 选类型与月付/预付 → 定数量 → Subscribe。
5. rbx-company-subscription:59 合法菜单/表单流：Members → 成员 → Services 页签 → 勾选 → Apply。
6. rbx-gateway-deployment:27 FTR 线性操作流：DHCP 接入 → 浏览器地址 → 设密码 → 选产品类型。
7. rbx-gateway-deployment:72 合法菜单/表单流：Communication → Manage connection → 勾 Activate → 选类型与通道数。
8. rbx-gateway-deployment:75 FE 施工线性顺序：建设备 → warm reset → 核 PBXID → OMC 核端口。
9. rbx-maintenance-support:48 合法菜单路径：MyPortal → Support → Service Request → Create SR → 填表单。
10. rbx-member-lifecycle:59 CSV 线性操作流：下模板 → 填列 → 导入 → 读报告修正。
11. rbx-omc-onboarding:19 首连菜单/表单流：Expert → LAN/WAN → IP → 勾认证 → 输密码。
12. rbx-omc-onboarding:63 安装线性流：解压 → setup.exe → 逐项选择 → Finish。
13. rbx-omc-onboarding:65 合法菜单流：View certificate → Install certificate → Trusted Root → Finish。
14. rbx-pbx-onboarding:18 合法菜单路径：web.openrainbow.com → 公司管理图标 → My company → Communication → 点 OXO → 复制凭证。
15. rbx-pbx-onboarding:20 表单线性流：填 PBX-ID → 填激活码 → 勾启用 → Apply。
16. rbx-pbx-onboarding:24 合法菜单路径：Webdiag → System 页签 → System Files → Log files → 取日志。
17. rbx-pbx-onboarding:25 合法菜单路径：Rainbow 界面 → User Settings → About Rainbow → Open logs。
18. rbx-pbx-onboarding:49 合法菜单路径（取凭证，同 14）。
19. rbx-pbx-onboarding:50 表单线性流：OMC/Cloud/Rainbow → 填双凭证 → 勾启用 → Apply。
20. rbx-rcc-association:16 合法菜单路径：Rainbow → My company → Members → 选成员 → Telephony 页签 → Equipment 选 OXO Connect → 选分机 → Apply。
21. rbx-teams-integration:29 合法菜单路径：Teams 管理中心 → Teams apps → Manage apps → 搜 Rainbow。
22. rbx-teams-integration:42 合法菜单路径：Apps → Built for your org → Add → Sign in。
23. rbx-teams-integration:60 合法菜单路径：Rainbow app → Permissions → Review permissions and consent → Accept。
24. DIGEST:10 交付主线纯流程链：云侧开户 → PBX 接入 → 分机关联 → 网关解锁音频 → 增值场景——教材主线线性管道，与原书章节顺序一致。

## 四、未改动文件说明

- cards/rbx-admin-tools.md、rbx-gateway-planning.md、rbx-network-readiness.md（除第 13 条措辞外）、.cangjie/capabilities/book/overview.md、glossary.md：通读后表达自然、无箭头链告警、无超长行，未做改动。
- overview.md 第 7 行"创建公司 → 开订阅 → …"六步主线未被扫描器告警（其本身也是合法交付流程链），按最小改动原则保留原状。

## 五、验收

- scan_dense.py：改写后剩余 24 条告警，全部为上表合法保留项，逐条注明理由。
- scan_blank.py：零输出。
