# OmniVista 8770 审计合规（Audit 启用 / mao 日志 / 检索导出）

## R — 原文依据

> "Browse to nmc > OmniVista 8770 > nms > Service > AuditServer ... Audit process Validate the check box to enable the Audit application"（p426）
> "The rsh command converts the /DHS3data/mao/mao_hdet file ... into the text file /DHS3data/mao/list_fhdet.txt"（p427）
> "2011/09/20 16:33:22 CREATE Subscriber 101 31004 (nms|adminnmc)"（p428）
> "The search options set up by default don't work. Erase all search entries and create the following entry: PbxName Not Empty"（p431）
> "Warning: THIS PART DOES NOT APPLY FOR THE AUDIT INFORMATION ON OMNIVISTA 8770 LOGS"（p433）

出处：8770XTE200EN p416-434（Audit 应用讲义与 How-To）。

## I — 自述

审计能力=让 OXE 上的管理操作留下"谁在何时改了什么"的痕迹，并在 8770 侧检索、导出、出报告。三个边界先行：

- 只审计 OXE：OXO/OpenTouch 的管理操作不进 Audit 应用（应用 Limits 原文 Only for OmniPCX Enterprise）
- 8770 自身 log（客户端登录、Accounting/Reports 应用访问）只可查看，不适用右键导出功能
- 双侧开关缺一不可：8770 侧 AuditServer + OXE 侧 Process audit

**启用清单（双侧）**

- 8770 侧：Administration 应用 nmc > OmniVista 8770 > nms > Service > AuditServer > Specific 页勾 Audit process；同页配审计记录保留天数、导出 CSV 寿命与 Keep one backup
- OXE 侧（Configuration 应用选 OXE）：Data Collection 页勾 Process audit；Software download 页填 mtcl 维护账号（rsh 执行 list_fhdet 转换 mao_hdet 用）；Connectivity 页勾 Secure Access for System Management（把 8770 管理员名记入 OXE 的 mao_hist）
- 同步：Configuration 或 Audit 应用右键 OXE > Synchronization > Audit information（日同步自动取回）

**OXE 侧三日志（痕迹本体）**

| 文件 | 内容 |
|---|---|
| /usr3/mao/mao_log_hist | 8770 管理员连接记录（nms\|账户名） |
| /usr3/mao/mao_hist | 管理操作行：时间 + CREATE/UPDATE/ACTION + 对象 + (来源\|操作者) |
| /usr3/mao/mao_hdet > list_fhdet.txt | rsh 转换的操作明细文本（8770 检索用）；/var/log/shell.log 另存命令历史 |

**检索与导出（8770 侧）**

- Operations 页：双击行看明细；广播场景 User 字段显示源节点（如 1.2）
- System 页：默认搜索条件无效（产品行为），先清空全部默认条目再建 PbxName Not Empty
- 8770 log 页：选服务器看客户端登录登出与 Accounting/Reports 应用访问（先开关一遍应用再查）
- 导出：右键 OXE > Export——Immediate on local drive（目录任选）或 Scheduled on Server（固定 8770\Client\data\audit）；粒度 History（13 个主参数）或 Detail（追加 Attributes 全量）；CSV 打开建议文本编辑器
- 报告：Reports 应用 Audit > Predefined Reports > Detailed Reports 复制到个人文件夹 > Generate Report（附加过滤可空）

## A1 — 书中案例

**审计实验**（p425-434）：

1. AuditServer 勾 Audit process 并配保留参数
2. OXE 侧勾 Process audit、填 mtcl、勾 Secure Access
3. 分别用 AdminNmc 与 Expert1 在配置界面做增删改
4. OXE 上查 mao_hist 出现 (nms|adminnmc) 标注的 CREATE Subscriber 行
5. 右键 Audit information 同步后，Audit 应用 Operations 页见操作记录
6. System 页清默认条件建 PbxName Not Empty，查出数据
7. 8770 log 页开关一遍应用后看到登录记录
8. 导出 CSV 落盘（Immediate 或 Scheduled 两模式各验一次）；Reports 复制 Detailed Reports 生成报告

## A2 — 未来触发

使用情境：等保审计取证；追查"谁改了配置"；客户要 OXO 操作审计；审计数据导出归档；定期审计报告。

语言信号：Audit / AuditServer / Process audit / mao_hist / mao_hdet / list_fhdet / 审计同步 / PbxName Not Empty / History Detail / 8770 log / Detailed Reports / 操作留痕。

与相邻能力区分：登录认证与密码锁定（安全管理能力）；告警与故障（告警管理能力）；本能力管"事后取证与留痕"。

## E — 可执行步骤

输入契约：客户审计保留期要求（天数）、mtcl 凭据（现场已自定义）、Secure access 可开启确认。

1. 8770 侧启用 AuditServer 并按客户要求配保留天数。完成标准：Audit 应用可打开
2. OXE 侧三开关：Process audit + mtcl + Secure Access。完成标准：三项勾选保存
3. 做一次已知操作（建/改/删用户）。完成标准：mao_hist 出现带操作者标注的记录行
4. 右键 Audit information 同步。完成标准：Operations 页检索到该操作
5. System 页建 PbxName Not Empty 查询。完成标准：返回该 OXE 的审计数据
6. 8770 log 页核对客户端登录与应用访问。完成标准：登录登出可见
7. 导出：Immediate（自选目录）或 Scheduled（固定目录）+ History/Detail 选粒度。完成标准：CSV 落盘可打开
8. 计划报告：Reports 复制 Detailed Reports > Schedule（挂入报表任务体系）。完成标准：计划任务执行成功

判停点：

- 客户要 OXO/OpenTouch 操作审计 → 判停说明边界（Audit 仅 OXE），给替代方案再立项
- System 页查出空结果 → 先清默认条件（默认条件无效是产品行为），不是丢数据
- 要导出 8770 自身 log → 导出功能不适用，只能页面查看或走服务器文件
- mao_hist 无管理员名 → 查 Connectivity 页 Secure Access 是否勾选

输出契约：审计启用核对单 + mao 日志样例 + 检索/导出记录 + 审计报告计划。

## B — 边界

- 审计对象仅 OXE；OXO/OpenTouch 管理操作不留痕于 Audit 应用
- rsh/mtcl 凭据明文通道是 OXE 侧既有口径；生产网络隔离与凭据轮换按客户基线
- 保留天数与导出 CSV 寿命须符合客户合规要求；NmcArchive 文件夹清理（磁盘/目录双阈值）在维护运营卡覆盖
- 审计的批量报告分发（邮件/计划）复用 Reports 体系，见 reports-scheduling 卡
- Secure Access for System Management 同时影响 OXE 侧访问白名单（安全管理卡），变更需联动评估
