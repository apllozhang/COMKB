# VAA 外部数据库集成（JDBC 驱动、SQL 节点树、MS SQL/Oracle 接入）

## R — 原文依据

> "By default, only the org.postgresql.Driver and org.mariadb.jdbc.Driver drivers are available and integrated with the VAA. Specific jdbc drivers (MS SQL, Oracle ...) must be downloaded or provided by customer's SGBD administrators."（p320）
> "sudo mv /home/admin/mssql-jdbc-9.4.1.jre8.jar /opt/ale/aa-webapp/lib … It is not possible to make a sftp directly in the directory /opt/ale/aa-webapp/lib … Note: in HA mode, the driver must also be on the slave VAA."（p320）
> "The VAA can only recover one field at a time. To retrieve several fields, you have to make as many requests as there are fields."（p323）
> "SELECT transfertNumber FROM customers WHERE callingNumber='VAR(callingNumber )'"（p323）

出处：VSAAXTE001EN p319-344。

## I — 自述

按数据库数据驱动呼叫流转的三段链：

1. **装驱动**：默认只内置 PostgreSQL 与 MariaDB 驱动；MS SQL/Oracle 等需下载或由客户 DBA 提供，优先厂商官方版

   - 安装路径两段式——SFTP 传到 /home/admin，再 sudo mv 到 /opt/ale/aa-webapp/lib（该目录不能直接 SFTP），sudo systemctl restart aa-webapp 生效
   - HA 模式 slave 也要装同一驱动
2. **建连接**：租户设置 → External Databases 页签 → 库名 + JDBC URL + 驱动名 + 凭证 + 连接测试

   - MS SQL 串形如 jdbc:sqlserver://主机:1433;Database=库名（驱动 com.microsoft.sqlserver.jdbc.SQLServerDriver）
   - Oracle 两种连接串（thin:@host:1521:TNS 服务名 与 service_name 长串式）不等价，可能只有一个能通（驱动 oracle.jdbc.driver.OracleDriver）
3. **建树**：Start、欢迎、SQL request 节点（SELECT 单字段 WHERE 主叫匹配）、Condition 判非空、Transfer 监督转到库中号码、失败播报、Release；SQL 失败走红色连线；绑定测试号验证
4. **MS SQL Express 测试库搭建**（原书整章，正常由客户 DBA 承担）：三个默认值陷阱——TCP/IP 协议默认禁用；1433 端口新版默认不再分配（要手工指定静态端口）；首登仅 Windows 认证（要 SQL 账号必须切 mixed authentication mode 并重启服务）；再加防火墙放行 1433、ODBC 远程验证（取消动态端口、写死 1433）

## A1 — 书中案例

**按来电查库转接树（31410）**（p319-325，实验口径库凭证）：

1. 取 mssql-jdbc-9.4.1.jre8.jar，SFTP 传到 VAA 的 /home/admin
2. sudo mv 到 /opt/ale/aa-webapp/lib 后重启 aa-webapp；HA 则 slave 重复
3. External Databases 页签建库连接：JDBC URL、驱动名、凭证，连接测试通过
4. 实验库 customers 表含 callingNumber/VIP/transfertNumber 三列与测试记录
5. 建树：Startup → Announcement 欢迎提示
6. 加 SQL request 节点执行查 transfertNumber，主叫用 VAR(callingNumber) 匹配
7. SQL 失败输出（红色连线）接专用失败提示
8. 加 Condition 判结果非空（空结果不报错，必须显式判）
9. Transfer 监督转到库中号码；任何失败播提示后 Release
10. 绑 31410 激活；不同主叫拨打，对照表核验转接号

## A2 — 未来触发

使用情境：客户来电报号码查会员转专属坐席；树要读写业务库；MS SQL 连不上；Oracle 连接串选型；驱动安装后不生效；HA 切换后 SQL 节点故障；测试库从零搭。

语言信号：SQL 节点 / JDBC / 驱动 / mssql-jdbc / ojdbc / 外部数据库 / External Databases / jdbc:sqlserver / 1433 / mixed authentication / Oracle thin / service_name / 单字段 / 空结果 / ODBC / SSMS。

与相邻能力区分：SQL/Condition 节点的参数与异常路径 → IVR 选项节点能力；变量机制 → IVR 选项节点能力；库连接安全口径本卡与节点卡共用（p24）。

## E — 可执行步骤

输入契约：客户数据库类型/版本/地址/端口、DBA 配合（生产权限最小化）、网络可达性（VAA 服务器到库端口）、驱动 jar 版本（jre8 兼容口径）。

1. 装驱动：SFTP 到 /home/admin，sudo mv 到 /opt/ale/aa-webapp/lib，重启 aa-webapp；HA 双机都装。完成标准：驱动加载无报错
2. 建连接：External Databases 页签配 URL/驱动/凭证并连接测试。完成标准：测试通过
3. 权限核对：生产账号按用途授最小权限（多数场景只 SELECT），不用测试库全权账号。完成标准：权限清单经 DBA 确认
4. 建树：SQL request（单字段）+ Condition 判非空 + Transfer + 失败路径。完成标准：每条连线有落点
5. 边界测试：库中无此主叫（空结果）、库不可达（SQL 失败）、多条匹配（取首条）三种情形逐一拨打。完成标准：行为符合预期
6. 文档化：库连接信息、驱动版本、查询语句入交付档案。完成标准：可交接

判停点：

- 客户库是 MongoDB/NoSQL → 停，书内仅 JDBC 关系库口径，如实声明边界
- 一次查询要取多个字段 → 停，拆多条 SQL 或重新设计（单字段硬规则）
- Oracle 连不通 → 停，两种连接串不等价，向客户 Oracle 管理员索取正确串，两种都试属正常排障
- MS SQL 新装连不上 → 停，按三默认值陷阱排查：TCP/IP 启用、静态 1433、mixed 认证 + 重启服务
- HA 只在 master 装了驱动 → 停，切换后 slave 跑 SQL 节点即故障，补装

输出契约：可用的库连接 + SQL 节点树 + 三种边界情形的测试记录 + 驱动安装清单（含 HA 双机）。

## B — 边界

- 实验口径：库凭证 vaa/vaa、测试库 DB_VAA、IP 10.20.30.11——生产由 DBA 交付并最小化授权（n28）
- MS SQL Express 整章是测试库搭建（原书定位），生产数据库由客户 SGBD 管理员承担
- "Enforce password policy 可取消勾选"仅限测试库（p334 原文），生产不适用
- Oracle 两种连接串不等价的根因（服务端监听配置）书内未展开（n26）
- 慢查询拖长呼叫时长无量化阈值，需按现场实测（n23 关联）
- 生产网络放行（VAA 到库端口）属客户防火墙策略，书内端口清单外置（n03 关联）
