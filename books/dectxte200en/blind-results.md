# dectxte200en 盲判结果（仅依据能力目录，未读答案）

should-pari-01 | dect-pari-identifier | 用户直指"标识没配对"，两类基站间锁不住对应 PARI/PLI 匹配规则
should-pari-02 | dect-pari-identifier | PLI+PARI 算 13 位号码=PARK 拼接算例，纯号码体系问题
should-select-01 | dect-product-selection | 有老 UA 板卡时 TDM 接用还是上全 IP，属产线与拓扑选型决策
should-select-02 | dect-product-selection | IBS 无加密是产线能力规格问题，靠选型分流判据回答
should-deploy-01 | dect-ipxbs-deployment | 8378 上电后 OXE 看不到设备，走全局参数/DHCP/注册开关部署链路排查
should-deploy-02 | dect-ipxbs-deployment | 换站后告警位置乱=自动注册致 RPN 漂移，需手动注册保 RPN
should-sync-01 | dect-xbs-sync-topology | 同步不稳想分组处理，对应同步树/Sync Cluster 组织方式
should-sync-02 | dect-xbs-sync-topology | 一台 OXE 跑 3 个 PARI，>2 PARI 需 Sync Highway 串链路
should-hsreg-01 | dect-handset-registration | 新开十个 DECT 分机并注册手机，系统侧+手机侧双通道流程
should-hsreg-02 | dect-handset-registration | 回收手机、分机号留给接手人，对应注销/换机保留用户操作
should-mixed-01 | dect-mixed-mode | TDM 现网加 IP 基站后老手机可用性，是混合模式部署问题
should-mixed-02 | dect-mixed-mode | 混合模式下跨类切换断话，对应跨类切换外部同步链路配置
should-rereg-01 | dect-auto-reregistration | PARI 彻底变化后三百台批量重注册，属 -forceUpdate/-f 批量场景
should-rereg-02 | dect-auto-reregistration | 确认哪些手机没迁成功=ReinstallSuccess/NOK 双清单核对
should-fw-01 | dect-firmware-management | 基站固件白天不停业务升级=downstat x TFTP 后台下载空闲重启
should-fw-02 | dect-firmware-management | 手机固件卡在等刷写=downstat m 六态状态机判读
should-maint-01 | dect-maintenance-troubleshooting | "先跑什么命令"判断切换问题，属排障命令集（tcdump/xbssynchro 等）
should-maint-02 | dect-maintenance-troubleshooting | 集中收基站日志给二线=syslog 514 四级配置
should-survey-01 | dect-radio-survey | 覆盖边界怎么划，依据话音门槛 -70/-60dBm 勘测判据
should-survey-02 | dect-radio-survey | 关掉勘测界面=*7378423* survey mode 开关操作
should-ibs-01 | dect-ibs-deployment | UA 板卡端口主偶从奇与 SYT/LY278 布线距离是 IBS 部署核心内容
should-ibs-02 | dect-maintenance-troubleshooting | OOS 与 NOK 标志区别及 inserv 拉回服务，属 dectview 标志判读与日常排障
should-sip-01 | dect-sip-dect | 低成本 SIP-DECT 基站部署流程
should-sip-02 | dect-sip-dect | 8328 双小区主站声明规则与建链约 5 分钟的等待判断
bait-pari-01 | dect-handset-registration | 13 位号是否要手输是注册流程问题，不是号码体系计算
bait-select-01 | dect-ipxbs-deployment | 产线已定，实际诉求是 IP-xBS 装站入网的具体步骤
bait-deploy-01 | dect-xbs-sync-topology | 同步树乱、Master 频繁切换属同步体系问题，"换基站"只是语境诱饵
bait-mixed-01 | dect-auto-reregistration | PLI 已降到 30，当前动作是把三百台手机推到新 PARI 的批量工具选择
bait-hsreg-01 | dect-firmware-management | 注册已完成，诉求是手机固件统一升级
bait-rereg-01 | dect-auto-reregistration | 重注册时机型版本是否支持属该能力机型版本表范围
bait-fw-01 | dect-ipxbs-deployment | 固件升完后换基站，注意点是换站手动注册保 RPN
bait-survey-01 | dect-xbs-sync-topology | RSSI 达标但基站间同步不起来是同步体系问题，勘测只是诱饵语境
bait-ibs-01 | dect-mixed-mode | IBS+IP 混用后老手机漫游不过去是混合模式 PLI/漫游问题，非装站质量
bait-sip-01 | dect-sip-dect | 8328 注册语义与四步闭环，与普通 DECT 的 mtcl 安装命令不同
bait-oos-01 | none | 天线选型/布点图纸/全套方案设计超出勘测能力范围，目录无整体无线设计能力
bait-oos-02 | none | Erlang 话务建模公式目录内无任何能力覆盖
bait-oos-03 | none | OXE 外线 SIP 中继对接运营商不属本 DECT 目录任一能力
edge-pli-01 | dect-pari-identifier | 末两位不同时 PLI 降 30 够不够，对应降位规则 30/29
edge-rssi-01 | dect-radio-survey | -70dBm 临界读数达标判定属勘测阈值知识
edge-cap-01 | dect-product-selection | 单 PARI 挂站数上限属产线容量规格边界（IBS 256 台/IP-xBS 2032 台量级）
