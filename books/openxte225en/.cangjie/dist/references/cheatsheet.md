# 决策规则速查 — OpenTouch — 移动与远程办公 (Participant's Guide)

| 能力 | 一句话规则 |
|---|---|
| 远程接入架构与 DMZ 双边缘 | 三类需求定方案边界，DMZ 双边缘（反代管 Web 服务、OTSBC 管 SIP/媒体），客户端×组件查矩阵，DNS 内外两套解析 |
| 证书策略与签发（CA、封装、SAN、自建 CA） | 远程访问必须 CA 签发；封装由私钥生成位置决定（PKCS7/PKCS12）；会议 FQDN 必须进反代与 OT 证书 SAN |
| OpenTouch 服务器侧远程访问设置 | RP 申报四 URL（EVS 带 8016）、OTSBC 申报 5261/8061、DAS 规则按序且国家相关、ACS 会议 FQDN 加 rehost 加证书重签 |
| OTSBC 部署与向导配置 | OVF 上电、CLI 初始化（write 后 reload）、许可与证书、Alcatel-Lucent Remote Users 向导模板、SIP 接口换证书、补 TCP 5060 |
| 反向代理两路线部署与选型（内嵌 RP、Nginx） | OTSBC 7.2+ 内嵌 RP（许可+三模板 ini）与独立 Nginx（三 conf+snippets）功能同向；OT 2.2 起两 conf 必须同改；LDAP daemon 需专用机器 |
| OTC PC 远程办公两模式（multi-devices、Nomadic SIP） | multi-devices 绑 SIP 分机做副设备（主话机保留），Nomadic SIP 用 Ghost Z 池+SIP 设备池顶替主话机（1 并发占 1+1） |
| OTC 智能手机开通（Connection 用户、自动对象、R2.6 单设备） | 关联一次自动建 OXE 对象（RE/tandem/速拨号/SIP 设备/判别器/ARS，按模式增减），再手工核判别器关联与 COS 区域授权；R2.6 起 RE 可做唯一设备 |
| iPhone+ APNS 推送专项 | 后台来话走 APNS 推送唤醒（多 SIP invite 设计行为）；防火墙四端口 5223/2195/2196/443；SBC 5265 声明；kamailio-wasp/wspcfg 缓冲与维护 |
| 客户端远程接入两步法（接入配置与路由档案） | 第一步填公共 URL 与凭证，第二步激活路由档案；手机发起拨打永远本机发话，dial from 不影响 |
| 智能手机连接模式与回落（WiFi/3G4G/DTMF、无 SIM） | 按数据连接五分场景定功能面；无数据仅 DTMF 回落（打/挂/留言/有限路由）；Android 无 SIM 纯 VoIP 但失回落/私人呼叫/短信 |
| VMware 虚机 OVF/OVA 部署 | 按 ESXi 版本选路线（6.5 用 web client、6.0 及以下才可用 vSphere client），网络映射选 DMZ，实验磁盘 Thin |
| 实验环境与拨测验证（RLAB、编号计划、模拟器预期表） | 编号三层（DHCP 池/用户编号/模拟器变换）；拨测按三格式预期表核对落点与主叫显示两个维度 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
