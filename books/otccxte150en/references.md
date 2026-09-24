# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| Feature List（原书 p18 指针） | ACR 容量与特性细则的权威口径（容量表仅给上限，细则查此） | p18 |
| CCD09001-CCD09013 底层 How-To 文档 | 20 个实验章的原始文档编号（CCD09001CB01/02 至 CCD09013CB01-05），跨发布物追溯用 | 各 How-To 章页眉（g55） |
| Installation procedure（外部 ASM 随软件文档） | 外部 ASM 硬件/软件需求与安装细节 | p323 |
| OXE/OTCC 侧配套文档（CCD 基础课程 CCD09001 系、OMF 配置手册） | CCD 矩阵与 OMF 操作的前置知识（原书假设读者已修） | 页眉 CCD09001 编号、BOOK_OVERVIEW 假设节 |
| MS SQL Server 2016 / Access 2016 / SSMS 17 官方文档 | 数据库安装与界面操作的权威来源（原书截图步骤的宿主产品文档） | p396-469 各 How-To |
| OPS 软件许可 N°167 "ACR data base read" | 外部库读/写许可；adm_acd 选项 61 核可用性 | p320, p376, p394 |

## 2. 官方工具与维护入口

| 工具 | 用途 | 书内位置 |
|---|---|---|
| adm_acd <ASM IP> -salb | ACR 命令行仪表盘（24 名单/25 内部库/28 呼叫动态数据/11 链路/14 连接类型/60 DB 连接/61 许可锁） | p45, p60, p141, p276, p339-343, p394 |
| hybvisu -f all | 混合链路状态校验（两 access 均须 up） | p35 |
| dhs3_init -R MAIN_AFE | 重启 AFE 进程（parameters.cfg 变更后必做） | p49, p264, p345 |
| ps -edf \| grep alb | 核查内部 ASM（alb）进程是否存活/已停 | p45, p345 |
| ASM Script Editor 内 Debugger | 脚本逐构件跟踪/改条件/发起测试呼叫 | p46, p59, p338 |
| SQL Server Profiler 17 | 数据库侧观测存储过程调用（LoginName 过滤） | p467-469 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g55（55 条）全部通过术语核验（BOOK_OVERVIEW 术语表 15 行逐条映射无遗漏，详见 glossary.md 收尾自检）。
- 落位口径：GLOSSARY.md 全量收录（按 concept/role/subscription/product/protocol/resource 六类分组）；阶段 3 生成 `book/glossary.md` 门户版（精选高频 30 条左右，保持第一本版式）。
- 仅 passing 提及未单列的词（MAO、GD (2-0)、MLE、RSI、csm、Speed dialing）已在 glossary.md 收尾自检备查，附于相关条目，不进主表；subscription 类仅许可 N°167 一条（本书无订阅体系，不虚构）。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- 实验矩阵编号（3x 的 x 为讲师给定位数）：普通链路 Pilot 3x600 + 队列 3x999700 + 坐席处理组 3x999800；ACR 链路 ACR Pilot 3x603 + 等待房间 3x999703；统计 Pilot 3x650（车险）/3x651（家险）/31652/31653；直拨 Pilot 31604、私有号 31001、转移目标 31010；重定向队列 31999702 + Voice Guide 处理组 31999802 + 引导 710；IAA 接入 31900/31888；坐席 31500/31501/31502；话机 3x000-3x002/3x500/3x501/3x502（p22 备注中 "3X800" 为笔误，见 nr-02）。
- 外部 ASM 双机（实验口径）：主 10.2.T.20/SoftPanel（Main）、备 10.2.T.21/SoftPanel2（Stand-By）；脚本目录 C:\Program Files (x86)\Alcatel\Agent Selector Module\Script。
- 外部数据库（实验口径）：Access 库 acr.accdb/表 Records；SQL Server 库 acr_sql/表 Customer（Caller 主键、Last_Agent 默认 NoAgent、Name 默认 NoName、VIP 默认 0）；SQL 登录 Brest/alcatel（关闭密码策略）；sa 口令 Alcatel@1 为安装时自定义；存储过程源 D:\CCD_ACR\SQL Call Procedure.txt；SQL Server 主机 SOFTPANEL（DSN 实验值 151.2.1.20）。
- 安全提示：以上全部口令/账号/IP 为实验口径，生产必须换强口令、最小授权、凭据不进明文脚本（原书安全话题缺席，n50，整改方向为推断）。
