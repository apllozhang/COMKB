# Book Overview（参考区）— OmniVista 8770 目录管理

> 供能力卡引用的背景参考；源自 references.md 落位。

## 全书主线（交付组织轴）

1. 目录核心概念（树/UID/DN/六类链接/数据更新/LDIF）
2. OXE 节点注册
3. PCX 自动创建
4. 链接管理与改名
5. LDIF 导入导出
6. Web 目录客户端
7. 保密级别
8. Click to Call（中间插 SIP 运营商前置）
9. 词典/客户端定制
10. MSAD 三部曲（声明同步/插件/Azure AD）
11. 管理域与委派
12. 目录复制
13. LDIF 管理工具（p4, p59-60, p88-558）

## 关键数字速览（与原文逐格核对）

| 数字 | 含义 | 出处 |
|---|---|---|
| 65535 | Consumer 副本 ID（固定自动） | p509 |
| 1-65534 | Master 副本 ID（手工，不重复） | p510 |
| 1 主 4 从 / 5 副本 | 复制拓扑上限 | p514 |
| 7 天 | 从机断联阈值，超时主侧新增数据丢失 | p515 |
| 500 | 个人地址簿条目上限（GlobalParameters 默认） | p328 |
| 五种 | 个人数据（家庭电话/住址/驾照/工号/密码） | p210 |
| 四级 + 五档 ×2 | 保密四级；Company/Web Directory 各五档访问级别 | p209, p214-215 |
| 六类 | 人员-用户链接类型 | p69-72 |
| 一条映射 | MSAD Attribute mapping 全 8770 只能建一条 | p380 |
| 5:00AM | 复制调度实验口径 | p530 |

## 实验环境（RLAB，仅 Boundary 背景）

- POD 池相互独立同构：OXE（csa 192.168.1.1 / csm 192.168.1.3）、OMS（192.168.1.13）、FlexLM（192.168.1.80）、Client PC（192.168.1.10，装 IPDSP 31000 + MicroSIP 31001/31002）、Ecosystem（192.168.1.100，AD 服务器）、OV8770 server（nms 192.168.1.70）；内部 DNS 192.168.1.250、网关 192.168.1.254；公共区 10.20.30.x（SIP 模拟器 12.0.0.2）（p41-51）。
- ITSP1 SIP 模拟器：gateway1.itsp1.com（10.20.30.51，注册 pbxP/alcatel）+ public.itsp1.com（10.20.30.50）；号码规则 3321PN12345 族（PN=POD 两位号）；DDI 首外部号 3321PN41000、首内部号 31000（p54-57）。
- 账户口令（实验口径）：AdminNmc/Superuser01*；adfexc、mtcl 均为 Superuser2580*；MSADadmin/MSAD8770Admin 用 Superuser01*；话机密码 0000、SIP 话机密码 123456；复制管理器默认 superuser（p47, p90-93, p219, p404, p520）。
- 分机口径：31000-31005/31022-31024/31105；CC：MKT/Training/TSS（ID 0/1/2）（p110-117）。
- 访问两模式：Console mode（管 PCX/装服务器，无音频）与 RDP（软电话实验必用）（p51）。

## 平台速览（方案沟通素材）

- 四套件：Setup/Network/Reports/Directory（本书只精讲 Directory 套件）；厚客户端 15 应用 + WBM 四应用（p4, p10, p34-38）。
- 双存储：MariaDB（SQL）+ LDAP；配置目录 o=nmc 与公司目录 o=directoryroot 两棵树靠链接缝合（p7, p67）。
- 版本兼容：OT R2.4-2.6.1 与 OXE R12.2-12.4 四版全兼容；OXE Purple R101.x 仅配 8770 R5.2；OXO/OCE R5.2-6.2 配 R5.1/R5.2（p9）。
- 虚拟化：ESXi 6.x/7.0/8.0、Hyper-V 2016/2019/2022、Nutanix AHV、AWS；虚拟化不收许可；sizing 用 Capacity Planning tool V3.0（p8）。

## 教材口径声明

- 全部实验密码/账号/网段/号码仅限实验环境（实验口径）；生产必须替换并做安全加固：全量换密、插件 properties 访问控制、复制管理器密码用 toolsOmniVista.exe 单独设置（p47, p407, p511）。
- 节点号公式示例自相矛盾（p95：1*100+2 书例写 101），按"百位=网络号、末两位=节点号"推断读法操作并现场验证（needs-review nr-01）。
- MSAD 插件强依赖 IE（信任站点/活动内容/active scripting，p414）：现代环境先实测，交付前置核查风险项（nr-06）。
- 目录复制不支持 LDAPS（p511/p514）：复制流量明文，加密合规场景需网络层方案（nr-07）。
- 生产化依据建议以 8770 官方 Installation/Administration Guide 为准——整理侧建议（批判章推导），非原书引用。
