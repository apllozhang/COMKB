# Connection 用户与语音邮箱交付（建户/寻址/许可核查/信箱三级对象）

## R — 原文依据

> "The resurrection method is used when no physical address is allocated to the set … Resurrection consists in dialing the phone directory number & the password ('0000' by default) directly, from the set"（p113）
> "Thank's to the directory number, you will be able to make the link between the user set up on OXE and its OTMC account."（p136）
> "Before validating the mailbox creation, it's mandatory to assign a profile to the voice mailbox, in the « configuration » tab."（p139）
> "Check that the users have the 'Voice mail' right enabled."（p141）

出处：OTMCXTE200EN p109-145（c06/c07、f15/f16、p11/p12/p13、n24 归并）。

## I — 自述

交付分 OXE 侧（宿主用户）与 OTMC 侧（信箱）两段。

**OXE 侧三件事**：

1. 建户两法：8770 的 OXE Configuration 接口（Users 右键 Create，General Characteristics 页签）或 Users 应用（Create user，含 OXE mailbox directory number 字段；OT applications=None 表示不用 OT 套件应用但仍可有 OTMC 信箱）；声明用户时话机设备自动创建
2. 寻址三法：resurrection（话机处于 255/255/255 空态时直拨分机号+密码 0000，自动绑定真实物理地址；移机配 In/Out of Service 前缀，ednump –l 查）、空闲地址表（System > Free addresses）、IP 话机静态 IP（i+# 菜单，TFTP=呼叫服务器 main 地址，注册输分机号+secret code 默认 0000）
3. 许可核查：三族六类对照 + 8770 Software package 过滤或 mtcl 登录跑 spadmin（左=已用/右=可用）

| 族 | License | 名称 | 话机 |
|---|---|---|---|
| TDM | 174 | Analog users | Z 设备模拟话机 |
| TDM | 173 | Advanced reflexes users | 8029/8039（UA 设备） |
| TDM | 316 | Connection reflexes users | 4019 |
| IP | 176 | Advanced IP users | 8028/8038/8068 |
| IP | 317 | Connection IP users | 4008/4018 |
| SIP | 177 | SIP users | SEPLOS/SIP 设备 |

**OTMC 侧三级对象**：

1. VMS：核验默认语音邮件系统存在（p138/p188 写 defaultVmsLS、p137 界面作 defaultVmLS，见 nr-06），Type=Local Storage
2. mailbox：General 页签定名/类型（Local Storage）/所属 VMS；Configuration 页签必须挂 profile 才能保存（强制前置）
3. user：Contacts 页签分机号必须与 OXE 用户一致（唯一挂钩键）+ 公司邮箱；Passwords 页签 TUI/GUI 密码；Licenses 页签 MyIC Business Communications 与 Voice mail 必开、Messaging API 可选；最后回 Mailboxes 页签把信箱挂给人

## A1 — 书中案例

**用户与信箱交付实验**（c06+c07，分机号/口令等环境值见 book/overview）：

1. 8770 建三个 Connection 用户（实验分机号 31000-31002，实验口径）
2. 数字话机走 resurrection：保持 255/255/255 空态，话机直拨分机号+默认密码 0000，地址自动绑定
3. IP 话机：断电重启按 i 键再 # 键进菜单，配静态 IP，TFTP 指向呼叫服务器 main 地址，注册后 in service
4. 许可核查：mtcl 登录呼叫服务器跑 spadmin 读计数（左=已用右=可用），或 8770 Software package 过滤
5. OTMC 建账户：General 页签录身份；Contacts 页签分机号对齐 OXE 用户并填公司邮箱
6. Passwords 页签设 TUI/GUI 密码（可选勾首登强改 TUI 密码）；Licenses 页签开 MyIC 与 Voice mail
7. 核验 VMS：Services/Topology/VMS 确认默认系统存在且为 Local Storage
8. 建信箱：Users and devices/Voicemail box 右键 Create；Configuration 页签必选 profile 才能保存
9. 分配信箱：Users 的 Mailboxes 页签搜索信箱挂接并 Apply
10. 核查 Voice mail 权：用户 Licenses 页签为 Enabled
11. TUI 验证：话机登录信箱改姓名密码，互留留言试听，核对 MWI 亮灯（信箱测试清单）

## A2 — 未来触发

使用情境：给新员工开语音信箱；"有信箱不能留言"；话机认领不了分机；信箱保存报错；话机许可够不够；用户换话机位置。

语言信号：Connection 用户 / 建户 / resurrection / 空闲地址 / IP 话机 / secret code / spadmin / OTMC 账户 / 信箱 / mailbox / defaultVmsLS / Voice mail 权 / Mailboxes 页签 / 分机号对齐。

与相邻能力区分：批控 profile 与问候语归 otmsg-mailbox-profiles；通道打不通查 otmsg-sip-trunk-provisioning；声明同步未做先回 otmsg-declaration-sync。

## E — 可执行步骤

输入契约：OXE 已被 8770 纳管、OTMC 已声明同步、目标话机许可族余量已知。DHCP 归客户网络管理员（书外，p116）。

1. 建 OXE 用户并开通话机：按话机类型选寻址法（resurrection/空闲地址/IP 静态）。完成标准：话机 in service
2. 核话机许可：spadmin 或 8770 过滤确认目标族有余量。完成标准：许可够用
3. 建 OTMC 账户：分机号与 OXE 一致、公司邮箱、TUI/GUI 密码。完成标准：账户创建成功
4. 核 VMS 建信箱：Configuration 页签必挂 profile。完成标准：信箱保存成功
5. 挂信箱开权限：Mailboxes 页签分配 + Voice mail 权 Enabled。完成标准：用户带可用信箱
6. 端到端验证：互留留言、MWI 亮灯、TUI 收听。完成标准：信箱业务闭环

判停点：

- "有信箱但不能留言" → 先查用户 Licenses 页签 Voice mail 权（p141），再查信箱是否挂到人
- 信箱保存报错 → Configuration 页签没挂 profile（强制前置，p139）
- 话机认领失败 → 核对 255/255/255 空态与密码（默认 0000）；交付清单必须含"改每台话机 secret code"（n24）
- spadmin 计数为 0 可用 → 停，先补许可，不要强行开通

输出契约：可电话可达的 OXE 用户 + 带邮箱与 Voice mail 权的 OTMC 账户 + 许可核查记录。

## B — 边界

- resurrection/IP 注册默认密码 0000 是出厂口径，生产是"任何人拿到话机就能认领分机"的安全口子；改法属 OXE 课程（n24）
- DHCP 服务器管理不在本培训内（p116 Note）
- OT applications=None 的含义：不用 one number/会议/OTC PC 等 OT 应用，与是否拥有 OTMC 信箱无关（p112）
- spadmin 需 mtcl 账号登录呼叫服务器；实验分机号、口令、用户名单集中见 book/overview
- 信箱可建户时或建户后分配（p122）；信箱命名示例为自由文本口径
