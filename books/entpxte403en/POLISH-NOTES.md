# POLISH-NOTES — entpxte403en（全文中文化润色核对记录）

核对日期：2026-09-24
核对范围：`.cangjie/capabilities/cards/*.md`（13 张卡片）+ `book/overview.md` + `book/glossary.md`，共 15 份文件，全部逐字通读。

## 结论：修改 16 处（集中在 1 个混写词 + 1 个术语不一致 + 2 处局部生硬）

全书整体表达达标，但有成批的"零touch"中英混写生造词（机翻残留的典型形态）、"远程工人"直译与另外两处局部生硬，逐处清单如下。所有修改只动表达，型号、页码、端口、路径等事实零改动。

## 修改清单

### A. "零touch" → "零接触"（11 处）

"零touch"是 zero-touch 的半翻译生造词，中文工程文档通用表述为"零接触（部署）"。统一替换；osip-remote-workers.md 语言信号行同步改为"零接触 / zero touch"，保留英文关键词供检索。

| # | 文件 | 卡片名/位置 | 原文片段 | 改后片段 | 理由 |
|---|---|---|---|---|---|
| 1 | book/overview.md | 关键数字速览 | "EDS 零touch 四限制" | "EDS 零接触四限制" | 中英混写生造词改通用中文 |
| 2 | book/overview.md | 教材口径声明 | "EDS user manual（零touch）" | "EDS user manual（零接触）" | 同上 |
| 3 | book/glossary.md | EDS 词条 | "ALE 云端零touch 部署服务器（AWS 巴黎）" | "ALE 云端零接触部署服务器（AWS 巴黎）" | 同上，"零接触部署"为通行译法 |
| 4 | cards/osip-remote-workers.md | 远程办公方案与落地 · I 段方案矩阵 | "LAN↔WAN 搬迁、EDS 零touch" | "LAN↔WAN 搬迁、EDS 零接触" | 同上 |
| 5 | cards/osip-remote-workers.md | 同卡 · I 段话机两用例 | "②EDS 零touch——出厂 NOE 起步" | "②EDS 零接触——出厂 NOE 起步" | 同上 |
| 6 | cards/osip-remote-workers.md | 同卡 · A2 使用情境 | "话机寄到家零touch 开通" | "话机寄到家零接触开通" | 同上 |
| 7 | cards/osip-remote-workers.md | 同卡 · 语言信号 | "EDS / 零touch / zero touch /" | "EDS / 零接触 / zero touch /" | 中文信号词规范化，英文关键词保留 |
| 8 | cards/osip-remote-workers.md | 同卡 · E 段输入契约 | "用户家庭网络触发零touch 四限制" | "用户家庭网络触发零接触四限制" | 同上 |
| 9 | cards/osip-remote-workers.md | 同卡 · E 段步骤 2 | "零touch 四限制逐条问掉" | "零接触四限制逐条问掉" | 同上 |
| 10 | cards/osip-remote-workers.md | 同卡 · E 段步骤 6 | "零touch 话机在 EDS 建 Profile" | "零接触话机在 EDS 建 Profile" | 同上 |
| 11 | cards/osip-remote-workers.md | 同卡 · 判停点 | "零touch 直接失败" | "零接触直接失败" | 同上 |

### B. "远程工人" → "远程工作者"（3 处）

remote worker 的直译"远程工人"（"工人"易联想体力劳动者）不符合电信文档口吻；同书 osip-sip-features.md 已用"远程工作者"，按"术语稳定"原则向多数用法看齐。

| # | 文件 | 卡片名/位置 | 原文片段 | 改后片段 | 理由 |
|---|---|---|---|---|---|
| 12 | cards/osip-remote-workers.md | 远程办公方案与落地 · I 段原生加密 | "N4 起远程工人可开用户级加密，OXE 经 REGISTER Via 头里的 SBC IP 识别远程工人" | "……N4 起远程工作者可开用户级加密，OXE 经 REGISTER Via 头里的 SBC IP 识别远程工作者" | 直译腔 + 与 osip-sip-features.md 术语统一 |
| 13 | cards/osip-remote-workers.md | 同卡 · B 段边界 | "原生加密远程工人是 N4 新语义" | "原生加密远程工作者是 N4 新语义" | 同上 |

（12 号含同一行 2 处，合计 3 处替换。）

### C. 局部生硬断句（2 处）

| # | 文件 | 卡片名/位置 | 原文片段 | 改后片段 | 理由 |
|---|---|---|---|---|---|
| 14 | cards/osip-protocol-foundation.md | SIP 协议机理与 OXE SIP 架构 · I 段组件表 | "收终端注册并送位置服务器（租期 1800-86400s 钳制）" | "收终端注册并送位置服务器（租期钳制在 1800-86400s）" | "1800-86400s 钳制"是英文语序直译（clamp 1800-86400s），调整为中文动补语序；数值未动 |
| 15 | book/glossary.md | ALES-DUID 词条 | "OXE 以 分机号↔DUID 实现一号多机互斥" | "OXE 以分机号↔DUID 实现一号多机互斥" | 删"以"后多余空格，英文排版残留 |

（第 16 处即 A-7 的语言信号行，与 A 组合并计数；去重后实际独立改动点为：零touch 11 + 远程工人 3 + 断句 1 + 空格 1 = 16 处替换。）

## 核对过但决定保留的边界情况（供后续复核参考）

| 文件 | 位置 | 原文片段 | 保留理由 |
|---|---|---|---|
| book/overview.md | 交付主线（组织轴） | "环境与外线地基 → SIP 协议与 OXE 六组件 → ……"（箭头链） | 章节路线图组织轴体例，四本书一致，非表达问题 |
| 各卡 | "touch 混写"扫描命中 | OpenTouch、dmictouch、ictouch.0、opentouch.company.com、IP Touch | 产品名/文件名/协议名，红线不动 |
| cards/osip-sip-device-provisioning.md | I 段 | "话机高级菜单=123456"等紧凑等式 | 全书统一的信息压缩风格，语义无损 |

## 红线遵守声明

- 上述替换均为纯表达层：未动任何数字、页码（p52/p404 等）、端口（5261/8443 等）、版本号（N4/R101.1）、文件名（EDS user manual）、命令与 R 段英文引文；未改任何 `#` 标题行；未触碰 yaml 代码块与工具脚本。

## 验收

- `python .cangjie/scan_dense.py books/entpxte403en` → 零输出问题（仅 done 行）
- `python .cangjie/scan_blank.py books/entpxte403en` → 零输出问题（仅 done 行）
