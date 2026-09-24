# OMC 安装与首次连接（OXO Connect）

## R — 原文依据

> "Make a connection to the system with OMC in Expert mode with server authentication ... Enter the default installer password pbxk1064 only used for the first connection"（p59）
> "The passwords must be different for each customer!"（p62）
> "browse to, ''Trusted Root Certification Authorities''"（p61）

出处：OXOCXTE107EN p54-64。

## I — 自述

OMC 是 OXO 的管理客户端，一切配置从它开始，流程五段：

1. **装软件**：解压 → setup.exe（管理员）→ 选语言/目录/国家分销渠道/目标产品/显示语言
2. **首连**：Expert 菜单 → LAN/WAN → 填设备 IP（出厂 192.168.92.246）→ 勾 Server authentication → 输一次性首连密码 pbxk1064
3. **装证书**：安全告警 → View certificate → Install certificate → 放入 Trusted Root Certification Authorities——一劳永逸消除告警
4. **改密**：各账户密码必须逐客户不同（之后可在 OMC/Security 改）
5. **录客户信息**：带 * 必填；完成后右下角图标显示已连接

## A1 — 书中案例

**OMC 安装实验**（p54-64，厂商实验）：

1. RLAB 的 OXOC_PC_CLIENT 虚机桌面 SOFTS OXO CONNECT 目录解压安装
2. 首连 192.168.92.246 + pbxk1064
3. 证书装入受信任根，此后告警不再出现
4. 改密并录客户/供应商信息
5. 右下角图标确认连接。

## A2 — 未来触发

使用情境：新设备首次管理；重装 OMC 后连不上；每次连接弹安全告警；问 pbxk1064 是什么。

语言信号：装 OMC / 连不上 / security alert / 证书告警 / pbxk1064 / 首次连接 / first connection / Expert mode。

与相邻能力区分：连上之后的 IP 参数修改 → IP 规划能力；本能力到"连接建立"为止。

## E — 可执行步骤

输入契约：管理 PC（Windows）、设备管理 IP、首连密码。缺密码向设备交付方索取，不要拿文档默认值猜生产设备。

1. 安装：解压 → setup.exe（管理员）→ 逐项选择 → Finish。完成标准：桌面出现 OMC
2. 首连：Expert → LAN/WAN → IP + Server authentication + 首连密码。完成标准：进入系统或弹证书告警
3. 证书：View certificate → Install certificate → Trusted Root → Finish。完成标准：下次连接不告警
4. 改密：逐账户定义新密码。完成标准：全部账户脱离默认值
5. 客户信息：必填项录入。完成标准：右下角显示已连接

判停点：首连密码被改且无人知道 → 走设备密码重置流程（原书未覆盖），不要反复试错。

输出契约：可用的 OMC 管理会话 + 已改密账户清单。

## B — 边界

- pbxk1064 是出厂一次性首连密码：生产设备已在首连时要求更换
- 原书全程内网明文管理；生产的访问加密/隔离不在原书范围
- OMC 版本与设备软件版本的兼容矩阵原书未提——装不上先核版本
