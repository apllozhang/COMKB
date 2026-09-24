# DECT 手机自动重注册（dectinston -update / -forceUpdate / -f 批量）

## R — 原文依据

> "New PARI as close as possible of the existing ones ... PARI and PLI are compatible with the existing system, the handset moves to new PARI immediately after ... Use the option '- update'"（p254）
> "For an installation where PARI needs to be changed, automatic re-registration must be done before changing the system PARI. ... the handsets are no longer able to communicate with the system, as soon as they receive their new configuration"（p255）
> "Total duration of a batch of handsets update is proportional to the duration of one set (2 -3s) ... Paging of the handsets: from 1,3s for a reachable handset to 6,5s for a handset that is out of coverage"（p253）
> "Handset that are not under radio coverage of their installation node cannot be updated • Handsets off when the command is launched • Handsets connected to a visited node in case of OXE DECT networking"（p253）

出处：DECTXTE200EN p249-262。

## I — 自述

PARI/PLI 变更的零接触迁移工具：手机不动手，由系统推新标识。决策规则二选一：

| 场景 | 选项 | 要点 |
|---|---|---|
| 新 PARI 与旧 PARI 高位兼容（相近） | -update | 手机立即迁移、业务不断 |
| PARI 彻底变化 | -forceUpdate | 顺序铁律：先推手机、后改系统 PARI |

命令形态：`dectinston -update <dn> -pari <八进制> -pli <十进制>`；批量用 `-f <文件>`（清单传到 /tmpd，每行一个目录号，# 开头为注释行）。

性能与安全口径（p253）：单机全程 2-3 秒（paging 1,3s 可达 / 6,5s 出覆盖，默认 5 次寻呼重传；过程本体约 800ms），批量时长≈单机×台数；安全级别保持不变、UAK 不重算、密钥永不上空口。

三类覆盖不了的手机（p253）：关机的、不在安装节点覆盖内的、漫游到访问节点的。机型前提（p252）：82x4 全系支持；8262 需 v5580b0007/v5680b0005、8262 Ex 需 v7381b0009、8214/8234/8244/8254 无最低版本。

## A1 — 书中案例

**单机与批量重注册实验**（p259-262）：

1. 前置：系统 PLI 已调 30，xBS 新 PARI=10000410114（实验口径）
2. 单机：dectinston -update 31015 -pari 10000410114 -pli 30 → 回显核对 → "31015 re-installed successfully!!!"
3. 批量准备：DECT.txt 写入 31016/31017 → FTP/SFTP 传 /tmpd
4. 批量执行：cd /tmpd → dectinston -update -f DECT.txt -pari 10000410114 -pli 30 → "Process Completed!!"
5. 结果核验：more ReinstallSuccessHandsetsList.txt（含命令头注释）与 ReinstallNOKHandsetsList.txt（应为空）

## A2 — 未来触发

使用情境：PARI 变更迁移；混合模式后推新标识；换号段批量迁移；重注册失败清单处理；估算迁移窗口时长。

语言信号：自动重注册 / re-registration / -update / -forceUpdate / -pari / -pli / DECT.txt / /tmpd / ReinstallSuccess / ReinstallNOK / 批量迁移 / 访问节点 / visited node。

与相邻能力区分：PARI/PLI 该取什么值见标识号码能力；混合部署的全局配置见混合部署能力；固件版本不达标先升级见固件管理能力。

## E — 可执行步骤

输入契约：新旧 PARI/PLI 对照、在册手机清单、维护窗口。手机固件不达 p252 版本表 → 先升固件（OTA 或 UST+USB）。

1. 判路线：新旧 PARI 高位兼容 → -update；彻底变化 → -forceUpdate。完成标准：路线与顺序确定
2. 拉在线清单：确认手机已注册、在运行、在安装节点覆盖内。完成标准：目标集可达
3. 单机试跑：dectinston -update <dn> -pari ... -pli ...，核对回显。完成标准：试跑机 re-installed successfully
4. 批量下发：DECT.txt 传 /tmpd → dectinston -update -f DECT.txt -pari ... -pli ...。完成标准：Process Completed
5. 核结果：more 两个结果文件，NOK 清单应为空。完成标准：成功清单=预期台数
6. （-forceUpdate 时）改系统 PARI：成功清单达标后才动系统配置。完成标准：系统与手机标识一致

判停点：

- 想先改系统 PARI 再推送（-forceUpdate 路线）→ 停，顺序不可逆：手机收到新配置即与旧系统断联，推送通道消失，全部沦为手工重装（p255）
- NOK 清单非空且系统已改 → 这些手机只能现场手工注册，排产时预留
- 手机在访问节点/关机 → 更新不了（p253），等回安装节点重跑，不要算作失败返工
- 8262 老固件报不支持 → 查 p252 版本表，先 OTA 或 USB 升级

输出契约：迁移执行单（路线/清单/窗口）+ ReinstallSuccess/NOK 双清单存档 + 系统变更记录。

## B — 边界

- 2-3s/机是"过程"时长，paging 部分随覆盖状态浮动（1,3s-6,5s）；窗口按单机×台数线性估算并留余量
- -update 失败时手机保留原参数不受影响（p251）；-forceUpdate 失败机在系统改完后无法远程补救
- UAK 不重算、密钥不上空口是安全口径（p253）；生产密钥治理策略在书外
- 结果文件生成在输入文件同目录（/tmpd）；文件名以当版为准
- "All 82x4 handsets are supported"不含 82x2 系列（p252 标题口径）
