# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| Feature list OmniTouch Contact Center Standard Edition（Common Hardware Architecture） | 话机兼容清单、可选件功能矩阵的权威依据（书中给 Salesforce 内部链与 MyPortal 外部链） | p33 |
| OTCC901 Advanced Training（进阶教材） | 话机录音第四法（Audio Station 线）、Excel 宏（ACDMacro）、CCIVR/ACR 深入的唯一指向 | p204, p524 |
| 目标库文档 / Feature list（分市场） | 国家默认差异核查：Show Supervisor Listening（法/德默认 False）、Recordable Voice Guides（法语库默认关）、ABC Local Call Allowed（法国库默认开） | p218, p315, p162 |
| OXE mgr / OmniVista 8770 | 语音指南装板管理的替代管理路径（书中仅点名） | p160 |
| CCA 10.7.8.0+ 发布说明 | 弃呼报表 click-to-call（tel: 协议超链接回呼）的版本前提 | p508 |
| Stat_lang.pdf（CCS 端 ProgramData 下） | Excel 统计模板字段的帮助文档 | p479 附近统计章 |
| ALE Connect 方案页 | 全渠道（邮件/聊天/社交）定位图，仅一页无细节 | p38-39 |

## 2. 官方站点与工具（书内出现）

| 站点/工具 | 用途 | 书内位置 |
|---|---|---|
| My ALE / Salesforce 内部链 | Feature list 获取入口之一（书内原样给出） | p33 |
| OTCC_NAS 网络盘 | CCS 安装包与 .wav 素材（实验口径） | p90, p240 |
| PuTTY（会话 OXE-SSH） | mtcl 命令行（acdsup/vgstat/hybvisu/rsthyb/config），字符集 ISO-8859-1 | p76-77, p215, p247 |
| Alcatel Audio Station / VGTransfer | 语音指南文件制作与传盘工具（书中点名未展开，实验用 CCS Audio File Update 替代） | p199 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g46（46 条）全部通过术语核验；六类分布：concept 17 / role 7 / subscription 1 / product 9 / protocol 8 / resource 4。
- 落位口径：`book/glossary.md` 收录精选高频词条（门户版）；阶段 3 编译时随包发布。全量 46 条保留在 candidates/glossary.md 作审计痕迹。
- 书中未展开全称的缩写（CCD、ABC-F、CSTA、DID、AFE、TSC、NOE、AGAP、ProACD、OMS、PLTR、ITSP）已在相应条目如实标注"书中未展开"，不采信外部知识补全（PLTR 另见 needs-review nr-10）。
- 本 bundle 为 on-premise 产品，无用户订阅体系；subscription 类以"许可/token"对齐（CcsLight / Monosite / Multisite token，FlexLM 承载）。

## 4. 实验环境口径备查（仅作 Boundary 背景，正文不进能力卡；book/overview.md 收全文）

- RLAB POD 五实例（实验口径）：OXE 192.168.1.1/1.3（mtcl，口令 Superuser2580*；swinst/root 同口令）、OMS 192.168.1.13（root）、FlexLM 192.168.1.80（root/letacla1）、Client PC10 192.168.1.10（IPDSP 31000 + 3 个 MicroSIP 31010/31011/Public）、Client PC11 192.168.1.11（IPDSP 31001）。
- ITSP1 模拟器：SIP 网关 gateway1.itsp1.com（10.20.30.51，注册 pbxP/alcatel）、公网网关 public.itsp1.com（10.20.30.50）；安装号 3321PN、DDI 首外线 41000/首内线 31000；打 Pilot 拨 0210X41600/0210X41601（X=POD 号）。
- 法国目标库实验前缀与资源：ACD 前缀 12（+1 退出/+2 wrap-up/+3 呼班长/+5 登出/+6 登入/+91/+92）、401 录音、580 试听；板位 4-0（OMS）；备份音 56、默认演示指南 70、直连阻塞默认 75；518/538 与消息 3226-4217 为系统预置。
- CCS 侧实验口径：administrator/alcatel 默认账号（首登强制改密，实验改 Superuser01*）、功能码个人码 0000、Excel 表单保护密码默认 alcatel、ShowStatisticWithData 手改 ccs.ini。
