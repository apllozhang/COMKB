# -*- coding: utf-8 -*-
"""批量发布所有已完成课程的门户子站页面。
注册表 REG：code -> (课程标题, crumb 分组)。只发布存在 verified.yaml 的书。
用法：build_comm_portal.py 之后、部署之前运行（替代单本发布脚本）。"""
import os
import re
import sys

import markdown
import yaml

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SITE = r"F:\AIwork\ZCode\ale_comm_site\site"
BOOKS = r"F:\AIwork\ZCode\books"

# code -> (课程标题, crumb 分组路径, 简称)
REG = {
    "oxocxte107en": ("OXO Connect · 呼叫中心", "communications", "oxo-connect-call-center", ""),
    "rainxte001en": ("Rainbow OXO Connect 集成", "cloud"),
    "otfcxte200en": ("OpenTouch Fax Center · Starter", "communications"),
    "otmcxte200en": ("OpenTouch Message Center · Starter", "communications"),
    "openxte225en": ("OpenTouch · 移动与远程办公", "communications"),
    "dectxte200en": ("OmniPCX Enterprise · DECT 解决方案", "communications"),
    "rainxte003en": ("Rainbow for OmniPCX Enterprise", "cloud"),
    "rainxte101en": ("Rainbow Hub", "cloud"),
    "vsaaxte001en": ("Visual Automated Attendant · 安装、配置与维护", "communications"),
    "entpxte421en": ("OmniPCX Enterprise · 加密解决方案", "communications"),
    "entpxte402en": ("OmniPCX Enterprise · 系统装载", "communications"),
    "entpxte403en": ("OmniPCX Enterprise · SIP", "communications"),
    "openxte301en": ("OpenTouch · Advanced", "communications"),
    "otccxte150en": ("OmniTouch Contact Center Standard · Advanced Call Routing", "communications"),
    "oxocxte300en": ("OXO Connect · Starter", "communications"),
    "entpxte401en": ("OmniPCX Enterprise · Advanced", "communications"),
    "8770xte202en": ("OmniVista 8770 · 目录管理", "communications"),
    "otccxte101en": ("OmniTouch Contact Center Standard · Advanced", "communications"),
    "oxocxte301en": ("OXO Connect · Advanced", "communications"),
    "openxte300en": ("OpenTouch · Starter", "communications"),
    "dt00xte215en": ("OmniSwitch LAN Access Switching", "communications", "dt00xte215en", "素材目录标注为「Postsales on ALE Connect」，PDF 实际内容为 OmniSwitch LAN Access Switching R8（与网络门户 DT00XTE215 同源）。归类说明：本课按实际内容收录于通信产品线，网络侧同源课程见网络门户。"),
    "otccxte100en": ("OmniTouch Contact Center Standard · Starter", "communications"),
    "8770xte201en": ("OmniVista 8770 · 计费与性能管理", "communications"),
    "8770xte200en": ("OmniVista 8770 · 安装与网络管理", "communications"),
    "entpxte400en": ("OmniPCX Enterprise · Starter", "communications"),
}

MD_EXT = ["tables", "fenced_code"]
CSS_REFS = (
    '<link rel="stylesheet" href="/assets/css/tokens.css?v=4">\n'
    '  <link rel="stylesheet" href="/assets/css/layout.css?v=4">\n'
    '  <link rel="stylesheet" href="/assets/css/components.css?v=4">\n'
    '  <link rel="stylesheet" href="/assets/css/content.css?v=7">\n'
    '  <link rel="stylesheet" href="/assets/css/portal.css?v=11">'
)


def md2html(text):
    html = markdown.markdown(text, extensions=MD_EXT)
    html = re.sub(r"<table>.*?</table>", lambda m: '<div class="table-scroll">%s</div>' % m.group(), html, flags=re.S)
    return html


def read(fp):
    with open(fp, encoding="utf-8") as f:
        return f.read()


def w(rel, html):
    fp = os.path.join(SITE, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


def shell(title, crumb, sidebar, main_class, body_html, meta_line):
    topbar = (
        '<header class="topbar" data-topbar>'
        '<a class="brand" href="/index.html"><img src="/assets/img/ale-logo-color.png" alt="ALE"><span>ALE 培训门户 · Communications</span></a>'
        '<nav id="primary-nav" class="primary-nav" aria-label="主导航">'
        '<a href="/index.html">首页</a>'
        '<a href="/cloud/index.html">云通信</a>'
        '<a href="/communications/index.html">通信产品线</a>'
        '<a href="/about.html">关于门户</a>'
        '<a href="http://10.20.30.103:8899/">网络门户 ↗</a>'
        '</nav></header>'
    )
    return (
        '<!doctype html>\n<html lang="zh-CN">\n<head>\n  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '  <meta name="theme-color" content="#6B489D">\n  <title>%s</title>\n'
        '  <link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">\n  %s\n</head>\n'
        '<body data-page-kind="course">\n  %s\n<div class="course-layout">\n%s\n'
        '  <main id="main-content" class="%s">\n'
        '    <nav class="breadcrumbs" aria-label="面包屑">%s</nav>\n%s\n'
        '    <footer class="content-footer">仅供内部学习使用 · 教材版权归 ALE Training Services 所有 · '
        '姊妹站：<a href="http://10.20.30.103:8899/">ALE Networking 技术培训门户</a></footer>\n'
        '  </main>\n</div>\n</body>\n</html>\n'
        % (title, CSS_REFS, topbar, sidebar, main_class, crumb, body_html)
    ) + meta_line


def publish_book(code, title, crumb_group, ws=None, note=""):
    book = os.path.join(BOOKS, ws or code)
    cap_dir = os.path.join(book, ".cangjie", "capabilities")
    vpath = os.path.join(cap_dir, "verified.yaml")
    if not os.path.isfile(vpath):
        return None
    bundle = yaml.safe_load(read(vpath))
    caps = bundle["capabilities"]
    promoted = [c for c in caps if c["promotion"]["destination"] == "promoted"]
    router = [c for c in caps if c["promotion"]["destination"] == "router"]
    n_caps = len(caps)
    bk = bundle.get("book", {})
    edition = ""
    pages = ""
    m = re.search(r"Edition (\d+)|Issue (\d+)", bk.get("title", "") + " " + read(os.path.join(book, "BOOK_OVERVIEW.md"))[:2000])
    base = "/courses/%s/" % code

    # 书元信息：从 BOOK_OVERVIEW 头部抓 Edition 与页数
    ov_head = read(os.path.join(book, "BOOK_OVERVIEW.md"))[:3000]
    me = re.search(r"Edition (\d+)|Issue (\d+)|Edition[:\s]*([A-Za-z0-9 ]+)", ov_head)
    ed_txt = ("Edition %s" % (me.group(1) or me.group(2) or me.group(3).strip())) if me else "—"
    mp = re.search(r"(\d+) 页", ov_head)
    pg_txt = ("%s 页" % mp.group(1)) if mp else "—"
    meta_line = ('<!-- book: %s | edition: %s | pages: %s -->' % (bk.get("title", code), ed_txt, pg_txt))

    # 元信息行（sidebar + hero 用）
    sub_meta = "%s · %s · 文档整理入库（%d 个知识单元）" % (ed_txt, pg_txt, n_caps)
    skill_name = bundle["entry"]["name"]

    def build_sidebar(active_slug=None):
        meta = ('<div class="sidebar-heading"><p class="eyebrow">COURSE</p><h2>%s</h2>'
                '<p>%s</p></div>' % (title, sub_meta))
        links = [
            '<a aria-current="page" href="%sindex.html">课程首页</a>' % base,
            '<a href="%sdigest.html">精华长文</a>' % base,
            '<a href="%soverview.html">教书理解</a>' % base,
            '<a href="%sglossary.html">术语词典</a>' % base,
        ]

        def group(name, items):
            return '<p class="course-nav-group">%s</p>%s' % (
                name, "".join('<a%s href="%sskills/%s.html">%s</a>' % (
                    ' aria-current="page"' if c["slug"] == active_slug else "", base, c["slug"], c["title"]) for c in items))

        nav = ('<nav class="course-nav" aria-label="课程目录">%s%s%s%s</nav>' % (
            "".join(links),
            group("核心能力", promoted),
            group("路由能力", router),
            '<p class="course-nav-group">已安装技能</p>'
            '<a href="%sindex.html">%s（%d 能力）</a>' % (base, skill_name, n_caps),
        ))
        return '<aside class="course-sidebar">%s%s</aside>' % (meta, nav)

    crumb_home = ('<a href="/index.html">首页</a><span>/</span>'
                  '<a href="/%s/index.html">%s</a><span>/</span>'
                  '<span aria-current="page">%s</span>' % (crumb_group, "云通信" if crumb_group == "cloud" else "通信产品线", code.upper()))

    sidebar = build_sidebar()

    # 能力卡页
    titles = {x["slug"]: x["title"] for x in caps}
    for c in caps:
        card_md = read(os.path.join(cap_dir, c["card"]))
        body_html = md2html(card_md)
        also = c.get("also_read") or []
        also_links = "、".join('<a href="%sskills/%s.html">%s</a>' % (base, s, titles.get(s, s)) for s in also) or "—"
        body_html += (
            '<h2>相关能力</h2><p>%s</p>'
            '<p class="source-page">能力 ID：%s · 来源：%s · 仅供内部学习</p>'
            % (also_links, c["capability_id"], code.upper()))
        heading = ('<header class="skill-heading"><div><p class="eyebrow">KNOWLEDGE UNIT</p>'
                   '<h1>%s</h1></div><dl><div><dt>Skill ID</dt><dd>%s</dd></div>'
                   '<div><dt>形态</dt><dd>%s</dd></div></dl></header>'
                   % (c["title"], c["slug"], c["promotion"]["destination"]))
        crumb = ('<a href="/index.html">首页</a><span>/</span>'
                 '<a href="%sindex.html">%s</a><span>/</span>'
                 '<span aria-current="page">%s</span>' % (base, code.upper(), c["title"]))
        html = shell(c["title"], crumb, sidebar, "course-main prose", heading + '<article class="markdown-body">' + body_html + "</article>", meta_line)
        w("courses/%s/skills/%s.html" % (code, c["slug"]), html)

    # DIGEST
    body = '<header class="skill-heading"><div><p class="eyebrow">DIGEST</p><h1>整理摘要 — 全书精华</h1></div></header>'
    body += '<article class="markdown-body">' + md2html(read(os.path.join(book, "DIGEST.md"))) + "</article>"
    crumb = ('<a href="/index.html">首页</a><span>/</span>'
             '<a href="%sindex.html">%s</a><span>/</span><span aria-current="page">整理摘要</span>' % (base, code.upper()))
    html = shell("整理摘要 · %s" % code.upper(), crumb, sidebar, "course-main prose", body, meta_line)
    w("courses/%s/digest.html" % code, html)

    # GLOSSARY
    body = '<header class="skill-heading"><div><p class="eyebrow">GLOSSARY</p><h1>术语词典 — 中英对照</h1></div></header>'
    body += '<article class="markdown-body">' + md2html(read(os.path.join(cap_dir, "book", "glossary.md"))) + "</article>"
    crumb = ('<a href="/index.html">首页</a><span>/</span>'
             '<a href="%sindex.html">%s</a><span>/</span><span aria-current="page">术语词典</span>' % (base, code.upper()))
    html = shell("术语词典 · %s" % code.upper(), crumb, sidebar, "course-main prose", body, meta_line)
    w("courses/%s/glossary.html" % code, html)

    # OVERVIEW
    body = '<header class="skill-heading"><div><p class="eyebrow">BOOK OVERVIEW</p><h1>教书理解 — 整书骨架与任务清单</h1></div></header>'
    body += '<article class="markdown-body">' + md2html(read(os.path.join(book, "BOOK_OVERVIEW.md"))) + "</article>"
    crumb = ('<a href="/index.html">首页</a><span>/</span>'
             '<a href="%sindex.html">%s</a><span>/</span><span aria-current="page">教书理解</span>' % (base, code.upper()))
    html = shell("教书理解 · %s" % code.upper(), crumb, sidebar, "course-main prose", body, meta_line)
    w("courses/%s/overview.html" % code, html)

    # 课程主页
    def cap_link(c):
        return ('<a href="%sskills/%s.html"><b>%s</b><code>%s</code>'
                '<span>%s</span></a>' % (base, c["slug"], c["title"], c["slug"], c["one_liner"]))

    def cap_section(name, items):
        return "<section><h3>%s</h3><div>%s</div></section>" % (name, "".join(cap_link(c) for c in items))

    body = f"""
    <header class="course-intro"><p class="eyebrow">{code.upper()}</p><h1>{title}</h1>
    <p>{sub_meta}</p>
    <div class="chips"><span>{ed_txt}</span><span>{pg_txt}</span><span>{n_caps} 个能力单元</span><span>1 个已安装技能</span></div></header>
    {('<aside class="course-note"><strong>归类说明</strong>：%s</aside>' % note) if note else ''}
    <section><div class="section-heading"><div><p class="eyebrow">EXECUTABLE KNOWLEDGE</p><h2>知识单元</h2></div></div>
      <div class="skill-groups">{cap_section("核心能力", promoted)}{cap_section("路由能力", router)}</div>
    </section>
    <section class="reading-links"><h2>课程全景资料</h2><a href="{base}digest.html">精华长文 DIGEST</a><a href="{base}overview.html">教书理解 BOOK_OVERVIEW</a><a href="{base}glossary.html">术语词典</a></section>
"""
    html = shell(title, crumb_home, sidebar, "course-main", body, meta_line)
    w("courses/%s/index.html" % code, html)
    return n_caps


def main():
    done, skipped = [], []
    for code, cfg in REG.items():
        title, group = cfg[0], cfg[1]
        ws = cfg[2] if len(cfg) > 2 else code
        note = cfg[3] if len(cfg) > 3 else ""
        n = publish_book(code, title, group, ws, note)
        if n:
            done.append("%s(%d)" % (code, n))
        else:
            skipped.append(code)
    print("published %d: %s" % (len(done), " ".join(done)))
    print("pending %d: %s" % (len(skipped), " ".join(skipped)))


if __name__ == "__main__":
    main()
