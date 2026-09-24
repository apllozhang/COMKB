# ACD 语音提示定制（OXO Connect）

## R — 原文依据

> "Respect the assignments 101.wav = welcome message, 102.wav = waiting message, etc."（p136）
> "Customer code announce 107.wav 207.wav 307.wav 407.wav 507.wav 607.wav 707.wav 807.wav"（p104）
> "Switch the Mode option to Transfer (1) • Select the prompts you want to download (2) • Define the directory path (3) • Load the new prompts (4)"（p105）

出处：OXOCXTE107EN p104-105（上传与编号）、p135-136（多秘书话术示例）、p76（全组下载陷阱）。

## I — 自述

ACD 每组最多 6 条语音提示，按**固定 wav 编号**管理：

1. **编号对照**：101=欢迎语、102=等待语，以此类推；客户码提示为 x07 系列（组 1-8 → 107-807.wav）
2. **制作两条路**：
   - 路径 A：话机 MMC 会话直接录（8/9 系列：Attendant session/Expert/Voice/ACD）
   - 路径 B：PC 制作 wav，再走 OMC 四步上传（Mode 切 Transfer、勾选 prompts、指定目录、Load）
3. **著名陷阱**：点 "Default messages" 会向**所有组**下载默认语音——只需部分组的要点列号排除

医生场景的逐条话术（"Doctor 1 is busy please wait"…）是标准定制样例（p135）。

## A1 — 书中案例

**多秘书语音定制**（p135-136，厂商实验）：组 1-3 定制医生场景——欢迎语 "Welcome to Doctor's 1 Office"、等待语 "Doctor 1 is busy please wait"、繁忙语、无法接听语、关闭语 "Doctor 1's office is currently closed"、长等待提示。

按编号命名 wav，OMC 四步上传或话机 MMC 逐条录制。

## A2 — 未来触发

使用情境：换欢迎语/等待语；本地语言话术；客户码提示音更换；"提示音怎么还是旧的"。

语言信号：欢迎语 / 提示音 / 录音 / voice prompt / 101.wav / 换语音 / 定制播报。

与相邻能力区分：提示音的**播放时机与逻辑**（何时播欢迎/等待）→ 六场景与队列能力；本能力只管"音频文件的制作与上传"。

## E — 可执行步骤

输入契约：各组话术文本（逐条对应提示类型）、录好的 wav 文件（编号命名）。缺话术先与客户确认文案。

1. 对照编号：101=欢迎、102=等待……客户码=x07.wav。完成标准：每条音频命名正确
2. 制作：路径 A 话机 MMC 逐组录；路径 B PC 制作 wav 备妥目录。完成标准：音频文件齐
3. OMC 上传四步：Transfer → 勾选 → 目录 → Load。完成标准：上传成功
4. 陷阱规避：Default messages 会广播全组——点列号排除不需要的组。完成标准：未误覆盖
5. 实呼验证：逐组触发各提示类型。完成标准：全部听到新版语音

输出契约：编号-话术对照表 + 上传记录 + 实呼验证结果。

## B — 边界

- wav 采样率/编码参数原书为截图未提取（nr-05/nr-07）——格式不符上传失败或无声时，对照 PDF 原图核格式，不要试错
- 提示音播放时机由场景逻辑决定（六场景/队列能力），改编号对应前先理解时机
- "Default messages 全组广播"反着用：新组上线恰好一次配齐默认音
- 组容量 6 条/组（p28）；话术超长截断行为原书未说明，录制后实呼试听为准
