# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 RTR 失败后的重试/扣减双口径（教材内部不一致）

- **位置**: p308（讲义 Miscellaneous）："OXE will retry the Right To Run check up for four hours with interval of ten minutes … If the connection is not restored at end of the fourth hour • OXE will decrement the qualifying period by one" vs p332（How-To Notes）："If a problem occurs when RTR request is sent, no retry is performed until next daily request and one day is decreased from remaining qualifying period"。
- **差异**: 一个说 4 小时窗口内每 10 分钟重试、4 小时后才扣 1 天；另一个说当天不再重试、（请求出问题时）当天即扣 1 天。
- **影响**: 监控告警阈值与客户沟通口径——"断连多久会扣资格期"两页答案不同。
- **处置**: 不强行统一（candidate p22/n35 已双记）。能力卡按保守口径表述（按当日即可能扣减做监控），并注明"具体行为以 ALE 最新 TC/发布说明为准"。

## nr-02 p404 Voice Agent(CCD) 计数示例排版错误

- **位置**: p404，计数示例 "13 | 2/2 | 18" 下方的解释文字误用了 5/5/25。
- **判断**: 同页其他条目与 p397 的四列读法均自洽，该处属复制粘贴级编辑错误。
- **处置**: 判据以 p397 原文为准（第一列=全网可新申请、中间两列=lms/oxe 两侧消耗且必须一致、末列=全网订阅上限）；示例数值不照抄。candidate n56 已记录。

## nr-03 SOT 媒体传输通道两章表述差异

- **位置**: p86（Standalone 章）："you have to establish a FTP or SFTP (port 2222) session … Login: upload"；hosted/ESXi 各章（p192、c09/c10/c11）仅写 "FTP"。
- **差异**: 一处给全协议与端口，其余章节表述粒度收窄；功能等价（同为向 SOT 传媒体）。
- **处置**: 能力卡统一按 p86 口径表述（FTP 或 SFTP 2222、upload 账号，实验口径），引用 hosted 章节时不再重复端口。

## nr-04 GAS 迁移文档件号为未定编号占位（原文如此）

- **位置**: p230 "« TC0000_GAS_migration_FR_ed04.docx »"。
- **判断**: TC0000 为文档编号占位（正式 TC 号未编或书未更新），同页其他指针（TC3138、TBE063）编号齐全。
- **处置**: 引用时保留原样并注明"占位件号，原文如此"；检索时改按文档标题 "GAS migration" 查 MyPortal。

## nr-05 实验凭证遍布正文（引用纪律）

- **位置**: 全书——Superuser2580*（OXE/SOT 四账户）、letacla/letacla1（SOT/GAS/OMS 出厂默认）、rainbow/Rainbow123（WebRTC VM）、ESXi root/Superuser-X*、192.168.1.x 全网段（p10-19、p43、p91、p175、p272-273 等）。
- **判断**: 培训教材性质所致，非安全建议；原书自身在 aging=0 处引用 CIS_Benchmark_Req.No_5.6.1.1 警告（p91/p175/p273）。
- **处置**: 一切 IP/账号/密码只进能力卡 Boundary 段与 book/overview 环境区，标注"实验口径"；操作正文一律用占位写法（如 <OXE-IP>、<账户口令>），不把实验值当生产配置。

## nr-06 "云服务不跑备机/PCS"与"lmsagent 跑全部 CS"双规则辨析

- **位置**: p297 "Cloud Services DO NOT run on Passive Communication Server (PCS)" + p329 "THERE IS NO NEED TO PERFORM FTR ON STANDBY CPU" vs p353 "Run in all Call Servers : main, stand by, PCS • Read only access on Stand-by CS"。
- **判断**: 非矛盾——两条规则对象不同（CC 云服务 vs OPEX 的 lmsagent），但字面看似打架，是最易误读点。
- **处置**: 两条规则在能力卡中成对出现并显式分域：排 FTR/RTR 问题看主机；排 OPEX 许可问题看备机 lmsagent 状态是合理的（只读）。
