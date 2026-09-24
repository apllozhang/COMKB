# rainxte101en 盲判结果（仅依据能力目录，判定后锁定）

should-company-01 | hub-company-voice-subscription | 开租户选订阅组合与公司可见性设置，正中建司与订阅开通范畴
should-company-02 | hub-company-voice-subscription | 订阅开通与声明 PBX 入口是 BP 专属权限问题，归建司订阅能力
should-pbx-01 | hub-cloud-pbx-provisioning | 声明 PBX、编号计划混长与出局前缀，正中 PBX 话务配置
should-pbx-02 | hub-cloud-pbx-provisioning | 黑白名单与 DDI 注入首号成公司主号，属 PBX 号码配置
should-member-01 | hub-member-telephony | 批量开户通道（AAD/LDAP/CSV）与密码要求归成员管理
should-member-02 | hub-member-telephony | 删除成员宽限恢复与号码订阅保留归成员管理
should-zt-01 | hub-zero-touch-provisioning | 话机开箱即用的 zero-touch 部署流程与网络前提（DHCP option）
should-zt-02 | hub-zero-touch-provisioning | DECT 8328/8368 选型在 zero-touch 与 DECT 移动能力内
should-dev-01 | hub-device-maintenance | 已注册话机禁直连、debug 一次性口令抓日志归设备维护
should-dev-02 | hub-device-maintenance | 第三方 SIP 话机与传真接入走 Generic SIP 限制条款
should-hunt-01 | hub-hunt-groups | 等待队列与溢出策略是呼叫组核心参数
should-hunt-02 | hub-hunt-groups | 经理助理筛电话依赖经理 DID 挂组级规则，归呼叫组
should-att-01 | hub-attendant-supervision | 全员状态可见、代接转接的工作台即 PC 话务台
should-att-02 | hub-attendant-supervision | 激活话务台后话机关联被删的口径在话务台能力内
should-ws-01 | hub-welcome-service-ivr | 闭店提示、时段开闭路由、假日日历属欢迎服务
should-ws-02 | hub-welcome-service-ivr | 多级按键菜单即 IVR 3 级结构，许可问题也在该能力内
should-net-01 | hub-network-readiness | 上线前端口/域名/防火墙核查与带宽估算（Opus/G711 口径）
should-net-02 | hub-network-readiness | 用 Rainbow Pilot 做承载评估正是该能力内容
should-ms-01 | hub-multisite | 两城各自外呼显示本地号码靠站点主号实现
should-ms-02 | hub-multisite | 分店站点 MoH 与站点主号、站点不是分 PBX 的口径在此能力
should-ana-01 | hub-analytics | 月度 CDR 话单获取通道与出账时间归分析体系
should-ana-02 | hub-analytics | MOS/抖动/RTT/丢包阈值定位通话质量归分析仪表盘
should-mnt-01 | hub-maintenance-support | 判断 ALE 云端故障看 status.openrainbow.com 归维护支持体系
should-mnt-02 | hub-maintenance-support | 开正式 SR 走 MyPortal 表单流程归维护支持体系
bait-company-01 | hub-member-telephony | 主线是开户配号绑话机验证，核心动作在成员管理与话务配置
bait-pbx-01 | hub-zero-touch-provisioning | Config Failed 取不到配置是 zero-touch 部署问题，非 PBX 声明
bait-zt-01 | hub-device-maintenance | Yealink 第三方话机 SIP 账号与证书链走 Generic SIP 接入
bait-hunt-01 | hub-welcome-service-ivr | 按 1/按 2 按键菜单是 IVR，不是呼叫组
bait-ms-01 | hub-multisite | 站点间目录隔离诉求要对照"目录跨站不变"口径，归多站点
bait-ana-01 | hub-maintenance-support | 查云服务实时状态是 status.openrainbow.com，归维护支持
bait-ws-01 | hub-attendant-supervision | 话务台免费与否由 Voice Attendant 订阅决定，归话务台能力
bait-hub-01 | none | OXO Connect 接入与 OMC 网关激活不在 Rainbow Hub 目录任何能力内
edge-nr-01 | hub-member-telephony | 纯 Voice Phone 用户配号前提归成员话务配置
edge-hunt-01 | hub-hunt-groups | 溢出时间口径（10-900 秒）归呼叫组
edge-emg-01 | hub-hunt-groups | 紧急组 112/0112 转警行为归呼叫组
edge-ivrm-01 | hub-welcome-service-ivr | IVR 唯一提示建后不可改的边界归欢迎服务与 IVR
edge-att-01 | hub-attendant-supervision | 话务台无移动端的边界归话务台能力
