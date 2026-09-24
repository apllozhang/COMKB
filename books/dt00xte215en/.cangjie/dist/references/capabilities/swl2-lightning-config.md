# Lightning Config 快速开局（七步流、禁令清单、模板导入）

## R — 原文依据

> "Port 1 DHCP Client Default IP interface VLAN1 192.168.0.1"（p104）
> "1.Click on RECOMMENDED DEFAULTS 2.Click on LIGHTNING CONFIG • Do NOT skip the Recommended Defaults!"（p115）
> "The new password must meet the following requirements: • At least 8 characters • 1 uppercase letter • 1 lowercase letter • 1 digit • 1 special character (but avoid using ! or $)."（p116）
> "Never connect an out-of-box ALE switch to another without running Lightning Config first."（p117）

出处：DT00XTE215EN p102-126。

## I — 自述

零专家单机开局向导：笔记本 DHCP 接端口 1，浏览器进 https://192.168.0.1，从拆箱到通流量厂商口径 <5 分钟/台（宣传口径，p106）。七步流：

1. **准备**：笔记本设 DHCP 客户端；遵守禁令清单（见 B）
2. **连接**：网线接交换机端口 1（唯一连线），上电等约 3 分钟看两侧绿灯
3. **登录**：浏览器开 https://192.168.0.1/（必须 https），接受自签名证书，admin/switch 登录；笔记本此时被交换机 DHCP 分到 192.168.0.200/24
4. **最小配置**：先 RECOMMENDED DEFAULTS 再 LIGHTNING CONFIG，填 IP/掩码/网关（全网唯一）
5. **改密**：YES 应用后立即改 admin 密码——至少 8 字符、各含 1 大写/1 小写/1 数字/1 特殊字符，避开 ! 与 $
6. **保存认证**：确认保留 working 开关后保存，等绿色成功提示（数分钟）
7. **扩展**：主页接边缘设备与其他已配置 ALE 交换机；任何后续改动必须 Write Memory

**模板复用**：IMPORT 导入架构师给的 .json 模板，再补必填项（IP 全网唯一）走同一流程（p120-121）。

## A1 — 书中案例

**Lightning Config 操作序列**（p110-121，讲义内嵌操作步骤）：

1. 禁令自查：不预接线、不接其他交换机、不先接外设、不接 DHCP 服务器、笔记本就绪再上电
2. 笔记本设 DHCP：控制面板 > 网络和共享中心 > 更改适配器设置 > 属性 > 自动获得 IP/DNS
3. 连接端口 1，上电等约 3 分钟，核对绿灯
4. Chrome 打开 https://192.168.0.1/，Advanced > Proceed 接受自签名证书，admin/switch 登录
5. 点 RECOMMENDED DEFAULTS，再点 LIGHTNING CONFIG 填必填项（不懂 IP 编址就停下来找架构师）
6. YES 应用后立即改 admin 密码（≥8 位四类字符，避开 ! 与 $），保存
7. 确认保存完成出现绿色成功消息，回主页
8. 主页巡检：Quick Links、搜索、PoE Port Configuration 看 Power mW 列确认受电设备已启动
9. 可选：IMPORT 选 .json 模板，Lightning Config 补 IP 后 SAVE CONFIGURATION 走完流程

## A2 — 未来触发

使用情境：新到的 OmniSwitch 第一次上电；小网络单台快速交付；导入架构师模板开局；开局后 admin 密码设置；确认受电设备功率。

语言信号：Lightning Config / OLC / 快速开局 / 192.168.0.1 / 端口 1 / Recommended Defaults / 出箱 / out-of-box / 开局模板 / .json / 5 分钟 / admin 密码。

与相邻能力区分：

- 30 台以上批量零触开局：升级与 Auto-Fabric 能力卡
- 开局后的配置保存纪律：配置生命周期能力卡
- 管理面加固清单：AAA 加固能力卡

## E — 可执行步骤

输入契约：IP 规划（全网唯一地址/掩码/网关）、架构师模板（可选）、笔记本与网线。IP 规划未知 → 判停，不要现编。

1. 环境自查：确认交换机未接入任何网络/交换机/DHCP 服务器，笔记本已设 DHCP。完成标准：唯一连线是笔记本到端口 1
2. 上电等待：约 3 分钟绿灯后访问 https://192.168.0.1/，admin/switch 登录。完成标准：进入向导主页
3. 基线应用：RECOMMENDED DEFAULTS（不可跳过）> LIGHTNING CONFIG 填必填项。完成标准：IP/掩码/网关填写且全网唯一
4. 改密固化：YES 应用后立即改 admin 密码（≥8 位四类字符、避开 ! 与 $），保存并等待成功提示。完成标准：新密码可登录、配置已保存
5. 模板路径（可选）：IMPORT .json 模板替代第 3 步，补 IP 唯一性后走完同一流程。完成标准：模板下发成功
6. 交接：只接边缘设备与其他已配置 ALE 交换机；每次后续改动 Write Memory。完成标准：设备通流量且配置已固化

判停点：

- 不理解 IP 编址/掩码/网关 → 停，按原文找方案架构师，不要试错
- 交换机已接在生产网络里 → 停，先按禁令断开，否则 DHCP 冲突或误入生产网
- 对端也是出箱交换机 → 停，两端都先做完 Lightning Config 再互联
- 批量开局需求 → 停，本向导一次一台；转 Auto-Fabric 零触路径

输出契约：开局完成且改密的交换机（管理地址可达）+ 已保存确认 + 后续接线边界说明。

## B — 边界

- 禁令清单（p108）：不预接线进网、不与其他交换机互联、不先接摄像头等外设、不接 DHCP 服务器、上电前笔记本就绪
- 出箱交换机严禁未开局先互联；示例拓扑含物理环路，照图接线前必须确认环路避免技术已实施（p117/p125）
- "每次改动必须 Write Memory、正确退出 Certified Mode" 为界面纪律，与 CLI 保存语义一致（p118）
- <5 分钟开局与 <15 分钟学习成本为厂商宣传口径（p106），非验收承诺
- 密码避开 ! 与 $ 的原因原文未解释，按原文执行即可
- 适用面以 ALE 6360 交换机口径为主（p106）；其他型号以当期产品文档为准
