# OTC 智能手机开通（Connection 用户、自动对象、R2.6 单设备、编号与 DISA/ARS 联动）

## R — 原文依据

> "OXE configuration principle is complex and specially for Wifi/dual mode: up to 9 objects have to be managed"（p178）
> "Automatic configuration of these objects when a Smartphone is associated to a Connection user in order to simplify administrator tasks"（p180）
> "Remote extension directory…: Enter a number for the remote extension created in OXE (e.g. 2131001). Do NOT use a number beginning with letter (A,B,C,D) in the directory number of the Remote Extension!"（p202）
> "Now, from release 2.6 of OpenTouch, the main device can be directly the remote extension"（p204）

出处：OPENXTE225EN p178-182, p189-217。

## I — 自述

智能手机移动化全部按 Connection 用户展开（SIP 走 OXE），主线是"先配系统参数，关联一次自动建对象，再补两处手工"：

1. **OXE 通用参数九项**（双模式口径）：

   - 专用 ARS 前缀；RE DISA 前缀（必须核对进 DDI 翻译表）；自动替代 Without code
   - 中继组允许 DISA；RE 参数（DTMF 序列）；RE 激活/去激活前缀（61/62）
   - Ghost Z 池（特性选 Remote Extension，一个 RE 一个 ghost 更稳）
   - 直连速拨号范围（不能为 0、不能满）；溢出定时器（INVITE 重传 2-3、T310=60）
2. **OT 侧参数**：OXE CS 前缀同步、RE DISA 公共号码与 ARS 前缀、判别器号、公网区号、中继组 ID、ARS Route list MAX ID（默认 3999，每手机一张表）
3. **关联**：Users 应用右键 Associate SIP device，New OTC Smartphone；授 Off-site mobility 许可

自动对象×模式矩阵（p181，V=自动创建）：

| 对象 | Mobile only | WiFi only | Dual | Dual（指定 GSM 号） |
|---|---|---|---|---|
| 远程分机 RE | V | V | V | V |
| Tandem（twinset） | V | V | V | V |
| 直连速拨号 | — | — | V | V |
| SIP 设备 | — | V | V | V |
| 判别器规则 | — | — | — | V |
| ARS 路由三件 | — | — | — | V |

编号前缀四则（p194/p201-202/p207）：RE 目录号严禁字母开头（A/B/C/D）；手机设备号用 D 前缀（实验口径 D2131001）；速拨号用 A 前缀（A2131001，自动替代用）；Ghost Z 可用 B<数字> 占位。混用会破坏自动替代与 tandem 关联。

R2.6 版本分界（p182/p204）：此前"只有手机"的用户要配永不入服的 SIP 主设备 + 溢出；R2.6 起远程分机直接做唯一设备——配置简化、修复主设备离线呼转问题、凭 RE 回调可进 OT 会议。

双模式呼手机的两道手工关卡（p212，自动对象建完仍必查）：用户 Entity 的判别器选择器把逻辑判别器关联到智能手机专用物理判别器；判别器指定的公网接入 COS 区域必须对该用户手机号放行（barring）。

## A1 — 书中案例

双模式开通主线（p189-212，实验口径号码见 book/overview）：

1. OXE 侧按九项清单配通用参数，RE DISA 前缀核对 DDI 翻译表
2. OT 侧执行 OXE CS prefixes synchro，填 RE DISA 公共号码与 ARS 前缀等
3. （可选）建 OTC Smartphone 设备档案：类型、连接性、SBC WAN、回落开关
4. Users 应用选用户，Associate SIP device，General 页填设备号（D 前缀）与 GSM 号
5. OXE CS 页填远程分机号（禁字母开头）与速拨号（A 前缀）
6. OT configuration 的 Licenses 勾 Off-site mobility
7. 按 p207-211 逐项核验自动对象：RE、速拨号、Tandem、SIP 设备、判别器、ARS 表
8. 手工补两处：Entity 判别器关联（物理判别器选专用值）、公网接入 COS 区域授权
9. 核验 ARS：Route 1=SIP 设备号、Route 2=公网中继呼手机、时间表 1&2 同时启用

单设备场景（R2.6，p204-206）：建用户时 Device type 直接选 Remote extension，关联手机时远程分机号与主号一致，其余核验与授权同上；App 安装后首启填公共/私有服务器地址（转客户端接入能力）。

## A2 — 未来触发

使用情境：给用户配工作手机；"只有手机没有话机"的开户；双模式倒换到 GSM 呼不通；RE 呼入显示陌生手机号（自动替代没生效）；从 R2.5 升级 R2.6 后的配法选型。

语言信号：Connection 用户 / OTC Smartphone / 远程分机 / remote extension / RE / tandem / twinset / DISA / DDI / ARS / 判别器 / discriminator / barring / 自动替代 / D2131001 / A2131001 / R2.6 / 单设备 / Off-site mobility。

与相邻能力区分：

- iPhone 推送与 5265 端口 → iPhone APNS 能力
- 手机上功能形态（回落/无 SIM）→ 智能手机模式能力
- App 首启填 URL → 客户端接入能力
- 游牧 PC → OTC PC 两模式能力

## E — 可执行步骤

输入契约：用户主号与手机号（规范格式）、连接模式（Mobile/WiFi/Dual）、系统版本（是否 R2.6+）、OXE 侧九项参数现状。

1. 按 p181 矩阵定模式，双模式确认用户已有主话机（twinset 结构）。完成标准：模式与对象清单对齐
2. OXE 侧九项通用参数逐项落地，RE DISA 前缀核对 DDI 翻译表。完成标准：九项有核对记录（n19）
3. OT 侧前缀同步并填 RE DISA 公共号码、ARS 前缀、判别器号等。完成标准：Telephony settings 保存生效
4. （可选）建设备档案统一网络与回落参数。完成标准：后续关联时能引用该档案
5. 关联手机：设备号 D 前缀、远程分机号纯数字、速拨号 A 前缀。完成标准：Device 页签出现 RE 与速拨号（nr-08）
6. 授 Off-site mobility 许可。完成标准：Licenses 页勾选生效
7. 自动对象六组逐项核验（RE/速拨号/Tandem/SIP 设备/判别器/ARS）。完成标准：与 p207-211 清单逐项对上
8. 手工核 Entity 判别器关联与公网接入 COS 区域授权。完成标准：两处 Warning 关卡有核验记录（n22）
9. R2.6 单设备：Device type 直接选 Remote extension，跳过旧法假主设备；R2.5 及以前按旧配法（n16）

判停点：

- 双模式呼手机失败 → 停，按两道关卡查：判别器逻辑→物理关联、COS 区域授权（n22）
- RE 呼入主叫显示不对 → 停，查速拨号（A 前缀）与自动替代系统参数（Without code）
- 版本低于 R2.6 却想用单设备配法 → 停，按版本分界走旧配法（n16）
- 客户问每用户带宽/并发容量 → 停，书内无数值（nr-07）

输出契约：开通完成的智能手机用户（模式与对象核验记录）+ 两处手工关卡核验结论 + 版本配法说明。

## B — 边界

- "自动配置"不等于零手工：判别器关联与 COS 区域授权两步必须人工核（n34）
- 直连速拨号范围不能为 0、也不能配满（n20）；编号前缀四则不可混用（n21）
- Android 无 SIM 纯 VoIP 模式下回落、私人呼叫、短信三项全部不可用（n23，详见智能手机模式能力）
- 实验号码（31280、#0306、D/A 前缀示例等）为实验口径，见 book/overview；生产按客户编号计划替换
- 完整手工配置清单与生产化细节以 TC2639、TC2341en 为准（书内明示外置）
