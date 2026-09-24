# -*- coding: utf-8 -*-
"""门户站点自检：站内链接与资源引用断链检查。"""
import os
import re
import sys

ROOT = r"F:\AIwork\ZCode\ale_comm_site\site"
REF_RE = re.compile(r'(?:href|src)="([^"#?]+)(?:[?#][^"]*)?"')


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    missing = []
    n_html = 0
    for dirpath, _dirs, files in os.walk(ROOT):
        for name in files:
            if not name.endswith(".html"):
                continue
            n_html += 1
            fp = os.path.join(dirpath, name)
            with open(fp, encoding="utf-8") as f:
                html = f.read()
            for ref in REF_RE.findall(html):
                if ref.startswith(("http://", "https://", "#")):
                    continue
                p = ref.lstrip("/")
                if not os.path.isfile(os.path.join(ROOT, p)):
                    missing.append((os.path.relpath(fp, ROOT), ref))
    print("html=%d broken=%d" % (n_html, len(missing)))
    for f, ref in missing[:20]:
        print("  BROKEN %s -> %s" % (f, ref))
    # 关键页抽查
    idx = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    print("home: cards=%d groups=%d hero=%s" % (
        idx.count("course-card"), idx.count("catalog-group"), "hero-comm" in idx))
    c1 = open(os.path.join(ROOT, "courses", "entpxte400en", "index.html"), encoding="utf-8").read()
    print("course page: pending=%s meta=%s note=%s" % (
        "待蒸馏" in c1, "meta-list" in c1, "归类说明" in c1))
    print("PASS" if not missing else "FAIL")


if __name__ == "__main__":
    main()
