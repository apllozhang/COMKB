# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 首用户邮箱两页不一致（barkley vs baker）

- **位置**: p50（First time wizard 讲义页）"Username: barkley@company.com" vs p70（FTW How-To 实验页）"User's email address: baker@company.com"。
- **差异**: 同一"首用户创建"步骤在讲义与实验两页取了生态示例中两个不同的真实账号（p45 生态图：barkley=31600 用户、baker=传真管理员）。
- **影响**: 照书做实验时首用户身份取哪个都能走通（两账号都在内部库），但写实验报告/交付文档时若混引两页会自相矛盾。
- **处置**: 能力卡按实验页口径执行（首用户 baker@company.com），并注明讲义页写 barkley；候选 p08/c03/n24 已完整记录。

## nr-02 "Microsoft Outlook 2022" 版本号疑为原文笔误

- **位置**: p41 Client Requirements："Microsoft Outlook 2022 / 2019 / 2016 (64-bit and 32-bit)"。
- **判断**: 桌面 Office 没有 2022 版本（2021 之后为 2024/365 路线——版本常识推断，原书如此）；同页工作站与终端服务器版本（Windows 11/10、TS 2022/2019）正常。
- **处置**: 保留原文不改；给客户出客户端环境方案时以 OTFC Features List 为准核实（原书同页明示 "Refer to feature list"）。

## nr-03 未展开缩写的全称均系推断（引用需带标注）

- **位置与清单**: DNIS/CSID/ANI（p9）、DDI（p205/p207）、ARS（p211）、MLE/SMB（封面与页眉）、CSGD（p34）、MMC（p74）、BIRT（p226）、UTL（第一本教材沿用词，本书未展开）、NT（p100）等，书内均未给全称。
- **处置**: 候选中的括注（如 DNIS=被叫号码识别、DDI=直拨、ARS=呼出路由选择）全部保留"（推断）"或"书中未展开"标注；能力卡引用时不升格为原文事实。书内确实给出全称的仅 FoIP、NDR、IIS、MFP 等。

## nr-04 SMTP 网关服务名两种写法并存（原文如此）

- **位置**: p51/p65/p183 写 "XMSMTPGateway"；p157/p158 写 "XMSmtpGateway"（module）。
- **判断**: 同一服务的两种大小写并存，疑为原文排版不统一；Windows 服务名以 services.msc 实际显示为准。
- **处置**: 能力卡统一采用服务界面口径 "XMSMTPGateway"，引用模块介绍时照原文 "XMSmtpGateway"；不据此判定版本差异。

## nr-05 p42 端口表与 p38 资源表正文缺失（提取文本无数值）

- **位置**: p42 "Ports in use" 与 p38 "Recommended server resources" 两页在提取文本中仅有标题与 "Always refer to the OTFC features list" 提示，无任何数值表格。
- **判断**: 原书即为指针页（数值外置 Features List），或为截图页文本不可提取；两种可能不影响口径——书内都不出数。
- **处置**: 防火墙白名单与售前 sizing 一律指向 OTFC Features List；已知书内数值仅 SIP UDP 5360（p142）、SMTP 25（p183）、LDAP 389（p196）三处（n26/n27）。

## nr-06 p148 停止命令行表述混用（原文如此）

- **位置**: p148 CHtrace 抓包页停止说明："kill the process "traced" with the command : "killall mtracer""。
- **判断**: 本页启动的进程是 mtracer，命令 killall mtracer 正确；"traced" 字样系与 p149 SIP trace 页（killall traced）混排的笔误。
- **处置**: 按 p31 逐字口径记录；能力卡引用时注明"进程名与命令以启动命令为准：CHtrace 用 mtracer、SIP trace 用 traced"。

## nr-07 编辑残留：p66/p151 页眉 "Communication Suite for SMB"

- **位置**: p66 与 p151 两章章头页眉写 "Communication Suite for SMB"，全书其余章节页眉均为 MLE。
- **判断**: 排版残留（MLE/SMB 均未展开全称），不影响内容归属。
- **处置**: 不改原文；引用章节名时按章标题（First Time Setup Wizard / OXE SIP gateway configuration）而非页眉。

## nr-08 三处以上含推断成分的结论（引用需带标注）

- n04: 许可 MAC 绑定意味着虚拟化迁移需注意（推断，书中未展开）。
- n10: 备份管理员"与主管理员用不同认证路径更能对冲风险"（推断，原文只给推荐动作）。
- n22: 私人电话本"收进公共电话簿更稳"（推断，原文只给路径）。
- n28/n29/n32: HA 部署书外、OXE 侧照书做完"大概率"回工、TLS 指路（边界推断，原文未指路或仅说 refer to TC3048）。
- g42: G.711 透传比 T.38 对抖动更敏感（电信常识推断，原文只给速率）；g57: Interstar Technologies 键名揭示 XMedius 血统（合理推断，书中未明说）。
- **处置**: 全部保留"（推断）"标注；能力卡引用时维持标注，不升格为书中明示事实。
