# OTFC 客户端部署与封页定制（Windows 四件套、Web Client、GPO 批量、封页五步）

## R — 原文依据

> "SendFAX • Web Fax Composer printer • Print to mail ; Silent installation & Installation by Massive Deployment through Group Policy are available"（p83）
> "A reduced client applications set including only independent applications usable by most of the users (no administration tools) is available through the installation files located in the ClientRedistribution folder"（p84）
> "Download the server coversheet to your desktop: •Log in the Fax MMC Snap-in. •Go to the Site Cover Sheets node."（p93）
> "Import the new coversheet using the web administration interface of fax server … Assign the new coversheet in user Profiles."（p95-96）

出处：OTFCXTE200EN p71-96（含 How-To 实验 5）、p130-133。

## I — 自述

用户侧入口与品牌化两条线：

1. **Web Client**：免安装任意浏览器，http(s)://<服务器名或IP>/fax 需认证；六区界面（Compose/Inbound history/Outbound/Outgoing queue/Manage faxes & contacts/Inbox）；符合美国康复法案 508 条款与欧洲 e-inclusion 无障碍要求
2. **Windows 四件套**：SendFAX（进阶用户：实时预览、Outlook 模式、电话簿、redact 涂黑；Outlook 模式依赖 'FAX' 地址空间）、Web Fax Composer printer（打印即经 Web 界面发）、Print to Mail（打印成 TIFF 交 Outlook 择机发）、MMC Snap-in（管理端，随服务器已装）
3. **部署三规则**：静默安装 + 组策略（GPO）批量；精简客户端包在发行介质 ClientRedistribution 文件夹（无管理工具）；认证用域 Windows 账号或 OTFC 内部账号
4. **封页五步**：Coversheet Editor 编辑 .cse（专有格式，8 语言 2 纸张，内置 Tiff Viewer），或从服务器 MMC 下载底稿（Site Cover Sheets 节点）、另存新名、经 Web 管理界面导入、挂到用户 Profile（一个 Profile 可挂多张）

队列与历史三视图（用户只见自己，管理员见全部）：外发队列六状态（Preprocessing/Delayed/Ready to Send/Sending/Waiting/Sent）、外发历史（Sent/Failed）、入呼历史（Received/Failed to receive）。

## A1 — 书中案例

**客户端安装与测试**（p130-133，实验 5，实验口径）：

1. 若 MMC Snap-in 开着先关闭
2. 发行介质 Client 目录双击 Setup.exe，按向导 Next，选安装语言
3. Custom Setup 选装除 MMC Snap-in 与 Java API 外的全部应用
4. Web Server 对话框填内部主机名或 URL：fax（也可 http://192.168.1.60 或 https://fax）
5. 完成安装；提示重启服务器可安全忽略（实验机不做客户端用途）
6. 用 allen/barkley 账号逐客户端测试 inbound/outbound/queue/投递选项

## A2 — 未来触发

使用情境：给全员发传真客户端；用户问浏览器能不能发；SendFAX 里要涂黑敏感信息；企业封页怎么上线；用户问传真卡在哪个状态；批量装客户端怎么省事。

语言信号：客户端 / client / SendFAX / Web Client / Web Fax Composer / Print to Mail / 虚拟打印机 / GPO / 组策略。

语言信号（续）：静默安装 / silent / ClientRedistribution / 封页 / coversheet / .cse / Cover Sheet Editor / 队列 / queue / 外发历史 / inbound / outbound / 涂黑 / redact。

与相邻能力区分：封页"经 Profile 下发"的策略面归 Profile 策略能力；通知格式归邮件与 Exchange 集成与 Profile 策略能力；账号与密码归用户管理能力。

## E — 可执行步骤

输入契约：用户群体画像（进阶/普通/无安装权限）、工作站环境（Win11/10、终端服务）、企业封页素材（Logo/版式）、分发通道（GPO/手工）。

1. 选入口矩阵：普通用户 Web Client 免安装起步；进阶用户加 SendFAX；打印习惯用户配虚拟打印机。完成标准：入口方案与人群对应
2. 批量部署：GPO/静默安装推 Full 包或发 ClientRedistribution 精简包。完成标准：目标工作站客户端就位
3. 客户端服务器地址：按可接受语法填（主机名 fax / http://IP / https://主机名）。完成标准：登录认证通过
4. 建封页：Coversheet Editor 编辑或从服务器下载底稿另存新名。完成标准：新 .cse 文件就绪
5. 导入封页：Web 管理界面上传新封页。完成标准：封页出现在服务器列表
6. 下发生效：在目标用户 Profile 关联封页（可多张）。完成标准：测试传真首页为新封页
7. 验收：按三视图核对一次收发（队列状态/历史记录），Outlook 模式另验 FAX 连接器依赖。完成标准：全入口可用

判停点：

- SendFAX 要开 Outlook/Exchange 模式 → 先确认 'FAX' 地址空间连接器已建，没建就先做邮件与 Exchange 集成
- 用户问"为什么耳机…传真卡住" → 按外发队列六状态对号解释（Preprocessing 转换中/Delayed 定时未到/Waiting 等待资源），不要笼统说"在发"
- 实验机"客户端装在传真服务器 + 忽略重启" → 停，这是实验口径；生产装用户工作站，该重启就重启
- 客户要求手机上发传真 → 停，书内收发入口无移动端形态，按 Features List 与产品线现状答复

输出契约：客户端部署清单（入口/人群/分发方式）+ 封页上线记录（编辑/导入/Profile 关联）+ 验收测试结果。

## B — 边界

- 浏览器支持明细以 OTFC Features List 为准（书内只举例 Firefox/Safari/Chrome）
- "Outlook 2022" 为原文笔误（nr-02），客户端邮件环境矩阵以 Features List 为准
- 精简客户端包不含管理工具；MMC Snap-in 随服务器安装、也可由客户端包安装——双来源别重复装
- 封面语言受安装语言影响（Basic Profile 口径），装错语言的善后在首次交付能力
- .cse 为专有格式；编辑器细节（区域设置/注释/Tiff Viewer）书内为讲义级介绍
