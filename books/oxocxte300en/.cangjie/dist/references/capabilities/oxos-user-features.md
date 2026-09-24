# 用户功能与语音信箱（按键 / 动态路由 / 前转 / 信箱三态）

## R — 原文依据

> "3 types of Keys are available on OXO Connect • Call keys • Feature keys • Resources keys"（p160）
> "If "apply diversion" is not ticked, all diversion, including users' forwarding (immediate, on-busy, selective…) will be disabled."（p165）
> "Standard Mailbox … Guest Mailbox … Answer Only Mailbox"（p186）
> "The password of the general mailbox is the operator password"（p189）

出处：OXOCXTE300EN p157-196（用户功能讲义与实验、语音信箱讲义与实验）。

## I — 自述

**用户功能**围绕键、权限、转移三件事：

- 键三类：呼叫键（直呼预存号）、功能键（激活功能）、资源键（multiline 专用：RGM/RSL/RSP/RSB/RSD）；默认配比按话机模式查键 profile 表（p09）
- 动态路由：久叫不应两级两计时——T1 到时转 LEVEL 1 目的地（hunt/分机/集体缩位）、T2 到时转话务台；计时上限 3276 秒、级联最多 5 级；apply diversion 是一切转移的总开关（n10）
- 能力=权限+载体两段：插入/外转等必须 Feature Rights 放行，再配键或用前缀——只建键不开权不生效（n46）
- 用户密码规则：信箱密码 4 或 6 位数字、建议 6 位；系统拒绝 000000、123456 类弱密码

**语音信箱**三态双模：

- 三态：Standard 全功能 / Guest（Hotel 客房受限界面）/ Answer Only（只应答不留信）
- 双模：APPLICATION（Message 键/前缀，不占端口）与 CONNECTED（拨端口或组号，占 1 端口走 DTMF 导览）
- 基线容量：2 接入端口、4 语言、1 小时存储、问候语至 120 秒；选配可扩端口至 8、存储 4h/30h/200h
- 特色：Message Screening（边录边听，需非默认密码）、Conversation Recorder（15 秒静音默认结束、录音默认 30 天删除）、General Mailbox（经自动话务员访问、密码=话务员密码）
- 语音文件 ADPCM 4bit 8kHz Mono 与 WAV PCM 16bit 8kHz Mono 可互转

## A1 — 书中案例

**用户功能实验**（p173-181）：

1. 直呼键：Keys → 空键，选 Resource Key → Local Call，填目标内线号
2. 遇忙前转键：Feature key → Diversion，类型 On Busy，填转移目标并命名
3. 动态路由 10 秒：Dyn. Rout → Timer1=10s → Local Calls 勾 Level 1 并填目的地
4. 选择性转移：Sel Divers → 清单 1 改 active，选 Telephone 填目标，加 2 个主叫入过滤清单
5. 热线：模拟话机 Misc → Hotline=Immediate → 目的地填话务台号 9（需物理话机）
6. 插入与防插入：授权方勾 Intrusion Allowed、经理话机勾 Intrusion Protection
7. 外转仅经理：经理勾 External Diversion，其余用户不开即禁
8. 验收：键生效、振铃 10 秒第二话机同响、清单内主叫被转、非授权无法插入

**语音信箱实验**（p190-196）：

1. 话机侧定制：按 Message 键，输默认密码（实验 142535）后设新密码（实验 142536），录姓名问候
2. Answer-only：用户 details → Mailbox，Options 页签模式选 answer only
3. 录音监听：勾 Recording of Conversation allowed，建 Conversation Rec 与 Screening 两键（Screening 须非默认密码）
4. 远程访问：公共计划加 41500→hunt 500（VM 端口组）→ 用户勾 Mailbox remote consultation
5. 删建信箱：Del Mailbox / Mailbox 按钮 → Yes
6. 验收：新密码进信箱、answer-only 不留信、外线拨 41500 远程听留言

## A2 — 未来触发

使用情境：给老板秘书配键；"用户设了前转不生效"排障；出差要远程听留言；酒店客房信箱模式；会议录音合规口径。

语言信号：可编程键 / 功能键 / 资源键 / RSL / 动态路由 / dynamic routing / 前转 / 转移 / 插入 / intrusion / 热线 / hotline / 语音信箱 / mailbox / answer only / 监听 / screening / 远程访问。

与相邻能力区分：组级业务 → 编号计划与组能力；转外线号码的可达性 → 出局闭锁域。本能力到"用户级行为符合定制"为止。

## E — 可执行步骤

输入契约：数据采集表的组与按键块、话机型号与模式、（信箱）许可范围。 multiline 资源键需求须先确认话机支持。

1. 配键：按需建呼叫/功能/资源键。完成标准：键位表与采集表一致
2. 动态路由：设 T1/T2 与两级目的地，核对 apply diversion 已勾。完成标准：久叫按预期转
3. 前转与选择性转移：配键或指导用户用前缀。完成标准：拨测生效
4. 权限配对：Intrusion/External Diversion 等按业务开权。完成标准：非授权用户实测被拒
5. 信箱初始化：改默认密码、录姓名问候、定模式。完成标准：新密码可进、模式行为正确
6. 录音监听：开权建键并验证（先改非默认密码）。完成标准：边录边听可用
7. 远程访问：公共计划加 VM DDI 入口+开用户权。完成标准：外线拨入可听留言

判停点：

- 前转不生效 → 先查 apply diversion 总开关，再查 Feature Rights 与 Sel Divers（n10/n46）
- Screening 测不了 → 用户仍是默认密码，先改密再测（n11）
- 虚课无物理话机 → 热线/监听等项如实标注"只配未验"（n09）
- 信箱容量/端口不够 → 走选配报价（端口至 8、存储至 200h），不要超配承诺

输出契约：用户配置清单（键/权限/动态路由）+ 信箱台账（模式/密码状态/远程入口）。

## B — 边界

- 实验密码（142535/142536 等）为实验口径；弱密码拒绝机制是系统行为，生产按 TC1143 策略
- 会话录音涉及当地法规合规，书外确认
- 键 profile 的 n 值（模拟线数与 B 通道）受话机键数上限约束，完整口径在 Expert 文档
- 录音 30 天删除与 15 秒静音结束为默认值，改动口径原书未展开
