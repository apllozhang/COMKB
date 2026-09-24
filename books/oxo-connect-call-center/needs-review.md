# needs-review.md — 待核查事项（不编译为 active 能力）

| id | 事项 | 来源 | 具体缺口 | 补齐途径 | 影响 |
|---|---|---|---|---|---|
| nr-01 | 组间溢出（Group overflow）的定时器配置入口 | f19 / p96 | 原文仅给 10s 定时器与行为示意图，配置菜单与可调范围未写明 | 查 OXO Connect Expert 文档或实机核对 ACD-SCR Services 菜单 | 溢出能力暂不独立，机制描述并入队列能力 Boundary |
| nr-02 | 话机 ACD 状态码"属于/不属于开放组"变体符号 | f22 / p122 | 纯文本提取两行均印作 "1:01"，视觉差异（符号/格式）丢失 | 实机 Premium 8/9 系列话机核对 PDF 原图 | 主码（1:01 / 1:01+ / 1-00）已 verified，仅变体存疑 |
| nr-03 | ACDAutoLog 的写入路径 | f21 / p123 | 已知条目名与取值（01/00），写入菜单未给 | 实机查系统寻址（System Miscellaneous/Addressing） | 已作 Boundary 标注，不阻塞 |
| nr-04 | Multi-Secretary 模式激活控件名 | f24 / p141 | General tab 截图页，控件名未提取 | 实机核对 OMC/ACD Setup/General | 已作 Boundary 标注，不阻塞 |
| nr-05 | .wav 语音格式参数 | f30 / p105 | 采样率/编码以截图呈现 | 核对 PDF 原图或 ALE 官方语音规格 | 已作 Boundary 标注，不阻塞 |
| nr-06 | 三个缩写全称：MLAA / OMC / MMC | 术语提取器 | 书中未展开全称，不编造 | 查 ALE 术语表或产品文档 | 词典中标注"全称待确认" |
| nr-07 | OCR 存疑项 | principle 提取器 5 项 | p122 状态码符号（同 nr-02）、wav 格式（同 nr-05）、103-106 语音编号对应关系、部分参数默认值/可配范围 | 核对 PDF 原图 | 合并跟踪；涉及语音编号者影响 f30 精度 |
| nr-08 | 溢出前等待开关 "Waiting begins before overflow time delay" | f29 / p190 | 仅提开关存在，行为未展开 | Expert 文档 | 统计阈值口径 Boundary |

## 处置原则

- nr-01 为唯一阻塞级缺口（对应单元 f19 暂不晋级，机制描述进队列能力 Boundary）。
- nr-02 ~ nr-08 均为"实机/原图可核"的精度问题，相关能力已带 Boundary 交付，不影响使用；后续有 RLAB 环境时一次性核完。
