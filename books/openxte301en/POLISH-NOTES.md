# POLISH-NOTES — openxte301en（全文中文化润色核对记录）

核对日期：2026-09-24
核对范围：`.cangjie/capabilities/cards/*.md`（13 张卡片）+ `book/overview.md` + `book/glossary.md`，共 15 份文件，全部逐字通读。

## 结论：修改 1 处

全书表达质量高，未发现"被配置为""允许……到……""使用……来进行……""respective"等机器翻译腔；唯一需要动手的是一处名词串断句。

## 修改清单

| # | 文件 | 卡片名 | 原文片段 | 改后片段 | 理由 |
|---|---|---|---|---|---|
| 1 | cards/ota-nomadic-ghost-z.md | Nomadic 移动模式与 Ghost Z 资源池 | "窄带 G.711u/a、G.729a、G.723 加宽带 G.722.2" | "窄带用 G.711u/a、G.729a、G.723，加宽带用 G.722.2" | 原句"……G.723 加宽带 G.722.2"两组编解码连写，易误读成"G.723 加宽带"；补"用"字并加逗号断句（对应"过长的名词串要断句"），编解码型号与档位事实未动 |

## 核对过但决定保留的边界情况（供后续复核参考）

| 文件 | 位置 | 原文片段 | 保留理由 |
|---|---|---|---|
| book/overview.md | 交付主线（11 站组织轴） | "实验 POD（RLAB）→ Nomadic 移动（蜂窝/VoIP）→ ……"（箭头链） | 章节路线图的组织轴体例，四本书 overview 一致；本行无表达问题，重排会破坏跨书一致性 |
| cards/ota-calendar-sync.md | E 段步骤 6 | "（locale/AM-PM/until 与 for the next hours）" | "until HH:mm""for the next hours"是产品实际展示字符串，属引用非残留 |
| cards/ota-desksharing.md | I 段 | "凭前缀 600 登录/601 登出加密码使用任意 DSS" | 动词短语紧凑但可解析，与全书"数字/英文混排"的紧凑风格一致，未达必改程度 |

## 红线遵守声明

- 仅做上述 1 处表达修改；数字、版本号、页码、IP、端口、菜单路径、命令、R 段英文引文、`#` 标题行、yaml 代码块均未触碰。

## 验收

- `python .cangjie/scan_dense.py books/openxte301en` → 零输出问题（仅 done 行）
- `python .cangjie/scan_blank.py books/openxte301en` → 零输出问题（仅 done 行）
