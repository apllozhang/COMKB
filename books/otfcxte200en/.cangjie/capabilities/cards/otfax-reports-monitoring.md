# OTFC 报表与监控（31 报表、BIRT 自定义、SNMP V2 陷阱）

## R — 原文依据

> "Reports can be executed by using the available report templates •It is possible to manage and customize the report templates by using the BIRT report designer •To install the BIRT report designer, unzip the .zip file found in the 3rd\birt folder of the OTFC installation package ; 31 reports are available"（p226）
> "SNMP V2 Services • Component status changes •Incoming queue reaches max size •Site outbound quota reaches maximum size •Rasterization failure •Routing failure"（p228）
> "Trace folder stores log files for all the OTFC services."（p225）

出处：OTFCXTE200EN p225-229。

## I — 自述

主动运维三件套：

1. **报表**：31 个模板（数值 + 图形），覆盖全系统/单用户 × 月/周/日、模块错误摘要；自定义用 BIRT 报表设计器，从安装包 3rd\birt 目录解压安装
2. **站点级/系统级监控**：路由、来话、去话、排队、错误、传真属性（错误信息/传输信息/时间与大小）分层可查
3. **SNMP V2 trap 清单**：组件状态变化、入呼队列达上限、站点出呼配额满、光栅化失败、路由失败、XML 文件读取错误、驱动发送错误、分区检测、通道初始化失败；主机监视 trap——组件状态变化、性能计数器、组件状态表、通道状态、远程主机心跳
4. **关联告警**：LDAP 目录断连也自动产生 SNMP trap；日志层（Trace 目录，默认 20MB/15 天）与 trap 层互补——trap 管"出事了"，日志管"为什么"

## A1 — 书中案例

**报表自定义安装**（p226，讲义口径）：

1. 找到 OTFC 安装包 3rd\birt 目录下的 zip 文件
2. 解压安装 BIRT 报表设计器
3. 用设计器管理与自定义报表模板
4. 按全系统/单用户、月/周/日维度出报表

**SNMP 监控落点**（p228-229）：

1. 客户网管平台接收 OTFC 的 SNMP V2 trap
2. 按清单对号：组件状态/队列满/配额满/光栅化失败/路由失败等
3. 主机监视类 trap 提供性能计数器与心跳，供容量与存活监控

## A2 — 未来触发

使用情境：领导要月度传真量报表；报表格式要改；网管平台要接传真服务器告警；磁盘/队列告警怎么设；目录断连怎么第一时间知道。

语言信号：报表 / report / 31 / BIRT / 模板 / 月报 / 周报 / 统计 / SNMP / trap / 告警 / 监控 / monitoring / 队列满 / 配额 / 光栅化 / routing failure / 心跳 / heartbeat / 性能计数器。

与相邻能力区分：日志排障（日志内容怎么读）归服务运维能力；配额/队列阈值背后的站点配置归 Profile 策略与用户管理能力；计费报表（按人成本）归目录与路由能力的 Accounting 段（OXE 话单 + OmniVista 8770）。

## E — 可执行步骤

输入契约：报表需求（维度/周期/受众）、客户网管平台（SNMP V2 接收能力）、告警分级口径。

1. 出标准报表：按全系统/单用户 × 月/周/日选模板执行。完成标准：报表交付
2. 装设计器：解压 3rd\birt 下 zip 安装 BIRT。完成标准：设计器可用
3. 定制模板：按受众改字段与图形。完成标准：自定义模板入模板库
4. 接网管：客户平台配置接收 OTFC 的 SNMP V2 trap，按清单做告警映射。完成标准：测试 trap 到达平台
5. 定告警分级：队列满/配额满/光栅化失败等按影响分级，LDAP 断连 trap 确认有落点。完成标准：分级表获客户确认
6. 建例行：月度报表定期出、trap 值班响应口径入运维手册。完成标准：例行化运转

判停点：

- 客户网管平台不支持 SNMP V2 → 停，书内只有 trap 上报一条监控通道，平台侧改造或替代方案另议
- 要把 31 个模板之外的指标入报表 → 停，先确认归档库里有没有该数据（BIRT 查库口径书外），不承诺书内没有的字段
- trap 收到了但没人管 → 停，先落值班响应口径再上线告警，避免告警疲劳
- 计费/成本类报表诉求 → 转目录与路由能力的 Accounting 机制（OXE 话单 + OmniVista 8770），不走本卡

输出契约：报表交付物（标准 + 自定义模板）+ SNMP 告警映射表（trap 对号/分级/响应人）+ 例行运维口径说明。

## B — 边界

- BIRT 设计器本身是外部工具（Eclipse 生态），安装与设计器用法书内只给 unzip 一句，细节在工具文档
- SNMP 网管平台由客户提供；OTFC 侧 MIB/_oid 明细书内未展开，对接时以产品文档为准
- 31 个报表的具体清单与字段书内为概述口径；模板明细以现场版本为准
- 主机监视 trap 的阈值调整书内未展开；性能基线需现场采集
- 报表数据来源于归档库（XMFaxArchive）；直接查库做定制属书外扩展，升级前按备份升级能力的自定义工具口径预验证
