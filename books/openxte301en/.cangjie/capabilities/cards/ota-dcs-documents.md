# DCS 文档转换服务器（Office 文档会议演示）

## R — 原文依据

> "Natively, without any installation of additional component, only 'pdf' and 'images' documents can be shared"（p365）
> "Warning Failure to perform these updates will result in documents that remain in the queued state and do not get converted."（p375）
> "Hyper-threading must be deactivated on the VM: set the option 'Hyperthreaded Core Sharing' to 'None'"（p373）

出处：OPENXTE301EN p363-383。

## I — 自述

DCS 决定会议能不能演示 Office 文档，两模式两形态：

1. **Basic（零安装）**：ACS 内嵌，只支持 pdf 与图片（png/gif/jpeg）；Office 文档只能当附件（attachment 可下载）
2. **Advanced（装 DCS）**：doc/docx/ppt/pptx/xls/xlsx 可作 presentation（参与者不可下载；attachment 可下载）
3. **内部 DCS**：OT 服务器 KVM 上自动构建 Windows 虚机（供 Windows/Office 介质与密钥，约 20 分钟+15-30 分钟）；兼容 Win7 32 位 + Office 2010/2019（US English）
4. **外部 DCS**：ESXi 虚机（必须 Hyperthreaded Core Sharing=None）或物理机；兼容面更宽（Win 8.1/2008R2/2012R2/Win10 + Office 2010/2013/2016）；ACS 管理台登记地址与管理员账号，DCS 软件由 OT 自动推送更新
5. **Windows 侧预配置四件**：关防火墙、UAC 从不通知、账号密码永不过期、注册表 Winlogon 四键自动登录（改完必须重启虚机）

## A1 — 书中案例

**DCS-V 外部虚机部署实验**（p374-383）：

1. 前提：Windows 机装好 Office，激活双许可并打齐强制更新（否则文档卡 queued）
2. 关闭专用/公用网络防火墙，UAC 设为从不通知
3. 账号勾密码永不过期（实验口径 Administrator/superuser）
4. 注册表 Winlogon 四键（AutoAdminLogon/DefaultDomainName/DefaultUserName/DefaultPassword）后重启虚机
5. 挂 DCS ISO，拷 dcs_install.bat 等三文件到 C:\temp 执行
6. 重启后验证自动登录与 DCS 两窗口自启
7. OT 侧声明：Advanced Settings 配 Remote DC 地址与管理员账号
8. 测试：OTC PC 上传 Office 文档为 presentation 并演示成功

## A2 — 未来触发

使用情境：会议里要放 PPT/Word/Excel；文档一直 queued 不转换；DCS 装哪（内部还是外部）；Office 版本兼容性；虚机装完转换服务不起。

语言信号：DCS / Document Conversion Server / 文档转换 / presentation / 演示 / queued / KVM / ESXi / Hyperthreaded / dcs_install / Remote DC / Office 转换 / pdf 图片。

与相邻能力区分：会议本体（预约/角色/密码）→ 协作会议能力；文档的下载权限规则也在会议卡（presentation 不可下载）。

## E — 可执行步骤

输入契约：Windows/Office 许可与介质（ALE 不提供）、虚拟化平台、Office 文档使用需求。

1. 选形态：内部 KVM（OT 一体化）或外部 VM/物理机（按规模与运维习惯）。完成标准：形态确认
2. Windows 预配置四件+重启。完成标准：自动登录生效、DCS 组件自启
3. OT 侧声明外部 DCS（地址+账号）。完成标准：管理台登记成功
4. 端到端测试：上传 Office 文档作 presentation。完成标准：能转换能演示

判停点：

- 文档卡 queued → 根因在 Windows 侧（许可未激活或强制更新未打齐），别去查 ACS 配置（n30）
- 改完注册表不重启 → 自动登录不生效、DCS 组件不起（n31）
- 客户的 Office 是俄语等小语种 → 多数西欧语言可用，其余需手动装语言包（p371 语境）
- 最新兼容性 → 以 OT release note 为准（书内明示口径会过时）

输出契约：DCS 形态与部署记录 + Windows 预配置清单 + Office 演示端到端验证结论。

## B — 边界

- Windows 与 Office 的介质和许可 ALE 一概不提供，项目预算自备（p367）
- 内部 DCS 兼容面窄（Win7 32 位 + Office 2010/2019 US English），外部更宽——选型时对照矩阵
- p371 "Windows 2010" 为原文笔误（应为 Windows 10，nr-05）
- 实验虚机账号（Administrator/superuser）为实验口径，生产必须替换
