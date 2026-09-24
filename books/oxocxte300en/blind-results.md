# oxocxte300en 盲判结果（仅依据能力目录，未读答案）

case-id | slug或none | 理由一句
should-collect-01 | oxos-data-collection | 交付前准备安装数据，正是七块安装输入清单的能力
should-collect-02 | oxos-data-collection | 交付前规划编号方案属于安装输入清单里的"编号计划"块
should-comm-01 | oxos-commissioning | 注册到 Cloud Connect 属于系统开通双路线的 Cloud Connect 路线
should-comm-02 | oxos-commissioning | OMC 首连改 IP 四页签及改后重启属于 Standard 路线开通范畴
should-term-01 | oxos-terminals | IP 话机注册不上，排查 Auto-Provision+DHCP 池等终端开通前置
should-term-02 | oxos-terminals | 8328 基站与 8214 话机接入属于终端开通（SIP-DECT 两段注册）
should-num-01 | oxos-numbering-groups | 新建缩位拨号段冲突，对应"先删冲突段再建新段"规则
should-num-02 | oxos-numbering-groups | 共号轮听是 hunt 分发、出差代接是 pick-up，都在四种组能力内
should-user-01 | oxos-user-features | 无应答定时转秘书是动态路由两级两计时，防插入属键与权利设置
should-user-02 | oxos-user-features | 遇忙前转不生效要查动态路由与 apply diversion 总开关
should-sip-01 | oxos-sip-trunk | 确认 SIP 注册成功正是"SIP registration success 验收"
should-sip-02 | oxos-sip-trunk | Outbound Proxy 置灰对应"DNS 先于 Outbound Proxy"顺序依赖
should-inbar-01 | oxos-incoming-barring | 按时段分派来话+预公告，对应话务台组时段表与双 DDI 计划
should-inbar-02 | oxos-incoming-barring | 下班后仍能外呼，查 6 张闭锁表与 Inhibition Time-ranges
should-maint-01 | oxos-maintenance | 升级注意事项与失败回退对应双版本+Swap+switchover 回退
should-maint-02 | oxos-maintenance | 退租清数据对应 Warm/Cold/Factory 三档复位与数据保留矩阵
should-hw-01 | oxos-hardware-platform | 250 用户平台选型与扩展机柜限制属于四平台容量与 HSL 三机柜
should-hw-02 | oxos-hardware-platform | SIP 并发 70 路对应 DSP 通道 16/48/60/76 容量口径
should-audio-01 | oxos-audio-messages | MP3 能否直接用对应 .wav 格式硬约束（16-bit PCM 或 A/μ-law 8kHz Mono）
should-audio-02 | oxos-audio-messages | 内线保持无音乐对应 Music on Hold 仅外线保持的设计约束
should-sec-01 | oxos-security | 话费暴增疑似盗打，对应盗打损失口径与应急
should-sec-02 | oxos-security | 管理密码构造与旧默认密码表弃用都在安全基线能力内
should-rb-01 | oxos-rainbow-integration | 凭证、填写位置与接通判据对应 PBXID+激活码与 Webdiag 判据
should-rb-02 | oxos-rainbow-integration | 电脑接听无声对应 RCC 中间态音频在话机的已知行为
bait-collect-01 | oxos-numbering-groups | 表面提采集清单，实际诉求是验证 hunt 三种分发，归组能力
bait-comm-01 | oxos-terminals | OMC 已能登录说明开通已完成，实际是 50 台话机批量开通
bait-term-01 | oxos-numbering-groups | 话机已开通，建共接号码轮听是建 hunt 组，归编号与组能力
bait-num-01 | oxos-incoming-barring | 限制谁能拨 0 出局是呼出闭锁与出局权限控制，非编号计划调整
bait-user-01 | oxos-incoming-barring | 外线来话按"下班后"时段转信箱，核心是时段表来话分发而非用户键
bait-sip-01 | oxos-incoming-barring | 中继已注册成功，打不出国际长途查闭锁表与默认 LC 限制
bait-inbar-01 | oxos-sip-trunk | 表面说出局，实际是中继注册不上，归 SIP 中继能力
bait-maint-01 | oxos-commissioning | Factory 复位后重建基础配置走初始安装向导，属开通范畴
bait-rb-01 | none | Rainbow 云侧批量开户与 Teams 集成超出本目录，目录明示深入转姊妹技能
bait-rb-02 | none | ACD 排队与坐席组配置在能力目录中无对应能力，超范围
bait-sec-01 | oxos-security | TC1143 防火墙话题落在安全基线能力，其内有 TC1143 强制指针可给出指引
bait-audio-01 | oxos-incoming-barring | 录音已备好，"仅非营业时间先播"是按时段来话分发与预公告的配置
bait-hw-01 | oxos-commissioning | 硬件已定，实际诉求是 OMC 安装与首次连接，属 Standard 开通路线
edge-version-01 | none | WebRTC 网关自动配置在能力目录中无对应条目，超范围
edge-hunt-01 | oxos-numbering-groups | hunt 500 能否占用对应"500 被 VM 保留"的规则
edge-hotel-01 | oxos-commissioning | Business 切 Hotel 对应"初始安装向导与 Hotel 唯一入口"约束
