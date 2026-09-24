# FlexLM 许可证体系部署与更换（.ice/dongle/核验）

## R — 原文依据

> "The Flex-lm server can be embedded in the OTMC or installed on another server (which can be a virtual machine)."（p35）
> "THE OK STATUS INDICATES THAT THE LOCAL FILE IS PRESENT. BUT THE CONTENT (VALIDITY) OF THE FILE IS NOT CONTROLLED."（p77）
> "When a new license file is copied into $LICENSES_HOME directory, the FlexLM service must be restarted to load this new file (service flexlmd restart)"（p42）

出处：OTMCXTE200EN p16, p33-45, p76-77, p82（f06、p05、n06/n07/n08、c02 归并）。

## I — 自述

许可机制四层结构：

| 层 | 内容 |
|---|---|
| 许可文件 | `<license>.ice`，装入 $LICENSES_HOME（/var/data/licenses） |
| 控制者 | flex-lm 服务器：内嵌 OTMC，或装在另一台服务器（可以是虚机） |
| 绑定凭证 | 物理机 = ALUID（128 位硬件标识，整机贴纸有；仅购软件时用 /usr/bin/getaluid 取加密值）；虚拟机 = Aladdin USB dongle 的 dongle-ID |
| 核验 | $FLEXLM_HOME 下执行 ./lmutil lmstat –a |

三条硬规则：

1. 虚拟环境 dongle 必须挂到承载 FlexLM 的虚机——内嵌 FlexLM 挂 OTMC 虚机，外部 FlexLM 挂 FlexLM 虚机
2. 向导许可页 OK（及外部许可服务器配置完成）只代表"本地文件存在"，有效性与连通性不校验
3. 拷入新 .ice 后必须重启 flexlmd（stop/start 或 restart）才加载；Skip 跳过装许可不会中断安装，但手工补装前 OTMC 不会正常工作

## A1 — 书中案例

**向导内装许可 + 手工装/换许可**（c02 步骤 6-7、11-12）：

1. 向导 1.6 步：Server Type 选 Local（内嵌）或 External（另填主机/IP/域）
2. 虚拟环境先把 Aladdin USB dongle 加到承载 FlexLM 的虚机设置里
3. 许可文件步：Browse 选目录、勾选 .ice、Next（或 Skip 事后手工装）；页面 OK 仅代表文件存在
4. 手工装：SFTP 用 otuser 账号连 OTMC，把 .ice 拷入 /var/data/licenses
5. service flexlmd stop，等几分钟后 service flexlmd start
6. 到 $FLEXLM_HOME 执行 ./lmutil lmstat –a，确认许可服务器带新文件启动

## A2 — 未来触发

使用情境：扩容换许可；向导里 Skip 了许可怎么补；"许可显示 OK 但系统不正常"；虚拟化环境 dongle 挂哪；只买了软件没有整机怎么取 ALUID。

语言信号：许可 / license / .ice / FlexLM / flexlmd / lmstat / dongle / ALUID / getaluid / LICENSES_HOME / 扩容 / Skip。

与相邻能力区分：向导全流程 → otmsg-install-site-setup；OXE 侧话机用户许可（L173 等）核查 → otmsg-user-mailbox-provisioning。

## E — 可执行步骤

输入契约：.ice 许可文件到手（申领流程在书外）、FlexLM 拓扑已知（内嵌/外部）、otuser 凭据。没有许可文件 → 先走申领，不要用向导 OK 当通行证。

1. 定拓扑：内嵌或外部 FlexLM；虚拟环境确认 dongle 挂在承载 FlexLM 的虚机上。完成标准：绑定锚点正确
2. 部署文件：SFTP otuser 把 .ice 拷入 $LICENSES_HOME（/var/data/licenses）。完成标准：文件在位
3. 重启服务：service flexlmd stop → 等几分钟 → service flexlmd start。完成标准：服务带新文件启动
4. 核验：$FLEXLM_HOME 下 ./lmutil lmstat –a 输出含新许可。完成标准：许可有效可查
5. 归档：许可号/绑定 ID（ALUID 或 dongle-ID）/日期写入交付档案。完成标准：可追溯

判停点：

- 向导显示 OK 就当许可有效 → 停，必须 lmstat 复核（OK 只校验文件存在，n06）
- 扩容后用户开不出来 → 先查是否漏了 flexlmd 重启（n08）
- 虚拟环境 dongle 挂错虚机 → 停，换挂到承载 FlexLM 的虚机（n07）
- U 盘导许可读不到 → 核对虚机 USB 控制器声明、U 盘插在跑 vSphere 的 PC、经 vSphere 转给目标虚机（p77 Notes）

输出契约：flexlmd 运行且 lmstat 可查的许可状态 + 许可台账记录。

## B — 边界

- 正式许可文件的申领流程在书外；OTMC 无许可不会正常工作（p77 Tips）
- OTID 与 alchostid.cfg 出现在 p40 虚拟化许可综合图，书中未展开释义——不做外部补全
- 8770/OXE 各自的许可文件（.swk/.zip/hardware.mao/nmc.license8770 等）在各自系统部署，与本卡无关（p38/p40/p42）
- 实验许可环境（独立 FlexLM 虚机及其 IP）见 book/overview；本书版本口径为 OTMC R2.6 / 2.6.1
