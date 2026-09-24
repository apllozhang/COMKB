/* ALE Communications 门户站内搜索（自包含静态索引版） */
(() => {
  const root = document.querySelector("[data-search]");
  if (!root) return;
  const input = root.querySelector("[data-search-input]");
  const box = root.querySelector("[data-search-results]");
  if (!input || !box) return;

  let idxPromise;
  const load = () => idxPromise ||= fetch("/search/index.json").then((r) => {
    if (!r.ok) throw new Error("search index " + r.status);
    return r.json();
  });
  const esc = (v) => { const d = document.createElement("span"); d.textContent = v; return d.innerHTML; };

  input.addEventListener("input", async () => {
    const q = input.value.trim().toLowerCase();
    if (q.length < 1) { box.innerHTML = ""; box.classList.remove("open"); return; }
    box.innerHTML = '<span class="search-state">正在检索…</span>';
    box.classList.add("open");
    try {
      const rows = await load();
      const scored = [];
      for (const e of rows) {
        const t = (e.t || "").toLowerCase(), s = (e.s || "").toLowerCase(), k = (e.k || "").toLowerCase();
        let sc = 0;
        if (t.startsWith(q)) sc += 4; else if (t.includes(q)) sc += 3;
        if (s.includes(q)) sc += 2;
        if (k.includes(q)) sc += 1;
        if (sc > 0) scored.push([sc, e]);
      }
      scored.sort((a, b) => b[0] - a[0]);
      const top = scored.slice(0, 12).map(([, e]) => e);
      box.innerHTML = top.length ? top.map((e) =>
        '<a class="search-result" role="option" href="/' + e.u + '"><b>' + esc(e.t) +
        '</b><small>' + esc(e.s) + '</small></a>').join("")
        : '<span class="search-state">没有匹配结果</span>';
    } catch (err) {
      box.innerHTML = '<span class="search-state">搜索暂时不可用</span>';
    }
  });
  document.addEventListener("click", (ev) => {
    if (!root.contains(ev.target)) box.classList.remove("open");
  });
  input.addEventListener("keydown", (ev) => {
    if (ev.key !== "Enter") return;
    const first = box.querySelector("a.search-result");
    if (first) window.location.href = first.getAttribute("href");
  });
})();
