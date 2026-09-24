# 语音邮箱 profile 定制与问候语管理（默认模板/批控参数/Greeting Managers）

## R — 原文依据

> "Profiles called 'Advanced', 'Classic' and 'Simplified', dedicated to Local Storage. 'Standard' profile is dedicated to Unified Messaging."（p147）
> "Attendant call enabled: If enabled, the caller can decide to be routed to an attendant by dialing digit '0' while the greetings are played (also known as zero-out enabled)"（p149）
> "Solution : Greetings Management Web Interface for Administrators / Greeting Managers"（p128）

出处：OTMCXTE200EN p121-132, p142-152（c08、f17/f18、p14/p15、c07 步骤 12 归并）。

## I — 自述

profile 是管理员"成池批控"信箱行为/容量/期限的模板；问候语是用户侧的听感层。两者合起来构成信箱的策略面。

**默认四 profile**：Advanced / Classic / Simplified（LS 专用）+ Standard（UM 专用）；可自建。

**profile 三张配置页**：

| 页签 | 管什么 | 代表参数 |
|---|---|---|
| Configuration 1 | 行为 | Answer only（默认 Manageable by users）、Check quota、Direct callback、Limited access、Propose options after message deposit（录后 1 确认/2 复听/3 重录/0 求助）、Attendant call（zero-out，问候中按 0 转话务台） |
| Configuration 2 | 时长与密码 | Maximum greeting / Max message recording / Max live record（秒）；TUI password management 三档（allowed / allowed but forbidden when expired / forbidden） |
| Configuration 3 | 容量与期限 | Max size per mailbox（Check quota 关闭时不生效）、Aging of new/saved messages（天）、Warning、Accessible via network / Accessible via IMAP |

**问候语四类**：standard（姓名或分机号）、personal（内外线可不同）、absence（长期离开）、alternative personal（最多 2 条、须管理员授权）。

**管理三入口**：管理员 Greeting Managers 网页（上传/激活/下载/删除，数量不设上限）、8770 侧信箱 Greetings 页签、用户 TUI 或 My Profile 自助。

## A1 — 书中案例

**profile 查看与新建 + 问候语集中管理**（c08 + c07 步骤 12）：

1. 查默认 profile：System services/Applications/Messaging/Voice Mail Profile 应见四个默认
2. 逐页签研读 Advanced，形成客户参数地图（默认值含 Answer only=Manageable by users、录音提示音默认开）
3. 新建 profile（local storage 型）：勾行为项、定三时长、定容量与保留天数（书中示例 my_profile：10MB、5s/15s/15s、15 天/7 天，实验口径）
4. 分配：Users and Devices/Voice Mail Box 选信箱，Configuration 页签选新 profile
5. 行为验证：向该信箱收几条留言，核对参数按预期生效（p151 验收要求）
6. 问候语集中管理：8770 选 OT 节点右键 WBM（otAdmin 登录）进入 Voice mail greetings management（再认证一次）
7. 选用户执行 Upload/Activate/Download/Delete；替代问候需先在信箱 Greetings 页签授权

## A2 — 未来触发

使用情境：按部门/岗位差异化信箱容量与保留期；"信箱满了自动删旧的行不行"；关掉"留言后按 1 确认"；zero-out 转话务台；给高管换专业问候语。

语言信号：profile / 批控 / 模板 / Answer only / zero-out / Check quota / 配额 / 保留天数 / aging / TUI 密码策略 / 问候语 / greeting / Greeting Managers / alternative。

与相邻能力区分：建账户与信箱本体归 otmsg-user-mailbox-provisioning；用户自己在网页激活问候见 otmsg-web-portal（路由卡）；通知阈值归 otmsg-notification-smtp-sms。

## E — 可执行步骤

输入契约：信箱已建（转 otmsg-user-mailbox-provisioning）、客户的容量/期限/行为策略清单。

1. 出参数地图：对照三页签逐项与客户确认取值。完成标准：策略表确认
2. 建 profile：类型按信箱存储选（LS 用前三默认的同类，UM 用 Standard 口径）。完成标准：profile 出现在可选列表
3. 分配并验证：挂到目标信箱，收留言核对参数。完成标准：行为符合预期
4. 问候语交付：Greeting Managers 上传/激活；按需授权 alternative。完成标准：问候生效
5. 变更管理：改 profile 即对挂接信箱批量生效，记录版本与时间。完成标准：变更可追溯

判停点：

- 配额没生效 → Check quota 未开（关闭时 Max size per mailbox 不生效，p150）
- 用户要"不同部门不同欢迎语/多套轮换" → 单 profile 是批控模板、general announcement 全局仅一条——差异化走多 profile 或问候语授权，需求先谈清（n20）
- 用户 My Profile 里 TUI 密码档位回落 → 无信箱或无 profile 的用户固定回落 "allowed but forbidden when expired"（p149-150），先补对象再看档位

输出契约：客户策略 profile（已分配）+ 问候语授权与激活记录 + 行为验证结论。

## B — 边界

- TUI 密码策略五参数（最小长度/历史/有效期/最大失败/锁定时长）默认值在 feature list（书外），本书只给参数名（p24）
- 问候语管理细节外指 Quick Reference Guide "Managing your welcome greetings message" 章（p142）；专业录音 wav 来自录音棚产线（p128 图示，制作在书外）
- my_profile 数值为实验口径，生产按客户策略
- UM 型 profile（Standard）的落地配置不在本书——UM 仅支持性声明（n28）
- 实验示例值（my_profile 参数、otAdmin 口令）见 book/overview
