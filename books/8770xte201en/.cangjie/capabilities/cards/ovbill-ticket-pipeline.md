# 计费票据管道（OXE 出票、维护命令、回收五方法、加载过滤、入库验证）

## R — 原文依据

> "Accounting records storage (max 500 records)"（p62）
> "This number defines the maximum of accounting files that can be saved on the PCX: default value 31 days i.e. 31 x 24 files = 744 compressed files."（p86）
> "Comparison of the ACCOUNT.LIS files ... Retrieval (via ftp) of the new files ... Records extraction and loading in the database ... Deletion of the retrieved files ... Update of the file"（p98）
> "Important: Modify the password to match the OmniPCX Enterprise password if it has been modified. Do not modify the FTP user to avoid a problem at verification of the license."（p109）

出处：8770XTE201EN p59-114, p448。

## I — 自述

票据数据链是单向管道，任何一环断开都会表现为"8770 里没票"，按段排查：

- OXE 出票：呼叫结束生成票据（ED5.2 版式最长 47 字段）先进内存缓冲（≤500 条）；落盘三时机——缓冲满、90 分钟无新票、account compress 强制（节点同步也触发）；文件落 /usr4/account（TAX*****.DAT + ACCOUNT.LIS）
- 出票边界两条：外线呼出/呼入未接通（时长=0）也出票，所以有 "Public Outgoing 0 Units calls" 类别；本机-本机只有已建立才出票
- OXE 侧开启：Files for External Accounting=Yes、存储上限默认 31 天（=744 个压缩文件）、过滤器选齐呼叫类型且必选 0 计费呼出；Financial Report 页签 PIN=Not masked、被叫遮蔽位数=0（遮蔽归 8770 管）
- 回收四步：先对比两侧 ACCOUNT.LIS，再 FTP 取回新 DAT 到 C:\8770\data\loader\networknumber=N\subnetworknodenumber=NNN，随后提取记录过加载过滤入库（成本在此步计算），最后删远端文件并更新本地索引
- 五种计费方法按 PCX 各选一：No accounting / Detailed（默认推荐：更新树+取票按分机归位）/ Organization update without records retrieval（建树期用）/ Global per node 两种（聚合实体键=网络号×1000000+节点号）
- FTP 铁律：用户名 adfexc 禁改（许可校验），密码必须与 OXE 一致并随 OXE 改密同步更新
- 加载过滤五道闸：Duration 阈值、Cost 阈值、Communication Type、Call type（勾 Network 才存内线与 OXE 间呼叫）、Charged party node（取消 Undeclared 防未声明节点入库）
- 排障入口：NMCLD_1.log 看 TicketsRead/BadLines/处理速度/被过滤数；PCS 场景票据带 PCS ID（IP 的十六进制）后缀

## A1 — 书中案例

**OXE 侧外部计费开启与维护核查**（p85-95）：

1. Applications > 1 > Accounting > 1：All 页签 Internal/External Accounting 均 Yes，先 Apply 再进后续页签
2. Max No. Days of Storage 保持 31（744 个压缩文件）；过滤器勾齐各呼叫类型并必选 Public Outgoing 0 Units calls
3. 右键过滤条目 Add After 加 PCX PCX Calls；Financial Report 页签 PIN=Not masked、被叫遮蔽位数=0
4. 成本中心命名 1=MKT、2=Training、3=TSS（槽位默认已建）；用户 Rights 页签分配 Cost Center ID
5. SSH 登录 mtcl 执行 account compress 强制落盘；cd /usr4/account 后 more ACCOUNT.LIS、ll *.DAT
6. accview -mtf <文件> 逐字段查票据（-b 10 / -e 10 看头尾 10 条）

**8770 侧回收与验证**（p108-114）：

1. PCX 页签：FTP=adfexc + 与 OXE 一致的密码；Accounting Process=Detailed accounting
2. Data Collection 页签：Record/ticket collection=Accounting（默认 None）；收集器目录 c:\8770\data\collector
3. Loading > Accounting 设五道过滤闸（Duration>0、Cost、类型勾选、节点去 Undeclared）
4. 确认 loader 与 collector 目录为空后执行同步，复查两目录出现文件
5. 打开 loader\networknumber=1\subnetworknodenumber=101\ACCOUNT.LIS；看 NMCLD_1.log：TicketsRead=9、52 tic/sec（实验口径）

## A2 — 未来触发

使用情境：8770 收不到话单；票据有没有入库；没打通为什么也有记录；漏选 0 计费呼出；OXE 改密后回收静默失败；建树期该选哪种计费方法；把票据转给第三方计费软件（收集器）；PCS 站点回收。

语言信号：TAX / ACCOUNT.LIS / ticket / 话单 / 话务票据 / account compress / accview / adfexc / loader / collector。

补充信号：Detailed accounting / 加载过滤 / loading filter / TicketsRead / NMCLD / PCS / Ticket collector / 0 Units。

与相邻能力区分：节点接不上 → OXE 纳管能力；入库后算钱错 → 资费建模能力；只建树不取票的排期原则见本卡 A1 与 B。

## E — 可执行步骤

输入契约：OXE 已纳管（节点声明完成）、维护账号可用。节点不通 → 先回 OXE 纳管能力。

1. OXE 开外部计费：All 页签双 Yes 并 Apply，过滤器选齐类型（含 0 计费呼出）。完成标准：配置保存且类型清单完整
2. 配成本中心并把用户 Rights 页签挂号。完成标准：每用户有成本中心
3. 打测试呼叫后 account compress，accview 验票。完成标准：/usr4/account 出现新 DAT 且字段可见
4. 8770 PCX 页签配 FTP（adfexc/与 OXE 一致）与 Detailed accounting。完成标准：参数落盘
5. Data collection 选 Accounting；PCS 场景核对 NmcArchive > Accounting > Specific 开关。完成标准：回收通道打开
6. 设五道加载过滤闸。完成标准：阈值与勾选符合业务口径
7. 同步并验证：loader 目录、组织树 Records 页签、NMCLD_1.log 三点核对。完成标准：TicketsRead 大于 0 且树中可见

判停点：

- 目录不动、日志无新文件 → 查 FTP 密码是否与 OXE 一致（用户名禁改），不重装服务
- 票量比通话量多 → 先解释"未接通外线也出票"是设计行为，再用 Duration>0 过滤
- 8770 里被叫号是一串横杠 → 查 OXE 侧 Dialed number masked 与 Financial Report 遮蔽参数，8770 侧无法还原
- 关了 PCS 随日同步 → 必须手工同步 PCS，否则无自动回收

输出契约：管道各段状态清单（出票/落盘/取回/加载/入库）+ 日志关键行摘录 + 过滤参数表。

## B — 边界

- "没打通也有话单"与"内线只有接通才有票"是并存的出票规则（p67/p68），完整话务画像要看流量分析
- FTP 用户名改动会触发许可校验故障（p109/p448 Important，两章重复）；示例密码与实验环境不一致（见 needs-review nr-06），以"与 OXE 一致"为准
- 加载过滤发生在入库前，被过滤的票不入库也不可恢复（p110-111）
- 建树期选 Organization update without records retrieval，树定型后再切 Detailed——库里有记录再搬条目极耗时（p101）
- 组织树搭建与历史归属属组织成本归属能力；票据进库后的计价属资费建模能力
