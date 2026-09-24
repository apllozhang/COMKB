# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| OTCC / CCD Feature List | ACR 对象容量上限超限后的权威依据（p77 唯一指针）；版本差异核对 | p77, p394 |
| OTCC Standard 基础课程教材 | Advanced 的前置：CCD 矩阵、Pilot、队列、处理组基础（本书默认学员已掌握） | p1-2, p19-38 |
| ACD/CCD 维护与安装文档（OXE 侧） | adm_acd/dhs3_init/mgr 菜单、hybvisu/compvisu 完整手册；本书只给实验用到的分支 | p127-128, p341-342 |
| CCS Server 安装说明（serv_ccs.msi 随包文档） | 外部 CCS Server 的系统要求与安装细节（Windows Server 2019/2022） | p567, p580-590 |
| Azul Zulu JRE 发布页 | ASM Script Editor 依赖的 JRE 8（书示 8.72.0.17 仅为示例，版本可不同） | p207 |
| FlexLM / LMTOOLS 文档 | SPM 许可服务器的安装与状态诊断（Start Server / Status Enquiry） | p408-411 |
| ActiveMQ / JMS 文档 | 业务数据接口推送通道（端口 61618 防火墙放行的协议背景） | p378, p387 |
| CCTA 工具文档（结束原因/呼叫类型全码表） | p488 只给样例码（40 种结束原因、10 种呼叫类型），全表在工具文档 | p488 |
| 生产安全基线文档（密码策略/证书/加固） | 原书安全基线零覆盖，交付前须按 ALE 安全指南补齐 | n01, n40 |

## 2. 官方工具与站点

| 工具/站点 | 用途 | 书内位置 |
|---|---|---|
| CCsupervision（CCS） | 配置/实时/统计/脚本编辑器四区一体；ASM Script Editor 内嵌入口 | p39-47, p94-115 |
| ASM Script Editor（asm-se_setup.msi） | ACR 脚本编写与调试；已装 CCS 后必须用专用 msi 补装 | p204-208 |
| Soft Panel Manager（wbm，端口 9060） | 实时统计上墙管理端；admin/admin 首登（实验口径） | p396-417 |
| RTI Connector | CCS 到 SPM 的取数 Windows 服务；同机时 CCS 须专用 | p396-411 |
| Contact Center Ticket Analyser | 通信/事件票据离线分析（Importation + Ticket Tracer） | p480-497 |
| Excel（FormPil 等模板） | CCS 统计报表定制载体；Formats 目录按对象分模板 | p531-554 |
| LMTOOLS | FlexLM 许可状态验证 | p408-411 |

## 3. 姊妹教材与技能分工

- **姊妹 bundle**: bundle.otcc-advanced-call-routing（ACR 专题技能）——承接 ASM 脚本编写/调试器深度/LCA 脚本族的完整操作闭环（本书 task-07/08/10/11 的脚本部分从简，卡内给安装与生命周期主干，深度操作指向姊妹技能）。
- **本书 bundle**: bundle.otcc-standard-advanced——聚焦"其余高级能力"：ABC-F 互助与 Remote PG、Soft Panel Manager 墙板、CCTA 票据分析、特殊功能、Excel 报表定制、CCS Server 集中接入，以及 ACR 对象/技能体系与 ISM 匹配口径。
- 两 bundle 的边界写法：本书卡内涉及脚本编写细节时标注"深度操作见姊妹技能 otcc-standard-advanced-call-routing"。

## 4. GLOSSARY 落位说明

- candidates/glossary.md g01-g56（56 条，concept 23 / role 4 / subscription 4 / product 12 / protocol 5 / resource 8）全部通过术语核验；OVERVIEW 的 16 个候选术语逐条映射无遗漏。
- 落位口径：GLOSSARY 全量收录（六类分组）；阶段 3 生成 `book/glossary.md` 门户版（精选高频约 40 条，保持第一本版式）。
- 书中未给全称的缩写（DDI/DID、ABC-F、GT、RSI、CSTA、MAO、OMS、GD4、TSC、COS、IPDSP、EWT/MWT、ITSP）均未编造 full_name，仅在定义里标注书内上下文用法。

## 5. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- POD 网段 192.168.1.x：OXE 本地节点主 CPU 192.168.1.3 / 远程节点主 CPU 192.168.1.103；Client PC10 192.168.1.10 / PC11 192.168.1.11；Windows Server 192.168.1.70；FlexLM 192.168.1.80；内网关 192.168.1.254 / 外网关 10.20.30.254；内 DNS 192.168.1.250 / 外 DNS 10.20.30.250（p7-9）。
- 实验账号（p9, p46, p52, p272, p404, p493）：OXE mtcl/Superuser2580*、root/Superuser2580*；CCS administrator/alcatel 首登强制改密；SPM admin/admin；FlexLM root/letacla1；SIP 分机密码 123456；IPDSP 个人码 0000；ITSP 注册 pbxP/alcatel；CCTA 导入书示 mtcl/mtcl（按现场实际填）。
- 实验号码（p16-17, p56-57）：安装号 3321PN（PN=POD 号两位）；DID 翻译首外号 33210N41000、首内号 31000、范围 1000；外呼拨 0210X41600/0210X41601；ACR 实验对象号 Agent2_PG=31803、WaitingRoom=31704、ACR Pilot=31603、统计 Pilot 31660/31661；Remote PG 实验网络前缀=32602、Remote_PG=31851、虚拟队列=32703、远端坐席 PG=32800。
- 培训环境专属：RLAB 公共 Pod 提供 NAS 与 SIP 模拟器；Console mode 无音频、RDP 通道承载软话机音频（p13, p61-62）。
