# Microsoft Teams 集成全流程（架构、上架、用户配置、在场同步）

## R — 原文依据

> "The integration is done at the workstation level"（p196）
> "As the user will use Teams for all collaboration services, Rainbow will only provide telephony integration services. So, it is better to apply a restrictive permission to users with Teams integration ... Assign the 'telephony' permission"（p234）
> "THE RAINBOW APPLICATION INTEGRATED INTO TEAMS REQUIRES THE INSTALLATION AND STARTUP OF THE RAINBOW DESKTOP APPLICATION ON THE PC."（p239）
> "we activate the sharing of information with Office 365 ... Synchronization is now active."（p243）

出处：RAINXTE001EN p195-244。

## I — 自述

**架构**：工作台级集成（按台落地，非租户一键生效），两个组件分工：
- **Rainbow App in Teams**（Telephony Power App）：电话设置/呼转/热键、通话历史（含未接）、语音信箱与提醒、拨号盘
- **Rainbow Desktop**：任意应用热键点击外呼（如 F6）、单路呼叫控制（接/挂/取消）、通话中 Mute/DTMF/挂断

**四条呼叫路径**：内呼走 MakeCall API → CSTA 到 PBX（p202）；外呼走 MakeCall → WebRTC 网关 → PSTN（p203）；外线来话（无网关路径）呈现于话机 + 桌面通知（p205）；来话经网关建 WebRTC 呼叫到电脑（p206）。

**部署四要素**：应用上架（商店或 zip 上传，状态须 Allowed）· 权限同意（管理中心直接批准为最简，或管理员首登时代表组织同意）· 订阅（Business/Enterprise）· 权限收敛（Rainbow 只留 Telephony，协作归 Teams）。

**硬前提**：每台 PC 安装且运行 Rainbow Desktop；SSO 非必需。

## A1 — 书中案例

**上架与同意实验**（p222-230）：Teams 管理中心 → Teams apps → Manage apps → 搜 Rainbow（搜不到则 Upload new app 传 zip）→ 状态置 Allowed → Permissions 页签 Review permissions and consent → Accept → Go to Azure Active Directory 核验权限已由管理员授予。

**用户配置实验**（p231-235）：Members → Telephony 页签关联 PBX 与分机（出现 Rainbow number）→ Permissions 页签只授 Telephony → Services 页签分配 Business/Enterprise。

**连接器与在场同步实验**（p236-244）：Teams 内 Apps → Built for your org → Add → Sign in → Desktop 未运行时从 "!" 图标拉起 → 先测"改 Teams 状态 Rainbow 不动"（基线）→ 激活 O365 信息共享 → 复测状态同步。

## A2 — 未来触发

使用情境：客户要 Teams 里打电话；Teams 应用上架；权限同意弹给用户了；Teams 用户要什么订阅；装完状态不同步；Rainbow 与 Teams 功能重复怎么收敛；Teams 打 PBX 分机走哪条路。

语言信号：Teams 集成 / Rainbow for Teams / Teams admin center / consent / 权限同意 / Telephony 权限 / Rainbow Desktop / 点击外拨 / click-to-call / F6 / 在场同步 / presence / O365 / workstation level。

与相邻能力区分：分机关联的通用做法 → 分机关联（路由卡）；网关部署 → 网关部署能力；订阅开通 → 公司与订阅能力。

## E — 可执行步骤

输入契约：Teams 租户管理员权限、用户清单与订阅、各 PC 的 Desktop 安装可达性、（外呼场景）WebRTC 网关已部署。无 Teams 管理员 → 判停转客户租户管理员。

1. 上架：admin.teams.microsoft.com → Teams apps → Manage apps → 搜 Rainbow；有 → 状态置 Allowed；无 → Upload new app 传 zip（上传后默认 Allowed）。完成标准：用户可安装
2. 权限同意：管理中心 Rainbow app → Permissions → Review permissions and consent → Accept（推荐）；或管理员首登 App 时勾"代表整个组织"。完成标准：Azure 侧权限已授予（Go to Azure AD 核验）
3. 用户配置（每用户）：Telephony 关联 PBX 与分机 → Permissions 只授 Telephony → Services 分配 Business/Enterprise。完成标准：三步齐备
4. 终端交付（每台 PC）：装 Rainbow Desktop 并保持运行 → Teams 内 Apps 添加 Rainbow → Sign in（"!" 图标消失即连接成功）。完成标准：App 激活
5. 在场同步（按需）：先做基线测试（改 Teams 状态 Rainbow 不动）→ App 设置图标 → 勾选与 Office 365 共享信息 → 选账户 → 复测同步生效。完成标准：前后对照通过

判停点：
- 权限同意落到普通用户头上 → 管理员未预同意；让该用户先不操作，管理员补方法 A，避免组织级授权悬空
- Teams 里 App 显示 "!" → Desktop 未运行：从图标拉起或先装 Desktop，不要反复重装 Teams App
- 用户看不到拨号盘/历史 → 依次查订阅（Business/Enterprise）、Telephony 权限、Desktop 运行态
- 打不了外线但内线通 → 外呼路径依赖 WebRTC 网关，转网关部署能力核验
- "装完即同步"写进验收 → 不成立：同步默认关、须手动激活 O365 共享（n53），改验收标准

输出契约：租户侧就绪（上架+同意）+ 用户配置清单 + 终端交付台账（PC ↔ Desktop/App 状态）+ 在场同步验证记录。

## B — 边界

- 工作台级集成：终端装机量是真实交付工作量，报价时计入（n48）
- Teams 租户侧策略（应用权限策略、紧急呼叫、Direct Routing 共存）原书不覆盖
- 协作功能（聊天/会议/文件）归 Teams 原生：Rainbow 侧收敛为 Telephony 是官方建议口径（p234），混开双轨的状态与记录分裂风险要向客户明示
- SSO 与连接器无依赖（p241 Important）：不要把"先上 SSO"排进集成前置
- 拨号盘/呼叫历史的详细功能矩阵以 help.openrainbow.com 的 Teams 集成文章为准（p199/p210 指针）
