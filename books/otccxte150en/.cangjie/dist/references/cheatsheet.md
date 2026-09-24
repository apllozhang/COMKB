# 决策规则速查 — OmniTouch Contact Center Standard Edition — Advanced Call Routing (Participant's Guide, Issue 01)

| 能力 | 一句话规则 |
|---|---|
| ACR 脚本编辑器与调试工具链 | 编辑器写脚本传输激活五环闭环；Debugger 只能改不能加构件；asm_ag_free_duration 定 Idle 语义；字符串五关键字 |
| ACR 基础 CCD 矩阵地基 | ACD 前缀先行，普通链路与 ACR 链路并行搭矩阵；规则 30 条分发 10 条，优先级 0 最高；房间与队列互斥 |
| ACR 重定向与再分发兜底 | 空列表两式兜底——Redirection 转号（静态/动态地址）或 Redistribution 退下一路由方向，全无方向落 Blockage |
| ACR 坐席直拨融合 | Pilot Direct Call 加私有号加 DICA 自动技能加 CALL_TYPE 分支脚本，实现直拨忙时等原坐席再转接 |
| ACR 内部数据库路由 | 主叫号、Call Tag、坐席号三键查档案名单优先级；CALL_PROFILE[键] 语法取用；区段键整段命中 |
| ACR 综合规则组合与高级构件 | 单 APPLY 链式过滤、多 APPLY 第一个失效；IDLE/COM 互斥；IQUEUE 停放覆写；LIST 变量动态名单；混跑选呼三序 |
| ACR 外部 ASM 部署与双机热备 | asm_on_dhs=0 停内部 alb，装 Windows 服务建 Site 链路，迁 .scr 重编译；双机 Main/Stand-By 自动复制脚本与连接 |
| ACR 外部数据库查询路由 | SQL 六构件（连接/请求/测试/映射/fetch）加 32 位 ODBC 加 167 许可；存储过程把 LCA 落库，ASM 重启不丢 |
| ACR 授权与非授权名单规则 | 名单规则五式给值（上下文索引/整数/名字/显式列表/LIST 变量）；100 列表每表 30 坐席；String 索引大小写敏感 |
| ACR Call Tag 生成与传递 | 统计 Pilot 静态标、IAA 编码叶 16 位、CCivr TransferCall 三来源；转发链上最后一个标签覆盖之前所有 |
| ACR 多语言语音引导与语言偏好分发 | 一个引导映射 40 语种；语言取档案偏好（1 最高）无则退 Pilot 语言；坐席 1 门语言技能即可入选 |
| ACR 过滤器与统计报表 | 过滤器只影响观测不改分发；200 个每个 7 技能 AND 语义；Super/Hyper-Filter 25 对象 OR；Excel 三模板 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
