# OMC 安装与首次连接（OXO Connect）

## R — 原文依据

> "Make a connection to the system with OMC in Expert mode with server authentication ... Enter the default installer password pbxk1064 only used for the first connection"（p59）
> "The passwords must be different for each customer!"（p62）
> "browse to, ''Trusted Root Certification Authorities''"（p61）

出处：OXOCXTE107EN p54-64。

## I — 自述

OMC 是 OXO 的管理客户端，一切配置从它开始。流程五段：装软件（解压 setup.exe 以管理员运行，选语言/目录/国家分销渠道/目标产品/显示语言）；首连（Expert 菜单 → LAN/WAN → 填设备 IP——出厂默认 192.168.92.246——勾选 Server authentication，输一次性首连密码 pbxk1064）；装证书（安全告警里 View certificate → Install certificate → 放入 Trusted Root Certification Authorities，一劳永逸消除告警）；改密（各账户密码必须逐客户不同，之后可在 OMC/Security 菜单改）；录客户信息（带 * 必填），完成后右下角图标显示已连接。

## A1 — 书中案例

**OMC 安装实验**（p54-64，厂商实验）：RLAB 环境下在 OXOC_PC_CLIENT 虚机的桌面 SOFTS OXO CONNECT 目录解压安装；首连填 192.168.92.246 + pbxk1064；证书装入受信任根后告警不再出现；改密后录入客户与供应商信息，右下角图标变绿即为连接成功。

## A2 — 未来触发

使用情境：新设备首次管理；重装 OMC 后连不上；每次连接都弹安全告警；问 pbxk1064 是什么。
语言信号：装 OMC / 连不上 / security alert / 证书告警 / pbxk1064 / 首次连接 / first connection / Expert mode。

与相邻能力区分：连上之后的 IP 参数修改 → IP 规划能力；本能力到"连接建立"为止。

## E — 可执行步骤

输入契约：管理 PC（Windows）、设备管理 IP（出厂 192.168.92.246 / 已改则用现值）、首连密码。缺密码先向设备交付方索取，不要用文档默认值猜生产设备。

1. 安装：解压 → setup.exe（管理员）→ 语言 → 目录 → 国家/渠道（可多选）→ 目标产品 → 显示语言 → Install → Finish。完成标准：桌面出现 OMC。
2. 首连：打开 OMC → Expert 菜单 → LAN/WAN → 填设备 IP → 勾 "Server authentication" → 输首连密码。完成标准：进入系统或弹出证书告警。
3. 证书：告警框 → View certificate → Install certificate → 存放位置选 "Trusted Root Certification Authorities" → OK → Finish。完成标准：下次连接不再告警。
4. 改密：逐账户定义新密码（每客户必须不同；OMC/Security 可再改）。完成标准：全部账户脱离默认值。
5. 客户信息：录入带 * 必填项与可选供应商信息。完成标准：右下角连接图标显示已连接。

判停点：首连密码被改过且无人知道 → 走设备密码重置流程（原书未覆盖），不要反复试错。

输出契约：可用的 OMC 管理会话 + 已改密账户清单。

## B — 边界

- pbxk1064 是出厂一次性首连密码：仅实验/出厂态可用；生产设备密码已被要求首连时更换。
- 原书全程内网明文管理，生产环境的管理访问加密/隔离不在原书范围（阶段 0 批判）。
- OMC 版本与设备软件版本的兼容矩阵原书未提，装不上先核版本。
