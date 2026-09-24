# POLISH-NOTES — oxo-connect-call-center 中文化润色记录（2026-09-24）

范围：.cangjie/capabilities/cards/*.md（15 卡）+ 根 DIGEST.md（扫描覆盖文件）。
原则：只改表达，不动任何数字、版本、页码、IP、端口、菜单路径、命令、参数、文件名、R 段英文原文、专有名词、yaml。

## 一、总体判断

本册为早期精写版本，通读 15 卡未发现机器翻译腔（"被配置为 / 允许……到…… / 使用……来进行……"等模式扫描零命中），无需翻译腔修改。本次工作集中在扫描告警处置：31 条告警（27 处箭头链 + 4 处超长行，其中 schedule-calendar:23 与 DIGEST:25 双重告警）中，改写/拆分 13 行，保留 16 处合法菜单路径/纯流程链（逐条见第三节）。

## 二、逐处修改记录（13 行）

1. cards/agent-app.md · A1「弹屏」
   - 原：`Customers data base → Edit → New（姓/名/电话）→ 用该号码呼组2 → 弹屏出现`
   - 改：`Customers data base → Edit → New 建联系人（姓/名/电话），用该号码呼组2，弹屏出现`
   - 理由：菜单后混入实验动作与结果箭头，保留菜单箭头、动作与结果改正文。
2. cards/basic-setup.md · A1 步骤 1
   - 原：`添加各组 DDI（505→41505、506→41506、507→41507）`
   - 改：`添加各组 DDI（内部前缀 505/506/507 分别对应 41505/41506/41507）`
   - 理由：箭头是"前缀↔DDI"映射符号，非流程；号码原样保留。
3. cards/login-status.md · I 步骤 1「登录」
   - 原：`拨登录前缀（base 1）或按 ACD 页签 Login → 选坐席（…）→ 输密码（若配置）→ 话机即"变成"他的席位`
   - 改：`拨登录前缀（base 1），或按 ACD 页签 Login 选坐席（IP 话机按姓名，模拟与 DECT 按坐席号）、输密码（若配置），话机即"变成"他的席位`
   - 理由：登录操作序列改自然行文，更顺口。
4. cards/omc-first-connect.md · A1「OMC 安装实验」
   - 原：整段一行箭头串（解压安装 → 首连 → 证书 → 改密录信息 → 图标确认）
   - 改：拆成 5 步编号列表（列表前空一行）
   - 理由：散文里塞 5 段逻辑的箭头串，按任务要求拆编号步骤；参数 192.168.92.246、pbxk1064 原样保留。
5. cards/routing.md · A1「需求」
   - 原：`UK(0044)→组1、Spain(0034)→组2、Germany(0049)→组3`
   - 改：`UK(0044) 进组1、Spain(0034) 进组2、Germany(0049) 进组3`
   - 理由：箭头是"分流去向"映射符号，非菜单非流程。
6. cards/routing.md · A1「行为推演」
   - 原：`Brest bank 拨对 DDI → 双匹配进组1；拨错 DDI → 双匹配不中 → 落兜底组3`
   - 改：`Brest bank 拨对 DDI 时双匹配进组1；拨错 DDI 则双匹配不中，落兜底组3`
   - 理由：条件分支逻辑用箭头串表达，改为"时/则"句式。
7. cards/schedule-calendar.md · A1（箭头链 + 超长行 231 字双重告警）
   - 原：实验参数与操作路径挤一行，操作部分 5 连箭头
   - 改：拆为两段——实验参数一段；`操作：General parameters → "Group 1-4" tab 选组，Opening criteria 图标填时段；Exceptional days 页签选过滤方式（opened/closed/both）后按组填两类例外日。`
   - 理由：超长行必须拆；操作序列改行文，保留 1 个菜单箭头。
8. cards/search-noanswer.md · A1「实验 A」
   - 原：`呼组3 无人接 → 103 响 10s → 102 响 10s → 101 响 10s → 回 103 循环`
   - 改：`呼组3 无人接，103 响 10s 转 102，102 响 10s 转 101，101 响 10s 回到 103 循环`
   - 理由：呼叫行为序列用逗号+"转"更自然（"转下一坐席"是本卡 I 段既有表述）。
9. cards/search-noanswer.md · A1「实验 B」
   - 原：`呼组3 无人接 → 103 响 10s 转 102 且 103 自动 off duty → 102 响 10s 转 101 且 102 自动 off duty → 呼叫钉在 101`
   - 改：`呼组3 无人接，103 响 10s 转 102 且 103 自动 off duty；102 响 10s 转 101 且 102 自动 off duty；呼叫钉在 101`
   - 理由：同上，分号分段。
10. cards/voice-prompts.md · I「路径 B」
    - 原：`PC 制作 wav → OMC 四步上传（Mode 切 Transfer → 勾选 prompts → 指定目录 → Load）`
    - 改：`PC 制作 wav，再走 OMC 四步上传（Mode 切 Transfer、勾选 prompts、指定目录、Load）`
    - 理由：括号内是四步操作列举，顿号更合适。
11. cards/voice-prompts.md · A1（超长行 202 字）
    - 原：医生场景话术与上传方式挤一行
    - 改：拆为两段——话术清单一段；`按编号命名 wav，OMC 四步上传或话机 MMC 逐条录制。`
    - 理由：超长行拆分，英文话术引号内容原样保留。
12. DIGEST.md · 第一节（超长行 218 字）
    - 原：产品定位、容量天花板、话机类型、许可四层意思挤一行
    - 改：拆两段——定位+话机+许可一段；容量天花板单独一段
    - 理由：超长行拆分；仅调整句序分段，容量数字（32/8/16/6/10000/14）与许可（5 坐席 8 组）逐一核对未动。
13. DIGEST.md · 第三节「第一层 ACD Setup 向导」（箭头链 + 超长行 298 字双重告警）
    - 原：向导页签序列一行箭头串（General → ACD Group → Profiles → Agents/Supervisors → OK 后重启）
    - 改：`一次成型，页签按顺序做：` + 5 步编号列表（列表前空一行），后台自动生成物段落保留为正文
    - 理由：散文塞 5 段逻辑 + 超长行，拆编号步骤；"501 在值/502 离值/503 文书/504 暂离"等参数原样保留。

## 三、保留的箭头链（16 处，均为合法菜单路径或纯流程链）

1. basic-setup:69 Voice messages 操作流：Transfer mode → 选组 → Default messages → 上传——线性 UI 流程，无分支。
2. multi-secretary:19 十步配置顺序摘要：DDI → 邮箱 → profile → Supervisor 声明 → 坐席 → 路由 → 时段 → 语音——纯顺序链，箭头正是"顺序"语义本体，改动反而失真。
3. omc-first-connect:16 首连菜单/表单流：Expert → LAN/WAN → IP → 勾认证 → 输密码。
4. omc-first-connect:17 装证书菜单流：安全告警 → View certificate → Install certificate → Trusted Root。
5. omc-first-connect:43 安装线性流：解压 → setup.exe → 逐项选择 → Finish。
6. omc-first-connect:45 证书流程（同 3，E 段精简版）。
7. queue:52 配置容量 UI 流：General parameters / "Group 1-4" tab → 选中组 → Queue management → 填 K。
8. routing:56 填表顺序链：双匹配 → 仅 CLI → 仅 DDI → 兜底——纯排序语义。
9. statistics-app:16 查询线性套路：选对象 → 选日期段 → 选图形或表格 → Synthesis 切指标。
10. statistics-app:27 组统计 UI 操作流：Group Statistics → 勾组+日期 → Graphic options → Synthesis → Number。
11. statistics-app:45 连接对话框流：Configuration → "PBX Server" → IP → 语言 → 确认 → 密码 → 点 "ACD"。
12. statistics-app:46 组统计操作流（同 10 精简版）。
13. statistics-app:49 导出操作流：Export → 选格式 → 路径与日期 → Export。
14. supervisor-app:47 纯菜单路径：OMC → System Miscellaneous → Passwords → Management password。
15. voice-prompts:43 OMC 上传四步：Transfer → 勾选 → 目录 → Load。
16. DIGEST:55 标准交付顺序主线：OMC 安装首连 → IP 规划 → 基础 ACD 三步走 → 路由表 → 时段日历 → 三件套部署 → 实呼验证——纯交付流程管道，箭头即顺序语义。

## 四、未改动文件说明

agent-app（除第 1 条）、call-scenarios、dtmf-popup、ip-replan、multi-secretary（除保留项外）、queue（除保留项外）、statistics-app（除保留项外）、supervisor-app（除保留项外）等卡通读后表达自然、无告警，未做改动。

## 五、验收

- scan_dense.py：改写后剩余 16 条告警，全部为上表合法保留项。
- scan_blank.py：零输出（含拆行后的空行规范检查）。
