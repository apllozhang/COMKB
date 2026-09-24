# OTC 智能手机交付全流程（REX/DISA/ARS 自动创建、iPhone APNS 特例）

## R — 原文依据

> "Automatic configuration of these objects when a Smartphone is associated to a Connection user ...: Remote extension / SIP device / Remote extension Number / Direct Speed Dialing Number / Discriminator Rule / ARS Route list / ARS Route SIP / ARS Route GSM / Tandem"（p94）
> "Do NOT use a number beginning with letter (A,B,C,D) in the directory number of the Remote Extension!"（p132）
> "From release 2.6 of OpenTouch, the main device can be directly the remote extension"（p134）

出处：OPENXTE301EN p76-147。

## I — 自述

智能手机的复杂度被"自动创建"消化，管理员的核心动作是配基座、做关联、做核验：

1. **基座（OXE 侧一次配置）**：专用 ARS 前缀（例 #0/#0306）、RE DISA 前缀 31280（必须能被 DDI 翻译表翻译）、DISA 免码替换两级授权、激活/停用前缀 61/62、专用 Ghost Z 池（可用 B<号> 占假号）、直达速拨范围（长度不能为 0 也不能满）
2. **Wi-Fi 到 GSM 溢出三参数**：Decline 映射 CH Cause=Temporary failure、INVITE 重传 2 或 3、Trunk COS 定时器 T310=60
3. **关联即自动建**：把手机关联到 Connection 用户时，系统自动建 RE、SIP 设备、RE 号码、速拨号、识别码规则、ARS 路由表（Route 1=SIP 设备、Route 2=公网拨手机）、Tandem（主话机与 RE 双多线绑定）
4. **手工两项**：Entity 识别码选择器（逻辑识别码映射物理识别码）与公网 COS 区域号 barring 放行
5. **iPhone 特例**：APNS 推送走苹果云（TCP 5223/2195/2196/443），证书一年有效、每年装专用 hotfix；后台唤醒多次 INVITE 本地 UDP 强制、经 SBC 出网 TCP 强制；VoIP everywhere 需 kamailio-wasp+wspcfg 组件与 5265 端口专用 SBC 声明
6. **R2.6 分水岭**：RE 可直接作主设备（单设备），此前需永不入服的 SIP 扩展做主机加溢出

授权关键：用户 Licenses 页签 Off site mobility 必须手动勾选，漏勾手机侧不可用。

## A1 — 书中案例

**从通用设置到 App 安装的交付实验**（p120-147）：

1. OXE 建专用 ARS 前缀与逻辑识别码（例 #0306、识别码 3，实验口径）
2. 建 RE DISA 前缀 31280 并核对 DDI 翻译表可翻译
3. 配 DISA 免码替换（系统级 Without code+中继组级 Yes）与激活/停用前缀 61/62
4. 建专用 Ghost Z 池（B<号> 形式）与直达速拨范围（起始 0、长度例 1000）
5. 配溢出三参数（Decline 映射、INVITE 重传、T310=60）
6. OT 侧声明 iPhone+ SBC（同 FQDN、端口 5265）并执行前缀同步、手填 DISA 公网号与 ARS 信息
7. 建设备档案（OTC Smartphone：Android/iPhone、GSM/Wifi/双模、SBC WAN、协议 UDP）
8. 用户关联：Associate SIP device→New→OTC Smartphone（RE 号纯数字、设备号 D2131001、速拨 A2131001）
9. 核验六类自动对象，手工补 Entity 识别码选择器与公网 COS 放行
10. 手机装 App（Android 装 OpenTouch Conversation、iPhone 装 Conversation Plus）填公共/私有 URL 登录

## A2 — 未来触发

使用情境：给移动员工配公司号手机；手机收不到来电/呼不出去；DISA 呼入不通；iPhone 收不到推送；GSM 倒换太慢；只有手机没有话机的用户怎么配。

语言信号：OTC Smartphone / 远程扩展 / RE / REX / DISA / 31280 / 速拨 / speed dial / ARS / 识别码 / discriminator / Tandem / APNS / kamailio-wasp / 5265 / Off site mobility / 双模。

与相邻能力区分：

- 手机注册的通道与证书 → 远程接入能力
- Ghost Z 池规划 → Nomadic 能力
- 扫码切换呼叫 → Extended Mobility 能力（路由卡）

## E — 可执行步骤

输入契约：用户类型（Connection）、手机平台（Android/iPhone）、连接模式（GSM/Wifi/双模）、号码计划余量（RE 号/速拨段/手机 E.164 号）。

1. 基座核查：ARS 前缀、DISA 前缀与 DDI 翻译、Ghost Z 池、速拨范围、溢出三参数。完成标准：OXE 侧清单全绿
2. OT 侧基座：iPhone+ SBC 声明、前缀同步、DISA 公网号与 ARS 手填项。完成标准：同步后前缀自动出现
3. 建设备档案并关联用户。完成标准：Device 页签同时列出 RE 与 OTC Smartphone
4. 授权 Off site mobility。完成标准：Licenses 页签已勾
5. 核验自动对象（RE/速拨/识别码/ARS/Tandem/SIP 设备）。完成标准：c11 六项逐一对上
6. 手工补 Entity 识别码映射与公网 COS 放行。完成标准：GSM 回退路由可拨通
7. App 安装登录与端到端测试（呼入落地、DISA 替换、GSM 倒换）。完成标准：行为测试通过

判停点：

- 公网呼入手机不通：按链路查 DDI 翻译（最常漏）、DISA 两级授权、速拨号触发替换
- RE 目录用了字母开头 → 停，A-D 开头保留给设备/速拨命名空间，改纯数字
- iPhone 推送全停 → 查防火墙四端口与 APNS 证书年度 hotfix（过期次年全停）
- 文档卡 queued 类问题不属本卡（DCS）；部署细节生产化以 TC2341 为准

输出契约：OXE/OT 两侧基座核查单 + 用户关联与自动对象核验记录 + 端到端测试结论（含 DISA 与 GSM 倒换）。

## B — 边界

- R2.6 前后"手机当主设备"语义不同：旧结构（SEPLOS 类主机+溢出）升级时要改造（n43）
- 自动创建不包办 Entity 识别码与 COS barring 两件事，漏掉即"配了但不通"（n15）
- APNS 依赖苹果云：防火墙四端口加每年证书 hotfix 是长期运维项，写进维保合同（n50）
- 实验值（31280/61/62/#0/#0306/D2131001 等）为示例口径，生产按客户号码计划替换
- 手机部署的生产化细节（Wi-Fi/VPN 话音、SIP over VPN 等）原书外置到 TC2341
