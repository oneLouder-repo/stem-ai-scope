#!/usr/bin/env python3
"""One-off: turn the verified backfill research into data/items.json + data/roundups/*.json.
Safe to re-run; it rewrites only 'research' items and backfill roundups (W20–W46 2026)."""
import datetime as dt, hashlib, json, runpy, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
here = Path(__file__).parent
I = runpy.run_path(str(here / "research_items.py"))["I"]
N = runpy.run_path(str(here / "roundup_notes.py"))["N"]
OVERRIDE = {"2026-08": "2026-W35", "2026-11": "2026-W45"}
START, END = dt.date(2026, 5, 11), dt.date(2026, 11, 15)

def wk(d):
    y, w, _ = d.isocalendar(); return f"{y}-W{w:02d}"

items_path = ROOT / "data/items.json"
existing = json.loads(items_path.read_text())["items"] if items_path.exists() else []
keep = [x for x in existing if x.get("via") != "research"]
out = []
for it in I:
    week = None
    d = it["date"]
    if not it["background"]:
        if len(d) == 10 and START <= dt.date.fromisoformat(d) <= END:
            week = wk(dt.date.fromisoformat(d))
        elif d in OVERRIDE:
            week = OVERRIDE[d]
    out.append({"id": hashlib.sha1(it["url"].encode()).hexdigest()[:10], **{k: it[k] for k in
               ("url","title","publisher","author","date","summary","topics","region","kind")},
               "week": week, "background": it["background"], "via": "research"})
allitems = keep + out
allitems.sort(key=lambda x: x.get("date") or "", reverse=True)
items_path.write_text(json.dumps({"items": allitems}, indent=1, ensure_ascii=False))

rdir = ROOT / "data/roundups"; rdir.mkdir(exist_ok=True)
for week_id, (headline, digest) in N.items():
    y, w = week_id.split("-W")
    s = dt.date.fromisocalendar(int(y), int(w), 1)
    ids = [x["id"] for x in sorted(out, key=lambda x: x["date"]) if x["week"] == week_id]
    (rdir / f"{week_id}.json").write_text(json.dumps({
        "id": week_id, "start": s.isoformat(), "end": (s + dt.timedelta(days=6)).isoformat(),
        "headline": headline, "digest": digest, "item_ids": ids,
        "generated_by": "backfill-research", "generated_at": "2026-11-15T00:00:00+00:00"}, indent=1, ensure_ascii=False))
import weekly_scan
weekly_scan.rebuild_index({x["id"]: x for x in allitems})
print(len(allitems), "items;", len(N), "roundups")
