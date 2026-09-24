# -*- coding: utf-8 -*-
"""部署 ALE Communications 门户到 103：上传 + docker nginx:alpine 8900 + 验证。"""
import os
import sys
import time
import paramiko

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HOST = os.environ.get("COMKB_DEPLOY_HOST", "")
USER = os.environ.get("COMKB_DEPLOY_USER", "")
PWD = os.environ.get("COMKB_DEPLOY_PWD", "")
if not (HOST and USER and PWD):
    sys.exit("请先设置环境变量 COMKB_DEPLOY_HOST / COMKB_DEPLOY_USER / COMKB_DEPLOY_PWD")
REMOTE = "/home/tina/ale-comm-site/site"
LOCAL = r"F:\AIwork\ZCode\ale_comm_site\site"

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(HOST, username=USER, password=PWD, timeout=10)


def run(cmd, timeout=60, show=True):
    _stdin, out, err = c.exec_command(cmd, timeout=timeout)
    o = out.read().decode("utf-8", "replace")
    e = err.read().decode("utf-8", "replace")
    if show:
        print("$ %s" % cmd)
        if o.strip():
            print(o.rstrip()[:2000])
        if e.strip():
            print("[stderr] %s" % e.rstrip()[:300])
        print()
    return o.strip(), e.strip()


# 0) 先清理自己的旧容器，再确认端口空闲
run("docker rm -f ale-comm-web 2>/dev/null; echo ok", show=False)
o, _ = run("ss -tln | grep -c ':8900 ' || true", show=False)
if o and o != "0":
    print("PORT 8900 STILL IN USE BY OTHER SERVICE -> abort")
    c.close()
    sys.exit(1)

# 1) 上传
files = []
for dirpath, _dirs, names in os.walk(LOCAL):
    for name in names:
        lp = os.path.join(dirpath, name)
        rp = os.path.relpath(lp, LOCAL).replace("\\", "/")
        files.append((lp, rp))
print("local files: %d" % len(files))
run("rm -rf %s && mkdir -p %s" % (REMOTE, REMOTE))
sftp = c.open_sftp()
t0 = time.time()
for lp, rp in files:
    rdir = os.path.dirname(rp)
    if rdir:
        cur = REMOTE
        for p in rdir.split("/"):
            cur += "/" + p
            try:
                sftp.stat(cur)
            except IOError:
                sftp.mkdir(cur)
    sftp.put(lp, REMOTE + "/" + rp)
print("upload done in %.0fs" % (time.time() - t0))
o, _ = run("find %s -type f | wc -l" % REMOTE, show=False)
print("remote files: %s (expect %d)" % (o, len(files)))
if int(o) != len(files):
    print("MISMATCH -> abort")
    c.close()
    sys.exit(1)

# 2) docker 启动
run("docker run -d --name ale-comm-web --restart unless-stopped -p 8900:80 "
    "-v %s:/usr/share/nginx/html:ro nginx:alpine" % REMOTE)
run("docker ps --format '{{.Names}}  {{.Status}}  {{.Ports}}' | grep ale-comm-web")

# 3) 健康检查（等 nginx 就绪）
import time as _t
for _ in range(10):
    o, _e = run("curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8900/", show=False)
    if o == "200":
        break
    _t.sleep(1)
print("nginx ready: %s" % o)
checks = [
    ("home 200 + title", "curl -s http://127.0.0.1:8900/ | grep -c 'ALE Communications'"),
    ("home cards", "curl -s http://127.0.0.1:8900/ | grep -c 'course-card'"),
    ("cloud board", "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8900/cloud/index.html"),
    ("comm board", "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8900/communications/index.html"),
    ("about 200", "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8900/about.html"),
    ("course page 200", "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8900/courses/entpxte400en/index.html"),
    ("rainxte001en course 200", "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8900/courses/rainxte001en/index.html"),
    ("rainxte001en skill 200", "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8900/courses/rainxte001en/skills/rbx-gateway-planning.html"),
    ("rainxte001en digest 200", "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8900/courses/rainxte001en/digest.html"),
    ("course note page", "curl -s http://127.0.0.1:8900/courses/dt00xte215en/index.html | grep -c '归类说明'"),
    ("portal css 200", "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8900/assets/css/portal.css"),
    ("hero img 200", "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8900/assets/img/hero-rainbow.jpg"),
    ("old portal still ok", "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8899/"),
]
failed = 0
for name, cmd in checks:
    o, e = run(cmd, show=False)
    v = (o or e).strip()
    ok = v not in ("000", "") and v != "0"
    if name in ("cloud board", "comm board", "about 200", "course page 200", "portal css 200", "hero img 200", "old portal still ok"):
        ok = v == "200"
    if not ok:
        failed += 1
    print("  [%s] %-22s %s" % ("OK " if ok else "FAIL", name, v[:40]))

if failed:
    print("HEALTH FAILED (%d)" % failed)
else:
    print("ALL HEALTH CHECKS PASSED")

c.close()
print("DONE")
