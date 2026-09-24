# 语音邮箱与移动办公（VM 高级、ACC 两级控制、游牧模式、远程替代）

## R — 原文依据

> "Access control code will get by default a system generated random 6 digits value … ACC is kept after warm reset and newly generated after cold reset"（p383）
> "The lockout time is doubled for each denial (24 hours max value, 1440 minutes)"（p384）
> "In case of migration, this field is disabled • After cold reset or in case of new installation, by default • 'Mailbox consultation from any phone' is enabled • 'Mailbox remote consultation' is disabled"（p382）
> "if the caller is external, his CLI is sent to the nomadic terminal … If the caller is internal and has a DDI, this DDI is sent … Else the OXO Connect installation number is sent"（p466）
> "Secondary Trunk Group #100 #199 ARS Keep Yes … #100 to #199 in order to avoid conflict with line 100 to 199"（p471, p479）

出处：OXOCXTE301EN p379-404, p463-480。

## I — 自述

语音邮箱高级与移动性共用一套远程接入体系（VMU 远程定制 + Remote Access Code/ACC），合为一个闭环：

**语音邮箱高级**（p379-404）：

| 机制 | 口径 |
|---|---|
| 端口 | 语音服务器 2-8 端口，默认动态分配、可固定 |
| 本地开关 | "Mailbox consultation from any phone"：冷复位/新装默认启用，禁用后仅本机可查 |
| 远程权 | "Mailbox remote consultation"（Features/Part 3）：默认禁用；迁移场景该字段被置禁用（n60） |
| ACC 两级控制 | 空=标准认证（话机号+密码）；设值=ACC+话机号+密码。默认随机 6 位、最长 16 位、warm 保留/cold 重生成 |
| 锁定 | 连续失败翻倍（10 分钟起步、封顶 1440 分钟，VMUMaxTry）；本地远程共享计数；解锁五途（OMC/Webdiag/话机/话务员/PIMphony） |
| 个人助理 | 迷你 AA：三目的地（内部/外部/移动）+转话务员；noteworthy PerAssAlwd 默认禁用；远程转移选项受 DivRemCust 默认禁用 |

**游牧模式**（p465-468）：游牧话机（多为手机）替代本地话机（本地可物理可虚拟）；启用链=订阅户勾 Nomadic right（自动建 Virtual Nomadic 虚拟终端）→VMU 远程定制选项 6 激活并设目的地。CLI 三选一：外部主叫发原 CLI；内部主叫有 DDI 发 DDI；否则发安装号；计费小票含游牧信息。SIP 话机不支持（p147）。

**远程替代**（p469-480）：拨远程替代 DDI、远程接入码、分机号、密码，以该分机身份外呼；拨内部号加 # 前缀（#100-#199，#9 话务员）经内部 ARS 回环——避免与本地直拨 100-199 冲突。ACC 与远程 VM 接入共用同一密码菜单。

## A1 — 书中案例

**语音邮箱高级实验**（p394-404，厂商实验）：

1. 给 103 配个人助理三目的地：同事 101、外部 0210P41102、移动 0610P41101（实验口径）。
2. noteworthy PerAssAlwd 置 01 激活系统开关。
3. 话机侧经邮箱菜单 9→2 配助理（也可 Settings/Assistant）。
4. 给语音邮箱寻线组分 DDI 41500；关 "Mailbox consultation from any phone"、勾 101 远程查。
5. Remote Access Code 设码 780911（实验口径）。
6. 锁定测试：远程接入连错 3 次密码，邮箱锁 10 分钟并见于 History Table（p402）。
7. 远程定制：勾 103 Remote customization，经远程菜单把助理配移动号+转话务员。
8. 寻线组邮箱：509 组关联虚拟分机 112 的邮箱（VM 键 LED 通知）。

**游牧与远程替代实验**（p472-480，厂商实验）：

1. 话机 104 定制邮箱：录名+改密码（实验口径 142536）。
2. 勾 Nomadic right，核对自动创建 Virtual Nomadic 虚拟终端。
3. VM 组 DDI 配 021PN41500；Features Part 2 勾 Remote customization、Part 3 勾远程查。
4. 激活游牧：拨 VM DDI、接入码、邮箱 104、密码，菜单 9 再 6，输目的地 0021PN41102 按 # 确认。
5. 验证：104 显示 Nomadic mode，来话转到目的地；随后停用。
6. 远程替代：替代 DDI 41200、接入码 615243（实验口径）、Part 2 勾 Remote Substitution。
7. 内部 ARS：#100-#199 base ARS、NMT Keep、Private=Yes；ARS 表 Priv #1 00-99；列表 Index=Local。
8. 测试：打 021PN41200，接听音后拨接入码、104、密码，拿到拨号音以 "#" 开头拨内部分机（p480）。

## A2 — 未来触发

使用情境：手机在外接分机电话；出差用任何话机查留言；远程改呼叫转移；邮箱被锁了；怕被人盗打远程邮箱；以自己分机身份在公司外呼出；升级后远程查不了邮箱。

语言信号：语音邮箱 / voice mail / 远程接入 / ACC / 锁定 / VMUMaxTry / 个人助理 / personal assistant / 游牧 / nomadic / Virtual Nomadic / 远程替代 / remote substitution / 远程接入码 / VMU / 远程定制 / "# 前缀"。

与相邻能力区分：远程接入码/ACC 的密码策略与锁定公式归安全加固能力；# 前缀内部 ARS 的三表机制归 ARS 套件能力；VMU 菜单里的转移选项 7 依赖 noteworthy DivRemCust（维护工具域的 noteworthy 修改流程）。

## E — 可执行步骤

输入契约：用户清单与移动需求、VM 端口与 DDI 规划、接入码与 ACC 策略、授权范围（哪些用户开远程权）。授权范围未定 → 判停按默认全关交付，逐用户开通。

1. VM 基线：确认端口分配与本地开关；新装默认"任意话机可查开+远程查关"（迁移则远程字段禁用，n60）。完成标准：VM 可用
2. 远程接入：给 VM 寻线组分 DDI；按需勾 Mailbox remote consultation。完成标准：外部可入
3. ACC 两级：Remote Access Code 设值即升级为三级认证（默认随机 6 位，可改至 16 位）。完成标准：防盗打口径成文
4. 个人助理：PerAssAlwd 置 01，配三目的地；远程转移需求另开 DivRemCust。完成标准：未接来话按助理分发
5. 游牧：勾 Nomadic right → VMU 选项 6 激活并设目的地 → 话机显示 Nomadic mode。完成标准：来话跟随
6. 远程替代：替代 DDI + 接入码 + Part 2 勾权；内部 ARS 配 #100-#199 段。完成标准：回环拨内部通
7. 验证：远程接入听留言、试错密码验锁定翻倍、外呼核对 CLI 与计费小票。完成标准：三场景闭环

判停点：

- 用户报"远程查不了邮箱"且为迁移系统 → 先核 n60 默认值矩阵再查权限
- SIP 话机用户要游牧 → 不支持（p147，推断：另走 Rainbow/软话机路线）
- 锁定中用户急用 → 走五途解锁（OMC 重置/Webdiag/话机改密/话务员/PIMphony），不要等锁时
- 远程接入码与分机密码混为一谈 → 停，两者是两层认证；ACC 改动影响远程替代与远程 VM 两个入口

输出契约：VM/移动授权清单（按用户）+ ACC 与接入码策略记录 + 游牧/替代场景测试结论 + 锁定事件验证记录。

## B — 边界

- 实验接入码（780911/615243）与密码（142536）为实验口径；生产按客户密码策略生成
- 防盗打三提醒（p382）：勤改邮箱密码、不用简单数字序列、遵 TC1143；ACC 是第一防线不是唯一防线
- 游牧 CLI 规则与计费小票内容随游牧变化：对账时注意小票新增游牧信息
- 远程定制默认三级全关（游牧按用户/远程定制按用户/DivRemCust 系统级，n54）：用户报"激活不了"先查授权链
- VMU 菜单语音为系统内置；自定义欢迎消息（MSG1-20）挂寻线组，与实体 MoH 录制入口共用但语义不同（n24）
