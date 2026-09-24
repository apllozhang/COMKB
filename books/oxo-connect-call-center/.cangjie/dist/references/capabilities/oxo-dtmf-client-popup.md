# DTMF 客户码识别弹屏（OXO Connect）

## R — 原文依据

> "he is able to type a customer DTMF code (ex 035) allowing to generate a specific client information pop-up (Customer code=035) on the agent application"（p101）
> "ACD groups with code must be selected in the line parameters ... give the ''automatic screen pop up'' rights in the agent parameters"（p102）

出处：OXOCXTE107EN p101-102。

## I — 自述

让来电者"报暗号"换个性化服务。机制一句话：来电者在语音提示下输客户码（如 035#），码随呼叫到坐席席面，自动弹出客户资料。**三处前置缺一不可**：

1. Line parameters：给目标 ACD 组勾选客户码功能（不勾则引擎根本不收码）
2. 定制客户码提示音（默认标签 107.wav 系，告诉来电者"请输码"）
3. 坐席参数授予 "automatic screen pop up" 权限（有码无权照样不弹）

码与客户的对应关系维护在坐席席面的客户数据库里（与 Agent 应用能力互链）。

## A1 — 书中案例

**机制示例**（p101-102，厂商讲义）：来电者听提示输 035# → 坐席席面弹出 "Customer code=035" 的客户信息。原书只给机制与三处前置，未含端到端实验步骤（已标注）。

## A2 — 未来触发

使用情境：VIP 客户来电自动带出资料；客户输会员号/工单号直接定位；"弹屏不出来"排查。

语言信号：输码 / 客户码 / customer code / DTMF / 弹屏 / pop up / 识别客户。

与相邻能力区分：按主叫号码自动匹配的弹屏（无输码）→ Agent 应用能力；本能力专管"输码触发"链路。

## E — 可执行步骤

输入契约：客户码表（码 ↔ 客户/业务）、提示音话术。缺码表先与业务方确认。

1. 勾组：OMC Line parameters → 选中启用客户码的 ACD 组。完成标准：组已启用收码
2. 提示音：定制 customer code announce（107.wav 系）。完成标准：实呼可听提示
3. 授权：Agent 参数 → 授 "automatic screen pop up" 权限。完成标准：权限已勾
4. 端到端验证：呼入 → 输 035# → 席面弹出 Customer code=035。完成标准：弹屏出现且资料正确

判停点：三处配齐仍不弹 → 查码表维护（坐席客户库内有无该码条目）与提示音是否真在播（端到端实测原书未给，逐段定位）。

输出契约：三处配置核对清单 + 端到端验证记录。

## B — 边界

- 原书无端到端实验——首例交付留足验证时间
- 码位数/格式与超时重输行为原书未说明，方案设计时与客户自定并写入交付文档
- 弹屏来源二分：客户库按 CLI 匹配（Agent 应用）vs DTMF 码触发（本能力）——排查先分清是哪一路
