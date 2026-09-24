# Microsoft Teams 集成全流程（双件套、上架与权限同意、用户配置、在场同步）

## R — 原文依据

> "The integration is done at the workstation level"（p259）
> "THE RAINBOW APPLICATION INTEGRATED INTO TEAMS REQUIRES THE INSTALLATION AND STARTUP OF THE RAINBOW DESKTOP APPLICATION ON THE PC."（p302）
> "it is better to apply a restrictive permission to users with Teams integration in order to forbid collaboration services from Rainbow … Select the required permission: Here 'Telephony'"（p297）
> "Rainbow presence status is now synchronized with Teams one"（p307）

出处：RAINXTE003EN p258-307。

## I — 自述

集成在工作站级（逐台 PC），不是租户一键生效（p259）。双件套分工：

1. **Rainbow App in Teams**（Telephony Power App）：电话设置/呼叫历史/留言与通知/拨号盘/呼转控制/当前话机选择
2. **Rainbow Desktop**：任意桌面应用热键点击外呼（如 F6）+ 单呼叫控制（拨打/接听/挂断/取消）；必须安装且常驻运行

四条呼叫流（p264-266）：

| 场景 | 路径 |
|---|---|
| Teams 拨分机 | MakeCall API（CSTA）→ PBX 话机响 |
| Teams 拨外部号 | MakeCall API 发起，音频经计算机 VoIP 与 WebRTC 网关出公网 |
| 外部来话（话机模式） | 话机响 + Desktop 通知（接听/转留言） |
| 外部来话（计算机模式） | WebRTC 经网关 → 计算机接听 |

部署三步：①Teams 管理中心上架应用并做权限同意；②Rainbow 侧配置（分机关联 + 权限收敛 Telephony + Business/Enterprise 订阅）；③最终用户装 App 与 Desktop 并登录。

关键行为口径：权限收敛为 Telephony-only（协作服务交 Teams 原生，p297）；订阅必须 Business 或 Enterprise（p298）；在场同步要单独激活（与 Office 365 共享信息），激活前两侧不一致属预期（p305-307）；SSO 非连接器必需（p304）。

## A1 — 书中案例

**租户侧上架与同意**（p285-293）：

1. 浏览器打开 Teams 管理中心，管理员登录
2. Teams apps、Manage apps 搜 Rainbow；用户可装的前提是状态 Allowed
3. 搜不到则 Upload new app 传 zip 包，状态变 published
4. 推荐同意法：应用 Permissions 页签点 Review permissions and consent 后 Accept（用户端不再弹窗）
5. 备选法：首次在 Teams 内登录时勾"代表整个组织"同意
6. Azure 核验：Permissions 页签跳转 Azure AD 确认权限已由管理员授予

**用户配置与终端**（p294-307）：

1. Rainbow 端 Telephony 页签给成员绑定 OXE 设备与分机
2. Permissions 页签只授 Telephony 权限并 Apply
3. Services 页签分配 Business 或 Enterprise 订阅
4. Teams 内 Apps 装 Rainbow（组织已添加的从 Built for your org 找）
5. Desktop 未运行时应用显示感叹号图标，启动 Rainbow Desktop 后图标恢复
6. 同步前基线测试：改 Teams 在场，确认 Rainbow 侧不同（属预期）
7. 设置里勾选与 Office 365 共享信息，提示同步已激活
8. 复测：再改 Teams 在场，Rainbow 侧随之同步

## A2 — 未来触发

使用情境：Teams 里打公司座机和外线；装 Rainbow App；状态不同步；权限同意弹窗；Teams 内应用显示感叹号。

语言信号：Teams / Rainbow App / Rainbow Desktop / 权限同意 / consent / Allowed / Upload / Telephony 权限 / MakeCall / click-to-call / F6 / 在场同步 / presence / Office 365 / 感叹号 / workstation。

与相邻能力区分：

- 网关侧音频通路 → 网关部署能力
- 分机关联本体 → 分机关联能力（路由卡）
- 订阅与权限分配的公司面 → 公司体系与订阅能力

## E — 可执行步骤

输入契约：Teams 管理员账户与 Azure AD 权限、用户清单（订阅/分机）、各 PC 装机权限。Teams 租户策略不受控 → 判停，声明边界后与客户 IT 协同。

1. 上架应用：管理中心搜 Rainbow 或上传 zip，状态置 Allowed。完成标准：用户可安装
2. 权限同意：推荐管理员预同意（最简且免全员弹窗）。完成标准：Azure 页显示权限已授予
3. 用户配置：Telephony 关联、Telephony-only 权限、Business/Enterprise 订阅。完成标准：三项齐备
4. 终端装配：Teams 装 App + PC 装 Rainbow Desktop 并保持运行。完成标准：应用图标正常（无感叹号）
5. 在场同步：先测基线（不同步属预期），再激活 O365 信息共享，复测一致。完成标准：前后对照成立

判停点：

- Teams 内应用一直显示感叹号 → 第一步查 Rainbow Desktop 是否安装并运行（硬依赖）
- 拨分机不通但拨外线通 → 分两条呼叫流排障（CSTA 侧与网关侧），不混修
- 用户在 Rainbow 里还能聊天 → 预期，权限未收敛；按 Telephony-only 收敛（p297）
- 客户问租户级应用策略/紧急呼叫 → 超出原书范围，声明边界并指向 Teams 官方文档

输出契约：租户侧上架与同意记录 + 用户配置清单 + 终端装配与在场同步验证结论。

## B — 边界

- Teams 租户侧策略（应用权限策略、紧急呼叫、Direct Routing 共存）在书外（n25 边界）
- SSO 可用于 Desktop 登录但非连接器必需（p304 Important）
- Teams 章两段内容重复（p259-269 与 p274-284，nr-05），以 p258-273 为引用主口径
- 配置细则以 Rainbow help center 文章为准（p273 指针），书内为 Ed12 界面口径
- 实验 Azure AD/O365 环境为培训租户（实验口径），生产用自己的租户
