#!/usr/bin/env python3
"""Harvest every source in data/sources.json into data/feed.json.

Standard library only, so it runs anywhere (GitHub Actions, a laptop, a cron box).

- RSS 2.0, RSS 1.0/RDF and Atom are supported.
- If a source has no 'feed' (or it fails), the homepage is fetched and the
  <link rel="alternate" type="application/rss+xml|atom+xml"> is auto-discovered.
- YouTube handles (@name) are resolved to a channel id and read from
  https://www.youtube.com/feeds/videos.xml?channel_id=...
- Bluesky handles are read from https://bsky.app/profile/<handle>/rss
- Per-source status (ok / error message, item count, resolved feed URL) is
  written to data/feed_status.json so the Sources page can show what works.

Usage:  python scripts/harvest_feeds.py [--days 60] [--max-per-source 15]
"""
import argparse
import datetime as dt
import email.utils
import html
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
UA = "Mozilla/5.0 (compatible; STEM-AI-Scope feed reader; +https://github.com/)"
TIMEOUT = 25

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "rss1": "http://purl.org/rss/1.0/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "media": "http://search.yahoo.com/mrss/",
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read(), r.geturl(), r.headers.get("Content-Type", "")


def strip_html(s, limit=320):
    s = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s or "", flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(re.sub(r"\s+", " ", s)).strip()
    return (s[: limit - 1] + "…") if len(s) > limit else s


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    try:
        d = email.utils.parsedate_to_datetime(s)
    except (TypeError, ValueError):
        d = None
    if d is None:
        try:
            d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            m = re.match(r"(\d{4}-\d{2}-\d{2})", s)
            if not m:
                return None
            d = dt.datetime.fromisoformat(m.group(1))
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d.astimezone(dt.timezone.utc)


def text(el, path):
    if el is None:
        return ""
    found = el.find(path, NS)
    return (found.text or "").strip() if found is not None and found.text else ""


def parse_feed(raw):
    root = ET.fromstring(raw)
    tag = root.tag.lower()
    items = []
    if tag.endswith("rss"):
        for it in root.iter("item"):
            items.append({
                "title": text(it, "title"),
                "link": text(it, "link") or text(it, "guid"),
                "date": parse_date(text(it, "pubDate") or text(it, "dc:date")),
                "summary": strip_html(text(it, "description") or text(it, "content:encoded")),
            })
    elif tag.endswith("feed"):
        for it in root.findall("atom:entry", NS):
            link = ""
            for l in it.findall("atom:link", NS):
                if l.get("rel", "alternate") == "alternate":
                    link = l.get("href", "")
                    break
            summ = text(it, "atom:summary") or text(it, "atom:content")
            if not summ:
                summ = text(it, "media:group/media:description")
            items.append({
                "title": text(it, "atom:title"),
                "link": link,
                "date": parse_date(text(it, "atom:published") or text(it, "atom:updated")),
                "summary": strip_html(summ),
            })
    elif tag.endswith("rdf"):
        for it in root.findall("rss1:item", NS):
            items.append({
                "title": text(it, "rss1:title"),
                "link": text(it, "rss1:link"),
                "date": parse_date(text(it, "dc:date")),
                "summary": strip_html(text(it, "rss1:description")),
            })
    else:
        raise ValueError("not an RSS/Atom document")
    return items


def discover(page_url):
    raw, final, _ = fetch(page_url)
    doc = raw.decode("utf-8", "ignore")
    for m in re.finditer(r"<link[^>]+>", doc, flags=re.I):
        tag = m.group(0)
        if re.search(r"rel=[\"']?alternate", tag, re.I) and re.search(r"(rss|atom)\+xml", tag, re.I):
            href = re.search(r"href=[\"']([^\"']+)", tag, re.I)
            if href:
                return urllib.parse.urljoin(final, html.unescape(href.group(1)))
    return None


def youtube_feed(handle):
    if handle.startswith("UC"):
        return f"https://www.youtube.com/feeds/videos.xml?channel_id={handle}"
    raw, _, _ = fetch(f"https://www.youtube.com/{handle}")
    doc = raw.decode("utf-8", "ignore")
    m = re.search(r'"(?:channelId|externalId)":"(UC[\w-]{20,})"', doc) or re.search(r"channel/(UC[\w-]{20,})", doc)
    if not m:
        raise ValueError("could not resolve YouTube channel id")
    return f"https://www.youtube.com/feeds/videos.xml?channel_id={m.group(1)}"


def candidates(src):
    if src.get("youtube"):
        yield youtube_feed(src["youtube"])
        return
    if src.get("bluesky"):
        yield f"https://bsky.app/profile/{src['bluesky']}/rss"
        return
    if src.get("feed"):
        yield src["feed"]
    if src.get("url"):
        d = discover(src["url"])
        if d:
            yield d


def harvest_one(src, since, max_items):
    if src.get("feed", "") is None:
        return src["id"], [], {"status": "link-only", "feed": None, "count": 0}
    errors = []
    try:
        for url in candidates(src):
            try:
                raw, _, _ = fetch(url)
                items = parse_feed(raw)
            except Exception as e:  # try next candidate
                errors.append(f"{url}: {e}")
                continue
            out = []
            for it in items:
                if not it["title"] or not it["link"]:
                    continue
                if it["date"] and it["date"] < since:
                    continue
                out.append({
                    "source": src["id"],
                    "source_name": src["name"],
                    "category": src.get("category", ""),
                    "region": src.get("region", ""),
                    "type": src.get("type", "blog"),
                    "title": strip_html(it["title"], 200),
                    "url": it["link"],
                    "date": it["date"].isoformat() if it["date"] else None,
                    "summary": it["summary"],
                })
            out.sort(key=lambda x: x["date"] or "", reverse=True)
            return src["id"], out[:max_items], {"status": "ok", "feed": url, "count": len(out[:max_items])}
    except Exception as e:
        errors.append(str(e))
    return src["id"], [], {"status": "error", "feed": src.get("feed") or None, "count": 0,
                            "error": "; ".join(errors)[:400] or "no feed found"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--max-per-source", type=int, default=15)
    a = ap.parse_args()
    cfg = json.loads((DATA / "sources.json").read_text())
    since = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=a.days)
    feed, status = [], {}
    with ThreadPoolExecutor(max_workers=12) as ex:
        for sid, items, st in ex.map(lambda s: harvest_one(s, since, a.max_per_source), cfg["sources"]):
            feed.extend(items)
            status[sid] = st
    feed.sort(key=lambda x: x["date"] or "", reverse=True)
    now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    (DATA / "feed.json").write_text(json.dumps({"generated": now, "items": feed}, indent=1, ensure_ascii=False))
    (DATA / "feed_status.json").write_text(json.dumps({"generated": now, "sources": status}, indent=1, ensure_ascii=False))
    ok = sum(1 for s in status.values() if s["status"] == "ok")
    print(f"harvested {len(feed)} items; {ok}/{len(status)} sources ok", file=sys.stderr)


if __name__ == "__main__":
    main()
