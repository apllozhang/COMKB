# ACR 多语言语音引导与语言偏好分发（40 语种映射、判定链、语言成本）

## R — 原文依据

> "40 messages maximum per multi-language guide … Voice guides 700 language 1: 1000 language 2: 1001 … language 40: 1039"（p215）
> "The language defined in the call profile has the highest priority … If no language is defined at call profile level, the ACR pilot language is used"（p216）
> "The value of the preference associated to each language will determine which language will be above the other when broadcasting guides or when choosing the agent who will handle the call (value included between 1 and 7, 1 for the highest priority language)"（p229）
> "Remind that an agent is not obliged to have all language skills defined in the call profile: 1 language skill is enough"（p214）

出处：OTCCXTE150EN p212-229。

## I — 自述

多语言引导与选人同源：播报语言和坐席语言成本都由呼叫档案里的语言技能决定。

结构三段：

1. **承载**：一个多语言引导（Function=Multi-language message）映射最多 40 条消息——语言 1 对应消息 1000、语言 2 对应 1001、依次到语言 40 对应 1039；存 OXE 闪存卡；Start=YES 加 Backup Tone
2. **判定**：播报语言取脚本所用呼叫档案里的语言（多语言时按 preference，值 1-7、1 最优先）；档案无语言则退 ACR Pilot 语言
3. **选人**：坐席无需具备档案全部语言，命中 1 门语言技能即可入选；ASM 按语言偏好加技能级别算 ISM 成本排序

可用引导类型：问候、等待、重定向、封锁、转发五类都可挂多语言引导。

配置与排障要点：

- 多语言引导在 System/Voice Guides 建；消息在 Dynamic Voice Guides 分配后用 *88 录音、*66 测音
- 统计 Pilot 自带的呈现引导会先于 ACR Pilot 问候引导播出，导致语言判定失真——必须清掉所有统计 Pilot 的呈现引导，问候只留 ACR Pilot 一处
- 偏好值仅对语言类技能有意义；档案里同一语言技能的偏好决定播报与选人两个场景的优先

## A1 — 书中案例

**多语言实验（c09）**：

1. 动态引导分配建消息 1000（法语欢迎）、1001（英语欢迎），录音并激活
2. System/Voice Guides 建 740 号引导：Function=Multi-language message、Start=YES、Backup Tone 56
3. 加两条映射：French 对应 1000、English 对应 1001
4. 建呼叫档案 3：Language 域 French 技能 Level 5 加 Insurance 域 Car 技能 Level 9
5. 建统计 Pilot 31653（French_Car）指 ACR Pilot，档案用 3
6. 清掉所有统计 Pilot 的呈现引导，问候引导只留 ACR Pilot
7. 坐席 31501 加 French Level 9（可用 Skill Matrix 批量）；脚本用 ISM 挂 ACR Pilot
8. 对照测试：呼英语入口播英语、呼法语入口播法语；档案内法语偏好 2、英语偏好 1 时播英语

## A2 — 未来触发

使用情境：多语言呼叫中心按客户语言播报；坐席按语言技能分配；语言判定不符合预期；引导语言播错。

语言信号：多语言 / Multi-language / Voice Guide / 语言偏好 / preference / 语言技能 / French / English / 呈现引导 / Presentation Guide / Backup Tone / 40 语种。

与相邻能力区分：档案与技能体系本身，见 CCD 矩阵地基能力；语言标签从哪来，见 Call Tag 卡（路由）；ISM 成本与混跑，见 综合规则组合能力。

## E — 可执行步骤

输入契约：语种清单与偏好次序、各语种录音内容、坐席语言技能数据。录音制作是环境操作，先备齐。

1. 动态引导分配建各语种消息并录音激活。完成标准：消息号可播
2. System/Voice Guides 建多语言引导：Function 选 Multi-language message、Start=YES、Backup Tone。完成标准：引导保存
3. 加语言到消息映射（最多 40 条）。完成标准：每语种有对应消息
4. 呼叫档案配语言技能与偏好（1-7，1 最高）。完成标准：档案可指派到入口
5. 清掉所有统计 Pilot 的呈现引导，问候只留 ACR Pilot。完成标准：无前置引导干扰
6. 坐席配语言技能（每语种一门即可命中）。完成标准：语言坐席池就位
7. 对照测试各语言入口：核播报语言与选中坐席。完成标准：判定链行为正确

判停点：

- 播报语言不对 → 按判定链查：档案语言偏好、档案无语言时的 Pilot 语言、统计 Pilot 残留呈现引导
- 坐席没被语言呼叫选中 → 核坐席是否至少有 1 门档案语言技能、级别与偏好
- 引导只播默认语言 → 核 Function 是否真为 Multi-language message 及映射行

输出契约：多语言引导映射表 + 语言档案与坐席技能 + 判定链验证记录。

## B — 边界

- 40 语种/引导、偏好 1-7 为原书 Issue 01 口径，细则以 Feature List 为准
- 录音内容制作与多语言 TTS 原书不涉及
- 语言技能只需 1 门命中即可入选（p214），不要求全语言——方案沟通时常见误解
- 多语言引导存 OXE 闪存卡，容量规划在书外
- ISM 成本计算含语言偏好的公式原书只给示例（成本 0/3），未给全貌
