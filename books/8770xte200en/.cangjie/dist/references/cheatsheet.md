# 决策规则速查 — OmniVista 8770 — Setup & Network Management (Participant's Guide, Edition 47)

| 能力 | 一句话规则 |
|---|---|
| OmniVista 8770 平台安装（服务器 + 客户端 + 补丁 + 首连） | 专用服务器七步装链（配置 > 组件 > 安装 > 补丁 > 首连）；IE ESC 关闭与 Defender 排除 C:\8770 是 Alarms/Topology 前提 |
| OmniVista 8770 节点接入（OXE 注册同步 + SSH 安全 + OXO Connect 纳管） | 三级树声明（节点号=网络号×100+节点号）> 四语义同步 > 31234 实时核验；OXE SSH 可信主机链；OXO 经 OMC 纳管（声明节点 180 落盘） |
| OmniVista 8770 用户开通（Profile / Meta profile / 批量 / WBM） | 三层递进（手建 > Profile 复用 > Meta profile 自动取号）+ 批量文件（XXXX/NULL/action）；WBM 轻客户端与 thick client 文件互不通用 |
| OmniVista 8770 告警管理（接入 + 定制出口 + SNMP Proxy） | OXE incident manager 全上送 + rstcpl/incvisu 验证（#2042/#1125）；出口三加一——签名、邮件（server:port）、脚本（%1/%2）、SNMP Proxy trap |
| OmniVista 8770 安全管理（密码策略 / 管理员与组 / 访问控制 / TLS） | 密码策略（B+C<A）> 管理员/组（取最高+单登录+四路解锁）> OXE Access Profile（11 档共用、删本地 MIB）> OXE 白名单（Secure access 前提） |
| OmniVista 8770 审计合规（Audit 启用 / mao 日志 / 检索导出） | 双侧启用（AuditServer + OXE Process audit/mtcl/Secure access）> mao 三日志留痕 > PbxName Not Empty 检索 > History/Detail 导出与报告 |
| OmniVista 8770 备份恢复（8770 数据库 rehosting + OXE swinst 全链） | 8770 备份四块内容、版本绑定（nmcVersion）、rehosting 三场景改址；OXE bck 备份取回与 swinst 七步恢复链（停电话+物理 IP） |
| OmniVista 8770 许可管理（锁结构 / 查询 / 更新 / 受限模式） | ACTIS 出证 nmc.license > 四段锁结构（8770Handle/Modules/8770Clients 30/Security 0-5）> spadmin/About 查询 > 换文件更新 > 超限进受限模式 |
| OmniVista 8770 报表与任务编排（Reports / Scheduler / 自动维护） | 报告生成/导出/计划（上限 TXT 4000 行、各格式 50 页、库 100000 行）+ Job/Task/jobset 编排 + 五类 purge 与 LDIF 恢复 |
| OmniVista 8770 维护运营（诊断工具 / NMC 服务与日志） | 三件套采数据（Diagnostic/DirManag/HeidiSQL）+ 两层服务模型（4 Automatic vs 约 20 被监督）+ 日志滚动与 TraceType 细跟踪（查完改回） |
| OmniVista 8770 Topology 视图（标准视图 / 自定义视图 / 告警重定向） | Standard 自动视图（背景地图 1100x793 入 maps 重启）+ Custom 编辑器建屏 + 告警重定向（Redirecting alarms）；只显示相关告警 |
| OmniVista 8770 OXE 配置界面高效操作（搜索/冻结/网格/导入导出） | 搜索、冻结列、网格/文件切换、属性选择、图形视图配键、树与网格导入导出（.txt/.prg） |
| OmniVista 8770 网络驱动器映射（报表与备份落网络存储） | 远程共享（REPORTS_ECO/BACKUP_ECO）+ 同名同密 ADM8770（Administrators 组+五项权利）+ ExecdEx/SaveRestore 注入 .\ADM8770 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
