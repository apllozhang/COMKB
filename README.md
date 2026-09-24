# COMKB · ALE Communications 技术培训知识库

ALE 通信产品线 **25 门官方售后（Postsales）培训教材** 的结构化整理：每本书蒸馏为可检索、可问答、可复用的能力卡（Capability Cards），并附带一个完整的培训门户站点与可复现的构建流水线。

- 在线门户（内网）：<http://10.20.30.103:8900/>
- 姊妹站：ALE 网络产品线培训门户（OmniSwitch / Stellar / OmniVista）
- 数据速览：**25 门课程 · 11,583 页原文 · 313 个知识单元 · 盲测通过率 96.9%**（945/975，含诱饵题）

## 目录结构

```
COMKB/
├── README.md            本文件
├── site/                门户静态站点（446 个文件，可直接托管）
│   ├── index.html       首页：搜索、知识版图、板块入口
│   ├── cloud/           云通信板块（Rainbow，3 门）
│   ├── communications/  通信产品线板块（22 门）
│   ├── paths.html       学习路径（6 条路径 × 分段推进图）
│   ├── about.html       关于门户
│   ├── courses/<code>/  每门课的子站（首页/概览/术语/摘要/能力卡）
│   ├── assets/          样式、脚本、图片
│   └── search/          全站搜索索引（413 条）
├── books/               25 本书的工作区（蒸馏过程全记录）
│   └── <课程代码>/
│       ├── BOOK_OVERVIEW.md     整书理解
│       ├── DIGEST.md            全书摘要
│       ├── candidates/          候选提取（案例/反例/原则/框架/术语）
│       ├── verified.md          验证单元
│       ├── blind-verdict.md     盲测验收
│       ├── POLISH-NOTES.md      中文化润色逐处记录
│       └── .cangjie/
│           ├── capabilities/    能力卡事实源（verified.yaml + cards/*.md）
│           └── dist/            编译产物（SKILL.md 入口 + references/）
└── pipeline/            构建-发布-校验-部署脚本
    ├── build_comm_portal.py    门户构建（rmtree 重建）
    ├── publish_all.py          25 本书子站发布
    ├── verify_comm_portal.py   发布校验（断链/索引/一致性）
    ├── deploy_comm_portal.py   部署（凭据走环境变量）
    ├── install_all_skills.py   能力库批量安装
    └── scan_dense.py / scan_blank.py / audit_scan_all.py   排版扫描
```

## 课程清单（10 组 · 25 门）

| 产品线 | 门数 | 课程 |
|---|---|---|
| Rainbow 云通信 | 3 | OXO Connect 集成、Rainbow for OmniPCX Enterprise、Rainbow Hub |
| OmniPCX Enterprise | 6 | Starter、Advanced、系统装载、SIP、加密解决方案、DECT 解决方案 |
| OXO Connect | 3 | 呼叫中心、Starter、Advanced |
| OpenTouch | 3 | Starter、Advanced、移动与远程办公 |
| OmniTouch Contact Center Standard | 3 | Starter、Advanced、Advanced Call Routing |
| OmniVista 8770 NMS | 3 | 安装与网络管理、计费与性能管理、目录管理 |
| OpenTouch Fax Center | 1 | Starter |
| OpenTouch Message Center | 1 | Starter |
| Visual Automated Attendant | 1 | 安装、配置与维护 |
| 待归类 | 1 | OmniSwitch LAN Access Switching（与网络门户同源，归类待确认） |

## 方法论：一本书 → 一个能力库

1. **整书理解**：通读原文，产出 BOOK_OVERVIEW 与 DIGEST
2. **候选提取**：按案例 / 反例 / 原则 / 框架 / 术语五类提取候选单元（每本约 200 条）
3. **验证写卡**：验证单元写成 RIA-TV 六段能力卡——R 原文依据（带页码）、I 自述、A1 书中案例、A2 未来触发、E 可执行步骤（输入/输出契约 + 判停点）、B 边界；三重验证后按晋级预算（每本 8 张）定级
4. **触发盲测**：每本 36-41 题去敏感化测试（含诱饵题），25 本合计 945/975 通过
5. **编译发布**：verified.yaml 为唯一事实源，确定性编译为 single 入口产物，原子发布 + 发布门校验
6. **门户编排**：课程子站 + 首页搜索 + 知识版图 + 学习路径；全量排版扫描（箭头链/超长行/缺空行）与中文化润色（见各书 POLISH-NOTES.md）

## 复现构建与部署

依赖：Python 3.10+，`pip install markdown pyyaml paramiko`

```bash
# 1) 重建门户静态站点
python pipeline/build_comm_portal.py

# 2) 发布 25 个课程子站
python pipeline/publish_all.py

# 3) 校验（断链 / 索引 / 发布一致性）
python pipeline/verify_comm_portal.py

# 4) 部署到目标机（nginx:alpine, 端口 8900）
set COMKB_DEPLOY_HOST=10.20.30.103
set COMKB_DEPLOY_USER=<ssh 用户>
set COMKB_DEPLOY_PWD=<ssh 密码>
python pipeline/deploy_comm_portal.py
```

> 注：脚本中的 `BOOKS`、`SITE` 等路径常量按本仓库工作区写死，换环境时需对应调整。

## 版权说明

本仓库内容整理自 Alcatel-Lucent Enterprise 官方售后培训教材（Postsales Training），相关教材版权归 ALE 所有。整理产出（能力卡、门户、图表）仅供学习与内部培训参考，请勿用于商业用途。
