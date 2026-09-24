# 决策规则速查 — OmniTouch Contact Center Standard Edition - Advanced (Participant's Guide, Edition 07)

| 能力 | 一句话规则 |
|---|---|
| ISM 技能匹配与排序口径 | 强制属性全满足进第 1 子列表，逐级降级；同级 Cman 最小者胜，同分比 Copt，再比 PLTR/LIT；列表缓冲 20-400 |
| Remote PG 分布式互助与 ABC-F 链路 | Remote PG+虚拟队列+专用 Pilot 三对象跨站点互助；优先级 0-9、分布门限、MWT 三级水位；hybvisu 判读链路 |
| Soft Panel Manager 部署与基础设置 | SPM 服务器+RTI Connector+FlexLM 三件套；CCD Filters 是统计总开关；日统计 15 分钟节拍不可更快 |
| Soft Panel 可视化配置（视图/挂件/消息/告警） | 背景>视图>面板>挂件四层模型；挂件 13 族；告警四步（阈值+邮件+告警视图）；显示端 displayPanel.htm |
| CCTA 话务票据分析 | Importation 导入 .Z 票据 + Ticket Tracer 过滤分析并导出 ASCII；结束原因 40 种/呼叫类型 10 种 |
| 特殊功能开关（优先转接/忙音/代接/监听/永恒整理/中继预留） | 四类开关（Pilot/PG/坐席数据/系统级）+ 行为验证；中继预留两级数学 62 条>50 条>15 条 |
| Excel 报表模板定制 | Formats 目录 11 种模板；Custom 工作表结构拷贝+值区 Paste Link；½ 小时粒度单表只到 16:00 |
| CCS Server 集中接入 | 直连 15 连接、内部 Server 15 客户端、外部 Server 120 客户端；连接数 >9 必须上 CCS Server |
| ACR 对象与技能体系 | 处理组/等待室/ACR Pilot/统计 Pilot/技能体系双侧配置；坐席无技能则等待室阻塞 |
| ASM 脚本与 LCA 主干 | 专用 msi 装编辑器、.scr+.alb 编译激活、调试器三窗格、LCA 记忆与 kill alb 清理 |
| CCS 安装与实验环境定稿 | CCS 八步安装+ccs.ini 声明重启+POD 定稿四件套（软话机/坐席/SIP 网关/DID） |
| ACD 维护命令箱 | adm_acd 命令树（含 -salb/-servccs）、agacd、hybvisu/compvisu、pildstctx/pgctx、acdsup、spadmin |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
