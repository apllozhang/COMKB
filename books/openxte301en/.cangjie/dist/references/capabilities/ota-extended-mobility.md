# Extended Mobility（QR 码/NFC 标签切换呼叫与路由修改）

## R — 原文依据

> "«Extended OT mobility» allows users with Android or iPhone (*) Smartphones: To switch an established communication from OTC application to any internal deskphone (one way) • To modify the end-user's call routing profile ... (*) NFC not supported by iPhone"（p150）
> "QR Code label ... accepted by the smartphone app for audio switch on an OXE deskphone: {\"v\":\"1\",\"DI\":{\"DiD\":{\"User\":\"phone number\"}}}"（p158）
> "Since the automated scenario has been executed, there is no retrieve facility to switch back the call to smartphone"（p152）

出处：OPENXTE301EN p148-167。

## I — 自述

用贴在话机上的标签触发两个动作，无需装新 App（OTC 应用须已启动）：

1. **两个功能**：呼叫切换——把进行中的通话从 OTC 应用切到任意内部话机（单向，不可回切）；路由修改——把当前路由档案切到含 "other and mobile()"（值=目标话机号）的条目
2. **QR 语法固定**：{"v":"1","DI":{"DiD":{"User":"<OXE 目录号>"}}}，任意第三方生成器可做；例 User=31000
3. **NFC 生态**：写卡用 Google 市场 "ALE NFC Extended Mobility Administration" 工具（Android R4.2+）；推荐 ALE 标签（Ref 3BA27856AA，100 张装），自购须 NFC Type 2 且由 BP 验证
4. **周期提醒**：路由修改后每小时弹提醒——Yes 恢复原档案、No 保留并停表、Later 一小时后再弹；再扫同一标签可 toggle 停止
5. **前提与成本**：OpenTouch R2.1 MD1 起（iPhone QR 自 R2.2）；成本项为话机/手机/许可（Connection+universal connection client）+REX 资源（GhostZ/IP/DTMF）+标签，无软件增项与使用费

## A1 — 书中案例

**标签制作与两类测试**（p163-167）：

1. 前提：OTC Mobile 已装、复用智能手机实验的设备（Backman 31001，实验口径）
2. 用在线生成器按语法生成 QR（User=31000）并打印/投屏
3. NFC：装 ALE 工具，OpenTouch Deskphone 页签填 DN=31000 写入标签
4. 测试 1（切换）：Boop 呼 Backman、手机接听、扫 QR → 通话切到 Barkley 话机 31000（用户拿起话机）
5. 测试 2（路由修改）：Backman 空闲态从 Routing Profile 菜单扫同一标签 → 档案改写为 other number=31000
6. 观察：小时提醒三种应答行为；再扫一次 toggle 取消

## A2 — 未来触发

使用情境：办公室内手机通话切到座机；把"到工位就用房机"做成碰一碰体验；售前算 Extended Mobility 的许可与资源成本；提醒弹窗行为解释。

语言信号：Extended Mobility / QR 码 / NFC / 标签 / 切换 / switch / 碰一碰 / 路由档案 / routing profile / other and mobile() / 周期提醒 / 3BA27856AA / NFC Type 2。

与相邻能力区分：手机基础交付（关联/授权）→ 智能手机能力；nomadic 离开办公室场景 → Nomadic 能力；本卡只管办公室内标签触发。

## E — 可执行步骤

输入契约：标签覆盖的话机清单（目录号）、手机平台（NFC 仅 Android）、OTC 应用版本、标签采购渠道。

1. 生成标签：QR 按固定 JSON 语法；NFC 用官方工具写卡。完成标准：标签内容可读且目录号正确
2. 现场张贴并验证切换：手机通话中扫码/碰标签 → 话机响铃接续。完成标准：通话延续、手机释放
3. 验证路由修改与提醒行为（空闲态执行）。完成标准：档案改写与小时提醒符合预期
4. 用户教育：单向不可回切、应用须已启动、NFC 仅 Android、拿起话机保私密。完成标准：培训完成

判停点：

- 客户要求"能从话机切回手机" → 机制不支持（单向），需求改道或升级
- 扫码后铃在别处 → 目标话机配了立即呼转，切换跟呼转走；演示前先清呼转（n16）
- 杀掉后台后标签无效 → 触发靠 OTC 应用，应用必须已启动（n17）
- 自购 NFC 标签 → 须 NFC Type 2 且由 BP 验证，否则兼容性自担

输出契约：标签清单（话机号对应表）+ 两类测试记录 + 用户教育材料要点。

## B — 边界

- 切换底层是"二通呼叫+转移"自动场景，执行后无回切；路由修改仅限空闲态（n41）
- 支持话机范围广（ALE-x/80x8/8001/DECT/模拟/4135 等，p157）但具体型号兼容以现场验证为准
- 教室 6 SSID 热点与学员自带手机为实验前提，生产需现场勘测替代（BOOK_OVERVIEW 批判节）
- 无容量与使用费口径之外的商务条款（p161 成本清单为许可+资源口径）
