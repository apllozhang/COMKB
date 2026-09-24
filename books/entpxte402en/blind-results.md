# ENTPX 盲判结果（仅依据能力目录，锁死后不回改）

should-sot-01 | entload-sot-installation | Template Factory 的标准 8CPU/16GB 前置与降级模式（50GB 盘+templateFactory）都在 SOT 安装能力内
should-sot-02 | entload-sot-installation | SOT 更新仅限同主版本 zip+MD5，跨版本能否升正是该能力的边界规则
should-cs-01 | entload-cs-loading | 全新 CS 板卡加载与加载后初始化清单（密码规则/国家码/板卡上线）是该能力主线
should-cs-02 | entload-cs-loading | 部署后等待目标机对应网络引导 BOOTP/DHCP 经 TFTP/FTP 不通，属 CS 加载域
should-patch-01 | entload-patch-management | 不停话音打补丁对应双分区+动态补丁热装或静态装 inactive 的安排
should-patch-02 | entload-patch-management | 动态补丁装完行为未变对应 downstat 收尾动作缺失
should-oxev-01 | entload-oxe-v-deployment | 平台矩阵（ESXi/Hyper-V/KVM 等）决定许可路径，正是 OXE-V 能力核心
should-oxev-02 | entload-oxe-v-deployment | OMS 规格 120 通道/240 台与规格模板 500/3000/7000/15000 在此能力
should-gas-01 | entload-gas-delivery | GAS 硬件前置表与 BootDVD+iso 经 SOT 加载流程属 GAS 交付能力
should-gas-02 | entload-gas-delivery | 后安装向导六段含 WebRTC GW（50 并发/7000 用户）配置
should-cloud-01 | entload-cloud-connect | 接入 ALE 云的网络前提（出站 443 XMPP/WSS+80 SOCKS5+53 DNS）正是该能力
should-cloud-02 | entload-cloud-connect | FTR 首次注册失败的排查（swk CCSID 换凭证/checkCloudConfig.sh）属云连接域
should-rtr-01 | entload-rtr-licensing | "Call your administrator"正是 RTR 资格期归零进 Panic 的表现
should-rtr-02 | entload-rtr-licensing | Duplicated 状态双扣与 PIN 恢复明列在 RTR 能力
should-pod-01 | entload-pod-licensing | 买断转订阅即 C2P 转换（下单即定局、件号 3EYxxxxxMA、MyPortal 须 Active）
should-pod-02 | entload-pod-licensing | spadmin 对账 lms/oxe 两列必须一致，失配进 panic 正是该能力
should-dist-01 | entload-distributor-loading | 不让架临时虚机（无 SOT）对应 Easy Installation 分发器模式本地加载
should-dist-02 | entload-distributor-loading | 分发器装完清盘对应 Rload 解包物 9-7 手动清理、/tmpd 源文件处理
should-media-01 | entload-sot-media | iso 传上去但项目选不到，对应 Refresh 后须 Declare media 的公共动作
should-media-02 | entload-sot-media | 许可可随项目部署还是装后手工恢复，正是该能力描述的点
should-gasops-01 | entload-gas-ops | Rocky 宿主升级走 SOT 项目或 gas-rocky-update.sh 且全系统停机，属 GAS 日常运维
should-gasops-02 | entload-gas-ops | gasbackup 出 tar.gz+_PostInstall.cfg，全新安装+备份=免后安装，正是该能力
should-fleet-01 | entload-fleet-dashboard | 不出机房看机队资产/版本/许可即 Inventory 云端机队服务
should-fleet-02 | entload-fleet-dashboard | 远程控制台单会话、1 分钟无操作断开正是该能力描述
bait-sot-01 | entload-sot-media | 表面像 SOT 安装问题，实际是媒体三库传输后未 Declare media，属加载项目配置公共动作
bait-cs-01 | entload-distributor-loading | 机房不让接临时设备即无 SOT 环境，走 Easy Installation 分发器模式
bait-patch-01 | entload-sot-installation | 表面问升级，实际约束是"一次只允许一个部署任务"，属 SOT 部署工具能力
bait-oxev-01 | entload-oxe-v-deployment | Hyper-V 平台按矩阵强制 Cloud Connect，FlexLM+加密狗仅 ESXi/KVM，许可路径判断在该能力
bait-gas-01 | entload-gas-ops | 交付完成后的每月例行备份（gasbackup）与版本盘点（gasversion）属日常运维
bait-cloud-01 | entload-rtr-licensing | FTR 成功后资格期仍往下掉是 RTR 计天规则（OK+0.5/NOK-1）问题，能力域在 RTR
bait-rtr-01 | entload-rtr-licensing | FlexLM 与 RTR 不能同时启用的互斥规则明列在 RTR 能力
bait-pod-01 | entload-pod-licensing | MyPortal 项目须 Active 才能拉许可，Pending 状态处理属 OPEX/订阅能力
bait-license-01 | none | 话机注册报 No license available 的逐话机许可诊断在 12 项能力目录中均无覆盖，判超范围
bait-scope-01 | none | 建 200 用户、编号计划、外线路由是 OXE 业务配置，不在本加载部署教材任何能力内，判超范围
edge-rtr-01 | entload-rtr-licensing | 扣 1 天的具体节奏与宽限细节属 RTR 计天规则域，目录未列 4 小时宽限，细节可能超教材
edge-pod-01 | entload-pod-licensing | 界面见到 OPEX 开关是否真计费对应 lock 431=1 才开 OPEX 的判定规则
edge-oxev-01 | entload-oxe-v-deployment | 平台版本比矩阵新能否上 OXE-V，属平台矩阵支持边界的判断
edge-gas-01 | entload-gas-delivery | 软件 RAID 容量再大也不行，因硬件前置"只认硬件 RAID"，属 GAS 交付前置
