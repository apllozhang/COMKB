# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 user2 邮箱跨章姓名不一致（原文如此）

- **位置**: p64 账户实验登记 "Last name: Rains / First name: Robby"，p216 4059 实验又要求 "Name: Betty / Firstname: Carol"，同一邮箱 cCpP.user2@ale-training.com。
- **判断**: 书内未解释；推断为不同 lab 的示例人物沿用同一邮箱模板（候选 n26 已标注推断属性）。
- **处置**: 照书逐字复现会在第二次建号时撞邮箱/改名困惑；实操按自己 POD 的实际状态建或复用即可，勿把姓名当考核点。能力卡引用时保留"（原文如此）"。

## nr-02 维护命令名 OCR 变体：invisu vs incvisu

- **位置**: p26 引文 "Use 'invisu' command"；c04 步骤、p87 incvisu 输出与其余各处均为 incvisu。
- **判断**: 同一命令的 OCR 变体，以 incvisu 为准。
- **处置**: 能力卡统一写 incvisu；引用 p26 原句时标注"原文如此"。

## nr-03 OXE 版本号双轨口径并存（非矛盾）

- **位置**: 网关前提 "Require OXE release 12.1 MD4, 12.2 or later"（p135）vs sizing 工具适用 "Available from OXE 101.0 MD3 and WebRTC 3.x"（p151）。
- **差异**: 12.x 与 101.x 属 ALE 新旧两套版本命名体系（Ed12 生态与 101.x 新版号），语义均为"对应功能自该版本起可用"。
- **处置**: 不作统一改写；能力卡引用时保留原文版本号与出处页码，跨版本交付以 TC2462 最新版复核。

## nr-04 RCC 呼纯 Rainbow 用户可行性为推断

- **位置**: p92-93 RCC 五项测试以 "Is it possible?" 呈现，书内未给答案。
- **判断**: "RCC 用户呼叫纯 Rainbow 用户不通"为机制推断（无网关即无音频通路），候选与本书验证均标注推断。
- **处置**: 能力卡引用时保留"（推断）"标注，不升格为书中明示事实；现场用 c05 第五项测试实测确认。

## nr-05 Teams 章内容两段重复（结构性冗余）

- **位置**: p259-269 与 p274-284 讲的是同一套架构与终端体验（讲解义与复习稿并存），p264-266 四条呼叫流亦在重复段再现。
- **处置**: 下游引用以 p258-273 为主、p274-284 作对照；不视为两套不同机制。

## nr-06 原文笔误三处（引用时注意）

- p52 "they allow to to distribute information"（to 重复）。
- p24 "a price-perminute/per-connection"（perminute 缺空格/连字符）。
- c02 引文 "XE 虚机已恢复软件许可"（应为 OXE，提取截断）。
- **处置**: 原文引用保留并注明；转述时用正确拼写。

## nr-07 实验账号命名口径（模板复用说明）

- **位置**: 实验正文账号均为 cCpP.admin / cCpP.user1 / cCpP.user2@ale-training.com（C=班号、P=POD 号），密码 Superuser-P* / PasswordP*。
- **判断**: 泛型命名法，非固定账号；具体值随班次/POD 变化。
- **处置**: 能力卡正文不引用具体实验账号，统一写"培训管理员账号（实验口径）"；完整环境值仅进 book/overview 环境区与各卡 Boundary。
