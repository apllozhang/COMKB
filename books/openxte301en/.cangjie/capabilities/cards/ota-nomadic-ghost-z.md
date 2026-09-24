# Nomadic 移动模式与 Ghost Z 资源池（蜂窝/VoIP、tsa_maintenance）

## R — 原文依据

> "The system requires ONE Ghost Z set for each Nomadic connection ... Ghost Z sets are retained as busy throughout the connection and are only released when nomadic mode is disabled."（p47）
> "For each Nomadic SIP connection, the system requires: 1 SIP device ... 1 Ghost Z set"（p51）
> "When nomadic mode is activated, the user phone set in the office is frozen and disabled."（p34）
> "Warning The management done for nomadic in cellular mode shown in the previous step is a pre-requisite."（p51）

出处：OPENXTE301EN p31-57。

## I — 自述

Nomadic 是 Connection 用户专属的移动机制：激活后办公话机冻结，来话改道。核心是资源池换轨：

1. **双模式**：蜂窝（cellular）——来话经虚拟 Ghost Z 改道到任意号码（家庭/手机）；VoIP——经 Ghost Z+SIP 设备改道到 PC 软话音
2. **容量公式**：池规模=最大并发连接数；每路蜂窝占 1 个 Ghost Z，每路 VoIP 占 1 个 Ghost Z + 1 个 SIP 设备；占线持续到用户关闭 nomadic（挂机不释放）
3. **权限成对**：蜂窝=Nomadic GSM+Desktop；VoIP=Nomadic SIP+Desktop；从 OTC PC 激活必须先有 Desktop 许可
4. **两侧登记**：Ghost Z 在 OXE 建（Set Type Analog+Ghost Z feature=Nomadic），OT 侧按范围登记（OXE Resources 的 Z ghosts min/max）；SIP 设备两侧各声明（OXE SIP Subscriber）
5. **编解码口径**：窄带用 G.711u/a、G.729a、G.723，加宽带用 G.722.2；VLAN 打标不支持、QoS 按 IP TOS；SIP 生存性不支持

激活入口在 OTC PC 的 routing 窗口切换"当前电话"（Home/Mobile/Personal computer）。

## A1 — 书中案例

**Nomadic 蜂窝到 VoIP 到维护的完整实验**（p45-57）：

1. OXE 建 3 个 Ghost Z：31017/31018/31019（Set Type Analog，feature=Nomadic，实验口径）
2. OT 侧登记范围：OXE Resources 的 Z ghosts min/max=31017/31019
3. 授权 Barkley：Licenses 页签启用 Nomadic GSM 与 Desktop
4. OTC PC 填 Home/Mobile 号码，routing 窗口切到 Home phone 测试（办公话机冻结）
5. OXE 建 2 个 SIP 设备：31951/31952 并核对 SIP 页签默认值
6. OT 侧声明 OXE SIP Subscriber（登录/密码/SBC WAN），授权 Nomadic SIP+Desktop
7. routing 窗口切到 Personal Computer，来话在 PC 接听
8. 维护：OT 服务器跑 tsa_maintenance，选项 20 dump Nomadic 核对三个 Ghost Z 在库
9. 缺失则手动同步：选 100（秘密码 2998）→ 输 106 2998 → 选 7 Load All Acapi Object

## A2 — 未来触发

使用情境：员工居家/出差要接办公电话；用户说 OTC PC 上没有 nomadic 菜单；"人连不上 nomadic"容量问题；Ghost Z 资源一致性核查；nomadic 目的号码能不能填同事。

语言信号：nomadic / 蜂窝 / cellular / VoIP 模式 / Ghost Z / 资源池 / 冻结 / frozen / Nomadic GSM / Nomadic SIP / tsa_maintenance / dump / routing 窗口。

与相邻能力区分：

- 手机的移动服务（OTC Smartphone）→ 智能手机能力
- 话机登出的共享工位场景（UA 替代冻结）→ Desksharing 能力
- 远程通道本身 → 远程接入能力

## E — 可执行步骤

输入契约：并发 nomadic 用户数（规划输入）、目的号码清单、用户许可现状。池规模算例需按客户话务补做（书内只有公式）。

1. 规划池：并发数=Ghost Z 数（VoIP 另加等量 SIP 设备）。完成标准：号码段规划表评审通过
2. OXE 建池：Ghost Z（Analog+Nomadic feature）与 SIP 设备逐个建。完成标准：号码在服
3. OT 登记范围与 SIP Subscriber：min/max 与登录参数、SBC WAN。完成标准：两侧一致
4. 授权：Nomadic GSM/SIP 与 Desktop 逐用户勾选。完成标准：OTC PC 出现 routing 入口
5. 号码管理：Home/Mobile 填目的号码。完成标准：号码可保存（同事号码会被拒绝）
6. 行为测试：蜂窝切 Home、VoIP 切 PC 各测一轮；关闭 nomadic 后话机恢复。完成标准：冻结/恢复与资源释放符合预期
7. 资源核查：tsa_maintenance 选项 20 dump，缺项走 100→106 2998→7 手动同步。完成标准：全部 Ghost Z 在库

判停点：

- 用户看不到 nomadic 菜单 → 先查 Desktop 与模式许可（Nomadic GSM/SIP），不要查终端
- VoIP 配不上的排查顺序：先确认 cellular 管理已完成（p51 前提），再查 SIP 两侧参数一致
- "挂着不用也占资源"的投诉 → 机制如此（关闭才释放），向用户宣导用完即关，必要时扩池
- 目的号码要求填同事号码 → 需求不被 nomadic 支持（n03），改路由档案/呼叫转移另行实现

输出契约：资源池规划与登记记录 + 授权清单 + 蜂窝/VoIP 行为测试结论 + 资源一致性核查记录。

## B — 边界

- 池满后新用户无法激活：容量=最大并发连接数，且要向用户宣导关闭习惯（n05）
- UA 替代只覆盖 Desksharing 场景：一般 nomadic 需要在服话机做底（p61，见 Desksharing 卡）
- SIP 生存性（OXE CS/OXE PCS/第三方网关）不支持（p36）
- tsa_maintenance 原文 option 47 在菜单中不存在，核验按选项 20（nr-02）；秘密码 2998 为实验口径
- 实验池号 31017-31019/31951-31952 为实验口径，生产按客户号码计划替换
