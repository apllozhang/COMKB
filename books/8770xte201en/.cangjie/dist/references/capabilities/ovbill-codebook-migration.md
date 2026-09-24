# Code Book 导出与导入（运营商配置迁移、.itl 节点修复、EFFECT_DATE 新周期）

## R — 原文依据

> "@ is the header character. A line beginning with this symbol gives the name of the fields used in the file • Only one header line per file and it is mandatory in all except information file ... % is the comment character"（p230）
> "Field Node must correspond to the name of the PCX declared in Configuration application ... Node name must be configured before importing the code book"（p233）
> "A second export is required to save the complete carrier configuration"（p236）
> "ALL MODIFICATIONS ON TELECOM 2 CODE BOOK FILES MUST BE APPLIED FROM THE DOCUMENTS DIRECTORY AND NOT FROM THE NAS DRIVE."（p246）

出处：8770XTE201EN p226-250。

## I — 自述

Code Book 是运营商配置的文本文件集，用于跨服务器迁移与存档：

- 十种文件：.inf 总信息（引用其余文件，含 VERSION/CARRIER_NAME/EFFECT_DATE）、.rgn 区域与前缀、.trf 资费、.dir 方向、.cal 特定日、.ccn 城市国家名、.adj 调整系数、.fct ISDN 服务费、.itl 安装文件（主叫区内 PCX 清单）、.trg 主叫区内中继组
- 格式规则三条：@行=表头（.inf 除外，每文件仅一行且必须）；Tab 分隔字段（要默认值就留空跳 Tab）；%行=注释
- 导入按 .inf 索引重建运营商；.itl 的 Node 必须与目标机 Configuration 里声明的 PCX 名一致，否则导入"部分成功"（区域/资费建了、方向建不出来）更具迷惑性
- 生命周期语义：改 .inf 的 EFFECT_DATE 再导入=同运营商下新增 Period（旧周期自动封口），是价目随政策演进的正规做法
- 备份规则：一次导出≠完整备份，第二次导出才完整；一切修改在 Documents 副本上做，不动共享盘原件

## A1 — 书中案例

**导出与重导入**（p238-242）：

1. Carriers 页签选 Telecom 1 > Period > 右键 Export，存 Documents 下新建文件夹，File Name=Telecom1.inf
2. 删除运营商 Telecom 1
3. 右键 Carrier > Import，选 Telecom1.inf，运营商重建成功

**EFFECT_DATE 演进**（p243-244）：

1. Notepad++ 编辑 Telecom1.inf，把 EFFECT_DATE 改为 20220101
2. 再次 Import，结果为同一运营商下新增一个 Period（价目演进的正规做法）

**跨服务器迁移与 .itl 修复**（p245-250）：

1. 从共享盘复制 Telecom2_7x 到 Documents（修改只动副本）
2. 直接 Import Telecom2.inf 报错：方向建不出来
3. 检查发现 Telecom2.itl 的 Node 名是 oxe9，与本机声明的 oxe 不一致
4. 把 Node 名改为 oxe，删除已导入的 Telecom 2，重新 Import 成功

## A2 — 未来触发

使用情境：运营商配置从测试机搬到生产机；价目政策换版怎么并存；导入报错但部分对象建出来了；配置备份怎么做才完整；.itl 是什么。

语言信号：Code Book / codebook / .inf / .itl / .rgn / .trf / .dir / EFFECT_DATE / 导出 / 导入 / export / import / Node 名 / oxe9 / Period / 价目迁移 / 运营商备份。

与相邻能力区分：建模本体（对象怎么配）→ 资费建模能力；本卡只管配置的搬移与存档形态。

## E — 可执行步骤

输入契约：源机运营商可导出、目标机已声明同名结构的 PCX。目标机节点名未知 → 判停先到 Configuration 核对，不改名直接导必然踩 .itl 坑。

1. 源机导出两次到 Documents 文件夹（第二次才完整）。完成标准：文件夹含 .inf 与全部关联文件
2. 传输到目标机 Documents（不占共享盘原件）。完成标准：副本可编辑
3. 用文本编辑器改 .itl 的 Node 为目标机声明名。完成标准：Node 与 Configuration 一致
4. 价目换版场景：改 .inf 的 EFFECT_DATE 后导入（结果=新增 Period）。完成标准：周期数符合预期
5. Import 并验证区域/资费/方向三层全部生成。完成标准：方向列表非空且与源一致

判停点：

- 导入"成功"但方向缺失 → 十有八九是 .itl 的 Node 不匹配，改后删除半成品重导
- 期望"修正原配置"却出现两个周期 → EFFECT_DATE 导入语义是新增不是覆盖，删多余周期前先确认无票据引用
- 共享盘原件只读使用，任何编辑都先复制到本地 Documents

输出契约：迁移文件包清单 + .itl 修改记录 + 导入验证结论（区域/资费/方向计数对照）。

## B — 边界

- .itl 的 Node 匹配的是"目标机"声明名，跨服务器前必须先改（p233/p247）
- 导出需两次才完整（p236），单次导出作备份不完整
- 文件格式为 @表头/Tab 分隔/%注释（p230）；字段顺序与默认值写法照原文样例，不自创格式
- 本卡不覆盖资费对象怎么建模（资费建模能力），也不覆盖导入后的成本重算触发（同上，属建模卡 B）
