/* STEM AI Scope — one script for every page. No build step, no dependencies. */
(() => {
  "use strict";

  // ---------- topic taxonomy ----------
  const GROUPS = {
    policy:     { label: "Policy & funding",        color: "var(--t-policy)" },
    education:  { label: "Education & literacy",    color: "var(--t-education)" },
    indigenous: { label: "Indigenous AI & futurism", color: "var(--t-indigenous)" },
    black:      { label: "Black AI & Afrofuturism", color: "var(--t-black)" },
    creative:   { label: "Creative & culture",      color: "var(--t-creative)" },
    ethics:     { label: "Ethics & safety",         color: "var(--t-ethics)" },
    community:  { label: "Community & workforce",   color: "var(--t-community)" },
    research:   { label: "Research",                color: "var(--t-research)" },
  };
  const TOPIC_GROUP = {
    policy: "policy", funding: "policy",
    "education-k12": "education", "post-secondary": "education", "adult-education": "education",
    teachers: "education", literacy: "education", "stem-outreach": "education", youth: "education",
    indigenous: "indigenous", "indigenous-futurism": "indigenous",
    "black-communities": "black", afrofuturism: "black",
    creative: "creative", culture: "creative",
    ethics: "ethics", safety: "ethics",
    community: "community", workforce: "community",
    research: "research",
  };
  const TOPIC_LABEL = {
    "education-k12": "K-12", "post-secondary": "Post-secondary", "adult-education": "Adult education",
    "stem-outreach": "STEM outreach", "black-communities": "Black communities", "indigenous-futurism": "Indigenous futurism",
  };
  const tLabel = t => TOPIC_LABEL[t] || t.charAt(0).toUpperCase() + t.slice(1).replace(/-/g, " ");
  // Pick the most specific group for colouring (focus areas win over generic ones).
  const PRIORITY = ["indigenous", "black", "creative", "education", "ethics", "community", "policy", "research"];
  const groupOf = item => {
    const gs = (item.topics || []).map(t => TOPIC_GROUP[t]).filter(Boolean);
    return PRIORITY.find(g => gs.includes(g)) || "research";
  };

  // ---------- helpers ----------
  const $ = (s, el = document) => el.querySelector(s);
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  const fmtDate = d => {
    if (!d) return "n.d.";
    const p = d.slice(0, 10).split("-");
    if (p.length === 1) return p[0];
    if (p.length === 2) return `${MONTHS[+p[1] - 1]} ${p[0]}`;
    return `${MONTHS[+p[1] - 1].slice(0, 3)} ${+p[2]}, ${p[0]}`;
  };
  const fmtRange = (a, b) => {
    const A = new Date(a + "T12:00:00"), B = new Date(b + "T12:00:00");
    const m = x => MONTHS[x.getMonth()].slice(0, 3);
    return A.getMonth() === B.getMonth() ? `${m(A)} ${A.getDate()}–${B.getDate()}, ${B.getFullYear()}` : `${m(A)} ${A.getDate()} – ${m(B)} ${B.getDate()}, ${B.getFullYear()}`;
  };
  const getJSON = async p => { const r = await fetch(p, { cache: "no-cache" }); if (!r.ok) throw new Error(p + " " + r.status); return r.json(); };
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch { /* ignore */ } },
  };
  const chip = t => `<span class="chip" style="color:${GROUPS[TOPIC_GROUP[t] || "research"].color}"><span class="dot"></span>${esc(tLabel(t))}</span>`;
  const itemHTML = it => `
    <div class="item">
      <a class="tt" href="${esc(it.url)}" target="_blank" rel="noopener">${esc(it.title)}</a>
      <div class="meta">${esc(it.publisher)} · ${fmtDate(it.date)} · ${esc(it.region || "")}${it.week ? ` · <a href="roundups.html?week=${it.week}">${it.week}</a>` : ""}</div>
      <p>${esc(it.summary)}</p>
      <div class="chips">${(it.topics || []).slice(0, 5).map(chip).join("")}</div>
    </div>`;

  // ---------- chrome (header/footer) ----------
  const PAGES = [
    ["index.html", "Home"], ["summary.html", "Summary"], ["brief.html", "Brief"], ["roundups.html", "Roundups"],
    ["timeline.html", "Timeline"], ["feed.html", "Feed"], ["sources.html", "Sources"], ["bibliography.html", "Bibliography"],
  ];
  const LOGO = `<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="14" fill="none" stroke="var(--accent)" stroke-width="2"/><circle cx="16" cy="16" r="8.5" fill="none" stroke="var(--accent-2)" stroke-width="1.5" stroke-dasharray="3 2.5"/><circle cx="16" cy="16" r="3" fill="var(--accent-3)"/><path d="M16 16 L27 8" stroke="var(--accent)" stroke-width="2" stroke-linecap="round"/><circle cx="24" cy="21" r="1.6" fill="var(--accent-4)"/><circle cx="9" cy="10" r="1.2" fill="var(--accent-2)"/></svg>`;
  function chrome() {
    const here = location.pathname.split("/").pop() || "index.html";
    const head = document.createElement("header");
    head.className = "site-head";
    head.innerHTML = `<div class="wrap">
      <a class="brand" href="index.html">${LOGO}<span>STEM AI SCOPE</span></a>
      <nav class="nav" aria-label="Main">${PAGES.map(([h, l]) => `<a href="${h}"${h === here ? ' aria-current="page"' : ""}>${l}</a>`).join("")}</nav>
      <button class="theme-btn" id="themeBtn" title="Toggle light/dark" aria-label="Toggle colour theme">◐</button></div>`;
    document.body.prepend(head);
    const foot = document.createElement("footer");
    foot.innerHTML = `<div class="wrap">STEM AI Scope is a landscape scan of AI in STEM education, community, ethics, creative practice, and Indigenous and Black AI, with Canada first and UK/EU second. Every item links to its original source. Weekly roundups are added automatically each Monday. <a href="https://github.com/oneLouder-repo/stem-ai-scope">Source &amp; data on GitHub</a>.</div>`;
    document.body.append(foot);
    const saved = store.get("theme");
    if (saved) document.documentElement.dataset.theme = saved;
    $("#themeBtn").onclick = () => {
      const cur = document.documentElement.dataset.theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      const nxt = cur === "dark" ? "light" : "dark";
      document.documentElement.dataset.theme = nxt; store.set("theme", nxt);
    };
  }

  // ---------- data ----------
  let _data;
  async function loadAll() {
    if (_data) return _data;
    const [items, index] = await Promise.all([getJSON("data/items.json"), getJSON("data/roundups/index.json")]);
    const byId = Object.fromEntries(items.items.map(i => [i.id, i]));
    _data = { items: items.items, byId, index };
    return _data;
  }
  const loadRoundup = id => getJSON(`data/roundups/${id}.json`);

  // ---------- tiny markdown ----------
  function md(src) {
    const inline = s => esc(s)
      .replace(/\[([^\]]+)\]\((https?:[^)\s]+|[\w./#?=-]+)\)/g, '<a href="$2">$1</a>')
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/(^|[^*])\*([^*\s][^*]*)\*/g, "$1<em>$2</em>")
      .replace(/`([^`]+)`/g, "<code>$1</code>");
    const out = []; let list = null, para = [], quote = [], table = [];
    const flush = () => {
      if (para.length) { out.push(`<p>${inline(para.join(" "))}</p>`); para = []; }
      if (list) { out.push(`<${list.t}>${list.items.map(i => `<li>${inline(i)}</li>`).join("")}</${list.t}>`); list = null; }
      if (quote.length) { out.push(`<blockquote>${quote.map(q => `<p>${inline(q)}</p>`).join("")}</blockquote>`); quote = []; }
      if (table.length) {
        const rows = table.filter(r => !/^\|?\s*:?-{2,}/.test(r)).map(r => r.replace(/^\||\|$/g, "").split("|").map(c => c.trim()));
        out.push(`<div class="table-wrap"><table><thead><tr>${rows[0].map(c => `<th>${inline(c)}</th>`).join("")}</tr></thead><tbody>${rows.slice(1).map(r => `<tr>${r.map(c => `<td>${inline(c)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`);
        table = [];
      }
    };
    for (const raw of src.split(/\r?\n/)) {
      const line = raw.trimEnd();
      let m;
      if (!line.trim()) { flush(); continue; }
      if ((m = line.match(/^(#{1,4})\s+(.*)/))) { flush(); const id = m[2].toLowerCase().replace(/[^\w]+/g, "-").replace(/^-|-$/g, ""); out.push(`<h${m[1].length} id="${id}">${inline(m[2])}</h${m[1].length}>`); continue; }
      if (/^---+$/.test(line)) { flush(); out.push("<hr>"); continue; }
      if (line.startsWith("|")) { if (para.length || list || quote.length) flush(); table.push(line); continue; }
      if ((m = line.match(/^>\s?(.*)/))) { if (para.length || list) flush(); quote.push(m[1]); continue; }
      if ((m = line.match(/^\s*([-*]|\d+\.)\s+(.*)/))) {
        const t = /\d/.test(m[1]) ? "ol" : "ul";
        if (para.length || quote.length) flush();
        if (!list || list.t !== t) { flush(); list = { t, items: [] }; }
        list.items.push(m[2]); continue;
      }
      if (list && /^\s{2,}/.test(raw)) { list.items[list.items.length - 1] += " " + line.trim(); continue; }
      if (list || quote.length || table.length) flush();
      para.push(line.trim());
    }
    flush();
    return out.join("\n");
  }

  // ---------- APA 7 ----------
  function apa(it) {
    const d = it.date || "";
    const p = d.split("-");
    const date = !d ? "n.d." : p.length === 1 ? p[0] : p.length === 2 ? `${p[0]}, ${MONTHS[+p[1] - 1]}` : `${p[0]}, ${MONTHS[+p[1] - 1]} ${+p[2]}`;
    const author = it.author ? it.author.replace(/\.$/, "") + "." : esc(it.publisher).replace(/\.$/, "") + ".";
    const site = it.author ? ` ${esc(it.publisher)}.` : "";
    const ital = ["report", "research"].includes(it.kind);
    const title = ital ? `<em>${esc(it.title)}</em>` : esc(it.title);
    return `${esc(author)} (${date}). ${title}.${site} <a href="${esc(it.url)}">${esc(it.url)}</a>`;
  }
  const sortKey = it => (it.author || it.publisher || "").replace(/^(The|La|Le)\s+/i, "").toLowerCase();

  // ---------- pages ----------
  async function home() {
    const { items, index, byId } = await loadAll();
    const latest = index[0];
    const r = await loadRoundup(latest.id);
    let srcCount = 0, feedInfo = null;
    try { srcCount = (await getJSON("data/sources.json")).sources.length; } catch {}
    try { feedInfo = await getJSON("data/feed.json"); } catch {}

    $("#latest").innerHTML = `
      <div class="wk">LATEST ROUNDUP · ${r.id} · ${fmtRange(r.start, r.end)}</div>
      <h2 style="margin-top:.3em">${esc(r.headline)}</h2>
      <p>${esc(r.digest)}</p>
      <div>${r.item_ids.map(id => byId[id]).filter(Boolean).map(itemHTML).join("") || '<p class="faint">No items yet this week.</p>'}</div>
      <p><a class="btn" href="roundups.html?week=${r.id}">Open roundup →</a> <a class="btn" href="roundups.html">All roundups</a></p>`;

    const scanned = items.filter(i => i.week);
    const canada = scanned.filter(i => /Canada/.test(i.region)).length;
    const ukeu = scanned.filter(i => /UK|EU/.test(i.region)).length;
    $("#stats").innerHTML = [
      [index.length, "weekly roundups"], [scanned.length, "items scanned"], [Math.round(100 * canada / scanned.length) + "%", "Canadian items"],
      [ukeu, "UK / EU items"], [srcCount, "sources tracked"], [feedInfo?.items?.length ?? 0, "feed posts (60 days)"],
    ].map(([n, l]) => `<div class="card stat"><div class="n">${n}</div><div class="l">${l}</div></div>`).join("");

    // theme bars
    const g = {}; scanned.forEach(i => { const k = groupOf(i); g[k] = (g[k] || 0) + 1; });
    const max = Math.max(...Object.values(g));
    $("#themes").innerHTML = Object.entries(GROUPS).map(([k, v]) => `
      <div class="row"><span>${v.label}</span><div class="track"><div class="fill" style="width:${100 * (g[k] || 0) / max}%;background:${v.color}"></div></div><span class="mono">${g[k] || 0}</span></div>`).join("");

    // weekly sparkline
    const ix = [...index].reverse();
    const W = 600, H = 64, mx = Math.max(...ix.map(x => x.count), 1);
    const pts = ix.map((x, i) => `${(i / (ix.length - 1)) * W},${H - 6 - (x.count / mx) * (H - 14)}`).join(" ");
    $("#spark").innerHTML = `<svg class="spark" viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" role="img" aria-label="Items per week">
      <polyline points="0,${H} ${pts} ${W},${H}" fill="color-mix(in srgb, var(--accent) 14%, transparent)" stroke="none"/>
      <polyline points="${pts}" fill="none" stroke="var(--accent)" stroke-width="2" vector-effect="non-scaling-stroke"/></svg>
      <div class="faint" style="display:flex;justify-content:space-between"><span>${ix[0].id}</span><span>items per week</span><span>${ix[ix.length - 1].id}</span></div>`;

    // focus watchlist: most recent items per focus group
    const focus = ["indigenous", "black", "creative", "education"];
    $("#watch").innerHTML = focus.map(f => {
      const list = scanned.filter(i => groupOf(i) === f).slice(0, 3);
      return `<div class="card"><h3 style="color:${GROUPS[f].color}">${GROUPS[f].label}</h3>${list.map(i => `<div class="item"><a class="tt" href="${esc(i.url)}" target="_blank" rel="noopener">${esc(i.title)}</a><div class="meta">${esc(i.publisher)} · ${fmtDate(i.date)}</div></div>`).join("")}<a href="roundups.html?topic=${f}" class="faint">More →</a></div>`;
    }).join("");
  }

  async function roundups() {
    const { items, index, byId } = await loadAll();
    const qs = new URLSearchParams(location.search);
    const view = qs.get("week") ? "weeks" : (store.get("rview") || "weeks");
    const scanned = items.filter(i => i.week || i.via !== "research");

    // controls
    const regions = [...new Set(items.map(i => i.region).filter(Boolean))].sort();
    const kinds = [...new Set(items.map(i => i.kind).filter(Boolean))].sort();
    $("#fGroup").innerHTML = `<option value="">All themes</option>` + Object.entries(GROUPS).map(([k, v]) => `<option value="${k}">${v.label}</option>`).join("");
    $("#fRegion").innerHTML = `<option value="">All regions</option>` + regions.map(r => `<option>${esc(r)}</option>`).join("");
    $("#fKind").innerHTML = `<option value="">All types</option>` + kinds.map(r => `<option>${esc(r)}</option>`).join("");
    $("#fWeek").innerHTML = `<option value="">All weeks</option>` + index.map(r => `<option value="${r.id}">${r.id} · ${fmtRange(r.start, r.end)}</option>`).join("");
    if (qs.get("topic")) $("#fGroup").value = qs.get("topic");
    if (qs.get("week")) $("#fWeek").value = qs.get("week");
    if (qs.get("q")) $("#q").value = qs.get("q");

    let sort = { k: "date", dir: -1 };
    const match = i => {
      const q = $("#q").value.trim().toLowerCase();
      if (q && !(`${i.title} ${i.summary} ${i.publisher} ${(i.topics || []).join(" ")}`.toLowerCase().includes(q))) return false;
      if ($("#fGroup").value && !(i.topics || []).some(t => TOPIC_GROUP[t] === $("#fGroup").value)) return false;
      if ($("#fRegion").value && i.region !== $("#fRegion").value) return false;
      if ($("#fKind").value && i.kind !== $("#fKind").value) return false;
      if ($("#fWeek").value && i.week !== $("#fWeek").value) return false;
      return true;
    };

    const renderTable = () => {
      const rows = scanned.filter(match).sort((a, b) => {
        const A = (a[sort.k] || "").toString().toLowerCase(), B = (b[sort.k] || "").toString().toLowerCase();
        return A < B ? -sort.dir : A > B ? sort.dir : 0;
      });
      $("#count").textContent = `${rows.length} item${rows.length === 1 ? "" : "s"}`;
      $("#tbody").innerHTML = rows.map(i => `<tr>
        <td class="date">${esc(i.date || "")}</td>
        <td><a href="${esc(i.url)}" target="_blank" rel="noopener"><strong>${esc(i.title)}</strong></a><div class="faint">${esc(i.summary)}</div></td>
        <td>${esc(i.publisher)}</td><td>${esc(i.region)}</td><td>${esc(i.kind)}</td>
        <td><div class="chips">${(i.topics || []).slice(0, 4).map(chip).join("")}</div></td>
        <td class="mono">${i.week ? `<a href="roundups.html?week=${i.week}">${i.week.replace("2026-", "")}</a>` : "—"}</td></tr>`).join("");
    };
    const renderWeeks = async () => {
      const want = $("#fWeek").value;
      const list = want ? index.filter(r => r.id === want) : index;
      const full = await Promise.all(list.map(r => loadRoundup(r.id)));
      const html = full.map(r => {
        const its = r.item_ids.map(id => byId[id]).filter(Boolean).filter(match);
        if (!its.length && ($("#q").value || $("#fGroup").value || $("#fRegion").value || $("#fKind").value)) return "";
        return `<article class="card rcard" id="${r.id}" style="margin-bottom:16px">
          <div class="wk"><b>${r.id.replace("2026-", "")}</b>${fmtRange(r.start, r.end)}<br><span class="faint">${r.item_ids.length} item${r.item_ids.length === 1 ? "" : "s"}</span>${r.generated_by && r.generated_by !== "backfill-research" ? `<br><span class="chip">${esc(r.generated_by)}</span>` : ""}</div>
          <div><h3 style="margin-top:0">${esc(r.headline)}</h3><p class="muted">${esc(r.digest)}</p>
          <details${want ? " open" : ""}><summary class="faint" style="cursor:pointer">Show ${its.length} item${its.length === 1 ? "" : "s"}</summary>${its.map(itemHTML).join("")}</details></div></article>`;
      }).join("");
      $("#weeks").innerHTML = html || `<p class="notice">No roundups match these filters.</p>`;
      $("#count").textContent = `${full.length} roundup${full.length === 1 ? "" : "s"}`;
    };
    const render = () => (curView === "table" ? renderTable() : renderWeeks());
    let curView = view;
    const setView = v => {
      curView = v; store.set("rview", v);
      document.querySelectorAll(".tabs button").forEach(b => b.setAttribute("aria-selected", b.dataset.v === v));
      $("#tableView").hidden = v !== "table"; $("#weeks").hidden = v !== "weeks";
      render();
    };
    document.querySelectorAll(".tabs button").forEach(b => (b.onclick = () => setView(b.dataset.v)));
    ["#q", "#fGroup", "#fRegion", "#fKind", "#fWeek"].forEach(s => $(s).addEventListener("input", render));
    document.querySelectorAll("th[data-k]").forEach(th => th.onclick = () => {
      sort = { k: th.dataset.k, dir: sort.k === th.dataset.k ? -sort.dir : 1 }; renderTable();
    });
    $("#csv").onclick = () => {
      const rows = scanned.filter(match);
      const cols = ["date", "title", "publisher", "region", "kind", "topics", "week", "url", "summary"];
      const csv = [cols.join(",")].concat(rows.map(r => cols.map(c => `"${String(Array.isArray(r[c]) ? r[c].join("; ") : r[c] ?? "").replace(/"/g, '""')}"`).join(","))).join("\n");
      const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([csv], { type: "text/csv" })); a.download = "stem-ai-scope-items.csv"; a.click();
    };
    setView(view);
    if (qs.get("week")) setTimeout(() => document.getElementById(qs.get("week"))?.scrollIntoView({ behavior: "smooth" }), 300);
  }

  async function timeline() {
    const { index, byId } = await loadAll();
    const ix = [...index].reverse();
    const full = await Promise.all(ix.map(r => loadRoundup(r.id)));

    // heat strip: weeks x theme groups
    const groups = Object.keys(GROUPS);
    const cw = 30, ch = 22, lw = 170, top = 34;
    const W = lw + full.length * cw + 10, H = top + groups.length * ch + 10;
    const counts = full.map(r => { const c = {}; r.item_ids.forEach(id => { const it = byId[id]; if (it) (it.topics || []).forEach(t => { const g = TOPIC_GROUP[t]; if (g) c[g] = (c[g] || 0) + 1; }); }); return c; });
    const mx = Math.max(1, ...counts.flatMap(c => Object.values(c)));
    let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" role="img" aria-label="Theme intensity by week">`;
    full.forEach((r, i) => {
      if (i % 2 === 0) svg += `<text x="${lw + i * cw + cw / 2}" y="16" font-size="10" text-anchor="middle" fill="var(--ink-faint)" font-family="var(--mono)">${r.id.slice(6)}</text>`;
      if (r.start.endsWith("-01") || i === 0 || r.start.slice(5, 7) !== full[i - 1].start.slice(5, 7)) svg += `<text x="${lw + i * cw + 2}" y="28" font-size="10" fill="var(--ink-soft)">${MONTHS[+r.start.slice(5, 7) - 1].slice(0, 3)}</text>`;
    });
    groups.forEach((g, j) => {
      svg += `<text x="0" y="${top + j * ch + 15}" font-size="12" fill="var(--ink-soft)">${GROUPS[g].label}</text>`;
      full.forEach((r, i) => {
        const v = counts[i][g] || 0;
        const rad = v ? 3 + 7 * Math.sqrt(v / mx) : 1.5;
        svg += `<a href="#${r.id}"><circle cx="${lw + i * cw + cw / 2}" cy="${top + j * ch + 11}" r="${rad}" fill="${GROUPS[g].color}" opacity="${v ? 0.85 : 0.2}"><title>${GROUPS[g].label} · ${r.id}: ${v}</title></circle></a>`;
      });
    });
    $("#heat").innerHTML = svg + "</svg>";

    // filter chips
    const active = new Set();
    $("#tlChips").innerHTML = Object.entries(GROUPS).map(([k, v]) => `<button class="chip" aria-pressed="false" data-g="${k}" style="color:${v.color}"><span class="dot"></span>${v.label}</button>`).join("");
    const apply = () => document.querySelectorAll(".tl-row").forEach(r => r.classList.toggle("dim", active.size > 0 && !r.dataset.gs.split(" ").some(g => active.has(g))));
    document.querySelectorAll("#tlChips button").forEach(b => b.onclick = () => {
      const g = b.dataset.g; active.has(g) ? active.delete(g) : active.add(g);
      b.setAttribute("aria-pressed", active.has(g)); apply();
    });

    // spine
    let side = 0;
    $("#tl").innerHTML = full.reverse().map(r => {
      const its = r.item_ids.map(id => byId[id]).filter(Boolean);
      return `<section class="tl-week" id="${r.id}"><span class="badge">${r.id} · ${fmtRange(r.start, r.end)}</span><span class="hl">${esc(r.headline)}</span></section>` +
        (its.length ? its.map(it => {
          const g = groupOf(it), gs = [...new Set((it.topics || []).map(t => TOPIC_GROUP[t]).filter(Boolean))].join(" ");
          side ^= 1;
          return `<div class="tl-row ${side ? "l" : "r"}" data-gs="${gs}" style="--c:${GROUPS[g].color}"><span class="node"></span>
            <div class="card"><div class="faint">${fmtDate(it.date)} · ${esc(it.publisher)}</div>
            <a class="tt" href="${esc(it.url)}" target="_blank" rel="noopener">${esc(it.title)}</a>
            <p>${esc(it.summary)}</p><div class="chips">${(it.topics || []).slice(0, 4).map(chip).join("")}</div></div></div>`;
        }).join("") : `<div class="tl-empty">No verified items this week.</div>`);
    }).join("");
  }

  async function doc() {
    const src = document.body.dataset.src;
    const text = await (await fetch(src, { cache: "no-cache" })).text();
    $("#doc").innerHTML = md(text);
    const hs = [...document.querySelectorAll("#doc h2")];
    const words = text.replace(/[#>*|\-\[\]()]/g, " ").split(/\s+/).filter(Boolean).length;
    $("#toc").innerHTML = `<div class="faint" style="margin-bottom:8px">≈ ${Math.round(words / 10) * 10} words · ${Math.max(1, Math.round(words / 230))} min read</div>` +
      hs.map(h => `<a href="#${h.id}">${h.textContent}</a>`).join("");
  }

  async function bibliography() {
    const { items } = await loadAll();
    let lit = [];
    try { lit = (await getJSON("data/literature.json")).items; } catch {}
    const scan = [...items].sort((a, b) => sortKey(a).localeCompare(sortKey(b)) || (a.date || "").localeCompare(b.date || ""));
    const litHTML = lit.map(l => `<li>${md(l.apa).replace(/^<p>|<\/p>$/g, "")}${l.url ? ` <a href="${esc(l.url)}">${esc(l.url)}</a>` : ""}</li>`).join("");
    $("#bibScan").innerHTML = scan.map(i => `<li>${apa(i)}</li>`).join("");
    $("#bibLit").innerHTML = litHTML;
    $("#bibCount").textContent = `${scan.length + lit.length} references (${scan.length} from the scan, ${lit.length} foundational works).`;
    $("#copyBib").onclick = async () => {
      const t = [...document.querySelectorAll(".bib li")].map(li => li.innerText).join("\n\n");
      try { await navigator.clipboard.writeText(t); $("#copyBib").textContent = "Copied ✓"; } catch { $("#copyBib").textContent = "Copy failed"; }
    };
  }

  async function feed() {
    let f = { items: [] }, cfg = { categories: {} };
    try { f = await getJSON("data/feed.json"); } catch {}
    try { cfg = await getJSON("data/sources.json"); } catch {}
    $("#feedMeta").textContent = f.generated ? `Last harvested ${new Date(f.generated).toLocaleString()} · ${f.items.length} posts from the last 60 days` : "The feed has not been harvested yet.";
    if (!f.items.length) {
      $("#feedList").innerHTML = `<div class="notice">No posts yet. The GitHub Action <code>Harvest feeds &amp; weekly scan</code> fills this page every day; it runs automatically after the first push, or you can run <code>python scripts/harvest_feeds.py</code> locally.</div>`;
      return;
    }
    const cats = Object.entries(cfg.categories);
    let cat = "";
    $("#feedChips").innerHTML = `<button class="chip" aria-pressed="true" data-c="">All</button>` + cats.map(([k, v]) => `<button class="chip" aria-pressed="false" data-c="${k}">${esc(v)}</button>`).join("");
    const draw = () => {
      const q = $("#fq").value.toLowerCase();
      const list = f.items.filter(i => (!cat || i.category === cat) && (!q || `${i.title} ${i.summary} ${i.source_name}`.toLowerCase().includes(q)));
      $("#feedList").innerHTML = list.slice(0, 300).map(i => `<article class="card">
        <div class="faint">${esc(i.source_name)} · ${i.date ? fmtDate(i.date) : ""} ${i.type === "youtube" ? "· ▶ video" : i.type === "bluesky" ? "· 🦋 post" : ""}</div>
        <a class="tt" style="font-weight:600;color:var(--ink);text-decoration:none" href="${esc(i.url)}" target="_blank" rel="noopener">${esc(i.title)}</a>
        <p class="muted" style="font-size:.92rem;margin:.4em 0 0">${esc(i.summary)}</p></article>`).join("") || `<p class="notice">Nothing matches.</p>`;
    };
    document.querySelectorAll("#feedChips button").forEach(b => b.onclick = () => {
      cat = b.dataset.c; document.querySelectorAll("#feedChips button").forEach(x => x.setAttribute("aria-pressed", x === b)); draw();
    });
    $("#fq").oninput = draw;
    draw();
  }

  async function sources() {
    const cfg = await getJSON("data/sources.json");
    let st = { sources: {} };
    try { st = await getJSON("data/feed_status.json"); } catch {}
    $("#srcMeta").textContent = st.generated ? `Feed status from the harvest at ${new Date(st.generated).toLocaleString()}.` : "Feed status appears after the first automated harvest.";
    $("#srcList").innerHTML = Object.entries(cfg.categories).map(([k, label]) => {
      const list = cfg.sources.filter(s => s.category === k);
      if (!list.length) return "";
      return `<h2>${esc(label)} <span class="faint">(${list.length})</span></h2><div class="table-wrap"><table><thead><tr><th>Source</th><th>Region</th><th>Type</th><th>Feed</th></tr></thead><tbody>` +
        list.map(s => {
          const x = st.sources[s.id];
          const status = s.feed === null ? `<span class="status-link">link only</span>` : !x ? `<span class="faint">pending</span>` :
            x.status === "ok" ? `<span class="status-ok">● ${x.count} recent</span>${x.feed ? ` <a class="faint" href="${esc(x.feed)}">feed</a>` : ""}` : `<span class="status-error" title="${esc(x.error || "")}">● not reachable</span>`;
          return `<tr><td><a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.name)}</a></td><td>${esc(s.region)}</td><td>${esc(s.type)}</td><td>${status}</td></tr>`;
        }).join("") + `</tbody></table></div>`;
    }).join("");
  }

  // ---------- boot ----------
  chrome();
  const page = document.body.dataset.page;
  const run = { home, roundups, timeline, doc, bibliography, feed, sources }[page];
  if (run) run().catch(e => {
    console.error(e);
    const main = document.querySelector("main");
    main?.insertAdjacentHTML("afterbegin", `<div class="wrap"><p class="notice">Could not load data (${esc(e.message)}). If you opened this file directly, serve the folder instead: <code>python -m http.server</code>.</p></div>`);
  });
})();
