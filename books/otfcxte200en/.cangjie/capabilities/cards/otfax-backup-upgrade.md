# OTFC 备份、恢复、升级与传真删除策略（三数据域、停服语义、五步升级法、零保留）

## R — 原文依据

> "Backups cannot be performed live … All fax server services (including MySQL) must be stopped (not killed) before backing up."（p216）
> "Make copies of OTFC Data folders … the Data folder • The Bin folder • The Config folder … Export the HKEY_LOCAL_MACHINE\SOFTWARE\Interstar Technologies key from Regedit to a .reg file"（p218）
> "1.Make sure the system is sane 2.Stop traffic 3.Stop services 4.Backup the data 5.Upgrade the system"（p222）
> "There are two types of fax elements that can be deleted, either separately or together: • The fax records … • The fax documents, corresponding to the fax image files stored in the Mediastore folder"（p223）

出处：OTFCXTE200EN p216-224（含 How-To 实验 8）、p230-232。

## I — 自述

灾难底线四件事：

1. **备份三数据域**：配置与状态（注册表 + Config/Data 文件夹 + MySQL）；传真元数据（MySQL 库）；传真图像与文档（Data\MediaStore）。备份动作口诀：停服（xmsc -oa）、拷 Data/Bin/Config、拷 MySQL 数据目录、导出 Interstar Technologies 注册表键、恢复运行（xmsc -aa）
2. **停服语义差**：备份前服务必须正常停止（not killed，留状态落盘）；恢复前服务停止（can be killed，数据反正被覆盖）；备份不能热备，约维护窗口
3. **恢复四前提**：环境与备份时相似、版本等同、拓扑一致、数据回灌到与原安装相同的文件系统路径；恢复前先擦除现有数据；用户私人电话本不在系统备份内（AppData\Roaming\Fax\PhoneBook，用户自备）
4. **升级五步法**：确认系统健康、停流量、停服务、备份数据、执行升级；善后四口径——升级自动备份被改的状态文件但 CompanyConfig/XmediusArchive 两个数据库除外（升级前手工备库）、Web 包 xmedius.war 整包替换（自定义界面改动要重做）、自定义工具先在测试系统验证、新第三方软件装新禁旧但保留在盘上
5. **删除策略**：传真记录（归档库元数据）与传真文档（Mediastore 图像文件）可分开或一起删，支持零保留合规

## A1 — 书中案例

**OTFC 备份与恢复**（p230-232，实验 8，路径实验口径）：

1. 管理界面确认全组件 Active 后，Bin\Util 执行 xmsc -oa 停全部传真服务
2. 停 mysql5 服务
3. 拷贝 FaxCenter 目录下 Data、Bin、Config 三文件夹
4. 拷贝 C:\Program Files\MySQL\MySQL Server 8.0\Data 数据库目录
5. regedit 导出 HKEY_LOCAL_MACHINE\SOFTWARE\Interstar Technologies 键为 .reg 文件
6. xmsc -aa 恢复传真服务
7. 恢复演练按同序停服，回灌三文件夹与 MySQL 目录，按需导入 .reg，再 xmsc -aa 与启动 mysql5

## A2 — 未来触发

使用情境：换服务器/重装系统前；版本升级窗口；客户合规要求数据零保留；磁盘满了清历史传真；恢复演练；升级后 Web 界面自定义丢了。

语言信号：备份 / backup / 恢复 / restore / MediaStore / MySQL / mysql5 / 注册表 / Interstar Technologies / .reg / 冷备 / 停机窗口。

语言信号（续）：升级 / upgrade / xmedius.war / CompanyConfig / XmediusArchive / 删除策略 / deletion / 零保留 / zero retention / GDPR。

与相邻能力区分：升级前的服务健康检查与日志 → 服务运维能力；停流量涉及的 OXE 话路 → SIP 通道集成能力；删除策略的合规条款解读在书外。

## E — 可执行步骤

输入契约：维护窗口（停机）、备份存储介质、目标恢复环境规格（版本/拓扑/路径）、升级包与 Release Notes（书外）、合规保留要求。

1. 预检：System Monitor ➤ Services Status 全组件 Active；确认无进行中传真作业。完成标准：系统健康可进窗口
2. 冷备：xmsc -oa 停全部传真服务（等待正常退出，禁 taskkill）→ 停 mysql5。完成标准：两类服务均为"已停止"
3. 拷数据：Data/Bin/Config 三文件夹 + MySQL 数据目录 + 导出 Interstar Technologies 注册表键。完成标准：三类备份物落盘并校验
4. 恢复运行：xmsc -aa + 启动 mysql5，回读 Services Status。完成标准：全组件 Active
5. 升级窗口（如执行）：按五步法走，升级前手工备份 CompanyConfig 与 XmediusArchive 两库。完成标准：升级完成且两库有备份
6. 升级善后：核对 xmedius.war 替换后的 Web 界面；自定义工具（外部通知/JavaApi 脚本/查归档库报表）逐个验证。完成标准：自定义项全部恢复或重做
7. 删除策略（如需）：按合规口径配置传真记录与传真文档的删除（可分开/一起，支持零保留）。完成标准：策略生效且有确认记录

判停点：

- 备份脚本里是强杀服务 → 停，改为正常停止（not killed）；强杀备出的档可能损坏，属高危操作
- 恢复环境与备份时版本/拓扑/路径不一致 → 停，先对齐环境再回灌，否则恢复不保证可用
- 升级想跳过"备份数据"一步 → 停，五步法的第 4 步不可省，且必须含手工备库（数据库不在升级自动备份内）
- 客户要"删一半留一半"的混合保留 → 停，书内口径是记录与文档两类可分开/一起删，粒度到类不到条
- 零保留生效后客户又要追溯历史 → 停，删除不可逆，合规口径需客户书面确认后再执行

输出契约：备份物清单（三文件夹/MySQL 目录/.reg）+ 恢复演练记录 + 升级窗口执行单（五步法逐项打勾）+ 删除策略配置与客户确认记录。

## B — 边界

- MySQL 随第三方组件安装（书内默认装成功）；mysql5 服务名与 MySQL Server 8.0 路径为实验口径，生产按实际安装核对
- 备份三域不含用户私人电话本（用户自备）；引导进 Public 电话簿属整理建议（推断）
- 升级目标版本的兼容性与 Release Notes 在书外；本书只给流程骨架
- 删除操作不可逆；GDPR/HIPAA 类合规条款的具体解读在书外，本书只提供"零保留可配置"的技术能力
- xmedius.war、CompanyConfig、XmediusArchive 等命名揭示产品 XMedius 血统（键名/文件名推断，书中未明说）
