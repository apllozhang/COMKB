# otccxte101en 判卷报告

判卷方式：blind-results.md（判卷前锁定）逐条对比 test-prompts.json 的 type 与 expected_behavior。

## 汇总

| 类别 | 结果 | 通过率 |
| --- | --- | --- |
| should_trigger | 24/24 | 100% |
| should_not_trigger | 12/12 | 100% |
| edge_case | 3/3 | 100% |
| 总计 | 39/39 | 100% |

## Fail 明细

无。

## 判卷备注（pass 但有判读空间的条目）

- bait-remote-01（none，pass）：expected"超出本书范围、应声明边界指向 OXE 组网文档、不应虚构步骤"，盲判 none 与"超范围+声明边界"一致。
- bait-ism-01 / bait-acro-01（otcad-asm-script-advanced，pass）：expected 给出"转 otcad-asm-script-advanced 或姊妹技能"的弹性口径，盲判命中 asm-script-advanced 即 pass；若实际目录无姊妹技能条目，该路由为唯一正确项。
- edge-remote-01（otcad-remote-pg-mutual-aid，pass）：expected 核心是"MWT=0 为零等待队列"的语义澄清，出处即互助水位参数 MWT 0-3276 秒，盲判路由到 remote-pg 合理；edge 规则本身也不强求特定 slug。
- edge-ism-01 / edge-ccss-01：盲判均落在口径出处能力（5 分钟刷新口径、>9 强制上 Server 口径），路由合理，pass。
