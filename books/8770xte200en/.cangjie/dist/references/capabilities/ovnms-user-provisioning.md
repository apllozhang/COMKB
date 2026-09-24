# OmniVista 8770 用户开通（Profile / Meta profile / 批量 / WBM）

## R — 原文依据

> "Select Use profile with auto. recognition ... This parameter allows creating a user from a profile."（p183）
> "Warning: SYNCHRONIZATION IS REQUIRED TO RETRIEVE THE FREE NUMBER RANGES FROM THE OMNIPCX ENTERPRISE!"（p205）
> "Personal and mandatory attributes which can't be provided by the Profile or Metaprofile replaced by XXXX to invite the administrator to enter them; Attributes that can be automatically computed from Profile or Metaprofile set to NULL"（p216）
> "Mass provisioning file generated from thick client cannot be used in WebAdmin and vice-et-versa"（p250）
> "Action[+;-;#] Replace the # by the + character, to add a new user."（p258-259）

出处：8770XTE200EN p170-224（Users 应用与批量）、p225-260（WBM）。

## I — 自述

开通能力四层递进：手建、Profile 复用、Meta profile 自动取号、批量文件；WBM 是给非专家的轻入口。

**Profile 机制（OXE 侧模板）**

- OXE 侧建 Set Function=Profile 的特殊用户：General Characteristics 页设 Profile、Rights 页设三个 COS（Public Network/Phone Feature/Connection）、All 页设继承默认值
- 生效双前提：OXE System Parameters 勾 "Use profile with auto. recognition"；Profile 名称必须全大写
- 8770 建户时选 profile 即继承参数；profile 用户默认不在 Users 文件夹显示，按 Filter "Set Function = Profile" 查看
- Key profile：set profile（机型+Profile）> Progr. Keys（键位定义）> Profile Features（键功能关联）；建户选 Key Profiles 自动配键；取回 8770 需同步一次

**Meta profile（8770 侧自动取号模板）**

- 构成：Meta profile 名 + OXE 节点 + OXE 空闲号码段 + 设备类型 + OXE profile（可选）+ Key Profile（可选）
- 前置：OXE 侧建 Free Numbers Ranges List 后必须同步，8770 才可见
- 建户只填姓名即自动取段内首个空闲号并填满 OXE 属性；选了 OXE profile 时邮箱号字段不可用

**批量开通（thick client 文件语义）**

- 导出四法：全参导出（改参用，定位靠 UID，全表头文件直接再导入无效）、空模板（仅表头）、单用户模板 Export user for template（批量新建首选）、Rainbow 用户批量（导 OXE 数据建 Rainbow 用户）
- 字段占位：XXXX=必填人工填；NULL=由 profile/metaprofile 自动计算；action 取 ADD/MODIFY/DELETE（模板默认 ADD）
- 手工指定号码：填 oxeDirectoryNumber 字段
- 导入：Users 树根右键 Import user data > From local drive（文件类型选 All Files）；核验双通道——Users 树确认 + Scheduler 的 Import user data 任务绿态与 ADD 成功日志

**WBM 轻客户端（非专家入口，需 Unified Management 许可）**

- 入口 https://<FQDN>:8443 > NETWORK MANAGEMENT > Users；单建向导按 User > Main device 选项卡渐进
- 批量：Export（Type 选 Users data 或 Template、TXT、Immediate）落下载目录；文件 action[+;-;#]（# 原样导出、+ 新增、- 删除）；import 后看 Activity report
- 三条红线：不能从用户移除设备；不能移除 Connection 用户的 OT 应用；thick client 与 WBM 批量文件互不通用
- 设备页签上限 4 个，ALES-Desktop/ALES-Mobile 软终端计入上限；secretCode 填 NULL 会以默认密码 1234 建户

## A1 — 书中案例

**Profile 建户实验**（p182-195）：

1. OXE 配置界面勾 Use profile with auto. recognition
2. Users 文件夹右键 Create 建 profile BASIC（大写），Directory number 用空闲物理号
3. Rights 页设三个 COS 值（实验取 3/4/5）
4. Users 应用建户 Bruno Black 引用 BASIC，Rights 页三 COS 自动按 profile 填入

**Meta profile 实验**（p203-210）：

1. OXE 建号段 Range 31050-31059 后同步（Partial > Separate）
2. Users 应用 Profiles 页建 OXE meta profile：绑节点、号段、设备 IP Touch 8078s、profile BASIC
3. 建户 Bobby Bell 只填姓名，号码自动取段内首个空闲号，OXE 侧参数正确

**批量实验**（p219-224）：导出 Bobby Bell 模板，Excel 改出 Berta Bernstein（action=ADD、oxeMetaProfile 填好、其余 NULL），Import user data 导入，Scheduler 任务绿态。

**WBM 实验**（p253-260）：单建 Beatriz Buckler（号码 31014、profile BASIC）；导出 Bruno Black 文件改出 Bill Buffy（action 改 +、secretCode 改 NULL），导入后 Activity report 确认。

## A2 — 未来触发

使用情境：开局批量建户；迁移导户；新员工自动取号；给话机预配可编程键；客户自助用 WBM 开户；批量导入报错。

语言信号：profile 自动识别 / BASIC / meta profile / 空闲号段 / 自动取号 / XXXX NULL / Import user data / Export user for template / Rainbow 批量 / WBM / Activity report / secretCode 1234。

与相邻能力区分：节点没同步先查接入（节点接入能力）；账户权限与白名单（安全管理能力）；本能力管"把用户建出来"，不管权限收敛。

## E — 可执行步骤

输入契约：已同步的 OXE 节点、开通清单（姓名/设备类型/号码规则或号段）、批量场景确认 thick client 与 WBM 不混用文件。

1. 开关核查：OXE System Parameters 勾 Use profile with auto. recognition。完成标准：不勾则 profile/key profile 均不工作
2. 模板准备：建 profile（大写名+COS）或 meta profile（号段已同步）。完成标准：Filter 可见 profile / Profiles 页可见 meta profile
3. 手建验证：先建 1 个引用用户。完成标准：COS 继承生效或号码自动取段内首个空闲号
4. 批量导出：选样板用户 Export user for template。完成标准：文件含优化键值（XXXX/NULL 语义可读）
5. 文件编辑：改必填项与 action，其余 NULL 保留。完成标准：逐行核对 action 与号码字段
6. 导入：树根右键 Import user data > From local drive > All Files。完成标准：成功消息 + Scheduler 任务绿态
7. WBM 线：8443 登录单建或导改导批量。完成标准：Activity report 无错误 + thick client 侧可见
8. 收尾安全：WBM 批量默认密码户立即改密。完成标准：无 1234 弱口令残留

判停点：

- 号段下拉为空 → 号段建后未同步，先同步再建 meta profile，不要手填号码段
- 拿全参导出文件做批量新建 → 换单用户模板（全表头导入无效）
- 要"移除设备/移除 OT 应用"或超 4 设备页签 → 转 thick client，WBM 做不了
- thick client 文件拿到 WBM 导（或反之）→ 判停换文件，两边格式互不通用

输出契约：新用户清单（含号码与 profile 归属）+ 导入任务日志 + 弱口令整改记录。

## B — 边界

- WBM 需 Unified Management 许可；Performance/目录树管理等进阶属许可包差异（见许可管理卡）
- 批量文件只能"加/改/删用户"，不覆盖设备资产盘点；Devices 应用仅面向 OXE 的 SIP 设备
- secretCode=NULL 的默认密码 1234 是批量弱口令源头（安全审计必查）；生产开通必须配套改密流程
- Manage My Phone 终端自助（呼转/密码重置/可编程键）另有许可与并发口径（20 OXE/100 并发、仅法语英语），本书只作功能分区介绍
- 实验用户名单（Bruno Black/31000-31002 等）与实验密码为教学口径，见 book/overview
