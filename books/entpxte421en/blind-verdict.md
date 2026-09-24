# 判卷报告 entpxte421en（oxe-native-encryption）

## 汇总

| 类型 | 通过 / 总数 |
|---|---|
| should_trigger | 22 / 22 |
| should_not_trigger | 9 / 12 |
| edge_case | 5 / 5 |
| **总计** | **36 / 39** |

## Fail 明细

### bait-eegw-01
- 预期：按 1500 分界留在开通/规划口径（500 路内嵌 EGW 够用），不应激活 enc-eegw-deployment 直接进入部署
- 盲判：enc-eegw-deployment
- 偏差分析：盲判把"容量分界查询"等同于"EEGW 部署能力"。根因在目录结构：1500/15000 分界与许可公式写在 enc-eegw-deployment 描述里，而"是否需要 EEGW"的规划判断按预期应归开通/规划口径，不触发部署能力。盲判顺着目录措辞走了，属于目录描述边界诱发的可解释误路由。

### bait-app-01
- 预期：超范围题，应声明边界（HTTPS 下载前提是 NE 已激活，p73），而非激活 enc-application-encryption 硬配
- 盲判：enc-application-encryption
- 偏差分析：目录描述明文含"HTTPS 替代 TFTP 的前提（NE+DHCP option 66）"，盲判据此直配该能力。但题面问的是"没开原生加密能不能改 HTTPS"，考点是识别前提不满足并声明边界，盲判没有做前提检查这一步。

### bait-lab-01
- 预期：拒绝并声明实验口径边界，不应激活 enc-lab-environment 当作生产配置依据
- 盲判：enc-lab-environment（理由已注明"识别其不得用于生产属该能力边界"）
- 偏差分析：盲判识别出了实验口径风险（理由正确），但路由仍落在被禁能力上。预期要求的是拒绝式边界声明，激活实验环境能力本身即判 fail。属"判断对、路由错"的边界型失分。

## 判卷口径备注
- "激活 A（或 B）"类预期命中任一即 pass（should-bringup-03 命中 enc-native-encryption-bringup 主预期，pass）。
- edge_case 按"路由合理或声明边界即 pass"执行，5 条全部通过（edge-port-01 精确命中 0 覆盖陷阱条目）。
