# rainxte003en 盲判结果（仅依据能力目录，未读答案）

should-company-01 | rxe-company-subscription | 建租户选订阅+公司可见性设置是该能力主体
should-company-02 | rxe-company-subscription | 建 PBX 与开付费订阅是 BP 专属权限，找不到按钮属角色/体系问题
should-agent-01 | rxe-agent-onboarding | netadmin 菜单配 DNS/代理并验证解析生效
should-agent-02 | rxe-agent-onboarding | PBXID+激活码启用 agent 与 incvisu 五链路确认
should-member-01 | rxe-member-lifecycle | 批量开户方式（CSV/Azure AD）与密码 12+3 要求
should-member-02 | rxe-member-lifecycle | 删除后 10 天宽限期内邮箱占用是该能力明确场景
should-routing-01 | rxe-routing-rex | 改路由后振铃终端不符预期，对应路由四案例与"路由不等于转发"
should-routing-02 | rxe-routing-rex | Ghost Z 池数量与 tandem 只做主站规则
should-deploy-01 | rxe-webrtc-gateway-deployment | mpnetwork/mpconfig 配置与 mpshow/mpcheck 核验
should-deploy-02 | rxe-webrtc-gateway-deployment | 远程升级（BP 账户）与手动 mpupgrade 两法及 NUC 门槛
should-oxecfg-01 | rxe-oxe-gateway-config | SIP TG/ARS/判别器等 OXE 侧九件套配置
should-oxecfg-02 | rxe-oxe-gateway-config | 话机通话记录回拨 Rainbow 分机需 CDT 配置
should-pool-01 | rxe-gateway-pool-sizing | 多 OXE 共用网关的共享池架构与 SIP 406 溢出分流
should-pool-02 | rxe-gateway-pool-sizing | 话音用户数估通道数=TBE067 四输入
should-teams-01 | rxe-teams-integration | Teams 打 PBX/外线的方案设计与工作站双件套安装
should-teams-02 | rxe-teams-integration | 在场不同步对应在场同步需激活 O365 共享
should-rcc-01 | rxe-rcc-association | 分机绑定 Telephony 页签与五项测试验证
should-att-01 | rxe-attendant-consoles | 前台工作台在 4059EE 与 Rainbow 话务台间选型
should-att-02 | rxe-attendant-consoles | 部门间临时互接对应互助组（非固定监督组）机制
should-maint-01 | rxe-maintenance-support | 判断是否 ALE 云侧问题用 status 状态页与告警订阅
should-maint-02 | rxe-maintenance-support | 开正式工单=MyPortal 开 SR/认证伙伴建 ESR 流程
should-net-01 | rxe-network-readiness | 上线前网络准备与端口/域名/带宽核查清单
should-net-02 | rxe-network-readiness | 混合用法承载评估用 Rainbow Pilot 按用法配比
should-lab-01 | rxe-lab-pod-setup | RLAB 基线核对机架板卡/软话机/DID
should-lab-02 | rxe-lab-pod-setup | 实验环境外线与 DID 翻译按 POD 号对齐排查
should-agent-03 | rxe-agent-onboarding | curl 报证书错误是该能力明确列出的两类误判之一
bait-company-01 | rxe-member-lifecycle | 租户已存在，诉求主体是给个人开户，绑分机验证是后续延续动作
bait-agent-01 | rxe-oxe-gateway-config | 网关装好后 OXE 侧 SIP 中继组/ARS 配置，与 agent 接入链路无关
bait-deploy-01 | rxe-gateway-pool-sizing | 复制 vs 共享池选型与通道数属容量规划，非部署动作
bait-pool-01 | rxe-webrtc-gateway-deployment | 共享池拓扑已定，当前动作是 OVF 部署并激活
bait-routing-01 | rxe-attendant-consoles | 4059EE 关联话机禁 multi-line 是话务台规则，tandem 只是被比较对象
bait-teams-01 | none | Teams 租户应用权限策略与紧急呼叫地址属微软侧租户管理，目录内集成能力只覆盖 Rainbow 侧上架与同意，不含租户策略统一配置
bait-rcc-01 | rxe-routing-rex | RCC 音频在话机是形态属性，要电脑出音频需按四形态矩阵改用户形态
bait-maint-01 | rxe-agent-onboarding | incvisu 五链路排障与维护四抓手属 agent 接入能力
bait-net-01 | rxe-agent-onboarding | 端口放行仍连不上，查 incvisu 五链路判据属 agent 接入排障
edge-oxecfg-01 | rxe-oxe-gateway-config | G711 是该书 OXE 侧配置口径，能否改 G729 属能力边界问题
edge-pool-01 | rxe-gateway-pool-sizing | 400 并发流上限与用户数的语义澄清
edge-att-01 | rxe-attendant-consoles | 手机开话务台值班触到"Rainbow 话务台仅 PC"边界
edge-routing-01 | rxe-routing-rex | 纯 DECT 话机用户上 Rainbow 路由对应四形态矩阵 DECT 特例
edge-lab-01 | rxe-lab-pod-setup | 实验口径（IP/账号/号码）不得搬生产是该能力的边界声明
