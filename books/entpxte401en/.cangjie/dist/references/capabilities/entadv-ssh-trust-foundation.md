# SSH 免密分发体系（oxe-ssh-auth 对机 / oxe-nw-sshkey-sync 全网）

## R — 原文依据

> "From N3 onwards, for security reasons SSHv2 is enabled by default with public key authentication. … Host based authentication is no longer supported, thanks to CIS compliance requirements."（p57）
> "Before starting the synchronization, the tool checks if passwordless connectivity already exists … and starts synchronizing the keys only if it does not exist already."（p60）
> "Usage: oxe-nw-sshkey-sync –f <.csv file> … <Main CS IP Address, Node X>,<mtcl password>,<swinst password>,<root password>,<log file>"（p64）
> "Password CSV file ssh_multi.csv, Config(/tmpd/config) folders are cleared ! Done !!!"（p206）

出处：ENTPXTE401EN p55-68, p203-208。

## I — 自述

N3 起 SSHv2+公钥认证是每台 OXE 的默认基线，host-based 认证已被 CIS 合规移除。mastercopy、pcscopy、audit、broadcast 全部依赖免密——密钥没分发，这些功能必失败。三层结构：

1. **机制层**：mtcl/swinst/root 三账户在每台 CS 各持独立密钥对；授权表为各账户 .ssh 下的 authorized_keys
2. **对机工具 oxe-ssh-auth -c <远端IP>**：root 执行，处理"一对"OXE；先检查免密是否已存在，已同步则跳过；可选"同一密码套用本地与远端全部三账户"（默认 y）
3. **全网工具 oxe-nw-sshkey-sync -f <csv>**：从主 CS 运行时自动按 MAO 推导 twin/PCS/网络节点/4645 清单，先主 CS 后 twin CS 逐对同步；全网每节点各跑一次即可；结束时自动删除 csv 与凭证目录，日志归档 /tmpd/oxenwsynclogs.zip

密钥存储路径（p67）：

| 账户 | 私钥/公钥路径 | 授权表 |
|---|---|---|
| mtcl | /usr2/mtcl/.ssh/id_rsa(.pub) | /usr2/mtcl/.ssh/authorized_keys |
| swinst | /usr2/soft_install/bin/.ssh/id_rsa(.pub) | 同目录 authorized_keys |
| root | /root/.ssh/id_rsa(.pub) | 同目录 authorized_keys |

## A1 — 书中案例

**对机同步（本地冗余实验，p100-103）**：

1. root 登录 csa 执行 oxe-ssh-auth -c 192.168.1.2（实验口径）
2. 输入远端 mtcl 密码；"同一密码套用全部账户"选 y
3. 工具输出 All Done OK!!!；两侧 more authorized_keys 各含 6 条公钥（2 机×3 账户）

**全网同步（PCS 实验，p203-208）**：

1. 准备 /tmpd/ssh_multi.csv：每行"IP,节点名>,mtcl 密码>,swinst 密码>,root 密码>,日志文件"
2. root 执行 oxe-nw-sshkey-sync -f /tmpd/ssh_multi.csv（含 csa/csb/pcs 三节点）
3. 完成后 csv 自动删除；root 解压 oxenwsynclogs.zip 查 /tmpd/logs/oxenwsync.log
4. 核验：authorized_keys 共 9 条（3 节点×3 账户）

## A2 — 未来触发

使用情境：mastercopy/pcscopy/audit/broadcast 报认证失败；新装冗余对/PCS/网络节点后的初始化；换密码后免密失效；怀疑 host-based 老脚本失效。

语言信号：SSH 免密 / public key / oxe-ssh-auth / oxe-nw-sshkey-sync / ssh_multi.csv / authorized_keys / 密钥分发 / scp 失败 / N3。

与相邻能力区分：免密建好后做库克隆与切换 → CS 冗余能力；audit/broadcast 前提核查 → 数据一致性能力。

## E — 可执行步骤

输入契约：root 权限、两端（或全网）mtcl/swinst/root 密码、CS 间防火墙互信（trusted hosts）。缺 root 或密码 → 判停，不要试图绕过认证。

1. 前提核查：确认两侧版本 ≥N3、防火墙已互信。完成标准：CS 间 22 端口可达且未被防火墙拒
2. 单对场景：root 执行 oxe-ssh-auth -c <远端IP>，按提示输密码（可复用同一密码）。完成标准：输出 All Done OK!!!
3. 全网场景：备好五段式 CSV → 每节点各跑一次 oxe-nw-sshkey-sync -f。完成标准：csv 自动删除且日志归档成功
4. 核验：more /usr2/mtcl/.ssh/authorized_keys 数公钥条数（两机 6 条、三机 9 条）。完成标准：条数与节点×账户数一致且含对端公钥
5. 联动验证：跑一次目标功能（如 pcscopy）确认免密生效。完成标准：目标功能无认证报错

判停点：

- mastercopy 报 scp/授权失败 → 先回到本卡核验 authorized_keys，再查是否在正确的机器上执行
- authorized_keys 条数不符 → 重跑对应工具（工具自带幂等：已同步会跳过）
- 老 host-based 免密脚本失效 → CIS 合规移除（p57），改走三账户密钥分发，不降级 SSH 配置

输出契约：全网免密互通的三账户密钥体系 + authorized_keys 条数核验记录。

## B — 边界

- 全部协同功能依赖本卡；免密未建立时不要先排查目标功能本身（p57/p71）
- csv 中含明文密码：工具结束自动删除 csv 与 config 目录（p206），不要自行留副本
- 生产系统的口令治理与证书轮换不在本书范围（实验口径明文口令仅限 RLAB）
- 防火墙 trusted hosts 配置本身属 netadmin 维护域（本书在冗余/audit 章内嵌教学，无独立章）
