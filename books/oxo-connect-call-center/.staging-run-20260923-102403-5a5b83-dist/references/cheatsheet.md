# 决策规则速查 — OXO Connect Call Center (Participant's Guide, Edition 07)

| 能力 | 一句话规则 |
|---|---|
| OXO Connect 基础 ACD 全流程搭建 | ACD Setup 向导五步成型 + ACD Services 两菜单补齐，OK 后必须重启 ACD 引擎才生效 |
| ACD 呼入六场景排障 | 任何呼入异常先归入六场景（空闲/全忙/队满/端口忙/全员登出/关闭），再按场景查出口配置 |
| 呼叫特征化与 Smart Call Routing 路由表设计 | 三级优先（双匹配>仅DDI>仅CLI），CLI 从左向右、DDI 从右向左比较，路由表从最特殊填到最一般 |
| ACD 等待队列管理（容量公式与出口配置） | 队列长度 = ceil(On duty 坐席数 × K)，K∈0.1-9.9、上限 16；等待播报 = (队列数/坐席+1)×平均通话时长 |
| 坐席搜索模式选型与无应答处理 | 组内分配三选一（Fixed/Rotating/Longest idle）与 rank 正交；无应答自动移除会把坐席连锁置 off duty |
| 坐席签入签出（free seating）与状态排障 | 四要素建链（坐席名+组+终端+坐席号）才算进入 ACD；登录默认状态看 ACDAutoLog（01 on duty/00 off duty） |
| Multi-Secretary 多秘书方案配置 | 复用 ACD 引擎：经理 DDI 当被叫特征、秘书组当坐席（全 rank1）、十步按序编程 |
| OMC 安装与首次连接 | Expert 模式 + Server authentication + 首连密码 pbxk1064，装证书到受信任根消除告警 |
| OXO 与客户端 IP 规划修改 | 先改 OXO 侧（Boards/LAN/DNS/DHCP 四页签）重启，再改客户端 PC，之后可 RDP |
| ACD 营业时段与例外日配置 | 每周常规时段 + 例外日两层：上限 40 关闭日/10 开放日/每开放日 2 时段，按组分别定义 |
| Supervisor 班长台部署与实时监控 | ACD Admin 专用密码（勿用 installer）+ 活动率周期 1/2h；实时视图含八子态与干预权 |
| Agent 坐席席面部署（弹屏/打标/客户库） | PC-终端关联后登录；Types 表先定义分类码；弹屏需 Line parameters+107.wav+坐席权限三处齐配 |
| Statistics 统计应用与报表导出 | 先核 S1=10s/S2=40s 阈值再连库；导出分 binary（自用）与 csv（外部分析）两种 |
| DTMF 客户码识别弹屏 | 来电输客户码（如 035#）触发席面弹屏；Line parameters 勾组 + 107.wav 提示 + 坐席弹屏权限三处齐配 |
| ACD 语音提示定制 | 每组 6 条提示按固定编号（101=欢迎…x07=客户码）；MMC 话机录制或 OMC 四步上传 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
