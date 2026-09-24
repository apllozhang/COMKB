# 计费机密控制三道闸（掩码档案、解密权限、可见域）

## R — 原文依据

> "Default profile cannot be renamed or deleted • However, you can reset masked digit to 0 to render it inactive • Two additional call categories: masked and unmasked group used systematically for grouped reports"（p300）
> "BY DEFAULT, THE GENERATION OF A REPORT WITHOUT MASK IS NOT ALLOWED. TO USE UNMASKING OPERATION, IT IS NECESSARY TO CREATE AN 8770 LOGIN WHICH IS MEMBER OF THE GROUP 'MASK DATA ACCESS'."（p314）
> "In case of grouped report, the server ignores the mask profiles applied to the organization: it only takes into account the profile named Default"（p310）
> "Visibility domain — Yes. To interrupt accounting access control and restrictions, deselect this option. — You must restart the Accounting/traffic/VoIP application"（p351）

出处：8770XTE201EN p296-357。

## I — 自述

机密性三道闸按"遮显示 → 管解密 → 裁可见"分层，全部只作用于 8770 侧显示与报表，不删数据：

- 掩码档案（Mask profile）：按呼叫类别（Personal/Project/Professional/Guest）定义"显示前 n 位、遮蔽后 n 位"与 PIN/成本/地名/时长/日期开关；Default 档案挂组织根、不可改名删除（遮蔽位数清 0 即等效停用）；档案随组织树继承（Inherited Masks），按条目可取消继承单独指定
- 显示位数优先于遮蔽位数："显示 4 位"的语义是至少显示前 4 位，号码不足 4 位全显
- grouped 报表例外：无视组织树上的一切档案，只认 Default 档案的 Masked group/Unmasked group 两个类别——合规验收两型报表都要测
- 解密权限：默认禁止无掩码报表；须建 8770 账号加入 "Mask data access" 组，任何人生成 w/o mask 时索要该组成员口令；解密程度仍受各档案 Unmasked 类别限制；组成员变更必须关闭并重开 Reports 应用才生效
- 可见域（Accounting domain）：功能开关开启后，管理员未配域只见光杆根节点；域挂组织树节点、按父继承（不必逐级配）；管理员在 Security > Individual 配域（可 Add a value 多域）；群组上的域配置不被采纳，只认用户级；AdminNmc 配根域即全域可见
- OXE 侧已遮蔽的号码（如 029845----）8770 任何手段无法还原——遮蔽职责分工在票据源头

## A1 — 书中案例

**掩码档案与解密**（p304-320）：

1. Organization 页签 Masks 图标：复制 Default 为 "Copy of Default"——masking 遮后 4 位+时长+成本+日期，unmasking 遮后 1 位+时长+日期
2. 新建空档案 "TSS Profile"：masking 遮后 5 位、unmasking 完整显示被叫号
3. 根 Alcatel 的 Properties 挂 Copy of Default（全树继承）；查 Training 确认显示 Inherited Masks
4. TSS 成本中心取消继承，单独挂 TSS Profile
5. Reports 里复制预定义 Duration by station 到个人目录，分别生成 Training/TSS 掩码报告对比遮蔽差异
6. Security 建账号 unmasking（口令实验口径 superuser）并加入 Mask data access 组；先关闭 Reports 应用
7. 右键报告定义 > Generate report w/o mask，输入组成员口令生成解密版，对比差异
8. 认知点：TSS 记录里 029845---- 形态号码是 OXE 侧遮蔽，8770 无法还原

**可见域**（p348-357）：

1. Security 建管理员 AdminBrest、AdminCostCenter 并入 Accounting experts 组（口令均实验口径）
2. AccountingParameters 的 Visibility domain=Yes，重启计费应用——出现"未配域，仅根可见"警告
3. 根 Properties 配域 Alcatel；AdminNmc 在 Individual 配根域后重启，全域可见
4. Brest level 配域 Brest；MKT/Training 成本中心各配同名域（子节点无域则继承父域）
5. AdminBrest 配域 Brest；AdminCostCenter 配 Training 后右键 Add a value 再加 MKT
6. 分别登录验证：两账号组织树按域裁剪

## A2 — 未来触发

使用情境：合规要求对普通管理员遮蔽成本/号码；谁有权看完整号码；汇总报表为什么没按子树遮蔽；多公司共享一台 PCX 怎么隔离视图；开了可见域后"数据全丢了"；解密账号怎么建。

语言信号：掩码 / mask profile / Default 档案 / 遮蔽 / 解密 / unmask / Mask data access / grouped 报表 / 机密 / 可见域 / visibility domain / Accounting domain / AdminBrest / AdminNmc / 域继承。

与相邻能力区分：组织树结构本身属组织成本归属能力；报告生成动作属报表能力；OXE 侧出票遮蔽参数属票据管道能力。

## E — 可执行步骤

输入契约：组织树已搭好；遮蔽策略与合规口径已与客户确认。策略未定 → 判停先拿合规要求。

1. 建掩码档案（复制 Default 起步），按类别定显示/遮蔽位数与字段开关。完成标准：预览校验通过
2. 根挂默认档案，按条目取消继承做差异化覆盖。完成标准：Records 页签遮蔽形态符合策略
3. 建解密账号入 Mask data access 组，关闭并重开 Reports 应用。完成标准：w/o mask 生成时弹口令框
4. 开 Visibility domain 并重启计费应用。完成标准：接受"仅根可见"警告
5. 根域 + AdminNmc 根域 + 子节点域按继承配。完成标准：各节点域名正确
6. 给各管理员 Individual 配域（多域用 Add a value）。完成标准：分账号登录视图按域裁剪
7. 合规验收：详细与 grouped 两型报表分别验证遮蔽口径。完成标准：两种报表均符合策略

判停点：

- grouped 报表遮蔽与子树档案不符 → 设计行为（只认 Default 的两个 group 类别），调整 Default 档案而非反复改子树
- 开域后整树只剩根 → 先配根域与 AdminNmc 域再重启应用，不是数据丢失
- 改了组成员解密不生效 → 必须关闭 Reports 应用后重开
- 号码在 OXE 侧已遮蔽（横杠形态）→ 8770 无法还原，回 OXE 检查出票参数

输出契约：掩码档案配置表 + 解密账号与组清单 + 域分配矩阵（管理员到域名）+ 双型报表验收记录。

## B — 边界

- 口令治理（谁持有 Mask data access 口令、是否轮换）书内不论，交付须自行约定；书内口令均为实验口径
- 解密后的显示仍受各档案 Unmasked 类别限制（如 Default 档案解密后仍遮 2 位，p306/p318）
- "开启可见域必须重启计费应用"与"群组域无效"是两条硬规则（p351/p355）
- 书内成本中心名 MKT 在部分章节写作 Marketing（见 needs-review nr-05），机制不受影响
- 掩码只影响显示；导出文件与数据库内仍是全量数据，合规评审要覆盖导出链路（原书未展开，属边界声明）
