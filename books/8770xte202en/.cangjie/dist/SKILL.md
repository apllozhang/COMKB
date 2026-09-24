---
name: omnivista-directory
description: |
  OmniVista 8770 目录（Company Directory）交付与运营支持：OXE 节点注册同步、目录树与 PCX 自动创建、六类链接与改名语义、MSAD/Azure AD 身份管道、保密与访问级别、Click to Call、管理域委派、目录复制、LDIF 批量管道。适用于 8770 R5.2 目录套件的配置、选型、排障与方案落地问答； 其余套件、网络安全加固与生产凭据不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.omnivista-directory
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# OmniVista 8770 — Directory Administration (Participant's Guide, Edition 40) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 性能/计费/报表/设备管理等其余套件（本书仅一页级介绍，需引用对应教材 8770XTE200/201 等）
- 端口级安全加固与 LDAPS 替代加密方案（目录复制不支持 LDAPS，加密替代在书外）
- OXE 侧完整命令手册与语音中继/媒体质量问题（本 bundle 仅覆盖注册所需子集）
- RLAB/SIP 模拟器环境搭建（教学专用基础设施，仅作 Boundary 背景）
- 培训评估与证书流程（p559-565，非技术内容）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 双存储两棵树：配置目录（o=nmc）与公司目录（o=directoryroot）靠六类链接缝合；主链接是根（1:1、姓名+成本中心一致），姓名/名字只能从公司目录改，配置入口改会断链生成新人
2. 目录供给三通道：PCX 事件自动创建（实时，受全局三开关+节点前提+UID 构造约束）、OXE 同步、LDIF 批量管道（导入只增改不删除，删除靠 PurgeLdap 机制）
3. 保密与权限正交：条目保密四级 × 个人数据五种决定 Web 目录可见性（本人级别不放大他人可见性）；账户访问级别（两应用各五档）在 Security 应用按应用授予
4. Click to Call 五环链：DDI 翻译器 → ISDN 号构造（前缀+实体安装号+话机号）→ 前缀规则 → 属性关联 → STAP 放行；OXE SIP 话机全线不支持
5. 身份管道两通道：MSAD 一条映射+N 条规则（sn 不可删、电话只从 8770 写回、8770 新建/删除不回写 AD）；Azure AD 恒为主节点走 Graph API、不 provision OXE 用户
6. 运营三件：管理域切割可见性与管理权（双许可、默认关闭、本地管理员建不了域）；目录复制 1 主最多 4 从、只冗余目录不冗余服务器、断联超 7 天数据丢失须 LDIF 人工恢复
7. 实验环境口径：教材所有 IP/密码/号码为教学约定值（实验口径），生产必须替换；生产化依据建议以 8770 官方 Installation/Administration Guide 为准（整理侧建议，非原书引用）

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 注册 OmniPCX Enterprise 节点；OXE 同步失败排查；节点声明字段怎么填；register OXE node to 8770 | references/capabilities/ovdir-oxe-sync-ldap.md | references/capabilities/ovdir-auto-creation.md |
| 搭建公司目录树；配置 PCX 自动创建；同名员工 UID 冲突；automatic creation troubleshooting | references/capabilities/ovdir-auto-creation.md | references/capabilities/ovdir-oxe-sync-ldap.md、references/capabilities/ovdir-links-rename.md |
| 管理人员与话机链接；成本中心修改被拒绝；改名后链接断裂修复；4760 多主链迁移 | references/capabilities/ovdir-links-rename.md | references/capabilities/ovdir-auto-creation.md、references/capabilities/ovdir-ldif-tools.md |
| 对接 Active Directory 同步；属性映射与同步规则；AD 删人后 8770 行为；Azure AD Entra ID sync | references/capabilities/ovdir-msad-azure-pipelines.md | references/capabilities/ovdir-msad-plugin.md、references/capabilities/ovdir-ldif-tools.md |
| 交付网页目录点击外呼；ISDN 号没生成排查；配置拨号前缀规则；STAP associated station setup | references/capabilities/ovdir-click-to-call.md | references/capabilities/ovdir-oxe-sync-ldap.md |
| 配置目录保密级别；授予目录访问级别；匿名与认证可见性；web directory authentication | references/capabilities/ovdir-confidentiality.md | references/capabilities/ovdir-domains-delegation.md |
| 部署目录复制主从；复制不一致恢复；副本移除与属性集变更；directory replication setup | references/capabilities/ovdir-replication.md | references/capabilities/ovdir-ldif-tools.md、references/capabilities/ovdir-oxe-sync-ldap.md |
| 搭建多站点分域管理；本地管理员权限分组；配置委派与定制视图；management domain delegation | references/capabilities/ovdir-domains-delegation.md | references/capabilities/ovdir-confidentiality.md |
| 部署 MSAD 插件；AD 右键开户 OXE 用户；Meta profile 前置配置；MSAD plug-in provisioning | references/capabilities/ovdir-msad-plugin.md | references/capabilities/ovdir-msad-azure-pipelines.md |
| 目录数据备份与恢复；批量导入外部目录数据；外部删除跟随清理；LDIF batch pipeline | references/capabilities/ovdir-ldif-tools.md | references/capabilities/ovdir-replication.md |
| 目录属性显示名定制；Web 目录客户端界面定制；定制回退与恢复；dictionary customization | references/capabilities/ovdir-client-dictionary.md | references/capabilities/ovdir-confidentiality.md |
| 8770 套件与应用全景；版本兼容核对；虚拟化部署形态；8770 architecture overview | references/capabilities/ovdir-platform-basics.md | references/capabilities/ovdir-oxe-sync-ldap.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 需要生产凭据（adfexc/mtcl/AdminNmc 等）而客户未提供 → 停止使用教材实验值，转客户安全流程
- PCX 版本配对在 p9 兼容矩阵之外 → 指向官方最新兼容文档核实，不口头承诺
- 要求复制加密或 8770 整机高可用 → 声明"只冗余目录、LDAPS 不支持"边界，转架构评估
- 无 IE 环境部署 MSAD 插件 → 按 needs-review nr-06 标记风险，先实测再承诺
- LDIF 管道出现坏结构（p.conf 根名忘改） → 明确 dirmanag.exe 删 ABS 根的救援路径，禁止盲目重跑 go.bat
