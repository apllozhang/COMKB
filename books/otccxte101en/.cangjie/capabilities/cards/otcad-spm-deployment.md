# Soft Panel Manager 部署（SPM 服务器、RTI Connector、FlexLM、基础设置与日统计）

## R — 原文依据

> "Install the Soft Panel Manager server • Launch ccdSoftpanel_setupx.x.x.x.exe … Install the RTI Connector application … Install the FlexLM server • Launch the installation file: ALE-FLEXlmServer-11.15.exe"（p389-390）
> "WHEN CCS AND RTI CONNECTOR ARE INSTALLED ON THE SAME PHYSICAL SERVER, THE CCS MUST BE DEDICATED TO THE RTI CONNECTOR. YOU MUST NOT START THE CCS MANUALLY IF THE RTI CONNECTOR IS RUNNING."（p405）
> "afe.sites OXE main CPU address … These statistics are retrieved every 15 minutes and reset to 0 at 00h00. This time can't be reduced"（p416-417）

出处：OTCCXTE101EN p371-417。

## I — 自述

SPM 是独立于 CCS 的实时统计上墙方案，数据链为：OXE CCD > CCS > RTI Connector（Windows 服务）> SPM 服务器（Tomcat，wbm 应用，默认端口 9060）> 墙板/液晶/Panel PC 显示 + 邮件告警。部署三件套缺一不可：

| 组件 | 形态 | 要点 |
|---|---|---|
| SPM 服务器 | ccdSoftpanel_setup，Tomcat 9060 | 装后核 SoftPanelServer 服务自启；wbm 登录 admin/admin（实验口径） |
| RTI Connector | RTIConnector 安装器，装为服务 | 前提：同机 CCS 已装且配好 OXE 连接；断连每 5 秒重试；启动即全量拉取 CCD 对象 |
| FlexLM 服务器 | ALE-FLEXlmServer + softpanel.lic | LMTOOLS 验证 Start Server 与 Status Enquiry；许可全程在线校验 |

独享服务器门槛（任一命中建议独享，p386）：统计+计算数据 >500、同时管理用户 >5、面板（硬+软）>10。最低配置 2.4 GHz 双核/4 GB 内存/50 GB 磁盘。

Settings 四区与日统计：

| 配置区 | 要点 |
|---|---|
| General | 服务器 IP；Tomcat 端口装后不可改 |
| License Server | FlexLM 主机默认 localhost、端口默认 27000 |
| Mail Configuration | SMTP+发件凭据，可发测试邮件（告警邮件的前提） |
| CCD Filters | 统计可用性总开关，勾选后必须 Save；AgentWidget 依赖 ServiceState/PhoneStat/StateDuration 三统计 |

日统计：编辑 afe.properties（afe.sites=OXE 主 CPU 地址、afe.pilots 留空=全部），每 15 分钟取一次（不可更快），取数在每刻后 2 分钟，0 点清零，结果在 Real Time Data > Statistics > Ccd Consolidated。

## A1 — 书中案例

**三件套安装**（p396-417，装在实验 Client11，192.168.1.11）：

1. 前置：Client11 的 CCS 改指本地节点 Master PABX=192.168.1.3 并重登，核对后关闭 CCS
2. 装 SPM 服务器：运行 ccdSoftpanel_setup，端口 9060，装后核服务自启，Chrome 开 http://localhost:9060/wbm 登录
3. 核 OXE 侧 RTI 许可：mtcl 下 adm_acd option 15 或 spadmin，确认 103 号包（WBI Licence）
4. 装 RTI Connector：运行安装器，填 SPM 服务器 IP 192.168.1.11，核服务自动启动
5. 装 FlexLM：softpanel.lic 放 C:\FLEXlmServer\License，LMTOOLS 点 Start Server 后 Perform Status Enquiry
6. 基础设置：Settings 四区逐项配，CCD Filters 两页全勾后 Save
7. 日统计：afe.properties 填 afe.sites=192.168.1.3，核对 Ccd Consolidated 出现 S(站点)_(Pilot)_daily_* 统计

## A2 — 未来触发

使用情境：客户要上实时看板；SPM 装完统计不动；墙板数值冻结；要出日统计报表；评估要不要独享服务器。

语言信号：Soft Panel Manager / SPM / RTI Connector / FlexLM / LMTOOLS / 9060 / 61618 / wbm / CCD Filters / afe.properties / 日统计 / daily / 订阅 / 独享服务器 / 103 号包 / WBI。

与相邻能力区分：装好之后的视图/挂件/告警配置转 Soft Panel 可视化配置卡；CCS 本体安装转 CCS 安装与实验环境卡（路由卡）；许可采购属书外商务流程。

## E — 可执行步骤

输入契约：一台 Windows（10 64 位或 Server 2016/2019/2022）、CCS 已装且能连 OXE、softpanel.lic 许可文件在手。许可缺位 → 停，先走授权渠道，不虚构。

1. 核 OXE 侧 RTI 许可（103 号包）：spadmin 或 adm_acd option 15。完成标准：包存在且有效
2. 装 SPM 服务器并核服务自启，wbm 登录成功。完成标准：浏览器可开 http://<服务器>:9060/wbm
3. 装 RTI Connector 并核服务自启；同机时确认 CCS 专用于 RTI。完成标准：SPM 能看到全量 CCD 对象
4. 装 FlexLM 并导入许可，LMTOOLS 状态查询正常。完成标准：Status Enquiry 返回许可信息
5. Settings 四区配置（邮件 + CCD Filters 勾选后 Save）。完成标准：目标统计在挂件/告警中可选
6. 需要日统计时改 afe.properties 并核对 Ccd Consolidated。完成标准：S(站点)_(Pilot)_daily_* 出现

判停点：

- 墙板数值全部冻结且界面有告警横幅 → 停，先查许可（LMTOOLS/Check license），不要重启 RTI Connector（n23）
- 新配挂件第一分钟数值不动 → 停，统计按需订阅最多 1 分钟生效，先制造话务再等满 1 分钟（n22）
- 客户统计+面板规模超门槛 → 停，按 500/5/10 三条件评估独享服务器，别挤在 CCS 机上

输出契约：三服务运行记录 + 许可校验记录 + Settings/过滤器配置清单 +（可选）日统计对账口径。

## B — 边界

- 全部实验地址（192.168.1.11/192.168.1.3）与口令（admin/admin）为实验口径；生产必须替换并按安全基线加固（n01）
- SPM 服务器不支持装防火墙、管理浏览器不支持代理；端口放行 9060 与 61618（p387）；61618 与配置示例 61668 是两个角色，见 nr-06
- 订阅统计 ≤500、并发连接 ≤150、面板+墙板 ≤200（p394）；AFE 统计不支持空间冗余
- RTIConnector.ini 的 WBMHost/WBMPortNum 示例值为文档示例环境，非实验 POD 值（p391）
- CCS 版本基线 V10.2.92.0+、浏览器基线 120（p387）随 Edition 迭代，实施前复核发布说明
