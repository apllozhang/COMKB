# Book Overview（参考区）— OmniPCX Enterprise 系统装载

> 供能力卡引用的背景参考；源自 references.md 落位。

## 全书交付主线（组织轴）

全书交付主线按章节递进（p1-408）：先装起来、再连上云、最后换许可模型。

1. RLAB 实验环境
2. S.O.T. 部署工具
3. CS 软件加载三场景（单版本/补丁/多版本）
4. Easy Installation 分发器
5. OXE-V 虚拟化
6. GAS 一体机
7. Cloud Connect 云连接（FTR/RTR）
8. OPEX/Purple on Demand 订阅许可

## 实验环境（RLAB，仅 Boundary 背景）

- POD 池相互独立、配置相同；网段 192.168.1.0/24，网关 192.168.1.254，DNS 192.168.1.250，NTP 192.168.1.252，代理示例 192.168.1.253:3128，NAS 与 SIP 模拟器 12.0.0.2（p5-20）。
- 节点（实验口径）：PC Client 192.168.1.9（Administrator/superuser）；SOT VM 192.168.1.130（hosted 192.168.1.230）；CS3 csa 192.168.1.101 / csm 192.168.1.103
- 节点（实验口径，续）：KVM host 192.168.1.55（其上 OXE 192.168.1.201/203、OMS 192.168.1.213）；GAS 192.168.1.45（其上 OXE 192.168.1.1/1.3、OMS 192.168.1.13、WebRTC VM 192.168.1.15）
- 培训口令（实验口径）：Superuser2580*（OXE/SOT 四账户改后值）、letacla（SOT/OMS 出厂）、letacla1（GAS/OMS 出厂）、rainbow/Rainbow123（WebRTC VM）、ESXi root/Superuser-X*（X=POD 号）；SOT 媒体通道 upload/sot（FTP/SFTP 2222）。
- 路径口径：OXE swk 恢复 /usr4/BACKUP/OPS；FlexLM 许可 /opt/Alcatel-Lucent/data/licenses；GAS 备份 /var/backup；GAS 加载约 60 分钟、后安装约 15-20 分钟（培训环境实测）。

## 平台速览（方案沟通素材）

- S.O.T.：Standalone（笔记本加物理机）与 Hosted（ESXi 加虚机）两模式；default 与 Template Factory（含降级模式）两配置；一次只允许一个部署任务（p22-35）。
- 双分区升级模型：第二版本不停话音装好、切换才重启；静态补丁停话音（或装 inactive）、动态补丁热装但排静态之后（p65-66、p71-77）。
- 虚拟化矩阵：FlexLM+加密狗仅 ESXi/KVM；Hyper-V/Nutanix/AWS 强制 Cloud Connect；FlexLM 与 RTR 互斥（p134-136、p331）。
- GAS：Rocky+KVM 打包三 VM；WebRTC 网关 50 并发封顶、>7000 用户外部网关；OMS 每 GAS 限 1 台（p225-226）。
- Cloud Connect：出站 443/80/53 连 connect2.opentouch.com；TLS 1.2；OXE 主动发起、零改动入云（p286-290）。
- RTR：资格期 30 天起、OK 加 0.5 天/NOK 减 1 天；归零 panic（话机显示 "Call your administrator"）（p304）。
- OPEX/PoD：lock 431=1、24 项订阅、每 4 小时与 LMS 对账；lms/oxe 计数不一致即 panic（p351-354、p371、p397）。

## 教材口径声明

- 全部实验密码/账号/网段仅限实验环境；生产必须替换并做安全加固（aging=0 触发 CIS_Benchmark_Req.No_5.6.1.1 警告，p91/p175/p273）。
- 生产化边界四文档：TBE043（虚拟化设计）、TC3138（GAS 安装）、TC3104en-Ed08（N3 迁移）、8AL91032ENBD（OXE 安装手册）——均为原书指定权威来源；OXE 业务配置指向 Starter 课程。
- 版本敏感点：虚拟化平台矩阵为 Ed12 时点值（演进以 TBE043 为准）；vSphere thick client 仅到 ESXi 6.0（p199）；PoD 目录 24 项与件号为商务快照。
- 口径冲突记录：RTR 失败重试双口径（p308 与 p332，needs-review nr-01）；p404 Voice Agent(CCD) 计数示例排版错误（nr-02）。
