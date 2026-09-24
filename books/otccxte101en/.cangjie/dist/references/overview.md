# Book Overview（参考区）— OmniTouch Contact Center Standard · Advanced

> 供能力卡引用的背景参考；源自 references.md 落位。

## 课程主线（成对结构，交付组织轴）

环境与基线（RLAB POD、CCD 预配置、CCS 安装、POD 定稿）> ACR 高级路由主线（对象管理 > ISM 算法 > 脚本编辑器 > 调试器与重选 > LCA 规则）> 网络化（互助 > Remote PG）> 增值域（Soft Panel Manager 三模块、CCTA、特殊功能、Excel 定制、CCS Server）。每个能力域"讲义（对象模型+数值边界）> How-To（菜单路径+行为验证）"成对出现；实验依赖链：CCS 安装 > POD 定稿 > ACR 管理 > ISM 脚本 > 重选/调试 > LCA > Remote PG。

## 实验环境（RLAB，仅 Boundary 背景）

- POD 池相互独立；公共 Pod 提供 NAS（软件/许可）与 SIP 模拟器（p5-7）。
- 实验网段 192.168.1.x：OXE 本地节点主 CPU 192.168.1.3、远程节点主 CPU 192.168.1.103；Client PC10 192.168.1.10 / PC11 192.168.1.11；Windows Server 192.168.1.70（CCS Server）；FlexLM 192.168.1.80；内网关 192.168.1.254、外网关 10.20.30.254；内 DNS 192.168.1.250、外 DNS 10.20.30.250（p7-9）。
- 客户端预装 3 个 MicroSIP（31010/31011/Public，SIP 密码 123456）+ IPDSP 坐席软话机（31000，个人码 0000）；接入双通道：Console mode（无音频，管理用）与 RDP（承载软话机音频，实验必用）；嵌套 RDP 时远程音频须指向本机（p10-13, p60-62）。
- ITSP1 号码规则：安装号 3321PN（PN=POD 号两位）、DID 首外号 33210N41000/首内号 31000/范围 1000、外呼拨 0210X41600（p16-17, p57）。
- ACR 实验对象号：Agent2_PG=31803、WaitingRoom=31704、ACR Pilot=31603、统计 Pilot 31660/31661；Remote PG 实验：网络前缀 32602、Remote_PG=31851、虚拟队列 32703、远端坐席 PG=32800、远端坐席 32500（p130-159, p338-370）。
- 实验账号口径：OXE mtcl/Superuser2580*、root/Superuser2580*；CCS administrator/alcatel 首登强制改密；SPM admin/admin；FlexLM root/letacla1；ITSP pbxP/alcatel；CCTA 导入书示 mtcl/mtcl。

## 平台速览（方案沟通素材）

- ACR 容量上限（p77，R10.15 口径）：

| 对象 | 上限 |
|---|---|
| 统计 Pilot | 3000 |
| Pilot | 600 |
| 队列与等待室 | 600 |
| 组 | 450 |
| Pilot>队列 / 队列>处理组方向 | 30 / 50 |
| 域 / 技能 | 20 / 1000 |
| 特征清单 | 1000 |
| 特征数（每档案/每坐席/系统） | 7 / 50 / 20000 |
| 授权名单 / 非授权名单 | 30 / 30 坐席 |

- SPM 限制（p394）：订阅统计 500、并发连接 150、面板+墙板 200；OXE 11.1 不放宽 CCD 对象数；AFE 统计不支持空间冗余。
- CCS Server 接入（p557-558, p567）：AFE 物理上限 15 连接；内部 Server 15 客户端、外部 Server 120 客户端；连接数 >9（CCd R3.1+CCs 4.3.46.1 起）必须上 CCS Server。
- 关键行为口径：坐席统计默认 5 分钟刷新（p175/p215）；脚本重选上限 21 次（p214/p245）；SPM 统计按需订阅最多 1 分钟生效（p408）；日统计 15 分钟节拍不可更快（p417）。

## 教材口径声明

- 全部实验密码/账号/号码/网段仅限实验环境；生产必须整体替换并按安全基线加固（原书明文口令遍布正文，引用时一律标"实验口径"）。
- 生产化边界：超限与 sizing 回当期 Feature List；技能体系设计方法论、话务建模、监听/录音合规均在书外，交付前须另行补齐。
- 版本敏感点：p558 "29 or 120" 按图示 15/120 理解（needs-review nr-01）；p236 统计 Pilot 31650 为讲义示例号串入（nr-02）；LAST_CALLED_/LAST_CALL_ 关键字混用以编辑器下拉为准（nr-03）。
- 版本基线：OTCC Standard R10.15 / OXE 11.1 / CCS V10.2.92.0+ / 浏览器 120+ / 外部 CCS Server 仅 Windows Server 2019/2022（p387, p567）。
