# -*- coding: utf-8 -*-
"""post_patch.py — build+publish 之后把"现场支持板块/侧栏交互/工具区/CSS"等
成品增强补丁回灌到站点。确定性、幂等；片段源在 comm_portal_assets/patch_src/。

用法: python post_patch.py [--site <site_dir>] [--src <patch_src_dir>]
链路顺序: build_comm_portal.py → publish_all.py → post_patch.py → verify → deploy
"""
import argparse
import io
import json
import os
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
DEF_SITE = r"F:\AIwork\ZCode\ale_comm_site\site"
# 片段源优先取脚本同目录 patch_src（仓库形态），回退工作区路径
DEF_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "patch_src")
if not os.path.isdir(DEF_SRC):
    DEF_SRC = r"F:\AIwork\ZCode\.cangjie\comm_portal_assets\patch_src"

# 全站标准导航（成品站口径，2026-09-24 更新）
NAV_RE = re.compile(r'(<nav id="primary-nav"[^>]*>).*?(</nav>)', re.S)
NAV_CANON = ('<a href="/index.html">首页</a>'
             '<a href="/paths.html">学习路径</a>'
             '<a href="/field/index.html">现场支持</a>'
             '<a href="/cloud/index.html">云通信</a>'
             '<a href="/communications/index.html">通信产品线</a>'
             '<a href="/about.html">关于门户</a>'
             '<a href="http://10.20.30.103:8899/">网络门户 →</a>')
NO_CHROME = ("index.html", "about.html", "paths.html")  # 无返回按钮/脚本的三个壳页


def rd(p):
    if not os.path.isfile(p):
        return ""
    return io.open(p, encoding="utf-8", errors="replace").read()


def wr(p, t):
    # 线上 HTML 统一 CRLF 口径（与成品站一致）
    io.open(p, "w", encoding="utf-8", newline="\r\n").write(t)


def patch_html(t, snippets, rel):
    changed = False
    # 0) DECT 课程标题零宽空格换行提示：title/h1/h2 全站；卡片链接仅 communications 板块
    dt = "OmniPCX Enterprise \u00b7 DECT \u89e3\u51b3\u65b9\u6848"
    dtz = "OmniPCX Enterprise \u00b7\u200b DECT \u89e3\u51b3\u65b9\u6848"
    pats = ["<title>%s</title>" % dt, "<h1>%s</h1>" % dt, "<h2>%s</h2>" % dt]
    if rel.startswith("communications"):
        pats.append('dectxte200en/index.html">%s</a>' % dt)
    for pat in pats:
        if pat in t:
            t = t.replace(pat, pat.replace(dt, dtz))
            changed = True
    # 1) 导航规范化为标准块
    m = NAV_RE.search(t)
    if m and m.group(1) + NAV_CANON + m.group(2) != m.group(0):
        t = t[:m.start()] + m.group(1) + NAV_CANON + m.group(2) + t[m.end():]
        changed = True
    # 2) portal.css 版本号
    if "portal.css?v=11" not in t and "portal.css?v=10" in t:
        t = t.replace("portal.css?v=10", "portal.css?v=11")
        changed = True
    # 3) 壳页特例（用相对路径精确匹配）：整段旧尾 → 新尾
    if rel in NO_CHROME:
        pairs = []
        if rel == "index.html":
            pairs.append(("tools_home_old", "tools_home_new"))
        if rel == "paths.html":
            pairs.append(("tools_paths_old", "tools_paths_new"))
        if rel == "about.html":
            pairs.append(("about_old", "about_new"))
        for old_f, new_f in pairs:
            old_t, new_t = snippets[old_f], snippets[new_f]
            if not old_t or old_t not in t:
                continue
            if "tools_" in old_f and 'id="tools"' in t:
                continue  # 工具区已在，避免重复插入
            t = t.replace(old_t, new_t, 1)
            changed = True
        return t, changed
    # 4) 其余页面：返回按钮 + 侧栏脚本 + 课程布局手柄
    if 'id="btn-back"' not in t and "</header>" in t:
        t = t.replace("</header>", snippets["btnback"] + "</header>", 1)
        changed = True
    if "var layout = document.querySelector('.course-layout')" not in t and "</body>" in t:
        t = t.replace("</body>", "\n" + snippets["script"] + "\n</body>", 1)
        changed = True
    if 'class="course-layout"' in t and 'id="sidebar-resizer"' not in t:
        before = t
        t = t.replace('<div class="course-layout">\n<aside class="course-sidebar">',
                      '<div class="course-layout">' + snippets["resizer"] + '<aside class="course-sidebar">', 1)
        if t == before:
            t = t.replace('<div class="course-layout">',
                          '<div class="course-layout">' + snippets["resizer"], 1)
        changed = True
    if 'class="sidebar-heading"' in t and 'id="sidebar-dock"' not in t:
        t = t.replace('<div class="sidebar-heading">',
                      '<div class="sidebar-heading">' + snippets["dock"], 1)
        changed = True
    return t, changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default=DEF_SITE)
    ap.add_argument("--src", default=DEF_SRC)
    args = ap.parse_args()
    site, src = args.site, args.src

    snippets = dict(
        resizer=rd(os.path.join(src, "snippet_resizer.html")),
        dock=rd(os.path.join(src, "snippet_dock.html")),
        btnback=rd(os.path.join(src, "snippet_btnback.html")),
        script=rd(os.path.join(src, "snippet_script.html")),
        tools_home_old=rd(os.path.join(src, "snippet_tools_home_old.html")),
        tools_home_new=rd(os.path.join(src, "snippet_tools_home_new.html")),
        tools_paths_old=rd(os.path.join(src, "snippet_tools_paths_old.html")),
        tools_paths_new=rd(os.path.join(src, "snippet_tools_paths_new.html")),
        about_old=rd(os.path.join(src, "snippet_about_old.html")),
        about_new=rd(os.path.join(src, "snippet_about_new.html")),
    )

    n_html = n_changed = 0
    for dirpath, dirnames, filenames in os.walk(site):
        dirnames[:] = [d for d in dirnames if d != "field"]
        for fn in filenames:
            if not fn.endswith(".html"):
                continue
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(p, site)
            t = rd(p)
            n_html += 1
            t2, changed = patch_html(t, snippets, rel)
            if changed:
                wr(p, t2)
                n_changed += 1
            elif t2 != t:
                wr(p, t2)
                n_changed += 1

    # field/ 四页原样覆盖
    for fn in ("index.html", "versions.html", "symptoms.html", "runbooks.html"):
        dst = os.path.join(site, "field", fn)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(os.path.join(src, "field", fn), dst)

    # 两个 CSS 原样覆盖
    for fn in ("layout.css", "portal.css"):
        shutil.copyfile(os.path.join(src, fn), os.path.join(site, "assets", "css", fn))

    # 4) 课程页内容级补丁（V 段/段落拆分等，逐文件顺序替换）
    split_file = os.path.join(src, "content_split.json")
    if os.path.isfile(split_file):
        split_map = json.load(io.open(split_file, encoding="utf-8"))
    else:
        split_map = {}

    # 5) 冻结页：base/live 双存；生成页偏离 base（源已更新）时跳过并告警
    frozen_dir = os.path.join(src, "frozen_pages")
    n_frozen = n_frozen_skip = 0
    if os.path.isdir(frozen_dir):
        for fn in sorted(os.listdir(frozen_dir)):
            if not fn.endswith(".html") or fn.endswith(".base.html"):
                continue
            rel = fn.replace("__", "\\")
            gen = os.path.join(site, rel)
            if not os.path.isfile(gen):
                continue
            base = rd(os.path.join(frozen_dir, fn.replace(".html", ".base.html")))
            live_v = rd(os.path.join(frozen_dir, fn))
            t = rd(gen)
            if t == live_v:
                continue  # 已应用过，静默跳过
            if t != base:
                print("[warn] 冻结页源已漂移，跳过覆盖: %s" % rel)
                n_frozen_skip += 1
                continue
            wr(gen, live_v)
            n_frozen += 1

    n_pairs = 0
    for dirpath, dirnames, filenames in os.walk(site):
        for fn in filenames:
            if not fn.endswith(".html"):
                continue
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(p, site)
            plist = split_map.get(rel)
            if not plist:
                continue
            t = rd(p)
            for old, new in plist:
                if old and old in t:
                    t = t.replace(old, new, 1)
                    n_pairs += 1
            wr(p, t)

    print("post_patch: %d html 扫描, %d 页修改; 内容替换 %d 处; 冻结页应用 %d（跳过 %d）; field/ 与 css 已同步"
          % (n_html, n_changed, n_pairs, n_frozen, n_frozen_skip))


if __name__ == "__main__":
    main()
