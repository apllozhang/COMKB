# VAA 日常维护与版本升级（命令族、备份恢复、密码策略、告警日志）

## R — 原文依据

> "vaa stop Stop all VAA services except postgresql & nginx / vaa fullstop Stop all VAA services, and also postgresql & nginx / vaa start … vaa restart … vaa status Get status for all VAA services"（p278）
> "Once enabled, automatic database backup can't be disabled even if the option Backup activation is unchecked"（p294）
> "Newer version of the VAA may add new required parameters in the file, so just replacing it by the backup is not advised. Please check that the values are still the same and perform modifications if needed."（p308）
> "Since version A 4.6.104, password expiration is enabled by default. It is therefore strongly recommended to change the password of the administrator account before backing up the database"（p295，原文如此）

出处：VSAAXTE001EN p272-295, p296-299, p307-310。

## I — 自述

运维闭环的地图分七块：

1. **许可**：.lic/.vaa 绑定 MAC 且须含正确 FQDN（改主机名/换网卡即失效）

   - 安装目录 /etc/ale/aa-license-server，排障目录 /var/lib/ale/aa-license-server/
   - FEATURE 项含 AAIVR/AAPORTS/ECCSTART/VAA_RELEASE；运行态用 vaa services 看 VAA_PORTS/VAA_IVR/VAA_RELEASE 三项
2. **密码策略**：Web 界面密码最少 12 位含大小写/数字/特殊字符各 1；5 次失败锁定，管理员锁 2 小时自动解锁（sudo vaa conf unlockAdmin 全解）；默认有效期 92 天，到期前 30/7/1 天邮件提醒；参数在 Admin/Settings/Security parameters 可改
3. **服务与命令族**：vaa stop（停业务服务，保留 postgresql 与 nginx）/fullstop（全停）/start/restart/status/services/version（-d 看组件明细）；另有 conf https/telephony/backup/unlockAdmin/pcs、diag https、db 子族、cert 与 full 子族、ha 子族
4. **备份恢复三级**（详见下表）+ Web 端导出（全局 zip 含 wav / 按租户 zip 或 CSV / 树可 CSV 导出）；自动备份强烈建议启用——默认名 vaa.tar，Daily 午夜/Weekly 周日/Monthly 首日/自定义 cron，可推 NFS；一旦启用无法关闭；系统不监控备份占用的磁盘，按 6 个月 20GB 起预估
5. **日志与呼叫日志**：Web 界面五类日志（aa-media-server 主日志/aa-management/aa-engine/softcmp (SIP)/tts-hub）+ 文件系统路径；呼叫日志逐呼叫明细，点开可见所用节点及各节点时长，CSV 可导出
6. **告警**：邮件三类事件（SIP 中继断开/恢复、端口到许可上限、许可问题）；SNMP trap 同类事件但服务默认不启用；SMTP 改后必须重启服务
7. **版本升级**：备份先行（/etc/ale/vaa.conf + vaa db backup）；下载新包新许可并重跑 install.sh；逐值比对 vaa.conf（新版可能新增必需参数，不能拿旧备份直接覆盖，改过则 vaa restart）；HA 场景所有服务器同法升级后在 master 跑 vaa ha resync

备份三级对照：

| 级别 | 命令 | 覆盖内容 |
|---|---|---|
| vaa db | vaa db backup / restore | 仅数据库（.sql.gz 或 .tar，推荐 .sql.gz） |
| vaa cert | vaa cert backup / restore | /etc/nginx/certificate 目录 + nginx.conf + conf.d |
| vaa full | vaa full backup / restore | 数据库 + /etc/ale/vaa.conf + secureCall 两本证书（VAACertificate.jks / OXECertificate.pfs） |

## A1 — 书中案例

**版本升级操作序列**（p307-309，讲义级流程）：

1. 备份 /etc/ale/vaa.conf 与执行 vaa db backup
2. 从 MyPortal 下载新发行包与新许可并传服务器
3. 解压新发行包
4. 重跑 ./install.sh（4.8.006 口径即全新安装 + 恢复）
5. 逐值核对 /etc/ale/vaa.conf，按需补改新参数
6. 有改动则执行 vaa restart 生效
7. HA 场景：所有服务器完成升级后在 master 执行 vaa ha resync
8. （可选）S.O.T 自动升级：项目更新菜单选目标 Boot DVD 与 VAA 版本，提供 admin 密码

## A2 — 未来触发

使用情境：日常巡检；许可到期/失效排查；管理员被锁；备份策略设计；恢复演练；磁盘被备份吃满；告警收不到；版本升级规划。

语言信号：vaa status / vaa services / vaa.conf / 备份 / backup / restore / vaa db / vaa cert / vaa full / 自动备份 / NFS / 92 天 / 密码过期 / unlockAdmin / 日志 / logs / 告警 / SNMP / 升级 / update / resync。

与相邻能力区分：双机角色与 addslave/resync 细节归 HA 能力（本卡只讲 resync 在升级中的位置）；日志里的 SIP 交互排障归安装对接能力；统计报表归统计能力。

## E — 可执行步骤

输入契约：SSH 访问（admin + sudo）、备份存储位置（本地/NFS）、SMTP 已配置（告警前提）、客户变更窗口。

1. 日常巡检：vaa status/services 看服务与许可三项（VAA_PORTS/VAA_IVR/VAA_RELEASE）；Web 看 Supervision。完成标准：无异常服务、许可在期
2. 密码治理：核对有效期（92 天默认），到期前改密；被锁走 unlockAdmin 或等 2 小时。完成标准：无临期强管账号
3. 备份执行：按需 vaa db/cert/full 三级备份；确认自动备份已启用并核对 NFS 可写。完成标准：备份文件生成且可读
4. 恢复演练：vaa db restore（或对应级别 restore）后验证 Web 可登录、树可查。完成标准：演练通过并记录
5. 磁盘监护：人工盯备份占用（系统不监控），按 6 个月 20GB 起预估清理策略。完成标准：磁盘水位受控
6. 升级执行：按 A1 序列走，先改密后备份（防恢复后密码过期登不进），升级后逐值比对 vaa.conf。完成标准：新版本服务全 Running 且配置完整
7. HA 收尾：全员升级后在 master vaa ha resync。完成标准：双机配置一致

判停点：

- 恢复备份后登不进 Web → 停，密码过期陷阱（备份里封存的密码已过有效期）；走登录页 "Password or login lost" 或另一管理员 vaa db resetAccount [account]（n33）
- 想关闭自动备份 → 停，一旦启用无法关闭（连取消勾选都无效），只能规划共存（n32）
- WebAdmin Supervision 页想直接重启服务 → 停，原书明确"除非技术支持指示不要用"，走 SSH vaa restart（n15）
- 升级后拿旧 vaa.conf 直接覆盖 → 停，新版可能新增必需参数，必须逐值比对（n40）
- SNMP 平台收不到 trap → 先确认 SNMP 服务是否启用（默认关），再查网络（n34）

输出契约：巡检记录 + 三级备份文件清单与恢复演练结论 + 升级前后 vaa.conf 差异记录。

## B — 边界

- 实验口径：postgres 口令、管理员口令、5 端口 Release 11 许可——生产必须替换（n49）
- vaa db userreset 会把超管重置回 admin/admin——应急手段也是风险项（p04）
- 新建管理员默认密码=其用户名，建完必须立即改密（n13，归 WebAdmin 卡详述，本卡为密码治理关联）
- 命令全集与完整系统管理细节外置到安装手册第 6 章 VAA system management（n50）
- 邮件周报开关、报表口径归统计能力卡；PCS 同步命令（conf pcs/db sendBackup）归 PCS/OPEX 卡
- "先改密后备份"的顺序要求源自 p295 警告（原文 "version A 4.6.104" 笔误见 nr-05）
