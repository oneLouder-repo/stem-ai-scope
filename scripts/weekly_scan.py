#!/usr/bin/env python3
"""Build a weekly roundup from the harvested feeds.

Run after scripts/harvest_feeds.py. It:
  1. picks the target week (default: the most recent complete Monday–Sunday week),
  2. filters data/feed.json to items published that week that match the scan scope
     (AI + education / community / ethics / Indigenous / Black / creative / policy),
  3. scores them (Canada first, UK/EU second) and keeps the top N,
  4. optionally asks Claude to write the digest and tidy summaries
     (only if ANTHROPIC_API_KEY is set; otherwise a plain digest is generated),
  5. writes data/roundups/<YYYY-Www>.json, appends new items to data/items.json
     and refreshes data/roundups/index.json.

Nothing is invented: every item in a roundup comes from a harvested feed entry
with its original link. If a week has no matching items the roundup says so.

Usage:  python scripts/weekly_scan.py [--week 2026-W47] [--max 15] [--force]
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RDIR = DATA / "roundups"

AI_RE = re.compile(r"\b(AI|A\.I\.|IA|artificial intelligence|intelligence artificielle|machine learning|"
                   r"generative|genAI|LLMs?|large language model|chatbot|ChatGPT|algorithm\w*|neural|"
                   r"deep learning|data science|automation)\b", re.I)

TOPICS = {
    "policy": r"strategy|policy|minister|government|regulat|legislat|act\b|parliament|federal|provinc|white paper|consultation",
    "funding": r"fund|invest|grant|\$\d|£\d|€\d|million|billion|budget",
    "education-k12": r"\bK-?12\b|school|classroom|pupil|student|curriculum|teacher|primary|secondary|élève",
    "post-secondary": r"universit|college|post-secondary|postsecondary|higher education|campus|faculty",
    "adult-education": r"adult|lifelong|upskill|reskill|workforce training|community learning|literacy course",
    "teachers": r"teacher|educator|instructor|pedagog|professional development|enseignant",
    "ethics": r"ethic|bias|fairness|harm|rights|accountab|responsible|justice|surveillance",
    "safety": r"safety|risk|alignment|trust",
    "indigenous": r"indigenous|first nations|inuit|métis|metis|anishinaabe|cree|mi'kmaq|māori|maori|autochtone|land-based|data sovereignty|ocap",
    "black-communities": r"\bblack\b|african|caribbean|afro|diaspora",
    "afrofuturism": r"afrofutur|afro-futur|black futures|speculative",
    "indigenous-futurism": r"indigenous futur|indigenous sci|skawennati|future ancestral",
    "creative": r"\bart\b|artist|creative|music|design|film|museum|gallery|culture|storytell",
    "community": r"community|communities|public engagement|citizen|nonprofit|non-profit|grassroots|civic",
    "research": r"research|study|report|paper|journal|survey|findings|evidence",
    "stem-outreach": r"\bSTEM\b|STEAM|coding|outreach|camp|hackathon|maker|robotics|girls|youth program",
    "youth": r"youth|young people|teen|children|kids|girls|boys|jeunes",
    "literacy": r"literacy|littératie|AI skills|digital skills",
    "workforce": r"jobs?\b|workforce|labour|labor|employ|career|apprentice|skills",
}
TOPIC_RE = {k: re.compile(v, re.I) for k, v in TOPICS.items()}
FOCUS = {"education-k12": 3, "teachers": 3, "stem-outreach": 3, "indigenous": 3, "black-communities": 3,
         "afrofuturism": 3, "indigenous-futurism": 3, "literacy": 3, "adult-education": 2, "youth": 2,
         "creative": 2, "community": 2, "ethics": 2, "post-secondary": 1, "policy": 1, "funding": 1,
         "research": 1, "workforce": 1, "safety": 1}
REGION_W = {"Canada": 3, "UK": 2, "EU": 2}
AI_NATIVE = {"institute", "community", "video"}


def iso_week_bounds(week_id):
    y, w = week_id.split("-W")
    start = dt.date.fromisocalendar(int(y), int(w), 1)
    return start, start + dt.timedelta(days=6)


def default_week(today=None):
    today = today or dt.date.today()
    last_sunday = today - dt.timedelta(days=today.isoweekday() % 7 or 7) if today.isoweekday() != 7 else today
    y, w, _ = last_sunday.isocalendar()
    return f"{y}-W{w:02d}"


def item_id(url):
    return hashlib.sha1(url.encode()).hexdigest()[:10]


def score(it):
    blob = f"{it['title']} {it.get('summary','')}"
    if it.get("category") not in AI_NATIVE and not AI_RE.search(blob):
        return 0, []
    topics = [k for k, rx in TOPIC_RE.items() if rx.search(blob)]
    s = 1 + sum(FOCUS.get(t, 0) for t in topics)
    for reg, w in REGION_W.items():
        if reg in (it.get("region") or ""):
            s += w
            break
    return s, topics


def claude_polish(week_id, items):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key or not items:
        return None
    model = os.environ.get("SCAN_MODEL", "claude-sonnet-5-5")
    listing = "\n".join(f"[{i}] {it['title']} | {it['publisher']} | {it['region']} | {it['date']} | {it['url']}\n    {it['summary']}"
                        for i, it in enumerate(items))
    prompt = (
        "You edit STEM AI Scope, a weekly landscape scan for a Canadian youth STEM outreach charity's AI strategy lead. "
        "Scope: AI think tanks, innovation hubs, public education institutes and public-facing university AI labs; "
        "community uses, ethics, academic literature, STEM promotion, creative methods, Afrofuturism, Indigenous futurism, "
        "Indigenous and Black AI projects, publicly funded AI, pedagogy/curriculum, adult education, STEM instructors. "
        "Canada first, UK/EU second.\n\n"
        f"Candidate items for {week_id} (from RSS feeds):\n{listing}\n\n"
        "Return ONLY JSON: {\"headline\": str (max 12 words), \"digest\": str (120-180 words, plain prose, only facts in the items), "
        "\"keep\": [{\"i\": int, \"summary\": str (max 40 words, factual, from the item text only), \"topics\": [str]}]} . "
        "Drop items that are off-scope. Never add facts that are not in the item text."
    )
    body = json.dumps({"model": model, "max_tokens": 2500, "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={
        "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            resp = json.loads(r.read())
        txt = "".join(b.get("text", "") for b in resp.get("content", []))
        return json.loads(txt[txt.find("{"): txt.rfind("}") + 1])
    except Exception as e:
        print(f"Claude polish skipped: {e}", file=sys.stderr)
        return None


def rebuild_index(items_by_id):
    idx = []
    for f in sorted(RDIR.glob("20*-W*.json")):
        r = json.loads(f.read_text())
        topics = Counter(t for iid in r["item_ids"] for t in items_by_id.get(iid, {}).get("topics", []))
        idx.append({"id": r["id"], "start": r["start"], "end": r["end"], "headline": r["headline"],
                    "count": len(r["item_ids"]), "themes": [t for t, _ in topics.most_common(4)],
                    "generated_by": r.get("generated_by", "")})
    idx.sort(key=lambda x: x["id"], reverse=True)
    (RDIR / "index.json").write_text(json.dumps(idx, indent=1, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--week", default=None)
    ap.add_argument("--max", type=int, default=15)
    ap.add_argument("--force", action="store_true", help="overwrite an existing roundup for that week")
    ap.add_argument("--reindex", action="store_true", help="only rebuild data/roundups/index.json")
    a = ap.parse_args()

    store = json.loads((DATA / "items.json").read_text())
    by_id = {it["id"]: it for it in store["items"]}
    if a.reindex:
        rebuild_index(by_id)
        return

    week = a.week or default_week()
    out = RDIR / f"{week}.json"
    if out.exists() and not a.force:
        print(f"{week} already exists; use --force to rebuild", file=sys.stderr)
        rebuild_index(by_id)
        return
    start, end = iso_week_bounds(week)
    feed = json.loads((DATA / "feed.json").read_text())["items"]

    seen_urls = {it["url"] for it in store["items"]}
    cands = []
    for it in feed:
        if not it.get("date"):
            continue
        d = dt.date.fromisoformat(it["date"][:10])
        if not (start <= d <= end) or it["url"] in seen_urls:
            continue
        s, topics = score(it)
        if s >= 4:
            cands.append((s, {
                "id": item_id(it["url"]), "url": it["url"], "title": it["title"],
                "publisher": it["source_name"], "author": "", "date": d.isoformat(),
                "summary": it.get("summary", ""), "topics": topics[:5], "region": it.get("region", ""),
                "kind": "video" if it.get("type") == "youtube" else ("social" if it.get("type") == "bluesky" else "news"),
                "week": week, "via": "feed"}))
            seen_urls.add(it["url"])
    cands.sort(key=lambda x: (-x[0], x[1]["date"]))
    picked = [c for _, c in cands[: a.max * 2]]

    polished = claude_polish(week, picked)
    if polished and polished.get("keep"):
        kept = []
        for k in polished["keep"]:
            if 0 <= k.get("i", -1) < len(picked):
                it = picked[k["i"]]
                it["summary"] = k.get("summary") or it["summary"]
                it["topics"] = [t for t in k.get("topics", []) if t in TOPICS] or it["topics"]
                kept.append(it)
        picked = kept[: a.max]
        headline, digest, gen = polished.get("headline", ""), polished.get("digest", ""), "auto-claude"
    else:
        picked = picked[: a.max]
        top = Counter(t for it in picked for t in it["topics"]).most_common(3)
        headline = (f"{len(picked)} signals: " + ", ".join(t for t, _ in top)) if picked else "Quiet week"
        digest = ("Automated scan of the listed feeds. Highest-scoring items this week: " +
                  "; ".join(f"{it['title']} ({it['publisher']})" for it in picked[:5]) + ".") if picked else \
                 "No in-scope items were found in the harvested feeds for this week."
        gen = "auto-feeds"

    for it in picked:
        store["items"].append(it)
        by_id[it["id"]] = it
    roundup = {"id": week, "start": start.isoformat(), "end": end.isoformat(), "headline": headline,
               "digest": digest, "item_ids": [it["id"] for it in picked], "generated_by": gen,
               "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
    out.write_text(json.dumps(roundup, indent=1, ensure_ascii=False))
    store["items"].sort(key=lambda x: x.get("date") or "", reverse=True)
    (DATA / "items.json").write_text(json.dumps(store, indent=1, ensure_ascii=False))
    rebuild_index(by_id)
    print(f"wrote {out.name} with {len(picked)} items ({gen})", file=sys.stderr)


if __name__ == "__main__":
    main()
