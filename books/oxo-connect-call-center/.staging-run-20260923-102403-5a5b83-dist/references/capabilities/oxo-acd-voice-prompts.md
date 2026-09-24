# ACD 语音提示定制（OXO Connect）

## R — 原文依据

> "Respect the assignments 101.wav = welcome message, 102.wav = waiting message, etc."（p136）
> "Customer code announce 107.wav 207.wav 307.wav 407.wav 507.wav 607.wav 707.wav 807.wav"（p104）
> "Switch the Mode option to Transfer (1) • Select the prompts you want to download (2) • Define the directory path (3) • Load the new prompts (4)"（p105）

出处：OXOCXTE107EN p104-105（上传与编号）、p135-136（多秘书场景话术示例）、p76（全组下载陷阱）。

## I — 自述

ACD 每组最多 6 条语音提示，用固定 wav 编号管理：101=欢迎语、102=等待语，依此类推；客户码提示是 x07 系列（组 1-8 对应 107-807.wav）。做语音两条路：话机上直接录（8/9 系列 MMC 会话：Attendant session/Expert/Voice/ACD），或 PC 制作 wav 后经 OMC 四步上传（Mode 切 Transfer → 勾选要下的 prompts → 指定目录 → Load）。上传有个著名陷阱：点 "Default messages" 会向**所有组**下载默认语音，只需部分组的要点列号排除。医生的个性化话术（"Doctor 1 is busy please wait…"）是标准的逐条定制样例。

## A1 — 书中案例

**多秘书语音定制**（p135-136，厂商实验）：为组 1-3 定制医生场景语音——欢迎语 "Welcome to Doctor's 1 Office"、等待语 "Doctor 1 is busy please wait"、繁忙语、无法接听语、关闭语 "Doctor 1's office is currently closed"、长等待提示；按编号命名 wav 后走 OMC 四步上传，或在话机 MMC 会话（Menu/Operator/PASSWORD OP/Expert/Voice/ACD/ACD Group 1 to 3/Welcome...）逐条录制。

## A2 — 未来触发

使用情境：换欢迎语/等待语；本地语言话术；客户码提示音更换；"提示音怎么还是旧的"。
语言信号：欢迎语 / 提示音 / 录音 / voice prompt / 101.wav / 换语音 / 定制播报。

与相邻能力区分：提示音的**播放时机与逻辑**（何时播欢迎语/等待语）→ 六场景与队列能力；本能力只管"音频文件的制作与上传"。

## E — 可执行步骤

输入契约：各组话术文本（逐条对应提示类型）、录好的 wav 文件（编号命名）。缺话术先与客户确认文案。

1. 对照编号：101=欢迎语、102=等待语……客户码提示=x07.wav（组 1-8 → 107-807）。完成标准：每条音频命名正确。
2. 制作：路径 A——8/9 系列话机 MMC 会话录制（Attendant session/Expert/Voice/ACD 逐组录）；路径 B——PC 制作 wav（格式要求见 Boundary）后备妥目录。完成标准：音频文件齐。
3. OMC 上传四步：Mode 切 Transfer → 勾选要下载的 prompts → 指定定制文件目录 → Load。完成标准：上传成功提示。
4. 陷阱规避：点 "Default messages" 会向全部 ACD 组下载默认语音——只需个别组的，点列号排除其他组。完成标准：未误覆盖无关组。
5. 实呼验证：逐组触发各提示类型（欢迎/等待/劝漏/关闭/客户码），确认音色与内容正确。完成标准：全部听到新版语音。

输出契约：编号-话术对照表 + 上传记录 + 实呼验证结果。

## B — 边界

- wav 的采样率/编码参数原书为截图、文字未提取（needs-review nr-05/nr-07）——格式不符上传失败或无声时，先对照 PDF 原图核格式，不要试错。
- 提示音何时播放由场景逻辑决定（六场景/队列能力），改编号对应关系前先理解播放时机。
- "Default messages 全组广播"陷阱（p76）：新组上线只想要默认音时反着用——它恰好帮你一次配齐。
- 组容量 6 条提示/组（p28）；话术超长会被截断的原书口径未说明，录制后实呼试听为准。
