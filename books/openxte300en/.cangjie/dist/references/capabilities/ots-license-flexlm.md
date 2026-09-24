# 许可体系与 FlexLM（三族文件、锚定物、核查与外部切换）

## R — 原文依据

> "OpenTouch license file: <OT license>.ice • OmniPCX Enterprise license file: software.swk ... <OXE license>.ice if OXE-v (Flexlm control) • OmniVista 8770 license file: xxx.sw8770"（p130）
> "IN OPENTOUCH, ALUID IS THE ELEMENT USED IN CASE OF PHYSICAL SERVER DEPLOYMENT (OTMS, OTMC) TO CONTROL THE LICENSE. USB DONGLE IS USED ONLY IN CASE OF VIRTUALIZATION."（p162）
> ""PANIC flag" value must be "0" otherwise it means that the licenses are locked "Panic Flex" value must be "0" otherwise it means that the FlexLM server is unreachable"（p159）
> "For security reasons, the standard FTP protocol cannot be used for the license server. Copy the license file with SFTP (Secure FTP), or SCP"（p177）
> "Enter the command: ot-config.sh --external_flex ... The operation takes about 5 minutes."（p184-185）

出处：OPENXTE300EN p128-185。

## I — 自述

许可自成一体，四层结构：文件族、锚定物、FlexLM 形态、目录流转。三族文件对照：

| 文件族 | 文件 | 适用产品 | 校验方式 |
|---|---|---|---|
| .ice | <OT license>.ice | OTMS / OTMS-v | FlexLM：物理机锚 ALUID，虚拟机锚加密狗 |
| .ice | <OXE license>.ice | OXE-v | FlexLM 只验 Product ID（容量仍看本地 .swk） |
| .swk | <offer ID>.swk | OXE | 专有加密；物理机 CPUID 验证；容量口径的真正载体 |
| .sw8770 | 改名 nmc.license | OmniVista 8770 | 8770 自查 handle，与 OXE .swk 内 Handle 4760 对应 |

目录流转与生效条件：

- 向导或手动把 .ice 放入 $LICENSES_HOME（内嵌 /var/data/licenses，外部 /opt/Alcatel-Lucent/data/licenses）
- Flexlm 服务启动时复制改名进 final_licenses，文件名含锚定物（ALUID_xxx、FLEXID_x-xxx、SERVERMACADDRESS_<接口> 或 ANY）
- OXE 的 .ice 另进 final_licenses/oxes；手动换文件后必须 service flexlmd stop/start 才生效

核查三件套：

- **spadmin**（OXE 控制台 mtcl）：选 1 看三个 PANIC 计数，全 0 才健康；选 2 读 Product-Id 与 Handle 4760。
- **lmutil**（$FLEXLM_HOME 下）：lmstat 看服务 UP、lmstat -a 看各 FEATURE 已发与在用量、lmhostid -flexid 读加密狗 ID。
- **checkLicensing.sh**：OT 与 FlexLM 两侧各跑一遍，输出主机信息、许可清单、活动测试与问题计数，并打包日志 zip。

外部 FlexLM 三条规则：许可文件必须含 Dongle ID、OT ID、OXE 产品 ID 三要素；传输只许 SFTP/SCP（标准 FTP 被禁）；SFTP 落地在 /root，必须再移动进许可目录并重启 flexlmd。

## A1 — 书中案例

**许可核查实验**（p155-166）：

1. 向导装入 .ice 后核许可目录与 final_licenses 生成。
2. OXE 也用 FlexLM 时，经 SFTP 把 OXE.ice 传到 OT 并复制进许可目录。
3. root 执行 service flexlmd restart 并确认 oxes 子目录出现。
4. OXE Webadmin 或 mgr 的 System/Licenses 配 FlexLM 字段。
5. 字段口径：Enabled=Yes、端口 27000、ProductID discovery=Yes、Use Flex License=No。
6. 改完 FlexLM 字段必须重启 OXE 才生效。
7. mtcl 登录 OXE 跑 spadmin 选 1，三个 PANIC 计数应全为 0。
8. spadmin 选 2 抄 Product-Id 与 Handle 4760，对应 .ice 的 FEATURE 行。
9. 物理机 getaluid 抄 ALUID；虚拟化用 lmhostid -flexid 读加密狗。
10. OT 与 FlexLM 两侧各跑 checkLicensing.sh，问题计数应为 0。

**外部 FlexLM 与切换**（p167-185）：

1. 部署 FlexLM 虚机并配网络（OVF 从 My Portal 下载）。
2. 现场给 FlexLM 虚机挂 USB Device；内嵌 FlexLM 还需先挂 USB Controller。
3. SFTP 传许可文件后从 /root 移入许可目录并重启 flexlmd。
4. 两侧跑 checkLicensing.sh 核验后，OT 上以 root 执行 ot-config.sh --external_flex。
5. 向导填外部 FlexLM 参数，Finish 后约 5 分钟完成。
6. 验证 checkAll.sh 全绿，必要时 service opentouchd restart。

## A2 — 未来触发

使用情境：向导宣布"许可 OK"但不放心；spadmin 的 PANIC 计数不为 0；多台 OXE 共用一台 FlexLM；要外置许可服务器；rehosting 涉及换 FlexLM 形态。

语言信号：FlexLM / .ice / .swk / sw8770 / nmc.license / ALUID / 加密狗 / dongle / spadmin / lmutil / checkLicensing / final_licenses / PANIC / 27000 / getaluid / 外部许可服务器。

与相邻能力区分：向导内许可步骤 → 初始化向导能力；rehosting 里的许可联动 → 维护与 rehosting 能力；OXE 用户数扩容走 .swk 采购，FlexLM 上没有"改容量"的操作。

## E — 可执行步骤

输入契约：许可文件与采购清单（.ice/.swk/.sw8770）；部署形态（物理/虚拟化）；FlexLM 形态（内嵌/外部）；OT root 与 OXE mtcl 访问权。

1. 对单：OT 用 .ice、OXE 用 .swk（OXE-v 另有 .ice）、8770 用 .sw8770 改名 nmc.license
2. 落位：内嵌放 /var/data/licenses；外部放 /opt/Alcatel-Lucent/data/licenses。完成标准：路径与形态匹配
3. 重启 flexlmd 并核 final_licenses 命名。完成标准：文件名含 ALUID/FLEXID/MAC 之一且与锚定物匹配
4. OXE 配 FlexLM 字段并重启；spadmin 三计数全 0。完成标准：PANIC/Panic Flex/Panic SWK 均为 0
5. 深查：lmstat -a 看 FEATURE 用量；checkLicensing.sh 两侧跑并留 zip。完成标准：问题计数 0
6. 外部化切换：先装外部 FlexLM 并绑加密狗，再 ot-config.sh --external_flex。完成标准：checkAll.sh 全绿

判停点：

- 许可 OK 但功能异常 → OK 只代表文件在，跑 checkLicensing.sh 与 spadmin 深查
- SFTP 后文件还在 /root → 没移进许可目录等于白传，补移动再重启 flexlmd
- 第二台 OXE 想共用同一份许可 → 不行，checkout 即独占，按台数采购
- 改了 OXE 的 FlexLM 字段"没生效" → 必须重启 OXE（p159）
- FlexLM 虚机想改系统语言 → 保持 CentOS 默认，勿改（p172）

输出契约：许可健康结论（三计数、FEATURE 用量、锚定物匹配）+ final_licenses 清单 + 外部切换记录（如执行）。

## B — 边界

- 实验口径（生产必须替换）：内嵌 FlexLM 即 OT 服务器 192.168.1.50；外部 FlexLM 虚机 192.168.1.80（flex.company.com），首登 root/letacla 强制改密。
- R-Lab 特例：许可锚 MAC 而非加密狗，跳过 USB 挂接；现场虚拟化必须加密狗（n10，见 needs-review nr-04）。
- 容量口径（用户数、中继组）在 OXE 本地 .swk，FlexLM 只验 Product ID；OXE 亦可用 Cloud Connect 控制许可（p130/132，本书不展开）。
- License_release 值：10 对应 R2.4、11 对应 R2.5；R2.6.1 时代装新许可需核对文件内版本值（p154）。
- alchostid.cfg 为 OT-v 外部 FlexLM 场景的 OTID 节流文件，随 Flexlm 服务启动生成（p142-153）。
- rehosting 换 FlexLM 形态的许可适配走 eBP（Siebel 工单），有商务周期——详见维护与 rehosting 能力卡。
