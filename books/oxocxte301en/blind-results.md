# oxocxte301en 盲判结果（仅依据能力目录第一判断，锁定后不改）

| case-id | slug/none | 理由 |
|---|---|---|
| should-sipnet-01 | oxoa-sip-networking | 公网 SIP 网关配置顺序与验收正是该能力主责 |
| should-sipnet-02 | oxoa-sip-networking | 两台 OXO 私网互联+双向溢出是该能力描述原文场景 |
| should-ars-01 | oxoa-numbering-ars-suite | GSM/VoIP/ISDN 多运营商分流是 ARS 套件典型场景 |
| should-ars-02 | oxoa-numbering-ars-suite | 一个 DDI 按日组时段分流到多目的地属 Internal ARS |
| should-hotel-01 | oxoa-hotel-billing-vertical | 无 PMS 走前台话机功能键办入住退房+客房计费是 Hotel 双路线场景 |
| should-hotel-02 | oxoa-hotel-billing-vertical | 话费小票与账号码分项目归属属计费通道与账号码能力 |
| should-sec-01 | oxoa-security-hardening | 默认密码与不用端口处理是安全加固基线核心项 |
| should-sec-02 | oxoa-voicemail-mobility | VMU 锁定翻倍与五途解锁正是该能力描述内容 |
| should-cert-01 | oxoa-certificate-suite | SIP 中继 TLS/SRTP（OCE 原生）在该能力描述内 |
| should-cert-02 | oxoa-certificate-suite | 2K↔4K 迁移回滚铁律对应证书升 4096 后回滚版本 |
| should-att-01 | oxoa-attendant-suite | AA 两棵树日夜两套菜单正是 AA 能力 |
| should-att-02 | oxoa-attendant-suite | 客户编码验证后转组是 SCR 客户码能力 |
| should-vm-01 | oxoa-voicemail-mobility | 来话转手机且回拨显本机分机是游牧模式场景 |
| should-vm-02 | oxoa-voicemail-mobility | VM 远程接入三要素与防乱试密码锁定属该能力 |
| should-cloud-01 | oxoa-cloud-connect-fleet | Fleet 面板看全舰队版本并批量推软件更新是该能力主责 |
| should-cloud-02 | oxoa-cloud-connect-fleet | 远程维护四路径与 50443 入站端口在该能力内 |
| should-foun-01 | oxoa-foundation-ip | OMC 首连证书告警与 pbxk1064 仅首连正是交付地基场景 |
| should-foun-02 | oxoa-foundation-ip | IPDSP 安装前 NTP 未同步致 lanpbx 报错是该能力明确内容 |
| should-term-01 | oxoa-terminal-ecosystem | 第三方 SIP 话机注册端口/超时基线（5059/120 秒）在该能力内 |
| should-term-02 | oxoa-terminal-ecosystem | PIMphony 四 profile 与两级更新策略正是该能力 |
| should-shar-01 | oxoa-shared-devices | 开放工位随坐随用本分机即 Hot Desking |
| should-shar-02 | oxoa-shared-devices | 盯多路来电+弹窗蜂鸣通知即站群监督能力 |
| should-enti-01 | oxoa-multi-entity | 独立 MoH、话费各记是四实体多实体能力内容 |
| should-dect-01 | oxoa-dect-deployment | 基站数量估算与 -72dBm 覆盖勘测验收属 DECT 部署 |
| should-dect-02 | oxoa-dect-deployment | 批量刷固件即 SUOTA 并发 50 场景 |
| should-maint-01 | oxoa-maintenance-toolkit | 报障前一次性取全系统信息即 Webdiag 七块信息树 |
| should-maint-02 | oxoa-maintenance-toolkit | 改默认振铃节奏即 noteworthy 铃音基址范畴 |
| should-ars-03 | oxoa-numbering-ars-suite | 传真强制走 ISDN 是 ARS 表强制选路场景 |
| bait-sipnet-01 | oxoa-numbering-ars-suite | 中继已通后按前缀分运营商属 ARS 选路，非网关注册 |
| bait-cert-01 | oxoa-certificate-suite | TLS 握手失败排障首先命中证书套件的 TLS/SRTP 配置面 |
| bait-hotel-01 | none | 软件话务台与呼叫中心排队不在目录十四个能力任何一项内 |
| bait-sec-01 | oxoa-certificate-suite | DTLS 只保信令的边界知识在证书套件，不在安全加固 |
| bait-att-01 | oxoa-attendant-suite | 给 AA 加动态菜单首先命中 AA 语音导航能力 |
| bait-vm-01 | oxoa-voicemail-mobility | 游牧模式关键词直接命中 VM 与移动办公能力 |
| bait-cloud-01 | oxoa-cloud-connect-fleet | Rainbow 关键词首先命中 Cloud Connect 里的 Rainbow 业务目录同步 |
| bait-maint-01 | oxoa-maintenance-toolkit | 铃音地址无效即 noteworthy 铃音基址随版本变化知识点 |
| bait-dect-01 | oxoa-terminal-ecosystem | 8168s 是 WiFi 话机走 SIP 注册，属终端生态而非 DECT |
| edge-time-01 | oxoa-numbering-ars-suite | Internal ARS 分时段数值归属 ARS 套件 |
| edge-dhcp-01 | none | DHCP 池配置在目录十四个能力中无对应项 |
| edge-cloud-01 | oxoa-cloud-connect-fleet | Fleet 面板看不到设备正是该能力 24h 延迟知识点 |
