# DECT 无线覆盖勘测（RSSI 门槛 / SSK / survey mode）

## R — 原文依据

> "Rs is a distance corresponding to a RSSI level for satisfactory voice quality: -70 dBm (for easy coverage) - 60dBm (for tricky coverage)"（p207）
> "-70 dB Minimum RSSI level between and ALE DECT handset and a base station ... Site with no coverage problem(s) = Easy"（p208）
> "-80 dB Zone of quality for DAP synchronization ... Minimum RSSI level between the base stations"（p210）
> "This mode is intended for debugging purpose and shall not be used for normal end user operation (while active, this mode can interfere with other features of the phone). In this mode, battery autonomy is reduced."（p216）

出处：DECTXTE200EN p204-217。

## I — 自述

覆盖勘测的三个门槛数字与一个调试工具：

1. **RSSI 门槛**：手机-基站话音质量门槛 -70dBm（容易场景：写字楼/仓库）、-60dBm（金属困难场景：厂房/洁净室）；基站-基站空中同步门槛 -80dBm。勘测时以对应门槛画覆盖边界。
2. **SSK（Site Survey Kit）**：官方勘测套件（TDM DECT/IP-xBS/IP DECT 通用）：专用 8378 xBS 两台、8dBi 天线、充电宝供电、2×8242 勘测手机、拉杆三脚架（3BN67191AA）等。
3. **survey mode**：手机菜单密钥 *7378423*（助记 *service*）激活，屏幕顶部 1/3 常驻显示 RSSI/基站列表/RFPI（Vol- 键）。按键语义：长按 *=慢/快测量、长按 #=No Lock/Lock to base、侧键=冻结/隐藏/恢复。

三个运营提醒（p216）：开启后常驻（重启前不消失）、激活期间干扰手机其他功能、续航明显下降——勘测机与交付机分开管理，勘测完显式 Off。

## A1 — 书中案例

**勘测模式开关实验**（p213-217）：

1. 手机空闲主页按 Menu 键（或两次 OK）进菜单
2. 输入 *7378423*（助记 *service*）
3. 选 Site Survey mode → 按 On 激活（勘测层常驻任何模式）
4. 长按 * 切换慢/快测量；Vol- 调出 RFPI 附加屏
5. 绕场测量，按 -70dBm 等值线找覆盖边界（实验任务口径）
6. 关闭：菜单 Off → On hook → 回空闲主页

## A2 — 未来触发

使用情境：覆盖范围验收；用户报楼梯间/车间断话；布点前勘测；同步可行性预估（站间 -80dBm）；借勘测工具。

语言信号：勘测 / survey / site survey / RSSI / -70dBm / -60dBm / -80dBm / SSK / Site Survey Kit / 8242 / 覆盖边界 / 信号强度 / RFPI / *7378423*。

与相邻能力区分：基站间同步门槛的配置应用见同步拓扑能力；覆盖不足的选型结论见产品选型能力；RSSI 之外的状态排障见维护排障（路由）。

## E — 可执行步骤

输入契约：场景类型（容易/金属困难）、覆盖目标（话音区/同步区）、勘测手机（SSK 含 8242，或交付机型临时充当）。

1. 定门槛：容易场景按 -70dBm、金属环境按 -60dBm 画话音边界；站间同步按 -80dBm。完成标准：验收门槛双方确认
2. 开勘测模式：*7378423* → Site Survey mode → On。完成标准：勘测层显示
3. 绕场采样：记录 RSSI 与基站列表，标出等值线与盲区。完成标准：覆盖图成型
4. 判定：达标区/弱区/盲区三色标注，给出加站/移站建议。完成标准：布点结论可评审
5. 关闭并回收：Off 退出、勘测机与交付机分离管理。完成标准：无调试模式残留

判停点：

- 勘测方法论问题（天线选型/传播模型/采样规范）→ 书外，指向 8AL90874USAA（工程规则+SSK 手册）
- 手机被侧键"失灵"投诉 → survey mode 接管了音量键与侧键，先查是否忘关
- 同步区达标但切换仍失败 → 转同步拓扑能力查配置，不要反复勘测

输出契约：覆盖勘测记录（等值线/盲区）+ 布点建议 + 门槛口径备注。

## B — 边界

- 勘测方法论（传播模型、天线增益选择、采样流程）全部在 8AL90874USAA，书内只有门槛数字与工具开关
- SSK 配 8242 勘测机与主流交付机型 82x4 不一致——勘测结论外推时留意机型差异（BOOK_OVERVIEW 批判项）
- RSSI 距离还取决于手机 RF 灵敏度与环境（p207）；书内未给勘测点密度规范
- -80dBm 门槛原文语境为 "DAP synchronization"（基站间同步），不作为话音验收门槛
