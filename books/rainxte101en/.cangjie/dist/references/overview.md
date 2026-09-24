# Book Overview（参考区）— Rainbow Hub

> 供能力卡引用的背景参考；源自 references.md 落位。

## 公司搭建七步主线（交付组织轴）

创建公司 → 分配 Voice 订阅 → 创建 Cloud PBX → 分配公网号码 → 创建物理 SIP 话机 → 创建成员（登录/号码/订阅）→ 功能管理（群组/欢迎服务/IVR 等）（p51）。步骤 1-5 为 BP 专属动作，6-7 起客户管理员可做；声明 Cloud PBX 前公司必须至少有一条 Voice Business 或 Voice Enterprise 订阅（p75）。

## 产品线定位（选型第一步）

- 两条产品线：混合云（连客户已有 OXO/OXE，订阅名 Business/Enterprise/Attendant）与 Rainbow Hub（全云托管，订阅名带 Voice 前缀、多 Voice Phone 档）（p6）。
- Hub 全景：云侧四大区块（SIP 运营商接入/协作服务/话机零接触供应/话务与欢迎服务）；客户站点只剩远程与移动工作者，无需 VPN、无需 SBC（p7）。
- 本 bundle 只覆盖 Hub 线；混合云接入（WebRTC 网关/OMC/OXO）属 RAINXTE001EN 语系。

## 实验环境（RLAB，仅 Boundary 背景）

- 每学员一个 POD 号（1-6，特殊 8）对应一家训练公司 Client-PX；BP 账号 bpX.rv1@ale-training.com（密码问讲师）；4 名成员 alice/bob/carol/dave X（内线 101-104、公网号 02982967X1-X4），公司号段 02982967X0-X9（X0 主号）（p17-18，实验口径）。
- 实验密码口径：成员 Superuser-P*、培训邮箱 mail44.lwspanel.com 为 PasswordP*；平台邮件可能被判 SPAM（p191-192，实验口径）。
- MicroSIP 公网模拟：每 POD 两个预配软话机，公网号规则 332982900P1/331409500P1/336050400P1/442056700P1（本地/国内/移动/国际，p22）；模拟器不能按公网号呼本公司成员；训后必须删除（p13/p20）。
- RLAB 远程实验室（可选，学员 PC 跑不了 MicroSIP 时）：Client1 192.168.1.10/24、网关 192.168.1.254、DNS 192.168.1.250、NAS 12.0.0.2（p27-34，实验口径）。
- 培训订阅口径：每公司仅 4 条 Voice Enterprise MONTHLY、禁用 1/3/5 年预付（p17/p68/p74 三处警告）；生产预付是正常计费方式（p65）。

## 平台速览（方案沟通素材）

- 合规四件套：GDPR、ALE ISO 27001、欧洲托管（面向欧洲客户）、不受 CLOUD Act/US PATRIOT Act 约束（p5）。
- 订阅 8 行：Voice Phone / Voice Business / Voice Enterprise / Voice Attendant / Voice Enterprise Dial-In Pack / Rainbow Room / Rainbow Alert / CRM Connect（p67）；电话服务硬门槛：成员必须持 Voice 档订阅才能配号（p66/p194）。
- 拓扑硬约束：一公司一 Cloud PBX、一 PBX 一条外部 SIP trunk、通道与线数无上限（p78）；多站点也是一台（p92）。
- 话务参数锚点：组 50 人、轮转 10 秒、队列溢出 10-900 秒、监督 5 页签/30 人/5 组、IVR 3 级无许可、录音 2 个月、删除宽限 10 天（p212/p215/p224/p266/p231/p176）。
- 终端供给三等：ALE 原生（Myriad/DECT，zero-touch）> 入门 ALE-2 > 第三方 Generic SIP（手工、无 RCC、ALE 不为大规模兜底）（p106, p116-121）。
- 端口锚点：TCP 5061（SIP over TLS）、TCP 443、UDP 30000-44999（SRTP）、UDP 53/123、TCP 22（p136）；全集以 Network Requirements 文章为准（p37）。

## 教材口径声明

- 全部实验账号/密码/号段/网段仅限实验环境；生产必须替换（原书明文实验值遍布正文，引用一律标"实验口径"）。
- 生产化边界四文档：Rainbow Network Requirements 文章与 PDF（网络数值）、Features List（订阅功能矩阵）、TBE099（话音服务/CDR）、TBE127（DECT 方案）——均为原书指定权威来源。
- 跨书差异点（引用时显式呈现）：Hub 订阅带 Voice 前缀且多 Voice Phone 档；BP 专属四项（混合云教材为两项）；SR 认证科目为 "certified on Rainbow Hub"（混合云为 "certified on Rainbow"）；MyPortal Product Category=Rainbow Hub。
- 版本敏感点：Sprint 170/Ed16 界面口径；LDAP 的 Exchange 在场同步为 161 版前功能等价回归（p179）；webadmin 设备日志要求固件 ≥2.14.22（p144）。
