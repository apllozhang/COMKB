# -*- coding: utf-8 -*-
"""构建 ALE Communications 技术培训门户（模板与 networking/8899 同构：topbar + course-layout + course-intro + skill-groups）。"""
import glob
import io
import json
import os
import shutil
import sys
from datetime import datetime

import yaml

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"F:\AIwork\ZCode\ale_comm_site"
SITE = os.path.join(ROOT, "site")
ASSETS_SRC = r"F:\AIwork\ZCode\.cangjie\comm_portal_assets"
BOOKS = r"F:\AIwork\ZCode\books"
NOW = datetime.now().strftime("%Y-%m-%d")

CSS_REFS = (
    '<link rel="stylesheet" href="/assets/css/tokens.css?v=4">\n'
    '  <link rel="stylesheet" href="/assets/css/layout.css?v=4">\n'
    '  <link rel="stylesheet" href="/assets/css/components.css?v=4">\n'
    '  <link rel="stylesheet" href="/assets/css/content.css?v=7">\n'
    '  <link rel="stylesheet" href="/assets/css/portal.css?v=11">'
)

# ---------- 课程数据（标题/版本自 PDF 首页提取整理） ----------
COURSES = [
    dict(code="rainxte001en", pdf="RAINXTE001EN.pdf", group="rainbow", title="Rainbow OXO Connect 集成",
         version="R6.3 / SP149", edition="Edition 13", pages=251, note="", distill_status="done"),
    dict(code="rainxte003en", pdf="RAINXTE003EN.pdf", group="rainbow", title="Rainbow for OmniPCX Enterprise",
         version="R101.1 N4 MD4 / SP161", edition="Edition 12", pages=314, note="", distill_status="done"),
    dict(code="rainxte101en", pdf="RAINXTE101EN.pdf", group="rainbow", title="Rainbow Hub",
         version="Sprint 170", edition="Edition 16", pages=351, note="", distill_status="done"),
    dict(code="dectxte200en", pdf="DECTXTE200EN.pdf", group="omnipcx", title="OmniPCX Enterprise · DECT 解决方案",
         version="R101.1 MD4", edition="Edition 12", pages=298, note="", distill_status="done"),
    dict(code="entpxte400en", pdf="ENTPXTE400EN.pdf", group="omnipcx", title="OmniPCX Enterprise · Starter",
         version="R101.1 MD4", edition="Edition 12", pages=821, note="", distill_status="done"),
    dict(code="entpxte401en", pdf="ENTPXTE401EN.pdf", group="omnipcx", title="OmniPCX Enterprise · Advanced",
         version="R101.1 MD4", edition="Edition 13", pages=543, note="", distill_status="done"),
    dict(code="entpxte402en", pdf="ENTPXTE402EN.pdf", group="omnipcx", title="OmniPCX Enterprise · 系统装载",
         version="R101.1 MD4", edition="Edition 12", pages=415, note="", distill_status="done"),
    dict(code="entpxte403en", pdf="ENTPXTE403EN.pdf", group="omnipcx", title="OmniPCX Enterprise · SIP",
         version="R101.1 MD4", edition="Edition 12", pages=465, note="", distill_status="done"),
    dict(code="entpxte421en", pdf="ENTPXTE421EN.pdf", group="omnipcx", title="OmniPCX Enterprise · 加密解决方案",
         version="R101.2", edition="Edition 05", pages=410, note="", distill_status="done"),
    dict(code="oxocxte107en", pdf="OXOCXTE107EN.pdf", group="oxo", title="OXO Connect · 呼叫中心",
         version="—", edition="Edition 07", pages=218, note="", distill_status="done"),
    dict(code="oxocxte300en", pdf="OXOCXTE300EN.pdf", group="oxo", title="OXO Connect · Starter",
         version="R6.3", edition="Edition 16", pages=472, note="", distill_status="done"),
    dict(code="oxocxte301en", pdf="OXOCXTE301EN.pdf", group="oxo", title="OXO Connect · Advanced",
         version="R6.3", edition="Edition 18", pages=601, note="", distill_status="done"),
    dict(code="openxte225en", pdf="OPENXTE225EN.pdf", group="opentouch", title="OpenTouch · 移动与远程办公",
         version="R2.6", edition="Issue 10", pages=287, note="", distill_status="done"),
    dict(code="openxte300en", pdf="OPENXTE300EN.pdf", group="opentouch", title="OpenTouch · Starter",
         version="R2.6.1", edition="Edition 10", pages=603, note="", distill_status="done"),
    dict(code="openxte301en", pdf="OPENXTE301EN.pdf", group="opentouch", title="OpenTouch · Advanced",
         version="R2.6.1", edition="Edition 08", pages=468, note="", distill_status="done"),
    dict(code="otfcxte200en", pdf="OTFCXTE200EN.pdf", group="otfax", title="OpenTouch Fax Center · Starter",
         version="R9.2", edition="Edition 04", pages=233, note="", distill_status="done"),
    dict(code="otmcxte200en", pdf="OTMCXTE200EN.pdf", group="otmsg", title="OpenTouch Message Center · Starter",
         version="R2.6", edition="Issue 08", pages=259, note="", distill_status="done"),
    dict(code="otccxte100en", pdf="OTCCXTE100EN.pdf", group="otcc", title="OmniTouch Contact Center Standard · Starter",
         version="R10.16", edition="Edition 09", pages=649, note="", distill_status="done"),
    dict(code="otccxte101en", pdf="OTCCXTE101EN.pdf", group="otcc", title="OmniTouch Contact Center Standard · Advanced",
         version="R10.15", edition="Edition 07", pages=597, note="", distill_status="done"),
    dict(code="otccxte150en", pdf="OTCCXTE150EN.pdf", group="otcc", title="OmniTouch Contact Center Standard · Advanced Call Routing",
         version="Standard Edition", edition="Issue 01", pages=470, note="", distill_status="done"),
    dict(code="8770xte200en", pdf="8770XTE200EN.pdf", group="ov8770", title="OmniVista 8770 · 安装与网络管理",
         version="R5.2", edition="Edition 47", pages=705, note="", distill_status="done"),
    dict(code="8770xte201en", pdf="8770XTE201EN.pdf", group="ov8770", title="OmniVista 8770 · 计费与性能管理",
         version="R5.2", edition="Edition 45", pages=650, note="", distill_status="done"),
    dict(code="8770xte202en", pdf="8770XTE202EN.pdf", group="ov8770", title="OmniVista 8770 · 目录管理",
         version="R5.2", edition="Edition 40", pages=565, note="", distill_status="done"),
    dict(code="vsaaxte001en", pdf="VSAAXTE001EN.pdf", group="vaa", title="Visual Automated Attendant · 安装、配置与维护",
         version="R4.8.006", edition="Edition 20", pages=351, note="", distill_status="done"),
    dict(code="dt00xte215en", pdf="DT00XTE215EN.pdf", group="tbd", title="OmniSwitch LAN Access Switching",
         version="R8", edition="Edition 23", pages=587,
         note="素材目录标注为「Postsales on ALE Connect」，PDF 实际内容为 OmniSwitch LAN Access Switching R8（与网络门户 DT00XTE215 同源）。归类待与素材提供方确认。", distill_status="done"),
]

GROUPS = [
    ("rainbow", "Rainbow 云通信", "Cloud 板块 · Rainbow 协作与云通信平台", "cloud"),
    ("omnipcx", "OmniPCX Enterprise", "中大型企业通信服务器（PBX）旗舰产品线", "comm"),
    ("oxo", "OXO Connect", "中小企业通信服务器", "comm"),
    ("opentouch", "OpenTouch", "OpenTouch 统一通信平台", "comm"),
    ("otfax", "OpenTouch Fax Center", "传真中心", "comm"),
    ("otmsg", "OpenTouch Message Center", "留言中心", "comm"),
    ("otcc", "OmniTouch Contact Center Standard", "标准版呼叫中心", "comm"),
    ("ov8770", "OmniVista 8770 NMS", "通信网络管理系统", "comm"),
    ("vaa", "Visual Automated Attendant", "可视化自动话务员", "comm"),
    ("tbd", "待归类", "素材目录与内容待核对", "comm"),
]

TOTAL_PAGES = sum(c["pages"] for c in COURSES)


def ws_dir(code):
    """课程 code → 工作区目录（第一本用语义 slug）。"""
    return os.path.join(BOOKS, "oxo-connect-call-center" if code == "oxocxte107en" else code)


def caps_for(code):
    d = os.path.join(ws_dir(code), ".cangjie", "capabilities", "cards")
    if not os.path.isdir(d):
        return 0
    return len([f for f in os.listdir(d) if f.endswith(".md")])


TOTAL_CAPS = sum(caps_for(c["code"]) for c in COURSES)


def caps_map():
    return {c["code"]: caps_for(c["code"]) for c in COURSES}

# 学习路径：Communications 为纯售后教材库，按"产品方向 × 成长阶段"编排 6 条路径，26 步覆盖 25 门课
PATHS = [
    dict(key="oxo-smb", tag="3 STEPS", title="OXO Connect 中小企业交付",
         sub="中小企业话务系统的装机、进阶组网到呼叫中心落地",
         steps=[
             ("oxocxte300en", "OXO Connect 本体交付入门", "FTR/OMC 双路线、编号与组、用户话机、SIP 中继与备份"),
             ("oxocxte301en", "进阶组网与垂直方案", "公网私网 SIP 组网、ARS 三件套、酒店与计费、DECT 与安全加固"),
             ("oxocxte107en", "呼叫中心（ACD）落地", "队列/坐席/班长/统计的 ACD 全流程与六场景排障"),
         ]),
    dict(key="oxe-ent", tag="5 STEPS", title="OmniPCX Enterprise 企业交付",
         sub="中大型 PBX 从准入闭环到高级组网与加密的完整纵深",
         steps=[
             ("entpxte400en", "Starter 准入闭环", "首登加固、许可激活、机架上架、用户编号、SIP 中继"),
             ("entpxte402en", "系统装载与云管", "SOT 装机、补丁定律、Cloud Connect 与 OPEX 许可池"),
             ("entpxte401en", "Advanced 高可用纵深", "CS 冗余、IP 域与 PCS、公私网溢出、Direct IP Link"),
             ("entpxte403en", "SIP 组网与终端延伸", "SEPLOS/SIP 设备开通、OTSBC 运营商对接、远程办公"),
             ("entpxte421en", "加密解决方案", "证书信任链、DTLS/SIP TLS、EEGW 大容量、ABC-F 网络加密"),
         ]),
    dict(key="cc", tag="4 STEPS", title="呼叫中心专精",
         sub="OmniTouch Contact Center Standard 从入门矩阵到高级路由与话务台",
         steps=[
             ("otccxte100en", "Starter 入门闭环", "pilot→队列→处理组矩阵、双控制台、EWT 与统计入门"),
             ("otccxte101en", "Advanced 高级能力", "ISM 技能匹配、ABC-F 互助、墙板、CCTA 与报表定制"),
             ("otccxte150en", "高级呼叫路由（ACR）", "CCD 矩阵、ASM 脚本、内外部数据库查询与多语言"),
             ("vsaaxte001en", "VAA 话务台与 IVR", "Visual Automated Attendant 安装、多租户树与高可用"),
         ]),
    dict(key="ot-uc", tag="5 STEPS", title="OpenTouch 协作与统一通信",
         sub="OpenTouch 平台从三件套上电到移动办公与增值外设",
         steps=[
             ("openxte300en", "Starter 平台上电", "OTMS 三件套装机、许可、节点声明与客户端交付"),
             ("openxte301en", "Advanced 移动与安全", "Nomadic、智能手机、UM/日历、LDAP/RADIUS 认证"),
             ("openxte225en", "移动与远程办公", "DMZ 双通道、OTSBC/SRTP、OTC PC 与手机双模式"),
             ("otmcxte200en", "留言中心（OTMC）", "语音邮箱装机、SIP 开通、通知与 IMAP 访问"),
             ("otfcxte200en", "传真中心（OTFC）", "FoIP 传真服务器、SIP 话路与 Exchange 通道"),
         ]),
    dict(key="nms", tag="3 STEPS", title="网管与运营分析",
         sub="OmniVista 8770 从平台安装到计费、性能与目录数据治理",
         steps=[
             ("8770xte200en", "安装与网络管理", "平台装机、节点接入、用户开通、告警与备份"),
             ("8770xte201en", "计费与性能管理", "话务出票、资费成本、报表与 VoIP 质量监控"),
             ("8770xte202en", "目录管理", "OXE 同步、MSAD/Azure 管道、Click to Call 与复制"),
         ]),
    dict(key="cloud-wireless", tag="5 STEPS", title="云化与无线扩展",
         sub="从 Rainbow 混合云到纯云 Hub，再补齐 DECT 移动与接入交换",
         steps=[
             ("rainxte001en", "Rainbow × OXO Connect 集成", "公司订阅、PBX 接入、WebRTC 网关与 Teams 共存"),
             ("rainxte003en", "Rainbow × OmniPCX 集成", "OXE 接入、REX 路由、共享网关池与 Teams 共存"),
             ("rainxte101en", "Rainbow Hub 纯云", "Cloud PBX 开户、zero-touch 终端、群组与 IVR"),
             ("dectxte200en", "DECT 无绳移动", "PARI 体系、IP-xBS 部署、空中同步与手机管理"),
             ("dt00xte215en", "OmniSwitch 接入交换", "AAA 加固、VLAN/VC 组网、QoS/ACL 策略与运维"),
         ]),
]


def w(rel, text):
    fp = os.path.join(SITE, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def topbar(active):
    nav = [
        ("/index.html", "首页", active == "home"),
        ("/paths.html", "学习路径", active == "paths"),
        ("/cloud/index.html", "云通信", active == "cloud"),
        ("/communications/index.html", "通信产品线", active == "comm"),
        ("/about.html", "关于门户", active == "about"),
        ("http://10.20.30.103:8899/", "网络门户 ↗", False),
    ]
    links = "".join(
        '<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if cur else "", t) for h, t, cur in nav
    )
    return (
        '<header class="topbar" data-topbar>'
        '<a class="brand" href="/index.html" aria-label="返回门户首页">'
        '<img src="/assets/img/ale-logo-color.png" alt="Alcatel-Lucent Enterprise"><span>ALE 培训门户 · Communications</span></a>'
        '<nav id="primary-nav" class="primary-nav" aria-label="主导航">%s</nav>'
        '</header>' % links
    )


def head(title, desc):
    return (
        '<!doctype html>\n<html lang="zh-CN">\n<head>\n  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '  <meta name="description" content="%s">\n  <meta name="theme-color" content="#6B489D">\n'
        '  <title>%s</title>\n  <link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">\n  %s\n</head>'
        % (desc, title, CSS_REFS)
    )


def footer_note():
    return ('<footer class="content-footer">仅供内部学习使用 · 教材版权归 ALE Training Services 所有 · '
            '姊妹站：<a href="http://10.20.30.103:8899/">ALE Networking 技术培训门户</a></footer>')


def status_badge(c):
    return ('<span class="status status-done">已入库</span>'
            if c.get("distill_status") == "done"
            else '<span class="status status-pending">待入库</span>')


def course_card(c, base=""):
    href = "/courses/%s/index.html" % c["code"]
    return (
        '<article class="course-card"><div class="card-topline"><span>%s</span>%s</div>'
        '<h3><a href="%s">%s</a></h3>'
        '<p>%s · %s · %d 页</p>'
        '<div class="chips"><span>%s</span><span>%d 页</span></div></article>'
        % (c["pdf"].replace(".pdf", "").upper(), status_badge(c), href, c["title"],
           c["version"], c["edition"], c["pages"], c["edition"], c["pages"])
    )


def group_section(key, base=""):
    g = [x for x in GROUPS if x[0] == key][0]
    cards = "".join(course_card(c, base) for c in COURSES if c["group"] == key)
    return (
        '<section class="catalog-group" id="%s"><div class="catalog-heading">'
        '<h2>%s</h2><p>%s · %d 门</p></div>'
        '<div class="course-grid">%s</div></section>' % (key, g[1], g[2], sum(1 for c in COURSES if c["group"] == key), cards)
    )


def km_rows():
    """知识版图数据：按产品线的知识单元数 + 按课程的页数（倒序）。"""
    cm = caps_map()
    group_rows = []
    for key, name, _desc, _loc in GROUPS:
        codes = [c["code"] for c in COURSES if c["group"] == key]
        caps = sum(cm[c] for c in codes)
        group_rows.append((name, len(codes), caps))
    course_rows = sorted(((c["title"], c["pages"], cm[c["code"]]) for c in COURSES),
                         key=lambda x: -x[1])
    return group_rows, course_rows


def km_bars():
    group_rows, course_rows = km_rows()
    g_max = max([r[2] for r in group_rows] + [1])
    g_bars = "".join(
        '<div class="km-row"><span class="km-label">%s <i>%d 门</i></span>'
        '<span class="km-track"><span class="km-bar" style="width:%.0f%%"></span></span>'
        '<span class="km-val">%d</span></div>'
        % (name, n, round(caps * 100.0 / g_max), caps)
        for name, n, caps in group_rows)
    c_max = max([r[1] for r in course_rows])
    c_bars = "".join(
        '<div class="km-row"><span class="km-label" title="%s">%s</span>'
        '<span class="km-track"><span class="km-bar km-bar--alt" style="width:%.0f%%"></span></span>'
        '<span class="km-val">%d 页</span></div>'
        % (title, title, round(pages * 100.0 / c_max), pages)
        for title, pages, _caps in course_rows)
    return ('<div class="km-card"><h3>按产品线 · 知识单元分布</h3>%s</div>' % g_bars,
            '<div class="km-card km-card--scroll"><h3>按课程 · 原文页数</h3>%s</div>' % c_bars)


def build_index():
    n_done = sum(1 for c in COURSES if c.get("distill_status") == "done")
    groups_html = "".join(group_section(k) for k, *_ in GROUPS)
    g_card, c_card = km_bars()
    body = f"""
  <section class="hero-comm">
    <div class="hero-inner">
      <p class="eyebrow">ALE COMMUNICATIONS TRAINING</p>
      <h1>ALE Communications 技术培训门户</h1>
      <p class="hero-sub">面向售后与交付工程师的官方教材知识库，覆盖 Rainbow 云通信与语音通信两大方向；<br>课程内容经文档整理流程逐门入库，当前已完成 <b>{n_done}</b> 门。</p>
      <div class="hero-search" data-search>
        <input type="search" data-search-input placeholder="搜索课程编号、产品型号或技术关键词…"
               aria-label="站内搜索" autocomplete="off">
        <div class="search-results" data-search-results role="listbox" aria-live="polite"></div>
      </div>
      <div class="hero-actions">
        <a class="btn btn-solid" href="#catalog">开始学习</a>
        <a class="btn btn-ghost" href="#knowledge-map">查找资料</a>
      </div>
      <div class="stat-row">
        <div class="stat"><b>{len(COURSES)}</b><span>门官方课程</span></div>
        <div class="stat"><b>{TOTAL_CAPS}</b><span>个知识单元</span></div>
        <div class="stat"><b>{len(GROUPS)}</b><span>条产品线</span></div>
        <div class="stat"><b>{TOTAL_PAGES:,}</b><span>页原文教材</span></div>
        <div class="stat"><b>{n_done} / {len(COURSES)}</b><span>已完成入库</span></div>
      </div>
    </div>
  </section>
  <section class="board-grid">
    <a class="board-card" href="/cloud/index.html">
      <img src="/assets/img/hero-rainbow.jpg" alt="Rainbow 云通信">
      <div><p class="eyebrow">CLOUD</p><h2>云通信板块</h2><p>Rainbow 平台 3 门课程 · 与 OXO / OmniPCX 的云端集成</p></div>
    </a>
    <a class="board-card" href="/communications/index.html">
      <img src="/assets/img/board-deskphones.jpg" alt="语音通信产品线">
      <div><p class="eyebrow">COMMUNICATIONS</p><h2>通信产品线板块</h2><p>OmniPCX Enterprise / OXO Connect / OpenTouch / Contact Center 等 22 门课程</p></div>
    </a>
  </section>
  <div class="page-shell home-shell">
    <section class="km-section" id="knowledge-map">
      <div class="section-heading"><div><p class="eyebrow">KNOWLEDGE MAP</p><h2>知识版图</h2></div>
        <p>先看整体分布，再进目录查详情。</p></div>
      <div class="km-grid">
        {g_card}
        {c_card}
      </div>
    </section>
    <div class="section-heading"><div><p class="eyebrow">CATALOG</p><h2>课程总目</h2></div><p>按产品线分组；点击卡片进入课程页。</p></div>
    {groups_html}
  </div>
"""
    html = (head("ALE Communications 技术培训门户", "ALE 通信产品线售后培训知识库")
            + '\n<body data-page-kind="home">\n  ' + topbar("home")
            + '\n  <main id="main-content" class="home-main">' + body + '\n  </main>\n'
            + '  <script src="/assets/js/comm-search.js" defer></script>\n</body>\n</html>\n')
    w("index.html", html)


def build_board(key, fname, title, desc, active, banner):
    if key == "rainbow":
        sections = group_section("rainbow")
    else:
        sections = "".join(group_section(k) for k, _, _, loc in GROUPS if loc == "comm")
    intro = ('<header class="course-intro course-intro--img">'
             '<img src="/assets/img/%s" alt="" role="presentation"><div class="ci-shade"></div>'
             '<div class="ci-text"><p class="eyebrow">TRAINING BOARD</p><h1>%s</h1><p>%s</p></div></header>'
             % (banner, title, desc))
    content = ('<div class="page-shell">%s</div>%s' % (sections, footer_note()))
    html = (head(title, "ALE Communications 技术培训门户")
            + '\n<body data-page-kind="board">\n  ' + topbar(active)
            + '\n  <main id="main-content" class="board-main">'
            + '\n    <nav class="breadcrumbs" aria-label="面包屑"><a href="/index.html">首页</a><span>/</span><span aria-current="page">%s</span></nav>' % title
            + '\n    ' + intro + '\n    ' + content
            + '\n  </main>\n</body>\n</html>\n')
    w(fname, html)


def build_about():
    rows = "".join(
        "<tr><td>%s</td><td>%d 门</td><td>%s</td></tr>" % (
            g[1], sum(1 for c in COURSES if c["group"] == g[0]),
            "、".join(c["pdf"].replace(".pdf", "").upper() for c in COURSES if c["group"] == g[0]))
        for g in GROUPS
    )
    intro = ('<header class="course-intro course-intro--img">'
             '<img src="/assets/img/banner-about.jpg" alt="" role="presentation"><div class="ci-shade"></div>'
             '<div class="ci-text"><p class="eyebrow">ABOUT</p><h1>关于本门户</h1>'
             '<p>ALE Communications 技术培训门户收录 ALE 通信产品线的售后（Postsales）培训教材，<br>'
             '与网络产品线门户（OmniSwitch / Stellar / OmniVista）互为姊妹站。</p></div></header>')
    content = ("""
    <div class="page-shell"><article class="markdown-body">
      <h2>定位</h2>
      <p>{n} 门课程（共 {pages:,} 页原文）已<b>全部完成入库</b>：内容经文档整理流程（整书理解 → 要点提取 → 校对 → 上架）统一处理，与网络门户同一标准。首门示范课：<a href="/courses/oxocxte107en/index.html">OXO Connect · 呼叫中心</a>（15 个能力单元）。</p>
      <h2>素材来源</h2>
      <p>原文教材：Training Offer by Job Function / CBD（{n} 份 PDF）；视觉素材：ALE 市场部 Digital Library。</p>
      <h2>课程清单</h2>
      <div class="table-scroll"><table><thead><tr><th>产品线</th><th>门数</th><th>课程代码</th></tr></thead><tbody>{rows}</tbody></table></div>
      <h2>版权</h2>
      <p>原文教材版权归 ALE Training Services 所有；门户内容仅供内部学习使用，请勿外传或用于商业用途。</p>
    </article></div>""").format(n=len(COURSES), pages=TOTAL_PAGES, rows=rows)
    html = (head("关于门户", "ALE Communications 技术培训门户")
            + '\n<body data-page-kind="about">\n  ' + topbar("about")
            + '\n  <main id="main-content" class="board-main">'
            + '\n    <nav class="breadcrumbs" aria-label="面包屑"><a href="/index.html">首页</a><span>/</span><span aria-current="page">关于门户</span></nav>'
            + '\n    ' + intro + '\n    ' + content
            + '\n  </main>\n</body>\n</html>\n')
    w("about.html", html)


def sidebar_for(c):
    done = c.get("distill_status") == "done"
    meta = (
        '<div class="sidebar-heading"><p class="eyebrow">COURSE</p><h2>%s</h2>'
        '<p>%s · %s · %d 页</p></div>' % (c["title"], c["version"], c["edition"], c["pages"])
    )
    items = [("课程首页", True, "index.html")]
    if done:
        items += [
            ("精华长文 DIGEST", False, "digest.html"),
            ("教书理解", False, "overview.html"),
            ("术语词典", False, "glossary.html"),
        ]
    links = "".join('<a%s href="courses/%s/%s">%s</a>' % (
        ' aria-current="page"' if cur else "", c["code"], rel, t
    ) for t, cur, rel in items)
    if not done:
        links += '<p class="course-nav-group">待入库</p><span class="course-nav-todo">文档整理后解锁全文</span>'
    return ('<aside class="course-sidebar">' + meta
            + '<nav class="course-nav" aria-label="课程目录">' + links + '</nav></aside>')


def build_course(c):
    done = c.get("distill_status") == "done"
    code_up = c["pdf"].replace(".pdf", "").upper()
    steps = [
        ("素材建档（本页）", True),
        ("文档整书理解与骨架梳理", done),
        ("方法论提取 + 三重验证", done),
        ("知识单元 / 可执行技能上架", done),
        ("整理摘要 + 术语表", done),
    ]
    pipeline = "".join('<li class="%s">%s</li>' % ("done" if ok else "todo", t) for t, ok in steps)
    if done:
        body_main = (
            '<p>本课程已完成 <b>文档整理</b> 整理并编译上架：<b>1 个可执行技能（15 个能力单元）</b>，'
            '配套整理摘要（DIGEST）与全书术语表。左侧目录进入各能力页；技能本体已安装至内部技能库，供 AI 会话直接调用。</p>'
            '<section class="reading-links"><h2>课程全景资料</h2>'
            '<a href="digest.html">精华长文 DIGEST</a>'
            '<a href="overview.html">教书理解 BOOK_OVERVIEW</a>'
            '<a href="glossary.html">术语词典</a></section>'
        )
    else:
        body_main = (
            '<p>本课程已纳入门户建档，原文 %d 页。当前为<b>框架占位页</b>：'
            '内容尚未完成文档整理入库，文档整理后此处将呈现能力单元、整理摘要与术语词典。</p>' % c["pages"]
        )
    note = ('<div class="note-card"><b>归类说明</b>：%s</div>' % c["note"]) if c["note"] else ""
    html = (head("%s · %s" % (c["title"], code_up), "ALE Communications 课程页")
            + '\n<body data-page-kind="course">\n  ' + topbar("")
            + '\n<div class="course-layout">\n'
            + sidebar_for(c)
            + '\n  <main id="main-content" class="course-main prose">\n'
            + '    <nav class="breadcrumbs" aria-label="面包屑"><a href="/index.html">首页</a><span>/</span>'
              '<a href="/communications/index.html">通信产品线</a><span>/</span>'
              '<span aria-current="page">%s</span></nav>\n' % code_up
            + ('    <header class="course-intro"><p class="eyebrow">%s</p><h1>%s</h1>'
               '<p>%s · %s · %d 页</p><div class="chips"><span>%s</span><span>%d 页</span><span>%s</span></div></header>\n')
            % (code_up, c["title"], c["version"], c["edition"], c["pages"], c["edition"], c["pages"], ("已入库" if done else "待入库"))
            + '    <section class="route"><h2>文档整理流程</h2><ol class="pipeline">' + pipeline + '</ol></section>\n'
            + ('    <article class="markdown-body">%s\n    <h2>原文信息</h2>'
               '<div class="table-scroll"><table><thead><tr><th>项目</th><th>内容</th></tr></thead><tbody>'
               '<tr><td>文件名</td><td>%s</td></tr>'
               '<tr><td>素材目录</td><td>Training Offer by Job Function / CBD</td></tr>'
               '<tr><td>原文页数</td><td>%d 页</td></tr>'
               '</tbody></table></div></article>\n') % (body_main + note, c["pdf"], c["pages"])
            + '    ' + footer_note() + '\n  </main>\n</div>\n</body>\n</html>\n')
    w("courses/%s/index.html" % c["code"], html)


def title_of(code):
    return [c["title"] for c in COURSES if c["code"] == code][0]


PATH_COVERS = {
    "oxo-smb": "path-oxo.jpg",
    "oxe-ent": "path-oxe.jpg",
    "cc": "path-cc.jpg",
    "ot-uc": "path-ot.jpg",
    "nms": "path-nms.jpg",
    "cloud-wireless": "path-cloud.jpg",
}


def build_paths():
    rows = "".join(
        '<div class="pp-row"><span class="pp-label">%s</span><span class="pp-track">%s</span></div>'
        % (p["title"], "".join(
            '<a class="pp-seg pp-seg--%d" style="flex:%d" href="/courses/%s/index.html" title="%s">%s</a>'
            % (i + 1, 3 if len(p["steps"]) < 5 else 2, s[0], s[1], i + 1)
            for i, s in enumerate(p["steps"])))
        for p in PATHS)
    cards = "".join(
        '<section class="learning-path"><div class="path-cover">'
        '<img src="/assets/img/%s" alt="" role="presentation"><div class="path-shade"></div>'
        '<header><p>%s</p><h2>%s</h2><span>%s</span></header></div>'
        '<ol>%s</ol></section>'
        % (PATH_COVERS.get(p["key"], "path-oxo.jpg"), p["tag"], p["title"], p["sub"],
           "".join('<li><a href="/courses/%s/index.html">%s</a><p>%s</p></li>' % (s[0], s[1], s[2])
                   for s in p["steps"]))
        for p in PATHS)
    html = (head("学习路径 — ALE Communications 技术培训门户",
                 "按产品方向与成长阶段编排的售后学习路径")
            + '\n<body data-page-kind="paths">\n  ' + topbar("paths")
            + '\n  <main id="main-content" class="paths-main">'
            + '\n    <header class="course-intro course-intro--img">'
            + '<img src="/assets/img/banner-paths.jpg" alt="" role="presentation"><div class="ci-shade"></div>'
            + '<div class="ci-text"><p class="eyebrow">LEARNING PATHS</p><h1>学习路径</h1>'
            + '<p>Communications 教材库面向售后与交付工程师：按产品方向编成 6 条路径，<br>每条路径分段推进，从入门走到可独立交付。</p></div></header>'
            + '\n    <section id="path-progress"><div class="section-heading"><div><p class="eyebrow">PROGRESS MAP</p>'
            + '<h2>路径推进图</h2></div><p>每段为一步，颜色由浅入深表示建议顺序；点击色块直达对应课程。</p></div>'
            + '\n    <div class="pp-chart">' + rows + '</div></section>'
            + '\n    <div class="learning-paths">' + cards + '</div>'
            + '\n    ' + footer_note()
            + '\n  </main>\n</body>\n</html>\n')
    w("paths.html", html)


def build_search_index():
    entries = []
    for c in COURSES:
        base = "courses/%s" % c["code"]
        vpath = os.path.join(ws_dir(c["code"]), ".cangjie", "capabilities", "verified.yaml")
        caps = []
        if os.path.isfile(vpath):
            try:
                bundle = yaml.safe_load(io.open(vpath, encoding="utf-8").read())
                for cap in bundle.get("capabilities", []):
                    caps.append((cap.get("slug"), cap.get("title"),
                                 " ".join(cap.get("keywords", []) or []),
                                 " ".join(cap.get("intents", []) or [])))
            except Exception as exc:
                print("[search] %s yaml error: %s" % (c["code"], exc))
        entries.append(dict(t=c["title"], s=c["group"], u=base + "/index.html",
                            k="%s %s" % (c["code"], c["pdf"])))
        for page, label in (("digest.html", "精华长文"), ("overview.html", "整书理解"),
                            ("glossary.html", "术语词典")):
            entries.append(dict(t="%s %s" % (c["title"], label), s=c["group"],
                                u="%s/%s" % (base, page), k=label))
        for slug, title, kw, intents in caps:
            entries.append(dict(t=title or slug, s=c["title"],
                                u="%s/skills/%s.html" % (base, slug),
                                k="%s %s %s" % (slug, kw, intents)))
    w("search" + os.sep + "index.json",
      json.dumps(entries, ensure_ascii=False, indent=0))
    print("search index entries:", len(entries))


PORTAL_CSS = """
/* ALE Communications 门户补充样式（骨架样式由 tokens/layout/components/content 提供） */
.status-pending { color: #8a6d1a; background: #fdf3d7; border: 1px solid #e8d48a; }
.status-done { color: #1e6b3a; background: #e2f5e9; border: 1px solid #9fd6b4; }
.pipeline .todo { color: var(--ink-500); }
.pipeline { padding-left: 1.4rem; }
.pipeline li { margin: .3rem 0; }
.pipeline .done { color: var(--ale-purple-700); font-weight: 600; }
.note-card { margin: 1rem 0; padding: .8rem 1rem; background: #fdf3d7; border-left: 4px solid #e8d48a; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; }
/* 首页 hero 与板块卡 */
.hero-comm { background: linear-gradient(90deg, rgba(28,16,48,.97) 0%, rgba(28,16,48,.90) 36%, rgba(46,26,80,.42) 64%, rgba(46,26,80,.06) 100%), url('/assets/img/hero-deskphones.jpg') center right / cover no-repeat; color: #fff; padding: 6rem 1rem 5rem; }
.hero-inner { max-width: 1080px; margin: 0 auto; }
.hero-inner h1 { margin: .4rem 0 .8rem; font-size: 2.4rem; }
.hero-sub { max-width: 44rem; color: #ece7f5; font-size: 1.04rem; line-height: 1.85; }
.hero-sub b { color: #ffd98a; }
.stat-row { display: flex; gap: 1.8rem; margin-top: 1.8rem; flex-wrap: wrap; }
.stat { min-width: 7.5rem; }
.stat b { display: block; font-size: 2rem; color: #fff; }
.stat span { color: #cfc4e4; font-size: .82rem; }
.board-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; max-width: 1080px; margin: -1.6rem auto 0; padding: 0 1rem; position: relative; z-index: 2; }
.board-card { display: grid; grid-template-columns: 200px 1fr; gap: 1rem; align-items: center; background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius-md); padding: .9rem; box-shadow: var(--shadow-sm); text-decoration: none; color: inherit; transition: box-shadow .15s, border-color .15s; }
.board-card:hover { border-color: var(--ale-purple-600); box-shadow: var(--shadow-md); }
.board-card img { width: 100%; height: 110px; object-fit: cover; border-radius: var(--radius-sm); }
.board-card h2 { margin: .2rem 0 .3rem; font-size: 1.15rem; color: var(--ale-purple-700); }
.board-card p:last-child { color: var(--ink-500); font-size: .88rem; }
@media (max-width: 860px) { .board-grid { grid-template-columns: 1fr; } .board-card img { height: 96px; } .hero-inner h1 { font-size: 1.7rem; } }
/* 表格：列宽按内容自适应，长串不断表（webui 规范 14A.3） */
.markdown-body .table-scroll table { table-layout: auto; }
.markdown-body .table-scroll th, .markdown-body .table-scroll td { overflow-wrap: break-word; }
/* 首页 hero 搜索框与按钮组 */
.hero-search { position: relative; max-width: 560px; margin-top: 1.6rem; }
.hero-search input[type="search"] { width: 100%; padding: .95rem 1.1rem; font-size: 1rem; color: var(--ink-700, #2a2438); background: #fff; border: 1px solid transparent; border-radius: 12px; box-shadow: 0 6px 24px rgba(10,4,26,.35); outline: none; }
.hero-search input[type="search"]:focus { border-color: var(--ale-purple-600, #6B489D); }
.search-results { display: none; position: absolute; top: calc(100% + 6px); left: 0; right: 0; max-height: 380px; overflow: auto; background: #fff; border-radius: 12px; box-shadow: 0 14px 40px rgba(10,4,26,.35); z-index: 30; }
.search-results.open { display: block; }
.search-result { display: block; padding: .55rem .9rem; text-decoration: none; color: var(--ink-700, #2a2438); border-bottom: 1px solid #f0ecf6; }
.search-result:last-child { border-bottom: none; }
.search-result:hover { background: #f4eff9; }
.search-result b { display: block; font-size: .92rem; }
.search-result small { color: var(--ink-500, #71688a); font-size: .78rem; }
.search-state { display: block; padding: .7rem .9rem; color: var(--ink-500, #71688a); font-size: .85rem; }
.hero-actions { display: flex; gap: .8rem; margin-top: 1.1rem; }
.btn { display: inline-block; padding: .68rem 1.5rem; border-radius: 10px; font-weight: 600; text-decoration: none; font-size: .95rem; }
.btn-solid { background: #fff; color: var(--ale-purple-700, #6B489D); }
.btn-solid:hover { background: #f0e9fa; }
.btn-ghost { color: #fff; border: 1.5px solid rgba(255,255,255,.65); }
.btn-ghost:hover { background: rgba(255,255,255,.12); }
/* 知识版图（纯 CSS 条形图） */
.km-section { margin-top: 2.2rem; }
.km-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; }
.km-card { background: var(--surface, #fff); border: 1px solid var(--line, #e6e1ef); border-radius: var(--radius-md, 12px); padding: 1.1rem 1.2rem; }
.km-card h3 { margin: 0 0 .9rem; font-size: 1rem; color: var(--ale-purple-700, #6B489D); }
.km-card--scroll { max-height: 560px; overflow: auto; }
.km-row { display: grid; grid-template-columns: 265px 1fr 64px; gap: .6rem; align-items: center; margin: .34rem 0; }
.km-label { font-size: .8rem; color: var(--ink-700, #2a2438); text-align: right; line-height: 1.3; }
.km-label i { color: var(--ink-500, #71688a); font-style: normal; font-size: .72rem; }
.km-track { display: block; background: #efeaf6; border-radius: 6px; height: 14px; overflow: hidden; }
.km-bar { display: block; height: 100%; background: linear-gradient(90deg, #8a63b8, #6B489D); border-radius: 6px; min-width: 3px; }
.km-bar--alt { background: linear-gradient(90deg, #8a63b8, #6B489D); }
.km-val { font-size: .78rem; color: var(--ink-500, #71688a); }
@media (max-width: 900px) { .km-grid { grid-template-columns: 1fr; } }
/* 学习路径页 */
.paths-main { max-width: 1080px; margin: 0 auto; padding: 1.5rem 1rem 3rem; }
.pp-chart { background: var(--surface, #fff); border: 1px solid var(--line, #e6e1ef); border-radius: var(--radius-md, 12px); padding: 1.2rem 1.3rem; display: grid; gap: .8rem; }
.pp-row { display: grid; grid-template-columns: 220px 1fr; gap: .8rem; align-items: center; }
.pp-label { font-size: .88rem; font-weight: 600; color: var(--ink-700, #2a2438); }
.pp-track { display: flex; gap: 4px; }
.pp-seg { display: block; padding: .5rem 0; text-align: center; color: #fff; font-size: .8rem; font-weight: 600; text-decoration: none; border-radius: 6px; }
.pp-seg:hover { filter: brightness(1.12); }
.pp-seg--1 { background: #d9c9ec; color: #4a3468; }
.pp-seg--2 { background: #c2a8e0; }
.pp-seg--3 { background: #a986d2; }
.pp-seg--4 { background: #8f66c2; }
.pp-seg--5 { background: #7a4fb0; }
.pp-seg--6 { background: #6B489D; }
.learning-paths { display: grid; gap: 1.4rem; margin-top: 1.6rem; }
.learning-path { background: var(--surface, #fff); border: 1px solid var(--line, #e6e1ef); border-radius: var(--radius-md, 12px); overflow: hidden; }
.path-cover { position: relative; padding: 3.2rem 1.5rem 1.6rem; color: #fff; min-height: 190px; display: flex; align-items: flex-end; }
.path-cover img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0; }
.path-cover .path-shade { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(28,16,48,.30) 0%, rgba(28,16,48,.78) 100%); z-index: 1; }
.path-cover header { position: relative; z-index: 2; }
.path-cover header p { margin: 0; font-size: .78rem; letter-spacing: .12em; color: #ffd98a; }
.path-cover header h2 { margin: .2rem 0 .3rem; font-size: 1.25rem; text-shadow: 0 1px 8px rgba(10,4,26,.45); }
.path-cover header span { color: #ece7f5; font-size: .92rem; }
.learning-path ol { list-style: none; margin: 0; padding: .4rem 0; counter-reset: step; }
.learning-path ol li { counter-increment: step; display: grid; grid-template-columns: 2.6rem 1fr; column-gap: 1.2rem; grid-template-areas: "num title" "num desc"; align-items: start; padding: .95rem 1.5rem .95rem 2.6rem; border-bottom: 1px solid #f0ecf6; }
.learning-path ol li:last-child { border-bottom: none; }
.learning-path ol li::before { content: counter(step); grid-area: num; width: 1.9rem; height: 1.9rem; display: flex; align-items: center; justify-content: center; background: #efeaf6; color: var(--ale-purple-700, #6B489D); border-radius: 50%; font-weight: 700; font-size: .88rem; }
.learning-path ol li a { grid-area: title; font-weight: 600; color: var(--ale-purple-700, #6B489D); text-decoration: none; }
.learning-path ol li a:hover { text-decoration: underline; }
.learning-path ol li p { grid-area: desc; margin: .15rem 0 0; color: var(--ink-500, #71688a); font-size: .85rem; }
@media (max-width: 760px) { .pp-row { grid-template-columns: 1fr; } .pp-label { text-align: left; } }
/* 板块页横幅：图片背景 + 渐变遮罩（替代纯色大条） */
.course-intro--img { position: relative; overflow: hidden; border-radius: var(--radius-md, 12px); max-width: 1080px; margin: 1.4rem auto 0; padding: 3rem 2.2rem; background: none; color: #fff; }
.course-intro--img img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center 24%; z-index: 0; }
.course-intro--img .ci-shade { position: absolute; inset: 0; z-index: 1; background: linear-gradient(90deg, rgba(28,16,48,.84) 0%, rgba(28,16,48,.52) 46%, rgba(28,16,48,.08) 100%); }
.course-intro--img .ci-text { position: relative; z-index: 2; max-width: 40rem; }
.course-intro--img .ci-text h1 { margin: .3rem 0 .6rem; font-size: 1.9rem; text-shadow: 0 1px 8px rgba(10,4,26,.4); }
.course-intro--img .ci-text p { margin: 0; color: #ece7f5; line-height: 1.75; }
.course-intro--img .ci-text .eyebrow { color: #ffd98a; }
@media (max-width: 760px) { .course-intro--img { padding: 1.6rem 1.3rem; } .course-intro--img .ci-text h1 { font-size: 1.4rem; } }
"""


def main():
    if os.path.exists(SITE):
        shutil.rmtree(SITE)
    shutil.copytree(ASSETS_SRC + r"\css", os.path.join(SITE, "assets", "css"))
    shutil.copytree(ASSETS_SRC + r"\img", os.path.join(SITE, "assets", "img"))
    shutil.copytree(ASSETS_SRC + r"\js", os.path.join(SITE, "assets", "js"))
    w("assets/css/portal.css", PORTAL_CSS)

    build_index()
    build_paths()
    build_search_index()
    build_board("rainbow", "cloud/index.html", "云通信板块 · Rainbow",
                "Rainbow 协作与云通信平台 3 门课程：<br>OXO Connect 集成、OmniPCX Enterprise 云化、Rainbow Hub。", "cloud",
                "banner-cloud.jpg")
    build_board(None, "communications/index.html", "通信产品线板块",
                "OmniPCX Enterprise、OXO Connect、OpenTouch 家族、Contact Center、<br>OmniVista 8770、Visual Automated Attendant。", "comm",
                "banner-comm.jpg")
    for c in COURSES:
        build_course(c)
    build_about()

    n = sum(len(fs) for _r, _d, fs in os.walk(SITE))
    print("site built: %d files -> %s" % (n, SITE))


if __name__ == "__main__":
    main()
