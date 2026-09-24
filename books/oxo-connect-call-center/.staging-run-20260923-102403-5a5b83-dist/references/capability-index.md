# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| cap.oxo-cc.basic-setup | OXO Connect 基础 ACD 全流程搭建 | critical | 从零搭建 OXO ACD；新建呼叫中心组；ACD 初始配置；configure ACD on OXO Connect | ACD Setup、向导、DDI、状态前缀 501-504、hunting group、voice mailbox、ACD 引擎重启、Line parameters、rank | capabilities/oxo-acd-basic-setup.md |
| cap.oxo-cc.call-scenarios | ACD 呼入六场景排障 | critical | 来电被挂断/排队/没铃声；ACD 呼入行为异常；caller behavior troubleshooting；为什么电话直接被劝退 | 六场景、Opening hours、queue full、dissuasion、劝漏、端口全忙、全员登出、transfer number、closed、welcoming message | capabilities/oxo-acd-call-scenarios.md |
| cap.oxo-cc.routing | 呼叫特征化与 Smart Call Routing 路由表设计 | high | 按客户/国家分流来电；配置 Smart Call Routing；大客户专线分组；call routing by CLI DDI | call characterization、Line parameters、Smart Call Routing、CLI、DDI、路由表、分流、优先级 | capabilities/oxo-acd-routing.md |
| cap.oxo-cc.queue | ACD 等待队列管理（容量公式与出口配置） | high | 队列长度怎么设；排队等待时间播报；queue length；estimated waiting time；队满了还来电 | queue、N×K、traffic factor、话务因子、等待时间、星号退出、Call management、劝漏出口 | capabilities/oxo-acd-queue.md |
| cap.oxo-cc.search-noanswer | 坐席搜索模式选型与无应答处理 | high | 话务怎么在坐席间分配；坐席被自动签出；ringing duration；无应答自动移除；search mode 选哪种 | search mode、Fixed、Rotating、Longest idle、rank、priority order、maximum ringing duration、automatically removed、off duty | capabilities/oxo-acd-search-noanswer.md |
| cap.oxo-cc.login-status | 坐席签入签出（free seating）与状态排障 | critical | 坐席怎么登录/签出；登录了却不接电话；话机显示 1:01；ACD tab；free seating；agent login logout | login、logout、ACD prefix、base0 base1、free seating、ACDAutoLog、状态码、501 502 503 504、On duty、Off duty | capabilities/oxo-acd-login-status.md |
| cap.oxo-cc.multi-secretary | Multi-Secretary 多秘书方案配置 | high | 多经理共享秘书；秘书台显示老板名字；multi secretary；领导秘书分机方案 | Multi-Secretary、multi-secretary mode、collective speed dialing、医生/经理 DDI、Secretary、rank 1、programming order | capabilities/oxo-multi-secretary.md |
| cap.oxo-cc.omc-first-connect | OMC 安装与首次连接 | high | 装 OMC；连不上 OXO；安全告警反复弹；OMC installation；pbxk1064 | OMC、Expert mode、Server authentication、certificate、pbxk1064、192.168.92.246 | capabilities/oxo-omc-first-connect.md |
| cap.oxo-cc.ip-planning | OXO 与客户端 IP 规划修改 | medium | 改 OXO IP；换网段；DHCP 地址池；change IP settings | IP configuration、Main CPU、DHCP range、192.168.1.246、网关、DNS | capabilities/oxo-ip-replan.md |
| cap.oxo-cc.schedule-calendar | ACD 营业时段与例外日配置 | medium | 设置营业时间；节假日关闭；exceptional days；opening hours | Opening criteria、Exceptional days、时段、节假日、40/10/2 上限 | capabilities/oxo-acd-schedule-calendar.md |
| cap.oxo-cc.supervisor-app | Supervisor 班长台部署与实时监控 | high | 装班长监控台；实时看坐席状态；坐席显示忙却不接；supervisor application；activity rate | Supervisor application、ACD Admin、Acdc1064、activity rate、八子态、On hold、Being routed | capabilities/oxo-supervisor-app.md |
| cap.oxo-cc.agent-app | Agent 坐席席面部署（弹屏/打标/客户库） | high | 装坐席软件；来电弹屏；通话分类打标；agent application；screen popup | Agent application、PC/terminal association、Types、call qualification、screen popup、contact database、PIMphony | capabilities/oxo-agent-app.md |
| cap.oxo-cc.statistics-app | Statistics 统计应用与报表导出 | medium | 看来话量报表；坐席统计；导出统计；statistics application；S1 S2 threshold | Statistics Manager、S1/S2、Group statistics、Agent statistics、CSV、binary export、automatic printout | capabilities/oxo-statistics-app.md |
| cap.oxo-cc.dtmf-popup | DTMF 客户码识别弹屏 | medium | 客户来电弹资料；输码识别客户；DTMF client code；customer code popup | DTMF、customer code、107.wav、automatic screen pop up、line parameters | capabilities/oxo-dtmf-client-popup.md |
| cap.oxo-cc.voice-prompts | ACD 语音提示定制 | medium | 定制欢迎语；换提示音；voice prompts；101.wav；录音上传 | voice guide、wav、101.wav 102.wav 107.wav、MMC session、Transfer mode、ACD Voice messages | capabilities/oxo-acd-voice-prompts.md |
