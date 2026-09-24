# 决策规则速查 — OXO Connect Starter (Participant's Guide, Edition 16)

| 能力 | 一句话规则 |
|---|---|
| 交付前数据采集 | 七块清单（IP/参考值/密码表/编号/信箱/组与按键/呼入呼出与运维前提）先定稿，后动配置 |
| 系统开通双路线与首次连接 | Cloud Connect 走 FTR（192.168.94.246）自动上云，Standard 走 OMC 首连+双钥匙许可；IP 四页签改完必须重启 |
| 终端开通（IP 话机与 DECT） | Auto-Provision+DHCP 池是总前置；IP 话机 static/dynamic 两路，DECT 走 ARI+GAP 或 8328 SIP 两条线 |
| 编号计划与四种组 | 四层拨号计划+Base 映射（0-2199）；先删冲突段再建新段；hunt/代接/广播/经理秘书四组各管一件事 |
| 用户功能与语音信箱 | 键三类+动态路由两级两计时（级联 5 级）+权限与载体两段式；信箱三态双模，录音默认 30 天删除 |
| 公共 SIP 中继 | 周边四项+网关九页签按序配置；验收判据 SIP registration success；生产参数与紧急号 ARS 以 TC1284 为准 |
| 呼入分发与呼出闭锁 | 呼入=话务台组+时段表+双 DDI 计划；呼出=Traffic sharing→Barring→闭锁表三层判定，00 国际默认禁 |
| 备份恢复、软件升级与复位 | 四线备份（自动/OMC 手动/SD 卡/DBAdapter）+双版本 Swap 可回退+三档复位按损失最小选 |
| 硬件平台与容量 | 四平台两 CPU 线（OCE IPBox / PowerCPU EE 三档）；DSP 通道 16/48/60/76；HSL 三机柜 5 米 |
| 消息与彩铃 | MSG1-20（默认 4 条许可 20、总 320 秒）与 MoH（仅外线保持、三源、Entity 1-4），.wav 格式硬约束 |
| 安全基线与防盗打 | 密码三句（非默认/常改/不简单）+8 位三类字符规则+盗打损失口径；生产加固强制 TC1143 |
| Rainbow 混合云接入速览 | PBXID+激活码接入（域名不动）+Webdiag 判据 connected with final password；网关四拓扑 20/50 上限；深入转姊妹技能 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
