# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 Windows 2019 安装章沿用旧版口径（文档未同步）

- **位置**: p639 连接信息文件名写 `C:\Users\<账户>\nmc5_5.1.cfg`（2022 章 p85/p103 为 nmc5_5.2.cfg）；p621 DNS 指向 192.168.1.100（ecosystem 虚机，2022 章为内部 DNS 192.168.1.250）；2019 章无 WMIC 附录。
- **判断**: 疑为旧版教材内容沿用（推断：文档未随版本同步）；文件名差异不影响功能，DNS 差异属实验环境编排不同。
- **处置**: 按 2019 章操作时以实际版本号与现场 DNS 为准；能力卡以 2022 章为基准、2019 章作并列参照；引用 cfg 文件名时标注两章口径。

## nr-02 OXO Connect 章法语残句（未完成翻译）

- **位置**: p643 "MAIN@: Vérifier que l'adresse IP de la Power CPU EE est : 151.1.1.246"；p659 "Renseigner le login de session Windows du serveur OmniVista 8770 (i.e. Administrator) / Renseigner le mot de passe (i.e. superuser)"。
- **判断**: 英文版 Ed47 翻译遗漏（推断），非内容差异；语义分别为"核对 MAIN@ IP"与"填 8770 服务器 Windows 会话账号/密码"。
- **处置**: 转述语义不逐字引用；同章节其他法语片段按上下文类推。

## nr-03 客户端硬件口径"剩余空间"与"内存"表述混写（原文如此）

- **位置**: p93 "OV8770 client cannot be launched if the space in the memory size is below 750 MB. It's the minimum required memory space to run JVM application"。
- **判断**: 同段先写 Free disk space 后写 memory size，属原文表述瑕疵；JVM 启动底线按"剩余磁盘空间 750MB"理解（与硬件表 RAM 4GB 并行不悖）。
- **处置**: 能力卡引用时写"剩余磁盘空间 ≥750MB（JVM 启动底线）"并标注原文表述混写。

## nr-04 缩写全称书中未展开——不得补外部全称

- **位置**: PCX（g16，仅注"Private eXchange？"存疑）、MAO（g17）、MCS 仅 p13 展开一次、TDS/GCS/DDI 等未展开。
- **判断**: 教材对部分缩写未给全称；PCX 的 "Private eXchange" 为提取器存疑标注，书内无出处。
- **处置**: 术语表如实省略或标注"未展开"；转述与能力卡不得补全称冒充书内事实。

## nr-05 含推断成分的结论（引用需带标注）

- n45: "2019 章为旧版沿用内容"——基于三处证据的推断（见 nr-01），非原书自述。
- n53: 法语残句处理方式"按上下文理解、以此类推"——语义转述含推断。
- f23/p39: OXE 侧 spadmin 锁号 39/42/47/49/50/98/99 与计费锁的对应关系——书中以清单呈现，逐号语义为提取器归纳。
- **处置**: 三条均已标"（推断）"；能力卡引用时保留推断标注，不升格为书中明示事实。

## nr-06 实验口径总提醒（全书明文凭据）

- **位置**: Superuser2580* / superuser / letacla1 / sql / pbxk1064 / Alcatel1 / Pbxnmc12 等明文凭据遍布正文（p47、p69、p642、p649、p657）。
- **判断**: 教学连贯性设计，书中自注 "password used on a classroom environment"；生产沿用等于零口令防护（n52）。
- **处置**: 环境值只进能力卡 B 边界与 book/overview；正文一律以角色名指代（目录管理器密码、installer 密码等）。
