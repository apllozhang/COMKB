# -*- coding: utf-8 -*-
"""批量安装各书 dist 到全局技能库（目录名取 verified.yaml 的 entry.name）。"""
import io
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BOOKS = r"F:\AIwork\ZCode\books"
SKILLS = r"C:\Users\Administrator\.agents\skills"

installed = []
for d in sorted(os.listdir(BOOKS)):
    bdir = os.path.join(BOOKS, d)
    vy = os.path.join(bdir, ".cangjie", "capabilities", "verified.yaml")
    dist = os.path.join(bdir, ".cangjie", "dist")
    if not (os.path.isfile(vy) and os.path.isdir(dist)):
        continue
    s = io.open(vy, encoding="utf-8").read()
    m = re.search(r"^entry:\s*\n\s*name:\s*(\S+)", s, re.M)
    if not m:
        print("[%s] entry.name 未找到，跳过" % d)
        continue
    name = m.group(1)
    dst = os.path.join(SKILLS, name)
    r = subprocess.run(
        ["robocopy", dist, dst, "/E", "/NFL", "/NDL", "/NJH", "/NJS"],
        capture_output=True)
    ok = r.returncode in (0, 1, 2, 3)
    installed.append("%s->%s%s" % (d, name, "" if ok else "(FAIL rc=%d)" % r.returncode))

print("installed %d:" % len(installed))
for x in installed:
    print(" ", x)
